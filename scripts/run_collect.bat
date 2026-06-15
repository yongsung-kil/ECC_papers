@echo off
REM LDPC 논문 자동 수집 — Windows 작업 스케줄러가 호출하는 진입점.
REM 프로젝트 루트로 이동 후 수집 1회 실행(쿼리당 100건씩 이어받기).

cd /d "%~dp0.."

REM 가상환경을 쓰는 경우 아래 줄의 주석을 풀고 경로를 맞추세요.
REM call ".venv\Scripts\activate.bat"

python -m src.runner -n 100
