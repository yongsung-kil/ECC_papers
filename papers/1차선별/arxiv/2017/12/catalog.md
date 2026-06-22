# arXiv — 2017-12 (1차선별 통과)


## Study of Iterative Detection and Decoding for Large-Scale MIMO Systems with 1-Bit ADCs

- **Status**: ✅
- **Reason**: LDPC error floor 낮추는 quasi-uniform quantizer(스케일링 인자) LLR 양자화 — NAND LLR 양자화에 이식 가능(A/C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: arxiv:1712.08689v1
- **Type**: preprint
- **Published**: 2017-12-23
- **Authors**: Z. Shao, L. Landau, R. de Lamare
- **PDF**: https://arxiv.org/pdf/1712.08689v1
- **Abstract**: We present a novel iterative detection and decoding scheme for the uplink of large-scale multiuser multiple-antenna systems. In order to reduce the receiver's energy consumption and computational complexity, 1-bit analog-to-digital converters are used in the front-end. The performance loss due to the 1-bit quantization can be mitigated by using large-scale antenna arrays. We propose a linear low-resolution-aware minimum mean square error detector for soft multiuser interference mitigation. Moreover, short block length low-density parity-check codes are considered for avoiding high latency. In the channel decoder, a quasi-uniform quantizer with scaling factors is devised to lower the error floor of LDPC codes. Simulations show good performance of the system in terms of bit error rate as compared to prior work.

## Sparse Graphs for Belief Propagation Decoding of Polar Codes

- **Status**: ✅
- **Reason**: polar를 LDPC-유사 sparse 그래프로 해석, CND/VND pruning으로 sparse BP 디코더 설계 - 부호 비의존 BP 이식 예외 포함(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: arxiv:1712.08538v5
- **Type**: preprint
- **Published**: 2017-12-22
- **Authors**: Sebastian Cammerer, Moustafa Ebada, Ahmed Elkelesh +1
- **PDF**: https://arxiv.org/pdf/1712.08538v5
- **Abstract**: We describe a novel approach to interpret a polar code as a low-density parity-check (LDPC)-like code with an underlying sparse decoding graph. This sparse graph is based on the encoding factor graph of polar codes and is suitable for conventional belief propagation (BP) decoding. We discuss several pruning techniques based on the check node decoder (CND) and variable node decoder (VND) update equations, significantly reducing the size (i.e., decoding complexity) of the parity-check matrix. As a result, iterative polar decoding can then be conducted on a sparse graph, akin to the traditional well-established LDPC decoding, e.g., using a fully parallel sum-product algorithm (SPA). This facilitates the systematic analysis and design of polar codes using the well-established tools known from analyzing LDPC codes. We show that the proposed iterative polar decoder has a negligible performance loss for short-to-intermediate codelengths compared to Arikan's original BP decoder. Finally, the proposed decoder is shown to benefit from both reduced complexity and reduced memory requirements and, thus, is more suitable for hardware implementations.
