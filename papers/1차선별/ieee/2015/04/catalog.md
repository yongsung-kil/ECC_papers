# IEEE Xplore — 2015-04 (1차선별 통과)


## A Two-Stage Decoding Algorithm to Lower the Error-Floors for LDPC Codes

- **Status**: ✅
- **Reason**: 새 2단계 디코딩 알고리즘으로 LDPC error-floor 낮춤(LLR 조작·정지기준), 바이너리 LDPC BP 디코더 개선 기법 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7036084
- **Type**: journal
- **Published**: April 2015
- **Authors**: Xueting Zhang, Shaoping Chen
- **PDF**: https://ieeexplore.ieee.org/document/7036084
- **Abstract**: A two-stage decoding algorithm to lower the error-floor for low-density parity-check (LDPC) codes is presented. An efficient stopping criterion is proposed to avoid unnecessary iterations in the first stage. If the stopping criterion is reached, the first stage decoding will be terminated and the second stage decoding will be started, where the unsuccessfully decoded words are re-decoded by manipulating the log-likelihood ratio (LLR) of two types of specifically selected variable nodes. Simulation results show that the proposed algorithm can effectively lower the error floor of LDPC codes while maintaining a low decoding complexity.

## Construction of block-LDPC codes based on quadratic permutation polynomials

