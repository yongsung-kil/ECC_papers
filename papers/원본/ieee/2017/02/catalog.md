# IEEE Xplore — 2017-02


## Design and efficient hardware implementation schemes for non-Quasi-Cyclic LDPC codes

- **Status**: ✅
- **Reason**: D: NQC-LDPC용 HW 구현(MOMP, 메모리충돌 회피 구성, cycle bus)으로 partly-parallel 디코더 활용효율 개선 → HW 아키텍처 이식 가능
- **ID**: ieee:7830899
- **Type**: journal
- **Published**: February 2
- **Authors**: Baihong Lin, Yukui Pei, Liuguo Yin +1
- **PDF**: https://ieeexplore.ieee.org/document/7830899
- **Abstract**: The design of a high-speed decoder using traditional partly parallel architecture for Non-Quasi-Cyclic (NQC) Low-Density Parity-Check (LDPC) codes is a challenging problem due to its high memory-block cost and low hardware utilization efficiency. In this paper, we present efficient hardware implementation schemes for NQCLDPC codes. First, we propose an implementation-oriented construction scheme for NQC-LDPC codes to avoid memory-access conflict in the partly parallel decoder. Then, we propose a Modified Overlapped Message-Passing (MOMP) algorithm for the hardware implementation of NQC-LDPC codes. This algorithm doubles the hardware utilization efficiency and supports a higher degree of parallelism than that used in the Overlapped Message Passing (OMP) technique proposed in previous works. We also present single-core and multi-core decoder architectures in the proposed MOMP algorithm to reduce memory cost and improve circuit efficiency. Moreover, we introduce a technique called the cycle bus to further reduce the number of block RAMs in multi-core decoders. Using numerical examples, we show that, for a rate-2/3, length-15360 NQC-LDPC code with 8.43-dB coding gain for Binary Phase- Shift Keying (BPSK) in an Additive White Gaussian Noise (AWGN) channel, the decoder with the proposed scheme achieves a 23.8%–52.6% reduction in logic utilization per Mbps and a 29.0%–90.0% reduction in message-memory bits per Mbps.

## A non-greedy puncturing method for rate-compatible LDPC codes

- **Status**: ✅
- **Reason**: 바이너리 rate-compatible LDPC용 신규 non-greedy puncturing(코드설계 E) 제안, NAND ECC 이식 가능
- **ID**: ieee:7875246
- **Type**: journal
- **Published**: February 2
- **Authors**: Lin Zhou, Wei-Cheng Huang, Rui Zhao +1
- **PDF**: https://ieeexplore.ieee.org/document/7875246
- **Abstract**: In this paper, we propose a non-greedy punctur- ing method for constructing binary rate-compatible low-density parity-check codes. First, we show that the recovery error prob- ability for a punctured variable node can be reduced by allocat- ing a small number of unpunctured variable nodes in the recovery tree. Then, we redefine the recovery tree according to the princi- ple of iterative decoding with the sum-product algorithm. The pro- posed non-greedy puncturing algorithm lies mainly in the dynam- ical minimization of the number of unpunctured variable nodes in the redefined recovery tree for the punctured variable nodes. Fi- nally, simulation results show that the proposed puncturing algo- rithm outperforms the existing best puncturing algorithms in bit error rate performances of iterative decoding.

## Improved Penalty Functions of ADMM Penalized Decoder for LDPC Codes

- **Status**: ✅
- **Reason**: ADMM penalized LDPC 디코더 페널티함수 개선=이식가능 디코더 알고리즘(C)
- **ID**: ieee:7740920
- **Type**: journal
- **Published**: Feb. 2017
- **Authors**: Biao Wang, Jianjun Mu, Xiaopeng Jiao +1
- **PDF**: https://ieeexplore.ieee.org/document/7740920
- **Abstract**: By making the pseudocodewords more costly than codewords, the alternating direction method of multipliers (ADMM) penalized decoder can improve the error rate performances significantly for low-density parity-check (LDPC) codes at low signal-to-noise ratios. In this letter, we design two improved piecewise penalty functions for ADMM penalized decoder by increasing the slope of the penalty function at the points near x = 0 and x = 1. The improved penalty functions can punish pseudocodewords more quickly and thus increase the decoding speed. Simulation results over two LDPC codes show that the proposed method improves the error rate performances and reduces the decoding time considerably.

## Non-Uniform Window Decoding Schedules for Spatially Coupled LDPC Codes

- **Status**: ✅
- **Reason**: SC-LDPC 윈도우 디코딩 비균일 스케줄=이식가능 디코더 스케줄링 기법(C)
- **ID**: ieee:7762121
- **Type**: journal
- **Published**: Feb. 2017
- **Authors**: Najeeb Ul Hassan, Ali E. Pusane, Michael Lentmaier +2
- **PDF**: https://ieeexplore.ieee.org/document/7762121
- **Abstract**: Spatially coupled low-density parity-check codes can be decoded using a graph-based message passing algorithm applied across the total length of the coupled graph. However, considering practical constraints on decoding latency and complexity, a sliding window decoding approach is normally preferred. In order to reduce decoding complexity compared with standard parallel decoding schedules, serial schedules can be applied within a decoding window. However, uniform serial schedules within a window do not provide the expected reduction in complexity. Hence, we propose non-uniform schedules (parallel and serial) based on measured improvements in the estimated bit error rate (BER). We show that these non-uniform schedules result in a significant reduction in complexity without any loss in performance. Furthermore, based on observations made using density evolution, we propose a non-uniform pragmatic decoding schedule (parallel and serial) that does not require any additional calculations (e.g., BER estimates) within the decoding process.

## A 5.28-Gb/s LDPC Decoder With Time-Domain Signal Processing for IEEE 802.15.3c Applications

- **Status**: ✅
- **Reason**: 고처리율 LDPC 디코더 VLSI(시간영역 처리, layered, min finder)=이식가능 HW 아키텍처(D)
- **ID**: ieee:7765065
- **Type**: journal
- **Published**: Feb. 2017
- **Authors**: Mao-Ruei Li, Chia-Hsiang Yang, Yeong-Luh Ueng
- **PDF**: https://ieeexplore.ieee.org/document/7765065
- **Abstract**: This paper presents a high-throughput, energy-efficient, and scalable low-density parity-check (LDPC) decoder with time-domain (TD) signal processing. The proposed arbiter-based minimum value finder is able to support practical long codes. The latency for determining the first two minimum values required in the check node unit is significantly reduced through TD processing. A layered Q-based decoding architecture together with the associated scheduling is proposed in order to reduce the amount of memory used for check node storage. Multimode operations are supported by leveraging the structure of the base matrices and the proposed scalable minimum finder architecture. As a proof of concept, a TD-based multimode LDPC decoder for high-speed IEEE 802.15.3c is designed and fabricated in a 90-nm CMOS process. The LDPC decoder integrates 495k logic gates in 2.25 mm2 and achieves a throughput of 5.28 Gb/s at 157 MHz from a 1.05 V supply voltage. The power and normalized energy dissipation are 182 mW and 34.47 pJ/b, respectively. The proposed LDPC decoder is more hardware and energy efficient than previous digital counterparts and is able to support long codes for practical applications, which is still infeasible for the state-of-the-art TD-based LDPC decoders.

