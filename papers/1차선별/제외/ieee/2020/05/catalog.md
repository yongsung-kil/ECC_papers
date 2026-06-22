# IEEE Xplore — 2020-05


## Low-Complexity Interval Passing Algorithm and VLSI Architecture for Binary Compressed Sensing

- **Status**: ❌
- **Reason**: Binary compressed sensing interval passing 알고리즘/VLSI — LDPC 행렬을 측정행렬로 사용한 CS 복원, 채널코딩 ECC 디코더 아님
- **ID**: ieee:8984332
- **Type**: journal
- **Published**: May 2020
- **Authors**: Shantharam Kalipatnapu, Indrajit Chakrabarti
- **PDF**: https://ieeexplore.ieee.org/document/8984332
- **Abstract**: Binary compressed sensing (BCS), in which signals of interest have binary values, finds applications in areas including fault detection and wireless sensor networks. In this article, a low-complexity VLSI architecture for BCS based on interval passing algorithm is proposed. Moreover, the algorithm is modified in order to reduce its complexity without significant loss in performance, and its corresponding VLSI architecture is proposed. Binary low-density parity check (LDPC) matrices based on finite geometry have been used as measurement matrices. The proposed VLSI architectures have been synthesized in both ASIC and field-programmable gate array (FPGA) platforms. The hardware consumption of the proposed designs is independent of sparsity values. Moreover, the proposed architectures offer high frequency of operation and low reconstruction time when compared to the state-of-the-art designs. Specifically, the 65-nm ASIC realization operates at a maximum frequency of 500 and 666.67 MHz and offer a reconstruction time of 6.3 and 4.7 ns, respectively, for a $64\times 256$ deterministic measurement matrix.

## Design and Analysis of Joint Source Channel Coding Schemes Over Non-Standard Coding Channels

- **Status**: ❌
- **Reason**: DCSK/Rayleigh 채널 위 JSCC(DP-LDPC) — 소스-채널 결합, LDPC가 베이스라인이고 떼어낼 ECC 기법 없음
- **ID**: ieee:9055164
- **Type**: journal
- **Published**: May 2020
- **Authors**: Qiwang Chen, Lin Wang
- **PDF**: https://ieeexplore.ieee.org/document/9055164
- **Abstract**: Although a mountain of work on joint source-channel coding (JSCC) scheme over standard coding channels (a combination of BPSK modulation and AWGN channels) have been studied deeply, there has been no knowledge about JSCC over non-standard coding channels. In this paper, a JSCC scheme based on double protograph low-density parity-check (DP-LDPC) codes is proposed over non-standard coding channels which consists of M-ary differential chaos shift keying (DCSK) and Rayleigh fading channels is proposed, named as JSCC-DCSK system. A joint protograph extrinsic information transform (JPEXIT) algorithm is proposed to analyze the decoding threshold of DP-LDPC codes on the non-standard coding channels. Considering the effects from the source redundancy left by source coding and the non-linear property of non-standard coding channels, the design of DP-LDPC structure is discussed, and new design principles from a global perspective are proposed. Several DP-LDPC codes for different source statistic are designed by the aid of JPEXIT algorithm and verified by Monte Carlo simulation. The appropriate number of the turbo iteration is determined to keep the bit error rate (BER) of system performance and the complexity of the receiver at a low level.

## A Reconciliation Strategy for Real-Time Satellite-Based QKD

- **Status**: ❌
- **Reason**: 위성 QKD reconciliation 전략; 양자 QKD 응용 + LDPC 디코더 스케줄링 설계로 이식 가능 ECC 새 기여 없음
- **ID**: ieee:9020104
- **Type**: journal
- **Published**: May 2020
- **Authors**: Xiaoyu Ai, Robert Malaney, Soon Xin Ng
- **PDF**: https://ieeexplore.ieee.org/document/9020104
- **Abstract**: In practical Quantum Key Distribution (QKD) deployments we would like to design QKD solutions that provide for a target QKD key rate, in bits/pulse, at a specified upper-limit on the failure probability. However, in the finite-signalling setting, in which all real-world QKD systems exist, the common practice of achieving such a solution fails to deliver the maximum throughput rate of the classical decoder. This in turn means that the possibility that classical reconciliation becomes the bottleneck of the entire QKD protocol is not minimised. A design strategy that minimises this latter possibility, whilst achieving a target QKD rate with a target ceiling on the failure probability has not been developed - a situation we remedy here. Although our new design strategy detailed here is for LDPC codes and applied to two specific QKD protocols, the same strategy is generally applicable to all classical decoders and all QKD protocols. It is also deployable even in circumstances where the quantum bit error is variable, such as in satellite QKD systems.

## DeepJSCC-f: Deep Joint Source-Channel Coding of Images With Feedback

- **Status**: ❌
- **Reason**: 이미지 딥 JSCC(피드백) 오토인코더 — 채널코딩 ECC 아닌 소스-채널 결합, 이식 가능 LDPC 기법 없음
- **ID**: ieee:9066966
- **Type**: journal
- **Published**: May 2020
- **Authors**: David Burth Kurka, Deniz Gündüz
- **PDF**: https://ieeexplore.ieee.org/document/9066966
- **Abstract**: We consider wireless transmission of images in the presence of channel output feedback. From a Shannon theoretic perspective feedback does not improve the asymptotic end-to-end performance, and separate source coding followed by capacity-achieving channel coding, which ignores the feedback signal, achieves the optimal performance. It is well known that separation is not optimal in the practical finite blocklength regime; however, there are no known practical joint source-channel coding (JSCC) schemes that can exploit the feedback signal and surpass the performance of separation-based schemes. Inspired by the recent success of deep learning methods for JSCC, we investigate how noiseless or noisy channel output feedback can be incorporated into the transmission system to improve the reconstruction quality at the receiver. We introduce an autoencoder-based JSCC scheme, which we call DeepJSCC-f , that exploits the channel output feedback, and provides considerable improvements in terms of the end-to-end reconstruction quality for fixed-length transmission, or in terms of the average delay for variable-length transmission. To the best of our knowledge, this is the first practical JSCC scheme that can fully exploit channel output feedback, demonstrating yet another setting in which modern machine learning techniques can enable the design of new and efficient communication methods that surpass the performance of traditional structured coding-based designs.

## Enhanced Belief Propagation Decoder for 5G Polar Codes With Bit-Flipping

- **Status**: ❌
- **Reason**: 5G 폴라 코드 BP flip 디코더 — LDPC가 아닌 polar code 전용 기법으로 NAND 바이너리 LDPC 이식 대상 아님
- **ID**: ieee:9051990
- **Type**: journal
- **Published**: May 2020
- **Authors**: Yifei Shen, Wenqing Song, Yuqing Ren +3
- **PDF**: https://ieeexplore.ieee.org/document/9051990
- **Abstract**: Due to its parallel propagation property, the belief propagation (BP) polar decoding can achieve high throughput and has drawn increasing attention. However, the BP decoding is not comparable with the successive cancellation list (SCL) decoding in terms of the error correction performance. In this brief, two BP flip (BPF) decoding algorithms are proposed. Compared with the existing BPF decoding, the generalized BPF (GBPF) decoding identifies error-prone bits more efficiently with a redefinition of bit-flipping. Furthermore, the GBPF decoding is optimized by decreasing the searching range by half, leading to the enhanced BP flip (EBPF) decoding with reduced complexity and improved performance for 5G polar codes. The hardware architecture is provided and implemented using SMIC 65nm CMOS technology. The results show that, compared with the state-of-the-art SC flip decoders, the proposed EBPF decoder exhibits 30% throughput improvement under comparable error correction performance.

