"""stage3 원본 결과(results/{연도}/{id}.md, 6,214편)를 무수정으로 두고,
그 위에 이식 후보 선별 축 4개(H/Q/R/L)를 추가로 재추출한다.

- **재분석 아님**: 논문 원문(PDF/txt)은 읽지 않는다. 오직 stage3 결과 md만 파싱한다.
- 각 md에서 (a) 하단 D섹션 JSON 블록, (b) 상단 A섹션 분류표의 `부호rate`/`부호length`/
  `연판정` 원문 문자열을 파싱한다. JSON의 code_rate는 범위표기 시 null이므로
  rate/length 는 **md 표 문자열이 소스**다.
- 선별 축(자세한 정의는 reselect/README.md):
  - **H** (hard decision): JSON `soft_quant == "hard-1bit"` (없으면 표 `연판정` 행 fallback).
  - **R** (high rate): rate 문자열의 (0,1] 소수·분수 최댓값 >= 0.8.
  - **L** (long length): length 문자열의 숫자(콤마 제거, `~` 범위는 상한) 최댓값 >= 16384 bit.
    단위 kB/KB 는 x8192, kbit/Kb 는 x1000 환산, 특이 단위는 환산하지 않고 별도 집계.
  - **Q 후보**: README 1차 키워드를 md 텍스트(분류표+요약+총평)에서 매칭. 단,
    `C.` 핀포인트 섹션(Prime ECC 모듈명이 논문과 무관하게 등장) 이후는 스캔 제외.

두 실행 모드:
  --scan   : H/R/L 판정 + Q 키워드 후보 추출 → q_candidates.jsonl + scan_summary.md
  --report : quant_tags.json(2차 agent 판정)을 반영해 최종 리포트/목록/JSON 생성
"""
import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path

BASE_DIR = Path(__file__).parent                 # criteria/stage3/reselect
STAGE3_DIR = BASE_DIR.parent                      # criteria/stage3
RESULTS_DIR = STAGE3_DIR / "results"              # criteria/stage3/results
PROJECT_ROOT = RESULTS_DIR.parents[2]             # 프로젝트 루트

# 출력 경로
Q_CANDIDATES_PATH = BASE_DIR / "q_candidates.jsonl"
SCAN_SUMMARY_PATH = BASE_DIR / "scan_summary.md"
QUANT_TAGS_PATH = BASE_DIR / "quant_tags.json"
REPORT_PATH = BASE_DIR / "reselect_report.md"
RESELECT_JSON_PATH = BASE_DIR / "reselect.json"
TAG_LIST_PATHS = {
    "H": BASE_DIR / "reselect_H.md",
    "Q": BASE_DIR / "reselect_Q.md",
    "R": BASE_DIR / "reselect_R.md",
    "L": BASE_DIR / "reselect_L.md",
}

RATE_THRESHOLD = 0.8
LENGTH_THRESHOLD = 16384  # bit (= 2KB x 8)

# 정규식 --------------------------------------------------------------------
# year_progress.py 와 동일한 JSON 블록 추출.
JSON_BLOCK_RE = re.compile(r"```json\s*(\{.*?\})\s*```", re.DOTALL)
# A섹션 분류표 행(| 라벨 | 값 |)에서 값 원문 추출.
RATE_ROW_RE = re.compile(r"^\|\s*부호rate\s*\|(.*?)\|", re.M)
LENGTH_ROW_RE = re.compile(r"^\|\s*부호length\s*\|(.*?)\|", re.M)
SOFT_ROW_RE = re.compile(r"^\|\s*연판정\s*\|(.*?)\|", re.M)
# C. 핀포인트 섹션 헤더(파일에 따라 `## C.` 또는 `### C.`).
C_HEADER_RE = re.compile(r"^#+\s*C\.", re.M)
D_HEADER_RE = re.compile(r"^#+\s*D\.", re.M)

# rate 파싱: 소수와 분수.
FRAC_RE = re.compile(r"(\d+)\s*/\s*(\d+)")
DEC_RE = re.compile(r"\d*\.\d+")
# 콤마 3자리 구분(16,384) 또는 일반 정수/소수.
NUM_RE = re.compile(r"\d{1,3}(?:,\d{3})+(?:\.\d+)?|\d+(?:\.\d+)?")

