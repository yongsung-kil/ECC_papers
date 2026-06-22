# IEEE Xplore — 2019-09


## An Improved Symbol-Flipping Algorithm for Nonbinary LDPC Codes and its Application to NAND Flash Memory

- **Status**: ❌
- **Reason**: NAND 직접 응용이나 nonbinary(GF q) LDPC symbol-flipping 디코더 — 비이진 LDPC는 명시적 제외 대상.
- **ID**: ieee:8741212
- **Type**: journal
- **Published**: Sept. 2019
- **Authors**: Jieun Oh, Seokju Han, Jeongseok Ha
- **PDF**: https://ieeexplore.ieee.org/document/8741212
- **Abstract**: This paper proposes a novel symbol-flipping decoding (SFD) algorithm called decision-symbol reliability-based SFD (DRB-SFD) algorithm for nonbinary low-density parity-check (LDPC) codes aiming to improve the error-rate performances of data storage devices with hard-decision channel outputs, e.g., data storage using NAND flash memory. The proposed algorithm generates the reliability information of decision symbols based on a metric for symbol flipping during iterations instead of soft-decision channel outputs. In addition, it quantizes the reliability information into reliability messages that are exchanged between variable and check nodes. The number of quantization levels is carefully chosen to be the same as the field size of coded symbols, which allows the message exchanges to be performed without the additional signal paths. It is also extensively discussed how to decide parameters in the proposed algorithm in an analytic way. We demonstrate that the proposed algorithm featured with the exchanges of reliability messages provides significant performance improvements over existing SFD algorithms on channels with hard-decision outputs.

## Variable-Length Coding With Shared Incremental Redundancy: Design Methods and Examples

- **Status**: ❌
- **Reason**: 피드백 없는 가변길이 코딩(VL) — degree distribution 설계는 inter-frame/peeling 디코더 중심, 무선 응용 특이적, NB-LDPC 예시 위주. NAND BP 이식 기법 없음.
- **ID**: ieee:8736397
- **Type**: journal
- **Published**: Sept. 2019
- **Authors**: Haobo Wang, Sudarsan V. S. Ranganathan, Richard D. Wesel
- **PDF**: https://ieeexplore.ieee.org/document/8736397
- **Abstract**: Variable-length (VL) coding with feedback is a commonly used technique that can approach point-to-point Shannon channel capacity with a significantly shorter average codeword length than fixed-length coding without feedback. This paper uses the inter-frame coding of Zeineddine and Mansour, originally introduced to address varying channel-state conditions in broadcast wireless communication, to approach capacity on point-to-point channels using VL codes without feedback. The per-symbol complexity is comparable to decoding the VL code with feedback (plus the additional complexity of a small peeling decoder amortized over many VL codes) and presents the opportunity for encoders and decoders that utilize massive parallel processing, where each VL decoder can process simultaneously. This paper provides an analytical framework and a design process for the degree distribution of the inter-frame code that allows the feedback-free system to achieve 96% or more of the throughput of the original VL code with feedback. As examples of VL codes, we consider non-binary (NB) low-density parity-check (LDPC), binary LDPC, and convolutional VL codes. The NB-LDPC VL code with an 8-bit CRC and an average codeword length of 336 bits achieves 85% of capacity with four rounds of ACK/NACK feedback. The proposed scheme using shared incremental redundancy without feedback achieves 97% of that performance or 83% of the channel capacity.

## Comparison of Low-Density Parity-Check Codes in ATSC 3.0 and 5G Standards

- **Status**: ❌
- **Reason**: ATSC 3.0/5G 표준 LDPC 구조 비교 — 표준 QC/multi-edge LDPC 단순 비교, 신규 구성·디코더 기여 없음
- **ID**: ieee:8509633
- **Type**: journal
- **Published**: Sept. 2019
- **Authors**: Seok-Ki Ahn, Kyung-Joong Kim, Seho Myung +2
- **PDF**: https://ieeexplore.ieee.org/document/8509633
- **Abstract**: Recently, low-density parity-check (LDPC) codes have been adopted in Advanced Television Systems Committee 3.0 and 3rd Generation Partnership Project 5G standards. In this paper, we present their structures in detail. They are delicately designed, based on the structures of quasi-cyclic LDPC codes and multi-edge type LDPC codes. The differences in their base matrices and parity-check matrices used in both standards are highlighted from the viewpoint of the distinction between broadcasting and cellular communication systems. Numerical results show that they are very competitive in their respective areas.

## Root-Protograph-Based BICM-ID: A Reliable and Efficient Transmission Solution for Block-Fading Channels

- **Status**: ❌
- **Reason**: Root-protograph LDPC + BICM-ID, block-fading 무선 채널 다이버시티/변조 결합 설계. 무선 응용 특이적, 떼어낼 NAND ECC 기법 없음.
- **ID**: ieee:8740906
- **Type**: journal
- **Published**: Sept. 2019
- **Authors**: Yi Fang, Guohua Zhang, Guofa Cai +3
- **PDF**: https://ieeexplore.ieee.org/document/8740906
- **Abstract**: As a bandwidth-efficient technique, bit-interleaved coded modulation with iterative demapping and decoding (BICM-ID) has attracted much research attention in the field of wireless communication. In this paper, we put forth a joint design of root-protograph (RP) low-density parity-check (LDPC) codes and BICM-ID, referred to as RP-based BICM-ID (RP-BICM-ID), over block-fading (BF) channels so as to boost the throughput under limited bandwidth. To preserve the full-diversity property of RP codes, we propose an efficient modulation strategy for the RP-BICM-ID system by taking the fading-block length into consideration. We also analyze the outage-probability limit of the RP-BICM-ID systems to establish the fundamental lower-limit on their word-error-rate (WER) performance. Moreover, we conceive a multi-level protograph extrinsic information transfer (ML-PEXIT) algorithm to derive the asymptotic WER and bit error rate (BER) of the RP-BICM-ID systems over BF channels. As a further insight, we develop a novel unequal-error-protection (UEP) bit-to-symbol (B2S) mapping scheme for the RP-BICM-ID systems, which gives rise to an additional performance improvement. Analyses and simulations show that the proposed RP-BICM-ID systems can not only realize desirable spectral efficiency, but also obtain near-outage-limit performance over BF channels. Therefore, the proposed RP-BICM-ID systems are very promising in achieving high-reliability and high-rate transmissions under slow-fading wireless-communication environments.

## Universal Sparse Superposition Codes With Spatial Coupling and GAMP Decoding

- **Status**: ❌
- **Reason**: Sparse superposition codes + GAMP 디코딩, AWGN/메모리리스 채널 capacity 이론. LDPC가 아닌 SPARC, 떼어낼 바이너리 LDPC BP 기법 없음.
- **ID**: ieee:8723607
- **Type**: journal
- **Published**: Sept. 2019
- **Authors**: Jean Barbier, Mohamad Dia, Nicolas Macris
- **PDF**: https://ieeexplore.ieee.org/document/8723607
- **Abstract**: Sparse superposition codes, or sparse regression codes, constitute a new class of codes, which was first introduced for communication over the additive white Gaussian noise (AWGN) channel. It has been shown that such codes are capacity-achieving over the AWGN channel under optimal maximum-likelihood decoding as well as under various efficient iterative decoding schemes equipped with power allocation or spatially coupled constructions. Here, we generalize the analysis of these codes to a much broader setting that includes all memoryless channels. We show, for a large class of memoryless channels, that spatial coupling allows an efficient decoder, based on the generalized approximate message-passing (GAMP) algorithm, to reach the potential (or Bayes optimal) threshold of the underlying (or uncoupled) code ensemble. Moreover, we argue that spatially coupled sparse superposition codes universally achieve capacity under GAMP decoding by showing, through analytical computations, that the error floor vanishes and the potential threshold tends to capacity, as one of the code parameters goes to infinity. Furthermore, we provide a closed-form formula for the algorithmic threshold of the underlying code ensemble in terms of Fisher information. Relating an algorithmic threshold to a Fisher information has theoretical as well as practical importance. Our proof relies on the state evolution analysis and uses the potential method developed in the theory of low-density parity-check (LDPC) codes and compressed sensing.

