# arXiv — 2019-01


## Model-Based Detector for SSDs in the Presence of Inter-cell Interference

- **Status**: ✅
- **Reason**: SSD ICI 채널모델로 soft LDPC 디코더에 더 정확한 LLR 공급, 검출기-디코더 반복 스킴 — A/C 이식 가능, NAND 직접 관련
- **ID**: arxiv:1902.01212v2
- **Type**: preprint
- **Published**: 2019-01-31
- **Authors**: Hachem Yassine, Mihai-Alin Badiu, Justin Coon
- **PDF**: https://arxiv.org/pdf/1902.01212v2
- **Abstract**: In this paper, we consider the problem of reducing the bit error rate of flash-based solid state drives (SSDs) when cells are subject to inter-cell interference (ICI). By observing that the outputs of adjacent victim cells can be correlated due to common aggressors, we propose a novel channel model to accurately represent the true flash channel. This model, equivalent to a finite-state Markov channel model, allows the use of the sum-product algorithm to calculate more accurate posterior distributions of individual cell inputs given the joint outputs of victim cells. These posteriors can be easily mapped to the log-likelihood ratios that are passed as inputs to the soft LDPC decoder. When the output is available with high precision, our simulation showed that a significant reduction in the bit-error rate can be obtained, reaching $99.99\%$ reduction compared to current methods, when the diagonal coupling is very strong. In the realistic case of low-precision output, our scheme provides less impressive improvements due to information loss in the process of quantization. To improve the performance of the new detector in the quantized case, we propose a new iterative scheme that alternates multiple times between the detector and the decoder. Our simulations showed that the iterative scheme can significantly improve the bit error rate even in the quantized case.

## Capacity Optimality of AMP in Coded Systems

- **Status**: ❌
- **Reason**: Turbo-AMP 용량 분석과 LRMS 이론 중심, 이진 LDPC BP에 떼어낼 신규 디코더/구성 없음 — 순수 이론 bound
- **ID**: arxiv:1901.09559v4
- **Type**: preprint
- **Published**: 2019-01-28
- **Authors**: Lei Liu, Chulong Liang, Junjie Ma +1
- **PDF**: https://arxiv.org/pdf/1901.09559v4
- **Abstract**: This paper studies a large random matrix system (LRMS) model involving an arbitrary signal distribution and forward error control (FEC) coding. We establish an area property based on the so-called Turbo approximate message passing (Turbo-AMP) algorithm. Under the assumption that the state evolution for AMP is correct for the coded system, the achievable rate of Turbo-AMP is analyzed. We prove that Turbo-AMP achieves the constraint capacity of the LRMS with an arbitrary signal distribution provided that a matching condition is satisfied. As a byproduct, we provide an alternative derivation for the constraint capacity of an LRMS using a proved property of AMP. We discuss realization techniques for the matching principle of binary signaling using irregular low-density parity-check (LDPC) codes and provide related numerical results. We show that optimized codes demonstrate significantly better performance over un-matched ones under Turbo-AMP. For quadrature phase shift keying (QPSK) modulation, bit error rate (BER) performance within 1 dB from the constrained capacity limit is observed.

## Design and Decoding of Polar Codes for the Gaussian Multiple Access Channel

- **Status**: ❌
- **Reason**: polar 부호 NOMA 설계·SC 디코딩, LDPC는 비교 대상일 뿐 이식 가능한 LDPC 기법 없음
- **ID**: arxiv:1901.07297v1
- **Type**: preprint
- **Published**: 2019-01-22
- **Authors**: Evgeny Marshakov, Gleb Balitskiy, Kirill Andreev +1
- **PDF**: https://arxiv.org/pdf/1901.07297v1
- **Abstract**: Massive machine-type communications (mMTC) is one of the key application scenarios for future 5G networks. Non-orthogonal multiple access (NOMA) is a promising technique for the use in mMTC scenario. In this paper, we investigate NOMA schemes based on polar codes. We compare two possible decoding techniques: joint successive cancellation algorithm and joint iterative algorithm. In order to optimize the codes (choose frozen bits) we propose a special and efficient design algorithm. We investigate the performance of the resulting scheme in the Gaussian multiple access channel (GMAC) by means of simulations. The scheme is shown to outperform LDPC based solution by approximately 1 dB and to be close to the achievability bound for GMAC.

## Polarization-ring-switching for nonlinearity-tolerant geometrically-shaped four-dimensional formats maximizing generalized mutual information

- **Status**: ❌
- **Reason**: 4D 변조포맷 GMI 최적화, LDPC는 부수 언급, 떼어낼 ECC 기법 없음 — 무선/광 응용 특이적
- **ID**: arxiv:1901.06878v2
- **Type**: preprint
- **Published**: 2019-01-21
- **Authors**: Bin Chen, Chigo Okonkwo, Hartmut Hafermann +1
- **PDF**: https://arxiv.org/pdf/1901.06878v2
- **Abstract**: In this paper, a new four-dimensional 64-ary polarization ring switching (4D-64PRS) modulation format with a spectral efficiency of 6 bit/4D-sym is introduced. The format is designed by maximizing the generalized mutual information (GMI) and by imposing a constant-modulus on the 4D structure. The proposed format yields an improved performance with respect to state-of-the-art geometrically shaped modulation formats for bit-interleaved coded modulation systems at the same spectral efficiency. Unlike previously published results, the coordinates of the constellation points and the binary labeling of the constellation are jointly optimized. When compared with polarization-multiplexed 8-ary quadrature-amplitude modulation (PM-8QAM), gains of up to 0.7 dB in signal-to-noise ratio are observed in the additive white Gaussian noise (AWGN) channel. For a long-haul nonlinear optical fiber system of 8,000 km, gains of up to 0.27 bit/4D-sym (5.5% data capacity increase) are observed. These gains translate into a reach increase of approximately 16% (1,100 km). The proposed modulation format is also shown to be more tolerant to nonlinearities than PM-8QAM. Results with LDPC codes are also presented, which confirm the gains predicted by the GMI.

