# IEEE Xplore — 2013-10 (1차선별 통과)


## Finite Alphabet Iterative Decoders—Part II: Towards Guaranteed Error Correction of LDPC Codes via Iterative Decoder Diversity

- **Status**: ✅
- **Reason**: FAID(유한알파벳 반복 디코더) 다양성으로 trapping set/error floor 개선, 바이너리 LDPC 디코더 알고리즘(C)으로 NAND 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6600720
- **Type**: journal
- **Published**: October 20
- **Authors**: David Declercq, Bane Vasic, Shiva Kumar Planjery +1
- **PDF**: https://ieeexplore.ieee.org/document/6600720
- **Abstract**: Recently, we introduced a new class of finite alphabet iterative decoders (FAIDs) for low-density parity-check (LDPC) codes. These decoders are capable of surpassing belief propagation (BP) in the error floor region on the binary symmetric channel (BSC) with much lower complexity. In this paper, we introduce a novel scheme with the objective of guaranteeing the correction of a given and potentially large number of errors on column-weight-three LDPC codes. The proposed scheme uses a plurality of FAIDs which collectively correct more error patterns than a single FAID on a given code. The collection of FAIDs utilized by the scheme is judiciously chosen to ensure that individual decoders have different decoding dynamics and correct different error patterns. Consequently, they can collectively correct a diverse set of error patterns, which is referred to as decoder diversity. We provide a systematic method to generate the set of FAIDs for decoder diversity on a given code based on the knowledge of the most harmful trapping sets present in the code. Using the well-known column-weight-three (155,64) Tanner code with dmin = 20 as an example, we describe the method in detail and show, by means of exhaustive simulation, that the guaranteed error correction capability on short length LDPC codes can be significantly increased with decoder diversity.

## Tree-Structured Expectation Propagation for LDPC Decoding over BMS Channels

