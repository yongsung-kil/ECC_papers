# IEEE Xplore — 2008-12


## Performance analysis on LDPC-Coded systems over quasi-static (MIMO) fading channels

- **Status**: ❌
- **Reason**: MIMO 페이딩채널 LDPC 오류확률 상한 유도 순수 이론 bound, 떼어낼 디코더/HW/구성 기법 없음
- **ID**: ieee:4711172
- **Type**: journal
- **Published**: December 2
- **Authors**: Jingqiao Zhang, Heung-no Lee
- **PDF**: https://ieeexplore.ieee.org/document/4711172
- **Abstract**: In this paper, we derive closed form upper bounds on the error probability of low-density parity-check (LDPC) coded modulation schemes operating on quasi-static fading channels. The bounds are obtained from the so-called Fano-Gallager's tight bounding techniques, and can be readily calculated when the distance spectrum of the code is available. In deriving the bounds for multiple-input multiple-output (MIMO) systems, we assume the LDPC code is concatenated with the orthogonal space-time block code as an inner code. We obtain an equivalent single-input single-output (SISO) channel model for this concatenated coded-modulation system. The upper bounds derived here indicate good matches with simulation results of a complete transceiver system over Rayleigh and Rician MIMO fading channels in which the iterative detection and decoding algorithm is employed at the receiver.

## Nonbinary LDPC Coding for Multicarrier Underwater Acoustic Communication

- **Status**: ❌
- **Reason**: 비이진(nonbinary GF(q)) LDPC 구성, 바이너리 한정 기준에 따라 제외
- **ID**: ieee:4686807
- **Type**: journal
- **Published**: December 2
- **Authors**: Jie Huang, Shengli Zhou, Peter Willett
- **PDF**: https://ieeexplore.ieee.org/document/4686807
- **Abstract**: Recently, multicarrier modulation in the form of orthogonal frequency division multiplexing (OFDM) has been shown feasible for underwater acoustic communications via effective algorithms to handle the channel time-variability. In this paper, we propose to use nonbinary low density parity check (LDPC) codes to address two other main issues in OFDM: (i) plain (or uncoded) OFDM has poor performance in fading channels, and (ii) OFDM transmission has high peak to average power ratio (PAPR). We develop new methods to construct nonbinary regular and irregular LDPC codes that achieve excellent performance, match well with the underlying modulation, and can be encoded in linear time and in a parallel fashion. Based on the fact that the generator matrix of LDPC codes has high density, we further show how to reduce the PAPR considerably with minimal overhead. Experimental results confirm the excellent performance of the proposed nonbinary LDPC codes in multicarrier underwater acoustic communications.

## Iterative Carrier Frequency Offset and Channel Estimation for Underwater Acoustic OFDM Systems

- **Status**: ❌
- **Reason**: 수중음향 OFDM의 CFO/채널추정 반복수신기 응용, LDPC는 부수적이고 떼어낼 ECC 기법 없음
- **ID**: ieee:4686804
- **Type**: journal
- **Published**: December 2
- **Authors**: Taehyuk Kang, Ronald A. Iltis
- **PDF**: https://ieeexplore.ieee.org/document/4686804
- **Abstract**: This paper presents a practical low-density parity-check (LDPC) coded OFDM system designed for the underwater acoustic channel with its attendant sparse multipath channel and Doppler effects. The carrier frequency offset (CFO) and channel state information (CSI) are assumed unavailable to both to the transmitter and the receiver. Several different receiver structures are considered, all of which perform CFO/channel estimation, detection and decoding in an iterative manner. The convergence behavior of the iterative receivers and their asymptotic performance are evaluated using the extrinsic information transfer (EXIT) chart method. OFDM receiver performance is further evaluated through simulations and field tests in shallow water.

## Jointly gaussian approximation and multi-stage LLR combining in the iterative receiver for MIMO-BICM systems

- **Status**: ❌
- **Reason**: MIMO-BICM 수신기 다단 LLR 결합 알고리즘, 무선 검출 특이적이며 LDPC ECC 비의존
- **ID**: ieee:4723333
- **Type**: journal
- **Published**: December 2
- **Authors**: Tao Yang, Jinhong Yuan, Zhenning Shi
- **PDF**: https://ieeexplore.ieee.org/document/4723333
- **Abstract**: In this letter, we propose a new multi-stage LLR combining (MLC) algorithm in an iterative receiver for MIMOBICM systems. This algorithm combines the soft information from different receive antennas in a multi-stage fashion, where the combining factors are derived based on the joint likelihood function of bivariate Gaussian random variables. The variance transfer (VT) function of the proposed scheme is derived for performance analysis. For slow fading channels, we show that the proposed MLC algorithm can achieve almost the same performance as the linear minimum mean square error (LMMSE) filtering approach, whereas the computation-demanding matrix inverse for LMMSE can be avoided.

## Cooperation over frequency-selective fading relay channels

- **Status**: ❌
- **Reason**: 릴레이 채널 분산 turbo 코딩+협력 통신, LDPC ECC 기법 아님
- **ID**: ieee:4712725
- **Type**: journal
- **Published**: December 2
- **Authors**: Jun Hu, Tolga M. Duman
- **PDF**: https://ieeexplore.ieee.org/document/4712725
- **Abstract**: We study information-rate calculations and coded cooperation strategies for relay channels with frequency-selective (FS) fading. We develop suitable channel trellises for the multiaccess and broadcast parts of the relay channel, and employ simulation-based techniques to calculate (approximate) ergodic information-rate bounds with FS Rayleigh fading. Our results show that frequency selectivity provides higher information rates than flat fading when the fading coefficients are known at the receiver, however, the improvement becomes marginal with increasing number of channel taps (when the overall signal to noise ratio is kept constant). Furthermore, we develop a distributed turbo-coding strategy and several decode-and-forward type detection/decoding schemes to ensure successful cooperative communication where the source and the relay may transmit simultaneously. We show that with suitable coding and iterative decoding, one can approach the approximate information-rate limits closely, and that detection schemes based on MMSE criterion provide a good performance/complexity trade-off.

## Optimal erasure selection of M-ary PAM signaling for errors and erasures decoding algorithms

- **Status**: ❌
- **Reason**: M-ary PAM errors-and-erasures 디코딩의 erasure 선택 임계값 분석, 부호 비특이적이나 LDPC BP가 아닌 hard-decision/erasure 디코딩이라 이식 기법 없음
- **ID**: ieee:4711171
- **Type**: journal
- **Published**: December 2
- **Authors**: Yeong-hyeon Kwon, Mi-kyung Oh, Dong-jo Park
- **PDF**: https://ieeexplore.ieee.org/document/4711171
- **Abstract**: Erasure selection for errors-and-erasures decoding algorithms is investigated and analyzed, where declaring erasures provides additional gain for hard decision decoding. To derive an analytical criterion for optimal erasure selection, we first investigate erasure effects on decoding performance, by which a metric function for erasure selection is derived. From the derived metric, a suboptimal threshold is defined, which can be used for errors and erasures decoding of large code-distance channel codes. Moreover, application to M-ary (M>2) PAM constellation is also described. For verification of the proposed erasure threshold, simulation results with popular channel codes are included.

## Maxwell Construction: The Hidden Bridge Between Iterative and Maximum a Posteriori Decoding

- **Status**: ❌
- **Reason**: BEC에서 BP-MAP 관계 Maxwell 디코더 순수 이론, 떼어낼 실용 디코더/HW/구성 없음
- **ID**: ieee:4675720
- **Type**: journal
- **Published**: Dec. 2008
- **Authors**: Cyril Measson, Andrea Montanari, RÜdiger Urbanke
- **PDF**: https://ieeexplore.ieee.org/document/4675720
- **Abstract**: There is a fundamental relationship between belief propagation and maximum a posteriori decoding. A decoding algorithm, which is called the Maxwell decoder, is introduced and provides a constructive description of this relationship. Both the algorithm itself and the analysis of the new decoder are reminiscent of the Maxwell construction in thermodynamics. This paper investigates in detail the case of transmission over the binary erasure channel, while the extension to general binary memoryless channels is discussed in a companion paper.

## Scalable Joint Source-Channel Coding for the Scalable Extension of H.264/AVC

- **Status**: ❌
- **Reason**: SVC 비디오 JSCC, LDPC가 베이스라인 채널보호일 뿐 떼어낼 ECC 기법 없음
- **ID**: ieee:4625977
- **Type**: journal
- **Published**: Dec. 2008
- **Authors**: Maryse Stoufs, Adrian Munteanu, Jan Cornelis +1
- **PDF**: https://ieeexplore.ieee.org/document/4625977
- **Abstract**: This paper proposes a novel joint source-channel coding (JSCC) methodology which minimizes the end-to-end distortion for the transmission over packet loss channels of scalable video encoded using SVC, the scalable extension of H.264/AVC. The proposed JSCC approach performs channel protection using low-density parity-check codes and relies on Lagrangian-based optimization techniques to derive the appropriate protection levels for each layer produced by the scalable source codec. Our JSCC approach for SVC can support spatial, temporal and quality scalability and can provide an optimized channel protection in any scalable setting. Experiments show that our JSCC methodology yields competitive results against state-of-the-art Lagrangian-based JSCC algorithms. Compared to the state-of-the-art, our approach significantly reduces the number of computations needed to derive the rate-distortion hulls. Moreover, the proposed approach constructs convex rate-distortion hulls for each frame, irrespective of the target rate. This allows the pre-computation of the convex rate-distortion hulls for typical packet loss channels, such that the extraction of a near-optimal JSCC allocation can be achieved on-the-fly for any target rate or packet-loss rate. We conclude that the proposed JSCC methodology provides optimized resilience against transmission errors in scalable video streaming over variable-bandwidth error-prone channels.

