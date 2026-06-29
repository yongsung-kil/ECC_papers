# IEEE Xplore — 2006-07 (1차선별 통과)


## A low-cost parallel scalable FPGA architecture for regular and irregular LDPC decoding

- **Status**: ✅
- **Reason**: 병렬 확장형 FPGA LDPC 디코더 아키텍처 — 이식 가능 HW 구현(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:1658216
- **Type**: journal
- **Published**: July 2006
- **Authors**: F. Verdier, D. Declercq
- **PDF**: https://ieeexplore.ieee.org/document/1658216
- **Abstract**: We present in this paper an architectural model for implementing parallel and scalable low-density parity-check (LDPC) decoders. This model has been developed for targeting field-programmable gate array devices and system-on-chip (SoC) platforms. We present first the motivations of investigating a new hardware model for regular and irregular LDPC decoders. The code flexibility, the memory usage optimization, and an easy hardware integration have been taken into account. The construction of a specific class of codes (hardware-constrained LDPC codes) is then presented. Parallelization and pseudorandomness constraints of codes are particularly detailed. A complete description of our parallel and scalable hardware model suitable for reprogrammable architectures is then given. Simulation results are presented showing the efficiency of this model with both (3,6) regular and irregular codes

## Mean field and mixed mean field iterative decoding of low-density parity-check codes

- **Status**: ✅
- **Reason**: Mean field/mixed mean field LDPC 디코딩 알고리즘 — BP 근사 대체 디코더, 바이너리 LDPC에 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1650362
- **Type**: journal
- **Published**: July 2006
- **Authors**: Juntan Zhang, M. Fossorier
- **PDF**: https://ieeexplore.ieee.org/document/1650362
- **Abstract**: In this paper, the mean field (MF) and mixed mean field (MMF) algorithms for decoding low-density parity-check (LDPC) codes are considered. The MF principle is well established in statistical physics and artificial intelligence. Instead of using a single completely factorized approximated distribution as in the MF approach, the mixed MF algorithm forms a weighted average of several MF distributions as an approximation of the true posterior probability distribution. The MF decoding algorithm for linear block codes is derived and shown to be an approximation of the a posteriori probability (APP) decoding algorithm. The MF approach is then developed in the context of iterative decoding and presented as an approximation of the popular belief propagation decoding method. These results are extended to iterative decoding with the MMF algorithm. Simulation results show that the MF and MMF decoding algorithms yield a good performance-complexity tradeoff, especially when employed for decoding LDPC codes based on finite geometries.

## Analysis of Low-Density Parity-Check Codes Based on EXIT Functions

- **Status**: ✅
- **Reason**: 바이너리 LDPC BP의 EXIT/Gaussian approximation 기반 임계값 예측 개선—코드설계/디코더 분석 기법 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1658236
- **Type**: journal
- **Published**: July 2006
- **Authors**: E. Sharon, A. Ashikhmin, S. Litsyn
- **PDF**: https://ieeexplore.ieee.org/document/1658236
- **Abstract**: We exploit extrinsic information tranfer functions of single parity-check and prepetition codes over the binay input additive white Gaussian noise (biAWGN) channel, for asymptotic performance analysis of belief propagation decoding of low-density parity-check codes. The approach is based on a Gaussian approximation (GA) of the density evolution algorithm using the mutual information measure. We show that our method allows more accurate prediction of the decoding threshold in the biAWGN channel than the earlier known GA methods.

## Kikuchi approximation method for joint decoding of LDPC codes and partial-response channels

- **Status**: ✅
- **Reason**: Kikuchi 근사/generalized BP — loopy BP보다 강력한 메시지패싱, 바이너리 LDPC 디코더로 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1658205
- **Type**: journal
- **Published**: July 2006
- **Authors**: P. Pakzad, V. Anantharam
- **PDF**: https://ieeexplore.ieee.org/document/1658205
- **Abstract**: In this letter, we apply the Kikuchi approximation method to the problem of joint decoding of a low-density parity-check code and a partial-response channel. The Kikuchi method is, in general, more powerful than the conventional loopy belief propagation (BP) algorithm, and can produce better approximations to an underlying inference problem. We will first review the Kikuchi approximation method and the generalized BP algorithm, which is an iterative message-passing algorithm based on this method. We will then report simulation results which show that the Kikuchi method outperforms the best conventional iterative method

## On LDPC codes over channels with memory

- **Status**: ✅
- **Reason**: 메모리 채널 LDPC factor graph+sum-product, 채널 노드 복잡도 감소 기법—메모리 채널 디코딩 기법 이식 검토 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1673087
- **Type**: journal
- **Published**: July 2006
- **Authors**: G. Colavolpe
- **PDF**: https://ieeexplore.ieee.org/document/1673087
- **Abstract**: The problem of detection and decoding of low-density parity-check (LDPC) codes transmitted over channels with memory is addressed. A new general method to build a factor graph which takes into account both the code constraints and the channel behavior is proposed and the a posteriori probabilities of the information symbols, necessary to implement maximum a posteriori (MAP) symbol detection, are derived by using the sum-product algorithm. With respect to the case of a LDPC code transmitted on a memoryless channel, the derived factor graphs have additional factor nodes taking into account the channel behavior and not the code constraints. It is shown that the function associated to the generic factor node modeling the channel is related to the basic branch metric used in the Viterbi algorithm when MAP sequence detection is applied or in the BCJR algorithm implementing MAP symbol detection. This fact suggests that all the previously proposed solutions for those algorithms can be systematically extended to LDPC codes and graph-based detection. When the sum-product algorithm works on the derived factor graphs, the most demanding computation is in general that performed at factor nodes modeling the channel. In fact, the complexity of the computation at these factor nodes is in general exponential in a suitably defined channel memory parameter. In these cases, a technique for complexity reduction is illustrated. In some particular cases of practical relevance, the above mentioned complexity becomes linear in the channel memory. This does not happen in the same cases when detection is performed by using the Viterbi algorithm or the BCJR algorithm, suggesting that the use of factor graphs and the sum-product algorithm might be computationally more appealing. As an example of application of the described framework, the cases of noncoherent and flat fading channels are considered

## Gear-shift decoding

- **Status**: ✅
- **Reason**: Gear-shift 디코딩 — iteration별 디코딩 규칙 전환으로 latency 최소화, 디코더+HW 파이프라인 기법 이식 가능(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1658218
- **Type**: journal
- **Published**: July 2006
- **Authors**: M. Ardakani, F.R. Kschischang
- **PDF**: https://ieeexplore.ieee.org/document/1658218
- **Abstract**: This paper considers a class of iterative message-passing decoders for low-density parity-check codes in which the decoder can choose its decoding rule from a set of decoding algorithms at each iteration. Each available decoding algorithm may have a different per-iteration computation time and performance. With an appropriate choice of algorithm at each iteration, overall decoding latency can be reduced significantly, compared with standard decoding methods. Such a decoder is called a gear-shift decoder because it changes its decoding rule (shifts gears) in order to guarantee both convergence and maximum decoding speed (minimum decoding latency). Using extrinsic information transfer charts, the problem of finding the optimum (minimum decoding latency) gear-shift decoder is formulated as a computationally tractable dynamic program. The optimum gear-shift decoder is proved to have a decoding threshold equal to or better than the best decoding threshold among those of the available algorithms. In addition to speeding up software decoder implementations, gear-shift decoding can be applied to optimize a pipelined hardware decoder, minimizing hardware cost for a given decoder throughput

## Generalized Construction of Quasi-Cyclic Regular LDPC Codes Based on Permutation Matrices

- **Status**: ✅
- **Reason**: 순열행렬 텐서곱 기반 QC-LDPC 신규 구성+4-cycle 제거 — 코드설계 기법(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4036049
- **Type**: conference
- **Published**: 9-14 July 
- **Authors**: Ernst Gabidulin, Abdi Moinian, Bahram Honary
- **PDF**: https://ieeexplore.ieee.org/document/4036049
- **Abstract**: A new approach is proposed for constructing regular low-density parity-check (LDPC) codes based on tensor product of matrices. In this paper, first a general construction method of regular LDPC codes exploiting permutation matrices is described. Constructed codes have a quasi-cyclic structure with no short cycles of length 4 in their Tanner graph, hence simple encoding while maintaining good performance is achieved. The paper also demonstrates a generalized design, which covers a large family of LDPC codes and number of other construction methods. The new generalized LDPC codes are defined by a small number of parameters and cover a large set of code lengths and rates. Using these codes, LDPC matrices of any column weight and row weight can be constructed. Performance of these codes under iterative decoding compares well with other well-structured as well as random LDPC codes

## A Combining Method of Structured LDPC Codes from Affine Permutation Matrices

- **Status**: ✅
- **Reason**: APM-LDPC 신규 QC 일반화 구성+girth 향상 결합법(CRT) — 바이너리 코드설계 기법(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4036048
- **Type**: conference
- **Published**: 9-14 July 
- **Authors**: Seho Myung, Kyeongcheol Yang, Dong Seek Park
- **PDF**: https://ieeexplore.ieee.org/document/4036048
- **Abstract**: In this paper we present a class of structured low-density parity-check (LDPC) codes from affine permutation matrices, called the APM-LDPC codes, which are a generalization of quasi-cyclic LDPC codes. We give a necessary and sufficient condition under which an APM-LDPC code has a cycle and introduce a simple method to construct APM-LDPC codes of large length by combining those of small length based on the Chinese Remainder Theorem. In particular, we show that the girth of APM-LDPC codes obtained in this method is always larger than or equal to those of given APM-LDPC codes.

## Ensemble Weight Enumerators for Protograph LDPC Codes

- **Status**: ✅
- **Reason**: Protograph LDPC 유한길이 weight enumerator, degree distribution과 최소거리 — 바이너리 LDPC 코드설계(E) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4036228
- **Type**: conference
- **Published**: 9-14 July 
- **Authors**: Dariush Divsalar
- **PDF**: https://ieeexplore.ieee.org/document/4036228
- **Abstract**: Recently, LDPC codes with projected graph, or protograph structures have been proposed. In this paper, finite length ensemble weight enumerators for LDPC codes with protograph structures are obtained. Asymptotic results are derived as the block size goes to infinity. In particular, we are interested in obtaining ensemble average weight enumerators for protograph LDPC codes which have typical minimum distance that grows linearly with block size. As with irregular ensembles, linear minimum distance property is sensitive to the proportion of degree-2 variable nodes. In this paper, the derived results on ensemble weight enumerators show that linear minimum distance condition on degree distribution of unstructured irregular LDPC codes is a sufficient but not a necessary condition for protograph LDPC codes

## Optimal Puncturing of Block-Type LDPC Codes and Their Fast Convergence Decoding

- **Status**: ✅
- **Reason**: B-LDPC 최적 천공+신규 고속수렴 디코딩 알고리즘 — 디코더 기법 이식 가능(C/E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4036079
- **Type**: conference
- **Published**: 9-14 July 
- **Authors**: Song-nam Hong, Hyeong-gun Joo, Dong-joon Shin
- **PDF**: https://ieeexplore.ieee.org/document/4036079
- **Abstract**: In this paper, we study and propose a puncturing algorithm of block-type low-density parity-check (B-LDPC) codes. This optimal puncturing algorithm is derived from the fact that puncturing of parity bits is equivalent to merging the check nodes. Furthermore, we propose a new decoding algorithm suitable for the punctured B-LDPC codes. This decoding algorithm needs not only smaller number of operations at each iteration, but also shows faster decoding convergence speed than the conventional erasure decoding algorithm. If the optimally punctured B-LDPC code is decoded by the new decoding algorithm, it results in the same performance as the unpunctured B-LDPC code of the same code rate.

## Construction of Protograph LDPC Codes with Linear Minimum Distance

- **Status**: ✅
- **Reason**: 선형 최소거리+낮은 임계값 protograph LDPC 구성법(체크분할/degree-2), FPGA 검증; 바이너리 코드설계 신규 기여(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4036046
- **Type**: conference
- **Published**: 9-14 July 
- **Authors**: Dariush Divsalar, Sam Dolinar, Christopher Jones
- **PDF**: https://ieeexplore.ieee.org/document/4036046
- **Abstract**: A construction method for protograph-based LDPC codes that simultaneously achieve low iterative decoding threshold and linear minimum distance is proposed. We start with a high-rate protograph LDPC code with variable node degrees of at least 3. Lower rate codes are obtained by splitting check nodes and connecting them by degree-2 nodes. This guarantees the linear minimum distance property for the lower-rate codes. Excluding checks connected to degree-1 nodes, we show that the number of degree-2 nodes should be at most one less than the number of checks for the protograph LDPC code to have linear minimum distance. Iterative decoding thresholds are obtained by using the reciprocal channel approximation. Thresholds are lowered by using either precoding or at least one very high-degree node in the base protograph. A family of high- to low-rate codes with minimum distance linearly increasing in block size and with capacity-approaching performance thresholds is presented. FPGA simulation results for a few example codes show that the proposed codes perform as predicted

## On the rank of LDPC matrices constructed by Vandermonde matrices and RS codes

- **Status**: ✅
- **Reason**: Vandermonde/RS 기반 LDPC 패리티검사 행렬 rank 계산 — 바이너리 확장체 LDPC 행렬 구성/rank 분석은 코드설계(E) 이식 가능, 애매하여 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4036086
- **Type**: conference
- **Published**: 9-14 July 
- **Authors**: Ernst M. Gabidulin, Martin Bossert
- **PDF**: https://ieeexplore.ieee.org/document/4036086
- **Abstract**: We calculate the rank of low-density parity-check (LDPC) matrices based on Vandermonde matrix like constructions. In the case of prime fields the rank is given exactly. We show that LDPC codes based on RS codes are a special case of the Vandermonde based construction, thus also for these LDPC matrix construction, the rank calculation is valid. However, for extension fields the calculation is more sophisticated because of the nilpotent property of the parity check matrix. Therefore we can give presently only a bound for the rank in case of binary extension fields

## Irregular Low-Density Parity-Check Convolutional Codes Based on Protographs

- **Status**: ✅
- **Reason**: 프로토그래프 기반 비정규 LDPC convolutional 코드 신규 구성(E) — 바이너리 코드설계 기법 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4036244
- **Type**: conference
- **Published**: 9-14 July 
- **Authors**: G. Richter, M. Kaupper, K. Sh. Zigangirov
- **PDF**: https://ieeexplore.ieee.org/document/4036244
- **Abstract**: Irregular low-density parity-check (LDPC) codes constructed from small protographs are one of the most powerful LDPC block codes. In this paper, we introduce the convolutional version of these codes. LDPC convolutional codes constructed from protographs have some advantages in comparison to LDPC block codes constructed from protographs, e.g., an effective pipeline decoding. We show that LDPC convolutional codes constructed from protographs have much lower error rates than analogous LDPC block codes with the same complexity and that they operate with low error rates near the Shannon limits even for a relatively small memory size

## Rate-Compatible Puncturing of Finite-Length Low-Density Parity-Check Codes

- **Status**: ✅
- **Reason**: 유한길이 LDPC rate-compatible puncturing 기법 + BEC/AWGN 성능 bound — 코드설계(E, 유한길이/구조) 바이너리 LDPC 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4036141
- **Type**: conference
- **Published**: 9-14 July 
- **Authors**: N. Vellambi, R. Badri, Faramarz Fekri
- **PDF**: https://ieeexplore.ieee.org/document/4036141
- **Abstract**: In this paper, we study rate-compatible puncturing of finite-length Low-Density Parity-Check (LDPC) codes. First, we derive simple and yet good bounds on the expected performance of punctured codes (constructed by random puncturing) over Binary Erasure Channel (BEC) as a function of the performance of their parent LDPC code. We then present a novel rate-compatible puncturing scheme that is very easy to implement. Our scheme uses the idea that a more uniform distribution of punctured bits across the Tanner graph results in punctured codes with better performance. Although the puncturing scheme tailored to regular codes is presented, it is also directly applicable to irregular parent ensembles. By simulations, the proposed rate-compatible puncturing scheme is shown to be superior to the existing puncturing methods for both regular and irregular LDPC codes over BEC and Additive White Gaussian Noise (AWGN) Channel.

## On the minimum distance of structured LDPC codes with two variable nodes of degree 2 per parity-check equation

- **Status**: ✅
- **Reason**: degree-2 변수노드 구조 LDPC 최소거리 분석 — 바이너리 LDPC 코드설계(E) error floor 관련 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4036227
- **Type**: conference
- **Published**: 9-14 July 
- **Authors**: Jean-pierre Tillich, Gilles Zemor
- **PDF**: https://ieeexplore.ieee.org/document/4036227
- **Abstract**: We investigate the minimum distance of structured LDPC codes with two variable nodes of degree 2 per parity-check equation and show that their minimum distance is a sub-linear power function of the code length

## Design of Rate-Compatible Irregular LDPC Codes for Incremental Redundancy Hybrid ARQ Systems

- **Status**: ✅
- **Reason**: 유한블록 irregular LDPC rate-compatible puncturing 구성 — 코드설계(E) 바이너리 LDPC 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4036143
- **Type**: conference
- **Published**: 9-14 July 
- **Authors**: Jaehong Kim, Woonhaing Hur, Aditya Ramamoorthy +1
- **PDF**: https://ieeexplore.ieee.org/document/4036143
- **Abstract**: We present a new class of irregular low-density parity-check (LDPC) codes for finite block length (up to a few thousand symbols). The proposed codes are efficiently encodable and have a simple rate-compatible puncturing structure which is suitable for incremental redundancy hybrid automatic repeat request (IR-HARQ) systems. The codes outperform optimized irregular LDPC codes and (extended) irregular repeat-accumulate codes for rates 0.67-0.94, and are particularly good at high puncturing rates where good puncturing performance has been previously difficult to achieve. These characteristics result in good throughput performance over time-varying channels in IR-HARQ systems

## Turbo-like Decoding Algorithm for Structured LDPC codes

- **Status**: ✅
- **Reason**: 구조화 LDPC의 turbo-like 디코딩 알고리즘+병렬 고속 디코더 구현(C/D) — 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4036259
- **Type**: conference
- **Published**: 9-14 July 
- **Authors**: Ajit Nimbalker, Yufei Blankenship, Brian Classon
- **PDF**: https://ieeexplore.ieee.org/document/4036259
- **Abstract**: This paper presents a high-speed "turbo-like" decoding algorithm for certain structured LDPC codes such as those adopted in IEEE 802.16e and in the draft 802.11n standards. It is shown that after a key modification, such LDPC codes may be processed as generalized repeat accumulate codes, codes which are known to support "turbo-like" decoding. A GRA-like encoder of structured LDPC codes is derived, which in turn leads to the decoding algorithm. It is also shown that the "structured" properties result in an inherent parallelism, leading to an efficient high speed decoder implementation

## H-ARQ Rate-Compatible Structured LDPC Codes

- **Status**: ✅
- **Reason**: Protograph 기반 rate-compatible 구조적 LDPC 구성·puncturing 알고리즘 — 코드설계(E) 바이너리 LDPC 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4036142
- **Type**: conference
- **Published**: 9-14 July 
- **Authors**: Mostafa El-Khamy, Jilei Hou, Naga Bhushan
- **PDF**: https://ieeexplore.ieee.org/document/4036142
- **Abstract**: In this paper, we design families of rate-compatible structured LDPC codes suitable for hybrid ARQ applications with high throughput. We devise a systematic technique of low complexity for the design of structured low-rate LDPC codes from higher rate ones. These codes have a good performance on the AWGN channel and are robust against erasures and puncturing. The codes designed here are protograph-based codes and have fast encoding and decoding structures. These low rate codes are used as the parent codes of rate-compatible families. Then, we propose a number of algorithms for puncturing the codes in a rate compatible manner to construct codes of higher rates. The two most promising ones are the random puncturing search technique and progressive node puncturing. We show that using the techniques in this paper one could construct a high throughput rate compatible family with codes whose rates are in the range from 0.1 to 0.9 and which are within 1 dB from the channel capacity and have good error floors

## Burst-Correction Decoding of Cyclic LDPC Codes

- **Status**: ✅
- **Reason**: cyclic LDPC의 sparse circulant 패리티검사 기반 burst-correction 디코딩 신규 기법(C/E) — 바이너리 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4036261
- **Type**: conference
- **Published**: 9-14 July 
- **Authors**: Shumei Song, Shu Lin, Khaled Abdel-Ghaffar
- **PDF**: https://ieeexplore.ieee.org/document/4036261
- **Abstract**: LDPC codes have excellent performance when iteratively decoded based on sparse parity-check matrices over both the AWGN channel and the erasure channel. In this paper, we propose a simple burst-correction decoding scheme for cyclic LDPC codes based on the same sparse circulant parity-check matrices used to perform iterative decoding. Although the proposed scheme may not achieve the full burst-correcting capability of the codes, it is rather simple and fast. We also show that the full burst-correcting capabilities of some codes constructed from Euclidean and projective geometries are very close to the Reiger upper bound

## Doubly Generalized LDPC Codes

- **Status**: ✅
- **Reason**: GLDPC(doubly generalized) 신규 코드설계, EXIT 최적화 — 바이너리 LDPC 구성 기법 이식 가능(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4036047
- **Type**: conference
- **Published**: 9-14 July 
- **Authors**: Yige Wang, Marc Fossorier
- **PDF**: https://ieeexplore.ieee.org/document/4036047
- **Abstract**: The design of generalized low-density parity-check (GLDPC) codes at both check and bit nodes over AWGN channel is considered in this paper. The new codes are referred to as doubly generalized LDPC codes. EXIT charts are used to optimize the parameters of these codes. Both analysis and simulations show that this method can provide more flexibility in constructing codes with good threshold

## A Method for Constructing LDPC Codes with Low Error Floor

- **Status**: ✅
- **Reason**: PEG 변형으로 error floor 낮추는 신규 코드 설계(E), 바이너리 LDPC에 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4036436
- **Type**: conference
- **Published**: 9-14 July 
- **Authors**: Eran Sharon, Simon Litsyn
- **PDF**: https://ieeexplore.ieee.org/document/4036436
- **Abstract**: This paper describes a novel progressive edge growth (PEG) algorithm for constructing LDPC codes with minimized block error probability over the binary erasure channel (BEC). The constructed codes provide superior performance and lower error floor compared to codes generated by previously known algorithms. Furthermore, an upper bound on the expected block error probability in the error floor region of the generated code is derived

## Instanton analysis of Low-Density Parity-Check codes in the error-floor regime

- **Status**: ✅
- **Reason**: error-floor 영역 LDPC 성능 정량분석 instanton 기법; 정규 바이너리 LDPC error floor 평가 도구로 이식 가능(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4036023
- **Type**: conference
- **Published**: 9-14 July 
- **Authors**: Mikhail Stepanov, Michael Chertkov
- **PDF**: https://ieeexplore.ieee.org/document/4036023
- **Abstract**: In this paper we develop instanton method introduced in V. Chernyak et al. (2004), M.G. Stepanov et al. (2005) to analyze quantitatively performance of low-density parity-check (LDPC) codes decoded iteratively in the so-called error-floor regime. We discuss statistical properties of the numerical instanton-amoeba scheme focusing on detailed analysis and comparison of two regular LDPC codes: Tanner's [155,64,20] and Margulis' [672,336,16] codes. In the regime of moderate values of the signal-to-noise ratio we critically compare results of the instanton-amoeba evaluations against the standard Monte Carlo calculations of the frame-error-rate

## Approximately Lower Triangular Ensembles of LPDC Codes with Linear Encoding Complexity

- **Status**: ✅
- **Reason**: 근사 하삼각 앙상블로 선형시간 인코딩 — 바이너리 LDPC 인코딩 구성 기법(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4036078
- **Type**: conference
- **Published**: 9-14 July 
- **Authors**: Shay Freundlich, David Burshtein, Simon Litsyn
- **PDF**: https://ieeexplore.ieee.org/document/4036078
- **Abstract**: The complexity of brute force encoding of LDPC codes is proportional to the square value of the block length. Richardson and Urbanke have proposed efficient encoding algorithms for LDPC codes. These algorithms permute the parity check matrix of the code iteratively, such that it becomes approximately lower triangular. We propose a new approach for efficient encoding of LDPC codes in which we modify the code ensemble to force an approximate lower triangular structure, thus eliminating the need to apply the algorithms of Richardson and Urbanke. We prove that the new ensemble has the same asymptotic threshold as the corresponding standard ensemble. The new ensemble can be used for linear time encoding of an arbitrary code profile. Computer simulations confirm that the performances of the standard and new ensembles are also very similar when using finite length codes

## Optimized Asymptotic Puncturing Distributions for Different LDPC Code Constructions

- **Status**: ✅
- **Reason**: 구성별 천공분포 최적화(밀도진화 확장) — 바이너리 LDPC 코드설계 기법(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4036080
- **Type**: conference
- **Published**: 9-14 July 
- **Authors**: G. Richter, S. Stiglmayr, M. Bossert
- **PDF**: https://ieeexplore.ieee.org/document/4036080
- **Abstract**: In this paper, we describe a method, how to optimize the asymptotic puncturing distributions for low-density parity-check codes constructed with different algorithms. Therefore, we generalize the discretized density evolution such that we can take care of the structure of the code. We show by density evolution and by simulations that even for the same degree distributions the optimized asymptotic puncturing distributions vary considerably for different construction algorithms. Furthermore, we demonstrate the performance gain by using the designed puncturing distributions compared to known puncturing distributions

## Design of Rate-Compatible IRA Codes for Capacity-Approaching with Hybrid ARQ

- **Status**: ✅
- **Reason**: IRA(LDPC 서브클래스) rate-compatible 설계: puncturing/extending + density evolution. 이식 가능한 바이너리 LDPC 코드설계 기법(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4036500
- **Type**: conference
- **Published**: 9-14 July 
- **Authors**: Guosen Yue, Xiaodong Wang, Mohammad Madihian
- **PDF**: https://ieeexplore.ieee.org/document/4036500
- **Abstract**: We consider the design of efficient rate-compatible (RC) irregular repeat accumulate (IRA) codes, a subclass of LDPC codes, over a wide code rate range. The goal is to provide a family of RC codes to achieve high throughput in hybrid automatic repeat request (ARQ) scheme for high-speed data packet wireless systems. We focus on a hybrid design method which employs both puncturing and extending. We propose a simple puncturing method based on minimizing the maximal recoverable step of the punctured nodes and a new extending scheme by introducing the degree-1 parity bits for the lower rate codes and obtaining the optimal proportions of extended nodes through density evolution analysis. Simulation results show that our designed RC codes offer good error correction performance over a wide rate range and provide high throughput, especially in the high and low SNR regions

## Which Codes Have 4-Cycle-Free Tanner Graphs?

- **Status**: ✅
- **Reason**: 4-cycle-free Tanner 그래프 존재 조건 — 사이클 제거(girth) 코드설계 기법(E)으로 바이너리 LDPC에 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4036088
- **Type**: conference
- **Published**: 9-14 July 
- **Authors**: Thomas R. Halford, Keith M. Chugg, Alex J. Grant
- **PDF**: https://ieeexplore.ieee.org/document/4036088
- **Abstract**: Let C be an [n, k, d] binary linear code with rate R = k/n and dual Cperp. In this correspondence, it is shown that C can be represented by a 4-cycle-free Tanner graph only if: pdperp  les lfloorradicnp(p-1)+n2/4+n/2rfloor where p = n - k and dperp is the minimum distance of Cperp . By applying this result, it is shown that 4-cycle-free Tanner graphs do not exist for many classical binary linear block codes

## A Compact Construction for LDPC Codes using Permutation Polynomials

- **Status**: ✅
- **Reason**: permutation polynomial 기반 QC-LDPC 신규 구성(girth 12 달성, 최소거리 상한) = E 바이너리 코드설계 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4035925
- **Type**: conference
- **Published**: 9-14 July 
- **Authors**: Oscar Y. Takeshita
- **PDF**: https://ieeexplore.ieee.org/document/4035925
- **Abstract**: A construction is proposed for low density parity check codes using quadratic permutation polynomials over finite integer rings. Graph isomorphisms and automorphisms are identified and used in an efficient search for good codes. Graphs with girth as large as 12 were found. Upper bounds on the minimum Hamming distance are found algorithmically. The bounds indicate that the minimum distance grows with block length. One of the new codes has a similar error performance as the best known PEG LDPC code. Finally, the new codes are quasi-cyclic

## Random Redundant Soft-In Soft-Out Decoding of Linear Block Codes

- **Status**: ✅
- **Reason**: redundant Tanner graph 기반 random redundant SISO 반복 디코딩(C) — 바이너리 LDPC BP에 이식 가능한 디코더 기법
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4036366
- **Type**: conference
- **Published**: 9-14 July 
- **Authors**: Thomas R. Halford, Keith M. Chugg
- **PDF**: https://ieeexplore.ieee.org/document/4036366
- **Abstract**: A number of authors have recently considered iterative soft-in soft-out (SISO) decoding algorithms for classical linear block codes that utilize redundant Tanner graphs. Jiang and Narayanan presented a practically realizable algorithm that applies only to cyclic codes while Kothiyal et al. presented an algorithm that, while applicable to arbitrary linear block codes, does not imply a low-complexity implementation. This work first presents the aforementioned algorithms in a common framework and then presents a related algorithm - random redundant iterative decoding - that is both practically realizable and applicable to arbitrary linear block codes. Simulation results illustrate the successful application of the random redundant iterative decoding algorithm to the extended binary Golay code. Additionally, the proposed algorithm is shown to outperform Jiang and Narayanan's algorithm for a number of Bose-Chaudhuri-Hocquenghem (BCH) codes

## Pseudo-Codewords in LDPC Convolutional Codes

- **Status**: ✅
- **Reason**: LDPC convolutional codes를 QC-LDPC에서 unwrap, pseudo-codeword/free pseudo-weight 분석 — 바이너리 LDPC 코드설계(E) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4036189
- **Type**: conference
- **Published**: 9-14 July 
- **Authors**: Roxana Smarandache, Ali Emre Pusane, Pascal O. Vontobel +1
- **PDF**: https://ieeexplore.ieee.org/document/4036189
- **Abstract**: Iterative message-passing decoders for low-density parity-check (LDPC) block codes are known to be subject to decoding failures due to so-called pseudo-codewords. These failures can cause the large signal-to-noise ratio performance of message-passing decoding to be worse than that predicted by the maximum-likelihood decoding union bound. In this paper we study the pseudo-codeword problem for the class of LDPC convolutional codes decoded continuously using an iterative, sliding window, message-passing decoder. In particular, for an LDPC convolutional code derived by unwrapping a quasi-cyclic LDPC block code, we show that the free pseudo-weight of the convolutional code is at least as large as the minimum pseudo-weight of the underlying quasi-cyclic code. This result parallels the well-known relationship between the free Hamming distance of convolutional codes and the minimum Hamming distance of their quasi-cyclic counterparts. Finally, simulation results are included that show improved performance for unwrapped LDPC convolutional codes compared to their underlying quasi-cyclic codes

## Analysis of One Step Majority Logic Decoders Constructed From Faulty Gates

- **Status**: ✅
- **Reason**: 불완전 게이트로 구성된 1단 다수결 디코더 성능 분석; girth>=6 정규 LDPC 적용 가능한 디코더/HW 신뢰성 기법(E/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4036005
- **Type**: conference
- **Published**: 9-14 July 
- **Authors**: Shashi Kiran Chilappagari, Milos Ivkovic, Bane Vasic
- **PDF**: https://ieeexplore.ieee.org/document/4036005
- **Abstract**: In this paper we propose an analytical method to evaluate the performance of one step majority logic decoders constructed from faulty gates. We analyze the decoder under the assumption that the gates fail independently. We calculate the average bit error probability of such a decoder and apply the method to the special case of projective geometry codes. The method, however, applies to any regular low-density parity-check code of girth at least six but the calculations are much simpler for the projective geometry codes. We present results for the bit error rate performance of four codes from projective planes

## Guessing Facets: Polytope Structure and Improved LP Decoder

- **Status**: ✅
- **Reason**: 바이너리 LDPC LP 디코딩 polytope 구조 분석으로 LP 디코더 능가하는 새 디코딩 알고리즘 제시 — 이식 가능 디코더(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4036190
- **Type**: conference
- **Published**: 9-14 July 
- **Authors**: Alexandros G. Dimakis, Martin J. Wainwright
- **PDF**: https://ieeexplore.ieee.org/document/4036190
- **Abstract**: A new approach for decoding binary linear codes by solving a linear program (LP) over a relaxed codeword polytope was recently proposed by Feldman et al. In this paper we investigate the structure of the polytope used in the LP relaxation decoding. We begin by showing that for expander codes, every fractional pseudocodeword always has at least a constant fraction of non-integral bits. We then prove that for expander codes, the active set of any fractional pseudocodeword is smaller by a constant fraction than the active set of any codeword. We exploit this fact to devise a decoding algorithm that provably outperforms the LP decoder for finite blocklengths. It proceeds by guessing facets of the polytope, and resolving the linear program on these facets. While the LP decoder succeeds only if the ML codeword has the highest likelihood over all pseudocodewords, we prove that for expander codes the proposed algorithm succeeds even with a constant number of pseudocodewords of higher likelihood. Moreover, the complexity of the proposed algorithm is only a constant factor larger than that of the LP decoder

## Complexity-Optimized Irregular Decoders

- **Status**: ✅
- **Reason**: irregular soft decoder 알고리즘과 복잡도 최소화 공동 최적화 — 디코더 복잡도 절감 기법(C) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4036399
- **Type**: conference
- **Published**: 9-14 July 
- **Authors**: Masoud Ardakani, Pirouz Zarrinkhat, Raman Yazdani
- **PDF**: https://ieeexplore.ieee.org/document/4036399
- **Abstract**: Irregular decoding of low-density parity-check codes, i.e., using different algorithms in one iteration of the decoding of a single word, is studied. We formulate density evolution for irregular decoders. Using a one-dimensional representation of density evolution, we then jointly optimize irregular codes and irregular soft decoders for minimizing the decoding complexity. More specifically, for a given set of soft algorithms, a given channel, and a given code-rate, we find an irregular code-decoder pair which is capable of achieving a desired error performance with minimal decoding complexity. Robustness of irregular decoders when there exist channel estimation errors is also shown via an example

## An Efficient Girth-Locating Algorithm for Quasi-Cyclic LDPC Codes

- **Status**: ✅
- **Reason**: QC-LDPC 효율적 girth 탐색 알고리즘으로 large-girth 코드 생성 — 코드설계 기법(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4036077
- **Type**: conference
- **Published**: 9-14 July 
- **Authors**: Xiaofu Wu, Xiaohu You, Chunming Zhao
- **PDF**: https://ieeexplore.ieee.org/document/4036077
- **Abstract**: The parity-check matrix of a quasi-cyclic code can be represented by a polynomial parity-check matrix with a significantly lower dimension. By using this compact representation, we can develop an efficient method for locating the girth of the quasi-cyclic code. The proposed girth-locating algorithm can be well employed to generate quasi-cyclic low-density parity-check codes with large girth

## Block code reconstruction using iterative decoding techniques

- **Status**: ✅
- **Reason**: 가중 패리티검사 Gallager 변형 알고리즘으로 코드 복원 — 부호 비의존 BP 변형(C) 이식 검토 여지
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4036374
- **Type**: conference
- **Published**: 9-14 July 
- **Authors**: Mathieu Cluzeau
- **PDF**: https://ieeexplore.ieee.org/document/4036374
- **Abstract**: In this paper, we present a new algorithm for recovering a linear block code from noisy codewords. To achieve this, we introduce a version of Gallager algorithm with weighted parity-check equations. This new algorithm efficiently recovers LDPC codes and can also be used for other block codes

## A low-complexity stopping criterion for the decoder of parallel concatenated LDPC codes

- **Status**: ✅
- **Reason**: 병렬연접 LDPC 반복디코더용 신규 저복잡도 정지기준(MEM), 부호비의존 BP 디코더 기법으로 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4124215
- **Type**: conference
- **Published**: 29-31 July
- **Authors**: Xu Xiaojian, Li Jin, Hu Hanying
- **PDF**: https://ieeexplore.ieee.org/document/4124215
- **Abstract**: In this paper, we propose a novel stopping criteria that based on the mean of the magnitude of the extrinsic information in the iterative decoder of parallel concatenated LDPC (low- density parity-check) codes. The proposed criterion has low computation complexity and few storage requirements. Simulations results proved that the MEM (mean of extrinsic information magnitude) rules outperforms the other existing criterions in terms of BER and average number of super iterations.
