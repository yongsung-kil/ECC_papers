"""1차 선별(Phase 2) 도구 — 병렬 워크플로(select_workflow.js)와 짝.

수집은 끝났고, 이 모듈은 미선별 논문을 다루는 3개 명령만 제공한다:
  - `batch` : 미선별 논문을 최신연도부터 실행폴더(_work/{타임스탬프}/agent_NN.json)로 분할
  - `apply` : 워크플로가 낸 판정 JSON을 DB(filter_results + papers.status)에 기록
  - `stats` : 선별 현황 출력

판정 JSON 형식 (리스트) — 점수 없이 포함/제외 이분법:
  [{"id": "arxiv:2401.12345", "decision": "in", "reason": "한 줄 근거"}, ...]
  - decision: "in"(포함) | "out"(제외)
"""

import argparse
import json
import re
import sys
from datetime import datetime
from pathlib import Path

from src.db import get_conn, init_db, _now

PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Windows 콘솔(cp949)에서도 한글/유니코드가 깨지거나 크래시하지 않도록 UTF-8 강제
try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass


def apply_judgments(items: list[dict]) -> dict:
    conn = get_conn()
    init_db(conn)

    applied = 0
    skipped = []
    for it in items:
        pid = it.get("id")
        decision = (it.get("decision") or "").lower()
        if decision not in ("in", "out"):
            skipped.append((pid, "decision은 'in'|'out' 이어야 함"))
            continue
        exists = conn.execute("SELECT 1 FROM papers WHERE id = ?", (pid,)).fetchone()
        if not exists:
            skipped.append((pid, "papers에 없는 id"))
            continue

        status = "filtered_in" if decision == "in" else "filtered_out"
        conn.execute(
            "INSERT OR REPLACE INTO filter_results "
            "(paper_id, relevance_score, reason, filtered_at) VALUES (?, ?, ?, ?)",
            (pid, it.get("score"), it.get("reason"), _now()),
        )
        conn.execute("UPDATE papers SET status = ? WHERE id = ?", (status, pid))
        applied += 1
    conn.commit()
    conn.close()

    print(f"적용 완료: {applied}건")
    for pid, why in skipped:
        print(f"  건너뜀: {pid} — {why}")
    return {"applied": applied, "skipped": skipped}


def show_stats():
    conn = get_conn()
    init_db(conn)
    print("=== 선별 현황 ===")
    for r in conn.execute("SELECT status, COUNT(*) n FROM papers GROUP BY status"):
        print(f"  {r['status']}: {r['n']}")
    print("=== 최근 포함(filtered_in) 샘플 ===")
    for r in conn.execute(
        "SELECT f.paper_id, f.reason, p.title "
        "FROM filter_results f JOIN papers p ON p.id = f.paper_id "
        "WHERE p.status = 'filtered_in' "
        "ORDER BY f.filtered_at DESC LIMIT 15"
    ):
        print(f"  {r['paper_id']}  {r['title'][:50]}  — {r['reason'] or ''}")
    conn.close()


def verify_run(run_dir: str) -> dict:
    """DB 기록 전 judgments.json 무결성 검증 — agent가 잘못된 id를 줬는지 확인.

    하드 에러(있으면 apply 금지):
      - DB에 없는 id        → apply가 건너뛰어 판정 유실
      - 배치 밖 id          → 실재하지만 담당 배치 아님 = 엉뚱한 논문에 적용 위험
      - decision != in/out  → 무효 판정
      - 중복 id             → 같은 논문 이중 판정
    경고(에러 아님):
      - 판정 누락(판정 < 할당) → 빠진 논문은 status='new'로 남아 다음 청크 재처리
    """
    rd = PROJECT_ROOT / run_dir
    jf = rd / "judgments.json"
    if not jf.exists():
        print(f"[verify] ❌ judgments.json 없음: {run_dir}")
        return {"ok": False, "reason": "no_judgments"}

    judgments = json.loads(jf.read_text(encoding="utf-8"))
    assigned = set()
    for af in sorted(rd.glob("agent_*.json")):
        for p in json.loads(af.read_text(encoding="utf-8")):
            assigned.add(p["id"])

    conn = get_conn()
    init_db(conn)
    db_ids = {r[0] for r in conn.execute("SELECT id FROM papers")}
    conn.close()

    bad_id, bad_dec, off_batch, dup = [], [], [], []
    seen = set()
    for it in judgments:
        pid = it.get("id")
        dec = (it.get("decision") or "").lower()
        if pid in seen:
            dup.append(pid)
        seen.add(pid)
        if pid not in db_ids:
            bad_id.append(pid)
            continue
        if assigned and pid not in assigned:
            off_batch.append(pid)
        if dec not in ("in", "out"):
            bad_dec.append(pid)

    errors = len(bad_id) + len(bad_dec) + len(off_batch) + len(dup)
    judged_assigned = len(seen & assigned) if assigned else None
    missing = (len(assigned) - judged_assigned) if assigned else None

    print(f"[verify] {run_dir} — 판정 {len(judgments)} / 할당 "
          f"{len(assigned) if assigned else '?(agent파일없음)'}")
    print(f"  DB없는 id {len(bad_id)} · 배치밖 id {len(off_batch)} · "
          f"decision오류 {len(bad_dec)} · 중복 {len(dup)}")
    for pid in bad_id[:10]:
        print(f"    ❌ DB없는 id: {pid}")
    for pid in off_batch[:10]:
        print(f"    ❌ 배치밖 id(엉뚱한 적용 위험): {pid}")
    for pid in bad_dec[:10]:
        print(f"    ❌ decision 오류: {pid}")
    for pid in dup[:10]:
        print(f"    ❌ 중복 id: {pid}")
    if missing:
        print(f"  ⚠️ 판정 누락 {missing}편 (status='new'로 남아 다음 청크 재처리)")
    if not assigned:
        print("  ⚠️ agent_*.json이 없어 '배치밖/누락'은 검증 불가 (id·decision·중복만 확인)")

    ok = errors == 0
    print("[verify] " + ("✅ 통과 — apply 진행 가능" if ok
                         else f"❌ 하드에러 {errors}건 — apply 금지"))
    return {"ok": ok, "errors": errors, "bad_id": bad_id, "off_batch": off_batch,
            "bad_dec": bad_dec, "dup": dup, "missing": missing}


