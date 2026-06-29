# IEEE Xplore — 2010-02


## Construction of nonbinary quasi-cyclic LDPC cycle codes based on singer perfect difference set

- **Status**: ❌
- **Reason**: 비이진(nonbinary) QC-LDPC cycle code 구성 → 비이진 LDPC 제외 대상
- **ID**: ieee:5403627
- **Type**: journal
- **Published**: February 2
- **Authors**: Chao Chen, Baoming Bai, Xinmei Wang
- **PDF**: https://ieeexplore.ieee.org/document/5403627
- **Abstract**: A low-density parity-check (LDPC) code whose parity-check matrix consists of weight-2 columns is known as a cycle code. In this letter, we propose a construction of nonbinary quasi-cyclic (QC) LDPC cycle codes based on Singer perfect difference set. The Tanner graph has girth 12 and the code length achieves the Gallager lower bound. We further show that constructed codes have exactly a minimum symbol Hamming distance 6. Simulation results show that the proposed codes perform better than random nonbinary LDPC cycle codes.

## Analysis of the joint network LDPC codes over orthogonal multi-access relay channel

- **Status**: ❌
- **Reason**: network LDPC의 relay 채널 용량/임계 분석(Gaussian approx)으로 무선 응용 특이적, 떼어낼 디코더/HW/구성 기법 없음
- **ID**: ieee:5403628
- **Type**: journal
- **Published**: February 2
- **Authors**: Ying Li, Guanghui Song, Lili Wang
- **PDF**: https://ieeexplore.ieee.org/document/5403628
- **Abstract**: The capacity approaching behavior of the joint network LDPC code is analyzed in this paper. We first derive the upper bound of the sum capacity of the orthogonal multiaccess relay channel where two sources communicate with one destination in the presence of one relay. Then, a new generalized Gaussian approximation method is designed to predict the decoding threshold of the joint network LDPC code. Results show that under the symmetric channel, the gap between the upper bound of the sum capacity and the decoding threshold ranges from 0.3 dB to 0.6 dB.

## Distance-Enhancing Constrained Codes with Parity-Check Constraints for Data Storage Channels

- **Status**: ❌
- **Reason**: 제약부호+PC 결합 설계(RMTR/MTR), 일반 선형 PC 부호 대상이며 LDPC 디코더/구성 기법 아님
- **ID**: ieee:5402488
- **Type**: journal
- **Published**: February 2
- **Authors**: Kui Cai, Kees A. Schouhamer Immink, Yuan Xing Lee +2
- **PDF**: https://ieeexplore.ieee.org/document/5402488
- **Abstract**: This paper proposes efficient distance-enhancing constrained codes with parity-check (PC) constraints for data storage channels. We first propose simple and efficient finitestate encoding methods to design various distance-enhancing constrained codes, including a repeated minimum transition runlength (RMTR) code for optical recording channels, as well as a maximum transition run (MTR) code for magnetic recording channels. We further propose a general and systematic code design methodology, which can efficiently combine constrained codes with PC codes. The constrained codes can be any distanceenhancing constrained codes. The PC codes can be any linear binary PC codes. The rates of the designed codes are only a few tenths of a percent below the theoretical maximum. The proposed method enables soft information to be available to the PC decoder and soft decoding of PC codes. Examples of several newly designed distance-enhancing constrained PC codes are illustrated. Simulation results with blu-ray disc (BD) systems show that the proposed new RMTR code and RMTR constrained 4-bit PC code perform 0.2 dB and 0.85 dB better than the standard 17PP code, respectively, at error correction code (ECC) failure rate (EFR) of 10-12 and high recording density.

## Design of turbo-like codes for short frames

