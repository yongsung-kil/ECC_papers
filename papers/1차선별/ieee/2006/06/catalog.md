# IEEE Xplore — 2006-06 (1차선별 통과)


## Lifting methods for quasi-cyclic LDPC codes

- **Status**: ✅
- **Reason**: QC-LDPC lifting 구성으로 girth 보장 확장(E)—새 코드 설계 기법, 바이너리 LDPC 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1638625
- **Type**: journal
- **Published**: June 2006
- **Authors**: Seho Myung, Kyeongcheol Yang, Youngkyun Kim
- **PDF**: https://ieeexplore.ieee.org/document/1638625
- **Abstract**: In this paper, we present two simple methods to construct a quasi-cyclic LDPC (QC-LDPC) code of larger length by lifting a given QC-LDPC code. We show that its girth is always larger than or equal to that of the given QC-LDPC code. Applying the methods recursively, it is possible to construct a sequence of QC-LDPC codes generated from a single exponent matrix by proper floor or modulo operations. Simulation results show that they have no serious performance degradation, as compared with randomly constructed LDPC codes.

## Surrogate-channel design of universal LDPC codes

- **Status**: ✅
- **Reason**: surrogate-channel 기반 universal LDPC 코드 설계(E)—한 채널을 대리로 다채널용 코드 구성, 이식 가능한 설계 기법
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1638622
- **Type**: journal
- **Published**: June 2006
- **Authors**: F. Peng, W.E. Ryan, R.D. Wesel
- **PDF**: https://ieeexplore.ieee.org/document/1638622
- **Abstract**: A universal code is a code that may be used across a number of different channel types or conditions with little degradation relative to a good single-channel code. The explicit design of universal codes, which simultaneously seeks to solve a multitude of optimization problems, is a daunting task. This letter shows that a single channel may be used as a surrogate for an entire set of channels to produce good universal LDPC codes. This result suggests that sometimes a channel for which LDPC code design is simple may be used as a surrogate for a channel for which LDPC code design is complex. We explore here the universality of LDPC codes over the BEC, AWGN, and flat Rayleigh fading channels in terms of decoding threshold performance. Using excess mutual information as a performance metric, we present design results which support the contention that an LDPC code designed for a single channel can be universally good across the three channels

## On unequal error protection LDPC codes based on plotkin-type constructions

- **Status**: ✅
- **Reason**: LDPC 컴포넌트+Plotkin 구성 UEP 코드와 신뢰도 기반 다단계 반복 디코딩(C/E)—새 디코딩/구성 기법 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1643529
- **Type**: journal
- **Published**: June 2006
- **Authors**: V. Kumar, O. Milenkovic
- **PDF**: https://ieeexplore.ieee.org/document/1643529
- **Abstract**: We introduce a new family of unequal error protection (UEP) codes, based on low-density parity-check (LDPC) component codes and Plotkin-type constructions. The codes are decoded iteratively in multiple stages, and the order of decoding determines the level of error protection. The level of UEP among the code bits is also influenced by the choice of the LDPC component codes and by some new reliability features incorporated into the decoding process. The proposed scheme offers a very good tradeoff between code performance on one side and encoding/decoding and storage complexity on the other side. The novel approach to UEP also allows for finding simple approximations for the achievable degrees of UEP, which can be used to govern practical code design implementations

## Adaptive offset min-sum algorithm for low-density parity check codes

- **Status**: ✅
- **Reason**: adaptive offset min-sum 디코더 변형(C)—최소값 차이에 따른 적응 오프셋, NAND LDPC 디코더에 직접 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1638623
- **Type**: journal
- **Published**: June 2006
- **Authors**: Ming Jiang, Chunming Zhao, Li Zhang +1
- **PDF**: https://ieeexplore.ieee.org/document/1638623
- **Abstract**: An improvement is presented to the offset min-sum decoding algorithm for low-density parity check codes. The proposed algorithm introduces a more efficient adjustment for check-node update computation in view of different minimum values. According to the optimal correction factor of normalized min-sum algorithm, we can determine the adaptive offset item. The improved algorithm achieves a noticeable performance gain with only a modest increase in computation complexity.

## Low-Density Parity-Check Codes for Discretized Min-Sum Decoding