def _pub_year(published: str | None) -> int:
    """published 문자열에서 4자리 연도 추출(없으면 0). 정렬용."""
    m = re.search(r"(19|20)\d{2}", published or "")
    return int(m.group(0)) if m else 0


def make_batches(limit: int, per: int, base_dir: str) -> dict:
    """미선별 논문을 실행 폴더(base_dir/{타임스탬프}/agent_NN.json)로 분할 — **최신 연도부터**.

    병렬 선별용. 메인은 초록을 읽지 않고 분할만 하며, 각 에이전트가 자기 파일만 읽는다.
    판정 결과(judgments.json)도 같은 실행 폴더에 모은다.
    실행 폴더는 추적성을 위해 **모두 보존**한다(정리는 나중에 수동으로).
    """
    conn = get_conn()
    init_db(conn)
    conn.create_function("pub_year", 1, _pub_year)
    rows = conn.execute(
        """
        SELECT p.id, p.source, p.title, p.abstract, p.published
        FROM papers p LEFT JOIN filter_results f ON p.id = f.paper_id
        WHERE f.paper_id IS NULL AND p.status = 'new'
        ORDER BY pub_year(p.published) DESC, p.published DESC, p.id
        LIMIT ?
        """,
        (limit,),
    ).fetchall()
    conn.close()

    base = PROJECT_ROOT / base_dir
    base.mkdir(parents=True, exist_ok=True)

    run_dir = base / datetime.now().strftime("%Y%m%d_%H%M%S")
    run_dir.mkdir(parents=True, exist_ok=True)

    n_files = 0
    for idx, start in enumerate(range(0, len(rows), per)):
        sl = rows[start:start + per]
        (run_dir / f"agent_{idx:02d}.json").write_text(
            json.dumps([dict(r) for r in sl], ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        n_files += 1

    rel = run_dir.relative_to(PROJECT_ROOT).as_posix()
    print(f"미선별 {len(rows)}편 → {n_files}개 파일: {rel}/agent_NN.json (에이전트 {n_files}개)")
    print(f"RUN_DIR={rel}")
    return {"papers": len(rows), "files": n_files, "run_dir": rel}


def main():
    parser = argparse.ArgumentParser(description="1차 선별(Phase 2) 도구")
    sub = parser.add_subparsers(dest="cmd")

    p_apply = sub.add_parser("apply", help="판단 결과(JSON) 적용")
    p_apply.add_argument("file", nargs="?", help="JSON 파일 경로(없으면 stdin)")

    p_verify = sub.add_parser("verify", help="DB 기록 전 judgments.json 무결성 검증")
    p_verify.add_argument("run_dir", help="실행 폴더(예: _work/20260618_144429)")

    sub.add_parser("stats", help="선별 현황")

    p_batch = sub.add_parser("batch", help="미선별 논문을 실행 폴더로 분할(병렬 선별용)")
    p_batch.add_argument("-n", type=int, default=100, help="한 청크 편수(기본 100)")
    p_batch.add_argument("--per", type=int, default=10, help="에이전트당 편수(기본 10)")
    p_batch.add_argument("--dir", default="_work",
                         help="출력 베이스 폴더(기본 _work, 하위에 타임스탬프 실행폴더 생성)")

    args = parser.parse_args()

    if args.cmd == "apply":
        raw = open(args.file, encoding="utf-8").read() if args.file else sys.stdin.read()
        apply_judgments(json.loads(raw))
    elif args.cmd == "verify":
        result = verify_run(args.run_dir)
        sys.exit(0 if result["ok"] else 1)
    elif args.cmd == "stats":
        show_stats()
    elif args.cmd == "batch":
        make_batches(limit=args.n, per=args.per, base_dir=args.dir)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
