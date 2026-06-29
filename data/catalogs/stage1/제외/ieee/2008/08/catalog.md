# IEEE Xplore — 2008-08


## LDPC Codes for Flat Rayleigh Fading Channels with Channel Side Information

- **Status**: ❌
- **Reason**: Rayleigh 페이딩 채널용 EXIT 기반 LDPC 코드 설계 - 무선 응용 특이적 capacity-approaching 설계, 떼어낼 신규 NAND 이식 기법 없음
- **ID**: ieee:4600168
- **Type**: journal
- **Published**: August 200
- **Authors**: Yibo Jiang, Alexei Ashikhmin, Naresh Sharma
- **PDF**: https://ieeexplore.ieee.org/document/4600168
- **Abstract**: In this paper, we design capacity approaching low- density parity-check (LDPC) codes in the low signal-to-noise ratio (SNR) regime for flat Rayleigh fading channels with channel side information at transmitter and receiver. We use the structure advocated by Caire et al, which uses a single codebook with dynamic power allocation. The extrinsic information transfer (EXIT) function method is used to design the LDPC codes which approach the channel capacities. We also study the EXIT function properties of various demappers.

## Probabilistic Analysis of Linear Programming Decoding

- **Status**: ❌
- **Reason**: LP 디코딩의 확률적 오류정정 능력 분석 — 순수 이론 bound, 디코더/HW/구성으로 안 이어짐
- **ID**: ieee:4567569
- **Type**: journal
- **Published**: Aug. 2008
- **Authors**: Constantinos Daskalakis, Alexandros G. Dimakis, Richard M. Karp +1
- **PDF**: https://ieeexplore.ieee.org/document/4567569
- **Abstract**: We initiate the probabilistic analysis of linear programming (LP) decoding of low-density parity-check (LDPC) codes. Specifically, we show that for a random LDPC code ensemble, the linear programming decoder of Feldman succeeds in correcting a constant fraction of errors with high probability. The fraction of correctable errors guaranteed by our analysis surpasses previous nonasymptotic results for LDPC codes, and in particular, exceeds the best previous finite-length result on LP decoding by a factor greater than ten. This improvement stems in part from our analysis of probabilistic bit-flipping channels, as opposed to adversarial channels. At the core of our analysis is a novel combinatorial characterization of LP decoding success, based on the notion of a flow on the Tanner graph of the code. An interesting by-product of our analysis is to establish the existence of ldquoprobabilistic expansionrdquo in random bipartite graphs, in which one requires only that almost every (as opposed to every) set of a certain size expands, for sets much larger than in the classical worst case setting.

## Mitigation of linear and nonlinear impairments in high-speed optical networks by using LDPC-coded turbo equalization

- **Status**: ❌
- **Reason**: 광통신 LDPC-coded turbo equalization — 표준 large-girth QC-LDPC 사용, 신규 디코더/구성 기여 없고 광채널 등화 특이
- **ID**: ieee:4588335
- **Type**: journal
- **Published**: Aug. 2008
- **Authors**: Ivan B. Djordjevic, Lyubomir L. Minkov, Hussam G. Batshon
- **PDF**: https://ieeexplore.ieee.org/document/4588335
- **Abstract**: We study a turbo equalization scheme based on low-density parity-check (LDPC) coded turbo equalization (TE). This scheme is suitable for simultaneous: (i) suppression of intra-channel nonlinearities, (ii) chromatic dispersion compensation, and (iii) polarization-mode dispersion (PMD) compensation. LDPC coding is based on large girth (g ges 8) block-circulant codes, and maximum a posteriori probability (MAP) equalizer is based on Bahl-Cocke-Jelinek-Raviv (BJCR) algorithm. The ultimate channel capacity limits, assuming an independent identically distributed (i.i.d.) source are reported as well. In the presence of intrachannel nonlinearities the LDPC-coded TE provides almost 12 dB improvement over BCJR equalizer at BER of 10-8. For an NRZ system operating at 10 Gb/s with residual dispersion of 11200 ps/nm and for differential group delay of 50 ps, the LDPC-coded TE is only 1 dB away from the i.i.d channel capacity. The efficiency of LDPC-coded TE in PMD compensation is demonstrated experimentally, with decoding performed off line.