# length 특이 단위/기호(환산 불가 → 원문 그대로 별도 집계, 비트 환산 안 함).
#   byte 계열(MB/GB/byte/640B), 심볼/무한/소수(prime) 파라미터, 차원(×)·거듭제곱(^),
#   지수표기(1e6), 부분 미상(예: 25~미상).
LEN_SPECIAL_RE = re.compile(
    r"미상|MB|GB|KiB|MiB|byte|심볼|symbol|무한|소수|×|\^|\d+e\d+|\dB\b"
)
# 'k'/'K' 약어(예: 16k, 4K~64K, 64800(64k)). 비트 환산은 하지 않고(=k 무시) 참고 목록에만 노출.
#   단, kB/KB/kbit/Kb 는 아래에서 정식 단위로 환산하므로 제외한다.
LEN_KSHORT_RE = re.compile(r"\d[kK](?![Bb])")
# 정식 kilo 단위. byte(대문자 B) 먼저, 그 다음 bit(소문자 b).
LEN_BYTE_UNIT_RE = re.compile(r"[kK]B")     # kB, KB -> x8192 (1KB = 1024 byte = 8192 bit)
LEN_KBIT_UNIT_RE = re.compile(r"kbit|Kbit|[kK]b")  # kbit, Kb -> x1000 (1kbit = 1000 bit)

# Q 1차 키워드(대소문자 무시). 짧은 약어(LUT/MIM/RCQ/FAID)는 단어경계 매칭으로
# 부분문자열 오탐(solution 안의 'lut' 등)을 피한다. README 1차 키워드 목록과 1:1.
Q_KEYWORDS = [
    ("quantiz", re.compile(r"quantiz", re.I)),
    ("양자화", re.compile(r"양자화")),
    ("bit-width", re.compile(r"bit[-\s]?width", re.I)),
    ("저비트", re.compile(r"저비트")),
    ("low-bit", re.compile(r"low[-\s]bit", re.I)),
    ("저정밀", re.compile(r"저정밀")),
    ("low-precision", re.compile(r"low[-\s]precision", re.I)),
    ("low-resolution", re.compile(r"low[-\s]resolution", re.I)),
    ("저해상도", re.compile(r"저해상도")),
    ("finite-alphabet", re.compile(r"finite[-\s]alphabet", re.I)),
    ("FAID", re.compile(r"\bFAID\b", re.I)),
    ("RCQ", re.compile(r"\bRCQ\b", re.I)),
    ("MIM", re.compile(r"\bMIM\b", re.I)),  # \b 로 MIMO 오탐 제외
    ("information-bottleneck", re.compile(r"information[-\s]bottleneck", re.I)),
    ("정보병목", re.compile(r"정보병목")),
    ("fixed-point", re.compile(r"fixed[-\s]point", re.I)),
    ("고정소수점", re.compile(r"고정소수점")),
    ("LUT", re.compile(r"\bLUTs?\b", re.I)),
]


# 파싱 헬퍼 ----------------------------------------------------------------
def parse_rate(raw: str):
    """rate 원문에서 (0,1] 소수·분수를 모두 추출해 최댓값을 반환.

    반환: (rate_max 또는 None, status) — status in {"ok","미상","추출불가"}.
    """
    v = (raw or "").strip()
    if v == "" or v == "미상":
        return None, "미상"
    vals = []
    for a, b in FRAC_RE.findall(v):
        b = int(b)
        if b:
            x = int(a) / b
            if 0 < x <= 1.0:
                vals.append(x)
    for d in DEC_RE.findall(v):
        x = float(d)
        if 0 < x <= 1.0:
            vals.append(x)
    if not vals:
        # 소수·분수가 없으면 rate 1 (=1.0) 단독 표기만 예외적으로 인정.
        for tok in re.findall(r"(?<![\d./])\d+(?![\d./])", v):
            if int(tok) == 1:
                vals.append(1.0)
                break
    if not vals:
        return None, "추출불가"
    return max(vals), "ok"