## Optimization Techniques for the Efficient Implementation of High-Rate Layered QC-LDPC Decoders

- **Status**: ✅
- **Reason**: 고율 QC-LDPC layered 디코더 HW 최적화+수정 min-sum(카테고리 C/D), NAND 이식 가능
- **ID**: ieee:7725494
- **Type**: journal
- **Published**: Feb. 2017
- **Authors**: Huang-Chang Lee, Mao-Ruei Li, Jyun-Kai Hu +2
- **PDF**: https://ieeexplore.ieee.org/document/7725494
- **Abstract**: For high-rate low-density parity-check (LDPC) codes, layered decoding processing can be reordered such that the first-in-first-out (FIFO) buffer that stores variable-to-check (V2C) messages is not needed and, hence, the memory area can be minimized, but at the cost of increased data dependency. This paper presents three techniques that can be used to implement an efficient reordered layered decoder. First, with the assistance of a graph coloring method, the required minimum number of V2C sign memory banks can be theoretically determined, with the corresponding pipeline architecture also designed. After that, the integer linear programming technique is adopted so as to arrange the V2C sign memory banks in a manner that minimizes the number of pipeline stalls, thereby increasing throughput. In order to further simplify the decoder, the first minimum values are not stored if the proposed modified min-sum algorithm is used. The proposed techniques are demonstrated by implementing a rate-0.905 (18396,16644) QC-LDPC decoder using 90-nm CMOS technology. When using the proposed techniques, implementation results show that the throughput-to-area ratio (TAR) increases by 58.9% without sacrificing error-rate performance.

## Spatially Coupled Codes Optimized for Magnetic Recording Applications

- **Status**: ✅
- **Reason**: 바이너리 SC-LDPC 유한길이 최적화·유해구조 제거(코드설계 E), MR 응용이나 NAND 이식 가능
- **ID**: ieee:7569000
- **Type**: journal
- **Published**: Feb. 2017
- **Authors**: Homa Esfahanizadeh, Ahmed Hareedy, Lara Dolecek
- **PDF**: https://ieeexplore.ieee.org/document/7569000
- **Abstract**: Spatially coupled (SC) codes are a class of sparse graph-based codes known to have capacity-approaching performance. SC codes are constructed based on an underlying low-density parity-check (LDPC) code, by first partitioning the underlying block code and then putting replicas of the components together. Significant recent research efforts have been devoted to the asymptotic, ensemble-averaged study of SC codes, as these coupled variants of the existing LDPC codes offer excellent properties. While the asymptotic analysis is important, due to simplifying assumptions and averaging effects, results from the asymptotic domain are not readily translatable to the practical, finite-length setting. Despite this chasm, the finite-length analysis of SC codes is still largely unexplored. In this paper, we tackle the problem of optimized design of SC codes in the context of magnetic-recording (MR) applications. In particular, we identify combinatorial structures in the graphical representation of the code that are detrimental in the MR setting. An intriguing observation is that for the same SC code, the problematic objects for the MR channels are combinatorially different from the additive white Gaussian noise (AWGN) setting, thus necessitating a careful code design approach for the MR applications. We first demonstrate that the choice of the so-called cutting vector, which guides the code partitioning in the SC code design, directly affects the cardinality of these problematic objects. In particular, we show that the number of problematic objects is the highest—and consequently that the performance is the worst—in the case of the degenerate cutting vector, which precisely corresponds to uncoupled LDPC block codes. We, therefore, show that coupling always improves the performance and that the degree of improvement is dependent on the choice of the cutting vector. We then extend our analysis to different column weights and present SC codes that outperform block codes with unoptimized edge weights by more than 3.5 orders of magnitude and that also outperform both optimized block codes and unoptimized SC codes by more than two orders of magnitude. Through presented examples, we demonstrate high performance of the proposed code design methodology.

## Edge-Based Dynamic Scheduling for Belief-Propagation Decoding of LDPC and RS Codes

- **Status**: ✅
- **Reason**: edge-based 동적 BP 스케줄링(e-Flooding/e-Shuffled), 복잡도 절감 디코더 알고리즘=이식가능(C)
- **ID**: ieee:7779107
- **Type**: journal
- **Published**: Feb. 2017
- **Authors**: Chaudhry Adnan Aslam, Yong Liang Guan, Kui Cai
- **PDF**: https://ieeexplore.ieee.org/document/7779107
- **Abstract**: This paper presents two low-complexity edge-based scheduling schemes, referred to as the e-Flooding and e-Shuffled schedules, for the belief-propagation (BP) decoding of low-density parity-check and Reed-Solomon codes. The proposed schedules selectively update the edges of the code graph based on the run-time reliability of variable and check nodes. Specifically, new message update is propagated exclusively along the unreliable edges of the code graph. This reduces the decoding complexity of BP algorithm as only a partial set of message updates is computed per decoding iteration. Besides, restricting the flow of message updates may also precludes the occurrence of some short graph cycles, which helps to preserve the BP message independence at certain variable and check nodes. Using numerical simulations, it is shown that the proposed edge-based schedules reduce the BP decoding complexity by more than 90% compared with the prior-art BP schedules, while simultaneously improving the error-rate performance, at medium-to-high signal-to-noise ratio over additive white Gaussian noise channel.

## LDPC Lattice Codes for Full-Duplex Relay Channels

- **Status**: ❌
- **Reason**: LDPC lattice 코드 릴레이 채널 응용, lattice shaping/decomposition으로 바이너리 LDPC ECC 이식 기법 없음
- **ID**: ieee:7782405
- **Type**: journal
- **Published**: Feb. 2017
- **Authors**: Hassan Khodaiemehr, Dariush Kiani, Mohammad-Reza Sadeghi
- **PDF**: https://ieeexplore.ieee.org/document/7782405
- **Abstract**: Low-density parity-check (LDPC) lattices were the first family of lattices to show efficient decoding in high dimensions. We consider a case of these lattices with one binary LDPC code as an underlying code. We employ encoding and decoding of the LDPC lattices in a cooperative transmission framework. We establish two efficient shaping based on hypercube and Voronoi shaping, to obtain LDPC lattice codes. Then, we propose the implementation of block Markov encoding for one-way and two-way relay networks using LDPC lattice codes. An efficient method is also required for decomposing full-rate codebook into lower rate codebooks. We apply different decomposition schemes for one-way and two-way relay channels, which are the altered versions of the decomposition methods of low density lattice code (LDLC) lattices. Due to the lower complexity of the decoding for LDPC lattices comparing with LDLCs, the complexity of our schemes is significantly lower than the ones proposed for LDLCs. The efficiency of the proposed schemes is presented using simulation results that indicate the outperforming behavior of LDLCs over LDPC lattice codes in the same dimensions. However, having lower decoding complexity enables us to increase the dimension of the lattice to compensate the existing gap between the performance of the LDPC lattice codes and the LDLCs.

## Practical Encoder and Decoder for Power Constrained QC LDPC-Lattice Codes

