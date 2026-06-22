# IEEE Xplore — 2018-04


## The Design of Protograph LDPC Codes as Source Codes in a JSCC System

- **Status**: ❌
- **Reason**: JSCC용 protograph LDPC 소스코드 설계, 소스코딩(압축)이며 채널 ECC 아님
- **ID**: ieee:8288583
- **Type**: journal
- **Published**: April 2018
- **Authors**: Chen Chen, Lin Wang, Sanya Liu
- **PDF**: https://ieeexplore.ieee.org/document/8288583
- **Abstract**: Although joint source-channel coding (JSCC) based on double protograph low-density parity-check (LDPC) codes has been shown to be an excellent solution for wireless communication, the protograph LDPC code for source coding needs to be optimized to improve the error-floor performance. In this letter, first, it is found that optimized protograph LDPC codes for channel coding are not optimal for source compression, which indicates that the source codes in the JSCC systems need to be designed specifically. Second, a rate-1/2 source code is designed by using the source decoding threshold as evaluation criteria. Finally, low rate source codes are designed by code lengthening. The protograph extrinsic information transfer analysis and the bit error rate simulation have shown that the proposed source codes obtain higher source decoding thresholds than conventional codes, which extend the range of compressible source entropies and improve the error-floor performance in the JSCC system.

## Improving the Decoding Threshold of Tailbiting Spatially Coupled LDPC Codes by Energy Shaping

- **Status**: ✅
- **Reason**: 바이너리 tailbiting SC-LDPC 디코딩 임계값 개선(energy shaping), SC-LDPC 코드설계 기법 이식 가능(E)
- **ID**: ieee:8281448
- **Type**: journal
- **Published**: April 2018
- **Authors**: Thomas Jerkovits, Gianluigi Liva, Alexandre Graell i Amat
- **PDF**: https://ieeexplore.ieee.org/document/8281448
- **Abstract**: We show how the iterative decoding threshold of tailbiting spatially coupled (SC) low-density parity-check (LDPC) code ensembles can be improved over the binary input additive white Gaussian noise channel by allowing the use of different transmission energies for the codeword bits. We refer to the proposed approach as energy shaping. We focus on the special case where the transmission energy of a bit is selected among two values, and where a contiguous portion of the codeword is transmitted with the largest one. Given these constraints, an optimal energy boosting policy is derived by means of a protograph extrinsic information transfer analysis. We show that the threshold of tailbiting SC-LDPC code ensembles can be made close to that of terminated code ensembles while avoiding the rate loss (due to termination). The analysis is complemented by Monte Carlo simulations, which confirm the viability of the approach.

## Design of Binary LDPC Codes With Parallel Vector Message Passing

- **Status**: ✅
- **Reason**: 바이너리 QC-LDPC 사이클 최적화(PMPE/QC-PMP) 신규 코드설계 기법, NAND LDPC 구성에 이식 가능(E)
- **ID**: ieee:8207605
- **Type**: journal
- **Published**: April 2018
- **Authors**: Xingcheng Liu, Feng Xiong, Zhongfeng Wang +1
- **PDF**: https://ieeexplore.ieee.org/document/8207605
- **Abstract**: Many studies were carried out for the construction of low density parity-check (LDPC) codes. They usually focused on introducing the construction methods for good LDPC codes instead of a general method for code optimization. This paper proposes a method with high versatility, called the parallel vector message passing-based edge exchange (PMPE), for optimizing a type of graph-based LDPC codes, without changing the code parameters of mother codes, such as the code length, code rate, and degree distribution. With the approximately nearest codewords searching approach, we find the optimization method can increase the Hamming distance of the LDPC codes. For the quasi-cyclic (QC) LDPC codes, an optimization method, called the parallel vector message passing oriented-to the QC-LDPC codes (QC-PMP), is further suggested, with which the quasi-cyclic characteristics of QC-LDPC codes can remain unchanged in the optimization. To evaluate the performance of the parity-check matrix corresponding to a Tanner graph, a very simple metric, the cycles metric, is introduced to work with the proposed PMPE and QC-PMP algorithms. The experimental results show that the performance of the LDPC codes optimized with the proposed PMPE can be improved significantly at low BER range compared with the mother codes of the random codes, including the regular MacKay code of rate 0.5 and the regular PEG code of rate 0.9. For the case of the regular and irregular QC-LDPC codes with different code lengths and code rates, the optimized LDPC codes with the proposed QC-PMP algorithm significantly outperform the mother codes.

## An LDPC Code Based Physical Layer Message Authentication Scheme With Prefect Security

- **Status**: ❌
- **Reason**: 물리계층 메시지 인증(보안)에 LDPC 사용; 채널 ECC 디코더/구성 신규 기여 없음, 보안 도메인 제외
- **ID**: ieee:8334238
- **Type**: journal
- **Published**: April 2018
- **Authors**: Dajiang Chen, Ning Zhang, Rongxing Lu +4
- **PDF**: https://ieeexplore.ieee.org/document/8334238
- **Abstract**: In this paper, we study physical layer message authentication with perfect security for wireless networks, regardless of the computational power of adversaries. Specifically, we propose an efficient and feasible authentication scheme based on low-density parity-check (LDPC) codes and ϵ-AU2 hash functions over binary-input wiretap channel. First, a multimessage authentication scheme for noiseless main channel case is presented by leveraging a novel ϵ-AU2 hash function family and the dual of large-girth LDPC codes. Concretely, the sender Alice first generates a message tag T with message M and key K by using a lightweight ϵ-AU2 hash functions; then Alice encodes T to a codeword Xn with the dual of large-girth LDPC codes; finally, Alice sends (M, Xn) to the receiver Bob noiselessly. An adversary Eve has infinite computational capacity, and he can obtain M and the output Zn of the BEC with input Xn. Then, an authentication scheme over binary erasure channel and binary-input wiretapper's channel is further developed, which can reduce the noisy main channel case to noiseless main channel case by leveraging public discussion. We theoretically prove that, the proposed schemes are perfect secure if the number of attacks from Eve is upper bounded by a polynomial times in terms of n. Furthermore, the simulation results are provided to demonstrate that the proposed schemes can achieve high authentication rate with low time latency.

## Nonbinary LDPC-Coded Spatial Modulation

- **Status**: ❌
- **Reason**: 비이진 LDPC(GF) 코딩 공간변조, non-binary LDPC라 제외
- **ID**: ieee:8290977
- **Type**: journal
- **Published**: April 2018
- **Authors**: Dan Feng, Hengzhou Xu, Jianping Zheng +1
- **PDF**: https://ieeexplore.ieee.org/document/8290977
- **Abstract**: This paper presents a nonbinary low-density parity-check (LDPC) coded spatial modulation (CSM) for multiple-input multiple-output communication systems, in which the information bits for choosing active transmit antennas and the bits for choosing constellation signals are protected by a nonbinary LDPC code. We apply a many-to-one mapping known as Gallager mapping to signal constellation, resulting in an improved constellation design for the CSM system. Furthermore, we propose a Gallager mapping-based scheme to solve the design problem of the CSM system with arbitrary transmit antennas, in which Gallager mapping is used to map the index information bits to the active antenna, thus an integer-bit transmission can be achieved for any number of transmit antennas. With the use of nonbinary LDPC codes, a non-iterative receiver is able to recover the undistinguished information caused by the many-to-one mapping. Several communication scenarios are studied and simulation results show that the proposed scheme can offer substantial performance gains with design flexibility over the Rayleigh fading channel.

## Randomized Serially Concatenated LDGM Codes for the Gaussian Wiretap Channel

- **Status**: ❌
- **Reason**: Gaussian wiretap 보안용 LDGM 코드+보안갭, 보안 응용이며 떼어낼 일반 ECC 기법 없음
- **ID**: ieee:8252922
- **Type**: journal
- **Published**: April 2018
- **Authors**: Alireza Nooraiepour, Tolga M. Duman
- **PDF**: https://ieeexplore.ieee.org/document/8252922
- **Abstract**: We study the application of a special class of low-density parity-check codes to the wiretap channel. We construct a randomized coding scheme based on serially concatenated low-density generator matrix codes and their duals extending the approach used for convolutional and turbo codes. Furthermore, we propose an efficient iterative decoder for this scheme utilizing a joint iterative message passing algorithm. We demonstrate via numerical examples that this approach outperforms other available practical coding alternatives for the Gaussian wiretap channel in terms of the resulting security gap.

## Design and Analysis of Anytime Codes for Relay Channels

