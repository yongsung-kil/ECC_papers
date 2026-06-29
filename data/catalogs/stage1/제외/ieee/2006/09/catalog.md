# IEEE Xplore — 2006-09


## On the Asymptotic Weight and Stopping Set Distribution of Regular LDPC Ensembles

- **Status**: ❌
- **Reason**: 정규 LDPC 앙상블 weight/stopping set 분포의 점근적 분산 추정 — 순수 이론 bound, 디코더/HW/구성으로 이어지지 않음
- **ID**: ieee:1683937
- **Type**: journal
- **Published**: Sept. 2006
- **Authors**: V. Rathi
- **PDF**: https://ieeexplore.ieee.org/document/1683937
- **Abstract**: In this correspondence, we estimate the variance of weight and stopping set distribution of regular low-density parity-check (LDPC) ensembles. Using this estimate and the second moment method we obtain bounds on the probability that a randomly chosen code from regular LDPC ensemble has its weight distribution and stopping set distribution close to respective ensemble averages. We are able to show that a large fraction of total number of codes have their weight and stopping set distribution close to the average

## Optimal Power/Rate Allocation and Code Selection for Iterative Joint Detection of Coded Random CDMA

- **Status**: ❌
- **Reason**: 코딩된 random CDMA 반복간섭제거 전력/율 할당 분석 — 무선 통신 응용 특이적, 떼어낼 LDPC ECC 기법 없음
- **ID**: ieee:1683950
- **Type**: journal
- **Published**: Sept. 2006
- **Authors**: C. Schlegel, Z. Shi, M. Burnashev
- **PDF**: https://ieeexplore.ieee.org/document/1683950
- **Abstract**: Iterative interference cancellation of coded code-division multiple access (CDMA) using random spreading with linear cancellation is analyzed. If users are grouped into power classes and Shannon bound approaching codes are used, a geometric power distribution achieves the additive white Gaussian noise (AWGN) channel Shannon bound as the numbers of classes becomes large. The optimal distribution of the size of these classes is shown to be uniform. If users are grouped into different rate classes with equal powers among equal rate users, the Shannon bound for AWGN channels can be achieved with an arbitrary distribution of the classes sizes, provided that the size of the largest rate class obeys the mild condition that its ratio of size to processing gain is much smaller than the inverse of the signal-to-noise ratio (SNR). The case of equal powers and equal rates among all users is addressed as a "worst case" scenario. It is argued that simple repetition codes provide for a larger achievable capacity than stronger codes. It is shown that this capacity monotonically increases as the rate of the code decreases. A density evolution analysis is used to show that the achievable rates exceed those of a minimum-mean square error filter applied to the uncoded signals. This lower bound is tight for small ratios of bit energy to noise power, and otherwise the iterative cancellation receiver provides an appreciably larger capacity. Relating to recent result from the application of statistical mechanics it is shown that the repetition-coded system with iterative cancellation achieves the performance of an equivalent optimal joint detector for uncoded transmission

## Adaptive demodulation using rateless erasure codes

- **Status**: ❌
- **Reason**: Raptor/rateless erasure 코드 기반 적응 복조 — fountain/erasure 부호, 떼어낼 LDPC ECC 기법 없음
- **ID**: ieee:1703815
- **Type**: journal
- **Published**: Sept. 2006
- **Authors**: J.D. Brown, S. Pasupathy, K.N. Plataniotis
- **PDF**: https://ieeexplore.ieee.org/document/1703815
- **Abstract**: We introduce a rate-adaptive system in which the receiver demodulates only those bits that have a high probability of being correct, treating nondemodulated bits as erasures. Several sets of decision regions, derived using composite hypothesis testing, are proposed for 16-QAM and 16-phase-shift keying, which allow for the simple implementation of this demodulation strategy. We demonstrate that pre-encoding the data with a Raptor code allows for simple reconstruction of the message, regardless of the erasure pattern introduced from the nondemodulated bits. We prove the optimality of the proposed decision regions in selecting the most likely subset of bits from any received symbol in moderate-to-high signal-to-noise ratios, and we analyze the performance of demodulating with these decision regions over an additive white Gaussian noise channel. Also demonstrated is the strong performance of 16-QAM for this application, compared with other power-efficient constellations and the near-optimality of using Gray mapping, even under the proposed alternate sets of decision regions.

## On the design of bit-interleaved turbo-coded modulation with low error floors

- **Status**: ❌
- **Reason**: 터보 부호화 변조(BITCM) 비트인터리버 error-floor 최적화 — 비-LDPC(터보) 부호이고 변조/인터리버 특화, BP 이식 기법 없음
- **ID**: ieee:1703814
- **Type**: journal
- **Published**: Sept. 2006
- **Authors**: E. Rosnes, O. Ytrehus
- **PDF**: https://ieeexplore.ieee.org/document/1703814
- **Abstract**: In this paper, we introduce an algorithm to optimize the performance in the error-floor region of bit-interleaved turbo-coded modulation (BITCM) on the additive white Gaussian noise channel. The key ingredient is an exact turbo code weight distribution algorithm producing a list of all codewords in the underlying turbo code of weight less than a given threshold. In BITCM, the information sequence is turbo-encoded, bit-interleaved, and mapped to signal points in a signal constellation. Using the union-bounding technique, we show that a well-designed bit interleaver is crucial to have a low error floor. Furthermore, the error-rate performance in the waterfall region depends on the bit interleaver, since the level of protection from channel noise on the bit level depends on the bit position and the neighboring bit values within the same symbol in the transmitted sequence. We observe a tradeoff between error-rate performance in the waterfall and error-floor regions, as illustrated by an extensive case study of a high-rate BITCM scheme. This tradeoff is typical in iterative decoding of turbo-like codes. The reported case study shows that it is possible to design bit interleavers with our proposed algorithm with equal or better performance in the waterfall region and superior performance in the error-floor region, compared with randomly generated bit interleavers. In particular, we were able to design BITCM schemes with maximum-likelihood decoding frame-error rates of 10-12 and 10 -17 at 2.6 and 3.8 dB away from unconstrained channel capacity, at spectral efficiencies of 3.10 and 6.20 b/s/Hz using square 16 and 256-quadrature amplitude modulation signal constellations, respectively

