# IEEE Xplore — 2024-06 (1차선별 통과)


## Low-Rate LDPC Code Design for DTMB-A

- **Status**: ✅
- **Reason**: E: 저부호율 LDPC 코드 설계(Raptor-Like 구조, 점진적 블록 확장, 최소거리 최적화) — 바이너리 코드 구성 기법 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10410655
- **Type**: journal
- **Published**: June 2024
- **Authors**: Zhitong He, Kewu Peng, Chao Zhang +1
- **PDF**: https://ieeexplore.ieee.org/document/10410655
- **Abstract**: Digital terrestrial television multimedia broadcasting-advanced (DTMB-A) proposed by China is served as a 2nd generation digital terrestrial television broadcasting (DTTB) standard with advanced forward error correction coding schemes. Nevertheless, to adapt low signal-to-noise ratio (SNR) scenarios such as in cloud transmission systems, LDPC codes with low rates are required for DTMB-A. In this paper, the new design of low-rate DTMB-A LDPC codes is presented systematically. Specifically, a rate-compatible Raptor-Like structure of low-rate DTMB-A LDPC codes is presented, which supports multiple low code rates with constant code length. Then a new construction method is proposed for low-rate DTMB-A LDPC codes, where progressive block extension is employed and the minimum distance is majorly optimized such that the minimum distance increases after each block extension. Finally, the performance of the constructed DTMB-A LDPC codes with two low code rates of 1/3 and 1/4 are simulated and compared with ATSC 3.0 LDPC codes, which demonstrates the effectiveness of our design.

## A Generalized Adjusted Min-Sum Decoder for 5G LDPC Codes: Algorithm and Implementation

- **Status**: ✅
- **Reason**: 새 디코더 알고리즘(generalized adjusted min-sum)과 28nm ASIC 구현 — min-sum 변형(C)·HW 아키텍처(D) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10461640
- **Type**: journal
- **Published**: June 2024
- **Authors**: Yuqing Ren, Hassan Harb, Yifei Shen +2
- **PDF**: https://ieeexplore.ieee.org/document/10461640
- **Abstract**: 5G New Radio (NR) has stringent demands on both performance and complexity for the design of low-density parity-check (LDPC) decoding algorithms and corresponding VLSI implementations. Furthermore, decoders must fully support the wide range of all 5G NR blocklengths and code rates, which is a significant challenge. In this paper, we present a high-performance and low-complexity LDPC decoder, tailor-made to fulfill the 5G requirements. First, to close the gap between belief propagation (BP) decoding and its approximations in hardware, we propose an extension of adjusted min-sum decoding, called generalized adjusted min-sum (GA-MS) decoding. This decoding algorithm flexibly truncates the incoming messages at the check node level and carefully approximates the non-linear functions of BP decoding to balance the error-rate and hardware complexity. Numerical results demonstrate that the proposed fixed-point GA-MS has only a minor gap of 0.1 dB compared to floating-point BP under various scenarios of 5G standard specifications. Secondly, we present a fully reconfigurable 5G NR LDPC decoder implementation based on GA-MS decoding. Given that memory occupies a substantial portion of the decoder area, we adopt multiple data compression and approximation techniques to reduce 42.2% of the memory overhead. The corresponding 28nm FD-SOI ASIC decoder has a core area of 1.823 mm2 and operates at 895 MHz. It is compatible with all 5G NR LDPC codes and achieves a peak throughput of 24.42 Gbps and a maximum area efficiency of 13.40 Gbps/mm2 at 4 decoding iterations.

## Area-Efficient QC-LDPC Decoding Architecture With Thermometer Code-Based Sorting and Relative Quasi-Cyclic Shifting

- **Status**: ✅
- **Reason**: 5G QC-LDPC min-sum 디코더 HW 아키텍처 - thermometer code 정렬 및 상대 QC 시프트로 면적 절감; NAND LDPC 디코더 HW(D)에 이식 가능
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:10507156
- **Type**: journal
- **Published**: June 2024
- **Authors**: Boseon Jang, Hyejung Jang, Sungho Kim +2
- **PDF**: https://ieeexplore.ieee.org/document/10507156
- **Abstract**: The 5G New-Radio (NR) communication standard requires high throughput and low latency, so low-density parity-check (LDPC) codes, which have higher inherent parallelism and lower decoding complexity than turbo codes, were adopted as the main coding method for data channels. In traditional LDPC min-sum decoders, the check node unit was realized using a sorting unit based on the min-tree structure. However, this structure resulted in high hardware complexity and long latency. To address this issue, we propose a new sorting method based on the thermometer code-based number system. Additionally, we introduce a new LDPC decoding architecture that reduces the number of QSN stages from two to one, significantly lowering the shifting logic complexity needed to support different lifting sizes. This is achieved by using relative shift amounts instead of absolute shift amounts specified in the parity check matrix. The proposed decoder implemented using a partially parallel structure in a 65nm CMOS technology satisfies the various operation modes and the throughput requirements of the 5G NR standard, and boasts a higher normalized throughput than state-of-the-art LDPC decoders.