- **Status**: ❌
- **Reason**: 릴레이 네트워크용 anytime bilayer 코드, NAND ECC에 떼어낼 디코더/HW/구성 기법 없는 통신 응용 특이적
- **ID**: ieee:8166790
- **Type**: journal
- **Published**: April 2018
- **Authors**: Md. Noor-A-Rahim, Khoa D. Nguyen, Gottfried Lechner +1
- **PDF**: https://ieeexplore.ieee.org/document/8166790
- **Abstract**: Anytime codes are known to be useful for tracking and controlling unstable systems over noisy channels. Although practical anytime codes have been developed for point-to-point communication, to date no practical code constructions and tractable analysis of anytime codes are known to exist for relay networks. In this paper, we study the design and theoretical analysis of anytime codes for a three-terminal relay network. We propose bilayer codes for anytime transmission over the relay network and consider two transmission schemes for the relay-destination link. For both schemes, we analytically derive the delay-exponents and show that they closely match the corresponding numerical results obtained from density evolution. Through simulation, we also show the finite-length performance of the proposed bilayer anytime code.

## Designing Protograph-Based LDPC Codes for Iterative Receivers on ${M}$ -ary DCSK Systems

- **Status**: ❌
- **Reason**: M-ary DCSK 카오스 수신기용 protograph-LDPC 설계로 응용특이적 EXIT 설계원칙, NAND 이식 가능한 일반 구성 기여 없음
- **ID**: ieee:8012533
- **Type**: journal
- **Published**: April 2018
- **Authors**: Qiwang Chen, Lin Wang, Yibo Lyu +1
- **PDF**: https://ieeexplore.ieee.org/document/8012533
- **Abstract**: In this brief, protograph-based low density parity check (P-LDPC) codes, which have simple structure and excellent error-correction capability, are designed for iterative receivers (IRs) on M-ary differential chaos shift keying (M-ary DCSK) systems. Due to the non-periodic and random characteristics of chaos carriers and their interaction with soft information, the conventional optimal P-LDPC codes over Bi-AWGN channels in the tandem mode may not perform well in M-ary DCSK systems with IR. With the help of a finite-length extrinsic information transfer (EXIT) algorithm, the convergence of IR is analyzed, by which a new design principle is proposed to construct new P-LDPC codes for the M-ary DCSK systems. Both EXIT analysis and simulated results demonstrate the superiority of the proposed P-LDPC codes.

## Precoded MIMO Systems With Nonbinary LDPC Codes and Many-to-One Mapping

- **Status**: ❌
- **Reason**: 비이진(NB-LDPC) MIMO 프리코딩 설계로 비이진 LDPC는 제외 대상
- **ID**: ieee:8120131
- **Type**: journal
- **Published**: April 2018
- **Authors**: Nhat-Quang Nhan, Philippe Rostaing, Karine Amis +2
- **PDF**: https://ieeexplore.ieee.org/document/8120131
- **Abstract**: A precoding design is proposed for multiple-input multiple-output (MIMO) systems utilizing nonbinary low-density parity check (NB-LDPC) codes and many-to-one mapping. When a high-order modulation scheme is used, many-to-one mapping converts a group of low-order Galois field (GF) coded symbols into one modulated MIMO symbol vector. In contrast, one-to-one mapping maps a high-order modulation symbol directly from one high-order GF coded symbol. With the help of an interleaver between the NB-LDPC encoder and the GF to MIMO symbol mapper, the many-to-one mapping enables turbo receiver and reduces the computational complexity by more than 95%. The proposed MIMO precoders enhance the error-rate performance of the many-to-one NB-LDPC MIMO system, especially in terms of reducing the error floor and improving the waterfall region. The proposed precoder design modifies the approach that suboptimally maximizes the minimal Euclidean distance between the received MIMO symbols. Simulation results show that the proposed precoders enhance the robustness of the precoder design and reduce the inner and outer iterations of the turbo receiver.

## Burst-mode fpga implementation and error location analysis of forward error correction for passive optical networks

- **Status**: ❌
- **Reason**: PON용 Reed-Solomon FEC의 FPGA 구현·에러분석; 비-LDPC 부호이고 RS 특화 기법뿐
- **ID**: ieee:8336683
- **Type**: journal
- **Published**: April 2018
- **Authors**: Nicola Brandonisio, Stefano Porto, Daniel Carey +4
- **PDF**: https://ieeexplore.ieee.org/document/8336683
- **Abstract**: Forward error correction (FEC) based on Reed–Solomon coding for the burst-mode upstream traffic of passive optical networks (PONs) is analyzed in detail using flexible field-programmable gate arrays (FPGAs). In order to achieve true burst-mode transmission using FPGAs, specific architectural solutions are required. In particular, a burst-mode frame synchronizer and a burstmode Reed–Solomon decoder are described in detail and analyzed experimentally within a state-of-the-art longreach PON test-bed. During this analysis, the upstream FEC performance is impaired by introducing strongly correlated and localized errors within the burst through the reduction of the burst preamble duration. The observed FEC degradation is exhaustively analyzed by implementing on the FPGAs a tool for error location analysis and frame loss measurements. This investigation demonstrates the importance of understanding the error distribution within the burst in order to correctly estimate the FEC performance in PON upstream links.

## A Survey of Physical Layer Security Techniques for 5G Wireless Networks and Challenges Ahead

- **Status**: ❌
- **Reason**: 5G 물리계층 보안 서베이; 신규 디코더·구성·HW 기여 없음
- **ID**: ieee:8335290
- **Type**: journal
- **Published**: April 2018
- **Authors**: Yongpeng Wu, Ashish Khisti, Chengshan Xiao +3
- **PDF**: https://ieeexplore.ieee.org/document/8335290
- **Abstract**: Physical layer security which safeguards data confidentiality based on the information-theoretic approaches has received significant research interest recently. The key idea behind physical layer security is to utilize the intrinsic randomness of the transmission channel to guarantee the security in physical layer. The evolution toward 5G wireless communications poses new challenges for physical layer security research. This paper provides a latest survey of the physical layer security research on various promising 5G technologies, including physical layer security coding, massive multiple-input multiple-output, millimeter wave communications, heterogeneous networks, non-orthogonal multiple access, full duplex technology, and so on. Technical challenges which remain unresolved at the time of writing are summarized and the future trends of physical layer security in 5G and beyond are discussed.

## A 9.52 dB NCG FEC Scheme and 162 b/Cycle Low-Complexity Product Decoder Architecture

- **Status**: ❌
- **Reason**: 광통신 product code(비-LDPC) FEC+post-processing 디코더 아키텍처로 LDPC 부호·BP 이식 기법 아님
- **ID**: ieee:8036239
- **Type**: journal
- **Published**: April 2018
- **Authors**: Carlo Condo, Pascal Giard, François Leduc-Primeau +2
- **PDF**: https://ieeexplore.ieee.org/document/8036239
- **Abstract**: Powerful forward error correction (FEC) schemes are used in optical communications to achieve bit-error rates (BERs) below 10-15. These FECs follow one of two approaches: the concatenation of simpler hard-decision codes or the usage of inherently powerful soft-decision codes. The first approach yields lower net coding gains (NCGs), but can usually work at higher code rates and have lower complexity decoders. In this paper, we propose a novel FEC scheme based on a product code and a post-processing technique. It can achieve an NCG of 9.52 dB at a BER of 10-15 and 9.96 dB at a BER of 10-18, an error-correction performance that sits between that of current hard-decision and soft-decision FECs. A decoder architecture is designed, tested on field programmable gate array and synthesized in 65-nm CMOS technology: its 162 b/cycle worst-case information throughput can reach 100 Gb/s at the achieved frequency of 616 MHz. Its complexity is shown to be lower than that of hard-decision decoders in literature, and an order of magnitude lower than the estimated complexity of soft-decision decoders.

## Flexible WOM codes for NAND flash memory based on raptor-like codes

- **Status**: ✅
- **Reason**: NAND 플래시 직접 대상 WOM 코드(raptor-like rate-compatible LDGM); 카테고리 A, NAND 수명 관련
- **ID**: ieee:8360624
- **Type**: journal
- **Published**: April 2018
- **Authors**: Bohwan Jun, Heeyoul Kwak, Jong-Seon No +1
- **PDF**: https://ieeexplore.ieee.org/document/8360624
- **Abstract**: Write-once memory (WOM) codes aim to extend the lifetime and improve the writing efficiency of storage devices such as NAND flash memory by reducing the number of erase operations. In this paper, a new rewriting scheme for NAND flash memory is proposed, which supports two writes (or only one rewrite) and allows the second write incrementally done multiple times by using raptor-like codes as rate-compatible (RC) low-density generator matrix (LDGM) codes. The proposed scheme improves writing efficiency of the NAND flash memory when combined with a proper page selection method. It is verified via numerical analysis that the proposed WOM codes outperform the conventional WOM codes in terms of writing efficiency.

## Low-Complexity Iterative MMSE-PIC Detection for MIMO-GFDM