- **Status**: ✅
- **Reason**: 양자화 min-sum 디코더용 최적 스칼라 양자화기 결정 + 차수분포 공동최적화 — LLR 양자화/디코더 기법(C/E) NAND 직접 관련
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1644559
- **Type**: conference
- **Published**: 30 May-1 J
- **Authors**: B. Smith, F.R. Kschischang, Wei Yu
- **PDF**: https://ieeexplore.ieee.org/document/1644559
- **Abstract**: The performance of low-density parity-check (LDPC) codes transmitted over a memoryless binary-input continuous output additive white Gaussian noise (AWGN) channel and decoded with quantized min-sum decoding is strongly influenced by the decoder's quantization scheme. This paper presents an efficient algorithm that determines the best uniform scalar quantizer for a particular code. To maximize performance, it is necessary to determine degree distributions that best match the characteristics of the quantized min-sum decoder. Toward this end, an iterative optimization framework that jointly optimizes the degree distributions and the quantizer is presented

## Capacity-Approaching LDPC Codes with Low Error Floors for High-Speed Digital Communications

- **Status**: ✅
- **Reason**: circulant permutation 기반 irregular QC-LDPC error floor 저감 코드설계(차수분포·사이클구조 최적화) — 바이너리 E 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1644558
- **Type**: conference
- **Published**: 30 May-1 J
- **Authors**: Zhiyong He, S. Roy, P. Fortier
- **PDF**: https://ieeexplore.ieee.org/document/1644558
- **Abstract**: This paper discusses the design of capacity-approaching irregular low density parity check (LDPC) codes constructed from circulant permutation matrices with low error floors. The experimental results indicate that the performance in the waterfall region of the error curve can be improved by increasing the maximum column degree or by decreasing the fraction of columns with maximum degree in the parity check matrix. To delay the onset of the error floor, several techniques in code constructions are proposed to optimize both the degree distributions and the cycle structures of irregular codes. Having encoder architectures supporting throughputs in the Gbits/s region, the proposed codes are suitable for high-speed applications of various digital communications

## On the Robustness of Iterative Decoders

- **Status**: ✅
- **Reason**: 채널 파라미터 불확실성 하 반복 메시지패싱 디코더 강건화 알고리즘 — 부호비의존 디코더 개선(C), NAND 채널추정 불확실성에 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1644613
- **Type**: conference
- **Published**: 30 May-1 J
- **Authors**: P. Zarrinkhat, M. Ardakani
- **PDF**: https://ieeexplore.ieee.org/document/1644613
- **Abstract**: Robustness of iterative decoders, i.e., their ability to successfully decode the received signal in spite of unknown changes in the channel parameter, is investigated. More specifically, using low-density parity-check codes and iterative message-passing decoders for error correction, we consider reliable communication over a binary-input power-limited Gaussian channel whose noise power is not perfectly known to the receiver. We propose iterative algorithms that can decode the received signal in the presence of a strong uncertainty in the channel parameter. Such decoders are of interest for wireless applications, where the channel attenuation could significantly vary with time

## A Low Memory FPGA Based LDPC Decoder Architecture for Quasi-Cyclic LDPC codes

