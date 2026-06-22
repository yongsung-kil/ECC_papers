# IEEE Xplore — 2009-08


## On asymptotic ensemble weight enumerators of LDPC-like codes

- **Status**: ✅
- **Reason**: E. LDPC ensemble weight enumerator로 error floor 좌우 차수분포 최적화 조건 도출; 결론은 바이너리 LDPC error floor 설계에 직접 적용 (nonbinary는 확장일 뿐)
- **ID**: ieee:5174519
- **Type**: journal
- **Published**: August 200
- **Authors**: Chung-Li Wang, Marc P.C. Fossorier
- **PDF**: https://ieeexplore.ieee.org/document/5174519
- **Abstract**: For LDPC-like codes such as LDPC, GLDPC, and DGLDPC codes, it is well known that the error floor can be caused by the codewords of small weights or stopping sets of small sizes. In this paper, we investigate the computation of asymptotic weight enumerators such that it becomes a convenient tool to determine a good distribution of code ensembles. In addition, by analyzing the first order approximation, we derive a condition to obtain a negative asymptotic growth rate of the codewords of small linear-sized weights, which is an important constraint for distribution optimization. Also the weight enumerators of turbo and repeat-accumulate codes are investigated. Furthermore, we extend our results to nonbinary DGLDPC codes. Generalization to N-layer and convolutional code based LDPC-like codes are also developed.

## Shortening for irregular QC-LDPC codes

- **Status**: ✅
- **Reason**: irregular QC-LDPC shortening 알고리즘-바이너리 코드설계(E) 이식 가능
- **ID**: ieee:5200902
- **Type**: journal
- **Published**: August 200
- **Authors**: Xiaojian Liu, Xiaofu Wu, Chunming Zhao
- **PDF**: https://ieeexplore.ieee.org/document/5200902
- **Abstract**: Shortening is a technique to obtain codes of shorter length and lower rate from a given LDPC code by putting infinite reliability on some variable nodes, whose positions are assumed to be available to both encoder and decoder. In this paper, we propose a shortening algorithm suitable for irregular QC-LDPC codes. The efficiency of the proposed algorithm is verified by both theoretical analysis and simulation.

## Geometrically-structured maximum-girth LDPC block and convolutional codes

- **Status**: ✅
- **Reason**: E. 신규 max-girth 기하구조 QC-LDPC(column-weight-2) 구성 알고리즘, girth 16/24, RPEG 대비 우수 — 바이너리 코드설계 이식 가능
- **ID**: ieee:5174513
- **Type**: journal
- **Published**: August 200
- **Authors**: Morteza Esmaeili, Mohammad Gholami
- **PDF**: https://ieeexplore.ieee.org/document/5174513
- **Abstract**: Four classes of maximum-girth geometrically structured column-weight-two regular quasi-cyclic (QC) low-density parity-check (LDPC) codes are introduced. Two classes of these codes, referred to as Type-I and Type-II codes, are with row-weights 4 and 3, and maximum girths 16 and 24, respectively. The idea behind the construction of these two classes of codes, with rates at least 1/2 and 1/3, is slightly generalized to obtain two classes of variable-high-rate codes, referred to as Type-III1 and Type-III2 codes, with maximum girth 20 and 16, respectively. A low-complexity deterministic algorithm for constructing these four classes of codes is given. The algorithm generates maximum-girth Type-I and Type-II codes with almost arbitrary length eta not less than 216 and 243, respectively. The output of the algorithm substantially improves on some of the previously best known codes constructed using a randomized progressive edge-growth (RPEG) algorithm. For instance, we have rate-0.71 Type-III1 codes of lengths 308 and 728 with girths 10 and 12, respectively, versus the code lengths 385 and 840 obtained by the RPEG algorithm. Simulation results on AWGN channel confirm that, from BER performance perspective, the constructed LDPC codes are superior to the column-weight-two LDPC codes constructed by the previously reported methods. The generator matrix G(D) of the convolutional codes associated with Type-I and Type-II codes is given. The free distance dfree of such a convolutional code is equal to the minimum distance of the corresponding QC block code.

## Design of joint network-low density parity check codes based on the EXIT charts

- **Status**: ❌
- **Reason**: joint network-LDPC(릴레이 네트워크 코딩) EXIT 설계-무선 네트워크 응용 특이적, NAND 이식 기법 없음
- **ID**: ieee:5200898
- **Type**: journal
- **Published**: August 200
- **Authors**: Ying Li, Guanghui Song, Lili Wang
- **PDF**: https://ieeexplore.ieee.org/document/5200898
- **Abstract**: For the multiple-access relay network where two sources communicate with one destination in the presence of one relay, a practical joint network-low density parity check code is designed to help the relay jointly re-encode the messages from both sources. A bilayer extrinsic information transfer chart is developed based on which a design methodology is proposed to iteratively improve the degree distribution of the proposed code. Simulations illustrate that the gap between the convergence threshold and the performance of the coding scheme is less than 0.6dB at BER=10-5.

## Predicting error floors of structured LDPC codes: deterministic bounds and estimates

- **Status**: ✅
- **Reason**: E. 구조화 LDPC absorbing set 기반 error floor 결정론적 예측 + importance sampling; array-based 바이너리 LDPC error floor 설계 이식 가능
- **ID**: ieee:5174520
- **Type**: journal
- **Published**: August 200
- **Authors**: L. Dolecek, P. Lee, Zhengya Zhang +3
- **PDF**: https://ieeexplore.ieee.org/document/5174520
- **Abstract**: The error-correcting performance of low-density parity check (LDPC) codes, when decoded using practical iterative decoding algorithms, is known to be close to Shannon limits for codes with suitably large blocklengths. A substantial limitation to the use of finite-length LDPC codes is the presence of an error floor in the low frame error rate (FER) region. This paper develops a deterministic method of predicting error floors, based on high signal-to-noise ratio (SNR) asymptotics, applied to absorbing sets within structured LDPC codes. The approach is illustrated using a class of array-based LDPC codes, taken as exemplars of high-performance structured LDPC codes. The results are in very good agreement with a stochastic method based on importance sampling which, in turn, matches the hardware-based experimental results. The importance sampling scheme uses a mean-shifted version of the original Gaussian density, appropriately centered between a codeword and a dominant absorbing set, to produce an unbiased estimator of the FER with substantial computational savings over a standard Monte Carlo estimator. Our deterministic estimates are guaranteed to be a lower bound to the error probability in the high SNR regime, and extend the prediction of the error probability to as low as 10-30. By adopting a channel-independent viewpoint, the usefulness of these results is demonstrated for both the standard Gaussian channel and a channel with mixture noise.

## Efficient encoding of QC-LDPC codes related to cyclic MDS codes

- **Status**: ✅
- **Reason**: E. QC-LDPC 효율적 systematic 인코딩 알고리즘(선형복잡도, 다항식 곱셈/나눗셈 회로) — 인코더 HW 이식 가능
- **ID**: ieee:5174514
- **Type**: journal
- **Published**: August 200
- **Authors**: Norifumi Kamiya, Eisaku Sasaki
- **PDF**: https://ieeexplore.ieee.org/document/5174514
- **Abstract**: In this paper, we present an efficient systematic encoding algorithm for quasi-cyclic (QC) low-density parity check (LDPC) codes that are related to cyclic maximum-distance separable (MDS) codes. The algorithm offers linear time complexity, and it can be easily implemented by using polynomial multiplication and division circuits. We show that the division polynomials can be completely characterized by their zeros and that the sum of the respective numbers of their zeros is equal to the parity-length of the codes.

## High-throughput layered decoder implementation for quasi-cyclic LDPC codes

