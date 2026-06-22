# IEEE Xplore — 2015-07


## Efficient Receiver Architecture for LDPC Coded BICM-ID System

- **Status**: ❌
- **Reason**: LDPC-BICM-ID 수신기 병렬 아키텍처지만 demapper-decoder 반복 구조 특이적, LDPC 디코더 자체의 이식 가능 신규 기법 아님 — 무선 BICM-ID 응용 특이
- **ID**: ieee:7095513
- **Type**: journal
- **Published**: July 2015
- **Authors**: Tao Cheng, Kewu Peng, Zaishuang Liu +1
- **PDF**: https://ieeexplore.ieee.org/document/7095513
- **Abstract**: The low-density parity-check (LDPC) coded bit-interleaved coded modulation with iterative demapping (BICM-ID) has excellent bit error rate (BER) performance, but with extremely high receiver complexity. This letter proposes a three-stage full-parallel receiver architecture in which each component decoder is separately but simultaneously iteratively decoded. This architecture can make full use of the computing resources and improve the system performance without sacrificing the throughput. Three-dimensional (3-D) extrinsic information transfer (EXIT) analysis and BER simulations are carried out to demonstrate the superiority of the proposed new receiver architecture.

## Byte-Reconfigurable LDPC Codec Design With Application to High-Performance ECC of NAND Flash Memory Systems

- **Status**: ✅
- **Reason**: NAND Flash QC-LDPC codec 직접: reconfigurable, shared/rescheduling memory HW, SIB-ET 조기종료 — A/D 직접 이식 기여
- **ID**: ieee:7119615
- **Type**: journal
- **Published**: July 2015
- **Authors**: Yu-Min Lin, Huai-Ting Li, Ming-Han Chung +1
- **PDF**: https://ieeexplore.ieee.org/document/7119615
- **Abstract**: The reliability of NAND Flash memory deteriorates due to multi-level cell technique and advanced manufacturing technology. To deal with more errors, LDPC codes show superior performance to conventional BCH codes as ECC of NAND Flash memory systems. However, LDPC codec for NAND Flash memory systems faces problems of high redesign effort, high on-chip memory cost and high-throughput demand. This paper presents a byte-reconfigurable cost-effective high-throughput QC-LDPC codec design for NAND Flash memory systems. Reconfigurable codec design is proposed to support various QC-LDPC codes for different Flash memories. To save on-chip memory cost, shared-memory architecture and rescheduling architecture are presented for encoder and decoder, respectively. The shared-memory architecture can save 23% area cost of the encoder and the rescheduling architecture reduces 15% area cost of decoder. In addition, the proposed sub-iteration based early termination (SIB-ET) scheme reduces 29.6% decoding iteration counts compare with the state-of-the-art early termination scheme when raw BER of Flash memory is $3\times 10^{-3}$. Finally, the QC-LDPC codec for NAND Flash memory systems is implemented in TSMC 90 nm technology. The post-layout result shows that the core size is only 6.72 ${\rm mm}^{2}$ at 222 MHz operating frequency.

## Variable-Length Convolutional Coding for Short Blocklengths With Decision Feedback

- **Status**: ❌
- **Reason**: 가변길이 컨볼루션 부호+ROVA 결정피드백 — 비-LDPC 부호, BP에 이식되는 부호 비의존적 기법 없음
- **ID**: ieee:7101235
- **Type**: journal
- **Published**: July 2015
- **Authors**: Adam R. Williamson, Tsung-Yi Chen, Richard D. Wesel
- **PDF**: https://ieeexplore.ieee.org/document/7101235
- **Abstract**: This paper presents a variable-length decision-feedback coding scheme that achieves high rates at short blocklengths. This scheme uses the reliability-output Viterbi algorithm (ROVA) to determine when the receiver's decoding estimate satisfies a given error constraint. We evaluate the performance of both terminated and tail-biting convolutional codes at average blocklengths less than 300 symbols, using the ROVA and the tail-biting ROVA, respectively. Comparing with recent results from finite-blocklength information theory, simulations for both the BSC and the AWGN channel show that the reliability-based decision-feedback scheme can surpass the random-coding lower bound on throughput for feedback codes at some blocklengths less than 100 symbols. This is true both when decoding after every symbol is permitted and when decoding is limited to a small number of increments. Finally, the performance of the reliability-based stopping rule with the ROVA is compared with retransmission decisions based on CRCs. For short blocklengths where the latency overhead of the CRC bits is severe, the ROVA-based approach delivers superior rates.

## Approaching the Rate-Distortion Limit With Spatial Coupling, Belief Propagation, and Decimation

- **Status**: ❌
- **Reason**: BSC 손실 소스코딩(rate-distortion), spatial coupling+BP guided decimation — 소스 코딩이지 채널 ECC 아님
- **ID**: ieee:7109906
- **Type**: journal
- **Published**: July 2015
- **Authors**: Vahid Aref, Nicolas Macris, Marc Vuffray
- **PDF**: https://ieeexplore.ieee.org/document/7109906
- **Abstract**: We investigate an encoding scheme for lossy compression of a binary symmetric source based on simple spatially coupled low-density generator-matrix codes. The degree of the check nodes is regular and the one of code-bits is Poisson distributed with an average depending on the compression rate. The performance of a low complexity belief propagation guided decimation algorithm is excellent. The algorithmic rate-distortion curve approaches the optimal curve of the ensemble as the width of the coupling window grows. Moreover, as the check degree grows both curves approach the ultimate Shannon rate-distortion limit. The belief propagation guided decimation encoder is based on the posterior measure of a binary symmetric test-channel. This measure can be interpreted as a random Gibbs measure at a temperature directly related to the noise level of the test-channel. We investigate the links between the algorithmic performance of the belief propagation guided decimation encoder and the phase diagram of this Gibbs measure. The phase diagram is investigated thanks to the cavity method of spin glass theory which predicts a number of phase transition thresholds. In particular, the dynamical and condensation phase transition temperatures (equivalently test-channel noise thresholds) are computed. We observe that: 1) the dynamical temperature of the spatially coupled construction saturates toward the condensation temperature and 2) for large degrees the condensation temperature approaches the temperature (i.e., noise level) related to the information theoretic Shannon test-channel noise parameter of rate-distortion theory. This provides heuristic insight into the excellent performance of the belief propagation guided decimation algorithm. This paper contains an introduction to the cavity method.

