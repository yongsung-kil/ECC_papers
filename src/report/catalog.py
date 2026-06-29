"""카탈로그 생성 — papers.db를 사람이 읽는 markdown/csv로 출력.

수집은 종료됐고, 이 모듈은 DB 내용을 사람이 읽는 카탈로그로 재생성하는
'보기' 기능만 담당한다. (예: Phase 2 선별로 status가 바뀐 뒤 갱신)

출력 구조:
    data/catalogs/원본/{source}/{year}/{month}/catalog.md|csv          # 전체 22,225편
    data/catalogs/stage1/통과/{source}/{year}/{month}/catalog.md|csv   # filtered_in
    data/catalogs/stage1/제외/{source}/{year}/{month}/catalog.md|csv   # filtered_out
    data/catalogs/stage1/SUMMARY.md                                     # 선별 통계 요약

`stage1/통과`는 1단계 선별 통과(status='filtered_in')를 모으며 알고리즘 기여
여부(filter_results.algo_mod)를 함께 표기한다.
`stage1/제외`는 1단계 선별 제외(status='filtered_out')를 모은다.

    python -m src.report.catalog        # 전체 카탈로그(원본+stage1) 재생성
"""

import csv
import json
import logging
import re
import shutil
from pathlib import Path

from src.db import get_conn

logger = logging.getLogger(__name__)

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
CATALOG_ROOT = PROJECT_ROOT / "data" / "catalogs"   # 카탈로그(md/csv) 출력 루트

# 출력 루트 디렉토리명
DIR_ORIGINAL = "원본"
DIR_SELECTED = "stage1"   # 1단계(선별) 산출 카탈로그
DIR_IN = "통과"
DIR_OUT = "제외"

_STATUS_LABEL = {
    "new": "⬜ 미선별",
    "filtered_in": "✅",
    "filtered_out": "❌",
    "analyzed": "🔬 분석완료",
    "archived": "📦 보관",
    "deleted": "🗑️ 삭제",
}

_ALGO_LABEL = {
    1: "✅ 알고리즘/코드 기여",
    0: "🔧 하드웨어 수정만",
    None: "N/A",
}


def _status_label(status: str | None) -> str:
    return _STATUS_LABEL.get(status, status or "")


def _algo_label(algo_mod) -> str:
    return _ALGO_LABEL.get(algo_mod, "N/A")


def rebuild_catalog():
    """기존 data/catalogs/{원본,stage1}을 비우고 DB로부터 전체 재생성 → 항상 DB와 정확히 일치."""
    for sub in (DIR_ORIGINAL, DIR_SELECTED):
        d = CATALOG_ROOT / sub
        if d.exists():
            shutil.rmtree(d)
    # 과거 구조(papers/ 하위 카탈로그)가 남아있으면 정리
    for legacy in ("원본", "1차선별", "arxiv", "ieee"):
        d = PROJECT_ROOT / "papers" / legacy
        if d.exists():
            shutil.rmtree(d)
    export_catalog()


def _fetch_rows():
    conn = get_conn()
    rows = conn.execute(
        "SELECT p.id, p.source, p.title, p.authors, p.abstract, p.categories, "
        "p.published, p.doi, p.pdf_url, p.content_type, p.status, "
        "f.reason, f.relevance_score, f.algo_mod "
        "FROM papers p LEFT JOIN filter_results f ON p.id = f.paper_id "
        "ORDER BY p.published DESC"
    ).fetchall()
    conn.close()
    return rows


def export_catalog():
    rows = _fetch_rows()

    # 원본: 전체
    _export_tree(CATALOG_ROOT / DIR_ORIGINAL, rows, selected=False)

    # stage1(선별): 통과(filtered_in) / 제외(filtered_out)
    selected = [r for r in rows if r["status"] == "filtered_in"]
    excluded = [r for r in rows if r["status"] == "filtered_out"]
    _export_tree(CATALOG_ROOT / DIR_SELECTED / DIR_IN, selected, selected=True)
    _export_tree(CATALOG_ROOT / DIR_SELECTED / DIR_OUT, excluded, selected=False)
    _export_summary(CATALOG_ROOT / DIR_SELECTED, rows, selected)


def _export_tree(root: Path, rows, selected: bool):
    """root/{source}/{year}/{month}/catalog.md|csv 생성."""
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
                dir_path = root / source / "unknown"
            else:
                year, month = ym.split("-")
                dir_path = root / source / year / month
            _export_md(dir_path, label, month_rows, ym, selected)
            _export_csv(dir_path, month_rows, selected)


def _export_md(dir_path: Path, label: str, rows, year_month: str, selected: bool):
    dir_path.mkdir(parents=True, exist_ok=True)
    md_path = dir_path / "catalog.md"

    suffix = " (1차선별 통과)" if selected else ""
    lines = [f"# {label} — {year_month}{suffix}\n", ""]
    for r in rows:
        authors = json.loads(r["authors"])
        author_str = ", ".join(authors[:3])
        if len(authors) > 3:
            author_str += f" +{len(authors)-3}"
        lines.append(f"## {r['title']}\n")
        lines.append(f"- **Status**: {_status_label(r['status'])}")
        lines.append(f"- **Reason**: {r['reason'] or 'N/A'}")
        if selected:
            lines.append(f"- **알고리즘 기여**: {_algo_label(r['algo_mod'])}")
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