## Efficient Belief Propagation Polar Decoder With Loop Simplification Based Factor Graphs

- **Status**: ❌
- **Reason**: Polar 코드 BP list 디코더 factor graph 루프 단순화 — LDPC가 아닌 polar 전용, 이식성 낮음
- **ID**: ieee:9027949
- **Type**: journal
- **Published**: May 2020
- **Authors**: Yuqing Ren, Yifei Shen, Zaichen Zhang +2
- **PDF**: https://ieeexplore.ieee.org/document/9027949
- **Abstract**: The performance of belief propagation list (BPL) decoding of polar codes is related to the selection of L factor graphs (FGs), which have the least number of girths. However, the straightforward search of such FGs is of high complexity. To achieve good performance with reasonable complexity, we propose an efficient method to find FGs with the least number of length-12 loops in all permuted FGs. Since some length-12 loops have been destroyed by redundant decoding operations, the corresponding FGs can be simplified to different numbers of length-12 loops. Thanks to the proposed loop simplification (LS), BPL decoding is now based on more efficient FGs, resulting in better performance and lower average decoding latency than the state-of-the-art. Numerical results have shown that the performance improvement is 0.15 dB when frame error ratio (FER) is 10-4, for (1024, 512) codes with L = 64.

## Factor Graph Based Message Passing Algorithms for Joint Phase-Noise Estimation and Decoding in OFDM-IM

- **Status**: ❌
- **Reason**: OFDM-IM 위상잡음 결합 추정·디코딩(GAMP/BP-MF) — 무선 응용 특이적, NAND LDPC ECC로 떼어낼 디코더 기법 없음
- **ID**: ieee:8993708
- **Type**: journal
- **Published**: May 2020
- **Authors**: Qiaolin Shi, Nan Wu, Hua Wang +2
- **PDF**: https://ieeexplore.ieee.org/document/8993708
- **Abstract**: In order to glean benefits from orthogonal frequency division multiplexing combined with index modulation (OFDM-IM) in the presence of strong Phase-Noise (PHN), in this paper, low-complexity joint PHN estimation and decoding methods are developed in the framework of message passing on a factor graph. Both the Wiener process and the truncated discrete cosine transform (DCT) expansion model are considered for approximating the PHN variation. Then based on these a factor graph is constructed for explicitly representing the joint estimation and detection problem. Taking full account of the sparse and structured a priori information arriving from the soft-in soft-out (SISO) decoder of a turbo receiver, a modified generalized approximate message passing (GAMP) algorithm is invoked for decoupling the frequency-domain symbols. In the decoupling step, mean field (MF) approximation is employed for solving the unknown nonlinear transform matrix problem imposed by PHN. Furthermore, merged belief propagation and MF (BP-MF) methods amalgamated both with sequential and parallel message passing schedules are introduced and compared to the proposed GAMP based algorithms in terms of their bit error ratio (BER) vs. complexity. Our simulation results demonstrate the efficiency of the proposed algorithms in the presence of both perfect and imperfect channel state information.

## Achievable Rate Region for Iterative Multi-User Detection via Low-Cost Gaussian Approximation

- **Status**: ❌
- **Reason**: IDMA 다중사용자 검출 EXIT chart 영역 정리 — 순수 이론/코드설계 가이드, 떼어낼 LDPC 디코더·HW 기법 없음
- **ID**: ieee:8995793
- **Type**: journal
- **Published**: May 2020
- **Authors**: Xiaojie Wang, Chulong Liang, Li Ping +1
- **PDF**: https://ieeexplore.ieee.org/document/8995793
- **Abstract**: We establish a multiuser extrinsic information transfer (EXIT) chart area theorem for the interleave-division multiple access (IDMA) scheme, a special form of superposition coding, in multiple access channels (MACs). A low-cost multi-user detection (MUD) based on the Gaussian approximation (GA) is assumed. The evolution of mean-square errors (MSE) of the GA-based MUD during iterative processing is studied. We show that the K-dimensional tuples formed by the MSEs of K users constitute a conservative vector field. The achievable rate is a potential function of this conservative field, so it is the integral along any path in the field with value of the achievable rate solely determined by the two path terminals. Optimized error correcting codes can be found given the integration paths in the MSE fields by matching EXIT type functions. The above findings imply that i) low-cost GA detection can provide MAC capacity-approaching performance, ii) the sum-rate capacity can be achieved independently of the integration path in the MSE fields; and iii) the integration path determining achievable rate tuples of all users can be an extra degree of freedom for code design.

## Optimized Polarizing Matrix Extension Based HARQ Scheme for Short Packet Transmission

- **Status**: ❌
- **Reason**: Polar matrix extension 기반 HARQ 단패킷 전송 — 폴라 부호 전용, LDPC 이식성 없음
- **ID**: ieee:8977565
- **Type**: journal
- **Published**: May 2020
- **Authors**: Jingqiu Gao, Pingzhi Fan, Li Li
- **PDF**: https://ieeexplore.ieee.org/document/8977565
- **Abstract**: In this letter, an optimized polarizing matrix extension (OPME) method is incorporated into the adaptive incremental redundancy hybrid ARQ for the sake of supporting short packet transmission. Benefiting from synthetically utilizing bit-channel reliability and code distance without adding extra online computational complexity, the generation and distribution of proper new information bits and bit-protect pairs are specifically designed. Finally, a suboptimal algorithm is proposed for simplifying the search process of the proper number of bit-protect pairs only at the cost of a negligible performance loss. As a result, the simulation demonstrate that the proposed scheme could achieve a considerable error-performance gain compared with the state-of-the-art result under short block length.

## A Novel Adaptive Rate Matching Algorithm Based on LDPC for Satellite Communication

- **Status**: ❌
- **Reason**: 위성통신용 LLR 신뢰순위 기반 적응 rate matching(shortening) — 무선 rate matching 특이적, NAND LDPC 이식 기법 약함
- **ID**: ieee:9119665
- **Type**: conference
- **Published**: 8-12 May 2
- **Authors**: Zhongliang Deng, Yanyue Yang, Ke Wang +3
- **PDF**: https://ieeexplore.ieee.org/document/9119665
- **Abstract**: The distance of satellite signal transmission is long, and it is easily affected by rain and snow. The channel state changes quickly. The traditional design is based on the worst channel conditions. In sunny conditions, it will cause much waste of resources. Therefore, the satellite needs to adaptively adjust the code rate according to the actual channel state. This technology not only helps to maximize the transmission rate but also effectively improves the spectral efficiency. A standard method of changing rates is rate matching. Shortening is a technique of rate matching. The performance of current shortening algorithms is weak, or the calculation is very complicated. For satellites, there are not enough resources to perform complex calculations and storage when the performance requirements are met. Therefore, this paper proposes an adaptive rate matching algorithm based on the confidence ranking of log-like ratio (LLR) information (CRLI) to reduce resource occupation and achieve better error correction and anti-interference capabilities. The simulation under the additive white Gaussian noise (AWGN) channel proves that the CRLI algorithm has a better bit error ratio (BER) performance, lower complexity, and occupies fewer resources.

## Deep Joint Source-Channel Coding of Images with Feedback