- **Status**: ❌
- **Reason**: QC LDPC-lattice 부호+nested lattice shaping, lattice/SP 알고리즘으로 바이너리 LDPC ECC 이식 기법 없음(LDA는 non-binary)
- **ID**: ieee:7762096
- **Type**: journal
- **Published**: Feb. 2017
- **Authors**: Hassan Khodaiemehr, Mohammad-Reza Sadeghi, Amin Sakzad
- **PDF**: https://ieeexplore.ieee.org/document/7762096
- **Abstract**: Low density parity check (LDPC) lattices were the first family of lattices equipped with iterative decoding algorithms. We introduce quasi-cyclic LDPC (QC LDPC) lattices as a special case of LDPC lattices with one binary QC-LDPC code as their underlying code. These lattices are obtained from the Construction A of lattices providing us to encode them efficiently using shift registers. To benefit from an encoder with linear complexity in the lattice dimension, we obtain the generator matrix of these lattices in quasi-cyclic form. We generalize the proposed quasi-cyclic form of the generator matrix for other Construction A lattices, namely the LDA lattices, with a non-binary QC-LDPC code as their underlying code. We provide a low-complexity decoding algorithm of QC LDPC-lattices based on the sum product algorithm. To design lattice codes, QC LDPC-lattices are combined with the nested lattice shaping that uses the Voronoi region of a sublattice for shaping. The shaping gain and the shaping loss of our lattice codes with dimensions 40, 50, and 60 using an optimal quantizer, are presented. The guidelines for applying efficient shaping methods, like hypercube shaping, for QC LDPC-lattices are also given. Consequently, we establish a family of lattice codes that perform practically close to the sphere bound.

## Improved Hard-Reliability Based Majority-Logic Decoding for Non-Binary LDPC Codes

- **Status**: ❌
- **Reason**: non-binary LDPC majority-logic 디코딩 - 비이진 제외
- **ID**: ieee:7728036
- **Type**: journal
- **Published**: Feb. 2017
- **Authors**: Saedong Yeo, In-Cheol Park
- **PDF**: https://ieeexplore.ieee.org/document/7728036
- **Abstract**: This letter proposes two methods to improve the iterative hard-reliability based majority-logic decoding algorithm for non-binary low-density parity-check (NB-LDPC) codes. The first method improves the error-correcting performance by modifying the initialization process, which is based on the fact that Gray coded modulation is used in general. In addition, a storage reduction method is proposed to make the proposed decoding hardware-friendly, which reduces the memory size considerably while sustaining the error-correcting performance achieved by the modified initialization. For an NB-LDPC code over Galois field of 32 elements, the memory size is reduced by about 75% compared with that of the conventional decoding algorithm.

## CRC Error Correction in IoT Applications

- **Status**: ❌
- **Reason**: CRC 부호 반복디코딩 IoT 적용 - 비-LDPC 부호, 떼어낼 LDPC BP 기법 없음
- **ID**: ieee:7558141
- **Type**: journal
- **Published**: Feb. 2017
- **Authors**: Evgeny Tsimbalo, Xenofon Fafoutis, Robert J. Piechocki
- **PDF**: https://ieeexplore.ieee.org/document/7558141
- **Abstract**: In this paper, error correction is introduced to the Bluetooth low energy and IEEE 802.15.4 standards by utilizing data redundancy provided by cyclic redundancy check (CRC) codes used by both protocols to detect erroneous packets. A scenario with an energy-constrained transmitter and a constraint-free infrastructure is assumed that enables additional signal processing at the receiving side, keeping the transmitter intact. CRC error correction is achieved using a novel approach of applying iterative decoding techniques. The proposed methods are evaluated based both on simulated and real packets. It is shown that by enabling CRC error correction, up to 2.5 dB of the signal to noise ratio gain can be achieved, while up to 35% of real corrupted packets can be corrected, at no extra cost for the transmitter. This results in potential range extension and longer battery life caused by a reduced number of retransmissions.

## Antiwear Leveling Design for SSDs With Hybrid ECC Capability

- **Status**: ✅
- **Reason**: SSD 하이브리드 ECC 대상 anti-wear-leveling 설계 - 카테고리 A(NAND/SSD 직접)
- **ID**: ieee:7527690
- **Type**: journal
- **Published**: Feb. 2017
- **Authors**: Chien-Chung Ho, Yu-Ping Liu, Yuan-Hao Chang +1
- **PDF**: https://ieeexplore.ieee.org/document/7527690
- **Abstract**: With the joint considerations of reliability and performance, hybrid error correction code (ECC) becomes an option in the designs of solid-state drives (SSDs). Unfortunately, wear leveling (WL) might result in the early performance degradation to SSDs, which is common with a limited number of P/E cycles, due to the efforts to delay the bit-error-rate growth. In this paper, an anti-WL design is proposed to avoid such a performance problem so that the performance of SSDs with hybrid ECC capability can be improved without sacrificing their reliability. The capability of the proposed design was evaluated by a series of experiments, for which it was shown that the proposed design could greatly improve the read and write performance of SSDs up to 50% without affecting the endurance of the investigated SSDs, compared with traditional approaches.

## A Novel Architecture for Elementary-Check-Node Processing in Nonbinary LDPC Decoders

- **Status**: ❌
- **Reason**: non-binary LDPC(GF(q)) elementary-check-node 아키텍처 - 비이진 제외
- **ID**: ieee:7448890
- **Type**: journal
- **Published**: Feb. 2017
- **Authors**: Oussama Abassi, Laura Conde-Canencia, Ali Al Ghouwayel +1
- **PDF**: https://ieeexplore.ieee.org/document/7448890
- **Abstract**: This brief presents an efficient architecture design for elementary-check-node processing in nonbinary low-density parity-check decoders based on the extended min-sum algorithm. This architecture relies on a simplified version of the bubble check algorithm and is implemented by the means of first-in-first-out. The adoption of this new design at the check node level results in a high-rate low-cost full-pipelined processor. A proof-of-concept implementation of this processor shows that the proposed architecture halves the occupied the field-programmable gate array (FPGA) surface and doubles the maximum frequency without modifying the input/output behavior of the previous one.

## Performance of LDPC Decoders With Missing Connections

- **Status**: ✅
- **Reason**: missing connection HW 결함하 message-passing LDPC 디코더 성능, HW 신뢰성 디코더 분석(C/D)
- **ID**: ieee:7776825
- **Type**: journal
- **Published**: Feb. 2017
- **Authors**: Linjia Chang, Avhishek Chatterjee, Lav R. Varshney
- **PDF**: https://ieeexplore.ieee.org/document/7776825
- **Abstract**: Due to process variation in nanoscale manufacturing, there may be permanently missing connections in information processing hardware. Due to timing errors in circuits, there may be missed messages in intra-chip communications, equivalent to transiently missing connections. In this paper, we investigate the performance of message-passing LDPC decoders in the presence of missing connections. We prove concentration and convergence theorems that validate the use of density evolution performance analysis. Arbitrarily small error probability is not possible with missing connections, but we find suitably defined decoding thresholds for communication systems with binary erasure channels under peeling decoding, as well as binary symmetric channels under Gallager A and B decoding. We see that decoding is robust to missing wires, as decoding thresholds degrade smoothly. Moreover, there is a stochastic facilitation effect in Gallager B decoders with missing connections. We also conduct finite-length simulations, compare the decoding sensitivity to channel noise and to missing wiring, and perform preliminary error-tolerant manufacturing yield analysis.

## On Frame Asynchronous Coded Slotted ALOHA: Asymptotic, Finite Length, and Delay Analysis