- **Status**: ❌
- **Reason**: MIMO-GFDM MMSE-PIC 검출기, LDPC는 부수 언급, 떼어낼 LDPC ECC 기법 없는 무선 검출 알고리즘
- **ID**: ieee:8186198
- **Type**: journal
- **Published**: April 2018
- **Authors**: Maximilian Matthé, Dan Zhang, Gerhard Fettweis
- **PDF**: https://ieeexplore.ieee.org/document/8186198
- **Abstract**: Driven by 5G requirements, research on alternatives to the popular cyclic-prefix orthogonal frequency division multiplexing (CP-OFDM) waveform recently arose. In particular, non-orthogonal circularly filtered waveforms such as generalized frequency division multiplexing (GFDM) were proposed due to flexibility and robustness. Applying multiple-input multiple-output (MIMO) techniques for future wireless networks are unquestionable and thereby compulsory for any alternative waveform. Despite advancements in accurate MIMO detection algorithms for GFDM, compared with CP-OFDM their complexity still exhibited a higher order of magnitude, impeding an energy-efficient implementation. In this paper, we propose a low-complexity formulation for iterative minimum mean squared error with parallel interference cancellation (MMSE-PIC) detection for non-orthogonal waveforms with localized inter-carrier interference, where we focus on the application to MIMO-GFDM. The proposal achieves complexity similar to CP-OFDM and we evaluate its performance under realistic channel conditions with imperfect channel state information, where we obtain up to 2-dB gain of GFDM compared with OFDM. We confirm our findings by analyzing the measured extrinsic information transfer charts and show that the proposal achieves the performance of optimal maximum likelihood detection. The results point out the MMSE-PIC algorithm as a viable technique for iterative MIMO receiver implementations for non-orthogonal waveforms.

## Partially Active Message Passing Receiver for MIMO-SCMA Systems

- **Status**: ❌
- **Reason**: MIMO-SCMA 메시지패싱 수신기로 SCMA 검출 특이적, 바이너리 LDPC BP에 떼어낼 일반 기법 없음
- **ID**: ieee:8089405
- **Type**: journal
- **Published**: April 2018
- **Authors**: Jincheng Dai, Guangjin Chen, Kai Niu +1
- **PDF**: https://ieeexplore.ieee.org/document/8089405
- **Abstract**: Recently, sparse code multiple access (SCMA) and multiple-input multiple-output (MIMO) are viewed as two key techniques to address the high spectral efficiency and massive connectivity requirements for the 5G wireless system. Even though the sparse structure of each user's codewords has been exploited, the complexity of joint MIMO and multiuser detection (JMMD) in the MIMO-SCMA systems still grows exponentially with the number of antennas and accessed users. In this letter, to tackle this severe problem, based on the Gaussian approximation principle, we propose a partially active message passing receiver for the MIMO-SCMA systems. In this case, a sliding window is introduced to determine which users stay active during each detection and decoding process while others keep silent. By this means, the complexity of JMMD can be efficiently reduced while its performance just suffers a slight loss, which fascinates the practical implementation of MIMO-SCMA systems.

## A Novel Joint PAPR Reduction Algorithm With Low Complexity Using LT Codes

- **Status**: ❌
- **Reason**: LT codes 기반 OFDM PAPR 저감 알고리즘으로 ECC 디코딩과 무관
- **ID**: ieee:8066380
- **Type**: journal
- **Published**: April 2018
- **Authors**: Dadi Bi, Peng Ren, Zheng Xiang
- **PDF**: https://ieeexplore.ieee.org/document/8066380
- **Abstract**: In this letter, a low complexity joint peak to average power ratio (PAPR) reduction scheme is proposed for orthogonal frequency division multiplexing systems based on Luby transform (LT) codes. In the encoding process of LT codes, a predetermined threshold is introduced to control PAPR and reduce complexity. Moreover, we use the number of IFFT operations to model and formulate the theoretical algorithm complexity. Simulation results show that the proposed scheme can effectively reduce PAPR with a huge complexity reduction. Compared with the existing scheme, a maximum complexity reduction of 81% can be obtained concerning the total number of IFFT operations. Regarding the IFFT operations per degree, experimental curves are also consistent with the mathematical analysis.

## Robust Modulation of PWM-Based Multi-Level Perpendicular Magnetic Recording for Conventional Media

- **Status**: ❌
- **Reason**: PWM 자기기록 변조 기법이 본질이고 LDPC는 평가용; 제안 부호는 GF(128) 비이진 LDPC라 제외
- **ID**: ieee:8293860
- **Type**: journal
- **Published**: April 2018
- **Authors**: Kohsuke Harada, Nobuhiro Maeto, Akihiro Yamazaki +1
- **PDF**: https://ieeexplore.ieee.org/document/8293860
- **Abstract**: In this letter, we propose a robust 3-ary modulation for a pulse width modulation (PWM)-based multi-level perpendicular magnetic recording. In the proposed 3-ary modulation, narrow-width pulses are restrained in PWM signal corresponding to resolution of magnetic media. We evaluate a user bit density (UBD) gain in our proposal using a low-density parity-check (LDPC) coded frame error rate performance. A low-resolution media is assumed as read/write (R/W) channel in the evaluation. Our simulation results show the proposed modulation has robust UBD gain compared with the conventional binary R/W systems in the low-resolution media. In addition, our proposed 7B6T modulation with non-binary LDPC codes over GF(128) has more than 6% density gain from the practical binary systems.

## Window-Interleaved Turbo Codes

- **Status**: ❌
- **Reason**: window-interleaved 터보 코드, 비-LDPC 부호이고 인터리버 기법이 LDPC BP에 직접 이식 안 됨
- **ID**: ieee:8259467
- **Type**: journal
- **Published**: April 2018
- **Authors**: Onurcan İşcan, Wen Xu
- **PDF**: https://ieeexplore.ieee.org/document/8259467
- **Abstract**: We consider a class of turbo codes with a band structured interleaver, such that the interleaving (and thus deinterleaving) is done within a window. This ensures that the extrinsic information for each symbol is generated from symbols within a window, allowing the processing of large message blocks with a sliding window decoder. This provides flexibility in terms of decoding latency and also makes parallel decoding with high-throughput possible.

## Probabilistic MIMO Symbol Detection With Expectation Consistency Approximate Inference

- **Status**: ❌
- **Reason**: MIMO 심볼 검출용 EC 추론기, LDPC는 후단 채널코드 결합일 뿐 떼어낼 ECC 디코더 기법 없음
- **ID**: ieee:8234658
- **Type**: journal
- **Published**: April 2018
- **Authors**: Javier Céspedes, Pablo M. Olmos, Matilde Sánchez-Fernández +1
- **PDF**: https://ieeexplore.ieee.org/document/8234658
- **Abstract**: In this paper, we explore low-complexity probabilistic algorithms for soft symbol detection in high-dimensional multiple-input multiple-output (MIMO) systems. We present a novel algorithm based on the expectation consistency (EC) framework, which describes the approximate inference problem as an optimization over a nonconvex function. EC generalizes algorithms such as belief propagation and expectation propagation. For the MIMO symbol detection problem, we discuss feasible methods to find stationary points of the EC function and explore their tradeoffs between accuracy and speed of convergence. The accuracy is studied, first in terms of input-output mutual information and show that the proposed EC MIMO detector greatly improves state-of-the-art methods, with a complexity order cubic in the number of transmitting antennas. Second, these gains are corroborated by combining the probabilistic output of the EC detector with a low-density parity-check channel code.

## Simulating the reliability of radio links during superior solar conjunctions

- **Status**: ❌
- **Reason**: 심우주 태양합 동안 무선링크 신뢰성 시뮬레이션; LDPC/ECC 기법 없음, 통신 응용 특이적
- **ID**: ieee:8568939
- **Type**: conference
- **Published**: 9-13 April
- **Authors**: A. J. Stocker, A. Aigyriou, A. Gioigetti +7
- **PDF**: https://ieeexplore.ieee.org/document/8568939
- **Abstract**: Some results so far achieved in the framework of the HELIOS (Highly rEliable Links during sOlar conjunctions) Project, founded by the European Space Agency (ESA), are presented. The purpose of the project is the definition of a TT&C communication subsystem architecture (including both ground and space segments, as well as operational methods) being robust to impairments due to superior solar conjunction, especially when the Sun-Earth-Probe angle is below 5 degrees.

## Compressed Low-rate Codes for Failure-tolerant Distributed Storage