## Random Linear Network Coding Based on Non-Orthogonal Multiple Access in Wireless Networks

- **Status**: ❌
- **Reason**: NOMA 기반 랜덤 선형 네트워크 코딩 — LDPC 아님, ECC 디코더 기법 없음
- **ID**: ieee:7111241
- **Type**: journal
- **Published**: July 2015
- **Authors**: Sungjin Park, Dong-Ho Cho
- **PDF**: https://ieeexplore.ieee.org/document/7111241
- **Abstract**: To improve the packet success probability, random linear network coding (RLNC) based on non-orthogonal multiple access (NOMA) for multicast services was employed in wireless downlink networks where a source superposes multiple coded packets before transmitting these packets to multiplexing groups of receivers in a power domain. Using a successive interference cancellation (SIC) and a Gauss-Jordan elimination process, receivers can recover their original packets. We derive expressions for the total packet success probability for the case of NOMA (or OMA) with (or without) RLNC, and propose group based power allocation schemes in order to improve performance with a low overhead. Through the results of simulations, we verify our derivations and show that RLNC based on NOMA improves the packet success probability and decreases the packet delay.

## A Randomized Algorithm for the Capacity of Finite-State Channels

- **Status**: ❌
- **Reason**: 유한상태채널 용량 계산 랜덤화 알고리즘 — 순수 정보이론, 디코더/HW/구성으로 안 이어짐
- **ID**: ieee:7105917
- **Type**: journal
- **Published**: July 2015
- **Authors**: Guangyue Han
- **PDF**: https://ieeexplore.ieee.org/document/7105917
- **Abstract**: Inspired by ideas from the field of stochastic approximation, we propose a randomized algorithm to compute the capacity of a finite-state channel with a Markovian input. When the mutual information rate of the channel is concave with respect to the chosen parameterization, the proposed algorithm proves to be convergent to the capacity of the channel almost surely with the derived convergence rate. We also discuss the convergence behavior of the algorithm without the concavity assumption.

## Capacity-Achieving Feedback Schemes for Gaussian Finite-State Markov Channels With Channel State Information

- **Status**: ❌
- **Reason**: 가우시안 유한상태 마르코프 채널 피드백 용량달성 스킴 — 순수 정보이론, 부호/디코더 기여 없음
- **ID**: ieee:7112479
- **Type**: journal
- **Published**: July 2015
- **Authors**: Jialing Liu, Nicola Elia, Sekhar Tatikonda
- **PDF**: https://ieeexplore.ieee.org/document/7112479
- **Abstract**: In this paper, we propose capacity-achieving communication schemes for Gaussian finite-state Markov channels subject to an average channel input power constraint, under the assumption that the transmitters can have access to delayed noiseless output feedback as well as instantaneous or delayed channel state information. We show that the proposed schemes reveals connections between feedback communication and feedback control.

## Differential Spatial Modulation for APSK in Time-Varying Fading Channels

- **Status**: ❌
- **Reason**: 차분 공간변조(DSM) APSK 변조 기법 — ECC는 부수 언급, 떼어낼 LDPC 기법 없음
- **ID**: ieee:7095517
- **Type**: journal
- **Published**: July 2015
- **Authors**: Philippa A. Martin
- **PDF**: https://ieeexplore.ieee.org/document/7095517
- **Abstract**: We develop a novel differential spatial modulation (DSM) scheme for amplitude phase shift keying (APSK) modulation, which can either improve throughput or performance over DSM for PSK. Then we investigate the impact of time-varying fading on DSM. We find performance degrades if the fading is too fast due to differential detection. The impact of a long outer error control code (ECC) is also considered. Its performance is limited by the slowly varying channel required for differential detection. We consider using reconfigurable antennas to periodically change the channel conditions and hence significantly improve coded performance for DSM systems.

## Iterative Detection and Decoding for TDMR With 2-D Intersymbol Interference Using the Four-Rectangular-Grain Model

- **Status**: ❌
- **Reason**: TDMR 2D 자기기록 채널 검출(BCJR 기반 검출기) 중심 — 채널코드는 기존 것 재사용, 새 LDPC 디코더/구성 기여 없음
- **ID**: ieee:7047859
- **Type**: journal
- **Published**: July 2015
- **Authors**: Michael Carosino, Jiyang Yu, Yiming Chen +6
- **PDF**: https://ieeexplore.ieee.org/document/7047859
- **Abstract**: This paper considers detection and error control coding for the 2-D magnetic recording (TDMR) channel modeled with the 2-D four-rectangular-grain model (FRGM). This simple model captures the effects of different 2-D grain sizes and shapes, as well as the TDMR grain overwrite effect. We construct a row-by-row Bahl-Cocke-Jelinek-Raviv-based detector that processes two rows at a time. Simulation results using the same coded bit density and channel code as a previous paper on FRGM detection show gains in user bits per grain of up to 13.4% when the detector and the decoder iteratively exchange soft information, resulting in densities higher than 0.5 user bits per grain under all scenarios simulated. When the proposed detector/decoder operates on coded bits read from a random Voronoi grain model, the achieved density drops to 0.25 user bits per grain due to model mismatch between the detector and the data. Finally, this paper considers an iterative detection and decoding scheme combining TDMR detection, 2-D-intersymbol interference (ISI) detection, and soft-in/soft-out channel decoding in a structure with two iteration loops. Simulation results for the concatenated FRGM and $2 \times 2$ averaging mask ISI channel with 10 dB signal-to-noise ratio show that densities of 0.496 user bits per grain and above can be achieved over the entire range of FRGM grain probabilities.

