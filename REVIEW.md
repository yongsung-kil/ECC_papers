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
   PYTHONIOENCODING=utf-8 python -m src.review batch -n 100 --per 10 --dir _batch
   ```
   출력의 "에이전트 N개"에서 **N**을 기억. **0편이면 → 선별 완료, 종료 보고.**

2. **병렬 판정** (사용자 동의 후 Workflow 실행):
   ```
   Workflow({ scriptPath: "select_workflow.js",
              args: { dir: "_batch", nAgents: N, criteriaFile: "criteria/selection_criteria.md" } })
   ```
   완료되면 `{ judgments, criteria_suggestions, borderline }` 수신.

3. **DB 기록** — `judgments`를 `_judgments.json`에 저장 후:
   ```bash
   PYTHONIOENCODING=utf-8 python -m src.review apply _judgments.json
   ```

4. **경계사례** — `borderline`이 있으면 `criteria/selection_criteria.md`의 "경계 사례" 섹션에
   한 줄씩 append. (이미 충분히 쌓였다고 판단되면 생략)

5. **기준 변경 제안** — `criteria_suggestions`가 있으면 **사용자에게 보고하고 결정을 받는다.**
   승인된 것만 `selection_criteria.md` 본문(in/out·판단절차) 수정. 없으면 건드리지 않음.

6. **진행맵 갱신**:
   ```bash
   PYTHONIOENCODING=utf-8 python -m src.progress
   ```

7. **커밋** — 임시(`_batch/`, `_judgments.json`)는 .gitignore됨:
   ```bash
   git add -A && PYTHONIOENCODING=utf-8 git commit -m "review: <N>편 선별" && git push
   ```

8. **보고** — 이번 청크 in/out 수 + 누적 진행률(`review_progress.md`) + (있으면) 기준 제안.

## 반복

- **"계속"** → 1~8 반복 (다음 100편 자동, `status='new'`만 조회).
- **"N청크 돌려"** → N번 반복.
- 파라미터 변경: 1번의 `-n`/`--per` 값만 조절 (예: `-n 200 --per 20` → 에이전트 10개).
