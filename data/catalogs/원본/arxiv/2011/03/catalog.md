# arXiv — 2011-03


## Power Consumption of LDPC Decoders in Software Radio

- **Status**: ✅
- **Reason**: LDPC 디코딩 알고리즘 복잡도/전력 비교 분석 — 디코더 구현 기법 이식 가능(C/D), 애매하면 in
- **ID**: arxiv:1103.5128v1
- **Type**: preprint
- **Published**: 2011-03-26
- **Authors**: Chia-han Lee, Wayne Wolf
- **PDF**: https://arxiv.org/pdf/1103.5128v1
- **Abstract**: LDPC code is a powerful error correcting code and has been applied to many advanced communication systems. The prosperity of software radio has motivated us to investigate the implementation of LDPC decoders on processors. In this paper, we estimate and compare complexity and power consumption of LDPC decoding algorithms running on general purpose processors. Using the estimation results, we show two power control schemes for software radio: SNR-based algorithm diversity and joint transmit power and receiver energy management. Overall, this paper discusses general concerns about using processors as the software radio platform for the implementation of LDPC decoders.

## Scheduled-PEG construction of LDPC codes for Upper-Layer FEC

- **Status**: ❌
- **Reason**: erasure/UL-FEC용 PEG 스케줄링 최적화, 디코딩 오버헤드 지표가 erasure 특이적 — NAND 채널 ECC 기법 아님
- **ID**: arxiv:1103.2690v1
- **Type**: preprint
- **Published**: 2011-03-14
- **Authors**: Lam Pham Sy, Valentin Savin, David Declercq +1
- **PDF**: https://arxiv.org/pdf/1103.2690v1
- **Abstract**: The Progressive Edge Growth (PEG) algorithm is one of the most widely-used method for constructing finite length LDPC codes. In this paper we consider the PEG algorithm together with a scheduling distribution, which specifies the order in which edges are established in the graph. The goal is to find a scheduling distribution that yields "the best" performance in terms of decoding overhead, performance metric specific to erasure codes and widely used for upper-layer forward error correction (UL-FEC). We rigorously formulate this optimization problem, and we show that it can be addressed by using genetic optimization algorithms. We also exhibit PEG codes with optimized scheduling distribution, whose decoding overhead is less than half of the decoding overhead of their classical-PEG counterparts.
