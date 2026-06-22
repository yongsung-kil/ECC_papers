# IEEE Xplore — 2013-08


## A Variant of the EMS Decoding Algorithm for Nonbinary LDPC Codes

- **Status**: ❌
- **Reason**: nonbinary LDPC EMS 디코딩 - 비이진 GF(q) LDPC, 제외
- **ID**: ieee:6559979
- **Type**: journal
- **Published**: August 201
- **Authors**: Shancheng Zhao, Zhifei Lu, Xiao Ma +1
- **PDF**: https://ieeexplore.ieee.org/document/6559979
- **Abstract**: This letter is concerned with low-complexity decoding algorithms for nonbinary low-density parity-check (NB-LDPC) codes. A new truncation rule based on an adaptive threshold μ is proposed for the extended min-sum (EMS) algorithm. The threshold μ is determined by the mean of the message vector. Therefore, it can be matched to channel observation and decoding iteration. The resulting algorithm is referred to as μ-EMS algorithm. Simulation results show that the μ-EMS algorithm performs almost as well as the Q-ary sum-product algorithm (QSPA). Simulation results also show that the μ-EMS algorithm is simpler than the other X-EMS algorithms for NB-LDPC over high order finite fields.

## Bilayer LDPC Convolutional Codes for Decode-and-Forward Relaying

- **Status**: ❌
- **Reason**: bilayer LDPC convolutional 릴레이 코드 - DF 릴레이 채널 특이적, NAND ECC 이식성 약함
- **ID**: ieee:6544192
- **Type**: journal
- **Published**: August 201
- **Authors**: Zhongwei Si, Ragnar Thobaben, Mikael Skoglund
- **PDF**: https://ieeexplore.ieee.org/document/6544192
- **Abstract**: In this paper we present bilayer LDPC convolutional codes for half-duplex relay channels. Two types of codes, bilayer expurgated LDPC convolutional codes and bilayer lengthened LDPC convolutional codes, are proposed for decode-and-forward (DF) relaying. In the case of the binary erasure relay channel, we prove analytically that both code constructions achieve the capacities of the source-relay link and the source-destination link simultaneously, provided that the channel conditions are known when designing the codes. Meanwhile, both codes enable the highest transmission rate possible with DF relaying for a wide range of channel parameters. In addition, the regular degree distributions can easily be computed from the channel parameters, which significantly simplifies the code optimization. The code construction and performance analysis are extended to the general binary memoryless symmetric channel, where a capacity-achieving performance is conjectured. Numerical results are provided for both types of codes with finite node degrees over binary erasure channels and binary-input additive white Gaussian noise channels, which verify the aforementioned theoretical analysis.

## Joint LDPC and Physical-Layer Network Coding for Asynchronous Bi-Directional Relaying

- **Status**: ❌
- **Reason**: 비동기 양방향 릴레이 물리계층 네트워크 코딩 - 무선 응용 특이적 Log-G-SPA, NAND 이식성 없음
- **ID**: ieee:6338379
- **Type**: journal
- **Published**: August 201
- **Authors**: Xiaofu Wu, Chunming Zhao, Xiaohu You
- **PDF**: https://ieeexplore.ieee.org/document/6338379
- **Abstract**: For practical bi-directional relaying, symbols transmitted by two sources cannot arrive at the relay with perfect symbol and frame alignments and the asynchronous multiple-access channel (MAC) should be seriously considered. In this paper, we consider the Low-Density Parity-Check (LDPC)-coded BPSK signalling over the general asynchronous MAC with both frame and symbol misalignments. For the symbol-asynchronous MAC, we present a formal log-domain generalized sum-product-algorithm (Log-G-SPA) for efficient decoding. When the frame-asynchronism is encountered at the relay, we propose an original approach by employing the cyclic LDPC codes and the simple cyclic-redundancy-check (CRC) coding technique. Simulation results demonstrate the effectiveness of the proposed approach.

## Low-Complexity LP Decoding of Nonbinary Linear Codes

- **Status**: ❌
- **Reason**: 비이진(Z4/GF(4)/GF(8)) LP 디코딩 일반화 — non-binary LDPC 제외 대상
- **ID**: ieee:6559989
- **Type**: journal
- **Published**: August 201
- **Authors**: Mayur Punekar, Pascal O. Vontobel, Mark F. Flanagan
- **PDF**: https://ieeexplore.ieee.org/document/6559989
- **Abstract**: Linear Programming (LP) decoding of Low-Density Parity-Check (LDPC) codes has attracted much attention in the research community in the past few years. LP decoding has been derived for binary and nonbinary linear codes. However, the most important problem with LP decoding for both binary and nonbinary linear codes is that the complexity of standard LP solvers such as the simplex algorithm remains prohibitively large for codes of moderate to large block length. To address this problem, two low-complexity LP (LCLP) decoding algorithms for binary linear codes have been proposed by Vontobel and Koetter, henceforth called the basic LCLP decoding algorithm and the subgradient LCLP decoding algorithm. In this paper, we generalize these LCLP decoding algorithms to nonbinary linear codes. The computational complexity per iteration of the proposed nonbinary LCLP decoding algorithms scales linearly with the block length of the code. A modified BCJR algorithm for efficient check-node calculations in the nonbinary basic LCLP decoding algorithm is also proposed, which has complexity linear in the check node degree. Several simulation results are presented for nonbinary LDPC codes defined over Z4, GF(4), and GF(8) using quaternary phase-shift keying and 8-phase-shift keying, respectively, over the AWGN channel. It is shown that for some group-structured LDPC codes, the error-correcting performance of the nonbinary LCLP decoding algorithms is similar to or better than that of the min-sum decoding algorithm.

