import sqlite3
from datetime import datetime, timezone
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent.parent / "data" / "papers.db"


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def get_conn() -> sqlite3.Connection:
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(DB_PATH))
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL")
    return conn


def init_db(conn: sqlite3.Connection | None = None):
    close = conn is None
    if conn is None:
        conn = get_conn()
    conn.executescript("""
    CREATE TABLE IF NOT EXISTS papers (
        id              TEXT PRIMARY KEY,   -- arxiv:2401.12345 / ieee:12345678
        source          TEXT NOT NULL,      -- 'arxiv' | 'ieee'
        title           TEXT NOT NULL,
        authors         TEXT NOT NULL,      -- JSON array
        abstract        TEXT,
        categories      TEXT,               -- JSON array
        published       TEXT,               -- ISO date
        updated         TEXT,
        doi             TEXT,
        pdf_url         TEXT,
        pdf_path        TEXT,               -- local path (relative)
        collected_at    TEXT NOT NULL,       -- ISO datetime
        content_type    TEXT,                -- journal|conference|magazine|standard|book|preprint|other
        status          TEXT NOT NULL DEFAULT 'new'
                        CHECK(status IN ('new','filtered_in','filtered_out',
                                         'analyzed','archived','deleted'))
    );

    -- Phase 2: 1차 선별 결과
    CREATE TABLE IF NOT EXISTS filter_results (
        paper_id        TEXT PRIMARY KEY REFERENCES papers(id),
        relevance_score REAL,               -- 0.0 ~ 1.0
        reason          TEXT,
        filtered_at     TEXT NOT NULL
    );

    -- Phase 3: 심층 분석 결과
    CREATE TABLE IF NOT EXISTS analyses (
        paper_id        TEXT PRIMARY KEY REFERENCES papers(id),
        summary         TEXT,
        key_ideas       TEXT,               -- JSON array
        nand_applicability TEXT,
        algorithm_notes TEXT,
        analyzed_at     TEXT NOT NULL
    );
    """)
    conn.commit()
    if close:
        conn.close()