## EBDN: Entropy-Based Double Nonuniform Sensing Algorithm for LDPC Decoding in TLC nand Flash Memory

- **Status**: ✅
- **Reason**: A: TLC NAND 플래시 LDPC 디코딩용 엔트로피 기반 이중 비균일 센싱(LLR/센싱레벨) — NAND 직접, 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10382664
- **Type**: journal
- **Published**: June 2024
- **Authors**: Yongchao Wang, Debao Wei, Ming Liu +2
- **PDF**: https://ieeexplore.ieee.org/document/10382664
- **Abstract**: Low-density parity-check (LDPC) codes are widely employed in NAND flash memory to improve the reliability of data. However, LDPC has serious latency problems when the raw bit error rate (RBER) is high. The reason is that not only a sufficient sensing level is required to obtain accurate soft information but also a high number of iterations are needed. To reduce the latency of LDPC, an entropy-based double nonuniform (EBDN) sensing algorithm is proposed in this article. The basic idea of this algorithm is to exploit the entropy to quantify the nonuniformity of intrastate and interstate. And the sensing levels are placed in a targeted manner based on the entropy, thereby significantly reducing the number of sensing levels without reducing the LDPC error correction performance. The experimental results show that the proposed algorithm can decrease the number of iterations of LDPC by approximately 70% and reduce the read latency by 34.52% compared with the traditional nonuniform sensing algorithm.

## Spatially Coupled Codes via Bidirectional Block Markov Superposition Transmission

- **Status**: ✅
- **Reason**: E: 양방향 block Markov superposition으로 새 spatially-coupled 코드 구성, SC-LDPC 대비 유한길이 성능 개선 - 이식 가능 바이너리 코드 설계
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10339816
- **Type**: journal
- **Published**: June 2024
- **Authors**: Gaoyan Li, Shancheng Zhao, Haiqiang Chen +1
- **PDF**: https://ieeexplore.ieee.org/document/10339816
- **Abstract**: In this paper, we present a new class of spatially coupled codes obtained by using both non-recursive and recursive block-oriented superposition. The resulting codes are termed as bidirectional block Markov superposition transmission (BiBMST) codes. Firstly, we perform an iterative decoding threshold analysis according to protograph-based extrinsic information transfer (PEXIT) charts for the BiBMST codes over the binary erasure channels (BECs). Secondly, we derive the generator and parity-check matrices of the BiBMST codes. Thirdly, extensive numerical results are presented to show the advantages of the proposed BiBMST codes. Particularly, our numerical results show that, under the constraint of an equal decoding latency, the BiBMST codes perform better than the recursive BMST (rBMST) codes. However, the simulation results show that, in finite-length regime, negligible performance gain is obtained by increasing the encoding memory. We solve this limitation by introducing partial superposition, and the resulting codes are termed as partially-connected BiBMST (PC-BiBMST) code. Analytical results have confirmed the advantages of the PC-BiBMST codes over the original BiBMST codes. We also present extensive simulation results to show the performance advantages of the PC-BiBMST codes over the spatially coupled low-density parity-check (SC-LDPC) codes, spatially coupled generalized LDPC (SC-GLDPC) codes, and the original BiBMST codes in the finite-length regime.

## Joint Design of Denoising Diffusion Probabilistic Models and LDPC decoding for Wireless Communications

