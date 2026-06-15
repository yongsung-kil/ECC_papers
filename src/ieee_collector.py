"""IEEE Xplore LDPC 논문 수집기 (REST 검색 기반).

IEEE Xplore 내부 REST 검색 endpoint(`/rest/search`)를 사용한다. 검색 응답에
abstract(약 400자 미리보기)가 포함되므로 개별 페이지 크롤링 없이 메타데이터+초록을
한 번에 받는다. 결과량이 많아(LDPC 전체 ≈ 1.8만건) 연도별 버킷으로 쪼개고,
버킷마다 독립 커서로 `pageNumber` 페이지네이션을 돌려 이어받는다.

NOTE: full abstract(전체 초록)가 필요하면 Phase 3에서 개별 페이지를 별도 수집한다.
"""

import json
import logging
import time
from datetime import datetime, timezone

import requests

from src.db import (
    get_conn, init_db, insert_paper, get_cursor, set_cursor,
)

logger = logging.getLogger(__name__)

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
    "Accept": "application/json, text/plain, */*",
    "Origin": "https://ieeexplore.ieee.org",
    "Referer": "https://ieeexplore.ieee.org/search/searchresult.jsp",
    "Content-Type": "application/json",
}

SEARCH_URL = "https://ieeexplore.ieee.org/rest/search"

# 광범위 수집(arXiv와 동일 철학): LDPC 전부 취합 후 Phase 2에서 선별.
SEARCH_TERMS = [
    "LDPC",
    "low density parity check code",
]
YEAR_START = 2005  # 이 해부터 현재까지 연도별로 수집
REQUEST_DELAY = 1.5  # 요청 간 딜레이(초) — 차단 방지


def year_buckets(start: int = YEAR_START) -> list[int]:
    """수집 대상 연도 목록(최신 연도부터)."""
    now = datetime.now(timezone.utc).year
    return list(range(now, start - 1, -1))


def bucket_queries() -> list[tuple[str, int]]:
    """(term, year) 버킷 전체 — runner가 이걸 순회한다."""
    return [(term, year) for year in year_buckets() for term in SEARCH_TERMS]


def search_ieee(query: str, max_results: int = 100, page_number: int = 1,
                year: int | None = None, sort: str = "oldestfirst") -> dict:
    """IEEE Xplore REST 검색. year 지정 시 해당 연도로 한정.

    페이지네이션은 `pageNumber`로 한다(`startRecord`는 이 endpoint에서 무시됨).
    `sort='oldestfirst'`로 오래된 것부터 받아 커서가 안정적으로 전진하도록 한다.
    """
    payload = {
        "newsearch": True,
        "queryText": query,
        "returnType": "SEARCH",
        "matchPubs": True,
        "rowsPerPage": min(max_results, 100),
        "pageNumber": page_number,
        "sortType": sort,
    }
    if year is not None:
        # IEEE Xplore REST의 발행연도 범위 필터 (시작_끝_Year)
        payload["ranges"] = [f"{year}_{year}_Year"]

    time.sleep(REQUEST_DELAY)  # 차단 방지용 딜레이
    try:
        resp = requests.post(SEARCH_URL, json=payload, headers=HEADERS, timeout=30)
        resp.raise_for_status()
        return resp.json()
    except requests.exceptions.HTTPError as e:
        logger.warning("IEEE 검색 HTTP 에러: %s", e)
        return {}
    except Exception as e:
        logger.warning("IEEE 검색 실패: %s", e)
        return {}


def _content_type(rec: dict) -> str:
    """IEEE 레코드를 콘텐츠 타입으로 정규화(journal/conference/magazine/standard/book/course/other).

    displayContentType 문자열(예: 'Journal Article', 'Conference')과 is* 플래그를
    함께 보고 분류한다. 'journal article' → 'journal' 처럼 정규화한다.
    """
    dct = (rec.get("displayContentType") or "").lower()
    if "conference" in dct or rec.get("isConference"):
        return "conference"
    if "journal" in dct or rec.get("isJournal"):
        return "journal"
    if "magazine" in dct or rec.get("isMagazine"):
        return "magazine"
    if "standard" in dct or rec.get("isStandard"):
        return "standard"
    if "book" in dct or rec.get("isBook") or rec.get("isBookWithoutChapters"):
        return "book"
    if "course" in dct:
        return "course"
    return dct or "other"


