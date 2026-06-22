# IEEE Xplore — 2023-09 (1차선별 통과)


## High Throughput and Hardware Efficient Hybrid LDPC Decoder Using Bit-Serial Stochastic Updating

- **Status**: ✅
- **Reason**: bit-serial stochastic updating 하이브리드 BP/stochastic LDPC 디코더 신규 알고리즘+HW — 디코더(C)/HW(D) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10143986
- **Type**: journal
- **Published**: Sept. 2023
- **Authors**: Shuai Hu, Kaining Han, Yubin Zhu +3
- **PDF**: https://ieeexplore.ieee.org/document/10143986
- **Abstract**: Hybrid low-density parity-check (LDPC) decoding combines conventional Belief-Propagation (BP) algorithm with stochastic decoding to achieve high performance and low complexity simultaneously. However, lossy and inefficient stochastic-to-binary (S2B) conversion brings extra performance degradation and decoding latency. In this paper, a bit-serial stochastic updating based hybrid decoding (BSSU-HD) is proposed, which employs fully correlated stochastic (FCS) check nodes (CNs) and probability tracers assisted variable nodes (VNs) to accomplish accurate and efficient S2B conversion. Two strategies, including random source selection and tracing speed switching, are proposed to further improve performance and convergence. A BSSU LDPC decoder for IEEE 802.3an is designed in a 65-nm CMOS process, which occupies 4.6 mm2 silicon area and achieves a throughput of 200.8 Gb/s at  $E_{b}/N_{0} = 4.4$  dB with 500 MHz clock frequency from a 1.2 V supply voltage. The power and energy efficiency are 2.933 W and 14.61 pJ/bit, respectively. To the best of our known, it achieves the best decoding performance, the highest throughput and hardware efficiency among state-of-the-art IEEE 802.3an LDPC decoders. We also verify that the BSSU-HD can achieve better performance for multi-rate 5th generation (5G) New Ratio (NR) LDPC codes than conventional algorithm, which greatly extends the application of the stochastic decoding.

## Cyclic Partial Geometries and Their Associated LDPC and Constant-Weight Codes

- **Status**: ✅
- **Reason**: 순환 부분기하 기반 새 QC/cyclic LDPC 코드 구성, error-floor 없이 BP 수렴 우수 — 바이너리 코드설계(E) 신규 기여
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10129876
- **Type**: journal
- **Published**: Sept. 2023
- **Authors**: Juane Li, Yi Gong, Xin Xiao +2
- **PDF**: https://ieeexplore.ieee.org/document/10129876
- **Abstract**: Partial geometries form an interesting branch in combinatorial mathematics, and recently they have been shown to be very effective in the construction of LDPC codes with distinct geometric and algebraic structures. This paper presents three specific cyclic classes of partial geometries. Based on these three classes of partial geometries, three classes of LDPC codes and three classes of constant-weight codes are constructed. Codes in these two categories are either cyclic or quasi-cyclic. Designs and constructions of these codes are straightforward and flexible without a need for extensive computer search. It is shown that long high-rate LDPC codes constructed based on the three classes of cyclic partial geometries perform well over the additive white Gaussian noise channel (AWGNC) with iterative decoding algorithm based on belief propagation. They can achieve low error-rates without visible error-floor and their decoding converges rapidly. These LDPC codes also perform well over the binary erasure channel (BEC) and are very effective in correcting phased-bursts of erasures. Based on cyclic partial geometries, a special type of constant-weight codes, called balanced codes, can be constructed. The constant-weight codes constructed based on partial geometries are either optimal or nearly optimal.

## Sparsity-Aware Medium-Density Parity-Check Decoder for McEliece Cryptosystems

