# IEEE Xplore — 2009-08 (1차선별 통과)


## On asymptotic ensemble weight enumerators of LDPC-like codes

- **Status**: ✅
- **Reason**: E. LDPC ensemble weight enumerator로 error floor 좌우 차수분포 최적화 조건 도출; 결론은 바이너리 LDPC error floor 설계에 직접 적용 (nonbinary는 확장일 뿐)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5174519
- **Type**: journal
- **Published**: August 200
- **Authors**: Chung-Li Wang, Marc P.C. Fossorier
- **PDF**: https://ieeexplore.ieee.org/document/5174519
- **Abstract**: For LDPC-like codes such as LDPC, GLDPC, and DGLDPC codes, it is well known that the error floor can be caused by the codewords of small weights or stopping sets of small sizes. In this paper, we investigate the computation of asymptotic weight enumerators such that it becomes a convenient tool to determine a good distribution of code ensembles. In addition, by analyzing the first order approximation, we derive a condition to obtain a negative asymptotic growth rate of the codewords of small linear-sized weights, which is an important constraint for distribution optimization. Also the weight enumerators of turbo and repeat-accumulate codes are investigated. Furthermore, we extend our results to nonbinary DGLDPC codes. Generalization to N-layer and convolutional code based LDPC-like codes are also developed.

## Shortening for irregular QC-LDPC codes

- **Status**: ✅
- **Reason**: irregular QC-LDPC shortening 알고리즘-바이너리 코드설계(E) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5200902
- **Type**: journal
- **Published**: August 200
- **Authors**: Xiaojian Liu, Xiaofu Wu, Chunming Zhao
- **PDF**: https://ieeexplore.ieee.org/document/5200902
- **Abstract**: Shortening is a technique to obtain codes of shorter length and lower rate from a given LDPC code by putting infinite reliability on some variable nodes, whose positions are assumed to be available to both encoder and decoder. In this paper, we propose a shortening algorithm suitable for irregular QC-LDPC codes. The efficiency of the proposed algorithm is verified by both theoretical analysis and simulation.

## Geometrically-structured maximum-girth LDPC block and convolutional codes

- **Status**: ✅
- **Reason**: E. 신규 max-girth 기하구조 QC-LDPC(column-weight-2) 구성 알고리즘, girth 16/24, RPEG 대비 우수 — 바이너리 코드설계 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5174513
- **Type**: journal
- **Published**: August 200
- **Authors**: Morteza Esmaeili, Mohammad Gholami
- **PDF**: https://ieeexplore.ieee.org/document/5174513
- **Abstract**: Four classes of maximum-girth geometrically structured column-weight-two regular quasi-cyclic (QC) low-density parity-check (LDPC) codes are introduced. Two classes of these codes, referred to as Type-I and Type-II codes, are with row-weights 4 and 3, and maximum girths 16 and 24, respectively. The idea behind the construction of these two classes of codes, with rates at least 1/2 and 1/3, is slightly generalized to obtain two classes of variable-high-rate codes, referred to as Type-III1 and Type-III2 codes, with maximum girth 20 and 16, respectively. A low-complexity deterministic algorithm for constructing these four classes of codes is given. The algorithm generates maximum-girth Type-I and Type-II codes with almost arbitrary length eta not less than 216 and 243, respectively. The output of the algorithm substantially improves on some of the previously best known codes constructed using a randomized progressive edge-growth (RPEG) algorithm. For instance, we have rate-0.71 Type-III1 codes of lengths 308 and 728 with girths 10 and 12, respectively, versus the code lengths 385 and 840 obtained by the RPEG algorithm. Simulation results on AWGN channel confirm that, from BER performance perspective, the constructed LDPC codes are superior to the column-weight-two LDPC codes constructed by the previously reported methods. The generator matrix G(D) of the convolutional codes associated with Type-I and Type-II codes is given. The free distance dfree of such a convolutional code is equal to the minimum distance of the corresponding QC block code.

## Predicting error floors of structured LDPC codes: deterministic bounds and estimates