## Deep Joint Source-Channel Coding for Wireless Image Transmission

- **Status**: ❌
- **Reason**: 딥 JSCC(이미지 무선전송) — LDPC 부호조차 안 쓰는 신경망 autoencoder, 떼어낼 ECC 기법 없음.
- **ID**: ieee:8723589
- **Type**: journal
- **Published**: Sept. 2019
- **Authors**: Eirina Bourtsoulatze, David Burth Kurka, Deniz Gündüz
- **PDF**: https://ieeexplore.ieee.org/document/8723589
- **Abstract**: We propose a joint source and channel coding (JSCC) technique for wireless image transmission that does not rely on explicit codes for either compression or error correction; instead, it directly maps the image pixel values to the complex-valued channel input symbols. We parameterize the encoder and decoder functions by two convolutional neural networks (CNNs), which are trained jointly, and can be considered as an autoencoder with a non-trainable layer in the middle that represents the noisy communication channel. Our results show that the proposed deep JSCC scheme outperforms digital transmission concatenating JPEG or JPEG2000 compression with a capacity achieving channel code at low signal-to-noise ratio (SNR) and channel bandwidth values in the presence of additive white Gaussian noise (AWGN). More strikingly, deep JSCC does not suffer from the “cliff effect,” and it provides a graceful performance degradation as the channel SNR varies with respect to the SNR value assumed during training. In the case of a slow Rayleigh fading channel, deep JSCC learns noise resilient coded representations and significantly outperforms separation-based digital communication at all SNR and channel bandwidth values.

## Physical Layer Performance Evaluation of LTE-Advanced Pro Broadcast and ATSC 3.0 Systems

- **Status**: ❌
- **Reason**: LTE/ATSC 3.0 물리계층 성능평가 — 무선 방송 응용, 떼어낼 LDPC ECC 기법 없음
- **ID**: ieee:8454855
- **Type**: journal
- **Published**: Sept. 2019
- **Authors**: Manuel Fuentes, De Mi, Hongzhi Chen +5
- **PDF**: https://ieeexplore.ieee.org/document/8454855
- **Abstract**: This paper provides a detailed performance analysis of the physical layer of two state-of-the-art point-to-multipoint (PTM) technologies: evolved Multimedia Broadcast Multicast Service (eMBMS) and Advanced Television Systems Committee - Third Generation (ATSC 3.0). The performance of these technologies is evaluated and compared using link-level simulations, considering relevant identified scenarios. A selection of Key Performance Indicators for the International Mobile Telecommunications 2020 (IMT-2020) evaluation process has been considered. Representative use cases are also aligned to the test environments as defined in the IMT-2020 evaluation guidelines. It is observed that ATSC 3.0 outperforms both eMBMS solutions, i.e., MBMS over Single Frequency Networks (MBSFN) and Single-Cell PTM (SC-PTM) in terms of spectral efficiency, peak data rate and mobility, among others. This performance evaluation serves as a benchmark for comparison with a potential 5G PTM solution.

## Irregular Repetition Slotted ALOHA With Energy Harvesting Nodes

- **Status**: ❌
- **Reason**: IRSA 랜덤액세스 + 에너지 하베스팅 — MAC 프로토콜 처리량 최적화, 채널 ECC 디코더 기법 아님
- **ID**: ieee:8758880
- **Type**: journal
- **Published**: Sept. 2019
- **Authors**: Umut Demirhan, Tolga M. Duman
- **PDF**: https://ieeexplore.ieee.org/document/8758880
- **Abstract**: We propose an irregular repetition slotted ALOHA (IRSA) based uncoordinated random access scheme for energy harvesting (EH) nodes. Specifically, we consider the case in which each user has a battery that is recharged with harvested energy from the environment in a probabilistic manner. We analyze this scheme starting with a unit-sized battery at the nodes and extend the analysis to the case of a finite-sized battery. For both scenarios, we derive the asymptotic throughput expressions and obtain the optimized probability distributions for the number of packet replicas of the users. We demonstrate that for the case of IRSA with EH nodes, these optimized distributions perform considerably better than the alternatives, including slotted ALOHA (SA), contention resolution diversity slotted ALOHA (CRDSA), and IRSA, which do not take into account the EH process for both asymptotic and finite frame length scenarios.

## Reliable State Estimation of an Unmanned Aerial Vehicle Over a Distributed Wireless IoT Network

- **Status**: ❌
- **Reason**: UAV 상태추정 + BCH 코딩 — 비-LDPC(BCH), 떼어낼 LDPC 기법 없음
- **ID**: ieee:8637032
- **Type**: journal
- **Published**: Sept. 2019
- **Authors**: Md. Noor-A-Rahim, M. O. Khyam, G. G. Md. Nawaz Ali +3
- **PDF**: https://ieeexplore.ieee.org/document/8637032
- **Abstract**: Unmanned aerial vehicles (UAVs) have attracted a lot of attention due to their enormous potentiality in civil and military applications over the past years. In order to allow accurate control action of UAV, a robust and real-time state estimation technique is required. In this paper, we propose a Kalman filter based UAV state estimation technique when the communication takes place over wireless links in an Internet of Things (IoT) network. We consider that a set of sensors observes the state of the UAV and transmits the observation to a control center (central server) over a distributed wireless IoT network. To deal with the communication impairments due to wireless communication links between the UAV's sensors and the IoT system components, e.g., IoT gateways, a Bose-Chaudhuri-Hocquenghem coded communication system is presented. Based on the received signals at the IoT gateways, a global state estimation technique is proposed. Performance of the proposed communication and estimation scheme is demonstrated through numerical results for different conditions. From the comparison with a conventional estimation scheme, it is observed that the proposed scheme significantly outperforms the conventional scheme in terms of state estimation and error performance.

## Radio-Frequency Impairments Compensation in Ultra High-Throughput Satellite Systems

