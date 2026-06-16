"""arXiv LDPC 논문 수집기.

arXiv API를 사용하여 LDPC 관련 논문의 메타데이터를 수집하고,
선택적으로 PDF를 다운로드합니다.
"""

import csv
import json
import logging
import re
import time
from datetime import datetime, timezone
from pathlib import Path

import arxiv
import requests

from src.db import (
    get_conn, init_db, insert_paper, get_cursor, set_cursor,
)

logger = logging.getLogger(__name__)

PROJECT_ROOT = Path(__file__).resolve().parent.parent
PDF_DIR = PROJECT_ROOT / "papers" / "pdfs"

# 광범위 수집: LDPC 논문을 전부 취합한 뒤 Phase 2에서 하나씩 선별.
# (양자/카테고리 제한 없이 recall 최대화 — 좁은 쿼리는 모두 이 집합의 부분집합)
SEARCH_QUERIES = [
    "LDPC",
    "low density parity check code",
]


def build_query(query_terms: list[str] | None = None) -> str:
    terms = query_terms or SEARCH_QUERIES
    return " OR ".join(f'all:"{t}"' for t in terms)


def _result_to_paper(result) -> dict:
    """arxiv.Result → papers 테이블 행(dict)."""
    arxiv_id = result.entry_id.split("/abs/")[-1]
    return {
        "id": f"arxiv:{arxiv_id}",
        "source": "arxiv",
        "title": result.title.replace("\n", " ").strip(),
        "authors": json.dumps([a.name for a in result.authors]),
        "abstract": result.summary.replace("\n", " ").strip(),
        "categories": json.dumps(result.categories),
        "published": result.published.isoformat() if result.published else None,
        "updated": result.updated.isoformat() if result.updated else None,
        "doi": result.doi,
        "pdf_url": result.pdf_url,
        "pdf_path": None,
        "collected_at": datetime.now(timezone.utc).isoformat(),
        "content_type": "preprint",
        "status": "new",
    }


def collect_batch(
    query: str | None = None,
    batch_size: int = 100,
    download_pdf: bool = False,
) -> dict:
    """커서 기반 1배치 수집(이어받기).

    제출일 **오름차순**(오래된 것부터)으로 정렬해 offset 커서가 안정적으로
    전진하도록 한다. 새 논문은 항상 결과 맨 뒤에 추가되므로 순서가 꼬이지 않는다.
    중복(이미 있는 ID)은 INSERT OR IGNORE로 제외한다.

    반환: {"new": 신규, "dup": 중복, "fetched": 이번에 받은 원시 건수,
           "offset": 갱신된 offset, "exhausted": 끝 도달 여부}
    """
    if query is None:
        query = build_query()

    conn = get_conn()
    init_db(conn)

    cursor = get_cursor(conn, "arxiv", query)
    offset = cursor["next_offset"]

    if cursor["exhausted"]:
        conn.close()
        return {"new": 0, "dup": 0, "fetched": 0, "offset": offset, "exhausted": True}

    logger.info("arXiv 배치 수집: offset=%d, size=%d, exhausted=%s",
                offset, batch_size, cursor["exhausted"])

    # arxiv 라이브러리에서 Search.max_results는 '전체 상한'이다. offset 이후
    # batch_size건을 받으려면 상한을 offset+batch_size로 잡아야 한다.
    client = arxiv.Client(page_size=min(batch_size, 100), delay_seconds=3.0, num_retries=3)
    search = arxiv.Search(
        query=query,
        max_results=offset + batch_size,
        sort_by=arxiv.SortCriterion.SubmittedDate,
        sort_order=arxiv.SortOrder.Ascending,
    )

    new_count = dup_count = fetched = 0
    for result in client.results(search, offset=offset):
        fetched += 1
        paper = _result_to_paper(result)
        if download_pdf:
            pdf_path = _download_pdf(paper["id"], paper["pdf_url"])
            if pdf_path:
                paper["pdf_path"] = str(pdf_path.relative_to(PROJECT_ROOT))
        if insert_paper(conn, paper):
            new_count += 1
            logger.info("[+%d] %s — %s", new_count, paper["id"], paper["title"][:60])
        else:
            dup_count += 1
    conn.commit()

    # batch_size 미만을 받으면 웹 결과 끝에 도달한 것.
    exhausted = fetched < batch_size
    new_offset = offset + fetched
    set_cursor(conn, "arxiv", query, new_offset, None, exhausted)
    conn.close()

    logger.info("arXiv 배치 완료: 신규 %d, 중복 %d, 받음 %d, 다음 offset %d%s",
                new_count, dup_count, fetched, new_offset,
                " (끝 도달)" if exhausted else "")

    if new_count > 0:
        export_catalog()

    return {"new": new_count, "dup": dup_count, "fetched": fetched,
            "offset": new_offset, "exhausted": exhausted}