- **Status**: ✅
- **Reason**: QC-LDPC 고처리율 layered 디코더 ASIC: 병렬 layered 아키텍처+critical path splitting+min-sum-이식 HW(D)
- **ID**: ieee:5174527
- **Type**: journal
- **Published**: August 200
- **Authors**: Kai Zhang, Xinming Huang, Zhongfeng Wang
- **PDF**: https://ieeexplore.ieee.org/document/5174527
- **Abstract**: This paper presents a high-throughput decoder design for the Quasi-Cyclic (QC) Low-Density Parity-Check (LDPC) codes. Two new techniques are proposed, including parallel layered decoding architecture (PLDA) and critical path splitting. PLDA enables parallel processing for all layers by establishing dedicated message passing paths among them. The decoder avoids crossbar-based large interconnect network. Critical path splitting technique is based on articulate adjustment of the starting point of each layer to maximize the time intervals between adjacent layers, such that the critical path delay can be split into pipeline stages. Furthermore, min-sum and loosely coupled algorithms are employed for area efficiency. As a case study, a rate-1/2 2304-bit irregular LDPC decoder is implemented using ASIC design in 90 nm CMOS process. The decoder can achieve the maximum decoding throughput of 2.2 Gbps at 10 iterations. The operating frequency is 950 MHz after synthesis and the chip area is 2.9 mm2.

## Design and analysis of E2RC codes

- **Status**: ✅
- **Reason**: E. E2RC rate-compatible 비정규 LDPC 설계, EXIT 기반 차수분포 최적화 + 빠른 EXIT 함수 계산법 — 바이너리 코드설계 이식 가능
- **ID**: ieee:5174518
- **Type**: journal
- **Published**: August 200
- **Authors**: Cuizhu Shi, Aditya Ramamoorthy
- **PDF**: https://ieeexplore.ieee.org/document/5174518
- **Abstract**: We consider the design and analysis of the efficiently-encodable rate-compatible (E2RC) irregular LDPC codes proposed in previous work. In this work we introduce semi-structured E2RC-like codes and protograph E2RC codes. EXIT chart based methods are developed for the design of semi-structured E2RC-like codes that allow us to determine near-optimal degree distributions for the systematic part of the code while taking into account the structure of the deterministic parity part, thus resolving one of the open issues in the original construction. We develop a fast EXIT function computation method that does not rely on Monte-Carlo simulations and can be used in other scenarios as well. Our approach allows us to jointly optimize code performance across the range of rates under puncturing. We then consider protograph E2RC codes (that have a protograph representation) and propose rules for designing a family of rate-compatible punctured protographs with low thresholds. For both the semi-structured and protograph E2RC families we obtain codes whose gap to capacity is at most 0.3 dB across the range of rates when the maximum variable node degree is twenty.

## Design of a high-throughput IDPC decoder for DVB-S2 using local memory banks

- **Status**: ✅
- **Reason**: DVB-S2 LDPC 디코더 HW 아키텍처 - 로컬 메모리뱅크로 충돌 회피·throughput 향상, 바이너리 LDPC HW 기법 이식 가능(D)
- **ID**: ieee:5277954
- **Type**: journal
- **Published**: August 200
- **Authors**: Seong-Woon Kim, Chang-Soo Park, Sun-Young Hwang
- **PDF**: https://ieeexplore.ieee.org/document/5277954
- **Abstract**: This paper proposes a novel LDPC (Low-Density Parity Check) decoder architecture to increase throughput for DVB-S2, a second generation standard of ETSI (European Telecommunications Standards Institute) for European satellite digital video broadcasting system, which is employed in European digital TVs. The proposed architecture clusters nodes of a Tanner graph into node groups utilizing the properties of IRA (Irregular Repeat-Accumulate) LDPC codes. Functional modules, which perform calculations for node groups, read and store messages at predetermined local memory banks. The memory banks are designed to avoid memory conflicts by differentiating read and store timings. Hence, throughput of the proposed architecture can be increased. Experimental results show that the throughput of the proposed architecture is increased by 104% ~ 479%, when compared to previous architectures.

## Design of rate-compatible structured LDPC codes for hybrid ARQ applications

- **Status**: ✅
- **Reason**: rate-compatible protograph LDPC 구성+progressive 노드 puncturing 알고리즘+error floor-바이너리 코드설계(E) 이식 가능
- **ID**: ieee:5174525
- **Type**: journal
- **Published**: August 200
- **Authors**: Mostafa El-Khamy, Jilei Hou, Naga Bhushan
- **PDF**: https://ieeexplore.ieee.org/document/5174525
- **Abstract**: In this paper, families of rate-compatible protograph-based LDPC codes that are suitable for incrementalredundancy hybrid ARQ applications are constructed. A systematic technique to construct low-rate base codes from a higher rate code is presented. The base codes are designed to be robust against erasures while having a good performance on error channels. A progressive node puncturing algorithm is devised to construct a family of higher rate codes from the base code. The performance of this puncturing algorithm is compared to other puncturing schemes. Using the techniques in this paper, one can construct a rate-compatible family of codes with rates ranging from 0.1 to 0.9 that are within 1 dB from the channel capacity and have good error floors.

## Capacity-achieving codes for finite-state channels with maximum-likelihood decoding

- **Status**: ❌
- **Reason**: sparse-graph 부호의 FSC 용량달성 ML 디코딩 이론 bound-순수 이론, 실용 디코더/HW/구성 기여 없음
- **ID**: ieee:5174526
- **Type**: journal
- **Published**: August 200
- **Authors**: Jung Hyun Bae, Achilleas Anastasopoulos
- **PDF**: https://ieeexplore.ieee.org/document/5174526
- **Abstract**: Codes on sparse graphs have been shown to achieve remarkable performance in point-to-point channels with low decoding complexity. Most of the results in this area are based on experimental evidence and/or approximate analysis. The question of whether codes on sparse graphs can achieve the capacity of noisy channels with iterative decoding is still open, and has only been conclusively and positively answered for the binary erasure channel. On the other hand, codes on sparse graphs have been proven to achieve the capacity of memoryless, binary-input, output-symmetric channels with finite graphical complexity per information bit when maximum likelihood (ML) decoding is performed. In this paper, we consider transmission over finite-state channels (FSCs). We derive upper bounds on the average error probability of code ensembles with ML decoding. Based on these bounds we show that codes on sparse graphs can achieve the symmetric information rate (SIR) of FSCs, which is the maximum achievable rate with independently and uniformly distributed input sequences. In order to achieve rates beyond the SIR, we consider a simple quantization scheme that when applied to ensembles of codes on sparse graphs induces a Markov distribution on the transmitted sequence. By deriving average error probability bounds for these quantized code ensembles, we prove that they can achieve the information rates corresponding to the induced Markov distribution, and thus approach the FSC capacity.

## Instanton-based techniques for analysis and reduction of error floors of LDPC codes

- **Status**: ✅
- **Reason**: C/E. instanton 기반 error floor 분석으로 BP/LP 디코더 실패구조 파악, Tanner graph에서 trapping 구조 제거하는 코드설계 — 바이너리 LDPC 이식 가능
- **ID**: ieee:5174515
- **Type**: journal
- **Published**: August 200
- **Authors**: Shashi Kiran Chilappagari, Michael Chertkov, Mikhail G. Stepanov +1
- **PDF**: https://ieeexplore.ieee.org/document/5174515
- **Abstract**: We describe a family of instanton-based optimization methods developed recently for the analysis of the error floors of low-density parity-check (LDPC) codes. Instantons are the most probable configurations of the channel noise which result in decoding failures. We show that the general idea and the respective optimization technique are applicable broadly to a variety of channels, discrete or continuous, and variety of sub-optimal decoders. Specifically, we consider: iterative belief propagation (BP) decoders, Gallager type decoders, and linear programming (LP) decoders performing over the additive white Gaussian noise channel (AWGNC) and the binary symmetric channel (BSC). The instanton analysis suggests that the underlying topological structures of the most probable instanton of the same code but different channels and decoders are related to each other. Armed with this understanding of the graphical structure of the instanton and its relation to the decoding failures, we suggest a method to construct codes whose Tanner graphs are free of these structures, and thus have less significant error floors.

## Capacity-approaching protograph codes

- **Status**: ✅
- **Reason**: E. protograph LDPC 구성(linear min-distance growth, threshold 분석) + BP 고처리율 디코딩 구현전략 — 바이너리 코드설계/디코더 이식 가능
- **ID**: ieee:5174517
- **Type**: journal
- **Published**: August 200
- **Authors**: Dariush Divsalar, Sam Dolinar, Christopher R. Jones +1
- **PDF**: https://ieeexplore.ieee.org/document/5174517
- **Abstract**: This paper discusses construction of protograph-based low-density parity-check (LDPC) codes. Emphasis is placed on protograph ensembles whose typical minimum distance grows linearly with block size. Asymptotic performance analysis for both weight enumeration and iterative decoding threshold determination is provided and applied to a series of code constructions. Construction techniques that yield both low thresholds and linear minimum distance growth are introduced by way of example throughout. The paper also examines implementation strategies for high throughput decoding derived from first principles of belief propagation on bipartite graphs.