## Rate-compatible distributed arithmetic coding

- **Status**: ❌
- **Reason**: 분산 산술부호(Slepian-Wolf 소스코딩) — 채널 ECC 아님
- **ID**: ieee:4601444
- **Type**: journal
- **Published**: Aug. 2008
- **Authors**: Marco Grangetto, Enrico Magli, Roberto Tron +1
- **PDF**: https://ieeexplore.ieee.org/document/4601444
- **Abstract**: Distributed arithmetic coding has been shown to be effective for Slepian-Wolf coding with side information. In this letter, we extend it to rate-compatible coding, which is useful in presence of a feedback channel between encoder and decoder. The performance loss with respect to the original version is negligible.

## An efficient algorithm for ML decoding of raptor codes over the binary erasure channel

- **Status**: ❌
- **Reason**: Raptor 부호 ML 디코딩(BEC) — fountain/erasure, 비-LDPC, 떼어낼 LDPC BP 기법 없음
- **ID**: ieee:4601445
- **Type**: journal
- **Published**: Aug. 2008
- **Authors**: Saejoon Kim, Seunghyuk Lee, Sae-Young Chung
- **PDF**: https://ieeexplore.ieee.org/document/4601445
- **Abstract**: In this letter, we propose an efficient algorithm for maximum-likelihood decoding of Raptor codes used over the binary erasure channel. The algorithm is inspired by the decoding scheme suggested in the 3GPP multimedia broadcast/multicast services standard and is an improved version of it.

## Fixed-Complexity Soft MIMO Detection via Partial Marginalization

- **Status**: ❌
- **Reason**: MIMO soft 검출기(partial marginalization) — LDPC 부호·디코더 기법 아님, 무선 검출 특이
- **ID**: ieee:4520145
- **Type**: journal
- **Published**: Aug. 2008
- **Authors**: Erik G. Larsson, Joakim Jalden
- **PDF**: https://ieeexplore.ieee.org/document/4520145
- **Abstract**: This paper presents a new approach to soft demodulation for MIMO channels. The proposed method is an approximation to the exact a posteriori probability-per-bit computer. The main idea is to marginalize the posterior density for the received data exactly over the subset of the transmitted bits that are received with the lower signal-to-noise-ratio (SNR), and marginalize this density approximately over the remaining bits. Unlike the exact demodulator, whose complexity is huge due to the need for enumerating all possible combinations of transmitted constellation points, the proposed method has very low complexity. The algorithm has a fully parallel structure, suitable for implementation in parallel hardware. Additionally, its complexity is fixed, which makes it suitable for pipelined implementation. We also show how the method can be extended to the situation when the receiver has only partial channel state information, and how it can be modified to take soft-input into account. Numerical examples illustrate its performance on slowly fading 4 times 4 and 6 times 6 complex MIMO channels.

## A High-Throughput Maximum a Posteriori Probability Detector

- **Status**: ❌
- **Reason**: MAP 채널 검출기(EEPR4) HW — LDPC 디코더가 아닌 채널 등화 검출기, 떼어낼 LDPC 기법 없음
- **ID**: ieee:4578762
- **Type**: journal
- **Published**: Aug. 2008
- **Authors**: Ruwan Ratnayake, Aleksandar Kavcic, Gu-Yeon Wei
- **PDF**: https://ieeexplore.ieee.org/document/4578762
- **Abstract**: This paper presents a maximum a posteriori probability (MAP) detector, based on a forward-only algorithm that can achieve high throughputs. The MAP algorithm is optimal in terms of bit error rate (BER) performance and, with Turbo processing, can approach performance close to the channel capacity limit. The implementation benefits from optimizations performed at both algorithm and circuit level. The proposed detector utilizes a deep-pipelined architecture implemented in skew-tolerant domino and experimentally measured results verify the detector can achieve throughputs greater than 750 Mb/s while consuming 2.4 W. The 16-state EEPR4 channel detector is implemented in a 0.13$\ \mu{\hbox {m}}$  CMOS technology and has a core area of 7.1  ${\hbox {mm}}^{2}$.

