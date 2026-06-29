# IEEE Xplore — 2006-03


## Combined source and channel coding with JPEG2000 and rate-compatible low-density Parity-check codes

- **Status**: ❌
- **Reason**: JPEG2000+RC-LDPC 소스-채널 결합(JSCC) — LDPC 베이스라인, 떼어낼 ECC 기법 없음
- **ID**: ieee:1597578
- **Type**: journal
- **Published**: March 2006
- **Authors**: Xiang Pan, A. Cuhadar, A.H. Banihashemi
- **PDF**: https://ieeexplore.ieee.org/document/1597578
- **Abstract**: Rate-compatible low-density parity-check (RC-LDPC) codes are used to provide unequal error protection for the robust and efficient transmission of JPEG2000 compressed images over noisy channels. The total bit budget is partitioned between the source and the channel coding by using a Viterbi algorithm (VA) applied to a search trellis, and appropriate channel code rates are assigned to the source blocks. The performance of the proposed scheme is evaluated on binary symmetric channels (BSCs). Experimental results indicate that the proposed scheme compares favorably with other combined source/channel coding schemes over a variety of channel conditions and transmission bit rates. In particular, the proposed scheme outperforms similar schemes based on turbo codes and irregular repeat-accumulate codes by up to about 1.1 and 1 dB in the expected peak signal-to-noise ratio (PSNR) of reconstructed images, respectively.

## Reliability-based coded modulation with low-density parity-check codes

- **Status**: ❌
- **Reason**: BICM 인터리버/열치환 설계는 변조-부호 매핑 응용 특이적, NAND LDPC ECC로 떼어낼 코드설계 기여 아님
- **ID**: ieee:1605456
- **Type**: journal
- **Published**: March 2006
- **Authors**: R.D. Maddock, A.H. Banihashemi
- **PDF**: https://ieeexplore.ieee.org/document/1605456
- **Abstract**: In this letter, we consider the interleaver design in bit-interleaved coded modulation (BICM) with low-density parity-check (LDPC) codes. The design paradigm is to provide more coding protection through iterative decoding to bits that are less protected by modulation (and are thus less reliable at the output of the demodulator). The design is carried out by an ad hoc search algorithm over the column permutations of the parity-check matrix. Our simulations show that the proposed reliability-based coded modulation scheme can improve the error-rate performance of conventional BICM schemes based on regular LDPC codes by a few tenths of a decibel, with no added complexity.

## Joint LDPC decoding and timing recovery using code constraint feedback

- **Status**: ❌
- **Reason**: LDPC 디코딩-타이밍복구 결합으로 PLL 동기화 응용, 떼어낼 ECC/디코더 기법 없음(무선/통신 응용 특이적)
- **ID**: ieee:1603380
- **Type**: journal
- **Published**: March 2006
- **Authors**: D.-U. Lee, E.L. Valles, J.D. Villasenor +1
- **PDF**: https://ieeexplore.ieee.org/document/1603380
- **Abstract**: Timing recovery and channel decoding are traditionally performed independently. However, we show here that the information generated during the iterative decoding of low-density parity-check (LDPC) coded data can be fed back to the timing recovery circuit to enable accurate estimation of frequency and phase errors without the need for any pilot symbols. We describe a method capable of handling large offsets with complexity that grows linearly with offset size. Combining the LDPC constraint node observations with a properly calibrated phase locked loop allows successful tracking of a constant time delay, a frequency offset and a random phase walk.

## On the stopping distance and the stopping redundancy of codes

- **Status**: ❌
- **Reason**: stopping set/stopping redundancy 순수 이론 bound(RM/Golay/MDS), 디코더/HW/구성으로 이어지지 않음
- **ID**: ieee:1603762
- **Type**: journal
- **Published**: March 2006
- **Authors**: M. Schwartz, A. Vardy
- **PDF**: https://ieeexplore.ieee.org/document/1603762
- **Abstract**: It is now well known that the performance of a linear code Copf under iterative decoding on a binary erasure channel (and other channels) is determined by the size of the smallest stopping set in the Tanner graph for Copf. Several recent papers refer to this parameter as the stopping distance s of Copf. This is somewhat of a misnomer since the size of the smallest stopping set in the Tanner graph for Copf depends on the corresponding choice of a parity-check matrix. It is easy to see that s les d, where d is the minimum Hamming distance of Copf, and we show that it is always possible to choose a parity-check matrix for Copf (with sufficiently many dependent rows) such that s=d. We thus introduce a new parameter, the stopping redundancy of Copf, defined as the minimum number of rows in a parity- check matrix H for Copf such that the corresponding stopping distance s(H) attains its largest possible value, namely, s(H)=d. We then derive general bounds on the stopping redundancy of linear codes. We also examine several simple ways of constructing codes from other codes, and study the effect of these constructions on the stopping redundancy. Specifically, for the family of binary Reed-Muller codes (of all orders), we prove that their stopping redundancy is at most a constant times their conventional redundancy. We show that the stopping redundancies of the binary and ternary extended Golay codes are at most 34 and 22, respectively. Finally, we provide upper and lower bounds on the stopping redundancy of MDS codes

