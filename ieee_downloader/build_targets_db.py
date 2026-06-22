# -*- coding: utf-8 -*-
"""
다운로드 대상 DB 생성 (이 PC에서 1회 실행)

전체 papers.db 에서 '1차선별 통과 + IEEE' 논문만 떼어내
이 폴더에 download.db 를 만든다. 이 download.db 와 run.py 를
통째로 다른 PC(기관망)로 넘겨서 run.py 를 돌리면 PDF 가 받아진다.

생성되는 테이블: download_targets
    id          ieee:12345
    arnumber    12345               (stamp.jsp 용 문서번호)
    title
    published                       (원본 날짜 문자열, 지저분할 수 있음)
    year_month  YYYY-MM             (디렉토리 분류용, 미리 계산)
    doc_url     https://ieeexplore.ieee.org/document/12345
    status      pending|done|failed (다운로드 결과)
    pdf_path                        (성공 시 저장된 상대경로)
    attempts    시도 횟수
    last_error  마지막 오류 메시지
    updated_at  마지막 기록 시각
"""

import os
import re
import sqlite3
import sys
from datetime import datetime, timezone

HERE = os.path.dirname(os.path.abspath(__file__))
SRC_DB = os.path.join(HERE, "..", "data", "papers.db")   # 전체 DB (이 PC에만 있음)
OUT_DB = os.path.join(HERE, "download.db")               # 패키지로 넘길 DB

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

# ── catalog.py 의 _extract_year_month 와 동일 (자립형으로 복제) ──────────
_MONTH_MAP = {
    "jan": "01", "january": "01", "feb": "02", "february": "02",
    "mar": "03", "march": "03", "apr": "04", "april": "04",
    "may": "05", "jun": "06", "june": "06", "jul": "07", "july": "07",
    "aug": "08", "august": "08", "sep": "09", "sept": "09", "september": "09",
    "oct": "10", "october": "10", "nov": "11", "november": "11",
    "dec": "12", "december": "12",
}


def extract_year_month(published):
    if not published:
        return "unknown"
    if re.match(r"\d{4}-\d{2}", published):
        return published[:7]
    ym = re.search(r"(\d{4})", published)
    if not ym:
        return "unknown"
    year = ym.group(1)
    for token in published.lower().replace(".", "").split():
        if token in _MONTH_MAP:
            return f"{year}-{_MONTH_MAP[token]}"
    return f"{year}-01"


def arnumber_from(paper_id, pdf_url):
    m = re.search(r":(\d+)$", paper_id or "")
    if m:
        return m.group(1)
    m = re.search(r"/document/(\d+)", pdf_url or "")
    return m.group(1) if m else ""


def main():
    if not os.path.exists(SRC_DB):
        print(f"! 전체 DB 를 찾을 수 없음: {SRC_DB}", file=sys.stderr)
        sys.exit(1)

    src = sqlite3.connect(SRC_DB)
    src.row_factory = sqlite3.Row
    rows = src.execute(
        "SELECT id, title, published, pdf_url FROM papers "
        "WHERE source='ieee' AND status='filtered_in'"
    ).fetchall()
    src.close()
    print(f"통과 IEEE 논문: {len(rows)}편")

    if os.path.exists(OUT_DB):
        os.remove(OUT_DB)
    out = sqlite3.connect(OUT_DB)
    out.execute("""
        CREATE TABLE download_targets (
            id          TEXT PRIMARY KEY,
            arnumber    TEXT,
            title       TEXT,
            published   TEXT,
            year_month  TEXT,
            doc_url     TEXT,
            status      TEXT NOT NULL DEFAULT 'pending',
            pdf_path    TEXT,
            attempts    INTEGER NOT NULL DEFAULT 0,
            last_error  TEXT,
            updated_at  TEXT
        )
    """)
    now = datetime.now(timezone.utc).isoformat()
    n = 0
    for r in rows:
        arnum = arnumber_from(r["id"], r["pdf_url"])
        if not arnum:
            continue
        ym = extract_year_month(r["published"])
        doc_url = f"https://ieeexplore.ieee.org/document/{arnum}"
        out.execute(
            "INSERT OR REPLACE INTO download_targets "
            "(id, arnumber, title, published, year_month, doc_url, "
            " status, attempts, updated_at) "
            "VALUES (?,?,?,?,?,?, 'pending', 0, ?)",
            (r["id"], arnum, r["title"], r["published"], ym, doc_url, now),
        )
        n += 1
    out.commit()

    # 연도 분포 요약
    dist = out.execute(
        "SELECT substr(year_month,1,4) y, count(*) c "
        "FROM download_targets GROUP BY y ORDER BY y"
    ).fetchall()
    out.close()
    print(f"download.db 생성 완료: {n}편 등록 → {OUT_DB}")
    print("연도 분포:", ", ".join(f"{y}:{c}" for y, c in dist))


if __name__ == "__main__":
    main()
