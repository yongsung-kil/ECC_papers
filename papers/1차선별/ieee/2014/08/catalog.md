# IEEE Xplore — 2014-08 (1차선별 통과)


## Fast and Accurate Error Floor Estimation of Quantized Iterative Decoders for Variable-Regular LDPC Codes

- **Status**: ✅
- **Reason**: 양자화 반복 디코더의 error floor 추정 + dominant trapping set 열거 — 바이너리 LDPC 디코더/error floor 기법(C/E), NAND 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6835193
- **Type**: journal
- **Published**: Aug. 2014
- **Authors**: Sina Tolouei, Amir H. Banihashemi
- **PDF**: https://ieeexplore.ieee.org/document/6835193
- **Abstract**: In this letter, we propose a fast and accurate technique to estimate the error floor of variable-regular low-density parity-check (LDPC) codes under quantized iterative decoding algorithms. The technique, which is based on enumerating the dominant elementary trapping sets of the code, provides significant improvement over existing methods in terms of speed and accuracy.

## Linear Programming Decoding of Spatially Coupled Codes

- **Status**: ✅
- **Reason**: 바이너리 SC-LDPC/정규 LDPC의 LP 디코딩 임계값·dual witness 분석, 이식 가능 디코더(C)·SC-LDPC 코드설계(E) 관련 — 애매하므로 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6824252
- **Type**: journal
- **Published**: Aug. 2014
- **Authors**: Louay Bazzi, Badih Ghazi, Rüdiger L. Urbanke
- **PDF**: https://ieeexplore.ieee.org/document/6824252
- **Abstract**: For a given family of spatially coupled codes, we prove that the linear programming (LP) threshold on the binary-symmetric channel (BSC) of the tail-biting graph cover ensemble is the same as the LP threshold on the BSC of the derived spatially coupled ensemble. This result is in contrast with the fact that spatial coupling significantly increases the belief propagation threshold. To prove this, we establish some properties related to the dual witness for LP decoding. More precisely, we prove that the existence of a dual witness, which was previously known to be sufficient for LP decoding success, is also necessary and is equivalent to the existence of certain acyclic hyperflows. We also derive a sublinear (in the block length) upper bound on the weight of any edge in such hyperflows, both for regular low-density parity-check (LPDC) codes and spatially coupled codes and we prove that the bound is asymptotically tight for regular LDPC codes. Moreover, we show how to trade crossover probability for LP excess on all the variable nodes, for any binary linear code.

## Algebraic Quasi-Cyclic LDPC Codes: Construction, Low Error-Floor, Large Girth and a Reduced-Complexity Decoding Scheme

- **Status**: ✅
- **Reason**: 유한체 기반 QC-LDPC 신규 구성 + masking으로 girth>=8 + reduced-complexity 반복 디코딩 — 코드설계(E)+디코더(C) 신규 기여
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6856152
- **Type**: journal
- **Published**: Aug. 2014
- **Authors**: Juane Li, Keke Liu, Shu Lin +1
- **PDF**: https://ieeexplore.ieee.org/document/6856152
- **Abstract**: This paper presents a simple and very flexible method for constructing quasi-cyclic (QC) low density parity-check (LDPC) codes based on finite fields. The code construction is based on two arbitrary subsets of elements from a given field. Some well known constructions of QC-LDPC codes based on finite fields and combinatorial designs are special cases of the proposed construction. The proposed construction in conjunction with a technique, known as masking, results in codes whose Tanner graphs have girth 8 or larger. Experimental results show that codes constructed using the proposed construction perform well and have low error-floors. Also presented in the paper is a reduced-complexity iterative decoding scheme for QC-LDPC codes based on the section-wise cyclic structure of their parity-check matrices. The proposed decoding scheme is an improvement of an earlier proposed reduced-complexity iterative decoding scheme.

## The improved Turbo-decoding Message-passing algorithm and corresponding decoder for LDPC based on LTE

