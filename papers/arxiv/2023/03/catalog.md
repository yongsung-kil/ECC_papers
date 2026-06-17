# arXiv — 2023-03


## Hierarchical memories: Simulating quantum LDPC codes with local gates

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: arxiv:2303.04798v2
- **Type**: preprint
- **Published**: 2023-03-08
- **Authors**: Christopher A. Pattison, Anirudh Krishna, John Preskill
- **PDF**: https://arxiv.org/pdf/2303.04798v2
- **Abstract**: Constant-rate low-density parity-check (LDPC) codes are promising candidates for constructing efficient fault-tolerant quantum memories. However, if physical gates are subject to geometric-locality constraints, it becomes challenging to realize these codes. In this paper, we construct a new family of $[[N,K,D]]$ codes, referred to as hierarchical codes, that encode a number of logical qubits $K = Ω(N/\log(N)^2)$. The N-th element of this code family is obtained by concatenating a constant-rate quantum LDPC code with a surface code; nearest-neighbor gates in two dimensions are sufficient to implement the corresponding syndrome-extraction circuit and achieve a threshold. Below threshold the logical failure rate vanishes superpolynomially as a function of the distance $D(N)$. We present a bilayer architecture for implementing the syndrome-extraction circuit, and estimate the logical failure rate for this architecture. Under conservative assumptions, we find that the hierarchical code outperforms the basic encoding where all logical qubits are encoded in the surface code.

## Mapper Side Geometric Shaping for QAM Constellations in 5G MIMO Wireless Channel with Realistic LDPC Codes

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: arxiv:2303.02605v1
- **Type**: preprint
- **Published**: 2023-03-05
- **Authors**: Daniil Yudakov, Dmitrii Kolosov, Evgeny Bobrov
- **PDF**: https://arxiv.org/pdf/2303.02605v1
- **Abstract**: In wireless communication systems, there are many stages for signal transmission. Among them, mapping and demapping convert a sequence of bits into a sequence of complex numbers and vice versa. This operation is performed by a system of constellations~ -- by a set of labeled points on the complex plane. Usually, the geometry of the constellation is fixed, and constellation points are uniformly spaced, e.g., the same quadrature amplitude modulation (QAM) is used in a wide range of signal-to-noise ratio (SNR). By eliminating the uniformity of constellations, it is possible to achieve greater values of capacity. Due to the current standard restrictions, it is difficult to change the constellation both on the mapper or demapper side. In this case, one can optimize the constellation only on the mapper or the demapper side using original methodology. By the numerical calculating of capacity, we show that the optimal geometric constellation depends on SNR. Optimization is carried out by maximizing mutual information (MI). The MI function describes the amount of information being transmitted through the channel with the optimal encoding. To prove the effectiveness of this approach we provide numerical experiments in the modern physical level Sionna simulator using the realistic LDPC codes and the MIMO 5G OFDM channels.

## On Probability Shaping for 5G MIMO Wireless Channel with Realistic LDPC Codes

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: arxiv:2303.02598v3
- **Type**: preprint
- **Published**: 2023-03-05
- **Authors**: Evgeny Bobrov, Adyan Dordzhiev
- **PDF**: https://arxiv.org/pdf/2303.02598v3
- **Abstract**: Probability Shaping (PS) is a method to improve a Modulation and Coding Scheme (MCS) in order to increase reliability of data transmission. It is already implemented in some modern radio broadcasting and optic systems, but not yet in wireless communication systems. Here we adapt PS for the 5G wireless protocol, namely, for relatively small transport block size, strict complexity requirements and actual low-density parity-check codes (LDPC). We support our proposal by a numerical experiment results in Sionna simulator, showing 0.6 dB gain of PS based MCS versus commonly used MCS.
