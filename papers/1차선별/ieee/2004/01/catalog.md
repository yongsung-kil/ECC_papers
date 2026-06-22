# IEEE Xplore — 2004-01 (1차선별 통과)


## Efficient high-speed quasicyclic LDPC decoder architecture

- **Status**: ✅
- **Reason**: D: QC-LDPC 고속 디코더 아키텍처, BP 두 단계 부하 재분배·LUT·adder tree 최적화 — NAND ECC HW로 이식 가능
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:1399191
- **Type**: conference
- **Published**: 2004
- **Authors**: Y. Zhang, Z. Wang, K. K. Parhi
- **PDF**: https://ieeexplore.ieee.org/document/1399191
- **Abstract**: This paper studies load imbalance problem in the two stages of belief propagation decoding algorithm for LDPC codes and redistributes computational load between two stages. To further reduce the critical path delay, new look-up-tables (LUT) are developed to replace both conventional LUTs and data format transformation blocks. The adder trees are also reorganized for speed. This novel approach can reduce the critical path delay by 41.0% with negligible increase in the logic core size. This paper also exploits the similarity between these two stages and derives an area efficient design that remaps the functional units for these two stages onto the same hardware, which can reduce the logic core size by 10.2% and reduce the critical path delay by 16.2%.

## An efficient encoding method for LDPC codes based on cyclic shift

