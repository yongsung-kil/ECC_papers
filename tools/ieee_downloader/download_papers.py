# -*- coding: utf-8 -*-
"""
IEEE 통과 논문 일괄 다운로드 (다른 PC / 기관망에서 실행)

준비
----
- Google Chrome 설치
- 같은 폴더에 download.db (build_targets_db.py 로 생성된 대상 목록) 가 있어야 함

실행
----
    python run.py

동작
----
1. selenium 이 없으면 자동으로 pip 설치한다.
2. download.db 의 status='pending'(또는 실패분) 논문을 하나씩 크롬으로 받는다.
   - 진짜 크롬을 쓰므로 사내망 SSL 검사·프록시·기관 IP 인증이 그대로 적용됨.
3. downloads/<연>/<월>/ieee_<번호>.pdf 로 저장한다.
4. 매 논문마다 결과(done/failed)를 download.db 에 기록한다.
   → 중간에 멈췄다 다시 실행해도 done 은 건너뛰고 이어받는다.

끝나면 download.db 와 downloads/ 폴더를 회수하면 된다.
"""

import os
import re
import shutil
import sqlite3
import subprocess
import sys
import time
from datetime import datetime, timezone
from urllib.parse import quote, urljoin, urlparse

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass

HERE = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(HERE, "download.db")
DOWNLOADS_ROOT = os.path.join(HERE, "downloads")
STAGING = os.path.join(DOWNLOADS_ROOT, "_staging")

# ── 설정 ───────────────────────────────────────────────────────────────
HEADLESS = False        # True 면 크롬 창 숨김. 처음엔 False 로 확인 권장.
LIMIT = None            # 테스트용: 정수 넣으면 그만큼만 받음. None=전부.
RETRY_FAILED = True     # 이전에 실패한 것도 다시 시도할지
MAX_ATTEMPTS = 3        # 같은 논문 최대 시도 횟수
DL_TIMEOUT = 90         # 논문 1편 다운로드 대기 최대 초
PAGE_TIMEOUT = 15       # stamp 페이지에서 iframe(실제 PDF)이 뜰 때까지 최대 초
POLITE_DELAY = 1.5      # 논문 사이 간격(초) — 너무 빠르면 IEEE 가 막을 수 있어 둠
FAIL_DELAY = 5          # 실패 시 추가 휴식(초)
USE_YONSEI_PROXY = True
YONSEI_PROXY_PREFIX = "https://access.yonsei.ac.kr/link.n2s?url="
ID = "2022313262"
PW = "Password1!"
# ───────────────────────────────────────────────────────────────────────


def ensure_selenium():
    try:
        import selenium  # noqa
        return
    except ImportError:
        print("selenium 미설치 → pip 설치 시도...")
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", "selenium"])
        print("selenium 설치 완료.")


def now():
    return datetime.now(timezone.utc).isoformat()


def build_driver():
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options

    os.makedirs(STAGING, exist_ok=True)
    opts = Options()
    if HEADLESS:
        opts.add_argument("--headless=new")
    opts.add_argument("--start-maximized")
    opts.add_argument("--ignore-certificate-errors")
    opts.add_experimental_option("excludeSwitches", ["enable-logging"])
    prefs = {
        "plugins.always_open_pdf_externally": True,
        "download.default_directory": STAGING,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "profile.default_content_setting_values.automatic_downloads": 1,
    }
    opts.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(options=opts)
    try:
        driver.execute_cdp_cmd("Page.setDownloadBehavior",
                               {"behavior": "allow", "downloadPath": STAGING})
    except Exception:
        pass
    return driver


def clear_staging():
    if os.path.isdir(STAGING):
        for f in os.listdir(STAGING):
            try:
                os.remove(os.path.join(STAGING, f))
            except OSError:
                pass


