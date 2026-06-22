# IEEE Xplore — 2012-08


## Binary Burst Error Correcting Cyclic Codes Designed with the Circulant Parity Check Matrix

- **Status**: ❌
- **Reason**: 바이너리 순환부호(cyclic code) 버스트오류정정, 비-LDPC 부호 - 이식 가능 BP 기법 없음
- **ID**: ieee:6208785
- **Type**: journal
- **Published**: August 201
- **Authors**: Sina Vafi, Pham Huu Dung
- **PDF**: https://ieeexplore.ieee.org/document/6208785
- **Abstract**: The letter presents binary cyclic codes with the maximum burst error correction capability. This is achieved based on the properties of circulant parity check matrix. Results conclude existence of codes with high minimum weight and rate greater than 0.28. It also gives cyclic product codes suitable for multiple burst and random error corrections.

## Fountain Coding via Multiplicatively Repeated Non-Binary LDPC Codes

- **Status**: ❌
- **Reason**: 비이진(non-binary) LDPC 기반 fountain code; 비이진 LDPC 및 fountain/erasure 모두 제외 대상
- **ID**: ieee:6220213
- **Type**: journal
- **Published**: August 201
- **Authors**: Kenta Kasai, David Declercq, Kohichi Sakaniwa
- **PDF**: https://ieeexplore.ieee.org/document/6220213
- **Abstract**: We study fountain codes transmitted over the binary-input symmetric-output channel. For channels with small capacity, receivers in fountain coding systems needs to collects many channel outputs to recover information bits. Since a collected channel output yields a check node in the decoding Tanner graph, the channel with small capacity leads to large decoding complexity. In this paper, we introduce a novel fountain coding scheme with non-binary LDPC codes. The decoding complexity of the proposed fountain code does not depend on the channel. Numerical experiments show that the proposed codes exhibit better performance than conventional fountain codes, especially for moderate number of information bits.

## Piggybacking an Additional Lonely Bit on Linearly Coded Payload Data

- **Status**: ❌
- **Reason**: 선형부호 기반 추가비트 피기백 시그널링 기법, LDPC 디코더/코드설계 비의존
- **ID**: ieee:6189016
- **Type**: journal
- **Published**: August 201
- **Authors**: Erik G. Larsson, Reza Moosavi
- **PDF**: https://ieeexplore.ieee.org/document/6189016
- **Abstract**: We provide a coding scheme, by which an additional lonely bit can be piggybacked on a payload data packet encoded with a linear channel code, at no essential extra cost in power or bandwidth. The underlying principle is to use the additional bit to select which of two linear codes that should be used for encoding the payload packet, this way effectively creating a nonlinear code. We give a fast algorithm for detecting the additional bit, without decoding the data packet. Applications include control signaling, for example, transmission of ACK/NACK bits.

## Design of Convergence-Optimized Non-Binary LDPC Codes over Binary Erasure Channel

- **Status**: ❌
- **Reason**: 비이진(non-binary) LDPC 코드 설계 - 바이너리 LDPC만 포함 원칙에 따라 제외
- **ID**: ieee:6196162
- **Type**: journal
- **Published**: August 201
- **Authors**: Yang Yu, Wen Chen, Lili Wei
- **PDF**: https://ieeexplore.ieee.org/document/6196162
- **Abstract**: In this letter, we present a hybrid iterative decoder for non-binary low density parity check (LDPC) codes over binary erasure channel (BEC), based on which the recursion of the erasure probability is derived to design non-binary LDPC codes with convergence-optimized degree distributions. The resulting one-step decoding tree is cycle-free and achieves lower decoding complexity. Experimental studies show that the proposed convergence-optimization algorithm accelerates the convergence process by 33%.

## Pairwise Check Decoding for LDPC Coded Two-Way Relay Block Fading Channels

- **Status**: ❌
- **Reason**: 양방향 릴레이 PLNC 결합 부분디코딩(PCD), 무선 네트워크코딩 응용 특이적 - 떼어낼 일반 BP 기법 아님
- **ID**: ieee:6199942
- **Type**: journal
- **Published**: August 201
- **Authors**: Jianquan Liu, Meixia Tao, Youyun Xu
- **PDF**: https://ieeexplore.ieee.org/document/6199942
- **Abstract**: Partial decoding has the potential to achieve a larger capacity region than full decoding in two-way relay (TWR) channels. Existing partial decoding realizations are however designed for Gaussian channels and with a static physical layer network coding (PLNC). In this paper, we propose a new solution for joint network coding and channel decoding at the relay, called pairwise check decoding (PCD), for low-density parity-check (LDPC) coded TWR system over block fading channels. The main idea is to form a check relationship table (check-relation-tab) for the superimposed LDPC coded packet pair in the multiple access (MA) phase in conjunction with an adaptive PLNC mapping in the broadcast (BC) phase. Using PCD, we then present a partial decoding method, two-stage closest-neighbor clustering with PCD (TS-CNC-PCD), with the aim of minimizing the worst pairwise error probability. Moreover, we propose the minimum correlation optimization (MCO) for selecting the better check-relation-tabs. Simulation results confirm that the proposed TS-CNC-PCD offers a sizable gain over the conventional XOR with belief propagation (BP) in fading channels.

## Linear Precoding for MIMO Broadcast Channels With Finite-Alphabet Constraints

- **Status**: ❌
- **Reason**: MIMO BC 유한알파벳 선형 프리코딩 설계가 핵심; LDPC는 iterative decoding/detection 베이스라인 부수 언급, 떼어낼 디코더/HW/코드설계 기법 없음
- **ID**: ieee:6213037
- **Type**: journal
- **Published**: August 201
- **Authors**: Yongpeng Wu, Mingxi Wang, Chengshan Xiao +2
- **PDF**: https://ieeexplore.ieee.org/document/6213037
- **Abstract**: We investigate the design of linear transmit precoder for multiple-input multiple-output (MIMO) broadcast channels (BC) with finite alphabet input signals. We first derive an explicit expression for the achievable rate region of the MIMO BC with discrete constellation inputs, which is generally applicable to cases involving arbitrary user number and arbitrary antenna number. We further present a weighted sum rate upper bound of the MIMO BC with identical transmit precoding matrices. The resulting bound exhibits a serious performance loss because of the non-uniquely decodable transmit signals for MIMO BC with finite alphabet inputs in high signal-to-noise ratio (SNR) region. This performance loss motivates the use of a simple precoding to combat the non-unique decodability. Based on a constrained optimization problem formulation, we apply the Karush-Kuhn-Tucker analysis to derive necessary conditions for MIMO BC precoders to maximize the weighted sum-rate. We then propose an iterative gradient descent algorithm with backtracking line search to optimize the linear precoders for each user. Our { simulation} results under the practical transmit symbols of discrete constellations demonstrate significant gains by the proposed algorithm over other precoding schemes including the traditional iterative water-filling (WF) design for the Gaussian input signals. For the low-density parity-check coded systems, our precoder provides considerably coded BER improvement through iterative decoding and detection.