- **Status**: ✅
- **Reason**: QPP 기반 block-LDPC 신규 구성(QC-LDPC를 부분집합으로 포함), 바이너리 코드설계 기법 이식 가능(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7104844
- **Type**: journal
- **Published**: April 2015
- **Authors**: Wu Guan, Liping Liang
- **PDF**: https://ieeexplore.ieee.org/document/7104844
- **Abstract**: A new block low-density parity-check (Block-LDPC) code based on quadratic permutation polynomials (QPPs) is proposed. The parity-check matrix of the Block-LDPC code is composed of a group of permutation submatrices that correspond to QPPs. The scheme provides a large range of implementable LDPC codes. Indeed, the most popular quasi-cyclic LDPC (QC-LDPC) codes are just a subset of this scheme. Simulation results indicate that the proposed scheme can offer similar error performance and implementation complexity as the popular QC-LDPC codes.

## Quasi-Cyclic Representation and Vector Representation of RS-LDPC Codes

- **Status**: ✅
- **Reason**: RS-LDPC의 QC 표현으로 circulant permutation 기반 QC-LDPC 구성·랭크 분석 — 바이너리 LDPC 코드 설계 기법(E) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7029068
- **Type**: journal
- **Published**: April 2015
- **Authors**: Haiyang Liu, Qin Huang, Gang Deng +1
- **PDF**: https://ieeexplore.ieee.org/document/7029068
- **Abstract**: RS-LDPC codes, constructed based on the codewords of Reed-Solomon (RS) codes with two information symbols, are an important class of LDPC codes. In this paper, we present two representations, namely, quasi-cyclic (QC) representation and vector representation, for RS-LDPC codes. Under the first representation, most part of the parity-check matrix of a full-length RS-LDPC code consists of circulant permutation matrices and zero matrices. As a result, the class of codes can enjoy the advantages in hardware implementation as QC-LDPC codes. In addition, the base matrix under the QC representation of an RS-LDPC code can be explicitly given such that the rank of its parity-check matrix can be analyzed combinatorially. Under the second representation, each permutation matrix in the parity-check matrix of an RS-LDPC code is defined by a nonbinary vector, whose entries are a permutation of entries in the field from which the RS code is constructed. Then, the “affine invariance” property is proved for full-length RS-LDPC codes, which can facilitate the structural analysis of the codes.

## High-Rate Quantum Low-Density Parity-Check Codes Assisted by Reliable Qubits

- **Status**: ✅
- **Reason**: 고전 바이너리 LDPC를 활용한 high-rate 부호 구성·신드롬 디코딩 — 양자보조이나 고전 바이너리 LDPC 구성/디코딩 기법 유래, 애매하여 Phase 3 재검토(E/C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7027863
- **Type**: journal
- **Published**: April 2015
- **Authors**: Yuichiro Fujiwara, Alexander Gruner, Peter Vandendriessche
- **PDF**: https://ieeexplore.ieee.org/document/7027863
- **Abstract**: Quantum error correction is an important building block for reliable quantum information processing. A challenging hurdle in the theory of quantum error correction is that it is significantly more difficult to design error-correcting codes with desirable properties for quantum information processing than for traditional digital communications and computation. A typical obstacle to constructing a variety of strong quantum error-correcting codes is the complicated restrictions imposed on the structure of a code. Recently, promising solutions to this problem have been proposed in quantum information science, where in principle any binary linear code can be turned into a quantum error-correcting code by assuming a small number of reliable quantum bits. This paper studies how best to take advantage of these latest ideas to construct desirable quantum error-correcting codes of very high information rate. Our methods exploit structured high-rate low-density parity-check codes available in the classical domain and provide quantum analogues that inherit their characteristic low decoding complexity and high error correction performance even at moderate code lengths. Our approach to designing high-rate quantum error-correcting codes also allows for making direct use of other major syndrome decoding methods for linear codes, making it possible to deal with a situation where promising quantum analogues of low-density parity-check codes are difficult to find.

## Recoverability of Variable Nodes in Periodically Punctured LDPC Convolutional Codes

- **Status**: ✅
- **Reason**: 주기적 펀처링 LDPC-CC의 노드 복구성 평가 신규 행렬 기반 알고리즘·펀처링 패턴 설계, 바이너리 코드설계 기법 이식 가능(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7042745
- **Type**: journal
- **Published**: April 2015
- **Authors**: Hua Zhou, Norbert Goertz
- **PDF**: https://ieeexplore.ieee.org/document/7042745
- **Abstract**: The concept of transformed codes is introduced to algebraically evaluate the recoverability of punctured nodes for periodically punctured low-density parity-check convolutional codes (LDPC-CCs) by a simple matrix-based approach. The proposed very efficient algorithm allows to identify and exclude those candidate puncturing patterns in a computer search that contain unrecoverable nodes that would lead to bad error-correction performance. Moreover, a novel upper bound on the maximum punctured code rate is obtained, above which any punctured code must contain unrecoverable punctured nodes.

## Anytime Reliability of Spatially Coupled Codes

- **Status**: ✅
- **Reason**: spatially coupled code 설계+적응 윈도 디코딩(저복잡도), 바이너리 SC-LDPC 코드설계·디코더 기법 이식 가능(C/E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7047734
- **Type**: journal
- **Published**: April 2015
- **Authors**: Md. Noor-A-Rahim, Khoa D. Nguyen, Gottfried Lechner
- **PDF**: https://ieeexplore.ieee.org/document/7047734
- **Abstract**: Anytime transmission was previously shown to be necessary and sufficient for tracking and controlling an unstable plant over a noisy channel. In this paper, we propose an efficient channel coding scheme for anytime transmission. We design this coding scheme based on spatially coupled codes and investigate its performance over binary erasure channels (BEC) and binary input additive white Gaussian noise (BIAWGN) channels. Through density evolution analysis, we asymptotically show the desired anytime properties of the proposed code. For the BEC, we derive the corresponding delay-exponent and numerically predict the finite-length performance of the proposed anytime code. We also propose adaptive window decoding techniques to ensure low complexity anytime receivers.

## Performance Improvement of Iterative Multiuser Detection for Large Sparsely Spread CDMA Systems by Spatial Coupling

- **Status**: ✅
- **Reason**: spatial coupling으로 BP 성능을 MAP까지 향상 — SC-LDPC 코드설계/디코더 분석 기법(E/C), 다중사용자 응용이나 핵심 기법 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7031889
- **Type**: journal
- **Published**: April 2015
- **Authors**: Keigo Takeuchi, Toshiyuki Tanaka, Tsutomu Kawabata
- **PDF**: https://ieeexplore.ieee.org/document/7031889
- **Abstract**: Kudekar et al. proved that the belief-propagation (BP) performance for low-density parity check codes can be boosted up to the maximum a posteriori (MAP) performance by spatial coupling. In this paper, spatial coupling is applied to sparsely spread code-division multiple-access systems to improve the performance of iterative multiuser detection based on BP. Two iterative receivers based on BP are considered: 1) one receiver is based on exact BP and 2) the other on an approximate BP with Gaussian approximation. The performance of the two BP receivers is evaluated via density evolution (DE) in the dense limit after taking the large-system limit, in which the number of users and the spreading factor tend to infinity while their ratio is kept constant. The two BP receivers are shown to achieve the same performance as each other in these limits. Furthermore, taking a continuum limit for the obtained DE equations implies that the performance of the two BP receivers can be improved up to the performance achieved by the symbol-wise MAP detection, called individually optimal detection, via spatial coupling. Numerical simulations show that spatial coupling can provide a significant improvement in bit-error rate for finite-sized systems especially in the region of high system loads.

## On the applicability of the most reliable basis algorithm for LDPC decoding in telecommand links

- **Status**: ✅
- **Reason**: most reliable basis(OSD류) 디코딩 + 양자화 영향 분석, 바이너리 short LDPC — 이식 가능 디코더/양자화 기법(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7103192
- **Type**: conference
- **Published**: 7-9 April 
- **Authors**: Marco Baldi, Nicola Maturo, Enrico Paolini +1
- **PDF**: https://ieeexplore.ieee.org/document/7103192
- **Abstract**: We analyze the performance of two short low-density parity-check codes recently proposed for updating the telecommand standard for space links. We show that the most reliable basis decoding algorithm can be efficiently applied to these codes, permitting us to achieve a significant coding gain with respect to more conventional iterative algorithms. In particular, in order to maintain limited complexity, we suggest to use a hybrid approach, that combines the two decoding procedures in a sequential manner. Thinking in terms of practical implementation, we also investigate the impact of quantization, by considering two different quantization laws and comparing their performance.

## Design and Implementation of Low Bit Error Rate of LDPC Decoder

- **Status**: ✅
- **Reason**: LLR-BP/SPA 디코더, min-sum 보정항, 양자화·log-tanh 근사가 error floor/absorbing set에 미치는 영향 — NAND LDPC 디코더로 직접 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7279944
- **Type**: conference
- **Published**: 4-6 April 
- **Authors**: Ashlesha P. Kshirsagar, Sandeep Kakde, Manish Chawhan +1
- **PDF**: https://ieeexplore.ieee.org/document/7279944
- **Abstract**: Many classes of high-performance Low-density parity check codes are based on parity check matrices composed of permutation sub matrices. The emulation-simulation framework further allows the algorithm and implementation to be iteratively redefined to improve the error floor performance of message passing decoder. Log-Like hood-Ratio (LLR) based Belief-Propagation (BP) algorithm is presented for Low Density Parity Check codes. Numerically accurate representation of check node update computation used in LLR-BP decoding is described. The implementation of Sum-Product algorithm (SPA) within Low Density Parity Check Code (LDPC) decoder is described in this paper and the correction term is used to improve the decoding performance of min-sum algorithm (MSA). Quantization and log-tanh function approximation in sum-product decoder strongly affect which absorbing set dominates in error floor region. For LDPC decoder, bit error rate (BER) decreases with increase in the signal to noise ratio.

## An algorithmic error-resilient scheme for robust LDPC decoding

- **Status**: ✅
- **Reason**: LDPC 디코딩의 소프트에러 내성 알고리즘적 검증 기법 — 부호 비의존적 디코더 신뢰성, NAND HW에 이식 가능(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7114527
- **Type**: conference
- **Published**: 27-29 Apri
- **Authors**: Huai-Ting Li, Ding-Yuan Lee, Kun-Chih Chen +1
- **PDF**: https://ieeexplore.ieee.org/document/7114527
- **Abstract**: To fit into multiple communication standards, flexible Low-Density Parity-Check (LDPC) decoding is desirable to be implemented in a chip multiprocessor (CMP) system. However, reliability issues, such as soft errors and timing errors, are severer in future advanced CMP systems when CMOS technology scale. Therefore, enhancing error resilience for a CMP system becomes an important design issue. In this paper, we propose a design methodology to achieve a robust LDPC decoding based on algorithmic error-resilient method. We firstly analyze the performance degradation caused by the soft errors which occur in the computing units (check node units and bit node units), and then explore the inherent error-tolerant characteristic of LDPC decoding algorithm. In our proposed method, we exploit some characteristic distribution or behavior in the operations of the LDPC decoding algorithm to validate the computing results. The experimental results show that the proposed algorithmic error resilience can approach the error-free decoder while facing high injected soft-error rate of 10−3 in computing units, but with only 6.07% computational overhead. To the best of our knowledge, this is the first discussion about the LDPC decoding algorithm in terms of soft errors in computing units.

## Spatial coupling of root-LDPC: Parity bits doping

- **Status**: ✅
- **Reason**: root-LDPC의 spatial coupling(패리티 도핑)으로 threshold 포화 — 바이너리 LDPC 코드 설계 기법(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7124695
- **Type**: conference
- **Published**: 27-29 Apri
- **Authors**: Volkan Dedeoglu, Fanny Jardel, Joseph J. Boutros
- **PDF**: https://ieeexplore.ieee.org/document/7124695
- **Abstract**: Random low-density parity-check (LDPC) ensembles do not achieve full diversity on block-fading channels. To cope with quasi-static fading, a special LDPC structure, known as root-LDPC, has been introduced. A root-LDPC ensemble guarantees that any information bit receives messages from all channel states. Results in the literature show that the gap between the root-LDPC boundary and the capacity boundary in the fading plane is not small enough. In this paper, we propose to saturate the whole root-LDPC boundary via spatial coupling. For simplicity, we adopt an equivalent erasure channel model rather than a block fading model. It is shown that spatial coupling of parity bits only is sufficient to saturate the root-LDPC threshold boundary in the erasure plane.

## Improved quasi-cyclic LDPC codes based on Euclidean geometry

- **Status**: ✅
- **Reason**: E — short cycle을 줄이는 개선된 EG QC-LDPC 행렬 구성 기법, 바이너리 LDPC 사이클 제거 구성으로 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7426007
- **Type**: conference
- **Published**: 24-26 Apri
- **Authors**: Yuan-hua Liu, Mei-ling Zhang
- **PDF**: https://ieeexplore.ieee.org/document/7426007
- **Abstract**: This paper presents an improved Euclidean geometry (EG) method for constructing parity check matrix of quasi-cyclic low-density parity-check (QC-LDPC) codes to decrease the performance degradation of short cycles to the iterative decoding. The new method results in a class of QC-LDPC codes with much fewer short cycles than usual EG-LDPC codes with the same parameters. Simulation results show that the designed QC-LDPC codes with fewer short cycles perform better than the existing Euclidean geometry LDPC codes under iterative decoding.

## Design of low density parity check decoder using Min-Sum algorithm

- **Status**: ✅
- **Reason**: Min-Sum LDPC 디코더 fully-parallel Verilog HW 구현 — 이식 가능 HW 아키텍처(D). 다만 표준 min-sum 수준이라 기여 약함
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:7322560
- **Type**: conference
- **Published**: 2-4 April 
- **Authors**: Sachin S. Bhojane, Monica V. Mankar, Gajendra M. Asutkar +1
- **PDF**: https://ieeexplore.ieee.org/document/7322560
- **Abstract**: Low density parity check (LDPC) code has received more attention due to their excellent error correcting performance capabilities. An LDPC code can be decoded using iterative method like the sum-product algorithm and the Min-Sum algorithm based on its Tanner graph. In this paper, fully parallel architecture has been designed for LDPC decoder using Min-Sum algorithm. This decoder modeled in Verilog synthesized and performed place and route for design using Xilinx 13.1.

## Accelerating and deceleratingmin-sum-based gear-shift LDPC decoders

- **Status**: ✅
- **Reason**: Min-Sum/Self-Corrected MS 기반 gear-shift 디코더 + 가변 양자화 — 이식 가능 디코더 알고리즘(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7178522
- **Type**: conference
- **Published**: 19-24 Apri
- **Authors**: Joao Andrade, Gabriel Falcao, Vitor Silva
- **PDF**: https://ieeexplore.ieee.org/document/7178522
- **Abstract**: Low-Density Parity-Check (LDPC) decoders typically implement a single decoding algorithm or update rule, which narrows down the design space of the decoder and maintains its overall simplicity. However, gear-shift techniques combine multiple decoding algorithms, update rules and quantization of the log-likelihood ratios (LLRs), allowing wider design space explorations as more parameters can be fine-tuned to a particular need. Gear-shift LDPC decoders have been shown to improve both the decoding throughput and the energy efficiency per bit decoded, while achieving similar capacity compared to traditional approaches that only use one algorithm. In this paper, we incorporate gear-shift techniques based on the Min-Sum algorithm (MSA) and Self-Corrected Min-Sum algorithm(SCMSA) using variable quantization steps. The proposed design allows bit error rate (BER) performances close to the more powerful SCMSA running only a selected number of iterations using the most powerful update rule.

## Enhancing LDPC code performance using pilot bits

- **Status**: ✅
- **Reason**: 파일럿 비트 삽입으로 트래핑셋 비활성화·error floor 저감 — 코드/디코딩 개선 기법(E), NAND LDPC error floor에 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7178520
- **Type**: conference
- **Published**: 19-24 Apri
- **Authors**: Jack F. Adolph, Jan C. Olivier, Brian P. Salmon
- **PDF**: https://ieeexplore.ieee.org/document/7178520
- **Abstract**: Creating the optimal bipartite graph and decoding of a Low Density Parity Check (LDPC) codeword on it is deemed an NP-complete problem. Much work in the last decade has gone into proper construction of LDPC codes with maximum girth and optimized stopping sets; to ensure the BER approaches channel capacity. When an edge alteration to the graph is proposed, it completely changes the performance of the graph and usually leads to the re-analysis of the entire graph's properties. In this work we propose a method of lowering the error floor experienced in an LDPC code by intelligently inserting a set of known bits in the message frame. This deactivates paths in the graph located around trapping sets without modification of edges in the graph, and provides high log-likelihood information to the induced sub-graph for improved performance.
