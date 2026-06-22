# arXiv — 2017-12


## Compute--Forward Multiple Access (CFMA): Practical Code Design

- **Status**: ❌
- **Reason**: CFMA 다중접속용 SPA로 codeword 합 복원 후 modified SPA — MAC 응용 특이, 표준 LDPC 사용, NAND 이식 ECC 기법 없음
- **ID**: arxiv:1712.10293v1
- **Type**: preprint
- **Published**: 2017-12-29
- **Authors**: Erixhen Sula, Jingge Zhu, Adriano Pastore +2
- **PDF**: https://arxiv.org/pdf/1712.10293v1
- **Abstract**: We present a practical strategy that aims to attain rate points on the dominant face of the multiple access channel capacity using a standard low complexity decoder. This technique is built upon recent theoretical developments of Zhu and Gastpar on compute-forward multiple access (CFMA) which achieves the capacity of the multiple access channel using a sequential decoder. We illustrate this strategy with off-the-shelf LDPC codes. In the first stage of decoding, the receiver first recovers a linear combination of the transmitted codewords using the sum-product algorithm (SPA). In the second stage, by using the recovered sum-of-codewords as side information, the receiver recovers one of the two codewords using a modified SPA, ultimately recovering both codewords. The main benefit of recovering the sum-of-codewords instead of the codeword itself is that it allows to attain points on the dominant face of the multiple access channel capacity without the need of rate-splitting or time sharing while maintaining a low complexity in the order of a standard point-to-point decoder. This property is also shown to be crucial for some applications, e.g., interference channels. For all the simulations with single-layer binary codes, our proposed practical strategy is shown to be within \SI{1.7}{\decibel} of the theoretical limits, without explicit optimization on the off-the-self LDPC codes.

## Study of Iterative Detection and Decoding for Large-Scale MIMO Systems with 1-Bit ADCs

- **Status**: ✅
- **Reason**: LDPC error floor 낮추는 quasi-uniform quantizer(스케일링 인자) LLR 양자화 — NAND LLR 양자화에 이식 가능(A/C)
- **ID**: arxiv:1712.08689v1
- **Type**: preprint
- **Published**: 2017-12-23
- **Authors**: Z. Shao, L. Landau, R. de Lamare
- **PDF**: https://arxiv.org/pdf/1712.08689v1
- **Abstract**: We present a novel iterative detection and decoding scheme for the uplink of large-scale multiuser multiple-antenna systems. In order to reduce the receiver's energy consumption and computational complexity, 1-bit analog-to-digital converters are used in the front-end. The performance loss due to the 1-bit quantization can be mitigated by using large-scale antenna arrays. We propose a linear low-resolution-aware minimum mean square error detector for soft multiuser interference mitigation. Moreover, short block length low-density parity-check codes are considered for avoiding high latency. In the channel decoder, a quasi-uniform quantizer with scaling factors is devised to lower the error floor of LDPC codes. Simulations show good performance of the system in terms of bit error rate as compared to prior work.

## Golden codes: quantum LDPC codes built from regular tessellations of hyperbolic 4-manifolds

- **Status**: ❌
- **Reason**: 양자 LDPC(쌍곡 4-manifold 테셀레이션 호몰로지 코드)로 양자 전용 개념에 의존, 고전 바이너리 이식 불가
- **ID**: arxiv:1712.08578v2
- **Type**: preprint
- **Published**: 2017-12-22
- **Authors**: Vivien Londe, Anthony Leverrier
- **PDF**: https://arxiv.org/pdf/1712.08578v2
- **Abstract**: We adapt a construction of Guth and Lubotzky [arXiv:1310.5555] to obtain a family of quantum LDPC codes with non-vanishing rate and minimum distance scaling like $n^{0.1}$ where $n$ is the number of physical qubits. Similarly as in [arXiv:1310.5555], our homological code family stems from hyperbolic 4-manifolds equipped with tessellations. The main novelty of this work is that we consider a regular tessellation consisting of hypercubes. We exploit this strong local structure to design and analyze an efficient decoding algorithm.

## Sparse Graphs for Belief Propagation Decoding of Polar Codes

- **Status**: ✅
- **Reason**: polar를 LDPC-유사 sparse 그래프로 해석, CND/VND pruning으로 sparse BP 디코더 설계 - 부호 비의존 BP 이식 예외 포함(C)
- **ID**: arxiv:1712.08538v5
- **Type**: preprint
- **Published**: 2017-12-22
- **Authors**: Sebastian Cammerer, Moustafa Ebada, Ahmed Elkelesh +1
- **PDF**: https://arxiv.org/pdf/1712.08538v5
- **Abstract**: We describe a novel approach to interpret a polar code as a low-density parity-check (LDPC)-like code with an underlying sparse decoding graph. This sparse graph is based on the encoding factor graph of polar codes and is suitable for conventional belief propagation (BP) decoding. We discuss several pruning techniques based on the check node decoder (CND) and variable node decoder (VND) update equations, significantly reducing the size (i.e., decoding complexity) of the parity-check matrix. As a result, iterative polar decoding can then be conducted on a sparse graph, akin to the traditional well-established LDPC decoding, e.g., using a fully parallel sum-product algorithm (SPA). This facilitates the systematic analysis and design of polar codes using the well-established tools known from analyzing LDPC codes. We show that the proposed iterative polar decoder has a negligible performance loss for short-to-intermediate codelengths compared to Arikan's original BP decoder. Finally, the proposed decoder is shown to benefit from both reduced complexity and reduced memory requirements and, thus, is more suitable for hardware implementations.
