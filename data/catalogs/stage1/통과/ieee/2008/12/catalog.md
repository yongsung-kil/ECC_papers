# IEEE Xplore — 2008-12 (1차선별 통과)


## Robust LDPC decoding using irregular decoders

- **Status**: ✅
- **Reason**: 비정규(irregular) LDPC 코드-디코더 쌍 공동최적화로 수렴영역 확대, 이식 가능 코드설계/디코더 기법(E/C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4720241
- **Type**: journal
- **Published**: December 2
- **Authors**: Raman Yazdani, Masoud Ardakani
- **PDF**: https://ieeexplore.ieee.org/document/4720241
- **Abstract**: It has been observed that irregular decoders for low density parity-check (LDPC) codes can be more robust to channel estimation errors compared to conventional decoders. In this work, by presenting a robustness measure, we propose a method for the joint optimization of irregular LDPC code-decoder pairs to have the widest convergence region when channel estimation errors exist.

## Complex rotary codes revisited: a low-complexity high-performance decoding approach

- **Status**: ✅
- **Reason**: 복소 rotary 부호의 BP/sum-product 반복 디코딩 저복잡도 접근, 일반화 패리티검사 부호의 이식 가능 디코더 기법(C, 애매하면 in)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4711159
- **Type**: journal
- **Published**: December 2
- **Authors**: Zheng Ma, Pingzhi Fan, Qingchun Chen +2
- **PDF**: https://ieeexplore.ieee.org/document/4711159
- **Abstract**: In this paper, based on a belief-propagation decoding strategy, a class of generalized parity-check codes called complex rotary codes is investigated. It is shown that, by using iterative sum-product decoding, the complex rotary codes have a much lower decoding complexity than Turbo codes, but have almost the same performance for the high code rate and short frame case (frame length< 500 bits). It is also shown that the prime block size of complex rotary codes is essential to achieve better performance because of its uniform checking characteristic.

## Design of versatile eIRA codes for parallel decoders

- **Status**: ✅
- **Reason**: 병렬 디코더용 eIRA(불규칙 바이너리 LDPC) 구성, low-weight 코드워드/near-codeword 회피로 error floor 개선하는 코드설계 기법(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4711170
- **Type**: journal
- **Published**: December 2
- **Authors**: Libero Dinoi, Francesco Sottile, Sergio Benedetto
- **PDF**: https://ieeexplore.ieee.org/document/4711170
- **Abstract**: In this paper we propose a semi-random technique for the generation of a class of eIRA codes (a popular class of irregular LDPC codes that can be encoded in linear time) suited to partially parallel decoder implementations. The suggested technique tries to avoid both low-weight codewords and nearcodewords, which limit the performance of the belief propagation decoder. Its effectiveness is verified by comparison with literature results. The obtained codes are versatile, in terms of code-rate and block length, and they are characterized by a low error floor.

## Algorithms of Finding the First Two Minimum Values and Their Hardware Implementation

- **Status**: ✅
- **Reason**: LDPC 디코더용 1st/2nd 최소값 탐색 HW 아키텍처(min-sum 핵심 유닛), NAND LDPC HW 직접 이식(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:4511767
- **Type**: journal
- **Published**: Dec. 2008
- **Authors**: Chin-Long Wey, Ming-Der Shieh, Shin-Yo Lin
- **PDF**: https://ieeexplore.ieee.org/document/4511767
- **Abstract**: Given a set of numbers X, finding the minimum value of X, min_1st, is a very easy task. However, efficiently finding its second minimum value, min_2nd, requires the derivations of min_1st and finding the minimum value from the set of the remaining numbers. Efficient algorithms and cost-effective hardware of finding the two smallest of X are greatly needed for the low-density parity-check (LDPC) decoder design. The following two architectures are developed in this paper: (1) sorting-based (XS) approach and (2) tree structure (TS) approach. Experimental results show that the XS approach provides less number of comparisons, while the TS approach achieves higher speed performance at lower hardware cost. Since the hardware unit is repeatedly used in the LDPC decoder design, the proposed high-speed low-cost TS approach is strongly recommended.

## Sliced Message Passing: High Throughput Overlapped Decoding of High-Rate Low-Density Parity-Check Codes

- **Status**: ✅
- **Reason**: 고처리율 고부호율 LDPC 디코딩 sliced message passing 신규 부분병렬 HW 아키텍처, 이식 가능(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:4539703
- **Type**: journal
- **Published**: Dec. 2008
- **Authors**: Lingzhi Liu, C.-J. Richard Shi
- **PDF**: https://ieeexplore.ieee.org/document/4539703
- **Abstract**: The efficient implementation of high-rate high-throughout low-density parity-check (LDPC) code decoding presents challenges to both fully parallel decoding and memory-sharing partially parallel decoding schemes. In this paper, a new decoding scheme, sliced message passing (SMP), is introduced. The key idea is to slice the total set of N variable-to-check messages into equal-sized p chunks, then to perform check-node computation sequentially chunk by chunk. This new decoding scheme can break the sequential tie between the check- and variable-node update stages and thus greatly improve the throughput. The hardware architectures of SMP decoding are introduced. Each check-node processing unit of the proposed register-based architecture has only c/p inputs instead of c inputs. By remapping the variable-node and check-node processing unit decoding blocks, the optimized SMP decoding units can reduce the overall hardware cost, shorten the critical-path delay, and improve the hardware-usage efficiency. An optimized SMP decoder has been further implemented for a 2048-bit (6, 32) LDPC decoder of the emerging IEEE 10 GBase-T standard in an IBM CMOS 90-nm process. Implementation results from synthesis and post layout simulation have shown the effectiveness of the proposed SMP scheme.

## Concatenated Low-Density Parity-Check and BCH Coding System for Magnetic Recording Read Channel With 4 kB Sector Format

- **Status**: ✅
- **Reason**: 자기기록용 LDPC+BCH 연접부호, 반복간 비트오류 진동 활용 디코딩 전략+FPGA 저SER 검증 - 스토리지 ECC 디코딩 기법(B/C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4711302
- **Type**: journal
- **Published**: Dec. 2008
- **Authors**: Ningde Xie, Wei Xu, Tong Zhang +2
- **PDF**: https://ieeexplore.ieee.org/document/4711302
- **Abstract**: In this paper, we examine the potential of applying concatenated low-density parity-check (LDPC) and Bose-Chaudhuri-Hocquenghem (BCH) coding for magnetic recording read channel with a 4 kB sector format. One key observation for such concatenated coding systems is that the overall error correction capability can be improved by exploiting the iteration-by-iteration bit error number oscillation behavior in case of inner LDPC code decoding failures. Moreover, assisted by field programmable gate array (FPGA)-based simulation platforms, empirical error-correcting performance analysis can reach a very low sector error rate (e.g., 10-10 and below), which is almost infeasible for LDPC-only coding systems. Finally, concatenated coding can further reduce the silicon cost. By implementing a high-speed FPGA-based perpendicular recording read channel simulator, we investigate a 4 kB rate-15/16 concatenated coding system with a 512-byte rate-19/20 inner LDPC code and an outer 4 kB BCH code. We apply a decoding strategy that can fully utilize the bit error number oscillation behavior of inner LDPC code decoding, and show that its sector error rate drops down to 10-11. For the purpose of comparison, we use the FPGA-based simulator to empirically observe the performance of 4 kB rate-15/16 LDPC and Reed-Solomon (RS) codes down to 10-7-10-8. Finally, we estimate the silicon cost of this concatenated coding system at 65 nm node, and compare it with that of the RS-only and LDPC-only coding systems.

## Efficient Implementation of Low-Density Parity-Check Convolutional Code Encoders With Built-In Termination

- **Status**: ✅
- **Reason**: LDPC-CC 인코더 built-in termination HW 아키텍처(1Gb/s, 90nm) - 이식 가능 HW/코드설계 기여(D/E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4694053
- **Type**: journal
- **Published**: Dec. 2008
- **Authors**: Zhengang Chen, Tyler L. Brandon, Stephen Bates +2
- **PDF**: https://ieeexplore.ieee.org/document/4694053
- **Abstract**: Low-density parity-check convolutional codes (LDPC-CCs) have demonstrated comparable error-correcting performance to LDPC block codes (LDPC-BCs). However, the LDPC-CC encoder requires termination when applied to finite-length data frames to ensure that the trailing information bits are fully protected. In this paper, the LDPC-CC encoder design is investigated, and a novel termination scheme is proposed. Starting from any encoder state, the proposed scheme is capable of generating a termination sequence in hardware without padding, thus minimizing the rate loss due to termination. A high-speed architecture for LDPC-CC encoders with built-in termination is proposed. Synthesis results for LDPC-CCs of code memory size up to 512 demonstrate maximum encoding throughputs of around 1 Gb/s for a 90-nm CMOS technology. The implementation cost for such encoders is shown to be reasonably low for average-sized LDPC-CCs.

## Adaptive Methods for Linear Programming Decoding

- **Status**: ✅
- **Reason**: 적응적 LP 디코딩: redundant parity check로 제약 추가, 패리티검사 밀도 무관한 복잡도 감소 - 부호 비의존 디코더 기법(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4675739
- **Type**: journal
- **Published**: Dec. 2008
- **Authors**: Mohammad H. Taghavi N., Paul H. Siegel
- **PDF**: https://ieeexplore.ieee.org/document/4675739
- **Abstract**: Detectability of failures of linear programming (LP) decoding and the potential for improvement by adding new constraints motivate the use of an adaptive approach in selecting the constraints for the underlying LP problem. In this paper, we make a first step in studying this method, and show that by starting from a simple LP problem and adaptively adding the necessary constraints, the complexity of LP decoding can be significantly reduced. In particular, we observe that with adaptive LP decoding, the sizes of the LP problems that need to be solved become practically independent of the density of the parity-check matrix. We further show that adaptively adding extra constraints, such as constraints based on redundant parity checks, can provide large gains in the performance.

## Approximate examination of trapping sets of LDPC codes using the probabilistic algorithm

- **Status**: ✅
- **Reason**: LDPC trapping set(error floor 지배 구조) 탐색 알고리즘 제안. 바이너리 LDPC 코드설계(error floor)에 이식 가능 → 포함(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4895509
- **Type**: conference
- **Published**: 7-10 Dec. 
- **Authors**: Masanori Hirotomo, Yoshiho Konishi, Masakatu Morii
- **PDF**: https://ieeexplore.ieee.org/document/4895509
- **Abstract**: The performance of LDPC codes decoded by iterative algorithms depends on the structural properties of their underlying Tanner graphs. For general memoryless channels, error patterns dominating the bit and frame error probabilities at the error floor region are termed trapping sets. In this paper, we propose an effective method for finding small-size trapping sets of LDPC codes. In the proposed method, a probabilistic algorithm to find low-weight codewords is applied to finding small trapping sets of LDPC codes. Furthermore, we show numerical results of examining small trapping sets of (504, 252) and (1008, 504) LDPC codes.

## Rate estimation scheme for weighted bit-flipping decoding of rate compatible LDPC codes

- **Status**: ✅
- **Reason**: C: RC-LDPC 가중 비트플립(WBF) 기반 부호율 추정, 디코딩 기법 이식 가능성
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4895385
- **Type**: conference
- **Published**: 7-10 Dec. 
- **Authors**: Kenji Kita, Tetsuo Tsujioka
- **PDF**: https://ieeexplore.ieee.org/document/4895385
- **Abstract**: This paper considers a new rate estimation scheme for rate compatible LDPC (RC-LDPC) codes. We have investigated some estimation schemes for RC-LDPC codes even though there is no side information about code rates used at a transmitter. The previous schemes were based on log-likelihood ratio of sum-product decoders at a receiver. Because of too much computational complexity, simpler estimation schemes are expected to be developed. For this purpose, we focus on a simpler decoding scheme, thus weighted bit-flipping (WBF) decoding which have been much attention by many reseachers recently. In this paper, we propose a new rate estimation scheme and evaluate its performance. Simulation results show that the proposed scheme has advantages of much effectiveness and potential for estimating code rates.

## Variable-to-Check Residual Belief Propagation for informed dynamic scheduling of LDPC codes

- **Status**: ✅
- **Reason**: VCRBP 동적 스케줄링 BP 제안 — 수렴/성능/복잡도 개선하는 새 디코더 알고리즘, 바이너리 LDPC BP에 직접 이식 → 포함(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4895535
- **Type**: conference
- **Published**: 7-10 Dec. 
- **Authors**: Jung-Hyun Kim, Mi-Young Nam, Hong-Yeop Song +1
- **PDF**: https://ieeexplore.ieee.org/document/4895535
- **Abstract**: We propose Variable-to-Check Residual Belief Propagation (VCRBP) for LDPC decoding for faster convergence, better error correcting performance and lower complexity. It is similar to Residual Belief Propagation (RBP) that was recently applied to LDPC decoding by Vila Casado et al. because it is also a dynamic scheduling belief propagation using residuals, but it is different because its residuals are computed from variable-to-check message. Simulation shows that it out-performs with only maximum 8 iterations by about 0.3 dB compared with RBP at an FER of 10-4. Also, we propose node-wise VCRBP (N-VCRBP) for reducing complexity of VCRBP. N-VCRBP also exhibits the performance very close to VCRBP but with significantly lower decoding complexity.

## Rate-compatible punctured LDPC codes based on recovery tree

- **Status**: ✅
- **Reason**: Rate-compatible punctured LDPC 새 puncturing pattern 탐색 알고리즘 = 코드설계(E), 바이너리 LDPC, NAND 레이트적응에 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4895650
- **Type**: conference
- **Published**: 7-10 Dec. 
- **Authors**: Sunghoon Choi, Kwangseok Noh, Jeong Hwan Shin +1
- **PDF**: https://ieeexplore.ieee.org/document/4895650
- **Abstract**: We consider the challenges of finding good puncturing patterns for rate-compatible LDPC codes over additive white Gaussian noise (AWGN) channel. In previous works, the role of survived check nodes in puncturing patterns was considered with the limitations such as single survived check node assumption and simulation-based verification. In this paper, we analyze the performance according to the role of multiple survived check nodes and multiple dead check nodes. Based on theses analyses, we propose new algorithm to find good puncturing pattern for LDPC codes over additive white Gaussian noise (AWGN) channel.

## Gradient descent bit flipping algorithms for decoding LDPC codes

- **Status**: ✅
- **Reason**: C: 신규 gradient descent bit flipping(GDBF) LDPC 디코딩 알고리즘, NAND 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4895387
- **Type**: conference
- **Published**: 7-10 Dec. 
- **Authors**: Tadashi Wadayama, Keisuke Nakamura, Masayuki Yagita +3
- **PDF**: https://ieeexplore.ieee.org/document/4895387
- **Abstract**: A novel class of bit-flipping (BF) algorithms for decoding low-density parity-check (LDPC) codes is presented. The proposed algorithms, which are called gradient descent bit flipping (GDBF) algorithms, can be regarded as simplified gradient descent algorithms. Based on gradient descent formulation, the proposed algorithms are naturally derived from a simple nonlinear objective function.

## Improvement of the forced-convergence decoding for LDPC codes

- **Status**: ✅
- **Reason**: forced-convergence 디코딩 수렴기준 개선으로 복잡도 절감 — SP 변형 새 디코더 알고리즘, 바이너리 LDPC 이식 가능 → 포함(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4895536
- **Type**: conference
- **Published**: 7-10 Dec. 
- **Authors**: Rumi Aoyama, Yuichi Kaji
- **PDF**: https://ieeexplore.ieee.org/document/4895536
- **Abstract**: An improvement of the forced-convergence decoding algorithm is discussed. Iterative decoding schemes such as the sum-product (SP) decoding bring out excellent performance of low-density parity check (LDPC) codes. The forced-convergence (FC) decoding is also an iterative decoding algorithm obtained by modifying the SP decoding. The FC decoding succeeds to reduce the decoding complexity of the SP decoding, but the error correcting performance is severely degraded by the modification. The performance degradation of the FC decoding is expected to be mitigated if the convergence criterion used in the algorithm is appropriately modified. This paper discusses several types of modifications of the convergence criteria. Computer simulation shows that the proposed modifications improve the performance of the FC decoding algorithm.

## Efficient encoding of QC-LDPC codes related to cyclic MDS codes

- **Status**: ✅
- **Reason**: QC-LDPC 선형시간 systematic 인코딩 알고리즘(다항식 회로 구현) — 코드설계/인코더 HW 기여로 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4895414
- **Type**: conference
- **Published**: 7-10 Dec. 
- **Authors**: Norifumi Kamiya, Eisaku Sasaki
- **PDF**: https://ieeexplore.ieee.org/document/4895414
- **Abstract**: In this paper, we present an efficient systematic encoding algorithm for quasi-cyclic (QC) low-density parity-check (LDPC) codes which are related to cyclic maximum-distance separable (MDS) codes. The algorithm has linear time complexity, and it can be easily implemented by using polynomial multiplication and division circuits. We show that the division polynomials can be completely characterized by its zeros and that the sum of the numbers of the zeros is equal to the parity-length of the codes.

## New stopping criteria for decoding LDPC codes in H-ARQ systems

- **Status**: ✅
- **Reason**: LDPC BP 디코딩 조기종료 기준 조합(syndrome 등)—복잡도 절감 기법으로 NAND LDPC 디코더에 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4895538
- **Type**: conference
- **Published**: 7-10 Dec. 
- **Authors**: Beomkyu Shin, Sang-Hyo Kim, Jong-Seon No +1
- **PDF**: https://ieeexplore.ieee.org/document/4895538
- **Abstract**: In this paper, we propose a combination of stopping criteria for BP decoding of LDPC codes effective on both high and low SNR and scalable to variable rate and length codes. The proposed algorithms combine three distinct criteria for decoding including conventional syndrome stopping. Each criterion is extremely simple and shall not be a burden to overall system. With these criteria, it is shown that the decoding complexity of H-ARQ system with AMC scheme can be reduced.

## A class of invertible circulant matrices for QC-LDPC codes

- **Status**: ✅
- **Reason**: 4-cycle 없는 invertible circulant 행렬 클래스로 sparse QC-LDPC 패리티검사/생성행렬 설계 — 바이너리 코드설계(E) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4895413
- **Type**: conference
- **Published**: 7-10 Dec. 
- **Authors**: Marco Baldi, Federico Bambozzi, Franco Chiaraluce
- **PDF**: https://ieeexplore.ieee.org/document/4895413
- **Abstract**: This paper presents a new class of easily invertible circulant matrices, defined by exploiting the isomorphism from the ring Mn of n times n circulant matrices over GF(p) to the ring Rn = GF(p)[x]/(xn - 1) of the polynomials modulo (xn - 1). Such class contains matrices free of 4-length cycles that, if sparse, can be included in the parity check matrix of QC-LDPC codes. Bounds for the weight of their inverses are also determined, that are useful for designing sparse generator matrices for these error correcting codes.

## Code design and performance analysis using a 2-level generalized Tanner graph on the binary erasure channel

- **Status**: ✅
- **Reason**: 일반화 Tanner graph(GLDPC) 코드설계+밀도진화, BEC 바이너리—구성/디코딩 복잡도 개선 기법 이식 가능(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4895648
- **Type**: conference
- **Published**: 7-10 Dec. 
- **Authors**: Eirik Rosnes
- **PDF**: https://ieeexplore.ieee.org/document/4895648
- **Abstract**: In this work, we consider code design and performance analysis using a 2-level generalized Tanner graph on the binary erasure channel. The 2-level generalized Tanner graph is composed of traditional variables nodes on the left side and generalized check nodes on the right side. The generalized check nodes are (dc, dc - 2), dc ges 3, binary linear codes. Iterative decoding is applied to the 2-level generalized Tanner graph using maximum a posteriori (MAP) erasure correction in the generalized check nodes. With MAP erasure correction, each check node decoder removes as much erasures as possible, even if it cannot resolve all erasures. Code design is done using density evolution, and we will show that the proposed scheme achieves both a better design rate and lower decoding complexity compared to the traditional scheme with only single parity-check nodes.

## On the design of irregular gldpc codes with low error floor over the BEC

- **Status**: ✅
- **Reason**: GLDPC error floor 저감 코드설계(stopping set 분석 기반)—바이너리 LDPC 구성 기법으로 이식 가능(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4895647
- **Type**: conference
- **Published**: 7-10 Dec. 
- **Authors**: Enrico Paolini, Marc Fossorier, Marco Chiani
- **PDF**: https://ieeexplore.ieee.org/document/4895647
- **Abstract**: The design of GLDPC codes for the binary erasure channel with low error floor under iterative decoding is investigated. Both bounded distance and maximum a posteriori decoding at the check nodes are considered. For both check node decoding algorithms a key parameter is identified, discriminating between an exponentially small and exponentially large expected number of small size stopping sets. A code design technique is proposed based on this theoretical investigation.

## Determination of the shortest balanced cycles

- **Status**: ✅
- **Reason**: QC-LDPC 구성을 위한 shortest balanced cycle 판정 조건 — girth/사이클 제거 기반 코드설계(E) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4895416
- **Type**: conference
- **Published**: 7-10 Dec. 
- **Authors**: Yuansheng Tang, Xinmei Huang, Jinli Wang +1
- **PDF**: https://ieeexplore.ieee.org/document/4895416
- **Abstract**: For the construction of some quasi-cyclic low-density parity-check codes, it is desired to find all the shortest balanced cycles in a base matrix. In this paper, we give some necessary and sufficient conditions for the existence of balanced cycles. Furthermore, we show that any of the shortest balanced cycles in a base matrix consists of the points of a sub-matrix of some patterns which are completely determined.

## Towards universal cover decoding

- **Status**: ✅
- **Reason**: C: min-sum 디코더 그래프커버/LP 디코딩 분석, BP 디코더 이론 개선 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4895386
- **Type**: conference
- **Published**: 7-10 Dec. 
- **Authors**: Nathan Axvig, Deanna Dreher, Katherine Morrison +3
- **PDF**: https://ieeexplore.ieee.org/document/4895386
- **Abstract**: In this paper, the non-codeword errors was analyzed that occur during parallel, iterative decoding with the min-sum decoder. Recently, work has been done relating the min-sum decoder to the linear programming (LP) decoder via graph covers. The LP decoder recasts the problem of decoding as an optimization problem whose feasible set is a polytope defined by the parity-check matrix of a code. It was shown that LP decoding can be realized as a decoder operating on graph covers.

## Noise Thresholds for Discrete LDPC Decoding Mappings

- **Status**: ✅
- **Reason**: 이산 메시지 양자화+min-sum 노드함수 설계(상호정보 기반 그리디), LLR 양자화 디코더로 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4697989
- **Type**: conference
- **Published**: 30 Nov.-4 
- **Authors**: Brian M. Kurkoski, Kazuhiko Yamaguchi, Kingo Kobayashi
- **PDF**: https://ieeexplore.ieee.org/document/4697989
- **Abstract**: For decoding low-density parity-check (LDPC) codes on discrete memoryless channels, a method to quantize messages and to find message-passing decoding functions for the variable and check nodes is developed. These are used to obtain noise thresholds by density evolution. The message-passing decoding alphabet is restricted to be discrete with a fixed maximum alphabet size. Discrete quantization is required to obtain this fixed alphabet size; a greedy algorithm which uses the mutual information between the code bit and message is presented. It is argued that using this message-passing decoding framework is more efficient for approaching channel capacity than simply quantizing the belief-propagation algorithm. This method is evaluated using regular LDPC codes on the binary symmetric channel. Using a maximum alphabet size of 16 (4 bits), noise thresholds close to those of belief propagation are obtained.

## Evaluation of the Concatenation of LDPC and RS Codes in Magnetic Recording Channel Using Field Programmable Gate Arrays

- **Status**: ✅
- **Reason**: LDPC+RS concatenation for magnetic recording (스토리지 ECC) on FPGA HW; code rate/HW 평가 떼어내 NAND LDPC에 이식 가능 (B/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4698379
- **Type**: conference
- **Published**: 30 Nov.-4 
- **Authors**: Seungjune Jeon, Xinde Hu, B. V. K. Vijaya Kumar
- **PDF**: https://ieeexplore.ieee.org/document/4698379
- **Abstract**: Concatenations of inner low-density parity-check (LDPC) codes and outer Reed-Solomon (RS) codes were evaluated in magnetic recording channel models by simulations using field programmable gate arrays (FPGAs). Fixed inner LDPC codes were used and the optimal code rates for the outer RS code were obtained. It is observed that the outer RS codes do not always improve sector error rates for a fixed user bit density. The effect of various parameters on the sector error rates was evaluated and discussed.

## A Two-Stage Iterative Decoding of LDPC Codes for Lowering Error Floors

- **Status**: ✅
- **Reason**: 트랩핑셋 깨는 2단 반복 디코딩으로 error floor 개선, 이식 가능 디코더 기법(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4697990
- **Type**: conference
- **Published**: 30 Nov.-4 
- **Authors**: Jingyu Kang, Li Zhang, Zhi Ding +1
- **PDF**: https://ieeexplore.ieee.org/document/4697990
- **Abstract**: In iterative decoding of LDPC codes, trapping sets often lead to high error floors. In this work, we propose a two-stage iterative decoding to break trapping sets. Simulation results show that the error floor performance can be significantly improved with this decoding scheme.

## Protograph E²RC Codes

- **Status**: ✅
- **Reason**: protograph 기반 rate-compatible punctured 코드 구성 + 고속 디코더 — 바이너리 코드설계 기법(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4697996
- **Type**: conference
- **Published**: 30 Nov.-4 
- **Authors**: Cuizhu Shi, Aditya Ramamoorthy
- **PDF**: https://ieeexplore.ieee.org/document/4697996
- **Abstract**: We propose a construction of rate-compatible punctured codes based on protographs that have a special E2RC structure in their parity part (E2RC codes were introduced in Kim, Ramamoorthy and McLaughlin '06) . The protograph representation of these codes facilitates their asymptotic performance analysis and allows the implementation of high speed decoders. The construction process starts with a good high rate protograph. The protographs of lower rate codes are derived from the higher rate protographs via the process of check-splitting. The check-splitting is done in a specific manner so that the parity nodes in the protograph have the special E2RC structure. We also present additional design rules that ensure that the gap to capacity remains low across the range of rates. Using our approach we exhibit protographs that have a gap of at most 0.27 dB to capacity across the range of rates 1/2 to 8/9. These conclusions are supported by our simulation results. Our work, therefore presents a systematic method for the design of E2RC-like codes.

## Clustering of Cycles and Construction of LDPC Codes

- **Status**: ✅
- **Reason**: 사이클 클러스터링으로 stopping set 회피하는 PEG 개선 — 바이너리 LDPC 코드설계 기법(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4697993
- **Type**: conference
- **Published**: 30 Nov.-4 
- **Authors**: Xiaofu Wu, Chunming Zhao, Xiaohu You +1
- **PDF**: https://ieeexplore.ieee.org/document/4697993
- **Abstract**: The clustering of cycles to form stopping sets are first observed by T. Tian and et al. As the determination of stopping sets of minimum size is NP-hard, we propose to consider clustering of cycles to avoid the stopping sets of small sizes. In particular, the clustering of two cycles are considered for an improved version of progressive edge-growth construction of LDPC codes.

## Enhanced Verification-Based Decoding for Packet-Based LDPC Codes over Wireless Channels

- **Status**: ✅
- **Reason**: verification-based decoding(EVA) BP 디코더 변형, 부호 비의존 BSC/GE; 디코더 알고리즘 이식 가능성 (C, 애매→in)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4698545
- **Type**: conference
- **Published**: 30 Nov.-4 
- **Authors**: Bin Zhu, Defeng Huang, Sven Nordholm
- **PDF**: https://ieeexplore.ieee.org/document/4698545
- **Abstract**: In this paper, we apply the enhanced verification-based decoding algorithm (EVA) for packet-based LDPC codes over wireless channels. Compared with the verification algorithm (VA) in the literature, the EVA algorithm enhances the verification condition thereby reducing the likelihood of false verification. The wireless channels in simulations are modeled by binary symmetric channel (BSC) and Gilbert-Elliott (GE) channel. The numerical results indicate the proposed algorithm gives a superior performance but with only moderate computation increase compared with VA. For example, when the bit error probability is less than 10-3 in bad state of GE channel, the EVA reduces the frame error rate (FER) by one order with less than 35% complexity increase compared with VA.

## Lowering LDPC Error Floors by Postprocessing

- **Status**: ✅
- **Reason**: absorbing set 기반 error floor 저감 postprocessing 디코더 + HW emulation — 이식 가능 디코더/error floor 기법(C/E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4698365
- **Type**: conference
- **Published**: 30 Nov.-4 
- **Authors**: Zhengya Zhang, Lara Dolecek, Borivoje Nikolic +2
- **PDF**: https://ieeexplore.ieee.org/document/4698365
- **Abstract**: A class of combinatorial structures, called absorbing sets, strongly influences the performance of low-density parity-check (LDPC) decoders at low error rates. Past experiments have shown that a class of (8,8) absorbing sets determines the error floor performance of the (2048,1723) Reed-Solomon based LDPC code (RS-LDPC). A postprocessing approach is formulated to exploit the structure of the absorbing set by biasing the reliabilities of selected messages in a message-passing decoder. The approach converges quickly and can be efficiently implemented with minimal overhead. Hardware emulation of the decoder with postprocessing shows more than two orders of magnitude improvement in the very low bit error rate performance and error- floor-free operation below a BER of 10-12.

## Fast Identification of Error-Prone Patterns for LDPC Codes under Message Passing Decoding

- **Status**: ✅
- **Reason**: ACE 기반 error-prone 패턴 식별+비트레벨 매핑으로 error floor 개선, 코드설계/디코더 이식 가능(C/E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4697991
- **Type**: conference
- **Published**: 30 Nov.-4 
- **Authors**: Jing Lei, Wen Gao
- **PDF**: https://ieeexplore.ieee.org/document/4697991
- **Abstract**: Although density evolution accurately predicts the asymptotic performance of LDPC codes, it provides limited information for codes of short or moderate block length. For this reason, combinatorial methods have been employed to analyze the performance of finite-length LDPC codes under message passing decoding. The error floor phenomenon is a key issue of finite-length effects, which is caused largely by poorly connected subgraphs residing in the LPDC codes structure. Because of the unequal noise immunity of different bit levels, error floors become more pronounced for LDPC-coded high-order modulation. Nevertheless, the enumeration of error-prone patterns that lead to error floors has been proven to be NP-hard, which motivates us to find substitute metrics with manageable complexity. Considering trapping sets always comprise loops of low extrinsic message degree (EMD) and the connectivity of a loop with the residual graph can be characterized by its approximate EMD (ACE), in this paper we propose a fast method to identify loops with low ACE for a given code. In light of this, the vulnerable variable nodes residing on low-ACE loops are judiciously mapped to bit levels benefitting from stronger error protection. As a result, the error floor can be significantly improved at the cost of a minor increase of hardware complexity.

## Efficient encoding for dual-diagonal structured LDPC codes based on parity bit prediction and correction

- **Status**: ✅
- **Reason**: D. dual-diagonal LDPC 인코딩 병렬화 HW(parity bit prediction/correction)—구조적 LDPC 인코더 기법 이식 가능
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:4746353
- **Type**: conference
- **Published**: 30 Nov.-3 
- **Authors**: Chia-Yu Lin, Chih-Chun Wei, Mong-Kai Ku
- **PDF**: https://ieeexplore.ieee.org/document/4746353
- **Abstract**: In this paper, an efficient encoding scheme for dual-diagonal structured LDPC codes is proposed. Our encoding algorithm employs parity bit prediction and correction to break up the data dependency within the encoding process. The encoder can achieve higher level of parallelism and better hardware utilization. The number of required clock cycles for encoding one codeword can be reduced to achieve higher throughput performance. The proposed scheme can be directly applied to IEEE 802.11n and 802.16e dual-diagonal codes without any matrix modification. A low-complexity encoder architecture is proposed and implemented to verify these characteristics. Results show that the proposed architecture outperforms conventional works in terms of throughput and throughput/area ratio.

## Low-complexity shift-LDPC decoder for high-speed communication systems

- **Status**: ✅
- **Reason**: C/D. single minimum decoding, 비균일 양자화, shifting 구조로 HW/메모리 절감—NAND 디코더에 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4746350
- **Type**: conference
- **Published**: 30 Nov.-3 
- **Authors**: Chuan Zhang, Li Li, Jun Lin +1
- **PDF**: https://ieeexplore.ieee.org/document/4746350
- **Abstract**: In this paper, an efficient high-speed low-density parity-check (LDPC) decoder is presented. Single minimum decoding and non-uniform quantization schemes are explored to reduce the complexity of computation core and the memory requirement. Shifting structure is incorporated to significantly reduce the routing complexity of the LDPC decoder. The implementation of an 8192-bit LDPC decoder demonstrates that about 63.3% hardware reduction can be achieved compared with the state-of-the-art design for high speed LDPC decoding. It is also shown that, using SMIC 0.18 mum CMOS technology, 5.4 Gb/s decoding throughput can be obtained at 15 decoding iterations.

## Efficient decoder design for high-throughput LDPC decoding

- **Status**: ✅
- **Reason**: D. matrix permutation으로 QC-LDPC를 shift구조 변환 + column-layered min-sum HW 구현—이식 가능
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:4746351
- **Type**: conference
- **Published**: 30 Nov.-3 
- **Authors**: Zhiqiang Cui, Zhongfeng Wang, Xinmiao Zhang +1
- **PDF**: https://ieeexplore.ieee.org/document/4746351
- **Abstract**: In this paper, a matrix permutation scheme is proposed to convert a generic QC-LDPC code to a shift-structured LDPC code. Thus, efficient VLSI architectures can be developed to achieve very high decoding throughput with low hardware complexity. Furthermore, novel implementation schemes for min-sum algorithm based column-layered decoding are presented. The proposed approaches provide very efficient ways for high-speed decoder design of generic QC-LDPC codes.

## Construction of short-length LDPC codes with low error floor

- **Status**: ✅
- **Reason**: E. ACSE 신규 메트릭으로 stopping/trapping set 제거하는 단길이 저 error-floor 코드 구성—바이너리 LDPC 코드설계 기법
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4746396
- **Type**: conference
- **Published**: 30 Nov.-3 
- **Authors**: X. Zheng, F. C. M. Lau, C. K. Tse +1
- **PDF**: https://ieeexplore.ieee.org/document/4746396
- **Abstract**: It has been known that stopping sets and trapping sets are the main contributors to error floors exhibited by short-length low-density parity-check (LDPC) codes. In this work, a new metric called ldquoapproximate cycle set extrinsic message degree (ACSE)rdquo is defined to help removing stopping sets with small size and bad trapping sets. Based on the new metric, we propose a code-construction algorithm that produces LDPC codes with very low error floors. Finally, we compare the error rates between codes produced by the proposed algorithm and MacKay code.

## Flexible LDPC decoder architecture for high-throughput applications

- **Status**: ✅
- **Reason**: D. flexible high-throughput LDPC 디코더 HW 아키텍처(block-parallel layered, 메모리 뱅킹)—NAND 디코더에 이식 가능
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:4745956
- **Type**: conference
- **Published**: 30 Nov.-3 
- **Authors**: Sangmin Kim, Gerald E. Sobelman, Hanho Lee
- **PDF**: https://ieeexplore.ieee.org/document/4745956
- **Abstract**: In this paper, we present a flexible high-throughput LDPC decoder architecture that can support different code rates and block sizes in wireless applications such as IEEE 802.11n, IEEE 802.16e, and IEEE 802.15.3c standards. Several flexible LDPC decoders have been presented in the literature but their throughput (less than 640 Mbps) is limited due to block-serial scheduling of the decoding computations. The proposed architecture is based on a block-parallel scheduling scheme using a layered decoding method. To achieve higher throughput, check node-based processes are implemented in a fully parallel architecture and the memory is partitioned into a number of banks. System flexibility is achieved by allowing the check node-based units and the memory banks to be configured according to the code rate and block size of the LDPC code of interest.

## Dynamically reconfigurable architecture for multi-rate compatible regular LDPC decoding

- **Status**: ✅
- **Reason**: D. multi-rate compatible 1st-2nd minimum searching unit 등 재구성 가능 디코더 HW 기법—이식 가능
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:4746121
- **Type**: conference
- **Published**: 30 Nov.-3 
- **Authors**: Akiyuki Nagashima, Yuta Imai, Nozomu Togawa +2
- **PDF**: https://ieeexplore.ieee.org/document/4746121
- **Abstract**: Recently a demand for high-speed wireless network service on mobile devices is rapidly increasing. Error correcting codes are used to enhance network communication quality. Particularly, LDPC (low density parity check) codes show high throughput and achieve information rates very close to the Shannon limit. In this paper, we propose a dynamically reconfigurable architecture for multi-rate compatible regular LDPC decoding. Our proposed decoder deals with multi-rate codes by introducing a multi-rate compatible 1st-2nd minimum searching unit. The proposed decoder shows the better throughput over the wide range of S/N ratio compared to conventional rate-fixed LDPC decoders.

## An IP generator for quasi-cyclic LDPC convolutional code decoders

- **Status**: ✅
- **Reason**: D. QC-LDPC convolutional 디코더 IP 생성기/저복잡도 디코더 HW—QC-LDPC HW 기법 이식 가능
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:4746354
- **Type**: conference
- **Published**: 30 Nov.-3 
- **Authors**: Chun-Hao Liao, Jun-Wei Lin, Yen-Shuo Chang +3
- **PDF**: https://ieeexplore.ieee.org/document/4746354
- **Abstract**: In this paper, the design and implementation of a high performance soft LDPC-CC decoder IP generator is presented. The proposed design is based on quasi-cyclic (QC) low-density parity-check matrices. These matrices not only simplify decoder design but also require less memory storage. A special digital processor is proposed to reduce the critical path and enhance the throughput. In addition, we have designed an IP generator and associated user interface that can take specifications of three parameters: iteration number, memory length, and code rate. With this generator, high-performance LDPC-CC decoders conforming to the user’s specifications can be generated effortlessly.

## Generalized serial schedules for iterative decoding of LDPC codes

- **Status**: ✅
- **Reason**: LDPC serial 디코딩 스케줄(Tanner 그래프 서브그래프 분할)로 복잡도/성능 개선, lifted graph 적용 - 이식 가능 디코더 알고리즘(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4736667
- **Type**: conference
- **Published**: 3-5 Dec. 2
- **Authors**: Noam Presman, Eran Sharon, Simon Litsyn
- **PDF**: https://ieeexplore.ieee.org/document/4736667
- **Abstract**: Efficient serial decoding schedules for LDPC codes are described. The schedules are based on dividing the Tanner graph to sub-graphs. This yields an improvement in complexity and performance over the standard schedules. An application of the introduced schedules to decoding codes based on lifted graphs is described. An analysis based on density evolution is presented and is used to predict the behavior of different schedules.

## New methodologies for high level modeling and synthesis of low density parity check decoders

- **Status**: ✅
- **Reason**: D: LDPC 디코더 고수준 모델링·합성 방법론으로 HW 구현 기법 이식 가능
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:4803046
- **Type**: conference
- **Published**: 24-27 Dec.
- **Authors**: Syed Mahfuzul Aziz, Sunil Sharma
- **PDF**: https://ieeexplore.ieee.org/document/4803046
- **Abstract**: Low density parity check (LDPC) codes are the error-correcting codes which offer huge advantages in terms of coding gain, throughput and power dissipation. Error correction algorithms are often implemented in hardware in order to ensure fast processing. The hardware implementation of LDPC decoders using traditional hardware description language (HDL) based approach is a complex and time consuming task. This paper investigates new high level approaches to design and synthesis of LDPC decoders using a combination of high level modelling tools. It compares the high level design approaches to traditional HDL-based approach. The results presented in this paper provide some useful insight into the high level design approaches, their efficiencies and possible future directions with a view to develop an efficient design and modelling framework for hardware implementation of complex LDPC decoders.

## A low-complexity high-performance decoding algorithm for fixed-point LDPC decoders

- **Status**: ✅
- **Reason**: 고정소수점 min-sum 변형(CMVP) — 양자화 오차 개선 디코더, NAND ECC 고정소수점에 직접 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4813725
- **Type**: conference
- **Published**: 15-17 Dec.
- **Authors**: Jui-Hui Hung, Sau-Gee Chen
- **PDF**: https://ieeexplore.ieee.org/document/4813725
- **Abstract**: The bit-error-rate (BER) performance of an LDPC decoding algorithm will be seriously degraded when the algorithm is realized with fixed-point implementation in practical applications, due to the introduced quantization errors and rounding errors. To remedy the problem, this paper proposes an improved min-sum algorithm (MSA), called CMVP algorithm. It achieves better performances than the popular min-sum algorithm (MSA), under the condition of the same fixed-point precision. Besides, the hardware overhead of the new algorithm over conventional MSA is small. On the other hand, under the condition of comparable performances, MSA algorithm needs a higher fixed-point precision and hardware costs than the new CMVP algorithm, according to the simulations and hardware synthesis results. The new algorithm also works well in a wide range of code rates and code lengths.

## An effective multibit-flipping algorithm for LDPC decoding

- **Status**: ✅
- **Reason**: 새 BF 변형(Low-Correlation Multibit-flipping) 디코더 알고리즘 — 바이너리 LDPC BP/BF 개선, NAND 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4813653
- **Type**: conference
- **Published**: 15-17 Dec.
- **Authors**: Jui-Hui Hung, Sau-Gee Chen
- **PDF**: https://ieeexplore.ieee.org/document/4813653
- **Abstract**: For LDPC decoding, bit-flipping (BF) algorithms are much simpler than the min-sum algorithms (MSA). However, BF algorithms have the disadvantages of poorer performances and higher iteration counts than MSA. To increase the BF performances, this paper presents a novel BF algorithm, called Low-Correlation Multibit-flipping (LCMBF) algorithm, which flips more than one bit in each iteration. High performances are achieved by flipping those bits with low correlation as much as possible. As such, the chances of introducing additional error bits are greatly reduced. Overall, the proposed algorithm achieves better BER performances and requires less iteration numbers than conventional BF algorithms.

## Design, implementation and applications of low-complexity LDPC codes

- **Status**: ✅
- **Reason**: QC-LDPC 구성(BIBD/finite field)+error floor 개선+FPGA 인코더/디코더 메모리효율 구현, 코드설계E·HW D 이식 가능
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:4813651
- **Type**: conference
- **Published**: 15-17 Dec.
- **Authors**: B. Honary, B. M. Heravi, S. Kariyawasam +1
- **PDF**: https://ieeexplore.ieee.org/document/4813651
- **Abstract**: Structured LDPC codes enable low-complexity decoding as well as efficient implementation of encoder reducing the complexity downto the order of the number of parity-check bits. Construction of structured LDPC codes is based on combinatorial approaches such as Balanced-Incomplete Block-Design (BIBD) and Finite Fields to design quasi-cyclic LDPC (QC-LDPC) codes. Well designed QC-LDPC codes can perform as well as randomly constructed LDPC codes with iterative decoding based on belief propagation in terms of bit-error probability. It has been shown that QC-LDPC codes can achieve lower error floor than randomly constructed LDPC codes. Within this work, the design of Quasi-cyclic LDPC codes for a range of practical applications is discussed which includes construction of variable-rate large-block-length LDPC codes for DVB-S2 and DVB-T2 applications and adaptive short-block-length LDPC codes for HF applications. Moreover, efficient implementation of QC-LDPC decoder/encoder for FPGA devices which reduces memory requirements is presented.

## Three-Level Error Control Coding for Dependable Solid-State Drives

- **Status**: ✅
- **Reason**: SSD용 3단계 ECC(스토리지 ECC 일반, 카테고리B)이나 BCH 기반이므로 Phase3 재검토 필요 — 애매하여 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4725307
- **Type**: conference
- **Published**: 15-17 Dec.
- **Authors**: Haruhiko Kaneko, Takuya Matsuzaka, Eiji Fujiwara
- **PDF**: https://ieeexplore.ieee.org/document/4725307
- **Abstract**: Solid-state drive (SSD) has advantages over hard-disk drive (HDD) in terms of power consumption, random access time, and resilience to shock and vibration. Large capacity SSD usually requires high-density multi-level cell flash memory fabricated with deep-submicron process. High-density memory chips, however, are vulnerable to soft errors caused by, for example, fluctuations of gate voltage and charge level in the floating gate. This paper proposes a hierarchical three-level error control coding suitable for the dependable SSD. The proposed coding is capable of correcting multiple random bit errors, as well as of recovering from single chip failures. Evaluation shows that the proposed coding scheme provides strong error correction capability. For example, bit error rate (BER) of the SSD is reduced from 1.08 × 10-4 to 2.44 × 10-19 by using the proposed coding, that is, using two BCH codes with different error correction capabilities for the first and the second levels, and the simple parity-check code for the third level. Extra one spare memory chip in the SSD improves mean time to data loss (MTTDL) from 13 years to 34 years.

## Modified BP Decoding Algorithms Combined with GA for Low-Density Parity Check Codes

- **Status**: ✅
- **Reason**: C. BP+GA 결합 변형 디코더로 short/middle LDPC BER/FER 개선, 바이너리 LDPC BP 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4724676
- **Type**: conference
- **Published**: 13-17 Dec.
- **Authors**: Zerong Deng, Xingcheng Liu, Man Teng
- **PDF**: https://ieeexplore.ieee.org/document/4724676
- **Abstract**: In this paper we propose algorithms which combine Belief-propagation (BP) decoding algorithm with genetic algorithm (GA). The main idea is to improve the performance of traditional BP decoding algorithm by efficiently using the belief of variable nodes passing to check nodes. By considering the belief as genes, the proposed algorithms mainly employ the mutation operation in GA, and change the genes¿ amplitudes (either increase or decrease) when updating the check nodes¿ information. First, we explore that the marriage of the GA and BP decoding algorithm is reasonable. Three algorithms are proposed accordingly. Proposed algorithm I mutates chosen genes by amplitude enhancement, while proposed algorithm II by amplitude reduction. Finally, proposed algorithm III is a mixture of the former two. From computer simulation results, we show that for short and middle length LDPC codes, our proposed algorithms can improve both BER (bit error rate) and FER (frame error rate) performance over traditional BP decoding algorithm, with slight modification of traditional BP decoding algorithm and little increase of computation complexity.
