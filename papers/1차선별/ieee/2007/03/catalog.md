# IEEE Xplore — 2007-03 (1차선별 통과)


## Unequal Error Protection Using Partially Regular LDPC Codes

- **Status**: ✅
- **Reason**: UEP용 부분정규 LDPC 신규 구성+DE 최적화, 바이너리 LDPC 코드설계(E) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4133006
- **Type**: journal
- **Published**: March 2007
- **Authors**: Nazanin Rahnavard, Hossein Pishro-Nik, Faramarz Fekri
- **PDF**: https://ieeexplore.ieee.org/document/4133006
- **Abstract**: In this paper, we propose a scheme to construct low-density parity-check (LDPC) codes that are suitable for unequal error protection (UEP). We derive density evolution (DE) formulas for the proposed unequal error protecting LDPC ensembles over the binary erasure channel (BEC). Using the DE formulas, we optimize the codes. For the finite-length cases, we compare our codes with some other LDPC codes, the time-sharing method, and a previous work on UEP using LDPC codes. Simulation results indicate the superiority of the proposed design methodology for UEP

## Quasi-Cyclic LDPC Codes for the Magnetic Recording Channel: Code Design and VLSI Implementation

- **Status**: ✅
- **Reason**: 고율 QC-LDPC 코드 설계 가이드라인 + low error floor + QC-LDPC 디코더 VLSI 아키텍처 - 코드설계(E)+HW(D), 스토리지 채널
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4100818
- **Type**: journal
- **Published**: March 2007
- **Authors**: Hao Zhong, Tong Zhong, Erich F. Haratsch
- **PDF**: https://ieeexplore.ieee.org/document/4100818
- **Abstract**: By implementing a field-programmable gate array (FPGA)-based simulator, we investigate the performance of randomly constructed high-rate quasi-cyclic (QC) low-density parity-check (LDPC) codes for the magnetic recording channel at very low block sector error rates. On the basis of extensive simulations, we conjecture guidelines for designing randomly constructed high-rate regular QC-LDPC codes with low error floor for the magnetic recording channel. Experimental results show that our high-rate regular QC-LDPC codes do not suffer from error floor, at least at block error rates of 10-9, and can realize significant coding gains over Reed-Solomon codes that are used in current practice. Furthermore, we develop a QC-LDPC decoder hardware architecture that is well suited to achieving high decoding throughput. Finally, to evaluate the implementation feasibility of LDPC codes for the magnetic recording channel, using 0.13 mum standard cell and memory libraries, we designed a read channel signal processing datapath consisting of a parallel max-log-MAP detector and a QC-LDPC decoder, which can achieve a throughput up to 1.8 Gb/s

## TS-LDPC Codes: Turbo-Structured Codes With Large Girth

- **Status**: ✅
- **Reason**: TS-LDPC: 임의 girth를 보장하는 신규 바이너리 LDPC 구성 알고리즘+선형 인코딩, 코드설계(E) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4106128
- **Type**: journal
- **Published**: March 2007
- **Authors**: Jin Lu, Jos M. F. Moura
- **PDF**: https://ieeexplore.ieee.org/document/4106128
- **Abstract**: We consider turbo-structured low-density parity-check (TS-LDPC) codes-structured regular codes whose Tanner graph is composed of two trees connected by an interleaver. TS-LDPC codes with good girth properties are easy to construct: careful design of the interleaver component prevents short cycles of any desired length in its Tanner graph. We present algorithms to construct TS-LDPC codes with arbitrary column weight jges2 and row weight k and arbitrary girth g. We develop a linear complexity encoding algorithm for a type of TS-LDPC codes-encoding friendly TS-LDPC (EFTS-LDPC) codes. Simulation results demonstrate that the bit-error rate (BER) performance at low signal-to-noise ratio (SNR) is competitive with the error performance of random LDPC codes of the same size, with better error floor properties at high SNR

## Invariance Properties of Binary Linear Codes Over a Memoryless Channel With Discrete Input

