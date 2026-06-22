# IEEE Xplore — 2006-03 (1차선별 통과)


## A 640-Mb/s 2048-bit programmable LDPC decoder chip

- **Status**: ✅
- **Reason**: D: 2048-bit 프로그래머블 LDPC 디코더 칩, TDMP+LUT-free 메시지연산+programmable network — NAND 디코더 HW 이식 가능
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:1599537
- **Type**: journal
- **Published**: March 2006
- **Authors**: M.M. Mansour, N.R. Shanbhag
- **PDF**: https://ieeexplore.ieee.org/document/1599537
- **Abstract**: A 14.3-mm/sup 2/ code-programmable and code-rate tunable decoder chip for 2048-bit low-density parity-check (LDPC) codes is presented. The chip implements the turbo-decoding message-passing (TDMP) algorithm for architecture-aware (AA-)LDPC codes which has a faster convergence rate and hence a throughput advantage over the standard decoding algorithm. It employs a reduced complexity message computation mechanism free of lookup tables, and features a programmable network for message interleaving based on the code structure. The chip decodes any mix of 2048-bit rate-1/2 (3,6)-regular AA-LDPC codes in standard mode by programming the network, and attains a throughput of 640 Mb/s at 125 MHz for 10 TDMP-decoding iterations. In augmented mode, the code rate can be tuned up to 14/16 in steps of 1/16 by augmenting the code. The chip is fabricated in 0.18-/spl mu/m six-metal-layer CMOS technology, operates at a peak clock frequency of 125 MHz at 1.8 V (nominal), and dissipates an average power of 787 mW.

## Two-dimensional correction for min-sum decoding of irregular LDPC codes

- **Status**: ✅
- **Reason**: 2D correction min-sum 디코더 변형(정규화/오프셋)+낮은 error floor — 카테고리 C 이식 가능 디코더 알고리즘
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1603377
- **Type**: journal
- **Published**: March 2006
- **Authors**: J. Zhang, M. Fossorier, D. Gu +1
- **PDF**: https://ieeexplore.ieee.org/document/1603377
- **Abstract**: Two-dimensional (2-D) correction schemes are proposed to improve the performance of conventional min-sum (MS) decoding of irregular low density parity check codes. An iterative procedure based on parallel differential optimization is presented to obtain the optimal 2-D factors. Both density evolution analysis and simulation show that the proposed method provides a comparable performance as belief propagation (BP) decoding while requiring less complexity. Interestingly, the new method exhibits a lower error floor than that of BP decoding. With respect to conventional MS and 1-D normalized MS decodings, the 2-D normalized MS offers a better performance. The 2-D offset MS decoding exhibits a similar behavior.

## Disclosing the LDPC code decoder design space

