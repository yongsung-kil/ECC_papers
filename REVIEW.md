# Phase 2 선별 Runbook

> 새 세션에서 **"REVIEW.md 읽고 진행해"** 라고 하면, 이 절차를 그대로 수행한다.

## 맥락 (한 줄)

LDPC 논문 22,225편(`data/papers.db`)을 **NAND 플래시 LDPC ECC 적용 가능성**으로 선별한다.
판단(LLM)은 외부 API가 아니라 **이 세션의 Claude가 초록을 읽고 직접** 한다. 초록만 본다(PDF 안 봄).

## 절차 (한 배치)

1. **기준 숙지** — `criteria/selection_criteria.md`를 읽는다.

2. **다음 배치 가져오기** (기본 50편):
   ```bash
   PYTHONIOENCODING=utf-8 python -m src.review pending -n 50 --no-criteria > _pending_review.md
   ```
   `_pending_review.md`를 읽는다. "미선별 논문이 없습니다"면 → 선별 완료, 종료 보고.

3. **판단 → JSON** — 각 논문을 기준서대로 **포함/제외(in/out)** 판정해 `_judgments.json`에 저장:
   ```json
   [{"id":"...","decision":"in|out","reason":"한 줄 근거"}]
   ```
   - 포함(in): NAND/스토리지 직접(A/B), 이식 가능 디코더·HW·코드설계(C/D/E)
   - 제외(out): 양자 LDPC·QKD·보안, **소스코딩(압축·양자화)**, 무선부수 언급, 순수이론
   - 애매하면 **포함(in)** 으로 살리고 `reason`에 근거.

4. **DB 기록**:
   ```bash
   PYTHONIOENCODING=utf-8 python -m src.review apply _judgments.json
   ```

5. **진행맵 갱신**:
   ```bash
   PYTHONIOENCODING=utf-8 python -m src.progress
   ```

6. **커밋**(임시파일은 .gitignore됨):
   ```bash
   git add -A && PYTHONIOENCODING=utf-8 git commit -m "review: <N>편 선별" && git push
   ```

7. **보고** — 이번 배치 통과/제외 수 + 누적 진행률(`review_progress.md` 요약).

## 반복

2~7을 반복하면 매번 다음 50편이 자동으로 나온다 (별도 커서 불필요 — `status='new'`만 조회).
배치 크기는 `-n` 값으로 조절(예: 토큰 여유 보고 100~200).

## 결과가 저장되는 곳

- `papers.db` 안 — `filter_results`(score·reason) + `papers.status`(filtered_in/out)
- `review_progress.md` — 진행 현황 맵
- 둘 다 GitHub에 커밋됨