## Spatially Coupled LDPC Codes and the Multiple Access Channel

- **Status**: ❌
- **Reason**: SC-LDPC를 IDMA 다중접속 검출기와 결합, 윈도우 검출/디코더는 MUD 의존적이고 표준 SC-LDPC 사용 — 통신 응용 특이적, 떼어낼 신규 ECC 기법 없음
- **ID**: arxiv:1901.05877v2
- **Type**: preprint
- **Published**: 2019-01-17
- **Authors**: Sebastian Cammerer, Xiaojie Wang, Yingyan Ma +1
- **PDF**: https://arxiv.org/pdf/1901.05877v2
- **Abstract**: We consider spatially coupled low-density parity-check (SC-LDPC) codes within a non-orthogonal interleave division multiple access (IDMA) scheme to avoid cumbersome degree profile matching of the LDPC code components to the iterative multi-user detector (MUD). Besides excellent decoding thresholds, the approach benefits from the possibility of using rather simple and regular underlying block LDPC codes owing to the universal behavior of the resulting coupled code with respect to the channel front-end, i.e., the iterative MUD. Furthermore, an additional outer repetition code makes the scheme flexible to cope with a varying number of users and user rates, as the SC-LDPC itself can be kept constant for a wide range of different user loads. The decoding thresholds are obtained via density evolution (DE) and verified by bit error rate (BER) simulations. To keep decoding complexity and latency small, we introduce a joint iterative windowed detector/decoder imposing carefully adjusted sub-block interleavers. Finally, we show that the proposed coding scheme also works for Rayleigh channels using the same code with tolerable performance loss compared to the additive white Gaussian noise (AWGN) channel.

## Protograph-Based LDPC Code Design for Probabilistic Shaping with On-Off Keying

- **Status**: ✅
- **Reason**: protograph 기반 LDPC 코드 설계(신규 구성)는 E에 해당, OOK는 응용이나 코드설계 기법 이식 가능 — 애매하여 살림
- **ID**: arxiv:1901.03285v1
- **Type**: preprint
- **Published**: 2019-01-10
- **Authors**: Alexandru Dominic Git, Balázs Matuz, Fabian Steiner
- **PDF**: https://arxiv.org/pdf/1901.03285v1
- **Abstract**: This work investigates protograph-based LDPC codes for the AWGN channel with OOK modulation. A non-uniform distribution of the OOK modulation symbols is considered to improve the power efficiency especially for low SNRs. To this end, a specific transmitter architecture based on time sharing is proposed that allows probabilistic shaping of (some) OOK modulation symbols. Tailored protograph-based LDPC code designs outperform standard schemes with uniform signaling and off-the-shelf codes by 1.1 dB for a transmission rate of 0.25 bits/channel use.

## Coding Techniques for Future Wi-Fi

- **Status**: ❌
- **Reason**: Wi-Fi용 LDPC 코딩 개요 기사(서베이성), root-check 구조 등 언급뿐 구체 신규 기여 불명 — 무선 응용 서베이
- **ID**: arxiv:1901.01348v1
- **Type**: preprint
- **Published**: 2019-01-05
- **Authors**: A. G. D. Uchoa, R. C. de Lamare
- **PDF**: https://arxiv.org/pdf/1901.01348v1
- **Abstract**: Future wireless applications such as high definition video streaming, wireless cloud radio access networks, and cellular data offload are bandwidth-hungry, which highlights the need for Wi-Fi links exceeding 1 Gb/s. This article discusses coding schemes and, in particular, the use of Low-Density Parity-Check (LDPC) codes as Forward Error Correction (FEC) in future Wi-Fi standards. Moreover, we consider advanced design strategies such as root-check LDPC structures, computer-aided design for short blocks and high-performance decoding algorithms with low latency. We then conclude the article with a discussion of FEC challenges for future Wi-FI applications.

## Convolutionally Coded SNR-Adaptive Transmission for Low-Latency Communications

- **Status**: ❌
- **Reason**: convolutional 부호 + 적응 변조, 비-LDPC이고 LDPC는 비교 언급뿐 — 비-LDPC 부호
- **ID**: arxiv:1901.03641v1
- **Type**: preprint
- **Published**: 2019-01-04
- **Authors**: Mehmet Cagri Ilter, Halim Yanikomeroglu
- **PDF**: https://arxiv.org/pdf/1901.03641v1
- **Abstract**: Fifth generation new radio aims to facilitate new use cases in wireless communications. Some of these new use cases have highly de-manding latency requirements; many of the powerful forward error correction codes deployed in current systems, such as the turbo and low-density parity-check codes, do not perform well when the low-latency requirement does not allow iterative decoding. As such, there is a rejuvenated interest in noniterative/one-shot decoding algorithms. Motivated by this, we propose a signal-to-noise ratio-adaptive convolutionally coded system with optimized constellations designed specifically for a particular set of convolutional code parameters. Numerical results show that significant performance improvements in terms of bit-error-rate and spectral efficiency can be obtained compared to the traditional adaptive modulation and coding systems inlow-latency communications.
