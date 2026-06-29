# IEEE Xplore — 2009-02


## Lossy distributed source coding using LDPC codes

- **Status**: ❌
- **Reason**: 분산 소스코딩(Wyner-Ziv) - 소스코딩, 채널 ECC 아님. 떼어낼 LDPC ECC 기법 없음
- **ID**: ieee:4783783
- **Type**: journal
- **Published**: February 2
- **Authors**: Mina Sartipi, Faramarz Fekri
- **PDF**: https://ieeexplore.ieee.org/document/4783783
- **Abstract**: In this paper, we propose a practical scheme for lossy distributed source coding with side information available at the decoder. Our proposed scheme is based on sending parity bits using LDPC codes. We provide the design procedure for the LDPC code that guarantees performance close to the Wyner-Ziv limit for long LDPC codes. Using simulation results, we show that the proposed method performs close to the theoretical limit for even short length codes.

## An improved decoding algorithm for finite-geometry LDPC codes

- **Status**: ✅
- **Reason**: FG-LDPC용 개선 bit-flipping 디코딩(다중 비트 플립) - 이식 가능 디코더C
- **ID**: ieee:4784333
- **Type**: journal
- **Published**: February 2
- **Authors**: Telex Magloire Nkouatchah Ngatched, Fambirai Takawira, Martin Bossert
- **PDF**: https://ieeexplore.ieee.org/document/4784333
- **Abstract**: In this letter, an improved bit-flipping decoding algorithm for high-rate finite-geometry low-density parity-check (FG-LDPC) codes is proposed. Both improvement in performance and reduction in decoding delay are observed by flipping multiple bits in each iteration. Our studies show that the proposed algorithm achieves an appealing tradeoff between performance and complexity for FG-LDPC codes.

## LDPC codes based on serially concatenated multiple parity-check codes

- **Status**: ❌
- **Reason**: 직렬연접 MPC/RA 계열 부호 구성 - 비-LDPC RA 변형, 새 디코더·이식 가능 바이너리 LDPC 기법 없음
- **ID**: ieee:4783785
- **Type**: journal
- **Published**: February 2
- **Authors**: Marco Baldi, Giovanni Cancellieri, Andrea Carassai +1
- **PDF**: https://ieeexplore.ieee.org/document/4783785
- **Abstract**: This letter proposes a new class of serially concatenated codes that can be viewed as low-density parity- check (LDPC) codes. They are derived from multiple serially concatenated single parity-check (M-SC-SPC) codes, but they use different components, that we call multiple parity-check (MPC) codes. In comparison with M-SC-SPC codes, the new scheme achieves better performance with similar complexity. The proposed codes can represent an alternative to the well-known family of repeat accumulate (RA) codes, being based on the same principles.

## Finite-length rate-compatible LDPC codes: a novel puncturing scheme - [transactions letters]

- **Status**: ✅
- **Reason**: 유한길이 바이너리 LDPC rate-compatible puncturing 신규 기법(Tanner graph 거리 기반) - 코드설계E 이식 가능
- **ID**: ieee:4784332
- **Type**: journal
- **Published**: February 2
- **Authors**: Badri N. Vellambi, Faramarz Fekri
- **PDF**: https://ieeexplore.ieee.org/document/4784332
- **Abstract**: In this paper, we study rate-compatible puncturing of finite-length low-density parity-check (LDPC) codes. We present a novel rate-compatible puncturing scheme that is easy to implement. Our scheme uses the idea that the degradation in performance is reduced by selecting a puncturing pattern wherein the punctured bits are far apart from each other in the Tanner graph of the code. Although the puncturing scheme presented is tailored to regular codes, it is also directly applicable to irregular parent ensembles. By simulations, the proposed rate-compatible puncturing scheme is shown to be superior to the existing puncturing methods for both regular and irregular LDPC codes over the binary erasure channel (BEC) and the additive white Gaussian noise (AWGN) channel.

## Accumulate codes based on 1+D convolutional outer codes

- **Status**: ❌
- **Reason**: 누산 부호+1+D convolutional 연접 구성 - 비-LDPC, 떼어낼 LDPC BP 기법 없음
- **ID**: ieee:4784335
- **Type**: journal
- **Published**: February 2
- **Authors**: M.-C. Chiu, H.-F. Lu
- **PDF**: https://ieeexplore.ieee.org/document/4784335
- **Abstract**: A new construction of good, easily encodable, and soft-decodable codes is proposed in this paper. The construction is based on serially concatenating several simple 1+D convolutional codes as the outer code, and a rate-1 1/(1+D) accumulate code as the inner code. These codes have very low encoding complexity and require only one shift-forward register for each encoding branch. The input-output weight enumerators of these codes are also derived. Divsalariquests simple bound technique is applied to analyze the bit error rate performance, and to assess the minimal required signal-to-noise ratio (SNR) for these codes to achieve reliable communication under AWGN channel. Simulation results show that the proposed codes can provide good performance under iterative decoding.

## The design of efficiently-encodable rate-compatible LDPC codes - [transactions papers]

