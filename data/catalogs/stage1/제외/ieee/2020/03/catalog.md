# IEEE Xplore — 2020-03


## Adaptive Linear Programming Decoding of Nonbinary Linear Codes Over Prime Fields

- **Status**: ❌
- **Reason**: 소수 체 Fp 위 비이진 선형부호의 적응 LP 디코딩 — 비이진(non-binary/GF(q)) 대상이라 제외
- **ID**: ieee:8911339
- **Type**: journal
- **Published**: March 2020
- **Authors**: Eirik Rosnes, Michael Helmling
- **PDF**: https://ieeexplore.ieee.org/document/8911339
- **Abstract**: In this work, we consider adaptive linear programming (ALP) decoding of linear codes over prime fields, i.e., the finite fields Fp of size p where p is a prime, when used over a p-ary input memoryless channel. In particular, we provide a general construction of valid inequalities (using no auxiliary variables) for the codeword polytope (or the convex hull) of the so-called constant-weight embedding of a single parity-check (SPC) code over any prime field. The construction is based on sets of vectors, called building block classes, that are assembled to form the left-hand side of an inequality according to several rules. In the case of almost doubly-symmetric valid classes we prove that the resulting inequalities are all facetdefining, while we conjecture this to be true if and only if the class is valid and symmetric. Valid symmetric classes impose certain symmetry conditions on the elements of the vectors from the class, while valid doubly-symmetric classes impose further technical symmetry conditions. For p = 3, there is only a single valid symmetric class and we prove that the resulting inequalities together with the so-called simplex constraints give a complete and irredundant description of the codeword polytope of the embedded SPC code. For p > 5, we show that there are additional facets beyond those from the proposed construction. As an example, for p =7, we provide additional inequalities that all define facets of the embedded codeword polytope. The resulting overall set of linear (in)equalities is conjectured to be irredundant and complete. Such sets of linear (in)equalities have not appeared in the literature before, have a strong theoretical interest, and we use them to develop an efficient (relaxed) ALP decoder for general (non-SPC) linear codes over prime fields. The key ingredient is an efficient separation algorithm based on the principle of dynamic programming. Furthermore, we construct a decoder for linear codes over arbitrary fields Eq with q = pm and m > 1 by a factor graph representation that reduces to several instances of the case m =1, which results, in general, in a relaxation of the original decoding polytope. Finally, we present an efficient cut-generating algorithm to search for redundant parity-checks to further improve the performance towards maximum-likelihood decoding for short-to-medium block lengths. Numerical experiments confirm that our new decoder is very efficient compared to a static LP decoder for various field sizes, check-node degrees, and block lengths.

## The Need for Structure in Quantum LDPC Codes

- **Status**: ❌
- **Reason**: 양자 LDPC(qLDPC) 존재성/구조에 관한 순수 이론(가중치 분포 bound)으로, 고전 바이너리 디코더·HW·구성 기여 없음
- **ID**: ieee:8908824
- **Type**: journal
- **Published**: March 2020
- **Authors**: Lior Eldar, Maris Ozols, Kevin Thompson
- **PDF**: https://ieeexplore.ieee.org/document/8908824
- **Abstract**: The existence of quantum LDPC codes with minimal distance scaling linearly in the number of qubits is a central open problem in quantum information. Despite years of research good quantum LDPC codes are not known to exist, but at the very least it is known they cannot be defined on very regular topologies, like low-dimensional grids. In this work we establish a complementary result, showing that good quantum CSS codes which are sparsely generated require “structure” in the local terms that constrain the code space so as not to be “too-random” in a well-defined sense. To show this, we prove a weak converse to a theorem of Krasikov and Litsyn on weight distributions of classical codes due to which may be of independent interest: subspaces for which the distribution of weights in the dual space is approximately binomial have very few codewords of low weight, tantamount to having a non-negligible “approximate” minimal distance. While they may not have a large minimal non-zero weight, they still have very few words of low Hamming weight.

## A Pliable Index Coding Approach to Data Shuffling

