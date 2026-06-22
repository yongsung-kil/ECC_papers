# IEEE Xplore — 2019-01 (1차선별 통과)


## A Probabilistic Parallel Bit-Flipping Decoder for Low-Density Parity-Check Codes

- **Status**: ✅
- **Reason**: 확률적 병렬 비트플리핑(PPBF) LDPC 디코더 신규 제안+HW 아키텍처, 카테고리 C/D 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8403902
- **Type**: journal
- **Published**: Jan. 2019
- **Authors**: Khoa Le, Fakhreddine Ghaffari, Lounis Kessal +4
- **PDF**: https://ieeexplore.ieee.org/document/8403902
- **Abstract**: This paper presents a new bit flipping (BF) decoder, called the probabilistic parallel BF (PPBF) for low-density parity-check codes on the binary symmetric channel. In the PPBF, the flipping operation is performed in a probabilistic manner which is shown to significantly improve the error correction performance. The advantage of the PPBF also comes from the fact that no global computation is required during the decoding process and that all the computations can be executed in the local computing units and in parallel. The PPBF provides a considerable improvement of the operating frequency and complexity, compared to other known BF decoders, while obtaining a significant gain in error correction. An improved version of the PPBF, called non-syndrome PPBF is also introduced, in which the global syndrome check is moved out of the critical path and a new terminating mechanism is proposed. In order to show the superiority of the new decoders in terms of hardware efficiency and decoding throughput, the corresponding hardware architectures are presented in Section II. The application-specific integrated circuit synthesis results confirm that the operating frequency of the proposed decoders is significantly improved, compared to that of the BF decoders in the literature while requiring lower complexity to be efficiently implemented.

## Finite-Length Construction of High Performance Spatially-Coupled Codes via Optimized Partitioning and Lifting

- **Status**: ✅
- **Reason**: 유한길이 바이너리 SC-LDPC 신규 구성(최적 overlap 파티셔닝+circulant power 최적화, error floor 개선), 카테고리 E
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8449217
- **Type**: journal
- **Published**: Jan. 2019
- **Authors**: Homa Esfahanizadeh, Ahmed Hareedy, Lara Dolecek
- **PDF**: https://ieeexplore.ieee.org/document/8449217
- **Abstract**: Spatially-coupled (SC) codes are a family of graph-based codes that have attracted significant attention, thanks to their capacity approaching performance and low decoding latency. An SC code is constructed by partitioning an underlying block code into a number of components and coupling their copies together. In this paper, we first introduce a general approach for the enumeration of detrimental combinatorial objects in the graph of finite-length SC codes. Our approach is general in the sense that it effectively works for SC codes with various partitioning schemes, column weights, and memories. Next, we present a two-stage framework for the construction of high performance binary SC codes optimized for the additive white Gaussian noise channels; we aim at minimizing the number of detrimental combinatorial objects in the error floor region. In the first stage, we deploy a novel partitioning scheme, called the optimal overlap partitioning, to produce the optimal partitioning corresponding to the smallest number of detrimental objects. In the second stage, we apply a new circulant power optimizer to further reduce the number of detrimental objects in the lifted graph. SC codes constructed by our new framework have up to two orders of magnitude error floor performance improvement and up to 0.6 dB SNR gain compared to prior state-of-the-art SC codes.

## Multi-Stream LDPC Decoder on GPU of Mobile Devices

- **Status**: ✅
- **Reason**: D: 모바일 GPU 다중스트림 LDPC 디코더 SW 구현, 병렬화/실시간 디코딩 아키텍처 기법 이식 가능
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:8666615
- **Type**: conference
- **Published**: 7-9 Jan. 2
- **Authors**: Roohollah Amiri, Hani Mehrpouyan
- **PDF**: https://ieeexplore.ieee.org/document/8666615
- **Abstract**: Low-density parity check (LDPC) codes have been extensively applied in mobile communication systems due to their excellent error correcting capabilities. However, their broad adoption has been hindered by the high complexity of the LDPC decoder. Although to date, dedicated hardware has been used to implement low latency LDPC decoders, recent advancements in the architecture of mobile processors have made it possible to develop software solutions. In this paper, we propose a multi-stream LDPC decoder designed for a mobile device. The proposed decoder uses graphics processing unit (GPU) of a mobile device to achieve efficient real-time decoding. The proposed solution is implemented on an NVIDIA Tegra board as a system on a chip (SoC), where our results indicate that we can control the load on the central processing units through the multi-stream structure.

## Decoder-in-the-Loop: Genetic Optimization-Based LDPC Code Design

- **Status**: ✅
- **Reason**: 유전 알고리즘 decoder-in-the-loop로 단길이 바이너리 LDPC 패리티검사행렬 설계(error floor/latency 개선) — 카테고리 E 이식 가능 코드 설계
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8846017
- **Type**: journal
- **Published**: 2019
- **Authors**: Ahmed Elkelesh, Moustafa Ebada, Sebastian Cammerer +2
- **PDF**: https://ieeexplore.ieee.org/document/8846017
- **Abstract**: LDPC code design tools typically rely on asymptotic code behavior and are affected by an unavoidable performance degradation due to model imperfections in the short length regime. We propose an LDPC code design scheme based on an evolutionary algorithm, the Genetic Algorithm (GenAlg), implementing a “decoder-in-the-loop” concept. It inherently takes into consideration the channel, code length and the number of iterations while optimizing the error-rate of the actual decoder hardware architecture. We construct short length LDPC codes (i.e., the parity-check matrix) with error-rate performance comparable to, or even outperforming that of well-designed standardized short length LDPC codes over both AWGN and Rayleigh fading channels. Our proposed algorithm can be used to design LDPC codes with special graph structures (e.g., accumulator-based codes) to facilitate the encoding step, or to satisfy any other practical requirement. Moreover, GenAlg can be used to design LDPC codes with the aim of reducing decoding latency and complexity, leading to coding gains of up to 0.325 dB and 0.8 dB at BLER of 10-5 for both AWGN and Rayleigh fading channels, respectively, when compared to state-of-the-art short LDPC codes. Also, we analyze what can be learned from the resulting codes and, as such, the GenAlg particularly highlights design paradigms of short length LDPC codes (e.g., codes with degree-1 variable nodes obtain very good results).

## On the Girth of Tanner (3, 13) Quasi-Cyclic LDPC Codes

- **Status**: ✅
- **Reason**: QC-LDPC girth 분석으로 스토리지용 바이너리 부호 설계 기법(E). 새로운 Tanner (3,13) 구성·사이클 분석 제시
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8588334
- **Type**: journal
- **Published**: 2019
- **Authors**: Hengzhou Xu, Huaan Li, Dan Feng +2
- **PDF**: https://ieeexplore.ieee.org/document/8588334
- **Abstract**: Girth is an important structural property of low-density parity-check (LDPC) codes. Motivated by the works on the girth of Tanner (3, 5), (3, 7), (3, 11), and (5, 7) quasi-cyclic (QC) LDPC codes, we, in this paper, study the girth of Tanner (3, 13) QC-LDPC codes of length  $13p$  for  $p$  being a prime of the form  $(39m+1)$ . First, the cycle structure of Tanner (3, 13) QC-LDPC codes is analyzed, and the cycles of length lesser than 12 are divided into five equivalent classes. Based on each equivalent class, the existence of the cycles is equivalent to the solution of polynomial equations in a 39th unit root in the prime filed  $\mathbb {F}_{p}$ . By solving these polynomial equations over  $\mathbb {F}_{p}$  and summarizing the resulting candidate prime values, the girth of Tanner (3, 13) QC-LDPC codes is obtained. As an advantage, Tanner (3, 13) QC-LDPC codes have much higher code rates than Tanner (3, 5), (3, 7), (3, 11), and (5, 7) QC-LDPC codes, and provide a promising coding scheme for the data storage systems and optical communications.

## Tanner  $(J,L)$  Quasi-Cyclic LDPC Codes: Girth Analysis and Derived Codes

- **Status**: ✅
- **Reason**: Tanner (J,L) QC-LDPC girth 분석 및 사이클 제거 기반 바이너리 LDPC 구성 — E 코드설계 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8571223
- **Type**: journal
- **Published**: 2019
- **Authors**: Hengzhou Xu, Huaan Li, Baoming Bai +2
- **PDF**: https://ieeexplore.ieee.org/document/8571223
- **Abstract**: Girth plays an important role in the design of low-density parity-check (LDPC) codes. Motivated by the works on the girth of some classes of Tanner quasi-cyclic (QC) LDPC codes, e.g., Tanner (3, 5), (3, 7), (3, 11), and (5, 7) codes, we, in this paper, study the girth of Tanner  $(J,L)$  QC-LDPC codes where  $J$  and  $L$  can be any two positive integers. According to the sufficient and necessary conditions for the existence of cycles of lengths 4, 6, 8, and 10, we propose an algorithm to determine the girth of Tanner  $(J,L)$  QC-LDPC codes with finite code lengths. Through the analysis of the obtained girth values, we generalize the laws of the girth distributions of Tanner  $(J,L)$  QC-LDPC codes. Furthermore, based on the exponent matrices of Tanner  $(J,L)$  QC-LDPC codes with known girths, we employ the column selection method and/or the masking technique to construct binary/nonbinary LDPC codes. The numerical results show that the constructed LDPC codes have good performance under iterative decoding over the additive white Gaussian noise channel.

## A High Throughput Implementation of QC-LDPC Codes for 5G NR

