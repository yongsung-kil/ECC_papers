"""카탈로그 생성 — papers.db를 사람이 읽는 markdown/csv로 출력.

수집은 종료됐고, 이 모듈은 DB 내용을 `papers/{source}/{year}/{month}/catalog.md|csv`
로 재생성하는 '보기' 기능만 담당한다. (예: Phase 2 선별로 status가 바뀐 뒤 갱신)

    python -m src.catalog        # 전체 카탈로그 재생성
"""

import csv
import json
import logging
import re
import shutil
from pathlib import Path

from src.db import get_conn

logger = logging.getLogger(__name__)

PROJECT_ROOT = Path(__file__).resolve().parent.parent

_STATUS_LABEL = {
    "new": "⬜ 미선별",
    "filtered_in": "✅",
    "filtered_out": "❌",
    "analyzed": "🔬 분석완료",
    "archived": "📦 보관",
    "deleted": "🗑️ 삭제",
}


def _status_label(status: str | None) -> str:
    return _STATUS_LABEL.get(status, status or "")


def rebuild_catalog():
    """기존 papers/{arxiv,ieee}를 비우고 DB로부터 전체 재생성 → 항상 DB와 정확히 일치."""
    for source in ("arxiv", "ieee"):
        d = PROJECT_ROOT / "papers" / source
        if d.exists():
            shutil.rmtree(d)
    export_catalog()


def export_catalog():
    conn = get_conn()
    rows = conn.execute(
        "SELECT p.id, p.source, p.title, p.authors, p.abstract, p.categories, "
        "p.published, p.doi, p.pdf_url, p.content_type, p.status, f.reason "
        "FROM papers p LEFT JOIN filter_results f ON p.id = f.paper_id "
        "ORDER BY p.published DESC"
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
        lines.append(f"- **Status**: {_status_label(r['status'])}")
        lines.append(f"- **Reason**: {r['reason'] or 'N/A'}")
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
        writer.writerow(["ID", "Type", "Title", "Status", "Reason", "Authors",
                         "Abstract", "Categories", "Published", "DOI", "PDF URL"])
        for r in rows:
            writer.writerow([
                r["id"], r["content_type"] or "", r["title"],
                _status_label(r["status"]), r["reason"] or "",
                ", ".join(json.loads(r["authors"])),
                r["abstract"],
                ", ".join(json.loads(r["categories"])),
                r["published"][:10] if r["published"] else "",
                r["doi"] or "",
                r["pdf_url"],
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
    if re.match(r"\d{4}-\d{2}", published):
        return published[:7]
    year_match = re.search(r"(\d{4})", published)
    if not year_match:
        return "unknown"
    year = year_match.group(1)
    for token in published.lower().replace(".", "").split():
        if token in _MONTH_MAP:
            return f"{year}-{_MONTH_MAP[token]}"
    return f"{year}-01"


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s [%(levelname)s] %(message)s")
    rebuild_catalog()  # 기존 삭제 후 재생성
    print("카탈로그 재생성 완료 (기존 삭제 후 DB로 재생성)")