- **Status**: ❌
- **Reason**: 압축 결합 low-rate code; 데이터 압축 소스코딩 결합, 채널 ECC LDPC 신규 디코더/구성 기법 없음
- **ID**: ieee:8385237
- **Type**: conference
- **Published**: 9-12 April
- **Authors**: Peter Sobe
- **PDF**: https://ieeexplore.ieee.org/document/8385237
- **Abstract**: The combination of low-rate codes, data distribution and data compression for application in the scope of failuretolerant storage systems is studied. First, we describe a number of specific compressed low-rate codes and evaluate them. Second, a principle is outlined to explore new compressed low-rate codes. Objectives are low computational cost for en- and decoding and an acceptable low storage overhead.

## 9.1x Error acceptable adaptive artificial neural network coupled LDPC ECC for charge-trap and floating-gate 3D-NAND flash memories

- **Status**: ✅
- **Reason**: A. 3D-NAND(charge-trap/floating-gate) ANN 결합 LDPC ECC, 컨트롤러 구현 직접 대상
- **ID**: ieee:8357064
- **Type**: conference
- **Published**: 8-11 April
- **Authors**: Toshiki Nakamura, Yoshiaki Deguchi, Ken Takeuchi
- **PDF**: https://ieeexplore.ieee.org/document/8357064
- **Abstract**: Adaptive Artificial Neural Network coupled (ANN) LDPC ECC (ANN-LDPC ECC) is proposed to increase acceptable errors by 9.1-times and to extend the data-retention lifetime by 76-times for charge-trap and floating-gate 3D-NAND flash memories. Adaptive ANN automatically compensates for complex memory cell errors such as lateral charge migration, vertical charge de-trap, inter floating-gate capacitive coupling noise and inter word-line variations. In addition, proposed ANN-LDPC can reproduce the dynamic endurance and data-retention time dependence of errors. Proposed ANN-LDPC is implemented in the storage controller and can precisely and adaptively estimate BER. As a result, memory cell errors are corrected without read time penalty or storage controller size increase.

## An Approach of Secure Image Transmission Using Low Density Parity Check Codes

- **Status**: ❌
- **Reason**: 표준 LDPC 인코더를 CDMA 영상전송에 단순 적용 - 새 디코더/구성/HW 기여 없음
- **ID**: ieee:8524546
- **Type**: conference
- **Published**: 3-5 April 
- **Authors**: A.Annamalai Giri, T. Suresh
- **PDF**: https://ieeexplore.ieee.org/document/8524546
- **Abstract**: This paper proposes an implementation of secure image transmission using Low Density Parity Check (LDPC) codes. Nowadays, the data from discrete memory less source have been transmitted without error is the major problem, which will be rectified in this proposed method. First of all the analog image is converted into digital image and encoded by Absolutely Addressed Picture Element (APEL) Encoder as a source coding. Further the digital data are encoded by the LDPC Encoder as a channel coding to convert an image into the most appropriate form used to transmit over the communication channel and the output of the channel encoder is transmitted through the communication channel by the CDMA Transmitter for secure transmission. The Rake Receiver is used to receive the CDMA signal and then decoded the transmitted sequence to obtain an original image.

## Reduced-complexity window decoding of spatially coupled LDPC codes for magnetic recording systems

- **Status**: ✅
- **Reason**: SC-LDPC 윈도우 디코딩 복잡도 감소(동적 시프팅 DS-WD/DS-N-WD), 이식 가능 디코더 알고리즘(C)
- **ID**: ieee:8508405
- **Type**: conference
- **Published**: 23-27 Apri
- **Authors**: S. Khittiwitchayakul, W. Phakphisut, P. Supnithi
- **PDF**: https://ieeexplore.ieee.org/document/8508405
- **Abstract**: In channel coding theory, the performance of error correcting codes (ECCs) approaching the Shannon limit can be achieved through increasing code lengths. Unfortunately, the complexity of ECCs will be increased as the code length increases. Nowadays, the magnetic recording (MR) system takes advantage of powerful ECCs by using 4 Kbytes sector. Among the advanced ECCs, the spatially coupled LDPC (SC-LDPC) codes (also known as a LDPC convolutional code) [1]are shown to have the decoding latency and complexity lower than those of the underlying LDPC block codes (LDPC-BC). Moreover, the SC-LDPC codes with threshold decoding outperform the LDPC-BC codes [2]. Hence, the SC-LDPC codes are the strong candidate for the future MR systems, when the sector size is increased beyond 4 Kbytes. An SC-LDPC decoder can use sliding window decoding [3]whereby the received signals are decoded by sliding window along the bit sequence. The window decoder is called “uniform window decoding (U-WD),” when all variable nodes (VNs) within a window are updated. In order to reduce the complexity of window decoding, some researchers proposed the non-uniform window decoding (N-WD) [4], which do not update the VNs with no improvement in the bit error rate (BER). This approach provides about 35-50% reduction in complexity compared to U-WD. In this work, we consider the application of SC-LDPC codes in MR systems, whereby SC-LDPC decoder cooperates with BCJR detector to encounter inter-symbol interference (ISI). We propose the dynamic shifting of window decoding (DS-WD) to reduce the complexity of SC-LDPC codes. Herein, the number of shifted bits is defined according to their soft BERs which are estimated at each decoding position. In addition, we modify the N-WD [4]to reinforce our proposed algorithm called “dynamic-shifting non-uniform window decoding (DS-N-WD).” The DS-WD and DS-N-WD achieve the complexity reduction of 7% and 25% without any loss in performance compared to the N-WD algorithms.

## Two-dimensional Signal Processing Systems Using CRC-polar Coding and List Decoding for Bit-patterned Magnetic Recording

- **Status**: ❌
- **Reason**: 비이진 LDPC + CRC-polar/SCL 디코더 조합; 비이진 LDPC는 제외, polar SCL은 부호 비의존 BP 이식 기법 아님
- **ID**: ieee:8508411
- **Type**: conference
- **Published**: 23-27 Apri
- **Authors**: H. Saito
- **PDF**: https://ieeexplore.ieee.org/document/8508411
- **Abstract**: In this research, a new effective signal processing scheme is proposed for a two-dimensional magnetic recording (TDMR) system using bit-patterned media (BPM). The proposed signal processing scheme uses concatenated cyclic redundancy check polar (CRC-polar) codes [1] as modulation codes and a non-binary low-density parity-check (LDPC) code as an error-correction code (ECC). In decoding process, successive-cancellation list (SCL) decoders [1] are introduced. These SCL decoders are expected to give an error rate performance improvement to the successive cancellation decoder of [2]. In these list decoder, several decoding paths are considered concurrently at each decoding stage. At the end of the decoding process, the most likely path among these survived paths is selected as the single codeword at the decoder output.

## Polar Coding for Spin-Torque Transfer Magnetic Random Access Memory (STT-MRAM)

- **Status**: ❌
- **Reason**: STT-MRAM용 polar 부호 설계; polar이며 부호 비의존 BP 이식 기법 없음
- **ID**: ieee:8508795
- **Type**: conference
- **Published**: 23-27 Apri
- **Authors**: Z. Mei, K. Cai, B. Dai
- **PDF**: https://ieeexplore.ieee.org/document/8508795
- **Abstract**: Spin-torque transfer magnetic random access memory (STT-MRAM) has emerged as a promising non-volatile memory (NVM) technology with various potential applications such as working as the embedded NVM or replacing the stand alone DRAM [1]. However, STT-MRAM suffers from process variations and thermal fluctuations, leading to both the write errors and read errors [2]. Hence it is critical to construct effective error correction codes (ECCs) to improve the system reliability. A single-error-correcting (71, 64) Hamming code is adopted by Everspin's 16Mb MRAM [3]. Extended Hamming codes with hybrid decoding are further proposed for STT-MRAM for the purpose of replacing DRAM [2]. Multiple-error-correcting BCH codes as well as low-density parity-check (LDPC) codes have also been investigated for STT-MRAM [4], for applications with relaxed requirement of the read latency. In this work, we propose, for the first time, the design and optimization of polar codes [5] for the STT-MRAM channel. Compared with LDPC codes with short code lengths, polar codes can achieve better error performance with lower decoding complexity. Moreover, polar codes allow easy adjustment of the code rates with a single encoder/decoder, which is a significant advantage over the Hamming codes and BCH codes. Such rate-compatible property can mitigate the raw bit error rate (BER) diversity of STT-MRAM cells caused by process variations.

## Spatially-Coupled Codes for Channels With SNR Variation