## Theoretical and Practical Boundaries of Binary Secure Sketches

- **Status**: ❌
- **Reason**: 바이오메트릭 fuzzy commitment(보안), 표준 product code+min-sum 재사용, 신규 LDPC 기여 없음
- **ID**: ieee:4668358
- **Type**: journal
- **Published**: Dec. 2008
- **Authors**: Julien Bringer, HervÉ Chabanne, Gerard Cohen +2
- **PDF**: https://ieeexplore.ieee.org/document/4668358
- **Abstract**: Fuzzy commitment schemes, introduced as a link between biometrics and cryptography, are a way to handle biometric data matching as an error-correction issue. We focus here on finding the best error-correcting code with respect to a given database of biometric data. We propose a method that models discrepancies between biometric measurements as an erasure and error channel, and we estimate its capacity. We then show that two-dimensional iterative min-sum decoding of properly chosen product codes almost reaches the capacity of this channel. This leads to practical fuzzy commitment schemes that are close to theoretical limits. We test our techniques on public iris and fingerprint databases and validate our findings.

## A Joint Source-Channel Video Coding Scheme Based on Distributed Source Coding

- **Status**: ❌
- **Reason**: 분산소스코딩 기반 결합소스-채널 비디오 코딩(JSCC) - LDPC가 베이스라인, 떼어낼 ECC 기법 없음
- **ID**: ieee:4694848
- **Type**: journal
- **Published**: Dec. 2008
- **Authors**: Yixuan Zhang, Ce Zhu, Kim-Hui Yap
- **PDF**: https://ieeexplore.ieee.org/document/4694848
- **Abstract**: Recently, several error resilient schemes have been proposed to tackle the error propagation problem in the motion-compensated predictive video coding based on a promising technique - distributed source coding (DSC). However, these schemes mainly apply the distributed source codes for channel error correction, while under-utilizing their capability for data compression. A channel-aware joint source-channel video coding scheme based on DSC is proposed to eliminate the error propagation problem in predictive video coding in a more efficient way. It is known that near Slepian-Wolf bound DSC is achieved using powerful channel codes, assuming the source and its reference (also known as side-information) are connected by a virtual error-prone channel. In the proposed scheme, the virtual and real error-prone channels are fused so that a unified single channel code is applied to encode the current frame thus accomplishing a joint source-channel coding. Our analysis of the rate efficiency in recovering error propagation shows that the joint scheme can achieve a lower rate compared with performing source and channel coding separately. Simulation results show that the number of bits used for recovering from error propagation can be reduced by up to 10% using the proposed scheme compared to Sehgal-Jagmohan-Ahuja's DSC-based error resilient scheme.

## Toward Compression of Encrypted Images and Video Sequences

- **Status**: ❌
- **Reason**: 암호화 이미지/비디오 압축(분산 소스코딩), 채널 ECC 아님
- **ID**: ieee:4668361
- **Type**: journal
- **Published**: Dec. 2008
- **Authors**: Daniel Schonberg, Stark C. Draper, Chuohao Yeo +1
- **PDF**: https://ieeexplore.ieee.org/document/4668361
- **Abstract**: We present a framework for compressing encrypted media, such as images and videos. Encryption masks the source, rendering traditional compression algorithms ineffective. By conceiving of the problem as one of distributed source coding, it has been shown in prior work that encrypted data are as compressible as unencrypted data. However, there are two major challenges to realize these theoretical results. The first is the development of models that capture the underlying statistical structure and are compatible with our framework. The second is that since the source is masked by encryption, the compressor does not know what rate to target. We tackle these issues in this paper. We first develop statistical models for images before extending it to videos, where our techniques really gain traction. As an illustration, we compare our results to a state-of-the-art motion-compensated lossless video encoder that requires unencrypted video input. The latter compresses each unencrypted frame of the ldquoForemanrdquo test sequence by 59% on average. In comparison, our proof-of-concept implementation, working on encrypted data, compresses the same sequence by 33%. Next, we develop and present an adaptive protocol for universal compression and show that it converges to the entropy rate. Finally, we demonstrate a complete implementation for encrypted video.

## Soft network coding in wireless two-way relay channels

- **Status**: ❌
- **Reason**: 무선 양방향 중계 소프트 네트워크 코딩 - LDPC 무관, 떼어낼 ECC 기법 없음
- **ID**: ieee:6389853
- **Type**: journal
- **Published**: Dec. 2008
- **Authors**: Shengli Zhang, Yu Zhu, Soung Chang Liew
- **PDF**: https://ieeexplore.ieee.org/document/6389853
- **Abstract**: Application of network coding in wireless two-way relay channels (TWRC) has received much attention recently because its ability to improve throughput significantly. In traditional designs, network coding operates at upper layers above (including) the link layer and it requires the input packets to be correctly decoded. However, this requirement may limit the performance and application of network coding due to the unavoidable fading and noise in wireless networks. In this paper, we propose a new wireless network coding scheme for TWRC, which is referred to as soft network coding (SoftNC), where the relay nodes applies symbol-by-symbol soft decisions on the received signals from the two end nodes to come up with the network coded information to be forwarded. We do not assume further channel coding on top of SoftNC at the relay node (channel coding is assumed at the end nodes). According to measures of the soft information adopted, two kinds of SoftNC are proposed: amplify-and-forward SoftNC (AF-SoftNC) and soft-bit-forward SoftNC (SBF-SoftNC). We analyze the both the ergodic capacity and the outage capacity of the two SoftNC schemes. Specifically, analytical form approximations of the ergodic capacity and the outage capacity of the two schemes are given and validated. Numerical simulation shows that our SoftNC schemes can outperform the traditional network coding based two-way relay protocol, where channel decoding and re-encoding are used at the relay node. Notable is the fact that performance improvement is achieved using only simple symbol-level operations at the relay node.

## Universal Multiterminal Source Coding Algorithms With Asymptotically Zero Feedback: Fixed Database Case

- **Status**: ❌
- **Reason**: 유니버설 멀티터미널 소스 코딩(피드백 압축) - 채널 ECC가 아닌 소스 코딩, 떼어낼 LDPC 기법 없음
- **ID**: ieee:4675724
- **Type**: journal
- **Published**: Dec. 2008
- **Authors**: En-hui Yang, Da-Ke He, Tomohiko Uyematsu +1
- **PDF**: https://ieeexplore.ieee.org/document/4675724
- **Abstract**: Consider a source network in which a finite alphabet source X = {Xi}i=0 infin is to be encoded and transmitted, and another finite alphabet source Y = {Xi}i=0 infin correlated with X is available only to the decoder as side information. Traditionally, the channel between the encoder and decoder in the source network is assumed to be one-way. This, together with the fact that the encoder does not have access to Y, implies that the encoder has to know the achievable rates before encoding. In this paper, we consider universal source coding for a feedback source network in which the channel between the encoder and decoder is two-way and asymmetric. Assume that the encoder and decoder share a random database that is independent of both X and Y. A string matching-based (variable-rate) block coding algorithm with simple progressive encoding and joint typicality decoding is first proposed for the feedback source network. The simple progressive encoder does not need to know the achievable rates at the beginning of encoding. It is proven that for any (X, Y) in a large class of sources satisfying some mixing conditions, the average number of bits per letter transmitted from the encoder to the decoder (compression rate) goes to the conditional entropy H(X | Y) of X given Y asymptotically, and at the same time the average number of bits per letter transmitted from the decoder to the encoder (feedback rate) goes to 0 asymptotically. The algorithm and the corresponding analysis results are then extended to the case where both X and Y are to be encoded separately, but decoded jointly. Finally, a universal decoding algorithm is proposed to replace the joint typicality decoding, and the resulting universal compression algorithm consisting of the simple progressive encoder and the universal decoding algorithm is further shown to be asymptotically optimal for the class of all jointly memoryless source-side information pairs (X,Y).

## EXIT-Chart Optimized Block Codes for Wireless Video Telephony

- **Status**: ❌
- **Reason**: 무선 비디오용 EXIT 최적화 블록부호(ECOBC)+turbo검출, GLDPC는 부수 언급 - 비-LDPC 부호이며 떼어낼 LDPC ECC 기법 없음
- **ID**: ieee:4675856
- **Type**: journal
- **Published**: Dec. 2008
- **Authors**: Anh Quang Pham, Lie Liang Yang, Noor Samsiah Othman +1
- **PDF**: https://ieeexplore.ieee.org/document/4675856
- **Abstract**: In this paper we investigate a turbo detection scheme designed for robust video transmission over an uncorrelated Rayleigh fading channel. We first introduce a novel block error-correcting code, referred to as an extrinsic information transfer (EXIT)-chart optimized block code (ECOBC), which benefits from soft decision decoding. The ECOBC exploits both the residual redundancy which manifests itself in terms of the non-uniform probability distribution of K-bit strings inherent in the video encoded bit-stream, as well as the intentional redundancy imposed by the ECOBC for mitigating the effects of transmission errors. As our first novel contribution, we address the design of ECOBCs by formulating the necessary and sufficient condition, which ensures that the EXIT function of the softbit ECOBC decoder reaches the (1,1) point in the EXIT chart. Secondly, we propose a novel real-valued free-distance metric for characterizing the ECOBC's performance. Furthermore, the attainable performance and the computational complexity imposed by the ECOBC are investigated. The effects of the interleaver delay on the ECOBC's performance are also quantified. As an additional result, we demonstrate that at a fixed system bandwidth, the turbo detection scheme using the H.264 video codec with the error concealment tools disabled but amalgamated with the proposed ECOBC as well as an additional generalized low-density parity-check (GLDPC) code may lead to an approximately 2.5 dB signal-to-noise ratio gain in comparison to the benchmarker having the same total bit rate, which operated the H.264 scheme with the error concealment tools enabled hence resulting in a higher video rate and amalgamated with the same-rate GLDPC code, but dispensing with our novel ECOBC.

