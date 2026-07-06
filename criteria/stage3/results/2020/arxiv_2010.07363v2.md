### arxiv:2010.07363v2 - Concentrated Stopping Set Design for Coded Merkle Tree: Improving Security Against Data Availability Attacks in Blockchain Systems (2020, arXiv)

| 카테고리 | 값 |
|---|---|
| 이식성 | 하 |
| NAND관련성 | 낮음 |
| 대상 | code-design |
| 부호종류 | irregular |
| 부호rate | 0.5 |
| 부호length | 100 |
| 연판정 | 무관 |
| 핵심기여 | PEG 알고리즘을 entropy-constrained 방식(EC-PEG)으로 변형해 stopping set을 소수 VN 집합에 집중시켜 블록체인 light node의 data availability 공격 탐지 확률을 높임 |
| HW설계 | X |
| 검증수준 | 시뮬 |
| 복잡도 | 미상 |
| 병렬화 | 미상 |
| Throughput | 미상 |
| 메모리라우팅 | 없음 |
| 정정능력향상 | N/A |
| 개선영역 | N/A |
| iteration감소 | N/A |
| latency | N/A |
| 추천도 | 하 |
| 한계,주의 | 채널이 BSC/erasure 기반 peeling decoder(블록체인 CMT) 전용이며, NAND의 BP/min-sum 복호 및 정정능력/error-floor와 무관한 목적함수(stopping set 집중)를 최적화 |
| 추가확인 | EC-PEG의 entropy-minimizing CN 선택 규칙이 일반 PEG 부호 구성(girth 최적화)에 부가적 girth 개선 효과가 있는지 |

> 총평: 블록체인 데이터 가용성 공격 탐지용 특수 목적 LDPC 부호 설계로, NAND 고전 binary LDPC의 정정성능/디코더와 직접적 연관이 없음.

### B. 알고리즘 요약

1. 대상 시스템: 블록체인 Coded Merkle Tree(CMT)에서 LDPC 부호로 인코딩된 레이어, `n=100`, `rate=1/2`, VN degree 정규(`d_v=4`) 부호.
2. 문제: 기존 CMT(Yu et al.)는 무작위 LDPC 앙상블로 stopping ratio를 높이지만, 이는 BSC용으로 설계되어 이 응용(악의적 노드의 stopping set 은닉 탐지)에 최적이 아님.
3. 핵심 모델: 악의적 full node가 stopping set(크기 `μ`)을 숨기면 light node가 무작위 샘플링 `s`회로 탐지 실패할 확률 `p_f(s,μ)=(1-μ/n)^s`.
4. 핵심 기법: stopping set을 직접 다루기 어려워 대신 cycle(길이 `g`)을 소수 VN 집합에 "집중(concentrate)"시키는 EC-PEG(entropy-constrained PEG) 알고리즘 제안.
5. 핵심 식: 새 엣지 후보 CN 중 결합 정규화 사이클카운트 `α_g<gc`의 엔트로피 `H(α_g<gc)`를 최소화하는 CN을 선택 — 엔트로피 최소화가 분포 집중을 유도.
6. 확장: greedy g-sample set `S_g^a`을 구성해 light node 샘플링 전략(Sampling Strategy 1)으로 사용, `Σ(d_v,g)` 이하 가중치 stopping set에 대해 실패확률 0 보장(Lemma 1).
7. 구현 디테일: `g_c=10`까지의 cycle count만 추적(복잡도-정확도 트레이드오프), 최대 CN degree를 무작위 구성 대비 낮춤(11 vs 16)으로 incorrect coding proof 크기 축소.
8. 최적화 절차: PEG의 edge-by-edge 그리디 구성을 엔트로피 최소화 CN 선택으로 대체(별도 학습 없음, 결정론적 그리디).
9. 결과: `n=100`에서 무작위 부호(stopping ratio `β*=0.064353`) 대비 EC-PEG+greedy sampling이 `p_f(s,μ)`를 크게 낮춤(그림3, red/blue vs black/green 곡선).
10. 한계: 순수 시뮬레이션, 짧은 코드(`n=100`)에서만 검증, 채널이 BSC/erasure(peeling decoder) 기반으로 AWGN/NAND soft-decision 복호와 무관, 목적함수가 정정능력이 아닌 stopping set 위치 집중.

### C. Prime ECC 관련 모듈 핀포인트

| 논문 요소 | Prime ECC 모듈 | 관련성 |
|---|---|---|
| EC-PEG 부호 구성(H-matrix 생성) | `ecc_top.cpp` `Load_PCM()` | 부호 구성 방식이나, 목적(stopping set 집중)이 NAND 정정능력과 무관해 대체 후보 아님 |
| Stopping set / cycle 최소화 | 대응 없음 | Prime ECC는 min-sum 복호 기준이며 peeling decoder/stopping set 개념 자체가 없음 |
| 샘플링 전략(light node 검증) | 대응 없음 | 블록체인 특유 개념으로 NAND ECC와 무관 |

> 적용 가치: 낮음 — peeling decoder 기반 블록체인 데이터 가용성 검증이라는 완전히 다른 응용이며, NAND LDPC의 min-sum 복호·정정능력·error-floor와 관련된 기여가 없음.

### D. JSON 블록

```json
{
  "id": "arxiv:2010.07363v2",
  "title": "Concentrated Stopping Set Design for Coded Merkle Tree: Improving Security Against Data Availability Attacks in Blockchain Systems",
  "year": 2020,
  "venue": "arXiv",
  "portability": "하",
  "nand_relevance": "낮음",
  "target": "code-design",
  "code_type": "irregular",
  "code_rate": 0.5,
  "code_length": "100",
  "soft_quant": "무관",
  "key_contribution": "PEG 알고리즘을 entropy-constrained 방식(EC-PEG)으로 변형해 stopping set을 소수 VN 집합에 집중시켜 블록체인 light node의 data availability 공격 탐지 확률을 높임",
  "hw_designed": "X",
  "verification": "시뮬",
  "complexity": "미상",
  "parallelism": "미상",
  "throughput_gbps": null,
  "mem_routing": "없음",
  "correction_gain": "N/A",
  "improve_region": "N/A",
  "iter_reduction": "N/A",
  "latency": "N/A",
  "recommend": "하",
  "caveat": "채널이 BSC/erasure 기반 peeling decoder(블록체인 CMT) 전용이며, NAND의 BP/min-sum 복호 및 정정능력/error-floor와 무관한 목적함수(stopping set 집중)를 최적화",
  "todo_check": "EC-PEG의 entropy-minimizing CN 선택 규칙이 일반 PEG 부호 구성(girth 최적화)에 부가적 girth 개선 효과가 있는지"
}
```
