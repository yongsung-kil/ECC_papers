# IEEE Xplore — 2009-06 (1차선별 통과)


## Pseudocodeword Performance Analysis for LDPC Convolutional Codes

- **Status**: ✅
- **Reason**: LDPC convolutional code의 의사부호어 성능분석은 error floor/구성 분석 기법으로 SC-LDPC 설계(E)에 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4957655
- **Type**: journal
- **Published**: June 2009
- **Authors**: Roxana Smarandache, Ali E. Pusane, Pascal O. Vontobel +1
- **PDF**: https://ieeexplore.ieee.org/document/4957655
- **Abstract**: Message-passing iterative decoders for low-density parity-check (LDPC) block codes are known to be subject to decoding failures due to so-called pseudocodewords. These failures can cause the large signal-to-noise ratio (SNR) performance of message-passing iterative decoding to be worse than that predicted by the maximum-likelihood (ML) decoding union bound.

## High-Throughput QC-LDPC Decoders

- **Status**: ✅
- **Reason**: QC-LDPC 고처리량 디코더, min-sum 변형+세미병렬 FPGA 아키텍처 이식 가능(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4806112
- **Type**: journal
- **Published**: June 2009
- **Authors**: Nan Jiang, Kewu Peng, Jian Song +2
- **PDF**: https://ieeexplore.ieee.org/document/4806112
- **Abstract**: High-throughput design approaches for quasi-cyclic (QC) low-density parity-check (LDPC) decoders are presented in this paper. Three novel schemes for the horizontal process in min-sum algorithm and its revisions are derived to reduce design and implementation complexity. The schemes can be directly applied for variant QC codes and easily pipelined to increase the operating frequency of the decoder. Some improvements of the semi-parallel architecture are proposed to enhance throughput performance and hardware efficiency. Employing the proposed approaches, QC-LDPC decoders for Chinese Digital Television Terrestrial Broadcasting (DTTB) standard are implemented using field programmable gate array (FPGA). As shown in the results, the proposed approaches can substantially improve the throughput performance, as well as the throughput-and-hardware tradeoff, of decoders with semi-parallel architecture.

## Eliminating small stopping sets in irregular low-density parity-check codes

- **Status**: ✅
- **Reason**: irregular LDPC의 small stopping set 제거 - check node 추가로 error floor 개선, 코드설계 기법 이식 가능(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5090428
- **Type**: journal
- **Published**: June 2009
- **Authors**: Xiaopeng Jiao, Jianjun Mu, Jing Song +1
- **PDF**: https://ieeexplore.ieee.org/document/5090428
- **Abstract**: We present a novel scheme to eliminate small stopping sets in irregular low-density parity-check (LDPC) codes. By adding several new check nodes and having their edges connected to small stopping sets in the original code, the improved code decreases the number of small stopping sets efficiently. Simulation results show that the proposed scheme decreases the frame error rate (FER) significantly in the error floor region, whereas having almost the same rate as the original code.

## Error rate estimation of low-density parity-check codes on binary symmetric channels using cycle enumeration

- **Status**: ✅
- **Reason**: Tanner 그래프 짧은 사이클 열거로 BSC 하 LDPC error floor/FER 추정, 코드설계·사이클제거 기법(E)으로 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5089484
- **Type**: journal
- **Published**: June 2009
- **Authors**: Hua Xiao, Amir H. Banihashemi
- **PDF**: https://ieeexplore.ieee.org/document/5089484
- **Abstract**: The performance of low-density parity-check (LDPC) codes decoded by hard-decision iterative decoding algorithms can be accurately estimated if the weight J and the number |EJ| of the smallest error patterns that cannot be corrected by the decoder are known. To obtain J and |EJ|, one would need to perform the direct enumeration of error patterns with weight i les J. The complexity of enumeration increases exponentially with J, essentially as nJ, where n is the code block length. This limits the application of direct enumeration to codes with small n and J. In this letter, we approximate J and |EJ | by enumerating and testing the error patterns that are subsets of short cycles in the code's Tanner graph. This reduces the computational complexity by several orders of magnitude compared to direct enumeration, making it possible to estimate the error rates for almost any practical LDPC code. To obtain the error rate estimates, we propose an algorithm that progressively improves the estimates as larger cycles are enumerated. Through a number of examples, we demonstrate that the proposed method can accurately estimate both the bit error rate (BER) and the frame error rate (FER) of regular and irregular LDPC codes decoded by a variety of hard-decision iterative decoding algorithms.

## Low-floor decoders for LDPC codes

- **Status**: ✅
- **Reason**: trapping set 식별 기반 low-floor SPA 디코더 3종(bi-mode/bit-pinning/generalized-LDPC), NAND LDPC 디코더에 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5089505
- **Type**: journal
- **Published**: June 2009
- **Authors**: Yang Han, William E. Ryan
- **PDF**: https://ieeexplore.ieee.org/document/5089505
- **Abstract**: One of the most significant impediments to the use of LDPC codes in many communication and storage systems is the error-rate floor phenomenon associated with their iterative decoders. The error floor has been attributed to certain subgraphs of an LDPC code's Tanner graph induced by so-called trapping sets. We show in this paper that once we identify the trapping sets of an LDPC code of interest, a sum-product algorithm (SPA) decoder can be custom-designed to yield floors that are orders of magnitude lower than floors of the the conventional SPA decoder. We present three classes of such decoders: (1) a bi-mode decoder, (2) a bit-pinning decoder which utilizes one or more outer algebraic codes, and (3) three generalized-LDPC decoders. We demonstrate the effectiveness of these decoders for two codes, the rate-1/2 (2640,1320) Margulis code which is notorious for its floors and a rate-0.3 (640,192) quasi-cyclic code which has been devised for this study. Although the paper focuses on these two codes, the decoder design techniques presented are fully generalizable to any LDPC code.

## Toward low LDPC-code floors: a case study

- **Status**: ✅
- **Reason**: LDPC error floor 저감 - 코드/디코더 수정 및 outer code 적용 기법, FPGA 시뮬, NAND ECC error floor에 이식 가능(C/E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5089487
- **Type**: journal
- **Published**: June 2009
- **Authors**: Yifei Zhang, William E. Ryan
- **PDF**: https://ieeexplore.ieee.org/document/5089487
- **Abstract**: While LDPC codes have been widely acclaimed in recent years for their near-capacity performance, they have not found their way into many important applications. For some cases, this is due to their increased decoding complexity relative to the classical coding techniques. For other cases, this is due to their inability to reach very low bit error rates (e.g., 10-12) at low signal-to-noise ratios (SNRs), a consequence of the error rate floor phenomenon associated with iterative LDPC decoders. In the present paper, we make strides in the low-floor problem by identifying the weaknesses of the code under study and applying compensatory counter-measures. These counter-measures include: modifying the code itself, modifying the decoder, or adding a properly designed outer algebraic code. Our results demonstrate that each of these techniques can successfully lower an LDPC code's floor, and that, for the code under study, an outer BCH code appears to be particularly effective. All of our results are based on FPGA decoder simulations and so they are reliable and repeatable.

## Finite-Precision Analysis of Demappers and Decoders for LDPC-Coded M-QAM Systems

- **Status**: ✅
- **Reason**: LDPC 디코더/수신샘플 유한정밀도 양자화 설계, NAND LLR 양자화에 직접 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4895676
- **Type**: journal
- **Published**: June 2009
- **Authors**: Marco Baldi, Franco Chiaraluce, Giovanni Cancellieri
- **PDF**: https://ieeexplore.ieee.org/document/4895676
- **Abstract**: LDPC codes are state-of-art error correcting codes, included in several standards for broadcast transmissions. Iterative soft-decision decoding algorithms for LDPC codes reach excellent error correction capability; their performance, however, is strongly affected by finite-precision issues in the representation of inner variables. Great attention has been paid, in recent literature, to the topic of quantization for LDPC decoders, but mostly focusing on binary modulations and analysing finite precision effects in a disaggregrated manner, i.e., considering separately each block of the receiver. Modern telecommunication standards, instead, often adopt high order modulation schemes, e.g. M-QAM, with the aim to achieve large spectral efficiency. This puts additional quantization problems, that have been poorly debated in previous literature. This paper discusses the choice of suitable quantization characteristics for both the decoder messages and the received samples in LDPC-coded systems using M-QAM schemes. The analysis involves also the demapper block, that provides initial likelihood values for the decoder, by relating its quantization strategy with that of the decoder. A new demapper version, based on approximate expressions, is also presented, that introduces a slight deviation from the ideal case but yields a low complexity hardware implementation.

## Radiation Tolerance Techniques for a 1.6 Gb/s, 8 K and 4 K Low-Density Parity-Check Encoder

- **Status**: ✅
- **Reason**: 고처리율 LDPC 인코더 CMOS 구현 HW 아키텍처(D), 방사선 내성 부분은 NAND 무관하나 인코더 HW 자체는 이식성 있음
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:4982883
- **Type**: journal
- **Published**: June 2009
- **Authors**: Sterling R. Whitaker, Lowell H. Miles, Jody W. Gambles +4
- **PDF**: https://ieeexplore.ieee.org/document/4982883
- **Abstract**: A multiple node upset tolerant, 1.6 Gb/s (8158, 7136) and (4088, 3360) low-density parity-check encoder was implemented in a five-metal, 0.25 mum CMOS process. Temporal separation coupled with single-event radiation tolerant flip-flops was used to harden the data path. A reduced sensitive cross-section combinational logic structure was used to harden the custom multiply accumulate blocks. This circuit structure is composed of a dual-rail NMOS-only pass-transistor network driving a cross coupled output buffer. By adding the output buffer section, only a small region of the buffer itself is vulnerable for propagation of a single-event transient. Single-event upset immunity with a linear energy transfer threshold of greater than 33 MeVldrcm2/mg and a saturation cross-section of just 0.075 mum2/bit was achieved for the 4 K encoder. A linear energy transfer threshold of greater than 17 MeVldrcm2/mg with a saturation cross-section of just 0.3 mu m2/bit was achieved for the 8 K encoder. This results in a CREME96 expected mean time between failure of 1700 years for a geosynchronous orbit. Multiple node upsets as a problem increases as smaller geometry processes are used for space electronics. A mathematical basis for this reduced cross-section, multiple upset combinational logic design method is presented.

## Iterative decoding algorithms of LDPC codes using TAP approach

- **Status**: ✅
- **Reason**: 통계물리 TAP 접근으로 LLR-BP/BP-based 디코딩 알고리즘 유도 - 이식 가능 디코더 기법(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5307067
- **Type**: conference
- **Published**: 23-26 June
- **Authors**: Manel Abdelhedi, Omessaad Hamdi, Ammar Bouallegue
- **PDF**: https://ieeexplore.ieee.org/document/5307067
- **Abstract**: Low-density parity-check (LDPC) codes are based on random construction. Because of this randomness, it is not easy to analyze them with the traditional methods of communication theory. N.Sourlas [6] was the first to point out that LDPC codes have a similarity to Ising spin systems in statistical physics. Besides, it has been shown that the Belief-Propagation algorithm, the decoding algorithm of LDPC codes, is equivalent to the Thouless-Anderson-Palmer(TAP) [9] approach. In this paper, we develop the log-likelihood ratios-Belief Propagation (LLR-BP) and the BP-Based decoding algorithms with the TAP approach.

## A 47 Gb/s LDPC decoder with improved low error rate performance

- **Status**: ✅
- **Reason**: (2048,1723) RS-LDPC 병렬 디코더 칩, 2단 디코딩으로 error floor 10^-14까지 저감 — 이식 가능 HW/디코더(D/C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5205323
- **Type**: conference
- **Published**: 16-18 June
- **Authors**: Zhengya Zhang, Venkat Anantharam, Martin J. Wainwright +1
- **PDF**: https://ieeexplore.ieee.org/document/5205323
- **Abstract**: A parallel low-density parity-check (LDPC) decoder is designed for the (2048,1723) Reed-Solomon-based LDPC (RS-LDPC) code suitable for 10GBASE-T Ethernet. A two-step decoding scheme lowers the error floor to a 10−14 BER. The decoder architecture is optimized for area, power, and high throughput. The resulting 5.35 mm2, 65nm CMOS chip achieves a decoding throughput of 47.7 Gb/s. With scaled frequency and voltage, the chip delivers a 6.67 Gb/s throughput while dissipating 144 mW of power.

## Performance Analysis of Verification-Based Decoding for Packet-Based LDPC Codes over Binary Symmetric Channel

- **Status**: ✅
- **Reason**: 패킷기반 바이너리 LDPC의 verification-based 디코더 성능분석(false verification 고려), 이식 가능 디코더 알고리즘(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5199318
- **Type**: conference
- **Published**: 14-18 June
- **Authors**: B. Zhu, D. Huang, S. Nordholm
- **PDF**: https://ieeexplore.ieee.org/document/5199318
- **Abstract**: In this paper, we propose a statistical model to analyze the performance of verification-based algorithm (VA) for packet-based low-density parity-check (LDPC) codes over binary symmetric channel (BSC). In contrast to the analysis of VA in the literature, we propose to take the false verification into consideration. For a given ensemble of LDPC codes and channel parameters, the proposed analysis model gives an efficient way to find the average performance of packet-based LDPC codes with verification-based decoding. Through numerical results, we find that the proposed method can provide a close estimation of frame error rate (FER) for packet-based LDPC codes with verification- based decoding over BSC for all crossover probabilities of practical interests.

## Design and Analysis of E² RC Codes Using EXIT Chart

- **Status**: ✅
- **Reason**: E2RC rate-compatible irregular LDPC 코드 설계+EXIT/LP 최적화, 바이너리 LDPC 코드설계(E) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5198897
- **Type**: conference
- **Published**: 14-18 June
- **Authors**: C. Shi, A. Ramamoorthy
- **PDF**: https://ieeexplore.ieee.org/document/5198897
- **Abstract**: We present the design and analysis of a family of codes based on the efflciently-encodable rate-compatible irregular LDPC codes (E2RC codes) introduced by Kim, Ramamoorthy and Mclaughlin '06. The basic idea is to utilize the structured parity part (of the parity check matrix) of E2RC codes and design optimal degree distributions for the systematic part based on EXIT chart analysis. In this work, we propose a new technique for computing EXIT functions of the structured parity part without resorting to Monte Carlo simulations. Our method provides smoother EXIT functions in substantially lesser time. Furthermore, we pose and solve the problem of designing good codes using linear programming. Next, we consider the performance of rate-compatible codes under puncturing using EXIT charts. Finally, we propose joint optimization of our codes at any specified code rate(s) which has not been explored in previous design of rate-compatible punctured codes.

## Evaluation of the Extremely Low Block Error Rate of Irregular LDPC Codes

- **Status**: ✅
- **Reason**: irregular LDPC의 trapping-set 기반 importance sampling으로 error floor/BLER 평가, error floor 분석기법(E) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5199011
- **Type**: conference
- **Published**: 14-18 June
- **Authors**: X. Zheng, F. C. M. Lau, C. K. Tse +2
- **PDF**: https://ieeexplore.ieee.org/document/5199011
- **Abstract**: In this paper, we attempt to evaluate irregular LDPC code performance at the high SNR region using the importance sampling (IS) approach in conjunction with primary- trapping-set identification. Results have indicated that our proposed IS scheme can produce speed-up gains up to 3.9 x 109 times compared with Monte Carlo simulations.

## Joint Message-Passing Symbol-Decoding of LDPC Coded Signals over Partial-Response Channels

- **Status**: ✅
- **Reason**: LDPC+PR 채널 joint detection/decoding SPA, 스토리지(자기기록) 인접 채널이며 부호/채널 그래프 SPA 기법 이식 검토 가치, 애매하여 in
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5199115
- **Type**: conference
- **Published**: 14-18 June
- **Authors**: R. Radhakrishnan, B. Vasic
- **PDF**: https://ieeexplore.ieee.org/document/5199115
- **Abstract**: We consider the problem of joint detection and decoding of low-density parity-check (LDPC) coded signals over partial response (PR) channels. A method to graphically represent the constraints imposed by the channel and the code on the channel output sequence is introduced. This enables the design of a detector and decoder that estimates a posteriori probabilities of noiseless channel output symbols rather than binary channel inputs. By running the sum-product algorithm (SPA) on this graph, a joint decoder is obtained that is shown to perform significantly better than the turbo-equalizer, at the cost of increased computational complexity.

## On Construction of Moderate-Length LDPC Codes over Correlated Erasure Channels

- **Status**: ✅
- **Reason**: correlated erasure 채널용 유한길이 LDPC 코드 구성(MTBL 개선), 바이너리 LDPC 유한길이 코드설계(E) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5199238
- **Type**: conference
- **Published**: 14-18 June
- **Authors**: G. Liva, B. Matuz, Z. Katona +2
- **PDF**: https://ieeexplore.ieee.org/document/5199238
- **Abstract**: The design of moderate-length erasure correcting low-density parity-check (LDPC) codes over correlated erasure channels is considered. Although the asymptotic LDPC code design remains the same as for a memoryless erasure channel, robustness to the channel correlation shall be guaranteed for the finite length LDPC code. This further requirement is of great importance in several wireless communication scenarios where packet erasure correcting codes represent a simple countermeasure for correlated fade events (e.g., in mobile wireless broadcasting services) and where the channel coherence time is often comparable with the code length. In this paper, the maximum tolerable erasure burst length (MTBL) is adopted as a simple metric for measuring the code robustness to the channel correlation. Correspondingly, a further step in the code construction is suggested, consisting of improving the LDPC code MTBL. Numerical results conducted over a Gilbert erasure channel, under both iterative and maximum likelihood decoding, highlight both the importance of the MTBL improvement in the finite-length code construction and the possibility to tightly approach the performance of maximum distance separable codes.

## A Low Complexity Iterative Technique for Soft Decision Decoding of Reed-Solomon Codes

- **Status**: ✅
- **Reason**: RS 부호지만 bit-level BP+확장 이진 패리티검사(저밀도화, 4-cycle 감소) - 부호 비의존적 BP 개선 기법, 바이너리 LDPC BP에 이식 가능(C 예외)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5198625
- **Type**: conference
- **Published**: 14-18 June
- **Authors**: F. Shayegh, M. R. Soleymani
- **PDF**: https://ieeexplore.ieee.org/document/5198625
- **Abstract**: A new iterative soft decision decoding method for Reed-Solomon (RS) codes is proposed. This method is based on bit level belief propagation (BP) decoding. In order to make BP decoding effective for RS codes, we use an extended binary parity check matrix with a lower density and reduced number of 4-cycles compared to the original binary parity check matrix of the code. In our proposed method, we take advantage of the cyclic structure of RS codes. Based on this property, we can apply the belief propagation algorithm on any cyclically shifted version of the received symbols with the same binary parity check matrix. For each shifted version of received symbols, the geometry of the factor graph will change and deterministic errors can be avoided. Our method results in considerable performance improvement of RS codes compared to hard decision decoding. The performance is also superior to some popular soft decision decoding methods.

## Improving the Performance of LP Decoders for Cyclic Codes

- **Status**: ✅
- **Reason**: LP(선형계획) 디코더 성능 개선 기법 - 부호 비의존적 디코더 알고리즘으로 바이너리 LDPC BP에 이식 가능성 있어 애매하면 in (C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5305944
- **Type**: conference
- **Published**: 14-18 June
- **Authors**: M. R. Heidarpour, M. Modarres-Hashemi, M. Khosravifard +1
- **PDF**: https://ieeexplore.ieee.org/document/5305944
- **Abstract**: N/A

## Probabilistic Data Detection for Probe-Based Storage Channels in the Presence of Jitter

- **Status**: ✅
- **Reason**: probe 스토리지 채널 LDPC soft 정보 생성(jitter/noise LLR 분석식), 스토리지 ECC+이식 가능 soft정보/LLR 기법(B/C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5199366
- **Type**: conference
- **Published**: 14-18 June
- **Authors**: H. Pozidis, G. Cherubini
- **PDF**: https://ieeexplore.ieee.org/document/5199366
- **Abstract**: Probe-storage devices employ large arrays of probes to write/read data in parallel in some storage medium. Because of their inherent parallelism and the independence of data retrieved from different probes, these devices lend themselves naturally to low-density parity-check (LDPC) codes and associated soft/iterative decoding techniques. In this paper, a concatenated coding scheme for a particular probe-storage channel is presented that comprises an inner (d, k)-constrained code and an outer LDPC code, and the problem of probabilistic data retrieval for this channel is addressed. In particular, soft information is generated by explicitly accounting for the channel output statistics in the presence of jitter and additive noise, based on derived analytical expressions.

## An Improved Split-Row Threshold Decoding Algorithm for LDPC Codes

- **Status**: ✅
- **Reason**: Split-Row Threshold LDPC 디코딩 알고리즘 개선 - min-sum 변형 디코더, HW 친화적 이식 가능(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5198733
- **Type**: conference
- **Published**: 14-18 June
- **Authors**: T. Mohsenin, D. Truong, B. Baas
- **PDF**: https://ieeexplore.ieee.org/document/5198733
- **Abstract**: We present an improved thresholding LDPC decoding algorithm which outperforms the split-row and original split-row threshold decoders with a small increase in hardware. Simulation results show that the algorithm provides 0.27- 0.50 dB coding gain over split-row, 0.10-0.20 dB over split-row threshold, and is within 0.08-0.13 dB of SPA. Compared with the original threshold algorithm the check node processor's gate count is increased by 3% while total chip area is kept the same.

## Vertex Packing Decoding

- **Status**: ✅
- **Reason**: configuration graph 기반 ML 디코딩+BP 결합으로 LDPC 성능개선하는 부호 비의존 신규 디코더 프레임워크(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5199565
- **Type**: conference
- **Published**: 14-18 June
- **Authors**: M. Lunglmayr, J. Berkmann, M. Huemer
- **PDF**: https://ieeexplore.ieee.org/document/5199565
- **Abstract**: In this work, we present a new framework for developing decoding algorithms for linear block codes. We define a new graphical model, called configuration graph and show that maximum likelihood (ML) sequence decoding can be performed by finding a maximum vertex packing on a configuration graph. We present examples of low-cost decoding algorithms developed using this graphical model and show that remarkable performance improvements can be achieved especially by combining these algorithms with belief propagation (BP) decoding for Low Density Parity Check (LDPC) codes.

## Correcting Suboptimal Metrics in Iterative Decoders

- **Status**: ✅
- **Reason**: 반복디코더 L-value 보정(scaling factor 이론적 일반화) - 부호 비의존적 메시지패싱 보정, LDPC BP에 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5198866
- **Type**: conference
- **Published**: 14-18 June
- **Authors**: A. Alvarado, V. Nunez, L. Szczecinski +1
- **PDF**: https://ieeexplore.ieee.org/document/5198866
- **Abstract**: In this paper the issue of improving the performance of iterative decoders based on sub-optimal calculation of the messages exchanged during iterations (L-values) is addressed. It is well known in the literature that a simple-yet very effective-way to improve the performance of suboptimal iterative decoders is based on applying a scaling factor to the L-values. In this paper, starting with a theoretical model based on the so-called consistency condition of a random variable, we propose a methodology for correcting the L-values that relies only on the distribution of the soft information exchanged in the iterative process. This methodology gives a clear explanation of why the well-known linear scaling factor provides a very good performance. Additionally, the proposed methodology allows us to avoid the exhaustive search required otherwise. Numerical simulations show that for turbo codes the scaling factors found closely follow the optimum values, which translates to a close-to-optimal BER performance. Moreover, for LDPC codes, the proposed methodology produces a better BER performance compared with the known method in the literature.