## An Efficient Code Structure of Block Coded Modulations with Iterative Viterbi Decoding Algorithm

- **Status**: ❌
- **Reason**: Block coded modulation + 반복 Viterbi 디코딩, 비-LDPC 부호이며 이식 가능한 BP 기법 없음
- **ID**: ieee:4362391
- **Type**: conference
- **Published**: 6-8 Sept. 
- **Authors**: Huan-Bang Li, Ryuji Kohno
- **PDF**: https://ieeexplore.ieee.org/document/4362391
- **Abstract**: Block coded modulations (BCM) with iterative Viterbi decoding algorithm can provide both high transmission throughput and small error probability. In this paper, a new code structure is proposed to further improve the performance. The strategy of the new code is to add parity check codes at corresponding coding levels of BCM to increase the Hamming distances among codewords. Decoding trellis of Viterbi decoding to support the new code structure is also developed. It is shown that the proposed code structure can not only guarantee the Euclidean distance of BCM but also mitigate the burden of iterative decoding. As a result, the proposed code structure can provide better transmission rates than the old one with identical or less decoding complexity. Computer simulation shows that the proposed code structure is also beyond the old one in bit error rate performance.

## A new LDPC-STB coded MC-CDMA systems with SOVA-based decoding and soft-interference cancellation

- **Status**: ❌
- **Reason**: LDPC-STB MC-CDMA의 SOVA 간섭제거 수신기, 무선 응용 특이적·LDPC는 부수 언급
- **ID**: ieee:7071256
- **Type**: conference
- **Published**: 4-8 Sept. 
- **Authors**: Luis Alberto Paredes Hernández, Mariano García Otero
- **PDF**: https://ieeexplore.ieee.org/document/7071256
- **Abstract**: This paper analyzes several interference cancellation scheme applied to LDPC-STB coded MC-CDMA systems. In these systems, a linear MMSE detector is conventionally used to reduce interference generated by multipath, multiuser, and multiple antennas propagation. To obtain further performance improvements, a more efficient SOVA-based iterative MMSE scheme is considered. This receiver performs soft-interference cancellation for every user based on a combination of the MMSE criterion and the turbo processing principle. It is shown that these block space-time schemes, concatenated with LDPC detectors can potentially provide significant capacity enhancements over the conventional matched filter receiver1.

## A turbo receiver for wireless MC-CDMA communications using pilot-aided Kalman filter-based channel tracking and MAP-EM demodulator with LDPC codes

- **Status**: ❌
- **Reason**: MC-CDMA turbo 수신기(Kalman 채널추적+MAP-EM), 무선 응용 특이적·LDPC 베이스라인
- **ID**: ieee:7071413
- **Type**: conference
- **Published**: 4-8 Sept. 
- **Authors**: T. M. Law, S. C. Chan
- **PDF**: https://ieeexplore.ieee.org/document/7071413
- **Abstract**: This paper presents a turbo receiver for wireless multi-carrier code division multiple access (MC-CDMA) communications using pilot-aided Kalman filter-based channel tracking and maximum a posteriori expectation-maximization (MAP-EM) demodulator with a soft low-density parity-check (LDPC) decoder. The pilot-aided Kalman filter considerably simplifies the tracking of the time-varying channel, which helps to improve the performance of the MAP-EM demodulator and LDPC decoder in fast fading channels. Simulation results show that the proposed system gives a better bit-error-rate (BER) performance than the conventional turbo receiver, at the expense of slightly lower data rate due to use of pilot symbols. It therefore provides a useful alternative to conventional approaches with a different tradeoff between BER performance, implementation complexity, and transmission bandwidth.

## Joint data hiding-source coding of still images

- **Status**: ❌
- **Reason**: 데이터하이딩-소스코딩 결합(정지영상), LDPC coset 소스코딩으로 채널 ECC 아님
- **ID**: ieee:7071642
- **Type**: conference
- **Published**: 4-8 Sept. 
- **Authors**: Çagatay Dikici, Khalid Idrissi, Atilla Baskurt
- **PDF**: https://ieeexplore.ieee.org/document/7071642
- **Abstract**: There exists a strong duality between Source Coding with side information (known as Distributed Source Coding) and Channel Coding with Side Information (informed data-hiding). Inspired by the system in [1], which is a combination of Data Hiding and Distributed Source Coding scheme, we have extended this system to 2D natural images. Hence a cascade of informed data hiding for a still image is followed by a distributed source coding with a fidelity criterion, given that a noisy version of the input image is available only at the decoder. We used baseline JPEG compression with different quality values for creation of the Side Information, a memoryless quantization for informed data hiding, and LDPC based coset construction for source coding. The preliminary experimental results are given using the theoretical findings of the duality problem.

## Near-lossless distributed coding of hyperspectral images using a statistical model for probability estimation

- **Status**: ❌
- **Reason**: 분산소스코딩(하이퍼스펙트럴 압축), 채널 ECC 아닌 소스코딩 → 제외
- **ID**: ieee:7071292
- **Type**: conference
- **Published**: 4-8 Sept. 
- **Authors**: Marco Grangetto, Enrico Magli, Gabriella Olmo
- **PDF**: https://ieeexplore.ieee.org/document/7071292
- **Abstract**: In this paper we propose an algorithm for near-lossless compression of hyper spectral images based on distributed source coding (DSC). The encoding is based on syndrome coding of bit-planes of the quantized prediction error of each band, using the same information in the previous band as side information. The practical scheme employs an array of low-density parity-check codes. Unlike other existing DSC techniques, the determination of the encoding rate for each data block is completely based on a statistical model, avoiding the need of inter-source communication, as well as of a feedback channel. Moreover, the statistical model allows to estimate the statistics of the currently decoded bit-plane also using the information about the previously decoded ones in the same band; this boosts the performance of the DSC scheme towards the capacity of the conditional entropy of the multilevel (as opposed to binary) source. Experimental results have been worked out using AVIRIS data; a significant performance improvement is obtained with respect to existing DSC and classical techniques, although there is still a gap with respect to the theoretical coding bounds.

