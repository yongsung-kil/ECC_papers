"""stage3 연도별 진행 현황 + 결과 분석 리포트를 생성한다.

- 총 편수: data/papers.db의 status='filtered_in' 논문을 published 필드에서
  연도를, source/content_type에서 IEEE Journal/Conference/arXiv 구분을
  추출해 집계 (stage3가 처리해야 할 전체 대상 풀).
- 완료 편수: 같은 DB 기준(연도, venue 구분)으로, 해당 논문의 결과 파일
  (results/{연도}/{id_underscore}.md, 어느 연도 폴더에 있든 무관)이
  존재하는지로 판정한다.
- 완료된 결과 파일의 JSON 블록(D섹션)을 모두 파싱해 이식성/추천도 등
  카테고리 분포와, 추천도가 '상'인 논문 목록을 함께 출력한다.

주의: "완료 편수"는 결과 파일이 위치한 연도 폴더가 아니라 DB published
연도로 집계한다. 폴더 위치와 DB 연도가 다른 파일은 별도 진단 목록으로만
남긴다 (진행률 계산에는 영향 없음).
"""
import json
import re
import sqlite3
from collections import Counter
from pathlib import Path

BASE_DIR = Path(__file__).parent
RESULTS_DIR = BASE_DIR / "results"
DB_PATH = BASE_DIR.parent.parent / "data" / "papers.db"
OUTPUT_PATH = BASE_DIR / "year_progress.md"

JSON_BLOCK_RE = re.compile(r"```json\s*(\{.*?\})\s*```", re.DOTALL)

VENUE_COLUMNS = [
    ("ieee_journal", "IEEE Journal"),
    ("ieee_conference", "Conference"),
    ("arxiv", "arXiv"),
]

# (JSON 키, 출력 라벨, enum 표시 순서)
CATEGORY_FIELDS = [
    ("portability", "이식성", ["상", "중", "하", "미상"]),
    ("recommend", "추천도", ["상", "중", "하", "미상"]),
    ("nand_relevance", "NAND관련성", ["직접", "간접", "낮음", "미상"]),
    ("target", "대상", ["decoder", "encoder", "both", "code-design", "other", "미상"]),
    ("code_type", "부호종류", ["QC-LDPC", "SC-LDPC", "regular", "irregular", "protograph", "기타", "미상"]),
    ("soft_quant", "연판정", ["hard-1bit", "soft-2~3bit", "soft-4bit+", "무관", "미상"]),
    ("hw_designed", "HW설계", ["O", "X", "미상"]),
    ("verification", "검증수준", ["이론", "시뮬", "FPGA", "ASIC합성", "실측", "미상"]),
    ("parallelism", "병렬화", ["없음", "부분", "완전병렬", "미상"]),
    ("correction_gain", "정정능력향상", ["O", "X", "N/A", "미상"]),
    ("improve_region", "개선영역", ["waterfall", "error-floor", "both", "N/A", "미상"]),
    ("iter_reduction", "iteration감소", ["O", "부분", "X", "N/A", "미상"]),
    ("latency", "latency", ["개선", "동등", "악화", "N/A", "미상"]),
]


def extract_published_year(published: str) -> str:
    matches = re.findall(r"(?:19|20)\d{2}", published or "")
    # IEEE published는 "6-8 April 2026"처럼 연도가 문자열 끝에 오고,
    # arXiv published는 ISO 날짜(YYYY-MM-DD...)라 연도가 하나뿐이다.
    return matches[-1] if matches else "미상"


def id_to_stem(paper_id: str) -> str:
    # results 저장 규칙(analysis_prompt.md)과 동일: ':'와 '/'를 '_'로 치환.
    return paper_id.replace(":", "_").replace("/", "_")


def venue_type(source: str, content_type: str) -> str:
    if source == "ieee":
        return "ieee_journal" if content_type == "journal" else "ieee_conference"
    if source == "arxiv":
        return "arxiv"
    return "other"