## Turbo coded multiple-antenna systems for near-capacity performance

- **Status**: ❌
- **Reason**: turbo coded MIMO/BLAST 무선 응용, LDPC 무관 떼어낼 기법 없음
- **ID**: ieee:5174524
- **Type**: journal
- **Published**: August 200
- **Authors**: Yeong-Luh Ueng, Chia-Jung Yeh, Mao-Chao Lin +1
- **PDF**: https://ieeexplore.ieee.org/document/5174524
- **Abstract**: For a turbo coded BLAST (Bell LAbs Space-Time architecture) system with Nt transmit antennas and Nr receive antennas, there is a significant gap between its detection threshold and the capacity in case Nt > Nr. In this paper, we show that by introducing a convolutional interleaver with block delay between the BLAST mapper and the turbo encoder, the threshold can be improved. Near-capacity thresholds can be achieved for some cases. To take advantage of the low detector complexity in Alamouti STBC (space-time block code), we also investigate a STBC system, which is the concatenation of the Alamouti STBC with a turbo trellis coded modulation. By using a proper labelling and adding a convolutional interleaver with block delay to such a STBC system, we achieve both lower error floors and lower thresholds.

## A cutting-plane method based on redundant rows for improving fractional distance

- **Status**: ✅
- **Reason**: 바이너리 패리티검사행렬 fractional distance 개선 cutting-plane 알고리즘-LP 디코딩 기법, 이식 가능(C/E)
- **ID**: ieee:5174529
- **Type**: journal
- **Published**: August 200
- **Authors**: Makoto Miwa, Tadashi Wadayama, Ichi Takumi
- **PDF**: https://ieeexplore.ieee.org/document/5174529
- **Abstract**: Decoding performance of linear programming (LP) decoding is closely related to geometrical properties of a fundamental polytope: fractional distance, pseudo codeword, etc. In this paper, an idea of the cutting-plane method is employed to improve the fractional distance of a given binary parity-check matrix. The fractional distance is the minimum weight (with respect to lscr1-distance) of nonzero vertices of the fundamental polytope. The cutting polytope is defined based on redundant rows of the parity-check matrix. The redundant rows are codewords of the dual code not yet appearing as rows in the parity-check matrix. The cutting polytope plays a key role to eliminate unnecessary fractional vertices in the fundamental polytope. We propose a greedy algorithm and its efficient implementation based on the cutting-plane method. It has been confirmed that the fractional distance of some parity-check matrices are actually improved by using the algorithm.

## Quasi-systematic doped LT codes

- **Status**: ❌
- **Reason**: QS-DLT(rateless erasure/LT fountain) 코드; fountain/erasure 부호로 떼어낼 채널 ECC 기법 없음
- **ID**: ieee:5174516
- **Type**: journal
- **Published**: August 200
- **Authors**: Xiaojun Yuan, Li Ping
- **PDF**: https://ieeexplore.ieee.org/document/5174516
- **Abstract**: We propose a family of binary erasure codes, namely, quasi-systematic doped Luby-Transform (QS-DLT) codes, that are rate-less, almost systematic, and universally capacity-achieving without the prior knowledge of channel erasure rate. The encoding and decoding complexities of QS-DLT codes are O(Klog(1/epsiv)), where K is the information length, and epsiv is the overhead. Stopping-set analysis is carried out to study the error-floor behavior of QS-DLT codes. Analysis and numerical results demonstrate that QS-DLT codes provide a low-complexity alternative to systematic Raptor codes with comparable performance.

## Finite-length scaling of turbo-like code ensembles on the binary erasure channel

- **Status**: ❌
- **Reason**: BEC에서 turbo-like 부호 유한길이 scaling 추정-순수 이론 bound, 떼어낼 디코더/HW/구성 없음
- **ID**: ieee:5174521
- **Type**: journal
- **Published**: August 200
- **Authors**: Iryna Andriyanova
- **PDF**: https://ieeexplore.ieee.org/document/5174521
- **Abstract**: A possibility of estimating the finite-length performance of sparse-graph code ensembles gives two opportunities: to compare different codes of the same length in a context very close to real, practical applications and to perform the parameter optimization for a given code length [2]. We need a finite-length approximation that is valid for any code ensemble. The scaling approach seems to be a tool, general enough to provide such an approximation. However, the analytical derivation of parameters of the scaling approximation has been successful only for LDPC codes [1]; despite several attempts [25], [20], no such result was proposed for other code ensembles. In this paper, we focus on the finite-length performance of turbo-like codes, by applying the scaling approach to this case. In particular, by assuming the transmission over the binary erasure channel, we conjecture the scaling law and derive its scaling parameter. As examples, we present the performance estimation for Repeat-Accumulate codes [11], parallel turbo codes [8] and TLDPC codes [5], in all cases matching well the numerical results.

## Good concatenated code ensembles for the binary erasure channel

- **Status**: ❌
- **Reason**: BEC용 concatenated(RMA/HCC) 부호 ensemble 점근 stopping set 분석-비-LDPC 부호+이론 분석, 이식 기법 없음
- **ID**: ieee:5174522
- **Type**: journal
- **Published**: August 200
- **Authors**: Alexandre Graell I Amat, Eirik Rosnes
- **PDF**: https://ieeexplore.ieee.org/document/5174522
- **Abstract**: In this work, we give good concatenated code ensembles for the binary erasure channel (BEC). In particular, we consider repeat multiple-accumulate (RMA) code ensembles formed by the serial concatenation of a repetition code with multiple accumulators, and the hybrid concatenated code (HCC) ensembles recently introduced by Koller et al. (5th Int. Symp. on Turbo Codes & Rel. Topics, Lausanne, Switzerland) consisting of an outer multiple parallel concatenated code serially concatenated with an inner accumulator. We introduce stopping sets for iterative constituent code oriented decoding using maximum a posteriori erasure correction in the constituent codes. We then analyze the asymptotic stopping set distribution for RMA and HCC ensembles and show that their stopping distance hmin, defined as the size of the smallest nonempty stopping set, asymptotically grows linearly with the block length. Thus, these code ensembles are good for the BEC. It is shown that for RMA code ensembles, contrary to the asymptotic minimum distance dmin, whose growth rate coefficient increases with the number of accumulate codes, the hmin growth rate coefficient diminishes with the number of accumulators. We also consider random puncturing of RMA code ensembles and show that for sufficiently high code rates, the asymptotic hmin does not grow linearly with the block length, contrary to the asymptotic dmin, whose growth rate coefficient approaches the Gilbert-Varshamov bound as the rate increases. Finally, we give iterative decoding thresholds for the different code ensembles to compare the convergence properties.

## Toward optimizing cauchy matrix for cauchy reed-solomon code

- **Status**: ❌
- **Reason**: Cauchy Reed-Solomon 행렬 최적화-비-LDPC(RS) 부호, 이식 디코더 기법 없음
- **ID**: ieee:5200899
- **Type**: journal
- **Published**: August 200
- **Authors**: Xiangxue Li, Qingji Zheng, Haifeng Qian +2
- **PDF**: https://ieeexplore.ieee.org/document/5200899
- **Abstract**: The computational costs of Cauchy Reed-Solomon (CRS) encoding operation make a great impact on the performance of its practical applications. The letter concentrates on how to construct a good Cauchy matrix which can lead to an efficient CRS coding scheme. We first formally model the problem by using a binary quadratic programming, then present an approximate method called localized greedy algorithm (LGA) to solve it. Compared with existing work, LGA requires much lower complexities to obtain the same performance of Cauchy matrices.

## On the Stopping Distance of Array Code Parity-Check Matrices

