# IEEE Xplore — 2021-07 (1차선별 통과)


## A Miniaturized LDPC Encoder: Two-Layer Architecture for CCSDS Near-Earth Standard

- **Status**: ✅
- **Reason**: QC-LDPC 인코더 저자원 2층 아키텍처+공통부분식 추출 — 이식 가능 HW 인코더 설계(D), 애매하므로 살림
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:9336038
- **Type**: journal
- **Published**: July 2021
- **Authors**: Jiaming Liu, Quanyuan Feng
- **PDF**: https://ieeexplore.ieee.org/document/9336038
- **Abstract**: Quasi-cyclic low-density parity-check (QC-LDPC) codes, which have been adopted by the Consultative Committee for Space Data Systems (CCSDS), are widely used in Deep-Space (AR4JA) and Near-Earth (C2) communications. A large number of encoder architectures with CCSDS recommended standard have been proposed. But the existing architectures are not efficient enough in high-throughput implementations, many architectures have a lot of logical resources and registers. In this brief, we introduce a novel architecture with low resource utilization. A grouping algorithm is used to extract the common subexpressions (CS) of the encoding algorithm. Similar circuit structures are integrated through a two-layer architecture, which further reduces logical resources. For the special size of the generator's matrix, we introduce a preprocessing method. In addition, configuration registers are used to replace the control unit. Implemented and verified on FPGA, the proposed architecture achieves a throughput of 4.69 Gbps using only 1658 LUTs and 1038 FFs. Compared with the previous architectures, this architecture achieves lower resource utilization and multi-Gbps throughput.

## Learning to Decode Protograph LDPC Codes

- **Status**: ✅
- **Reason**: 프로토그래프 LDPC용 신경망 min-sum 디코더 - 이식 가능한 디코더 알고리즘(C), 바이너리 LDPC, MS 변형 새 기여
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9427170
- **Type**: journal
- **Published**: July 2021
- **Authors**: Jincheng Dai, Kailin Tan, Zhongwei Si +4
- **PDF**: https://ieeexplore.ieee.org/document/9427170
- **Abstract**: The recent development of deep learning methods provides a new approach to optimize the belief propagation (BP) decoding of linear codes. However, the limitation of existing works is that the scale of neural networks increases rapidly with the codelength, thus they can only support short to moderate codelengths. From the point view of practicality, we propose a high-performance neural min-sum (MS) decoding method that makes full use of the lifting structure of protograph low-density parity-check (LDPC) codes. By this means, the size of the parameter array of each layer in the neural decoder only equals the number of edge-types for arbitrary codelengths. In particular, for protograph LDPC codes, the proposed neural MS decoder is constructed in a special way such that identical parameters are shared by a bundle of edges derived from the same edge-type. To reduce the complexity and overcome the vanishing gradient problem in training the proposed neural MS decoder, an iteration-by-iteration (i.e., layer-by-layer in neural networks) greedy training method is proposed. With this, the proposed neural MS decoder tends to be optimized with faster convergence, which is aligned with the early termination mechanism widely used in practice. To further enhance the generalization ability of the proposed neural MS decoder, a codelength/rate compatible training method is proposed, which randomly selects samples from a set of codes lifted from the same base code. As a theoretical performance evaluation tool, a trajectory-based extrinsic information transfer (T-EXIT) chart is developed for various decoders. Both T-EXIT and simulation results show that the optimized MS decoding can provide faster convergence and up to 1dB gain compared with the plain MS decoding and its variants with only slightly increased complexity. In addition, it can even outperform the sum-product algorithm for some short codes.

## On Doped SC-LDPC Codes for Streaming