## Distributed Joint Source-Channel Coding Using Unequal Error Protection LDPC Codes

- **Status**: ❌
- **Reason**: 분산 소스-채널 결합(JSCC) UEP-LDPC — JSCC는 제외, 떼어낼 신규 ECC 디코더/HW 없음
- **ID**: ieee:6560076
- **Type**: journal
- **Published**: August 201
- **Authors**: Iqbal Shahid, Pradeepa Yahampath
- **PDF**: https://ieeexplore.ieee.org/document/6560076
- **Abstract**: This paper presents a general approach to designing distributed joint source channel (DJSC) codes with arbitrary rates for communication of a pair of correlated binary sources over noisy channels. In this approach, both distributed compression and channel error correction are simultaneously achieved by transmitting, for each source, a fraction of the information bits together with the parity bits of a systematic channel code. This approach is shown to be asymptotically optimal, i.e., any rate-pair in the achievable rate-region can be approached as the codeword length is increased. The practical realization of such a code requi res the design of a pair of channel codes with unequal error protection (UEP) properties determined by the inter-source correlation and the channel capacity available to each source. Towards this end, a linear programming based procedure for jointly optimizing the degree profiles of a pair of irregular LDPC codes to achieve the required UEP properties is presented. Experimental results obtained with both binary symmetric channels and binary-input Gaussian channels are presented, which demonstrate that the proposed UEP-DJSC codes can significantly outperform separate source-channel codes, as well as previously reported joint source-channel coding schemes, particularly for short codeword lengths.

## Improved Successive Cancellation Decoding of Polar Codes

- **Status**: ❌
- **Reason**: polar 코드 SC/SCL/SCS 디코딩 — 비-LDPC, 부호 트리 탐색 기법이라 바이너리 LDPC BP에 이식 불가
- **ID**: ieee:6560025
- **Type**: journal
- **Published**: August 201
- **Authors**: Kai Chen, Kai Niu, Jiaru Lin
- **PDF**: https://ieeexplore.ieee.org/document/6560025
- **Abstract**: As improved versions of the successive cancellation (SC) decoding algorithm, the successive cancellation list (SCL) decoding and the successive cancellation stack (SCS) decoding are used to improve the finite-length performance of polar codes. In this paper, unified descriptions of the SC, SCL, and SCS decoding algorithms are given as path search procedures on the code tree of polar codes. Combining the principles of SCL and SCS, a new decoding algorithm called the successive cancellation hybrid (SCH) is proposed. This proposed algorithm can provide a flexible configuration when the time and space complexities are limited. Furthermore, a pruning technique is also proposed to lower the complexity by reducing unnecessary path searching operations. Performance and complexity analysis based on simulations shows that under proper configurations, all the three improved successive cancellation (ISC) decoding algorithms can approach the performance of the maximum likelihood (ML) decoding but with acceptable complexity. With the help of the proposed pruning technique, the time and space complexities of ISC decoders can be significantly reduced and be made very close to those of the SC decoder in the high signal-to-noise ratio regime.

## Joint Source-Channel Coding for Deep-Space Image Transmission using Rateless Codes

- **Status**: ❌
- **Reason**: JSCC rateless(GF(4) Raptor) 이미지전송 - 소스-채널 결합·비이진 부호, 떼어낼 ECC 기법 없음
- **ID**: ieee:6549238
- **Type**: journal
- **Published**: August 201
- **Authors**: O. Y. Bursalioglu, G. Caire, D. Divsalar
- **PDF**: https://ieeexplore.ieee.org/document/6549238
- **Abstract**: A new coding scheme for image transmission over noisy channel is proposed. Similar to standard image compression, the scheme includes a linear transform followed by successive refinement scalar quantization. Unlike conventional schemes, though, in the proposed system the quantized transform coefficients are linearly mapped into channel symbols using systematic linear encoders. This fixed-to-fixed length "linear index coding" approach avoids the use of an explicit entropy coding stage (e.g., arithmetic or Huffman coding), which is typically fragile to channel post-decoding residual errors. We use linear codes over GF(4), which are particularly suited for this application, since they are matched to the dead-zone quantizer symbol alphabet and to the QPSK modulation used on the deep-space communication channel. We optimize the proposed system where the linear codes are systematic Raptor codes over GF(4). The rateless property of Raptor encoders allows to implement a "continuum" of coding rates, in order to accurately match the channel coding rate to the transmission channel capacity and to the quantized source entropy rate for each transform subband and refinement level. Comparisons are provided with respect to the concatenation of state-of-the-art image coding and channel coding schemes used by Jet Propulsion Laboratories (JPL) for the Mars Exploration Rover (MER) Mission.