- **Status**: ❌
- **Reason**: coded slotted ALOHA 랜덤액세스 분석, LDPC는 분석도구일 뿐 떼어낼 ECC 디코더/구성 없음
- **ID**: ieee:7762138
- **Type**: journal
- **Published**: Feb. 2017
- **Authors**: Erik Sandgren, Alexandre Graell i Amat, Fredrik Brännström
- **PDF**: https://ieeexplore.ieee.org/document/7762138
- **Abstract**: We consider a frame asynchronous coded slotted ALOHA (FA-CSA) system for uncoordinated multiple access, where users join the system on a slot-by-slot basis according to a Poisson random process, and in contrast to standard frame synchronous CSA (FS-CSA), users are not frame-synchronized. We analyze the performance of FA-CSA in terms of packet loss rate and delay. In particular, we derive the (approximate) density evolution that characterizes the asymptotic performance of FA-CSA when the frame length goes to infinity. We show that, if the receiver can monitor the system before anyone starts transmitting, a boundary effect similar to that of spatially coupled codes occurs, which greatly improves the iterative decoding threshold. Furthermore, we derive tight approximations of the error floor (EF) for the finite frame length regime, based on the probability of occurrence of the most frequent stopping sets. We show that, in general, FA-CSA provides better performance in both the EF and waterfall regions as compared to FS-CSA. Moreover, FA-CSA exhibits better delay properties than FS-CSA.

## Broadcast Coded Slotted ALOHA: A Finite Frame Length Analysis

- **Status**: ❌
- **Reason**: coded slotted ALOHA MAC/erasure 분석 - 무선 응용 특이, 떼어낼 ECC 기법 없음
- **ID**: ieee:7736044
- **Type**: journal
- **Published**: Feb. 2017
- **Authors**: Mikhail Ivanov, Fredrik Brännström, Alexandre Graell i Amat +1
- **PDF**: https://ieeexplore.ieee.org/document/7736044
- **Abstract**: We propose an uncoordinated medium access control (MAC) protocol, called all-to-all broadcast coded slotted ALOHA (B-CSA) for reliable all-to-all broadcast with strict latency constraints. In B-CSA, each user acts as both transmitter and receiver in a half-duplex mode. The half-duplex mode gives rise to a double unequal error protection (DUEP) phenomenon: the more a user repeats its packet, the higher the probability that this packet is decoded by other users, but the lower the probability for this user to decode packets from others. We analyze the performance of B-CSA over the packet erasure channel for a finite frame length. In particular, we provide a general analysis of stopping sets for B-CSA and derive an analytical approximation of the performance in the error floor (EF) region, which captures the DUEP feature of B-CSA. Simulation results reveal that the proposed approximation predicts very well the performance of B-CSA in the EF region. Finally, we consider the application of B-CSA to vehicular communications and compare its performance with that of carrier sense multiple access (CSMA), the current MAC protocol in vehicular networks. The results show that B-CSA is able to support a much larger number of users than CSMA with the same reliability.

## Achieving Secrecy Capacity of the Wiretap Channel and Broadcast Channel With a Confidential Component

- **Status**: ❌
- **Reason**: polar code 기반 wiretap 보안 용량 달성, 보안+비-LDPC 부호, 떼어낼 LDPC BP 기법 없음
- **ID**: ieee:7750596
- **Type**: journal
- **Published**: Feb. 2017
- **Authors**: Talha Cihad Gulcu, Alexander Barg
- **PDF**: https://ieeexplore.ieee.org/document/7750596
- **Abstract**: The wiretap channel model of Wyner is one of the first communication models with both reliability and security constraints. Capacity-achieving schemes for various models of the wiretap channel have received considerable attention in recent literature. In this paper, we show that capacity of the general (not necessarily degraded or symmetric) wiretap channel under a “strong secrecy constraint” can be achieved using a transmission scheme based on polar codes. We also extend our construction to the case of broadcast channels with confidential messages defined by Csiszár and Körner, achieving the entire capacity region of this communication model.

## Multiuser Detection in Multibeam Satellite Systems: Theoretical Analysis and Practical Schemes

- **Status**: ❌
- **Reason**: 다중빔 위성 multiuser detection+DVB-S2 코드 재설계, 통신 응용 특이적이고 떼어낼 LDPC 기법 없음
- **ID**: ieee:7782367
- **Type**: journal
- **Published**: Feb. 2017
- **Authors**: Giulio Colavolpe, Andrea Modenini, Amina Piemontese +1
- **PDF**: https://ieeexplore.ieee.org/document/7782367
- **Abstract**: We consider the rates achievable by a user in a multibeam satellite system for unicast applications and propose alternatives to the conventional single-user symbol-by-symbol detection applied at user terminals. Single-user detection is known to suffer from strong degradation when the terminal is located near the edge of the coverage area of a beam and when aggressive frequency reuse is adopted. For this reason, we consider multiuser detection and take into account the strongest interfering signal. We also analyze two additional transmission strategies requiring modifications at medium access control layer. We describe an information-theoretic framework to compare the different strategies by computing the information rate of the user in the reference beam. Furthermore, we analyze the performance of coded schemes that could approach the information-theoretic limits. We show that classical codes from the DVB-S2(X) standard are not suitable when multiuser detection is adopted and we propose two ways to improve the performance based on the redesign of the code and of the bit mapping.

## Product Codes for Data Storage on Magnetic Tape

- **Status**: ❌
- **Reason**: 테이프 스토리지용 product code(비-LDPC), 떼어낼 LDPC BP 기법 없음
- **ID**: ieee:7577779
- **Type**: journal
- **Published**: Feb. 2017
- **Authors**: Roy D. Cideciyan, Simeon Furrer, Mark A. Lantz
- **PDF**: https://ieeexplore.ieee.org/document/7577779
- **Abstract**: For 2-D product codes used in tape storage, the mapping of error-correction-coding (ECC) blocks (EBs) into 2-D physical blocks (PBs) on magnetic tape is generalized. The 3-D product codes that have the same code rate and EB size as interleaved 2-D product codes currently used in tape storage are proposed. For 3-D product codes, a new family of mappings of EBs into 2-D PBs on magnetic tape is introduced, which fulfills the stringent burst-error-correction requirements of tape storage. The burst-error-correction capability of 2-D and 3-D product code words recorded on magnetic tape is analyzed as a function of track rotation, linear density, and ECC parameters. The performance limits of the tape-storage channel are determined based on computations of channel capacity and random coding bound. Hardware simulations of iterative hard-decision decoding of product codes implemented in a field-programmable gate array demonstrate the improved error-rate performance of 3-D product codes over 2-D product codes.

## Multi-Party Secret Key Agreement Over State-Dependent Wireless Broadcast Channels

