# IEEE Xplore — 2010-09


## LDPC Codes for Non-Uniform Memoryless Sources and Unequal Energy Allocation

- **Status**: ❌
- **Reason**: 비균일 소스용 에너지할당+SPA 적용, 소스코딩/변조 응용으로 표준 SPA만 사용 — 신규 디코더 기여 없음
- **ID**: ieee:5572892
- **Type**: journal
- **Published**: September 
- **Authors**: Idoia Ochoa, Pedro M. Crespo, Mikel Hernaez
- **PDF**: https://ieeexplore.ieee.org/document/5572892
- **Abstract**: In this paper, we design a new energy allocation strategy for non-uniform binary memoryless sources encoded by Low-Density Parity-Check (LDPC) codes and sent over Additive White Gaussian Noise (AWGN) channels. The new approach estimates the a priori probabilities of the encoded symbols, and uses this information to allocate more energy to the transmitted symbols that occur less likely. It can be applied to systematic and non-systematic LDPC codes, improving in both cases the performance of previous LDPC based schemes using binary signaling. The decoder introduces the source non-uniformity and estimates the source symbols by applying the SPA (Sum Product Algorithm) over the factor graph describing the code.

## Adaptive Modulation and Coding Schemes Based on LDPC Codes with Irregular Modulation

- **Status**: ❌
- **Reason**: 무선 적응변조/AMC+비정규변조 응용 특이적 — 떼어낼 LDPC ECC 기법 없음
- **ID**: ieee:5557648
- **Type**: journal
- **Published**: September 
- **Authors**: Seok-Ki Ahn, Kyeongcheol Yang
- **PDF**: https://ieeexplore.ieee.org/document/5557648
- **Abstract**: In this paper we propose an adaptive modulation and coding (AMC) scheme which uses only a single low-density parity-check (LDPC) encoder/decoder with irregular modulation. Two Gray-mapped quadrature-amplitude modulations are employed within a codeword so that the transmission rates of the proposed AMC can be controlled even though the rate of the employed LDPC code is fixed. The rate and degree distribution of the employed LDPC code are selected properly for the proposed scheme. We also optimize the bit-to-symbol mapping for the LDPC code over irregular modulation at each transmission rate. The performance of the proposed scheme is compared with that of the AMC scheme with a dedicated LDPC code at each transmission rate. Numerical results show that the proposed scheme has a performance comparable to that of the AMC scheme with dedicated LDPC codes.

## Capacity-Approaching Irregular Turbo Codes for the Binary Erasure Channel

- **Status**: ❌
- **Reason**: BEC용 비정규 터보부호 — 비-LDPC, 터보 인터리버/밀도진화로 LDPC BP 이식 기법 없음
- **ID**: ieee:5577801
- **Type**: journal
- **Published**: September 
- **Authors**: Ghassan M. Kraidy, Valentin Savin
- **PDF**: https://ieeexplore.ieee.org/document/5577801
- **Abstract**: In this paper, we propose a class of irregular turbo codes that approach the capacity of the binary erasure channel. First, an analytic expression of the erasure probability of punctured recursive systematic convolutional codes is derived. This expression will then be used to study the density evolution of turbo codes over the binary erasure channel, that will allow for the design of capacity-approaching infinite-length irregular turbo codes. Next, a graph-optimal interleaver for finite-length irregular turbo codes is proposed. Finally, simulation results for different coding rates are shown.

## Semi-Analytical Performance Prediction Methods for Iterative MMSE-IC Multiuser MIMO Joint Decoding

- **Status**: ❌
- **Reason**: MMSE-IC MIMO 다중사용자 결합디코딩 성능예측(EXIT) — 무선 응용, 떼어낼 LDPC ECC 기법 없음
- **ID**: ieee:5577805
- **Type**: journal
- **Published**: September 
- **Authors**: Raphael Visoz, Antoine O. Berthet, Massinissa Lalam
- **PDF**: https://ieeexplore.ieee.org/document/5577805
- **Abstract**: In this paper, two semi-analytical performance prediction methods are proposed and compared for multiuser MIMO transmission over block-fading multipath channels and iterative MMSE successive interference cancellation based joint decoding. In the first method, we develop a completely analytical parameterisation of the whole turbo receiver up to the users' channel decoders. The method which follows the classical framework of extrinsic information transfer charts tracks the evolution of the average mutual information defined at coded bit level and circulating between the multiuser detector and the bank of channel decoders. The modelling of the demapping output in the multiuser detector is based on an explicit calculation of the (conditional) mutual information for each symbol digit in a symbol label under arbitrary (possibly non-uniform) a priori probability distributions on others. Then, shifting in viewpoint and considering user demapping and decoding as a joint process, we present an alternative method which tracks the evolution of the average mutual information defined at symbol level and circulating between the MMSE successive interference based interface and the bank of joint demappers and channel decoders. This allows to avoid the critical issue of parameterising the demapping. Numerical results demonstrate the superiority of the second method for high-order non-linear mapping.

## Distance Bounds for Periodically Time-Varying and Tail-Biting LDPC Convolutional Codes

- **Status**: ❌
- **Reason**: LDPC convolutional code 거리 bound 순수 이론, 디코더·HW·구성으로 이어지지 않음
- **ID**: ieee:5550417
- **Type**: journal
- **Published**: Sept. 2010
- **Authors**: Dmitri Truhachev, Kamil Sh. Zigangirov, Daniel J. Costello
- **PDF**: https://ieeexplore.ieee.org/document/5550417
- **Abstract**: Existence type lower bounds on the free distance of periodically time-varying LDPC convolutional codes and on the minimum distance of tail-biting LDPC convolutional codes are derived. It is demonstrated that the bound on free distance of periodically time-varying LDPC convolutional codes approaches the bound on free distance of general (nonperiodic) time-varying LDPC convolutional codes as the period increases. The proof of the bound is based on lower bounding the minimum distance of corresponding tail-biting LDPC convolutional codes, which is of interest in its own right.

## Group Codes Outperform Binary-Coset Codes on Nonbinary Symmetric Memoryless Channels

- **Status**: ❌
- **Reason**: 비이진 group code vs binary-coset 이론적 거리/지수 분석, LDPC 디코더·구성 기여 없음
- **ID**: ieee:5550276
- **Type**: journal
- **Published**: Sept. 2010
- **Authors**: Giacomo Como
- **PDF**: https://ieeexplore.ieee.org/document/5550276
- **Abstract**: Typical minimum distances and error exponents are analyzed on the 8-PSK Gaussian channel for two capacity-achieving code ensembles with different algebraic structure. It is proved that the typical group code over the cyclic group of order eight achieves both the Gilbert-Varshamov bound and the expurgated error exponent. On the other hand, the typical binary-coset codes (under any labeling) is shown to be bounded away both from the Gilbert-Varshamov bound (at any rate) and the expurgated exponent (at low rates). The reason for this phenomenon is shown to rely on the symmetry structure of the 8-PSK constellation, which is known to match the cyclic group of order eight, but not the direct product of three copies of the binary group. The presented results indicate that designing group codes matching the symmetry of the channel guarantees better typical-code performance than designing codes whose algebraic structure does not match the channel. This contrasts the well-known fact that the average binary-coset code achieves both the capacity and the random-coding error exponent of any discrete memoryless channel.

## Cooperation in the Low Power Regime for the MAC Using Multiplexed Rateless Codes

- **Status**: ❌
- **Reason**: rateless/Raptor 코드 기반 협력통신 용량분석, LDPC 아님·떼어낼 ECC 기법 없음
- **ID**: ieee:5482064
- **Type**: journal
- **Published**: Sept. 2010
- **Authors**: Momin Uppal, Zigui Yang, Anders Host-Madsen +1
- **PDF**: https://ieeexplore.ieee.org/document/5482064
- **Abstract**: In this paper, we consider cooperation in the low power (low SNR) regime for the multiple access channel with the assumption that the transmitters have no channel state information. A relevant performance measure to consider is therefore the outage capacity. We develop cooperation methods based on multiplexed coding in conjunction with rateless codes and find the achievable rates and in particular the minimum energy per bit required to achieve a certain outage probability. We consider two modes of operation: full duplex [code-division multiple access (CDMA)], where nodes can transmit and receive simultaneously on the same frequency band, and half duplex [frequency-division multiple access (FDMA)], where the nodes transmit and listen on different frequency bands. We show that, perhaps surprisingly, there is little loss in performance when using FDMA. Furthermore, our results show that multiplexed rateless codes come within 0.1 dB of the outer bound on capacity. We also develop practical rateless coding methods for FDMA using multiplexed Raptor codes which operate within 0.52 and 1.1 dB of the theoretical limit for the two- and four-user case, respectively.

## Near Optimal Iterative Channel Estimation for KSP-OFDM

- **Status**: ❌
- **Reason**: KSP-OFDM 채널추정(EM/turbo) 무선통신 특이적, 떼어낼 LDPC 디코더·코드설계 기법 없음
- **ID**: ieee:5467224
- **Type**: journal
- **Published**: Sept. 2010
- **Authors**: Dieter Van Welden, Heidi Steendam
- **PDF**: https://ieeexplore.ieee.org/document/5467224
- **Abstract**: In this correspondence, we propose an iterative “turbo” channel estimation algorithm for known symbol padding (KSP) orthogonal frequency-division multiplexing (OFDM), where the guard interval is filled with pilot symbols. Additional pilot symbols are transmitted on some of the OFDM carriers. The channel estimation algorithm is based on the expectation-maximization (EM) algorithm. In the initialization phase of this iterative algorithm, the received time-domain samples are first converted to the frequency domain, and the initial channel estimate is based on the observation of the pilot carriers only. Then the EM-algorithm switches back to the time-domain and updates the channel estimates until convergence is reached. The proposed estimator performs very good: the mean square error (MSE) performance of the proposed estimator is close to the Cramér-Rao lower bound (CRB) corresponding to the all pilots case, for the SNR region of practical interest, and the resulting bit error rate essentially coincides with the case of the perfectly known channel.

## Spectral Classification and Multiplicative Partitioning of Constant-Weight Sequences Based on Circulant Matrix Representation of Optical Orthogonal Codes

- **Status**: ❌
- **Reason**: 광직교코드(OOC) 시퀀스 분류 이론, LDPC ECC와 무관
- **ID**: ieee:5550470
- **Type**: journal
- **Published**: Sept. 2010
- **Authors**: Mohammad M. Alem-Karladani, Jawad A. Salehi
- **PDF**: https://ieeexplore.ieee.org/document/5550470
- **Abstract**: Considering the space of constant-weight sequences as the reference set for every optical orthogonal code (OOC) design algorithm, we propose a classification method that preserves the correlation properties of sequences. First, we introduce the circulant matrix representation of optical orthogonal codes and, based on the spectrum of circulant matrices, we define the spectral classification of the set Sn,w of all (0, 1)-sequences with length n, weight w, and the first chip “1”. Then, as a method for spectrally classifying the set Sn,w, we discuss an algebraic structure called multiplicative group action. Using the above multiplicative group action, we define an equivalence relation on Sn,w in order to classify it into equivalence classes called multiplicative partitions which are the same as the spectral classes. The algebraic properties of the proposed partitioning such as the number of classes and the size of each class are investigated and in the case of prime n, a novel formula for the number of classes is derived. Finally, we present and prove the autocorrelation, intraclass and interclass cross-correlation properties of our proposed classification of the space Sn,w that decrease the computational complexity of search algorithms in designing and constructing (n, w, λa,λc)-OOC.

## Low-power techniques for flexible channel decoders

- **Status**: ❌
- **Reason**: Turbo 코드 조기정지 규칙 중심의 저전력 채널디코더, LDPC 비의존 아니고 turbo 전용
- **ID**: ieee:5599606
- **Type**: conference
- **Published**: 8-9 Sept. 
- **Authors**: Giuseppe Gentile, Massimo Rovini, Luca Fanucci
- **PDF**: https://ieeexplore.ieee.org/document/5599606
- **Abstract**: This paper proposes a framework for a low-power design of flexible multi-standard channel decoders which are the most computational demanding blocks of modern communication systems. A power-efficient design envisages hardware level techniques to reduce static power consumption and algorithmic level technique to early stop the iterative decoding when the received information is estimated to be correct. Particularly, the paper focuses on two different stopping rules for Turbo codes which are well-suited for a multi-standard scenario. Simulation results indeed show an achievable power saving ranging from 50% to 80%.

## Low-Density Parity-Check Codes for Two-Way Relay Channels

- **Status**: ❌
- **Reason**: 양방향 릴레이 채널용 LDPC와 간섭제거 결합 디코더 - 무선 릴레이 응용 특이적, NAND 이식 불가
- **ID**: ieee:5594222
- **Type**: conference
- **Published**: 6-9 Sept. 
- **Authors**: Xin Sheng Zhou, Liang-Liang Xie, Xuemin Shen
- **PDF**: https://ieeexplore.ieee.org/document/5594222
- **Abstract**: In this paper, we propose Low-density Parity-check (LDPC) codes for two-way relay channels, where two sources communicate with each other through a relay. At the relay, a simpler interference cancellation joint decoder decodes for the multiple access phase of two-way relay channels. Then, the relay codeword is encoded from two decoded source codewords with LDPC codes. At source, a sub-optimal belief propagation decoder decodes message from codewords received from the relay, the other source and its own source. Simulation results are given to show that our proposed simpler interference cancellation joint decoder at the relay is only 0.2 dB away from the existing sub-optimal belief propagation joint decoder. The required Eb/No at the source is 1.5 dB less than that of the single user channel with the same bit error rate (BER).

