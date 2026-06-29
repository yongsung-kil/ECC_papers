# IEEE Xplore — 2005-10


## Nonbinary LDPC codes for optical communication systems

- **Status**: ❌
- **Reason**: 비이진(nonbinary) LDPC 부호로 명시적 제외 대상
- **ID**: ieee:1512327
- **Type**: journal
- **Published**: Oct. 2005
- **Authors**: I.B. Djordjevic, B. Vasic
- **PDF**: https://ieeexplore.ieee.org/document/1512327
- **Abstract**: We propose a class of moderate-length nonbinary low-density parity-check (LDPC) codes for long-haul high-speed optical transmission systems. In particular, we present an LDPC code with 12.59% redundancy that achieves a 9.9-dB coding gain at a bit-error rate of 10/sup -10/. A similar coding gain is obtained for a long nonbinary LDPC code with a redundancy of only 6.7%.

## Low-density parity-check matrices for coding of correlated sources

- **Status**: ❌
- **Reason**: 상관 소스 코딩용 LDPC 행렬 — 채널 ECC가 아닌 소스코딩(Slepian-Wolf류) 제외
- **ID**: ieee:1512435
- **Type**: journal
- **Published**: Oct. 2005
- **Authors**: J. Muramatsu, T. Uyematsu, T. Wadayama
- **PDF**: https://ieeexplore.ieee.org/document/1512435
- **Abstract**: Linear codes for a coding problem of correlated sources are considered. It is proved that we can construct codes by using low-density parity-check (LDPC) matrices with maximum-likelihood (or typical set) decoding. As applications of the above coding problem, a construction of codes is presented for multiple-access channel with correlated additive noises and a coding theorem of parity-check codes for general channels is proved.

## Integrated interleaving error correcting code and high-dimensional parity codes

- **Status**: ❌
- **Reason**: 인터리빙 통합 ECC + 고차원 패리티 — 비-LDPC 인터리빙/패리티 부호, 떼어낼 바이너리 LDPC 기법 없음
- **ID**: ieee:1519175
- **Type**: journal
- **Published**: Oct. 2005
- **Authors**: H. Kamabe, H. Katou
- **PDF**: https://ieeexplore.ieee.org/document/1519175
- **Abstract**: The integrated interleaving error correcting scheme is a coding scheme for combining codes with different error correcting capabilities. This method is applied to channels in which a data sequence is interleaved, e.g., magnetic recording channels. We propose a decoding method which enhances the error correcting capability of the scheme. By using the method, we can correct more errors which occur in retrieved data sequences.

## Decoding for magnetic recording media with overlapping tracks

- **Status**: ❌
- **Reason**: 자기기록 트랙오버랩 ITI에 MMSE 등화+LDPC 결합, 표준 LDPC 베이스라인일 뿐 떼어낼 새 디코더/코드설계 기법 없음
- **ID**: ieee:1519176
- **Type**: journal
- **Published**: Oct. 2005
- **Authors**: N. Singla, J.A. O'Sullivan, C.T. Miller +1
- **PDF**: https://ieeexplore.ieee.org/document/1519176
- **Abstract**: Increasing recording track density by allowing overlap of adjacent tracks can lead to a substantial increase in storage density for magnetic recording. However, track overlap may cause severe intertrack interference (ITI) and result in loss of performance. Sophisticated signal processing techniques must then be used to recover this loss. We study the use of joint equalization and decoding for magnetic recording with overlapping tracks. We present results for a scheme that uses minimum mean-squared-error (MMSE) equalization in conjunction with error-correction coding using low-density parity-check (LDPC) codes. The recording process is simulated using a micromagnetic model for longitudinal magnetic recording. We use a three-track system to study the track overlap. The outer two tracks are allowed to overlap on the middle track to simulate ITI. Bit-error rate simulations show that the MMSE-LDPC decoding scheme incurs negligible loss when each of the outer tracks overlaps 10% on the middle track. By varying the recording parameters, the tradeoff between storage density and performance is also studied. We show that by a judicious choice of LDPC codes, a recording with track overlap can have better performance than when there is no overlap. Hence, a higher storage density can be obtained without loss in performance.

