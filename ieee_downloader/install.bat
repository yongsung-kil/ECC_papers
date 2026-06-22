@echo off
REM IEEE 다운로더 의존성 설치 (다른 PC에서 1회 실행)
REM Python 3 와 Google Chrome 이 미리 설치돼 있어야 합니다.

echo [1/2] Python 확인...
python --version
if errorlevel 1 (
    echo Python 이 없습니다. https://www.python.org 에서 설치 후 다시 실행하세요.
    pause
    exit /b 1
)

echo [2/2] selenium 설치...
python -m pip install -r "%~dp0requirements.txt"

echo.
echo 설치 완료. 이제  python run.py  를 실행하세요.
pause
