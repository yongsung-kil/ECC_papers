"""stage3 결과 6,214편을 정적 웹 뷰어용 단일 JSON(`docs/papers.json`)으로 내보낸다.

데이터 소스 3종을 논문(sid) 단위로 합친다.
- `criteria/stage3/results/{연도}/*.md` 하단 ```json 블록: 카테고리/판정 필드 전량
  (단, 사내 코드 관련 메모인 `todo_check` 필드는 공개 페이지에서 제외).
- 같은 md 상단 2열 표의 `부호rate`/`부호length` **원문 문자열**: JSON 블록의
  code_rate/code_length는 범위표기 시 null이라, 범위·분수를 살리려 표를 소스로 쓴다.
- `data/papers.db`(status='filtered_in'): 발행 연도와 venue 구분
  (IEEE Journal / IEEE Conference / arXiv)을 year_progress.py와 동일 방식으로 얻는다.

추가 파생 필드:
- rate_max : 표 rate 문자열에서 (0,1] 범위의 소수·분수 최댓값 (불가 시 null).
- length_max: 표 length 문자열에서 비트 최댓값 (콤마 제거, `~`는 상한, kB→×8192; 불가 시 null).
- dq/dq_reason: 디코더양자화 3값. quant_tags.json에서 quant=="O"면 "핵심"(reason 동반),
  아니면 quant_body_tags.json의 bq("있음"/"없음"/"미상")과 그 reason, 둘 다 없으면 "없음"/null.
- month: 발행 월(1~12, 불명 null). `data/pdfs/{venue}/{연}/{월}/{stem}` 폴더 구조에서 취하고
  (arxiv sid 접두 별칭 처리), DB published 파싱값으로 교차검증(불일치 시 경로 우선·건수 보고).

출력: `ensure_ascii=False`, `separators=(",",":")`로 크기를 아낀다. 표준 라이브러리만 사용.
"""
import json
import re
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).parent                       # criteria/stage3/reselect
STAGE3_DIR = BASE_DIR.parent                           # criteria/stage3
RESULTS_DIR = STAGE3_DIR / "results"
REPO_ROOT = STAGE3_DIR.parent.parent                  # 저장소 루트
DB_PATH = REPO_ROOT / "data" / "papers.db"
PDFS_DIR = REPO_ROOT / "data" / "pdfs"                    # {venue}/{연}/{월}/{stem}.{pdf,txt}
QUANT_TAGS_JSON = BASE_DIR / "quant_tags.json"            # 핵심 판정 (quant O/X)
QUANT_BODY_TAGS_JSON = BASE_DIR / "quant_body_tags.json"  # 본문 스니펫 판정 (bq 있음/없음/미상)
OUTPUT_PATH = REPO_ROOT / "docs" / "papers.json"

# md 하단 ```json 블록 (year_progress.py와 동일 regex)
JSON_BLOCK_RE = re.compile(r"```json\s*(\{.*?\})\s*```", re.DOTALL)
# 상단 2열 표의 부호rate / 부호length 행
RATE_ROW_RE = re.compile(r"^\|\s*부호rate\s*\|\s*(.*?)\s*\|", re.M)
LENGTH_ROW_RE = re.compile(r"^\|\s*부호length\s*\|\s*(.*?)\s*\|", re.M)

# 공개 페이지에 싣지 않을 JSON 필드 (사내 코드 관련 메모)
EXCLUDE_JSON_FIELDS = {"todo_check"}

# JSON 블록에서 그대로 옮길 필드 (id/year/venue는 별도 처리)
PASS_THROUGH_FIELDS = [
    "title", "portability", "nand_relevance", "target", "code_type",
    "soft_quant", "key_contribution", "hw_designed", "verification",
    "complexity", "parallelism", "throughput_gbps", "mem_routing",
    "correction_gain", "improve_region", "iter_reduction", "latency",
    "recommend", "caveat",
]


def extract_published_year(published: str) -> str:
    """DB published 문자열에서 발행 연도를 뽑는다 (year_progress.py와 동일).

    IEEE published는 "6-8 April 2026"처럼 연도가 끝에 오고,
    arXiv published는 ISO 날짜라 연도가 하나뿐이라 마지막 매치를 쓴다.
    """
    matches = re.findall(r"(?:19|20)\d{2}", published or "")
    return matches[-1] if matches else "미상"


