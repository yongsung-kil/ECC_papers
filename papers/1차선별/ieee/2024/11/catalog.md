# IEEE Xplore — 2024-11 (1차선별 통과)


## List-Based Optimization of Proximal Decoding for LDPC Codes

- **Status**: ✅
- **Reason**: LDPC proximal decoding 개선(oscillation 보정 + ML-in-the-list) - 새 디코더 알고리즘, 바이너리 LDPC에 이식 가능 (C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10677441
- **Type**: journal
- **Published**: Nov. 2024
- **Authors**: Andreas Tsouchlos, Holger Jäkel, Laurent Schmalen
- **PDF**: https://ieeexplore.ieee.org/document/10677441
- **Abstract**: In this letter, the proximal decoding algorithm is considered within the context of additive white Gaussian noise (AWGN) channels. An analysis of the convergence behavior of the algorithm shows that proximal decoding inherently enters an oscillating behavior of the estimate after a certain number of iterations. Due to this oscillation, frame errors arising during decoding can often be attributed to only a few remaining wrongly decoded bit positions. In this letter, an improvement of the proximal decoding algorithm is proposed by establishing an additional step, in which these erroneous positions are attempted to be corrected. We suggest an empirical rule with which the components most likely needing correction can be determined. Using this insight and performing a subsequent “ML-in-the-list” decoding, a gain of up to 1 dB is achieved compared to conventional proximal decoding, depending on the decoder parameters and the code.

## ECCPM: An Efficient Internal Data Migration Scheme for Flash Memory Systems

- **Status**: ✅
- **Reason**: 플래시 copyback 데이터 마이그레이션, RBER/디코딩 전 임계값 예측 모델 - NAND 직접(A)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10680162
- **Type**: journal
- **Published**: Nov. 2024
- **Authors**: Haihua Hu, Guojun Han, Wenhua Wu +2
- **PDF**: https://ieeexplore.ieee.org/document/10680162
- **Abstract**: The copyback command can be used to accelerate data migration in solid-state drives. However, the reliability of this command is not guaranteed, posing challenges for broad utilization within the consumer electronics device. The existing algorithms for predicting the copyback threshold do not consider two issues: 1) Due to page/wordline restrictions restrictions, the accumulation of errors across pages during copyback operations is asymmetrical; and 2) The controller lacks prior knowledge about the raw bit error rate (RBER) before decoding. As a result, it is impossible to predict the frequency of copyback command execution. In this paper, we explore the mathematical models of flash programs and read operations. We further develop the state transition probability matrix for wordline-level data migration within the same plane. Therefore, we propose a predictive model for the maximum copyback threshold within the same plane. To address these two issues, we conduct tests and analyse the characteristics of error accumulation in copyback using actual chips and substitute the relative entropy of the state distribution in our prediction model for RBER. By integrating these insights, we introduce an estimated copyback count prediction model (ECCPM). The simulation results demonstrate that the ECCPM can significantly reduce latency while minimally impacting write amplification.

## Energy-Efficient Channel Decoding for Wireless Federated Learning: Convergence Analysis and Adaptive Design

- **Status**: ✅
- **Reason**: FL 에너지효율 위해 채널 디코더 반복횟수 적응 조절 — 디코더 반복수 적응 제어는 LDPC BP/min-sum 조기종료로 이식 여지, 애매하여 살림(Phase3 재검토)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10669200
- **Type**: journal
- **Published**: Nov. 2024
- **Authors**: Linping Qu, Yuyi Mao, Shenghui Song +1
- **PDF**: https://ieeexplore.ieee.org/document/10669200
- **Abstract**: One of the most critical challenges for deploying distributed learning solutions, such as federated learning (FL), in wireless networks is the limited battery capacity of mobile clients. While it is a common belief that the major energy consumption of mobile clients comes from the uplink data transmission, this paper presents a novel finding, namely channel decoding also contributes significantly to the overall energy consumption of mobile clients in FL. Motivated by this new observation, we propose an energy-efficient adaptive channel decoding scheme that leverages the intrinsic robustness of FL to model errors. In particular, the robustness is exploited to reduce the energy consumption of channel decoders at mobile clients by adaptively adjusting the number of decoding iterations. We theoretically prove that wireless FL with communication errors can converge at the same rate as the case with error-free communication provided the bit error rate (BER) is properly constrained. An adaptive channel decoding scheme is then proposed to improve the energy efficiency of wireless FL systems. Experimental results demonstrate that the proposed method maintains the same learning accuracy while reducing the channel decoding energy consumption by  $\sim ~20$ % when compared to an existing approach.