- **Status**: ✅
- **Reason**: rate-compatible puncturing용 신규 비정규 바이너리 LDPC 코드설계 + 선형시간 인코딩 - 코드설계E 이식 가능
- **ID**: ieee:4784346
- **Type**: journal
- **Published**: February 2
- **Authors**: Jaehong Kim, Aditya Ramamoorthy, Steven W. Mclaughlin
- **PDF**: https://ieeexplore.ieee.org/document/4784346
- **Abstract**: We present a new class of irregular low-density parity-check (LDPC) codes for moderate block lengths (up to a few thousand bits) that are well-suited for rate-compatible puncturing. The proposed codes show good performance under puncturing over a wide range of rates and are suitable for usage in incremental redundancy hybrid-automatic repeat request (ARQ) systems. In addition, these codes are linear-time encodable with simple shift-register circuits. For a block length of 1200 bits the codes outperform optimized irregular LDPC codes and extended irregular repeat-accumulate (eIRA) codes for all puncturing rates 0.6~0.9 (base code performance is almost the same) and are particularly good at high puncturing rates where good puncturing performance has been previously difficult to achieve.

## Wyner-Ziv coding based on TCQ and LDPC codes

- **Status**: ❌
- **Reason**: Wyner-Ziv/Slepian-Wolf 소스코딩에서 LDPC를 베이스라인으로 사용 - 소스코딩, 떼어낼 ECC 기법 없음
- **ID**: ieee:4784347
- **Type**: journal
- **Published**: February 2
- **Authors**: Yang Yang, Samuel Cheng, Zixiang Xiong +1
- **PDF**: https://ieeexplore.ieee.org/document/4784347
- **Abstract**: This paper considers trellis coded quantization (TCQ) and low-density parity-check (LDPC) codes for the quadratic Gaussian Wyner-Ziv coding problem. After TCQ of the source X, LDPC codes are used to implement Slepian-Wolf coding of the quantized source Q(X) with side information Y at the decoder. Assuming 256-state TCQ and ideal Slepian-Wolf coding in the sense of achieving the theoretical limit H(Q(X)|Y ), we experimentally show that Slepian-Wolf coded TCQ performs 0.2 dB away from the Wyner-Ziv distortion-rate function DWZ(R) at high rate. This result mirrors that of entropy-constrained TCQ in classic source coding of Gaussian sources. Furthermore, using 8,192-state TCQ and assuming ideal Slepian-Wolf coding, our simulations show that Slepian-Wolf coded TCQ performs only 0.1 dB away from DWZ(R) at high rate. These results establish the practical performance limit of Slepian-Wolf coded TCQ for quadratic Gaussian Wyner-Ziv coding. Practical designs give performance very close to the theoretical limit. For example, with 8,192-state TCQ, irregular LDPC codes for Slepian-Wolf coding and optimal non-linear estimation at the decoder, our performance gap to DWZ(R) is 0.20 dB, 0.22 dB, 0.30 dB, and 0.93 dB at 3.83 bit per sample (b/s), 1.83 b/s, 1.53 b/s, and 1.05 b/s, respectively. When 256-state 4-D trellis-coded vector quantization instead of TCQ is employed, the performance gap to DWZ(R) is 0.51 dB, 0.51 dB, 0.54 dB, and 0.80 dB at 2.04 b/s, 1.38 b/s, 1.0 b/s, and 0.5 b/s, respectively.

## A new framework for soft decision equalization in frequency selective MIMO channels

- **Status**: ❌
- **Reason**: MIMO 주파수선택 채널 BP 등화기 - LDPC는 부수 언급, 등화 응용특이적, 떼어낼 LDPC 기법 없음
- **ID**: ieee:4784350
- **Type**: journal
- **Published**: February 2
- **Authors**: Sara Bavarian, James K. Cavers
- **PDF**: https://ieeexplore.ieee.org/document/4784350
- **Abstract**: We introduce a novel framework for soft-input, soft-output (SISO) equalization in frequency selective multipleinput multiple-output (MIMO) channels based on the well-known belief propagation (BP) algorithm. As in the BP equalizer, we model the multipath channels using factor graphs (FGs) where the transmitted and received signals are represented by the function and variable nodes respectively. The edges connecting the function and variable nodes illustrate the dependencies of the multipath channel and soft decisions are developed by exchanging information on these edges iteratively. We incorporate powerful techniques such as groupwise iterative multiuser detection (IMUD), probabilistic data association (PDA) and sphere decoding (SD) in order to reduce the computational complexity of BP equalizer with relatively small degradation in performance. The computational complexity of this new reduced-complexity BP (RCBP) equalizer grows linearly with block size and memory length of the channel. The proposed framework has a flexible structure that allows for parallel as well as serial detection. We will illustrate through simulations that the RCBP equalizer can even handle overloaded scenarios where the channel matrix is rank deficient, and it can achieve excellent performance by applying iterative equalization using the low-density parity check codes (LDPC).

## Performance analysis of network coding with raptor codes for IPTV

- **Status**: ❌
- **Reason**: 네트워크코딩+Raptor(fountain/erasure) IPTV - LDPC 아닌 fountain, 떼어낼 ECC 기법 없음
- **ID**: ieee:4814418
- **Type**: journal
- **Published**: February 2
- **Authors**: Kwangseok Noh, Sungroh Yoon, Jun Heo
- **PDF**: https://ieeexplore.ieee.org/document/4814418
- **Abstract**: Multimedia services including IPTV require huge multimedia data transmission on the Internet. In order to improve a throughput of data transmission, network coding has been proposed to use network bandwidth (=throughput) efficiently with error free channel assumption. However, when the channel is not error free, network coding may not increase the throughput. In this case, effective erasure recovery codes such as Raptor codes have to be used with the network coding. We present the advantage of Raptor codes combined with network coding for high throughput multimedia data transmission services like IPTV. For the applications allowing retransmission, hybrid-ARQ combined with network coding is also considered.