def id_to_stem(paper_id: str) -> str:
    """results 저장 규칙과 동일하게 ':'와 '/'를 '_'로 치환한다."""
    return paper_id.replace(":", "_").replace("/", "_")


MONTH_RE = re.compile(
    r"\b(jan(?:uary)?|feb(?:ruary)?|mar(?:ch)?|apr(?:il)?|may|jun(?:e)?|jul(?:y)?"
    r"|aug(?:ust)?|sep(?:t|tember)?|oct(?:ober)?|nov(?:ember)?|dec(?:ember)?)\.?\b",
    re.IGNORECASE,
)
MONTH_NUM = {"jan": 1, "feb": 2, "mar": 3, "apr": 4, "may": 5, "jun": 6,
             "jul": 7, "aug": 8, "sep": 9, "oct": 10, "nov": 11, "dec": 12}


def parse_published_month(published: str):
    """DB published 문자열에서 발행 월(1~12)을 파싱. 불가 시 None (교차검증용).

    arXiv는 ISO(YYYY-MM-DD), IEEE는 "8-10 Oct. 2013"/"April 2026"처럼 월명 표기.
    """
    if not published:
        return None
    m_iso = re.search(r"(?:19|20)\d{2}-(\d{2})(?:-\d{2})?", published)
    if m_iso:
        mm = int(m_iso.group(1))
        if 1 <= mm <= 12:
            return mm
    m = MONTH_RE.search(published)
    if m:
        return MONTH_NUM[m.group(1)[:3].lower()]
    return None


def build_month_map() -> dict:
    """data/pdfs/{venue}/{연}/{월}/{stem}.(pdf|txt) → stem → month(int|None).

    arxiv 파일 stem에는 'arxiv_' 접두가 없으므로 'arxiv_'+stem 별칭도 등록한다
    (quant_body_scan.build_sid_map과 동일 규칙).
    """
    month_map = {}
    if not PDFS_DIR.exists():
        return month_map
    for p in PDFS_DIR.rglob("*"):
        if p.suffix.lower() not in (".pdf", ".txt"):
            continue
        parts = p.relative_to(PDFS_DIR).parts       # (venue, 연, 월, 파일명)
        if len(parts) < 4:
            continue
        venue, mm = parts[0], parts[2]
        month = int(mm) if mm.isdigit() and 1 <= int(mm) <= 12 else None
        stem = p.stem
        month_map[stem] = month
        if venue == "arxiv" and not stem.startswith("arxiv_"):
            month_map["arxiv_" + stem] = month
    return month_map


def venue_type(source: str, content_type: str) -> str:
    """DB source/content_type을 vtype(ieee_journal|ieee_conference|arxiv|other)으로."""
    if source == "ieee":
        return "ieee_journal" if content_type == "journal" else "ieee_conference"
    if source == "arxiv":
        return "arxiv"
    return "other"


def parse_rate_max(text):
    """rate 문자열에서 (0,1] 범위의 소수·분수 최댓값을 구한다. 없으면 None.

    - 분수 a/b는 실수로 환산 (예: 8/9 → 0.889).
    - 범위(0.5~0.9)·콤마열거(0.5, 0.75)는 모든 값을 모아 최댓값.
    - 1 초과값(예: 1.2, 2 bits/channel use)·기호식은 무시 → None.
    """
    if not text:
        return None
    values = []
    # 분수 a/b
    for a, b in re.findall(r"(\d+(?:\.\d+)?)\s*/\s*(\d+(?:\.\d+)?)", text):
        try:
            v = float(a) / float(b)
        except ZeroDivisionError:
            continue
        if 0 < v <= 1:
            values.append(v)
    # 분수 토큰 제거 후 소수 추출
    rest = re.sub(r"\d+(?:\.\d+)?\s*/\s*\d+(?:\.\d+)?", " ", text)
    for tok in re.findall(r"\d+\.\d+", rest):
        v = float(tok)
        if 0 < v <= 1:
            values.append(v)
    # rate가 정확히 1인 경우(정수 1 단독)만 별도 허용
    for tok in re.findall(r"(?<![\d.])\d+(?![\d.])", rest):
        if float(tok) == 1:
            values.append(1.0)
    if not values:
        return None
    return round(max(values), 4)


