# arXiv — 2019-03 (1차선별 통과)


## High Throughput and Low Cost LDPC Reconciliation for Quantum Key Distribution

- **Status**: ✅
- **Reason**: QKD reconciliation은 원칙 제외이나 quantized LDPC 디코더(개선된 RCBP CN 처리, saturation VN 처리)는 떼어낼 디코더 양자화/HW 기법(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: arxiv:1903.10107v1
- **Type**: preprint
- **Published**: 2019-03-25
- **Authors**: Haokun Mao, Qiong Li, Qi Han +1
- **PDF**: https://arxiv.org/pdf/1903.10107v1
- **Abstract**: Reconciliation is a crucial procedure in post-processing of Quantum Key Distribution (QKD), which is used for correcting the error bits in sifted key strings. Although most studies about reconciliation of QKD focus on how to improve the efficiency, throughput optimizations have become the highlight in high-speed QKD systems. Many researchers adpot high cost GPU implementations to improve the throughput. In this paper, an alternative high throughput and efficiency solution implemented in low cost CPU is proposed. The main contribution of the research is the design of a quantized LDPC decoder including improved RCBP-based check node processing and saturation-oriented variable node processing. Experiment results show that the throughput up to 60Mbps is achieved using the bi-directional approach with reconciliation efficiency approaching to 1.1, which is the optimal combination of throughput and efficiency in Discrete-Variable QKD (DV-QKD). Meanwhile, the performance remains stable when Quantum Bit Error Rate (QBER) varies from 1% to 8%.

## Deep Log-Likelihood Ratio Quantization

- **Status**: ✅
- **Reason**: 딥러닝 기반 LLR 양자화/압축 — NAND LDPC의 LLR 양자화/저장에 직접 이식 가능(A/C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: arxiv:1903.04656v3
- **Type**: preprint
- **Published**: 2019-03-11
- **Authors**: Marius Arvinte, Ahmed H. Tewfik, Sriram Vishwanath
- **PDF**: https://arxiv.org/pdf/1903.04656v3
- **Abstract**: In this work, a deep learning-based method for log-likelihood ratio (LLR) lossy compression and quantization is proposed, with emphasis on a single-input single-output uncorrelated fading communication setting. A deep autoencoder network is trained to compress, quantize and reconstruct the bit log-likelihood ratios corresponding to a single transmitted symbol. Specifically, the encoder maps to a latent space with dimension equal to the number of sufficient statistics required to recover the inputs - equal to three in this case - while the decoder aims to reconstruct a noisy version of the latent representation with the purpose of modeling quantization effects in a differentiable way. Simulation results show that, when applied to a standard rate-1/2 low-density parity-check (LDPC) code, a finite precision compression factor of nearly three times is achieved when storing an entire codeword, with an incurred loss of performance lower than 0.1 dB compared to straightforward scalar quantization of the log-likelihood ratios.

## Decoder-in-the-Loop: Genetic Optimization-based LDPC Code Design

- **Status**: ✅
- **Reason**: 진화알고리즘 decoder-in-the-loop 단길이 바이너리 LDPC 코드 설계 — 유한길이 코드 구성(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: arxiv:1903.03128v3
- **Type**: preprint
- **Published**: 2019-03-07
- **Authors**: Ahmed Elkelesh, Moustafa Ebada, Sebastian Cammerer +2
- **PDF**: https://arxiv.org/pdf/1903.03128v3
- **Abstract**: LDPC code design tools typically rely on asymptotic code behavior and are affected by an unavoidable performance degradation due to model imperfections in the short length regime. We propose an LDPC code design scheme based on an evolutionary algorithm, the Genetic Algorithm (GenAlg), implementing a "decoder-in-the-loop" concept. It inherently takes into consideration the channel, code length and the number of iterations while optimizing the error-rate of the actual decoder hardware architecture. We construct short length LDPC codes (i.e., the parity-check matrix) with error-rate performance comparable to, or even outperforming that of well-designed standardized short length LDPC codes over both AWGN and Rayleigh fading channels. Our proposed algorithm can be used to design LDPC codes with special graph structures (e.g., accumulator-based codes) to facilitate the encoding step, or to satisfy any other practical requirement. Moreover, GenAlg can be used to design LDPC codes with the aim of reducing decoding latency and complexity, leading to coding gains of up to $0.325$ dB and $0.8$ dB at BLER of $10^{-5}$ for both AWGN and Rayleigh fading channels, respectively, when compared to state-of-the-art short LDPC codes. Also, we analyze what can be learned from the resulting codes and, as such, the GenAlg particularly highlights design paradigms of short length LDPC codes (e.g., codes with degree-1 variable nodes obtain very good results).