## Multi-Gb/s LDPC Code Design and Implementation

- **Status**: ✅
- **Reason**: shift-LDPC 신규 부호 구성+girth 최적화+고속 VLSI 디코더 ASIC, 메모리 절감 — D/E 이식 가능
- **ID**: ieee:4689312
- **Type**: journal
- **Published**: Feb. 2009
- **Authors**: Jin Sha, Zhongfeng Wang, Minglun Gao +1
- **PDF**: https://ieeexplore.ieee.org/document/4689312
- **Abstract**: Low-density parity-check (LDPC) code, a very promising near-optimal error correction code (ECC), is being widely considered in next generation industry standards. The VLSI implementation of high-speed LDPC decoder remains a big challenge. This paper presents the construction of a new class of implementation-oriented LDPC codes, namely shift-LDPC codes. With girth optimization, this kind of codes can perform as well as computer generated random codes. More importantly, the decoder can be efficiently implemented to obtain very high decoding speeds. In addition, more than 50% of message memory can be generally saved over conventional partially parallel decoder architectures. We demonstrate the benefits of the proposed techniques with an application-specific integrated circuit (ASIC) design (in 0.18-mum CMOS) for a 8192-bit regular LDPC code, which can achieve 5 Gb/s throughput at 15 iterations.

## Code design and shuffled iterative decoding of a quasi-cyclic LDPC coded OFDM system

- **Status**: ❌
- **Reason**: 표준 QC-LDPC(density evolution+circulant)+shuffled BP를 OFDM에 그대로 적용, 신규 기여 없음
- **ID**: ieee:6073167
- **Type**: journal
- **Published**: Feb. 2009
- **Authors**: Binbin Liu, Dong Bai, Qihong Ge +1
- **PDF**: https://ieeexplore.ieee.org/document/6073167
- **Abstract**: In multipath environments, the error rate performance of orthogonal frequency division multiplexing (OFDM) is severely degraded by the deep fading subcarriers. Powerful error-correcting codes must be used with OFDM. This paper presents a quasi-cyclic low-density parity-check (LDPC) coded OFDM system, in which the redundant bits of each codeword are mapped to a higher-order modulation constellation. The optimal degree distribution was calculated using density evolution. The corresponding quasi-cyclic LDPC code was then constructed using circulant permutation matrices. Group shuffled message passing scheduling was used in the iterative decoding. Simulation results show that the system achieves better error rate performance and faster decoding convergence than conventional approaches on both additive white Gaussian noise (AWGN) and Rayleigh fading channels.

## Power and modulo loss tradeoff with expanded soft demapper for LDPC coded GMD-THP MIMO systems

- **Status**: ❌
- **Reason**: GMD-THP MIMO용 expanded soft demapper(LLR 계산)는 변조/THP 특이적, NAND ECC로 이식 불가
- **ID**: ieee:4786433
- **Type**: journal
- **Published**: Feb. 2009
- **Authors**: Edward C. Y. Peh, Ying-Chang Liang
- **PDF**: https://ieeexplore.ieee.org/document/4786433
- **Abstract**: Tomlinson-Harashima precoding (THP) can be combined with geometric mean decomposition (GMD) to decouple a multiple-input multiple-output (MIMO) channel into multiple single-input single-output (SISO) subchannels with identical signal-to-noise ratios (SNRs). The combined system is called GMD-THP MIMO system. As all subchannels for this system have identical SNRs, it is more convenient to design modulation/demodulation and coding/decoding schemes than other MIMO systems that have different SNRs among the subchannels. In this paper, we consider low-density parity-check (LDPC) coded GMD-THP MIMO systems. Modulo operation at the receiver is needed for THP decoding but it may generate modulo errors. These modulo errors cause the log likelihood ratio (LLR) values provided by conventional soft demapper to be very inaccurate. We propose an expanded soft demapper scheme to reduce the inaccuracy of the LLR values, by which significant performance improvement can be achieved for LDPC decoding. Furthermore, THP introduces power loss and modulo loss into the system. These two losses are related to the size of the modulo boundaries and therefore we derive the expressions for these two losses as functions of the modulo size factor. With these expressions, we find the optimal modulo size factor which achieves the minimum combined losses through doing a tradeoff between power loss and modulo loss. Computer simulations are presented to show that the tradeoff indeed improves the performance of the LDPC coded GMD-THP systems.

## Low-Density Codes Based on Chaotic Systems for Simple Encoding

- **Status**: ❌
- **Reason**: 카오스 동역학 기반 LDGM(generator-matrix) 부호 - LDPC 아닌 LDGM, NAND 이식 가능 기법 없음
- **ID**: ieee:4663666
- **Type**: journal
- **Published**: Feb. 2009
- **Authors**: Slobodan Kozic, Martin Hasler
- **PDF**: https://ieeexplore.ieee.org/document/4663666
- **Abstract**: This paper proposes a new class of low-density generator-matrix codes (LDGM) based on chaotic dynamical systems. The codes are designed by controlling symbolic dynamics and using linear convolutional codes. Analyzing the complex structure of chaotic systems, iterative decoding is developed. The communication performance is studied, and convergence analysis of the iterative-decoding system is presented. Finally, comparison and advantages over LDGM linear block codes in terms of encoding complexity and bit-error-rate performance are described, and possible applications of our codes are discussed.