- **Status**: ✅
- **Reason**: SC-LDPC 신규 분할(MO 확장 γ=4)·채널인지 인터리빙으로 error floor 개선, 코드설계 기법(E) 이식 가능
- **ID**: ieee:8508464
- **Type**: conference
- **Published**: 23-27 Apri
- **Authors**: H. Esfahanizadeh, A. Hareedy, R. Wu +2
- **PDF**: https://ieeexplore.ieee.org/document/8508464
- **Abstract**: Modern magnetic recording (MR) systems require error correcting codes (ECCs) with outstanding error floor performance. Low-density parity-check (LDPC) codes are a primary choice for MR systems because of their error correcting capabilities [1]–[3]. In a magnetic recording device, some sections can be more error-prone than other sections because of the read/write mechanism and physical properties of the device [4]. A realistic channel model for magnetic recording systems must consider the variation of signal to noise ratio (SNR) among consecutive sections of a hard disk drive. For channels with SNR variation, the conventional ECCs are designed to achieve the certain BER for the section with the lowest SNR. For the sections with higher SNRs, this approach results in an additional redundancy which is not necessary to achieve the target BER. Spatially-coupled (SC) codes are a family of graph-based codes that have attracted significant attention because of their capacity approaching performance [5]. SC codes are constructed by partitioning a parity-check matrix H of the underlying block code into component matrices H0,…,Hm, H=H0+…+Hm, and coupling L copies of the component matrices together to obtain the parity-check matrix HSC, Fig. 1. The parameters m and L are known as the memory and coupling length, respectively. An SC code with coupling length L has L replicas, {R1,…,RL}, see Fig. 1. In this paper, we present an SC code design approach for channels with SNR variation. In our code design, the length of the underlying block codes is equal to the length of one section of the channel, and the number of sections spanned by one SC code is determined by L. Because of this structure, each check node (CN) receives messages from more than one section, so more reliable variable nodes (VNs) can help compensate for the sections that are highly affected by noise. In our model for a channel with SNR variation, each section is considered as an AWGN channel with SNRi (i is the section index). For the i’th section, we state the SNR as (SNRi)dB=(SNRabs)dB+(ΔSNRi)dB, where (SNRabs)dB is the absolute SNR and (ΔSNRi)dB is the variation from the absolute SNR for the i’th section. We first describe our code construction approach: The length of the underlying block code is equal to the length of one section of the channel, so each replica of an SC code spans one section of the channel. The coupling length L determines how many sections are spanned by one SC code, so it must be chosen such that a variety of sections with different reliabilities are included. The minimum overlap (MO) approach is recently introduced for partitioning block codes and constructing SC codes [6]. In this approach, the matrix H of a block code is partitioned into several component matrices such that the number of detrimental objects in the graph of the derived SC code for AWGN channels is reduced. In this paper, we use MO approach for constructing SC codes with γ=3. Moreover, we extend this approach to construct SC codes with γ=4. The memory m of an SC code plays the critical role on its performance over channels with SNR variation. By increasing memory, sections are more cooperative, and the SNR variation among them can be alleviated better. The parameter m determines how many different sections are involved in the check equations in an iterative decoding. Because of our SC code construction, most CNs receive messages from VNs within m+1 consecutive sections. As a result, if there is one reliable section with a high SNR, it can in principle help the messages from other m sections be recovered more reliably. For interleaving, we divide the SC codeword into L2/(m+1) chunks. Then, we rearrange them by taking one chunk from each L consecutive chunks and putting them next to each other. This interleaved data is passed through the channel, and the de-interleaving is performed on the received data from the channel and before decoding. Due to interleaving, most CN receives an equal number of messages from all L different levels of reliabilities. Our simulation results show that our channel-based interleaving compensates for the performance gap that exists between the error rates of SC codes over non-uniform and uniform channels with similar average SNR. Our proposed scheme is the first channel-aware interleaving for SC codes, and the complexity of the proposed interleaving is inversely proportional to the number of component matrices. The regular interleaving has a fixed complexity with respect to the memory which is equal to the complexity of our interleaving scheme for the case m=0 (the uncoupled setup). Finally, we show some important simulation results. Block Code 1 is an array-based block code with γ=3, length 289 bits, and rate r=0.82. SC Code 1 and 2 are SC codes with Block Code 1 as the underlying block code. They both have L=30 and length 8670 bits. The memory and rate for SC Code 1 are m=1 and r=0.82, and for SC Code 2 are m=2 and r=0.81, respectively. Fig. 2 shows the BER curves for Block Code 1, SC Code 1, and SC Code 2 over the non-uniform channel. It can be seen that SC Code 1 shows 2 orders of magnitude performance improvement in the error floor area compared to the Block Code 1, with and without (regular) interleaving, respectively. We achieve further improvement when we apply our optimized interleaving to SC Code 1. Moreover, SC Code 2 secures even further improvement by providing more cooperation among different sections of the channel. The longer version includes results for our γ=4 SC codes.

## Channel modeling and multi-island recording scheme on bit patterned media with long-range island orientation fluctuations

- **Status**: ❌
- **Reason**: BPM 채널모델링·multi-island 기록방식 연구; LDPC는 표준 사용 베이스라인, 떼어낼 신규 ECC 기법 없음
- **ID**: ieee:8508481
- **Type**: conference
- **Published**: 23-27 Apri
- **Authors**: Y. Wang, V. Bhagavatula, Y. Wen +1
- **PDF**: https://ieeexplore.ieee.org/document/8508481
- **Abstract**: Usually for Bit patterned media recording (BPMR)[1], the media noise (island size and position fluctuations) exhibits short-range disordering[2]. However, recently some BPM fabricated with cost effectiveself-assembled technology exhibits long-range disordering, as shown in the TEM image (Fig. 1(a), courtesy of Jimmy Zhu and Vignesh at CMU). Specifically, the BPM consists of multiple small domains (rectangular frame in Fig.1(a)) with different island orientations (indicated by arrows). In each domain, the islands are relatively organized because islands in a domain have similar orientation, however, the islands’ orientation varies much more from one domain to another. Hence such BPM introduces long-range island orientation fluctuations among domains besides the usual local island size and position fluctuations. Since such BPM appears to be more attractive due to its potentially lower fabrication cost, an interesting question is whether it is possible to record the information reliably on such BPM. To investigate the feasibility of reliably storing and retrieving data from such BPM, we first need to develop a channel model. For channel modeling, we assume that the track pitch and bit length are 12.7nm and 12.7nm, the island size is 7nm x 7nm, corresponding to the channel density of 4Tb/in $^{2}$. Based on the TEM image in Fig. 1(a), the island position and size fluctuations are modeled as strongly and weakly 2-D correlated Gaussian noise, respectively. To model orientation fluctuations, a mask (size ${\mathrm{L}_{M}} \times {mathrm{W}_{M}})$ with size larger than the domain (size L x W) is assumed, where the aligned islands within each mask are rotated with some angle. Then after the rotation, only the islands remaining within each domain are retained (Fig.1 (b)). The orientation fluctuation among each domain is assumed to uniformly distributed on the interval [- a, a] i.e. a = the angle 0, 5° and 15° in Fig.2 (b), (c)). The modeled BPM is shown in Fig.1 (c). Then the write and read process is modeled as in[2]. A read head array with three elements (with free layer dimension of 15nm x 15nm x 4nm) and 13nm shield-to-shield spacing and 4nm magnetic fly height is used to readback three tracks. Then the multitrack signals are processed with 2D MMSE equalizer, detected with BCJR detector and the write/read errors are corrected with an LDPC code (Fig.1 (d)). For LDPC decoder, the number of internal and global iterations ${(\mathrm{N}_{turbo}})$ are 10 and 3. Considering that the significant media noise and the write in errors for such BPM, we have proposed a recording scheme using multi-island (2 by 2 dots) representation for one bit information compared to the regular recording scheme by recording one bit on one dot (Fig.2 (a)). For the LDPC encoding, the code rate for 4 dots/bit $(R=0.9)$ is about 4 times as high as 1 dot/bit $(R=0.225)$ to obtain the same user areal density (i.e., 0.9 Tb/in $^{2})$, considering there are 4 Teradots/in2. Then the raw BER performance is investigated (Fig.2(b)). Here we assume 10% island position and size fluctuations (1.27nm, 0.7nm), 5% switching field distribution, 5% track mis-registration and 5% write clock phase shift. It is found that the raw BER performances for both recording schemes degrade with increasing orientation fluctuations. However, the 1 dot/bit case degrades much more severely than the 4 dots/bit case because the redundancy in the 4 dots/bit representation reduces the impact of write errors and decreases the effect of the media noise. More importantly, we have investigated the decoded BER performance of both recording schemes at the same user areal density (Fig.2 (c)). It is observed that when the angle fluctuation is small (<=5 degrees), the decoded BER performance for 1 dot/bit is better than 4 dots/bit due to the much lower code rate (0.225) and hence the much higher error correction capability of the LDPC code in the former case. However, when the angle fluctuationis large (for example, 15°), the decoded BER performance of the 1 dot/bit case becomes worse than the 4 dots/bit one because the write in error becomes increasingly dominant compared to the readback error caused by the inter-track interference (ITI) when the orientation fluctuation increases. However, for the 4 dots/bit case, the redundancy in the multi-island representation reduces the impact of the write in errors and media noise because the magnetic flux picked by the reader is the superposition of the magnetic fluxes from all the 4 dots when it scans over them. Even though when one dot in the 4 dots/bit pattern is written in mistake, the picked up magnetic flux is still quite likely to be correct. Here the greatly increased write in error and media noises (i.e., dominant at large orientation fluctuation) are more detrimental to the LDPC decoding performance compared to the read error caused by AWGN and ITI (i.e., dominant at small orientation fluctuation) for the 1 dot/bit case[3]. In conclusion, A channel modeling and multi-island representation scheme (4 dots/bit) was used to investigate the BPM with orientation fluctuation, which is compared to standard 1 dot/bit scheme. For the LDPC code encoded at the same user density, it is found that the decoded BER performance of the proposed 4 dots/bit scheme is better than 1 dot/bit scheme when the orientation fluctuation is large.

