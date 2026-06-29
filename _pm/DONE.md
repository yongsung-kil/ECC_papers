# DONE

> 일자별 작업 이력 (최신이 위). 새 항목은 이 줄 아래에 append.

### 2026-06-29 — 저장소 구조 차수화(stageN) + 데이터/PDF 통합
판정 단계를 stageN으로 통일하고, 논문 PDF·카탈로그를 `data/` 아래로 모음
- **배경**: criteria(`1차`)·src(`stage1`)·papers(`1차선별`) 세 곳이 같은 "단계"를 다른 이름으로 불러 혼란. PDF도 `data/`와 `papers/`로 갈려 있고 `papers/`엔 정작 PDF가 없는 이름 불일치.
- **변경**:
  - 단계 라벨 **stageN 전면 통일**: `criteria/1차`→`criteria/stage1` (src는 이미 stage1/stage2/report). 파이썬 패키지 제약상 영문 stageN으로 통일.
  - **PDF 통합**: IEEE 5,871 + arXiv 349 → `data/pdfs/{ieee,arxiv}/<연>/<월>/`
  - **카탈로그 이전**: `papers/{원본,1차선별}` → `data/catalogs/{원본,stage1}` (papers/ 비움)
  - **다운로더 정리**: `ieee_downloader_new`→`tools/ieee_downloader/`; 구 단일URL 예시(`tools/ieee_download*.py`)·`download.db`·`install.bat`·`requirements.txt` 삭제(다운로더가 selenium 자동설치)
  - **경로 참조 갱신**: `src/report/catalog.py`, `tools/arxiv_download.py`, `src/stage1/select_workflow.js`, `README/REVIEW/CLASSIFICATION`, `.gitignore`(`data/pdfs/`, `tools/ieee_downloader/downloads/`)
- **파일**: `data/catalogs/`, `data/pdfs/`, `criteria/stage1/`, `src/report/catalog.py`, `tools/*`, 루트 문서, `.gitignore`
- **커밋**: `ed6219c` — papers.db·PDF는 **미포함**(바이너리 git 비대화 회피)

### 2026-06-29 — Phase 3(2차) 심층분석 설계 프로토타입
통과 논문 PDF를 정독해 **이식성·카테고리를 enum으로 판정**하는 2차 분석 설계
- **배경**: 1차(초록 선별) 통과 중 algo_mod=1 **5,307편**을 본문까지 읽어 "실제 이식 가능 수준인지 + 어떤 카테고리인지" 판정 필요.
- **변경**:
  - `_test/20260625_phase3_example/`에 프롬프트·enum 카테고리·예시 1편(`ieee:7828079`)·PDF 경로 리졸버(`resolve_pdf.py`) 작성·검증.
  - 카테고리 enum화(필터 가능): 이식성/NAND관련성/대상(decoder·encoder)/부호/연판정/HW·gatecount·병렬화·throughput/정정능력·avg iteration/error floor·waterfall + 추천도·한계.
  - **저장 방식 확정**: md/json이 소스 → `data/papers.db`에 enum+`round` 컬럼 테이블로 적재, **차수 마일스톤에만 커밋**(`.git` 732MB 비대화 회피).
- **파일**: `_test/20260625_phase3_example/*`(gitignore), `src/stage2/README.md`
- **상태**: 프로토타입 검증 단계 — 카테고리 확정 후 전체 5,307편 배치 예정.

### 2026-06-29 — IEEE 통과분 PDF 다운로드 완료 · ieee-collector 태스크 종료
1차 통과 논문 PDF 일괄 확보, 구 크롤러 태스크 폐기
- **배경**: 2차 본문 분석용 PDF 확보. 구 `src/ieee_collector.py` 크롤러는 수집 종료로 코드 제거됨.
- **변경**: 브라우저 자동조종 다운로더(`tools/ieee_downloader`)로 통과분 다운로드 — **IEEE 5,871/5,873**(2편 IEEE Xplore 미제공), **arXiv 349/349**(통과 6,222편 중 6,220편 = 99.97%). `_pm/tasks/ieee-collector` → `done/`로 폐기 이동(수집기 태스크 무효화·다운로더로 대체).
- **파일**: `data/pdfs/`, `tools/ieee_downloader/`

