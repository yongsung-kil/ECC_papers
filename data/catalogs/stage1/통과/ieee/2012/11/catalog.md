# IEEE Xplore — 2012-11 (1차선별 통과)


## LDPC-Based Lossless Compression of Nonstationary Binary Sources Using Sliding-Window Belief Propagation

- **Status**: ✅
- **Reason**: LDPC 무손실 압축용 슬라이딩윈도우 BP(SWBP) 알고리즘 제안 - 소스코딩이나 신규 BP 변형이 LDPC 디코더에 이식 가능성, 애매하여 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6266765
- **Type**: journal
- **Published**: November 2
- **Authors**: Yong Fang
- **PDF**: https://ieeexplore.ieee.org/document/6266765
- **Abstract**: Low-density parity-check (LDPC) codes have been used to implement lossless distributed or conventional source coding. However, block-wise LDPC codes are difficult to adapt to varying source statistics as traditional symbol-wise entropy coding techniques. In this paper, we propose the sliding-window belief propagation (SWBP) algorithm which is able to simultaneously recover the source and refine the estimate of varying source statistics. The SWBP is easy to implement and performs well in simulations.

## Progressive Differences Convolutional Low-Density Parity-Check Codes

- **Status**: ✅
- **Reason**: progressive differences 기반 신규 LDPC convolutional 코드 구성, 고정 최소거리·short cycle 제거 기법으로 코드 설계(E) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6307785
- **Type**: journal
- **Published**: November 2
- **Authors**: Marco Baldi, Marco Bianchi, Giovanni Cancellieri +1
- **PDF**: https://ieeexplore.ieee.org/document/6307785
- **Abstract**: We present a new family of low-density parity-check (LDPC) convolutional codes that can be designed using ordered sets of progressive differences. We study their properties and define a subset of codes in this class that have some desirable features, such as fixed minimum distance and Tanner graphs without short cycles. The design approach we propose ensures that these properties are guaranteed independently of the code rate. This makes these codes of interest in many practical applications, particularly when high rate codes are needed for saving bandwidth. We provide some examples of coded transmission schemes exploiting this new class of codes.

## Designing a Good Low-Rate Sparse-Graph Code

- **Status**: ✅
- **Reason**: linear d_min 보장하는 신규 저율 sparse-graph 코드 앙상블 설계(degree-1 비트)로 바이너리 LDPC 코드 설계(E) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6291708
- **Type**: journal
- **Published**: November 2
- **Authors**: Iryna Andriyanova, Jean-Pierre Tillich
- **PDF**: https://ieeexplore.ieee.org/document/6291708
- **Abstract**: This paper deals with the design of low-rate sparse-graph codes, having a linear minimum distance d_{min} in the blocklength n. Its main contributions are: a) a necessary condition on a general family of sparse-graph codes with linear d_{min}; b) a justification of having degree-1 bits in the low-rate code structure; c) a new, efficient ensemble of low-rate sparse-graph codes with bits of degree 1, designed so that the necessary condition (a) is satisfied.

## Efficient Algorithm for Finding Dominant Trapping Sets of LDPC Codes

- **Status**: ✅
- **Reason**: LDPC dominant trapping set 탐색 알고리즘 — error floor 추정·저-floor 코드 설계(E)에 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6259854
- **Type**: journal
- **Published**: Nov. 2012
- **Authors**: Mehdi Karimi, Amir H. Banihashemi
- **PDF**: https://ieeexplore.ieee.org/document/6259854
- **Abstract**: This paper presents an efficient algorithm for finding the dominant trapping sets of a low-density parity-check (LDPC) code. The algorithm can be used to estimate the error floor of LDPC codes or as a tool to design LDPC codes with low error floors. For regular codes, the algorithm is initiated with a set of short cycles as the input. For irregular codes, in addition to short cycles, variable nodes with low degree and cycles with low approximate cycle extrinsic message degree (ACE) are also used as the initial inputs. The initial inputs are then expanded recursively to dominant trapping sets of increasing size. At the core of the algorithm lies the analysis of the graphical structure of dominant trapping sets and the relationship of such structures to short cycles, low-degree variable nodes, and cycles with low ACE. The algorithm is universal in the sense that it can be used for an arbitrary graph and that it can be tailored to find a variety of graphical objects, such as absorbing sets and Zyablov-Pinsker trapping sets, known to dominate the performance of LDPC codes in the error floor region over different channels and for different iterative decoding algorithms. Simulation results on several LDPC codes demonstrate the accuracy and efficiency of the proposed algorithm. In particular, the algorithm is significantly faster than the existing search algorithms for dominant trapping sets.