- **Status**: ❌
- **Reason**: Deep JSCC(소스-채널 결합) 이미지 전송 — 기준상 JSCC 명시 제외, 떼어낼 LDPC ECC 기법 없음
- **ID**: ieee:9054216
- **Type**: conference
- **Published**: 4-8 May 20
- **Authors**: David Burth Kurka, Deniz Gündüz
- **PDF**: https://ieeexplore.ieee.org/document/9054216
- **Abstract**: We consider wireless transmission of images in the presence of channel output feedback, by introducing an autoencoder-based deep joint source-channel coding (JSCC) scheme. We achieve impressive results in terms of the end-to-end reconstruction quality for fixed length transmission, and in terms of the average delay for variable length transmission. To the best of our knowledge, this is the first practical JSCC scheme that can fully exploit channel output feedback, demonstrating yet another setting in which modern machine learning techniques can enable the design of new and efficient communication methods that surpass the performance of traditional structured coding schemes.

## Fully Pipelined Iteration Unrolled Decoders the Road to TB/S Turbo Decoding

- **Status**: ❌
- **Reason**: Turbo 디코더 파이프라인/언롤 HW 아키텍처 — Turbo 전용 반복구조, LDPC 이식성 낮음
- **ID**: ieee:9053453
- **Type**: conference
- **Published**: 4-8 May 20
- **Authors**: Stefan Weithoffer, Rami Klaimi, Charbel Abdel Nour +2
- **PDF**: https://ieeexplore.ieee.org/document/9053453
- **Abstract**: Turbo codes are a well-known code class used for example in the LTE mobile communications standard. They provide built-in rate flexibility and a low-complexity and fast encoding. However, the serial nature of their decoding algorithm makes high-throughput hardware implementations difficult. In this paper, we present recent findings on the implementation of ultra-high throughput Turbo decoders. We illustrate how functional parallelization at the iteration level can achieve a throughput of several hundred Gb/s in 28 nm technology. Our results show that, by spatially parallelizing the half-iteration stages of fully pipelined iteration unrolled decoders into X-windows of size 32, an area reduction of 40% can be achieved. We further evaluate the area savings through further reduction of the X-window size. Lastly, we show how the area complexity and the throughput of the fully pipelined iteration unrolled architecture scale to larger frame sizes. We consider the same target bit error rate performance for all frame sizes and highlight the direct correlation to area consumption.

## Joint Coding and Modulation in the Ultra-Short Blocklength Regime for Bernoulli-Gaussian Impulsive Noise Channels Using Autoencoders

- **Status**: ❌
- **Reason**: 오토인코더 기반 결합 코딩/변조(JSCC형) — 떼어낼 LDPC ECC 기법 없음
- **ID**: ieee:9053716
- **Type**: conference
- **Published**: 4-8 May 20
- **Authors**: Kirty Vedula, Randy Paffenroth, D. Richard Brown
- **PDF**: https://ieeexplore.ieee.org/document/9053716
- **Abstract**: This paper develops a joint coding and modulation scheme for end-to-end communication system design using an autoencoder architecture in the ultra-short blocklength regime. Unlike the classical approach of separately designing error correction codes and modulation schemes for a given channel, the approach here is to learn an optimal mapping directly from messages to channel inputs while simultaneously learning an optimal mapping directly from channel outputs to estimated messages. The block error rate (BLER) of this approach is compared against classical short blocklength linear block codes with binary phase shift keying (BPSK) modulation in additive white Gaussian noise (AWGN) and Bernoulli-Gaussian impulsive noise (BGIN) channels. For AWGN channels, numerical results show that the autoencoder can achieve better BLER performance than BPSK modulated Hamming codes with maximum likelihood decoding. For BGIN channels, numerical results show the autoencoder achieves uniformly better BLER performance than conventional block codes with BPSK modulation, even with impulsive noise mitigation techniques such as blanking and clipping. The proposed architecture is general and can be modified for comparison against other block coding schemes and higher-order modulations.

## Complex Trainable Ista for Linear and Nonlinear Inverse Problems

- **Status**: ❌
- **Reason**: 복소필드 신호복원(C-TISTA) deep unfolding — LDPC/ECC 디코더 아닌 일반 역문제 신호복원
- **ID**: ieee:9053161
- **Type**: conference
- **Published**: 4-8 May 20
- **Authors**: Satoshi Takabe, Tadashi Wadayama, Yonina C. Eldar
- **PDF**: https://ieeexplore.ieee.org/document/9053161
- **Abstract**: Complex-field signal recovery problems from noisy linear/nonlinear measurements appear in many areas of signal processing and wireless communications. In this paper, we propose a trainable iterative signal recovery algorithm named complex-field TISTA (C-TISTA) which treats complex-field nonlinear inverse problems. C-TISTA is based on the concept of deep unfolding and consists of a gradient descent step with the Wirtinger derivatives followed by a shrinkage step with a trainable complex-valued shrinkage function. Importantly, it contains a small number of trainable parameters so that its training process can be executed efficiently. Numerical results indicate that C-TISTA shows remarkable signal recovery performance compared with existing algorithms.

## On Polar Coding For Finite Blocklength Secret Key Generation Over Wireless Channels

- **Status**: ❌
- **Reason**: Polar coding 기반 비밀키 생성 — LDPC 아니고 보안/키생성 도메인, 이식할 LDPC 디코더 기법 없음
- **ID**: ieee:9054247
- **Type**: conference
- **Published**: 4-8 May 20
- **Authors**: Henri Hentilä, Yanina Y. Shkel, Visa Koivunen +1
- **PDF**: https://ieeexplore.ieee.org/document/9054247
- **Abstract**: We consider the problem of secret key generation from correlated Gaussian random variables in the finite blocklength regime. Such keys could be used to encrypt communication in IoT networks, and have provable secrecy guarantees in contrast to classic cryptographic approaches. We investigate the performance of polar coding schemes for generating the secret key over short blocklengths. Our simulation results show that the proposed scheme achieves close to theoretical upper bounds at short blocklengths.

## A Linear Time Partitioning Algorithm for Frequency Weighted Impurity Functions

- **Status**: ❌
- **Reason**: 불순도 함수 파티셔닝(k-means/VQ) 알고리즘 — LDPC ECC와 무관
- **ID**: ieee:9054763
- **Type**: conference
- **Published**: 4-8 May 20
- **Authors**: Thuan Nguyen, Thinh Nguyen
- **PDF**: https://ieeexplore.ieee.org/document/9054763
- **Abstract**: Partitioning algorithms play a key role in machine learning, signal processing, and communications. They are used in many well-known NP-hard problems such as k-means clustering and vector quantization. The goodness of a partition scheme is measured by a given impurity function over the resulted partitions. The optimal partition is one(s) with the minimum impurity. Practical algorithms for finding an optimal partitioning are approximate, heuristic, and often assume certain properties of the given impurity function such as concavity/convexity. In this paper, we propose a heuristic, efficient (linear time) algorithm for finding the minimum impurity for a broader class of impurity functions which includes popular impurities such as Gini index and entropy. We also make a connection to a well-known result which states that the optimal partitions correspond to the regions separated by hyperplane cuts in the probability space of the posterior distribution.

## Dynamic Oversampling in 1-Bit Quantized Asynchronous Large-Scale Multiple-Antenna Systems for Sustainable Iot Networks