## On information transmission over a finite buffer channel

- **Status**: ❌
- **Reason**: buffer/deletion channel 용량 이론, LDPC 무관 순수 정보이론
- **ID**: ieee:1603788
- **Type**: journal
- **Published**: March 2006
- **Authors**: S. Diggavi, M. Grossglauser
- **PDF**: https://ieeexplore.ieee.org/document/1603788
- **Abstract**: We study information transmission through a finite buffer queue. We model the channel as a finite-state channel whose state is given by the buffer occupancy upon packet arrival; a loss occurs when a packet arrives to a full queue. We study this problem in two contexts: one where the state of the buffer is known at the receiver, and the other where it is unknown. In the former case, we show that the capacity of the channel depends on the long-term loss probability of the buffer. Thus, even though the channel itself has memory, the capacity depends only on the stationary loss probability of the buffer. The main focus of this correspondence is on the latter case. When the receiver does not know the buffer state, this leads to the study of deletion channels, where symbols are randomly dropped and a subsequence of the transmitted symbols is received. In deletion channels, unlike erasure channels, there is no side-information about which symbols are dropped. We study the achievable rate for deletion channels, and focus our attention on simple (mismatched) decoding schemes. We show that even with simple decoding schemes, with independent and identically distributed (i.i.d.) input codebooks, the achievable rate in deletion channels differs from that of erasure channels by at most H0(pd)-pd logK/(K-1) bits, for pd<1-K-1, where p d is the deletion probability, K is the alphabet size, and H 0(middot) is the binary entropy function. Therefore, the difference in transmission rates between the erasure and deletion channels is not large for reasonable alphabet sizes. We also develop sharper lower bounds with the simple decoding framework for the deletion channel by analyzing it for Markovian codebooks. Here, it is shown that the difference between the deletion and erasure capacities is even smaller than that with i.i.d. input codebooks and for a larger range of deletion probabilities. We also examine the noisy deletion channel where a deletion channel is cascaded with a symmetric discrete memoryless channel (DMC). We derive a single letter expression for an achievable rate for such channels. For the binary case, we show that this result simplifies to max(0,1-[H0(thetas)+thetasH0(p e)]) where pe is the cross-over probability for the binary symmetric channel

## Adaptive MAP receiver via the EM algorithm and message passings for MIMO-OFDM mobile communications

- **Status**: ❌
- **Reason**: MIMO-OFDM MAP 수신기(EM/RLS 채널추정)로 LDPC는 부수 언급, 떼어낼 디코더 기법 없음
- **ID**: ieee:1603700
- **Type**: journal
- **Published**: March 2006
- **Authors**: T. Kashima, K. Fukawa, H. Suzuki
- **PDF**: https://ieeexplore.ieee.org/document/1603700
- **Abstract**: This paper proposes two new types of maximum a posteriori probability (MAP) receivers for multiple-input-multiple-output and orthogonal frequency-division multiplexing mobile communications with a channel coding such as the low-density parity-check code. One proposed receiver employs the expectation-maximization algorithm so as to improve performance of approximated MAP detection. Differently from a conventional receiver employing the minimum mean-square estimation (MMSE) algorithm, it applies the recursive least squares (RLS) algorithm to the channel estimation in order to track a fast fading channel. For the purpose of further improvement, the other proposed receiver applies a new adaptive algorithm that can be derived from the message passing on factor graphs. The algorithm exploits all detected signals but one of targeted time, and can gain a considerable advantage over the MMSE and RLS. Computer simulations show that the first proposed receiver is superior in channel-tracking ability to the conventional receiver employing the MMSE. Furthermore, it is demonstrated that the second proposed receiver remarkably outperforms both the conventional and the first proposed ones.

## Area-Efficient Error Protection for Caches