## Detection of media defects in perpendicular magnetic recording channels

- **Status**: ❌
- **Reason**: 자기기록 매체 결함 검출(진폭 임계) — 검출 알고리즘, LDPC 디코더 기법 아님
- **ID**: ieee:1519172
- **Type**: journal
- **Published**: Oct. 2005
- **Authors**: W. Tan, J.R. Cruz
- **PDF**: https://ieeexplore.ieee.org/document/1519172
- **Abstract**: Two new algorithms for detection of media defects in perpendicular magnetic recording channels are proposed. These algorithms are based on amplitude thresholding of the channel reliability information. The performance of these algorithms is evaluated for low-density parity-check coded channels using generalized partial response targets with different dc-components.

## DC-free error-control block codes

- **Status**: ❌
- **Reason**: DC-free + EC 통합 부호 — 주로 BCH/RS/RM, LDPC는 한 사례일 뿐, 제약코딩 중심으로 신규 LDPC 기여 없음
- **ID**: ieee:1516280
- **Type**: journal
- **Published**: Oct. 2005
- **Authors**: Fengqin Zhai, Yan Xin, I.J. Fair
- **PDF**: https://ieeexplore.ieee.org/document/1516280
- **Abstract**: DC-free codes and error-control (EC) codes are widely used in digital transmission and storage systems. To improve system performance in terms of code rate, bit-error rate (BER), and low-frequency suppression, and to provide a flexible tradeoff between these parameters, this paper introduces a new class of codes with both dc-control and EC capability. The new codes integrate dc-free encoding and EC encoding, and are decoded by first applying standard EC decoding techniques prior to dc-free decoding, thereby avoiding the drawbacks that arise when dc-free decoding precedes EC decoding. The dc-free code property is introduced into standard EC codes through multimode coding techniques, at the cost of minor loss in BER performance on the additive white Gaussian noise channel, and some increase in implementation complexity, particularly at the encoder. This paper demonstrates that a wide variety of EC block codes can be integrated into this dc-free coding structure, including binary cyclic codes, binary primitive BCH codes, Reed-Solomon codes, Reed-Muller codes, and some capacity-approaching EC block codes, such as low-density parity-check codes and product codes with iterative decoding. Performance of the new dc-free EC block codes is presented.

## Noise-predictive turbo equalization for partial-response channels

- **Status**: ❌
- **Reason**: 노이즈 예측 터보 이퀄라이제이션 — PR 채널 이퀄라이저, LDPC는 오버레이일 뿐 떼어낼 LDPC 디코더 기법 없음
- **ID**: ieee:1519173
- **Type**: journal
- **Published**: Oct. 2005
- **Authors**: S. Aviran, P.H. Siegel, J.K. Wolf
- **PDF**: https://ieeexplore.ieee.org/document/1519173
- **Abstract**: We present a modified turbo equalization scheme that accounts for the colored noise present in high-density partial-response equalization systems. The scheme uses soft information from previous turbo iterations to selectively predict the noise before the next iteration. Simulation results on a PR4 target with low-density parity check (LDPC) coding show that the proposed scheme with up to 2-tap prediction substantially outperforms standard turbo equalization schemes for LDPC-coded EPR4 and PR4 channels.

## A close-to-capacity dirty paper coding scheme

- **Status**: ❌
- **Reason**: Dirty paper coding/precoding (trellis shaping, EXIT chart) — JSCC/precoding, LDPC 부수, 떼어낼 바이너리 LDPC ECC 기법 없음
- **ID**: ieee:1512417
- **Type**: journal
- **Published**: Oct. 2005
- **Authors**: U. Erez, S. ten Brink
- **PDF**: https://ieeexplore.ieee.org/document/1512417
- **Abstract**: The "writing on dirty paper"-channel model offers an information-theoretic framework for precoding techniques for canceling arbitrary interference known at the transmitter. It indicates that lossless precoding is theoretically possible at any signal-to-noise ratio (SNR), and thus dirty-paper coding may serve as a basic building block in both single-user and multiuser communication systems. We design an end-to-end coding realization of a system materializing a significant portion of the promised gains. We employ multidimensional quantization based on trellis shaping at the transmitter. Coset decoding is implemented at the receiver using "virtual bits." Combined with iterative decoding of capacity-approaching codes we achieve an improvement of 2dB over the best scalar quantization scheme. Code design is done using the EXIT chart technique.

