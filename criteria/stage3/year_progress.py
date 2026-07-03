"""stage3 연도별 진행 현황을 집계한다.

- 총 편수: data/papers.db의 status='filtered_in' 논문을 published 필드에서
  연도를 추출해 연도별로 집계 (stage3가 처리해야 할 전체 대상 풀).
- 완료 편수: stage3/results/*.md 파일을 첫 줄 "### <id> - <title> (YYYY, <venue>)"
  형식에서 연도를 추출해 연도별로 집계.
"""
import re
import sqlite3
from collections import Counter
from pathlib import Path

BASE_DIR = Path(__file__).parent
RESULTS_DIR = BASE_DIR / "results"
DB_PATH = BASE_DIR.parent.parent / "data" / "papers.db"
OUTPUT_PATH = BASE_DIR / "year_progress.md"

TITLE_YEAR_RE = re.compile(r"\((\d{4}),")
PUBLISHED_YEAR_RE = re.compile(r"(19|20)\d{2}")


def extract_title_year(first_line: str) -> str:
    matches = TITLE_YEAR_RE.findall(first_line)
    # 제목에 "(2048,1723)" 같은 부호 파라미터가 섞여 있을 수 있어
    # 마지막 매치(실제 연도 표기 위치)를 사용한다.
    return matches[-1] if matches else "미상"


def extract_published_year(published: str) -> str:
    matches = re.findall(r"(?:19|20)\d{2}", published or "")
    # IEEE published는 "6-8 April 2026"처럼 연도가 문자열 끝에 오고,
    # arXiv published는 ISO 날짜(YYYY-MM-DD...)라 연도가 하나뿐이다.
    return matches[-1] if matches else "미상"


def count_total_by_year() -> Counter:
    conn = sqlite3.connect(DB_PATH)
    try:
        cur = conn.cursor()
        cur.execute("SELECT published FROM papers WHERE status = 'filtered_in'")
        rows = cur.fetchall()
    finally:
        conn.close()

    counts = Counter()
    for (published,) in rows:
        counts[extract_published_year(published)] += 1
    return counts


def count_done_by_year() -> tuple[Counter, list[str]]:
    counts = Counter()
    unmatched = []
    for path in sorted(RESULTS_DIR.glob("*.md")):
        with path.open("r", encoding="utf-8") as f:
            first_line = f.readline()
        year = extract_title_year(first_line)
        counts[year] += 1
        if year == "미상":
            unmatched.append(path.name)
    return counts, unmatched


def main() -> None:
    total_counts = count_total_by_year()
    done_counts, unmatched = count_done_by_year()

    total_sum = sum(total_counts.values())
    done_sum = sum(done_counts.values())

    all_years = sorted(
        {y for y in total_counts if y != "미상"} | {y for y in done_counts if y != "미상"},
        key=int,
    )

    lines = []
    lines.append("# Stage3 연도별 진행 현황")
    lines.append("")
    lines.append(f"- 전체 대상(filtered_in): {total_sum}편")
    lines.append(f"- 완료(stage3 결과): {done_sum}편 ({done_sum / total_sum:.1%})")
    lines.append("")
    lines.append("| 연도 | 총 편수 | 완료 편수 | 진행률 |")
    lines.append("|---|---|---|---|")

    for year in all_years:
        total = total_counts.get(year, 0)
        done = done_counts.get(year, 0)
        rate = f"{done / total:.0%}" if total else "-"
        lines.append(f"| {year} | {total} | {done} | {rate} |")

    if "미상" in total_counts or "미상" in done_counts:
        lines.append(
            f"| 미상 | {total_counts.get('미상', 0)} | {done_counts.get('미상', 0)} | - |"
        )

    if unmatched:
        lines.append("")
        lines.append("## 완료 편수 연도 파싱 실패 파일 (stage3/results)")
        for name in unmatched:
            lines.append(f"- {name}")

    output = "\n".join(lines) + "\n"
    OUTPUT_PATH.write_text(output, encoding="utf-8")
    print(output)


if __name__ == "__main__":
    main()