## On the design of a novel joint network-channel coding scheme for the multiple access relay channel

- **Status**: ❌
- **Reason**: non-binary 결합 네트워크-채널 코드 - 비이진 LDPC 및 무선 릴레이 특이적, 제외
- **ID**: ieee:6330081
- **Type**: journal
- **Published**: August 201
- **Authors**: Mikel Hernaez, Pedro M. Crespo, Javier Del Ser
- **PDF**: https://ieeexplore.ieee.org/document/6330081
- **Abstract**: This paper proposes a novel joint non-binary network-channel code for the Time-Division Decode-and-Forward Multiple Access Relay Channel (TD-DF-MARC), where the relay linearly combines — over a non-binary finite field — the coded sequences from the source nodes. A method based on an EXIT chart analysis is derived for selecting the best coefficients of the linear combination. Moreover, it is shown that for different setups of the system, different coefficients should be chosen in order to improve the performance. This conclusion contrasts with previous works where a random selection was considered. Monte Carlo simulations show that the proposed scheme outperforms, in terms of its gap to the outage probabilities, the previously published joint network-channel coding approaches. Besides, this gain is achieved by using very short-length codewords, which makes the scheme particularly attractive for low-latency applications.

## Faster-Than-Nyquist Signaling

- **Status**: ❌
- **Reason**: Faster-than-Nyquist 시그널링 서베이, 변조 기법으로 LDPC ECC 이식 기법 없음
- **ID**: ieee:6479673
- **Type**: journal
- **Published**: Aug. 2013
- **Authors**: John B. Anderson, Fredrik Rusek, Viktor Öwall
- **PDF**: https://ieeexplore.ieee.org/document/6479673
- **Abstract**: In this paper, we survey faster-than-Nyquist (FTN) signaling, an extension of ordinary linear modulation in which the usual data bearing pulses are simply sent faster, and consequently are no longer orthogonal. Far from a disadvantage, this innovation can transmit up to twice the bits as ordinary modulation at the same bit energy, spectrum, and error rate. The method is directly applicable to orthogonal frequency division multiplex (OFDM) and quadrature amplitude modulation (QAM) signaling. Performance results for a number of practical systems are presented. FTN signaling raises a number of basic issues in communication theory and practice. The Shannon capacity of the signals is considerably higher.

## Low-Complexity Iterative Row-Column Soft Decision Feedback Algorithm for 2-D Inter-Symbol Interference Channel Detection With Gaussian Approximation

- **Status**: ❌
- **Reason**: 2D ISI 채널 검출기(BCJR/GA) 복잡도 감소가 핵심, LDPC는 부수적 외부코드 베이스라인일 뿐 떼어낼 LDPC 기법 없음
- **ID**: ieee:6418035
- **Type**: journal
- **Published**: Aug. 2013
- **Authors**: Jianping Zheng, Xiao Ma, Yong Liang Guan +2
- **PDF**: https://ieeexplore.ieee.org/document/6418035
- **Abstract**: In this paper, we study the complexity reduction problem of the iterative row-column soft decision feedback algorithm (IRCSDFA) for 2-D inter-symbol interference (ISI) detection. Specifically, Gaussian approximation (GA) is employed in both the component row and column detectors of the IRCSDFA in order to reduce its computational complexity. With the employment of GA, the state space dimension of the ISI trellis of either component detector can be reduced enormously (i.e., the number of branches in one ISI trellis section decreases). Bahl-Cocke-Jelinek-Raviv (BCJR) algorithm is then employed to perform detection over the GA-simplified ISI trellis. For brevity, we refer to the IRCSDFA with BCJR detection over the GA-simplified ISI trellis as “IRCSDFA-GA-BCJR”. Next, the iteration scheduling of component detectors and decoder in coded 2-D ISI channels with low density parity check (LDPC) coding and IRCSDFA-GA-BCJR detection is studied. Specifically, three iteration schemes: single detector (row or column) scheme, alternate detector scheme, and combined detector scheme, are considered, with the last scheme showing the best coded performance. Finally, the computational complexity of the proposed IRCSDFA-GA-BCJR is analyzed, and shown to have significant reduction with a cost of only about 0.3 and 0.35 dB in coded BER/FER performance loss compared to the conventional IRCSDFA without GA and the optimal symbol-based BCJR algorithm, respectively.

## Network Coding Meets Multimedia: A Review

