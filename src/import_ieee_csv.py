"""IEEE Xplore CSV 내보내기 파일을 DB로 import (전체 초록 확보용).

IEEE 검색 API의 abstract는 ~400자 미리보기로 잘린다. 반면 IEEE Xplore 웹의
Export → "Citation and Abstract" → CSV 에는 **전체 초록**이 들어 있다.

이 도구는 CSV를 읽어 **UPSERT** 한다:
  - 이미 있는 논문(같은 article number)  → 전체 초록으로 abstract 갱신(+ 빈 필드 보완)
  - 새 논문                                → 신규 삽입
중복은 article number(없으면 DOI) 기준으로 판정한다.

사용법:
    python -m src.import_ieee_csv                 # imports/ieee_csv/ 의 모든 *.csv
    python -m src.import_ieee_csv path/to/file.csv
    python -m src.import_ieee_csv path/to/dir
"""

import csv
import json
import logging
import re
import sys
from pathlib import Path

from src.db import get_conn, init_db, insert_paper, _now

logger = logging.getLogger(__name__)

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_DIR = PROJECT_ROOT / "imports" / "ieee_csv"

# IEEE CSV 컬럼명 후보(소문자 비교)
COL = {
    "title": ["document title", "title"],
    "authors": ["authors", "author"],
    "abstract": ["abstract"],
    "year": ["publication year", "year"],
    "doi": ["doi"],
    "pdf_url": ["pdf link", "pdf url", "pdf"],
    "terms": ["ieee terms", "author keywords", "index terms"],
    "article_number": ["article number", "articlenumber", "accession number"],
    "doc_identifier": ["document identifier", "document type"],
}


def _pick(row_lc: dict, keys: list[str]) -> str:
    for k in keys:
        if k in row_lc and row_lc[k]:
            return row_lc[k].strip()
    return ""


def _extract_arnumber(pdf_url: str, explicit: str) -> str | None:
    if explicit and explicit.strip().isdigit():
        return explicit.strip()
    for pat in (r"arnumber=(\d+)", r"/document/(\d+)"):
        m = re.search(pat, pdf_url or "")
        if m:
            return m.group(1)
    return None


def _content_type(doc_identifier: str) -> str | None:
    s = (doc_identifier or "").lower()
    for key, val in [("conference", "conference"), ("journal", "journal"),
                     ("magazine", "magazine"), ("standard", "standard"),
                     ("book", "book"), ("course", "course")]:
        if key in s:
            return val
    return None


def _row_to_paper(row: dict) -> dict | None:
    row_lc = {(k or "").strip().lower(): (v or "") for k, v in row.items()}

    title = _pick(row_lc, COL["title"])
    if not title:
        return None

    doi = _pick(row_lc, COL["doi"])
    pdf_url = _pick(row_lc, COL["pdf_url"])
    arnum = _extract_arnumber(pdf_url, _pick(row_lc, COL["article_number"]))

    if arnum:
        pid = f"ieee:{arnum}"
        pdf_url = f"https://ieeexplore.ieee.org/document/{arnum}"
    elif doi:
        pid = f"ieee-doi:{doi}"
    else:
        slug = re.sub(r"[^a-z0-9]+", "-", title.lower())[:60].strip("-")
        pid = f"ieee-title:{slug}"

    authors = [a.strip() for a in re.split(r"[;,]", _pick(row_lc, COL["authors"])) if a.strip()]
    terms = [t.strip() for t in re.split(r"[;,]", _pick(row_lc, COL["terms"])) if t.strip()]

    return {
        "id": pid,
        "source": "ieee",
        "title": title,
        "authors": json.dumps(authors),
        "abstract": _pick(row_lc, COL["abstract"]) or None,
        "categories": json.dumps(terms),
        "published": _pick(row_lc, COL["year"]) or None,
        "updated": None,
        "doi": doi or None,
        "pdf_url": pdf_url or None,
        "content_type": _content_type(_pick(row_lc, COL["doc_identifier"])),
    }


def _upsert(conn, paper: dict) -> str:
    """기존이면 전체 초록으로 갱신, 없으면 삽입. 반환: 'updated'|'inserted'|'skipped'."""
    row = conn.execute(
        "SELECT abstract, content_type, doi FROM papers WHERE id = ?", (paper["id"],)
    ).fetchone()
    if row is None:
        insert_paper(conn, paper)
        return "inserted"

    # 기존 논문: 더 긴(전체) 초록이면 갱신, 빈 필드 보완
    new_abs = paper.get("abstract") or ""
    old_abs = row["abstract"] or ""
    sets, vals = [], []
    if len(new_abs) > len(old_abs):
        sets.append("abstract = ?"); vals.append(new_abs)
    if paper.get("content_type") and not row["content_type"]:
        sets.append("content_type = ?"); vals.append(paper["content_type"])
    if paper.get("doi") and not row["doi"]:
        sets.append("doi = ?"); vals.append(paper["doi"])
    if not sets:
        return "skipped"
    vals.append(paper["id"])
    conn.execute(f"UPDATE papers SET {', '.join(sets)} WHERE id = ?", vals)
    return "updated"


def import_path(target: Path) -> dict:
    files = ([target] if target.is_file()
             else sorted(target.glob("*.csv")) if target.is_dir() else [])
    if not files:
        logger.warning("CSV 파일이 없습니다: %s", target)
        return {"inserted": 0, "updated": 0, "skipped": 0, "bad": 0, "files": 0}

    conn = get_conn()
    init_db(conn)
    tot = {"inserted": 0, "updated": 0, "skipped": 0, "bad": 0}
    for fp in files:
        cnt = {"inserted": 0, "updated": 0, "skipped": 0, "bad": 0}
        with open(fp, encoding="utf-8-sig", newline="") as f:
            for r in csv.DictReader(f):
                paper = _row_to_paper(r)
                if paper is None:
                    cnt["bad"] += 1
                    continue
                cnt[_upsert(conn, paper)] += 1
        conn.commit()
        for k in tot:
            tot[k] += cnt[k]
        logger.info("%s: 신규 %d, 갱신 %d, 변화없음 %d, 무효 %d",
                    fp.name, cnt["inserted"], cnt["updated"], cnt["skipped"], cnt["bad"])
    conn.close()
    tot["files"] = len(files)

    if tot["inserted"] or tot["updated"]:
        from src.arxiv_collector import export_catalog
        export_catalog()

    logger.info("=== import 완료: 파일 %d, 신규 %d, 갱신 %d, 변화없음 %d, 무효 %d ===",
                tot["files"], tot["inserted"], tot["updated"], tot["skipped"], tot["bad"])
    return tot


def main():
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s [%(levelname)s] %(message)s")
    target = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_DIR
    DEFAULT_DIR.mkdir(parents=True, exist_ok=True)
    print("결과:", import_path(target))


if __name__ == "__main__":
    main()
