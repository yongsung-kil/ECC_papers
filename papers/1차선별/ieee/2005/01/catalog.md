# IEEE Xplore — 2005-01 (1차선별 통과)


## Regular and irregular progressive edge-growth tanner graphs

- **Status**: ✅
- **Reason**: PEG 알고리즘 — large-girth Tanner graph 구성, 바이너리 LDPC 코드 설계의 대표 기법(E); GF(q) 확장은 부수 언급
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1377521
- **Type**: journal
- **Published**: Jan. 2005
- **Authors**: Xiao-Yu Hu, E. Eleftheriou, D.M. Arnold
- **PDF**: https://ieeexplore.ieee.org/document/1377521
- **Abstract**: We propose a general method for constructing Tanner graphs having a large girth by establishing edges or connections between symbol and check nodes in an edge-by-edge manner, called progressive edge-growth (PEG) algorithm. Lower bounds on the girth of PEG Tanner graphs and on the minimum distance of the resulting low-density parity-check (LDPC) codes are derived in terms of parameters of the graphs. Simple variations of the PEG algorithm can also be applied to generate linear-time encodeable LDPC codes. Regular and irregular LDPC codes using PEG Tanner graphs and allowing symbol nodes to take values over GF(q) (q>2) are investigated. Simulation results show that the PEG algorithm is a powerful algorithm to generate good short-block-length LDPC codes.

## Verification-based decoding for packet-based low-density parity-check codes