## Designing LDPC Codes with Gated Noise Model for Terrestrial Mobile DTV Channels

- **Status**: ❌
- **Reason**: 모바일 DTV 버스트오류용 dual-degree IRA 코드 설계 - 무선 응용 특이적, NAND에 이식할 바이너리 LDPC 디코더/구성 기법 없음
- **ID**: ieee:5594173
- **Type**: conference
- **Published**: 6-9 Sept. 
- **Authors**: Bo Liu, Liang Gong, Yin Xu +5
- **PDF**: https://ieeexplore.ieee.org/document/5594173
- **Abstract**: This paper investigates the design of LDPC codes over mobile DTV multipath channels. Most of the existing LDPC codes are optimized for additive white Gaussian noise (AWGN) channel, and not feasible to encounter the long burst error occurring in mobile DTV channel. Accordingly, we study the error propagation statistics of decision feedback equalizer (DFE) and formulate it into a gated noise model. To achieve good error correction in burst error channel, we proposed a class of dual-degree IRA codes to balance the metrics of decoding threshold and robustness. Extensive simulation results are presented in this paper to justify the performance of dual-degree IRA codes over gated noise model.

## Spectrally Efficient Cooperative Scheme with Implicit Feedback Assisted Transmission

- **Status**: ❌
- **Reason**: 협력 무선 incremental redundancy 전송 기법 - LDPC는 베이스라인 사용, 떼어낼 ECC 기법 없음
- **ID**: ieee:5594323
- **Type**: conference
- **Published**: 6-9 Sept. 
- **Authors**: Ashish James, A. S. Madhukumar, Ernest Kurniawan +1
- **PDF**: https://ieeexplore.ieee.org/document/5594323
- **Abstract**: In this paper, an incremental redundancy based cooperative coding scheme for wireless networks is proposed. User cooperation is an effective way of mitigating fading where one user cooperates with another user in transmitting its information, thereby providing spatial diversity. Wireless transmissions are broadcast by nature and this provides a new dimension to the system in terms of an implicit feedback channel from the relay to the source. To exploit the implicit feedback channel a novel incremental redundancy based transmission scheme called incremental code relaying with implicit feedback (ICRIF) is proposed. This scheme enhances the reliability of information transmitted by the relay and thereby improving the throughput at the destination. By employing a powerful code such as low-density parity-check (LDPC) code, the benefit of the proposed scheme is clearly established. The simplified error probability for correct reception of the proposed scheme is derived with respect to direct transmissions and transmissions assisted by the relay.

## Performance Comparison of BICM-ID and BILDPCM-ID Based Cooperative Network

- **Status**: ❌
- **Reason**: 협력 네트워크 BICM-ID vs BILDPCM-ID 성능 비교 - LDPC는 부수 사용, 떼어낼 디코더/구성 기법 없음
- **ID**: ieee:5594176
- **Type**: conference
- **Published**: 6-9 Sept. 
- **Authors**: Shujaat Ali Khan Tanoli, Imran Khan, Nandana Rajatheva
- **PDF**: https://ieeexplore.ieee.org/document/5594176
- **Abstract**: In this paper the performance of bit-interleaved coded modulation with iterative decoding (BICM-ID) based multiple-relay cooperative system is analyzed over Nakagami-$m$ fading channels. The relays are operating in amplify-and-forward (AF) mode. The moment generating function (MGF) based approach is used to obtain the theoretical error-free feedback (EF) bounds. The results show that a significant gain is obtained in the performance of the system due to cooperative and code diversities by introducing cooperating relays and bit-interleaved coded modulation with iterative decoding. The performance of bit-interleaved low-density parity-check coded modulation with iterative decoding (BILDPCM-ID) based cooperative system, using low-density parity-check (LDPC) code instead of convolutional code, is also analyzed in term of bit-error rate (BER). The performance comparisons of BICM-ID and BILDPCM-ID based systems are shown using the set partitioning (SP) labelling for 8PSK modulation scheme. The BER curves are obtained by performing the Monte Carlo simulation.

## A Novel Digital Coded Track Signal-ITRS Based on TVM430

- **Status**: ❌
- **Reason**: 철도 신호(TVM430) 코딩 설계 - LDPC 무관, ECC 기법 없음
- **ID**: ieee:5594432
- **Type**: conference
- **Published**: 6-9 Sept. 
- **Authors**: Yong Kong, Zhen-Hui Tan, Pu-Xuan Du +1
- **PDF**: https://ieeexplore.ieee.org/document/5594432
- **Abstract**: With the developing of the high-speed railways, the requirement for railway signalling turns more and more strict. Came from France, the TVM430 signal has more information up to 27 bits digital word, with each bit corresponding to one of the 27 frequencies modulated onto the carrier frequency in the track circuits. The presence of a particular frequency indicates a "1" bit and lack of corresponds to a "0". But the slow demodulation is the biggest flaw for TVM430. To solve the above problems, we design a new digital coded track signal - Improved TVM430 Railway Signalling (ITRS). ITRS reduces the number of TVM430's modulation frequency while provides the same information capacity as TVM430. We also search for cycle generating polynomial, add parity checking to the important code - speed identification code. New frequency, amplitude and phase are defined for frequency modulated signals. ITRS performs better in information capacity, reliability and demodulation speed.

## Decision-Directed Carrier Phase and Symbol Timing Recovery for LDPC-Coded Systems

- **Status**: ❌
- **Reason**: LDPC-coded 시스템의 반송파/심볼타이밍 동기화(decision-directed) - 동기화 기법, 떼어낼 LDPC 디코더/구성 기법 아님
- **ID**: ieee:5594466
- **Type**: conference
- **Published**: 6-9 Sept. 
- **Authors**: Hua Wang, Nan Wu, Jingming Kuang +1
- **PDF**: https://ieeexplore.ieee.org/document/5594466
- **Abstract**: In this paper, we consider the effect of different rules of symbol decision on the performance of decision-directed synchronizers for LDPC-coded systems. Different from the conventional hard symbol decision based on the Maximum-A- Posteriori (MAP) criterion, soft symbol decision can be considered as the Minimum-Mean-Square-Error (MMSE) estimation of the transmitted symbol. By whether or not the coding constraints are taken into account, soft symbol decision is derived in non-code-aided (NCA) mode and code-aided (CA) mode, respectively. The performance of the soft decision-directed (SDD) synchronizer is compared with that of the hard decision-directed (HDD) counterpart in both NCA and CA mode. Simulation results show that, without much implementation complexity increase, the jitter performance of the synchronizer in CA mode significantly outperforms that in NCA mode. It is also observed that, in the scenario of this paper, SDD synchronizer works only slightly better than HDD synchronizer.

## Joint Network and Channel Decoding for HARQ in Wireless Broadcasting System

- **Status**: ❌
- **Reason**: 무선 브로드캐스트 HARQ 네트워크+채널 결합 디코딩 - 무선 응용 특이적, NAND 이식 가능 LDPC 기법 없음
- **ID**: ieee:5594394
- **Type**: conference
- **Published**: 6-9 Sept. 
- **Authors**: Yuan Zhao, Xiaoxiang Wang, Song Li
- **PDF**: https://ieeexplore.ieee.org/document/5594394
- **Abstract**: This paper presents a novel joint network and channel decoding-interference canceling (JNCD-IC) algorithm for HARQ in wireless broadcasting system. In this system, the base station uses network coding for retransmission. In the retransmission phase, JNCD-IC scheme is proposed for the receivers to recover multiple error packets from the composite packet which is formed by XORing error packets from different receivers. Traditionally, receivers can only recovery one error packet from the composite packet using XOR method when it knows all the other packets in this composite packet as a prior, while the JNCD-IC scheme is trying to recovery multiple error packets from the composite packet by treating the network code and channel code as a single parity check product code. Simulation results for Rayleigh block fading channel show a significant increase in throughput compared to the current schemes.

## Fountain codes with multiplicatively repeated non-binary LDPC codes

- **Status**: ❌
- **Reason**: non-binary LDPC 기반 fountain code - 비이진 LDPC 제외
- **ID**: ieee:5613905
- **Type**: conference
- **Published**: 6-10 Sept.
- **Authors**: Kenta Kasai, Kohichi Sakaniwa
- **PDF**: https://ieeexplore.ieee.org/document/5613905
- **Abstract**: We study fountain codes transmitted over the binary-input symmetric-output channel. For channels with small capacity, receivers needs to collects many channel outputs to recover information bits. Since a collected channel output yields a check node in the decoding Tanner graph, the channel with small capacity leads to large decoding complexity. In this paper, we introduce a novel fountain coding scheme with non-binary LDPC codes. The decoding complexity of the proposed fountain code does not depend on the channel. Numerical experiments show that the proposed codes exhibit better performance than conventional fountain codes, especially for small number of information bits.

## Robust clipping demapper for LDPC decoding in impulsive channel

- **Status**: ❌
- **Reason**: 임펄스 채널용 clipping demapper 파라미터 튜닝 — 무선/채널 특이적, NAND에 떼어낼 LDPC 기법 없음
- **ID**: ieee:5613845
- **Type**: conference
- **Published**: 6-10 Sept.
- **Authors**: Hassen Ben Mâad, Alban Goupil, Laurent Clavier +1
- **PDF**: https://ieeexplore.ieee.org/document/5613845
- **Abstract**: Low-Density Parity-Check codes, are a class of linear block codes and have recently received a great deal of attention owing to their excellent performances over Additive White Gaussian Noise channels. However they are not well investigated in non-Gaussian environments, for instance when the noise is impulsive. In this paper we discuss the use of clipping to mitigate the effect of impulsive noise modeled as an α-stable random variable. The slope in the linear section of the demapper and the threshold have a significant impact on the Belief Propagation decoder performance. We show that judicious choices of those parameters can result in an important performance improvement.

## Design of network-coding based multi-edge type LDPC codes for a multi-source relaying system

- **Status**: ❌
- **Reason**: 릴레이 다중소스 네트워크코딩 multi-edge LDPC EXIT 최적화, 무선 응용 특이적 코드프로파일이라 NAND 이식 기법 없음
- **ID**: ieee:5613817
- **Type**: conference
- **Published**: 6-10 Sept.
- **Authors**: Jun Li, Marwan H. Azmi, Robert Malaney +1
- **PDF**: https://ieeexplore.ieee.org/document/5613817
- **Abstract**: In this paper we investigate a multi-source LDPC coding scheme for a Gaussian relay system, where M sources communicate with the destination under the help of a single relay (M - 1 - 1 system). More specifically, we propose a network coded LDPC coding scheme for the M - 1 - 1 system where network coding over all sources' data is performed at the relay. A challenge in such a scheme is the code design for asymmetric channels where each source has different code rate. To address this issue, we present here a novel scheme named network coded multi-edge type LDPC code (NCMET-LDPC). Within NCMETLDPC we optimize the code profiles by EXIT charts, and show that the our coding scheme achieves better bit error rate (BER) performance relative to existing schemes.

## Novel LDPC code structures for the nonergodic block-fading channels

- **Status**: ❌
- **Reason**: block-fading 채널 전용 Root-Check LDPC 다이버시티 설계, 무선 채널 특이적 코드설계로 NAND 이식성 낮음
- **ID**: ieee:5613872
- **Type**: conference
- **Published**: 6-10 Sept.
- **Authors**: Jun Li, Jinhong Yuan, Marwan H. Azmi +1
- **PDF**: https://ieeexplore.ieee.org/document/5613872
- **Abstract**: In this paper we study LDPC code design in block-fading (BF) channels. Our main purpose is to introduce a new Root Check (RC)-LDPC code design which obtains full diversity whilst delivering improved coding gain relative the other LDPC code designs. More specifically, we show that when our codes are combined with the check splitting method for the ARQ BF channels, we obtain the highest coding gain relative to conventional RC-LDPC codes.

## Protograph-based q-ary LDPC codes for higher-order modulation

- **Status**: ❌
- **Reason**: GF(16) 비이진 q-ary LDPC - 비이진 제외 대상
- **ID**: ieee:5613806
- **Type**: conference
- **Published**: 6-10 Sept.
- **Authors**: Andrea Marinoni, Pietro Savazzi, Richard D. Wesel
- **PDF**: https://ieeexplore.ieee.org/document/5613806
- **Abstract**: This paper introduces a protograph-based method for designing q-ary LDPC codes for use with modulations larger than QPSK. Simulations focus on a GF(16), 16-QAM example. The proposed construction method achieves the maximum gain when the average column weight is chosen so that the linear minimum distance growth property is satisfied. In this region, the benefit of a protograph-based design over a standard PEG approach was 0.3 dB. We found that a careful field-element selection algorithm provides about 0.1 dB of improvement over random field-element selection. Overall, the proposed improvements yielded 0.4 dB of gain over a PEG-based GF(16) code with randomly selected Galois field elements. The performance of this baseline GF(16) code was comparable to the best known binary LDPC code for 16-QAM, so that the proposed improvements allow the GF(16) LDPC code to outperform known binary approaches.

