"""Phase 2.5 — '알고리즘 측면 수정' 재분류.

filtered_in 논문 중 **기여가 HW 아키텍처(D)뿐인 논문을 제외**하기 위한 분류.
A(NAND 직접)·B(스토리지)·C(디코더 알고리즘)·E(코드설계) 중 하나라도 있으면 유지,
카테고리가 D만이면 제외.

filter_results.algo_mod 컬럼에 기록:
  1 = 알고리즘/코드/NAND 기여 있음(유지)
  0 = D(HW)만 = 제외 대상
  NULL = 미판정(파싱으로 카테고리 못 찾음 → 에이전트 재판정 필요)

명령:
  python -m src.stage1.algo_classify dry     # 파싱 분포만 출력(쓰기 없음)
  python -m src.stage1.algo_classify apply    # 컬럼 추가 + 비애매분 기록 + 애매분 목록 저장
  python -m src.stage1.algo_classify stats    # algo_mod 현황
"""

import argparse
import json
import re
import sys
from pathlib import Path

from src.db import get_conn, init_db

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass

# 카테고리 글자 집합을 reason 자유서술에서 추출.
# 관찰된 표기: "(C)", "(C/D)", "(A/C/D)", "(B/E)", "이식 가능 HW(D)", "코드설계(E)",
#   "카테고리 A", "A 직접 해당", "A/E 정통 부합", "A/E에 직접", 선두 "C:", "D —", "A/C/D:"
# 주의: "NAND 직접"의 D, "QC-LDPC"의 C 등 단어 내부 글자가 오탐되지 않도록
#   - 슬래시 묶음(A/E, C/D, A/C/D)은 영숫자 경계로 감싸 강한 신호로 채택
#   - 단일 글자는 괄호/'카테고리'/선두태그/'직접'(단어경계) 문맥에서만 채택
_SLASH = re.compile(r"(?<![A-Za-z0-9])([A-E](?:\s*[\/·+]\s*[A-E])+)(?![A-Za-z0-9])")
_PAREN = re.compile(r"\(([A-E](?:\s*[\/·,+]\s*[A-E])*)\)")
_KEY_POST = re.compile(r"카테고리\s*([A-E](?:\s*[\/·,+]\s*[A-E])*)")  # "카테고리 A/E"
_KEY_PRE = re.compile(r"(?<![A-Za-z0-9])([A-E](?:\s*[\/·,+]\s*[A-E])*)\s*카테고리")  # "A 카테고리"
_LEAD1 = re.compile(r"^\s*([A-E])\s*[:\-—]")                       # 선두 "C:" "D —"
_DIRECT = re.compile(r"(?<![A-Za-z])([A-E])\s*직접")               # "A 직접"(단어경계)
_ISIK = re.compile(r"(?<![A-Za-z0-9])([A-E])\s*이식")             # "D 이식 가능"
_COLON = re.compile(r"(?<![A-Za-z0-9])([A-E])\s*:")               # "C: ..." 어디서나


def parse_categories(reason: str | None) -> set[str]:
    if not reason:
        return set()
    cats: set[str] = set()
    for rx in (_SLASH, _PAREN, _KEY_POST, _KEY_PRE, _LEAD1, _DIRECT, _ISIK, _COLON):
        for m in rx.finditer(reason):
            cats.update(c for c in m.group(1) if c in "ABCDE")
    return cats


def classify(cats: set[str]) -> int | None:
    """1=유지, 0=D만(제외), None=애매(카테고리 미검출)."""
    if not cats:
        return None
    if cats == {"D"}:
        return 0
    return 1


def _rows():
    conn = get_conn()
    init_db(conn)
    rows = conn.execute(
        "SELECT f.paper_id, f.reason FROM filter_results f "
        "JOIN papers p ON p.id = f.paper_id WHERE p.status = 'filtered_in'"
    ).fetchall()
    conn.close()
    return rows


def dry():
    keep = excl = amb = 0
    amb_samples, excl_samples = [], []
    for r in _rows():
        v = classify(parse_categories(r["reason"]))
        if v == 1:
            keep += 1
        elif v == 0:
            excl += 1
            if len(excl_samples) < 8:
                excl_samples.append((r["paper_id"], r["reason"]))
        else:
            amb += 1
            if len(amb_samples) < 8:
                amb_samples.append((r["paper_id"], r["reason"]))
    total = keep + excl + amb
    print(f"=== algo_mod 파싱 분포 (filtered_in {total}편) ===")
    print(f"  유지(algo 기여 있음) : {keep}")
    print(f"  제외(D만/HW only)    : {excl}")
    print(f"  애매(카테고리 미검출) : {amb}  ← 에이전트 재판정 대상")
    print("--- 제외(D만) 샘플 ---")
    for pid, rs in excl_samples:
        print(f"  {pid}  {rs[:90]}")
    print("--- 애매 샘플 ---")
    for pid, rs in amb_samples:
        print(f"  {pid}  {(rs or '')[:90]}")


