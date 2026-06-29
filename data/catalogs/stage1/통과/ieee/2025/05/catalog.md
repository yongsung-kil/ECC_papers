# IEEE Xplore — 2025-05 (1차선별 통과)


## Ternary Message Passing Decoding of High-Rate Regular LDPC Codes

- **Status**: ✅
- **Reason**: 스토리지용 고률 정규 LDPC 대상 3진 메시지 패싱 디코더로 밀도 진화 기반 파라미터 최적화 — 스토리지 LDPC 직접 적용(A/C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10912471
- **Type**: journal
- **Published**: May 2025
- **Authors**: Qiushi Xu, Ming Jiang, Fan Ding +1
- **PDF**: https://ieeexplore.ieee.org/document/10912471
- **Abstract**: In this letter, we present an improved ternary message passing (TMP) decoding scheme designed for the high-rate regular low-density parity-check (LDPC) codes, which are widely used in storage systems. The decoders in this approach transmit information internally by only three states, and compared to traditional normalized min-sum decoding, it retains only sign multiplication operations, resulting in lower complexity. Meanwhile, we propose a method for optimizing decoder parameters using the density evolution (DE) analysis, which allows the TMP decoders to achieve performance close to that of the belief propagation decoders. Furthermore, in the case of hard decision inputs, we introduce a quantized DE analysis to optimize and compute decoder parameters, enabling the TMP decoders to even outperform the normalized min-sum decoders.

## Memory-Assisted Quantized LDPC Decoding

- **Status**: ✅
- **Reason**: 조대 양자화 환경에서 이전 반복의 체크노드 메시지 재사용으로 0.23 dB 개선 및 32% 면적 효율 향상 — 양자화 민감한 NAND 플래시 LDPC 디코더에 직접 이식 가능한 알고리즘(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10879049
- **Type**: journal
- **Published**: May 2025
- **Authors**: Philipp Mohr, Gerhard Bauch
- **PDF**: https://ieeexplore.ieee.org/document/10879049
- **Abstract**: We enhance coarsely quantized LDPC decoding by reusing computed check node messages from previous iterations. Typically, variable and check nodes update and replace old messages every iteration. We show that, under coarse quantization, discarding old messages entails a significant loss of mutual information. The loss is avoided with additional memory, improving performance by up to 0.23 dB. We optimize quantization with a modified information bottleneck algorithm that considers the statistics of old messages. A simple merge operation reduces memory requirements. Depending on channel conditions and code rate, memory assistance enables up to 32% better area efficiency for 2-bit decoding.

## Generalized Fourier Transform Pair Codes

- **Status**: ✅
- **Reason**: 일반화 FTP 코드에 LC-OSD 알고리즘 적용, 병렬화 가능한 OSD계열 디코더(C) 이식 가능; 애매하므로 Phase 3 재검토
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10909205
- **Type**: journal
- **Published**: May 2025
- **Authors**: Yaping Lv, Suihua Cai, Xiao Ma
- **PDF**: https://ieeexplore.ieee.org/document/10909205
- **Abstract**: This letter is concerned with Fourier transform pair (FTP) codes over finite fields. Given any element of order n in a finite field, we can construct an FTP code with length  $2n$ , dimension n, and minimum distance at least  $2\sqrt {n}$ . Distinguishingly, an FTP code defined with any element (if it exists) of order 2, 3 or 5 in a finite field is a maximum distance separable code. In this letter, we extend the FTP codes to generalized FTP (GFTP) codes. To show the superiority of the GFTP codes over the FTP codes, we compute the binary weight spectra of the GFTP codes, approaching more close than the FTP codes to that of the random codes. We also apply the ordered statistic decoding with local constraints (LC-OSD) algorithm to the binary image of GFTP codes. Numerical results show that the GFTP codes perform better than the FTP codes as the code length increases. Numerical results also show that GFTP codes are comparable with existing codes of the same code rate and similar code length.

## Random Staircase Generator Matrix Codes: Coding Theorem, Performance Analysis, and Code Design

- **Status**: ✅
- **Reason**: 계단형 생성행렬 기반 LC-ROSD 알고리즘으로 가우시안 소거 병렬화·저지연 디코딩 실현 — OSD계열 이식 가능 디코더(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10884829
- **Type**: journal
- **Published**: May 2025
- **Authors**: Qianfan Wang, Yiwen Wang, Yixin Wang +2
- **PDF**: https://ieeexplore.ieee.org/document/10884829
- **Abstract**: In this paper, we present a class of codes, referred to as random staircase generator matrix codes (SGMCs), which have staircase-like generator matrices. In the infinite-length region, we prove that the random SGMC is capacity-achieving over binary-input output-symmetric (BIOS) channels. In the finite-length region, we propose the generalized representative ordered statistics decoding with local constraints (LC-ROSD) algorithm for the SGMCs. The most distinguished feature of the SGMCs with LC-ROSD is that the staircase-like matrices enable parallel implementation of the Gaussian elimination (GE), avoiding the serial GE of conventional OSD and supporting a potential low decoding latency, as implied from simulations. To analyze the performance of random SGMCs in the finite-length region, we derive the ensemble weight spectrum and invoke the conventional union bound. We also derive a partially random coding union (RCU) bound, which is tighter than the conventional one and is used as a criterion to design the SGMCs. Staircase-like generator matrices allow us to derive a series of (tighter and tighter) lower bounds based on the second-order Bonferroni inequality with the incremental number of codewords. The numerical results show that the decoding performance can match well with the proposed partially RCU bound for different code rates and different profiles. The numerical results also show that the tailored SGMCs with the LC-ROSD algorithm can approach the finite-length performance bound, outperforming the 5G low-density parity-check (LDPC) codes, 5G polar codes, and Reed-Muller (RM) codes.

## TRHyper: Low-Complexity Hypernetwork for Channel Neural Decoding With Learning Weights in Tensor Ring Format

- **Status**: ✅
- **Reason**: 텐서 링 형식 하이퍼네트워크로 재훈련 없이 디코더 파라미터 적응 — 저복잡도 신경망 LDPC 디코더 아키텍처(C) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10908838
- **Type**: journal
- **Published**: May 2025
- **Authors**: Yuanhui Liang, Chan-Tong Lam, Qingle Wu +2
- **PDF**: https://ieeexplore.ieee.org/document/10908838
- **Abstract**: In this letter, we propose a low-complexity hypernetwork for channel neural decoding with learning weights in tensor ring (TR) format, called TRHyper. The internal parameters and the number of layers of the TRHyper based channel neural decoding algorithm can be updated without retraining. We design the size of each TRHyper layer according to the size of the factor tensor in tensor ring format. During the training phase, we reuse the storage space for the learning weights of the main decoding network, so the proposed TRHyper no longer require additional storage space for its learning weights. Numerical results show that for low-density parity check (LDPC) codes, the performance of the TRHyper based channel neural decoder is similar to that of the original decoder, while for Bose-Chaudhuri-Hocquenghem (BCH) codes, the performance slightly exceeds the original decoder.

## Iterative Bounded Distance Decoding With Random Flipping for Product-Like Codes

- **Status**: ✅
- **Reason**: 제품 코드·스테어케이스 코드용 soft-aided HDD(iBDD-RF)를 제안하며 LLR 가중 합산·랜덤 플리핑으로 성능 개선 — 광통신/고속 스토리지용 디코더 알고리즘으로 C(이식 가능 디코더) 해당.
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10731861
- **Type**: journal
- **Published**: May 2025
- **Authors**: Guorong Li, Shiguo Wang, Shancheng Zhao
- **PDF**: https://ieeexplore.ieee.org/document/10731861
- **Abstract**: Product-like codes are widely used in high-speed communication systems since they can be decoded with low-complexity hard decision decoders (HDDs). To meet the growing demand of data rates, enhanced HDDs are required. In this paper, we propose a novel soft-aided HDD (SA-HDD), termed iterative bounded distance decoding with random flipping (iBDD-RF), for product-like codes. In iBDD-RF, the soft reliability of a bit is a weighted sum of the output of bounded distance decoder (BDD) and the channel log-likelihood ratio (LLR). When the amplitude of the soft reliability of a bit is less than a given threshold, it is flipped with a given probability. This random flipping may make the decoder escape from the local optimum. To optimize the threshold and the flipping probability, we derive the density evolution (DE) equations of iBDD-RF for product codes (PCs) and staircase codes (SCs). Our extensive numerical results show that iBDD-RF outperforms iBDD with scaled reliability (iBDD-SR) over the binary-input additive white Gaussian noise (Bi-AWGN) channel. Particularly, for a PC with (255,239,2) Bose-Chaudhuri-Hocquenghem (BCH) code and an SC with (254,230,3) BCH code, iBDD-RF performs about 0.25 dB and 0.28 dB better than iBDD-SR, respectively.

## Long-Haul Optical-Eigenvalue Transmission Using a Neural Network Demodulator and SD-FEC

- **Status**: ✅
- **Reason**: NN 디모듈레이터가 복잡한 수신 신호 분포에서 L-값(LLR)을 생성해 SD-FEC 성능 개선 — LLR 추정 NN 기법이 NAND 플래시 소프트 정보 생성에 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10892258
- **Type**: journal
- **Published**: May 2025
- **Authors**: Ken Mishina, Ryotaro Harada, Tsuyoshi Yoshida +2
- **PDF**: https://ieeexplore.ieee.org/document/10892258
- **Abstract**: Optical eigenvalue transmission based on inverse scattering transform (IST) has been studied for one of approaches to overcome the Kerr nonlinearity limit in fiber optic communications. In the recent decade, several multilevel modulation schemes that are based on IST, such as 16-ary and 64-ary signals using on-off encoding and b-modulation of multieigenvalues, have been proposed. To increase the transmission capacity and extend the transmission distance, applications of machine learning-based approaches to IST-based transmission have been proposed and demonstrated. Another prospective approach to increase the transmission capacity and extend the transmission distance in fiber optic communication involves the application of soft-decision forward error correction (SD-FEC). However, the applicability of SD-FEC to eigenvalue-modulated signals has not yet been investigated in detail because the distribution of the received signal is complicated for IST-based transmissions. In this paper, we describe in detail the theory of optical eigenvalue transmission, including the design of multilevel eigenvalue-modulated signals and the effects of noise and scaring parameters (coefficients for normalization of the nonlinear Schrödinger equation). We explain why neural network (NN) demodulators are advantageous for eigenvalue transmission systems. Consequently, we propose a combination of NN-based demodulators and SD-FEC decoding. A multilabel NN-based demodulator is employed to compute the L-value from the received eigenvalue pattern at the receiver. For a 16-ary eigenvalue-modulated signal, the proposed method outperformed a combination of the Gaussian approximation and SD-FEC in the simulation. Moreover, the experimental results show successful operation with error-free transmission through a 3000-km optical fiber line. In addition, we experimentally demonstrate the applicability of SD-FEC to a 4096-ary eigenvalue-modulated signal. The experimental results indicate that an achievable transmission distance can be extended to 1200 km using the NN demodulator and SD-FEC.

## Construction-D’ Lattices Based on Raptor Codes for Unconstrained AWGN Channels

- **Status**: ✅
- **Reason**: QC-LDPC pre-code와 BP 멀티레벨 디코더 사용 — QC-LDPC 구성·BP 디코더 요소가 이식 가능성 있어 애매하므로 in(Phase 3 재검토)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:11364450
- **Type**: conference
- **Published**: 26-29 May 
- **Authors**: Pegah Sharifi, Khadijeh Bagheri, Hassan Khodaiemehr +1
- **PDF**: https://ieeexplore.ieee.org/document/11364450
- **Abstract**: Raptor codes provide low encoding and decoding complexity, making them effective in unreliable networks. This paper introduces a novel framework for constructing multilevel lattices using Raptor codes, integrating Construction-D’ to enhance joint coding and modulation. We employ a multilevel decoder with Belief Propagation (BP) and concatenate Luby Transform (LT) codes with quasi-cyclic low-density parity-check (QC-LDPC) pre-codes, streamlining the construction process. Simulation results demonstrate that the proposed Raptor lattices significantly outperform traditional counterparts in Frame Error Rate (FER) over additive white Gaussian noise (AWGN) channels.

## FPGA Accelerated Adaptive LDPC-based Quantum Error Correction by Bitwise Pipeline Parallelism

- **Status**: ✅
- **Reason**: 양자 EC지만 generic LDPC soft-decision에 적용 가능한 FPGA 아키텍처·적응적 code rate(D 이식 가능)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:11044052
- **Type**: conference
- **Published**: 25-28 May 
- **Authors**: Bingze Ye, Jiyuan Liu, He Li
- **PDF**: https://ieeexplore.ieee.org/document/11044052
- **Abstract**: Quantum networks are at the forefront of next-generation communication technologies, providing unparalleled security by leveraging the fundamental properties of quantum mechanics. However, noise and interference adversely affect information sharing within quantum networks, causing quantum bit errors and diminishing the quality of quantum keys. To address this issue, high-speed quantum information error correction is necessitated and this work proposes an FPGA-accelerated error correction system based on low-density parity check (LDPC), incorporating algorithm-hardware co-optimizations. The proposed hardware architecture is applicable to generic LDPC soft decision algorithms and can adaptively select LDPC matrices with different code rates based on the quantum bit error rates. Experiment results demonstrate that the system exhibits high performance in error correction acceleration, achieving a throughput of 728 Mbps and up-to 9.4× speedup compared to existing FPGA-based LDPC error correction implementations.

## Hardware Implementation of Modified Noisy Gradient Descent Bit-Flipping Decoders

- **Status**: ✅
- **Reason**: MNGDBF 비트플립 디코더 FPGA 구현·6비트 양자화 — 이식 가능 디코더 알고리즘+HW(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:11043621
- **Type**: conference
- **Published**: 25-28 May 
- **Authors**: Qingan Li, Wai-Man Tam, Francis C. M. Lau
- **PDF**: https://ieeexplore.ieee.org/document/11043621
- **Abstract**: Recently, modified noisy gradient descent bit flipping (MNGDBF) algorithms have been proposed to eliminate the Gaussian random generators required in the original noisy gradient descent bit flipping (NGDBF) algorithm for the decoding of low-density parity-check (LDPC) codes. In this paper, a platform has been established for the hardware implementation of the LDPC encoder, the Gaussian noise channel generator and the decoder using MNGDBF decoding algorithms based on the use of field programmable gate array (FPGA). With 6-bit quantization, results show that the error performance achieved by hardware experiments is similar to that obtained by floating-point computer simulations. Moreover, we propose a new MNGDBF algorithm, in which the flipping condition is determined with the help of the summation of all inversion functions. Experimental results show that the proposed algorithm has superior performance than the original MNGDBF algorithm.

## Simulation and Performance Comparison of BP and NMSA Algorithm for QC-LDPC Codes under CCSDS Standards in BPSK-Modulated AWGN Channels

- **Status**: ✅
- **Reason**: QC-LDPC에 대한 BP vs NMSA 디코더 비교(NMSA 변형, 수치 안정성) — 이식 가능 디코더 알고리즘(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:11084120
- **Type**: conference
- **Published**: 23-25 May 
- **Authors**: Luyu Ren
- **PDF**: https://ieeexplore.ieee.org/document/11084120
- **Abstract**: Low-Density Parity-Check (LDPC) codes are essential for error correction in space communications, particularly in CCSDS implementations. Space communication channels face interference challenges due to extreme distances and signal attenuation. While Belief Propagation (BP) and Normalized Min-Sum Algorithm (NMSA) are widely used decoding techniques, quantitative comparisons for short-length QC-LDPC codes remain insufficient. This paper addresses this gap through systematic evaluation. This article implemented QC-LDPC encoding structures per CCSDS standards and conducted MATLAB simulations using BPSK modulation over AWGN channels. Simulations compared 1/2-rate codes across different lengths which including 320, 640, 1280 bits, and analyzed performance across rates (1/2, 2/3, 4/5) with fixed information length. Results show performance improves logarithmically with code length. BP outperforms NMSA by 0.2-0.3dB at low SNRs, while differences narrow at moderate SNRs. At high SNRs, NMSA occasionally surpasses BP due to better numerical stability. These findings provide reference data for spacecraft communication system designers facing power and computational constraints.

## Velocity Pausing Particle Swarm Optimization Algorithm based Universal High-Throughput and Low-Complexity LDPC Decoder for Laser Communications

- **Status**: ✅
- **Reason**: FPGA LDPC 디코더 HW 아키텍처(IFPP-IFP 파이프라인/병렬, 메시지패킹, 데이터정렬) — 고처리량 디코더 HW로 이식 가능(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:11070064
- **Type**: conference
- **Published**: 23-24 May 
- **Authors**: Bhanu Priya Y, Kishore Kumar A
- **PDF**: https://ieeexplore.ieee.org/document/11070064
- **Abstract**: This work presents Lower-Density Parity-Check (LDPC) decoder that is distinguished by its low complexity and highest throughput to fulfil the highest data rate of needs of laser communications and overcome the difficulties caused by propagation channel impairments. Existing techniques have issues with error correction, latency, and resource efficiency. In this manuscript, Velocity Pausing Particle Swarm Optimization Algorithm based Universal High-Throughput with Lower-Complexity Lower-Density Parity-Check Decoder used for Laser Communications (LDPC-LC-VPPSOA) is proposed. The primary goal of this decoder, depending upon Inter-Frame Pipeline with Intra-Frame Parallel (IFPP-IFP) system, is particularly designed to optimize the effectiveness of processing units, most important to enhance in decoding throughput. The performance of IFPP is enhanced through the Unitary Approximate Message Passing (UAMP) approach and the Velocity Pausing Particle Swarm Optimization Algorithm (VPPSOA), differentiating from existing solutions. Furthermore, the decoder uses a message packing approach and lower-complexity data alignment units to efficiently attain IFP. Then the proposed LDPC-LC-VPPSOA method is implemented in Xilinx XCKU060 FPGA and the performance metrics like decoding throughput, hardware complexity and Bit error rate are analyzed. Then, the LDPC-LC-VPPSOA approach attains 18.34%, 16.23%, 19.56% higher decoding throughput, 16.55%, 24.12% and 27.22% lower Hardware Complexity compared with existing techniques like Universal Higher- Throughput and Lower-Complexity Lower-Density Parity-Check Decoder used for Laser Communications (UHTLC-LDPCD-LC), Scalable High-Throughput with Lower-Latency DVB-S2(x) Lower-Density Parity-Check Decoders on SIMD Devices (SHTLL-LDPCD-SIMD) and Highly Reliable with Secure Scheme and Multi-Layer Parallel Lower-Density Parity-Check with Kyber for fist the generation Communications (HRSS-LDPC-KC) respectively.

## MISO-LDPC Decoding on UAV Communications: A Limited Bit-Width Learning Approach

- **Status**: ✅
- **Reason**: adder/XOR만 쓰는 고정소수점 LDPC 디코더 + 8bit 양자화 — LLR 양자화·저복잡도 디코더로 NAND 이식 가능(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:11152889
- **Type**: conference
- **Published**: 19-19 May 
- **Authors**: Shiyang Zhou, Xianhua Niu, Chao Pu
- **PDF**: https://ieeexplore.ieee.org/document/11152889
- **Abstract**: This paper proposes a low-complexity limited bit-width (LBW) multiple-input single-output (MISO) - low density parity check (LDPC) decoding algorithm for unmanned aerial vehicle (UAV) communications. Firstly, to solve the NP-hard problem of maximum a posteriori conventional (MAP) -based MISO detection, a learning-based quantized neural network (QNN) is proposed to fit the mapping of inputs and outputs in the MISO detector, whose computational complexity increases linearly with the number of antennas and modulation order. Secondly, a low-complexity fixed-point LDPC decoder is designed, which implements LDPC decoding only using adder and XOR operations with little performance loss. Additionally, The two-step LBW decoding algorithm only uses 8-bit quantized data throughout the MISO detection and LDPC decoding, which has a significantly lower computational complexity compared with floating-point computation. Finally, the simulation results demostrate the effectiveness of our proposed LBW MISO-LDPC decoding algorithm, whose bit error rate (BER) performance is only 0.5dB away from optimal floating-point MISO-LDPC decoding algorithm.

## Design and Simulation of An Efficient LDPC Encoder Suitable for 5G New Radio Base Graph 1

- **Status**: ✅
- **Reason**: QC-LDPC 인코더 구현: 부분행렬 양자화 순열값만 저장해 메모리 절감하는 HW 구성 — 이식 가능 HW 기법(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:11166776
- **Type**: conference
- **Published**: 15-16 May 
- **Authors**: Abhishek Bapurao Rode, Radhika D Joshi
- **PDF**: https://ieeexplore.ieee.org/document/11166776
- **Abstract**: This paper presents an encoder for 5G New Radio (NR)'s physical channel encoding which uses Quasi-Cyclic, Low-density parity check codes (QC-LDPC). The encoder utilizes a forward substitution algorithm within a configurable circuit structure, allowing it to adapt dynamically to various base graphs associated with 5G-LDPC codes. A key innovation is the storage of only quantized permutation values for each submatrix of the parity check matrix, rather than the entire parity check matrix, significantly reducing memory requirements. The encoder in this paper gives a throughput of up to 32.36 Mbps for a scaling factor of Z=192 at the frequency of 50Mhz.

## Learning of Information Bottleneck LDPC Decoding Operations with Genetic Algorithms

- **Status**: ✅
- **Reason**: 유전 알고리즘으로 정보병목 LDPC 디코딩 회로 학습 — min-sum 능가하는 신규 디코더 기법(C), 바이너리 LDPC
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:11047708
- **Type**: conference
- **Published**: 13-14 May 
- **Authors**: Rocío Martín Lima, Jan Lewandowsky, Marc Adrat +2
- **PDF**: https://ieeexplore.ieee.org/document/11047708
- **Abstract**: Physical layer signal processing presents significant challenges in military communication systems, where robust systems must retrieve data efficiently and rapidly. Therefore, this research focuses on the decoding of powerful low-density parity-check (LDPC) codes. Conventional LDPC decoders often become bottlenecks because they use cumbersome high-precision real number arithmetic. Recent approaches from the literature use compressive information bottleneck methods to reduce this complexity. They rely on integer messages and simple look-up operations, easing software implementations. Implemented on a chip, however, information bottleneck decoders, still need many logical gates to synthesize the decoding operations. As countermeasure, we directly utilize the bit-level representations of the exchanged messages. We propose to learn mutual-information-maximizing decoding circuits directly using genetic algorithms, instead of designing look-up tables and synthesizing them with elementary logical gates afterwards. Experimental results demonstrate that the proposed LDPC decoders outperform traditional suboptimal decoders, such as the min-sum decoder, in terms of bit error rate. This paper was originally presented at the NATO Science and Technology Organization Symposium (ICMCIS) organized by the Information Systems Technology (IST) Scientific and Technical Committee, IST-209-RSY - the ICMCIS, held in Oeiras, Portugal, 13–14 May 2025.”

## Low-Complexity Neural Belief Propagation Algorithm for LDPC Decoding

- **Status**: ✅
- **Reason**: 저복잡도 신경 BP(NBP) LDPC 디코더 — 가중치 공유로 파라미터/메모리 절감하는 신규 디코더(C), 바이너리 LDPC
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:11059590
- **Type**: conference
- **Published**: 12-16 May 
- **Authors**: Haojia Zhang, Shuai Han, Hao Chen
- **PDF**: https://ieeexplore.ieee.org/document/11059590
- **Abstract**: With the rapid development of deep learning research and physical layer communication applications, deep learning-based channel coding has gradually become a research hotspot. In this paper, we propose a LDPC decoding network based on neural belief propagation (NBP) decoding. By introducing weights sharing mechanism, the weights vary across different iterations. The number of parameters is reduced, which significantly lowers memory requirements. In addition, we optimize the loss function to better train the model, achieving a lower bit error rate (BER) performance. Experimental results show that the proposed decoder yields significant performance improvements with respect to NBP, and significantly reducing the number of learnable weights.

## Burst Correcting Capability of Block-Permutation LDPC Codes

- **Status**: ✅
- **Reason**: 블록순열 LDPC 버스트 정정능력 — 블록순열/순환 구성의 코드설계(E) 신규 분석, 바이너리 LDPC
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:11017292
- **Type**: conference
- **Published**: 12-16 May 
- **Authors**: Alina M. Veresova, Andrei A. Ovchinnikov
- **PDF**: https://ieeexplore.ieee.org/document/11017292
- **Abstract**: The article examines the impact of the block-permutation structure of low-density parity-check codes on their ability to correct single error bursts. The length of the corrected burst is estimated, depending on the size of the blocks used in block-circulant and block-permutation codes with different parameter settings. The article also estimates the probability of finding codes with maximum achievable correcting capabilities when using different construction methods. It is found that using a block-permutation construction allows for a high probability of achieving the maximum possible correcting capability, regardless of the parameters used. However, when using block-circulant codes, it can be difficult or impossible to find codes with the maximum achievable length of burst to be corrected for nonprime block sizes. Thus, the block-permutation construction turns out to be more effective in terms of its correcting capabilities, and can be used in situations where storing the code in a compact form of a base matrix is not a significant criterion.