- **Status**: ❌
- **Reason**: 1비트 ADC 동적 오버샘플링 안테나 시스템 — LDPC/ECC와 무관한 RF 프론트엔드 신호처리
- **ID**: ieee:9054015
- **Type**: conference
- **Published**: 4-8 May 20
- **Authors**: Zhichao Shao, Lukas T. N. Landau, Rodrigo C. de Lamare
- **PDF**: https://ieeexplore.ieee.org/document/9054015
- **Abstract**: In this paper, we propose a dynamic oversampling technique for asynchronous large-scale multiple-antenna systems with 1-bit analog-to-digital converters at the base station that is suitable for sustainable internet of things and cellular networks. To the best of our knowledge, this is the first paper to introduce a dynamic oversampling technique for such systems. The main idea is to sample the received signal at a higher rate and only few weighted samples are chosen for further signal processing. We apply the generalized eigenvalue decomposition algorithm for linearly combining the samples and performing dimension reduction. We investigate the proposed technique in terms of the Bussgang theorem based sum rate capacity. Numerical results show that with the proposed dynamic oversampling technique the system can use small number of processing samples to achieve the same sum rates as the standard uniform oversampling technique while maintaining the same power consumption.

## A Low-Latency Successive Cancellation Hybrid Decoder for Convolutional Polar Codes

- **Status**: ❌
- **Reason**: convolutional polar SC 하이브리드 디코더 — polar 전용 SC/SCL/SCF 구조, LDPC BP로 이식할 기법 없음
- **ID**: ieee:9054155
- **Type**: conference
- **Published**: 4-8 May 20
- **Authors**: Yu Wang, Shikai Qiu, Lirui Chen +4
- **PDF**: https://ieeexplore.ieee.org/document/9054155
- **Abstract**: By adopting successive cancellation list decoding (SCL), polar codes demonstrate competitive error correction performance over LDPC and Turbo codes. However, SCL decoding suffers from high computational complexity and long decoding latency, especially when the list size is very large. Successive cancellation flip (SCF), as another decoding algorithm that can achieve high error correction performance, has a complexity that is close to that of successive cancellation (SC) decoding. With the observation that SCL and SCF decoding are similar at giving more chances to inspect possible codewords simultaneously or sequentially, a novel hybrid decoder is proposed in this paper, which essentially combines the ideas of SCF and SCL decoders. Moreover, in order to compensate for the degradation of performance caused by the reduction of path splitting and further reduce the decoding latency, the convolutional polar codes are adopted with a designed bit-flipping set. Simulation results demonstrate that the proposed decoder achieves the reduction of decoding latency while attaining better performance than conventional CRC-aided SCL decoder.

## Secure Communication Based on Reliability-Based Hybrid ARQ and LDPC Codes

- **Status**: ❌
- **Reason**: RB-HARQ+irregular LDPC 보안 재전송 전략 — 무선 보안 응용 특이적, 표준 LDPC 사용, 떼어낼 새 ECC 기법 없음
- **ID**: ieee:9115533
- **Type**: conference
- **Published**: 4-7 May 20
- **Authors**: Lei Wang, Daoxing Guo
- **PDF**: https://ieeexplore.ieee.org/document/9115533
- **Abstract**: This paper designs a re-transmission strategy to intensify the security of communication over the additive white Gaussian noise (AWGN) wire-tap channel. In this scheme, irregular low-density parity-check (LDPC) codes work with reliability-based hybrid automatic repeat-request (RB-HARQ). For irregular LDPC codes, the variable nodes have different degrees, which means miscellaneous protection for the nodes. In RB-HARQ protocol, the legitimate receiver calls for re-transmissions including the most unreliable bits at decoder's outputting. The bits' reliability can be evaluated by the average magnitude of a posteriori probability log-likelihood ratios (APP LLRs). Specifically, this scheme utilizes the bit-error rate (BER) to assess the secrecy performance. Besides, the paper gives close analyses of BER through theoretical arguments and simulations. Results of numerical example demonstrate that RB-HARQ protocol with irregular LDPC codes can hugely reinforce the security performance of the communication system.

## Gbit/s Non-Binary LDPC Decoders: High-Throughput using High-Level Specifications

- **Status**: ❌
- **Reason**: 비이진(non-binary) LDPC 디코더 — 바이너리 LDPC만 포함 원칙에 따라 제외
- **ID**: ieee:9114836
- **Type**: conference
- **Published**: 3-6 May 20
- **Authors**: Oscar Ferraz, Srinivasan Subramaniyan, Guohui Wang +3
- **PDF**: https://ieeexplore.ieee.org/document/9114836
- **Abstract**: It is commonly perceived that an HLS specification targeted for FPGAs cannot provide throughput performance in par with equivalent RTL descriptions. In this work we developed a complex design of a non-binary LDPC decoder, that although hard to generalise, shows that HLS provides sufficient architectural refinement options. They allow attaining performance above CPU- and GPU-based ones and excel at providing a faster design cycle when compared to RTL development.

## A Turbo Maximum-a-Posteriori Equalizer for Faster-than-Nyquist Applications

- **Status**: ❌
- **Reason**: FTN용 turbo BCJR 등화기(non-binary constellation) — 등화 전용, 바이너리 LDPC BP에 이식할 기법 없음
- **ID**: ieee:9114873
- **Type**: conference
- **Published**: 3-6 May 20
- **Authors**: Mohamed Omran Matar, Mrinmoy Jana, Jeebak Mitra +2
- **PDF**: https://ieeexplore.ieee.org/document/9114873
- **Abstract**: Faster-than-Nyquist (FTN) transmission employs non-orthogonal signaling to improve spectral efficiency over conventional orthogonal transmission at the Nyquist rate. However, FTN signaling also introduces inter-symbol interference (ISI), which must be mitigated through additional signal processing.In this paper, we present a scalable FPGA-based architecture for a turbo maximum-a-posteriori (MAP) equalizer based on the Bahl-Cock-Jelinek-Raviv (BCJR) algorithm to mitigate the ISI. In contrast to many existing hardware implementations of BCJR, where the algorithm performs turbo decoding over a binary alphabet for an already-equalized channel, our FPGA design applies BCJR to non-binary signal constellations and for the task of equalization. To the best of our knowledge, this is the first published FPGA-based BCJR equalizer implementation suitable for FTN applications, where a binary forward-error-correction decoder is employed in tandem with the equalizer.Through careful tradeoff selection and optimization of the design space, our implementation achieves a maximum per-PE throughput of 602 Mbps, and a total of 15.4 Gbps within the constraints of a Xilinx UltraScale+(xcvu13p) device.

## New Nonlinear Signal Processing Method Based on LS Algorithm and Decision Feedback at Receiver

- **Status**: ❌
- **Reason**: 위성수신기 비선형 등화 LS 알고리즘 — LDPC는 부수 언급, 떼어낼 디코더/HW/구성 기법 없음
- **ID**: ieee:9123285
- **Type**: conference
- **Published**: 29-31 May 
- **Authors**: Zhaoyang Xi, Jinshu Chen
- **PDF**: https://ieeexplore.ieee.org/document/9123285
- **Abstract**: This paper proposes a new low-complexity decision feedback nonlinear equalization architecture. It applies the Least Square (LS) algorithm to the coefficient updating structure of decision feedback blind equalization polynomials and momentum coefficient updating algorithm. It uses a low-complexity memory polynomial model to compensate for the nonlinearity and memory effects caused by amplifiers and channels. Besides, the new structure uses an improved iterative LS algorithm when updating the coefficients of the memory polynomial model, and it uses the decision feedback signal as a standard point to calculate the cost function. The new processing method can handle sizeable nonlinear distortion and memory effects. In the model coefficient updating, the symbol point data block is used to update the memory polynomial coefficients by the improved LS algorithm. Compared with other traditional Least Mean Square (LMS) algorithms or Recursive Least Square (RLS) algorithms, the new method has higher stability. The new algorithm can use shorter data blocks to meet the Low-Density Parity Check Code (LDPC) decoding performance requirements and save a lot of computing and storage resources for satellite receivers. It has excellent reference significance for practical engineering applications.

