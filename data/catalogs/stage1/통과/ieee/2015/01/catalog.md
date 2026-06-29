# IEEE Xplore — 2015-01 (1차선별 통과)


## On the Encoding Complexity of Quasi-Cyclic LDPC Codes

- **Status**: ✅
- **Reason**: QC-LDPC 인코딩 복잡도 저감 PCM 구성 기법(HW 면적 40-55% 감소) — 바이너리 QC-LDPC 코드 설계/HW(E/D) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7174548
- **Type**: journal
- **Published**: Nov.15, 20
- **Authors**: Ahmed Mahdi, Vassilis Paliouras
- **PDF**: https://ieeexplore.ieee.org/document/7174548
- **Abstract**: In this paper, we propose a parity check matrix (PCM) construction technique that reduces the encoding complexity of quasi-cyclic (QC)-LDPC codes. The proposed construction method is based on a constraint selection of shifting factors, shown here to reduce the density of an inverted matrix used in several encoding algorithms. Furthermore, it demonstrates that the complexity of encoding schemes involving inverted matrices, can be defined by the density of the small inverted binary base matrix and not by the extended QC-PCM. Comparisons of the proposed codes with codes employed in international standards and with randomly shifted QC-LDPC codes of comparable characteristics, show the low complexity of the corresponding hardware implementations and a BER performance equivalent to that of previously reported codes without increasing the decoding complexity. Furthermore, adoption of the proposed method can decrease the complexity of several encoding procedures; in particular, an area reduction of 40%–55% is reported for QC-LDPC encoders, while a reduction of 86% is reported for Multi-Level-QC-LDPC encoders.

## Joint Detection and Decoding in LDPC-Based Space-Time Coded MIMO-OFDM Systems via Linear Programming

- **Status**: ✅
- **Reason**: LDPC LP 디코딩에 적응적 패리티검사 부등식 축소 기법 제시 — joint LP는 MIMO-OFDM 특이적이나 LP 디코딩 복잡도 감소 기법은 바이너리 LDPC BP/LP 디코더로 이식 가능성 있음(C). 애매하여 보존
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7084660
- **Type**: journal
- **Published**: July1, 201
- **Authors**: Kun Wang, Hong Shen, Wenhao Wu +1
- **PDF**: https://ieeexplore.ieee.org/document/7084660
- **Abstract**: This work proposes a novel linear programming approach for the joint detection and decoding of LDPC-based space-time (ST) coded signals in multi-antenna orthogonal frequency division multiplexing (OFDM) systems. While traditional receivers typically decouple the detection and decoding processes as two disjunctive blocks or require iterative turbo exchange of extrinsic information between the soft detector and decoder, we formulate a joint linear program (LP) by exploiting the constraints imposed on the data symbols, training symbols, noise subspace as well as channel code. In consideration of the vast amount of LDPC parity check inequalities, we further present an adaptive procedure to significantly reduce the complexity of the joint LP receiver. Our LP-based receivers outperform existing receivers with substantial performance gains. Moreover, the proposed joint LP receiver demonstrates strong robustness when pilot symbols are sparsely arranged on subcarriers.

## Construction of Type-II QC LDPC Codes Based on Perfect Cyclic Difference Set

- **Status**: ✅
- **Reason**: 바이너리 QC-LDPC 신규 구성(perfect CDS 기반 type-II, girth>=6, error floor 개선) — E 코드설계 기여
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10855193
- **Type**: journal
- **Published**: January 20
- **Authors**: Lijun Zhang, Bing Li, Leelung Cheng
- **PDF**: https://ieeexplore.ieee.org/document/10855193
- **Abstract**: Quasi-cyclic (QC) Low-density parity-check (LDPC) codes are constructed from combination of weight-0 (null matrix) and Weight-2 (W2) Circulant matrix (CM), which can be seen as a special case of the general type-II QC LDPC codes. The shift matrix of the codes is built on the basis of one integer sequence, called perfect Cyclic difference set (CDS), which guarantees the girth of the code at least six. Simulation results show that the codes can perform well in comparison with a variety of other LDPC codes. They have excellent error floor and decoding convergence characteristics.

## Design of a High-Throughput QC-LDPC Decoder With TDMP Scheduling

- **Status**: ✅
- **Reason**: 바이너리 QC-LDPC TDMP 스케줄링 디코더 HW + hybrid normalized MS, 데이터상관/메모리충돌 해소 — C/D 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6920049
- **Type**: journal
- **Published**: Jan. 2015
- **Authors**: Ming Zhao, Xiaolin Zhang, Ling Zhao +1
- **PDF**: https://ieeexplore.ieee.org/document/6920049
- **Abstract**: Low-density parity-check (LDPC) codes with turbodecoding message-passing (TDMP) scheduling can obtain good performance and high convergence rates. In addition, the min- sum (MS) algorithm can reduce the complexity. The hybrid normalized MS algorithm with TDMP scheduling is presented to achieve good performance and to lower the complexity. For a quasi-cyclic LDPC (QC-LDPC) code with a long code length, parallel degree optimization and an offset iterative sequence rule are proposed. With the proposed techniques, the data correlation problem and memory access conflicts during TDMP scheduling can be resolved so that the iteration can smoothly proceed through the reasonable division of each block row. Fabricated in the 90-nm 1-Poly 9-Metal (1P9M) CMOS process, a multimode 96000-bit irregular QC-LDPC decoder is implemented. It attains throughputs of 1.7-3.0 Gb/s and dissipates an average power of 502 mW at an operation frequency of 100 MHz and at 10 iterations. The decoder chip area is 13.32 mm2, with a core area of 9.73 mm2.

## Low-Complexity Tree Architecture for Finding the First Two Minima

- **Status**: ✅
- **Reason**: min-sum 디코더용 first-two-minima 트리 HW 아키텍처, 비교기 재사용 — D 직접 이식
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:6922514
- **Type**: journal
- **Published**: Jan. 2015
- **Authors**: Youngjoo Lee, Bongjin Kim, Jaehwan Jung +1
- **PDF**: https://ieeexplore.ieee.org/document/6922514
- **Abstract**: This brief presents an area-efficient tree architecture for finding the first two minima as well as the index of the first minimum, which is essential in the design of a low-density parity-check decoder based on the min-sum algorithm. The proposed architecture reduces the number of comparators by reusing the intermediate comparison results computed for the first minimum in order to collect the candidates of the second minimum. As a result, the proposed tree architecture improves the area-time complexity remarkably.

## Efficient majority logic fault detection and correction using EG-LDPC codes for memory applications

- **Status**: ✅
- **Reason**: E/C: 메모리용 EG-LDPC majority-logic 디코딩, 디코딩 시간 단축 수정 구현 - 메모리 ECC 디코더 기법
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7282232
- **Type**: conference
- **Published**: 9-10 Jan. 
- **Authors**: V. Lakshmanan, R. Dhananjeyan, A. Narendrakumar
- **PDF**: https://ieeexplore.ieee.org/document/7282232
- **Abstract**: SER is increasing for every IC process generation. Radiation induced soft errors are major concern in semiconductor memories due to technology scaling, higher integration densities and lower operating voltages. Nowadays memory cells are protected by using error correction codes. Among various multiple error correction codes ML decodable codes are suitable for memory applications due to their capability to detect a large number of errors but it requires large decoding time. In this paper a special type of low density parity check (LDPC) codes, which belongs to the family of majority logic decoding called Euclidean Geometry Low Density Parity Check (EG-LDPC) codes which detects the error in less cycle time so the decoding time is greatly reduced and also the memory accessing time also get reduced. The recent paper deals only with error detection in memories but the present paper focus on both error detection and correction by modified implementation of majority gate. The simulation results are compared with the existing techniques.

