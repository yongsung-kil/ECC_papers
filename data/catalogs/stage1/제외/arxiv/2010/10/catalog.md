# arXiv — 2010-10


## Towards a communication-theoretic understanding of system-level power consumption

- **Status**: ❌
- **Reason**: 메시지패싱 디코딩 전력의 정보이론 하한/송수신 전력 tradeoff — 순수 이론 bound, 디코더/HW/구성으로 안 이어짐, 제외
- **ID**: arxiv:1010.4855v2
- **Type**: preprint
- **Published**: 2010-10-23
- **Authors**: Pulkit Grover, Kristen Ann Woyach, Anant Sahai
- **PDF**: https://arxiv.org/pdf/1010.4855v2
- **Abstract**: Traditional communication theory focuses on minimizing transmit power. However, communication links are increasingly operating at shorter ranges where transmit power can be significantly smaller than the power consumed in decoding. This paper models the required decoding power and investigates the minimization of total system power from two complementary perspectives.   First, an isolated point-to-point link is considered. Using new lower bounds on the complexity of message-passing decoding, lower bounds are derived on decoding power. These bounds show that 1) there is a fundamental tradeoff between transmit and decoding power; 2) unlike the implications of the traditional "waterfall" curve which focuses on transmit power, the total power must diverge to infinity as error probability goes to zero; 3) Regular LDPCs, and not their known capacity-achieving irregular counterparts, can be shown to be power order optimal in some cases; and 4) the optimizing transmit power is bounded away from the Shannon limit.   Second, we consider a collection of links. When systems both generate and face interference, coding allows a system to support a higher density of transmitter-receiver pairs (assuming interference is treated as noise). However, at low densities, uncoded transmission may be more power-efficient in some cases.

## On a Low-Rate TLDPC Code Ensemble and the Necessary Condition on the Linear Minimum Distance for Sparse-Graph Codes

- **Status**: ❌
- **Reason**: TLDPC(터보형 sparse-graph) 저레이트 앙상블의 최소거리 필요조건 이론분석 — 비-LDPC(TLDPC) 앙상블 이론, 떼어낼 바이너리 LDPC 디코더/구성 기법 없음, 제외
- **ID**: arxiv:1010.1911v1
- **Type**: preprint
- **Published**: 2010-10-10
- **Authors**: Iryna Andriyanova, Jean-Pierre Tillich
- **PDF**: https://arxiv.org/pdf/1010.1911v1
- **Abstract**: This paper addresses the issue of design of low-rate sparse-graph codes with linear minimum distance in the blocklength. First, we define a necessary condition which needs to be satisfied when the linear minimum distance is to be ensured. The condition is formulated in terms of degree-1 and degree-2 variable nodes and of low-weight codewords of the underlying code, and it generalizies results known for turbo codes [8] and LDPC codes. Then, we present a new ensemble of low-rate codes, which itself is a subclass of TLDPC codes [4], [5], and which is designed under this necessary condition. The asymptotic analysis of the ensemble shows that its iterative threshold is situated close to the Shannon limit. In addition to the linear minimum distance property, it has a simple structure and enjoys a low decoding complexity and a fast convergence.

## Design and Performance of Rate-compatible Non-Binary LDPC Convolutional Codes

- **Status**: ❌
- **Reason**: 비이진(non-binary GF(q)) LDPC convolutional 부호 설계 — 비이진 LDPC는 제외
- **ID**: arxiv:1010.0060v2
- **Type**: preprint
- **Published**: 2010-10-01
- **Authors**: Hironori Uchikawa, Kenta Kasai, Kohichi Sakaniwa
- **PDF**: https://arxiv.org/pdf/1010.0060v2
- **Abstract**: In this paper, we present a construction method of non-binary low-density parity-check (LDPC) convolutional codes. Our construction method is an extension of Felstroem and Zigangirov construction for non-binary LDPC convolutional codes. The rate-compatibility of the non-binary convolutional code is also discussed. The proposed rate-compatible code is designed from one single mother (2,4)-regular non-binary LDPC convolutional code of rate 1/2. Higher-rate codes are produced by puncturing the mother code and lower-rate codes are produced by multiplicatively repeating the mother code. Simulation results show that non-binary LDPC convolutional codes of rate 1/2 outperform state-of-the-art binary LDPC convolutional codes with comparable constraint bit length. Also the derived low-rate and high-rate non-binary LDPC convolutional codes exhibit good decoding performance without loss of large gap to the Shannon limits.