- **Status**: ❌
- **Reason**: turbo-like 부호 자체 설계(SFC 컴포넌트+serial BP)로 비-LDPC 부호 설계가 핵심, 바이너리 LDPC BP에 떼어낼 부호 비의존 기법 없음
- **ID**: ieee:5403624
- **Type**: journal
- **Published**: February 2
- **Authors**: Fan Yang, Zhendong Luo, Baoyu Tian +1
- **PDF**: https://ieeexplore.ieee.org/document/5403624
- **Abstract**: Turbo codes have been shown to yield very good performance for long block sizes. However, their performance degrades when the frame size decreases. Furthermore, decoding turbo codes with the maximum a posteriori (MAP) algorithm or the soft output Viterbi algorithm (SOVA) is quite complex. We proposed a type of turbo-like (TL) codes for short frame transmission. The component encoder of a TL code is a systematic feed-forward convolutional (SFC) code designed without 4-cycles and the associated component decoder uses serial belief propagation rule. TL codes are linear-time encodable and they can be decoded by belief propagation (BP) algorithms with very low complexity.

## LDPC code design for asynchronous Slepian-Wolf coding

- **Status**: ❌
- **Reason**: Slepian-Wolf 분산 소스코딩용 LDPC 설계 → 소스 코딩(채널 ECC 아님) 제외
- **ID**: ieee:5407617
- **Type**: journal
- **Published**: February 2
- **Authors**: Zhibin Sun, Chao Tian, Jun Chen +1
- **PDF**: https://ieeexplore.ieee.org/document/5407617
- **Abstract**: We consider asynchronous Slepian-Wolf coding where the two encoders may not have completely accurate timing information to synchronize their individual block code boundaries, and propose LDPC code design in this scenario. A new information-theoretic coding scheme based on source splitting is provided, which can achieve the entire asynchronous Slepian-Wolf rate region. Unlike existing methods based on source splitting, the proposed scheme does not require common randomness at the encoder and the decoder, or the construction of super-letter from several individual symbols. We then design LDPC codes based on this new scheme, by applying the recently discovered source-channel code correspondence. Experimental results validate the effectiveness of the proposed method.

## Channel Modeling and Signal Processing for Probe Storage Channels

- **Status**: ❌
- **Reason**: probe-storage 채널 모델 + (d,k) 변조코드 결합 디코딩 특이적, LDPC는 외부 부호 벤치마크로 부수 언급, 떼어낼 LDPC 기법 없음
- **ID**: ieee:5402481
- **Type**: journal
- **Published**: February 2
- **Authors**: Haralampos Pozidis, Giovanni Cherubini, Angeliki Pantazi +2
- **PDF**: https://ieeexplore.ieee.org/document/5402481
- **Abstract**: Probe-storage devices employ large arrays of probes to write/read data in parallel in some storage medium, and combine ultra-high density, low access times, and low power consumption. A particular probe-storage technique utilizes thermomechanical means to store and retrieve information in thin polymer films. In this paper, a system-level channel model for the thermomechanical probe-storage channel is presented. Each of the components of the proposed model is derived by extensive characterization of experimentally obtained readback signals from probe recording tests. Moreover, detection techniques that are actually utilized in a probe-storage prototype implementation are described, followed by coding techniques for added reliability in the presence of particles or other impurities of the storage medium. In addition to low-complexity coding constructs, a concatenated coding scheme with an outer LDPC and inner modulation code is considered, in order to establish a benchmark for overall system performance. A novel methodology for joint decoding of outer LDPC and inner (d,k) modulation codes is developed. Furthermore, an optimal soft decoder for the modulation code is proposed, based on a modification of the decoder metrics to accurately account for the probe storage channel output statistics. Experimental results are used throughout the paper to validate the channel model and identify its relevant parameters, as well as to verify the system performance obtained by simulations.

## Approaching MIMO capacity using bitwise Markov Chain Monte Carlo detection

