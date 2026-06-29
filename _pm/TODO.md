# TODO

> Claude 마지막 확인: 2026-06-29 20:13:15

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

### Phase 4: 아이디어 정리 & 평가 — 예정
- [ ] 아이디어 카드 / 실현 가능성 평가 / 알고리즘 pseudo-code

### Phase 5: 관리 & 운영 — 예정
- [ ] 검토 이력 관리 · 저장소 용량 관리 · 리포트 생성

---

## 새 작업 추가
(여기에 새 작업을 적으면 Claude가 처리합니다)