def staging_pdf():
    """
    STAGING 폴더에 다운로드가 완료된 PDF가 있으면 파일 경로 반환.
    연세 proxy를 거치면 파일명이 getPDF.jsp로 저장될 수 있으므로,
    확장자가 .pdf가 아니어도 실제 파일 내용이 PDF이면 인정한다.
    """
    if not os.path.isdir(STAGING):
        return None

    files = os.listdir(STAGING)

    # 아직 다운로드 중이면 기다림
    if any(
        f.lower().endswith((".crdownload", ".tmp"))
        for f in files
    ):
        return None

    for f in files:
        path = os.path.join(STAGING, f)

        if not os.path.isfile(path):
            continue

        # 너무 작은 파일은 오류 페이지일 가능성이 높으니 제외
        try:
            if os.path.getsize(path) < 1000:
                continue
        except OSError:
            continue

        # 1) 일반적인 PDF 파일명
        if f.lower().endswith(".pdf"):
            return path

        # 2) getPDF.jsp 같은 이름이어도 실제 내용이 PDF이면 인정
        try:
            with open(path, "rb") as fp:
                header = fp.read(5)

            if header == b"%PDF-":
                return path

        except Exception:
            pass

    return None


def wait_download(timeout):
    """staging 에 .pdf 가 완성될 때까지 대기. 완성 파일경로 반환 or None."""
    deadline = time.time() + timeout
    while time.time() < deadline:
        got = staging_pdf()
        if got:
            return got
        time.sleep(1)
    return None


def proxify(url):
    if not USE_YONSEI_PROXY:
        return url

    if url.startswith(YONSEI_PROXY_PREFIX):
        return url

    if url.startswith("//"):
        url = "https:" + url

    return YONSEI_PROXY_PREFIX + quote(url, safe="")


def find_first_visible(driver, selectors, timeout=3):
    from selenium.webdriver.common.by import By

    deadline = time.time() + timeout

    while time.time() < deadline:
        for sel in selectors:
            try:
                elements = driver.find_elements(By.CSS_SELECTOR, sel)
                for e in elements:
                    if e.is_displayed() and e.is_enabled():
                        return e
            except Exception:
                pass

        time.sleep(0.2)

    return None


def login_yonsei_if_needed(driver, timeout=5):
    """
    현재 페이지가 연세 로그인 페이지이면 ID/PW 입력 후 로그인.
    로그인 페이지가 아니면 False 반환.
    """

    # 아무 사이트에나 비밀번호를 넣지 않도록 yonsei 도메인에서만 작동
    host = urlparse(driver.current_url).netloc.lower()
    if "yonsei.ac.kr" not in host:
        return False

    user_selectors = [
        "input[name='id']",
        "input[name='userId']",
        "input[name='userid']",
        "input[name='username']",
        "input[name='loginId']",
        "input#id",
        "input#userId",
        "input#userid",
        "input[type='text']",
        "input[type='email']",
    ]

    pw_selectors = [
        "input[name='pw']",
        "input[name='password']",
        "input[name='passwd']",
        "input#pw",
        "input#password",
        "input[type='password']",
    ]

    button_selectors = [
        "button[type='submit']",
        "input[type='submit']",
        "button#loginBtn",
        "button#btnLogin",
        "input#loginBtn",
        ".login_btn",
        ".btn_login",
    ]

    pw_box = find_first_visible(driver, pw_selectors, timeout=timeout)

    # password input이 없으면 로그인 페이지가 아니라고 판단
    if pw_box is None:
        return False

    user_box = find_first_visible(driver, user_selectors, timeout=timeout)

    if user_box is None:
        print("! 로그인 페이지로 보이지만 ID 입력칸을 찾지 못함")
        return False

    try:
        user_box.clear()
    except Exception:
        pass

    user_box.send_keys(ID)

    try:
        pw_box.clear()
    except Exception:
        pass

    pw_box.send_keys(PW)

    btn = find_first_visible(driver, button_selectors, timeout=1)

    if btn is not None:
        driver.execute_script("arguments[0].click();", btn)
    else:
        from selenium.webdriver.common.keys import Keys
        pw_box.send_keys(Keys.ENTER)

    time.sleep(3)
    return True