## Joint iterative decoding and estimation for side-informed data hiding

- **Status**: ❌
- **Reason**: 데이터 은닉용 turbo 부호 결합 반복디코딩·추정, 비-LDPC이고 떼어낼 LDPC ECC 기법 없음
- **ID**: ieee:1511013
- **Type**: journal
- **Published**: Oct. 2005
- **Authors**: F. Balado, K.M. Whelan, G.C.M. Silvestre +1
- **PDF**: https://ieeexplore.ieee.org/document/1511013
- **Abstract**: We present a previously unavailable study on a general procedure for joint iterative decoding and estimation of attack parameters in side-informed data hiding. This type of approach, which exploits iteratively decodable codes for channel identification purposes, has recently become a relevant research trend in many digital communications problems. An advantage is that estimation pilots are not strictly required, thus affording in principle the implementation of blind methods that are able to work close to the theoretically maximum achievable rate. Such a target naturally requires the use of both near-optimum side-informed data hiding methods (e.g., DC-DM) and near-optimum iteratively decodable channel codes (e.g., turbo codes). The attack channels considered in this study are additive independent random noise, amplitude scaling, and a particular case of fine desynchronization of the sampling grid, whose parameters are estimated by maximum likelihood at the decoder. The complexity of this task is tackled by means of the Expectation-Maximization (EM) algorithm, relying on the use of a priori probabilities produced by the iterative decoding process.

## Performance of BCJR-DFE detectors over recording channels using pattern-dependent noise prediction

- **Status**: ❌
- **Reason**: BCJR-DFE 검출기+PDNP 자기기록 수신기, 비-LDPC 검출 기법으로 LDPC ECC 이식 기법 없음
- **ID**: ieee:1519177
- **Type**: journal
- **Published**: Oct. 2005
- **Authors**: N. Nangare, Xueshi Yang, E. Kurtas +1
- **PDF**: https://ieeexplore.ieee.org/document/1519177
- **Abstract**: A noniterative receiver, namely Bahl-Cocke-Jelinek-Raviv (BCJR)-decision feedback equalizer (DFE), for achieving near capacity performance for intersymbol interference channels was proposed earlier. In this paper, we investigate the performance of BCJR-DFE receivers for recording channels with pattern-dependent media noise. To account for the media noise, we integrated pattern-dependent noise prediction (PDNP) into the BCJR-DFE receiver and evaluated its performance by comparing it to conventional iterative (turbo)-coded recording channels. Numerical simulations suggest that PDNP BCJR-DFE receivers provide superior or comparable performance as a turbo receiver, albeit with lower computation complexity and longer processing delays.

## Carrier phase tracking from turbo and LDPC coded signals affected by a frequency offset

- **Status**: ❌
- **Reason**: 반송파 위상 추적/동기화 — 무선 응용 특이적, 떼어낼 LDPC ECC 기법 없음
- **ID**: ieee:1515668
- **Type**: journal
- **Published**: Oct. 2005
- **Authors**: N. Nele, S. Heidi, M. Moeneclaey
- **PDF**: https://ieeexplore.ieee.org/document/1515668
- **Abstract**: This contribution considers carrier phase estimation from coded signals, affected by a frequency offset at low operating signal-to-noise ratio (SNR). We derive a maximum likelihood (ML) based iterative code-aided feedback phase-tracker suited for receivers with iterative maximum-a-posteriori (MAP) detection. Simulations indicate that the proposed synchronizer is considerably more robust against frequency offsets than a feedforward synchronizer.

## Low Latency Algorithms of Iterative Codes for Wireless Broadband Communication Systems