def parse_length(raw: str):
    """length 원문에서 비트 최댓값을 추출한다.

    - 콤마 제거, `~` 범위는 자연히 상한(더 큰 값)이 최댓값으로 잡힌다.
    - kB/KB x8192, kbit/Kb x1000, 그 외는 bit.
    - 특이 단위/기호(byte·MB·심볼·×·^·지수표기·부분미상)는 환산하지 않고 status="특이".

    반환: (length_max 또는 None, status, k_short) —
      status in {"ok","미상","특이","추출불가"}, k_short 는 'k' 약어 표기 여부(참고용).
    """
    v = (raw or "").strip()
    if v == "" or v == "미상":
        return None, "미상", False
    if LEN_SPECIAL_RE.search(v):
        return None, "특이", False
    k_short = bool(LEN_KSHORT_RE.search(v))
    if LEN_BYTE_UNIT_RE.search(v):
        mult = 8192
    elif LEN_KBIT_UNIT_RE.search(v):
        mult = 1000
    else:
        mult = 1
    nums = [float(m.replace(",", "")) for m in NUM_RE.findall(v)]
    if not nums:
        return None, "추출불가", k_short
    return max(nums) * mult, "ok", k_short


def determine_hard(obj: dict, soft_row: str) -> bool:
    """H(hard-1bit) 판정. JSON soft_quant 우선, 없으면 표 `연판정` 행 fallback."""
    sq = obj.get("soft_quant")
    if sq is None or sq == "":
        return (soft_row or "").strip().startswith("hard-1bit")
    return sq == "hard-1bit"


def scan_q_keywords(text: str):
    """C. 핀포인트 섹션 이전(분류표+요약+총평)만 스캔해 Q 1차 키워드를 찾는다.

    C 헤더가 없으면 D 헤더/JSON 블록 앞까지로 잘라 D섹션 JSON 오탐을 막는다.
    반환: 매칭된 키워드 라벨 리스트(입력 순서, 중복 제거).
    """
    cut = None
    for rx in (C_HEADER_RE, D_HEADER_RE):
        m = rx.search(text)
        if m:
            cut = m.start()
            break
    if cut is None:
        j = text.find("```json")
        cut = j if j != -1 else len(text)
    head = text[:cut]
    matched = [label for label, rx in Q_KEYWORDS if rx.search(head)]
    return matched


# 전체 파싱 ----------------------------------------------------------------
def parse_all():
    """results/*/*.md 전량을 파싱해 논문별 레코드 리스트와 실패/특이 목록을 반환."""
    records = []
    parse_fail = []       # JSON 블록 없음/파싱 실패
    missing_rate_row = []  # 표에 부호rate 행 자체가 없음
    missing_length_row = []

    for path in sorted(RESULTS_DIR.glob("*/*.md")):
        sid = path.stem
        folder_year = path.parent.name
        rel = path.relative_to(PROJECT_ROOT).as_posix()

        text = path.read_text(encoding="utf-8")
        m = JSON_BLOCK_RE.search(text)
        obj = {}
        if m:
            try:
                obj = json.loads(m.group(1))
            except (json.JSONDecodeError, ValueError):
                parse_fail.append(rel)
        else:
            parse_fail.append(rel)

        rate_m = RATE_ROW_RE.search(text)
        length_m = LENGTH_ROW_RE.search(text)
        soft_m = SOFT_ROW_RE.search(text)
        if rate_m is None:
            missing_rate_row.append(sid)
        if length_m is None:
            missing_length_row.append(sid)

        rate_raw = rate_m.group(1).strip() if rate_m else ""
        length_raw = length_m.group(1).strip() if length_m else ""
        soft_raw = soft_m.group(1).strip() if soft_m else ""

        rate_max, rate_status = parse_rate(rate_raw)
        length_max, length_status, k_short = parse_length(length_raw)

        tag_H = determine_hard(obj, soft_raw)
        tag_R = rate_status == "ok" and rate_max is not None and rate_max >= RATE_THRESHOLD
        tag_L = length_status == "ok" and length_max is not None and length_max >= LENGTH_THRESHOLD

        matched = scan_q_keywords(text)

        year = obj.get("year")
        if year in (None, ""):
            year = int(folder_year) if folder_year.isdigit() else folder_year

        records.append({
            "sid": sid,
            "id": obj.get("id") or sid.replace("_", ":", 1),
            "title": obj.get("title") or "",
            "year": year,
            "folder_year": folder_year,
            "key_contribution": obj.get("key_contribution") or "",
            "portability": obj.get("portability") or "미상",
            "recommend": obj.get("recommend") or "미상",
            "md": rel,
            "rate_raw": rate_raw,
            "rate_max": rate_max,
            "rate_status": rate_status,
            "length_raw": length_raw,
            "length_max": length_max,
            "length_status": length_status,
            "length_kshort": k_short,
            "tag_H": tag_H,
            "tag_R": tag_R,
            "tag_L": tag_L,
            "q_matched": matched,
            "q_candidate": bool(matched),
        })

    return records, parse_fail, missing_rate_row, missing_length_row