- **Status**: ✅
- **Reason**: MDPC 디코더 희소성 활용 저지연·저전력 HW 설계 — bit-flipping 계열 디코더 latency/메모리 최적화 기법이 LDPC HW(D)로 이식 가능, 애매하여 보존
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:10092892
- **Type**: journal
- **Published**: Sept. 2023
- **Authors**: Xinmiao Zhang, Zhenshan Xie
- **PDF**: https://ieeexplore.ieee.org/document/10092892
- **Abstract**: McEliece cryptosystem based on medium-density parity-check (MDPC) codes is one of the finalists for the post-quantum cryptography standard. Although decoder design for low-density parity-check (LDPC) codes used for digital communications is well-investigated, the design of MDPC decoders faces many new challenges due to the different structure in the parity-check matrix. Even though the parity-check matrices of MDPC codes have relatively higher density, they are still very sparse. Previous decoder designs did not explore such sparsity and derive the columns of the parity check matrix one after the other by cyclic shifting. This brief proposes a low-complexity MDPC decoder design by exploiting the sparsity of the parity-check matrix. The processing corresponding to zero segments of each parity check matrix column is skipped to substantially reduce the latency. Moreover, the columns are processed in a novel non-consecutive order to significantly reduce the number of memory writes for deriving all the columns and accordingly the power consumption. For an example MDPC code considered for the standard, the proposed design can reduce both the decoding latency and the number of memory writes by 70% with 35% area saving.

## Analysis of Binary and Ternary Message Passing Decoding for Generalized LDPC Codes