def _export_csv(dir_path: Path, rows, selected: bool):
    dir_path.mkdir(parents=True, exist_ok=True)
    csv_path = dir_path / "catalog.csv"

    header = ["ID", "Type", "Title", "Status", "Reason"]
    if selected:
        header.append("Algo")
    header += ["Authors", "Abstract", "Categories", "Published", "DOI", "PDF URL"]

    with open(csv_path, "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for r in rows:
            row = [
                r["id"], r["content_type"] or "", r["title"],
                _status_label(r["status"]), r["reason"] or "",
            ]
            if selected:
                row.append(_algo_label(r["algo_mod"]))
            row += [
                ", ".join(json.loads(r["authors"])),
                r["abstract"],
                ", ".join(json.loads(r["categories"])),
                r["published"][:10] if r["published"] else "",
                r["doi"] or "",
                r["pdf_url"],
            ]
            writer.writerow(row)
    logger.info("%s/catalog.csv 갱신 (%d건)", dir_path.relative_to(PROJECT_ROOT), len(rows))


def _export_summary(root: Path, all_rows, selected):
    """1차선별 통계 요약 → root/SUMMARY.md."""
    root.mkdir(parents=True, exist_ok=True)
    total = len(all_rows)
    n_in = len(selected)
    n_out = total - n_in

    # 소스별
    def src_count(rows, src):
        return sum(1 for r in rows if r["source"] == src)

    # 알고리즘 기여
    algo_keep = sum(1 for r in selected if r["algo_mod"] == 1)
    algo_hw = sum(1 for r in selected if r["algo_mod"] == 0)
    algo_na = n_in - algo_keep - algo_hw

    # 연도별 선별 통과 분포
    by_year = {}
    for r in selected:
        ym = _extract_year_month(r["published"])
        year = ym.split("-")[0] if ym != "unknown" else "unknown"
        by_year[year] = by_year.get(year, 0) + 1

    pct = lambda n, d: f"{n/d*100:.1f}%" if d else "0%"

    lines = [
        "# 1차선별 요약 (Phase 2 통과분)\n",
        f"> 전체 {total:,}편 중 NAND LDPC ECC 적용성 1차 선별 통과분.\n",
        "## 전체 현황\n",
        "| 구분 | 편수 | 비율 |",
        "|------|------|------|",
        f"| 전체 수집 | {total:,} | 100% |",
        f"| ✅ 통과 (filtered_in) | {n_in:,} | {pct(n_in, total)} |",
        f"| ❌ 제외 (filtered_out) | {n_out:,} | {pct(n_out, total)} |",
        "",
        "## 소스별 통과\n",
        "| 소스 | 통과 | 전체 | 통과율 |",
        "|------|------|------|--------|",
        f"| arXiv | {src_count(selected, 'arxiv'):,} | {src_count(all_rows, 'arxiv'):,} | "
        f"{pct(src_count(selected, 'arxiv'), src_count(all_rows, 'arxiv'))} |",
        f"| IEEE Xplore | {src_count(selected, 'ieee'):,} | {src_count(all_rows, 'ieee'):,} | "
        f"{pct(src_count(selected, 'ieee'), src_count(all_rows, 'ieee'))} |",
        "",
        "## 알고리즘 기여 여부 (Phase 2.5)\n",
        "통과분 중 알고리즘/코드 기여가 있어 다음 단계 대상이 되는 논문 구분.\n",
        "| 구분 | 편수 | 비율 |",
        "|------|------|------|",
        f"| ✅ 알고리즘/코드 기여 (algo_mod=1) | {algo_keep:,} | {pct(algo_keep, n_in)} |",
        f"| 🔧 하드웨어 수정만 (algo_mod=0) | {algo_hw:,} | {pct(algo_hw, n_in)} |",
    ]
    if algo_na:
        lines.append(f"| N/A (미분류) | {algo_na:,} | {pct(algo_na, n_in)} |")
    lines += [
        "",
        "## 연도별 통과 분포\n",
        "| 연도 | 통과 편수 |",
        "|------|-----------|",
    ]
    for year in sorted(by_year, reverse=True):
        lines.append(f"| {year} | {by_year[year]:,} |")
    lines += [
        "",
        "---",
        "",
        "- 상세 분류 기준: [../../../CLASSIFICATION.md](../../../CLASSIFICATION.md)",
        "- 판정 기준서: [../../../criteria/stage1/selection_criteria.md](../../../criteria/stage1/selection_criteria.md)",
        "- 통과 카탈로그: `data/catalogs/stage1/통과/{arxiv,ieee}/{연}/{월}/catalog.md`",
        "- 제외 카탈로그: `data/catalogs/stage1/제외/{arxiv,ieee}/{연}/{월}/catalog.md`",
        "",
    ]

    with open(root / "SUMMARY.md", "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    logger.info("%s/SUMMARY.md 갱신 (통과 %d건)", root.relative_to(PROJECT_ROOT), n_in)


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
    print("카탈로그 재생성 완료 (data/catalogs/원본 + data/catalogs/stage1)")
