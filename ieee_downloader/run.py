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


def wait_download(timeout):
    """staging 에 .pdf 가 완성될 때까지 대기. 완성 파일경로 반환 or None."""
    deadline = time.time() + timeout
    while time.time() < deadline:
        files = os.listdir(STAGING)
        crdownload = [f for f in files if f.endswith(".crdownload")]
        pdfs = [f for f in files if f.lower().endswith(".pdf")]
        if pdfs and not crdownload:
            return os.path.join(STAGING, pdfs[0])
        time.sleep(1)
    return None


def download_one(driver, arnumber):
    """stamp 페이지 → iframe PDF 다운로드. 완성 파일경로 반환 or None."""
    stamp = f"https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber={arnumber}"
    clear_staging()
    driver.get(stamp)
    time.sleep(2)
    saved = wait_download(8)          # stamp 가 바로 다운로드 트리거하는 경우
    if saved:
        return saved
    # iframe 의 실제 PDF 로 직접 이동
    try:
        iframe = driver.find_element("css selector", "iframe")
        src = iframe.get_attribute("src")
        if src and ".pdf" in src:
            driver.get(src)
    except Exception:
        pass
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
            else:
                conn.execute(
                    "UPDATE download_targets SET status='failed', "
                    "attempts=attempts+1, last_error=?, updated_at=? WHERE id=?",
                    (err or "다운로드 미완(권한/SSL/타임아웃)", now(), r["id"]))
                conn.commit()
                fail += 1
                print("실패")
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