- **Status**: ❌
- **Reason**: MIMO용 MCMC 검출기가 핵심, LDPC는 부수적 결합부호, 떼어낼 디코더 기법 없음
- **ID**: ieee:5407603
- **Type**: journal
- **Published**: February 2
- **Authors**: Rong-rong Chen, Ronghui Peng, Alexei Ashikhmin +1
- **PDF**: https://ieeexplore.ieee.org/document/5407603
- **Abstract**: This paper examines near capacity performance of Markov Chain Monte Carlo (MCMC) detectors for multiple-input and multiple-output (MIMO) channels. The proposed MCMC detector (Log-MAP-tb b-MCMC) operates in a strictly bit-wise fashion and adopts Log-MAP algorithm with table look-up. When concatenated with an optimized low-density parity-check (LDPC) code, Log-MAP-tb b-MCMC can operate within 1.2-1.8 dB of the capacity of MIMO systems with 8 transmit/receive antennas at spectral efficiencies up to ¿ = 24 bits/channel use (b/ch). This result improves upon best performance achieved by turbo coded systems using list sphere decoding (LSD) detector by 2.3-3.8 dB, leading to nearly 50% reduction in the capacity gap. Detailed comparisons of the Log-MAP-tb b-MCMC with LSD based detectors demonstrate that MCMC detector is indeed the detector of choice for achieving channel capacity both in terms of performance and complexity.

## Interblock memory for turbo coding

- **Status**: ❌
- **Reason**: turbo coding의 interblock memory 기법, 비-LDPC 부호 전용으로 LDPC BP 이식 기법 없음
- **ID**: ieee:5407597
- **Type**: journal
- **Published**: February 2
- **Authors**: Chia-Jung Yeh, Yeong-Luh Ueng, Mao-Chao Lin +1
- **PDF**: https://ieeexplore.ieee.org/document/5407597
- **Abstract**: We investigate a binary code, which is implemented by serially concatenating a multiplexer, a multilevel delay processor, and a signal mapper to a binary turbo encoder. To achieve improved convergence behavior, we modify the binary code by passing only a fraction of the bits in the turbo code through the multilevel delay processor and the signal mapper. Two decoding methods are discussed and their performances are evaluated.

## An Iteratively Decodable Tensor Product Code with Application to Data Storage

- **Status**: ❌
- **Reason**: q-ary(비이진) LDPC 기반 텐서곱 EPCC — non-binary LDPC 제외
- **ID**: ieee:5402490
- **Type**: journal
- **Published**: February 2
- **Authors**: Hakim Alhussien, Jaekyun Moon
- **PDF**: https://ieeexplore.ieee.org/document/5402490
- **Abstract**: The error pattern correcting code (EPCC) can be constructed to provide a syndrome decoding table targeting the dominant error events of an inter-symbol interference channel at the output of the Viterbi detector. For the size of the syndrome table to be manageable and the list of possible error events to be reasonable in size, the codeword length of EPCC needs to be short enough. However, the rate of such a short length code will be too low for hard drive applications. To accommodate the required large redundancy, it is possible to record only a highly compressed function of the parity bits of EPCC's tensor product with a symbol correcting code. In this paper, we show that the proposed tensor error-pattern correcting code (T-EPCC) is linear time encodable and also devise a low-complexity soft iterative decoding algorithm for EPCC's tensor product with q-ary LDPC (T-EPCC-qLDPC). Simulation results show that T-EPCC-qLDPC achieves almost similar performance to single-level qLDPC with a 1/2 KB sector at 50% reduction in decoding complexity. Moreover, 1 KB T-EPCC-qLDPC surpasses the performance of 1/2 KB single-level qLDPC at the same decoder complexity.

## Iterative Soft Decision Feedback Zig-Zag Equalizer for 2D Intersymbol Interference Channels