## Improved Data Detection Exploiting Full Cyclic Prefix for the Evolution of DVB-T

- **Status**: ❌
- **Reason**: DVB-T OFDM 수신기 cyclic prefix 데이터 검출 개선, LDPC는 부수 언급, 떼어낼 ECC 기법 없음
- **ID**: ieee:4600085
- **Type**: conference
- **Published**: 6-8 Aug. 2
- **Authors**: Lorenzo Vangelista, Marco Rotoloni, Alberto Morello
- **PDF**: https://ieeexplore.ieee.org/document/4600085
- **Abstract**: Orthogonal frequency division multiplexing (OFDM) has significantly reduced the complexity of the receivers, however to allow simple equalization procedures and avoid interblock interference, a cyclic prefix (CP) has to be appended to the OFDM block. CP reduces the efficiency of the transmission, because it is discarded at the receiver. This paper proposes a receiver structure which recovers the CP and exploits it to improve data detection. The performance of this structure is then analyzed comparing it with other two structures in a simulation scenario suitable for the evolution of the current Terrestrial Digital Video Broadcasting (DVB-T). The impact of low-density parity check codes (LDPC) is also outlined.

## Coding Schemes Applied to Peak-to-Average Power Ratio (PAPR) Reduction in OFDM Systems

- **Status**: ❌
- **Reason**: OFDM PAPR 감소용 코딩(패리티검사/SLM), 무선 응용 특이적, NAND LDPC ECC로 떼어낼 디코더·구성 기법 없음
- **ID**: ieee:4600038
- **Type**: conference
- **Published**: 6-8 Aug. 2
- **Authors**: Jyh-Horng Wen, Gwo-Ruey Lee, Chih-Chung Kung +1
- **PDF**: https://ieeexplore.ieee.org/document/4600038
- **Abstract**: High PAPR of the transmitted signal is a major drawback in the OFDM systems. In this paper, coding schemes are proposed to reduce high PAPR One is using parity check coding scheme, and the other is using selected mapping (SLM) applied scheme. With parity check coding scheme, the parity information is used to expand the signal space. Mapping from original source information to the corresponding message sequence with a low PAPR the PAPR of transmitted signal can be reduced. In the SLM applied scheme, a coding scheme with data position permutation and phase rotation is used. For the practical application to IEEE 802.11g, the performance of PAPR reduction is given. The simulation results show PAPR definitely can be greatly reduced with applying the SLM applied coding scheme in the OFDM system.

## Low-Complexity LDPC Codes with Near-Optimum Performance over the BEC

- **Status**: ❌
- **Reason**: BEC erasure ML 디코딩 LDPC vs Raptor 성능비교, erasure/소거채널 응용으로 NAND 채널 ECC 기법 없음
- **ID**: ieee:4620277
- **Type**: conference
- **Published**: 26-28 Aug.
- **Authors**: Enrico Paolini, Michela Varrella, Marco Chiani +2
- **PDF**: https://ieeexplore.ieee.org/document/4620277
- **Abstract**: Recent works showed how low-density parity-check (LDPC) erasure correcting codes, under maximum likelihood (ML) decoding, are capable of tightly approaching the performance of an ideal maximum-distance-separable code on the binary erasure channel. Such result is achievable down to low error rates, even for small and moderate block sizes, while keeping the decoding complexity low, thanks to a class of decoding algorithms which exploits the sparseness of the parity-check matrix to reduce the complexity of Gaussian elimination (GE). In this paper the main concepts underlying ML decoding of LDPC codes are recalled. A performance analysis among various LDPC code classes is then carried out, including a comparison with fixed-rate Raptor codes. The results confirm that a judicious LDPC code design allows achieving achieving a near-optimum performance on the erasure channel, with very low error floors. Furthermore, it is shown that LDPC and Raptor codes, under ML decoding, provide almost identical performance in terms of decoding failure probability vs. overhead.