## Distributed Fronthaul Compression Design for Rateless Coded Multi-User Uplink Transmission in C-RAN

- **Status**: ❌
- **Reason**: C-RAN fronthaul 압축에 LDPC를 분산소스코딩(신드롬)으로 사용 — 채널 ECC 아닌 소스압축, 떼어낼 ECC 기법 없음
- **ID**: ieee:9123261
- **Type**: conference
- **Published**: 29-31 May 
- **Authors**: Yu Zhang, Zhehao Fan, Limin Meng +1
- **PDF**: https://ieeexplore.ieee.org/document/9123261
- **Abstract**: We consider the multi-user uplink transmission in cloud radio access network (C-RAN), which consists of two users, two radio remote heads (RRHs), and the baseband processing unit (BBU) pool. The users adopt Raptor code and send the modulated signals to both RRHs continuously until receiving the acknowledge character (ACK) feedback from the BBU. A novel fronthaul compression scheme for RRH is proposed. Explicitly, both RRHs quantize the received signal to meet the fronthaul capacity constraint. One of the RRHs further compresses the quantized signal with low density parity check (LDPC) code. Then not only the resulted syndrome bits, additional quantization bits are also sent to the BBU according to the remaining fronthaul capacity, which can reduce the quantization noise at the BBU. We optimize the LDPC code based on extrinsic information transfer (EXIT) analysis. Simulation results show that optimized LDPC code has good compression performance compared with regular LDPC code, and the proposed fronthaul compression scheme outperforms the conventional scheme without DSC.

## Iterative Cancellation for Inter-Block-Interference on LDPC coded MIMO-OFDM Systems

- **Status**: ❌
- **Reason**: MIMO-OFDM IBI 반복 간섭제거 수신기, LDPC는 베이스라인일 뿐 이식할 ECC 기법 없음
- **ID**: ieee:9129167
- **Type**: conference
- **Published**: 25-28 May 
- **Authors**: Masakazu Kizawa, Tetsushi Ikegami
- **PDF**: https://ieeexplore.ieee.org/document/9129167
- **Abstract**: An OFDM transmission is robust to the multipath delay due to the addition of a cyclic prefix (CP). However, it will suffer from an inter-block-interference (IBI) under a severe long delay multipath channel whose channel impulse response (CIR) is longer than that of the CP. Since extending the CP leads to the loss of spectrum efficiency, some compensation scheme is needed to cope with the interference. The iterative interference cancellation with a channel code is effective even such a severe multipath channel because more reliable symbols can be obtained. Whereas a convolutional code has been mainly examined in the previous work, this paper considers a LDPC code. In the simulation, the performance of LDPC coded MIMO-OFDM systems with the iterative cancellation receiver is evaluated under such a severe long delay multipath channel in terms of bit-error-rate (BER) and block-error-rate (BLER). The results show that the performance can be improved by a few iterations.

## LDPC Coded Non-Recursive GMSK System with Quasi-Coherent Demodulation

- **Status**: ❌
- **Reason**: GMSK 변조+BCJR 복조 무선 기법, LDPC는 베이스라인 부호일 뿐 이식 기법 없음
- **ID**: ieee:9129629
- **Type**: conference
- **Published**: 25-28 May 
- **Authors**: Mengmeng Liu, Zhongyang Yu, Qingya Lu +2
- **PDF**: https://ieeexplore.ieee.org/document/9129629
- **Abstract**: A novel low-density parity-check (LDPC) coded Gaussian minimum shift keying (GMSK) scheme is proposed for wireless communications subject to low SNRs, limited power and spectrum resources. We first design a non-recursive GMSK modulator to alleviate the impact of error propagation. Then, a pilot-aided quasi-coherent demodulation algorithm (PA-QCDA) is derived, where a modified BCJR-based detection is used to produce the soft-output with initial and ending trellis-states being determined using the overhead-limited pilot. We choose proper parameters for the non-recursive GMSK signaling according to the trade-off of the power and spectral efficiency. Simulation results show that the proposed non-recursive GMSK system with the PA-QCDA can achieve performance similar to the LDPC coded BPSK system and can also work well in the presence of large frequency and phase offsets or burst errors.

## Performance of FDE Using Partial LDPC Coding with Double Gray Mapping for Single-Carrier LOS-MIMO

- **Status**: ❌
- **Reason**: 무선 LOS-MIMO FDE 응용, partial LDPC coding은 변조/매핑 기법, 떼어낼 NAND LDPC ECC 기법 없음
- **ID**: ieee:9128528
- **Type**: conference
- **Published**: 25-28 May 
- **Authors**: Kana Aono, Bin Zheng, Mamoru Sawahashi +1
- **PDF**: https://ieeexplore.ieee.org/document/9128528
- **Abstract**: This paper presents the bit error rate (BER) performance of frequency domain equalization (FDE) using low-density parity-check (LDPC) coding for single-carrier line-of-sight (LOS)-multiple-input multiple-output (MIMO) multiplexing. We use partial LDPC coding with double Gray mapping and collaborative decoding, which is suitable for a high coding rate such as 0.9. Computer simulation results show that partial LDPC coding decreases the required received signal-to-noise power ratio (SNR) at the bit error rate (BER) of 10-7 by approximately 1.0 dB compared to that for full LDPC coding for 256QAM in a Rummler fading channel. We show that the required received SNR at the BER of 10-7 using partial LDPC coding is decreased by more than 6.6 dB compared to that without LDPC coding even for the deep notch depth of -20dB regardless of the relationship between the notch frequencies in the direct and cross links for 2×2 LOS-MIMO in a Rummler fading channel. Therefore, we conclude that FDE using partial LDPC coding with double Gray mapping and collaborative decoding is effective in achieving a low BER for single-carrier LOS-MIMO in microwave radio backhaul channels.

## An Unequal Coding Scheme for H.265 Video Transmission

- **Status**: ❌
- **Reason**: H.265 영상 UEP 전송 응용, 표준 5G LDPC 그대로 사용, 떼어낼 ECC/디코더 신규 기법 없음 — 무선응용 특이적 제외
- **ID**: ieee:9120661
- **Type**: conference
- **Published**: 25-28 May 
- **Authors**: Yekeng Huang, Meiying Ji, Jiachen Sun +2
- **PDF**: https://ieeexplore.ieee.org/document/9120661
- **Abstract**: In this paper, we propose a new multi-level unequal error protection (UEP) by superposition transmission (referred to as ML-UEP-by-ST) coding scheme, which provides finer error protection abilities than the unequal error protection by partial superposition transmission (referred to as UEP-by-PST) coding scheme. This new coding scheme is then applied to video transmission with the H.265 standard, where a video bitstream can be regarded as a series of one or more groups. Each group consists of either a coded video sequence (CVS) and parameter sets or a CVS only. In the ML-UEP-by-ST system, each group of an H.265 video bitstream is partitioned equally into three parts, the most important part (Part A), the less important part (Part B) and the least important part (Part C). Each of these three parts is encoded by the same low-density parity check (LDPC) code as standardized in the fifth generation mobile networks(5G). The transmission is then formed by three sections. The first transmission is coded Part A, the second transmission is the superposition of coded Part B and the interleaved version of coded Part A, and the third transmission is the superposition of coded Part C and the interleaved version of the second transmission. Simulation results show that the performance of our proposed UEP scheme is better than the traditional equal error protection (EEP) scheme and the two-level UEP-by-PST scheme over both additive white Gaussian noise (AWGN) channels and Rayleigh fading channels.