def load_filtered_in():
    conn = sqlite3.connect(DB_PATH)
    try:
        cur = conn.cursor()
        cur.execute("SELECT id, published, source, content_type FROM papers WHERE status = 'filtered_in'")
        rows = cur.fetchall()
    finally:
        conn.close()

    total_by_year_venue = Counter()
    stem_to_info = {}
    for paper_id, published, source, content_type in rows:
        year = extract_published_year(published)
        venue = venue_type(source, content_type)
        total_by_year_venue[(year, venue)] += 1
        stem_to_info[id_to_stem(paper_id)] = (paper_id, year, venue)
    return total_by_year_venue, stem_to_info


def parse_results(stem_to_info: dict):
    done_by_year_venue = Counter()
    unknown_files = []  # 결과 파일은 있으나 filtered_in DB에 대응 id가 없음
    folder_mismatch = []  # 결과 파일의 위치 폴더 연도 != DB published 연도
    duplicate_files = []  # 같은 논문 id가 여러 연도 폴더에 중복 저장됨
    json_parse_fail = []  # JSON 블록이 없거나 파싱 실패
    seen_stems = {}
    records = []

    for path in sorted(RESULTS_DIR.glob("*/*.md")):
        stem = path.stem
        folder_year = path.parent.name
        match = stem_to_info.get(stem)
        if match is None:
            unknown_files.append(f"{folder_year}/{path.name}")
            continue

        if stem in seen_stems:
            duplicate_files.append(f"{folder_year}/{path.name} (첫 위치: {seen_stems[stem]})")
            continue
        seen_stems[stem] = f"{folder_year}/{path.name}"

        paper_id, db_year, venue = match
        done_by_year_venue[(db_year, venue)] += 1
        if db_year != folder_year:
            folder_mismatch.append(f"{folder_year}/{path.name} (DB 발행연도: {db_year})")

        text = path.read_text(encoding="utf-8")
        m = JSON_BLOCK_RE.search(text)
        obj = {}
        if m:
            try:
                obj = json.loads(m.group(1))
            except (json.JSONDecodeError, ValueError):
                json_parse_fail.append(f"{folder_year}/{path.name}")
        else:
            json_parse_fail.append(f"{folder_year}/{path.name}")

        obj["_id"] = paper_id
        obj["_year"] = db_year
        obj["_venue_type"] = venue
        obj["_relpath"] = path.relative_to(BASE_DIR).as_posix()
        records.append(obj)

    return done_by_year_venue, records, unknown_files, folder_mismatch, duplicate_files, json_parse_fail


def fmt_ratio(done: int, total: int) -> str:
    if total == 0:
        return f"{done}/0" if done else "-"
    return f"{done}/{total} ({done / total:.0%})"


def build_progress_table(total_by_year_venue: Counter, done_by_year_venue: Counter):
    years = sorted(
        {y for (y, _v) in total_by_year_venue} | {y for (y, _v) in done_by_year_venue},
        key=lambda y: (y == "미상", int(y) if y != "미상" else 0),
    )

    lines = ["| 연도 | IEEE Journal | Conference | arXiv | 전체 |", "|---|---|---|---|---|"]
    grand_total = Counter()
    grand_done = Counter()
    grand_total_all = 0
    grand_done_all = 0

    for year in years:
        cells = [year]
        year_total = 0
        year_done = 0
        for venue_key, _label in VENUE_COLUMNS:
            t = total_by_year_venue.get((year, venue_key), 0)
            d = done_by_year_venue.get((year, venue_key), 0)
            grand_total[venue_key] += t
            grand_done[venue_key] += d
            year_total += t
            year_done += d
            cells.append(fmt_ratio(d, t))
        cells.append(fmt_ratio(year_done, year_total))
        grand_total_all += year_total
        grand_done_all += year_done
        lines.append("| " + " | ".join(cells) + " |")

    total_row = ["**합계**"]
    for venue_key, _label in VENUE_COLUMNS:
        total_row.append(f"**{fmt_ratio(grand_done[venue_key], grand_total[venue_key])}**")
    total_row.append(f"**{fmt_ratio(grand_done_all, grand_total_all)}**")
    lines.append("| " + " | ".join(total_row) + " |")

    return lines, grand_total_all, grand_done_all