- **Status**: ✅
- **Reason**: array code 패리티검사행렬 stopping distance 분석, 바이너리 LDPC 유한길이/error floor 코드설계에 관련(E)
- **ID**: ieee:5165182
- **Type**: journal
- **Published**: Aug. 2009
- **Authors**: Morteza Esmaeili, Mohammad Javad Amoshahy
- **PDF**: https://ieeexplore.ieee.org/document/5165182
- **Abstract**: For q an odd prime and 1 les m les q, we study two binary qm times q2 parity check matrices for binary array codes. For both parity check matrices, we determine the stopping distance and the minimum distance of the associated code for 2 les m les 3, and for (m, q)=(4, 5). In the case (m, q)=(4, 7), the stopping distance and the related minimum distance are also determined for one of the given parity check matrices. Moreover, we give a lower bound on the stopping distances for m > 3 and q > 3.

## Guessing Facets: Polytope Structure and Improved LP Decoder

- **Status**: ✅
- **Reason**: LP 디코딩 polytope 구조 활용 개선 디코더 알고리즘, expander 부호용이나 바이너리 LDPC 디코더 기법으로 이식 가능(C)
- **ID**: ieee:5165163
- **Type**: journal
- **Published**: Aug. 2009
- **Authors**: Alexandros G. Dimakis, Amin A. Gohari, Martin J. Wainwright
- **PDF**: https://ieeexplore.ieee.org/document/5165163
- **Abstract**: We investigate the structure of the polytope underlying the linear programming (LP) decoder introduced by Feldman, Karger, and Wainwright. We first show that for expander codes, every fractional pseudocodeword always has at least a constant fraction of nonintegral bits. We then prove that for expander codes, the active set of any fractional pseudocodeword is smaller by a constant fraction than that of any codeword. We further exploit these geometrical properties to devise an improved decoding algorithm with the same order of complexity as LP decoding that provably performs better. The method is very simple: it first applies ordinary LP decoding, and when it fails, it proceeds by guessing facets of the polytope, and then resolving the linear program on these facets. While the LP decoder succeeds only if the ML codeword has the highest likelihood over all pseudocodewords, we prove that the proposed algorithm, when applied to suitable expander codes, succeeds unless there exists a certain number of pseudocodewords, all adjacent to the ML codeword on the LP decoding polytope, and with higher likelihood than the ML codeword. We then describe an extended algorithm, still with polynomial complexity, that succeeds as long as there are at most polynomially many pseudocodewords above the ML codeword.

## Moment Balancing Templates: Constructions to Add Insertion/Deletion Correction Capability to Error Correcting or Constrained Codes

- **Status**: ❌
- **Reason**: 삽입/삭제 정정 moment balancing template, NAND 채널 ECC와 무관한 부호 확장 기법
- **ID**: ieee:5165175
- **Type**: journal
- **Published**: Aug. 2009
- **Authors**: Hendrik C. Ferreira, Khaled A. S. Abdel-Ghaffar, Ling Cheng +2
- **PDF**: https://ieeexplore.ieee.org/document/5165175
- **Abstract**: Templates are constructed to extend arbitrary additive error correcting or constrained codes, i.e., additional redundant bits are added in selected positions to balance the moment of the codeword. The original codes may have error correcting capabilities or constrained output symbols as predetermined by the usual communication system considerations, which are retained after extending the code. Using some number theoretic constructions in the literature, insertion/deletion correction can then be achieved. If the template is carefully designed, the number of additional redundant bits for the insertion/deletion correction can be kept small-in some cases of the same order as the number of parity bits in a Hamming code of comparable length.

## New insights into weighted bit-flipping decoding

- **Status**: ✅
- **Reason**: WBF-BP 관계 규명 후 새 WBF 디코딩 알고리즘 제안, 병렬화·임계값 최적화 — 이식 가능 디코더(C)
- **ID**: ieee:5201000
- **Type**: journal
- **Published**: Aug. 2009
- **Authors**: Xiaofu Wu, Cong Ling, Ming Jiang +3
- **PDF**: https://ieeexplore.ieee.org/document/5201000
- **Abstract**: A natural relationship between weighted bit-flipping (WBF) decoding and belief-propagation-like (BP-like) decoding is explored. This understanding can help us develop WBF algorithms from BP-like algorithms. For min-sum decoding, one can find that its WBF algorithm is the algorithm proposed by Jiang et al. For BP decoding, we propose a new WBF algorithm and show its performance advantage. The proposed WBF algorithms are parallelized to achieve rapid convergence. Two efficient simulation-based procedures are proposed for the optimization of the associated thresholds.

## Design and Analysis of Successive Decoding With Finite Levels for the Markov Channel

- **Status**: ❌
- **Reason**: Markov 채널 successive decoding+인터리버 설계, LDPC는 베이스라인이고 채널특이적 기법으로 NAND 이식성 없음
- **ID**: ieee:5165193
- **Type**: journal
- **Published**: Aug. 2009
- **Authors**: Teng Li, Oliver Michael Collins
- **PDF**: https://ieeexplore.ieee.org/document/5165193
- **Abstract**: This paper proposes a practical successive decoding scheme with finite levels for the finite-state Markov channels (FSMCs) where there is no a priori state information at the transmitter or the receiver. The design employs either a random interleaver or a deterministic interleaver with an irregular pattern and an optional iterative estimation and decoding procedure within each level. The interleaver design criteria may be the achievable rate or the extrinsic information transfer (EXIT) chart, depending on the receiver type. For random interleavers, the optimization problem is solved efficiently using a pilot-utility function, while for deterministic interleavers, a good construction is given using empirical rules. Simulation results demonstrate that the new successive decoding scheme combined with irregular low-density parity-check (LDPC) codes can approach the identically and uniformly distributed (i.u.d.) input capacity on the Markov-fading channel using only a few levels.

## Transactions papers evaluation and design of irregular LDPC codes using ACE spectrum

- **Status**: ✅
- **Reason**: ACE 스펙트럼 기반 유한길이 irregular LDPC error floor 코드설계(E), BEC지만 바이너리 LDPC 구성 기법 이식 가능
- **ID**: ieee:5201020
- **Type**: journal
- **Published**: Aug. 2009
- **Authors**: Dejan Vukobratovic, Vojin Senk
- **PDF**: https://ieeexplore.ieee.org/document/5201020
- **Abstract**: The construction of finite-length irregular LDPC codes with low error floors is currently an attractive research problem. In particular, for the binary erasure channel (BEC), the problem is to find the elements of selected irregular LDPC code ensembles with the size of their minimum stopping set being maximized. Due to the lack of analytical solutions to this problem, a simple but powerful heuristic design algorithm, the approximate cycle extrinsic message degree (ACE) constrained design algorithm, has recently been proposed. Building upon the ACE metric associated with a cycle in a code graph, we introduce the ACE spectrum of LDPC codes as a useful tool for evaluation of codes from selected irregular LDPC code ensembles. Using the ACE spectrum, we generalize the ACE constrained design algorithm, making it more flexible and efficient. We justify the ACE spectrum approach through examples and simulation results.

## A flexible rate slepian-wolf code construction

- **Status**: ❌
- **Reason**: Slepian-Wolf 분산소스코딩+RCPC convolutional code 신드롬, LDPC 아님이고 소스코딩 도메인
- **ID**: ieee:5201023
- **Type**: journal
- **Published**: Aug. 2009
- **Authors**: Mahdi Zamani, Farshad Lahouti
- **PDF**: https://ieeexplore.ieee.org/document/5201023
- **Abstract**: A flexible rate Slepian-Wolf (SW) code is constructed, which is vital for wireless sensor network applications. The proposed solution is based on an efficient and practical algorithm to compute the syndrome of the rate-compatible convolutional codes (RCPC). Using this algorithm, there is no need to compute the syndrome of punctured version of the mother code for each puncturing matrix, which is complex. Instead, the syndrome of the punctured code is the punctured version of the syndrome of the mother code using the same pattern of puncturing. The algorithm is general for all convolutional codes in Zq. The strategy is also generalized for parallel and serial concatenated convolutional codes. For the cases, where the dependencies among sources are modeled as a virtual discrete channel, a simplified decoding scheme is suggested. This method is generalized to achieve all points on the SW boundary using a simple code design technique. Simulation results demonstrate the performance and effectiveness of the proposed methods.

## Parameter Selection for Wyner–Ziv Coding of Laplacian Sources with Additive Laplacian or Gaussian Innovation