## LDPC-coded OFDM-system with BPSK modulation: Performance comparison with uncoded OFDM system

- **Status**: ❌
- **Reason**: 표준 LDPC-coded OFDM BPSK 성능 비교; 신규 디코더/구성/HW 기여 없는 표준 기법 단순 재사용
- **ID**: ieee:8376467
- **Type**: conference
- **Published**: 20-23 Apri
- **Authors**: Aneeqa Ramzan, Muhammad Omer Bin Saeed
- **PDF**: https://ieeexplore.ieee.org/document/8376467
- **Abstract**: This paper proposes an automated algorithm to correct loss of sub-carriers in Orthogonal Frequency Division Multiplexing (OFDM) system using Low-Density Parity-Check (LDPC) codes. OFDM transmits data on high bit-rate but high-peak-to-average ratio PAPR, subcarriers-loss due to deep fades in multipath causes 2-dimensional errors i.e., in time and frequency-domain, and inter-symbol-interference (ISI) etc. occurs in multipath OFDM system. In order to reduce such OFDM errors, error correcting codes have been used by researchers like Turbo-code, LDPC-code, ReedSolomon-code, Alamouti-code etc. LDPC-coded OFDM system is employed in the paper to correct 2D error and make improvement in OFDM BER curve. LDPC was first introduced by Gallager during his graduation in 1962. The main purpose for LDPC selection amongst all error correcting codes is its performance which is near Shannon limit. Information bits are encoded using LDPC and modulated using binary phase-shift-keying (BPSK). Then, OFDM system transmit subcarriers on channel and is demodulated using BPSK and decoded using LDPC at receiver to recover original information bits. Results show that LDPC-coded-OFDM performed better than un-coded-OFDM in terms of BER vs Eb/No (energy-per-bit to spectral-noise ratio) in decibels.

## Construction and decoding of OSMLD codes derived from unital and oval designs

- **Status**: ✅
- **Reason**: BIBD 기반 OSMLD 코드 신규 구성 + iterative threshold decoding — 바이너리 LDPC 계열 코드설계(E) 이식 가능
- **ID**: ieee:8360280
- **Type**: conference
- **Published**: 2-4 April 
- **Authors**: Otmane El Mouaatamid, Mohamed Lahmer, Mostafa Belkasmi
- **PDF**: https://ieeexplore.ieee.org/document/8360280
- **Abstract**: A construction of One-Step Majority-Logic Decodable (OSMLD) codes based on the incidence matrices of Balanced Incomplete Block Designs (BIBD) is given. In this paper, we focus on unital and oval designs which are constructed from a Projective Geometry (PG). Thus, we derive from the unital and oval designs new systematic and non-systematic OSMLD codes with rates and lengths not available with existing OSMLD codes. Simulation results show that the derived codes converge well under Iterative Threshold Decoding with an efficient trade-off between complexity and performances.

## Information Freshness Over an Interference Channel: A Game Theoretic View

- **Status**: ❌
- **Reason**: 간섭채널 정보신선도 게임이론 분석 — ECC/LDPC 무관
- **ID**: ieee:8486409
- **Type**: conference
- **Published**: 16-19 Apri
- **Authors**: Gam D. Nguyen, Sastry Kompella, Clement Kam +2
- **PDF**: https://ieeexplore.ieee.org/document/8486409
- **Abstract**: Communication over an interference channel, which is fundamental and pervasive in the wireless and wireline environment, is often intended to carry information among different transmitter-receiver pairs. For applications that require time critical updates, it is desirable to maintain the freshness of the received information, which is quantified by the age metric (unlike the familiar delay metric). In this paper, we consider the case of two transmitter-receiver pairs, and address the impact of interference on information freshness by formulating a two-player “interference” game, in which each player is a transmitter desiring to maintain the freshness of the information updates it sends to its receiver. The strategy of a player is the choice of power level at which it will transmit. We then derive both Nash and Stackelberg strategies for the game. Our analysis shows that the Stackelberg strategy uses less power than the Nash strategy, and that it dominates the Nash strategy (i.e., the Stackelberg total cost function is lower than the Nash total cost function). Our obtained Nash and Stackelberg strategies are desirable user operating points in competitive situations.

## Lightweight Retransmission for Random Access in Satellite Networks

- **Status**: ❌
- **Reason**: 위성 random access 재전송(ZigZag 디코딩) 프로토콜 — LDPC ECC 아님, 떼어낼 디코더 기법 없음
- **ID**: ieee:8485806
- **Type**: conference
- **Published**: 16-19 Apri
- **Authors**: Jing Chen, Feilong Tang, Heteng Zhang +1
- **PDF**: https://ieeexplore.ieee.org/document/8485806
- **Abstract**: Existing random access protocols designed for satellite networks have poor performance in short burst communications because of the difficulty on global time synchronization and frequent collisions. In this paper, we propose a Lightweight Retransmission (LwR) mechanism for random access in satellite networks to reduce collisions and get rid of synchronization requirement. In our LwR, only partial bits in a packet are retransmitted. Firstly, we formulate the lightweight retransmission problem and prove that it is NP-hard. Next, we focus on the construction of partial replicas, which is the core of our LwR, and propose regular and random construction methods. Especially, we prove the sufficient conditions for successfully decoding two conflicted packets by ZigZag. Finally, we propose an algebraic model and derive the upper and lower bounds of successfully decoding probability under different construction methods. Both theoretical analysis and experimental results reveal that the random construction method achieves higher decoding probability than the regular construction method. Simulation results also demonstrate that our LwR significantly outperforms related schemes designed for satellite networks.

## Reduced-Complexity Trellis Min-Max Decoder for Non-Binary Ldpc Codes

- **Status**: ❌
- **Reason**: Non-Binary LDPC GF(16) trellis min-max 디코더, 비이진 LDPC라 제외
- **ID**: ieee:8462192
- **Type**: conference
- **Published**: 15-20 Apri
- **Authors**: Huyen Pham Thi, Hanho Lee
- **PDF**: https://ieeexplore.ieee.org/document/8462192
- **Abstract**: In this paper, a novel algorithm and corresponding reduced-complexity decoder architecture are proposed for decoding the trellis min-max NB-LDPC code. This proposal reduces the number of messages exchanged between check node and variable node as well as the hardware complexity. Thus, the memory requirement and the wiring congestion is decreased, which increases the throughput of the decoder with a negligible error-correcting performance loss. A layered decoder architecture is implemented for the (2304, 2048) NB-LDPC code over GF(16) based on the proposed algorithm with a 90-nm CMOS technology. The results show an area reduction of 19.4% for the check node unit, 26.56% for the whole decoder and a throughput of 1396 Mbps with almost similar error-correcting performance, compared to previous works.

## A Shuffled-Based Iterative Demodulation and Decoding Scheme for Ldpc Coded Flash Memory

- **Status**: ✅
- **Reason**: TLC NAND 플래시 LDPC 직접(A), shuffled IDD + HW-friendly interleaver 구조로 이식 가능한 HW 기법(D)
- **ID**: ieee:8461609
- **Type**: conference
- **Published**: 15-20 Apri
- **Authors**: Li-Chung Lee, Wei-Min Lai, Mao-Ruei Li +1
- **PDF**: https://ieeexplore.ieee.org/document/8461609
- **Abstract**: In previous studies, a very sparse low-density parity-check (LDPC) code was designed for triple-level cell (TLC) NAND flash using non-Gray mapping, which is able to achieve comparable error-rate performance to the conventional Gray mapping-based scheme. Although a sparse LDPC code can be of benefit to hardware implementations of an iterative demodulation and decoding (IDD) scheme, difficulties emerge, such as latency issue between the decoder and demodulator, when compared to non-IDD schemes. In this paper, a hardware-friendly structure interleaver is used such that a shuffle-based IDD scheme can be realized efficiently. Compared to the conventional Gray-based non-IDD scheme and layered-based IDD scheme, the proposed shuffled-based IDD scheme can provide a better hardware efficiency and better error-rate performance.