## A symbol-reliability based message-passing decoding algorithm for nonbinary LDPC codes over finite fields

- **Status**: ❌
- **Reason**: 비이진(GF(q)) LDPC 메시지패싱 디코더 — 비이진 LDPC는 제외 대상
- **ID**: ieee:5613849
- **Type**: conference
- **Published**: 6-10 Sept.
- **Authors**: Chao Chen, Baoming Bai, Xiao Ma +1
- **PDF**: https://ieeexplore.ieee.org/document/5613849
- **Abstract**: Based on the idea of plurality voting, we develop a low-complexity symbol-reliability based message-passing decoding algorithm for nonbinary low-density parity-check (LDPC) codes over finite fields. A key feature of the algorithm is that the message passed in the Tanner graph is the field element with the highest reliability. This leads to a very simple check node update. The algorithm requires only finite and integer operations. Moreover, the estimation of the signal-to-noise ratio (SNR) is not needed. Compared to the Fast Fourier Transform based q-ary sum-product algorithm (FFT-QSPA), the proposed decoding algorithm provides an excellent trade-off between performance and complexity for the nonbinary LDPC codes constructed based on finite geometries, finite fields and cyclotomic cosets.

## Exploiting the CRC-CCITT code on the binary erasure channel

- **Status**: ❌
- **Reason**: CRC-CCITT 외부부호+인터리버, 비-LDPC 부호 중심으로 떼어낼 바이너리 LDPC 기법 없음
- **ID**: ieee:5613897
- **Type**: conference
- **Published**: 6-10 Sept.
- **Authors**: Eirik Rosnes, Guang Yang, Øyvind Ytrehus
- **PDF**: https://ieeexplore.ieee.org/document/5613897
- **Abstract**: Cyclic redundancy check (CRC) codes are designed for error detection, but can in principle be used for error correction. In this work, we analyze the performance of the CRC-CCITT code, both as a stand-alone code, and as the outer code in a serially concatenated code with an inner low-density parity-check code on the binary erasure channel. To optimize the recovery failure probability for low channel erasure probabilities, we propose to add a permutation/interleaver between the outer and inner codes in order to increase the overall stopping distance.

## Interactive reconciliation with low-density parity-check codes

- **Status**: ❌
- **Reason**: QKD 정보조정(reconciliation) puncturing/shortening 프로토콜 — 채널 ECC 아닌 정보조정, 떼어낼 신규 디코더/HW 기법 없음
- **ID**: ieee:5613856
- **Type**: conference
- **Published**: 6-10 Sept.
- **Authors**: Jesús Martínez-Mateo, David Elkouss, Vicente Martín
- **PDF**: https://ieeexplore.ieee.org/document/5613856
- **Abstract**: Efficient information reconciliation is crucial in several scenarios, being quantum key distribution a remarkable example. However, efficiency is not the only requirement for determining the quality of the information reconciliation process. In some of these scenarios we find other relevant parameters such as the interactivity or the adaptability to different channel statistics. We propose an interactive protocol for information reconciliation based on low-density parity-check codes. The coding rate is adapted in real time by using simultaneously puncturing and shortening strategies, allowing it to cover a predefined error rate range with just a single code. The efficiency of the information reconciliation process using the proposed protocol is considerably better than the efficiency of its non-interactive version.

## Complexity evaluation of non-binary Galois field LDPC code decoders

- **Status**: ❌
- **Reason**: 비이진 GF(4/16/256) LDPC 디코더 HW 복잡도 평가. non-binary LDPC 제외
- **ID**: ieee:5613874
- **Type**: conference
- **Published**: 6-10 Sept.
- **Authors**: Timo Lehnigk-Emden, Norbert Wehn
- **PDF**: https://ieeexplore.ieee.org/document/5613874
- **Abstract**: Forward error correction is an essential part of digital communication systems. Non-binary low-density parity-check (NB-LDPC) codes have an excellent communications performance for short block lengths. The higher the field size is, the better the communications performance is. Non-binary LDPC codes can outperform all other state-of-the-art code classes. However, the algorithmic decoding complexity grows with the field size. For an intended, future use of these codes in real systems, an efficient hardware implementation is mandatory. Hardware architectures for binary LDPC codes are well investigated, but efficient implementation of non-binary LDPC decoders is still an open field. To the best of our knowledge, this paper studies for the first time the hardware implementation costs for non-binary LDPC decoders with Galois field sizes of 4, 16 and 256 on FPGA and a 65nm ASIC technology.

## LDPC code design for transmission of correlated sources across noisy channels without CSIT

- **Status**: ❌
- **Reason**: 상관소스 전송용 LDPC 설계, 소스 상관/JSCC 채널 적응 응용 특이적이라 떼어낼 ECC 기법 없음
- **ID**: ieee:5613829
- **Type**: conference
- **Published**: 6-10 Sept.
- **Authors**: Arvind Yedla, Henry D. Pfister, Krishna R. Narayanan
- **PDF**: https://ieeexplore.ieee.org/document/5613829
- **Abstract**: We consider the problem of transmitting correlated data after independent encoding to a central receiver through orthogonal channels. We assume that the channel state information is not known at the transmitter. The receiver has access to both the source correlation and the channel state information. We provide a generic framework for analyzing the performance of joint iterative decoding, using density evolution. Using differential evolution, we design punctured systematic LDPC codes to maximize the region of achievable channel conditions, with joint iterative decoding. The main contribution of this paper is to demonstrate that properly designed LDPC can perform well simultaneously over a wide range of channel parameters.

## Joint factor graph detection for LDPC and STBC coded MIMO systems: A new framework

- **Status**: ❌
- **Reason**: LDPC+STBC MIMO 결합 factor graph 검출, MIMO 채널 의존 무선 응용 특이적이라 떼어낼 ECC 기법 없음
- **ID**: ieee:5613820
- **Type**: conference
- **Published**: 6-10 Sept.
- **Authors**: Jianxiao Yang, Charbel Abdel Nour, Charlotte Langlais
- **PDF**: https://ieeexplore.ieee.org/document/5613820
- **Abstract**: By modeling the corresponding MIMO channel as a factor graph (FG), STBC decoder, bit interleaver and LDPC decoder can be combined together to form a larger joint factor graph (JFG). Extrinsic information transfer (EXIT) charts and bit error rate (BER) results show that the JFG enables a shuffled decoding superior to the classical serial iterative detection in performance while reducing complexity.

## Non-asymmetric Slepian-Wolf coding of non-uniform Bernoulli sources

- **Status**: ❌
- **Reason**: Slepian-Wolf 분산 소스 코딩(LDPC를 소스코딩에 사용), 채널 ECC 아님. 제외
- **ID**: ieee:5613888
- **Type**: conference
- **Published**: 6-10 Sept.
- **Authors**: V. Toto-Zarasoa, A. Roumy, C. Guillemot
- **PDF**: https://ieeexplore.ieee.org/document/5613888
- **Abstract**: We address the problem of non-asymmetric Slepian-Wolf (SW) coding of two correlated non-uniform Bernoulli sources. We first show that the problem is not symmetric in the two sources, contrarily to the case of uniform sources, due to the asymmetry induced by two underlying channel models, namely additive and predictive Binary Symmetric Channels (BSC). That asymmetry has to be accounted for during the decoding. In view of that result, we describe the implementation of a joint non-asymmetric decoder of the two sources based on Low-Density Parity-Check (LDPC) codes and Message Passing (MP) decoding. We also give a necessary and sufficient condition for the recovery of the two sources, that imposes a triangular structure of a sub-part of the equivalent matrix representation of the code.

## A lower bound for the minimum distance of intersection codes

- **Status**: ❌
- **Reason**: intersection code 최소거리 하한 순수 이론 bound, 디코더/HW/구성으로 안 이어짐
- **ID**: ieee:5613889
- **Type**: conference
- **Published**: 6-10 Sept.
- **Authors**: Christian Franck, Uli Sorger
- **PDF**: https://ieeexplore.ieee.org/document/5613889
- **Abstract**: Intersection codes are a superclass of Turbo- and LDPC codes. This class contains codes constructed by intersecting interleaved constituent codes. We propose a lower bound for the minimum distance of these codes. Using this bound, we compare intersection codes obtained from different constituent codes.

## Calculating the minimum distance of linear block codes via Integer Programming

- **Status**: ❌
- **Reason**: IP로 최소거리 계산하는 분석 도구, 주대상 turbo 부호이며 떼어낼 디코더/HW/구성 기법 없음
- **ID**: ieee:5613894
- **Type**: conference
- **Published**: 6-10 Sept.
- **Authors**: Mayur Punekar, Frank Kienle, Norbert Wehn +3
- **PDF**: https://ieeexplore.ieee.org/document/5613894
- **Abstract**: In recent years several authors have used Integer Programming (IP) formulations to model the Maximum Likelihood (ML) decoding problem. IP formulation of the ML decoding problem can be modified to calculate the minimum distance of the code also. The IP based approach for MD calculation can be effectively used for small block length codes. However, it is not known if this approach is useful for the moderate and long length codes used in practice. In this paper we demonstrate the usefulness of the IP based approach for the MD calculation by applying it to practically relevant codes. We calculate either the true MD or upper bounds on the MD for 3GPP LTE turbo codes, WiMax duo-binary turbo codes and WiMax & WiFi low density parity-check codes. A new IP formulation is also introduced to calculate the MD of punctured turbo codes. Along with MD calculation, the same IP formulation is used to find multiplicity of low weight codewords. Our results prove that, the IP based approach can estimate the MD of practically relevant codes fairly quickly and can also provide information about the multiplicity of codewords with a given Hamming weight. Also, the IP based method for the MD calculation is independent of the code used and can easily accommodate puncturing schemes.

## Optimized variable degree matched mapping for protograph LDPC coded modulation with 16QAM

- **Status**: ❌
- **Reason**: Protograph LDPC coded modulation 16QAM VDMM 최적화, 변조-매핑 무선 응용 특이적
- **ID**: ieee:5613828
- **Type**: conference
- **Published**: 6-10 Sept.
- **Authors**: Yi Jin, Ming Jiang, Chunming Zhao
- **PDF**: https://ieeexplore.ieee.org/document/5613828
- **Abstract**: The protograph LDPC (P-LDPC) coded modulation is an efficient scheme using the variable degree matched mapping (VDMM) based on the protograph structure. We propose a VDMM optimization strategy, as a crucial part for the P-LDPC coded modulation, by checking different permutation patterns between the variable nodes in protograph and the modulated bits. Then, we develop a modified EXIT analysis for evaluating the thresholds for P-LDPC coded modulation. For some specified P-LDPC codes and 16QAM constellations, the optimum patterns for VDMM can be obtained by a limited number of searches based on the modified EXIT analysis. We find that for a certain labeling, the edge distributions of the protogragh structure should be taken into consideration, rather than using the water-filling strategy or BICM approach. Decoding simulations, being consistent with the numerical analysis results, show that P-LDPC coded modulation with the optimum pattern noticeably outperforms that with the conventional water-filling pattern.

## The missed message of the cutoff rate

- **Status**: ❌
- **Reason**: cutoff rate 역사·이론 논평 — 순수 이론, 디코더/HW/구성으로 안 이어짐
- **ID**: ieee:5613859
- **Type**: conference
- **Published**: 6-10 Sept.
- **Authors**: Richard E. Blahut
- **PDF**: https://ieeexplore.ieee.org/document/5613859
- **Abstract**: The history of the cutoff rate is reviewed. It is argued that the cutoff rate is a fundamental constant associated with each discrete memoryless channel. It is the largest rate for which maximum-likelihood (or minimum-distance) decoding is tractable for that channel. This statement is the appropriate backdrop against which to see recent progress in coding.

## Simplified check node processing in nonbinary LDPC decoders

- **Status**: ❌
- **Reason**: 비이진 GF(64) LDPC check node 처리(Bubble Check), non-binary LDPC라 제외
- **ID**: ieee:5613839
- **Type**: conference
- **Published**: 6-10 Sept.
- **Authors**: E. Boutillon, L. Conde-Canencia
- **PDF**: https://ieeexplore.ieee.org/document/5613839
- **Abstract**: This paper deals with low-complexity algorithms for the check node processing in nonbinary LDPC decoders. After a review of the state-of-the-art, we focus on an original solution to significantly reduce the order of complexity of the Extended Min-Sum decoder at the elementary check node level. The main originality of the so-called Bubble Check algorithm is the two-dimensional strategy for the check node processing, which leads to a reduction of the number of comparisons. The simulation results obtained for the Bubble Check show that this complexity reduction does not introduce any performance loss and that it is even possible to further reduce the number of comparisons. This motivated the search of a simplified architecture and led to the L-Bubble Check, which is the main contribution of the paper. The implementation of a forward/backward check node as a systolic architecture of L-Bubble elementary checks is also described. Finally, some FPGA synthesis results of a whole GF(64)-LDPC decoder implementation are presented.

