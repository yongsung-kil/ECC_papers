### arxiv:1507.01970v2 - Triggering Wave-Like Convergence of Tail-biting Spatially Coupled LDPC Codes (2015, arXiv)

| 카테고리 | 값 |
|---|---|
| 이식성 | 하 |
| NAND관련성 | 낮음 |
| 대상 | both |
| 부호종류 | SC-LDPC |
| 부호rate | 0.481~0.5 |
| 부호length | 2000 |
| 연판정 | 무관 |
| 핵심기여 | tail-biting SC-LDPC 코드를 랜덤 shortening 또는 두 병렬채널 간 bit interleaving으로 최적화해 termination에 의한 rate-loss를 50% 이상 절감하면서 terminated SC-LDPC와 동등하거나 더 나은 BP 임계값 달성 |
| HW설계 | X |
| 검증수준 | 시뮬 |
| 복잡도 | 미상 |
| 병렬화 | 미상 |
| Throughput | 미상 |
| 메모리라우팅 | 언급 |
| 정정능력향상 | O |
| 개선영역 | waterfall |
| iteration감소 | N/A |
| latency | 악화 |
| 추천도 | 하 |
| 한계,주의 | 대상이 BEC/BAWGN, BICM(4-ASK) 등 통신·광통신 채널이고 density evolution 기반 무한장 ensemble 분석 위주라 NAND 채널(비대칭 read voltage, RBER) 특성과 무관, encoder 측 버퍼링으로 latency가 오히려 증가함을 저자도 명시 |
| 추가확인 | shortening/interleaving 최적화 알고리즘(differential evolution)이 유한 length 실제 NAND용 QC-LDPC 부호(protograph 기반 아님)에 적용 가능한지, buffer 크기 증가가 NAND 컨트롤러 latency 예산에 미치는 영향 확인 필요 |

> 총평: tail-biting SC-LDPC의 rate-loss 완화를 위한 shortening/interleaving 최적화이며 통신·광통신 채널의 DE 기반 이론/시뮬 분석으로, encoder 버퍼링 대가로 latency가 악화되는 순수 부호설계 논문.

### B. 알고리즘 요약

1. 대상: tail-biting SC-LDPC(dv, dc, L, w, n) 앙상블 — 원형 배치된 L개 spatial position, 각 position에 n code bit/m parity 할당, 총 N=Ln bit.
2. 문제의식: SC-LDPC는 BP 복호로 capacity에 근접(threshold saturation)하나 유한 coupling length L에서 termination으로 인한 rate-loss가 무시할 수 없음; tail-biting은 termination 없이 rate-loss를 줄이려는 시도.
3. 핵심 가정: BEC(erasure probability ε)와 BAWGN 채널, density evolution(DE)으로 무한 length 점근 성능 분석. `x_z^(t+1)` 재귀식(BEC 스칼라 갱신)으로 spatial position별 erasure 확률 전파.
4. 핵심 기법 1: 일부 code bit를 0으로 고정하는 랜덤 shortening 비율 `α_z`를 도입, `R(α)` 식으로 design rate 계산, `α*(ε) = argmax R(α)` s.t. BP 복호 성공(δ=1e-7 기준 완화).
5. 핵심 식의 의미: shortening은 BP decoding wave를 트리거하는 "신뢰 가능한" 코드비트를 인위적으로 주입해 threshold saturation을 유도하되 termination보다 rate 손실을 줄임.
6. 핵심 기법 2(확장): 두 병렬 채널(BEC 또는 BICM 4-ASK) 간 코드비트를 spatial position별로 `β_z` 비율로 분배(interleaving)해, shortening 없이도 유사한 threshold saturation 효과를 얻음 — (ε1,ε2) achievable region을 MAP 영역에 근접시킴.
7. 부수 구현 디테일: 비균일 최적화 대신 단순한 "uniform shortening/interleaving"(`α_uni(B)`, `β_uni(B)`)도 거의 동일 성능을 냄; encoder에 code bit를 저장하는 큐(buffer)가 필요하며 큐 길이 `Q(β)=max_z|Q(z)|`가 추가 latency를 유발.
8. 최적화 절차: 작은 L은 이산화된 α 공간 exhaustive search(해상도 Δ=1e-3), 큰 L은 differential evolution 알고리즘 사용; LLR 분포는 [-20,20] 구간 1000레벨 양자화 DE로 계산.
9. 결과: SC-LDPC(3,6,50,3) 예시에서 최적 shortening으로 rate-loss 50% 이상 절감(R(α*)=0.491637 vs terminated 0.4810); BICM 4-ASK에서 non-uniform interleaving으로 BP threshold 3.399dB→2.804dB, terminated 대비 net coding gain ≈0.04dB.
10. 한계: 순수 이론/시뮬(DE, exhaustive/differential evolution 탐색)이며 HW/디코더 구현 전무, 대상 채널이 BEC/BAWGN/BICM(광통신·무선 지향)이고 encoder 버퍼링으로 인한 latency 증가를 저자 스스로 명시.

