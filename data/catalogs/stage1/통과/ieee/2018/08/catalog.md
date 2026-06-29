# IEEE Xplore — 2018-08 (1차선별 통과)


## Analytical Lower Bound on the Lifting Degree of Multiple-Edge QC-LDPC Codes With Girth 6

- **Status**: ✅
- **Reason**: multiple-edge QC-LDPC girth-6 lifting degree 하한 및 구성기법 - 바이너리 QC-LDPC 신규 코드설계(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8368304
- **Type**: journal
- **Published**: Aug. 2018
- **Authors**: Mohammad-Reza Sadeghi, Farzane Amirzade
- **PDF**: https://ieeexplore.ieee.org/document/8368304
- **Abstract**: Multiple-edge protographs have some advantages over single-edge protographs, such as potentially having larger minimum Hamming distance. However, most of results in the literature are related to the construction of single-edge quasi-cyclic low-density parity-check codes (QC-LDPC) codes and little research has been done for the construction of multiple-edge QC-LDPC codes. In this letter, for the first time, necessary and sufficient conditions for the exponent matrices to have multiple-edge QC-LDPC codes with girth 6 are provided. As a consequence of this letter, a lower bound on the lifting degree of regular and irregular multiple-edge QC-LDPC codes with girth 6 is derived. We also present QC-LDPC codes whose lifting degrees meet our proposed lower bound. These codes have shorter lengths compared with single-edge QC-LDPC codes. Another contribution of this letter is presenting a technique to reduce the size of the search space to find these codes.

## Comments on “Edge-Based Dynamic Scheduling for Belief-Propagation Decoding of LDPC Codes”

- **Status**: ✅
- **Reason**: BP 디코딩의 edge-based dynamic scheduling 임계값 최적화 코멘트, 바이너리 LDPC 디코더 스케줄링 기법(C) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8214239
- **Type**: journal
- **Published**: Aug. 2018
- **Authors**: Qiyou Xie
- **PDF**: https://ieeexplore.ieee.org/document/8214239
- **Abstract**: In this paper, we provide comments on the recent paper by Aslam et al. that proposed two low-complexity edge-based scheduling schemes for belief-propagation (BP) decoding of low-density parity-check (LDPC) codes. In their schemes, the check-node reliability threshold ( ${\mathcal {T}}$ ) is important to select the updating edges. However, it is found that the selected value of  ${\mathcal {T}}$  in the above literature is not optimal. In this comment, we present a method that leads to a better choice of  ${\mathcal {T}}$ .

## Dispersed Array LDPC Codes and Decoder Architecture for NAND Flash Memory

- **Status**: ✅
- **Reason**: NAND flash용 Dispersed Array QC-LDPC 코드 구성 및 디코더 아키텍처(CBSD, ASIC), 직접 적용 대상(A/D/E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8207629
- **Type**: journal
- **Published**: Aug. 2018
- **Authors**: Wei Shao, Jin Sha, Chuan Zhang
- **PDF**: https://ieeexplore.ieee.org/document/8207629
- **Abstract**: Quasi-cyclic (QC) low-density parity-check (LDPC) codes have become popular in NAND flash memories, owing to their excellent error correction performance and hardware-friendly structures. However, the large scale of barrel shifters result in prohibitive routing complexity. Array LDPC code is a kind of highly structured QC-LDPC code, which provides a good balance of performance, complexity, and throughput. In this brief, a construction method of dispersed array LDPC (DA-LDPC) codes based on an array square is proposed. DA-LDPC codes not only benefit from the array property but also a hybrid and efficient storage architecture due to their stair-like structure. For NAND flash applications, the code construction and decoder architecture of a (18300, 16470) DA-LDPC code is illustrated in this brief, where a two-level decision of LDPC decoding strategy is employed. The numerical results based on an FPGA emulation platform have shown that the error floor of the (18300, 16470) DA-LDPC code is under 10-11 in term of bit error rate (BER). Thanks to the well-structured DA-LDPC codes, we can conveniently apply a column-based shuffle decoding (CBSD) algorithm for ease of implementation. The corresponding ASIC implementation results have proved that the decoder architecture of DA-LDPC codes can achieve higher normalized-throughput-gate-count-ratio (NTGR) compared to state-of-art works.

## Tree-Permutation-Matrix Based LDPC Codes

- **Status**: ✅
- **Reason**: Tree-permutation-matrix 기반 신규 LDPC 코드 구성, girth-8/10 사이클 제거 및 FPGA 구현(E/D) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8233210
- **Type**: journal
- **Published**: Aug. 2018
- **Authors**: Sheng Jiang, Fanlu Mo, Francis C. M. Lau +1
- **PDF**: https://ieeexplore.ieee.org/document/8233210
- **Abstract**: Low-density parity-check (LDPC) codes are normally categorized into random structure or regular structure. In this brief, we introduce a new type of LDPC codes which is of semi-regular style. The parity-check matrices of the new LDPC code type are composed of sub-matrices termed tree-permutation matrices (TPMs). These TPMs are “semi-regular” and are constructed in a systematic way. Using the 2 × 2 identity matrix and anti-diagonal matrix as an example, we illustrate how 2M × 2M TPMs are formed. During the formation of the 2M × 2M TPMs, we further apply the hill-climbing algorithm to avoid short cycles. Finally, we construct a girth-8 TPM-LDPC code with a base matrix of size 4 × 24 and a girth-10 TPM-LDPC code with a base matrix of size 3 ×10. We implement the TPM-LDPC decoders on an FPGA and compare the simulation results and decoder complexity with other LDPC codes.

## Connections Between Low-Weight Codewords and Cycles in Spatially Coupled LDPC Convolutional Codes

- **Status**: ✅
- **Reason**: SC-LDPC-CC의 저중량 코드워드-사이클 연결 분석 및 사이클 제거로 저중량 코드워드 회피 설계(E: 바이너리 사이클제거/error floor 코드설계)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8327849
- **Type**: journal
- **Published**: Aug. 2018
- **Authors**: Massimo Battaglioni, Marco Baldi, Giovanni Cancellieri
- **PDF**: https://ieeexplore.ieee.org/document/8327849
- **Abstract**: In this paper, time-invariant spatially coupled low-density parity-check convolutional codes (SC-LDPC-CCs) are considered, and the connections existing between their low-weight codewords and cycles in their Tanner graphs are studied. Using the polynomial representation of these codes, we show that parity-check matrices having columns with weight ≥2 can be analyzed considering a certain number of parity-check sub-matrices having regular columns with weight 2. These sub-matrices are associated to cycles in the code Tanner graph and define as many codes we denote as component codes. Based on this observation, we find that codewords of the main code can be expressed as combinations of codewords of the component codes. The design of codes free of codewords up to a certain weight is also addressed. We show that low-weight codewords in the main code can be avoided by removing some types of cycles in its Tanner graph. Our design approach is applied to some well-known ensembles of SC-LDPC-CCs to prove its effectiveness.

## Belief Propagation List Decoding of Polar Codes

- **Status**: ✅
- **Reason**: polar용 BP list 디코더지만 다중 permuted factor graph 병렬 BP+Euclidean 선택은 부호 비의존적 BP 기법으로 바이너리 LDPC BP에 이식 가능(예외 C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8396299
- **Type**: journal
- **Published**: Aug. 2018
- **Authors**: Ahmed Elkelesh, Moustafa Ebada, Sebastian Cammerer +1
- **PDF**: https://ieeexplore.ieee.org/document/8396299
- **Abstract**: We propose a belief propagation list (BPL) decoder with comparable performance to the successive cancellation list (SCL) decoder of polar codes, which already achieves the maximum likelihood (ML) bound of polar codes for sufficiently large list size L. The proposed decoder is composed of multiple parallel independent belief propagation (BP) decoders based on differently permuted polar code factor graphs. A list of possible transmitted codewords is generated and the one closest to the received vector, in terms of Euclidean distance, is picked. To the best of our knowledge, the proposed BPL decoder provides the best performance of plain polar codes under iterative decoding known so far. The proposed algorithm does not require any changes in the polar code structure itself, rendering the BPL into an alternative to the SCL decoder, equipped with a soft output capability enabling, e.g., iterative detection and decoding to further improve performance. Further benefits are the lower decoding latency than the SCL decoder and the possibility of high throughput implementations. Additionally, we show that a different selection strategy of frozen bit positions can further enhance the error-rate performance of the proposed decoder.

## Classification-Based Algorithm for Bit-Flipping Decoding of GLDPC Codes Over AWGN Channels

- **Status**: ✅
- **Reason**: GLDPC용 개선 비트플리핑 디코더(분류단계+보조비트로 trapping set 완화) - 이식 가능 BP/BF 디코더 알고리즘(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8364571
- **Type**: journal
- **Published**: Aug. 2018
- **Authors**: Sherif Elsanadily, Ashraf Mahran, Osama Elghandour
- **PDF**: https://ieeexplore.ieee.org/document/8364571
- **Abstract**: In this letter, an improved bit-flipping (BF) decoder for generalized LDPC over AWGN channels is proposed. It takes the advantage of the fast BF decoding with only initial help from the channel soft information by introducing a classification step at first. Second, it adds an auxiliary bit in messages between the bipartite graph nodes as a tool for increasing the decision reliability and improving the performance. The reliability is presented as a tool for diminishing the effect of the generated trapping sets. The proposed classification threshold is mathematically derived, and the algorithm is revealed to surpass the various BF algorithms concerning the bit error rate performance.

## The Probabilistic Finite Alphabet Iterative Decoder for Low-Density Parity-Check Codes

- **Status**: ✅
- **Reason**: C: 확률적 유한알파벳 반복디코더(PFAID) — 저비트 양자화로 MS 능가, HW 오버헤드 없는 이식 가능 디코더
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8623923
- **Type**: conference
- **Published**: 5-8 Aug. 2
- **Authors**: Khoa Le, Fakhreddine Ghaffari, David Declercq
- **PDF**: https://ieeexplore.ieee.org/document/8623923
- **Abstract**: This paper proposes a new concept of applying the Non-Surjective Finite Alphabet Iterative Decoder (NS-FAID) for the Low-Density Parity-Check (LDPC) decoding. Differently from the NS-FAID which applies a fixed nonlinear function by using a fixed Look-Up-Table (LUT) on the variable node messages, the proposed method, called Probabilistic FAID (PFAID), uses more than one LUTs in a probabilistic way. By using the density evolution, we show that this method provides a significant improvement in performance compared to the NS-FAID and the traditional MS. The advantage of PFAID is shown by the fact that, a PFAID with low message quantization level can reach or even surpass the performance of the higher level quantization MS decoder. Furthermore, we show that PFAID can be efficiently implemented with no hardware overhead compared to MS or NSFAID with the same message quantization level. The hardware complexity analysis and decoding simulation performance are provided as superiority evidences of PFAID over the referenced benchmarks.

## On the use of Probabilistic Parallel Bit-Flipping decoder for the storage systems

- **Status**: ✅
- **Reason**: C/D: 스토리지용 비신드롬 병렬 비트플립(NS-PPBF) 디코더+HW 아키텍처, 고율 장블록 메모리 코드 대상 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8623848
- **Type**: conference
- **Published**: 5-8 Aug. 2
- **Authors**: Khoa Le, Fakhreddine Ghaffari, David Declercq
- **PDF**: https://ieeexplore.ieee.org/document/8623848
- **Abstract**: The soft-decision Low-Density Parity-Check (LDPC) decoders have been applied in several storage systems thanks to their powerful error correction capability. However, these systems may suffer a long read latency since the soft-decision decoders require an intensive computations as well as a long sensing time for the soft-information before decoding. In this paper, we modify the recent-introduced Probabilistic Parallel Bit-Flipping (PPBF) LDPC decoder, to use on the storage systems in replacing the soft decision decoders, to improve the memory reading speed. The modified decoder is named Non-Syndrome Probabilistic Parallel Bit-Flipping (NS-PPBF). A special flipping mechanism is introduced such that the decoder can stop flipping without requiring the syndrome check results, which helps significantly improve the decoding frequency. We provide also the hardware architecture to implement NS-PPBF on the LDPC code used on the memory systems, which are usually very long block length with very high rate. The advantages of using NS-PPBF decoder in terms of error correction and decoding throughput are confirmed by the simulating decoding performance and the hardware synthesis.

## Dynamics of ML Approaching Randomized Decoders on Graphs with Cycles

- **Status**: ✅
- **Reason**: C: 사이클 그래프상 ML 근접 랜덤화 디코더 동역학 — BP에 이식 가능한 디코더 알고리즘 기여, 애매하나 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8624093
- **Type**: conference
- **Published**: 5-8 Aug. 2
- **Authors**: Saied Hemati
- **PDF**: https://ieeexplore.ieee.org/document/8624093
- **Abstract**: Randomized channel decoders are promising candidates for approaching maximum-likelihood (ML) decoding using low-complexity decoders when decoding latency is not a concern. This paper is focused on the dynamics of randomized decoders and divides these decoders into statically and dynamically randomized decoders. It is shown that some statically randomized decoders are ML achieving. For dynamically randomized channel decoders that are defined on graphs with cycles, it is shown that randomness can alleviate the impact of cycles.

## Memory-Centric Flooded LDPC Decoder Architecture Using Non-surjective Finite Alphabet Iterative Decoding

- **Status**: ✅
- **Reason**: NS-FAID 기반 flooded LDPC 디코더 아키텍처, 메시지 저장 압축+FPGA - 이식 가능 디코더(C)+HW(D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8491802
- **Type**: conference
- **Published**: 29-31 Aug.
- **Authors**: Oana Boncalo, Alexandru Amaricai, Sergiu Nimara
- **PDF**: https://ieeexplore.ieee.org/document/8491802
- **Abstract**: Non-Surjective Finite Alphabet Iterative Decoding (NS-FAID) represents an LDPC decoding algorithm that uses reduced message storage, with similar or improved error correction performance with respect to Min-Sum. In this paper, we employ NS-FAID compression tables for a memory-centric flooded LDPC decoding architecture. Due to the approximate message storage, improved memory footprint and overall cost is obtained using the NS-FAID approach. We present FPGA synthesis results, in terms of LUT-FF pairs used, working frequency and throughput, as well as Throughput to Area Ratio (TAR). The estimates indicate that employing NS-FAID compression tables yield improvements between 25% and 110% in TAR with respect to the baseline Min-Sum decoder.

## Enhanced LDPC Based Differential Iteration Decoding Scheme for PDM 16-QAM Coherent Optical Communication Systems

- **Status**: ✅
- **Reason**: LDPC 기반 differential iteration decoding 기법 - 새 반복 디코딩 변형 가능성, 애매하여 in으로 살림(Phase3 재검토)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8699782
- **Type**: conference
- **Published**: 29 July-3 
- **Authors**: Wenxiang Cao, Jing He, Zhihua Zhou
- **PDF**: https://ieeexplore.ieee.org/document/8699782
- **Abstract**: An enhanced LDPC based differential iteration decoding scheme is applied in 400-Gb/s PDM 16-QAM coherent optical communication systems. The simulation results show that, the system performance can be greatly improved by using the proposed method.

## Efficient Construction for QC-LDPC Convolutional Codes with Periodic Bit-Filling

- **Status**: ✅
- **Reason**: QC-LDPC-C 구성에서 length-4 사이클 제거 periodic bit-filling 신규 코드설계 기법(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8542328
- **Type**: conference
- **Published**: 18-20 Aug.
- **Authors**: Ming Zhao, Zhipeng Liu, Ling Zhao
- **PDF**: https://ieeexplore.ieee.org/document/8542328
- **Abstract**: QC-LDPC-C (Quasi-Cyclic Low Density Parity-Check Convolutional) codes are with low encoding and decoding complexity and can achieve decoding performance approaching the Shannon limit. However, the construction of the parity check matrices need to be free of the length-4 cycles, and the computational complexity of direct construction will increase exponentially without considering the characteristics of the matrices. The construction for QC-LDPC-C codes with periodic bit-filling method is proposed. With the periodicity of the base check matrix, the proposed method firstly fills the deterministic submatrices to realize fast encoding; then it avoids all possible length-4 cycles by periodic filling in the construction of random submatrices. Thus the base check matrix without cycles of length-4 can be obtained, and the girth of expanded check matrix is at least 6. LDPC-C codes with different parameters are used to compare with the constructed QC-LDPC codes. Experimental results show that the codes constructed with proposed method can achieve better performance and lower encoding and decoding complexity.

## Sequential Scheduling for Belief-Propagation Demodulation of Rate Compatible Modulation

- **Status**: ✅
- **Reason**: GS-BP/BS-RBP 순차 스케줄링 BP 수렴가속 기법 — 부호 비의존적 메시지패싱 스케줄링, 카테고리 C 이식 가능(애매시 in)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8641191
- **Type**: conference
- **Published**: 16-18 Aug.
- **Authors**: Huilian Zhang, Shaoping Chen
- **PDF**: https://ieeexplore.ieee.org/document/8641191
- **Abstract**: In this paper, two sequential scheduling (SS) algorithms, group-shuffled BP (GS-BP) and bit-to-symbol residual BP (BS-RBP), are proposed to accelerate the convergence speed of the demodulation of rate compatible modulation (RCM). Unlike the conventional BP demodulation that works in a parallel or flooding manner, the proposed schemes work in serial manner. Since the proposed schemes may make full use of the latest messages available in current iteration, a faster convergence rate and a lower bit error rtae (BER) may be achieved. Simulations show that the proposed schemes can effectively accelerate the convergence speed of RCM demodulation and improve the bit error rate (BER) performance.

## Piggybacking Belief Propagation Decoding for Rateless Codes Based on RA Structure

- **Status**: ✅
- **Reason**: RA구조 rateless용 Piggybacking BP 디코더+syndrome 기반 정지기준 — 부호 비의존적 BP 개선, 카테고리 C 이식 가능(애매시 in)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8641154
- **Type**: conference
- **Published**: 16-18 Aug.
- **Authors**: Rong Sun, Meng Zhao, Jingwei Liu +3
- **PDF**: https://ieeexplore.ieee.org/document/8641154
- **Abstract**: In this paper, a new Belief Propagation (BP) decoding algorithm named Piggybacking Belief Propagation (PBP) decoding algorithm is proposed for rateless codes based on repeat-accumulate (RA) structure over AWGN channel. The "piggybacking" characteristic of the proposed algorithm is transmitting the Log-Likelihood Ratio (LLR) results calculated from the previous decode attempt to the new decoding process after receiving more information from the channel. Moreover, the proposed algorithm introduces a new stopping criterion to stop the decoding attempt when it is almost impossible to succeed. The stopping criterion is based on the weight change ratio of syndrome. The simulation results show that, compared with the traditional BP decoding algorithm, the proposed algorithm has lower decoding overhead and the a reduced decoding delay.

## An Improved Belief Propagation Algorithm Based on Exponential Model

- **Status**: ✅
- **Reason**: LDPC BP에서 tanh 지수모델 근사 및 비선형 연산 단순화로 min-sum류 디코더 복잡도 저감 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8652337
- **Type**: conference
- **Published**: 12-16 Aug.
- **Authors**: Yuhuan Wang, Hang Yin, Zhanxin Yang +1
- **PDF**: https://ieeexplore.ieee.org/document/8652337
- **Abstract**: This paper proposes a new belief propagation algorithm to reduce the computational complexity of Low Density Parity Check codes. In the iterative process of the proposed algorithm, an exponential model is adopted to segmental approximate the hyperbolic tangent function. In addition, two kinds of nonlinear operations are simplified into one nonlinear operation. Simulations reveal that this proposed decoding algorithm can reduce the computational complexity of decoding algorithm with a minimal loss of performance.
