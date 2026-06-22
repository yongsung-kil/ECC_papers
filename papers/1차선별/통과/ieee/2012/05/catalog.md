# IEEE Xplore — 2012-05 (1차선별 통과)


## Cyclic and Quasi-Cyclic LDPC Codes on Constrained Parity-Check Matrices and Their Trapping Sets

- **Status**: ✅
- **Reason**: 바이너리 cyclic/QC-LDPC 구성+trapping set/error floor 분석(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6135499
- **Type**: journal
- **Published**: May 2012
- **Authors**: Qin Huang, Qiuju Diao, Shu Lin +1
- **PDF**: https://ieeexplore.ieee.org/document/6135499
- **Abstract**: This paper is concerned with construction and structural analysis of both cyclic and quasi-cyclic codes, particularly low-density parity-check (LDPC) codes. It consists of three parts. The first part shows that a cyclic code given by a parity-check matrix in circulant form can be decomposed into descendant cyclic and quasi-cyclic codes of various lengths and rates. Some fundamental structural properties of these descendant codes are developed, including the characterization of the roots of the generator polynomial of a cyclic descendant code. The second part of the paper shows that cyclic and quasi-cyclic descendant LDPC codes can be derived from cyclic finite-geometry LDPC codes using the results developed in the first part of the paper. This enlarges the repertoire of cyclic LDPC codes. The third part of the paper analyzes the trapping set structure of regular LDPC codes whose parity-check matrices satisfy a certain constraint on their rows and columns. Several classes of finite-geometry and finite-field cyclic and quasi-cyclic LDPC codes with large minimum distances are shown to have no harmful trapping sets of size smaller than their minimum distances. Consequently, their error-floor performances are dominated by their minimum distances.

## Design of Length-Compatible Low-Density Parity-Check Codes

- **Status**: ✅
- **Reason**: 바이너리 LDPC 길이호환 모체부호 설계 신규 알고리즘 — 코드설계 기법(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6168878
- **Type**: journal
- **Published**: May 2012
- **Authors**: Kyung-Joong Kim, Jin-Ho Chung, Kyeongcheol Yang
- **PDF**: https://ieeexplore.ieee.org/document/6168878
- **Abstract**: Length-compatible low-density parity-check (LC-LDPC) codes are a class of low-density parity-check (LDPC) codes which can support a wide range of lengths for a given rate. They may be obtained by applying shortening and puncturing schemes to good LDPC codes. However, this conventional approach does not always guarantee them to have a good performance because their degree distributions may be wildly varied. In this paper we propose a novel algorithm to generate a mother code for LC-LDPC codes of a given rate such that their degree distributions are almost the same as the degree distribution of the mother code. Numerical results show that LC-LDPC codes constructed by our approach perform much better than those by the conventional approach.

## On the Design of LDPC-Convolutional Ensembles Using the TEP Decoder

- **Status**: ✅
- **Reason**: BEC용 TEP 디코더로 BP 개선 + window-sliding로 latency 감소 — 부호 비의존 BP 개선 디코더 기법(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6168872
- **Type**: journal
- **Published**: May 2012
- **Authors**: Pablo M. Olmos, Luis Salamanca, Juan Jose Murillo-Fuentes +1
- **PDF**: https://ieeexplore.ieee.org/document/6168872
- **Abstract**: Low-density parity-check convolutional (LDPCC) codes asymptotically achieve channel capacity under belief propagation (BP) decoding. In this paper, we decode LDPCC codes using the Tree-Expectation Propagation (TEP) decoder, recently proposed as an alternative decoding method to the BP algorithm for the binary erasure channel (BEC). We show that, for LDPCC codes, the TEP decoder improves the BP solution with a comparable complexity or, alternatively, it allows using shorter codes to achieve similar error rates. We also propose a window-sliding scheme for the TEP decoder to reduce the decoding latency.

## On the Overflow Problem in Finite Precision Turbo Decoding Message Passing

- **Status**: ✅
- **Reason**: LDPC layered(TDMP) 디코더 유한정밀도 overflow 처리 HW 기법(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6168190
- **Type**: journal
- **Published**: May 2012
- **Authors**: Wojciech Sulek
- **PDF**: https://ieeexplore.ieee.org/document/6168190
- **Abstract**: Much attention has been paid recently to the so-called layered decoding of LDPC codes, also known as turbo-decoding message passing (TDMP). The TDMP algorithm for decoding LDPC codes is known to possess some desirable features, such as fast convergence speed, reduced memory requirements and reduced implementation complexity in comparison with standard two-phase message passing algorithm. In this paper we analyze an important issue connected with hardware implementation of TDMP algorithm, namely the finite precision representation of messages influence on the decoding performance. Constrained dynamic range of the finite precision representation of messages entails overflow errors. We present an analysis revealing that in the subsequent decoding iterations, the subtraction of non-overflowed intrinsic message from overflowed extrinsic message is a source of errors that have substantial impact on the decoding results. The analysis is confirmed by simulation results showing significant performance loss. However this performance loss can be almost completely eliminated with a basic modifications in the messages computation algorithm. Effectiveness of the presented modifications is confirmed by simulation results obtained with hardware TDMP decoder implementation that has been developed.

## Incremental Redundancy for LDPC Codes of 2nd Generation DVB Systems

- **Status**: ✅
- **Reason**: DVB LDPC를 점진 중복(IR)으로 확장하는 부호 설계 알고리즘+최적 차수열, 코드설계 기여 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6239927
- **Type**: conference
- **Published**: 6-9 May 20
- **Authors**: Nabil Sven Loghin, Makiko Kan, Jan Zollner
- **PDF**: https://ieeexplore.ieee.org/document/6239927
- **Abstract**: In 2nd generation Digital Video Broadcasting (DVB) systems, low-density parity-check codes (LDPCCs) are applied. In this paper, we propose extension of the standardized LDPCCs to allow for additional incremental redundancy (IR). Several use-cases of IR in broadcasting systems are outlined. We derive an algorithm to extend a given LDPCC with optimized degree sequences. The extended LDPCC yields both original codeword and additional IR. We suggest to transmit IR part at later instances as the standard LDPC codewords. If the receiver fails to decode the standard LDPCC, it can use in addition the IR part. However, in all other cases, the receiver can fall into sleep mode during transmission of IR, allowing for power saving. Examples are given to indicate both coding gain and power saving capabilities of IR.

## Factor Graph Based Joint Detection/Decoding for LDPC Coded Large-MIMO Systems

- **Status**: ✅
- **Reason**: factor graph 기반 LDPC 결합 검출/복호 메시지패싱; BP 기반 디코더 기법 이식 가능성
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6240094
- **Type**: conference
- **Published**: 6-9 May 20
- **Authors**: T. Lakshmi Narasimhan, A. Chockalingam, B. Sundar Rajan
- **PDF**: https://ieeexplore.ieee.org/document/6240094
- **Abstract**: In this paper, we employ message passing algorithms over graphical models to jointly detect and decode symbols transmitted over large multiple-input multiple-output (MIMO) channels with low density parity check (LDPC) coded bits. We adopt a factor graph based technique to integrate the detection and decoding operations. A Gaussian approximation of spatial interference is used for detection. This serves as a low complexity joint detection/decoding approach for large dimensional MIMO systems coded with LDPC codes of large block lengths. This joint processing achieves significantly better performance than the individual detection and decoding scheme.

## Shortening Design Time through Multiplatform Simulations with a Portable OpenCL Golden-model: The LDPC Decoder Case

- **Status**: ✅
- **Reason**: LDPC 디코더 시뮬레이션용 OpenCL→RTL 멀티플랫폼(CPU/GPU/FPGA) 설계흐름, bit width/데이터표현 탐색 - HW 설계공간 탐색 기법(D), 애매하나 살림
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:6239819
- **Type**: conference
- **Published**: 29 April-1
- **Authors**: G. Falcao, M. Owaida, D. Novo +6
- **PDF**: https://ieeexplore.ieee.org/document/6239819
- **Abstract**: Hardware designers and engineers typically need to explore a multi-parametric design space in order to find the best configuration for their designs using simulations that can take weeks to months to complete. For example, designers of special purpose chips need to explore parameters such as the optimal bit width and data representation. This is the case for the development of complex algorithms such as Low-Density Parity-Check (LDPC) decoders used in modern communication systems. Currently, high-performance computing offers a wide set of acceleration options, that range from multicore CPUs to graphics processing units (GPUs) and FPGAs. Depending on the simulation requirements, the ideal architecture to use can vary. In this paper we propose a new design flow based on Open CL, a unified multiplatform programming model, which accelerates LDPC decoding simulations, thereby significantly reducing architectural exploration and design time. Open CL-based parallel kernels are used without modifications or code tuning on multicore CPUs, GPUs and FPGAs. We use SOpen CL (Silicon to Open CL), a tool that automatically converts Open CL kernels to RTL for mapping the simulations into FPGAs. To the best of our knowledge, this is the first time that a single, unmodified Open CL code is used to target those three different platforms. We show that, depending on the design parameters to be explored in the simulation, on the dimension and phase of the design, the GPU or the FPGA may suit different purposes more conveniently, providing different acceleration factors. For example, although simulations can typically execute more than 3× faster on FPGAs than on GPUs, the overhead of circuit synthesis often outweighs the benefits of FPGA-accelerated execution.

## Absorbing sets of Fountain codes over noisy channels

- **Status**: ✅
- **Reason**: absorbing set/trapping set 기반 finite-length 디코더 설계 기법, Fountain 베이스이나 LDPC error-floor 분석 기법(E) 이식 여지로 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6221348
- **Type**: conference
- **Published**: 28-29 May 
- **Authors**: Seyed Masoud Mirrezaei, Karim Faez, Shahram Yousefi
- **PDF**: https://ieeexplore.ieee.org/document/6221348
- **Abstract**: Although error-prone patterns have been extensively studied for low-density parity-check (LDPC) codes, to the best of our knowledge, they have never been fully explored for Fountain codes. It is shown that dominant trapping sets of Fountain codes are the absorbing sets. They happen in the so-called error floor, corresponding to a significant flattening in the error probability curves. In this paper, we introduce the properties of these dominant trapping sets for Fountain codes. This definition of absorbing sets leads to better design of practical finite-length Fountain encoders and decoders.

## An effective puncturing algorithm for QC-LDPC codes with dual-diagonal structure

- **Status**: ✅
- **Reason**: QC-LDPC dual-diagonal puncturing 알고리즘(저차 VN 선택, 동일 검사식 회피)은 rate-compatible 코드설계 기법으로 이식 가능(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6314002
- **Type**: conference
- **Published**: 27-30 May 
- **Authors**: Xin Zhao, Lidong Zhu, Yantao Guo +1
- **PDF**: https://ieeexplore.ieee.org/document/6314002
- **Abstract**: Puncturing is an effective method to achieve rate compatible. However, the existing puncturing algorithms are complex and difficult to implement by hardware. This article researches on puncturing algorithm for QC-LDPC codes with dual-diagonal structure. Taking LDPC codes under IEEE802.16e standard as an example, this paper proposes a simple puncturing algorithm to achieve bit-rate compatible. Based on dual-diagonal structure, the puncturing algorithm chooses variable nodes with low degree for deletion and follows the rule that the deleted variable nodes should not be in the same calibration equation as far as possible. The simulation shows that the proposed puncturing algorithm is simple and effective, and the sub-codes obtained through the puncturing have better BER performance than that of random puncturing and order puncturing. In addition, because the puncturing matrix does not need to send to the receiver, it reduces a lot of overhead. Overall, the proposed puncturing algorithm is very practical to achieve rate compatible.

## Sub-Gaussian model based LDPC decoder for SαS noise channels

- **Status**: ✅
- **Reason**: SαS impulsive noise용 sub-Gaussian 모델 기반 저복잡도 LDPC soft 디코더 — 바이너리 LDPC 디코더 알고리즘(C), 비가우시안 LLR/마진 계산은 NAND impulsive-like 노이즈에 이식 검토 여지
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6263372
- **Type**: conference
- **Published**: 21-24 May 
- **Authors**: Iulian Topor, Mandar Chitre, Mehul Motani
- **PDF**: https://ieeexplore.ieee.org/document/6263372
- **Abstract**: OFDM communication through warm shallow water acoustic channel (WSWA) is affected by snapping shrimp noise. Due to its impulsive broadband nature, the snapping shrimp noise is able to affect a large number of OFDM sub-carriers at once. The effect on the sub-carriers can be modeled as a symmetric α-stable (SαS) noise vector with dependent components. Although the performance of the conventional LDPC soft decoder is poorer in non-Gaussian SαS noise than in Gaussian noise, the performance can be improved by employing the dependency between the noise components while decoding. The multivariate probability densities and marginals are required in the computation of symbol a posteriori probabilities. For binary codes, the complexity of the algorithm using marginals is O(2dN), where d is the number of dependent components and N is the length of the code. Practical implementation of a decoder employing dependency through marginals is infeasible for high number of dependent components. In order to address this problem we develop a lower complexity algorithm using the sub-Gaussian model of SαS vectors.

## Design and Application of dynamic coding in shallow water acoustic communications

- **Status**: ✅
- **Reason**: rate-compatible LDPC(RC-LDPC) 코드 설계 — 가변레이트 구성(E), 바이너리 LDPC; OFDM/SWA 응용이나 RC 구성 기법 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6263386
- **Type**: conference
- **Published**: 21-24 May 
- **Authors**: Yougan Chen, Xiaomei Xu, Lan Zhang +1
- **PDF**: https://ieeexplore.ieee.org/document/6263386
- **Abstract**: In fast temporal variations shallow water acoustic (SWA) channels, flexible channel coding rate should be desired in the design of practical error control SWA communication system. Herein, as one of the dynamic coding schemes, rate compatible LDPC (RC-LDPC) codes combing OFDM technique are proposed to improve the system reliability for SWA communications. Based on the automatic repeat request (ARQ) mechanism, the proposed SWA OFDM system consists of three important preprocessing: channel state information (CSI) estimator, signal-to-noise ratio (SNR) estimator and RC-LDPC pattern. The design of RC-LDPC codes and SWA channel profile are described. A look-up table (LUT) of RC-LDPC performances for ARQ-SWA system is built via statistical simulation test. For the proposed scheme, we define and derive the sensitivity to channel time variations and the effects of different performance target BER threshold, which are further confirmed via numerical results. It is shown that RC-LDPC codes have good performances with wide range of rates in SWA channels. Finally, coding rate distributions of RC-LDPC codes in different SNR at BER below 10-4 for Xiamen harbor SWA channel are investigated.

## Stochastic decoding for LDPC convolutional codes

- **Status**: ✅
- **Reason**: LDPC-CC stochastic 디코더+virtual edge 보상 아키텍처 — 바이너리 SC-LDPC 디코더 기법 이식 가능(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6271843
- **Type**: conference
- **Published**: 20-23 May 
- **Authors**: Xin-Ru Lee, Chih-Lung Chen, Hsie-Chia Chang +1
- **PDF**: https://ieeexplore.ieee.org/document/6271843
- **Abstract**: Among LDPC codes, LDPC convolutional codes (LDPC-CCs) seem to be more suitable for variable length applications. However, a LDPC-CC decoder is difficult to implement for its long latency and large storage usage. The stochastic computation makes the decoding of LDPC-CCs more efficient, but the boundary effect of sliding window causes poor performance. In this paper, a stochastic LDPC-CC decoder with virtual edge compensation as well as decoder architecture is presented. The simulation results based on (491, 3, 6) time-varying LDPC-CC show that under the same signal-to-noise ratio, our proposed decoder could achieve better performance, 60% less decoding latency and 40% storage reduction compared to log-BP decoder with 10 processors.

## A novel method of constructing Quasi-Cyclic RS-LDPC codes for 10GBASE-T Ethernet

- **Status**: ✅
- **Reason**: QC-RS-LDPC 구성+Banyan/QSN 스위치네트워크 HW 절감 — 바이너리 QC-LDPC 디코더 네트워크 기법 이식 가능(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:6271608
- **Type**: conference
- **Published**: 20-23 May 
- **Authors**: Seong-In Hwang, Hanho Lee, Shin-Il Lim
- **PDF**: https://ieeexplore.ieee.org/document/6271608
- **Abstract**: This paper presents a novel method of constructing of Quasi-Cyclic Reed-Solomon-based LDPC (QC-RS-LDPC) codes for the application of 10GBASE-T Ethernet. The proposed code construction method makes RS-LDPC codes to be quasi-cyclic codes without bit error rate performance degradation. Therefore, QC-RS-LDPC decoder using the proposed method can use Banyan network or QSN that are efficient switch networks for QC codes. For performance comparison, the switch networks have been implemented. The results show that the switch network using the proposed method requires less memory size than existing switch network like Benes network. Since the switch network optimized for QC codes reduces critical path delay, the clock speed of QC-RS-LDPC decoder can be improved. The proposed method is able to construct QC-RS-LDPC codes, which reduces hardware size and improves clock speed.

## Low-power LDPC decoding based on iteration prediction

- **Status**: ✅
- **Reason**: 반복횟수 예측 기반 저전력 LDPC 디코딩(전압 스케일링) — 바이너리 LDPC 디코더 저전력 기법 이식 가능(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6271960
- **Type**: conference
- **Published**: 20-23 May 
- **Authors**: Xinmiao Zhang, Fang Cai, C. J. Richard Shi
- **PDF**: https://ieeexplore.ieee.org/document/6271960
- **Abstract**: Low-density parity-check (LDPC) codes have very broad applications. Low-power LDPC decoder design is becoming increasingly important for wireless and other power-constraint systems. Compared to disabling or simplifying the decoder circuit, reducing the power supply voltage can bring more power reduction. Through predicting the number of iterations needed for convergence, this paper proposes to make full use of the time available for decoding and scale down the power supply voltage in the remaining decoding iterations. Novel iteration prediction schemes are developed. The proposed schemes require very small hardware overhead and do not lead to noticeable error-correcting performance loss. Compared to using the original supply voltage and powering off the decoder after convergence, the proposed schemes can bring 50% dynamic power reduction for an example LDPC code, and the power saving further increases with the signal-to-noise ratio.

## An LDPC decoding method for fault-tolerant digital logic

- **Status**: ✅
- **Reason**: 고장허용 디지털로직용 저복잡도 LDPC 디코딩 알고리즘+로직 구현 — 바이너리 디코더 알고리즘/HW 이식 가능(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6271956
- **Type**: conference
- **Published**: 20-23 May 
- **Authors**: Yangyang Tang, Chris Winstead, Emmanuel Boutillon +2
- **PDF**: https://ieeexplore.ieee.org/document/6271956
- **Abstract**: A decoding algorithm and logic implementation is proposed for fast, low-complexity error correction in environments with a high rate of transient faults as well as hard errors. The circuit is able to correct a single error in one clock cycle, making it suitable for mitigating faults in pipelined digital logic systems. The proposed method is also resilient against internal transient gate errors that may occur within the decoder itself. In the presence of a high input error rate (0.001) and high internal gate fault rate (10-5), the new decoding algorithm is able to reduce the error probability by two orders of magnitude. An asynchronous implementation is also presented for the new algorithm, which performs iterative error-correction with reduced latency compared to synchronous algorithms.

## A pure software ldpc decoder on a multi-core processor platform with reduced inter-processor communication cost

- **Status**: ✅
- **Reason**: 멀티코어 소프트웨어 LDPC 디코더 프로세서간 통신비용 절감 — 바이너리 LDPC 디코더 병렬화/매핑 기법 이식 가능(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:6271839
- **Type**: conference
- **Published**: 20-23 May 
- **Authors**: Yan Ying, Kaidi You, Liyang Zhou +4
- **PDF**: https://ieeexplore.ieee.org/document/6271839
- **Abstract**: As an error correction code, Low Density Parity Check (LDPC) code has been widely used in various communication standards such as WiMAX and DVB-S2. But these continuously-evolving communication standards and the high development cost and low-flexibility of hardwired ASIC solutions have pushed LDPC researchers to turn to more cost-efficient and flexible implementation, and thus the multi-core processor based implementation of LDPC decoder is gaining increasing attention in the last few years. However, the performance of the multi-core processor based implementation is far below the hardwired ASICs, with one of the key reasons that the cost of communication between processors is very high. Three approaches are proposed in this paper to reduce the communication cost, including: optimized algorithm partitioning to reduce communication traffic, utilizing imbalanced communication between tasks to optimize mapping and reduce overall communication distance, and simplified data sending-receiving mechanism to reduce the cost of identifying received data. By using these approaches, the communication time of the proposed implementation of LDPC decoder only accounts for 12.2% of total decoding time, which generally occupies 50% decoding time in the previously reported LDPC decoders on multi-core processors. And our work can achieve better throughput performance under the same hardware condition compared with other state-of-the-art works.

## Improved hard-decision decoding LDPC Codec IP design

- **Status**: ✅
- **Reason**: NAND 플래시 컨트롤러용 LDPC 코덱 HW 구현(면적효율 인코더, column-by-column 디코더)으로 A/D 직접 해당
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6272052
- **Type**: conference
- **Published**: 20-23 May 
- **Authors**: Daehyun Kim, Biwoong Chung, Roy E. Kim
- **PDF**: https://ieeexplore.ieee.org/document/6272052
- **Abstract**: This paper presents an area efficient low density parity check (LDPC) encoder/decoder (Codec) implementation which can deliver high throughput performance and error correction capability for flash memory controller. In order to reduce the size of memory to store variable node LLR values, flooding schedule with column-by-column decoding architecture is exploited for the decoder. The encoder architecture provides area efficient encoding by using the specially designed H-matrix structure. The LDPC Codec IP is implemented with 700Kgates of 45nm standard CMOS technology of Samsung ASIC library and can support decoding data of 400MB/s from NAND flash without compromising the error correction capability up to raw bit-error-rate (BER) range of 2.5E-3 by hard-decision decoding mode.

## Design and research of improved algorithm decoder of LDPC code

- **Status**: ✅
- **Reason**: 확장형 저장어레이/주소제어 기반 개선 LDPC HW 디코더 아키텍처(D) - 이식 가능
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:6273344
- **Type**: conference
- **Published**: 18-20 May 
- **Authors**: Qing-gang Meng, Teng-yu Liu
- **PDF**: https://ieeexplore.ieee.org/document/6273344
- **Abstract**: Through researching the structural characteristics of LDPC parity matrix and algorithm data flow features of LDPC code, an improved type of algorithm decoder of LDPC code is designed in this paper. The decoder includes expandable storage array, exquisite address-controlling unit and powerful sequential state-controlling machine. It possesses the advantages of expanding the decoding code length flexibly and lower complexity for hardware realizing and higher hardware resource utilization rate. After constructing communication system and testing the performance of hardware decoder, the results showed that the performance of the decoder and the theory simulation value can fit each other perfectly. The correctness of the design is proved. The decoder which is designed in this paper can provide valuable reference for the development of general chips for LDPC decoder.

## Improved Gradient Descent Bit Flipping algorithms for LDPC decoding

- **Status**: ✅
- **Reason**: 신뢰도비 기반 적응임계 Gradient Descent Bit-Flipping LDPC 디코더 변형(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6215420
- **Type**: conference
- **Published**: 16-18 May 
- **Authors**: Tharathorn Phromsa-ard, Jiratchaporn Arpornsiripat, Jutaphet Wetcharungsri +3
- **PDF**: https://ieeexplore.ieee.org/document/6215420
- **Abstract**: For LDPC decoding, a class of weighted bit-flipping algorithms is much simpler than a belief propagation algorithm. This work proposes a modified Gradient Descent Bit-Flipping algorithm based on Reliability Ratio with an adaptive threshold to address trade-off between performance and latency. From numerical results, the proposed algorithm achieves lower latency without an expense of performance. It yields average iteration reduction of 15-27% over SNR range from 2.5 dB to 4.5 dB. In addition, it provides better decoding performance gains, i.e. 0.05-0.25 dB over low-to-medium SNR range between 1.5 dB and 4 dB comparing to previous schemes.
