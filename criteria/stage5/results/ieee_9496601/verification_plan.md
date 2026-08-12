# ieee:9496601 — 검증 계획서 (저쪽 src 환경에서 실행)

> 목적: "이 clip delta가 **실제로 의미가 있는가**(정정능력·bit 절감)"를 토큰-제한 환경이 **빈칸 채우고 실행만** 하도록 설계.
> 원칙: **성능 판정은 여기(float toy)서 하지 않는다.** 이득은 (저bit 내부폭 fixed-point) × (실 QC-LDPC error-floor) × (NAND soft-read)에서만 발현 → src 실코드에서만 권위 있는 숫자.

---

## 1. 실험 대상

| 축 | 값 | 주의 |
|---|---|---|
| 부호 | Prime ECC 실 QC-LDPC(`Load_PCM()`의 `PCM_b`, z=32, 고rate~0.9) | error-floor는 **부호 고유** → 논문 floor 위치·(P,Q) 차용 금지, 실 H에서 재측정 |
| 채널 | (primary) NAND soft-read(RBER, 2SD/3SD) · (secondary) AWGN+3/4bit 양자화(논문 그림 대조) | `channel.cpp` `Set_R_Offset()`/`Set_LLR_Th()` |
| bit-width | 입력 3bit(3SD) 필수, 2bit 보조 + **내부 magnitude/posterior 폭 sweep**(baseline폭, −1bit) | **soft-4bit+ 미지원** → 4bit 논문값 재현 약속 금지 |

## 2. 비교군 (arms)

1. **Baseline** = 현 Prime ECC NMS (clip off = `P=Q=Lm`, 기존 `PARAM_LLR` clamp 그대로).
2. **Asymmetric** = 논문 delta, `P<Q` 스캔 최적.
3. **Symmetric 대조군(P=Q)** = 단일 포화 clip. **"min1·min2를 *서로 다른* 상한으로"가 이득의 원천인지** 격리. arm2가 arm3보다 유의하게 낫지 않으면 신규 기여 불성립.

> ⚠ **baseline 이중정의 리스크(HIGH)**: `PARAM_LLR`가 이미 대칭 포화 중이면 순수 delta는 "clip 추가"가 아니라 "대칭→비대칭"뿐. baseline을 실코드 clamp에 맞춰 고정해야 pass/fail 해석이 안 어긋남.

## 3. 지표

| 지표 | 판정 역할 |
|---|---|
| UBER vs RBER (NAND) / FER·BER vs SNR (AWGN) | 주 곡선 |
| **error-floor 위치** | 헤드라인 — arm2가 arm1 대비 floor를 낮은 UBER/높은 RBER로 미는가 |
| 평균 iteration (실 스케줄 + partial/full CRC 조기종료) | 논문 iter=X·latency=동등 → **악화만 안 하면 됨** |
| **내부폭 iso-성능(−1bit)** | 고정 (P,Q)에서 내부폭 −1bit로 성능 유지 → **Prime ECC 최고가치(면적/전력)** |

## 4. P·Q 스캔 그리드

- 도메인: **내부 magnitude 정수** `[1..Lm]` (입력폭 아님 — [integration_patch.md](integration_patch.md) §3).
- 삼각형 스캔: `for P in 1..Lm: for Q in P..Lm` (`P≤Q` 강제). Lm≈7이면 ~28쌍, a=3급 ~6쌍 → **저렴**.
- 재스캔 단위: (부호 × bit-width × 채널 동작점). 논문값(P≈L/4,Q≈L/2)은 seed로만.
- **α는 Prime ECC 기존값 고정, P·Q만 이동**(1차). 외부 α=0.75(impl.py값) 사용 금지.

## 5. 합격 / 기각 (정량)

- **PASS-A(정정능력)**: 동작 UBER에서 arm2가 arm1 대비 ≥3×(0.5 order) 개선 또는 floor onset을 측정 마진 이상 우측 이동.
- **PASS-B(bit 절감, 최우선)**: 내부폭 −1bit에서 arm2가 arm1 원래폭 UBER를 동등 유지.
- **NEUTRAL-PASS**: 손실 0 + clip 비용 comparator 2개 → config 옵션으로 보존.
- **FAIL**: 최적 (P,Q)에서도 개선 없음 AND −1bit 불가 AND arm2≈arm3(대칭). → 이 코드베이스엔 무의미.
- **iteration 게이트**: 어느 PASS든 avg-iter 악화 ≤5%.

## 6. 통계·비용 예산 (feasibility, HIGH)

- floor(UBER 1e-10~1e-12)는 순수 MC로 ~1e11+ bit → C++에서도 비쌈.
- 분업: **워터폴 = MC(Python 라이트로 부호 예판 가능)** / **floor = Prime ECC C++ bit-exact + IS/trapping-set**(Python 재구현 금지).
- 토큰 절약: 스캔·로깅·플롯을 **런타임 LLM 개입 0**으로 스크립트화해 넘긴다.

## 7. 현재 커버리지 & 여기서 딱 하나 돌려볼 것

- [impl.py](impl.py) = **mechanics smoke test(≈10~15%)**. "clip이 pseudocode대로 돌고 진폭을 α·Q로 억제"까지만. **성능(이득) 커버 0%**(float·flooding·6var toy는 floor 자체가 없음).
- (선택) **이득의 *부호*만 예판**: 정수 fixed-point + floor 알려진 표준부호(802.11n 등)로 소형 MC → 충실한 fixed-point에서도 저내부폭에서 clip이 못 도우면 **값싼 조기경보**(C++ 착수 전). bit-exact 일치는 C++ 몫.
- **스캔 하네스(`scan_pq.py`) 코드는 여기서 만들지 않는다** (2026-07-09 결정). 실 H·채널·내부 magnitude 폭이 있어야 faithful → **src 환경에서 이 §4~8 스펙대로 작성**한다. 이 계획서가 그 구현 명세다.

## 8. CSV 스키마 (로깅)
`code, channel, op_point, a_bits, internal_w, arm, P, Q, frames, frame_err, bit_err, UBER, FER, avg_iter, floor_flag`
