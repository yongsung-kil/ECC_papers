# IEEE 통과 논문 일괄 다운로더

1차 선별을 **통과한 IEEE 논문**의 PDF를 기관망(회사·학교) PC에서 한 번에 받아오는
자립형 패키지입니다. 진짜 Chrome을 자동 조종하므로 사내망 SSL 검사·프록시·기관 IP
인증이 그대로 적용됩니다.

> 본 저장소 기준 다운로드는 **이미 완료**되어 PDF는 `data/pdfs/ieee/<연>/<월>/`에 있습니다.
> 이 폴더는 **재다운로드가 필요할 때 쓰는 키트**로 남겨둡니다.

## 구성

| 파일 | 설명 |
|------|------|
| `download_papers.py` | 메인 실행 스크립트 — 크롬으로 PDF를 받아 `downloads/<연>/<월>/`에 저장. selenium이 없으면 자동 설치 |
| `build_targets_db.py` | `download.db`(대상 목록 + 상태)를 `data/papers.db`에서 새로 생성 (전체 DB가 있는 PC에서 1회) |

> `download.db`는 `papers.db`에서 언제든 재생성되므로 저장소에 두지 않습니다.
> 의존성은 selenium 하나뿐이고 `download_papers.py`가 자동 설치하므로 별도 설치 파일은 없습니다.

## 사용법 (기관망 PC)

1. **이 폴더 통째로** 기관망 PC에 복사합니다. 사전 조건: **Python 3**, **Google Chrome**.
2. 대상 목록 생성 — `papers.db`가 있는 PC에서:
   ```
   python build_targets_db.py
   ```
   → 같은 폴더에 `download.db` 생성.
3. 실행:
   ```
   python download_papers.py
   ```
   - selenium이 없으면 자동 설치 후 진행.
   - 크롬 창이 떴다 사라지며 `downloads/<연>/<월>/ieee_<문서번호>.pdf`로 저장.
   - 매 논문마다 성공/실패가 `download.db`에 기록됩니다.
4. 중간에 멈춰도 다시 실행하면 **완료분은 건너뛰고 이어받습니다.**

## 끝나면

`downloads/` 폴더를 원래 PC의 `data/pdfs/ieee/`로 **회수**하면 됩니다.

## 설정 (`download_papers.py` 상단)

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