## Three-edge type LDPC code ensembles with exponentially few codewords with linear small weight

- **Status**: ❌
- **Reason**: multi-edge type LDPC 앙상블의 최소거리/저중량 codeword 존재조건 이론 분석. 새 디코더/HW/구체 구성 없는 순수 앙상블 이론 → 제외
- **ID**: ieee:4895505
- **Type**: conference
- **Published**: 7-10 Dec. 
- **Authors**: Tomoharu Awano, Kenta Kasai, Tomoharu Shibuya +1
- **PDF**: https://ieeexplore.ieee.org/document/4895505
- **Abstract**: Multi-edge type LDPC codes are introduced by Richardson and Urbanke, and they show examples of their ensembles have better performance than other known ensembles. Orlitsky et al. derived the condition for irregular LDPC code ensembles with minimum distance linearly increasing in code length. Nakasendo et al. derived the condition that code ensembles have exponentially decreasing small linear weight codewords for two-edge type LDPC code ensembles which is simple example of multi-edge type LDPC code ensembles. In this paper, we derive the condition for three-edge type LDPC code ensembles whose edge-types does not share any variable node and does share all of the check nodes with exponentially decreasing small linear weight codewords. The condition is necessary for the existence of the average relative minimum distance of ensembles. Our method is expected to derive the condition for multi-edge type LDPC codes.

## Design of low-density parity-check codes for multi-input multi-output systems

- **Status**: ❌
- **Reason**: MIMO용 비정칙 LDPC를 EXIT chart로 설계—무선 검출기 결합 특이적, NAND에 이식할 신규 코드설계 기여 없음
- **ID**: ieee:4895553
- **Type**: conference
- **Published**: 7-10 Dec. 
- **Authors**: Jeong Hwan Shin, Jin Young Kim, Jun Heo
- **PDF**: https://ieeexplore.ieee.org/document/4895553
- **Abstract**: In previous works, density evolution schemes have been used to design an irregular low-density parity-check (LDPC) code for the multi-input multi-output (MIMO) systems. However the code design based on the density evolution can be used only for simple code structure like LDPC codes and repeat-accumulate (RA) codes. Recently simple and accurate irregular LDPC code design method based on the extrinsic information transfer (EXIT) chart was introduced for an AWGN channel. This code design scheme is much flexible, therefore it can be used for any kind of code structure like turbo codes. In this paper we design an irregular LDPC code for a MIMO system using the EXIT chart based scheme. The EXIT charts are used to obtain the optimal edge degree distribution of the irregular LDPC code combined with the MMSE-SIC MIMO detector. This scheme can be generalized for designing the optimal iterative MIMO detector combined with any kind of channel codes including turbo codes.

## Burst detection by parity check matrix of LDPC code for perpendicular magnetic recording using bit-patterned medium

- **Status**: ❌
- **Reason**: 자기기록(BPM) 채널의 burst 검출 스킴; 채널 특이적 검출기로 이식 가능한 일반 LDPC 디코더/코드설계 기법 없음
- **ID**: ieee:4895390
- **Type**: conference
- **Published**: 7-10 Dec. 
- **Authors**: Y. Nakamura, Y. Okamoto, H. Osawa +2
- **PDF**: https://ieeexplore.ieee.org/document/4895390
- **Abstract**: In this paper, a burst detection scheme using a parity check matrix of LDPC code is described for the perpendicular magnetic recording using a bit-pattered medium. It is assumed that the burst-like bit-flipping occurs due to missing the write synchronization. The phenomenon cannot be detected as a signal decay and significantly degrades the performance of the LDPC coding and iterative decoding system. Therefore, a good alternative detector is required in order to keep the performance. The LDPC coding and iterative decoding system is evaluated by the computer simulation in a perpendicular magnetic recording channel using a bit-patterned medium with the burst-like bit-flipping. It is clarified that the LDPC coding and iterative decoding system with a burst detector has the resistance to a burst-like bit-flipping of 200 bits.

## Weight distribution of non-binary LDPC codes

- **Status**: ❌
- **Reason**: 비이진(non-binary GF(q)) LDPC의 weight distribution 분석. 비이진 LDPC는 명시적 제외 대상 → 제외
- **ID**: ieee:4895508
- **Type**: conference
- **Published**: 7-10 Dec. 
- **Authors**: Kenta Kasai, Charly Poulliat, David Declercq +2
- **PDF**: https://ieeexplore.ieee.org/document/4895508
- **Abstract**: Weight distributions of binary low-density parity-check (LDPC) codes are well studied. We investigate the average distributions of symbol and binary weight for non-binary LDPC code ensemble. We derive the asymptotic growth rate and its linear approximation for small weight. Moreover, we show the typical minimum distance does not monotonically increase with the size of the field where the codes are defined.

## Lossy source coding algorithm using lossless multi-terminal source codes

- **Status**: ❌
- **Reason**: lossy source coding 알고리즘(소스코딩); 채널코딩 ECC가 아니며 떼어낼 LDPC 디코더/구성 기법 없음
- **ID**: ieee:4895482
- **Type**: conference
- **Published**: 7-10 Dec. 
- **Authors**: Jun Muramatsu, Sigeki Miyake
- **PDF**: https://ieeexplore.ieee.org/document/4895482
- **Abstract**: A lossy source coding algorithm is presented that employs lossless multi-terminal source codes. By using nearly optimal lossless multi-terminal source codes, the proposed algorithm achieves the rate-distortion limit. The construction of lossless multi-terminal source codes, which are needed for the lossy source coding algorithm, can be realized by using sparse matrices, known as Low Density Parity Check (LDPC) matrices, or Turbo codes, and practically efficient decoding algorithms such as the Belief Propagation (BP) algorithm and the Linear Codes Linear Program (LCLP) algorithm.

## Modified min-sum algorithm with threshold filtering for nonbinary LDPC codes over GF(q)

- **Status**: ❌
- **Reason**: GF(q) 비이진 LDPC용 min-sum 복잡도 절감 기법. 비이진 LDPC 전용(configuration set filtering)으로 제외 대상 → 제외
- **ID**: ieee:4895537
- **Type**: conference
- **Published**: 7-10 Dec. 
- **Authors**: Yue Liu, Jun Ning, Jinhong Yuan
- **PDF**: https://ieeexplore.ieee.org/document/4895537
- **Abstract**: In this paper, we propose a scheme to reduce the computation complexity of min-sum (MS) algorithm for decoding of nonbinary low-density parity-check (LDPC) codes over GF(q). Previously, MS algorithm reduced the decoding complexity by lowering the size of the configuration set for each variable node through a sorting. In the proposed scheme, we modify the MS algorithm by minimizing the size of the configuration set for each variable node through a filtering. In the filtering, the reduction of the set size can be controlled by a preset threshold. This way we can reduce the complexity more efficiently. Simulation results show, compared to the previous EMS algorithm, the complexity of proposed scheme is reduced with a negligible degradation in the code performance.

## A study on a key establishment scheme with QC LDPC codes and UH-protocols

- **Status**: ❌
- **Reason**: QC-LDPC를 쓴 키 설정/프라이버시 증폭(보안·QKD 정보조정류); 채널 ECC가 아니고 떼어낼 디코더/HW 기법 없음
- **ID**: ieee:4895466
- **Type**: conference
- **Published**: 7-10 Dec. 
- **Authors**: Yuto Matsunaga, Manabu Hagiwara, Kazukuni Kobara +1
- **PDF**: https://ieeexplore.ieee.org/document/4895466
- **Abstract**: In this paper, we study a key establishment scheme with quasi-cyclic (QC) low-density parity-check (LDPC) codes and universal hushing (UH) protocols. We show probabilities that different keys are shared by our error-correction and a privacy amplification scheme for a given key distribution scheme, and we propose a permutation technique that the probability becomes lower.

## Kovalenko's full-rank limit and overheads as lower bounds of error-performances of LDPC and LT codes over binary erasure channels

- **Status**: ❌
- **Reason**: BEC상 ML 디코딩 성능의 확률적 하한(bound) 이론. 디코더/HW/구성으로 안 이어지는 순수 이론 bound이며 BEC/LT코드 대상 → 제외
- **ID**: ieee:4895488
- **Type**: conference
- **Published**: 7-10 Dec. 
- **Authors**: Ki-Moon Lee, Hayder Radha, Beom-Jin Kim +1
- **PDF**: https://ieeexplore.ieee.org/document/4895488
- **Abstract**: We present Kovalenko's full-rank limit as a tight probabilistic lower bound for error performances of LDPC codes and LT codes over BEC. From the limit, we derive a full-rank overhead as a tight lower-bound for stable overheads for successful maximum-likelihood decoding of the codes.

## LLR metrics for LDPC codes with quadrature differential PSK transmission, and their performances