## LDPC Decoder Using Pattern-Dependent Modified LLR for the Bit Patterned Media Storage With Written-In Errors

- **Status**: ✅
- **Reason**: 패턴 의존 수정 LLR을 LDPC 디코더 입력에 사용 — LLR 계산/입력 기법 이식 가능성(C), 애매하여 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6332943
- **Type**: journal
- **Published**: Nov. 2012
- **Authors**: Pornchai Supnithi, Warangrat Wiriya, Watid Phakphisut +1
- **PDF**: https://ieeexplore.ieee.org/document/6332943
- **Abstract**: The written-in errors in bit patterned media recording (BPMR) system cause the erroneous bits during the writing process leading to the performance degradation. In this work, we propose the pattern-dependent modified log-likelihood ratio (LLR) usage in low-density parity check (LDPC) decoder to reduce the written-in errors and also improve the write margin. Unlike the existing works, LLR computed based on the input data patterns is used at the LDPC decoder for the cascaded written-in error channel (WEC) with the additive white Gaussian noise (AWGN) channel. The proposed LDPC decoder outperforms the one with conventional LLR in terms of both the write margin, when the SNR is fixed at 5.5 dB, and the performance of LDPC decoder. The SNR gain is about 0.2 dB at the BER of 10- 6.

## A Fresh Look at Coding for  $q$-ary Symmetric Channels

