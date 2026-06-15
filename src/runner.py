"""수집 러너 진입점.

수집은 주기 스케줄이 아니라 **한 번에 전량(drain)** 받는 방식이다.

  python -m src.runner --drain          # 끝까지 전량 수집(arXiv+IEEE)
  python -m src.runner -n 100           # 1배치만(쿼리/버킷당 100건)
  python -m src.runner --sources arxiv  # 특정 소스만
  python -m src.runner --no-push        # git 업로드 생략

한 번의 실행(run_once)은:
  1. arXiv 단일 광범위 쿼리 + IEEE (term,year) 버킷을 커서 기반으로 수집(이어받기, 중복 제외)
  2. arXiv/IEEE 교차 중복 제거 + 카탈로그 재생성
  3. 실행 로그를 파일(logs/) + DB(run_log)에 기록
  4. 신규 수집이 있으면 DB·카탈로그를 git commit & push (GitHub 업로드)
"""

import argparse
import logging
import subprocess
from datetime import datetime, timezone
from pathlib import Path

from src import arxiv_collector, ieee_collector
from src.db import (
    get_conn, init_db, start_run, finish_run, checkpoint,
)

PROJECT_ROOT = Path(__file__).resolve().parent.parent
LOG_DIR = PROJECT_ROOT / "logs"

logger = logging.getLogger("runner")


def _setup_logging():
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    month = datetime.now(timezone.utc).strftime("%Y-%m")
    log_file = LOG_DIR / f"collect_{month}.log"
    fmt = logging.Formatter("%(asctime)s [%(levelname)s] %(name)s: %(message)s")

    root = logging.getLogger()
    root.setLevel(logging.INFO)
    # 중복 핸들러 방지
    if not any(isinstance(h, logging.FileHandler) for h in root.handlers):
        fh = logging.FileHandler(log_file, encoding="utf-8")
        fh.setFormatter(fmt)
        root.addHandler(fh)
    if not any(isinstance(h, logging.StreamHandler) and not isinstance(h, logging.FileHandler)
               for h in root.handlers):
        sh = logging.StreamHandler()
        sh.setFormatter(fmt)
        root.addHandler(sh)


def _git(*args: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["git", *args],
        cwd=str(PROJECT_ROOT),
        capture_output=True,
        text=True,
    )


def git_commit_push(new_total: int):
    """신규 수집이 있을 때만 DB·카탈로그를 커밋하고 push."""
    if new_total <= 0:
        logger.info("신규 수집 없음 → git 커밋 건너뜀")
        return

    # WAL 내용을 본 DB 파일에 합쳐 단일 파일로 커밋 가능하게 함
    conn = get_conn()
    checkpoint(conn)
    conn.close()

    _git("add", "data/papers.db", "papers")
    status = _git("status", "--porcelain")
    if not status.stdout.strip():
        logger.info("변경된 파일 없음 → git 커밋 건너뜀")
        return

    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M")
    msg = f"chore: 자동 수집 {stamp} (신규 {new_total}건)"
    commit = _git("commit", "-m", msg)
    if commit.returncode != 0:
        logger.warning("git commit 실패: %s", commit.stderr.strip())
        return
    logger.info("git commit: %s", msg)

    push = _git("push")
    if push.returncode != 0:
        logger.warning("git push 실패: %s", push.stderr.strip())
    else:
        logger.info("git push 완료")