- **Status**: ✅
- **Reason**: 이진 선형부호 LLR pdf 불변성/대칭성 - LLR 양자화/디코더 설계 이론 기반으로 이식 가능, 애매하면 in (Phase3 재검토)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4106107
- **Type**: journal
- **Published**: March 2007
- **Authors**: Ali Abedi, Amir K. Khandani
- **PDF**: https://ieeexplore.ieee.org/document/4106107
- **Abstract**: This work studies certain properties of the probability density function (pdf) of the bit log-likelihood ratio (LLR) for binary linear block codes over a memoryless channel with discrete input and discrete or continuous output. We prove that under a set of mild conditions, the pdf of the bit LLR of a specific bit position is independent of the transmitted codeword. It is also shown that the pdf of a given bit LLR when the corresponding bit takes the values of zero and one are symmetric with respect to each other (reflection of one another with respect to the vertical axis). For the case of channels with binary input, a sufficient condition for two bit positions to have the same pdf is presented.

## Gradient Projection Decoding of LDPC Codes

- **Status**: ✅
- **Reason**: Gradient Projection 디코딩: 패리티검사를 비선형함수로 재정식화한 신규 LDPC 디코더, 병렬·저지연 특성으로 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4133922
- **Type**: journal
- **Published**: March 2007
- **Authors**: Christos Kasparis, Barry G. Evans
- **PDF**: https://ieeexplore.ieee.org/document/4133922
- **Abstract**: A new practical method for decoding low-density parity check (LDPC) codes is presented. The followed approach involves reformulating the parity check equations using nonlinear functions of a specific form, defined over Rrho, where rho denotes the check node degree. By constraining the inputs to these functions in the closed convex subset [0,1]rho ("box" set) of Rrho, and also by exploiting their form, a multimodal objective function that entails the code constraints is formulated. The gradient projection algorithm is then used for searching for a valid codeword that lies in the vicinity of the channel observation. The computational complexity of the new decoding technique is practically sub-linearly dependent on the code's length, while processing on each variable node can be performed in parallel allowing very low decoding latencies. Simulation results show that convergence is achieved within 10 iterations, although some performance degradations relative to the belief propagation (BP) algorithm are observed

## Semi-random Construction of Rate-Compatible Low-Density Parity-Check Codes

- **Status**: ✅
- **Reason**: 새 semi-random rate-compatible LDPC 패리티검사행렬 구성(코드설계 E) - 바이너리 LDPC 구성 기법 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4138141
- **Type**: conference
- **Published**: 4-9 March 
- **Authors**: Liang Chen, Songyan Wu, Shijun Yan +3
- **PDF**: https://ieeexplore.ieee.org/document/4138141
- **Abstract**: This paper presents a semi-random construction of rate-compatible low-density parity-check (LDPC) codes. We analyze some crucial properties determining the performance of LDPC codes to direct our construction approach. The new parity-check matrices corresponding to lower-rate codes are generated by computer search which is subject to these important properties. The novel construction approach is flexible as we only add new rows with certain constraints to the original parity-check matrix. The simulation results demonstrate that rate-compatible LDPC codes based on this approach work quite well.

## Speculative Energy Scheduling for LDPC Decoding

- **Status**: ✅
- **Reason**: 수신프레임 분석으로 필요 반복수 추정→동적 주파수/전압 조정 저전력 디코더(D). 페이딩채널이나 기법 자체는 NAND 디코더에 이식 가능
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:4149015
- **Type**: conference
- **Published**: 26-28 Marc
- **Authors**: Weihuang Wang, Gwan Choi
- **PDF**: https://ieeexplore.ieee.org/document/4149015
- **Abstract**: This paper presents a low-power LDPC decoder design based on speculative scheduling of energy necessary to decode dynamically varying data frame in fading channels. The proposed scheme pre-analyzes each received data frame to estimate the maximum number of necessary iterations for the frame convergence. The results are then used to dynamically adjust decoder frequency and switch between multiple-voltage levels; thereby energy use is minimized. This is in contrast to the conventional fixed-iteration decoding schemes that operates at a fixed voltage level regardless the quality of data received. The result is a decoder implementation that provides a judicious trade-off between power consumption and coding gain

## Reduced-Complexity Decoding Algorithm for LDPC Codes for Practical Circuit Implementation in Optical Communications

