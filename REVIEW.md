# Phase 2 선별 Runbook (병렬 오케스트레이터)

> 새 세션에서 **"REVIEW.md 읽고 진행해"** 라고 하면, 메인 Claude가 이 절차로 한 청크를 선별한다.
> 멀티에이전트 **Workflow**를 쓴다 → 토큰을 많이 쓰므로 **Workflow 실행 전 사용자에게 확인**한다.

## 파라미터 (여기 숫자만 바꾸면 됨)

```
CHUNK = 100   # 한 청크에 선별할 편수
PER   = 10    # 에이전트 1개가 맡는 편수
# → 에이전트 수 = CHUNK / PER = 10  (동시 실행 상한 16)
```

## 역할 분리

- **판단 규칙**: `criteria/selection_criteria.md` ← 각 sub-agent가 읽음
- **판단 실행**: `select_workflow.js`의 sub-agent (각자 자기 파일만 읽고 in/out)
- **DB 입출력**: `src/review.py` (batch=분할, apply=기록, stats=현황)
- **이 절차서**: 메인(오케스트레이터)이 읽음

## 절차 (한 청크)

1. **배치 분할** — 메인은 초록을 읽지 않는다(파일로만 분할):
   ```bash
   PYTHONIOENCODING=utf-8 python -m src.review batch -n 100 --per 10
   ```
   출력의 **`RUN_DIR=...`** 경로(예: `_work/20260617_084500`)와 "에이전트 N개"의 **N**을 기억.
   **0편이면 → 선별 완료, 종료 보고.** (스크래치는 `_work/{타임스탬프}/`에 실행별로 모두 보존됨)

2. **병렬 판정** (사용자 동의 후 Workflow 실행):
   ```
   Workflow({ scriptPath: "select_workflow.js",
              args: { dir: "<RUN_DIR>", nAgents: N, criteriaFile: "criteria/selection_criteria.md" } })
   ```
   - `dir`에는 1번의 **`RUN_DIR`** 값을 넣는다.
   - **`args`는 객체 그대로 넘긴다** (JSON 문자열로 감싸지 말 것 — 감싸면 `nAgents=0`으로 빈 결과 종료).
   - 완료되면 `{ judgments, criteria_suggestions }` 수신.
   - **판정 수 < 청크 편수면** 에이전트가 일부를 누락한 것. 누락분은 `status='new'`로 남아
     **다음 청크에서 자동 재조회**되므로 그대로 진행하면 된다(보고만).

3. **DB 기록** — `judgments`를 **`<RUN_DIR>/judgments.json`** 에 저장 후:
   ```bash
   PYTHONIOENCODING=utf-8 python -m src.review apply <RUN_DIR>/judgments.json
   ```

4. **기준 변경 제안** — `criteria_suggestions`가 있으면 **사용자에게 보고하고 결정을 받는다.**
   승인된 것만 `selection_criteria.md` 본문(in/out·판단절차) 수정. 없으면 건드리지 않음.

5. **진행맵 갱신**:
   ```bash
   PYTHONIOENCODING=utf-8 python -m src.progress
   ```

6. **커밋** — 스크래치(`_work/`)는 .gitignore됨:
   ```bash
   git add -A && PYTHONIOENCODING=utf-8 git commit -m "review: <N>편 선별" && git push
   ```

7. **보고** — 이번 청크 in/out 수 + 누적 진행률(`review_progress.md`) + (있으면) 기준 제안.

## 반복

- **"계속"** → 1~8 반복 (다음 100편 자동, `status='new'`만 조회).
- **"N청크 돌려"** → N번 반복.
- 파라미터 변경: 1번의 `-n`/`--per` 값만 조절 (예: `-n 200 --per 20` → 에이전트 10개).