## Video Error Correction Using Soft-Output and Hard-Output Maximum Likelihood Decoding Applied to an H.264 Baseline Profile

- **Status**: ❌
- **Reason**: H.264 비디오 JSCC 에러 컨실먼트, 구문요소 ML 디코딩 — LDPC ECC 기법 아님, 떼어낼 디코더 없음
- **ID**: ieee:6671959
- **Type**: journal
- **Published**: July 2015
- **Authors**: François Caron, Stéphane Coulombe
- **PDF**: https://ieeexplore.ieee.org/document/6671959
- **Abstract**: Error concealment has long been identified as the last line of defense against transmission errors. Since error handling is outside the scope of video coding standards, decoders may choose to simply ignore corrupted packets or attempt to decode their content. In this paper, we present a novel joint source-channel decoding approach that can be applied to received video packets containing transmission errors. Soft-output information is combined with our novel syntax-element-level maximum likelihood decoding framework to effectively extract valid macroblocks from corrupted H.264 slices. Simulation results show that our video error correction strategy provides an average peak signal-to-noise ratio (PSNR) improvement near 2 dB compared to the error concealment approach used by the H.264 reference software, as well as an average PSNR improvement of 0.8 dB compared to state-of-the-art error concealment. The proposed method is also applicable when only hard-information is available, in which case it performs better than state-of-the-art error concealment especially in high error conditions. Finally, in our simulations, the proposed method increased the decoder computational complexity by only 5% to 20%, making it applicable for real-time applications.

## Column weights optimization for semi-regular nonbinary LDPC codes

- **Status**: ❌
- **Reason**: 비이진 GF(q) nonbinary LDPC 코드 구성 - 바이너리 한정 기준 위배
- **ID**: ieee:7296246
- **Type**: conference
- **Published**: 9-11 July 
- **Authors**: Wojciech Sułek, Marcin Kucharczyk
- **PDF**: https://ieeexplore.ieee.org/document/7296246
- **Abstract**: The paper concerns Low Density Parity Check (LDPC) codes over nonbinary Galois Fields GF(q), that are a generalization of the industrial standard binary LDPC codes for forward error correction in communication and information systems. The semi-regular nonbinary LDPC codes can outperform their binary counterparts in the case of short to moderate code word lengths. The methods for the good code construction based on a computer search techniques are already well investigated. However, there is a lack of systematic results for optimal weight distribution of columns of parity check matrices for codes over different field order and different rate. In this article we present a Monte Carlo like algorithm for column weight optimization devoted to nonbinary semi-regular codes along with optimization results that facilitate the codes construction computer-based methods.

## Superimposed effects of signature sequences and LDPC technique in faded CDMA multiuser systems

- **Status**: ❌
- **Reason**: CDMA 멀티유저 무선 응용, LDPC 부수 언급, 떼어낼 신규 디코더/구성 기법 없음
- **ID**: ieee:7203957
- **Type**: conference
- **Published**: 9-10 July 
- **Authors**: Ioana I. Marcu, Carmen Voicu, Simona V. Halunga
- **PDF**: https://ieeexplore.ieee.org/document/7203957
- **Abstract**: Multiuser detection systems face multiple challenges during communication error correction process when the communication environment is dramatically affected by fading. Depending on the type of channel model that occurs during a communication the bit error rate (BER) can be more or less decreased using appropriate coding/decoding technique. This paper illustrates error correction in (Low-Density Parity Check Code Division Multiple Access) LDPC-CDMA systems when Gaussian mixture noise and Nakagami-m fading affect the multiuser communication. The proposed DS-CDMA multiuser system in combination with LDPC technique together with a careful choice of signature sequences will significantly improve the performance of the multiuser system and will minimize the effect of Gaussian mixture noise and Nakagami fading on the communication channel.

## A new reliability-based incremental redundancy hybrid ARQ scheme using LDPC codes

- **Status**: ✅
- **Reason**: RC-LDPC 기반 RB-HARQ, 클러스터 신뢰도 메트릭 신규 제안 — 바이너리 LDPC RC/신뢰도 기법 이식 검토 여지(애매, 살림)
- **ID**: ieee:7255170
- **Type**: conference
- **Published**: 6-9 July 2
- **Authors**: Hamid Saber, Ian Marsland
- **PDF**: https://ieeexplore.ieee.org/document/7255170
- **Abstract**: We present a new reliability-based hybrid automatic repeat request (RB-HARQ) scheme based on low density parity check (LDPC) codes. With the proposed RB-HARQ, which uses a rate-compatible LDPC code with puncturing and extending, the longest codeword is divided into clusters of code bits. Unlike previous works, in the event of a decoding failure, the receiver measures the reliability of received clusters, instead of code bits, and determines which cluster would be most beneficial for retransmission. Several metrics to determine the best cluster candidates for retransmission are derived analytically. We show that one of the new metrics outperforms the previous metrics. We also show that even with the feedback overhead taken into account, our RB-HARQ can still result in significant gain over the previous works, provided that the cluster size is appropriately selected.