- **Status**: ❌
- **Reason**: L2/L3 캐시 ECC 면적 절감(parity+선택적 ECC), LDPC 무관·떼어낼 ECC 기법 없음
- **ID**: ieee:1657092
- **Type**: conference
- **Published**: 6-10 March
- **Authors**: Soontae Kim
- **PDF**: https://ieeexplore.ieee.org/document/1657092
- **Abstract**: Due to increasing concern about various errors, current processors adopt error protection mechanisms. Especially, protecting L2/L3 caches incur as much as 12.5% area overhead due to error correcting codes. Considering large L2/L3 caches of current processors, the area overhead is very high. This paper proposes an area-efficient error protection scheme for L2/L3 caches. First, it selectively applies ECC (Error Correcting Code) to only dirty cache lines and other clean cache lines are protected using simple parity check codes. Second, the dirty cache lines are periodically cleaned by exploiting the generational behavior of cache lines. Experimental results show that the cleaning technique effectively reduces the number of dirty cache lines per cycle. The ECCs of this reduced number of dirty cache lines can be maintained in a small storage. Our proposed scheme is shown to reduce the area overhead of a 1MB L2 cache for error protection by 59% for SPEC2000 benchmarks running on a typical four-issue superscalar processor.

## Low-density parity-check codes for 40 Gb/s transmission

- **Status**: ❌
- **Reason**: 40Gb/s용 LDPC BER 비교(서베이성), 비이진 LDPC 포함·신규 디코더/구성/HW 기여 없음
- **ID**: ieee:1636729
- **Type**: conference
- **Published**: 5-10 March
- **Authors**: B. Vasic, I.B. Djordjevic
- **PDF**: https://ieeexplore.ieee.org/document/1636729
- **Abstract**: BER performance of LDPC codes, generalized LDPC codes and nonbinary LDPC codes, suitable for 40 Gb/s transmission, are compared against turbo product codes and RS concatenation schemes.

## Using FEC code for improving the WDM/SCM - PON performance

- **Status**: ❌
- **Reason**: RS 코드 기반 FEC 선택(WDM/SCM-PON), LDPC 아님·떼어낼 기법 없음 → 제외
- **ID**: ieee:1636900
- **Type**: conference
- **Published**: 5-10 March
- **Authors**: Dong-Min Seol, Seung-Hyun Jang, Chul-Soo Lee +2
- **PDF**: https://ieeexplore.ieee.org/document/1636900
- **Abstract**: For improving the performance of the most cost-efficient WDM/SCM-PON, the way how to choose a FEC code is described. The choosing methods are a code rate and hard resource size. A RS code is best suitable.

## Suppression of intrachannel nonlinearities using BCJR algorithm and iterative decoding

- **Status**: ❌
- **Reason**: BCJR/MAP 반복 디코딩으로 광채널 비선형 억제, LDPC 부재·이식 ECC 기법 없음
- **ID**: ieee:1636440
- **Type**: conference
- **Published**: 5-10 March
- **Authors**: B. Vasic, I.B. Djordjevic, V.S. Rao
- **PDF**: https://ieeexplore.ieee.org/document/1636440
- **Abstract**: MAP symbol decoding supplemented with iterative decoding is used to mitigate the intrachannel nonlinearities. The MAP detector operates on the channel trellis to correct the corrupted data and to provide soft outputs processed further in an iterative decoder. A dramatic performance improvement is demonstrated.

## Low density codes achieve the rate-distortion bound

- **Status**: ❌
- **Reason**: 저밀도 소스코드의 rate-distortion bound 달성; 소스 코딩(압축)이며 채널 ECC 아님
- **ID**: ieee:1607250
- **Type**: conference
- **Published**: 28-30 Marc
- **Authors**: E. Martinian, M. Wainwright
- **PDF**: https://ieeexplore.ieee.org/document/1607250
- **Abstract**: We propose a new construction for low-density source codes with multiple parameters that can be tuned to optimize the performance of the code. In addition, we introduce a set of analysis techniques for deriving upper bounds for the expected distortion of our construction, as well as more general low-density constructions. We show that (with an optimal encoding algorithm) our codes achieve the rate-distortion bound for a binary symmetric source and Hamming distortion. Our methods also provide rigorous upper bounds on the minimum distortion achievable by previously proposed low-density constructions.

## On efficient quantizer design for robust distributed source coding

- **Status**: ❌
- **Reason**: 분산 소스코딩용 양자화기 설계(deterministic annealing); 소스 코딩이며 채널 ECC 아님
- **ID**: ieee:1607241
- **Type**: conference
- **Published**: 28-30 Marc
- **Authors**: A. Saxena, J. Nayak, K. Rose
- **PDF**: https://ieeexplore.ieee.org/document/1607241
- **Abstract**: This paper considers the design of efficient quantizers for a distributed source coding system. The information is encoded at independent terminals and transmitted across separate channels, any of which may fail. The scenario subsumes a wide range of vector quantization problems. Greedy descent methods rely heavily on initialization, and the presence of numerous 'poor' local optima on the distortion cost surface strongly motivates the use of a global design algorithm. We propose a deterministic annealing approach for the design of all components of a generic distributed source coding system. Our approach avoids many poor local optima, is independent of initialization, and does not assume any prior information on the underlying source distribution. Simulation results show significant gains over an iterative greedy algorithm.