def _download_pdf(paper_id: str, pdf_url: str) -> Path | None:
    PDF_DIR.mkdir(parents=True, exist_ok=True)
    safe_name = paper_id.replace(":", "_").replace("/", "_")
    pdf_path = PDF_DIR / f"{safe_name}.pdf"

    if pdf_path.exists():
        return pdf_path

    try:
        resp = requests.get(pdf_url, timeout=30, stream=True)
        resp.raise_for_status()
        with open(pdf_path, "wb") as f:
            for chunk in resp.iter_content(chunk_size=8192):
                f.write(chunk)
        logger.info("PDF 다운로드 완료: %s", pdf_path.name)
        time.sleep(1)
        return pdf_path
    except Exception as e:
        logger.warning("PDF 다운로드 실패 (%s): %s", paper_id, e)
        return None


def export_catalog():
    conn = get_conn()
    rows = conn.execute(
        "SELECT id, source, title, authors, abstract, categories, "
        "published, doi, pdf_url, content_type, status "
        "FROM papers ORDER BY published DESC"
    ).fetchall()
    conn.close()

    for source, label in [("arxiv", "arXiv"), ("ieee", "IEEE Xplore")]:
        source_rows = [r for r in rows if r["source"] == source]
        if not source_rows:
            continue

        by_month = {}
        for r in source_rows:
            ym = _extract_year_month(r["published"])
            by_month.setdefault(ym, []).append(r)

        for ym, month_rows in sorted(by_month.items(), reverse=True):
            if ym == "unknown":
                dir_path = PROJECT_ROOT / "papers" / source / "unknown"
            else:
                year, month = ym.split("-")
                dir_path = PROJECT_ROOT / "papers" / source / year / month
            _export_md(dir_path, label, month_rows, ym)
            _export_csv(dir_path, month_rows)


def _export_md(dir_path: Path, label: str, rows, year_month: str):
    dir_path.mkdir(parents=True, exist_ok=True)
    md_path = dir_path / "catalog.md"

    lines = [f"# {label} — {year_month}\n", ""]
    for r in rows:
        authors = json.loads(r["authors"])
        author_str = ", ".join(authors[:3])
        if len(authors) > 3:
            author_str += f" +{len(authors)-3}"
        lines.append(f"## {r['title']}\n")
        lines.append(f"- **ID**: {r['id']}")
        lines.append(f"- **Type**: {r['content_type'] or 'N/A'}")
        lines.append(f"- **Published**: {r['published'][:10] if r['published'] else 'N/A'}")
        lines.append(f"- **Authors**: {author_str}")
        lines.append(f"- **PDF**: {r['pdf_url']}")
        lines.append(f"- **Abstract**: {r['abstract'] or 'N/A'}")
        lines.append("")

    with open(md_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    logger.info("%s/catalog.md 갱신 (%d건)", dir_path.relative_to(PROJECT_ROOT), len(rows))


def _export_csv(dir_path: Path, rows):
    dir_path.mkdir(parents=True, exist_ok=True)
    csv_path = dir_path / "catalog.csv"

    with open(csv_path, "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Type", "Title", "Authors", "Abstract",
                         "Categories", "Published", "DOI", "PDF URL", "Status"])
        for r in rows:
            writer.writerow([
                r["id"], r["content_type"] or "", r["title"],
                ", ".join(json.loads(r["authors"])),
                r["abstract"],
                ", ".join(json.loads(r["categories"])),
                r["published"][:10] if r["published"] else "",
                r["doi"] or "",
                r["pdf_url"], r["status"],
            ])
    logger.info("%s/catalog.csv 갱신 (%d건)", dir_path.relative_to(PROJECT_ROOT), len(rows))