- **Status**: ❌
- **Reason**: 위성 RF 손상(DC offset/IQ imbalance) 보상 알고리즘 — ECC/LDPC 무관, 떼어낼 디코더·HW 기법 없음
- **ID**: ieee:8752011
- **Type**: journal
- **Published**: Sept. 2019
- **Authors**: Bassel F. Beidas
- **PDF**: https://ieeexplore.ieee.org/document/8752011
- **Abstract**: The quest for massive satellite throughput is relentless, motivating the transmission of broadband signals at multiple Giga-Baud rates. Building low-cost, low-complexity user terminals is essential. These competing drivers conspire to cause analog radio-frequency (RF) components to exceed their tolerance limits. Specifically, analog mixers, anti-aliasing filters and amplification in quadrature frequency-conversion architectures create direct-current (DC) offset and in-phase/quadrature (I/Q) imbalance that is strong and frequency-selective. This paper provides two characterization models of analog RF impairments when the frequency offset is present. Novel digital compensation algorithms with immunity to frequency offset are presented, categorized into equalization with image-rejection capability and image cancellation. Adaptive techniques are utilized that operate without a priori knowledge of RF impairments. Two optimization methods are proposed for the multicarrier scenarios that are useful when using known data samples for factory calibration or in decision-directed mode during field re-calibration. Special consideration is given to estimating the frequency offset during initial factory calibration. Extensive computer simulations reveal that the proposed compensators are robust to frequency offset, provide lossless attenuation of imbalance-induced image and remove DC offset, under numerous scenarios. Cases include when the desired carrier is plagued by image interference from more than one source and on-board high-power amplifier is operated near saturation.

## Upper and Lower Bounds on the Computational Complexity of Polar Encoding and Decoding

- **Status**: ❌
- **Reason**: Polar 부호 인코딩/디코딩의 회로 복잡도 이론적 bound. 비-LDPC 부호이고 떼어낼 BP 이식 기법 없는 순수 이론.
- **ID**: ieee:8719012
- **Type**: journal
- **Published**: Sept. 2019
- **Authors**: Christopher G. Blake, Frank R. Kschischang
- **PDF**: https://ieeexplore.ieee.org/document/8719012
- **Abstract**: It is shown that all polar encoding schemes using a standard encoding matrix with rate R>1/2 and block length N have energy within the Thompson circuit model that scales at least as E ≥ Ω (N3/2). This lower bound is achievable up to polylogarithmic factors using a mesh network topology defined by Thompson and the encoding algorithm defined by Arıkan. A general class of circuits that compute successive cancellation decoding adapted from Arıkan's butterfly network algorithm is defined. It is shown that such decoders implemented on a rectangle grid for codes of rate R > 2/3 must take energy E ≥ Ω (N3/2). The energy of a Mead memory architecture and a mesh network memory architecture are analyzed and it is shown that a processor architecture using these memory elements can reach the decoding energy lower bounds to within a polylogarithmic factor. Similar scaling rules are derived for polar list decoders and belief propagation decoders. Capacity approaching sequences of energy optimal polar encoders and decoders, as a function of reciprocal gap to capacity χ = (1- R/C)-1 (where R is rate C and is channel capacity), have energy that scales as Ω (χ5.3685) ≤ E ≤ O (χ7.071 log4 (χ)). Known results in constant depth circuit complexity theory imply that no polynomial size classical circuits can compute polar encoding, but this is possible in quantum circuits that include a constant depth quantum fan-out gate.

## Gaussian Mixture Message Passing for Blind Known Interference Cancellation

- **Status**: ❌
- **Reason**: Gaussian mixture message passing for blind interference cancellation; MP 기법이지만 연속 실수값 BKIC 신호모델 전용이라 바이너리 LDPC BP로 떼어낼 ECC 기법 없음
- **ID**: ieee:8745691
- **Type**: journal
- **Published**: Sept. 2019
- **Authors**: Taotao Wang, Long Shi, Shengli Zhang +1
- **PDF**: https://ieeexplore.ieee.org/document/8745691
- **Abstract**: This paper proposes a Gaussian mixture message passing (GMMP) scheme to implement the blind known-interference cancellation (BKIC). Being aware of interference data as a priori information, the BKIC aims at canceling the interference without estimating the interference channel. Since the target signals are represented by continuous real-valued variables, the previous BKIC scheme is constructed as a real-valued belief propagation (RBP) for implementing message passing on the factor graph that represents the corresponding signal model. To implement the RBP-BKIC, the real-valued variables are actually quantized into vectors of discrete values. As such, the quantized RBP-BKIC has some drawbacks: 1) its performance is determined by the quantization step size and 2) it can only be applied to real signaling with 1-D PAM modulations. To overcome these drawbacks, we propose a GMMP scheme for the BKIC. First, we reveal that all messages passing over the factor graph of BKIC systems can be exactly represented by the mixtures of weighted Gaussian probability density functions. Superior to the quantized RBP-BKIC, we further show that the proposed GMMP scheme is an exact and efficient solution to the BKIC. In particular, it can approach performances of point-to-point communication systems with complex QAM modulations at the cost of affordable computational complexities. Moreover, we put forth a message passing framework that combines the GMMP-BKIC and the channel decoding into an iterative message passing scheme.

## Expander Recovery Performance of Bipartite Graphs With Girth Greater Than 4

- **Status**: ❌
- **Reason**: Expander recovery/compressed sensing 희소신호 복원 — 채널 ECC 디코더 아닌 신호복원 알고리즘, 바이너리 LDPC BP 이식 불명
- **ID**: ieee:8584893
- **Type**: journal
- **Published**: Sept. 2019
- **Authors**: Weizhi Lu, Weiyu Li, Wei Zhang +1
- **PDF**: https://ieeexplore.ieee.org/document/8584893
- **Abstract**: Expander recovery is an iterative algorithm designed to recover sparse signals measured with binary matrices with linear complexity. In the paper, we study the expander recovery performance of the bipartite graph with girth greater than 4, which can be associated with a binary matrix with column correlations equal to either 0 or 1. For such a graph, expander recovery is proved to achieve the same performance as the traditional basis pursuit recovery, as the signal is dissociated. Compared to random graphs widely used for expander recovery, the graph we study tends to present better empirical performance. Furthermore, its special structure enables reducing the iteration number of expander recovery from O(n log k) times to exactly k times in serial recovery, and from O(log k) times to exactly one time in parallel recovery.

## A Study on Dual-Polarized MIMO-ICI Canceller With Complexity Reduction Under Mobile Reception of OFDM Signals

- **Status**: ❌
- **Reason**: MIMO-OFDM ICI 캔슬러 — LDPC 무관, 무선 수신 특이적
- **ID**: ieee:8563051
- **Type**: journal
- **Published**: Sept. 2019
- **Authors**: Akira Nakamura, Hiroaki Otsubo, Makoto Itami
- **PDF**: https://ieeexplore.ieee.org/document/8563051
- **Abstract**: In the next Japanese digital terrestrial television broadcasting systems, the scheme that combines orthogonal frequency division multiplexing (OFDM) and dual-polarized multi-input multi-output (MIMO) is proposed. One of the major problems to be considered is inter-carrier interference (ICI) that is generated by Doppler-spread under mobile reception of MIMO-OFDM systems. In this case, reception characteristics are deteriorated significantly. The ICI canceller for MIMO-OFDM can demodulate transmitted symbols. To realize the MIMO-ICI canceller based on zero-forcing (ZF), it is necessary to reduce the complex calculations such as matrix operations. Therefore, complexity reduction of the MIMO-ICI canceller is proposed. The proposed MIMO-ICI canceller with complexity reduction based on ZF can improve the influence of ICI with low complexity. However, reception characteristics are deteriorated as compared to the MIMO-ICI canceller based on ZF. Thus, improving scheme of MIMO-ICI canceller with complexity reduction based on ZF is proposed. In the proposed scheme, the iterative detection is adopted. In addition, MIMO-ICI cancellers based on minimum mean square error (MMSE) are proposed. As the results of computer simulations, the MIMO-ICI cancellers using iterative detection based on ZF and MMSE can improve the reception characteristics with low complexity.