## Self-Protection of Turbo- and LDPC-Coded OFDM Systems against Non-Stationary Disturbances

- **Status**: ❌
- **Reason**: Burst-error self-protection (erasure decoding, subframing/interleaving) for OFDM; channel-domain trick, no transferable NAND LDPC decoder/code-design
- **ID**: ieee:4534726
- **Type**: conference
- **Published**: 27-28 Marc
- **Authors**: Julien Pons, Amitkumar Mahadevan, Patrick Duvaut
- **PDF**: https://ieeexplore.ieee.org/document/4534726
- **Abstract**: This paper presents a method to protect turbo- and low density parity check (LDPC)-coded OFDM systems against non-stationary disturbances without using external codes. The technique does not alter the structure of the original code and the constellation mapper/demapper, but requires the insertion of a so-called self-protection unit (SPU) between the coding and constellation mapping units. The SPU enhances the burst-error-correction capabilities of turbo and LDPC codes by combining erasure-decoding, subframing (i.e., reordering the coded data into subframes), and the optional use of subframe interleaving to spread error bursts. Self-protected systems exhibit a reduced latency and storage capacity compared to classical channel interleaving schemes with similar protection level.

## Mitigation of Performance Degradation by Impulsive Noise in LDPC Coded OFDM System

- **Status**: ❌
- **Reason**: 임펄스 잡음 채널 LLR 추정/신호 리미터(PLC-OFDM 응용 특이적), 떼어낼 LDPC 디코더/코드설계 기법 없음
- **ID**: ieee:1716934
- **Type**: conference
- **Published**: 26-29 Marc
- **Authors**: Hui-Myoung Oh, Young-Jin Park, Sungsoo Choi +2
- **PDF**: https://ieeexplore.ieee.org/document/1716934
- **Abstract**: In the paper, LDPC (Low-Density Parity-Check) coded OFDM system applicable for impulsive noise channel, such as powerline channel (PLC) will be presented. Performance degradation in the proposed system over impulsive noise channel is mitigated using a simple estimator based on the Gaussian approximation with estimated channel information (ECI) and a signal level limiter. At first, it will be shown that the performance of a conventional LDPC coded OFDM system is seriously degraded due to the imperfection of estimating the initial LLRs (Log Likelihood Ratios) of sum-product decoder over impulsive noise channels and hard evaluation of the initial LLRs from the decentralized noise samples by OFDM demodulator. Thereafter, to overcome the problems, the system using the simple estimator and the received signal level limiter is proposed. Simulation results show that the proposed system has much better performance than that of conventional systems. For the verification, Monte Carlo simulation is applied.

## LDPC Coding for Non-Uniform Power-Line Channels

- **Status**: ❌
- **Reason**: PLC 주파수선택 채널용 불균일 비균일 채널 LDPC 코드설계(비이진 변조 포함), NAND 이식 가능한 코드설계 기법 없는 채널 특이적 최적화
- **ID**: ieee:1716936
- **Type**: conference
- **Published**: 26-29 Marc
- **Authors**: M. Ardakani, A. Sanaei
- **PDF**: https://ieeexplore.ieee.org/document/1716936
- **Abstract**: Irregular low-density parity-check coding is studied for frequency selective channels and discreet multi-tone (DMT) systems that are used for power-line channels. To let a long block-length code with a practical buffer delay, we protect all the symbols that are transmitted in a DMT symbol with one code. The main challenge, therefore, is the varying signal to noise ratio in different frequency tones, which normally necessitates using different codes for different frequency tones (according to their signal to noise ratios). We show that if this non-uniformity is considered in the code design process, low-density parity-check codes that approach the capacity of such frequency selective channels can he found. Compared to codes that are designed for uniform channels, our codes have a significantly smaller gap from the capacity. As an extreme case, we focus on systems that - for reducing signalling and detection complexity - use only one non-binary modulation in all frequency tones. Therefore, the soft information at the receiver experiences a dramatic non-uniform quality from bit to bit. Surprisingly, even in this case, very close-to-capacity performance can be obtained

## Fundamental Performance Limits for PLC Systems Impaired by Impulse Noise

