### arxiv:1204.0556v2 - Decomposition Methods for Large Scale LP Decoding (2012, arXiv)

| 카테고리 | 값 |
|---|---|
| 이식성 | 중 |
| NAND관련성 | 간접 |
| 대상 | decoder |
| 부호종류 | 기타 |
| 부호rate | 0.5~0.77 |
| 부호length | 1002~2640 |
| 연판정 | soft-4bit+ |
| 핵심기여 | Linear Programming(LP) 복호를 ADMM으로 분산·병렬화하고, parity polytope에 대한 "two-slice" 표현으로 유클리드 투영을 선형시간 알고리즘화하여 대규모 LDPC 부호에 실용적으로 적용 |
| HW설계 | X |
| 검증수준 | 시뮬 |
| 복잡도 | 미상 |
| 병렬화 | 완전병렬 |
| Throughput | 미상 |
| 메모리라우팅 | 없음 |
| 정정능력향상 | O |
| 개선영역 | error-floor |
| iteration감소 | X |
| latency | 동등 |
| 추천도 | 중 |
| 한계,주의 | 부호는 일반 binary LDPC(Margulis, Tanner류)이며 Min-Sum이 아닌 LP/ADMM 기반 완전히 다른 복호 패러다임이라 기존 min-sum 디코더 구조에 직접 이식 불가, 고정소수점/HW 설계 전무 |
| 추가확인 | ADMM iteration당 요구 반복수는 BP보다 많음(수치 없음, "더 많다"고만 서술) - NAND read latency 목표와 상충 가능성 검토 필요 |

> 총평: BP 대비 error-floor가 관측되지 않는 LP/ADMM 복호 기법으로 정정성능 관점에서 흥미로우나, 복호 패러다임 자체가 min-sum과 전혀 다르고 HW 설계가 없어 Prime ECC 이식은 구조적으로 어려움.

### B. 알고리즘 요약

1. `M×N` parity-check 행렬 `H`를 갖는 이진 LDPC 부호(정규/비정규)에 대해 Feldman의 LP 복호(ML 복호의 convex relaxation, `conv(C)` 위에서 `γ^T x` 최소화)를 표준 LP solver 대신 ADMM으로 분산 처리해 실용 블록길이까지 확장하는 것이 목표.
2. 기존 LP 복호는 이론적으로 BP 대비 error-floor가 낮다는 장점이 있으나 표준 LP solver로는 수천 비트급 부호에 계산량이 너무 커 실용성이 없었음.
3. 채널 모델은 표준 AWGN/BSC이며 새로운 채널 모델 제시 없음; 새로움은 오직 최적화 알고리즘/기하학적 표현에 있음.
4. 핵심 기법: 각 parity-check 제약을 parity polytope `PPd = conv({e∈{0,1}^d | sum(e) even})`에 대한 투영 문제로 분해하고, ADMM으로 변수(`x`)-업데이트와 체크(`z`)-업데이트를 교대로 반복(`x_{k+1}`, `z_{k+1}`, `λ_{k+1}` 갱신).
5. `x`-update는 `[0,1]^N` 하이퍼큐브로의 투영(단순 클리핑), `z`-update는 `parity polytope`으로의 유클리드 투영으로, 이는 기존 sum-product BP의 `tanh`/`log` 연산과 성격이 다른 message-passing 스케줄이다.
6. 핵심 확장(2단): "two-slice" 정리 — parity polytope의 임의의 점은 Hamming weight `r`과 `r+2`인 정점들의 볼록조합만으로 표현 가능함을 증명하여, `O(d^2)` 변수의 기존(Yannakakis) 표현을 `O(d)`로 축소.
7. 구현 디테일: 정렬(sort) + 최대 `d`개의 breakpoint 탐색으로 투영을 `O(d log d)`(정렬 지배) 시간에 계산하는 Algorithm 2(waterfilling형); check-node 연산이 `tanh`/`log` 없이 기본 산술연산만 사용해 "HW 친화적"이라 서술(정성적 언급, 정량 HW 검증은 없음). Over-relaxation 파라미터 `ρ∈[1,2)` 도입으로 평균 복호시간 약 50% 단축.
8. 별도 학습 절차 없음(최적화 이론 기반); 파라미터 `ε`(허용오차), `μ`(penalty), `t_max`(최대 반복)의 민감도만 실험적으로 탐색.
9. 결과: [2640,1320] rate-0.5 Margulis 부호, [1057,813] rate-0.77 부호, 길이 1002 (3,6)-regular 앙상블 100개에서 ADMM이 BP 대비 WER 10^-10까지 error-floor 미관측(BP는 flare 관측); 반복수는 ADMM이 BP보다 많으나 실행시간은 BP와 비슷하거나 correct decoding시 더 빠름.
10. 한계: 부동소수점 시뮬레이션뿐이며 고정소수점/양자화, HW 아키텍처, gatecount, throughput 등 전혀 다루지 않음; waterfall 영역은 BP보다 약 0.4dB 늦게 시작하는 트레이드오프 존재.