- **Status**: ✅
- **Reason**: array/SFT 바이너리 QC-LDPC를 cyclic shift 나눗셈회로로 인코딩하는 HW 기법(D/E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1365312
- **Type**: conference
- **Published**: 2004
- **Authors**: H. Fujita, K. Sakaniwa
- **PDF**: https://ieeexplore.ieee.org/document/1365312
- **Abstract**: Low-density parity-check (LDPC) codes are one of the most promising next generation error correcting codes and many investigations shows that LDPC codes suitable for many hardware implementation. Although randomly constructed LDPC codes are usually encoded by using generator matrix, this method requires quadratic time complexity and is not easy to implement. This work presents the encoding of array-type LDPC codes and a special class of Sridhara-Fuja-Tanner (SFT) codes by division circuits as cyclic codes, which are very easy to implement.

## Rate-compatible array LDPC codes

- **Status**: ✅
- **Reason**: array LDPC 기반 rate-compatible, permutation matrix로 효율적 디코더 구현 — 코드설계/HW(E/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1365191
- **Type**: conference
- **Published**: 2004
- **Authors**: A. Dholakia, S. Olcer
- **PDF**: https://ieeexplore.ieee.org/document/1365191
- **Abstract**: Rate-compatible low-density parity-check (LDPC) codes obtained from the class of array LDPC codes are presented. Our approach builds on the deterministic array LDPC code construction and allows efficient encodability across all codes in a rate-compatible family. Furthermore, the use of permutation matrices as building blocks of the parity-check matrix permits efficient decoder implementation. The suitability of rate-compatible array (RCA) LDPC codes for various applications is examined.

## Performance analysis and code design of low-density parity-check (LDPC) coded space-time transmit diversity (STTD) system

- **Status**: ✅
- **Reason**: DE 기반 irregular LDPC 부호 최적화/설계 기법(E)이 STBC 응용과 분리해 바이너리 LDPC 구성에 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1378926
- **Type**: conference
- **Published**: 2004
- **Authors**: A. Ohhashi, T. Ohtsuki
- **PDF**: https://ieeexplore.ieee.org/document/1378926
- **Abstract**: Space-time transmit diversity (STTD) and space-time block codes (STBC) are the attractive techniques for high bit-rate and high capacity transmission. Recently, low-density parity-check (LDPC) codes have attracted much attention as good error correcting codes achieving the near Shannon limit. Concatenation schemes of LDPC codes and STBC (LDPC-STBC), and turbo codes and STBC (turbo-STBC) have been proposed. The performance of the LDPC-STBC is better than that of the turbo-STBC on a flat Rayleigh fading channel. The performance of LDPC code can be analyzed by density evolution (DE). In this paper we analyze the performance of the LDPC-STBC by using DE. Also, we optimize the irregular LDPC codes for the LDPC-STBC by using DE. Furthermore, we evaluate the error rate performance of the optimized irregular LDPC codes and the regular LDPC codes for the LDPC-STBC. From the numerical and simulation results, we show that the LDPC-STBC with the irregular LDPC codes achieves better error rate performance than the LDPC-STBC with the regular LDPC codes.

## Grouping-and-shifting designs for structured LDPC codes with large girth

- **Status**: ✅
- **Reason**: E. grouping-and-shifting으로 large girth 구조적 바이너리 LDPC 신규 구성(작은 사이클 방지 정리) — NAND 코드설계 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1365275
- **Type**: conference
- **Published**: 2004
- **Authors**: J. Lu, J. M. F. Moura, U. Niesen
- **PDF**: https://ieeexplore.ieee.org/document/1365275
- **Abstract**: We introduce a method to design structured LDPC codes with large girth and flexible code rates. The method is simple to explain: we divide the nodes in the Tanner graph into groups and connect nodes in these groups according to a set of parameters called shifts. We derive a general theorem on the shifts to prevent small cycles. Simulations show that these codes, GS-LDPC codes, outperform random LDPC codes.

## Further results on finite-length scaling for iteratively decoded LDPC ensembles

- **Status**: ✅
- **Reason**: 유한길이 스케일링+error floor로 실용길이 LDPC 성능 분석 — 코드설계(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1365138
- **Type**: conference
- **Published**: 2004
- **Authors**: A. Amraoui, R. Urbanke, A. Montanari +1
- **PDF**: https://ieeexplore.ieee.org/document/1365138
- **Abstract**: The behavior of iteratively decoded low-density parity-check (LDPC) codes over the binary erasure channel in the so-called "waterfall region" is investigated and shows that the performance curves in this region follow a very basic scaling law. This scaling law, combined with previously known expressions for the error floor, yields a promising direction for analyzing the performance of irregular LDPC codes of practical lengths.

## LDPC product codes

- **Status**: ✅
- **Reason**: 인코딩 복잡도 낮춘 LDPC product code 구성 — 바이너리 코드설계 기여(E) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1359423
- **Type**: conference
- **Published**: 2004
- **Authors**: Zhang Qi, Ng Chun Sum
- **PDF**: https://ieeexplore.ieee.org/document/1359423
- **Abstract**: Low-density parity-check (LDPC) codes are well known for their abilities to achieve near Shannon channel capacity limit and low decoding complexity compared with the turbo decoder. However, their encoding complexities grow with the square of the code length. In this paper, we proposed a type of LDPC product codes, which can significantly lower the encoding complexity at the expense of slight degradation in error-rate performance as well as slight increase in decoding complexity

## Results on punctured LDPC codes

- **Status**: ✅
- **Reason**: 바이너리 LDPC 부호 설계 기여(punctured LDPC로 다중 레이트 단일 인코더/디코더 구성). MBIOS 채널 대상 코드 설계 기법(E)으로 NAND에 이식 가능.
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1405302
- **Type**: conference
- **Published**: 2004
- **Authors**: H. Pishro-Nik, F. Fekri
- **PDF**: https://ieeexplore.ieee.org/document/1405302
- **Abstract**: In this paper we study some fundamental properties of punctured LDPC codes. We first prove that for any ensemble of LDPC codes, there exists a puncturing threshold p*. We then find lower bounds on the achievable rates of punctured codes over general MBIOS channels. These bounds are satisfied by using only one encoder and decoder for all rates. We then prove that for any rates R/sub 1/ and R/sub 2/ satisfying 0 < R/sub 1/ < R/sub 2/ < 1, there exists an ensemble of LDPC codes with the following property. The ensemble can be punctured from rate R/sub 1/ to R/sub 2/ resulting in asymptotically good codes for all rates R/sub 1/ /spl les/ R /spl les/ R/sub 2/. Specifically, this implies that rates arbitrarily close to one are achievable via puncturing. We also show that punctured LDPC codes are as good as ordinary LDPC codes. For binary erasure channel (BEC) and arbitrary positive numbers R/sub 1/ < R/sub 2/ < 1, we prove the existence of the sequences of punctured LDPC codes that are capacity achieving for all rates R/sub 1/ /spl les/ R /spl les/ R/sub 2/. Based on the above observations, we then propose a method to design good punctured LDPC codes over a broad range of rates. The method is very simple and does not suffer from the performance degradation at high rates. Finally, we show that punctured codes might be useful for proof of the existence of capacity-achieving LDPC codes over memoryless binary-input output-symmetric channels.

## Performance studies of a multi-band OFDM system using a simplified LDPC code

- **Status**: ✅
- **Reason**: (3,k) 정규 LDPC를 부분병렬 디코더 구현에 맞춘 joint code/decoder 설계 — HW 아키텍처 이식 가능(D), 단 단순 구성일 수 있어 살림
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:1320999
- **Type**: conference
- **Published**: 2004
- **Authors**: Khiam-Boon Png, Xiaoming Peng, F. Chin
- **PDF**: https://ieeexplore.ieee.org/document/1320999
- **Abstract**: Ultra-wideband (UWB) is a promising radio technology for networks delivering extremely high data rates at short ranges. Multi-band orthogonal frequency division multiplexing (MB-OFDM) is a suitable solution to implement high speed data in ultra wideband spectrum by dividing the available spectrum into multiple bands. MB-OFDM achieves adaptability as well as high performance, low-power and low-cost characteristics through the usage of OFDM. Due to the importance of error correcting codes for OFDM systems, it is essential to employ a powerful error correcting code for the MB-OFDM system to improve the performance. Recently, low-density parity-check (LDPC) code has attracted great attention because it achieves bit error rate near to the Shannon limit. In this paper, we design and evaluate the performance of the MB-OFDM system using LDPC code. In order to simplify the implementation of the LDPC encoder and decoder, we introduce a joint code and decoder design approach to construct a class of (3, k)-regular LDPC code which exactly fits to a partly parallel decoder implementation. The simulations show that the performance of such a simplified LDPC coded MB-OFDM system is better than that of a convolutional coded MB-OFDM system, and is very close to that of the conventional LDPC coded MB-OFDM system. The implementation complexity of the simplified LDPC code is carefully examined subsequently in the paper.

## Regular low-density parity-check (LDPC) code with normalized and UMP BP-based algorithms on fast Rayleigh fading channel

- **Status**: ✅
- **Reason**: 정규화 BP-based / UMP min-sum 변형의 정규화 인자 이론 유도 — 이식 가능 디코더(C). 도메인은 Rayleigh이나 NF 도출 기법 떼어낼 수 있음
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1400508
- **Type**: conference
- **Published**: 2004
- **Authors**: A. Ohhashi, T. Ohtsuki
- **PDF**: https://ieeexplore.ieee.org/document/1400508
- **Abstract**: For the short regular LDPC codes, we derive the formula of the normalization factor (NF) theoretically by using the probability density function (pdf) of the initial likelihood information for the normalized BP-based algorithm. For the long regular LDPC codes, we derive the optimal NF for the normalized BP-based algorithm by using density evolution (DE). We also analyze the performance of the long regular LDPC codes with the UMP BP-based algorithm by using DE. From the numerical and simulation results, we show that the optimum NF for the short regular LDPC codes is different from that on the AWGN channel. We also show that for the short regular LDPC codes, the normalized BP-based algorithm outperforms the UMP BP-based algorithm, and has the performance very close to those of the BP algorithm. Furthermore, for the long regular LDPC codes, we show that the normalized BP-based algorithm outperforms the BP algorithm and the UMP BP-based algorithm. Therefore, for the short and long regular codes, the normalized BP-based algorithm is shown to be suitable as the decoding algorithm on the fast Rayleigh fading channel.

## Low complexity encoding of improved regular LDPC codes

- **Status**: ✅
- **Reason**: 저복잡도 인코딩 PABR 알고리즘 + Costas array 기반 sparse PCM 구성 + FPGA 구현 — 코드설계(E)/HW(D) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1400513
- **Type**: conference
- **Published**: 2004
- **Authors**: Su-Chang Chae, Yun-Ok Park
- **PDF**: https://ieeexplore.ieee.org/document/1400513
- **Abstract**: The existing encoding scheme for LDPC codes usually incurs too high complexity and should be changed to a low complexity encoding scheme. However, little consideration has been given to the LDPC encoder VLSI implementation. We consider low complexity encoding of regular LDPC codes, and we propose a pivoting and bit-reverse (PABR) algorithm to rapidly construct the parity-check matrix (PCM). And we consider improved regular LDPC codes in BER performance. We propose that the PCM is constructed with sub-matrixes which are made up of Costas arrays. The codes have sparse PCMs. They are designed to perform well when iteratively decoded with the sum-product decoding algorithm and to allow low complexity encoding. We show an approach to implementing the LDPC encoder using the PABR algorithm and improving BER performance using a PCM with Costas arrays. This paper then describes an FPGA implementation of regular LDPC encoder on a hardware platform for 4G mobile communication systems.

## A class of structured LDPC codes with large girth

- **Status**: ✅
- **Reason**: TS-LDPC structured codes with large-girth interleaver design plus reduced-complexity decoding — portable code design + decoder (C/E).
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1312524
- **Type**: conference
- **Published**: 2004
- **Authors**: J. Lu, J. M. F. Moura, U. Niesen
- **PDF**: https://ieeexplore.ieee.org/document/1312524
- **Abstract**: A class of structured LDPC codes-turbo-structured LDPC (TS-LDPC) codes-composed of two subtrees connected by an interleaver is introduced in this paper. TS-LDPC codes with good girth properties are easy to design: careful design of the interleaver component prevents short cycles in its Tanner graph. A methodology to design TS-LDPC codes with arbitrary column weight j/spl ges/2 and arbitrary girth is also presented. In addition, a complexity reduced decoding algorithm is described. Simulation results demonstrate the good performance of TS-LDPC codes when compared to random LDPC codes of the similar size and rate.

## Methodologies for designing LDPC codes using protographs and circulants

- **Status**: ✅
- **Reason**: E/D. protograph+circulant 기반 QC-LDPC 구성, circulant permutation으로 loop length 최대화 + 단순 HW 구현 지향 — NAND로 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1365273
- **Type**: conference
- **Published**: 2004
- **Authors**: J. Thorpe, K. Andrews, S. Dolinar
- **PDF**: https://ieeexplore.ieee.org/document/1365273
- **Abstract**: A method is presented for constructing LDPC codes with excellent performance, simple hardware implementation, low encoder complexity, and which can be concisely documented. The simple code structure is achieved by using a base graph, expanded with circulants. The base graph is chosen by computer search using simulated annealing, driven by density evolution's decoding threshold as determined by the reciprocal channel approximation. To build a full parity check matrix, each edge of the base graph is replaced by a circulant permutation, chosen to maximize loop length by using a Viterbi-like algorithm.

## Construction of quasicyclic LDPC codes based on the minimum weight codewords of Reed-Solomon codes

- **Status**: ✅
- **Reason**: E. RS 최소무게 코드워드 기반 QC-LDPC 대수적 구성법 — 부호 자체는 바이너리 QC-LDPC, 신규 구성 기법 이식 가능(애매하면 살림, Phase 3 재검토)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1365276
- **Type**: conference
- **Published**: 2004
- **Authors**: L. Chen, I. Djurdjevic, J. Xu
- **PDF**: https://ieeexplore.ieee.org/document/1365276
- **Abstract**: This work presents an algebraic method for constructing QC-LDPC codes based on the minimum-weight (m-w) codewords of Reed-Solomon (RS) codes over GF(q) with two information symbols.

## Minimum distance bounds of irregular QC-LDPC codes and their applications

- **Status**: ✅
- **Reason**: 불규칙 바이너리 QC-LDPC 최소거리 하한 도출 — 코드 구성/설계 관련(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1365348
- **Type**: conference
- **Published**: 2004
- **Authors**: Min-Ho Shin, Joon-Sung Kim, Hong-Yeop Song
- **PDF**: https://ieeexplore.ieee.org/document/1365348
- **Abstract**: We consider a design of quasicyclic LDPC codes which have irregular column weights. We derive bit-oriented bound and parity-oriented bound on the minimum distances of irregular quasicyclic codes using a similar technique to Tanner's simple lower bound

## Overlapped decoding for a class of quasi-cyclic LDPC codes

- **Status**: ✅
- **Reason**: QC-LDPC overlapped 디코딩으로 CNU/VNU 중첩, 클럭 50% 절감 HW 스케줄링 기법 — 디지털 디코더 HW 이식 가능(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:1363034
- **Type**: conference
- **Published**: 2004
- **Authors**: Sang-Min Kim, K. K. Parhi
- **PDF**: https://ieeexplore.ieee.org/document/1363034
- **Abstract**: In low-density parity-check (LDPC) code decoding with the iterative sum-product algorithm (SPA), due to the randomness of the parity-check matrix, H, the overlapping of the check node processing unit (CNU) and variable node processing unit (VNU) in the same clock cycle is difficult. The paper demonstrates that overlapped decoding can be exploited as long as the LDPC matrix is composed of identity matrices and their cyclic-shifted matrices, i.e., the parity-check matrix, H, belongs to a class of quasi-cyclic LDPC codes. It is shown that the number of clock cycles required for decoding can be reduced by 50% when overlapped decoding is applied to a (3,6)-regular LDPC code decoder.

## New research on unequal error protection (UEP) property of irregular LDPC codes

- **Status**: ✅
- **Reason**: Binary irregular LDPC code-design: weight-increasing parity-check matrix construction for UEP — a code construction technique potentially transferable (E).
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1286888
- **Type**: conference
- **Published**: 2004
- **Authors**: Xiumei Yang, Dongfeng Yuan, Piming Ma +1
- **PDF**: https://ieeexplore.ieee.org/document/1286888
- **Abstract**: A new scheme is proposed about how to make use of the unequal error protection (UEP) property of irregular low-density parity-check (LDPC) codes. By means of the construction of a weight-increasing parity-check matrix and systematic encoding, the mapping between the important information data and the elite bits of an irregular LDPC code becomes traceable and tractable. Thus, the inherent UEP property of irregular LDPC codes is not the theoretical interest any more. The proposed scheme makes it practical to implement UEP in system applications. Taking an irregular LDPC code with code length 10000 and code rate one half as an example, simulation results are presented over AWGN channels. The validity of the proposed scheme is verified by simulation.

## Joint code-encoder-decoder design for LDPC coding system VLSI implementation

- **Status**: ✅
- **Reason**: E/D: implementation-aware irregular LDPC code construction + encoder/decoder VLSI architecture, binary, 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1329290
- **Type**: conference
- **Published**: 2004
- **Authors**: Hao Zhong, Tong Zhang
- **PDF**: https://ieeexplore.ieee.org/document/1329290
- **Abstract**: This paper presents a design approach for low-density parity-check (LDPC) coding system hardware implementation by jointly conceiving irregular LDPC code construction and VLSI implementations of encoder and decoder. The key idea is to construct good irregular LDPC codes subject to two constraints that ensure the effective LDPC encoder and decoder hardware implementations. We propose a heuristic algorithm to construct such implementation-aware irregular LDPC codes that can achieve very good error correction performance. The encoder and decoder hardware architectures are correspondingly presented.

## Irregular rate-compatible LDPC codes for capacity-approaching hybrid-ARQ schemes

- **Status**: ✅
- **Reason**: 불규칙 rate-compatible LDPC 구성(puncturing/extending, 구조화 확장 H행렬), 바이너리 LDPC 코드설계 이식 가능(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1345016
- **Type**: conference
- **Published**: 2004
- **Authors**: M. Yazdani, A. H. Banihashemi
- **PDF**: https://ieeexplore.ieee.org/document/1345016
- **Abstract**: In this paper, we describe the construction method of a family of irregular rate-compatible low-density parity-check (LDPC) codes by a combination of puncturing and extending techniques. In particular, we introduce a suitable structure for the extended parity-check matrices which preserves the structure of LDPC codes during extensions. Based on this construction, a family of efficient rate-compatible linear-time encodable codes are generated from an optimized irregular mother code of rate 8/13 and information block length k=1024. The rates of the codes vary from 8/10 to 8/19 and employing them in a type-II hybrid ARQ scheme results in a throughput which is only 0.7 dB away from the Shannon limit. This improves over the existing schemes, based on turbo codes and LDPC codes, by up to 0.5 dB.

## Unified decoder architectures for repeat-accumulate and LDPC codes

- **Status**: ✅
- **Reason**: D/E: RA·LDPC 통합 디코더 아키텍처, architecture-aware 그래프 구조와 staggered 스케줄 — 바이너리 LDPC HW로 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1399188
- **Type**: conference
- **Published**: 2004
- **Authors**: M. M. Mansour
- **PDF**: https://ieeexplore.ieee.org/document/1399188
- **Abstract**: This paper investigates the design of high-performance decoder architectures for two promising codes-repeat-accumulate (RA) and LDPC codes-of large block length, in both regular and irregular forms. It addresses the decoder implementation complexity problem for such codes that stems from the "unstructured" nature of the code's underlying Tanner graph. To decouple the complexity of the decoder from the randomness of the code structure, we extend our earlier results on LDPC codes in M. M. Mansour et al., (2003) to RA codes and identify an architecture-aware (AA) graph structure that induces regularity features amenable to efficient and scalable decoder implementations. Design methods of AA-RA codes with structured graphs for which an iterative decoding algorithm performs well under message-passing are analogous to those for AA-LDPC codes. A unified decoder architecture capable of decoding both AA-RA and LDPC codes based on the staggered decoding schedule of M. M. Mansour et al. (2003) is introduced. Architectural optimizations that address the latency, memory overhead and implementation complexity problems typical of iterative decoders for long codes are also investigated.

## Performance of generalized soft-output demapper for LDPC-CFMT system over frequency selective fading channel

- **Status**: ✅
- **Reason**: 노이즈 분산 추정 불필요한 신규 soft 디코딩 메트릭(M-PSK/M-QAM) 제안 — LLR 생성/양자화 기법으로 NAND LLR 메트릭에 이식 검토 가치(C), 애매하여 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1321917
- **Type**: conference
- **Published**: 2004
- **Authors**: Qiang Li, Guangguo Bi, Peng Du
- **PDF**: https://ieeexplore.ieee.org/document/1321917
- **Abstract**: In this paper, we proposed the LDPC coded FMT systems and showed that the LDPC codes are effective to improve the bit error rate of FMT in frequency selective fading channel. When the LDPC codes are used for the FMT systems in mobile communications, especially in high bit rate applications, high bandwidth efficiency is required, and thus the high-order modulation is preferred. In this paper, we also propose a new soft decision metric generation method, which obviates the need of the noise variance estimation, for M-PSK/M-QAM modulation over frequency selective fading channel. Computer simulation indicates that there is no performance loss with our new metric, but the complexity of implementation is reduced.

## Estimating LDPC codeword error rates via importance sampling

- **Status**: ✅
- **Reason**: 바이너리 LDPC codeword error rate importance sampling 추정 — error floor 평가 기법, 코드설계 보조(E), 애매하여 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1365513
- **Type**: conference
- **Published**: 2004
- **Authors**: B. Xia, W. E. Ryan
- **PDF**: https://ieeexplore.ieee.org/document/1365513
- **Abstract**: This paper proposes an importance sampling design for the codeword error rate estimation of low-density parity-check codes. An error set partitioning method is introduced to reduce the error boundary complexity and to improve the simulation efficiency. This is a follow-up to the work in (B. Xia et al., 2003).

## Efficient DSP implementation of an LDPC decoder

- **Status**: ✅
- **Reason**: LDPC BP 디코더의 DSP 구현 + 단순화 디코딩 알고리즘 + 조기종료 정지기준 — 이식 가능 디코더/HW 기법(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1326914
- **Type**: conference
- **Published**: 2004
- **Authors**: G. Lechner, J. Sayir, M. Rupp
- **PDF**: https://ieeexplore.ieee.org/document/1326914
- **Abstract**: We present a high performance implementation of a belief propagation decoder for decoding low-density parity-check (LDPC) codes on a fixed point digital signal processor. A simplified decoding algorithm was used and a stopping criteria for the iterative decoder was implemented to reduce the average number of required iterations. This leads to an implementation with increased throughput compared to other implementations of LDPC codes or turbo codes. This decoder is able to decode at 5.4 Mbps on a Texas Instruments TMS320C64xx DSP running at 600 MHz.

## Design and implementation of a parameterizable LDPC decoder IP core

- **Status**: ✅
- **Reason**: 임의 H에 대한 병렬 log-domain LDPC 디코더 ASIC IP; 메시지 해상도·log 근사 트레이드오프 다룸, D 디지털 HW + C 양자화 기법
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:1314940
- **Type**: conference
- **Published**: 2004
- **Authors**: G. Murphy, E. M. Popovici, R. Bresnan +2
- **PDF**: https://ieeexplore.ieee.org/document/1314940
- **Abstract**: This paper presents a design methodology that quickly enables the design and implementation of a fully parallel log-domain LDPC decoder based on any parity check matrix. A simulation method to perform an analysis of an arbitrary LDPC code is presented and then extended to predict the actual performance of the final hardware implementation. The design trade-offs due to parameterizable terms such as message resolution and approximation of the log functions are discussed. Finally using the presented design methodology an IP core is generated (using a randomly chosen parity check matrix H). Results for this IP core are presented for an ASIC implementation using a 0.35 /spl mu/m CMOS technology.

## A hybrid decoding approach for LDPC coded MIMO-OFDM systems

- **Status**: ✅
- **Reason**: C: LDPC MIMO-OFDM 하드+반복 2단계 하이브리드 디코딩으로 복잡도 감소 — 디코더 스케줄링 기법 이식 가능(애매하면 in)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1399326
- **Type**: conference
- **Published**: 2004
- **Authors**: Yan Xin, S. A. Mujtaba
- **PDF**: https://ieeexplore.ieee.org/document/1399326
- **Abstract**: In this paper, we propose a novel decoding approach for coded multiple input multiple output (MIMO) orthogonal frequency division multiplexing (OFDM) systems that employ low-density parity-check (LDPC) codes. In the proposed decoding approach, a code word is decoded in two steps, hard decoding and iterative decoding, based on the log-likelihood ratios of coded bits. We show that compared with conventional decoding approaches for LDPC coded MIMO-OFDM systems, the proposed decoding approach not only delivers a considerable reduction in decoding complexity but also maintains comparable performance.

## On unequal error protection LDPC codes based on Plotkin-type constructions

- **Status**: ✅
- **Reason**: E — Plotkin 구성 기반 UEP 바이너리 LDPC 다단 디코딩·구조/랜덤 성분 결합. 코드 설계 기법 이식 가능(경계: UEP는 NAND 직결 아니나 살림)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1377996
- **Type**: conference
- **Published**: 2004
- **Authors**: 
- **PDF**: https://ieeexplore.ieee.org/document/1377996
- **Abstract**: A family of unequal error-protection (UEP) low-density parity-check (LDPC) codes, based on Plotkin-type constructions, is introduced. The codes are decoded in multiple stages in such a manner that the order of decoding determines the level of error protection. The level of UEP among the code bits can be further increased by properly combining structured and random-like LDPC component codes with carefully chosen properties, and by using some new reliability features. The proposed scheme also offers a good trade-off between code performance on the one hand and encoding/decoding and storage complexity on the other. To the best of our knowledge, the proposed approach represents the first iterative UEP method with analytically provable properties.

## New implementation for the scalable LDPC-decoders

- **Status**: ✅
- **Reason**: 확장형 LDPC 디코더 trellis/BCJR 기반 신뢰도 계산, 스케줄·메모리 절감·permutation matrix HW(C/D) — 디지털 디코더 아키텍처 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1387971
- **Type**: conference
- **Published**: 2004
- **Authors**: Li Yanping, Moon Ho Lee, GiYean Hwang +1
- **PDF**: https://ieeexplore.ieee.org/document/1387971
- **Abstract**: Trellis decoding of regular and irregular low-density parity-check (LDPC) codes and the corresponding decoder architectures are considered. Moreover, we propose a new approach for computing reliability metrics based on the BCJR algorithm that reduces the message switching activity in the decoder compared to existing approaches. The trellis decoding schedule is employed to decode LDPC codes using constituent soft-input soft-output (SISO) decoders that communicate through interleavers. The proposed tunable schedule exhibits a faster convergence behavior (up to 50% fewer iterations), and hence lower decoding latency, than the commonly employed two-phase schedule, and the corresponding decoder architecture has a significantly reduced memory requirement. Improvement in decoding gain (up to an order of magnitude for moderate-to-high SNR and small number of iterations) is achieved and structural regularity features in the form of permutation matrices further reduce interconnect complexity and improve decoding throughput.

## On construction of rate-compatible low-density parity-check codes

- **Status**: ✅
- **Reason**: Deterministic rate-compatible binary LDPC construction via puncturing/extending — portable code design (E).
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1312525
- **Type**: conference
- **Published**: 2004
- **Authors**: M. Yazdani, A. H. Banihashemi
- **PDF**: https://ieeexplore.ieee.org/document/1312525
- **Abstract**: This paper deals with the problem of devising an efficient framework for constructing rate-compatible low-density parity-check (RC-LDPC) codes. We present a deterministic framework for constructing a family of linear-time encodable RC-LDPC codes from a mother code using puncturing and extending. Application of the proposed construction to a type-II hybrid ARQ scheme with information block length k=1024 and code rates 8/19 to 8/10, using an optimized irregular mother code of rate 8/13, results in a throughput which is only about 0.7dB away from Shannon limit. This outperforms existing similar schemes based on turbo codes and LDPC codes by up to 0.5dB.

## A reduced complexity decoder architecture via layered decoding of LDPC codes

- **Status**: ✅
- **Reason**: layered BP 디코딩 + 메모리/로직 50% 절감 HW 아키텍처 — NAND LDPC 디코더 HW로 이식 가능(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1363033
- **Type**: conference
- **Published**: 2004
- **Authors**: D. E. Hocevar
- **PDF**: https://ieeexplore.ieee.org/document/1363033
- **Abstract**: We apply layered belief propagation decoding to our previously devised irregular partitioned permutation LDPC codes. These codes have a construction that easily accommodates a layered decoding and we show that the decoding performance is improved by a factor of two in the number of iterations required. We show how our previous flexible decoding architecture can be adapted to facilitate layered decoding. This results in a significant reduction in the number of memory bits and memory instances required, in the range of 45-50%. The faster decoding speed means the decoder logic can also be reduced by nearly 50% to achieve the same throughput and error performance. In total, the overall decoder architecture can be reduced by nearly 50%.

## An efficient message-passing schedule for LDPC decoding

- **Status**: ✅
- **Reason**: LDPC serial(layered) 메시지패싱 스케줄로 수렴반복 절반 감소 — 부호 비의존 디코더 기법, NAND BP에 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1361130
- **Type**: conference
- **Published**: 2004
- **Authors**: E. Sharon, S. Litsyn, J. Goldberger
- **PDF**: https://ieeexplore.ieee.org/document/1361130
- **Abstract**: An efficient decoding schedule for low-density parity-check (LDPC) codes that outperforms the conventional approach, in terms of both complexity and performance, is presented. Conventionally, in each iteration, all symbol nodes and, subsequently, all the check nodes, send messages to their neighbors ("flooding schedule"). In contrast, in the proposed method, the updating of nodes is performed according to a serial schedule which propagates the information twice as fast. A density evolution (DE) algorithm for asymptotic analysis of the new schedule is derived, showing that, when working near the code's capacity, the decoder converges in approximately half the number of iterations. In addition, a concentration theorem is proved, showing that, for a randomly chosen serial schedule, code graph, and decoder input, the decoder's performance approaches its expected one as predicted by the DE algorithm, when the code length increases.

## Density evolution method and threshold decision for irregular LDPC codes

- **Status**: ✅
- **Reason**: E/C: 비정규 LDPC 밀도진화 분석·임계값 결정(이산화 DE, 가우시안 근사)으로 차수분포 최적화 — 코드설계 기법 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1345932
- **Type**: conference
- **Published**: 2004
- **Authors**: Wang Lin, Xiao Juan, Guanrong Chen
- **PDF**: https://ieeexplore.ieee.org/document/1345932
- **Abstract**: Density evolution is a new method for analyzing the asymptotic performance of network capability approaching error-correcting codes. For irregular LDPC codes with message-passing decoding, the density evolution method can track the messages to find out the threshold, enabling optimization of the degree distribution. In this paper, the principle of density evolution combined with the decoding process is firstly explored. Then, two algorithms for programming the evolution proceeding are discussed: the discretized density evolution and the Gaussian approximation, as well as their application conditions. Finally, simulation results are presented.

## LDPC codes over channels with memory

- **Status**: ✅
- **Reason**: 메모리 채널용 LDPC: 코드제약+채널을 합친 팩터그래프 sum-product 디코딩 — NAND의 셀간간섭/메모리 채널 결합 BP 디코더로 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1312603
- **Type**: conference
- **Published**: 2004
- **Authors**: G. Colavolpe
- **PDF**: https://ieeexplore.ieee.org/document/1312603
- **Abstract**: In this paper, the problem of detection and decoding of low-density parity-check (LDPC) codes transmitted over channels with memory is addressed. A general method to build a factor graph which takes into account both the code constraints and the channel behavior is described and the a posteriori probabilities of the transmitted symbols are derived by using the sum-product algorithm. A noncoherent channel and a flat fading channel are considered as examples of application.

## Analysis of the cycle-structure of LDPC codes based on Latin squares

- **Status**: ✅
- **Reason**: Latin square 기반 구조적 바이너리 LDPC, 순열블록 girth/최소거리 보장+6-cycle 제거 shortening, 저장량 절감 — QC형 코드설계+사이클 제거 기법(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1312607
- **Type**: conference
- **Published**: 2004
- **Authors**: O. Milenkovic, S. Laendner
- **PDF**: https://ieeexplore.ieee.org/document/1312607
- **Abstract**: In this paper, we introduce a family of structured low-density parity-check (LDPC) codes based on a class of idempotent, symmetric Latin and modified Latin squares. The parity-check matrices of the codes have a block structure with permutation blocks which insures that both their corresponding girth and minimum distance are at least equal to six. The storage requirement for codes from this class is reduced to only one parameter. We also propose a structured method for shortening the codes by removing columns that break a large number of cycles of length six. The storage requirements for the codes obtained using the described procedure consist in memorizing only two integers, while their performance under iterative decoding matches that of random-like codes of comparable length.

## Accelerating LDPC decoding using multiple-cycle eigenmessages

- **Status**: ✅
- **Reason**: C: eigenmessage 기반 다중 사이클 고정점 BP 가속 — 부호 비의존 메시지패싱 개선, 바이너리 LDPC BP로 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1399319
- **Type**: conference
- **Published**: 2004
- **Authors**: J. S. Crockett, T. K. Moon, J. H. Gunther +1
- **PDF**: https://ieeexplore.ieee.org/document/1399319
- **Abstract**: The eigenmessage decoder O. Chauhan et al. (2003) expresses a degree of nonlocality in a message passing decoder by representing an entire cycle in a single linear equation. The eigenvector for the linear message passing matrix represents a fixed point of the message passing algorithm around a cycle and has been shown to significantly decrease the number of iterations required for low-density parity-check (LDPC) decoding using message passing. In this paper, we extend the eigenmessage idea to simultaneously solving for a fixed point of multiple cycles. The representation is thus nonlocal over a broader section of the graph. This multiple-cycle eigenmessage algorithm shows improvement over traditional belief propagation (BP) methods. We present and compare results for the new algorithm and consider possible variations.

## Design semialgebraic LDPC codes on u/u+v construction

- **Status**: ✅
- **Reason**: Semialgebraic LDPC via u/u+v construction targeting large girth/min distance with iterative decoding; binary code-design technique (E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1414689
- **Type**: conference
- **Published**: 2004
- **Authors**: Dong Min Lee, MoonHo Lee, Sarm Gu Cho
- **PDF**: https://ieeexplore.ieee.org/document/1414689
- **Abstract**: In this paper, semialgebraic low-density parity-check (SA-LDPC) codes on u/u+v construction are proposed. The codes by the u/u+v construction have the extended error capacity for additional Hamming weight. It is a simple way to construct a large size block code using smaller ones. Semialgebraic low-density parity-check codes in this class have a large girth and good minimum distances. They perform well with iterative decoding.

## Fast convergence decoding scheme for regular LDPC codes

- **Status**: ✅
- **Reason**: 정규 LDPC용 노드 그룹핑·스케줄링 기반 빠른 수렴 BP; 반복수 감소 디코더 기법, NAND LDPC 디코더에 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1439096
- **Type**: conference
- **Published**: 2004
- **Authors**: Jaebum Kim, Namsik Kim, Hyuncheol Park
- **PDF**: https://ieeexplore.ieee.org/document/1439096
- **Abstract**: We propose a new belief propagation (BP) decoding algorithm for fast convergence decoding of regular LDPC codes. The fast convergence is achieved by grouping and scheduling updates of nodes on a bipartite-graph without additional computations or approximations. For this reason, the proposed algorithm can be applied to a serially constructed decoder, and can reduce the power consumption and decoding delay of the decoder. Simulation results show that the convergence speed of the proposed algorithm depends on the degree, d/sub v/, of the variable-nodes of the bipartite-graph, and the average number of iterations of the decoder can be reduced to (d/sub v/-1)/d/sub v/ by using the proposed algorithm without performance degradation or additional computation.

## Implementation of an LDPC decoder on a vector signal processor

- **Status**: ✅
- **Reason**: D: 벡터 신호프로세서 기반 sum-product 병렬 디코더, 면적-처리량 트레이드오프 — 디지털 병렬 LDPC HW 이식 가능
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:1399193
- **Type**: conference
- **Published**: 2004
- **Authors**: G. Lechner, A. Bolzer, J. Sayir +1
- **PDF**: https://ieeexplore.ieee.org/document/1399193
- **Abstract**: A parallel processor architecture-a vector signal processor (VSP), which consists of independent computation units is presented. This architecture is used to implement the sum-product algorithm to decode low-density parity-check codes. The VSP is well suited for this parallel decoding algorithm which results in a scalable decoder that allows a tradeoff between chip area and data throughput. With increasing number of computation units a data throughput of up to 36.1 MBit per second can be achieved which outperforms existing implementations on digital signal processors.

## Geometry based designs of LDPC codes

- **Status**: ✅
- **Reason**: 기하 기반 column-weight-3 girth-8/10 LDPC 구성, error floor 개선, 데이터저장 명시 — 바이너리 LDPC 코드설계 기법(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1312604
- **Type**: conference
- **Published**: 2004
- **Authors**: Haotian Zhang, J. M. F. Moura
- **PDF**: https://ieeexplore.ieee.org/document/1312604
- **Abstract**: In this paper we construct three types of low-density parity-check codes with column weight j = 3 based on geometries in graphical models. Low-density parity-check codes with j > 2 are desired because their minimum distance improves linearly with the code block length n. The codes we present here have girth 8 and girth 10. All codes are regular and well-structured. These codes have flexible block lengths and code rates, and may be used in the area of communications and data storage. Our simulation results show that they have better bit-error-rate decoding performance and lower error floors in additive white Gaussian noise channels than randomly constructed low-density parity-check codes.

## Analytical derivation of EXIT charts for simple block codes and for LDPC codes using information combining

- **Status**: ✅
- **Reason**: EXIT chart 분석을 정보결합으로 LDPC에 적용 — 바이너리 LDPC 코드설계/수렴분석 기법 이식 가능(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7079706
- **Type**: conference
- **Published**: 2004
- **Authors**: I. Land, P. A. Hoeher, J. Huber
- **PDF**: https://ieeexplore.ieee.org/document/7079706
- **Abstract**: The extrinsic information transfer (EXIT) chart describes the input-output behavior of a decoder by means of the mapping from a-priori information and channel information to extrinsic information. In this paper, we consider single parity check and repetition codes over binary-input symmetric memoryless channels. Using the concept of information combining, we derive bounds on the extrinsic information for these codes, which depend only on the a-priori information and on the channel information, but not on the channel models. The bounds are applied to the EXIT charts of these codes and to the EXIT charts of low-density parity-check codes.

## Rate-compatible low-density parity-check codes for digital subscriber lines

- **Status**: ✅
- **Reason**: Rate-compatible array LDPC with generic decoder architecture and algebraic construction — portable binary LDPC code design/HW (D/E).
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1312522
- **Type**: conference
- **Published**: 2004
- **Authors**: A. Dholakia, S. Olcer
- **PDF**: https://ieeexplore.ieee.org/document/1312522
- **Abstract**: Rate-compatible low-density parity-check (LDPC) codes obtained from the class of array LDPC codes are presented. The design methodology described herein retains practical advantages of array LDPC codes such as excellent performance and efficient encodability across all the codes in a rate-compatible family. Different codes in the rate-compatible family can be specified by a small number of parameters and constructed algebraically with a small amount of preprocessing. The rate-compatible codes can be decoded using a generic decoder architecture, leading to efficient implementations. These properties make the codes attractive for use in DSL systems that need to support a large number of code parameters to cope with channel variability.

## A throughput/complexity analysis for the VLSI implementation of LDPC decoder

- **Status**: ✅
- **Reason**: VLSI complexity analysis of binary LDPC decoder, parallel vs serial architectures, throughput/power (category D HW)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:1433805
- **Type**: conference
- **Published**: 2004
- **Authors**: L. Fanucci, F. Rossi
- **PDF**: https://ieeexplore.ieee.org/document/1433805
- **Abstract**: This paper presents an analysis of the VLSI complexity of different LDPC decoder implementations. Both fully parallel and serial solutions are considered and compared in terms of architectural issues, hardware complexity, power consumption and supported throughput. To provide numeric results a 1/2 rate, (3,6) regular LDPC code with a 2048 codeword has been considered and area complexity estimations have been carried out with reference to a 0.18 /spl mu/m standard-cell CMOS technology.

## On regular quasicyclic LDPC codes from binomials

- **Status**: ✅
- **Reason**: 이항식 기반 정규 바이너리 QC-LDPC 구성으로 최소거리 향상 — 코드 설계(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1365314
- **Type**: conference
- **Published**: 2004
- **Authors**: R. Smarandache, P. O. Vontobel
- **PDF**: https://ieeexplore.ieee.org/document/1365314
- **Abstract**: In the past, several authors have considered quasicyclic LDPC codes whose circulant matrices in the parity-check matrix are cyclically shifted identity matrices. By composing a parity-check matrix not only with such matrices but also with sums of two cyclically shifted identity matrices and with zero matrices, one can increase the minimum distance while keeping the same regularity. Specifically, whereas for (3, 4)-regular codes in the first class the best minimum distance is 24, the best minimum distance in the second class is 32. We give examples of codes that achieve these bounds.

## Scaleable check node centric architecture for LDPC decoder

- **Status**: ✅
- **Reason**: 확장 가능한 check-node 중심 LDPC 디코더 아키텍처 — 디지털 HW(D) 병렬/스케일 기법, 이식 가능
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:1328972
- **Type**: conference
- **Published**: 2004
- **Authors**: R. Singhal, G. S. Choi, N. Mickler +1
- **PDF**: https://ieeexplore.ieee.org/document/1328972
- **Abstract**: Low density parity check codes are a popular class of linear block codes for forward error correction in communication channels. Recent years have seen a lot of work towards the development of decoding architectures for these codes. The architectures range from completely parallel to completely serial. While the parallel architectures have a high throughput, they have a large hardware resource requirement. On the other hand, although the serial architectures are very efficient in terms of hardware requirement, they suffer from low throughput. This paper presents a novel scalable check node centric architecture with a 1.5 Gbps throughput. The throughput may be further increased by using more readily scalable data-paths which have a individual throughput of 0.5 Gbps.

## Reliability-based schedule for decoding low-density parity-check codes

- **Status**: ✅
- **Reason**: Reliability-based message-passing schedule for LDPC decoding improving speed/performance — portable decoder scheduling technique (C).
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1312528
- **Type**: conference
- **Published**: 2004
- **Authors**: A. Nouh, A. H. Banihashemi
- **PDF**: https://ieeexplore.ieee.org/document/1312528
- **Abstract**: A reliability-based message-passing schedule for iterative decoding of low-density parity-check codes is proposed. Simulation results for bit-flipping algorithms (with binary messages) show that reliability-based schedule can provide considerable improvement in performance and decoding speed over the so-called flooding (parallel) schedule as well as the existing graph-based schedules. The cost associated with this improvement is negligible and is equivalent to having a 2-bit representation for initial messages, instead of the standard 1-bit for hard-decision algorithms, only at the first iteration (all the exchanged messages are still binary).

## Puncturing for finite length low-density parity-check codes

- **Status**: ✅
- **Reason**: 유한길이 LDPC puncturing 알고리즘으로 rate 적응 — 코드설계(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1365189
- **Type**: conference
- **Published**: 2004
- **Authors**: J. Ha, J. Kim, S. W. McLaughlin
- **PDF**: https://ieeexplore.ieee.org/document/1365189
- **Abstract**: In this paper we study and propose an algorithm to puncture finite length low density parity check (LDPC) codes (Ha, J, et al., 2002). The introduced puncturing criterion results in good performance (for 1024 and 4096 bits) when compared with both random puncturing and dedicated LDPC codes, i.e. unpunctured codes designed for a given rate. The comparison also shows that the proposed punctured LDPC codes have better block-error rates than the dedicated codes because of longer effective block lengths of the high-rate puncturing. Although we apply the idea for regular LDPC codes, we can easily modify the idea for irregular LDPC codes.

## Belief-propagation with information correction: improved near maximum-likelihood decoding of low-density parity-check codes

- **Status**: ✅
- **Reason**: 채널정보 보정 기반 BP 디코더 개선(워터폴+error floor), 부호 비의존적 BP 개선 기법으로 바이너리 LDPC에 이식 가능(C).
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1365380
- **Type**: conference
- **Published**: 2004
- **Authors**: N. Varnica, M. Fossorier
- **PDF**: https://ieeexplore.ieee.org/document/1365380
- **Abstract**: We propose an improved beliefpropagation (BP) decoder for low-density parity-check (LDPC) codes based on channel information correction. We show that our algorithm achieves sizeable performance gains (in waterfall and error floor regions) compared to the standard BP decoder. We verify by examples that the proposed decoder almost achieves the maximum-likelihood decoding performance for short LDPC codes.

## Bayesian and nonBayesian methods for iterative joint decoding and detection in the presence of phase noise

- **Status**: ✅
- **Reason**: 위상잡음 하 joint 반복 디코딩/검출(EM+sum-product) — 부호비의존 메시지패싱 기법(C), 애매하면 in
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1365166
- **Type**: conference
- **Published**: 2004
- **Authors**: G. Colavolpe, A. Barbieri, G. Caire +1
- **PDF**: https://ieeexplore.ieee.org/document/1365166
- **Abstract**: This paper proposes new algorithms for joint iterative decoding and parameter estimation in Bayesian and nonBayesian method. The low-density parity-check (LDPC) codes in the presence of phase noise is focused in this paper. The nonBayesian algorithm for an unknown phase channel is based on the application of the expectation-maximization (EM) algorithm. The proposed Bayesian algorithms are obtained as an application of the sum-product algorithm to the factor graph. Comparing the performance of the considered algorithms in the case of LDPC code, the EM-KL (EM-Karhunen-Loeve) algorithm performs better than EM-SW (sliding window) algorithm.

## Low-density mirror-concatenated codes: a generalization of irregular repeat-and- accumulate codes

- **Status**: ✅
- **Reason**: LDMC가 LDPC와 등가임을 보인 코드 구성 관점, IRA 일반화 — 바이너리 LDPC 구성 기여(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1365543
- **Type**: conference
- **Published**: 2004
- **Authors**: S. Dolinar, K. Andrews
- **PDF**: https://ieeexplore.ieee.org/document/1365543
- **Abstract**: Low-density mirror-concatenated (LDMC) codes are defined and shown to be equivalent to low-density parity-check (LDPC) codes. As a generalization of irregular repeat-and-accumulate (IRA) codes, LDMC codes offer a slightly different, but potentially useful, perspective on LDPC codes as concatenated codes.

## Rate-compatible low-density parity-check codes

- **Status**: ✅
- **Reason**: rate-compatible LDPC 구성(차수분포+puncturing, error floor 억제) — 코드설계(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1365190
- **Type**: conference
- **Published**: 2004
- **Authors**: T. Tian, C. Jones, J. D. Villasenor
- **PDF**: https://ieeexplore.ieee.org/document/1365190
- **Abstract**: Rate-compatible coding is appropriate for communication systems that experience a range of operating SNRs but seek to adhere to a single underlying codec structure. This paper constructs rate-compatible low-density parity-check (LDPC) codes by carefully selecting degree distributions, followed by a combination of information nulling and parity puncturing. Techniques that suppress error floors are included as part of the construction methodology.

## LP decoding corrects a constant fraction of errors

- **Status**: ✅
- **Reason**: LP 디코딩의 오류정정 보장 분석 — 이식 가능 디코더 알고리즘(C), 바이너리 LDPC
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1365106
- **Type**: conference
- **Published**: 2004
- **Authors**: J. Feldman, T. Malkin, R. A. Servedio +2
- **PDF**: https://ieeexplore.ieee.org/document/1365106
- **Abstract**: We show that for low-density parity-check (LDPC) codes with sufficient expansion, the linear programming (LP) decoder corrects a constant fraction of errors.

## Low-density parity-check codes with fast decoding convergence speed

- **Status**: ✅
- **Reason**: BEC용이나 디코딩 반복수 감소 위한 바이너리 LDPC 패리티검사 설계 — 수렴속도 코드설계(E), 애매하므로 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1365311
- **Type**: conference
- **Published**: 2004
- **Authors**: X. Ma, E. Yang
- **PDF**: https://ieeexplore.ieee.org/document/1365311
- **Abstract**: In this paper, the design of low-density parity-check (LDPC) codes for binary erasure channels (BEC) with less number of decoding iterations in the parallel message-passing decoding is presented. We consider only the cases where the capacity is approached with sufficiently low parity-check matrix density.

## Approximate algorithms for computing the minimum distance of low-density parity-check codes

- **Status**: ✅
- **Reason**: 바이너리 LDPC 최소거리 근사계산 알고리즘 — error floor/코드설계 평가에 이식 가능(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1365512
- **Type**: conference
- **Published**: 2004
- **Authors**: X. . -Y. Hu, M. P. C. Fossorier, E. Eleftheriou
- **PDF**: https://ieeexplore.ieee.org/document/1365512
- **Abstract**: We propose a family of randomized approximate algorithms, called nearest nonzero codewords search (NNCS), for computing the minimum distance of low-density parity-check (LDPC) codes, including Gallager-type and finite-geometry-type codes.

## A practical analysis of low-density parity-check erasure codes for wide-area storage applications

- **Status**: ✅
- **Reason**: 스토리지용 바이너리 LDPC erasure code의 유한길이 개별 코드 생성·분석(B/E), 코드 설계 실무 고찰 이식 가능성
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1311882
- **Type**: conference
- **Published**: 2004
- **Authors**: J. S. Plank, M. G. Thomason
- **PDF**: https://ieeexplore.ieee.org/document/1311882
- **Abstract**: As peer-to-peer and widely distributed storage systems proliferate, the need to perform efficient erasure coding, instead of replication, is crucial to performance and efficiency. Low-density parity-check (LDPC) codes have arisen as alternatives to standard erasure codes, such as Reed-Solomon codes, trading off vastly improved decoding performance for inefficiencies in the amount of data that must be acquired to perform decoding. The scores of papers written on LDPC codes typically analyze their collective and asymptotic behavior. Unfortunately, their practical application requires the generation and analysis of individual codes for finite systems. This paper attempts to illuminate the practical considerations of LDPC codes for peer-to-peer and distributed storage systems. The three main types of LDPC codes are detailed, and a huge variety of codes are generated, then analyzed using simulation. This analysis focuses on the performance of individual codes for finite systems, and addresses several important heretofore unanswered questions about employing LDPC codes in real-world systems.

## A flexible hardware encoder for low-density parity-check codes

- **Status**: ✅
- **Reason**: Flexible FPGA hardware encoder for binary LDPC with linear encoding complexity and parallelism (D); portable to NAND LDPC HW.
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:1364621
- **Type**: conference
- **Published**: 2004
- **Authors**: D. . -U. Lee, W. Luk, C. Wang +1
- **PDF**: https://ieeexplore.ieee.org/document/1364621
- **Abstract**: We describe a flexible hardware encoder for regular and irregular low-density parity-check (LDPC) codes. Although LDPC codes achieve better performance and lower decoding complexity than turbo codes, a major drawback of LDPC codes is their apparently high encoding complexity. Using an efficient encoding method proposed by Richardson and Urbanke, we present a hardware LDPC encoder with linear encoding complexity. The encoder is flexible, supporting arbitrary H matrices, rates and block lengths. An implementation for a rate 1/2 irregular length 2000 LDPC code encoder on a Xilinx Virtex-II XC2V4000-6 FPGA takes up 4% of the device. It runs at 143 MHz and has a throughput of 45 million codeword bits per second (or 22 million information bits per second) with a latency of 0.18 ms. The performance can be improved by exploiting parallelism: several instances of the encoder can be mapped onto the same chip to encode multiple message blocks concurrently. An implementation of 16 instances of the encoder on the same device at 82 MHz is capable of 410 million codeword bits per second, 80 times faster than an Intel Pentium-lV 2.4 GHz PC.

## Iterative decoding algorithm of lattices

- **Status**: ✅
- **Reason**: min-sum 알고리즘을 일반화한 반복 디코딩 기법 — 디코더 복잡도 분석이 바이너리 LDPC min-sum 디코더로 이식 검토 여지 있어 애매하므로 살림(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1349667
- **Type**: conference
- **Published**: 2004
- **Authors**: M. R. Sadeghi, A. H. Banihashemi, D. Panario
- **PDF**: https://ieeexplore.ieee.org/document/1349667
- **Abstract**: The so-called min-sum algorithm for iterative decoding of low-density parity-check (LDPC) codes is generalized to decode lattices. An upper bound on the decoding complexity per iteration is derived, and for LDPC lattices constructed by Construction D' and using a nested sequence of LDPC codes, exact values for computational complexity are also given. We show that iterative decoding of LDPC lattices has a reasonably low complexity such that lattices with dimensions of a few thousands can be easily decoded.

## Lowering the error floors of irregular high-rate LDPC codes by graph conditioning

- **Status**: ✅
- **Reason**: ACE 그래프 컨디셔닝으로 고율 불규칙 LDPC error floor 저감 — 코드설계(E) 직접 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1400516
- **Type**: conference
- **Published**: 2004
- **Authors**: Wen-Yen Weng, A. Ramamoorthy, R. D. Wesel
- **PDF**: https://ieeexplore.ieee.org/document/1400516
- **Abstract**: This paper applies a graph conditioning algorithm, called the approximate cycle extrinsic message degree (ACE) algorithm, to design high-rate (R/spl ges/1/2) irregular LDPC codes. The algorithm was shown to be an effective tool to lower the error floors of lower-rate (R/spl les/1/2) LDPC codes. However, for high-rate LDPC codes, due to the large number of degree-2 variable nodes in the optimal degree distribution, the error floor is high and it is more difficult to condition the graph. By constraining the number of degree-2 nodes, we found that the ACE algorithm can dramatically lower the error floor with little compromise of the threshold. A rate-3/4, length-10688 LDPC code is proposed whose AWGN channel performance is within 0.67 dB of the Shannon limit at BER=10/sup -5/ and its error floor is lower than 10/sup -7/. Compared to existing semi-regular codes which lower the floor by adopting non-optimal degree distributions, our graph-conditioned codes provides 0.38 dB of performance improvement at BER=10/sup -5/. The same design criteria also apply well to medium-length LDPC code design and are suitable for rate-compatible applications using the information-nulling technique. The rate-compatible scheme has consistently good thresholds and low error floors for 1/2/spl les/ R/spl les/ 8/9.

## The effect of noise estimation error in the LDPC decoding performance

- **Status**: ✅
- **Reason**: LDPC 입력 양자화 비트수 최적화 및 채널신뢰도 Lc/잡음분산 추정오차 영향 — LLR 양자화·HW 복잡도 기법(A/C/D)으로 NAND에 직결
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1359421
- **Type**: conference
- **Published**: 2004
- **Authors**: I. -K. Lee, S. -J. Park, J. -W. Jung +3
- **PDF**: https://ieeexplore.ieee.org/document/1359421
- **Abstract**: The number of quantization bits of the input signals rn needs to be optimally determined through the trade-off between the H/W complexity and the BER performance in LDPC codes applications. Also, an effective means to incorporate a channel reliability Lc in the log-MAP based LDPC decoding is highly required, because it has a major effect on both the complexity and performance. In this paper so as to effectively incorporate Lc in LDPC decoding. The optimal number of quantization bits of rn is investigated through Monte-Carlo simulations assuming that bit-shifting approach is adopted. In addition, the effects of an incorrect estimation of noise variance on the performance of LDPC codes are investigated. There is a confined range in which the effects of an in correct estimation can be ignored

## Performance analysis of BP-based algorithms for irregular low-density parity-check codes on fast Rayleigh fading channel

- **Status**: ✅
- **Reason**: 불규칙 LDPC에 UMP/normalized/offset BP-based 디코더 파라미터 최적화 — 이식 가능 디코더 기법(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1400512
- **Type**: conference
- **Published**: 2004
- **Authors**: A. Ohhashi, T. Ohtsuki
- **PDF**: https://ieeexplore.ieee.org/document/1400512
- **Abstract**: In this paper, we analyze the performance of irregular low-density parity-check (LDPC) codes with three belief propagation (BP) based decoding algorithms, namely, the uniformly most powerful (UMP) BP-based algorithm, the normalized BP-based algorithm, and the offset BP-based algorithm on a fast Rayleigh fading channel by using density evolution (DE). We also optimize the code construction of the irregular LDPC codes with three BP-based algorithms, and determine optimum parameters for the normalized BP-based algorithm and the offset BP-based algorithm on the fast Rayleigh fading channel. From the numerical results, we show that the performance of the irregular LDPC codes with offset BP-based algorithm can be very close to that with the BP algorithm on the fast Rayleigh fading channel. We also show that the irregular LDPC codes with offset BP-based algorithm can achieve a very good trade-off between the performance and decoding complexity.

## A scalable architecture for LDPC decoding

- **Status**: ✅
- **Reason**: check-node 중심 재정식화로 메모리 대폭 절감하는 LDPC 디코더 HW 아키텍처(D), 스토리지 타깃
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:1269212
- **Type**: conference
- **Published**: 2004
- **Authors**: M. Cocco, J. Dielissen, M. Heijligers +2
- **PDF**: https://ieeexplore.ieee.org/document/1269212
- **Abstract**: Low density parity check (LDPC) codes offer excellent error correcting performance. However, current implementations are not capable of achieving the performance required by next generation storage and telecom applications. Extrapolation of many of those designs is not possible because of routing congestions. This article proposes a new architecture, based on a redefinition of a lesser-known LDPC decoding algorithm. As random LDPC codes are the most powerful, we abstain from making simplifying assumptions about the LDPC code which could ease the routing problem. We avoid the routing congestion problem by going for multiple independent sequential decoding machines, each decoding separate received codewords. In this serial approach the required amount of memory must be multiplied by the large number of machines. Our key contribution is a check node centric reformulation of the algorithm which gives huge memory reduction and which thus makes the serial approach possible.

## On the computation of the minimum distance of low-density parity-check codes

- **Status**: ✅
- **Reason**: LDPC 최소거리 계산 알고리즘(NNCS) — error floor 평가/코드설계에 이식 가능한 바이너리 LDPC 분석 기법(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1312605
- **Type**: conference
- **Published**: 2004
- **Authors**: Xiao-Yu Hu, M. P. C. Fossorier, E. Eleftheriou
- **PDF**: https://ieeexplore.ieee.org/document/1312605
- **Abstract**: Low-density parity-check (LDPC) codes in their broader-sense definition are linear codes whose parity-check matrices have fewer 1s than 0s. Finding their minimum distance is therefore in general an NP-hard problem. We propose a randomized algorithm called nearest nonzero codeword search (NNCS) approach to tackle this problem for iteratively decodable LDPC codes. The principle of the NNCS approach is to search codewords locally around the all-zero codeword perturbed by minimal noise, anticipating that the resultant nearest nonzero codewords will most likely contain the minimum-Hamming- weight codeword whose Hamming weight is equal to the minimum distance of the linear code. This approach has its roots in Berrou et al.'s error-impulse method and a form of Fossorier's list decoding for LDPC codes.

## Low-density parity-check code constructions for hardware implementation

- **Status**: ✅
- **Reason**: 계층적 구조 LDPC의 fully/partially serial HW 디코더 아키텍처(라우팅 혼잡 감소, 면적); D 이식 가능 디지털 HW
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:1312997
- **Type**: conference
- **Published**: 2004
- **Authors**: E. Liao, Engling Yeo, B. Nikolic
- **PDF**: https://ieeexplore.ieee.org/document/1312997
- **Abstract**: We present several hardware architectures to implement low-density parity-check (LDPC) decoders for codes constructed with a hierarchical structure. The proposed hierarchical formulation of the LDPC code allows a structured hardware realization of the decoder. For a fully-parallel implementation, there is a reduced routing congestion that allows implementations for blocks sizes up to 1024 bits in 0.13/spl mu/m technology. Partially and fully serial implementations benefits greatly from the structure of the code as well, leading to several flexible, efficient architectures. In a general purpose 0.13/spl mu/m technology, the approximate area required by a 1024-bit fully-parallel LDPC decoder is found to be 12.5 mm/sup 2/ while a serial decoder can be implemented in an area of 0.15 mm/sup 2/.

## High-throughput VLSI implementations of iterative decoders and related code construction problems

- **Status**: ✅
- **Reason**: D — 구조화 LDPC용 fully-parallel NPLA 기반 VLSI 디코더 아키텍처, array code 변형으로 라우팅 혼잡 감소. 디지털 HW 구현 기법 이식 가능
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:1377970
- **Type**: conference
- **Published**: 2004
- **Authors**: V. Nagarajan, N. Jayakumar, S. Khatri +1
- **PDF**: https://ieeexplore.ieee.org/document/1377970
- **Abstract**: In this paper, an efficient, fully-parallel network of programmable logic array (NPLA)-based realization of iterative decoders for structured LDPC codes is presented. The LDPC codes are developed in tandem with the underlying VLSI implementation technique, without compromising chip design constraints. The codes are based on a novel modification of array codes. This design methodology results in reduced routing congestion, a major problem in prior approaches. The operating power, delay and chip-size of the circuits are estimated, indicating that this implementation significantly outperforms presently used standard-cell based architectures. The described LDPC design method can accommodate widely different requirements, such as those arising from recording and wireless channel applications.

## On the effect of parity-check weights in iterative decoding

- **Status**: ✅
- **Reason**: 패리티검사 가중치가 반복디코딩에 미치는 효과(유한길이) — 코드설계/디코더 통찰(E/C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1365137
- **Type**: conference
- **Published**: 2004
- **Authors**: N. Santhi, A. Vardy
- **PDF**: https://ieeexplore.ieee.org/document/1365137
- **Abstract**: It is well-established "folk knowledge" that in order to be iteratively decodable, a code should have a sparse parity-check matrix, as it has some qualitative and quantitative properties for finite-length codes.

## On the dynamics of continuous-time analog iterative decoding

- **Status**: ✅
- **Reason**: 아날로그 디코더지만 SOR 기반 BP/min-sum 개선이 동기식 디지털 구현에도 이식 가능하다고 명시 — 디지털 디코더 알고리즘(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1365299
- **Type**: conference
- **Published**: 2004
- **Authors**: S. Hemati, A. H. Banihashemi
- **PDF**: https://ieeexplore.ieee.org/document/1365299
- **Abstract**: Iterative decoding with flooding schedule can be formulated as a fixed-point problem solved iteratively by successive substitution (88) method. In this work, we model continuous-time analog (asynchronous) iterative decoding by a first-order differential equation, and show that it can be approximated as the application of the well-known successive over relaxation (SOR) method for solving the fixed-point problem. Simulation results for belief propagation (sum-product) and min-sum algorithms confirm that SOR, which is in general superior to the simpler 88 method, can considerably improve the performance of iterative decoding for short codes. The improvement in performance increases with the maximum number of iterations and by reducing the step size in SOR, and the asymptotic result, corresponding to infinite maximum number of iterations and infinitesimal step size represents the performance of continuous-time analog iterative decoding. This means that under ideal circumstances continuous-time analog decoders can outperform their discrete-time digital counterparts by a large margin. Moreover, the results obtained by the proposed model are surprisingly close to the results of circuit simulation of a min-sum analog decoder presented in [S. Hemati et al., 2003]. Our work also suggests a general framework for improving iterative decoding algorithms on graphs with cycles, even for synchronous digital implementations.

## Reduced complexity decoding strategies for LDPC convolutional codes

- **Status**: ✅
- **Reason**: 바이너리 LDPC convolutional 저장·지연 감축 디코딩 전략 — 디코더 스케줄링/저장 기법 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1365528
- **Type**: conference
- **Published**: 2004
- **Authors**: A. E. Pusane, M. Lentmaier, K. S. Zigangirov +1
- **PDF**: https://ieeexplore.ieee.org/document/1365528
- **Abstract**: While low-density parity-check (LDPC) convolutional codes tend to significantly outperform LDPC block codes with the same processor complexity, large storage requirements and a long initial decoding delay are two issues related to their continuous pipeline decoding architecture [A. Jimenez Feltstrom et al., (1999)]. In this paper, we propose reduced complexity decoding strategies to lessen the storage requirements and the initial decoding delay without significant loss in performance.

## A scalable architecture of a structured LDPC decoder

- **Status**: ✅
- **Reason**: 구조적 LDPC FPGA 디코더 + 3비트 비균일 양자화기 — 이식 가능 HW 아키텍처+양자화(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1365330
- **Type**: conference
- **Published**: 2004
- **Authors**: J. K. . -S. Lee, B. Lee, J. Thorpe +3
- **PDF**: https://ieeexplore.ieee.org/document/1365330
- **Abstract**: We present a scalable decoding architecture for a certain class of structured LDPC codes. The codes are designed using a small (n, r) protograph that is replicated Z times to produce a decoding graph for a (Z/spl times/n, Z/spl times/r) code. Using this architecture, we have implemented a decoder for a (4096, 2048) LDPC code on a Xilinx Virtex-II 2000 FPGA, and achieved decoding speeds of 31 Mbps with 10 fixed iterations. The implemented message-passing algorithm uses an optimized 3-bit nonuniform quantizer that allows near floating point performance in the waterfall region, with drastically smaller hardware implementation requirements.

## Performance of low density parity check (LDPC) codes with bootstrap decoding algorithm on a fast fading channel

- **Status**: ✅
- **Reason**: BWBF/bootstrapped LLR-BP 등 부호 비의존 LDPC 디코더 알고리즘 개선(C) — 바이너리 LDPC BP에 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1387969
- **Type**: conference
- **Published**: 2004
- **Authors**: Y. Inaba, T. Ohtsuki
- **PDF**: https://ieeexplore.ieee.org/document/1387969
- **Abstract**: Low density parity check (LDPC) codes can be decoded in various ways, namely the bit-flipping (BF) algorithm, the weighted BF (WBF) algorithm and the log-likelihood ratio belief propagation (LLR-BP) algorithm, and so on. These algorithms provide a wide range of tradeoffs among decoding complexity, decoding speed, and error rate performance. Recently, the bootstrapped WBF (BWBF) algorithm has been proposed to improve the error rate performance and the decoding complexity of the WBF algorithm. In this paper, we study the effects of the predetermined threshold /spl alpha/ of the bootstrap step on BER for various LDPC codes. Furthermore, we apply the bootstrap step to the LLR-BP algorithm. We evaluate the BWBF and the bootstrapped LLR-BP (B-LLR-BP) algorithms on a fast fading channel. We show that the optimal threshold depends on the row and column weights of the LDPC codes. We also show that the BWBF algorithm provides a large improvements in both the error rate performance and the decoding complexity on a fast fading channel. Moreover, we show that the LLR-BP algorithm hardly receives the effect of the bootstrap step.

## Explicit construction of families of LDPC codes with no 4-cycles

- **Status**: ✅
- **Reason**: E. 4-cycle 없는 바이너리 LDPC 명시적 구성족(known girth Tanner graph) — girth/사이클 제거 코드설계 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1365274
- **Type**: conference
- **Published**: 2004
- **Authors**: J. . -L. Kim, U. N. Peled
- **PDF**: https://ieeexplore.ieee.org/document/1365274
- **Abstract**: LDPC codes are serious contenders to turbo codes in terms of decoding performance. One of the main problems is to give an explicit construction of such codes whose Tanner graphs have known girth. For a prime power q and m/spl ges/2, Lazebnik and Ustimenko construct a q-regular bipartite graph D(m,q) on 2q/sup m/ vertices, which has girth at least 2/spl lceil/m/2/spl lfloor/+4. We regard these graphs as Tanner graphs of binary codes LU(m,q). We can determine the dimension and minimum weight of LU(2,q), and show that the weight of its minimum stopping set is at least q+2 for q odd and exactly q+2 for q even. We know that D(2,q) has girth 6 and diameter 4, whereas D(3,q) has girth 8 and diameter 6. We prove that for an odd prime p, LU(3,p) is a [p/sup 3/,k] code with k/spl ges/(p/sup 3/-2p/sup 2/+3p-2)/2. We show that the minimum weight and the weight of the minimum stopping set of LU(3,q) are at least 2q and they are exactly 2q for many LU(3,q) codes. We find some interesting LDPC codes by our partial row construction.

## Power efficient architecture for (3,6)-regular low-density parity-check code decoder

- **Status**: ✅
- **Reason**: (3,6)-regular LDPC 디코더 저전력 VLSI 아키텍처(메모리 접근 절감) — 디지털 HW(D) 신규 기여, NAND 컨트롤러 ECC HW로 이식 가능
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:1328945
- **Type**: conference
- **Published**: 2004
- **Authors**: Yijun Li, M. Elassal, M. Bayoumi
- **PDF**: https://ieeexplore.ieee.org/document/1328945
- **Abstract**: Most of the current LDPC decoder VLSI architecture research focuses on increasing system throughput or reducing hardware implementation complexity, but neglects power consumption. In this paper, we analyze the power consumption of the (3,k)-regular LDPC decoder architecture. Our analysis shows that 95% of the power consumption is consumed in accessing the memory. A new architecture is proposed which reduces memory access, hence power consumption, without sacrificing the performance. Experimental results show reduction in the power consumption by 14% and lower hardware complexity without sacrificing the Bit-Error-Ratio performance compared to previous work.

## Field programmable gate array implementation of a generalized decoder for structured low-density parity check codes

- **Status**: ✅
- **Reason**: 구조적 LDPC용 범용 FPGA 디코더 구현, 완전 재구성 가능 코어 — 이식 가능 디지털 HW 아키텍처(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:1393246
- **Type**: conference
- **Published**: 2004
- **Authors**: Lingyan Sun, B. V. K. Vijaya Kumar
- **PDF**: https://ieeexplore.ieee.org/document/1393246
- **Abstract**: This work describes a generalized decoder implementation for structured low-density parity check (LDPC) codes. The decoder features low logic consumption, efficient memory management, and full parameterization for reconfiguration. The goal is to provide a unified solution for fast evaluation of a broad class of structured LDPC codes utilizing the properties of field programmable gate arrays (FPGA): high speed and configurability. As a fully reconfigurable core, it is ready to be used in different applications to lower the design to market time. The throughput and resource consumptions are evaluated.

## The semi-algebra low-density parity-check codes

- **Status**: ✅
- **Reason**: Semi-algebra LDPC construction with novel Adaptive Slope Group girth scheme — portable binary LDPC code design (E).
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1312527
- **Type**: conference
- **Published**: 2004
- **Authors**: Yu Yi, Gi Yean Hwang, Moon Ho Lee
- **PDF**: https://ieeexplore.ieee.org/document/1312527
- **Abstract**: In this paper, the construction of semi-algebra Low-density parity-check (LDPC) code with an arbitrary block length is presented. The encoding circuit is based on the original semi-algebra design and users can have the choice of using the matrix pattern and various code rates to design for different communication applications. Especially, a novel girth scheme named Adaptive Slope Group (ASG) is proposed for the semi-algebra code design with the large girth and maximum minimum distance. We can compare the performance of this novel semi-algebra LDPC code against the Shannon limit for several rates. The simulation results show our codes can perform a large coding gain at high SNRs with BPSK modulation over AWGN channels. However, column weight j is not random, only for j=2.

## Design of irregular LDPC codec on a single chip FPGA

- **Status**: ✅
- **Reason**: D — irregular LDPC codec의 부분병렬 FPGA 구현, VN/CN 처리·메모리 관리 등 디지털 HW 아키텍처 이식 가능
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:1322959
- **Type**: conference
- **Published**: 2004
- **Authors**: Yukei Pei, Liuguo Yin, Jianhua Lu
- **PDF**: https://ieeexplore.ieee.org/document/1322959
- **Abstract**: A novel implementation of irregular low density parity check (LDPC) codec on a single chip Xilinx FPGA is presented in this paper. The encoder and decoder are accomplished by partial parallel architectures with very low complexity. Specifically, details including the decoder and encoder structures, memory management, and required computation units to realize the variable/check node decoding and the parity-check bits generation are discussed. It is verified that the error-correcting capability of the codes with the proposed scheme is kept the same as that by random generation method, while highly parallel encoding/decoding scheme may be realized with ease. Thereby, the proposed design approach for the complex LDPC codec is very promising for real applications.

## Low complexity decoding algorithm of parallel concatenated LDPC code

- **Status**: ✅
- **Reason**: C — 병렬연접 Gallager(LDPC) 부호용 저복잡도 BP 변형 디코딩 알고리즘, HW 구현 지향이라 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1322978
- **Type**: conference
- **Published**: 2004
- **Authors**: Jin Li, Xiaohu You, Yun Hee Kim
- **PDF**: https://ieeexplore.ieee.org/document/1322978
- **Abstract**: PCGC (parallel concatenated Gallager code) is a new class of concatenated codes based on component LDPC codes. The decoder of it uses modified BP (belief propagation) algorithm in component LDPC decoder. But this conventional decoding algorithm has high complexity and is not suitable for implementation in hardware. So in this paper we propose a new decoding algorithm of PCGC, which has good performance and low complexity. And it is feasible to be implemented in hardware.

## Joint graph-decoder design of IRA codes on scalable architectures [LDPC codes]

- **Status**: ✅
- **Reason**: IRA(LDPC 부류) 부분병렬 디코더 아키텍처 + RAM 충돌 없는 joint graph-decoder 설계 → HW 이식 가능(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:1326916
- **Type**: conference
- **Published**: 2004
- **Authors**: F. Kienle, N. Wehn
- **PDF**: https://ieeexplore.ieee.org/document/1326916
- **Abstract**: Channel coding is an important building block in communication systems since it ensures the quality of service. Irregular repeat-accumulate (IRA) codes belong to the class of low-density parity-check (LDPC) codes and even outperform the recently introduced turbo-codes of current communication standards. The advantage of IRA codes over LDPC codes is that they come with a linear-time encoding complexity. IRA codes can be represented by a Tanner graph with arbitrary connections between nodes of given degrees. The implementation complexity of IRA decoders is dominated by the randomness of these connections. In this paper, we present a scalable partly parallel IRA decoder architecture. We present a joint graph-decoder design to parallelize IRA codes which can be efficiently processed by this decoder without any RAM access conflicts. We show design examples of these IRA codes which outperform the UMTS turbo-code by 0.2 dB.

## Investigation of circulant matrices for reversible LDPC codes

- **Status**: ✅
- **Reason**: Reversible LDPC from circulant matrices over GF(2), binary; structured circulant construction relevant to QC-LDPC code design (E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1413866
- **Type**: conference
- **Published**: 2004
- **Authors**: Anchalee Puengnim
- **PDF**: https://ieeexplore.ieee.org/document/1413866
- **Abstract**: We investigate the error performance of reversible LDPC codes constructed from the circulant matrix (Haley, D. et al., IEEE Global Telecom. Conf., vol.1, p.1303-7, 2002) in the region of BER smaller than 10/sup -5/. We also propose and investigate other possible circulant matrices selected from some primitive polynomials over GF(2). We expect to offer another choice of block length and in some cases better error performance for reversible LDPC codes.

## Construction of short block length irregular low-density parity-check codes

- **Status**: ✅
- **Reason**: Short irregular LDPC construction via stopping-set/trellis search achieving low error floor — portable code design (E).
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1312521
- **Type**: conference
- **Published**: 2004
- **Authors**: A. Ramamoorthy, R. Wesel
- **PDF**: https://ieeexplore.ieee.org/document/1312521
- **Abstract**: We present a construction algorithm for short block length irregular low-density parity-check (LDPC) codes. Based on a novel interpretation of stopping sets in terms of the parity-check matrix, we present an approximate trellis-based search algorithm that detects many stopping sets. Growing the parity check matrix by a combination of random generation and the trellis-based search, we obtain codes that possess error floors orders of magnitude below randomly constructed codes and significantly better than other comparable constructions.

## Multiple rate low-density parity-check codes with constant blocklength

- **Status**: ✅
- **Reason**: 단일 디코더 아키텍처 공유하는 다중 rate 바이너리 LDPC 구성 + 낮은 error floor, 코드설계·HW 이식 가능(D/E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1399517
- **Type**: conference
- **Published**: 2004
- **Authors**: A. I. V. Casado, Wen-Yen Weng, R. D. Wesel
- **PDF**: https://ieeexplore.ieee.org/document/1399517
- **Abstract**: This paper presents a new method to design low-density parity-check codes for a variety of different rates that all share the same fundamental decoder architecture. Combining rows of the parity-check matrix for the lowest rate code produces the parity-check matrices for higher rates. An important advantage of this approach is that all effective code rates have the same blocklength. These LDPC codes also share the same variable degree distribution. The proposed design method maintains good graphical properties and hence low error floors for all rates. Furthermore, an imposed matrix structure facilitates a low complexity encoding and decoding of the codes.

## A class of turbo-like codes with efficient and practical high-speed decoders

- **Status**: ✅
- **Reason**: turbo-like 부호 고속 디코더 아키텍처 — 인터리버/병렬처리/메모리접근 구조가 부호 비의존적 VLSI 고속 디코더로 LDPC HW에 이식 가능(D, 애매하면 살림)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1493276
- **Type**: conference
- **Published**: 2004
- **Authors**: A. Abbasfar, D. Divsalar, Kung Yao
- **PDF**: https://ieeexplore.ieee.org/document/1493276
- **Abstract**: Turbo-like codes not only achieve near Shannon-capacity performance, but also have decoders with modest complexity, which is crucial for implementation. Recently some efficient architectures for high-speed decoding of turbo and LDPC codes have been presented in the literature. The memory access is the main problem in practical implementation of such decoders. This problem has also been solved by using interleaves with special structure. In this paper, a generalized class of turbo-like codes that have high-speed decoding capability, which is based on the graphical interpretation of their code, is introduced. It has been shown that previous codes are part of this class. This class of codes not only provides code structure for parallel processing, but also provides the interleaver structure for practical implementation. A general architecture for high-speed decoding of these codes is presented. Regularity and modularity of the decoder makes it the architecture of choice for VLSI implementation of very high-speed decoders.

## Structured eIRA codes

- **Status**: ✅
- **Reason**: structured eIRA(LDPC계) 코드 설계 — 효율적 인코딩 가능한 구조화 패리티검사·낮은 error floor, 바이너리 코드 설계 이식 가능(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1399516
- **Type**: conference
- **Published**: 2004
- **Authors**: Yifei Zhang, W. E. Ryan, Yan Li
- **PDF**: https://ieeexplore.ieee.org/document/1399516
- **Abstract**: In a recent paper, Yang et at. presented the class of extended irregular repeat-accumulate (eIRA) codes which are efficiently encodable LDPC codes possessing very low error-rate floors and are appropriate for code rates 1/2 or greater. While efficiently encodable, the left-most (n - k)-by-k submatrix of an eIRA code parity-check matrix is random in nature, making efficient decoder implementation problematic. In the present paper, we present structured eIRA codes. We first present some ensemble results for the general class of eIRA codes, after which the subclass of structured eIRA codes is defined. Software and hardware-based performance results for structured eIRA code designs (rates 0.5 to 0.9) are then presented. Results include a 0.5(2048, 1024) code with a BER floor at 10/sup -9/ and a 0.8(5120, 4096) code with a BER floor below 10/sup -11/.

## Low-density generator matrix codes for indoor and Markov channels

- **Status**: ✅
- **Reason**: C — LDGM(LDPC 일종) 메시지패싱을 Markov 채널 그래프에 통합한 디코더 수정. 채널상태 그래프 결합 BP 기법은 NAND 채널 모델링에 이식 여지. 경계라 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1377997
- **Type**: conference
- **Published**: 2004
- **Authors**: Hanqing Lou, J. Garcia-Frias
- **PDF**: https://ieeexplore.ieee.org/document/1377997
- **Abstract**: We propose a modified algorithm for the decoding of linear codes with low-density generator matrix (LDGM) codes (a class of LDPC codes) over indoor and finite-state binary Markov channels. In order to avoid error floors, a concatenation of two LDGM codes is utilized. The hidden Markov model representing the channel is incorporated into the graph corresponding to the LDGM codes, and the message passing algorithm is modified accordingly. The proposed scheme clearly outperforms systems in which the channel statistics are not exploited in the decoding process, allowing reliable communication at rates which are above the capacity of a memoryless channel with the same stationary bit error probability as the Markov channel. Moreover, the proposed method can be successfully applied for real wireless channels that can be modeled with hidden Markov models, such as indoor channels.

## Efficient hardware realization of IRA code decoders

- **Status**: ✅
- **Reason**: IRA codes are a subclass of binary LDPC; HW decoder architecture template (D) is portable to NAND LDPC ECC HW.
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:1363064
- **Type**: conference
- **Published**: 2004
- **Authors**: F. Kienle, N. Wehn
- **PDF**: https://ieeexplore.ieee.org/document/1363064
- **Abstract**: Channel coding is an important building block in communication systems since it ensures the quality of service. Irregular repeat-accumulate (IRA) codes belong to the class of low-density parity-check (LDPC) codes and can even outperform the recently introduced turbo-codes of current communication standards. Implementation complexities like area and achievable throughput of these channel coding schemes have a major impact on the decisions of standardization committees. In this paper, we investigate implementation issues of IRA codes and analyze the strong interdependency of code performance and architectural dependencies, like throughput and area. We present an architecture template which is capable of decoding hardware optimized IRA codes which can outperform turbo-codes. We demonstrate this new approach through instances synthesized in a 0.13 /spl mu/m technology.

## Programmable low-density parity-check decoder

- **Status**: ✅
- **Reason**: 프로그래머블 semi-parallel LDPC 디코더 HW; edge-coloring 통신충돌 회피·VHDL 구현, 디지털 디코더 아키텍처 이식 가능(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:1439171
- **Type**: conference
- **Published**: 2004
- **Authors**: G. Malema, M. Liebelt
- **PDF**: https://ieeexplore.ieee.org/document/1439171
- **Abstract**: This paper presents a programmable semi-parallel architecture for low-density parity-check (LDPC) codes. Communication conflicts are avoided by edge-coloring the code graph and grouping of edges/physical connections by color. The architecture model is easily scalable and programmable for larger block sizes. Though the communication hardware cost is high, the model can be easily reconfigured to reduce hardware cost at the expense of flexibility in code design and decoding performance. The hardware cost, latency, code flexibility and code performance tradeoffs can be varied over a wide range to suit a wide range of applications. Simple execution control and mapping are other advantages of this model. A behavioral VHDL implementation was developed to verify the functionality of the architecture.

## Analysis of an algorithm for irregular LDPC code construction

- **Status**: ✅
- **Reason**: stopping set/error floor 줄이는 불규칙 LDPC 구성 알고리즘 분석 — 코드설계(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1365107
- **Type**: conference
- **Published**: 2004
- **Authors**: A. Ramamoorthy, R. D. Wesel
- **PDF**: https://ieeexplore.ieee.org/document/1365107
- **Abstract**: This work presents a rigorous analysis of an algorithm proposed by Tian et al. (2003) for the construction of irregular LDPC codes with reduced stopping sets and low error floors. Computation of the expected number of stopping sets of a given size proves that the algorithm significantly outperforms a random construction. We show that the algorithm provably reduces the expected number of stopping sets up to a certain size (based on the input parameters). The expected number of cycles of a given size is computed for both constructions.

## An LDPC decoding schedule for memory access reduction

- **Status**: ✅
- **Reason**: 구조화 LDPC 디코딩의 메모리 접근 66% 감소 스케줄링 아키텍처 — 디지털 HW/스케줄 기법(C/D) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1327075
- **Type**: conference
- **Published**: 2004
- **Authors**: K. Gunnam, Gwan Choi, M. Yeary
- **PDF**: https://ieeexplore.ieee.org/document/1327075
- **Abstract**: Recent research efforts based on a joint code-decoder design methodology have shown that it is possible to construct structured LDPC (low density parity check) codes without any performance degradation. An interesting new data independence property between the two classes of messages viz. check to bit and bit to check, involved in decoding, is observed. This property is a result of the specific structuring of the parity check matrix. By exploiting this property, we propose an architecture in which the computation of messages is synchronized such that each class of message is consumed immediately by the computational unit for another class of message. The internal memory of the check to bit units is increased in tune with the storage requirement of the check to bit messages. The separate memories for check to bit and bit to check messages are eliminated. This approach has memory savings of 75% and reduces the overall memory accesses by 66%.

## A new family of irregular LDPC codes

- **Status**: ✅
- **Reason**: E — optical orthogonal code 기반 QC irregular LDPC 구성, 바이너리 sum-product 동작; 코드 설계 기법 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1322977
- **Type**: conference
- **Published**: 2004
- **Authors**: Hong Wen, Fei Hu, Jian Li +1
- **PDF**: https://ieeexplore.ieee.org/document/1322977
- **Abstract**: In this paper, we present a method for constructing irregular LDPC (low density parity check) codes based on the optical orthogonal codes. The resulting codes are quasi-cyclic codes and can be encoded with low complexity. They perform well with the sum-product iterative decoding.

## LDPC codes for unequal error protection

- **Status**: ✅
- **Reason**: 하삼각 패리티검사 LDPC + 수정 디코딩으로 UEP; 부호 구성·디코딩 변형이 바이너리 LDPC에 이식 가능(E/C, 애매하나 살림)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1441685
- **Type**: conference
- **Published**: 2004
- **Authors**: Lin Xuehong, Wu Weiling
- **PDF**: https://ieeexplore.ieee.org/document/1441685
- **Abstract**: This paper proposed LDPC codes with lower triangular parity check and the modified decoding algorithm, which can achieve unequal error protection for transmission bitstream with different level of protection. It is well suitable for transmitting the important sequence in front of codeword, such as wavelet-based image codecs.

## Structured LDPC over urn model channels with memory

- **Status**: ✅
- **Reason**: E: block-circulant 기반 신규 정규/비정규 LDPC 구성 + 메모리 채널용 반복디코딩(state XORing 부가정보) — 코드설계/디코더 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1345094
- **Type**: conference
- **Published**: 2004
- **Authors**: V. Nagarajan, O. Milenkovic
- **PDF**: https://ieeexplore.ieee.org/document/1345094
- **Abstract**: In this paper we investigate the performance of structured LDPC codes over a class of channels with memory. The channels under consideration are based on Polya's urn model (F.Alajaji et al, IEEE Trans. Inform. Theory, vol.40, no.6, p.2035-2041, 1994) and can be viewed as a practical representative of channels with burst errors. The BER curves for iterative decoding with channel estimation show that random-like codes and a new class of regular and irregular codes, based on parity-check matrices of the form of block-circulants, have comparable performance for codelengths of the order of several thousands. Furthermore, the complete convergence region within the parameter space of the urn channel model is determined by using a new technique for generating side-information, termed state XORing. This technique also allows for complete characterization of the convergence region of another important bursty channel model, namely the Gilbert-Eliot scheme. Some possible applications of the results described in this paper are for designing reliable coding schemes for communication over fading or storage channels.

## Pseudo-codewords of cycle codes via zeta functions

- **Status**: ✅
- **Reason**: cycle code(LDPC 특수형)의 의사부호어를 zeta function·fundamental cone으로 분석 — 반복디코딩 error floor/성능 특성화 이론으로 코드설계(E)에 이식 여지, 애매하여 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1405265
- **Type**: conference
- **Published**: 2004
- **Authors**: R. Koetter, W. . -C. W. Li, P. O. Vontobel +1
- **PDF**: https://ieeexplore.ieee.org/document/1405265
- **Abstract**: Cycle codes are a special case of low-density parity-check (LDPC) codes and as such can be decoded using an iterative message-passing decoding algorithm on the associated Tanner graph. The existence of pseudo-codewords is known to cause the decoding algorithm to fail in certain instances. In this paper, we draw a connection between pseudo-codewords of cycle codes and the so-called edge zeta function of the associated normal graph and show how the Newton polytope of the zeta function equals the fundamental cone of the code, which plays a crucial role in characterizing the performance of iterative decoding algorithms.

## High-performance decoders for regular and irregular repeat-accumulate codes

- **Status**: ✅
- **Reason**: RA 부호 디코더의 메시지패싱 아키텍처(staggered 스케줄링·permuter·저복잡도 병렬화)가 AA-LDPC 디코더와 유사, HW 스케줄링 기법 이식 가능(D, 애매시 in)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1378472
- **Type**: conference
- **Published**: 2004
- **Authors**: M. M. Mansour
- **PDF**: https://ieeexplore.ieee.org/document/1378472
- **Abstract**: This paper investigates high-performance decoder design for regular and irregular repeat-accumulate (RA) codes of large block length. In order to achieve throughputs and bit-error rate performance that are inline with future trends in high-speed communications. high-throughput and low-power decoders of low complexity are needed. To meet such conflicting requirements for long codes, the concept of architecture-aware RA (AARA) code design is proposed. AARA code design decouples the complexity of the decoder from the owe structure by inducing structural regularity features that are amenable to efficient and scalable decoder implementations. Design methods of AARA codes with structured permuters for which an iterative decoding algorithm performs well under message-passing are analogous to those for AA LDPC codes. Algorithmic and architectural optimizations that address the latency, memory overhead, and complexity problems typical of iterative decoders for long RA codes are investigated, and a staggered decoding schedule is introduced. AARA decoders using the proposed schedule have substantial advantage over serial and parallel RA decoders.

## Bounds on information combining for parity-check equations

- **Status**: ✅
- **Reason**: Information combining bounds for parity-check equations on BISO channels — directly relevant to LDPC BP message-passing analysis/density evolution (C/E borderline, keep for Phase 3).
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1287390
- **Type**: conference
- **Published**: 2004
- **Authors**: I. Land, P. A. Hoeher, J. Huber
- **PDF**: https://ieeexplore.ieee.org/document/1287390
- **Abstract**: When several independent channels are coupled by a parity check constraint on their inputs, the mutual information between the input of one channel and the outputs of all other channels can be expressed as a combination of the mutual information between the input and the output of each individual channel. This concept is denoted as information combining. For binary-input symmetric discrete memoryless channels, we present bounds on the combined information which are only based on the mutual information of the channels. Furthermore, we show that these bounds cannot be further improved. Exact expressions are provided for the case that all channels are binary symmetric channels and for the case that all channels are binary erasure channels.

## Hybrid hard-decision iterative decoding of regular low-density parity-check codes

- **Status**: ✅
- **Reason**: Hybrid time-invariant iterative decoding of regular LDPC (binary message-passing) — portable decoder algorithm (C).
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1312526
- **Type**: conference
- **Published**: 2004
- **Authors**: P. Zarrinkhat, A. H. Banihashemi
- **PDF**: https://ieeexplore.ieee.org/document/1312526
- **Abstract**: Hybrid decoding is to combine different iterative decoding algorithms with the aim of improving error performance or decoding complexity. In this work, we introduce "time-invariant" hybrid (HTI) algorithms, and show that for regular low-density parity-check codes and binary message-passing algorithms, HTI algorithms perform remarkably better than their constituent algorithms. We also show that compared to "switch-type" hybrid algorithms, such as Gallager's algorithm B, where a comparable improvement is obtained by switching between different iterative decoding algorithms, HTI algorithms are far less sensitive to channel conditions and thus can be practically more attractive.

## Quantization and quantization sensitivity of soft-output product codes for fast-speed applications

- **Status**: ✅
- **Reason**: min-sum 소프트출력 디코딩의 (3,1) 양자화 기법 — 부호 비의존적 디코더 양자화로 LDPC min-sum에 이식 가능(C/D). product code지만 양자화 기법 떼어냄
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1302869
- **Type**: conference
- **Published**: 2004
- **Authors**: Ruiyuan Hu, Jing Li, E. Kurtas
- **PDF**: https://ieeexplore.ieee.org/document/1302869
- **Abstract**: This paper investigates two quantization schemes on three soft-output message-passing decoding algorithms for 2-dimensional product codes. Quantization sensitivity on code rates and channel conditions is also investigated. The surprising yet encouraging result is that a simple (3,1) uniform quantization scheme on the min-sum algorithm results in the best overall quality in terms of space, performance and complexity.

## Improved progressive-edge-growth (PEG) construction of irregular LDPC codes

- **Status**: ✅
- **Reason**: E — 비정칙 LDPC PEG 구성의 개선(고SNR 성능 향상). 유한길이 코드 설계 기법으로 바이너리 LDPC에 직접 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1377995
- **Type**: conference
- **Published**: 2004
- **Authors**: Hua Xiao, A. H. Banihashemi
- **PDF**: https://ieeexplore.ieee.org/document/1377995
- **Abstract**: The progressive-edge-growth (PEG) algorithm (X.-Y. Hu et al., 2001; 2002) is known to construct low-density parity-check codes at finite block lengths with very good performance. We propose a very simple modification to the PEG construction for irregular codes, which considerably improves the performance at high signal-to-noise ratios (SNR) with no sacrifice in low-SNR performance.

## Construction of good LDPC codes using dilation matrices

- **Status**: ✅
- **Reason**: E. dilation matrix로 designed girth 갖는 바이너리 LDPC 신규 구성법 — NAND 코드설계로 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1365272
- **Type**: conference
- **Published**: 2004
- **Authors**: M. Greferath, M. E. O'Sullivan, R. Smarandache
- **PDF**: https://ieeexplore.ieee.org/document/1365272
- **Abstract**: A new method is given to construct low-density parity check codes the graphs of which are of designed girth. We give examples to illustrate the new method, and also present performance diagrams that suggest that these codes are as good as random codes in low SNR, and preferable to random codes at higher SNR.

## Evaluating alternative implementations for LDPC decoder check node function

- **Status**: ✅
- **Reason**: LDPC 체크노드 함수 근사(ROM LUT vs 구간선형) VLSI 구현 기법, 디지털 디코더 HW 이식 가능(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1339511
- **Type**: conference
- **Published**: 2004
- **Authors**: T. Theocharides, G. Link, E. Swankoski +3
- **PDF**: https://ieeexplore.ieee.org/document/1339511
- **Abstract**: Low density parity checks (LDPC) are a method of error detection and correction that are able to achieve near Shannon-limit channel communication. LDPC decoders involve a series of computations between two units, the check node and the bit node. In this paper we propose the use of an approximation unit to perform the check node operation. Additionally, we propose a ROM based look-up table (LUT) as a function approximation technique, to be used with an LDPC decoder. The paper shows that a ROM based LUT achieves better performance than using a piecewise linear approximation method to approximate the LDPC computation function. Furthermore, this paper shows that the ROM LUT method can gradually take over as the selected function approximation technique for computationally intensive demanding VLSI designs as the technology shifts to the nanometer era.

## Semi-parallel reconfigurable architectures for real-time LDPC decoding

- **Status**: ✅
- **Reason**: Semi-parallel VHDL LDPC decoder with modified min-sum on structured H — portable digital HW + decoder algorithm (C/D).
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1286526
- **Type**: conference
- **Published**: 2004
- **Authors**: M. Karkooti, J. R. Cavallaro
- **PDF**: https://ieeexplore.ieee.org/document/1286526
- **Abstract**: This paper presents a semi-parallel architecture for decoding low density parity check (LDPC) codes. A modified version of min-sum algorithm has been used which the advantage of simpler computations has compared to sum-product algorithm without any loss in performance. Special structure of the parity check matrix of the proposed code leads to an efficient semi-parallel implementation of the decoder for a family of (3, 6) LDPC codes. A prototype architecture has been implemented in VHDL on programmable hardware. The design is easily scalable and reconfigurable for larger block sizes. Simulation results show that our proposed decoder for a block length of 1536 bits can achieve data rates up to 127 Mbps.

## LDPC codes for Gaussian broadcast channels

- **Status**: ✅
- **Reason**: 가우시안 방송채널용 LDPC 차수분포 최적화(differential evolution, EXIT); 코드설계 기법 바이너리 LDPC에 이식 가능(E, 애매하나 살림)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1439282
- **Type**: conference
- **Published**: 2004
- **Authors**: P. Berlin, D. Tuninetti
- **PDF**: https://ieeexplore.ieee.org/document/1439282
- **Abstract**: We study coding over a class of two-user broadcast channels with additive white Gaussian noise and fading known at the receivers only. Joint decoding of low-density parity-check codes is analyzed. The message update rule at the mapping node linking the users' codes is derived and is shown to exhibit an interesting soft interference cancellation property. Good degree distributions are found using the differential evolution optimization technique and extrinsic information transfer analysis. The corresponding codes have rates close to the boundary of the achievable region for binary constrained input channels, both with and without fading. Simulation results for moderate blocklength show that the optimized codes operate within 1 dB of their thresholds.

## A class of good quasi-cyclic low-density parity check codes based on progressive edge growth graph

- **Status**: ✅
- **Reason**: PEG에 QC 제약을 더한 새 QC-LDPC 구성(E) — HW 친화적 패리티검사 행렬, 바이너리 코드 설계 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1399513
- **Type**: conference
- **Published**: 2004
- **Authors**: Zongwang Li, B. V. K. V. Kumar
- **PDF**: https://ieeexplore.ieee.org/document/1399513
- **Abstract**: We present a new class of quasi-cyclic low density parity check (QC-LDPC) codes, whose quasi-cyclic nature makes them attractive for implementation. Both regular and irregular QC-LDPC codes are designed by modifying the progressive edge growth (PEG) graph with a quasi-cyclic constraint. Simulations show that these QC-LDPC codes offer hardware-friendly parity check matrices and have as good error correction performance as random LDPC codes and other good QC-LDPC codes. In addition, the proposed QC-LDPC codes offer a much more flexible set of parameters compared to the traditional designs.

## Construction of low density parity check codes: BIBD and vandermonde

- **Status**: ✅
- **Reason**: Binary LDPC construction via BIBD/Vandermonde (category E code design); algebraic structured construction portable to NAND QC-LDPC
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1409480
- **Type**: conference
- **Published**: 2004
- **Authors**: B. Ammar, B. Honary
- **PDF**: https://ieeexplore.ieee.org/document/1409480
- **Abstract**: In this presentation we shall go briefly through the properties of LDPC-codes and discuss two methods for constructing LDPC matrices. One of these methods is based on BIBD, which we explain in the first part of the presentation. We shall go through the definition of BIBD and introduce the general methods of finding them. Then we shall explain one particular method called symmetrically repeated differences SRD and explain several designs based on this method. We shall then show how to use BIBD in LDPC construction. Go through the performance of some LDPC-codes based on BIBD [ 1, 2].

## Accumulate repeat accumulate codes

- **Status**: ✅
- **Reason**: E/C — ARA 코드는 LDPC 하위클래스, protograph 구성으로 capacity 근접 threshold + 고속 디코더 구현 가능. 프로토그래프 코드 설계 기법 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1377999
- **Type**: conference
- **Published**: 2004
- **Authors**: 
- **PDF**: https://ieeexplore.ieee.org/document/1377999
- **Abstract**: We propose an innovative channel coding scheme called "accumulate repeat accumulate codes" (ARA). This class of codes can be viewed as serial turbo-like codes, or as a subclass of low density parity check (LDPC) codes, thus belief propagation can be used for iterative decoding of ARA codes on a graph. The structure of encoder for this class can be viewed as precoded repeat accumulate (RA) code or as precoded irregular repeat accumulate (IRA) code, where simply an accumulator is chosen as the precoder. Thus ARA codes have simple, and very fast encoder structure when they representing LDPC codes. Based on density evolution for LDPC codes through some examples for ARA codes, we show that for maximum variable node degree 5 a minimum bit SNR as low as 0.08 dB from channel capacity for rate 1/2 can be achieved as the block size goes to infinity. Thus based on fixed low maximum variable node degree, its threshold outperforms not only the RA and IRA codes but also the best known unstructured irregular LDPC codes with the same maximum node degree. Furthermore, by puncturing the accumulators, any desired high rate codes close to code rate 1 can be obtained with thresholds that stay close to the channel capacity thresholds uniformly. Iterative decoding simulation results are provided. The ARA codes also have projected graph or protograph representation, that allows for high speed decoder implementation.

## Accumulate-repeat-accumulate-accumulate-codes

- **Status**: ✅
- **Reason**: ARAA를 LDPC 하위클래스로 protograph 표현+BP 디코더, density evolution 기반 저 error-floor 구성으로 바이너리 LDPC 코드설계 이식 가능(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1400450
- **Type**: conference
- **Published**: 2004
- **Authors**: D. Divsalar, S. Dolinar, J. Thorpe
- **PDF**: https://ieeexplore.ieee.org/document/1400450
- **Abstract**: Inspired by recently proposed accumulate-repeat-accumulate (ARA) codes (Abbasfar et al. (2004)), in this paper we propose a channel coding scheme called accumulate-repeat-accumulate-accumulate (ARAA) codes. These codes can he seen as serial turbo-like codes or as a subclass of low density parity check (LDPC) codes, and they have a projected graph or protograph representation, this allows for a high-speed iterative decoder implementation using belief propagation. An ARAA code can be viewed as a precoded repeat-and-accumulate (RA) code with puncturing in concatenation with another accumulator, where simply an accumulator is chosen as the precoder; thus ARAA codes have a very fast encoder structure. Using density evolution on their associated protographs, we find examples of rate-1/2 ARAA codes with maximum variable node degree 4 for which a minimum bit-SNR as low as 0.21 dB from the channel capacity limit can be achieved as the block size goes to infinity. Such a low threshold cannot be achieved by RA or irregular RA (IRA) or unstructured irregular LDPC codes with the same constraint on the maximum variable node degree. Furthermore by puncturing the accumulators we can construct families of higher rate ARAA codes with thresholds that stay close to their respective channel capacity thresholds uniformly. Iterative decoding simulation results show comparable performance with the best-known LDPC codes but with very low error floor even at moderate block sizes.

## An improved quasi-cyclic low-density parity-check code for memory channels

- **Status**: ✅
- **Reason**: 개선된 circulant QC-LDPC 구성 + BP 복잡도 저감 디코딩법 — 코드설계(E)/디코더(C) 이식 가능, memory channel 대상
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1400515
- **Type**: conference
- **Published**: 2004
- **Authors**: M. Jayabalan, H. M. Kwon
- **PDF**: https://ieeexplore.ieee.org/document/1400515
- **Abstract**: This paper presents an improved construction of circulant sub-matrices based quasi-cyclic low density parity check codes (QC-LDPC) under fading channels. The proposed construction yields a performance gain of about 2 to 5 dB at a 10/sup -4/ bit error rate (BER). This paper also proposes a decoding method to reduce the implementation complexity in the belief propagation algorithm. Furthermore, this paper studies the performance of circulant sub-matrices based QC-LDPC codes at higher rates under AWGN and fading channels.

## Memory-based low density parity check code decoder architecture using loosely coupled two data-flows

- **Status**: ✅
- **Reason**: D: memory-based parallel LDPC decoder architecture (scalable, segmented memory scheduling), 디지털 HW 이식 가능
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:1329292
- **Type**: conference
- **Published**: 2004
- **Authors**: Se-Hyeon Kang, In-Cheol Park
- **PDF**: https://ieeexplore.ieee.org/document/1329292
- **Abstract**: To achieve high throughput, parallel decoding of low density parity check (LDPC) codes is required, but needs a large set of registers and complex interconnection due to randomly located 1's in a sparse parity check matrix of large block size. This paper proposes a memory-based decoding architecture for low density parity check codes using loosely coupled two data flows. Instead of register, intermediate values are optimally grouped and scheduled to store into the segmented memory, which reduces large area and enables a scalable architecture. The performance of the proposed decoder architecture is demonstrated by implementing a 1024 bit, rate-1/2 LDPC codes decoder.

## Accumulate repeat accumulate codes

- **Status**: ✅
- **Reason**: ARA는 LDPC 부분집합, 프로토그래프 기반 구성+밀도진화 — 바이너리 LDPC 코드설계 이식(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1365542
- **Type**: conference
- **Published**: 2004
- **Authors**: A. Abbasfar, D. Divsalar, K. Yao
- **PDF**: https://ieeexplore.ieee.org/document/1365542
- **Abstract**: An innovative channel coding scheme called "accumulate repeat accumulate codes" (ARA) is proposed. ARA codes can be viewed as a subclass of low density parity check (LDPC) codes with fast encoder, and they have a projected graph or protograph representation. Using density evolution on their associated protographs, we find examples of rate 1/2 ARA codes with maximum variable node degree 5 for which a minimum bit SNR as low as 0.08 dB from channel capacity can be achieved as the block size goes to infinity. A family of high rate ARA codes with thresholds that stay uniformly close to their respective channel capacity thresholds are constructed. The ensemble weight distribution and ML threshold for rate 1/2 ARA codes were computed. For ARA with repeat 4, the ML threshold approaches within 0.005 dB of the ML threshold of random codes based on the existing tightest closed form bound.

## Design methodology for IRA codes

- **Status**: ✅
- **Reason**: IRA(LDPC 일종) 디코더 아키텍처+RAM 충돌 없는 Tanner 그래프 공동설계, HW·코드설계 이식 가능(D/E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1337619
- **Type**: conference
- **Published**: 2004
- **Authors**: F. Kienle, N. Wehn
- **PDF**: https://ieeexplore.ieee.org/document/1337619
- **Abstract**: Channel coding is an important building block in communication systems since it ensures the quality of service. Irregular repeat-accumulate (IRA) codes belong to the class of low-density parity-check (LDPC) codes and even outperform the recently introduced turbo-codes of current communication standards. IRA codes can be represented by a Tanner graph with arbitrary connections between nodes of given degrees. The implementation complexity of an IRA decoders is dominated by the randomness of these connections. We present for the first time an IRA decoder architecture which can process any given IRA code. We developed a joint graph-decoder design methodology to construct the Tanner graph of a given IRA code which can be efficiently processed by this decoder architecture without any RAM access conflicts. We show that these constructed IRA codes can outperform the UMTS turbo-codes.

## LDPC block and convolutional codes based on circulant matrices

- **Status**: ✅
- **Reason**: circulant 기반 QC-LDPC 및 convolutional 구성, girth·최소거리 bound·인코딩 기법 제시 — 바이너리 코드설계 이식 가능(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1362891
- **Type**: journal
- **Published**: 2004
- **Authors**: R. M. Tanner, D. Sridhara, A. Sridharan +2
- **PDF**: https://ieeexplore.ieee.org/document/1362891
- **Abstract**: A class of algebraically structured quasi-cyclic (QC) low-density parity-check (LDPC) codes and their convolutional counterparts is presented. The QC codes are described by sparse parity-check matrices comprised of blocks of circulant matrices. The sparse parity-check representation allows for practical graph-based iterative message-passing decoding. Based on the algebraic structure, bounds on the girth and minimum distance of the codes are found, and several possible encoding techniques are described. The performance of the QC LDPC block codes compares favorably with that of randomly constructed LDPC codes for short to moderate block lengths. The performance of the LDPC convolutional codes is superior to that of the QC codes on which they are based; this performance is the limiting performance obtained by increasing the circulant size of the base QC code. Finally, a continuous decoding procedure for the LDPC convolutional codes is described.

## Improved progressive-edge-growth (PEG) construction of irregular LDPC codes

- **Status**: ✅
- **Reason**: E: 비정형 바이너리 LDPC PEG 구성 개선 — 코드설계 기법 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1369235
- **Type**: journal
- **Published**: 2004
- **Authors**: Hua Xiao, A. H. Banihashemi
- **PDF**: https://ieeexplore.ieee.org/document/1369235
- **Abstract**: Progressive-edge-growth (PEG) algorithm is known to construct low-density parity-check codes at finite block lengths with very good performance. In this letter, we propose a very simple modification to PEG construction for irregular codes, which considerably improves the performance at high signal-to-noise (SNR) ratios with no sacrifice in low-SNR performance.

## A more accurate one-dimensional analysis and design of irregular LDPC codes

- **Status**: ✅
- **Reason**: E: 비정형 바이너리 LDPC 1-D 분석·설계 기법 — 코드설계 이식 가능(단 이론성 강함, Phase3 재검토)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1369623
- **Type**: journal
- **Published**: 2004
- **Authors**: M. Ardakani, F. R. Kschischang
- **PDF**: https://ieeexplore.ieee.org/document/1369623
- **Abstract**: We introduce a new one-dimensional (1-D) analysis of low-density parity-check (LDPC) codes on additive white Gaussian noise channels which is significantly more accurate than similar 1-D methods. Our method assumes a Gaussian distribution in message-passing decoding only for messages from variable nodes to check nodes. Compared to existing work, which makes a Gaussian assumption both for messages from check nodes and from variable nodes, our method offers a significantly more accurate estimate of convergence behavior and threshold of convergence. Similar to previous work, the problem of designing irregular LDPC codes reduces to a linear programming problem. However, our method allows irregular code design in a wider range of rates without any limit on the maximum variable-node degree. We use our method to design irregular LDPC codes with rates greater than 1/4 that perform within a few hundredths of a decibel from the Shannon limit. The designed codes perform almost as well as codes designed by density evolution.

## Systematic recursive construction of LDPC codes

- **Status**: ✅
- **Reason**: QC-LDPC의 체계적/재귀적 구성으로 min-distance·girth 보존, 바이너리 LDPC 코드설계 (카테고리 E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1300585
- **Type**: journal
- **Published**: 2004
- **Authors**: N. Miladinovic, M. Fossorier
- **PDF**: https://ieeexplore.ieee.org/document/1300585
- **Abstract**: This letter presents a systematic and recursive method to construct good low-density parity-check (LDPC) codes, especially those with high rate. The proposed method uses a parity check matrix of a quasi-cyclic LDPC code with given row and column weights as a core upon which the larger code is recursively constructed with extensive use of pseudorandom permutation matrices. This construction preserves the minimum distance and girth properties of the core matrix and can generate either regular, or irregular LDPC codes. The method provides a unique representation of the code in compact notation.

## Memory-efficient sum-product decoding of LDPC codes

- **Status**: ✅
- **Reason**: 메모리 효율적 sum-product 디코딩 + density evolution 기반 코드설계 — HW 메모리 절감(D)과 디코더 변형(C)으로 NAND LDPC에 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1327834
- **Type**: journal
- **Published**: 2004
- **Authors**: H. Sankar, K. R. Narayanan
- **PDF**: https://ieeexplore.ieee.org/document/1327834
- **Abstract**: Low-density parity-check (LDPC) codes perform very close to capacity for long lengths on several channels. However, the amount of memory (fixed-point numbers that need to be stored) required for implementing the message-passing algorithm increases linearly as the number of edges in the graph increases. In this letter, we propose a decoding algorithm for decoding LDPC codes that reduces the memory requirement at the decoder. The proposed decoding algorithm can be analyzed using density evolution; further, we show how to design good LDPC codes using this. Results show that this algorithm provides almost the same performance as the conventional sum-product decoding of LDPC codes.

## Efficiency of short LDPC codes combined with long Reed-Solomon codes for magnetic recording channels

- **Status**: ✅
- **Reason**: B — 자기기록(스토리지)용 단블록 LDPC + RS 연접, 반복디코딩 오류분포·버퍼/HW 관점; 스토리지 ECC로 직접 관련
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1325738
- **Type**: journal
- **Published**: 2004
- **Authors**: T. Morita, M. Ohta, T. Sugawara
- **PDF**: https://ieeexplore.ieee.org/document/1325738
- **Abstract**: This paper proposes the use of low-density parity check (LDPC) codes with short block lengths such as 1-K bits for magnetic recording. In general, there is a degradation in bit error rate as the block length of the LDPC codes decreases. Yet, we show that short LDPC codes do not suffer from degraded sector-error-rate performance if the sector size is 32 K bits and if long Reed-Solomon codes over GF(2/sup 12/) are used. This is due to the unique error distribution of iterative decoding. Shorter codes significantly reduce the amount of buffer memory in the iterative decoder and make hardware implementation more feasible.

## Graph-based message-passing schedules for decoding LDPC codes

- **Status**: ✅
- **Reason**: C: girth 기반 메시지패싱 스케줄, min-sum/BP 적용 — 바이너리 LDPC 디코더 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1369622
- **Type**: journal
- **Published**: 2004
- **Authors**: Hua Xiao, A. H. Banihashemi
- **PDF**: https://ieeexplore.ieee.org/document/1369622
- **Abstract**: We study a wide range of graph-based message-passing schedules for iterative decoding of low-density parity-check (LDPC) codes. Using the Tanner graph (TG) of the code and for different nodes and edges of the graph, we relate the first iteration in which the corresponding messages deviate from their optimal value (corresponding to a cycle-free graph) to the girths and the lengths of the shortest closed walks in the graph. Using this result, we propose schedules, which are designed based on the distribution of girths and closed walks in the TG of the code, and categorize them as node based versus edge based, unidirectional versus bidirectional, and deterministic versus probabilistic. These schedules, in some cases, outperform the previously known schedules, and in other cases, provide less complex alternatives with more or less the same performance. The performance/complexity tradeoff and the best choice of schedule appear to depend not only on the girth and closed-walk distributions of the TG, but also on the iterative decoding algorithm and channel characteristics. We examine the application of schedules to belief propagation (sum-product) over additive white Gaussian noise (AWGN) and Rayleigh fading channels, min-sum (max-sum) over an AWGN channel, and Gallager's algorithm A over a binary symmetric channel.

## Selective avoidance of cycles in irregular LDPC code construction

- **Status**: ✅
- **Reason**: EMD 기반 사이클 선택적 회피로 error floor 개선 — 바이너리 LDPC 코드설계(E) 신규 기법, 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1327837
- **Type**: journal
- **Published**: 2004
- **Authors**: Tao Tian, C. R. Jones, J. D. Villasenor +1
- **PDF**: https://ieeexplore.ieee.org/document/1327837
- **Abstract**: This letter explains the effect of graph connectivity on error-floor performance of low-density parity-check (LDPC) codes under message-passing decoding. A new metric, called extrinsic message degree (EMD), measures cycle connectivity in bipartite graphs of LDPC codes. Using an easily computed estimate of EMD, we propose a Viterbi-like algorithm that selectively avoids small cycle clusters that are isolated from the rest of the graph. This algorithm is different from conventional girth conditioning by emphasizing the connectivity as well as the length of cycles. The algorithm yields codes with error floors that are orders of magnitude below those of random codes with very small degradation in capacity-approaching capability.

## Design of efficiently encodable moderate-length high-rate irregular LDPC codes

- **Status**: ✅
- **Reason**: 이식 가능 코드설계(E): moderate-length 고rate irregular LDPC 구성+error floor 저감+density/differential evolution 설계, 바이너리 LDPC. NAND 고rate ECC에 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1291797
- **Type**: journal
- **Published**: 2004
- **Authors**: M. Yang, W. E. Ryan, Yan Li
- **PDF**: https://ieeexplore.ieee.org/document/1291797
- **Abstract**: This paper presents a new class of irregular low-density parity-check (LDPC) codes of moderate length (10/sup 3//spl les/n/spl les/10/sup 4/) and high rate (R/spl ges/3/4). Codes in this class admit low-complexity encoding and have lower error-rate floors than other irregular LDPC code-design approaches. It is also shown that this class of LDPC codes is equivalent to a class of systematic serial turbo codes and is an extension of irregular repeat-accumulate codes. A code design algorithm based on the combination of density evolution and differential evolution optimization with a modified cost function is presented. Moderate-length, high-rate codes with no error-rate floors down to a bit-error rate of 10/sup -9/ are presented. Although our focus is on moderate-length, high-rate codes, the proposed coding scheme is applicable to irregular LDPC codes with other lengths and rates.

## Joint (3,k)-regular LDPC code and decoder/encoder design

- **Status**: ✅
- **Reason**: D/E: (3,k)-정규 LDPC 코드+부분병렬 디코더/저복잡도 인코더 HW 공동설계, 디지털 HW 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1275678
- **Type**: journal
- **Published**: 2004
- **Authors**: Tong Zhang, K. K. Parhi
- **PDF**: https://ieeexplore.ieee.org/document/1275678
- **Abstract**: Recently, low-density parity-check (LDPC) codes have attracted a lot of attention in the coding theory community. However, their real-world applications are still problematic mainly due to the lack of effective decoder/encoder hardware design approaches. In this paper, we present a joint (3,k)-regular LDPC code and decoder/encoder design technique to construct a class of (3,k)-regular LDPC codes that not only have very good error-correcting capability but also exactly fit to high-speed partly parallel decoder and low-complexity encoder implementations. We also develop two techniques to further modify this joint design scheme to achieve more flexible tradeoffs between decoder hardware complexity and decoding speed.

## Several properties of short LDPC codes

- **Status**: ✅
- **Reason**: 짧은 바이너리 LDPC의 min-distance/girth 유한길이 코드설계 분석 (카테고리 E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1299062
- **Type**: journal
- **Published**: 2004
- **Authors**: Lei Wei
- **PDF**: https://ieeexplore.ieee.org/document/1299062
- **Abstract**: In this paper, we present several properties on minimum distance(d/sub min/) and girth(G/sub min/) in Tanner graphs for low-density parity-check (LDPC) codes with small left degrees. We show that the distance growth of (2, 4) LDPC codes is too slow to achieve the desired performance. We further give a tight upper bound on the maximum possible girth. The numerical results show that codes with large G/sub min/ could outperform the average performance of regular ensembles of the LDPC codes over binary symmetric channels. The same codes perform about 1.5 dB away from the sphere-packing bound on additive white Gaussian noise channels.

## Enforcing maximum-transition-run code constraints and low-density parity-check decoding

- **Status**: ✅
- **Reason**: partial response 채널에서 MTR 제약을 LDPC 디코딩에 통합하는 log/max-log enforcer — 저장채널 LDPC 디코더 변형 기법으로 이식 검토 여지(B/C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1353468
- **Type**: journal
- **Published**: 2004
- **Authors**: R. M. Todd, J. R. Cruz
- **PDF**: https://ieeexplore.ieee.org/document/1353468
- **Abstract**: We present a novel algorithm for imposing the maximum-transition-run (MTR) code constraint in the decoding of low-density parity-check (LDPC) codes over a partial response channel. This algorithm provides a gain of about 0.2 dB. We also develop log and max-log versions of the MTR enforcer, similar to the well-known "log-MAP" (maximum a posteriori ) and "max-log-MAP" variants of the LDPC decoder, that have performance equivalent to that of the original version.

## Mapping interleaving laws to parallel turbo and LDPC decoder architectures

- **Status**: ✅
- **Reason**: 병렬 LDPC 디코더의 충돌 없는 메모리 매핑 알고리즘(코드설계 불필요) — 디지털 HW 병렬화 기법(D) 이식 가능
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:1327801
- **Type**: journal
- **Published**: 2004
- **Authors**: A. Tarable, S. Benedetto, G. Montorsi
- **PDF**: https://ieeexplore.ieee.org/document/1327801
- **Abstract**: For high-data-rate applications, the implementation of iterative turbo-like decoders requires the use of parallel architectures posing some collision-free constraints to the reading/writing process from/into the memory. This consideration applies to the two main classes of turbo-like codes, i.e., turbo codes and low-density parity-check (LDPC) codes. Contrary to the literature belief, we prove in this paper that there is no need for an ad hoc code design to meet the parallelism requirement, because, for any code and any choice of the scheduling of the reading/writing operations, there is a suitable mapping of the variables in the memory that grants a collision-free access. The proof is constructive, i.e., it gives an algorithm that obtains the desired collision-free mapping. The algorithm is applied to two simple examples, one for turbo codes and one for LDPC codes, to illustrate how the algorithm works.

## Explicit construction of families of LDPC codes with no 4-cycles

- **Status**: ✅
- **Reason**: E: 4-cycle 없는(girth 보장) 바이너리 LDPC 부호족의 명시적 구성, 코드설계 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1337111
- **Type**: journal
- **Published**: 2004
- **Authors**: Jon-Lark Kim, U. N. Peled, I. Perepelitsa +2
- **PDF**: https://ieeexplore.ieee.org/document/1337111
- **Abstract**: Low-density parity-check (LDPC) codes are serious contenders to turbo codes in terms of decoding performance. One of the main problems is to give an explicit construction of such codes whose Tanner graphs have known girth. For a prime power q and m/spl ges/2, Lazebnik and Ustimenko construct a q-regular bipartite graph D(m,q) on 2q/sup m/ vertices, which has girth at least 2/spl lceil/m/2/spl rceil/+4. We regard these graphs as Tanner graphs of binary codes LU(m,q). We can determine the dimension and minimum weight of LU(2,q), and show that the weight of its minimum stopping set is at least q+2 for q odd and exactly q+2 for q even. We know that D(2,q) has girth 6 and diameter 4, whereas D(3,q) has girth 8 and diameter 6. We prove that for an odd prime p, LU(3,p) is a [p/sup 3/,k] code with k/spl ges/(p/sup 3/-2p/sup 2/+3p-2)/2. We show that the minimum weight and the weight of the minimum stopping set of LU(3,q) are at least 2q and they are exactly 2q for many LU(3,q) codes. We find some interesting LDPC codes by our partial row construction. We also give simulation results for some of our codes.

## Efficient maximum-likelihood decoding of LDPC codes over the binary erasure channel

- **Status**: ✅
- **Reason**: C: BEC상 LDPC 효율적 ML 디코딩 알고리즘 — 디코더 알고리즘, 스토리지(erasure) 관련성 있어 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1347372
- **Type**: journal
- **Published**: 2004
- **Authors**: D. Burshtein, G. Miller
- **PDF**: https://ieeexplore.ieee.org/document/1347372
- **Abstract**: We propose an efficient maximum-likelihood (ML) decoding algorithm for decoding low-density parity-check (LDPC) codes over the binary-erasure channel (BEC). We also analyze the computational complexity of the proposed algorithm.

## Decoding of low-density parity-check codes over finite-state binary Markov channels

- **Status**: ✅
- **Reason**: finite-state Markov 채널용 수정 LDPC 디코딩 알고리즘 — 채널통계 활용 BP 변형으로 디코더 기법(C) 이식 가능, NAND retention/상관오류에 응용 여지
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1356191
- **Type**: journal
- **Published**: 2004
- **Authors**: J. Garcia-Frias
- **PDF**: https://ieeexplore.ieee.org/document/1356191
- **Abstract**: We propose a modified algorithm for decoding of low-density parity-check codes over finite-state binary Markov channels. The proposed approach clearly outperforms systems in which the channel statistics are not exploited in the decoding, even when the channel parameters are not known a priori at the decoder.

## Reliability-based schedule for bit-flipping decoding of low-density Parity-check codes

- **Status**: ✅
- **Reason**: C: bit-flipping 디코딩의 reliability-based 메시지패싱 스케줄 — 바이너리 LDPC 디코더 개선 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1369610
- **Type**: journal
- **Published**: 2004
- **Authors**: A. Nouh, A. H. Banihashemi
- **PDF**: https://ieeexplore.ieee.org/document/1369610
- **Abstract**: A reliability-based message-passing schedule for iterative decoding of low-density parity-check codes is proposed. Simulation results for bit-flipping algorithms (with binary messages) show that a reliability-based schedule can provide considerable improvement in performance and decoding speed over the so-called flooding (parallel) schedule, as well as the existing graph-based schedules. The cost associated with this improvement is negligible and is equivalent to having a two-bit representation for initial messages, instead of the standard one bit for hard-decision algorithms, only at the first iteration (all the exchanged messages are still binary).

## Threshold values and convergence properties of majority-based algorithms for decoding regular low-density parity-check codes

- **Status**: ✅
- **Reason**: C: majority-based 바이너리 메시지패싱 디코딩(저복잡도) 분석 — 단순 HW 디코더 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1369621
- **Type**: journal
- **Published**: 2004
- **Authors**: P. Zarrinkhat, A. H. Banihashemi
- **PDF**: https://ieeexplore.ieee.org/document/1369621
- **Abstract**: This work presents a detailed study of a family of binary message-passing decoding algorithms for low-density parity-check (LDPC) codes, referred to as "majority-based algorithms." Both Gallager's algorithm A (G/sub A/) and the standard majority decoding algorithm belong to this family. These algorithms, which are, in fact, the building blocks of Gallager's algorithm B (G/sub B/), work based on a generalized majority-decision rule and are particularly attractive for their remarkably simple implementation. We investigate the dynamics of these algorithms using density evolution and compute their (noise) threshold values for regular LDPC codes over the binary symmetric channel. For certain ensembles of codes and certain orders of majority-based algorithms, we show that the threshold value can be characterized as the smallest positive root of a polynomial, and thus can be determined analytically. We also study the convergence properties of majority-based algorithms, including their (convergence) speed. Our analysis shows that the stand-alone version of some of these algorithms provides significantly better performance and/or convergence speed compared with G/sub A/. In particular, it is shown that for channel parameters below threshold, while for G/sub A/ the error probability converges to zero exponentially with iteration number, this convergence for other majority-based algorithms is super-exponential.

## Design and performance of turbo Gallager codes

- **Status**: ✅
- **Reason**: turbo 코드를 LDPC BP로 디코딩하는 turbo Gallager — 부호 비의존적 메시지패싱 이식 + 완전병렬 디코딩 구조(C 예외 포함)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1356201
- **Type**: journal
- **Published**: 2004
- **Authors**: G. Colavolpe
- **PDF**: https://ieeexplore.ieee.org/document/1356201
- **Abstract**: The most powerful channel-coding schemes, namely, those based on turbo codes and low-density parity-check (LDPC) Gallager codes, have in common the principle of iterative decoding. However, the relative coding structures and decoding algorithms are substantially different. This paper shows that recently proposed novel coding structures bridge the gap between these two schemes. In fact, with properly chosen component convolutional codes, a turbo code can be successfully decoded by means of the decoding algorithm used for LDPC codes, i.e., the belief-propagation algorithm working on the code Tanner graph. These new turbo codes are here nicknamed "turbo Gallager codes." Besides being interesting from a conceptual viewpoint, these schemes are important on the practical side because they can be decoded in a fully parallel manner. In addition to the encoding complexity advantage of turbo codes, the low decoding complexity allows the design of very efficient channel-coding schemes.

## On the suboptimality of iterative decoding for turbo-like and LDPC codes with cycles in their graph representation

- **Status**: ✅
- **Reason**: 그래프 cycle로 인한 iterative decoding 준최적성을 reliability 기반으로 보정 — LDPC BP에 이식 가능 (카테고리 C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1299074
- **Type**: journal
- **Published**: 2004
- **Authors**: M. Isaka, M. P. C. Fossorier, H. Imai
- **PDF**: https://ieeexplore.ieee.org/document/1299074
- **Abstract**: In this paper, we focus on the suboptimality of iterative decoding on graphs with cycles, through examining the use of a reliability-based decoding algorithm for some concatenated codes with an interleaver, known as turbo-like codes. The a posteriori probabilities delivered by the iterative decoding are regarded as reliability information, and an efficient algorithm for the overall linear block code is applied at certain iterations. Simulation results show that the suboptimality of iterative decoding due to cycles can be at least partially compensated by this approach. Some insights about the potential additional coding gains achievable are investigated based on the characteristics of the constituent decoders. These characteristics are related to the nature of suboptimality in the overall iterative decoding. The effects of some code parameters and channel conditions on the behavior of iterative decoding are also studied for a better understanding of its suboptimality.

## Design and Performance of Turbo Gallager Codes

- **Status**: ✅
- **Reason**: turbo 코드를 LDPC BP(Tanner graph belief-propagation)로 디코딩하는 부호 비의존적 메시지패싱 기법 — 바이너리 LDPC BP 이식 예외 포함(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1350932
- **Type**: journal
- **Published**: 2004
- **Authors**: 
- **PDF**: https://ieeexplore.ieee.org/document/1350932
- **Abstract**: Design and Performance of Turbo Gallager Codes The most powerful channel-coding schemes, namely those based on turbo codes and low-density parity-check (LDPC) Gallager codes, have in common the principle of iterative decoding. However, the relative coding structures and decoding algorithms are substantially different. This paper shows that recently proposed novel coding structures bridge the gap between these two schemes. In fact, with properly chosen component convolutional codes, a turbo code can be successfully decoded by means of the decoding algorithm used for LDPC codes, i.e., the belief-propagation algorithm working on the code Tanner graph. These new turbo codes are here nicknamed “turbo Gallager codes.” Besides being interesting from a conceptual viewpoint, these schemes are important on the practical side, because they can be decoded in a fully parallel manner. In addition to the encoding complexity advantage of turbo codes, the low decoding complexity allows the design of very efficient channel-coding schemes.

## On decoding of low-density parity-check codes over the binary erasure channel

- **Status**: ✅
- **Reason**: 바이너리 LDPC의 개선된 디코딩 알고리즘(C)·유한길이 그래프 특성; BEC 한정이나 애매하므로 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1273654
- **Type**: journal
- **Published**: 2004
- **Authors**: H. Pishro-Nik, F. Fekri
- **PDF**: https://ieeexplore.ieee.org/document/1273654
- **Abstract**: This paper investigates decoding of low-density parity-check (LDPC) codes over the binary erasure channel (BEC). We study the iterative and maximum-likelihood (ML) decoding of LDPC codes on this channel. We derive bounds on the ML decoding of LDPC codes on the BEC. We then present an improved decoding algorithm. The proposed algorithm has almost the same complexity as the standard iterative decoding. However, it has better performance. Simulations show that we can decrease the error rate by several orders of magnitude using the proposed algorithm. We also provide some graph-theoretic properties of different decoding algorithms of LDPC codes over the BEC which we think are useful to better understand the LDPC decoding methods, in particular, for finite-length codes.

## Performance of efficiently encodable low-density parity-check codes in noise bursts on the EPR4 channel

- **Status**: ✅
- **Reason**: 바이너리 LDPC를 스토리지 ECC로 단독사용, noise burst(미디어 결함) 견고성 — 스토리지 LDPC(B) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1284454
- **Type**: journal
- **Published**: 2004
- **Authors**: M. Yang, W. E. Ryan
- **PDF**: https://ieeexplore.ieee.org/document/1284454
- **Abstract**: We consider in this paper the possibility of using a low-density parity-check (LDPC) code as the complete error control system in a magnetic recording channel. We compare the performance of selected LDPC codes with two Reed-Solomon (RS) code schemes on an extended partial-response class 4 (EPR4) channel, with particular emphasis on their performance in noise bursts (induced by media defects or thermal asperities). We quantify the performance of LDPC codes in noise bursts via a maximum-burst-length parameter, and we present a simple algorithm for computing this parameter. We find some very promising initial results: the LDPC codes are very robust against large noise bursts (128 bits long or more), and are superior to the RS schemes examined in the measurable error rate region. The extent to which they are superior depends on the particular LDPC scheme involved, and the results provide motivation for further investigation in this area.

## Design of Efficiently Encodable Moderate-Length High-Rate Irregular LDPC Codes

- **Status**: ✅
- **Reason**: E: 중간길이 고율 불규칙 LDPC 구성+낮은 error floor 설계(밀도진화 기반), 바이너리 LDPC 코드설계 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1273707
- **Type**: journal
- **Published**: 2004
- **Authors**: 
- **PDF**: https://ieeexplore.ieee.org/document/1273707
- **Abstract**: This paper presents a new class of irregular low-density parity-check (LDPC) codes of the moderate length<tex>$(10^3le n le 10^4)$</tex>and high rate<tex>$(R ge 3/4)$</tex>. Codes in this class admit low-complexity encoding and have lower error-rate floors than other irregular LDPC code design approaches. It is also shown that this class of LDPC codes is equivalent to a class of systematic serial turbo codes, and is an extension of irregular repeat-accumulate codes. A code design algorithm based on the combination of density evolution and differential evolution optimization with a modified cost function is presented. Moderate-length, high-rate codes with no error-rate floors down to a bit-error rate of<tex>$10^-9$</tex>are presented. Although our focus is on moderate-length, high-rate codes, the proposed coding scheme is applicable to irregular LDPC codes with other lengths and rates.

## Several Properties of Short LDPC Codes

- **Status**: ✅
- **Reason**: 이식 가능 코드설계(E): 짧은 바이너리 LDPC의 minimum distance·girth 상한 등 유한길이 구조 특성, NAND 짧은 코드 설계에 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1291813
- **Type**: journal
- **Published**: 2004
- **Authors**: 
- **PDF**: https://ieeexplore.ieee.org/document/1291813
- **Abstract**: We present several properties on minimum distance$(d_min)$and girth$(G_min)$in Tanner graphs for low-density parity-check (LDPC) codes with small left degrees. We show that the distance growth of (2, 4) LDPC codes is too slow to achieve the desired performance. We further give a tight upper bound on the maximum possible girth. The numerical results show that codes with large$G_min$could outperform the average performance of regular ensembles of the LDPC codes over binary symmetric channels. The same codes perform about 1.5 dB away from the sphere-packing bound on additive white Gaussian noise channels.

## Projective-plane iteratively decodable block codes for WDM high-speed long-haul transmission systems

- **Status**: ✅
- **Reason**: 유한기하(projective/affine plane) QC-LDPC 구성+min-sum/bit-flipping, error floor 우수 — 바이너리 LDPC 코드설계(E) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1281931
- **Type**: journal
- **Published**: 2004
- **Authors**: I. B. Djordjevic, S. Sankaranarayanan, B. V. Vasic
- **PDF**: https://ieeexplore.ieee.org/document/1281931
- **Abstract**: Low-density parity-check (LDPC) codes are excellent candidates for optical network applications due to their inherent low complexity of both encoders and decoders. A cyclic or quasi-cyclic form of finite geometry LDPC codes simplifies the encoding procedure. In addition, the complexity of an iterative decoder for such codes, namely the min-sum algorithm, is lower than the complexity of a turbo or Reed-Solomon decoder. In fact, simple hard-decoding algorithms such as the bit-flipping algorithm perform very well on codes from projective planes. In this paper, the authors consider LDPC codes from affine planes, projective planes, oval designs, and unitals. The bit-error-rate (BER) performance of these codes is significantly better than that of any other known foward-error correction techniques for optical communications. A coding gain of 9-10 dB at a BER of 10/sup -9/, depending on the code rate, demonstrated here is the best result reported so far. In order to assess the performance of the proposed coding schemes, a very realistic simulation model is used that takes into account in a natural way all major impairments in long-haul optical transmission such as amplified spontaneous emission noise, pulse distortion due to fiber nonlinearities, chromatic dispersion, crosstalk effects, and intersymbol interference. This approach gives a much better estimate of the code's performance than the commonly used additive white Gaussian noise channel model.

## Codes for iterative decoding from partial geometries

- **Status**: ✅
- **Reason**: 부분기하 기반 신규 바이너리 LDPC 부호 구성(E), girth·최소거리 분석, 성능·복잡도 개선
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1269971
- **Type**: journal
- **Published**: 2004
- **Authors**: S. J. Johnson, S. R. Weller
- **PDF**: https://ieeexplore.ieee.org/document/1269971
- **Abstract**: This paper develops codes suitable for iterative decoding using the sum-product algorithm. By considering a large class of combinatorial structures, known as partial geometries, we are able to define classes of low-density parity-check (LDPC) codes, which include several previously known families of codes as special cases. The existing range of algebraic LDPC codes is limited, so the new families of codes obtained by generalizing to partial geometries significantly increase the range of choice of available code lengths and rates. We derive bounds on minimum distance, rank, and girth for all the codes from partial geometries, and present constructions and performance results for the classes of partial geometries which have not previously been proposed for use with iterative decoding. We show that these new codes can achieve improved error-correction performance over randomly constructed LDPC codes and, in some cases, achieve this with a significant decrease in decoding complexity.

## A modified weighted bit-flipping decoding of low-density Parity-check codes

- **Status**: ✅
- **Reason**: C: 수정 가중치 비트플리핑(WBF) 디코딩 알고리즘 개선, 바이너리 LDPC 디코더 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1278309
- **Type**: journal
- **Published**: 2004
- **Authors**: Juntan Zhang, M. P. C. Fossorier
- **PDF**: https://ieeexplore.ieee.org/document/1278309
- **Abstract**: In this letter, a modified weighted bit-flipping decoding algorithm for low-density parity-check codes is proposed. Improvement in performance is observed by considering both the check constraint messages and the intrinsic message for each bit.

## Quasicyclic low-density parity-check codes from circulant permutation matrices

- **Status**: ✅
- **Reason**: 순환순열행렬 기반 QC-LDPC 구성과 girth 6/8/10/12 필요충분조건, 최소거리 조건 제시 — 바이너리 QC-LDPC 코드설계 기법(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1317123
- **Type**: journal
- **Published**: 2004
- **Authors**: M. P. C. Fossorier
- **PDF**: https://ieeexplore.ieee.org/document/1317123
- **Abstract**: In this correspondence, the construction of low-density parity-check (LDPC) codes from circulant permutation matrices is investigated. It is shown that such codes cannot have a Tanner graph representation with girth larger than 12, and a relatively mild necessary and sufficient condition for the code to have a girth of 6, 8,10, or 12 is derived. These results suggest that families of LDPC codes with such girth values are relatively easy to obtain and, consequently, additional parameters such as the minimum distance or the number of redundant check sums should be considered. To this end, a necessary condition for the codes investigated to reach their maximum possible minimum Hamming distance is proposed.

## Overlapped message passing for quasi-cyclic low-density parity check codes

- **Status**: ✅
- **Reason**: QC-LDPC용 overlapped message passing 고처리율 디코더 스케줄링·메모리충돌 회피 — 이식 가능 HW 아키텍처(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:1304967
- **Type**: journal
- **Published**: 2004
- **Authors**: Yanni Chen, K. K. Parhi
- **PDF**: https://ieeexplore.ieee.org/document/1304967
- **Abstract**: In this paper, a systematic approach is proposed to develop a high throughput decoder for quasi-cyclic low-density parity check (LDPC) codes, whose parity check matrix is constructed by circularly shifted identity matrices. Based on the properties of quasi-cyclic LDPC codes, the two stages of belief propagation decoding algorithm, namely, check node update and variable node update, could be overlapped and thus the overall decoding latency is reduced. To avoid the memory access conflict, the maximum concurrency of the two stages is explored by a novel scheduling algorithm. Consequently, the decoding throughput could be increased by about twice assuming dual-port memory is available.

## On construction of rate-compatible low-density Parity-check codes

- **Status**: ✅
- **Reason**: E: puncturing/extending 기반 rate-compatible 바이너리 LDPC 구성 기법, NAND ECC로 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1278307
- **Type**: journal
- **Published**: 2004
- **Authors**: M. R. Yazdani, A. H. Banihashemi
- **PDF**: https://ieeexplore.ieee.org/document/1278307
- **Abstract**: In this letter, we present a framework for constructing rate-compatible low-density parity-check (LDPC) codes. The codes are linear-time encodable and are constructed from a mother code using puncturing and extending. Application of the proposed construction to a type-II hybrid automatic repeat request (ARQ) scheme with information block length k=1024 and code rates 8/19 to 8/10, using an optimized irregular mother code of rate 8/13, results in a throughput which is only about 0.7 dB away from Shannon limit. This outperforms existing similar schemes based on turbo codes and LDPC codes by up to 0.5 dB.

## On algebraic construction of Gallager and circulant low-density parity-check codes

- **Status**: ✅
- **Reason**: 유한기하 기반 Gallager·circulant/QC LDPC 신규 대수적 구성 — 바이너리 LDPC 코드 설계(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1302304
- **Type**: journal
- **Published**: 2004
- **Authors**: Heng Tang, Jun Xu, Yu Kou +2
- **PDF**: https://ieeexplore.ieee.org/document/1302304
- **Abstract**: This correspondence presents three algebraic methods for constructing low-density parity-check (LDPC) codes. These methods are based on the structural properties of finite geometries. The first method gives a class of Gallager codes and a class of complementary Gallager codes. The second method results in two classes of circulant-LDPC codes, one in cyclic form and the other in quasi-cyclic form. The third method is a two-step hybrid method. Codes in these classes have a wide range of rates and minimum distances, and they perform well with iterative decoding.

## Information geometry of turbo and low-density parity-check codes

- **Status**: ✅
- **Reason**: LDPC 디코딩의 정보기하 분석에서 근사 개선용 correction term 제안 — BP 디코더 개선 기여로 살림 (C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1302292
- **Type**: journal
- **Published**: 2004
- **Authors**: S. Ikeda, T. Tanaka, S. Amari
- **PDF**: https://ieeexplore.ieee.org/document/1302292
- **Abstract**: Since the proposal of turbo codes in 1993, many studies have appeared on this simple and new type of codes which give a powerful and practical performance of error correction. Although experimental results strongly support the efficacy of turbo codes, further theoretical analysis is necessary, which is not straightforward. It is pointed out that the iterative decoding algorithm of turbo codes shares essentially similar ideas with low-density parity-check (LDPC) codes, with Pearl's belief propagation algorithm applied to a cyclic belief diagram, and with the Bethe approximation in statistical physics. Therefore, the analysis of the turbo decoding algorithm will reveal the mystery of those similar iterative methods. In this paper, we recapture and extend the geometrical framework initiated by Richardson to the information geometrical framework of dual affine connections, focusing on both of the turbo and LDPC decoding algorithms. The framework helps our intuitive understanding of the algorithms and opens a new prospect of further analysis. We reveal some properties of these codes in the proposed framework, including the stability and error analysis. Based on the error analysis, we finally propose a correction term for improving the approximation.

## Performance evaluation of low-density parity-check codes on partial-response channels using density evolution

- **Status**: ✅
- **Reason**: PR 채널 LDPC 성능을 density evolution으로 평가 — NAND도 ISI/PR-유사 채널이며 DE 분석 기법은 이식 여지, 애매하여 in 유지
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1327839
- **Type**: journal
- **Published**: 2004
- **Authors**: W. Tan, J. R. Cruz
- **PDF**: https://ieeexplore.ieee.org/document/1327839
- **Abstract**: A method to evaluate the performance of a low-density parity-check (LDPC) code on partial-response (PR) channels in terms of the noise threshold and decoding error is presented. Given a particular codeword or assuming an independent and uniformly distributed (i.u.d.) codeword for transmission, the density-evolution algorithm is used to compute the probability density function of messages passing in the decoding process, from which the decoding error is extracted. This estimated i.u.d. decoding error is used to approximate the decoding error of an ensemble of LDPC codes on arbitrary PR channels. Comparison with simulation results shows that it is a very good approximation for the simulated codes, provided their length is large enough.

## Block-circulant low-density parity-check codes for optical communication systems

- **Status**: ✅
- **Reason**: block-circulant 구조 LDPC 신규 구성(cycle-invariant 차집합), girth≥6, 빠른 인코딩 — 광통신 도메인이나 바이너리 LDPC 코드 설계(E) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1303577
- **Type**: journal
- **Published**: 2004
- **Authors**: O. Milenkovic, I. B. Djordjevic, B. Vasic
- **PDF**: https://ieeexplore.ieee.org/document/1303577
- **Abstract**: A novel family of structured low-density parity-check (LDPC) codes with block-circulant parity-check matrices that consist of permutation blocks is proposed. The codes from this family are based on new combinatorial objects termed cycle-invariant difference sets, and they have low storage requirements, fast encoding algorithms, and girth of at least six. Most importantly, they tend to outperform many other known structured LDPCs of comparable rate and length.

## Hybrid hard-decision iterative decoding of regular low-density parity-check codes

- **Status**: ✅
- **Reason**: 이식 가능 디코더(C): regular 바이너리 LDPC용 time-invariant hybrid 메시지패싱 알고리즘으로 BER/복잡도 개선, density evolution 분석. NAND 디코더에 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1294940
- **Type**: journal
- **Published**: 2004
- **Authors**: P. Zarrinkhat, A. H. Banihashemi
- **PDF**: https://ieeexplore.ieee.org/document/1294940
- **Abstract**: Hybrid decoding means to combine different iterative decoding algorithms with the aim of improving error performance or decoding complexity. In this work, we introduce "time-invariant" hybrid (H/sub TI/) algorithms, and using density evolution show that for regular low-density parity-check (LDPC) codes and binary message-passing algorithms, H/sub TI/ algorithms perform remarkably better than their constituent algorithms. We also show that compared to "switch-type" hybrid (H/sub ST/) algorithms, such as Gallager's algorithm B, where a comparable improvement is obtained by switching between different iterative decoding algorithms, H/sub TI/ algorithms are far less sensitive to channel conditions and thus can be practically more attractive.

## On general linear block code decoding using the sum-product iterative decoder

- **Status**: ✅
- **Reason**: sum-product 반복 디코더의 일반 선형부호 적용 분석 — 디코더 동작/패리티검사 weight 영향 분석으로 LDPC BP 이해/개선에 이식 가능(C). 애매하나 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1306428
- **Type**: journal
- **Published**: 2004
- **Authors**: T. K. Moon
- **PDF**: https://ieeexplore.ieee.org/document/1306428
- **Abstract**: The sum-product iterative decoder, conventionally used for low-density parity-check (LDPC) codes, hold promise as a decoder for general linear block code decoding. However, the promise is only partly fulfilled because, as we show experimentally, the decoder performance degrades rapidly as a function of parity check matrix weight. Even in the case of decoder failure, however, we demonstrate that there is information present in the decoder output probabilities that can still help with the decoding problem.

## On concatenated zigzag codes and their decoding schemes

- **Status**: ✅
- **Reason**: concatenated zigzag을 LDPC로 보고 개선된 sum-product 변형 디코더 제시 — 부호 비의존적 BP 개선으로 바이너리 LDPC 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1261925
- **Type**: journal
- **Published**: 2004
- **Authors**: Xiaofu Wu, Yingjian Xue, Haige Xiang
- **PDF**: https://ieeexplore.ieee.org/document/1261925
- **Abstract**: In this letter, we show that a concatenated zigzag code can be viewed as a low-density parity-check (LDPC) code. Based on the bipartite graph representation for such a parallel-concatenated code, various sum-product based decoding algorithms are introduced and compared. The results show that the improved versions of sum-product algorithm exhibit better convergence rate while maintaining the essential parallel form.

## Threshold of LDPC-coded BICM for Rayleigh fading

- **Status**: ✅
- **Reason**: LDPC-coded BICM의 density evolution/EXIT 임계값 분석 + 불규칙 코드설계 예시; E 유한/불규칙 LDPC 코드설계 기법 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1315675
- **Type**: journal
- **Published**: 2004
- **Authors**: Huaning Niu, M. Shen, J. A. Ritcey
- **PDF**: https://ieeexplore.ieee.org/document/1315675
- **Abstract**: We analyze the threshold and convergence of LDPC coded bit interleaved coded modulation over Rayleigh fading channels. We compute the system threshold using the discretized density evolution and the extrinsic information transfer (EXIT) chart, and verify its effectiveness by simulation. Simulated detector output pdf is used to compute the variable node EXIT curve. It is shown that the convergence SNR observed from the transfer curves matches the density evolution threshold perfectly, and the EXIT chart actually provides a more computational efficient approach to estimate the threshold. An irregular code design example using the EXIT chart is given.

## Extrinsic information transfer functions: model and erasure channel properties

- **Status**: ✅
- **Reason**: C/E: EXIT 차트 모델·면적정리로 용량근접 LDPC 설계를 곡선맞춤으로 환원 — 코드설계 분석기법 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1347354
- **Type**: journal
- **Published**: 2004
- **Authors**: A. Ashikhmin, G. Kramer, S. ten Brink
- **PDF**: https://ieeexplore.ieee.org/document/1347354
- **Abstract**: Extrinsic information transfer (EXIT) charts are a tool for predicting the convergence behavior of iterative processors for a variety of communication problems. A model is introduced that applies to decoding problems, including the iterative decoding of parallel concatenated (turbo) codes, serially concatenated codes, low-density parity-check (LDPC) codes, and repeat-accumulate (RA) codes. EXIT functions are defined using the model, and several properties of such functions are proved for erasure channels. One property expresses the area under an EXIT function in terms of a conditional entropy. A useful consequence of this result is that the design of capacity-approaching codes reduces to a curve-fitting problem for all the aforementioned codes. A second property relates the EXIT function of a code to its Helleseth-Klove-Levenshtein information functions, and thereby to the support weights of its subcodes. The relation is via a refinement of information functions called split information functions, and via a refinement of support weights called split support weights. Split information functions are used to prove a third property that relates the EXIT function of a linear code to the EXIT function of its dual.

## Rate-compatible puncturing of low-density parity-check codes

- **Status**: ✅
- **Reason**: E: LDPC rate-compatible 펑처링 패턴 설계(단일 mother 인코더/디코더로 다중 rate) — 코드설계 기법 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1347371
- **Type**: journal
- **Published**: 2004
- **Authors**: Jeongseok Ha, Jaehong Kim, S. W. McLaughlin
- **PDF**: https://ieeexplore.ieee.org/document/1347371
- **Abstract**: In this correspondence, we consider puncturing of low-density parity-check (LDPC) codes for additive white Gaussian noise (AWGN) channels. We show that good puncturing patterns exist and that the puncturing can be performed in a rate-compatible fashion. Furthermore, rate-compatible puncturing results in a small loss of performance with respect to threshold, namely, the punctured code is good (in terms of threshold) across a range of rates when compared with the optimal codes for each rate. This allows one to implement a single "mother" encoder and decoder that is good across a wide range of rates.

## Combinatorial constructions of low-density parity-check codes for iterative decoding

- **Status**: ✅
- **Reason**: 조합론 기반 정규 Gallager LDPC 신규 구성(차집합족·affine 구성), 저복잡도 구현 지향 — 바이너리 LDPC 코드 설계 기법(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1302295
- **Type**: journal
- **Published**: 2004
- **Authors**: B. Vasic, O. Milenkovic
- **PDF**: https://ieeexplore.ieee.org/document/1302295
- **Abstract**: This paper introduces several new combinatorial constructions of low-density parity-check (LDPC) codes, in contrast to the prevalent practice of using long, random-like codes. The proposed codes are well structured, and unlike random codes can lend themselves to a very low-complexity implementation. Constructions of regular Gallager codes based on cyclic difference families, cycle-invariant difference sets, and affine 1-configurations are introduced. Several constructions of difference families used for code design are presented, as well as bounds on the minimal distance of the codes based on the concept of a generalized Pasch configuration.

## Construction of low-density parity-check codes based on balanced incomplete block designs

- **Status**: ✅
- **Reason**: BIBD 기반 구조적 정규 바이너리 LDPC 신규 구성, girth≥6, QC 형태 — 코드 설계 기법(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1302303
- **Type**: journal
- **Published**: 2004
- **Authors**: B. Ammar, B. Honary, Yu Kou +2
- **PDF**: https://ieeexplore.ieee.org/document/1302303
- **Abstract**: This correspondence presents a method for constructing structured regular low-density parity-check (LDPC) codes based on a special type of combinatoric designs, known as balance incomplete block designs. Codes constructed by this method have girths at least 6 and they perform well with iterative decoding. Furthermore, several classes of these codes are quasi-cyclic and hence their encoding can be implemented with simple feedback shift registers.

## Design methods for irregular repeat-accumulate codes

- **Status**: ✅
- **Reason**: IRA 부호 앙상블의 density-evolution 기반 LP 최적화 4가지 신규 방법 제시 — 바이너리 LDPC BP 디코더 대상 코드설계 기법으로 이식 가능(E/C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1317116
- **Type**: journal
- **Published**: 2004
- **Authors**: A. Roumy, S. Guemghar, G. Caire +1
- **PDF**: https://ieeexplore.ieee.org/document/1317116
- **Abstract**: We optimize the random-like ensemble of irregular repeat-accumulate (IRA) codes for binary-input symmetric channels in the large block-length limit. Our optimization technique is based on approximating the evolution of the densities (DE) of the messages exchanged by the belief-propagation (BP) message-passing decoder by a one-dimensional dynamical system. In this way, the code ensemble optimization can be solved by linear programming. We propose four such DE approximation methods, and compare the performance of the obtained code ensembles over the binary-symmetric channel (BSC) and the binary-antipodal input additive white Gaussian noise channel (BIAWGNC). Our results clearly identify the best among the proposed methods and show that the IRA codes obtained by these methods are competitive with respect to the best known irregular low-density parity-check (LDPC) codes. In view of this and the very simple encoding structure of IRA codes, they emerge as attractive design choices.

## Near-Shannon-limit quasi-cyclic low-density parity-check codes

- **Status**: ✅
- **Reason**: Shannon 한계 근접 QC-LDPC 두 부류 구성; E 바이너리 QC-LDPC 구성 기법
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1315899
- **Type**: journal
- **Published**: 2004
- **Authors**: Lei Chen, Jun Xu, I. Djurdjevic +1
- **PDF**: https://ieeexplore.ieee.org/document/1315899
- **Abstract**: This letter presents two classes of quasi-cyclic low-density parity-check codes that perform close to the Shannon limit.

## Box and match techniques applied to soft-decision decoding

- **Status**: ✅
- **Reason**: Box-and-match soft-decision (ordered statistics) decoding improvement — OSD is explicitly listed as transferable decoder algorithm (C).
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1291728
- **Type**: journal
- **Published**: 2004
- **Authors**: A. Valembois, M. Fossorier
- **PDF**: https://ieeexplore.ieee.org/document/1291728
- **Abstract**: In this paper, we improve the ordered statistics decoding algorithm by using matching techniques. This allows us: to reduce the worst case complexity of decoding (the error performance being fixed) or to improve the error performance (for a same complexity); to reduce the ratio between average complexity and worst case complexity; to achieve practically optimal decoding of rate-1/2 codes of lengths up to 128 (rate-1/2 codes are a traditional benchmark, for coding rates different from 1/2, the decoding is easier); to achieve near-optimal decoding of a rate-1/2 code of length 192, which could never be performed before.

## Improving belief propagation on graphs with cycles

- **Status**: ✅
- **Reason**: normalized BP / offset BP — 짧은 LDPC 사이클 대응 BP 메시지 스케일링 변형, NAND LDPC 디코더에 직접 이식되는 핵심 기법(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1261926
- **Type**: journal
- **Published**: 2004
- **Authors**: M. R. Yazdani, S. Hemati, A. H. Banihashemi
- **PDF**: https://ieeexplore.ieee.org/document/1261926
- **Abstract**: In this letter, we propose two modifications to belief propagation (BP) decoding algorithm. The modifications are based on reducing the reliability of messages throughout the iteration process, and are particularly effective for short low-density parity-check codes, where the existence of cycles makes the original BP algorithm perform suboptimal. The proposed algorithms, referred to as "normalized BP" and "offset BP," reduce the absolute value of the outgoing log-likelihood ratio messages at variable nodes by using a multiplicative factor and an additive factor, respectively. Simulation results show that both algorithms perform more or less the same, and both outperform BP in error performance.

## Exact thresholds and optimal codes for the binary-symmetric channel and Gallager's decoding algorithm A

- **Status**: ✅
- **Reason**: Gallager decoding algorithm A 임계값 해석 + 최적 차수분포 — 바이너리 LDPC 코드설계/디코더 이론으로 E에 해당, 차수분포는 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1327802
- **Type**: journal
- **Published**: 2004
- **Authors**: L. Bazzi, T. J. Richardson, R. L. Urbanke
- **PDF**: https://ieeexplore.ieee.org/document/1327802
- **Abstract**: We show that for the case of the binary-symmetric channel and Gallager's decoding algorithm A the threshold can, in many cases, be determined analytically. More precisely, we show that the threshold is always upper-bounded by the minimum of (1-/spl lambda//sub 2//spl rho/'(1))/(/spl lambda/'(1)/spl rho/'(1)-/spl lambda//sub 2//spl rho/'(1)) and the smallest positive real root /spl tau/ of a specific polynomial p(x) and we observe that for most cases this bound is tight, i.e., it determines the threshold exactly. We also present optimal degree distributions for a large range of rates. In the case of rate one-half codes, for example, the threshold x/sub 0//sup */ of the optimal degree distribution is given by x/sup *//sub 0//spl sim/0.0513663. Finally, we outline how thresholds of more complicated decoders might be determined analytically.

## High-rate girth-eight low-density parity-check codes on rectangular integer lattices

- **Status**: ✅
- **Reason**: 정수격자 기반 girth-8 고율 QC-LDPC 구성(circulant 배열) — 바이너리 코드설계(E) 신규 구성, 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1327838
- **Type**: journal
- **Published**: 2004
- **Authors**: B. Vasic, K. Pedagani, M. Ivkovic
- **PDF**: https://ieeexplore.ieee.org/document/1327838
- **Abstract**: This letter introduces a combinatorial construction of girth-eight high-rate low-density parity-check codes based on integer lattices. The parity-check matrix of a code is defined as a point-line incidence matrix of a 1-configuration based on a rectangular integer lattice, and the girth-eight property is achieved by a judicious selection of sets of parallel lines included in a configuration. A class of codes with a wide range of lengths and column weights is obtained. The resulting matrix of parity checks is an array of circulant matrices.

## Run-length-limited low-density Parity check codes based on deliberate error insertion

- **Status**: ✅
- **Reason**: RLL 제약+iterative LDPC 디코딩 결합 부호화 기법, 기록/스토리지 제약 관련 바이너리 LDPC 기여로 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1298953
- **Type**: journal
- **Published**: 2004
- **Authors**: B. Vasic, K. Pedagani
- **PDF**: https://ieeexplore.ieee.org/document/1298953
- **Abstract**: We propose a novel approach to modulation and error control coding. The idea is to completely eliminate a constrained encoder and, instead, impose the constraint by the deliberate introduction of bit errors before transmission. The redundancy that would have been used for imposing the constraint is used in our scheme to strengthen the error control code (ECC), in such a way that the ECC becomes capable of correcting both deliberate errors as well as channel errors that occur during the detection. Our ECC-modulation scheme is based on iterative decoding of low-density parity check codes and a run-length constraint.

## Large girth cycle codes for partial response channels

- **Status**: ✅
- **Reason**: girth-12 cycle code 구성 + 효율적 인코딩 알고리즘 — 바이너리 LDPC 코드설계(girth/사이클) 이식 가능(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1325740
- **Type**: journal
- **Published**: 2004
- **Authors**: Hongwei Song, Jingfeng Liu, B. V. K. V. Kumar
- **PDF**: https://ieeexplore.ieee.org/document/1325740
- **Abstract**: In this paper, we present a general approach for constructing high-rate cycle codes having girth 12 which achieve the lower bound on the block length. An efficient encoding algorithm is also proposed for this class of codes. We estimate the word error rate of the cycle codes for additive white Gaussian noise (AWGN) channels under maximum likelihood decoding, using the minimum distance and its multiplicity. These estimates are compared to simulation results with iterative soft decoding. The performance of these codes for partial response channels is studied under iterative soft decoding using computer simulations.

## MacNeish-Mann theorem based iteratively decodable codes for optical communication systems

- **Status**: ✅
- **Reason**: E — MacNeish-Mann 직교라틴방진 기반 신규 LDPC 구성(girth>=6, 고부호율); 바이너리 코드 설계 기법 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1324685
- **Type**: journal
- **Published**: 2004
- **Authors**: I. B. Djordjevic, B. Vasic
- **PDF**: https://ieeexplore.ieee.org/document/1324685
- **Abstract**: A novel family of low-density parity-check codes is proposed based on MacNeish-Mann theorem for construction of mutually orthogonal Latin squares. Codes from this family have high code rate, girth at least six, large minimum distance, and significantly outperform conventional forward error correction schemes based on Reed-Solomon (RS) and turbo codes.

## Signal-to-noise ratio mismatch for low-density parity-check coded magnetic recording channels

- **Status**: ✅
- **Reason**: LDPC 자기기록 채널 SNR mismatch가 LLR 미스매치/density evolution과 직결 — NAND LLR 캘리브레이션에 이식 가능(A/C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1284453
- **Type**: journal
- **Published**: 2004
- **Authors**: W. Tan, J. R. Cruz
- **PDF**: https://ieeexplore.ieee.org/document/1284453
- **Abstract**: Signal-to-noise ratio (SNR) mismatch is found in simulations to have great influence on the performance of low-density parity-check coded magnetic recording channels. While an inappropriate SNR mismatch degrades the performance dramatically, a properly selected optimum SNR mismatch can improve it significantly. In this paper we analyze the causes of this phenomenon and find optimum SNR mismatch values for specific magnetic recording systems with physical impairments such as electronic and media noise as well as erasures, using both density evolution analysis and Monte Carlo simulations. We observed that two characteristics of the probability density function (pdf) of the channel message, namely, the Gaussianity and the variance-to-mean ratio (VMR) have a major effect on the SNR mismatch. Generally speaking, if the channel message is approximately Gaussian-distributed and the VMR is larger than two, a negative SNR mismatch substantially improves the system performance. Numerical results show that for a magnetic recording channel with additive white Gaussian noise (AWGN), the optimum SNR mismatch is about -3 to -2 dB, while for a channel with 10% AWGN and 90% media noise, is about -10 to -8 dB, whether erasures are present or not.

## High code rate low-density parity-check codes for optical communication systems

- **Status**: ✅
- **Reason**: difference system 기반 고율 바이너리 LDPC 신규 구성, girth≥6 (카테고리 E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1300678
- **Type**: journal
- **Published**: 2004
- **Authors**: I. B. Djordjevic, B. Vasic
- **PDF**: https://ieeexplore.ieee.org/document/1300678
- **Abstract**: A novel family of low-density parity-check codes based on symmetrically repeated difference systems is proposed. Codes from this family have very high code rate, girth at least six, large minimum distance, and significantly outperform conventional Reed-Solomon codes.

## A trellis-based method for removing cycles from bipartite graphs and construction of low density parity check codes

- **Status**: ✅
- **Reason**: 이분그래프 단주기 제거 trellis 기반 방법으로 LDPC 성능개선·신규 구성; E 사이클 제거/코드설계
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1315671
- **Type**: journal
- **Published**: 2004
- **Authors**: L. Lan, Y. Y. Tai, L. Chen +2
- **PDF**: https://ieeexplore.ieee.org/document/1315671
- **Abstract**: This letter presents a trellis-based iterative method for removing short cycles from bipartite graphs. This method can be used to improve the performance of low density parity check (LDPC) codes or to construct new LDPC codes.

## Area efficient decoding of quasi-cyclic low density parity check codes

- **Status**: ✅
- **Reason**: QC-LDPC BP의 CN/VN 기능 유닛 통합으로 면적 21% 절감 — 디지털 디코더 HW 아키텍처(D) 이식 가능
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:1327044
- **Type**: conference
- **Published**: 2004
- **Authors**: Zhongfeng Wang, Yanni Chen, K. K. Parhi
- **PDF**: https://ieeexplore.ieee.org/document/1327044
- **Abstract**: This paper exploits the similarity between the two stages of belief propagation decoding algorithm for low density parity check codes to derive an area efficient design that re-maps the check node functional units and variable node functional units into the same hardware. Consequently, the novel approach could reduce the logic core size by approximately 21% without any performance degradation. In addition, the proposed approach improves the hardware utilization efficiency as well.

## Synthesizing interconnect-efficient low density parity check codes

- **Status**: ✅
- **Reason**: interconnect-efficient LDPC 부호 합성 — 라우팅/배선 효율 고려한 HW 친화적 코드설계, NAND 디코더 HW 이식 가능(D/E). 초록 없어 제목 근거로 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1322530
- **Type**: conference
- **Published**: 2004
- **Authors**: M. Mohiyuddin, A. Prakash, A. Aziz +1
- **PDF**: https://ieeexplore.ieee.org/document/1322530
- **Abstract**: N/A

## A new look at the generalized distributive law

- **Status**: ✅
- **Reason**: GDL/junction tree 일반화로 marginalization 저복잡도 알고리즘 — BP가 GDL의 특수형이므로 메시지패싱 복잡도 절감 기법이 바이너리 LDPC BP에 이식 가능(C). 애매하나 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1302294
- **Type**: journal
- **Published**: 2004
- **Authors**: P. Pakzad, V. Anantharam
- **PDF**: https://ieeexplore.ieee.org/document/1302294
- **Abstract**: In this paper, we develop a measure-theoretic version of the junction tree algorithm to compute desired marginals of a product function. We reformulate the problem in a measure-theoretic framework, where the desired marginals are viewed as corresponding conditional expectations of a product of random variables. We generalize the notions of independence and junction trees to collections of /spl sigma/-fields on a space with a signed measure. We provide an algorithm to find such a junction tree when one exists. We also give a general procedure to augment the /spl sigma/-fields to create independencies, which we call "lifting." This procedure is the counterpart of the moralization and triangulation procedure in the conventional generalized distributive law (GDL) framework, in order to guarantee the existence of a junction tree. Our procedure includes the conventional GDL procedure as a special case. However, it can take advantage of structures at the atomic level of the sample space to produce junction tree-based algorithms for computing the desired marginals that are less complex than those GDL can discover, as we argue through examples. Our formalism gives a new way by which one can hope to find low-complexity algorithms for marginalization problems.