- **Status**: ❌
- **Reason**: 네트워크 코딩 멀티미디어 서베이, LDPC ECC와 무관하며 떼어낼 디코더/HW/코드설계 기법 없음
- **ID**: ieee:6416071
- **Type**: journal
- **Published**: Aug. 2013
- **Authors**: Enrico Magli, Mea Wang, Pascal Frossard +1
- **PDF**: https://ieeexplore.ieee.org/document/6416071
- **Abstract**: While every network node only relays messages in a traditional communication system, the recent network coding (NC) paradigm proposes to implement simple in-network processing with packet combinations in the nodes. NC extends the concept of “encoding” a message beyond source coding (for compression) and channel coding (for protection against errors and losses). It has been shown to increase network throughput compared to traditional networks implementation, to reduce delay and to provide robustness to transmission errors and network dynamics. These features are so appealing for multimedia applications that they have spurred a large research effort towards the development of multimedia-specific NC techniques. This paper reviews the recent work in NC for multimedia applications and focuses on the techniques that fill the gap between NC theory and practical applications. It outlines the benefits of NC and presents the open challenges in this area. The paper initially focuses on multimedia-specific aspects of network coding, in particular delay, in-network error control, and media-specific error control. These aspects permit to handle varying network conditions as well as client heterogeneity, which are critical to the design and deployment of multimedia systems. After introducing these general concepts, the paper reviews in detail two applications that lend themselves naturally to NC via the cooperation and broadcast models, namely peer-to-peer multimedia streaming and wireless networking.

## A new iterative LT decoding algorithm for binary and nonbinary Galois fields

- **Status**: ❌
- **Reason**: LT/fountain 코드 디코딩(erasure), 비이진 GF 포함이며 fountain/erasure는 제외 대상
- **ID**: ieee:6608220
- **Type**: journal
- **Published**: Aug. 2013
- **Authors**: Yuexin Mao, Jie Huang, Bing Wang +3
- **PDF**: https://ieeexplore.ieee.org/document/6608220
- **Abstract**: Digital fountain codes are record-breaking codes for erasure channels. They have many potential applications in both wired and wireless communications. Most existing digital fountain codes operate over binary fields using an iterative belief-propagation (BP) decoding algorithm. In this paper, we propose a new iterative decoding algorithm for both binary and nonbinary fields. The basic form of our proposed algorithm considers both degree-1 and degree-2 check nodes (instead of only degree-1 check nodes as in the original BP decoding scheme), and has linear complexity. Extensive simulation demonstrates that it outperforms the original BP decoding scheme, especially for a small number of source packets. The enhanced form of the proposed algorithm combines the basic form of the algorithm and a guess-based algorithm to further improve the decoding performance. Simulation results demonstrate that it can provide better decoding performance than the guess-based algorithm with fewer guesses, and can achieve decoding performance close to that of the maximum likelihood decoder at a much lower decoding complexity. Last, we show that our nonbinary scheme has the potential to outperform the binary scheme when choosing suitable degree distributions, and furthermore it is insensitive to the size of the Galois field.

## On the LDPC-coded relay cooperation with multiple receive antennas and joint iterative decoding in the destination

- **Status**: ❌
- **Reason**: LDPC-coded relay 협력+joint iterative decoding, 무선 응용 특이적; 표준 BP를 multi-antenna Tanner graph에 적용, 떼어낼 신규 디코더/HW 없음
- **ID**: ieee:6663869
- **Type**: conference
- **Published**: 5-8 Aug. 2
- **Authors**: Lei Tang, Fengfan Yang, Shunwai Zhang
- **PDF**: https://ieeexplore.ieee.org/document/6663869
- **Abstract**: In this paper, we propose an low-density parity-check codes (LDPC)-coded relay cooperation with receive multi-antenna in the destination over a Rayleigh fading channel, where maximal ratio combining and belief propagation algorithm (BP)-based joint iterative decoding based on the introduced treble-layer Tanner graph are designed to detect and decode the corrupted received sequence at the destination. Theoretical analysis and numerical simulation exhibit that the proposed approach can well combine the diversity and coding gains, which results in significant advantage over the conventional coded cooperation and non-cooperation schemes under the same conditions.

## Joint LDPC-DQPSK iteration system for underwater acoustic communications

- **Status**: ❌
- **Reason**: joint LDPC-DQPSK 반복검출 수중음향통신 — 무선 응용 특이적, 표준 turbo 원리, 떼어낼 LDPC ECC 기법 없음
- **ID**: ieee:6663949
- **Type**: conference
- **Published**: 5-8 Aug. 2
- **Authors**: Fu Fang, Zhao Dan-feng
- **PDF**: https://ieeexplore.ieee.org/document/6663949
- **Abstract**: To reduce inter-symbol-interference (ISI) in underwater acoustic channels, a communication system based on joint LDPC-DQPSK iterative detection was proposed. Spread spectrum technology was adopted to increase communication distance and to combat multi-path effect. Joint LDPC-DQPSK iteration is essentially a joint demodulation and decoding iterative detection based on Turbo principle. To verify BER performance of proposed system, simulation experiments over typical underwater acoustic channels were carried out. Experiment results show that proposed system outperforms conventional systems. Proposed system with four rounds of joint iterations can obtain 3.5 dB SNR gains compared with conventional systems at BER of 10-4.