## Soft-output detection of differentially encoded M-PSK over channels with phase noise

- **Status**: ❌
- **Reason**: 차동 M-PSK MAP 검출(위상잡음), forward-backward 위상추정기로 LDPC 무관·떼어낼 BP 기법 없음
- **ID**: ieee:7071241
- **Type**: conference
- **Published**: 4-8 Sept. 
- **Authors**: Alan Barbieri, Giulio Colavolpe
- **PDF**: https://ieeexplore.ieee.org/document/7071241
- **Abstract**: We consider a differentially encoded M-PSK signal transmitted over a channel affected by phase noise. For this problem, we derive the exact maximum a posteriori (MAP) symbol detection algorithm. By analyzing its properties, we demonstrate that it can be implemented by a forward-backward estimator of the phase probability density function, followed by a symbol-by-symbol completion to produce the a posteriori probabilities of the information symbols. To practically implement the forward-backward phase estimator, we propose a couple of schemes with different complexity. The resulting algorithms exhibit an excellent performance and, in one case, only a slight complexity increase with respect to the algorithm which perfectly knows the channel phase. The application of the proposed algorithms to repeat and accumulate codes is assessed in the numerical results.

## Low-Complexity Joint Channel Estimation and LDPC Decoding for Block Fading Channel

- **Status**: ❌
- **Reason**: 블록페이딩 결합 채널추정+표준 normalized min-sum 사용, 무선 응용 특이적이고 신규 디코더 기여 없음
- **ID**: ieee:4023106
- **Type**: conference
- **Published**: 31 Aug.-1 
- **Authors**: Zhichu Lin, Zhixing Yang, Changyong Pan
- **PDF**: https://ieeexplore.ieee.org/document/4023106
- **Abstract**: This paper presents a low-complexity iterative joint channel estimation and LDPC decoding algorithm for block-fading channel. Normalized min-sum algorithm, which has a much lower complexity than sum-product algorithm, is used as LDPC decoding algorithm. By choosing an optimal normalization factor, the performance of our algorithm can be as good as its counterpart using sum-product algorithm, and only 0.3-0.5 dB away from the case where perfect CSI is known

## Low Power Digital Communication in Implantable Devices Using Volume Conduction of Biological Tissues

- **Status**: ❌
- **Reason**: 체내 이식기기 통신·채널코딩 변조 응용. 떼어낼 LDPC 디코더/HW/코드설계 기법 없음
- **ID**: ieee:4463237
- **Type**: conference
- **Published**: 30 Aug.-3 
- **Authors**: Ning Yao, Heung-No Lee, R.J. Sclabassi +1
- **PDF**: https://ieeexplore.ieee.org/document/4463237
- **Abstract**: This work investigates the data communication problem of implantable devices using fundamental theories in communications. We utilize the volume conduction property of biological tissues to establish a digital communications link. Data obtained through animal experiments are used to analyze the time and frequency response of the volume conduction channel as well as to characterize the biological signals and noises present in the system. A low power bandwidth efficient channel-coded modulation scheme is proposed to conserve battery power and reduce the health risks associated

## Image Transmission in LDPC Coded Mobile Satellite Communication Systems

- **Status**: ❌
- **Reason**: 위성 이미지전송 UEP 응용, PEG 기반 불규칙 LDPC를 표준대로 사용 — 새 코드설계 기여 없음
- **ID**: ieee:1692024
- **Type**: conference
- **Published**: 30 Aug.-1 
- **Authors**: Yuling Zhang, Dongfeng Yuan
- **PDF**: https://ieeexplore.ieee.org/document/1692024
- **Abstract**: This paper investigates the performance of image transmission with unequal error protection (UEP) through typical satellite communication channel, and the UEP is achieved by mapping different bits of the image bytes to different positions of a progressive edge growth (PEG) constructed irregular Low-Density Parity-Check (LDPC) codes. The satellite communication channel consists of two main fading: one is the nonlinearity caused by on-board high power amplifier (HPA), and another is the time-varying fading caused by the propagation channel, a neural network (NN) based predistortion technique is adopted to deal with the nonlinearity.

## Efficient Wavelet Zero-Tree Video Coding Based on Wyner-Ziv Coding and Lattice Vector Quantization

- **Status**: ❌
- **Reason**: Wyner-Ziv/Slepian-Wolf 소스코딩에 LDPC를 엔트로피코딩 대체로 사용 — 채널 ECC 아님
- **ID**: ieee:1691973
- **Type**: conference
- **Published**: 30 Aug.-1 
- **Authors**: Anhong Wang, Yao Zhao, Jing Li
- **PDF**: https://ieeexplore.ieee.org/document/1691973
- **Abstract**: In this paper, we present a new wavelet zero-tree video coding method based on lattice vector quantization (LVQ) and Wyner-Ziv coding. It uses dependences only at decoder and develops a new intra-encoding and inter-decoding framework. In this framework, the conventional entropy coding is replaced by a low-density parity-check (LDPC) Slepian-Wolf codec and the idea of Slepian-Wolf coding is used to set partitioning in hierarchical trees (SPIHT) and lattice vector quantization completely. Experiment results suggest that our scheme can get higher PSNR and better recovered video than intraframe SPIHT and scalar Slepian-Wolf SPIHT.