- **Status**: ❌
- **Reason**: 2D ISI용 zig-zag 등화/검출기, LDPC 무관
- **ID**: ieee:5402483
- **Type**: journal
- **Published**: February 2
- **Authors**: Yiming Chen, Patrick Njeim, Taikun Cheng +2
- **PDF**: https://ieeexplore.ieee.org/document/5402483
- **Abstract**: We present a novel iterative soft decision feedback zig-zag algorithm for detection of binary images corrupted by two dimensional intersymbol interference and additive white Gaussian noise. The algorithm exchanges soft information between maximum-a-posteriori detectors employing different zigzag scan directions. Each detector exploits soft-decision feedback from the other zig-zag detectors. Simulation results for the 2 × 2 averaging mask channel show that, at low signal-to-noise ratios, the new algorithm gains about 1 dB over an iterative row column soft decision feedback algorithm and over a separable mask algorithm, two of the best previously published schemes. When the zig-zag algorithm is concatenated with the row-column algorithm, the concatenated system performs as well as or better than four of the best previously published algorithms, at both low and high signal-to-noise ratios, for a variety of 2 × 2 and 3 × 3 convolution masks; in several cases, the system performs within less than 0.1 dB of the maximum-likelihood performance bound.

## On the Photonic Implementation of Universal Quantum Gates, Bell States Preparation Circuit, Quantum Relay and Quantum LDPC Encoders and Decoders

- **Status**: ❌
- **Reason**: 양자 sparse-graph(qLDPC) 인코더/디코더 광학 구현, 양자 전용(entanglement-assisted, dual-containing)에 의존 → 양자 EC 제외
- **ID**: ieee:5409640
- **Type**: journal
- **Published**: Feb. 2010
- **Authors**: Ivan B. Djordjevic
- **PDF**: https://ieeexplore.ieee.org/document/5409640
- **Abstract**: We show that any family of universal quantum gates can be implemented based on a single optical hybrid/Mach-Zehnder interferometer (MZI)/directional coupler (DC) and either a highly nonlinear optical fiber or a tap coupler with an avalanche photodiode. We further show how to implement Pauli gates, which are needed in quantum error correction, using the same technology. The use of Bell states in quantum teleportation is essential. We also show how to implement the Bell states preparation circuit. To extend the transmission distance of quantum teleportation systems, the use of quantum relays is necessary. We show how to implement the quantum relay in integrated optics as well. We further study the implementation of encoders/decoders for sparse-graph quantum codes and show that the encoder/decoder for arbitrary quantum sparse-graph code can be implemented in integrated optics as well. We also study the performance of sparse-graph codes and demonstrate that entanglement-assisted sparse-graph codes from balanced incomplete block designs significantly outperform the corresponding dual-containing quantum codes. Finally, we provide several theorems that can be used in the design of entanglement-assisted (EA) quantum codes that require only one qubit to be shared between the source and the destination.

## Heredity as an Encoded Communication Process

- **Status**: ❌
- **Reason**: 유전체 정보이론/생물학 비유, LDPC ECC와 무관, 떼어낼 디코더·구성·HW 기법 없음
- **ID**: ieee:5420288
- **Type**: journal
- **Published**: Feb. 2010
- **Authors**: Gérard Battail
- **PDF**: https://ieeexplore.ieee.org/document/5420288
- **Abstract**: Heredity is relevant to information theory as a communication process. The conservation of genomes over intervals at the geological timescale and the existence of mutations at shorter intervals can be conciliated assuming that genomes possess intrinsic error-correction codes. The better conservation of old parts of genomes leads to assume that these codes are organized as a nested system set up during geological times, which protects a genomic message the better, the older it is. These hypotheses imply that: genomes are redundant, discrete species exist with a hierarchical taxonomy, successive generations are needed, evolution is contingent and saltationist; it trends towards increasing complexity. These consequences match features of the actual living world but their experimental confirmation needs a still lacking collaboration of biologists and information-theorists. It is suggested that genomic error-correcting codes could consist of ¿soft codes¿ where mutual dependence of symbols results from physical-chemical and linguistic constraints, not only mathematical equalities. The constraints incurred by DNA molecules moreover result in a nested structure. Guesses about genomic error-correcting codes are made.

## Impact of Network Coding on System Delay for Multisource–Multidestination Scenarios

