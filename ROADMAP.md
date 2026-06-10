# Auto Paper Analysis — Roadmap

LDPC 논문 자동 수집 → 선별 → 분석 → 아이디어 정리 시스템

## Phase 1: 논문 수집 (Crawling & API)
- [ ] **1-1. arXiv API 수집기** — arXiv API로 LDPC 관련 논문 메타데이터 + PDF 수집
- [ ] **1-2. IEEE Xplore API 수집기** — IEEE Xplore API로 LDPC 논문 수집
- [ ] **1-3. 수집 DB 구축** — 수집된 논문 메타데이터 저장 (SQLite, 중복 체크 포함)
- [ ] **1-4. 스케줄러** — 주기적 자동 수집 (cron/scheduler)

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
| Phase 1 | **진행 예정** | 1-1 arXiv API부터 시작 |
| Phase 2 | 대기 | |
| Phase 3 | 대기 | |
| Phase 4 | 대기 | |
| Phase 5 | 대기 | |

---

## 기술 스택 (예정)

- **언어**: Python 3.11+
- **논문 API**: arxiv (Python 패키지), IEEE Xplore API
- **DB**: SQLite (로컬, 경량)
- **PDF 파싱**: PyMuPDF / pdfplumber
- **LLM**: Claude API (분석/선별)
- **스케줄러**: schedule / APScheduler 또는 OS cron