## Performance Comparisons of Different Channel Codes in Distributed Video Coding

- **Status**: ❌
- **Reason**: 분산비디오코딩에서 turbo vs LDPC 성능비교(소스코딩 응용), 떼어낼 신규 ECC 기법 없음
- **ID**: ieee:1691968
- **Type**: conference
- **Published**: 30 Aug.-1 
- **Authors**: Hao Wang, Yao Zhao, Anhong Wang
- **PDF**: https://ieeexplore.ieee.org/document/1691968
- **Abstract**: This paper introduces advanced channel codes turbo and LDPC to distributed video coding (DVC), and compares their performance in the whole system. From the simulation results, we can find that the LDPC codes are superior to turbo codes when the video sequence has high motion. Additionally, whether turbo or LDPC, the DVC system outperforms the conventional intra-frame coding though underperforms conventional motion-compensated inter-frame coding. But DVC has the advantage of easy encoding which can meet the demands of friendly up-linking media communication

## Progressive Network Coding for Message-Forwarding in Ad-Hoc Wireless Networks

- **Status**: ❌
- **Reason**: 무선 ad-hoc 네트워크 코딩/협력 전송, LDPC ECC 기법 없음 — 무선 응용 특이
- **ID**: ieee:4068123
- **Type**: conference
- **Published**: 28-28 Sept
- **Authors**: Xingkai Bao, Jing Li
- **PDF**: https://ieeexplore.ieee.org/document/4068123
- **Abstract**: We consider multi-hop transmission from the source to the destination in ad-hoc wireless networks. Cooperative forwarding approaches in the framework of progressive network coding are proposed which generalize coded cooperation in a multi-hop context. In this framework, the source node and each succeeding relay node progressively decode what they receive from the previous stages and re-encode the messages to different parts of the parity bits from a single (network) codeword hop by hop. The maximal achievable rates for the multi-hop wireless networks using traditional repetition-forward and progressive network coding are analyzed with respect to different transmit power constraint and packet length allocation. The optimal number of relays are derived in each scheme. It is found that progressive network coding with adaptive packet length significantly increases the system throughput and improves the energy efficiency

## Performance Analysis of LDPC Code with Spatial Diversity

- **Status**: ❌
- **Reason**: SIMO 공간다이버시티용 irregular LDPC 최적 차수분포 임계값 분석, 채널/시스템 특이적 최적화로 NAND 이식 불가
- **ID**: ieee:4109664
- **Type**: conference
- **Published**: 25-28 Sept
- **Authors**: Satoshi Gounai, Tomoaki Ohtsuki
- **PDF**: https://ieeexplore.ieee.org/document/4109664
- **Abstract**: In mobile communications, the quality of signal is deteriorated by fading. The spatial diversity technique is used to reduce the degradation of the signal by fading. There are several techniques to realize the spatial diversity gain, such as Single- Input Multiple-Output (SIMO), Space-Time Block Code (STBC), and so on. The SIMO system realizes the receive diversity. The error correcting code can be combined with spatial diversity gain. Low-Density Parity Check (LDPC) codes can achieve good performance approaching Shannon limit. In particular, an irregular LDPC code with optimum degree distribution achieves better performance than a regular LDPC code. The optimum degree distribution of the irregular LDPC code depends both on the channel and the system. In this paper, we derive the Eb/No thresholds of a regular LDPC codes and the irregular LDPC codes for SIMO systems with several diversity orders. The Eb/No threshold is the smallest Eb/No that the decoder can achieve the error free. We also derive the optimum degree distributions of the irregular LDPC codes for SIMO systems with several diversity orders. We show that with low diversity order, the optimum degree distributions of the irregular LDPC code depends on the diversity order largely, while with high diversity order, the optimum degree distribution depends both on the diversity order and the combining scheme largely. We also show that comparing the optimum degree distributions for MRC and STBC, when the diversity orders are the same, the optimum degree distributions are also the same.

## Block-LDPC Codes vs Duo-Binary Turbo-Codes for European Next Generation Wireless Systems

- **Status**: ❌
- **Reason**: Block-LDPC vs duo-binary turbo 복잡도/처리량 비교 평가, 신규 디코더/구성/HW 기여 없음
- **ID**: ieee:4109550
- **Type**: conference
- **Published**: 25-28 Sept
- **Authors**: Thierry Lestable, Ernesto Zimmerman, Marie-helene Hamon +1
- **PDF**: https://ieeexplore.ieee.org/document/4109550
- **Abstract**: In this paper, we investigate the performance-complexity trade-off for two leading-edge channel coding techniques, namely duo-binary turbo-codes (DBTC) and block LDPC codes (BLDPCC). We assess their respective decoding complexity in terms power consumption and cycle delays, as a function of both the code rate and packet length, to derive a domain of suitability for both techniques. We also compare their capabilities to serve as mother codes for rate-compatible punctured codes (RCPC) and finally analyze their achievable throughput, as a function of the degree of parallelism.

## LDPC Coded Iterative Signal Detection Based on QRD-M with CRC Check

- **Status**: ❌
- **Reason**: MIMO QRD-M 신호검출에 LDPC 적용(검출기 결합 무선 특이적), 떼어낼 LDPC 디코더 기법 없음
- **ID**: ieee:4109379
- **Type**: conference
- **Published**: 25-28 Sept
- **Authors**: Koichi Adachi, Masao Nakagawa
- **PDF**: https://ieeexplore.ieee.org/document/4109379
- **Abstract**: Maximum likelihood detection with QR decomposition and M-algorithm (QRD-M) is one of the detection methods in multiple-input multiple-output (MIMO) multiplexing. We recently proposed a Turbo coded iterative modified QRD-M with decision directed channel estimation and showed that the packet error rate (PER) performance close to the ideal channel estimation case can be obtained. In the iterative modified QRD-M, signal ranking is performed based on both received signal-to- interference plus noise power ratio (SINR) and results of cyclic redundancy check (CRC) decoding and then, signal detection is performed by modified M-algorithm based on the results of CRC decoding. In this paper, we apply irregular low density parity check (irregular LDPC) codes to the previously proposed iterative modified QRD-M. The a posteriori probability of each bit (including parity bit) is necessary for decision directed channel estimation and modified M-algorithm in the iterative modified QRD-M. Unlike Turbo decoding, the a posteriori probability of each bit can be obtained in LDPC decoding. Thus, by using LDPC codes, more accurate signal detection is possible than using Turbo codes. To achieve more powerful detection of decoding errors, CRC codes can be jointly used with parity check equation of LDPC codes. It is shown by the computer simulation that the performance of the LDPC coded iterative modified QRD-M is superior to that of the Turbo coded iterative modified QRD-M.

