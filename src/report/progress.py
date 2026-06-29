"""선별(Phase 2) 진행 현황 맵 생성 → review_progress.md.

연도 × 타입(conference/journal/arXiv)별로 '완료/전체'를 표로 출력한다.
완료 = status가 'new'가 아님(=선별 판단이 끝남).

    python -m src.report.progress
"""

import re
from collections import defaultdict
from datetime import datetime
from pathlib import Path

from src.db import get_conn

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
OUT = PROJECT_ROOT / "review_progress.md"

# 표 컬럼 순서 (content_type → 표시명)
COLS = [("conference", "conference"), ("journal", "journal"), ("preprint", "arXiv")]


def _year(published: str | None) -> str:
    m = re.search(r"(19|20)\d{2}", published or "")
    return m.group(0) if m else "????"


def generate() -> str:
    conn = get_conn()
    rows = conn.execute("SELECT content_type, published, status FROM papers").fetchall()
    conn.close()

    by_year = defaultdict(lambda: defaultdict(lambda: [0, 0]))   # year -> type -> [done, total]
    by_type = defaultdict(lambda: [0, 0])
    total = [0, 0]
    n_in = n_out = 0

    for r in rows:
        t = r["content_type"] if r["content_type"] in dict(COLS) else "other"
        y = _year(r["published"])
        done = 0 if r["status"] == "new" else 1
        by_year[y][t][0] += done; by_year[y][t][1] += 1
        by_type[t][0] += done;    by_type[t][1] += 1
        total[0] += done;         total[1] += 1
        if r["status"] == "filtered_in":
            n_in += 1
        elif r["status"] == "filtered_out":
            n_out += 1

    pct = (100 * total[0] // total[1]) if total[1] else 0
    stamp = datetime.now().strftime("%Y-%m-%d %H:%M")

    lines = [
        "# 선별(Phase 2) 진행 현황",
        "",
        f"> 생성: {stamp} · `python -m src.report.progress`로 갱신",
        "",
        "## 요약",
        f"- 전체 **{total[1]:,}편** · 선별 완료 **{total[0]:,}편** ({pct}%)",
        f"  - 통과(filtered_in) {n_in:,} / 제외(filtered_out) {n_out:,}",
        "- 타입별 완료/전체:",
    ]
    for key, name in COLS:
        d, t = by_type[key]
        lines.append(f"  - {name}: {d:,}/{t:,}")
    lines += ["", "## 연도별 진행 (완료/전체)", "",
              "| 연도 | conference | journal | arXiv | 합계 |",
              "|------|-----------|---------|-------|------|"]

    for y in sorted(by_year, reverse=True):
        cells = []
        row_done = row_tot = 0
        for key, _ in COLS:
            d, t = by_year[y][key]
            cells.append(f"{d}/{t}" if t else "–")
            row_done += d; row_tot += t
        lines.append(f"| {y} | {cells[0]} | {cells[1]} | {cells[2]} | {row_done}/{row_tot} |")

    return "\n".join(lines) + "\n"


def main():
    md = generate()
    OUT.write_text(md, encoding="utf-8")
    print(f"진행맵 생성: {OUT.relative_to(PROJECT_ROOT)}")


if __name__ == "__main__":
    main()