## Generalized space-time shift keying: Randomized bitwise Markov chain Monte Carlo detection and code design

- **Status**: ❌
- **Reason**: G-STSK MCMC 검출+EXIT 기반 LDPC 최적화 — 무선 변조 특이 코드 최적화, 표준 EXIT 사용, 떼어낼 신규 기법 없음
- **ID**: ieee:6664095
- **Type**: conference
- **Published**: 5-8 Aug. 2
- **Authors**: Jianping Zheng, Yue Sun
- **PDF**: https://ieeexplore.ieee.org/document/6664095
- **Abstract**: In this paper, the low-complexity near-optimal (LCNO) detector and code design for the generalized space-time shift keying (G-STSK) scheme are studied. First, the LCNO randomized bitwise Markov chain Monte Carlo (R-b-MCMC) detector is presented. Next, the low-density parity-check code is optimized based on the extrinsic-information transfer chart technique. Simulation results are provided to demonstrate the performance of the proposed detector and the optimized code.

## Asynchronous two-step physical-layer network coding scheme for broadband two-way Relaying

- **Status**: ❌
- **Reason**: physical-layer network coding(two-way relay) — LDPC ECC 기법 아님, 채널/네트워크 코딩 결합 무선 응용
- **ID**: ieee:6664113
- **Type**: conference
- **Published**: 5-8 Aug. 2
- **Authors**: Cong Wang, Wei Xie, Xiaochen Xia +2
- **PDF**: https://ieeexplore.ieee.org/document/6664113
- **Abstract**: In two-way OFDM relay, carrier frequency offsets (CFOs) between relay and terminal nodes introduce severe intercarrier interference (ICI) which degrades the performance of traditional physical-layer network coding (PLNC). Moreover, traditional algorithm to compute the posteriori probability in the presence of ICI would incur prohibitive computational complexity at the relay node. In this paper, we proposed a two-step asynchronous PLNC scheme at the relay to mitigate the effect of CFOs. In the first step, we intend to reconstruct the ICI component, in which space-alternating generalized expectation-maximization (SAGE) algorithm is used to jointly estimate the needed parameters. In the second step, a channel-decoding and network-coding scheme is proposed to transform the received signal into the XOR of two terminals' transmitted information using the reconstructed ICI. It is shown that the proposed scheme greatly mitigates the impact of CFOs with a relatively lower computational complexity in two-way OFDM relay.

## IEEE 802.15.4g SUN MR-OQPSK PHY using a novel CA-CDM scheme

- **Status**: ❌
- **Reason**: turbo product code(SPC+Hadamard) 기반 CA-CDM, 비-LDPC 부호+무선 응용 특이적
- **ID**: ieee:6766021
- **Type**: conference
- **Published**: 29-31 Aug.
- **Authors**: KeunHyung Lee, TaeJoon Park, HoYong Kang
- **PDF**: https://ieeexplore.ieee.org/document/6766021
- **Abstract**: This paper presents a constant amplitude code division multiplexing scheme and the corresponding decoding algorithm for the IEEE 802.15.4g network (WPAN) standard for advanced utility service. The proposed scheme based on a turbo product code (TPC) consists of single parity check code and Hadamard code. Thus, an iterative TPC decoder can be exploited within a receiver for the proposed scheme. The proposed scheme offers constant amplitude output with low peak-to-average power ratio compared to conventional code division multiplexing schemes.

## Full Diversity LDPC Codes with a Reduced Structure for General Block Fading Channels

- **Status**: ❌
- **Reason**: 블록 페이딩 채널용 full-diversity LDPC 구성 — 무선 채널 특이적, NAND에 떼어낼 신규 코드설계 기법 없음
- **ID**: ieee:6629833
- **Type**: conference
- **Published**: 27-30 Aug.
- **Authors**: C. T. Healy, R. C. de Lamare
- **PDF**: https://ieeexplore.ieee.org/document/6629833
- **Abstract**: A general class of codes capable of near-outage performance on the block fading channel with any number of independent fading coefficients is proposed. The code class requires fewer restrictions on the graph structure than previously proposed methods and demonstrate comparable performance. In addition, it is demonstrated via simulations that the proposed codes can be adapted for use on varying block fading channels, through the use of a simple puncturing scheme.

## Iterative FDE Design for LDPC-coded Magnitude Modulation Schemes

