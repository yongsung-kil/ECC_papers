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
        status          TEXT NOT NULL DEFAULT 'new'
                        CHECK(status IN ('new','filtered_in','filtered_out',
                                         'analyzed','archived','deleted'))
    );

    CREATE TABLE IF NOT EXISTS filter_results (
        paper_id        TEXT PRIMARY KEY REFERENCES papers(id),
        relevance_score REAL,               -- 0.0 ~ 1.0
        reason          TEXT,
        filtered_at     TEXT NOT NULL
    );

    CREATE TABLE IF NOT EXISTS analyses (
        paper_id        TEXT PRIMARY KEY REFERENCES papers(id),
        summary         TEXT,
        key_ideas       TEXT,               -- JSON array
        nand_applicability TEXT,
        algorithm_notes TEXT,
        analyzed_at     TEXT NOT NULL
    );

    -- 쿼리별 수집 커서: 다음에 받을 위치(offset)를 보존해 이어받기.
    CREATE TABLE IF NOT EXISTS collect_state (
        source      TEXT NOT NULL,          -- 'arxiv' | 'ieee'
        query       TEXT NOT NULL,          -- 검색 쿼리 문자열(쿼리 단위 커서)
        next_offset INTEGER NOT NULL DEFAULT 0,
        total       INTEGER,                -- 마지막 확인 시점의 웹 전체 건수(있으면)
        exhausted   INTEGER NOT NULL DEFAULT 0,  -- 1=마지막 배치에서 끝 도달
        updated_at  TEXT,
        PRIMARY KEY (source, query)
    );

    -- 스케줄러 실행 로그
    CREATE TABLE IF NOT EXISTS run_log (
        id          INTEGER PRIMARY KEY AUTOINCREMENT,
        started_at  TEXT NOT NULL,
        finished_at TEXT,
        source      TEXT,                   -- 'arxiv' | 'ieee' | 'all'
        new_count   INTEGER NOT NULL DEFAULT 0,
        dup_count   INTEGER NOT NULL DEFAULT 0,
        fetched     INTEGER NOT NULL DEFAULT 0,
        error       TEXT
    );
    """)
    conn.commit()
    if close:
        conn.close()


# --- 수집 커서 ---------------------------------------------------------------

def get_cursor(conn: sqlite3.Connection, source: str, query: str) -> dict:
    """쿼리의 수집 커서를 반환. 없으면 offset=0 기본값."""
    row = conn.execute(
        "SELECT next_offset, total, exhausted FROM collect_state "
        "WHERE source = ? AND query = ?",
        (source, query),
    ).fetchone()
    if row is None:
        return {"next_offset": 0, "total": None, "exhausted": 0}
    return dict(row)


def set_cursor(conn: sqlite3.Connection, source: str, query: str,
               next_offset: int, total: int | None, exhausted: bool):
    """쿼리의 수집 커서를 갱신(upsert)."""
    conn.execute(
        """
        INSERT INTO collect_state (source, query, next_offset, total, exhausted, updated_at)
        VALUES (?, ?, ?, ?, ?, ?)
        ON CONFLICT(source, query) DO UPDATE SET
            next_offset = excluded.next_offset,
            total       = excluded.total,
            exhausted   = excluded.exhausted,
            updated_at  = excluded.updated_at
        """,
        (source, query, next_offset, total, 1 if exhausted else 0, _now()),
    )
    conn.commit()


# --- 논문 적재(중복 제외) -----------------------------------------------------

PAPER_COLUMNS = (
    "id", "source", "title", "authors", "abstract", "categories",
    "published", "updated", "doi", "pdf_url", "pdf_path",
    "collected_at", "status",
)


def insert_paper(conn: sqlite3.Connection, paper: dict) -> bool:
    """논문을 적재. ID가 이미 있으면 무시(중복 제외). 신규 삽입 시 True."""
    paper.setdefault("collected_at", _now())
    paper.setdefault("status", "new")
    paper.setdefault("pdf_path", None)
    cur = conn.execute(
        f"""
        INSERT OR IGNORE INTO papers ({', '.join(PAPER_COLUMNS)})
        VALUES ({', '.join(':' + c for c in PAPER_COLUMNS)})
        """,
        {c: paper.get(c) for c in PAPER_COLUMNS},
    )
    return cur.rowcount > 0


# --- 실행 로그 ---------------------------------------------------------------

def start_run(conn: sqlite3.Connection, source: str) -> int:
    cur = conn.execute(
        "INSERT INTO run_log (started_at, source) VALUES (?, ?)",
        (_now(), source),
    )
    conn.commit()
    return cur.lastrowid


def finish_run(conn: sqlite3.Connection, run_id: int, *,
               new_count: int, dup_count: int, fetched: int,
               error: str | None = None):
    conn.execute(
        "UPDATE run_log SET finished_at = ?, new_count = ?, dup_count = ?, "
        "fetched = ?, error = ? WHERE id = ?",
        (_now(), new_count, dup_count, fetched, error, run_id),
    )
    conn.commit()


def checkpoint(conn: sqlite3.Connection):
    """WAL 내용을 본 DB 파일에 합쳐 -wal/-shm 없이 커밋 가능하게 함."""
    conn.execute("PRAGMA wal_checkpoint(TRUNCATE)")