## Progressive encoding with non-linear source codes for compression of low-entropy sources

- **Status**: ❌
- **Reason**: 소스 코딩(저엔트로피 소스 압축), 채널 ECC 아님. 제외
- **ID**: ieee:5613878
- **Type**: conference
- **Published**: 6-10 Sept.
- **Authors**: Francisco Ramirez Javega, Meritxell Lamarca, Javier Garcia-Frias
- **PDF**: https://ieeexplore.ieee.org/document/5613878
- **Abstract**: We propose a novel scheme for source coding of non-uniform memoryless binary sources based on progressively encoding the input sequence with non-linear encoders. At each stage, a number of source bits is perfectly recovered, and these bits are thus not encoded in the next stage. The last stage consists of an LDPC code acting as a source encoder over the bits that have not been recovered in the previous stages.

## Design of non-binary decoders using the role model framework

- **Status**: ❌
- **Reason**: 비이진(non-binary) LDPC 디코더 (rank 기반 메시지패싱). 기준상 non-binary LDPC는 제외
- **ID**: ieee:5613868
- **Type**: conference
- **Published**: 6-10 Sept.
- **Authors**: Jossy Sayir
- **PDF**: https://ieeexplore.ieee.org/document/5613868
- **Abstract**: The concept of a message-passing decoder for non-binary low-density parity-check (LDPC) codes that operates on symbol rankings instead of probability distributions is investigated. The optimal Bayesian conversion from ranks back to probabilities is derived, and the hypothetical performance of a rank-based algorithm is measured by converting the rank-valued messages back to probabilities and implementing the node operations in the probability domain. While the performance of a pure rank-based decoder is disappointing, further analysis and performance evaluation shows that a hybrid decoder that switches to the probability domain for its final iteratons exhibits a performance at par with the best known low complexity decoders without causing a significant increase in the overall number of iterations.

## A universal coding approach for superposition mapping

- **Status**: ❌
- **Reason**: superposition mapping용 LDHC 변조-코딩, 무선 SM 응용 특이적·떼어낼 바이너리 LDPC ECC 기법 없음
- **ID**: ieee:5613890
- **Type**: conference
- **Published**: 6-10 Sept.
- **Authors**: Tianbin Wo, Peter Adam Hoeher
- **PDF**: https://ieeexplore.ieee.org/document/5613890
- **Abstract**: Superposition mapping (SM) is a modulation technique that uses linear superposition to produce Gaussian-like data symbols. Communication systems employing SM have a theoretical potential to approach the Gaussian channel capacity without using active signal shaping. This paper tackles several critical issues of SM and provides corresponding solutions. We point out that repetition coding is often an indispensable part for SM systems, a topic which has been obscured for a long time. More importantly, the bandwidth efficiency limit of SM systems with equal power allocation of about 2 bits per symbol per dimension can be eliminated by using irregular repetition codes. Following this cognition, we propose a universal coding approach, called low-density hybrid-check (LDHC) coding, for SM systems with arbitrary power allocation.

## Interblock memory for turbo trellis coded modulation

- **Status**: ❌
- **Reason**: turbo TCM 변조 스킴, LDPC 무관·이식할 BP 기법 없음. 비-LDPC 부호 제외
- **ID**: ieee:5613870
- **Type**: conference
- **Published**: 6-10 Sept.
- **Authors**: Yeong-Luh Ueng, Chia-Jung Yeh, Mao-Chao Lin
- **PDF**: https://ieeexplore.ieee.org/document/5613870
- **Abstract**: This paper presents a turbo trellis coded modulation (TTCM) scheme for which the encoding is implemented by serially concatenating a demultiplexer, a multilevel delay processor, and a signal mapper to the encoder of a binary turbo code. Through the delay processor and the signal mapper, interblock memory is introduced between consecutive binary turbo codewords. The proposed TTCM can be decoded based on the demapper and the binary turbo decoder. We can design a TTCM with a rate of 2 bits per 8PSK symbol and a pinch-off limit of 3.08 dB which is only 0.18 dB away from the capacity (2.9 dB).

## Bounds on thresholds related to maximum satisfiability of regular random formulas

- **Status**: ❌
- **Reason**: SAT 임계값 bound 순수 이론, 디코더/HW/코드설계로 안 이어짐
- **ID**: ieee:5613816
- **Type**: conference
- **Published**: 6-10 Sept.
- **Authors**: Vishwambhar Rathi, Erik Aurell, Lars Rasmussen +1
- **PDF**: https://ieeexplore.ieee.org/document/5613816
- **Abstract**: We consider the regular balanced model of satisfiability formula generation in conjunctive normal form (CNF), where each literal participates in equal number of clauses and there are k literals participating in a clause. We say that a formula is p-satisfying if there is a truth assignment satisfying 1–2−k+p2−k fraction of clauses. Using the first moment method we determine upper bound on the threshold clause density such that there are no p-satisfying assignments with high probability above this upper bound. There are two aspects in deriving the lower bound using the second moment method. The first aspect is, given any p ∈ (0;1) and k, evaluate the lower bound on the threshold. This evaluation is numerical in nature. The second aspect is to derive the lower bound as a function of p for large enough k. We address the first aspect and evaluate the lower bound on the p-satisfying threshold using the second moment method. Based on the numerical evaluation, we observe that as k increases the ratio of the lower bound and the upper bound seems to converge to one.

## Design optimization of iterative receivers

- **Status**: ❌
- **Reason**: MIMO-OFDM CFO/채널 추정 iterative receiver, LDPC 부수 언급 무선 응용 특이적
- **ID**: ieee:5613819
- **Type**: conference
- **Published**: 6-10 Sept.
- **Authors**: S. Salari, V. Meghdadi, J.P. Cances
- **PDF**: https://ieeexplore.ieee.org/document/5613819
- **Abstract**: In this paper, we consider design optimization of low-density parity-check (LDPC) coded multiple-input multiple-output (MIMO) orthogonal frequency division multiplexing (OFDM) systems for high data rate wireless transmission. First, starting from the maximum-likelihood (ML) principle, we devise a novel expectation-maximization (EM)-based scheme for joint estimation of carrier frequency-offset (CFO) and channel coefficients in MIMO-OFDM systems. Based on simulation results, the performance of joint estimator is quite satisfying. Then, this CFO estimator is incorporated into the initialization step of the turbo receiver. Experimental results show the effectiveness of our receiver design in combating CFO over unknown frequency selective fading channels.

## Turbo code design for H-ARQ with cross-packet channel coding

- **Status**: ❌
- **Reason**: Turbo code design for H-ARQ cross-packet coding; 비-LDPC 부호이고 떼어낼 LDPC BP 이식 기법 없음
- **ID**: ieee:5613815
- **Type**: conference
- **Published**: 6-10 Sept.
- **Authors**: Christoph Hausl, Daniele Capirone
- **PDF**: https://ieeexplore.ieee.org/document/5613815
- **Abstract**: In wireless scenarios a simple and effective method to increase the reliability for time-varying channels is the hybrid automatic repeat request (H-ARQ) protocol. Recently, a H-ARQ scheme with cross-packet channel coding (CPC) has been proposed to increase the maximum coding rate at which full-diversity can be achieved. In this paper, CPC based on turbo codes is analyzed with EXIT charts. This allows to find a suitable CPC design. Simulation results show that the designed code outperforms the previous approach, providing full-diversity and good coding gain also at high coding rates.

## Multiple-packet versus single-packet incremental redundancy strategies for type-II hybrid ARQ

- **Status**: ❌
- **Reason**: HARQ incremental redundancy 패킷 전략 — 채널코딩 ECC 디코더/구성 아님, NAND 무관
- **ID**: ieee:5613846
- **Type**: conference
- **Published**: 6-10 Sept.
- **Authors**: Moustapha El Aoun, Raphaël Le Bidan, Xavier Lagrange +1
- **PDF**: https://ieeexplore.ieee.org/document/5613846
- **Abstract**: In classical incremental redundancy (IR) hybrid ARQ schemes, successive retransmissions consist of different redundant versions of the same message. This paper investigates the improvements that may result by jointly coding across several data packets, in order to create redundancy packets relative to multiple messages. Theoretical analysis as well as simulation results suggest that multiple-packet IR may offer substantial throughput gains with respect to the classical, single-packet IR approach, particularly at medium-to-high signal-to-noise ratio.

## IMP: A message-passing algorithm for matrix completion

- **Status**: ❌
- **Reason**: 행렬완성(추천시스템)용 메시지패싱, 채널 ECC LDPC 아님
- **ID**: ieee:5613803
- **Type**: conference
- **Published**: 6-10 Sept.
- **Authors**: Byung-Hak Kim, Arvind Yedla, Henry D. Pfister
- **PDF**: https://ieeexplore.ieee.org/document/5613803
- **Abstract**: A new message-passing (MP) method is considered for the matrix completion problem associated with recommender systems. We attack the problem using a (generative) factor graph model that is related to a probabilistic low-rank matrix factorization. Based on the model, we propose a new algorithm, termed IMP, for the recovery of a data matrix from incomplete observations. The algorithm is based on a clustering followed by inference via MP (IMP). The algorithm is compared with a number of other matrix completion algorithms on real collaborative filtering (e.g., Netflix) data matrices. Our results show that, while many methods perform similarly with a large number of revealed entries, the IMP algorithm outperforms all others when the fraction of observed entries is small. This is helpful because it reduces the well-known cold-start problem associated with collaborative filtering (CF) systems in practice.

## Selection procedure of turbocode parameters by combinatorial optimization

- **Status**: ❌
- **Reason**: 터보코드 인터리버(permutation) 파라미터 선정, 비-LDPC 부호이고 이식 기법 없음
- **ID**: ieee:5613825
- **Type**: conference
- **Published**: 6-10 Sept.
- **Authors**: Yannick Saouter
- **PDF**: https://ieeexplore.ieee.org/document/5613825
- **Abstract**: Permutation design is a crucial point for turbocodes in terms of error correction performance. Many permutation design models have been proposed to deal with this point. However, most of them are defined in terms of several free parameters that have to be correctly chosen. The selection of these parameters generally leads to a systematic search in a wide domain of parameters value. In this article, we focus on the ARP model and describe an algorithm which avoids combinatorial enumeration.

## An interference-aware perspective on decoding power

- **Status**: ❌
- **Reason**: 디코딩 전력 vs 간섭 관점 무선 시스템 설계 분석 — 무선 응용 특이적, 떼어낼 LDPC ECC 기법 없음
- **ID**: ieee:5613865
- **Type**: conference
- **Published**: 6-10 Sept.
- **Authors**: Pulkit Grover, Kristen Ann Woyach, Hari Palaiyanur +1
- **PDF**: https://ieeexplore.ieee.org/document/5613865
- **Abstract**: Traditionally, coding has been seen as a way of saving transmit power: capacity-approaching codes require minimal transmitted energy-per-bit given the bandwidth available. But because transmit power is often smaller than decoding power at short distances, many recent wireless system designs continue to use uncoded transmission! We first observe that in wireless systems that both generate and face interference, coding serves another purpose (assuming interference is treated as noise): it allows a system to support a higher density of transmitter-receiver pairs. Bringing decoding power into the picture, we propose an approach to investigate which code/decoder to use and whether to use any coding at all. It turns out that the code's gap to capacity determines how high the maximum supportable link density can be when power is plentiful, whereas the code's decoding complexity governs what link densities can be supported at low power.

## Low-complexity video encoding method for wireless image transmission in capsule endoscope

- **Status**: ❌
- **Reason**: 캡슐내시경 Wyner-Ziv 저복잡도 비디오 인코딩, LDPC는 부수 채널코딩 베이스라인. 떼어낼 ECC 기법 없음
- **ID**: ieee:5627839
- **Type**: conference
- **Published**: 31 Aug.-4 
- **Authors**: Kenichi Takizawa, Kiyoshi Hamaguchi
- **PDF**: https://ieeexplore.ieee.org/document/5627839
- **Abstract**: This paper presents a low-complexity video encoding method applicable for wireless image transmission in capsule endoscopes. This encoding method is based on Wyner-Ziv theory, in which side information available at a transmitter is treated as side information at its receiver. Therefore complex processes in video encoding, such as estimation of the motion vector, are moved to the receiver side, which has a larger-capacity battery. As a result, the encoding process is only to decimate coded original data through channel coding. We provide a performance evaluation for a low-density parity check (LDPC) coding method in the AWGN channel.

## Strong secrecy for erasure wiretap channels