def add_column():
    conn = get_conn()
    init_db(conn)
    cols = {r[1] for r in conn.execute("PRAGMA table_info(filter_results)")}
    if "algo_mod" not in cols:
        conn.execute("ALTER TABLE filter_results ADD COLUMN algo_mod INTEGER")
        conn.commit()
        print("컬럼 추가: filter_results.algo_mod")
    else:
        print("컬럼 이미 존재: filter_results.algo_mod")
    conn.close()


def apply():
    add_column()
    conn = get_conn()
    init_db(conn)
    rows = conn.execute(
        "SELECT f.paper_id, f.reason FROM filter_results f "
        "JOIN papers p ON p.id = f.paper_id WHERE p.status = 'filtered_in'"
    ).fetchall()
    keep = excl = amb = 0
    ambiguous = []
    for r in rows:
        v = classify(parse_categories(r["reason"]))
        if v is None:
            amb += 1
            ambiguous.append({"id": r["paper_id"], "reason": r["reason"]})
            continue
        conn.execute("UPDATE filter_results SET algo_mod = ? WHERE paper_id = ?",
                     (v, r["paper_id"]))
        keep += (v == 1)
        excl += (v == 0)
    conn.commit()
    conn.close()

    out = PROJECT_ROOT / "_work" / "algo_ambiguous.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(ambiguous, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"기록 완료 — 유지 {keep} · 제외(D만) {excl} · 애매 {amb}(미기록)")
    print(f"애매분 목록: {out.relative_to(PROJECT_ROOT).as_posix()} (에이전트 재판정용)")


def batch(per: int = 10):
    """애매분(algo_mod IS NULL, filtered_in)을 에이전트 파일로 분할 — 재판정용."""
    from datetime import datetime
    conn = get_conn()
    init_db(conn)
    rows = conn.execute(
        "SELECT p.id, p.title, p.abstract, f.reason "
        "FROM filter_results f JOIN papers p ON p.id = f.paper_id "
        "WHERE p.status = 'filtered_in' AND f.algo_mod IS NULL "
        "ORDER BY p.id"
    ).fetchall()
    conn.close()
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    run_dir = PROJECT_ROOT / "_work" / f"algo_{stamp}"
    run_dir.mkdir(parents=True, exist_ok=True)
    n = 0
    for idx, start in enumerate(range(0, len(rows), per)):
        sl = rows[start:start + per]
        (run_dir / f"agent_{idx:02d}.json").write_text(
            json.dumps([dict(r) for r in sl], ensure_ascii=False, indent=2), encoding="utf-8")
        n += 1
    rel = run_dir.relative_to(PROJECT_ROOT).as_posix()
    print(f"애매분 {len(rows)}편 → {n}개 파일: {rel}/agent_NN.json (에이전트 {n}개)")
    print(f"RUN_DIR={rel}")


def applyjudge(path: str):
    """algo 재판정 JSON [{id, algo:"keep"|"drop", reason}] 을 algo_mod에 기록."""
    items = json.loads(Path(path).read_text(encoding="utf-8"))
    conn = get_conn()
    init_db(conn)
    ok = bad = 0
    for it in items:
        pid = it.get("id")
        a = (it.get("algo") or "").lower()
        if a not in ("keep", "drop"):
            bad += 1
            continue
        v = 1 if a == "keep" else 0
        cur = conn.execute(
            "UPDATE filter_results SET algo_mod = ? "
            "WHERE paper_id = ? AND algo_mod IS NULL", (v, pid))
        ok += cur.rowcount
    conn.commit()
    conn.close()
    print(f"algo_mod 기록: {ok}건 (무효 {bad})")


def stats():
    conn = get_conn()
    init_db(conn)
    print("=== algo_mod 현황 (filtered_in) ===")
    for r in conn.execute(
        "SELECT f.algo_mod, COUNT(*) n FROM filter_results f "
        "JOIN papers p ON p.id = f.paper_id WHERE p.status = 'filtered_in' "
        "GROUP BY f.algo_mod ORDER BY f.algo_mod"
    ):
        label = {1: "유지(algo)", 0: "제외(D만)", None: "미판정"}.get(r["algo_mod"], "?")
        print(f"  {label}: {r['n']}")
    conn.close()


def main():
    ap = argparse.ArgumentParser(description="Phase 2.5 알고리즘 수정 재분류")
    ap.add_argument("cmd", choices=["dry", "apply", "stats", "addcol", "batch", "applyjudge"])
    ap.add_argument("arg", nargs="?", help="applyjudge: 판정 JSON 경로")
    ap.add_argument("--per", type=int, default=10, help="batch: 에이전트당 편수")
    args = ap.parse_args()
    if args.cmd == "dry":
        dry()
    elif args.cmd == "apply":
        apply()
    elif args.cmd == "stats":
        stats()
    elif args.cmd == "addcol":
        add_column()
    elif args.cmd == "batch":
        batch(per=args.per)
    elif args.cmd == "applyjudge":
        applyjudge(args.arg)


if __name__ == "__main__":
    main()