## Soft-Input Soft-Output Multiple Symbol Differential Detection for UWB Communications

- **Status**: ❌
- **Reason**: UWB용 SISO MSDD 반복검출, ECC는 외부 디코더로 부수 언급 - 떼어낼 LDPC 기법 없음
- **ID**: ieee:6211369
- **Type**: journal
- **Published**: August 201
- **Authors**: Qi Zhou, Xiaoli Ma
- **PDF**: https://ieeexplore.ieee.org/document/6211369
- **Abstract**: Multiple-symbol differential detection (MSDD) is a promising technique to enhance the performance of ultra-wideband (UWB) communications without estimating the channel explicitly. In this context, the generalized log-likelihood ratio test (GLRT) for MSDD was developed, and the hard-output multiple-symbol detector was proposed, which exhibits considerable bit-error-rate (BER) performance improvement over transmitted reference transmissions. In this paper, we further improve the system performance by incorporating error correction code (ECC) and iterative processing at the receiver. The soft-input soft-output (SISO) MSDD is developed to deliver a posteriori information to the outer ECC decoder and enables iterative detection and decoding. Simulations show that the iterative processing achieves significant gains over the existing MSDD in UWB communications.

## Nonbinary multiple rate QC-LDPC codes with fixed information or block bit length

- **Status**: ❌
- **Reason**: Nonbinary QC-LDPC for wireless; non-binary GF(q) explicitly excluded
- **ID**: ieee:6292249
- **Type**: journal
- **Published**: Aug. 2012
- **Authors**: Lei Liu, Wuyang Zhou, Shengli Zhou
- **PDF**: https://ieeexplore.ieee.org/document/6292249
- **Abstract**: In this paper, we consider nonbinary quasi-cyclic low-density parity-check (QC-LDPC) codes and propose a method to design multiple rate codes with either fixed information bit length or block bit length, tailored to different scenarios in wireless applications. We show that the proposed codes achieve good performance over a broad range of code rates.

## Perfect Secrecy Over Binary Erasure Wiretap Channel of Type II

- **Status**: ❌
- **Reason**: binary erasure wiretap channel 비밀키 합의(보안/secrecy); 패리티검사행렬 보안척도 최적화로 채널 ECC 기법 아님, 보안 제외
- **ID**: ieee:6200853
- **Type**: journal
- **Published**: Aug. 2012
- **Authors**: Won Taek Song, Jinho Choi, Jeongseok Ha
- **PDF**: https://ieeexplore.ieee.org/document/6200853
- **Abstract**: We introduce a binary erasure wiretap channel of type II in which the number of eavesdropped bits μ becomes available a posteriori. We aim at achieving perfect secrecy over such a channel model. The most appropriate application is a secret key agreement scheme. We present a secret key agreement scheme that adopts the formulation S = HX of Wyner-Ozarows's linear coset coding. The scheme is based on the following simple observation: even if some information on a secret message leaked out, I(S; Xμ) >; 0, where Xμ is a binary sequence of length μ, it is still possible to have perfect secrecy I(SJ; Xμ) = 0 for some subsequence SJ of S. Our secret key agreement scheme achieves perfect secrecy by taking only those subsequences SJ that are independent of the eavesdropped bits Xμ. Our secret key agreement scheme naturally leads to defining a security measure DH(μ) for parity-check matrices such that the eavesdropper gets zero information on SJ as long as the length of SJ is less than DH(μ). We study basic properties of DH(μ) and prove the perfect secrecy of our key agreement scheme. For parity-check matrices of small sizes, we perform an exhaustive search for matrices maximizing DH(μ).

## Delay-Cognizant Interactive Streaming of Multiview Video With Free Viewpoint Synthesis

- **Status**: ❌
- **Reason**: 멀티뷰 비디오 스트리밍 프레임 구조 최적화; LDPC/ECC 무관
- **ID**: ieee:6171861
- **Type**: journal
- **Published**: Aug. 2012
- **Authors**: Xiaoyu Xiu, Gene Cheung, Jie Liang
- **PDF**: https://ieeexplore.ieee.org/document/6171861
- **Abstract**: In interactive multiview video streaming (IMVS), a client receives and observes one of many available viewpoints of the same scene and periodically requests from the server view switches to neighboring views, as the video is played back in time uninterruptedly. One key technical challenge is to design a frame coding structure that facilitates periodic view switching and achieves an optimal tradeoff between storage cost and expected transmission rate. In this paper, we first propose three significant improvements over existing IMVS systems and then study the corresponding frame structure optimization. First, using depth-image-based rendering, the new IMVS system enables free viewpoint switching, i.e., by encoding and transmitting both texture and depth maps of captured views, a client can select and synthesize any virtual view from an almost continuum of viewpoints between the left-most and right-most captured views. Second, the IMVS system adopts a more realistic Markovian view-switching model with memory that more accurately captures user behaviors than previous memoryless models . A view-switching model is used in predicting client's future view-switching patterns. Third, assuming that the round-trip-time (RTT) delay during server-client communication is nonnegligible, during an IMVS session, the IMVS system additionally transmits redundant frames RTT into future playback, so that zero-delay view switching can be achieved. Given these improvements, we formalize a new joint optimization of the frame coding structure, transmission schedule, and quantization parameters of the texture and depth maps of multiple camera views. We propose an iterative algorithm to achieve fast and near-optimal solutions. The convergence of the algorithm is also demonstrated. Experimental results show that the proposed optimized rate-allocation method requires 38% lower transmission rate than the fixed rate-allocation scheme. In addition, with the same storage, the transmission rate of the optimized frame structure can be up to 55% lower than that of an I-frame-only structure and 27% lower than that of the structure without distributed source coding frames.

## Hardware Architecture of a Gaussian Noise Generator Based on the Inversion Method

- **Status**: ❌
- **Reason**: Gaussian noise generator HW (ICDF inversion) for simulation, not an LDPC decoder/code/ECC technique
- **ID**: ieee:6236107
- **Type**: journal
- **Published**: Aug. 2012
- **Authors**: R. Gutierrez, V. Torres, J. Valls
- **PDF**: https://ieeexplore.ieee.org/document/6236107
- **Abstract**: In this brief, we present a hardware-based Gaussian noise generator (GNG) with low hardware cost, high generation rate, and high Gaussian tail accuracy. The proposed generator is based on a piecewise polynomial approximation of the inverse cumulative distribution function (ICDF). We propose to avoid the area-demanding barrel-shifter of the ICDF approximation by means of creating a new uniform random sequence from the uniform random number generator output. The GNG architecture has been implemented in field-programmable gate array devices, and the implementation results are compared with other published designs, achieving a higher deviation with fewer hardware resources. Our GNG generates 242 Msps of random noise and achieves a tail of 13.1 $\sigma$ with 442 slices, two multipliers, and two Block-RAM of a Virtex-II device. The generator output successfully passed commonly used statistical tests.

