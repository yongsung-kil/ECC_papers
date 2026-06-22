# IEEE Xplore — 2005-09 (1차선별 통과)


## A combining method of quasi-cyclic LDPC codes by the Chinese remainder theorem

- **Status**: ✅
- **Reason**: CRT로 QC-LDPC 결합 구성하는 신규 코드설계 기법, girth 보장·4-cycle 제거(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1506715
- **Type**: journal
- **Published**: Sept. 2005
- **Authors**: Seho Myung, Kyeongcheol Yang
- **PDF**: https://ieeexplore.ieee.org/document/1506715
- **Abstract**: In this paper we propose a method of constructing quasi-cyclic low-density parity-check (QC-LDPC) codes of large length by combining QC-LDPC codes of small length as their component codes, via the Chinese remainder theorem. The girth of the QC-LDPC codes obtained by the proposed method is always larger than or equal to that of each component code. By applying the method to array codes, we present a family of high-rate regular QC-LDPC codes with no 4-cycles. Simulation results show that they have almost the same performance as random regular LDPC codes.

## An improvement on the modified weighted bit flipping decoding algorithm for LDPC codes

- **Status**: ✅
- **Reason**: WBF 디코더 개선(플리핑 기준·신뢰도 계산 개선)으로 바이너리 LDPC 디코더 알고리즘(C)에 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1506712
- **Type**: journal
- **Published**: Sept. 2005
- **Authors**: Ming Jiang, Chunming Zhao, Zhihua Shi +1
- **PDF**: https://ieeexplore.ieee.org/document/1506712
- **Abstract**: We present a major improvement to the modified weighted bit flipping (MWBF) decoding algorithm for low density parity-check (LDPC) codes. We improve the flipping criterion by introducing a more efficient method for computing the reliability of the parity checks. We derive an approximate theoretical expression for the weighting factor and demonstrate its consistency with simulation results. The improved MWBF algorithm achieves a noticeable gain over the MWBF algorithm with only a modest increase in computational complexity.

## Iterative decoding of linear block codes: a parity-check orthogonalization approach

- **Status**: ✅
- **Reason**: 임의 선형부호를 4-cycle-free 직교 패리티검사로 변환→BEC/AWGN BP 성능 개선 — 부호 비의존 사이클 제거 기법, 바이너리 LDPC BP 이식 가능(C/E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1499067
- **Type**: journal
- **Published**: Sept. 2005
- **Authors**: S. Sankaranarayanan, B. Vasic
- **PDF**: https://ieeexplore.ieee.org/document/1499067
- **Abstract**: It is widely accepted that short cycles in Tanner graphs deteriorate the performance of message-passing algorithms. This discourages the use of these algorithms on Tanner graphs (TGs) of well-known algebraic codes such as Hamming codes, Bose-Chaudhuri-Hocquenghem codes, and Reed-Solomon codes. Yedidia et al. presented a method to generate code representations suitable for message-passing algorithms. This method does not guarantee a representation free of four-cycles. In this correspondence, we present an algorithm to convert an arbitrary linear block into a code with orthogonal parity-check equations. A combinatorial argument is used to prove that the algorithm guarantees a four-cycle free representation for any linear code. The effects of removing four-cycles on the performance of a belief propagation decoder for the binary erasure channel are studied in detail by analyzing the structures in different representations. Finally, we present bit-error rate (BER) and block-error rate (BLER) performance curves of linear block codes under belief propagation algorithms for the binary erasure channel and the additive white Gaussian noise (AWGN) channel in order to demonstrate the improvement in performance achieved with the help of the proposed algorithm.

## An analysis of the orthogonality structures of convolutional codes for iterative decoding

- **Status**: ✅
- **Reason**: self-doubly-orthogonal code의 6/8-cycle 최소화로 BP 수렴/성능 개선 — 사이클 제거 코드설계 기법, 바이너리 BP에 이식 가능(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1499055
- **Type**: journal
- **Published**: Sept. 2005
- **Authors**: Yu-Cheng He, D. Haccoun
- **PDF**: https://ieeexplore.ieee.org/document/1499055
- **Abstract**: The structures of convolutional self-orthogonal codes and convolutional self-doubly-orthogonal codes for both belief propagation and threshold iterative decoding algorithms are analyzed on the basis of difference sets and computation tree. It is shown that the double orthogonality property of convolutional self-doubly-orthogonal codes improves the code structure by maximizing the number of independent observations over two successive decoding iterations while minimizing the number of cycles of lengths 6 and 8 on the code graphs. Thus, the double orthogonality may improve the iterative decoding in both convergence speed and error performance. In addition, the double orthogonality makes the computation tree rigorously balanced. This allows the determination of the best weighing technique, so that the error performance of the iterative threshold decoding algorithm approaches that of the iterative belief propagation decoding algorithm, but at a substantial reduction of the implementation complexity.

## Performance Evaluation of A Modified Sum-Product Decoding Algorithm for LDPC Codes

- **Status**: ✅
- **Reason**: 수정 tanh SPA·양자화/piecewise 근사로 error floor 저감, 이식 가능 디코더 변형(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1547819
- **Type**: conference
- **Published**: 5-7 Sept. 
- **Authors**: S. Papaharalabos, P. Sweeney, B.G. Evans +3
- **PDF**: https://ieeexplore.ieee.org/document/1547819
- **Abstract**: We propose a modified hyperbolic tangent (tanh) function that is used in the sum-product algorithm (SPA). This is done in order to approximate the infinite argument of the tanh function, when decoding low-density parity-check (LDPC) codes. As shown by computer simulation results, the proposed modification has a significant impact on the error floor reduction of the code and to the coding gain improvement with respect to the SPA with no modification. Computer simulation results with approximations using both piecewise linear function and coarse quantization are also presented

## Hardware Aware eIRA LDPC Code Generation

- **Status**: ✅
- **Reason**: eIRA LDPC 코드 생성 HW-aware 방법론, 4-cycle 제거·error floor 저감(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1547738
- **Type**: conference
- **Published**: 5-7 Sept. 
- **Authors**: J.M. Perez, V. Fernandez
- **PDF**: https://ieeexplore.ieee.org/document/1547738
- **Abstract**: This paper presents a new methodology for generating eIRA LDPC codes with low hardware cost. Approach is based on hierarchical matrices and primitive generators. Apart from implementation considerations, proposed method shows good BER performance due to a pseudo-random construction and the absence of length-four cycles. Moreover, low-weight codewords and near-codewords are also considered in order to reduce error floors

## Constructions of quasi-cyclic LDPC codes for the AWGN and binary erasure channels based on finite fields and affine mappings

- **Status**: ✅
- **Reason**: 유한체·affine mapping 기반 QC-LDPC 신규 대수적 구성, error-floor 개선 — 이식 가능 코드설계(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1523755
- **Type**: conference
- **Published**: 4-9 Sept. 
- **Authors**: L. Lan, L.-Q. Zeng, Y.Y. Tai +2
- **PDF**: https://ieeexplore.ieee.org/document/1523755
- **Abstract**: This paper presents two algebraic methods for constructing efficiently encodable quasi-cyclic (QC) LDPC codes that perform well on both the AWGN and binary erasure channels with iterative decoding in terms of bit-error performance, block error performance and error-floor, collectively. The constructions are based on the cyclic subgroups of the multiplicative groups of finite fields and affine mappings

## Extension of quasi-cyclic LDPC codes by lifting

- **Status**: ✅
- **Reason**: QC-LDPC lifting 확장 기법과 girth 상한 분석, 메모리 효율 — 코드설계(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1523759
- **Type**: conference
- **Published**: 4-9 Sept. 
- **Authors**: Seho Myung, Kyeongcheol Yang
- **PDF**: https://ieeexplore.ieee.org/document/1523759
- **Abstract**: In this paper, we analyze some cycle properties of quasi-cyclic low-density parity-check (QC-LDPC) codes and show that the girth of a QC-LDPC code is upper bounded by a certain number introduced by the structure of its mother matrix. We also propose a simple method to extend QC-LDPC codes of large length by lifting QC-LDPC codes of smaller length. In particular, it is possible to generate them from a single exponent matrix by a proper modulo-operation. Simulation results show that the more we apply the lifting to QC-LDPC codes, the more memory efficiency becomes better, but it may induce a little performance degradation

## Improved min-sum decoding algorithms for irregular LDPC codes

- **Status**: ✅
- **Reason**: irregular LDPC용 normalized/offset min-sum 개선(degree-2 노드 처리) - min-sum 변형 디코더(C), NAND 표준
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1523374
- **Type**: conference
- **Published**: 4-9 Sept. 
- **Authors**: Jinghu Chen, R.M. Tanner, C. Jones +1
- **PDF**: https://ieeexplore.ieee.org/document/1523374
- **Abstract**: In this paper, we apply two improved min-sum algorithms, the normalized and offset min-sum algorithms, to the decoding of irregular LDPC codes. We show that the behavior of the two algorithms in decoding irregular LDPC codes is different from that in decoding regular LDPC codes, due to the existence of bit nodes of degree two. We analyze and give explanations to the difference, and propose approaches to improve the performance of the two algorithms.

## Girth analysis of Tanner's (3, 5) QC LDPC codes

- **Status**: ✅
- **Reason**: Tanner (3,5) QC-LDPC girth 분석·사이클 존재조건 도출, 바이너리 QC 코드 설계(E) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1523621
- **Type**: conference
- **Published**: 4-9 Sept. 
- **Authors**: Sunghwan Kim, Jong-Seon No, Habong Chung +1
- **PDF**: https://ieeexplore.ieee.org/document/1523621
- **Abstract**: In this paper, the cycles of Tanner's (3,5) quasicyclic (QC) low-density parity-check (LDPC) codes are analyzed and their girth values are derived. The conditions for the existence of cycles of lengths 4, 6, 8, and 10 in Tanner's (3,5) QC LDPC codes of length 5p are expressed in terms of polynomial equations in a 15-th root of unity of the prime field Fp. By checking the existence of solutions for these equations over Fp, the girths of Tanner's (3,5) QC LDPC codes are derived

## An algebraic method for constructing efficiently encodable irregular LDPC codes

- **Status**: ✅
- **Reason**: 효율적 인코딩 가능한 불규칙 LDPC 대수적 구성(보장된 최소거리) — 신규 바이너리 LDPC 코드 설계(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1523458
- **Type**: conference
- **Published**: 4-9 Sept. 
- **Authors**: H. Fujita, M. Ohata, K. Sakaniwa
- **PDF**: https://ieeexplore.ieee.org/document/1523458
- **Abstract**: In this paper we propose an algebraic construction of efficiently encodable irregular LDPC codes. The proposed irregular LDPC codes have not only an efficient encoding algorithm but also guaranteed minimum distances. Simulation results show that the proposed codes perform well compared to randomly constructed irregular LDPC codes

## Terminated LDPC convolutional codes with thresholds close to capacity

- **Status**: ✅
- **Reason**: Terminated LDPC convolutional(SC-LDPC) 코드 구성과 density evolution threshold 분석; 신규 SC-LDPC 설계(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1523567
- **Type**: conference
- **Published**: 4-9 Sept. 
- **Authors**: M. Lentmaier, A. Sridharan, K.Sh. Zigangirov +1
- **PDF**: https://ieeexplore.ieee.org/document/1523567
- **Abstract**: An ensemble of LDPC convolutional codes with parity-check matrices composed of permutation matrices is considered. The convergence of the iterative belief propagation based decoder for terminated convolutional codes in the ensemble is analyzed for binary-input output-symmetric memoryless channels using density evolution techniques. We observe that the structured irregularity in the Tanner graph of the codes leads to significantly better thresholds when compared to corresponding LDPC block codes

## Near perfect decoding of LDPC codes

- **Status**: ✅
- **Reason**: cooperative optimization 기반 새 LDPC 디코더, sum-product 대비 error floor 1차수↓·저복잡도 - 이식 가능 디코더(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1523343
- **Type**: conference
- **Published**: 4-9 Sept. 
- **Authors**: Xiaofei Huang
- **PDF**: https://ieeexplore.ieee.org/document/1523343
- **Abstract**: Cooperative optimization is a new way for finding global optima of complicated functions of many variables. It has some important properties not possessed by any conventional optimization methods. It has been successfully applied in solving many large scale optimization problems in image processing, computer vision, and computational chemistry. This paper shows the application of this optimization principle in decoding LDPC codes, which is another hard combinatorial optimization problem. The cooperative optimization algorithm is much simpler in computation than the classical sum-product algorithm. Compared to the sum-product algorithm, our algorithm lowered the error floor more than one order of magnitude in decoding an experimental LDPC code for China's HDTV

## High-rate quasi-cyclic low-density parity-check codes derived from finite affine planes

- **Status**: ✅
- **Reason**: finite affine plane 기반 고율 QC-LDPC 신규 구성, error-floor 예측 — 바이너리 코드설계(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1523757
- **Type**: conference
- **Published**: 4-9 Sept. 
- **Authors**: N. Kamiya
- **PDF**: https://ieeexplore.ieee.org/document/1523757
- **Abstract**: This paper shows that several attractive classes of quasi-cyclic (QC) low-density parity-check (LDPC) codes can be obtained from affine planes over finite fields. One class of these consists of duals of one-generator QC codes. Here, for codes contained in this class, the exact minimum-distance and a lower bound on the multiplicity of the minimum-weight codewords are presented. It is shown that the lower bound on the multiplicity provides a very accurate indication of the bit error performance at moderate and high signal-to-noise ratios, and thus error-floor behavior can be easily predicted. Also discussed is a class consisting of codes from circulant permutation matrices. An explicit formula for the rank of the parity-check matrix is presented for these codes. Furthermore, it is shown that each of these codes can be identified as a code constructed from a constacyclic maximum distance separable (MDS) code in a similar manner to the RS-based LDPC codes presented by Chen et al. and Djurdjevic et al. Experimental results show that a number of high rate QC-LDPC codes with excellent error performance are contained in these classes

## Design of irregular concatenated zigzag codes

- **Status**: ✅
- **Reason**: ICZZ를 선형시간 인코딩 가능한 irregular LDPC 특수 사례로 구성하는 신규 코드 설계(E), 바이너리 BP 적용
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1523565
- **Type**: conference
- **Published**: 4-9 Sept. 
- **Authors**: Song-Nam Hong, Dong-Joon Shin
- **PDF**: https://ieeexplore.ieee.org/document/1523565
- **Abstract**: Capacity-approaching codes using iterative decoding have been the main research subject of coding area during past decade. In this paper, a new channel coding scheme called irregular concatenated zigzag (ICZZ) code is proposed. ICZZ codes can be viewed as a special case of irregular low-density parity-check (LDPC) codes with linear-time encodable structure. They are different from concatenated zigzag (CZZ) codes in the sense that the number of information bits entering into each zigzag encoder can be different and different zigzag codes can be used as component codes. A simple method to design ICZZ codes is proposed and by using an example, it is shown that ICZZ code of rate 1/3 has better performance than the optimal CZZ code and turbo code adopted in 3GPP

## Low-rate LDPC codes with simple protograph structure

- **Status**: ✅
- **Reason**: 프로토그래프 기반 저율 LDPC 구성+고속 디코더 구현 가능 protograph 표현, 바이너리 코드 설계(E) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1523619
- **Type**: conference
- **Published**: 4-9 Sept. 
- **Authors**: D. Divsalar, S. Dolinar, C. Jones
- **PDF**: https://ieeexplore.ieee.org/document/1523619
- **Abstract**: This paper provides a construction method for low-rate low density parity check codes. Inspired by recently proposed accumulate-repeat-accumulate (ARA) codes, and hybrid concatenated codes, in this paper we extend the construction to low rates. Such codes can be viewed as hybrid concatenations of simple modules such as accumulators, repetition codes, differentiators, and punctured single parity check codes. These codes constitute a subclass of LDPC codes with very fast encoder structure. They also have a projected graph or protograph representation that allows for high-speed decoder implementation. Based on density evolution, we show through some examples that low iterative decoding thresholds close to the channel capacity limits can be achieved, as the block size goes to infinity. Iterative decoding simulation results for short blocks are provided for a few examples that show near-capacity performance and very low error floor

## Memory-efficient decoding of LDPC codes

- **Status**: ✅
- **Reason**: 정규 (3,6) 바이너리 LDPC용 비균일 양자화 BP, MI 최대화 3/4비트 양자화 — NAND LLR 양자화에 직접 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1523376
- **Type**: conference
- **Published**: 4-9 Sept. 
- **Authors**: J.K.-S. Lee, J. Thorpe
- **PDF**: https://ieeexplore.ieee.org/document/1523376
- **Abstract**: We present a low-complexity quantization scheme for the implementation of regular (3,6) LDPC codes. The quantization parameters are optimized to maximize the mutual information between the source and the quantized messages. Using this non-uniform quantized belief propagation algorithm, we have simulated that an optimized 3-bit quantizer operates with 0.2 dB implementation loss relative to a floating point decoder, and an optimized 4-bit quantizer operates less than 0.1 dB quantization loss

## Encoders for block-circulant LDPC codes

- **Status**: ✅
- **Reason**: block-circulant LDPC 인코더 신규 기법, FPGA 구현 100Msym/s — 이식 가능 HW(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:1523758
- **Type**: conference
- **Published**: 4-9 Sept. 
- **Authors**: K. Andrews, S. Dolinar, J. Thorpe
- **PDF**: https://ieeexplore.ieee.org/document/1523758
- **Abstract**: In this paper, we present two encoding methods for block-circulant LDPC codes. The first is an iterative encoding method based on the erasure decoding algorithm, and the computations required are well organized due to the block-circulant structure of the parity check matrix. The second method uses block-circulant generator matrices, and the encoders are very similar to those for recursive convolutional codes. Some encoders of the second type have been implemented in a small field programmable gate array (FPGA) and operate at 100 Msymbols/second

## A rate-compatible family of protograph-based LDPC codes built by expurgation and lengthening

- **Status**: ✅
- **Reason**: 프로토그래프 rate-compatible LDPC 코드패밀리(expurgation+lengthening), 공통 HW 구현·error floor 억제, 바이너리 코드 설계(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1523620
- **Type**: conference
- **Published**: 4-9 Sept. 
- **Authors**: S. Dolinar
- **PDF**: https://ieeexplore.ieee.org/document/1523620
- **Abstract**: We construct a protograph-based rate-compatible family of low-density parity-check (LDPC) codes that cover a very wide range of rates from 1/2 to 16/17, perform within about 0.5 dB of their capacity limits for all rates, and can be decoded conveniently and efficiently with a common hardware implementation. In contrast to alternative methods that create codes of different rates by puncturing, shortening, or expurgation, our method uses a combination of expurgation and lengthening (equivalent to an unusual extension) to produce lower-rate codes. Advantages compared to the alternative methods include roughly uniform utilization of common family decoder hardware for different rates, implementation with uniformly low maximum check node degrees despite high maximum rate, and a large fixed portion of the protograph that can be labeled with a fixed set of edge permutations for all rates. We apply this method to create a rate-compatible code family anchored by a particular code of (nominal) rate 7/8 and length n = 8176 designed by Kou, Lin and Fossorier [1] whose edge permutations are determined by Euclidean geometries (EG). All members of our family retain all of the EG-designed edges and circulant permutations of this anchor code, and this helps to avoid weak spots in the code graph that usually arise when edge permutations are assigned by greedy algorithms. There are also varying numbers of auxiliary and ancillary checks, variables, and edges, allowing realization of different rates, with fixed (nominal) dimension k = 8176 for all rates. Simulations show that all members of this family achieve steeply falling error rate curves without detectable error floors, at least to codeword error rates of about 10-6

## A degree-matched check node approximation for LDPC decoding

- **Status**: ✅
- **Reason**: C: min-sum 보정인자를 임의 차수 체크노드에 매칭하는 저복잡도 근사로 sum-product 성능 달성 - 이식 가능 디코더 기법
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1523516
- **Type**: conference
- **Published**: 4-9 Sept. 
- **Authors**: S.L. Howard, C. Schlegel, V.C. Gaudet
- **PDF**: https://ieeexplore.ieee.org/document/1523516
- **Abstract**: This paper examines ways to recoup the performance loss incurred when using the min-sum approximation instead of the exact sum-product algorithm for decoding low-density parity check codes (LDPCs). Approximations to the correction factor exactly expressing the difference between these two decoding algorithms exist for degree 3 check nodes, and can be applied to higher degree nodes by subdividing them into component degree 3 nodes. However, this results in replication of the approximation. An asymptotic expression for the correction factor at a check node of any degree is derived in this paper, and used to develop two simple approximations to the correction factor, matched to the check node degree. One has very low complexity, and both only need be applied once per check node extrinsic message. Simulation results are presented for each check node approximation when decoding a regular and an irregular LDPC. Both degree-matched check node approximations achieve sum-product decoding performance

## Design of an LDPC code with low error floor

- **Status**: ✅
- **Reason**: E: Tanner 그래프 stopping set 탐색 알고리즘 기반 저 error floor LDPC 코드 설계 - 이식 가능 코드 설계 기법
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1523486
- **Type**: conference
- **Published**: 4-9 Sept. 
- **Authors**: Sang Hyun Lee, Kwang Soon Kim, Jae Kyun Kwon +2
- **PDF**: https://ieeexplore.ieee.org/document/1523486
- **Abstract**: A search algorithm for stopping sets in a Tanner graph is proposed for designing good low-density parity-check (LDPC) codes. By applying the belief-propagation algorithm with messages containing the information of originated variable nodes and their connected edges, the stopping sets can be detected. Furthermore, a code design method using the algorithm is presented and the performances of the designed code over several channels are shown

## Enumerators for protograph ensembles of LDPC codes

- **Status**: ✅
- **Reason**: 프로토그래프 앙상블 weight/stopping set enumerator·최소거리 분석, QC-LDPC 코드 설계(E) 평가기법 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1523728
- **Type**: conference
- **Published**: 4-9 Sept. 
- **Authors**: S.L. Fogal, R. McEliece, J. Thorpe
- **PDF**: https://ieeexplore.ieee.org/document/1523728
- **Abstract**: This paper considers the problem of finding average enumerators for the class of protograph ensembles, which are related in a certain way to quasi-cyclic codes. Our methods, which are necessarily different from those used to compute enumerators for classical irregular ensembles, can be applied to both codeword and stopping set weight enumerators. The method divides codewords into types based on their partial weight enumerator. For each type, an exponent can be computed for the average number of codewords of that type. Maximizing over types of fixed average weight gives the average enumerator which we seek. Although this maximization step is in general difficult because of non-unique local maxima, we can compute it for simple cases. We show that certain ensembles exist which have a linearly growing minimum distance with high probability, while others have at most sublinearly growing minimum distance with high probability

## Improved reversible LDPC codes

- **Status**: ✅
- **Reason**: 반복 인코딩 가능 LDPC의 pseudo-codeword 약점 분석 후 expansion 개선한 신규 재귀적 코드 구성(E), error floor 관련
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1523566
- **Type**: conference
- **Published**: 4-9 Sept. 
- **Authors**: D. Haley, A. Grant
- **PDF**: https://ieeexplore.ieee.org/document/1523566
- **Abstract**: We provide a thorough analysis for a class of iteratively encodable low-density parity-check codes. The iterative encoding technique is based upon the graphical representation of the code and allows the decoder circuit to also be used for encoding, thus saving circuit area. The analysis identifies a weakness in the structure of the code, which arises due to a repetitive pattern in its factor graph. We show that the graph supports pseudo-codewords of low pseudo-weight, and relate this to the empirical observation of some near-codewords. We then propose a new recursive technique for constructing iteratively encodable codes which have improved expansion. The new codes offer a large amount of flexibility in the choice of code length and rate, and performance that compares well to both randomly generated and extended Euclidean-geometry codes

## Hybrid decoding of irregular LDPC codes

- **Status**: ✅
- **Reason**: irregular LDPC용 hybrid majority-based 바이너리 메시지패싱 디코더, Gallager A 초과 성능 - 이식 가능 디코더(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1523345
- **Type**: conference
- **Published**: 4-9 Sept. 
- **Authors**: P. Zarrinkhat, A.H. Banihashemi
- **PDF**: https://ieeexplore.ieee.org/document/1523345
- **Abstract**: Time-invariant hybrid (HTI) decoding of irregular low-density parity-check (LDPC) codes is studied. Focusing on HTI  algorithms with majority-based (MB) binary message-passing constituents, we use density evolution and finite-length simulation to analyze the performance and the convergence properties of these algorithms. Tight upper bounds on the threshold of MB HTI algorithms are derived, and it is proven that the asymptotic error probability for these algorithms tends to zero at least exponentially with the number of iterations. We devise optimal MB HTI algorithms for irregular LDPC codes, and show that these algorithms outperform Gallager's algorithm A applied to optimized irregular LDPC codes. We also show that compared to switch-type algorithms, such as Gallager's algorithm B, where a comparable improvement is obtained by switching between different MB algorithms, MB HTI algorithms are more robust, and can better cope with unknown channel conditions, and thus can be practically more attractive

## The benefit of thresholding in LP decoding of LDPC codes

- **Status**: ✅
- **Reason**: 바이너리 LDPC LP 디코더용 LLR thresholding/truncation 기법 - NAND LLR 양자화에 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1523344
- **Type**: conference
- **Published**: 4-9 Sept. 
- **Authors**: J. Feldman, R. Koetter, P.O. Vontobel
- **PDF**: https://ieeexplore.ieee.org/document/1523344
- **Abstract**: Consider data transmission over a binary-input additive white Gaussian noise channel using a binary low-density parity-check code. We ask the following question: Given a decoder that takes log-likelihood ratios as input, does it help to modify the log-likelihood ratios before decoding? If we use an optimal decoder then it is clear that modifying the log-likelihoods cannot possibly help the decoder's performance, and so the answer is "no." However, for a suboptimal decoder like the linear programming decoder, the answer might be "yes": In this paper we prove that for certain interesting classes of low-density parity-check codes and large enough SNRs, it is advantageous to truncate the log-likelihood ratios before passing them to the linear programming decoder

## Constructions for irregular repeat-accumulate codes

- **Status**: ✅
- **Reason**: IRA 인터리버 조합론적 설계+sum-product 적합 Tanner 그래프, w3IRA 신규 구성—바이너리 코드설계 E
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1523318
- **Type**: conference
- **Published**: 4-9 Sept. 
- **Authors**: S.J. Johnson, S.R. Weller
- **PDF**: https://ieeexplore.ieee.org/document/1523318
- **Abstract**: Recent promising theoretical results for irregular repeat-accumulate (IRA) codes, together with their extremely simple encoding, motivates this investigation into the design and implementation of finite-length IRA codes. In this paper interleavers for RA codes are designed using combinatorial techniques to produce RA codes with Tanner graphs suitable for sum-product decoding. Further, a modified RA code accumulator is used to construct new IRA codes with columns of weight 3 in the accumulator. These new codes, called w3IRA codes, can be designed with flexible degree distributions and retain the simple encoding of traditional IRA codes

## Structured eIRA codes with low floors

- **Status**: ✅
- **Reason**: 구조화 eIRA 코드(낮은 error floor, 효율적 인코딩, SW/HW 성능)—바이너리 코드설계 E
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1523317
- **Type**: conference
- **Published**: 4-9 Sept. 
- **Authors**: Yifei Zhang, W.E. Ryan, Yan Li
- **PDF**: https://ieeexplore.ieee.org/document/1523317
- **Abstract**: In a recent paper, Yang et al. presented the class of extended irregular repeat-accumulate (eIRA) codes which are efficiently encodable LDPC codes possessing very low error-rate floors and are appropriate for code rates 1/2 or greater. While efficiently encodable, the left-most (n-k)-by-k submatrix of an eIRA code parity-check matrix is random in nature, making efficient decoder implementation problematic. In the present paper, we present structured eIRA codes. We first present some ensemble results for the general class of eIRA codes, after which the subclass of structured eIRA (SeIRA) codes is defined. Software- and hardware-based performance results for SeIRA code designs (rates 0.5 to 0.9) are then presented.

## A class of quasi-cyclic regular LDPC codes from cyclic difference families with girth 8

- **Status**: ✅
- **Reason**: cyclic difference family 기반 girth-8 QC-LDPC 신규 구성, 4/6-cycle 제거 조건 제시 — 코드설계(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1523756
- **Type**: conference
- **Published**: 4-9 Sept. 
- **Authors**: M. Fujisawa, S. Sakata
- **PDF**: https://ieeexplore.ieee.org/document/1523756
- **Abstract**: In this paper, we propose a class of regular LDPC codes from a cyclic difference family, which is a kind of combinatorial design. These LDPC codes have no 4-cycles, i.e., cycles of length 4. We clarify the conditions on which these codes with column weight 3 have no 6-cycles and discuss their minimum distance. Finally, we show the performance of the proposed codes with high rates and moderate leng...

## Tree-based construction of LDPC codes

- **Status**: ✅
- **Reason**: 트리 기반 바이너리 LDPC 구성(MOLS 연결, pseudocodeword weight=최소거리) — 신규 코드 설계 기법(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1523456
- **Type**: conference
- **Published**: 4-9 Sept. 
- **Authors**: D. Sridhara, C. Kelley, J. Rosenthal
- **PDF**: https://ieeexplore.ieee.org/document/1523456
- **Abstract**: We present a construction of LDPC codes that have minimum pseudocodeword weight equal to the minimum distance, and perform well with iterative decoding. The construction involves enumerating a d-regular tree for a fixed number of layers and employing a connection algorithm based on mutually orthogonal Latin squares to close the tree. Methods are presented for degrees d = ps and d = ps + 1, for p a prime, one of which includes the well-known finite-geometry-based LDPC codes

## Asymptotically good codes with high iterative decoding performances

- **Status**: ✅
- **Reason**: LDPC/터보 하이브리드 신규 부호, 우수한 반복 디코딩 성능+선형 최소거리 — 신규 구성/디코딩 기여(E/C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1523457
- **Type**: conference
- **Published**: 4-9 Sept. 
- **Authors**: I. Andriyanova, J.-P. Tillich, J.-C. Carlach
- **PDF**: https://ieeexplore.ieee.org/document/1523457
- **Abstract**: We investigate a new class of codes which is in some senses a hybrid between LDPC codes and turbo-codes. We show that when the parameters of this class are well chosen they have very good iterative decoding performances and at the same time a minimum distance which is typically linear in the code length

## On the stopping distance and the stopping redundancy of codes

- **Status**: ✅
- **Reason**: stopping set/distance/redundancy — 패리티검사 행렬 설계로 stopping distance 향상, 바이너리 LDPC error floor 관련 코드 설계(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1523483
- **Type**: conference
- **Published**: 4-9 Sept. 
- **Authors**: M. Schwartz, A. Vardy
- **PDF**: https://ieeexplore.ieee.org/document/1523483
- **Abstract**: It is now well known that the performance of a linear code Copf under iterative decoding on a binary erasure channel (and other channels) is determined by the size of the smallest stopping set in the Tanner graph for Copf. Several recent papers refer to this parameter as the stopping distance s of Copf. This is somewhat of a misnomer since the size of the smallest stopping set in the Tanner graph for Copf depends on the corresponding choice of a parity-check matrix. It is easy to see that s les d, where d is the minimum Hamming distance of Copf, and we show that it is always possible to choose a parity-check matrix for Copf (with sufficiently many dependent rows) such that s = d. We thus introduce a new parameter, termed the stopping redundancy of Copf, defined as the minimum number of rows in a parity-check matrix H for Copf such that the corresponding stopping distance s(H) attains its largest possible value, namely s(H) = d. We then derive general bounds on the stopping redundancy of linear codes. We also examine several simple ways of constructing codes from other codes, and study the effect of these constructions on the stopping redundancy. Specifically, for the family of binary Reed-Muller codes (of all orders), we prove that their stopping redundancy is at most a constant times their conventional redundancy. We show that the stopping redundancies of the binary and ternary extended Golay codes are at most 34 and 22, respectively. Finally, we provide upper and lower bounds on the stopping redundancy of MDS codes

## Replica shuffled iterative decoding

- **Status**: ✅
- **Reason**: replica shuffled iterative decoding, 수렴 가속·복잡도/지연 trade-off - LDPC BP 스케줄 개선 디코더(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1523375
- **Type**: conference
- **Published**: 4-9 Sept. 
- **Authors**: Juntan Zhang, Yige Wang, M. Fossorier +1
- **PDF**: https://ieeexplore.ieee.org/document/1523375
- **Abstract**: Replica shuffled versions of iterative decoders of turbo codes, low-density parity-check codes and turbo product codes are presented. The proposed schemes converge faster than standard and previously proposed "shuffled" approaches. Simulations show that the new schedules offer good performance versus complexity/latency trade-offs.

## A high-speed analog min-sum iterative decoder

- **Status**: ✅
- **Reason**: 아날로그 min-sum 반복 디코더 CMOS 회로(current-mode); 이식 가능 HW 아키텍처(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:1523649
- **Type**: conference
- **Published**: 4-9 Sept. 
- **Authors**: S. Hemati, A.H. Banihashemi, C. Plett
- **PDF**: https://ieeexplore.ieee.org/document/1523649
- **Abstract**: Current-mode circuits are presented for implementing analog min-sum (MS) iterative decoders. Proposed circuits are devised based on current mirrors. Therefore, in any fabrication technology that accurate current mirrors can be designed, analog MS decoders can be implemented. The functionality of the proposed modules was verified by implementing an analog MS decoder for a (32,8,10) regular LDPC code in 0.18-mum CMOS technology. In low signal to noise ratios when the circuit imperfections are dominated by the noise of the channel, the measured error correcting performance of this chip in steady-state condition surpasses that of the conventional MS decoder, and is close to the performance predicted by the earlier work on the dynamics of the continuous-time analog decoding by Hemati and Banihashemi, ISIT2004. At a throughput of 24 Mb/s, loss in the coding gain compared to the conventional MS decoder at BER of 10-3 is about 0.3 dB. To the best of our knowledge, this decoder has the highest throughput and the lowest power/speed ratio among the reported analog CMOS iterative decoders

## An LDPCC decoding algorithm based on bowman-levin approximation -comparison with bp and CCCP-

- **Status**: ✅
- **Reason**: Bowman-Levin 근사 기반 새 LDPC 복호 알고리즘, BP/CCCP 초과 성능 - 이식 가능 디코더(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1523373
- **Type**: conference
- **Published**: 4-9 Sept. 
- **Authors**: M. Inoue, M. Komiya, Y. Kabashima
- **PDF**: https://ieeexplore.ieee.org/document/1523373
- **Abstract**: Belief propagation (BP) and the concave convex procedure (CCCP) are both methods that utilize the Bethe free energy as a cost function and solve information processing tasks. We have developed a new algorithm that also uses the Bethe free energy, but changes the roles of the master variables and the slave variables. This is called the Bowman-Levin (BL) approximation in the domain of statistical physics. When we applied the BL algorithm to decode the Gallager ensemble of short-length regular low-density parity check codes (LDPCC) over an additive white Gaussian noise (AWGN) channel, its average performance was somewhat better than that of either BP or CCCP. This implies that the BL algorithm can also be successfully applied to other problems to which BP or CCCP has already been applied

## Bit-flipping post-processing for forced convergence decoding of LDPC codes

- **Status**: ✅
- **Reason**: forced convergence LDPC 디코더에 bit-flipping 후처리로 error floor 완화; 이식 가능 BP 디코더 개선(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7078274
- **Type**: conference
- **Published**: 4-8 Sept. 
- **Authors**: Ernesto Zimmermann, Prakash Pattisapu, Gerhard Fettweis
- **PDF**: https://ieeexplore.ieee.org/document/7078274
- **Abstract**: The recently proposed forced convergence technique allows for reducing the decoding complexity of Low-Density Parity-Check Codes (LDPCC) at only slight deterioration in performance. The basic idea is to restrict the message passing during LDPC decoding to the nodes that still significantly contribute to the decoding result. In this paper, we propose to add a bit-flipping post-processor to the forced convergence decoder in order to alleviate some problems of this novel technique, namely the error floors observed when aiming for high reduction in decoding complexity. Our results show that combining a hard decision bit-flipping with the forced convergence approach enables to almost retain original error correction performance while further reducing decoding complexity.

## VLSI design of a high-throughput multi-rate decoder for structured LDPC codes

- **Status**: ✅
- **Reason**: structured LDPC용 고처리량 다중율 VLSI 디코더, 유한정밀도 분석·플렉시블 아키텍처 — 이식 가능 HW(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:1559801
- **Type**: conference
- **Published**: 30 Aug.-3 
- **Authors**: M. Rovini, N.E. L'Insalata, F. Rossi +1
- **PDF**: https://ieeexplore.ieee.org/document/1559801
- **Abstract**: Despite recent advances in the microelectronics technology, the implementation of high-throughput decoders for LDPC codes remains a challenging task. This paper aims at summarising the top-down design flow of a decoder for a structured LDPC code compliant with the WWiSE proposal for WLAN. Starting from the system performance analysis with finite-precision arithmetic, a high-throughput architecture is presented as an enhancement of the state-of-the-art solutions, and its VLSI design detailed. The envisaged architecture is also very flexible as it supports several code rates with no significant hardware overhead. The overall decoder, synthesised on 0.18/spl mu/m standard cells CMOS technology, showed remarkable performances: small implementation loss (0.2dB down to BER=10/sup -8/), low latency (less than 6.0/spl mu/s), high useful throughput (up to 940 Mbps) and low complexity (about 375 Kgates).

## A finite-field transform domain construction of binary low-density parity-check codes

- **Status**: ✅
- **Reason**: 유한체 변환 도메인 바이너리 LDPC(sparse H) 신규 구성법 - 코드설계(E) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1531860
- **Type**: conference
- **Published**: 29 Aug.-1 
- **Authors**: R. Horan, C. Tjhai, M. Tomlinson +2
- **PDF**: https://ieeexplore.ieee.org/document/1531860
- **Abstract**: A new method of finding binary cyclic codes from the finite-field transform domain is presented. These cyclic codes have sparse parity-check matrix and thus are suitable for iterative decoding. Some interesting properties of the proposed construction method include the knowledge of the minimum distance and the ability to trade the increase in code dimension with a reduction in the parity-check matrix sparsity. By means of simulations, we show that the error correcting performance of the codes under iterative decoding is very close to the sphere-packing-bound constrained for binary transmission.

## Finite-length scaling of irregular LDPC code ensembles

- **Status**: ✅
- **Reason**: 불규칙 LDPC 유한길이 스케일링/차수분포 최적화 - 유한길이 코드설계(E) 기법 이식 가능, BEC이나 분석방법론 일반적
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1531845
- **Type**: conference
- **Published**: 29 Aug.-1 
- **Authors**: A. Amraoui, R. Urbanke, A. Montanari
- **PDF**: https://ieeexplore.ieee.org/document/1531845
- **Abstract**: We investigate the finite-length scaling methodology for irregular LDPC code ensembles when transmission takes place over the binary erasure channel (BEC). We first show how the necessary computations, namely the covariance evolution and the computation of the finite-length shift, can be accomplished in the irregular case. We then investigate how the obtained approximation can be used to predict the performance of irregular code ensembles and to optimize the degree distributions for finite-length codes.

## Construction of LDPC codes for AWGN and binary erasure channels based on finite fields

- **Status**: ✅
- **Reason**: 유한체 기반 구조적 바이너리 LDPC 구성(girth>=6, QC) — 이식 가능 코드 설계(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1531903
- **Type**: conference
- **Published**: 29 Aug.-1 
- **Authors**: Lingqi Zeng, L. Lan, Y.Y. Tai +2
- **PDF**: https://ieeexplore.ieee.org/document/1531903
- **Abstract**: This paper presents a method for constructing structured LDPC codes based on finite fields and affine mappings. The Tanner graphs of these codes have girth at least six. Experimental results show that codes constructed based on this method with iterative decoding perform well on both the AWGN and binary erasure channels. Furthermore, codes constructed based on prime fields are quasi-cyclic.

## A note on a decoding algorithm of codes on graphs with small loops

- **Status**: ✅
- **Reason**: FG 작은 루프 클러스터링 디코딩 알고리즘(SPA 개선) - 바이너리 LDPC 디코더(C) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1531867
- **Type**: conference
- **Published**: 29 Aug.-1 
- **Authors**: N. Kobayashi, T. Matsushima, S. Hirasawa
- **PDF**: https://ieeexplore.ieee.org/document/1531867
- **Abstract**: The best-known algorithm for the decoding of low-density parity-check (LDPC) codes is the sum-product algorithm (SPA). The SPA is a message-passing algorithm on a graphical model called a factor graph (FG). The performance of the SPA depends on a structure of loops in a FG. Pearl showed that loops in a graphical model could be erased by the clustering method. This method clusters plural nodes into a single node. In this paper, we show several examples about a decoding on a FG to which the clustering method is applied. And we propose an efficient decoding algorithm for it. For a binary erasure channel (BEC), the performance with this method goes up clearly.

## Iterative list decoding

- **Status**: ✅
- **Reason**: 확장 패리티검사 행렬 기반 반복 list 디코딩(bit-flipping 변형) - 디코더 기법(C) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1531863
- **Type**: conference
- **Published**: 29 Aug.-1 
- **Authors**: J. Justesen, T. Hoholdt, J. Hjaltason
- **PDF**: https://ieeexplore.ieee.org/document/1531863
- **Abstract**: We analyze the relation between iterative decoding and the properties of the extended parity check matrix. By considering a modified version of bit flipping, which produces a list of decoded words, we derive several relations between decodable error patterns and parameters of the code. By developing a tree of codewords at minimal distance form the received vector, we also obtain new information about the code.

## Further results on mapping functions

- **Status**: ✅
- **Reason**: 병렬 LDPC 디코더의 collision-free 메모리 매핑함수 일반화 - 이식 가능 HW 아키텍처 D
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:1531893
- **Type**: conference
- **Published**: 29 Aug.-1 
- **Authors**: A. Tarable, S. Benedetto
- **PDF**: https://ieeexplore.ieee.org/document/1531893
- **Abstract**: In a previous paper as presented by Tarable et al. (2004), the authors introduced the concept of mapping functions as a tool to cope with the problem of collision-free memory mappings in turbo and LDPC parallel decoder implementations. In this paper, we address some implementation issues of the original solution, define a dual problem, which can be of high interest for practical implementations, and give the generalization of mapping functions to N > 2 parallel decoders.

## Cycle elimination method to construct VLSI oriented LDPC codes

- **Status**: ✅
- **Reason**: 사이클 제거 + VLSI 지향 LDPC 구성 — 코드설계+HW(E/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1557966
- **Type**: conference
- **Published**: 28-28 Sept
- **Authors**: Lei Yang, Hiu Liu, C.-J.R. Shi
- **PDF**: https://ieeexplore.ieee.org/document/1557966
- **Abstract**: N/A

## Deterministic quasi-regular LDPC codes

- **Status**: ✅
- **Reason**: 결정론적 quasi-regular 바이너리 LDPC 코드 구성 — 이식 가능 코드 설계(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1557964
- **Type**: conference
- **Published**: 28-28 Sept
- **Authors**: Wenming Liu, Guangxi Zhu, Yongqiang Deng +1
- **PDF**: https://ieeexplore.ieee.org/document/1557964
- **Abstract**: N/A

## Greedy constructions of degree puncture sequences for irregular LDPC codes

- **Status**: ✅
- **Reason**: 비정칙 LDPC용 degree puncture sequence의 greedy 구성 - 바이너리 LDPC 코드 설계(E) 이식 가능, abstract null이나 제목상 코드설계 기여
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1558062
- **Type**: conference
- **Published**: 28-28 Sept
- **Authors**: V.J. Stolpman, G.C. Orsak
- **PDF**: https://ieeexplore.ieee.org/document/1558062
- **Abstract**: N/A

## Design of low-density parity-check codes using linear programming for modulation and detection

- **Status**: ✅
- **Reason**: 선형계획 기반 LDPC 코드 설계, 변조/검출용 — 이식 가능 코드 설계 가능성, 애매하여 in
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1557968
- **Type**: conference
- **Published**: 28-28 Sept
- **Authors**: Yi Yang, Xu Changqing, Zhang Haibin
- **PDF**: https://ieeexplore.ieee.org/document/1557968
- **Abstract**: N/A

## Low computational complexity algorithms of LDPC decoder for DVB-s2 systems

- **Status**: ✅
- **Reason**: DVB-S2 LDPC 디코더 저복잡도 알고리즘 — 이식 가능 디코더 기법(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1557969
- **Type**: conference
- **Published**: 28-28 Sept
- **Authors**: Eun-A Choi, Dae-Ik Chang, Deock-Gil +1
- **PDF**: https://ieeexplore.ieee.org/document/1557969
- **Abstract**: N/A

## Optimization of irregular LDPC codes on Rician channel

- **Status**: ✅
- **Reason**: PSO+이산밀도진화로 비정규 LDPC degree distribution 최적화 - offset BP 디코더 코드설계 기법(E) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1544061
- **Type**: conference
- **Published**: 26-26 Sept
- **Authors**: Xu Hua, Xu Cheng-qi, Zheng Xiao-chuan
- **PDF**: https://ieeexplore.ieee.org/document/1544061
- **Abstract**: For irregular LDPC codes,the density evolution method can track the messages to find out the noise threshold, enabling optimization of the degree distribution. A new optimized scheme for irregular LDPC codes is proposed in this paper, which is combining Zhengya He's modified particle swarm optimization (PSO) algorithm with discrete density evolution (DDE) for the offset BP-based decoding algorithm. Several optimized degree distribution pairs and corresponding threshold of LDPC codes over Rician channel were given using the proposed scheme. The performance of the optimized LDPC codes was also analyzed. Simulation results shows that the proposed scheme is effective.

## Construction of low density parity check codes using quadratic congruential sequences

- **Status**: ✅
- **Reason**: 2차합동수열 기반 정규 LDPC 구성으로 인코더 구조를 재귀생성(메모리 절약, HW 친화) - 코드설계(E)/HW(D) 기여
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1544068
- **Type**: conference
- **Published**: 26-26 Sept
- **Authors**: Wenming Liu, Guangxi Zhu, Yongqiang Deng
- **PDF**: https://ieeexplore.ieee.org/document/1544068
- **Abstract**: In this paper a method using quadratic congruential sequences to design regular LDPC code is proposed. The main advantage of this method is that the structure of the encoder can be generated using a determined recursion, rather than having to store the encoder structure graph in memory, which facilitates hardware implementation. Simulation results show that these codes provide almost the same performance of a constrained pseudorandom construction that explicitly avoids cycles of length less than or equal to four.

## An improved decoding algorithm of low-density parity-check codes

- **Status**: ✅
- **Reason**: factor graph cycle 경로 기록·차단으로 BP 개선하는 신규 디코더 알고리즘(C) - 바이너리 LDPC BP 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1544078
- **Type**: conference
- **Published**: 26-26 Sept
- **Authors**: Deng Yongqiang, Zhu Guangxi, Liu Wenming +1
- **PDF**: https://ieeexplore.ieee.org/document/1544078
- **Abstract**: In this paper, the decoding algorithm of low-density parity-check (LDPC) codes is analyzed, and a new decoding algorithm based on the belief propagation (BP) algorithm to eliminate the influence of cycles in the factor graph is proposed. In the traditional BP algorithm, the cycles of factor graph sends message back to its source, and this decreases the decoding performance. The new algorithm records each cycle's path and length of each node, and cuts off the path by which message is propagated when the message comes back. It can advance the decoding performance by protect the message of good quality be propagated as widely as possible. Our results of simulation show that the performance of new algorithm is not worse than that of traditional BP algorithm in the low SNR channel and the new algorithm significantly outperform traditional BP algorithm in good channel condition.

## An (8158,7136) low-density parity-check encoder

- **Status**: ✅
- **Reason**: regular QC-LDPC sub-code 인코더 VLSI 구현, 효율적 패리티 레지스터 설계; HW(D)+QC구성(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1568764
- **Type**: conference
- **Published**: 21-21 Sept
- **Authors**: L. Miles, J. Gambles, G. Maki +2
- **PDF**: https://ieeexplore.ieee.org/document/1568764
- **Abstract**: Low-density parity-check codes achieve coding performance which approaches the Shannon limit. Based on a novel method for deriving regular quasi-cyclic sub-codes, a radiation tolerant encoder was implemented in 0.25/spl mu/m CMOS. Use of generator polynomial reconstruction, partial product multiplication and functional sharing in the parity register results in a highly efficient design. Only 1,492 flip flops along with a programmable 21-bit look-ahead scheme are used to achieve a 1 Gb/s data throughput. A comparable two-stage encoder requires 8,176 flip flops.

## Loosely coupled memory-based decoding architecture for low density parity check codes

- **Status**: ✅
- **Reason**: loosely-coupled 메모리 기반 부분병렬 LDPC 디코더 아키텍처+스케줄링; 이식 HW(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:1568765
- **Type**: conference
- **Published**: 21-21 Sept
- **Authors**: Se-Hyeon Kang, In-Cheol Park
- **PDF**: https://ieeexplore.ieee.org/document/1568765
- **Abstract**: Parallel decoding is required for low density parity check (LDPC) codes to achieve high decoding throughput, but it suffers from a large set of registers and complex interconnections due to randomly located 1's in the sparse parity check matrix. This paper proposes a new LDPC decoding architecture to reduce registers and alleviate complex interconnections. To reduce the number of messages to be exchanged among processing units, two data flows that can be loosely coupled are developed by allowing duplicated operations. In addition, a partially parallel architecture is proposed to promote the memory usage and an efficient algorithm that schedules the processing order of the partially parallel architecture is also proposed to reduce the overall processing time by overlapping operations. To verify the proposed architecture, a 1024 bit rate-1/2 LDPC decoder is designed using a 0.18 /spl mu/m CMOS process. The decoder occupies an area of 10.08mm/sup 2/ and provides almost 1Gbps decoding throughput at the frequency of 200MHz.

## An 80-Mb/s 0.18-/spl mu/m CMOS analog min-sum iterative decoder for a (32,8,10) LDPC code

- **Status**: ✅
- **Reason**: min-sum 반복디코더 CMOS 아날로그 구현; 이식 가능 디코더/HW(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1568652
- **Type**: conference
- **Published**: 21-21 Sept
- **Authors**: S. Hemati, A.H. Banihashemi, C. Plett
- **PDF**: https://ieeexplore.ieee.org/document/1568652
- **Abstract**: Analog current-mode circuits are presented for implementing min-sum (MS) iterative decoders, which are used for decoding low-density parity-check (LDPC) codes and turbo codes. While previously reported analog decoders rely on the exponential characteristics of bipolar or subthreshold MOS transistors, proposed circuits can also be used for designing strongly inverted CMOS analog decoders. A proof-of-concept 80-Mb/s CMOS MS decoder is designed and fabricated that consumes the least reported energy per bit and operates at least six times faster than previously reported CMOS analog decoders.

## Versatile architectures for decoding a class of LDPC codes

- **Status**: ✅
- **Reason**: 가변 rate LDPC 구성과 이를 활용한 FPGA 디코딩 아키텍처 — D/E HW+코드설계
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1523112
- **Type**: conference
- **Published**: 2-2 Sept. 
- **Authors**: A. Byrne, E.M. Popovici, M. O'Sullivan
- **PDF**: https://ieeexplore.ieee.org/document/1523112
- **Abstract**: This paper presents a construction for low and high rate Low-Density Parity Check (LDPC) codes, their performance and efficient hardware implementation. The problem with decoding for LDPC codes is the linear increase in resource requirements as the size of the parity check matrix increases. This results in a number of issues with regard to practical implementation. These issues include interconnect routing, memory size and parallelism. A construction for low complexity, variable rate LDPC code will be introduced and an architecture that takes advantage of certain properties of this construction is proposed. A versatile LDPC decoding architecture is then evaluated on FPGA.

## Study of nonlinear dynamics of LDPC decoders

- **Status**: ✅
- **Reason**: LDPC 반복 디코더를 비선형 동역학으로 분석해 더 나은 디코더 설계 시사 — C 디코더 알고리즘 통찰, 애매하여 in
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1523017
- **Type**: conference
- **Published**: 2-2 Sept. 
- **Authors**: Xia Zheng, F.C.M. Lau, C.K. Tse +1
- **PDF**: https://ieeexplore.ieee.org/document/1523017
- **Abstract**: Low-density-parity-check (LDPC) codes have aroused much research interest because of their excellent bit error performance. The behaviour of the iterative LDPC decoders, however, has not been fully investigated at all signal-to-noise ratios (SNRs). By considering the LDPC decoders as high-dimensional nonlinear dynamical systems, we attempt to study the corresponding phase trajectories at different SNR values. By having an in-depth understanding of the decoder behaviour, engineers should be able to design more effective and efficient decoders.

## An early decision decoding algorithm for LDPC codes using dynamic thresholds

- **Status**: ✅
- **Reason**: early decision dynamic threshold 디코딩으로 메시지/스위칭 감소 — C 이식 가능 BP 디코더 변형
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1523116
- **Type**: conference
- **Published**: 2-2 Sept. 
- **Authors**: A. Blad, O. Gustafsson, L. Wanhammar
- **PDF**: https://ieeexplore.ieee.org/document/1523116
- **Abstract**: Low-density parity-check codes have recently received extensive attention as a forward error correction scheme in a wide area of applications. The decoding algorithm is inherently parallelizable, allowing communication at high speeds. One of the main disadvantages, however, is large memory requirements for interim storing of decoding data. In this paper, we investigate a modification to the decoding algorithm, using early decisions for bits with high reliabilities. This reduces the amount of messages passed by the algorithm, which can be expected to reduce the switching activity of a hardware implementation. While direct application of the modification results in severe performance penalties, we show how to adapt the algorithm to reduce the impact, resulting in a negligible decrease in error correction performance.

## Reduced complexity, FPGA implementation of quasi-cyclic LDPC decoder

- **Status**: ✅
- **Reason**: QC-LDPC 디코더 FPGA semi-parallel 아키텍처/메모리 컨트롤러 — D 이식 가능 HW
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:1522967
- **Type**: conference
- **Published**: 2-2 Sept. 
- **Authors**: C. Spagnol, W. Marnane, E. Popovici
- **PDF**: https://ieeexplore.ieee.org/document/1522967
- **Abstract**: This paper describes an FPGA implementation of a decoder for a particular family of low density parity check (LDPC) codes, the quasi-cyclic LDPC codes. The structure of a quasi-cyclic code is well known and allows us to reduce the complexity of the interconnections between bit nodes and check nodes. The decoder has a semi-parallel architecture and it takes full advantage of the structure of the code and the hardware resources present in an FPGA. We achieve simple memory controller resulting in an efficient use of the memory. The decoder is implemented based on the parameters that characterize a quasi-cyclic LDPC code. This makes it easily adaptable for a class of quasi-cyclic codes. We evaluate the performance of our codes and present some FPGA design trade-off.

## A 3.33Gb/s (1200,720) low-density parity check code decoder

- **Status**: ✅
- **Reason**: 3.33Gb/s LDPC 디코더 VLSI 아키텍처(데이터 재정렬, 동시 2코드워드 처리) 이식 가능 HW(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:1541597
- **Type**: conference
- **Published**: 12-16 Sept
- **Authors**: Chien-Ching Lin, Kai-Li Lin, Hsie-Chia Chang +1
- **PDF**: https://ieeexplore.ieee.org/document/1541597
- **Abstract**: In this paper, a (1200,720) LDPC decoder based on an irregular parity check matrix is presented. For achieving higher chip density and less critical path delay, the proposed architecture features a data reordering such that only one specific data bus exists between message memories and computational units. Moreover, the LDPC decoder can also process two different codewords concurrently to increase throughput and datapath efficiency. After chip implementation, a 3.33Gb/s data rate is achieved with 8 decoding iterations in the 21.23mm/sup 2/ 0.18/spl mu/m silicon area. The other 0.13/spl mu/m chip with the 10.24mm/sup 2/ core can further reach a 5.92Gb/s data rate under 1.02V supply.

## A Study on Symbol and Sub-Carrier Mapping Techniques for MC-CDMA based on LDPC Code with Progressively Increased Column-Weight

- **Status**: ✅
- **Reason**: PICW(점진 증가 열가중치) rate-compatible LDPC 코드 구성 제안 — 이식 가능한 코드설계 기법(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1651440
- **Type**: conference
- **Published**: 11-14 Sept
- **Authors**: Miyazaki, Chen Zheng, Suzuki +1
- **PDF**: https://ieeexplore.ieee.org/document/1651440
- **Abstract**: This paper proposes a symbol mapping scheme on sub-carriers in use of MC-CDMA (Multi Carrier-Code Division Multiple Access) and LDPC (Low-Density Parity-Check) codes. Aiming at high spectrum efficiency, 16QAM modulation and LDPC codes with the PICW (Progressively Increased Column-Weight) are used here. The PICW-LDPC code is proposed in our previous studies and is proved to have better decoding performance as rate-compatible LDPC codes. By adopting the proposed symbol mapping method, the FER (Frame Error Rate) performance of the PICW-LDPC code is improved, the required EJN0 is reduced by 0.12 dB in an AWGN channel. In order to improve FER performance in the multi-path channel, the proposed sub-carrier mapping is further applied, and the required Es/N0can also be reduced by 2.32 dB.

## Rate-compatible puncturing for low-density parity-check codes with dual-diagonal parity structure

- **Status**: ✅
- **Reason**: dual-diagonal QC-LDPC용 rate-compatible puncturing 패턴 — 이식 가능한 코드설계 기법(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1651922
- **Type**: conference
- **Published**: 11-14 Sept
- **Authors**: Eoiyoung Choi, Seung-Bum Suh, Jaehong Kim
- **PDF**: https://ieeexplore.ieee.org/document/1651922
- **Abstract**: We investigate suitable puncturing patterns for circulant sub-matrices based quasi-cyclic low-density parity-check codes whose binary base matrices have dual-diagonal parity structure with a single weight-3 column. The proposed method develops the existing puncturing criteria, and exploits the structure of the parity-check matrix. The performance of the proposed puncturing patterns is quite competitive with the performance of dedicated codes for individual rates

## Construction of irregular low-density parity-check codes based on V-matrix

- **Status**: ✅
- **Reason**: V-matrix 기반 비정규 LDPC 패리티검사행렬 구성법(컴퓨터 탐색 회피) — 이식 가능한 코드설계(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1651908
- **Type**: conference
- **Published**: 11-14 Sept
- **Authors**: D. Xie, Jun Wang, Yu Wen +1
- **PDF**: https://ieeexplore.ieee.org/document/1651908
- **Abstract**: Traditional irregular low-density parity-check (IR-LDPC) codes are constructed based on the irregular bipartite graphs with carefully chosen degree patterns on both sides and computer searching is usually applied, which leads complexity to be relatively high. In this paper, we introduce the concept of V-matrix which is a matrix composed of vectors and propose a new approach to construct the IR-LDPC codes. By introducing some special operations, we can obtain the desired sparse parity-check matrix for IR-LDPC codes design. Because computer searching is avoided, the complexity is efficiently reduced. Computer simulation results show that our approach can achieve good tradeoff between complexity and performance

## A performance improvement and error floor avoidance technique for belief propagation decoding of LDPC codes

- **Status**: ✅
- **Reason**: trapping set 식별로 BP error-floor 회피·waterfall 개선 — NAND LDPC error floor에 직접 이식 가능한 디코더 기법(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1651870
- **Type**: conference
- **Published**: 11-14 Sept
- **Authors**: E. Cavus, B. Daneshrad
- **PDF**: https://ieeexplore.ieee.org/document/1651870
- **Abstract**: In this work, we introduce a unique technique that improves the performance of the BP decoding in waterfall and error-floor regions by reversing the decoder failures. Based on the short cycles existing in the bipartite graph, an importance sampling simulation technique is used to identify the bit and check node combinations that are the dominant sources of error events, called trapping sets. Then, the identified trapping sets are used in the decoding process to avoid the pre-known failures and to converge to the transmitted codeword. With a minimal additional decoding complexity, the proposed technique is able to provide performance improvements for short-length LDPC codes and push or avoid error-floor behaviors of longer codes