- **Status**: ❌
- **Reason**: turbo/TPC/LDPC 일반 저지연 언급뿐, 구체적 신규 LDPC 디코더 기여 불명확
- **ID**: ieee:1554157
- **Type**: conference
- **Published**: 5-5 Oct. 2
- **Authors**: Duk Gun Choi, Jin Hee Jeong, Ji Won Jung
- **PDF**: https://ieeexplore.ieee.org/document/1554157
- **Abstract**: This paper presents low latency and computation algorithms of iterative codes such as turbo codes, turbo product codes(TPC), and low density parity check(LDPC) codes for use in wireless broadband communication systems. Due to high coding complexity of iterative codes, this paper focus on lower complexity and/or latency algorithms that are easily implementable in hardware To reduce the latency, this paper proposes some kinds of low latency algorithm for each iterative codes.

## Low Density Parity Check Decoding Algorithm for Multi-level Modulation Scheme

- **Status**: ❌
- **Reason**: 8PSK 다중레벨 변조 bit-splitting 디맵핑, 변조 특이적이라 NAND 이식 기법 없음
- **ID**: ieee:1554158
- **Type**: conference
- **Published**: 5-5 Oct. 2
- **Authors**: Jin Hee Jeong, Duk Gun Choi, Ji Won Jung
- **PDF**: https://ieeexplore.ieee.org/document/1554158
- **Abstract**: LDPC decoding for 8PSK, received symbols are split bit by bit based using the received in-phase and quadrature components. The method of bit-splitting is affects on decoding performance because its method depend on distance over symbol constellation. This paper proposes the bit split method using the sector information with sacrifice a little performance loss compared to Euclidean distance method. Furthermore DVB-S2 Digital Video Broadcasting specification supports BC(Backward Compatible) mode which using the hierarchical modulation method, this paper also analyzes the decoding performance according to deviation angle of 8PSK constellation for various LDPC coding rates.

## Finite-Length Repeat-Accumulate Codes on the Binary Erasure Channel

- **Status**: ❌
- **Reason**: RA 코드의 BEC 유한길이 분석(stopping set), 비-LDPC·순수 이론, 떼어낼 ECC 기법 없음
- **ID**: ieee:1554051
- **Type**: conference
- **Published**: 5-5 Oct. 2
- **Authors**: S.J. Johnson
- **PDF**: https://ieeexplore.ieee.org/document/1554051
- **Abstract**: This paper considers the finite-length performance of repeat-accumulate codes on the binary erasure channel. We provide lower bounds for the minimum stopping set size of RA codes and develop finite-length analysis algorithms for them. Using these results the effect of the RA accumulator and the choice of repetition rate on the decoding performance of finite length RA codes is investigated, and their performance compared to that of low-density parity-check codes

## On Unicast based Recovery for Multicast Content Distribution considering XOR-FEC

- **Status**: ❌
- **Reason**: 멀티캐스트 XOR/LT fountain erasure 복구, 채널 ECC 기법 아님
- **ID**: ieee:1554223
- **Type**: conference
- **Published**: 5-5 Oct. 2
- **Authors**: C. Sasaki, T. Hasegawa, O. Kobayashi +2
- **PDF**: https://ieeexplore.ieee.org/document/1554223
- **Abstract**: In this paper, we propose a fail-safe and efficient download completion scheme for reliable multicast to which FEC (Forward Error Correction) is applied with practical constraints on multicast transmission time. Recently, erasure codes based on XOR operation have become major FEC candidates for multicast content file distribution over the Internet or mobile networks in terms of their recovery performance and processing overheads. In particular LT (Luby Transform) codes are effective in a heterogeneous multicast environment because they can achieve higher reliability by expanding the receiving time at each client. However, multicast transmission time can be restricted due to operational reasons considering multicast resource efficiency. In order to assure all the clients of download completion under such conditions, we newly designed a unicast based recovery mechanism considering LT codes characteristics. We confirmed the efficiency of our proposed mechanism by computer simulation.

## A General Carrier Frequency Offset Estimator for Broadband OFDM