- **Status**: ✅
- **Reason**: DDPM+RNN 결합 LDPC 디코딩 구조 제안, NMS 대비 BER 이득. 무선 응용이나 신경망 보조 디코더 기법은 이식 가능(C) - 애매하여 in으로 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10615729
- **Type**: conference
- **Published**: 9-13 June 
- **Authors**: Xudong Guan, Hao Ju, Yin Xu +4
- **PDF**: https://ieeexplore.ieee.org/document/10615729
- **Abstract**: Due to its powerful generative capabilities, denoising diffusion probabilistic models (DDPM) have found applications in various domains. In this paper, DDPM is employed in a wireless channel receiver, where we design a decoder structure incor-porating DDPM and low-density parity-check (LDPC) decoding to enhance the error correction capabilities of the receiver. The LDPC decoding method based on DDPM proposed in this paper is iterative. The received signal must pass through the DDPM and demodulation modules first. The output is multiplied with the LDPC parity check matrix to get the parity information and then feedback to the DDPM module to assist and carry out the following iterative denoising output. Compared with the typical communication system, the LDPC decoding method proposed in this paper utilizes the diffusion model to assist the channel equal-ization with the parity check information generated during the decoding process and realizes the inter-module joint optimization at the receiver. Also, in order to have a better performance on processing and predicting sequence data, recurrent neural net-work (RNN) is a reasonable choice for its unique circular concept and the long-short-term memory network structure. This paper proved that the proposed decoding method has BER performance gains of 0.5dB to 0.2dB over the typical LDPC decoding methods using normalized min-sum(NMS) algorithm under additive white Gaussian noise (AWGN) channel and Rayleigh channel.

## High-Rate Fair-Density Parity-Check Codes

- **Status**: ✅
- **Reason**: FDPC 신규 패리티검사행렬 구성 + MP-PL(weighted min-sum+progressive list) 신규 디코더 — 바이너리 코드설계(E)·디코더(C) 모두 새 기여
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10622808
- **Type**: conference
- **Published**: 9-13 June 
- **Authors**: Hessam Mahdavifar
- **PDF**: https://ieeexplore.ieee.org/document/10622808
- **Abstract**: We introduce fair-density parity-check (FDPC) codes targeting high-rate applications. In particular, we start with a base parity-check matrix $H_{b}$ of dimension $2\sqrt{n}\times n$, where $n$ is the code block length, and the number of ones in each row and column of $H_{b}$ is equal to $\sqrt{n}$ and 2, respectively. We propose a deterministic combinatorial method for picking the base matrix $H_{b}$, assuming $n=4t^{2}$ for some integer $t\geqslant 2$. We then extend this by obtaining permuted versions of $H_{b}$ (e.g., via random permutations of its columns) and stacking them on top of each other leading to codes of dimension $k\geqslant n-2s\sqrt{n}+s$, for some $s\geqslant 2$, referred to as order-s FDPC codes. We propose methods to explicitly characterize and bound the weight distribution of the new codes and utilize them to derive union-type approximate upper bounds on their error probability under Maximum Likelihood (ML) decoding. For the binary erasure channel (BEC), we demonstrate that the approximate ML bound of FDPC codes closely follows the random coding upper bound (RCU) for a wide range of channel parameters. Also, remarkably, FDPC codes, under the low-complexity min-sum decoder, improve upon 5G-LDPC codes for transmission over the binary-input additive white Gaussian noise (B-AWGN) channel by almost 0.5dB (for $n=1024$, and rate = 0.878). Furthermore, we propose a new decoder as a combination of weighted min-sum message-passing (MP) decoding algorithm together with a new progressive list (PL) decoding component, referred to as the MP-PL decoder, to further boost the performance of FDPC codes. This paper opens new avenues for a fresh investigation of new code constructions and decoding algorithms in high-rate regimes suitable for ultra-high throughput (high-frequency/optical) applications.

## Effect of Feedback Delay on Adaptive LDPC Coding in a Fading Free-Space Optical Channel

- **Status**: ✅
- **Reason**: PBRL(protograph Raptor-like) LDPC 가변레이트 부호 설계 — 코드 구성 기법(E) 이식 가능, FSO 적응코딩은 응용일 뿐
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10622619
- **Type**: conference
- **Published**: 9-13 June 
- **Authors**: Semira Galijasevic, Jingchao Luo, Dariush Divsalar +1
- **PDF**: https://ieeexplore.ieee.org/document/10622619
- **Abstract**: Free-space optical (FSO) links are sensitive to channel fading caused by atmospheric turbulence, varying weather conditions, and changes in the distance between the transmitter and receiver. To mitigate FSO fading, this paper applies linear and quadratic prediction to estimate fading channel conditions and dynamically select the appropriate low-density parity check (LDPC) code rate. This adaptivity achieves reliable communication while efficiently utilizing the available channel mutual information. Protograph-based Raptor-like (PBRL) LDPC codes supporting a wide range of rates are designed, facilitating convenient rate switching. When channel state information (CSI) is known without delay, dynamically selecting LDPC code rate appropriately maximizes throughput. This work explores how such prediction behaves as the feedback delay is increased from no delay to a delay of 4 ms for a channel with a coherence time of 10 ms.