- **Status**: ❌
- **Reason**: erasure wiretap 보안(coset coding) + stopping set 이론 bound, 떼어낼 채널 ECC 디코더/HW/구성 기여 없음
- **ID**: ieee:5592770
- **Type**: conference
- **Published**: 30 Aug.-3 
- **Authors**: Ananda T. Suresh, Arunkumar Subramanian, Andrew Thangaraj +2
- **PDF**: https://ieeexplore.ieee.org/document/5592770
- **Abstract**: We show that duals of certain low-density parity-check (LDPC) codes, when used in a standard coset coding scheme, provide strong secrecy over the binary erasure wiretap channel (BEWC). This result hinges on a stopping set analysis of ensembles of LDPC codes with block length n and girth ≥ 2k for some k ≥ 2. We show that if the minimum left degree of the ensemble is lmin, the expected probability of block error is O(1/n⌈l mink/2⌉ -k) when the erasure probability ϵ <;; ϵef, where ϵef depends on the degree distribution of the ensemble. As long as lmin and k > 2, the dual of this LDPC code provides strong secrecy over a BEWC of erasure probability greater than 1-ϵef.

## Lossy source compression of non-uniform binary sources using GQ-LDGM codes

- **Status**: ❌
- **Reason**: GF(q) 비이진 LDGM 소스압축(quantization) — 비이진+소스코딩, 제외 카테고리 이중 해당
- **ID**: ieee:5592821
- **Type**: conference
- **Published**: 30 Aug.-3 
- **Authors**: Lorenzo Cappellari
- **PDF**: https://ieeexplore.ieee.org/document/5592821
- **Abstract**: In this paper, we study the use of GF(q)-quantized LDGM codes for binary source coding. By employing quantization, it is possible to obtain binary codewords with a non-uniform distribution. The obtained statistics is hence suitable for optimal, direct quantization of non-uniform Bernoulli sources. We employ a message-passing algorithm combined with a decimation procedure in order to perform compression. The experimental results based on GF(q)-LDGM codes with regular degree distributions yield performances quite close to the theoretical rate-distortion bounds.

## Stopping sets for physical-layer security

- **Status**: ❌
- **Reason**: 물리계층 보안(wiretap) 응용 - stopping-set으로 도청자 디코딩 실패 유도, 떼어낼 채널 ECC 디코더/구성 기법 없음(보안 목적)
- **ID**: ieee:5592686
- **Type**: conference
- **Published**: 30 Aug.-3 
- **Authors**: Willie K. Harrison, João Almeida, Demijan Klinc +2
- **PDF**: https://ieeexplore.ieee.org/document/5592686
- **Abstract**: Physical-layer security based on wiretap codes can be used to complement cryptographic applications at higher layers of the protocol stack. We assume a passive eavesdropper that has access to noise-corrupted codewords with erasures that are statistically independent to those of the legitimate communication partners. Our goal is to minimize the information leaked to the eavesdropper. In this paper we present a low-complexity coding scheme for channels with feedback, which employs extensive interleaving of carefully punctured LDPC codewords. The key idea is to ensure that every transmitted packet is crucial for successful decoding. This is achieved by ensuring that stopping-set bit combinations for coded blocks are distributed among different packets and by enforcing that retransmission requests be restricted to the friendly parties. A probabilistic analysis reveals that an eavesdropper who uses a message-passing decoding algorithm will experience catastrophic decoding failure with high probability. This encoder thus provides physical-layer secrecy which is both independent from, and complementary of, the cryptographic layer. The proposed scheme works even when an eavesdropper has a better channel than the legitimate receiver.

## Non-systematic codes for physical layer security

- **Status**: ❌
- **Reason**: non-systematic scrambling 부호 기반 물리계층 보안 — 보안 응용, 떼어낼 LDPC ECC 디코더/구성 없음
- **ID**: ieee:5592833
- **Type**: conference
- **Published**: 30 Aug.-3 
- **Authors**: Marco Baldi, Marco Bianchi, Franco Chiaraluce
- **PDF**: https://ieeexplore.ieee.org/document/5592833
- **Abstract**: This paper is a first study on the usage of non-systematic codes based on scrambling matrices for physical layer security. The chance of implementing transmission security at the physical layer is known since many years, but it is now gaining an increasing interest due to its several possible applications. It has been shown that channel coding techniques can be effectively exploited for designing physical layer security schemes, in such a way that an unauthorized receiver, experiencing a channel different from that of the authorized receiver, is not able to gather any information. Recently, it has been proposed to exploit puncturing techniques in order to reduce the security gap between the authorized and unauthorized channels. In this paper, we show that the security gap can be further reduced by using non-systematic codes, able to scramble information bits within the transmitted codeword.

## Unimodular lattices for the Gaussian Wiretap Channel

- **Status**: ❌
- **Reason**: 가우시안 도청채널의 unimodular lattice secrecy gain 이론 - 보안/lattice, LDPC ECC 기법 없음
- **ID**: ieee:5592923
- **Type**: conference
- **Published**: 30 Aug.-3 
- **Authors**: Jean-Claude Belfiore, Patrick Solé
- **PDF**: https://ieeexplore.ieee.org/document/5592923
- **Abstract**: In the authors introduced a lattice invariant called “Secrecy Gain” which measures the confusion experienced by a passive eavesdropper on the Gaussian Wiretap Channel. We study, here, the behavior of this invariant for unimodular lattices by using tools from Modular Forms and show that, for some families of unimodular lattices, indexed by the dimension, the secrecy gain exponentially goes to infinity with the dimension.

## Coding solutions for the secure biometric storage problem

- **Status**: ❌
- **Reason**: 바이오메트릭 보안 저장(fuzzy commitment) + 일반 ECC 선택 논의 — 보안 응용, 떼어낼 LDPC 신규 기법 없음
- **ID**: ieee:5592899
- **Type**: conference
- **Published**: 30 Aug.-3 
- **Authors**: Davide Schipani, Joachim Rosenthal
- **PDF**: https://ieeexplore.ieee.org/document/5592899
- **Abstract**: The paper studies the problem of securely storing biometric passwords, such as fingerprints and irises. With the help of coding theory Juels and Wattenberg derived in 1999 a scheme where similar input strings will be accepted as the same biometric. In the same time nothing could be learned from the stored data. They called their scheme a fuzzy commitment scheme. In this paper we will revisit the solution of Juels and Wattenberg and we will provide answers to two important questions: what type of error-correcting codes should be used and what happens if biometric templates are not uniformly distributed, i.e. the biometric data come with redundancy. Answering the first question will lead us to the search for low-rate large-minimum distance error-correcting codes which come with efficient decoding algorithms up to the designed distance. In order to answer the second question we relate the rate required with a quantity connected to the “entropy” of the string, trying to estimate a sort of “capacity”, if we want to see a flavor of the converse of Shannon's noisy coding theorem. Finally we deal with side-problems arising in a practical implementation and we propose a possible solution to the main one that seems to have so far prevented in many situations real life applications of the fuzzy scheme.

## An algebraic view to gradient descent decoding

- **Status**: ❌
- **Reason**: gradient descent 디코딩의 대수적 monoid 구조 통합 — 순수 이론, 일반 선형부호 대상이며 LDPC BP 이식 기여 없음
- **ID**: ieee:5592830
- **Type**: conference
- **Published**: 30 Aug.-3 
- **Authors**: M. Borges Quintana, M. A. Borges Trenard, I. Márquez-Corbella +1
- **PDF**: https://ieeexplore.ieee.org/document/5592830
- **Abstract**: There are two gradient descent decoding procedures for binary codes proposed independently by Liebler and by Ashikhmin and Barg. Liebler in his paper mentions that both algorithms have the same philosophy but in fact they are rather different. The purpose of this communication is to show that both algorithms can be seen as two ways of understanding the reduction process algebraic monoid structure related to the code. The main tool used for showing this is the Gröbner representation of the monoid associated to the linear code.

## Optimized relay selection strategy for adaptive network coded cooperation

- **Status**: ❌
- **Reason**: 분산 LDGM 릴레이 선택으로 short cycle 제거 — 네트워크 토폴로지 의존이라 NAND LDPC로 떼어낼 코드설계 기법 아님
- **ID**: ieee:5671702
- **Type**: conference
- **Published**: 26-30 Sept
- **Authors**: Kaibin Zhang, Liuguo Yin, Youzheng Wang +1
- **PDF**: https://ieeexplore.ieee.org/document/5671702
- **Abstract**: Adaptive network coded cooperation (ANCC) scheme has been shown to have better performance than the conventional repetition-based schemes and the space-time coded cooperation (STCC) frameworks for data transmissions from a large collection of terminals to a common destination in large wireless networks. However, the random selection strategy for ANCC protocol may generate many short cycles in the distributed low-density generator-matrix(LDGM) codes, which may cause error-floor and performance degradation. In this paper, an optimized relay selection strategy for ANCC is proposed. By exploiting information interaction between destination and terminals before data communication, and matching the instantaneous network topology, the proposed method generates ensembles of distributed LDGM codes free of short cycles. Simulation results demonstrate that the proposed relay selection protocol significantly outperforms the random relay selection strategy for various network sizes and different fixed numbers of selected terminals.

## Design of diversity-achieving LDPC codes for H-ARQ with cross-packet channel coding

- **Status**: ❌
- **Reason**: H-ARQ cross-packet용 full-diversity LDPC(rootcheck) 설계 — outage/다이버시티 무선 특이 설계, NAND 채널 ECC로 떼어낼 기법 없음
- **ID**: ieee:5671785
- **Type**: conference
- **Published**: 26-30 Sept
- **Authors**: Dieter Duyck, Daniele Capirone, Christoph Hausl +1
- **PDF**: https://ieeexplore.ieee.org/document/5671785
- **Abstract**: In wireless scenarios an effective protocol to increase the reliability for time-varying channels is the hybrid automatic repeat request (H-ARQ). The H-ARQ scheme with cross-packet channel coding (CPC) is a recently published extension of H-ARQ with several advantages. No full-diversity low-density parity-check (LDPC) code design for the whole range of coding rates yielding full-diversity has been published. In this paper the authors provide a new outage behavior analysis and a new structured LDPC code ensemble achieving full-diversity for H-ARQ with CPC by exploiting the rootcheck principle. Simulation results show that the new code design outperforms the previous approaches, providing full-diversity and good coding gain, also at high coding rates.

## Variable-rate equal-power waterfilling for non-binary LDPC coded multicarrier systems

- **Status**: ❌
- **Reason**: 비이진 GF(64) LDPC + 무선 멀티캐리어 워터필링 링크적응. 비이진 제외 + 떼어낼 ECC 기법 없음
- **ID**: ieee:5671883
- **Type**: conference
- **Published**: 26-30 Sept
- **Authors**: Gabriele Boccolini, Inbar Fijalkow
- **PDF**: https://ieeexplore.ieee.org/document/5671883
- **Abstract**: This paper presents a link adaptation strategy for non-binary LDPC code over a time-variant frequency-selective channel. The algorithm is based first on the adoption of waterfilling technique to wisely adapt the transmitted power. It is shown that as long as best subchannels are identified with the waterfilling algorithm, an equal power distribution can be applied with performance comparable to the ideal power adaptation. What it is more important is to decide which are the subchannels that should not be used in order to increase the energy efficiency of the system. The throughput is increased with the adoption of multilevel modulations that changes the rate of each subchannel depending on the channel-to-noise ratio and the quality of service required. The Galois Field GF(64) code symbols are mapped into four modulation schemes (BPSK, 4QAM, 16QAM, 64QAM) and the channel is assumed to be constant over six OFDM symbols. Simulation results are presented when a perfect channel state information is available at the transmitter and at the receiver side. In real dynamic channel environments, the performance of the system degrades due to the delay and the approximation of the feedback information. Simulation of partial channel state information scenario is also reported.

## Non-iterative signal processing for a new coded LSTF architecture in OFDM MIMO multiplexing

- **Status**: ❌
- **Reason**: LSTF MIMO-OFDM 아키텍처에 irregular LDPC를 구성코드로 사용, LDPC 자체 신규 기여 없음(무선 응용 특이)
- **ID**: ieee:5671847
- **Type**: conference
- **Published**: 26-30 Sept
- **Authors**: Yuanliang Huang, J Wang
- **PDF**: https://ieeexplore.ieee.org/document/5671847
- **Abstract**: This paper is focused on the study of layered space-time-frequency (LSTF) architectures with channel coding for orthogonal frequency division multiplexing (OFDM) multiple-input multiple-output (MIMO) multiplexing systems for high speed wireless communications over a frequency-selective fading channel. In order to achieve the available spatial, temporal and frequency diversities, and also make the system implementation feasible for high speed OFDM MIMO multiplexing, a novel LSTF architecture with multiple channel encoders is proposed with each independently coded layer being threaded in the three-dimensional space-time-frequency transmission resource array. Non-iterative receiver is adopted which consists of list sphere detector and irregular low-density parity-check (LDPC) codes as the constituent codes. Simulation results show that the performance of the proposed multiple-encoder LSTF architecture is very close to that of the conventional single-encoder LSTF where coding is applied across the whole information stream. However, due to the use of multiple parallel encoders/decoders with a shorter codeword length, the proposed LSTF architecture has much lower hardware processing speed and complexity than the conventional LSTF.

## Overview of ARQ and HARQ in beyond 3G systems

