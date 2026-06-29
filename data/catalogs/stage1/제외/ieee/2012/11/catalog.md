# IEEE Xplore — 2012-11


## Spectral Method for Quasi-Cyclic Code Analysis

- **Status**: ❌
- **Reason**: QC 부호의 BCH bound 일반화는 순수 최소거리 이론 bound로 디코더/HW/구성으로 안 이어짐
- **ID**: ieee:6313583
- **Type**: journal
- **Published**: November 2
- **Authors**: P. Semenov, P. Trifonov
- **PDF**: https://ieeexplore.ieee.org/document/6313583
- **Abstract**: A generalization of the BCH bound to the case of quasi-cyclic codes is proposed. The new approach is based on eigenvalues of matrix polynomials. This results in improved minimum distance estimates compared to the existing bounds.

## Maximum Likelihood Erasure Decoding of LDPC Codes: Pivoting Algorithms and Code Design

- **Status**: ❌
- **Reason**: erasure 채널 ML 디코딩(pivoting)·erasure용 코드 설계로 NAND 채널 ECC와 무관, 떼어낼 바이너리 LDPC BP 기법 없음
- **ID**: ieee:6266770
- **Type**: journal
- **Published**: November 2
- **Authors**: Enrico Paolini, Gianluigi Liva, Balazs Matuz +1
- **PDF**: https://ieeexplore.ieee.org/document/6266770
- **Abstract**: This paper investigates efficient maximum-likelihood (ML) decoding of low-density parity-check (LDPC) codes over erasure channels. A set of algorithms, referred to as pivoting algorithms, is developed. The aim is to limit the average number of pivots (or reference variables) from which all the other erased symbols are recovered iteratively. The suggested algorithms exhibit different trade-offs between complexity of the pivoting phase and average number of pivots. Moreover, a systematic procedure to design LDPC code ensembles for efficient ML decoding is proposed. Numerical results illustrate that the designed LDPC codes achieve a near-optimum performance (very close to the Singleton bound, at least down to a codeword error rate level 10-8) with an affordable decoding complexity. For one of the presented codes and algorithms, a software implementation has been developed which is capable to provide data rates above 1.5 Gbps on a commercial computing platform.

## Multi-Input Multi-Output Deletion Channel

- **Status**: ❌
- **Reason**: MIMO deletion 채널 동기화 검출기(marker code)로 통신응용 특이적, LDPC는 부수 요소이고 떼어낼 ECC 기법 없음
- **ID**: ieee:6317096
- **Type**: journal
- **Published**: November 2
- **Authors**: Feng Wang, Tolga M. Duman
- **PDF**: https://ieeexplore.ieee.org/document/6317096
- **Abstract**: We describe a new channel model suitable in certain applications, namely the multi-input multi-output (MIMO) deletion channel. This channel models the scenarios where multiple transmitters and receivers suffering from synchronization errors are employed. We then consider a coding scheme over such channels based on a serial concatenation of a low-density parity check (LDPC) code, a marker code and a layered space-time code. We design two detectors operating at the bit level which jointly achieve synchronization for the deletion channel (with the help of the marker code) and detection for the MIMO channel. Utilizing the proposed detector together with an LDPC code with powerful error-correction capabilities, we demonstrate that reliable transmission over a MIMO deletion channel is feasible.

## Polar Codes for Cooperative Relaying

- **Status**: ❌
- **Reason**: polar 부호 자체 구성(relay/source compression), LDPC BP에 이식 가능한 디코더 기법 없어 원칙 제외
- **ID**: ieee:6276210
- **Type**: journal
- **Published**: November 2
- **Authors**: Ricardo Blasco-Serrano, Ragnar Thobaben, Mattias Andersson +2
- **PDF**: https://ieeexplore.ieee.org/document/6276210
- **Abstract**: We consider the symmetric discrete memoryless relay channel with orthogonal receiver components and show that polar codes are suitable for decode-and-forward and compress-and-forward relaying. In the first case we prove that polar codes are capacity achieving for the physically degraded relay channel; for stochastically degraded relay channels our construction provides an achievable rate. In the second case we construct sequences of polar codes that achieve the compress-and-forward rate by nesting polar codes for source compression into polar codes for channel coding. In both cases our constructions inherit most of the properties of polar codes. In particular, the encoding and decoding algorithms and the bound on the block error probability O(2-Nβ) which holds for any 0<;β<;1/2.

## Distributed Algorithms for Spectrum Access in Cognitive Radio Relay Networks

- **Status**: ❌
- **Reason**: 인지무선 스펙트럼 접근 분산 알고리즘으로 LDPC/ECC와 무관
- **ID**: ieee:6331685
- **Type**: journal
- **Published**: November 2
- **Authors**: Manohar Shamaiah, Sang Hyun Lee, Sriram Vishwanath +1
- **PDF**: https://ieeexplore.ieee.org/document/6331685
- **Abstract**: We develop distributed algorithms for efficient spectrum access strategies in cognitive radio relay networks. In our setup, primary users permit secondary users access to the resource (spectrum) as long as they consent to aiding the primary users as relays in addition to transmitting their own data. Given a pool of primary and secondary users, we desire to optimize overall network utility by determining the best configuration/pairing of secondary users with primary users. This optimization can be stated in a form similar to the maximum weighted matching problem. Given such formulation, we develop an algorithm based on affinity propagation technique that is completely distributed in its structure. We demonstrate the convergence of the developed algorithm and show that it performs close to the optimal centralized scheme.

## Turbo Equalization Effect for Nonbinary LDPC Code in BPM R/W Channel

- **Status**: ❌
- **Reason**: GF(2^8) 비이진 LDPC turbo equalization(BPM 채널) — non-binary LDPC 제외
- **ID**: ieee:6332861
- **Type**: journal
- **Published**: Nov. 2012
- **Authors**: Yasuaki Nakamura, Yasuhisa Bandai, Yoshihiro Okamoto +3
- **PDF**: https://ieeexplore.ieee.org/document/6332861
- **Abstract**: It is expected for the nonbinary low-density parity-check (LDPC) coding and iterative decoding system to introduce the turbo equalization in order to enhance the error correction ability in the bit-patterned medium (BPM) R/W channel. In this paper, we investigate the effect of the turbo equalization on the bit-error rate (BER) performance of nonbinary LDPC coding and iterative decoding system over Galois filed GF(28) in BPM R/W channel with write-error at an areal recording density of 2 Tbit/inch2 considering the coding rate loss. The performance of turbo equalization using the nonbinary LDPC coding and iterative decoding system is evaluated by computer simulation, and it is compared to that without turbo equalization. The results show that the nonbinary LDPC and iterative decoding system with the turbo equalization has the larger write-margin compared to that without turbo equalization.

## Performance of Low-Density Parity Check Codes With Parity Encoded by (1, 7) Run-Length Limited Code for Perpendicular Magnetic Recording