- **Status**: ❌
- **Reason**: noncoherent QDPSK 채널 전용 LLR metric 유도; 무선/변조 응용 특이적이고 NAND LDPC에 떼어낼 디코더/HW/코드설계 기여 없음
- **ID**: ieee:4895388
- **Type**: conference
- **Published**: 7-10 Dec. 
- **Authors**: Elisa Mo, Pooi Yuen Kam, Marc A. Armand
- **PDF**: https://ieeexplore.ieee.org/document/4895388
- **Abstract**: Iterative decoding of low-density parity-check codes transmitted over noncoherent channels using quadrature differential phase-shift keying is investigated. The log-likelihood ratio for each of the two code bits sent over one transmission period, based on the joint probability of two consecutive received signal samples pertaining to these code bits, is derived. An approximation of this metric yields a less complex metric with negligible performance loss. Applications of these metrics to the decoding of binary and mixed alphabet LDPC codes are considered. In addition, performances of these metrics in the presence of signal-to-noise ratio estimation error are also studied.

## Information interflow network (I2N) using LDPC codes

- **Status**: ❌
- **Reason**: 멀티홉 무선망 throughput용 LDPC 활용(I2N). LDPC가 부수적 적용, 떼어낼 ECC 디코더/구성 기법 없는 통신 응용 → 제외
- **ID**: ieee:4895511
- **Type**: conference
- **Published**: 7-10 Dec. 
- **Authors**: Yugo Haruta, Koji Ishibashi, Tadahiro Wada
- **PDF**: https://ieeexplore.ieee.org/document/4895511
- **Abstract**: Recently, multihop wireless networks have gained much attraction. Since the available bandwidth and battery are strictly limited, multihop wireless networks should communicate efficiently. If the error correcting code is used, by using the longer codeword, the decoding error probability can be improved. Therefore, in this paper, we propose the information interflow network (I2N), which transmits several data packets as one longer data packet and show that the proposed network with lowdensity parity check (LDPC) codes can improve the throughput performance compared with the conventional network.

## An efficient design of irregular LDPC codes using beta approximation for the Gilbert-Elliott channel

- **Status**: ❌
- **Reason**: GE 채널용 비정칙 LDPC 밀도진화 근사 설계—무선 Markov채널 특이적 설계법, NAND 고전채널에 떼어낼 구성 기법 없음
- **ID**: ieee:4895649
- **Type**: conference
- **Published**: 7-10 Dec. 
- **Authors**: Manabu Kobayashi, Hideki Yagi, Toshiyasu Matsushima +1
- **PDF**: https://ieeexplore.ieee.org/document/4895649
- **Abstract**: In this paper, we investigate the design of low-density parity-check (LDPC) codes for the Gilbert-Elliott (GE) channel. Recently, Eckford et al. proposed a design method of irregular LDPC codes using approximate density-evolution (DE) for Markov channels [7]. In the design method proposed by Eckford et al., the probability density function (PDF) of the messages from variable nodes to check nodes is approximated by the Gaussian distribution. In this paper, we first show the method to obtain the accurate PDF of the messages from variable nodes to check nodes by utilizing two DE steps for the Gaussian distribution. We call this method the iterative density approximation (IDA). Using this method, we can design the good LDPC codes. Next, we propose an efficient design method of irregular LDPC codes by using Beta approximation to the PDF of the channel state probability for the GE channel. Consequently, we show that the complexity to calculate PDFs of the channel messages is considerably reduced though the rates of LDPC codes obtained by using the proposed approximation are almost the same as that of the IDA method.

## Computation of zeta functions counting pseudo-codewords of linear codes

- **Status**: ❌
- **Reason**: 선형부호 pseudo-codeword 세는 zeta function 계산. 순수 조합/이론, 디코더·HW·구성으로 이어지지 않음 → 제외
- **ID**: ieee:4895507
- **Type**: conference
- **Published**: 7-10 Dec. 
- **Authors**: Shuzo Matsuda, Seiken Saito, Toyokazu Hiramatsu
- **PDF**: https://ieeexplore.ieee.org/document/4895507
- **Abstract**: It is described in this document how to compute zeta functions counting unscaled pseudo-codewords of general binary linear codes. This zeta functions are introduced in [2] for cycle codes and extended in [3] for general linear codes. Especially, we show that the zeta functions of codes are computed by using a 1/2 size determinants compared to those of [3] for non-cycle codes.

## An application of linear codes to Slepian-Wolf coding of individual sequences

- **Status**: ❌
- **Reason**: Slepian-Wolf 소스코딩(분산 소스압축)으로 LDPC 사용, 채널 ECC 아닌 소스코딩이라 제외
- **ID**: ieee:4895662
- **Type**: conference
- **Published**: 7-10 Dec. 
- **Authors**: Shigeaki Kuzuoka
- **PDF**: https://ieeexplore.ieee.org/document/4895662
- **Abstract**: This paper clarifies the adequacy of the linear channel coding approach for the Slepian-Wolf coding of individual sequences. Our result reveals that LDPC code ensembles give optimal code for the Slepian-Wolf coding of individual sequences.

## Iterative decoding of BDPSK modulated LDPC codes using two-symbol-interval observations

- **Status**: ❌
- **Reason**: BDPSK Rayleigh 페이딩 LDPC LLR 메트릭 유도—무선 변조/채널 특이적, NAND에 이식 불가
- **ID**: ieee:4895598
- **Type**: conference
- **Published**: 7-10 Dec. 
- **Authors**: Vu Thanh Nam, Pooi Yuen Kam, Yan Xin
- **PDF**: https://ieeexplore.ieee.org/document/4895598
- **Abstract**: This paper studies the detection and decoding of LDPC encoded, interleaved, BDPSK-modulated symbols on the correlated flat Rayleigh fading channel using two-symbol-interval observations. The log-likelihood metric is derived for sum-product decoders. For each hypothesized code bit, the metric depends on two consecutive received signals and only on two other variables: the received SNR per bit and the fade rate. We simulate the performance of the system with this metric, and compare it with that of other metrics that do not take into account the fade rate. Numerical results are given for different codes. In practice, the fade rate may not be precisely known at the receiver, so we also examine how the system performance is affected if the actual fade rate differs from the assumed fade rate.

## Bounds on error probability of block codes with bounded-angle maximum-likelihood incomplete decoding

- **Status**: ❌
- **Reason**: 일반 블록부호의 BA-ML 불완전 디코딩 오류확률 상한(순수 이론 bound); 디코더/HW/구성으로 안 이어짐
- **ID**: ieee:4895487
- **Type**: conference
- **Published**: 7-10 Dec. 
- **Authors**: Sam Dolinar, Kenneth Andrews, Fabrizio Pollara +1
- **PDF**: https://ieeexplore.ieee.org/document/4895487
- **Abstract**: Recently, Dolinar et al. obtained extremely tight bounds on the probabilities of decoding error and undetected error for block codes using bounded-angle maximum-likelihood (BA-ML) incomplete decoding. Unfortunately, these bounds are complex and difficult to compute for large block sizes. In this paper we obtain simple exponential upper bounds on both the word error probability and the undetected error probability of block codes using BA-ML decoding.

## Achieving near-capacity on large discrete memoryless channels with uniform distributed selected input

- **Status**: ❌
- **Reason**: DMC 입력집합 축소로 용량 접근—코딩이론 입력설계, 떼어낼 LDPC 디코더/HW/구성 없음
- **ID**: ieee:4895582
- **Type**: conference
- **Published**: 7-10 Dec. 
- **Authors**: Amine Mezghani, Michel T. Ivrlac, Josef A. Nossek
- **PDF**: https://ieeexplore.ieee.org/document/4895582
- **Abstract**: We propose a method to increase the capacity achieved by uniform prior in discrete memoryless channels (DMC) with high input cardinality. It consists in appropriately reducing the input set. Different design criteria of the input subset are discussed. We develop an efficient algorithm to solve this problem based on the maximization of the cut-off rate. The method is applied to a mono-bit transceiver MIMO system, and it is shown that the capacity can be approached within tenths of a dB by employing standard binary codes while avoiding the use of distribution shapers.

## APP decoding of non-binary block codes on Gilbert-Elliott channels using generalized weight polynomials

- **Status**: ❌
- **Reason**: 비이진 블록부호 GEC APP 디코딩—비이진+비-LDPC, 제외 대상
- **ID**: ieee:4895567
- **Type**: conference
- **Published**: 7-10 Dec. 
- **Authors**: Wayne Griffiths, Hans-Jurgen Zepernick, Manora Caldera
- **PDF**: https://ieeexplore.ieee.org/document/4895567
- **Abstract**: In this paper, we present an a posteriori probability (APP) decoding algorithm for non-binary block codes on non-binary Gilbert-Elliott channels (GECs) using generalized weight polynomials. The proposed approach is based on a single-sweep APP decoding technique that utilizes matrix multiplications. By fixing the crossover probability in the ‘bad’ state of the non-binary GEC such that for a given transmitted symbol, all symbols are equally likely to be received, an APP decoding decision can efficiently be reached by evaluating trivariate polynomials. In this case, the non-binary GEC is described by three variables that are referred to as the average fade to connection time ratio, the burst factor, and the channel reliability factor. The application of the generalized weight polynomial approach is demonstrated with respect to numerical performance results obtained for simple non-binary block codes from computer simulations.

## Typical performance of irregular LDGM codes for lossy compression

- **Status**: ❌
- **Reason**: lossy compression용 LDGM 부호 성능을 replica method로 분석; 소스코딩+순수이론으로 채널 ECC 디코더/HW/구성 기여 없음
- **ID**: ieee:4895480
- **Type**: conference
- **Published**: 7-10 Dec. 
- **Authors**: Kazushi Mimura
- **PDF**: https://ieeexplore.ieee.org/document/4895480
- **Abstract**: We evaluate typical performance of irregular low-density generator-matrix (LDGM) codes, which is defined by sparse matrices with arbitrary irregular bit degree distribution and arbitrary check degree distribution, for lossy compression. We apply the replica method under one-step replica symmetry breaking (1RSB) ansatz to this problem.