- **Status**: ❌
- **Reason**: OFDM CFO 추정기, LDPC 무관
- **ID**: ieee:1554231
- **Type**: conference
- **Published**: 5-5 Oct. 2
- **Authors**: Defeng Huang, K.B. Letaief
- **PDF**: https://ieeexplore.ieee.org/document/1554231
- **Abstract**: OFDM (Orthogonal Frequency Division Multiplexing) is a promising technology for future broadband wireless communications due to its capability in combating multipath fading. Carrier frequency offset (CFO), which can induce the loss of orthogonality among OFDM sub-carriers and significant performance degradation, needs to be estimated and compensated for. In this paper, we propose a general CFO estimator based on the maximum likelihood (ML) estimation criterion. It will be shown that with the same estimator architecture, CFO can be obtained using either training OFDM symbols, pilot tones, null sub-carriers, or a combination of them. Furthermore, by taking advantage of the channel side information, the performance of CFO estimation can be significantly improved. To demonstrate the capability of the proposed CFO estimator, we will consider an OFDM system using the signal structure of the IEEE WLAN standard 802.11a. Compared with previous work using null sub-carriers alone, it will be shown that by taking advantage of the pilot tones, null sub-carriers, and the channel statistics, the performance of CFO estimation can be improved by about 2dB.

## Maximizing throughput for satellite communication in a hybrid FEC/ARQ scheme using LDPC codes

- **Status**: ❌
- **Reason**: 위성 FEC/ARQ throughput 최적화, LDPC를 블랙박스로 사용, 디코더/HW/구성 기여 없음
- **ID**: ieee:1606163
- **Type**: conference
- **Published**: 17-20 Oct.
- **Authors**: S. Shambayati, C.R. Jones, D. Divsalar
- **PDF**: https://ieeexplore.ieee.org/document/1606163
- **Abstract**: A hybrid forward error correction (FEC)/automatic repeat request (ARQ) has been considered as a mechanism for providing reliable communication between NASA orbiters and landers at the planet Mars. On such a link it is proposed to use a family of capacity achieving LDPC channel codes for FEC and go-back-N protocols for ARQ. In this paper, we analyze such a system and derive equations for its performance. We then use these equations to optimize the performance of the link in terms of information throughput subject to limitations on maximum channel baud rate and spacecraft power and select the best channel code and packet size accordingly at different link path lengths. In this optimization, first the frame error rate of the channel code is expressed in terms of a simple exponential function of the transmitted bit signal-to-noise ratio (Eb/N0), obtained through curve-fitting. Then the standard throughput equation for the go-back-N protocol in terms of the channel codes frame error rate is derived. Next, using the equations for the throughput and the frame error rate, the received Eb/N0 is calculated as a function of transmitted Eb/N0. By minimizing this function, the throughput of the system is maximized for a given available spacecraft power. In the course of this optimization, we quantify the advantage afforded by a system that supports a set of possible code rates and bandwidths as opposed to a system that uses a single rate at different link path lengths.

## Adaptive iterative detection of low density parity check coded bandwidth and power efficient CPM over fading channels

- **Status**: ❌
- **Reason**: CPM/페이딩 채널 F-LDPC 적응반복검출 — 무선 응용 특이적, 떼어낼 신규 디코더/구성 기법 없음
- **ID**: ieee:1605837
- **Type**: conference
- **Published**: 17-20 Oct.
- **Authors**: A. Blair, T. Carter, S. Kim +1
- **PDF**: https://ieeexplore.ieee.org/document/1605837
- **Abstract**: This paper presents a family of waveforms, incorporating a combination of constant envelope (power efficient) modulation and flexible low-density parity-check (F-LDPC) coding that advances the state of the art in terms of spectral efficiency, robustness, and implementation efficiency while providing quality of service (QoS) flexibility. To this point, the F-LDPC (primary candidate for adoption into the 802.11n standard) has been applied to QAM and PSK modulations. This work extends the use of this code to include constant envelope, continuous phase modulation (CPM) in fading channels processed using adaptive iterative detection (AID) techniques. With excellent performance over both constant envelope and non-constant envelope modulations, this scheme has the potential to unify any modulation type with a single coding scheme

## New class of turbo-like codes with universally good performance and high-speed decoding