_MONTH_MAP = {
    "jan": "01", "january": "01", "feb": "02", "february": "02",
    "mar": "03", "march": "03", "apr": "04", "april": "04",
    "may": "05", "jun": "06", "june": "06", "jul": "07", "july": "07",
    "aug": "08", "august": "08", "sep": "09", "sept": "09", "september": "09",
    "oct": "10", "october": "10", "nov": "11", "november": "11",
    "dec": "12", "december": "12",
}


def _extract_year_month(published: str | None) -> str:
    """다양한 날짜 형식에서 'YYYY-MM'을 추출. 실패 시 'unknown'."""
    if not published:
        return "unknown"
    # ISO format: "2026-06-05T..." → "2026-06"
    if re.match(r"\d{4}-\d{2}", published):
        return published[:7]
    # IEEE format: "April 2024", "2-4 Dec. 2015", "21-23 July 2016"
    year_match = re.search(r"(\d{4})", published)
    if not year_match:
        return "unknown"
    year = year_match.group(1)
    for token in published.lower().replace(".", "").split():
        if token in _MONTH_MAP:
            return f"{year}-{_MONTH_MAP[token]}"
    return f"{year}-01"


def _normalize_title(title: str) -> str:
    t = title.lower().strip()
    t = re.sub(r"[^a-z0-9\s]", "", t)
    t = re.sub(r"\s+", " ", t)
    return t


def dedup_cross_source():
    """arXiv/IEEE 교차 중복 제거. 동일 논문이 양쪽에 있고 IEEE가 더 늦으면 arXiv 삭제."""
    conn = get_conn()
    arxiv_rows = conn.execute(
        "SELECT id, title, doi, published FROM papers WHERE source='arxiv'"
    ).fetchall()
    ieee_rows = conn.execute(
        "SELECT id, title, doi, published FROM papers WHERE source='ieee'"
    ).fetchall()

    ieee_by_doi = {}
    ieee_by_title = {}
    for r in ieee_rows:
        if r["doi"]:
            ieee_by_doi[r["doi"]] = r
        ieee_by_title[_normalize_title(r["title"])] = r

    removed = []
    for ar in arxiv_rows:
        match = None
        if ar["doi"] and ar["doi"] in ieee_by_doi:
            match = ieee_by_doi[ar["doi"]]
        else:
            norm = _normalize_title(ar["title"])
            if norm in ieee_by_title:
                match = ieee_by_title[norm]

        if match is None:
            continue

        ieee_date = match["published"] or ""
        arxiv_date = ar["published"] or ""
        if ieee_date >= arxiv_date:
            conn.execute("DELETE FROM papers WHERE id = ?", (ar["id"],))
            removed.append((ar["id"], ar["title"][:60], match["id"]))
            logger.info("중복 제거: %s → %s 유지 (%s)", ar["id"], match["id"], ar["title"][:40])

    conn.commit()
    conn.close()

    if removed:
        logger.info("교차 중복 제거 완료: %d건 arXiv 삭제", len(removed))
        export_catalog()
    else:
        logger.info("교차 중복 없음")

    return removed


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
    )
    result = collect_batch(batch_size=10)
    print(f"\n=== arXiv 배치 수집: {result} ===")