## LP-Decodable Permutation Codes Based on Linearly Constrained Permutation Matrices

- **Status**: ❌
- **Reason**: LP-decodable permutation code 구성(순열행렬 기반); LDPC 채널 ECC 디코더/HW/코드설계 이식 기법 아님
- **ID**: ieee:6189389
- **Type**: journal
- **Published**: Aug. 2012
- **Authors**: Tadashi Wadayama, Manabu Hagiwara
- **PDF**: https://ieeexplore.ieee.org/document/6189389
- **Abstract**: A set of linearly constrained permutation matrices are proposed for constructing a class of permutation codes. The main feature of this class of permutation codes, called linear programming (LP)-decodable permutation codes, is this LP decodability. It is demonstrated that the LP decoding performance of the proposed class of permutation codes is characterized by the vertices of the code polytope of the code. Two types of linear constraints are discussed: one is structured constraints and the other is random constraints. The structured constraints allow an efficient encoding algorithm. On the other hand, the random constraints enable us to use probabilistic methods for analyzing several code properties such as the average cardinality and the average weight distribution.

## Applications of Belief Propagation in CSMA Wireless Networks

- **Status**: ❌
- **Reason**: CSMA 무선망 BP/GBP 추론 적용; 채널코딩 ECC가 아닌 네트워크 최적화 추론, 떼어낼 LDPC 디코더 기법 없음
- **ID**: ieee:6108317
- **Type**: journal
- **Published**: Aug. 2012
- **Authors**: Cai Hong Kai, Soung Chang Liew
- **PDF**: https://ieeexplore.ieee.org/document/6108317
- **Abstract**: “Belief propagation” (BP) is an efficient way to solve “inference” problems in graphical models, such as Bayesian networks and Markov random fields. It has found great success in many application areas due to its simplicity, high accuracy, and distributed nature. This paper is a first attempt to apply BP algorithms in CSMA wireless networks. Compared to prior CSMA optimization algorithms such as ACSMA, which are measurement-based, BP-based algorithms are proactive and computational, without the need for network probing and traffic measurement. Consequently, BP-based algorithms are not affected by the temporal throughput fluctuations and can converge faster. Specifically, this paper explores three applications of BP. 1) We show how BP can be used to compute the throughputs of different links in the network given their access intensities, defined as the mean packet transmission time divided by the mean backoff countdown time. 2) We propose an inverse-BP algorithm to solve the reverse problem of how to set the access intensities of different links to meet their target throughputs. 3) We introduce a BP-adaptive CSMA algorithm to find the link access intensities that can achieve optimal system utility. The first two applications are NP-hard problems, and BP provides good approximations to them. The advantage of BP is that it can converge faster compared to prior algorithms like ACSMA, especially in CSMA networks with temporal throughput fluctuations. Furthermore, this paper goes beyond BP and considers a generalized version of it, GBP, to improve accuracy in networks with a loopy contention graph. The distributed implementation of GBP is nontrivial to construct. A contribution of this paper is to show that a “maximal clique” method of forming regions in GBP: 1) yields accurate results; and 2) is amenable to distributed implementation in CSMA networks, with messages passed between one-hop neighbors only. We show that both BP and GBP algorithms for all three applications can yield solutions within seconds in real operation.

## Error correction circuits for bio-implantable electronics

- **Status**: ❌
- **Reason**: 바이오 임플란트용 ECC 회로 서베이로 구체적 신규 LDPC 디코더/구성/HW 기여 없음
- **ID**: ieee:6291981
- **Type**: conference
- **Published**: 5-8 Aug. 2
- **Authors**: Chris Winstead, Yi Luo
- **PDF**: https://ieeexplore.ieee.org/document/6291981
- **Abstract**: Methods are reviewed for achieving high data rates in bio-implantable devices. Particular attention is given to cortical stimulator arrays for restoring vision. Error-correction codes (ECC) are shown to be essential to obtain reliable operation in next-generation high-rate implants. A survey of reported ECC implementations is presented, and power-vs-performance tradeoffs are revealed after re-scaling to remove differences in technology and clock speed. Recommendations are offered for realizing high-rate ECC circuits within the tight power constraints of implantable device applications.

## Experimental PDM-OFDM Signal Transmission with Shaped Signal Constellations Achieving a Net Spectral Efficiency of 11.15 b/s/Hz over a Distance of

- **Status**: ❌
- **Reason**: 광통신 OFDM 전송 실험, LDPC는 BICM-ID FEC 베이스라인으로 부수 언급, 떼어낼 디코더/HW/구성 기법 없음
- **ID**: ieee:6293039
- **Type**: conference
- **Published**: 29-30 Aug.
- **Authors**: T. H. Lotz, X. Liu, S. Chandrasekhar +3
- **PDF**: https://ieeexplore.ieee.org/document/6293039
- **Abstract**: In this contribution we present a coded coherent optical orthogonal frequency-division multiplex (COOFDM) transmission scheme with reduced guard interval (RGI) and our latest results on achieving highest information spectral densities. In our scheme, a RGI is used to accommodate the intersymbol interference (ISI) with short memory, such as induced by transmitter bandwidth limitations or fiber polarization mode dispersion(PMD), while fiber chromatic dispersion (CD) with long memory and well-defined characteristics is mostly compensated within the receiver by a discrete Fourier transform (DFT)-based electronic dispersion compensation (EDC). We apply strong forward error correction (FEC) coding as an enhancement of bit interleaved coded modulation with iterative decoding (BICM-ID) by using low-density parity-check (LDPC) codes and shaped signal constellations (256-iterative polar modulation (IPM)) on the subcarriers of the OFDM system. We then present our latest experimental results on the generation and FEC-decoding of a polarization-division multiplexed (PDM)- OFDM signal with a net channel data rate of 231.5 Gb/s, occupying a bandwidth of 20.75 GHz. In an experiment on the performance of the developed system, transmission was performed over 800 km of ultra-large-area fiber (ULAF), achieving an intrachannel spectral efficiency (ISE) of 11.15 b/s/Hz with a coding gain of 15.1 dB compared to uncoded 256-QAM at a post-FEC BER of 10-15.

## Full diversity NB-LDPC coding with non-binary repetition symbols over the block-fading channel

- **Status**: ❌
- **Reason**: 비이진(non-binary) LDPC 코딩, 바이너리 한정 기준에 따라 제외
- **ID**: ieee:6328512
- **Type**: conference
- **Published**: 28-31 Aug.
- **Authors**: Matteo Gorgoglione, Valentin Savin, David Declercq
- **PDF**: https://ieeexplore.ieee.org/document/6328512
- **Abstract**: In this paper we propose a flexible coding scheme that achieves full diversity over the block-fading channel. The particularity of our approach is to rely on non-binary LDPC codes coupled with multiplicative non-binary codes, so that to easily adapt the coding rate to the number of fading blocks. A simple combining strategy is used at the receiver end before the iterative decoding, so that decoding can be performed on the same mother code. As a consequence, the decoding complexity is the same irrespectively of the number of fading blocks. Moreover, we propose an optimization of the non-binary multiplicative coefficients according to the Euclidian distance between the constellation points. Simulation results demonstrate that the proposed technique yields to a close-to-outage performance, with significant gains with respect to the binary LDPC codes from the literature.