- **Status**: ❌
- **Reason**: PLC 임펄스노이즈 정보율 한계 이론분석, LDPC는 BER 시뮬 베이스라인일 뿐 떼어낼 기법 없음
- **ID**: ieee:1716925
- **Type**: conference
- **Published**: 26-29 Marc
- **Authors**: R. Pighi, M. Franceschini, G. Ferrari +1
- **PDF**: https://ieeexplore.ieee.org/document/1716925
- **Abstract**: In this paper, we provide insights on the ultimate performance limits, in terms of achievable information rate, for power line communication (PLC) systems impaired by impulse noise. In particular, we analyze single carrier (SC) and multiple carrier (MC) transmission systems employing quadrature amplitude modulation (QAM) formats. In order to compute the information rates of standard MC systems, we introduce a theoretically equivalent channel model which allows the exact computation of the information rate. This simplified channel model will be referred to as interleaved MC channel model. We show that the use of MC schemes leads to an unavoidable loss with respect to SC schemes. In order to validate our theoretical results, we analyze the bit error rate (BER) performance of SC and MC schemes through Monte Carlo simulations. Several trellis-coded modulation (TCM) and low-density parity-check (LDPC)-coded schemes are considered

## Joint Low Density Parity-Check Coding and Linear Precoding for Rayleigh Fading Channels

- **Status**: ❌
- **Reason**: Rayleigh 페이딩 채널용 LDPC+linear precoding 결합; 무선 응용 특이적, 떼어낼 일반 디코더/구성 기법 없음
- **ID**: ieee:4067954
- **Type**: conference
- **Published**: 22-24 Marc
- **Authors**: Yingqun Yu, Georgios B. Giannakis
- **PDF**: https://ieeexplore.ieee.org/document/4067954
- **Abstract**: We introduce a serially concatenated scheme consisting of outer low density parity-check (LDPC) coding and inner complex field linear precoding (LP) for reliable communications over wireless fading channels. We compare the ergodic capacities of the uncorrelated Rayleigh flat fading channel with and without LP, and show that for constellation-constrained inputs LP can bring considerable signal-to-noise ratio (SNR) gains even with precoders of size as small as 2 or 4. We further derive both optimal and low-complexity sub-optimal iterative decoding algorithms and employ extrinsic information transfer (EXIT) charts to approximately evaluate threshold values of their performance. Simulations reveal that when BPSK is used, the novel LDPC-LP scheme results in up to 1.3 dB (1.0 dB) gain at rate frac12for regular (irregular) codes with a medium block size.

## The Generator and Parity-Check Matrices of Turbo Codes

- **Status**: ❌
- **Reason**: 터보 부호의 생성/패리티검사 행렬 이론 분석. 비-LDPC 부호이고 떼어낼 디코더·HW 기법 없음
- **ID**: ieee:4068034
- **Type**: conference
- **Published**: 22-24 Marc
- **Authors**: Fan Jiang, Eric Psota, Lance C. Perez
- **PDF**: https://ieeexplore.ieee.org/document/4068034
- **Abstract**: Turbo codes are typically represented as parallel concatenated convolutional codes, but will be treated as serially concatenated codes in this paper. Treating turbo codes as serially concatenated codes makes possible the general description of their generator and parity-check matrices. Given the generator and parity-check matrices, turbo codes may be analyzed from a block and low-density parity-check code point of view.

## Incremental Redundancy Low-Density Parity Check Codes for MIMO V-BLAST Systems

- **Status**: ❌
- **Reason**: MIMO V-BLAST용 IR-HARQ 펑처링 rate-compatible LDPC; 무선 시스템 특이적 코드선택, 떼어낼 NAND ECC 기법 없음
- **ID**: ieee:4067923
- **Type**: conference
- **Published**: 22-24 Marc
- **Authors**: Woonhaing Hur, Steven W. McLaughlin
- **PDF**: https://ieeexplore.ieee.org/document/4067923
- **Abstract**: The throughput of an incremental redundancy hybrid forward error correction/automatic retransmission request (IR-hybridARQ) scheme strongly depends on the design of the error correction code. In this paper, we consider ensembles of rate-compatible LDPC codes using an intentional puncturing algorithm in a vertical bell lab layered space-time (V-BLAST) system. We also present an adaptive IR-hybridARQ scheme with a code selection algorithm for reducing the traffic of a feedback channel. With the proposed adaptive code selection algorithm, we can reduce the traffic of the feedback channel for NACK signaling greatly without any significant throughput loss.

## On the Complexity of finding stopping set size in Tanner Graphs

- **Status**: ❌
- **Reason**: Tanner 그래프 stopping set 크기 결정의 NP-완전성 증명, 순수 이론 bound로 디코더/HW/구성으로 안 이어짐
- **ID**: ieee:4067794
- **Type**: conference
- **Published**: 22-24 Marc
- **Authors**: K. Murali Krishnan, Priti Shankar
- **PDF**: https://ieeexplore.ieee.org/document/4067794
- **Abstract**: The problem of determining whether a tanner graph for a linear block code has a stopping set of a given size is shown to be NP-complete.

## Performance Analysis and Code Design for Cooperative Relay Channels

