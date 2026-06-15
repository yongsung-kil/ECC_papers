"""IEEE Xplore LDPC 논문 수집기 (크롤링 방식).

IEEE Xplore 내부 REST endpoint를 활용하여 검색 결과를 가져오고,
개별 논문 페이지에서 abstract를 크롤링합니다.

NOTE: 뼈대 구현. 라이센스가 있는 네트워크에서 테스트/완성 필요.
IEEE Xplore 이용약관을 준수하여 사용하세요.
"""

import json
import logging
import time
from datetime import datetime, timezone
from pathlib import Path

import requests
from bs4 import BeautifulSoup

from src.db import (
    get_conn, init_db, insert_paper, get_cursor, set_cursor,
)

logger = logging.getLogger(__name__)

PROJECT_ROOT = Path(__file__).resolve().parent.parent
PDF_DIR = PROJECT_ROOT / "papers" / "pdfs"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
    "Accept": "application/json, text/plain, */*",
    "Origin": "https://ieeexplore.ieee.org",
    "Referer": "https://ieeexplore.ieee.org/search/searchresult.jsp",
    "Content-Type": "application/json",
}

SEARCH_URL = "https://ieeexplore.ieee.org/rest/search"
ABSTRACT_URL = "https://ieeexplore.ieee.org/document/{article_number}"

SEARCH_QUERIES = [
    "LDPC NAND",
    "LDPC flash memory",
    "LDPC decoder hardware",
    "LDPC error floor",
    "LDPC min-sum decoding",
    "low density parity check SSD",
]


def search_ieee(query: str, max_results: int = 25, start_record: int = 1) -> dict:
    """IEEE Xplore REST endpoint로 검색 요청."""
    payload = {
        "newsearch": True,
        "queryText": query,
        "highlight": True,
        "returnFacets": ["ALL"],
        "returnType": "SEARCH",
        "matchPubs": True,
        "rowsPerPage": min(max_results, 100),
        "startRecord": start_record,
    }

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


def scrape_abstract(article_number: str) -> str | None:
    """개별 논문 페이지에서 abstract를 크롤링."""
    url = ABSTRACT_URL.format(article_number=article_number)
    try:
        resp = requests.get(url, headers=HEADERS, timeout=30)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "html.parser")

        # IEEE Xplore는 JS 렌더링이 많아서 meta 태그에서 추출 시도
        meta = soup.find("meta", attrs={"property": "og:description"})
        if meta and meta.get("content"):
            return meta["content"].strip()

        # JSON-LD에서 추출 시도
        for script in soup.find_all("script", type="application/ld+json"):
            try:
                data = json.loads(script.string)
                if isinstance(data, dict) and "description" in data:
                    return data["description"].strip()
            except (json.JSONDecodeError, TypeError):
                continue

        # xplGlobal.document.metadata JS 변수에서 추출 시도
        for script in soup.find_all("script"):
            if script.string and "xplGlobal.document.metadata" in script.string:
                text = script.string
                start = text.find('"abstract":"')
                if start != -1:
                    start += len('"abstract":"')
                    end = text.find('"', start)
                    if end != -1:
                        return text[start:end].replace("\\n", " ").strip()

        logger.warning("Abstract 추출 실패: %s", url)
        return None
    except Exception as e:
        logger.warning("페이지 크롤링 실패 (%s): %s", article_number, e)
        return None


def parse_search_results(data: dict) -> list[dict]:
    """검색 결과 JSON에서 논문 메타데이터를 파싱."""
    records = data.get("records", [])
    papers = []

    for rec in records:
        article_number = rec.get("articleNumber", "")
        if not article_number:
            continue

        authors = []
        for author in rec.get("authors", []):
            name = author.get("preferredName") or author.get("normalizedName", "")
            if name:
                authors.append(name)

        paper = {
            "id": f"ieee:{article_number}",
            "source": "ieee",
            "title": (rec.get("articleTitle") or "").replace("<b>", "").replace("</b>", "").strip(),
            "authors": json.dumps(authors),
            "abstract": None,  # 별도 크롤링으로 채움
            "categories": json.dumps(rec.get("indexTerms", {}).get("ieee", {}).get("terms", [])),
            "published": rec.get("publicationDate", ""),
            "updated": None,
            "doi": rec.get("doi", ""),
            "pdf_url": f"https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber={article_number}",
            "article_number": article_number,
        }
        papers.append(paper)

    return papers


