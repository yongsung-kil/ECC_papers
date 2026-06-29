# src/stage2 — 2차: PDF 정독 분류 + 이식성 판정

통과(1차 algo_mod=1) 논문의 **PDF 본문을 읽어** enum 카테고리로 분류한다.
현재 `_test/20260625_phase3_example/`에서 프로토타이핑 중 — 확정되면 이리로 정착.

예정 모듈:
- `analyze.py` — 미분석 분할(batch) / 결과 기록(apply) / 현황(stats)
- `analyze_workflow.js` — 정독 분석 병렬 워크플로
- 기준: `criteria/stage2/` (categories.md · prompt.md)
- 저장처: 결과 md/json이 소스 → `data/papers.db`에 enum+round 컬럼 테이블로 적재(차수 마일스톤에만 커밋). 카탈로그는 `data/catalogs/`