## Joint Design of Twin-Antenna Assisted Space-Time Multilevel Sphere Packing Aided Coded Modulation

- **Status**: ❌
- **Reason**: multilevel coding + sphere packing/STBC, 비-LDPC 무선 변조 기법
- **ID**: ieee:4109344
- **Type**: conference
- **Published**: 25-28 Sept
- **Authors**: R. Y. S. Tee, O. Alamri, L. Hanzo
- **PDF**: https://ieeexplore.ieee.org/document/4109344
- **Abstract**: A new multilevel coding (MLC) scheme invoking sphere packing (SP) modulation is proposed, where the SP arrangement is jointly designed with a space time block code (STBC) for the sake of attaining an additional space diversity gain. An iterative multistage decoding (MSD) aided multilevel sphere packing demodulator is proposed for attaining a high decoding performance at a low decoding complexity, when communicating over a correlated Rayleigh channel. The appropriate design of a 4-dimensional (4D) sphere packing bit-to-SP-symbol mapping scheme and the beneficial choice of the individual coding rates of the MLC scheme allows us to provide an unequal error protection capability, which is often required for efficient audio or video transmissions.

## BER Transfer Chart Analysis of Turbo Frequency Domain Equalization

- **Status**: ❌
- **Reason**: Turbo frequency domain equalizer BER transfer chart analysis; non-LDPC equalization, no transferable binary LDPC decoder/code/HW technique
- **ID**: ieee:4109686
- **Type**: conference
- **Published**: 25-28 Sept
- **Authors**: Maryam Sabbaghian, David Falconer, Hamid Saeedi
- **PDF**: https://ieeexplore.ieee.org/document/4109686
- **Abstract**: In this paper we analyze the performance of a turbo frequency domain equalizer using the BER transfer chart. This tool evaluates the signal to noise ratio improvement at the decoder input during iterations. We derive a formula for the variance of the equalizer output at each iteration as a function of the error probability of the previous iteration. By defining an equivalent SNR based on the equalizer output mean and variance, and knowing the decoder bit error rate curve, we are able to evaluate the bit error rate of the decoder output in each iteration. Compared to the initially proposed BER transfer charts, this method gives us a more accurate curve for the equalizer and follows the dynamic of the process. Simulation results show that this method can predict the performance of the system with reasonable accuracy.

## A Turbo Receiver for Wireless Mc-Cdma Communications Using Map-Em Demodulator with Ldpc Codes under Narrowband Interference

- **Status**: ❌
- **Reason**: MC-CDMA 무선 수신기·다중사용자 검출·채널추정 중심, LDPC는 부수 언급, 떼어낼 ECC 기법 없음
- **ID**: ieee:4041038
- **Type**: conference
- **Published**: 24-27 Sept
- **Authors**: T. M. Law, S. C. Chan, Z. G. Zhang
- **PDF**: https://ieeexplore.ieee.org/document/4041038
- **Abstract**: This paper presents a turbo receiver for wireless multicarrier code division multiple access (MC-CDMA) communication systems using maximum a posteriori expectation-maximization (MAP-EM) demodulator with a soft low-density parity-check (LDPC) decoder with pilot-aided robust channel tracking and multiuser detection under time-varying narrowband interference (NBI). It was found that the conventional least-squares (LS) channel estimators and multiuser detectors will be significantly degraded when some sub-carrier are contaminated by narrowband interfering signals. A new weighted least M-estimate (WLM) multiuser detector, which is based on the M-estimation and weighted least square (WLS) concept, is proposed to jointly suppress the multiple access interference (MAI) and time-varying NBI. To reliably estimate the channel in NBI, a weighted recursive least M-estimate (WRLM) channel estimator is also employed to estimate the time-varying frequency-selective fading channels. Simulation results show that the proposed WLM multiuser detector significantly outperforms over the conventional linear decorrelator under NBI

## A Real Time Programmable Encoder for Low Density Parity Check Code as specified in the IEEE P802.16E/D7 Standard and its Efficient Implementation on a DSP Processor

- **Status**: ❌
- **Reason**: 표준(802.16e) LDPC 인코더 DSP 구현, 디코더·신규 코드설계 기여 아닌 표준 인코더 최적화
- **ID**: ieee:4063003
- **Type**: conference
- **Published**: 24-27 Sept
- **Authors**: Zahid Khan, Tughrul Arslan, Scott MacDougall
- **PDF**: https://ieeexplore.ieee.org/document/4063003
- **Abstract**: This paper presents a real time programmable irregular low density parity check (LDPC) Encoder as specified in the IEEE P802.16E/D7 standard. The encoder is programmable for frame sizes from 576 to 2304 and for five different code rates. H matrix is efficiently generated and stored for a particular frame size and code rate. The encoder is implemented on SC140 Processor and different optimization techniques are applied to enhance the throughput. With SC140, a reduction of 2.6 times in the number of effective MAC operations has been achieved, with further reduction in cycle counts possible. A pipelined architecture is also presented for possible ASIC or FPGA implementation.

