@echo off
chcp 65001 >nul
cd /d "%~dp0"
echo Prime ECC 발표용 서버를 띄웁니다.
echo 끝나면 이 창을 닫으세요.
start "" /b python -m http.server 8000
timeout /t 2 >nul
start "" http://localhost:8000/
pause >nul
