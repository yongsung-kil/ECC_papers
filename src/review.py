"""1차 선별(Phase 2) 도구 — LLM(Claude Code 세션)이 직접 구동.

API를 호출하지 않는다. 대신:
  1. `--pending [N]` 으로 미선별 논문(제목·초록)을 출력하면
  2. 세션의 Claude가 각 논문의 NAND 플래시 관련성을 읽고 판단한 뒤
  3. 판단 결과(JSON)를 `--apply` 로 DB(filter_results)에 기록한다.

판단 JSON 형식 (리스트) — 점수 없이 포함/제외 이분법:
  [
    {"id": "arxiv:2401.12345", "decision": "in",
     "reason": "NAND 플래시 LDPC 디코더 지연시간 개선 직접 관련"},
    ...
  ]
  - decision: "in"(포함) | "out"(제외)
  - reason:   판단 근거 한 줄
"""

import argparse
import json
import re
import sys
from datetime import datetime
from pathlib import Path

from src.db import get_conn, init_db, _now

PROJECT_ROOT = Path(__file__).resolve().parent.parent
CRITERIA_PATH = PROJECT_ROOT / "criteria" / "selection_criteria.md"

# Windows 콘솔(cp949)에서도 한글/유니코드가 깨지거나 크래시하지 않도록 UTF-8 강제
try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass

# NAND 관련성 힌트용 키워드(판단 보조 표시. 자동 필터 아님)
NAND_HINTS = [
    "nand", "flash", "ssd", "solid-state", "solid state", "storage",
    "memory", "read disturb", "retention", "wear", "error floor",
    "soft decision", "soft information", "llr", "quantization",
]


def _highlight_hints(text: str) -> list[str]:
    if not text:
        return []
    low = text.lower()
    return [k for k in NAND_HINTS if k in low]


def _print_criteria_header():
    """선별 기준서를 출력 맨 앞에 붙여, 판단 주체(Claude)가 매번 같은 기준을 적용하도록 한다."""
    if CRITERIA_PATH.exists():
        print("<!-- 아래 논문을 판단하기 전에 반드시 이 기준을 적용하세요 -->")
        print(CRITERIA_PATH.read_text(encoding="utf-8"))
        print("\n---\n")
    else:
        print(f"<!-- 기준서 없음: {CRITERIA_PATH} (먼저 작성 필요) -->\n")


def list_pending(limit: int | None = None, as_json: bool = False,
                 with_criteria: bool = True):
    conn = get_conn()
    init_db(conn)
    rows = conn.execute(
        """
        SELECT p.id, p.source, p.title, p.abstract, p.published
        FROM papers p
        LEFT JOIN filter_results f ON p.id = f.paper_id
        WHERE f.paper_id IS NULL AND p.status = 'new'
        ORDER BY p.source, p.collected_at
        """
    ).fetchall()
    conn.close()

    if limit:
        rows = rows[:limit]

    if as_json:
        print(json.dumps([dict(r) for r in rows], ensure_ascii=False, indent=2))
        return

    if not rows:
        print("미선별 논문이 없습니다.")
        return

    if with_criteria:
        _print_criteria_header()

    print(f"# 미선별 논문 {len(rows)}건\n")
    for i, r in enumerate(rows, 1):
        hints = _highlight_hints(f"{r['title']} {r['abstract']}")
        print(f"## [{i}] {r['id']}  ({r['source']})")
        print(f"- **제목**: {r['title']}")
        print(f"- **발행**: {(r['published'] or 'N/A')[:10]}")
        if hints:
            print(f"- **NAND 힌트**: {', '.join(hints)}")
        print(f"- **초록**: {r['abstract'] or 'N/A'}")
        print()


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

    p_pending = sub.add_parser("pending", help="미선별 논문 출력(기준서 포함)")
    p_pending.add_argument("-n", type=int, default=None, help="최대 건수")
    p_pending.add_argument("--json", action="store_true", help="JSON으로 출력")
    p_pending.add_argument("--no-criteria", action="store_true",
                           help="기준서 헤더 생략")

    p_apply = sub.add_parser("apply", help="판단 결과(JSON) 적용")
    p_apply.add_argument("file", nargs="?", help="JSON 파일 경로(없으면 stdin)")

    sub.add_parser("stats", help="선별 현황")

    p_batch = sub.add_parser("batch", help="미선별 논문을 실행 폴더로 분할(병렬 선별용)")
    p_batch.add_argument("-n", type=int, default=100, help="한 청크 편수(기본 100)")
    p_batch.add_argument("--per", type=int, default=10, help="에이전트당 편수(기본 10)")
    p_batch.add_argument("--dir", default="_work",
                         help="출력 베이스 폴더(기본 _work, 하위에 타임스탬프 실행폴더 생성)")

    args = parser.parse_args()

    if args.cmd == "pending":
        list_pending(limit=args.n, as_json=args.json,
                     with_criteria=not args.no_criteria)
    elif args.cmd == "apply":
        raw = open(args.file, encoding="utf-8").read() if args.file else sys.stdin.read()
        apply_judgments(json.loads(raw))
    elif args.cmd == "stats":
        show_stats()
    elif args.cmd == "batch":
        make_batches(limit=args.n, per=args.per, base_dir=args.dir)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