- **Status**: ❌
- **Reason**: 무선 브로드캐스트 채널 비밀키 합의(보안), 떼어낼 LDPC ECC 기법 없음
- **ID**: ieee:7574374
- **Type**: journal
- **Published**: Feb. 2017
- **Authors**: Mahdi Jafari Siavoshani, Shaunak Mishra, Christina Fragouli +1
- **PDF**: https://ieeexplore.ieee.org/document/7574374
- **Abstract**: We consider a group of m trusted and authenticated nodes that aim to create a shared secret key K over a wireless channel in the presence of an eavesdropper Eve. We assume that there exists a state-dependent wireless broadcast channel from one of the honest nodes to the rest of them including Eve. All of the trusted nodes can also discuss over a cost-free, noiseless and unlimited rate public channel which is also overheard by Eve. For this setup, we develop an information-theoretically secure secret key agreement protocol. We show the optimality of this protocol for “linear deterministic” wireless broadcast channels. This model generalizes the packet erasure model studied in the literature for wireless broadcast channels. Here, the main idea is to convert a deterministic channel into multiple independent erasure channels by using superposition coding. For “state-dependent Gaussian” wireless broadcast channels, by using insights from the deterministic problem, we propose an achievability scheme based on a multi-layer wiretap code. By using the wiretap code, we can mimic the phenomenon of converting the wireless channel into multiple independent erasure channels. Then, finding the best achievable secret key generation rate leads to solving a non-convex power allocation problem over these channels (layers). We show that using a dynamic programming algorithm, one can obtain the best power allocation for this problem. Moreover, we prove the optimality of the proposed achievability scheme for the regime of high-SNR and large-dynamic range over the channel states in the (generalized) degrees of freedom sense.

## Coded Pulse-Amplitude-Modulation for Intensity- Modulated Optical Communications

- **Status**: ❌
- **Reason**: q-ary(비이진) Polar 부호 광통신 코드변조. 비이진+비-LDPC, 제외
- **ID**: ieee:7938058
- **Type**: conference
- **Published**: 6-9 Feb. 2
- **Authors**: Zifeng Wu, Berthold Lankl
- **PDF**: https://ieeexplore.ieee.org/document/7938058
- **Abstract**: In this paper, we study the optimization of M-ary pulse-amplitude modulation (PAM) in the context of a coded modulation scheme for intensity-modulated optical communications. Building on previous approaches in literature, we propose to employ q-ary codes, in particular q-ary Polar codes, to achieve simplified mapping and a high degree of flexibility at low to moderate complexity. We focus on information-theoretic aspects and verify the performance of our coded modulation scheme using numerical simulations.

## A New Error Correction Scheme for Physical Unclonable Functions

- **Status**: ❌
- **Reason**: PUF 보안용 ECC, LDPC 사용하나 보안+helper data 없는 개별코드 구성. 보안 도메인, 떼어낼 일반 LDPC 기법 없음
- **ID**: ieee:7938055
- **Type**: conference
- **Published**: 6-9 Feb. 2
- **Authors**: Sven Mueelich, Martin Bossert
- **PDF**: https://ieeexplore.ieee.org/document/7938055
- **Abstract**: Error correction is an indispensable component when Physical Unclonable Functions (PUFs) are used in cryptographic applications. So far, there exist schemes that obtain helper data, which they need within the error correction process. We introduce a new scheme, which only uses an error correcting code without any further helper data. The main idea is to construct for each PUF instance an individual code which contains the initial PUF response as codeword. In this work we use LDPC codes, however other code classes are also possible. Our scheme allows a trade-off between code rate and cryptographic security. In addition, decoding with linear complexity is possible.

## Design of Protograph-based LDPC Code Ensembles with Fast Convergence Properties

- **Status**: ✅
- **Reason**: protograph LDPC 앙상블 유한반복 수렴 최적화, MI 기반 새 임계값 분석 기법. 바이너리 코드설계 이식 가능(E)
- **ID**: ieee:7938045
- **Type**: conference
- **Published**: 6-9 Feb. 2
- **Authors**: Ian P. Mulholland, Enrico Paolini, Mark F. Flanagan
- **PDF**: https://ieeexplore.ieee.org/document/7938045
- **Abstract**: The design of protograph-based low-density parity-check (LDPC) code ensembles optimized for a finite number of decoder iterations is investigated. We show by example that protograph-based EXIT (PEXIT) analysis is not sufficiently reliable in the finite-iteration case, and develop a new technique which, similarly to PEXIT analysis, uses the mutual information (MI) as a tool in order to predict the performance of ensembles based on protographs. In contrast to PEXIT analysis, in which a critical value of the MI is used to define the decoding threshold, in our technique we examine the behavior of the MI over a range of channel parameters in order to define the threshold. Using this new definition of the iteration-constrained threshold, we perform a search over a large family of protographs in order to find the protograph with the highest iteration-constrained threshold for a finite number of iterations over the BEC.

## On the Performance of Short Tail-Biting Convolutional Codes for Ultra-Reliable Communications

- **Status**: ❌
- **Reason**: tail-biting convolutional codes(비-LDPC) 성능분석+Viterbi 디코딩, 바이너리 LDPC BP에 이식할 기법 없음
- **ID**: ieee:7938068
- **Type**: conference
- **Published**: 6-9 Feb. 2
- **Authors**: Lorenzo Gaudio, Tudor Ninacs, Thomas Jerkovits +1
- **PDF**: https://ieeexplore.ieee.org/document/7938068
- **Abstract**: Motivated by the increasing interest in powerful short channel codes for low-latency ultra-reliable communications, we analyze the performance of tail-biting convolutional codes with different memories, block lengths and code rates over the additive white Gaussian noise channel. The analysis is carried out both through Monte Carlo simulations and by upper bounding the error probability via Poltyrev's tangential sphere bound at very low error rates. For the simulations, the near maximum likelihood wrap-around Viterbi algorithm is considered. We then compare the performance of tail-biting convolutional codes both with finite-length performance bounds and with that of other channel codes that have been recently considered for ultra-reliable satellite telecommand links. For the shortest block lengths, tail-biting convolutional codes outperform significantly state-of-the-art iterative coding schemes, while as expected their performance degrades visibly with increasing block lengths.

## Multi-track Recording Systems Using Non-binary Error Correction Coding Schemes for Bit-patterned Magnetic Recording

- **Status**: ❌
- **Reason**: BPMR용 non-binary 부호+2D 신호처리/MAP 검출, 비이진+자기기록 특이적이라 제외
- **ID**: ieee:7938081
- **Type**: conference
- **Published**: 6-9 Feb. 2
- **Authors**: Hidetoshi Saito
- **PDF**: https://ieeexplore.ieee.org/document/7938081
- **Abstract**: In this paper, a new multi-track recording system based on two-dimensional (2D) signal processing schemes is proposed for bit-patterned magnetic recording (BPMR). This system uses a non-binary error-correcting code and a modulation code with 2D run-length limited constraints. The signal processing scheme in the proposed system gets mixed readback signal sequences from the parallel adjacent tracks using a single reading head simultaneously. These readback signal sequences are equalized to a frequency response given by a desired 2D generalized partial response (GPR) system for BPMR. In decoding, a single sequence detector using maximum a posteriori (MAP) estimation combined with pattern-dependent noise-predictive detection is able to detect the equalized GPR signal sequences for recorded data written in a group of parallel adjacent tracks. Using computer simulation, this decoding scheme improves the signalto- noise ratio compared to the conventional MAP detection under media noise.

## Comparison of Geometric and Probabilistic Shaping with Application to ATSC 3.0