## Low-Complexity Linear Programming Based Decoding of Quantum LDPC Codes

- **Status**: ✅
- **Reason**: quantum LDPC지만 SB-LP/SB-MS 디코더와 early-stopping은 고전 BP/min-sum 유래로 error floor 저감 — 양자전용 개념 의존 낮아 예외 포함(C), 애매해 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10622622
- **Type**: conference
- **Published**: 9-13 June 
- **Authors**: Sana Javed, Francisco Garcia-Herrero, Bane Vasić +1
- **PDF**: https://ieeexplore.ieee.org/document/10622622
- **Abstract**: This paper proposes two approaches for reducing the impact of the error floor phenomenon when decoding quantum low-density parity-check codes with belief propagation based algorithms. First, a low-complexity syndrome-based linear programming (SB- LP) decoding algorithm is proposed, and second, the proposed SB-LP is applied as a post-processing step after syndrome-based min-sum (SB-MS) decoding. For the latter case, a new early stopping criterion is introduced to decide when to activate the SB- LP algorithm, avoiding executing a predefined maximum number of iterations for the SB-MS decoder. Simulation results show, for a sample hypergraph code, that the proposed decoder can lower the error floor by two to three orders of magnitude compared to SB-MS for the same total number of decoding iterations.

## Efficient Near Maximum-Likelihood Reliability-Based Decoding for Short LDPC Codes

- **Status**: ✅
- **Reason**: 짧은 LDPC용 BP+OSD 결합 근ML 디코딩 알고리즘 제안 - 이식 가능 디코더 알고리즘(C)에 직접 해당
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10622261
- **Type**: conference
- **Published**: 9-13 June 
- **Authors**: Weiyang Zhang, Chentao Yue, Yonghui Li +1
- **PDF**: https://ieeexplore.ieee.org/document/10622261
- **Abstract**: In this paper, we propose an efficient decoding algorithm for short low-density parity check (LDPC) codes by carefully combining the belief propagation (BP) decoding and ordered statistics decoding (OSD) algorithms. Specifically, a modified BP (mBP) algorithm is applied for a certain number of iterations prior to OSD to enhance the reliability of the received message, where an offset parameter is utilized in mBP to control the weight of the extrinsic information in message passing. By carefully selecting the offset parameter and the number of mBP iterations, the number of errors in the most reliable positions (MRPs) in OSD can be reduced by mBP, thereby significantly improving the overall decoding performance of error rate and complexity. Simulation results show that the proposed algorithm can approach the maximum-likelihood decoding (MLD) for short LDPC codes with only a slight increase in complexity compared to BP and a significant decrease compared to OSD. Specifically, the order- (m -1) decoding of the proposed algorithm can achieve the performance of the order-m OSD.

## A Deep Learning Based Decoder for Concatenated Coding Over Deletion Channels

- **Status**: ✅
- **Reason**: DL 기반 LLR 추정/외부 LDPC 디코더(BI-GRU) — 신경망 디코더 기법(C)으로 이식 가능, deletion 채널이지만 디코더 구조 떼어낼 여지
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10622561
- **Type**: conference
- **Published**: 9-13 June 
- **Authors**: E. Uras Kargı, Tolga M. Duman
- **PDF**: https://ieeexplore.ieee.org/document/10622561
- **Abstract**: In this paper, we introduce a deep learning-based decoder designed for concatenated coding schemes over a deletion/substitution channel. Specifically, we focus on serially concatenated codes, where the outer code is either a convolutional or a low-density parity-check (LDPC) code, and the inner code is a marker code. We utilize Bidirectional Gated Recurrent Units (BI-GRUs) as log-likelihood ratio (LLR) estimators and outer code decoders for estimating the message bits. Our results indicate that decoders powered by BI-GRUs perform comparably in terms of error rates with the MAP detection of the marker code. We also find that a single network can work well for a wide range of channel parameters. In addition, it is possible to use a single BI-GRU based network to estimate the message bits via one-shot decoding when the outer code is a convolutional code. 11Code is available at https://github.com/Bilkent-CTAR-Lab/DNN-for-Deletion-Channel

## Implementation of LDPC Decoder using Barrel Shifter

