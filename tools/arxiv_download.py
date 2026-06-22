# -*- coding: utf-8 -*-
"""
arXiv 논문 PDF 일괄 다운로드 (1차선별 통과분)

이 세션 전용: arXiv 논문만 받는다. (IEEE 는 별도 세션/스크립트가 담당)

대상
----
papers/1차선별/통과/arxiv/ 아래 모든 catalog.csv 의 'PDF URL' 을 읽어
arXiv PDF 를 내려받는다. arXiv 는 공개 + 표준 TLS 라 사내망 SSL 우회 불필요.

저장 위치
--------
원본 디렉토리 구조를 그대로 미러링한다(추적성).
  papers/1차선별/통과/arxiv/2003/10/catalog.csv
    → papers/1차선별_pdf/arxiv/2003/10/<논문ID>.pdf

특징
----
- 이미 받은 파일은 건너뜀(재실행 시 이어받기).
- arXiv 예의상 요청 사이 DELAY 초 대기(과도한 요청 방지).
- requests 있으면 사용, 없으면 표준 라이브러리(urllib) 폴백.

사용법
------
  python tools/arxiv_download.py            # 전체(통과 353편) 다운로드
  python tools/arxiv_download.py 5          # 앞 5편만 (테스트용)
"""

import csv
import os
import re
import sys
import time

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass

# ── 경로 설정 ──────────────────────────────────────────────────────────
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)  # 프로젝트 루트
SRC_DIR = os.path.join(ROOT, "papers", "1차선별", "통과", "arxiv")
OUT_DIR = os.path.join(ROOT, "papers", "1차선별_pdf", "arxiv")

DELAY = 3       # 요청 사이 대기(초) — arXiv 예의
TIMEOUT = 60    # 요청 타임아웃(초)
# ───────────────────────────────────────────────────────────────────────

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/124.0 Safari/537.36")


def safe_filename(paper_id: str) -> str:
    """'arxiv:cond-mat/0310177v1' → 'cond-mat_0310177v1.pdf'"""
    pid = paper_id.split(":", 1)[-1]          # arxiv: 접두 제거
    pid = pid.replace("/", "_").replace("\\", "_")
    pid = re.sub(r"[^0-9A-Za-z._-]", "_", pid)
    return pid + ".pdf"


def normalize_pdf_url(url: str, paper_id: str) -> str:
    """PDF URL 컬럼이 비었거나 부실하면 ID 로 arXiv 표준 주소 구성."""
    url = (url or "").strip()
    if url.startswith("http"):
        return url
    pid = paper_id.split(":", 1)[-1]
    return f"https://arxiv.org/pdf/{pid}"


def collect_jobs(limit: int = 0):
    """(catalog 상대경로, paper_id, pdf_url) 목록 수집."""
    jobs = []
    for dirpath, _, files in os.walk(SRC_DIR):
        if "catalog.csv" not in files:
            continue
        rel = os.path.relpath(dirpath, SRC_DIR)  # 예: 2003/10
        with open(os.path.join(dirpath, "catalog.csv"),
                  encoding="utf-8-sig", newline="") as f:
            for row in csv.DictReader(f):
                pid = (row.get("ID") or "").strip()
                if not pid.startswith("arxiv:"):
                    continue
                url = normalize_pdf_url(row.get("PDF URL", ""), pid)
                jobs.append((rel, pid, url))
    jobs.sort()
    if limit > 0:
        jobs = jobs[:limit]
    return jobs


def _build_getter():
    """url → (bytes, content_type) 함수 반환."""
    headers = {"User-Agent": UA}
    try:
        import requests  # noqa
        sess = requests.Session()
        sess.headers.update(headers)

        def get_bytes(url):
            r = sess.get(url, timeout=TIMEOUT, allow_redirects=True)
            r.raise_for_status()
            return r.content, r.headers.get("Content-Type", "")
        return get_bytes
    except ImportError:
        import urllib.request
        opener = urllib.request.build_opener()
        opener.addheaders = list(headers.items())

        def get_bytes(url):
            with opener.open(url, timeout=TIMEOUT) as resp:
                return resp.read(), resp.headers.get("Content-Type", "")
        return get_bytes


def main():
    limit = int(sys.argv[1]) if len(sys.argv) > 1 and sys.argv[1].isdigit() else 0

    jobs = collect_jobs(limit)
    total = len(jobs)
    print(f"대상 arXiv 논문: {total}편")
    print(f"저장 위치      : {OUT_DIR}")
    if not total:
        print("받을 논문이 없습니다.")
        return

    get_bytes = _build_getter()
    ok = skip = fail = 0

    for i, (rel, pid, url) in enumerate(jobs, 1):
        out_dir = os.path.join(OUT_DIR, rel)
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, safe_filename(pid))

        tag = f"[{i}/{total}] {pid}"
        if os.path.exists(out_path) and os.path.getsize(out_path) > 0:
            skip += 1
            print(f"{tag}  ⏭  이미 있음")
            continue

        try:
            data, ctype = get_bytes(url)
            if data[:4] != b"%PDF":
                fail += 1
                print(f"{tag}  ✗ PDF 아님 (ct={ctype}, url={url})")
                continue
            with open(out_path, "wb") as f:
                f.write(data)
            ok += 1
            print(f"{tag}  ✓ {len(data):,} bytes")
        except Exception as e:
            fail += 1
            print(f"{tag}  ✗ 실패: {e}  (url={url})")

        time.sleep(DELAY)  # arXiv 예의상 대기

    print(f"\n완료 — 받음 {ok} / 건너뜀 {skip} / 실패 {fail}  (총 {total})")


if __name__ == "__main__":
    main()