## Short IRA Codes for Mobile DVB-RCS

- **Status**: ❌
- **Reason**: DVB-RCS 표준용 short IRA(LDPC) 부호 성능평가, 무선 응용 특이적이고 신규 이식 기법 없음
- **ID**: ieee:4620274
- **Type**: conference
- **Published**: 26-28 Aug.
- **Authors**: Gianluigi Liva, Cristina Parraga Niebla, S. Scalise +4
- **PDF**: https://ieeexplore.ieee.org/document/4620274
- **Abstract**: In this paper, the design of the new short low-density parity-check introduced in the upcoming version of DVB-RCS standard targeting interactive mobile services will be described. The codes performance evaluation on the additive white Gaussian noise sand on a mobile (Rice-distributed) fading channels will be carried out assuming QPSK, 8PSK, 16APSK, and 32APSK modulations.

## Recovering from Packet Losses in CCSDS Links

- **Status**: ❌
- **Reason**: CCSDS 패킷 소거 복구 erasure code 구현 비교, 패킷 레벨 소거코드로 떼어낼 ECC 기법 없음
- **ID**: ieee:4620278
- **Type**: conference
- **Published**: 26-28 Aug.
- **Authors**: Enrico Paolini, Michela Varrella, Marco Chiani +1
- **PDF**: https://ieeexplore.ieee.org/document/4620278
- **Abstract**: Data unit losses in deep space communications are currently faced using retransmission techniques which are however inefficient due to the large round trip delays. For this reason, the Consultative Committee for Space Data Systems (CCSDS) has recently considered packet erasure correcting codes for inclusion in its recommendations for space data system standards. Erasure correcting codes are expected to replace (or drastically reduce) retransmission requests. Erasure codes operate on packets instead of bits and are usually implemented above at the upper layers of the communication stack. In this paper, the implementation of erasure codes within the CCSDS communication stack is considered. Moreover, a comparison in terms of decoding complexity when using a maximum likelihood (ML) erasure decoder in the Control Center is performed between possible solutions, namely Raptor codes and low-density parity-check (LDPC) codes.

## Experimental Validation of Advanced Mobile Broadcasting Waveform in S-Band

- **Status**: ❌
- **Reason**: DVB-SH 위성 모바일 방송 파형 실험 검증, 떼어낼 LDPC 디코더/구성 기법 없음
- **ID**: ieee:4620255
- **Type**: conference
- **Published**: 26-28 Aug.
- **Authors**: A. Heuberger, H. Stadali, Balazs Matuz +6
- **PDF**: https://ieeexplore.ieee.org/document/4620255
- **Abstract**: Herein, the results of the ESA co-funded research project named "ORTIGIA" are summarized The scope of the project was to validate experimentally the techniques introduced by the DVB-SH working group to counteract fading in satellite and terrestrial environments. The experiments include measurements both on the field and in the laboratory.

## Random discrete measure of the phase posterior pdf in turbo synchronization

- **Status**: ❌
- **Reason**: turbo 동기화 위상잡음 추정 particle filter, LDPC는 시뮬레이션 부수 언급, 떼어낼 디코더 기법 없음
- **ID**: ieee:7080329
- **Type**: conference
- **Published**: 25-29 Aug.
- **Authors**: Nicolas Paul, Didier Le Ruyet, Tanya Bertozzi +1
- **PDF**: https://ieeexplore.ieee.org/document/7080329
- **Abstract**: In this paper we consider the iterative decoding of channels with strong phase noise. We propose to use a random discrete measure to estimate the phase posterior pdf given the past observations (forward pdf) and another random discrete measure to estimate the phase posterior pdf given the future observations (backward pdf). The particle filter algorithm is used to recursively generate the supports in the relevant phase space area and recursively update the weights associated to these supports. An estimation of the phase posterior pdf given all the past and future observations is then derived from the forward and backward measures. The relevance of our proposal is finally illustrated through simulation of binary LDPC codes and QPSK modulation over a severe Wiener-Levy phase noise with a standard deviation of πΔ = 6 degrees. Our algorithm is compared with a forward-backward message passing algorithm performed over a trellis resulting from the discretization of the phase. The proposed algorithm leads to a a slight performance degradation compared to the optimal treillis based method.