- **Status**: ❌
- **Reason**: S-SCP 터보형/RA 부호 구성, 비-LDPC 부호 설계로 바이너리 LDPC BP에 떼어낼 기법 없음
- **ID**: ieee:1606137
- **Type**: conference
- **Published**: 17-20 Oct.
- **Authors**: K.M. Chugg, P. Thiennviboon, G.D. Dimou +2
- **PDF**: https://ieeexplore.ieee.org/document/1606137
- **Abstract**: Modern turbo-like codes (TLCs), including concatenated convolutional codes and low density parity check (LDPC) codes, have been shown to approach the Shannon limit on the additive white Gaussian noise (AWGN) channel Many design aspects remain relatively unexplored, however, including TLC design for maximum flexibility, very low error rate performance, and amenability to simple or very high-speed hardware codecs. In this paper we address these design issues by suggesting a new class of TLCs that we call systematic with serially concatenated parity (S-SCP) codes. One example member of this family is the Generalized (or Systematic) repeat accumulate code. We describe two other members of this family that both exhibit good performance over a wide range of block sizes, code rates, modulation, and target error probability. One of these provides error floor performance not previously demonstrated with any other TLC construction and the other is shown to offer very low complexity decoding with good performance. These two codes have been implemented in high-speed hardware codecs and performance curves based on these down to bit error rates below 10-10 are provided.

## A new MIMO detector for iterative decoding with multiple antenna systems

- **Status**: ❌
- **Reason**: MIMO soft 검출기로 LDPC ECC 자체 기여 없음, 떼어낼 LDPC 기법 없음
- **ID**: ieee:1605877
- **Type**: conference
- **Published**: 17-20 Oct.
- **Authors**: A. Bhargave, R.J.P. DeFegueiredo
- **PDF**: https://ieeexplore.ieee.org/document/1605877
- **Abstract**: Recent research has shown that it is possible to achieve near capacity performance with multiple antennas using iterative techniques with an outer channel code. For the iterative multi-input multi-output (MIMO) system to operate at extremely high data rates, the design and development of practically feasible inner MIMO detector is an important issue. A new soft-input soft-output MIMO detector is presented in this paper. A tree-like algorithm is developed by arranging the maximum a posteriori equations in a specific form, The algorithm exploits the concepts of ordering, symbol cancellation, interference nulling and multiple quantization, which have been very successful in Vertical Bell laboratories layered space time (V-Blast) system. Monte-Carlo simulations are presented analyzing different aspects of the soft detector. The performance is also compared with other well-known iterative methods including the modified sphere decoder used with outer convolutional and turbo codes. Results presented show that the detector not only has very good performance, but also has many practical advantages, compared to other methods, like an ability to easily control performance-complexity tradeoff.

## Spectrum efficient coding scheme for correlated non-binary sources in wireless sensor networks

- **Status**: ❌
- **Reason**: 무선센서망 비이진 상관소스 분산소스코딩(Wyner-Ziv) — 소스코딩이며 비이진, 채널 ECC 아님
- **ID**: ieee:1605796
- **Type**: conference
- **Published**: 17-20 Oct.
- **Authors**: Haining Shu, Qilian Liang
- **PDF**: https://ieeexplore.ieee.org/document/1605796
- **Abstract**: Energy-aware technique to reduce energy consumption in distributed sensor networks has become a prominent topic in sensor network research. Various sensor network applications have taken energy efficiency into consideration, in the case of correlated binary sources, distributed source coding has been literally studied in information theory. However, data sources from real sensor networks are normally non-binary. In this paper, we proposed a spectrum efficient coding scheme for correlated non-binary sources in sensor networks. Our approach constructs the codeword cosets for the interested source, taking advantage of statistical characters of the distinct observations from sensor nodes. The coset leaders are then transmitted via the channel and decoding is performed with the available side information. Simulations are carried out over independent and identically distributed (i.i.d) Gaussian sources and data collected from Xbow wireless sensor network test bed. Simulation results show that the proposed scheme performs at 0.5 - 1.5 dB from the Wyner-Ziv distortion bound.

## Evaluation of low density parity-check codes on frequency-selective fading channels