- **Status**: ❌
- **Reason**: 광대역 무선 SC magnitude modulation + IB-DFE turbo 등화에 LDPC 부수 사용. 무선 응용 특이적, 떼어낼 신규 LDPC ECC 기법 없음
- **ID**: ieee:6629774
- **Type**: conference
- **Published**: 27-30 Aug.
- **Authors**: Marco Gomes, Rui Dinis, Vitor Silva +2
- **PDF**: https://ieeexplore.ieee.org/document/6629774
- **Abstract**: In this paper we consider the design of broadband wireless systems with high power efficiency. For this purpose we employ magnitude modulation (MM) techniques for single carrier (SC) signals, to reduce the PAPR of the transmitted signals, combined with powerful low-density parity check (LDPC) codes and iterative frequency-domain equalization based on the IB-DFE concept (Iterative Block Decision Feedback Equalization) that are particularly effective on dealing with the severe distortion of multipath time dispersive channels. Different turbo frequency domain equalization schemes are proposed and their performance compared with the combination of MM-IB-DFE and a LDPC iterative decoder. It is shown that for the case of transmissions employing channel coding, considerable efficiency gains above 2dB can be obtained from using MM with no added complexity to the turbo IB-DFE receiver

## Repeat Accumulate Based Constructions for LDPC Codes on Fading Channels

- **Status**: ❌
- **Reason**: Root-Check IRAA LDPC, 블록/패스트 페이딩 채널 전용 PEG 구성. 페이딩 다이버시티 의존적이라 NAND 이식성 약함, 무선 응용 특이적
- **ID**: ieee:6629768
- **Type**: conference
- **Published**: 27-30 Aug.
- **Authors**: Andre G. D. Uchoa, Cornelius Healy, Rodrigo C. de Lamare
- **PDF**: https://ieeexplore.ieee.org/document/6629768
- **Abstract**: Irregular repeat-accumulate Root-Check LDPC codes based on Progressive Edge Growth (PEG) techniques for block-fading channels are proposed. The proposed Root-Check LDPC codes are both suitable for channels under F = 2, 3 independent fadings per codeword and for fast fading channels. An Irregular Repeat-Accumulate and Accumulate IRAA Root- Check structure is devised for F = 2, 3 independent fadings. The performance of the new codes is investigated in terms of the Frame Error Rate (FER). Numerical results show that the IRAA LDPC codes constructed by the proposed algorithm outperform by about 1dB the existing IRA Root-Check LDPC codes under fast-fading channels.

## Block-Fading Channels at Finite Blocklength

- **Status**: ❌
- **Reason**: 블록페이딩 유한블록길이 최대달성률 튜토리얼(순수 이론 bound). 디코더/HW/구성으로 안 이어짐
- **ID**: ieee:6629767
- **Type**: conference
- **Published**: 27-30 Aug.
- **Authors**: Wei Yang, Giuseppe Durisi, Tobias Koch +1
- **PDF**: https://ieeexplore.ieee.org/document/6629767
- **Abstract**: This tutorial paper deals with the problem of characterizing the maximal achievable rate R* (n, e) at a given blocklength n and error probability e over block-fading channels. We review recent results that establish tight bounds on R* (n, e) and characterize its asymptotic behavior. Comparison between the theoretical results and the data rates achievable with the coding scheme used in LTE-Advanced are reported.

## Linear Precoder Design for Correlated Partially Coherent Channels with Discrete Inputs

- **Status**: ❌
- **Reason**: MIMO 부분코히어런트 채널 선형 프리코더 설계. 채널코딩/LDPC 무관, 떼어낼 ECC 기법 없음
- **ID**: ieee:6629755
- **Type**: conference
- **Published**: 27-30 Aug.
- **Authors**: Animesh Yadav, Markku Juntti, Jorma Lilleberg
- **PDF**: https://ieeexplore.ieee.org/document/6629755
- **Abstract**: We consider the single-user multiple-input multipleoutput (MIMO) precoder design problem for the spatially correlated partially coherent Rayleigh fading channels with discrete inputs. The objective is to design a linear precoder to adapt to the degradation caused by the imperfect channel estimation at the receiver and the transmit-receive antenna correlation. The system is partially coherent so that the MIMO channel coefficients are estimated at the receiver and its error covariance matrix is fed back to the transmitter.We derive the cutoff rate (CR) expression, an alternative to the mutual information (MI), and propose to use it as a design criterion to design the linear precoders. A linear precoder is obtained by numerically maximizing the CR w.r.t. the precoder matrix with a given average power constraint. Two step optimization algorithm is proposed to find a close-to-optimal precoder matrix. Precoders are designed to be used in conjunction with space-time block codes (STBCs). Numerical examples show that the performance gains of the newly designed CR precoders are significant compared to the CR optimized partially coherent constellations (PCCs) and conventional codewords.

## Performance enhancement of optical QPSK systems with coherent reception for high speed links