def run_once(batch_size: int = 100, sources=("arxiv", "ieee"),
             download_pdf: bool = False, push: bool = True) -> dict:
    """1회 수집 사이클 실행."""
    _setup_logging()
    logger.info("=== 수집 사이클 시작 (batch_size=%d, sources=%s) ===",
                batch_size, ",".join(sources))

    conn = get_conn()
    init_db(conn)
    run_id = start_run(conn, "all")
    conn.close()

    totals = {"new": 0, "dup": 0, "fetched": 0}
    error = None

    try:
        if "arxiv" in sources:
            try:
                r = arxiv_collector.collect_batch(
                    batch_size=batch_size, download_pdf=download_pdf)
                for k in totals:
                    totals[k] += r[k]
            except Exception as e:
                logger.exception("arXiv 수집 실패: %s", e)
                error = f"arxiv: {e}"

        if "ieee" in sources:
            for term, year in ieee_collector.bucket_queries():
                try:
                    r = ieee_collector.collect_batch(term, year, batch_size=batch_size)
                    for k in totals:
                        totals[k] += r[k]
                except Exception as e:
                    logger.exception("IEEE 수집 실패(%s %d): %s", term, year, e)
                    error = f"ieee[{term}#{year}]: {e}"

        # 교차 중복 제거(내부에서 변경 시 카탈로그 재생성)
        try:
            arxiv_collector.dedup_cross_source()
        except Exception as e:
            logger.exception("교차 중복 제거 실패: %s", e)
    finally:
        conn = get_conn()
        finish_run(conn, run_id, new_count=totals["new"], dup_count=totals["dup"],
                   fetched=totals["fetched"], error=error)
        conn.close()

    logger.info("=== 수집 사이클 종료: 신규 %d, 중복 %d, 받음 %d ===",
                totals["new"], totals["dup"], totals["fetched"])

    if push:
        git_commit_push(totals["new"])

    return totals


def drain(batch_size: int = 100, sources=("arxiv", "ieee"),
          download_pdf: bool = False, push: bool = True,
          max_cycles: int = 1000) -> dict:
    """모든 쿼리가 끝(exhausted)에 도달할 때까지 반복 수집 — 1회성 전체 백필.

    push는 마지막에 한 번만 수행한다(매 사이클 커밋 방지).
    """
    _setup_logging()
    logger.info(">>> 전체 백필(drain) 시작 — 끝까지 수집 <<<")
    totals = {"new": 0, "dup": 0, "fetched": 0}

    for cycle in range(1, max_cycles + 1):
        if _all_exhausted(sources):
            logger.info("모든 쿼리가 끝에 도달 — drain 종료")
            break
        logger.info("--- drain 사이클 %d ---", cycle)
        r = run_once(batch_size=batch_size, sources=sources,
                     download_pdf=download_pdf, push=False)
        for k in totals:
            totals[k] += r[k]
        # 아무것도 못 받았으면(차단/에러 등) 무한루프 방지로 중단
        if r["fetched"] == 0:
            logger.info("이번 사이클 수집 0건 — drain 중단")
            break

    logger.info(">>> 전체 백필 종료: 신규 %d, 중복 %d, 받음 %d <<<",
                totals["new"], totals["dup"], totals["fetched"])
    if push:
        git_commit_push(totals["new"])
    return totals


def _all_exhausted(sources) -> bool:
    """대상 소스의 모든 등록된 쿼리 커서가 exhausted인지. 커서가 하나도 없으면 False."""
    conn = get_conn()
    init_db(conn)
    placeholders = ",".join("?" for _ in sources)
    rows = conn.execute(
        f"SELECT exhausted FROM collect_state WHERE source IN ({placeholders})",
        tuple(sources),
    ).fetchall()
    conn.close()
    if not rows:
        return False
    return all(r["exhausted"] for r in rows)


def main():
    parser = argparse.ArgumentParser(description="LDPC 논문 수집 러너")
    parser.add_argument("-n", "--batch-size", type=int, default=100,
                        help="쿼리당 1회 수집 건수(이어받기 단위, 기본 100)")
    parser.add_argument("--sources", default="arxiv,ieee",
                        help="수집 소스(쉼표 구분, 기본 arxiv,ieee)")
    parser.add_argument("--drain", action="store_true",
                        help="끝까지 전체 수집(1회성 백필). 미지정 시 1배치만.")
    parser.add_argument("--pdf", action="store_true", help="PDF도 다운로드")
    parser.add_argument("--no-push", action="store_true", help="git commit/push 생략")
    args = parser.parse_args()

    sources = tuple(s.strip() for s in args.sources.split(",") if s.strip())
    fn = drain if args.drain else run_once
    fn(batch_size=args.batch_size, sources=sources,
       download_pdf=args.pdf, push=not args.no_push)


if __name__ == "__main__":
    main()