def click_open_button_if_exists(driver, timeout=2):
    """
    연세 proxy 중간 페이지에서 '열기' 버튼이 뜨면 자동 클릭.
    없으면 False.

    이전 구현은 5개 xpath를 각각 WebDriverWait(timeout)로 '순차' 대기해
    버튼이 없는 정상 케이스에서 timeout×5 만큼 낭비했다.
    여기서는 전체 timeout 안에서 5개 xpath를 함께 폴링해
    버튼이 없으면 timeout 한 번만 소진하고 즉시 빠져나온다.
    """
    from selenium.webdriver.common.by import By

    xpaths = [
        "//button[normalize-space()='열기']",
        "//a[normalize-space()='열기']",
        "//input[@value='열기']",
        "//*[self::button or self::a][contains(normalize-space(), '열기')]",
        "//*[self::button or self::a][contains(normalize-space(), 'Open')]",
    ]

    deadline = time.time() + timeout
    while time.time() < deadline:
        for xp in xpaths:
            try:
                for btn in driver.find_elements(By.XPATH, xp):
                    if btn.is_displayed() and btn.is_enabled():
                        driver.execute_script("arguments[0].click();", btn)
                        time.sleep(0.5)
                        return True
            except Exception:
                pass
        time.sleep(0.2)

    return False


def open_url_with_yonsei_handling(driver, url, max_rounds=3):
    """
    URL 접근 시:
    1. 로그아웃 상태면 자동 로그인
    2. proxy '열기' 버튼이 있으면 자동 클릭
    3. 로그인 후 원래 URL 재접근
    """

    for _ in range(max_rounds):
        driver.get(url)
        time.sleep(0.5)

        did_login = login_yonsei_if_needed(driver, timeout=2)

        if did_login:
            # 로그인 후 원래 PDF/IEEE URL로 다시 접근
            time.sleep(2)
            continue

        clicked = click_open_button_if_exists(driver, timeout=2)

        if clicked:
            time.sleep(1)

            # 열기 클릭 후 로그인 페이지로 넘어가는 경우까지 처리
            did_login_after_click = login_yonsei_if_needed(driver, timeout=2)

            if did_login_after_click:
                time.sleep(2)
                continue

        return
    

def download_one(driver, arnumber):
    """
    연세 proxy 경유:
    stamp 페이지 접근 → proxy '열기' 자동 클릭 → iframe PDF src 추출
    → PDF src 접근 → proxy '열기' 자동 클릭 → 다운로드 대기
    """

    raw_stamp = f"https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber={arnumber}"
    stamp = proxify(raw_stamp)

    clear_staging()
    open_url_with_yonsei_handling(driver, stamp)

    # 연세 proxy에서 '열기' 버튼 뜨면 자동 클릭
    click_open_button_if_exists(driver, timeout=2)

    src = None
    deadline = time.time() + PAGE_TIMEOUT

    while time.time() < deadline:
        got = staging_pdf()
        if got:
            return got

        try:
            iframe = driver.find_element("css selector", "iframe")
            s = iframe.get_attribute("src")

            if s and ("pdf" in s.lower() or "getpdf" in s.lower()):
                s = urljoin(driver.current_url, s)
                src = proxify(s)
                break

        except Exception:
            pass

        time.sleep(0.5)

    if src:
        src = proxify(src)
        open_url_with_yonsei_handling(driver, src)

        # PDF src로 들어간 뒤에도 proxy '열기'가 다시 뜨면 자동 클릭
        click_open_button_if_exists(driver, timeout=2)

    return wait_download(DL_TIMEOUT)