def collect_batch(
    query: str,
    batch_size: int = 100,
    fetch_abstract: bool = True,
    delay: float = 3.0,
) -> dict:
    """커서 기반 1배치 수집(이어받기).

    IEEE REST는 `startRecord`(1부터 시작) 페이지네이션과 `totalRecords`를 제공한다.
    저장된 커서(next_offset, 0-기반)를 startRecord로 변환해 이어받고, 받은 만큼
    커서를 전진시킨다. 중복(이미 있는 ID)은 INSERT OR IGNORE로 제외한다.

    반환: {"new", "dup", "fetched", "offset", "exhausted", "total"}
    """
    conn = get_conn()
    init_db(conn)

    cursor = get_cursor(conn, "ieee", query)
    offset = cursor["next_offset"]
    start_record = offset + 1  # IEEE는 1-기반

    logger.info("IEEE 배치 수집: '%s' offset=%d, size=%d", query, offset, batch_size)

    data = search_ieee(query, max_results=batch_size, start_record=start_record)
    if not data:
        conn.close()
        logger.warning("IEEE 검색 결과 없음(또는 차단): '%s'", query)
        return {"new": 0, "dup": 0, "fetched": 0, "offset": offset,
                "exhausted": False, "total": cursor["total"]}

    total = data.get("totalRecords", 0)
    papers = parse_search_results(data)
    fetched = len(papers)

    new_count = dup_count = 0
    for paper in papers:
        article_number = paper.pop("article_number")
        # 신규일 때만 abstract 크롤링(중복은 건너뛰어 트래픽 절약)
        exists = conn.execute(
            "SELECT 1 FROM papers WHERE id = ?", (paper["id"],)
        ).fetchone()
        if exists:
            dup_count += 1
            continue
        if fetch_abstract and paper["abstract"] is None:
            paper["abstract"] = scrape_abstract(article_number)
            time.sleep(delay)
        if insert_paper(conn, paper):
            new_count += 1
            logger.info("[+%d] %s — %s", new_count, paper["id"], paper["title"][:60])
        else:
            dup_count += 1
    conn.commit()

    new_offset = offset + fetched
    # 끝 도달: 받은 게 batch_size 미만이거나, 다음 위치가 전체 건수 이상.
    exhausted = fetched < batch_size or (total and new_offset >= total)
    set_cursor(conn, "ieee", query, new_offset, total or None, exhausted)
    conn.close()

    logger.info("IEEE 배치 완료: 신규 %d, 중복 %d, 받음 %d/%d, 다음 offset %d%s",
                new_count, dup_count, fetched, total, new_offset,
                " (끝 도달)" if exhausted else "")

    if new_count > 0:
        from src.arxiv_collector import export_catalog
        export_catalog()

    return {"new": new_count, "dup": dup_count, "fetched": fetched,
            "offset": new_offset, "exhausted": bool(exhausted), "total": total}


def collect_papers(
    queries: list[str] | None = None,
    max_per_query: int = 25,
    fetch_abstract: bool = True,
    delay: float = 3.0,
) -> list[dict]:
    """IEEE Xplore에서 LDPC 논문을 수집하여 DB에 저장."""
    if queries is None:
        queries = SEARCH_QUERIES

    conn = get_conn()
    init_db(conn)

    collected = []
    new_count = 0
    dup_count = 0

    for query in queries:
        logger.info("IEEE 검색: '%s' (max=%d)", query, max_per_query)
        data = search_ieee(query, max_results=max_per_query)

        if not data:
            logger.warning("검색 결과 없음: '%s'", query)
            continue

        total = data.get("totalRecords", 0)
        logger.info("검색 결과: %d건 (총 %d건 중)", len(data.get("records", [])), total)

        papers = parse_search_results(data)

        for paper in papers:
            existing = conn.execute(
                "SELECT id FROM papers WHERE id = ?", (paper["id"],)
            ).fetchone()
            if existing:
                dup_count += 1
                continue

            if fetch_abstract and paper["abstract"] is None:
                logger.info("Abstract 크롤링: %s", paper["article_number"])
                paper["abstract"] = scrape_abstract(paper["article_number"])
                time.sleep(delay)

            article_number = paper.pop("article_number")

            paper["collected_at"] = datetime.now(timezone.utc).isoformat()
            paper["status"] = "new"
            paper["pdf_path"] = None

            conn.execute("""
                INSERT INTO papers (id, source, title, authors, abstract, categories,
                                    published, updated, doi, pdf_url, pdf_path,
                                    collected_at, status)
                VALUES (:id, :source, :title, :authors, :abstract, :categories,
                        :published, :updated, :doi, :pdf_url, :pdf_path,
                        :collected_at, :status)
            """, paper)
            conn.commit()

            collected.append(paper)
            new_count += 1
            logger.info("[%d] %s — %s", new_count, paper["id"], paper["title"][:60])

        time.sleep(delay)

    conn.close()
    logger.info("IEEE 수집 완료: 신규 %d건, 중복 %d건", new_count, dup_count)

    if new_count > 0:
        from src.arxiv_collector import export_catalog
        export_catalog()

    return collected


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
    )
    papers = collect_papers(
        queries=["LDPC NAND flash"],
        max_per_query=5,
        fetch_abstract=True,
    )
    print(f"\n=== IEEE 수집 결과: {len(papers)}건 ===")
    for p in papers[:5]:
        print(f"  - {p['id']}: {p['title'][:70]}")
