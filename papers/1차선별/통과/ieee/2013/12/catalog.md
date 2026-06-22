# IEEE Xplore — 2013-12 (1차선별 통과)


## Lowering Error Floors of Systematic LDPC Codes Using Data Shortening

- **Status**: ✅
- **Reason**: systematic LDPC error floor 저감용 data shortening으로 trapping/stopping set 약화, 이식 가능 코드설계(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6656081
- **Type**: journal
- **Published**: December 2
- **Authors**: Sung-Rae Kim, Dong-Joon Shin
- **PDF**: https://ieeexplore.ieee.org/document/6656081
- **Abstract**: In this paper, data shortening methods for lowering error floors of systematic LDPC codes are proposed. Rather than attempting to analyze trapping (or stopping) sets of a given LDPC code rigorously, we search information bits associated with dominant trapping (or stopping) sets of systematic LDPC codes through simulation under various channels. Then, proper information bits forming dominant trapping (or stopping) sets are selected and known values are assigned to them before encoding to weaken the effect of dominant trapping (or stopping) sets. To decode codewords, fixed known values are assigned to the selected information bits, which gives rise to the disconnection of some edges in dominant trapping (or stopping) sets. Through simulation, it is shown that the proposed schemes result in remarkably better performance, especially at the error floor region, than the base LDPC codes under various channels with negligible loss of code rate.

## A Revolving Iterative Algorithm for Decoding Algebraic Cyclic and Quasi-Cyclic LDPC Codes

- **Status**: ✅
- **Reason**: 대수적 cyclic/QC-LDPC를 작은 부분행렬로 revolving 디코딩해 HW 복잡도·메모리 대폭 감소; 이식 가능 디코더/HW(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6612626
- **Type**: journal
- **Published**: December 2
- **Authors**: Keke Liu, Shu Lin, Khaled Abdel-Ghaffar
- **PDF**: https://ieeexplore.ieee.org/document/6612626
- **Abstract**: Cyclic and quasi-cyclic algebraic LDPC codes constructed based on finite fields, finite geometries, and combinatorial designs can achieve excellent performance in terms of error rate, error floor and rate of decoding convergence with iterative decoding. However, the relatively high density of the parity-check matrix of an algebraic cyclic or quasi-cyclic LDPC code makes the hardware implementation complexity of the decoder quite large, which may be a critical issue in practical applications. This paper presents an effective reduced-complexity algorithm for decoding algebraic cyclic and quasi-cyclic LDPC codes based on the block cyclic structure and cyclic grouping of the rows of their parity-check matrices. The decoding of a code is carried out based on a single small submatrix of the parity-check matrix of the code in a revolving manner. The proposed decoding algorithm significantly reduces the hardware implementation complexity and the size of memory required to store information.

## Comparison of parallelization strategies for min-sum decoding of irregular LDPC codes

- **Status**: ✅
- **Reason**: irregular LDPC min-sum 디코더의 멀티코어/GPU 병렬화 전략 - 이식 가능 HW/병렬화 기법(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:6678903
- **Type**: journal
- **Published**: Dec. 2013
- **Authors**: Hua Xu, Wei Wan, Wei Wang +3
- **PDF**: https://ieeexplore.ieee.org/document/6678903
- **Abstract**: Low-Density Parity-Check (LDPC) codes are powerful error correcting codes. LDPC decoders have been implemented as efficient error correction codes on dedicated VLSI hardware architectures in recent years. This paper describes two strategies to parallelize min-sum decoding of irregular LDPC codes. The first implements min-sum LDPC decoders on multicore platforms using OpenMP, while the other uses the Compute Unified Device Architecture (CUDA) to parallelize LDPC decoding on Graphics Processing Units (GPUs). Empirical studies on data with various scales show that the performance of these decoding processes is improved by these parallel strategies and the GPUs provide more efficient, fast implementation decoder.

## LDPC Codes on Partial Geometries: Construction, Trapping Set Structure, and Puncturing

- **Status**: ✅
- **Reason**: 바이너리 LDPC 부분기하 구성·trapping set 구조·puncturing(코드설계 E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6588899
- **Type**: journal
- **Published**: Dec. 2013
- **Authors**: Qiuju Diao, Ying Yu Tai, Shu Lin +1
- **PDF**: https://ieeexplore.ieee.org/document/6588899
- **Abstract**: Many known constructions of LDPC codes can be placed in a general framework using the notion of partial geometries. Based on this notion, the structure of such LDPC codes can be analyzed using a geometric approach that illuminates important properties of their parity-check matrices. In this approach, trapping sets are represented by subgeometries of the geometry used to construct the code. Based on the incidence relations between lines and points in this geometry, the structure of trapping sets is investigated. On the other hand, it is shown that removing a subgeometry corresponding to a trapping set gives a punctured matrix which can be used as a parity-check matrix of an LDPC code. This relates trapping sets, represented by subgeometries, and punctured matrices, represented by the residual geometries. The null spaces of these punctured matrices are LDPC codes which inherit many of the good structural properties of the original code. Hence, new LDPC codes, with various lengths and rates, can be obtained by puncturing an LDPC code constructed based on a partial geometry. Furthermore, these punctured matrices and codes can be used in a two-phase decoding scheme to correct combinations of errors and erasures.

## Decomposition Methods for Large Scale LP Decoding

- **Status**: ✅
- **Reason**: ADMM 기반 LP 디코딩, 병렬 message-passing·error floor 제거, 이식 가능 디코더(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6595057
- **Type**: journal
- **Published**: Dec. 2013
- **Authors**: Siddharth Barman, Xishuo Liu, Stark C. Draper +1
- **PDF**: https://ieeexplore.ieee.org/document/6595057
- **Abstract**: When binary linear error-correcting codes are used over symmetric channels, a relaxed version of the maximum likelihood decoding problem can be stated as a linear program (LP). This LP decoder can be used to decode error-correcting codes at bit-error-rates comparable to state-of-the-art belief propagation (BP) decoders, but with significantly stronger theoretical guarantees. However, LP decoding when implemented with standard LP solvers does not easily scale to the block lengths of modern error correcting codes. In this paper, we draw on decomposition methods from optimization theory, specifically the alternating direction method of multipliers (ADMM), to develop efficient distributed algorithms for LP decoding. The key enabling technical result is a “two-slice” characterization of the parity polytope, the polytope formed by taking the convex hull of all codewords of the single parity check code. This new characterization simplifies the representation of points in the polytope. Using this simplification, we develop an efficient algorithm for Euclidean norm projection onto the parity polytope. This projection is required by the ADMM decoder and its solution allows us to use LP decoding, with all its theoretical guarantees, to decode large-scale error correcting codes efficiently. We present numerical results for LDPC codes of lengths more than 1000. The waterfall region of LP decoding is seen to initiate at a slightly higher SNR than for sum-product BP, however an error floor is not observed for LP decoding, which is not the case for BP. Our implementation of LP decoding using the ADMM executes as fast as our baseline sum-product BP decoder, is fully parallelizable, and can be seen to implement a type of message-passing with a particularly simple schedule.

## Spatially Coupled Ensembles Universally Achieve Capacity Under Belief Propagation

- **Status**: ✅
- **Reason**: 바이너리 SC-LDPC 앙상블 BP 임계·capacity, 코드설계(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6589171
- **Type**: journal
- **Published**: Dec. 2013
- **Authors**: Shrinivas Kudekar, Tom Richardson, Rüdiger L. Urbanke
- **PDF**: https://ieeexplore.ieee.org/document/6589171
- **Abstract**: We investigate spatially coupled code ensembles. For transmission over the binary erasure channel, it was recently shown that spatial coupling increases the belief propagation threshold of the ensemble to essentially the maximum a priori threshold of the underlying component ensemble. This explains why convolutional LDPC ensembles, originally introduced by Felström and Zigangirov, perform so well over this channel. We show that the equivalent result holds true for transmission over general binary-input memoryless output-symmetric channels. More precisely, given a desired error probability and a gap to capacity, we can construct a spatially coupled ensemble that fulfills these constraints universally on this class of channels under belief propagation decoding. In fact, most codes in this ensemble have this property. The quantifier universal refers to the single ensemble/code that is good for all channels but we assume that the channel is known at the receiver. The key technical result is a proof that, under belief-propagation decoding, spatially coupled ensembles achieve essentially the area threshold of the underlying uncoupled ensemble. We conclude by discussing some interesting open problems.

## A new stopping criterion for fast low-density parity-check decoders

- **Status**: ✅
- **Reason**: APP 증가성 이용한 T-tolerance 조기종료 정지기준. 비이진 대상이나 정지기준 자체는 바이너리 LDPC BP에 이식 가능(C), 애매하여 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6831642
- **Type**: conference
- **Published**: 9-13 Dec. 
- **Authors**: Tian Xia, Hsiao-Chun Wu, Scott C.-H. Huang
- **PDF**: https://ieeexplore.ieee.org/document/6831642
- **Abstract**: Nonbiliary low-density parity-check (LDPC) codes can lead to excellent error performance while the codewords are of short or moderate length. However, the high decoding complexity of nonbiliary LDPC codes inevitably depreciates their practical values. The computational bottleneck arises from the check node processing in the iterative message passing (MP) algorithms which terminate when either all parity checks are satisfied or the maximum iteration number is reached. We have observed that for undecodable blocks, the MP algorithms always run up to the maximum iteration limit and therefore cannot generate the correct codeword. Thus, it would be better to terminate the algorithms early so as to save the unnecessary computational time and reduce the extra power consumption when undecodable blocks are experienced. In this paper, we propose a new T-tolerance stopping criterion for LDPC decoders by exploiting the fact that the total a posteriori probability (APP) should increase as the iteration number grows. Simulation results demonstrate that our proposed new T-tolerance criterion can greatly reduce the average iteration number (complexity) while restricting the decoding performance degradation within 0.1 dB in low bit-energy-to-noise ratio scenarios.

## Min-Sum-based decoders running on noisy hardware

- **Status**: ✅
- **Reason**: 노이즈 HW에서 동작하는 min-sum 디코더 분석+노이지 밀도진화. min-sum 변형 디코더 견고성(C)이라 NAND HW 신뢰성/양자화 분석에 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6831348
- **Type**: conference
- **Published**: 9-13 Dec. 
- **Authors**: Christiane Kameni Ngassa, Valentin Savin, David Declercq
- **PDF**: https://ieeexplore.ieee.org/document/6831348
- **Abstract**: This paper deals with Low-Density Parity-Check decoders running on noisy hardware. This represents an unconventional paradigm in communication theory, since it is traditionally assumed that the error correction decoder operates on error-free devices and the randomness (in the form of noise and/or errors) exists only in the transmission channel. However, with the advent of nanoelectronics, it starts to be widely accepted that the future generations of circuits and systems will need to reliability compute and solve statistical inferences, by making use of unreliable “noisy” components. It is then critical to properly evaluate the robustness of the existing decoders in the presence of an additional source of noise at the circuit level. To this end, we first introduce a new error model approach and carry out the “noisy” density evolution analysis of the fixed-point Min-Sum decoding. Then, for different parameters of the noisy components of the decoder, we determine the range of the signal-to-noise ratio values for which the decoder is able to achieve a target bit error rate performance. Finally, we evaluate the finite-length performance of the Min-Sum and two other Min-Sum-based decoders running on noisy hardware.

## High throughput low latency LDPC decoding on GPU for SDR systems

- **Status**: ✅
- **Reason**: GPU 병렬 LDPC 디코더 최적화(메모리 coalescing, 비동기 전송 등) — 이식 가능 디코더/HW 기법(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6737137
- **Type**: conference
- **Published**: 3-5 Dec. 2
- **Authors**: Guohui Wang, Michael Wu, Bei Yin +1
- **PDF**: https://ieeexplore.ieee.org/document/6737137
- **Abstract**: In this paper, we present a high throughput and low latency LDPC (low-density parity-check) decoder implementation on GPUs (graphics processing units). The existing GPU-based LDPC decoder implementations suffer from low throughput and long latency, which prevent them from being used in practical SDR (software-defined radio) systems. To overcome this problem, we present optimization techniques for a parallel LDPC decoder including algorithm optimization, fully coalesced memory access, asynchronous data transfer and multi-stream concurrent kernel execution for modern GPU architectures. Experimental results demonstrate that the proposed LDPC decoder achieves 316 Mbps (at 10 iterations) peak throughput on a single GPU. The decoding latency, which is much lower than that of the state of the art, varies from 0.207 ms to 1.266 ms for different throughput requirements from 62.5 Mbps to 304.16 Mbps. When using four GPUs concurrently, we achieve an aggregate peak throughput of 1.25 Gbps (at 10 iterations).

## Open the Gates: Using High-level Synthesis towards programmable LDPC decoders on FPGAs

- **Status**: ✅
- **Reason**: 프로그래머블/유연 바이너리 LDPC 디코더의 FPGA HW 구현 전략 — 이식 가능 HW 아키텍처(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:6737141
- **Type**: conference
- **Published**: 3-5 Dec. 2
- **Authors**: Frederico Pratas, Joao Andrade, Gabriel Falcao +2
- **PDF**: https://ieeexplore.ieee.org/document/6737141
- **Abstract**: State-of-the-art decoders for LDPC codes adopted by several digital communication standards require a significant amount of hardware resources to achieve the desired high throughput performance. With technology scaling below the 22nm and with billions of transistors available per chip/device, the development cost and complexity of such designs represent an increasing challenge for hardware designers tackling these communication algorithms. This paper proposes a new strategy for developing flexible and totally programmable long-length LDPC decoders to target execution on FPGA devices. We exploit Maxeler's Java-based technology to describe the LDPC decoder architecture. We compare the performance of this approach with state-of-the-art parallel computing architectures and show that for the most complex family of binary LDPC codes, real-time throughputs in the order of Mbit/s can be achieved with much lower development effort than imposed by RTL descriptions, and with tremendous power savings compared to the powerful GPUs.

## Low overhead correction scheme for unreliable LDPC buffering

- **Status**: ✅
- **Reason**: 전압 오버스케일링 하 LDPC 디코더 내부메모리 신뢰성 보정(defect map) HW 기법 — 이식 가능 HW(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:6736979
- **Type**: conference
- **Published**: 3-5 Dec. 2
- **Authors**: Amr M. A. Hussien, Wael M. Elsharkasy, Ahmed M. Eltawil +2
- **PDF**: https://ieeexplore.ieee.org/document/6736979
- **Abstract**: Aggressive voltage overscaling (VOS) has been recently adopted to reduce the power consumption of embedded memories. While this affects reliability, several techniques have been developed to achieve reliable operation under aggressive VOS. In this paper, we present a comprehensive power-performance study of LDPC decoders enabling aggressive VOS to internal memories. We propose a correction scheme based on defect map insertion that maintains reliable LDPC decoder under aggressive VOS. The proposed scheme maintains the LDPC decoder performance while achieving a power saving of up to 21%.

## A processor based multi-standard low-power LDPC engine for multi-Gbps wireless communication

- **Status**: ✅
- **Reason**: 멀티표준 저전력 LDPC 디코더 ASIP 엔진, 레이어 병렬화 트레이드오프 — 이식 가능 HW 아키텍처(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:6737136
- **Type**: conference
- **Published**: 3-5 Dec. 2
- **Authors**: Meng Li, Frederik Naessens, Min Li +5
- **PDF**: https://ieeexplore.ieee.org/document/6737136
- **Abstract**: The design of multi-Gbps LDPC decoder has become a hot topic in recent years as the demand of the transformation towards 4G. In this paper, we describe an energy efficient multi-Gbps LDPC decoder engine based on ASIP using Target tool suite. The ASIP core can be configured as half-layer paralleled or quarter-layer paralleled decoding, which offers a good trade-off between the throughput and power/area efficiency when compared to the state-of-art fully paralleled ASIC based multi-Gbps LDPC decoder. When the ASIP core is instantiated for 802.11ad, it achieved a throughput up to 5.3 Gbps at 5 iterations with a latency of less than 150 ns and a record energy efficiency of 4.3 pJ/bit/iteration in 40G TSMC technology for the coding rate 13/16, showing to be competitive versus published ASIC solutions.

## A new decoding algorithm of LDPC for COFDM-MIMO system

- **Status**: ✅
- **Reason**: COFDM-MIMO용 LDPC 신규 디코딩 알고리즘(반복횟수 감소) 제시 — 부호 비의존 BP 개선 가능성(C), 애매하여 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6885263
- **Type**: conference
- **Published**: 20-22 Dec.
- **Authors**: Baojian Gao, Luwei Hao, Qian Wu +3
- **PDF**: https://ieeexplore.ieee.org/document/6885263
- **Abstract**: The features of the received signal in the LDPC-COFDM MIMO system with space-time block coding(STBC) was analyzed in this paper, the signal estimate of the received signal obeys Gaussian distribution and it has nothing to do with the statistical distribution of the specific channel. According to the features of the received signal, a new decoding algorithm of LDPC for COFDM-MIMO system is proposed. The performance of the algorithm is detailed analyzed in the case of different bit rates and compared with other decoding schemes. The simulation results show that the algorithm can greatly reduce the number of iterations, and improve the decoding speed. Furthermore, the algorithm has the good decoding performances and the adaptability of different code rates.

## Effects of base matrices on iterative decoding performance of irregular QC-LDPC codes

- **Status**: ✅
- **Reason**: protograph EXIT chart로 QC-LDPC base matrix가 waterfall/error floor에 미치는 영향 분석·개선 base matrix 설계 (E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6723960
- **Type**: conference
- **Published**: 16-18 Dec.
- **Authors**: Sheng Tong, Qinghua Guo, Jiangtao Xi +1
- **PDF**: https://ieeexplore.ieee.org/document/6723960
- **Abstract**: The edge connections in factor graphs of quasi-cyclic (QC) LDPC codes, which affect their iterative decoding performance, are determined by their base matrices. In this paper, the effects of base matrices on the iterative decoding performance of QC-LDPC codes are investigated by using the recently proposed EXIT chart tool for protograph LDPC codes. Extensive experiments have been carried out and iterative decoding thresholds of QC-LDPC codes with the same degree distribution pair but base matrices having different structures and different dimensions have been obtained and compared. Experimental results show that 1) the base matrix structure affects not only the waterfall performance but also the error floor performance; base matrices having good waterfall performance may exhibit rather poor error floor performance. 2) by increasing the dimensions of base matrices for a given degree distribution, the threshold means are reduced while the ranges of threshold distributions are increased. 3) similar to the case of detailed represented LDPC codes, base matrices with sufficiently large dimensions may have thresholds surpassing the conventional ensemble threshold with the same degree distribution pair. Moreover, as a concrete example, an improved base matrix is designed for a rate-1/2 WiMax LDPC code.

## A reduced-complexity successive-cancellation decoding algorithm for polar codes

- **Status**: ✅
- **Reason**: polar SC 디코더지만 Gallager LDPC update rule을 piecewise-linear로 근사하는 노드연산 기법은 부호 비의존적이고 바이너리 LDPC BP에 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6743858
- **Type**: conference
- **Published**: 16-18 Dec.
- **Authors**: Chao Xing, Bei Wang, Shengmei Zhao
- **PDF**: https://ieeexplore.ieee.org/document/6743858
- **Abstract**: Polar codes are codes which provably achieve the capacity of arbitrary symmetric binary-input channels with the complexity of encoders and decoders O(N log N), where N is the code block-length. In the paper, we will focus on a lower complexity implementation of decoding algorithm in the log-likelihood ratio domain. We use the update rule proposed by Gallager in the decoding algorithm of low density parity check (LDPC) codes to replace the node update rules used in successive cancellation (SC) algorithm for polar codes. To simplify the logarithmic and the exponential operations in the Gallager's approach node updates rule for polar codes, we further utilize a piece-wise linear algorithm to approximate the involution transform function, where the piece-wise linear algorithm only uses multiplication and addition operation. It has resulted in a reduced complexity SC decoding algorithm for polar codes. The numerical simulations show that our proposed SC algorithm (Piece-wise approx.) has a lower implementation complexity for polar code decoding, but at the cost about 0.7dB degradation in the bit-error-rate (BER) performance in comparison with the SC algorithm proposed by Arikan when the BER is 10-5. The proposed SC algorithm (Piece-wise approx.) is a tradeoff between the error performance and the decoding complexity.

## Reliability Adjustment Weighted Bit-Flipping Decoding for Low-Density Parity-Check Codes

- **Status**: ✅
- **Reason**: 신뢰도조정 가중 비트플리핑(RA-WBF) 신규 디코딩 알고리즘 - 바이너리 LDPC에 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6746512
- **Type**: conference
- **Published**: 14-15 Dec.
- **Authors**: Shengpei Ding, Jiongcheng Li, Henghui Xiao +1
- **PDF**: https://ieeexplore.ieee.org/document/6746512
- **Abstract**: In this paper, we propose reliability adjustment weighted bit-flipping (RA-WBF) decoding algorithm for low density parity-check (LDPC) codes. By adjusting the reliability of received symbols during iterative decoding, the proposed algorithm can offer better tradeoff between performance, convergence speed and computational complexity. Furthermore, this improvement can easily be extended to other variations of weighted bit-flipping decoding algorithm and obtain noticeable improvement in error performance. Simulation results are shown to verify our conclusions.

## High-throughput dual-shift stochastic-detection quasi-cyclic LDPC decoder

- **Status**: ✅
- **Reason**: NVM 스토리지 타겟 QC-LDPC dual-shift stochastic-detection 디코더, 신규 처리량 향상 디코더/HW 기법(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6782970
- **Type**: conference
- **Published**: 10-13 Dec.
- **Authors**: Melvin Heng Li Lim, Wang Ling Goh
- **PDF**: https://ieeexplore.ieee.org/document/6782970
- **Abstract**: Driven by its renowned near-capacity performance over a wide spectrum of channels, the capitalization of quasi-cyclic low-density parity-check (QC-LDPC) codes is irrefutably the focal point of research and solution to virtually all communication systems of the next generation. Steered towards non-volatile memory (NVM) storage applications, we introduce a modernistic approach to LDPC decoding in this paper, known as the dual-shift stochastic-detection (DSSD). Weaving two novel ideas: dual-shift cyclic generation and stochastic-detection of local minima, our proposed DSSD decoder achieves throughput gains (∼ 300%) by minimizing its overall computational delay and maximizing its operational frequency. Along with the amalgamation of our spearheading mirror-paradigm, the DSSD QC-LDPC decoder acquires yet another dimension of gain in throughput while relinquishing a cluster of its address generation counters, which elicits a wide expanse for its application.

## An LDPC decoder with SNR information

- **Status**: ✅
- **Reason**: IEEE 802.11n LDPC 부분병렬 VLSI 디코더, min-sum-correct CNU/BNU 재정렬+early termination+PCM 재정렬 등 이식 가능 HW 기법(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:6782886
- **Type**: conference
- **Published**: 10-13 Dec.
- **Authors**: Kai-Jiun Yang, Shang-Ho Tsai, Heng-Chang Hsu
- **PDF**: https://ieeexplore.ieee.org/document/6782886
- **Abstract**: In this work an LDPC decoder which complies with IEEE 802.11n is proposed and implemented. The code rate is 1/2 and the code length is 648. We used partially parallel structure to reduce the area. Additionally the SNR information is applied to improve the BER performance. Moreover the CNU and the BNU in the min-sum-correct algorithm were reordered so that the hardware complexity can be reduced, and early termination can be achieved at the first iteration. Furthermore the parity check matrix is reordered such that the latency of each iteration is reduced by 1/3. The proposed LDPC decoder can reach a throughput of 37 ~ 319Mbps with a core area of 5.3mm2 and power consumption 224mW in a TSMC 90nm process.

## Linearly-encodable rate-compatible punctured LDPC codes with low error floor

- **Status**: ✅
- **Reason**: 선형 인코딩 rate-compatible punctured LDPC, layered DE+node-connection으로 error floor 저감 바이너리 코드설계 기법(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6782968
- **Type**: conference
- **Published**: 10-13 Dec.
- **Authors**: Zhiyong He, Yong Liang Guan, Chee Cheon Chui +3
- **PDF**: https://ieeexplore.ieee.org/document/6782968
- **Abstract**: We propose a class of rate-compatible (RC) low-density parity-check (LDPC) codes that has linear encoding complexity and low error floor. To ensure linear encoding, a deterministic form for the parity part of the mother parity-check matrix is used. To guarantee good performances in the waterfall region for a wide range of code rates, a layered density evolution algorithm is developed to obtain the degree distributions. Then, a layered node-connection algorithm is proposed to lower the error floor by increasing the values of extrinsic-message degrees of the codes. Simulation results show that no error floor is observed at a frame error rate of 10-5 for the proposed RC code.