- **Status**: ✅
- **Reason**: E. 구조화 LDPC absorbing set 기반 error floor 결정론적 예측 + importance sampling; array-based 바이너리 LDPC error floor 설계 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5174520
- **Type**: journal
- **Published**: August 200
- **Authors**: L. Dolecek, P. Lee, Zhengya Zhang +3
- **PDF**: https://ieeexplore.ieee.org/document/5174520
- **Abstract**: The error-correcting performance of low-density parity check (LDPC) codes, when decoded using practical iterative decoding algorithms, is known to be close to Shannon limits for codes with suitably large blocklengths. A substantial limitation to the use of finite-length LDPC codes is the presence of an error floor in the low frame error rate (FER) region. This paper develops a deterministic method of predicting error floors, based on high signal-to-noise ratio (SNR) asymptotics, applied to absorbing sets within structured LDPC codes. The approach is illustrated using a class of array-based LDPC codes, taken as exemplars of high-performance structured LDPC codes. The results are in very good agreement with a stochastic method based on importance sampling which, in turn, matches the hardware-based experimental results. The importance sampling scheme uses a mean-shifted version of the original Gaussian density, appropriately centered between a codeword and a dominant absorbing set, to produce an unbiased estimator of the FER with substantial computational savings over a standard Monte Carlo estimator. Our deterministic estimates are guaranteed to be a lower bound to the error probability in the high SNR regime, and extend the prediction of the error probability to as low as 10-30. By adopting a channel-independent viewpoint, the usefulness of these results is demonstrated for both the standard Gaussian channel and a channel with mixture noise.

## Efficient encoding of QC-LDPC codes related to cyclic MDS codes

- **Status**: ✅
- **Reason**: E. QC-LDPC 효율적 systematic 인코딩 알고리즘(선형복잡도, 다항식 곱셈/나눗셈 회로) — 인코더 HW 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5174514
- **Type**: journal
- **Published**: August 200
- **Authors**: Norifumi Kamiya, Eisaku Sasaki
- **PDF**: https://ieeexplore.ieee.org/document/5174514
- **Abstract**: In this paper, we present an efficient systematic encoding algorithm for quasi-cyclic (QC) low-density parity check (LDPC) codes that are related to cyclic maximum-distance separable (MDS) codes. The algorithm offers linear time complexity, and it can be easily implemented by using polynomial multiplication and division circuits. We show that the division polynomials can be completely characterized by their zeros and that the sum of the respective numbers of their zeros is equal to the parity-length of the codes.

## High-throughput layered decoder implementation for quasi-cyclic LDPC codes