- **Status**: ❌
- **Reason**: geometric/probabilistic shaping 비교(ATSC 3.0), 변조 정형화 주제. LDPC 디코더/구성 기여 없음
- **ID**: ieee:7937997
- **Type**: conference
- **Published**: 6-9 Feb. 2
- **Authors**: Fabian Steiner, Georg Boecherer
- **PDF**: https://ieeexplore.ieee.org/document/7937997
- **Abstract**: In this work, geometric shaping (GS) and probabilistic shaping (PS) for the additive white Gaussian noise (AWGN) channel is reviewed. Both approaches are investigated in terms of symbol-metric decoding (SMD) and bit-metric decoding (BMD). For GS, an optimization algorithm based on differential evolution is formulated. Achievable rate analysis reveals that GS suffers from a 0.4 dB signal-to-noise ratio (SNR) performance degradation compared to PS when BMD is used. Forward-error correction simulations of the ATSC 3.0 modulation and coding formats (modcods) confirm the theoretical findings. In particular, PS enables seamless rate adaptation with one modcod and it outperforms ATSC 3.0 GS modcods by more than 0.5 dB for spectral efficiencies larger than 3.2 bits per channel use.

## Approximate Image Authentication and Correction using Spatial and Frequency Domain Features

- **Status**: ❌
- **Reason**: 이미지 인증/워터마킹+RS 코드, 채널 ECC 아님. 떼어낼 LDPC 기법 없음
- **ID**: ieee:7938051
- **Type**: conference
- **Published**: 6-9 Feb. 2
- **Authors**: Obaid Ur-Rehman, Natasa Zivic, Christoph Ruland
- **PDF**: https://ieeexplore.ieee.org/document/7938051
- **Abstract**: Images traversing from source to sink can undergo intentional and unintentional modifications. An image authentication scheme is presented in this paper which is capable of detecting modifications in the image, locating their positions and correcting some or all of them. It is also able to tolerate minor unintentional modifications. However, intentional forgeries are detected by the proposed scheme. The idea is to build a watermark using local frequency domain image features and protecting them with Reed Solomon codes. This helps in the localization of modifications and their correction to the extent possible with the used code. At the same time, the global image histogram features are protected using an approximate message authentication code. This provides tolerance in authentication in the presence of unintentional modifications such as channel noise, image transformation operations, compression etc. Security strength of the proposed image authentication scheme is analyzed in the paper. Simulation results in the presence of unintentional modifications show the noise tolerant authentication capability, whereas simulation results in the presence of intentional modifications demonstrate the forgery detection capability of the proposed scheme.

## Flexible Length Polar Codes through Graph Based Augmentation

- **Status**: ❌
- **Reason**: Polar 부호 유연 길이(graph augmentation), 비-LDPC. BP는 polar 전용이라 LDPC 이식 기법 없음
- **ID**: ieee:7938067
- **Type**: conference
- **Published**: 6-9 Feb. 2
- **Authors**: A. Elkelesh, M. Ebada, S. Cammerer +1
- **PDF**: https://ieeexplore.ieee.org/document/7938067
- **Abstract**: The structure of polar codes inherently requires block lengths to be powers of two. In this paper, we investigate how different block lengths can be realized by coupling of several short-length polar codes. For this, we first analyze "code augmentation" to better protect the semipolarized channels, improving the BER performance under belief propagation decoding. Several serial and parallel augmentation schemes are discussed. A coding gain of 0:3 dB at a BER of 10(exp -5) can be observed for the same total rate and length. Further, we extend this approach towards coupling of several "sub-polar codes", leading to a reduced computational complexity and enabling the construction of flexible length polar codes.

## Algorithms for the Iterative Estimation of Discrete-Valued Sparse Vectors

- **Status**: ❌
- **Reason**: 압축센싱 이산값 희소벡터 추정, 채널코딩 ECC 아님(소스/추정)
- **ID**: ieee:7938053
- **Type**: conference
- **Published**: 6-9 Feb. 2
- **Authors**: Susanne Sparrer, Robert F. H. Fischer
- **PDF**: https://ieeexplore.ieee.org/document/7938053
- **Abstract**: In Compressed Sensing, a real-valued sparse vector has to be estimated from an underdetermined system of linear equations. In many applications, however, the elements of the sparse vector are drawn from a finite set. For the estimation of these discrete-valued vectors, matched algorithms are required which take the additional knowledge of the discrete nature into account. In this paper, the estimation problem is treated from a communications engineering point of view. A powerful new algorithm incorporating techniques known from digital communications and information theory is derived. For comparison, Turbo Compressed Sensing is adapted to the discrete setup and a simplified and generalized notation is presented. The performance of the algorithms is covered by numerical simulations.

## On the Relationship Between the KL Means Algorithm and the Information Bottleneck Method

- **Status**: ✅
- **Reason**: MI-최대화 양자기(IB/KL means)는 LDPC 디코더 LLR 양자화에 직접 이식 가능(C)
- **ID**: ieee:7938084
- **Type**: conference
- **Published**: 6-9 Feb. 2
- **Authors**: Brian M. Kurkoski
- **PDF**: https://ieeexplore.ieee.org/document/7938084
- **Abstract**: The problem of finding the mutual informationmaximizing quantizer of a discrete memoryless channel is important in the implementation of communication receivers, LDPC code decoders, and in the design of polar codes. Two algorithms algorithms that provide suboptimal solutions in polynomial time are the information bottleneck method and the KL means algorithm. The contribution of this paper is show that the information bottleneck method with beta ⃗ ∞ is algorithmically equivalent to the KL means algorithm. This is done by showing that both the DMC channel outputs, and the quantizer outputs, are in the same J-dimensional space, where J is the cardinality of the input alphabet.

## Combining LDPC codes, M-QAM modulations, and IFDMA multiple-access to achieve 5G requirements

- **Status**: ❌
- **Reason**: 표준 LDPC를 M-QAM/IFDMA와 결합한 5G 무선 응용, 떼어낼 ECC 기법 없음
- **ID**: ieee:7891828
- **Type**: conference
- **Published**: 22-24 Feb.
- **Authors**: Andrés Leonardo Ortega-Ortega, Jack Fernando Bravo-Torres
- **PDF**: https://ieeexplore.ieee.org/document/7891828
- **Abstract**: In this paper we explore the advantage of combining M-QAM modulations, LDPC codes, and IFDMA multi-access techniques in order to increase the capacity of the system, reduce the peak-to-average power ratio (PAPR) and to improve the BER performance. The simulation results show that our proposal provides better performance, even allowing significant reductions, of about 1 dB, in the PARP of the high-level modulation schemes, such as 64-QAM. In addition, the spectral efficiency and BER, using LDPC codes (FEC), provides a considerable advantage and low complexity respect to traditional systems.

## [Table of contents]

- **Status**: ❌
- **Reason**: 학술대회 목차로 논문 내용 없음
- **ID**: ieee:7891807
- **Type**: conference
- **Published**: 22-24 Feb.
- **Authors**: 
- **PDF**: https://ieeexplore.ieee.org/document/7891807
- **Abstract**: The following topics are dealt with: Atila; UIDP-based educational application generator; mobile devices; epileptic seizure detection; optical and electrical recordings; analytical workspace delineation; translational underconstrained cable-based robot; switching position-force controller; two independent finger gripper; Horn & Schunck parameter characterization; gradient based method; optical flow computing; longest classical EM waves; communications carriers; sensor fusion; serious game; children nutrition education; pupillary response; spiking neural network; latent semantic analysis; Syslog correlation; liquid level system; fuzzy control; visual odometry; trilateration method; stereo images; zone based hybrid approach; wireless sensor networks; falling people detection; autonomous service robots: ROS module integration approach; diabetes; pneumatic manipulator robot; back propagation neural network; capacitive touch interfaces; depth-first search satisfiability; mu-calculus; trees; LDPC codes; M-QAM modulations; IFDMA; 5G requirements; super-resolution methods; digital mammograms: multiscale iterative resolution; wavelet transform; cosine transform; wavelet family iterative scales; direct local search operators impact; memetic differential evolution; constrained numerical optimization problems; Mexican sign language recognition; Kinect; data time warping algorithm; object recognition modular system implementation; service robotics context; feature selection; botnets detection; machine learning algorithms; mosquito larva classification method; convolutional neural networks; LOD4AIR; linked open data and OAI-PMH repositories.

