# IEEE Xplore — 2013-11 (1차선별 통과)


## QC-LDPC Codes with Girth Eight Based on Independent Row-Column Mapping Sequence

- **Status**: ✅
- **Reason**: QC-LDPC girth-8 신규 구성법(독립 행-열 매핑 시퀀스), 바이너리 코드설계 기여 → 카테고리 E
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6626311
- **Type**: journal
- **Published**: November 2
- **Authors**: Lei Wang, Xing Zhang, Feng Yu +2
- **PDF**: https://ieeexplore.ieee.org/document/6626311
- **Abstract**: Quasi-cyclic low-density parity-check (QC-LDPC) codes are known to have algebraic structure, which suits hardware implementation. However, low girth makes their performances worse than random structured LDPC codes. Based on independent row-column mapping sequence, this work proposed a generalized method of constructing QC-LDPC codes with girth eight, which enlarges the class of girth eight QC-LDPC codes to a fairly general series. Simulation results show that the bit error rate of the constructed codes is close to that of progressive edge growth (PEG) based QC-LDPC codes under iterative decoding.

## Low Density Parity Check Codes with Non-Equiprobable Symbols

- **Status**: ✅
- **Reason**: 비등확률 이진심볼 LDPC 디코딩 위해 Tanner 그래프 메시지패싱(전/후방 비대칭) 수정 제안 — 바이너리 LDPC BP 디코더 변형으로 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6600715
- **Type**: journal
- **Published**: November 2
- **Authors**: Bowen Dai, Lei Wei
- **PDF**: https://ieeexplore.ieee.org/document/6600715
- **Abstract**: In this letter, we analyze how to decode LDPC codes with non-equiprobable binary symbols. For such symbols, we need to modify the conventional Tanner graph, because the message passing from check nodes to information bits and to parity check bits are diverse. In other words, in conventional Tanner graph, the message passing along two directions are identical, while in our case, the message along the forward direction and backward direction are different. A method to optimize signaling constellation which maximizes the channel mutual information is presented as well. In the numerical section, symbols with prior probabilities (0.3,0.7) could gain 0.72 dB in performance if we replace equal space constellation with optimal constellation. Several cases of short LDPC codes (N, K =1024, 512) are explored and gain almost 0.4 dB. The simulation shows that additional gain of only 0.2 dB could be attainable, if optimal source coding is achievable.

## Unequal Diversity LDPC Codes for Relay Channels

