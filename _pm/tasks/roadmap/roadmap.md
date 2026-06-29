# Auto Paper Analysis — Roadmap

LDPC 논문 자동 수집 → 선별 → 분석 → 아이디어 정리 시스템

## Phase 1: 논문 수집 (Crawling & API)

- [x] **1-1. arXiv API 수집기** ✅
  - `arxiv` Python 패키지로 메타데이터 + PDF 수집
  - 검색 쿼리: LDPC 관련 10개 키워드 × 4개 카테고리(cs.IT, eess.SP, cs.AR, cs.ET)
  - 중복 체크: `paper_id` 기반
  - 파일: `src/arxiv_collector.py`
- [x] **1-2. IEEE Xplore 수집기 (뼈대)** ✅
  - REST endpoint 크롤링 방식 (API 키 불필요)
  - abstract: 개별 페이지에서 meta/JSON-LD/JS 변수 순서로 추출
  - **라이센스 네트워크에서 테스트/완성 필요**
  - 파일: `src/ieee_collector.py`
- [x] **1-3. 수집 DB** ✅
  - SQLite (`data/papers.db`), 단일 `papers` 테이블에 `source` 컬럼으로 arXiv/IEEE 구분
  - 3개 테이블: `papers`, `filter_results`, `analyses`
  - 파일: `src/db.py`
- [x] **1-3a. 카탈로그 출력** ✅
  - `papers/catalog.md` — 소스별 구분, PDF 링크 클릭 가능 (Ctrl+Shift+V)
  - `papers/catalog.csv` — 엑셀용 내보내기 (utf-8-sig)
  - 수집 시 자동 갱신
- [x] **1-4. 수집 러너** ✅ — 주기 스케줄 대신 **전량 drain**(`src/runner.py --drain`)
  - arXiv: 단일 광범위 쿼리(LDPC, 양자/카테고리 제한 없음), 커서 이어받기
  - IEEE: REST 검색(pageNumber 페이지네이션 + 검색 응답 초록), (term,year) 연도 버킷
  - DB·카탈로그 GitHub 자동 push, 로그(`logs/`+`run_log`)
  - 폐기: Windows 스케줄러/CSV import (불필요)

## Phase 2: 1차 선별 (Filtering)

- [ ] **2-1. 키워드 기반 필터** — NAND/Flash/Storage 관련 키워드 매칭
- [ ] **2-2. LLM 기반 관련성 판단** — Abstract 기반으로 NAND 활용 가능성 점수화
- [ ] **2-3. 선별 결과 저장** — 관련성 점수, 판단 근거 DB 기록

## Phase 3: Deep Dive 분석

- [ ] **3-1. PDF 파싱** — 논문 전문 텍스트 추출 (수식, 표, 그림 포함)
- [ ] **3-2. LLM 기반 논문 분석** — 핵심 기여, 방법론, 실험 결과 요약
- [ ] **3-3. NAND 적용 가능성 분석** — 구체적 활용 시나리오, 필요 수정사항 정리

## Phase 4: 아이디어 정리 & 평가

- [ ] **4-1. 아이디어 카드 생성** — 논문별 실용적 아이디어 구조화
- [ ] **4-2. 실현 가능성 평가** — 구현 난이도, 성능 개선 예상치, HW 제약 등
- [ ] **4-3. 알고리즘/방법 정리** — 실제 구현 가능한 수준의 pseudo-code 또는 설계 문서

## Phase 5: 관리 & 운영

- [ ] **5-1. 검토 이력 관리** — 이미 분석한 논문 추적, 재검토 방지
- [ ] **5-2. 저장소 용량 관리** — 불필요 PDF 삭제 정책, Git LFS 또는 외부 저장
- [ ] **5-3. 리포트 생성** — 주간/월간 신규 논문 요약 리포트

---

## 현재 진행 상태

| Phase | 상태 | 비고 |
|-------|------|------|
| Phase 1 | **진행 중** | 1-1~1-3 완료, 1-2 IEEE 테스트 필요, 1-4 스케줄러 대기 |
| Phase 2 | 대기 | Phase 1 완료 후 진행 |
| Phase 3 | 대기 | |
| Phase 4 | 대기 | |
| Phase 5 | 대기 | |

---

## 기술 스택

- **언어**: Python 3.11+
- **논문 수집**: `arxiv` (Python 패키지), `requests` + `BeautifulSoup` (IEEE 크롤링)
- **DB**: SQLite (`data/papers.db`)
- **카탈로그**: Markdown + CSV 자동 생성
- **PDF 파싱**: PyMuPDF / pdfplumber (예정)
- **LLM**: Claude API (분석/선별, 예정)
- **스케줄러**: schedule / APScheduler 또는 OS cron (예정)

---

## 프로젝트 관리

- `_pm/TODO.md` — 작업 목록
- `_pm/DONE.md` — 완료 이력
- `_pm/tasks/` — 진행 중 작업 상세 문서
- `_pm/done/` — 완료된 작업 문서 아카이브