- **Status**: ❌
- **Reason**: ARQ/HARQ 서베이, LDPC 코드설계/디코더 기여 없음
- **ID**: ieee:5671369
- **Type**: conference
- **Published**: 26-30 Sept
- **Authors**: Antonio Maria Cipriano, Paul Gagneur, Guillaume Vivier +1
- **PDF**: https://ieeexplore.ieee.org/document/5671369
- **Abstract**: In this paper, we present a review of automatic repeat request (ARQ) and hybrid ARQ (HARQ) mechanisms implemented or proposed in beyond 3rd generation (B3G) wireless systems based on OFDMA. In particular, we will focus on part of the IEEE 802.16 standard family (IEEE 802.16-2005, IEEE 802.16m) and on 3GPP Long Term Evolution (LTE). In the second part of this overview, some performance curves show how HARQ can help in reducing performance degradation in mobility context.

## 60-GHz adaptive beamforming receiver arrays for interference mitigation

- **Status**: ❌
- **Reason**: 60GHz 빔포밍 수신기 간섭완화, LDPC/ECC 무관
- **ID**: ieee:5671942
- **Type**: conference
- **Published**: 26-30 Sept
- **Authors**: Chang-Soon Choi, Mohamed Elkhouly, Eckhard Grass +1
- **PDF**: https://ieeexplore.ieee.org/document/5671942
- **Abstract**: This paper describes a millimetre-wave receiver beamforming for interference mitigation as well as array gain enhancement. Like the beamforming architecture in the IEEE 802.15.3c standard, it is based on only one baseband processor to support multiple N-element antenna arrays for low-cost implementation. This makes it difficult to estimate received signals and channel state information on each antenna, which restricts baseband digital processing and introduces large overheads for adaptive beamforming. For these reasons, the IEEE 802.15.3c standard utilizes 2-bit beam codebook for repetitive beam-searching, however it cannot offer adaptive interference nulling capability. We propose an algorithm to get received signal information on each antenna so that we can find optimum weight vectors for maximum beamforming gain. This also enables to mitigate co-channel interference, which increase total throughput by enhancing spatial re-use in multiple 60-GHz indoor networks. The structural difference from the IEEE 802.15.3c beamformer is to employ a continuous phase-shifter, however our implementation proves that it exhibits almost same-level complexity as 2-bit phase-shifters.

## Iterative SIC receiver scheme for non-orthogonally superimposed signals on top of OFDMA

- **Status**: ❌
- **Reason**: OFDMA 반복 SIC 수신기, 떼어낼 코딩/디코더 기법 없음
- **ID**: ieee:5671952
- **Type**: conference
- **Published**: 26-30 Sept
- **Authors**: Andreas Rüegg, Alberto Tarable
- **PDF**: https://ieeexplore.ieee.org/document/5671952
- **Abstract**: In this paper, we propose an iterative SIC receiver architecture with pilot- and data-based channel estimation for efficient decoding of non-orthogonal superimposed signals. The non-orthogonal superposition concept on top of OFDMA is a promising technique to improve cell spectral efficiency. In the cellular case, where users with significant path loss are superimposed by an intelligent scheduler, the SIC multi-user receiver scheme is well adapted for user signal separation. Based on the proposed receiver, we show the performance by means of multi-link link-level simulations in a realistic OFDMA uplink system including channel estimation based on real pilot patterns.

## Reed-Solomon coding for cooperative wireless communication

- **Status**: ❌
- **Reason**: Reed-Solomon 협력통신, 비-LDPC 부호이고 이식할 BP 기법 없음
- **ID**: ieee:5672091
- **Type**: conference
- **Published**: 26-30 Sept
- **Authors**: Ismail Shakeel, Mazen O. Hasna, Adnan Abu-Dayya +1
- **PDF**: https://ieeexplore.ieee.org/document/5672091
- **Abstract**: During the last few years, several authors have studied the performance of many different types of channel codes for cooperative communication systems. Some of these codes include Low Density Parity Check (LDPC), Turbo and convolutional codes. Published results show that these codes effectively improve both the data rate and system performance in cooperative schemes such as the decode and forward (DF). Reed-Solomon (RS) codes are one of the most widely used channel codes in wireless communication systems today. These codes have also been adopted by several 3G standards including several digital video broadcasting (DVB) standards and also by worldwide interoperability for microwave access (WiMAX) which is based on the IEEE 802.16 standard. However, published literature shows no specific study to investigate their performance for the cooperative communication environment. Using the component codes adopted in the IEEE 802.16 standard, this paper investigates the performance of the concatenated RS coding schemes for cooperative communication. This paper first analyses the standard RS-coded DF cooperative system. The results obtained for the standard RS-coded scheme show huge gains over the non-cooperative system. Some of the problems of the standard DF relay protocol is then discussed and an improved RS-coded DF cooperative scheme is proposed. The performance of the proposed scheme shows significant gains over the standard RS-coded DF system.

## Performance comparison of LDPC-Coded IDMA system with equal spreading and unequal spreading

- **Status**: ❌
- **Reason**: IDMA spreading용 LDPC degree profile 최적화(무선 MAC 응용 특이적), 떼어낼 NAND 이식 디코더·구성 기법 없음
- **ID**: ieee:5702972
- **Type**: conference
- **Published**: 26-29 Sept
- **Authors**: Jingxi Zhang, Zhisong Bie, Weiling Wu +1
- **PDF**: https://ieeexplore.ieee.org/document/5702972
- **Abstract**: A scheme of applying unequal spreading to LDPCCoded IDMA system was proposed. The issue of LDPC-Coded DDMA system with equal spreading and unequal spreading was studied. Gaussian approximation was applied to the messages probability density distribution function between nodes on factor graph of LDPC-Coded spreading system. We compare two cases, the first is optimization of LDPC with fixed spreading factor, and the second is joint optimization of LDPC and spreading degree. By means of iteration and applying the method of differential evolution we obtained degree profiles in the case of 8 users with equal spreading and unequal spreading on condition that the system spectral efficiency is the same. We constructed the check matrix randomly based on the optimized degree profiles and made simulations. It has shown that the performance of LDPC-Coded spreading IDMA system cannot be improved by joint optimization of LDPC code and spreading degree for AWGN Multiple Access Channel (MAC) from the perspective of approaching MAC channel capacity. The result gives us guidance in designing LDPC-Coded IDMA spreading system.

## LDPC coded MIMO communication system with time varying linear transformation

- **Status**: ❌
- **Reason**: MIMO 시공간 변환+LDPC 결합 시스템(무선 응용), girth는 교과서 수준 언급뿐, NAND 이식 신규 기법 없음
- **ID**: ieee:5702984
- **Type**: conference
- **Published**: 26-29 Sept
- **Authors**: Qina Gao, Yu Tian, Ying Zhao
- **PDF**: https://ieeexplore.ieee.org/document/5702984
- **Abstract**: A novel low-density parity-check (LDPC) coded multiinput multi-output (MIMO) communication system with time varying linear transformation (TVLT) is proposed in this paper. Combined with the outstanding distance property of LDPC codes, TVLT can provide full diversity and maximum coding gain at the same time without exhaustive search for the good space-time codes as usual. To satisfy the demand of TVLT on channel coding, the girth in Tanner code is discussed briefly. Corresponding joint iterative detector /decoder structure of receiver in the new system greatly simplifies the demodulation/decoding process. Compared with the common Turbo coded or conventional convolution coded concatenated MIMO system, the novel concise system achieves higher coding gain and full diversity together, which is verified by simulation results.

## Hidden Markov Model for distributed video coding

- **Status**: ❌
- **Reason**: 분산 비디오 코딩(HMM/소스메모리), LDPC는 베이스라인이고 떼어낼 채널 ECC 기법 없음
- **ID**: ieee:5652643
- **Type**: conference
- **Published**: 26-29 Sept
- **Authors**: V. Toto-Zarasoa, A. Roumy, C. Guillemot
- **PDF**: https://ieeexplore.ieee.org/document/5652643
- **Abstract**: This paper addresses the problem of asymmetric distributed coding of correlated binary Hidden Markov Sources, modeled as a Gilbert-Elliott process. The model parameters are estimated with an estimation-decoding Expectation-Maximization algorithm. The rate gain obtained by accounting for the memory of the sources is first assessed theoretically. The method is then shown to improve the PSNR versus rate performance of a Distributed Video Coding system, based on Low-Density Parity-Check codes.

## Side-information-adaptive distributed source coding

- **Status**: ❌
- **Reason**: side-info 적응 분산 소스코딩, density evolution도 doping rate 최적화용(소스코딩)이라 채널 ECC 아님
- **ID**: ieee:5653404
- **Type**: conference
- **Published**: 26-29 Sept
- **Authors**: David Varodayan, Bernd Girod
- **PDF**: https://ieeexplore.ieee.org/document/5653404
- **Abstract**: Consider distributed source coding in which each block of the source at the encoder is associated with multiple candidates for side information at the decoder, just one of which is statistically dependent on the source block. Our encoder codes the source as syndrome bits and also sends a portion of it uncoded as doping bits. The decoder adaptively discovers the best side information candidates for each block of the source. The main contribution is a method based on density evolution to analyze and design the coding performance. Experimental results show that the density evolution technique is accurate in modeling the codec and optimizing its doping rate.

## Distributed joint source-channel arithmetic coding

- **Status**: ❌
- **Reason**: 분산 결합 소스-채널 산술부호(DAC), 비-LDPC 소스코딩 JSCC
- **ID**: ieee:5652684
- **Type**: conference
- **Published**: 26-29 Sept
- **Authors**: Marco Grangetto, Enrico Magli, Gabriella Olmo
- **PDF**: https://ieeexplore.ieee.org/document/5652684
- **Abstract**: We address distributed source coding with decoder side information, when the decoder observes the source through a noisy channel. Existing approaches employ syndromeor parity-based channel codes. We propose a new approach based on distributed arithmetic coding (DAC).We introduce a DAC with forbidden symbol, which allows to tune the redundancy according to the amount of channel noise. We propose a novel sequential decoder that employs the known side information to decode the corrupted codeword. Experimental results show that the proposed scheme is better than parity-based turbo codes at relatively short block lengths.

## Quality-aware video based on robust embedding of intra- and inter-frame reduced-reference features

- **Status**: ❌
- **Reason**: 비디오 워터마킹 품질평가, LDPC ECC 기법 없음
- **ID**: ieee:5651106
- **Type**: conference
- **Published**: 26-29 Sept
- **Authors**: Kai Zeng, Zhou Wang
- **PDF**: https://ieeexplore.ieee.org/document/5651106
- **Abstract**: With the rapid development of network visual communications, there is an urgent need of effective and efficient video quality assessment (VQA) methods for quality control and resource allocation purposes. In this paper, a spatial and temporal reduced-reference (RR) VQA measure is combined with a robust video watermarking approach, leading to a quality-aware video (QAV) system. At the sender side, both intra- and inter-frame RR features are calculated from the original video based on statistical models of natural video. This is followed by error control coding to improve robustness. The encoded features are then embedded invisibly into the same video signal using a robust angle quantization index modulation based watermarking method in 3D discrete cosine transform domain. At the receiver side, the RR features are extracted and decoded from the distorted video and employed to predict the perceptual degradation of the video signal. Experimental results demonstrate the applicability of the proposed approach to a wide range of distortion types and levels.

## LDPC Encoding Based on the Primitive Polynomial

- **Status**: ❌
- **Reason**: 표준 LDPC를 primitive polynomial 기반으로 구성하는 코드설계지만 무선 응용 맥락의 교과서 수준 행렬 구성, 신규 디코더/HW 기여 없음
- **ID**: ieee:5600987
- **Type**: conference
- **Published**: 23-25 Sept
- **Authors**: Dai Nina, Cai Li
- **PDF**: https://ieeexplore.ieee.org/document/5600987
- **Abstract**: Low-Density Parity-Check (LDPC) code is a class of error-correcting codes which have limited capacity. For long code lengths, LDPC codes can even outperform Turbo codes. LDPC is regarded as one of the key technologies that realize the high-speed broadband wireless networks in the future. In this thesis, a new encoding method of LDPC is attempted to construct the parity check matrix from the point of view of primitive polynomial. That is to say, the matrix is made use of primitive polynomial and the technology of ranks decomposition. Matlab is implemented to do a number of computer-aided simulations for getting the performance of the primitive LDPC encoding.

## Scalable Video Coding Transmission System with Error Correction of High-Resolution Multi-View Stereo Video with LDPC

- **Status**: ❌
- **Reason**: 스케일러블 비디오 전송에 LDPC 적용, 떼어낼 디코더/구성/HW 기법 없는 응용 논문
- **ID**: ieee:5601046
- **Type**: conference
- **Published**: 23-25 Sept
- **Authors**: Zhigang Jin, Ximan Zhao, Jia Wang
- **PDF**: https://ieeexplore.ieee.org/document/5601046
- **Abstract**: In this paper, we presents a scalable video coding transmission system with error correction of high-resolution multi-view stereo video with LDPC (Low Density Parity-Check Codes). In order to ensure the quality of service, we design two transmission modes with scalable video coding technology. The system could switch the transmission mode according to the channel bandwidth or the agent devices in real-time. In addition, to correct the bit errors caused by the channel noise and improve the PSNR (Peak Signal to Noise Ratio) of the transmission system, we encode the video content with LDPC. Compared to the scenario without LDPC, the video content with LDPC outperforms the source without LDPC.