- **Status**: ❌
- **Reason**: 협력 릴레이 채널 LDPC 부호 설계; EXIT/differential evolution으로 채널특이 ensemble 최적화, 무선 응용 특이
- **ID**: ieee:4067959
- **Type**: conference
- **Published**: 22-24 Marc
- **Authors**: Chuxiang Li, Mohammad Ali Khojastepour, Guosen Yue +2
- **PDF**: https://ieeexplore.ieee.org/document/4067959
- **Abstract**: We treat the LDPC code design for relay channels in this paper. The capacity of relay channels has been analyzed in current literature. How to approach such capacity with the aid of good codes is, however, a challenging problem. An efficient structure is proposed to decouple the factor graph (FG) of a B-block transmission into successive partial FGs, and then, the code design can be performed over the partial FG. Based on this efficient structure, we develop the approaches to find the optimum code ensemble. In particular, we formulate the relay and the destination operations as virtual multiple-antenna channels. Moreover, we develop the approaches based on the binary symmetric channel modelling for the relay and Gaussian approximation to fast estimate the extrinsic mutual information of the destination detector output. Then we can analyze the performance of the relay system using the EXIT technique. Differential evolution is employed to search for the optimum code ensemble. Extensive simulations are further carried out to show the results of the proposed optimum code design.

## Bandwidth Expansion Shannon Mapping for Analog Error-Control Coding

- **Status**: ❌
- **Reason**: Shannon mapping 아날로그 전송. LDPC와 무관, 떼어낼 ECC 기법 없음
- **ID**: ieee:4068077
- **Type**: conference
- **Published**: 22-24 Marc
- **Authors**: Xiaodong Cai, James W. Modestino
- **PDF**: https://ieeexplore.ieee.org/document/4068077
- **Abstract**: Based on an initial idea of Shannon, we investigate an approach, named Shannon mapping, for transmission of analog messages, that is fundamentally different from current digital communication methods. We investigate 1:2 bandwidth expansion Shannon mapping based on two specific mapping curves. We demonstrate that bandwidth expansion Shannon mapping using a mapping curve does not introduce any delay and its encoding and decoding processes exhibit very low complexity. More importantly, our simulations show that the distortion performance of 1:2 bandwidth expansion Shannon mapping is significantly better than the rate-distortion bound without bandwidth expansion at moderate to high SNRs, and about 3-5 dB inferior to the rate-distortion bound with the same bandwidth expansion.

## A Practical Scheme for Relaying in Sensor Networks Using Repeat-Accumulate Codes

- **Status**: ❌
- **Reason**: 비-LDPC(repeat-accumulate) 부호의 센서망 릴레이 협력 응용, 떼어낼 바이너리 LDPC BP 기법 없음
- **ID**: ieee:4067838
- **Type**: conference
- **Published**: 22-24 Marc
- **Authors**: Andrew W. Eckford, Raviraj S. Adve
- **PDF**: https://ieeexplore.ieee.org/document/4067838
- **Abstract**: Given limitations with current technology, nodes in a sensor network have stringent energy and complexity constraints. This paper presents a scheme for cooperation via relaying and error-control coding in sensor networks, using punctured systematic repeat-accumulate codes. Assuming knowledge of the source-relay channel quality, we use density evolution to show that the proposed scheme achieves good performance and a good energy tradeoff despite low computational complexity. An interesting additional benefit of such a scheme is the notion of fractional cooperation by a relay node. As a motivating example, we analyze networks of up to ten cooperating nodes in Rayleigh fading, which communicate with a more sophisticated receiver.

## Optimal Linear Dispersion Codes for Correlated MIMO Channels

- **Status**: ❌
- **Reason**: MIMO 상관채널 linear dispersion 시공간부호 설계; LDPC ECC와 무관, 떼어낼 디코더/HW/코드설계 기법 없음
- **ID**: ieee:4067873
- **Type**: conference
- **Published**: 22-24 Marc
- **Authors**: Che Lin, Venugopal V. Veeravalli
- **PDF**: https://ieeexplore.ieee.org/document/4067873
- **Abstract**: The design of space-time codes for frequency flat, spatially correlated MIMO fading channels is considered. The focus of the paper is on the class of space-time block codes known as linear dispersion (LD) codes, introduced by Hassibi and Hochwald. The LD codes are optimized with respect to the mutual information between the inputs to the space-time encoder and the output of the channel. The use of the mutual information as both a design criterion and a performance measure is justified by allowing soft decisions at the output of the space-time decoder. A spatial Fourier (virtual) representation of the channel is exploited to allow for the analysis of MIMO channels with quite general fading statistics. Conditions, known as generalized orthogonality conditions (GOC), are derived for an LD code to achieve an upper bound on the mutual information, with the understanding that LD codes that achieve the upper bound, if they exist, are optimal. Explicit code constructions and properties of the optimal power allocation schemes are also derived. In particular, it is shown that optimal LD codes correspond to beamforming to a single virtual transmit angle at low SNR, and a necessary and sufficient condition for beamforming to be optimal is provided. Finally, numerical results are provided to illustrate the optimal code design for two examples of sparse scattering environments. The performance of the optimal LD codes for these scattering environments is compared with that of LD codes designed assuming the i.i.d. Rayleigh (rich scattering) model, and it is shown that the optimal LD codes perform significantly better. The optimal LD codes are also compared to beamforming LD codes and it is shown that beamforming is nearly optimal over a range of SNR's of interest.