## Improved Extended Min-Sum Algorithm for Non-Binary LDPC Codes Based on Node Reliability

- **Status**: ❌
- **Reason**: Non-Binary(GF(q)) LDPC EMS 디코더 개선 — 비이진 LDPC는 제외 대상
- **ID**: ieee:8870565
- **Type**: conference
- **Published**: 9-13 Sept.
- **Authors**: Yibing Li, Sitong Zhang, Fang Ye +3
- **PDF**: https://ieeexplore.ieee.org/document/8870565
- **Abstract**: Low Density Parity Check (LDPC) codes have been widely applied in recent years, and Extended Min-Sum (EMS) decoding algorithm is the most practical algorithm, which has a fairly low computational cost. Due to the great loss in error correction performance of EMS algorithm, in this paper, we establish constraints to obtain reliable nodes while decoding and evaluate the reliability of the nodes. The nodes and information transferred between nodes are processed and optimized according to the reliability of the nodes. High reliability nodes will not be updated in the decoding process while the information of the sub-reliability nodes will be optimized in different situations, thereby improving the decoding accuracy. This algorithm can accelerate the convergence of the algorithm, while the reduced number of update nodes can control the increase of the computation to a certain extent, and maintain the advantage of the low computation quantity of EMS algorithm. Through simulation results and computational analysis, we prove that the improved algorithm has significantly improved error correction performance compared with the traditional EMS algorithm. Under the same conditions, it has completely entered the waterfall area at 3.6dB, and the EMS algorithm has not entered the waterfall area. By comparing the average iteration times of decoding of the two algorithms, the convergence speed of the algorithm can be reflected. Compared with EMS algorithm, the improved algorithm has significantly improved the convergence speed in most areas, which indicates that the processing of sub-reliable nodes accelerates the convergence of the algorithm. Finally, the average update times of the check nodes and variable nodes of the two algorithms are compared respectively. Although the improved algorithm introduces extra processing flow, it speeds up the convergence of the algorithm, and the computational cost of decoding is less expensive.

## Creation of communication system for unmanned aerial vehicles using SDR and SOC technologies

- **Status**: ❌
- **Reason**: UAV SDR/SoC 통신시스템 구축, LDPC/ECC 기법 없음
- **ID**: ieee:9165422
- **Type**: conference
- **Published**: 9-13 Sept.
- **Authors**: Mykola Kaidenko, Serhii Kravchuk
- **PDF**: https://ieeexplore.ieee.org/document/9165422
- **Abstract**: The principles of the functional and structural construction of a communication part of the UAV system based on SDR and SoC technologies while ensuring the survivability of the formed radio channels are presented. The main increase in survivability is achieved through the use of adaptation over the frequency range using an additional reception channel for continuous analysis of interference conditions, using two or more data transmission channels, complex algorithms for optimal selection of the operating range, transmission channel parameters and adaptive protocols for simultaneous data transmission over two or more channels.

## Dual Trellis Construction for High-Rate Punctured Convolutional Codes

- **Status**: ❌
- **Reason**: punctured convolutional/turbo code dual trellis MAP 디코딩, 비-LDPC이고 BP 이식 불가
- **ID**: ieee:8880816
- **Type**: conference
- **Published**: 8-8 Sept. 
- **Authors**: Vinh Hoang Son Le, Charbel Abdel Nour, Emmanuel Boutillon +1
- **PDF**: https://ieeexplore.ieee.org/document/8880816
- **Abstract**: Puncturing a low-rate convolutional code to generate a high-rate code has some drawback in terms of hardware implementation. In fact, a Maximum A-Posteriori (MAP) decoder based on the original trellis will then have a decoding throughput close to the decoding throughput of the mother non-punctured code. A solution to overcome this limitation is to perform MAP decoding on the dual trellis of a high-rate equivalent convolutional code. In the literature, dual trellis construction is only reported for specific punctured codes with rate k/(k+1). In this paper, we propose a multi-step method to construct the equivalent dual code defined by the corresponding dual trellis for any punctured code. First, the equivalent nonsystematic generator matrix of the high-rate punctured code is derived. Then, the reciprocal parity-check matrix for the construction of the dual trellis is deduced. As a result, we show that the dual-MAP algorithm applied on the newly constructed dual trellis yields the same performance as the original MAP algorithm while allowing the decoder to achieve a higher throughput. When applied to turbo codes, this method enables highly efficient implementations of high-throughput high-rate turbo decoders.

## Partial Access for LDPC-Coded-IDMA Systems

- **Status**: ❌
- **Reason**: LDPC-coded IDMA 다중접속 partial-access, 무선 응용 특이적이고 떼어낼 ECC 기법 없음
- **ID**: ieee:8904215
- **Type**: conference
- **Published**: 8-11 Sept.
- **Authors**: Akira Osamura, Guanghui Song, Tomotaka Kimura +1
- **PDF**: https://ieeexplore.ieee.org/document/8904215
- **Abstract**: A partial-access scheme is proposed for coded-IDMA (interleave-division multiple-access) systems. Similar to conventional IDMA systems, the transmitter of each user consists of a concatenation of channel encode, spreading, and user-specific interleaving. The only difference is that after spreading, some 0s are inserted into the chip sequence. Among the transmitted symbols of −1, 0, 1, symbol 0, however, implies a non-energy transmission or non-access to the channel. In the IDMA receiver, we use a customary joint iterative decoding based on a single factor graph. In our proposed IDMA systems, partial access not only greatly decreases the complexity of the joint decoding; it also decreases the number of short loops in the factor graph. Our extrinsic information transfer (EXIT) analysis and bit-error-rate (BER) simulations show that the proposed partial-access scheme outperforms conventional full-access-IDMA systems in a low SNR range.

## Error-correcting Performance Comparison for Polar Codes, LDPC Codes and Convolutional Codes in High-performance Wireless

- **Status**: ❌
- **Reason**: polar/LDPC/convolutional 성능 비교(서베이성), 신규 디코더/구성/HW 기여 없음
- **ID**: ieee:9115442
- **Type**: conference
- **Published**: 27-30 Sept
- **Authors**: Chao Yang, Ming Zhan, Yi Deng +3
- **PDF**: https://ieeexplore.ieee.org/document/9115442
- **Abstract**: In this paper, polar codes, low-density parity-check (LDPC) codes and convolutional codes in the status of high-performance wireless (WirelessHP) are discussed. Those classic code schemes are compared in terms of their encoding and decoding complexity and the error-correcting performance. Results show that, polar codes with successive cancellation list (SCL) decoding is superior to the LDPC codes and the convolutional codes in the condition of WirelessHP. The result has certain significance for the development of next generation communication technology.

## NEXTRACK - Next Generation ESTRACK Uplink Services

