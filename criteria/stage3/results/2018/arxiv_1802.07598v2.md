### arxiv:1802.07598v2 - Design of Irregular SC-LDPC Codes With Non-Uniform Degree Distributions by Linear Programming (2018, arXiv cs.IT)

| 카테고리 | 값 |
|---|---|
| 이식성 | 하 |
| NAND관련성 | 낮음 |
| 대상 | code-design |
| 부호종류 | SC-LDPC |
| 부호rate | 0.4~0.47 |
| 부호length | 9900~29700 |
| 연판정 | 무관 |
| 핵심기여 | LP 반복(1차원 DE + δu(z) 사전계산)으로 non-uniform degree SC-LDPC 부호를 저복잡도로 설계 |
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
| 한계,주의 | BEC 전용 설계·평가(BP threshold/block erasure), soft-read·AWGN·NAND 채널 미검증, HW 미설계 |
| 추가확인 | AWGN/NAND 채널에서 waterfall/error-floor 성능이 유지되는지, block 구조 SC-LDPC의 NAND 지연 적합성 |

> 총평: BEC 위 SC-LDPC degree 분포 최적화 이론으로, Prime ECC의 고rate binary QC-LDPC block code와 부호 클래스·채널이 달라 이식성 하.

### B. 알고리즘 요약

1. 대상은 L개 위치를 결합한 irregular SC-LDPC 앙상블로, 위치별 variable node degree 분포 `λu(x)`가 비균일(non-uniform)일 수 있는 구조. 채널은 BEC(erasure prob `ε`).
2. 문제: irregular SC-LDPC의 DE 방정식은 위치 수 L만큼 다차원이라 `λu(x)`, `ρ(x)`를 저복잡도로 전역 최적화하기 어렵다.
3. 핵심 아이디어 1 - Local design: 한 쌍의 위치 `u, L-u+1`의 degree 분포만 최적화하고 나머지 위치는 고정, 중앙부터 바깥으로 순차 반복.
4. 핵심 아이디어 2 - `δu(z)` 사전계산(Algorithm 1): 나머지 그래프를 입출력 메시지 관계 `δu(z)`로 요약해 1차원 DE `z⁽ℓ⁺¹⁾ = ε·λu(δu(z⁽ℓ⁾))`로 축약.
5. 1차원 DE 덕분에 uncoupled LDPC용 LP 최적화 도구(설계율 최대화 / 요구 iteration 최소화)를 그대로 적용 가능.
6. Algorithm 2: 목적함수 = 평균 variable node degree 최소화(=설계율 최대화). 그러나 중앙 위치만 개선돼 L이 커지면 효과 축소.
7. Algorithm 3: 목적함수 = 성공복호까지 요구 iteration 수 최소화(평균 degree=l 고정). 모든 위치가 개선돼 BP threshold까지 상승.
8. Algorithm 4: check node degree까지 비균일 허용(`rmin~rmax` 탐색). 자유도 추가로 threshold 추가 개선, 연결행렬 T도 비상수화.
9. 결과: BP threshold가 regular 대비 상승(예 L=10: 0.4981→0.5241(Alg3)→0.5679(Alg4)). MET 구조·SC-RA 적용 시 유한길이 block erasure 성능도 개선.
10. 한계: 전 과정이 BEC 전용(threshold·block erasure로만 평가), AWGN/NAND·soft-read 미검증, HW 미설계, block length 1만~3만의 긴 convolutional 구조.

### C. Prime ECC 관련 모듈 핀포인트

```
| 논문 요소 | Prime ECC 모듈 | 관련성 |
|---|---|---|
| SC-LDPC degree 분포 LP 설계 (λu(x), ρv, T) | 대응 없음 | Prime ECC는 고정 QC-LDPC block code, SC(convolutional) 부호설계 대응 없음 |
| 1차원 DE 기반 부호 최적화 이론 | 대응 없음 | 부호설계 이론이며 코드베이스 디코더/인코더 모듈과 무관 |
| BEC BP 복호 시뮬 | 대응 없음 | Prime ECC는 AWGN/RBER 채널의 min-sum HW 모사, BEC peeling과 무관 |
```

적용 가치: **낮음** — BEC 전용 SC-LDPC 부호설계 이론으로 Prime ECC의 binary QC-LDPC block code·AWGN/soft-read 구조와 부호 클래스와 채널이 모두 달라 떼어 쓸 층이 없다.

### D. JSON 블록

```json
{
  "id": "arxiv:1802.07598v2",
  "title": "Design of Irregular SC-LDPC Codes With Non-Uniform Degree Distributions by Linear Programming",
  "year": 2018,
  "venue": "arXiv cs.IT",
  "portability": "하",
  "nand_relevance": "낮음",
  "target": "code-design",
  "code_type": "SC-LDPC",
  "code_rate": null,
  "code_length": "9900~29700",
  "soft_quant": "무관",
  "key_contribution": "LP 반복(1차원 DE + δu(z) 사전계산)으로 non-uniform degree SC-LDPC 부호를 저복잡도로 설계",
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
  "caveat": "BEC 전용 설계·평가(BP threshold/block erasure), soft-read·AWGN·NAND 채널 미검증, HW 미설계",
  "todo_check": "AWGN/NAND 채널에서 waterfall/error-floor 성능이 유지되는지, block 구조 SC-LDPC의 NAND 지연 적합성"
}
```
