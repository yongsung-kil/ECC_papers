# -*- coding: utf-8 -*-
"""
IEEE Xplore 논문 PDF 자동 다운로드 — 브라우저 자동조종(크롤링) 버전

왜 이 버전?
----------
사내망은 SSL 검사(자체 루트 CA로 인증서를 중간에서 교체)와 프록시를 끼는데,
파이썬 requests/urllib 는 사내 CA·프록시를 몰라서 막힌다.
반면 "진짜 크롬"은 사내 CA·프록시·기관 IP 인증을 OS 차원에서 이미 신뢰/사용한다.
그래서 크롬을 자동조종해 stamp 링크를 열고, PDF 를 뷰어로 띄우지 말고
바로 다운로드하게 설정하면 브라우저로 손수 받는 것과 똑같이 동작한다.

준비물
------
- Google Chrome (설치돼 있으면 됨)
- pip install selenium   (Selenium 4 는 드라이버 자동관리 → 별도 설치 불필요)

사용법
------
1) 아래 PAPER_URL 에 IEEE Xplore 링크를 넣는다. 아래 형태 모두 OK:
     https://ieeexplore.ieee.org/document/9159114
     https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=9159114
2) python tools/ieee_download_browser.py  실행
   → 크롬 창이 떴다가 PDF 를 tools/downloads/ 에 저장하고 닫힌다.
"""

import os
import re
import sys
import time

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass

# ── 설정 ───────────────────────────────────────────────────────────────
PAPER_URL = "https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=9159114"

OUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "downloads")

HEADLESS = False   # True 면 크롬 창을 띄우지 않음. 처음엔 False 로 눈으로 확인 권장.
TIMEOUT = 90       # 다운로드 완료 대기 최대 초
# ───────────────────────────────────────────────────────────────────────


def arnumber_from_url(url: str) -> str:
    m = re.search(r"/document/(\d+)", url) or re.search(r"arnumber=(\d+)", url)
    if not m:
        raise ValueError(f"URL 에서 문서 번호를 찾지 못함: {url}")
    return m.group(1)


def build_driver(download_dir: str):
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options

    opts = Options()
    if HEADLESS:
        opts.add_argument("--headless=new")
    opts.add_argument("--start-maximized")
    # 사내망에서 자체서명 인증서 경고로 막히는 경우 대비
    opts.add_argument("--ignore-certificate-errors")
    opts.add_experimental_option("excludeSwitches", ["enable-logging"])

    prefs = {
        # PDF 를 내장 뷰어로 열지 말고 곧장 다운로드
        "plugins.always_open_pdf_externally": True,
        "download.default_directory": download_dir,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "profile.default_content_setting_values.automatic_downloads": 1,
    }
    opts.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome(options=opts)
    # headless 모드에서도 다운로드가 되도록 명시적으로 허용
    try:
        driver.execute_cdp_cmd("Page.setDownloadBehavior", {
            "behavior": "allow", "downloadPath": download_dir,
        })
    except Exception:
        pass
    return driver


def wait_for_download(download_dir: str, before: set, timeout: int):
    """새로 생긴 .pdf 파일이 완성(.crdownload 사라짐)될 때까지 대기."""
    deadline = time.time() + timeout
    while time.time() < deadline:
        now = set(os.listdir(download_dir))
        new = now - before
        # 다운로드 진행 중이면 .crdownload 가 있다
        crdownload = [f for f in now if f.endswith(".crdownload")]
        pdfs = [f for f in new if f.lower().endswith(".pdf")]
        if pdfs and not crdownload:
            return os.path.join(download_dir, pdfs[0])
        time.sleep(1)
    return None


def main():
    arnum = arnumber_from_url(PAPER_URL)
    stamp_url = f"https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber={arnum}"
    os.makedirs(OUT_DIR, exist_ok=True)

    print(f"[1/3] 문서 번호 : {arnum}")
    print(f"[2/3] 크롬 실행 후 접속: {stamp_url}")

    before = set(os.listdir(OUT_DIR))
    driver = build_driver(OUT_DIR)
    try:
        driver.get(stamp_url)
        # stamp 페이지 안 iframe 의 PDF 가 로드되며 다운로드가 트리거됨.
        # 혹시 트리거가 안 되면 iframe src(실제 PDF)로 직접 이동해 한 번 더 시도.
        time.sleep(3)
        saved = wait_for_download(OUT_DIR, before, timeout=10)
        if not saved:
            try:
                iframe = driver.find_element("css selector", "iframe")
                src = iframe.get_attribute("src")
                if src and ".pdf" in src:
                    print(f"      iframe PDF 로 직접 이동: {src}")
                    driver.get(src)
            except Exception:
                pass
            saved = wait_for_download(OUT_DIR, before, timeout=TIMEOUT)
    finally:
        driver.quit()

    if not saved:
        print("  ! 다운로드 실패 — 권한(기관 IP)·SSL·프록시 확인 필요.",
              file=sys.stderr)
        sys.exit(2)

    # arnumber 기준으로 파일명 정리
    target = os.path.join(OUT_DIR, f"ieee_{arnum}.pdf")
    if os.path.abspath(saved) != os.path.abspath(target):
        try:
            if os.path.exists(target):
                os.remove(target)
            os.rename(saved, target)
            saved = target
        except Exception:
            pass

    size = os.path.getsize(saved)
    print(f"\n✓ 저장 완료: {saved}  ({size:,} bytes)")


if __name__ == "__main__":
    main()