## Single parity check product codes for erasure recovery in opportunistic spectrum access

- **Status**: ❌
- **Reason**: 단일패리티검사 곱부호 erasure 복구, 비-LDPC 부호이며 떼어낼 LDPC 디코더/HW/구성 기법 없음
- **ID**: ieee:6328333
- **Type**: conference
- **Published**: 28-31 Aug.
- **Authors**: Muhammad Moazam Azeem, Patrick Tortelier, Didier Le Ruyet
- **PDF**: https://ieeexplore.ieee.org/document/6328333
- **Abstract**: We address the use of single parity check product codes (SPCPC) for erasure recovery in opportunistic spectrum access schemes, where erasures are packets lost during a collision with the primary user (PU) due to sensing impairments (non detection). Our main motivation in using SPCPC is their low decoding complexity. We derive an analytical performance bound for these product codes when the PU's activity is described by a two-state On/Off model, and give a comparison with simulation results. The main result of the paper is the existence of a good functioning point on the receiver operating characteristic (ROC) curve [1] in terms of spectrum reuse efficiency for the secondary user (SU). Various product codes are compared according to their minimum distance, length and erasure recovery capability for different primary user's activity rate.

## Iterative detection/decoding of majority-logic decodable nonbinary LDPC codes over partial response channels

- **Status**: ❌
- **Reason**: nonbinary LDPC + PR 채널 joint detection/decoding, 비이진 LDPC라 제외
- **ID**: ieee:6325227
- **Type**: conference
- **Published**: 27-31 Aug.
- **Authors**: Shancheng Zhao, Xiao Ma, Baoming Bai
- **PDF**: https://ieeexplore.ieee.org/document/6325227
- **Abstract**: This paper is concerned with the applications of majority-logic decodable nonbinary low-density parity-check (LDPC) codes to partial response (PR) channels. We propose a joint detection/decoding algorithm that works in an iterative manner by exchanging messages between the Viterbi detector and a generalized majority logic decoder (GMLGD). The Viterbi detector is implemented over a sectionalized trellis. The hard-decisions made by the Viterbi detector are then passed to the decoder. The decoder delivers as output estimates of each coded symbols, which will be utilized in next iteration to update the branch metrics of the trellis. Since the proposed algorithm requires only integer operations and finite field operations, it can be implemented with simple combinational logic circuits. Simulation results and complexity analysis show that, when compared with the conventional turbo equalizer implemented with the BCJR algorithm and the Q-ary sum-product algorithm (BCJR-QSPA), the proposed algorithm has a much lower complexity but suffers from a little performance degradation. So the proposed algorithm provides a good candidate for trade-offs between performance and complexity.

## Low-density hybrid-check coded superposition mapping in BICM-OFDM

- **Status**: ❌
- **Reason**: superposition mapping+BICM-OFDM 무선 변조 응용, LDHC 코드설계가 비균등보호 변조 특화로 NAND 이식 기법 없음
- **ID**: ieee:6325225
- **Type**: conference
- **Published**: 27-31 Aug.
- **Authors**: Zhenyu Shi, Peter Adam Hoeher
- **PDF**: https://ieeexplore.ieee.org/document/6325225
- **Abstract**: Superposition mapping (SM) is known to be capacity achieving on the Gaussian channel, but an outer code is necessary because SM is a non-bijective modulation scheme. Towards this goal, the combination of SM with bit-interleaved coded modulation (BICM) has extensively been studied for the Gaussian channel. SM in conjunction with BICM-OFDM has recently been proposed by the authors for frequency-selective fading channels. In this paper, the results are extended by applying the concept of low-density hybrid-check (LDHC) coding. We propose a flexible overall code design taking adaptive bit loads into account. The performance of the system proposal is analyzed, with special focus on the degree allocation of the concatenated code, and the effect of iterations.

## ML vs. BP decoding of binary and non-binary LDPC codes

- **Status**: ❌
- **Reason**: binary vs non-binary LDPC ML/BP 비교 분석 — 신규 디코더/구성 기여 없는 비교 연구
- **ID**: ieee:6325201
- **Type**: conference
- **Published**: 27-31 Aug.
- **Authors**: Stefan Scholl, Frank Kienle, Michael Helmling +1
- **PDF**: https://ieeexplore.ieee.org/document/6325201
- **Abstract**: It has been shown that non-binary LDPC codes have a better error correction performance than binary codes for short block lengths. However, this advantage was up to now only shown under belief propagation decoding. To gain new insights, we investigate binary and non-binary codes under ML decoding. Our analysis includes different modulation schemes and decoding algorithms. For ML decoding under different modulation schemes a flexible integer programming formulation is presented. In this paper, we show that with respect to ML decoding short non-binary LDPC codes are not necessarily superior to binary codes. The decoding gain observed under BP decoding originates mainly in the more powerful non-binary decoding algorithm.

## Importance sampling for performance estimation of LDPC codes over Rayleigh fading channels

- **Status**: ❌
- **Reason**: Rayleigh fading 채널에서 importance sampling 성능추정 기법, 떼어낼 디코더/HW/코드설계 기여 없음
- **ID**: ieee:6325204
- **Type**: conference
- **Published**: 27-31 Aug.
- **Authors**: Seok-Ki Ahn, Kyeongcheol Yang
- **PDF**: https://ieeexplore.ieee.org/document/6325204
- **Abstract**: In this paper we propose a new importance sampling (IS) scheme to estimate the low error-rate performance of LDPC codes over a Rayleigh fading channel. It biases the Rayleigh fading distribution as well as the noise distribution in order to improve the quality of estimation. The proposed IS scheme is compared with the Monte-Carlo (MC) simulator and other IS schemes in terms of its efficiency and accuracy. Numerical results show that the proposed IS estimator is much more efficient than the MC estimator and other IS estimators from the viewpoint of the required simulation time. Furthermore, the proposed IS scheme provides a more accurate performance estimation of LDPC codes over a Rayleigh fading channel with only a limited simulation time than other IS schemes.

## Analysis and optimization of iteration schedules for LDPC coded modulation and detection

- **Status**: ❌
- **Reason**: LDPC coded modulation/detection iteration schedule 최적화(EXIT 곡선), 변조·검출 결합 무선 응용으로 떼어낼 ECC 기법 없음
- **ID**: ieee:6325229
- **Type**: conference
- **Published**: 27-31 Aug.
- **Authors**: Laurent Schmalen, Stephan ten Brink, Andreas Leven
- **PDF**: https://ieeexplore.ieee.org/document/6325229
- **Abstract**: In this paper, we consider iterative detection in combination with an outer low-density parity-check (LDPC) code, and present new EXIT curves that help to optimize the decoding schedule among these blocks. For this, we compute a set of (inner) detector and variable node decoder curves depending on whether or not the detector update is included into the iteration loop; interestingly, this involves the differentiation of EXIT curves. We illustrate the schedule optimization using examples such as an inner equalizer for partial response channels. The new design insights are confirmed by trajectory simulations and are used to find the detector execution order minimizing the bit error rate at a given channel quality.