- **Status**: ✅
- **Reason**: TDMP(layered) BP의 정수 양자화 오버플로 제거 + 디코더 HW 개선(감산기/시프트만 추가) — 바이너리 LDPC 디코더·양자화 기법, NAND 이식 가능(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6986326
- **Type**: conference
- **Published**: 5-8 Aug. 2
- **Authors**: Lingling Lao, Lixin Li, Meng Zhu +1
- **PDF**: https://ieeexplore.ieee.org/document/6986326
- **Abstract**: The Turbo-decoding Message-passing (TDMP) algorithm of Low-Density Parity-Check (LDPC) codes has a faster convergence speed, lower hardware implementation complexity, and less storage units than the Belief-Passing (BP) algorithms. However, because of the integer quantization operations for initial information, restriction of storage units will cause the problem of decoding information overflowing. This paper gives the reason of overflow errors, proposes the improved decoding algorithm which can partially eliminate overflow errors, and designs the corresponding decoder which only requires some extra subtractors and shift operations. We analyze the computation complexity and compute decoder throughput. Finally, we simulate the error performances of the LDPC codes over the LTE channel, and simulation results show that the proposed algorithm effectively suppresses the overflow errors with a low decoder complexity and a high throughput.

## Joint noise distribution parameter estimation and LDPC decoding using variational Bayes

- **Status**: ✅
- **Reason**: 변분베이즈를 BP에 결합한 새 메시지패싱 스킴으로 노이즈 파라미터 동시추정, 부호 비의존 디코더 개선(C) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6908538
- **Type**: conference
- **Published**: 3-6 Aug. 2
- **Authors**: Y. Mohammad Taheri, M. Omair Ahmad, M. N. S. Swamy
- **PDF**: https://ieeexplore.ieee.org/document/6908538
- **Abstract**: In this work, we investigate the problem of estimating time-varying noise distribution parameter on a factor graph. A new message passing scheme is proposed by incorporating the variational Bayes (VB) into the belief propagation algorithm for estimating of time-varying noise distribution parameter in a low-density parity-check decoder. The scheme can also be used for the estimation of the correlation noise model parameter in distributed video coding. A Bayesian estimator is used to estimate this parameter by obtaining its posterior distribution given the channel output. The VB algorithm is employed to approximate the complex form of the posterior distribution with a simple distribution. Finally, this distribution is used to derive a closed-form expression for the messages on the augmented factor graph for online parameter estimation and decoding process at the same time.

## Spatially coupled turbo codes: Principles and finite length performance

- **Status**: ✅
- **Reason**: spatially coupled 부호(turbo지만), 공간결합 코드설계·threshold saturation이 SC-LDPC 설계와 직결—애매, Phase3 재검토
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6933478
- **Type**: conference
- **Published**: 26-29 Aug.
- **Authors**: Alexandre Graell i Amat, Saeedeh Moloudi, Michael Lentmaier
- **PDF**: https://ieeexplore.ieee.org/document/6933478
- **Abstract**: In this paper, we give an overview of spatially coupled turbo codes (SC-TCs), the spatial coupling of parallel and serially concatenated convolutional codes, recently introduced by the authors. For presentation purposes, we focus on spatially coupled serially concatenated codes (SC-SCCs). We review the main principles of SC-TCs and discuss their exact density evolution (DE) analysis on the binary erasure channel. We also consider the construction of a family of rate-compatible SC-SCCs with simple 4-state component encoders. For all considered code rates, threshold saturation of the belief propagation (BP) to the maximum a posteriori threshold of the uncoupled ensemble is demonstrated, and it is shown that the BP threshold approaches the Shannon limit as the coupling memory increases. Finally we give some simulation results for finite lengths.

## Hardware-friendly Probabilistic Min-Sum algorithm for fully-parallel LDPC decoders

- **Status**: ✅
- **Reason**: 신규 디코더(Normalized Probabilistic Min-Sum)로 비교 횟수 절반 감소+고처리율 HW 구현 — 부호 비의존 min-sum 변형, NAND 이식 가능(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6955094
- **Type**: conference
- **Published**: 18-22 Aug.
- **Authors**: Huang-Chang Lee, Chung-Chao Cheng, Yeong-Luh Ueng
- **PDF**: https://ieeexplore.ieee.org/document/6955094
- **Abstract**: In order to simplify the check node operation of the low-density parity-check (LDPC) decoders, this paper presents a Normalized Probabilistic Min-Sum Algorithm (NPMSA), where the second minimum value is replaced by a probabilistic second minimum value. For NPMSA, the number of required comparisons can be reduced to about half compared to that of the conventional Normalized Min-Sum Algorithm (NMSA). It is shown that the simplification only introduces negligible impact on the bit-error rate performance, especially for codes with a high check node degree. When the proposed NPMSA is applied to the (2048, 1723) RS-LDPC code, the degradation in the error-rate performance is only about 0.05 dB. The hardware implementation shows that a throughput of 45.42 Gbps can be achieved using the proposed NPMSA.

## Highly flexible design of multi-rate multi-length quasi-cyclic LDPC codes

- **Status**: ✅
- **Reason**: 다중율·다중길이 유연 QC-LDPC 구성(PEG 기반) — 바이너리 코드 설계(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6955081
- **Type**: conference
- **Published**: 18-22 Aug.
- **Authors**: Moritz Beermann, Florian Wickert, Peter Vary
- **PDF**: https://ieeexplore.ieee.org/document/6955081
- **Abstract**: The design of Low-Density Parity-Check (LDPC) codes with fixed code rate and block length for a fixed channel condition has been well investigated and very close-to-capacity performance can be achieved by careful optimization of a code's degree distributions. The growing variety of services supported by mobile communication systems, however, constitutes the need for highly flexible Forward Error Correction (FEC) schemes. Pursuing this need, we present a design method for the construction of quasi-cyclic (QC) LDPC codes supporting arbitrarily many block lengths and code rates using only a single common mother code. Different block lengths are achieved by an optimized expansion of the mother code's lifting matrix. For the support of multiple code rates, a joint optimization of shortening and puncturing distributions as well as an optimized check matrix construction based on the progressive edge-growth algorithm is employed.

## On the equivalence of the ACE and the EMD of a cycle for the ACE spectrum constrained LDPC codes

- **Status**: ✅
- **Reason**: ACE/EMD 등가 조건 — LDPC 사이클 연결성 기반 코드 설계 기법(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6955087
- **Type**: conference
- **Published**: 18-22 Aug.
- **Authors**: Kuntal Deka, A. Rajesh, P. K. Bora
- **PDF**: https://ieeexplore.ieee.org/document/6955087
- **Abstract**: The Extrinsic Message Degree (EMD) of a cycle in the Tanner graph of a low density parity check (LDPC) code measures the connectivity of the cycle. As it is difficult to calculate the EMD, the Approximate EMD (ACE) is generally used. However, the ACE of a cycle is not always equal to its EMD. This paper presents some sufficient conditions for the equivalence of the ACE and the EMD of a cycle for the ACE spectrum constrained LDPC codes.

## Rate-compatible spatially coupled LDPC codes via repeat-accumulation extension

- **Status**: ✅
- **Reason**: rate-compatible SC-LDPC 구성(RA-extension) — 바이너리 LDPC 코드 설계(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6955091
- **Type**: conference
- **Published**: 18-22 Aug.
- **Authors**: Wei Hou, Shan Lu, Jun Cheng
- **PDF**: https://ieeexplore.ieee.org/document/6955091
- **Abstract**: We propose the construction of rate-compatible spatially coupled low-density parity-check (SC-LDPC) codes. For a given high-rate SC-LDPC mother code, a family of low-rate member codes can be obtained by extending the protogragh of the mother code with repeat-accumulation (RA). Rate compatibility is obtained by adjusting the RA-extension parameters. Continuous code rate is achieved without extra cost. Density evolution analysis shows that the iterative decoding thresholds of all the member codes of the rate-compatible family are very close to the Shannon limits over the binary erasure channels.

## A unified approach to optimization of LDPC codes for various communication scenarios

- **Status**: ✅
- **Reason**: QC-LDPC base matrix 순환행렬 구성+greedy 최적화 통합 기법(E); 다만 비이진/컨볼루셔널 포함 — 바이너리 QC-LDPC 구성 부분 이식 가능, 애매하여 in
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6955122
- **Type**: conference
- **Published**: 18-22 Aug.
- **Authors**: Irina E. Bocharova, Rolf Johannesson, Boris D. Kudryashov
- **PDF**: https://ieeexplore.ieee.org/document/6955122
- **Abstract**: A unified approach to construct and optimize codes determined by their sparse parity-check matrices is presented. Parity-check matrices of quasi-cyclic (QC) LDPC block codes are obtained by replacing the nonzero elements of a base (seed) matrix by circulants. Replacing the nonzero elements either by companion matrices of elements from a finite field GF(2m) or by a formal variable D gives parity-check matrices of binary images of nonbinary LDPC block codes and LDPC convolutional codes, respectively. A set of performance measures applicable to different classes of LDPC codes are considered and a greedy algorithm for code performance optimization is presented. For a few classes of LDPC codes examples of codes combining good error-correcting performance with compact representation are obtained. Moreover, a specific channel model can easily be embedded into the optimization loop. Thereby, the code can be optimized for a specific channel. The efficiency of such an optimization is demonstrated via an example of Faster Than Nyquist (FTN) signaling using LDPC codes.

## Randomly punctured spatially coupled LDPC codes

- **Status**: ✅
- **Reason**: 랜덤 펑처링 SC-LDPC 앙상블 설계/임계값 분석 — 바이너리 코드 설계(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6955074
- **Type**: conference
- **Published**: 18-22 Aug.
- **Authors**: David G. M. Mitchell, Michael Lentmaier, Ali E. Pusane +1
- **PDF**: https://ieeexplore.ieee.org/document/6955074
- **Abstract**: In this paper, we study random puncturing of protograph-based spatially coupled low-density parity-check (SC-LDPC) code ensembles. We show that, with respect to iterative decoding threshold, the strength and suitability of an LDPC code ensemble for random puncturing over the binary erasure channel (BEC) is completely determined by a single constant θ ≥ 1 that depends only on the rate and iterative decoding threshold of the mother code ensemble. We then use this analysis to show that randomly punctured SC-LDPC code ensembles display near capacity thresholds for a wide range of rates. We also perform an asymptotic minimum distance analysis and show that, like the SC-LDPC mother code ensemble, the punctured SC-LDPC code ensembles are also asymptotically good. Finally, we present some simulation results that confirm the excellent decoding performance promised by the asymptotic results.

## On characterization of elementary trapping sets of variable-regular LDPC codes

- **Status**: ✅
- **Reason**: variable-regular 바이너리 LDPC ETS 구조 특성화, error floor 분석 및 저-error-floor 코드 설계(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6955086
- **Type**: conference
- **Published**: 18-22 Aug.
- **Authors**: Mehdi Karimi, Amir H. Banihashemi
- **PDF**: https://ieeexplore.ieee.org/document/6955086
- **Abstract**: In this paper, we study the graphical structure of elementary trapping sets (ETS) of variable-regular low-density parity-check (LDPC) codes. ETSs are known to be the main cause of error floor in LDPC coding schemes. For the set of LDPC codes with a given variable node degree dl and girth g, we identify all the non-isomorphic structures of an arbitrary class of (a, b) ETSs, where a is the number of variable nodes and b is the number of odd-degree check nodes in the induced subgraph of the ETS. Our study leads to a simple characterization of dominant classes of ETSs (those with relatively small values of a and b) based on short cycles in the Tanner graph of the code. For such classes of ETSs, we prove that any set S in the class is a layered superset (LSS) of a short cycle, where the term “layered” is used to indicate that there is a nested sequence of ETSs that starts from the cycle and grows, one variable node at a time, to generate S. This characterization corresponds to a simple search algorithm that starts from the short cycles of the graph and finds all the ETSs with LSS property in a guaranteed fashion. Specific results on the structure of ETSs are presented for dl = 3, 4, 5, 6, g = 6, 8 and a, b ≤ 10. The results of this work can be used for the error floor analysis and for the design of LDPC codes with low error floors.

## An efficient complexity-optimizing LDPC code design for the binary erasure channel

- **Status**: ✅
- **Reason**: BEC용 LDPC 복잡도-성능 최적화 차수분포 설계(SDP), 바이너리 LDPC 코드 설계(E) 기법 이식 가능성
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6955121
- **Type**: conference
- **Published**: 18-22 Aug.
- **Authors**: Vahid Jamali, Yasser Karimian, Johannes Huber +1
- **PDF**: https://ieeexplore.ieee.org/document/6955121
- **Abstract**: The complexity-performance trade-off is a fundamental aspect of the design of low-density parity-check (LDPC) codes. In this paper, we consider LDPC codes for the binary erasure channel (BEC), use code rate for performance metric, and number of decoding iterations to achieve a certain residual erasure probability for complexity metric. The available complexity-optimizing problems in the literature for the BEC are either non-convex or belong to the class of semi-infinite problems which are computationally challenging to be solved. Hence, in this paper, we first propose a lower bound on the number of iterations for the BEC. Moreover, a simple but efficient utility function corresponding to the number of iterations is developed. Using this utility function, an optimization problem w.r.t. complexity is formulated to find complexity-optimized code degree distributions. We prove that the considered problem with the proposed utility function falls into the class of semi-definite programming (SDP) and thus, the global solution can be found efficiently using available SDP solvers. Numerical results reveal the superiority of the proposed code design compared to existing code designs from literature.

## On the guaranteed error-correction of decimation-enhanced iterative decoders

- **Status**: ✅
- **Reason**: BSC용 FAID 변형 decimation-enhanced FAID 보장 오정정 분석 — error floor 디코더/코드설계 기법(C/E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6955085
- **Type**: conference
- **Published**: 18-22 Aug.
- **Authors**: Shiva Kumar Planjery, David Declercq, Madiagne Diouf +1
- **PDF**: https://ieeexplore.ieee.org/document/6955085
- **Abstract**: Finite alphabet iterative decoders (FAIDs) proposed for LDPC codes on the binary symmetric channel are capable of surpassing the belief propagation (BP) decoder in the error floor region with lower complexity and precision, but these decoders are difficult to analyze for finite-length codes. Recently, decimation-enhanced FAIDs (DFAIDs) were proposed for column-weight-three codes. Decimation involves fixing the bit values of certain variable nodes during message-passing based on the messages they receive after some number of iterations. In this paper, we address the problem of proving the guaranteed error-correction capability of DFAIDs for column-weight-three LDPC codes. We present the methodology of the proof to derive sufficient conditions on the Tanner graph that guarantee the correction of a given error pattern in a finite number of iterations. These sufficient conditions are described as a list of forbidden graphs that must not be contained in the Tanner graph of the code. As a test case, we consider the problem of guaranteeing the correction of four errors. We illustrate the analysis for a specific 4-error pattern and provide the sufficient conditions for its correction. We also present results on the design of codes satisfying those sufficient conditions and their impact on the achievable code rate.

## Variational message passing without initialization using a free energy constraint

- **Status**: ✅
- **Reason**: 바이너리 LDPC 디코더용 sum-product 변형(free energy 제약, 초기화 제거) 제시 — 이식 가능 디코더 알고리즘(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6955083
- **Type**: conference
- **Published**: 18-22 Aug.
- **Authors**: Murthy V. R. S. Devarakonda
- **PDF**: https://ieeexplore.ieee.org/document/6955083
- **Abstract**: In iterative algorithms with graphical models, it is common to initialize messages. But this approach is not suitable in certain applications. In this paper, it is conjectured that if some messages are confined to a ball around their initialized values, then initialization can be avoided. Towards this goal, for networks specified with a bipartite graph, a variant of the sum-product algorithm is derived by adding an inequality constraint on the variable free energy in the underlying Bethe optimization problem. In the binary case, this leads to an upper bound that restricts the ℓ1 norm of the extrinsic message (vector) to a ball around its (otherwise) initial value. Results are reported for binary LDPC decoders through simulations which confirm that initialization between decoding attempts can be eliminated and show that the algorithm tends to outperform the standard sum-product. A few more observations and comments on this approach, relation with other variational methods, and applications to analog processing and inference over distributed networks are outlined in the end.

## Error floors and finite geometries

- **Status**: ✅
- **Reason**: 트래핑셋·error floor·유한기하 구조 — 바이너리 LDPC 코드 설계/error floor(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6955082
- **Type**: conference
- **Published**: 18-22 Aug.
- **Authors**: Shu Lin, Qiuju Diao, Ian Blake
- **PDF**: https://ieeexplore.ieee.org/document/6955082
- **Abstract**: The structure of certain subgraphs of the Tanner graph of an LDPC code, the trapping sets, has been identified as important for the error floor performance of iterative decoding algorithms. To investigate such sets requires the parity check matrix of the code to be generated with sufficient structure that allows useful information to be obtained while giving good codes. Structures that have been considered include combinatorial designs and classical finite geometries. More recently other finite geometric notions such as partial geometries and generalized d-gons have been considered with some success. This work considers aspects of this approach.

## Improving the finite-length performance of long SC-LDPC code chains by connecting consecutive chains

- **Status**: ✅
- **Reason**: SC-LDPC 유한길이 성능 개선 인코딩/전송 기법 — 바이너리 LDPC 코드 설계(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6955088
- **Type**: conference
- **Published**: 18-22 Aug.
- **Authors**: Pablo M. Olmos, David G. M. Mitchell, Dmitry Truhachev +1
- **PDF**: https://ieeexplore.ieee.org/document/6955088
- **Abstract**: We propose a novel encoding/transmission scheme called continuous chain (CC) transmission that is able to improve the finite-length performance of a system using long spatially coupled low-density parity-check (SC-LDPC) code chains. First, we show that the decoding of SC-LDPC code chains is more reliable for shorter chain lengths, i.e., the scaling between block error rate and gap to threshold is more favorable for shorter chains. This motivates the use of CC transmission in which, instead of transmitting a sequence of independent codewords from a long SC-LDPC chain, we connect multiple chains in a layered format, where encoding, transmission, and decoding are now performed in a continuous fashion. Finally, we show that CC transmission can be implemented with only a small increase in decoding complexity or delay with respect to a system employing a single SC-LDPC code chain for transmission.

## New and efficient decoding architecture for Quasi-Cyclic LDPC codes

- **Status**: ✅
- **Reason**: offset min-sum 단순화한 Single-Scan Layer Decoding(SLD) QC-LDPC FPGA 디코더 — 이식 가능 디코더/HW(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7054294
- **Type**: conference
- **Published**: 14-16 Aug.
- **Authors**: Zhiming Fan, Zhanji Wu, Hui Che +1
- **PDF**: https://ieeexplore.ieee.org/document/7054294
- **Abstract**: In this paper, a new and efficient decoding architecture, Single-Scan Layer Decoding (SLD), is realized in FPGA for multi-rate Quasi-Cyclic LDPC (QC-LDPC) codes. The SLD algorithm simplifies the nodes updating process and messages storing process of the offset min-sum algorithm, speeding up the decoding process and reducing nearly a half of resources consumption. Besides, the SLD algorithm, introducing the semi-parallel architecture into decoding architecture, can increase the convergence rate by 2X and decrease the interconnect complexity of hardware implementation. For multi-rate QC-LDPC Codes in 802.11.n, comparing with float-point software implementation, the degradations of the fixed-point SLD algorithm with 10 iterations in FPGA are all less than 0.ldB and the throughput of different code rates are all above 100Mbps.

## Poster: FPGA based implementation of overlapped QC-LDPC decoder with limited resources

- **Status**: ✅
- **Reason**: NMS 기반 overlapped message passing QC-LDPC 디코더 FPGA 구현으로 지연 단축 — 이식 가능 HW 아키텍처(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:7054382
- **Type**: conference
- **Published**: 14-16 Aug.
- **Authors**: Xu Dijia, Bie Hongxia, Zheng Jian +1
- **PDF**: https://ieeexplore.ieee.org/document/7054382
- **Abstract**: In this paper, we propose a simplified architecture based on overlapped message passing (OMP) for QC-LDPC decoders with Normalized Minimum Sum (NMS) algorithm, aiming to reduce decoding latency with as less additional resources as possible. According to the OMP architecture, the two stages of NMS, namely check node process and variable node process, could be overlapped. Hence, overall decoding latency is reduced and hardware utilization efficiency (HUE) is improved. Based on the proposed OMP architecture, two irregular QC-LDPC decoders are implemented in serial and partly-parallel styles in FPGA respectively. Experimental results show that, achieving the same decoding performance, the serial QC-LDPC decoder with proposed OMP architecture can reduce latency by 39.1% compared with that of the decoder with TPMP(Two Stages Message Passing) architecture, and the latency reduction of partly-parallel decoder varies with degrees of parallelism.

## Work in progress: A new algorithm to improve the decoding success probability of Raptor code

- **Status**: ✅
- **Reason**: Raptor용이나 girth-4 회피 LDPC 검사행렬 구성 + stopping set 기반 cascaded BP 개선 — 이식 가능 코드설계/디코더(E/C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7054299
- **Type**: conference
- **Published**: 14-16 Aug.
- **Authors**: Huihui Li, Xiangying Li, Pei He +3
- **PDF**: https://ieeexplore.ieee.org/document/7054299
- **Abstract**: Raptor code is a kind of new fountain code which usually adopts belief propagation(BP) decoding algorithm. In order to improve the decoding success probability of Raptor code, this paper proposes two methods. On the one hand, we adopt a new construction method of check matrix for LDPC code, which can effectively avoid the girth of 4. On the other hand, we analyze and simulate the number of stopping set after BP decoding and propose a new decoding algorithm-the cascaded iterative algorithm based on the Ripple detection. Comparing our algorithm with BP, simulation results show that the proportion of encoded packages with degree 2, 3 in stopping set has decreased apparently and the success probability of Raptor decoding has improved.

## Timing errors in LDPC decoding computations with overscaled supply voltage

- **Status**: ✅
- **Reason**: min-sum LDPC 디코더 아키텍처의 VOS 타이밍 오류 분석 및 VNU/CNU 회로 설계 통찰 — 이식 가능 HW 기법(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:7298249
- **Type**: conference
- **Published**: 11-13 Aug.
- **Authors**: Behnam Sedighi, N. Prasanth Anthapadmanabhan, Dusan Suvakovic
- **PDF**: https://ieeexplore.ieee.org/document/7298249
- **Abstract**: Decoders for Low Density Parity Check (LDPC) codes, used commonly in communication networks, possess inherent tolerance to random internal computation errors. Consequently, it is possible to apply voltage over-scaling (VOS) in their implementation to save energy. In this paper, the impact of VOS on timing errors is characterized for a typical min-sum LDPC decoder architecture using circuit simulations. Failure modes are analyzed for arithmetic circuits performing variable and check node computations. It is shown that a rather unconventional register placement in the variable node unit is beneficial for voltage scaling, and that the check node unit may be designed such that only the least significant bits are more likely to experience errors. Insights into timing error characteristics obtained through this analysis can be used to estimate the limits of voltage scaling and associated energy saving in practical LDPC decoder designs.
