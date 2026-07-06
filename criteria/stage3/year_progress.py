"""stage3 연도별 진행 현황을 집계한다.

- 총 편수: data/papers.db의 status='filtered_in' 논문을 published 필드에서
  연도를 추출해 연도별로 집계 (stage3가 처리해야 할 전체 대상 풀).
- 완료 편수: 같은 DB published 연도를 기준으로, 해당 논문의 결과 파일
  (results/{연도}/{id_underscore}.md, 어느 연도 폴더에 있든 무관)이
  존재하는지로 판정한다.

주의: 예전에는 "완료 편수"를 결과 파일이 위치한 연도 폴더(=분석 시 LLM이
읽어낸 발행연도)로 집계했다. 그 값은 DB published 연도와 다를 수 있어
(예: arXiv 프리프린트 연도 vs 실제 저널 게재 연도) 연도별 진행률이 100%를
넘는 경우가 있었다. 총/완료를 같은 기준(DB published 연도)으로 맞춰
이 문제를 없앤다. 폴더 위치와 DB 연도가 다른 파일은 별도 진단 목록으로만
남긴다.
"""
import re
import sqlite3
from collections import Counter
from pathlib import Path

BASE_DIR = Path(__file__).parent
RESULTS_DIR = BASE_DIR / "results"
DB_PATH = BASE_DIR.parent.parent / "data" / "papers.db"
OUTPUT_PATH = BASE_DIR / "year_progress.md"


def extract_published_year(published: str) -> str:
    matches = re.findall(r"(?:19|20)\d{2}", published or "")
    # IEEE published는 "6-8 April 2026"처럼 연도가 문자열 끝에 오고,
    # arXiv published는 ISO 날짜(YYYY-MM-DD...)라 연도가 하나뿐이다.
    return matches[-1] if matches else "미상"


def id_to_stem(paper_id: str) -> str:
    # results 저장 규칙(analysis_prompt.md)과 동일: ':'와 '/'를 '_'로 치환.
    return paper_id.replace(":", "_").replace("/", "_")


def load_filtered_in() -> tuple[Counter, dict]:
    conn = sqlite3.connect(DB_PATH)
    try:
        cur = conn.cursor()
        cur.execute("SELECT id, published FROM papers WHERE status = 'filtered_in'")
        rows = cur.fetchall()
    finally:
        conn.close()

    total_counts = Counter()
    stem_to_id_year = {}
    for paper_id, published in rows:
        year = extract_published_year(published)
        total_counts[year] += 1
        stem_to_id_year[id_to_stem(paper_id)] = (paper_id, year)
    return total_counts, stem_to_id_year


def count_done_by_db_year(stem_to_id_year: dict):
    done_counts = Counter()
    unknown_files = []  # 결과 파일은 있으나 filtered_in DB에 대응 id가 없음
    folder_mismatch = []  # 결과 파일의 위치 폴더 연도 != DB published 연도
    duplicate_files = []  # 같은 논문 id가 여러 연도 폴더에 중복 저장됨
    seen_stems = {}

    for path in sorted(RESULTS_DIR.glob("*/*.md")):
        stem = path.stem
        folder_year = path.parent.name
        match = stem_to_id_year.get(stem)
        if match is None:
            unknown_files.append(f"{folder_year}/{path.name}")
            continue

        if stem in seen_stems:
            duplicate_files.append(f"{folder_year}/{path.name} (첫 위치: {seen_stems[stem]})")
            continue
        seen_stems[stem] = f"{folder_year}/{path.name}"

        _paper_id, db_year = match
        done_counts[db_year] += 1
        if db_year != folder_year:
            folder_mismatch.append(f"{folder_year}/{path.name} (DB 발행연도: {db_year})")

    return done_counts, unknown_files, folder_mismatch, duplicate_files


def main() -> None:
    total_counts, stem_to_id_year = load_filtered_in()
    done_counts, unknown_files, folder_mismatch, duplicate_files = count_done_by_db_year(stem_to_id_year)

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
    lines.append("- 집계 기준: 총/완료 모두 DB `published` 연도로 통일 (결과 파일이 실제 위치한 연도 폴더와는 무관)")
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

    if unknown_files:
        lines.append("")
        lines.append("## DB(filtered_in)에 대응 id가 없는 결과 파일")
        for name in unknown_files:
            lines.append(f"- {name}")

    if duplicate_files:
        lines.append("")
        lines.append("## 중복 저장된 결과 파일 (같은 id가 여러 연도 폴더에 존재)")
        for name in duplicate_files:
            lines.append(f"- {name}")

    if folder_mismatch:
        lines.append("")
        lines.append(f"## 폴더 위치와 DB 발행연도가 다른 파일 ({len(folder_mismatch)}건, 진행률 계산에는 영향 없음)")
        for name in folder_mismatch:
            lines.append(f"- {name}")

    output = "\n".join(lines) + "\n"
    OUTPUT_PATH.write_text(output, encoding="utf-8")
    print(output)


if __name__ == "__main__":
    main()
