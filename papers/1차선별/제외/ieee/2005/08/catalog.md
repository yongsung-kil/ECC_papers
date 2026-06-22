# IEEE Xplore — 2005-08


## Successive refinement for the Wyner-Ziv problem and layered code design

- **Status**: ❌
- **Reason**: Wyner-Ziv 소스코딩(Slepian-Wolf) LDPC, 채널 ECC 아닌 소스코딩이며 떼어낼 신규 디코더/HW 없음
- **ID**: ieee:1468519
- **Type**: journal
- **Published**: Aug. 2005
- **Authors**: S. Cheng, Zixiang Xiong
- **PDF**: https://ieeexplore.ieee.org/document/1468519
- **Abstract**: We examine successive refinement for the Wyner-Ziv problem described in a recent paper by Steinberg and Merhav, where the authors showed that if the side information for all stages is identical, then the jointly Gaussian source with squared error distortion measure is successively refinable. We first extend this result to the case where the difference between the source and the side information is Gaussian and independent of the side information. As a byproduct, we give an alternative proof that the Wyner-Ziv problem for these sources has no rate loss-a result that was recently shown by Pradhan et al. through invoking the duality between the Gaussian Wyner-Ziv problem and the Costa problem. We then perform layered Wyner-Ziv code design for this general type of source based on nested scalar quantization, bit-plane coding, and low-density parity check (LDPC) code-based Slepian-Wolf coding (source coding with side information). We show that density evolution can be used to analyze the Slepian-Wolf code performance, provided that certain symmetry conditions, which have been dubbed dual symmetry, are satisfied by the hypothetical channel between the source and the side information. We also show that the dual symmetry condition is indeed satisfied by the hypothetical channel in our Slepian-Wolf coding setup. This justifies the use of density evolution in our LDPC code-based Slepian-Wolf code design for Wyner-Ziv coding. For the jointly Gaussian source, our layered coder performs 1.29 to 3.45 dB from the Wyner-Ziv bound for rates ranging from 0.47 to 4.68 bits per sample. When the side information is Laplacian and the source equals the side information plus an independent Gaussian noise term, our layered coder performs 1.33 to 3.90 dB from the Wyner-Ziv bound for rates ranging from 0.48 to 4.64 bits per sample.

## On channel estimation and equalization in TDS-OFDM based terrestrial HDTV broadcasting system

- **Status**: ❌
- **Reason**: TDS-OFDM 채널추정/등화, LDPC 무관 통신 응용
- **ID**: ieee:1510485
- **Type**: journal
- **Published**: Aug. 2005
- **Authors**: Bowei Song, Lin Gui, Yunfeng Guan +1
- **PDF**: https://ieeexplore.ieee.org/document/1510485
- **Abstract**: In TDS-OFDM (time-domain synchronous orthogonal frequency division multiplexing) systems, pseudonoise (PN) sequences rather than cyclic prefixes are inserted as guard interval, between consecutive inverse discrete Fourier transformed (IDFT) symbol blocks. Since the PN sequences can also be used as training symbols, such system can provide higher spectrum efficiency. However, due to non-cyclic property of the signal, the simple channel estimation and equalization techniques for conventional cyclic prefixed OFDM (CP-OFDM) can not be applied to TDS-OFDM. In this paper, we propose a channel estimation and equalization method for TDS-OFDM. Channel estimation depends on time domain correlation and iterative interference cancellation techniques, while equalization is based on tail cancellation and cyclic restoration algorithm (TCCR). It is shown that our proposed method can provide satisfactory performance in TDS-OFDM based terrestrial high-definition television (HDTV) broadcasting system.

## Area-efficient high-throughput MAP decoder architectures