- **Status**: ✅
- **Reason**: QC-LDPC용 저메모리 FPGA 디코더 아키텍처; 코드구성·알고리즘·아키텍처 최적화로 메모리 절감, NAND HW 디코더에 직접 이식(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:4123899
- **Type**: conference
- **Published**: 28-30 June
- **Authors**: Paul Saunders, Antony D. Fagan
- **PDF**: https://ieeexplore.ieee.org/document/4123899
- **Abstract**: We propose a novel low memory fully programmable FPGA decoder architecture to decode quasi-cyclic LDPC codes. By performing optimizations at the code construction, algorithmic and architecture levels we are able to achieve significant memory storage advantages over current FPGA decoder implementations. Our decoder employs the modified turbo decoding algorithm, to achieve a memory utilisation of 71Kb using a Xilinx Virtex-4 device.

## Construction of Girth 8 LDPC Codes based on Finite Lattice Geometries

- **Status**: ✅
- **Reason**: 유한 격자기하 기반 girth-8 LDPC 신규 구성법+구현 이점 — 카테고리 E(코드설계) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4123943
- **Type**: conference
- **Published**: 28-30 June
- **Authors**: John Craddock, Mark Flanagan, Anthony Fagan
- **PDF**: https://ieeexplore.ieee.org/document/4123943
- **Abstract**: This paper presents a novel method for constructing Low Density Parity Check (LDPC) codes with a girth of up to 8. These codes are based on the structural properties of finite lattice geometries. Results are presented which show that these codes perform well over awgn channels with iterative decoding. These codes also have several implementation advantages, which are presented.

## A Class of Improved Low-Density Parity-Check Codes Constructed Based on Gallager's Form

- **Status**: ✅
- **Reason**: New finite-length LDPC construction (QC form, 4-cycle free, good min distance) for small block length — E portable code design
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4063991
- **Type**: conference
- **Published**: 25-28 June
- **Authors**: Guangen Wu, Pinyi Ren
- **PDF**: https://ieeexplore.ieee.org/document/4063991
- **Abstract**: Focused on the problem that short cycles degrade the iterative decoding performance of finite length LDPC, a class of improved low density parity check (LDPC) codes constructed based on Gallager's form is designed. On the basis of keeping down the basic form of Gallager's construction, a quasi-cyclic form is used, then the new codes are free of cycles of length 4 and have good minimum distance. Simulation results demonstrated that the improved codes are better than Gallager's codes when block length is small

## Enhanced Low-Density Parity-Check Codes Based on Sum-check Blocks

- **Status**: ✅
- **Reason**: Adds sum-check blocks over GF(2) to reduce error floor with circuits presented — binary LDPC error-floor reduction technique + HW (C/D/E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4064000
- **Type**: conference
- **Published**: 25-28 June
- **Authors**: Jingli Lin, Longjiang Jing, Weile Zhu +1
- **PDF**: https://ieeexplore.ieee.org/document/4064000
- **Abstract**: Based on some characteristics of decoding and error-floors of low-density parity-check (LDPC) codes, an approach of adding sum-check blocks to original LDPC blocks over GF(2) is proposed. The performance of this approach is analyzed and the circuits are also presented. Also, the simulation results show that the performance of the constructed LDPC codes can be improved significantly with low cost, as the block error probability (BEP) drops

## Efficient Decoder Implementation for QC-LDPC Codes

- **Status**: ✅
- **Reason**: QC-LDPC용 메모리 효율 고속 VLSI 디코더 아키텍처 + modified Min-Sum, 메모리 70% 절감 — 이식 가능 HW(D)/디코더(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4064429
- **Type**: conference
- **Published**: 25-28 June
- **Authors**: Jin Sha, Minglun Gao, Zhongjin Zhang +2
- **PDF**: https://ieeexplore.ieee.org/document/4064429
- **Abstract**: Channel coding is an important building block in communication systems. Low-density parity-check codes is one kind of prominent error correcting codes being considered in next generation industry standards. This paper presents a memory efficient, very high speed decoder architecture suited for quasi-cyclic low-density parity-check codes using modified Min-Sum decoding algorithm. In general, about seventy percent of message memory can be saved over conventional decoder architectures, and the decoding speed can be largely accelerated because of the highly efficient VLSI architecture. Consequently, the proposed approach facilitates the applications of LDPC codes in area/latency sensitive communication systems.

## A New Design Method of Multi-Rate Quasi-Cyclic LDPC Codes

- **Status**: ✅
- **Reason**: New multi-rate QC-LDPC design (fractional row combination, BIBD) plus low-complexity universal decoder architecture — E/D portable construction+HW
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4063994
- **Type**: conference
- **Published**: 25-28 June
- **Authors**: Zhichu Lin, Zhixing Yang, Changyong Pan
- **PDF**: https://ieeexplore.ieee.org/document/4063994
- **Abstract**: A new method called fractional row combination is proposed to design a group of multi-rate quasi-cyclic LDPC codes in this paper. Unlike the original row combination method, it guarantees all the codes under different rates have concentrated check-node degree distributions, hence better performance under iterative decoding. Moreover, a combinatorial method based on BIBD is applied to our design. Together with fractional row combination, a family of multi-rate quasi-cyclic LDPC codes can be constructed. A low-complexity architecture of the universal decoder for all rates is also introduced

## Iterative Decoding for the Concatenation of LDPC Codes and BCH Codes Based on Chase Algorithm

- **Status**: ✅
- **Reason**: LDPC+BCH 연접의 반복 joint 디코딩(Chase+BP 소프트정보 교환). 디코더 알고리즘 기법(C)으로 이식 가능하며 short-loop 대응.
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4068518
- **Type**: conference
- **Published**: 21-23 June
- **Authors**: Zhiping Shi, Liang Zhou, Hong Wen +1
- **PDF**: https://ieeexplore.ieee.org/document/4068518
- **Abstract**: In this paper, an iterative joint decoding algorithm for low density parity check codes with BCH codes based on Chase algorithm is proposed. After a certain number of iterations, the soft output values delivered by belief propagation algorithm of LDPC codes are used as reliability values to perform Chase decoding of BCH codes. And BCH decoder also will return soft information to LDPC decoder as input. This approach presents an option scheme for LDPC with medium length because of the relevant presence of short loops. It allows to bridge the gap between error performance and maximum likelihood decoding. Simulation result for the scheme is given.

## A novel simple stopping criterion for the PCGC decoder

- **Status**: ✅
- **Reason**: 반복 디코더 정지기준(extrinsic 정보 크기 평균 기반)으로 복잡도/연산 절감, 부호 비의존 디코더 기법(C)으로 이식 가능.
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4068833
- **Type**: conference
- **Published**: 21-23 June
- **Authors**: Xu Xiaojian, Li Jin, Hu Hanying
- **PDF**: https://ieeexplore.ieee.org/document/4068833
- **Abstract**: In this paper, in order to degrade the computation complexity and storage of the iterative decoder of parallel concatenated LDPC (low-density parity-check) codes, we propose a novel stopping criteria by using of the mean of the magnitude of the extrinsic information. We verify our algorithms with Monte Carlo simulation, and the results proved that the proposed rules outperforms the other existing criterions in terms of BER and average number of super iterations

## Fault Tolerance of Tornado Codes for Archival Storage

- **Status**: ✅
- **Reason**: B/E: Tornado (LDPC erasure) code graph construction, critical-set elimination for fault tolerance; storage ECC + cycle/graph-design technique
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1652139
- **Type**: conference
- **Published**: 19-23 June
- **Authors**: M. Woitaszek, H.M. Tufo
- **PDF**: https://ieeexplore.ieee.org/document/1652139
- **Abstract**: This paper examines a class of low density parity check (LDPC) erasure codes called Tornado codes for applications in archival storage systems. The fault tolerance of Tornado code graphs is analyzed and it is shown that it is possible to identify and mitigate worst-case failure scenarios in small (96 node) graphs through use of simulations to find and eliminate critical node sets that can cause Tornado codes to fail even when almost all blocks are present. The graph construction procedure resulting from the preceding analysis is then used to construct a 96-device Tornado code storage system with capacity overhead equivalent to RAID 10 that tolerates any 4 device failures. This system is demonstrated to be superior to other parity-based RAID systems. Finally, it is described how a geographically distributed data stewarding system can be enhanced by using cooperatively selected Tornado code graphs to obtain fault tolerance exceeding that of its constituent storage sites or site replication strategies

## HDL Library of Processing Units for an Automatic LDPC Decoder Design

- **Status**: ✅
- **Reason**: LDPC 디코더 처리유닛(bit/check node) HDL 라이브러리, serial/parallel 아키텍처 자동생성으로 HW 이식 가능(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:1689967
- **Type**: conference
- **Published**: 12-15 June
- **Authors**: G. Falcao, M. Gomes, J. Goncalves +2
- **PDF**: https://ieeexplore.ieee.org/document/1689967
- **Abstract**: In this paper we propose an efficient and generic HDL library of processing units which are the key elements of a modular low-density parity check (LDPC) decoder design approach. General purpose, low complexity and high throughput bit node and check functional models are developed. Both full serial and parallel architectures are considered. Also, it is described an automatic HDL code generator for the proposed processing units using Matlab language and synthesis results for a Xilinx FPGA device are documented

## On a Construction Method of Irregular LDPC Codes Without Small Stopping Sets

- **Status**: ✅
- **Reason**: PEG 기반으로 small stopping set 없는 irregular LDPC 구성, 사이클/최소거리 개선 코드설계(E)에 직접 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4024289
- **Type**: conference
- **Published**: 11-15 June
- **Authors**: G. Richter, A. Hof
- **PDF**: https://ieeexplore.ieee.org/document/4024289
- **Abstract**: In this paper, we present a construction method based on the progressive edge-growth (PEG) algorithm to design irregular low-density parity-check (LDPC) codes without small stopping sets. We show how to choose the connections in the PEG algorithm when having multiple choices to connect a variable node with a check node. Since preventing small stopping sets also prevents a low minimum distance, our construction method also leads to LDPC codes with a higher minimum distance. Furthermore, we show by simulation that our construction method improves the performance over the binary erasure channel and over the additive white Gaussian noise channel for a low erasure probability and a high signal-to-noise ratio, respectively.

## On Gaussian Approximation for Density Evolution of Low-Density Parity-Check Codes

- **Status**: ✅
- **Reason**: LDPC density evolution의 가우시안 근사(mean+variance) 분석 기법, 코드설계/디코더 분석(E)에 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4024287
- **Type**: conference
- **Published**: 11-15 June
- **Authors**: Minyue Fu
- **PDF**: https://ieeexplore.ieee.org/document/4024287
- **Abstract**: This paper is concerned with density evolution for iterative decoding of low-density parity-check (LDPC) codes. We first study the problem of density evolution computation for regular LDPC codes. For this, we propose a simple computational algorithm based on the ergodicity theory. This method is shown to match very well with explicit calculations of density functions. The second problem we study is about the approach of Gaussian approximation to density evolution. We point out that it is inappropriate to use the mean of the density only to model the iterative decoding process. Instead, both the mean and variance are needed for Gaussian approximation. Finally, we consider the problem of density evolution for irregular LDPC codes. For this, we extend the density evolution algorithm for regular LDPC codes to irregular LDPC codes. We then illustrate that Gaussian approximation is also valid provided that the degree distributions are not wide. A dynamic model is also presented based on Gaussian approximation.

## Improved Low-Density Parity-Check Codes for Burst Erasure Channels

- **Status**: ✅
- **Reason**: 임의 LDPC 부호에 적용 가능한 디코더 성능 최적화 알고리즘(C). 부호 비의존적 LDPC BP 개선이라 이식 가능.
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4024300
- **Type**: conference
- **Published**: 11-15 June
- **Authors**: Enrico Paolini, Marco Chiani
- **PDF**: https://ieeexplore.ieee.org/document/4024300
- **Abstract**: In this work we deal with Low-Density Parity-Check (LDPC) codes under iterative message passing decoding algorithm, over channels introducing bursts of erasures. The burst erasure channel model we consider in this paper can be seen as an erasure channel based on a hidden Markov chain (HMC-EC). In order to characterize the channel, in the first part of the paper the expression of mutual information is recalled for any erasure channel with memory and with i.i.d. and equiprobable input symbols. In the second part of the paper an optimization algorithm is proposed which is able to heavily improve LDPC iterative decoder performance. This algorithm can be in principle applied to any given LDPC code. Simulation results relative to both random and IRA / eIRA codes are shown comparing the performance before and after the application of our optimization algorithm.

## The Minimal Product Parity Check Matrix and Its Application

- **Status**: ✅
- **Reason**: 최소 product 패리티검사행렬로 girth g 보장 irregular LDPC 구성, NAND LDPC 코드설계(E)에 이식 가능한 바이너리 LDPC 구성법
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4024288
- **Type**: conference
- **Published**: 11-15 June
- **Authors**: Morteza Esmaeili
- **PDF**: https://ieeexplore.ieee.org/document/4024288
- **Abstract**: In decoding a linear block code C by iterative decoding algorithms, these algorithms are essentially applied on a graphical representation of C such as Tanner graph and factor graph. Due to the impact of the structure of these graphs on the performance of code, we consider minimal parity check matrices(matrices with minimum number of nonzero entries) of product codes. An algorithm constructing such matrices is given. It turns out that under the given construction method, product coding technique is indeed a powerful method to construct irregular LDPC codes. Given two codes A and B, the construction method produces a Tanner graph with girth g := min {8, ga, gb} for the product code A ⊗ B, where ga and gb are the girth of Tanner graphs representing A and B, respectively. Simulation results confirm the positive practical impact of the minimality of the parity check matrices.

## Error Floors of LDPC Codes on the Binary Symmetric Channel

- **Status**: ✅
- **Reason**: BSC상 LDPC error floor를 trapping set/girth로 해석하는 정량 기법, error floor 분석은 NAND LDPC 코드설계(E)에 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4024284
- **Type**: conference
- **Published**: 11-15 June
- **Authors**: Shashi Kiran Chilappagari, Sundararajan Sankaranarayanan, Bane Vasic
- **PDF**: https://ieeexplore.ieee.org/document/4024284
- **Abstract**: In this paper, we propose a semi-analytical method to compute error floors of LDPC codes on the binary symmetric channel decoded iteratively using the Gallager B algorithm. The error events of the decoder are characterized using combinatorial objects called trapping sets, originally defined by Richardson. In general, trapping sets are characteristic of the graphical representation of a code. We study the structure of trapping sets and explore their relation to graph parameters such as girth and vertex degrees. Using the proposed method, we compute error floors of regular structured and random LDPC codes with column weight three.

## Design of Efficiently-Encodable Rate-Compatible Irregular LDPC Codes

- **Status**: ✅
- **Reason**: 유한블록 efficiently-encodable rate-compatible irregular 바이너리 LDPC 구성/펑처링, 코드설계(E)에 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4024291
- **Type**: conference
- **Published**: 11-15 June
- **Authors**: Jaehong Kim, Aditya Ramamoorthy, Steven W. McLaughlin
- **PDF**: https://ieeexplore.ieee.org/document/4024291
- **Abstract**: We present a new class of irregular low-density parity-check (LDPC) codes for finite block length (up to a few thousand symbols). The proposed codes are efficiently encodable and have a simple rate-compatible puncturing structure. For block lengths on the order of n=1000 bits, the codes show good puncturing performance over a wide range of rates. The codes outperform optimized irregular LDPC codes and (extended) irregular repeat-accumulate codes for all rates 0.5~0.9, and are particularly good at high puncturing rates where good puncturing performance has been previously difficult to achieve.

## Construction of Irregular LDPC Convolutional Codes with Fast Encoding

- **Status**: ✅
- **Reason**: 불규칙 LDPC convolutional 부호의 신규 구성 + 시프트레지스터 기반 빠른 인코더(E/D). 바이너리 LDPC 구성·HW 이식 가능.
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4024296
- **Type**: conference
- **Published**: 11-15 June
- **Authors**: Ali Emre Pusane, Kamil Sh. Zigangirov, Daniel J. Costello
- **PDF**: https://ieeexplore.ieee.org/document/4024296
- **Abstract**: We propose a novel code design technique for irregular LDPC convolutional codes. The constructed codes can be encoded continuously in real time with the help of a shift-register based encoder. For moderate values of the syndrome former memory, simulation results show that the constructed codes outperform LDPC block codes with comparable hardware (processor) complexity.

## A Structured LDPC Code Construction for Efficient Encoder Design

- **Status**: ✅
- **Reason**: 효율적 인코더용 구조적 LDPC 구성, 패리티검사 행렬 레이어 분할 병렬처리; 이식 가능 코드설계/HW 병렬화(E/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4024394
- **Type**: conference
- **Published**: 11-15 June
- **Authors**: Jean-baptiste Dore, Marie-helene Hamon, Pierre Penard
- **PDF**: https://ieeexplore.ieee.org/document/4024394
- **Abstract**: Low-Density Parity Check codes have been widely investigated over the past few years, and construction of Low-Density Parity Check code enabling efficient implementation design represents one of the main topics of interest. This article proposes a new code family, based on a structures code construction with an inherent parallelism. This construction divides the parity check matrix into layers which can be processed simultaneously, improving encoding throughput and latency. Possible optimizations and example are proposed and illustrated.

## Trapping Sets in Irregular LDPC Code Ensembles

- **Status**: ✅
- **Reason**: irregular 바이너리 LDPC ensemble의 trapping set 분포 분석, error floor 코드설계(E) 관련 기법
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4024286
- **Type**: conference
- **Published**: 11-15 June
- **Authors**: Olgica Milenkovic, Emina Soljanin, Philip Whiting
- **PDF**: https://ieeexplore.ieee.org/document/4024286
- **Abstract**: Trapping sets represent subgraphs in the Tanner graph of a code that, for certain classes of channels, exhibit a strong influence on the height and point of onset of the error-floor. We compute the asymptotic normalized distributions of trapping sets in random, irregular, binary low-density parity-check (LDPC) code ensembles. Our derivations rely on techniques from large deviation theory and statistical methods for enumeracting random-like matrices. Similar methods can be used for computing the spectra of other combinatorial entities in LDPC code, such as subcodes and/or minimal codewords.

## A Linear-Programming Approach to The Design of LDPC Codes for Non-Uniform Channels

- **Status**: ✅
- **Reason**: 비균일 채널 LDPC 부호 설계를 LP로 최적화하는 코드설계 기법(E). NAND는 페이지/비트별 채널 편차가 있어 비균일 채널 최적화가 이식 가능.
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4024293
- **Type**: conference
- **Published**: 11-15 June
- **Authors**: Masoud Ardakani
- **PDF**: https://ieeexplore.ieee.org/document/4024293
- **Abstract**: We propose a linear-programming approach to the design of low-density parity-check codes for non-uniform channels, i.e., when different bits of the codeword experience different channel parameters. Non-uniform channels are encountered in many communication systems, e.g., in a network that different packets are sent through parallel routes; in orthogonal frequency division multiplexing, where the codeword bits are modulated in different frequency bins with different SNR; also in multi-input multi-output systems, where different channel pairs have different parameters. We formulate the problem of optimizing the rate of an irregular low-density parity-check code, with guaranteed convergence over such a channel, as an iterative linear-programming. The number of design-parameters for code-design over non-uniform channels is much greater than the number of design-parameters in conventional channels. Therefore, search-based optimization methods are impractical. As a result, a linear-programming approach is significantly more efficient. The methodology of this paper is directly applicable to all decoding algorithms for which an exact or accurate-enough one-dimensional analysis is possible. For other decoding algorithms, we show that the method can still be applied after minor modifications.

## An IS Simulation Technique for Very Low BER Performance Evaluation of LDPC Codes

- **Status**: ✅
- **Reason**: trapping set 기반 IS 시뮬레이션으로 LDPC 초저BER 성능평가, NAND ECC의 error floor 검증 방법론(E)으로 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4024285
- **Type**: conference
- **Published**: 11-15 June
- **Authors**: Enver Cavus, Charles L. Haymes, Babak Daneshrad
- **PDF**: https://ieeexplore.ieee.org/document/4024285
- **Abstract**: We introduce an Importance Sampling (IS) method that successfully simulates the performance of Low density Parity Check (LDPC) Codes in an AWGN channel at very low bit error rates (BERs). By effectively finding and biasing bit node combinations that are the dominant sources of error events, called trapping sets, the developed technique provokes more frequent decoder failures. Consequently, fewer simulation runs and higher simulation gains are achieved. Regardless of the block size of an LDPC code, only a few dominant trapping set classes cause decoder failures at low BER regions. Therefore, the proposed technique allows the performance evaluation for any size LDPC code at very low BER regions with remarkable simulation gains. For BERs of 10-20, we observed simulation gains on the order of 1014.

## A new family of codes with high iterative decoding performances

- **Status**: ✅
- **Reason**: LDPC와 터보의 하이브리드 신규 부호 클래스로 error floor 없는 우수한 iterative 디코딩 성능. 코드설계/디코더 기법 이식 가능성으로 애매하면 in.
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4024299
- **Type**: conference
- **Published**: 11-15 June
- **Authors**: Iryna Andriyanova, Jean-pierre Tillich, Jean-claude Carlach
- **PDF**: https://ieeexplore.ieee.org/document/4024299
- **Abstract**: We investigate a new class of codes which is in a sense a hybrid between LDPC codes and turbo-codes. Some members of this new class have been shown to be asymptotically good and we conjecture that such a behavior holds for all classes of codes presented here. They all display excellent iterative decoding performances with no error floor at block error rates up to 10-6 for lengths of several thousand together with low average decoding complexity.