## Enhancing secrecy of the Gaussian wiretap channel using rate compatible LDPC codes with error amplification

- **Status**: ❌
- **Reason**: RC-LDPC 물리계층 보안(wiretap)+error amplification — 표준 RC-LDPC 사용, 보안 도메인이라 떼어낼 신규 ECC 기법 없음
- **ID**: ieee:7255148
- **Type**: conference
- **Published**: 6-9 July 2
- **Authors**: Mohamed Haj Taieb, Jean-Yves Chouinard
- **PDF**: https://ieeexplore.ieee.org/document/7255148
- **Abstract**: This paper proposes a physical layer coding scheme to secure communications over the Gaussian wiretap channel. This scheme is based on non-systematic Rate-Compatible Low-Density-Parity-Check (RC-LDPC) codes. The rate compatibility involves the presence of a feedback channel that allows transmission at the minimum rate required for legitimate successful decoding. Whenever the decoding is unsuccessful, a feedback request is sent back by the intended receiver, favoring the legitimate recipient over an unauthorized receiver (eavesdropper). The proposed coding scheme uses a finer granularity rate compatible code to increase the eavesdropper decoding failure rate. However, finer granularity also implies longer decoding delays. For this reason, a rate estimator based on the wiretap channel capacity is used. For this purpose, a set of packets is sent at once and then successive small packets are added subsequently as needed until successful decoding by the legitimate receiver is achieved. Since the secrecy level can be assessed through the bit error rate (BER) at the unintended receiver, an error amplifier is proposed to convert the loss of only few packets in the wiretap channel into much higher BERs for the eavesdroppers. Simulation results show the secrecy improvements obtained in terms of error amplification with the proposed coding scheme. Negative security gaps can also be achieved at the physical layer.

## Construction of structured low density lattice codes based on finite fields

- **Status**: ❌
- **Reason**: Low-density lattice codes(LDLC)/CLDLC — 격자부호(비이진 계열), 바이너리 LDPC ECC 아님
- **ID**: ieee:7405587
- **Type**: conference
- **Published**: 6-9 July 2
- **Authors**: Jia-Yun Li, Shu-Tao Xia, Xin-Ji Liu
- **PDF**: https://ieeexplore.ieee.org/document/7405587
- **Abstract**: Finite fields were successfully used to construct algebraic low-density parity-check (LDPC) codes, especially Quasi-Cyclic LDPC codes. These LDPC codes with large minimum distances have lower error floor, linear complexity of encoding and are more practical for hard-decision algebraic decoding. In this paper, we show that finite fields can also be successfully used to construct algebraic low-density lattice codes (LDLC), denoted by structured LDLC. A general framework to construct algebraic LDLC is presented. LDLC constructed by this general framework have comparable performance to the corresponding random codes over addition white Gaussian noise (AWGN) channel with iterative soft-decision decoding in terms of symbol-error probability. Furthermore, the general framework is extended to complex low-density lattice codes (CLDLC) and results in algebraic CLDLC which perform very well for small dimensions.

## Analysis of forward error correction and achievable rates for optical fiber systems

- **Status**: ❌
- **Reason**: 광섬유 FEC의 achievable rate(상호정보 bound) 분석; 디코더/HW/구성으로 안 이어지는 순수 이론 bound
- **ID**: ieee:7193358
- **Type**: conference
- **Published**: 5-9 July 2
- **Authors**: Tobias Fehenberger, Norbert Hanik
- **PDF**: https://ieeexplore.ieee.org/document/7193358
- **Abstract**: We study lower bounds on mutual information that are achievable rates for optimal and sub-optimal hard-decision (HD) and soft-decision (SD) decoding. These rates represent the maximum amount of information we can convey over a memoryless channel with a fixed input if ideal forward error correction (FEC) is employed. We find that the gain of complex SD decoding over HD decoding can be very small, depending on the modulation format and the system parameters. We further study the gap of a practical FEC scheme to its asymptotic limit.

## Multidimensional aspects of ultra high speed optical networking

- **Status**: ❌
- **Reason**: 초고속 광네트워크 다차원 변조/멀티플렉싱 개관; LDPC 부수 언급, 떼어낼 ECC 기법 없음
- **ID**: ieee:7193472
- **Type**: conference
- **Published**: 5-9 July 2
- **Authors**: Milorad Cvijetic, Ivan B. Djordjevic
- **PDF**: https://ieeexplore.ieee.org/document/7193472
- **Abstract**: Multidimensional approach in optical channel construction and parallelization in signal processing are the key factors in enabling high spectral efficiency of optical transmission links and the overall throughput increase in optical networks. Multidimensionality is mainly related to employment of advanced modulation and multiplexing schemes operating in combination with the advanced coding and detection techniques. In this paper we discuss the key multidimensional principles that can be used not only of the information capacity increase, but also as enablers of the elastic and dynamic networking.

## A simple and efficient multi-way relay network coding scheme