- **Status**: ❌
- **Reason**: MAP/터보 디코더 HW 아키텍처(BIP), 터보 전용 재귀구조로 LDPC BP에 비이식적
- **ID**: ieee:1512180
- **Type**: journal
- **Published**: Aug. 2005
- **Authors**: Seok-Jun Lee, N.R. Shanbhag, A.C. Singer
- **PDF**: https://ieeexplore.ieee.org/document/1512180
- **Abstract**: Iterative decoders such as turbo decoders have become integral components of modern broadband communication systems because of their ability to provide substantial coding gains. A key computational kernel in iterative decoders is the maximum a posteriori probability (MAP) decoder. The MAP decoder is recursive and complex, which makes high-speed implementations extremely difficult to realize. In this paper, we present block-interleaved pipelining (BIP) as a new high-throughput technique for MAP decoders. An area-efficient symbol-based BIP MAP decoder architecture is proposed by combining BIP with the well-known look-ahead computation. These architectures are compared with conventional parallel architectures in terms of speed-up, memory and logic complexity, and area. Compared to the parallel architecture, the BIP architecture provides the same speed-up with a reduction in logic complexity by a factor of M, where M is the level of parallelism. The symbol-based architecture provides a speed-up in the range from 1 to 2 with a logic complexity that grows exponentially with M and a state metric storage requirement that is reduced by a factor of M as compared to a parallel architecture. The symbol-based BIP architecture provides speed-up in the range M to 2M with an exponentially higher logic complexity and a reduced memory complexity compared to a parallel architecture. These high-throughput architectures are synthesized in a 2.5-V 0.25-/spl mu/m CMOS standard cell library and post-layout simulations are conducted. For turbo decoder applications, we find that the BIP architecture provides a throughput gain of 1.96 at the cost of 63% area overhead. For turbo equalizer applications, the symbol-based BIP architecture enables us to achieve a throughput gain of 1.79 with an area savings of 25%.

## On error-correction coding for CDMA PON

- **Status**: ❌
- **Reason**: OCDMA PON용 FEC 표준 부호 소프트디코딩, 신규 LDPC 디코더/구성 기여 없음
- **ID**: ieee:1498937
- **Type**: journal
- **Published**: Aug. 2005
- **Authors**: H. Lundqvist, G. Karlsson
- **PDF**: https://ieeexplore.ieee.org/document/1498937
- **Abstract**: Optical-code-division multiple access (OCDMA) has been investigated as a multiple-access technique for a long time, but so far, it has not reached any practical success. We investigate the performance of low-complexity OCDMA systems with a realistic model of noise and interference; the main limitation of the system is beat noise. To improve the performance, we consider forward-error correction (FEC) and soft decoding using standard error-correcting codes. The achievable error rates are evaluated using simulations and show significant improvement when FEC is used. The results also show that frequency-hopping systems perform better than temporally coded systems when beat noise is taken into account.

## A 3-bit soft-decision IC for powerful forward error correction in 10-Gb/s optical communication systems

- **Status**: ❌
- **Reason**: 광통신용 3비트 소프트결정 IC+블록터보 코덱, 비-LDPC(터보)이고 LDPC 디코더 기법 비의존
- **ID**: ieee:1487614
- **Type**: journal
- **Published**: Aug. 2005
- **Authors**: H. Tagami, T. Kobayashi, Y. Miyata +8
- **PDF**: https://ieeexplore.ieee.org/document/1487614
- **Abstract**: We describe the design concept and performance of a 3-bit soft-decision IC, which opens a vista for new terabit-capacity optical communication systems by dramatically improving the capability of forward error correction (FEC). The proposed soft-decision IC is composed of five functional blocks, i.e., a soft-decider, an error filter, a 3-bit encoder, a 3:48 de-multiplexer, and a clock recovery circuit. The biggest challenge was the soft-decision block regenerating the common data using seven deciders with separate thresholds. We employed a novel SiGe BiCMOS process and a custom BGA package made from low-temperature co-fired ceramics to achieve a high sensitivity of 20 mVpp with a wide phase margin of 270/spl deg/ for 12.4-Gb/s nonreturn-to-zero (NRZ) data signals. The error filter and the 3-bit encoder, which are incorporated in the IC, prevent the degradation of the FEC performance due to signal noise or fluctuations. The 3:48 de-multiplexer provides an accessible interface with the FEC encoder/decoder LSI. The clock recovery circuit, based on a phase-locked-loop technology, fulfilled the jitter tolerance requirements corresponding to ITU-T G.825, even for 55% duty cycle optical return-to-zero (RZ) signals. The 3-bit soft-decision IC, in cooperation with a block turbo encoder/decoder, achieved a record net coding gain of 10.1 dB with 24.6% redundancy, which is only 0.9 dB away from the Shannon limit for a code rate of 0.8 for a binary symmetric channel.

## Iterative carrier phase recovery methods in turbo receivers