- **Status**: ❌
- **Reason**: 우주 ESTRACK 업링크 LDPC 인코더 HW(SRAA·Winograd) — 표준 CCSDS 단축 LDPC 인코딩 구현, NAND 디코더/구성 신규 기여 아님
- **ID**: ieee:8895312
- **Type**: conference
- **Published**: 24-27 Sept
- **Authors**: R. Abelló, M. Baldi, F. Chiaraluce +9
- **PDF**: https://ieeexplore.ieee.org/document/8895312
- **Abstract**: The Consultative Committee for Space Data Systems has recently updated its recommendation for uplink communication systems, to cope with new requirements for telecommand and modern profiles and applications. Two short Low-Density Parity-Check (LDPC) codes have been added to the Coding and Synchronization sublayer options, to improve the link performance. In this paper we focus on the real-time implementation of the transmitter for the Ground Station segment. We analyze the critical modules, in particular LDPC encoding, for which two efficient solutions based on a Shift Register Adder Accumulator and on Winograd convolution are considered. We then discuss the selection of a proper hardware or software platform, and we show that a Central Processing Unit-based solution is able to achieve the high data-rates required by the new uplink applications.

## Coding for optical communications — Can we approach the Shannon limit with low complexity?

- **Status**: ❌
- **Reason**: 광통신 저복잡도 코딩 서베이/비교 — 구체적 신규 LDPC 디코더/구성 없음
- **ID**: ieee:9125535
- **Type**: conference
- **Published**: 22-26 Sept
- **Authors**: Alexandre Graell i Amat, Gianluigi Liva, Fabian Steiner
- **PDF**: https://ieeexplore.ieee.org/document/9125535
- **Abstract**: Approaching capacity with low complexity is a very challenging task. In this paper, we review and compare three promising coding solutions to achieve that, which are suitable for future very high-throughput, low-complexity optical communications.

## Coded modulation using a 512-ary Hurwitz-integer constellation

- **Status**: ❌
- **Reason**: Hurwitz-integer 성좌 coded modulation — 변조 설계, LDPC 디코더/구성 기여 없음
- **ID**: ieee:9125653
- **Type**: conference
- **Published**: 22-26 Sept
- **Authors**: Felix Frey, Sebastian Stern, Robert Emmerich +3
- **PDF**: https://ieeexplore.ieee.org/document/9125653
- **Abstract**: A signaling scheme is presented which effectively combines a class of power-efficient four-dimensional modulation formats with forward error correction using a tailored two-stage coded modulation scheme. In a 400ZR system experiment, a 0.8-dB gain in required OSNR over DP 16-QAM at 60 GBd is demonstrated.

## Delivery of 1.196-Tb/s signal over 800 M based on RF/FSO convergence

- **Status**: ❌
- **Reason**: RF/FSO 융합 전송 시스템 — ECC 무관, LDPC 기법 없음
- **ID**: ieee:9125769
- **Type**: conference
- **Published**: 22-26 Sept
- **Authors**: Kaihui Wang, Jianjun Yu, Yiran Wei +10
- **PDF**: https://ieeexplore.ieee.org/document/9125769
- **Abstract**: We demonstrate a hybrid RF/FSO converged system consisting of two FSO links and two RF links. 1.196-Tb/s wireless signals are delivered over 800-m converged RF/FSO links. Kramers-Kronig scheme, probabilistic-shaping algorithm, and simplified wireless architecture at W-band are introduced in the system for the first time.

## Long-haul mode multiplexing transmission enhanced by interference cancellation technique

- **Status**: ❌
- **Reason**: 모드분할 다중화 전송·간섭제거(affine projection) — ECC 무관, LDPC 기법 없음
- **ID**: ieee:9125636
- **Type**: conference
- **Published**: 22-26 Sept
- **Authors**: Kohki Shibahara, Takayuki Mizuno, Yutaka Miyamoto
- **PDF**: https://ieeexplore.ieee.org/document/9125636
- **Abstract**: We discuss transmission issues in achieving long-haul SDM transmission using mode division multiplexing (MDM). Key MDM transmission techniques that we have recently developed are also reviewed. Their applications for optical MDM transmission are experimentally investigated with linear filter adaptation techniques including the affine projection algorithm.

## 16384-QAM transmission at 10 GBd over 25-km SSMF using polarization-multiplexed probabilistic constellation shaping

- **Status**: ❌
- **Reason**: 16384-QAM 확률성좌성형 전송 실험 — 변조/성형, LDPC 기법 없음
- **ID**: ieee:9125758
- **Type**: conference
- **Published**: 22-26 Sept
- **Authors**: Xi Chen, Junho Cho, Andrew Adamiecki +1
- **PDF**: https://ieeexplore.ieee.org/document/9125758
- **Abstract**: We demonstrate the transmission of 10-GBd polarization-multiplexed probabilistically shaped 16384-ary quadrature amplitude modulation (16384-QAM) over 25.5-km standard single mode fiber (SSMF), with a net single-carrier bit rate of 223.8 Gb/s carrying 22.3 information bits/symbol/2-pol.

## Enumerative sphere shaping for rate adaptation and reach increase in WDM transmission systems

- **Status**: ❌
- **Reason**: enumerative sphere shaping(확률성형) WDM — 소스성형/분포매칭, 채널 LDPC ECC 기법 없음
- **ID**: ieee:9125723
- **Type**: conference
- **Published**: 22-26 Sept
- **Authors**: Abdelkerim Amari, Sebastiaan Goossens, Yunus Can Gültekin +6
- **PDF**: https://ieeexplore.ieee.org/document/9125723
- **Abstract**: The performance of enumerative sphere shaping (ESS), constant composition distribution matching (CCDM), and uniform signalling are compared at the same forward error correction rate. ESS is shown to offer a reach increase of approximately 10% and 22% compared to CCDM and uniform signalling, respectively.

## Performance-complexity tradeoffs of concatenated FEC for 64-QAM MLC and BICM

- **Status**: ❌
- **Reason**: MLC vs BICM 성능-복잡도 tradeoff, staircase 외부부호 연접 — LDPC 디코더/구성 기여 없음, 떼어낼 ECC 기법 없음
- **ID**: ieee:9125534
- **Type**: conference
- **Published**: 22-26 Sept
- **Authors**: Masoud Barakatain, Diego Lentner, Georg Böcherer +1
- **PDF**: https://ieeexplore.ieee.org/document/9125534
- **Abstract**: Multilevel coding (MLC) is compared with bit-interleaved coded modulation (BICM) from a performance-versus-complexity standpoint. In both approaches, complexity-optimized error-reducing inner codes are designed for concatenation with an outer staircase code, assuming signaling with 64-point quadrature amplitude modulation. The codes are designed to achieve various points on the Pareto frontier characterizing the performance-complexity tradeoff. Computer simulations of the resulting codes reveal that the MLC approach (a) provides significant advantages compared to BICM and (b) has a clear edge over an existing MLC proposal, providing a net coding gain of up to 13.6 dB at 28% overall overhead, yet with reasonable decoding complexity.

## Experimental validation of clipping combined with digital resolution enhancer for high speed optical transmission

- **Status**: ❌
- **Reason**: 클리핑+디지털 해상도 향상 DAC 송신기 — ECC 무관
- **ID**: ieee:9125700
- **Type**: conference
- **Published**: 22-26 Sept
- **Authors**: Menno van den Hout, Sjoerd van der Heide, Chigo Okonkwo
- **PDF**: https://ieeexplore.ieee.org/document/9125700
- **Abstract**: A digital resolution enhancer combined with clipping is experimentally validated by transmitting single channel 600 Gb/s 64-QAM and WDM 460 Gb/s 128-QAM over 75 km, allowing to reduce the DAC's physical number of bits to 3. Low resolution DACs will play an important role in low-power transmitters.