- **Status**: ❌
- **Reason**: Wyner-Ziv 소스코딩 파라미터 선택, 채널 ECC가 아닌 소스코딩
- **ID**: ieee:4803747
- **Type**: journal
- **Published**: Aug. 2009
- **Authors**: Debargha Mukherjee
- **PDF**: https://ieeexplore.ieee.org/document/4803747
- **Abstract**: A large number of practical coding scenarios deal with sources such as transform coefficients that can be well modeled as Laplacians. For regular coding of such sources, samples are often quantized by a family of uniform quantizers possibly with a deadzone, and then entropy coded. For the Wyner-Ziv coding problem when correlated side-information is available at the decoder, the side-information can be modeled as obtained by independent additive Laplacian or Gaussian innovation on the source. This paper deals with optimal choice of parameters for practical Wyner-Ziv coding in such scenarios, using the same quantizer family as in the regular codec to cover a range of rate-distortion tradeoffs, given the variances of the source and additive noise. We propose and analyze a general encoding model based on multilevel coset codes that combines source coding and channel coding and show that at practical block lengths and code complexities, not pure channel coding but a hybrid combination of source coding and channel coding with right parameters provide optimal rate-distortion performance. We also provide a framework for on-the-fly parameter choice based on nonparametric representation of a set of seed functions, for use in scenarios where variances are estimated during encoding. A good insight in the optimal parameter selection mechanism is essential for building practical distributed codecs.

## Reliability-based retransmission criteria for hybrid ARQ

- **Status**: ❌
- **Reason**: HARQ 재전송 기준(BEP/WEP)으로 ECC 부호·디코더·HW 기여 없음, 무선 프로토콜 특이적
- **ID**: ieee:5201001
- **Type**: journal
- **Published**: Aug. 2009
- **Authors**: Justus Ch. Fricke, Peter A. Hoeher
- **PDF**: https://ieeexplore.ieee.org/document/5201001
- **Abstract**: Bit error probability (BEP) and word error probability (WEP) are used as reliability-based retransmission criteria in conjunction with hybrid ARQ (HARQ) protocols. Instead of exploiting an error-detecting code, the decision for a retransmission is based on the error probability of the decoded word, which can be calculated in or after the decoding process.

## An FPGA implementation of LDPC simulation platform

- **Status**: ✅
- **Reason**: FPGA LDPC 시뮬레이션 플랫폼으로 error floor 고속 평가, HW 평가 기법(D) 이식 가능
- **ID**: ieee:5268152
- **Type**: conference
- **Published**: 8-9 Aug. 2
- **Authors**: Jin Sha, Chuan Zhang, Li Li +1
- **PDF**: https://ieeexplore.ieee.org/document/5268152
- **Abstract**: This paper presents an FPGA implementation for LDPC codes performance simulation. The goal is for fast evaluation of LDPC code to investigate the error floor. The hardware evaluation platform features by fast simulation speed and high precision. The construction of the platform is described. The critical modules designed in the platform such as LDPC encoder, decoder, and AWGN noise generator are presented. As the result, a throughput of 120 Mbps is achieved and the BER curve can reach beyond 10-11 within 10 hours.

## Joint frame synchronization and belief propagation decoding for quasi-cyclic LDPC-coded system under pseudorandom noise disturbance

- **Status**: ❌
- **Reason**: 프레임 동기화+BP 결합 무선통신 응용 특이적, 떼어낼 NAND ECC 디코더 기법 없음
- **ID**: ieee:5267829
- **Type**: conference
- **Published**: 8-9 Aug. 2
- **Authors**: Zhixiong Chen, Jinsha Yuan
- **PDF**: https://ieeexplore.ieee.org/document/5267829
- **Abstract**: Because of the quasi-cyclic nature of Quasi-Cyclic LDPC (QC-LDPC) codes, there are ramps in the frame synchronization searching process. A pilotless code-aided frame synchronization algorithm joint with improved BP decoding for QC-LDPC coded system under PN disturbance to eliminate the ramps is proposed in this paper. Simulation results show the validity of the modified BP decoding algorithm and outstanding synchronization performance compared to the algorithm before improvement and hard decision frame synchronization proposed by Dong-U Lee.

## The study of LDPC code applied to underwater laser communication

- **Status**: ❌
- **Reason**: 수중 레이저 PPM 통신에 표준 LDPC 소프트판정 적용 — 신규 디코더/구성 없는 응용, 떼어낼 기법 없음
- **ID**: ieee:5292710
- **Type**: conference
- **Published**: 30-3 Aug. 
- **Authors**: Tiansong Li, Haiyan Zhou, Lihua Sun
- **PDF**: https://ieeexplore.ieee.org/document/5292710
- **Abstract**: Low density parity check code is applied to underwater laser pulse position modulation communication system. The soft-decision decoding algorithm improves the error-correcting capacity by using the output soft information of the photon detector.

## Flexible Architectures for LDPC Decoders Based on Network on Chip Paradigm

- **Status**: ✅
- **Reason**: NoC 기반 유연 LDPC 디코더 HW 아키텍처, 부분병렬 설계 면적/처리량 개선; 이식 가능 HW(D)
- **ID**: ieee:5350172
- **Type**: conference
- **Published**: 27-29 Aug.
- **Authors**: Fabrizio Vacca, Guido Masera, Hazem Moussa +2
- **PDF**: https://ieeexplore.ieee.org/document/5350172
- **Abstract**: This paper explores the possibility of building a flexible Low Density Parity Check (LDPC) decoder using a network on chip communication infrastructure. Even if this idea is not completely new, previously published works suffered from an excessive area occupation and their practical impact has been very limited. In the following we analyze two possible NOCs specifically designed for the LDPC case. From synthesis results it can be observed how the proposed networks outperform previous implementations in terms of active area with no significant bandwidth loss. Finally to prove the effectiveness of the proposed approach a complete, partially parallel LDPC decoder design is presented and characterized in terms of throughput and area occupation.

## An improved algorithm for constructing QC-LDPC codes based on the PEG algorithm

- **Status**: ✅
- **Reason**: PEG 기반 개선 QC-LDPC 구성, 짧은 사이클 제거·error floor 저감·HW친화—이식 가능 코드설계(E)
- **ID**: ieee:5339908
- **Type**: conference
- **Published**: 26-28 Aug.
- **Authors**: Zhiyong Fan, Weibo Zhang, Xingcheng Liu +1
- **PDF**: https://ieeexplore.ieee.org/document/5339908
- **Abstract**: The Progressive edge-growth (PEG) algorithm was proven to be a simple and effective approach in designing Low-density parity-check (LDPC) codes. However, the Tanner graph constructed with the PEG algorithm is non-structured, which leads to random distributions of the positions of 1's in the corresponding parity-check matrix. In this paper, an improved algorithm based on the PEG algorithm for constructing quasi-cyclic (QC) LDPC codes is proposed. The proposed algorithm can eliminate short cycles efficiently and gain low error-floors. What is more important, the proposed QC-LDPC codes construction method is hardware-friendly because of its quasi-cyclic structure. Our simulation results demonstrate that the codes constructed with the proposed algorithm has better performance than the PEG algorithm over the additive white Gaussian noise (AWGN) channel and Rayleigh flat fading channel.

## A simplified decoding algorithm for nonbinary LDPC codes

- **Status**: ❌
- **Reason**: 비이진(high order GF) LDPC 간소화 디코딩—비이진 LDPC 제외
- **ID**: ieee:5339910
- **Type**: conference
- **Published**: 26-28 Aug.
- **Authors**: Ce-lun Liu, Jian-ping An, Xiang-yuan Bu
- **PDF**: https://ieeexplore.ieee.org/document/5339910
- **Abstract**: A simplified decoding algorithm for low-density parity-check (LDPC) codes over high order Galois field is proposed to reduce the complexity of traditional sum-product algorithm (SPA). There are only addition operation and comparison operation in this algorithm, without complex multiplication operation. The computation complexity of proposed algorithm is much smaller than the SPA. The signal-to-noise power ratio (SNR) isn't needed in this algorithm, so the process of SNR estimation can also be removed. The simulation results show that the bit error rate (BER) performance of proposed algorithm degrades only about 0.5 dB than the SPA, so the proposed algorithm is an efficient simplified algorithm in engineering.

## Design of High-Rate LDGM codes