- **Status**: ❌
- **Reason**: 터보 수신기 반송파 위상 복구, LDPC 부수 언급 없고 떼어낼 ECC 기법 없음
- **ID**: ieee:1496599
- **Type**: journal
- **Published**: Aug. 2005
- **Authors**: Xiaofu Wu, Haige Xiang
- **PDF**: https://ieeexplore.ieee.org/document/1496599
- **Abstract**: This letter considers carrier phase recovery in turbo receivers. Firstly, a novel maximum-likelihood (ML) based iterative carrier phase estimator is proposed for coded linear modulations over static phase channels. The proposed carrier phase estimator, combined with the iterative sum-product decoder, performs very close to, the Cramer-Rao bound. Moreover, for practical dynamic phase channels, an efficient carrier phase recovery method is proposed to perform very close to that of a perfect coherent receiver.

## On the performance of LDPC coded MC-CDMA in Rayleigh fading channels

- **Status**: ❌
- **Reason**: LDPC coded MC-CDMA 무선 응용 성능평가, 최적 반복횟수만 도출 — 떼어낼 디코더/HW/코드설계 신규 기법 없음
- **ID**: ieee:1618132
- **Type**: conference
- **Published**: 8-12 Aug. 
- **Authors**: Lei Xiong, Zhenhui Tan, Yinghong Wen +1
- **PDF**: https://ieeexplore.ieee.org/document/1618132
- **Abstract**: In this paper, we evaluate the performance of LDPC coded MC-CDMA in Rayleigh fading channels. We derive an exact expression of the variance of multiuser interference and obtain the optimal maximum number of iterations in LDPC decoding. Compared to turbo coded MC-CDMA, the LDPC coded MC-CDMA has advantages in BER performance and complexity. The simulation results also show that the system using MMSEC outperforms the system using MRC in BER performance and complexity.

## Design considerations of a new HF modem and performance analysis

- **Status**: ❌
- **Reason**: HF 모뎀 설계, LDPC는 부수 비교 언급뿐 떼어낼 기법 없음
- **ID**: ieee:1618021
- **Type**: conference
- **Published**: 8-12 Aug. 
- **Authors**: Hui Zhang, Huazhong Yang, Rong Luo +1
- **PDF**: https://ieeexplore.ieee.org/document/1618021
- **Abstract**: A new 12.8 kbps high frequency (HF) modem is presented in this paper. To gain the low bit error rate (BER) in frequency-selective fading channels, this modem adopts a set of new technologies, including orthogonal frequency division multiplexing (OFDM) and space time block code (STBC). Extensive BER performance comparison between turbo code, low density parity check (LDPC) code, and punctured convolutional code have been made to determine which combination of technologies can achieve better performance while maintaining low complexity. Furthermore, theoretical analysis is presented for the BER performance hi two typical systems: the two transmit antennas and two receivers (2Tx/2Rx), two transmit antennas and a single receiver (2Tx/1Rx) in CCIR defined poor channel. Simulation results show that the performance of our new modem can be significantly improved. Compared to the conventional OFDM system, the 2Tx/1Rx system has achieved 3-10 dB diversity gain, while the 2Tx/2Rx system yields 4-15 dB

## Accuracy of dynamical models for analog iterative error control decoders

- **Status**: ❌
- **Reason**: 아날로그 연속시간 반복디코더 동역학 모델 정확도 평가 — 디지털 NAND LDPC 디코더에 이식할 기법 아님
- **ID**: ieee:1594399
- **Type**: conference
- **Published**: 7-10 Aug. 
- **Authors**: V.S.S.A. Devarakonda, C. Winstead
- **PDF**: https://ieeexplore.ieee.org/document/1594399
- **Abstract**: This paper examines the accuracy of an abstract dynamical model for continuous-time analog iterative error-control decoders. An existing compact dynamical model formulates iterative decoding as a fixed point problem. The dynamics of each analog cell are modeled by a non-linear differential equation with a single time-constant, which is solved numerically using Euler's method. We propose a fitness test to evaluate the accuracy of this abstract model. For randomly constructed codes and random stimuli, circuit descriptions are synthesized using both the abstract dynamical model and SPICE. A comparison is performed to measure the correspondence between the two simulations for codes of increasing length and complexity.

## Performance evaluation of LDPC codes in the presence of colored noise