- **Status**: ✅
- **Reason**: 배럴 시프터 기반 LDPC 디코더 HW 아키텍처 — 시프트 연산·throughput/latency 최적화, NAND LDPC HW로 이식 가능(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:10575499
- **Type**: conference
- **Published**: 5-7 June 2
- **Authors**: Bhavya Lakshmi Tulasi Edara, T Guhambika Naga Aishwarya, Saahith Reddy Patlolla +1
- **PDF**: https://ieeexplore.ieee.org/document/10575499
- **Abstract**: The research work explores the implementation of an LDPC decoder utilizing a barrel shifter architecture tailored for processing 128-bit data. LDPC codes are recognized for their efficacy in error correction across various communication systems, necessitating efficient decoding mechanisms. Integration of a barrel shifter into the decoder architecture facilitates essential shifting operations required for LDPC decoding, thereby enhancing throughput and minimizing latency. The study delves into the design considerations for the barrel shifter-based implementation and elucidates the LDPC decoding algorithm. Through simulation, the performance of the proposed decoder is evaluated in terms of throughput, latency, and resource utilization. The experimental results validate the feasibility and effectiveness of the LDPC decoder with a barrel shifter architecture for processing 128-bit data, underscoring its potential for integration into high-speed communication systems.

## The Comparative Analysis of Single Error Bursts Decoders for Linear Codes

- **Status**: ✅
- **Reason**: single error burst 디코더를 sparse parity-check matrix 구조(블록-순열 구성) 영향 관점에서 분석 — LDPC sparse 패리티검사 행렬 디코딩 기법 이식 가능성, 애매하므로 in.
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10564623
- **Type**: conference
- **Published**: 3-7 June 2
- **Authors**: A. M. Veresova, M. N. Isaeva, A. A. Ovchinnikov
- **PDF**: https://ieeexplore.ieee.org/document/10564623
- **Abstract**: The article considers the problem of correcting single error bursts, taking into account the influence of the structure of the linear block code parity-check matrix on the performance of decoding algorithms. A heuristic algorithm based on the determination of certain events and an algorithm based on dense information sets for correcting single error bursts are considered. Codes based on a block-permutation construction, as well as random linear codes, are selected. Experiments have been conducted to evaluate the computational efficiency and error probability for the codes and decoders under consideration, taking into account the density of the parity-check matrices and the construction of the codes. It is obtained that when using a block-permutation construction, the heuristic algorithm shows a much lower probability of error with an operating time slightly inferior to the decoder based on dense information sets. However, when the structure of the sparse parity-check matrix changes, the decoding complexity increases, and with increasing matrix density, the complexity of the heuristic algorithm tends to exponential even with small burst lengths. For matrices that do not have a block-permutation structure, the algorithm based on dense information sets shows the best error probability and operating time. Thus, based on the comparative analysis carried out, it can be concluded that the task of correcting single error bursts can be solved with polynomial complexity regardless of the structure of the linear code and optimized taking into account this structure.

## Comparative Analysis of Processing Latency and CPU Efficiency in FPGA-Based FEC Acceleration

- **Status**: ✅
- **Reason**: FPGA 기반 LDPC 디코더 가속(RFNoC) 아키텍처·지연/CPU 효율 분석 — 이식 가능 HW(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:10588877
- **Type**: conference
- **Published**: 24-28 June
- **Authors**: Aerman Tuerxun, Akihiro Nakao
- **PDF**: https://ieeexplore.ieee.org/document/10588877
- **Abstract**: As Radio Access Networks (RANs) evolve towards more intelligent and software-defined paradigms, an increasing number of workloads are being offloaded to hardware accelerators. A significant challenge in this context is to minimize CPU consumption while ensuring low and stable latency in processing acceleration. Tailoring load allocation to meet varying latency requirements in different application scenarios is essential. In this paper, we present an application of RF Network on Chip (RFNoC) technology for FPGA-based acceleration of Low-Density Parity-Check (LDPC) code and Polar code. We conduct a comparative analysis of CPU and FPGA processing performance in OpenAinInterface (OAI) platform, with and without the Data Plane Development Kit (DPDK), to determine optimal load allocation for diverse data requirements. The findings indicate that RFNoC serves as an effective FPGA accelerator for the LDPC process, offering up to a fivefold increase in acceleration and significantly reducing processing delay jitter. Furthermore, the experimental outcomes provide a foundation for future research endeavors, specifically in the realm of efficient load optimization strategies.

## Systematic Turbo-Polar, Turbo-LDPC-Polar and Turbo-LDPC Codes Based on Belief Propagation Decoding

- **Status**: ✅
- **Reason**: Turbo-LDPC/Turbo-LDPC-Polar BP 디코딩 결합 신규 스킴, 바이너리 — 이식 가능 디코더(C), 애매하나 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10683047
- **Type**: conference
- **Published**: 24-27 June
- **Authors**: Rahim Umar, Atta ul Quddus, Yi Ma
- **PDF**: https://ieeexplore.ieee.org/document/10683047
- **Abstract**: In this paper, we propose the Turbo principle (of using parallel concatenated channel encoders separated by an interleaver and iterative soft-input and soft-output decoding between the constituent decoders) onto Polar and LDPC codes resulting in Turbo-Polar, Turbo-LDPC-Polar and Turbo-LDPC schemes with the aim of enhancing the BLER performance while also reducing the decoding complexity. All the proposed turbo-coded schemes are decoded using the traditional Belief Propagation (BP) algorithm based on low-density parity-check iterative decoding through a factor graph. Monte Carlo simulation results confirm the superiority of Turbo-LDPC and Turbo-LDPC-Polar schemes in BLER performance over state-of-the-art cyclic redundancy check-aided successive cancellation List decoding (CA-SCL) of Polar Codes with a large list size of 32 for large block lengths (larger than 3072 bits) while having reduced computational decoding complexity in comparison to CA-SCL decoding in an additive white Gaussian noise (A WGN) channel. Furthermore, Turbo-LDPC (based on 5G New Radio specifications for LDPC code) outperforms the standalone 5G-NR LDPC code and achieves about 1 dB gain at a BLER of 10–4 over correlated slow fading Rayleigh channel; however, being turbo-iterative in nature, it has higher complexity (about six-fold) than the standalone 5GNR LDPC code.

## Enhanced Layered Quasi-Cyclic Low-Density Parity-Check Codes for the McEliece Cryptosystem in Satellite Communications System

- **Status**: ✅
- **Reason**: row-layered normalized min-sum QC-LDPC 디코딩 알고리즘 제안(C/D) — HW 자원 최적화, 바이너리 LDPC, 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10803377
- **Type**: conference
- **Published**: 21-23 June
- **Authors**: Junda Zhang, Ge Zhang, Zhigang Zhang +2
- **PDF**: https://ieeexplore.ieee.org/document/10803377
- **Abstract**: Given the rapid advancement of quantum computing technology, the McEliece cryptosystem, rooted in coding theory, stands out as one of the few cryptographic systems resilient against quantum attacks. Nevertheless, the system's extensive public key length and low transmission rate have hindered its practical utility. To overcome these challenges, we propose a methodology to implement the McEliece cryptosystem employing quasi-cyclic low-density parity-check (QC-LDPC) codes, thereby diminishing the public key size albeit at the expense of height-ened decryption complexity. Furthermore, we introduce a row-layered normalized min-sum low-density parity-check decoding algorithm aimed at minimizing system complexity and optimizing hardware resource utilization.

## Adaptive LDPC Decoder with Performance Prediction Based on Average Mutual Information

- **Status**: ✅
- **Reason**: AMI 기반 성능예측으로 디코딩 옵션을 전환하는 적응형 LDPC 디코더 — 이식 가능한 디코더 알고리즘(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10608331
- **Type**: conference
- **Published**: 19-21 June
- **Authors**: Xia An, Chao Zhang, Kewu Peng +2
- **PDF**: https://ieeexplore.ieee.org/document/10608331
- **Abstract**: In mobile reception scenario, the channel quality usually shows some fluctuation, while traditional low-density parity-check (LDPC) decoders which utilize fixed decoding algorithms have difficulties to balance the decoding complexity and threshold performance under different channel quality. Adaptive LDPC decoder needs performance prediction in order to guide the selection of decoding options. Traditional performance prediction based on signal-to-noise ratio and channel state information is not precise enough to help the selection of decoding options due to the rapidly varying instant channel state information or incorrect channel-parameter estimation. In this paper, we propose a novel adaptive LDPC decoder with bit-wise average mutual information (AMI) based performance prediction, which could switch between multiple decoding options according to the performance prediction results obtained from the computed AMI and the pre-determined AMI-performance relationship. The proposed decoder adopts multiple candidate decoding algorithms with distinct decoding complexity and threshold performance, and includes the option of direct retransmission. Thus, it could enhance the adaptability of the decoder to the varying channel quality, the robustness to the channel-parameter estimation error, and meanwhile cut down the computing resource waste caused by the avoidable decoding failure. We further propose a novel loop correction method which could effectively correct the channelparameter estimation error by using the decoder output to adjust the decoder input.
