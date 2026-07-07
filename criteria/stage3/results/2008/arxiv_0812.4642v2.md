### arxiv:0812.4642v2 - Error-Trellis State Complexity of LDPC Convolutional Codes Based on Circulant Matrices (2009, arXiv cs.IT)

| 카테고리 | 값 |
|---|---|
| 이식성 | 하 |
| NAND관련성 | 낮음 |
| 대상 | other |
| 부호종류 | QC-LDPC |
| 부호rate | 0.41 |
| 부호length | 155 |
| 연판정 | 무관 |
| 핵심기여 | monomial `H(D)`의 행/열 순환시프트(row/column operation)로 error-trellis OCL을 최소거리 보존하며 대폭 축소 |
| HW설계 | X |
| 검증수준 | 이론 |
| 복잡도 | 미상 |
| 병렬화 | 미상 |
| Throughput | 미상 |
| 메모리라우팅 | 언급 |
| 정정능력향상 | N/A |
| 개선영역 | N/A |
| iteration감소 | N/A |
| latency | N/A |
| 추천도 | 하 |
| 한계,주의 | trellis 기반 복호 패러다임(반복 message-passing 아님)·저rate(0.41) convolutional code 대상이라 NAND binary QC-LDPC 반복복호에 직접 무관 |
| 추가확인 | 없음 (Prime ECC 반복복호 경로와 접점 없음) |

> 총평: QC 코드에서 unwrap한 LDPC convolutional code의 error-trellis 상태복잡도(OCL)를 순환시프트로 줄이는 순수 이론 논문으로, min-sum 반복복호 기반 Prime ECC와는 복호 패러다임 자체가 달라 이식 가치 없음.

### B. 알고리즘 요약

1. 대상: Tanner et al.[10]의 (155,64) QC 블록코드(`m=31`, `dmin=20`)를 unwrapping해 얻은 LDPC convolutional code로, 다항식 parity-check `H(D)`의 모든 엔트리가 monomial(`D^x`)이다.
2. 문제: 이런 convolutional code는 constraint length가 커 trellis 기반 복호의 상태공간(2^ν)이 과대 → 실용 불가로 알려짐. 상태복잡도(OCL, overall constraint length)를 줄이는 게 목표.
3. 모델: `F=GF(2)`, syndrome former `H^T(D)`의 adjoint-obvious realization 기반 error-trellis. 시각-k error `e_k`와 syndrome `ζ_k=e_k H^T(D)`.
4. 핵심기법1(행/열 연산): `H(D)`의 i행이 인자 `D^{l_i}`를 가지면 syndrome subsequence를 `l_i` 시프트, j열이 `D^{l_j}`를 가지면 error subsequence를 `l_j` 시프트해 인자를 소거 → 상태 수 감소(row/column operation).
5. 의미: 인자 소거는 error path의 부분수열을 시간 이동시키는 것과 등가라, 정정능력(자유거리)은 그대로 두고 trellis 상태만 줄인다.
6. 핵심기법2(행 순환시프트 탐색): 원본 `H`의 각 블록 행을 순환시프트하면 QC 블록코드/제약그래프는 불변이지만 대응 `H'(D)`의 monomial 인자가 달라져 OCL이 달라짐 → 시프트 패턴 `[P_i,Q_j,R_k]` (5×5×5=125가지) 탐색.
7. 부수기법: reciprocal dual encoder `H̃(D)`로 backward-shift 활용(열 인자 `D^l` ↔ `D^{-l}`), 그리고 reciprocal+재적용으로 추가 OCL 감소(Δμ).
8. 효율 탐색: 각 열의 max-min 편차 `δ_j ≤ Δ`(예 Δ=20)인 패턴만 검색해 OCL 최소 후보를 빠르게 찾음.
9. 결과: 125패턴 중 OCL `μ_min=35`(원 평균 대비 대폭↓, `μ_max=83`), reciprocal dual로 `η_min=31`, 추가기법으로 최대 Δμ=16 및 μ'=34까지 감소. 자유거리 `d'_free ≥ dmin=20` 보존.
10. 한계: HW 미설계, BER 시뮬 없음(OCL 열거 분석뿐), trellis 복호 자체가 여전히 고비용이며 반복 message-passing 복호와 무관.

### C. Prime ECC 관련 모듈 핀포인트

| 논문 요소 | Prime ECC 모듈 | 관련성 |
|---|---|---|
| error-trellis 상태복잡도(OCL) 축소 | 대응 없음 | Prime ECC는 반복 min-sum message-passing 복호로 trellis-state 개념 자체가 없음 |
| monomial `H(D)` 행/열 순환시프트 | 대응 없음 | convolutional code 다항식 표현 조작으로, `PCM_b` binary circulant 구조와 무관 |
| QC 블록코드→LDPC convolutional unwrap | 대응 없음 | Prime ECC는 고정 binary QC-LDPC 블록코드(비 convolutional) |

적용 가치: 낮음 - trellis 기반 convolutional code 복호 이론이라 NAND용 반복복호 binary QC-LDPC 코드베이스(Prime ECC 3.1)와 접점이 전혀 없다.

### D. JSON 블록

```json
{
  "id": "arxiv:0812.4642v2",
  "title": "Error-Trellis State Complexity of LDPC Convolutional Codes Based on Circulant Matrices",
  "year": 2009,
  "venue": "arXiv cs.IT",
  "portability": "하",
  "nand_relevance": "낮음",
  "target": "other",
  "code_type": "QC-LDPC",
  "code_rate": 0.41,
  "code_length": "155",
  "soft_quant": "무관",
  "key_contribution": "monomial H(D)의 행/열 순환시프트로 error-trellis OCL을 최소거리 보존하며 대폭 축소",
  "hw_designed": "X",
  "verification": "이론",
  "complexity": "미상",
  "parallelism": "미상",
  "throughput_gbps": null,
  "mem_routing": "언급",
  "correction_gain": "N/A",
  "improve_region": "N/A",
  "iter_reduction": "N/A",
  "latency": "N/A",
  "recommend": "하",
  "caveat": "trellis 기반 복호 패러다임(반복 message-passing 아님)·저rate(0.41) convolutional code 대상이라 NAND binary QC-LDPC 반복복호에 직접 무관",
  "todo_check": "없음 (Prime ECC 반복복호 경로와 접점 없음)"
}
```