- **Status**: ❌
- **Reason**: colored noise 하 기존 LDPC 성능평가만, 새 디코더·구성·HW 기여 없음 - 무선응용 성능분석
- **ID**: ieee:1517230
- **Type**: conference
- **Published**: 24-26 Aug.
- **Authors**: S.S. Tehrani, B.F. Cockburn, S. Bates
- **PDF**: https://ieeexplore.ieee.org/document/1517230
- **Abstract**: The class of low density parity check (LDPC) codes includes the most powerful capacity-approaching codes reported to date. As a result, LDPC codes have been considered for application in new communication standards such as 10GBASE-T Ethernet. However, the successful use of LDPC codes for such applications requires a better understanding of the effects of signal impairments on their error correction capabilities. In this paper, the performance of various LDPC codes in the presence of additive colored Gaussian noise (ACGN) is evaluated and compared with the effects of conventional additive white Gaussian noise (AWGN). The simulation results provide insight into the performance of LDPC codes in real systems in which the noise components can indeed be correlated. In particular, our results show that at the same signal-to-noise ratio (SNR), ACGN is more detrimental to the bit error rate (BER) performance than AWGN.

## Multiple access receiver based on hierarchical clusters/users detection using non-binary LDPC codes

- **Status**: ❌
- **Reason**: GF(4) 비이진 LDPC 기반 다중접속 검출 - 비이진 LDPC 제외
- **ID**: ieee:1517286
- **Type**: conference
- **Published**: 24-26 Aug.
- **Authors**: A. Goupil, M. Colas, D. Declercq +1
- **PDF**: https://ieeexplore.ieee.org/document/1517286
- **Abstract**: A new scheme of detection for multiple access channel is investigated, which consists in the combining of PIC-like detection and joint decoding of LDPC codes. The joint decoding is first investigated through the use of LDPC codes over Galois extensions of binary field for the AWGN multiple access channel. It turns out that the (2,4)-regular GF(4)-based LDPC codes perform 2dB better than the binary regular LDPC. As second result, we point out that GF(4) is also the best suited field's extension for this application. These preliminary results indicate that conjunction of PIC and joint detection could provide substantial improvement without any complexity growth of the emitter in a MC-CDMA like up-link framework.

## Spectral performance of integrated DC-free error-control codes

- **Status**: ❌
- **Reason**: DC-free 에러제어부호 스펙트럼 성능평가, LDPC 비관련 비-LDPC 변조부호
- **ID**: ieee:1517261
- **Type**: conference
- **Published**: 24-26 Aug.
- **Authors**: Fengqin Zhai, Yan Xin, I.J. Fair
- **PDF**: https://ieeexplore.ieee.org/document/1517261
- **Abstract**: Spectral performance of DC-free codes can be evaluated through performance metrics such as sum variance (SV) and low-frequency spectrum weight (LFSW). In this paper we investigate the spectral performance of integrated DC-free error-control codes. Analytical results for estimating the SV and LFSW of these codes are given.

## An enhanced block-coded modulation scheme with interblock memory

- **Status**: ❌
- **Reason**: 단일패리티검사 기반 블록부호화변조(interblock memory) - 비-LDPC, 떼어낼 LDPC ECC 기법 없음
- **ID**: ieee:1512834
- **Type**: conference
- **Published**: 24-22 Aug.
- **Authors**: Shang-Chih Ma, Chih-Fong Cheng
- **PDF**: https://ieeexplore.ieee.org/document/1512834
- **Abstract**: A new block coded modulation scheme with interblock memory is proposed. The proposed code construction is based on the use of single parity check codes to concatenate a set of K coded blocks. Simulation results show that the proposed scheme does attain a more efficient utilization of the available bandwidth and power.

## Serially concatenated LDPC and turbo code with global iteration

- **Status**: ❌
- **Reason**: LDPC+turbo 직렬연접 global iteration 성능분석, 새 디코더·구성 없는 연접 응용
- **ID**: ieee:1562852
- **Type**: conference
- **Published**: 16-18 Aug.
- **Authors**: Sang Hoon Lee, Ji Ae Seok, Eon Kyeong Joo
- **PDF**: https://ieeexplore.ieee.org/document/1562852
- **Abstract**: LDPC (low density parity check) code shows good performance at high SNR (signal to noise ratio), but turbo code shows better performance than LDPC code at low SNR. So, serially concatenated LDPC and turbo code can be a good choice to get good performance in both low and high SNR regions. Since both LDPC and turbo code use iterative decoding algorithms, global as well as local iteration is possible. Thus, the performance of serially concatenated LDPC and turbo code with global iteration is analyzed in this paper.
