# Stage 4 입력 — 외부 검증 논문 리스트 (템플릿, 나중에 채움)

> 위치: `criteria/stage4/reviewed_papers.md`
> **상태: 빈 템플릿.** 사용자가 "다른 곳에서 검토·검증한 논문"을 여기에 채운다.
> raw 원천: 프로젝트 루트 [reviewed_papers.txt](../../reviewed_papers.txt) (제목·IEEE URL 혼재)

---

## 채우는 법

각 행 = 검증 논문 1편. `stage3_id` 는 매핑되면 채우고, 안 되면 비워둔다(후속 매칭).

- **IEEE**: URL `…/document/9810937` → `stage3_id` = `ieee_9810937` (끝 숫자)
- **arXiv**: `arxiv_YYYY.NNNNNvK`
- **제목만 있는 경우**: `stage3_id` 공란 → 제목 유사도로 후속 매칭

## 표

| # | 제목 / URL (원문) | stage3_id | 외부 검증 결과 | 메모 |
|---|---|---|---|---|
| 1 | (예: https://ieeexplore.ieee.org/document/9810937) | ieee_9810937 | `verified-keep`\|`verified-drop` | (한 줄) |
| 2 | | | | |
| 3 | | | | |

> 검증 결과 enum은 [filter_criteria.md](filter_criteria.md) 축1 참조.
> 채우고 나면 [orchestrator_prompt.md](orchestrator_prompt.md) 절차로 stage3 결과와 대조한다.