def target_path(year_month, arnumber):
    if year_month and re.match(r"\d{4}-\d{2}", year_month):
        year, month = year_month.split("-")
    else:
        year, month = "unknown", "01"
    d = os.path.join(DOWNLOADS_ROOT, year, month)
    os.makedirs(d, exist_ok=True)
    return os.path.join(d, f"ieee_{arnumber}.pdf")


def main():
    if not os.path.exists(DB_PATH):
        print(f"! download.db 가 없음: {DB_PATH}\n"
              f"  먼저 (대상 목록이 있는 PC에서) build_targets_db.py 로 생성하세요.",
              file=sys.stderr)
        sys.exit(1)

    ensure_selenium()
    os.makedirs(DOWNLOADS_ROOT, exist_ok=True)

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    statuses = "('pending','failed')" if RETRY_FAILED else "('pending')"
    rows = conn.execute(
        f"SELECT * FROM download_targets "
        f"WHERE status IN {statuses} AND attempts < ? "
        f"ORDER BY year_month",
        (MAX_ATTEMPTS,),
    ).fetchall()
    if LIMIT:
        rows = rows[:LIMIT]

    total_all = conn.execute(
        "SELECT count(*) FROM download_targets").fetchone()[0]
    done_already = conn.execute(
        "SELECT count(*) FROM download_targets WHERE status='done'").fetchone()[0]
    print(f"전체 {total_all}편 | 이미 완료 {done_already}편 | 이번 대상 {len(rows)}편\n")
    if not rows:
        print("받을 대상이 없습니다.")
        return

    driver = build_driver()
    ok = fail = 0
    try:
        for i, r in enumerate(rows, 1):
            arnum = r["arnumber"]
            tgt = target_path(r["year_month"], arnum)
            # 이미 파일이 있으면 done 처리하고 건너뜀
            if os.path.exists(tgt) and os.path.getsize(tgt) > 1000:
                conn.execute(
                    "UPDATE download_targets SET status='done', pdf_path=?, "
                    "updated_at=? WHERE id=?",
                    (os.path.relpath(tgt, HERE), now(), r["id"]))
                conn.commit()
                ok += 1
                print(f"[{i}/{len(rows)}] {arnum} 이미 존재 → skip")
                continue

            print(f"[{i}/{len(rows)}] {arnum} ({r['year_month']}) 받는 중...",
                  end=" ", flush=True)
            err = None
            try:
                saved = download_one(driver, arnum)
            except Exception as e:
                saved, err = None, str(e)[:300]

            if saved and os.path.exists(saved):
                shutil.move(saved, tgt)
                conn.execute(
                    "UPDATE download_targets SET status='done', pdf_path=?, "
                    "attempts=attempts+1, last_error=NULL, updated_at=? WHERE id=?",
                    (os.path.relpath(tgt, HERE), now(), r["id"]))
                conn.commit()
                ok += 1
                print(f"OK ({os.path.getsize(tgt):,} B)")
                time.sleep(POLITE_DELAY)            # 편당 간격(과속 방지)
            else:
                conn.execute(
                    "UPDATE download_targets SET status='failed', "
                    "attempts=attempts+1, last_error=?, updated_at=? WHERE id=?",
                    (err or "다운로드 미완(권한/SSL/타임아웃)", now(), r["id"]))
                conn.commit()
                fail += 1
                print("실패")
                time.sleep(FAIL_DELAY)              # 실패 시 추가 휴식
    finally:
        driver.quit()
        clear_staging()
        try:
            os.rmdir(STAGING)
        except OSError:
            pass

    remain = conn.execute(
        "SELECT count(*) FROM download_targets WHERE status!='done'").fetchone()[0]
    conn.close()
    print(f"\n완료: 성공 {ok} / 실패 {fail} | 남은(미완) {remain}편")
    if remain:
        print("→ 다시 run.py 실행하면 남은 것부터 이어받습니다.")


if __name__ == "__main__":
    main()