- **Status**: ✅
- **Reason**: SC-LDPC doping 스케일링 법칙·error rate 예측 — SC-LDPC 코드설계(E), 바이너리(BEC), 애매하므로 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9389745
- **Type**: journal
- **Published**: July 2021
- **Authors**: Roman Sokolovskii, Alexandre Graell i Amat, Fredrik Brännström
- **PDF**: https://ieeexplore.ieee.org/document/9389745
- **Abstract**: In streaming applications, doping improves the performance of spatially-coupled low-density parity-check (SC-LDPC) codes by creating reduced-degree check nodes in the coupled chain. We formulate a scaling law to predict the bit and block error rate of periodically-doped semi-infinite SC-LDPC code ensembles streamed over the binary erasure channel under sliding window decoding for a given finite component block length. The scaling law assumes that with some probability doping is equivalent to full termination and triggers two decoding waves; otherwise, decoding performs as if the coupled chain had not been doped at all. We approximate that probability and use the derived scaling laws to predict the error rates of SC-LDPC code ensembles in the presence of doping. The proposed scaling law provides accurate error rate predictions. We further use it to show that in streaming applications periodic doping can yield higher rates than periodic full termination for the same error-correcting performance.

## Fast Column Message-Passing Decoding of Low-Density Parity-Check Codes