- **Status**: ✅
- **Reason**: QC-LDPC 고처리율 layered 디코더 ASIC: 병렬 layered 아키텍처+critical path splitting+min-sum-이식 HW(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:5174527
- **Type**: journal
- **Published**: August 200
- **Authors**: Kai Zhang, Xinming Huang, Zhongfeng Wang
- **PDF**: https://ieeexplore.ieee.org/document/5174527
- **Abstract**: This paper presents a high-throughput decoder design for the Quasi-Cyclic (QC) Low-Density Parity-Check (LDPC) codes. Two new techniques are proposed, including parallel layered decoding architecture (PLDA) and critical path splitting. PLDA enables parallel processing for all layers by establishing dedicated message passing paths among them. The decoder avoids crossbar-based large interconnect network. Critical path splitting technique is based on articulate adjustment of the starting point of each layer to maximize the time intervals between adjacent layers, such that the critical path delay can be split into pipeline stages. Furthermore, min-sum and loosely coupled algorithms are employed for area efficiency. As a case study, a rate-1/2 2304-bit irregular LDPC decoder is implemented using ASIC design in 90 nm CMOS process. The decoder can achieve the maximum decoding throughput of 2.2 Gbps at 10 iterations. The operating frequency is 950 MHz after synthesis and the chip area is 2.9 mm2.

## Design and analysis of E2RC codes

- **Status**: ✅
- **Reason**: E. E2RC rate-compatible 비정규 LDPC 설계, EXIT 기반 차수분포 최적화 + 빠른 EXIT 함수 계산법 — 바이너리 코드설계 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5174518
- **Type**: journal
- **Published**: August 200
- **Authors**: Cuizhu Shi, Aditya Ramamoorthy
- **PDF**: https://ieeexplore.ieee.org/document/5174518
- **Abstract**: We consider the design and analysis of the efficiently-encodable rate-compatible (E2RC) irregular LDPC codes proposed in previous work. In this work we introduce semi-structured E2RC-like codes and protograph E2RC codes. EXIT chart based methods are developed for the design of semi-structured E2RC-like codes that allow us to determine near-optimal degree distributions for the systematic part of the code while taking into account the structure of the deterministic parity part, thus resolving one of the open issues in the original construction. We develop a fast EXIT function computation method that does not rely on Monte-Carlo simulations and can be used in other scenarios as well. Our approach allows us to jointly optimize code performance across the range of rates under puncturing. We then consider protograph E2RC codes (that have a protograph representation) and propose rules for designing a family of rate-compatible punctured protographs with low thresholds. For both the semi-structured and protograph E2RC families we obtain codes whose gap to capacity is at most 0.3 dB across the range of rates when the maximum variable node degree is twenty.

## Design of a high-throughput IDPC decoder for DVB-S2 using local memory banks

- **Status**: ✅
- **Reason**: DVB-S2 LDPC 디코더 HW 아키텍처 - 로컬 메모리뱅크로 충돌 회피·throughput 향상, 바이너리 LDPC HW 기법 이식 가능(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:5277954
- **Type**: journal
- **Published**: August 200
- **Authors**: Seong-Woon Kim, Chang-Soo Park, Sun-Young Hwang
- **PDF**: https://ieeexplore.ieee.org/document/5277954
- **Abstract**: This paper proposes a novel LDPC (Low-Density Parity Check) decoder architecture to increase throughput for DVB-S2, a second generation standard of ETSI (European Telecommunications Standards Institute) for European satellite digital video broadcasting system, which is employed in European digital TVs. The proposed architecture clusters nodes of a Tanner graph into node groups utilizing the properties of IRA (Irregular Repeat-Accumulate) LDPC codes. Functional modules, which perform calculations for node groups, read and store messages at predetermined local memory banks. The memory banks are designed to avoid memory conflicts by differentiating read and store timings. Hence, throughput of the proposed architecture can be increased. Experimental results show that the throughput of the proposed architecture is increased by 104% ~ 479%, when compared to previous architectures.

## Design of rate-compatible structured LDPC codes for hybrid ARQ applications

- **Status**: ✅
- **Reason**: rate-compatible protograph LDPC 구성+progressive 노드 puncturing 알고리즘+error floor-바이너리 코드설계(E) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5174525
- **Type**: journal
- **Published**: August 200
- **Authors**: Mostafa El-Khamy, Jilei Hou, Naga Bhushan
- **PDF**: https://ieeexplore.ieee.org/document/5174525
- **Abstract**: In this paper, families of rate-compatible protograph-based LDPC codes that are suitable for incrementalredundancy hybrid ARQ applications are constructed. A systematic technique to construct low-rate base codes from a higher rate code is presented. The base codes are designed to be robust against erasures while having a good performance on error channels. A progressive node puncturing algorithm is devised to construct a family of higher rate codes from the base code. The performance of this puncturing algorithm is compared to other puncturing schemes. Using the techniques in this paper, one can construct a rate-compatible family of codes with rates ranging from 0.1 to 0.9 that are within 1 dB from the channel capacity and have good error floors.

## Instanton-based techniques for analysis and reduction of error floors of LDPC codes

- **Status**: ✅
- **Reason**: C/E. instanton 기반 error floor 분석으로 BP/LP 디코더 실패구조 파악, Tanner graph에서 trapping 구조 제거하는 코드설계 — 바이너리 LDPC 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5174515
- **Type**: journal
- **Published**: August 200
- **Authors**: Shashi Kiran Chilappagari, Michael Chertkov, Mikhail G. Stepanov +1
- **PDF**: https://ieeexplore.ieee.org/document/5174515
- **Abstract**: We describe a family of instanton-based optimization methods developed recently for the analysis of the error floors of low-density parity-check (LDPC) codes. Instantons are the most probable configurations of the channel noise which result in decoding failures. We show that the general idea and the respective optimization technique are applicable broadly to a variety of channels, discrete or continuous, and variety of sub-optimal decoders. Specifically, we consider: iterative belief propagation (BP) decoders, Gallager type decoders, and linear programming (LP) decoders performing over the additive white Gaussian noise channel (AWGNC) and the binary symmetric channel (BSC). The instanton analysis suggests that the underlying topological structures of the most probable instanton of the same code but different channels and decoders are related to each other. Armed with this understanding of the graphical structure of the instanton and its relation to the decoding failures, we suggest a method to construct codes whose Tanner graphs are free of these structures, and thus have less significant error floors.

## Capacity-approaching protograph codes

- **Status**: ✅
- **Reason**: E. protograph LDPC 구성(linear min-distance growth, threshold 분석) + BP 고처리율 디코딩 구현전략 — 바이너리 코드설계/디코더 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5174517
- **Type**: journal
- **Published**: August 200
- **Authors**: Dariush Divsalar, Sam Dolinar, Christopher R. Jones +1
- **PDF**: https://ieeexplore.ieee.org/document/5174517
- **Abstract**: This paper discusses construction of protograph-based low-density parity-check (LDPC) codes. Emphasis is placed on protograph ensembles whose typical minimum distance grows linearly with block size. Asymptotic performance analysis for both weight enumeration and iterative decoding threshold determination is provided and applied to a series of code constructions. Construction techniques that yield both low thresholds and linear minimum distance growth are introduced by way of example throughout. The paper also examines implementation strategies for high throughput decoding derived from first principles of belief propagation on bipartite graphs.

## A cutting-plane method based on redundant rows for improving fractional distance

- **Status**: ✅
- **Reason**: 바이너리 패리티검사행렬 fractional distance 개선 cutting-plane 알고리즘-LP 디코딩 기법, 이식 가능(C/E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5174529
- **Type**: journal
- **Published**: August 200
- **Authors**: Makoto Miwa, Tadashi Wadayama, Ichi Takumi
- **PDF**: https://ieeexplore.ieee.org/document/5174529
- **Abstract**: Decoding performance of linear programming (LP) decoding is closely related to geometrical properties of a fundamental polytope: fractional distance, pseudo codeword, etc. In this paper, an idea of the cutting-plane method is employed to improve the fractional distance of a given binary parity-check matrix. The fractional distance is the minimum weight (with respect to lscr1-distance) of nonzero vertices of the fundamental polytope. The cutting polytope is defined based on redundant rows of the parity-check matrix. The redundant rows are codewords of the dual code not yet appearing as rows in the parity-check matrix. The cutting polytope plays a key role to eliminate unnecessary fractional vertices in the fundamental polytope. We propose a greedy algorithm and its efficient implementation based on the cutting-plane method. It has been confirmed that the fractional distance of some parity-check matrices are actually improved by using the algorithm.

## On the Stopping Distance of Array Code Parity-Check Matrices

- **Status**: ✅
- **Reason**: array code 패리티검사행렬 stopping distance 분석, 바이너리 LDPC 유한길이/error floor 코드설계에 관련(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5165182
- **Type**: journal
- **Published**: Aug. 2009
- **Authors**: Morteza Esmaeili, Mohammad Javad Amoshahy
- **PDF**: https://ieeexplore.ieee.org/document/5165182
- **Abstract**: For q an odd prime and 1 les m les q, we study two binary qm times q2 parity check matrices for binary array codes. For both parity check matrices, we determine the stopping distance and the minimum distance of the associated code for 2 les m les 3, and for (m, q)=(4, 5). In the case (m, q)=(4, 7), the stopping distance and the related minimum distance are also determined for one of the given parity check matrices. Moreover, we give a lower bound on the stopping distances for m > 3 and q > 3.

## Guessing Facets: Polytope Structure and Improved LP Decoder

- **Status**: ✅
- **Reason**: LP 디코딩 polytope 구조 활용 개선 디코더 알고리즘, expander 부호용이나 바이너리 LDPC 디코더 기법으로 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5165163
- **Type**: journal
- **Published**: Aug. 2009
- **Authors**: Alexandros G. Dimakis, Amin A. Gohari, Martin J. Wainwright
- **PDF**: https://ieeexplore.ieee.org/document/5165163
- **Abstract**: We investigate the structure of the polytope underlying the linear programming (LP) decoder introduced by Feldman, Karger, and Wainwright. We first show that for expander codes, every fractional pseudocodeword always has at least a constant fraction of nonintegral bits. We then prove that for expander codes, the active set of any fractional pseudocodeword is smaller by a constant fraction than that of any codeword. We further exploit these geometrical properties to devise an improved decoding algorithm with the same order of complexity as LP decoding that provably performs better. The method is very simple: it first applies ordinary LP decoding, and when it fails, it proceeds by guessing facets of the polytope, and then resolving the linear program on these facets. While the LP decoder succeeds only if the ML codeword has the highest likelihood over all pseudocodewords, we prove that the proposed algorithm, when applied to suitable expander codes, succeeds unless there exists a certain number of pseudocodewords, all adjacent to the ML codeword on the LP decoding polytope, and with higher likelihood than the ML codeword. We then describe an extended algorithm, still with polynomial complexity, that succeeds as long as there are at most polynomially many pseudocodewords above the ML codeword.

## New insights into weighted bit-flipping decoding

- **Status**: ✅
- **Reason**: WBF-BP 관계 규명 후 새 WBF 디코딩 알고리즘 제안, 병렬화·임계값 최적화 — 이식 가능 디코더(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5201000
- **Type**: journal
- **Published**: Aug. 2009
- **Authors**: Xiaofu Wu, Cong Ling, Ming Jiang +3
- **PDF**: https://ieeexplore.ieee.org/document/5201000
- **Abstract**: A natural relationship between weighted bit-flipping (WBF) decoding and belief-propagation-like (BP-like) decoding is explored. This understanding can help us develop WBF algorithms from BP-like algorithms. For min-sum decoding, one can find that its WBF algorithm is the algorithm proposed by Jiang et al. For BP decoding, we propose a new WBF algorithm and show its performance advantage. The proposed WBF algorithms are parallelized to achieve rapid convergence. Two efficient simulation-based procedures are proposed for the optimization of the associated thresholds.

## Transactions papers evaluation and design of irregular LDPC codes using ACE spectrum

- **Status**: ✅
- **Reason**: ACE 스펙트럼 기반 유한길이 irregular LDPC error floor 코드설계(E), BEC지만 바이너리 LDPC 구성 기법 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5201020
- **Type**: journal
- **Published**: Aug. 2009
- **Authors**: Dejan Vukobratovic, Vojin Senk
- **PDF**: https://ieeexplore.ieee.org/document/5201020
- **Abstract**: The construction of finite-length irregular LDPC codes with low error floors is currently an attractive research problem. In particular, for the binary erasure channel (BEC), the problem is to find the elements of selected irregular LDPC code ensembles with the size of their minimum stopping set being maximized. Due to the lack of analytical solutions to this problem, a simple but powerful heuristic design algorithm, the approximate cycle extrinsic message degree (ACE) constrained design algorithm, has recently been proposed. Building upon the ACE metric associated with a cycle in a code graph, we introduce the ACE spectrum of LDPC codes as a useful tool for evaluation of codes from selected irregular LDPC code ensembles. Using the ACE spectrum, we generalize the ACE constrained design algorithm, making it more flexible and efficient. We justify the ACE spectrum approach through examples and simulation results.

## An FPGA implementation of LDPC simulation platform

- **Status**: ✅
- **Reason**: FPGA LDPC 시뮬레이션 플랫폼으로 error floor 고속 평가, HW 평가 기법(D) 이식 가능
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:5268152
- **Type**: conference
- **Published**: 8-9 Aug. 2
- **Authors**: Jin Sha, Chuan Zhang, Li Li +1
- **PDF**: https://ieeexplore.ieee.org/document/5268152
- **Abstract**: This paper presents an FPGA implementation for LDPC codes performance simulation. The goal is for fast evaluation of LDPC code to investigate the error floor. The hardware evaluation platform features by fast simulation speed and high precision. The construction of the platform is described. The critical modules designed in the platform such as LDPC encoder, decoder, and AWGN noise generator are presented. As the result, a throughput of 120 Mbps is achieved and the BER curve can reach beyond 10-11 within 10 hours.

## Flexible Architectures for LDPC Decoders Based on Network on Chip Paradigm

- **Status**: ✅
- **Reason**: NoC 기반 유연 LDPC 디코더 HW 아키텍처, 부분병렬 설계 면적/처리량 개선; 이식 가능 HW(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:5350172
- **Type**: conference
- **Published**: 27-29 Aug.
- **Authors**: Fabrizio Vacca, Guido Masera, Hazem Moussa +2
- **PDF**: https://ieeexplore.ieee.org/document/5350172
- **Abstract**: This paper explores the possibility of building a flexible Low Density Parity Check (LDPC) decoder using a network on chip communication infrastructure. Even if this idea is not completely new, previously published works suffered from an excessive area occupation and their practical impact has been very limited. In the following we analyze two possible NOCs specifically designed for the LDPC case. From synthesis results it can be observed how the proposed networks outperform previous implementations in terms of active area with no significant bandwidth loss. Finally to prove the effectiveness of the proposed approach a complete, partially parallel LDPC decoder design is presented and characterized in terms of throughput and area occupation.

## An improved algorithm for constructing QC-LDPC codes based on the PEG algorithm

- **Status**: ✅
- **Reason**: PEG 기반 개선 QC-LDPC 구성, 짧은 사이클 제거·error floor 저감·HW친화—이식 가능 코드설계(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5339908
- **Type**: conference
- **Published**: 26-28 Aug.
- **Authors**: Zhiyong Fan, Weibo Zhang, Xingcheng Liu +1
- **PDF**: https://ieeexplore.ieee.org/document/5339908
- **Abstract**: The Progressive edge-growth (PEG) algorithm was proven to be a simple and effective approach in designing Low-density parity-check (LDPC) codes. However, the Tanner graph constructed with the PEG algorithm is non-structured, which leads to random distributions of the positions of 1's in the corresponding parity-check matrix. In this paper, an improved algorithm based on the PEG algorithm for constructing quasi-cyclic (QC) LDPC codes is proposed. The proposed algorithm can eliminate short cycles efficiently and gain low error-floors. What is more important, the proposed QC-LDPC codes construction method is hardware-friendly because of its quasi-cyclic structure. Our simulation results demonstrate that the codes constructed with the proposed algorithm has better performance than the PEG algorithm over the additive white Gaussian noise (AWGN) channel and Rayleigh flat fading channel.

## Design of High-Rate LDGM codes

- **Status**: ✅
- **Reason**: 고율 바이너리 LDGM/LDPC 코드 설계, 4-cycle 제거·낮은 인코딩 복잡도—이식 가능 코드설계(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5339739
- **Type**: conference
- **Published**: 26-28 Aug.
- **Authors**: Puripong Suthisopapan, Mongkol Kupimai, Rangsan Tongta +1
- **PDF**: https://ieeexplore.ieee.org/document/5339739
- **Abstract**: Low density generator matrix to construct low-density parity check (LDPC) codes is designed in this paper. The proposed structure significantly reduces the encoding complexity of LDPC codes. Codes in this class can be easily constructed by concatenating the parity-check matrix of array low-density parity-check (ALDPC) codes with the identity matrix and also contains no short cycle of length four. The results shown in this paper indicate that these codes can perform very well at high code rate (R ¿ 0.85) under iterative decoding with no serial or parallel concatenation of two codes.

## Improved parallel weighted bit flipping decoding of finite geometry LDPC codes

- **Status**: ✅
- **Reason**: 개선된 병렬 가중치 비트플리핑(IPWBF) LDPC 디코더 알고리즘—이식 가능 디코더(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5339713
- **Type**: conference
- **Published**: 26-28 Aug.
- **Authors**: Guangwen Li, Dashe Li, Yuling Wang +1
- **PDF**: https://ieeexplore.ieee.org/document/5339713
- **Abstract**: To seek a decoding scheme with good performance, low complexity and fast convergence, we present an improved parallel weighted bit flipping (IPWBF) algorithm for finite geometry low-density parity-check codes whose parity check matrix is of heavy row and column weights. In the IPWBF, a bit flipping (BF) function and two parallel BF criteria, all of which scatter in the literature, are exploited jointly to serve our purpose. Meanwhile, differential evolution is used to optimize the involved parameters. Simulation results show that the proposed algorithm achieves an observable performance gain over its counterparts without any complexity penalty. Furthermore, with respect to other known low complexity decodings such as normalized BP-based, the IPWBF yields a new performance versus complexity tradeoff, that is, higher throughput at the expense of moderate performance loss.

## AE-BP: Adaptive Erasure Belief Propagation Decoding Algorithm of LDPC Codes

- **Status**: ✅
- **Reason**: AE-BP 적응적 소거 BP 디코딩, 불안정 메시지 소거하는 신규 LDPC 디코더 — 이식 가능 디코더(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5331673
- **Type**: conference
- **Published**: 25-27 Aug.
- **Authors**: Chaonian Guo, Xiangxue Li, Dong Zheng +2
- **PDF**: https://ieeexplore.ieee.org/document/5331673
- **Abstract**: In the decoding process of LDPC codes, variable node messages often fluctuate continuously and thereby become the hindrance to the successful decoding. This paper proposes an Adaptive Erasure Belief Propagation (AE-BP) decoding algorithm to reduce the influence of these unreliable messages. The idea behind AE-BP is recording the continuous fluctuant times of variable nodes by introducing a sequence of counters, and then adaptively erasing the messages according to their fluctuant times so that other messages would recover to more precise states. Semi-Gaussian approximation demonstrates adaptive erasure is a good candidate towards offsetting the defect of unreliable messages. Experimental simulations show that, for LDPC codes AE-BP outperforms most decoding algorithms in the literature.

## Fully programmable layered LDPC decoder architecture

- **Status**: ✅
- **Reason**: 완전 프로그래머블 layered LDPC 디코더 아키텍처+충돌없는 매핑/스케줄링 — D 이식 가능 HW
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:7077452
- **Type**: conference
- **Published**: 24-28 Aug.
- **Authors**: Christiane Beuschel, Hans-Jörg Pfeiderer
- **PDF**: https://ieeexplore.ieee.org/document/7077452
- **Abstract**: We present a fully programmable layered LDPC decoder architecture together with an optimum mapping and scheduling algorithm. In contrast to other designs proposed in the literature, we use one-phase message passing. This allows for the first time the design of a fully programmable layered decoder. The proposed mapping and scheduling algorithm exploits the full parallelism of the architecture at any time for any code, which means that the mapping algorithm achieves collision-free memory access and 100% utilization of the architecture. Compared to existing programmable designs without layered decoding we double the data throughput. The parallelism of the architecture is unconstrained and fully scalable so that hardware cost and data throughput can be exchanged with fine granularity.

## On the performance and numerical stability of soft-decision Reed-Solomon decoding

- **Status**: ✅
- **Reason**: soft-decision RS의 ABP 디코딩 고정소수점 양자화 분석 — 부호 비의존적 BP 양자화/HW 기법으로 바이너리 LDPC BP에 이식 가능(C/D 예외)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7077766
- **Type**: conference
- **Published**: 24-28 Aug.
- **Authors**: Marcel Bimberg, Emil Matúš, Gerhard P. Fettweis
- **PDF**: https://ieeexplore.ieee.org/document/7077766
- **Abstract**: In this paper we numerically analyze soft-decision Reed-Solomon decoding based on adaptive Belief Propagation (ABP) algorithm in an additive white Gaussian noise (AWGN) and Rayleigh fading environment. We compare modifications of ABP in terms of frame-error-rate performance and decoding latency, while focusing on efficient implementations in software or hardware. Main outcome of the paper is the analysis of quantization effects when ABP is implemented employing fixed-point values.

## Development of a high throughput LDPC codec with 1Gb/s and OFDM transmission system utilizing MBD

- **Status**: ✅
- **Reason**: 고처리율 LDPC 코덱 HW 설계/평가 환경(MBD) — 이식 가능 HW 아키텍처(D), 애매하나 살림
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:5332794
- **Type**: conference
- **Published**: 18-21 Aug.
- **Authors**: Takashi Maehata
- **PDF**: https://ieeexplore.ieee.org/document/5332794
- **Abstract**: Low-density parity-check (LDPC) codes, which are among the most powerful error correcting codes, can achieve performance close to the Shannon limit. It is difficult to evaluate the performance of LDPC codes by software simulation only, because it takes much time and labor. To solve this problem, we have developed the design environment for designing and evaluating LDPC codes on hardware.

## Extended PEG Algorithm for High Rate LDPC Codes

- **Status**: ✅
- **Reason**: 고율 LDPC용 확장 PEG 알고리즘으로 girth 보장 코드 구성, 바이너리 코드설계 기법 이식 가능(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5207892
- **Type**: conference
- **Published**: 10-12 Aug.
- **Authors**: Zhiheng Zhou, Xiangxue Li, Dong Zheng +2
- **PDF**: https://ieeexplore.ieee.org/document/5207892
- **Abstract**: Progressive Edge-Growth(PEG) Algorithm is a good candidate to generate Tanner Graphs with a large girth by establishing edges or connections between symbol and check nodes in an edge-by-edge manner. In this paper, we propose an extended PEG algorithm for constructing Low-Density Parity-Check (LDPC) codes with very high rate when given a lower bound of girth. Simulation results show the bit error rates of constructed LDPC codes with very high rate or large girth.