## Performance Evaluation of a Novel Low-Density Parity-Check Coded Ultra Wide Band Impulse Radio (UWB-IR) System

- **Status**: ❌
- **Reason**: LDPC를 UWB-IR 무선 시스템에 적용한 응용 논문, 떼어낼 신규 디코더/구성/HW 기법 없음
- **ID**: ieee:4149289
- **Type**: conference
- **Published**: 22-24 Sept
- **Authors**: Fangni Chen, Shiju Li, Lei Shen
- **PDF**: https://ieeexplore.ieee.org/document/4149289
- **Abstract**: As a new spread spectrum system, an ultra wide band technology has attracted much attention in high speed indoor multiple access radio communications. The conventional UWB system repeats and transmits pulses for each bit, but repeat code can't get code gains. As an error correcting code, low-density parity-check code (LDPC) has attracted much attention because of its good bit error performance. In this paper, we propose a novel LDPC coded direct-sequence ultra wide band (DS-UWB) system. Furthermore, we give the computer simulation and our results show that the LDPC coded UWB system can improve the BER over AWGN channel and IEEE 802.15.3a recommended UWB multi-path faded channel

## An Improved Degree Distribution Based HARQ for LDPC

- **Status**: ❌
- **Reason**: irregular LDPC용 HARQ 재전송 노드 선택 개선, 시스템 레벨 기법으로 NAND ECC에 이식할 디코더/구성 기여 없음
- **ID**: ieee:4149311
- **Type**: conference
- **Published**: 22-24 Sept
- **Authors**: Xuehua Li, Yiqing Cao, Dacheng Yang
- **PDF**: https://ieeexplore.ieee.org/document/4149311
- **Abstract**: An improved hybrid ARQ (HARQ) scheme for irregular LDPC codes based on degree distributions is introduced in this paper. In traditional degree distribution based HARQ (DDB-HARQ), the source selectively retransmits the nodes with large degrees and this scheme brings a significant gain to the irregular LDPC coded system. However, the selecting method of the traditional scheme is thought to be not accurate enough. In this paper, an improved method in which the source retransmits the nodes in different degrees at specific proportions each time has been proposed. According to the analysis with Gaussian approximation (GA) the improved scheme could be more efficient since the retransmission proportions are more accurate which has also been proved by the simulation results

## Simplified Iterative Symbol Timing and Carrier Phase Recovery Scheme for LDPC-Coded Systems

- **Status**: ❌
- **Reason**: 심볼 타이밍/반송파 위상 동기화 기법, LDPC는 응용 베이스라인일 뿐 떼어낼 ECC 기법 없음
- **ID**: ieee:4149315
- **Type**: conference
- **Published**: 22-24 Sept
- **Authors**: Liu An, Luo Wu
- **PDF**: https://ieeexplore.ieee.org/document/4149315
- **Abstract**: A simplified ML-based iterative synchronization scheme is proposed in this paper for LPDC-coded systems. Symbol timing and carrier phase are estimated in a simple way based on the maximum likelihood theory aided by hard decision obtained from LDPC decoder. The synchronized samples input to the decoder are updated when a new iterative estimation for symbol timing and carrier phase is completed. The synchronized samples are reconstructed by quadratic interpolation which is very simple and can be implemented in parallel. This approach is applied to a LDPC-coded QPSK system over AWGN channel. Simulation results demonstrate that the performance of the proposed scheme approaches that with the ideal synchronization

## A Joint Timing Recovery and SNR Estimation Algorithm for LDPC-Coded Systems

- **Status**: ❌
- **Reason**: 타이밍 복구/SNR 추정 동기화 알고리즘, LDPC 디코더 자체 개선 아님
- **ID**: ieee:4149321
- **Type**: conference
- **Published**: 22-24 Sept
- **Authors**: Pan Xiao-Fei, Hao Xie-Dong
- **PDF**: https://ieeexplore.ieee.org/document/4149321
- **Abstract**: The effects of both symbol synchronization error and SNR estimation on the LDPC decoding performance have been investigated. Based on the statistical properties of the LDPC decoding output value, a joint timing recovery and SNR estimation algorithm is given, which puts the symbol synchronization, SNR estimation and iterative decoding together by two cooperative loops. After several iterative steps, the estimated values of symbol synchronization error and SNR convergent rapidly, and little performance degradation has been observed than the system with foregone SNR and accurate symbol timing

## A New Method for Detection of LDPC Coded GMSK Modulated Signals

- **Status**: ❌
- **Reason**: GMSK/CPM 복조 검출 기법, LDPC는 부수, 떼어낼 ECC 코드/디코더 기여 없음
- **ID**: ieee:4149318
- **Type**: conference
- **Published**: 22-24 Sept
- **Authors**: Mehrdad Taki, Mohammad B. Nezafati
- **PDF**: https://ieeexplore.ieee.org/document/4149318
- **Abstract**: In this paper a new method for detection of LDPC coded, GMSK modulated signals will be proposed. Detection technique is based on Laurent decomposition of CPM signal into PAM pulses. At the receiver, the signal is passed through a filter matched to a PAM pulse with highest energy. Thereafter to eliminate effect of other pulses, a linear equalizer and a turbo like equalizer combined with LDPC decoder will be used. The performance of designed receiver is shown that is very close to optimum maximum likelihood receiver but its complexity is much smaller

## Joint Design for LDPC Coded OFDM with Transmit Adaptive Antenna