## Finite-Length Scaling for Iteratively Decoded LDPC Ensembles

- **Status**: ✅
- **Reason**: 바이너리 LDPC 유한길이 스케일링 법칙+error floor로 빠른 유한길이 최적화 — E 코드설계 이식 가능
- **ID**: ieee:4777618
- **Type**: journal
- **Published**: Feb. 2009
- **Authors**: Abdelaziz Amraoui, Andrea Montanari, Tom Richardson +1
- **PDF**: https://ieeexplore.ieee.org/document/4777618
- **Abstract**: We investigate the behavior of iteratively decoded low-density parity-check (LDPC) codes over the binary erasure channel in the so-called ldquowaterfall region.rdquo We show that the performance curves in this region follow a simple scaling law. We conjecture that essentially the same scaling behavior applies in a much more general setting and we provide some empirical evidence to support this conjecture. The scaling law, together with the error floor expressions developed previously, can be used for a fast finite-length optimization.

## On the ARMA approximation for fading channels described by the Clarke model with applications to Kalman-based receivers

- **Status**: ❌
- **Reason**: Clarke 페이딩 채널 Kalman 수신기 ARMA 근사, LDPC 없음 — 떼어낼 ECC 기법 없음
- **ID**: ieee:4786403
- **Type**: journal
- **Published**: Feb. 2009
- **Authors**: Alan Barbieri, Amina Piemontese, Giulio Colavolpe
- **PDF**: https://ieeexplore.ieee.org/document/4786403
- **Abstract**: We consider a terrestrial wireless channel, whose statistical model under flat-fading conditions is due to Clarke. A lot of papers in the literature deal with receivers for this scenario, aiming at estimating and tracking the time-varying channel, possibly with the aid of known (pilot) symbols. A common approach to derive receivers of reasonable complexity is to resort to a Kalman filter which is based on an approximation of the actual fading process as autoregressive moving-average (ARMA) of a given order. The aim of this paper is to show that the approximation of the actual fading process, usually exploited in the literature, is far from effective. Thus, we present a novel technique, based on an off-line minimization of the mean square error of the channel estimate, which ensures a considerable gain in terms of bit-error rate for Kalman-based receivers without increasing the receiver complexity. Moreover, we also propose a novel approximation, to be employed in Kalman smoothers proposed for iterative detection schemes, which allows further performance improvements without a significant increase of the computational complexity.

## Diversity and coding gain evolution in graph codes

- **Status**: ❌
- **Reason**: full-diversity MDS LDPC는 무선 페이딩 채널 다이버시티 목적, NAND 고전 LDPC에 이식할 기법 아님
- **ID**: ieee:5044920
- **Type**: conference
- **Published**: 8-13 Feb. 
- **Authors**: Joseph J. Boutros
- **PDF**: https://ieeexplore.ieee.org/document/5044920
- **Abstract**: This work is a first attempt to analyze and understand the coding gain of full-diversity (MDS) low-density parity-check (LDPC) codes. A diversity population evolution is derived. The steady-state distribution of energy coefficients is found. Based on this new analysis, we show new full-diversity LDPC codes with improved performance. Finally, we describe a family of graph codes where all variable nodes, including parity nodes, achieve full diversity after a large number of decoding iterations. Full-diversity MDS low-density codes are not only useful for digital data transmission over wireless channels, some other applications can be found in situations where coding for a finite number of states is required.

## Asymptotic trapping set analysis of regular protograph-based LDPC convolutional code ensembles

- **Status**: ✅
- **Reason**: 코드 설계(E): protograph SC-LDPC ensemble의 trapping set 성장률 분석으로 error floor 예측, 이식 가능
- **ID**: ieee:5044956
- **Type**: conference
- **Published**: 8-13 Feb. 
- **Authors**: David G. M. Mitchell, Ali E. Pusane, Daniel J. Costello
- **PDF**: https://ieeexplore.ieee.org/document/5044956
- **Abstract**: It has been suggested that ldquonear-codewordsrdquo may be a significant factor affecting decoding failures of LDPC codes over the AWGN channel. A near-codeword is a sequence that satisfies almost all of the check equations. These near-codewords can be associated with so-called dasiatrapping setspsila that exist in the Tanner graph of a code. In this paper, we analyse the trapping sets of protograph-based LDPC convolutional codes. LDPC convolutional codes have been shown to be capable of achieving the same capacity-approaching performance as LDPC block codes with iterative message-passing decoding. Further, it has been shown that some ensembles of LDPC convolutional codes are asymptotically good, in the sense that the average free distance grows linearly with constraint length. Here, asymptotic methods are used to calculate a lower bound on the trapping set growth rates for several ensembles of regular asymptotically good protograph-based LDPC convolutional codes. This provides us with an estimate of where the error floor will occur for these codes under iterative message-passing decoding.

## Approaching capacity with asymptotically regular LDPC codes