### 2026-06-15 — Phase 2: 1차 선별 (LLM=Claude 세션 직접 판단)
NAND 관련성 선별을 API 없이 세션의 Claude가 직접 판단하는 체계 + 기준서 구축
- **배경**: API 토큰 비용 없이 선별하려 LLM을 "이 세션의 Claude"로 구동. 핵심은 **판단 기준의 문서화**(세션 간 일관성·확장)
- **변경**:
  - `criteria/selection_criteria.md` — 살아있는 선별 기준서. 대전제: NAND 직접 여부가 아니라 **디코더/HW/알고리즘 이식 가능 여부**로 판단. INCLUDE(A~E)/EXCLUDE 카테고리, 점수 루브릭(임계 0.40), 변경 이력
  - `src/review.py` — `pending`(기준서 헤더 + 미선별 초록 덤프) / `apply`(판단 JSON → `filter_results` + status) / `stats`. Windows UTF-8 출력
  - `src/runner.py` — `drain` 모드 추가(끝까지 1회성 백필, `--drain`)
  - `.gitignore` — 선별 임시파일 제외
- **파일**: `criteria/selection_criteria.md`, `src/review.py`, `src/runner.py`, `.gitignore`
- **검증**: 수집된 36건 전수 선별 → 통과 18/제외 18. 기준 명시 후 경계 4건(이식 가능 HW/알고리즘) 재정정 반영. arXiv 최신분 다수가 양자 LDPC라 제외됨

### 2026-06-15 — Phase 1-4: 수집 스케줄러 구현
arXiv·IEEE 주기적 자동 수집 + 커서 기반 이어받기 + GitHub 자동 업로드
- **배경**: 1회성 수집을 넘어 주기적으로 신규 논문을 채집하고, 웹의 대량 결과(예: 1000건)를 N건씩 나눠 누락 없이 백필 필요
- **변경**:
  - `src/db.py` — `collect_state`(쿼리별 offset 커서), `run_log`(실행 로그) 테이블 + `insert_paper`(INSERT OR IGNORE 중복 제외)/`get_cursor`/`set_cursor`/`start_run`/`finish_run`/`checkpoint` 헬퍼
  - `src/arxiv_collector.py` — `collect_batch()`: 제출일 **오름차순**(순서 안 꼬임) + offset 커서로 이어받기. `max_results=offset+batch_size` 보정
  - `src/ieee_collector.py` — `collect_batch()`: `startRecord`/`totalRecords` 기반 커서 이어받기
  - `src/runner.py` — `run_once()` 오케스트레이터: 수집→교차중복제거→카탈로그→로그→신규 있을 때만 git commit/push
  - `scripts/run_collect.bat`, `scripts/register_task.ps1`, `scripts/README.md` — Windows 작업 스케줄러 등록(기본 6시간 간격)
  - `.gitignore` — `papers.db`는 GitHub에 올리고(`!data/papers.db`) WAL 보조파일·`logs/` 제외
- **파일**: `src/db.py`, `src/arxiv_collector.py`, `src/ieee_collector.py`, `src/runner.py`, `scripts/*`, `.gitignore`
- **검증**: arXiv 배치 2회 연속 실행 — offset 0→3→6 전진, 같은 논문 재수집 없음, 중복 제외 정상

### 2026-06-10 — Phase 1-1: arXiv API 수집기 구현
arXiv API로 LDPC 논문 메타데이터를 자동 수집하는 시스템 구축
- **배경**: LDPC 논문 자동 수집 → 선별 → 분석 파이프라인의 첫 단계
- **변경**:
  - `src/arxiv_collector.py` — arXiv API 수집기 (검색, 메타데이터 저장, PDF 다운로드, 중복 체크)
  - `src/db.py` — SQLite DB 스키마 (papers/filter_results/analyses 3테이블)
- **파일**: `src/arxiv_collector.py`, `src/db.py`, `requirements.txt`, `.gitignore`
- **검증**: arXiv에서 20건 시범 수집 성공, 중복 체크 정상 동작 확인

### 2026-06-10 — Phase 1-2: IEEE Xplore 수집기 구현
IEEE Xplore 크롤링 방식 수집기 구현 및 테스트 완료
- **배경**: IEEE 논문도 수집 필요, API 키 없이 크롤링으로 접근
- **변경**:
  - `src/ieee_collector.py` — REST endpoint + BeautifulSoup 크롤링
- **파일**: `src/ieee_collector.py`, `requirements.txt`
- **검증**: 10건 수집 성공, abstract 추출 정상 동작

### 2026-06-10 — Phase 1-3: 수집 DB + 카탈로그
DB 구축 및 카탈로그 자동 생성 체계 완성
- **배경**: 수집된 논문 관리 및 열람 편의
- **변경**:
  - SQLite DB (`data/papers.db`) — 단일 DB, source 컬럼으로 arXiv/IEEE 구분
  - 카탈로그 소스별/월별 분리: `papers/{source}/{year}/{month}/catalog.md|csv`
  - arXiv/IEEE 교차 중복 제거 (`dedup_cross_source()`)
  - CSV 내보내기 (엑셀 호환, utf-8-sig)
- **파일**: `src/arxiv_collector.py`, `src/db.py`
