### arxiv:0705.0543v1 - The Design of Efficiently-Encodable Rate-Compatible LDPC Codes (2007, arXiv)

| 카테고리 | 값 |
|---|---|
| 이식성 | 하 |
| NAND관련성 | 낮음 |
| 대상 | code-design |
| 부호종류 | irregular |
| 부호rate | 0.4~0.9 |
| 부호length | 1200~2000 |
| 연판정 | 무관 |
| 핵심기여 | k-step recoverable(k-SR) 개념 기반 mother code 설계로 넓은 rate 범위에서 puncturing 성능이 좋은 E2RC 코드 제안 |
| HW설계 | O |
| 검증수준 | 시뮬 |
| 복잡도 | 미상 |
| 병렬화 | 미상 |
| Throughput | 미상 |
| 메모리라우팅 | 없음 |
| 정정능력향상 | X |
| 개선영역 | N/A |
| iteration감소 | X |
| latency | N/A |
| 추천도 | 하 |
| 한계,주의 | IR Hybrid-ARQ 무선/가변채널용 rate-compatible puncturing 목적으로 NAND 고정rate ECC와 목적 자체가 다름 |
| 추가확인 | 없음 |

> 총평: 무선 IR-HARQ용 rate-compatible puncturing 코드 구성법으로, NAND 고정 rate 부호에는 목적이 맞지 않아 이식 가치가 낮음.

### B. 알고리즘 요약

1. Rate-1/2~0.9(고rate 예제), N=1200~2000, 무선/IR Hybrid-ARQ 채널을 타깃으로 하는 systematic irregular LDPC의 mother code 설계.
2. 기존 랜덤 mother code에 puncturing 알고리즘([8-9])을 적용하면 낮은-k인 k-SR(k-step recoverable) 노드 수가 제한되어 고rate puncturing 성능이 나쁨.
3. k-SR 노드: 소거 복호에서 k번 반복 안에 복구 가능한 punctured variable node. 채널은 오류 없는 소거(erasure) 가정 하 반복복호 분석.
4. 비체계부(H2)를 여러 개의 k-SR 서브행렬(1-SR, 2-SR, ..., d-SR)을 순서대로 배치해 구성. 각 열의 위치는 다항식 `h_{k,j} = D^{j+S_{k-1}}(1+D^{γ(k)})`로 결정.
5. `γ(k) = ceil((M - S_{k-1})/2^{k})` 형태로 절반씩 낮은 k에 배분해 저-k SR 노드 비율을 극대화, 이는 puncturing 시 반복복호 수렴을 빠르게 하려는 설계.
6. depth `d = ceil(log2 M)`이고 degree-2 노드만 puncture 대상으로 삼아 최대 puncturing rate `R_H = K/(N - N_v(2))`까지 rate-compatible 계열을 형성.
7. H2가 하삼각(lower-triangular)이면서 degree-2 열만으로 구성되어 사이클이 없음(Lemma 2,3 증명)을 이용, 선형시간 shift-register(sliding window) 인코더 구현.
8. 인코더는 window size `w=γ(1)`인 division circuit으로 구현, 계수는 시간에 따라 on/off (Fig.3~5). Low-rate(R<0.5) 확장은 degree>2인 L 서브행렬을 추가.
9. 결과: N=1200, rate 0.9에서 E2RC가 eIRA 대비 0.7dB, 일반 irregular LDPC 대비 1.5dB 개선(BER 1e-5); low-rate 확장(N=2000, rate 0.85)에서 최대 2.7dB 개선.
10. 한계: 순수 시뮬레이션(이론+BER 곡선)뿐이며 HW 게이트/throughput 미제시, 무선 IR-HARQ의 가변 rate·시변 채널을 전제로 한 구성으로 NAND 고정 rate ECC와는 목적이 다름.

### C. Prime ECC 관련 모듈 핀포인트

```
| 논문 요소 | Prime ECC 모듈 | 관련성 |
|---|---|---|
| E2RC mother code / H-matrix 구성(k-SR 배치) | [ecc_top.cpp](Prime_ECC_3.1_Claude) `Load_PCM()` | 부호설계 레이어(이식 난이도 높음), Prime ECC는 QC-LDPC 고정 구조라 비QC 랜덤형 E2RC 이식 어려움 |
| Shift-register 기반 선형시간 인코더 | [encoder.cpp](Prime_ECC_3.1_Claude) `LDPC_encoder_4KB()`, `Generate_PCM_encoding()` | Prime ECC는 dual-diagonal 인코딩을 이미 채택, 유사 계열이나 대응 불필요 |
| Rate-compatible puncturing | 대응 없음 | Prime ECC는 고정 rate NAND ECC로 가변 puncturing 미지원 |
```

> 적용 가치: 낮음 — 무선 IR-HARQ 대상 가변 rate puncturing 설계로 NAND 고정 rate binary QC-LDPC와 목적·부호구조가 상이하며, 정정능력/HW 개선 요소가 없음.

### D. JSON 블록

```json
{
  "id": "arxiv:0705.0543v1",
  "title": "The Design of Efficiently-Encodable Rate-Compatible LDPC Codes",
  "year": 2007,
  "venue": "arXiv",
  "portability": "하",
  "nand_relevance": "낮음",
  "target": "code-design",
  "code_type": "irregular",
  "code_rate": null,
  "code_length": "1200~2000",
  "soft_quant": "무관",
  "key_contribution": "k-step recoverable(k-SR) 개념 기반 mother code 설계로 넓은 rate 범위에서 puncturing 성능이 좋은 E2RC 코드 제안",
  "hw_designed": "O",
  "verification": "시뮬",
  "complexity": "미상",
  "parallelism": "미상",
  "throughput_gbps": null,
  "mem_routing": "없음",
  "correction_gain": "X",
  "improve_region": "N/A",
  "iter_reduction": "X",
  "latency": "N/A",
  "recommend": "하",
  "caveat": "IR Hybrid-ARQ 무선/가변채널용 rate-compatible puncturing 목적으로 NAND 고정rate ECC와 목적 자체가 다름",
  "todo_check": "없음"
}
```
