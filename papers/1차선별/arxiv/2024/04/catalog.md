# arXiv — 2024-04 (1차선별 통과)


## GLDPC-PC Codes: Channel Coding Towards 6G Communications

- **Status**: ✅
- **Reason**: GLDPC-PC(폴라형 컴포넌트 결합 일반화 LDPC) 새 코드 설계 제시 — 바이너리 LDPC 구성 기법으로 이식 가능(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: arxiv:2404.14828v2
- **Type**: preprint
- **Published**: 2024-04-23
- **Authors**: Li Shen, Yongpeng Wu, Yin Xu +3
- **PDF**: https://arxiv.org/pdf/2404.14828v2
- **Abstract**: The sixth generation (6G) wireless communication system will improve the key technical indicators by one to two orders of magnitude, and come with some new features. As a crucial technique to enhance the reliability and efficiency of data transmission, the next-generation channel coding is thus confronted with new challenges in terms of complexity, latency, performance. This article supplies an overview of the potential channel codes for 6G communications. In addition, we explore to develop next-generation channel codes based on lowdensity parity-check (LDPC) and polar frameworks, introducing a concept named generalized LDPC with polar-like component(GLDPC-PC) codes. The codes have exhibited promising error correction performance and manageable complexity, which can be further optimized by specific code design. The opportunities and challenges of GLDPC-PC codes are also discussed.

## Robust Performance Over Changing Intersymbol Interference Channels by Spatial Coupling

- **Status**: ✅
- **Reason**: 공간결합 LDPC로 채널 변동에 강건한 성능, threshold saturation 분석 — 바이너리 SC-LDPC 코드설계 기법 이식 가능(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: arxiv:2404.10367v1
- **Type**: preprint
- **Published**: 2024-04-16
- **Authors**: Mgeni Makambi Mashauri, Alexandre Graell i Amat, Michael Lentmaier
- **PDF**: https://arxiv.org/pdf/2404.10367v1
- **Abstract**: We show that spatially coupled low-density parity-check (LDPC) codes yield robust performance over changing intersymbol interfere (ISI) channels with optimal and suboptimal detectors. We compare the performance with classical LDPC code design which involves optimizing the degree distribution for a given (known) channel. We demonstrate that these classical schemes, despite working very good when designed for a given channel, can perform poorly if the channel is exchanged. With spatially coupled LDPC codes, however, we get performances close to the symmetric information rates with just a single code, without the need to know the channel and adapt to it at the transmitter. We also investigate threshold saturation with the linear minimum mean square error (LMMSE) detector and show that with spatial coupling its performance can get remarkably close to that of an optimal detector for regular LDPC codes.

## On the Universality of Spatially Coupled LDPC Codes Over Intersymbol Interference Channels

- **Status**: ✅
- **Reason**: ISI 채널에서 공간결합 LDPC의 보편성/threshold 분석 — SC-LDPC 코드설계 기법으로 이식 가능(E), 애매하면 in
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: arxiv:2404.10348v1
- **Type**: preprint
- **Published**: 2024-04-16
- **Authors**: Mgeni Makambi Mashauri, Alexandre Graell i Amat, Michael Lentmaier
- **PDF**: https://arxiv.org/pdf/2404.10348v1
- **Abstract**: In this paper, we derive the exact input/output transfer functions of the optimal a-posteriori probability channel detector for a general ISI channel with erasures. Considering three channel impulse responses of different memory as an example, we compute the BP and MAP thresholds for regular spatially coupled LDPC codes with joint iterative detection and decoding. When we compare the results with the thresholds of ISI channels with Gaussian noise we observe an apparent inconsistency, i.e., a channel which performs better with erasures performs worse with AWGN. We show that this anomaly can be resolved by looking at the thresholds from an entropy perspective. We finally show that with spatial coupling we can achieve the symmetric information rates of different ISI channels using the same code.

## Study of Adaptive Reweighted Sparse Belief Propagation Decoders for Polar Codes

- **Status**: ✅
- **Reason**: 적응형 재가중 희소 BP 디코더(AR-SBP), LLR 재가중으로 반복수 감소 — BP 개선 디코더 알고리즘 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: arxiv:2404.04674v1
- **Type**: preprint
- **Published**: 2024-04-06
- **Authors**: R. M. Oliveira, R. C. de Lamare
- **PDF**: https://arxiv.org/pdf/2404.04674v1
- **Abstract**: In this paper, we present an adaptive reweighted sparse belief propagation (AR-SBP) decoder for polar codes. The AR-SBP technique is inspired by decoders that employ the sum-product algorithm for low-density parity-check codes. In particular, the AR-SBP decoding strategy introduces reweighting of the exchanged log-likelihood-ratio in order to refine the message passing, improving the performance of the decoder and reducing the number of required iterations. An analysis of the convergence of AR-SBP is carried out along with a study of the complexity of the analyzed decoders. Numerical examples show that the AR-SBP decoder outperforms existing decoding algorithms for a reduced number of iterations, enabling low-latency applications.

## Density Evolution Analysis of Generalized Low-density Parity-check Codes under a Posteriori Probability Decoder

- **Status**: ✅
- **Reason**: GLDPC 밀도진화/가우시안 근사 개선 및 message-invariant 서브코드 — 바이너리 LDPC 코드설계·분석 기법 이식 가능(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: arxiv:2404.01136v2
- **Type**: preprint
- **Published**: 2024-04-01
- **Authors**: Dongxu Chang, Qingqing Peng, Zhiming Ma +2
- **PDF**: https://arxiv.org/pdf/2404.01136v2
- **Abstract**: In this study, the performance of generalized low-density parity-check (GLDPC) codes under the a posteriori probability (APP) decoder is analyzed. We explore the concentration, symmetry, and monotonicity properties of GLDPC codes under the APP decoder, extending the applicability of density evolution to GLDPC codes. On the binary memoryless symmetric channels, using the BEC and BI-AWGN channels as two examples, we demonstrate that with an appropriate proportion of generalized constraint (GC) nodes, GLDPC codes can reduce the original gap to capacity compared to their original LDPC counterparts. Additionally, on the BI-AWGN channel, we apply and improve the Gaussian approximation algorithm in the density evolution of GLDPC codes. By adopting Gaussian mixture distributions to approximate the message distributions from variable nodes and Gaussian distributions for those from constraint nodes, the precision of the channel parameter threshold can be significantly enhanced while maintaining a low computational complexity similar to that of Gaussian approximations. Furthermore, we identify a class of subcodes that can greatly simplify the performance analysis and practical decoding of GLDPC codes, which we refer to as message-invariant subcodes. Using the aforementioned techniques, our simulation experiments provide empirical evidence that GLDPC codes, when decoded with the APP decoder and equipped with the right fraction of GC nodes, can achieve substantial performance improvements compared to low-density parity-check (LDPC) codes.
