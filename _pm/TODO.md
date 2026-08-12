# TODO

> Claude 마지막 확인: 2026-08-12 15:13:44

전체 로드맵: `_pm/tasks/roadmap/roadmap.md` · 완료 이력: `_pm/DONE.md`

## 작업 목록

### Phase 1: 수집 — ✅ 완료·종료
22,225편(arXiv 1,124 + IEEE 21,101) 확정 보존, 수집 코드 전면 제거. (상세: DONE.md)

### Phase 2: 1차 선별(stage1) — ✅ 완료
- 전체 22,225편 in/out 판정 완료 — 통과 6,222 / 제외 15,999 (+ algo_mod로 알고리즘 기여 분류).
- 진행맵 `review_progress.md`(100%), 기준서 `criteria/stage1/selection_criteria.md`(살아있는 문서).

### Phase 3: 2차 심층 분석(stage2) — 🔄 진행 중
- [x] 분석 프롬프트 · enum 카테고리 설계 (`_test/20260625_phase3_example/`)
- [x] 저장 방식 결정 (md/json 소스 + papers.db enum+round 테이블, 마일스톤 커밋)
- [x] 통과분 PDF 확보 (`data/pdfs/`, 6,220/6,222)
- [ ] 카테고리 확정 (예시 1~2편 더 정독 검증)
- [ ] 전체 5,307편(algo_mod=1) PDF 정독 분류 배치
- [ ] `src/stage2/analyze.py` + `analyze_workflow.js` 정착 (`_test` 프로토타입 이관)

### stage3 재선별(reselect) + 웹 뷰어 — 🔄 진행 중 (상세: `_pm/tasks/stage3_reselect_webviewer/`)
- [x] `criteria/stage3/reselect/` — H(hard-1bit)·Q(내부 양자화)·R(rate≥0.8)·L(length≥2KB) OR 추출
  - 2026-07-22: 6,214편 전량 파싱(실패 0) → H 424 / Q 208 / R 2,031 / L 815, 합집합 2,783편. 리포트 `reselect_report.md` + 태그별 목록 4종 + `reselect.json`
- [x] Q 태그: 키워드 스캔 → 걸린 논문 전량 opus agent 재확인 (원문 재독 없음)
  - 2026-07-22: 키워드 후보 1,948편 → opus 20배치 전수 판정(O 208 / X 1,740), `quant_tags.json`
- [x] `docs/` 웹 뷰어(papers.json 6.21MB + 단일 index.html, 필터/검색/정렬/프리셋) 작성·태그 반영
- [x] GitHub Pages 활성화 + 커밋/푸시 (https://yongsung-kil.github.io/ECC_papers/)
- [x] 디코더양자화 축 확장 (2026-07-22): '핵심 기여'만이던 판정을 본문 txt 스니펫 재판정으로 확장
  - 본문 키워드 스캔 3,086편 → opus 31배치 판정(있음 1,159/없음 1,927) → dq 3값: 핵심 208/있음 1,159/없음 4,847
  - 계기: ieee_6661539(EG-LDPC FPGA)가 HW 구현 양자화인데 X — 기준 문제 확인 후 유무 축 신설
- [ ] 완료 처리(tasks→done 이동) — 보류 중

### stage4: 외부 검증 기반 추가 필터 — 🔄 틀만 (입력 대기)
- [x] 스켈레톤 생성 (`criteria/stage4/`: README·filter_criteria·reviewed_papers·orchestrator + results/)
- [ ] 외부 검증 논문 리스트 채우기 (`criteria/stage4/reviewed_papers.md`, 원천: 루트 `reviewed_papers.txt`)
- [ ] 매핑 방법·필터 방향·출력 형식 확정 → 기준 고정 후 실행 (상세: `criteria/stage4/README.md` "미결정")

### stage5: pseudo-code + 간단 구현 — 🔄 틀만 (대상·언어 대기)ㅇ
- [x] 스켈레톤 생성 (`criteria/stage5/`: README·implementation_prompt·orchestrator·targets + results/_TEMPLATE/)
- [ ] 예시 대상 논문 선정 (stage4 미완 → stage3 샘플, `criteria/stage5/targets.md`)
- [ ] 구현 언어(Python/C++)·검증 깊이 확정 → 예시 1~2편 구현
- [ ] (추후) Prime ECC 3.1 src 실이식

> 참고: 위 stage4/stage5는 `criteria/stageN/` 실행 폴더 번호 기준. 로드맵 Phase 4(아이디어 평가)/Phase 5(운영)와는 번호가 다름.

### 상위 페이지(개요) 제작 — 🔄 진행 중 (상세: `_pm/tasks/20260810_page구성/`)
프로젝트 전체 구조를 보여주는 상위 페이지. 독자는 회사 임원이며 발표 화면으로 쓴다.
- [x] 설계 확정 (`설계.md`) — 사이드바 전체 + 개요 페이지 본문, 메인 블록도 1개 + 보조 3개
- [x] `docs/index.html` 상위 페이지 작성, 기존 탐색기를 `docs/papers.html`로 이동
- [x] 발표 해상도에서 첫 화면 확인 (계산 검증, 육안 확인은 사용자 몫)

### 작업공간 재구성 — 📋 계획 수립 (상세: `_pm/tasks/20260812_작업공간재구성/`)
분석 종료 후 작업 기준을 LDPC_dev로 단일화. 실험 내용은 LDPC_dev, 본 repo는 아카이브 + 탐색기에 적용 상태 표시.
- [x] 방향 논의, 계획 문서 작성 (`재구성계획.md`)
- [x] 디렉토리 정리 (2026-08-12): .superpowers, tmp(41M, DB백업 포함), __pycache__ 4곳, _test 완료실험 4건 제거. BMWM 디자인 문서는 `_pm/tasks/20260810_page구성/`으로 이동. phase3_example은 보존
- [x] LDPC_dev CLAUDE.md에 아카이브 참조 명시 (2026-08-12)
- [x] 본 repo README 아카이브 상태 명시 (2026-08-12)
- [ ] 아이디어 이식 + 원격 실행 규약 (사용자 지시 대기, 외부 머신 환경 확인 필요)
- [ ] 탐색기 통합 (papers.json 상태 필드 + 동기화 스크립트 + papers.html UI)

### Phase 5: 관리 & 운영 — 예정
- [ ] 검토 이력 관리 · 저장소 용량 관리 · 리포트 생성

---

## 새 작업 추가
(여기에 새 작업을 적으면 Claude가 처리합니다)