## Parallel LDGM Codes for the Transmission of Highly Correlated Senders over Rayleigh Fading Multiple Access Channels

- **Status**: ❌
- **Reason**: LDGM 부호로 상관 소스 JSCC 전송; 소스-채널 결합, 채널 ECC 떼어낼 기법 없음
- **ID**: ieee:4067994
- **Type**: conference
- **Published**: 22-24 Marc
- **Authors**: Wei Zhong, Javier Garcia-Frias
- **PDF**: https://ieeexplore.ieee.org/document/4067994
- **Abstract**: We investigate the use of LDGM codes for the transmission of two highly correlated senders over a Rayleigh fading multiple access channel. Each one of the senders is encoded independently, and without knowledge of the correlation parameters, using an LDGM code. Decoding is performed in a common receiver, which exploits the correlation between the senders by performing message passing in a graph jointly describing the correlation model and the channel codes. The resulting performance surpasses the theoretical limits obtained when separation between source and channel coding is assumed. As opposed to the case of uncorrelated senders, the performance loss when the channel state information is not available at the decoder is practically non-existent.

## Low-density constructions for lossy compression, binning, and coding with side information

- **Status**: ❌
- **Reason**: lossy compression·binning·side-information용 LDGM/LDPC 소스코딩, 채널 ECC 아님
- **ID**: ieee:1633825
- **Type**: conference
- **Published**: 13-17 Marc
- **Authors**: E. Martinian, M.J. Wainwright
- **PDF**: https://ieeexplore.ieee.org/document/1633825
- **Abstract**: In this extended abstract, we provide a high-level overview of some of our recent work [10], [11], [9] on low-density graphical codes for various communication problems including lossy compression, binning, and coding with side information. Sparse graphical codes, particularly low-density parity check (LDPC) codes, are widely used and well understood in application to channel coding problems [16]. On the other hand, for other communication problems—especially those involving aspects of both channel and source coding—there remain various open questions associated with using low-density code constructions. Examples of such problems include (a) lossy source coding (data compression); (b) source coding with side information (the Wyner-Ziv problem [19]), and (c) channel coding with side information (the Gelfand-Pinsker problem [7]). Our work tackles these problems using sparse graphical constructions that are based on a combination of LDPC codes, and their dual versions, namely low-density generator matrix (LDGM) codes.

## The Block Error Probability of Detailedly Represented Irregular LDPC Code Ensembles under Maximum Likelihood Decoding

- **Status**: ❌
- **Reason**: irregular LDPC ML 디코딩 block error probability 상한 — 순수 이론 bound로 디코더/HW/구성으로 안 이어짐
- **ID**: ieee:1633837
- **Type**: conference
- **Published**: 13-17 Marc
- **Authors**: R. Ikegaya, K. Kasai, T. Shibuya +1
- **PDF**: https://ieeexplore.ieee.org/document/1633837
- **Abstract**: In this paper, we have derived the upper bound of the average block error probability of a given detailedly represented irregular low-density parity-check (LDPC) code ensemble under maximum likelihood decoding.

## LDPC-based Gaussian key reconciliation

- **Status**: ❌
- **Reason**: Gaussian key reconciliation (정보조정)이며 코드설계도 표준 LDPC 적용 수준, 떼어낼 디코더/HW 기법 없음
- **ID**: ieee:1633793
- **Type**: conference
- **Published**: 13-17 Marc
- **Authors**: M. Bloch, A. Thangaraj, S.W. McLaughlin +1
- **PDF**: https://ieeexplore.ieee.org/document/1633793
- **Abstract**: We propose a new information reconciliation method which allows two parties sharing continuous random variables to agree on a common bit string. We show that existing coded modulation techniques can be adapted for reconciliation and give an explicit code construction based on LDPC codes in the case of Gaussian variables. Simulations show that our method achieves higher efficiency than previously reported results.

## Using Many Machines to Handle an Enormous Error-Correcting Code