## Connectivity analysis of an AUV network with OFDM based communications

- **Status**: ❌
- **Reason**: AUV 수중 OFDM 네트워크 연결성 분석, LDPC는 부수 사용 — 떼어낼 기법 없음
- **ID**: ieee:7890334
- **Type**: conference
- **Published**: 21-24 Feb.
- **Authors**: Alper Bereketli, Muharrem Tumcakir, Ilkay Yazgi +3
- **PDF**: https://ieeexplore.ieee.org/document/7890334
- **Abstract**: Autonomous underwater vehicle (AUV) networks play a crucial role in tactical, commercial, and scientific applications, where reliable and robust communication protocols are needed due to the challenging characteristics of the channel. With this motivation, connectivity of AUV networks in different regions with varying transducer characteristics are analyzed through simulations based on real-life orthogonal frequency division multiplexing (OFDM) based communication experiments over noisy and Doppler-distorted channels. Doppler compensation is performed according to the autocorrelation using the cyclic prefix. Using binary and quadrature phase shift keying (BPSK and QPSK) modulation schemes in conjunction with low density parity check (LDPC) coding, error rate levels are investigated through shallow water pond and at-sea experiments. It is shown that, the utilized transmission scheme is capable of correcting all bit errors among nearly one million bits transmitted up to a distance of 1 km, yielding a payload rate of 15.6 kbps with 4096 subcarriers and QPSK modulation. The simulations provide key parameters that must be taken into account in the design of scalable and connected AUV networks.

## New code based identification scheme

- **Status**: ❌
- **Reason**: MDPC 기반 코드기반 신원확인(보안 프로토콜), 채널 ECC 디코더/구성 기여 없음
- **ID**: ieee:7889187
- **Type**: conference
- **Published**: 20-22 Feb.
- **Authors**: Hamza Moufek, Kenza Guenda
- **PDF**: https://ieeexplore.ieee.org/document/7889187
- **Abstract**: In this paper, we propose a new identification scheme, based on two hard problems: the syndrome decoding problem and the problem of finding the parity-check matrix from the generator matrix of an MDPC-code. Our scheme is zero-knowledge and it has a short key compared to other protocols.

## Random-permutation-matrix-based cyclically-coupled LDPC codes

- **Status**: ✅
- **Reason**: 신규 코드 설계 기여(random-permutation-matrix 기반 CC-LDPC) + FPGA BER 시뮬·디코더 복잡도 비교, 바이너리 QC-LDPC 계열 → E
- **ID**: ieee:7890139
- **Type**: conference
- **Published**: 19-22 Feb.
- **Authors**: Francis C. M. Lau, Fanlu Mo, Wai M. Tarn +1
- **PDF**: https://ieeexplore.ieee.org/document/7890139
- **Abstract**: Cyclically-coupled quasi-cyclic low-density parity-check (CC-QC-LDPC) codes are a new class of QC-LDPC codes which can achieve excellent error performance and relatively low hardware requirement. In this paper, we modify the CC-QC-LDPC code construction by using random permutation matrices instead of circulant permutation matrices, forming the “random-permutation-matrix-based CC-LDPC (RP-CC-LDPC) code”. The objective is to achieve a better error performance under the same code length. We simulate the bit error rate using FPGA simulations. We also compare the BER results and decoder complexity of the above codes with those of regular and irregular QC-LDPC codes under the same code length and code rate.

## LDPC convolutional codes coded cooperation based on puncturing

- **Status**: ❌
- **Reason**: LDPC convolutional+puncturing의 5G coded cooperation 응용, MIMO/diversity 통신 특이적이고 떼어낼 신규 디코더·구성 기법 없음
- **ID**: ieee:7890141
- **Type**: conference
- **Published**: 19-22 Feb.
- **Authors**: Wenhe Jin, Shaohua Wu, Erpeng Yang +1
- **PDF**: https://ieeexplore.ieee.org/document/7890141
- **Abstract**: Coded cooperation is a kind of virtual MIMO transmission technology that can achieve both coding gain and diversity gain, which is very promising in 5G communication. To design a scheme that can be used for near-capacity transmission and can be generalized for slow and fast fading channels, this paper studies the coding cooperation based on convolutional LDPC codes. Firstly, channel coding the original information by LDPC convolutional codes, then divided the coded words into two parts by puncturing algorithm; secondly, introducing space-time transmission into the second frame of coded cooperation, so the diversity gain can be obtained under different fading scenarios. Simulation results show that the system performance can be improved generally.

## Performance of PLC synchronization for DOCSIS 3.1 receiver

- **Status**: ❌
- **Reason**: DOCSIS 3.1 PLC OFDM 동기화 기법, LDPC는 부수 언급뿐 떼어낼 ECC 기법 없음
- **ID**: ieee:7890166
- **Type**: conference
- **Published**: 19-22 Feb.
- **Authors**: Jaeho Lee, Younok Park, Seungchan Bang
- **PDF**: https://ieeexplore.ieee.org/document/7890166
- **Abstract**: A Physical layer link channel (PLC) is a narrowband signaling channel located within the downstream OFDM channel used in data-over-service-interface specifications (DOCSIS) 3.1 system. It consists of a PLC preamble and PLC data which include information about a low density parity check (LDPC) coding rate, QAM order and interleaver depth etc. PLC preamble has +1 or −1 for PLC synchronization. In this paper, a novel method of PLC synchronization in frequency domain is proposed to demodulate a received orthogonal frequency division multiplexing (OFDM) signal correctly.

## Reed-Solomon based globally coupled quasi-cyclic LDPC codes

- **Status**: ✅
- **Reason**: RS 패리티검사 기반 globally coupled QC-LDPC 신규 구성과 2-phase local/global 디코딩, 바이너리 코드설계 이식 가능(E)
- **ID**: ieee:8023442
- **Type**: conference
- **Published**: 12-17 Feb.
- **Authors**: Juane Li, Keke Liu, Shu Lin +1
- **PDF**: https://ieeexplore.ieee.org/document/8023442
- **Abstract**: This paper presents a special type of LDPC codes constructed based on the conventional parity-check matrices of Reed-Solomon (RS) codes. LDPC codes of this type are referred to as globally coupled RS-LDPC codes. These codes are designed for correcting random errors, random short phased bursts of erasures and long bursts of erasures. The Tanner graph of a globally coupled RS-LDPC is composed of a number of disjoint copies of the Tanner graph of a local RS-LDPC code which are connected together by a group of overall check-nodes (CNs), called global CNs. A globally coupled RS-LDPC code can be decoded with a two-phase local/global iterative scheme which allows correction of local random errors and phased bursts of erasures in the local phase and global random errors and a single long burst of erasures in the global phase.

