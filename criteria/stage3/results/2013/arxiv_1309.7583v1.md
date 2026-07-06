### arxiv:1309.7583v1 - Optimized Bit Mappings for Spatially Coupled LDPC Codes over Parallel Binary Erasure Channels (2013, arXiv)

| 카테고리 | 값 |
|---|---|
| 이식성 | 하 |
| NAND관련성 | 낮음 |
| 대상 | code-design |
| 부호종류 | SC-LDPC |
| 부호rate | 0.36~0.5 |
| 부호length | 미상 |
| 연판정 | 무관 |
| 핵심기여 | 병렬 BEC 채널에 코드 비트를 배분하는 bit mapper를 differential evolution으로 최적화하여 SC-LDPC 복호 threshold를 개선 |
| HW설계 | X |
| 검증수준 | 이론 |
| 복잡도 | 미상 |
| 병렬화 | 미상 |
| Throughput | 미상 |
| 메모리라우팅 | 없음 |
| 정정능력향상 | X |
| 개선영역 | N/A |
| iteration감소 | O |
| latency | N/A |
| 추천도 | 하 |
| 한계,주의 | BICM/다중반송파 등 병렬채널 특유 시나리오이며 NAND 단일채널 ECC와 무관, 채널모델도 BEC(소거)로 NAND의 BSC/AWGN성 read noise와 다름 |
| 추가확인 | 해당 없음 |

> 총평: BICM 병렬 이진소거채널 특화 bit mapper 최적화 논문으로 NAND binary LDPC ECC 이식 가치는 낮음.

### B. 알고리즘 요약

1. 시스템: 하나의 인코더/디코더가 m개의 병렬 이진 채널(BICM의 bit channel을 독립 BEC로 근사)로 통신, bit mapper가 코드 비트를 채널에 배분.
2. 문제: 균일 랜덤 bit mapper 대비, 병렬 채널 품질 차이를 활용해 SC-LDPC 복호 threshold를 개선하거나 동일 threshold에서 spatial chain length `L`을 줄이고자 함.
3. 채널 모델: 4-PAM/BRGC 라벨링에서 유도된 두 개의 독립 BEC(erasure 확률 `ε1, ε2`), 평균 소거확률 `ε̄`로 파라미터화.
4. 부호: 양측단(two-sided) 및 순환(circular, tail-biting) `(dv, dc, L, w)` SC-LDPC 앙상블, VN erasure 확률의 시공간 진화를 밀도진화(DE) 식 `p_j^(l+1)`로 기술.
5. 핵심 변수: 배분행렬 `A=[a_{i,j}]` (채널 i → 위치 j VN 비율), 열 합=1·행 합=L/m 제약. `A`가 곧 최적화 대상.
6. 최적화: 직접 threshold 최적화(`argmax ε̄*(A)`)는 계산비용이 크므로, 고정 `ε̄`에서 수렴 반복횟수 `l_s(A, ε̄)`를 최소화하는 `A*`를 differential evolution으로 구하고 threshold 재계산을 반복하는 2단계 휴리스틱 사용.
7. 결과 구조: 최적화된 `A*`는 양측단 앙상블에서 한쪽 방향 디코딩 웨이브를 유도하고, 순환 앙상블에서는 가상 종단경계(virtual termination boundary)를 만들어 양방향 웨이브를 유도.
8. 수치 결과: 양측단 `(4,8,L,2)`에서 Δ=0.04일 때 chain length를 L=40→25로 단축 가능(`w=4`), 순환 앙상블은 균일 mapper 대비 threshold가 유의미하게 개선(예: L 증가 시 gap-to-capacity 감소폭 확대).
9. 한계: 무한 코드워드(M→∞) 가정의 점근적 DE 해석뿐, 유한길이 시뮬레이션·HW 구현·에러플로어 분석 없음. L→∞에서는 이득이 0으로 수렴.

### C. Prime ECC 관련 모듈 핀포인트

| 논문 요소 | Prime ECC 모듈 | 관련성 |
|---|---|---|
| bit mapper 최적화(배분행렬 A) | 대응 없음 | Prime ECC는 단일 NAND 채널 대상이며 병렬 채널/BICM bit mapper 개념 자체가 없음 |
| SC-LDPC 앙상블 구성/DE threshold | `ecc_top.cpp` `Load_PCM()` | Prime ECC는 고정 QC-LDPC(비-SC) H-matrix 로드 구조로, SC 앙상블 구성법과 직접 대응 없음 |
| BEC 채널 모델 | `channel.cpp` | Prime ECC는 AWGN/RBER/fixed-error 채널만 지원, BEC(소거) 모델 없음 |

적용 가치: **낮음** — BICM 병렬 채널용 bit mapper 최적화 이론 연구로 NAND 단일채널 binary QC-LDPC ECC의 부호설계·디코더·HW 어느 레이어에도 대응 요소가 없음.

### D. JSON 블록

```json
{
  "id": "arxiv:1309.7583v1",
  "title": "Optimized Bit Mappings for Spatially Coupled LDPC Codes over Parallel Binary Erasure Channels",
  "year": 2013,
  "venue": "arXiv",
  "portability": "하",
  "nand_relevance": "낮음",
  "target": "code-design",
  "code_type": "SC-LDPC",
  "code_rate": "0.36~0.5",
  "code_length": "미상",
  "soft_quant": "무관",
  "key_contribution": "병렬 BEC 채널에 코드 비트를 배분하는 bit mapper를 differential evolution으로 최적화하여 SC-LDPC 복호 threshold를 개선",
  "hw_designed": "X",
  "verification": "이론",
  "complexity": "미상",
  "parallelism": "미상",
  "throughput_gbps": null,
  "mem_routing": "없음",
  "correction_gain": "X",
  "improve_region": "N/A",
  "iter_reduction": "O",
  "latency": "N/A",
  "recommend": "하",
  "caveat": "BICM/다중반송파 등 병렬채널 특유 시나리오이며 NAND 단일채널 ECC와 무관, 채널모델도 BEC(소거)로 NAND의 BSC/AWGN성 read noise와 다름",
  "todo_check": "해당 없음"
}
```