- **Status**: ✅
- **Reason**: 고율 바이너리 LDGM/LDPC 코드 설계, 4-cycle 제거·낮은 인코딩 복잡도—이식 가능 코드설계(E)
- **ID**: ieee:5339739
- **Type**: conference
- **Published**: 26-28 Aug.
- **Authors**: Puripong Suthisopapan, Mongkol Kupimai, Rangsan Tongta +1
- **PDF**: https://ieeexplore.ieee.org/document/5339739
- **Abstract**: Low density generator matrix to construct low-density parity check (LDPC) codes is designed in this paper. The proposed structure significantly reduces the encoding complexity of LDPC codes. Codes in this class can be easily constructed by concatenating the parity-check matrix of array low-density parity-check (ALDPC) codes with the identity matrix and also contains no short cycle of length four. The results shown in this paper indicate that these codes can perform very well at high code rate (R ¿ 0.85) under iterative decoding with no serial or parallel concatenation of two codes.

## A construction method of quantum low density parity check code based on projective geometry

- **Status**: ❌
- **Reason**: 양자 LDPC(QLDPC) 사영기하 구성—양자 EC, 원칙 제외
- **ID**: ieee:5339860
- **Type**: conference
- **Published**: 26-28 Aug.
- **Authors**: Sheng-Mei Zhao, Xiu-Li Zhu, Guo-Jun Sun
- **PDF**: https://ieeexplore.ieee.org/document/5339860
- **Abstract**: With the development of quantum error correction techniques, many counterparts of classical error correction coding techniques have been found in quantum area. As the quantum counterpart of a good error correction code in classical communications, quantum low density parity check code becomes a promising coding technique in quantum error correction area. In this paper, a construction method of quantum low density parity check code (quantum LDPC) based on Projective Geometry is proposed, and the quantum code QLDPC [21,6] is selected as an example to illustrate the whole construction procedures. By numerical simulation, the error correction performance of QLDPC [21,6] is discussed over the bit-flipping channel. It is shown that this method is available and has some advantages.

## Bit-wise shortening of nonbinary LDPC codes using their binary images

- **Status**: ❌
- **Reason**: 비이진(nonbinary) RC-LDPC 단축 구성—비이진 LDPC 제외
- **ID**: ieee:5339905
- **Type**: conference
- **Published**: 26-28 Aug.
- **Authors**: Lin Zhou, Baoming Bai, Ming Xu +1
- **PDF**: https://ieeexplore.ieee.org/document/5339905
- **Abstract**: Most of work on rate-compatible low-density parity-check (RC-LDPC) codes focus on binary codes. In this paper, we propose a construction of nonbinary RC-LDPC codes at short block length by using a bit-wise shortening method based on the algebraic properties of their binary images. All shortened information bits are carefully chosen according to the degree distributions of their binary images. Simulations show that a gain of around 1 dB is attained at the shortened code rate R = 1/5 over conventional symbol-wise shortening.

## Parallel encodable nonbinary quasi-cyclic LDPC codes with near-capacity performance

- **Status**: ❌
- **Reason**: 비이진(nonbinary) QC-LDPC 병렬 인코딩—비이진 LDPC 제외
- **ID**: ieee:5339907
- **Type**: conference
- **Published**: 26-28 Aug.
- **Authors**: Chao Chen, Baoming Bai, Ruijia Yuan +1
- **PDF**: https://ieeexplore.ieee.org/document/5339907
- **Abstract**: In this paper, we propose a class of efficiently encodable nonbinary quasi-cyclic low-density parity-check (QC-LDPC) codes over finite fields. The special structure of the parity-check matrix allows the construction of both regular and irregular codes. A parallel encoding algorithm with a simple shift-register circuits implementation is presented, which significantly reduces the encoding latency. Simulation results show that, the proposed codes, when combined with higher order modulations, perform close to the Shannon limit.

## A distributed joint source-channel coding scheme for multiple correlated sources

- **Status**: ❌
- **Reason**: 분산 JSCC, 단일 LDPC를 소스+채널 결합에 사용 — LDPC는 베이스라인이고 떼어낼 ECC 기법 없음
- **ID**: ieee:5339955
- **Type**: conference
- **Published**: 26-28 Aug.
- **Authors**: Xuqi Zhu, Lin Zhang, Yu Liu
- **PDF**: https://ieeexplore.ieee.org/document/5339955
- **Abstract**: Multiple nodes sensing the common target is the most popular application of the Wireless Sensor Networks (WSNs). Pure distributed compression of multiple correlated sources has been discussed much in the related literature, while taking the noisy communication channels into account is more suitable for the actual scenario. In this paper, a practical Distributed Joint Source-Channel Coding (DJSCC) scheme for multiple correlated sources is proposed. Besides considering the noisy channels and multiple sources, the processing of the noisy side information is also investigated here. By combining the Shannon theorem and the Slepian-Wolf theorem, the theoretical limits of the proposed DJSCC scheme are derived. An efficient coding strategy with a single Low-Density Parity Check (LDPC) code is designed based on the theory to cope with both source and channel coding. The simulation results demonstrate the desired efficiency of our scheme.

## Improved parallel weighted bit flipping decoding of finite geometry LDPC codes

- **Status**: ✅
- **Reason**: 개선된 병렬 가중치 비트플리핑(IPWBF) LDPC 디코더 알고리즘—이식 가능 디코더(C)
- **ID**: ieee:5339713
- **Type**: conference
- **Published**: 26-28 Aug.
- **Authors**: Guangwen Li, Dashe Li, Yuling Wang +1
- **PDF**: https://ieeexplore.ieee.org/document/5339713
- **Abstract**: To seek a decoding scheme with good performance, low complexity and fast convergence, we present an improved parallel weighted bit flipping (IPWBF) algorithm for finite geometry low-density parity-check codes whose parity check matrix is of heavy row and column weights. In the IPWBF, a bit flipping (BF) function and two parallel BF criteria, all of which scatter in the literature, are exploited jointly to serve our purpose. Meanwhile, differential evolution is used to optimize the involved parameters. Simulation results show that the proposed algorithm achieves an observable performance gain over its counterparts without any complexity penalty. Furthermore, with respect to other known low complexity decodings such as normalized BP-based, the IPWBF yields a new performance versus complexity tradeoff, that is, higher throughput at the expense of moderate performance loss.

## Side-information-adaptive LDPC coding for distributed multi-view video coding over wireless sensor networks

- **Status**: ❌
- **Reason**: 분산 다시점 비디오 코딩(DMVC)용 LDPC—응용 특이적 소스코딩, 떼어낼 ECC 기법 없음
- **ID**: ieee:5339857
- **Type**: conference
- **Published**: 26-28 Aug.
- **Authors**: Zhang Bo, Zhang Lin, Liu Yu +1
- **PDF**: https://ieeexplore.ieee.org/document/5339857
- **Abstract**: Distributed multi-view video coding (DMVC) has become a focus due to the prosperity of the multimedia applications in wireless sensor networks. We propose a novel method of an adaptive scheme, named side-information-adaptive Low Density Parity Check (LDPC) coding. Apart from the existing multiple side-information implications in DMVC, this paper is dedicated to not only utilizing LDPC to produce the syndromes to realize DMVC, but exploiting preferable side-information search scheme for decoding scheme between the temporal and the inter-view correlation in DMVC. Simulation results illustrate the significant improvements of the proposed scheme with high motion in DMVC for high motion video.

## An iterative soft-decision decoding algorithm for conventional concatenated codes

- **Status**: ❌
- **Reason**: concatenated code의 KV+BCJR 반복 소프트디코딩—비-LDPC, BP 이식성 없음
- **ID**: ieee:5339712
- **Type**: conference
- **Published**: 26-28 Aug.
- **Authors**: Jingwei Zhang, Jiaying You, Lishuang Lu +1
- **PDF**: https://ieeexplore.ieee.org/document/5339712
- **Abstract**: In this paper, we present an iterative soft-decision decoding algorithm for conventional concatenated codes, which incorporates Koetter-Vardy (KV) algorithm for outer codes and Bahl-Cocke-Jelinek-Raviv (BCJR) algorithm for inner codes. After one round of decoding, the successfully decoded codewords from the outer decoder can be fed back to the inner decoder as constraint information. We compare several decoding algorithms for conventional concatenated codes in terms of the bit-error-rate (BER) performance. Simulation results show that, for conventional concatenated codes, performance improvements of about 0.4 dB and 0.1 dB can be achieved by the iterative soft-decision decoding algorithm over the conventional two-stage decoding algorithm and the iterative hard-decision decoding algorithm, respectively.