- **Status**: ✅
- **Reason**: BMS 채널용 tree-structured EP 디코더(BP 개선, 유한길이 error rate 감소)-바이너리 LDPC BP에 이식 가능한 신규 디코더(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6587624
- **Type**: journal
- **Published**: October 20
- **Authors**: Luis Salamanca, Pablo M. Olmos, Fernando Perez-Cruz +1
- **PDF**: https://ieeexplore.ieee.org/document/6587624
- **Abstract**: In this paper, we put forward the tree-structured expectation propagation (TEP) algorithm for decoding block and convolutional low-density parity-check codes over any binary channel. We have already shown that TEP improves belief propagation (BP) over the binary erasure channel (BEC) by imposing marginal constraints over a set of pairs of variables that form a tree or a forest. The TEP decoder is a message-passing algorithm that sequentially builds a tree/forest of erased variables to capture additional information disregarded by the standard BP decoder, which leads to a noticeable reduction of the error rate for finite-length codes. In this paper, we show how the TEP can be extended to any channel, specifically to binary memoryless symmetric (BMS) channels. We particularly focus on how the TEP algorithm can be adapted for any channel model and, more importantly, how to choose the tree/forest to keep the gains observed for block and convolutional LDPC codes over the BEC.

## Finite Alphabet Iterative Decoders—Part I: Decoding Beyond Belief Propagation on the Binary Symmetric Channel

- **Status**: ✅
- **Reason**: BSC용 Finite Alphabet Iterative Decoders(FAID)-3비트 정밀도로 error floor서 BP 능가, NAND 바이너리 LDPC 유한정밀 디코더로 직접 이식(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6600695
- **Type**: journal
- **Published**: October 20
- **Authors**: Shiva Kumar Planjery, David Declercq, Ludovic Danjean +1
- **PDF**: https://ieeexplore.ieee.org/document/6600695
- **Abstract**: We introduce a new paradigm for finite precision iterative decoding on low-density parity-check codes over the binary symmetric channel. The messages take values from a finite alphabet, and unlike traditional quantized decoders which are quantized versions of the belief propagation (BP) decoder, the proposed finite alphabet iterative decoders (FAIDs) do not propagate quantized probabilities or log-likelihoods and the variable node update functions do not mimic the BP decoder. Rather, the update functions are maps designed using the knowledge of potentially harmful subgraphs that could be present in a given code, thereby rendering these decoders capable of outperforming the BP in the error floor region. On certain column-weight-three codes of practical interest, we show that there exist {FAIDs that surpass the floating-point BP decoder in the error floor region while requiring only three bits of precision for the representation of the messages}. Hence, FAIDs are able to achieve a superior performance at much lower complexity. We also provide a methodology for the selection of FAIDs that is not code-specific, but gives a set of candidate FAIDs containing potentially good decoders in the error floor region for any column-weight-three code. We validate the code generality of our methodology by providing particularly good three-bit precision FAIDs for a variety of codes with different rates and lengths.

## VLSI Architecture for Layered Decoding of QC-LDPC Codes With High Circulant Weight

- **Status**: ✅
- **Reason**: circulant weight K>=1 지원 QC-LDPC 레이어드 디코더 VLSI 아키텍처, 바이너리 LDPC HW(D)로 NAND 이식 가능
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:6338364
- **Type**: journal
- **Published**: Oct. 2013
- **Authors**: Yang Sun, Joseph R. Cavallaro
- **PDF**: https://ieeexplore.ieee.org/document/6338364
- **Abstract**: In this brief, we propose a high-throughput layered decoder architecture to support a broader family of quasicyclic low-density parity-check (QC-LDPC) codes, whose parity-check matrices are constructed from arrays of circulant submatrices. Each nonzero circulant submatrix is a superposition of K cyclic-shifted identity matrices, where the circulant weight K ≥ 1. We propose a novel layered decoder architecture to support QC-LDPC codes with any circulant weight. We present a block-serial decoding architecture which processes a layer of a parity check matrix block by block, where each block is a Z×Z circulant matrix with a circulant weight of K. In the case study, we demonstrate an LDPC decoder design for the China Mobile Multimedia Broadcasting (CMMB) standard, which was synthesized for a TSMC 65-nm CMOS technology. With a core area of 3.9 mm2, the CMMB LDPC decoder achieves a maximum throughput of 1.1 Gb/s with 15 iterations.

## FPGA accelerator of Quasi cyclic EG-LDPC codes decoder for NAND flash memories

- **Status**: ✅
- **Reason**: NAND 플래시용 QC EG-LDPC 디코더 FPGA 가속기, layered+병렬 CNP HW 아키텍처 (A/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6661539
- **Type**: conference
- **Published**: 8-10 Oct. 
- **Authors**: Syed Azhar Ali Zaidi, Muhammad Awais, Carlo Condo +2
- **PDF**: https://ieeexplore.ieee.org/document/6661539
- **Abstract**: High rate low density parity check (LDPC) codes that are employed in NAND flash memories are required to have excellent error correcting performance and should avoid error floors at low bit error rate. For evaluating the performance of error correcting codes FPGA based accelerators are used. This paper presents a high speed, partially parallel and flexible decoder design for evaluating the performance of regular Quasi cyclic LDPC codes. We have targeted euclidean geometry (EG) LDPC codes which have high code rate and good error correcting performance. The throughput of the decoder is increased by using a fully parallel check node processor along with the layered decoding algorithm. The proposed decoder is implemented on XILINX XC7V2000T FPGA device. Synthesis results show that the proposed decoder is 60% faster as compared to the previously published FPGA implementations and is also capable of decoding high circulant weight EG-LDPC codes.

## Rapid design and prototyping of a reconfigurable decoder architecture for QC-LDPC codes

- **Status**: ✅
- **Reason**: QC-LDPC용 재구성 가능 ASIP 디코더 아키텍처(가변 블록/코드레이트) — 이식 가능 HW(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:6683963
- **Type**: conference
- **Published**: 3-4 Oct. 2
- **Authors**: Purushotham Murugappa, Vianney Lapotre, Amer Baghdadi +1
- **PDF**: https://ieeexplore.ieee.org/document/6683963
- **Abstract**: Many modern and emerging designs require having efficient dynamically reconfigurable and reprogrammable processors. However, when the implemented design needs an upgrade, newly added features have to be quickly supported and validated. This is clearly noticed in modern receivers of recent wireless communication standards that feature continuously different frame lengths and code rates for the channel decoder. This paper explores with an example the possibility of realizing a flexible channel decoder to implement and validate new/incremental algorithm changes with fast turnaround time in design. An application specific instruction-set processor (ASIP) is proposed as flexible core that can decode low-density parity-check (LDPC) codes with the various block sizes and code rates as specified in WiFi and WiMAX standards. Furthermore, the proposed architecture enables quick support of other Quasi-Cyclic LDPC (QC-LDPC) codes, e.g. DVB-S2, with simple incremental hardware changes at design time.

## Reduced complexity implementation of quasi-cyclic LDPC decoders by parity-check matrix reordering

- **Status**: ✅
- **Reason**: QC-LDPC layered 디코더 패리티검사행렬 재정렬로 병렬도 감소 신규 HW 기법(D), NAND QC-LDPC 이식 가능
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:6811974
- **Type**: conference
- **Published**: 28-31 Oct.
- **Authors**: Jianing Su, Zhenghao Lu
- **PDF**: https://ieeexplore.ieee.org/document/6811974
- **Abstract**: The layered scheme is famous for its efficiency and high throughput structure in decoding of LDPC codes, especially the quasi-cyclic LDPC codes, whose parity check matrices are made of cyclically-shifted identity matrices, which can be used as natural partitions of decoding layers. However, for many QC-LDPC codes, it leads to serious routing congestion if the cyclically shifted identity matrix size is taken directly as the layer partition and parallel factor in decoding. In this paper, a parity-check matrix reordering method is introduced, which can lower the decoding parallelism while keeping the layered decoding structure at the same time. The LDPC codes in DVB-S2/T2 standards are taken as an example to illustrate the proposed method, simulation and FPGA implementation shows that the method is effective in reducing the total decoder cost.

## A high-throughput LDPC decoder for optical communication

- **Status**: ✅
- **Reason**: 고처리율 Min-Sum 완전병렬 디코더 clock multiplexing 신규 HW 아키텍처, NAND 이식 가능(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6811973
- **Type**: conference
- **Published**: 28-31 Oct.
- **Authors**: Di Wu, Yun Chen, Yuebin Huang +3
- **PDF**: https://ieeexplore.ieee.org/document/6811973
- **Abstract**: As Optical Communication is on the way, conventional LDPC decoders do not work well with the requirement for high throughput over 100 Gb/s. Many new LDPC decoder structures aiming at high throughput have been proposed, such as stochastic decoders, bit serial decoders, digit serial decoders and so forth. In this paper, a Min-Sum fully parallel structure using clock multiplexing is proposed, as an attempt to relieve the wiring problem. This decoder makes full use of clock edges comparing to conventional decoders. With SIMC 0.13um technology, our decoder achieves a throughput of 54.2 Gb/s at 200MHz for the WiMAX standard of 5/6 code rate. Our conjecture is that with lower feature size and higher clock frequency, 100 Gb/s could be achieved.

## VLSI design of fuzzy-decision bit-flipping QC-LDPC decoder

- **Status**: ✅
- **Reason**: MLC NAND용 fuzzy-decision bit-flipping QC-LDPC 디코더 VLSI 신규 알고리즘+HW(A/C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6811972
- **Type**: conference
- **Published**: 28-31 Oct.
- **Authors**: Wenzhe Zhao, Minjie Lv, Hongbin Sun +2
- **PDF**: https://ieeexplore.ieee.org/document/6811972
- **Abstract**: In MLC NAND flash system, the hybrid hard-decision /soft-decision LDPC decoder prefers a high throughput bit-flipping decoder. Therefore, the high-efficiency silicon implementation of bit-flipping decoder becomes a practically relevant topic. This paper presents a so-called fuzzy-decision bit-flipping decoding algorithm to reduce the hardware consumption and average iteration numbers. Simulations and VLSI design show that the proposed design solution can improve upto 10% higher decoding throughput, and meanwhile reduce upto 40% less silicon cost, without performance reducing.

## Length-compatible PEG-CRT algorithm

- **Status**: ✅
- **Reason**: PEG-CRT 코드 구성을 길이 호환으로 확장(girth 유지, 가변 길이/율) - 바이너리 LDPC 코드설계(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6677054
- **Type**: conference
- **Published**: 24-26 Oct.
- **Authors**: Xueqin Jiang, Hongyun Guan, Moon Ho Lee +1
- **PDF**: https://ieeexplore.ieee.org/document/6677054
- **Abstract**: Among the existing methods for the construction of random-like LDPC codes, one of the most successful approaches is progressive-edge-growth (PEG) algorithm. This approach is simple but the complexity of the PEG algorithm scale as O(nm), where n is the number of symbol nodes and m is the number of check nodes. The PEG-CRT algorithm deals with this problem by construct a base matrix Hb of size mb × nb with the PEG algorithm and expand this base matrix into a parity-check matrix H of size m × n via the chinese remainder theorem (CRT), where m >> mb and n >> nb. The size of the base matrix is expanded without decreasing the girth. Since a smaller matrix is constructed with the PEG algorithm and the complexity of the CRT computation is negligible compared to the PEG algorithm, the complexity of the whole code construction process is reduced. However, unlike the PEG LDPC codes, the code lengths of PEG-CRT LDPC codes are not flexible. To solve this problem, in this paper, we propose a length compatible PEG-CRT algorithm, which preserves good properties such as large girths, flexible code rates, flexible code length and low densities.

## LDPC codes based on MPEG algorithm for block fading channels

- **Status**: ✅
- **Reason**: 개선된 PEG(MPEG, ACE 메트릭) 코드 구성으로 girth 최대화·iteration 감소; 바이너리 LDPC 코드설계 기법 이식 가능(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6718855
- **Type**: conference
- **Published**: 22-25 Oct.
- **Authors**: Shan Ding, Ya-nan Zhao
- **PDF**: https://ieeexplore.ieee.org/document/6718855
- **Abstract**: This paper presents a novel algorithm to design Root-LDPC codes based on improved PEG algorithm for block fading channels. The modified Progressive Edge-Growth (MPEG) algorithm is a PEG algorithm with Approximated Cycle Extrinsic Message Degree (ACE) metric, which is used to describe the connectivity of cycles. The approach can maximize the girth of the cycles, improve the connectivity of cycles. Simulation results demonstrate that the algorithm we proposed can achieve full diversity and significantly better code performance, suitable to different fading blocks. From medium to high SNR, the average required number of iterations can be decreased.

## Anytime characteristics of spatially coupled code

- **Status**: ✅
- **Reason**: SC-LDPC 기반 anytime 부호 + adaptive window decoding(저복잡도) - 코드설계(E)+디코더(C) 이식 가능, BEC 바이너리
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6736543
- **Type**: conference
- **Published**: 2-4 Oct. 2
- **Authors**: Md. Noor-A-Rahim, Khoa D. Nguyen, Gottfried Lechner
- **PDF**: https://ieeexplore.ieee.org/document/6736543
- **Abstract**: In this paper, we propose an efficient channel coding scheme for anytime communications. We design this anytime code based on spatially coupled LDPC codes and investigate the performance over binary erasure channels. Through density evolution analysis, we asymptotically show the desired anytime properties of the proposed code. We also numerically predict the finite-length performance of the anytime code. We develop an adaptive window decoding technique to ensure a low complexity anytime receiver. Through simulation, we compare the performance of our proposed code with existing anytime codes.

## On the convergence speed of spatially coupled LDPC ensembles

- **Status**: ✅
- **Reason**: SC-LDPC BP 수렴속도 상한 유도, degree profile 최적화로 수렴 가속 - 바이너리 SC-LDPC 코드설계(E) 기여
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6736544
- **Type**: conference
- **Published**: 2-4 Oct. 2
- **Authors**: Vahid Aref, Laurent Schmalen, Stephan ten Brink
- **PDF**: https://ieeexplore.ieee.org/document/6736544
- **Abstract**: Spatially coupled low-density parity-check codes show an outstanding performance under the low-complexity belief propagation (BP) decoding algorithm. They exhibit a peculiar convergence phenomenon above the BP threshold of the underlying non-coupled ensemble, with a wave-like convergence propagating through the spatial dimension of the graph, allowing to approach the MAP threshold. We focus on this particularly interesting regime in between the BP and MAP thresholds. On the binary erasure channel, it has been proved [1] that the information propagates with a constant speed toward the successful decoding solution. We derive an upper bound on the propagation speed, only depending on the basic parameters of the spatially coupled code ensemble such as degree distribution and the coupling factor w. We illustrate the convergence speed of different code ensembles by simulation results, and show how optimizing degree profiles helps to speed up the convergence.

## Taylor-Kuznetsov fault-tolerant memories: A survey and results under correlated gate failures

- **Status**: ✅
- **Reason**: Taylor-Kuznetsov 결함허용 메모리 서베이지만 LDPC 기반 메모리 아키텍처와 상관 게이트 고장 신규 분석, 애매하여 in으로 살림(Phase3 재검토)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:6704419
- **Type**: conference
- **Published**: 16-19 Oct.
- **Authors**: Srdjan Brkic, Predrag Ivanis, Goran Djordjevic +1
- **PDF**: https://ieeexplore.ieee.org/document/6704419
- **Abstract**: This paper gives a brief survey of information theoretic results on fault-tolerant memory systems. The main focus is on Taylor-Kuznetsov memory architecture which has been shown to achieve nonzero computational capacity. A new approach for analyzing fault-tolerant memories that takes into account gate failure correlation is also presented. The analysis was done by modelling gate failures by Markov chain.

## An area and energy efficient half-row-paralleled layer LDPC decoder for the 802.11AD standard

- **Status**: ✅
- **Reason**: half-row-paralleled layered LDPC 디코더 HW 아키텍처(single permutation network, 면적·에너지 효율), 이식 가능 HW(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:6674490
- **Type**: conference
- **Published**: 16-18 Oct.
- **Authors**: Meng Li, Frederik Naessens, Peter Debacker +5
- **PDF**: https://ieeexplore.ieee.org/document/6674490
- **Abstract**: Multi-gigabit LDPC decoders are demanded by standards such as IEEE 802.11ad and IEEE 802.15.3c. In order to achieve high throughput, most published multi-gigabit designs use row-paralleled architecture. In this paper, we proposed a half-row paralleled LDPC decoder with half layer level pipeline and single permutation network for the 802.11ad standard, which reduces the hardware resources almost by half compared to the state-of-the-art row-paralleled LDPC decoder, achieving a good trade-off between energy efficiency and area efficiency. The decoder achieves a throughput of 5.6 Gbps and consumes only 99 mW for the highest coding rate 13/16 at 5 iterations, working at 500 MHz by using 40nm G technology, yielding an energy efficiency of 3.53 pJ/bit/iteration and area efficiency of 35 Gbps/sqmm.

## High-speed conflict-free layered LDPC decoder for the DVB-S2, -T2 AND -C2 standards

- **Status**: ✅
- **Reason**: layered 디코딩 메모리 업데이트 충돌 해소(layer repetition+write disable) 신규 HW 기법, 이식 가능(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:6674491
- **Type**: conference
- **Published**: 16-18 Oct.
- **Authors**: C. Marchand, L. Conde-Canencia, E. Boutillon
- **PDF**: https://ieeexplore.ieee.org/document/6674491
- **Abstract**: Layered decoding is known to provide efficient and high-throughput implementation of LDPC decoders. However, the implementation of layered architecture is not always straightforward because of memory update conflicts in the a posteriori information memory. In this paper, we focus our attention on a particular type of conflict that is due to multiple-diagonal sub-matrices in the DVB-S2, -T2 and -C2 parity-check matrices. We propose an original solution that combines repetition of the concerned layers and the write disable of the a posteriori information memory. The implementation of this solution on an FPGA-based LDPC decoder led to an average air throughput of 200 Mbit/s with a parallelism of 45 and a clock frequency of 300 MHz. Increasing the parallelism to 120 led to an average air throughput of 720 Mbit/s with a clock frequency of 400 MHz on CMOS technology.

## A semi-analytical bivariate Gaussian model of the approximation error impact on the Min-Sum LDPC decoding algorithm

- **Status**: ✅
- **Reason**: Min-Sum/normalized/offset MS 근사오차의 이론모델·성능예측 기법, 부호 비의존 디코더 분석으로 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6674486
- **Type**: conference
- **Published**: 16-18 Oct.
- **Authors**: Nikos Kanistras, Vassilis Paliouras
- **PDF**: https://ieeexplore.ieee.org/document/6674486
- **Abstract**: In this paper, a new theoretical model that describes the impact of the approximation error on the decisions taken by LDPC decoders is discussed. In particular, the theoretical model extends previous results and reconstructs the mechanism, by means of which the approximation error alters the decisions of the decoding algorithm, with respect to the decisions taken by the optimal decoding algorithm, namely Log Sum-Product. We focus on the most popular algorithm for LDPC decoding, namely Min-Sum and its also popular modifications, normalized and offset Min-Sum. The model is applied to all of these decoding algorithms, which are actually approximations of the Log Sum-Product. Moreover a method that exploits the output of the proposed model in order to estimate the decoding performance is also proposed. Finally, experimental results prove the validity of both the proposed model and the method, demonstrating the usefulness of this contribution towards achieving accurate decoding behavior prediction without relying on time-consuming simulations.

## A class of structured quasi-cyclic LDPC codes based on planar difference families

- **Status**: ✅
- **Reason**: planar difference family 기반 QC-LDPC 구성, 4-cycle 제거·최소거리 개선 (E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6698188
- **Type**: conference
- **Published**: 16-18 Oct.
- **Authors**: Shady M. Ibraheem, M. M. Abd Elrazzak, Salwa M. Serag Eldin +2
- **PDF**: https://ieeexplore.ieee.org/document/6698188
- **Abstract**: This paper is devoted to introduce a special classes of (QC-LDPC) with very restricted code parameters based on planar difference families. Such difference families could be obtained by numerical analysis and computer programs. The resulting codes have parity check matrices with column-weight greater than three, at least no 4-cycle and approximately full rank. It can be noted that the construction based on planar difference families exhibits more flexibility than that based on difference sets in terms of length and code rate selections. Besides, the more increasing in the column-weights of parity check matrices of QC-LDPC codes, the more improvement in the minimum distances of them. Simulation results show that over the additive white Gaussian noise channel, these codes could outperform their randomly constructed counterparts.

## A construction of LDPC codes with low error floors

- **Status**: ✅
- **Reason**: masked LU 코드 기반 low error floor 바이너리 LDPC 구성·stopping distance 하한 (E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6698119
- **Type**: conference
- **Published**: 16-18 Oct.
- **Authors**: Tsung-Hsin Yeh, Wen-Yao Chen, Chung-Chin Lu
- **PDF**: https://ieeexplore.ieee.org/document/6698119
- **Abstract**: In this paper, we propose an effective method to construct practical LDPC codes with low error floors. We first consider a class of LDPC codes, called masked Lazebnik-Ustimenko (LU) codes each of which is obtained by removing edges and nodes from the Tanner graph of an LU code and may have arbitrary large girth and high code rate. We then derive a lower bound for the stopping distance of a masked LU code and develop a simple method to further purge edges and nodes to obtain a small code ensemble with relatively lower error floors than the original masked LU code ensemble.

## A class of doubly-generalized LDPC codes

- **Status**: ✅
- **Reason**: DGLDPC 신규 저복잡도 반복 디코딩 알고리즘 제시, 바이너리 BP 이식 가능 (C/E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6698122
- **Type**: conference
- **Published**: 16-18 Oct.
- **Authors**: Y. Min, F. C. M. Lau, C. K. Tse
- **PDF**: https://ieeexplore.ieee.org/document/6698122
- **Abstract**: We propose a class of doubly-generalized LDPC (DGLDPC) codes that use single-parity-check (SPC) codes as component codes at the super-variable nodes (SVNs) and SPC product-codes (SPC-PCs) as component codes at the super-check nodes (SCNs). We propose a low-complexity iterative decoding algorithm catered for the special structures of the SPC-PCs. Finally, we present the error performance and the convergence rate of the proposed DGLDPC codes.

## A new dimension of parallelism in ultra high throughput LDPC decoding

- **Status**: ✅
- **Reason**: 초고속 병렬 LDPC 디코더의 routing congestion 저감 아키텍처(새 병렬화 차원), 이식 가능 HW(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:6674497
- **Type**: conference
- **Published**: 16-18 Oct.
- **Authors**: Philipp Schläfer, Norbert Wehn, Matthias Alles +1
- **PDF**: https://ieeexplore.ieee.org/document/6674497
- **Abstract**: In modern communication systems the required data rates are continuously increasing. High speed transmissions can easily generate throughputs far beyond 1 Tbit/s. To ensure error free communication, channel codes like Low-Density Parity Check (LDPC) codes are utilized. However state-of-the-art LDPC decoders can process only data rates in the range of 10 to 50 Gbit/s. This results in a gap in decoder performance which has to be closed. Therefore we propose a new ultra high speed LDPC decoder architecture. We show that our architecture significantly reduces the routing congestion which poses a big problem for fully parallel, high speed LDPC decoders. The presented 65nm ASIC implementation runs at 257 MHz and consumes an area of 12 mm2The resulting system throughput is 160 Gbit/s, it is the fastest LDPC decoder which has been published up to now. At the same time we show that extremely parallel architectures do not only increase the maximum throughput but also increase area and power efficiency in comparison to state-of-the-art decoders.

## A conflict-free memory mapping approach to design parallel hardware interleaver architectures with optimized network and controller

- **Status**: ✅
- **Reason**: 병렬 디코더용 conflict-free 메모리 매핑/인터리버 네트워크 설계 기법, LDPC 병렬 HW에 이식 가능(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:6674505
- **Type**: conference
- **Published**: 16-18 Oct.
- **Authors**: Aroua Briki, Cyrille Chavet, Philippe Coussy
- **PDF**: https://ieeexplore.ieee.org/document/6674505
- **Abstract**: Recent communication standards and storage systems (e.g. wireless access, digital video broadcasting or magnetic storage in hard disk drives) uses error correcting codes such as LDPC (Low Density Parity Check) or Turbo-codes to reliably transfer data between source and destination. For high data rate applications, Turbo and LDPC codes are decoded on parallel architectures. However, parallel architectures suffer from memory access conflicts and efficient memory mapping algorithms are required to design parallel interleaver architectures which are one of the most critical parts of parallel decoders. In this paper, we present a method that finds a conflict-free memory mapping for any interleaving law and associated parallelism constraint. The proposed approach always complies with the interconnection network topology the designer wants to infer. Moreover, contrary to traditional methods, the resulting architecture is optimized by reducing the cost of network and controller (network and memory controller) architectures. Our approach is compared with state of the art techniques and its interest is shown through the design of parallel interleavers used in different industrial applications such as High Speed Downlink Packet Access (HSDPA), Multi Band-Orthogonal Frequency-Division Multiplexing Ultra-WideBand (MB-OFDM UWB) and a WiMAX application.

## Performance comparison of LDPC convolutional codes for memory size and encoder block size

- **Status**: ✅
- **Reason**: LDPC-CC 메모리/블록크기 성능 비교 및 H행렬 sub-matrix 확장 연산 제시, 코드 설계(E) 이식 가능 가능성으로 애매시 in
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6675408
- **Type**: conference
- **Published**: 14-16 Oct.
- **Authors**: Ki-Hyeon Park, Jin Soo Park, Jung-Hyun Kim +3
- **PDF**: https://ieeexplore.ieee.org/document/6675408
- **Abstract**: In this paper, we compare the performance of some different types of time-invariant LDPC convolutional codes. We first confirm the well-known fact that the performance can be increased by increasing the number of delay, i.e. memory size. Then, we show by simulation that increasing the encoder block size may possibly increase the performance when the memory size is fixed, but this must be done properly. We show also that the performance is comparable when the constraint lengths are comparable regardless of memory size and encoder block size. For all these, we introduce a matrix expansion operation for various sizes of sub-matrices of H matrix to be used in the simulation.

## Performance analysis of LDPC Convolutional Codes

- **Status**: ✅
- **Reason**: 새 LDPC-CC 구성 기법과 반복 디코딩 알고리즘 제시, FPGA/ASIC 저복잡도 구현 - 코드설계/디코더(C/E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6675426
- **Type**: conference
- **Published**: 14-16 Oct.
- **Authors**: Zahoor Ahmed Baloch, Ayaz Hussain, Noor Hussain
- **PDF**: https://ieeexplore.ieee.org/document/6675426
- **Abstract**: Low Density Parity Check Convolutional Codes (LDPC-CCs) have the advantage of simple encoding and decoding. ASIC or FPGA implementation of LDPC-CCs have been shown to have very good complexity-performance trade-off. In this paper, we present a class of LDPC-CC and iterative algorithm to decode these codes. The construction technique of our code is simple and easy, compared to other LDPC-CCs, which reduces hardware complexity. The simulation results show that the performance of our proposed codes is better than the LDPC Block codes with the same decoding complexity per information bit. Our code also outperforms its counterpart LDPC-CCs.

## High-speed LDPC encoder architecture for digital video broadcasting systems

- **Status**: ✅
- **Reason**: DVB-S2 LDPC 인코더 병렬 360비트 아키텍처 FPGA 10Gbps 구현, 이식 가능 HW 병렬화 기법(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:6675433
- **Type**: conference
- **Published**: 14-16 Oct.
- **Authors**: InKi Lee, MinHyuk Kim, DeockGil Oh +1
- **PDF**: https://ieeexplore.ieee.org/document/6675433
- **Abstract**: In this paper, we propose a high-speed LDPC encoder architecture for the DVB-S2 standard. The proposed LDPC encoding architecture is based on parallel 360 bit-wise operations. The key issues for realizing a high speed are two kinds of index addresses and making efficient use of memory. We implemented a half-rate LDPC encoder on an FPGA, and confirmed that its maximum throughput is up to 10 Gbps with a 100 MHz clock.

## Short-block LDPC codes design with semi-random parity-check matrix

- **Status**: ✅
- **Reason**: short-block 바이너리 LDPC 코드 설계(semi-random parity matrix + density evolution 최적 차수분포) — 유한길이 코드설계(E) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6967247
- **Type**: conference
- **Published**: 12-13 Oct.
- **Authors**: Qingshuang Zhang, Aijun Liu, Jingbo Mao
- **PDF**: https://ieeexplore.ieee.org/document/6967247
- **Abstract**: In this paper, we propose a design method for short block length low-density parity-check (LDPC) codes which use the structure of semi-random parity-check matrix and the optimal degree distribution pairs derived from density evolution algorithm. Simulation results show that the bit error performance of the designed code is better than Turbo codes with the same block length and code rate when Signal Noise Ratio (SNR) exceeds 2.5dB. At the same time, the complexity of decoder is lower than that of Turbo codes. This design method provides guiding significance for choosing an error-correcting code for reliable communication in narrow-band channel.

## Error detection and correction using LDPC in parallel Hopfield networks

- **Status**: ✅
- **Reason**: Hopfield network 기반 LDPC 디코딩 + FPGA 병렬 구현 — 신경망 디코더(C)/HW(D) 이식 가능성
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6674380
- **Type**: conference
- **Published**: 11-13 Oct.
- **Authors**: Constantin Anton, Laurenţiu Ionescu, Ion Tutănescu +2
- **PDF**: https://ieeexplore.ieee.org/document/6674380
- **Abstract**: Low Density Parity Check (LDPC) coding is a classical method for the detection and correction of errors. Its problem is the relatively complex operations which must be performed at encoding, and especially at decoding, to detect and correct errors caused by communication channels. We present a solution for the errors correction using regular LDPC and Hopfield network-based associative memories. Our solution solves this problem by using an associative memory based on the Hopfield network on the decoding stage, which stores the correct code words. This memory tends to transform the code words received with errors in errors free code words. We improved the ability of the associative memory by storing the code words in a specific format (pairs with their inverses, the constant number of “1” bits). These conditions are met by using LDPC coding. To be viable in communications, which require real-time correction, our proposed solution has used Hopfield networks operating in parallel, fully integrated into the Field Programmable Gates Array (FPGA) circuit.