# --scan --------------------------------------------------------------------
def run_scan():
    records, parse_fail, missing_rate_row, missing_length_row = parse_all()

    n = len(records)
    n_H = sum(r["tag_H"] for r in records)
    n_R = sum(r["tag_R"] for r in records)
    n_L = sum(r["tag_L"] for r in records)
    n_Q = sum(r["q_candidate"] for r in records)

    # 교집합(H/R/L + Q후보).
    def pair(a, b):
        return sum(1 for r in records if r[a] and r[b])

    inter = {
        "H∩R": pair("tag_H", "tag_R"),
        "H∩L": pair("tag_H", "tag_L"),
        "R∩L": pair("tag_R", "tag_L"),
        "H∩Q후보": pair("tag_H", "q_candidate"),
        "R∩Q후보": pair("tag_R", "q_candidate"),
        "L∩Q후보": pair("tag_L", "q_candidate"),
        "H∩R∩L": sum(1 for r in records if r["tag_H"] and r["tag_R"] and r["tag_L"]),
    }
    union_HRL = sum(1 for r in records if r["tag_H"] or r["tag_R"] or r["tag_L"])
    union_all = sum(1 for r in records if r["tag_H"] or r["tag_R"] or r["tag_L"] or r["q_candidate"])

    # rate/length 미상·특이·추출불가 집계.
    rate_unknown = [r["sid"] for r in records if r["rate_status"] == "미상"]
    rate_unparse = [(r["sid"], r["rate_raw"]) for r in records if r["rate_status"] == "추출불가"]
    length_unknown = [r["sid"] for r in records if r["length_status"] == "미상"]
    length_special = [(r["sid"], r["length_raw"]) for r in records
                      if r["length_status"] in ("특이", "추출불가")]
    length_kshort = [(r["sid"], r["length_raw"]) for r in records
                     if r["length_status"] == "ok" and r["length_kshort"]]

    # q_candidates.jsonl 작성.
    with Q_CANDIDATES_PATH.open("w", encoding="utf-8") as f:
        for r in records:
            if not r["q_candidate"]:
                continue
            row = {
                "sid": r["sid"],
                "id": r["id"],
                "md": r["md"],
                "title": r["title"],
                "year": r["year"],
                "key_contribution": r["key_contribution"],
                "matched": r["q_matched"],
            }
            f.write(json.dumps(row, ensure_ascii=False) + "\n")

    # scan_summary.md / stdout 공통 라인.
    lines = ["# Stage3 재선별 --scan 요약", ""]
    lines.append(f"- 전체 파싱 편수: {n}편")
    lines.append(f"- JSON 파싱 실패: {len(parse_fail)}건")
    lines.append(f"- 표 `부호rate` 행 없음: {len(missing_rate_row)}건 / `부호length` 행 없음: {len(missing_length_row)}건")
    lines.append("")
    lines.append("## 태그별 편수 (OR 조합)")
    lines.append("| 태그 | 정의 | 편수 |")
    lines.append("|---|---|---|")
    lines.append(f"| H | soft_quant=hard-1bit | {n_H} |")
    lines.append(f"| R | rate >= {RATE_THRESHOLD} | {n_R} |")
    lines.append(f"| L | length >= {LENGTH_THRESHOLD} bit | {n_L} |")
    lines.append(f"| Q(후보) | 1차 키워드 매칭 | {n_Q} |")
    lines.append(f"| **H∪R∪L** | (확정 3축 합집합) | **{union_HRL}** |")
    lines.append(f"| **H∪R∪L∪Q후보** | (Q후보 포함 합집합) | **{union_all}** |")
    lines.append("")
    lines.append("## 태그 교집합")
    lines.append("| 조합 | 편수 |")
    lines.append("|---|---|")
    for k, v in inter.items():
        lines.append(f"| {k} | {v} |")
    lines.append("")

    lines.append("## rate 파싱 불가 집계")
    lines.append(f"- 미상(값=미상/행없음): {len(rate_unknown)}건")
    lines.append(f"- 추출불가(숫자 없음): {len(rate_unparse)}건")
    if rate_unparse:
        lines.append("")
        lines.append("| sid | 원문 |")
        lines.append("|---|---|")
        for sid, raw in rate_unparse:
            lines.append(f"| {sid} | {raw} |")
    lines.append("")

    lines.append("## length 특이/파싱 불가 집계")
    lines.append(f"- 미상(값=미상/행없음): {len(length_unknown)}건")
    lines.append(f"- 특이 단위·추출불가(비트 환산 안 함): {len(length_special)}건")
    if length_special:
        lines.append("")
        lines.append("| sid | 원문 |")
        lines.append("|---|---|")
        for sid, raw in sorted(length_special):
            lines.append(f"| {sid} | {raw} |")
    lines.append("")
    lines.append(f"### 'k' 약어 표기(참고, k는 환산 안 하고 숫자만 비트로 처리): {len(length_kshort)}건")
    if length_kshort:
        lines.append("")
        lines.append("| sid | 원문 |")
        lines.append("|---|---|")
        for sid, raw in sorted(length_kshort):
            lines.append(f"| {sid} | {raw} |")
    lines.append("")

    if parse_fail:
        lines.append("## JSON 파싱 실패 파일")
        for name in parse_fail:
            lines.append(f"- {name}")
        lines.append("")
    if missing_rate_row:
        lines.append(f"## 표 `부호rate` 행 없는 파일 ({len(missing_rate_row)}건)")
        for sid in missing_rate_row:
            lines.append(f"- {sid}")
        lines.append("")

    output = "\n".join(lines).rstrip() + "\n"
    SCAN_SUMMARY_PATH.write_text(output, encoding="utf-8")

    sys.stdout.reconfigure(encoding="utf-8")
    print(output)
    print(f"[작성] {Q_CANDIDATES_PATH.relative_to(PROJECT_ROOT).as_posix()} (Q후보 {n_Q}편)")
    print(f"[작성] {SCAN_SUMMARY_PATH.relative_to(PROJECT_ROOT).as_posix()}")