- **Status**: ❌
- **Reason**: 분산컴퓨팅 데이터 셔플링용 pliable index coding — ECC/LDPC 무관
- **ID**: ieee:8906011
- **Type**: journal
- **Published**: March 2020
- **Authors**: Linqi Song, Christina Fragouli, Tianchu Zhao
- **PDF**: https://ieeexplore.ieee.org/document/8906011
- **Abstract**: A promising research area that has recently emerged, is on how to use index coding to improve the communication efficiency in distributed computing systems, especially for data shuffling in iterative computations. In this paper, we posit that pliable index coding can offer a more efficient framework for data shuffling, as it can better leverage the many possible shuffling choices to reduce the number of transmissions. We theoretically analyze pliable index coding under data shuffling constraints, and design a hierarchical data-shuffling scheme that uses pliable coding as a component. We find benefits up to O(ns/m) over index coding, where ns/m is the average number of workers caching a message, and m, n, and s are the numbers of messages, workers, and cache size, respectively.

## Finite Block-Length Analog Fountain Codes for Ultra-Reliable Low Latency Communications

- **Status**: ❌
- **Reason**: 아날로그 fountain 부호 URLLC — fountain/erasure 계열, 떼어낼 LDPC ECC 기법 없음
- **ID**: ieee:8954789
- **Type**: journal
- **Published**: March 2020
- **Authors**: Ke Zhang, Jian Jiao, Zixuan Huang +2
- **PDF**: https://ieeexplore.ieee.org/document/8954789
- **Abstract**: In this paper, a theoretical framework for the design and evaluation of finite block-length analog fountain codes (AFC) towards ultra-reliable low latency communications (URLLC) is proposed. First, based on the achievable rate analysis and extrinsic information transfer (EXIT) analysis for AFC, we propose a weight adaptive (WA) AFC transmission scheme by introducing a limited feedback link, which can realize the lowest complexity AFC over a wide range SNRs. Further, by combining the conventional EXIT analysis and the dispersion perspective of mutual information, we propose a modified weight selection scheme for short block length WA-AFC (SWA-AFC) scheme. Simulation results show that our SWA-AFC scheme can achieve a superior performance than the existing AFC schemes, and approaching to the Polyansky-Poor-Verdu (PPV) bound.

## Joint Detection and Decoding of Polar Coded 5G Control Channels

- **Status**: ❌
- **Reason**: Polar 부호 5G 제어채널 합동 검출·복호 — LDPC 아니고 떼어낼 LDPC ECC 기법 없음
- **ID**: ieee:8948322
- **Type**: journal
- **Published**: March 2020
- **Authors**: Amin Jalali, Zhi Ding
- **PDF**: https://ieeexplore.ieee.org/document/8948322
- **Abstract**: The recent release of the cellular standard known as 5G New Radio (5G-NR) has adopted polar codes for error protection in the physical downlink control channel (PDCCH). We develop a novel joint detection and decoding algorithm for 5G multiple-input multiple-output (MIMO) transceivers to achieve robustness against practical obstacles including channel state information (CSI) errors, noise, interferences, and pilot contamination. To optimize the performance of PDCCH detection, we incorporate the polar code information during signal detection by transforming the Galois field code constraints into the complex signal field. Specifically, our novel joint linear programming (LP) formulation takes into consideration the transformed polar code constraints. Our proposed detector can also be integrated with effective successive cancellation list (SCL) decoders to deliver superior receiver performance and improve the computational efficiency compared to turbo approach joint detection decoding design. Moreover, similar to 4G-LTE, each active user equipment (UE) must blindly detect its own PDCCH in the downlink search space. We further introduce a metric readily available at the detector that can be used to eliminate most of wrong PDCCH candidates before sending them to the decoder and therefore, improve the computational efficiency of PDCCH blind detection for 5G-NR.

## A Stochastic Computing Architecture for Iterative Estimation

