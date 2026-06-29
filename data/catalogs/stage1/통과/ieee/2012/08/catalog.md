# IEEE Xplore — 2012-08 (1차선별 통과)


## A PEG Construction of Finite-Length LDPC Codes with Low Error Floor

- **Status**: ✅
- **Reason**: PEG 알고리즘 개선으로 유한길이 LDPC error floor/trapping set 저감 - 이식 가능 코드 설계(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6211373
- **Type**: journal
- **Published**: August 201
- **Authors**: Sina Khazraie, Reza Asvadi, Amir H. Banihashemi
- **PDF**: https://ieeexplore.ieee.org/document/6211373
- **Abstract**: The progressive-edge-growth (PEG) algorithm of Hu et al. is modified to improve the error floor performance of the constructed low-density parity-check (LDPC) codes. To improve the error floor, the original PEG algorithm is equipped with an efficient algorithm to find the dominant elementary trapping sets (ETS's) that are added to the Tanner graph of the under-construction code by the addition of each variable node and its adjacent edges. The aim is to select the edges, among the candidates available at each step of the original PEG algorithm, that prevent the creation of dominant ETS's. The proposed method is applicable to both regular and irregular variable node degree distributions. Simulation results are presented to demonstrate the superior ETS distribution and error floor performance of the constructed codes compared to similar codes constructed by the original and other modifications of the PEG algorithm.

## Design of LDPC Codes with Strong Universal Properties

- **Status**: ✅
- **Reason**: 정보결합 bound+가우시안 근사로 universal LDPC 코드 설계법 제안(E: 코드 설계, 바이너리 LDPC)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6220292
- **Type**: journal
- **Published**: August 201
- **Authors**: Chao Zheng, Ali Sanaei, Masoud Ardakani
- **PDF**: https://ieeexplore.ieee.org/document/6220292
- **Abstract**: Using the information combining bounds together with a Gaussian approximation, a method for finding low-density parity-check codes with strong universal properties that achieve a high percentage of the channel capacity is proposed. For a given channel capacity C, it is proven that the designed codes satisfy the stability condition for all channels with capacity C. Our experimental results also verify the strong universal properties of codes designed by the proposed method.

## Dithered Belief Propagation Decoding

- **Status**: ✅
- **Reason**: dithered BP 디코딩으로 error floor 저감, 최소 HW 오버헤드 - 이식 가능 디코더 알고리즘(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6199939
- **Type**: journal
- **Published**: August 201
- **Authors**: Francois Leduc-Primeau, Saied Hemati, Shie Mannor +1
- **PDF**: https://ieeexplore.ieee.org/document/6199939
- **Abstract**: We introduce two dithered belief propagation decoding algorithms to lower the error floor with a minimal hardware overhead. One of the algorithms can additionally improve the decoding performance in the waterfall region using a large iteration limit but with a negligible increase in the average time complexity.

## Verification Decoding of High-Rate LDPC Codes With Applications in Compressed Sensing

- **Status**: ✅
- **Reason**: 고율 바이너리 LDPC verification/MP 디코딩 밀도진화·스케일링 분석(C: 디코더 기법); 압축센싱은 부수 확장이나 바이너리 LDPC BEC/q-SC 디코더 분석 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6205393
- **Type**: journal
- **Published**: Aug. 2012
- **Authors**: Fan Zhang, Henry D. Pfister
- **PDF**: https://ieeexplore.ieee.org/document/6205393
- **Abstract**: This paper considers the performance of (j, k)-regular low-density parity-check (LDPC) codes with message-passing (MP) decoding algorithms in the high-rate regime. In particular, we derive the high-rate scaling law for MP decoding of LDPC codes on the binary erasure channel (BEC) and the q-ary symmetric channel (q-SC). For the BEC and a fixed j, the density evolution (DE) threshold of iterative decoding scales like Θ(k-1) and the critical stopping ratio scales like Θ(k-j/(j-2)). For the q-SC and a fixed j, the DE threshold of verification decoding depends on the details of the decoder and scales like Θ(k-1) for one decoder. Using the fact that coding over large finite alphabets is very similar to coding over the real numbers, the analysis of verification decoding is also extended to the compressed sensing (CS) of strictly sparse signals. A DE-based approach is used to analyze the CS systems with randomized-reconstruction guarantees. This leads to the result that strictly sparse signals can be reconstructed efficiently with high probability using a constant oversampling ratio (i.e., when the number of measurements scales linearly with the sparsity of the signal). A stopping-set-based approach is also used to get stronger (e.g., uniform-in-probability) reconstruction guarantees.

## Jointly Designed Architecture-Aware LDPC Convolutional Codes and Memory-Based Shuffled Decoder Architecture

- **Status**: ✅
- **Reason**: AA-LDPC-CC 구성+shuffled MPD 메모리기반 디코더 아키텍처(permutation network, 병렬화) VLSI 구현 — C/D/E 이식 가능 HW/디코더
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6195029
- **Type**: journal
- **Published**: Aug. 2012
- **Authors**: Yeong-Luh Ueng, Yu-Luen Wang, Li-Sheng Kan +2
- **PDF**: https://ieeexplore.ieee.org/document/6195029
- **Abstract**: In this paper, we jointly design architecture-aware (AA) low-density parity-check convolutional codes (LDPC-CCs) and the associated memory-based decoder architecture based on shuffled message-passing decoding (MPD). We propose a method for constructing AA-LDPC-CCs that can facilitate the design of a memory-based shuffled decoder using parallelization in both iteration and node dimensions. Through the use of shuffled MPD, the number of base processors and, hence, the decoder area is significantly reduced, since a fewer number of iterations is required in order to achieve a desired error performance. In addition, the use of memory instead of registers minimizes the implementation cost of each base processor. In the memory-based decoder, collisions in memory access can be avoided and the difficulty in exchanging information between iterations (processors) is overcome by using simple permutation networks. To demonstrate the feasibility of the proposed techniques, we constructed a time-varying (479, 3, 6) AA-LDPC-CC and implemented its associated shuffled decoder using a 90-nm CMOS process. This decoder comprises 11 processors, occupies an area of 5.36 , and achieves an information throughput of 1.025 Gbps at a clock frequency of 256.4 MHz based on post-layout results.

## Limited magnitude error locating parity check codes for flash memories

- **Status**: ✅
- **Reason**: NAND MLC 플래시의 limited-magnitude 비대칭 오류 특성에 맞춘 parity check code 신규 설계(저복잡도 인코딩/디코딩), 카테고리 A 직접
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6291949
- **Type**: conference
- **Published**: 5-8 Aug. 2
- **Authors**: Myeongwoon Jeon, Sungkyu Chung, Beomju Shin +1
- **PDF**: https://ieeexplore.ieee.org/document/6291949
- **Abstract**: NAND multi-level cell (MLC) flash memories are widely used due to low cost and high capacity. However the increased number of levels in MLC results in larger interference and errors. The errors in MLC flash memories tend to be asymmetric and with limited-magnitude. To take advantage of the characteristics, we propose limited-magnitude parity check codes, which can reduce errors more effectively. A key advantage of the proposed method is that it has low complexity for encoding and decoding. Another useful feature of the proposed method is that the code rate and the block size can be chosen almost continuously unlike conventional error correcting codes.

## Bayesian hypothesis test for sparse support recovery using belief propagation

- **Status**: ✅
- **Reason**: BP 기반 sparse support recovery 신규 알고리즘(BHT-BP)으로 메시지패싱/BP 개선 기법이 바이너리 LDPC BP에 이식 가능성 있어 애매-살림(C, Phase3 재검토)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6319731
- **Type**: conference
- **Published**: 5-8 Aug. 2
- **Authors**: Jaewook Kang, Heung-No Lee, Kiseon Kim
- **PDF**: https://ieeexplore.ieee.org/document/6319731
- **Abstract**: In this paper, we introduce a new support recovery algorithm from noisy measurements called Bayesian hypothesis test via belief propagation (BHT-BP). BHT-BP focuses on sparse support recovery rather than sparse signal estimation. The key idea behind BHT-BP is to detect the support set of a sparse vector using hypothesis test where the posterior densities used in the test are obtained by aid of belief propagation (BP). Since BP provides precise posterior information using the noise statistic, BHT-BP can recover the support with robustness against the measurement noise. In addition, BHT-BP has low computational cost compared to the other algorithms by the use of BP. We show the support recovery performance of BHT-BP on the parameters (N, M, K, SNR) and compare the performance of BHT-BP to OMP and Lasso via numerical results.

## Novel technique for scaling down LDPC code lengths in DVB-T2 standard

- **Status**: ✅
- **Reason**: LDPC 길이 축소+girth-4/저중량 회피, error floor 분석 — 코드설계(E) 이식 가능, 바이너리 LDPC
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6294713
- **Type**: conference
- **Published**: 30 July-1 
- **Authors**: Fatma A. Newagy, Salwa H. Elramly
- **PDF**: https://ieeexplore.ieee.org/document/6294713
- **Abstract**: The paper proposes an approach to scale-down the LDPC code length, thus saving memory and processing power, without significantly sacrificing the code robustness. the paper describes how to use specific Low Density Parity Check (LDPC) codes for Digital Video Broadcasting Terrestrial Second Generation DVB-T2. While the original LDPC codes are rather long 16200 bits and 64800 bits, we propose to reduce their size (about 3k instead of 16k). To reduce the encoder/decoder complexity, the scaled down LDPC codes based on DVB-T2 of length 16200 are proposed in this paper. Scaling the codes may lead to the problems of girth-4 and low weight codes. This paper analyzed the possible reasons leading to the problems, and proposed the optimum scaled down LDPC codes of DVB-T2 that avoid girth-4 and low weight codes. The simulation results in the AWGN channel show that for code rate ½ at BER = 10-5, LDPC DVB-T2_3240 requires only additional 0.5dB above that required by DVB-T2_16200 and the proposed scaled down code by 5 still has no error floor as well as the former codes in [10]. The impact of the paper is not restricted to DVB-T2 systems, but also to DVB-S2 and all future technologies which are to adopt LDPC.

## FPGA-based design and implementation of a multi-GBPS LDPC decoder

- **Status**: ✅
- **Reason**: (3,6)-regular LDPC FPGA 디코더, hybrid quantization+파이프라이닝+early termination, 16.9Gbps - 이식 가능 HW 아키텍처(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:6339191
- **Type**: conference
- **Published**: 29-31 Aug.
- **Authors**: Alexios Balatsoukas-Stimming, Apostolos Dollas
- **PDF**: https://ieeexplore.ieee.org/document/6339191
- **Abstract**: We design a very high speed LDPC code decoder architecture for (3,6)-regular codes by employing hybrid quantization, pipelining, and FPGA-specific optimizations. Our pipelined architecture fully addresses the decoder's significant I/O requirements, even when an early termination circuit is employed. The proposed decoder can achieve a throughput of up to 16.9 Gbps at an Eb/N0 of 3.5 dB using a code of length 1152, running at a clock speed of 153 MHz and performing a maximum of 10 decoding iterations, thus out-performing the state of the art by a significant margin. This design was fully implemented and tested on a Xilinx Virtex 5 XC5VLX110 FPGA. We also present an alternative, low-complexity design, which is able to achieve a throughput of up to 21.6 Gbps by sacrifing 0.75 dB in terms of Eb/N0.

## Generalised Quasi-Cyclic LDPC codes based on Progressive Edge Growth Techniques for block fading channels

- **Status**: ✅
- **Reason**: QC Root-Check LDPC의 새 PEG 기반 사이클 감소 패리티검사 행렬 설계 기법(E) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6328513
- **Type**: conference
- **Published**: 28-31 Aug.
- **Authors**: André G. D. Uchôa, Cornelius Healy, Rodrigo C. de Lamare +1
- **PDF**: https://ieeexplore.ieee.org/document/6328513
- **Abstract**: Generalised Quasi-Cyclic Root-Check LDPC codes based on Progressive Edge Growth (PEG) techniques for block-fading channels are proposed. The proposed Root-Check LDPC codes are suitable for channels under F= 3, 4 independent fadings per codeword which is a scenario that has not been previously considered. A generalised Quasi-Cyclic Root-Check structure is devised for F= 3, 4 independent fadings. The proposed PEG-based algorithm for generalised Quasi-Cyclic Root-Check LDPC codes takes into account the specific structure, and designs a parity-check matrix with a reduced number of cycles. The performance of the new codes is investigated in terms of the Frame Error Rate (FER). Numerical results show that the codes constructed by the proposed algorithm perform about 0.5dB from the theoretical limit.

## Knowledge-aided reweighted belief propagation decoding for regular and irregular LDPC codes with short blocks

- **Status**: ✅
- **Reason**: short cycle 지식 활용 reweighted BP(VFAP-BP) 새 메시지패싱 디코더(C), 바이너리 LDPC에 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6328515
- **Type**: conference
- **Published**: 28-31 Aug.
- **Authors**: Jingjing Liu, Rodrigo C. de Lamare
- **PDF**: https://ieeexplore.ieee.org/document/6328515
- **Abstract**: In this paper a new message passing algorithm, which takes advantage of both tree-based re-parameterization and the knowledge of short cycles, is introduced for the purpose of decoding LDPC codes with short block lengths. The proposed algorithm is called variable factor appearance probability belief propagation (VFAP-BP) algorithm and is suitable for wireless communications applications, where both good decoding performance and low-latency are expected. Our simulation results show that the VFAP-BP algorithm outperforms the standard BP algorithm and requires a significantly smaller number of iterations than existing algorithms when decoding both regular and irregular LDPC codes.

## A hybrid iterative decoder for LDPC codes

- **Status**: ✅
- **Reason**: min-sum BP에 erasure 반복 디코딩 결합한 새 하이브리드 디코더, error-floor 개선 기법(C) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6328514
- **Type**: conference
- **Published**: 28-31 Aug.
- **Authors**: W. P. S. Guimarães, J. S. Lemos-Neto, V. C. da Rocha
- **PDF**: https://ieeexplore.ieee.org/document/6328514
- **Abstract**: A hybrid decoder (HD) for LDPC codes in the presence of additive white Gaussian noise is proposed. This HD employs a min-sum belief propagation (BP) decoding to correct errors, combined with erasure iterative decoding. Whenever BP decoding fails, its output is modified and artificially created erasures are introduced. The proposed HD employs an overall reduced number of iterations and achieves a similar performance to that of traditional BP decoding schemes, especially in the error-floor region, with equivalent implementation complexity. Results of HD performance obtained by computer simulation are presented.

## New quasi-cyclic LDPC codes with girth at least eight based on Sidon sequences

- **Status**: ✅
- **Reason**: Sidon 수열 기반 girth>=8 QC-LDPC 신규 구성 — 바이너리 코드설계(E) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6325193
- **Type**: conference
- **Published**: 27-31 Aug.
- **Authors**: Guohua Zhang, Rong Sun, Xinmei Wang
- **PDF**: https://ieeexplore.ieee.org/document/6325193
- **Abstract**: A new family of quasi-cyclic low-density parity-check (LDPC) codes of girth at least eight is explicitly constructed from Sidon sequences. These codes can be encoded using simple shift-registers. Furthermore, for short to moderate lengths these quasi-cyclic codes perform close to random progressive edge-growth (PEG) LDPC codes in terms of bit-error probability and block-error probability, collectively.

## Adapted scheduling of QC-LDPC decoding for multistandard receivers

- **Status**: ✅
- **Reason**: QC-LDPC 디코딩 trellis 스케줄링으로 메모리 접근충돌 회피 HW 기법, 병렬 디코더 아키텍처 이식 가능(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:6325209
- **Type**: conference
- **Published**: 27-31 Aug.
- **Authors**: Jean Dion, Marie-Helene Hamon, Pierre Pénard +2
- **PDF**: https://ieeexplore.ieee.org/document/6325209
- **Abstract**: Wireless and PLC standards have to cope with noisy channels. The advanced FEC codes like LDPC and turbo codes are the most competitive ones. Multi-standards devices (such as mobile phones with cellular and WiFi) are becoming more and more attractive but raise the issue of duplicating hardware. Trellis decoding is a good solution to share material and to achieve good throughputs on FEC multi-standard decoders. Such a technique added with natural parallelism underlines access memory conflicts on the LDPC decoding process, which decreases the decoding performance. This paper presents an optimized trellis design to avoid these access conflicts with no loss in decoding performance.

## Generalized LDPC code with single-parity-check product constraints at super check nodes

- **Status**: ✅
- **Reason**: GLDPC super check node에 SPC-PC와 turbo iteration 적용한 신규 디코더/구성, 이식 검토 여지 있어 살림(C/E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6325220
- **Type**: conference
- **Published**: 27-31 Aug.
- **Authors**: Y. Min, F. C. M. Lau, C. K. Tse
- **PDF**: https://ieeexplore.ieee.org/document/6325220
- **Abstract**: Due to the more complex constraints, generalized low-density parity-check (GLDPC) codes can achieve better error performance but require much higher decoding complexities compared with the standard LDPC codes. In this paper, single-parity-check product-codes (SPC-PCs) are considered as the constituent codes in the super check nodes of a GLDPC code. Moreover, turbo iterations are used in decoding the SPC-PCs. The error performance and the decoder complexity of the proposed GLDPC code are compared with other LDPC code and GLDPC code.

## High-rate QC LDPC codes of short and moderate length with good girth profile

- **Status**: ✅
- **Reason**: 단/중길이 QC-LDPC의 girth profile 개선 신규 구성 알고리즘, 바이너리 코드설계(E) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6325217
- **Type**: conference
- **Published**: 27-31 Aug.
- **Authors**: Irina E. Bocharova, Florian Hug, Rolf Johannesson +1
- **PDF**: https://ieeexplore.ieee.org/document/6325217
- **Abstract**: Irregular QC LDPC codes with parity-check matrices having different degree distributions are studied. A new algorithm for finding regular and irregular QC LDPC codes with a good girth profile as well as a good sliding-window girth is presented. As examples, simulation results for QC LDPC codes with good girth profile, rate R=4/5, and lengths about 1000, 2000, and 4000, constructed from base matrices with proper degree distributions are given. Their simulated BER and FER performances for belief propagation decoding are compared with the best previously known irregular QC LDPC codes of the same rate and length. It is shown that the constructed codes outperform the best previously known codes of same rate and lengths.

## Adaptive decoding algorithms for LDPC codes with redundant check nodes

- **Status**: ✅
- **Reason**: Adaptive decoding로 active/silent check node 분류해 BP 복잡도-성능 트레이드오프 제시(C). 단 finite field/geometry 기반 코드라 비이진 가능성 있으나 디코더 기법은 바이너리 BP 이식 가능, 애매하여 in
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6325222
- **Type**: conference
- **Published**: 27-31 Aug.
- **Authors**: Kai Zhang, Haiqiang Chen, Xiao Ma
- **PDF**: https://ieeexplore.ieee.org/document/6325222
- **Abstract**: This paper is concerned with decoding of algebraic low-density parity-check (LDPC) codes that are constructed based on finite fields and finite geometries. The parity-check matrices of such codes usually have redundant rows. Equivalently, their Tanner graphs have redundant check nodes. Based on this property, we propose an adaptive decoding algorithm. In the adaptive decoding algorithm, all the check nodes are classified into active nodes and silent nodes according to certain criteria, and only active check nodes are involved in the iterative procession. That is, each variable node collects messages from active check nodes and passes the extrinsic messages to its active neighbors. Two approaches to select the active check nodes are presented. Simulation results show that, the adaptive decoding algorithm can make a trade-off between the complexity and the performance.

## Distributed punctured LDPC coding scheme using novel shuffled decoding for MIMO relay channels

- **Status**: ✅
- **Reason**: 분산 punctured LDPC의 shuffled decoding 개선 + punctured VN recoverability 저복잡도 계산(90% 단축)은 BP 디코더 비의존 기법으로 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6333910
- **Type**: conference
- **Published**: 27-31 Aug.
- **Authors**: Nanfan Qiu, Xiao Peng, Yichao Lu +1
- **PDF**: https://ieeexplore.ieee.org/document/6333910
- **Abstract**: We propose a distributed punctured LDPC coding scheme to approach the theoretical limit for half-duplex MIMO relay channels. Distributed punctured LDPC coding scheme only requires the design of mother code which avoids complicated joint signal design in previous LDPC schemes [6],[7]. For punctured LDPC decoding, shuffled decoding algorithm proposed in [4] can provide good performance, however traditional BP decoding algorithm should also be used for calculating recoverability. Therefore we propose a low complexity algorithm to calculate the recoverability of punctured variable nodes which can reduce nearly 90% computational time compared with [4]. Furthermore, soft information relaying protocol is adopted to allow relay forwarding soft messages to destination. By this method, LLR values received at the destination will become more reliable. The simulation results verify that our proposed methods can achieve better performance comparing with previous reported methods in literature.

## Absorbing sets and cycles

- **Status**: ✅
- **Reason**: absorbing set과 cycle 등가성·degree distribution 조건으로 error floor 회피 제시, 코드설계 기법(E) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6325224
- **Type**: conference
- **Published**: 27-31 Aug.
- **Authors**: Gottfried Lechner, Sarah J. Johnson
- **PDF**: https://ieeexplore.ieee.org/document/6325224
- **Abstract**: Absorbing sets have been identified as structures in the graph of a low-density parity-check code that cause error floors - in particular in combination with binary message passing decoding algorithms. In this paper it is shown that absorbing sets involving only variable nodes up to degree 3 are equivalent to cycles and a sufficient and necessary condition on the degree distribution to avoid these absorbing sets is derived. The results are extended to irregular graphs and simulation results demonstrate the improvement in the error floor region.

## Comparison of LDPC block and LDPC convolutional codes based on their decoding latency

- **Status**: ✅
- **Reason**: 바이너리 protograph regular LDPC block vs convolutional 비교, sliding window 디코더·BP 복잡도-지연 트레이드오프 기법(C/E) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6325232
- **Type**: conference
- **Published**: 27-31 Aug.
- **Authors**: Najeeb ul Hassan, Michael Lentmaier, Gerhard P. Fettweis
- **PDF**: https://ieeexplore.ieee.org/document/6325232
- **Abstract**: We compare LDPC block and LDPC convolutional codes with respect to their decoding performance under low decoding latencies. Protograph based regular LDPC codes are considered with rather small lifting factors. LDPC block and convolutional codes are decoded using belief propagation. For LDPC convolutional codes, a sliding window decoder with different window sizes is applied to continuously decode the input symbols. We show the required Eb/N0 to achieve a bit error rate of 10−5 for the LDPC block and LDPC convolutional codes for the decoding latency of up to approximately 550 information bits. It has been observed that LDPC convolutional codes perform better than the block codes from which they are derived even at low latency. We demonstrate the trade off between complexity and performance in terms of lifting factor and window size for a fixed value of latency. Furthermore, the two codes are also compared in terms of their complexity as a function of Eb/N0. Convolutional codes with Viterbi decoding are also compared with the two above mentioned codes.

## Rate-compatible QC-LDPC codes design based on EXIT chart analysis

- **Status**: ✅
- **Reason**: EXIT chart 기반 rate-compatible QC-LDPC column extension 새 구성 설계(E) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6314328
- **Type**: conference
- **Published**: 27-31 Aug.
- **Authors**: Zaishuang Liu, Kewu Peng, Weilong Lei +2
- **PDF**: https://ieeexplore.ieee.org/document/6314328
- **Abstract**: This paper proposes a "column extension" design method for rate-compatible quasi-cyclic (QC) low-density parity-check (LDPC) codes, which can provide efficient multi-rate coding schemes for communication systems with flexible spectrum efficiency. The optimization of degree distributions among multiple code rates makes the designed QC-LDPC codes achieve excellent performance at each code rate, while the nested parity-check matrix structure of the designed codes facilitates the implementation of multi-rate encoder/decoder and offers the advantage of low-complexity. A comparison with the multi-rate LDPC codes in DVB-S2 specification is addressed. Extrinsic information transfer (EXIT) chart analysis predicts the superiorities of the optimized degree distributions in Eb/N0 thresholds, and the bit error rate (BER) simulation results show that the designed codes perform 0.03-0.1 dB better than the DVB-S2 64K codes at each typical code rate, with even shorter code length.

## Spatially coupled protograph-based LDPC codes for incremental redundancy

- **Status**: ✅
- **Reason**: protograph 기반 SC-LDPC rate-compatible 구성, 바이너리 코드설계(E) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6325218
- **Type**: conference
- **Published**: 27-31 Aug.
- **Authors**: Walter Nitzold, Michael Lentmaier, Gerhard P. Fettweis
- **PDF**: https://ieeexplore.ieee.org/document/6325218
- **Abstract**: We investigate a family of protograph based rate-compatible LDPC convolutional codes. The code family shows improved thresholds close to the Shannon limit compared to their uncoupled versions for the binary erasure channel as well as the AWGN channel. In fact, the gap to Shannon limit is almost uniform for all members of the code family ensuring good performance for all subsequent incremental redundancy transmissions. Compared to similar code families based on regular LDPC codes [1] the complexity of our approach grows slower for the considered rates.

## Efficient iterative decoding of LDPC in the presence of strong phase noise

- **Status**: ✅
- **Reason**: 강한 위상잡음 하 새 메시지패싱(canonical 모델+클러스터링) 디코더 — BP 개선(C) 이식 가능성, 애매하면 in
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6325187
- **Type**: conference
- **Published**: 27-31 Aug.
- **Authors**: Shachar Shayovitz, Dan Raphaeli
- **PDF**: https://ieeexplore.ieee.org/document/6325187
- **Abstract**: In this paper we propose a new efficient message passing algorithm for decoding LDPC transmitted over a channel with strong phase noise. The algorithm performs approximate bayesian inference on a factor graph representation of the channel and code joint posterior. The approximate inference is based on an improved canonical model for the messages of the Sum & Product Algorithm, and a method for clustering the messages using the directional statistics framework. The proposed canonical model includes treatment for phase slips which can limit the performance of tracking algorithms. We show simulation results and complexity analysis for the proposed algorithm demonstrating its superiority over some of the current state of the art algorithms.

## A space-time redundancy technique for embedded stochastic error correction

- **Status**: ✅
- **Reason**: stochastic LDPC 디코더 feedback+시간적 다수결 중복 신규 기법 — 디코더/HW 결함내성(C/D) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6325194
- **Type**: conference
- **Published**: 27-31 Aug.
- **Authors**: Chris Winstead, Yangyang Tang, Emmanuel Boutillon +2
- **PDF**: https://ieeexplore.ieee.org/document/6325194
- **Abstract**: An error-correction algorithm, referred as to Low Density Parity Check (LDPC) stochastic decoding technique, has recently been introduced for implementing iterative LDPC decoders in logic technologies with a high rate of transient faults. In this work, a modified algorithm that includes a feedback mechanism is first presented. A temporal majority logic is also applied at the decoder's output, providing an additional dimension of redundancy. By comparison to Gallager-A decoding method, the combination of feedback with temporal redundancy is shown to significantly increase the decoder's resilience against a high rate of internal upsets as a gain of up to three orders of magnitude.

## A puncturing algorithm for rate-compatible LDPC convolutional codes

- **Status**: ✅
- **Reason**: RC 펑처링 알고리즘이 trapping set/short cycle 최소화 기준으로 설계됨 — LDPC 코드설계(E) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6325182
- **Type**: conference
- **Published**: 27-31 Aug.
- **Authors**: Hua Zhou, David G. M. Mitchell, Norbert Goertz +1
- **PDF**: https://ieeexplore.ieee.org/document/6325182
- **Abstract**: A family of rate-compatible (RC) punctured low-density parity-check convolutional codes (LDPC-CCs) is derived from an LDPC-CC by periodically puncturing encoded bits (variable nodes) with respect to several criteria: (1) ensuring the recoverability of punctured variable nodes, (2) minimizing the number of completely punctured cycle trapping sets (CPCTSs), and (3) minimizing the number of punctured variable nodes involved in short cycles. As an example, a family of RC punctured LDPC-CCs with rates 4/9, 4/8, 4/7, 4/6, and 4/5 are obtained from the (21,3, 5) Tanner LDPC-CC.

## A LDPC Encoding and Decoding Scheme of Low Complexity Applied to Physical Layer 802.16e

- **Status**: ✅
- **Reason**: 802.16e LDPC용 개선 BF(bit-flipping) 디코딩+체크행렬 저장 최적화; 이식 가능 저복잡도 디코더(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6322483
- **Type**: conference
- **Published**: 23-25 Aug.
- **Authors**: Xu Li, Zhan Xu
- **PDF**: https://ieeexplore.ieee.org/document/6322483
- **Abstract**: In the IEEE 802.16e OFDM (Orthogonal Frequency Division Multiplexing) physical layer, the optional LDPC (Low Density Parity Check) code channel coding scheme based on the IEEE 802.16e protocol is able to be applied in order to improve the whole system's BER (bit error rate) performance. Due to the excellent characteristics and good error correcting performance of LDPC code itself, it has become the central issue of current channel coding field with broad application prospects. In this paper, we use the improved BF (Bit Flipping) decoding algorithm, which is based on the structure of check matrix and the protocol's provisions of LDPC coding scheme, to replace RS-CC (Reed Solomon-Convolutional Codes) concatenated coding scheme on the consideration of decoding delay and further improvement of BER performance. Meanwhile, the storage method of constructed check matrix mentioned in this paper is also optimized. The improved BF decoding algorithm can be verified by simulation that improvement of BER performance is realized on basis of low complexity.
