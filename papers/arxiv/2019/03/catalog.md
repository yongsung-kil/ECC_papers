# arXiv — 2019-03


## High Throughput and Low Cost LDPC Reconciliation for Quantum Key Distribution

- **Status**: 미선별
- **Reason**: N/A
- **ID**: arxiv:1903.10107v1
- **Type**: preprint
- **Published**: 2019-03-25
- **Authors**: Haokun Mao, Qiong Li, Qi Han +1
- **PDF**: https://arxiv.org/pdf/1903.10107v1
- **Abstract**: Reconciliation is a crucial procedure in post-processing of Quantum Key Distribution (QKD), which is used for correcting the error bits in sifted key strings. Although most studies about reconciliation of QKD focus on how to improve the efficiency, throughput optimizations have become the highlight in high-speed QKD systems. Many researchers adpot high cost GPU implementations to improve the throughput. In this paper, an alternative high throughput and efficiency solution implemented in low cost CPU is proposed. The main contribution of the research is the design of a quantized LDPC decoder including improved RCBP-based check node processing and saturation-oriented variable node processing. Experiment results show that the throughput up to 60Mbps is achieved using the bi-directional approach with reconciliation efficiency approaching to 1.1, which is the optimal combination of throughput and efficiency in Discrete-Variable QKD (DV-QKD). Meanwhile, the performance remains stable when Quantum Bit Error Rate (QBER) varies from 1% to 8%.

## Modified belief propagation decoders for quantum low-density parity-check codes

- **Status**: 미선별
- **Reason**: N/A
- **ID**: arxiv:1903.07404v2
- **Type**: preprint
- **Published**: 2019-03-18
- **Authors**: Alex Rigby, JC Olivier, Peter Jarvis
- **PDF**: https://arxiv.org/pdf/1903.07404v2
- **Abstract**: Quantum low-density parity-check codes can be decoded using a syndrome based $\mathrm{GF}(4)$ belief propagation decoder. However, the performance of this decoder is limited both by unavoidable $4$-cycles in the code's factor graph and the degenerate nature of quantum errors. For the subclass of CSS codes, the number of $4$-cycles can be reduced by breaking an error into an $X$ and $Z$ component and decoding each with an individual $\mathrm{GF}(2)$ based decoder. However, this comes at the expense of ignoring potential correlations between these two error components. We present a number of modified belief propagation decoders that address these issues. We propose a $\mathrm{GF}(2)$ based decoder for CSS codes that reintroduces error correlations by reattempting decoding with adjusted error probabilities. We also propose the use of an augmented decoder, which has previously been suggested for classical binary low-density parity-check codes. This decoder iteratively reattempts decoding on factor graphs that have a subset of their check nodes duplicated. The augmented decoder can be based on a $\mathrm{GF}(4)$ decoder for any code, a $\mathrm{GF}(2)$ decoder for CSS code, or even a supernode decoder for a dual-containing CSS code. For CSS codes, we further propose a $\mathrm{GF}(2)$ based decoder that combines the augmented decoder with error probability adjustment. We demonstrate the performance of these new decoders on a range of different codes, showing that they perform favorably compared to other decoders presented in literature.

## Deep Log-Likelihood Ratio Quantization

- **Status**: 미선별
- **Reason**: N/A
- **ID**: arxiv:1903.04656v3
- **Type**: preprint
- **Published**: 2019-03-11
- **Authors**: Marius Arvinte, Ahmed H. Tewfik, Sriram Vishwanath
- **PDF**: https://arxiv.org/pdf/1903.04656v3
- **Abstract**: In this work, a deep learning-based method for log-likelihood ratio (LLR) lossy compression and quantization is proposed, with emphasis on a single-input single-output uncorrelated fading communication setting. A deep autoencoder network is trained to compress, quantize and reconstruct the bit log-likelihood ratios corresponding to a single transmitted symbol. Specifically, the encoder maps to a latent space with dimension equal to the number of sufficient statistics required to recover the inputs - equal to three in this case - while the decoder aims to reconstruct a noisy version of the latent representation with the purpose of modeling quantization effects in a differentiable way. Simulation results show that, when applied to a standard rate-1/2 low-density parity-check (LDPC) code, a finite precision compression factor of nearly three times is achieved when storing an entire codeword, with an incurred loss of performance lower than 0.1 dB compared to straightforward scalar quantization of the log-likelihood ratios.

## Decoder-in-the-Loop: Genetic Optimization-based LDPC Code Design

- **Status**: 미선별
- **Reason**: N/A
- **ID**: arxiv:1903.03128v3
- **Type**: preprint
- **Published**: 2019-03-07
- **Authors**: Ahmed Elkelesh, Moustafa Ebada, Sebastian Cammerer +2
- **PDF**: https://arxiv.org/pdf/1903.03128v3
- **Abstract**: LDPC code design tools typically rely on asymptotic code behavior and are affected by an unavoidable performance degradation due to model imperfections in the short length regime. We propose an LDPC code design scheme based on an evolutionary algorithm, the Genetic Algorithm (GenAlg), implementing a "decoder-in-the-loop" concept. It inherently takes into consideration the channel, code length and the number of iterations while optimizing the error-rate of the actual decoder hardware architecture. We construct short length LDPC codes (i.e., the parity-check matrix) with error-rate performance comparable to, or even outperforming that of well-designed standardized short length LDPC codes over both AWGN and Rayleigh fading channels. Our proposed algorithm can be used to design LDPC codes with special graph structures (e.g., accumulator-based codes) to facilitate the encoding step, or to satisfy any other practical requirement. Moreover, GenAlg can be used to design LDPC codes with the aim of reducing decoding latency and complexity, leading to coding gains of up to $0.325$ dB and $0.8$ dB at BLER of $10^{-5}$ for both AWGN and Rayleigh fading channels, respectively, when compared to state-of-the-art short LDPC codes. Also, we analyze what can be learned from the resulting codes and, as such, the GenAlg particularly highlights design paradigms of short length LDPC codes (e.g., codes with degree-1 variable nodes obtain very good results).

## Outage-Limit-Approaching Protograph LDPC Codes for Slow-Fading Wireless Communications

- **Status**: 미선별
- **Reason**: N/A
- **ID**: arxiv:1903.01223v2
- **Type**: preprint
- **Published**: 2019-03-04
- **Authors**: Yi Fang, Pingping Chen, Guofa Cai +3
- **PDF**: https://arxiv.org/pdf/1903.01223v2
- **Abstract**: Block-fading (BF) channel, also known as slow-fading channel, is a type of simple and practical channel model that can characterize the primary feature of a number of wireless-communication applications with low to moderate mobility. Although the BF channel has received significant research attention in the past twenty years, designing low-complexity outage-limit-approaching error-correction codes (ECCs) is still a challenging issue. For this reason, a novel family of protograph low-density parity-check (LDPC) codes, called root-protograph (RP) LDPC codes, has been conceived recently. The RP codes can not only realize linear-complexity encoding and high-speed decoding with the help of a quasi-cyclic (QC) structure, but also achieve near-outage-limit performance in a variety of BF scenarios. In this article, we briefly review the design guidelines of such protograph codes with the aim of inspiring further research activities in this area.