## Faster-Than-Nyquist Signaling with Differential Encoding and Non Coherent Detection

- **Status**: ❌
- **Reason**: Faster-than-Nyquist 차동변조/비코히어런트 검출, LDPC 무관
- **ID**: ieee:8462455
- **Type**: conference
- **Published**: 15-20 Apri
- **Authors**: Takumi Ishihara, Shinya Sugiura
- **PDF**: https://ieeexplore.ieee.org/document/8462455
- **Abstract**: In this paper, we propose a novel differential faster-than-Nyquist (DFTN) signaling scheme, which allows us to dispense with any channel estimation at the receiver while benefiting from the rate boost of faster-than-Nyquist (FTN) signaling. At the transmitter, differentially modulated binary phase-shift keying (DBPSK) symbols are transmitted with the symbol interval that is smaller than that defined by the Nyquist criterion. The receiver noncoherently estimates the DBPSK symbols, suffering from the effects of FTN-specific inter-symbol interference (ISI), based on frequency-domain equalization. This is enabled, because FTN-specific lSI is deterministic, by assuming that the FTN's symbol packing ratio and the roll-off factor of a shaping filter are known in advance at the receiver.

## Performance analysis and optimization for LDPC coded OFDM systems with pulse blanking

- **Status**: ❌
- **Reason**: LDPC-OFDM pulse blanking 임계값 최적화, 무선응용 특이적이고 떼어낼 디코더·코드설계·HW 없음
- **ID**: ieee:8377021
- **Type**: conference
- **Published**: 15-18 Apri
- **Authors**: Yuan He, Ming Jiang, Xiaoning Wu +1
- **PDF**: https://ieeexplore.ieee.org/document/8377021
- **Abstract**: Pulse blanking is a common approach for impulsive interference mitigation in orthogonal frequency division multiplexing (OFDM) systems. The blanking threshold that decides whether a received signal is blanked or not, shows a crucial effect on the mitigation performance. Considering the influence of error correcting codes, we investigate the threshold optimization of pulse blanking for low-density parity-check (LDPC) coded OFDM systems. The protograph based extrinsic information transfer (PEXIT) charts and system simulations are used to tackle the optimization problem of blanking threshold with various LDPC coding schemes, which include different proto-graph structures, code lengths, code rates and the number of iterations. The simulation results show that the optimal blanking threshold changes with the code rate, whereas it remains the same regardless of the protograghs, code lengths and decoding iterations.

## Efficient multi-source network coding using low rank parity check code

- **Status**: ❌
- **Reason**: low rank parity check(rank metric) 코드 기반 멀티소스 네트워크코딩; 비-LDPC 랭크메트릭 부호, NAND 이식 기법 없음
- **ID**: ieee:8377229
- **Type**: conference
- **Published**: 15-18 Apri
- **Authors**: Imad El Qachchach, Oussama Habachi, Jean-Pierre Cances +1
- **PDF**: https://ieeexplore.ieee.org/document/8377229
- **Abstract**: Network coding (NC) is one of the promising high-performance techniques for wireless sensor networks (WSNs). However, few works have focused on the concerns of multi-source networks using error correcting codes. When an intermediate node fails errors may occur and since NC combines packets from different sources, several packets can be affected. In this paper, we propose a modified-low rank parity check (M-LRPC) decoding algorithm for a scenario with multiple source nodes. Furthermore, we investigate the performance of the proposed coding technique in terms of success decoding rate. Then, we derive an analytical expression for the decoding probability of the proposed M-LRPC. Simulation results are conducted in order to validate our analytical findings. These results show that the proposed scheme significantly improves the decoding probability compared to Gabidulin codes.

## ADMM hardware decoder for regular LDPC codes using a NISC-based architecture

- **Status**: ✅
- **Reason**: regular LDPC용 ADMM-LP NISC 기반 FPGA 디코더 HW 구현+BP 대비 자원비교; 이식 가능 HW 아키텍처(D)
- **ID**: ieee:8377331
- **Type**: conference
- **Published**: 15-18 Apri
- **Authors**: Imen Debbabi, Bertrand Le Gal, Nadia Khouja +2
- **PDF**: https://ieeexplore.ieee.org/document/8377331
- **Abstract**: The Alternate Direction Method of Multipliers (ADMM) approach is an original method for LDPC decoding based on the linear programming (LP) technique. It introduces a novelty at the error correction performance level. Nevertheless, this method can be toughly implemented due to its high computational complexity. In this paper, an implementation of the ADMM LP decoding algorithm on an FPGA target is presented. Its hardware resource cost is evaluated and compared with the state of the art LDPC decoders using the belief propagation (BP) decoding approach. The preliminary logic synthesis results show that an LP based hardware decoder for LDPC codes should be viable for applications with tough error correction requirements. However, additional research works are required to reach equivalent hardware complexity and throughput performances that are similar to traditional BP based LDPC decoders.

## Short length non-binary rate-adaptive LDPC codes for Slepian-Wolf source coding

- **Status**: ❌
- **Reason**: non-binary LDPC 기반 Slepian-Wolf 소스코딩(LDPCA); 비이진 LDPC+소스코딩으로 이중 제외
- **ID**: ieee:8377291
- **Type**: conference
- **Published**: 15-18 Apri
- **Authors**: Zeina Mheich, Elsa Dupraz
- **PDF**: https://ieeexplore.ieee.org/document/8377291
- **Abstract**: In this paper, we consider the construction of a Slepian-Wolf source coding scheme in a context where only a small amount of data has to be transmitted to the decoder. In this context, we propose a novel rate-adaptive Slepian-Wolf code construction that is based on non-binary LDPC codes. The construction we propose replaces the regular accumulator of the standard LDPCA method by a local graph that is optimized at every rate of interest. In our method, the local graph is specifically designed in order to give good decoding performance at short length, while existing LDPCA constructions are usually optimized under an infinite codeword length assumption. Our simulation results on short codes obtained from our design method show a FER improvement of up to an order to magnitude compared to the standard LDPCA construction.

## New concatenated code schemes for data gathering in WSN's using rank metric codes

- **Status**: ❌
- **Reason**: WSN 데이터수집용 LRPC(rank metric)+convolutional 연접부호; 비이진/비-LDPC, 떼어낼 LDPC 기법 없음
- **ID**: ieee:8377248
- **Type**: conference
- **Published**: 15-18 Apri
- **Authors**: Imad El Qachchach, Abdul Karim Yazbek, Oussama Habachi +2
- **PDF**: https://ieeexplore.ieee.org/document/8377248
- **Abstract**: In wireless sensor networks (WSNs), data produced by sensors are usually routed through several intermediate nodes to reach the sink Base Station (BS). In fact, since a WSN is usually composed of low-cost and limited capability sensors, their transmission range prevents the establishment of a reliable communication with the sink. When an intermediate node fails, errors may occur and the message is not delivered to the sink. The reliability of the system can be increased by using Network Coding (NC) techniques. In this paper, we consider the problem of data gathering in WSNs and we propose a novel error correction mechanism using Low Rank Parity Check code (LRPC), which is known to be good at correcting burst errors, as an outer code and a convolutional code as an inner code to correct sparse errors. Furthermore, we investigate the performance of the proposed system in terms of the packet error probability and the decoding complexity. We also propose a theoretical approximation of the decoding probability for LRPC codes in the case of network coding for binary and non-binary fields. We show, through Matlab simulations, that the proposed concatenated code outperforms the proposed coding schemes in the literature for data gathering in terms of decoding rate and complexity.

## Implementation aspects of a pipeline ADMM-based LP decoding of LDPC convolutional codes

- **Status**: ✅
- **Reason**: LDPC-CC용 ADMM-LP layered 파이프라인 디코딩+8비트 고정소수점 양자화+Euclidean projection skipping 최적화; 이식 가능한 디코더/HW 기법(C/D)
- **ID**: ieee:8377103
- **Type**: conference
- **Published**: 15-18 Apri
- **Authors**: Hayfa Ben Thameur, Bertrand Le Gal, Nadia Khouja +2
- **PDF**: https://ieeexplore.ieee.org/document/8377103
- **Abstract**: The enforcement of the linear programming (LP) decoding was recently extended to LDPC convolutional codes (LDPC-CC). It was demonstrated that their convolutional structure suites the message-passing based representation of the LP problem, thanks to the application of the alternating directions method of multipliers (ADMM). In this paper, a modified formulation of the ADMM-LP problem is introduced for pipeline decoding of LDPC-CCs based on the layered schedule. Moreover, an assessment of the fixed-point format required for hardware implementation is provided to evaluate the complexity of the underlying decoding algorithm. Simulations show that an 8-bit quantization scheme yields negligible error correction performances loss of about 0.05 dB regarding the floating-precision ADMM based LDPC-CC decoder. Further, an algorithmic optimization of the Euclidean projection skipping technique, described in [1] [2], is proposed. This improved version enables to reduce the computational complexity of the decoding process without memory penalty contrary to the original formulation.

