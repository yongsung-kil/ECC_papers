# IEEE Xplore — 2017-02 (1차선별 통과)


## Design and efficient hardware implementation schemes for non-Quasi-Cyclic LDPC codes

- **Status**: ✅
- **Reason**: D: NQC-LDPC용 HW 구현(MOMP, 메모리충돌 회피 구성, cycle bus)으로 partly-parallel 디코더 활용효율 개선 → HW 아키텍처 이식 가능
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:7830899
- **Type**: journal
- **Published**: February 2
- **Authors**: Baihong Lin, Yukui Pei, Liuguo Yin +1
- **PDF**: https://ieeexplore.ieee.org/document/7830899
- **Abstract**: The design of a high-speed decoder using traditional partly parallel architecture for Non-Quasi-Cyclic (NQC) Low-Density Parity-Check (LDPC) codes is a challenging problem due to its high memory-block cost and low hardware utilization efficiency. In this paper, we present efficient hardware implementation schemes for NQCLDPC codes. First, we propose an implementation-oriented construction scheme for NQC-LDPC codes to avoid memory-access conflict in the partly parallel decoder. Then, we propose a Modified Overlapped Message-Passing (MOMP) algorithm for the hardware implementation of NQC-LDPC codes. This algorithm doubles the hardware utilization efficiency and supports a higher degree of parallelism than that used in the Overlapped Message Passing (OMP) technique proposed in previous works. We also present single-core and multi-core decoder architectures in the proposed MOMP algorithm to reduce memory cost and improve circuit efficiency. Moreover, we introduce a technique called the cycle bus to further reduce the number of block RAMs in multi-core decoders. Using numerical examples, we show that, for a rate-2/3, length-15360 NQC-LDPC code with 8.43-dB coding gain for Binary Phase- Shift Keying (BPSK) in an Additive White Gaussian Noise (AWGN) channel, the decoder with the proposed scheme achieves a 23.8%–52.6% reduction in logic utilization per Mbps and a 29.0%–90.0% reduction in message-memory bits per Mbps.

## A non-greedy puncturing method for rate-compatible LDPC codes

- **Status**: ✅
- **Reason**: 바이너리 rate-compatible LDPC용 신규 non-greedy puncturing(코드설계 E) 제안, NAND ECC 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7875246
- **Type**: journal
- **Published**: February 2
- **Authors**: Lin Zhou, Wei-Cheng Huang, Rui Zhao +1
- **PDF**: https://ieeexplore.ieee.org/document/7875246
- **Abstract**: In this paper, we propose a non-greedy punctur- ing method for constructing binary rate-compatible low-density parity-check codes. First, we show that the recovery error prob- ability for a punctured variable node can be reduced by allocat- ing a small number of unpunctured variable nodes in the recovery tree. Then, we redefine the recovery tree according to the princi- ple of iterative decoding with the sum-product algorithm. The pro- posed non-greedy puncturing algorithm lies mainly in the dynam- ical minimization of the number of unpunctured variable nodes in the redefined recovery tree for the punctured variable nodes. Fi- nally, simulation results show that the proposed puncturing algo- rithm outperforms the existing best puncturing algorithms in bit error rate performances of iterative decoding.

## Improved Penalty Functions of ADMM Penalized Decoder for LDPC Codes