- **Status**: ✅
- **Reason**: 5G QC-LDPC 고처리율 구현+base matrix 프루닝 — 이식 가능 HW/구현 기법(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:8936954
- **Type**: journal
- **Published**: 2019
- **Authors**: Hao Wu, Huayong Wang
- **PDF**: https://ieeexplore.ieee.org/document/8936954
- **Abstract**: Quasi-cyclic low-density parity-check (QC-LDPC) codes are the choice for data channels in the fifth generation (5G) new radio (NR). At the transmitter side, code bits from the QC-LDPC encoder are delivered to the rate matcher. The task of the rate matcher is to select an appropriate number of code bits via puncturing and/or repetition. Code bits that are not selected do not need to be encoded. At the receiver side, the de-rate matcher combines code bits of different transmission attempts and sends them to the QC-LDPC decoder. The output of the QC-LDPC decoder only needs to include necessary systematic bits. Unnecessary systematic bits and parity bits can be completely removed from the decoding process. Taking these considerations into account, a smaller sub-base matrix instead of a full-base matrix can be used in the encoding and decoding process. In this paper, we propose an efficient implementation of QC-LDPC codes for 5G NR. The full-base matrix is pruned before being used. Compared to the traditional schemes, the proposed scheme improves the throughput of QC-LDPC codes in 5G NR.

## Joint Coding and Adaptive Image Transmission Scheme Based on DP-LDPC Codes for IoT Scenarios

- **Status**: ✅
- **Reason**: DP-LDPC 유한길이 error floor 저감 결합최적화; 바이너리 LDPC 코드설계 기법(E) 이식 여지로 애매하여 보존
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8630931
- **Type**: journal
- **Published**: 2019
- **Authors**: Li Deng, Zhiping Shi, Ouxun Li +1
- **PDF**: https://ieeexplore.ieee.org/document/8630931
- **Abstract**: For wireless image communication in the Internet of Things (IoT) scenarios, fast and low error coding and transmission mechanisms are imperative. The joint source-channel coding scheme based on the double protograph low-density parity-check (DP-LDPC) codes would be a potential candidate due to the low complexity and good error performance. However, the error floor performance of DP-LDPC codes may deteriorate for source sequences with higher source probabilities or shorter block lengths. This paper aims to improve the traditional DP-LDPC image transmission system for the IoT scenarios from the following aspects. First, a joint optimization method of finite-length DP-LDPC codes is proposed to reduce the error floor while keeping satisfactory waterfall region performance. Second, an improved rate allocation strategy based on the fuzzy logic control is adopted to further improve the transmission reliability of the proposed short block length DP-LDPC codes. This scheme may offer some new solutions for the IoT image communication. The simulation results indicate the effectiveness of the proposed methods.

## Design of Rate-Compatible Protograph LDPC Codes for Spin-Torque Transfer Magnetic Random Access Memory (STT-MRAM)

- **Status**: ✅
- **Reason**: STT-MRAM용 신규 RCP-LDPC 프로토그래프 설계+수정 P-EXIT — 바이너리 LDPC 코드설계(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8933063
- **Type**: journal
- **Published**: 2019
- **Authors**: Zhong Xingwei, Kui Cai, Pingping Chen +1
- **PDF**: https://ieeexplore.ieee.org/document/8933063
- **Abstract**: Thanks to its superior features of non-volatility, fast read/write speed, high endurance, and low power consumption, spin-torque transfer magnetic random access memory (STT-MRAM) has become a promising candidate for the next generation non-volatile memories (NVMs) and storage class memories (SCMs). However, it has been found that the write errors and read errors caused by thermal fluctuation and process variation severely degrade the reliability of STT-MRAM. Moreover, process imperfection also causes a diversity of the raw bit error rate (BER) among different dies of STT-MRAM. In this paper, we propose the design of novel rate-compatible protograph low-density parity-check (RCP-LDPC) codes to correct memory cell errors and mitigate the raw BER diversity of STT-MRAM. In particular, to deal with the asymmetric property of the STT-MRAM channel, we first apply an independent and identically distributed (i.i.d.) channel adapter to symmetrize the STT-MRAM channel. We then present a modified protograph extrinsic information transfer (P-EXIT) algorithm for the symmetrized STT-MRAM channel. We further propose a combined guideline, including the modified P-EXIT algorithm, the asymptotic weight enumerator (AWE) analysis, as well as the actual error rate performance, for designing protograph LDPC codes with short information word lengths for STT-MRAM. By further applying a code extension approach, we design novel RCP-LDPC codes that can work with a single encoder/decoder. Simulation results show that our proposed RCP-LDPC codes outperform the well-known rate-compatible AR4JA protograph codes as well as the fixed-rate quasi-cyclic (QC) LDPC codes in terms of both the error rate performance and the convergence speed over the STT-MRAM channel.

## Performance of HARQ-Assisted OFDM Systems Contaminated by Impulsive Noise: Finite-Length LDPC Code Analysis

- **Status**: ✅
- **Reason**: 유한길이 LDPC 성능 분석(밀도진화+워터폴 SNR), 바이너리 LDPC 유한길이 해석 기법(E) 이식 가능성
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8606937
- **Type**: journal
- **Published**: 2019
- **Authors**: Tong Bai, Chao Xu, Rong Zhang +2
- **PDF**: https://ieeexplore.ieee.org/document/8606937
- **Abstract**: Impulsive noise (IN) constitutes a limiting factor in power-line communication systems, especially in those relying on orthogonal frequency division multiplexing (OFDM). If a single time-domain sample is contaminated by an impulse, all subcarriers become contaminated after the spreading of the discrete Fourier transform-based demodulation. In order to alleviate this problem, hybrid automatic repeat-and-request (HARQ) is often invoked. Moreover, the powerful low-density parity-check (LDPC) codes have been increasingly employed in a variety of current and next-generation communication standards. Against this background, in this paper, we explicitly characterize the performance of LDPC-coded HARQ-assisted OFDM systems in the face of IN, where the performance metrics of the outage probability (OP) and the average number of retransmissions, as well as the effective throughput, are analyzed. First of all, we conceive a new algorithm for evaluating the OP in a realistic finite-length LDPC regime, by adapting both the so-called density evolution technique and the waterfall signal-to-noise ratio analysis method. Following this, both the average number of retransmission attempts and the effective throughput are investigated based on our analysis of the OP. The accuracy of the proposed analysis is confirmed by the simulation results, which also effectively quantify the impact of IN on HARQ-assisted OFDM systems in a finite-length LDPC regime.

## Girth Analysis of Tanner’s (3, 17)-Regular QC-LDPC Codes Based on Euclidean Division Algorithm

- **Status**: ✅
- **Reason**: 바이너리 (3,17) QC-LDPC girth/cycle 결정법(유클리드 나눗셈); 코드 설계 카테고리 E
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8765603
- **Type**: journal
- **Published**: 2019
- **Authors**: Hengzhou Xu, Yake Duan, Xiaoxiao Miao +1
- **PDF**: https://ieeexplore.ieee.org/document/8765603
- **Abstract**: In this paper, the girth distribution of the Tanner’s (3, 17)-regular quasi-cyclic LDPC (QC-LDPC) codes with code length  $17p$  is determined, where  $p$  is a prime and  $p \equiv 1~(\bmod ~51)$ . By analyzing their cycle structure, five equivalent types of cycles with length not more than 10 are obtained. The existence of these five types of cycles is transmitted into polynomial equations in a 51st unit root of the prime field  $\mathbb {F}_{p}$ . By using the Euclidean division algorithm to check the existence of solutions for such polynomial equations, the girth values of the Tanner’s (3, 17)-regular QC-LDPC codes are obtained.

## Protograph QC-LDPC and Rate-Adaptive Polar Codes Design for MLC NAND Flash Memories

- **Status**: ✅
- **Reason**: MLC NAND 플래시용 protograph QC-LDPC 코드설계+양자화 LLR/EXIT 기반 디코딩. NAND 직접+코드설계(A/E).
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8666631
- **Type**: journal
- **Published**: 2019
- **Authors**: Lingjun Kong, Yahui Liu, Haiyang Liu +1
- **PDF**: https://ieeexplore.ieee.org/document/8666631
- **Abstract**: A protograph-based quasi-cyclic (QC) low-density parity-check (LDPC) code for multi-level cell (MLC) NAND flash memories is proposed in this paper. In this design approach, the quantized voltage signals are measured for soft decoding because the exact voltage values are unavailable. Flash memory channels are asymmetric, and therefore, not optimal for existing LDPC codes optimized for symmetric additive white Gaussian noise (AWGN)-like channels. Mutual information (MI) between the input and output of flash memory is used to model the quantized log-likelihood ratio (LLR) messages. The base matrix of the method is constructed according to the degree sequences optimized by the modified extrinsic information transfer (EXIT) chart method for flash memories. The designed protograph-based codes have a low-complexity QC encoder structure with a readily parallelizable decoder structure. In addition, rate-adaptive polar code design based on Bhattacharyya parameters of the memory cell bits is proposed to further improve the storage efficiency of the MLC NAND flash memories. The code design takes advantage of the inherent characteristics of MLC flash memory channel to iteratively calculate the Bhattacharyya parameter of each memory cell bit, where the punctured positions are selected by choosing the bits with higher Bhattacharyya parameters to construct rate-adaptive polar codes. The simulation results confirm the benefits of the proposed coding schemes.

## Residual-Decaying-Based Informed Dynamic Scheduling for Belief-Propagation Decoding of LDPC Codes

- **Status**: ✅
- **Reason**: LDPC BP용 신규 informed dynamic scheduling(RD-RBP) — 부호 비의존 디코더 스케줄링 개선, NAND LDPC BP에 직접 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8641399
- **Type**: journal
- **Published**: 2019
- **Authors**: Huilian Zhang, Shaoping Chen
- **PDF**: https://ieeexplore.ieee.org/document/8641399
- **Abstract**: Belief-propagation (BP) algorithm and its variants are well-established methods for iterative decoding of LDPC codes. Among them, residual belief-propagation (RBP), which is the most primitive and representative informed dynamic scheduling (IDS) strategy, can significantly accelerate the convergence speed. However, RBP decoding suffers from a poor convergence error-rate performance due to its greedy property, which is one of the challenging issues in the design of IDS strategies. To tackle this problem, a novel IDS scheme, namely residual-decaying-based residual belief-propagation (RD-RBP) algorithm, is presented in this paper. In RD-RBP, a decaying mechanism is introduced to manipulate the residuals of those check-to-variable messages, preventing the decoding resources from being unreasonably occupied by a small group of edges in the Tanner graph. The greediness is therefore alleviated and better performance of convergence error-rate is achieved. Besides, a two-stage scheduling scheme combining prior-art variable-node and variable-to-check-edge RBP (V-VCRBP) with RD-RBP, named V-VC-RD-RBP, is proposed for achieving both fast convergence speed and a low convergence error-rate. The simulation results validate the advantages of the proposed schemes.

## Spatially Coupled Generalized Low-Density Parity-Check Codes Over Class-A Impulsive Noise Channels

- **Status**: ✅
- **Reason**: Binary SC-GLDPC code design: spatial coupling, generalized check nodes, edge-spreading optimization — portable code construction (E).
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8700190
- **Type**: journal
- **Published**: 2019
- **Authors**: Ping Wang, Liuguo Yin, Jianhua Lu
- **PDF**: https://ieeexplore.ieee.org/document/8700190
- **Abstract**: In this paper, a class of spatially coupled generalized low-density parity-check (SC-GLDPC) codes with minimum coupling width is introduced to mitigate the Class-A impulsive noise. Codes with minimum coupling width are beneficial to simple code structure, short window decoding delay, and small rate-loss. The SC-GLDPC code is constructed by coupling the multiple identical generalized low-density parity-check (GLDPC) codes. Decoding thresholds over impulsive channels are derived by a recursive extrinsic information transfer function approach and are further estimated by the fast prediction approach. An edge spreading optimization method is proposed to design SC-GLDPC codes with minimum coupling width. The simulation results show that the optimized SC-GLDPC codes with minimum coupling width can show capacity-approaching property over impulsive channels. Benefitting from spatial coupling and generalized check nodes the SC-GLDPC codes show better bit error rate performance over impulsive channels, compared with GLDPC codes and spatially coupled low-density parity-check (SC-LDPC) codes.

## Protograph Based Low-Density Parity-Check Codes Design With Mixed Integer Linear Programming

- **Status**: ✅
- **Reason**: MILP 기반 protograph QC-LDPC 단주기 제거/girth 최적화 신규 구성법, 바이너리 적용 — E 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8573763
- **Type**: journal
- **Published**: 2019
- **Authors**: Wojciech Sułek
- **PDF**: https://ieeexplore.ieee.org/document/8573763
- **Abstract**: An approach to design protograph-based low-density parity-check (LDPC) codes utilizing mixed integer linear programming (MILP) optimization is presented in this paper. The protograph (base graph) cyclic lifting for a class of quasi-cyclic LDPC codes is considered. In general, the short cycles elimination is the primary optimization goal, possibly weighted by a metric of cycles connectivity. A notion of closed walks in the base graph is shown to be a convenient way for representing sources of cycles in the lifted graph. We express the condition for non-existence of a cycle in the lifted graph corresponding to a closed walk in the base graph in the form of a set of linear inequalities. Such inequalities, collected for all closed walks shorter than a desired limit corresponding to girth, form a set of linear constraints. Meanwhile, the longer closed walks can be reflected in a linear objective function of the optimization. The proposed combination of constraints and objective function forms an input to a MILP solver. As a result, a globally optimized code graph can be obtained. The method can be utilized for binary as well as nonbinary LDPC codes. The numerical results show that the constructed codes can outperform similar codes deigned with reference heuristic search methods.

## Construction of Quasi-Cyclic Low Density Parity Check Codes for Magnetic Induction Communication

- **Status**: ✅
- **Reason**: 바이너리 QC-LDPC 신규 구성(PEXIT+PSO=DPMIP) 코드설계; 카테고리 E 이식 가능성, 애매하므로 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8790804
- **Type**: journal
- **Published**: 2019
- **Authors**: Hua Xu, Yanjing Sun, Wenjuan Shi
- **PDF**: https://ieeexplore.ieee.org/document/8790804
- **Abstract**: The magnetic induction (MI) communication has been proved to be an effective method in the wireless underground sensor networks (WUSN). MI communication system based on quasi-cyclic low density parity check (QC-LDPC) codes is expected to improve the transmission performance in WUSN for its good performance and hardware friendliness. In this paper, we aim to construct an optimized QC-LDPC code with low encoding complexity for MI communication system. Firstly, we present a novel method, magnetic induction - protograph extrinsic information transfer (MI-PEXIT) algorithm, which can evaluate the performance of the QC-LDPC codes and predict the distance threshold for successfully transmission of the direct MI communication. Then, we combine the discrete particle swarm optimization (PSO) algorithm with the MI-PEXIT algorithm, and propose a novel scheme DPMIP method to optimize the QC-LDPC codes for MI communication system. Furthermore, two groups of QC-LDPC codes with low encoding complexity are constructed by the proposed DPMIP algorithm, which have different code parameters and different coil parameters. Simulation results validate the superiority of the proposed QC-LDPC codes for MI communication in WUSN, and the proposed codes also can achieve a good trade-off between the complexity and the performance.

## Protograph-Based Globally-Coupled LDPC Codes Over the Gaussian Channel With Burst Erasures

- **Status**: ✅
- **Reason**: 프로토그래프 기반 GC-LDPC 바이너리 코드 설계(edge spreading 최적화·디코딩 임계값) — 카테고리 E 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8878962
- **Type**: journal
- **Published**: 2019
- **Authors**: Ji Zhang, Baoming Bai, Min Zhu +2
- **PDF**: https://ieeexplore.ieee.org/document/8878962
- **Abstract**: This paper presents two types of protograph-based globally-coupled low-density parity-check (GC-LDPC) codes formed by a new edge spreading operation. This operation is called the global edge spreading. The Gaussian approximation (GA) and the protograph-based extrinsic information transfer (P-EXIT) analysis are then generalized over a special type of burst-erasure channels (BuECs). Such channel incorporates both Gaussian noise and burst erasures, and is denoted by the Gaussian channel with burst erasures (BuEC-G). Furthermore, the stability condition for BuECs-G is proved and an edge spreading optimization method is proposed to design the structured GC-LDPC codes by predicting the iterative decoding thresholds of corresponding protographs. Simulation results show that the optimized GC-LDPC codes can achieve better thresholds and error performances than existing well-designed GC-LDPC codes, and provide near-capacity performances over BuECs-G.

## Improved Decoding Algorithms of LDPC Codes Based on Reliability Metrics of Variable Nodes

- **Status**: ✅
- **Reason**: LDPC IDS/RBP 스케줄링 개선(신뢰도 메트릭 기반 변수노드 업데이트). 바이너리 LDPC BP 디코더 알고리즘 이식 가능(C).
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8664167
- **Type**: journal
- **Published**: 2019
- **Authors**: Xingcheng Liu, Li’e Zi, Dong Yang +1
- **PDF**: https://ieeexplore.ieee.org/document/8664167
- **Abstract**: The informed dynamic scheduling (IDS) strategies for decoding of low-density parity-check codes obtained superior performance in error correction performance and convergence speed. However, there are still two problems existing in the current IDS algorithms. The first is that the current IDS algorithms only preferentially update the selected unreliable messages, but they do not guarantee the updating is performed with reliable information. In this paper, a two-step message selecting strategy is introduced. On the basis of the two reliability metrics and two types of variable node residuals, the residual belief propagation (BP) decoding algorithm, short for TRM-TVRBP, is proposed. With the algorithm, the reliability of the updating-messages can be improved. The second is the greediness problem, prevalently existed in the IDS-like algorithms. The problem arises mainly from the fact that the major computing resources are allocated to or concentrated on some nodes and edges. To overcome the problem, the reliability metric-based RBP algorithm (RM-RBP) is proposed, which can force every variable node to contribute its intrinsic information to the iterative decoding. At the same time, the algorithm can force the related variable nodes to be updated, and make every edge have an equal opportunity of being updated. The simulation results show that both the TRM-TVRBP and the RM-RBP have appealing convergence rate and error-correcting performance compared with the previous IDS decoders over the white Gaussian noise (AWGN) channel.

## Variable-Node-Based Belief-Propagation Decoding With Message Pre-Processing for NAND Flash Memory

- **Status**: ✅
- **Reason**: Binary LDPC VNBP-MP decoder for NAND flash with message pre-processing/oscillation handling — direct NAND + portable decoder (A/C).
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8703377
- **Type**: journal
- **Published**: 2019
- **Authors**: Xingcheng Liu, Guojun Yang, Xuechen Chen
- **PDF**: https://ieeexplore.ieee.org/document/8703377
- **Abstract**: With the fast development of non-volatile storage technology, NAND flash memory faces more and more challenges such as data reliability and lifetime. To overcome the issue of the reliability, low-density parity-check (LDPC) codes are considered as a main candidate of error-correction-codes (ECCs) for NAND flash storages. However, conventional soft decoding algorithms for LDPC codes suffer from the drawback of slow convergence speed, which increases the decoding latency. For achieving fast convergence speed, a variable-node-based belief-propagation with message pre-processing (VNBP-MP) decoding algorithm for binary LDPC codes and a non-binary VNBP-MP (NVNBP-MP) decoding algorithm for non-binary LDPC codes are proposed. Both of the algorithms utilize the characteristics of the NAND flash channel to perform the message pre-processing operations. In theory, the propagation of unreliable messages can be effectively prevented and the propagation of reliable messages can be speeded up. To further improve the decoding convergence, the treatment for oscillating variable nodes is considered after the message pre-processing operations. The simulation results also show that the proposed algorithms both have a noticeable improvement in convergence speed and latency, without compromising error-correction performance, compared with the existing soft decoding algorithms.

## Optimized Code Design for Constrained DNA Data Storage With Asymmetric Errors

- **Status**: ✅
- **Reason**: 바이너리 protograph LDPC를 EXIT로 최적화한 신규 코드 설계(E), NAND LDPC 구성에 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8746106
- **Type**: journal
- **Published**: 2019
- **Authors**: Li Deng, Yixin Wang, MD. Noor-A-Rahim +4
- **PDF**: https://ieeexplore.ieee.org/document/8746106
- **Abstract**: With ultra-high density and preservation longevity, deoxyribonucleic acid (DNA)-based data storage is becoming an emerging storage technology. Limited by the current biochemical techniques, data might be corrupted during the processes of DNA data storage. A hybrid coding architecture consisting of modified variable-length run-length limited (VL-RLL) codes and optimized protograph low-density parity-check (LDPC) codes is proposed in order to suppress error occurrence and correct asymmetric substitution errors. Based on the analyses of the different asymmetric DNA sequencer channel models, a series of the protograph LDPC codes are optimized using a modified extrinsic information transfer algorithm (EXIT). The simulation results show the better error performance of the proposed protograph LDPC codes over the conventional good codes and the codes used in the existing DNA data storage system. In addition, the theoretical analysis shows that the proposed hybrid coding scheme stores ~1.98 bits per nucleotide (bits/nt) with only 1% gap from the upper boundary (2 bits/nt).

## Joint VMIMO and LDPC Decoders for IR-UWB Wireless Body Area Network

- **Status**: ✅
- **Reason**: 신규 저복잡도 하이브리드 LDPC 복호 알고리즘 제안 — C 이식 가능 디코더, 애매하나 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8581588
- **Type**: journal
- **Published**: 2019
- **Authors**: Albashir Adel Youssef, Bassant Abdelhamid, S. H. Elramly +2
- **PDF**: https://ieeexplore.ieee.org/document/8581588
- **Abstract**: A complete impulse radio-ultra wide band (IR-UWB) system is proposed to mitigate the impairments concerning on-body to off-body Wireless Body Area Networks (WBAN). The proposed system maintains the practical communication link between on-body sensors to the fusion center or the monitoring device held by the medical representative. Also, these sensors are assigned a recently proposed pulse shaping to mitigate the noise that existed in the IR-UWB WBAN channel. Furthermore, virtual multiple-input multiple-output (VMIMO) is proposed to perform spatial multiplexing between various sensors transmitted data. Moreover, low complex low density parity check (LDPC) encoding/decoding algorithms, including a new low complex hybrid LDPC decoding algorithm, are proposed to reduce the complexity and to enhance the bit error rate of the on-body sensors. Interestingly, low energy consumption at every sensor participating in the on-body to off-body WBAN was achieved by adopting the combination between LDPC decoders and VMIMO technique. According to simulation results, the new system enhanced the BER performance and reduced the complexity of the on-body to off-body IR-UWB communication system effectively.

## Construction of Rate-Compatible Raptor-Like Quasi-Cyclic LDPC Code With Edge Classification for IDMA Based Random Access

- **Status**: ✅
- **Reason**: RL-QC-LDPC 코드 구성(edge-classification 확장 알고리즘, EXIT 기반 최적화). 바이너리 QC-LDPC 신규 구성 기법으로 이식 가능(E).
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8660484
- **Type**: journal
- **Published**: 2019
- **Authors**: Yushu Zhang, Kewu Peng, Zhangmei Chen +1
- **PDF**: https://ieeexplore.ieee.org/document/8660484
- **Abstract**: Recently, rate-compatible raptor-like quasi-cyclic low-density parity-check (RL-QC-LDPC) codes, which are a typical class of multi-edge type LDPC codes with excellent performance and high flexibility, have been adopted in the technical specification of 5G new radio (5G-NR). In this paper, the rate-compatible RL-QC-LDPC coded interleave division multiple access (IDMA), or called the enhanced IDMA, is developed as non-orthogonal multiple access (NOMA)-based random access solution, and various spectral efficiencies can be flexibly supported thanks to the rate compatible capability. First, 5G-NR LDPC codes are directly incorporated into enhanced IDMA-based random access, which can support a wide range of user loads with relatively low system throughput. Second, to improve the supported user load and system throughput, an edge-classification-based extension (ECE) algorithm is proposed to construct rate-compatible RL-QC-LDPC codes toward enhanced IDMA while taking into consideration the novel structural features of 5G-NR LDPC codes. Based on the two proposed edge-classification methods, the ECE can efficiently reduce the search space of base matrices for each extension round and effectively maintain enough diversity in the selected seed base matrices to facilitate further extension. Multi-edge type density evolution-aided extrinsic information transfer chart is employed to predict the asymptotic performance during the base matrix extension and optimization. As an example, a rate-compatible RL-QC-LDPC code family with fine code-rate granularity is constructed via the proposed ECE. Compared with 5G-NR LDPC coded IDMA, the outage performance of enhanced IDMA with the new code family can be significantly improved at high user load and system throughput for NOMA-based random access.

## Performance Analysis of Protograph LDPC Codes Over Large-Scale MIMO Channels With Low-Resolution ADCs

- **Status**: ✅
- **Reason**: 바이너리 protograph LDPC + 저해상도 ADC 양자화 잡음 반영 PEXIT 분석 — LLR 양자화/디코더 성능예측 기법 NAND 이식 여지(애매, Phase3 재검토)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8853252
- **Type**: journal
- **Published**: 2019
- **Authors**: Thuy V. Nguyen, Hieu D. Vu, Diep N. Nguyen +1
- **PDF**: https://ieeexplore.ieee.org/document/8853252
- **Abstract**: Protograph LDPC (P-LDPC) codes and large-scale multiple-input multiple-output (LS-MIMO) are cornerstones of 5G and future wireless systems, thanks to their powerful error-correcting capability and high spectral efficiency. To alleviate the high complexity in signal detection/decoding that dramatically grows with the number of antennas (in the order of tens or even hundreds), low-resolution analog-to-digital converters (ADCs) and joint detection and decoding using factor graph have recently attracted paramount interest. Unlike high-resolution ADCs, by using a small number of bits to quantize the received signal, low-resolution ADCs help reduce the hardware cost and power consumption of the RF circuit of practical LS-MIMO transceivers. Such a very much desirable reduction comes at the cost of additional quantization noise, introduced by low-resolution ADCs. This work aims to provide a unified framework to analyze the impact of the low-resolution ADCs on the performance of P-LDPC codes in practical LS-MIMO systems. It is worth noting that the previous analytical tools that have been used to evaluate the performance of P-LDPC codes do not account for the quantization noise effect of the low-resolution ADCs and the fact that the covariance of quantization noise depends on the fading channels. This article addresses this shortcoming by first leveraging the additive quantization noise model. We then derive the expression of extrinsic information for the belief-propagation LS-MIMO detector. The mutual information functions, which are the core elements of our proposed protograph extrinsic information transfer (PEXIT) algorithm, are analyzed for LS-MIMO communication systems. Our proposed PEXIT algorithm allows us to analyze and predict the impact of the low-resolution ADCs on the performance of P-LDPC codes, considering various input parameters, including the LS-MIMO configuration, the code rate, and the maximum number of decoding iterations, and the code structure. Based on our extensive analytical and simulation results, we found that the performance of 3-bit and 4-bit ADC systems only have a small gap to that of the unquantized systems. Especially when the 5-bit ADC scheme is applied, the performance loss is negligible. This finding sheds light on the practical design of LS-MIMO systems using P-LDPC codes.

## Parallel Concatenated Gallager Code with Single Encoder for Cognitive Radio Applications

- **Status**: ✅
- **Reason**: Gallager(LDPC) 부호의 parallel concatenated 단일 인코더 구성으로 enc/dec 복잡도 감소 — 바이너리 LDPC 코드설계/디코더 기법 이식 여지(애매, 살림)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8986215
- **Type**: conference
- **Published**: 2019
- **Authors**: G. P. Aswathy, K. Gopakumar, T. P. I. Ahamed
- **PDF**: https://ieeexplore.ieee.org/document/8986215
- **Abstract**: Recently, wireless communication operators identify the spectrum scarcity as a major problem to be solved. The revolutionary concept of Cognitive radio addresses this issue by providing opportunistic access of licensed bands to unlicensed users. The technology offers many challenges among which the reliable transmission of secondary user data is the significant one. The constant interference from the licensed users affects the secondary user communication thereby affecting the reliable communication in cognitive radio networks. Error control coding can be used to reduce the impact of interference from incumbent users. Low density parity check codes are used in cognitive radio networks for ensuring reliable data transmission. However, as the block length increases, these codes have high encoding and decoding complexity. Parallel concatenated Gallager codes overcome these drawbacks. We analyse the performance of proposed parallel concatenated Gallager codes with single encoder for secondary users in a dynamic network. Results confirm that these codes attained the performance of a dedicated code with reduced complexity and less decoding delay.

## Efficient Belief Propagation List Decoding of Polar Codes

- **Status**: ✅
- **Reason**: polar code용 효율적 BP list(EBPL) 디코딩 제안 — BP 리스트 메시지패싱 기법이 바이너리 LDPC BP에 이식 가능성 있어 애매하므로 살림(C, Phase 3 재검토)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8983597
- **Type**: conference
- **Published**: 2019
- **Authors**: Y. Ren, W. Xu, Z. Zhang +2
- **PDF**: https://ieeexplore.ieee.org/document/8983597
- **Abstract**: As known to all, polar codes have been chosen as the control channel codes for the enhance mobile broadband (eMBB) scenario in the 3GPP RAN1. Due to its excellent performance, polar codes also have caused widespread concern in the academia and industry. In general, polar codes can be decoded by two methods: successive cancellation (SC) and belief propagation (BP) algorithms. However, compared with the series of SC algorithms, the error-correction performance of BP decoding is not satisfactory, even though it has excellent parallel throughput. Hence, this paper proposes an efficient BP list (EBPL) decoding of polar codes which can enhance the performance to the same scale of successive cancellation list (SCL) without sacrificing decoding throughput. With reasonable complexity, the proposed EBPL decoding can achieve comparable BER and FER compared to SCL in simulation results.

## Theoretical Analysis and Implementation of Effective Receivers for Telecommand Space Links

- **Status**: ✅
- **Reason**: 짧은 LDPC용 비반복 디코더(most reliable basis=OSD 계열) 보드 구현은 OSD 디코더 알고리즘/HW로 NAND LDPC에 이식 가능(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8895426
- **Type**: conference
- **Published**: 2019
- **Authors**: M. Baldi, M. Bertinelli, F. Chiaraluce +9
- **PDF**: https://ieeexplore.ieee.org/document/8895426
- **Abstract**: This paper deals with the feasibility of the new receiver scheme for telecommand space links, based on the adoption of short low-density parity-check codes recently introduced in the standard. Being able to reduce significantly the required signal-to-noise ratio, these codes have an impact on the acquisition, tracking and synchronization issues. All these aspects have been faced, both theoretically and practically through the realization of a breadboard that implements the core elements of the on-board receiver, and is able to demodulate and decode uplink signals employing the new codes. The breadboard incorporates innovative solutions to cope with the acquisition and synchronization problems, and a pioneering implementation of non-iterative decoders based on the most reliable basis algorithm.

## Reliability Enhancement for Multi-level Cell NAND Flash Memory Using Error Asymmetry

- **Status**: ✅
- **Reason**: MLC NAND 플래시 ECC와 제약부호 결합으로 신뢰성/read latency 개선 — A(NAND 직접)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9026538
- **Type**: conference
- **Published**: 2019
- **Authors**: D. -P. Nguyen, K. Le Trung, F. Ghaffari +1
- **PDF**: https://ieeexplore.ieee.org/document/9026538
- **Abstract**: This paper presents the jointly use of constraint code (CC) and error correction codes (ECC) for the reliability enhancement in Multi-level cell NAND flash memories. In the proposed system, the constraint code helps transform the user data distribution, adapting to the asymmetry in error behavior of MLC NAND flash memories and the ECC corrects more errors thanks to the prior information from the data distribution. The compatibility of CC and ECC is analyzed, and the information loss is shown to be negligible, especially for the use in MLC NAND flash memories. Simulation under practical MLC NAND flash error model has shown that the proposed scheme can improve remarkably output error rate and reduce read latency in these memories.

## Improved iterative decoding of QC-MDPC codes in the McEliece public key cryptosystem

- **Status**: ✅
- **Reason**: QC-MDPC 반복 디코딩 개선(BF 실패 시 보조 변수노드 추가) — MDPC는 저밀도 패리티검사 계열이고 BF/iterative 디코더 개선 기법이 바이너리 LDPC에 이식 가능(C, 애매하면 in)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8849839
- **Type**: conference
- **Published**: 2019
- **Authors**: I. E. Bocharova, T. Johansson, B. D. Kudryashov
- **PDF**: https://ieeexplore.ieee.org/document/8849839
- **Abstract**: We improve iterative decoding of the moderate density parity-check codes, recently suggested as code candidates in the McEliece public key cryptosystem. In case of bit-flipping (BF) decoder failure, the code parity-check matrix is extended by adding auxiliary variable nodes based on reliability information from the BF decoder. Then iterative decoding is applied to the extended parity-check matrix. The proposed decoding algorithm is analyzed and its frame error rate performance is compared to the same performance of both the best implementations of BF decoding and its modifications. It is demonstrated an improved performance for the iterative decoding step in decryption, which allows to increase the resistance against recent attacks based on taking advantage of the somewhat large failure probability of the BF algorithm.

## Density Evolution Analysis of Partially Information Coupled Turbo Codes on the Erasure Channel

- **Status**: ✅
- **Reason**: 부분정보결합 turbo의 density evolution/BP threshold + 공간결합 기법이 SC-LDPC 분석에 이식 여지(애매, 살림)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8989359
- **Type**: conference
- **Published**: 2019
- **Authors**: M. Qiu, X. Wu, Y. Xie +1
- **PDF**: https://ieeexplore.ieee.org/document/8989359
- **Abstract**: In this paper, we investigate the performance of a class of spatially coupled codes, namely partially information coupled turbo codes (PIC-TCs) over the binary erasure channel (BEC). This class of codes enjoy flexible code rate adjustment by varying the coupling ratio. Moreover, the coupling method can be directly applied to any component codes without changing the encoding and decoding architectures of the underlying component codes. However, the theoretical performance of PIC-TCs has not been fully investigated. For this work, we consider the codes that have coupling memory $m$ and study the corresponding graph model. We then derive the exact density evolution equations for these code ensembles with any given coupling ratio and coupling memory $m$ to precisely compute their belief propagation decoding thresholds for the BEC. Our simulation results verify the correctness of our theoretical analysis and also show better error performance over uncoupled turbo codes with a variety of code rates on the BEC.

## Segmentation-Discarding Ordered-Statistic Decoding for Linear Block Codes

- **Status**: ✅
- **Reason**: Segmentation-discarding OSD for short block codes — OSD is listed under C (portable decoder algorithms); proposes novel complexity-reduction technique transferable to LDPC OSD.
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9014173
- **Type**: conference
- **Published**: 2019
- **Authors**: C. Yue, M. Shirvanimoghaddam, Y. Li +1
- **PDF**: https://ieeexplore.ieee.org/document/9014173
- **Abstract**: In this paper, we propose an efficient reliability based segmentation-discarding decoding (SDD) algorithm for short block-length codes. A novel segmentation- discarding technique is proposed along with the stopping rule to significantly reduce the decoding complexity without a significant performance degradation compared to ordered statistics decoding (OSD). In the proposed decoder, the list of test error patterns (TEPs) is divided into several segments according to carefully selected boundaries and every segment is checked separately during the reprocessing stage. Decoding is performed under the constraint of the discarding rule and stopping rule. Simulations results for different codes show that our proposed algorithm can significantly reduce the decoding complexity compared to the existing OSD algorithms in literature.

## ASCache: An Approximate SSD Cache for Error-Tolerant Applications

- **Status**: ✅
- **Reason**: 플래시 SSD 캐시 오류 허용 — 카테고리 A(NAND/SSD 직접), ECC 오버헤드 트레이드오프 관련
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8807019
- **Type**: conference
- **Published**: 2019
- **Authors**: F. Li, Y. Lu, Z. Wu +1
- **PDF**: https://ieeexplore.ieee.org/document/8807019
- **Abstract**: With increased density, flash memory becomes more vulnerable to errors. Error correction incurs high overhead, which is sensitive in SSD cache. However, some applications like multimedia processing have the intrinsic tolerance of inaccuracies. In this paper, we propose ASCache, an approximate SSD cache, which allows bit errors in a controllable threshold for error-tolerant applications, so as to reduce the cache miss ratio caused by incorrect cache pages. ASCache further trades the strictness of error correction mechanisms for higher SSD access performance. Evaluations show ASCache reduces the average read latency by at most 30% and the cache miss ratio by 52%.

## A Joint Graph Based Coding Scheme for the Unsourced Random Access Gaussian Channel

- **Status**: ✅
- **Reason**: unsourced random access용 sparse 그래프 joint message-passing 디코딩, 바이너리 BP 기법 이식 가능성 — 애매하여 살림(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9013278
- **Type**: conference
- **Published**: 2019
- **Authors**: A. Pradhan, V. Amalladinne, A. Vem +2
- **PDF**: https://ieeexplore.ieee.org/document/9013278
- **Abstract**: This article introduces a novel communication paradigm for the unsourced, uncoordinated Gaussian multiple access problem. The major components of the envisioned framework are as follows. The encoded bits of every message are partitioned into two groups. The first portion is transmitted using a compressive sensing scheme, whereas the second set of bits is conveyed using a multi-user coding scheme. The compressive sensing portion is key in sidestepping some of the challenges posed by the unsourced aspect of the problem. The information afforded by the compressive sensing is employed to create a sparse random multi-access graph conducive to joint decoding. This construction leverages the lessons learned from traditional IDMA into creating low- complexity schemes for the unsourced setting and its inherent randomness. Under joint message- passing decoding, the proposed scheme offers superior performance compared to existing low- complexity alternatives. Findings are supported by numerical simulations.

## Information Preserving Quantization and Decoding for Satellite-Aided 5G Communications

- **Status**: ✅
- **Reason**: Information Bottleneck 저비트 양자화+LUT 기반 이산 디코더가 BP 근접 — LLR 양자화/LUT 디코더 기법이 NAND LDPC에 직접 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8911701
- **Type**: conference
- **Published**: 2019
- **Authors**: T. Monsees, D. Wübben, A. Dekorsy
- **PDF**: https://ieeexplore.ieee.org/document/8911701
- **Abstract**: We consider the uplink of a non-terrestrial network where a relay node is forwarding digitized signals via a rate limited error-prone forward link to the serving satellite. The focus of our investigations are the design of suitable low-bit resolution quantization schemes to limit the rate on the forward link and the optimization of the decoder processing at the satellite. To this end, we investigate Information Bottleneck (IB) based quantizer design with mutual information as fidelity criterion. The IB approach can be extended to consider also the error statistic of the forward link within the quantizer design. By numerical investigations we demonstrate the performance gains of this forward-aware IB quantizer in case of erroneous forward links. Furthermore, we investigate a lookup-table based decoder which is optimized for the end-to-end statistic including the access link, the quantizer and the forward link. This decoder implementation processes only discrete values using lookup-tables of small size. The numerical results show that the performance of 3-bit forward-aware IB quantizer in combination with a 3-bit discrete decoder implementation is close to the double-precision floating-point belief propagation decoder even for strongly error-prone forward links.

## Deep Learning-Based Polar Code Design

- **Status**: ✅
- **Reason**: 폴라코드지만 decoder-in-the-loop 학습형 BP 구성 — 바이너리 LDPC BP에 이식 가능성, 애매하여 살림(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8919804
- **Type**: conference
- **Published**: 2019
- **Authors**: M. Ebada, S. Cammerer, A. Elkelesh +1
- **PDF**: https://ieeexplore.ieee.org/document/8919804
- **Abstract**: In this work, we introduce a deep learning-based polar code construction algorithm. The core idea is to represent the information/frozen bit indices of a polar code as a binary vector which can be interpreted as trainable weights of a neural network (NN). For this, we demonstrate how this binary vector can be relaxed to a soft-valued vector, facilitating the learning process through gradient descent and enabling an efficient code construction. We further show how different polar code design constraints (e.g., code rate) can be taken into account by means of careful binary-to-soft and soft-to-binary conversions, along with rate-adjustment after each learning iteration. Besides its conceptual simplicity, this approach benefits from having the “decoder-in-the-toop”, i.e., the nature of the decoder is inherently taken into consideration while learning (designing) the polar code. We show results for belief propagation (BP) decoding over both AWGN and Rayleigh fading channels with considerable performance gains over state-of-the-art construction schemes.

## Pseudocodeword-based Decoding of Quantum Stabilizer Codes

- **Status**: ✅
- **Reason**: 그래프커버 pseudocodeword 기반 SPA 약점 분석·수정 — 양자 부호 대상이나 고전 SPA 일반론 유래이고 BP 디코더 개선 기법이 바이너리 LDPC에 이식 가능(C, 애매하면 in)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8849833
- **Type**: conference
- **Published**: 2019
- **Authors**: J. X. Li, P. O. Vontobel
- **PDF**: https://ieeexplore.ieee.org/document/8849833
- **Abstract**: It has been shown that graph-cover pseudocodewords can be used to characterize the behavior of sum-product algorithm (SPA) decoding of classical codes. In this paper, we leverage and adapt these results to analyze SPA decoding of quantum stabilizer codes. We use the obtained insights to formulate modifications to the SPA that overcome some of its weaknesses.

## Long-Term JPEG Data Protection and Recovery for NAND Flash-Based Solid-State Storage

- **Status**: ✅
- **Reason**: NAND 플래시 3D TLC retention 데이터 보호/복구 — 카테고리 A 직접 해당
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8890138
- **Type**: conference
- **Published**: 2019
- **Authors**: Y. -C. Kuo, R. -F. Chiu, R. -S. Liu
- **PDF**: https://ieeexplore.ieee.org/document/8890138
- **Abstract**: NAND flash memory is widely used in solid-state storage including SD cards and eMMC chips, in which JPEG pictures are one of the most valuable data. In this work, we study NAND flash memory-aware, long-term JPEG data protection and recovery. Our goal is to increase the robustness of JPEG files stored in flash-based storage and rescue JPEG files that are corrupted due to long-term retention. JPEG files with our proposed protection techniques are compatible with existing JPEG viewers. We conduct real-system experiments by storing JPEG files on 16 nm, 3-bit-per-cell flash chips and let the JPEG files undergo a retention process equivalent to ten years at 25 degrees Celsius. Experimental results show that the proposed techniques can rescue corrupted JPEG files to achieve a PSNR improvement of up to 23.5 dB.

## Learning to Decode Polar Codes with Quantized LLRs Passing

- **Status**: ✅
- **Reason**: 양자화 LLR(3-bit) NN 가중 디코딩 — polar용이나 양자화 LLR+NN 가중치 기법이 바이너리 LDPC BP에 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8904378
- **Type**: conference
- **Published**: 2019
- **Authors**: J. Gao, J. Dai, K. Niu
- **PDF**: https://ieeexplore.ieee.org/document/8904378
- **Abstract**: In this paper, a weighted successive cancellation (WSC) algorithm is proposed to improve the decoding performance of polar codes with the quantized log-likelihood ratio (LLR). The weights used in the WSC are automatically learned by a neural network (NN). A novel NN model and its simplified architecture are build to select the optimal weights of the WSC, and all-zero codewords can train the NN. Besides, we impose the constraints on weights to direct the learning process. The small number of trainable parameters lead to faster learning without performance loss. Simulation results show that the WSC algorithm is valid to various codewords and the trained weights make it outperform SC algorithm with the same quantization precision. Notably, the WSC with 3-bit quantization precision achieves a near floating point performance for short length.

## Deep Learning-Based Quantization of L-Values for Gray-Coded Modulation

- **Status**: ✅
- **Reason**: 딥러닝 기반 LLR(L-value) 양자화·메모리 저장 기법 — NAND LDPC LLR 양자화에 직접 이식 가능(A/C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9024547
- **Type**: conference
- **Published**: 2019
- **Authors**: M. Arvinte, S. Vishwanath, A. H. Tewfik
- **PDF**: https://ieeexplore.ieee.org/document/9024547
- **Abstract**: In this work, a deep learning-based quantization scheme for log-likelihood ratio (L-value) storage in fading channels affected by interference is introduced. We derive the number of sufficient statistics required to exactly reconstruct the set of L-values corresponding to a channel use as 3+2xNI, where NI is the number of interferers. We analyze the dependency between the average magnitudes of different L-values and show they follow a consistent ordering, regardless of the channel coefficient or interference distribution. Based on this we design a deep autoencoder that jointly compresses and separately reconstructs each L-value, allowing the use of a weighted loss function that promotes more accurate reconstruction of low magnitude inputs. Our method is shown to be competitive with state-of- the-art maximum mutual information quantization schemes, reducing the required memory footprint by a ratio of up to two and achieving a loss of performance lower than 0.1 dB with less than two effective bits per L-value and lower than 0.04 dB with 2.25 effective bits. We demonstrate that the same network can be reused without further training on various channel models and error- correcting codes while preserving the same performance benefits.

## Hamming Distance Distribution of the 0-reprocessing Estimate of the Ordered Statistic Decoder

- **Status**: ✅
- **Reason**: OSD(순서통계디코딩) 통계기반 효율화 알고리즘 — 부호 비의존적 디코더로 카테고리 C(OSD) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8849229
- **Type**: conference
- **Published**: 2019
- **Authors**: C. Yue, M. Shirvanimoghaddam, Y. Li +1
- **PDF**: https://ieeexplore.ieee.org/document/8849229
- **Abstract**: In this paper, we derive the distribution of the Hamming distance at 0-reprocessing of the ordered statistics decoding (OSD). With the assumption of decoding a random linear block code, we first find the distribution of the number of errors in any partition of the ordered channel output sequence. Then the distribution of the Hamming distance after 0-reprocessing is derived by a mixture model of two random variables. Based on the proposed statistical approach, we outline the design of high-efficiency OSD algorithm. Simulation and numerical results show that our proposed statistical approaches accurately describe the Hamming distance distributions in OSD decoding process.

## A Novel Recovery Data Technique on MLC NAND Flash Memory

- **Status**: ✅
- **Reason**: NAND MLC 플래시 ECC/FTL 파워로스 복구 — 카테고리 A NAND 직접
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8919382
- **Type**: conference
- **Published**: 2019
- **Authors**: T. V. Dai, J. Park, D. -J. Park
- **PDF**: https://ieeexplore.ieee.org/document/8919382
- **Abstract**: Flash memory today is more popular because of its advantages, such as low power consumption, high mobility and fast data access. In NAND flash memory, a solution called Flash Translation Layer (FTL) was proposed to solve its disadvantages like erase-before-write and unsymmetrical read or write response time. During the process of using the data, the data might be lost on the power failure in the systems. In some systems, the data is very important. Hence, recovery of data in the event of the system crash or a sudden power outage is of prime importance. One of the methods to fix is the error code correction (ECC), supplied with the flash device by the manufacturer. In the process of power off failure recovery, there have been previous schemes such as In-Page Backup, In-Block Backup, Hybrid Backup, A-PLR (Accumulation based Power Loss Recovery), HYFLUR (Hybrid FLUsh Recovery), and C-HYFLUR (Compression scheme for HYFLUR). In this paper, we introduce a technique based on the page leveling mapping using the spare area in FTL divided into ECC, map information, and reserved. To estimate the performance of this technique, we compare the recovery time and mapping information management cost of our approach with those of previous schemes such as In-Block Backup and In-Page Backup.

## Hardware Implementation Aspects of a Syndrome-based Neural Network Decoder for BCH Codes

- **Status**: ✅
- **Reason**: 신경망 디코더 HW 구현+pruning/8-bit 양자화 — BCH용이나 NN 디코더 압축/HW 기법이 LDPC 신경망 디코더에 이식 가능(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8906946
- **Type**: conference
- **Published**: 2019
- **Authors**: E. Kavvousanos, V. Paliouras
- **PDF**: https://ieeexplore.ieee.org/document/8906946
- **Abstract**: Deep-Learning-based Decoders have been recently introduced for use with short-length codes. They have been found to act as a Soft-Decision-Decoding method achieving near Maximum-Likelihood error correcting capability. However, Deep-Learning decoding methods are hard to implement as they normally require millions of operations for inference. In order for Deep-Learning decoding to be a competitive candidate for practical applications, research effort is required to reduce the computational complexity and storage requirements of the Neural Networks involved. In this work, a structured flow is presented that significantly compresses a trained Syndrome-Based Neural Network Decoder by pruning up to 80% of the network's weights and quantizing them to 8-bit fixed-point representation, with no loss in its BER performance. The attained compressed Neural Network can then be used for inference, by designing specific hardware or by using a generic Deep-Learning hardware accelerator that exploits the compressed structure of the network. The deployment of the DL Decoder in an embedded application is showcased, using the AI Edge platform by Xilinx. To accomplish this, a simple method to obtain a computationally equivalent convolutional layer from a fully-connected one is introduced. Implementation results are provided for the compressed DL Decoder, regarding throughput rate and BER performance. To our knowledge, this is the first DL decoder in hardware reported.

## The Method of Predicting Retention Threshold Voltage Distribution for NAND Flash Memory Based on Back-Propagation Neural Network

- **Status**: ✅
- **Reason**: 3D TLC/QLC NAND retention Vth 분포 예측(BpNN)으로 read voltage 최적화→soft-decision LLR 개선, 카테고리 A 직접 해당
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8739277
- **Type**: conference
- **Published**: 2019
- **Authors**: K. Wang, G. Du, Z. Lun +1
- **PDF**: https://ieeexplore.ieee.org/document/8739277
- **Abstract**: A new retention threshold voltage (Vth) distributions prediction method for 3-D TLC and QLC NAND flash memories based on back-propagation neural network (BpNN) is proposed. The data pre-processing and post-processing techniques are developed to improve the prediction accuracy of BpNN model. Based on our proposed BpNN model, the predicted Vth distributions after different data retention times (t) and program/erase (P/E) cycles have good agreement with the measurements, which can be used for read voltage optimization (RVO) not only hard-decision decoding algorithm but also soft-decision decoding algorithm. Especially, this BpNN model can be embedded into the SSD controller and help in improving the reliability of NAND flash memory.

## TDMR Detection System with Local Area Influence Probabilistic a Priori Detector

- **Status**: ✅
- **Reason**: TDMR 자기기록 검출기가 채널 디코더에 LLR 전달(turbo equalization)구조; 스토리지·soft LLR 체인 이식 가능성 애매 → 살림(Phase 3 재검토)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8761903
- **Type**: conference
- **Published**: 2019
- **Authors**: J. Shen, X. Sun, K. Sivakumar +3
- **PDF**: https://ieeexplore.ieee.org/document/8761903
- **Abstract**: We propose a three-track detection system for two dimensional magnetic recording (TDMR) in which a local area influence probabilistic (LAIP) detector works with a trellis-based Bahl-Cocke-Jelinek-Raviv (BCJR) detector to remove intersymbol interference (ISI) and intertrack interference (ITI) among coded data bits as well as media noise due to magnetic grain-bit interactions. Two minimum mean-squared error (MMSE) linear equalizers with different response targets are employed before the LAIP and BCJR detectors. The LAIP detector considers local grain-bit interactions and passes coded bit log-likelihood ratios (LLRs) to the channel decoder, whose output LLRs serve as a priori information to the BCJR detector, which is followed by a second channel decoding pass. Simulation results under 1-shot decoding on a grain-flipping-probability (GFP) media model show that the proposed LAIP/BCJR detection system achieves density gains of 10.16% for center-track detection and 3.13% for three-track detection compared to a standard BCJR/1D-PDNP. The proposed system's BCJR detector bit error rates (BERs) are lower than those of a recently proposed two-track BCJR/2D-PDNP system by factors of (0.55, 0.08) for tracks 1 and 2 respectively.

## A Study on Replica Generation Using LUT Based on Information Bottleneck for MF-GaBP in Massive MIMO Detection

- **Status**: ✅
- **Reason**: IB(정보병목) 기반 LUT 양자화 메시지패싱(MF-GaBP)+sIB 임계 설계는 NAND LDPC LLR/메시지 양자화 LUT 디코더로 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8891317
- **Type**: conference
- **Published**: 2019
- **Authors**: L. Wang, T. Takahashi, S. Ibi +1
- **PDF**: https://ieeexplore.ieee.org/document/8891317
- **Abstract**: This paper proposes a symbol replica generation method using look-up table (LUT) based on the information bottleneck (IB) theory in matched filter Gaussian belief propagation (MF-GaBP) for massive multi-input multi-output (MIMO) detection. MF-GaBP serves as an iterative signal detection scheme with low computational complexity by utilizing massive MIMO simplification owing to the law of large numbers. However, when the internal mathematical processes in MF-GaBP are conducted in double precision, a severe processing delay is inevitable. To avoid the impairment, we propose a quantized MF-GaBP detection scheme using predesigned LUTs. The quantization threshold is designed based on the sequential IB (sIB) method for minimizing the mutual information loss. Finally, computer simulations demonstrate that the proposed method significantly reduces the memory occupancy on the basis of table-based processing while suppressing error floor level of the bit error rate (BER) performance.

## MIND: Model Independent Neural Decoder

- **Status**: ✅
- **Reason**: 신경망 디코더 MAML 빠른 채널적응 — 부호 비의존적 적응기법으로 LDPC 신경망 디코더(C)에 이식 가능성, 애매하여 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8815537
- **Type**: conference
- **Published**: 2019
- **Authors**: Y. Jiang, H. Kim, H. Asnani +1
- **PDF**: https://ieeexplore.ieee.org/document/8815537
- **Abstract**: Standard decoding approaches rely on model-based channel estimation methods to compensate for varying channel effects, which degrade in performance whenever there is a model mismatch. Recently proposed Deep learning based neural decoders address this problem by leveraging a model-free approach via gradient-based training. However, they require large amounts of data to retrain to achieve the desired adaptivity, which becomes intractable in practical systems. In this paper, we propose a new decoder: Model Independent Neural Decoder (MIND), which builds on the top of neural decoders and equips them with a fast adaptation capability to varying channels. This feature is achieved via the methodology of Model-Agnostic Meta-Learning (MAML). Here the decoder: (a) learns a ‘good’ parameter initialization in the meta-training stage where the model is exposed to a set of archetypal channels and (b) updates the parameter with respect to the observed channel in the meta-testing phase using minimal adaptation data and pilot bits. Building on top of existing state-of-the-art neural Convolutional and Turbo decoders, MIND outperforms the static benchmarks by a large margin and shows minimal performance gap when compared to the neural (Convolutional or Turbo) decoders designed for that particular channel. In addition, MIND also shows strong learning capability for channels not exposed during the meta training phase.

## On the Capacity of the Flash Memory Channel with Inter-cell Interference

- **Status**: ✅
- **Reason**: NAND 플래시 ICI 채널 용량/상호정보 — A(NAND 직접) 채널 모델, LLR/코드설계 참고 가능
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:8849822
- **Type**: conference
- **Published**: 2019
- **Authors**: Y. Li, G. Han, P. H. Siegel
- **PDF**: https://ieeexplore.ieee.org/document/8849822
- **Abstract**: In this paper, we consider a discrete channel with inter-cell interference (ICI) as a model for NAND flash memory. We derive an explicit formula for the mutual information rate when the input is Markovian. Using this formula, we obtain the asymptotics of the channel capacity in the high signal-to-noise (SNR) regime.

## A User-Independent Successive Interference Cancellation Based Coding Scheme for the Unsourced Random Access Gaussian Channel

- **Status**: ✅
- **Reason**: unsourced random access에 LDPC + joint message passing 디코더 사용, T-user adder channel용 MP 디코더 기법이 떼어낼 여지(애매, Phase 3 재검토)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8830448
- **Type**: journal
- **Published**: 2019
- **Authors**: A. Vem, K. R. Narayanan, J. -F. Chamberland +1
- **PDF**: https://ieeexplore.ieee.org/document/8830448
- **Abstract**: This work introduces a novel coding paradigm for the unsourced multiple access channel model. The envisioned framework builds on a select few key components. First, the transmission period is partitioned into a sequence of sub-blocks, thereby yielding a slotted structure. Second, messages are split into two parts. A portion of the data is encoded using spreading sequences or codewords that are designed to be recovered by a compressed sensing type decoder. In addition to being an integral part of the data, the information bits associated with this first part also determine the parameters of the low-density parity check code employed during the subsequent stages of the communication process. The other portion of the message is encoded using the aforementioned low-density parity check code. The data embedded in this latter stage is decoded using a joint message passing algorithm designed for the T-user binary input real adder channel. Finally, devices repeat their codeword in multiple sub-blocks, with the transmission pattern being a deterministic function of message content independent of the identity of the device. When combined with successive interference cancellation, the ensuing communication infrastructure offers significant performance improvement compared to coding schemes recently published in the literature for unsourced random access.

## Decoding Binary Linear Codes Using Penalty Dual Decomposition Method

- **Status**: ✅
- **Reason**: PDD 기반 이진 선형부호 ML 디코딩 알고리즘 — 부호 비의존적 메시지패싱/최적화 기법으로 바이너리 LDPC BP에 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8691508
- **Type**: journal
- **Published**: 2019
- **Authors**: M. -M. Zhao, Q. Shi, Y. Cai +2
- **PDF**: https://ieeexplore.ieee.org/document/8691508
- **Abstract**: In this letter, we utilize the penalty dual decomposition (PDD) framework and develop a novel PDD decoding algorithm for binary linear codes. Instead of relaxing the discrete constraints to continuous ones, we take an alternative by transforming them into equivalent equality constraints. This idea leads to a double-loop parallel algorithm: In the outer loop, we update the dual variables and certain penalty parameters, while in the inner loop, we divide the primal variables into several blocks and employ the block successive upper-bound minimization method to iteratively optimize each block variable in closed form. Every limit point generated by the proposed algorithm is guaranteed to be a stationary point of the maximum likelihood decoding problem. Simulation results demonstrate that the proposed algorithm shows great error rate performance at both low and high signal-to-noise ratios.

## A Low-Complexity Belief Propagation Based Decoding Scheme for Polar Codes - Decodability Detection and Early Stopping Prediction

- **Status**: ✅
- **Reason**: 폴라 BP 조기종료 예측/디코더빌리티 검출 — 부호 비의존적 BP 종료기법일 수 있어 이식성 검토차 살림(Phase3)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8888244
- **Type**: journal
- **Published**: 2019
- **Authors**: Y. Wang, S. Zhang, C. Zhang +2
- **PDF**: https://ieeexplore.ieee.org/document/8888244
- **Abstract**: In the 5G communication systems, polar code has been adapted as the control channel coding solution in the enhanced mobile broadband (eMBB) scenario. Although different decoding schemes, including belief propagation (BP) and successive cancellation (SC) based algorithms, have been proposed, the decoding complexity as well as the latency are still significant. To address this critical issue, several low-complexity schemes, e.g., the use of simplified decoding operation and stop the decoding operation in earlier stage, have been proposed recently. However, conventional early stopping strategies have to check a pre-defined metric in each iteration, and the associated decoding delay is significant. In this paper, to address this challenge, we proposed a low-complexity BP based decoding scheme, which contains the decodability detection stage and the early stopping prediction stage. The decodability detection stage can identify the codewords in the deep channel fading environment and eliminate the unnecessary decoding operations to reduce the decoding complexity, while the early stopping prediction stage can directly predict the required number of iterations rather than checking the metric in each iteration to avoid the associated decoding delay. Through the above two approaches, our proposed scheme is shown to achieve 71% decoding delay reduction and maintain the same decoding performance as traditional BP, G-matrix, MinLLR schemes.

## Cell-State-Distribution-Assisted Threshold Voltage Detector for NAND Flash Memory

- **Status**: ✅
- **Reason**: NAND 플래시 read reference voltage 최적화(CSD-TVD) — 카테고리 A 직접 해당(threshold voltage detection, retention)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8648493
- **Type**: journal
- **Published**: 2019
- **Authors**: Z. Fan, G. Cai, G. Han +2
- **PDF**: https://ieeexplore.ieee.org/document/8648493
- **Abstract**: The process scaling as well as the multi-level cell technology greatly increase the storage density of NAND flash memory. Unfortunately, the high-density flash memory suffers from severe noise such that its performance will be dramatically deteriorated. In this letter, we propose a cell-state-distribution-assisted threshold voltage detection (CSD-TVD) to optimize read reference voltages. Specifically, the proposed detection method exploits the variation of a number of cells within each sub-window of the overlap region to detect the voltage shift and analyze its distribution. Afterward, the mean of the voltage-shift distribution is viewed as the optimal voltage shift, which is used to boost the accuracy of the read reference voltage. Based on the retention characteristics, we also conceive a novel low-latency (LL) CSD-TVD to reduce the detection range of the CSD-TVD. The experimental results demonstrate that the proposed CSD-TVD and LL-CSD-TVD achieve better error performance than the state-of-the-art retention-optimized-reading (ROR) and nonuniform detection methods. In addition, the LL-CSD-TVD significantly reduces the read latency with respect to the CSD-TVD and ROR.

## Low-Latency Adaptive Ordered Statistic Decoding of Polar Codes

- **Status**: ✅
- **Reason**: OSD(ordered statistic decoding)는 포함 카테고리 C에 명시된 이식 가능 디코더, 병렬화/저지연 기법 일부 이식 여지(애매, Phase 3 재검토)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8831380
- **Type**: journal
- **Published**: 2019
- **Authors**: K. Qin, Z. Zhang
- **PDF**: https://ieeexplore.ieee.org/document/8831380
- **Abstract**: Deploying polar codes in ultra-reliable low-latency communication (URLLC) is of critical importance and is currently receiving tremendous attention in both academia and industry. However, most of the state of the art polar codes decoders like progressive bit-flipping decoder (PBF) and successive cancellation list (SCL) decoder, involve strong data dependencies and suffer from huge decoding delay. This contradicts the low-latency requirement in URLLC. To address such issue, this paper appeals to the parallel computing and proposes an adaptive ordered statistic decoder (OSD). In particular, we first propose a novel codeword searching metric which proves to be hardware-friendly, and an adaptive OSD algorithm is then developed to adaptively rule out the unpromising codewords, thus significantly reducing the latency. Secondly, to further reduce the computational complexity of the proposed algorithm, we decompose the current code sequence into several independent subcodes, and by handling these subcodes with concatenated adaptive OSDs, a good trade-off between decoding latency and complexity can be achieved. Finally, numerical results show that the proposed adaptive OSD outperforms the conventional decoders in terms of block error rate (BLER) and decoding latency.

## Investigation of Retention Noise for 3-D TLC NAND Flash Memory

- **Status**: ✅
- **Reason**: 3D TLC NAND retention noise/Vth 분포 모델링 — A NAND 직접, LLR/리텐션 보정에 활용
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8579606
- **Type**: journal
- **Published**: 2019
- **Authors**: K. Wang, G. Du, Z. Lun +1
- **PDF**: https://ieeexplore.ieee.org/document/8579606
- **Abstract**: In this paper, the retention noise [electron emission statistics (EES)] after program operation of 3-D triple-level program cell (TLC) NAND flash memory is investigated. Three main noise sources, consisting of essential EES (EEES), electron numbers fluctuation, and device parameters fluctuation to broaden the retention Vth distributions are comprehensively considered, and the corresponding analytic models are developed. The impact of device parameters fluctuation is relatively larger than EEES and electron numbers fluctuation for our measured 3-D TLC NAND flash memory devices. Using the proposed models, the calculated Vth distributions after different data retention times have good agreements with the measurements, which validate our proposed models. This paper provides a method to predict the Vth distributions accurately and efficiently, and can help in improving reliability of 3-D TLC and quad-level program cell NAND flash memory.

## Reliability Variance based Weighted Bit Flipping Algorithms for LDPC

- **Status**: ✅
- **Reason**: 수신값 분산 기반 가중 비트플리핑(WBF) 변형 알고리즘 — 이식 가능 LDPC 디코더(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8776988
- **Type**: conference
- **Published**: 10-11 Jan.
- **Authors**: D. Harita, K. Parguna Rajan
- **PDF**: https://ieeexplore.ieee.org/document/8776988
- **Abstract**: Low density parity check codes is decoded by bit flipping algorithm and sum product algorithm. Bit flipping algorithm has low complexity and poor performance. To achieve trade-off between performance and complexity weights of the inversion function modified by using variance of the received values. These modifications improve performance with mild increase in the computations. It decreases in average number of iterations for maintaining high reliability and higher speed decoding.

## Optimization of QC-LDPC Codes by Edge Exchange Method Based on ACE

- **Status**: ✅
- **Reason**: QC-LDPC error floor 개선 위한 신규 EEA(edge exchange/ACE+girth) 코드설계 기법, 바이너리, E 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8756119
- **Type**: journal
- **Published**: 1 Sept.1, 
- **Authors**: Xin Qin, Chuanchuan Yang, Ziyuan Zheng +1
- **PDF**: https://ieeexplore.ieee.org/document/8756119
- **Abstract**: Long quasi-cyclic low-density parity check (QC-LDPC) codes have been chosen as one of the forward error correction (FEC) schemes in passive optical network (PON) systems benefiting from the excellent performance. About how to get the appropriate LDPC codes, some traditional methods which focus on obtaining large girth or flat approximated cycle extrinsic message degree (ACE) spectrums are proposed for the design of LDPC codes. These methods which may still make the existence of small stopping sets containing short cycles probably are not so useful for long QC-LDPC codes. Recently, the parallel vector message passing (PMP) algorithm oriented-to decreasing the number of short cycles is proved to be an effective method to optimize LDPC codes. Since ignoring short cycles with poor connectivity which can induce error floor, this method cannot guarantee its effectiveness for long QC-LDPC codes. In this letter, an edge exchange optimization method based on the global properties of ACE and girth called EEA method is proposed, which tries to reduce cycles with low ACE in the order of cycle length. The numerical results prove that our EEA method can bring the improvements of error floor up to two orders of magnitude to long QC-LDPC codes and obviously outperforms PMP algorithm.

## Hardware-Based Linear Program Decoding With the Alternating Direction Method of Multipliers

- **Status**: ✅
- **Reason**: ADMM-LP 디코딩 FPGA HW 구현(바이너리 선형부호, 스토리지 지향), 신규 디코더+HW 아키텍처 C/D 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8768221
- **Type**: journal
- **Published**: 1 Oct.1, 2
- **Authors**: Mitchell Wasson, Mario Milicevic, Stark C. Draper +1
- **PDF**: https://ieeexplore.ieee.org/document/8768221
- **Abstract**: We present a hardware-based implementation of linear program (LP) decoding for binary linear codes. LP decoding frames error–correction as an optimization problem. In contrast, variants of belief propagation (BP) decoding frame error–correction as a problem of graphical inference. LP decoding has several advantages over BP-based methods, including convergence guarantees and better error-rate performance in high-reliability channels. The latter makes LP decoding attractive for optical transport and storage applications. However, LP decoding, when implemented with general solvers, does not scale to large blocklengths and is not suitable for a parallelized implementation in hardware. It has been recently shown that the alternating direction method of multipliers (ADMM) can be applied to decompose the LP decoding problem. The result is a message-passing algorithm with a structure very similar to BP. We present modifications to this algorithm, resulting in a more intuitive and hardware-compatible form. This is particularly true for projection onto the parity polytope: the major computational primitive for ADMM-LP decoding. Furthermore, we present results for a fixed-point Verilog implementation of ADMM-LP decoding. This implementation targets a field-programmable gate array (FPGA) platform to evaluate error-rate performance and estimate resource usage. We show that frame error rate performance well within 0.5 dB of double-precision implementations is possible with 10-bit messages. Finally, we outline research opportunities that should be explored en route to an application-specific integrated circuit (ASIC) implementation that is capable of Gigabit-per-second throughput.

## Joint Decoder Design for SSDs

- **Status**: ✅
- **Reason**: NAND SSD ECC/RAID 중복정보 활용 joint decoder 제안, A 카테고리 직접 해당
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8668457
- **Type**: journal
- **Published**: 1 May1, 20
- **Authors**: Qing Li
- **PDF**: https://ieeexplore.ieee.org/document/8668457
- **Abstract**: Error-correction codes (ECC) and redundant array of independent disks (RAID) are commonly used to protect NAND-based solid state drives (SSD) from serious noise/disturb. In order to tolerate more errors, common solutions are more complex ECCs and RAIDs. Meanwhile, due to the error-correction mechanisms and flash translation layer, NAND-based SSDs inevitably generate abundant redundant information. The theme of this paper is to show that instead of designing new error correction mechanisms from scratch, the NAND-based SSD reliability can be greatly improved by utilizing current decoders to explore the inherent information between redundant pages. We first propose a joint decoder to recover multiple pages by utilizing redundant pages within a stripe of ECC/RAID, and then we consider a joint decoder to recover multiple pages by utilizing write-amplified (WA) pages. The simulation results show that with the proposed algorithm, a performance gain of as much as 1.8 dB can be obtained. The theoretical study reveals that the joint decoding model can be studied from the perspective of relay channel model, and this helps to explore how much information can be reliably stored with the RAID/WA system in SSD.

## LDPC Soft Decoding with Improved Performance in 1X-2X MLC and TLC NAND Flash-Based Solid State Drives

- **Status**: ✅
- **Reason**: NAND MLC/TLC SSD LDPC 소프트 디코딩 최적화 + NAND 칩 HW 자원 활용 (A+D 직접 해당)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7887724
- **Type**: journal
- **Published**: 1 July-Sep
- **Authors**: Lorenzo Zuolo, Cristian Zambelli, Alessia Marelli +2
- **PDF**: https://ieeexplore.ieee.org/document/7887724
- **Abstract**: The reliability of non-volatile NAND flash memories is reaching critical levels for traditional error detection and correction. Therefore, to ensure data trustworthiness in nowadays NAND flash-based Solid State Drives, it is essential to exploit powerful correction algorithms such as the Low Density Parity Check. However, the burdens of this approach materialize in a disk performance reduction. In this work a standard decoding approach is compared with an optimized solution exploiting hardware resources available in NAND flash chips. The simulation results on 2X, 1X and mid-1X MLC and TLC NAND flash-based Solid State Drives in terms of disk bandwidth, average latency, and Quality of Service favor the adoption of the presented solution in different host scenarios and realistic workloads. The proposed solution is particularly effective when high error correction interventions and read- or write-intensive workloads are considered.

## One and Two Bit Message Passing for SC-LDPC Codes With Higher-Order Modulation

- **Status**: ✅
- **Reason**: 바이너리 SC-LDPC BP용 1/2비트 양자화 메시지패싱 신규 QMP 알고리즘, NAND LLR 양자화에 이식 가능 (C+E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8847350
- **Type**: journal
- **Published**: 1 Dec.1, 2
- **Authors**: Fabian Steiner, Emna Ben Yacoub, Balázs Matuz +2
- **PDF**: https://ieeexplore.ieee.org/document/8847350
- **Abstract**: Low complexity decoding algorithms are necessary to meet data rate requirements in excess of 1 Tbps. In this paper, we study one and two bit message passing algorithms for belief propagation decoding of low-density parity-check (LDPC) codes and analyze them by density evolution. The variable nodes (VNs) exploit soft information from the channel output. To decrease the data flow, the messages exchanged between check nodes (CNs) and VNs are represented by one or two bits. The newly proposed quaternary message passing (QMP) algorithm is compared asymptotically and in finite length simulations to binary message passing (BMP) and ternary message passing (TMP) for spectrally efficient communication with higher-order modulation and probabilistic amplitude shaping (PAS). To showcase the potential for high throughput forward error correction, spatially coupled LDPC codes and a target spectral efficiency (SE) of 3 bits/QAM symbol are considered. Gains of about 0.7 dB and 0.1 dB are observed compared to BMP and TMP, respectively. The gap to unquantized belief propagation (BP) decoding is reduced to about 0.75 dB. For smaller code rates, the gain of QMP compared to TMP is more pronounced and amounts to 0.24 dB in the considered example.
