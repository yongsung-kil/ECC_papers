### arxiv:1706.09239v6 - Scattered EXIT Charts for Finite Length LDPC Code Design (2018, arXiv/cs.IT)

| 카테고리 | 값 |
|---|---|
| 이식성 | 하 |
| NAND관련성 | 낮음 |
| 대상 | code-design |
| 부호종류 | irregular |
| 부호rate | 0.5 |
| 부호length | 128~180 |
| 연판정 | 무관 |
| 핵심기여 | 짧은 LDPC의 EXIT 궤적을 확률변수로 보고 2D 히스토그램(S-EXIT)으로 차수분포 미세조정 |
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
| 한계,주의 | 초단(N=128~180) 코드·저rate(0.5) 대상, NAND 고rate QC-LDPC와 무관, HW/디코더 개선 없음 |
| 추가확인 | 고rate·긴 코드에서도 유효한지, QC-LDPC 구조 제약과 병용 가능한지 |

> 총평: 초단 LDPC 차수분포 최적화 시뮬 도구로, NAND 고rate QC-LDPC 부호설계에는 이식성 하.

### B. 알고리즘 요약

1. 대상: AWGN/BEC 채널의 **짧은(N=128~180) irregular LDPC**, rate `R=0.5`, BP 반복복호.
2. 문제: 기존 EXIT 차트는 무한장 가정 기반이라, 짧은 코드의 차수분포 최적화에 부적합(궤적이 "흩어짐"/quasi-chaotic).
3. 가정: 짧은 코드에서 반복간 독립성 가정이 깨지므로 평균 extrinsic 정보 `IE`를 결정함수가 아닌 **확률변수**로 모델링.
4. 핵심기법: 실제 자유주행 반복복호기의 `M`개 EXIT 궤적을 시뮬 → VND/CND 출력점을 2D 히스토그램(S-EXIT 차트)으로 집계.
5. 식: 상호정보 `I(L;X)=1-E[log2(1+e^{-L})]`를 관측 LLR 벡터로 근사(식1) — 임의 LLR 분포에 유효.
6. 여러 H-matrix 랜덤 실현에 대해 평균 → 특정 실현 효과 제거, 앙상블 평균 개선을 봄.
7. 최적화: 해석적 EXIT 곡선을 가이드로 차수분포 `λ(Z), ρ(Z)`를 rate 고정(곡선 사이 면적 유지) 하에 수정.
8. girth-4 제거 등 기본 최적화만 적용(PEG는 미사용, 병용 가능하다고 언급).
9. 결과: 관례적 EXIT 대비 target BER 10^-4에서 **N=128 0.5 dB, N=180 0.6 dB** BER 이득(AWGN); BEC도 이득.
10. 한계: 시뮬 전용, HW 미설계, 초단 저rate 코드 예시뿐, 고차 변경 시 고BER 영역에서 성능 손실 발생 가능.

### C. Prime ECC 관련 모듈 핀포인트

| 논문 요소 | Prime ECC 모듈 | 관련성 |
|---|---|---|
| 차수분포 최적화 결과(부호구조) | `ecc_top.cpp` `Load_PCM()` | 부호 자체는 고정 QC-LDPC라 짧은 irregular 차수분포 산물을 그대로 못 씀 |
| S-EXIT 궤적 시뮬(설계 도구) | 대응 없음 | Prime ECC는 설계 도구가 아닌 bit-exact 시뮬레이터 |
| BP/EXIT 반복복호 개념 | `decoder.cpp` `LDPC_Decoder()` | 교과서 수준 개념 재사용, 이식 신규성 없음 |

적용 가치: **낮음** — 초단·저rate irregular 코드용 설계 도구로, NAND 고rate QC-LDPC(구조 고정)에 직접 이식 여지가 거의 없다.

### D. JSON 블록

```json
{
  "id": "arxiv:1706.09239v6",
  "title": "Scattered EXIT Charts for Finite Length LDPC Code Design",
  "year": 2018,
  "venue": "arXiv/cs.IT",
  "portability": "하",
  "nand_relevance": "낮음",
  "target": "code-design",
  "code_type": "irregular",
  "code_rate": 0.5,
  "code_length": "128~180",
  "soft_quant": "무관",
  "key_contribution": "짧은 LDPC의 EXIT 궤적을 확률변수로 보고 2D 히스토그램(S-EXIT)으로 차수분포 미세조정",
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
  "caveat": "초단(N=128~180) 코드·저rate(0.5) 대상, NAND 고rate QC-LDPC와 무관, HW/디코더 개선 없음",
  "todo_check": "고rate·긴 코드에서도 유효한지, QC-LDPC 구조 제약과 병용 가능한지"
}
```