- **Status**: ❌
- **Reason**: 멀티웨이 릴레이 네트워크 코딩 기법, LDPC는 부수적 신뢰성 향상 언급일 뿐 떼어낼 ECC 기법 없음
- **ID**: ieee:7194082
- **Type**: conference
- **Published**: 29 June-2 
- **Authors**: Zhanji Wu, Chengxin Jiang
- **PDF**: https://ieeexplore.ieee.org/document/7194082
- **Abstract**: For full-data exchange multi-way relay channels, a novel efficient multi-way relay network coding scheme is proposed. It is based on multi-stage two-way network coding, which is low-complexity and high reliable. For the channel without noise, the throughput per node per channel is increased by 50 % compared to plain routing, and even by 12.5% compared to the binary-signaling network coding scheme. Besides, due to the simple nature of 3-pulse amplitude modulation (3-PAM), it has much lower complexity and much higher reliability compared to the binary-signaling network coding scheme. Both theoretical analysis and computer simulations prove such throughput gain. On the additive white Gaussian noise (AWGN) channel, low density parity check (LDPC) codes are utilized in this scheme to improve the reliability. The simulation results show that the signal-to-noise ratio (SNR) gains to reference scheme increase as the number of the source nodes increases, and the SNR gains of the LDPC-coding scheme are even bigger than the uncoding scheme.

## Sliceable bandwidth variable transponder: The IDEALIST vision

- **Status**: ❌
- **Reason**: 광전송 sliceable transponder 아키텍처, LDPC/ECC 무관
- **ID**: ieee:7194093
- **Type**: conference
- **Published**: 29 June-2 
- **Authors**: E. Riccardi, A. Pagano, E. Hugues-Salas +12
- **PDF**: https://ieeexplore.ieee.org/document/7194093
- **Abstract**: This paper reports on the general architecture for a sliceable bandwidth variable transponder as discussed within the IDEALIST European project. Support for super-channels (optical connections with several adjacent sub-carriers) and slice-ability (super-channels generated together but independently routed in the network towards different destinations) is guaranteed. For illustrative purpose some driving ideas on a possible modular implementation are shown.

## Impacts of the packet scheduling on the performance of erasure codes: Methodology and application to GLDPC-Staircase codes

- **Status**: ❌
- **Reason**: AL-FEC erasure 코드(GLDPC-Staircase, RS 내부부호)의 패킷 스케줄링—erasure/소거코드라 채널 ECC 비대상
- **ID**: ieee:7194119
- **Type**: conference
- **Published**: 29 June-2 
- **Authors**: Ferdaouss Mattoussi, Vincent Roca, Bessem Sayadi
- **PDF**: https://ieeexplore.ieee.org/document/7194119
- **Abstract**: Content broadcasting over wireless networks heavily relies on Application-Level FEC codes to improve transmission robustness in front of channel erasures. Because they operate in the higher layers of the protocol stack, they benefit from a lot of flexibility. In particular, since streaming applications and bulk transfer applications have different constraints, different packet scheduling strategies may be used by the sender, offering different trade-offs between decoding latency and long erasure burst protection. This work tries to find the best packet scheduling scheme(s) at a sender for a given type of AL-FEC codes. The contributions are twofold: first we define a methodology to measure the impacts of packet scheduling on AL-FEC performance, both under ITerative (IT) and Maximum Likelihood (ML) decoding, for a large set of channels; then we apply this methodology to GLDPC-Staircase codes, an extension of LDPC-Staircase codes using Reed Solomon codes as inner codes. In previous works we showed that these codes have erasure recovery performance close to ideals codes when packets are transmitted in a random order. In this work we show that these codes perform extremely well when sending source packets sequentially first (a key requirement to keep latency minimum with streaming applications) and then extra-repair packets followed by LDPC repair packets, both in a random order.

## A new channel coding network coding scheme for two-way relay

- **Status**: ❌
- **Reason**: lattice/PNC 채널-네트워크 부호화 relay, 비-LDPC, 이식 기법 없음
- **ID**: ieee:7237263
- **Type**: conference
- **Published**: 28-30 July
- **Authors**: William Liu
- **PDF**: https://ieeexplore.ieee.org/document/7237263
- **Abstract**: In this paper, after a brief review of all the channel coded physical layer network coding (PNC) schemes, we introduce the definition of compatibility of channel code and lattice code, and provide a methodology with which the standard joint channel coding lattice coding (JCCNC) scheme can be applied to general types of pulse amplitude modulation (PAM) and quadrature amplitude modulation (QAM) modulation systems. We also propose a new scheme for two-way relay systems called lattice decoding joint channel coding network coding scheme (LDJCCNC). Compared with the existing schemes, this new scheme has the advantage of less complexity, not requiring the channel information, and being able to be conveniently applied to general types of PAM and QAM modulation systems. Simulation results show that this new channel coded PNC scheme has good performance and its performance is better than the standard channel coded network coding scheme when the channel information is unknown or misestimated.

## Spatially-coupled codes for optical communications: state-of-the-art and open problems

- **Status**: ❌
- **Reason**: spatially-coupled codes 서베이/open problems, 구체적 신규 기여 없음
- **ID**: ieee:7340116
- **Type**: conference
- **Published**: 28 June-2 
- **Authors**: Alexandre Graell i Amat, Christian Häger, Fredrik Brännström +1
- **PDF**: https://ieeexplore.ieee.org/document/7340116
- **Abstract**: We give a brief survey of a particularly interesting class of codes, called spatially-coupled codes, which are strong candidates for future optical communication systems. We discuss some recent research on this class of codes in the area of optical communications, and summarize some open research problems.

## Spatially coupled codes and optical fiber communications: An ideal match?

