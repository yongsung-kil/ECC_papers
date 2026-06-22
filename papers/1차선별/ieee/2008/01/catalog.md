# IEEE Xplore — 2008-01 (1차선별 통과)


## Hybrid Iterative Decoding for Low-Density Parity-Check Codes Based on Finite Geometries

- **Status**: ✅
- **Reason**: FG-LDPC용 WBF+BP 2단 하이브리드 디코딩으로 복잡도 절감 — 이식 가능 디코더(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4432324
- **Type**: journal
- **Published**: January 20
- **Authors**: Jian Li, Xian-da Zhang
- **PDF**: https://ieeexplore.ieee.org/document/4432324
- **Abstract**: In this letter, a two-stage hybrid iterative decoding algorithm which combines two iterative decoding algorithms is proposed to reduce the computational complexity of finite geometry low-density parity-check (FG-LDPC) codes. We introduce a fast weighted bit-flipping (WBF) decoding algorithm for the first stage decoding. If the first stage decoding fails, the decoding is continued by the powerful belief propagation (BP) algorithm. The proposed hybrid decoding algorithm greatly reduces the computational complexity while maintains the same performance compared to that of using the BP algorithm only.

## New constructions of quasi-cyclic LDPC codes based on special classes of BIBD's for the AWGN and binary erasure channels

- **Status**: ✅
- **Reason**: BIBD 기반 신규 QC-LDPC 구성(인코딩 효율적), AWGN/BEC — 바이너리 코드 설계(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4436087
- **Type**: journal
- **Published**: January 20
- **Authors**: Lan Lan, Ying Yu Tai, Shu Lin +2
- **PDF**: https://ieeexplore.ieee.org/document/4436087
- **Abstract**: This paper presents new methods for constructing efficiently encodable quasi-cyclic LDPC codes based on special balanced incomplete block designs (BIBD's). Codes constructed perform well over both the AWGN and binary erasure channels with iterative decoding.

## Generalized ACE Constrained Progressive Edge-Growth LDPC Code Design

- **Status**: ✅
- **Reason**: ACE 제약 일반화 PEG LDPC 코드 그래프 설계 — 사이클/구조 개선 코드 설계(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4432325
- **Type**: journal
- **Published**: January 20
- **Authors**: Dejan Vukobratovic, Vojin Senk
- **PDF**: https://ieeexplore.ieee.org/document/4432325
- **Abstract**: In this letter, we propose a generalization of the progressive edge-growth (PEG) algorithm with the aim of designing LDPC code graphs with substantially improved approximated cycle extrinsic message degree (ACE) properties. The proposed realization of generalized PEG algorithm outperforms original PEG algorithm and its subsequent modification proposed by Xiao and Banihashemi.

## Block-Interlaced LDPC Decoders With Reduced Interconnect Complexity

- **Status**: ✅
- **Reason**: LDPC 디코더 HW 아키텍처(broadcasting로 라우팅 혼잡 완화, interlacing로 throughput 증대) - 이식 가능 HW 아키텍처(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:4389924
- **Type**: journal
- **Published**: Jan. 2008
- **Authors**: Ahmad Darabiha, Anthony Chan Carusone, Frank R. Kschischang
- **PDF**: https://ieeexplore.ieee.org/document/4389924
- **Abstract**: Two design techniques are proposed for high-throughput low-density parity-check (LDPC) decoders. A broadcasting technique mitigates routing congestion by reducing the total global wirelength. An interlacing technique increases the decoder throughput by processing two consecutive frames simultaneously. The brief discusses how these techniques can be used for both fully parallel and partially parallel LDPC decoders. For fully parallel decoders with code lengths in the range of a few thousand bits, the half-broadcasting technique reduces the total global wirelength by about 26% without any hardware overhead. The block interlacing scheme is applied to the design of two fully parallel decoders, increasing the throughput by 60% and 71% at the cost of 5.5% and 9.5% gate count overhead, respectively.

## Design of Inner LDPC Codes for Magnetic Recording Channels

- **Status**: ✅
- **Reason**: single-parity 기반 저복잡도 inner 바이너리 LDPC 코드 설계(E), 4k 섹터 스토리지용으로 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4407612
- **Type**: journal
- **Published**: Jan. 2008
- **Authors**: Weijun Tan
- **PDF**: https://ieeexplore.ieee.org/document/4407612
- **Abstract**: Inner low-density parity-check (LDPC) codes are designed for practical use in magnetic recording read channel with traditional outer Reed-Solomon (RS) codes. These codes are based on single-parity codes and therefore have low encoding and decoding complexity. Simulation results show that these LDPC codes are promising inner codes for both 512 and 4 k byte sectors.

## Minimum Pseudoweight and Minimum Pseudocodewords of LDPC Codes

- **Status**: ✅
- **Reason**: LDPC pseudoweight/pseudocodeword, girth와 LP 디코딩 error floor 관련 코드설계 분석(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4418506
- **Type**: journal
- **Published**: Jan. 2008
- **Authors**: Shu-Tao Xia, Fang-Wei Fu
- **PDF**: https://ieeexplore.ieee.org/document/4418506
- **Abstract**: In this correspondence, we study the minimum pseudoweight and minimum pseudocodewords of low-density parity-check (LDPC) codes under linear programming (LP) decoding. First, we show that the lower bound of Kelley, Sridhara, Xu, and Rosenthal on the pseudoweight of a nonzero pseudocodeword of an LDPC code whose Tanner graph has girth greater than is tight if and only if this pseudocodeword is a real multiple of a codeword. Then, the lower bound of Kashyap and Vardy on the stopping distance of an LDPC code is proved to be also a lower bound on the pseudoweight of a nonzero pseudocodeword of an LDPC code whose Tanner graph has girth , and this lower bound is tight if and only if this pseudocodeword is a real multiple of a codeword. Using these results we further obtain that for some LDPC codes, there are no other minimum pseudocodewords except the real multiples of minimum weight codewords. This means that the LP decoding for these LDPC codes is asymptotically optimal in the sense that the ratio of the probabilities of decoding errors of LP decoding and maximum-likelihood decoding approaches as the signal-to-noise ratio (SNR) tends to infinity. Finally, some LDPC codes are listed to illustrate these results.

## Extremal Problems of Information Combining

- **Status**: ✅
- **Reason**: information combining으로 바이너리 LDPC BP 수렴 예측 개선, BP 분석기법 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4418482
- **Type**: journal
- **Published**: Jan. 2008
- **Authors**: Yibo Jiang, Alexei Ashikhmin, Ralf Koetter +1
- **PDF**: https://ieeexplore.ieee.org/document/4418482
- **Abstract**: In this paper, we study moments of soft bits of binary-input symmetric-output channels and solve some extremal problems of the moments. We use these results to solve the extremal information combining problem. Further, we extend the information combining problem by adding a constraint on the second moment of soft bits, and find the extremal distributions for this new problem. The results for this extension problem are used to improve the prediction of convergence of the belief propagation decoding of low-density parity-check (LDPC) codes, provided that another extremal problem related to the variable nodes is solved.

## Efficient Realization of CORDIC based LDPC Decoder for WiMax System

- **Status**: ✅
- **Reason**: QC-LDPC 디코더 HW에서 CNU를 CORDIC로 구현해 LUT 대비 절감; 이식 가능 HW 아키텍처(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:4447158
- **Type**: conference
- **Published**: 4-6 Jan. 2
- **Authors**: P. Palanisamy, R. Thilagavathy, M.Ratheesh Kumar +1
- **PDF**: https://ieeexplore.ieee.org/document/4447158
- **Abstract**: Low-density parity-check (LDPC) codes have recently emerged due to their excellent performance in wired, wireless communication applications and in disk drives. Based on architecture-aware LDPC codes, this paper presents an efficient joint LDPC coding and decoding hardware architecture. We used a special class of quasi-cyclic low-density parity-check (QC-LDPC) codes, which have an efficient encoding algorithm due to the simple structure of their parity-check matrices. Since the parity-check matrix of a QC-LDPC code consists of circulant permutation matrices or the zero matrix, the required memory for storing it can be significantly reduced, as compared with randomly constructed LDPC codes. An encoder and a decoder are designed using Verilog-HDL and are synthesized using synopsys design compiler with 150 nm TSMC standard cell library. We used CORDIC algorithm to implement check node update unit in decoder which saves much hardware compared to conventional LUT approach. We study the optimal permutation of the bit nodes that will result in the maximum possible burst erasure correction capability for a given LDPC code. The simulation results show the burst-erasure correction capability of quasi-cyclic LDPC codes in the IEEE 802.16e (WiMax) standard.

## Current-mode memory cell with power down phase for discrete time analog iterative decoders

- **Status**: ✅
- **Reason**: 아날로그 반복디코더용 저전력 current-mode 메모리셀 HW, 반복디코더 HW 아키텍처(D)로 이식 가능성
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:4541526
- **Type**: conference
- **Published**: 2008
- **Authors**: R. Dlugosz, V. Gaudet
- **PDF**: https://ieeexplore.ieee.org/document/4541526
- **Abstract**: A low power, current-mode memory element for analog discrete time iterative decoders is proposed. In the circuit a high-speed power-down mechanism has been implemented that enables a significant increase of the operation speed without increasing the power dissipation. During the power down phase the data stored in the memory is maintained in the capacitor. The proposed memory element works at a sampling frequency of 10 MSps. During the normal operation the memory cell dissipates power of 1.5-μW, while in the standby phase 50-nW.

## A thresholding algorithm for improved Split-Row decoding of LDPC codes

- **Status**: ✅
- **Reason**: LDPC Split-Row 디코딩의 thresholding 개선 알고리즘으로 throughput/HW 효율 향상, 이식 가능 디코더(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5074444
- **Type**: conference
- **Published**: 2008
- **Authors**: T. Mohsenin, P. Urard, B. Baas
- **PDF**: https://ieeexplore.ieee.org/document/5074444
- **Abstract**: The recently proposed split-row decoding algorithm provides significant improvements in the throughput, hardware efficiency and energy efficiency when compared to existing soft decision decoding algorithms at the cost of some error performance loss. In this paper we propose split-row threshold which outperforms the split-row algorithm while maintaining the same level of complexity. Simulation results show that the algorithm provides 0.15-0.2 dB coding gain over split-row decoding and is within 0.15-0.2 dB of SPA and MinSum normalized.

## Channel Code Division Multiple Access and its Multilevel Structured LDPC Based Instantiation

- **Status**: ✅
- **Reason**: 다중사용자용 MLS(multilevel structured) LDPC 신규 구성으로 메모리·복잡도 절감, 바이너리 구조화 LDPC 코드설계(E) 이식 가능성
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4657193
- **Type**: conference
- **Published**: 2008
- **Authors**: N. Bonello, R. Zhang, S. Chen +1
- **PDF**: https://ieeexplore.ieee.org/document/4657193
- **Abstract**: In this paper, we introduce and outline the concept of channel code division multiple access (CCDMA) using a design example based on the proposed multilevel structured (MLS) LDPC codes. We succeeded in making the memory requirements of the multi-user transceiver to become practically independent of the total number of users supported by the system as well as ascertain that each user benefits from the same quality of service (QoS). Finally, we demonstrate that despite their beneficial compact structure, the proposed MLS LDPC codes do not suffer from any bit error ratio (BER) or block error ratio (BLER) performance degradation, when compared to an otherwise identical benchmarker scheme using significantly more complex LDPC codes having pseudo-random parity-check matrices.

## PEG algorithm based interleavers design for systematic IRA codes

- **Status**: ✅
- **Reason**: PEG 알고리즘으로 short cycle 제거하는 코드 설계(E)—IRA지만 패리티검사가 sparse하고 BP 디코딩, PEG girth 기법은 바이너리 LDPC 구성에 직접 이식 가능.
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4735505
- **Type**: conference
- **Published**: 2008
- **Authors**: Pei-Jun Chen, Lian-Xiang Zhu, Qing Hu
- **PDF**: https://ieeexplore.ieee.org/document/4735505
- **Abstract**: Irregular-repeat-accumulate (IRA) codes are random-like codes having extremely good performance over AWGN channel. They can be viewed as special kinds of LDPC codes in the way their parity-check matrix are sparse. Like LDPC codes, they can be decoded using the messages-passing algorithm efficiently, while the existence of short length circles in their corresponding factor graph representation has a deleterious effect on the BER performance of the codes. Progressive edge-growth (PEG) algorithm is a famous method to construct factor graph without short circles. In this paper, we use PEG algorithm to construct the parity-check matrix of IRA codes firstly, and then deduce the interleaver design of the codes. Experimental results show significant improvement on the BER performance of the IRA codes with designed interleaver over the IRA codes with randomly choose interleaver.

## Maximum Likelihood Decoding of Turbo Codes on the Binary Erasure Channel

- **Status**: ✅
- **Reason**: Turbo ML 디코딩(BEC stopping set→연립방정식)이며 LDPC ML 디코딩 알고리즘을 turbo에 적용·비교, stopping set 처리 기법이 바이너리 LDPC BP에 이식 가능성(C)으로 애매하여 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4533259
- **Type**: conference
- **Published**: 2008
- **Authors**: M. Ferrari, S. Bellini
- **PDF**: https://ieeexplore.ieee.org/document/4533259
- **Abstract**: In this paper we deal with Maximum Likelihood (ML) decoding of Turbo Codes on the Binary Erasure Channel. First we describe a new ML decoder. When the standard iterative decoder fails because the set of erasures includes a stopping set, with the component decoders we obtain a linear system of equations that seeks the codeword constrained by both component codes. We evaluate the complexity in terms of equivalent turbo iterations and we show that this ML decoder is implementable. We also modify the algorithm proposed in [6] for LDPC to decode Turbo Codes and we compare the two methods. We find that, in general, our method is more efficient with low memory or punctured codes. Finally, by simulation we show that m-ary Turbo Codes under ML decoding outperform the error exponent bounds for random codes down to WER=10-6, for all rates ranging from 1/3 to 7/8.

## PEEC: a channel-adaptive feedback-based error

- **Status**: ✅
- **Reason**: 무선LAN 오류제어이나 adaptive LDPC 디코더(A-LDPC) 설계·구현 제시, 적응형 디코더 기법 이식 가능성(C) 검토
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4641948
- **Type**: journal
- **Published**: 2008
- **Authors**: S. Soltani, H. Radha
- **PDF**: https://ieeexplore.ieee.org/document/4641948
- **Abstract**: Reliable transmission is a challenging task over wireless LANs since wireless links are known to be susceptible to errors. Although the current IEEE802.11 standard ARQ error control protocol performs relatively well over channels with very low bit error rates (BERs), this performance deteriorates rapidly as the BER increases. This paper investigates the problem of reliable transmission in a contention free wireless LAN and introduces a packet embedded error control (PEEC) protocol, which employs packet-embedded parity symbols instead of ARQ-based retransmission for error recovery. Specifically, depending on receiver feedback, PEEC adaptively estimates channel conditions and administers the transmission of (data and parity) symbols within a packet. This enables successful recovery of both new data and old unrecovered data from prior transmissions. In addition to theoretically analyzing PEEC, the performance of the proposed scheme is extensively analyzed over real channel traces collected on 802.11b WLANs. We compare PEEC performance with the performance of the IEEE802.il standard ARQ protocol as well as contemporary protocols such as enhanced ARQ and the hybrid ARQ/FEC. Our analysis and experimental simulations show that PEEC outperforms all three competing protocols over a wide range of actual 802.11b WLAN collected traces. Finally, the design and implementation of PEEC using an adaptive low-density-parity-check (A-LDPC) decoder is presented.

## Improved impulse method to evaluate the low weight profile of sparse binary linear codes

- **Status**: ✅
- **Reason**: sparse 바이너리 코드의 저중량 프로파일(error floor 관련) 평가 개선 기법, 코드설계(E) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4595332
- **Type**: conference
- **Published**: 2008
- **Authors**: D. Declercq, M. Fossorier
- **PDF**: https://ieeexplore.ieee.org/document/4595332
- **Abstract**: In this paper, the impulse method to determine the low weight profile of sparse codes is improved based on efficient probabilistic approaches for reliability based decoding that are adapted to this problem. As a result, compared with previous approaches, the same low weight profile can be obtained with a significant time reduction (for example from 30 hours to a few minutes) or more complete low weight profiles can be determined in the same amount of time.

## A construction of channel code, joint source-channel code, and universal code for arbitrary stationary memoryless channels using sparse matrices

- **Status**: ✅
- **Reason**: sparse matrix 기반 채널코드 신규 구성, 비대칭 메모리리스 채널용 sparse 코드 설계 이식 가능성 (애매하면 in)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4595176
- **Type**: conference
- **Published**: 2008
- **Authors**: S. Miyake, J. Muramatsu
- **PDF**: https://ieeexplore.ieee.org/document/4595176
- **Abstract**: A channel code is constructed using sparse matrices for stationary memoryless channels that do not necessarily have a symmetric property like a binary symmetric channel. It is also shown that the constructed code has the following remarkable properties: 1) Joint source-channel coding: Combining with lossy source code, which is also constructed by sparse matrices, a simpler joint source-channel code can be constructed than that constructed by the ordinary block code. 2) Universal coding: The constructed channel code has a universal property under a specified condition.

## Linear-programming receivers

- **Status**: ✅
- **Reason**: LP 디코딩과 SP(BP) 디코더의 등가성·pseudoconfiguration 분석은 바이너리 LDPC BP 디코더 분석/설계에 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4797568
- **Type**: conference
- **Published**: 2008
- **Authors**: M. F. Flanagan
- **PDF**: https://ieeexplore.ieee.org/document/4797568
- **Abstract**: It is shown that any communication system which admits a sum-product (SP) receiver also admits a corresponding linear-programming (LP) receiver. The two receivers have a relationship defined by the local structure of the underlying graphical model, and are inhibited by the same phenomenon, which we call pseudoconfigurations. This concept is a generalization of the concept of pseudocodewords for linear codes. It is proved that the LP receiver has the dasiaoptimum certificatepsila property, and that the receiver output is the lowest cost pseudoconfiguration. Equivalence of graph-cover pseudoconfigurations and linear-programming pseudoconfigurations is also proved. While the LP receiver is generally more complex than the corresponding SP receiver, the LP receiver and its associated pseudoconfiguration structure provide an analytic tool for the analysis of SP receivers. As an example application, we show how the LP design technique may be applied to the problem of joint equalization and decoding.

## The slope scaling parameter for general channels, decoders, and ensembles

- **Status**: ✅
- **Reason**: irregular LDPC 앙상블 유한길이 scaling 최적화 도구, 유한길이 코드설계(E)에 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4595226
- **Type**: conference
- **Published**: 2008
- **Authors**: J. Ezri, A. Montanari, S. Oh +1
- **PDF**: https://ieeexplore.ieee.org/document/4595226
- **Abstract**: Scaling laws are a powerful way to analyze the performance of moderately sized iteratively decoded sparse graph codes. Our aim is to provide an easily usable finite-length optimization tool that is applicable to the wide variety of channels, blocklengths, error probability requirements, and decoders that one encounters for practical systems. The tool is aimed at non-experts in the field, who need to quickly find code designs that are comparable with the best known codes available today but do not have the luxury of spending months in doing so. In previous work we have shown how to compute scaling parameters for transmission over the binary erasure channel, as well as general channels and general quantized message-passing decoders when applied to regular ensembles. In this paper we show how to compute the message variance for a fixed number of iterations for irregular low-density parity-check ensembles. From these calculations the basic scaling parameter alpha can be deduced by determining the leading term of the limiting expression when the number of iterations tends to infinity and the channel parameter approaches the density evolution threshold.

## Macroscopic and Microscopic Approaches in Sector Failure Rate Estimation

- **Status**: ✅
- **Reason**: HDD 섹터 실패율(SFR) 추정 통계모델, 스토리지 ECC 일반(B)이며 반복채널 LDPC 오류통계 추정에 활용 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4407600
- **Type**: journal
- **Published**: 2008
- **Authors**: A. V. Kuznetsov, R. Venkataramani
- **PDF**: https://ieeexplore.ieee.org/document/4407600
- **Abstract**: The sector failure rate (SFR) is extremely small at normal operating conditions of hard disk drives. In practice, it cannot be obtained by counting as that would require prohibitively large simulation times. Therefore, appropriate statistical models characterizing the distribution of error symbols are used in order to estimate the SFR. In this paper, we look at the underlying philosophy of existing estimation methods and classify them into macroscopic and microscopic types. We observe that the microscopic approach is well suited for certain iterative channels.

## Design of cages with a randomized progressive edge-growth algorithm

- **Status**: ✅
- **Reason**: PEG 개선으로 girth 향상·g-cycle 최소화하는 신규 코드설계(E); 본문은 dv=2 비이진용이나 알고리즘 자체가 부호 비의존이라 바이너리 LDPC에 이식 가능, 애매하여 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4489674
- **Type**: journal
- **Published**: 2008
- **Authors**: A. Venkiah, D. Declercq, C. Poulliat
- **PDF**: https://ieeexplore.ieee.org/document/4489674
- **Abstract**: The progressive edge-growth (PEG) construction is a well known algorithm for constructing bipartite graphs with good girth properties. In this letter, we propose some improvements in the PEG algorithm which greatly improve the girth properties of the resulting graphs: given a graph size, they increase the girth g achievable by the algorithm, and when the girth cannot be increased, our modified algorithm minimizes the number of cycles of length g. As a main illustration, we focus on regular column-weight two graphs (dv = 2), although our algorithm can be applied to any graph connectivity. The class of dv = 2 graphs is often used for non-binary low density parity check codes that can be seen as monopartite graphs: for a given target girth gt, this new instance of the PEG algorithm allows to construct cages, i.e. graphs with the minimal size such that a graph of girth gt exists, which is the best result one might hope for.

## On a Class of High-Girth LDPC Codes Based on Finite Multidimensional Lattices

- **Status**: ✅
- **Reason**: 유한 다차원 격자 기반 고-girth LDPC 신규 구성+저복잡도 직병렬 디코더, 바이너리 코드설계 기여(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5755776
- **Type**: conference
- **Published**: 14-16 Jan.
- **Authors**: John T. Craddock, Mark F. Flanagan, Anthony D. Fagan
- **PDF**: https://ieeexplore.ieee.org/document/5755776
- **Abstract**: An LDPC code construction technique is proposed based on the structural properties of finite m-dimensional lattices. The Tanner graph of any code from this class is shown to have a girth of eight, and the number of proper eight-cycles in the graph is enumerated. The minimum distance of the codes is shown to be lower bounded by 2m. The codes are also shown to be highly flexible in terms of code length and rate, and compatible with a low-complexity serial-parallel decoder implementation based on the turbo-decoding message passing algorithm. Finally, simulation results over the AWGN channel demonstrate that these codes have good error-correcting performance.

## Multiple-Bases Belief-Propagation with Leaking for Decoding of Moderate-Length Block Codes

- **Status**: ✅
- **Reason**: MBBP 디코더 개선+PEG용 패리티검사 행렬 구성 알고리즘, 바이너리 LDPC BP 디코더/구성 기여(C/E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5755491
- **Type**: conference
- **Published**: 14-16 Jan.
- **Authors**: Thorsten Hehn, Johannes B. Huber, Pei He +1
- **PDF**: https://ieeexplore.ieee.org/document/5755491
- **Abstract**: Short algebraic codes promise low-delay data transmission and good performance results when transmitted over the additive white Gaussian noise (AWGN) channel and decoded by maximum-likelihood (ML) soft-decision decoding. One reason for this is the large minimum distance of these codes. For belief-propagation (BP) decoding, short algebraic codes show suboptimal results due to their high-density parity-check matrices. Using a collection of parity-check matrices for a given code, Multiple-Bases Belief-Propagation (MBBP) allows for decoding of many dense linear block codes with near ML performance. One convenient way to generate these matrices is using the automorphism group of a code. We point out limits of this approach and show two novel improvements, a decoder modification and a construction algorithm for parity-check matrices, which emphasize that MBBP is a more general approach and independent of the automorphism group. We use these methods to extend the field of application for MBBP to codes of moderate length. This includes codes with parity-check matrices tailored for BP decoding, in particular Progressive Edge-Growth (PEG) codes.
