# IEEE Xplore — 2005-03 (1차선별 통과)


## A decoding algorithm for finite-geometry LDPC codes

- **Status**: ✅
- **Reason**: FG-LDPC용 신규 저복잡도 비트플리핑류 디코더(실패체크수+신뢰도 기반)로 바이너리 LDPC에 이식 가능한 디코더 알고리즘(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1413585
- **Type**: journal
- **Published**: March 2005
- **Authors**: Zhenyu Liu, D.A. Pados
- **PDF**: https://ieeexplore.ieee.org/document/1413585
- **Abstract**: In this paper, we develop a new low-complexity algorithm to decode low-density parity-check (LDPC) codes. The developments are oriented specifically toward low-cost, yet effective, decoding of (high-rate) finite-geometry (FG) LDPC codes. The decoding procedure updates iteratively the hard-decision received vector in search of a valid codeword in the vector space. Only one bit is changed in each iteration, and the bit-selection criterion combines the number of failed checks and the reliability of the received bits. Prior knowledge of the signal amplitude and noise power is not required. An optional mechanism to avoid infinite loops in the search is also proposed. Our studies show that the algorithm achieves an appealing tradeoff between performance and complexity for FG-LDPC codes.

## Stopping set distribution of LDPC code ensembles

- **Status**: ✅
- **Reason**: LDPC stopping set 분포·최소 stopping set 크기를 degree distribution과 연결, error floor·코드설계(E)에 연결되는 분석
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1397932
- **Type**: journal
- **Published**: March 2005
- **Authors**: A. Orlitsky, K. Viswanathan, Junan Zhang
- **PDF**: https://ieeexplore.ieee.org/document/1397932
- **Abstract**: Stopping sets determine the performance of low-density parity-check (LDPC) codes under iterative decoding over erasure channels. We derive several results on the asymptotic behavior of stopping sets in Tanner-graph ensembles, including the following. An expression for the normalized average stopping set distribution, yielding, in particular, a critical fraction of the block length above which codes have exponentially many stopping sets of that size. A relation between the degree distribution and the likely size of the smallest nonempty stopping set, showing that for a /spl radic/1-/spl lambda/'(0)/spl rho/'(1) fraction of codes with /spl lambda/'(0)/spl rho/'(1)<1, and in particular for almost all codes with smallest variable degree >2, the smallest nonempty stopping set is linear in the block length. Bounds on the average block error probability as a function of the erasure probability /spl epsi/, showing in particular that for codes with lowest variable degree 2, if /spl epsi/ is below a certain threshold, the asymptotic average block error probability is 1-/spl radic/1-/spl lambda/'(0)/spl rho/'(1)/spl epsi/.

## Simple reconfigurable low-density parity-check codes

- **Status**: ✅
- **Reason**: 저복잡도 인코딩/디코딩 reconfigurable GeIRA 바이너리 LDPC 코드 구성(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1411025
- **Type**: journal
- **Published**: March 2005
- **Authors**: G. Liva, E. Paolini, M. Chiani
- **PDF**: https://ieeexplore.ieee.org/document/1411025
- **Abstract**: Low-density parity-check codes (LDPCC) have been recently investigated as a possible solution for high data rate applications, for both space and terrestrial wireless communications. A main issue is the research of low complexity encoding and decoding schemes. In this letter we present a class of reconfigurable LDPCC characterized by low encoding and decoding complexity: we call them generalized irregular repeat-accumulate (GeIRA) codes.

## Using linear programming to Decode Binary linear codes

- **Status**: ✅
- **Reason**: 바이너리 LDPC LP 디코딩 신규 디코더·pseudocodeword 특성화, BP에 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1397933
- **Type**: journal
- **Published**: March 2005
- **Authors**: J. Feldman, M.J. Wainwright, D.R. Karger
- **PDF**: https://ieeexplore.ieee.org/document/1397933
- **Abstract**: A new method is given for performing approximate maximum-likelihood (ML) decoding of an arbitrary binary linear code based on observations received from any discrete memoryless symmetric channel. The decoding algorithm is based on a linear programming (LP) relaxation that is defined by a factor graph or parity-check representation of the code. The resulting "LP decoder" generalizes our previous work on turbo-like codes. A precise combinatorial characterization of when the LP decoder succeeds is provided, based on pseudocodewords associated with the factor graph. Our definition of a pseudocodeword unifies other such notions known for iterative algorithms, including "stopping sets," "irreducible closed walks," "trellis cycles," "deviation sets," and "graph covers." The fractional distance d/sub frac/ of a code is introduced, which is a lower bound on the classical distance. It is shown that the efficient LP decoder will correct up to /spl lceil/d/sub frac//2/spl rceil/-1 errors and that there are codes with d/sub frac/=/spl Omega/(n/sup 1-/spl epsi//). An efficient algorithm to compute the fractional distance is presented. Experimental evidence shows a similar performance on low-density parity-check (LDPC) codes between LP decoding and the min-sum and sum-product algorithms. Methods for tightening the LP relaxation to improve performance are also provided.

## A simple convergence comparison of Gallager codes under two message-passing schedules

- **Status**: ✅
- **Reason**: flooding vs turbo 메시지패싱 스케줄 수렴 비교, 바이너리 LDPC BP에 이식 가능한 디코더 스케줄 기법(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1411022
- **Type**: journal
- **Published**: March 2005
- **Authors**: Sheng Tong, Xinmei Wang
- **PDF**: https://ieeexplore.ieee.org/document/1411022
- **Abstract**: The convergence rate of iterative decoding of Gallager codes on the additive white Gaussian noise (AWGN) channel using the sum-product algorithm (SPA) under the flooding schedule (FS) is compared with that under the turbo-decoding schedule (TDS). Analyses using extrinsic information transfer (EXIT) charts show that TDS exhibits a much faster convergence behavior than FS.

## A synthesizable IP core for DVB-S2 LDPC code decoding

- **Status**: ✅
- **Reason**: DVB-S2 LDPC 디코더 synthesizable IP core, 처리량/메모리 HW 아키텍처 — D 이식 가능
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:1395802
- **Type**: conference
- **Published**: 7-11 March
- **Authors**: F. Kienle, T. Brack, N. Wehn
- **PDF**: https://ieeexplore.ieee.org/document/1395802
- **Abstract**: The new standard for digital video broadcast DVB-S2 features low-density parity-check (LDPC) codes as their channel coding scheme. The codes are defined for various code rates with a block size of 64800 which allows a transmission close to the theoretical limits. The decoding of LDPC is an iterative process. For DVB-S2 about 300000 messages are processed and reordered in each of the 30 iterations. These huge data processing and storage requirements are a real challenge for the decoder hardware realization, which has to fulfill the specified throughput of 255 Mbit/s for base station applications. In this paper we show, to the best of our knowledge, the first published IP LDPC decoder core for the DVB-S2 standard. We present a synthesizable IP block based on ST Microelectronics 0.13 /spl mu/m CMOS technology.

## Net coding gain of 10.2 dB using an irregular LDPC code with a three-dimensional analyser [optical communication applications]

- **Status**: ✅
- **Reason**: irregular LDPC용 3차원 디코딩 스킴 제안으로 신규 디코더 기법(C), 반복디코딩 개선
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1501582
- **Type**: conference
- **Published**: 6-11 March
- **Authors**: S. Schollmann, O. Jean, W. Rosenkranz
- **PDF**: https://ieeexplore.ieee.org/document/1501582
- **Abstract**: We present a three-dimensional decoding scheme for an irregular low density parity check code (LDPC). With this setup, we achieved a net coding gain of 10.2 dB and a significant improvement in the iterating decoding process.

## Towards practical minimum-entropy universal decoding

- **Status**: ✅
- **Reason**: LP 완화 기반 디코딩, 바이너리 선형부호 LP decoding 구성 명시 — 부호 비의존 디코더 기법(C) 이식 가능, 애매하여 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1402164
- **Type**: conference
- **Published**: 29-31 Marc
- **Authors**: T.P. Coleman, M. Medard, M. Effros
- **PDF**: https://ieeexplore.ieee.org/document/1402164
- **Abstract**: Minimum-entropy decoding is a universal decoding algorithm used in decoding block compression of discrete memoryless sources as well as block transmission of information across discrete memoryless channels. Extensions can also be applied for multiterminal decoding problems, such as the Slepian-Wolf source coding problem. The 'method of types' has been used to show that there exist linear codes for which minimum-entropy decoders achieve the same error exponent as maximum-likelihood decoders. Since minimum-entropy decoding is NP-hard in general, minimum-entropy decoders have existed primarily in the theory literature. We introduce practical approximation algorithms for minimum-entropy decoding. Our approach, which relies on ideas from linear programming, exploits two key observations. First, the 'method of types' shows that that the number of distinct types grows polynomially in n. Second, recent results in the optimization literature have illustrated polytope projection algorithms with complexity that is a function of the number of vertices of the projected polytope. Combining these two ideas, we leverage recent results on linear programming relaxations for error correcting codes to construct polynomial complexity algorithms for this setting. In the binary case, we explicitly demonstrate linear code constructions that admit provably good performance.

## Equation based LDPC decoder for intersymbol interference channels

- **Status**: ✅
- **Reason**: C/D: signed sum-product(SSP), equation-based LDPC 디코더로 메모리 대폭 절감 아키텍처 — 디코더/HW 기법 이식 가능(ISI 결합이나 LDPC측 신규)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1416414
- **Type**: conference
- **Published**: 23-23 Marc
- **Authors**: Zining Wu, G. Burd
- **PDF**: https://ieeexplore.ieee.org/document/1416414
- **Abstract**: The application of LDPC codes to intersymbol interference (ISI) channels requires efficient soft decoding methods for the ISI channel as well as the outer LDPC code. We introduce a fully pipelined turbo equalization architecture that combines soft decoders for the channel and the LDPC code. This equation based LDPC decoder uses a signed sum product (SSP) decoding algorithm, and stores soft information for each equation, in contrast to each edge in conventional LDPC decoders. The memory size of the LDPC decoder is greatly reduced, and the delay of the LDPC decoder is absorbed by the delay of the soft channel detector.

## Error floor investigation and girth optimization for certain types of low-density parity check codes

- **Status**: ✅
- **Reason**: E: LDPC error floor 조사 + array code girth 최적화 기법, FPGA 평가 — 사이클/girth 코드설계 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1415906
- **Type**: conference
- **Published**: 23-23 Marc
- **Authors**: Lingyan Sun, Hongwei Song, B.V.K.V. Kumar
- **PDF**: https://ieeexplore.ieee.org/document/1415906
- **Abstract**: Low-density parity check (LDPC) codes with their near-Shannon capacity limit error correcting performance and iterative decoding algorithm are being evaluated for digital communications applications. For LDPC codes to be used in real systems, their error floors need to be investigated. In this paper, we evaluate the performance of disjoint difference set (DDS)-based LDPC codes (with column weights 3, 4, 5) and array code-based LDPC codes (with column weights 3, 4, 5) in the additive white Gaussian noise (AWGN) channel using a high-speed field programmable gate array (FPGA) simulation platform. The error floor regions (bit error rates down to 10/sup -12/) of those codes are presented. For better performance of array codes, a girth optimization method is proposed and the FPGA evaluation results are presented.

## FPGA based implementation of decoder for array low-density parity-check codes

- **Status**: ✅
- **Reason**: D: 바이너리 array LDPC 디코더 FPGA 구현 아키텍처 — HW 이식 가능
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:1416232
- **Type**: conference
- **Published**: 23-23 Marc
- **Authors**: P. Bhagawat, M. Uppal, G. Choi
- **PDF**: https://ieeexplore.ieee.org/document/1416232
- **Abstract**: Low density parity check (LDPC) codes have received much attention for their excellent performance, and the inherent parallelism involved in decoding them. We consider a type of structured binary LDPC codes, known as array LDPC codes, which have low encoding complexity and good performance, for implementation on a Xilinx field programmable gate array (FPGA) device.

## A memory efficient serial LDPC decoder architecture

- **Status**: ✅
- **Reason**: C/D: min-constraint SPA 변형으로 extrinsic 메시지 메모리 68% 절감 시리얼 디코더 아키텍처 — 디코더+HW 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1416235
- **Type**: conference
- **Published**: 23-23 Marc
- **Authors**: A. Prabhakar, K. Narayanan
- **PDF**: https://ieeexplore.ieee.org/document/1416235
- **Abstract**: We present a memory efficient serial low density parity check (LDPC) decoder that implements a modified sum product algorithm (SPA). The modification is similar to the approximate min constraint presented by C. Jones et al. (see IEEE Conf. Military Commun., MILCOM 2003, p.157-162, 2003) but differs in hardware implementation to suit a serial architecture. Our main contribution is the proposed architecture that exploits the min constraint to reduce the storage of extrinsic messages which forms the bulk of the hardware. The least reliable bit to check input along with the check sum are the only quantities stored in the decoder. Extrinsic message memory reduction increases with the rate of the code and up to 68% saving is achieved for a rate 9/10 code. Simulation results show that the proposed changes do not degrade the bit error rate performance.

## An algorithm for the estimation of the minimum distance of LDPC codes

- **Status**: ✅
- **Reason**: LDPC 최소거리 추정용 error-impulse 기법 신규 확장, 코드설계/평가 도구로 이식 가능(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1424653
- **Type**: conference
- **Published**: 13-17 Marc
- **Authors**: F. Danesharan, M. Laddoinada, M. Mondin
- **PDF**: https://ieeexplore.ieee.org/document/1424653
- **Abstract**: The evaluation of the minimum distance of low-density parity-check (LDPC) codes remains an open problem due to the rather large dimension of the parity check matrix H associated with any practical code. In this article, we propose an effective modification of the error impulse (EI) technique for estimation of the minimum distance of the LDPCs. The EI method is successfully applied to suboptimum decoding algorithms such as the iterative MAP decoding algorithm for turbo codes. We present novel modifications and extensions of this method to the suboptimum iterative sum-product algorithm for LDPCs. Simulation results validate the functionality of the proposed technique. Simulations focus on a particular class of LDPC codes, but our approach is general and applies to any LDPC code.

## Quasi-cyclic codes from extended difference families

- **Status**: ✅
- **Reason**: EDF 기반 QC-LDPC 신규 코드설계(가변 코드사이즈, 고율)로 카테고리 E 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1424651
- **Type**: conference
- **Published**: 13-17 Marc
- **Authors**: Tao Xia, Bo Xia
- **PDF**: https://ieeexplore.ieee.org/document/1424651
- **Abstract**: Quasi-cyclic codes are renowned for their structural design and low-complexity shift register encoding. However, existing design techniques based on difference families have limited code size options due to algebraic constraints. We introduce in this paper a notation of extended difference family (EDF) and provide a systematic code design based on EDFs with a high degree of flexibility in code size. Short/medium-length codes of high rate (/spl ges/ 0.9) can be easily constructed.
