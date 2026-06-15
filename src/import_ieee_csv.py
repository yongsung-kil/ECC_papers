"""IEEE Xplore CSV 내보내기 파일을 DB로 import.

IEEE 크롤링(REST)이 봇 차단(HTTP 418)되므로, IEEE Xplore 웹에서 직접
검색 결과를 CSV로 내보내(Export → "Citation and Abstract" → CSV) 받은 뒤
이 도구로 import 한다. 여러 CSV(연도별 등)를 한 폴더에 모아 한 번에 병합 가능.
중복(같은 article number/DOI)은 자동 제외된다.

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

from src.db import get_conn, init_db, insert_paper

logger = logging.getLogger(__name__)

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_DIR = PROJECT_ROOT / "imports" / "ieee_csv"

# IEEE CSV 컬럼명은 버전마다 조금씩 다르므로 후보를 여럿 둔다(소문자 비교).
COL = {
    "title": ["document title", "title"],
    "authors": ["authors", "author"],
    "abstract": ["abstract"],
    "year": ["publication year", "year"],
    "doi": ["doi"],
    "pdf_url": ["pdf link", "pdf url", "pdf"],
    "terms": ["ieee terms", "author keywords", "index terms"],
    "article_number": ["article number", "articlenumber", "accession number"],
}


def _pick(row_lc: dict, keys: list[str]) -> str:
    for k in keys:
        if k in row_lc and row_lc[k]:
            return row_lc[k].strip()
    return ""


def _extract_arnumber(pdf_url: str, explicit: str) -> str | None:
    if explicit and explicit.strip().isdigit():
        return explicit.strip()
    m = re.search(r"arnumber=(\d+)", pdf_url or "")
    if m:
        return m.group(1)
    m = re.search(r"/document/(\d+)", pdf_url or "")
    if m:
        return m.group(1)
    return None


def _row_to_paper(row: dict) -> dict | None:
    row_lc = { (k or "").strip().lower(): (v or "") for k, v in row.items() }

    title = _pick(row_lc, COL["title"])
    if not title:
        return None

    doi = _pick(row_lc, COL["doi"])
    pdf_url = _pick(row_lc, COL["pdf_url"])
    arnum = _extract_arnumber(pdf_url, _pick(row_lc, COL["article_number"]))

    # id 우선순위: article number → DOI → 제목 슬러그(최후)
    if arnum:
        pid = f"ieee:{arnum}"
        if not pdf_url:
            pdf_url = f"https://ieeexplore.ieee.org/document/{arnum}"
    elif doi:
        pid = f"ieee-doi:{doi}"
    else:
        slug = re.sub(r"[^a-z0-9]+", "-", title.lower())[:60].strip("-")
        pid = f"ieee-title:{slug}"

    authors_raw = _pick(row_lc, COL["authors"])
    authors = [a.strip() for a in re.split(r"[;,]", authors_raw) if a.strip()]
    terms_raw = _pick(row_lc, COL["terms"])
    terms = [t.strip() for t in re.split(r"[;,]", terms_raw) if t.strip()]
    year = _pick(row_lc, COL["year"])

    return {
        "id": pid,
        "source": "ieee",
        "title": title,
        "authors": json.dumps(authors),
        "abstract": _pick(row_lc, COL["abstract"]) or None,
        "categories": json.dumps(terms),
        "published": year or None,
        "updated": None,
        "doi": doi or None,
        "pdf_url": pdf_url or None,
    }


def import_file(path: Path, conn) -> dict:
    new = dup = bad = 0
    # IEEE CSV는 BOM(utf-8-sig)이 흔함
    with open(path, encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            paper = _row_to_paper(row)
            if paper is None:
                bad += 1
                continue
            if insert_paper(conn, paper):
                new += 1
            else:
                dup += 1
    conn.commit()
    logger.info("%s: 신규 %d, 중복 %d, 무효 %d", path.name, new, dup, bad)
    return {"new": new, "dup": dup, "bad": bad}


def import_path(target: Path) -> dict:
    if target.is_dir():
        files = sorted(target.glob("*.csv"))
    elif target.is_file():
        files = [target]
    else:
        raise FileNotFoundError(f"경로 없음: {target}")

    if not files:
        logger.warning("CSV 파일이 없습니다: %s", target)
        return {"new": 0, "dup": 0, "bad": 0, "files": 0}

    conn = get_conn()
    init_db(conn)
    totals = {"new": 0, "dup": 0, "bad": 0}
    for fp in files:
        r = import_file(fp, conn)
        for k in totals:
            totals[k] += r[k]
    conn.close()
    totals["files"] = len(files)

    if totals["new"] > 0:
        from src.arxiv_collector import export_catalog
        export_catalog()

    logger.info("=== IEEE CSV import 완료: 파일 %d개, 신규 %d, 중복 %d, 무효 %d ===",
                totals["files"], totals["new"], totals["dup"], totals["bad"])
    return totals


def main():
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s [%(levelname)s] %(message)s")
    target = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_DIR
    DEFAULT_DIR.mkdir(parents=True, exist_ok=True)
    r = import_path(target)
    print(f"\n결과: {r}")


if __name__ == "__main__":
    main()
