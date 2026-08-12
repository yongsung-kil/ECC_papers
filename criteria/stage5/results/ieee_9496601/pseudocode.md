# ieee:9496601 — A Low Bit-Width LDPC Min-Sum Decoding Scheme for NAND Flash : Pseudo-code

> 출처 stage3: [../../../stage3/results/2022/ieee_9496601.md](../../../stage3/results/2022/ieee_9496601.md)
> venue: IEEE TCAD 2022 · 대상: decoder · 이식성: 상 · 적용가치: 높음
> 핵심 delta: **CNU에서 min1은 상한 `P`, min2는 상한 `Q`(단 `P≤Q`)로 각각 클리핑** → 저비트폭 NMS 성능손실 완화.

---

## 스펙

- **입력**
  - `H` : QC-LDPC 패리티체크(base+circulant, `p×p`). Tanner graph = check 집합 `C`, variable 집합 `V`, 인접 `N(c)`, `M(v)`.
  - `lambda[v]` : 채널 LLR (NAND soft-read, 저비트폭 fixed-point). 입력 bit-width `a`.
  - `alpha` : normalization factor (기존 NMS와 동일, bit-width별 조정).
  - `P`, `Q` : min1/min2 진폭 상한 (정수, `P ≤ Q`).
  - `max_iter` : 최대 iteration (논문 20).
- **출력**
  - `x_hat[v]` : 복호 비트(0/1), 또는 실패.
- **자료구조**
  - `L[v][c]` : variable→check 메시지 (V2C).
  - `R[c][v]` : check→variable 메시지 (C2V).
- **파라미터 결정**
  - `L_max = 2^(a-1) - 1` (진폭 상한). 정수 전수 스캔으로 `(P,Q)` 선택 — 대략 `Q ≈ L_max/2`, `P ≈ L_max/4`. **부호·bit-width별로 재탐색**.

## 알고리즘 (핵심 delta)

기저는 표준 normalized min-sum. 논문 기여는 아래 `CLIP` 두 줄뿐 (식(3) 대입 직전).

```
FUNCTION MinSumDecode(H, lambda, alpha, P, Q, max_iter):
    # --- 초기화 ---
    FOR each edge (v, c):
        L[v][c] = lambda[v]

    FOR it in 1..max_iter:

        # --- CNU : check node update (여기에 delta) ---
        FOR each check c in C:
            # 인접 V2C 메시지의 부호곱과 최소 두 값
            sign_prod = PRODUCT over v in N(c) of sign(L[v][c])
            (M1, M2, pos1) = TwoSmallestMagnitudes({ |L[v][c]| : v in N(c) })
            #   M1 = 최소값, M2 = 차소값, pos1 = 최소값을 준 variable

            # ★ 논문 핵심 : min1/min2를 서로 다른 상한으로 클리핑 (P ≤ Q)
            M1 = min(M1, P)          # CLIP-1
            M2 = min(M2, Q)          # CLIP-2

            FOR each v in N(c):
                mag = (M2 if v == pos1 else M1)          # 식(3): 자기 최소값이면 차소값 사용
                own_sign = sign_prod * sign(L[v][c])     # 자기 부호 제외
                R[c][v] = alpha * own_sign * mag

        # --- VNU : variable node update ---
        FOR each variable v in V:
            total = lambda[v] + SUM over c in M(v) of R[c][v]
            FOR each c in M(v):
                L[v][c] = truncate( total - R[c][v] )     # fixed-point: 소수부 버림
            posterior[v] = total

        # --- 판정 & 조기종료 ---
        x_hat[v] = (posterior[v] < 0) ? 1 : 0
        IF H · x_hat == 0 (mod 2):
            RETURN x_hat                                  # syndrome=0 → 성공

    RETURN x_hat (or FAIL)                                # max_iter 도달
```

```
FUNCTION TwoSmallestMagnitudes(mags):
    M1 = M2 = +inf ; pos1 = -1
    FOR (idx, m) in mags:
        IF m < M1: M2 = M1 ; M1 = m ; pos1 = idx
        ELIF m < M2: M2 = m
    RETURN (M1, M2, pos1)          # 동률이면 최소 위치 1개만 표시(랜덤 택1)
```

## 참고

- **논문 근거**: 클리핑은 §CNU 식(3) 대입 직전 `M1m=min{M1m,P}`, `M2m=min{M2m,Q}` (B.요약 4항).
- **기존(표준 NMS) 대비 바뀐 부분**: `CLIP-1`, `CLIP-2` 두 줄이 전부. 나머지는 동일한 min-sum.
- **의미**: 두 값을 다른 진폭으로 눌러 iteration별 LLR 성장 속도를 늦춤 → error-floor 지연, VNU/posterior 내부 bit-width 1bit 절감(§B 5·9항).
- **스케줄 무관**: 논문은 row-layered지만 클리핑 delta는 flooding/layered 무관하게 동일. (프로토타입은 flooding으로 검증 — [impl.py](impl.py))
- **한계**: `(P,Q)`는 부호·bit-width별 시뮬 스캔 필요, HW 미구현(comparator 2개 추가 주장). (stage3 caveat)