- **Status**: ❌
- **Reason**: 광 QPSK에서 LDPC가 RS/concatenated와 단순 비교되는 부수 언급, 떼어낼 신규 LDPC 기법 없음
- **ID**: ieee:6637246
- **Type**: conference
- **Published**: 22-25 Aug.
- **Authors**: D. Jokhakar Jignesh, U. Sripati, Muralidhar Kulkarni
- **PDF**: https://ieeexplore.ieee.org/document/6637246
- **Abstract**: Coherent optical QPSK systems have attracted the attention of the research community and the Optical industry on account of features such as low power requirement and high receiver sensitivity. This can bring about a reduction in the transmitter power levels as well as the link margin to maintain a required BER. However, in order to realize a coherent detection system, the local oscillator laser needs to be synchronized with the transmitter laser diode. This can be achieved by using an optical (Phase Lock Loop) PLL at the receiver for medium data rate (Mbps). But for high data rate applications (data rates in terms of Gbps), optical PLLs are not practically realizable. In this paper, we have analyzed the use of Viterbi and Viterbi Phase Estimation Algorithm for phase synchronization. We have carried out the BER calculations and determined the BER performance degradation when compared to ideal uncoded QPSK BER performance when synchronization is not maintained. The use of Viterbi and Viterbi phase estimation algorithm brings about an improvement in BER even in the absence of an optical synchronizing arrangement. This performance improvement is further enhanced with the use of suitable error control codes. A comparison has been made between various Error Control Codes such as Reed-Solomon (RS) codes, Concatenated codes comprising of a RS and convolutional code and Low Density Parity check (LDPC) codes. We have quantified the improvement achievable with the use of these codes.

## FPGA implementation and verification of LDPC minimum sum algorithm decoder with weight (3, 6) regular parity check matrix

- **Status**: ❌
- **Reason**: 표준 (3,6) regular MSA 디코더의 FPGA 단순 구현, 새 기여 없는 교과서 수준 min-sum
- **ID**: ieee:6743140
- **Type**: conference
- **Published**: 16-19 Aug.
- **Authors**: Yi-Hua Chen, Chang-Lueng Chu, Jheng-Shyuan He
- **PDF**: https://ieeexplore.ieee.org/document/6743140
- **Abstract**: This work uses a regular parity check matrix with weight (3, 6) on the 5641R plate card of the Software-Defined Radio (SDR) system developed by National Instruments. The Min-Sum Algorithm (MSA) decoder of the Low Density Parity Check (LDPC) codes is completed using the LabVIEW FPGA. Subsequently, integration with the approximate lower triangular LDPC codes complement the complete LDPC encoding and decoding system. In addition to an explicit description of the decoding mechanism of the LDPC-code MSA decoder, analyses of decoding program optimization efficiency and Bit Error Rate (BER) performance curves are conducted. The program simulation results of FPGA indicate that under the additive white Gaussian noise environment, if the BER is 1 E-05, the Signal-to-Noise Ratio (SNR) without using LDPC code is 9.6 dB. The SNR of the LDPC MSA decoder with a min-sum one iteration and ten iterations are 6.8 dB and 6 dB, respectively; the coding gain of the MSA decoder with min-sum one iteration and 10 iterations is 2.8 dB and 3.6 dB, respectively, showing a discrepancy of 0.8 dB.

## LDPC coded MSK-BOC modulation for satellite navigation system

- **Status**: ❌
- **Reason**: 위성항법 변조(MSK-BOC) 신호설계에 LDPC 부수 언급, 떼어낼 디코더·코드설계 기법 없음
- **ID**: ieee:6743220
- **Type**: conference
- **Published**: 16-19 Aug.
- **Authors**: Xue Rui, Xu Xichao, Wei Qiang +1
- **PDF**: https://ieeexplore.ieee.org/document/6743220
- **Abstract**: Signal structure is one of the decisive factors of the inherent performance of satellite navigation system, meanwhile it is one of the critical technologies which must be resolved during system design and upgrading process. In order to improve code tracking precision and have the better bit error rate (BER) ability at the same time, we combine low-density party-check (LDPC) codes and minimum shift keying (MSK) with binary offset carrier (BOC), which called LDPC coded MSK-BOC (LDPC-MSK-BOC). Theoretic analysis and simulation results show that the proposed signal system can not only achieve lower BER, but also have better performance in the aspects of Multipath Error, code tracking error and Gabor Bandwidth. Meanwhile, the proposed signal structure can provide potential opportunities for Global Navigation Satellite System (GNSS) modernization and construction, such as Galileo, Compass, and so on.

## Packet loss recovery algorithm based on row-column coding and RS coding

- **Status**: ❌
- **Reason**: 패킷손실 복구(행-열+RS) erasure 코딩 - 비-LDPC, 채널 ECC 디코더 기법 없음
- **ID**: ieee:6694718
- **Type**: conference
- **Published**: 14-16 Aug.
- **Authors**: Yatian Li, Ping Chen, Qiyue Yu +1
- **PDF**: https://ieeexplore.ieee.org/document/6694718
- **Abstract**: Nowadays, the end-to-end network is widely used to transmit multimedia information over Internet Protocol (IP) network, and TCP (Transmission Control Protocol) is employed to guarantee the quality of service (QoS) when packet loss happened. However, the transmit delay increases by TCP, and it could not be acceptable for real-time data communications. Thereby, this paper provides a kind of packet loss recovery algorithms that combines single parity check and RS coding, in which case coding is done not only to a single data block but also to different blocks. Simulation results show that the provided algorithm can improve the transmission reliability at packet-level, meanwhile the delay can be controlled short enough for real-time network.