### C. Prime ECC 관련 모듈 핀포인트

| 논문 요소 | Prime ECC 모듈 | 관련성 |
|---|---|---|
| tail-biting SC-LDPC 부호 구성/shortening 최적화 | `ecc_top.cpp` `Load_PCM()` | Prime ECC는 특정 QC-LDPC(non-SC) H-matrix 고정 사용, tail-biting SC-LDPC 구조나 shortening 기법 자체는 이식 난이도 높음(§4 부호설계=높음) |
| 병렬채널 bit interleaving / 인코딩 큐 | `encoder.cpp` | Prime ECC 인코더는 dual-diagonal 고정 방식이며 병렬채널·큐잉 개념은 NAND 단일 채널 read 구조와 맞지 않아 대응 어려움 |
| BP decoding wave / threshold saturation | 대응 없음 | Prime ECC는 min-sum 기반 iterative 복호이며 SC-LDPC의 spatial decoding wave 개념과 구조적으로 다름(non-coupled QC-LDPC) |

> 적용 가치: 낮음 — SC-LDPC 특유의 tail-biting/shortening/interleaving 부호설계 이론이며 통신·광통신 채널의 DE 분석 위주로, NAND binary QC-LDPC(non-coupled) 구조인 Prime ECC와 코드 토폴로지 자체가 달라 이식 난이도가 매우 높음.

### D. JSON 블록

```json
{
  "id": "arxiv:1507.01970v2",
  "title": "Triggering Wave-Like Convergence of Tail-biting Spatially Coupled LDPC Codes",
  "year": 2015,
  "venue": "arXiv",
  "portability": "하",
  "nand_relevance": "낮음",
  "target": "both",
  "code_type": "SC-LDPC",
  "code_rate": "0.481~0.5",
  "code_length": 2000,
  "soft_quant": "무관",
  "key_contribution": "tail-biting SC-LDPC 코드를 랜덤 shortening 또는 두 병렬채널 간 bit interleaving으로 최적화해 termination에 의한 rate-loss를 50% 이상 절감하면서 terminated SC-LDPC와 동등하거나 더 나은 BP 임계값 달성",
  "hw_designed": "X",
  "verification": "시뮬",
  "complexity": "미상",
  "parallelism": "미상",
  "throughput_gbps": null,
  "mem_routing": "언급",
  "correction_gain": "O",
  "improve_region": "waterfall",
  "iter_reduction": "N/A",
  "latency": "악화",
  "recommend": "하",
  "caveat": "대상이 BEC/BAWGN, BICM(4-ASK) 등 통신·광통신 채널이고 density evolution 기반 무한장 ensemble 분석 위주라 NAND 채널(비대칭 read voltage, RBER) 특성과 무관, encoder 측 버퍼링으로 latency가 오히려 증가함을 저자도 명시",
  "todo_check": "shortening/interleaving 최적화 알고리즘(differential evolution)이 유한 length 실제 NAND용 QC-LDPC 부호(protograph 기반 아님)에 적용 가능한지, buffer 크기 증가가 NAND 컨트롤러 latency 예산에 미치는 영향 확인 필요"
}
```
