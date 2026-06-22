# IEEE Xplore — 2007-06 (1차선별 통과)


## Implementation of a Flexible LDPC Decoder

- **Status**: ✅
- **Reason**: 유연한 LDPC 디코더 구현 — 새 디코딩 알고리즘 정식화로 통신요구 단순화, 임의 코드 지원 아키텍처(C/D 이식 가능 HW)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4237370
- **Type**: journal
- **Published**: June 2007
- **Authors**: Guido Masera, Federico Quaglio, Fabrizio Vacca
- **PDF**: https://ieeexplore.ieee.org/document/4237370
- **Abstract**: Low-density parity-check codes (LDPC) are among the most powerful error correcting tools today available. For this reason they became very popular in several applications such as the digital satellite broadcasting system (DVB-S2), wireless local area network (IEEE 802.11n) and metropolitan area network (802.16e). Whereas several code-specific decoders have been proposed in the literature, the implementation of a high performance yet flexible LDPC decoder still is a challenging topic. This work presents a novel formulation of the decoding algorithm that strongly simplifies internal communication requirements and enables the development of decoders supporting generally defined LDPC codes. The resulting architecture is tailored to decode both IEEE 802.11n and IEEE 802.16e LDPC codes, as well as any other code of comparable complexity. The implementation cost deriving from the full flexibility offered by the proposed approach is also evaluated.

## Iterative Decoding Using Attenuated Extrinsic Information from Sum-Product Decoder for PMR Channel With Patterned Medium

- **Status**: ✅
- **Reason**: sum-product extrinsic 감쇠 기법 — BP 메시지 스케일링은 NAND LDPC 디코더에 이식 가능(C), 애매시 in
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4202981
- **Type**: journal
- **Published**: June 2007
- **Authors**: Yasuaki Nakamura, Mitsuhiro Nishimura, Yoshihiro Okamoto +4
- **PDF**: https://ieeexplore.ieee.org/document/4202981
- **Abstract**: An LDPC coding and iterative decoding system is studied in perpendicular magnetic recording (PMR) with a bit-patterned medium. We propose an iterative decoding scheme using attenuated extrinsic information from a sum-product decoder, and the bit error rate (BER) performance of the LDPC coding and iterative decoding system is evaluated by R/W computer simulations. It has been clarified that at an areal density of 1 Tbpsi the proposed system provides a jitter margin of the island edges of approximately 0.6% larger than the conventional system using (3, 18)-regular LDPC code

## Computing the Stopping Distance of a Tanner Graph Is NP-Hard

- **Status**: ✅
- **Reason**: Tanner graph stopping set/stopping distance NP-hardness — 바이너리 LDPC error floor/stopping set 분석 기법(E)에 직결, 코드설계 관련 이론
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4215144
- **Type**: journal
- **Published**: June 2007
- **Authors**: Karunakaran Murali Krishnan, Priti Shankar
- **PDF**: https://ieeexplore.ieee.org/document/4215144
- **Abstract**: Two decision problems related to the computation f stopping sets in Tanner graphs are shown to be NP-complete. It follows as a consequence that there exists no polynomial time algorithm for computing the stopping distance of a Tanner graph unless P = NP.

## Self-Compensation Technique for Simplified Belief-Propagation Algorithm