- **Status**: ✅
- **Reason**: 프로토그래프 기반 LDPC 신규 구성(unequal diversity, EXIT 분석). 바이너리 LDPC 코드설계 기법으로 이식 가능(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6620926
- **Type**: journal
- **Published**: November 2
- **Authors**: Paola Pulini, Gianluigi Liva, Marco Chiani
- **PDF**: https://ieeexplore.ieee.org/document/6620926
- **Abstract**: A novel protograph-based construction of low-density parity-check (LDPC) codes for the relay channel is proposed, which provides an enhanced unequal error protection property named unequal diversity. The focus is on quasi-static fading channels and on the high-code-rate (R>1/2) regimes, for which (according to the Singleton bound) no full diversity can be achieved. In the proposed construction, some nodes (and the corresponding codeword fragment) associated with the code graph enjoy the diversity provided by the relay, whereas the remaining nodes do not experience any diversity. The proposed approach can be thus tailored to transmit information blocks with different priority levels. An extrinsic information transfer (EXIT) analysis is developed, which allows an accurate performance prediction over the considered channel model, and more in general over block-fading channels.

## Robust Rate-Compatible Punctured LDPC Convolutional Codes

- **Status**: ✅
- **Reason**: RC punctured LDPC-CC 신규 펑처링 설계(trapping set/사이클 최소화), 바이너리 코드설계 E
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6648352
- **Type**: journal
- **Published**: November 2
- **Authors**: Hua Zhou, David G. M. Mitchell, Norbert Goertz +1
- **PDF**: https://ieeexplore.ieee.org/document/6648352
- **Abstract**: A family of robust rate-compatible (RC) punctured low-density parity-check convolutional codes (LDPC-CCs) is derived from a time-invariant LDPC-CC mother code by periodically puncturing encoded bits (variable nodes) with respect to several criteria: (1) ensuring the recoverability of punctured variable nodes, (2) minimizing the number of completely punctured cycle trapping sets (CPCTSs), and (3) minimizing the number of punctured variable nodes involved in short cycles. The influence of (1) and (3) on iterative decoding performance is felt most strongly in the waterfall region of the bit-error-rate (BER) curve, while (2) has a larger effect in the error floor, or high signal-to-noise ratio (SNR), region. We show that the length of the puncturing period is an important parameter when designing high rate punctured codes and, moreover, that extending the puncturing period can improve the decoding performance and extend the range of compatible rates. As examples, we obtain families of RC LDPC-CCs from several time-invariant LDPC-CC mother codes with monomial and binomial entries in their polynomial syndrome former matrices.

## Large Scale LP Decoding with Low Complexity

- **Status**: ✅
- **Reason**: 바이너리 LP 디코딩 ADMM, parity polytope 사영 선형복잡도 신규 알고리즘 → 이식가능 디코더 C
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6636134
- **Type**: journal
- **Published**: November 2
- **Authors**: Guoqiang Zhang, Richard Heusdens, W. Bastiaan Kleijn
- **PDF**: https://ieeexplore.ieee.org/document/6636134
- **Abstract**: Linear program (LP) decoding has become increasingly popular for error-correcting codes due to its simplicity and promising performance. Low-complexity and efficient iterative algorithms for LP decoding are of great importance for practical applications. In this paper we focus on solving the binary LP decoding problem by using the alternating direction method of multipliers (ADMM). Our main contribution is that we propose a linear-complexity algorithm for the projection onto a parity polytope (having a computational complexity of small O(d), where small d is the check-node degree), as compared to recent work , which has a computational complexity of small O(d log d). In particular, we show that the projection onto the parity polytope can be transformed to a projection onto a simplex.

## Bounds on the Size of Parity-Check Matrices for Quasi-Cyclic Low-Density Parity-Check Codes

- **Status**: ✅
- **Reason**: QC-LDPC girth/사이클 존재조건과 패리티검사행렬 크기 bound — 바이너리 코드설계(E) 신규 기여
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6587468
- **Type**: journal
- **Published**: Nov. 2013
- **Authors**: Kyung-Joong Kim, Jin-Ho Chung, Kyeongcheol Yang
- **PDF**: https://ieeexplore.ieee.org/document/6587468
- **Abstract**: In this paper, we investigate the cycle properties of quasi-cyclic low-density parity-check (QC-LDPC) codes. Using the sequence representation of a parity-check matrix for a QC-LDPC code, we analyze a necessary and sufficient condition for a cycle of a given length to exist. We then derive bounds which are necessary conditions for a QC-LDPC code to have a given girth in terms of its parameters. We also give a bound which is a sufficient condition for a QC-LDPC code of a given girth to be constructed by a greedy algorithm. The bounds derived here are applicable to any regular or irregular QC-LDPC codes as well as they improve the existing bounds in many classes of regular LDPC codes.

## Error-Prediction LDPC and Error-Recovery Schemes for Highly Reliable Solid-State Drives (SSDs)

- **Status**: ✅
- **Reason**: NAND/SSD LDPC ECC 직접 — EP-LDPC 에러예측, read cycle 7배 감소, retention(A)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6601731
- **Type**: journal
- **Published**: Nov. 2013
- **Authors**: Shuhei Tanakamaru, Yuki Yanagihara, Ken Takeuchi
- **PDF**: https://ieeexplore.ieee.org/document/6601731
- **Abstract**: Highly reliable solid-state drives (SSDs) with error-prediction low-density parity-check (EP-LDPC) and error-recovery schemes are proposed. Since the reliability of the nand flash memory of the SSD is seriously degraded as the scaling, the conventional error-correction scheme is becoming useless. Thus, LDPC error-correcting code (ECC) is considered to be the next-generation ECC for SSD. However, many read cycles are required and the LDPC scheme consumes an unacceptably long read time. To solve this problem, the proposed EP-LDPC scheme realizes the 7 × fewer sequential read cycles than the conventional LDPC scheme. Instead of reading repeatedly, the EP-LDPC scheme estimates errors from VTH, write/erase cycles, data-retention time, and inter-cell coupling information. The bit error rate (BER) estimation is based on the prerecorded table which stores the relations among write/erase cycles, data-retention time, neighboring cell data, and BER. As a result, the acceptable data-retention time of the SSD increases by more than 10 ×. Additionally, the proposed error-recovery scheme is executed and reduces the bit error if the BER of the data exceeds the error-correction capability of EP-LDPC scheme. Program-disturb error-recovery pulse and data-retention error-recovery pulse reduce the BER of the nand flash memory by 76% and 56%, respectively.

## Locally-connected Viterbi decoder architectures and their VLSI implementation for LDPC and convolutional codes

- **Status**: ✅
- **Reason**: 임의 LDPC를 trellis로 표현해 Viterbi ACS 기반 통합 디코더 VLSI 아키텍처 제시 — 이식 가능 HW/디코더(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6810329
- **Type**: conference
- **Published**: 3-6 Nov. 2
- **Authors**: Ahmed Refaey, Sébastien Roy, Isabelle Laroche +1
- **PDF**: https://ieeexplore.ieee.org/document/6810329
- **Abstract**: The applicability of the Viterbi add-compare-select (ACS) functional block to both convolutional and LDPC codes in various parallel implementations is investigated. To this end, a trellis representation for arbitrary LDPC codes must first be established. Then, a high-level architecture for a Viterbi-algorithm-based unified decoder is proposed. An in-depth exploration of the crucial path metrics (i.e ACS) functional block is then presented, where various locally-connected parallel structures at different speed-area points are explored. Some implementation results are provided, showing that the proposed structures offer high throughput, low latency, and a wide spectrum of speed-area trade-off point, depending on the specific topology that is chosen.

## Performance analysis of faulty Gallager-B decoding of QC-LDPC codes

- **Status**: ✅
- **Reason**: QC-LDPC Gallager-B 디코더의 faulty/unreliable 연산 하 성능 분석, 디코더 신뢰성 기법(C)으로 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6716235
- **Type**: conference
- **Published**: 26-28 Nov.
- **Authors**: Omran Al Rasheed, Srdjan S. Brkic, Predrag N. Ivanis +1
- **PDF**: https://ieeexplore.ieee.org/document/6716235
- **Abstract**: In this paper we evaluate the performance of Gallager-B algorithm, used for decoding low-density parity-check (LDPC) codes, under unreliable message computation. Our analysis is restricted to LDPC codes constructed from circular matrices (QC-LDPC codes). Using Monte Carlo simulation we investigate effects of different code parameters to coding system performance, under binary symmetric communication channel and independent transient faults model.

## LDPC code optimization based on Tanner graph mutations

- **Status**: ✅
- **Reason**: Tanner graph mutation 기반 유전알고리즘 LDPC 코드 구성/최적화, 신규 코드설계 기법(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6716251
- **Type**: conference
- **Published**: 26-28 Nov.
- **Authors**: Jan Broulím, Vjačeslav Georgiev, Jan Moldaschl +1
- **PDF**: https://ieeexplore.ieee.org/document/6716251
- **Abstract**: The paper presents LDPC error correcting code optimization based on Tanner graph mutations. A statistical experiment focused on a heuristic LDPC code construction was performed with the genetic algorithm. The algorithm used is briefly described. Short wordlength LDPC code optimization was simulated. Results of these simulations are summarized in this paper.

## Decoding algorithm of LDPC codes based on genetic algorithm

- **Status**: ✅
- **Reason**: 유전 알고리즘 기반 sum-product 디코딩(SPGD) 신규 디코더 알고리즘 제안; 부호 비의존 BP 개선 기법으로 바이너리 LDPC 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6827804
- **Type**: conference
- **Published**: 22-258 Nov
- **Authors**: Sheng Huang, Kai Tian, Fangfang Tian +1
- **PDF**: https://ieeexplore.ieee.org/document/6827804
- **Abstract**: In order to improve the decoding performance of low density parity check (LDPC) codes, a sum-product genetic decoding (SPGD) algorithm based on genetic algorithm (GA) is proposed. By means of the classical decoding algorithm of sum-product algorithm (SPA) of LDPC codes, variable node information generated by each hard decision of iteration is regarded as individuals that constitute initial population of GA. The decoded optimal solutions are produced by a series of genetic operations. Simulation results show that under the premise of almost no increase in complexity, the proposed SPGD algorithm has the superior decoding error correction performance, better practicability and higher net coding gain (NCG).

## Weighted candidate bit based bit-flipping decoding algorithms for LDPC codes

- **Status**: ✅
- **Reason**: 가중 후보비트 기반 bit-flipping 신규 디코더(min-sum과 연결), 바이너리 LDPC 이식 가능 C
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6703435
- **Type**: conference
- **Published**: 20-22 Nov.
- **Authors**: Qing Zhu, Le-nan Wu
- **PDF**: https://ieeexplore.ieee.org/document/6703435
- **Abstract**: In order to improve the bit-flipping (BF) decoding algorithms, a weighted hard-decision based BF decoding algorithm for low-density parity-check (LDPC) codes is presented, in which the weights of variable-nodes are employed. A new metric is defined for the weight of candidate bits not only in unsatisfied parity check equations but also in satisfied ones. The connection between min-sum decoding algorithm and the proposed algorithm is presented. Simulation results show that the new decoding algorithm can provide better FER performance and faster convergence speed than the original candidate bit based bit-flipping (CBBF) algorithm.

## Theoretic approach to BP-based WBF decoding algorithm of LDPC codes

- **Status**: ✅
- **Reason**: BP기반 WBF 통합 이론(IMWBF/MWBF/WBF/BF 일반화) 신규 디코더 기법, 이식 가능 C
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6707424
- **Type**: conference
- **Published**: 20-22 Nov.
- **Authors**: Erl-Huei Lu, Tso-Cho Chen, Pen-Yao Lu
- **PDF**: https://ieeexplore.ieee.org/document/6707424
- **Abstract**: A theoretic approach to the belief-propagation - based weighted bit-flipping (BP-based WBF) algorithm is proposed for decoding low-density parity-check codes. The decoding algorithm can be easily simplified to IMWBF, MWBF, WBF or BF decoding algorithms by setting different parameters; hence it could offer a high flexible performance/complexity trade-off for hybrid decoding.

## Implementing the NASA Deep Space LDPC Codes for Defense Applications

- **Status**: ✅
- **Reason**: NASA deep space LDPC 디코더 HW 구현: memory layout, parallelization, layered-decoding scheduling, FPGA 자원(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:6735722
- **Type**: conference
- **Published**: 18-20 Nov.
- **Authors**: Wiley H. Zhao, Jeffrey P. Long
- **PDF**: https://ieeexplore.ieee.org/document/6735722
- **Abstract**: Selected codes from, and extended from, the NASA's deep space low-density parity-check (LDPC) codes are implemented for high speed defense applications. This is part of an effort to build Government reference waveform implementations to assist defense acquisition programs and to promote waveform re-use. Details of the decoder implementation, including memory layout, parallelization architecture, layered-decoding scheduling, and field programmable gate array (FPGA) resource utilization are presented.

## Anti-jam Communications Using Frequency-Hopped OFDM and LDPC with Erasure Decoding ("Minotaur")

- **Status**: ✅
- **Reason**: Custom LDPC design for short block length (1248 info bits) + erasure decoding; 유한길이 코드설계(E) 기법 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6735603
- **Type**: conference
- **Published**: 18-20 Nov.
- **Authors**: Laurence Mailaender
- **PDF**: https://ieeexplore.ieee.org/document/6735603
- **Abstract**: We consider frequency-hopped OFDM (FH-OFDM) as the basis for anti-jam communications achieving very high processing gain. A conventional OFDM signal is hopped across a number of frequency sub-bands. Our design hops a 1 MHz bandwidth OFDM waveform to one of 400 frequencies (26 dB processing gain), occupying a large total bandwidth of 400 MHz. On each hop we assume an independent channel realization and jammer state. Employing 16-QAM and rate-1/2 coding, we achieve a data rate of 1.22 Mbps after accounting for all overheads, such as cyclic prefix, pilots, and peak-to-average control. We examine the impact of coding across hops in fading channels to achieve frequency diversity, and design custom LDPC codes for the resulting short block length (1248 information bits). We find that under jammed conditions erasure decoding improves BER by an order of magnitude, and develop a simple yet effective "in-band" approach to jammer state estimation. A non-real-time prototype was tested in the lab, sending the 400 MHz signal over a wired channel. Jamming levels high enough to completely preclude non-hopped communication degrade our system by only 2-5 dB, depending on channel conditions.

## A QC-LDPC construction algorithm for increasing the throughput of layered decoders

- **Status**: ✅
- **Reason**: E/D: 파이프라인 layered 디코더용 QC-LDPC 구성(EL-BPEG)으로 메모리충돌 제거·throughput 개선, 이식 가능 코드설계
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6820446
- **Type**: conference
- **Published**: 17-19 Nov.
- **Authors**: Jianjun Zhang, Mingke Dong, Ye Jin
- **PDF**: https://ieeexplore.ieee.org/document/6820446
- **Abstract**: Pipelined layered decoder (PLD) of quasi-cyclic low-density parity-check (QC-LDPC) codes is one of most popular high-throughput decoder in modern communication systems. However, the traditional QC-LDPC codes are not suitable for PLD and lead to memory access conflict problems (MACPs) that reduce the throughput of PLD. Therefore, an efficient layered block progressive edge-growth (EL-BPEG) algorithm is proposed to construct a class of QC-LDPC codes that can avoid MACPs and increase throughput. EL-BPEG appends check nodes, rather than variable nodes, progressively into Tanner Graph with strict concentrated check-node degrees. And it establishes edges according to the latency of the pipelines in PLD; thus, all idle clocks can be eliminated for the PLD with EL-BPEG codes. Result indicates that the throughput of PLD can be improved by 50.2% to 99.2% by using the EL-BPEG codes compared with the traditional QC-LDPC codes. Simulations show that the error performances of EL-BPEG codes are as well as the codes in standards.

## Implementation of IEEE 802.11n LDPC codes based on general purpose processors

- **Status**: ✅
- **Reason**: D: 802.11n LDPC GPP/SIMD layered decoding 구현, 병렬 디코더 기법 이식 가능
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:6820375
- **Type**: conference
- **Published**: 17-19 Nov.
- **Authors**: Xiao Han, Kai Niu, Zhiqiang He
- **PDF**: https://ieeexplore.ieee.org/document/6820375
- **Abstract**: Recently, General-purpose processor (GPP) soft defined radio (SDR) platforms have drawn great attention for their programmability and flexibility, and some high-speed wireless protocol stacks (e.g., IEEE 802.11a/b/g) have been implemented on them using commodity general-purpose PCs. Low-density parity-check (LDPC) codes are optionally used in IEEE 802.11n high throughput (HT) system as a high-performance error correcting code instead of convolutional codes for the near Shannon limit performance. In order to complete the implementation of IEEE 802.11n on SDR platforms, this paper presents the encoding and decoding of IEEE 802.11n LDPC codes on GPPs. We extensively use the features of contemporary processor architectures to accelerate data processing, including large low-latency caches to store lookup tables and SIMD processing on GPPs. Layered decoding is used in this paper, which can significantly reduce the number of iterations and is well suited to using SIMD instructions. The implementation results show that the throughput can meet the protocol timing requirement under the performance premise.

## Efficient Forced Convergence algorithm for low power LDPC decoders

- **Status**: ✅
- **Reason**: C: Forced Convergence 저전력 LDPC 디코더 복잡도 감소 알고리즘, min-sum 변형 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6864054
- **Type**: conference
- **Published**: 17-19 Nov.
- **Authors**: Byung Jun Choi, Myung Hoon Sunwoo
- **PDF**: https://ieeexplore.ieee.org/document/6864054
- **Abstract**: This paper proposes an efficient Forced Convergence (FC) algorithm to reduce the computational complexity of LDPC decoders. To reduce the computational complexity, the proposed algorithm uses only one threshold value and two conditions of variable nodes (VNs) while the existing FC algorithm uses two threshold values and two conditions. The simulation results show that the proposed algorithm achieves the bit error rate (BER) performance close to the typical Min-Sum algorithm. however, it can significantly reduce the computational complexity compared to the existing FC algorithm.

## A block-PEG construction method for LDPC codes

- **Status**: ✅
- **Reason**: QC-LDPC 새 구성법(block-PEG)으로 선형시간에 PEG급 성능, 바이너리 코드설계 기여(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6835504
- **Type**: conference
- **Published**: 15-17 Nov.
- **Authors**: Wei Han, Jianguo Huang
- **PDF**: https://ieeexplore.ieee.org/document/6835504
- **Abstract**: The construction of low-density parity codes(LDPC) is one of the hottest fields in the research of LDPC codes. In this paper, we propose a quasi-cyclic(QC) construction method of parity-check matrix of LDPC codes, named block-PEG method. In this method, a basic matrix is constructed firstly, then the none-zero elements in the matrix are extended by circulant permutation matrices, and the parity-check matrix is obtained at last. The simulation results indicate that the performances of LDPC codes constructed by block-PEG method are similar with that of PEG algorithm. In linear-time, block-PEG can generate LDPC codes with similar performance of the PEG-generated codes.

## Energy-efficient LDPC layered decoder

- **Status**: ✅
- **Reason**: QC-LDPC layered BP 디코더의 에너지효율 개선(lazy threshold로 CN 스킵), 이식 가능 디코더 알고리즘(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6835452
- **Type**: conference
- **Published**: 15-17 Nov.
- **Authors**: Jianjun Zhang, Da Wang, Ye Jin
- **PDF**: https://ieeexplore.ieee.org/document/6835452
- **Abstract**: It is very important to reduce the energy consumption of low-density parity-check (LDPC) decoders, especially for the intelligent and mobile terminals in green communications. This paper presents a novel energy-efficient layered decoder (EELD) to save the power consumption of quasi-cyclic LDPC (QC-LDPC) decoders based on the layered belief propagation (LBP) algorithm. The EELD forces a check-node process into asleep, when all the reliabilities of its neighboring variable nodes exceed the lazy threshold. The EELD also adopts the lower limit of the beliefs, rather than all the beliefs, of the neighboring variable nodes to compare with the lazy threshold in order to decide the state of check-node process. The EELD can skip the useless check-node processes to save energy consumption with slight additional complexity. Simulation results show that the EELD can improve the power efficiencies of the decoders by up to 28% for WiMAX codes without loss of error performances.

## A low-hardware consumption FPGA based configurable LDPC decoder

- **Status**: ✅
- **Reason**: 바이너리 LDPC용 FPGA 디코더, structured/random 모두 처리하는 저자원 configurable 아키텍처+범용 매핑 알고리즘 — 이식 가능 HW(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:6704550
- **Type**: conference
- **Published**: 12-15 Nov.
- **Authors**: Lijun Zhang, Ying Jiang
- **PDF**: https://ieeexplore.ieee.org/document/6704550
- **Abstract**: FPGAs are widely used for evaluating the performance of low-density parity check (LDPC) codes. But most of the existing LDPC decoders are designed for structured codes and extremely resource consuming. In this paper we propose a low-consumption configurable decoder architecture and a universal mapping algorithm for extrinsic messages to cope with structured or random regular LDPC codes. It can be implemented in low-priced products such as XILINX Spartan FPGAs family. In comparison with the decoders previously implemented, the proposed decoder significantly reduces the number of block RAMs used for extrinsic messages with no loss of throughput.

## 750Mb/s 17pJ/b 90nm CMOS (120,75) TS-LDPC Min-Sum based analog decoder

- **Status**: ✅
- **Reason**: Min-Sum 기반 TS-LDPC 아날로그 디코더 IC 구현 — 디코더 HW 아키텍처(D), 바이너리 LDPC min-sum
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:6691012
- **Type**: conference
- **Published**: 11-13 Nov.
- **Authors**: Alireza Rabbani Abolfazli, Yousef R. Shayan, Glenn E.R. Cowan
- **PDF**: https://ieeexplore.ieee.org/document/6691012
- **Abstract**: Circuit and IC implementation of a (120, 75) Min-Sum based Turbo-Structured LDPC analog decoder in CMOS 90nm technology is presented. This is the highest throughput and one of the longest codes implemented to date using analog techniques. At a Bit Error Rate of 10-5, the measured performance is within 0.2dB of modeled performance using floating-point arithmetic. The chip was tested at a throughput of 750Mb/s. This improves the throughput of analog decoders by a factor of 57. The power dissipation of the core is 13 mW resulting in 17pJ/b energy efficiency. The core area is 1.38mm2. The fabricated MS-based TS-LDPC analog decoder has BER performance nearly identical to theory without compromising energy efficiency.

## A 3.66Gb/s 275mW TB-LDPC-CC decoder chip for MIMO broadcasting communications

- **Status**: ✅
- **Reason**: TB-LDPC-CC 디코더 칩: layered scheduling 수정으로 수렴 2배·메모리 30% 절감, adaptive channel addressing — 이식 가능 HW 아키텍처(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:6691005
- **Type**: conference
- **Published**: 11-13 Nov.
- **Authors**: Chih-Lung Chen, Yu-Cheng Lan, Hsie-Chia Chang +1
- **PDF**: https://ieeexplore.ieee.org/document/6691005
- **Abstract**: In this work, a decoder chip for time-invariant tail-biting LDPC convolutional code (TB-LDPC-CC) is proposed. By modifying the layered decoding scheduling, the proposed decoding algorithm can achieve twice faster decoding convergence than the conventional flooding scheduling. Furthermore, 30.77% storage requirement is also reduced due to adaptive channel value addressing employed in memory-based decoder design. The multiple frame sizes handling ability can lower the power and adapt to multiple applications. By integrating these techniques, a TB-LDPC-CC decoder chip supporting three frame sizes is implemented in UMC 90nm CMOS technology. The decoder containing 4 processors occupies 2.18mm2 area and provides maximum throughput 3.66Gb/s under 0.8V supply and 305MHz with a 18.8pJ/bit/proc energy efficiency.