- **Status**: ✅
- **Reason**: E/D: irregular SC-LDPC(바이너리) 구성 최적화 + FPGA 디코더, NAND LDPC 코드설계·HW 이식 가능
- **ID**: ieee:7227080
- **Type**: conference
- **Published**: 28 June-1 
- **Authors**: Laurent Schmalen, Detlef Suikat, Detlef Rösener +3
- **PDF**: https://ieeexplore.ieee.org/document/7227080
- **Abstract**: In this paper, we highlight the class of spatially coupled codes and discuss their applicability to long-haul and submarine optical communication systems. We first demonstrate how to optimize irregular spatially coupled LDPC codes for their use in optical communications with limited decoding hardware complexity and then present simulation results with an FPGA-based decoder where we show that very low error rates can be achieved and that conventional block-based LDPC codes can be outperformed. In the second part of the paper, we focus on the combination of spatially coupled LDPC codes with different demodulators and detectors, important for future systems with adaptive modulation and for varying channel characteristics. We demonstrate that SC codes can be employed as universal, channel-agnostic coding schemes.

## Compressed Sensing using sparse binary measurements: A rateless coding perspective

- **Status**: ❌
- **Reason**: sparse 행렬 압축센싱 복구, 채널 ECC 아님
- **ID**: ieee:7227005
- **Type**: conference
- **Published**: 28 June-1 
- **Authors**: Dejan Vukobratovic, Dino Sejdinovic, Aleksandra Pizurica
- **PDF**: https://ieeexplore.ieee.org/document/7227005
- **Abstract**: Compressed Sensing (CS) methods using sparse binary measurement matrices and iterative message-passing recovery procedures have been recently investigated due to their low computational complexity and excellent performance. Drawing much of inspiration from sparse-graph codes such as Low-Density Parity-Check (LDPC) codes, these studies use analytical tools from modern coding theory to analyze CS solutions. In this paper, we consider and systematically analyze the CS setup inspired by a class of efficient, popular and flexible sparse-graph codes called rateless codes. The proposed rateless CS setup is asymptotically analyzed using tools such as Density Evolution and EXIT charts and fine-tuned using degree distribution optimization techniques.

## Multiuser detection in multibeam satellite systems: Theoretical analysis and practical schemes

- **Status**: ❌
- **Reason**: 다중빔 위성 다중사용자 검출 코드 재설계+비트매핑, 응용 특이적, 이식 LDPC 기법 없음
- **ID**: ieee:7227093
- **Type**: conference
- **Published**: 28 June-1 
- **Authors**: Giulio Colavolpe, Andrea Modenini, Amina Piemontese +1
- **PDF**: https://ieeexplore.ieee.org/document/7227093
- **Abstract**: The application of multiuser detection has been recently suggested as an effective solution to maximize the achievable rates in multibeam satellite systems. While the possibility of significant theoretical gains has already been proved, the question remains whether these gains can be achieved by practical schemes. In this work, we analyze the performance of coded schemes in two different transmission scenarios. We show that classical single-user codes are not suitable for multiuser applications, and we propose two ways to improve the performance, based on the redesign of the code and of the bit mapping.

## Stochastic amplify-and-forward schemes for multigroup multicast transmission in a distributed relay network

- **Status**: ❌
- **Reason**: stochastic AF beamforming relay, LDPC 무관
- **ID**: ieee:7227097
- **Type**: conference
- **Published**: 28 June-1 
- **Authors**: Sissi Xiaoxiao Wu, Qiang Li, Wing-Kin Ma +1
- **PDF**: https://ieeexplore.ieee.org/document/7227097
- **Abstract**: In this paper, we study amplify-and-forward (AF) schemes to for multigroup multicast information delivery between long-distance users. The target scenario is a two-hop distributed one-way relay network where the transmitters, relays and receivers are all equipped with a single antenna. Assuming that channel state information (CSI) is perfectly known, our goal here is to design the AF weights at the relays so that the system rate performance can be optimized. A classic AF scheme in this context is to employ a rank-one beamformed AF (BF-AF) strategy with a max-min-fair (MMF) achievable rate objective. In this way, the semidefinite relaxation (SDR) technique is widely used to provide an (approximate) solution for the MMF problem. It is known that the achievable rate performance of the SDR-based BF-AF scheme tends to degrade seriously with the number of users served in the relay network. This motivates us to propose stochastic beamformed AF (SBF-AF) schemes to improve the achievable rate performance. The salient feature of the SBF-AF schemes is that it employs time-varying AF weights and bypass some inherent issues in the SDR-based BF-AF scheme. Our theoretical analysis and numerical results both show that the SBF-AF schemes can outperform the BF-AF scheme.

## Efficient implementation of structured long block-length LDPC codes

- **Status**: ✅
- **Reason**: 긴 블록 구조적 LDPC의 offset min-sum 부분병렬 디코더 아키텍처+인터커넥트 절감 — 이식 가능 HW(D)
- **ID**: ieee:7245739
- **Type**: conference
- **Published**: 27-29 July
- **Authors**: Andrew J. Wong, Saied Hemati, Warren J. Gross
- **PDF**: https://ieeexplore.ieee.org/document/7245739
- **Abstract**: High-speed and low-area decoders for low-density parity-check (LDPC) codes with very long block lengths are challenging to implement due to the large amount of nodes and edges required. In this paper we implement a decoder for a (32643, 30592) LDPC code that has variable nodes of degree 7, check nodes degrees of 111 and 112, and 228501 edges, making fully-parallel hardware implementation unfeasible. We analyze the structure of this code and describe a method of replacing the complex interconnect with a local, area-efficient version. We develop an modular architecture resulting in a low-complexity partially-parallel decoder architecture based on the offset min-sum algorithm. The proposed decoder is shown to achieve a minimum gain of 92% in area utilization, compared to an extremely optimistic area estimation of the fully-parallel decoder that neglects the interconnection overhead. Synthesis in 65 nm CMOS is performed resulting in a clock frequency of 370 MHz and a throughput of 24 Gbps with an area of 7.99 mm2.