## Joint channel decoding of spatially and temporally correlated data in wireless sensor networks

- **Status**: ❌
- **Reason**: WSN 공간/시간 상관 turbo 결합 디코딩—LDPC 비의존, 떼어낼 바이너리 LDPC BP 기법 없음
- **ID**: ieee:4895540
- **Type**: conference
- **Published**: 7-10 Dec. 
- **Authors**: Kentaro Kobayashi, Takaya Yamazato, Hiraku Okada +1
- **PDF**: https://ieeexplore.ieee.org/document/4895540
- **Abstract**: In densely deployed wireless sensor networks, sensor observations are spatially correlated. Furthermore, the nature of physical phenomena constitutes a temporal correlation between transmitted observations of an individual sensor node. In this paper, we propose a joint iterative channel decoding scheme using turbo codes. The proposed decoder exploits the spatial and temporal correlations of two binary data sequences to achieve additional coding gain. Simultaneously exploiting the spatial and temporal correlation, the proposed decoder achieves large performance gain.

## An unconditionally secure protocol based on lattices over the Gaussian channel

- **Status**: ❌
- **Reason**: 격자 기반 oblivious transfer 보안 프로토콜—보안+비-LDPC, 제외
- **ID**: ieee:4895618
- **Type**: conference
- **Published**: 7-10 Dec. 
- **Authors**: Motohiko Isaka
- **PDF**: https://ieeexplore.ieee.org/document/4895618
- **Abstract**: We propose to achieve an information theoretically secure oblivious transfer using lattice partitions based on the additive white Gaussian noise channel. A protocol is presented and the security and efficiency is discussed.

## A reliable soft-output of autoregressive ML detector for perpendicular magnetic recording with intertrack interference

- **Status**: ❌
- **Reason**: ARML 검출기(ITI 대응) 제안; LDPC 부호와 무관한 자기기록 채널 검출기로 떼어낼 ECC 기법 없음
- **ID**: ieee:4895392
- **Type**: conference
- **Published**: 7-10 Dec. 
- **Authors**: Kohsuke Harada, Hironori Uchikawa
- **PDF**: https://ieeexplore.ieee.org/document/4895392
- **Abstract**: In this paper, we consider a behavior of an autoregressive maximum-likelihood (ARML) detector and that of a conventional partial-response ML (PRML) detector against intertrack interference (ITI) of a perpendicular magnetic recording. Based on the consideration, we propose a calculation of a branch metric with the ITI estimation for the ARML detector, And also, we explain that the performance of the ARML detector is sensitive to the ITI. Finally, we show that our proposed ARML detector can derive a better performance against the ITI.

## Fast simulation method of BER performance of error correcting codes over AWGN channel

- **Status**: ❌
- **Reason**: AWGN에서 ECC의 BER 성능 시뮬레이션 가속 기법. ECC 자체 기법이 아니라 평가/시뮬레이션 방법론 → 떼어낼 디코더/구성/HW 없음, 제외
- **ID**: ieee:4895489
- **Type**: conference
- **Published**: 7-10 Dec. 
- **Authors**: Haruo Ogiwara, Yasunori Hori, Toshiyuki Shohon
- **PDF**: https://ieeexplore.ieee.org/document/4895489
- **Abstract**: This article proposes a method to estimate the bit error rate performance of error correcting code over an additive white Gaussian noise channel at SNR=A[dB] by simulation at SNR=B[dB] which is less than A and to accelerate the estimation. The previous such method, called envelope method (EM) needs an auxiliary simulation at SNR=A[dB] in addition to the simulation at SNR=B[dB]. The proposed method makes the auxiliary simulation unnecessary, by using analytically derived property at SNR=A[dB], and becomes faster than EM. The application of the proposed method makes the simulation time 50% for an LDPC code of length 1027 and 20% for an LDPC code of length 4000 compared to time needed by direct simulations. The simulation time also reduces to 60% of that of EM. This article discusses the variance of the estimated BER which was not discussed in the previous report.

## Cooperative communication

- **Status**: ❌
- **Reason**: 제목만 'Cooperative communication', 초록 null, LDPC 관련 기법 식별 불가
- **ID**: ieee:4895370
- **Type**: conference
- **Published**: 7-10 Dec. 
- **Authors**: 
- **PDF**: https://ieeexplore.ieee.org/document/4895370
- **Abstract**: N/A

## Performance of Regular Low Density Parity Check Codes over Hybrid Optical/RF Channels

- **Status**: ❌
- **Reason**: 표준 regular LDPC를 hybrid FSO/RF 채널에 적용+density evolution 분석, 새 디코더/구성 없음
- **ID**: ieee:4698546
- **Type**: conference
- **Published**: 30 Nov.-4 
- **Authors**: Hrishikesh Tapse, Deva K. Borah
- **PDF**: https://ieeexplore.ieee.org/document/4698546
- **Abstract**: A hybrid channel, consisting of a free space optical (FSO) link and a parallel radio frequency (RF) link, is considered. Information bits are first encoded by a low density parity check (LDPC) code and the coded bits are transmitted through both the FSO and the RF links. A density evolution (DE) technique to analyze the convergence of the message passing algorithm at the detector is described for the hybrid channel, and a Gaussian approximation (GA) technique is presented. Numerical results showing the benefits of the hybrid channel are discussed.

## A Class of Quantum LDPC Codes Constructed From Finite Geometries

- **Status**: ❌
- **Reason**: 양자 LDPC(self-orthogonal, depolarizing channel) — 직교성 등 양자 전용 개념 의존, 고전 바이너리 이식 아님
- **ID**: ieee:4697992
- **Type**: conference
- **Published**: 30 Nov.-4 
- **Authors**: Salah A. Aly
- **PDF**: https://ieeexplore.ieee.org/document/4697992
- **Abstract**: Low-density parity check (LDPC) codes are a significant class of classical codes with many applications. Several good LDPC codes have been constructed using random, algebraic, and finite geometries approaches, with containing cycles of length at least six in their Tanner graphs. However, it is impossible to design a self-orthogonal parity check matrix of an LDPC code without introducing cycles of length four. In this paper, a new class of quantum LDPC codes based on lines and points of finite geometries is constructed. The parity check matrices of these codes are adapted to be self- orthogonal with containing only one cycle of length four in each pair of two rows. Also, the column and row weights, and bounds on the minimum distance of these codes are given. As a consequence, these codes can be encoded using shift-register encoding algorithms and can be decoded using iterative decoding algorithms over various quantum depolarizing channels.

## Virtual Channel Based LLR Calculation for LDPC Coded SC-FDE System in 60-GHz WPAN

- **Status**: ❌
- **Reason**: SC-FDE 60GHz WPAN용 가상채널 LLR 계산, 무선 채널 특이적 LLR, NAND 이식 불가
- **ID**: ieee:4698547
- **Type**: conference
- **Published**: 30 Nov.-4 
- **Authors**: Ming Lei, Senjie Zhang, Kuilin Chen +3
- **PDF**: https://ieeexplore.ieee.org/document/4698547
- **Abstract**: To deal with the multi-path delay spread in non- line-of-sight (NLOS) environments, single-carrier frequency- domain equalization (SC-FDE), a.k.a., single-carrier block transmission (SCBT), is thought to be an effective alternative of orthogonal frequency division multiplexing (OFDM). On the other hand, the low-density parity-check (LDPC) coding is considered as the high-performance channel coding scheme due to its good tradeoff between performance and complexity. To facilitate using LDPC for SC-FDE, we proposed a virtual channel based log-likelihood ratio (LLR) calculation method aided by the Unique Word (UW). The proposed method can significantly improve the LDPC decoding performance in SC-FDE system, and does not need additional overhead or complexity. This is very promising to support ultra high-data-rate wireless transmission.

## An Improvement on LDPC Coded Queued Codes

- **Status**: ❌
- **Reason**: LDPC queued-code의 puncturing/repetition 구성은 block fading 채널 전용; NAND 무관한 무선 적응 puncturing
- **ID**: ieee:4698544
- **Type**: conference
- **Published**: 30 Nov.-4 
- **Authors**: Ming Jiang, Chunming Zhao, Enyang Xu +1
- **PDF**: https://ieeexplore.ieee.org/document/4698544
- **Abstract**: The queued-code based on low-density parity-check (LDPC) codes, which exploit both the near Shannon-limit performance LDPC codes and the instantaneous channel state information (CSI), can provide excellent performance in the block fading channels. The existing work utilized the conventional random puncturing and repetition operation, which may lead to considerable performance loss due to the changed intrinsic connections of parity-check matrix (PCM) for the receiver. In this paper, we present a reversed sequential puncturing (RSP) scheme and a construction method with modified dual-diagonal structure for the LDPC coded queued-code. The consecutive puncturing pattern in reversed direction can ensure the uniform row-weight distribution of the punctured PCM. The modified dual-diagonal form and the RSP scheme can ensure no more than one punctured symbol involved in each check-sum equation. The simulation results demonstrate that our proposed scheme can achieve noticeable performance gains.

## An Efficient Hybrid ARQ System Using Multilevel Coded Modulation with Reduced Constellation Size