## Multi-relay cooperative NB-LDPC coding with non-binary repetition codes over block-fading channels

- **Status**: ❌
- **Reason**: non-binary LDPC + 비이진 repetition 협력코딩, 비이진 LDPC라 제외
- **ID**: ieee:6333864
- **Type**: conference
- **Published**: 27-31 Aug.
- **Authors**: Valentin Savin, David Declercq, Stephan Pfletschinger
- **PDF**: https://ieeexplore.ieee.org/document/6333864
- **Abstract**: In this paper, we propose a cooperative coding scheme to communicate efficiently over multiple-relay fading channels. The particularity of our approach is to rely on non-binary LDPC codes at the source, coupled with non-binary repetition codes at the relays. A simple joint decoding strategy is used at the receiver end, so that the decoding complexity is not increased compared to a system without relays, while preserving the coding gain brought by re-encoding the signal at the relays. We show by simulations that the proposed scheme allows maintaining a constant gap to the outage probability of the cooperative system, irrespective of the number of relays.

## Spatially coupled LDPC codes for two-user decode-and-forward relaying

- **Status**: ❌
- **Reason**: two-user decode-and-forward 릴레이용 SC-LDPC, 표준 SC-LDPC를 릴레이/네트워크코딩에 적용 — 무선 응용, 신규 구성 기여 없음
- **ID**: ieee:6325196
- **Type**: conference
- **Published**: 27-31 Aug.
- **Authors**: Stefan Schwandter, Alexandre Graell i Amat, Gerald Matz
- **PDF**: https://ieeexplore.ieee.org/document/6325196
- **Abstract**: We present a decode-and-forward transmission scheme that is based on spatially coupled LDPC codes and applies to a network consisting of two sources, one relay, and one destination. The relay performs network coding to achieve full diversity. We prove analytically that the proposed scheme achieves the Shannon limit on the binary erasure relay channel for symmetric channel conditions. Using density evolution, we furthermore demonstrate that our scheme approaches capacity also for asymmetric channel conditions.

## NB-LDPC: Absorbing set and importance sampling

- **Status**: ❌
- **Reason**: non-binary LDPC absorbing set/IS 기준 제외(비이진 LDPC)
- **ID**: ieee:6325207
- **Type**: conference
- **Published**: 27-31 Aug.
- **Authors**: A. Poloni, S. Valle, S. Vincenti
- **PDF**: https://ieeexplore.ieee.org/document/6325207
- **Abstract**: The identification of error sources when sub-optimal decoding algorithms are used is an open point both in binary and non-binary LDPC. Here a mathematical definition for absorbing sets in the case of non-binary LDPC is given and several examples are proposed to illustrate it. The definition is consistent with the error patterns resulting from Montecarlo (MC) simulations at high SNR. The absorbing sets patterns, as defined here, are used to predict the error floor of NB-LDPC with the Importance Sampling (IS). The IS and the MC simulation results match up very well when both are available.

## Interleaver design for spectrally-efficient bit-interleaved LDPC-coded modulation

- **Status**: ❌
- **Reason**: BICM 인터리버 설계(매핑 분포 최적화)는 변조-인터리빙 응용 특이적이고 NAND LDPC ECC로 떼어낼 디코더·구성 기법 없음
- **ID**: ieee:6325235
- **Type**: conference
- **Published**: 27-31 Aug.
- **Authors**: Stefan Nowak, Ruediger Kays
- **PDF**: https://ieeexplore.ieee.org/document/6325235
- **Abstract**: A design methodology for interleavers in bit-interleaved coded modulation systems deploying (binary irregular) low-density parity-check (LDPC) codes and higher-order modulation is presented. The interleaver is introduced to balance unequal error protection characteristics inherent in coding and modulation. For this purpose, mapping distributions are used to describe the interleaver configuration. Furthermore, an optimization procedure is applied to derive good mapping distributions for practical block lengths in the order of 102-103 bits. Exemplary numerical results are presented for higher-order modulation and LDPC codes as defined in the IEEE standard 802.11n.

## A simple proof of threshold saturation for coupled scalar recursions

- **Status**: ❌
- **Reason**: threshold saturation 순수 이론 증명(potential function) — 디코더/HW/구성으로 안 이어짐
- **ID**: ieee:6325197
- **Type**: conference
- **Published**: 27-31 Aug.
- **Authors**: Arvind Yedla, Yung-Yih Jian, Phong S. Nguyen +1
- **PDF**: https://ieeexplore.ieee.org/document/6325197
- **Abstract**: Low-density parity-check (LDPC) convolutional codes (or spatially-coupled codes) have been shown to approach capacity on the binary erasure channel (BEC) and binary-input memoryless symmetric channels. The mechanism behind this spectacular performance is the threshold saturation phenomenon, which is characterized by the belief-propagation threshold of the spatially-coupled ensemble increasing to an intrinsic noise threshold defined by the uncoupled system. In this paper, we present a simple proof of threshold saturation that applies to a broad class of coupled scalar recursions. The conditions of the theorem are verified for the density-evolution (DE) equations of irregular LDPC codes on the BEC, a class of generalized LDPC codes, and the joint iterative decoding of LDPC codes on intersymbol-interference channels with erasure noise. Our approach is based on potential functions and was motivated mainly by the ideas of Takeuchi et al. The resulting proof is surprisingly simple when compared to previous methods.

## Near Shannon limit precoded concatenated zigzag codes

- **Status**: ❌
- **Reason**: concatenated zigzag(turbo-like) 코드, 비-LDPC이고 LDPC BP 이식 디코더 기법 없음
- **ID**: ieee:6325212
- **Type**: conference
- **Published**: 27-31 Aug.
- **Authors**: Sheng Tong, Li Ping, Baoming Bai
- **PDF**: https://ieeexplore.ieee.org/document/6325212
- **Abstract**: Concatenated zigzag (CZ) codes are a class of multidimensional parallel concatenated codes, which have some favorable properties, such as low encoding and decoding complexities and rate compatibility. However, there is a noticeable gap between the performance of a standard CZ code and the corresponding Shannon limit. To overcome this problem, we apply the precoding technique recently developed by Abbasfar et al. to CZ codes, resulting in a novel class of turbo-like codes, termed precoded CZ codes. The EXIT chart tool is used for convergence analysis and performance optimization. We show that the proposed precoded CZ codes have thresholds within 0.25 dB of the Shannon limit for a wide code rate range of [0.5, 20/21]. Extensive simulation results are provided to demonstrate that optimized precoded CZ codes exhibit good performance at different code rates and different block lengths.

## Distributed source coding: Application in biometrics