- **Status**: ❌
- **Reason**: PMR용 (1,7)RLL+LDPC 패리티 결합 변조코딩 — Viterbi trellis 채널 특이적, 떼어낼 LDPC 디코더·구성 기법 없음
- **ID**: ieee:6332803
- **Type**: journal
- **Published**: Nov. 2012
- **Authors**: Jinyoung Kim, Jaejin Lee, Joohyun Lee
- **PDF**: https://ieeexplore.ieee.org/document/6332803
- **Abstract**: Maximum transition run (MTR) codes have recently been applied for perpendicular magnetic recording because of their high code rate. At the same time, the (1, 7) run-length limited (RLL) code, which increases the minimum distance of data transition, has not been applied due to a code rate that is lower than MTR codes. Therefore, in order to receive the advantages of both codes when low-density parity check (LDPC) codes are applied, this paper proposes an LDPC coding scheme with parity encoded by (1, 7) RLL code. This will increase the performance of LDPC codes and minimize the loss of code rate with MTR-coded user data in the perpendicular magnetic recording channel. The Viterbi trellis is easily modified by different constraints of MTR and (1, 7) RLL codes. Simulation results show that MTR-coded user data with (1, 7) RLL-coded LDPC parity performs approximately 0.3 dB better than MTR-coded user data with parity. It also performs better regardless of various user bit densities.

## A Nonbinary LDPC Decoder Architecture With Adaptive Message Control

- **Status**: ❌
- **Reason**: 비이진(nonbinary) LDPC 디코더 아키텍처로 비이진 LDPC는 제외 대상
- **ID**: ieee:6018325
- **Type**: journal
- **Published**: Nov. 2012
- **Authors**: Weiguo Tang, Jie Huang, Lei Wang +1
- **PDF**: https://ieeexplore.ieee.org/document/6018325
- **Abstract**: A new decoder architecture for nonbinary low-density paritycheck (LDPC) codes is presented in this paper to reduce the hardware operational complexity in VLSI implementations. The low decoding complexity is achieved by employing adaptive message control (AMC) that dynamically trims the message length of belief information to reduce the amount of memory accesses and arithmetic operations. To implement the proposed AMC, we develop the architecture of a horizontal sequential nonbinary LDPC decoder. Key components in the architecture have been designed with the consideration of variable message lengths to leverage the benefit of the proposed AMC. Simulation results demonstrate that the proposed nonbinary LDPC decoder architecture can significantly reduce hardware operations and power consumption as compared with existing work with negligible performance degradation.

## High-Throughput Efficient Non-Binary LDPC Decoder Based on the Simplified Min-Sum Algorithm

- **Status**: ❌
- **Reason**: 비이진(NB-LDPC) min-sum 디코더 아키텍처 — non-binary LDPC는 제외 대상
- **ID**: ieee:6177696
- **Type**: journal
- **Published**: Nov. 2012
- **Authors**: Xiaoheng Chen, Chung-Li Wang
- **PDF**: https://ieeexplore.ieee.org/document/6177696
- **Abstract**: Non-binary low-density parity-check (NB-LDPC) codes are robust to various channel impairments. The excessive computational complexity and memory usage of the existing decoder designs are considerably expensive for practical applications. Based on a newly proposed simplified min-sum algorithm, which only has 0.05-0.1 dB performance loss against the sum-product algorithm, a highly efficient decoder architecture is developed. Compared with the existing works, our design has three advantages. First, the design increases the parallelism and throughput of the decoder by three to four times. The implementation results for the decoder show high throughput of 64 Mbps at 15 iterations. Second, this design saves memory usage by 38% to 76%. Third, this design shows 2.64 × area efficiency improvement even compared with the most state-of-the-art design.

## Dynamic Power Management for the Iterative Decoding of Turbo Codes

- **Status**: ❌
- **Reason**: turbo 디코더 동적 전력관리로 비-LDPC 부호이고 부호 비의존적 BP 이식 기법 아님
- **ID**: ieee:6042349
- **Type**: journal
- **Published**: Nov. 2012
- **Authors**: Erick Amador, Raymond Knopp, Renaud Pacalet +1
- **PDF**: https://ieeexplore.ieee.org/document/6042349
- **Abstract**: Turbo codes are presently ubiquitous in the context of mobile wireless communications among other application domains. A decoder for such codes is typically the most power intensive component in the baseband processing chain of a wireless receiver. The iterative nature of these decoders represents a dynamic workload. This brief presents a dynamic power management policy for these decoders. An algorithm is proposed to tune a power manageable decoder according to a prediction of the workload involved within the decoding task. By reclaiming the timing slack left when operating the decoder at a high power mode, the proposed algorithm continuously looks for opportunities to switch to a lower power mode that guarantees the task completion. We apply this technique to an long term evolution Turbo decoder and explore the feasibility of a VLSI implementation on a CMOS technology of 65 nm. Energy savings of up to 54% were achieved with a relatively low loss in error-correction performance.

## Low-Complexity Reliability-Based Message-Passing Decoder Architectures for Non-Binary LDPC Codes

- **Status**: ❌
- **Reason**: 비이진(NB-)LDPC 디코더 아키텍처로 비이진 LDPC는 제외 대상
- **ID**: ieee:6018324
- **Type**: journal
- **Published**: Nov. 2012
- **Authors**: Xinmiao Zhang, Fang Cai, Shu Lin
- **PDF**: https://ieeexplore.ieee.org/document/6018324
- **Abstract**: Non-binary low-density parity-check (NB-LDPC) codes can achieve better error-correcting performance than their binary counterparts at the cost of higher decoding complexity when the codeword length is moderate. The recently developed iterative reliability-based majority-logic NB-LDPC decoding has better performance-complexity tradeoffs than previous algorithms. This paper first proposes enhancement schemes to the iterative hard reliability-based majority-logic decoding (IHRB-MLGD). Compared to the IHRB algorithm, our enhanced (E-)IHRB algorithm can achieve significant coding gain with small hardware overhead. Then low-complexity partial-parallel NB-LDPC decoder architectures are developed based on these two algorithms. Many existing NB-LDPC code construction methods lead to quasi-cyclic or cyclic codes. Both types of codes are considered in our design. Moreover, novel schemes are developed to keep a small proportion of messages in order to reduce the memory requirement without causing noticeable performance loss. In addition, a shift-message structure is proposed by using memories concatenated with variable node units to enable efficient partial-parallel decoding for cyclic NB-LDPC codes. Compared to previous designs based on the Min-max decoding algorithm, our proposed decoders have at least tens of times lower complexity with moderate coding gain loss.

## Boolean Functions Over Nano-Fabrics: Improving Resilience Through Coding