def parse_length_max(text):
    """length 문자열에서 비트 최댓값을 구한다. 없으면 None.

    - 콤마는 이 데이터에서 예제 구분자로만 쓰인다(예: '504, 1008', '16200,64800').
      천단위 구분(1,234) 표기는 코퍼스에 존재하지 않으므로 콤마를 '제거'해 이어
      붙이면 '120,273,504,255'→120억 같은 허위값이 나온다. 따라서 콤마는 값
      **구분자**로 보고 공백 치환한 뒤 각 숫자를 개별 값으로 취급해 최댓값을 쓴다.
    - 범위(576~2304)도 모든 값 중 최댓값.
    - kB/KB/KByte/KiB 단위는 바이트→비트로 ×8192.
    - 단순 정수는 비트 그대로.
    """
    if not text:
        return None
    text = text.replace(",", " ")
    values = []
    # 바이트 단위(kB 계열) → ×8192
    for m in re.finditer(r"(\d+(?:\.\d+)?)\s*(?:KByte|KiB|KB|kB)\b", text):
        values.append(float(m.group(1)) * 8192)
    # kB 토큰 제거 후 남은 정수(비트) 추출
    rest = re.sub(r"\d+(?:\.\d+)?\s*(?:KByte|KiB|KB|kB)\b", " ", text)
    for tok in re.findall(r"\d+", rest):
        values.append(float(tok))
    if not values:
        return None
    mx = max(values)
    return int(mx) if mx == int(mx) else round(mx, 2)


def load_db_info():
    """filtered_in 논문의 sid → (id, year:int, vtype) 매핑을 만든다."""
    conn = sqlite3.connect(DB_PATH)
    try:
        cur = conn.cursor()
        cur.execute(
            "SELECT id, published, source, content_type "
            "FROM papers WHERE status = 'filtered_in'"
        )
        rows = cur.fetchall()
    finally:
        conn.close()

    info = {}
    for paper_id, published, source, content_type in rows:
        year_str = extract_published_year(published)
        year = int(year_str) if year_str.isdigit() else None
        db_month = parse_published_month(published)
        info[id_to_stem(paper_id)] = (paper_id, year, venue_type(source, content_type), db_month)
    return info


def load_quant_tags():
    """quant_tags.json → sid → {"quant": "O"|"X", "reason": ...}. 없으면 빈 dict."""
    if not QUANT_TAGS_JSON.exists():
        return {}
    return json.loads(QUANT_TAGS_JSON.read_text(encoding="utf-8"))


def load_quant_body_tags():
    """quant_body_tags.json → sid → {"bq": "있음"|"없음"|"미상", "reason": ...}. 없으면 빈 dict."""
    if not QUANT_BODY_TAGS_JSON.exists():
        return {}
    return json.loads(QUANT_BODY_TAGS_JSON.read_text(encoding="utf-8"))


def derive_dq(stem: str, quant_tags: dict, body_tags: dict):
    """디코더양자화 3값을 산출한다: 핵심(quant=="O") > 본문판정(bq) > 없음.

    반환: (dq, dq_reason). 핵심이면 quant_tags의 reason, 본문 판정이면 body_tags의
    reason, 어느 쪽에도 없으면 ("없음", None).
    """
    qt = quant_tags.get(stem)
    if qt and qt.get("quant") == "O":
        return "핵심", qt.get("reason")
    bt = body_tags.get(stem)
    if bt:
        return bt.get("bq"), bt.get("reason")
    return "없음", None


