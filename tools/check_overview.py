"""상위 페이지(docs/index.html) 검사기.

실행: python tools/check_overview.py
검사에 실패하면 실패 목록을 찍고 종료 코드 1로 끝난다.
"""
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

# 페이지에 반드시 들어가야 하는 글. 설계 문서의 문구 정본과 블록도 명세에서 옮겨 적었다.
REQUIRED_TEXTS = [
    "AI-agent 활용 Prime ECC 개발",
    "PRIME ECC PROJECT",
    # 사이드바
    "개요",
    "Prime ECC 최적화",
    "성능 결과",
    "논문과 특허 분석",
    "논문 탐색기",
    "아이디어 구현",
    "적용 이력",
    "로드맵",
    # 메인 블록도 레인 1
    "Prime ECC (원본)",
    "사람이 만든 C++ 코드",
    "동작 검증과 속도 개선",
    "Light Prime ECC",
    "검증된 알고리즘 적용",
    "다음 세대",
    "결과 분석과 시행착오 기록",
    # 메인 블록도 레인 2
    "논문 수집",
    "IEEE 저널과 학회, arXiv",
    "전수 분석과 선별",
    "적용 가능 논문 선별",
    "특허 수집과 분석",
    # 메인 블록도 레인 3
    "아이디어 구현과 최적화",
    "정정 성능과 처리량 평가",
    "성능개선 아이디어",
    # 레인을 잇는 곁말
    "실험 바탕으로 넘김",
    "무엇을 시도할지 넘김",
    "검증 끝난 것만 원본으로",
]

# 페이지에 반드시 들어가야 하는 수치.
REQUIRED_NUMBERS = ["22,225", "6,222", "2,783", "1.9배"]

# 사이드바 항목 수와 준비 중 표시 수.
SIDEBAR_ITEM_COUNT = 8
SIDEBAR_WIP_COUNT = 6

fails = []


def check(ok, message):
    if not ok:
        fails.append(message)


def strip_code_blocks(html):
    """style과 script 안쪽을 지운다. 눈에 보이는 글만 남기기 위함이다."""
    html = re.sub(r"<style\b.*?</style>", " ", html, flags=re.S | re.I)
    html = re.sub(r"<script\b.*?</script>", " ", html, flags=re.S | re.I)
    return html


def visible_text(html):
    """태그를 걷어내고 눈에 보이는 글만 남긴다."""
    return re.sub(r"<[^>]+>", " ", strip_code_blocks(html))


def main():
    index = DOCS / "index.html"
    papers = DOCS / "papers.html"
    data = DOCS / "papers.json"

    check(index.exists(), "docs/index.html 이 없다")
    check(papers.exists(), "docs/papers.html 이 없다")
    check(data.exists(), "docs/papers.json 이 없다")

    if not index.exists():
        report()
        return

    html = index.read_text(encoding="utf-8")

    # 1. 반드시 들어가야 하는 글
    for text in REQUIRED_TEXTS:
        check(text in html, f"글이 빠졌다: {text}")

    # 2. 반드시 들어가야 하는 수치
    for number in REQUIRED_NUMBERS:
        check(number in html, f"수치가 빠졌다: {number}")

    # 3. 모든 SVG 가 올바른 XML 인지
    svgs = re.findall(r"<svg\b.*?</svg>", html, flags=re.S)
    check(len(svgs) >= 4, f"SVG 가 4개 이상이어야 한다 (메인 1개, 보조 3개). 지금 {len(svgs)}개")
    for i, svg in enumerate(svgs, 1):
        try:
            ET.fromstring(svg)
        except ET.ParseError as err:
            fails.append(f"{i}번째 SVG 가 올바른 XML 이 아니다: {err}")

    # 4. 바깥 자원을 불러오지 않는지
    for pattern, label in [
        (r"<link\b[^>]*href\s*=\s*[\"']https?://", "외부 스타일시트"),
        (r"<script\b[^>]*src\s*=\s*[\"']https?://", "외부 스크립트"),
        (r"<img\b[^>]*src\s*=\s*[\"']https?://", "외부 이미지"),
        (r"url\(\s*[\"']?https?://", "CSS 안 외부 자원"),
        (r"\bfetch\s*\(", "fetch 호출"),
        (r"@import\b", "CSS import"),
    ]:
        check(not re.search(pattern, html, flags=re.I), f"바깥 자원을 쓰고 있다: {label}")

    # 5. 눈에 보이는 글에 줄표와 가운뎃점이 없는지
    text = visible_text(html)
    check("\u2014" not in text, "눈에 보이는 글에 줄표(—)가 있다")
    check("\u00b7" not in text, "눈에 보이는 글에 가운뎃점(·)이 있다")

    # 6. 사이드바 구성
    # script 와 style 안쪽을 지우고 센다. 스크립트가 쓰는 선택자까지 세면 개수가 어긋난다.
    markup = strip_code_blocks(html)
    items = re.findall(r"data-nav\b", markup)
    wips = re.findall(r"data-wip\b", markup)
    check(
        len(items) == SIDEBAR_ITEM_COUNT,
        f"사이드바 항목이 {SIDEBAR_ITEM_COUNT}개여야 한다. 지금 {len(items)}개",
    )
    check(
        len(wips) == SIDEBAR_WIP_COUNT,
        f"준비 중 항목이 {SIDEBAR_WIP_COUNT}개여야 한다. 지금 {len(wips)}개",
    )
    check('href="papers.html"' in html, "사이드바에 papers.html 링크가 없다")

    # 7. 탐색기가 그대로인지
    if papers.exists():
        papers_html = papers.read_text(encoding="utf-8")
        check(
            'fetch("papers.json")' in papers_html,
            "papers.html 의 papers.json 읽는 부분이 사라졌다",
        )

    report()


def report():
    if fails:
        print(f"실패 {len(fails)}건")
        for f in fails:
            print(f"  - {f}")
        sys.exit(1)
    print("모든 검사를 통과했다")


if __name__ == "__main__":
    main()