## Highly spectral efficient transmission of 183 + 24.5 GBaud 256-QAM spatial super channels over 55 km three-mode fiber

- **Status**: ❌
- **Reason**: 256-QAM few-mode fiber 전송 실험 — 변조/전송, 떼어낼 LDPC 기법 없음
- **ID**: ieee:9125640
- **Type**: conference
- **Published**: 22-26 Sept
- **Authors**: Georg Rademacher, Kasper Ingerslev, Ruben S. Luís +7
- **PDF**: https://ieeexplore.ieee.org/document/9125640
- **Abstract**: We investigate the data-rate increase of 256-QAM over 64-QAM signals in few-mode fiber transmission. Simulations and experimental validation indicate an increased total data throughput by applying 256-QAM, achieving 146 Tbit/s total data-rate at an average spectral efficiency of 10.67 bit/s/Hz/mode over the entire C-band.

## Outer Code-Based HARQ Retransmission for Multicast/Broadcast Services in 5G

- **Status**: ❌
- **Reason**: 외부 RS/Raptor + 내부 LDPC HARQ 멀티캐스트, LDPC는 베이스라인일 뿐 떼어낼 디코더/HW/코드설계 없음
- **ID**: ieee:8891304
- **Type**: conference
- **Published**: 22-25 Sept
- **Authors**: Jeongho Yeo, Jonghyun Bang, Hyoungju Ji +2
- **PDF**: https://ieeexplore.ieee.org/document/8891304
- **Abstract**: This paper studies a hybrid automatic repeat and request (HARQ) mechanism for multicast/broadcast services in 5G New Radio (NR) systems. HARQ is widely used in unicast transmission to improve reliability and resource efficiency under the fading channel. However, for multicast/broadcast, it is difficult to apply conventional HARQ technology because the probability of retransmission becomes high as the number of receiver increases. In this paper, we propose a novel and efficient retransmission scheme, called outer code- based HARQ. After the initial transmission of a given data packet for multicast/broadcast, each receiver sends feedback information on how many code blocks (CBs) are broken instead of which CBs are broken. Then, for retransmission of the data, the transmitter generates parity CBs by using outer code such as Reed- Solomon (RS) or Raptor code and transmits the parity CBs after applying inner code such as low density parity check (LDPC) code. Numerical results show that the proposed scheme outperforms the conventional HARQ schemes, reducing more than 50% of retransmissions.

## Efficient Concatenated Same Codebook Construction for the Random Access Gaussian MAC

- **Status**: ❌
- **Reason**: 외부 비이진 LDPC(QSPA) + 내부 바이너리 연접부호 — 비이진 LDPC q-ary SPA 제외
- **ID**: ieee:8891568
- **Type**: conference
- **Published**: 22-25 Sept
- **Authors**: Daria Ustinova, Anton Glebov, Pavel Rybin +1
- **PDF**: https://ieeexplore.ieee.org/document/8891568
- **Abstract**: In this paper, a low complexity scheme for unsourced random multiple access over the Gaussian channel is proposed. Following the literature by the word "unsourced" we mean the fact that the users use the same codebook codes. The proposed scheme is based on T-fold ALOHA with successive interference cancellation (SIC) procedure. In each slot, the same codebook concatenated code construction with outer non-binary (NB) low- density parity-check (LDPC) code and inner linear binary code is decoded with iterative joint decoding algorithm. Outer NB-LDPC code is decoded with low-complexity iterative q-ary sum-product algorithm (QSPA) and short inner binary code is decoded with maximum likelihood. Finally, the numerical results and comparison with theoretical bounds are represented.

## An Iterative Receiver for Polar-Coded Massive MU-MIMO Systems

- **Status**: ❌
- **Reason**: 폴라 부호 기반 MU-MIMO 반복 수신기 — 비-LDPC 무선 응용, 이식 가능 LDPC 기법 없음
- **ID**: ieee:8891345
- **Type**: conference
- **Published**: 22-25 Sept
- **Authors**: Yi Sun, Ming Jiang, Chunming Zhao +1
- **PDF**: https://ieeexplore.ieee.org/document/8891345
- **Abstract**: A novel iterative receiver for polar-coded massive multiuser multiple-input-multiple-output (MU-MIMO) systems is proposed. In the receiver, the feedbacks of the polar decoder, including the correctly decoded data and the soft outputs generated using Pyndiah's Chase algorithm, are available to the detector and the channel estimator, respectively. Moreover, interference cancellation (IC) schemes are employed to improve the overall performance and reduce the computation complexity. Simulation results show that the proposed receiver with polar codes can bring about considerable performance gains through iterations and can always outperform the one with LDPC codes.

## Performance Analysis of Finite Length Non-Binary Raptor Codes under Ordered Statistics Decoder

- **Status**: ❌
- **Reason**: 비이진(GF(q)) LDPC 프리코드 + LT Raptor 부호, OSD가 non-binary 구조에 종속 — 비이진 LDPC·비-LDPC 제외
- **ID**: ieee:8891217
- **Type**: conference
- **Published**: 22-25 Sept
- **Authors**: Lianqin Li, Ke Zhang, Jian Jiao +4
- **PDF**: https://ieeexplore.ieee.org/document/8891217
- **Abstract**: Raptor code is the current standard of 4G long term evolution (LTE) evolved multimedia broadcast and multi-cast services (eMBMS), which is viewed as a potential approach in the design of ultra-reliable low latency communications (uRLLC) for 5G. This paper analyzes the performance of finite length non-binary (over finite field of order q, GF(q)) Raptor codes under ordered statistics decoder (OSD) towards uRLLC, where the non-binary Raptor code ensembles by a non-binary low density parity-check (LDPC) code as pre-code and a non-binary inner Luby transform (LT) code. Moreover, by investigating the property of code structure and decoding algorithm, an upper bound of decoding failure probability (DFP) of finite length non-binary Raptor code under OSD is derived. Simulation results validate the accuracy of our derived upper bound, and demonstrate that our non-binary Raptor codes can achieve 10â'5 DFP with block length 128 bits at SNR 3.6 dB.

## Partial Enumerative Sphere Shaping

- **Status**: ❌
- **Reason**: partial enumerative sphere shaping(확률진폭성형) — 성형 기법, 채널 LDPC 디코더/구성 기여 없음
- **ID**: ieee:8891195
- **Type**: conference
- **Published**: 22-25 Sept
- **Authors**: Yunus Can Gultekin, W. J. van Houtum, Arie Koppelaar +1
- **PDF**: https://ieeexplore.ieee.org/document/8891195
- **Abstract**: The dependency between the Gaussianity of the input distribution for the additive white Gaussian noise (AWGN) channel and the gap-to-capacity is discussed. We show that a set of particular approximations to the Maxwell- Boltzmann (MB) distribution virtually closes most of the shaping gap. We relate these symbol-level distributions to bit-level distributions, and demonstrate that they correspond to keeping some of the amplitude bit-levels uniform and independent of the others. Then we propose partial enumerative sphere shaping (P-ESS) to realize such distributions in the probabilistic amplitude shaping (PAS) framework. Simulations over the AWGN channel exhibit that shaping 2 amplitude bits of 16-ASK have almost the same performance as shaping 3 bits, which is 1.3 dB more power- efficient than uniform signaling at a rate of 3 bit/symbol. In this way, required storage and computational complexity of shaping are reduced by factors of 6 and 3, respectively.