- **Status**: ❌
- **Reason**: HARQ+멀티레벨 코딩 변조, 무선 재전송 기법, 떼어낼 LDPC ECC 없음
- **ID**: ieee:4698503
- **Type**: conference
- **Published**: 30 Nov.-4 
- **Authors**: Takashi Tamagawa, Hideki Ochiai
- **PDF**: https://ieeexplore.ieee.org/document/4698503
- **Abstract**: In order to guarantee highly reliable communications over noisy channels, the use of retransmission techniques is necessary, and the hybrid auto repeat request (HARQ) technique has been widely adopted in packet-based data communication systems. A common approach is to retransmit the entire packet that contains uncorrectable errors. However, this approach is inefficient if the number of errors in those packets is small. In this paper, we propose a new HARQ system based on multilevel coded modulation and multi-stage decoding at the receiver. In this system, retransmission is performed based on each level of multilevel signaling with reduced constellation size. The major advantage of this approach is that not only retransmission is efficient, but also the receiver complexity for code combining is low. Moreover, this approach offers a flexibility in the retransmission patterns. We derive an optimal algorithm of retransmission based on the channel capacity rule in this framework. The simulation results demonstrate that the proposed HARQ can significantly outperform the HARQ system based on the bit-interleaved coded modulation (BICM).

## Distance-Enhancing Constrained Codes for Optical Recording Channels

- **Status**: ❌
- **Reason**: 광기록 채널 거리증강 제약부호(RMTR) — 제약/변조부호, LDPC ECC 아님
- **ID**: ieee:4698362
- **Type**: conference
- **Published**: 30 Nov.-4 
- **Authors**: Kui Cai, Kees A. Schouhamer Immink, Zhiliang Qin
- **PDF**: https://ieeexplore.ieee.org/document/4698362
- **Abstract**: This paper proposes distance-enhancing constrained codes for optical recording channels. The repeated minimum transition runlength (RMTR) constraints are first investigated, based on error event analysis and capacity calculation. A new RMTR constrained code is then proposed. Compared with the codes used in standard systems, it imposes the minimum achievable RMTR constraint on the channel bit stream with the least decoding window length, without introducing additional code rate loss. A systematic method is further proposed, which can efficiently combine the RMTR code with the parity-check (PC) codes. Simulation results show that the new RMTR constrained PC code performs 1.1 dB better than the 17PP code, at BER = 10-5 and high recording density.

## Receiver-Cooperation: Network Coding and Distributed Scheduling

- **Status**: ❌
- **Reason**: 네트워크 코딩 수신협력(OSBram), QC-LDPC는 구조적 비유로만 언급, 떼어낼 ECC 기법 없음
- **ID**: ieee:4698690
- **Type**: conference
- **Published**: 30 Nov.-4 
- **Authors**: Phisan Kaewprapha, Nattakan Puttarak, Haidong Wang +1
- **PDF**: https://ieeexplore.ieee.org/document/4698690
- **Abstract**: We study network-coded receiver cooperation for a wireless system comprising a remote sender and a set of local receivers. Network codes based on GF(2q) random-mixing are complex and prone to errors. Sparse binary random-mixing is considerably simpler, but for it to be space-preserving requires the involvement of a huge number of source packets (vectors). We propose a novel strategy of offset sparse binary random-mixing (OSBram), in which the source vectors are firstly circularly shifted, each by a different random offset, before being XORed. This simple strategy cleverly compensates the low degree of the binary field by the large dimension of the vector space, ensure (near) linear-independence of random binary superpositions, and finds solid structural support from the well-known class of quasi-cyclic low-density parity-check codes. A second innovation is the introduction of scheduling in user cooperation. We show that this previously ignored factor can be critical to cooperative gains. An elegant distributed scheduler is proposed that allows distributed nodes to quickly reach a rational consensus without the need to exchange any side information.

## New Rateless Sparse-Graph Codes with Dynamic Degree Distribution for Erasure Channels

- **Status**: ❌
- **Reason**: rateless erasure 채널용 동적 차수분포 코드 — fountain/erasure 계열, 떼어낼 NAND ECC 기법 없음
- **ID**: ieee:4697994
- **Type**: conference
- **Published**: 30 Nov.-4 
- **Authors**: Xingkai Bao, Jing Li
- **PDF**: https://ieeexplore.ieee.org/document/4697994
- **Abstract**: A new class of rateless low-density parity-check (LDPC) codes, called the dynamic degree distribution (DDD) codes, are proposed for erasure channels. The parity symbols are generated from a set of degree distributions, one embedded in one another and each optimized for different channel erasure rates. Thus, instead of sticking to a fixed degree distribution for all the channel conditions, the encoder progressively adapts different degree distributions for different channel conditions, such that each distribution is operated in its most-desirable region. Theoretic analysis shows that the new codes perform close to the capacity in a large range of code rates with fairly low complexity. Simulations confirm that these codes can actually outperform the existing raptor rateless codes.

## Bandwidth-Efficient Modulation Codes Based on Nonbinary Irregular Repeat Accumulate Codes

- **Status**: ❌
- **Reason**: 비이진(nonbinary) IRA 코드 + 변조 — 비이진 LDPC 제외 대상
- **ID**: ieee:4697999
- **Type**: conference
- **Published**: 30 Nov.-4 
- **Authors**: Mao-Ching Chiu
- **PDF**: https://ieeexplore.ieee.org/document/4697999
- **Abstract**: Due to the random nature of LDPC codes, most of the good LDPC codes found in the literature do not possess a simple encoding structure. Thus, the encoding complexity of those LDPC codes can be as high as O(N 2), where N is the codeword length. To reduce the encoding complexity, in this paper, binary irregular repeat accumulate (IRA) codes are extended to the nonbinary cases for bandwidth-efficient modulation schemes. By proper selection of nonuniform signal constellations, the constructed codes are inherently capable to obtain shaping gains even without shaping codes. Under Gaussian approximation, extrinsic information transfer (EXIT) charts for nonbinary IRA codes are developed and several codes of different spectral efficiencies are designed based on EXIT charts. Simulation results indicate that the proposed codes not only have simple encoding schemes, but also have remarkable performances that are comparable to those of nonbinary LDPC codes.

## Spatial Diversity with LDPC Codes

- **Status**: ❌
- **Reason**: 무선 SIMO 공간다이버시티 응용; LDPC는 부수 언급, 떼어낼 디코더/HW/코드설계 기법 없음
- **ID**: ieee:4746596
- **Type**: conference
- **Published**: 30 Nov.-4 
- **Authors**: Surbhi Sharma, Rajesh Khanna
- **PDF**: https://ieeexplore.ieee.org/document/4746596
- **Abstract**: Wireless links are impaired by random fluctuations in signal level across space, time and frequency known as fading. Spatial diversity is an attractive solution to improve system capacity as well as system performance by providing array gain or increased SNR. Satellites (GEO,MEO) and High Altitude platform stations(HAPS) also exploit spatial diversity in LOS/NLOS envirornment. Exact nature of the diversity system depends on satellite antenna configuration. One of such configuration is SIMO diversity system that realizes receive diversity. LDPC codes have outstanding performance in some cases than that of turbo codes, with iterative decoding algorithm which is easy to implement and parallelizable in hardware. LDPC codes when implemented along with SIMO system with Maximum Ratio Combining (MRC) under the combination of AWGN and multipath fading is optimum from the standpoint of maximising SNR at combiner output. In addition when operating in interference scenario optimum combining can be employed that maximizes the output SINR. In this paper it is shown that LDPC codes with optimum combining (LDPC-OC) system improves SINR by 1.98 dB and 2.62 dB with 3 and 4 receive antennas respectively in multipath fading channel in the presence of a single interferer.

## Media Defect Recovery Using Full-Response Reequalization in Magnetic Recording Channels

- **Status**: ❌
- **Reason**: 자기기록 채널 미디어 결함 복구(reequalization) — 채널 검출/이퀄라이저 기법, NAND LDPC 디코더 이식 아님
- **ID**: ieee:4698361
- **Type**: conference
- **Published**: 30 Nov.-4 
- **Authors**: Weijun Tan, Shaohua Yang, Kelly Fitzpatrick +3
- **PDF**: https://ieeexplore.ieee.org/document/4698361
- **Abstract**: Conventional method for media defect recovery in a low-density parity-check (LDPC) coded magnetic recording channel is erasure decoding. In erasure decoding, read back signal in media defect region is erased and not used in channel detection or iterative decoding. In this paper, a new method based on full-response reequalization, in which media defect corrupted signal is first reequalized to full response then partially used in iterative decoding, is proposed. Simulation results show significant performance improvement over conventional erasure decoding in both non-precoded and preceded channels.

## Optimizing TCP Performance Through Joint Channel Coding and Power Management in Power Constrained Satellite Networks

- **Status**: ❌
- **Reason**: 위성 TCP 성능 최적화에 LDPC 부수 언급 — 무선/통신 응용 특이적, 떼어낼 기법 없음
- **ID**: ieee:4698336
- **Type**: conference
- **Published**: 30 Nov.-4 
- **Authors**: Laura Galluccio, Giacomo Morabito, Sergio Palazzo +2
- **PDF**: https://ieeexplore.ieee.org/document/4698336
- **Abstract**: In this paper an analytical framework is introduced for the optimization of TCP performance through joint channel coding and transmission power management in satellite communications, where both energy and bandwidth are scarce and costly resources. More specifically, the analysis takes into account the use of Low-Density Parity-Check (LDPC) codes as coding scheme for high data rate satellite communications. The analytical framework allows for the evaluation of the transmission power and coding rate that maximize the TCP throughput per unitary cost, which is a metric defined in terms of energy cost and bandwidth cost when related to throughput. Numerical examples demonstrate the usability of the proposed framework.

## Physical Layer Network Coding Schemes over Finite and Infinite Fields