## Practical distributed source coding with impulse-noise degraded side information at the decoder

- **Status**: ❌
- **Reason**: Wyner-Ziv 분산 소스코딩(Slepian-Wolf), q-ary LDPC — 소스코딩+비이진, 채널 ECC 아님
- **ID**: ieee:7080715
- **Type**: conference
- **Published**: 25-29 Aug.
- **Authors**: Claudio Weidmann, Francesca Bassi, Michel Kieffer
- **PDF**: https://ieeexplore.ieee.org/document/7080715
- **Abstract**: This paper introduces a practical method for distributed lossy compression (Wyner-Ziv quantization) with side information available only at the decoder, where the side information is equal to the signal affected by background noise and additional impulse noise. At the core of the method is an LDPC-based lossless distributed (Slepian-Wolf) source code for q-ary alphabets, which is matched to the impulse probability and allows to remove the scalar-quantized impulse noise. Applications of this method to distributed compressed sensing of signals that differ in a sparse set of locations is also discussed, as well as some differences and similarities of variable- and fixed-length coding of sparse signals.

## Lossless compression of encrypted grey-level and color images

- **Status**: ❌
- **Reason**: 암호화 이미지 무손실 압축(소스코딩 with side info), 채널 ECC가 아님
- **ID**: ieee:7080641
- **Type**: conference
- **Published**: 25-29 Aug.
- **Authors**: Riccardo Lazzeretti, Mauro Barni
- **PDF**: https://ieeexplore.ieee.org/document/7080641
- **Abstract**: The feasibility of lossless compression of encrypted images has been recently demonstrated by relying on the analogy with source coding with side information at the decoder. However previous works only addressed the compression of bilevel images, namely sparse black and white images, with asymmetric probabilities of black and white pixels. In this paper we investigate the possibility of compressing encrypted grey level and color images, by decomposing them into bit-planes. A few approaches to exploit the spatial and cross-plane correlation among pixels are discussed, as well as the possibility of exploiting the correlation between color bands. Some experimental results are shown to evaluate the gap between the proposed solutions and the theoretically achievable performance.

## Analysis of error propagation due to frame losses in a distributed video coding system

- **Status**: ❌
- **Reason**: 분산 비디오 코딩 프레임 손실 오류전파 이론 모델 — LDPC ECC 기법 없음, 소스코딩/응용 특이적
- **ID**: ieee:7080668
- **Type**: conference
- **Published**: 25-29 Aug.
- **Authors**: Thomas Maugey, Thomas André, Béatrice Pesquet-Popescu +1
- **PDF**: https://ieeexplore.ieee.org/document/7080668
- **Abstract**: In this paper, we propose a theoretical model for the error propagation phenomenon generated by a frame loss in a distributed video coding framework. Using rate-distortion functions, we analyze the impact of a frame loss on the average distortion of a group of pictures depending on the position of the lost frame within the GOP, as well as the level of motion in each frame and the quantization errors in the key frames and the Wyner-Ziv frames. This theoretical analysis is further confirmed by a practical implementation of the DVC framework using different configurations of frame losses.

## Convolutional codes for iterative decoding

- **Status**: ❌
- **Reason**: 반복디코딩용 컨볼루션 부호 개관 — 비-LDPC 부호, 부호 비의존 이식 기법 없음, 개관성
- **ID**: ieee:4621512
- **Type**: conference
- **Published**: 25-28 Aug.
- **Authors**: Michael Lentmaier, Gerhard P. Fettweis, Kamil Sh. Zigangirov +1
- **PDF**: https://ieeexplore.ieee.org/document/4621512
- **Abstract**: This paper gives an overview of three different classes of convolutional codes that are suitable for iterative decoding. They are characterized by the type of component codes that are used to construct the overall codes, which can be trivial parity-check constraints, block component codes, or convolutional component codes. Distance properties and iterative decoding performance are considered. All three classes of codes are asymptotically good, allow simple encoding, and can be decoded efficiently using iterative pipeline decoding architectures.