- **Status**: ✅
- **Reason**: 코드 설계(E): protograph 기반 비대칭 정규 SC-LDPC 구성과 density evolution threshold 개선, 이식 가능
- **ID**: ieee:5044941
- **Type**: conference
- **Published**: 8-13 Feb. 
- **Authors**: Michael Lentmaier, Gerhard P. Fettweis, Kamil Sh. Zigangirov +1
- **PDF**: https://ieeexplore.ieee.org/document/5044941
- **Abstract**: We present a family of protograph based LDPC codes that can be derived from permutation matrix based regular (J,K) LDPC convolutional codes by termination. In the terminated protograph, all variable nodes still have degree J but some check nodes at the start and end of the protograph have degrees smaller than K. Since the fraction of these stronger nodes vanishes as the termination length L increases, we call the codes asymptotically regular. The density evolution thresholds of these protographs are better than those of regular (J, K) block codes. Interestingly, this threshold improvement gets stronger with increasing node degrees (at a fixed rate) and it does not decay as L increases. Terminated convolutional protographs can also be derived from standard irregular protographs and may exhibit a significant threshold improvement.

## Optimizing channel coding for orthogonal multiple access schemes with correlated sources

- **Status**: ❌
- **Reason**: 상관소스 다중접속 채널코딩 최적화(SCCC/EXIT), 무선 응용 특이적이고 LDPC는 비교대상일 뿐 신규 이식 기법 없음
- **ID**: ieee:5044916
- **Type**: conference
- **Published**: 8-13 Feb. 
- **Authors**: A. Abrardo, G. Ferrari, M. Martalo +2
- **PDF**: https://ieeexplore.ieee.org/document/5044916
- **Abstract**: In this paper, we consider multiple access schemes with correlated sources. Distributed source coding is not used; rather, the correlation is exploited at the access point (AP). In particular, we assume that each source uses a channel code to transmit, through an additive white Gaussian noise (AWGN) channel, its information to the AP, where component decoders, associated with the sources, iteratively exchange soft information by taking into account the correlation. The key goal of this paper is to investigate whether there exist optimized channel codes for this scenario, i.e., channel codes which guarantee a desired performance level (in terms of average bit error rate, BER) at the lowest possible signal-to-noise ratio (SNR). A two-dimensional extrinsic information transfer (EXIT) chart-inspired optimization approach is proposed. Our results suggest that by properly designing serially concatenated convolutional codes (SCCCs), the theoretical performance limits can be approached better than by using parallel concatenated convolutional codes (PCCCs) or low-density parity-check (LDPC) codes. It is also shown that irregular LDPC codes tend to perform better than regular LDPC codes, so that the design of appropriate LDPC codes remains an open issue.

## On trapping sets for repeat accumulate accumulate codes

- **Status**: ✅
- **Reason**: trapping set 분석을 BP 디코딩에 적용한 유한길이 enumerator, LDPC error floor 분석 기법(C/E) 이식 가능
- **ID**: ieee:5044939
- **Type**: conference
- **Published**: 8-13 Feb. 
- **Authors**: Jorg Kliewer, Christian Koller, Alexandre Graell i Amat +1
- **PDF**: https://ieeexplore.ieee.org/document/5044939
- **Abstract**: The serial concatenation of a repetition code with two or more accumulators has the advantage of a simple encoder structure. Furthermore, the resulting ensemble is asymptotically good and exhibits minimum distance growing linearly with block length. For low-density parity-check codes, the notion of trapping sets has been introduced to estimate the performance of these codes under non-maximum likelihood decoding. We briefly address asymptotic expressions for the normalized minimum trapping distance for the Gallager-Zyablov-Pinsker bit flipping decoding algorithm. Then we consider belief propagation decoding and present a closed form finite length ensemble average trapping set enumerator for repeat accumulate accumulate codes by creating a trellis representation of trapping sets. For this case, we also obtain asymptotic expressions and evaluate them numerically.

## Guaranteed error correction capability of codes on graphs

- **Status**: ✅
- **Reason**: 코드 설계(E): column weight·girth와 보장 오류정정능력 관계, expander 논증 신규 결과 이식 가능
- **ID**: ieee:5044922
- **Type**: conference
- **Published**: 8-13 Feb. 
- **Authors**: Shashi Kiran Chilappagari, Bane Vasic, Michael W. Marcellin
- **PDF**: https://ieeexplore.ieee.org/document/5044922
- **Abstract**: The guaranteed error correction capability of left regular LDPC codes under different hard decision decision algorithms is investigated. A summary of recent results relating the column weight and girth of the Tanner graph to the guaranteed error correction capability is provided. The intuition behind expander based arguments and their potential to derive new results for column-weight-three codes is provided.

## Iterated decoding of modified product codes in optical networks

- **Status**: ❌
- **Reason**: 비-LDPC 부호(modified product codes) 광통신용, LDPC BP 이식 기법 없음
- **ID**: ieee:5044938
- **Type**: conference
- **Published**: 8-13 Feb. 
- **Authors**: Jorn Justesen
- **PDF**: https://ieeexplore.ieee.org/document/5044938
- **Abstract**: Appendix I of the standard ITU-T G.975 contains several codes that have been proposed for improved performance of optical transmission. While the original application was submarine cables, the codes are now also used in terrestrial systems where wavelength-division multiplexing (WDM) is introduced. Currently codes suitable for data rates of 100 Gbits/sec in each channel are being studied. We discuss performance limits for codes with the specified block lengths of about 130,000 and rates about 15/16. The most promising codes appear to be modified product codes, and iterated decoding is used in several cases. We discuss the construction, decoding, and performance of such codes.