## Asynchronous decoding of LDPC codes over BEC

- **Status**: ✅
- **Reason**: LDPC 비동기 메시지패싱 스케줄링; HW 구현 시 디코딩 시간 단축, NAND LDPC 디코더 스케줄링(C)에 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7282942
- **Type**: conference
- **Published**: 2015
- **Authors**: S. Haghighatshoar, A. Karbasi, A. H. Salavati
- **PDF**: https://ieeexplore.ieee.org/document/7282942
- **Abstract**: LDPC codes are typically decoded by running a synchronous message passing algorithm over the corresponding bipartite factor graph (made of variable and check nodes). More specifically, each synchronous round consists of 1) updating all variable nodes based on the information received from the check nodes in the previous round, and then 2) updating all the check nodes based on the information sent from variable nodes in the current round. However, in many applications, ranging from message passing in neural networks to hardware implementation of LDPC codes, assuming that all messages are sent and received at the same time is far from realistic. In this paper, we investigate the effect of asynchronous message passing on the decoding of LDPC codes over a Binary Erasure Channel (BEC). We effectively assume that there is a random delay assigned to each edge of the factor graph that models the random propagation delay of a message along the edge. As a result, the output messages of a check/variable node are also asynchronously updated upon arrival of a new message in its input. We show, for the first time for BEC, that the asymptotic performance of the asynchronous message passing is fully characterized by a fixed point integral equation that takes into account both the temporal and the spatial features of the factor graph. Our theoretical result is reminiscent of the fixed point equation in traditional BP decoding. Also, our simulation results show that asynchronous scheduling reduces decoding time compared to the traditional BP in certain cases in the finite block-length regime.

## Reconfigurable decoder for irregular random low density parity check matrix based on FPGA