- **Status**: ✅
- **Reason**: LDPC용 verification-based 디코딩(선형시간 패킷 단위 새 디코더 알고리즘) — 이식 가능 디코더(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1377496
- **Type**: journal
- **Published**: Jan. 2005
- **Authors**: M.G. Luby, M. Mitzenmacher
- **PDF**: https://ieeexplore.ieee.org/document/1377496
- **Abstract**: We introduce and analyze verification-based decoding for low-density parity-check (LDPC) codes, an approach specifically designed to manipulate data in packet-sized units. Verification-based decoding requires only linear time for both encoding and decoding and succeeds with high probability under random errors. We describe how to utilize code scrambling to extend our results to channels with errors controlled by an oblivious adversary.

## EXIT-chart properties of the highest-rate LDPC code with desired convergence behavior

- **Status**: ✅
- **Reason**: 원하는 수렴거동을 위한 최대율 LDPC 코드 설계(EXIT-chart 필요·충분조건) — 바이너리 LDPC 코드 설계 기법(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1375239
- **Type**: journal
- **Published**: Jan. 2005
- **Authors**: M. Ardakani, T.H. Chan, F.R. Kschischang
- **PDF**: https://ieeexplore.ieee.org/document/1375239
- **Abstract**: We consider uniparametric LDPC decoding schemes, i.e., the class of decoding algorithms for which an extrinsic information transfer (EXIT) chart analysis of the decoder is exact. We treat the general case of code design for a desired convergence behavior and provide necessary conditions and sufficient conditions that the EXIT chart of the maximum rate low-density parity-check code must satisfy. Our results generalize some of the existing results for the binary erasure channel: our results apply to all uniparametric decoding schemes and they apply to any desired convergence behavior.

## Tree LDPC codes for IEEE 802.16 broadband wireless Internet

- **Status**: ✅
- **Reason**: 구조적 패리티검사 갖는 신규 tree-LDPC 부호 설계, 낮은 인코딩 복잡도 — 코드설계(E) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1429863
- **Type**: conference
- **Published**: 8-12 Jan. 
- **Authors**: Jun Heo, Kyuhyuk Chung
- **PDF**: https://ieeexplore.ieee.org/document/1429863
- **Abstract**: This work presents a new tree-LDPC code, which has a structured parity check matrix, in the application of IEEE 802.16 broadband wireless Internet. The proposed tree-LDPC code shows better performance with low encoding complexity compared to the regular LDPC codes and RA codes.

## Research on decoding of LDPC coded modulation in OFDM wireless communication system

- **Status**: ✅
- **Reason**: 채널노이즈전력 추정 없이 동작하는 LDPC 디코딩 초기화 알고리즘 제안(C), 디코더 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1405205
- **Type**: conference
- **Published**: 6-6 Jan. 2
- **Authors**: Piming Ma, Dongfeng Yuan
- **PDF**: https://ieeexplore.ieee.org/document/1405205
- **Abstract**: This paper investigates a low-density parity-check (LDPC) coded orthogonal frequency-division multiplexing (OFDM) wireless communication system based on IEEE 802.11a standard. And an initialization algorithm is proposed for the decoding of LDPC coded modulation in OFDM system. The LDPC decoding procedure is simplified without the estimation of channel noise power. Simulation results show that this algorithm is effective and the decoding performance is satisfied when maximum iteration number is 10.

## Implementing LDPC decoding on network-on-chip

- **Status**: ✅
- **Reason**: NoC 기반 LDPC 디코더 아키텍처, 재구성 가능·power-aware 최적화 — 이식 가능 HW(D), 디스크 드라이브도 언급
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:1383266
- **Type**: conference
- **Published**: 3-7 Jan. 2
- **Authors**: T. Theocharides, G. Link, N. Vijaykrishnan +1
- **PDF**: https://ieeexplore.ieee.org/document/1383266
- **Abstract**: Low-density parity check codes are a form of error correcting codes used in various wireless communication applications and in disk drives. While LDPC codes are desirable due to their ability to achieve near Shannon-limit communication channel capacity, the computational complexity of the decoder is a major concern. LDPC decoding consists of a series of iterative computations derived from a message-passing bipartite graph. In order to efficiently support the communication intensive nature of this application, we present a LDPC decoder architecture based on a network-on-chip communication fabric that provides a 1.2 Gbps decoded throughput rate for a 3/4 code rate, 1024-bit block LDPC code. The proposed architecture can be reconfigured to support other LDPC codes of different block sizes and code rates. We also propose two novel power-aware optimizations that reduce the power consumption by up to 30%.

## An FPGA implementation of low-density parity-check code decoder with multi-rate capability

- **Status**: ✅
- **Reason**: 멀티레이트 LDPC 디코더 FPGA 구현; 이식 가능 HW 아키텍처(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:1466451
- **Type**: conference
- **Published**: 21-21 Jan.
- **Authors**: Lei Yang, Manyuan Shen, Hui Liu +1
- **PDF**: https://ieeexplore.ieee.org/document/1466451
- **Abstract**: With superior error correction capability, low-density parity-check (LDPC) has initiated wide scale interests in wireless telecommunication fields. In the past, various structures of single code rate LDPC decoders have been implemented for different applications. However, in order to cover a wide range of service requirements and diverse interference conditions in wireless applications, LDPC decoders that can operate in both high and low code rates are desired. In this paper, a new multi-rate LDPC decoder architecture is presented and implemented in a Xilinx FPGA device. Through selection pins, three operating modes with the irregular 1/2 rate, regular 5/8 rate and regular 7/8 rate are supported. The measurement results show LDPC decoder can achieve BER below 10/sup -5/ at SNR of 1.4dB in the most critical case with the irregular 1/2 mode.

## A memory-based architecture for FPGA implementations of low-density parity-check convolutional decoders

- **Status**: ✅
- **Reason**: LDPC convolutional 디코더의 FPGA 메모리기반 아키텍처 - 이식 가능 HW(D), 바이너리 LDPC
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:1464593
- **Type**: conference
- **Published**: 2005
- **Authors**: S. Bates, G. Block
- **PDF**: https://ieeexplore.ieee.org/document/1464593
- **Abstract**: Low-density parity-check convolutional codes complement their popular block-oriented counterparts and may be more suitable in certain communication applications. These include streaming voice and video and packet switching networks. In this paper we introduce these codes and propose a memory-based decoder architecture that is well suited for implementation on field-programmable gate arrays. We present an overview of the architecture and demonstrate its efficiency over register-based architectures. We then discuss a realization of this architecture that can trade performance for throughput and can achieve up to 120 Mb/s of information throughput and a BER as low as 2 /spl times/ 10/sup -6/ at an Eb/Nq of 3 dB on an Altera Stratix FPGA. For a first-generation implementation this compares favorable with current block-oriented decoder implementations.

## Complexity-optimized low-density parity-check codes for gallager decoding algorithm B

- **Status**: ✅
- **Reason**: 바이너리 LDPC, Gallager B 디코딩 복잡도-rate 결합 최적화 코드설계(EXIT 기반 새 설계법) → 카테고리 C/E
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1523591
- **Type**: conference
- **Published**: 2005
- **Authors**: Wei Yu, M. Ardakani, B. Smith +1
- **PDF**: https://ieeexplore.ieee.org/document/1523591
- **Abstract**: The complexity-rate tradeoff for error-correcting codes below the Shannon limit is a central question in coding theory. This paper makes progress in this area by presenting a joint numerical optimization of rate and decoding complexity for low-density parity-check codes. The focus of this paper is on the binary symmetric channel and on a class of decoding algorithms for which an exact extrinsic information transfer (EXIT) chart analysis is possible. This class of decoding algorithms includes the Gallager decoding algorithm B. The main feature of the optimization method is a complexity measure based on the EXIT chart that accurately estimates the number of iterations required for the decoding algorithm to reach a target error rate. Under a fixed check-degree distribution, it is shown that the proposed complexity measure is a convex function of the variable-degree distribution in a region of interest. This allows us to numerically characterize the complexity-rate tradeoff. We show that for the Gallager B decoding algorithm on binary symmetric channels, the optimization procedure can produce complexity savings of 30-40% as compared to the conventional code design method

## Low-density parity-check convolutional codes for Ethernet networks

- **Status**: ✅
- **Reason**: LDPC convolutional codes(SC-LDPC 계열) 구성/종단·인코딩 복잡도 - E 이식 가능 코드설계
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1517231
- **Type**: conference
- **Published**: 2005
- **Authors**: S. Bates, Zhengang Chen, Xiaodai Dong
- **PDF**: https://ieeexplore.ieee.org/document/1517231
- **Abstract**: In this paper we discuss the application of low-density parity-check convolutional codes to several communication protocols which employ the Ethernet frame format. We argue that these codes are more suited to such systems than their block counterparts. This is due, in part, to a reduced encoder complexity and the ability to operate on random lengths of data. We also discuss how we can use existing frame delimiters and interframe gaps to perform presetting and termination of the code. We present simulation results which suggest this may be used to improve error performance over the first and last bytes of the frame.

## Integrated interleaving ECC and high dimensional parity codes

- **Status**: ✅
- **Reason**: 고차원 패리티 product code를 LDPC로 보고 sum-product 디코딩 적용 - 코드설계+디코더 이식 가능(E/C), 바이너리
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1463925
- **Type**: conference
- **Published**: 2005
- **Authors**: H. Kamabe, H. Katou
- **PDF**: https://ieeexplore.ieee.org/document/1463925
- **Abstract**: The integrated interleaving error correcting scheme allows the use of redundancies of different levels through all data blocks. That is, a redundancy of the error correcting capability of a (strong) code can be distributed over data blocks which are encoded with different redundancies. The high dimensional parity code is defined as a product code of simple parity check codes. Since the structure of the code is very simple, expect that the encoding procedure is also simple. Another advantage of the code is that the code can be viewed as a low density parity check code. Therefore the powerful decoding method, the sum-product algorithm can be applied in decoding. In this paper, the codes are used as constituent codes for the integrated interleaving error correcting scheme.

## Design of low density generator matrix codes for continuous phase modulation

- **Status**: ✅
- **Reason**: CPM용 LDGM(저밀도 생성행렬, LDPC 친화) 부호설계+EXIT 최적화+error floor 분석, 코드설계 기법 이식 가능(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1577851
- **Type**: conference
- **Published**: 2005
- **Authors**: Ming Xiao, T. M. Aulin
- **PDF**: https://ieeexplore.ieee.org/document/1577851
- **Abstract**: We investigate the low density generator matrix (LDGM) codes for continuous phase modulation (CPM). The nonsystematic version of LDGM codes is used in the scheme. The overall system has linear encoding complexity due to the low complexity of the LDGM codes. A property of the check node degree of the LDGM code is shown. We use the EXIT chart/function to optimize the LDGM codes. The EXIT function of CPM with a fixed SNR (signal-to-noise-ratio) is shown. We derive the union bound to analyze the error floor performance. Design approaches for lowering error floors are suggested from the analysis process. Numerical results show that this scheme converges earlier (lower SNR) than best found serially concatenated CPM (SCCPM) for iterative decoding while maintaining comparable error floors.

## A comparison of adaptive belief propagation and the best graph algorithm for the decoding of linear block codes

- **Status**: ✅
- **Reason**: 바이너리 선형부호 적응적 BP 디코딩(그래프 구조 적응 수정) - C 이식 가능 BP 개선 디코더
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1523431
- **Type**: conference
- **Published**: 2005
- **Authors**: A. Kothiyal, O. Y. Takeshita
- **PDF**: https://ieeexplore.ieee.org/document/1523431
- **Abstract**: In this paper, two iterative message passing algorithms based on belief propagation proposed for the decoding of any binary linear block code are compared. The innovation of these algorithms lies in the fact that the structure of the graph of the parity check matrix is adaptively modified to render it suitable to belief propagation decoding. The modification is done such that the least reliable bits received from the channel are leaves of the graph. These algorithms perform favorably when compared with existing hard and iterative soft decision decoding algorithms in terms of error rate while maintaining a complexity polynomial in block length. It was found that while these two algorithms are conceptually similar, their performance in terms of word error rate (as a function of signal-to-noise ratio), decoding time (average number of iterations) and the updated bit reliabilities are very different

## On achievable rates of multistage decoding on two-dimensional ISi channels

- **Status**: ✅
- **Reason**: 2D ISI 채널 다단디코딩에서 LDPC 부호 최적화로 정보율 접근 - 떼어낼 LDPC 구성/최적화 가능성, 애매하여 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1523562
- **Type**: conference
- **Published**: 2005
- **Authors**: J. B. Soriaga, P. H. Siegel, J. K. Wolf +1
- **PDF**: https://ieeexplore.ieee.org/document/1523562
- **Abstract**: The achievable information rates for multilevel coding (MLC) systems with multistage decoding (MSD) are examined on two-dimensional binary-input intersymbol interference (ISI) channels. One MSD scheme employs trellis-based detection, while another involves zero-forcing equalization and linear noise prediction. Information rates are determined by examining the output statistics at each stage of MSD. The first scheme is shown to achieve rates very close to known information-theoretic limits. Systems with low-density parity-check codes are then optimized to approach these rates

## Noise predictive belief propagation

- **Status**: ✅
- **Reason**: BP에 잡음 화이트닝을 결합한 noise predictive BP - 부호 비의존 BP 메시지패싱 개선(C), NAND 상관잡음에 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1494443
- **Type**: conference
- **Published**: 2005
- **Authors**: M. N. Kaynak, T. M. Duman, E. M. Kurtas
- **PDF**: https://ieeexplore.ieee.org/document/1494443
- **Abstract**: We introduce iterative noise whitening for belief propagation (BP) based channel detectors over intersymbol interference (ISI) channels with correlated noise. Called noise predictive belief propagation (NPBP), the new scheme iteratively whitens the noise samples by modifying the edge probability computation of the BP algorithm. NPBP detectors based on finite impulse response (FIR) and infinite impulse response (IIR) prediction filters are introduced. In addition, we propose a novel prediction filter optimization method leading to a better noise whitening performance. Simulation results for both coded and uncoded systems and comparisons with maximum a posteriori (MAP) and BP detectors show that, significant improvements can be obtained.

## Belief propagation decoding of Reed-Solomon codes; a bit-level soft decision decoding algorithm

- **Status**: ✅
- **Reason**: RS부호의 바이너리 image에 sparse 패리티검사 만들어 BP 디코딩, 부호 비의존적 BP 기법(C)으로 바이너리 LDPC에 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1406158
- **Type**: journal
- **Published**: 2005
- **Authors**: B. Kamali, A. H. Aghvami
- **PDF**: https://ieeexplore.ieee.org/document/1406158
- **Abstract**: In this article we propose the application of Belief Propagation (BP) algorithm as a novel bit-level soft decision decoding (SDD) technique for Reed-Solomon (RS) codes. A brief tutorial on Belief Propagation algorithm is presented. A central issue in the application of BP algorithm to decoding RS codes is the construction of a sparse parity check matrix for the binary image of the code. It is demonstrated that Vardy's technique may be applied to find a sparse parity check matrix for RS codes. However, this technique is not applicable to all cases. The BP algorithm is applied to two test codes. In one case, simulation models show that the BP algorithm outperforms the hard decision Euclidean decoding by more than 2 dB of additional coding gain. The results with the second test code are not as promising.

## Estimation and Marginalization Using the Kikuchi Approximation Methods

- **Status**: ✅
- **Reason**: Kikuchi 근사 기반 message-passing 알고리즘 일반화로 BP/디코더 메시지패싱 기법 이식 여지(C), 애매하나 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6788339
- **Type**: journal
- **Published**: 2005
- **Authors**: P. Pakzad, V. Anantharam
- **PDF**: https://ieeexplore.ieee.org/document/6788339
- **Abstract**: In this letter, we examine a general method of approximation, known as the Kikuchi approximation method, for finding the marginals of a product distribution, as well as the corresponding partition function. The Kikuchi approximation method defines a certain constrained optimization problem, called the Kikuchi problem, and treats its stationary points as approximations to the desired marginals. We show how to associate a graph to any Kikuchi problem and describe a class of local message-passing algorithms along the edges of any such graph, which attempt to find the solutions to the problem. Implementation of these algorithms on graphs with fewer edges requires fewer operations in each iteration. We therefore characterize minimal graphs for a Kikuchi problem, which are those with the minimum number of edges. We show with empirical results that these simpler algorithms often offer significant savings in computational complexity, without suffering a loss in the convergence rate. We give conditions for the convexity of a given Kikuchi problem and the exactness of the approximations in terms of the loops of the minimal graph. More precisely, we show that if the minimal graph is cycle free, then the Kikuchi approximation method is exact, and the converse is also true generically. Together with the fact that in the cycle-free case, the iterative algorithms are equivalent to the well-known belief propagation algorithm, our results imply that, generically, the Kikuchi approximation method can be exact if and only if traditional junction tree methods could also solve the problem exactly.