## Weight-Adaptive Analog Fountain Codes toward Massive Machine Type Communications

- **Status**: ❌
- **Reason**: 아날로그 fountain 부호 mMTC 이론 프레임워크 — fountain/용량분석, 떼어낼 LDPC ECC 기법 없음
- **ID**: ieee:8891449
- **Type**: conference
- **Published**: 22-25 Sept
- **Authors**: Ke Zhang, Jian Jiao, Lianqin Li +3
- **PDF**: https://ieeexplore.ieee.org/document/8891449
- **Abstract**: In this paper, towards the fifth generation (5G) massive machine type communications (mMTC), a theoretical framework of the design and evaluation model for analog fountain codes (AFC) is proposed. Motivated by the capacity analysis of AFC, we propose a weight adaptive (WA) AFC transmission scheme by introducing a limit feedback link, which can realize the optimal AFC in theoretical. Simulation results reveal that our WA-AFC coding scheme can approach the Shannon capacity in a wide range of SNRs over AWGN channel.

## Design on Polarization Weight-Based Polar Coded SCMA System over Fading Channels

- **Status**: ❌
- **Reason**: 폴라 부호 SCMA(PW/BRS/CRC) — 비-LDPC 무선 응용, 이식 가능 기법 없음
- **ID**: ieee:8891433
- **Type**: conference
- **Published**: 22-25 Sept
- **Authors**: Kexin Liang, Bowen Feng, Jian Jiao +4
- **PDF**: https://ieeexplore.ieee.org/document/8891433
- **Abstract**: Sparse code multiple access (SCMA) is one of the key techniques to address the high spectral efficiency and massive connectivity requirements for the fifth generation (5G) wireless systems. Moreover, polar codes are selected as the candidate scheme of control codes in enhanced mobile broadband (eMBB). Note that the joint design of channel coding and SCMA scheme can significantly improve the system overall performances, which essentially shows the potential for 5G massive machine type communications (mMTC). Thus, in this paper, we proposed a polarization weight (PW)-based polar coded SCMA (PC SCMA) system to satisfy the requirements of low complexity implementation and high reliability under a wide range of code length and rate. Our design of PW-based PC SCMA system is mainly including the following three aspects: 1) deploy the polarization weight (PW) algorithm to construct polar code with lower complexity; 2) employ the bit-reverse shortening (BRS) algorithm to achieve rate matching in the encoding part; 3) adopt the cyclic redundancy check (CRC) to set up an early stopping criterion in the decoding part. Simulation results show that the proposed PW-based PC SCMA system can outperform the existing PC SCMA system over AWGN and fading channels.

## A Curve Fitting Method to Construct Polar Coded OFDM Systems with Channel Side Information for the Transmitter

- **Status**: ❌
- **Reason**: 폴라 부호 OFDM 곡선맞춤 구성 — 비-LDPC, 이식 가능 LDPC 기법 없음
- **ID**: ieee:8891458
- **Type**: conference
- **Published**: 22-25 Sept
- **Authors**: Shih-Kai Lee, Yung-Tsao Hsu, Bei-Hao Chang +2
- **PDF**: https://ieeexplore.ieee.org/document/8891458
- **Abstract**: We construct polar codes for OFDM systems over the frequency selective channel. The channel coefficients are assumed to be available to the transmitter such that the encoder of polar codes can correctly distinguish the input reliabilities and make proper arrangement of frozen bits and message bits. Instead of using the well-known Gaussian approximation method to construct polar codes, we propose a curve fitting method which not only closely approximate the corresponding channel capacity function but also significantly reduce the computational complexity. With the proposed method, the polar coded OFDM systems can achieve good error performances for systems using high- rate polar codes.

## A Polar Code Based Unsourced Random Access for the Gaussian MAC

- **Status**: ❌
- **Reason**: 폴라 부호 기반 unsourced random access(IRSA) — 비-LDPC, LDPC를 폴라로 대체하는 연구
- **ID**: ieee:8891583
- **Type**: conference
- **Published**: 22-25 Sept
- **Authors**: Evgeny Marshakov, Gleb Balitskiy, Kirill Andreev +1
- **PDF**: https://ieeexplore.ieee.org/document/8891583
- **Abstract**: Massive machine-type communications (mMTC) is one of the key application scenarios for future 5G networks. In the literature, this problem is known as unsourced random access. We propose a polar code based scheme for the unsourced random access Gaussian channel. This scheme is based on T-fold irregular repetition slotted ALOHA (IRSA). We use polar codes as slot codes and investigate their practical performance in T-user MAC. We compare two possible decoding techniques: joint successive cancellation algorithm and joint iterative algorithm. In order to optimize the codes (choose frozen bits), we propose a specialized and efficient design algorithm. Finally, we investigate the performance of the resulting scheme by means of simulations and conclude that replacing of LDPC codes with polar codes in IRSA scheme leads to a significant performance gain.

## On the Impact of CW interference on 5G NR

- **Status**: ❌
- **Reason**: 5G NR의 CW 간섭 취약성·리미터 분석, LDPC는 베이스라인 ECC로 언급뿐 — 떼어낼 디코더 기법 없음
- **ID**: ieee:8871665
- **Type**: conference
- **Published**: 2-6 Sept. 
- **Authors**: Karina Fors, Erik Axell, Sara Linder +1
- **PDF**: https://ieeexplore.ieee.org/document/8871665
- **Abstract**: Orthogonal frequency division multiplex (OFDM) is used in several modern wireless systems, for example in the fourth generation mobile system LTE (long term evolution), the wireless local area network (WLAN) standard IEEE 802.11, digital audio broadcasting (DAB) and digital video broadcasting (DVB). OFDM has also recently been included in the standard for the fifth generation mobile system, 5G.In this work, we analyze the vulnerability of 5G NR to different types of continuous wave (CW) interference, both a single CW signal or several synchronized CW signals. The analysed system includes OFDM and error correction by LDPC codes, with parameters chosen to resemble those of the 5G NR release 15 standard. An important conclusion of this work is that the 5G NR system is significantly more sensitive to CW interference than to white Gaussian noise. To improve the robustness against CW interference, different types of limiters on the received signal are also evaluated. Limiters in the frequency domain are shown to mitigate the impact from a single CW signal significantly. For an interfering signal consisting of several CW signals, a limiter in the time domain can reduce the impact of the interference signal so that its impact is below that of Gaussian noise with the same power.

## Performance Study of a Class of Irregular LDPC Codes through Low Complexity Bounds on Their Belief-Propagation Decoding Thresholds

- **Status**: ❌
- **Reason**: 순수 이론 bound — density evolution BP 임계값 상한 분석만, 떼어낼 디코더/HW/구성 기여 없음
- **ID**: ieee:8893306
- **Type**: conference
- **Published**: 18-20 Sept
- **Authors**: F. Vatta, A. Soranzo, M. Comisso +2
- **PDF**: https://ieeexplore.ieee.org/document/8893306
- **Abstract**: This paper investigates about the usefulness of some recently published low complexity upper bounds on belief-propagation decoding thresholds for irregular low-density parity-check (LDPC) codes to analyze their performance on memoryless binary input - additive white Gaussian noise (BI-AWGN) channels, with sum-product decoding. Irregular LDPC codes are known to perform better than regular ones, and to exhibit, like them, the so called “threshold phenomenon”, being the threshold defined as the maximum noise level such that an arbitrarily small bit-error probability can be achieved as the block length tends to infinity. We use a simplified analysis of the belief-propagation decoding algorithm, i.e., consider a Gaussian approximation for message densities under density evolution, and a simple algorithmic method, defined recently, to estimate the decoding thresholds for regular and irregular LDPC codes on BI-AWGN channels.