- **Status**: ❌
- **Reason**: 추정 문제용 스토캐스틱 컴퓨팅 아키텍처(Kaczmarz) — LDPC 디코더가 아님, ECC 이식 기법 없음
- **ID**: ieee:8713530
- **Type**: journal
- **Published**: March 2020
- **Authors**: Michael Lunglmayr, Daniel Wiesinger, Werner Haselmayr
- **PDF**: https://ieeexplore.ieee.org/document/8713530
- **Abstract**: Stochastic computing (SC) is a promising candidate for fault-tolerant computing in digital circuits. We present a novel stochastic computing estimation architecture allowing to solve a large group of estimation problems including least squares estimation as well as sparse estimation. This allows utilizing the high fault tolerance of stochastic computing for implementing estimation algorithms. The presented architecture is based on the recently proposed linearized-Bregman-based sparse Kaczmarz algorithm. To realize this architecture, we develop a shrink function in stochastic computing and analytically describe its error probability. We compare the stochastic computing architecture to a fixed-point binary implementation and present bit-true simulation results as well as synthesis results demonstrating the feasibility of the proposed architecture for practical implementation.

## Application of Maximum Entropy Theorem in Channel Estimation

- **Status**: ❌
- **Reason**: 블라인드 채널 추정 기법, LDPC BP는 성능 검증용 부수 언급 — 떼어낼 디코더/코드설계 기여 없음
- **ID**: ieee:10848240
- **Type**: journal
- **Published**: March 2020
- **Authors**: Zhengyu Zhang, Jinming Lou, Mengdi Jin +2
- **PDF**: https://ieeexplore.ieee.org/document/10848240
- **Abstract**: Scholars have been highly concerned with the blind channel estimation of multi-carrier modulation transmission systems, and the decoding process of block codes is usually closely related to channel parameters. Therefore, the accurate estimation of channel parameters is an important method to ensure communication accuracy. According to the transmission characteristics of multi-carrier modulated transmission channels, this paper uses the maximum likelihood theorem and the maximum entropy theorem to put forward a blind channel estimation method based on the proposed received signals. In order to verify the effect of this method, this research utilizes the BP decoding algorithm, which is used in LDPC coding, to calculate the symbol error rate and analyze the estimated effect of the transmission system. The simulation results show that the proposed method can estimate channel parameters effectively, and that the symbol error rate of LDPC decoding is almost similar to that of non-blind channel estimation. This implies that the proposed channel estimation method can effectively improve both channel utilization and transmission efficiency.

## Joint Optimization of Processing Complexity and Rate Allocation through Entropy Tunability for 64-/256-QAM Based Radio Fronthauling with LDPC and PAS-OFDM

- **Status**: ❌
- **Reason**: LDPC는 부수 언급, 무선 fronthaul PAS-OFDM 엔트로피/율 할당이 핵심 — 떼어낼 디코더/HW/코드설계 기법 없음
- **ID**: ieee:9082985
- **Type**: conference
- **Published**: 8-12 March
- **Authors**: Rui Zhang, You-Wei Chen, Shuyi Shen +5
- **PDF**: https://ieeexplore.ieee.org/document/9082985
- **Abstract**: We experimentally demonstrate LDPC coded PAS-OFDM 64-/256-QAM signals in radio fronthauls. Through entropy allocation by adjusting the complexity and signal bandwidth, tunable power margins gain up to 3 dB and relaxed process latency are achieved.

## 50G PON FEC Evaluation with Error Models for Advanced Equalization

- **Status**: ❌
- **Reason**: 50G PON ISI 채널 에러모델(Fritchman Markov)로 LDPC FEC 평가만, 새 디코더/코드설계 기여 없음
- **ID**: ieee:9083155
- **Type**: conference
- **Published**: 8-12 March
- **Authors**: Amitkumar Mahadevan, Doutje van Veen, Noriaki Kaneda +3
- **PDF**: https://ieeexplore.ieee.org/document/9083155
- **Abstract**: Post-equalization bit-errors from ISI-impaired 50G PON transmission experiments are modeled using Fritchman's Markov chain. LDPC FEC evaluation with this error model reveals a 0.3–0.6 dB optical power penalty for equalizing ISI including 83 ps/nm dispersion.