## Adapted LDPC Error Correction Scheme for 2D Optical CDMA Multimedia System

- **Status**: ❌
- **Reason**: 2D OCDMA 광통신 응용에 LDPC 디코딩을 MAI 노이즈 분포에 적응시킨 것으로, NAND로 떼어낼 신규 디코더 기법 없음(응용 특이적)
- **ID**: ieee:4621510
- **Type**: conference
- **Published**: 25-28 Aug.
- **Authors**: Stephanie Sahuguede, Anne Julien-Vergonjanne, Jean-Pierre Cances
- **PDF**: https://ieeexplore.ieee.org/document/4621510
- **Abstract**: To provide multimedia services in optical networks, 2 dimensional optical code division multiple access (2D OCDMA) system is considered as a potential solution. We focus here on a 2D OCDMA system using 2D multi-weight codes and parallel mapping technique to provide respectively quality of service (QoS) and data rate differentiation. To improve the performance of such a scheme, we investigate forward error correction (FEC) based on low density parity check (LDPC) codes known to have an efficient error correction power for Gaussian channels. We particularly propose an adaptation of the LDPC decoding scheme to the 2D OCDMA multimedia channel which has a specific noise distribution due to multiple access interference (MAI). We evaluate the system robustness to additive white Gaussian noise (AWGN) perturbation in addition to MAI and the gain provided in term of SNR. Finally, we show that the adapted FEC scheme we propose, not only permits improving the data rate per service but also the number of simultaneously communicating users.

## Soft Detection of Modulation Diversity Schemes for Next Generation Digital Terrestrial Television

- **Status**: ❌
- **Reason**: DVB-T2 변조 다이버시티 소프트 검출 비교 — LDPC는 부수 시나리오, 떼어낼 디코더/코드설계 기법 없음
- **ID**: ieee:4621429
- **Type**: conference
- **Published**: 25-28 Aug.
- **Authors**: Alberto Vigato, Stefano Tomasin, Lorenzo Vangelista +2
- **PDF**: https://ieeexplore.ieee.org/document/4621429
- **Abstract**: The next generation of digital terrestrial television (DVB-T2) standard requires to improve performance of the current DVB-T standard. Commercial and technical reasons suggest that orthogonal frequency division multiplexing (OFDM) could still be adopted. As multiple-input multiple-output antennas techniques are not backward compatible with current constellations, new modulation methods suitable for OFDM in the presence of Rayleigh fading channels could be developed in order to provide diversity gain without spectral or power inefficiencies. In this paper we compare three modulation methods, namely, (1) re-mapped repetition, (2) rotational multi-carrier and (3) multidimensional rotated QAM, in a low-density parity-check (LDPC) block code scenario. As most of the modulation methods were introduced for an uncoded scenario, indeed it is seen that in the presence of coding, the bit error rate deeply differs from that in an uncoded scenario.

## Multiuser Detection Algorithm for CDMA Based on the Belief Propagation Algorithm

- **Status**: ❌
- **Reason**: CDMA 다중사용자 검출 BP 알고리즘 — 검출용 factor graph 변환, LDPC 부호 디코더 비의존, 무선응용 특이적
- **ID**: ieee:4621400
- **Type**: conference
- **Published**: 25-28 Aug.
- **Authors**: Shunsuke Horii, Tota Suko, Toshiyasu Matsushima +1
- **PDF**: https://ieeexplore.ieee.org/document/4621400
- **Abstract**: Optimum detection for the multiuser code-division multiple-access channel is prohibitively complex. This paper considers new iterative multiuser detection algorithm based on the belief propagation algorithm. Previously, the idea to apply the belief propagation algorithm to multiuser detection problem was suggested , however, it was believed that to apply the belief propagation algorithm to the detection problem is impossible because it requires an exponentially large amount of computation. It was the only fact that the parallel interference canceller is derived as an approximation of the belief propagation. In this paper, we show that the belief propagation algorithm can be applied to the detection problem by converting the factor graph structure. Performance of the detector based on the belief propagation algorithm is better than that of the parallel interference canceller.

