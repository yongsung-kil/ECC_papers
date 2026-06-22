# IEEE Xplore — 2007-09


## Universal Context Based Decoding with Low-Density Parity-Check Codes

- **Status**: ❌
- **Reason**: BWT/소스압축 redundancy 활용 채널디코딩—소스코딩/denoising 결합, 떼어낼 바이너리 LDPC ECC 디코더 기법 아님
- **ID**: ieee:4299421
- **Type**: journal
- **Published**: September 
- **Authors**: Li Wang, Gil I. Shamir
- **PDF**: https://ieeexplore.ieee.org/document/4299421
- **Abstract**: Universal estimation strategies are proposed to improve channel decoding of sequences that contain context based redundancy. The new methods combine techniques from universal compression, such as the Burrows-Wheeler Transform (BWT) and segmentation of piecewise stationary memoryless sources (PSMS's) with recently proposed methods of discrete denoising. Simulation results with systematic low density parity check (LDPC) codes show significant improvements of the proposed methods on standard decoding, even when the actual sequence context model is unknown in advance. The combined methods inherit advantages of each of the separate methods.

## On Analysis and Design of Low Density Generator Matrix Codes for Continuous Phase Modulation

- **Status**: ❌
- **Reason**: LDGM(저밀도 생성행렬) 코드+CPM, 바이너리 LDPC ECC 부호설계 아니고 응용특이적
- **ID**: ieee:4362508
- **Type**: journal
- **Published**: September 
- **Authors**: Ming Xiao, Tor M. Aulin
- **PDF**: https://ieeexplore.ieee.org/document/4362508
- **Abstract**: We investigate the analysis and design of low density generator matrix (LDGM) codes for continuous phase modulation (CPM). The system uses LDGM codes as an outer code for CPM. For additive white Gaussian noise channels, we derive the union bound to analyze the error floor performance. Design principles for lowering error floors are suggested from this analysis. We propose a design approach of jointly considering the LDGM code degree and the CPM modulation index. Then we consider the rate-adaptive system for slowly fading channels. By changing the rate of the LDGM codes, the information rate of the CPM signals is adapted according to channel variations. We use a low-rate LDGM code as the mother code. Higher rates are achieved by puncturing the output of these codes. To exploit the rate-flexible property of punctured LDGM codes, a rate function is proposed to calculate the rate of each transmitted block. Thus, we can have a quasi-continuous information rate. Numerical results show that this approach can improve the energy efficiency from a discrete-rate adaptation. Using the rate-adaptive approach, up to 11 dB transmitted energy gain can be achieved from the non-adaptive scheme in the low bit-error-rate region (smaller than 10-3) for minimum shift keying (MSK).

## Low Density Parity Check Codes over Wireless Relay Channels

- **Status**: ❌
- **Reason**: 릴레이 채널용 irregular LDPC 코딩 설계—표준 LDPC를 응용에 적용, 떼어낼 신규 디코더/구성 기법 없음
- **ID**: ieee:4362502
- **Type**: journal
- **Published**: September 
- **Authors**: Jun Hu, Tolga M. Duman
- **PDF**: https://ieeexplore.ieee.org/document/4362502
- **Abstract**: We exploit the capacity approaching capability of low density parity check (LDPC) codes to design coding schemes for relay channels. We consider the classical relay channel model, and the use of both full-duplex relays and half-duplex ones. In addition to the design of practical coding schemes and the development of the appropriate receiver structures, we also exploit the use of average mutual information to characterize the convergence behavior of the proposed systems. Using the convergence predictions and the simulation results, we demonstrate that the proposed LDPC coded relay systems, in particular, with irregular LDPC codes, have the capability to approach the ergodic/outage information rates very closely. This is true for both ergodic fading channels where the Shannon type (constrained, i.e., modulation specific) capacity is considered, and non-ergodic fading channels where the outage capacity provides the appropriate limits of reliable communication. For the (time-division) half-duplex relay schemes, we also discuss the optimization of the time-division parameters, and the bit allocation strategies to improve the system performance further.

## Approaching MIMO-OFDM Capacity with Per-Antenna Power and Rate Feedback

- **Status**: ❌
- **Reason**: MIMO-OFDM closed-loop V-BLAST 전력/레이트 피드백, LDPC 무관
- **ID**: ieee:4299600
- **Type**: journal
- **Published**: September 
- **Authors**: Rui Zhang, Ying-chang Liang, Ravi Narasimhan +1
- **PDF**: https://ieeexplore.ieee.org/document/4299600
- **Abstract**: This paper presents power-efficient transmission schemes for the multiple-input multiple-output orthogonal frequency-division multiplexing (MIMO-OFDM) block-fading channel under the assumption that the channel during each fading block is known perfectly at the receiver, but is unavailable at the transmitter. Based on the well-known vertical Bell Labs layered space-time (V-BLAST) architecture that employs independent encoding for each transmit antenna and successive decoding at the receiver, this paper presents a per-antenna-based power and rate feedback scheme, termed the "closed-loop" V- BLAST, for which the receiver jointly optimizes the power and rate assignments for all transmit antennas, and then returns them to the transmitter via a low-rate feedback channel. The power and rate optimization minimizes the total transmit power for support of an aggregate transmission rate during each fading block. Convex optimization techniques are used to design efficient algorithms for optimal power and rate allocation. The proposed algorithms are also modified to incorporate practical system constraints on feedback complexity and on modulation and coding. Furthermore, this paper shows that the per-antenna-based power and rate control can be readily modified to combine with the conventional linear MIMO transmit preceding technique as an efficient and capacity-approaching partial-channel-feedback scheme. Simulation results show that the closed-loop V-BLAST is able to approach closely the MIMO-OFDM channel capacity assuming availability of perfect channel knowledge at both the transmitter and the receiver.

## Low-Complexity High-Rate Reed--Solomon Block Turbo Codes

- **Status**: ❌
- **Reason**: Reed-Solomon block turbo code, 비-LDPC이며 디코더가 RS BTC 전용이라 바이너리 LDPC BP에 이식 불가
- **ID**: ieee:4303371
- **Type**: journal
- **Published**: Sept. 2007
- **Authors**: Rong Zhou, Raphael Le Bidan, Ramesh Pyndiah +1
- **PDF**: https://ieeexplore.ieee.org/document/4303371
- **Abstract**: This letter considers high-rate block turbo codes (BTC) obtained by concatenation of two single-error-correcting Reed-Solomon (RS) constituent codes. Simulation results show that these codes perform within 1 dB of the theoretical limit for binary transmission over additive white Gaussian noise with a low-complexity decoder. A comparison with Bose-Chaudhuri-Hocquenghem BTCs of similar code rate reveals that RS BTCs have interesting advantages in terms of memory size and decoder complexity for very-high-data-rate decoding architectures.

## On the Error Exponent and the Use of LDPC Codes for Cooperative Sensor Networks With Misinformed Nodes

- **Status**: ❌
- **Reason**: LDPC가 센서망 stay-k 스케줄러의 응용 베이스라인일 뿐, 떼어낼 디코더/HW/코드설계 기법 없음
- **ID**: ieee:4294177
- **Type**: journal
- **Published**: Sept. 2007
- **Authors**: Zhiyu Yang, Lang Tong
- **PDF**: https://ieeexplore.ieee.org/document/4294177
- **Abstract**: The problem of retrieving information by a mobile access point from a sensor network where sensors cooperatively transmit messages using a common codebook is considered. It is assumed that there is a probability that a sensor is misinformed with a wrong message, which complicates the information retrieval process. The access point uses the capacity achieving stay-k scheduler that schedules a sensor to transmit for k consecutive code-letters before switching to a new sensor. The random coding exponent is derived as a function of k, and it is shown that there is an optimal k that gives the largest error exponent. The application of low-definition parity-check (LDPC) codes is considered next. It is shown in simulations that the optimal k of the stay-k scheduler for LDPC codes can be inferred from that for the random coding exponent.

## On Pilot-Symbol-Assisted Carrier Synchronization for DVB-S2 Systems

- **Status**: ❌
- **Reason**: DVB-S2 캐리어 동기화/주파수 추정, LDPC 디코더 기여 없음
- **ID**: ieee:4292329
- **Type**: journal
- **Published**: Sept. 2007
- **Authors**: Alan Barbieri, Giulio Colavolpe
- **PDF**: https://ieeexplore.ieee.org/document/4292329
- **Abstract**: We consider the problem of carrier synchronization in future 2nd-generation satellite digital video broadcasting (DVB-S2) receivers. In this scenario, this task is made harder by the complexity constraints, related to the use of consumer-grade equipment. Making use of the distributed pilot symbols of the DVB-S2 standard, low-complexity techniques for fine frequency estimation and for detection in the presence of a strong phase noise, typical of consumer-grade equipment, will be proposed. The performance of the described algorithms will be analysed in detail through computer simulations.

## A Lagrangian Relaxation Algorithm for Finding the MAP Configuration in QMR-DT

- **Status**: ❌
- **Reason**: QMR-DT 베이지안망 MAP 추론 Lagrangian relaxation, LDPC/ECC 무관
- **ID**: ieee:4292232
- **Type**: journal
- **Published**: Sept. 2007
- **Authors**: Feili Yu, Fang Tu, Haiying Tu +1
- **PDF**: https://ieeexplore.ieee.org/document/4292232
- **Abstract**: The quick medical reference decision-theoretic (QMR-DT) network is a large two-layer Bayesian network (BN) [consisting of 571 diseases (ldquofailure sourcesrdquo) and 4075 findings (ldquotest outcomesrdquo)] based on expert and statistical knowledge in internal medicine. The maximum a posteriori (MAP) diagnosis (configuration) based on QMR-DT constitutes an intractable inference problem for all, but a small set of, cases. Consequently, we consider near-optimal algorithms for finding the most likely set of diseases given a set of findings. A computationally efficient algorithm that can handle cases with hundreds of positive findings, i.e., the Lagrangian relaxation algorithm (LRA), is presented. By relaxing the original problem via a set of Lagrange multipliers, the LRA generates an upper bound for the objective function. The near-optimal diagnosis (configuration) is found by minimizing the duality gap via a subgradient method. Numerical experiments show that the LRA is promising in achieving highly accurate diagnosis, and that it is computationally very efficient in solving MAP configuration problems in large and dense two-layer BNs with noisy-OR (BN2O) nodes and containing undirected loops (cycles), such as the QMR-DT network.

## Signal-Processing-Aided Distributed Compression in Virtual MIMO-Based Wireless Sensor Networks

- **Status**: ❌
- **Reason**: WSN 분산 소스압축(distributed source coding), 채널 ECC 아님
- **ID**: ieee:4305507
- **Type**: journal
- **Published**: Sept. 2007
- **Authors**: Sudharman K. Jayaweera, Madhavi L. Chebolu, Rakesh K. Donapati
- **PDF**: https://ieeexplore.ieee.org/document/4305507
- **Abstract**: An adaptive signal-processing-aided distributed source coding scheme for virtual multiple-input-multiple-output communication-based wireless sensor networks (WSNs) is proposed. A computationally inexpensive distributed compression scheme that exploits the spatiotemporal correlations of sensor data is implemented with the aid of a recursive least squares (RLS)-based adaptive correlation tracking algorithm. The tracked correlation is used to compute side information that assists in distributed source compression. The proposed virtual space-time block coding and RLS-based compression side information are shown to improve energy efficiency at distributed nodes compared to previously proposed schemes with single-input-single-output communication. A semi-analytical approach is developed for energy efficiency analysis over different channel conditions and transmission distances. The energy efficiency performance of the proposed design is evaluated on real WSN data. The results show that the proposed integrated system outperforms conventional designs beyond certain transmission distance thresholds and leads to lower decoding errors, which makes it a good candidate for energy-aware WSNs.

## LDPC code optimization for diversity reception and turbo equalization

- **Status**: ❌
- **Reason**: 무선(turbo equalization/diversity) 응용 특이적 EXIT 기반 코드 최적화, NAND 이식 가능한 구성 기법 없음
- **ID**: ieee:5903301
- **Type**: conference
- **Published**: 7-7 Sept. 
- **Authors**: T. Schorr, M. Matuszak, W. Sauer-Greff +1
- **PDF**: https://ieeexplore.ieee.org/document/5903301
- **Abstract**: Iterative “turbo” decoding of parallel or serial concatenated convolutional codes (CC) allows for a performance close to Shannon's channel capacity limit. Whereas “turbo” equalization (TE) for intersymbol interference (ISI) channels corresponds to serial concatenation, we show that the turbo decoding principle for parallel concatenation can be extended to a diversity receiver concept. “Turbo diversity” outperforms maximum-ratio combining (MRC) in forward error correction (FEC) encoded broadcast systems like “Digital Radio Mondiale” (DRM). In addition, we apply low-density parity-check (LDPC) codes instead of CC to turbo equalization and to turbo diversity, where an LDPC code design using fitted extrinsic information transfer (EXIT) functions is applied to optimize the system performance.

## Turbo- and LDPC-Coded MIMO-OFDM Systems: A Comparative Study

- **Status**: ❌
- **Reason**: Turbo vs LDPC MIMO-OFDM 성능 비교만, 신규 디코더·구성 기여 없음 → 제외
- **ID**: ieee:4394817
- **Type**: conference
- **Published**: 3-7 Sept. 
- **Authors**: Baoshen Tan, Yan Xin, Syed Aon Mujtaba +1
- **PDF**: https://ieeexplore.ieee.org/document/4394817
- **Abstract**: In this paper, we employ iteratively decodable codes in a turbolike receiver of a multiple-input multiple-output (MIMO) orthogonal frequency division multiplexing (OFDM) communication system. With such a receiver, we compare the decoding complexity and performance of a turbo code with a low- density-parity-check (LDPC) code. For the same level of decoding complexity, we show that LDPC codes perform better than turbo codes in a typical high data rate MIMO-OFDM system.

## Design of spatially multiplexed LDPC codes for multi-user detection

- **Status**: ❌
- **Reason**: CDMA 다중사용자 검출용 LDPC 설계(EXIT 기반), 무선 응용 특이적·표준 설계 → 제외
- **ID**: ieee:7099016
- **Type**: conference
- **Published**: 3-7 Sept. 
- **Authors**: Gottfried Lechner, Andreas Burg
- **PDF**: https://ieeexplore.ieee.org/document/7099016
- **Abstract**: The extrinsic information transfer function of multi-user detection for synchronous CDMA is evaluated depending on the load of the system and the signal to noise ratio. This transfer function is used to discuss the benefits of putting redundancy into spreading or coding. Finally, it is shown how low-density parity-check codes can be designed for a specific system.

## Design and Code Optimization of Parallel Concatenated Gallager Codes

- **Status**: ❌
- **Reason**: 병렬연쇄 Gallager 부호(PCGC) EXIT 최적화 — turbo형 연쇄 구조 특이적, 단일 바이너리 LDPC BP에 떼어낼 기법 부족
- **ID**: ieee:4394240
- **Type**: conference
- **Published**: 3-7 Sept. 
- **Authors**: Fang Wang, Shixin Cheng, Wei Xu +1
- **PDF**: https://ieeexplore.ieee.org/document/4394240
- **Abstract**: Constructing PCGCs with unequal-code-rate irregular component LDPC codes is proposed in this paper. Parameters of component codes are optimized by differential evolution based on EXIT chart. In the optimization results, code rate of component code 1 is relatively higher and the other one is lower so that these two component codes play different roles in different decoding stages. Numerical simulation results show that the proposed PCGCs with optimized parameters outperform PCGCs constructed by equal-code-rate regular/likely regular component codes and optimized irregular LDPC code.

## Blind frame synchronization on Gaussian channel

- **Status**: ❌
- **Reason**: LDPC를 베이스라인으로 한 블라인드 프레임 동기화(LLR of syndrome) 응용, 떼어낼 ECC 디코더 기법 없음 → 제외
- **ID**: ieee:7098865
- **Type**: conference
- **Published**: 3-7 Sept. 
- **Authors**: Rodrigue Imad, Sebastien Houcke, Catherine Douillard
- **PDF**: https://ieeexplore.ieee.org/document/7098865
- **Abstract**: Being initially proposed for a Binary Symmetric Channel, we adapt in this paper a blind frame synchronization method to a Gaussian channel. This new method is based on the computation of the Logarithmic Likelihood Ratio (LLR) of the syndromes elements. A comparison between the performance of these two methods is done by synchronizing some Low Density Parity Check (LDPC) codes and Convolutional codes. The simulated results are also compared to the theoretical ones by finding the probabilities of false synchronization for the two methods. The theoretical results may help us to define a synchronization threshold so that the calculation time can be decreased.

## Iterative Detection and Decoding for the Near-Capacity Performance of Turbo Coded MIMO Schemes

- **Status**: ❌
- **Reason**: Turbo-coded MIMO 검출-복호(EXIT) 기법, LDPC 아님·떼어낼 BP 이식 기법 없음 → 제외
- **ID**: ieee:4394737
- **Type**: conference
- **Published**: 3-7 Sept. 
- **Authors**: Yeong-Luh Ueng, Chia-Jung Yeh, Chung-Li Wang +1
- **PDF**: https://ieeexplore.ieee.org/document/4394737
- **Abstract**: In this paper, we investigate detection-decoding algorithms for the near-capacity performances of turbo coded MIMO (multiple-input multiple-output) schemes in the fast fading channel. Both the conventional turbo coded MIMO scheme Gamma0 and turbo coded MIMO scheme with interblock memory which is denoted by Gamma are investigated. Gamma is implemented by introducing some delay elements between the BLAST mapper and the turbo encoder. We show that, unlike Gamma0, the extrinsic information transfer (EXIT) curves of detector and turbo decoder in Gamma can match well. Hence, Gamma can provide error performances much better than Gamma0. In particular, we find an improved detection and decoding algorithm which can closely approach the Shannon capacity.

## Optimal joint source channel coding for scalable video transmission over wireless channels

- **Status**: ❌
- **Reason**: JSCC 비디오 전송용 LDPC+turbo 직렬연결, LDPC는 베이스라인·NAND 이식 기법 없음 → 제외
- **ID**: ieee:7098889
- **Type**: conference
- **Published**: 3-7 Sept. 
- **Authors**: Naeem Ramzan, Ebroul Izquierdo
- **PDF**: https://ieeexplore.ieee.org/document/7098889
- **Abstract**: In this paper, a robust and novel approach for optimal bit allocation between source and channel coding is proposed. The proposed approach consists of a wavelet-based scalable video coding framework and a forward error correction method based on the serial concatenation of LDPC codes and turbo codes. Turbo codes shows good performance at low signal to noise ratios but LDPC outperforms turbo codes at high signal to noise ratios. So the concatenation of LDPC and TC enhances the performance at both low and high signal to noise ratios. The scheme reduces the video distortion at the decoder under band-with constraints. The reduction is achieved by efficiently protecting the different quality layers from channel errors. Furthermore, an efficient decoding algorithm is proposed that reduces the decoding complexity of channel decoder. Experimental results clearly show that the proposed approach outperforms conventional forward error correction techniques.

## Adaptive Exploitation of Residual Redundancy in Iterative Source-Channel Decoding

- **Status**: ❌
- **Reason**: 반복 소스-채널 복호(ISCD) 잔여중복 활용 — 채널 ECC 기법 아님, JSCC 계열 제외
- **ID**: ieee:4394167
- **Type**: conference
- **Published**: 3-7 Sept. 
- **Authors**: Birgit Schotsch, Peter Vary, Thorsten Clevorn
- **PDF**: https://ieeexplore.ieee.org/document/4394167
- **Abstract**: Iterative source-channel decoding (ISCD) aims at the exploitation of the time-variant residual redundancy of the source samples, e.g., source codec parameters, for error concealment and quality improvements. In most previous publications the receiver had perfect knowledge of the amount of residual redundancy. This assumption would require a reliable, i.e. highly redundant, transmission of side information. In contrast, in this paper we present a relatively simple scheme, yet efficient and robust, by which the residual redundancy at the receiver can be estimated accurately without any side information, and then can be exploited adaptively. We present the achievable performance gains in an ISCD system including the estimation of the residual source redundancy at the receiver for various scenarios. Several methods of different performance and computational complexity are proposed, with some of them even outperforming a system with perfect side information. The latter, not quite intuitive fact, is explained in the paper.

## A MAC Protocol with Multi-User MIMO Support for Ad-Hoc WLANs

- **Status**: ❌
- **Reason**: MIMO MAC 프로토콜, ECC/LDPC 무관
- **ID**: ieee:4394517
- **Type**: conference
- **Published**: 3-7 Sept. 
- **Authors**: Jelena Mirkovic, Jing Zhao, Dee Denteneer
- **PDF**: https://ieeexplore.ieee.org/document/4394517
- **Abstract**: Multiple Input-Multiple Output (MIMO) is a wide set of multiple antenna technologies, which significantly increase the capacity of wireless networks, without additional bandwidth or increased transmission power. They are widely recognized as methods that can meet the ever growing network capacity requirements. With a MIMO physical layer (PHY), the transmission channel gains a layered structure, which gives another degree of freedom in scheduling transmissions. Additionally, support from higher layers with a cross-layer approach that provides efficient management of the channel's spatial layers, can significantly increase the networks' performance on both link and system level. Single-User-DCF (SU-DCF), a Multiple Access Control (MAC) protocol with the support for Single-User (SU)-MIMO transmissions in Ad-Hoc WLANs, has been previously presented. In this paper we extend that protocol to support Multi-User (MU) transmissions. In the new protocol - Multi-User-DCF (MU-DCF), destination stations for the frames in a MIMO frame can be different stations. We have studied and compared different transmission strategies and schedulers including the IEEE 802.11n system, to explore the benefits of transmitting in MU mode.

## Performance Analysis of Turbo Codes over Nakagami-m Fading Channels with Impulsive Noise

- **Status**: ❌
- **Reason**: turbo 부호 성능분석, LDPC 아님 — 비-LDPC 제외
- **ID**: ieee:4394265
- **Type**: conference
- **Published**: 3-7 Sept. 
- **Authors**: Syed Amjad Ali, Erhan AliRiza Ince
- **PDF**: https://ieeexplore.ieee.org/document/4394265
- **Abstract**: The statistical characteristics of impulsive noise differ greatly from those of Gaussian noise. Hence, the performance of conventional decoders, optimized for AWGN channels is not promising in non-Gaussian environments. In order to achieve improved performance in impulsive environments the decoder structure needs to be adapted in accordance with the impulsive noise model. This paper provides performance analysis of turbo codes over fully interleaved Nakagami-m fading channels with Middleton's additive white Class-A impulsive noise (MAWCAIN). Simulation results for memoryless Nakagami-m fading channels under coherent BPSK signaling are provided for the cases of ideal channel state information (ICSI) and no channel state information (NCSI) at the decoder. As in the 3GPP UMTS forward link an eight state turbo encoder having (1, 13/15, 13/15) generator polynomial is used throughout the analysis. The novelty of this work lies in the fact that this is an initial attempt to provide a detailed analysis of turbo codes over Nakagami-m fading channels with impulsive noise rather than fading channels with AWGN.

## Error-resilient transmission of H.264 SVC streams over DVB-T/H and WiMAX channels with multiple description coding techniques

- **Status**: ❌
- **Reason**: H.264 SVC 다중기술 비디오 전송, LDPC ECC 무관 → 제외
- **ID**: ieee:7099157
- **Type**: conference
- **Published**: 3-7 Sept. 
- **Authors**: Peter Schelkens, Augustin Gavrilescu, Adrian Munteanu +6
- **PDF**: https://ieeexplore.ieee.org/document/7099157
- **Abstract**: The European STREP Project SUIT involves the development of a multiple description scalable video codec for the transmission of video content over DVB-T/H and WiMAX channels. In this paper, we elaborate on the architectural design choices for such a multiple description transmission system, which utilizes H.264 Scalable Video Coding (SVC). We follow a phased approach focusing on the following unbalanced multiple description coding approaches: fully redundant unbalanced multiple description coding, multiple description coding based on redundant slices and multiple description coding by means of embedded multiple description quantisation.

## Optimal Iris Fuzzy Sketches

- **Status**: ❌
- **Reason**: 홍채 바이오메트릭 fuzzy sketch 오류정정, 2D min-sum 응용이나 떼어낼 LDPC ECC 신규 기법 없음
- **ID**: ieee:4401904
- **Type**: conference
- **Published**: 27-29 Sept
- **Authors**: J. Bringer, H. Chabanne, G. Cohen +2
- **PDF**: https://ieeexplore.ieee.org/document/4401904
- **Abstract**: Fuzzy sketches, introduced as a link between biometry and cryptography, are a way of handling biometric data matching as an error correction issue. We focus here on iris biometrics and look for the best error-correcting code in that respect. We show that two-dimensional iterative min-sum decoding leads to results near the theoretical limits. In particular, we experiment our techniques on the iris challenge evaluation (ICE) database and validate our findings.

## Graphical Model-based Approaches to Target Tracking in Sensor Networks: An Overview of Some Recent Work and Challenges

- **Status**: ❌
- **Reason**: 센서네트워크 타겟트래킹용 그래피컬 모델 서베이, LDPC ECC 기법 없음
- **ID**: ieee:4383743
- **Type**: conference
- **Published**: 27-29 Sept
- **Authors**: Murat Uney, Mujdat Cetin
- **PDF**: https://ieeexplore.ieee.org/document/4383743
- **Abstract**: Sensor Networks have provided a technology base for distributed target tracking applications among others. Conventional centralized approaches to the problem lack scalability in such a scenario where a large number of sensors provide measurements simultaneously under a possibly non-collaborating environment. Therefore research efforts have focused on scalable, robust, and distributed algorithms for the inference tasks related to target tracking, i.e. localization, data association, and track maintenance. Graphical models provide a rigorous tool for development of such algorithms modeling the information structure of a given task and providing distributed solutions through message passing algorithms. However, the limited communication capabilities and energy resources of sensor networks pose the additional difficulty of considering the trade-off between the communication cost and the accuracy of the result. Also the network structure and the information structure are different aspects of the problem and a mapping between the physical entities and the information structure is needed. In this paper we discuss available formalisms based on graphical models for target tracking in sensor networks with a focus on the aforementioned issues. We point out additional constraints that must be asserted in order to achieve further insight and more effective solutions.

## Bit-Interleaved LDPC-Coded Modulation Suitable for Free-Space Optical Communication over the Atmospheric Turbulence Channel

- **Status**: ❌
- **Reason**: FSO 대기난류 채널 LDPC-coded modulation 응용 특이적; LDPC는 표준 PBD 설계, 떼어낼 새 기법 없음
- **ID**: ieee:4375981
- **Type**: conference
- **Published**: 26-28 Sept
- **Authors**: Ivan B. Djordjevic, Goran T. Djordjevic
- **PDF**: https://ieeexplore.ieee.org/document/4375981
- **Abstract**: We determine the channel capacity of coded repetition MIMO scheme assuming non-ideal p.i.n. photodetection, and the channel is modeled using the statistical model due to Al-Habash et al. The coded repetition MIMO scheme is suitable for communication over the strong atmospheric turbulence channel. The scheme under study employs the Q-ary pulse position modulation and low-density parity-check (LDPC) codes. Component LDPC codes are designed using the concept of pairwise-balanced designs.

## On low density parity check codes for combined reliability and security

- **Status**: ❌
- **Reason**: McEliece 기반 LDPC 암호시스템(보안); 채널 ECC 아님, 보안 도메인 제외
- **ID**: ieee:4401585
- **Type**: conference
- **Published**: 26-28 Sept
- **Authors**: Ackburally Fezal, Soyjaudah Sunjiv
- **PDF**: https://ieeexplore.ieee.org/document/4401585
- **Abstract**: In this manuscript we examine the possibility of using Low Density Parity-Check (LDPC) codes as cryptographic primitive in a Public-Key Cryptosystem (PKC). The designed cryptosystem is based on a modified McEliece scheme and provides for combined reliability and security within one combined algorithm. A model for evaluating its security is then presented. Result shows that our new cryptosystem is at least theoretically more secure than the original McEliece PKC.

## Low density parity check irreducible Goppa codes

- **Status**: ❌
- **Reason**: Goppa 코드(비-LDPC)의 sparse 패리티검사 구성; 부호 특화 구성으로 고전 바이너리 LDPC에 이식 안 됨
- **ID**: ieee:4401460
- **Type**: conference
- **Published**: 26-28 Sept
- **Authors**: Paul F. Kubwalo, John A. Ryan
- **PDF**: https://ieeexplore.ieee.org/document/4401460
- **Abstract**: In this paper, whose earlier version was presented at SAMSA 05 conference, we present some of the results obtained in the on-going research on low density parity check (LDPC) irreducible Goppa codes. The objective of the research is to find irreducible Goppa codes with sparse parity check matrices to which LDPC decoding can be applied. If such codes are found then they would permit efficient encoding and decoding algorithms. We use two methods to come up with a sparse parity check matrix. The first method involves changing the basis of the splitting field of the Goppa polynomial. In the other method, we build the parity check matrix using low weight codewords in the dual code of the Goppa code.

## Performance of sparse graph codes on a four-dimensional CDMA system in AWGN and multipath fading

- **Status**: ❌
- **Reason**: 4D CDMA 통신플랫폼에서 BTC/LDPC/RA 성능비교 응용; LDPC 부수 언급, 떼어낼 새 디코더/구성 없음
- **ID**: ieee:4401523
- **Type**: conference
- **Published**: 26-28 Sept
- **Authors**: Jacobus D. Vlok, Louis P. Linde
- **PDF**: https://ieeexplore.ieee.org/document/4401523
- **Abstract**: This paper presents the uncoded and coded multiuser error performance results of a novel super-orthogonal (SO) 4D CDMA communication platform under AWGN and multi- path fading channel conditions. The communication platform employs a special class of root-of-unity filtered (RUF) constant- envelope (CE) complex spreading sequences (CSS) with zero cross-correlation (ZCC) properties. The uncoded communication platform employs multi-layered-modulation (MLM) to improve spectral efficiency compared with existing multi-level modulation techniques, and the coded system uses the multiple dimensions to transmit redundancy to improve error performance. Three classes of sparse graph coding schemes are evaluated and compared on the multi-dimensional (MD) communication platform. The channel codes include a 3D block-turbo-code (BTC) with extended Reed-Muller (RM) constituent codes, low- density parity-check (LDPC) codes and repeat-accumulate (RA) codes. It is shown that the three channel codes have comparable error performance results and approximately 6 dB performance improvement over BPSK is achieved at Pc(bit) = 1 x 10 -5.

## Generalized LDPC Codes and Turbo-Product Codes with Reed-Muller Component Codes

- **Status**: ❌
- **Reason**: GLDPC + RM/BCH component 디코딩(Walsh-Hadamard MAP)은 일반화된 비-LDPC component 의존; 바이너리 고전 LDPC BP에 그대로 이식 안 됨
- **ID**: ieee:4375955
- **Type**: conference
- **Published**: 26-28 Sept
- **Authors**: Ivan B. Djordjevic
- **PDF**: https://ieeexplore.ieee.org/document/4375955
- **Abstract**: A forward error correction (FEC) scheme based on generalized low-density parity-check (GLDPC) codes can improve overall characteristics of LDPC codes by decreasing the decoding complexity. We consider the GLDPC codes with Reed- Muller (RM) and Bose-Chaudhuri-Hocquenghem (BCH) component codes. GLDPC codes with RM codes as component codes is an attractive option for high-speed applications, such as optical communications, because they provide excellent coding gains, while the RM codes can be decoded using low-complexity maximum a posteriori probability (MAP) decoding algorithm due to Ashikhmin and Lytsin, based on Walsh-Hadamard transform. Several classes of GLDPC codes (with component RM or BCH codes) outperforming the turbo product codes are presented. Several turbo product codes suitable for use in highspeed transmission are identified as well.

## Tornado Codes for MAID Archival Storage

- **Status**: ❌
- **Reason**: Tornado(erasure) LDPC를 MAID 아카이브 파일시스템에 적용한 시스템 논문, 떼어낼 디코더/구성 기법 없는 fountain/erasure 응용
- **ID**: ieee:4367976
- **Type**: conference
- **Published**: 24-27 Sept
- **Authors**: Matthew Woitaszek, Henry M. Tufo
- **PDF**: https://ieeexplore.ieee.org/document/4367976
- **Abstract**: This paper examines the application of Tornado codes, a class of low density parity check (LDPC) erasure codes, to archival storage systems based on massive arrays of idle disks (MAID). We present a log- structured extent-based archival file system based on Tornado Coded stripe storage. The file system is combined with a MAID simulator to emulate the behavior of a large-scale storage system with the goal of employing Tornado Codes to provide fault tolerance and performance in a power-constrained environment. The effect of power conservation constraints on system throughput is examined, and a policy of placing multiple data nodes on a single device is shown to increase read throughput at the cost of a measurable, but negligible, decrease in fault tolerance. Finally, a system prototype is implemented on a 100 TB Lustre storage cluster, providing GridFTP accessible storage with higher reliability and availability than the underlying storage architecture.

## An enhanced very high data rate UWB airinterface based on the WIMEDIA standard - An European View -

- **Status**: ❌
- **Reason**: UWB OFDM 무선 에어인터페이스 표준화 논문, LDPC 언급 없음, 떼어낼 ECC 기법 없음
- **ID**: ieee:4380979
- **Type**: conference
- **Published**: 24-26 Sept
- **Authors**: Friedbert Berens, Emil Dimitrov, Thomas Kaiser +3
- **PDF**: https://ieeexplore.ieee.org/document/4380979
- **Abstract**: The existing UWB standard based on OFDM developed by the WIMEDIA industrial consortium can support data rates up to 480 MBit/s for a distance of up to 2m. The initial focus and key application driver of the WIMEDIA standard implementation will be the replacement of USB 2 cables in PC peripherals using the certified wireless USB protocol. Typical usage scenarios for this implementation will be the connection of a PC to hard disk drives, digital cameras, printers, etc. For future deployments of UWB technologies in multimedia and network centric consumer electronics applications higher data rates are needed. The goal of work package WP2a in the PULSERS II project is the definition and evaluation of an air interface and the corresponding building blocks that can provide data rates in the range 3GBit/s over a distance of around 2m. In order to achieve this goal the OFDM based air interface of the WIMEDIA system will be upgraded in an evolutionary manner with strong considerations for the backward compatibility of the future devices. This paper will give an overview of the state of the definition of this enhanced air-interface developed in the PULSERS II project. The concepts and the evaluation results coming out of this activity should be used as an input to the future standardization activities in the WIMEDIA group starting in 2007 with an initial step towards a IGbit/s enhancement of the air interface.

## Consideration of fast simulation technique of LDPC code

- **Status**: ❌
- **Reason**: LDPC BER 고속 시뮬레이션 추정 기법, 디코더/HW/코드설계 기여 아님, 순수 평가 방법론
- **ID**: ieee:4408338
- **Type**: conference
- **Published**: 23-27 Sept
- **Authors**: Toshiyuki Shohon, Yasunori Hori, Haruo Ogiwara
- **PDF**: https://ieeexplore.ieee.org/document/4408338
- **Abstract**: This paper proposes a method to estimate bit-error rate (BER) at high signal-to-noise ratio. The computer simulation result of the proposed method shows good agreement with those of the original Monte Carlo (MC) simulations. By using the proposed method, the number of bits needed to computer simulation is reduced to 50% of the MC simulation for code length 1027[bit], It is reduced to 20% compared with the MC simulation for code length 4000[bit], The time to estimate BER for the proposed method is reduced to 60% of original envelop method.

## An Internally Adaptive LDPC Coded Ultra Wideband-Impulse Radio System

- **Status**: ❌
- **Reason**: UWB-IR 응용 특이적 적응 LDPC 코드율 선택 시스템, 떼어낼 일반 ECC 기법 없음
- **ID**: ieee:4408394
- **Type**: conference
- **Published**: 23-27 Sept
- **Authors**: Jianhua Yang, Danfeng Zhao, Chunhui Zhao +1
- **PDF**: https://ieeexplore.ieee.org/document/4408394
- **Abstract**: In this paper, we propose an internally adaptive LDPC coded ultra wideband-impulse radio (IALC-UWB-IR) system which is able to adaptively select the code rate of the LDPC code and the number of pulse repetitions. Performance of the proposed system is evaluated under the UWB multipart channel proposed in the IEEE 802.15.3a standard, and the selective-RAKE receiver with maximal radio combining is used. Simulation result shows that the proposed 1ALC-UWB-IR system significantly outperforms the conventional UWB-1R systems.

## Optimization of LDPC Codes for Turbo Equalization Based on PSO-EXIT Algorithm

- **Status**: ❌
- **Reason**: turbo equalization용 LDPC degree distribution을 PSO-EXIT로 최적화, 채널 특이적 EXIT 최적화라 NAND 이식성 낮음
- **ID**: ieee:4340129
- **Type**: conference
- **Published**: 21-25 Sept
- **Authors**: Hua Xu
- **PDF**: https://ieeexplore.ieee.org/document/4340129
- **Abstract**: Optimization of LDPC codes based on EXIT chart of MIMO channel is recently proposed by Brink. In this paper, Brink's idea is extended to optimization of LDPC codes for MMSE turbo equalization.First ,a new method to obtain EXIT curves of the receiver was given. Furthermore ,a new optimized scheme of LDPC codes for turbo equalization, PSO-EXIT algorithm, was proposed, which combined He's modified Particle swarm optimization(PSO) algorithm with EXIT chart method. Decoding trajectory of (3,6)regular LDPC codes for MMSE turbo equalization was also analyzed in this paper.The degree distribution pair of the optimized irregular LDPC codes were compared with the result of Narayanan's. Simulation results shows that the proposed scheme is effective.

## Linear Time Encoding of Low-Density Parity Check Codes and its Performance in Weak Atmospheric Turbulent Channels

- **Status**: ❌
- **Reason**: 표준 RU 선형시간 인코딩을 광 대기난류 채널에 적용; 새 기법 없는 응용특이 논문
- **ID**: ieee:4340507
- **Type**: conference
- **Published**: 21-25 Sept
- **Authors**: Jiajie Chen, Xiaofeng Li, Yanhui Liu
- **PDF**: https://ieeexplore.ieee.org/document/4340507
- **Abstract**: A major drawback of low-density parity -check (LDPC) Codes is their apparently high encoding complexity and consequent encoding delay. A linear time encoding method proposed by Richardson and Urbanke can effectively reduce the encoding complexity to only linear encoding complexity. In this paper, LDPC codes based on the linear time encoding method is adopted for improving the bit-error rate (BER) performance of an on-off keying (OOK) modulated optical signal through a weak atmosphere turbulence channel. The optical atmosphere channel is modeled as a stationary ergodic channel with lognormal intensity fading. We simulate and analyze the BER performance of the channel using the linear time encoding method. Simulation results show that the presented encoding method can be greatly reduce the BER Moreover, as the code length increases or code rate decreases, the coding gain of LDPC codes over the uncoded system becomes large. Therefore, the presented encoding method with both large code length and low code rate obtain high encode gain for the optical atmosphere turbulence channel.

## An Adaptive LDPC-Coded MIMO-OFDM System Based on Statistical Channel State Information

- **Status**: ❌
- **Reason**: 통계적 CSI 기반 적응형 MIMO-OFDM 시스템, LDPC는 부수 사용, 떼어낼 ECC 기법 없음
- **ID**: ieee:4339829
- **Type**: conference
- **Published**: 21-25 Sept
- **Authors**: Yi Hui, Zhijie Zhou, Wenqiang Zhang +2
- **PDF**: https://ieeexplore.ieee.org/document/4339829
- **Abstract**: An adaptive MIMO OFDM system using QAM and LDPC code is proposed with only two parameters required to be sent to the transmitter, which are the mean and the variance. Simulation shows that the proposed system can outperform the other similar systems.

## Accurate Union-Bound for LDPC Block Codes Concatenated with Linear Dispersion Block Codes

- **Status**: ❌
- **Reason**: LDPC+dispersion concatenation의 ML union-bound 성능분석만; 떼어낼 디코더/HW/구성 기법 없음(순수 bound)
- **ID**: ieee:4340134
- **Type**: conference
- **Published**: 21-25 Sept
- **Authors**: A. Kora, J. P. Cances, V. Meghdadi
- **PDF**: https://ieeexplore.ieee.org/document/4340134
- **Abstract**: The use of turbo-like codes, such as LDPC or turbo codes, over the MIMO channel has recently gained significant interests. In this paper, a computationally efficient maximum- likelihood union-bound framework is proposed for the analysis of the concatenated coding scheme. Our method provides efficient and fast union bound analysis framework.

## LDPC Coded Irregular Modulation Based on Degree Distribution

- **Status**: ❌
- **Reason**: irregular modulation 매핑 최적화(link adaptation), 변조-부호 매핑 기법이라 채널 ECC 디코더·구성 기여 아님
- **ID**: ieee:4340000
- **Type**: conference
- **Published**: 21-25 Sept
- **Authors**: Minli Jia, Zunwen He, Jingming Kuang +1
- **PDF**: https://ieeexplore.ieee.org/document/4340000
- **Abstract**: A novel irregular low density parity check (LDPC) coded link adaptation technique is presented to achieve flexible spectral efficiency and various reliabilities with irregular modulation. The mapping rule between LDPC coded bits and signal constellations is optimized in terms of LDPC code degree distribution and inherent unequal error protection property of irregular modulation. Simulation results show that the combination of various modulations can achieve not only fine data rate adaptation, but also better bit error rate (BER) performance with optimized mapping rule. Convergence performance is also analyzed using extrinsic information transfer (EXIT) chart based on actual probability dense function of extrinsic information by Monte Carlo simulations.

## Gaussian Approximation for LDPC Codes

- **Status**: ❌
- **Reason**: 정규 LDPC threshold 추정용 Gaussian Approximation(밀도진화 분석 도구)일 뿐, 신규 디코더/구성/HW 기여 없음
- **ID**: ieee:4340139
- **Type**: conference
- **Published**: 21-25 Sept
- **Authors**: S. Asoodeh, H. Ramezani, H. Samimi
- **PDF**: https://ieeexplore.ieee.org/document/4340139
- **Abstract**: Today, LDPC codes have become one of the hottest topics in coding theory. Unlike many other classes of cods LDPC codes are already equipped with very fast (probabilistic) encoding and decoding algorithm. The decoding of LDPC codes are implemented through message-passing algorithm. Passed messages can be modeled as Gaussian variables. In this paper, the new approximate method for calculation of statistical parameters of these Gaussian variables is proposed. Based on proposed method, we can be able to estimate the threshold level of noise of regular LDPC codes over AWGN channels.

## LDPC Coded Link Adaptation Based on Irregular Modulation Integrated with Full Incremental Redundancy

- **Status**: ❌
- **Reason**: irregular modulation+HARQ link adaptation, LDPC는 베이스라인 부호, 떼어낼 디코더·구성 기법 없음
- **ID**: ieee:4340131
- **Type**: conference
- **Published**: 21-25 Sept
- **Authors**: Minli Jia, Zunwen He, Jingming Kuang +1
- **PDF**: https://ieeexplore.ieee.org/document/4340131
- **Abstract**: The irregular modulation (IM) technique was initially proposed in bit-interleaved coded modulation (BICM) for convolutional code and turbo code cases (Schreckenbach and Bauch, 2006), which apply different signal constellations and mappings within one codeword. The IM technique gives a simple method to improve flexibility of BICM, which can also provide an adaptive modulation with fine granularity. We combine the IM and low density parity check (LDPC) coded full incremental redundancy (FIR) hybrid automatic repeat request (HARQ) to propose a novel link adaptation method-"IM_FIR". Simulation results show that the "IM_FIR" can not only achieve higher throughput efficiency but also significantly reduce transmission delay than the LDPC coded regular modulation with FIR schemes. Furthermore, an adaptive IM with FIR scheme is presented, which can adaptively select proper IM strategies to get highest throughput in accordance with variations of the channel conditions.

## An Improved Decoding Method for LDPC Codes in SC-FDE System

- **Status**: ❌
- **Reason**: SC-FDE 시스템에서 CP 손실 보상 위한 디코딩 개선, CP 선택 알고리즘이 핵심이라 NAND 이식 불가 무선 특이적
- **ID**: ieee:4339961
- **Type**: conference
- **Published**: 21-25 Sept
- **Authors**: Ying-Hao Qi, Pei-Wei Huang, Meng-Tian Rong
- **PDF**: https://ieeexplore.ieee.org/document/4339961
- **Abstract**: Single carrier transmission with cyclic prefix (SC-CP or SC-FDE), has been adopted in wireless applications as an alternative technique to orthogonal frequency division multiplexing (OFDM). In this paper, an improved decoding method for regular low density parity check (LDPC) codes is proposed to compensate for the loss in signal-to-noise (SNR) due to the CP insertion. According to our research, the algorithm to select suitable CP plays an important role in decoding. The performance of the uncoded case is well analyzed. Simulation results show that the proposed scheme is effective under both AWGN and Rayleigh fading channels.

## Soft-Decision RS Decoding Algorithm and Its DSP Implementation in DSSS Systems

- **Status**: ❌
- **Reason**: RS 소프트디시전 Chase 디코딩·DSP 구현, 비-LDPC 부호이고 부호 의존적이라 BP 이식 불가
- **ID**: ieee:4340096
- **Type**: conference
- **Published**: 21-25 Sept
- **Authors**: Xiang Yuan Bu, Pei-Pei Zhu
- **PDF**: https://ieeexplore.ieee.org/document/4340096
- **Abstract**: A soft-decision Reed-Solomon(RS) decoding algorithm is introduced. Chase algorithm is employed and an improved Chase algorithm is presented. Hard-decision and soft-decision decoding are tested under Additive White Gaussian Noise(AWGN) channel using BPSK. Simulation results show that larger coding gain is obtained by using soft-decision decoding and the tradeoff between error performance and decoding complexity using improved Chase algorithm is provided. Finally, DSP implementation scheme of soft-decision RS decoder in Direct Sequence Spread Spectrum(DSSS) systems is proposed.

## AMC-HARQ System Baded On RC-LDPC Codes in MIMO Channels

- **Status**: ❌
- **Reason**: RC-LDPC를 베이스라인으로 한 AMC-HARQ 크로스레이어 처리율 설계, 새 디코더/HW/코드설계 없음 무선응용 특이적
- **ID**: ieee:4379061
- **Type**: conference
- **Published**: 20-21 Sept
- **Authors**: Changchun Li, Yuling Zhang, Dongfeng Yuan +1
- **PDF**: https://ieeexplore.ieee.org/document/4379061
- **Abstract**: In this paper, we propose a cross-layer design framework combining adaptive modulation and coding (AMQ) with hybrid automatic repeat request (HARQ) based on rate-compatible low-density parity-check codes (RC-LDPC) in multiple-input multiple-output (MIMO) fading channels with estimation errors. We derive the expressions for the throughput of the system and investigated the effect of channel estimation errors on the system throughput. Numerical results show that the joint design of AMC and ARQ based on RC-LDPC codes can achieve considerable spectral efficiency gain.

## Design of Nonbinary Quasi-Cyclic LDPC Cycle Codes

- **Status**: ❌
- **Reason**: 비이진 QC-LDPC cycle code 설계(GF(q)) — 비이진 LDPC는 제외 대상
- **ID**: ieee:4313042
- **Type**: conference
- **Published**: 2-6 Sept. 
- **Authors**: Rong-Hui Peng, Rong-Rong Chen
- **PDF**: https://ieeexplore.ieee.org/document/4313042
- **Abstract**: In this paper, we study the design of nonbinary low-density parity-check (LDPC) cycle codes over Galois field GF(q). First, we construct a special class of nonbinary LDPC cycle codes with low error floors. Our construction utilizes the cycle elimination algorithm to remove short cycles in the normal graph and to select nonzero elements in the parity-check matrix to reduce the number of low-weight codewords generated by short cycles. Furthermore, we show that simple modifications of such codes are parallel sparse encodable (PSE). The PSE code, consisting of a quasi-cyclic (QC) LDPC cycle code and a simple tree code, has the attractive feature that it is not only linearly encodable, but also allows parallel encoding which can reduce the encoding time significantly. We provide a systematic comparison between nonbinary coded systems and binary coded systems. For the MIMO channel considered, our results show that the proposed nonbinary system employing the PSE code outperforms not only the binary LDPC code specified in the 802.16e standard, but also the optimized binary LDPC code obtained using the EXIT chart methods.

## Iterative Coded Pulse-Position-Modulation for Deep-Space Optical Communications

- **Status**: ❌
- **Reason**: deep-space optical PPM 결합 코딩(SCPPM/LDPC-PPM) — LDPC가 변조 결합 베이스라인, 떼어낼 신규 ECC 기법 없음
- **ID**: ieee:4313051
- **Type**: conference
- **Published**: 2-6 Sept. 
- **Authors**: Maged F. Barsoum, Bruce Moision, Michael Fitz +2
- **PDF**: https://ieeexplore.ieee.org/document/4313051
- **Abstract**: This paper presents and compares two iterative coded modulation techniques for deep-space optical communications using pulse-position modulation (PPM). The first code, denoted by SCPPM, consists of the serial concatenation of an outer convolutional code, an interleaver, a bit accumulator, and PPM. The second code, denoted by LDPC-PPM, consists of the serial concatenation of an LDPC code and PPM. We employ Extrinsic Information Transfer (EXIT) charts for their analysis and design. Under conditions typical of a communications link from Mars to Earth, SCPPM is 1 dB away from capacity, while LDPC-PPM is 1.4 dB away from capacity, at a Bit Error Rate (BER) of approximately 10-5. However, LDPC-PPM lends itself naturally to low latency parallel processing in contrast to SCPPM.

## Lower bounds on the rate-distortion function of LDGM codes

- **Status**: ❌
- **Reason**: LDGM 손실 소스코딩 rate-distortion 하한 — 채널 ECC 아닌 소스코딩 이론 bound, 떼어낼 디코더/HW 없음
- **ID**: ieee:4313151
- **Type**: conference
- **Published**: 2-6 Sept. 
- **Authors**: A. G. Dimakis, M. J. Wainwright, K. Ramchandran
- **PDF**: https://ieeexplore.ieee.org/document/4313151
- **Abstract**: We analyze the performance of low-density generator matrix (LDGM) codes for lossy source coding. We first develop a generic technique for deriving lower bounds on the effective rate-distortion functions of binary linear codes. This result provides a source coding analog of a classical result due to Gallager for channel coding over the binary symmetric channel. We illustrate this method for the ensemble of check-regular low- density generator matrix (LDGM) codes by deriving an explicit lower bound on its rate-distortion performance as a function of the check degree.

## Analysis of the Distribution of the Number of Correctable Erasures for Turbo Codes with DRP Interleavers

- **Status**: ❌
- **Reason**: 터보 부호 DRP 인터리버의 erasure 성능 분석, 비-LDPC이며 떼어낼 LDPC BP 기법 없음
- **ID**: ieee:4313076
- **Type**: conference
- **Published**: 2-6 Sept. 
- **Authors**: M. Ambroze, M. Tomlinson, C. Tjhai +1
- **PDF**: https://ieeexplore.ieee.org/document/4313076
- **Abstract**: This paper investigates the maximum likelihood (ML) performance of turbo codes employing dithered relative prime (DRP) interleavers for the erasure channel. The performance is analysed by determining the distribution of correctable erasures based on the weight distribution of the code. A degradation from optimal maximum distance separable (MDS) performance or MDS shortfall is defined and determined for DRP and S-random interleavers. It is shown that the MDS shortfall is less than 4 bits on average for short turbo codes and is reduced to less than 3 bits by using DRP interleavers. The ML decoder error rate performance is determined for the turbo codes and compared to the best known linear code of the same block length and code rate, and also compared to a hypothetical binary MDS code. Given the constraints of turbo codes the DRP interleaver is shown to have good performance and is considerably better than the S-random interleaver turbo code.

## Bounds on the Tradeoff Between Decoding Complexity and Rate for Sparse-Graph Codes

- **Status**: ❌
- **Reason**: sparse-graph 부호의 복잡도-rate 트레이드오프 하한 — 순수 이론 bound, 디코더/HW/구성으로 안 이어짐
- **ID**: ieee:4313073
- **Type**: conference
- **Published**: 2-6 Sept. 
- **Authors**: Pulkit Grover
- **PDF**: https://ieeexplore.ieee.org/document/4313073
- **Abstract**: Khandekar and McEliece suggested the problem of per bit decoding complexity for capacity achieving sparse-graph codes as a function of their gap from the channel capacity. We consider the problem for the case of the binary symmetric channel. We derive a lower bound on this complexity for some codes on graphs for Belief Propagation decoding. For bounded degree LDPC and LDGM codes, any concatenation of the two, and punctured bounded-degree LDPC codes, this reduces to a lower bound of O (log (1/isin-)). The proof of this result leads to an interesting necessary condition on the code structures which could achieve capacity with bounded decoding complexity over BSC: the average edge-degree must converge to infinity while the average node-degree must be bounded. That is, one of the node degree distributions must have a finite mean and an infinite variance.

## Adding a Rate-1 Third Dimension to Turbo Codes

- **Status**: ❌
- **Reason**: turbo code에 rate-1 3차원 추가로 MHD 향상 — turbo 부호 특이적, 바이너리 LDPC BP로 이식할 디코더 기법 없음
- **ID**: ieee:4313066
- **Type**: conference
- **Published**: 2-6 Sept. 
- **Authors**: C. Berrou, A. Graell i Amat, Y. Ould Cheikh Mouhamedou +2
- **PDF**: https://ieeexplore.ieee.org/document/4313066
- **Abstract**: Thanks to the message passing principle, turbo decoding is able to provide strong error correction near the theoretical (Shannon) limit. However, the minimum Hamming distance (MHD) of a turbo code may not be sufficient to prevent a detrimental change in the error rate vs. signal to noise ratio curve, the so-called flattening. Increasing the MHD of a turbo code may involve using component encoders with a large number of states, devising more sophisticated internal permutations, or increasing the dimension of the turbo code, i.e. the number of component encoders. This paper addresses the latter option and proposes a modified turbo code, in which some of the parity bits stemming from the classical component encoders are encoded by a rate-1, third encoder. The result is a significantly increased MHD, which improves turbo decoder performance at low error rates, at the expense of a very small increase in complexity. In this paper, we compare the performance of the proposed turbo code with that of the DVB-RCS turbo code and the DVB-S2 LDPC code. Comparisons with more complex 16-state TCs are also reported.

## Secure Nested Codes for Type II Wiretap Channels

- **Status**: ❌
- **Reason**: Type II wiretap 보안 nested code 설계, 보안 응용이며 NAND ECC로 이식할 디코더/구성 기법 없음
- **ID**: ieee:4313097
- **Type**: conference
- **Published**: 2-6 Sept. 
- **Authors**: Ruoheng Liu, Yingbin Liang, H. Vincent Poor +1
- **PDF**: https://ieeexplore.ieee.org/document/4313097
- **Abstract**: This paper considers the problem of secure coding design for a type II wiretap channel, where the main channel is noiseless and the eavesdropper channel is a general binary-input symmetric-output memoryless channel. The proposed secure error-correcting code has a nested code structure. Two secure nested coding schemes are studied for a type II Gaussian wiretap channel. The nesting is based on cosets of a good code sequence for the first scheme and on cosets of the dual of a good code sequence for the second scheme. In each case, the corresponding achievable rate-equivocation pair is derived based on the threshold behavior of good code sequences. The two secure coding schemes together establish an achievable rate-equivocation region, which almost covers the secrecy capacity-equivocation region in this case study. The proposed secure coding scheme is extended to a type II binary symmetric wiretap channel. A new achievable perfect secrecy rate, which improves upon the previously reported result by Thangaraj et al., is derived for this channel.

## Image Encryption and Data Hiding: Duality and Code Designs

- **Status**: ❌
- **Reason**: 이미지 암호화/데이터 은닉의 부호설계 쌍대성, LDPC는 부수 사용이고 보안/소스 응용으로 떼어낼 ECC 기법 없음
- **ID**: ieee:4313090
- **Type**: conference
- **Published**: 2-6 Sept. 
- **Authors**: Yang Yang, Vladimir Stankovic, Zixiang Xiong
- **PDF**: https://ieeexplore.ieee.org/document/4313090
- **Abstract**: We analyze duality in code design between encryption and data hiding problems. First we point out dual operations of the encoder/decoder pairs of the two problems, and then, we apply the developed duality principle to practical image communication. Using the same image DCT coefficients as side information for both problems, practical code designs based on trellis quantization and LDPC codes are then provided. Under the same simulation condition, the performance of the two practical designs show consistency with each other, hence validating the coding duality between the two problems.

## Efficient Compressive Sensing with Deterministic Guarantees Using Expander Graphs

- **Status**: ❌
- **Reason**: expander 그래프 기반 compressive sensing 복원, 채널코딩 ECC가 아닌 신호복원으로 떼어낼 LDPC 디코더 기법 없음
- **ID**: ieee:4313110
- **Type**: conference
- **Published**: 2-6 Sept. 
- **Authors**: Weiyu Xu, Babak Hassibi
- **PDF**: https://ieeexplore.ieee.org/document/4313110
- **Abstract**: Compressive sensing is an emerging technology which can recover a sparse signal vector of dimension n via a much smaller number of measurements than n. However, the existing compressive sensing methods may still suffer from relatively high recovery complexity, such as O(n3), or can only work efficiently when the signal is super sparse, sometimes without deterministic performance guarantees. In this paper, we propose a compressive sensing scheme with deterministic performance guarantees using expander-graphs-based measurement matrices and show that the signal recovery can be achieved with complexity O(n) even if the number of nonzero elements k grows linearly with n. We also investigate compressive sensing for approximately sparse signals using this new method. Moreover, explicit constructions of the considered expander graphs exist. Simulation results are given to show the performance and complexity of the new method.

## Nonlinear Sparse-Graph Codes for Lossy Compression of Discrete Nonredundant Sources

- **Status**: ❌
- **Reason**: sparse-graph 부호의 손실 압축(소스 코딩), 채널코딩 ECC가 아님
- **ID**: ieee:4313132
- **Type**: conference
- **Published**: 2-6 Sept. 
- **Authors**: Ankit Gupta, Sergio Verdu
- **PDF**: https://ieeexplore.ieee.org/document/4313132
- **Abstract**: We propose a scheme to implement lossy data compression for discrete equiprobable sources using block codes based on sparse matrices. We prove asymptotic optimality of the codes for a Hamming distortion criterion. We also present a sub-optimal decoding algorithm, which has near optimal performance for moderate blocklengths.

## Erasure-Burst and Error-Burst Decoding of Linear Codes

- **Status**: ❌
- **Reason**: erasure/error-burst 채널용 반복 디코딩 행렬 설계 — erasure 중심, NAND 바이너리 BP로 떼어낼 신규 기법 미약
- **ID**: ieee:4313062
- **Type**: conference
- **Published**: 2-6 Sept. 
- **Authors**: Shumei Song, Shu Lin, Khaled Abdel-Ghaffar +1
- **PDF**: https://ieeexplore.ieee.org/document/4313062
- **Abstract**: Iterative algorithms for decoding over erasure-burst channels have attracted much interest lately due to their simplicity. Although the performance of these techniques is typically good, it may not be optimal if the underlying matrix used for decoding is not properly chosen. In this paper, we construct matrices that lead to optimal performance when used with iterative decoding over erasure-burst channels. We also develop a simple decoding technique that makes use of these same matrices to decode any linear code over error-burst channels. For cyclic codes, this algorithm is optimal.

## The Maximum A Posteriori Decoding Using Variational Bayes Methods for Digital Magnetic Recording Channels

- **Status**: ❌
- **Reason**: 자기기록채널 VB 기반 MAP 검출기(컬러/전이잡음 추정), LDPC ECC 디코더 아님 채널검출 기법
- **ID**: ieee:4313041
- **Type**: conference
- **Published**: 2-6 Sept. 
- **Authors**: Hidetoshi Saito, Masayuki Hayashi, Ryuji Kohno
- **PDF**: https://ieeexplore.ieee.org/document/4313041
- **Abstract**: In this paper, we present new maximum a posteriori (MAP) decoding based on the variational base (VB) method in digital magnetic recording channels with colored Gaussian noise and transition noise. Multivariate autoregressive (AR) models is used for an inference model for the mixture noise sources. Noise estimating in the MAP detector uses the VB method of the AR mixtures. It is shown that the proposed MAP detector is effective to estimate signal sequences degraded by the mixture noise sources and improve the bit error rate (BER) performances.

## Achieving the Rate-Distortion Bound with Linear Codes

- **Status**: ❌
- **Reason**: 선형코드의 rate-distortion bound 달성(소스코딩) — 채널 ECC 아님, 큰 유한체 기반 비이진
- **ID**: ieee:4313153
- **Type**: conference
- **Published**: 2-6 Sept. 
- **Authors**: Jun Chen, Da-ke He, Ashish Jagmohan
- **PDF**: https://ieeexplore.ieee.org/document/4313153
- **Abstract**: We show that linear codes can achieve the rate- distortion bound of a discrete memoryless source with arbitrary distortion measure if the size of finite field is sufficiently large. An alternative approach based on multilevel quantization is proposed. The optimality of this approach and the sufficiency of binary linear codes are established. Linear codes are also shown to be able to achieve a simplified version of the El Gamal-Cover (EGC) region for multiple description coding.

## Experimental Demonstration of PMD Compensation by LDPC-Coded Turbo Equalization

- **Status**: ❌
- **Reason**: LDPC-coded turbo equalization으로 광통신 PMD 보상 실험. 떼어낼 NAND용 디코더/구성 기법 없는 응용 시연
- **ID**: ieee:5758492
- **Type**: conference
- **Published**: 16-20 Sept
- **Authors**: Ivan B. Djordjevic, Hussam G. Batshon, Lyubomir L. Minkov +5
- **PDF**: https://ieeexplore.ieee.org/document/5758492
- **Abstract**: The possibility of PMD compensation by using LDPC-coded turbo equalization is demonstrated experimentally for NRZ systems operating at 10-Gb/s. Significant BER performance improvement over the optimum threshold receiver is obtained.

## Some Remarks on Sparse Graph Codes for Packet Loss Recovery

- **Status**: ❌
- **Reason**: G-LDPC(generalized LDPC) protograph 설계지만 erasure channel용 패킷손실복구로 채널 ECC 아닌 erasure 영역이고 떼어낼 신규 NAND 이식 기법 불명확
- **ID**: ieee:4409408
- **Type**: conference
- **Published**: 13-14 Sept
- **Authors**: Gianluigi Liva, Marco Chiani, Matteo Berioli +1
- **PDF**: https://ieeexplore.ieee.org/document/4409408
- **Abstract**: In this paper we provide some novel design techniques for sparse-graph-based erasure correcting codes. The paper is focused on codes based on sparse graph belonging to the category of the so-called generalized low-density parity-check (G-LDPC) codes. Some design insights are provided for multi-edge type G-LDPC codes based on protographs. The performance assessment of some G-LDPC codes is carried out by use of both simulation and analytic tools, showing the capacity-approaching performance of the presented code designs on the uncorrelated binary erasure channel.

## Soft Demapping and Turbo Decoding for Satellite Broadcasting Communications

- **Status**: ❌
- **Reason**: 위성방송용 turbo 부호+소프트 디매핑/반복복조 수신기로 LDPC를 대체한 응용 논문; 바이너리 LDPC BP에 이식할 부호 비의존적 디코더 기법 없음 (비-LDPC 원칙 제외)
- **ID**: ieee:4409397
- **Type**: conference
- **Published**: 13-14 Sept
- **Authors**: Rosalba Suffritti, Enrico del Re, Simone Morosi
- **PDF**: https://ieeexplore.ieee.org/document/4409397
- **Abstract**: In this paper an original detection strategy for satellite digital broadcasting communications is defined; particularly, we consider a system derived from the DVB-S2 standard, which has been proposed as a development of the DVB-S system and exploits an iterative decoding and higher order modulations. The proposed approach relies on the use of the information which can be obtained by proper soft demapping schemes and on the use of the Turbo codes instead of the LDPC (Low Density Parity Check) codes required by the standard. Moreover, an original receiver which is based on iterative demapping and decoding, is introduced. The adoption of this strategy can permit a remarkable performance gain and an improvement of the system throughput.