- **Status**: ✅
- **Reason**: LDPC 디코더 설계공간(파라미터 trade-off) 분석, HW 아키텍처 통찰(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:1656876
- **Type**: conference
- **Published**: 6-10 March
- **Authors**: T. Brack, F. Kienle, N. Wehn
- **PDF**: https://ieeexplore.ieee.org/document/1656876
- **Abstract**: The design of future communication systems with high throughput demands will become a critical task, especially when sophisticated channel coding schemes have to be applied. LDPC codes are one of the most promising candidates because of their outstanding communications performance. One major problem for a decoder hardware realization is the huge design space composed of many interrelated parameters which enforces drastic design trade-offs. Another important issue is the need for flexibility of such systems. In this paper we illuminate this design space with special emphasis on the strong interrelations of theses parameters. Three design studies are presented to highlight the effects on a generic architecture if some parameters are constraint by a given standard, given technology, and given area constraints

## Low cost LDPC decoder for DVB-S2

- **Status**: ✅
- **Reason**: DVB-S2 저비용 LDPC 디코더, sub-block 병렬화 HW 기법(D) 이식 가능
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:1657127
- **Type**: conference
- **Published**: 6-10 March
- **Authors**: J. Dielissen, A. Hekstra, V. Berg
- **PDF**: https://ieeexplore.ieee.org/document/1657127
- **Abstract**: Because of its excellent bit-error-rate performance, the Low-Density Parity-Check (LDPC) algorithm is gaining increased attention in communication standards and literature. The new Digital Video Broadcast via Satellite stan dard (DVB-S2) is the first broadcast standard to include a LDPC-code, and the first implementations are available. In our investigation of generic LDPC-implementations we found that scalable sub-block parallelism enables efficient implementations for a wide range of applications. For the DVB-S2 case, using sub-block parallelism we obtain half the chip-size of known solutions. For the required performance in the normative configurations for the broadcast service (90 Mbps), the area is even 3 compared to the smallest published decoder.

## Interconnection framework for high-throughput, flexible LDPC decoders

- **Status**: ✅
- **Reason**: 고처리율 유연 LDPC 디코더 상호연결 구조(D), 병렬/반병렬 통신복잡도 감소
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:1657126
- **Type**: conference
- **Published**: 6-10 March
- **Authors**: F. Quaglio, F. Vacca, C. Castellano +2
- **PDF**: https://ieeexplore.ieee.org/document/1657126
- **Abstract**: This paper presents a possible interconnection structure suitable for being used in a flexible LDPC decoder. The main feature of the proposed approach is the possibility of implementing parallel or semi-parallel decoders with a reduced communication complexity. To the best of our knowledge this is the first work detailing the implementation of a fully flexible LDPC decoder, able to support any type of code. To prove the effectiveness of this approach, a complete decoder has been implemented on a XC2V8000, achieving a decoding throughput of 529 Mbps on a (1920, 640) code.

## Analysis and Design of Moderate Length Regular LDPC Codes with Low Error Floors

- **Status**: ✅
- **Reason**: E: regular LDPC error floor 저감, trapping set 지배 오류이벤트 탐색·낮은 error floor 부호 설계 — NAND에 직접 이식
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4067922
- **Type**: conference
- **Published**: 22-24 Marc
- **Authors**: Chad A. Cole, Stephen G. Wilson, Eric. K. Hall +1
- **PDF**: https://ieeexplore.ieee.org/document/4067922
- **Abstract**: The traditional method to estimate code performance in the higher SNR region is to use a sum of the contributions of the most dominant error events to the probability of error. If an ML decoder is used, these events will be minimum distance codewords; the traditional decoder used in LDPC codes, some variant of the message passing algorithm, will introduce non-codeword error events known as trapping sets. For long LDPC codes it is difficult to enumerate all of these dominant error events. A procedure to efficiently find dominant error events by using the regular low-density structure of an LDPC code is presented here. The search method can be adapted to work with LDPC codes of various regular and irregular degree distributions, but is especially suited to a very practical subset of LDPC known as regular {3, 6} codes of moderate block length. We also show how codes with very low error floors can be created by utilizing this search method.

## High-Throughput Turbo-Sum-Product Decoding of QC LDPC Codes

- **Status**: ✅
- **Reason**: C: QC-LDPC용 turbo-sum-product/shuffled-SP 디코딩, 빠른 수렴·적은 메모리 — 부호 비의존 디코더 개선, NAND 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4067925
- **Type**: conference
- **Published**: 22-24 Marc
- **Authors**: Yongmei Dai, Zhiyuan Yan, Ning Chen
- **PDF**: https://ieeexplore.ieee.org/document/4067925
- **Abstract**: In this paper, we first propose a turbo-sum-product (TSP) decoding algorithm for quasi-cyclic (QC) low-density parity-check (LDPC) codes and show that our proposed algorithm not only achieves faster convergence and better error performances than the sum-product (SP) algorithm, but also needs less memory in implementation. Compared with the turbo decoding algorithm, our TSP algorithm saves the same amount of memory and achieves a better tradeoff between sub-iterations and convergence rate, leading to a higher throughput. We also propose a shuffled-sum-product (SSP) decoding algorithm, which is the dual of the TSP algorithm.

## A Wiring-Efficient, High-Throughput Low Density Parity Check Decoder Design

- **Status**: ✅
- **Reason**: D: 배선효율 고처리량 LDPC 디코더 HW 설계, unwrapping으로 size-throughput 트레이드오프 — NAND 디코더에 이식 가능
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:4067921
- **Type**: conference
- **Published**: 22-24 Marc
- **Authors**: Radivoje Zarubica, Stephen G. Wilson
- **PDF**: https://ieeexplore.ieee.org/document/4067921
- **Abstract**: A high-throughput 1020-bit rate-1/2 low density parity check (LDPC) decoder design is proposed that matches the coding gain of current LDPC decoders. The decoder features wiring-efficient code design and an unwrapping technique that allows us to trade between size and the throughput of a decoder.

## Construction of Quasi-Cyclic LDPC Codes Based on the Primitive Elements of Finite Fields

- **Status**: ✅
- **Reason**: E: 유한체 원시원소 기반 QC-LDPC 대수적 구성, 효율 인코딩 가능 — 새 코드설계로 NAND 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4067924
- **Type**: conference
- **Published**: 22-24 Marc
- **Authors**: Shumei Song, Lan Lan, Shu Lin +1
- **PDF**: https://ieeexplore.ieee.org/document/4067924
- **Abstract**: This paper presents an algebraic method for constructing quasi-cyclic LDPC codes based on the primitive elements of finite fields. The construction gives a class of efficiently encodable quasi-cyclic LDPC codes. Experimental results show that the constructed codes decoded with iterative decoding using the sum-product algorithm perform well over the AWGN channel.

## A New Fast Density Evolution Method for LDPC Codes Using Higher Order Statistics

- **Status**: ✅
- **Reason**: C/E: 고차 통계 모멘트 매칭 기반 density evolution 신규 기법, 비가우시안 LLR 분포 정확 추정 — LDPC 설계 분석에 이식
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4067926
- **Type**: conference
- **Published**: 22-24 Marc
- **Authors**: Soroush Akhlaghi, Amir K. Khandani, Abolfazl Falahati
- **PDF**: https://ieeexplore.ieee.org/document/4067926
- **Abstract**: Density evolution (DE) is a technique for tracking the distribution of the log likelihood ratio (LLR) messages exchanged between the variable nodes and the check nodes in a bipartite graph. It is widely assumed that these distributions are close to Gaussian. However, in many scenarios, this assumption is not valid, e.g., the case that the signal to noise ratio (SNR) is low, or the degree of variable nodes exceeds a certain threshold. This article introduces a new (suboptimal) method for DE algorithm in low-density parity-check (LDPC) codes. We provide a more accurate model for the distribution of message bits (as compared to Gaussian) through matching the first n statistical moments. An iterative message passing algorithm is proposed to compute these moments from the graphical representation of the underlying code. We show that the proposed algorithm results in an improved estimate of the underlying EXIT chart as compared to using a Gaussian assumption. In this respect, the proposed method achieves a performance very close to that of the best earlier methods, while it offers a much lower complexity.

## A New Fast Density Evolution

- **Status**: ✅
- **Reason**: LDPC density evolution 고효율 구현 — 코드설계 도구(E)로 유한길이/구성 설계에 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1633807
- **Type**: conference
- **Published**: 13-17 Marc
- **Authors**: Hui Jin, T. Richardson
- **PDF**: https://ieeexplore.ieee.org/document/1633807
- **Abstract**: Density evolution for LDPC codes predicts asymptotic performance and serves as a practical design tool for designing top performing structures [1]. Many papers advocate the use of exit chart methods and other approximations, proclaiming that density evolution is computationally too intensive. In this paper we show that this is not the case: we present a highly efficient and accurate implementation of density evolution for LDPC codes.

## Bounds on the Threshold of Linear Programming Decoding

- **Status**: ✅
- **Reason**: LP 디코딩 threshold bound — LP 디코더는 이식 가능 디코더 알고리즘(C) 범주, Phase 3 재검토
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1633805
- **Type**: conference
- **Published**: 13-17 Marc
- **Authors**: P.O. Vontobel, R. Koetter
- **PDF**: https://ieeexplore.ieee.org/document/1633805
- **Abstract**: Whereas many results are known about thresholds for ensembles of low-density parity-check codes under message-passing iterative decoding, this is not the case for linear programming decoding. Towards closing this knowledge gap, this paper presents some bounds on the thresholds of low-density parity-check code ensembles under linear programming decoding.