- **Status**: ❌
- **Reason**: LDPC-coded OFDM + 적응안테나 결합 설계(UEP 매핑) — OFDM/무선 응용 특이, 표준 구조화 LDPC 사용, 떼어낼 신규 ECC 기법 없음
- **ID**: ieee:4149255
- **Type**: conference
- **Published**: 22-24 Sept
- **Authors**: Xiumei Yang, Xiaomei Xia, Yong Xiong
- **PDF**: https://ieeexplore.ieee.org/document/4149255
- **Abstract**: A novel design is proposed for the OFDM system using structured LDPC codes with the transmit adaptive antennas (TxAA), which can achieve improved performance by adaptively using the feedback subcarrier frequency information at the transmit side. With the aid of the closed multiple antenna technique, much gain can be achieved in the coded OFDM system. Furthermore, irregular LDPC codes have the advantage of unequal error protection (UEP) for coded bits with different degree distributions. Thus mapping the coded bits with high degrees to the subcarriers with weak subchannel attenuation is proposed to fully utilize the feedback information not only in the design of the closed-loop OFDM transmission but also in the combination design of the coding scheme and OFDM modulation. The proposed scheme is proven to be effective by simulation results in the frequency selective channel scenario

## Maximum Likelihood Decoding of Low Density Parity Check Coded Subcarrier Modulation in Optical Wireless Systems

- **Status**: ❌
- **Reason**: 광무선 LDPC ML 디코딩 BER 상한 — 광채널 응용 이론 bound, 표준 LDPC 사용, 떼어낼 디코더/구성 기법 없음
- **ID**: ieee:4086233
- **Type**: conference
- **Published**: 15-17 Sept
- **Authors**: Manish Sharma, D. Chadha
- **PDF**: https://ieeexplore.ieee.org/document/4086233
- **Abstract**: We propose low density parity check (LDPC) coded optical wireless communication systems with multiple subcarrier modulation (BPSK and QPSK). Upper bounds on the bit-error rate (BER) for maximum likelihood (ML) decoding of LDPC coded systems have been obtained on atmospheric optical channels where the effects of the scintillation exist. We also show that LDPC coded atmospheric optical systems have better BER than turbo coded atmospheric optical systems

## Reliability Analysis for On-chip Networks under RC Interconnect Delay Variation

- **Status**: ❌
- **Reason**: NoC 인터커넥트 신뢰성/고장허용 분석 — LDPC ECC 무관
- **ID**: ieee:4152821
- **Type**: conference
- **Published**: 14-16 Sept
- **Authors**: Mosin Mondal, Xiang Wu, Adnan Aziz +1
- **PDF**: https://ieeexplore.ieee.org/document/4152821
- **Abstract**: Future integrated circuits are characterized by their high defect rates thereby necessitating certain degree of redundancy. In a typical network-on-chip (NoC), multiple paths exist between a source and a sink to provide the required level of fault tolerance. Consequently, a manufacturing fault on a single interconnect does not necessarily render the resulting integrated circuit useless. In this paper we quantify the fault tolerance offered by an NoC. Specifically, we (1) provide a model for determining the probability that an NoC link fails due to manufacturing variation, and (2) measure the impact of link failure on the number of cycles taken by the NoC to implement communication

## Throughput of WLAN Systems with LDPC Codes and Adaptive Bit Loading

- **Status**: ❌
- **Reason**: WLAN 802.11a 처리량 연구로 LDPC는 기존 코드 선택만, 떼어낼 신규 디코더/구성/HW 기여 없음
- **ID**: ieee:4022594
- **Type**: conference
- **Published**: 11-14 Sept
- **Authors**: Andrey Belogolovy, Mikhail Yu. Lyakh, Oleg Semenov +1
- **PDF**: https://ieeexplore.ieee.org/document/4022594
- **Abstract**: Advanced forward error correcting (FEC) and modulation scheme basing on low-density parity-check codes (LDPC) and adaptive bit loading (ABL) procedure is investigated for WLAN physical layer (PHY) of IEEE 802.11a standard. The main intention of the present paper is to study influence of the advanced PHY algorithms on the WLAN throughput under the realistic deployment conditions, for which a hardware-friendly simulation model was developed. Also, we present approaches for selection of the most suitable LDPC codes and ABL algorithms. Simulation results show performance gains of the both techniques and illustrate sensitivity of them to the deployment conditions such as channel stability, channel profile measurement precision, etc

## A-Performance-Improved-Iterative-Channel-Code-Decoder-For-High-Order-Modulation-Signals-

- **Status**: ❌
- **Reason**: 고차변조 LLR 반복 갱신 기법으로 turbo/LDPC 공용이나 변조 의존적이며 NAND ECC LLR 생성에 이식할 부호 독립 기법 아님(무선 응용 특이)
- **ID**: ieee:4022600
- **Type**: conference
- **Published**: 11-14 Sept
- **Authors**: Xiaoyong Yu
- **PDF**: https://ieeexplore.ieee.org/document/4022600
- **Abstract**: A method of log-likelihood ratio (LLR) generation for input to channel code decoder is presented in this paper. It will be demonstrated that, in a communication system where iterative channel decoding, namely turbo and low density parity check (LDPC) codes, and high order modulations, such as 8PSK, 16QAM and 64QAM, are used, the input to channel code decoder can be iteratively updated by using intermediate results of the decoder for better performance. This technique is applicable to 3G wireless systems, for example 3GPP and 3GPP2, and WiMax (IEEE 802.16)

## A Cluster-Based MC-CDMA System for Up-Link Transmission

- **Status**: ❌
- **Reason**: MC-CDMA 다중접속+GF 확장체 LDPC joint decoding으로 비이진 LDPC이며 무선 응용 특이
- **ID**: ieee:4022691
- **Type**: conference
- **Published**: 11-14 Sept
- **Authors**: A. Goupil, M. Colas, G. Gelle
- **PDF**: https://ieeexplore.ieee.org/document/4022691
- **Abstract**: A new scheme of detection for multiple access channel is investigated, which consists in the combining of PIC-like detection and joint decoding of LDPC codes. The joint decoding is first studied through the use of LDPC codes over Galois extensions of binary field for the AWGN multiple access channel. Then, a hierarchical MC-CDMA system which uses both parallel interference canceler and joint detection is implemented and simulations show that it can provide a substantial improvement without any complexity growth of the emitter in a MC-CDMA like up-link framework