## Analysis of 5G Wireless Systems in FR1 and FR2 Frequency Bands

- **Status**: ❌
- **Reason**: 5G FR1/FR2 빔포밍 성능 분석, LDPC 무관
- **ID**: ieee:9074973
- **Type**: conference
- **Published**: 5-7 March 
- **Authors**: Ravilla Dilli
- **PDF**: https://ieeexplore.ieee.org/document/9074973
- **Abstract**: According to 3GPP, the frequency bands of 5G technologies are occupied at various parts of the frequency spectrum. E.g. mmWave frequencies are used for short-range communications in 5G mobile communications which can provide much higher bandwidth, supports greater data rates and also overcome the effect of path loss using carrier aggregation feature. However, the frequency bands for 5G wireless technology are classified into FR1 and FR2 frequency ranges. FR1 (4.1 GHz to 7.125 GHz) band of frequencies are used for carrying most of the traditional cellular mobile communications traffic, while the FR2 (24.25 GHz to 52.6 GHz) band of frequencies are focused on short-range, high data rate capabilities. A frequency selective wireless channel is converted into a parallel collection of frequency flat sub-channels using “Orthogonal Frequency Division Multiplexing (OFDM)” techniques that improve multipath fading issues and bandwidth efficiency, also reduces the inter-sub carrier interference. The recent wireless communication standards like 802.11x families combine the techniques of multiple-input-multiple-output (MIMO) and OFDM to provide improved data rates. As MIMO uses an array of antennas, and it is possible to achieve a higher signal-to-noise ratio (SNR) using “beamforming” which in turn reduces the bit error rate (BER). This research paper is focused on the performance of hybrid beamforming for single user and multi-user “massive MIMO-OFDM systems” and facilitate to explore various system-level configurations for different channel modellings in FR1 and FR2 bands.

## Systematic Low Density Parity Check Codes with Hard Decision Message Passing Algorithm for Non-binary Symbols

- **Status**: ❌
- **Reason**: 비이진 심볼용 systematic LDPC + hMP(VSD 전단) — 비이진 LDPC 대상, 즉시 제외
- **ID**: ieee:9077506
- **Type**: conference
- **Published**: 4-6 March 
- **Authors**: Usana Tuntoolavest, Visuttha Manthamkarn, Abhishek Maheshwari
- **PDF**: https://ieeexplore.ieee.org/document/9077506
- **Abstract**: This paper proposes the use of systematic LDPC codes for hard decision Message Passing (hMP), which is a predecoder to Vector Symbol Decoding (VSD) for non-binary codes. VSD is a verification-based decoder whose outputs are decoded code words. LDPC are randomly generated and by nature, they are non-systematic codes. Using systematic instead of non-systematic codes allows the decoder to obtain the decoded data directly without a troublesome mapping step. In the simulations, 15 regular parity check matrices H are randomly generated and converted to their systematic forms. Results in a Gilbert-Elliot 2-state fading channel model with 6 different channel conditions show that hMP prefers codes with lower- weight H. For column weight of 9 bits and row weight of 18 bits, systematic H have lower weight after row operation and are better than the non-systematic ones for all channel conditions.

## A LDPC codes based Authentication Scheme

- **Status**: ❌
- **Reason**: LDPC 기반 디지털서명 배치검증 인증 스킴. 채널 ECC 아님, 보안 응용, 떼어낼 ECC 기법 없음
- **ID**: ieee:9079253
- **Type**: conference
- **Published**: 27 Feb.-1 
- **Authors**: Apurva S. Kittur, Swapnil Kauthale, Alwyn R. Pais
- **PDF**: https://ieeexplore.ieee.org/document/9079253
- **Abstract**: Verifying multiple digital signatures in a batch to reduce verification time and computation has caught the interest of many researchers since many years. There are various batch verification schemes proposed for various popular digital signature algorithms such as DSS, RSA, ECDSA and other signature schemes. If there are any bad signatures in the given batch of signatures, then the batch verification test fails but the test does not indicate the location of the bad signature. In literature, there are very few efficient schemes, which locate the index of the bad signature/s in the given batch. These existing schemes perform poorly when the bad signature/s count is unknown or when the entire batch of signatures is faulty. To overcome these disadvantages, we propose a new Low-Density Parity-Check (LDPC) based verification scheme to locate the index of the bad signature/s. Our proposed scheme outperforms the other bad signature identification schemes. The comparative analysis of our scheme with the other schemes is provided. The primary advantage of the scheme is, it removes all the transmission errors in the received batch of signatures.