# --report ------------------------------------------------------------------
def _safe_cell(text) -> str:
    return str(text or "").replace("|", "/").replace("\n", " ").strip()


def _sort_desc_year(records: list):
    return sorted(
        records,
        key=lambda r: (int(r["year"]) if str(r["year"]).isdigit() else -1, r["sid"]),
        reverse=True,
    )


def _build_tag_list_md(tag: str, tag_name: str, tagged: list) -> str:
    """태그별 목록 md(연도 내림차순, 상대경로 링크)."""
    lines = [f"# 재선별 {tag} ({tag_name}) 목록 - {len(tagged)}편", ""]
    lines.append("| 연도 | 이식성 | 추천도 | 논문 | 핵심기여 |")
    lines.append("|---|---|---|---|---|")
    for r in _sort_desc_year(tagged):
        link = f"[{r['sid']}](../results/{r['folder_year']}/{r['sid']}.md)"
        paper = f"{link}<br>{_safe_cell(r['title'])}" if r["title"] else link
        lines.append(
            f"| {r['year']} | {r['portability']} | {r['recommend']} | {paper} | {_safe_cell(r['key_contribution'])} |"
        )
    return "\n".join(lines).rstrip() + "\n"


def run_report():
    if not QUANT_TAGS_PATH.exists():
        print(
            f"[안내] {QUANT_TAGS_PATH.relative_to(PROJECT_ROOT).as_posix()} 가 없습니다.\n"
            "  먼저 --scan 으로 q_candidates.jsonl 을 만들고, agent 2차 판정 결과를\n"
            "  quant_tags.json ({\"sid\": {\"quant\": \"O\", \"reason\": \"...\"}, ...}) 로 저장한 뒤\n"
            "  다시 --report 를 실행하세요.",
            flush=True,
        )
        return

    quant_tags = json.loads(QUANT_TAGS_PATH.read_text(encoding="utf-8"))
    records, parse_fail, _missing_rate, _missing_len = parse_all()

    # Q 확정: quant_tags.json 에서 quant=="O" 인 sid.
    for r in records:
        entry = quant_tags.get(r["sid"]) or {}
        r["tag_Q"] = str(entry.get("quant", "")).upper() == "O"
        r["q_reason"] = entry.get("reason", "")

    def tagged(key):
        return [r for r in records if r.get(key)]

    tag_records = {
        "H": tagged("tag_H"),
        "Q": tagged("tag_Q"),
        "R": tagged("tag_R"),
        "L": tagged("tag_L"),
    }

    # ② 태그별 목록 md.
    for tag, name in [("H", "hard decision"), ("Q", "내부 로직 양자화"),
                      ("R", "high rate"), ("L", "long length")]:
        TAG_LIST_PATHS[tag].write_text(
            _build_tag_list_md(tag, name, tag_records[tag]), encoding="utf-8"
        )

    # ③ reselect.json (전 편수).
    payload = []
    for r in records:
        tags = [t for t in ("H", "Q", "R", "L") if r.get(f"tag_{t}")]
        payload.append({
            "sid": r["sid"],
            "id": r["id"],
            "title": r["title"],
            "year": r["year"],
            "tags": tags,
            "rate_max": r["rate_max"],
            "length_max": r["length_max"],
            "q_reason": r["q_reason"],
        })
    RESELECT_JSON_PATH.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    # ① reselect_report.md (집계 + 목록 링크).
    union = sum(1 for r in records if any(r.get(f"tag_{t}") for t in ("H", "Q", "R", "L")))
    lines = ["# Stage3 재선별 리포트", ""]
    lines.append(f"- 전체: {len(records)}편")
    lines.append(f"- 재선별(H∪Q∪R∪L): {union}편")
    lines.append("")
    lines.append("## 태그별 편수")
    lines.append("| 태그 | 이름 | 편수 | 목록 |")
    lines.append("|---|---|---|---|")
    names = {"H": "hard decision", "Q": "내부 로직 양자화", "R": "high rate", "L": "long length"}
    for tag in ("H", "Q", "R", "L"):
        rel = TAG_LIST_PATHS[tag].name
        lines.append(f"| {tag} | {names[tag]} | {len(tag_records[tag])} | [{rel}]({rel}) |")
    lines.append("")
    REPORT_PATH.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")

    sys.stdout.reconfigure(encoding="utf-8")
    print(f"[작성] {REPORT_PATH.name} / {RESELECT_JSON_PATH.name} / "
          + " / ".join(p.name for p in TAG_LIST_PATHS.values()))
    print(f"재선별(H∪Q∪R∪L): {union}편")


def main() -> None:
    ap = argparse.ArgumentParser(description="stage3 재선별 (H/Q/R/L)")
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--scan", action="store_true", help="H/R/L 판정 + Q 키워드 후보 추출")
    g.add_argument("--report", action="store_true", help="quant_tags.json 반영 최종 리포트 생성")
    args = ap.parse_args()
    if args.scan:
        run_scan()
    else:
        run_report()


if __name__ == "__main__":
    main()