- **Status**: ❌
- **Reason**: network coding의 시스템 지연 분석, convolutional code 사용, LDPC/ECC 이식 기법 없음
- **ID**: ieee:5299065
- **Type**: journal
- **Published**: Feb. 2010
- **Authors**: Zhiguo Ding, Zheng Ma, Kin K. Leung
- **PDF**: https://ieeexplore.ieee.org/document/5299065
- **Abstract**: Existing work has shown that random coding across multicast sessions can significantly reduce system delay. However, such a scheme requires the strong assumption that each source has priori information of other sources' messages. The broadcasting nature of radio propagation can provide an opportunity to realize collaboration across sessions without causing much system overhead. In this paper, we propose the application of network coding to multisource-multidestination (MSMD) scenarios and provide formal analysis for the improvement of system delay. In particular, two types of analytical results have been developed, with one based on the outage probability and the other based on the use of practical convolutional codes. Monte Carlo simulation results have also been provided to demonstrate the delay performance of the proposed network-coded protocol.

## Performance analysis of LDPC codes over WS-EWC coded optical CDMA networks

- **Status**: ❌
- **Reason**: OCDMA 네트워크 성능분석에 표준 QC-LDPC 단순 적용 - 새 기여 없는 표준 부호 재사용
- **ID**: ieee:5440369
- **Type**: conference
- **Published**: 7-10 Feb. 
- **Authors**: Chun-Ming Huang, Jen-Fa Huang, Chao-Chin Yang
- **PDF**: https://ieeexplore.ieee.org/document/5440369
- **Abstract**: One extended Welch-Costas (EWC) code family for the wavelength-division-multiplexing/spectral-amplitude coding (WDM/SAC; WS) optical code-division multiple-access (OCDMA) networks is proposed. This system has a superior performance as compared to the previous modified quadratic congruence (MQC) coded OCDMA networks. However, since the performance of such a network is unsatisfactory when the data bit rate is higher, one class of quasi-cyclic low-density parity-check (QC-LDPC) code is adopted to improve that. Simulation results show that the performance of the WS-EWC coded OCDMA network can be greatly improved by using the LDPC codes when data rate is 2.5 Gb/s.

## Density evolution-based analysis and design of LDPC codes with a priori information

- **Status**: ❌
- **Reason**: 다중접속 상관소스용 a priori 정보 활용 LDPC 설계/밀도진화 분석. 응용특이적이며 NAND ECC에 떼어낼 신규 디코더·구성 기법 없음
- **ID**: ieee:5454106
- **Type**: conference
- **Published**: 31 Jan.-5 
- **Authors**: M. Martalò, G. Ferrari, A. Abrardo +2
- **PDF**: https://ieeexplore.ieee.org/document/5454106
- **Abstract**: In this paper, we consider multiple access schemes with correlated sources, where a priori information, in terms of source correlation, is available at the access point (AP). In particular, we assume that each source uses a proper low-density parity-check (LDPC) code to transmit, through an additive white Gaussian noise (AWGN) channel, its information sequence to the AP. At the AP, the information sequences are recovered by an iterative decoder, with component decoders associated with the sources, which exploit the available a priori information. In order to analyze the behaviour of the considered multiple access coded system, we propose a density evolution-based approach, which allows to determine a signal-to-noise ratio (SNR) transfer chart and compute the system multi-dimensional SNR feasible region. The proposed technique, besides characterizing the performance of LDPC-coded multiple access scheme, is expedient to design optimized LDPC codes for this application.

## A factor-graph-based random walk, and its relevance for LP decoding analysis and Bethe entropy characterization