## Performance of Polar-LDPC Concatenated Coding on AWNG Channel

- **Status**: ❌
- **Reason**: polar-LDPC 연접 부호 AWGN 성능; 새 디코더/구성 기여 없는 표준 연접 시뮬레이션, 떼어낼 LDPC 기법 없음
- **ID**: ieee:9194794
- **Type**: conference
- **Published**: 20-22 Marc
- **Authors**: Yuling Zhang, Rui Feng, Wenwei He
- **PDF**: https://ieeexplore.ieee.org/document/9194794
- **Abstract**: This paper propose a concatenated coding scheme based on polar codes and LDPC codes on AWGN channel. A polar code is served as an outer code and a LDPC code is employed as an inner code. First it proposes the system framework, and introduces the principle of polar codes and LDPC codes respectively, then demonstrates the decoding scheme of the concatenated codes. Finally, it gives the simulation results and some conclusions.

## Improved Optimization Design of Degree Distributions in Fountain Codes

- **Status**: ❌
- **Reason**: fountain/LT 코드 degree distribution 최적화(BEC); fountain/erasure 소스 영역으로 떼어낼 채널 ECC 기법 없음
- **ID**: ieee:9194925
- **Type**: conference
- **Published**: 20-22 Marc
- **Authors**: Shengkai Xu, Dazhuan Xu
- **PDF**: https://ieeexplore.ieee.org/document/9194925
- **Abstract**: Digital fountain codes are designed to realize a reliable transmission of large-scale data and Luby Transform (LT) codes are the first practical digital fountain codes to be realized. Luby discovered that the performance and decoding efficiency are mainly determined by the degree distribution used in LT codes. So this paper focuses on designing good degree distributions for LT codes over the binary erasure channel (BEC). An improved approach to optimize the degree distribution is proposed based on the asymptotic analysis of LT codes. More importantly, the overhead and the desired erasure ratio pair set for the proposed optimization model can be realized in the asymptotic analysis of the optimal degree distribution. Simulation results show that the optimal degree distribution can provide better bit erasure ratio performance especially at low overheads.

## On the Universality of Low-Density Parity-Check Block Codes

- **Status**: ❌
- **Reason**: BEC용 capacity-achieving LDPC 시퀀스의 universality 순수 이론 분석; 디코더/HW/구성으로 안 이어짐
- **ID**: ieee:9086211
- **Type**: conference
- **Published**: 18-20 Marc
- **Authors**: Wei Liu, Rüdiger Urbanke
- **PDF**: https://ieeexplore.ieee.org/document/9086211
- **Abstract**: An important class of modern channel codes is the capacity-achieving sequences of low-density parity-check block codes. Such sequences are usually designed for the binary erasure channel and are decoded by iterative message-passing algorithms. In this paper we investigate the universality of such sequences. We show that many existing capacity-achieving sequences designed for the binary erasure channel do not achieve the same capacity of many other binary-input memoryless output-symmetric channels under belief propagation decoding.

## Coexistence of Orthogonal and Non-orthogonal Multicarrier Signals in Beyond 5G Scenarios

