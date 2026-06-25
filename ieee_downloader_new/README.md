# IEEE 통과 논문 일괄 다운로더

1차 선별을 **통과한 IEEE 논문(5,873편)**의 PDF를 기관망(회사·학교) PC에서
한 번에 받아오는 자립형 패키지입니다. 진짜 Chrome을 자동 조종하므로
사내망 SSL 검사·프록시·기관 IP 인증이 그대로 적용됩니다.

## 구성

| 파일 | 설명 |
|------|------|
| `download.db` | 받을 대상 목록 + 다운로드 상태 DB (이미 5,873편 등록됨) |
| `run.py` | 메인 실행 스크립트 — 크롬으로 PDF를 받아 `downloads/<연>/<월>/`에 저장 |
| `build_targets_db.py` | `download.db`를 새로 만드는 스크립트 (전체 DB가 있는 PC에서만 사용) |
| `requirements.txt` / `install.bat` | 의존성(selenium) 설치 |

## 사용법 (기관망 PC)

1. **이 폴더 통째로** 기관망 PC에 복사합니다.
2. 사전 조건: **Python 3**, **Google Chrome** 설치.
3. 의존성 설치 — `install.bat` 더블클릭 (또는 `python -m pip install -r requirements.txt`).
   - `run.py`도 selenium이 없으면 자동 설치를 시도합니다.
4. 실행:
   ```
   python run.py
   ```
   - 크롬 창이 떴다 사라지며 PDF를 받습니다.
   - `downloads/<연>/<월>/ieee_<문서번호>.pdf` 로 저장됩니다.
   - **매 논문마다 성공/실패가 `download.db`에 기록**됩니다.
5. 중간에 멈춰도 다시 `python run.py` 하면 **완료분은 건너뛰고 이어받습니다.**

## 끝나면

`download.db`와 `downloads/` 폴더를 원래 PC로 **회수**하면 됩니다.
`download.db`의 `status`(done/failed)와 `pdf_path`로 결과를 확인할 수 있습니다.

## 설정 (`run.py` 상단)

| 변수 | 기본 | 설명 |
|------|------|------|
| `HEADLESS` | `False` | `True`면 크롬 창을 숨김. 동작 확인 후 바꾸세요. |
| `LIMIT` | `None` | 정수를 넣으면 그 개수만 받음(테스트용). |
| `RETRY_FAILED` | `True` | 실패분도 재시도. |
| `MAX_ATTEMPTS` | `3` | 같은 논문 최대 시도 횟수. |
| `DL_TIMEOUT` | `90` | 1편 다운로드 대기 최대 초. |

## 상태 확인 (쿼리 예시)

```bash
python -c "import sqlite3;c=sqlite3.connect('download.db');print(c.execute(\"select status,count(*) from download_targets group by status\").fetchall())"
```
