### arxiv:1712.08538v5 - Sparse Graphs for Belief Propagation Decoding of Polar Codes (2018, arXiv/cs.IT)

| 카테고리 | 값 |
|---|---|
| 이식성 | 하 |
| NAND관련성 | 낮음 |
| 대상 | both |
| 부호종류 | 기타 |
| 부호rate | 0.5 |
| 부호length | 256~32768 |
| 연판정 | 무관 |
| 핵심기여 | 폴라 부호를 LDPC-like 부호로 보고 encoding factor graph를 pruning해 sparse H로 BP 복호 |
| HW설계 | X |
| 검증수준 | 시뮬 |
| 복잡도 | 미상 |
| 병렬화 | 완전병렬 |
| Throughput | 미상 |
| 메모리라우팅 | 언급 |
| 정정능력향상 | X |
| 개선영역 | N/A |
| iteration감소 | X |
| latency | 개선 |
| 추천도 | 하 |
| 한계,주의 | 폴라 부호 전용 pruning으로 QC-LDPC 부호설계와 무관, 원본 BP 대비 평균 iteration 증가 |
| 추가확인 | 없음 |

> 총평: 폴라 부호를 sparse LDPC-like 그래프로 복호하는 기법으로 NAND QC-LDPC 엔진과 부호·구조가 달라 이식성 낮음.

### B. 알고리즘 요약

1. 대상은 폴라 부호 `P(N,k)` (rate 1/2, N=256/2048/32768), 시스템형 인코딩, AWGN, design SNR 0.6dB.
2. 문제: SC/SCL은 직렬 복호로 latency가 크고 SCL은 soft-out 미제공; Arıkan BP는 `log2 N` 스테이지 factor graph라 병렬성·구조 분석이 불리.
3. G의 frozen index 열로 구성한 H는 매우 dense(check degree 최대 N, den 4~16%)라 표준 SPA가 실패.
4. 핵심 기법: encoding factor graph를 bipartite로 재해석하고 CND/VND update 식(1)(2)만으로 노드를 제거하는 pruning 정의.
5. VN을 `VNCH`(채널, Lch), `VNH`(hidden, Lch=0), `VNF`(frozen, Lch=∞)로 구분 — frozen/degree-1 노드가 상수 메시지만 전달함을 이용해 제거.
6. 확장 규칙: degree-1 CN 제거, degree-1 VNCH+degree-2 CN 병합, degree-2 VNH/CN을 feed-forward로 condensing (Algorithm 1이 크기 불변까지 반복).
7. 구현 디테일: pruning 후 H가 1-stage sparse 그래프가 되어 fully parallel SPA로 복호 가능, degree profile `λ(Z)/ρ(Z)` 로 sparsity 유지 확인.
8. 학습 절차 없음 (규칙 기반 그래프 축소만).
9. 결과: H 크기 83~85% 축소; short-to-intermediate N에서 Arıkan BP 대비 BER 손실 무시 가능; 평균 iteration은 증가(Iavg 3.8→10.9)하나 동기화 스텝 `ssyn`은 감소(60.8→21.8)해 latency·메모리 이점.
10. 한계: HW 미설계(시뮬만), gate/throughput 없음, 폴라 부호 전용이라 QC-LDPC 부호설계로 이식 불가.

### C. Prime ECC 관련 모듈 핀포인트

| 논문 요소 | Prime ECC 모듈 | 관련성 |
|---|---|---|
| LDPC-like BP 복호 루프 | [decoder.cpp](../Prime_ECC_3.1_Claude) `LDPC_Decoder()` | BP 복호 자리는 같으나 폴라 유래 pruned graph라 Prime의 고정 QC-LDPC H와 무관 |
| H-matrix pruning / 그래프 축소 | [ecc_top.cpp](../Prime_ECC_3.1_Claude) `Load_PCM()` | H 로드부에 닿으나 Prime은 QC circulant 고정, pruning 대상 아님 |
| edge/노드 선택(그래프 축소) | [GT.cpp](../Prime_ECC_3.1_Claude) `Make_GT_HW()` | Graph Thinning과 개념은 유사하나 폴라 factor graph 전용이라 직접 이식 불가 |

적용 가치: **낮음** — 폴라 부호를 LDPC처럼 복호하려는 기법이라 대상 부호가 다르고, Prime의 고정 QC-LDPC 구조·min-sum HW와 정합되지 않는다.

### D. JSON 블록

```json
{
  "id": "arxiv:1712.08538v5",
  "title": "Sparse Graphs for Belief Propagation Decoding of Polar Codes",
  "year": 2018,
  "venue": "arXiv/cs.IT",
  "portability": "하",
  "nand_relevance": "낮음",
  "target": "both",
  "code_type": "기타",
  "code_rate": 0.5,
  "code_length": "256~32768",
  "soft_quant": "무관",
  "key_contribution": "폴라 부호를 LDPC-like 부호로 보고 encoding factor graph를 pruning해 sparse H로 BP 복호",
  "hw_designed": "X",
  "verification": "시뮬",
  "complexity": "미상",
  "parallelism": "완전병렬",
  "throughput_gbps": null,
  "mem_routing": "언급",
  "correction_gain": "X",
  "improve_region": "N/A",
  "iter_reduction": "X",
  "latency": "개선",
  "recommend": "하",
  "caveat": "폴라 부호 전용 pruning으로 QC-LDPC 부호설계와 무관, 원본 BP 대비 평균 iteration 증가",
  "todo_check": "없음"
}
```