## Short packet physical-layer network coding with mismatched channel state information

- **Status**: ❌
- **Reason**: 단패킷 물리계층 네트워크코딩+CSI mismatch; random coding bound 분석, LDPC 무관, 떼어낼 ECC 기법 없음
- **ID**: ieee:8377116
- **Type**: conference
- **Published**: 15-18 Apri
- **Authors**: Shakeel Salamat Ullah, Gianluigi Liva, Soung Chang Liew
- **PDF**: https://ieeexplore.ieee.org/document/8377116
- **Abstract**: Future multi-terminal communication networks such as machine-to-machine, telecommand and remote control communication systems will be based on short-packet transmissions. Physical-layer network coding (PNC) in such multi-terminal communication systems can potentially enhance network throughput and reduce communication latency. For practical PNC systems, preambles are contained in transmissions for accurate estimation of the channel-state-information (CSI). Identifying good preamble-length regimes, however, is critical for good performance of short-packet PNC systems. Long preambles for short packets reduce spectral efficiency. On the other hand, short preambles compromise accuracy of estimated CSI, leading to sub-par packet error rate (PER) performance. This paper studies the impact of preamble length on the performance of short-packet PNC systems. Specifically, we use random coding bound to quantify PER of channel-coded mismatched-CSI PNC systems and identify the preamble-length regime that achieves the target PER with minimum Eb/No. As an example, we consider a simple yet practically relevant setup of a BPSK modulated PNC system in a two-way relay channel operating with short packets of 128 symbols. Our results show that a preamble of 20 to 30 symbols provides the minimum PER for a wide range of Eb/N0 and achieves a target PER of 10-3 with minimum Eb/No.

## Flexible IR-HARQ scheme for polar-coded modulation

- **Status**: ❌
- **Reason**: Polar-coded IR-HARQ, 비-LDPC 부호 원칙 제외
- **ID**: ieee:8369005
- **Type**: conference
- **Published**: 15-18 Apri
- **Authors**: Peihong Yuan, Fabian Steiner, Tobias Prinz +1
- **PDF**: https://ieeexplore.ieee.org/document/8369005
- **Abstract**: A flexible incremental redundancy hybrid automated repeat request (IR-HARQ) scheme for polar codes is proposed based on dynamically frozen bits and the quasi-uniform puncturing (QUP) algorithm. The length of each transmission is not restricted to a power of two. It is applicable for the binary input additive white Gaussian noise (biAWGN) channel as well as higher-order modulation. Simulation results show that this scheme has similar performance as directly designed polar codes with QUP and outperforms LTE-turbo and 5G-LDPC codes with IR-HARQ.

## Belief propagation decoding of polar codes on permuted factor graphs

- **Status**: ✅
- **Reason**: polar 부호이나 permuted factor graph 기반 BP 디코딩 기법이 부호 비의존적 메시지패싱 개선으로 바이너리 LDPC BP에 이식 가능(예외 C)
- **ID**: ieee:8377158
- **Type**: conference
- **Published**: 15-18 Apri
- **Authors**: Ahmed Elkelesh, Moustafa Ebada, Sebastian Cammerer +1
- **PDF**: https://ieeexplore.ieee.org/document/8377158
- **Abstract**: We show that the performance of iterative belief propagation (BP) decoding of polar codes can be enhanced by decoding over different carefully chosen factor graph realizations. With a genie-aided stopping condition, it can achieve the successive cancellation list (SCL) decoding performance which has already been shown to achieve the maximum likelihood (ML) bound provided that the list size is sufficiently large. The proposed decoder is based on different realizations of the polar code factor graph with randomly permuted stages during decoding. Additionally, a different way of visualizing the polar code factor graph is presented, facilitating the analysis of the underlying factor graph and the comparison of different graph permutations. In our proposed decoder, a high rate Cyclic Redundancy Check (CRC) code is concatenated with a polar code and used as an iteration stopping criterion (i.e., genie) to even outperform the SCL decoder of the plain polar code (without the CRC-aid). Although our permuted factor graph-based decoder does not outperform the SCL-CRC decoder, it achieves, to the best of our knowledge, the best performance of all iterative polar decoders presented thus far.

## Randomized chained polar subcodes

- **Status**: ❌
- **Reason**: Polar subcode 구성/리스트 디코딩, 비-LDPC이며 디코더 polar 전용
- **ID**: ieee:8369001
- **Type**: conference
- **Published**: 15-18 Apri
- **Authors**: Peter Trifonov
- **PDF**: https://ieeexplore.ieee.org/document/8369001
- **Abstract**: A generalization of polar subcodes is proposed, which enables a simple construction of codes of arbitrary length. The obtained codes are shown to outperform punctured and shortened polar codes under list/sequential decoding. Furthermore, a simplified Gaussian approximation for polar codes is presented.

## On the construction of protograph based SC-LDPC codes for windowed decoding

- **Status**: ✅
- **Reason**: protograph 기반 SC-LDPC 윈도우 디코딩용 코드 설계+DE 최적화로 degree-1 회피·threshold 개선; 바이너리 코드설계 기여(E)
- **ID**: ieee:8377289
- **Type**: conference
- **Published**: 15-18 Apri
- **Authors**: Martin Schlüter, Najeeb Ul Hassan, Gerhard P. Fettweis
- **PDF**: https://ieeexplore.ieee.org/document/8377289
- **Abstract**: In this paper we optimize spatially coupled protographs for window decoding (WD) and arbitrary rate. Previous studies found that the belief propagation (BP) threshold of spatially coupled code ensembles achieves the maximum a posteriori (MAP) threshold of their underlying block code ensemble. This property requires a large coupling length L and thus the window decoder is considered to reduce latency and complexity of the decoding. To approach the BP threshold fast in the size of the window W, it is well known that the code requires a special structure to avoid degree-1 variable nodes inside the window. We further require additional structure to construct a systematic code with low encoding complexity, which unfortunately forces degree-1 variable nodes inside the window. Thus, we formulate an optimization problem to maximize the WD threshold and solve it by applying a differential evolution (DE) based algorithm. Compared to the regular protographs obtained by edge spreading, our optimized irregular protographs show a significant improvement in terms of WD threshold and finite length performance for small window sizes, hence leads to small decoding latency and complexity. Furthermore, for high rates our codes can compete with the highly optimized LDPC block codes from the WiMAX standard.

## IIC of the MIMO-FBMC/OQAM system using linear and SIC detection schemes in LTE channel

- **Status**: ❌
- **Reason**: MIMO-FBMC/OQAM 무선 수신기 IIC/SIC 간섭제거 논문; LDPC는 부수 사용, 떼어낼 부호/디코더/HW 기여 없음
- **ID**: ieee:8377031
- **Type**: conference
- **Published**: 15-18 Apri
- **Authors**: Yahya J. Harbi, Alister G. Burr
- **PDF**: https://ieeexplore.ieee.org/document/8377031
- **Abstract**: Iterative decoding has been widely used to achieve reliable high data rate transmission for broadband multi-carriers communication systems. However, in Multiple-Input Multiple-Output Orthogonal Frequency Division Multiplexing (MIMO-OFDM) systems with insufficient cyclic prefix (CP), there are significant challenges for efficient receiver design under the effect of the time-variant Long-Term Evolution (LTE) multipath channel. It means that the system performance may be degraded due to the inter-symbol interference (ISI) and inter-carrier interference (ICI) resulting from other transmitted signals. In this work, iterative interference cancellation (IIC) and MIMO-IIC with linear and successive interference cancellation (SIC) detection schemes are proposed using a Low-Density Parity-Check (LDPC) decoder for MIMO filter bank multicarrier/offset QAM (MIMO-FBMC/OQAM) and MIMO-OFDM systems. IIC and MIMO-IIC are used to calculate the ICI/ISI components from the estimated decoded signals and remove them from the received signals. SIC is used to reduce the cross interference from the other antenna. The bit error probability is compared with that of the MIMO-OFDM system with insufficient cyclic prefix (CP) under different environments. The results obtained indicate that IIC and MIMO-IIC can effectively mitigate error floors introduced by channel variation and insufficient CP with high bandwidth efficiency. With SIC detection, a second order diversity is approximately achieved.