- **Status**: ✅
- **Reason**: 바이너리 LDPC를 q-ary 채널에 쓰는 새 디코더(front-end factor-graph, 표준 BP 수정+EXIT 최적화) — 이식 가능 디코더(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6253262
- **Type**: journal
- **Published**: Nov. 2012
- **Authors**: Claudio Weidmann, Gottfried Lechner
- **PDF**: https://ieeexplore.ieee.org/document/6253262
- **Abstract**: This paper studies coding schemes for the q-ary symmetric channel based on binary low-density parity-check (LDPC) codes that work for any alphabet size q=2m, m ∈N, thus complementing some recently proposed packet-based schemes requiring large q . First, theoretical optimality of a simple layered scheme is shown; then, a practical coding scheme based on a simple modification of standard binary LDPC decoding is proposed. The decoder is derived from first principles and using a factor-graph representation of a front end that maps q -ary symbols to groups of m bits connected to a binary code. The front end can be processed with a complexity that is linear in m=log2q. An extrinsic information transfer chart analysis is carried out and used for code optimization. Finally, it is shown how the same decoder structure can also be applied to a larger class of q-ary channels.

## Low complexity product codes with LDPC codes achieving ultra low BER

- **Status**: ✅
- **Reason**: LDPC 디코딩 실패의 sparse 오류분포를 활용한 product code 설계로 ultra-low BER/error floor 개선, 코드설계(E) 이식 가능성 있어 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6511401
- **Type**: conference
- **Published**: 9-11 Nov. 
- **Authors**: Weigang Chen, Tongxin Dong
- **PDF**: https://ieeexplore.ieee.org/document/6511401
- **Abstract**: Ultra low bit error rate (BER) is required in high speed communications such as the 100 Gbit/s long haul optic communications. In this paper, a type of simple product codes is proposed using low density parity check (LDPC) codes with very high rate algebraic block codes by exploiting the sparsity of LDPC decoding failure and sparse error distribution in an LDPC frame with errors. Specifically, different with traditional product codes, the information bits are first encoded with very high rate algebraic block codes of low encoding and decoding complexity. Even the block codes correcting a single error using algebraic decoding method can be used. Then, LDPC codes are used as the inner code to obtain a low decoding threshold using iterative decoding. This design scheme can achieve the ultra low bit error rate at relatively low signal-to-noise ratios. The cost of the proposed scheme is the relatively large latency, which is not so critical for the ultra high speed communications.

## Performance study on implementation of DVB-S2 low density parity check codes on additive white Gaussian noise channel and Rayleigh fading channel

- **Status**: ✅
- **Reason**: DVB-S2 LDPC log-BP/min-sum의 정밀도·반복수 비교 및 세미병렬 FPGA 구현 지향 — D/C 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6507791
- **Type**: conference
- **Published**: 5-6 Nov. 2
- **Authors**: Hanady Hussien, Khaled Ali Shehata, Mohamed Khedr +1
- **PDF**: https://ieeexplore.ieee.org/document/6507791
- **Abstract**: Low density parity check (LDPC) codes are one of the best error correcting codes known to approach the Shannon limit. This paper examines the impact of different rates and code lengths of Log Belief Propagation LDPC algorithm on the performance of digital video broadcasting-satellite-second generation (DVB-S2) on both Additive white Gaussian Noise (AWGN) channel and Rayleigh fading channel, it also examines low complexity LDPC algorithm which is minimum sum LDPC algorithm for DVB-S2 with different numbers of iterations and simulating it on both channels using matlab targeting to chose the appropriate algorithm for the architecture of DVB-S2 to be implemented hierarchically on semi-parallel LDPC design Field Programmable Gate Array.

## A novel FPGA implementation of mirror-paradigm RS-based QC-LDPC decoder for NVM channels

- **Status**: ✅
- **Reason**: NVM용 RS기반 QC-LDPC의 메모리효율 mirror-paradigm 구성 + FPGA 구현 — 코드설계/HW(E/D), 바이너리
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6473593
- **Type**: conference
- **Published**: 4-7 Nov. 2
- **Authors**: Melvin Heng Li Lim, Wang Ling Goh, Zhiliang Qin
- **PDF**: https://ieeexplore.ieee.org/document/6473593
- **Abstract**: The scrutiny of the class of Reed-Solomon (RS) based quasi-cyclic (QC) low-density parity-check (LDPC) codes has inspired the authors to propose a memory efficient mirror-paradigm (MP) RS-based QC-LDPC code by exploiting the geometrical properties from the RS-based QC-LDPC nomenclature. Without any loss in performance, the proposed MPRS-based QC-LDPC code delivers discernible memory savings that address the concerns of hefty H-matrices associated to lengthy codewords for non-volatile memory (NVM) applications. Besides, the MPRS-based QC-LDPC codes are not confined to any particular hardware implementation and are compatible with various decoder architectures to complement other optimization schemes.

## A study into high-throughput decoder architectures for high-rate LDPC codes

- **Status**: ✅
- **Reason**: 고율 바이너리 LDPC용 고처리율 디코더 아키텍처(Split-Row Threshold, vertical scheduling) 비교/연구 — 이식 가능 HW(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:6407112
- **Type**: conference
- **Published**: 4-7 Nov. 2
- **Authors**: Yeong-Luh Ueng, Chung-Chao Cheng
- **PDF**: https://ieeexplore.ieee.org/document/6407112
- **Abstract**: This study investigates a variety of high-throughput decoder architectures designed for high-rate low-density parity-check (LDPC) codes. To implement a high-throughput decoder, a fully-parallel architecture can be adopted, but with complex interconnections. In order to reduce the routing complexity, a Split-Row Threshold decoder can be adopted. However, the high check-node degree of a high-rate LDPC code leads to a long critical path when using the Split-Row Threshold decoder. The long critical path can be shortened by using partially-parallel architectures combined with vertical scheduling. Two-phase message passing and shuffled message passing can be adopted in the vertical scheduling. The features of these state-of-the-art high-throughput decoder architectures and the associated comparison are presented in this paper.

## 7.7Gbps encoder design for IEEE 802.11n/ac QC-LDPC codes

- **Status**: ✅
- **Reason**: QC-LDPC 인코더 HW 아키텍처(부분병렬, 저복잡도 cyclic shifter, CMOS 구현) — 이식 가능 HW(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:6407078
- **Type**: conference
- **Published**: 4-7 Nov. 2
- **Authors**: Yongmin Jung, Chulho Chung, Jaeseok Kim +1
- **PDF**: https://ieeexplore.ieee.org/document/6407078
- **Abstract**: This paper proposes a high throughput encoding process and encoder architecture for quasi-cyclic low-density parity-check (QC-LDPC) codes in IEEE 802.11n/ac standards. In order to achieve the high throughput with low complexity, a partially parallel processing based encoding process and encoder architecture are proposed. Forward and backward accumulations are performed in one clock cycle to increase the encoder throughput. A low complexity cyclic shifter is also proposed to minimize the hardware overhead of combinational logic in the encoder architecture. The proposed encoder is implemented with 130-nm CMOS technology. For (1944, 1620) irregular code, 7.7 Gbps throughput is achieved at 100 MHz clock frequency. The gate count of the proposed encoder core is about 96 K.

## Low complexity full parallel Multi-Split LDPC decoder reusing sign wire of row processor

- **Status**: ✅
- **Reason**: Multi-Split LDPC 디코더 HW로 sign/magnitude wire 공유로 복잡도 절감 — 이식 가능 디코더/HW(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6407079
- **Type**: conference
- **Published**: 4-7 Nov. 2
- **Authors**: Byung Jun Choi, Jae Do Lee, Myung Hoon Sunwoo +1
- **PDF**: https://ieeexplore.ieee.org/document/6407079
- **Abstract**: This paper proposes a novel modified Multi-Split LDPC decoder. In the proposed design, wires are shared to communicate not only the signs, but also the magnitudes of the messages among adjacent partitions of the LDPC codes. As a result, the proposed decoder can achieve significant coding gain over existing designs when the same word length is used. In addition, the error correcting performance of the proposed decoder is better than prior decoders even when shorter word length is adopted. Synthesis was carried out for fully-parallel decoders of an example (504, 252) LDPC code. To achieve similar performance as previous effort, the proposed decoder requires 13% hardware complexity.

## Quantization, absorbing regions and practical message passing decoders

- **Status**: ✅
- **Reason**: 양자화-absorbing set 상호작용 분석 및 유한정밀 디코더 설계 가이드라인, 두 양자화 디코더 직렬화로 성능개선(C). NAND LLR 양자화에 직접 이식
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6489224
- **Type**: conference
- **Published**: 4-7 Nov. 2
- **Authors**: Behzad Amiri, Shayan Garani Srinivasa, Lara Dolecek
- **PDF**: https://ieeexplore.ieee.org/document/6489224
- **Abstract**: Low-density parity-check (LDPC) codes and accompanying message passing decoding algorithms are a popular choice for data encoding and decoding in modern communications and storage systems. To reduce implementation complexity, the messages in a practical message passing decoder are necessarily quantized. It is well known that the performance of practical, quantized message passing decoders in the high-reliability regime is governed by non-codeword decoding errors, typically described via trapping/absorbing sets. Absorbing regions act as “decoding regions” around absorbing sets. In this work, we take a closer look at the interplay between quantization and absorbing regions. We provide a study of a range of quantization choices, describe the impact of quantization on the candidate absorbing regions, and derive guidelines for practical finite-precision decoders. In particular, we show that, depending on the choice of the quantization allocation, different absorbing sets emerge as dominant: even though the overall performance of two quantization schemes can be similar, the distribution of decoding errors across possible absorbing sets can be substantially different. We take the advantage of disjointness of error profiles of two carefully chosen quantized decoders to design a decoder that is a series of these two decoders. The result is a performance improvement of at least an order magnitude relative to constituent decoders without increase in complexity.

## Iterative detection and decoding for MIMO systems with knowledge-aided belief propagation algorithms

- **Status**: ✅
- **Reason**: 단주기 이용·하이퍼그래프 reweighting 기반 새 BP 디코더 알고리즘(C). MIMO 응용이나 부호 비의존적 BP 개선으로 바이너리 LDPC에 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6489223
- **Type**: conference
- **Published**: 4-7 Nov. 2
- **Authors**: Jingjing Liu, Peng Li, Rodrigo C. de Lamare
- **PDF**: https://ieeexplore.ieee.org/document/6489223
- **Abstract**: In this paper, we consider the problem of iterative detection and decoding (IDD) for multi-antenna systems using low-density parity-check (LDPC) codes. The proposed IDD system consists of a soft-input soft-output parallel interference (PIC) cancellation scheme with linear minimum mean-square error (MMSE) receive filters and two novel belief propagation (BP) decoding algorithms. The proposed BP algorithms exploit the knowledge of short cycles in the graph structure and the reweighting factors derived from the hypergraph's expansion. Simulation results show that when used to perform IDD for multi-antenna systems both proposed BP decoding algorithms can consistently outperform existing BP techniques with a small number of decoding iterations.

## Iterative reduced-complexity detection for LDPC coded 2-D recording channels

- **Status**: ✅
- **Reason**: LDPC 코딩 2D ISI 채널 check node 연산 저복잡도화(부분집합 제한) — 디코더 복잡도 저감 기법이 BP에 이식 가능(C), 애매하면 in
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6407560
- **Type**: conference
- **Published**: 31 Oct.-2 
- **Authors**: Zhiliang Qin, Kui Cai, Kheong Sann Chan
- **PDF**: https://ieeexplore.ieee.org/document/6407560
- **Abstract**: In this paper, we consider iterative graph-based detection for low-density parity-check (LDPC) coded two-dimensional (2-d) intersymbol interference (ISI) channels and propose a novel approach to reduce the complexity of the check node operation in the channel Tanner Graph by restricting the computation to a small subset of binary vectors. Simulation results show that the proposed receiver approaches closely the performance of the full-complexity receiver with a much lower complexity.

## Cell-to-cell interference compensation schemes using reduced symbol pattern of interfering cells for MLC NAND flash memory

- **Status**: ✅
- **Reason**: MLC NAND 셀간간섭 보상 후 LDPC용 LLR 생성 — NAND 직접(A), LLR 양자화/생성 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6407527
- **Type**: conference
- **Published**: 31 Oct.-2 
- **Authors**: G. Kong, T. Kim, W. Xi +1
- **PDF**: https://ieeexplore.ieee.org/document/6407527
- **Abstract**: Cell-to-cell interference compensation schemes using reduced symbol pattern of interfering cells for multi-level cell (MLC) NAND flash memory are proposed in this paper. The proposed schemes contain three signal-processing techniques, estimating cell-to-cell interference, compensating cell-to-cell interference, and generating log-likelihood ratio (LLR). Firstly, reduced symbol pattern of interfering cells is used to easily estimate cell-to-cell interference by setting threshold voltage shift to be only two values in the programming state. Based on this estimation, cell-to-cell interference is compensated by modifying the read voltage in the proposed scheme 1 and by subtracting the estimated cell-to-cell interference from the sensed voltage in the proposed scheme 2. Finally, after conducting compensation, LLR is calculated for low-density parity check codes in the assumption of free cell-to-cell interference since interference between cells is mitigated by the compensation procedure. By using these techniques, the interference can be relaxed with a simpler structure and a higher reliability compared to the conventional methods for MLC NAND flash memory.

## Improved decoder design for LDPC codes based on selective node processing

- **Status**: ✅
- **Reason**: 선택적 노드 처리로 H 행렬 축약하는 신규 저복잡도 LDPC 디코더+세미패럴렐 고처리율 아키텍처 — 디코더(C)+HW(D) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6409113
- **Type**: conference
- **Published**: 30 Oct.-2 
- **Authors**: Sachin Singh Khati, Pooja Bisht, Subhash Chandra Pujari
- **PDF**: https://ieeexplore.ieee.org/document/6409113
- **Abstract**: This paper proposes a low complexity decoder design for low density parity check (ldpc) codes. The design primarily comprises a novel decoding algorithm and semi parallel high throughput architecture. Based on the observation that nodes with high log likelihood ratio provide almost same information in every iteration and can be deemed as static, we propose an algorithm in which the parity check matrix H is updated to a reduced form every time a static node is encountered resulting in lesser number of computations in subsequent iterations. Also the design greatly benefits from the area efficient semi-parallel architecture and the various improvisations introduced at different levels of abstraction in the decoder design. The decoder design is implemented for a ldpc code compliant with WLAN 802.11n standard using sum product algorithm. The simulation results showed a significantly higher throughput with an easily controllable increase in bit error rate.

## Low cost VLSI design of the LDPC decoder in Advanced Broadcasting System for Satellite

- **Status**: ✅
- **Reason**: QC-LDPC용 layered+sorted scheduling, scaled min-sum, CRC 조기종료 결합한 VLSI/FPGA 디코더 아키텍처(D/C) - 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6466751
- **Type**: conference
- **Published**: 29 Oct.-1 
- **Authors**: Jianing Su, Zhenghao Lu
- **PDF**: https://ieeexplore.ieee.org/document/6466751
- **Abstract**: In this paper, a low cost VLSI implementation of an LDPC decoder for the Advanced Broadcasting System of Satellite (ABS-S) is presented. The decoder is fully compatible with all the 8 code rates in ABS-S standard. The layered decoding with sorted scheduling architecture is employed and the scaled min-sum belief propagation method is used for check node update. The CRC check is embedded into the decoding process to gain the best early stopping effect in decoding iterations. The decoder is implemented in Altera FPGA and results show that the proposed decoder is suitable for satellite broadcasting application ABS-S and its scheme can be generalized in other quasi-cyclic structured LDPC codes.

## On the Generalized Belief Propagation and its dynamics

- **Status**: ✅
- **Reason**: Generalized BP + trapping-set 대응 region graph 구성(C) — 바이너리 LDPC Tanner 그래프 BP 개선 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6466622
- **Type**: conference
- **Published**: 26-29 Nov.
- **Authors**: Jean-Christophe Sibel, Sylvain Reynal
- **PDF**: https://ieeexplore.ieee.org/document/6466622
- **Abstract**: Numerous inference problems in statistical physics, computer vision or error-correcting coding theory consist in approximating the marginal probability distributions on Markov Random Fields (MRF). The Belief Propagation (BP) is an accurate solution that is optimal if the MRF is loop free and suboptimal otherwise. In the context of error-correcting coding theory, any Low-Density Parity-Check (LDPC) code has a graphical representation, the Tanner graph, which is a particular MRF. It is used as a media for the BP algorithm to correct the bits, damaged by a noisy channel, by estimating their probability distributions. Though loops and combination thereof in the Tanner graph prevent the BP from being optimal, especially harmful topological structures called the trapping-sets. The BP has been extended to the Generalized Belief Propagation (GBP). This message-passing algorithm runs on a non unique mapping of the Tanner graph, namely the regiongraph, such that its nodes are gatherings of the Tanner graph nodes. Then it appears the possibility to decrease the loops effect, making the GBP more accurate than the BP. In this article, we expose a novel region graph construction suited to the Tanner code, an LDPC code whose Tanner graph is entirely covered by trapping-sets. Furthermore, we investigate the dynamic behavior of the GBP compared with that of the BP to understand its evolution in terms of the Signal-to-Noise Ratio (SNR). To this end we make use of classical estimators and we introduce a new one called the hyperspheres method.

## Iterative detection scheme with LDPC codes for two-dimensional interference channels

- **Status**: ✅
- **Reason**: 2D interference 채널 joint detection-decoding+density evolution, NAND 셀간 간섭 유사 — 이식 가능 디코더/분석(C) 애매 보존
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6406178
- **Type**: conference
- **Published**: 21-23 Nov.
- **Authors**: Jun Yao, Kah Chan Teh, Kwok Hung Li
- **PDF**: https://ieeexplore.ieee.org/document/6406178
- **Abstract**: In this paper, an algorithm that performs joint iterative detection and decoding for 2D interference channels is proposed. Low-density parity-check (LDPC) codes are adopted as the error control codes in this system. The density evolution technique is further employed to track the message densities in the iterations. Using the density evolution technique, a threshold can be calculated which can be used to predict the performance of the system with long code length. Simulation results demonstrate that the proposed detection scheme outperforms some existing schemes. The density evolution technique is effective in analyzing the system performance.

## Serially concatenated codes with euclidean geometry LDPC and convolutional codes

- **Status**: ✅
- **Reason**: EG-LDPC+RSC 직렬연접+interleaver 저복잡 설계, EG-LDPC 코드설계 요소 이식 여지(E) — 애매하여 보존
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6406177
- **Type**: conference
- **Published**: 21-23 Nov.
- **Authors**: Sina Vafi, Huu Dung Pham
- **PDF**: https://ieeexplore.ieee.org/document/6406177
- **Abstract**: This paper presents a new scheme of serially concatenated codes. It is formed by a combination of Euclidean Geometry (EG) Low Density Parity Check (LDPC) and Recursive Systematic Convolutional (RSC) codes linked by the row-column interleaver. A modification is proposed on the interleaver, which improves performance of concatenated codes. This is conducted by recognition of patterns producing low-weights for both LDPC and RSC codes. Simulation results confirm that with similar rates and less decoding complexity, newly designed codes outperform product codes constituted by two cyclic EG codes.

## A novel region graph construction based on trapping sets for the Generalized Belief Propagation

- **Status**: ✅
- **Reason**: Trapping set 기반 region graph로 GBP 디코더 개선 — BP 한계 극복 신규 디코더 기법(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6406159
- **Type**: conference
- **Published**: 21-23 Nov.
- **Authors**: Jean-Christophe Sibel, Sylvain Reynal, David Declercq
- **PDF**: https://ieeexplore.ieee.org/document/6406159
- **Abstract**: The Belief Propagation (BP) is an inference algorithm used to estimate marginal probability distributions for any Markov Random Field (MRF). In the realm of Low-Density Parity-Check (LDPC) codes that can be represented by MRF called Tanner graphs, the BP is used as a decoding algorithm to estimate the states of bits sent through a noisy channel. Known to be optimal when the Tanner graph is a tree, the BP suffers from suboptimality when the Tanner graph has a loop-like topology. Furthermore, combinations of loops, namely the trapping sets, are particularly harmful for the decoding. To circumvent this problem were proposed other algorithms, like the Generalized Belief Propagation (GBP) that comes from statistical physics. This algorithm allows to absorb topological structures inside new nodes called regions. An advantage is that the resulting graph, the region graph, is not unique then according to its construction this region graph is a media for the GBP that can provide more accurate estimates than the BP. In this paper, we propose novel constructions of the region graph for the famous Tanner code of length N = 155 by making use of the trapping sets as basis for the regions.

## A Construction Method of QC-LDPC Codes without Short Cycles

- **Status**: ✅
- **Reason**: short cycle(4/6) 제거 QC-LDPC 구성법 — E 바이너리 코드 설계 기법
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6405647
- **Type**: conference
- **Published**: 2-4 Nov. 2
- **Authors**: Jianwu Zhang, Chengxia Li, Jianrong Bao
- **PDF**: https://ieeexplore.ieee.org/document/6405647
- **Abstract**: Low-density Parity-check (LDPC) coding is a class of advanced channel coding techniques. To improve the performance of LDPC codes, a simple and effective method to construct QC-LDPC codes without short cycles (cycles of length four and six) is proposed. The approach is especially effective when the parity-check matrix of QC-LDPC codes is composed of circulant permutation matrices. Firstly, we analyze the shapes of the cycles in the exponent matrix, to get the required conditions of no four-cycles and six-cycles. Then we show how to construct the parity-check matrix without four-cycles and six-cycles by filling rows of the exponent matrix with arithmetic sequences. Simulation results show that the proposed codes have better performance than array codes. Though the performance of the proposed codes is not as well as random codes at higher Eb/N0, they can be applied to practical communications because of being encoded in linear time with shift registers.

## Design of irregular LDPC codes for nonparametric channels

- **Status**: ✅
- **Reason**: 히스토그램 기반 비모수 채널용 비정규 LDPC 설계+soft-decision 디코더 확장 - 코드설계/디코더 이식 가능(C/E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6408080
- **Type**: conference
- **Published**: 15-16 Nov.
- **Authors**: W. Proß, M. Otesteanu, F. Quint
- **PDF**: https://ieeexplore.ieee.org/document/6408080
- **Abstract**: In this paper we propose a design-method for irregular LDPC codes in the context of channels, that can not sufficiently be described with the known parametric channel-models. We introduce a very flexible histogram-based channel-model. Furthermore a design-method based on the downhill simplex optimization is explained for the design of irregular LDPC codes in the context of histogram-based channel-models. We also propose an extension for soft-decision based LDPC decoders and explain the simulation of LDPC codes considering histogram-based channels-models. Following results based on a 2-state Markov-model prove the effectiveness of our design-method, the description of the channel and the decoding based on histograms.

## Message-passing decoding beyond the girth with local-optimality guarantees

- **Status**: ✅
- **Reason**: 신규 메시지패싱 디코더 NWMS(min-sum 변형, girth 넘는 local-optimality 보장)로 바이너리 LDPC BP에 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6376924
- **Type**: conference
- **Published**: 14-17 Nov.
- **Authors**: Nissim Halabi, Guy Even
- **PDF**: https://ieeexplore.ieee.org/document/6376924
- **Abstract**: We present a new message-passing iterative decoding algorithm, called normalized weighted min-sum (NWMS). NWMS-decoding is a BP-type algorithm that applies to any irregular Tanner code with single parity-check local codes (e.g., LDPC codes and HDPC codes). The decoding guarantee of NWMS applies whenever there exists a locally optimal codeword. We prove that if a locally-optimal codeword with respect to height parameter h exists, then NWMS-decoding finds it in h iterations. This decoding guarantee holds for every finite value of h and is not limited by the girth. Because local optimality of a codeword implies that it is the unique ML-codeword, the decoding guarantee also has an ML-certificate.