- **Status**: ❌
- **Reason**: distributed source coding 기반 생체인식 템플릿 저장, 채널 ECC 아닌 소스코딩/보안 응용
- **ID**: ieee:6333854
- **Type**: conference
- **Published**: 27-31 Aug.
- **Authors**: Maurício Ramalho, Sanchit Singh, Paulo Lobato Correia +1
- **PDF**: https://ieeexplore.ieee.org/document/6333854
- **Abstract**: Distributed source coding (DSC) applications range from sensor networks to video coding. In this paper, DSC principles are integrated in a biometric system to provide secure template storage. The proposed biometric recognition system uses the palmprint as a biometric trait together with a state-of-the-art feature extraction technique that produces binary templates. The hand images are captured in an unconstrained way, i.e., the user can place his hand freely within the camera's field of view and the background is not required to be constant. The proposed system was tested in indoor environments and promising recognition accuracy results were achieved, when performing identification on a small database, acquired using the proposed system.

## Bidirectional broadcasting by using multi-edge type LDPC convolutional codes

- **Status**: ❌
- **Reason**: 양방향 브로드캐스트 채널용 MET-LDPC convolutional 코드, 무선응용 특이적이며 표준 MET 구성, NAND 이식 기법 없음
- **ID**: ieee:6325205
- **Type**: conference
- **Published**: 27-31 Aug.
- **Authors**: Zhongwei Si, Ragnar Thobaben, Mikael Skoglund +1
- **PDF**: https://ieeexplore.ieee.org/document/6325205
- **Abstract**: In this paper we propose multi-edge type (MET) LDPC convolutional codes for the bidirectional broadcast channel with common message (BBC-CM). It describes a two-user broadcast channel in which different subsets of the broadcasted messages are a priori known at the receivers. This situation occurs, e.g., in the second transmission phase of a bidirectional relaying protocol. In the proposed scheme, the transmitter broadcasts codewords of an MET LDPC convolutional code. Each user tries then to recover the unknown messages by decoding a two-edge type code which is embedded in the MET code. We prove for each user that the two-edge type LDPC convolutional code has the same properties as a standard LDPC convolutional code, and therefore it is capacity achieving for the binary erasure channel (BEC) and the general binary memoryless symmetric (BMS) channel. Meanwhile, we show that the capacity region of the BBC-CM is achieved. Numerical results with finite node degrees show that the achievable rates approach the channel capacities in both BECs and BI-AWGN channels.

## Signal recovery performance of the interval-passing algorithm

- **Status**: ❌
- **Reason**: compressed sensing 신호복원 알고리즘(IPA), 채널 ECC 디코더 아님
- **ID**: ieee:6325208
- **Type**: conference
- **Published**: 27-31 Aug.
- **Authors**: Vida Ravanmehr, Ludovic Danjean, Bane Vasić +1
- **PDF**: https://ieeexplore.ieee.org/document/6325208
- **Abstract**: This paper considers an iterative algorithm called the Interval-Passing Algorithm (IPA) which is used to reconstruct non-negative real signals using binary measurement matrices in compressed sensing (CS). The failures of the algorithm on stopping sets, also non-decodable configurations in iterative decoding of LDPC codes over the binary erasure channel (BEC), shows a connection between iterative reconstruction algorithm in CS and iterative decoding of LDPC codes over the BEC. In this paper, a stopping-set based approach is used to analyze the recovery of the IPA. We show that a smallest stopping set is not necessarily a smallest configuration on which the IPA fails and provide sufficient conditions under which the IPA recovers a sparse signal whose non-zero values lie on a subset of a stopping set. Reconstruction performance of the IPA using IEEE 802.16e LDPC measurement matrices are provided to show the effect of the stopping sets in the performance of the IPA.

## Improved message passing techniques in fast correlation attacks on stream ciphers

- **Status**: ❌
- **Reason**: 스트림암호 fast correlation attack(보안/암호해석)으로 girth-4 코드 적용 — 채널 ECC 아님, 보안 도메인 제외
- **ID**: ieee:6325183
- **Type**: conference
- **Published**: 27-31 Aug.
- **Authors**: Martin Ågren, Martin Hell, Thomas Johansson +1
- **PDF**: https://ieeexplore.ieee.org/document/6325183
- **Abstract**: The fast correlation attack is a general cryptanalytic attack directed at stream ciphers and is related to the decoding of low-density parity-check (LDPC) codes. In this paper, we improve the message passing algorithm by exploiting the fact that the sum of an arbitrary number of initial state variables, called a fixed point, can be written as the sum of only a few other variables. This will result in better use of information in the message passing algorithm. Simulations show that this added information results in better success probabilities for the attack. Our technique may also find applications to LDPC codes with girth 4, although such codes are normally avoided.

## An EXIT-chart aided optimization of bit mapping for DVB-C2 system

- **Status**: ❌
- **Reason**: DVB-C2 비트매핑/coded-modulation 최적화, LDPC는 베이스라인이고 떼어낼 디코더/구성 기법 없음
- **ID**: ieee:6314373
- **Type**: conference
- **Published**: 27-31 Aug.
- **Authors**: Keqian Yan, Kewu Peng, Fang Yang +2
- **PDF**: https://ieeexplore.ieee.org/document/6314373
- **Abstract**: Due to the unequal error protection (UEP) property of both the irregular low-density parity-check (LDPC) code and the higher-order modulation, bit mapping is proposed as a joint optimization of the LDPC coded-modulation scheme. In this paper, we discuss the bit mapping optimization performed by employing an additional DEMUX following the given bit interleaver, and then apply it to the second generation digital video broadcasting system for cable (DVB-C2). The extrinsic information transfer (EXIT) chart technique is adopted to analyze the influence of bit mapping on the iterative decoding process. Based on the EXIT-chart analysis, an optimization method is proposed to design the DEMUX for performance improvement. As an example, we re-design the DEMUX for the DVB-C2 system with reduced DEMUX width. The superior performance of the optimized DEMUX is verified by the bit error rate (BER) simulation.

## Modeling Adaptive Coded Modulation in real time partially reconfigurable mobile terminals

- **Status**: ❌
- **Reason**: Non-binary LDPC 기반 WiMAX 적응변조 설계 — 비이진 LDPC는 제외 대상
- **ID**: ieee:6334015
- **Type**: conference
- **Published**: 27-31 Aug.
- **Authors**: L. Conde-Canencia, Y. Eustache, J.-C. Prévotet +1
- **PDF**: https://ieeexplore.ieee.org/document/6334015
- **Abstract**: This paper considers the design of partially reconfigurable WiMAX 802.16m mobile terminals that use Adaptive Coding and Modulation techniques to enhance the Quality Of Service. Non-binary LDPC codes (with three different coding rates) and three different modulation schemes are considered. As this kind of design requires a huge amount of time and resources to lead to an operational platform, our approach is based on a methodology that describes the complete platform at high level of abstraction. This approach considerably reduces the design time, as it helps the designer in making good choices prior to the final implementation.

## Fast simulation of turbo codes on GPUs

