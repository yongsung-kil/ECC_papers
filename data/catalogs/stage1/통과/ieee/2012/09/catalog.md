# IEEE Xplore — 2012-09 (1차선별 통과)


## New Combinatorial Construction Techniques for Low-Density Parity-Check Codes and Systematic Repeat-Accumulate Codes

- **Status**: ✅
- **Reason**: 조합설계 기반 신규 LDPC(및 RA) 구성 기법, column-weight 3+ 구조화 부호 설계(E) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6241375
- **Type**: journal
- **Published**: September 
- **Authors**: Alexander Gruner, Michael Huber
- **PDF**: https://ieeexplore.ieee.org/document/6241375
- **Abstract**: This paper presents several new construction techniques for low-density parity-check (LDPC) and systematic repeat-accumulate (RA) codes. Based on specific classes of combinatorial designs, the improved code design focuses on high-rate structured codes with constant column weights 3 and higher. The proposed codes are efficiently encodable and exhibit good structural properties. Experimental results on decoding performance with the sum-product algorithm show that the novel codes offer substantial practical application potential, for instance, in high-speed applications in magnetic recording and optical communications channels.

## A 5.79-Gb/s Energy-Efficient Multirate LDPC Codec Chip for IEEE 802.15.3c Applications

- **Status**: ✅
- **Reason**: 65nm LDPC 코덱 칩: layered NMS, 재구성형 sorter, 라우팅 최적화 등 이식 가능 HW 아키텍처(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:6198294
- **Type**: journal
- **Published**: Sept. 2012
- **Authors**: Shao-Wei Yen, Shiang-Yu Hung, Chih-Lung Chen +3
- **PDF**: https://ieeexplore.ieee.org/document/6198294
- **Abstract**: An LDPC codec chip supporting four code rates of IEEE 802.15.3c applications is presented. After utilizing row-based layered scheduling, the normalized min-sum (NMS) algorithm can reduce half of the iteration number while maintaining similar performance. According to the unique code structure of the parity-check matrix, a reconfigurable 8/16/32-input sorter is designed to deal with LDPC codes in four different code rates. Both sorter input reallocation and pre-coded routing switch are proposed to alleviate routing complexity, leading to 64% input reduction of multiplexers. In addition, an adder-accumulator-shift register (AASR) circuit is proposed for the LDPC encoder to reduce hardware complexity. After implemented in 65-nm 1P10M CMOS process, the proposed LDPC decoder chip can achieve maximum 5.79-Gb/s throughput with the hardware efficiency of 3.7 Gb/s/mm2 and energy efficiency of 62.4 pJ/b, respectively.

## Reweighted LP Decoding for LDPC Codes

- **Status**: ✅
- **Reason**: Reweighted LP decoding for binary LDPC codes - novel decoder algorithm (C), 부호 비의존적이고 BP/LP 디코더 개선 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6210385
- **Type**: journal
- **Published**: Sept. 2012
- **Authors**: Amin Khajehnejad, Alexandros G. Dimakis, Babak Hassibi +2
- **PDF**: https://ieeexplore.ieee.org/document/6210385
- **Abstract**: We introduce a novel algorithm for decoding binary linear codes by linear programming (LP). We build on the LP decoding algorithm of Feldman  and introduce a postprocessing step that solves a second linear program that reweights the objective function based on the outcome of the original LP decoder output. Our analysis shows that for some LDPC ensembles we can improve the provable threshold guarantees compared to standard LP decoding. We also show significant empirical performance gains for the reweighted LP decoding algorithm with very small additional computational complexity.

## On LDPC codes corresponding to infinite family of graphs A(k, K)

- **Status**: ✅
- **Reason**: E: 새 무한 극단그래프족 A(k,K) 기반 LDPC 구성 - 신규 그래프기반 코드설계 기법(바이너리)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6354445
- **Type**: conference
- **Published**: 9-12 Sept.
- **Authors**: Monika Polak, Vasyl Ustimenko
- **PDF**: https://ieeexplore.ieee.org/document/6354445
- **Abstract**: In this paper we investigate correcting properties of LDPC error correcting codes obtained from new infinite family of special extremal graphs. We describe how to construct these codes and compare our results with codes obtained by Guinand and Lodge, corresponding to family of graphs D(k, q).

## Performance and complexity analysis of channel coding schemes for multi-Gbps wireless communications

- **Status**: ✅
- **Reason**: C/D: min-sum layered 디코더의 감쇠계수·유한어장·early-termination HW 파라미터 분석+40nm 합성 - 이식 가능 디코더/HW 기법
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6362670
- **Type**: conference
- **Published**: 9-12 Sept.
- **Authors**: Miroslav Marinkovic, Milos Krstic, Eckhard Grass +1
- **PDF**: https://ieeexplore.ieee.org/document/6362670
- **Abstract**: In this paper, a trade-off analysis between concatenated codes consisting of a convolutional (CC) followed by a Reed-Solomon (RS) code versus low-density parity-check (LDPC) codes is presented. The analysis is based on a twofold criterion: coding gain for a target bit error rate (BER) of 10-6 and required decoder hardware complexity for a target data throughput of 10 Gbps. Furthermore, we have investigated relevant parameters which directly impact an efficient hardware implementation as well as the error correction performance of the LDPC decoder. These parameters include an attenuation factor in the min-sum layered (MSL) decoding algorithm, the finite word length of soft information and an early-termination (ET) strategy. The error correction performances are evaluated for 16-QAM modulation over an independent Rayleigh fading channel. The complexity of the RS-CC and LDPC decoders is estimated based on synthesis results using an Infineon 40 nm CMOS design kit.

## Design of irregular LDPC codes with degree-set and degree-sum distributions

- **Status**: ✅
- **Reason**: E: degree-set/degree-sum 분포로 irregular LDPC 앙상블 설계, waterfall-error floor 트레이드오프 - 신규 코드설계 기법(바이너리)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6362668
- **Type**: conference
- **Published**: 9-12 Sept.
- **Authors**: Min Jang, Jin Whan Kang, Sang-Hyo Kim
- **PDF**: https://ieeexplore.ieee.org/document/6362668
- **Abstract**: In this paper, we introduce new attributes of low-density parity-check graphs, degree-set and degree-sum, which explains the connectivity of a check node with more detail. Then, we consider more specified ensembles defined by degree-set/sum distribution of the graph than one defined by the degree distribution. As the degree set/sum distribution varies, tradeoff between the performance at the waterfall and that at the error-floor is observed. The trade-off point can be managed by controlling degree-set/sum distribution.

## Low-density parity-check codes based on the independent subgroups

- **Status**: ✅
- **Reason**: 독립 부분군 기반 바이너리 정규 LDPC 신규 구성, 4-cycle 제거 — E 코드설계
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6338401
- **Type**: conference
- **Published**: 5-10 Sept.
- **Authors**: Fedor Ivanov, Victor Zyablov, Vladimir Potapov
- **PDF**: https://ieeexplore.ieee.org/document/6338401
- **Abstract**: Two criteria of cyclic subgroups independence are proved. The ensemble of regular binary LDPC codes which are based on independent subgroups, is built. The condition of absence of the cycles of the length 4 is proved for the resulting code construction. The results of the received code constructions are presented for the iterative algorithm Sum-Product when the codeword is transmitted over channel with additive Gaussian white noise (AGWN).

## Effects of belief propagation computational precision on LDPC codes error floors

- **Status**: ✅
- **Reason**: BP 디코더 연산정밀도가 error floor·pseudo-codeword에 미치는 영향 — C 디코더 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6338417
- **Type**: conference
- **Published**: 5-10 Sept.
- **Authors**: Igor Zhilin, Victor Zyablov
- **PDF**: https://ieeexplore.ieee.org/document/6338417
- **Abstract**: The influence of the computational precision used in BP decoder on LDPC codes performance is studied. It is shown that an error floor can be lowered and pseudo-codewords are made possible to decode by increasing computational precision.

## Finite-length performance of spatially-coupled LDPC codes under TEP decoding

- **Status**: ✅
- **Reason**: SC-LDPC 유한길이 성능을 TEP 디코더+window-sliding으로 개선; 신규 디코더 알고리즘이나 erasure 채널 한정이라 Phase3 재검토(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6404722
- **Type**: conference
- **Published**: 3-7 Sept. 
- **Authors**: Pablo M. Olmos, Fernando Pérez-Cruz, Luis Salamanca +1
- **PDF**: https://ieeexplore.ieee.org/document/6404722
- **Abstract**: Spatially-coupled (SC) LDPC codes are constructed from a set of L regular sparse codes of length M. In the asymptotic limit of these parameters, SC codes present an excellent decoding threshold under belief propagation (BP) decoding, close to the maximum a posteriori (MAP) threshold of the underlying regular code. In the finite-length regime, we need both dimensions, L and M, to be sufficiently large, yielding a very large code length and decoding latency. In this paper, and for the erasure channel, we show that the finite-length performance of SC codes is improved if we consider the tree-structured expectation propagation (TEP) algorithm in the decoding stage. When applied to the decoding of SC LDPC codes, it allows using shorter codes to achieve similar error rates. We also propose a window-sliding scheme for the TEP decoder to reduce the decoding latency.

## Efficient termination of spatially-coupled codes

- **Status**: ✅
- **Reason**: SC-LDPC 종료(termination)/rate-loss 절감 코드 설계 기법(E), 바이너리
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6404682
- **Type**: conference
- **Published**: 3-7 Sept. 
- **Authors**: Koji Tazoe, Kenta Kasai, Kohichi Sakaniwa
- **PDF**: https://ieeexplore.ieee.org/document/6404682
- **Abstract**: Spatially-coupled low-density parity-check codes attract much attention due to their capacity-achieving performance and a memory-efficient sliding-window decoding algorithm. On the other hand, the encoder needs to solve large linear equations to terminate the encoding process. In this paper, we propose modified spatially-coupled codes. The modified (dl, dr, L) codes have less rate-loss, i.e., higher coding rate, and have the same threshold as (dl, dr, L) codes and are efficiently terminable by using an accumulator.

## Approaching maximum likelihood decoding of finite length LDPC codes via FAID diversity

- **Status**: ✅
- **Reason**: FAID diversity로 유한길이 regular LDPC BP 이상 ML 근접 디코딩, 이식 가능 신규 디코더 알고리즘(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6404721
- **Type**: conference
- **Published**: 3-7 Sept. 
- **Authors**: David Declercq, Erbao Li, Bane Vasić +1
- **PDF**: https://ieeexplore.ieee.org/document/6404721
- **Abstract**: We introduce a generic approach, called FAID diversity, for improving the error correction capability of regular low-density parity check codes, beyond the belief propagation performance. The method relies on operating a set of finite alphabet iterative decoders (FAID). The message-passing update rules are interpreted as discrete dynamical systems, and are judiciously chosen to ensure that decoders have different dynamics on a specific finite-length code. An algorithm is proposed which uses random jumps in the iterative message passing trajectories, such that the system is not trapped in periodic attractors. We show by simulations that the FAID diversity approach with random jumps has the potential of approaching the performance of maximum-likelihood decoding for finite-length regular, column-weight three codes.

## Constructing good QC-LDPC codes by pre-lifting protographs

- **Status**: ✅
- **Reason**: QC-LDPC pre-lifting protograph 구성으로 min-distance/girth 개선하는 신규 코드 설계(E), 바이너리
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6404658
- **Type**: conference
- **Published**: 3-7 Sept. 
- **Authors**: David G. M. Mitchell, Roxana Smarandache, Daniel J. Costello
- **PDF**: https://ieeexplore.ieee.org/document/6404658
- **Abstract**: Quasi-cyclic (QC) low-density parity-check (LDPC) codes are of great interest to code designers because of their implementation advantages and algebraic properties that facilitate their analysis. In this paper, we present some new results on QC-LDPC codes that are constructed using a two-step lifting procedure based on a protograph, and, by implementing this method instead of the usual one-step procedure, we are able to show improved minimum distance and girth properties. We also present two design rules to construct QC-LDPC codes: one uses only circulant permutation matrices at the first (pre-lifting) stage and the other uses a selection of non-commuting permutation matrices. For both techniques, we obtain a demonstrable increase in the minimum distance compared to a one-step circulant-based lifting. The expected performance improvement is verified by simulation results.

## Reduced complexity window decoding schedules for coupled LDPC codes

- **Status**: ✅
- **Reason**: SC-LDPC window decoding 메시지패싱 스케줄로 복잡도 절감하는 디코더 기법(C), 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6404660
- **Type**: conference
- **Published**: 3-7 Sept. 
- **Authors**: Najeeb ul Hassan, Ali E. Pusane, Michael Lentmaier +2
- **PDF**: https://ieeexplore.ieee.org/document/6404660
- **Abstract**: Window decoding schedules are very attractive for message passing decoding of spatially coupled LDPC codes. They take advantage of the inherent convolutional code structure and allow continuous transmission with low decoding latency and complexity. In this paper we show that the decoding complexity can be further reduced if suitable message passing schedules are applied within the decoding window. An improvement based schedule is presented that easily adapts to different ensemble structures, window sizes, and channel parameters. Its combination with a serial (on-demand) schedule is also considered. Results from a computer search based schedule are shown for comparison.

## Suppressing pseudocodewords by penalizing the objective of LP decoding

- **Status**: ✅
- **Reason**: ADMM 기반 LP 디코딩에 penalty로 pseudocodeword 억제, error floor 없는 신규 바이너리 LDPC 디코더(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6404695
- **Type**: conference
- **Published**: 3-7 Sept. 
- **Authors**: Xishuo Liu, Stark C. Draper, Benjamin Recht
- **PDF**: https://ieeexplore.ieee.org/document/6404695
- **Abstract**: In this paper, we present a new class of decoders for low density parity check (LDPC) codes. We are motivated by the observation that the linear programming (LP) decoder has worse error performance than belief propagation (BP) decoders at low SNRs. We base our new decoders on the alternating direction method of multipliers (ADMM) decomposition technique for LP decoding. The ADMM not only efficiently solves the LP decoding problem, but also makes it possible to explore other decoding algorithms. In particular, we add various penalty terms to the linear objective of LP decoding with the goal of suppressing pseudocodewords. Simulation results show that the new decoders achieve much better error performance compared to LP decoder at low SNRs. What is more, similar to the LP decoder, no error floor is observed at high SNRs.

## Hybrid Construction of Long LDPC Codes with Very Low Density

- **Status**: ✅
- **Reason**: 대수+랜덤 하이브리드 LDPC 구성으로 girth>=6 보장, 저밀도 장부호 구성기법(E) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6398982
- **Type**: conference
- **Published**: 3-6 Sept. 
- **Authors**: Lijun Zhang, Yanjing Zhang, L. L. Cheng
- **PDF**: https://ieeexplore.ieee.org/document/6398982
- **Abstract**: By combining an algebraic method and a random method, a hybrid method is proposed to construct LDPC codes, which can easily ensure the girth is at least six. The complexity of construction for the hybrid code is only a fraction of that for PEG code, which facilitates the construction of long LDPC codes with very low density. Simulation results show that the hybrid code from EG-LDPC code and PEG code has the identical error performance and convergence rate to the PEG code with the same length.

## A Puncturing Scheme for Low-Density Parity-Check Codes Based on 1-SR Nodes

- **Status**: ✅
- **Reason**: 1-SR 노드 기반 rate-compatible 펑처링 기법은 바이너리 LDPC 부호설계(E)로 NAND ECC에 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6398903
- **Type**: conference
- **Published**: 3-6 Sept. 
- **Authors**: Lijun Zhang, Fuli Ma, L. L. Cheng
- **PDF**: https://ieeexplore.ieee.org/document/6398903
- **Abstract**: A rate-compatible puncturing scheme for LDPC codes is proposed based on the fact that a one-step recoverable (1-SR) node is more reliable than a k-SR node (k>;1) and a 1-SR node with more survived check nodes can be recovered more reliably in a recovery tree, so the scheme tries to obtain 1-SR nodes which have multiple survived check nodes as many as possible. Simulation results show that the puncturing scheme has better performance than both the random puncturing scheme and the novel method in [5].

## An Efficient Method of Constructing Quasi-Cyclic Low-Density Parity-Check Codes

- **Status**: ✅
- **Reason**: EXIT+수정 PEG로 비정규 QC-LDPC 구성 및 단주기 제거 시프트 최적화, 바이너리 부호설계(E) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6398992
- **Type**: conference
- **Published**: 3-6 Sept. 
- **Authors**: Zhanji Wu, Jiao Cheng
- **PDF**: https://ieeexplore.ieee.org/document/6398992
- **Abstract**: An efficient method of constructing irregular quasi-cyclic (QC) low-density parity-check (LDPC) codes is proposed. In order to find the degree distribution with low convergence threshold, the extrinsic information transfer (EXIT) chart is utilized to optimize the degree distribution of LDPC codes. Then, a modified progressive edge growth (PEG) algorithm is used to get the mask matrix with the optimal degree distribution. Finally, the parity-check matrix of QC LDPC code is constructed based on the mask matrix, and the shift values are optimized to eliminate short cycles. Simulation results show that the constructed irregular QC LDPC codes with optimized degree distribution significantly outperform the regular QC LDPC codes in the additive white Gaussion noise (AWGN) channel.

## A Novel Hybrid ARQ Scheme Based on LDPC Code Extension and Feedback

- **Status**: ✅
- **Reason**: E/C: rate-compatible LDPC puncturing/extending+PEG mother code 설계, BP 디코더 결합 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6399337
- **Type**: conference
- **Published**: 3-6 Sept. 
- **Authors**: Hamid Saber, Ian Marsland
- **PDF**: https://ieeexplore.ieee.org/document/6399337
- **Abstract**: The design of an efficient hybrid automatic repeat request (ARQ) scheme based on rate compatible low density parity check (LDPC) codes is considered. It has been shown that extending as well as puncturing of LDPC codes can produce good rate compatible LDPC codes for the additive white Gaussian noise channel. One issue with the traditional LDPC-based hybrid ARQ methods is that the throughput drops off significantly at low signal-to-noise ratios (SNRs). In this paper we introduce a coding scheme which is capable of using puncturing, extending and feedback at the same time to address this issue. Appropriate choice of feedback functions along with optimum combining of received signals for the belief propagation decoder mitigates the throughput drop- off issue at low SNRs, while having a small feedback overhead from the receiver. A powerful mother code is generated via the progressive edge growth algorithm and is used for puncturing and extending in the proposed scheme. Clustering the codewords of the longest codebook is used to decrease the overhead of the feedback connection. Simulation analysis of the throughput shows that our scheme could get as close as 0.5 dB to the Shannon limit while having up to 2 dB gain compared to previous works at low SNRs.

## Low Complexity Progressive Edge-Growth Algorithm Based on Chinese Remainder Theorem

- **Status**: ✅
- **Reason**: CRT 기반 저복잡도 PEG 확장 구성+HW on-the-fly 확장, 바이너리 LDPC 부호설계/HW(E/D) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6399027
- **Type**: conference
- **Published**: 3-6 Sept. 
- **Authors**: Xueqin Jiang, Papa Ousmance Thiaw Diagne, Moon Ho Lee +1
- **PDF**: https://ieeexplore.ieee.org/document/6399027
- **Abstract**: Progressive edge-growth (PEG) algorithm construction builds the Tanner graph for an LDPC code by establishing edges between the symbol nodes and the check nodes in an edge-by-edge manner and maximizing the local girth in a greedy fashion. This approach is simple but the computational complexity of the PEG algorithm scale as O(nm), where n is the number of symbol nodes and m is the number of check nodes. We deal with this problem by first construct a base LDPC code of length n1 with the PEG algorithm and then extend this LDPC code into an LDPC code of length n, where n ≥ n1, via the the chinese remainder theorem (CRT). This method increase the code length of an LDPC code generated with the PEG algorithm, without decreasing its girth. Due to the code length reducing in the PEG construction step, the computational complexity of the whole code construction process is reduced. Furthermore, the proposed algorithm have a potential advantage by storing a small parity-check matrix of a base code and extending it “on-the-fly” in hardware.

## A New Genetics-Aided Message Passing Decoding Algorithm for LDPC Codes

- **Status**: ✅
- **Reason**: C: 유전알고리즘 보조 메시지패싱(GA-MP) 디코더, 바이너리 LDPC BP 개선 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6399254
- **Type**: conference
- **Published**: 3-6 Sept. 
- **Authors**: Jui-Hui Hung, Yi-De Lu, Sau-Gee Chen
- **PDF**: https://ieeexplore.ieee.org/document/6399254
- **Abstract**: The popular LDPC decoding algorithms based on the message passing (MP) algorithm have high decoding performances. However, they are noticeably inferior to the maximum likelihood (ML) decoding algorithm. This work proposes a genetics-aided message passing (GA-MP) algorithm by applying a new genetic algorithm to MP algorithm. As a result, significantly performance improvement over MP algorithm can be achieved. Besides, compared with other genetic-aided decoding algorithms, the proposed algorithm has much better performances and much lower computational complexity. Simulations show that the decoding performance of GA-MP algorithm can achieve performances very close to the algorithm, while outperform MP algorithm. Besides, its performance will grow proportionally with the generation number without leveling off as observed in conventional MP algorithms, under high SNR condition.

## Approximated sum-product decoding for LDPC codes

- **Status**: ✅
- **Reason**: C: 근사 sum-product 디코더(곱셈·메모리·채널정보 불요, 정수연산), NAND 디코더 이식 적합
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6336445
- **Type**: conference
- **Published**: 3-5 Sept. 
- **Authors**: Sung Ik Park, Heung Mook Kim, Jeongchang Kim
- **PDF**: https://ieeexplore.ieee.org/document/6336445
- **Abstract**: This paper proposes an approximated sum-product decoding algorithm for LDPC codes. The proposed decoding algorithm may be efficiently implemented through integer additions, comparisons, and bit-shift operations without multiplications and memories. Moreover, it doesn't require any channel information such as signal to noise ratio and operate with just the received values from channel.

## A 45 GS/s optical soft-decision front-end

- **Status**: ✅
- **Reason**: LDPC 디코더용 soft-decision front-end(LLR 양자화/soft-input HW)는 NAND read soft-input 양자화 HW로 이식 가능 가능성, 애매하여 in
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:6358728
- **Type**: conference
- **Published**: 23-27 Sept
- **Authors**: M. N. Sakib, M. Moayedi, O. Liboiron-Ladouceur
- **PDF**: https://ieeexplore.ieee.org/document/6358728
- **Abstract**: A low complexity 45 GS/s soft-decision optical front-end is demonstrated for low-density parity-check (LDPC) decoders. A net coding gain of 7.06 dB at 10-7 is experimentally achieved for 45 Gb/s NRZ-OOK optical signal.

## Tree-structured expectation propagation for LDPC decoding over the AWGN channel

- **Status**: ✅
- **Reason**: Tree-structured expectation propagation 디코더 — 표준 BP 대비 유한길이 게인·error floor 개선, 이식 가능한 신규 디코더 알고리즘(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6349716
- **Type**: conference
- **Published**: 23-26 Sept
- **Authors**: Luis Salamanca, Juan José Murillo-Fuentes, Pablo M. Olmos +1
- **PDF**: https://ieeexplore.ieee.org/document/6349716
- **Abstract**: In this paper, we propose the tree-structured expectation propagation (TEP) algorithm for low-density parity-check (LDPC) decoding over the additive white Gaussian noise (AWGN) channel. By imposing a tree-like approximation over the graphical model of the code, this algorithm introduces pairwise marginal constraints over pairs of variables, which provide joint information of the variables related. Thanks to this, the proposed TEP decoder improves the performance of the standard belief propagation (BP) solution. An efficient way of constructing the tree-like structure is also described. The simulation results illustrate the TEP decoder gain in the finite-length regime, compared to the standard BP solution. For code lengths shorter than n = 512, the gain in the waterfall region achieves up to 0.25 dB. We also notice a remarkable reduction of the error floor.

## Two Efficient Algorithms Based on Majority-Logic and Min-Sum Algorithms for LDPC Codes

- **Status**: ✅
- **Reason**: 바이너리 EG/PG-LDPC용 신규 ISRB-MS/MISRB-MS 디코더(정수연산·저복잡도 min-sum 변형), 이식 가능 디코더 알고리즘(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6478732
- **Type**: conference
- **Published**: 21-23 Sept
- **Authors**: Zuotao Zhang, Yibo Fang, Guanghui Liu
- **PDF**: https://ieeexplore.ieee.org/document/6478732
- **Abstract**: Recently, an iterative soft information reliability-based majority-logic (ISRB-MLG) decoding algorithm was proposed for Euclidean geometry LDPC (EG-LDPC) and Projective geometry LDPC (PG-LDPC) codes. This paper first presents an iterative soft information reliability-based min-sum (ISRB-MS) decoding algorithm based on ISRB-MLG and traditional min-sum decoding algorithm. The performance of ISRB-MS algorithm is greatly improved with a little more complexity than ISRB-MLG algorithm, it mainly needs integer additions and logical operations. Different from traditional min-sum decoding algorithm, the extrinsic information transfer of ISRB-MS algorithm is simplified, we use the full information that all check nodes pass rather than the extrinsic information to update the bit nodes information. Then a modified iterative soft information reliability-based min-sum (MISRB-MS) decoding algorithm is proposed. Compared to (ISRB-MS) algorithm, MISRB-MS algorithm multiplies a scaling factor, so it needs some extra multiplication, but it achieves better performance. Simulation results show that the two algorithms achieve excellent performance and fast convergence rate, they only needs about 10 iterations, if an appropriate scaling factor is chosen, the performance of MISRB-MS algorithm very closes to that of sum-product algorithm (SPA).

## Construction of codes protographes LDPC quasi-cycliques based on an arithmetic progression

- **Status**: ✅
- **Reason**: 등차수열 기반 protograph QC-LDPC 신규 구성법(E) - girth/이진 코드설계 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6457749
- **Type**: conference
- **Published**: 18-20 Sept
- **Authors**: I. Diop, S. M. Farssi, M. Ba +1
- **PDF**: https://ieeexplore.ieee.org/document/6457749
- **Abstract**: In this document, we study the construction of codes LDPC quasi cyclic based on a protograph. In addition to their large perimeters, the presented codes take profit from the advantages of bass coding and decoding complexity. The aim of this article is to make an improvement on the implementation of quasi-cyclic LDPC codes. Thus to respect the structure of the basic protograph we use an arithmetic progression to determine in advance the positions of certain nodes of control in the derived graph, which turn to some extent amounts generating a new model while proceeding to an enlarging of the basic protograph. Once this new model conceived we apply the usual techniques to build in an optimal way the derived graph.

## Min-Sum Algorithm based efficient high level methodology for design, simulation and hardware implementation of LDPC decoders

- **Status**: ✅
- **Reason**: Min-Sum VNPU/CNPU 병렬 HW 디코더 FPGA/VHDL 구현(D) - HW 아키텍처 이식 가능
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:6457751
- **Type**: conference
- **Published**: 18-20 Sept
- **Authors**: Abdessalam. Ait Madi, Ali. Ahaitouf, Anas Mansouri
- **PDF**: https://ieeexplore.ieee.org/document/6457751
- **Abstract**: A Variable Node Processing Unit (VNPU) and a Check Node Processing Unit (CNPU) are designed in order to be used in Low Density Parity Check (LDPC) decoding by the Min-Sum Algorithm (MSA). The designed blocks are fully parallel and flexible to be used for different block length when a regular (3, 6) LDPC codes are required. The proposed VNPU and CNPU have been first designed and implemented in software using Simulink tool following a modular design approach. In a second step, these blocks were described and simulated using Very High Speed integrated circuits Hardware Description Language (VHDL). Comparison between these two implementations shows that the proposed high level methodology is efficient to test and validate digital circuits before being implemented on desired Field Programmable Gate Array (FPGA) device.

## On the generator matrix of array LDPC codes

- **Status**: ✅
- **Reason**: array LDPC 생성행렬 일반식·최소거리 최적화 조건, 바이너리 코드설계(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6347593
- **Type**: conference
- **Published**: 11-13 Sept
- **Authors**: Marco Baldi, Marco Bianchi, Giovanni Cancellieri +2
- **PDF**: https://ieeexplore.ieee.org/document/6347593
- **Abstract**: In this paper we present a general expression for the generator matrix of array low-density parity-check codes. This is a further contribution towards understanding the inner structure of these codes. Moreover, it represents a useful tool that can be used in the estimation and optimization of their minimum distance, which is an open problem. By using the new form of the generator matrix, we derive some necessary conditions on the maximization of the minimum distance.