- **Status**: ✅
- **Reason**: FCMP 고속 열 메시지패싱 스케줄+VLSI 디코더 아키텍처(40nm, 8.4Gbps) — 이식 가능 디코더/HW(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9314911
- **Type**: journal
- **Published**: July 2021
- **Authors**: Saleh Usman, Mohammad M. Mansour
- **PDF**: https://ieeexplore.ieee.org/document/9314911
- **Abstract**: A new fast column message-passing (FCMP) schedule for decoding LDPC codes is presented and investigated in this brief. FCMP converges in half the number of iterations compared to existing serial decoding schedules, has a significantly lower computational complexity than residual-belief-propagation (RBP)-based schedules, and consumes less power compared to state-of-the-art schedules. An FCMP decoder architecture supporting IEEE 802.11ad (WiGig) LDPC codes is presented. The architecture is synthesized using the TSMC 40 nm CMOS technology node and operates at a clock frequency of 200 MHz. The decoder achieves a throughput of 8.4 Gbps while consuming 72 mW of power. This results in an energy efficiency of 8.6 pJ/bit, which is the best-reported energy-efficiency in the literature for a WiGig LDPC decoder.

## Pruning and Quantizing Neural Belief Propagation Decoders

- **Status**: ✅
- **Reason**: 신경망 BP 디코더 가지치기+양자화(PB-NBP/PB-NOMS), 5비트 양자화·오프셋 최적화 — 바이너리 LDPC에 직접 이식 가능한 디코더 기법(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9281328
- **Type**: journal
- **Published**: July 2021
- **Authors**: Andreas Buchberger, Christian Häger, Henry D. Pfister +2
- **PDF**: https://ieeexplore.ieee.org/document/9281328
- **Abstract**: We consider near maximum-likelihood (ML) decoding of short linear block codes. In particular, we propose a novel decoding approach based on neural belief propagation (NBP) decoding recently introduced by Nachmani et al. in which we allow a different parity-check matrix in each iteration of the algorithm. The key idea is to consider NBP decoding over an overcomplete parity-check matrix and use the weights of NBP as a measure of the importance of the check nodes (CNs) to decoding. The unimportant CNs are then pruned. In contrast to NBP, which performs decoding on a given fixed parity-check matrix, the proposed pruning-based neural belief propagation (PB-NBP) typically results in a different parity-check matrix in each iteration. For a given complexity in terms of CN evaluations, we show that PB-NBP yields significant performance improvements with respect to NBP. We apply the proposed decoder to the decoding of a Reed-Muller code, a short low-density parity-check (LDPC) code, and a polar code. PB-NBP outperforms NBP decoding over an overcomplete parity-check matrix by 0.27–0.31 dB while reducing the number of required CN evaluations by up to 97%. For the LDPC code, PB-NBP outperforms conventional belief propagation with the same number of CN evaluations by 0.52 dB. We further extend the pruning concept to offset min-sum decoding and introduce a pruning-based neural offset min-sum (PB-NOMS) decoder, for which we jointly optimize the offsets and the quantization of the messages and offsets. We demonstrate performance 0.5 dB from ML decoding with 5-bit quantization for the Reed-Muller code.

## Counter Random Gradient Descent Bit-Flipping Decoder for LDPC Codes

- **Status**: ✅
- **Reason**: CRGDBF 새 비트플리핑 경판정 LDPC 디코더+HW 아키텍처, NAND LDPC 이식 가능(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9516718
- **Type**: conference
- **Published**: 7-9 July 2
- **Authors**: Keyue Deng, Hangxuan Cui, Jun Lin +1
- **PDF**: https://ieeexplore.ieee.org/document/9516718
- **Abstract**: Tabu-list random-penalty gradient descent bit-flipping (TRGDBF) is a hard-decision algorithm for decoding low-density parity-check (LDPC) codes, which offers a significant improvement in error correction. However, compared to the current gradient descent bit-flipping (GDBF) variants, it converges slower and has no obvious performance advantage unless enough iterations are allowed. To accelerate the convergence speed, this paper presents a counter random GDBF (CRGDBF) algorithm in which a bit is forbidden to flip in the next iteration after being flipped several times. Incorporating the random operation, the forbidden-mechanism shows a dynamic property, facilitating the decoder more efficiently to break trapping sets. Simulation results show that the CRGDBF can achieve up to 5 times better decoding performance than the TRGDBF algorithm within finite iterations. Additionally, an architecture is presented for implementing the CRGDBF algorithm, demonstrating it only brings limited hardware overhead compared to the TRGDBF.

## FPGA Implementation of LDPC Decoder Architecture for Wireless Communication Standards

- **Status**: ✅
- **Reason**: QC-LDPC FPGA 디코더로 새 parallel multicore VTC/CTV 아키텍처+prior shift 제안 — 이식 가능 HW(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:9493380
- **Type**: conference
- **Published**: 5-7 July 2
- **Authors**: Ruslan Goriushkin, Pavel Nikishkin, Evgeny Likhobabin +1
- **PDF**: https://ieeexplore.ieee.org/document/9493380
- **Abstract**: This paper presents a decoder design for Quasi-Cyclic (QC) Low-Density Parity-Check (LDPC) codes. The design is parameterized and can be easily rebuilt to support various LDPC Parity-Check matrices taken from the WiMAX (IEEE 802.16e) and the WiFi (IEEE 802.11n) standards. New techniques such as parallelization of the decoding architecture cores are proposed. These cores calculate variable-to-check (VTC) and new check-to-variable (CTV) messages and also update posterior probabilities (APPs). The parallel multicore decoding architecture implies a prior shift of values based on the LDPC matrix and simultaneous calculation of values for the core. Our decoder is implemented on FPGAs of the Zynq-7000 Mini-ITX Evaluation Board (XC7Z100-2FFG900). The throughput of up to 1,2 GBit/s and the operation frequency of up to 240 MHz have been achieved.

## Combination of Multi-impairments Compensation and Decoding for LDPC-coded CO-OFDM via Deep Learning

- **Status**: ✅
- **Reason**: 딥러닝 기반 LDPC 디코딩+보상 결합, 복잡도 저감 - 신경망 디코더 기법 이식 가능성, 애매하여 살림(Phase3 재검토)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9866227
- **Type**: conference
- **Published**: 3-7 July 2
- **Authors**: Ying Han, Yuanxiang Chen, Jia Fu +6
- **PDF**: https://ieeexplore.ieee.org/document/9866227
- **Abstract**: We propose a combination scheme of multi-impairment compensation and LDPC decoding based deep learning for LDPC-coded CO-OFDM system. Experiments show it can greatly reduce the BER and decoding complexity in different transmission scenarios.

## Design of Protograph-based LDPC Codes for DVB-S2 Systems

- **Status**: ✅
- **Reason**: protograph 기반 LDPC 코드 설계 + PEXIT 분석 — 바이너리 코드 구성 기법 이식 가능(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9580405
- **Type**: conference
- **Published**: 28-30 July
- **Authors**: Runze Li, Jingyi Zhang, Pingping Chen +1
- **PDF**: https://ieeexplore.ieee.org/document/9580405
- **Abstract**: Since low-density parity-check (LDPC) codes have been studied and adopted in the DVB-S2 standard, many efforts have been made to improve their performance and optimize them up to the broadcasting standard. This paper proposes a family of protograph-based LDPC codes to provide a multi-rate coding for efficient DVB-S2 systems, considering low-complexity and excellent performance of the protograph codes. Moreover, we employ Bit Interleaved Code Modulation Iterative Decoding (BICM-ID) to enhance the performance of the ASK-modulated DVB systems. Both the protograph extrinsic information transfer (PEXIT) analysis and simulation results demonstrate the performance advantage of the proposed protograph-based LDPC codes over the conventional DVB-S2 codes for all the code rates. In particular, the proposed codes yield performance gains of more than 0.2 dB as compared to the conventional codes at high rates for 16-APSK modulations.

## Deep Learning Methods for Channel Decoding: A Brief Tutorial

- **Status**: ✅
- **Reason**: 채널 디코딩 딥러닝 튜토리얼(LDPC 포함 신경망 디코더) — 이식 가능 디코더 기법 서베이(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9580304
- **Type**: conference
- **Published**: 28-30 July
- **Authors**: Kai Niu, Jincheng Dai, Kailin Tan +1
- **PDF**: https://ieeexplore.ieee.org/document/9580304
- **Abstract**: The recent development of deep learning methods demonstrates a new insight to optimize the decoding of linear codes. In this paper, we survey the typical neural network decoding methods, including data-driven and model-driven schemes. We investigate the design principle, algorithm mechanism, parameter assignment, and training process of these neural decoders for high-density parity check (HDPC), low-density parity-check (LDPC), and polar codes. Finally, we summarize the advantages of neural network decoding and point out some research directions in the future.

## AVX-512 Based, High-Throughput LDPC Decoders

- **Status**: ✅
- **Reason**: AVX-512 기반 layered OMS-LDPC 고처리율 디코더 — 이식 가능한 병렬 디코더 구현(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:9527002
- **Type**: conference
- **Published**: 23-25 July
- **Authors**: Jingxin Dai, Hang Yin, Sihan Liu +1
- **PDF**: https://ieeexplore.ieee.org/document/9527002
- **Abstract**: Low Density Parity Check (LDPC) codes can approach the Shannon limit in digital communication systems and have good error correction performance. At present, with the continuous development of communication technology, the demand for the throughput of the communication system is also increasing. In order to further improve the throughput of the LDPC decoder, this paper uses the AVX512 instruction set based on the parallel structure of the LDPC codes decoding algorithm, and proposes a design scheme based on the layered OMS-LDPC decoding algorithm. This solution can be implemented on a general-purpose processor (GPP) and achieve higher throughput. The experimental results show that, in the case of 10 iterations, the decoder based on the X86 processor supporting AVX512 can reach a throughput of 53Mbps to 131Mbps.

## Hardware Implementation Method of LDPC Efficient Decoding Based on FPGA

- **Status**: ✅
- **Reason**: FPGA 기반 LDPC 효율 디코딩, 고정소수점/reweighting/tree topology HW 개선 — 이식 가능 HW(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:9603866
- **Type**: conference
- **Published**: 23-25 July
- **Authors**: Yuyang Ji, Yanjun Ji
- **PDF**: https://ieeexplore.ieee.org/document/9603866
- **Abstract**: In this paper,the logarithmic domain efficient decoding algorithm of LDPC code has been deeply studied,and the efficient algorithm with tree topology structure has been improved. The fixed-point representation and reweighting analysis of the receiving and processing information of LDPC code decoding has been carried out. At the same time,based on Quartus development software platform and Verilog HDL language,the efficient parallel decoding algorithm of regular LDPC code with length of 8designed by geometric construction method is designed, and the circuit design and simulation results of some main modules are given. The logic synthesis and implementation of the whole algorithm are carried out on StatixL EP2S60F484C3.The highest data processing rate is 10Mbps,and the error correction performance is ideal. After the reprocessing method is adopted,all the information in the decoding implementation process is the same standard,and there is no need for additional processing , which reduces the hardware complexity and calculation delay,and meets the needs of engineering implementation.

## Quasi-Cyclic Protograph-Based Raptor-Like LDPC Codes With Girth 6 and Shortest Length

- **Status**: ✅
- **Reason**: 다중에지 QC-PBRL-LDPC degree reduction 신규 구성법 + girth-6 4-cycle 제거 충분조건 — 바이너리 코드설계 기법(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9518125
- **Type**: conference
- **Published**: 12-20 July
- **Authors**: Farzane Amirzade, Mohammad-Reza Sadeghi, Daniel Panario
- **PDF**: https://ieeexplore.ieee.org/document/9518125
- **Abstract**: We consider multiple-edge QC-LDPC codes with a base matrix of large size. We propose a new method, the degree reduction method, to obtain exponent matrices of these codes which considerably reduces the complexity of the search algorithm. We also provide a necessary and sufficient condition to avoid 4-cycles from occurrence in the Tanner graph of codes obtained using our method. Then, we apply our method to quasi-cyclic protograph-based Raptor-Like LDPC (QC-PBRL-LDPC) codes whose base matrices are multiple-edge. Numerical results show that as a consequence of this study we can obtain the minimum lifting degree of QC-PBRL-LDPC codes with girth at least 6. Thus, the lengths of the obtained codes are much smaller than those of their counterpart short-length codes in the literature.

## Construction of Algebraic-Based Variable-Rate QC-LDPC Codes

- **Status**: ✅
- **Reason**: 대수기반 variable-rate QC-LDPC 신규 구성 + isomorphism 기반 탐색공간 축소·cycle 분포 개선 — 바이너리 코드설계 기법(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9518132
- **Type**: conference
- **Published**: 12-20 July
- **Authors**: Huaan Li, Baoming Bai, Hengzhou Xu +1
- **PDF**: https://ieeexplore.ieee.org/document/9518132
- **Abstract**: In this paper, we concentrate on one algebraic-based quasi-cyclic low-density parity-check (QC-LDPC) code constructed from two subsets of a finite field and generalize it to propose a class of variable-rate QC-LDPC (VR-QC-LDPC) codes, whose parity-check matrices are nested horizontally and have constant number of rows. Thus the proposed codes are significant at least in terms of storage complexity and can be simply implemented. The constructed codes also inherit the original algebraic-based QC-LDPC codes and their exponent matrices can be obtained from two subsets of the given finite field. We hereby analyze the structural properties from the isomorphism perspective, and present some rules to significantly prune the size of search space and determine the non-isomorphic exponent matrices. By distinguishing the smaller quantities of non-isomorphic matrices with cycle property metric, we can easily construct a series of nested exponent matrices with better cycle distributions and obtain the VR-QC-LDPC codes. Numerical results demonstrate that the constructed codes have better iterative decoding performance within a range of code rates and decoding iterations.

## Necessary and Sufficient Girth Conditions for Tanner Graphs of Quasi-Cyclic LDPC Codes

- **Status**: ✅
- **Reason**: QC-LDPC girth 6~12 필요충분조건 + 구성 알고리즘 — 바이너리 사이클/girth 코드설계 기법(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9518241
- **Type**: conference
- **Published**: 12-20 July
- **Authors**: Roxana Smarandache, David G. M. Mitchell
- **PDF**: https://ieeexplore.ieee.org/document/9518241
- **Abstract**: This paper revisits the connection between the girth of a protograph-based LDPC code given by a parity-check matrix and the properties of powers of the product between the matrix and its transpose in order to obtain the necessary and sufficient conditions for a code to have given girth between 6 and 12, and to show how these conditions can be incorporated into simple algorithms to construct codes of that girth. To this end, we highlight the role that certain submatrices that appear in these products have in the construction of codes of desired girth. In particular, we show that imposing girth conditions on a parity-check matrix is equivalent to imposing conditions on a square submatrix obtained from it and we show how this equivalence is particularly strong for a protograph based parity-check matrix of variable node degree 2, where the cycles in its Tanner graph correspond one-to-one to the cycles in the Tanner graph of a square submatrix obtained by adding the permutation matrices (or products of these) in the composition of the parity-check matrix. We end the paper with exemplary constructions of codes with various girths and computer simulations. Although, we mostly assume the case of fully connected protographs of variable node degree 2 and 3, the results can be used for any parity-check matrix/protograph-based Tanner graph.

## Codes approaching the Shannon limit with polynomial complexity per information bit

- **Status**: ✅
- **Reason**: weight-3 LDPC + polar 결합 디코딩(LDPC/polar 왕복) 새 스킴, 부호 비의존적 BP 이식 가능성·error floor 분석(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9517788
- **Type**: conference
- **Published**: 12-20 July
- **Authors**: Ilya Dumer, Navid Gharavi
- **PDF**: https://ieeexplore.ieee.org/document/9517788
- **Abstract**: We consider codes for channels with extreme noise that emerge in various low-power applications. Simple LDPC codes with parity checks of weight 3 are first studied for any code dimension m → ∞. These codes form modulation schemes: they improve the original channel outputs for any SNR > -6 dB (per information bit) and gain 3 dB over uncoded modulation as SNR grows. However, they also have a floor on the output bit error rate (BER) irrespective of their length. Tight lower and upper bounds, which are virtually identical to simulation results, are then obtained for BER at any SNR. We also study a combined scheme that splits $m$ information bits into $b$ blocks and protects each with some polar code. Decoding moves back and forth between polar and LDPC codes, every time using a polar code of a higher rate. For m → ∞and a sufficiently large parameter b, this design yields a vanishing BER at any SNR above the Shannon limit of -1.59 dB and has complexity order of m log m per information bit.

## Proximal Decoding for LDPC-coded Massive MIMO Channels

- **Status**: ✅
- **Reason**: 근접(proximal) 최적화 기반 LDPC 디코딩 알고리즘, 부호 proximal operator 새 디코더로 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9517988
- **Type**: conference
- **Published**: 12-20 July
- **Authors**: Tadashi Wadayama, Satoshi Takabe
- **PDF**: https://ieeexplore.ieee.org/document/9517988
- **Abstract**: We propose a novel optimization-based decoding algorithm for LDPC-coded massive MIMO channels. The proposed decoding algorithm is based on a proximal gradient method for solving an approximate maximum a posteriori (MAP) decoding problem. The key idea is the use of a code-constraint polynomial penalizing a vector far from a codeword as a regularizer in the approximate MAP objective function. The code proximal operator is naturally derived from code-constraint polynomials. The proposed algorithm, called proximal decoding, can be described by a simple recursion consisting of the gradient descent step for a negative log-likelihood function and the code proximal operation. Several numerical experiments show that the proposed algorithm outperforms known massive MIMO detection algorithms, such as an MMSE detector with belief propagation decoding.

## Encoding and Decoding Construction D' Lattices for Power-Constrained Communications

- **Status**: ✅
- **Reason**: Construction D' lattice용 QC-LDPC 신규 설계 + 저복잡도 인코딩/디코딩 — 바이너리 QC-LDPC 구성 기법 이식 가능(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9518122
- **Type**: conference
- **Published**: 12-20 July
- **Authors**: Fan Zhou, Arini Fitri, Khoirul Anwar +1
- **PDF**: https://ieeexplore.ieee.org/document/9518122
- **Abstract**: This paper focuses on the encoding and decoding of Construction D' coding lattices that can be used with shaping lattices for power-constrained channels. Two encoding methods and a decoding algorithm for Construction D' lattices are given. A design of quasi-cyclic low-density parity-check (QC-LDPC) codes to form Construction D' lattices is presented. This allows construction of nested lattice codes which are good for coding, good for shaping, and have low-complexity encoding and decoding. Numerical results using $E_{8},\ BW_{16}$ and Leech lattices for shaping a Construction D' lattice indicate that the shaping gains 0.65 dB, 0.86 dB and 1.03 dB are preserved, respectively.