- **Status**: ❌
- **Reason**: turbo 코드 GPU 시뮬레이션 — 비-LDPC, 시뮬 가속이라 LDPC BP 이식 디코더 기법 없음
- **ID**: ieee:6325199
- **Type**: conference
- **Published**: 27-31 Aug.
- **Authors**: Stefano Chinnici, Paolo Spallaccini
- **PDF**: https://ieeexplore.ieee.org/document/6325199
- **Abstract**: Simulation of turbo codes with moderately long block lengths down to bit error rates of the order of 10-9 requires long runtimes on conventional CPUs. The approach described in this paper is based on a CPU/GPU co-processing strategy which aims at effectively distributing the processing tasks between the two platforms. In this paper, the most computationally intensive parts of turbo codes simulation are analyzed and their implementation on the GPU parallel architecture is discussed. Results on a case study for a serial concatenated convolutional code are presented, showing a simulation speed-up in excess of 10×. These initial results show that the CPU/GPU approach is a powerful tool that allows the characterization of the high SNR behavior of turbo codes with a short simulation runtime.

## Irregular repeat accumulate codes with few iterations for the binary adder channel

- **Status**: ❌
- **Reason**: binary adder channel용 IRA 코드, multiuser interference cancellation 응용 특화로 NAND 이식 기법 없음(IRA는 비-LDPC)
- **ID**: ieee:6325230
- **Type**: conference
- **Published**: 27-31 Aug.
- **Authors**: Guangsong Wang, Ingmar Land, Alex Grant
- **PDF**: https://ieeexplore.ieee.org/document/6325230
- **Abstract**: Iterative interference cancellation is a powerful technique for design of multiuser decoders. Careful encoder and decoder design is essential for reducing implementation complexity. When used in conjunction with iteratively-decodeable sparse graph codes, there is a choice to be made between the number of multiuser interference cancellation stages and the number of iterations used for decoding each user's code. Too few decoder iterations may increase the number of interference cancellation steps, whereas too many may superfluous, or even inhibit the convergence behaviour of the cancellation loop. In this paper we design non-systematic irregular repeat-accumulate codes for multiple-access channels where the number of cancellation stages and number of decoder iterations at each stage are fixed. The design goal is minimal bit error rate. Our formulation is based on extrinsic information transfer, and introduces the number of iterations directly into the curve fitting problem. For clear development of concepts, we restrict attention to the binary adder channel, where our approach is exact. Generalisation to other sparse graph codes and other multiple-access channels is straightforward, subject to the usual approximations.

## Random clique codes

- **Status**: ❌
- **Reason**: 신경망 연상메모리 기반 clique 코드, LDPC ECC 디코더 아니고 점근 good code 이론, 이식 기법 없음
- **ID**: ieee:6325211
- **Type**: conference
- **Published**: 27-31 Aug.
- **Authors**: Vincent Gripon, Vitaly Skachek, Warren J. Gross +1
- **PDF**: https://ieeexplore.ieee.org/document/6325211
- **Abstract**: A new family of associative memories based on sparse neural networks has been recently introduced. These memories achieve excellent performance thanks to the use of error-correcting coding principles. In this work, we introduce a new family of codes termed clique codes. These codes are based on the cliques in balanced n-partite graphs describing associative memories. In particular, we study an ensemble of random clique codes, and prove that such ensemble contains asymptotically good codes. Furthermore, these codes can be efficiently decoded using the neural networks based associative memories with limited complexity and memory consumption.

## Multiple description analog joint source-channel coding for parallel channels with side information

- **Status**: ❌
- **Reason**: 아날로그 JSCC(병렬 AWGN) — LDPC 무관, 떼어낼 ECC 기법 없음
- **ID**: ieee:6334019
- **Type**: conference
- **Published**: 27-31 Aug.
- **Authors**: Iker Alustiza, Aitor Erdozain, Pedro Crespo +1
- **PDF**: https://ieeexplore.ieee.org/document/6334019
- **Abstract**: With the purpose of reducing the coding complexity and delay of the separation-based schemes, an analog joint source-channel coding scheme is proposed for transmissions through parallel AWGN channels with side information at the receiver. This scheme divides the bidimensional source space into a set of hexagons and transmits the relative position of the source vectors inside the corresponding hexagon by using two complimentary analog mappings. The results are satisfactory, specially taking into consideration the low complexity and delay of the proposed scheme.

## Decentralized power control for random access with iterative multi-user detection

- **Status**: ❌
- **Reason**: ALOHA 랜덤액세스 전력제어+iterative MUD — 무선 응용 특이적, 떼어낼 LDPC ECC 기법 없음
- **ID**: ieee:6325189
- **Type**: conference
- **Published**: 27-31 Aug.
- **Authors**: Chongbin Xu, Peng Wang, Sammy Chan +1
- **PDF**: https://ieeexplore.ieee.org/document/6325189
- **Abstract**: This paper is concerned with the application of iterative multi-user detection (MUD) in ALOHA-type random access systems. We focus on a random-power transmission scheme, in which the transmission power level of each user is randomly selected according to a certain distribution f. We aim at designing f to maximize the system throughput given an average power constraint for each user. We adopt a suboptimal scheme, in which only type-2 collisions (collisions involving two packets) are resolved. We first prove that, the support (i.e., the smallest closed set whose complement has zero probability) of the optimal f in this case is a discrete set for systems with certain feasible regions (the set of power profiles that can support reliable communications). The related discrete set can be easily obtained according to the boundaries of the feasible region. We then apply this finding to the design of f. Numerical results show that with iterative MUD, the proposed scheme can achieve noticeable performance improvement compared with the conventional ALOHA and offer flexible tradeoff between the system throughput and power consumption.

## Compressive linear network coding for efficient data collection in wireless sensor networks

- **Status**: ❌
- **Reason**: 네트워크 코딩+소스 압축 BP — 채널 ECC가 아닌 압축/상관복원, 떼어낼 LDPC 기법 없음
- **ID**: ieee:6334252
- **Type**: conference
- **Published**: 27-31 Aug.
- **Authors**: Francesca Bassi, Chao Liu, Lana Iwaza +1
- **PDF**: https://ieeexplore.ieee.org/document/6334252
- **Abstract**: We address the problem of data collection in a wireless sensor network. Network coding is used for data delivery. The correlation between the measurements is exploited to recover the data at the sink, even in case of rank-deficient network matrix. The network coding operations are seen as lossy source compression, achieved by a finite-field random code generated during transmission. Decoding is performed using belief propagation on a factor graph which accounts for the correlation between the sensor measurements. Experimental results illustrate the performance of this technique for various field sizes and correlation levels.

## Bandwidth-reduction analog mappings for AWGN channels with side information