### C. Prime ECC 관련 모듈 핀포인트

| 논문 요소 | Prime ECC 모듈 | 관련성 |
|---|---|---|
| ADMM 기반 LP 복호(전체 알고리즘) | [decoder.cpp](Prime_ECC_3.1_Claude) `LDPC_Decoder()` | 반복복호 루프 위치는 대응되나 Min-Sum C2V/V2C 갱신 자체를 parity polytope 투영으로 전면 교체해야 해 통합 난이도 높음 |
| parity polytope 투영(체크노드 연산) | [decoder.cpp](Prime_ECC_3.1_Claude) `CNU_Update_New_Mag()`, `C2V_Cal_New_Sgn()` | Min-Sum의 min1/min2 연산과 근본적으로 다른 연산(정렬+선형탐색)이라 대응 없음에 가까움 |
| error-floor 억제(트래핑셋 없이) | 대응 없음 | Prime ECC는 Min-Sum + 조기종료(Partial CRC) 방식으로 error-floor 대응, LP/ADMM 패러다임과 무관 |
| over-relaxation을 통한 반복수/시간 단축 | 대응 없음 | Prime ECC의 조기종료(Partial CRC)와는 다른 메커니즘(최적화 파라미터 튜닝) |

> 적용 가치: 낮음 — 알고리즘 패러다임이 Min-Sum과 근본적으로 달라 기존 HW 파이프라인(z=32, HCU, GT)에 이식하려면 디코더 코어를 전면 재설계해야 함.

### D. JSON 블록

```json
{
  "id": "arxiv:1204.0556v2",
  "title": "Decomposition Methods for Large Scale LP Decoding",
  "year": 2012,
  "venue": "arXiv",
  "portability": "중",
  "nand_relevance": "간접",
  "target": "decoder",
  "code_type": "기타",
  "code_rate": "0.5~0.77",
  "code_length": "1002~2640",
  "soft_quant": "soft-4bit+",
  "key_contribution": "Linear Programming(LP) 복호를 ADMM으로 분산·병렬화하고, parity polytope에 대한 two-slice 표현으로 유클리드 투영을 선형시간 알고리즘화하여 대규모 LDPC 부호에 실용적으로 적용",
  "hw_designed": "X",
  "verification": "시뮬",
  "complexity": "미상",
  "parallelism": "완전병렬",
  "throughput_gbps": null,
  "mem_routing": "없음",
  "correction_gain": "O",
  "improve_region": "error-floor",
  "iter_reduction": "X",
  "latency": "동등",
  "recommend": "중",
  "caveat": "부호는 일반 binary LDPC(Margulis, Tanner류)이며 Min-Sum이 아닌 LP/ADMM 기반 완전히 다른 복호 패러다임이라 기존 min-sum 디코더 구조에 직접 이식 불가, 고정소수점/HW 설계 전무",
  "todo_check": "ADMM iteration당 요구 반복수는 BP보다 많음(수치 없음, 더 많다고만 서술) - NAND read latency 목표와 상충 가능성 검토 필요"
}
```
