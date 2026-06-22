# -*- coding: utf-8 -*-
"""
IEEE Xplore 논문 PDF 자동 다운로드 (예시 / 단일 링크 하드코딩 버전)

전제: 회사·학교 등 기관 네트워크(IP 자동인증) 환경에서 실행한다.
      IEEE Xplore 는 기관 IP 면 로그인/쿠키 없이 PDF 접근 권한이 생긴다.

사용법
------
1) 아래 PAPER_URL 에 IEEE Xplore 링크를 넣는다. 아래 두 형태 모두 OK:
     https://ieeexplore.ieee.org/document/7117421
     https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=7117421
2) python tools/ieee_download.py  실행 → tools/downloads/ 에 PDF 저장.

동작 원리
--------
stamp.jsp?arnumber=<번호> 뷰어 페이지 안의 iframe 에 실제 PDF 주소가 들어 있다.
그 주소를 다시 요청하면 PDF 바이트가 내려온다. (기관 IP 면 권한 OK)
"""

import os
import re
import sys

# Windows 콘솔(cp949)에서 한글·기호 출력이 깨지지 않도록 UTF-8 강제
try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass

# ── 설정 ───────────────────────────────────────────────────────────────
PAPER_URL = "https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=7117421"

OUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "downloads")
# ───────────────────────────────────────────────────────────────────────

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/124.0 Safari/537.36")
HEADERS = {"User-Agent": UA, "Referer": "https://ieeexplore.ieee.org/"}


def arnumber_from_url(url: str) -> str:
    """문서/뷰어 URL 에서 arnumber(문서 번호) 추출."""
    m = re.search(r"/document/(\d+)", url) or re.search(r"arnumber=(\d+)", url)
    if not m:
        raise ValueError(f"URL 에서 문서 번호를 찾지 못함: {url}")
    return m.group(1)


def _build_fetcher():
    """(get_text, get_bytes) 함수 쌍 반환. requests 있으면 사용, 없으면 urllib."""
    try:
        import requests  # noqa
        sess = requests.Session()
        sess.headers.update(HEADERS)

        def get_text(url):
            r = sess.get(url, timeout=30)
            r.raise_for_status()
            return r.text

        def get_bytes(url):
            r = sess.get(url, timeout=60)
            r.raise_for_status()
            return r.content, r.headers.get("Content-Type", "")

        return get_text, get_bytes

    except ImportError:
        import urllib.request
        opener = urllib.request.build_opener()
        opener.addheaders = list(HEADERS.items())

        def get_text(url):
            with opener.open(url, timeout=30) as resp:
                return resp.read().decode("utf-8", "replace")

        def get_bytes(url):
            with opener.open(url, timeout=60) as resp:
                return resp.read(), resp.headers.get("Content-Type", "")

        return get_text, get_bytes


def find_pdf_url(html: str, arnumber: str) -> str:
    """stamp.jsp 페이지 HTML 에서 실제 PDF 주소를 추출."""
    for pat in (
        r'<iframe[^>]+src="([^"]+\.pdf[^"]*)"',
        r'<iframe[^>]+src="([^"]*getPDF\.jsp[^"]*)"',
        r'"(https?://ieeexplore\.ieee\.org/(?:ielx?\d+|iel\d+)/[^"]+\.pdf[^"]*)"',
        r'"(/(?:ielx?\d+|iel\d+)/[^"]+\.pdf[^"]*)"',
    ):
        m = re.search(pat, html)
        if m:
            url = m.group(1).replace("&amp;", "&")
            if url.startswith("/"):
                url = "https://ieeexplore.ieee.org" + url
            return url
    # 못 찾으면 표준 getPDF 주소로 추측
    return (f"https://ieeexplore.ieee.org/stampPDF/getPDF.jsp"
            f"?tp=&arnumber={arnumber}&ref=")


def main():
    arnum = arnumber_from_url(PAPER_URL)
    stamp_url = f"https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber={arnum}"
    os.makedirs(OUT_DIR, exist_ok=True)
    out_path = os.path.join(OUT_DIR, f"ieee_{arnum}.pdf")

    get_text, get_bytes = _build_fetcher()

    print(f"[1/3] 문서 번호 : {arnum}")
    print(f"[2/3] 뷰어 페이지: {stamp_url}")
    try:
        html = get_text(stamp_url)
    except Exception as e:
        print(f"  ! 뷰어 페이지 요청 실패: {e}", file=sys.stderr)
        sys.exit(1)

    pdf_url = find_pdf_url(html, arnum)
    print(f"[3/3] PDF 주소   : {pdf_url}")

    try:
        data, ctype = get_bytes(pdf_url)
    except Exception as e:
        print(f"  ! PDF 요청 실패: {e}", file=sys.stderr)
        sys.exit(1)

    # PDF 검증: 매직넘버 %PDF 확인 (권한 없으면 HTML 페이지가 옴)
    if data[:4] != b"%PDF":
        print("  ! 받은 데이터가 PDF 가 아님 (기관 IP 권한 확인 필요).")
        print(f"    Content-Type={ctype}, 앞부분={data[:120]!r}")
        debug = out_path + ".debug.html"
        with open(debug, "wb") as f:
            f.write(data)
        print(f"    응답 내용을 {debug} 에 저장했으니 확인하세요.")
        sys.exit(2)

    with open(out_path, "wb") as f:
        f.write(data)
    print(f"\n✓ 저장 완료: {out_path}  ({len(data):,} bytes)")


if __name__ == "__main__":
    main()