## Constructions of Flexible-Size Deterministic Measurement Matrices Using Protograph LDPC Codes and Hadamard Codes

- **Status**: ❌
- **Reason**: 압축센싱용 측정행렬 구성(소스 코딩 영역), 채널 ECC 디코더/구성 아님
- **ID**: ieee:9129082
- **Type**: conference
- **Published**: 25-28 May 
- **Authors**: Kangjian Chen, Yi Fang, Guofa Cai +3
- **PDF**: https://ieeexplore.ieee.org/document/9129082
- **Abstract**: In this letter, we conduct an insightful study on protograph-low-density parity-check (PLDPC)-code-assisted deterministic measurement matrices for compressed sensing applications. As is well known, the recovery performance of conventional PLDPC sparse matrices (PLDPC-SM) will be dramatically degraded as the ratio of N to M increases, where M × N is the size of the matrices. To address the above issue, we propose a novel construction method to formulate a class of extended PLDPC-SM (EPLDPCSM) by intelligently inserting part of Hadamard matrices into the conventional PLDPC-SM. The proposed EPLDPC-SM not only can realize more flexible sizes with respect to the existing counterparts, but also can be amenable to lower coherence without costing more storage resources. Both coherence analyses and experiment results demonstrate that the proposed EPLDPC-SM are superior to the well-performing deterministic measurement matrices (i.e., PLDPCSM) and random matrices (i.e., random Gaussian matrices (R-GM) and random sparse matrices (R-SBM)) for various values of N/M1.

## Protograph-based LDPC-Hadamard Codes

- **Status**: ❌
- **Reason**: LDPC-Hadamard 연접부호로 초저율(R=0.05) Shannon-limit 접근, Hadamard 의존 특수 구조라 NAND 고전 바이너리 LDPC로 떼어낼 기법 없음
- **ID**: ieee:9120683
- **Type**: conference
- **Published**: 25-28 May 
- **Authors**: P. W. Zhang, F. C. M. Lau, C.-W. Sham
- **PDF**: https://ieeexplore.ieee.org/document/9120683
- **Abstract**: We propose a novel type of ultimate-Shannon-limit-approaching codes, namely protograph-based low-density parity-check Hadamard (PLDPC-Hadamard) codes in this paper. We also propose a systematic way of analyzing such codes using Protograph EXtrinsic Information Transfer (PEXIT) charts. Using the analytical technique we have found a code of rate about 0.05 having a theoretical threshold of -1.42dB. At a BER of $10^{-5}$, the gaps of our code to the Shannon capacity for R=0.05 and to the ultimate Shannon limit are 0.25 dB and 0.40 dB, respectively.

## Performance Comparison of Adaptive Terminal Selection Schemes for Terminal-Collaborated MIMO Reception Using Actual Received Signals

- **Status**: ❌
- **Reason**: 단말협력 MIMO 수신 단말선택 기법, LDPC 무관
- **ID**: ieee:9129404
- **Type**: conference
- **Published**: 25-28 May 
- **Authors**: Mampei Kasai, Hidekazu Murata
- **PDF**: https://ieeexplore.ieee.org/document/9129404
- **Abstract**: In terminal-collaborated multiple-input multiple-output (MIMO) reception, a base station transmits multiple signal streams to a virtual terminal with a large number of reception antennas. The virtual terminal consists of multiple mobile terminals sharing their signals with other terminals. As the number of terminals increases, the performance of terminal-collaborated MIMO reception improves. However, the overhead for inter-terminal communication also increases. If the optimum set of collaborated terminals is selected, it is possible to improve the performance of terminal-collaborated MIMO reception and reduce the aforementioned overhead. In this study, adaptive terminal selection schemes were examined using actual received signals previously stored during outdoor experiments.

## Index Modulated Polar Codes

- **Status**: ❌
- **Reason**: Polar 코드 신규 구성(IM-Polar)+SCL 디코딩, LDPC 비의존이며 떼어낼 BP 기법 없음 — 비-LDPC 제외
- **ID**: ieee:9120578
- **Type**: conference
- **Published**: 25-28 May 
- **Authors**: Yajing Deng, Shaohua Wu, Xijin Liu +3
- **PDF**: https://ieeexplore.ieee.org/document/9120578
- **Abstract**: Polar codes with short code length under successive cancellation (SC) decoding are inferior to other advanced codes of similar block length. Although more sophisticated algorithms, such as SC list (SCL) decoding and SC stack (SCS) decoding were introduced to address the problem, the complexity of these algorithms has also increased. In this paper, we first propose a novel construction of Polar codes, named index modulated Polar (IM-Polar) codes. This scheme conveys information not only by the information bits in non-frozen channels as conventional Polar codes, but also by the indices of channels, which are activated according to the incoming bit stream. Moreover, we give a specific implementation of IM-Polar codes under cyclic redundancy check (CRC) aided SCL (CA-SCL) decoding. In this implementation, repetition-assisted encoding is employed to improve the accuracy of index detection. It is shown via simulations that the proposed implementation of IM-Polar codes can provide gain of 0.2--0.3 dB over the classical CRC-aided Polar (CA-Polar) codes with code rate 0.357 and code length 128 at the bit error ratio (BER) of $10^{-4}$.

## Performance of Raptor Codes on the BIAWGN Channel in the Presence of SNR Mismatch

- **Status**: ❌
- **Reason**: Raptor 부호 SNR mismatch DE 분석. 비-LDPC fountain, BP SNR mismatch는 fountain 특이적, 이식 ECC 기법 약함
- **ID**: ieee:9120480
- **Type**: conference
- **Published**: 25-28 May 
- **Authors**: Hussein Fadhel, Amrit Kharel, Lei Cao
- **PDF**: https://ieeexplore.ieee.org/document/9120480
- **Abstract**: Accurate estimation of the channel signal to noise ratio (SNR) is essential for belief propagation (BP) decoding to operate optimally. Incorrect estimation of the channel SNR is known as SNR mismatch and can lead to serious degradation in BP decoding performance especially when a code is operating near its decoding threshold. We analyze the asymptotic performance of Raptor codes under SNR mismatch on the binary input additive white Gaussian noise (BIAWGN) channel using discretized density evolution (DDE). We provide the decoding thresholds of Raptor codes for a wide range of SNR mismatch values. Our results show that overestimation of channel SNR is slightly more detrimental than underestimation for lower levels of SNR mismatch, while, underestimation becomes more detrimental as the mismatch increases. Finally, we use DDE-based optimization to design SNR mismatch tolerant output degree distributions.

## Thresholding Quantizer Design for Mutual Information Maximization Under Output Constraint

