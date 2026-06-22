# IEEE Xplore — 2022-07 (1차선별 통과)


## A Novel Base Graph Based Static Scheduling Scheme for Layered Decoding of 5G LDPC Codes

- **Status**: ✅
- **Reason**: QC-LDPC 레이어드 디코딩의 새 정적 스케줄링(BGSS) 기법 — 5G 응용이나 디코더 스케줄링 자체가 NAND QC-LDPC 디코더로 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9765969
- **Type**: journal
- **Published**: July 2022
- **Authors**: Kuangda Tian, Hao Wang
- **PDF**: https://ieeexplore.ieee.org/document/9765969
- **Abstract**: Quasi-cyclic low-density parity-check (QC-LDPC) codes have been selected as the channel coding scheme for 5G new radio (NR) data channel. In this letter, a novel base graph based static scheduling (BGSS) method is proposed for layered decoding of 5G LDPC codes to accelerate decoding convergence and reduce the average number of iterations (ANI). In the proposed BGSS method, the update order of layers is determined based on row weight, column weight and number of punctured non-zero elements of BG matrix. Three optimization rules are included in BGSS to determine the order: 1) The layer with less punctured non-zero element is updated firstly. 2) The layer with relatively small row weight is updated firstly. 3) The layer which can utilize more recent information is updated firstly. The first rule has the highest priority and the third rule has the lowest priority. Simulation results show that compared with other scheduling method, the proposed method reduces about 1.1 ANI and obtains about 0.05dB performance gain for given LDPC codes.

## Generalized Mutual Information-Maximizing Quantized Decoding of LDPC Codes With Layered Scheduling

