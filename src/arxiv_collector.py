"""arXiv LDPC 논문 수집기.

arXiv API를 사용하여 LDPC 관련 논문의 메타데이터를 수집하고,
선택적으로 PDF를 다운로드합니다.
"""

import csv
import json
import logging
import time
from datetime import datetime, timezone
from pathlib import Path

import arxiv
import requests

from src.db import get_conn, init_db

logger = logging.getLogger(__name__)

PROJECT_ROOT = Path(__file__).resolve().parent.parent
PDF_DIR = PROJECT_ROOT / "papers" / "pdfs"

SEARCH_QUERIES = [
    "LDPC",
    "low density parity check",
    "LDPC decoding",
    "LDPC decoder",
    "LDPC code design",
    "LDPC belief propagation",
    "min-sum LDPC",
    "LDPC NAND flash",
    "LDPC SSD",
    "LDPC error floor",
]

CATEGORIES = [
    "cs.IT",   # Information Theory
    "eess.SP", # Signal Processing
    "cs.AR",   # Hardware Architecture
    "cs.ET",   # Emerging Technologies
]


def build_query(query_terms: list[str] | None = None,
                categories: list[str] | None = None) -> str:
    terms = query_terms or SEARCH_QUERIES
    cats = categories or CATEGORIES

    term_part = " OR ".join(f'all:"{t}"' for t in terms)
    cat_part = " OR ".join(f"cat:{c}" for c in cats)
    return f"({term_part}) AND ({cat_part})"


def collect_papers(
    max_results: int = 100,
    query: str | None = None,
    download_pdf: bool = False,
    sort_by: arxiv.SortCriterion = arxiv.SortCriterion.SubmittedDate,
) -> list[dict]:
    if query is None:
        query = build_query()

    logger.info("arXiv 검색 시작: %s (max=%d)", query[:80], max_results)

    client = arxiv.Client(
        page_size=50,
        delay_seconds=3.0,
        num_retries=3,
    )
    search = arxiv.Search(
        query=query,
        max_results=max_results,
        sort_by=sort_by,
        sort_order=arxiv.SortOrder.Descending,
    )

    conn = get_conn()
    init_db(conn)

    collected = []
    new_count = 0
    dup_count = 0

    for result in client.results(search):
        arxiv_id = result.entry_id.split("/abs/")[-1]
        paper_id = f"arxiv:{arxiv_id}"

        existing = conn.execute(
            "SELECT id FROM papers WHERE id = ?", (paper_id,)
        ).fetchone()
        if existing:
            dup_count += 1
            continue

        paper = {
            "id": paper_id,
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
            "status": "new",
        }

        if download_pdf:
            pdf_path = _download_pdf(paper_id, result.pdf_url)
            if pdf_path:
                paper["pdf_path"] = str(pdf_path.relative_to(PROJECT_ROOT))

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
        logger.info("[%d] %s — %s", new_count, paper_id, paper["title"][:60])

    conn.close()
    logger.info("수집 완료: 신규 %d건, 중복 %d건", new_count, dup_count)

    if new_count > 0:
        export_catalog()

    return collected


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
        "published, doi, pdf_url, status "
        "FROM papers ORDER BY published DESC"
    ).fetchall()
    conn.close()

    for source, label in [("arxiv", "arXiv"), ("ieee", "IEEE Xplore")]:
        source_rows = [r for r in rows if r["source"] == source]
        if not source_rows:
            continue
        _export_md(source, label, source_rows)
        _export_csv(source, source_rows)


def _export_md(source: str, label: str, rows):
    dir_path = PROJECT_ROOT / "papers" / source
    dir_path.mkdir(parents=True, exist_ok=True)
    md_path = dir_path / "catalog.md"

    lines = [f"# {label} — Collected Papers\n", f"Total: {len(rows)}\n", ""]
    for i, r in enumerate(rows, 1):
        authors = json.loads(r["authors"])
        author_str = ", ".join(authors[:3])
        if len(authors) > 3:
            author_str += f" +{len(authors)-3}"
        lines.append(f"## {i}. {r['title']}\n")
        lines.append(f"- **ID**: {r['id']}")
        lines.append(f"- **Published**: {r['published'][:10] if r['published'] else 'N/A'}")
        lines.append(f"- **Authors**: {author_str}")
        lines.append(f"- **Status**: {r['status']}")
        lines.append(f"- **PDF**: {r['pdf_url']}")
        lines.append(f"- **Abstract**: {r['abstract'] or 'N/A'}")
        lines.append("")

    with open(md_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    logger.info("%s/catalog.md 갱신 완료 (%d건)", source, len(rows))


def _export_csv(source: str, rows):
    dir_path = PROJECT_ROOT / "papers" / source
    dir_path.mkdir(parents=True, exist_ok=True)
    csv_path = dir_path / "catalog.csv"

    with open(csv_path, "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Title", "Authors", "Abstract",
                         "Categories", "Published", "DOI", "PDF URL", "Status"])
        for r in rows:
            writer.writerow([
                r["id"], r["title"],
                ", ".join(json.loads(r["authors"])),
                r["abstract"],
                ", ".join(json.loads(r["categories"])),
                r["published"][:10] if r["published"] else "",
                r["doi"] or "",
                r["pdf_url"], r["status"],
            ])
    logger.info("%s/catalog.csv 갱신 완료 (%d건)", source, len(rows))


def get_stats(conn=None) -> dict:
    close = conn is None
    if conn is None:
        conn = get_conn()
    row = conn.execute("""
        SELECT
            COUNT(*) as total,
            SUM(CASE WHEN source='arxiv' THEN 1 ELSE 0 END) as arxiv_count,
            SUM(CASE WHEN source='ieee' THEN 1 ELSE 0 END) as ieee_count,
            SUM(CASE WHEN status='new' THEN 1 ELSE 0 END) as new_count,
            SUM(CASE WHEN status='filtered_in' THEN 1 ELSE 0 END) as filtered_in,
            SUM(CASE WHEN status='analyzed' THEN 1 ELSE 0 END) as analyzed
        FROM papers
    """).fetchone()
    if close:
        conn.close()
    return dict(row)


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
    )
    papers = collect_papers(max_results=20, download_pdf=False)
    print(f"\n=== 수집 결과: {len(papers)}건 ===")
    for p in papers[:5]:
        print(f"  - {p['id']}: {p['title'][:70]}")
    if len(papers) > 5:
        print(f"  ... 외 {len(papers) - 5}건")