## Construction of quantum low density parity check code based on quasi-cyclic sparse sequence

- **Status**: ❌
- **Reason**: 양자 LDPC 구성, 양자 채널 전용이며 떼어낼 고전 바이너리 신규 기법 없음
- **ID**: ieee:4685067
- **Type**: conference
- **Published**: 25-27 Aug.
- **Authors**: Sheng-mei Zhao, Bao-yui Zheng, Wan-nai Wang
- **PDF**: https://ieeexplore.ieee.org/document/4685067
- **Abstract**: In this paper, a construction method of quantum low density parity check codes (quantum LDPC) which based on classical quasi-cyclic sparse sequence is proposed, and the quantum code QLDPC(3,8)(16,6) and QLDPC(3,8)(64,24) are selected as examples to illustrate this construction method. The performances of this kind quantum LDPC codes are discussed over the bit-flipping channel by numerical simulations. The results show that these quantum codes have good ability to correct error in quantum channel.

## EXIT-chart-based power allocations for superposition multilevel coding systems

- **Status**: ❌
- **Reason**: 멀티레벨 코딩 EXIT 차트 기반 전력할당, ECC 디코더/HW/코드설계 기법 없는 통신 응용
- **ID**: ieee:4685037
- **Type**: conference
- **Published**: 25-27 Aug.
- **Authors**: Xiuni Wang, Xiao Ma
- **PDF**: https://ieeexplore.ieee.org/document/4685037
- **Abstract**: Multilevel coding with sigma-mapping is one simple way to obtain coding gain as well as shaping gain, while power-allocation, by allocating proper powers to different levels, can facilitate the iterative decoding/detection algorithms. In this paper, we utilize the EXIT chart to calculate the convergence threshold for each level by treating the signals from other levels as Gaussian noise. Based on the threshold, we propose a simple power allocation scheme. Numerical results show that the proposed EXIT-based power allocation scheme improves the performance when compared with the existing Gaussian approximation power allocation scheme while still keeping a reasonable complexity.

## Constructing linear codes with good joint spectra

- **Status**: ❌
- **Reason**: JSCC용 linear code joint spectra 구성, 소스-채널 결합이라 떼어낼 ECC 기법 없음
- **ID**: ieee:4685175
- **Type**: conference
- **Published**: 25-27 Aug.
- **Authors**: Shengtian Yang, Yan Chen, Thomas Honold +2
- **PDF**: https://ieeexplore.ieee.org/document/4685175
- **Abstract**: The problem of finding good linear codes for joint source-channel coding (JSCC) is investigated in this paper. By the code-spectrum approach, it has been proved in the authors' previous paper that a good linear code for the authors' JSCC scheme is a code with a good joint spectrum, so the main task in this paper is to construct linear codes with good joint spectra. First, the code-spectrum approach is developed further to facilitate the calculation of spectra. Second, some general principles for constructing good linear codes are presented. Finally, we propose an explicit construction of linear codes with good joint spectra based on low density parity check (LDPC) codes and low density generator matrix (LDGM) codes.

## Security Research on an Information-Theoretically Secure Secret Key Agreement Using LDPC Matrices

- **Status**: ❌
- **Reason**: LDPC 행렬 기반 정보이론적 비밀키합의 보안 분석; 채널 ECC 아닌 키합의/보안, 원칙 제외
- **ID**: ieee:4624489
- **Type**: conference
- **Published**: 20-22 Aug.
- **Authors**: Jia Yu, Yuan Luo, Minglu Li
- **PDF**: https://ieeexplore.ieee.org/document/4624489
- **Abstract**: Secret key agreement is a major task in network security solutions using secret-key cryptosystems. An information-theoretically secure secret key agreement protocol using LDPC matrices was introduced by Jun Muramatsu. In this paper, the enemy can obtain not only full transmitted messages but also partial side information. We are interested in the equivocation of the generated key to this more powerful enemy. A relation between the security of the secret key agreement protocol and the LDPC matrices used in it is also discussed.