## Transmit Diversity Schemes for MIMO-OFDM Based Wireless Lan Systems

- **Status**: ❌
- **Reason**: MIMO-OFDM 송신 다이버시티 비교로 LDPC는 부수 베이스라인, 떼어낼 ECC 기법 없음
- **ID**: ieee:4022703
- **Type**: conference
- **Published**: 11-14 Sept
- **Authors**: Wu Yan, Sumei Sun, Yuan Li +1
- **PDF**: https://ieeexplore.ieee.org/document/4022703
- **Abstract**: In this paper, we study the performance of two transmit diversity schemes, the cyclic delay diversity (CDD) and the groupwise space time block code (G-STBC), for high throughput wireless local area network (LAN) system using orthogonal frequency division multiplexing (OFDM) and multiple input multiple output (MIMO) technologies. We compare the performance of CDD and the G-STBC transmission with the VBLAST transmission using both convolutional code (CC) and low density parity check (LDPC) code. We show that G-STBC provides the best performance in all the three transmission schemes. The performance of CDD depends both on the frequency diversity of the channel and the power of coding. CDD has better performance advantage for systems with smaller multi-path and with powerful coding schemes. CDD also has the advantage of being receiver transparent

## Iterative FDE for DD-Based Cooperative Relaying with FD-STBC in Quasi-Synchronous Networks

- **Status**: ❌
- **Reason**: 협력 릴레이 반복 FDE, LDPC 기법 없음
- **ID**: ieee:4022349
- **Type**: conference
- **Published**: 11-14 Sept
- **Authors**: Toshiaki Koike, Hidekazu Murata, Susumu Yoshida
- **PDF**: https://ieeexplore.ieee.org/document/4022349
- **Abstract**: A cooperative diversity requires accurate synchronization for relaying in multihop communications. This paper presents an iterative equalizer for multihop networks with delay diversity, which is tolerant to asynchronous relaying. We introduce frequency-domain space-time coding suited for the equalizer. In addition, we employ cooperative spatial multiplexing to improve the system throughput. We demonstrate that cooperative diversity and multiplexing can offer high spectrum-efficiency even in frequency-selective and poor-scattering channels

## Improving HomePlug Power Line Communications with LDPC Coded OFDM

- **Status**: ❌
- **Reason**: PLC OFDM에 LDPC 적용 성능 비교로 표준 LDPC 사용, 떼어낼 신규 디코더/구성/HW 기여 없음
- **ID**: ieee:4018161
- **Type**: conference
- **Published**: 10-14 Sept
- **Authors**: Christine Hsu, Neng Wang, Wai-yip Chan +1
- **PDF**: https://ieeexplore.ieee.org/document/4018161
- **Abstract**: Power line communications (PLC) has received much attention due to the wide connectivity and availability of power lines. Effective PLC must overcome the harsh and noisy environments inherent in PLC channels. HomePlug 1.0 is the current PLC standard in North America. The physical layer of HomePlug 1.0 employs orthogonal frequency division multiplexing (OFDM) as well as concatenated Reed-Solomon and convolutional coding. Aiming to obtain higher PLC throughput, we investigate the performance of OFDM with low-density parity-check (LDPC) codes and compare the proposed scheme with HomePlug 1.0 ROBO mode. In our simulations, the PLC channel is modeled by multipath fading, with Middleton's Class A noise (AWCN) model simulating the worst-case impulsive noise. We apply clipping to lessen the impact of impulsive noise. A simple but effective method is devised to estimate the variance of the clipped noise for LDPC decoding. In comparison with ROBO mode, the proposed scheme offers improved performance and lower computational complexity per decoded bit. Our scheme provides increased throughput by dispensing with ROBO mode's repetitive transmission of information to gain time diversity

## Nonlinear Soft-Output Signal Detector Design and Implementation for MIMO Communication Systems with High Spectral Efficiency

- **Status**: ❌
- **Reason**: MIMO 비선형 soft-output 신호검출기 VLSI 구현; LDPC 부호/디코더 기법 아님, 떼어낼 ECC 기법 없음
- **ID**: ieee:4114969
- **Type**: conference
- **Published**: 10-13 Sept
- **Authors**: Sizhong Chen, Fei Sun, Tong Zhang
- **PDF**: https://ieeexplore.ieee.org/document/4114969
- **Abstract**: VLSI implementations of nonlinear MIMO signal detectors are not trivial, particularly for systems with high spectral efficiency. For example, realization of such a detector for 4 times 4 MIMO with 64-QAM still remains missing in open literature. To tackle this challenge, we developed a nonlinear soft-output detector design solution, based on which a detector for up to 4 times 4 MIMO with 64-QAM has been designed using 0.13mum CMOS technology. Above 75 Mbps detection throughput has been verified based on post-layout results

## A Novel Application of LDPC-Based Decoder for WiMAX Dual-mode Inner Encoder

- **Status**: ❌
- **Reason**: WiMAX 통신 응용에 LDPC 디코더로 Viterbi 대체; 표준 LDPC 단순 적용, 신규 디코더/구성 기여 없음
- **ID**: ieee:4057467
- **Type**: conference
- **Published**: 10-12 Sept
- **Authors**: Li-hsieh Lin, Kuei-ann Wen
- **PDF**: https://ieeexplore.ieee.org/document/4057467
- **Abstract**: LDPC codes have recently received a lot of attention by their excellent error-correcting capability and have been adopted as an optional error correct coding scheme in WiMAX (802.16e) standard for mobility. In order to the low-complexity SOC (system-on-a-chip) design and multi-mode transmitter compatible, we proposed a novel application of LDPC decoder to substitute Viterbi decoder for convolutional encoder. The main character presented in this study is that the general two-decoder structure is replaced by one decoder. Our results indicate that the proposed scheme processes nice performance for mobile WiMAX system
