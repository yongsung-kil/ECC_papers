"""
ieee:9496601 — A Low Bit-Width LDPC Min-Sum Decoding Scheme for NAND Flash (TCAD 2022)
delta 정확성 레퍼런스 (stage5 예시). 언어: Python.

핵심 delta = CNU에서 min1은 상한 P, min2는 상한 Q(P<=Q)로 각각 클리핑. (아래 CLIP-1/CLIP-2 2줄)
pseudocode.md 와 1:1 대응. 스케줄은 flooding (클리핑 delta는 스케줄 무관).

⚠ 이 파일의 성격 (오해 금지):
- **mechanics smoke test**일 뿐이다. "clip이 pseudocode대로 돌고 진폭을 상한 이하로 억제"까지만 확인.
- **성능(이득) 검증이 아니다.** 논문 이득(저bit 내부폭 UBER↓·error-floor 지연·bit 절감)은
  실 QC-LDPC·저bit fixed-point·NAND soft-read에서만 발현 → float·flooding·6var toy로는 관측 불가.
- 디코더 본체(H·스케줄·VNU·min1/min2 계산)는 **전이 대상 아님**(Prime ECC가 이미 보유). 전이되는 건 CLIP 2줄뿐.
- 성능 검증 설계는 verification_plan.md, 실이식은 integration_patch.md 참조. 실측 무대는 src(C++/py Prime ECC).

실행: python impl.py
"""
import math


# --- toy QC-LDPC 급 소형 부호: 6 vars, 3 checks, col-weight 2, row-weight 4 ---
#   c0: v0 v1 v2 v3
#   c1: v0 v1 v4 v5
#   c2: v2 v3 v4 v5
H = [
    [0, 1, 2, 3],
    [0, 1, 4, 5],
    [2, 3, 4, 5],
]
NV = 6
M_of_v = [[c for c, row in enumerate(H) if v in row] for v in range(NV)]  # 각 var가 속한 check


def sign(x):
    return -1.0 if x < 0 else 1.0


def two_smallest(pairs):
    """pairs = [(var_idx, magnitude), ...] -> (M1, M2, pos1). pseudocode의 TwoSmallestMagnitudes."""
    M1 = M2 = math.inf
    pos1 = -1
    for idx, m in pairs:
        if m < M1:
            M2, M1, pos1 = M1, m, idx
        elif m < M2:
            M2 = m
    return M1, M2, pos1


def syndrome_ok(H, x):
    return all(sum(x[v] for v in row) % 2 == 0 for row in H)


def min_sum_decode(H, lam, alpha=0.75, P=math.inf, Q=math.inf, max_iter=20, quantize=None):
    """
    P=Q=inf 이면 클리핑 없는 표준 NMS(baseline).
    quantize: fixed-point 흉내용 truncation 함수(옵션).
    반환: (x_hat, iters, converged, max_abs_R)  # max_abs_R = 관측된 최대 |C2V| 진폭
    """
    L = {(v, c): lam[v] for v in range(NV) for c in M_of_v[v]}   # V2C 초기화
    R = {}
    x_hat = [0] * NV
    max_abs_R = 0.0
    for it in range(1, max_iter + 1):
        # --- CNU (delta 위치) ---
        for c, row in enumerate(H):
            sign_prod = 1.0
            for v in row:
                sign_prod *= sign(L[(v, c)])
            M1, M2, pos1 = two_smallest([(v, abs(L[(v, c)])) for v in row])
            M1 = min(M1, P)      # ★ CLIP-1
            M2 = min(M2, Q)      # ★ CLIP-2
            for v in row:
                mag = M2 if v == pos1 else M1
                own_sign = sign_prod * sign(L[(v, c)])   # 자기 부호 제외
                R[(c, v)] = alpha * own_sign * mag
                max_abs_R = max(max_abs_R, abs(R[(c, v)]))
        # --- VNU ---
        posterior = [0.0] * NV
        for v in range(NV):
            total = lam[v] + sum(R[(c, v)] for c in M_of_v[v])
            posterior[v] = total
            for c in M_of_v[v]:
                msg = total - R[(c, v)]
                L[(v, c)] = quantize(msg) if quantize else msg
        # --- 판정 & 조기종료 ---
        x_hat = [1 if posterior[v] < 0 else 0 for v in range(NV)]
        if syndrome_ok(H, x_hat):
            return x_hat, it, True, max_abs_R
    return x_hat, max_iter, False, max_abs_R


def _selfcheck():
    # all-zero codeword 전송, BPSK 0->+1 => 정상 LLR 양수(정수 스케일). 1개 비트를 오류(음수)로 뒤집음.
    ALPHA = 0.75
    clean = [6.0] * NV                  # 확신도 높은 정상 LLR (4bit 스케일 ~ [-7,7])
    lam = list(clean)
    lam[0] = -4.0                       # v0 오류 (부호 반전)
    print("수신 LLR:", lam, "(부호<0 인 v0 가 오류)")

    x0, it0, ok0, r0 = min_sum_decode(H, lam, alpha=ALPHA)                    # baseline NMS
    print(f"[baseline NMS]        x_hat={x0} iters={it0} conv={ok0} max|R|={r0:.2f}")

    # 저비트폭 클리핑: 입력 bit-width a=4 -> L_max=7, 논문 근사 Q~L/2, P~L/4
    Lmax = 2 ** (4 - 1) - 1             # =7
    P, Q = Lmax // 4, Lmax // 2         # =1, 3
    x1, it1, ok1, r1 = min_sum_decode(H, lam, alpha=ALPHA, P=P, Q=Q,
                                      quantize=lambda m: float(int(m)))       # trunc = fixed-point
    print(f"[clipped NMS P={P} Q={Q}]  x_hat={x1} iters={it1} conv={ok1} max|R|={r1:.2f}")

    # --- mechanics smoke test (성능 아님) ---
    # (1) sanity: 자명한 1비트 오류 시나리오에서 파이프라인이 돈다 (수렴 여부는 toy라 의미 약함)
    assert ok0 and x0 == [0] * NV, "baseline sanity 실패"
    assert ok1 and x1 == [0] * NV, "clipped sanity 실패"
    # (2) mechanics: clip이 실제로 |C2V| 진폭을 상한 alpha*Q 이하로 강제하는가 (정의상 참 = 삽입 확인용)
    assert r1 <= ALPHA * Q + 1e-9, f"클리핑 상한 위반: {r1} > {ALPHA*Q}"
    assert r1 < r0, "clip이 진폭을 억제하지 못함(삽입 누락?)"
    print(f"mechanics smoke test PASS: clip이 max|R| {r0:.2f}->{r1:.2f} (<= alpha*Q={ALPHA*Q:.2f}) 로 억제. "
          f"[성능 아님 — verification_plan.md 참조]")


if __name__ == "__main__":
    _selfcheck()