## Performance Analysis of a LDPC Coded CDMA System with Physical Layer Security Enhancement

- **Status**: ❌
- **Reason**: LDPC-CDMA 물리계층 보안(AES 스크램블링), 보안/무선 응용이며 떼어낼 ECC 기법 없음
- **ID**: ieee:5601271
- **Type**: conference
- **Published**: 23-25 Sept
- **Authors**: Tahereh Shojaeezand, Paeiz Azmi, AmirMansour Yadegari
- **PDF**: https://ieeexplore.ieee.org/document/5601271
- **Abstract**: CDMA systems in comparison with other communication systems, are resistant against unauthorized information detection attacks, yet have some weakness with respect to some eavesdropping techniques. Increasing the physical layer built-in security through secure scrambling method is an advantageous method. Besides, using some capacity achieving codes such as LDPC codes, was shown that help the system for better secrecy and good performance. Here a LDPC coded CDMA system with AES scrambling as the secure method is described and analyzed. The performance of the system is acceptable along with all the security advantages mentioned above.

## A LDPC and Turbo Codes Hybrid Coding Scheme Based on OFDM System

- **Status**: ❌
- **Reason**: OFDM에서 Turbo+LDPC 적응 부호화 결합. 무선 응용, 새 디코더/구성 기여 없음
- **ID**: ieee:5600936
- **Type**: conference
- **Published**: 23-25 Sept
- **Authors**: Hao Chen, XueKang Sun, Liang Dai
- **PDF**: https://ieeexplore.ieee.org/document/5600936
- **Abstract**: In this paper, we employ to provide a method which combines Turbo codes and Low-Density Parity-Check (LDPC) codes based on Orthogonal Frequency Division Multiplexing (OFDM) system by adaptive encoding. The technique of channel estimation is used. The code rate and encoding scheme are all adaptive selection in the light of different channel conditions, so that we can make good use of these two types of codes' respective advantages. This new method can guarantee the quality of service and pursuit of maximum useful bit rate. Through analysis and simulation, we show the better bit error rate (BER) performance compared to conventional method.

## Concatenated LDPC and Differential Space-Time Block Codes

- **Status**: ❌
- **Reason**: LDPC+차분 STBC 다중안테나 연접 시스템, LDPC는 부수적이고 무선 다이버시티 응용 특이적, 떼어낼 ECC 기법 없음
- **ID**: ieee:5600996
- **Type**: conference
- **Published**: 23-25 Sept
- **Authors**: Yuling Zhang, Wenwei He
- **PDF**: https://ieeexplore.ieee.org/document/5600996
- **Abstract**: In this paper, we propose a multi-antenna system concatenated Low-density Parity-check (LDPC) codes and Differential Space-time Block codes (DSTBC), in which channel state information (CSI) is unknown to the transmitter and the receiver. The system performance is given through computer simulation, we can see that the proposed system not only provides transmit diversity gain but also coding gain.

## Near Optimal BP Algorithm for LDPC-Coded BICM System with EXIT Analysis

- **Status**: ❌
- **Reason**: BICM 시스템용 BP 변형(NOBP)이나 M-ary BICM 채널 의존(generalized M-ary BP), 무선 통신 응용 특이적이며 바이너리 LDPC BP로 떼어낼 신규 기법 불명
- **ID**: ieee:5600964
- **Type**: conference
- **Published**: 23-25 Sept
- **Authors**: Ying Wang, Lei Xie, Huifang Chen +1
- **PDF**: https://ieeexplore.ieee.org/document/5600964
- **Abstract**: A near optimal BP (NOBP) algorithm for low-density parity-check (LDPC) coded M-ary BICM communication system is proposed in this paper. Due to the good code structure of LDPC code, we derive the NOBP algorithm with the generalized distributive law from the generalized M-ary BP algorithm. The simulation results show that the NOBP algorithm outperforms the traditional BICM-BP algorithm over both the AWGN and Rayleigh fading channel. And the EXIT chart of two algorithms confirms the superiority and the fast convergence of our proposed NOBP algorithm.

## Efficient Encoder Structures for Non-Binary Cycle Codes

- **Status**: ❌
- **Reason**: GF(q) 비이진 cycle code 인코더 구조. 비이진 LDPC 제외 대상
- **ID**: ieee:5600231
- **Type**: conference
- **Published**: 23-25 Sept
- **Authors**: Weigang Chen
- **PDF**: https://ieeexplore.ieee.org/document/5600231
- **Abstract**: Low-density parity-check codes with variable node degree two over high order Galois fields, also called non-binary cycle codes, exhibit good error correction performance. In this paper, several efficient encoder structures are proposed for non-binary cycle codes with only one optimized group of non-zero entries in GF(q)(q > 2). The computation complexity and storage requirement are compared for these methods. Considering the underlying sparse graph of cycle code, the encoding complexity is quite low with the proposed modifications. In this way, a proper tradeoff between complexity and performance is achieved for non-binary cycle codes.

## DmF Cooperation Based on Joint Network-Channel Coding in Wireless Communication

- **Status**: ❌
- **Reason**: DmF 협력통신 joint network-channel coding, LDPC는 베이스라인일 뿐 떼어낼 디코더/구성 ECC 기법 없음(무선 응용 특이적)
- **ID**: ieee:5600995
- **Type**: conference
- **Published**: 23-25 Sept
- **Authors**: Gu Li, Zhiping Shi
- **PDF**: https://ieeexplore.ieee.org/document/5600995
- **Abstract**: In this paper, we study the strategy of Demodulation-and-Forward(DmF) based on joint network and channel coding and extend it to multi-user access relay channel . In DmF model, there are two users accessing the relay. Users encode original signals using LDPC codes. In the relay, we conduct demodulation instead of decoding and implement network coding that is the Demodulation-and-Forward(DmF) method which based on joint network-channel coding. Throughout the whole DmF system, we implement encoding with LDPC codes only once in users. And at the base station, we only use one matrix H to decode all of these signals from the users and the relay jointly. Finally, we extend the DmF model to cases of three users and four and take some improvement in the relay and base station which is called extended DmF model. In the extended model, we encode the codeword using LDPC codes again after network coding in the relay, namely, we encode signals twice using LDPC codes throughout the whole system. In the base station, we redesign the parity check matrix H which can also decode all of signals from the users and relay jointly. The result shows us that the DmF model has lower hardware complexity and more practicability than DF. And we can apply it to multi-user access relay channel effectively.

## Design of Irregular Quasi-Cyclic LDPC Codes

- **Status**: ❌
- **Reason**: irregular QC-LDPC 설계지만 girth>=6, 시프트레지스터 인코더 등 교과서 수준 표준 QC-LDPC 구성, 새 기여 없음
- **ID**: ieee:5600227
- **Type**: conference
- **Published**: 23-25 Sept
- **Authors**: Jintao Hu, Yongsheng Wang, Ding Wang +1
- **PDF**: https://ieeexplore.ieee.org/document/5600227
- **Abstract**: Abstract-In this paper, a novel methodology for design irregular quasi-cyclic LDPC codes is presented. The quasi-cyclic structure facilitates encoder and decoder implementation through shift-register-based circuits. The irregularity characteristic improves the code performance in waterfall region. The structure imposed on the bipartite graphs together with shifting matrix, Lead to a class of this code suitable for fast iterative decoding. The construction method results in a class of quasi-cyclic LDPC codes with girth of at least 6.The simulation results show, using the Sum Productive Decoder, this kinds of codes having excellent performance on the additive white Gaussian noise channels.

## A comparison study of binary and non-binary LDPC codes decoding

- **Status**: ❌
- **Reason**: 비이진(GF(4)/GF(16)) LDPC 성능 비교 논문 — 비이진 LDPC는 제외 대상
- **ID**: ieee:5623667
- **Type**: conference
- **Published**: 23-25 Sept
- **Authors**: Sanae El Hassani, Marie-Hélène Hamon, Pierre Pénard
- **PDF**: https://ieeexplore.ieee.org/document/5623667
- **Abstract**: Non binary LDPC codes are promising error correcting codes which have increasingly raised interest in the last few years. This paper addresses some comparisons for short and moderate blocklengths between binary and non binary LDPC codes from different points of view, including error correction performance, complexity cost and possible adaptation and optimization opportunities. It shows a performance advantage of non binary codes up to 0.5 dB when only using GF(4) instead of GF(2), and up to 0.75 dB when using GF(16). Despite the large additional complexity induced by non binary decoding, these codes are very promising since adapted complexity reduction techniques are already investigated and show interesting results. Some analysis on decoding behavior of non binary LDPC decoder is also given in this paper. Such comparisons and analysis are interesting to gain insights on non binary LDPC codes and to derive guidelines for their optimization.

## A Novel Approach to Improve the Iterative Detection Convergence of LDPC Coded CPM Modulated Signals

- **Status**: ❌
- **Reason**: LDPC+CPM 반복검출 수렴 개선(weighted extrinsic). CPM 변조 응용 특이적, 떼어낼 LDPC BP 기법 아님
- **ID**: ieee:5600751
- **Type**: conference
- **Published**: 23-25 Sept
- **Authors**: Rui Xue, Dan-feng Zhao, Chun-li Xiao
- **PDF**: https://ieeexplore.ieee.org/document/5600751
- **Abstract**: Continuous Phase Modulation (CPM) provides an attractive option for spectral efficient communication systems. Low-Density Parity-Check Code (LDPCC) combined with CPM has a potential to result in a spectrally efficient scheme that is also energy efficient in that it yields low error rates at low signal-to-noise ratios. In this paper we consider the concatenation of a LDPC encoder and a CPM modulator which can be decoded and demodulated iteratively. In order to decrease the positive feedback during iterative detection with short frame, an improved method based on weighed extrinsic information exchange is proposed. Theoretic analysis and simulation results show that the proposed method can not only prevent the phenomena of positive feedback from taking place, reduce the error floor and improve the performance of BER under the condition of low SNR effectively, but also reduce the average number of iteration as well as the iterative decoding delay.

## An Improved Quantum LDPC Codes Construction Based on Balanced Incomplete Block Designs

- **Status**: ❌
- **Reason**: 양자 LDPC 구성(BIBD 기반, 패리티검사 commutativity 보장). 양자 전용 스태빌라이저 직교성에 의존, 제외
- **ID**: ieee:5600960
- **Type**: conference
- **Published**: 23-25 Sept
- **Authors**: Sheng-Mei Zhao, Xiu-Li Zhu, Feng Gao +1
- **PDF**: https://ieeexplore.ieee.org/document/5600960
- **Abstract**: Taking advantages of the property of classical codes from balance incomplete block designs (BIBDs), an improved construction of quantum Low Density Parity Check (quantum LDPC) codes is proposed in this paper. In the construction, we modified the original "Construction B" procedures to assure the quantum parity check matrix commutativity. It is shown that this construction method is a systematic structured method, and it is easier to obtain quantum codes. By simulation, we find the quantum parity check matrix obtained by our method are sparser than those from the method proposed by Ivan, and the codes have more good performance with the belief propagation iterative decoding algorithms.

## Frequency-domain turbo detection for LDPC-coded single-carrier mimo underwater acoustic communications

- **Status**: ❌
- **Reason**: 수중음향 MIMO turbo equalization 응용 특이적; LDPC는 표준 sum-product 베이스라인, 떼어낼 신규 디코더/HW/코드설계 기법 없음
- **ID**: ieee:5664491
- **Type**: conference
- **Published**: 20-23 Sept
- **Authors**: Longbao Wang, Jun Tao, Chengshan Xiao +1
- **PDF**: https://ieeexplore.ieee.org/document/5664491
- **Abstract**: This paper proposes a frequency-domain detection scheme for single-carrier multiple-input, multiple-output (MIMO) underwater acoustic (UWA) communication using low-density parity-check (LDPC) codes. The new scheme employs turbo equalization technology together with iterative decoding technique, leading to a double-layer turbo detection structure. In the outer-layer turbo equalization, a soft-decision frequency-domain equalizer (FDE) iteratively exchanges soft information with the soft-decision LDPC channel decoder. Within each outer-layer iteration, the LDPC decoder performs inner-layer iterative decoding with sum-product algorithm. The new scheme achieves excellent detection performance attributing to the double layers of iterative operation, which has been tested by experimental data measured in two undersea trials: WHOI09 and ACOMM09. Experimental results have demonstrated that it achieves consistently decent detection performance with different modulations, different symbol rates, and different transmission ranges.

## A LDPC code/decode channel coding model based on sum-product algorithm realization via LabVIEW