## A novel repeat accumulate codes for 40-Gb/s OFDM-ROF systems

- **Status**: ❌
- **Reason**: RA코드 OFDM-ROF 광통신 응용 - 비-LDPC, 떼어낼 신규 디코더/구성 기법 없음
- **ID**: ieee:6694704
- **Type**: conference
- **Published**: 14-16 Aug.
- **Authors**: Juan Nie, Ming Chen
- **PDF**: https://ieeexplore.ieee.org/document/6694704
- **Abstract**: As we know that, data rate and fiber length lead to fiber non-linearity, chromatic dispersion and polarization mode dispersion phenomenon. which are seriously affect bit error rate (BER) in the long optical channels system. In this paper we consider repeat-accumulate (RA) codes as channel coding in OFDM Radio over Fiber system to enhance the optical transmission performance. The message passing algorithm is used to decoded RA code. We propose and demonstrate a new channel code employeed in Orthogonal Frequency Division Multiplexing (OFDM). We analysed the performance of RA code, evaluated the BER when the RA code employed in OFDM-ROF system. Results show that choosing the RA code as the channel code for our proposed system can reduce BER to 10−4 after 150km transmission. Our study can give a meaningful guidance for forward error correction code to compensation signal linear distortion type in OFDM Radio over Fiber system.

## Decoding algorithms for binary LDPC coded Gaussian interference channels

- **Status**: ❌
- **Reason**: Gaussian 간섭채널 결합디코딩(NB-LDPC 취급, 채널구조 활용). 무선 간섭채널 특이적이고 NB-LDPC — 제외
- **ID**: ieee:6671086
- **Type**: conference
- **Published**: 12-14 Aug.
- **Authors**: Shancheng Zhao, Xiao Ma, Baoming Bai
- **PDF**: https://ieeexplore.ieee.org/document/6671086
- **Abstract**: This paper is concerned with Gaussian interference channels (GIFC) in which all transmitters are coded with binary low-density parity-check (LDPC) codes. We focus on the design of decoding algorithms. The main contributions of this paper include: 1) we present three types of iterative decoding algorithms (IDA), which are computing-decoding type, decoding computing type and computing-decoding-computing type, respectively; 2) we propose a joint decoding algorithm (JDA) by treating the system as a nonbinary LDPC (NB-LDPC) coded system; 3) we propose a time-varying signaling scheme for the joint decoding algorithm. Numerical results show that, 1) for weak interference, the four decoding algorithms have almost the same error performances, 2) for moderate and strong interference, the JDA has the best error performance. These results show that structures in interference can be utilized to achieve better performances. In addition, it is shown by simulation that, from moderate to strong interference, the time-varying signaling scheme significantly outperforms the constant signaling scheme when decoded with the JDA (8.5 dB for strong interference).

## Effect of the threshold offset on the performance of UEP LDPC codes

- **Status**: ❌
- **Reason**: UEP-LDPC threshold offset 효과 분석(degree distribution 최적화)이나 HOC 무선 UEP 특이적, NAND 이식 신기여 없음 — 제외
- **ID**: ieee:6671088
- **Type**: conference
- **Published**: 12-14 Aug.
- **Authors**: Abdul Wakeel, Werner Henkel, Feifei Gao
- **PDF**: https://ieeexplore.ieee.org/document/6671088
- **Abstract**: This letter addresses the effect of threshold offset on the average performance and UEP capability of higher order constellation (HOC) unequal error protection low density parity check (UEP-LDPC) codes. We optimize the variable node degree distribution for an HOC UEP-LDPC code at a minimum threshold, with a fixed check node degree distribution and code rate. The average performance and the UEP capability of the ensemble code for a marginal offset in the threshold value were investigated. The simulation results show that the average performance and UEP capability can be enhanced by a slight offset in the threshold value. We looked into the connectivity between protection classes due to the threshold offset for a possible answer to the performance gain.

## Nonbinary LDPC-coded differential modulation with reduced-complexity decoding

- **Status**: ❌
- **Reason**: 비이진 q-ary LDPC 차분변조 결합검출-디코딩. 비이진 LDPC는 제외
- **ID**: ieee:6671087
- **Type**: conference
- **Published**: 12-14 Aug.
- **Authors**: Minghua Li, Baoming Bai, Xiao Ma
- **PDF**: https://ieeexplore.ieee.org/document/6671087
- **Abstract**: In this paper, we apply q-ary LDPC codes to differential modulation systems, and study the design and performance of the resultant coded modulation systems. Two low-complexity joint detection-decoding methods for noncoherent demodulation are proposed, in which the hard-message-passing strategy is used for a joint factor graph. The first method is based on the joint detection-decoding algorithm introduced in [1]; and the second one is developed by combining trellis-based differential detection and the hard-decision-based decoding of nonbinary LDPC codes. The Max-Log-MAP algorithm with soft-in hard-out is used for the differential detection. Simulation results show that both methods offer acceptable performances with greatly reduced complexities.