- **Status**: ❌
- **Reason**: 상호정보 최대화 thresholding 양자기 설계(일반 채널), LDPC 무관 소스/양자화 이론 — ECC 디코더 기법 아님 제외
- **ID**: ieee:9128395
- **Type**: conference
- **Published**: 25-28 May 
- **Authors**: Thuan Nguyen, Thinh Nguyen
- **PDF**: https://ieeexplore.ieee.org/document/9128395
- **Abstract**: We consider a channel with discrete input X, a continuous noise that corrupts the input X to produce the continuous-valued output U. A thresholding quantizer is then used to quantize the continuous-valued output U to the final discrete output V. The goal is to jointly design a thresholding quantizer that maximizes the mutual information between input and quantized output I(X; V ) while minimizing a pre-specified function of the quantized output F(pV). A general dynamic programming algorithm is proposed having the time complexity O(KNM2) where N, M and K are the sizes of input X, output U and quantized output V, respectively. Moreover, we show that if F(pV) Σi=1K gi(p(vi)) where gi(.) is a convex function, p(vi) ∈ pV {pv1,..., pvK} is the probability mass function of output vi ∈ V and the channel conditional density p(u|x) satisfies the dominated condition (often true in practice), then the existing SMAWK algorithm can be applied to reduce the time complexity of the dynamic programming algorithm from O(KNM2) to O(KNM). Both theoretical and numerical results are provided to verify our contributions.

## Highly efficient TIBWB-OFDM waveform for broadband wireless communications

- **Status**: ❌
- **Reason**: TIBWB-OFDM 파형 설계, LDPC 언급 없는 무선 통신 특이 기법
- **ID**: ieee:9128826
- **Type**: conference
- **Published**: 25-28 May 
- **Authors**: Filipe Conceição, Marco Gomes, Vitor Silva +1
- **PDF**: https://ieeexplore.ieee.org/document/9128826
- **Abstract**: The Time-Interleaved Block Windowed Burst Orthogonal Frequency Division Multiplexing (TIBWB-OFDM) waveform enables to achieve greater confinement in the signal spectrum. This improves with the increase of the window roll-off since the out of band (OOB) radiation drops. However, the TIBWB-OFDM block duration also increases, which leads to a decrease in the transmission rate for a given band, limiting, therefore, the spectral efficiency gains of the system. In this paper, we propose an alternative method for TIBWB-OFDM symbol construction by allowing a partial overlap between adjacent windowed OFDM symbols that compose it. This improves the spectral efficiency at the expense of introduced interference between the signal’s blocks, that deteriorates the Bit Error Rate (BER) performance. To avoid these BER performance losses, we propose a modified receiver design that includes the cancellation of block overlapping effects in the time domain. The proposed receiver is shown to be able to achieve excellent performance, even with the strong overlapping effects of a TIBWB-OFDM system with high spectral efficiency.

## Performance Analysis of Various Waveforms and Coding Schemes in V2X Communication Scenarios

- **Status**: ❌
- **Reason**: V2X 파형/코딩 비교 서베이성, LDPC는 베이스라인 비교 대상일 뿐 신규 기법 없음 — 무선응용 제외
- **ID**: ieee:9120732
- **Type**: conference
- **Published**: 25-28 May 
- **Authors**: Waqar Anwar, Anton Krause, Atual Kumar +2
- **PDF**: https://ieeexplore.ieee.org/document/9120732
- **Abstract**: 5G and beyond communications systems need to cope with a high degree of heterogeneity in terms of services and requirements. Specially, vehicle-to-everything (V2X) use cases require ultra-reliable and low latency communications (URLLC) under harsh channel conditions. To design an optimal waveform and coding scheme for such use cases is a key challenge. Therefore, new waveforms and coding techniques are need to be investigated. In this paper, we present a comparison of several waveform candidates (orthogonal frequency-division multiplexing (OFDM), discrete Fourier transform-spread-OFDM (DFT-s-OFDM), generalized frequency division multiplexing (GFDM) and orthogonal time frequency space (OTFS)) and coding schemes (convolution, turbo, low-density priority-check (LDPC) and polar) under a common framework. We consider two metrics, i.e. maximum data rates and packet error rate, to evaluate their performance under various fading conditions. The simulation results show that OTFS outperforms all other waveforms in both frequency selective and doubly selective channels. Regarding the coding schemes, turbo codes outperforms all other coding schemes, even though difference with LDPC codes is marginal.

## How Does Channel Coding Affect the Design of Uplink SCMA Multidimensional Constellations?

- **Status**: ❌
- **Reason**: SCMA 다차원 성상도 설계에 LDPC 영향 분석, LDPC는 외부 코드로 활용될 뿐 떼어낼 신규 ECC 기법 없음 — 무선응용 제외
- **ID**: ieee:9120782
- **Type**: conference
- **Published**: 25-28 May 
- **Authors**: Monirosharieh Vameghestahbanati, Ian Marsland, Ramy H. Gohary +2
- **PDF**: https://ieeexplore.ieee.org/document/9120782
- **Abstract**: Sparse code multiple access (SCMA) is a potential non-orthogonal multiple access candidate for future wireless systems. The key performance indicators (KPIs) of uplink SCMA multidimensional constellations (MdCs) that should be considered in their design process have recently been identified in conjunction with the LTE turbo code for different channel scenarios. However, it is questionable whether the same KPIs are applicable to designing MdCs when a different error correcting code is employed. In this paper, we investigate the effect of the high-rate and low-rate 5G low density parity check (LDPC) codes on determining KPIs in designing MdCs for uplink SCMA systems under various channel scenarios. Through simulations, we show that similar results to the LTE turbo coded case occur in the presence of 5G LDPC code, with one notable exception over one specific scenario. The exception is in the performance of one MdC, which has a low number of distinct points; its performance is significantly worse than predicted by the KPIs when the low-rate 5G LDPC code is employed. This phenomenon happens due to the inherent structure of the 5G LDPC code, in which we propose a pseudorandom interleaver to rectify the problem.

## A Novel E-band Testbed for Polarization MIMO -OFDM Systems with Wideband IQ Imbalance Compensation

- **Status**: ❌
- **Reason**: E-band MIMO-OFDM 백홀 테스트베드+IQ 불균형 보상, LDPC 언급 없음 — 무선 응용 제외
- **ID**: ieee:9120730
- **Type**: conference
- **Published**: 25-28 May 
- **Authors**: D. Uchida, T. Kawaguchi, D. Yoda +6
- **PDF**: https://ieeexplore.ieee.org/document/9120730
- **Abstract**: Considerable research efforts have been made into 5G systems, in which wireless backhaul plays a key part. This paper presents a novel E-band testbed for 5G backhaul applications with wideband IQ imbalance compensation. It is based on OFDM to compensate the effect of wideband channel distortions as well as RF impairments. Moreover, line-of-sight polarization MIMO with two orthogonal polarizations is applied to enhance the data rate, which in combination with OFDM results in a simple equalization approach. In this testbed, carrier frequency offset and Tx/Rx IQ imbalance are jointly estimated and compensated. We describe how the testbed was designed. Then, we apply the IQ imbalance compensation and demonstrate that a data rate of 20 Gbps can be achieved in an actual outdoor environment distances of 900 m.

## Neural Network MIMO Detection for Coded Wireless Communication with Impairments

