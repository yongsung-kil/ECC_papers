# IEEE Xplore — 2010-11 (1차선별 통과)


## A Unified Early Stopping Criterion for Binary and Nonbinary LDPC Codes Based on Check-Sum Variation Patterns

- **Status**: ✅
- **Reason**: 체크섬 변동 패턴 기반 BP early stopping 기준 — 바이너리 LDPC BP 디코더에 그대로 이식 가능한 조기종료 기법(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5599947
- **Type**: journal
- **Published**: November 2
- **Authors**: Guojun Han, Xingcheng Liu
- **PDF**: https://ieeexplore.ieee.org/document/5599947
- **Abstract**: In order to detect uncorrectable error frames and early terminate their iterative belief-propagation (BP) decoding for binary or nonbinary LDPC codes, a unified early stopping criterion using check-sum variation patterns is proposed. In addition to low computational overhead and easy choice of threshold parameters, it can be adapted to different channels. Simulation results show that the proposed criterion greatly reduces the average number of iterations (ANI) at low to medium signal-to-noise ratio (SNR) while keeping the error performance degradation negligible over a wide SNR region.

## Quasi-Cyclic LDPC Codes: An Algebraic Construction, Rank Analysis, and Codes on Latin Squares

- **Status**: ✅
- **Reason**: Latin square 기반 바이너리 QC-LDPC 대수적 구성·rank 분석 — 이식 가능 코드설계(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5590324
- **Type**: journal
- **Published**: November 2
- **Authors**: Li Zhang, Qin Huang, Shu Lin +2
- **PDF**: https://ieeexplore.ieee.org/document/5590324
- **Abstract**: Quasi-cyclic LDPC codes are the most promising class of structured LDPC codes due to their ease of implementation and excellent performance over noisy channels when decoded with message-passing algorithms as extensive simulation studies have shown. In this paper, an approach for constructing quasi-cyclic LDPC codes based on Latin squares over finite fields is presented. By analyzing the parity-check matrices of these codes, combinatorial expressions for their ranks and dimensions are derived. Experimental results show that, with iterative decoding algorithms, the constructed codes perform very well over the AWGN and the binary erasure channels.

## A Min-Sum Iterative Decoder Based on Pulsewidth Message Encoding

- **Status**: ✅
- **Reason**: PWM 메시지 인코딩 기반 offset min-sum LDPC 디코더 VLSI 구현 — NAND LDPC 디코더 HW 아키텍처에 직결(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5610712
- **Type**: journal
- **Published**: Nov. 2010
- **Authors**: Kevin Cushon, Camille Leroux, Saied Hemati +2
- **PDF**: https://ieeexplore.ieee.org/document/5610712
- **Abstract**: In this brief, we introduce a new iterative decoder implementation called pulsewidth-modulated min-sum (PWM-MS), in which messages are exchanged in a pulsewidth-encoded format. The advantages of this method are low switching activity, very low complexity check nodes, low routing congestion, and excellent energy efficiency. We implement a fully parallel PWM offset MS decoder for a (660, 484) regular (4, 15) low-density parity-check code with 4-bit quantization in 0.13-μm CMOS, with a core area of 5.76 mm2 (4.24-mm2 cell area or 556K equivalent and gates). In postlayout simulations, this decoder achieves an average information throughput of 5.71 Gb/s and an energy consumption of 65.8 pJ per information bit at a signal-to-noise ratio of 5.5 dB. Our results show a 21% reduction in area, a 0.6-dB improvement in coding gain, and an energy efficiency improvement of 19% over the comparable bit-serial MS decoder architecture. We also demonstrate 3-bit implementations, in which the coding gain is traded off for further improvements in throughput, area, and energy efficiency.

## Relaxation Dynamics in Stochastic Iterative Decoders

- **Status**: ✅
- **Reason**: 그래프 기반 stochastic 반복 디코딩의 hysteresis/successive relaxation 기법 — 바이너리 LDPC 디코더 HW에 이식 가능(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5547000
- **Type**: journal
- **Published**: Nov. 2010
- **Authors**: Saeed Sharifi Tehrani, Chris Winstead, Warren J. Gross +3
- **PDF**: https://ieeexplore.ieee.org/document/5547000
- **Abstract**: Stochastic decoding is a recently proposed approach for graph-based iterative error control decoding. We present and investigate three hysteresis methods for stochastic decoding on graphs with cycles and show their close relationship with the successive relaxation method. Implementation results demonstrate the tradeoff in bit error rate performance with circuit complexity.

## A 5.7Gbps row-based layered scheduling LDPC decoder for IEEE 802.15.3c applications

- **Status**: ✅
- **Reason**: row-based layered scheduling + normalized min-sum LDPC 디코더 칩, reconfigurable sorter/permutation routing 등 NAND 이식 가능 HW 아키텍처(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:5716617
- **Type**: conference
- **Published**: 8-10 Nov. 
- **Authors**: Shiang-Yu Hung, Shao-Wei Yen, Chih-Lung Chen +3
- **PDF**: https://ieeexplore.ieee.org/document/5716617
- **Abstract**: A LDPC decoder chip supporting four code rates of IEEE 802.15.3c applications is presented. The row-based layered scheduling with normalized min-sum algorithm is proposed to reduce the iteration number while maintaining similar performance. In addition, the reconfigurable 8/16/32-input sorter is designed to deal with four LDPC codes. In order to alleviate routing complexity, both of the reallocation of sorter inputs and pre-coding routing network are proposed to reduce the input numbers of multiplexers by 64%. Fabricated in 65-nm 1P10M CMOS process, this test chip can achieve maximum 5.79 Gbps throughput for the highest code rate code while the hardware efficiency and energy efficiency are 3.7 Gbps/mm2 and 62.4pJ/bit, respectively.

## A 5.35 mm2 10GBASE-T Ethernet LDPC decoder chip in 90 nm CMOS

- **Status**: ✅
- **Reason**: partially parallel LDPC 디코더, layered offset-min-sum + 글로벌 와이어 50% 감축 라우팅 기법, 면적/처리율 HW 기여 이식 가능(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:5716619
- **Type**: conference
- **Published**: 8-10 Nov. 
- **Authors**: Alessandro Cevrero, Yusuf Leblebici, Paolo Ienne +1
- **PDF**: https://ieeexplore.ieee.org/document/5716619
- **Abstract**: A partially parallel low density parity check (LDPC) decoder compliant with the IEEE 802.3an standard for 100BASE-T Ethernet is presented. The design is optimized for minimum silicon area and is based on the layered offset-min-sum algorithm which speeds up the convergence of the message passing decoding algorithm. To avoid routing congestion the decoder architecture employs a novel communication scheme that reduces the critical number of global wires by 50%. The prototype LDPC decoder ASIC, fabricated in 90 nm CMOS, occupies only 5.35 mm2 and achieves a decoding throughput of 11.69 Gb/s at 1.2 V with an energy efficiency of 133pJ/bit.

## A 15.8 pJ/bit/iter quasi-cyclic LDPC decoder for IEEE 802.11n in 90 nm CMOS

- **Status**: ✅
- **Reason**: layered offset-min-sum 기반 QC-LDPC 저전력 디코더 ASIC, 에너지효율 최적화 HW 기법 이식 가능(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5716618
- **Type**: conference
- **Published**: 8-10 Nov. 
- **Authors**: C. Roth, P. Meinerzhagen, C. Studer +1
- **PDF**: https://ieeexplore.ieee.org/document/5716618
- **Abstract**: We present a low-power quasi-cyclic (QC) low density parity check (LDPC) decoder that meets the throughput requirements of the highest-rate (600 Mbps) modes of the IEEE 802.11n WLAN standard. The design is based on the layered offset-min-sum algorithm and is runtime-programmable to process different code matrices (including all rates and block lengths specified by IEEE 802.11n). The register-transfer-level implementation has been optimized for best energy efficiency. The corresponding 90 nm CMOS ASIC has a core area of 1.77 mm2 and achieves a maximum throughput of 680 Mbps at 346 MHz clock frequency and 10 decoding iterations. The measured energy efficiency is 15.8pJ/bit/iteration at a nominal operating voltage of 1.0 V.

## Rate-compatible LDPC code decoder using check-node merging

- **Status**: ✅
- **Reason**: rate-compatible QC-LDPC 디코더, check-node merging+serial min-sum 아키텍처 - 이식 가능 디코더/HW 기법(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5757578
- **Type**: conference
- **Published**: 7-10 Nov. 
- **Authors**: Anton Blad, Oscar Gustafsson, Meng Zheng +1
- **PDF**: https://ieeexplore.ieee.org/document/5757578
- **Abstract**: The use of rate-compatible error correcting codes offers several advantages as compared to the use of fixed-rate codes: a smooth adaptation to the channel conditions, the possibility of incremental Hybrid ARQ schemes, as well as sharing of the encoder and decoder implementations between the codes of different rates. In this paper, the implementation of a decoder for rate-compatible quasi-cyclic LDPC codes is considered. Assuming the use of a code ensemble obtained through puncturing of a low-rate mother code, the decoder achieves significantly reduced convergence rates by merging the check node neighbours of the punctured variable nodes. The architecture uses the minsum algorithm with serial node processing elements to efficiently handle the wide spread of node degrees that results from the merging of the check nodes.

## A design of rate-adaptive LDPC codes for distributed source coding using PEG algorithm

- **Status**: ✅
- **Reason**: PEG 기반 rate-adaptive LDPC 구성으로 girth 향상·error floor 제거 코드설계 기법(E), 응용은 source coding이나 떼어낼 구성 기법 존재하여 애매-살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5680317
- **Type**: conference
- **Published**: 31 Oct.-3 
- **Authors**: Min Jang, Jin Whan Kang, Sang-Hyo Kim
- **PDF**: https://ieeexplore.ieee.org/document/5680317
- **Abstract**: We propose a method for constructing rate-adaptive low-density parity check (LDPC) codes with large girth by syndrome merging with progressive-edge-growth (PEG) algorithm. Proposed scheme has a different structure from LDPC accumulate (LDPCA) codes. As a result, the new construction method turns the girth up for each specific code, and eliminates error floor.

## Analysis of error-prone patterns for LDPC codes under belief propagation decoding

- **Status**: ✅
- **Reason**: error floor 유발 error-prone 패턴(trapping set) 분석 + 모든 trapping set 정보 없이 동작하는 개선 디코더 제시(C), 스토리지 응용 명시
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5680460
- **Type**: conference
- **Published**: 31 Oct.-3 
- **Authors**: Huanlin Li, Yanyan Cao, Jeffrey C. Dill
- **PDF**: https://ieeexplore.ieee.org/document/5680460
- **Abstract**: Lowering the error floor of LDPC codes is extremely attractive to some systems, such as deep space communication systems and storage systems, which desire very low error rates. The error floor phenomenon of LDPC codes, which is associated with their message passing decoding algorithms, is mainly caused by some unfavorable combinatorial characteristics (or error-prone patterns) of LDPC codes. In this paper, a mathematical analysis method which enables the identification of some significant features of error-prone patterns is presented with the help of the beliefs passed in their decoders. Based on the analysis, an improved decoder is proposed which can effectively deal with the traversable trapping sets and achieve significantly improved error floor performance compared with current decoders. More importantly, this proposed decoder does not require the information of all the possible trapping sets of an individual LDPC code when correcting the error bits in its trapping sets.

## Decoding of a quasi-cyclic LDPC code on a stream processor

- **Status**: ✅
- **Reason**: QC-LDPC TDMP layered BP의 고정소수점 양자화·스케줄 재정렬·소프트웨어 파이프라이닝으로 throughput 개선, 디코더 양자화·HW 기법 이식 가능(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5680462
- **Type**: conference
- **Published**: 31 Oct.-3 
- **Authors**: Jawone A. Kennedy, Daniel L. Noneaker
- **PDF**: https://ieeexplore.ieee.org/document/5680462
- **Abstract**: The TDMP layered belief-propagation algorithm is investigated for decoding a quasi-cyclic low-density parity-check code on a stream processor using fixed-point arithmetic. The effect of the processor's fixed-point resolution on the decoder performance is determined, and a simple technique is described for minimizing the performance penalty incurred when using the (highest throughput) lowest-resolution arithmetic mode of the processor. A reordering of the decoder schedule and a modification of the parity checks are also considered which permit increased software pipelining and improved latency hiding, with a corresponding increase in the data throughput. The fixed-point Storm-1 stream processor is used for comparative throughput results.

## Reduced-complexity decoding of low-density parity check codes based on adaptive convergence

- **Status**: ✅
- **Reason**: VN 수렴 판정 규칙으로 디코딩 복잡도 감소하는 새 디코더 기법 — BP 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5682908
- **Type**: conference
- **Published**: 22-23 Nov.
- **Authors**: Jia-Ning Su, Zhenghao Lu, Xiaopeng Yu +1
- **PDF**: https://ieeexplore.ieee.org/document/5682908
- **Abstract**: Low-density parity-check (LDPC) codes have recently been considered as a viable candidate for forward error correction in system level hardware-redundant, fault-tolerant logics. An important factor that influences the choosing of a specific FEC technique in a nano-scale system implementation is its real-time performance, namely its computational complexity. In this paper, we propose a set of rules to decide whether a variable node in a LDPC decoder should update its value in subsequent iterations of the decoding process, or be considered as converged. We show that by carefully choosing the convergence rules for variable nodes, significant reduction of decoding complexity can be achieved with endurable performance loss.

## Reduced-complexity decoding of high-rate LDPC codes over partial-response channels

- **Status**: ✅
- **Reason**: 고율 LDPC SPA 복잡도 감소(체크연산 부분집합·MacLaurin 근사·감쇠계수) 디코더 기법 C, 바이너리
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5685882
- **Type**: conference
- **Published**: 17-19 Nov.
- **Authors**: Zhiliang Qin, Kui Cai, Songhua Zhang
- **PDF**: https://ieeexplore.ieee.org/document/5685882
- **Abstract**: In this paper, we consider high-rate low-density parity-check (LDPC) codes for magnetic recording systems. We propose an efficient approach to reduce the computational complexity of the sum-product algorithm (SPA) for LDPC decoding by restricting the check operation to a small subset of input messages. Furthermore, the first-order MacLaurin Series is used to simplify the core operation and an attenuation factor is introduced to improve bit-error-rate (BER) performance by scaling down log-likelihood ratio (LLR) reliabilities in the decoding process. Simulation results show that the proposed decoder can obtain a noticeable performance gain over the conventional SPA at high signal-to-noise ratios (SNR) when used in turbo equalization schemes; while achieving a significantly lower computational complexity.

## Multiple parallel concatenation of low-density parity-check codes based on BIBD

- **Status**: ✅
- **Reason**: BIBD 기반 column-weight-2 QC-LDPC MPC 구성으로 error floor 개선, 코드설계 E
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5685888
- **Type**: conference
- **Published**: 17-19 Nov.
- **Authors**: Zhiliang Qin, Kui Cai, Songhua Zhang
- **PDF**: https://ieeexplore.ieee.org/document/5685888
- **Abstract**: In this paper, we propose a low-complexity multiple-parallel-concatenated (MPC) coding scheme for magnetic recording systems, where a high-rate quasi-cyclic (QC) low-density parity-check (LDPC) code with column weight 2 based on the Balanced Incomplete Block Design (BIBD) construction is used as the component code. Simulation results show that the proposed scheme improves the error floor performance considerably as compared with previous MPC schemes with single-parity-check (MPCSPC) codes and performs comparably to structured LDPC codes over idealized partial-response channels.

## Hybrid construction of quasi-cyclic low-density parity-check codes with large girth based on euclidean geometries

- **Status**: ✅
- **Reason**: 유클리드기하 기반 QC-LDPC 신규 구성(large girth)으로 코드설계 E 이식 가능, 바이너리
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5674261
- **Type**: conference
- **Published**: 17-19 Nov.
- **Authors**: Jun Li, Khan Md. Hashem Ali, Xueqin Jiang +1
- **PDF**: https://ieeexplore.ieee.org/document/5674261
- **Abstract**: This paper presents a hybrid approach to the construction of quasi-cyclic (QC) low-density parity-check (LDPC) codes based on parallel bundles in Euclidean geometries and circulant permutation matrices. Codes constructed by this method are shown to be regular with large girth and low density. Simulation results show that these codes perform very well with iterative decoding and achieve reasonably large coding gains over uncoded system.

## Extended optimum decoding for LDPC codes based on exhaustive tree search algorithm

- **Status**: ✅
- **Reason**: sparse 패리티검사 선형블록부호 ML/ISD 트리탐색 near-ML 디코더, LDPC 대상 C 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5685891
- **Type**: conference
- **Published**: 17-19 Nov.
- **Authors**: Li Yang, Martin Tomlinson, Marcel Ambroze +1
- **PDF**: https://ieeexplore.ieee.org/document/5685891
- **Abstract**: A maximum-likelihood decoding algorithm inspired by information set decoding is realised for LDPC codes or linear block codes with sparse parity-check matrices of moderate codeword lengths over the AWGN channel. The extension involves an exhaustive branch and bound tree-search based algorithm for finding all small Euclidean distance error vectors. It provides an approach of searching on the bounded n-bit positions, which involves 2k combinatorial dual codes based on the corresponding parity-check matrix, to achieve the near-optimum decoding output with attainable computational complexity. Soft decision decoding results are presented for some well-known LDPC codes demonstrating near-optimum maximum-likelihood performance.

## Protograph design for QC LDPC codes with large girth

- **Status**: ✅
- **Reason**: girth≥12 protograph 구성·다중에지 조합설계 신규 QC-LDPC 코드설계 E
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5674263
- **Type**: conference
- **Published**: 17-19 Nov.
- **Authors**: Hosung Park, Seokbeom Hong, Jong-Seon No +1
- **PDF**: https://ieeexplore.ieee.org/document/5674263
- **Abstract**: In this paper, all subgraph patterns of protographs which prevent quasi-cyclic (QC) low-density parity-check (LDPC) codes from having large girth are searched in allowance with multiple edges based on graph theoretic approach. A systematic construction of protograph with multiple edges using combinatorial design is proposed for QC LDPC codes with girth larger than or equal to 12.

## A tree-based ML decoding algorithm with adaptive thresholding

- **Status**: ✅
- **Reason**: OSD 대비 적응적 임계 트리탐색 ML 소프트디코딩, 선형블록부호 일반·LDPC 이식 가능 디코더 C
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5686162
- **Type**: conference
- **Published**: 17-19 Nov.
- **Authors**: Jing Cai, Martin Tomlinson, Cen Tjhai +1
- **PDF**: https://ieeexplore.ieee.org/document/5686162
- **Abstract**: In this work, we propose a maximum-likelihood (ML) soft-decision decoding algorithm of linear block codes based on an enhanced tree-based search algorithm. The algorithm considers each codeword as a tree branch and explores the subtree corresponding to the more reliable basis (MRB) of received vectors. By making use of the pre-defined ensemble branches and their costs, the branch evaluation process is effectively controlled by adaptive thresholding. This paper details the implementation of the proposed algorithm, compares the performance with the classic ordered statistic decoding (OSD) algorithm, and discusses the general decoding complexity and search effort in comparison to that of the OSD algorithm.

## Design and implementation of multi-mode QC-LDPC decoder

- **Status**: ✅
- **Reason**: 멀티모드 QC-LDPC FPGA 디코더, 메모리 구성/주소지정으로 자원 절약 — 이식 가능 HW(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:5688680
- **Type**: conference
- **Published**: 11-14 Nov.
- **Authors**: Yun Chen, Xiang Chen, Yifei Zhao +2
- **PDF**: https://ieeexplore.ieee.org/document/5688680
- **Abstract**: Low-density parity-check (LDPC) codes are one of the most effective error controlling methods, which now are widely used in multiple communication systems, for example, DVB-S2, 802.16e, etc. In these communication standards, the adopted LDPC codes are all quasi-cyclic low-density parity-check (QC-LDPC) codes. The parity-check matrices of QC-LDPC codes consist of arrays of circulants, in which each row is the cyclic shift of the row above it, and the first row is the cyclic shift of the last row. This character of QC-LDPC codes results in the linear encoding complexity and opens the door for the multi-mode LDPC decoders with enough flexibility of resource multiplexing. Based on the quasi-cyclic character of QC-LDPC codes, a design method for multi-mode QC-LDPC decoders is proposed in this paper. The node memory is skillfully organized and can be expediently addressed by a simple control unit to save memory consumption in hardware implementation. Then this design method is implemented and test on Field Programmable Gate Array (FPGA) platform. The test results show that the resource occupied by the multi-mode decoder is only a little more than that of maximal resource occupied by the single-mode decoder, and this multi-mode decoder can support at least 3 code rates with the throughput higher than 100 Mbps when the iteration number is fixed to 12 and the clock frequency is set to 200 MHZ.

## An FPGA design of low power LDPC decoder for high-speed wireless LAN

- **Status**: ✅
- **Reason**: LDPC 디코더 복잡도 저감 알고리즘(부분그룹 순차복호, early detection) + FPGA 구현 — 디코더(C)/HW(D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5688980
- **Type**: conference
- **Published**: 11-14 Nov.
- **Authors**: Min Hyuk Kim, Tae Doo Park, Chul Seong Kim +1
- **PDF**: https://ieeexplore.ieee.org/document/5688980
- **Abstract**: This paper proposes three kinds of simplified complexity-reduced algorithms for a low density parity check (LDPC) decoder. First, sequential decoding using a partial group is proposed. Second, an early detection method for reducing the computational complexity is proposed. Finally, in order to support the high-speed systems, we implemented LDPC decoder using three algorithms by N=648, R=1/2. And the decoder runs at a clock speed of 10ns. Therefore we implemented the LDPC decoder with the decoding speed of 110Mbps.