## Integrated code design for a joint source and channel LDPC coding scheme

- **Status**: ❌
- **Reason**: JSCC(소스-채널 결합) LDPC 코드 설계 — 떼어낼 순수 채널 ECC 기법 없음, 기준상 JSCC 원칙 제외
- **ID**: ieee:8023458
- **Type**: conference
- **Published**: 12-17 Feb.
- **Authors**: Hsien-Ping Lin, Shu Lin, Khaled Abdel-Ghaffar
- **PDF**: https://ieeexplore.ieee.org/document/8023458
- **Abstract**: This paper presents a design of LDPC codes for a joint source-channel (JSC) coding system. In the construction of such an LDPC code, the source compression matrix and the channel code parity-check matrix are designed jointly. The integrated matrix is used for both JSC encoding and decoding. Experimental results show that the codes constructed not only perform well in the waterfall region but also achieve low error-floors.

## Correcting errors by natural redundancy

- **Status**: ❌
- **Reason**: 압축데이터의 natural redundancy 활용 소스코딩+채널코딩 결합, 떼어낼 LDPC ECC 기법 없음
- **ID**: ieee:8023455
- **Type**: conference
- **Published**: 12-17 Feb.
- **Authors**: Anxiao Jiang, Pulakesh Upadhyaya, Erich F. Haratsch +1
- **PDF**: https://ieeexplore.ieee.org/document/8023455
- **Abstract**: For the storage of big data, there are significant challenges with its long-term reliability. This paper studies how to use the natural redundancy in data for error correction, and how to combine it with error-correcting codes to effectively improve data reliability. It explores several aspects of natural redundancy, including the discovery of natural redundancy in compressed data, the efficient decoding of codes with random structures, the capacity of error-correcting codes that contain natural redundancy, and the time-complexity tradeoff between source coding and channel coding.

## Multi-bit flipping algorithms with probabilistic gradient descent

- **Status**: ✅
- **Reason**: 바이너리 LDPC용 새로운 멀티비트 비트플립+확률적 경사하강(PGD-MBF) 디코더 — 저복잡도 디코더 알고리즘(C), NAND 이식 가능
- **ID**: ieee:8023480
- **Type**: conference
- **Published**: 12-17 Feb.
- **Authors**: Bane Vasić, Predrag Ivaniš, Srdan Brkic
- **PDF**: https://ieeexplore.ieee.org/document/8023480
- **Abstract**: A new class of bit flipping algorithms for low-density parity-check codes over the binary symmetric channel is proposed. The algorithms employ multiple bits at a variable node to represent its reliability, and multiple bits a check node to capture the sequence of its syndrome values. The check node update function thus requires a simple bit-shift operation, while the variable node updates require a nonlinear Boolean function. This class of multi-bit flipping (MBF) algorithms is enhanced by the probabilistic gradient descent (PGD) algorithm. The gradient descent algorithm minimizes the variable node energy function which, in addition to the classical term which quantifies the discrepancy between the variable estimate and channel value, also involves an additive term defined as a weighted sum of neighboring check node states. Only the variable nodes with the maximal value of energy are eligible for updating, but the updates are not done by default but probabilistically. The resulting probabilistic gradient descent multi-bit flipping PGD-MBF algorithm combined with rewinding improves the codeword probability of error while keeping the complexity lower than that of the state-of-the-art algorithms of comparable throughput.

## Using QAM-9 and ternary noise-immune codes to approach the Shannon bound

- **Status**: ❌
- **Reason**: QAM-9+삼진 부호 변조/코딩 방식, 비이진·비-LDPC이며 이식 기법 없음.
- **ID**: ieee:7910520
- **Type**: conference
- **Published**: 1-3 Feb. 2
- **Authors**: Vitaly Kuznetsov, Vladimir Batura, Alexey Solodkov +1
- **PDF**: https://ieeexplore.ieee.org/document/7910520
- **Abstract**: Analysis of experimental results of the binary noise-immune coding with one-dimensional modulation best achievements points out the impossibility of achievement the continuous Gaussian channel parameters of such scheme in practice. In the paper is exhibited that changeover to more effective two-dimensional non-binary PAM modulation with ternary noise-immune codes in each quadrature branch of a modem allows to work with high enough reliability and to reach frequency-energetical system parameters that are equal to analogous parameters of continuous channel with AWGN. Symbol error probability Qs=10-4 for Eb/N0=4.963 and total spectral efficiency 4.036 bit/s/Hz have achieved for best modulation and coding scheme from proposed set.

## Error probability bounds for SCMA signals

- **Status**: ❌
- **Reason**: SCMA 오류확률 bound 분석, LDPC 부호 아니고 떼어낼 디코더·구성 기법 없음.
- **ID**: ieee:7910519
- **Type**: conference
- **Published**: 1-3 Feb. 2
- **Authors**: Vyacheslav P. Klimentyev, Alexander B. Sergienko
- **PDF**: https://ieeexplore.ieee.org/document/7910519
- **Abstract**: In this paper, we investigated error probability bounds for sparse code multiple access (SCMA) signals. SCMA is one of proposed non-orthogonal multiple access schemes for Fifth generation (5G) wireless communication standard. This scheme allows to increase the number of active users inside a given time-frequency resource. For AWGN and Rayleigh (without diversity) channels, we calculated union bounds for symbol and bit error probability. Asymptotic bound based on minimal distance between signals is also calculated. Analytical bounds are compared with simulations results (Maximum Likelihood (ML) Algorithm and Message Passing Algorithm (MPA) were used for signal reception). For AWGN channel, the results show that analytical bounds (symbol and bit error probabilities) are tight in the high-SNR region. For Rayleigh channel, analytical bound for symbol error probability are pessimistic with the gap of approximately 0.7 dB in the medium- and high-SNR regions.

## Soft Hint Enabled Adaptive Visible Light Communication over Screen-Camera Links

- **Status**: ❌
- **Reason**: VLC screen-camera용 rateless/erasure 코딩 응용, LDPC ECC로 떼어낼 디코더/구성 기법 없음
- **ID**: ieee:7448931
- **Type**: journal
- **Published**: 1 Feb. 201
- **Authors**: Wan Du, Jansen Christian Liando, Mo Li
- **PDF**: https://ieeexplore.ieee.org/document/7448931
- **Abstract**: Screen-camera links for Visible Light Communication (VLC) are diverse, as the link quality varies according to many factors, such as ambient light and camera's performance. This paper presents SoftLight, a channel coding approach that considers the unique channel characteristics of VLC links and automatically adapts the transmission data rate to the link qualities of various scenarios. SoftLight incorporates two new ideas: (1) an expanded color modulation interface that provides soft hint about its confidence in each demodulated bit and establishes a bit-level VLC erasure channel, and (2) a rateless coding scheme that achieves bit-level rateless transmissions with low computation complexity and tolerates the false positive of bits provided by the soft hint enabled erasure channel. SoftLight is orthogonal to the visual coding schemes and can be applied atop any barcode layouts. We implement SoftLight on Android smartphones and evaluate its performance under a variety of environments. The experiment results show that SoftLight can correctly transmit a 22-KByte photo between two smartphones within 0.6 second and improves the average goodput of the state-of-the-art screen-camera VLC solution by 2.2×.