- **Status**: ❌
- **Reason**: Tornado 코드를 MapReduce로 분산 인코딩/디코딩, erasure 채널 대규모 인프라 문제로 NAND ECC 기법 없음
- **ID**: ieee:1633806
- **Type**: conference
- **Published**: 13-17 Marc
- **Authors**: J. Feldman
- **PDF**: https://ieeexplore.ieee.org/document/1633806
- **Abstract**: We investigate the problem of using many machines to represent, encode and decode an error-correcting code with an extremely large block length. Standard algorithms for encoding and decoding run into problems when scaled to a block length that does not allow random access to the data. We apply the massive computing infrastructure at Google together with the MapReduce programming abstraction to encode and decode a Tornado code over the erasure channel.

## Analysis of Belief Propagation for Non-Linear Problems: The Example of CDMA (or: How to Prove Tanaka's Formula)

- **Status**: ❌
- **Reason**: CDMA 다중사용자 검출 BP 분석, 통신 응용 특이적이고 LDPC ECC로 이식할 디코더 기법 아님
- **ID**: ieee:1633802
- **Type**: conference
- **Published**: 13-17 Marc
- **Authors**: A. Montanari, D. Tse
- **PDF**: https://ieeexplore.ieee.org/document/1633802
- **Abstract**: We consider the CDMA (code-division multiple-access) multi-user detection problem for binary signals and additive white gaussian noise. We propose a spreading sequences scheme based on random sparse signatures, and a detection algorithm based on belief propagation (BP) with linear time complexity. In the new scheme, each user conveys its power onto a finite number of chips l̄, in the large system limit. We analyze the performances of BP detection and prove that they coincide with the ones of optimal (symbol MAP) detection in the l̄ → ∞ limit. In the same limit, we prove that the information capacity of the system converges to Tanaka's formula for random 'dense' signatures, thus providing the first rigorous justification of this formula. Apart from being computationally convenient, the new scheme allows for optimization in close analogy with irregular low density parity check code ensembles.

## Distributed Kernel Regression: An Algorithm for Training Collaboratively

- **Status**: ❌
- **Reason**: 분산 커널 회귀 학습 알고리즘, LDPC/ECC와 무관
- **ID**: ieee:1633840
- **Type**: conference
- **Published**: 13-17 Marc
- **Authors**: J.B. Predd, S.R. Kulkarni, H.V. Poor
- **PDF**: https://ieeexplore.ieee.org/document/1633840
- **Abstract**: This paper addresses the problem of distributed learning under communication constraints, motivated by distributed signal processing in wireless sensor networks and data mining with distributed databases. After formalizing a general model for distributed learning, an algorithm for collaboratively training regularized kernel least-squares regression estimators is derived. Noting that the algorithm can be viewed as an application of successive orthogonal projection algorithms, its convergence properties are investigated and the statistical behavior of the estimator is discussed in a simplified theoretical setting.

## Superposition by Position

- **Status**: ❌
- **Reason**: OFDM superposition 코딩, 무선 채널 추정 문제로 LDPC ECC 무관
- **ID**: ieee:1633816
- **Type**: conference
- **Published**: 13-17 Marc
- **Authors**: Hui Jin, R. Laroia, T. Richardson
- **PDF**: https://ieeexplore.ieee.org/document/1633816
- **Abstract**: We present a novel method for superposition coding applicable to OFDM systems in which the receivers being transmitted to are one high SNR receiver and one low SNR receiver. The degradation of the high SNR receiver, however, results primarily from channel uncertainty. Thus, we consider the effect of imperfect channel estimates, a ubiquitous problem in mobile wireless, and show that the new scheme performs much better than traditional schemes in such a setting.

## Punctured vs Rateless Codes for Hybrid ARQ

- **Status**: ❌
- **Reason**: HARQ용 LDPC vs Raptor 비교, 무선 채널 응용 특이적이며 떼어낼 신규 디코더/구성 기법 없음
- **ID**: ieee:1633801
- **Type**: conference
- **Published**: 13-17 Marc
- **Authors**: E. Soijanin, N. Varnica, P. Whiting
- **PDF**: https://ieeexplore.ieee.org/document/1633801
- **Abstract**: Two incremental redundancy hybrid ARQ (IR-HARQ) schemes are compared: one is based on LDPC code ensembles with random transmission assignments, the other is based on recently introduced Raptor codes. A number of important issues, such as rate and power control, and error rate performance after each transmission on time varying binary-input, symmetric-output channels are addressed by analyzing performance of LDPC and Raptor codes on parallel channels. The theoretical results obtained for random code ensembles are tested on several practical code examples by simulation. Both theoretical and simulation results show that both LDPC and Raptor codes are suitable for HARQ schemes. Which codes would make a better choice depends mainly on the width of the signal-to-noise operating range of the HARQ scheme, prior knowledge of that range, and other design parameters and constraints dictated by standards.