- **Status**: ❌
- **Reason**: 5G OFDM/SEFDM 공존 시나리오; LDPC는 표준 적용 베이스라인 부수 언급, 신규 ECC 기법 없음
- **ID**: ieee:9083780
- **Type**: conference
- **Published**: 17-20 Marc
- **Authors**: Xinyue Liu, Tongyang Xu, Izzat Darwazeh
- **PDF**: https://ieeexplore.ieee.org/document/9083780
- **Abstract**: Optimum operation of future mobile communication systems requires more flexible signalling mechanisms for radio access. For flexible heterogeneous signalling implementation, this work discusses coexistence scenarios of orthogonal and nonorthogonal multicarrier signals, specifically considering orthogonal frequency division multiplexing (OFDM) and spectrally efficient FDM (SEFDM) signals. Three main scenarios of the coexisting signalling are addressed under 5G new radio (5G NR) numerology with varying subcarrier spacing. Using numerical simulations, this work reports performance results of systems operating under the studied coexistence scenarios assuming uncoded and coded signals. Results reveal that systems employing SEFDM and OFDM result in some BER degradation when uncoded signals are used and also show that when applying low-density parity-check (LDPC) to the transmitted signals, the coexistence effects are mitigated and the block error rate (BLER) for both orthogonal and non-orthogonal signals suffers only slight degradation.

## Iris Recognition System Implementation Improved by QC-LDPC codes

- **Status**: ❌
- **Reason**: 홍채인식에 표준 WiFi QC-LDPC 인코더/디코더 그대로 적용, 새 기여 없음
- **ID**: ieee:9081256
- **Type**: conference
- **Published**: 10-12 Marc
- **Authors**: Longyu Ma, Chiu Wing Sham
- **PDF**: https://ieeexplore.ieee.org/document/9081256
- **Abstract**: In this paper, an iris recognition system is implemented with certain LDPC codes which have the ability to correct intrinsic fuzziness. The whole architecture is thoroughly designed from scratch onto an SoC-FPGA based platform, namely Intel DE-10 nano Cyclone V SOC evaluation board. A WiFi standard-compatible QC-LDPC encoder and decoder are adopted to enable the error-correction ability. The result shows the system with LDPC codes leads to less hamming distance, which means the proposed system obtains a better true acceptance rate.

## LifeTech 2020 Abstracts

- **Status**: ❌
- **Reason**: 컨퍼런스 초록 모음, 기술 기여 없음
- **ID**: ieee:9081062
- **Type**: conference
- **Published**: 10-12 Marc
- **Authors**: 
- **PDF**: https://ieeexplore.ieee.org/document/9081062
- **Abstract**: Presents abstracts for the articles comprising the conference proceedings.

## Lightweight Key Encapsulation Using LDPC Codes on FPGAs

- **Status**: ❌
- **Reason**: LEDAkem QC-LDPC 키 캡슐화(보안/PQC), 채널 ECC 아닌 암호 응용; FPGA 회전 기법은 코드별 디코더 아님 — 보안 원칙 제외
- **ID**: ieee:8877876
- **Type**: journal
- **Published**: 1 March 20
- **Authors**: Jingwei Hu, Marco Baldi, Paolo Santini +3
- **PDF**: https://ieeexplore.ieee.org/document/8877876
- **Abstract**: In this paper, we present a lightweight hardware design for a recently proposed quantum-safe key encapsulation mechanism based on QC-LDPC codes called LEDAkem, which has been admitted as a round-2 candidate to the NIST post-quantum standardization project. Existing implementations focus on high speed while few of them take into account area or power efficiency, which are particularly decisive for low-cost or power constrained IoT applications. The solution we propose aims at maximizing the metric of area efficiency by rotating the QC-LDPC code representations amongst the block RAMs in digit level. Moreover, optimized parallelized computing techniques, lazy accumulation and block partition are exploited to improve key decapsulation in terms of area and timing efficiency. We show for instance that our area-optimized implementation for 128-bit security requires 6.82 x 105 cycles and 2.26 x 106 cycles to encapsulate and decapsulate a shared secret, respectively. The area-optimized design uses only 39 slices (3 percent of the available logic) and 809 slices (39 percent of the available logic) for key encapsulation and key decapsulation respectively, on a small-size low-end Xilinx Spartan-6 FPGA.