- **Status**: ✅
- **Reason**: 불규칙 랜덤 LDPC용 부분병렬 재구성형 FPGA 디코더, quad-port 메모리로 4배 throughput — 이식 가능 HW 아키텍처(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:7146937
- **Type**: conference
- **Published**: 2015
- **Authors**: M. Musiyenko, Y. Krainyk, O. Denysov
- **PDF**: https://ieeexplore.ieee.org/document/7146937
- **Abstract**: Method for design of partially parallel reconfigurable LDPC-decoder based on FPGA is presented in the paper. The decoder is able to process messages according to irregular random parity check matrix. The decoder can work with irregular random matrix and makes only small constraints on its structure. Parallel processing with several decoding units is considered. It is shown that decoder based on quad-port memory created on two-port memory can increase throughput in four times.

## LDPC code design for noncoherent physical layer network coding

- **Status**: ✅
- **Reason**: EXIT 기반 바이너리 LDPC variable node degree distribution 최적화—코드설계(E) 이식 가능, 애매하여 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7248628
- **Type**: conference
- **Published**: 2015
- **Authors**: T. Ferrett, M. C. Valenti
- **PDF**: https://ieeexplore.ieee.org/document/7248628
- **Abstract**: This work considers optimizing LDPC codes in the physical-layer network coded two-way relay channel using noncoherent FSK modulation. The error-rate performance of channel decoding at the relay node during the multiple-access phase was improved through EXIT-based optimization of Tanner graph variable node degree distributions. Codes drawn from the DVB-S2 and WiMAX standards were used as a basis for design and performance comparison. The computational complexity characteristics of the standard codes were preserved in the optimized codes by maintaining the extended irregular repeat-accumulate (eIRA). The relay receiver performance was optimized considering two modulation orders M = {4; 8} using iterative decoding in which the decoder and demodulator refine channel estimates by exchanging information. The code optimization procedure yielded unique optimized codes for each case of modulation order and available channel state information. Performance of the standard and optimized codes were measured using Monte Carlo simulation in the flat Rayleigh fading channel, and error rate improvements up to 1:2 dB are demonstrated depending on system parameters.

## Spatially-coupled codes for write-once memories

- **Status**: ✅
- **Reason**: WOM용 spatially-coupled compound LDGM/LDPC 신규 구성 + 메시지패싱 enc/dec, 코드설계(E) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7446994
- **Type**: conference
- **Published**: 2015
- **Authors**: S. Kumar, A. Vem, K. Narayanan +1
- **PDF**: https://ieeexplore.ieee.org/document/7446994
- **Abstract**: The focus of this article is on low-complexity capacity-achieving coding schemes for write-once memory (WOM) systems. The construction is based on spatially-coupled compound LDGM/LDPC codes. Both noiseless systems and systems with read errors are considered. Compound LDGM/LDPC codes are known to achieve capacity under MAP decoding for the closely related Gelfand-Pinsker problem and their coset decomposition provides an elegant way to encode the messages while simultaneously providing error protection. The application of compound codes to the WOM system is new. The main result is that spatial coupling enables these codes to achieve the capacity region of the 2-write WOM system with low-complexity message-passing encoding and decoding algorithms.

## Scaling Rules for the Energy of Decoder Circuits

- **Status**: ✅
- **Reason**: LDPC 디코더 회로 에너지/면적-시간 복잡도 하한; HW 구현 스케일링 통찰로 NAND LDPC HW 아키텍처에 참조 가능(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:7282693
- **Type**: conference
- **Published**: 2015
- **Authors**: C. G. Blake, F. R. Kschischang
- **PDF**: https://ieeexplore.ieee.org/document/7282693
- **Abstract**: A standard VLSI model is used to derive universal lower bounds on the energy of decoder circuits. In the circuit model used, the product of the circuit area and number of clock cycles, or the area-time complexity is proportional to the energy of computation. Lower bounds as a function of block length n are presented for three different circuit paradigms. Firstly, for circuits that compute in parallel, an Ω(n(logn)1/2) scaling rule is shown. Secondly, for circuits that compute serially, an Ω(nlogn) lower bound is presented. Thirdly, for a sequence of decoding circuits in which the number of output pins grows arbitrarily with block length, the energy is shown to grow as Ω(n(logn)1/5). In addition, it is shown that the energy complexity of almost all LDPC decoders that can get close to capacity and whose Tanner graphs are generated according to a uniform standard configuration model must take Ω(n2) area to implement directly.

## Belief-propagation reconstruction for compressed sensing: Quantization vs. Gaussian approximation

- **Status**: ✅
- **Reason**: BP 메시지 양자화 vs 가우시안 근사 비교 — 소스코딩 아닌 BP 메시지 양자화 기법으로 NAND LLR 양자화에 이식 가능성, 애매하여 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7447132
- **Type**: conference
- **Published**: 2015
- **Authors**: M. Lian, H. D. Pfister
- **PDF**: https://ieeexplore.ieee.org/document/7447132
- **Abstract**: This work considers the compressed sensing (CS) of i.i.d. signals with sparse measurement matrices and belief-propagation (BP) reconstruction. In general, BP reconstruction for CS requires the passing of messages that are distributions over the real numbers. To implement this in practice, one typically uses either quantized distributions or a Gaussian approximation. In this work, we use density evolution to compare the reconstruction performance of these two methods. Since the reconstruction performance depends on the signal realization, this analysis makes use of a novel change of variables to analyze the performance for a typical signal. Simulation results are provided to support the results.

## Soft decision decoding of RAID stripe for higher endurance of flash memory based solid state drives

- **Status**: ✅
- **Reason**: SSD RAID 스트라이프 soft decision 디코딩 + LDPC soft info 활용 — A/B 스토리지 ECC 직접
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7069413
- **Type**: conference
- **Published**: 2015
- **Authors**: R. Motwani, C. Ong
- **PDF**: https://ieeexplore.ieee.org/document/7069413
- **Abstract**: RAID schemes have been in use for hard disk drives to provide improved performance or fault tolerance. RAID schemes, particularly RAID 2 and higher comprise of striping and adding parity. For solid state drives (SSDs), to combat die failures, schemes like RAID 5 and RAID 6 are effective. The idea is to have block level striping with distributed parity to provide data recovery in case of single or multiple die failures. In this work, we analyze the RAID 5 case used in SSDs when there is no die failure. For this case, the distributed parity information can be used to either combat higher raw bit error rate (RBER) or to improve the uncorrectable bit error rate (ÜBER). The algorithm we propose can be used with BCH or LDPC codes. With LDPC codes, it uses soft information on RAID 5 parity in order to recover from multiple error correcting code (ECC) fatals in a RAID stripe. The entire stripe data is read and then decoding is performed using the RAID parity to try recovery. We used simulations in order to characterize the RBER gains. First, modeling of the RBER distribution of the dies was performed using the log-normal distribution. Using this model, a performance evaluation for ECC schemes like LDPC codes and BCH codes was performed. We show that if LDPC codes are used, RAID 5 theoretically offers an RBER capability which is 3 times that of the error correcting code RBER capability. However, it is not possible to realize this RBER benefit completely since it has SSD performance downside. In order to meet the Quality of Service (QoS) specification, a realizable RBER gain is by a factor of 1.3 to 2 instead of 3. Further, these gains can only be realized if an LDPC code is used as an error correcting code, algebraic codes like BCH codes will provide limited gains. If no RBER benefit is permitted by a particular configuration of solid state drive, this scheme can be used to provide UBER gain by 3 orders of magnitude.

## Protograph design for spatially-coupled codes to attain an arbitrary diversity order

- **Status**: ✅
- **Reason**: Novel algorithm to build protograph-based SC-LDPC ensembles with target diversity order; binary LDPC code construction (E).
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7360752
- **Type**: conference
- **Published**: 2015
- **Authors**: N. ul Hassan, I. Andriyanova, M. Lentmaier +1
- **PDF**: https://ieeexplore.ieee.org/document/7360752
- **Abstract**: This work focuses on the design of SC-LDPC codes for transmission over non-ergodic, block-fading channels. Our main contribution is an algorithm, allowing to start from a (J,K)-regular, uncoupled LDPC ensemble, from which one can recursively build up a protograph-based SC-LDPC ensemble having any target diversity order d. The diversity order is achieved assuming a low-complexity iterative decoding algorithm. The increase of d comes at the cost of increasing the memory constraint (i.e., the coupling parameter) of the SC-LDPC ensemble.

## Ensemble weight enumerators for protographs: A proof of Abu Surra's conjecture and a continuous relaxation for a faster enumeration

- **Status**: ✅
- **Reason**: 프로토그래프 LDPC(SC-LDPC 포함) ensemble weight enumerator 계산 신기법; 코드 설계/error floor 분석 도구로 이식 가능(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7282985
- **Type**: conference
- **Published**: 2015
- **Authors**: T. Benaddi, C. Poulliat, M. -L. Boucheret +2
- **PDF**: https://ieeexplore.ieee.org/document/7282985
- **Abstract**: In this paper, we provide a proof for the conjecture made by Abu Surra et al. [1] to simplify the computation of ensemble input output weight enumerators for protograph-based low density parity check (LDPC) codes. Furthermore, we propose a new method to compute more efficiently the ensemble weight enumerator. This approach can be applied particularly to lighten the computations for high rate codes, generalized LDPC codes or spatially coupled LDPC codes.

## Iterative threshold decoding of Quasi-Cyclic One Step Majority logic decodable codes

- **Status**: ✅
- **Reason**: 완전차집합 기반 QC 1단 다수결판정 부호가 LDPC 서브패밀리로 BP 디코딩 가능, BER 비교 제시. 신규 QC-LDPC 구성·디코딩(E/C).
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7489656
- **Type**: conference
- **Published**: 2015
- **Authors**: K. Rkizat, M. Lahmer, M. Belkasmi
- **PDF**: https://ieeexplore.ieee.org/document/7489656
- **Abstract**: This paper presents a new class of Quasi-Cyclic One Step Majority logic codes of 1/2 rate constructed from perfect difference set. Theses codes can be encoded with low complexity, and perform very well when decoded with the Iterative threshold decoding algorithm. Much of these codes is a subfamily of the LDPC codes and can be decoded using belief propagation algorithm. A comparison between our results and those for LDPC code in terms of BER performance are presented.

## Experimental demonstration of cycle-slip-tolerant turbo differential decoding for 100-Gb/s DP-DQPSK coherent transmission

- **Status**: ✅
- **Reason**: Cycle-slip-tolerant turbo differential decoding via dynamic decoding/limiting in soft-decision LDPC; decoder technique, keep for Phase 3
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7341656
- **Type**: conference
- **Published**: 2015
- **Authors**: F. Yu, Z. Xiao, M. Li +3
- **PDF**: https://ieeexplore.ieee.org/document/7341656
- **Abstract**: We propose and experimentally demonstrate the use of dynamic decoding and limiting to achieve high-performance cycle-slip-tolerant turbo differential decoding in soft-decision LDPC, reducing the differential decoding penalty by 2 dB even in the presence of 10-2 probability of cycle slips.

## Use soft-decision error-correction codes in Phase-Change Memory

- **Status**: ✅
- **Reason**: 멀티레벨 PCM에 LDPC soft-decision, LLR read level 저감 비균일 보정 — read 양자화 기법 NAND 이식 가능(A/C 근접)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7153460
- **Type**: conference
- **Published**: 2015
- **Authors**: Binbin Li, Bolun Zhang, Yifan Zhang +1
- **PDF**: https://ieeexplore.ieee.org/document/7153460
- **Abstract**: Researches indicate that the resistance of phase-change material will become larger over the time. Use time-aware based soft-decision error correction code, which needs LLR to decode, can correct the errors in multilevel PCM effectively. Accurate LLR needs to read the resistance accurately, which will lead to a longer transmission latency. In this paper, we proposed a non-uniform correction strategy, which can reduce the read levels maintaining bit-error-rate performance. We use LDPC in correction of 4-level per cell PCM, and get the result via computer simulation.

## Multi-level probabilistic timing error reliability analysis using a circuit dependent fault map generation

- **Status**: ✅
- **Reason**: flooded Min-Sum LDPC 디코더의 타이밍 에러 신뢰성/결함주입 분석 — HW 결함 내성 평가가 NAND LDPC 디코더 HW 신뢰성에 참조 가능, 애매하여 살림(Phase 3 재검토).
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:7388580
- **Type**: conference
- **Published**: 2015
- **Authors**: A. Amaricai, N. Cucu-Laurenciu, O. Boncalo +4
- **PDF**: https://ieeexplore.ieee.org/document/7388580
- **Abstract**: This paper proposes a methodology for timing error analysis of RTL circuit descriptions. The evaluation has three components: (i) statistical static timing analysis (SSTA) for standard cell components (ii) estimation based on probability density function (PDF) propagation for characterization of combinational blocks, and (iii) simulated fault injection (SFI) performed at RTL. Reliability characterization of basic components is derived using SSTA; PDF propagation is used to accurately capture the probabilistic error profile of each primary output (PO) of combinational blocks; RTL saboteur based SFI is employed in order to assess the reliability of the whole circuit. The proposed methodology is applied for the fault tolerance analysis of a flooded Min-Sum (MS) LDPC decoder.

## Bethe and M-Bethe Permanent Inequalities

- **Status**: ✅
- **Reason**: Bethe/M-Bethe permanent 부등식 — protograph LDPC BP 성능 분석/코드설계 함의, 애매하여 살림(Phase 3 재검토)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7417452
- **Type**: conference
- **Published**: 2015
- **Authors**: R. Smarandache, M. Haenggi
- **PDF**: https://ieeexplore.ieee.org/document/7417452
- **Abstract**: It was recently conjectured that the permanent of a $P$-lifting $\theta^{\uparrow P}$ of a matrix $\theta$ of degree $M$ is less than or equal to the $M$th power of the permanent perm$(\theta)$, i.e., perm$(\theta^{\uparrow P})\leq$perm$(\theta)^M$ and, consequently, that the degree-$M$ Bethe permanent perm$_{M,\mathrm{B}} (\theta)$ of a matrix $\theta$ is less than or equal to the permanent perm$(\theta)$ of $\theta$, i.e., perm$_{M, \mathrm{B}} (\theta)\leq$perm$(\theta)$. In this paper, we prove these related conjectures and show some properties of the permanent of block matrices that are lifts of a matrix. As a corollary, we obtain an alternative proof of the inequality perm$_{\mathrm{B}} (\theta)\leq$perm$(\theta)$ on the Bethe permanent of the base matrix $\theta$, which uses only the combinatorial definition of the Bethe-permanent. The results have implications in coding theory. Since a $P$-lifting corresponds to an $M$-graph cover and thus to a protograph-based LDPC code, the results may help explain the performance of these codes.

## Wave-Like Solutions of General 1-D Spatially Coupled Systems

- **Status**: ✅
- **Reason**: spatially-coupled 바이너리 LDPC threshold saturation을 EXIT-area 그래픽 기준으로 증명, BP/min-sum 적용 — SC-LDPC 코드설계(E)·디코더 분석 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7115123
- **Type**: journal
- **Published**: 2015
- **Authors**: S. Kudekar, T. J. Richardson, R. L. Urbanke
- **PDF**: https://ieeexplore.ieee.org/document/7115123
- **Abstract**: We establish the existence of wave-like solutions to spatially coupled graphical models which, in the large size limit, can be characterized by a 1-D real-valued state. This is extended to a proof of the threshold saturation phenomenon for all such models, which includes spatially coupled irregular low-density parity-check codes over the binary erasure channel (BEC), but also addresses hard-decision decoding for transmission over general channels, the code division multiple access problem, compressed sensing, and some statistical physics models. For traditional uncoupled iterative coding systems with two components and transmission over the BEC, the asymptotic convergence behavior is completely characterized by the EXIT curves of the components. In particular, the system converges to the desired fixed point, which is the one corresponding to perfect decoding, if and only if the two EXIT functions describing the components do not cross. For spatially coupled systems whose state is 1-D a closely related graphical criterion applies. Now the curves are allowed to cross, but not by too much. More precisely, we show that the threshold saturation phenomenon is related to the positivity of the (signed) area enclosed by two EXIT-like functions associated to the component systems, a very intuitive, and easy-to-use graphical characterization. In the spirit of EXIT functions and Gaussian approximations, we also show how to apply the technique to higher dimensional and even infinite-dimensional cases. In these scenarios, the method is no longer rigorous, but it typically gives accurate predictions. To demonstrate this application, we discuss transmission over general channels using both the belief-propagation as well as the min-sum decoder.

## Belief Propagation Algorithms on Noisy Hardware

- **Status**: ✅
- **Reason**: 노이즈 HW 상의 BP 알고리즘 robust 구현(censoring/averaging BP)+LDPC 디코더 적용 — 카테고리 C 이식 가능 BP 개선/노이즈 HW
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6981967
- **Type**: journal
- **Published**: 2015
- **Authors**: C. -H. Huang, Y. Li, L. Dolecek
- **PDF**: https://ieeexplore.ieee.org/document/6981967
- **Abstract**: The wide recognition that emerging nano-devices will be inherently unreliable motivates the evaluation of information processing algorithms running on noisy hardware as well as the design of robust schemes for reliable performance against hardware errors of varied characteristics. In this paper, we investigate the performance of a popular statistical inference algorithm, belief propagation (BP) on probabilistic graphical models, implemented on noisy hardware, and we propose two robust implementations of the BP algorithm targeting different computation noise distributions. We assume that the BP messages are subject to zero-mean transient additive computation noise. We focus on graphical models satisfying the contraction mapping condition that guarantees the convergence of the noise-free BP. We first upper bound the distances between the noisy BP messages and the fixed point of (noise-free) BP as a function of the iteration number. Next, we propose two implementations of BP, namely, censoring BP and averaging BP, that are robust to computation noise. Censoring BP rejects incorrect computations to keep the algorithm on the right track to convergence, while averaging BP takes the average of the messages in all iterations up to date to mitigate the effects of computation noise. Censoring BP works effectively when, with high probability, the computation noise is exactly zero, and averaging BP, although having a slightly larger overhead, works effectively for general zero-mean computation noise distributions. Sufficient conditions on the convergence of censoring BP and averaging BP are derived. Simulations on the Ising model demonstrate that the two proposed implementations successfully converge to the fixed point achieved by noise-free BP. Additionally, we apply averaging BP to a BP-based image denoising algorithm and as a BP decoder for LDPC codes. In the image denoising application, averaging BP successfully denoises an image even when nominal BP fails to do so in the presence of computation noise. In the BP LDPC decoder application, the power of averaging BP is manifested by the reduction in the residual error rates compared with the nominal BP decoder.

## Refined upper bounds on stopping redundancy of binary linear codes

- **Status**: ✅
- **Reason**: 이진 선형부호 stopping redundancy/패리티검사행렬 상계 개선 — stopping set은 LDPC BP 성능(error floor)과 직결, 코드설계(E) 이식 가능, 애매하면 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7133087
- **Type**: conference
- **Published**: 2015
- **Authors**: Y. Yakimenka, V. Skachek
- **PDF**: https://ieeexplore.ieee.org/document/7133087
- **Abstract**: The l-th stopping redundancy ρι(C) of the binary [n, k, d] code C, 1 ≤ l ≤ d, is defined as the minimum number of rows in the parity-check matrix of C, such that the smallest stopping set is of size at least l. The stopping redundancy ρ(C) is defined as ρd(C). In this work, we improve on the probabilistic analysis of stopping redundancy, proposed by Han, Siegel and Vardy, which yields the best bounds known today. In our approach, we judiciously select the first few rows in the parity-check matrix, and then continue with the probabilistic method. By using similar techniques, we improve also on the best known bounds on ρι(C), for 1 ≤ l ≤ d. Our approach is compared to the existing methods by numerical computations.

## Joint weighted bit-flipping decoder for use in diversity network coding

- **Status**: ✅
- **Reason**: weighted bit-flipping 디코더 변형(병렬 PWBF, 정보교환) — BP/BF 디코더 기법으로 이식 가능성(C), 애매하여 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7343279
- **Type**: conference
- **Published**: 2015
- **Authors**: H. King, M. F. Flanagan
- **PDF**: https://ieeexplore.ieee.org/document/7343279
- **Abstract**: A new joint message-passing decoder is presented for use in a two-user cooperative wireless network. This decoder is designed for use with the diversity network coding scheme of Xiao et al. , which uses nonbinary network codes together with channel coding to achieve high diversity gains. The proposed joint decoder, together with appropriate modifications to the cooperative protocol of Xiao and Skoglund (2010), significantly reduces the required implementation complexity both at the relay nodes and at the receiver. The destination's joint decoder structure consists of two parallel weighted bit flipping (PWBF) decoders which exchange extrinsic soft/hard information regarding the two users' packets. It is demonstrated through simulations that the proposed joint decoder achieves not only the same diversity gain as in the work of Xiao and Skoglund (2010), but also approximately 5dB of additional coding gain. It is also notable that a significant improvement in system performance can be achieved after only two joint decoding iterations.

## Iterative soft-decision decoding of Reed-Solomon codes using informed dynamic scheduling

- **Status**: ✅
- **Reason**: RS 부호용이나 패리티검사행렬 적응 + informed dynamic scheduling은 부호 비의존적 BP 기법으로 바이너리 LDPC BP에 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7282989
- **Type**: conference
- **Published**: 2015
- **Authors**: H. -C. Lee, G. -X. Huang, C. -H. Wang +1
- **PDF**: https://ieeexplore.ieee.org/document/7282989
- **Abstract**: In this paper, an iterative soft-decision decoding algorithm is proposed for Reed-Solomon (RS) codes. The proposed decoding algorithm combines the concepts of adapting the parity-check matrix and informed dynamic scheduling. Before each iteration, the parity-check matrix is re-arranged according to the reliability of the codeword bits, meaning that the influence of the least reliable variable nodes on the decoding process can be reduced. Consequently, the important decoding messages can be scheduled to be updated first, and the reliability of the least reliable bits can be enhanced. The simulation results show that the proposed decoding algorithm can provide significant improvement in the error-rate performance. By using the proposed algorithm, a gain of 0.5 dB can be achieved compared to the conventional adapting belief propagation algorithm.

## Anytime properties of protograph-based repeat-accumulate codes

- **Status**: ✅
- **Reason**: Protograph repeat-accumulate / SC-LDPCC binary LDPC code design with density-evolution and finite-length analysis (E).
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7360758
- **Type**: conference
- **Published**: 2015
- **Authors**: N. Zhang, M. Noor-A-Rahim, B. N. Vellambi +1
- **PDF**: https://ieeexplore.ieee.org/document/7360758
- **Abstract**: In this paper, a highly efficient protograph-based repeat-accumulate (P-RA) anytime code is proposed, which is derived from the combination of protograph-based low-density parity-check convolutional (P-LDPCC) and spatially coupled low-density parity-check convolutional (SC-LDPCC) codes. Density evolution technique is applied to demonstrate the anytime properties of the P-RA codes over the binary erasure channel (BEC). The simulation results show that P-RA codes perform better than SC-LDPCC and P-LDPCC codes. More importantly, the finite-length performance of P-RA codes is only dependent on the decoding delay rather than the decoding message position.

## CRC error correction for energy-constrained transmission

- **Status**: ✅
- **Reason**: CRC 고밀도 패리티검사에 BP/ADMM 반복디코딩 적용 — ADMM 디코더 기법은 부호 비의존적이며 바이너리 LDPC BP에 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7343337
- **Type**: conference
- **Published**: 2015
- **Authors**: E. Tsimbalo, X. Fafoutis, R. J. Piechocki
- **PDF**: https://ieeexplore.ieee.org/document/7343337
- **Abstract**: In this paper, we investigate the application of iterative decoding algorithms to error correction of cyclic redundancy check (CRC) codes widely used in low-energy communication standards. We consider the case when traditional error correction codes are not available due to energy constraints at the transmitter. Using the CRC-24 code adopted by the Bluetooth Low Energy standard as an example, we show how two iterative techniques traditionally used for decoding of low-density parity check codes - Belief Propagation (BP) and the Alternating Direction Method of Multipliers (ADMM) - can be applied to the high-density parity check matrix of the code. The performance of both techniques is evaluated through simulation, and it is demonstrated that a gain of up to 1.7 dB in terms of the SNR per bit and a total reduction of the packet error rate by more than 70% can be achieved compared with the non-correction scenario, at no extra cost for the transmitter. We also compare the two techniques and use the standard syndrome look-up method as a benchmark. Both schemes enable the correction of multiple errors, with the ADMM-based decoder demonstrating better overall performance than BP.

## Analysis and comparison of decoding algorithms on repeat accumulate code

- **Status**: ✅
- **Reason**: Tanner 그래프 기반 RA 부호 메시지패싱 디코딩 알고리즘 비교. BP 계열 디코더 기법으로 바이너리 LDPC BP에 이식 가능성 — 애매하므로 살림(C).
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7454080
- **Type**: conference
- **Published**: 2015
- **Authors**: Xueting Zeng, Jing He
- **PDF**: https://ieeexplore.ieee.org/document/7454080
- **Abstract**: This paper presents some decoding methods based on Tanner graph for the analysis of the repeat accumulate code which has been proved to be linear time encoding and linear time decoding. We study the structure of the repeat accumulate code and make a detail derivation of the procedure of these iterative algorithms. The extensive simulation results show that these efficient decoding methods based on the message passing algorithm are suitable for the repeat accumulate code both in performance and complexity.

## Reliability-Based ECC System for Adaptive Protection of NAND Flash Memories

- **Status**: ✅
- **Reason**: NAND 플래시 적응형 ECC 시스템(reliability map 기반 ECC 선택, UBER 최적화) — 카테고리 A 직접 해당
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7280050
- **Type**: conference
- **Published**: 2015
- **Authors**: L. Yuan, H. Liu, P. Jia +1
- **PDF**: https://ieeexplore.ieee.org/document/7280050
- **Abstract**: In order to make the implementation of the error correcting code(ECC) efficiently, it should be tailored individually to each block, and can be changed over time as the running condition changes. The combined effect of reliability factors makes it difficult to select ECC by considering the effect factors separately. So more appropriate ECC selection method need to be found. Meanwhile, most of the ECCs are designed to adapt to specific hardware, the implementation of the ECC needs to be redesigned when the hardware platform changes. So the introduction of commonly used ECC system can provide a great convenience for error correction. In this paper, we propose an easy-to-use and flexible ECC system which takes advantage of the reliability map to provide adaptive protection. Proposed ECC system comprises ECC selection module and ECC codec module. A method to select appropriate ECC based on reliability map which provides the evaluation of bit error rate is proposed in ECC selection module. ECC encoder and decoder suit are called in ECC codec module to provide various protection. Proposed system can be used in many platforms, such as DSP, ARM, etc. Compared with the early works, the uncorrectable bit error rate(UBER) performance, coding time and redundancy are all optimized by proposed ECC system.

## Hardware implementation of a real-time distributed video decoder

- **Status**: ✅
- **Reason**: LDPCA 디코더 포함한 90nm VLSI HW 아키텍처(soft input 계산 등), HW 병렬화 기법이 LDPC 디코더로 이식 가능성 있어 살림
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:7251957
- **Type**: conference
- **Published**: 2015
- **Authors**: H. -P. Yang, M. -H. Ho, H. -C. Hsieh +2
- **PDF**: https://ieeexplore.ieee.org/document/7251957
- **Abstract**: Distributed video coding (DVC), based on Slepian-Wolf Theorem and/or Wyner-Ziv Theorem, was proposed to apply for the situation with little encoding and big decoding. We design and implement a distributed video decoder which is majorly composed of low-density parity-check accumulate (LDPCA), correlation noise modeling, soft input computation, and side information creation. Our proposed DVC decoder architecture, implemented in TSMC 90nm GUTM process technology, can meet the requirement of decoding a QCIF video with a speed of 30fps. The maximum operating frequency of the designed chip is 100MHz, the chip area is 4.67 mm2, and the gate count is 690K.

## Understanding NAND’s Intrinsic Characteristics Critical Role in Solid State Drive (SSD) Design

- **Status**: ✅
- **Reason**: NAND 플래시 SSD 내재특성·flash error management — 카테고리 A(NAND/SSD 직접)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7150310
- **Type**: conference
- **Published**: 2015
- **Authors**: W. Akin
- **PDF**: https://ieeexplore.ieee.org/document/7150310
- **Abstract**: The use of NAND flash-based SSDs in enterprises has grown at a ~33% compound annual growth rate [1] worldwide for the past three years. The majority of the growth comes from enterprise data center applications where the trend is to leverage the cost benefits of using MLC and TLC NAND flash memory by focusing on the use model behavior to optimize performance and life characteristics. In the data center, requirements for these MLC/TLC SSDs demand high sequential performance and reliability, moderate IOPS, and low power consumption along with maintaining 3 to 5 years of useful life. These challenges are tackled by tightening the links between the SSD's operation, host operating environment, and intrinsic NAND memory behavior and by exploiting increasingly sophisticated controllers, firmware, and flash memory error management techniques.

## A novel evidence theory based row message passing algorithm for LDS systems

- **Status**: ✅
- **Reason**: New row message-passing scheduling (gradual APP update, turbo-effect) potentially transferable to LDPC BP scheduling; keep for Phase 3
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7341122
- **Type**: conference
- **Published**: 2015
- **Authors**: Y. Liu, J. Zhong, P. Xiao +1
- **PDF**: https://ieeexplore.ieee.org/document/7341122
- **Abstract**: The low density signature (LDS) technique which is able to support massive connectivity with non-orthogonal low density signatures is a promising multiple access (MA) scheme in future 5G systems. We firstly examine the theory of evidence to illustrate the weakness of the update rule for the message passing algorithm in LDS detection process. The combination results against the common sense (RACS) deteriorate the performance of LDS systems with high order modulation schemes considerably. To reduce the occurrence of the RACS, we propose a novel row message passing (RMP) algorithm by gradually updating the a posteriori probability (APP) messages of all variable nodes in each iteration. Hence, the RMP algorithm benefits from the turbo-effect on the rows of indicator matrix which results in fast convergence with moderate complexity. Simulations prove the reduction of iteration times and the effectiveness of the RMP algorithm for LDS systems with high order modulation schemes.

## Improved symbol-based belief propagation detection for large-scale MIMO

- **Status**: ✅
- **Reason**: MIMO용 실수영역/심볼기반 BP 검출기 — BP 메시지패싱 복잡도 저감 기법이 LDPC BP에 이식 가능성(C), 애매하여 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7345035
- **Type**: conference
- **Published**: 2015
- **Authors**: J. Yang, C. Zhang, X. Liang +2
- **PDF**: https://ieeexplore.ieee.org/document/7345035
- **Abstract**: In this paper, BP detection based on belief propagation in real domain for large-scale MIMO systems is proposed. Numerical results have shown that, with quadrature phase shift keying (QPSK) modulation, this approach can show 1 dB performance improvement at the BER of 10-2, compared to conventional single-edge based BP (SE-BP) in complex domain. Based on the proposed BP detection, its symbol-based variation is also investigated for applications in large-scale MIMO systems with a high-order modulation. This symbol-based method successfully reduces computational complexity by avoiding large dimensional matrix inversion and decomposition. Since the proposed method can also shrink the constellation size, its complexity can be further reduced. Numerical simulation results and complexity comparison have demonstrated that the proposed symbol-based BP detection can show advantages in both performance and complexity compared to existing ones. Therefore, it is suitable for large-scale MIMO system applications, especially for those with high-order modulations.

## Coding scheme for 3D vertical flash memory

- **Status**: ✅
- **Reason**: 3D 수직 플래시 메모리 fast detrapping/ICI 보상 코딩; NAND 플래시 직접(A)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7248332
- **Type**: conference
- **Published**: 2015
- **Authors**: Y. Kim, R. Mateescu, S. -H. Song +2
- **PDF**: https://ieeexplore.ieee.org/document/7248332
- **Abstract**: Recently introduced 3D vertical flash memory is expected to be a disruptive technology since it overcomes scaling challenges of conventional 2D planar flash memory by stacking up cells in the vertical direction. However, 3D vertical flash memory suffers from a new problem known as fast detrapping, which is a rapid charge loss problem. In this paper, we propose a scheme to compensate the effect of fast detrapping by intentional inter-cell interference (ICI). In order to properly control the intentional ICI, our scheme relies on a coding technique that incorporates the side information of fast detrapping during the encoding stage. This technique is closely connected to the well-known problem of coding in a memory with defective cells. Numerical results show that the proposed scheme can effectively address the problem of fast detrapping.

## Efficient Decoding of Short Length Linear Cyclic Codes

- **Status**: ✅
- **Reason**: 순환부호의 automorphism permutation을 BP에 통합해 수렴/성능 개선 — 부호 비의존적 BP 개선 기법(C)으로 바이너리 LDPC에 이식 가능성
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7009983
- **Type**: journal
- **Published**: 2015
- **Authors**: M. Ismail, S. Denic, J. Coon
- **PDF**: https://ieeexplore.ieee.org/document/7009983
- **Abstract**: Iterative soft decision decoding of linear block codes is a practical necessity when working with even modest block lengths. A number of algorithms have been proposed in the literature which use the permutation group of a code and the belief propagation (BP) algorithm for decoding. A novel soft-input, soft-output algorithm is presented that can be used for efficiently decoding of linear cyclic codes. Utilising the automorphism property of cyclic codes the permutation is incorporated into the belief propagation algorithm resulting in faster convergence and better error correcting performance. Performance of the new approach is analysed using a (63,45) BCH code and a (72,36) quadratic residue code. Simulation results show significant reduction in the average number of required decoding iterations and some improvement in error correcting performance over published algorithms.

## Polar Codes: Graph Representation and Duality

- **Status**: ✅
- **Reason**: polar code 4-cycle 제거 그래프표현으로 LDPC식 반복디코딩 — 부호 비의존 사이클제거→BP 개선, 예외 포함(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7154407
- **Type**: journal
- **Published**: 2015
- **Authors**: M. Fossorier
- **PDF**: https://ieeexplore.ieee.org/document/7154407
- **Abstract**: In this letter, we present an iterative method to obtain the representation of a polar code free of 4-cycles, as well as the properties of the dual of a polar code. Based on these results, iterative decoding of a polar code can be presented in the context of low-density parity check codes.

## Analysis and Design of Finite Alphabet Iterative Decoders Robust to Faulty Hardware

- **Status**: ✅
- **Reason**: faulty HW 견고한 FAID(유한알파벳 반복디코더) 설계 프레임워크 — 이식 가능 디코더 알고리즘(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7147804
- **Type**: journal
- **Published**: 2015
- **Authors**: E. Dupraz, D. Declercq, B. Vasić +1
- **PDF**: https://ieeexplore.ieee.org/document/7147804
- **Abstract**: This paper addresses the problem of designing low-density parity check decoders robust to transient errors introduced by faulty hardware. We assume that the faulty hardware introduces errors during the message-passing updates, and we propose a general framework for the definition of the message update faulty functions. Within this framework, we define symmetry conditions for the faulty functions and derive two simple error models used in the analysis. With this analysis, we propose a new interpretation of the functional density evolution threshold introduced by Kameni et al. in the recent literature and show its limitations in the case of highly unreliable hardware. However, we show that under restricted decoder noise conditions, the functional threshold can be used to predict the convergence behavior of finite alphabet iterative decoders (FAIDs) under faulty hardware. In particular, we reveal the existence of robust and nonrobust FAIDs and propose a framework for the design of robust decoders. We finally illustrate robust- and nonrobust-decoder behaviors of finite-length codes using Monte Carlo simulations.

## Spectrally-Efficient 400-Gb/s Single Carrier Transport Over 7 200 km

- **Status**: ✅
- **Reason**: SC-LDPC + decoder-aware degree optimization 사용; SC-LDPC 차수최적화 코드설계(E)로 이식 가능, 애매하므로 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7029062
- **Type**: journal
- **Published**: 2015
- **Authors**: R. Rios-Müller, J. Renaudier, P. Brindel +6
- **PDF**: https://ieeexplore.ieee.org/document/7029062
- **Abstract**: Since the advent of wavelength division multiplexed optical systems, increasing the bit rate per optical carrier has proved to be the most effective method to drive the overall cost of optical systems down. However, multicarrier approaches have gained momentum for 400-Gb/s transport to cope with bandwidth limitations of optoelectronic components. In this paper, single carrier modulated 400-Gb/s transport over transatlantic distances is demonstrated for the first time. Using high-speed digital-to-analog converters, we successfully generated a 64 GBaud dual-polarization signal modulated using 16-ary quadrature amplitude modulation. Thanks to Nyquist pulse shaping, our channels are closely packed with 66.7 and 75 GHz channel spacing, resulting on 6 and 5.33-bit/s/Hz of spectral efficiencies, respectively. Transceiver design is based on an optimization procedure of inter-symbol interference mitigation and forward error correction overhead. A spatially-coupled low density parity check code with decoder-aware degree optimization is used to reduce the gap to capacity. We validated our transceiver design by transporting five channels over 6600 and 7200-km with 6 and 5.33-bit/s/Hz of spectral efficiency, respectively. We analyze as well the performance gain provided by non-linear mitigation using filtered digital back-propagation algorithm.

## Quality-of-Service Implications of Enhanced Program Algorithms for Charge-Trapping NAND in Future Solid-State Drives

- **Status**: ✅
- **Reason**: 3D charge-trap NAND 신뢰성·read retry·ECC 시스템 영향 분석 — 카테고리 A 직접
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7130589
- **Type**: journal
- **Published**: 2015
- **Authors**: A. Grossi, L. Zuolo, F. Restuccia +2
- **PDF**: https://ieeexplore.ieee.org/document/7130589
- **Abstract**: Three-dimensional nand memory devices based on charge trapping (CT) technology represent the most promising solution for hyperscaled solid-state drives (SSDs). However, the intrinsic low reliability offered by that storage medium leads to a high number of errors requiring an extensive use of complex error correction codes (ECCs) and advanced read algorithms such as read retry. This materializes in an overall reduction in the SSD's QoS. In order to limit the error number, enhanced program algorithms that are able to improve the reliability figures of CT memory devices have been introduced. In this paper, the impact of such program algorithms combined with read retry and the ECC is experimentally characterized on CT- nand arrays. The results are then exploited for cosimulations at the system level, assessing the reliability, performance, and QoS of future SSDs integrating CT-based memory devices.

## Design Methodology for Highly Reliable, High Performance ReRAM and 3-Bit/Cell MLC NAND Flash Solid-State Storage

- **Status**: ✅
- **Reason**: 3bit/cell MLC NAND 플래시+ReRAM 신뢰성 설계(read-ref, ECC 오버헤드, RAID) — 카테고리 A NAND 직접
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6979273
- **Type**: journal
- **Published**: 2015
- **Authors**: S. Tanakamaru, H. Yamazawa, T. Tokutomi +2
- **PDF**: https://ieeexplore.ieee.org/document/6979273
- **Abstract**: This paper proposes design methodology for highly reliable, high performance ReRAM and 3-bit/cell multi-level cell (MLC) NAND flash solid-state storage. Six techniques, calibrated RRef (CR), flexible RRef (FR), adaptive asymmetric coding (AAC), verify trials reduction (VTR), bits/cell optimization (BCO), and balanced RAID-5/6 are proposed. CR, FR, AAC, and VTR are for ReRAM. CR and FR change the read-reference resistance (RRef) to reduce the BER. AAC first increases the population of Set and then Reset. The BER reduction with FR and AAC is 69 and 78% with 60 and 75% asymmetry, respectively. In VTR, by changing the number of acceptable bit-errors, the total Reset time is reduced by 97% at maximum with small ECC calculation overhead. The reliability of 3-bit/cell MLC NAND flash memory is improved by BCO and balanced RAID-5/6. BCO reallocates 3-bit/cell MLC to 2-bit/cell MLC and single-level cell (SLC) and the write/erase cycle increases by over 22-times. Balanced RAID-5/6 evenly allocates upper/middle/lower pages to a stripe to reduce the RAID failure rate by 98%.

## STRAUSS: Spectral Transform Use in Stochastic Circuit Synthesis

- **Status**: ✅
- **Reason**: 스토�스틱 컴퓨팅 회로 합성(STRAUSS)이 LDPC 디코딩에 응용된다고 명시, SC 기반 저면적 LDPC 디코더 HW 기법으로 이식 가능성 있어 애매하므로 살림
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:7105882
- **Type**: journal
- **Published**: 2015
- **Authors**: A. Alaghi, J. P. Hayes
- **PDF**: https://ieeexplore.ieee.org/document/7105882
- **Abstract**: Stochastic computing (SC) is an approximate computing technique that processes data in the form of long pseudorandom bit-streams which can be interpreted as probabilities. Its key advantages are low-complexity hardware and high-error tolerance. SC has recently been finding application in several important areas, including image processing, artificial neural networks, and low-density parity check decoding. Despite a long history, SC still lacks a comprehensive design methodology, so existing designs tend to be either ad hoc or based on specialized design methods. In this paper, we demonstrate a fundamental relation between stochastic circuits and spectral transforms. Based on this, we propose a general, transform-based approach to the analysis and synthesis of SC circuits. We implemented this approach in a program spectral transform use in stochastic circuit synthesis (STRAUSS), which also includes a method of optimizing stochastic number-generation circuitry. Finally, we show that the area cost of the circuits generated by STRAUSS is significantly smaller than that of previous work.

## Energy Consumption of VLSI Decoders

- **Status**: ✅
- **Reason**: VLSI 디코더 에너지 복잡도 이론 + LDPC 디코딩 회로 에너지 스케일링 예시 — D HW 관련, 애매하나 살림
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:7083760
- **Type**: journal
- **Published**: 2015
- **Authors**: C. G. Blake, F. R. Kschischang
- **PDF**: https://ieeexplore.ieee.org/document/7083760
- **Abstract**: Thompson’s model of very large scale integration computation relates the energy of a computation to the product of the circuit area and the number of clock cycles needed to carry out the computation. It is shown that for any sequence of increasing block-length decoder circuits implemented according to this model, if the probability of block error is asymptotically less than 1/2 then the energy of the computation scales at least as  $\Omega (n({\log n)^{1/2}})$ , and so the energy of decoding per bit must scale at least as  $\Omega ({\log n)^{1/2}}$ . This implies that the average energy per decoded bit must approach infinity for any sequence of decoders that approaches capacity. The analysis techniques used are then extended to show that for any sequence of increasing block-length serial decoders, if the asymptotic block error probability is less than 1/2 then the energy scales at least as fast as  $\Omega (n\log n)$ . In a very general case that allows for the number of output pins to vary with block length, it is shown that the energy must scale as  $\Omega (n(\log n)^{1/5})$ . A simple example is provided of a class of circuits performing low-density parity-check decoding whose energy complexity scales as  $O(n^{2} \log \log n)$ .

## Simplified Detection for DVB-NGH MIMO Decoders

- **Status**: ✅
- **Reason**: LLR용 유클리드거리 계산 HW 간소화(곱셈 제거)로 LDPC 입력 LLR 생성 — 면적 절감 HW 기법, 애매하나 살림(Phase3)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6983587
- **Type**: journal
- **Published**: 2015
- **Authors**: D. Perez-Calderon, V. Baena-Lecuyer, J. Chavez +2
- **PDF**: https://ieeexplore.ieee.org/document/6983587
- **Abstract**: Nowadays, communication systems need to satisfy very demanding constraints in order to cope with users new necessities. One of the most promising techniques to improve the system capacity is multiple input multiple output (MIMO). However, the use of MIMO implies a huge complexity increase in the detection process. In this paper, a method to reduce the aforementioned complexity is presented. Although the proposed method is analyzed for digital video broadcasting next generation for handhelds, its implementation is useful for any MIMO system that requires the computation of log likelihood ratios (LLRs), used by the low density parity check codes. The presented technique consists of applying a simplification when calculating the Euclidean distances needed by the LLRs. The simplification avoids almost all the multiplications, very area demanding when translated into hardware, and presents a performance loss under 0.1 dB.

## Spatially Coupled Soft-Decision Error Correction for Future Lightwave Systems

- **Status**: ✅
- **Reason**: 공간결합(SC) 바이너리 LDPC 신규 코드 클래스·degree distribution 설계 + FPGA 검증 — 카테고리 E/D 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6983533
- **Type**: journal
- **Published**: 1 March1, 
- **Authors**: Laurent Schmalen, Vahid Aref, Junho Cho +3
- **PDF**: https://ieeexplore.ieee.org/document/6983533
- **Abstract**: In this paper, we discuss and present some recent advances in the field of error correcting codes and discuss their applicability for lightwave transmission systems. We introduce several classes of spatially coupled codes and discuss several design options for spatially coupled codes and show how rapidly decodable codes can be constructed by careful selection of the degree distribution. We confirm the good performance of some spatially coupled codes at very low bit error rates using an FPGA-based simulation. Finally, we compare all proposed schemes and show how spatially coupled Low-Density Parity-Check (LDPC) codes outperform conventional LDPC and polar codes with similar receiver complexity and memory requirements.

## A Low-Complexity LDPC Coding Scheme for Channels With Phase Slips

- **Status**: ✅
- **Reason**: 신규 phase-slip transparent LDPC 구성(block symmetric codes), 바이너리 구성 제시 — 코드설계(E) 이식 가능성 애매하여 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6974985
- **Type**: journal
- **Published**: 1 April1, 
- **Authors**: Laurent Schmalen
- **PDF**: https://ieeexplore.ieee.org/document/6974985
- **Abstract**: We propose low-complexity coding schemes that are resilient against sporadic phase slip events. These schemes are based on a new phase-slip transparent construction of LDPC codes, called block symmetric codes and on outer differential coding. The slip transparent LDPC codes correct single bit error events but are transparent to phase slips. The phase slips, which correspond to runs of bit errors, are corrected by the outer coding part of the receiver. We present practical binary and nonbinary code constructions for multiple modulation formats, and evaluate the proposed scheme by means of simulation examples.

## Terminated and Tailbiting Spatially Coupled Codes With Optimized Bit Mappings for Spectrally Efficient Fiber-Optical Systems

- **Status**: ✅
- **Reason**: SC-LDPC(프로토그래프 바이너리) 비트매핑 최적화+density evolution 설계, 코드설계(E) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7005396
- **Type**: journal
- **Published**: 1 April1, 
- **Authors**: Christian Häger, Alexandre Graell i Amat, Fredrik Brännström +2
- **PDF**: https://ieeexplore.ieee.org/document/7005396
- **Abstract**: We study the design of spectrally efficient fiber-optical communication systems based on different spatially coupled (SC) forward error correction (FEC) schemes. In particular, we optimize the allocation of the coded bits from the FEC encoder to the modulation bits of the signal constellation. Two SC code classes are considered. The codes in the first class are protograph-based low-density parity-check (LDPC) codes which are decoded using iterative soft-decision decoding. The codes in the second class are generalized LDPC codes which are decoded using iterative hard-decision decoding. For both code classes, the bit allocation is optimized for the terminated and tailbiting SC cases based on a density evolution analysis. An optimized bit allocation can significantly improve the performance of tailbiting SC codes over the baseline sequential allocation, up to the point where they have a comparable gap to capacity as their terminated counterparts, at a lower FEC overhead. For the considered terminated SC codes, the optimization only results in marginal performance improvements, suggesting that in this case a sequential allocation is close to optimal.