## The design of a rateless channel coding scheme for deep-space communication

- **Status**: ❌
- **Reason**: 심우주용 Raptor(fountain) rateless 코드 — 비-LDPC 부호, 떼어낼 BP 이식 기법 없음
- **ID**: ieee:7266524
- **Type**: conference
- **Published**: 27-29 July
- **Authors**: Shaolei Chen, Chuangmu Yao, Rui Dai
- **PDF**: https://ieeexplore.ieee.org/document/7266524
- **Abstract**: In this paper, a rateless channel coding scheme is proposed for deep-space communication. Unlike the traditional fixed-rate coding schemes, in our scheme the coding rate is not designed as a fixed value before transmission, but adaptive to the channel variations resulted from the dynamically varied transmission distance and complex atmospheric conditions. Specifically, a Raptor code which is provided by a cascade structure is adopted for the data transmission. The pre-code of Raptor code is encoded with a linear-time progressive edge-growth algorithm which avoids tedious calculations by matrix transformation. Moreover, based on a joint iterative decoding method, the output degree distribution of our Raptor code is optimized so as to obtain good decoding performances. Comparisons are provided with respect to the fixed-rate coding schemes by numerical simulation, which shows that our proposed rateless coding scheme has better performance and is adaptively capacity-approaching for the deep-space data transmission.

## Mixed-signal implementation of differential decoding using binary message passing algorithms

- **Status**: ✅
- **Reason**: 바이너리 LDPC용 MDD-BMP 디코더의 혼합신호 회로 구현 — 이식 가능 HW/디코더(C/D)
- **ID**: ieee:7245718
- **Type**: conference
- **Published**: 27-29 July
- **Authors**: Glenn Cowan, Kevin Cushon, Warren Gross
- **PDF**: https://ieeexplore.ieee.org/document/7245718
- **Abstract**: This paper presents the mixed-signal circuit implementation of reduced complexity algorithms for decoding low-density parity check (LDPC) codes. Based on modified differential decoding using binary message passing (MDD-BMP), binary addition using discrete-time digital circuits is replaced by continuous-time analog-current summation. Potential degradation due to the mismatch between current sources, P/N strength mismatch and inverter-threshold mismatch is considered in behavioural simulation and shown to be tolerable. Area estimates suggest a reduction from 0.27 mm2 to 0.11 mm2 for the FG(273, 191) code. Finally, transistor level simulation of the FG(273, 191) code using TSMC 65 nm technology shows an efficiency of 0.56 pJ/bit.

## Iterative block DFE techniques based on LDPC for SC-FDE underwater acoustic communications

- **Status**: ❌
- **Reason**: 수중음향 SC-FDE에서 IBDFE 등화기와 LDPC 디코더 정보교환; LDPC는 표준 채널코드로 베이스라인, 떼어낼 신규 디코더/HW/구성 기법 없음
- **ID**: ieee:7250313
- **Type**: conference
- **Published**: 22-24 July
- **Authors**: Xiaoyi Hu, HeQun Zhu, DeQing Wang +1
- **PDF**: https://ieeexplore.ieee.org/document/7250313
- **Abstract**: An iterative block decision-feedback equalizer based on LDPC (LDPC-IBDEF) for SCFDE underwater acoustic (UWA) communication system is proposed. The new equalizer employs IBDFE together with iterative LDPC decoding technique, leading to a double-layer structure which can solve the frequency selective fading problem in UWA channel. In the outer-layer, IBDFE iteratively exchanges information with the LDPC channel decoder to improve its performance. Sea tests carried out in Xiamen Harbor show that the average BER performance of the new scheme for SCFDE system is in the order of 10-3, when the data rate is 2kbps and the distance is 10km.

## An area-efficient architecture for stochastic LDPC decoder

- **Status**: ✅
- **Reason**: 확률적(stochastic) LDPC 디코더의 면적효율 변수노드 아키텍처 신규 제안; 이식 가능 HW(D)
- **ID**: ieee:7251868
- **Type**: conference
- **Published**: 21-24 July
- **Authors**: Qichen Zhang, Yun Chen, Di Wu +2
- **PDF**: https://ieeexplore.ieee.org/document/7251868
- **Abstract**: Stochastic computation is an excellent approach for low-density parity-check codes decoding. By adding edge memories at each edge in the Tanner graph, fully parallel hardware implementation can be designed with much lower wire complexity. This feature can alleviate the wire congestion in conventional Min-Sum decoders. However, edge memories occupy large physical area percentage of variable node and cause large dynamic power dissipation. In this paper, we propose an area-efficient counter based structure for variable nodes. In order to reduce the area of variable nodes, we eliminate the edge memories in all variable nodes and reuse the counter designed to function the hard-decision to trace the probability of the prior message. The value boundary of the counter is enlarged to record the probability more precisely, and the value of the counter is compared with a random number to determine the output of variable nodes. We also reuse parts of some sub-units in variable nodes to build others. As a result, for LDPC codes of 10GBASE-T (IEEE 802.3an-2006), the proposed structure of variable node can reduce 88.3% EM based variable node area.

## Effect of bit-level correlation in stochastic computing

