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
- tags/q_reason: `reselect.json`이 있으면 sid로 조인 (없으면 tags=[], q_reason=null).

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
RESELECT_JSON = BASE_DIR / "reselect.json"
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
        info[id_to_stem(paper_id)] = (paper_id, year, venue_type(source, content_type))
    return info


def load_reselect_tags():
    """reselect.json이 있으면 sid → {tags, q_reason} 매핑을 만든다 (없으면 빈 dict).

    reselect.json 형식이 dict(sid 키) / list(sid 필드) 어느 쪽이든 수용한다.
    """
    if not RESELECT_JSON.exists():
        return {}
    data = json.loads(RESELECT_JSON.read_text(encoding="utf-8"))

    entries = []
    if isinstance(data, dict):
        # {"papers": [...]} 또는 {sid: {...}} 두 형태 모두 처리
        if "papers" in data and isinstance(data["papers"], list):
            entries = data["papers"]
        else:
            for sid, val in data.items():
                if isinstance(val, dict):
                    entries.append({"sid": sid, **val})
    elif isinstance(data, list):
        entries = data

    tags = {}
    for e in entries:
        if not isinstance(e, dict):
            continue
        sid = e.get("sid") or (id_to_stem(e["id"]) if e.get("id") else None)
        if not sid:
            continue
        tags[sid] = {
            "tags": e.get("tags", []) or [],
            "q_reason": e.get("q_reason"),
        }
    return tags


def build_paper(path: Path, db_info: dict, reselect_tags: dict, fails: list):
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
    paper_id, year, vtype = db_match

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

    tag_info = reselect_tags.get(stem, {})
    record["tags"] = tag_info.get("tags", [])
    record["q_reason"] = tag_info.get("q_reason")

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
    db_info = load_db_info()
    reselect_tags = load_reselect_tags()

    papers = []
    fails = []
    for path in sorted(RESULTS_DIR.glob("*/*.md")):
        rec = build_paper(path, db_info, reselect_tags, fails)
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
    if reselect_tags:
        print(f"  reselect.json 조인: {len(reselect_tags)}편에 태그 반영")
    else:
        print("  reselect.json 없음 → 모든 tags=[]")
    if fails:
        print(f"  파싱/조인 실패 {len(fails)}편:")
        for f in fails:
            print(f"    - {f}")
    else:
        print("  파싱 실패 0편")


if __name__ == "__main__":
    main()