## Symbol Message Passing Decoding of Nonbinary Spatially-Coupled Low-Density Parity-Check Codes

- **Status**: ❌
- **Reason**: 비이진 SC-LDPC 대상 SMP 디코더 — non-binary q-ary 전용, 바이너리 한정 위배
- **ID**: ieee:8893373
- **Type**: conference
- **Published**: 18-20 Sept
- **Authors**: Emna Ben Yacoub, Francisco Lázaro, Alexandre Graell i Amat +1
- **PDF**: https://ieeexplore.ieee.org/document/8893373
- **Abstract**: The performance of a decoding algorithm, called symbol message passing (SMP), is analyzed for nonbinary spatially coupled low-density parity-check (LDPC) codes. The SMP algorithm can be seen as a generalization of Gallager B and the binary message passing algorithm by Lechner et al. to q-ary LDPC codes. The analysis is performed via density evolution over the q-ary symmetric channel, with q being the field order used for the code construction.

## Using Non-Binary LDPC and MDPC Codes in the McEliece Cryptosystem

- **Status**: ❌
- **Reason**: 비이진 LDPC/MDPC + McEliece 암호 — non-binary 및 보안, 바이너리 NAND ECC 대상 아님
- **ID**: ieee:8893339
- **Type**: conference
- **Published**: 18-20 Sept
- **Authors**: Marco Baldi, Giovanni Cancellieri, Franco Chiaraluce +2
- **PDF**: https://ieeexplore.ieee.org/document/8893339
- **Abstract**: In this paper we study the use of non-binary Low-Density Parity-Check and Moderate-Density Parity-Check codes for the McEliece cryptosystem. We generalize existing constructions by using codes and errors that are both nonbinary. We devise a decoding technique which is inspired by the binary Bit Flipping decoder and whose complexity grows linearly with the code length. We show that the non-binary schemes are potentially able to reach the same security levels of the binary ones, for equal or smaller key sizes, but with reduced decryption failure rate, the latter being a relevant parameter in view of countering statistical attacks.

## Optimization Info Rate Using APSK Modulation Scheme for Delivery GSM ABIS over Satellite Communications

- **Status**: ❌
- **Reason**: 위성/GSM 통신 응용 특이적 — 표준 16APSK LDPC 5/6 단순 사용, 떼어낼 ECC 기법 없음
- **ID**: ieee:8977020
- **Type**: conference
- **Published**: 18-20 Sept
- **Authors**: Hillman Akhyar Damanik, Merry Anggraeni
- **PDF**: https://ieeexplore.ieee.org/document/8977020
- **Abstract**: Mobile operators move quickly from 2G GSM networks in urban areas to remote rural areas, which are 2G networks by offering voice connectivity. As a result, more and more technology is optimizing cellular operators that reduce and perform bandwidth efficiency that will be implemented. The optimization solution for this cellular operator produces voice communication on GSM, in a cost-effective application for satellites. This paper discusses and applies to creating GSM links via satellite communication. The ABIS interface on GSM, which is defined between the Base Transceiver Station (BTS) of GSM remote cells and the Base Station Controller (BSC), is considered here to be transferred via GSM communication with the Modulation and Coding scheme 16 APSK 5/6. The MODCOD scheme determines the efficiency of what MHz is needed to send one Mbps. The efficiency value achieved by allocating, bandwidth (MHz) generated by 1.0 Mhz is an efficiency of 3.222 [bit / baud]. And Info Data Rate is generated from the value (Mbps) of 3,175. The highest traffic intensity with the value of Traffic Volume (Hours) = 3.5, Traffic Intensity (Erlang) 0.145833333. While the lowest traffic intensity with the value of Traffic Volume (Hour) = 2.6, traffic intensity = 0.108333333 (Erlang). The value obtained on Traffic Volume and Traffic Intensity is 0.1%. Service levels are very good at grade of service, because of the small possibility of access fail. Calculation of the availability of link network availability links, using ACM 16APSK LDPC 5/6 techniques that can increase up to 100%.

## Prototyping Software Transceiver for the 5G New Radio Physical Uplink Shared Channel

- **Status**: ❌
- **Reason**: 5G NR PUSCH 트랜시버 프로토타입, 표준 LDPC enc/dec를 부수 언급할 뿐 새 디코더·구성 기여 없음
- **ID**: ieee:8882079
- **Type**: conference
- **Published**: 17-19 Sept
- **Authors**: Grzegorz Cisek, Tomasz P. Zieliński
- **PDF**: https://ieeexplore.ieee.org/document/8882079
- **Abstract**: 5G New Radio (NR) is an emerging radio access technology, which is planned to succeed 4G Long Term Evolution (LTE) as global standard of cellular communications in the upcoming years. This paper considers a digital signal processing model and a software implementation of a complete transceiver chain of the Physical Uplink Shared Channel (PUSCH) defined by the version 15 of the 3GPP standard, consisting of both baseband transmitter and receiver chains on a physical layer level. The BLER performance of the prototype system implementation under AWGN and Rayleigh fading channel conditions is evaluated. Moreover, the source code of high-level numerical model was made available online on a public repository by the authors. In the paper's tutorial part, the aspects of the 5G NR standard are reviewed and their impact on different functional building blocks of the system is discussed, including synchronization, channel estimation, equalization, soft-bit demodulation and LDPC en- coding/decoding. A review of State-of-Art algorithms that can be utilized to increase the performance of the system is provided together with a guidelines for practical implementations.

## Multidimensional Cross Parity Check Codes as a Promising Solution to CubeSat Low Data Rate Downlinks

- **Status**: ❌
- **Reason**: CubeSat용 다차원 cross parity check 부호 — LDPC 형태라지만 비-LDPC parity 코드 신규 제안, 떼어낼 바이너리 LDPC 디코더/구성 기법 없음
- **ID**: ieee:8867037
- **Type**: conference
- **Published**: 10-11 Sept
- **Authors**: Ivo Vertat, Ludek Dudacek
- **PDF**: https://ieeexplore.ieee.org/document/8867037
- **Abstract**: Simple cross parity check codes have been well known for decades in the areas of magnetic recording and radiation-hardened memory in space applications. However, the computational power requirements of higher dimensional cross codes mean that priority has been given to different forward error correction methods, with the result that cross parity check codes have not become sufficiently generalized to include a higher number of dimensions. In the last two decades, the focus has mainly been on Reed-Solomon codes, Hamming codes, BCH codes, convolutional codes and turbo codes. In this paper, the issues behind generalized multidimensional parity check codes are explored again in relation to current main-stream interest by covering parity check codes in the form of low-density parity checks. I will put forward a new solution to the multidimensional parity check code decoding process for low data rate downlinks in CubeSat satellites. I propose that the high computational power of software-defined radio can be utilized for iterative decoding of CubeSat satellite transmissions in ground control segments, ensuring that onboard multidimensional parity encoders are as simple to use as possible.