- **Status**: ✅
- **Reason**: MIM 양자화 디코딩(MIM-DE LUT 구성, min-sum/BP 기반, 레이어드 스케줄링) — NAND LLR 양자화·min-sum 변형에 직접 이식 가능한 새 디코더 기법(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9743741
- **Type**: journal
- **Published**: July 2022
- **Authors**: Peng Kang, Kui Cai, Xuan He +2
- **PDF**: https://ieeexplore.ieee.org/document/9743741
- **Abstract**: In this paper, we propose a framework of the mutual information-maximizing (MIM) quantized decoding for low-density parity-check (LDPC) codes by using simple mappings and fixed-point additions. Our decoding method is generic in the sense that it can be applied to LDPC codes with arbitrary degree distributions, and can be implemented based on either the belief propagation (BP) algorithm or the min-sum (MS) algorithm. In particular, we propose the MIM density evolution (MIM-DE) to construct the lookup tables (LUTs) for the node updates. The computational complexity and memory requirements are discussed and compared to the LUT decoder variants. For applications with low-latency requirement, we consider the layered schedule to accelerate the convergence speed of decoding quasi-cyclic LDPC codes. In particular, we develop the layered MIM-DE to design the LUTs based on the MS algorithm, leading to the MIM layered quantized MS (MIM-LQMS) decoder. An optimization method is further introduced to reduce the memory requirement for storing the LUTs. Simulation results show that the MIM quantized decoders outperform the state-of-the-art LUT decoders in the waterfall region with both 3-bit and 4-bit precision over the additive white Gaussian noise channels. For small decoding iterations, the MIM quantized decoders also achieve a faster convergence speed compared to the benchmarks. Moreover, the 4-bit MIM-LQMS decoder can approach the error performance of the floating-point layered BP decoder within 0.3 dB in the moderate-to-high SNR regions, over both the AWGN channels and the fast fading channels.

## Design of Lookup-Table (LUT) Decoder for Protograph-Based Low-Density Parity-Check (LDPC) codes

- **Status**: ✅
- **Reason**: protograph LDPC용 LUT 디코더 설계(parallel edge/degree-1/punctured 지원, 2-4bit 양자화) — 이식 가능 디코더 알고리즘(C), 양자화 NAND LLR과 연관
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9895041
- **Type**: conference
- **Published**: 5-8 July 2
- **Authors**: Chatuporn Duangthong, Watid Phakphisut
- **PDF**: https://ieeexplore.ieee.org/document/9895041
- **Abstract**: The Belief-propagation (BP) algorithm is a powerful decoder for LDPC codes. However, the BP algorithm requires the high complexity of the check node operation. Therefore, in the previous works, a lookup table (LUT)-based decoder has been proposed for LDPC codes. In this work, we propose the LUT design for protograph LDPC codes. Our LUT design can support the parallel edge, variable node with degree-1 and punctured variable node. As a result, the coding losses of 2-, 3- and 4-bit quantization of LUT decoder are 1.6, 0.5 and 0.1 dB compared to BP algorithm.

## Finite-Alphabet Message Passing using only Integer Operations for Highly Parallel LDPC Decoders

- **Status**: ✅
- **Reason**: C/D: 정수 연산만 쓰는 유한 알파벳 메시지패싱 디코더(mLUT/MIC), min-sum 대비 면적·에너지 개선 - 바이너리 LDPC 디코더+HW 신규 기여
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9833953
- **Type**: conference
- **Published**: 4-6 July 2
- **Authors**: Tobias Monsees, Dirk Wübben, Armin Dekorsy +3
- **PDF**: https://ieeexplore.ieee.org/document/9833953
- **Abstract**: In this paper, we present a new design of Finite Alphabet (FA) Message Passing (MP) decoders using only integer operations. We utilize Discrete Density Evolution with a multidimensional Lookup-Table (mLUT) design for Variable Node (VN) updates to consider all input messages jointly for reducing the information loss compared to the frequent sequential LUT design approaches. From this mLUT design, we derive a minimum-integer computation (MIC) decoder that allows for different bit-widths for node operations and message exchanges between nodes. The mLUT operations for VN updates are replaced by low complexity signed integer additions and threshold operations, and the Check Node (CN) updates simplify to a minimum search over integers. For a (816,406) regular LDPC code, we show that our 3-bit MIC decoder achieves the communication performance of the corresponding mLUT decoder and outperforms a 4-bit state-of-the-art Min-Sum (MS) decoder. We show that the node implementations on a 22 nm FD-SOI technology yield an improved area and energy efficiency over the respective MS implementation. To the best of our knowledge, this is the first time that an implementation improvement for the VNs and CNs is shown when using FA MP.

## High-Throughput VLSI Architecture for LDPC Decoder Based on Low-Latency Decoding Technique for Wireless Communication Systems

- **Status**: ✅
- **Reason**: D: min-sum 기반 저지연 디코딩 기법+병렬 VLSI 아키텍처(컬럼 슬라이스 의존성 완화) - 이식 가능 HW 신규 기여
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:9912041
- **Type**: conference
- **Published**: 4-6 July 2
- **Authors**: Kumari Suravi, Rahul Shrestha
- **PDF**: https://ieeexplore.ieee.org/document/9912041
- **Abstract**: This paper proposes hardware-friendly and low-latency technique for min-sum based LDPC-decoding algorithm with flooding schedule. It enhances the data independency of LDPC decoding algorithm by mitigating dependency among the column slices. Parallel VLSI-architecture of LDPC decoder based on the proposed decoding algorithm has been presented here. Subsequently, performance analysis of such algorithm in AWGN-channel environment has shown that it delivers adequate BER of 10−5 at 1.2 dB of channel-SNR. Furthermore, ASIC synthesis and post-layout simulation of our design are performed in 130 nm-CMOS technology-node. Thus, it occupies a core area of 6.02 mm2and operates at maximum clock frequency of 217 MHz. The proposed LDPC decoder is capable of delivering a high-throughput of 36 Gbps per iteration. Eventually, aforementioned results are compared with the relevant contemporary works where our design achieved 85.64% higher throughput and 41.02% better energy-efficiency in comparison with the state-of-the-art implementation.

## Trade-Based LDPC Codes

- **Status**: ✅
- **Reason**: block design trade 기반 multi-edge QC-LDPC 패리티검사행렬 구성 — 새 코드설계 기법(E), 바이너리 LDPC, NAND ECC 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9834826
- **Type**: conference
- **Published**: 26 June-1 
- **Authors**: Farzane Amirzade, Daniel Panario, Mohammad-Reza Sadeghi
- **PDF**: https://ieeexplore.ieee.org/document/9834826
- **Abstract**: LDPC codes based on multi-edge protographs potentially have larger minimum distances compared to their counterparts, single-edge protographs. However, considering different features of their Tanner graph, such as short cycles, girth and other graphical structures, is harder than for Tanner graphs from single-edge protographs. Here, we provide a novel approach to construct the parity-check matrix of an LDPC code which is based on trades obtained from block designs. We employ our method to construct multi-edge quasi-cyclic (QC) LDPC codes.We use those trade-based matrices to define base matrices of multi-edge protographs. The construction of exponent matrices corresponding to these base matrices has less complexity than the ones proposed in the literature. We prove that these base matrices result in QC-LDPC codes with smaller lower bounds on the lifting degree than existing ones.

## Using Minors to Construct Generator Matrices for Quasi-Cyclic LDPC Codes

- **Status**: ✅
- **Reason**: QC-LDPC 생성행렬을 minor로 구성하는 새 인코딩 방법 + rank/차원 계산, 바이너리 QC-LDPC 코드설계 기여(E), 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9834862
- **Type**: conference
- **Published**: 26 June-1 
- **Authors**: Roxana Smarandache, Anthony Gómez-Fonseca, David G. M. Mitchell
- **PDF**: https://ieeexplore.ieee.org/document/9834862
- **Abstract**: This paper gives a simple method to construct generator matrices with polynomial entries (and hence offers an alternative encoding method to the one commonly used) for all quasi-cyclic low-density parity-check (QC-LDPC) codes, even for those that are rank deficient. The approach is based on constructing a set of codewords with the desired total rank by using minors of the parity-check matrix. We exemplify the method on several well-known and standard codes. Moreover, we explore the connections between the minors of the parity-check matrix and the known upper bound on minimum distance and provide a method to compute the rank of any parity-check matrix representing a QC-LDPC code, and hence the dimension of the code, by using the minors of the corresponding polynomial parity-check matrix.

## Cycle-Free Windows of SC-LDPC Codes

- **Status**: ✅
- **Reason**: SC-LDPC windowed 디코딩용 cycle-free window code 구성/파라미터 분석 — 사이클 제거·코드 설계 기여(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9834404
- **Type**: conference
- **Published**: 26 June-1 
- **Authors**: Emily McMillon, Christine A. Kelley
- **PDF**: https://ieeexplore.ieee.org/document/9834404
- **Abstract**: In this paper, we define a window code to be the portion of an SC-LDPC code seen by a single iteration of a windowed decoder. We consider the design of SC-LDPC codes for windowed decoding via optimization of the window code. In particular, because iterative decoding is optimal on codes with cycle-free graph representations, we ask fundamental questions about the construction and parameters of cycle-free window codes. Further, we show that it is possible to have an SC-LDPC code with cycles and with cycle-free window codes.

## A Design of Layered Decoding for QC-LDPC Codes Based on Reciprocal Channel Approximation

- **Status**: ✅
- **Reason**: RCA 기반 layered density evolution으로 QC-LDPC layered 디코딩 처리순서 최적화 — 이식 가능 디코더 알고리즘 기여(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9834415
- **Type**: conference
- **Published**: 26 June-1 
- **Authors**: Min Jang, Kyeongyeon Kim, Seho Myung +3
- **PDF**: https://ieeexplore.ieee.org/document/9834415
- **Abstract**: This paper presents an analytically designed layered decoding algorithm for quasi-cyclic low-density parity-check (QC-LDPC) codes in the 5th Generation (5G) New Radio (NR) mobile communication system. First, a layered density evolution (DE) based on reciprocal channel approximation (RCA) is newly developed to accurately reflect the layered decoding operation in the decoder design. Using this technique, a single nested sequence is optimized in a greedy way to configure the processing order for any given number of layers. The error-correction performance is improved by up to 0.15 dB, while the number of iterations is reduced by about one simultaneously.

## Systematic Doping of SC-LDPC Codes

- **Status**: ✅
- **Reason**: SC-LDPC 슬라이딩윈도우 디코딩 error propagation 완화 systematic doping — 바이너리 SC-LDPC 코드설계/인코딩 신규 기여(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9834590
- **Type**: conference
- **Published**: 26 June-1 
- **Authors**: Min Zhu, David G. M. Mitchell, Michael Lentmaier +1
- **PDF**: https://ieeexplore.ieee.org/document/9834590
- **Abstract**: In this paper, we examine variable node (VN) doping to mitigate the error propagation problem in sliding window decoding (SWD) of spatially coupled LDPC (SC-LDPC) codes from the point of view of the encoding process. More specifically, in order to simplify the process of generating an encoded sequence with some number of doped code bits, we propose to employ systematic encoding and to limit doping to systematic bits only. Numerical results show that doping of systematic bits only achieves comparable performance to employing general (nonsystematic) encoding and full doping of all the code bits at each doping position, while benefiting from a much simpler encoding process. We then show that the inherent rate loss due to doping can be reduced by doping only a fraction of the variable nodes at each doping position with only a minor impact on performance.

## On Average Number of Cycles in Finite-Length Spatially Coupled LDPC Codes

- **Status**: ✅
- **Reason**: 유한길이 SC-LDPC 사이클 분포 확률 분석(spatial coupling 사이클 제거) — 바이너리 코드설계/사이클 제거 기법(E) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9834637
- **Type**: conference
- **Published**: 26 June-1 
- **Authors**: Sima Naseri, Ali Dehghan, Amir H. Banihashemi
- **PDF**: https://ieeexplore.ieee.org/document/9834637
- **Abstract**: In this paper, a probabilistic analysis of the cycle distribution of protograph-based spatially coupled low-density parity-check (SC LDPC) codes is presented. In particular, we derive the probability that cycles of specific, but arbitrary, length are broken as a result of spatial coupling with a random spreading matrix in a general edge spreading process. Our results show that the probability of existence of cycles in SC codes is O(1/m), where m is the code memory. This result is independent of the cycle length.

## Capacity Optimality of OAMP in Coded Large Unitarily Invariant Systems

- **Status**: ✅
- **Reason**: OAMP-FEC 결합용 용량달성 부호화 원리로 irregular LDPC 최적화(바이너리) 제시 — 코드 설계 기여로 살림, Phase 3 재검토(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9834360
- **Type**: conference
- **Published**: 26 June-1 
- **Authors**: Lei Liu, Shansuo Liang, Li Ping
- **PDF**: https://ieeexplore.ieee.org/document/9834360
- **Abstract**: This paper investigates a large unitarily invariant system (LUIS) involving a unitarily invariant sensing matrix, an arbitrary fixed signal distribution, and forward error control (FEC) coding. Several area properties are established based on the state evolution of orthogonal approximate message passing (OAMP) in an un-coded LUIS. Under the assumptions that the state evolution for joint OAMP and FEC decoding is correct and the replica method is reliable, we analyze the achievable rate of OAMP. We prove that OAMP reaches the constrained capacity predicted by the replica method of the LUIS with an arbitrary signal distribution based on matched FEC coding. Meanwhile, we elaborate a constrained capacity-achieving coding principle for LUIS, based on which irregular low-density parity-check (LDPC) codes are optimized for binary signaling in the simulation results. We show that OAMP with the optimized codes has significant performance improvement over the un-optimized ones and the well-known Turbo linear MMSE algorithm. For quadrature phase-shift keying (QPSK) modulation, constrained capacity-approaching bit error rate (BER) performances are observed under various channel conditions.

## A Semi Linear State Space Model for Error Floor Estimation of LDPC codes over the AWGN Channel

- **Status**: ✅
- **Reason**: AWGN LDPC error floor 추정용 신규 비선형 상태공간 모델(trapping set) — 바이너리 LDPC error floor 기법(E)으로 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9834504
- **Type**: conference
- **Published**: 26 June-1 
- **Authors**: Ali Farsiabi, Amir H. Banihashemi
- **PDF**: https://ieeexplore.ieee.org/document/9834504
- **Abstract**: In this paper, we propose a novel state-space model to represent the behavior of sum-product algorithm (SPA) in the vicinity of a trapping set (TS) of a low-density parity-check (LDPC) code over the additive white Gaussian noise (AWGN) channel in the error floor region. The proposed model takes into account the non-linear behavior of SPA and dynamically adjusts the operating point of the model in accordance to the statistical properties of TS messages. This is in contrast to the existing linear state-space models which linearly approximate such behavior at around the operating point of zero. Simulation results are provided to demonstrate the higher accuracy of the proposed model in estimating the error floor of LDPC codes compared to the linear state-space model.

## Joint SB/NMS and Genetic Optimization for High Performance LDPC Decoding

- **Status**: ✅
- **Reason**: Segmented Bias/Normalized Min-Sum(SB/NMS) 계층 디코딩 — min-sum 변형 새 디코더 알고리즘(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9851728
- **Type**: conference
- **Published**: 19-22 July
- **Authors**: Junhao Ding, Honghao Shi, Zhiyong Luo
- **PDF**: https://ieeexplore.ieee.org/document/9851728
- **Abstract**: In recent years, many communication standards have adopted the LDPC (Low-Density Parity Check) code due to its excellent error correction performance, but it also induces some problems. For example, the use of 5G in mobile phones dramatically reduces battery life. Therefore, it is particularly significant for LDPC code to design a decoding algorithm that does not increase hardware implementation complexity but has superior error correction performance and iteration speed faster than traditional decoding algorithms. Inspired by several network structures in artificial intelligence, bias is used to improve the performance and robustness of the network. In order to enhance decoding algorithm robustness and accuracy, a method is shown by changing the offset in OMSA to the bias and combining NMSA in the near-zero range in this paper. It significantly avoids the log-likelihood ratio information loss when less than the offset value and diminishes too quickly or sluggishly. A Segmented Bias/Normalize Min-Sum(SB/NMS) LDPC decoding algorithm is proposed with a layered structure. This algorithm can avoid the impact of the problems mentioned above and significantly improve the performance and iteration speed of the decoding process. Compared with the BLER (resp. BER) performance the traditional BP, NMS and OMS algorithm achieves a gain of 0.04, 0.11, and 0.15dB (resp. 0.035dB, 0.06, and 0.13dB). Meanwhile, the minimum SNR requirements of BLER =0.001 can be reduced by 0.02 dB compared with the BP algorithm. The parameters of SN/NMSA can be pre-processed on the computer, so there will be no additional increase in the overhead in resources and get better performance while getting faster iteration speed, while greatly guaranteeing the reliability and effectiveness of data transmission.