- **Status**: ❌
- **Reason**: Physical-layer network coding (relay) 무선 응용, LDPC ECC 기법 없음
- **ID**: ieee:4698501
- **Type**: conference
- **Published**: 30 Nov.-4 
- **Authors**: Shengli Zhang, Soung Chang Liew, Lu Lu
- **PDF**: https://ieeexplore.ieee.org/document/4698501
- **Abstract**: Direct application of network coding at the physical layer - physical layer network coding (PNC) - is a promising technique for two-way relay wireless networks. In a two-way relay network, relay nodes are used to relay two-way information flows between pairs of end nodes. This paper proposes a precise definition for PNC. Specifically, in PNC, a relay node does not decode the source information from the two ends separately, but rather directly maps the combined signals received simultaneously to a signal to be relayed. Based on this definition, PNC can be further sub-classed into two categories - PNCF (PNC over finite field) and PNCI (PNC over infinite field) - according to whether the network-code field (or groups, rings) adopted is finite or infinite. For each of PNCF and PNCI, we consider two specific estimation techniques for dealing with noise in the mapping process. The performance of the four schemes is investigated by means of analysis and simulation, assuming symbol-level time synchronization only.

## H-ARQ Based Non-Orthogonal Multiple Access with Successive Interference Cancellation

- **Status**: ❌
- **Reason**: NOMA+HARQ+SIC 무선 다중접속, LDPC 무관, 떼어낼 ECC 기법 없음
- **ID**: ieee:4698415
- **Type**: conference
- **Published**: 30 Nov.-4 
- **Authors**: Jinho Choi
- **PDF**: https://ieeexplore.ieee.org/document/4698415
- **Abstract**: In this paper, we consider non-orthogonal multiple access (NOMA) over block fading channels where the performance is limited by interference and fading. Re-transmission and interference cancellation techniques can be employed to improve performance. Re-transmissions can provide diversity gain, while successive interference cancellation (SIC) can improve signal to interference ratio (SIR). We can show that the proposed NOMA approach with re-transmission outperforms an orthogonal multiple access (OMA) approach with re-transmission using information outage probability when the signal to noise ratio (SNR) is low. It can also be shown that the outage probability of the NOMA with SIC is lower than that of the OMA when the transmission rate is sufficiently low where SIC can be facilitated.

## A Novel Fast Semi-Analytical Performance Prediction Method for Iterative MMSE-IC Multiuser MIMO Joint Decoding

- **Status**: ❌
- **Reason**: MIMO 다중사용자 MMSE-IC 결합디코딩 성능예측(MIESM), LDPC ECC 기법 아님
- **ID**: ieee:4697988
- **Type**: conference
- **Published**: 30 Nov.-4 
- **Authors**: Raphael Visoz, Antoine O. Berthet, Massinissa Lalam
- **PDF**: https://ieeexplore.ieee.org/document/4697988
- **Abstract**: This paper presents a novel fast performance prediction method for iterative minimum-mean square error interference cancellation based joint decoding in a very general multiuser MIMO setting considering a transmission over block-fading frequency-selective channels. A Gaussian approximation is made for all propagated messages between the outer codes and the space-time multiuser detector. The method relies on a signal-to-interference-plus-noise ratio compression, by means of the mutual information effective signal-to-noise metric (MIESM), which allows a one-dimensional AWGN look-up table to capture the soft decoding result of each distinct user. Simulations show that this method while being extremely simple and fast keeps very accurate and is thus adequate for radio resource management and link adaptation purposes.

## Novel Graph-Based Algorithms for Soft-Output Detection over Dispersive Channels

- **Status**: ❌
- **Reason**: ISI 채널 soft-output detection/turbo equalization용 factor graph — 채널 검출기법, LDPC ECC 비의존
- **ID**: ieee:4697998
- **Type**: conference
- **Published**: 30 Nov.-4 
- **Authors**: Dario Fertonani, Alan Barbieri, Giulio Colavolpe
- **PDF**: https://ieeexplore.ieee.org/document/4697998
- **Abstract**: We address the design of low-complexity algorithms for soft-output detection over channels impaired by intersymbol interference. Unlike most works with similar aims, which assume the presence of the whitened matched filter at the receiver (Forney approach), algorithms that can directly work on the matched filter output (Ungerboeck approach) are considered. We introduce a novel (cyclic) factor graph describing the channel and, by applying the sum-product algorithm to it, we derive soft-output detection schemes that can provide impressive complexity reductions with respect to the benchmark algorithms, since their complexity is linear, instead of exponential, in the channel memory. Finally, we report simulation results proving that the performance of the proposed algorithms makes them appealing for turbo equalization in various practical scenarios.

## Routing with Probabilistic Delay Guarantees in Wireless Ad-Hoc Networks

- **Status**: ❌
- **Reason**: 무선 ad-hoc 라우팅 지연보장, LDPC 무관
- **ID**: ieee:4698569
- **Type**: conference
- **Published**: 30 Nov.-4 
- **Authors**: Matthew Brand, Petar Maymounkov, Andreas F. Molisch
- **PDF**: https://ieeexplore.ieee.org/document/4698569
- **Abstract**: In many wireless ad-hoc networks it is important to find a route that delivers a message to the destination within a certain deadline (delay constraint). We propose to identify such routes based on average channel state information (CSI) only, since this information can be distributed more easily over the network. Such cases allow probabilistic QoS guarantees i.e., we maximize and report the probability of on-time delivery. We develop a convolution-free lower bound on probability of on-time arrival, and a scheme to rapidly identify a path that maximizes this bound. This analysis is motivated by a class of infinite variance subexponential distributions whose properties preclude the use of deviation bounds and convolutional schemes. The bound then forms the basis of an algorithm that finds routes that give probabilistic delay guarantees. Simulations demonstrate that the algorithm performs better than shortest-path algorithm based on statistics of path loss or CSI.

## An O(qlogq) log-domain decoder for non-binary LDPC over GF(q)

- **Status**: ❌
- **Reason**: 비이진 GF(q) LDPC 디코더—바이너리 LDPC만 포함 대상, 제외
- **ID**: ieee:4746352
- **Type**: conference
- **Published**: 30 Nov.-3 
- **Authors**: Chun-Hao Liao, Chien-Yi Wang, Chun-Hao Liu +1
- **PDF**: https://ieeexplore.ieee.org/document/4746352
- **Abstract**: This paper presents a log-domain decoder for non-binary LDPC over GF(q). Comparing with the conventional O(q2) decoders, the proposed decoder can efficiently reduce the decoding complexity to O(qlogq) with only negligible degradation in BER. Comparisons on both simulated BER performance and computational complexity between the proposed and existing log-domain decoders are also provided.

## Scalable and parallel codec architectures for the DVB-S2 FEC system

- **Status**: ❌
- **Reason**: DVB-S2 BCH+LDPC-IRA 표준 코덱 HW; 표준 부호 구성 그대로, 새 디코더/구성 기여 약함
- **ID**: ieee:4746318
- **Type**: conference
- **Published**: 30 Nov.-3 
- **Authors**: M. Gomes, G. Falcao, V. Silva +5
- **PDF**: https://ieeexplore.ieee.org/document/4746318
- **Abstract**: The recent Digital Video Satellite Broadcast Standard (DVB-S2) has adopted a powerful FEC scheme based on the serial concatenation of Bose-Chaudhuri-Hocquenghen (BCH) and low-density parity-check (LDPC) codes. The high-speed requirements, long block lengths and adaptive encoding defined in the DVB-S2 standard, present complex challenges in the design of an efficient codec hardware architecture. In this paper, synthesizable, high throughput, scalable and parallel HDL models supporting the 21 different BCH+LDPC DVB-S2 code configurations are presented. For BCH decoding, an efficient Chien search circuit for shortened BCH codes is proposed. The LDPC codec architecture explores the periodicity M = 360 of the special LDPC-IRA codes adopted by the standard. Synthesis results for an FPGA device from Xilinx show a throughput above the minimal 90 Mbps.

## Bit manipulation techniques for LDPC coding in OFDM

- **Status**: ❌
- **Reason**: 무선 OFDM 적응형 bit-loading/permutation 응용, 표준 regular LDPC 부수 언급, 떼어낼 ECC 기법 없음
- **ID**: ieee:4736551
- **Type**: conference
- **Published**: 3-5 Dec. 2
- **Authors**: T. E. Salamon, O. Amrani
- **PDF**: https://ieeexplore.ieee.org/document/4736551
- **Abstract**: This work considers a wireless OFDM system employing a short-length, regular, low density parity check code (LDPC) when only limited feedback is available between receiver and transmitter. Methods are discussed for combining the advantages of LDPC codes with adaptive techniques, when the transmitter is subject to a restricting spectral mask. 0.5 dB gain is demonstrated when combining a regular, rate-half, LDPC code with adaptive bit-permutation using a constant modulation scheme over all subchannels. Gains of up to 1.5 dB are reported when combining this code with a BER-optimized adaptive bit-loading technique.

## Bounds on the thresholds of non-binary LDPC codes

- **Status**: ❌
- **Reason**: non-binary GF(q) LDPC threshold bound — 비이진 LDPC 제외 대상
- **ID**: ieee:4736544
- **Type**: conference
- **Published**: 3-5 Dec. 2
- **Authors**: Oron Levi, David Burshtein
- **PDF**: https://ieeexplore.ieee.org/document/4736544
- **Abstract**: LDPC codes over non-binary Galois fields were proposed for reliable transmission over arbitrary discrete memoryless channels and in particular for transmission in the bandwidth efficient regime. It was shown that some properties, originally derived for binary LDPC codes, extend to the appropriately defined non-binary ensemble. However, the extension of density evolution to this ensemble results in a prohibitive computational complexity. In this paper we analyze the performance by tracking the evolution of the Bhattacharya noise parameter associated with the decoding messages, and derive upper and lower bounds on its evolution. These bounds are then used to obtain upper and lower bounds on the asymptotic threshold required for reliable communication.