- **Status**: ❌
- **Reason**: LabVIEW로 표준 sum-product LDPC 구현 교육용 모델; 신규 디코더/구성/HW 기여 없음
- **ID**: ieee:5729742
- **Type**: conference
- **Published**: 20-23 Sept
- **Authors**: Iva Bacic, Kresimir Malaric, Zeljko Petrunic
- **PDF**: https://ieeexplore.ieee.org/document/5729742
- **Abstract**: In this work the basic concept of low-density parity-check codes is presented. First discovered in early 1960's, but were out of use because of their computing complexity for that time, today they are used in communication systems that take advantage of parallelism, very good error correction and high throughput like the DVB-S2. A soft decision sum-product algorithm based low-density parity-check code/decode channel coding model was developed through use of National Instruments' LabVIEW. This model was used to test the influence of the number of bits used in a message to be sent, the number of iterations and the low-density parity-check code rate on communication quality and the bit error rate. Simulation results show that the increase of message bits improves the communication quality. To achieve a better communication (lower BER) the code rate should be reduced but the number of iteration of the LDPC decoder should be set to a higher value.

## 5 Mbps optical wireless communication with error correction coding for underwater sensor nodes

- **Status**: ❌
- **Reason**: 수중 광무선통신 시스템 데모, ECC는 부수 언급·떼어낼 LDPC 기법 없음
- **ID**: ieee:5664429
- **Type**: conference
- **Published**: 20-23 Sept
- **Authors**: Jim A. Simpson, William C. Cox, John R. Krier +3
- **PDF**: https://ieeexplore.ieee.org/document/5664429
- **Abstract**: One issue with underwater sensors is how to efficiently transfer large amounts of data collected by the node to an interrogating platform such as an underwater vehicle. It is often impractical to make a physical connection between the node and the vehicle which suggests an acoustic or optical wireless solution. For large amounts of data, the high bandwidth of underwater optical wireless is an advantage. A small, low-cost platform to demonstrate the potential of an optical wireless communications interface for underwater sensor nodes is demonstrated. To enhance the reliability and robustness of the optical wireless communication digital signal processing and error correction techniques are used. The system was tested in 3 and 7.7 meter tanks at 5 Mbps with the turbidity of the water controlled by the addition of Maalox.

## Joint channel decoding and physical-layer network coding in two-way QPSK relay systems by a generalized Sum-Product Algorithm

- **Status**: ❌
- **Reason**: two-way relay 물리계층 네트워크코딩, GF(16) generalized SPA — 비이진 LDPC 제외
- **ID**: ieee:5624358
- **Type**: conference
- **Published**: 19-22 Sept
- **Authors**: Dirk Wübben
- **PDF**: https://ieeexplore.ieee.org/document/5624358
- **Abstract**: A physical-layer network coded two-way relay system applying Low-Density Parity-Check (LDPC) codes for error correction is considered in this paper, where two sources A and B desire to exchange information with each other by the help of a relay R. The critical process in such a system is the calculation of the network-coded transmit word at the relay on basis of the superimposed channel-coded QPSK words of the two sources. For this joint channel-decoding and network-encoding task a generalized Sum-Product Algorithm (SPA) over F16 is developed. This novel iterative decoding approach outperforms other recently proposed schemes as demonstrated by simulations.

## The stability of LDPC codes over GF(q) with higher order modulation schemes

- **Status**: ❌
- **Reason**: GF(q) 비이진 LDPC 안정성 조건 (density evolution) — 비이진 LDPC 제외
- **ID**: ieee:5624527
- **Type**: conference
- **Published**: 19-22 Sept
- **Authors**: V. S. Ganepola, R. A. Carrasco, I. J. Wassell +1
- **PDF**: https://ieeexplore.ieee.org/document/5624527
- **Abstract**: In this paper, we derive stability conditions for nonbinary low-density-parity-check (LDPC) codes with Gray mapped M-ary phase-shift keying (M-PSK) and M-ary quadrate-amplitude-modulation (M-QAM) constellations. The stability of the GF (q) LDPC decoder with higher order modulation schemes is examined on both additive-white-Gaussian-noise (AWGN) and block Rayleigh fading channels and threshold stability conditions under iterative decoding are obtained using density evolution techniques. It is shown that both on block Rayleigh fading channel when the ideal channel state information (CSI) of the fading process is known, and on AWGN channel, the stability condition of the underlying code is bounded by the Bhattacharya noise parameter. We show that the derived stability condition is both sufficient and necessary condition for iterative belief propagation decoding assuming cycle free massage passing between variable and check nodes. The evolution of stability condition is assessed over several finite fields for M-PSK and M-QAM constellations. This study provides an analytical framework to evaluate the performance bounds of both binary and nonbinary LDPC coded systems that extend over higher order modulation schemes.

## Analysis of ICI compensation for DVB-T2

- **Status**: ❌
- **Reason**: DVB-T2 ICI 보상+iterative 수신기, LDPC는 부수 — 무선 응용 특이적, 떼어낼 기법 없음
- **ID**: ieee:5624331
- **Type**: conference
- **Published**: 19-22 Sept
- **Authors**: Pello Ochandiano, Iker Sobrón, Lorena Martínez +2
- **PDF**: https://ieeexplore.ieee.org/document/5624331
- **Abstract**: This paper analyzes the impact of inter-carrier interference (ICI) compensation on the physical layer of DVB-T2, the new digital terrestrial television standard. We compare the performance of a well-known low complexity soft demapper for different time-interleaving depths and code rates in several realistic mobile scenarios. This paper further presents an iterative receiver design that exchanges extrinsic information between the low-density parity-check (LDPC) decoder and the ICI canceller in order to improve performance. Provided simulation results show that the proposed ICI cancellation algorithms can be necessary in several DVB-T2 transmission modes when the length of the time interleaver is limited.

## Type-I HARQ scheme using LDPC codes and partial retransmissions for AWGN and quasi static fading channels

- **Status**: ❌
- **Reason**: HARQ 부분 재전송+다이버시티 결합 throughput — 무선 응용 특이적, 디코더/코드설계 기여 없음
- **ID**: ieee:5624326
- **Type**: conference
- **Published**: 19-22 Sept
- **Authors**: André Gustavo Degraf Uchôa, Richard Demo Souza, Marcelo Eduardo Pellenz
- **PDF**: https://ieeexplore.ieee.org/document/5624326
- **Abstract**: In this paper we present a Type-I HARQ scheme for low density parity check codes (LDPC) using partial retransmissions and diversity combining. The proposed method divides the retransmissions in equal length sub-packets, and applies a power compensation. We demonstrate that the new scheme outperforms, in terms of throughput, the typical diversity combining methods for AWGN and quasi static fading channels, considering BPSK and 16-QAM modulation. Both theoretical and simulation results are presented, with a very good agreement between them. The numerical results show that the gains in terms of throughput, with respect to the typical methods, can be as large as 5 dB.

## Forward link performance of packet data with LDPC in cellular CDMA

- **Status**: ❌
- **Reason**: 셀룰러 CDMA forward link 성능 평가, LDPC는 부수 적용·ARQ 중심, 떼어낼 디코더/구성/HW 기법 없음
- **ID**: ieee:5640423
- **Type**: conference
- **Published**: 17-19 Sept
- **Authors**: Sanjay Dhar Roy, Priyobrata Parida, Sumit Kundu
- **PDF**: https://ieeexplore.ieee.org/document/5640423
- **Abstract**: Forward link performance of data services has been evaluated in cellular CDMA network by incorporating low density parity check (LDPC) codes in presence of soft handoff. This scheme is found to enhance throughput while reducing delay and packet error rate significantly. A stop and wait ARQ has been assumed in link layer. Both the cases of coded and uncoded data transmission are investigated.

## PLC link control based on minimal total distance and LDPC codes

- **Status**: ❌
- **Reason**: PLC 링크 제어, LDPC 디코더 반복수를 피드백 신호로만 사용, 떼어낼 ECC 기법 없음
- **ID**: ieee:5641006
- **Type**: conference
- **Published**: 15-17 Sept
- **Authors**: Martin Guzzo, Marcelo Segura, Juan Pablo Aguiar +1
- **PDF**: https://ieeexplore.ieee.org/document/5641006
- **Abstract**: Multimedia applications like high definition digital television push the manufacturers to increase available bandwidth mainly in Powerline Communication (PLC) links. Because of this needs in this work a PLC link control is developed to maximize the information rate meanwhile the bit error rate (BER) is maintained under a desired reference limit. The developed control system has a unique variable called minimal total distance and the feedback loop signal is estimated from the low-density parity check (LDPC) decoder iterations. These mentioned characteristics enable a fast and simple control scheme. In order to evaluate the control system behavior a complete Powerline (PL) link was modeled in a matrix form and simulated with a measured PL channel model and with an additive white Gaussian noise (AWGN) channel. The implemented PL link reaches 570Mbps in AWGN. Finally the BER control shows a good response under a severe random walk SNR channel variation.

## On the performance of moderate-length non-binary LDPC codes for space communications

- **Status**: ❌
- **Reason**: 비이진(non-binary/GF(q)) LDPC 부호 — 바이너리 한정 기준에 따라 제외
- **ID**: ieee:5586886
- **Type**: conference
- **Published**: 13-15 Sept
- **Authors**: Laura Costantini, Balazs Matuz, Gianluigi Liva +2
- **PDF**: https://ieeexplore.ieee.org/document/5586886
- **Abstract**: In this paper, an overview of recent achievements in the design and decoding of non-binary low-density parity-check (LDPC) codes is provided. Non-binary constructions based on ultra-sparse matrices are compared with binary low-density parity-check codes and turbo codes from satellite communication standards, to show that larger coding gains (outperforming the binary competitors by at least 0.3 dB) can be achieved on the AWGN channel, especially in the moderate/short block regimes. Thanks to this excellent performance, non-binary LDPC codes represent an appealing solution for space communications.

## New frontiers for the mobile satellite interactive services

- **Status**: ❌
- **Reason**: Ka밴드 위성 모바일 서비스 시스템/안테나/핸드오버 논문, LDPC ECC 언급 없음
- **ID**: ieee:5586863
- **Type**: conference
- **Published**: 13-15 Sept
- **Authors**: Eros Feltrin, Elisabeth Weller
- **PDF**: https://ieeexplore.ieee.org/document/5586863
- **Abstract**: The new generation multi-spot Ka band satellites increase dramatically the offer of capacity whose cost is consequently reduced and give promising perspectives for fix interactive broadband services and mobile services. However, if on one hand the market and deployment of fix interactive broadband services definitely benefit from Ka band, on the other hand concerning mobile services the drawback of a multi-spot coverage is the huge effort required for preparing the ground segment infrastructures and the associated technologies. A few examples of the issues Eutelsat is working on are the development of high performances Ka band low profile antennas and satellite systems able to manage the handover from one satellite spot-beam to another, the mitigation of the fading impacting the transmissions to/from mobiles and the dynamic routing of IP traffic. This paper describes the approach adopted by Eutelsat together with some partners in order to solve these problems on different communication layers, in view of the launch of the satellite KA-SAT. Preliminary analysis and results, also built on past experiences done in Ku band, are presented.

## A comparison of different physical layer network coding techniques for the satellite environment

- **Status**: ❌
- **Reason**: 물리계층 네트워크 코딩 비교, LDPC ECC 기법 없음
- **ID**: ieee:5586915
- **Type**: conference
- **Published**: 13-15 Sept
- **Authors**: Francesco Rossetto
- **PDF**: https://ieeexplore.ieee.org/document/5586915
- **Abstract**: The increased interest around the concept of "physical layer network coding" has generated a whole range of different technical solutions to implement it, which tradeoff complexity at the different elements of the network. While the effectiveness of this concept has been safely established for the two way relay channel, far less investigation has touched more sophisticated topologies, neither terrestrial nor satellite. Hence the scalability of such concepts has not yet been duly analyzed. We provide in this paper a first evaluation of this important idea in the satellite environment. Results show that the amplify-and-forward paradigm would scale rather badly and thus some computational capability at the relay (i.e., the satellite or the controlling gateway) are necessary.

## ALOE-Based Flexible LDPC Decoder

- **Status**: ❌
- **Reason**: ALOE 미들웨어 기반 유연 LDPC 디코더 FPGA 구현, 미들웨어 오버헤드 분석에 초점 — NAND 이식할 신규 디코더/코드/HW 기법 없음
- **ID**: ieee:5615595
- **Type**: conference
- **Published**: 1-3 Sept. 
- **Authors**: Ismael Gomez, Massimo Camatel, Jordi Bracke +4
- **PDF**: https://ieeexplore.ieee.org/document/5615595
- **Abstract**: Radio communications terminals and infrastructure tend to support an increasing range of algorithms and radio access technologies. Flexible processing platforms are therefore needed for supporting multi-standard or heterogeneous radios. Channel decoding is one of the most computing demanding digital signal processing blocks of a radio transceiver. At the same time, it provides a high degree of implementation flexibility as well as facilitates dynamic parameter adjustments. This paper presents a flexible LDPC decoder implemented on an FPGA device following the ALOE middleware design paradigm. We analyse the middleware efficiency in terms of flexibility versus resource requirements. The results show a relative middleware area overhead of 32 %.