- **Status**: ❌
- **Reason**: LP 디코딩 성능분석·Bethe 엔트로피 특성화의 순수 이론(random walk/fundamental cone), 디코더·HW·구성으로 이어지지 않는 이론 bound
- **ID**: ieee:5454077
- **Type**: conference
- **Published**: 31 Jan.-5 
- **Authors**: Pascal O. Vontobel
- **PDF**: https://ieeexplore.ieee.org/document/5454077
- **Abstract**: Although min-sum algorithm (MSA) and linear programming (LP) decoding are tightly related, it is not straightforward to translate MSA decoding performance analysis techniques to the LP decoding setup. Towards closing this performance analysis techniques gap, Koetter and Vontobel [ITAW 2006] showed how the collection of messages from several MSA decoding iterations can be used to construct a dual witness for LP decoding, thereby deriving some performance results for LP decoding. In a recent breakthrough paper by Arora, Daskalakis, and Steurer (ADS) [STOC 2009], the understanding of the performance of LP decoding was brought to a new level, not only from the perspective of available analysis tools but also from the perspective of significantly improving the known asymptotic LP decoding threshold bounds. ADS achieved this by showing how MSA decoding analysis type results can be used in the primal domain of the LP decoder, along the way also giving evidence that the above detour over the dual domain is neither necessary nor simpler. In the present paper we focus on the geometrical aspects of the ADS paper and show that one of the key results of the ADS paper can be reformulated as the construction of a rather nontrivial class of supersets of the fundamental cone, where these supersets are convex cones that are generated by vectors that are derived from computation trees and minimal valid deviations therein. As we will discuss, the main ingredient that allows the verification of this superset construction is a certain class of backtrackless random walks on the code's normal factor graph. Moreover, formulating our results in terms of normal factor graphs will facilitate the generalization of the geometrical results of the ADS paper to setups with non-uniform node degrees, with other types of constraint function nodes, and with no restrictions on the girth. We conclude the paper by showing connections between the entropy rates of the above-mentioned random walks and the Bethe entropy function of the normal factor graph that these random walks are defined on.

## A soft information calculating method for SC-FDE output symbol

- **Status**: ❌
- **Reason**: SC-FDE 출력 soft information 계산법(무선 등화기 프론트엔드), LDPC는 SISO 디코더 베이스라인, 떼어낼 ECC 기법 없음
- **ID**: ieee:5451815
- **Type**: conference
- **Published**: 26-28 Feb.
- **Authors**: Dinggen Xu, Naiping Cheng, Hui Zhou
- **PDF**: https://ieeexplore.ieee.org/document/5451815
- **Abstract**: The hard decision symbol of conventional SC-FDE output is not perfect to the posterior SISO decoder of Shannon limit codes such as Turbo code and LDPC codes, which can achieve the Shannon limit performance on condition that the in-out information is soft. In this paper, a soft information calculation method for SC-FDE output symbol is proposed which increases the accuracy of information into the SISO decoder of Shannon limit codes and improves the transmission system. The numerical simulation results also show that the soft output SC-FDE gains an advantage over the hard one and the additional SNR gain can be obtained in frequency selective channel.

## An improved physical layer network coding scheme for two-way relay systems

- **Status**: ❌
- **Reason**: two-way relay 물리계층 네트워크코딩 JCNC 반복디코딩 — 네트워크코딩 응용 특이적, NAND 채널 ECC 비의존
- **ID**: ieee:5456460
- **Type**: conference
- **Published**: 23-24 Feb.
- **Authors**: Yidong Lang, Dirk Wübben, Karl-Dirk Kammeyer
- **PDF**: https://ieeexplore.ieee.org/document/5456460
- **Abstract**: In this paper we consider a two-way relaying system with two sources A, B and one relay R, where the two sources desire to exchange information through the relay. The transmission consists of two states: multiple access (MAC) stage, where A and B transmit the channel-coded signals to R simultaneously, and broadcast (BC) stage, where R transmits towards both A and B. One critical process at R is to decode the superimposed signal from A and B in such a way that A and B could decode the information from each other reliably at the BC stage. Instead of decoding the individual information belonging to A and B separately, R aims to decode the superimposed signal to the network-coded combination of the two source information, i.e., the binary XOR of the two source information. We refer this decoding process as the joint channel decoding and physical network encoding (JCNC). In this paper, a novel iterative decoding algorithm is presented for the physical network coding scheme, which is applicable to any linear channel code, e.g. Low-Density Parity-Check (LDPC) code. Furthermore, the two-way relaying scheme is extended to distributed multiple input multiple output (MIMO) multi-hop networks. Based on an antenna selection criterion within each virtual antenna array (VAA), the end-to-end (e2e) BER of the multi-hop system can be further reduced. Simulation results show that the proposed scheme outperforms other recently proposed network coding schemes with slightly increased complexity.