## Bit-Error-Rate of LDPC coded QAM in the presence of a residual phase noise process and a non-linear distortion

- **Status**: ❌
- **Reason**: 위상잡음/비선형 왜곡하 LDPC-QAM BER 해석, 신규 디코더/구성/HW 기여 없는 성능분석
- **ID**: ieee:4736682
- **Type**: conference
- **Published**: 3-5 Dec. 2
- **Authors**: Yitzhak Aviv, Isaac Rosenhouse
- **PDF**: https://ieeexplore.ieee.org/document/4736682
- **Abstract**: In this paper we present an analysis of the Bit Error Rate (BER) of LDPC-coded-QAM systems in an Additive-White-Gaussian-Noise (AWGN) channel impaired by a residual Phase-Noise (PN) process and a Nonlinear (NL) distortion. We start by deriving expressions for the Mean-Square-Error (MSE) caused by these common impairments. The BER is calculated separately for the coded bits and the uncoded bits, in a coded modulation scheme. In the first case, the MSE is added to the channel noise variance. As a consequence, the BER curve, which is assumed to be known, is shifted and an error floor is generated. The BER of the uncoded bits is calculated directly from the phase noise variance, the channel SNR and the nonlinear distortion which affects the distance between constellation points. Simulation results using an LDPC code validate the derivations.

## Iterative multiuser detection in coded UWB

- **Status**: ❌
- **Reason**: UWB TH-IR 다중사용자 검출/반복디코딩 응용 특이적, LDPC 부호 비의존, 이식 가능한 LDPC ECC 기법 없음
- **ID**: ieee:4736568
- **Type**: conference
- **Published**: 3-5 Dec. 2
- **Authors**: Y. Shen bahar, O. Amrani
- **PDF**: https://ieeexplore.ieee.org/document/4736568
- **Abstract**: Ultra wide band Time-Hopping Impulse-Radio (UWB THIR) received renewed attention in recent years. This approach is known to achieve high data rates in multiuser environment. The current work introduces coding into the original uncoded scheme and provides a simple decoder accompanied by its performance analysis. A new system model is derived and the capacity of the system is calculated. It is shown that the original scheme can not achieve capacity. A new iterative decoding algorithm is also introduced. Simulation results reveal that the proposed coding and decoding approach compare favorably with other TH-IR UWB communication schemes.

## Reduced tree-search, heuristic and linear decoupler low-complexity MIMO detectors

- **Status**: ❌
- **Reason**: MIMO 검출기 저복잡도; short LDPC 부수 언급, 떼어낼 디코더 기법 없음
- **ID**: ieee:4772704
- **Type**: conference
- **Published**: 27-29 Dec.
- **Authors**: Isaque Suzuki, Fernando Ciriaco, Taufik Abrao +1
- **PDF**: https://ieeexplore.ieee.org/document/4772704
- **Abstract**: Since the optimal detector for coded and even uncoded multiple-input-multiple-output (MIMO) antenna systems results too complex when the number of antennas and/or the modulation order index increases, strictly low-complexity detection schemes are considered, aiming to achieve promising performance times complexity trade-off. Under the same throughput basis, this work analyzes some capacity-approaching heuristic and reduced tree-search MIMO detection algorithms, combining simple linear decouplers, local search detectors, particle swarm intelligence (PSO) concepts and parallel short low density parity check codes (LDPC), suitable to uncoded as well to MIMO channel coding. For uncoded MIMO systems, low-complexity PSO approach showed to reach efficiently MIMO near-capacity for any number of transmit and receive antennas configuration, while simple linear decoupler detectors for QPSK modulation with short LDPC coding achieve reasonable performance only for nR ges nT condition.

## Reversible watermarking with localization for biometric images

- **Status**: ❌
- **Reason**: 가역 워터마킹/데이터하이딩, ECC와 무관
- **ID**: ieee:4795762
- **Type**: conference
- **Published**: 17-20 Dec.
- **Authors**: Hyobin Lee, Seongwan Kim, Jaeho Lee +2
- **PDF**: https://ieeexplore.ieee.org/document/4795762
- **Abstract**: In this paper, we propose a novel reversible data hiding algorithm, which can recover the original image if it is deemed authentic or detect the block-wise malicious manipulation if it is classified as manipulated. We explore the strong spatial correlation of neighboring pixels in digital images to achieve very high embedding capacity and keep the distortion low. Also, this technique provides cryptographic strength when verifying image integrity because the probability of making undetectable modifications to the image is directly related to a secure cryptographic element, such as a hash function. The algorithm has been successfully applied to a wide range of images, including commonly used images, biometric images, texture images, and aerial images. Experimental results and performance comparison with other reversible data hiding schemes are presented to demonstrate the validity of the proposed algorithm.

## Capacity and BER analysis for Nakagami-n channel in LDPC coded wireless sensor network

- **Status**: ❌
- **Reason**: 무선센서망 LDPC coded 용량/BER 분석, LDPC는 부수 적용이고 신규 디코더·구성·HW 기여 없음
- **ID**: ieee:4761981
- **Type**: conference
- **Published**: 15-18 Dec.
- **Authors**: Mohammad Rakibul Islam, Jinsang Kim
- **PDF**: https://ieeexplore.ieee.org/document/4761981
- **Abstract**: Energy efficient transmission with fairly high capacity is an attractive feature for energy constraint wireless sensor network. This opens a door for the outage analysis keeping the energy efficient performance active. We propose to employ LDPC codes to provide reliable communication while saving power in the sensor networks. We derive the ergodic and outage capacity for a cluster head to DGN transmission through a Nakagami-n channel in a wireless sensor network. We also explore the BER analysis for the same channel for an LDPC coded transmission. We compared the ergodic and outage capacity over average SNR for different Nakagami channel parameter. We see that the ergodic as well as outage capacity increases as both SNR and Nakagami-n channel parameters increase. We also compare the outage capacity for different probability of outage. Nakagami-n channel simulations are also compared with AWGN channel simulations. Simulation results show that with the proper choice of LDPC decoding, capacity achieving low power transmission is possible in wireless sensor network.

## Improved BP Decoding Algorithm for Nonbinary LDPC Codes Based on Bit-flipping Method

- **Status**: ❌
- **Reason**: 비이진(nonbinary) LDPC 디코딩 알고리즘; 비이진 제외 대상
- **ID**: ieee:4724677
- **Type**: conference
- **Published**: 13-17 Dec.
- **Authors**: Man Teng, Xingcheng Liu, Zerong Deng
- **PDF**: https://ieeexplore.ieee.org/document/4724677
- **Abstract**: Nonbinary LDPC codes demonstrated excellent performance. However, how to reduce the decoding complexity for such codes without performance degradation is still a problem to be solved. In this paper, the bit-flipping method is introduced into the standard Fourier transform decoding algorithm for decoding nonbinary LDPC codes. Simulation results show that the proposed method gains better BER performance with efficiently reduce of the decoding computation complexity in high Eb/N0 regions.

## World-Wide Accessible LDPC Encoder/Decoder Generator Using Web-Based GUI and API

- **Status**: ❌
- **Reason**: LDPC 인코더/디코더 생성기의 웹 GUI/API 도구—구체적 신규 디코더/코드설계/HW 기법 없음
- **ID**: ieee:5172698
- **Type**: conference
- **Published**: 10-12 Dec.
- **Authors**: Hirotaka Nosato, Yukari Ishida, Tatsumi Furuya +4
- **PDF**: https://ieeexplore.ieee.org/document/5172698
- **Abstract**: LDPC (low-density parity check) code, which is a class of error correcting code, is attracting attention due to the considerable potential for error correction that approaches the theoretical limits. However, there are some problems with LDPC code because it requires a great deal of time and effort involving trial and error in order to generate LDPC codes. Accordingly, we have proposed a design system for LDPC codes that uses a general-purpose cluster system and a hardware accelerator. However, it is rather difficult to utilize use the design system in real-world applications because of problems in widely implementing the cluster system and the hardware accelerator. Thus, the present paper proposes a Web-based application of the LDPC codes design system in order to overcome these problems. The proposal application has three advantages (no need for development of a commercial system, accessibility to the system all over the world with a general Web-browser, and streamlining and sharing with a database implementation of the system), and effectively solves the problems of applying LDPC codes for practical use.

## Performance evaluation of high capacity channel coding schemes using image transmission system

- **Status**: ❌
- **Reason**: LDPC vs RS 무선채널 성능 비교/이미지전송 평가, 신규 디코더/구성/HW 기여 없음
- **ID**: ieee:4786643
- **Type**: conference
- **Published**: 1-3 Dec. 2
- **Authors**: Ierwan Ab. Karim, M. F. M. Salleh
- **PDF**: https://ieeexplore.ieee.org/document/4786643
- **Abstract**: In this paper the performance evaluation of the low-density parity-check (LDPC) and Reed-Solomon (RS) codes over wireless channels is presented. These codes are used as the forward error correction (FEC) technique to protect source data prior transmission over wireless channel. The system simulation includes the use of additive White gaussian noise (AWGN) as the wireless channel, while a grayscale image is used as the data source. The quality of the reconstructed grayscale image is measured using the peak signal to noise ratio (PSNR) measurement. The quality of output grayscale image is considered good if the value of the PSNR is above 30 dB.