def build_category_distributions(records: list) -> list:
    lines = [f"## 세부 카테고리별 분포 (완료 {len(records)}편 기준)"]
    for key, label, order in CATEGORY_FIELDS:
        counter = Counter(str(r.get(key)) if r.get(key) not in (None, "") else "미상" for r in records)
        total = sum(counter.values())
        keys_sorted = [k for k in order if k in counter] + [k for k in counter if k not in order]
        lines.append("")
        lines.append(f"### {label}")
        lines.append("| 값 | 편수 | 비율 |")
        lines.append("|---|---|---|")
        for k in keys_sorted:
            c = counter[k]
            lines.append(f"| {k} | {c} | {c / total:.1%} |")
    return lines


def _safe_cell(text) -> str:
    return str(text or "").replace("|", "/").replace("\n", " ").strip()


def build_top_recommend_list(records: list) -> list:
    top = [r for r in records if r.get("recommend") == "상"]
    portability_rank = {"상": 0, "중": 1, "하": 2}
    top.sort(key=lambda r: (
        portability_rank.get(r.get("portability"), 9),
        -(int(r["_year"]) if str(r.get("_year")).isdigit() else 0),
    ))

    lines = [
        f"## 추천도 '상' 논문 목록 ({len(top)}편) - Prime ECC 3.1 이식 우선 검토 대상",
        "",
        "| 연도 | 이식성 | 대상 | 논문 | 핵심기여 |",
        "|---|---|---|---|---|",
    ]
    for r in top:
        pid = r.get("id") or r.get("_id")
        title = _safe_cell(r.get("title"))
        contribution = _safe_cell(r.get("key_contribution"))
        link = f"[{_safe_cell(pid)}]({r['_relpath']})"
        paper_cell = f"{link}<br>{title}" if title else link
        lines.append(
            f"| {r.get('_year')} | {r.get('portability', '미상')} | {r.get('target', '미상')} | {paper_cell} | {contribution} |"
        )
    return lines


def main() -> None:
    total_by_year_venue, stem_to_info = load_filtered_in()
    done_by_year_venue, records, unknown_files, folder_mismatch, duplicate_files, json_parse_fail = parse_results(stem_to_info)

    lines = ["# Stage3 연도별 진행 현황", ""]

    progress_lines, total_sum, done_sum = build_progress_table(total_by_year_venue, done_by_year_venue)
    lines.append(f"- 전체 대상(filtered_in): {total_sum}편")
    lines.append(f"- 완료(stage3 결과): {done_sum}편 ({done_sum / total_sum:.1%})")
    lines.append("- 집계 기준: 총/완료 모두 DB `published` 연도 + `source`/`content_type`(IEEE Journal/Conference/arXiv) 기준으로 통일")
    lines.append("")
    lines.extend(progress_lines)
    lines.append("")

    lines.extend(build_category_distributions(records))
    lines.append("")

    lines.extend(build_top_recommend_list(records))
    lines.append("")

    if json_parse_fail:
        lines.append(f"## JSON 블록 파싱 실패 파일 ({len(json_parse_fail)}건, 위 카테고리 분포에서 제외됨)")
        for name in json_parse_fail:
            lines.append(f"- {name}")
        lines.append("")

    if unknown_files:
        lines.append("## DB(filtered_in)에 대응 id가 없는 결과 파일")
        for name in unknown_files:
            lines.append(f"- {name}")
        lines.append("")

    if duplicate_files:
        lines.append("## 중복 저장된 결과 파일 (같은 id가 여러 연도 폴더에 존재)")
        for name in duplicate_files:
            lines.append(f"- {name}")
        lines.append("")

    if folder_mismatch:
        lines.append(f"## 폴더 위치와 DB 발행연도가 다른 파일 ({len(folder_mismatch)}건, 진행률 계산에는 영향 없음)")
        for name in folder_mismatch:
            lines.append(f"- {name}")
        lines.append("")

    output = "\n".join(lines).rstrip() + "\n"
    OUTPUT_PATH.write_text(output, encoding="utf-8")
    print(f"wrote {OUTPUT_PATH} ({len(lines)} lines, 완료 {done_sum}/{total_sum}편)")


if __name__ == "__main__":
    main()