- **Status**: ✅
- **Reason**: GLDPC 바이너리/터너리 메시지패싱 디코딩 DE 분석 + 양자화 스케일링 계수. 이식 가능 디코더 기법(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10173581
- **Type**: journal
- **Published**: Sept. 2023
- **Authors**: Emna Ben Yacoub, Gianluigi Liva
- **PDF**: https://ieeexplore.ieee.org/document/10173581
- **Abstract**: The performance of generalized low-density parity-check (GLDPC) codes under binary and ternary message passing decoding (BMP/TMP) is analyzed from a density evolution (DE) perspective. At the check nodes, two types of local decoders are considered, namely optimum a-posteriori probability (APP) soft-input soft-output decoding, and bounded distance decoding (BDD). The purpose is to shed light on the performance loss incurred by BMP and TMP decoding of GLDPC codes with respect to unquantized belief propagation (BP) decoding. A DE analysis for irregular code ensembles is developed for all the algorithms, which allows obtaining the scaling coefficients needed for the variable node operation of BMP and TMP decoders. The stability analysis for the case of bounded distance decoding at the check nodes is derived. The asymptotic DE analysis is confirmed by the finite-length simulation results. For the codes analyzed in this paper, which rely on extended Hamming component codes, the study shows that under BMP decoding, BDD at the check nodes yields almost the same performance as optimum APP check node processing, while under TMP decoding the loss incurred by the sub-optimum BDD at check nodes is within 0.7 dB, when compared with APP decoding at the check nodes.

## Efficient Protection of FPGA Implemented LDPC Decoders Against Single Event Upsets (SEUs) on Configuration Memories

- **Status**: ✅
- **Reason**: FPGA Min-Sum LDPC 디코더 SEU 보호(DWC) HW 기법 — parity-check sum 분포 기반 결함검출, HW 신뢰성 기법(D) 이식 가능
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:10143330
- **Type**: journal
- **Published**: Sept. 2023
- **Authors**: Zhen Gao, Yinghao Cheng, Qiang Liu +2
- **PDF**: https://ieeexplore.ieee.org/document/10143330
- **Abstract**: Low Density Parity Check (LDPC) codes are used in 5G systems for traffic channels due to their excellent error correction capability for long sequences, and the Min-Sum algorithm is widely applied in practical implementations of LDPC decoders due to its low complexity. If the decoder is implemented on a SRAM-based field-programmable gate array (SRAM-FPGA), the radiation-induced single-event upsets (SEUs) can affect the operation of the LDPC decoder by corrupting the configuration memory, which can change the circuit functionality and will not be corrected unless the FPGA is reconfigured. Therefore, protection of LDPC decoders with low overhead is an important problem, especially for resource-limited on-board space systems. In this paper, an efficient Duplicate With Comparison (DWC) protection scheme is proposed based on the different distribution of the parity check sum of the LDPC decoder in the error-free case and the faulty case. In particular, the check sum accumulation number and threshold are optimized to achieve high detection probability with short delay. FPGA based implementation and hardware fault injection experiments are conducted to evaluate the performance of the proposed schemes. Experimental results show that, the effect of SEUs on the LDPC decoder can be completely eliminated by the proposed scheme with 2 times computational overhead and 1.69 times power consumption overhead compared to the unprotected decoder.

## Performance Comparison of Channel Coding Methods for Optical Satellite Data Relay System

- **Status**: ✅
- **Reason**: DVB-S2 LDPC 대상 LLR 보정 기법 제안 — 이식 가능 LLR 기법 가능성, Phase3 재검토
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10294033
- **Type**: conference
- **Published**: 5-8 Sept. 
- **Authors**: Eiji Okamoto, Yuma Yamashita, Yohei Satoh +3
- **PDF**: https://ieeexplore.ieee.org/document/10294033
- **Abstract**: The demand for high-capacity satellite communications has continuously increased, owing to the need to enhance the performance of sensors on earth observation satellites. One of the challenges is to realize a high-capacity return link from user satellites to ground stations. The Japan Aerospace Exploration Agency (JAXA) developed an optical intersatellite communication system "LUCAS" in 2020. JAXA aims to demonstrate a 1.8 Gbps data relay between a user satellite in low earth orbit and a ground station. Currently, the realization of a next-generation optical data relay system capable of even higher-speed communications is being studied. However, a detailed performance comparison of channel coding methods for optical data relay systems has not been conducted to enable high-speed communication within the limits of realistic computation power for installation in data relay satellites using optical intersatellite communication. Therefore, in this paper, we conduct numerical simulations to evaluate the characteristics of communication channel coding technologies, such as polar, low-density parity check codes, and Digital Video Broadcasting- Satellite-Second Generation (DVB-S2) channel codes, when applied to optical data relay satellite systems. The results of the simulations indicate that the performance of DVB-S2 codes is relatively good. Furthermore, a simple log-likelihood ratio correction method for DVB-S2 is proposed and shown to be effective.

## Using Partial Orthomorphisms to Construct Short Quasi-Cyclic LDPC Codes with Girth at Least 6

- **Status**: ✅
- **Reason**: partial orthomorphism으로 girth>=6 short QC-LDPC 구성, 최소 lifting degree 결정 — 새 코드설계 기법(E), 바이너리
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10273465
- **Type**: conference
- **Published**: 4-8 Sept. 
- **Authors**: Henry Chimal-Dzul, Anthony Gómez-Fonseca
- **PDF**: https://ieeexplore.ieee.org/document/10273465
- **Abstract**: Since the publication of Fossorier’s work on the necessary and sufficient conditions for a $(k,\ell)$-regular QC-LDPC code to have a desired girth g, many researchers have been attracted to the problem of determining the smallest lifting degree $N_{\text{min}}$ for which such a code exists. For some values of $ k,\ell$ and g, either an explicit algebraic formula for $N_{\min}$ has been given or its value has been determined by exhaustive computer search. For most cases, however, only lower bounds are known. In this paper, we translate the problem of determining $N_{\min}$ into one about the existence of mutually adjacent partial orthomorphisms of $\mathbb{Z}_{N}$ with certain deficit d, and determine its value for certain parameters. These particular orthomorphisms can also be used to determine, for a fixed $\ell$ and N, the maximum number $k_{\max}$ for which there exists a $(k_{\max},\ell)$-regular QC-LDPC code with girth g.

## Superposition Construction of Globally-Coupled LDPC Codes for MIMO Communication

- **Status**: ✅
- **Reason**: GC-LDPC 신규 superposition 구성 + 병렬 분할 TPD 디코딩 — 코드설계(E)·디코더(C) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10273556
- **Type**: conference
- **Published**: 4-8 Sept. 
- **Authors**: Jian Fang, Baoming Bai, Ruimin Yuan +3
- **PDF**: https://ieeexplore.ieee.org/document/10273556
- **Abstract**: This paper presents a globally-coupled low-density parity-check (GC-LDPC) coding scheme with high throughput for multiple-input and multiple-output transmission. To design rate-compatible length-scalable GC-LDPC codes, a novel superposition construction of GC-LDPC codes is proposed. To reduce the complexity of the two-phase decoding (TPD) method, we propose a modified TPD method based on partial check matrices. Numerical results show that our coding scheme can divide the decoding of a large code into 4 and 5 parallel decodings of short codes and increase throughput by 4 and 5 times at the frame error rate of $10^{-5}$ for code rates of 0.49 and 0.66, respectively. Besides, the modified TPD method reduces the global decoding complexity to almost 1/4 and 1/5 of the TPD method at the frame error rate of $10^{-5}$ for code rates of 0.49 and 0.66, respectively.

## Gradient Flow Decoding for LDPC Codes

- **Status**: ✅
- **Reason**: GDBF 기반 gradient flow 아날로그 디코딩 — 이식 가능한 새 디코더 알고리즘(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10273536
- **Type**: conference
- **Published**: 4-8 Sept. 
- **Authors**: Tadashi Wadayama, Kensho Nakajima, Ayano Nakai-Kasai
- **PDF**: https://ieeexplore.ieee.org/document/10273536
- **Abstract**: The power consumption of the integrated circuit is becoming a significant burden, particularly for large-scale signal processing tasks requiring high throughput. The decoding process of LDPC codes is such a heavy signal processing task that demands power efficiency and higher decoding throughput. A promising approach to reducing both power and latency of a decoding process is to use an analog circuit instead of a digital circuit. This paper investigates a continuous-time gradient flow-based approach for decoding LDPC codes, which employs a potential energy function similar to the objective function used in the gradient descent bit flipping (GDBF) algorithm. We experimentally demonstrate that the decoding performance of the gradient flow decoding is comparable to that of the multi-bit mode GDBF algorithm. Since an analog circuit of the gradient flow decoding requires only analog arithmetic operations and an integrator, future advancements in programmable analog integrated circuits may make practical implementation feasible.

## Energy-Efficient Decoding of Spatially Coupled Low-Density Parity-Check Codes using Adaptive Window Sizes

- **Status**: ✅
- **Reason**: SC-LDPC 적응형 윈도우 SWD 신규 디코더 + 22nm HW 구현 — C/D 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10273561
- **Type**: conference
- **Published**: 4-8 Sept. 
- **Authors**: Oliver Griebel, Matthias Herrmann, Bilal Hammoud +1
- **PDF**: https://ieeexplore.ieee.org/document/10273561
- **Abstract**: Wireless communication systems require high error correction capability, increasing data rates, lower round-trip latency, and efficient silicon implementation. Low-density parity-check (LDPC) codes have gained popularity as a class of forward error correction codes due to their ability to approach channel capacity for large block sizes. However, high-throughput decoding implementation is limited to small block sizes and few iterations. Spatially coupled LDPC (SC-LDPC) codes can outperform standard LDPC codes from an error correction perspective and exhibit locality in the Tanner graph by coupling small LDPC block codes (LDPC-BCs). This enables a sliding window decoding (SWD) decoding and, thus, overcomes the limitation of small block sizes. In this paper, we present a new SWD decoding algorithm and its decoder implementation in a 22 nm technology. The new decoder is based on an adaptive window size yielding power savings up to a factor of 4 in the high SNR range compared to the state-of-the-art.

## Generalized Automorphisms of Channel Codes: Properties, Code Design, and a Decoder

- **Status**: ✅
- **Reason**: 단블록 BP 개선용 일반화 자기동형 앙상블 디코딩(GAED)+코드구성, 바이너리 선형부호 — C/E 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10273488
- **Type**: conference
- **Published**: 4-8 Sept. 
- **Authors**: Jonathan Mandelbaum, Holger Jäkel, Laurent Schmalen
- **PDF**: https://ieeexplore.ieee.org/document/10273488
- **Abstract**: Low-density parity-check codes together with belief propagation (BP) decoding are known to be well-performing for large block lengths. However, for short block lengths there is still a considerable gap between the performance of BP decoding and maximum likelihood decoding. Different ensemble decoding schemes such as, e.g., automorphism ensemble decoding (AED), can reduce this gap in short block length regime. We propose generalized AED (GAED) that uses automorphisms according to the definition in linear algebra. Here, an automorphism of a vector space is defined as a linear, bijective self-mapping, whereas in coding theory self-mappings that are scaled permutations are commonly used. We show that the more general definition leads to an explicit joint construction of codes and automorphisms, and significantly enlarges the search space for automorphisms of existing linear codes. Furthermore, we prove the concept that generalized automorphisms can indeed be used to improve decoding. Additionally, we propose a code construction of linear codes enabling the construction of codes with suitably designed automorphisms. Finally, we analyze the decoding performances of GAED for some of our constructed codes.

## Low-Activity Gallager-B LDPC Decoding

- **Status**: ✅
- **Reason**: Low-Activity Gallager-B 신규 디코더 + ASIC 언롤 구현, 50% 동적에너지 절감 — 이식 가능 디코더/HW 신규 기여(C/D), on-chip memory ECC 직접 언급
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10273576
- **Type**: conference
- **Published**: 4-8 Sept. 
- **Authors**: Simon Brown, Jérémy Nadal, François Leduc-Primeau
- **PDF**: https://ieeexplore.ieee.org/document/10273576
- **Abstract**: Reducing the energy consumption of LDPC decoders is an essential step towards increasing the relevance of these codes in energy-constrained applications such as protecting on-chip memories. Gallager-B (GaB) LDPC decoders are well suited for high throughput applications due to their low complexity. We propose Low-Activity Gallager-B (LA-GaB), a functional equivalent to GaB with reduced message switching probability, and an adapted density evolution technique capable of predicting its message switching probabilities. We demonstrate an ASIC implementation of LA-GaB in an unrolled configuration achieving a reduction of more than 50% of dynamic energy and lower surface area compared to standard GaB, with no change in decoding performance. We also propose a high-level energy model of this unrolled implementation based on our activity model for rapid design exploration in the energy domain.

## LDPC Decoders Prefer More Reliable Parity Bits: Unequal Data Protection Over BSC

- **Status**: ✅
- **Reason**: BSC에서 패리티 비트 비균등 보호로 LDPC 메시지패싱 디코더 임계/수렴 개선 — 스토리지(BSC)·이식 가능 코드설계 기법(B/E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10273452
- **Type**: conference
- **Published**: 4-8 Sept. 
- **Authors**: Beyza Dabak, Ece Tiryaki, Robert Calderbank +1
- **PDF**: https://ieeexplore.ieee.org/document/10273452
- **Abstract**: Low-density parity-check (LDPC) codes are specified by graphs, and are the error correction technique of choice in many communications and data storage contexts. Message passing decoders diffuse information carried by parity bits into the payload, and this paper measures the value of engineering parity bits to be more reliable than message bits. We consider the binary symmetric channel (BSC) and measure the impact of unequal data protection on the threshold of a regular LDPC code. Our analysis also includes doping where the parity bits are known to the decoder. We investigate BSC with Gallager-A decoder, with a 3-1evel-alphabet decoder, and with a full belief propagation decoder. We demonstrate through theoretical analysis and simulation that non-equiprobable inputs lead to significant improvements both in the threshold and in the speed with which the decoder converges. We also show that all these improvements are possible even with a simple 3-1evel-alphabet decoder.

## A Low Complexity PEG-like Algorithm to Construct Quasi-Cyclic LDPC Codes

- **Status**: ✅
- **Reason**: large girth QC-LDPC 구성을 위한 저복잡도 PEG 변형(forbidden set·exponent 선택) — 새 코드설계 기법(E), 바이너리
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10273481
- **Type**: conference
- **Published**: 4-8 Sept. 
- **Authors**: Anthony Gómez-Fonseca, Roxana Smarandache, David G. M. Mitchell
- **PDF**: https://ieeexplore.ieee.org/document/10273481
- **Abstract**: In this paper, we introduce a modified version of the Progressive Edge-Growth (PEG) algorithm that is used to construct the Tanner graphs of quasi-cyclic (QC) low-density parity-check (LDPC) codes having large girth. In our algorithms, we replace certain requirements in the original PEG algorithm, namely the expansion of subgraphs from symbol nodes and the identification of a most distant check node before placing a new edge, by the construction of certain minimal sets, called forbidden sets, that contain the problematic quasi-cyclic constraints that do not let us exceed a given girth. We propose some exponent-selection strategies that are shown to increase the chance of obtaining large girth, and reduce the number of short cycles in the Tanner graph.

## Energy Optimization of Faulty Quantized Min-Sum LDPC Decoders

- **Status**: ✅
- **Reason**: 양자화 Min-Sum LDPC 디코더의 에너지 최적화(코드워드 길이·양자화 비트·전압 공동최적화) — 이식 가능한 디코더/HW 기법(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10273447
- **Type**: conference
- **Published**: 4-8 Sept. 
- **Authors**: Jérémy Nadal, Mohamed Yaoumi, Elsa Dupraz +2
- **PDF**: https://ieeexplore.ieee.org/document/10273447
- **Abstract**: The objective of this paper is to minimize the energy consumption of a quantized Min-Sum LDPC decoder, by considering aggressive voltage downscaling of the decoder circuit. Since low power supply may introduce faults in the memories used by the decoder architecture, this paper proposes to optimize the energy consumption of the faulty Min-Sum decoder while satisfying a given performance criterion. The proposed optimization method relies on a coordinate-descent algorithm that optimizes code and decoder parameters that have a strong influence on the decoder energy consumption: codeword length, number of quantization bits, and supply voltage. Optimal parameter values are provided for several codes defined by their protographs, and significant energy gains are observed compared to non-optimized setups. Finally, further gains are obtained when the supply voltage is optimized per decoding iteration.

## Learning to Decode Linear Block Codes using Adaptive Gradient-Descent Bit-Flipping

- **Status**: ✅
- **Reason**: 적응형 gradient-descent bit-flipping 디코더 일반화(학습 파라미터·AWGN 확장) — 이식 가능한 새 디코더 알고리즘(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10273470
- **Type**: conference
- **Published**: 4-8 Sept. 
- **Authors**: Jovan Milojković, Srdan Brkic, Predrag Ivaniš +1
- **PDF**: https://ieeexplore.ieee.org/document/10273470
- **Abstract**: In this paper we propose a generalization of the recently published adaptive diversity gradient-descent bit flipping (AD-GDBF) decoder, named generalized AD-GDBF (gAD-GDBF) decoder. While the original AD-GDBF decoder was designed for the binary symmetric channel and used mostly to decode regular low-density parity-check codes, the gAD-GDBF algorithm incorporates several improvements which makes it eligible for the additive white Gaussian channel and decoding of arbitrary linear block code. The gAD-GDBF decoder uses the genetic algorithm to optimize a set of learnable parameters, for a targeted linear block code. The effectiveness of the proposed method is verified on short Bose-Chaudhuri-Hocquenghem (BCH) codes, where it was shown that for the same number of decoding iterations the gAD-GDBF decoder outperforms the belief-propagation decoder in terms of bit error rate and at the same time reduces the decoding complexity significantly.

## Learning to Decode Trapping Sets in QLDPC Codes

- **Status**: ✅
- **Reason**: QLDPC이나 RNN 메시지패싱 학습 디코더가 고전 LDPC BP에서 유래, QC구조 활용·HW지향 — C(신경망 디코더) 예외 포함, Phase 3 재검토
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10273526
- **Type**: conference
- **Published**: 4-8 Sept. 
- **Authors**: Asit Kumar Pradhan, Nithin Raveendran, Narayanan Rengaswamy +2
- **PDF**: https://ieeexplore.ieee.org/document/10273526
- **Abstract**: Quantum low-density parity-check (QLDPC) codes with asymptotically nonzero rates are promising candidates for fault-tolerant quantum computation. Belief propagation (BP) based iterative decoding algorithms, a primary choice for classical LDPC codes, perform poorly for QLDPC codes due to stabilizer-induced trapping sets, resulting in a high error floor. Several decoding algorithms, like post-processing decoders, normalized BP decoders, and neural decoders, have been proposed to increase the performance in the error-floor region. However, this improvement comes at the expense of an increase in the execution time of the decoder. This paper proposes a general framework for error correction for a class of QLDPC codes called lifted-product codes using recurrent neural networks (RNNs). The RNN is employed to learn message-passing rules that can decode quantum-trapping sets. Then the standard message-passing rules are used with the learned rules to improve the error floor. While training the RNN, the quasi-cyclic property of the lifted product codes is exploited to reduce the size of the training set and the number of parameters in the network. This reduction in the number of parameters makes these decoders amenable to hardware implementation. Simulation results show that the proposed decoder performs better than the existing decoders in the literature.

## Analysis of Syndrome-Based Iterative Decoder Failure of QLDPC Codes

- **Status**: ✅
- **Reason**: QLDPC지만 trapping/absorbing set와 고전 LDPC 반복 디코딩 실패 구조 연결 — 양자 전용 개념 의존 약하고 고전 absorbing set 분석 이식 가능, 애매하여 살림(Phase 3 재검토)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10273573
- **Type**: conference
- **Published**: 4-8 Sept. 
- **Authors**: Kirsten D. Morris, Tefjol Pllaha, Christine A. Kelley
- **PDF**: https://ieeexplore.ieee.org/document/10273573
- **Abstract**: Iterative decoder failures of quantum low density parity check (QLDPC) codes are attributed to substructures in the code’s graph, known as trapping sets, as well as degenerate errors that can arise in quantum codes. Failure inducing sets are subsets of codeword coordinates that, when initially in error, lead to decoding failure in a trapping set. In this paper we examine the failure inducing sets of QLDPC codes under syndrome-based iterative decoding, and their connection to absorbing sets in classical LDPC codes.

## Sets of complementary LLRs to improve OSD post-processing of BP decoding

- **Status**: ✅
- **Reason**: BP 소프트출력에 대한 신경망 기반 다중 OSD 후처리 신규 기법, 바이너리 LDPC 대상 — C 포함
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10273537
- **Type**: conference
- **Published**: 4-8 Sept. 
- **Authors**: Joachim Rosseel, Valérian Mannoni, Valentin Savin +1
- **PDF**: https://ieeexplore.ieee.org/document/10273537
- **Abstract**: This article deals with Ordered Statistics Decoding (OSD) applied to the soft outputs of the Belief Propagation (BP) algorithm. We first model the weighted sum of the a posteriori LLRs across BP decoding iterations into a neuron. The neuron is then trained with the focal loss to compute for each BP decoding failure a set of accumulated Log Likelihood Ratios (LLRs) suited for OSD post-processing. Then, we propose a recursive selection procedure of LLRs sets, for multiple OSD post-processing. This selection is carried out from the sets of a posteriori LLRs calculated at each BP iteration, and from the accumulated LLRs optimized for the OSD, based on their joint probabilities of failure with OSD post-processing. An OSD is then applied to each set of LLRs belonging to the selection. In addition, we propose to reduce the OSD post-processing decoding complexity without significantly degrading its performance. Our results show that this new decoding method provides an effective way to bridge the gap to maximum likelihood decoding for short and long Low Density Parity Check (LDPC) codes.

## Reinforcement Learning for Sequential Decoding of Generalized LDPC Codes

- **Status**: ✅
- **Reason**: GLDPC 순차 BP 스케줄링을 RL로 최적화하는 새 디코더 기법, 바이너리 — C 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10273515
- **Type**: conference
- **Published**: 4-8 Sept. 
- **Authors**: Salman Habib, David G. M. Mitchell
- **PDF**: https://ieeexplore.ieee.org/document/10273515
- **Abstract**: In this work, we propose reinforcement learning (RL) for sequential decoding of moderate length generalized low-density parity-check (GLDPC) codes. Here, sequential decoding refers to scheduling all the generalized constraint nodes (GCNs) and single parity-check nodes (SPCNs) of a GLDPC code serially in each iteration. A GLDPC decoding environment is modeled as a finite Markov decision process (MDP) in which the state-space comprises of all possible sequences of hard-decision values of the variables nodes (VNs) connected to the scheduled GCN or SPCN, and the action-space of the MDP consists of all possible actions (GCN and SPCN scheduling). The goal of RL is to determine an optimized scheduling policy, i.e., one that results in a decoded codeword by minimizing the complexity of the belief propagation (BP) decoder. For training, we consider the proportion of correct bits at the output of the GCN or SPCN as a reward once it is scheduled. The expected rewards for scheduling all the GCNs/SPCNs in the code’s Tanner graph are earned via BP decoding during the RL phase. The proposed RL-based decoding scheme is shown to significantly outperform the standard BP flooding decoder, as well as a sequential decoder in which the GCNs/SPCNs are scheduled randomly.

## Improving Read Performance for LDPC-Based SSDs with Adaptive Bit Labeling on $V_{th}$ States

- **Status**: ✅
- **Reason**: NAND SSD LDPC 직접(A) — Vth 상태 적응형 비트 라벨링으로 read latency 최적화, NAND ECC 직접 관련
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10296401
- **Type**: conference
- **Published**: 30 Aug.-1 
- **Authors**: Jia-Xin Hou, Li-Pin Chang
- **PDF**: https://ieeexplore.ieee.org/document/10296401
- **Abstract**: NAND-based Solid-State Disks (SSDs) have become the mainstream storage solution thanks to their high I/O performance and data persistency. Modern SSDs boost their storage capacity by increasing the flash cell-bit density, resulting in severe leakage-induced bit errors over time. Low-Density Parity-Check (LDPC) is a common error correcting code for flash memory, which features incremental decoding strength levels through adding extra voltage sensing levels. However, when bit error rate becomes high, LDPC decoding with strong correction will be very slow. In this study, we identify that the read latency is strongly correlated with the method of bit labeling on cell threshold-voltage states, and based on this finding we propose using adaptive bit labeling to optimize the SSD read latency. Specifically, our method employ 2-3-2 Gray Coding as the default mode, and frequently-read data will be switched to using the least-significant page and center-significant page with 1-2-4 Gray Coding for fast reading. Our experimental results show that our design greatly outperforms static bit labeling and a state-of-the-art method.

## Trapping and Absorbing Set Enumerators for Multi-Edge Type LDPC Code Ensembles

- **Status**: ✅
- **Reason**: MET-LDPC 트래핑/흡수 집합 enumerator — error floor 분석 기법, 바이너리 코드 설계(E)에 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10313486
- **Type**: conference
- **Published**: 26-29 Sept
- **Authors**: Emna Ben Yacoub
- **PDF**: https://ieeexplore.ieee.org/document/10313486
- **Abstract**: The finite-length and asymptotic (elementary) trapping and (fully) absorbing set enumerators for multi-edge type (MET) low-density parity-check (LDPC) code ensembles are derived. An efficient method for the evaluation of the asymptotic distributions is presented and evaluated.

## Reliable Belief Propagation: Recent Theoretical and Practical Advances

- **Status**: ✅
- **Reason**: BP 수렴 개선(초기화/메시지 스케줄링/구조 수정) 부호 비의존 기법으로 바이너리 LDPC BP에 이식 가능 (C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10285934
- **Type**: conference
- **Published**: 17-20 Sept
- **Authors**: Christian Knoll, Franz Pernkopf
- **PDF**: https://ieeexplore.ieee.org/document/10285934
- **Abstract**: Belief propagation (BP) is an effective approximate inference method but lacks theoretical guarantees for loopy graphs. We discuss the optimization landscape and the message dynamics and how this helps to understand the behavior of message passing algorithms. These insights suggest several improvements. Specifically, we consider iterative initialization strategies, optimized message scheduling methods, and structural modifications, to improve the convergence behavior and accuracy while maintaining the model’s interpretability. We then evaluate the different modifications on signal detection problems in MIMO systems, which is a particularly challenging application for message passing algorithms. Our experimental results show consistent improvements over standard BP with minimal increase in computational burden.

## A Concise Polytope Projection Method for ADMM-Assisted LP Decoding of LDPC Codes

- **Status**: ✅
- **Reason**: LDPC ADMM-LP 디코딩의 패리티폴리톱 투영을 정렬 없이 HW 친화적으로 — 이식 가능 디코더 알고리즘·HW (C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10391405
- **Type**: conference
- **Published**: 15-16 Sept
- **Authors**: Parul, Manish Gupta, Rajesh Kumar Narula +1
- **PDF**: https://ieeexplore.ieee.org/document/10391405
- **Abstract**: The alternating direction method of multipliers (ADMM) has proven to be a highly efficient method for implementing linear programming (LP) decoding for low-density parity-check (LDPC) codes. The projection on the parity polytope is the most time-intensive operation involved in the ADMM-assisted LP decoding. The existing projection methods involve sorting operations or complicated iterations which are difficult to perform by hardware systems. In this paper, an efficient parity-polytope projection algorithm is proposed by mapping the projection problem onto an isomorphic problem of probability simplex. The projection on probability simplex is obtained by utilizing its recurrent structure. This algorithm does not require sorting operations. Each iteration fixes at least one component of the input vector and has straightforward iteration steps. The simulation results show a noticeable reduction in the processing time for obtaining the projection of a given vector. Due to these advantages, it is beneficial for the effective implementation of ADMM-assisted LP decoding systems.