## Low-Latency Parallel Row-Layered Min-sum MDPC Decoder for McEliece Cryptosystem

- **Status**: ✅
- **Reason**: row-layered Min-sum MDPC 디코더 저지연 병렬화 HW — Min-sum 변형·병렬 layered 스케줄·HW 아키텍처가 바이너리 LDPC 디코더로 이식 가능(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10768229
- **Type**: conference
- **Published**: 4-6 Nov. 2
- **Authors**: Jiaxuan Cai, Xinmiao Zhang
- **PDF**: https://ieeexplore.ieee.org/document/10768229
- **Abstract**: In the latest round of post-quantum cryptography standardization, the McEliece cryptosystem utilizing medium-density parity-check (MDPC) codes remains a candidate. The row-layered Min-sum decoding for MDPC codes has better tradeoff between performance and complexity. Previous work adds constraints to the parity-check matrix construction in order to enable efficient parallel decoding. However, the constraints for large parallelism cause an undesirable reduction in the number of usable secret keys and hence the previous scheme has limitations in achieving higher speed. This paper proposes two new schemes to substantially reduce the latency of row-layered MDPC decoding. Instead of further increasing the constraints to achieve higher parallelism, multiple identity blocks in the parity-check matrix are processed simultaneously in the first scheme and large blocks of variable width are processed in a hybrid way in the second design. Efficient hardware architectures are also developed for both proposed decoders. For an example code, the two proposed decoders achieve around 40% speedup compared to the best prior effort with less than 10% area overhead.

## LDPC Decoding Based on Hybrid Stochastic Computing

- **Status**: ✅
- **Reason**: 하이브리드 확률컴퓨팅 기반 OMS LDPC 디코더 — 바이너리 LDPC용 새 디코더/HW 구조(C/D), 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10874397
- **Type**: conference
- **Published**: 28-30 Nov.
- **Authors**: Yali Li, Zhisong Bie
- **PDF**: https://ieeexplore.ieee.org/document/10874397
- **Abstract**: Compared with traditional computing methods, stochastic computing (SC) is simpler in circuit implementation. The Belief Propagation (BP) or Min-Sum (MS) algorithms used in traditional Low Density Parity Check (LDPC) decoding require a large amount of circuits for the calculation of check nodes (CNs). In this paper, decoding is completed on a decoding structure that combines the advantages of the Offset Min-Sum (OMS) algorithm and SC. CN information is calculated in the probability domain, and variable node (VN) information is calculated in the Log Likelihood Ratio (LLR) domain. It is proposed to use the gold sequence combined with a synchronizer to generate a positively correlated sequence, and combine the Noise-Dependent Scaling (NDS) algorithm to obtain a positively correlated random number generator to complete the conversion from LLR to a positively correlated bit stream. The positively correlated bit stream is input into an AND gate to find the minimum value of the input bit streams. Simulation results show that the bit error rate curve of the proposed method is close to the OMS algorithm.

## Spectrum-Efficient LDPC Codes for CPM

- **Status**: ✅
- **Reason**: CPM용 protomatrix search+lifting 기반 QC-LDPC 새 구성법 제시(E) — EXIT 기반 설계 기법 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10773725
- **Type**: conference
- **Published**: 28 Oct.-1 
- **Authors**: Erik Perrins
- **PDF**: https://ieeexplore.ieee.org/document/10773725
- **Abstract**: Low density parity check (LDPC) codes received preliminary study in the early 2000s for use in aeronautical telemetry, which is an application domain that relies exclusively on continuous phase modulation (CPM) waveforms due to their power and spectrum efficiency under severe size, weight, and power (SWAP) constraints. The limited deployment of LDPC in telemetry has proved to be very successful, which has motivated interest in finding an LDPC solution with comprehensive applicability to all CPM waveforms used in the IRIG-106 telemetry standard. Such a solution, however, has proved to be elusive due to the "coded" nature of CPM itself and its nonlinear characteristics. In this paper, we lay out a design methodology that begins with an extrinsic information transfer (EXIT) characterization of CPM. We show how to incorporate these EXIT characteristics into a protomatrix search that optimizes the decoding threshold for a given CPM scheme. From there, we employ protomatrix lifting techniques to arrive at final quasi-cyclic LDPC codes with desired code rates and information block sizes. Our simulation results demonstrate performance around one dB from the respective waveform channel capacities with no error floors observed at error rates below 10−8. As such, these codes can be considered to fill in the options for LDPC codes that are currently absent in the IRIG-106 standard.

## Optimization of the iterative decoding algorithms for irregular block codes

- **Status**: ✅
- **Reason**: GDBF(gradient-descent bit flipping) 디코더 변형+유전알고리즘 파라미터 학습 신규 기여 - 이식 가능 디코더 알고리즘(C), BCH 대상이나 LDPC 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10819061
- **Type**: conference
- **Published**: 26-27 Nov.
- **Authors**: Jovan Milojkovic, Srdjan Brkić, Predrag Ivaniš +1
- **PDF**: https://ieeexplore.ieee.org/document/10819061
- **Abstract**: In this paper, we analyze the performances of iterative decoders for linear block codes. In particular, we consider two modifications of the gradient-descent bit flipping (GDBF) algorithm with momentum, where multiple component decoders with different momentum values are concatenated to improve the decoder performance. The learning parameters of the component decoders are obtained by using a Genetic algorithm based on the database of the uncorrectable error patterns of the previous decoder. We present three optimization strategies and provide a comparison with the state-of-the-art decoders. The numerical results are presented on short Bose-Chaudhuri-Hocquenghem (BCH) codes and the channel with additive white Gaussian noise (AWGN).

## Explicit Constructions of Girth-Eight QC-LDPC Codes: A Unified Framework Motivated by TDGS

- **Status**: ✅
- **Reason**: TDGS 기반 girth-8 QC-LDPC 새 구성 프레임워크(4/6-cycle 제거). 바이너리 QC-LDPC 코드 설계(E), 새 기여
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10806926
- **Type**: conference
- **Published**: 24-28 Nov.
- **Authors**: Guohua Zhang, Yulin Hu, Defeng Ren +1
- **PDF**: https://ieeexplore.ieee.org/document/10806926
- **Abstract**: A new search method named two-dimensional greedy search (TDGS) is proposed to progressively determine each element within an exponent matrix, so as to generate quasi-cyclic (QC) low-density parity-check (LDPC) codes without 4-cycles and 6-cycles. By applying four different two-dimensional scanning orders to the TDGS, a design framework is formulated to unify several existing and novel explicit constructions for short (3, $L$)-regular QC-LDPC codes without 4-cycles and 6-cycles. Through equivalence analysis between the exponent matrices greedily found by the TDGS and directly defined by explicit constructions, novel girth properties of (and connections between) these existing explicit constructions are also revealed.

## Theoretical Bounds for the Size of Elementary Trapping Sets by Graph Theory Methods

- **Status**: ✅
- **Reason**: 바이너리 LDPC ETS(error floor) 제거를 위한 새 Turán number 기반 이론적 bound와 Tanner graph 구성 — 코드 설계 기법(E), 새 기여
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10806922
- **Type**: conference
- **Published**: 24-28 Nov.
- **Authors**: Haoran Xiong, Zicheng Ye, Huazi Zhang +6
- **PDF**: https://ieeexplore.ieee.org/document/10806922
- **Abstract**: Elementary trapping sets (ETSs) are the principal culprits for the performance of LDPC codes in the error floor region. Due to their large quantity, intricate structures, and high computational complexity, determining how to eliminate dominant ETSs in the design of LDPC codes has become a critical issue in improving error floor behavior. In this paper, we address this problem by avoiding particular theta graphs $(\theta(1,2,2)$ and $\theta(2,2,2))$ in the Tanner graph to eliminate specific ETSs. These can be characterized by a pivotal tool in graph theory - Turán numbers. Theoretically, we derive the exact Turán number for $\theta(1,2,2)$ and demonstrate that all $(a, b)$-ETSs in a Tanner graph with variable-reaular degree $d_{L}(v)=\gamma$ must satisfy the inequality $b\geq a\gamma-\frac{1}{2}a^{2}$. This result improves the lower bound previously obtained by Amirzade when the girth is 6. For girth 8, by constraining the relationship between any two 8-cycles in the Tanner graph, we establish a similar inequality $b\geq a\gamma-\frac{a(\sqrt{8a-7}-1)}{2}$. Our simulation results indicate that codes designed with these considerations exhibit improved performance and a lower error floor over additive white Gaussian noise channels.

## Guessing what, Noise or Codeword?

- **Status**: ✅
- **Reason**: 바이너리 선형부호 ML 디코딩(GCD/GND)과 OSD 변형 제시 — 이식 가능 디코더 알고리즘(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10806987
- **Type**: conference
- **Published**: 24-28 Nov.
- **Authors**: Xiao Ma
- **PDF**: https://ieeexplore.ieee.org/document/10806987
- **Abstract**: In this paper, we distinguish two guessing algorithms for decoding binary linear codes. One is the guessing noise decoding (GND) algorithm, and the other is the guessing codeword decoding (GCD) algorithm. We prove that the GCD is a maximum likelihood (ML) decoding algorithm and that the GCD is more efficient than GND for most practical applications. We also introduce several variants of ordered statistic decoding (OSD) to trade off the complexity of the Gaussian elimination (GE) and that of the guessing, which may find applications in decoding short block codes in the high signal-to-noise ratio (SNR) region.

## A Regression-Based Optimal Scaling Factor Scheme for 5G LDPC Codes with MIMO Systems

- **Status**: ✅
- **Reason**: 회귀 기반 최적 스케일링 계수로 NMS 개선 — 이식 가능 디코더 알고리즘(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10892181
- **Type**: conference
- **Published**: 20-22 Nov.
- **Authors**: Madhavsingh Indoonundon, Tulsi Pawan Fowdur
- **PDF**: https://ieeexplore.ieee.org/document/10892181
- **Abstract**: Low-Density Parity Check (LDPC) codes are powerful forward error correction (FEC) codes which achieve near-channel capacity performances. They have been adopted in several technologies, such as WiFi and 5G NR, and there is active research on optimising both their encoding and decoding algorithms. This paper proposes a low-complexity regression-based optimal scaling factor (OSF) scheme to optimise the Normalized Min-Sum Algorithm (NMSA) performance in 5G NR with different Multiple-Input Multiple-Output (MIMO) configurations. The proposed scheme provides Eb/N0 gains in all tested scenarios, with the maximum achievable Eb/N0 gain being 1 dB when using the 8T2R MIMO configuration in the low BER range.

## High-Throughput LDPC Encoder/Decoder for Real-Time Coherent Optical Communications

- **Status**: ✅
- **Reason**: High-throughput LDPC encoder/decoder FPGA architecture — portable HW arch (D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:10809382
- **Type**: conference
- **Published**: 2-5 Nov. 2
- **Authors**: Kun Chen, Yanhao Chen, Qianwu Zhang +3
- **PDF**: https://ieeexplore.ieee.org/document/10809382
- **Abstract**: We demonstrate an LDPC encoder/decoder architecture with a maximum throughput of 2229 Mbps. Implemented on an FPGA, the receiver sensitivity achieves −56 dBm@2Gbps BPSK (decoded BER < 1E-7), with a decoding gain exceeding 8 dB.

## Designing Polar Code and LDPC Code for Reduction of Decoder Complexity

- **Status**: ✅
- **Reason**: Polar+LDPC code design to cut SD-FEC decoder complexity; borderline code-design (E), keep for Phase 3
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10809952
- **Type**: conference
- **Published**: 2-5 Nov. 2
- **Authors**: Zhiyuan Song, Koji Igarashi
- **PDF**: https://ieeexplore.ieee.org/document/10809952
- **Abstract**: We show a method for designing polar code and LDPC code to reduce the SD-FEC decoder complexity. The proposed method determines the appropriate LDPC code for polar encoder and estimates the BER performance.

## LVLDPC: Intra-Layer Variation Aware LDPC Coding for 3D TLC NAND Flash Memory

- **Status**: ✅
- **Reason**: A: 3D TLC NAND 층간변이 인지 LDPC 코딩(read-retry/반복횟수 저감), NAND 직접
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10818002
- **Type**: conference
- **Published**: 18-20 Nov.
- **Authors**: Lanlan Cui, Meng Zhang, Fei Wu
- **PDF**: https://ieeexplore.ieee.org/document/10818002
- **Abstract**: NAND flash memory employs high code rate low-density parity-check (LDPC) code to minimize redundant data. High code rates reduce redundancy but compromise error cor-rection compared to medium/low code rates. Raw bit error rate (RBER) varies among the storage layers for 3D triple-level cell (TLC) NAND flash memory, which causes the number of using read retry to increase. Repeatedly initiating read retry seriously increases the decoding latency and decreases the performance of the 3D TLC NAND flash memory. To alleviate this problem, this article proposes Intra-Layer Variation aware LDPC coding, called LVLDPC. The LVLDPC scheme categorizes RBER into distinct levels. Then, we select LDPC codes with appropriate error correction capabilities to decode data with varying levels of RBER. Through this scheme, we don't need to start read-retry when RBER $< 1.56\times 10^{-2}$. The iteration number is reduced by 67% in total. This scheme only causes 1.15 % space overhead, which is negliaible,

## HEncode: A Highly Modularized and Efficient FPGA QC-LDPC Encoder using High Level Synthesis

- **Status**: ✅
- **Reason**: D: HLS 기반 모듈화 FPGA QC-LDPC 인코더(스토리지 채널 대상), NAND HW 이식 가능
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:10818010
- **Type**: conference
- **Published**: 18-20 Nov.
- **Authors**: Jiawei Yang, Shaohua Wang, Xiangrui Yang +5
- **PDF**: https://ieeexplore.ieee.org/document/10818010
- **Abstract**: QC-LDPC (Quasi Cyclic Low-Density Parity-Check) codes, as a regular block-based code, have been preva-lently adopted in communication and storage fields to ensure high reliability and bandwidth of data channels. However, existing Field-Programmable Gate Array (FPGA) QC-LDPC encoders designed by RTL experts are generally dedicated to specialized LDPC codes and hardware platforms without flexibility and scalability. Recently, High-Level Synthesis (HLS) was introduced to compile a high-level encoding logic into Register Transfer Level (RTL) implementations, which are low performance and hardware efficiency due to the overlarge HLS-to-RTL design space, especially for large-scale FPGA hardware. This paper proposes a highly modularized and efficient FPGA QC-LDPC encoder, HEncoder, to fully leverage HLS to achieve high bandwidth, flexibility in both code parameters, and hardware efficiency. Firstly, HEncode presents an efficient Encode Block (EB) fully exploiting the FPGA LUT characteristic. Second, HEncode designs a low-level subword-encoding pipeline using multiple EBs and subword-parallel Encode Units (EU). Third, HEncoder designs an encode module with a pipelined data stream consecutively passing Input, EU array, and Output to balance bandwidths of accessing and encoding words. Finally, HEncode develops a design space analyzer to automatically determine the encoder parameters under constrained conditions to achieve high bandwidth. We implemented and evaluated HEncode on the Xilinx U50. The results show that compared to existing encoders, HEncode gains an increase of approximately 154.5× in the peak throughput and about 5.89 × in hardware efficiency to achieve the encoding throughput of 922.66 Gbps.

## Application of LDPC Codes in Digital Communication Systems for Robotic Systems

- **Status**: ✅
- **Reason**: 802.11n LDPC에 MinSum Normalized 정규화 계수 최적화 — min-sum 변형 이식 가능 디코더(C), 표준 부호지만 정규화 분석 기여
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10804986
- **Type**: conference
- **Published**: 15-17 Nov.
- **Authors**: Karen Grigoryan, Elena S. Basan, Ivan Polovko
- **PDF**: https://ieeexplore.ieee.org/document/10804986
- **Abstract**: The purpose of this article is to analyze the possibility of using low-density parity-check (LDPC) codes to create an information exchange system for robotic systems. The article discusses using of the Richardson- Urbanke coding method with the basic matrix of the 802.11n standard. Also, methods for decoding LDPC codes are considered. The article discusses the MinSum method, as well as a method for improving decoding results called MinSum Normalized. Research was conducted using modeling in the Python programming language to estimate the bit error rate (BER) indicator with different normalization coefficients to obtain a coefficient at which the bit error rate ratio will be minimal. Also, comparisons of the complexity of the MinSum and MinSum Normalized algorithms were presented. Normalized algorithm in particular can significantly reduce the number of errors when transmitting data over a noisy communication channel. The results obtained will be used to develop an information exchange system for robotic systems. The obtained results are planned to be used in the design of a receiving and transmitting device for information exchange in robotic systems.

## FPGA Implementation of QC-LDPC Decoder with Rapid Cyclic Shifter for CV-QKD Systems

- **Status**: ✅
- **Reason**: CV-QKD용이나 syndrome-based NMS + rapid cyclic shifter QC-LDPC FPGA 디코더 — 양자 전용 개념 비의존, 고전 바이너리 LDPC HW로 직접 이식 가능(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:10765523
- **Type**: conference
- **Published**: 13-15 Nov.
- **Authors**: Zeyuan Jin, Yinghua Xie, Xue-Qin Jiang +1
- **PDF**: https://ieeexplore.ieee.org/document/10765523
- **Abstract**: In continuous variable quantum key distribution (CV-QKD) systems, low-density parity check (LDPC) decoders have gained widespread adoption due to their robust error correction capabilities and good adaptability to parallel processing hardware designs. We introduce a syndrome-based normalized min-sum algorithm (S-NMSA) and implement the decoder on FPGAs for high throughput and minimal resource consumption. The decoder utilizes a semi-parallel architecture. The proposed rapid cyclic shifter (RCS) can complete the shift of any dimension matrix in one clock cycle and realizes a significant reduction in hardware resource consumption. The semi-parallel decoding structure attains a 68.5 Mbps processing throughput on the condition that the system clock of the quasi-cyclic (QC) LDPC decoder is 250 Mhz.

## Efficient FPGA Implementation of Syndrome-Assisted Layered Belief Propagation Decoder for CV-QKD Systems

- **Status**: ✅
- **Reason**: CV-QKD용이나 syndrome-assisted layered BP + 고정소수점 + 2-segment 비균일 LUT psi(x) + LS-ET 조기종료의 FPGA QC-LDPC 디코더 — 양자 전용 개념 비의존, 바이너리 LDPC 디코더/HW로 이식 가능(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10765534
- **Type**: conference
- **Published**: 13-15 Nov.
- **Authors**: Yong Chen, Xue-Qin Jiang, Genlong Chen +3
- **PDF**: https://ieeexplore.ieee.org/document/10765534
- **Abstract**: In this paper, we propose a QC-LDPC decoder architecture with low complexity as well as excellent decoding performance in CV-QKD systems, which employs the syndrome-assisted layered belief propagation decoding algorithm. To minimize the complexity of hardware implementation and resource consumption in iterative decoding, we use fixed-point numbers instead of floating-point numbers to update node messages. Additionally, two-segment nonuniform lookup tables are employed to implement $\psi(x)$ efficiently. Besides, the layered syndrome-assisted early termination (LS-ET) scheme is introduced, resulting in the reduction of the number of decoding iterations while maintaining superior frame error rate (FER) performance. The experimental results indicate that the QC-LDPC decoder implemented on an FPGA is capable of achieving throughput of 50.8 Mbps when the code length is 26112 and code rate is 22/68.

## Enhancing Proximal Decoding for LDPC Codes through Deep Unfolding

- **Status**: ✅
- **Reason**: C: deep unfolding 적용 proximal gradient 기반 LDPC 디코더 — 새 디코더 알고리즘, MIMO 응용이나 기법 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10858271
- **Type**: conference
- **Published**: 10-13 Nov.
- **Authors**: Asahi Ito, Lantian Wei, Tadashi Wadayama
- **PDF**: https://ieeexplore.ieee.org/document/10858271
- **Abstract**: This paper introduces a deep unfolding-assisted proximal decoding for low-density parity-check (LDPC) codes. Proximal decoding method is a decoding algorithm based on the proximal gradient method. Our proposal, deep unfolding-assisted proximal (DU-Proximal) decoding, is obtained by applying deep unfolding to the proximal decoding. We especially focus on the decoding performance in multiple-input multiple-output (MIMO) channels. In numerical experiments, we compare the error correcting capability of the proposed algorithm with the minimum mean squared error (MMSE) signal detection method, the tanh signal detection method, and the MMSE jointly with belief propagation (BP) algorithm for LDPC decoding. The experimental results demonstrate that parameter optimization via DU yields significant performance gains, especially at high signal-to-noise ratio levels.