def build_paper(path: Path, db_info: dict, quant_tags: dict, body_tags: dict,
                month_map: dict, fails: list, mismatches: list):
    """md 한 편을 papers.json 레코드(dict)로 변환. 실패 시 None."""
    stem = path.stem
    text = path.read_text(encoding="utf-8")

    m = JSON_BLOCK_RE.search(text)
    if not m:
        fails.append(f"{path.parent.name}/{path.name} (JSON 블록 없음)")
        return None
    try:
        obj = json.loads(m.group(1))
    except (json.JSONDecodeError, ValueError) as exc:
        fails.append(f"{path.parent.name}/{path.name} (JSON 파싱 실패: {exc})")
        return None

    db_match = db_info.get(stem)
    if db_match is None:
        fails.append(f"{path.parent.name}/{path.name} (filtered_in DB에 없음)")
        return None
    paper_id, year, vtype, db_month = db_match

    # month: 경로 폴더 우선, 없으면 DB 파싱값 폴백. 둘 다 있고 다르면 경로 우선 + 불일치 집계
    path_month = month_map.get(stem)
    if path_month is not None and db_month is not None and path_month != db_month:
        mismatches.append((stem, path_month, db_month))
    month = path_month if path_month is not None else db_month

    # code_rate/code_length: md 표 원문 문자열 우선, 없으면 JSON 블록 값으로 폴백
    rate_row = RATE_ROW_RE.search(text)
    len_row = LENGTH_ROW_RE.search(text)
    code_rate = rate_row.group(1) if rate_row else _as_str(obj.get("code_rate"))
    code_length = len_row.group(1) if len_row else _as_str(obj.get("code_length"))

    record = {
        "sid": stem,
        "id": paper_id,
        "title": obj.get("title"),
        "year": year if year is not None else obj.get("year"),
        "month": month,
        "venue": obj.get("venue"),
        "vtype": vtype,
    }
    for key in PASS_THROUGH_FIELDS:
        if key == "title":
            continue
        record[key] = obj.get(key)

    record["code_rate"] = code_rate
    record["rate_max"] = parse_rate_max(code_rate)
    record["code_length"] = code_length
    record["length_max"] = parse_length_max(code_length)

    dq, dq_reason = derive_dq(stem, quant_tags, body_tags)
    record["dq"] = dq
    record["dq_reason"] = dq_reason

    record["md"] = path.relative_to(REPO_ROOT).as_posix()

    # 만약을 위해 제외 필드가 흘러들지 않았는지 확정 제거
    for f in EXCLUDE_JSON_FIELDS:
        record.pop(f, None)
    return record


def _as_str(value):
    """JSON 블록의 숫자/문자 값을 표시용 문자열로 (None은 그대로 None)."""
    if value is None:
        return None
    return str(value)


def main() -> None:
    import datetime
    from collections import Counter
    db_info = load_db_info()
    quant_tags = load_quant_tags()
    body_tags = load_quant_body_tags()
    month_map = build_month_map()

    papers = []
    fails = []
    mismatches = []
    for path in sorted(RESULTS_DIR.glob("*/*.md")):
        rec = build_paper(path, db_info, quant_tags, body_tags, month_map, fails, mismatches)
        if rec is not None:
            papers.append(rec)

    # 연도 desc, 그다음 sid로 안정 정렬 (뷰어 기본 정렬과 무관, 재현성용)
    papers.sort(key=lambda r: (-(r["year"] or 0), r["sid"]))

    generated = datetime.date.today().isoformat()
    out = {"generated": generated, "total": len(papers), "papers": papers}

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT_PATH.open("w", encoding="utf-8") as fh:
        json.dump(out, fh, ensure_ascii=False, separators=(",", ":"))

    size_mb = OUTPUT_PATH.stat().st_size / (1024 * 1024)
    print(f"wrote {OUTPUT_PATH}")
    print(f"  총 {len(papers)}편, 생성일 {generated}, 크기 {size_mb:.2f} MB")
    dist = Counter(p["dq"] for p in papers)
    order = ["핵심", "있음", "없음", "미상"]
    parts = [f"{k} {dist[k]}" for k in order if dist.get(k)]
    for k in dist:
        if k not in order:
            parts.append(f"{k} {dist[k]}")
    print("  dq 분포: " + " / ".join(parts))
    month_null = sum(1 for p in papers if p.get("month") is None)
    print(f"  month: null {month_null}편 / 경로·DB 불일치 {len(mismatches)}건")
    for stem, pm, dm in mismatches[:5]:
        print(f"    - {stem}: path={pm} db={dm}")
    if fails:
        print(f"  파싱/조인 실패 {len(fails)}편:")
        for f in fails:
            print(f"    - {f}")
    else:
        print("  파싱 실패 0편")


if __name__ == "__main__":
    main()
