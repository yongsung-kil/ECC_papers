# IEEE Xplore — 2007-11 (1차선별 통과)


## On the Construction of Quasi-Systematic Block-Circulant LDPC Codes

- **Status**: ✅
- **Reason**: 준-시스테매틱 블록순환 QC-LDPC 신규 구성, 저복잡 인코딩—바이너리 코드설계 (E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4381377
- **Type**: journal
- **Published**: November 2
- **Authors**: Ying Xu, Guo Wei
- **PDF**: https://ieeexplore.ieee.org/document/4381377
- **Abstract**: A class of quasi-systematic block-circulant LDPC (QSBC-LDPC) Codes is proposed. The parity-check matrix of a QSBC-LDPC code is a sparse block-circulant matrix with a quasi-systematic structure. Due to the special structure of the parity-check matrix, only limited memories, XOR computations and cyclic-shifting operations are needed in the recursive encoding process of the QSBC-LDPC codes. Simulations show that the QSBC-LDPC codes provide remarkable performance improvement with low encoding complexity.

## Efficient Puncturing Method for Rate-Compatible Low-Density Parity-Check Codes

- **Status**: ✅
- **Reason**: 레이트호환 LDPC 효율적 펑처링 기법, stopping set 회피 cost function—신규 코드설계 (E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4381399
- **Type**: journal
- **Published**: November 2
- **Authors**: Hyo Yol Park, Jae Won Kang, Kwang Soon Kim +1
- **PDF**: https://ieeexplore.ieee.org/document/4381399
- **Abstract**: In this paper, we propose an efficient puncturing method for LDPC codes. The proposed algorithm provides the order of variable nodes for puncturing based on the proposed cost function. The proposed cost function tries to maximize the minimum reliability among those provided from all check nodes. Also, it tries to allocate survived check nodes evenly to all punctured variable nodes. Furthermore, the proposed algorithm prevents the formation of a stopping set from the punctured variable nodes even when the amount of puncturing is quite large. Simulation results show that the proposed punctured LDPC codes perform better than existing punctured LDPC codes.

## The Development of Turbo and LDPC Codes for Deep-Space Applications

- **Status**: ✅
- **Reason**: 프로토그래프+circulant 기반 LDPC 구성, 디코딩 threshold 분석·그래프 루프 회피, HW 인코더/디코더 구현. 이식 가능 코드설계(E)/HW(D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4383367
- **Type**: journal
- **Published**: Nov. 2007
- **Authors**: Kenneth S. Andrews, Dariush Divsalar, Sam Dolinar +3
- **PDF**: https://ieeexplore.ieee.org/document/4383367
- **Abstract**: The development of error-correcting codes has been closely coupled with deep-space exploration since the early days of both. Since the discovery of turbo codes in 1993, the research community has invested a great deal of work on modern iteratively decoded codes, and naturally NASA's Jet Propulsion Laboratory (JPL) has been very much involved. This paper describes the research, design, implementation, and standardization work that has taken place at JPL for both turbo and low-density parity-check (LDPC) codes. Turbo code development proceeded from theoretical analyses of polynomial selection, weight distributions imposed by interleaver designs, decoder error floors, and iterative decoding thresholds. A family of turbo codes was standardized and implemented and is currently in use by several spacecraft. JPL's LDPC codes are built from protographs and circulants, selected by analyses of decoding thresholds and methods to avoid loops in the code graph. LDPC encoders and decoders have been implemented in hardware for planned spacecraft, and standardization is under way.

## Efficient Serial Message-Passing Schedules for LDPC Decoding

- **Status**: ✅
- **Reason**: LDPC 디코딩 serial(layered) message-passing 스케줄 이론분석, 수렴속도 2배; NAND 디코더 직결 핵심 기법 (C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4373433
- **Type**: journal
- **Published**: Nov. 2007
- **Authors**: Eran Sharon, Simon Litsyn, Jacob Goldberger
- **PDF**: https://ieeexplore.ieee.org/document/4373433
- **Abstract**: Conventionally, in each low-density parity-check (LDPC) decoding iteration all the variable nodes and subsequently all the check nodes send messages to their neighbors (flooding schedule). An alternative, more efficient, approach is to update the nodes' messages serially (serial schedule). A theoretical analysis of serial message passing decoding schedules is presented. In particular, the evolution of the computation tree under serial scheduling is analyzed. It shows that the tree grows twice as fast in comparison to the flooding schedule's one, indicating that the serial schedule propagates information twice as fast in the code's underlying graph. Furthermore, an asymptotic analysis of the serial schedule's convergence rate is done using the density evolution (DE) algorithm. Applied to various ensembles of LDPC codes, it shows that for long codes the serial schedule is expected to converge in half the number of iterations compared to the standard flooding schedule, when working near the ensemble's threshold. This observation is generally proved for the binary erasure channel (BEC) under some natural assumptions. Finally, an accompanying concentration theorem is proved.

## Generic Description and Synthesis of LDPC Decoders

- **Status**: ✅
- **Reason**: LDPC 디코더 아키텍처 일반 프레임워크 및 비-flooding 스케줄용 generic 아키텍처 합성, HW 아키텍처 직결 (D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:4383290
- **Type**: journal
- **Published**: Nov. 2007
- **Authors**: FrÉdÉric Guilloud, Emmanuel Boutillon, Jacky Tousch +1
- **PDF**: https://ieeexplore.ieee.org/document/4383290
- **Abstract**: Through a rapid survey of the architecture of low-density parity-check (LDPC) decoders, this paper proposes a general framework to describe and compare the LDPC decoder architectures. A set of parameters makes it possible to classify the scheduling of iterative decoders, memory organization, and type of check-node processors and variable-node processors. Using the proposed framework, an efficient generic architecture for nonflooding schedules is also given.

## An Information Theoretical Framework for Analysis and Design of Nanoscale Fault-Tolerant Memories Based on Low-Density Parity-Check Codes

- **Status**: ✅
- **Reason**: LDPC 기반 fault-tolerant 메모리 분석/설계 프레임워크, faulty Gallager B 디코딩 등 메모리 ECC 직결 기법 (B/C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4358596
- **Type**: journal
- **Published**: Nov. 2007
- **Authors**: Bane Vasic, Shashi Kiran Chilappagari
- **PDF**: https://ieeexplore.ieee.org/document/4358596
- **Abstract**: In this paper, we develop a theoretical framework for the analysis and design of fault-tolerant memory architectures. Our approach is a modification of the method developed by Taylor and refined by Kuznetsov. Taylor and Kuznetsov (TK) showed that memory systems have nonzero computational (storage) capacity, i.e., the redundancy necessary to ensure reliability grows asymptotically linearly with the memory size. The restoration phase in the TK method is based on low-density parity-check codes which can be decoded using low complexity decoders. The equivalence of the restoration phase in the TK method and faulty Gallager B algorithm enabled us to establish a theoretical framework for solving problems in reliable storage on unreliable media using the large body of knowledge in codes on graphs and iterative decoding gained in the past decade.

## Pseudocodewords of Tanner Graphs

- **Status**: ✅
- **Reason**: Tanner 그래프 pseudocodeword 분석으로 min-sum 디코딩 문제 그래프 구조 식별 및 좋은 min pseudocodeword weight 설계법, 코드설계/디코더 직결 (C/E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4373411
- **Type**: journal
- **Published**: Nov. 2007
- **Authors**: Christine A. Kelley, Deepak Sridhara
- **PDF**: https://ieeexplore.ieee.org/document/4373411
- **Abstract**: This paper presents a detailed analysis of pseudocodewords of Tanner graphs. Pseudocodewords arising on the iterative decoder's computation tree are distinguished from pseudocodewords arising on finite degree lifts. Lower bounds on the minimum pseudocodeword weight are presented for the BEC, BSC, and AWGN channel. Some structural properties of pseudocodewords are examined, and pseudocodewords and graph properties that are potentially problematic with min-sum iterative decoding are identified. An upper bound on the minimum degree lift needed to realize a particular irreducible lift-realizable pseudocodeword is given in terms of its maximal component, and it is shown that all irreducible lift-realizable pseudocodewords have components upper bounded by a finite value $t$ that is dependent on the graph structure. Examples and different Tanner graph representations of individual codes are examined and the resulting pseudocodeword distributions and iterative decoding performances are analyzed. The results obtained provide some insights in relating the structure of the Tanner graph to the pseudocodeword distribution and suggest ways of designing Tanner graphs with good minimum pseudocodeword weight.

## Iterative List Decoding of Some LDPC Codes

- **Status**: ✅
- **Reason**: LDPC 반복 list decoding 알고리즘 + list bit-flipping 디코딩, 부호 비의존 이식 가능 디코더 기법 (C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4373410
- **Type**: journal
- **Published**: Nov. 2007
- **Authors**: JØrn Justesen, Tom Hoholdt, Johann Hjaltason
- **PDF**: https://ieeexplore.ieee.org/document/4373410
- **Abstract**: We present an iterative list decoding algorithm for low-density parity-check (LDPC) codes. In particular we apply this decoder to a class of LDPC codes from finite geometries and show that the (73,45,10) projective geometry code can be maximum-likelihood (ML) decoded with low complexity. Moreover, the list decoding approach enables us to give a theoretical analysis of the performance. We also consider list bit-flipping (BF) decoding of longer LDPC codes.

## Turbo Decoding on the Binary Erasure Channel: Finite-Length Analysis and Turbo Stopping Sets

- **Status**: ✅
- **Reason**: BEC stopping set은 LDPC BP에서 유래; turbo 부호지만 LDPC stopping set 개념 확장이라 유한길이 분석 이식성 있음, 애매하여 in으로 살림 (Phase3 재검토)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4373428
- **Type**: journal
- **Published**: Nov. 2007
- **Authors**: Eirik Rosnes, Oyvind Ytrehus
- **PDF**: https://ieeexplore.ieee.org/document/4373428
- **Abstract**: This paper is devoted to the finite-length analysis of turbo decoding over the binary erasure channel (BEC). The performance of iterative belief-propagation decoding of low-density parity-check (LDPC) codes over the BEC can be characterized in terms of stopping sets. We describe turbo decoding on the BEC which is simpler than turbo decoding on other channels. We then adapt the concept of stopping sets to turbo decoding and state an exact condition for decoding failure. Apply turbo decoding until the transmitted codeword has been recovered, or the decoder fails to progress further. Then the set of erased positions that will remain when the decoder stops is equal to the unique maximum-size turbo stopping set which is also a subset of the set of erased positions. Furthermore, we present some improvements of the basic turbo decoding algorithm on the BEC. The proposed improved turbo decoding algorithm has substantially better error performance as illustrated by the given simulation results. Finally, we give an expression for the turbo stopping set size enumerating function under the uniform interleaver assumption, and an efficient enumeration algorithm of small-size turbo stopping sets for a particular interleaver. The solution is based on the algorithm proposed by Garello et al. in 2001 to compute an exhaustive list of all low-weight codewords in a turbo code.

## A solution for memory collision in semi-parallel FPGA-based LDPC decoder design

- **Status**: ✅
- **Reason**: semi-parallel FPGA LDPC 디코더의 메모리 충돌 해결 위한 새 코드 구조 - HW 아키텍처(D) 이식 가능
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:4487366
- **Type**: conference
- **Published**: 4-7 Nov. 2
- **Authors**: Radivoje Zarubica, Stephen G. Wilson
- **PDF**: https://ieeexplore.ieee.org/document/4487366
- **Abstract**: Low Density Parity Check (LDPC) decoders implementing long blocklength codes require semi-parallel design. One challenge when implementing these codes on Field Programmable Gate Arrays (FPGAs) is efficiently storing messages needed in the iteration process. To meet this challenge, a new class of LDPC codes is presented. They combine regularity of implementation with reduction of time needed for decoding process, and do not suffer of any significant performance loss due to their structure.

## Efficient check node update implementation for normalized min-sum algorithm

- **Status**: ✅
- **Reason**: Normalized min-sum CNU의 새 m-to-2m HW 구현으로 곱셈 연산 감소 — 이식 가능 디코더/HW(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4429021
- **Type**: conference
- **Published**: 30 Oct.-2 
- **Authors**: Lu Xin, Liang Yongsheng, Xu Jun
- **PDF**: https://ieeexplore.ieee.org/document/4429021
- **Abstract**: This paper has presented various min-sum related LDPC decoding algorithms and their typical hardware architectures of check node update in the scenario of parallel implementation. The m-to-2m decoder has been introduced to generate more efficient new hardware implementations of check node update, which can obviously reduce the number of multiplication operations for normalized min-sum algorithm for high rate LDPC codes. Simulations have claimed the performance of normalized min-sum is nearly the same as that of Log-BP, namely the optimal algorithm. In general, this paper has proved that normalized min-sum is good choices as LDPC decoding methods.

## Protograph LDPC Codes Design Based on EXIT Analysis

- **Status**: ✅
- **Reason**: protograph/multi-edge type LDPC용 신규 EXIT 분석 기반 코드설계 기법, 바이너리 LDPC 구성에 이식 가능(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4411526
- **Type**: conference
- **Published**: 26-30 Nov.
- **Authors**: Gianluigi Liva, Marco Chiani
- **PDF**: https://ieeexplore.ieee.org/document/4411526
- **Abstract**: In this paper, a novel extrinsic information transfer (EXIT) analysis is presented for protograph-based and multi- edge type low-density parity-check (LDPC) codes. A protograph defines a subset of an LDPCC ensemble (identified by the degree distributions of the bipartite graph), introducing further constraints about the edge connections. For many codes belonging to this class, the conventional approach based on EXIT charts cannot be applied. The proposed EXIT analysis takes into account edge connections, permitting the decoding convergence evaluation for protograph-based LDPC codes, allowing the design of highly-structured capacity approaching LDPC codes.

## A Bit-Node Centric Architecture for Low-Density Parity-Check Decoders

- **Status**: ✅
- **Reason**: bit-node centric LDPC 디코더 HW 아키텍처(메모리 절감 sum-product), NAND 디코더에 이식 가능(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:4410967
- **Type**: conference
- **Published**: 26-30 Nov.
- **Authors**: Ruwan N. S. Ratnayake, Erich F. Haratsch, Gu-Yeon Wei
- **PDF**: https://ieeexplore.ieee.org/document/4410967
- **Abstract**: A bit-node centric decoder architecture for low- density parity-check codes is proposed. This architecture performs the optimum sum-product algorithm. A bit node processing unit computes the bit-to-check node messages sequentially, while the computation of the check-to-bit node messages is broken up into several steps. A stand-alone decoder architecture, and a decoder architecture for a concatenated detector-decoder system are presented. The proposed stand-alone decoder architecture requires significantly less memory compared to other known serial architectures. The hardware requirements are reduced even further for the concatenated detector-decoder system.

## A Differential Binary Message-Passing LDPC Decoder

- **Status**: ✅
- **Reason**: 신규 binary message-passing LDPC 디코더, 저메모리·고속·SNR추정 불필요 - 이식 가능 디코더(C), NAND 적합
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4411210
- **Type**: conference
- **Published**: 26-30 Nov.
- **Authors**: Nastaran Mobini, Amir H. Banihashemi, Saied Hemati
- **PDF**: https://ieeexplore.ieee.org/document/4411210
- **Abstract**: In this paper, we propose a binary message-passing algorithm for decoding low-density parity-check (LDPC) codes. The algorithm substantially improves the performance of purely hard-decision iterative algorithms with a small increase in the memory requirements and the computational complexity. We associate a reliability value to each nonzero element of the code's parity-check matrix, and differentially modify this value in each iteration based on the sum of the extrinsic binary messages from the check nodes. For the tested random and finite-geometry LDPC codes, the proposed algorithm can achieve performance as close as 1.3 dB and 0.7 dB to that of belief propagation (BP) at the error rates of interest, respectively. This is while, unlike BP, the algorithm does not require the estimation of channel signal to noise ratio. Low memory and computational requirements and binary message-passing make the proposed algorithm attractive for high-speed low-power applications.

## Flexible Parallel Architecture for DVB-S2 LDPC Decoders

- **Status**: ✅
- **Reason**: DVB-S2 LDPC용 M-kernel 병렬 디코더의 임의 M인자 분할 HW 기법, NAND LDPC 디코더 병렬화에 이식 가능(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:4411529
- **Type**: conference
- **Published**: 26-30 Nov.
- **Authors**: Marco Gomes, Gabriel Falcao, Vitor Silva +3
- **PDF**: https://ieeexplore.ieee.org/document/4411529
- **Abstract**: State-of-the-art decoders for Low-Density Parity-Check (LDPQ codes adopted by the DVB-S2 standard, explore the periodicity M = 360 features of the selected special LDPC- IRA codes. This paper addresses the generalization of a well known M-kernel parallel hardware structure and proposes an efficient partitioning by any factor of M, without memory addressing overhead and keeping unchanged the efficient message mapping scheme. The method provides a simple and efficient way to reduce the decoder complexity. Synthesizing the proposed decoder architecture for N = {45,90,180} parallel processing units using an FPGA family from Xilinx shows a minimum throughput above the minimal 90 Mbps.

## Deterministic Design of Low-Density Parity-Check Codes for Binary Erasure Channels

- **Status**: ✅
- **Reason**: 불규칙 LDPC 결정론적 설계법(BEC), 빠른 코드설계 기법(E) - 애매하나 신규 구성기법으로 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4411211
- **Type**: conference
- **Published**: 26-30 Nov.
- **Authors**: Hamid Saeedi, Amir H. Banihashemi
- **PDF**: https://ieeexplore.ieee.org/document/4411211
- **Abstract**: We propose a deterministic method to design irregular Low-Density Parity-Check (LDPC) codes for binary erasure channels. Compared to the existing methods, which are based on the application of asymptomatic analysis tools such as density evolution or Extrinsic Information Transfer (EXIT) charts in an optimization process, the proposed method is much simpler and faster. Through a number of examples, we demonstrate that the codes designed by the proposed method perform very closely to the best codes designed by optimization. It can also be proved that, the proposed code ensembles are capacity-achieving and are thus asymptotically optimal.

## Multi-Gbps FPGA-Based Low Density Parity Check (LDPC) Decoder Design

- **Status**: ✅
- **Reason**: FPGA 완전병렬 LDPC 디코더 + 무오버헤드 modified min-sum, 이식 가능 HW(D)·디코더(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4411018
- **Type**: conference
- **Published**: 26-30 Nov.
- **Authors**: Radivoje Zarubica, Stephen G. Wilson, Eric Hall
- **PDF**: https://ieeexplore.ieee.org/document/4411018
- **Abstract**: A novel high-throughput (6 Gb/s), fully-parallel FPGA-based 1200-bit rate-1/2 Low Density Parity Check (LDPC) decoder design is presented. The decoder features a PEG- based regular (6,3) code and a modified min-sum algorithm that improves performance without any additional hardware overhead.

## A Scalable Decoder Architecture for IEEE 802.11n LDPC Codes

- **Status**: ✅
- **Reason**: 802.11n LDPC layered 디코더 확장형 클러스터 아키텍처+iteration latency 최적화, NAND HW에 이식 가능(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:4411530
- **Type**: conference
- **Published**: 26-30 Nov.
- **Authors**: Massimo Rovini, Giuseppe Gentile, Francesco Rossi +1
- **PDF**: https://ieeexplore.ieee.org/document/4411530
- **Abstract**: This paper describes a scalable IP of a decoder for LDPC codes compliant to IEEE 802.1 In and running the well- known layered decoding algorithm. The decoder architecture is arranged in clusters of serial processing units, which are configurable to process all the codes in the standard and, at the same time, to support multiple frame decoding. An optimization methodology of the iteration latency is also described, which relates to the order of the messages updated by the processors, as well as to the sequence of layers the decoder goes through. The logic synthesis on 65 nm CMOS technology with low- power standard-cell library, shows that the proposed design is suitable for portable devices, the throughput ranging from 180 to 410 Mbps, and the power consumption being below 235 mW.

## Design of High-Rate QC-LDPC Encoder/Decoder for Microwave Radio Systems

- **Status**: ✅
- **Reason**: QC-LDPC용 신규 shift-register-based min-sum(SRMS) 디코더 아키텍처+VLSI 구현, NAND LDPC HW에 이식 가능(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:4411246
- **Type**: conference
- **Published**: 26-30 Nov.
- **Authors**: Norifumi Kamiya, Eisaku Sasaki
- **PDF**: https://ieeexplore.ieee.org/document/4411246
- **Abstract**: A novel decoder architecture is presented for quasi- cyclic low-density parity-check (QC-LDPC) codes. The architecture implements a min-sum algorithm and uses feedback shift-registers to store all the messages exchanged within the algorithm. This shift-register-based min-sum (SRMS) decoder does not require complex interconnections between processors and registers and is amenable to a simple, high throughput hardware implementation. A codec with the SRMS decoder for high-rate codes of length 4095 bits has been fabricated with a 0.15 mum, 1.5 V CMOS technology. The decoder has a gate count of 693 K gates and achieves a throughput of 155.52 Mbps (STM-1) using high-order QAM schemes. Measurement results show that a microwave radio system employing this LDPC codec exhibits good error performance.

## Error Floor Estimation of Long LDPC Codes on Partial Response Channels

- **Status**: ✅
- **Reason**: QC-LDPC error floor 추정(trapping set 기반, FPGA 시뮬), 스토리지 채널 error floor 기법으로 NAND에 이식 가능(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4410966
- **Type**: conference
- **Published**: 26-30 Nov.
- **Authors**: Xinde Hu, B. V. K. Vijaya Kumar, Zongwang Li +1
- **PDF**: https://ieeexplore.ieee.org/document/4410966
- **Abstract**: The presence of error floor in low density parity check (LDPC) codes is of great concern for potential applications of LDPC codes to data storage channels, which require the error correcting code (ECC) to maintain the near-capacity error correcting performance at frame error rate as low as 10-12. In order to investigate the error floor of LDPC codes under partial response channels used in data storage systems, we propose a new estimation method combining analytical tools and simulation, based on the concept of trapping sets. The definition of trapping sets is based on the dominant error patterns observed in the decoding process. The goal is to accurately estimate the error rate in the error floor region for certain types of LDPC codes under the partial response channel and further extend the frame error rate down to 10-14 or lower. Towards this goal, we first use field programmable gate array (FPGA) hardware simulation to find the trapping sets that cause the decoding failure in the error floor region. For each trapping set, we extract the parameters which are key to the decoding failure rate caused by this trapping set. Then we use a much simpler in situ hardware simulation with these parameters to obtain the conditional decoding failure rate. By considering all the trapping sets we find, we obtain the overall frame error rate in the error floor region. The estimation results for a length -4623 QC-LDPC code under the EPR4 channel are within 0.3 dB of the direct simulation results. In addition, this method allows us to estimate the frame error rate of a LDPC code down to 10-14 or lower.

## Improving BER Performance of LDPC Codes based on Intermediate Decoding Results

- **Status**: ✅
- **Reason**: BP 중간 반복결과(failed parity-check 추적)로 BER 개선하는 신규 디코더 수정 — 부호 비의존 BP 개선(C)으로 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4728627
- **Type**: conference
- **Published**: 24-27 Nov.
- **Authors**: Esa Alghonaim, Mohamed Adnan Landolsi, Aiman El-Maleh
- **PDF**: https://ieeexplore.ieee.org/document/4728627
- **Abstract**: The paper presents a novel approach to reduce the bit error rate (BER) in iterative belief propagation (BP) decoding of low density parity check (LDPC) codes. The behavior of the BP algorithm is first investigated as a function of number of decoder iterations, and it is shown that typical uncorrected error patterns can be classified into 3 categories: oscillating, nearly-constant, or random-like, with a predominance of oscillating patterns at high Signal-to-Noise (SNR) values. A proposed decoder modification is then introduced based on tracking the number of failed parity check equations in the intermediate decoding iterations, rather than relying on the final decoder output (after reaching the maximum number of iterations). Simulation results with a rate ¿ (1024,512) progressive edge-growth (PEG) LDPC code show that the proposed modification can decrease the BER by as much as 10-to-40%, particularly for high SNR values.

## Construction of Regular and Irregular LDPC Codes using (n, {k1, k2}, 1) Block Design

- **Status**: ✅
- **Reason**: block design 기반 규칙/불규칙 LDPC 구성, girth≥6·short cycle 분석 + 저복잡도 인코더/디코더 — 바이너리 LDPC 코드설계(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4728629
- **Type**: conference
- **Published**: 24-27 Nov.
- **Authors**: Siddarama R. Patil, Sant S. Pathak
- **PDF**: https://ieeexplore.ieee.org/document/4728629
- **Abstract**: In this paper, we construct regular and irregular LDPC codes using (n, {k 1, k 2}, 1)block design. The problem of designing regular and irregular structured LDPC codes that have good overall error performance for wide range of code rates and block sizes with attractive storage requirements is attempted. The codes constructed by this method have the girth at least 6 and they perform well with the sum-product iterative decoding algorithm. Further we analyze the constructed codes based on number of short cycles of the corresponding Tanner graph. The analysis shows that codes having small number of short cycles and a cycle structure which is not overly regular in their Tanner graph perform better. The presented codes are well structured and unlike random codes can lend themselves to a very low-complexity encoder and decoder implementation.

## Parallel Computing Platform for Evaluating LDPC Codes Performance

- **Status**: ✅
- **Reason**: LDPC 성능평가용 분산 병렬 시뮬레이션 플랫폼 — 디코더 알고리즘/구성 기여는 아니나 검증 인프라로 애매, 살려서 Phase3 재검토
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:4728279
- **Type**: conference
- **Published**: 24-27 Nov.
- **Authors**: Esa Alghonaim, Aiman El-Maleh, Adnan Al-Andalusi
- **PDF**: https://ieeexplore.ieee.org/document/4728279
- **Abstract**: This paper presents a novel approach for the design and implementation of a simulation platform for evaluating LDPC codes performance. The existing LDPC code simulation tools consume very long time in evaluating the performance of a specific code design. This is due to the intensive number of required computations. This problem is overcome by developing a parallel protocol to distribute the computations among processing nodes in a TCP/IP network. As indicated by experimental results, the proposed simulation platform is scalable with the number of processing nodes. Another practical advantage of the proposed system is that it does not need dedicated processors to run it; rather, it can utilize idle times of processing nodes in a network and work transparent to a node user. Furthermore, network daemons are used to utilize network nodes even if they are in the log-off state.

## Programmable LDPC Decoder for Wireless Network

- **Status**: ✅
- **Reason**: 부분병렬 LDPC 디코더 HW에 Benes network 적용해 가변 패리티검사·다중 코드레이트 지원, permutation network 기법 이식 가능(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:4410628
- **Type**: conference
- **Published**: 23-24 Nov.
- **Authors**: Hye-Jin Ryu, Jong Yeol Lee
- **PDF**: https://ieeexplore.ieee.org/document/4410628
- **Abstract**: Low density parity check (LDPC) code is adopted to high quality satellite broadcast standard in Europe and having been given attention to channel coding of mobile communication due to its high performance. Partially parallel decoding architecture uses less size of the chip. In this paper, we combined the partially parallel architecture with Benes network and implemented LDPC decoder which reduces size of interconnection and supports variable parity-check matrices. The proposed architecture supports multiple code rates and moderate codeword lengths.

## Two-Stage Hybrid decoding for Low-Density Parity-Check codes

- **Status**: ✅
- **Reason**: LDPC 신규 하이브리드 디코딩(soft+hard 혼합)으로 오류성능·지연 트레이드오프, 이식 가능 디코더 알고리즘(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4430491
- **Type**: conference
- **Published**: 18-20 Nov.
- **Authors**: Hany R. Zeidan, Maha M. Elsabrouty
- **PDF**: https://ieeexplore.ieee.org/document/4430491
- **Abstract**: Low-density parity check (LDPC) codes are gaining increased attention in information theory field. However one of the main problems facing usage of these codes in communication systems is its high complexity decoding scheme that results in high decoding delay. Such a delay is not acceptable in many applications. This paper presents, a new hybrid decoding scheme. The proposed scheme mixes between soft-decision and hard-decision algorithms and provides a good trade off between error performance and decoding delay as proved by simulation results.