- **Status**: ❌
- **Reason**: 아날로그 매핑 JSCC(Wyner-Ziv) — LDPC 무관, 채널 ECC 기법 없음
- **ID**: ieee:6334023
- **Type**: conference
- **Published**: 27-31 Aug.
- **Authors**: Iker Alustiza, Aitor Erdozain, Pedro Crespo +1
- **PDF**: https://ieeexplore.ieee.org/document/6334023
- **Abstract**: Recently, the joint source-channel coding schemes based on analog mappings have gained prominence. Their simplicity and low delay compared to other coding strategies make them more suitable for real-time applications. In this work, we propose a novel joint source-channel coding scheme, based also on analog mappings, for a point-to-point communication channel with side information at the receiver (also known as Wyner-Ziv scenario).

## A grouped decoding algorithm for non-binary LDPC code with Quasi-orthogonal STBC in MIMO system

- **Status**: ❌
- **Reason**: non-binary LDPC + GF(q) grouped decoding, 비이진 LDPC라 제외
- **ID**: ieee:6418657
- **Type**: conference
- **Published**: 27-29 Aug.
- **Authors**: Yier Yan, Xueqing Jiang, Wei Duan +2
- **PDF**: https://ieeexplore.ieee.org/document/6418657
- **Abstract**: We extend the group decoding algorithm [1] for space time block code (STBC) to the non-binary low density parity check code (LDPC) with Quasi-Orthogonal STBC in multiple-input and multiple-output (MIMO) system. A Gaussian based detection is proposed to reduce the decoding complexity in this paper. The complexity involved grows linearly with the number of transmit antennas and size of Galois Field. The simulation result shows that the Gaussian based detection is reasonable to employ in this system.

## Distributed joint source and channel code with correlated information sources

- **Status**: ❌
- **Reason**: 분산 결합 소스-채널 부호화(DJSCC) - JSCC, LDPC 베이스라인, 떼어낼 ECC 기법 없음
- **ID**: ieee:6356923
- **Type**: conference
- **Published**: 15-17 Aug.
- **Authors**: Ning Sun, Jingxian Wu, Hai Lin
- **PDF**: https://ieeexplore.ieee.org/document/6356923
- **Abstract**: In this paper, a new distributed joint source-channel code (DJSCC) is proposed for a communication network with multiple correlated information sources. The DJSCC is performed by puncturing the information bits of a linear block code but leaving the parity bits intact, given the fact that the correlation among the parity bits is usually much lower compared to the corresponding information bits. In recognition of the different roles of the information and parity bits in the DJSCC scheme, we propose to allocate unequal amounts of energy per bit to these two different types of bits. The unequal energy allocation leads to significant performance gains over conventional equal energy transmissions. At the receiver, the sources are jointly decoded with the iterative message passing algorithm. Simulation results demonstrate that the proposed scheme can achieve considerable performance gains over conventional schemes.

## LDPC code construction for wireless physical-layer key reconciliation

- **Status**: ❌
- **Reason**: 무선 물리계층 키 reconciliation용 LDPC(Slepian-Wolf) - 정보조정 영역, 떼어낼 디코더/HW 기법 없음
- **ID**: ieee:6356879
- **Type**: conference
- **Published**: 15-17 Aug.
- **Authors**: Jalal Etesami, Werner Henkel
- **PDF**: https://ieeexplore.ieee.org/document/6356879
- **Abstract**: The paper describes a reconciliation procedure for physical key generation based on specially designed LDPC codes using Slepian-Wolf-type coding. The LDPC codes are optimized for intrinsic information with two different noise variances within the same codeword.

## The implementation of encoder and decoder of LT codes based on DSP

- **Status**: ❌
- **Reason**: LT rateless 부호 DSP 구현 - 비-LDPC fountain 부호, NAND 채널 ECC 이식 기법 없음
- **ID**: ieee:6308140
- **Type**: conference
- **Published**: 15-17 Aug.
- **Authors**: Junhong Hu, Hongfeng Gao, Shi Ge
- **PDF**: https://ieeexplore.ieee.org/document/6308140
- **Abstract**: LT codes are efficient rateless codes. In this article, the TMS320VC5416 is used to design and realize the encoder and decoder of LT codes. In order to improve the decoding efficiency, the redundancy process is introduced to remove the redundancies of code signals. As the computational burden and memory usage of the encoder and decoder increase rapidly with the encoding length, the feedback control signal is introduced to control the length of code signals. Positional coefficient storage mechanism of neighbors' list of the code signals is built to ensure the optimal use of DSP chip's memory resources. The simulation results show that the LT codes encoder and decoder based on DSP have good performance.

## Performance evaluation of rate less channel coding for MU-MIMO OFDM-LTE systems

- **Status**: ❌
- **Reason**: LT/rateless·erasure 코드와 무선 MU-MIMO 성능비교, 표준 LDPC는 베이스라인일 뿐 떼어낼 기법 없음
- **ID**: ieee:6335637
- **Type**: conference
- **Published**: 12-15 Aug.
- **Authors**: P. Krishna, K. Kishan Rao, T. Anilkumar +1
- **PDF**: https://ieeexplore.ieee.org/document/6335637
- **Abstract**: 3GPP Long term evolution (LTE) wireless broadband is intended to provide higher data rates and throughput with less latency. Due to the channel impairments of the radio channel and higher order modulation techniques, the probabilities of errors are high. Using belief propagation algorithm both irregular and regular Low Density Parity Codes (LDPC) have showed to achieve rates close to the capacity on the other channels like Binary Symmetric channel (BSC) and Additive White Gaussian Noise Channel (AWGNC) with channel state information (CSI) available at both transmitter and receiver. Furthermore, Rate less codes is a class of codes without a predefined number of encoding symbols. Luby Transform (LT) code a class of rate less codes provides an efficient way to transfer information over erasure channels like Internet. In this paper, the performance of LDPC (irregular, regular) and LT codes are investigated and the results illustrate the performance gains of LT codes for Multi user Multiple Inputs and Multiple Outputs in combination with orthogonal frequency division multiplexing system over LDPC codes with the Binary erasure channel (BEC).

## The performance of polar codes in distributed source coding

- **Status**: ❌
- **Reason**: polar 코드 기반 분산 소스코딩(Slepian-Wolf); 비-LDPC 부호 + 소스 코딩이라 원칙 제외, 떼어낼 바이너리 LDPC BP 기법 없음
- **ID**: ieee:6315897
- **Type**: conference
- **Published**: 1-3 Aug. 2
- **Authors**: Vu Thi Thuy Trang, Jin Whan Kang, Min Jang +2
- **PDF**: https://ieeexplore.ieee.org/document/6315897
- **Abstract**: The application of polar coding to rate-adaptive asymmetric Slepian-Wolf coding is considered. The encoder transmits the syndrome set which includes high entropy bits to the decoder to achieve the optimal compression. It means that the encoder must know the correlation between two sources and the syndrome set varies according to this correlation. In this paper, we propose polar source coding scheme with the construction which is designed by density evolution for the target range of crossover probabilities from 0.01 to 0.25. This proposed scheme performs closely to the theoretical Slepian Wolf bound and can be comparable with Low Density Parity Check Accumulate (LDPCA) codes.