## Performance evaluation of iterative LDPC-coded MIMO OFDM system with time interleaving in mobile line-of-sight environments

- **Status**: ❌
- **Reason**: LDPC-MIMO-OFDM 무선 수신기(MMSE-SIC) 성능평가 — 통신응용 특이적, 떼어낼 디코더 기법 없음
- **ID**: ieee:5456383
- **Type**: conference
- **Published**: 23-24 Feb.
- **Authors**: Kazuhiko Mitsuyama, Kohei Kambara, Takayuki Nakagawa +2
- **PDF**: https://ieeexplore.ieee.org/document/5456383
- **Abstract**: Iterative low-density parity-check (LDPC) coded multiple-input multiple-output (MIMO) systems are known to be able to theoretically achieve excellent performance by computer simulation. If the systems can exploit time interleaving long enough to cover a fading cycle, excellent error rate performance should be obtained in mobile line-of-sight (LOS) environments. This paper describes an iterative LDPC minimum mean square error with soft interference cancellation (LDPC-MMSE-SIC) receiver with a time de-interleaver before the MMSE detector and evaluates it using channel state information (CSI) acquired in outdoor measurements. We show that the iterative receiver with time interleaving improves the error rate performance significantly in mobile LOS environments and outperforms an LDPC maximum likelihood detection (LDPC-MLD) receiver with the same error correction and interleaving.

## Improving low-delay MIMO-OFDM channel estimation

- **Status**: ❌
- **Reason**: MIMO-OFDM 채널추정 개선 — LDPC는 보조, ECC 신규 기법 없음
- **ID**: ieee:5456436
- **Type**: conference
- **Published**: 23-24 Feb.
- **Authors**: Patric Beinschob, Udo Zölzer
- **PDF**: https://ieeexplore.ieee.org/document/5456436
- **Abstract**: To overcome performance degradation in mobile multiple input multiple output (MIMO) orthogonal frequency-division multiplexing (OFDM) spatial multiplexing downlink systems an improved channel estimation algorithm is proposed. It yields channel estimates after every OFDM symbol reflecting time-variant channel behavior and provides data with approx. 4 bit/s/Hz for a 4×4 MIMO setup due to a decision directed scheme. Through the usage of short LDPC codes and employing a MIMO-OFDM symbol reconstruction method from the LDPC decoder output significant gains in estimation accuracy were realized in computer experiments even in high velocity scenarios. Simulation results based on 3GPP MIMO spatial channel model show the estimation accuracy for a range of velocities which are underlined by comparison of bit error rates with perfect channel state information and the channel estimation.

## Check splitting of root-check LDPC codes over ARQ block-fading channels

- **Status**: ❌
- **Reason**: ARQ block-fading 채널용 root-check LDPC check splitting incremental redundancy → 무선 fading/다이버시티 특이적, NAND ECC 이식 기법 없음
- **ID**: ieee:5426768
- **Type**: conference
- **Published**: 2-5 Feb. 2
- **Authors**: Sri Krishna Kambhampati, Gottfried Lechner, Terence Chan +1
- **PDF**: https://ieeexplore.ieee.org/document/5426768
- **Abstract**: In this paper we extend the concept of check splitting to root-check LDPC codes, thus providing an incremental redundancy code construction specifically for the ARQ block-fading channel. By construction, the proposed coding scheme achieves a high level of diversity and effectively adapts the transmission rate to the instantaneous channel conditions.