- **Status**: ❌
- **Reason**: 나노회로 Boolean 함수 신뢰성 코딩(don't-care 활용 CSP/트리 DP), LDPC ECC 디코더·구성·HW 이식 기법 없음
- **ID**: ieee:6042351
- **Type**: journal
- **Published**: Nov. 2012
- **Authors**: Sang Hyun Lee, Sriram Vishwanath
- **PDF**: https://ieeexplore.ieee.org/document/6042351
- **Abstract**: This paper determines mechanisms to mitigate errors when implementing Boolean functions in nano-circuits. Nano-fabrics are expected to have high defect rates as atomic variations directly impact such materials. This paper develops a coding mechanism that uses a combination of cheap, but unreliable nano-device as the main function and reliable, but expensive CMOS devices to implement the coding mechanism. The unique feature of this paper is that it exploits the don't-cares that naturally occur in Boolean functions to construct better codes. The reliable Boolean function problem is cast as a constraint satisfaction problem and then solved using a tree-based dynamic programming algorithm. (Here, the word “dynamic programming” is used in the same sense as computer-science literature, i.e., and as an efficient search algorithm over trees.)

## On Compression of Data Encrypted With Block Ciphers

- **Status**: ❌
- **Reason**: 블록암호 암호문 압축(소스코딩/보안) — 채널 ECC 아님
- **ID**: ieee:6253260
- **Type**: journal
- **Published**: Nov. 2012
- **Authors**: Demijan Klinc, Carmit Hazay, Ashish Jagmohan +2
- **PDF**: https://ieeexplore.ieee.org/document/6253260
- **Abstract**: This paper investigates compression of data encrypted with block ciphers, such as the Advanced Encryption Standard. It is shown that such data can be feasibly compressed without knowledge of the secret key. Block ciphers operating in various chaining modes are considered and it is shown how compression can be achieved without compromising security of the encryption scheme. Further, it is shown that there exists a fundamental limitation to the practical compressibility of block ciphers when no chaining is used between blocks. Some performance results for practical code constructions used to compress binary sources are presented.

## Modeling of Writing Process for Two-Dimensional Magnetic Recording and Performance Evaluation of Two-Dimensional Neural Network Equalizer

- **Status**: ❌
- **Reason**: TDMR 2D 신경망 이퀄라이저 — LDPC는 베이스라인 시스템, 떼어낼 디코더/코드 기법 없음(이퀄라이저가 핵심)
- **ID**: ieee:6333011
- **Type**: journal
- **Published**: Nov. 2012
- **Authors**: Masato Yamashita, Yoshihiro Okamoto, Yasuaki Nakamura +6
- **PDF**: https://ieeexplore.ieee.org/document/6333011
- **Abstract**: Modeling of a simple writing process considering intergranular exchange fields and magnetostatic interaction fields between grains is studied for two-dimensional magnetic recording (TDMR). A new designing method of a two-dimensional neural network equalizer with a mis-equalization suppression function (2D-NNEMS) for TDMR is also proposed. The bit-error rate (BER) performance of a low-density parity-check coding and iterative decoding system with the designed 2D-NNEMS is obtained via computer simulation using a read/write channel model employing the proposed writing process under TDMR specifications of 4 Tb/in2, and it is compared with those for one- and two-dimensional finite impulse response equalizers (FIREs). It is clarified that the BER performance for the designed 2D-NNEMS is far superior to those for the FIREs.

## A digital audio broadcasting system using short length QC-LDPC

- **Status**: ❌
- **Reason**: 오디오 방송용 short QC-LDPC를 표준 구성으로 적용+EXIT 분석만, 새 코드설계/디코더 기여 없음
- **ID**: ieee:6511352
- **Type**: conference
- **Published**: 9-11 Nov. 
- **Authors**: Jilong Li, Na Di, Peng Gao +2
- **PDF**: https://ieeexplore.ieee.org/document/6511352
- **Abstract**: This paper presents a system designed for digital audio broadcasting. Short length Quasi Cyclic Low-density parity-check (QC-LDPC) codes is constructed and used in the designed broadcasting system. EXIT chart analysis proves that the QC-LDPC converges fast. In contrast to convolutional code, the LDPC code has no more computation operations and achieves better error performance in simulation. Short length QC-LDPC is an appropriate selection for audio broadcasting system.

## Coded cooperation with non-binary codes for wireless networks

- **Status**: ❌
- **Reason**: 비이진 NB-LDPC(GF(q)) 분산 협력부호, 비이진 LDPC는 제외 대상
- **ID**: ieee:6511379
- **Type**: conference
- **Published**: 9-11 Nov. 
- **Authors**: Changcai Han, Si Li
- **PDF**: https://ieeexplore.ieee.org/document/6511379
- **Abstract**: A novel coded cooperation scheme based on distributed non-binary low-density parity-check (NB-LDPC) codes is proposed to jointly transmit the data of two independent sources to a common destination aided by two potential relays. Specifically, the source data are broadcasted by each source node independently and then jointly processed in the high order Galois fields at relay nodes. Finally, the destination node forms the data from sources and relays as an NB-LDPC code and performs iterative decoding. In the proposed scheme, the source nodes and relay nodes have low complexity, for the encoding and transmission of the NB-LDPC codes are implemented in a distributed manner by multiple nodes located at different sites. The distributed coding scheme with iterative decoding can obtain the diversity gain and coding gain simultaneously, and thus significant performance gain is achieved compared with the non-cooperation scheme.

## Performance of polar codes on wireless communication channels

- **Status**: ❌
- **Reason**: polar 부호의 무선채널 성능/Bhattacharyya 파라미터 구성 논문, LDPC BP에 이식할 부호-비의존 디코더 기법 없음
- **ID**: ieee:6511367
- **Type**: conference
- **Published**: 9-11 Nov. 
- **Authors**: Peng Shi, Wenjuan Tang, Shengmei Zhao +1
- **PDF**: https://ieeexplore.ieee.org/document/6511367
- **Abstract**: Polar codes are a class of codes proposed currently, which can achieve the capacity of binary symmetric channel with low encoding and decoding algorithm. By generalizing the definition of Bhattacharyya parameter in discrete memoryless channel, we discuss the performance of polar codes on wireless communication channels in this paper. We present the special expressions of the parameters for continuous channels (Gaussian and Rayleigh fading channels), including the recursive formulas and the initial values, and we discuss the construction of polar codes for Gaussian and Rayleigh fading channels. We analyze the application of polar codes with the defined parameter over Rayleigh fading channel by transmitting image signals. The simulation results show that polar codes have better performance than that of low density parity-check codes (LDPC) codes with the same simulation condition. It is shown that polar codes will be a good candidate for wireless communication channels.

## A practical compress-and-forward relay scheme based on superposition coding

- **Status**: ❌
- **Reason**: 중계 CF 양자화/superposition coding 소스코딩(Wyner-Ziv) 기법, 채널 ECC LDPC 기법 아님
- **ID**: ieee:6511396
- **Type**: conference
- **Published**: 9-11 Nov. 
- **Authors**: Yang Liu, Wenbo Xu, Kai Niu +2
- **PDF**: https://ieeexplore.ieee.org/document/6511396
- **Abstract**: Compress and forward (CF) is one of the protocols in cooperative communication and has drawn much attention. In CF scheme, the relay compresses and transmits the received signals to the destination, where Wyner-Ziv coding is considered as an efficient way to compress the signal with side information available. Since the current research of superposition coding for Wyner-Ziv problem only remains in theory, we design a practical CF scheme in half-duplex mode by using the technique of superposition coding and provide specific coding strategy for it. The relay compresses the received signal by the quantization method based on superposition coding, and then the destination performs a joint decoding to recover the original message. Simulations show that our proposed scheme outperforms the conventional CF scheme with scalar quantization at the relay. This coding strategy can be easily extended to the scenarios of fading channels, which are more practical in wireless communication.

## Hybrid multidimensional dynamic optical networking based on adaptive LDPC-coded mode-multiplexed CO-OFDM

- **Status**: ❌
- **Reason**: 광네트워크 mode-multiplexed CO-OFDM 응용; 적응형 LDPC 부수 언급, 떼어낼 기법 없음
- **ID**: ieee:6510811
- **Type**: conference
- **Published**: 7-10 Nov. 
- **Authors**: Ivan B. Djordjevic, Ding Zou, Milorad Cvijetic
- **PDF**: https://ieeexplore.ieee.org/document/6510811
- **Abstract**: Spatial-MIMO combined with multiband-OFDM will lead to significant improvement in aggregate throughput of optical networks. In this paper, we describe how spatial and spectral domains can be used to enable hybrid multidimensional, dynamic, elastic optical networking based on adaptive LDPC-coded mode-multiplexed CO-OFDM.

## Bandwidth-efficient LDPC coded CO-OFDM for 1-Tb/s superchannel 8000-km SSMF transmission

- **Status**: ❌
- **Reason**: 1Tb/s 광전송 성능 평가; LDPC 부호화 부수 언급, 신규 디코더·구성·HW 없음
- **ID**: ieee:6511023
- **Type**: conference
- **Published**: 7-10 Nov. 
- **Authors**: Zhixue He, Ivan B. Djordjevic, Wu Liu +5
- **PDF**: https://ieeexplore.ieee.org/document/6511023
- **Abstract**: We evaluate the 1-Tb/s CO-OFDM transmission performance using LDPC-coded 8-QAM and 8-PSK. Equipped with improvement in OSNR sensitivity, we successfully demonstrate 1 Tb/s CO-OFDM over 8000-km SSMF transmission at spectral efficiency of 3.3 bit/s/Hz.

## Novel blind identification of LDPC codes using average LLR of syndrome a posteriori probability

- **Status**: ❌
- **Reason**: 블라인드 LDPC 인코더 식별(인지무선)로 디코더/코드설계/HW가 아닌 식별 문제, 떼어낼 ECC 기법 없음
- **ID**: ieee:6425150
- **Type**: conference
- **Published**: 5-8 Nov. 2
- **Authors**: Tian Xia, Hsiao-Chun Wu
- **PDF**: https://ieeexplore.ieee.org/document/6425150
- **Abstract**: Blind signal processing methods have been very popular recently since they can play crucial roles in the prevalent cognitive radio research. Blind encoder identification has drawn immense research interest lately. In this paper, we make the first-ever attempt to tackle the blind low-density parity-check (LDPC) encoder identification for binary phase-shift keying (BPSK) signals. We propose a novel blind identification system which consists of three components, namely EM (expectation-maximization) estimator for signal amplitude and noise variance, LLR (log-likelihood ratio) estimator for syndrome a posteriori probabilities, and maximum average LLR detector. Monte Carlo simulation results demonstrate that our proposed new blind LDPC encoder identification scheme is very promising even for harsh channel environments with low signal-to-noise ratios.

## The synthesis of complex arithmetic computation on stochastic bit streams using sequential logic

- **Status**: ❌
- **Reason**: stochastic bit stream 산술연산용 FSM 합성으로 LDPC ECC와 무관
- **ID**: ieee:6386710
- **Type**: conference
- **Published**: 5-8 Nov. 2
- **Authors**: Peng Li, David J. Lilja, Weikang Qian +2
- **PDF**: https://ieeexplore.ieee.org/document/6386710
- **Abstract**: The paradigm of logical computation on stochastic bit streams has several key advantages compared to deterministic computation based on binary radix, including error-tolerance and low hardware area cost. Prior research has shown that sequential logic operating on stochastic bit streams can compute non-polynomial functions, such as the tanh function, with less energy than conventional implementations. However, the functions that can be computed in this way are quite limited. For example, high order polynomials and non-polynomial functions cannot be computed using prior approaches. This paper proposes a new finite-state machine (FSM) topology for complex arithmetic computation on stochastic bit streams. It describes a general methodology for synthesizing such FSMs. Experimental results show that these FSM-based implementations are more tolerant of soft errors and less costly in terms of the area-time product that conventional implementations.

## Efficient EMS decoding for non-binary LDPC codes

- **Status**: ❌
- **Reason**: 비이진 NB-LDPC EMS 디코딩 — 비이진 LDPC는 제외 대상
- **ID**: ieee:6407110
- **Type**: conference
- **Published**: 4-7 Nov. 2
- **Authors**: Leixin Zhou, Jin Sha, Zhongfeng Wang
- **PDF**: https://ieeexplore.ieee.org/document/6407110
- **Abstract**: Non-binary low-density parity-check (NB-LDPC) codes are an extension of binary LDPC codes with significantly better performance when the code length is moderate. Previously, forward-backward schemes are used to implement check node processing, which need large memory. In this paper, a novel approach is proposed for EMS NB-LDPC decoding. Compared to EMS decoding algorithm, the message memory and the average number of iterations have been reduced. Also, the overall decoder architecture is proposed.

## Parallel nonbinary LDPC decoding on GPU

- **Status**: ❌
- **Reason**: 비이진 GF(q) LDPC Min-Max 디코딩 GPU 구현으로 제외 대상
- **ID**: ieee:6489229
- **Type**: conference
- **Published**: 4-7 Nov. 2
- **Authors**: Guohui Wang, Hao Shen, Bei Yin +3
- **PDF**: https://ieeexplore.ieee.org/document/6489229
- **Abstract**: Nonbinary Low-Density Parity-Check (LDPC) codes are a class of error-correcting codes constructed over the Galois field GF(q) for q > 2. As extensions of binary LDPC codes, nonbinary LDPC codes can provide better error-correcting performance when the code length is short or moderate, but at a cost of higher decoding complexity. This paper proposes a massively parallel implementation of a nonbinary LDPC decoding accelerator based on a graphics processing unit (GPU) to achieve both great flexibility and scalability. The implementation maps the Min-Max decoding algorithm to GPU's massively parallel architecture. We highlight the methodology to partition the decoding task to a heterogeneous platform consisting of the CPU and GPU. The experimental results show that our GPU-based implementation can achieve high throughput while still providing great flexibility and scalability.

## Sequential decoding of non-binary LDPC codes on graphics processing units

- **Status**: ❌
- **Reason**: 비이진(GF(q)) LDPC 디코딩으로 제외 대상
- **ID**: ieee:6489227
- **Type**: conference
- **Published**: 4-7 Nov. 2
- **Authors**: David L. Romero, Nicholas B. Chang
- **PDF**: https://ieeexplore.ieee.org/document/6489227
- **Abstract**: Non-binary low-density parity-check (LDPC) codes have been shown to attain near capacity error correcting performance in noisy wireless communication channels. It is well known that these codes require a very large number of operations per-bit to decode. This high computational complexity along with a parallel decoder structure makes graphics processing units (GPUs) an attractive platform for acceleration of the decoding algorithm. The seemingly random memory access patterns associated with decoding are generally beneficial to error-correcting performance but present a challenge to designers who want to leverage the computational capabilities of the GPU. In this paper we describe the design of an efficient decoder implementation based on GPUs and a corresponding set of powerful non-binary LDPC codes. Using the belief propagation algorithm with a sequential message updating scheme it is shown that we are able to exploit parallelism inherent in the decoding algorithm while decreasing the number of decoding iterations required for convergence.

## Improved modeling of the correlation between continuous-valued sources in LDPC-based DSC

- **Status**: ❌
- **Reason**: 분산 소스코딩(DSC)·Slepian-Wolf 상관모델링으로 채널 ECC가 아님, 떼어낼 디코더 기법 없음
- **ID**: ieee:6489314
- **Type**: conference
- **Published**: 4-7 Nov. 2
- **Authors**: Mojtaba Vaezi, Fabrice Labeau
- **PDF**: https://ieeexplore.ieee.org/document/6489314
- **Abstract**: Accurate modeling of the correlation between the sources plays a crucial role in the efficiency of distributed source coding (DSC) systems. This correlation is commonly modeled in the binary domain by using a single binary symmetric channel (BSC), both for binary and continuous-valued sources. We show that “one” BSC cannot accurately capture the correlation between continuous-valued sources; a more accurate model requires “multiple” BSCs, as many as the number of bits used to represent each sample. We incorporate this new model into the DSC system that uses low-density parity-check (LDPC) codes for compression. The standard Slepian-Wolf LDPC decoder requires a slight modification so that the parameters of all BSCs are integrated in the log-likelihood ratios (LLRs). Further, using an interleaver the data belonging to different bit-planes are shuffled to introduce randomness in the binary domain. The new system has the same complexity and delay as the standard one. Simulation results prove the effectiveness of the proposed model and system.

## Non-binary coded modulation and iterative detection for high spectral efficiency in MIMO

- **Status**: ❌
- **Reason**: 비이진 LDPC coded modulation for MIMO — 비이진 LDPC는 제외 대상
- **ID**: ieee:6489046
- **Type**: conference
- **Published**: 4-7 Nov. 2
- **Authors**: Nicholas B. Chang, David L. Romero
- **PDF**: https://ieeexplore.ieee.org/document/6489046
- **Abstract**: Non-binary low density parity check codes (LDPC) have been shown to outperform their binary counterparts and attain the best-known performance among error-correction codes. At the same time, it has also been established that wireless communication using multiple-input multiple-output (MIMO) schemes dramatically increases system capacity and reliability when information symbols are appropriately coded and modulated across transmit antennas. Recent works have studied techniques for applying non-binary LDPC codes to MIMO systems and demonstrated near-capacity performance. However, the constellation sizes in the proposed approaches are limited by the Galois field (GF) size of the non-binary LDPC code, thus limiting the maximum spectral efficiency of the proposed joint modulation-coding approaches. In practice, the GF size may be limited by computational complexity reasons but high spectral efficiencies are desired. Thus, we study iterative coded modulation based techniques for applying non-binary LDPC codes to higher order modulations. These methods have been well-studied for binary codes but not for non-binary codes. It is demonstrated that performance of the technique is dependent on the mapping of GF symbols to constellations, but applying the appropriate mapping attains near-capacity performance. To reduce the error floor region for smaller field sizes, while maintaining steep waterfall curves, we combine a nonbinary-based accumulator with a parallel concatenated coding scheme.

## Random access on graphs: A survey and new results

- **Status**: ❌
- **Reason**: coded slotted ALOHA 랜덤액세스 서베이로 LDPC가 베이스라인, 신규 디코더·구성·HW 기여 없음
- **ID**: ieee:6489332
- **Type**: conference
- **Published**: 4-7 Nov. 2
- **Authors**: Enrico Paolini, Gianluigi Liva, Marco Chiani
- **PDF**: https://ieeexplore.ieee.org/document/6489332
- **Abstract**: This paper overviews the recently proposed coded slotted ALOHA (CSA) random access scheme and illustrates some new results in this area. In CSA, a randomly picked linear block code is employed by each user to encode segments of its bursts prior to transmission, where the choice of the code is performed with no coordination with the other users. On the receiver side iterative interference cancellation combined with decoding of the local codes is performed to recover from collisions. This process may be represented as an iterative decoding algorithm over a sparse bipartite graph.

## Content-assisted file decoding for nonvolatile memories

- **Status**: ❌
- **Reason**: 콘텐츠(텍스트 통계 redundancy) 기반 디코딩, 소스코딩 결합 — 채널 LDPC ECC 기법 아님
- **ID**: ieee:6489154
- **Type**: conference
- **Published**: 4-7 Nov. 2
- **Authors**: Yue Li, Yue Wang, Anxiao Jiang +1
- **PDF**: https://ieeexplore.ieee.org/document/6489154
- **Abstract**: Nonvolatile memories (NVMs) such as flash memories play a significant role in meeting the data storage requirements of today's computation activities. The rapid increase of storage density for NVMs however brings reliability issues due to closer alignment of adjacent cells on chip, and more levels that are programmed into a cell. We propose a new method for error correction, which uses the random access capability of NVMs and the redundancy that inherently exists in information content. Although it is theoretically possible to remove the redundancy via data compression, existing source coding algorithms do not remove all of it for efficient computation. We propose a method that can be combined with existing storage solutions for text files, namely content-assisted decoding. Using the statistical properties of words and phrases in the text of a given language, our decoder identifies the location of each subcodeword representing some word in a given input noisy codeword, and flips the bits to compute a most likely word sequence. The decoder can be adapted to work together with traditional ECC decoders to keep the number of errors within the correction capability of traditional decoders. The combined decoding framework is evaluated with a set of benchmark files.

## Compressed-and-forward: Compressive sensing for cooperative communication

- **Status**: ❌
- **Reason**: 협력통신 compressed-and-forward + JSCC/compressive sensing — 떼어낼 LDPC ECC 기법 없음
- **ID**: ieee:6473503
- **Type**: conference
- **Published**: 4-7 Nov. 2
- **Authors**: Chia-Hung Yeh, Yu-Liang Lin, Cheng-Chih Liu +1
- **PDF**: https://ieeexplore.ieee.org/document/6473503
- **Abstract**: Cooperative communication has been shown that it is an effective way to achieve spatial diversity in order to combat the user-outage caused by effects fading channel. Except for amplify-and-forward (AF) and decode-and-forward (DF), compressed-and-forward (CF) is also an efficient forwarding strategy. In the existing CF protocol, the relay will switch to the DF mode when the source transmitted signal can be recovered by the relay completely; however, no further compression is made in this scheme. This paper proposes a new CF scheme. The relay will estimate if the codeword in a predefined block can be succeeded decoded, then choose the corresponding forwarding methods which are based on joint source-channel coding or compressive sensing. At the decode side, a joint decoder is designed to decode the source according to the relay compression mode. Simulation results show that the proposed CF scheme can acquire the spatial diversity and outperform AF and DF schemes.

## EXIT chart based LDPC codes design for 2D ISI channels

- **Status**: ❌
- **Reason**: 2D ISI 채널용 EXIT chart 기반 LDPC degree 최적화 — 채널 특이적 코드설계, 표준 EXIT 차트 수준이라 NAND 이식 기여 약함
- **ID**: ieee:6407541
- **Type**: conference
- **Published**: 31 Oct.-2 
- **Authors**: Lingjun Kong, Guojun Han, Yong Liang Guan +2
- **PDF**: https://ieeexplore.ieee.org/document/6407541
- **Abstract**: Optimization of low-density parity-check (LDPC) codes to two dimensional (2D) intersymbol interference (ISI) channels is proposed, which exploits the modified Extrinsic Information Transfer (EXIT) chart. Specifically, a new degree optimization through EXIT chart fitting is proposed, where optimal variable node degree is search by selecting the best regular check node degree to match the check node decoder (CND) curve to the variable node decoder (VND) curve combined with 2d detector. Simulation result shows that the optimized LDPC code of length 13824 bits is 0.35 dB away from the symmetric information rate (SIR) of 2D ISI channels.

## Bi-directional pattern-dependent noise prediction with LDPC codes for heat-assisted magnetic recording

- **Status**: ❌
- **Reason**: HAMR 자기기록 BiPDNP/BCJR 검출기 + LDPC — 채널검출기 특이적, LDPC는 부수, 이식 디코더 기법 없음
- **ID**: ieee:6407562
- **Type**: conference
- **Published**: 31 Oct.-2 
- **Authors**: Yibin Ng, Kui Cai, B. V. K. Vijaya Kumar +2
- **PDF**: https://ieeexplore.ieee.org/document/6407562
- **Abstract**: As areal densities increase, substantial jitter noise is expected in heat-assisted magnetic recording (HAMR). To mitigate the effects of jitter noise, in an earlier work we proposed the bi-directional pattern-dependent noise prediction (BiPDNP) detector, which employs backward linear prediction as well as the conventional forward linear prediction. In this work, we implement BiPDNP in the Bahl-Cocke-Jelinek-Raviv (BCJR) detector, and investigate its performance with low-density parity check (LDPC) codes. For the LDPC coded channel, by combining the BCJR detector with BiPDNP, we observe that a SNR gain of 1 dB (at bit error rate 10−4 with 30% microtrack jitter) is achieved over the conventional BCJR detector. Further, in HAMR channel modeling the conventional thermal Williams-Comstock (TWC) model with linear relationship for coercivity with temperature is used. In this work, we update the TWC model by using a non-linear relationship for coercivity with temperature.

## Efficient correction of single insertion/deletion and multi-substitution errors

- **Status**: ❌
- **Reason**: 단일 삽입/삭제 동기화 오류정정(마커 비트) — LDPC ECC 아님, 떼어낼 BP 기법 없음
- **ID**: ieee:6407558
- **Type**: conference
- **Published**: 31 Oct.-2 
- **Authors**: G. J. Han, Y. L. Guan, K. Cai +2
- **PDF**: https://ieeexplore.ieee.org/document/6407558
- **Abstract**: A two-stage synchronization algorithm is proposed to correct single insertion/deletion and multi-substitution errors. The new algorithm only uses marker bits to infer the position of segment with synchronization error in the first stage and performs a local synchronization over the identified segment and its adjacent segments in the second stage, which results in reduced computational complexity while maintaining good error performance.

## A study of iterative detection method for four-grain based two-dimensional magnetic recording

- **Status**: ❌
- **Reason**: TDMR 2D 자기기록 반복검출 기법; LDPC 부수, 채널검출기 ISI/ITI 특이적이라 NAND BP 이식 기법 없음
- **ID**: ieee:6407371
- **Type**: conference
- **Published**: 31 Oct.-2 
- **Authors**: T. Losuwan, C. Warisarn, L. M. Myint +1
- **PDF**: https://ieeexplore.ieee.org/document/6407371
- **Abstract**: Two-dimensional magnetic recording (TDMR) is one of the novel magnetic recording technologies for the future ultra-high storage density beyond 10 Tb/in2 [1]. However, due to the high areal density, the readback signal is extremely corrupted by the inter-symbol interference (ISI) and the inter-track interference (ITI) in the recorded data retrieving. This problem can be alleviated by utilizing an advanced iterative decoding technique. This paper proposes a novel iterative decoding technique incorporating the iterative detectors and an iterative decoder to combat the severe ISI/ITI. Simulation results show that the proposed technique can reduce the ISI/ITI effect and provides a significant performance improvement in terms of bit-error rate if compared to the conventional receiver, which employs a non-iterative detector.

## Joint Source Channel Coding Using LDPC Codes

- **Status**: ❌
- **Reason**: JSCC(소스-채널 결합)에 LDPC를 베이스라인으로 사용, 표준 sum-product/puncturing만 언급, 떼어낼 신규 ECC 기법 없음
- **ID**: ieee:6375132
- **Type**: conference
- **Published**: 3-5 Nov. 2
- **Authors**: S. Nandan, P.P. Deepthi
- **PDF**: https://ieeexplore.ieee.org/document/6375132
- **Abstract**: A novel method of combined source-channel coding using LDPC codes is presented in this paper. The system presented is designed to transmit a discrete time, continuous amplitude signal over an Additive White Gaussian Noise (AWGN) channel where a Low Density Parity Check (LDPC) code is used for error correction purposes. LDPC code is a channel coding technique that provides performance near to Shannon's limit. To achieve optimum decoding, Sum-Product or message passing decoding is used for LDPC codes. Code puncturing can be implemented to obtain different code rates and this can be used for implementing joint source channel coding. Here, Source coding and Channel coding can be done in a single step using LDPC codes by puncturing the transmitted information so as to make the rate greater than or equal to the entropy of the source.

## Quasi-cyclic low-density parity-check stabilizer codes

- **Status**: ❌
- **Reason**: 양자 stabilizer 코드이며 비이진 QC-LDPC 기반(nonbinary SPA) - 비이진+양자 의존으로 이중 제외
- **ID**: ieee:6415852
- **Type**: conference
- **Published**: 29 Oct.-1 
- **Authors**: Feng Shi, Zhiyuan Yan
- **PDF**: https://ieeexplore.ieee.org/document/6415852
- **Abstract**: Quantum error correction codes are needed to protect quantum systems from interference. An important family of quantum error correction codes are stabilizer codes. Many stabilizer codes in the literature belong to a subclass of stabilizer codes, referred to as CSS codes since they are based on the so-called CSS formalism. CSS codes have received significant attention because the dual-containing condition for the CSS formalism is relatively straightforward to satisfy and also because it is easy to produce CSS codes from classical error correction codes. However, some stabilizer codes in the literature show superior error correction performance than existing CSS codes, and are based on binary low-density parity-check (LDPC) codes. Since it has been shown that CSS codes based on nonbinary LDPC codes have good performance over quantum qubit channels, in this paper we investigate stabilizer codes based on nonbinary LDPC codes. In particular, we propose constructions of stabilizer codes based on nonbinary quasi-cyclic low-density parity-check (QC-LDPC) codes for qubit channels. The simulation results show that our QC-LDPC stabilizer codes decoded by a nonbinary sum-product algorithm have better performance than their binary counterparts.

## Energy minimization of wireless sensor networks based on modulation and coding optimization under finite frame length constraint

- **Status**: ❌
- **Reason**: WSN 에너지 최소화 변조/코딩 최적화, regular LDPC는 성능평가 도구로 사용, 떼어낼 신규 ECC 기법 없음
- **ID**: ieee:6415881
- **Type**: conference
- **Published**: 29 Oct.-1 
- **Authors**: Kei Kinoshita, Hideki Ochiai
- **PDF**: https://ieeexplore.ieee.org/document/6415881
- **Abstract**: Recent hardware advances allow more signal processing functionality to be integrated into a single chip. In sensor networks, the wireless nodes are typically operated with small batteries for which their replacement, when not impossible, is very difficult and expensive. Thus, minimizing the energy consumption of transmitting sensor nodes is an important issue on the design of such communication systems. The previous work in the literature proposes modulation as well as coding optimization considering uncoded and coded bit error rate (BER) of M-ary QAM as well as its average mutual information. However, these approaches do not address the coded case with finite frame length, which is always the case in practical systems. In this paper, we consider a design of coding and modulation that minimizes the transmit circuit energy under finite codeword length constraint of capacity-approaching channel codes and analyze its performance through simulation using regular low-density parity-check (LDPC) codes in a point-to-point communication link. The results are also compared with those of information-theoretic analysis based on the mutual information rate.

## BCS: Compressive sensing for binary sparse signals

- **Status**: ❌
- **Reason**: 바이너리 sparse 신호용 압축센싱(CS) 디코딩, 채널코딩 ECC가 아닌 소스/샘플링 영역
- **ID**: ieee:6415872
- **Type**: conference
- **Published**: 29 Oct.-1 
- **Authors**: Ukash Nakarmi, Nazanin Rahnavard
- **PDF**: https://ieeexplore.ieee.org/document/6415872
- **Abstract**: Model-based compressive sensing (CS) for signal-specific applications is of particular interest in the sparse signal approximation. In this paper, we deal with a special class of sparse signals with binary entries. Unlike conventional CS approaches based on l1 minimization, we model the CS process with a bi-partite graph. We design a novel sampling matrix with unique sum property, which can be universally applied to any binary signal. Moreover, a novel binary CS decoding algorithm (BCS) based on graph and unique sum table, which does not need complex optimization process, is proposed. Proposed method is verified and compared with existing solutions through mathematical analysis and numerical simulations.

## A low-complexity multicarrier scheme with LDPC coding for mobile-to-mobile environment

- **Status**: ❌
- **Reason**: FBMC vs CP-OFDM 멀티캐리어 비교, LDPC는 코딩 BER 평가용 베이스라인, 떼어낼 ECC 기법 없음
- **ID**: ieee:6415654
- **Type**: conference
- **Published**: 29 Oct.-1 
- **Authors**: Damien Roque, Cyrille Siclet, Jean-Marc Brossier
- **PDF**: https://ieeexplore.ieee.org/document/6415654
- **Abstract**: In this paper, we consider a mobile ad-hoc radio network in an urban area. The propagation environment between two endpoints can be modeled by a double-Rayleigh fading multipath channel. Such a mobile scenario justifies the use of filter bank based multicarrier (FBMC) transmission systems. This technique generalizes traditional cyclic prefix orthogonal frequency-division multiplexing (CP-OFDM), allowing the design of non-rectangular pulse shape filters. We show that this approach leads to a better interference mitigation in time-variant channels. We restrict our study to short filters and single-tap per sub-channel equalization in order to preserve a low-complexity transmultiplexer. In this study, we compare FBMC with short filters to CP-OFDM in terms of coded bit-error-rate performances, using a realistic mobile-to-mobile channel model.

## Optimized nested protection for video Region of Interest with Raptor codes

- **Status**: ❌
- **Reason**: Raptor(fountain) 코드 기반 비디오 UEP — fountain/erasure 응용, LDPC ECC 기법 없음
- **ID**: ieee:6410766
- **Type**: conference
- **Published**: 27-30 Nov.
- **Authors**: Zhengyi Luo, Li Song, Shibao Zheng +1
- **PDF**: https://ieeexplore.ieee.org/document/6410766
- **Abstract**: Due to the best effort feature of many existing transmission channels, video streams often suffer from inevitable transmission errors. In this paper, we propose a scheme of robust video transmission based on the state-of-the-art Raptor codes, whose applications are in full swing now. And considering Region of Interest (ROI) often draws much attention in images, the scheme adopts a nested protection framework to show partialities to ROI areas for better protection. Different from many existing Raptor codes based UEP methods, our scheme is developed based on the easy-to-use standardized Raptor codes. Experimental results show that significant robustness can be obtained for the video streams, especially for the ROI areas.

## Enhancement of Error-Correction Coding of Spatial Watermarks for JPEG Compression

- **Status**: ❌
- **Reason**: 이미지 워터마크용 단순 단일오류정정 블록부호, LDPC 아님, 떼어낼 ECC 기법 없음
- **ID**: ieee:6395095
- **Type**: conference
- **Published**: 25-29 Nov.
- **Authors**: Tadahiko Kimoto
- **PDF**: https://ieeexplore.ieee.org/document/6395095
- **Abstract**: This paper demonstrates how channel coding can improve the robustness of spatial image watermarks against JPEG DCT-based compression. Two error-correction coding (ECC) schemes are used here. One scheme, referred to as the vertical ECC (VECC), is to encode information bits in pixel levels by error-correction coding where the Gray code is used to improve the performance. The other scheme, referred to as the horizontal ECC (HECC), is to encode information bits in an image plane by error-correction coding. VECC is also used to encode the code bits of HECC in pixels. Simple single-error-correcting block codes are used in VECC and HECC. Several experiments of these schemes were conducted on test images. The result demonstrates that the error-correcting performance of HECC depends on that of VECC, and accordingly, HECC enhances the capability of VECC. Consequently, HECC with appropriate codes can achieve stronger robustness to JPEG-caused distortions than non-channel-coding watermarking schemes.

## Comparative Performance Evaluation of Convolutionally Coded and LDPC Coded OFDM System over AWGN and SUI-5 Fading Channel

- **Status**: ❌
- **Reason**: OFDM에서 convolutional vs LDPC 부호 BER 성능 비교만; 표준 부호 사용, 떼어낼 신규 디코더/HW/구성 없음
- **ID**: ieee:6394707
- **Type**: conference
- **Published**: 23-25 Nov.
- **Authors**: Ashish Goel, Manoj Kumar Garg
- **PDF**: https://ieeexplore.ieee.org/document/6394707
- **Abstract**: Orthogonal Frequency Division Multiplexing (OFDM) is a very attractive technique for high data rate transmission with good bandwidth efficiency. OFDM system utilize the cyclic prefix (CP) to mitigate the effect of inter symbol interference (ISI) produced by the multipath effect of wireless channel. The CP insertion only mitigates the effect of inter block interference of OFDM symbols, whereas the intra block interference remain present in the OFDM symbol. The intra block OFDM symbol interference degrades the error performance of the OFDM system. In order to improve the error performance of the OFDM system forward error correction scheme can be utilized. Many FEC schemes for single carrier and multicarrier systems have been proposed in the literature. Convolution and LDPC codes are two popular coding schemes for FEC. In this paper we have considered Convolution and LDPC codes for improving the error performance of OFDM system. The BER performance of convolution ally coded & LDPC coded OFDM is evaluated for various code rates in AWGN and fading channel. We have also compared the performance of coded OFDM system with an OFDM system without FEC.

## A novel approach for using extended LDPC codes in cooperative diversity

- **Status**: ❌
- **Reason**: Cooperative diversity 무선 응용에 표준 extended/punctured LDPC 적용, 떼어낼 신규 ECC 기법 없음
- **ID**: ieee:6406165
- **Type**: conference
- **Published**: 21-23 Nov.
- **Authors**: Hussain Ali, Maan Kousa
- **PDF**: https://ieeexplore.ieee.org/document/6406165
- **Abstract**: Cooperative diversity or user cooperation achieves the diversity gain without adding physical antennas to the users or mobile stations. The users work in cooperative fashion using their single antennas to create a virtual transmit diversity, called relay diversity or cooperative diversity. The diversity gain achieved by cooperative diversity can be further improved using error correction codes. Low-density parity-check (LDPC) codes are linear block codes with good error correction capabilities. We present a novel approach using extended LDPC codes to increase the diversity gain in cooperative diversity. We also compare the extended LDPC codes with punctured LDPC codes in cooperative diversity and show that extended LDPC codes have lesser complexity than punctured LDPC codes in cooperative diversity.

## On secrecy above secrecy capacity

- **Status**: ❌
- **Reason**: Wiretap channel 보안/secrecy 주제, 떼어낼 LDPC 디코더·코드설계 기법 없음
- **ID**: ieee:6406111
- **Type**: conference
- **Published**: 21-23 Nov.
- **Authors**: R Rajesh, Shahid M Shah, Vinod Sharma
- **PDF**: https://ieeexplore.ieee.org/document/6406111
- **Abstract**: We consider secrecy obtained when one transmits on a Gaussian Wiretap channel above the secrecy capacity. Instead of equivocation, we consider probability of error as the criterion of secrecy. The usual channel codes are considered for transmission. The rates obtained can reach the channel capacity. We show that the “confusion” caused to the Eve when the rate of transmission is above capacity of the Eve's channel is similar to the confusion caused by using the wiretap channel codes used below the secrecy capacity.

## LDPC error correction code utilization

- **Status**: ❌
- **Reason**: LDPC 코드 마이크로컨트롤러 구현이나 표준 구성·짧은 코드 테스트 수준, 신규 디코더·HW 기여 불명확
- **ID**: ieee:6419390
- **Type**: conference
- **Published**: 20-22 Nov.
- **Authors**: Jan Broulím, Vjaceslav Georgiev
- **PDF**: https://ieeexplore.ieee.org/document/6419390
- **Abstract**: The paper presents a flexible construction of LDPC error correcting codes and an implementation of a code in a small microcontroller. A chosen short wordlength code was tested on the microcontroller platform and there were performed measurements focused on the error rate.

## Performances of Progressive Edge-Growth LDPC codes in Nakagami fading channel

- **Status**: ❌
- **Reason**: 표준 PEG 구성을 Nakagami 페이딩 채널에 적용한 성능분석, 교과서 수준 기법 재사용으로 신규 기여 없음
- **ID**: ieee:6419272
- **Type**: conference
- **Published**: 20-22 Nov.
- **Authors**: Omran Al Rasheed, Daj ana M. Radovic, Predrag N. Ivaniš
- **PDF**: https://ieeexplore.ieee.org/document/6419272
- **Abstract**: In this paper we analyze the error performances of low density parity check (LDPC) codes in channel with Nakagami distribution of the fading envelope. We consider the Progressive Edge-Growth (PEG) method for the parity check matrix construction, which can be used to avoid short girths, small trapping sets and high level of error floor. The comparative analysis with a several classes of LDPC codes is also presented for various propagation conditions.

## MTR decoding employing MAP algorithm in Boolean logic circuits

- **Status**: ❌
- **Reason**: MTR(변조부호) MAP 디코더, 자기기록 채널용 비-LDPC 부호로 이식 가능 LDPC 기법 없음
- **ID**: ieee:6419329
- **Type**: conference
- **Published**: 20-22 Nov.
- **Authors**: N. Djuric, V. Senk
- **PDF**: https://ieeexplore.ieee.org/document/6419329
- **Abstract**: Soft-decision decoding of maximum-transitionrun (MTR) codes have been required in order to utilize those codes in modern data storage systems. The maximum a posteriori (MAP) algorithm, based on Bayesian algorithm, computing a posteriori information using set of valid MTR codewords, already has been presented. The MAP method proves as a valuable for the MTR decoding in several magnetic recording applications. In this paper, the MAP approach has been considered for utilization in basic Boolean logic circuits, trying to assemble a new low-complex and soft-decision MTR decoder. The proposed idea was considered with simple and well known rate 4/5 (2, k = 8) MTR code, without loosing in generality, over E2PR4 magnetic recording channel.

## Bayesian compressive sensing with polar-distributed low-density sensing matrices

- **Status**: ❌
- **Reason**: Bayesian compressive sensing용 저밀도 sensing matrix 설계; 채널코딩 ECC 아님, 소스/CS 응용
- **ID**: ieee:6412333
- **Type**: conference
- **Published**: 19-22 Nov.
- **Authors**: Seungshik Shin, Sang-Yun Shin, Min Jang +1
- **PDF**: https://ieeexplore.ieee.org/document/6412333
- **Abstract**: Unlike general random independent identically distributed (i.i.d.) signal, sparse signal in compressive sensing is not i.i.d. and its representation consists of significant coefficients and near-zero coefficients. With consideration of the signal characteristics used in the design method of low density parity check matrix, we propose a design method of low density sensing matrix (LDSM) for the Bayesian compressive sensing framework. Good LDSM is obtained by assuming a two-state mixture Gaussian signal model, by using polar-degree-distributed variable nodes and allocating high degree nodes to the significant coefficients. Simulation results showed that the polar-distributed LDSM results in 35.1% lower mean square error than irregular LDSM which is conventionally optimized in the channel coding problem, even though the noise threshold of the polar-distributed LDSM over BI-AWGN is much lower than the conventionally optimized LDSM.

## Performance evaluation of a network coding scheme for interference channels with LTE codes

- **Status**: ❌
- **Reason**: LTE turbo 코드 기반 quantise-forward 네트워크 코딩; LDPC 아니고 떼어낼 디코더 기법 없음
- **ID**: ieee:6399390
- **Type**: conference
- **Published**: 16-16 Nov.
- **Authors**: Filippo Tosato
- **PDF**: https://ieeexplore.ieee.org/document/6399390
- **Abstract**: In this paper we consider a recently proposed quantise-forward network coding strategy, whereby a relay is used to help resolve the interference caused by independently transmitting source nodes. The relay listens to the interfering signals and performs a course lattice-based quantisation of the observations without decoding the information messages. The quantised observations are forwarded to the destination nodes on an interference-free channel and help the receivers improve the decoding process. We generalise the optimisation of the nested lattice construction to any number of quantisation bits and evaluate the strategy on the turbo codes used in the 3GPP long term evolution (LTE) to assess the viability of the strategy in LTE-based small cell deployments.

## The MAP Implementation in Logic Circuits for Soft-Decision Decoding of MTR Codes

- **Status**: ❌
- **Reason**: MTR 부호 소프트디코딩 MAP/min-max 로직회로 구현, 비-LDPC 자기기록 채널 특이적이고 LDPC BP로 떼어낼 기법 없음
- **ID**: ieee:6410155
- **Type**: conference
- **Published**: 14-16 Nov.
- **Authors**: Nikola Djuric, Vojin Senk
- **PDF**: https://ieeexplore.ieee.org/document/6410155
- **Abstract**: Maximum a posteriori (MAP) algorithm and decoding with min-max approximations in Boolean logic circuits, had been independently considered as soft-decision decoding methods for maximum-transition-run (MTR) codes. These two approaches are confirmed as quite valuable, enabling MTR decoder to handle soft-values in framework of iterative decoding. In this paper further research of these methods has been made and novel idea of MAP algorithm utilization into logic circuits, of new MTR soft-decision decoder, is presented. The proposed concept is considered with simple and well know rate 4/5 (2, k = 8) MTR code over E2PR4 magnetic recording channel. The non-log and log MAP implementation results with equal performance, while max-log version results with 1.6 dB of coding gain, for BER = 10-5.

## A (50,2,4) nonbinary LDPC convolutional code decoder chip over GF(256) in 90nm CMOS

- **Status**: ❌
- **Reason**: 비이진 GF(256) NB-LDPC convolutional 디코더 칩, 바이너리 비대상
- **ID**: ieee:6522660
- **Type**: conference
- **Published**: 12-14 Nov.
- **Authors**: Chia-Lung Lin, Chih-Lung Chen, Hsie-Chia Chang +1
- **PDF**: https://ieeexplore.ieee.org/document/6522660
- **Abstract**: A memory-based (ms = 50,dv = 2,dc = 4) nonbinary LDPC convolutional code (NB-LDPC-CC) decoder over GF(256) with layered scheduling is presented. The proposed architecture-aware construction features fewer memory banks, low degree, low period, and better performance. To the best of our knowledge, this is the first architecture discussion and implementation for NB-LDPC-CC decoders. We optimized the architecture of message first-in-first-out (M-FIFO), check node unit, and variable node unit in terms of area and throughput. Jointly designing code and architecture, overall normalized area efficiency can be enhanced by more then six times with respect to decoders of nonbinary LDPC block codes (NB-LDPC BCs). After fabricated in 90nm CMOS, our prototype NB-LDPC-CC decoder chip can achieve maximum throughput of 22.8Mbps with frequency of 285MHz. The measured average power is 211mW at a typical operating voltage of 1.0V.