## AE-BP: Adaptive Erasure Belief Propagation Decoding Algorithm of LDPC Codes

- **Status**: ✅
- **Reason**: AE-BP 적응적 소거 BP 디코딩, 불안정 메시지 소거하는 신규 LDPC 디코더 — 이식 가능 디코더(C)
- **ID**: ieee:5331673
- **Type**: conference
- **Published**: 25-27 Aug.
- **Authors**: Chaonian Guo, Xiangxue Li, Dong Zheng +2
- **PDF**: https://ieeexplore.ieee.org/document/5331673
- **Abstract**: In the decoding process of LDPC codes, variable node messages often fluctuate continuously and thereby become the hindrance to the successful decoding. This paper proposes an Adaptive Erasure Belief Propagation (AE-BP) decoding algorithm to reduce the influence of these unreliable messages. The idea behind AE-BP is recording the continuous fluctuant times of variable nodes by introducing a sequence of counters, and then adaptively erasing the messages according to their fluctuant times so that other messages would recover to more precise states. Semi-Gaussian approximation demonstrates adaptive erasure is a good candidate towards offsetting the defect of unreliable messages. Experimental simulations show that, for LDPC codes AE-BP outperforms most decoding algorithms in the literature.

## Fully programmable layered LDPC decoder architecture

- **Status**: ✅
- **Reason**: 완전 프로그래머블 layered LDPC 디코더 아키텍처+충돌없는 매핑/스케줄링 — D 이식 가능 HW
- **ID**: ieee:7077452
- **Type**: conference
- **Published**: 24-28 Aug.
- **Authors**: Christiane Beuschel, Hans-Jörg Pfeiderer
- **PDF**: https://ieeexplore.ieee.org/document/7077452
- **Abstract**: We present a fully programmable layered LDPC decoder architecture together with an optimum mapping and scheduling algorithm. In contrast to other designs proposed in the literature, we use one-phase message passing. This allows for the first time the design of a fully programmable layered decoder. The proposed mapping and scheduling algorithm exploits the full parallelism of the architecture at any time for any code, which means that the mapping algorithm achieves collision-free memory access and 100% utilization of the architecture. Compared to existing programmable designs without layered decoding we double the data throughput. The parallelism of the architecture is unconstrained and fully scalable so that hardware cost and data throughput can be exchanged with fine granularity.

## Soft LDPC decoding in nonlinear channels with Gaussian processes for classification

- **Status**: ❌
- **Reason**: 비선형 채널 GPC 기반 등화기 제안, LDPC는 성능평가용 후단일 뿐 떼어낼 디코더 기법 없음
- **ID**: ieee:7077392
- **Type**: conference
- **Published**: 24-28 Aug.
- **Authors**: Pablo Martínez-Olmos, Juan José Murillo-Fuentes, Fernando Pérez-Cruz
- **PDF**: https://ieeexplore.ieee.org/document/7077392
- **Abstract**: In this paper, we propose a new approach for nonlinear equalization based on Gaussian processes for classification (GPC). We also measure the performance of the equalizer after a low-density parity-check channel decoder has detected the received sequence. Typically, most channel equalizers concentrate on reducing the bit error rate, instead of providing accurate posterior probability estimates. GPC is a Bayesian nonlinear classification tool that provides accurate posterior probability estimates with short training sequences. We show that the accuracy of these estimates is essential for optimal performance of the channel decoder and that the error rate outputted by the equalizer might be irrelevant to understand the performance of the overall communication receiver. We compare the proposed equalizers with state-of-the-art solutions.

## Blind time-period synchronization for LDPC Convolutionally Coded transmission

- **Status**: ❌
- **Reason**: LDPC-CC 블라인드 시간동기화 기법, 무선 동기화 특이적이며 떼어낼 디코더/HW/코드 기법 없음
- **ID**: ieee:7077660
- **Type**: conference
- **Published**: 24-28 Aug.
- **Authors**: Čedomir Stefanović, Dejan Vukobratović, Dragana Bajić +2
- **PDF**: https://ieeexplore.ieee.org/document/7077660
- **Abstract**: In this paper we propose a scheme for blind time-period synchronization of Low-Density Parity-Check Convolutional Codes (LDPC CC) over the AWGN channel. Reliable time-period synchronization for LDPC CC coded transmission is a requirement for successful decoding at the receiving end. The proposed scheme exploits parity-check constraints incorporated into LDPC CC coded stream, and variants based both on the hard and soft-detected symbols are presented. We show that time-period synchronization can be acquired during the time-frame of one LDPC CC time period, which is considerably faster and less complex when compared to the block LDPC coded transmission of similar performance. Additionally, by appending the time-period synchronization preprocessors, we effectively incorporate the time-period synchronization into the iterative LDPC CC decoder “pipeline” structure. Our simulation study demonstrates flexibility and excellent performance of the proposed scheme.

## On distributed arithmetic codes and syndrome based turbo codes for Slepian-Wolf coding of non uniform sources

- **Status**: ❌
- **Reason**: 분산 산술부호+turbo의 Slepian-Wolf 분산소스코딩, LDPC 아님이며 소스코딩 영역
- **ID**: ieee:7077599
- **Type**: conference
- **Published**: 24-28 Aug.
- **Authors**: V. Toto-Zarasoa, E. Magli, A. Roumy +1
- **PDF**: https://ieeexplore.ieee.org/document/7077599
- **Abstract**: We consider the use of source codes and channel codes for asymmetric distributed source coding of non uniform correlated sources. In particular, we use distributed arithmetic codes as source codes and syndrome based turbo codes as channel codes. We compare the advantages and drawbacks of the two systems for different source probabilities and different compression ratio. We show that prior knowledge of the source distribution improves the performance of both approaches in terms of their distances to the Slepian-Wolf bound. Turbo codes are better when the puncturing is low, while distributed arithmetic codes are less impacted by the change of compression rate.

## On the performance and numerical stability of soft-decision Reed-Solomon decoding

- **Status**: ✅
- **Reason**: soft-decision RS의 ABP 디코딩 고정소수점 양자화 분석 — 부호 비의존적 BP 양자화/HW 기법으로 바이너리 LDPC BP에 이식 가능(C/D 예외)
- **ID**: ieee:7077766
- **Type**: conference
- **Published**: 24-28 Aug.
- **Authors**: Marcel Bimberg, Emil Matúš, Gerhard P. Fettweis
- **PDF**: https://ieeexplore.ieee.org/document/7077766
- **Abstract**: In this paper we numerically analyze soft-decision Reed-Solomon decoding based on adaptive Belief Propagation (ABP) algorithm in an additive white Gaussian noise (AWGN) and Rayleigh fading environment. We compare modifications of ABP in terms of frame-error-rate performance and decoding latency, while focusing on efficient implementations in software or hardware. Main outcome of the paper is the analysis of quantization effects when ABP is implemented employing fixed-point values.

## Network low density parity check codes designed for multiple-access relay channel

- **Status**: ❌
- **Reason**: 멀티액세스 릴레이용 network LDPC(네트워크코딩 결합) 설계 - NAND ECC에 떼어낼 기법 없는 응용 특이적
- **ID**: ieee:5291317
- **Type**: conference
- **Published**: 23-26 Aug.
- **Authors**: Guanghui Song, Ying Li, Jun Cheng +1
- **PDF**: https://ieeexplore.ieee.org/document/5291317
- **Abstract**: A relay scheme combining network coding with channel coding is proposed for multiple-access relay channel. Via a newly designed network low density parity check code, this scheme permits the relay node to jointly encode the data information from two source nodes. To predict the system performance, a newly generalized Gaussian approximation algorithm is derived, based on which an optimization algorithm is developed to search the degree distribution of the network LDPC code. Simulations show that, in a network with two sources, one relay and one destination, the system with the designed network low density parity check code hold a performance gap less than 0.6 dB from the threshold and a performance gain of about 0.3 dB can be achieved to the same rate XOR network coding scheme at BER = 10-5.