## Quantization effects in biometric systems

- **Status**: ❌
- **Reason**: 바이오메트릭 비밀키 생성/프라이버시 누설율 트레이드오프(보안), LDPC ECC 무관, 떼어낼 디코더/HW/구성 없음
- **ID**: ieee:5044973
- **Type**: conference
- **Published**: 8-13 Feb. 
- **Authors**: Frans M.J. Willems, Tanya Ignatenko
- **PDF**: https://ieeexplore.ieee.org/document/5044973
- **Abstract**: The fundamental secret-key rate vs. privacy-leakage rate trade-offs for secret-key generation and transmission for i.i.d. Gaussian biometric sources are determined. These results are the Gaussian equivalents of the results that were obtained for the discrete case by the authors and independently by Lai et al. in 2008. Also the effect that binary quantization of the biometric sequences has on the ratio of the secret-key rate and privacy-leakage rate is considered. It is shown that the squared correlation coefficient must be increased by a factor of pi2/4 to compensate for such a quantization action, for values of the privacy-leakage rate that approach zero, when the correlation coefficient is close to zero.

## Layered LDGM codes for scalable video streaming over packet erasure channels

- **Status**: ❌
- **Reason**: LDGM 기반 패킷 erasure FEC 비디오 스트리밍, erasure/scalable 코딩이라 NAND 채널 ECC로 이식할 기법 없음
- **ID**: ieee:4806671
- **Type**: conference
- **Published**: 8-11 Feb. 
- **Authors**: Yoshihide Tonomura, Daisuke Shirai, Takayuki Nakachi +2
- **PDF**: https://ieeexplore.ieee.org/document/4806671
- **Abstract**: This paper introduces layered low-density generator matrix (Layered-LDGM) codes for scalable video streaming data. The layered-LDGM codes maintain the arbitrary relationship of each layer from the encoder side to the decoder side. This resulting structure supports partial decoding. Furthermore, the proposed codes create forward error correcting (FEC) packets that considers the relationship between the scalable components. Thus, the layered-LDGM codes enable lost packet data to be recovered effectively. Simulation results show that the proposed codes offer better error resiliency, without sacrificing scalability, than the existing method which creates FEC packets for each scalable component independently.

## A Modified Belief Propagation Decoding Algorithm of LDPC Codes for Fast Convergence

- **Status**: ✅
- **Reason**: 빠른 수렴 위한 수정 BP 디코딩 알고리즘(반복 횟수 절반); 이식 가능 디코더 기법(C)
- **ID**: ieee:5076905
- **Type**: conference
- **Published**: 27-28 Feb.
- **Authors**: Ai-min Zhu, Sen-jie Yao
- **PDF**: https://ieeexplore.ieee.org/document/5076905
- **Abstract**: The belief-propagation decoding algorithm for low-density parity check codes is analyzed and the convergence characteristic of this algorithm is researched. A modified belief-propagation decoding algorithm aiming at decreasing the number of iteration is proposed. Simulation result shows that the number of iteration of the proposed algorithm is only half of that of the standard one at expense of little loss in performance.

## Design of Optimal LDPC Code for the System of MDPSK Concatenated with LDPC Codes

- **Status**: ❌
- **Reason**: MDPSK 결합 복조/디코딩용 EXIT 차트 기반 degree distribution 최적화; 무선 변조 특이적, 떼어낼 일반 기법 없음
- **ID**: ieee:5076906
- **Type**: conference
- **Published**: 27-28 Feb.
- **Authors**: Zhu Aimin, Yao Senjie
- **PDF**: https://ieeexplore.ieee.org/document/5076906
- **Abstract**: The combined demodulating and decoding algorithm of the system of M-ary Differential Phase-Shift Keying (MDPSK) concatenated with Low-Density Parity Check Codes in AWGN channels is analyzed in this paper. Concentrating on the above algorithm, we propose a design method of optimal LDPC code based on Extrinsic Information Transfer Chart. Meanwhile, as an example, degree distribution of LDPC code at a rate of one-half bit per channel is given for both MDPSK and pi/4 DQPSK system concatenated with Low-Density Parity Check Codes.

## Selective Cooperative Schemes Using Quasi-Cyclic LDPC Codes over Rayleigh Fading Channels

- **Status**: ❌
- **Reason**: Rayleigh 페이딩 협력통신에 표준 QC-LDPC 적용 성능 평가; 신규 구성/디코더 없는 무선 응용
- **ID**: ieee:5076935
- **Type**: conference
- **Published**: 27-28 Feb.
- **Authors**: Zhixiong Chen, Jinsha Yuan
- **PDF**: https://ieeexplore.ieee.org/document/5076935
- **Abstract**: Cooperative communication enables distributed terminals with a single antenna to form a virtual multiple antenna system and benefits from diversity. In this paper quasi-cyclic LDPC codes are applied to both amplify-and-forward cooperative scheme and decode-and-forward scheme over Rayleigh fading half-duplex relay channel. Simulation results show excellent performance of quasi-cyclic LDPC codes with cooperative schemes compared to the same codes in direct link communication of AWGN channel and Rayleigh channel. Compared to amplify-and-forward scheme, it is shown that decode-and-forward scheme is more sensitive to the path-loss fading.