- **Status**: ❌
- **Reason**: 주파수선택 페이딩 채널에서 quasi-regular LDPC 성능평가, 떼어낼 새 기법 없음
- **ID**: ieee:1566801
- **Type**: conference
- **Published**: 12-14 Oct.
- **Authors**: Deshan Miao, Daoben Li
- **PDF**: https://ieeexplore.ieee.org/document/1566801
- **Abstract**: Many papers have shown that low density parity-check (LDPC) codes exhibit excellent performance in the additive white noise (AWGN) channel and flat fading channels, but their performance on frequency-selective fading channels slightly degrades. In this paper, we evaluate the performance of quasi-regular low density parity-check codes in frequency-selective fading channels based on the large area synchronization code division multiple access (LAS-CDMA) system. Simulation results show that LDPC codes outperform turbo codes at high signal-to-noise ratio (SNR) over a wild range of mobile speeds. Furthermore we simply analyze the reasons on their differences on performance, indicating that the distance spectrum plays a very important role to the performance of codes.

## More accurate performance analysis for BP decoding of LDPC codes using EXIT trajectories

- **Status**: ❌
- **Reason**: EXIT 궤적 기반 BP 수렴 임계 성능분석 방법, 디코더/HW/구성 산출물 아닌 순수 분석
- **ID**: ieee:1567129
- **Type**: conference
- **Published**: 12-14 Oct.
- **Authors**: He Zheng, Xiaolei Jin, Hangying Hu
- **PDF**: https://ieeexplore.ieee.org/document/1567129
- **Abstract**: By using extrinsic information transfer (EXIT) trajectories, we propose an improved performance-analysis method for belief propagation (BP) decoding of low-density parity-check (LDPC) codes. On the additive white Gaussian noise (AWGN) channel, the achieved convergence threshold values have errors to those computed by density evolution (DE) within 0.01 dB. Compared with those by EXIT charts, the threshold values obtained by the proposed EXIT-trajectory method are more accurate. Furthermore, we extend the method to the uncorrelated flat Rayleigh fading channel. In contrast with DE, the proposed method is more convenient since no computations for Fourier and inverse Fourier transforms are required during the analysis.

## Decoding for LDPC coded DUSTM over flat Rayleigh fading channel

- **Status**: ❌
- **Reason**: DUSTM 결합 무선 시스템 응용, LDPC는 외부부호로 부수적, 이식 ECC 기법 없음
- **ID**: ieee:1566810
- **Type**: conference
- **Published**: 12-14 Oct.
- **Authors**: Haiyan Cao, Jun Li, Gang Wei
- **PDF**: https://ieeexplore.ieee.org/document/1566810
- **Abstract**: A serially concatenated system with DUSTM (differential unitary space-time modulation) as an inner code and LDPC (low density parity check codes) as outer code is proposed. And a combined iterative soft decoding algorithm is presented based on serially concatenated structure and turbo principle. This proposed scheme outperforms the trellis coded DUSTM scheme studied previously for the usage of good LDPC codes and the combined iterative decoding algorithm.

## Repeat accumulate coded modulation with partial iterative demapping

- **Status**: ❌
- **Reason**: RA 부호 변조 결합(비-LDPC), iterative demapping 변조 노드 기법으로 LDPC BP 이식성 없음
- **ID**: ieee:1566877
- **Type**: conference
- **Published**: 12-14 Oct.
- **Authors**: Xiaoqing Chen, Ping Yu, Hongwen Yang +1
- **PDF**: https://ieeexplore.ieee.org/document/1566877
- **Abstract**: Repeat accumulate (RA) codes are the known simplest one among the family of the capacity-approaching codes. It is much simpler than turbo codes and low density parity check (LDPC) codes, and hence is a competitive choice for the applications of B3G/3G or 4G systems. The main drawback of RA codes, the low code rate, can be overcome by concatenating modulations. In this paper, performance of RA coded demapping (RACM-ID) and referred to as RA coded modulation with partial iterative demapping (RACM-PID) is proposed. The algorithm is equivalent to reduce the degree of the modulation nodes, which is the most calculation cost in the Tanner graph, and thus we have reduced a large part of the calculation complexity of iterative demapping (ID) while keeping the most of the performance gain due to ID. Simulation results are presented for 8PSK and 16QAM examples.