- **Status**: ❌
- **Reason**: 신경망 MIMO 검출기. 디텍터이지 LDPC 디코더 아님, 떼어낼 ECC 기법 없음
- **ID**: ieee:9120517
- **Type**: conference
- **Published**: 25-28 May 
- **Authors**: Omer Sholev, Haim H. Permuter, Eilam Ben-Dror +1
- **PDF**: https://ieeexplore.ieee.org/document/9120517
- **Abstract**: In this paper, a neural network based Multiple-Input-Multiple-Output (MIMO) algorithm is presented. The algorithm is specifically designed to be integrated in a coded MIMO-OFDM system, and is based upon projected gradient descent iterations. We combine our model as a part of a modern coded MIMO-OFDM system, and we compare its performance with common MIMO detectors on simulated data, as well as on field data. We also investigated our model’s performance in the presence of several common communication impairments, and demonstrated empirically its robustness. We show empirically that a single trained model is suited for the detection of both coded and uncoded data, with or without impairments, and in the presence of a wide range of tested SNR levels.

## Data-Aided LS Channel Estimation in Massive MIMO Turbo-Receiver

- **Status**: ❌
- **Reason**: Massive MIMO 채널추정 알고리즘, LDPC LLR은 부수 입력일 뿐 떼어낼 디코더/HW 기여 없음
- **ID**: ieee:9128566
- **Type**: conference
- **Published**: 25-28 May 
- **Authors**: Alexander Osinsky, Andrey Ivanov, Dmitry Lakontsev +2
- **PDF**: https://ieeexplore.ieee.org/document/9128566
- **Abstract**: In this paper, we propose a new algorithm of iterative least squared (LS) channel estimation for 64 antennas Massive Multiple Input, Multiple Output (MIMO) turbo-receiver. The algorithm employs log-likelihood ratios (LLR) of low-density parity-check (LDPC) decoder and minimum mean square error (MMSE) estimator to achieve soft data symbols. These soft data symbols are further MMSE-weighted again and combined with pilot symbols to achieve a modified LS channel estimate. The modified LS estimate is employed by the same channel estimation unit to enhance turbo-receiver performance via channel re-estimation, as a result, the proposed approach has low complexity and fits any channel estimation solution, which is quite valuable in practice. We analyze both hard and soft algorithm versions and present simulation results of 5G turbo-receiver in the 3D-UMa model of the QuaDRiGa 2.0 channel. Simulation results demonstrate up to 0. 3dB performance gain compared to the unweighted hard data symbols utilization in the LS channel re-calculation.

## A Comparison of Concatenated Polar Codes with Different Interleaving and Decoding Schemes

- **Status**: ❌
- **Reason**: 연접 polar/turbo 인터리빙·SCL 디코딩 비교, 비-LDPC 부호 중심이고 LDPC BP에 이식할 부호비의존 기법 없음
- **ID**: ieee:9118473
- **Type**: conference
- **Published**: 15-18 May 
- **Authors**: Quanyv Wang, Panpan Fu, Shouzhen Zhang
- **PDF**: https://ieeexplore.ieee.org/document/9118473
- **Abstract**: Towards the 5th generation wireless systems (5G) and beyond, polar codes have become a hot research topic in the field of communications. In our work, concatenated polar codes with different interleaving and decoding schemes are designed to improve the error performance of finite-length polar codes. In this paper, concatenated polar codes with outer BCH codes are first constructed, besides, concatenated LDPC codes and concatenated Turbo codes are also designed for comparison. At the same time, random interleaving (RI) scheme and blind interleaving (BI) scheme are proposed to construct the concatenated codes. From the simulation results of this paper, we can see that the bit error rate (BER) performance of concatenated codes using BI scheme is better than that of concatenated codes using RI scheme. Furthermore, the BER performance of concatenated polar codes outperforms that of concatenated LDPC codes, but not as good as that of concatenated Turbo codes. To improve the BER performance of concatenated polar codes, we adopt the CRC Aided Successive Cancellation List (CA-SCL) decoding scheme instead of the Successive Cancellation (SC) decoding scheme for inner polar decoding. The results of our study indicate that the BER performance of concatenated polar codes with CA-SCL outperforms that of concatenated polar codes with SC. In addition to this, with the same CRC code length, increasing the list size can improve the decoding performance of CA-SCL. However, there is also a bad side: the decoding complexity of CA-SCL increases rapidly as the list size increases. On the other hand, with the same list size, increasing the CRC code length adversely deteriorates the decoding performance of CA-SCL.

## Adding Artificial Noise for Dynamic Code Rate Matching in Continuous-Variable Quantum Key Distribution

- **Status**: ❌
- **Reason**: CV-QKD reconciliation 코드율 매칭에 인공잡음 추가, 채널 ECC 아닌 정보조정이며 떼어낼 디코더/HW 기법 없음
- **ID**: ieee:9192221
- **Type**: conference
- **Published**: 10-15 May 
- **Authors**: Sören Kreinberg, Igor Koltchanov, André Richter
- **PDF**: https://ieeexplore.ieee.org/document/9192221
- **Abstract**: CV-QKD over long distances requires high reconciliation efficiencies, hence matching error correction code rate vs. SNR. For time-varying quantum channels, we achieve this by adding a controlled amount of digital noise to the measured data.

## Generation and Heterodyne Detection of a 2-μm-Band 16-QAM Signal Based on Inter-Band Wavelength Conversion

- **Status**: ❌
- **Reason**: 2um 16-QAM 광전송에 표준 LDPC를 베이스라인으로 사용, 새 디코더/구성/HW 기여 없음
- **ID**: ieee:9193613
- **Type**: conference
- **Published**: 10-15 May 
- **Authors**: Yong Liu, Deming Kong, Zhengqi Ren +7
- **PDF**: https://ieeexplore.ieee.org/document/9193613
- **Abstract**: We demonstrate the generation and self-heterodyne detection of a 2-μm-band 32-Gbit/s line-rate 16-QAM signal based on inter-band wavelength conversion in an AlGaAsOI nanowaveguide. Error-free performance is achieved using LDPC codes with 33% overhead.

## PS-64QAM-OFDM THz Photonic-Wireless Transmission with 2×300 Gbit/s Line Rate

- **Status**: ❌
- **Reason**: THz 무선 전송/64QAM-OFDM 데모, LDPC 언급 없음, 떼어낼 ECC 기법 없음
- **ID**: ieee:9192750
- **Type**: conference
- **Published**: 10-15 May 
- **Authors**: Shi Jia, Lu Zhang, Shiwei Wang +8
- **PDF**: https://ieeexplore.ieee.org/document/9192750
- **Abstract**: THz photonic-wireless transmission of a record 612.65 Gbit/s line rate is successfully demonstrated in the 320-380-GHz band by employing THz orthogonal polarization dual-antenna, PS-64QAM-OFDM modulation and advanced nonlinear-digital reception techniques.

## LDPC Code Classification using Convolutional Neural Networks

- **Status**: ❌
- **Reason**: CNN으로 LDPC 코드 분류(식별) — ECC 디코딩/구성/HW가 아닌 코드 인식 문제. 이식 기법 없음
- **ID**: ieee:9114915
- **Type**: conference
- **Published**: 1-2 May 20
- **Authors**: Bradley Comar
- **PDF**: https://ieeexplore.ieee.org/document/9114915
- **Abstract**: This paper discusses the performance of an LDPC code classification system. Three randomly generated binary LDPC codes are created, all having the same codeword size and coderate. Multi-scaled convolutional neural networks are employed to classify codeword streams. High classification accuracies are obtained with relatively small networks.
