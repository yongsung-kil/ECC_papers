# arXiv — 2022-04 (1차선별 통과)


## On Quantum-Assisted LDPC Decoding Augmented with Classical Post-Processing

- **Status**: ✅
- **Reason**: LDPC 디코딩을 QUBO로 정식화 후 어닐링+고전 후처리 디코더 — 바이너리 LDPC 디코딩 알고리즘 기법(C), 양자 전용 부호개념 아님
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: arxiv:2204.09940v1
- **Type**: preprint
- **Published**: 2022-04-21
- **Authors**: Aditya Das Sarma, Utso Majumder, Vishnu Vaidya +3
- **PDF**: https://arxiv.org/pdf/2204.09940v1
- **Abstract**: Utilizing present and futuristic Quantum Computers to solve difficult problems in different domains has become one of the main endeavors at this moment. Of course, in arriving at the requisite solution both quantum and classical computers work in conjunction. With the continued popularity of Low Density Parity Check (LDPC) codes and hence their decoding, this paper looks into the latter as a Quadratic Unconstrained Binary Optimization (QUBO) and utilized D-Wave 2000Q Quantum Annealer to solve it. The outputs from the Annealer are classically post-processed using simple minimum distance decoding to further improve the performance. We evaluated and compared this implementation against the decoding performance obtained using Simulated Annealing (SA) and belief propagation (BP) decoding with classical computers. The results show that implementations of annealing (both simulated and quantum) are superior to BP decoding and suggest that the advantage becomes more prominent as block lengths increase. Reduced Bit Error Rate (BER) and Frame Error Rate (FER) are observed for simulated annealing and quantum annealing, at useful SNR range - a trend that persists for various codeword lengths.

## LDPC codes: comparing cluster graphs to factor graphs

- **Status**: ✅
- **Reason**: LDPC를 cluster graph로 표현해 factor graph BP보다 수렴/정확도 개선 — 이식 가능한 BP 개선 디코더 기법(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: arxiv:2204.06350v2
- **Type**: preprint
- **Published**: 2022-04-13
- **Authors**: J du Toit, J du Preez, R Wolhuter
- **PDF**: https://arxiv.org/pdf/2204.06350v2
- **Abstract**: We present a comparison study between a cluster and factor graph representation of LDPC codes. In probabilistic graphical models, cluster graphs retain useful dependence between random variables during inference, which are advantageous in terms of computational cost, convergence speed, and accuracy of marginal probabilities. This study investigates these benefits in the context of LDPC codes and shows that a cluster graph representation outperforms the traditional factor graph representation.

## LDPC codes: tracking non-stationary channel noise using sequential variational Bayesian estimates

- **Status**: ✅
- **Reason**: cluster graph 기반 순차 베이지안 채널 잡음(SNR) 추정 — NAND retention/노이즈 변동 추적에 이식 가능한 LLR 추정 기법(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: arxiv:2204.07037v2
- **Type**: preprint
- **Published**: 2022-04-13
- **Authors**: J du Toit, J du Preez, R Wolhuter
- **PDF**: https://arxiv.org/pdf/2204.07037v2
- **Abstract**: We present a sequential Bayesian learning method for tracking non-stationary signal-to-noise ratios in LDPC codes using probabilistic graphical models. We represent the LDPC code as a cluster graph using a general purpose cluster graph construction algorithm called the layered trees running intersection property (LTRIP) algorithm. The channel noise estimator is a global Gamma cluster, which we extend to allow for Bayesian tracking of non-stationary noise variation. We evaluate our proposed model on real-world 5G drive test data. Our results show that our model is capable of tracking non-stationary channel noise, which outperforms an LDPC code with a fixed knowledge of the actual average channel noise.
