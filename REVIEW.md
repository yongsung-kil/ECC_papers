# Phase 2 선별 Runbook (병렬 오케스트레이터)

> 새 세션에서 **"REVIEW.md 읽고 진행해"** 라고 하면, 메인 Claude가 이 절차로 한 청크를 선별한다.
> **배치 분할 + 병렬 판정(Workflow)까지는 묻지 않고 바로 진행**한다.
> 판정 결과를 받은 뒤 **DB에 기록하기 전(3단계)에만 사용자에게 확인**한다.

## 파라미터 (여기 숫자만 바꾸면 됨)

```
CHUNK = 100   # 한 청크에 선별할 편수
PER   = 10    # 에이전트 1개가 맡는 편수
# → 에이전트 수 = CHUNK / PER = 10  (동시 실행 상한 16)
YEAR  = (없음) # 특정 연도만 진행할 때 지정 (예: "2017년도만 진행해" → --year 2017)
TAG   = (없음) # 다중 세션 구분 라벨 (예: --tag A)
```

- **"2017년도만 진행해"** → 1번 batch에 `--year 2017` 추가. 그 연도 미선별만 분할한다.
- YEAR 미지정 시 전체 미선별 중 **최신 연도부터**.

## 역할 분리

- **판단 규칙**: `criteria/selection_criteria.md` ← 각 sub-agent가 읽음
- **판단 실행**: `select_workflow.js`의 sub-agent (각자 자기 파일만 읽고 in/out)
- **DB 입출력**: `src/review.py` (batch=분할, apply=기록, stats=현황)
- **이 절차서**: 메인(오케스트레이터)이 읽음

## 절차 (한 청크)

1. **배치 분할** — 메인은 초록을 읽지 않는다(파일로만 분할):
   ```bash
   PYTHONIOENCODING=utf-8 python -m src.review batch -n 100 --per 10 [--year 2017] [--tag A]
   ```
   출력의 **`RUN_DIR=...`** 경로(예: `_work/2017-A_20260618_151457`)와 "에이전트 N개"의 **N**을 기억.
   **0편이면 → (해당 연도/전체) 선별 완료, 종료 보고.** (스크래치는 `_work/{라벨}_{타임스탬프}/`에 모두 보존)

2. **병렬 판정** (확인 없이 바로 Workflow 실행):
   ```
   Workflow({ scriptPath: "select_workflow.js",
              args: { dir: "<RUN_DIR>", nAgents: N, criteriaFile: "criteria/selection_criteria.md" } })
   ```
   - `dir`에는 1번의 **`RUN_DIR`** 값을 넣는다.
   - **`args`는 객체 그대로 넘긴다** (JSON 문자열로 감싸지 말 것 — 감싸면 `nAgents=0`으로 빈 결과 종료).
   - 완료되면 `{ judgments, criteria_suggestions }` 수신.
   - **판정 수 < 청크 편수면** 에이전트가 일부를 누락한 것. 누락분은 `status='new'`로 남아
     **다음 청크에서 자동 재조회**되므로 그대로 진행하면 된다(보고만).

3. **검증 + DB 기록**:
   - 먼저 `judgments`를 **`<RUN_DIR>/judgments.json`** 에 저장한 뒤 **무결성 검증**:
     ```bash
     PYTHONIOENCODING=utf-8 python -m src.review verify <RUN_DIR>
     ```
     (DB없는 id·배치밖 id·decision오류·중복을 검사. ❌ 하드에러면 **apply 금지**하고 사용자에게 보고.)
   - 검증 통과(✅)면 판정 결과(in/out 수, 샘플)를 **사용자에게 보고하고 기록 여부를 확인받는다.**
   - 승인되면:
     ```bash
     PYTHONIOENCODING=utf-8 python -m src.review apply <RUN_DIR>/judgments.json
     ```

4. **기준 변경 제안** — `criteria_suggestions`가 있으면 **최종 보고에 모아 적기만 한다.**
   기준서(`selection_criteria.md`) 본문은 **자동 수정하지 않는다**(사용자가 직접 판단). 멈추지 말고 계속 진행.

5. **진행맵 갱신**:
   ```bash
   PYTHONIOENCODING=utf-8 python -m src.progress
   ```

6. **커밋** — 스크래치(`_work/`)는 .gitignore됨. push 충돌 대비 rebase 후 push:
   ```bash
   git add -A && PYTHONIOENCODING=utf-8 git commit -m "review: <N>편 선별"
   git pull --rebase && git push
   ```

7. **보고** — 이번 청크 in/out 수 + 누적 진행률(`review_progress.md`) + (있으면) 기준 제안.

## 반복

- **"계속"** → 1~7 반복 (다음 100편 자동, `status='new'`만 조회).
- **"N청크 돌려"** → N번 반복.
- 파라미터 변경: 1번의 `-n`/`--per`/`--year` 값만 조절.

## 다중 세션 동시 진행 (여러 창에서 병렬)

같은 폴더에서 여러 세션을 동시에 돌릴 때 **겹침·충돌을 막는 규칙**:

1. **세션마다 다른 연도를 맡는다** — 세션A `--year 2017 --tag A`, 세션B `--year 2018 --tag B` …
   `batch`는 `status='new'`를 예약 없이 읽으므로, **연도로 갈라야 같은 논문을 이중 판정하지 않는다.**
   (연도 = 파티션 키. `verify`의 '배치밖 id'와 무관하게, 애초에 배치가 안 겹치게 한다.)
2. **`papers.db`는 한 파일을 공유**한다(디스크 1개 + WAL). 모든 세션의 판정이 같은 DB에 쌓이므로
   apply 자체는 안전하다. 단 **git에서는 papers.db가 바이너리라 병합 불가** →
   **세션마다 매 청크 push 하지 말 것.** 6단계 커밋·push는 **한 세션만(또는 마지막에 한 번)** 담당.
   나머지 세션은 1~5단계(판정+apply)만 돌리고 push는 생략한다.
3. 폴더는 `_work/{연도}-{태그}_{타임스탬프}/`로 자동 분리되어 세션 간 충돌이 없다.
