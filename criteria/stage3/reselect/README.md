# Stage 3 재선별 (reselect)

> 위치: `criteria/stage3/reselect/`
> 성격: **재분석 아님.** stage3 원본 결과(`../results/{연도}/{id}.md`, 6,214편)를 무수정으로 두고,
> 그 위에 선별 축 4개를 추가해 이식 후보를 **OR 조합**으로 재추출한다.
> 배경: 기존 추천도('상' 216편)는 NAND 관련도 의존이 큼 → NAND 무관이라도 Prime ECC 이식 가치가 있는
> hard-decision / 양자화 / 고rate / 장길이 논문을 놓치지 않기 위한 보완 축.

---

## 기준 (2026-07-22 확정)

| 태그 | 이름 | 판정 규칙 | 소스 |
|---|---|---|---|
| **H** | hard decision | `soft_quant = hard-1bit` | JSON 블록 |
| **Q** | 내부 로직 양자화 | 결과 md 텍스트 키워드 스캔 → **걸린 논문 전량 agent 재확인**으로 확정 | md 전문 + agent |
| **R** | high rate | `부호rate ≥ 0.8` | md 표(범위표기 시 **상한** 기준; JSON은 범위 시 null이라 표가 소스) |
| **L** | long length | `부호length ≥ 16384` bit (= 2KB×8) | md 표(범위표기 시 상한 기준, kB 단위는 bit 환산) |

- 조합: **OR** — 하나라도 해당하면 재선별 목록에 포함. 통합 목록에는 태그 컬럼(H/Q/R/L)으로 어느 기준에 걸렸는지 표기.
- `미상`/파싱 불가 값은 해당 기준 미충족으로 처리하되, 건수를 리포트에 별도 집계(누락 감사용).

### Q(내부 로직 양자화) 상세

- **개념**: 채널 read soft 정보(`연판정` 필드)가 아니라, **디코더 내부 메시지/데이터패스가 저비트폭으로 양자화**된 기법
  (예: RCQ, MIM/IB 기반 LUT 디코딩, finite-alphabet(FAID), 저비트폭 min-sum, fixed-point 설계가 핵심 기여인 것).
- **1차 키워드** (대소문자 무시, md 전문 대상): `quantiz`, `양자화`, `bit-width`/`bitwidth`/`bit width`, `저비트`,
  `low-bit`/`low bit`, `저정밀`, `low-precision`/`low precision`, `low-resolution`/`저해상도`, `finite-alphabet`, `FAID`,
  `RCQ`, `MIM`, `information bottleneck`/`정보병목`, `fixed-point`/`고정소수점`, `LUT`
- **2차 확정**: 키워드가 걸린 논문 전량을 agent가 결과 md(분류표+요약 10줄)만 읽고
  "내부 메시지/데이터패스 양자화가 핵심 기법인가"를 O/X + 한 줄 근거로 판정 → [quant_tags.json](quant_tags.json).
  단순 언급(예: 입력 LLR 양자화만, LUT를 다른 용도로 사용)은 X.

## 파일 구성

| 파일 | 역할 |
|---|---|
| [reselect.py](reselect.py) | 6,214편 md 파싱(표+JSON) → H/R/L 판정 + Q 키워드 후보 추출 + 리포트/JSON 생성 |
| [quant_tags.json](quant_tags.json) | Q 2차 agent 판정 결과 (id → O/X + 근거 한 줄) |
| [reselect_report.md](reselect_report.md) | 사람용 리포트: 집계 + 기준별 목록 + 통합 목록(태그 컬럼) |
| [reselect.json](reselect.json) | 기계용: 논문별 태그 + 파싱된 수치 (웹 뷰어·stage4/5 입력) |

## 실행

```
python criteria/stage3/reselect/reselect.py --scan     # H/R/L 판정 + Q 키워드 후보 목록 출력
python criteria/stage3/reselect/reselect.py --report   # quant_tags.json 반영해 최종 리포트/JSON 생성
```

## 파이프라인 연결

- 재선별 목록은 기존 추천도 '상' 216편([../year_progress.md](../year_progress.md))과 **병행하는 보완 축**이다.
- stage5 대상 선정([../../stage5/targets.md](../../stage5/targets.md)) 시 두 축을 모두 후보 풀로 쓴다.
- 웹 뷰어(`docs/`)는 reselect 태그를 포함한 전체 6,214편을 필터링 UI로 제공한다.
