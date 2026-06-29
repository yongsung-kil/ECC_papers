"""논문 id -> PDF 절대경로 매핑 헬퍼.

사용:
  python resolve_pdf.py ieee:7828079
  python resolve_pdf.py --next 5      # 분석 대상(algo_mod=1) 중 결과 없는 것 N개의 (id, pdf경로)
프로젝트 루트에서 실행 (cwd = Auto_Paper_Analysis).
"""
import os, sqlite3, sys, glob

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
MAIN_DB = os.path.join(ROOT, "data", "papers.db")
IEEE_PDF_DIR = os.path.join(ROOT, "data", "pdfs", "ieee")  # {YYYY}/{MM}/ieee_{ar}.pdf
ARXIV_DIR = os.path.join(ROOT, "data", "pdfs", "arxiv")


def pdf_for(pid: str):
    """id -> 존재하는 PDF 절대경로 (없으면 None). 경로에 년/월이 있어 glob만으로 충분 (download.db 불필요)."""
    if pid.startswith("ieee:"):
        ar = pid.split(":", 1)[1]
        hits = glob.glob(os.path.join(IEEE_PDF_DIR, "*", "*", f"ieee_{ar}.pdf"))
        return hits[0] if hits else None
    if pid.startswith("arxiv:"):
        aid = pid.split(":", 1)[1]
        # 파일명은 ':' 대신 '_' 등 변형 가능 → 후보 glob
        cand = aid.replace("/", "_")
        hits = glob.glob(os.path.join(ARXIV_DIR, "*", "*", f"{cand}*.pdf"))
        if not hits:
            base = cand.split("v")[0]
            hits = glob.glob(os.path.join(ARXIV_DIR, "*", "*", f"{base}*.pdf"))
        return hits[0] if hits else None
    return None


def next_targets(n: int, results_dir: str):
    """algo_mod=1 중 결과파일이 아직 없는 것 n개 (id, title, pdf경로)."""
    done = set()
    if os.path.isdir(results_dir):
        for f in os.listdir(results_dir):
            if f.endswith(".md"):
                done.add(f[:-3].replace("ieee_", "ieee:").replace("arxiv_", "arxiv:"))
    m = sqlite3.connect(MAIN_DB)
    out = []
    for pid, title in m.execute(
        "SELECT p.id, p.title FROM papers p JOIN filter_results f ON p.id=f.paper_id "
        "WHERE f.algo_mod=1 ORDER BY p.published DESC"
    ):
        if pid in done:
            continue
        pdf = pdf_for(pid)
        if pdf:
            out.append((pid, title, pdf))
        if len(out) >= n:
            break
    m.close()
    return out


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    if len(sys.argv) >= 3 and sys.argv[1] == "--next":
        rdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "results")
        for pid, title, pdf in next_targets(int(sys.argv[2]), rdir):
            print(f"{pid}\t{title[:60]}\t{pdf}")
    elif len(sys.argv) >= 2:
        print(pdf_for(sys.argv[1]) or "NOT_FOUND")
    else:
        print(__doc__)