## Low density parity check codes for dedicated short range communication (DSRC) systems

- **Status**: ❌
- **Reason**: DSRC IVC에 표준 regular LDPC를 convolutional code와 성능 비교만; 새 디코더·구성 없음, 응용 특이적
- **ID**: ieee:5291266
- **Type**: conference
- **Published**: 23-26 Aug.
- **Authors**: Najmeh Khosroshahi, T. Aaron Gulliver
- **PDF**: https://ieeexplore.ieee.org/document/5291266
- **Abstract**: In this paper, we consider the performance of a dedicated short range communication (DSRC) system for inter-vehicle communications (IVC). The DSRC standard employs convolutional codes for forward error correction (FEC). The performance of the DSRC system is evaluated in three different channels with convolutional codes and regular LDPC codes. In addition, we compare the complexity of these codes. It is shown that LDPC codes provide a significant improvement in performance with similar complexity to convolutional codes.

## M-ary hyper phase-shift keying over non-linear satellite channels

- **Status**: ❌
- **Reason**: MHPSK 변조+RS/DVB-LDPC 베이스라인 위성통신 비교; LDPC 부수 언급, 떼어낼 기법 없음
- **ID**: ieee:5291402
- **Type**: conference
- **Published**: 23-26 Aug.
- **Authors**: James Caldwell, Clark Robertson
- **PDF**: https://ieeexplore.ieee.org/document/5291402
- **Abstract**: Forward error correction (FEC) coding in conjunction with M-ary hyper phase-shift keying (MHPSK) is considered in order to improve the robustness of a high spectral efficiency, non-linear satellite communications link. MHPSK is a spectrally efficient modulation technique that uses four orthonormal basis functions to increase the Euclidean distance between different symbols in the signal space. The use of four orthonormal basis functions provides an advantage over traditional spectrally efficient modulation techniques such as M-ary phase-shift keying (MPSK) and M-ary quadrature amplitude modulation (MQAM) that only possess two degrees of freedom. MHPSK offers an improvement in probability of bit error performance over other spectrally efficient modulation techniques for the same average energy per bit-to-noise power spectral density ratio and the same spectral efficiency. As a result, MHPSK offers a novel way to improve both throughput and reduce power requirements using easy to generate waveforms. MHPSK and two-subcarrier orthogonal frequency division multiplexing (OFDM) with 8-PSK or 8-QAM on each subcarrier are compared in terms of the effect of peak-to-average power ratio and required amplifier backoff on the probability of bit error. In this paper, long block length Reed Solomon (RS) codes are used to encode information symbols which are then transmitted with MHPSK. Additionally, a comparison is made with two-subcarrier OFDM that uses 8-PSK or 8-QAM on each subcarrier and utilizing the Digital Video Broadcast (DVB) standard rate 0.9 low density parity check (LDPC) code commonly employed in non-linear satellite communications. As such, MHPSK and two-subcarrier OFDM with 8-QAM or 8-PSK on each subcarrier are compared in terms of probability of bit error, peak-to-average power ratio, amplifier backoff, and bandwidth efficiency using long forward error correction code block lengths.

## A novel UEP Daul-Segment-Check H-ARQ

- **Status**: ❌
- **Reason**: UEP H-ARQ 메커니즘(FEC+ARQ+CRC), LDPC 비특정 FEC이고 떼어낼 디코더/구성 기법 없음
- **ID**: ieee:5276980
- **Type**: conference
- **Published**: 20-22 Aug.
- **Authors**: Zhibin Gao, Lianfen Huang, Yan Yao +1
- **PDF**: https://ieeexplore.ieee.org/document/5276980
- **Abstract**: In order to make multimedia data transmission more robust and meet QoS requirements over wireless channel, Forward Error Correction codes (FEC) are joint with Automatic Repeat-reQuest (ARQ) and a novel Dual-Segment-Check CRC, to form hybrid ARQ (H-ARQ) mechanism, making the system not only have strong error correcting capability and high throughput, but also can adaptively adjust code rate as channel state changes.

## Analysis of QIM-based audio watermarking using LDPC codes

- **Status**: ❌
- **Reason**: 오디오 워터마킹(QIM/DM)에 표준 Margulis LDPC를 그대로 사용, 신규 부호/디코더 기여 없음
- **ID**: ieee:5235992
- **Type**: conference
- **Published**: 2-5 Aug. 2
- **Authors**: R. Martinez-Noriega, M. Nakano, B. Kurkoski +2
- **PDF**: https://ieeexplore.ieee.org/document/5235992
- **Abstract**: In this paper, we analyze audio watermarking methods based on quantization index modulation and low-density parity-check (LDPC) codes. We found that dither modulation (DM) can achieve better performance using half-rate Margulis LDPC code even better than some low-rate codes. Then, we propose a scheme based on LDPC codes and DM with distortion-compensation (DC) property which has a robustness benefit of 6 dB versus uncoded case, 2 dB versus algebraic codes, 1 dB versus DM with LDPC code. In DM with DC property, we show that it is possible to achieve. 5 dB better robustness using a scale parameter alpha lower than the theoretically optimal and LDPC codes. Finally our proposal was evaluated against more practical attacks. These results show that our scheme could be a good option for robust watermarks.

## Development of a high throughput LDPC codec with 1Gb/s and OFDM transmission system utilizing MBD

- **Status**: ✅
- **Reason**: 고처리율 LDPC 코덱 HW 설계/평가 환경(MBD) — 이식 가능 HW 아키텍처(D), 애매하나 살림
- **ID**: ieee:5332794
- **Type**: conference
- **Published**: 18-21 Aug.
- **Authors**: Takashi Maehata
- **PDF**: https://ieeexplore.ieee.org/document/5332794
- **Abstract**: Low-density parity-check (LDPC) codes, which are among the most powerful error correcting codes, can achieve performance close to the Shannon limit. It is difficult to evaluate the performance of LDPC codes by software simulation only, because it takes much time and labor. To solve this problem, we have developed the design environment for designing and evaluating LDPC codes on hardware.

## Density Evolution and Thresholds for Accumulate Repeat Tree Codes in Mobile Communication Systems

- **Status**: ❌
- **Reason**: ART(accumulate repeat tree) turbo-like 부호의 density evolution/threshold 분석, LDPC 자체가 아닌 새 부호족 이론, 떼어낼 바이너리 LDPC 기법 없음
- **ID**: ieee:5364641
- **Type**: conference
- **Published**: 14-16 Aug.
- **Authors**: Maofan Yang, Hua Zhou, Xin Zhang +1
- **PDF**: https://ieeexplore.ieee.org/document/5364641
- **Abstract**: Channel coding theories are widely used in computer science and communication systems. This paper proposes a novel channel coding scheme called accumulate repeat tree (ART) codes for improving the channel coding performance in mobile communication systems. This class of codes can be viewed as turbo-like codes combining many advantages of turbo codes and low-density parity-check (LDPC) codes. ART codes can be represented by the Bayesian network and Tanner graph, which allows for high-speed iterative decoding implementation using belief-propagation (BP) algorithm. The density evolution method is presented, and the practicable Gaussian approximation algorithm for ART codes to analyze the thresholds and decoding performance is discussed. ART codes have low coding complexity, and they show good performance improvement by simulation.

## Extended PEG Algorithm for High Rate LDPC Codes

- **Status**: ✅
- **Reason**: 고율 LDPC용 확장 PEG 알고리즘으로 girth 보장 코드 구성, 바이너리 코드설계 기법 이식 가능(E)
- **ID**: ieee:5207892
- **Type**: conference
- **Published**: 10-12 Aug.
- **Authors**: Zhiheng Zhou, Xiangxue Li, Dong Zheng +2
- **PDF**: https://ieeexplore.ieee.org/document/5207892
- **Abstract**: Progressive Edge-Growth(PEG) Algorithm is a good candidate to generate Tanner Graphs with a large girth by establishing edges or connections between symbol and check nodes in an edge-by-edge manner. In this paper, we propose an extended PEG algorithm for constructing Low-Density Parity-Check (LDPC) codes with very high rate when given a lower bound of girth. Simulation results show the bit error rates of constructed LDPC codes with very high rate or large girth.