## Construction of regular quasi-cyclic LDPC codes based on cosets

- **Status**: ✅
- **Reason**: 코셋 기반 QC-LDPC 구성(비소수 circulant size 포함, girth>=6), 코드설계 기법(E)
- **ID**: ieee:4909226
- **Type**: conference
- **Published**: 17-18 Feb.
- **Authors**: Pengcheng Chen, Yuansheng Tang, Zhanghua Cao +1
- **PDF**: https://ieeexplore.ieee.org/document/4909226
- **Abstract**: We propose a construction method for constructing quasi-cyclic low-density parity-check (QC LDPC) codes based on subgroup's coset. Our construction method is available not only for the prime circulants size, but also for the nonprime circulants size in some conditions. And it is showed that these conditions are easy to satisfy. Regular QC LDPC codes with various lengths and rates can be easily constructed with girth at least 6. Simulation results show that they are have almost the same performance as random regular LDPC codes over AWGN channel.

## Reduced complexity soft detection for BICM MIMO OFDM system

- **Status**: ❌
- **Reason**: MIMO/OFDM BICM 소프트 검출(MMSE/ZF/max-log-MAP) — LDPC ECC 아님, 떼어낼 디코더/HW 기법 없음
- **ID**: ieee:4909263
- **Type**: conference
- **Published**: 17-18 Feb.
- **Authors**: Rizwan Ghaffar, Raymond Knopp
- **PDF**: https://ieeexplore.ieee.org/document/4909263
- **Abstract**: This paper presents a new approach to the soft detection of spatial data streams in MIMO channels in slow fading channels. We focus on high spectral efficiency bit interleaved coded modulation (BICM) MIMO OFDM system where, after serial to parallel conversion and per antenna coding, spatial data streams are simultaneously transmitted by using an antenna array. We propose a detection algorithm basing on the combination of linear and non linear detection techniques. The proposed algorithm orders the spatial streams as per V-BLAST ordering and then uses linear detectors as MMSE or zero forcing (ZF) to detect the streams which have seen good channel realizations and therefore enjoy higher signal-to-noise-ratios (SNRs). These streams after being detected are subsequently stripped off leading to the max log MAP detection of the streams which have seen comparatively poor realizations of the channel and consequently have lower SNRs. Unlike maximum likelihood (ML) detection, whose complexity is huge due to the need for enumerating all possible combinations of the transmitted constellation points, the proposed method has low complexity. The algorithm has a fully parallel structure, suitable for the implementation in parallel hardware. Numerical examples illustrate its performance on slow fading 3 times 3 and 4 times 4 complex MIMO channels.

## On the use of QC-LDPC code for data transfer using short and medium block length

- **Status**: ✅
- **Reason**: circulant submatrix 기반 QC-LDPC 개선 구성 제안 - 이식 가능 코드설계(E)
- **ID**: ieee:4809425
- **Type**: conference
- **Published**: 15-18 Feb.
- **Authors**: Mohammad Rakibul Islam, Jinsang Kim
- **PDF**: https://ieeexplore.ieee.org/document/4809425
- **Abstract**: Quasi Cyclic Low Density Parity Check codes (QC-LDPC) is proposed to reduce the complexity of the Low Density Parity Check codes (LDPC) further while obtaining the similar performance. Our proposed QC-LDPC presents an improved construction of circulant sub-matrices based QC-LDPC at high SNR. The proposed construction yields a performance gain of about 1 dB at a 0.0003 bit error rate (BER). Proposed code is tested on 4 types of decoding algorithm and compared. Proposed algorithm is also compared with the existing QC-LDPC and the proposed approach outperforms the existing one at high SNR. Simulation is also performed varying the number of horizontal submatrix and the result shows that the parity check matrix with smaller horizontal concatenation shows better performance.

## Rateless erasure resilient codes for content storage and distribution in P2P networks

- **Status**: ❌
- **Reason**: P2P용 rateless erasure resilient code - fountain/erasure 계열, 떼어낼 바이너리 LDPC ECC 기법 없음
- **ID**: ieee:4809990
- **Type**: conference
- **Published**: 15-18 Feb.
- **Authors**: Saejoon Kim, Seunghyuk Lee
- **PDF**: https://ieeexplore.ieee.org/document/4809990
- **Abstract**: In this paper, we investigate the performance of rateless erasure resilient codes for distributed file storage in P2P networks. While the key distinctive feature of the proposed codes is the scalability to an arbitrary number of peers in the P2P network, it will be shown that the proposed rateless erasure resilient codes also offer great improvement in increase in bandwidth and reliability of data retrieval compared to other erasure resilient coding schemes.

## Improving the security of McEliece-like public key cryptosystem based on LDPC codes

- **Status**: ❌
- **Reason**: LDPC 기반 McEliece 공개키 암호 보안 강화 - 보안 도메인, 떼어낼 ECC 디코더/구성 기법 없음
- **ID**: ieee:4809594
- **Type**: conference
- **Published**: 15-18 Feb.
- **Authors**: Masumeh Koochak Shooshtari, Mahmoud Ahmadian, Ali Payandeh
- **PDF**: https://ieeexplore.ieee.org/document/4809594
- **Abstract**: Decoding attacks are subjected to McEliece code-based public key cryptosystems. Nowadays, complexity of order 280 is considered to be immune. However, the original McEliece cryptosystem has work factor of order 264 against this kind of attacks. There aren't any immune methods to avoid this kind of attacks except increasing code parameters, whereas, this modifications make McEliece cryptosystem impractical. In this paper we improve the security level of LDPC based McEliece cryptosystem i.e. Baldi's cryptosystem about 223 operations to achieve the work factor of 294, without any remarkable increment in key-size or any decrement in transmission rate or speed of cryptosystem.