- **Status**: ✅
- **Reason**: cyclic approximated delta-minimum 디코딩 알고리즘 + 3비트 소프트 양자화, 이식 가능 디코더(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4348865
- **Type**: conference
- **Published**: 25-29 Marc
- **Authors**: Yoshikuni Miyata, Rui Sakai, Wataru Matsumoto +2
- **PDF**: https://ieeexplore.ieee.org/document/4348865
- **Abstract**: For superior, practical decoding of LDPC based FEC, a cyclic approximated delta-minimum algorithm is proposed. Simulation shows that 3-bit soft-decision decoding provides a required Q of 6.2 dB at 10-6 BER with only 16 iterations.

## The Design of the Maximum-Likelihood Decoding Algorithm of LDPC Codes over BEG

- **Status**: ✅
- **Reason**: PEG-LDPC over BEC에 대한 개선된 ML 디코딩 알고리즘(C), 바이너리 LDPC 디코더 기여
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4298350
- **Type**: conference
- **Published**: 14-16 Marc
- **Authors**: Ki-Moon Lee, Hayder Radha
- **PDF**: https://ieeexplore.ieee.org/document/4298350
- **Abstract**: We improve the design of the maximum likelihood decoding algorithm (MLDA) for the development of LDPC codes. Furthermore, we apply the improved design to the decoding of progressive edge growth (PEG) LDPC codes over binary erasure channels (BEC). We also demonstrate clear improvements over current LDPC decoding algorithms.

## Arbitrary Bit Generation and Correction Technique for Encoding QC-LDPC Codes with Dual-Diagonal Parity Structure

- **Status**: ✅
- **Reason**: dual-diagonal QC-LDPC용 저복잡도 systematic 인코딩 기법; 바이너리 QC-LDPC 구성/인코더(D/E) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4224372
- **Type**: conference
- **Published**: 11-15 Marc
- **Authors**: Chanho Yoon, Eunyoung Choi, Minho Cheong +1
- **PDF**: https://ieeexplore.ieee.org/document/4224372
- **Abstract**: In this paper, we propose a simple yet low complex systematic LDPC encoding method for class of quasi-cyclic low-density parity-check (QC-LDPC) codes which have an efficient encoding/decoding algorithm due to the simple structure of their parity-check matrices. The proposed encoding method is applicable to parity-check matrices having dual-diagonal parity structure with single column of weight 3. Unlike finding a direct solution for parity bits in schemes (Richardson and Urbanke, 2001 and Classon and Blankeship, 2004), the proposed scheme first generates arbitrary parity bits. Then, given the parity bits for the first sub-block and exploiting the dual-diagonal structure, all parity bits are found through correction. With slight modification of parity-check matrix H, proposed LDPC encoding scheme is directly applicable to matrices defined in IEEE physical layer standards with almost negligible performance loss. Moreover, the overall computational complexity involving encoding process is lower than well-known Richardson's efficient encoding scheme (Richardson and Urbanke, 2001).

## A Perturbation Method for Decoding LDPC Concatenated with CRC

- **Status**: ✅
- **Reason**: LDPC-CRC perturbation 재디코딩으로 error floor 저감 — BP 개선 디코더 기법(C), CRC concat은 NAND에서 흔함
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4224373
- **Type**: conference
- **Published**: 11-15 Marc
- **Authors**: Dongliang Xiao, Jianhua Lu, Chunlei Lin +1
- **PDF**: https://ieeexplore.ieee.org/document/4224373
- **Abstract**: In this paper, a novel decoding algorithm using perturbation techniques for LDPC concatenated with CRC (LDPC-CRC) is proposed. The CRC is used to check the residual error of the BP algorithm, while a new parameter is introduced to LDPC decoding to describe the reliability of each bit in the iterative decoding algorithm. Upon an error is detected, re-decoding process with perturbation method will be aroused. Simulation results show that this method lowers the error floor for codeword length of several hundred bits effectively.

## A Modified PEG Algorithm for Construction of LDPC Codes with Strictly Concentrated Check-Node Degree Distributions

- **Status**: ✅
- **Reason**: PEG 변형으로 check-node degree 집중·girth 개선 — 바이너리 LDPC 코드설계(E) 신규 구성기법, 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4224354
- **Type**: conference
- **Published**: 11-15 Marc
- **Authors**: Hua Chen, Zhigang Cao
- **PDF**: https://ieeexplore.ieee.org/document/4224354
- **Abstract**: Progressive edge-growth (PEG) algorithm is a good approach to construct low-density parity-check (LDPC) codes with large girth at finite block lengths. However, the check-node degrees of PEG codes are usually loosely concentrated for both regular (more than one degree) and irregular codes (more than two degrees). In this paper, the authors propose a modified PEG algorithm for construction of LDPC codes with strictly concentrated check-node degrees, which yields both completely regular codes and strictly right-concentrated irregular codes with two consecutive check-node degrees. Moreover, our algorithm further improves the girth histogram of the codes for better performance. Simulation results show that even under strictly concentrated check-node degrees, our proposed algorithm slightly improves the performance of both regular and irregular PEG codes, especially for irregular codes at high SNR values.

## Analysis of Check-Node Merging Decoding for Punctured LDPC Codes with Dual-Diagonal Parity Structure

- **Status**: ✅
- **Reason**: punctured LDPC용 check-node merging 디코딩 — 연산 감소·수렴속도 향상 신규 디코더 기법(C), 바이너리 LDPC 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4224356
- **Type**: conference
- **Published**: 11-15 Marc
- **Authors**: Jung-Ae Kim, Sung-Rae Kim, Dong-Joon Shin +1
- **PDF**: https://ieeexplore.ieee.org/document/4224356
- **Abstract**: In this paper, the authors propose new decoding scheme of punctured LDPC codes with dual-diagonal parity structure by merging check nodes connected to the punctured parity nodes. This check-node merging decoding not only needs smaller number of operations at each iteration but also shows faster decoding convergence speed than the conventional erasure decoding. For the binary erasure channel (BEC) and AWGN channel, the authors analyze and compare the check-node merging and the conventional erasure decoding schemes of the punctured LDPC codes with dual-diagonal parity structure using density evolution. Analytical results show that the check-node merging decoding gives faster convergence speed for both BEC and AWGN channel. Also, simulation results are provided to confirm the analytical results.

## Greedy Check Allocation for Irregular LDPC Codes Optimization in Multicarrier Systems

- **Status**: ✅
- **Reason**: 불규칙 LDPC irregularity 프로파일 최적화 신규 greedy check allocation 구성법 — 코드설계 기법(E) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4224377
- **Type**: conference
- **Published**: 11-15 Marc
- **Authors**: Asad Mahmood, Emmanuel Jaffrot
- **PDF**: https://ieeexplore.ieee.org/document/4224377
- **Abstract**: The capacity approaching performances (Richardson et al., 2001) of different types of low density parity check (LDPC) codes have led them to undergo extensive research in recent years. Along with asymptotic performances analysis, the optimization of 'irregularity' profile for different channels and the performance analysis of practical finite-length codes has also been extensively explored. With multi-carrier communications becoming the physical layer choice for many emerging wireless systems, a feasible solution for optimizing the irregularity profile of irregular LDPC codes for a frequency selective channel is a problem of particular importance and interest. This paper proposes a simple-to-implement greedy 'check' allocation (GCA) based method for the construction of BER-optimized irregular LDPC codes using the criterion of Gallager upper bound (Gallager, 1962) for probabilistic decoding. A comparison of our GCA algorithm with some existing works (Mannoni et al., 2002) on the irregular LDPC codes optimization for multicarrier systems based on the classical Gaussian approximation of the 'density evolution' approach, shows that the same irregularity behavior can be achieved with a much simpler method.

## A Novel Scheme for Type-II Hybrid ARQ Protocols Using LDPC Codes

- **Status**: ✅
- **Reason**: rate-compatible LDPC용 PEG+zigzag 선형시간 인코딩 구성기법(E); HARQ는 응용이나 떼어낼 바이너리 LDPC 구성 있음
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4224376
- **Type**: conference
- **Published**: 11-15 Marc
- **Authors**: Liang Chen, Xiumin Shi, Shijun Yan +3
- **PDF**: https://ieeexplore.ieee.org/document/4224376
- **Abstract**: In this paper, we propose a novel type-II hybrid ARQ scheme using low density parity check (LDPC) codes. The proposed approach combines low hardware overhead with good decoding performance by using an efficient decoder operating at a much higher rate with a much smaller size parity check matrix. Our scheme makes parts of the previously received data gradually improved until successful decoding of the entire original codeword. We also present a novel efficient framework for constructing rate-compatible LDPC codes applied in our hybrid ARQ scheme. The progressive edge growth (PEG) construction method with zigzag pattern results in linear-time encoding.