- **Status**: ✅
- **Reason**: min-sum 자기보정 동적정규화 기법 — 부호 비의존 BP 개선+HW 게이트비용 제시, NAND LDPC 디코더 이식 가능(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4203089
- **Type**: journal
- **Published**: June 2007
- **Authors**: Yen-Chin Liao, Chien-Ching Lin, Hsie-Chia Chang +1
- **PDF**: https://ieeexplore.ieee.org/document/4203089
- **Abstract**: The min-sum algorithm is the most common method to simplify the belief-propagation algorithm for decoding low-density parity-check (LDPC) codes. However, there exists a performance gap between the min-sum and belief-propagation algorithms due to nonlinear approximation. In this paper, a self-compensation technique using dynamic normalization is thus proposed to improve the approximation accuracy. The proposed scheme scales the min-sum algorithm by a dynamic factor that can be derived theoretically from order statistics. Moreover, applying the proposed technique to several LDPC codes for DVB-S2 system, the average signal-to-noise ratio degradation, which results from approximation inaccuracy and quantization error, is reduced to 0.2 dB. Not only does it enhance the error-correcting capability of the min-sum algorithm, but the proposed self-compensation technique also preserves a modest hardware cost. After realized with 0.13-mum standard cell library, the dynamic normalization requires about 100 additional gates for each check node unit in the min-sum algorithm

## Iterative Decoding of Multiple-Step Majority Logic Decodable Codes

- **Status**: ✅
- **Reason**: 다단계 majority-logic 코드용 새 bit-flipping 반복 디코더 — 부호 비의존적 bit-flipping 디코더 기법, 바이너리 LDPC BP에 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4237471
- **Type**: journal
- **Published**: June 2007
- **Authors**: Ravi Palanki, Marc P. C. Fossorier, Jonathan S. Yedidia
- **PDF**: https://ieeexplore.ieee.org/document/4237471
- **Abstract**: We investigate the performance of iterative decoding algorithms for multistep majority logic decodable (MSMLD) codes of intermediate length. We introduce a new bit-flipping algorithm that is able to decode these codes nearly as well as a maximum-likelihood decoder on the binary-symmetric channel. We show that MSMLD codes decoded using bit-flipping algorithms can outperform comparable Bose-Chaudhuri-Hocquenghem (BCH) codes decoded using standard algebraic decoding algorithms, at least for high bit-flip rates (or low and moderate signal-to-noise ratios (SNRs)).

## The Factor Graph Approach to Model-Based Signal Processing

- **Status**: ✅
- **Reason**: Factor graph 메시지패싱 일반론(message computation rules) - 부호 비의존적 BP 프레임워크로 LDPC 디코더에 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4282128
- **Type**: journal
- **Published**: June 2007
- **Authors**: Hans-Andrea Loeliger, Justin Dauwels, Junli Hu +3
- **PDF**: https://ieeexplore.ieee.org/document/4282128
- **Abstract**: The message-passing approach to model-based signal processing is developed with a focus on Gaussian message passing in linear state-space models, which includes recursive least squares, linear minimum-mean-squared-error estimation, and Kalman filtering algorithms. Tabulated message computation rules for the building blocks of linear models allow us to compose a variety of such algorithms without additional derivations or computations. Beyond the Gaussian case, it is emphasized that the message-passing approach encourages us to mix and match different algorithmic techniques, which is exemplified by two different approaches—steepest descent and expectation maximization—to message passing through a multiplier node.

## Belief Propagation over SISO/MIMO Frequency Selective Fading Channels

- **Status**: ✅
- **Reason**: SISO/MIMO 채널용 BP 검출기, 4-cycle 존재 하에서도 동작하는 병렬 BP 구조 — 4-cycle 환경 BP 기법은 바이너리 LDPC BP에 잠재 이식 가능, 애매하여 살림(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4251138
- **Type**: journal
- **Published**: June 2007
- **Authors**: Mustafa N. Kaynak, Tolga M. Duman, Erozan M. Kurtas
- **PDF**: https://ieeexplore.ieee.org/document/4251138
- **Abstract**: In this letter, we propose an iterative belief propagation (BP) channel detector (equalizer) over single-input single- output (SISO) and multiple-input multiple-output (MIMO) frequency selective fading channels as an alternative to the typically used maximum a-posteriori (MAP) or maximum likelihood (ML) detectors. The proposed detector has a parallel structure, resulting in fast hardware implementations. Moreover, BP detector is less complex than the MAP detector and it has a short decoding delay. We analyze the bit error rate and the mutual information and show that, over frequency selective fading channels, the proposed BP detector achieves a near-optimal performance, even in the presence of the length 4 cycles in the corresponding channel factor graph.

## LDPC Codes of Arbitrary Girth

- **Status**: ✅
- **Reason**: 임의 girth LDPC 구성을 위한 SLG 그리디 알고리즘 - 코드설계 기법(E), 바이너리 LDPC, NAND 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4259757
- **Type**: conference
- **Published**: 6-8 June 2
- **Authors**: Tsvetan Asamov, Nuh Aydin
- **PDF**: https://ieeexplore.ieee.org/document/4259757
- **Abstract**: For regular, degree two LDPC (low density parity-check) codes, there is a strong relationship between high girth and performance. This article presents a greedy algorithm, called successive level growth (SLG), for the construction of LDPC codes with arbitrarily specified girth. The simulation results show that our codes exhibit significant coding gains over randomly constructed LDPC codes and in some cases outperform PEG codes in the additive white Gaussian noise channel.

## Estimation of Bit and Frame Error Rates of Low-Density Parity-Check Codes on Binary Symmetric Channels

- **Status**: ✅
- **Reason**: BSC 하드디시전 반복디코딩 LDPC의 BER/FER 추정법 - 디코더 성능평가 기법, 바이너리 LDPC error pattern 분석 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4259758
- **Type**: conference
- **Published**: 6-8 June 2
- **Authors**: Hua Xiao, Amir H. Banihashemi
- **PDF**: https://ieeexplore.ieee.org/document/4259758
- **Abstract**: A method for estimating the performance of low-density parity-check (LDPC) codes decoded by hard-decision iterative decoding algorithms on binary symmetric channels (BSC) is proposed. Based on the enumeration of the smallest weight error patterns that cannot be all corrected by the decoder, this method estimates both the frame error rate (FER) and the bit error rate (BER) of a given LDPC code with very good precision for all crossover probabilities of practical interest. Through a number of examples, we show that the proposed method can be effectively applied to both regular and irregular LDPC codes and to a variety of hard-decision iterative decoding algorithms. Compared with the conventional Monte Carlo simulation, the proposed method has a much smaller computational complexity, particularly for lower error rates.

## Cycle and Distance Properties of Structured LDPC Codes Based on Circulant Permutation Matrices

- **Status**: ✅
- **Reason**: 순환순열행렬 기반 QC-LDPC의 girth/cycle 설계 알고리즘 및 최소거리 bound, 바이너리 코드설계(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4259740
- **Type**: conference
- **Published**: 6-8 June 2
- **Authors**: Jean-Baptiste Dore, Marie-Helene Hamon, Pierre Penard
- **PDF**: https://ieeexplore.ieee.org/document/4259740
- **Abstract**: This paper investigates cycle and distance properties of structured Low Density Parity Check (LDPC) codes based on circulant permutation matrices. A very simple algorithm to detect and construct codes with good cycle properties is proposed. A geometrical approach to design codes with good girth properties is then presented and illustrated, through the definition of rules for the design of parity check matrices without short length cycles. An upper bound on the minimal distance of the proposed structured code is also derived. The information provided by this bound can help the construction of the parity check matrices, in order to achieve a target minimum distance.

## On the minimum weight of simple full-length array LDPC codes

- **Status**: ✅
- **Reason**: array LDPC(SFA-LDPC)의 최소중량 분석 — 바이너리 QC-array LDPC 코드설계/error floor 관련 유한길이 특성(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4557314
- **Type**: conference
- **Published**: 24-29 June
- **Authors**: Kenji Sugiyama, Yuichi Kaji
- **PDF**: https://ieeexplore.ieee.org/document/4557314
- **Abstract**: Simple and full-length array LDPC codes (SFA-LDPC codes) is a class of LDPC codes which are algebraically constructed from a family of array codes. The minimum weight of SFA-LDPC codes has been investigated in literatures, but exact minimum weight of the code is not known except for some small parameters. In this paper it is shown that the class of SFA-LDPC codes which are denoted by CA (p, 4) in this paper contains a codeword whose minimum weight is 10 or less, if p is a prime number greater than 7. Combined with the Yang's lower bound on the minimum weight of CA (p,4), this implies that the minimum weight of CA (p, 4) is exactly 10 for any prime p with p > 7.

## Tight Bounds of Minimum Distance Distributions of Irregular LDPC Code Ensembles

- **Status**: ✅
- **Reason**: irregular LDPC 앙상블 최소거리 분포의 tight bound — 바이너리 LDPC 유한길이 코드설계·error floor 분석에 이식 가능(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4557315
- **Type**: conference
- **Published**: 24-29 June
- **Authors**: Shinya Miyamoto, Kenta Kasai, Tomoharu Shibuya +1
- **PDF**: https://ieeexplore.ieee.org/document/4557315
- **Abstract**: Upper bounds of minimum distance distributions of Gallger codes and irregular LDPC codes were derived by Callage and Di, respectively. Di's bounds are tight for irregular LDPC codes which have variable nodes of degree two, however, it is not tight for irregular LDPC codes which do not. In this paper, we derive tight lower and upper bounds of minimum distance distributions of irregular LDPC code ensembles without variable nodes of degree two.

## On the Minimum Distance of Generalized LDPC Codes

- **Status**: ✅
- **Reason**: LDPC 최소거리·degree-2 변수노드 사이클 구조 분석 — 코드설계(E) error floor/사이클 제거 관련 통찰 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4557106
- **Type**: conference
- **Published**: 24-29 June
- **Authors**: Ayoub Otmani, Jean-Pierre Tillich, Iryna Andriyanova
- **PDF**: https://ieeexplore.ieee.org/document/4557106
- **Abstract**: We study necessary conditions which have to be satisfied in order to have LDPC codes with linear minimum distance. We give two conditions of this kind in this paper. These conditions are not met for several interesting code families: this shows that they are not asymptotically good. The second one concerns LDPC codes that have a Tanner graph in which there are cycles linking variable nodes of degree 2 together and provides some insight about the combinatorial structure of some low-weight codewords in such a case. When the LDPC code family is obtained from the lifts of a given protograph and if there are such cycles in the protograph, the second condition seems to capture really well the linear minimum distance character of the code. This is illustrated by a code family which is asymptotically good for which there is a cycle linking all the variable nodes of degree 2 together. Surprisingly, this family is only a slight modification of a family which does not satisfy the second condition.

## Fast Decoding of Rate-Compatible Punctured LDPC Codes

- **Status**: ✅
- **Reason**: RCP-LDPC 레이어드 BP 체크노드 레이어링으로 수렴 가속 — 이식 가능 디코더 스케줄링/HW비용 무증가(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4557229
- **Type**: conference
- **Published**: 24-29 June
- **Authors**: Jini Kwon, Demijan Klinc, Jeongseok Ha +1
- **PDF**: https://ieeexplore.ieee.org/document/4557229
- **Abstract**: While rate-compatible punctured low-density parity-check (RCP-LDPC) codes offer high flexibility in terms of code rate at a relatively low cost in implementation complexity, they are reported to require more decoding iterations than unpunctured LDPC codes. In this paper1 we consider layered belief propagation decoding and propose efficient check node layering that significantly accelerates the decoding convergence of RCP-LDPC codes. We show that the proposed layering outperforms both random layering and conventional BP decoding. The performance improvements become more distinctive at high rates and they come at no additional implementation cost.

## An Algorithm to Find All Small-Size Stopping Sets of Low-Density Parity-Check Matrices

- **Status**: ✅
- **Reason**: Efficient algorithm to find all small stopping sets of an LDPC matrix; useful for error-floor/code-design evaluation (E).
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4557664
- **Type**: conference
- **Published**: 24-29 June
- **Authors**: Eirik Rosnes, Oyvind Ytrehus
- **PDF**: https://ieeexplore.ieee.org/document/4557664
- **Abstract**: In this work, we introduce an efficient algorithm to find all stopping sets of size less than some threshold of a fixed low-density parity-check (LDPC) matrix. The solution is inspired by the algorithm proposed by Rosnes and Ytrehus in 2005 to find an exhaustive list of all small-size turbo stopping sets in a turbo code. The efficiency of the proposed algorithm is demonstrated by several numerical examples. For instance, we have applied the algorithm to the well-known (3, 5)-regular (155,64) Tanner code and found all stopping sets of size at most 18 in about one minute on a standard desktop computer. Also, we have verified that the minimum stopping set size of the (4896,2474) Ramanujan-Margulis code is indeed 24, and that the corresponding multiplicity is exactly 204.

## Error Rate Estimation of Finite-Length Low-Density Parity-Check Codes on Binary Symmetric Channels Using Cycle Enumeration

- **Status**: ✅
- **Reason**: 유한길이 LDPC의 BSC상 사이클 열거 기반 오류율 추정 — error floor/사이클 분석 코드설계(E), NAND 직접 관련
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4557138
- **Type**: conference
- **Published**: 24-29 June
- **Authors**: Hua Xiao, Amir H. Banihashemi
- **PDF**: https://ieeexplore.ieee.org/document/4557138
- **Abstract**: The performance of low-density parity-check (LDPC) codes decoded by hard-decision iterative decoding algorithms can be accurately estimated if the weight J and the number |Ej| of the smallest error patterns that cannot be corrected by the decoder are known. To obtain J and |Ej|, one would need to perform the direct enumeration of error patterns with weight i les J. The complexity of enumeration increases exponentially with J, essentially as nJ, where n is the code block length. In this paper, we approximate J and |Ej| by enumerating and testing the error patterns that are subsets of short cycles in the code's Tanner graph. This reduces the computational complexity by several orders of magnitude compared to direct enumeration, making it possible to estimate the error rates for almost any practical LDPC code. To obtain the error rate estimates, we propose an algorithm that progressively improves the estimates as larger cycles are enumerated. Through a number of examples, we demonstrate that the proposed method can accurately estimate both the bit error rate (BER) and the frame error rate (FER) of regular and irregular LDPC codes decoded by a variety of hard-decision iterative decoding algorithms.

## Stopping-Set Enumerator Approximations for Finite-Length Protograph LDPC Codes

- **Status**: ✅
- **Reason**: Finite-length protograph LDPC stopping-set enumerator analysis for error-floor design; binary code design (E).
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4557666
- **Type**: conference
- **Published**: 24-29 June
- **Authors**: Kaiann Fu, Achilleas Anastasopoulos
- **PDF**: https://ieeexplore.ieee.org/document/4557666
- **Abstract**: Asymptotic analysis of low-density parity-check (LDPC) code weight and stopping-set enumerators, for codewords and stopping sets which grow linearly with codelength, has aided in designing codes with linear minimum distance and low error floors. However, the analysis cannot capture the behavior of codewords and stopping sets that grow sublinearly with codelength. Thus, it is unclear how well the analysis describes behavior for finite codelengths, particularly for short codes. In this paper, we provide another perspective on protograph-based and standard LDPC ensemble enumerators, based on analysis of stopping sets with sublinear growth, which brings new insight into sublinear stopping-set behavior, protograph structure, and preceding. Using approximations to the stopping-set enumerators, we show that for stopping sets that grow at most logarithmically with codelength, the enumerators follow a polynomial relationship with codelength, unlike the exponential relationship for linearly- growing stopping sets. Further, we analyze for what stopping-set sizes and codelengths the approximations apply.

## Cycle Analysis and Construction of Protographs for QC LDPC Codes With Girth Larger Than 12

- **Status**: ✅
- **Reason**: QC-LDPC 프로토그래프의 inevitable cycle 분석 및 girth>=14 신규 조합 구성법 제시, 바이너리 코드설계(E) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4557555
- **Type**: conference
- **Published**: 24-29 June
- **Authors**: Sunghwan Kim, Jong-Seon No, Habong Chung +1
- **PDF**: https://ieeexplore.ieee.org/document/4557555
- **Abstract**: A quasi-cyclic (QC) low-density parity-check (LDPC) code can be viewed as the protograph code with circulant permutation matrices. In this paper, we find all the subgraph patterns of protographs of QC LDPC codes having inevitable cycles of length 2i, i = 6,7,8,9,10, i.e., the cycles existing regardless of the shift values of circulants. It is also derived that if the girth of the protograph is 2g, g ges 2, its protograph code cannot have the inevitable cycles of length smaller than 6g. Based on these subgraph patterns, we propose new combinatorial construction methods of the protographs, whose protograph codes can have girth larger than or equal to 14.

## Designing LDPC Codes without small trapping sets by using Tanner Graph Covers

- **Status**: ✅
- **Reason**: Tanner graph cover로 trapping set 제거하여 error floor 낮추는 범용 코드설계 기법, 바이너리 LDPC error floor 개선(E)에 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4557557
- **Type**: conference
- **Published**: 24-29 June
- **Authors**: Milos Ivkovic, Shashi Kiran Chilappagari, Bane Vasic
- **PDF**: https://ieeexplore.ieee.org/document/4557557
- **Abstract**: We present a method for lowering the error floor of low-density parity check (LDPC) codes. It is based on Tanner graph covers that do not have trapping sets from the original code. The advantages of the method are that it is universal, as it can be applied to any LDPC code/channel model/decoding algorithm and it improves performance at the expense of increasing the code length, without losing the code regularity, without changing the decoding algorithm, and, under certain conditions, without lowering the code rate. We illustrate the method by modifying Tanner, MacKay and Margulis codes to improve performance on the binary symmetric channel (BSC) under the Gallager B decoding algorithm.

## Edge-based Scheduled BP in LDPC Codes

- **Status**: ✅
- **Reason**: 엣지 기반 스케줄 BP, 단/중간 길이 LDPC 스케줄링 이득 — 이식 가능 디코더 스케줄링 기법(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4557171
- **Type**: conference
- **Published**: 24-29 June
- **Authors**: Oren Golov, Ofer Amrani
- **PDF**: https://ieeexplore.ieee.org/document/4557171
- **Abstract**: This paper studies the potential performance gain, referred to as scheduling gain, when decoding LDPC codes using scheduled belief-propagation. Introducing genie-aided scheduling, it is shown that the scheduling-gain can be quite impressive for moderate and short-length codes. Adaptive schedule based on edge ordering is presented. This approach compares favorably with serial scheduling schemes based on random node ordering. Density evolution-based analysis appropriately tailored for decoding finite-length LDPC codes is provided. For serial decoding and genie-aided decoding, it is shown that the performance in the first iteration can be accurately predicted analytically using the proposed technique.

## Staircase and other structured linear-time encodable LDPC codes: analysis and design

- **Status**: ✅
- **Reason**: 선형시간 인코딩 가능 구조적 LDPC(staircase) 구성·앙상블 설계 — 바이너리 LDPC 코드설계(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4557125
- **Type**: conference
- **Published**: 24-29 June
- **Authors**: Federica Garin, Giacomo Como, Fabio Fagnani
- **PDF**: https://ieeexplore.ieee.org/document/4557125
- **Abstract**: We consider a family of codes which can be seen both as a special kind of serial turbo codes and as LDPC codes having a parity check matrix which is partly random and partly structured. These codes are linear-time encodable, thanks to the turbo structure, and can be decoded as LDPC codes. We provide an ensemble analysis for the waterfall region, on the line of classical results for serial turbo codes, and we find some design parameters.

## Iterative LDPC decoding using neighborhood reliabilities

- **Status**: ✅
- **Reason**: 이웃 신뢰도 기반 노드 처리순서로 min-sum을 sum-product 성능에 근접 — 이식 가능 min-sum 디코더 개선(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4557230
- **Type**: conference
- **Published**: 24-29 June
- **Authors**: Valentin Savin
- **PDF**: https://ieeexplore.ieee.org/document/4557230
- **Abstract**: In this paper we study the impact of the processing order of nodes of a bipartite graph, on the performance of an iterative message-passing decoding. To this end, we introduce the concept of neighborhood reliabilities of graph's nodes. Nodes reliabilities are calculated at each iteration and then are used to obtain a processing order within a serial or serial/parallel scheduling. The basic idea is that by processing first the most reliable data, the decoder is reinforced before processing the less reliable one. Using neighborhood reliabilities, the min-sum decoder of LDPC codes approaches the performance of the sum-product decoder.

## On the error correction of regular LDPC codes using the flipping algorithm

- **Status**: ✅
- **Reason**: regular LDPC bit-flipping 알고리즘 오류정정 능력 분석(left degree 4 확장), 이식 가능 디코더(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4557085
- **Type**: conference
- **Published**: 24-29 June
- **Authors**: David Burshtein
- **PDF**: https://ieeexplore.ieee.org/document/4557085
- **Abstract**: We apply the iterative bit flipping algorithm to the standard regular low-density parity-check (LDPC) code ensemble. In the past it was shown, for a typical code in the ensemble with left degree at least five and block length sufficiently large, that this algorithm can correct all error patterns with some linear (in the block length) number of errors. We extend this result to the case where the left degree is at least four. For the case where the left degree is larger than four, we obtain an improvement of several orders of magnitude compared to the existing results on the fraction of worst case errors that can be corrected. We also show how our results can be improved when we consider random errors (as opposed to worst case errors) produced by the channel.

## Constructing LDPC Codes by 2-Lifts

- **Status**: ✅
- **Reason**: 2-lift 기반 LDPC 구성으로 error floor 저감, stopping set 설계 기준 - 코드설계(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4557391
- **Type**: conference
- **Published**: 24-29 June
- **Authors**: Xudong Ma, En-hui Yang
- **PDF**: https://ieeexplore.ieee.org/document/4557391
- **Abstract**: With the motivation of constructing Low-Density Parity-Check (LDPC) codes with low error floors, we propose a new code construction scheme based on random 2-lifts. An analysis on stopping set distributions of the proposed code ensembles is presented. The analysis shows that low-weight stopping sets in the resulting codes are typically the results of stopping sets with weak graph expansion properties in the base graphs. Based on this analysis, we propose a set of design criteria for constructing codes with low error floors. According to the design criteria, stopping sets with weak graph expansion properties should be avoided in the base graphs. We present numerical results on constructing capacity-approaching codes over Binary Erasure Channels (BEC). The numerical results show that the codes by the proposed scheme have significantly lower error floors compared with the codes by the standard construction.

## Tail-Biting LDPC Convolutional Codes

- **Status**: ✅
- **Reason**: tail-biting LDPC convolutional code의 패리티검사행렬/인코더·디코더 아키텍처 및 최소거리 분석, 바이너리 SC-LDPC 코드설계(E) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4557569
- **Type**: conference
- **Published**: 24-29 June
- **Authors**: Marcos B.S. Tavares, Kamil Sh. Zigangirov, Gerhard P. Fettweis
- **PDF**: https://ieeexplore.ieee.org/document/4557569
- **Abstract**: In this paper, the tail-biting version of the low-density parity-check convolutional codes (LDPCCCs) is introduced and investigated. The definition of the tail-biting LDPCCCs (TB-LDPCCCs) is given through their parity-check matrices and the basic ideas behind the architectures of the encoders and decoders for these codes are also presented. In addition, the asymptotical lower bound for the minimum distance of these codes and simulation results are shown.

## Analytical Performance of One-Step Majority Logic Decoding of Regular LDPC Codes

- **Status**: ✅
- **Reason**: 정규 LDPC의 one-step majority logic 디코딩 BER 정확 계산 조합 알고리즘 + 나노스케일 메모리 적용 언급 — 디코더 분석 기법 이식 가능(C), 메모리 ECC 관련
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4557231
- **Type**: conference
- **Published**: 24-29 June
- **Authors**: Rathnakumar Radhakrishnan, Sundararajan Sankaranarayanan, Bane Vasic
- **PDF**: https://ieeexplore.ieee.org/document/4557231
- **Abstract**: In this paper, we present a combinatorial algorithm to calculate the exact bit error rate performance of regular low-density parity check codes under one-step majority logic decoding. Majority logic decoders have regained importance in nano-scale memories due to their resilience to both memory and logic gate failures. This result is an extension of the work of Rudolph on error correction capability of majority-logic decoders.

## On Deriving Good LDPC Convolutional Codes from QC LDPC Block Codes

- **Status**: ✅
- **Reason**: QC LDPC에서 LDPC convolutional code 유도, short cycle 감소로 BER 개선 - 이식 가능 코드설계(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4557390
- **Type**: conference
- **Published**: 24-29 June
- **Authors**: Ali Emre Pusane, Roxana Smarandache, Pascal O. Vontobel +1
- **PDF**: https://ieeexplore.ieee.org/document/4557390
- **Abstract**: In this paper we study the iterative decoding behavior of time-invariant and time-varying LDPC convolutional codes derived by unwrapping QC LDPC block codes. In particular, for a time-varying LDPC convolutional code, we show that the minimum pseudo-weight of the convolutional code is at least as large as the minimum pseudo-weight of the underlying QC code. We also prove that the unwrapped convolutional codes have fewer short cycles than the QC codes. These results taken together lead to improved BER performance in the low-to-moderate SNR region, where the decoding behavior is influenced by the complete pseudo-codeword spectra and by the Tanner graph cycle histogram, with the time-varying convolutional codes outperforming both the underlying QC block codes and their time-invariant convolutional counterparts.

## On Codes Constructed by Generalized Kronecker Product

- **Status**: ✅
- **Reason**: Generalized Kronecker product로 큰 girth circulant LDPC 구성, 효율적 인코딩 - 바이너리 코드설계(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4557392
- **Type**: conference
- **Published**: 24-29 June
- **Authors**: Wen-Yao Chen, Chung-Chin Lu
- **PDF**: https://ieeexplore.ieee.org/document/4557392
- **Abstract**: In this paper, we apply generalized Kronecker product recursively to construct low-density parity-check (LDPC) codes with arbitrarily large girth. The parity check matrices of these codes are block matrices consisting of circulant permutation matrices, thus may benefit from efficient encoding. It turns out that the LU(m, q) codes proposed in the literature is a special case of this construction for prime q. Connectivity of Tanner graphs of these codes are investigated.

## Multiple-Bases Belief-Propagation for Decoding of Short Block Codes

- **Status**: ✅
- **Reason**: 대수 블록부호용 다중기저(dual code) BP 소프트디코딩 — 부호 비의존적 BP 개선으로 바이너리 LDPC BP에 이식 가능, 반복수 감소·near-ML(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4557244
- **Type**: conference
- **Published**: 24-29 June
- **Authors**: Thorsten Hehn, Johannes B. Huber, Stefan Laendner +1
- **PDF**: https://ieeexplore.ieee.org/document/4557244
- **Abstract**: A novel soft-decoding method for algebraic block codes is presented. The algorithm is designed for soft-decision decoding and is based on belief-propagation (BP) decoding using multiple bases of the dual code. Compared to other approaches for high-performance BP decoding, this method is conceptually simple and does not change at each stage of the decoding process. With its multiple BP decoders the proposed scheme achieves the performance of a standard BP algorithm with a significantly lower number of iterations per decoder realization. By this means the data delay introduced by decoding is reduced. Moreover, a significant improvement in decoding performance is achieved while keeping the data delay small. It is shown that for selected codes the proposed scheme approaches near maximum likelihood (ML) performance for very small data processing delays.

## Generalized Iterative Decoding for Linear Block Codes on the Binary Erasure Channel

- **Status**: ✅
- **Reason**: BEC상 선형블록부호 일반화 반복디코딩(차수 vs girth 분석) — LDPC 반복디코더 개선 기법, girth 연관 디코더 설계(C/E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4557205
- **Type**: conference
- **Published**: 24-29 June
- **Authors**: Khaled A.S. Abdel-Ghaffar, Jos H. Weber
- **PDF**: https://ieeexplore.ieee.org/document/4557205
- **Abstract**: The generalized iterative decoding concept offers attractive performance versus complexity trade-off opportunities in the spectrum between traditional iterative decoding and optimal decoding for linear block codes over the binary erasure channel. In each iteration, a system of equations is solved. The maximum number of equations to be solved in one iteration is called the order of the decoder. In case the order is just one, the generalized iterative decoder reduces to the traditional iterative decoder. On the other hand, if the order is set to the redundancy of the codes, the generalized iterative decoder gives the same performance as the optimal decoder. Varying the order between these two extremes allows for a better match to the system specifications. In this paper, we consider aspects regarding the implementation of generalized iterative decoding and we determine the minimum order (as a function of the girth) that can potentially lead to improvement over traditional iterative decoding.

## Improving the Performance of Protograph LDPC Codes by Using Different Transmission Energies

- **Status**: ✅
- **Reason**: 프로토그래프 LDPC에 변수노드별 전송에너지 분포 최적화(밀도진화 일반화) — 코드설계/임계값 최적화 기법, 바이너리 LDPC 이식 가능(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4557166
- **Type**: conference
- **Published**: 24-29 June
- **Authors**: Gerd Richter, Martin Bossert
- **PDF**: https://ieeexplore.ieee.org/document/4557166
- **Abstract**: Irregular low-density parity-check (LDPC) codes constructed from small protographs are one of the most powerful LDPC codes. In this paper, we show that the performance of LDPC codes based on small protographs can be further improved by using different transmission energies for every variable node of the protograph. Thus, a protograph is now described by a set of variable nodes, a set of check nodes, edges connecting variable nodes and check nodes, and the transmission energy used for every variable node, which is called the energy distribution. We optimize the energy distribution of protographs by choosing the energy distribution with the highest threshold calculated with a generalization of the discretized density evolution. Furthermore, we show by simulations that the performance of long LDPC codes based on protographs can be improved as expected from the thresholds.

## Pseudo-codeword Landscape

- **Status**: ✅
- **Reason**: LP 디코딩 dendro trick으로 복잡도 저감, pseudo-codeword 기반 error floor 분석 - 이식 가능 디코더(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4557442
- **Type**: conference
- **Published**: 24-29 June
- **Authors**: Michael Chertkov, Mikhail Stepanov
- **PDF**: https://ieeexplore.ieee.org/document/4557442
- **Abstract**: We discuss the performance of low-density-parity-check (LDPC) codes decoded by means of linear programming (LP) at moderate and large signal-to-noise-ratios (SNR). Utilizing a combination of the previously introduced pseudo-codeword-search method and a new "dendro" trick, which allows us to reduce the complexity of the LP decoding, we analyze the dependence of the frame-error-rate (FER) on the SNR. Under maximum-a-posteriori (MAP) decoding the dendro-code, having only checks with connectivity degree three, performs identically to its original code with high-connectivity checks. For a number of popular LDPC codes performing over the additive-white-Gaussian-noise (AWGN) channel we found that either an error-floor sets at a relatively low SNR, or otherwise a transient asymptote, characterized by a faster decay of FER with the SNR increase, precedes the error-floor asymptote. We explain these regimes in terms of the pseudo-codeword spectra of the codes.

## Explicit Construction of Type-II QC LDPC Codes with Girth at least 6

- **Status**: ✅
- **Reason**: Type-II QC-LDPC explicit construction with girth>=6 conditions; new binary code design technique (E).
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4557574
- **Type**: conference
- **Published**: 24-29 June
- **Authors**: Kristine Lally
- **PDF**: https://ieeexplore.ieee.org/document/4557574
- **Abstract**: Type-II quasi-cyclic (QC) LDPC codes are constructed from combinations of weight-0, weight-1 and weight-2 circulant matrices. The structure of cycles of length 2n are investigated, and necessary and sufficient conditions for a type-II QC LDPC parity check matrix H to have girth at least 2(n + 1) are given. An explicit construction of type-II codes which guarantees girth at least 6 is presented. A necessary and sufficient condition for a QC matrix with one or more rows of circulants, to be fullrank is derived.

## ML decoding via mixed-integer adaptive linear programming

- **Status**: ✅
- **Reason**: adaptive LP+정수제약으로 ML 디코더 구현, 바이너리 LDPC 디코딩 - 이식 가능 디코더(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4557459
- **Type**: conference
- **Published**: 24-29 June
- **Authors**: Stark C. Draper, Jonathan S. Yedidia, Yige Wang
- **PDF**: https://ieeexplore.ieee.org/document/4557459
- **Abstract**: Linear programming (LP) decoding was introduced by Feldman et al. (IEEE Trans. Inform. Theory Mar. 2005) as a novel way to decode binary low-density parity-check codes. Taghavi and Siegel (Proc. ISIT 2006) describe a computationally simplified decoding approach they term "adaptive" LP decoding. Adaptive LP decoding starts with a sub-set of the LP constraints, and iteratively adds violated constraints until an optimum of the original LP is found. Usually only a tiny fraction of the original constraints need to be reinstated, leading to huge efficiency gains compared to ordinary LP decoding. Here we describe a modification of the adaptive LP decoder that results in a maximum likelihood (ML) decoder. Whenever the adaptive LP decoder returns a pseudo-codeword rather than a codeword, we add an integer constraint on the least certain symbol of the pseudo-codeword. For certain codes, and especially in the high-SNR (error floor) regime, only a few integer constraints are required to force the resultant mixed-integer LP to the ML solution. We demonstrate that our approach can efficiently achieve the optimal ML decoding performance on a (155,64) LDPC code introduced by Tanner et al.

## Average Stopping Set Weight Distribution of Redundant Random Matrix Ensembles

- **Status**: ✅
- **Reason**: Redundant rows reducing small stopping sets in binary parity-check matrices; relevant to error-floor/code-design analysis (E).
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4557663
- **Type**: conference
- **Published**: 24-29 June
- **Authors**: Tadashi Wadayama
- **PDF**: https://ieeexplore.ieee.org/document/4557663
- **Abstract**: In this paper, redundant random matrix ensembles (abbreviated as redundant random ensembles) are defined and their stopping set (SS) weight distributions are analyzed. A redundant random ensemble consists of a set of binary matrices with linearly dependent rows. These linearly dependent rows (redundant rows) significantly reduce the number of stopping sets of small size. Upper and lower bounds on the average SS weight distribution of the redundant random ensembles are shown.

## EXIT Chart Analysis of Binary Message-Passing Decoders

- **Status**: ✅
- **Reason**: 바이너리 message-passing 디코더 EXIT 분석·Gallager B 변형, 출력 알파벳 확장으로 이득 — 이식 가능 디코더 기법(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4557334
- **Type**: conference
- **Published**: 24-29 June
- **Authors**: Gottfried Lechner, Troels Pedersen, Gerhard Kramer
- **PDF**: https://ieeexplore.ieee.org/document/4557334
- **Abstract**: Binary message-passing decoders for LDPC codes are analyzed using EXIT charts. For the analysis, the variable node decoder performs all computations in the L-value domain. For the special case of a hard decision channel, this leads to the well-know Gallager B algorithm, while the analysis can be extended to channels with larger output alphabets. By increasing the output alphabet from hard decisions to four symbols, a gain of more than 1.0 dB is achieved using optimized codes. For this code optimization, the mixing property of EXIT functions has to be modified to the case of binary message-passing decoders.

## Equalization on Graphs: Linear Programming and Message Passing

- **Status**: ✅
- **Reason**: ISI 채널 등화를 바이너리 디코딩으로 변환해 LDPC 디코딩과 결합(LP/메시지패싱) — BP 결합 가능 디코더 기법(C), 애매하나 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4557178
- **Type**: conference
- **Published**: 24-29 June
- **Authors**: Mohammad H. Taghavi, Paul H. Siegel
- **PDF**: https://ieeexplore.ieee.org/document/4557178
- **Abstract**: We propose an approximation of maximum-likelihood detection in ISI channels based on linear programming or message passing. We convert the detection problem into a binary decoding problem, which can be easily combined with LDPC decoding. We show that, for a certain class of channels and in the absence of coding, the proposed technique provides the exact ML solution without an exponential complexity in the size of channel memory, while for some other channels, this method has a non-diminishing probability of failure as SNR increases. Some analysis is provided for the error events of the proposed technique under linear programming.

## Towards Understanding Weighted Bit-Flipping Decoding

- **Status**: ✅
- **Reason**: weighted bit-flipping과 message-passing 관계, 병렬 구현으로 빠른 수렴 - 이식 가능 디코더/HW(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4557461
- **Type**: conference
- **Published**: 24-29 June
- **Authors**: Xiaofu Wu, Cong Ling, Ming Jiang +3
- **PDF**: https://ieeexplore.ieee.org/document/4557461
- **Abstract**: A natural relationship between weighted bit-flipping (WBF) decoding and message-passing decoding is explored. This understanding can help us develop a dual WBF decoding algorithm from one type of message-passing decoding algorithm and vice versa. For min-sum decoding, one can find that its dual WBF algorithm is the algorithm proposed by Jiang et al. For belief-propagation (BP) decoding, we propose a new WBF algorithm and show its performance advantage. For some high-rate low-density parity-check (LDPC) codes of large row weight, it is shown that the WBF algorithm proposed by Liu and Pados performs extraordinarily well. However, its dual message- passing decoding does not work well. Furthermore, we propose a parallel implementation framework for various WBF algorithms. Compared to serial implementations, various WBF algorithms in their parallel form converge significantly faster and often perform better.

## A Combinatorial Family of Near Regular LDPC Codes

- **Status**: ✅
- **Reason**: high-girth near-regular LDPC Tanner 그래프 구성(quadratic time, rate/girth 보장) — 바이너리 LDPC 코드설계·girth 기법(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4557316
- **Type**: conference
- **Published**: 24-29 June
- **Authors**: K. Murali Krishnan, Rajdeep Singh, L. Sunil Chandran +1
- **PDF**: https://ieeexplore.ieee.org/document/4557316
- **Abstract**: An elementary combinatorial Tanner graph construction for a family of near-regular low density parity check (LDPC) codes achieving high girth is presented. These codes are near regular in the sense that the degree of a left/right vertex is allowed to differ by at most one from the average. The construction yields in quadratic time complexity an asymptotic code family with provable lower bounds on the rate and the girth for a given choice of block length and average degree. The construction gives flexibility in the choice of design parameters of the code like rate, girth and average degree. Performance simulations of iterative decoding algorithm for the AWGN channel on codes designed using the method demonstrate that these codes perform better than regular PEG codes and MacKay codes of similar length for all values of Signal to noise ratio.

## Constraint Relaxation and Annealed Belief Propagation for Binary Networks

- **Status**: ✅
- **Reason**: annealed/generalized BP로 수렴 개선(동적 온도, free energy) — LDPC 디코딩에 직접 적용 검증, 이식 가능한 BP 개선 기법(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4557246
- **Type**: conference
- **Published**: 24-29 June
- **Authors**: Yen-Chih Chen, Yu T. Su
- **PDF**: https://ieeexplore.ieee.org/document/4557246
- **Abstract**: In this paper, we propose two novel generalized belief propagation (BP) algorithms to improve the convergence behavior of the conventional BP algorithm. By incorporating a dynamic temperature into the free energy formulation, message passing is performed on a dynamic surface of energy cost. The proposed cooling process helps BP converge to a stable fixed point with a lower energy value that leads to better estimations. For decoding turbo-like error correcting codes, we adopt a parametric Gaussian approximation to relax the binary parity check constraints and generalize the conventional binary networks as well. Both the computational complexity and the convergence rate of the proposed annealed BP algorithms are almost the same as those of the conventional BP algorithm. Simulated performance of the proposed algorithms when they are used to decode a low density parity check (LDPC) code and the (23,12) Golay code is presented to validate our proposals.

## On the Dynamics of Analog Min-Sum Iterative Decoders, an Analytical Approach

- **Status**: ✅
- **Reason**: 아날로그 min-sum 디코더의 동역학 해석 — 이식 가능 디코더 알고리즘(C) 변형, NAND LDPC BP에 적용 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4557089
- **Type**: conference
- **Published**: 24-29 June
- **Authors**: Saied Hemati, Abbas Yongacoglu
- **PDF**: https://ieeexplore.ieee.org/document/4557089
- **Abstract**: In this paper, we show that an ideal analog min-sum decoder, in the log-likelihood ratio domain, can be considered as a piecewise linear system. Many theoretical aspects of these decoders, thus, can be studied analytically. It is also shown that the dynamic equations can become singular and degrade the decoding performance. When the decoder is nonsingular, the corresponding dynamic equations can be solved analytically to derive outputs of the decoder. The proposed approach paves the way for further analytical analysis on the dynamics of analog min-sum decoders.

## Encoding for the Blackwell Channel with Reinforced Belief Propagation

- **Status**: ✅
- **Reason**: Reinforced BP 알고리즘은 BP를 solver로 전환하는 부호 비의존적 메시지패싱 변형으로 바이너리 LDPC BP 개선(C)에 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4557497
- **Type**: conference
- **Published**: 24-29 June
- **Authors**: Alfredo Braunstein, Farbod Kayhan, Guido Montorsi +1
- **PDF**: https://ieeexplore.ieee.org/document/4557497
- **Abstract**: A key idea in coding for the broadcast channel (BC) is binning, in which the transmitter encode information by selecting a codeword from an appropriate bin (the messages are thus the bin indexes). This selection is normally done by solving an appropriate (possibly difficult) combinatorial problem. Recently it has been shown that binning for the Blackwell channel -a particular BC- can be done by iterative schemes based on Survey Propagation (SP). This method uses decimation for SP and suffers a complexity of O(n2). In this paper we propose a new variation of the Belief Propagation (BP) algorithm, named Reinforced BP algorithm, that turns BP into a solver. Our simulations show that this new algorithm has complexity O(n log n). Using this new algorithm together with a non-linear coding scheme, we can efficiently achieve rates close to the border of the capacity region of the Blackwell channel.

## Optimum Linear LLR Calculation for Iterative Decoding on Fading Channels

- **Status**: ✅
- **Reason**: 페이딩 채널 반복디코딩용 최적 선형 LLR 근사 계산 — LLR 양자화/근사 기법, NAND LLR 계산에 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4557204
- **Type**: conference
- **Published**: 24-29 June
- **Authors**: Raman Yazdani, Masoud Ardakani
- **PDF**: https://ieeexplore.ieee.org/document/4557204
- **Abstract**: On a fading channel with no channel state information at the receiver, calculating true log-likelihood ratios (LLR) is complicated. Existing work assume that the power of the additive noise is known and use the expected value of the fading gain in a linear function of the channel output to find approximate LLRs. In this work, we first assume that the power of the additive noise is known and we find the optimum linear approximation of LLRs in the sense of maximum achievable transmission rate on the channel. The maximum achievable rate under this linear LLR calculation is almost equal to the maximum achievable rate under true LLR calculation. We also observe that this method appears to be the optimum in the sense of bit error rate performance too. These results are then extended to the case that the noise power is unknown at the receiver and a performance almost identical to the case that the noise power is perfectly known is obtained.

## EXIT and Density Evolution Analysis for Homogeneous Expectation Propagation

- **Status**: ✅
- **Reason**: BP/EP의 EXIT·밀도진화 분석을 LDPC 소프트 디코딩에서 확장 — 디코더 수렴분석 도구(C/E) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4557111
- **Type**: conference
- **Published**: 24-29 June
- **Authors**: John MacLaren Walsh
- **PDF**: https://ieeexplore.ieee.org/document/4557111
- **Abstract**: We extend Gaussian approximation density evolution (DE) techniques from the soft iterative decoding of turbo and low density parity check (LDPC) codes to the performance and convergence analysis of belief propagation (BP) and expectation propagation (EP) in randomly connected very large sparse homogeneous factor graphs. A strict form of the Gaussian approximation allows the use of extrinsic information transfer (EXIT) charts to study the performance and convergence of the algorithms. The result is a graphical tool that design engineers can use to quickly predict the performance and convergence speed of BP or EP applied to these inference problems. We demonstrate the utility of the new tool, and a motivation for the generalization of the results, by showing how it may surprisingly be applied to determine the performance of a scheme for distributed data fusion in a sensor network.

## ACE Spectrum of LDPC Codes and Generalized ACE Design

- **Status**: ✅
- **Reason**: ACE spectrum and generalized ACE design for finite-length LDPC; cycle/stopping-set based code design (E).
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4288785
- **Type**: conference
- **Published**: 24-28 June
- **Authors**: D. Vukobratovic, A. Djurendic, V. Senk
- **PDF**: https://ieeexplore.ieee.org/document/4288785
- **Abstract**: The construction of good, finite-length, LDPC codes is currently an attractive research area. Reducing attention to the binary erasure channel (BEC), this problem translates into the problem of finding elements of selected (irregular) LDPC code ensemble with the size of the minimal stopping set being maximized. Faced with the lack of analytical solution to this problem, simple but powerful heuristic design algorithm, an ACE constrained design algorithm, was recently introduced. Building upon the ACE metric associated with every cycle in the code graph, we introduce the ACE spectrum of LDPC code as a useful measure of success in selection of the LDPC code from selected ensemble. Using ACE spectrum, we farther generalize ACE constrained design, making it more flexible and efficient.

## A Modified Bit-Flipping Decoding Algorithm for Low-Density Parity-Check Codes

- **Status**: ✅
- **Reason**: Modified multi-bit-flipping decoding algorithm for LDPC; portable decoder technique (C).
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4288783
- **Type**: conference
- **Published**: 24-28 June
- **Authors**: T. M. N. Ngatched, F. Takawira, M. Bossert
- **PDF**: https://ieeexplore.ieee.org/document/4288783
- **Abstract**: In this paper, a modified bit-flipping decoding algorithm for low-density parity-check (LDPC) codes is proposed. Both improvement in performance and reduction in decoding delay are observed by flipping multiple bits in each iteration. Our studies show that the proposed algorithm achieves an appealing tradeoff between performance and complexity for many constructions of LDPC codes.

## Lowering Error Floor of LDPC Codes Using a Joint Row-Column Decoding Algorithm

- **Status**: ✅
- **Reason**: joint row-column 디코딩으로 error floor/trapping set 개선 + FPGA 구현 — 이식 가능 디코더(C)+HW(D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4288827
- **Type**: conference
- **Published**: 24-28 June
- **Authors**: Z. He, S. Roy, P. Fortier
- **PDF**: https://ieeexplore.ieee.org/document/4288827
- **Abstract**: Low-density parity-check codes using the belief-propagation decoding algorithm tend to exhibit a high error floor in the bit error rate curves, when some problematic graphical structures, such as the so-called trapping sets, exist in the corresponding Tanner graph. This paper presents a joint row-column decoding algorithm to lower the error floor, in which the column processing is combined with the processing of each row. By gradually updating the pseudo-posterior probabilities of all bit nodes, the proposed algorithm minimizes the propagation of erroneous information from trapping sets into the whole graph. The simulation indicates that the proposed joint decoding algorithm improves the performance in the waterfall region and lowers the error floor. Implementation results into field programmable gate array (FPGA) devices indicate that the proposed joint decoder increases the decoding speed by a factor of eight, compared to the traditional decoder.

## An Efficient Analysis of Finite-Length LDPC Codes

- **Status**: ✅
- **Reason**: 유한길이 바이너리 LDPC 성능 해석(E 코드설계 관련) — 채널변동 기반 블록오류 예측, 애매하므로 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4288787
- **Type**: conference
- **Published**: 24-28 June
- **Authors**: R. Yazdani, M. Ardakani
- **PDF**: https://ieeexplore.ieee.org/document/4288787
- **Abstract**: An efficient method for finite-length low-density parity-check (LDPC) code analysis is proposed. This method is based on studying the channel variations when observed during a finite-length codeword. To this end, channel parameters are interpreted as random variables and their distributions are found. Assuming that a decoding failure is the result of an observed channel worse than the code's decoding threshold, the block error probability of finite-length LDPC codes is estimated. Using an extrinsic information transfer chart analysis, bit error probability is obtained from the block error probability. Our results suggest that by considering only the channel variations around its expected behavior and even ignoring the effects of cycles, one can closely predict the performance of LDPC codes of a few thousand bits or longer in the waterfall region.

## Systematic Modification of Parity-Check Matrices for Efficient Encoding of LDPC Codes

- **Status**: ✅
- **Reason**: 패리티검사행렬 수정으로 효율적 인코딩(stopping set 회피) — 바이너리 LDPC 코드설계/인코더 기법(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4288831
- **Type**: conference
- **Published**: 24-28 June
- **Authors**: M. Shaqfeh, N. Goertz
- **PDF**: https://ieeexplore.ieee.org/document/4288831
- **Abstract**: An algorithm for efficient encoding of LDPC codes is presented that does not impose any restrictions on the construction of the parity-check matrices. The algorithm modifies the parity check matrix, without changing the subspace spanned by its rows, by removing linear dependent rows and adding a small number of new rows such that the graph-based message-passing encoder will not get stuck in a stopping set. The added rows are designed by a new algorithm which is based on the notion of the "key set". The encoder exploits the sparseness of the parity-check matrix, and the encoding complexity grows almost linear with the blocksize, because the number of added rows, which may not be sparse, is relatively small.

## Quantization Effects in Low-Density Parity-Check Decoders

- **Status**: ✅
- **Reason**: LDPC 디코더 양자화가 absorbing set·error floor에 미치는 영향과 adaptive quantization — NAND LLR 양자화/error floor에 직결되는 디코더 기법(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4289703
- **Type**: conference
- **Published**: 24-28 June
- **Authors**: Z. Zhang, L. Dolecek, M. Wainwright +2
- **PDF**: https://ieeexplore.ieee.org/document/4289703
- **Abstract**: A. class of combinatorial structures, called absorbing sets, strongly influences the performance of low-density parity- check (LDPC) decoders. In particular, the quantization scheme strongly affects which absorbing sets dominate in the error-floor region. Absorbing sets may be characterized as weak or strong. They are a characteristic of the parity check matrix of a code. Conventional quantization schemes applied to a (2209,1978) array-based LDPC code can induce low-weight weak absorbing sets and, as a result, elevate the error floor. Adaptive quantization schemes alleviate the effects of weak absorbing sets, and, as a result, only the strong ones dominate the error floor of an optimized decoder implementation. Another benefit of an adaptive quantization scheme is that it performs well even in very few iterations.

## Informed Dynamic Scheduling for Belief-Propagation Decoding of LDPC Codes

- **Status**: ✅
- **Reason**: Informed Dynamic Scheduling BP 디코딩 — trapping set 해소, 이식 가능 디코더 스케줄링 기법(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4288829
- **Type**: conference
- **Published**: 24-28 June
- **Authors**: A. I. V. Casado, M. Griot, R. D. Wesel
- **PDF**: https://ieeexplore.ieee.org/document/4288829
- **Abstract**: Low-density parity-check (LDPC) codes are usually decoded by running an iterative belief-propagation, or message-passing, algorithm over the factor graph of the code. The traditional message-passing schedule consists of updating all the variable nodes in the graph, using the same pre-update information, followed by updating all the check nodes of the graph, again, using the same pre-update information. Recently several studies show that sequential scheduling, in which messages are generated using the latest available information, significantly improves the convergence speed in terms of number of iterations. Sequential scheduling raises the problem of finding the best sequence of message updates. This paper presents practical scheduling strategies that use the value of the messages in the graph to find the next message to be updated. Simulation results show that these informed update sequences require significantly fewer iterations than standard sequential schedules. Furthermore, the paper shows that informed scheduling solves some standard trapping set errors. Therefore, it also outperforms traditional scheduling for a large numbers of iterations. Complexity and implementability issues are also addressed.

## VLSI Architectures for Layered Decoding for Irregular LDPC Codes of WiMax

- **Status**: ✅
- **Reason**: WiMax irregular LDPC layered decoding VLSI 아키텍처 — offset min-sum value-reuse, block-serial 스케줄링, 메모리/throughput 개선 HW 기법 이식 가능(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:4289421
- **Type**: conference
- **Published**: 24-28 June
- **Authors**: K. K. Gunnam, G. S. Choi, M. B. Yeary +1
- **PDF**: https://ieeexplore.ieee.org/document/4289421
- **Abstract**: We present a new multi-rate architecture for decoding irregular LDPC codes in IEEE 802.16e WiMax standard. The proposed architecture utilizes the value-reuse property of offset min-sum, block-serial scheduling of computations and turbo decoding message passing algorithm. The decoder has the following advantages: 55% savings in memory, reduction of routers by 50%, and increase of throughput by 2times when compared to the recent state-of-the-art decoder architectures.

## A Class of LDPC Erasure Distributions with Closed-Form Threshold Expression

- **Status**: ✅
- **Reason**: New LDPC degree-distribution family with closed-form threshold; binary code-design technique (E), though BEC-focused.
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4288784
- **Type**: conference
- **Published**: 24-28 June
- **Authors**: E. Paolini, M. Chiani
- **PDF**: https://ieeexplore.ieee.org/document/4288784
- **Abstract**: In this paper, a family of low-density parity-check (LDPC) degree distributions, whose decoding threshold on the binary erasure channel (BEC) admits a simple closed form, is presented. These degree distributions are a subset of the check regular distributions (i.e. all the check nodes have the same degree), and are referred to as p-positive distributions. It is given proof that the threshold for a p-positive distribution is simply expressed by [lambda'(0)rho'(1)]-1. Besides this closed form threshold expression, the p-positive distributions exhibit three additional properties. First, for given code rate, check degree and maximum variable degree, they are in some cases characterized by a threshold which is extremely close to that of the best known check regular distributions, under the same set of constraints. Second, the threshold optimization problem within the p-positive class can be solved in some cases with analytic methods, without using any numerical optimization tool. Third, these distributions can achieve the BEC capacity. The last property is shown by proving that the well-known binomial degree distributions belong to the p-positive family.

## Analysis of Absorbing Sets for Array-Based LDPC Codes

- **Status**: ✅
- **Reason**: array-based LDPC의 absorbing set 분석·열거 — error floor 원인 규명으로 코드설계(E)에 직접 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4289708
- **Type**: conference
- **Published**: 24-28 June
- **Authors**: L. Dolecek, Z. Zhang, V. Anantharam +2
- **PDF**: https://ieeexplore.ieee.org/document/4289708
- **Abstract**: Low density parity check codes (LDPC) are known to perform very well under iterative decoding. However, these codes also exhibit a change in the slope of the bit error rate (BER) vs. signal to noise ratio (SNR) curve in the very low BER region. In our earlier work using hardware emulation in this deep BER regime we argue that this behavior can be attributed to specific structures within the Tanner graph associated with an LDPC code, called absorbing sets. In this paper we provide a detailed theoretical analysis of absorbing sets for array-based LDPC codes Cp.gamma. Specifically, we identify and enumerate all the smallest absorbing sets for these array-based LDPC codes with gamma = 2,3,4 with standard parity check matrix. Experiments carried out on the emulation platform show excellent agreement with our theoretical results.

## A 19-mode 8.29mm2 52-mW LDPC Decoder Chipp for IEEE 802.16e System

- **Status**: ✅
- **Reason**: LDPC 디코더 칩: 디코딩 지연 감소·HW 이용률 향상·early termination 기법, NAND LDPC HW(D)에 이식 가능
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:4342718
- **Type**: conference
- **Published**: 14-16 June
- **Authors**: Xin-Yu Shih, Cheng-Zhou Zhan, Cheng-Hung Lin +1
- **PDF**: https://ieeexplore.ieee.org/document/4342718
- **Abstract**: This paper presents a LDPC decoder chip supporting all 19 modes in IEEE 802.16e system. An efficient design strategy is proposed to reduce 31.25% decoding latency, and enhance hardware utilization ratio from 50% to 75%. Besides, we propose an early termination scheme that can dynamically adjust the number of iterations. The multi-mode chip can be maximally measured at 83.3 MHz with only 52 mW power consumption. The core area is 4.45 mm2 and the die area is 8.29 mm2.
