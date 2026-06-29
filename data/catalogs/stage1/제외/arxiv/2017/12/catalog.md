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

## Golden codes: quantum LDPC codes built from regular tessellations of hyperbolic 4-manifolds

- **Status**: ❌
- **Reason**: 양자 LDPC(쌍곡 4-manifold 테셀레이션 호몰로지 코드)로 양자 전용 개념에 의존, 고전 바이너리 이식 불가
- **ID**: arxiv:1712.08578v2
- **Type**: preprint
- **Published**: 2017-12-22
- **Authors**: Vivien Londe, Anthony Leverrier
- **PDF**: https://arxiv.org/pdf/1712.08578v2
- **Abstract**: We adapt a construction of Guth and Lubotzky [arXiv:1310.5555] to obtain a family of quantum LDPC codes with non-vanishing rate and minimum distance scaling like $n^{0.1}$ where $n$ is the number of physical qubits. Similarly as in [arXiv:1310.5555], our homological code family stems from hyperbolic 4-manifolds equipped with tessellations. The main novelty of this work is that we consider a regular tessellation consisting of hypercubes. We exploit this strong local structure to design and analyze an efficient decoding algorithm.