- **Status**: ✅
- **Reason**: ADMM penalized LDPC 디코더 페널티함수 개선=이식가능 디코더 알고리즘(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7740920
- **Type**: journal
- **Published**: Feb. 2017
- **Authors**: Biao Wang, Jianjun Mu, Xiaopeng Jiao +1
- **PDF**: https://ieeexplore.ieee.org/document/7740920
- **Abstract**: By making the pseudocodewords more costly than codewords, the alternating direction method of multipliers (ADMM) penalized decoder can improve the error rate performances significantly for low-density parity-check (LDPC) codes at low signal-to-noise ratios. In this letter, we design two improved piecewise penalty functions for ADMM penalized decoder by increasing the slope of the penalty function at the points near x = 0 and x = 1. The improved penalty functions can punish pseudocodewords more quickly and thus increase the decoding speed. Simulation results over two LDPC codes show that the proposed method improves the error rate performances and reduces the decoding time considerably.

## Non-Uniform Window Decoding Schedules for Spatially Coupled LDPC Codes

- **Status**: ✅
- **Reason**: SC-LDPC 윈도우 디코딩 비균일 스케줄=이식가능 디코더 스케줄링 기법(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7762121
- **Type**: journal
- **Published**: Feb. 2017
- **Authors**: Najeeb Ul Hassan, Ali E. Pusane, Michael Lentmaier +2
- **PDF**: https://ieeexplore.ieee.org/document/7762121
- **Abstract**: Spatially coupled low-density parity-check codes can be decoded using a graph-based message passing algorithm applied across the total length of the coupled graph. However, considering practical constraints on decoding latency and complexity, a sliding window decoding approach is normally preferred. In order to reduce decoding complexity compared with standard parallel decoding schedules, serial schedules can be applied within a decoding window. However, uniform serial schedules within a window do not provide the expected reduction in complexity. Hence, we propose non-uniform schedules (parallel and serial) based on measured improvements in the estimated bit error rate (BER). We show that these non-uniform schedules result in a significant reduction in complexity without any loss in performance. Furthermore, based on observations made using density evolution, we propose a non-uniform pragmatic decoding schedule (parallel and serial) that does not require any additional calculations (e.g., BER estimates) within the decoding process.

## A 5.28-Gb/s LDPC Decoder With Time-Domain Signal Processing for IEEE 802.15.3c Applications

- **Status**: ✅
- **Reason**: 고처리율 LDPC 디코더 VLSI(시간영역 처리, layered, min finder)=이식가능 HW 아키텍처(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:7765065
- **Type**: journal
- **Published**: Feb. 2017
- **Authors**: Mao-Ruei Li, Chia-Hsiang Yang, Yeong-Luh Ueng
- **PDF**: https://ieeexplore.ieee.org/document/7765065
- **Abstract**: This paper presents a high-throughput, energy-efficient, and scalable low-density parity-check (LDPC) decoder with time-domain (TD) signal processing. The proposed arbiter-based minimum value finder is able to support practical long codes. The latency for determining the first two minimum values required in the check node unit is significantly reduced through TD processing. A layered Q-based decoding architecture together with the associated scheduling is proposed in order to reduce the amount of memory used for check node storage. Multimode operations are supported by leveraging the structure of the base matrices and the proposed scalable minimum finder architecture. As a proof of concept, a TD-based multimode LDPC decoder for high-speed IEEE 802.15.3c is designed and fabricated in a 90-nm CMOS process. The LDPC decoder integrates 495k logic gates in 2.25 mm2 and achieves a throughput of 5.28 Gb/s at 157 MHz from a 1.05 V supply voltage. The power and normalized energy dissipation are 182 mW and 34.47 pJ/b, respectively. The proposed LDPC decoder is more hardware and energy efficient than previous digital counterparts and is able to support long codes for practical applications, which is still infeasible for the state-of-the-art TD-based LDPC decoders.

## Optimization Techniques for the Efficient Implementation of High-Rate Layered QC-LDPC Decoders

- **Status**: ✅
- **Reason**: 고율 QC-LDPC layered 디코더 HW 최적화+수정 min-sum(카테고리 C/D), NAND 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7725494
- **Type**: journal
- **Published**: Feb. 2017
- **Authors**: Huang-Chang Lee, Mao-Ruei Li, Jyun-Kai Hu +2
- **PDF**: https://ieeexplore.ieee.org/document/7725494
- **Abstract**: For high-rate low-density parity-check (LDPC) codes, layered decoding processing can be reordered such that the first-in-first-out (FIFO) buffer that stores variable-to-check (V2C) messages is not needed and, hence, the memory area can be minimized, but at the cost of increased data dependency. This paper presents three techniques that can be used to implement an efficient reordered layered decoder. First, with the assistance of a graph coloring method, the required minimum number of V2C sign memory banks can be theoretically determined, with the corresponding pipeline architecture also designed. After that, the integer linear programming technique is adopted so as to arrange the V2C sign memory banks in a manner that minimizes the number of pipeline stalls, thereby increasing throughput. In order to further simplify the decoder, the first minimum values are not stored if the proposed modified min-sum algorithm is used. The proposed techniques are demonstrated by implementing a rate-0.905 (18396,16644) QC-LDPC decoder using 90-nm CMOS technology. When using the proposed techniques, implementation results show that the throughput-to-area ratio (TAR) increases by 58.9% without sacrificing error-rate performance.

## Spatially Coupled Codes Optimized for Magnetic Recording Applications

- **Status**: ✅
- **Reason**: 바이너리 SC-LDPC 유한길이 최적화·유해구조 제거(코드설계 E), MR 응용이나 NAND 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7569000
- **Type**: journal
- **Published**: Feb. 2017
- **Authors**: Homa Esfahanizadeh, Ahmed Hareedy, Lara Dolecek
- **PDF**: https://ieeexplore.ieee.org/document/7569000
- **Abstract**: Spatially coupled (SC) codes are a class of sparse graph-based codes known to have capacity-approaching performance. SC codes are constructed based on an underlying low-density parity-check (LDPC) code, by first partitioning the underlying block code and then putting replicas of the components together. Significant recent research efforts have been devoted to the asymptotic, ensemble-averaged study of SC codes, as these coupled variants of the existing LDPC codes offer excellent properties. While the asymptotic analysis is important, due to simplifying assumptions and averaging effects, results from the asymptotic domain are not readily translatable to the practical, finite-length setting. Despite this chasm, the finite-length analysis of SC codes is still largely unexplored. In this paper, we tackle the problem of optimized design of SC codes in the context of magnetic-recording (MR) applications. In particular, we identify combinatorial structures in the graphical representation of the code that are detrimental in the MR setting. An intriguing observation is that for the same SC code, the problematic objects for the MR channels are combinatorially different from the additive white Gaussian noise (AWGN) setting, thus necessitating a careful code design approach for the MR applications. We first demonstrate that the choice of the so-called cutting vector, which guides the code partitioning in the SC code design, directly affects the cardinality of these problematic objects. In particular, we show that the number of problematic objects is the highest—and consequently that the performance is the worst—in the case of the degenerate cutting vector, which precisely corresponds to uncoupled LDPC block codes. We, therefore, show that coupling always improves the performance and that the degree of improvement is dependent on the choice of the cutting vector. We then extend our analysis to different column weights and present SC codes that outperform block codes with unoptimized edge weights by more than 3.5 orders of magnitude and that also outperform both optimized block codes and unoptimized SC codes by more than two orders of magnitude. Through presented examples, we demonstrate high performance of the proposed code design methodology.

## Edge-Based Dynamic Scheduling for Belief-Propagation Decoding of LDPC and RS Codes

- **Status**: ✅
- **Reason**: edge-based 동적 BP 스케줄링(e-Flooding/e-Shuffled), 복잡도 절감 디코더 알고리즘=이식가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7779107
- **Type**: journal
- **Published**: Feb. 2017
- **Authors**: Chaudhry Adnan Aslam, Yong Liang Guan, Kui Cai
- **PDF**: https://ieeexplore.ieee.org/document/7779107
- **Abstract**: This paper presents two low-complexity edge-based scheduling schemes, referred to as the e-Flooding and e-Shuffled schedules, for the belief-propagation (BP) decoding of low-density parity-check and Reed-Solomon codes. The proposed schedules selectively update the edges of the code graph based on the run-time reliability of variable and check nodes. Specifically, new message update is propagated exclusively along the unreliable edges of the code graph. This reduces the decoding complexity of BP algorithm as only a partial set of message updates is computed per decoding iteration. Besides, restricting the flow of message updates may also precludes the occurrence of some short graph cycles, which helps to preserve the BP message independence at certain variable and check nodes. Using numerical simulations, it is shown that the proposed edge-based schedules reduce the BP decoding complexity by more than 90% compared with the prior-art BP schedules, while simultaneously improving the error-rate performance, at medium-to-high signal-to-noise ratio over additive white Gaussian noise channel.

## Antiwear Leveling Design for SSDs With Hybrid ECC Capability

- **Status**: ✅
- **Reason**: SSD 하이브리드 ECC 대상 anti-wear-leveling 설계 - 카테고리 A(NAND/SSD 직접)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7527690
- **Type**: journal
- **Published**: Feb. 2017
- **Authors**: Chien-Chung Ho, Yu-Ping Liu, Yuan-Hao Chang +1
- **PDF**: https://ieeexplore.ieee.org/document/7527690
- **Abstract**: With the joint considerations of reliability and performance, hybrid error correction code (ECC) becomes an option in the designs of solid-state drives (SSDs). Unfortunately, wear leveling (WL) might result in the early performance degradation to SSDs, which is common with a limited number of P/E cycles, due to the efforts to delay the bit-error-rate growth. In this paper, an anti-WL design is proposed to avoid such a performance problem so that the performance of SSDs with hybrid ECC capability can be improved without sacrificing their reliability. The capability of the proposed design was evaluated by a series of experiments, for which it was shown that the proposed design could greatly improve the read and write performance of SSDs up to 50% without affecting the endurance of the investigated SSDs, compared with traditional approaches.

## Performance of LDPC Decoders With Missing Connections

- **Status**: ✅
- **Reason**: missing connection HW 결함하 message-passing LDPC 디코더 성능, HW 신뢰성 디코더 분석(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7776825
- **Type**: journal
- **Published**: Feb. 2017
- **Authors**: Linjia Chang, Avhishek Chatterjee, Lav R. Varshney
- **PDF**: https://ieeexplore.ieee.org/document/7776825
- **Abstract**: Due to process variation in nanoscale manufacturing, there may be permanently missing connections in information processing hardware. Due to timing errors in circuits, there may be missed messages in intra-chip communications, equivalent to transiently missing connections. In this paper, we investigate the performance of message-passing LDPC decoders in the presence of missing connections. We prove concentration and convergence theorems that validate the use of density evolution performance analysis. Arbitrarily small error probability is not possible with missing connections, but we find suitably defined decoding thresholds for communication systems with binary erasure channels under peeling decoding, as well as binary symmetric channels under Gallager A and B decoding. We see that decoding is robust to missing wires, as decoding thresholds degrade smoothly. Moreover, there is a stochastic facilitation effect in Gallager B decoders with missing connections. We also conduct finite-length simulations, compare the decoding sensitivity to channel noise and to missing wiring, and perform preliminary error-tolerant manufacturing yield analysis.

## Design of Protograph-based LDPC Code Ensembles with Fast Convergence Properties

- **Status**: ✅
- **Reason**: protograph LDPC 앙상블 유한반복 수렴 최적화, MI 기반 새 임계값 분석 기법. 바이너리 코드설계 이식 가능(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7938045
- **Type**: conference
- **Published**: 6-9 Feb. 2
- **Authors**: Ian P. Mulholland, Enrico Paolini, Mark F. Flanagan
- **PDF**: https://ieeexplore.ieee.org/document/7938045
- **Abstract**: The design of protograph-based low-density parity-check (LDPC) code ensembles optimized for a finite number of decoder iterations is investigated. We show by example that protograph-based EXIT (PEXIT) analysis is not sufficiently reliable in the finite-iteration case, and develop a new technique which, similarly to PEXIT analysis, uses the mutual information (MI) as a tool in order to predict the performance of ensembles based on protographs. In contrast to PEXIT analysis, in which a critical value of the MI is used to define the decoding threshold, in our technique we examine the behavior of the MI over a range of channel parameters in order to define the threshold. Using this new definition of the iteration-constrained threshold, we perform a search over a large family of protographs in order to find the protograph with the highest iteration-constrained threshold for a finite number of iterations over the BEC.

## On the Relationship Between the KL Means Algorithm and the Information Bottleneck Method

- **Status**: ✅
- **Reason**: MI-최대화 양자기(IB/KL means)는 LDPC 디코더 LLR 양자화에 직접 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7938084
- **Type**: conference
- **Published**: 6-9 Feb. 2
- **Authors**: Brian M. Kurkoski
- **PDF**: https://ieeexplore.ieee.org/document/7938084
- **Abstract**: The problem of finding the mutual informationmaximizing quantizer of a discrete memoryless channel is important in the implementation of communication receivers, LDPC code decoders, and in the design of polar codes. Two algorithms algorithms that provide suboptimal solutions in polynomial time are the information bottleneck method and the KL means algorithm. The contribution of this paper is show that the information bottleneck method with beta ⃗ ∞ is algorithmically equivalent to the KL means algorithm. This is done by showing that both the DMC channel outputs, and the quantizer outputs, are in the same J-dimensional space, where J is the cardinality of the input alphabet.

## Random-permutation-matrix-based cyclically-coupled LDPC codes

- **Status**: ✅
- **Reason**: 신규 코드 설계 기여(random-permutation-matrix 기반 CC-LDPC) + FPGA BER 시뮬·디코더 복잡도 비교, 바이너리 QC-LDPC 계열 → E
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7890139
- **Type**: conference
- **Published**: 19-22 Feb.
- **Authors**: Francis C. M. Lau, Fanlu Mo, Wai M. Tarn +1
- **PDF**: https://ieeexplore.ieee.org/document/7890139
- **Abstract**: Cyclically-coupled quasi-cyclic low-density parity-check (CC-QC-LDPC) codes are a new class of QC-LDPC codes which can achieve excellent error performance and relatively low hardware requirement. In this paper, we modify the CC-QC-LDPC code construction by using random permutation matrices instead of circulant permutation matrices, forming the “random-permutation-matrix-based CC-LDPC (RP-CC-LDPC) code”. The objective is to achieve a better error performance under the same code length. We simulate the bit error rate using FPGA simulations. We also compare the BER results and decoder complexity of the above codes with those of regular and irregular QC-LDPC codes under the same code length and code rate.

## Reed-Solomon based globally coupled quasi-cyclic LDPC codes

- **Status**: ✅
- **Reason**: RS 패리티검사 기반 globally coupled QC-LDPC 신규 구성과 2-phase local/global 디코딩, 바이너리 코드설계 이식 가능(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8023442
- **Type**: conference
- **Published**: 12-17 Feb.
- **Authors**: Juane Li, Keke Liu, Shu Lin +1
- **PDF**: https://ieeexplore.ieee.org/document/8023442
- **Abstract**: This paper presents a special type of LDPC codes constructed based on the conventional parity-check matrices of Reed-Solomon (RS) codes. LDPC codes of this type are referred to as globally coupled RS-LDPC codes. These codes are designed for correcting random errors, random short phased bursts of erasures and long bursts of erasures. The Tanner graph of a globally coupled RS-LDPC is composed of a number of disjoint copies of the Tanner graph of a local RS-LDPC code which are connected together by a group of overall check-nodes (CNs), called global CNs. A globally coupled RS-LDPC code can be decoded with a two-phase local/global iterative scheme which allows correction of local random errors and phased bursts of erasures in the local phase and global random errors and a single long burst of erasures in the global phase.

## Multi-bit flipping algorithms with probabilistic gradient descent

- **Status**: ✅
- **Reason**: 바이너리 LDPC용 새로운 멀티비트 비트플립+확률적 경사하강(PGD-MBF) 디코더 — 저복잡도 디코더 알고리즘(C), NAND 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8023480
- **Type**: conference
- **Published**: 12-17 Feb.
- **Authors**: Bane Vasić, Predrag Ivaniš, Srdan Brkic
- **PDF**: https://ieeexplore.ieee.org/document/8023480
- **Abstract**: A new class of bit flipping algorithms for low-density parity-check codes over the binary symmetric channel is proposed. The algorithms employ multiple bits at a variable node to represent its reliability, and multiple bits a check node to capture the sequence of its syndrome values. The check node update function thus requires a simple bit-shift operation, while the variable node updates require a nonlinear Boolean function. This class of multi-bit flipping (MBF) algorithms is enhanced by the probabilistic gradient descent (PGD) algorithm. The gradient descent algorithm minimizes the variable node energy function which, in addition to the classical term which quantifies the discrepancy between the variable estimate and channel value, also involves an additive term defined as a weighted sum of neighboring check node states. Only the variable nodes with the maximal value of energy are eligible for updating, but the updates are not done by default but probabilistically. The resulting probabilistic gradient descent multi-bit flipping PGD-MBF algorithm combined with rewinding improves the codeword probability of error while keeping the complexity lower than that of the state-of-the-art algorithms of comparable throughput.