- **Status**: ❌
- **Reason**: stochastic computing 일반 비트상관 분석; LDPC 디코더 특정 기여 아님, 떼어낼 ECC 기법 없음
- **ID**: ieee:7251915
- **Type**: conference
- **Published**: 21-24 July
- **Authors**: Megha Parhi, Marc D. Riedel, Keshab K. Parhi
- **PDF**: https://ieeexplore.ieee.org/document/7251915
- **Abstract**: Simple stochastic logic gates can compute complex functions using stochastic computing. A stochastic number is encoded by a unary bit stream where each bit is 0 or 1. The value of the number is represented by the percent of 1's in the number, and is interpreted as a probability. Each bit of the stochastic number can be modeled as a Bernoulli random variable, and each stochastic number can be represented by a binomial random variable. The variance of a stochastic number is given by p(1 - p)/N where N represents the number of bits in the sequence, and p represents the mean value of the number. For long word-lengths, a binomial random variable behaves as a Gaussian random variable. The mean and variance of a two-input stochastic logic gate are dependent on the bit-level correlation of the two inputs. This paper derives closed-form expressions for mean and variance of two-input stochastic logic gates with correlated inputs. An approach to synthesize correlated stochastic bit streams with specified correlation from uncorrelated bit streams is also presented. Using the proposed synthesis method, stochastic logic gates are simulated with correlated inputs. The simulated values of means and variances are shown to be the same as the theoretical values; thus, the closed-form expressions are validated.

## Adaptive reliability-based iteration min-sum decoding algorithm for majority-logic decodable LDPC codes

- **Status**: ✅
- **Reason**: C: majority-logic decodable LDPC용 적응형 RBI min-sum 디코더(체크노드별 적응 스케일링 팩터) — 이식 가능 디코더 알고리즘
- **ID**: ieee:7395208
- **Type**: conference
- **Published**: 13-15 July
- **Authors**: Hongwei Zhao, Kai Zhang, Mengmeng Shi
- **PDF**: https://ieeexplore.ieee.org/document/7395208
- **Abstract**: In this paper, an adaptive decoding algorithm for majority-logic decodable LDPC codes is present based on a recent work by Chen et al. Different from the RBI-MSD algorithm, the presented adaptive reliability-based iteration min-sum decoding algorithm does not need to predesignate the scaling factor, which is optimized by discretized density evolution. In the adaptive RBIMSD algorithm, an adaptive scaling factor is induced for each check node to modify the extrinsic message. The adaptive scaling factor is computed by the ratio of the second minimum and the maximum value among the message, which is received by the check nodes. Simulation results show that, the performance of the adaptive RBI-MSD algorithm is almost as well as that of the original RBI-MSD algorithm but with a little (or negligible) computation increase.

## An efficient structure for terminating spatially coupled LDPC codes

- **Status**: ✅
- **Reason**: E: spatially-coupled LDPC 종단 구조(RA tail로 termination 단순화) — 바이너리 SC-LDPC 코드 설계 기법 이식 가능
- **ID**: ieee:7230548
- **Type**: conference
- **Published**: 12-15 July
- **Authors**: Junyang Ma, Zhongwei Si, Zhiqiang He
- **PDF**: https://ieeexplore.ieee.org/document/7230548
- **Abstract**: A recursive encoding of spatially coupled LDPC codes with low complexity has been proposed in recent works. But it has to solve a system of linear equations to terminate the codes. In this paper we modify the protograph of spatially coupled LDPC codes by adding extra variable nodes, called repeat-accumulate(RA) tail, which can simplify the termination without time delays. Performance analysis with density evolution and simulation results over binary erasure channel(BEC) channels are also provided. Simulation results show that, for spatially coupled LDPC codes with RA tail, the complexity of termination can be reduced with a small trade-off in performance.

## Reversible visible watermark embedded in encrypted domain

- **Status**: ❌
- **Reason**: 암호화 영역 가역 가시 워터마킹 — 보안/데이터하이딩, LDPC ECC와 무관
- **ID**: ieee:7230520
- **Type**: conference
- **Published**: 12-15 July
- **Authors**: Xinpeng Zhang, Zichi Wang, Jiang Yu +1
- **PDF**: https://ieeexplore.ieee.org/document/7230520
- **Abstract**: This work proposes a novel reversible visible watermarking scheme for encrypted images. In the scheme, the original plaintext image is encrypted by bit-wise exclusive-or operation. Although a data-hider does not know the original content, he may modify a part of encrypted data corresponding to the black pixels of a binary watermark image to insert the visible watermark. Meanwhile, some additional data used for content recovery are also embedded by using wet paper coding. After receiving the marked encrypted image, a user with the encryption key may perform direct decryption to obtain a visibly marked image, while a user with the encryption and data-hiding keys can perform data-extraction, image-decryption, and content-recovery to retrieve the original plaintext image.

## Early stopping criterion for message-passing decoding of LDLC

- **Status**: ❌
- **Reason**: LDLC(low-density lattice codes) 조기정지 기준 - 격자부호 전용, 바이너리 LDPC BP에 직접 이식 어려움
- **ID**: ieee:7224811
- **Type**: conference
- **Published**: 1-3 July 2
- **Authors**: Jin Xu, Can Duan, Danfeng Zhao +2
- **PDF**: https://ieeexplore.ieee.org/document/7224811
- **Abstract**: An early stopping criterion is proposed for low-density lattice codes (LDLC) to reduce the number of decoding iterations. The stopping criterion is based on a new metric which is used to predict the convergence of the iterative decoding algorithm for LDLC. Simulation results demonstrate that the proposed criterion can decrease the average iteration number considerably while the decoding performance degradation is within 0.2dB in the low symbol error rate region. Besides, the proposed criterion can provide a flexible tradeoff between performance and complexity.