def parse_search_results(data: dict) -> list[dict]:
    """검색 결과 JSON에서 논문 메타데이터(+초록)를 파싱."""
    papers = []
    for rec in data.get("records", []):
        article_number = rec.get("articleNumber", "")
        if not article_number:
            continue

        authors = []
        for author in rec.get("authors", []):
            name = author.get("preferredName") or author.get("normalizedName", "")
            if name:
                authors.append(name)

        terms = rec.get("indexTerms", {}).get("ieee", {}).get("terms", [])

        papers.append({
            "id": f"ieee:{article_number}",
            "source": "ieee",
            "title": (rec.get("articleTitle") or "")
                     .replace("<b>", "").replace("</b>", "").strip(),
            "authors": json.dumps(authors),
            "abstract": (rec.get("abstract") or "").strip() or None,
            "categories": json.dumps(terms),
            "published": rec.get("publicationDate", ""),
            "updated": None,
            "doi": rec.get("doi", ""),
            "pdf_url": f"https://ieeexplore.ieee.org/document/{article_number}",
            "content_type": _content_type(rec),
        })
    return papers


def collect_batch(term: str, year: int, batch_size: int = 100) -> dict:
    """커서 기반 1배치 수집(이어받기) — (term, year) 버킷 단위.

    버킷마다 독립 커서(`{term}#{year}`)를 두고 `pageNumber`로 이어받는다.
    검색 응답에 초록이 포함되므로 개별 페이지 크롤링은 하지 않는다.
    중복(이미 있는 ID)은 INSERT OR IGNORE로 제외한다.

    반환: {"new", "dup", "fetched", "offset", "exhausted", "total"}
    """
    cursor_key = f"{term}#{year}"
    conn = get_conn()
    init_db(conn)

    cursor = get_cursor(conn, "ieee", cursor_key)
    offset = cursor["next_offset"]

    if cursor["exhausted"]:
        conn.close()
        return {"new": 0, "dup": 0, "fetched": 0, "offset": offset,
                "exhausted": True, "total": cursor["total"]}

    page_number = offset // batch_size + 1

    logger.info("IEEE 배치 수집: '%s' year=%d page=%d (offset=%d, size=%d)",
                term, year, page_number, offset, batch_size)

    data = search_ieee(term, max_results=batch_size, page_number=page_number,
                       year=year)
    if not data:
        conn.close()
        logger.warning("IEEE 검색 결과 없음: '%s' %d", term, year)
        return {"new": 0, "dup": 0, "fetched": 0, "offset": offset,
                "exhausted": False, "total": cursor["total"]}

    total = data.get("totalRecords", 0)
    papers = parse_search_results(data)
    fetched = len(papers)

    new_count = dup_count = 0
    for paper in papers:
        if insert_paper(conn, paper):
            new_count += 1
            logger.info("[+%d] %s — %s", new_count, paper["id"], paper["title"][:60])
        else:
            dup_count += 1
    conn.commit()

    new_offset = offset + fetched
    # 끝 도달: 받은 게 batch_size 미만이거나, 다음 위치가 전체 건수 이상.
    exhausted = fetched < batch_size or (total and new_offset >= total)
    set_cursor(conn, "ieee", cursor_key, new_offset, total or None, exhausted)
    conn.close()

    logger.info("IEEE 배치 완료: 신규 %d, 중복 %d, 받음 %d/%d, 다음 offset %d%s",
                new_count, dup_count, fetched, total, new_offset,
                " (끝 도달)" if exhausted else "")

    if new_count > 0:
        from src.arxiv_collector import export_catalog
        export_catalog()

    return {"new": new_count, "dup": dup_count, "fetched": fetched,
            "offset": new_offset, "exhausted": bool(exhausted), "total": total}


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
    )
    buckets = bucket_queries()
    print(f"버킷 수: {len(buckets)} (예: {buckets[:3]} ...)")
    term, year = buckets[0]
    r = collect_batch(term, year, batch_size=10)
    print(f"\n=== IEEE 시범 수집({term} {year}): {r} ===")