## Low-complexity entirely-overlapped parallel decoder architecture for quasi-cyclic LDPC codes

- **Status**: ✅
- **Reason**: QC-LDPC용 저복잡도 entirely-overlapped 병렬 디코더 아키텍처 - 이식 가능 HW(D)
- **ID**: ieee:4809576
- **Type**: conference
- **Published**: 15-18 Feb.
- **Authors**: Weizhi Lu, Piming Ma
- **PDF**: https://ieeexplore.ieee.org/document/4809576
- **Abstract**: In this paper, we propose a low-complexity entirely-overlapped partially-parallel decoder architecture for quasi-cyclic low-density parity-check (QC-LDPC) codes. For a (c, t)-regular QC-LDPC decoder, this decoder can achieve approximate 100% hardware utilization efficiency (HUE) and entirely overlapped decoding by using only one check node process unit group (CNUG) to process c groups of check node messages sequentially. Compared with traditional partially-parallel decoder, the quantities of check node process unit (CNU), barrel shifters and counters can be decreased prominently. Moreover, it is flexible in code rate and code length.

## An error control scheme of hybrid ARQ based on conception of plurality voting

- **Status**: ❌
- **Reason**: binary linear block code용 hybrid ARQ 투표 기법 - LDPC 비특이적 재전송 프로토콜, 떼어낼 ECC 기법 없음
- **ID**: ieee:4809893
- **Type**: conference
- **Published**: 15-18 Feb.
- **Authors**: Chia-Chin Ma, Hsin-Kun Lai, Erl-Huei Lu
- **PDF**: https://ieeexplore.ieee.org/document/4809893
- **Abstract**: Based on the conception of voting, this paper proposes an error control scheme of hybrid ARQ for binary linear block codes over AWGN channel. The proposed scheme keeps each decoded code word in the memory buffers as a candidate at each transmission. Whenever there are a number of code words in the candidates are the same one, retransmission stops. In other words, the plurality of code words among candidates is chosen as the output code word. Simulation results illustrate that the proposed scheme outperforms ARQ scheme not only in the throughput efficiency but also in the error-correcting performance, particularly under low SNR.

## Comparison of Downlink Throughput Distributions between Frequency Reuse Factors of One and Three in MBWA System Field Trial

- **Status**: ❌
- **Reason**: MBWA 무선시스템 주파수재사용 throughput 필드시험, ECC 무관
- **ID**: ieee:4800575
- **Type**: conference
- **Published**: 11-13 Feb.
- **Authors**: H. Oguma, S. Kameda, T. Takagi +4
- **PDF**: https://ieeexplore.ieee.org/document/4800575
- **Abstract**: In this paper, we report on a mobile broadband wireless access (MBWA) system field trial with fast low-latency access with seamless handoff orthogonal frequency division multiplexing (FLASH-OFDM), which was carried out at Sendai city in Japan. Downlink throughput distributions in multiple-cells environment with a sectored cell layout are discussed when the frequency reuse factors are one and three. The field trial results show that the reuse factors of one and three yield the median downlink throughputs of 3.2 Mbit/s and 2.1 Mbit/s, respectively, within 3.84 MHz system bandwidth. It is considered that the MBWA system with the reuse factor of one has higher median throughput by 50% than that with the reuse factor of three in multiple-cells environment.

## Study on the decoding algorithm for LDPC based on DMB-TH

- **Status**: ✅
- **Reason**: TDMP(turbo-decoding message-passing) 기반 LDPC 코드탐색+디코더 아키텍처, HW 고려 코드설계/디코더 기법 이식 가능(C/D/E)
- **ID**: ieee:4939498
- **Type**: conference
- **Published**: 10-13 Feb.
- **Authors**: Guo-Chun Wan, Yan-Fen Luo, Xun Liu +1
- **PDF**: https://ieeexplore.ieee.org/document/4939498
- **Abstract**: Terrestrial digital multimedia TV/handle broadcasting (DMB-TH) is a newly upcoming framing structure, channel coding and modulation for digital television terrestrial broadcasting system standard of China, which is recently drafted and is ready to be verified in order to deploy mobile multimedia broadcasting services for the public. The adoption of strong channel coding techniques appears to be of key importance for mobile operators and broadcasters. Low-density parity-check (LDPC) codes have been widely considered as error-correcting codes for next generation communication systems. A good LDPC decoder design requires both implementation friendly LDPC codes and efficient decoder architectures. The quality of LDPC code is crucial in determining the coding gain and implementation complexity of LDPC hardware decoders. This paper presents a turbo-decoding message-passing algorithm (TDMP) based LDPC code search algorithm with hardware considerations. The main advantages of the proposed algorithm over the DMB-TH standard decoding algorithm are 1) improvement in coding gain by an order of magnitude at high signal-to-noise ratio (SNR), 2) reduced decoder complexity. The performance of the proposed TDMP architecture is shown by the comparison of simulation results.
