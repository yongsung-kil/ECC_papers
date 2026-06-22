# IEEE Xplore — 2019-08 (1차선별 통과)


## Reed-Solomon Based Quasi-Cyclic LDPC Codes: Designs, Girth, Cycle Structure, and Reduction of Short Cycles

- **Status**: ✅
- **Reason**: RS기반 QC-LDPC 구성, girth≥8·short cycle 제거 신규 코드설계(E), 바이너리
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8714057
- **Type**: journal
- **Published**: Aug. 2019
- **Authors**: Xin Xiao, Bane Vasić, Shu Lin +2
- **PDF**: https://ieeexplore.ieee.org/document/8714057
- **Abstract**: Designs and constructions of quasi-cyclic (QC) LDPC codes for the AWGN channel are presented. The codes are constructed based on the conventional parity-check matrices of Reed-Solomon (RS) codes and are referred to as RS-QC-LDPC codes. Several classes of RS-QC-LDPC codes are given. Cycle structural properties of the Tanner graphs of codes in these classes are analyzed and specific methods for constructing codes with girth at least eight and reducing their short cycles are presented. The designed codes perform well in both waterfall and low error-rate regions.

## Implementation of encoder and decoder for LDPC codes based on FPGA

- **Status**: ✅
- **Reason**: IR-QC-LDPC FPGA 인코더/디코더, 병렬 순환시프트 주소디코더 + 정규화 min-sum — D(HW)·C 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8820733
- **Type**: journal
- **Published**: Aug. 2019
- **Authors**: Cheng Kun, Shen Qi, Liao Shengkai +1
- **PDF**: https://ieeexplore.ieee.org/document/8820733
- **Abstract**: This paper proposes a parallel cyclic shift structure of address decoder to realize a high-throughput encoding and decoding method for irregular-quasi-cyclic low-density parity-check (IR-QC-LDPC) codes, with a dual-diagonal parity structure. A normalized min-sum algorithm (NMSA) is employed for decoding. The whole verification of the encoding and decoding algorithm is simulated with Matlab, and the code rates of 5/6 and 2/3 are selected respectively for the initial bit error ratio as 6% and 1.04%. Based on the results of simulation, multi-code rates are compatible with different basis matrices. Then the simulated algorithms of encoder and decoder are migrated and implemented on the field programmable gate array (FPGA). The 183.36 Mbps throughput of encoder and the average 27.85 Mbps decoding throughput with the initial bit error ratio 6% are realized based on FPGA.

## GatedNet: Neural Network Decoding for Decoding Over Impulsive Noise Channels

- **Status**: ✅
- **Reason**: GatedNet 신경망 디코더, BP 능가·부호비의존 NN 디코딩으로 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8734085
- **Type**: journal
- **Published**: Aug. 2019
- **Authors**: Yang Hu, Ling Zhao, Zhiyuan Yan +3
- **PDF**: https://ieeexplore.ieee.org/document/8734085
- **Abstract**: This letter proposes a novel neural network (NN) called GatedNet for decoding over-impulsive noise channels. To reduce the impact of impulsive noise, the neurons in the GatedNet are redesigned with control gates to achieve better performance and robustness. Furthermore, a partially connected layer (PCL) in the neural network design is proposed to reduce the computational complexity. Simulation results show that the proposed GatedNet decoder outperforms the belief propagation (BP) decoder for different impulsive noise channels. Furthermore, it achieves near-maximum likelihood (ML) performance with much shorter decoding time.

## Minimum-Polytope-Based Linear Programming Decoder for LDPC Codes via ADMM Approach

- **Status**: ✅
- **Reason**: ADMM 기반 LP 디코딩 신규 알고리즘(check polytope projection 제거, 병렬·저복잡도) — 이식 가능 바이너리 LDPC 디코더(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8665873
- **Type**: journal
- **Published**: Aug. 2019
- **Authors**: Jing Bai, Yongchao Wang, Francis C. M. Lau
- **PDF**: https://ieeexplore.ieee.org/document/8665873
- **Abstract**: In this letter, we develop an efficient linear programming (LP) decoding algorithm for low-density parity-check (LDPC) codes. The LP relaxation is formulated based on a check-node decomposition approach. Our main contributions are as follows. First, we propose an algorithm based on the alternating direction method of multipliers (ADMM) technique to solve this LP relaxation. By exploiting the orthogonality structure of the LP model, each ADMM update step can be implemented in parallel. Second, the proposed decoding algorithm under this LP formulation eliminates the Euclidean projection on the check polytope compared with the existing ADMM-based LP decoding algorithms. Third, the feasibility analysis of the proposed algorithm is presented. Moveover, complexity analysis shows that our proposed LP decoder in each iteration has a lower complexity than the state-of-the-art ADMM-based LP decoders. Simulation results demonstrate that the proposed LP decoder achieves better performance than other competing ADMM-based LP decoders in terms of decoding time.

## An Improved Gradient Descent Bit-Flipping Decoder for LDPC Codes

- **Status**: ✅
- **Reason**: TRGDBF 신규 경판정 bit-flipping 디코더+HW, trapping set/error-floor 개선으로 이식 가능(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8693677
- **Type**: journal
- **Published**: Aug. 2019
- **Authors**: Hangxuan Cui, Jun Lin, Zhongfeng Wang
- **PDF**: https://ieeexplore.ieee.org/document/8693677
- **Abstract**: Low-complexity and high-performance low-density parity-check (LDPC) decoders are highly demanded in various modern communication and storage systems. In this paper, a novel hard-decision decoding algorithm, called tabu-list random-penalty gradient descent bit-flipping (TRGDBF) algorithm, is proposed. Compared to the state-of-the-art hard-decision algorithms, the TRGDBF algorithm has much better error-correction performance due to several algorithmic improvements. First, a random-penalty term is introduced to the inversion function to help the decoder escape from trapping sets, which are the main causes of the error-floor phenomenon. Second, a tabu-list is employed to improve the decoding efficiency. Numerical results show that the TRGDBF algorithm can achieve up to two orders of magnitude better error-correction performance than the probabilistic gradient descent bit-flipping (PGDBF) algorithm and reduce the average iteration count by about 15%. In addition, a well-optimized hardware architecture is developed to implement the TRGDBF algorithm. Algorithmic transformation and architecture optimization are well explored to reduce the hardware complexity and latency. Synthesis results show that the TRGDBF decoder can work at a higher frequency and offer a larger throughput than the PGDBF decoder.

## Noise-Aided Belief Propagation List Decoding of Polar Codes

- **Status**: ✅
- **Reason**: polar용이나 병렬 BP에 인공잡음 추가하는 noise-aided BPL 아이디어가 LDPC BP로 이식 가능성, 애매→in(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8723089
- **Type**: journal
- **Published**: Aug. 2019
- **Authors**: A. Çağrı Arlı, Orhan Gazi
- **PDF**: https://ieeexplore.ieee.org/document/8723089
- **Abstract**: Noise can help weak information bearing signal to be detected in nonlinear systems by the use of stochastic perturbation. In this letter, we propose a novel belief propagation list (BPL) decoder that relies on artificial noise. The proposed decoder is constructed by using parallel independent BP decoders. Noise with different powers are added to different BP decoders that runs in parallel, and the output of the decoder that pass the early detection and termination criteria check is considered as the recovered data. Adding small amount of noise enables the decoder to handle un-converged errors. The obtained results show that the performance of noise-aided BPL decoder is much better than the performances of BP, successive cancelation (SC), and successive cancelation list (SCL) decoders, and it is a bit behind of cyclic redundancy check aided SCL in terms of bit-error rate performance.

## A Probabilistic Peeling Decoder to Efficiently Analyze Generalized LDPC Codes Over the BEC

- **Status**: ✅
- **Reason**: GLDPC 확률적 peeling 디코더·DE 분석 신규 기법 — 코드설계/디코더 분석(C/E), 애매하나 신규 기여로 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8684906
- **Type**: journal
- **Published**: Aug. 2019
- **Authors**: Yanfang Liu, Pablo M. Olmos, Tobias Koch
- **PDF**: https://ieeexplore.ieee.org/document/8684906
- **Abstract**: In this paper, we analyze the tradeoff between coding rate and asymptotic performance of a class of generalized low-density parity-check (GLDPC) codes constructed by including a certain fraction of generalized constraint (GC) nodes in the graph. The rate of the GLDPC ensemble is bounded using classical results on linear block codes, namely, Hamming bound and Varshamov bound. We also study the impact of the decoding method used at GC nodes. To incorporate both bounded-distance (BD) and maximum likelihood (ML) decoding at GC nodes into our analysis without resorting on multi-edge type of degree distributions (DDs), we propose the probabilistic peeling decoding (P-PD) algorithm, which models the decoding step at every GC node as an instance of a Bernoulli random variable with a successful decoding probability that depends on both the GC block code and its decoding algorithm. The P-PD asymptotic performance over the BEC can be efficiently predicted using standard techniques for LDPC codes such as density evolution (DE) or the differential equation method. Furthermore, for a class of GLDPC ensembles, we demonstrate that the simulated P-PD performance accurately predicts the actual performance of the GLPDC code under ML decoding at GC nodes. We illustrate our analysis for GLDPC code ensembles with regular and irregular DDs. In all cases, we show that a large fraction of GC nodes is required to reduce the original gap to capacity, but the optimal fraction is strictly smaller than one. We then consider techniques to further reduce the gap to capacity by means of random puncturing, and the inclusion of a certain fraction of generalized variable nodes in the graph.

## Adaptive Soft Detection for Flash Memory

- **Status**: ✅
- **Reason**: 플래시 메모리 soft detection·LLR 추정, retention/wear-out 대응 — 카테고리 A 직접
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8723068
- **Type**: journal
- **Published**: Aug. 2019
- **Authors**: Magnus Sandell, Amr Ismail
- **PDF**: https://ieeexplore.ieee.org/document/8723068
- **Abstract**: To provide reliability of flash memory, error-correcting codes are usually used which can be further enhanced by moving on from hard-decision to soft-decision decoders. This requires multiple readings to obtain a reliability measure of the stored data, which is complicated by the fact that a posteriori probability distributions change as the memory ages through retention and wear-out. The existing methods for reading a flash memory either assume knowledge of these distributions or require a large number of readings for accurate estimation. In this letter, we propose a low-complexity algorithm that tracks the soft-decision boundaries and estimates the corresponding log-likelihood ratios (LLRs). It does not require any additional readings and only involves simple calculations using already available variables. The efficacy is verified through the simulations and is shown to provide near-optimal performance.

## PEG based Construction of Irregular QC-LDPC Codes by jointly Optimizing the Girth and the Number and ACE of Short cycles

- **Status**: ✅
- **Reason**: PEG로 girth·짧은사이클 수·ACE 동시 최적화한 불규칙 QC-LDPC 구성, error-floor 개선 카테고리 E
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8934212
- **Type**: conference
- **Published**: 5-8 Aug. 2
- **Authors**: Dongdong Wang, Yantao Guo, Zhihui Wang +2
- **PDF**: https://ieeexplore.ieee.org/document/8934212
- **Abstract**: In this paper, we consider the construction of irregular QC-LDPC codes by jointly optimizing the girth, the number and approximate cycle extrinsic message degree (ACE) of short cycles to further improve the error-floor performance of irregular QC-LDPC codes with given degree distributions. By selecting the best edges, each of which must make the cycles consisting of the current variable node have the best lower bound of ACE or the minimum number of cycles with ACE lower bound, for each variable node via the progressive Edge growth (PEG) approaches, irregular QC-LDPC codes with better tradeoff between girth, the shortest cycle number and ACE could be constructed. Simulation results show that the proposed codes achieve better error-floor performance compared with the codes using the same degree distributions constructed by the recent proposed methods.

## Reliability Assessment of Flooded Min-Sum LDPC Decoders Based on Sub-Threshold Processing Units

- **Status**: ✅
- **Reason**: sub-threshold 처리유닛 기반 flooded Min-Sum LDPC 디코더의 결함/신뢰성 평가; 디코더 HW 신뢰성 분석으로 이식 관련(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8875205
- **Type**: conference
- **Published**: 28-30 Aug.
- **Authors**: Sergiu Nimara
- **PDF**: https://ieeexplore.ieee.org/document/8875205
- **Abstract**: This paper aims to evaluate the performance degradation of faulty flooded Min-Sum LDPC decoder architectures based on sub-threshold processing units, by performing hierarchical decomposition of combinational and sequential sub-blocks of processing units described at RTL level. Logic synthesis of the combinational sub-blocks is performed and faults are injected for each logic gate according to a delay-dependent fault model for critical and non-critical paths of the design. The impact of the probabilistic behavior of sub-threshold gates on the error-correction performance of the decoder is analyzed in terms of bit error rate (BER) metrics for Binary Additive White Gaussian Noise (BiAWGN) communication channel model.

## Optimization of Protograph LDPC Codes based on High-Level Energy Models

- **Status**: ✅
- **Reason**: C/E: quantized Min-Sum 디코더 에너지 모델+protograph 최적화 신규 기법 — NAND 디코더/구성 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8877353
- **Type**: conference
- **Published**: 27-30 Aug.
- **Authors**: Mohamed Yaoumi, François Leduc-Primeau, Elsa Dupraz +1
- **PDF**: https://ieeexplore.ieee.org/document/8877353
- **Abstract**: This paper considers the optimization of the energy consumption of LDPC decoders. For a given protograph, two models are introduced to approximate the energy consumption of a quantized Min-Sum decoder. The first model takes into account the number of operations performed by the decoder, the second model considers the number of bits that are written into memory. An optimization problem is then formulated to minimize the decoder energy consumption with respect to the protograph and the number of iterations, while satisfying a given performance criterion. Finally, an optimization method based on Differential Evolution is proposed.

## Neighbor-Cell-Information Based Detection for LDPC Coded MLC NAND Flash Memory

- **Status**: ✅
- **Reason**: A: LDPC MLC NAND 플래시 직접, CCI 완화 neighbor-cell 후처리 검출 — read-back/LLR에 직결
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8877237
- **Type**: conference
- **Published**: 27-30 Aug.
- **Authors**: Yanfu Li, Guojun Han, Zishuai Peng +2
- **PDF**: https://ieeexplore.ieee.org/document/8877237
- **Abstract**: As the feature size of NAND flash memory decreases, multi-level cell (MLC) technique is emerging to dramatically increase the storage density. In such scenarios, the cell-to-cell interference (CCI) arising from parasitic coupling-capacitance between adjacent cells becomes more severe, which will significantly distort the threshold voltage and deteriorate the data-storage reliability. In this paper, through analyzing the characteristics of threshold voltage distribution of low-density parity-check (LDPC) code MLC NAND flash memory, a post-processing detection scheme is proposed to mitigate the CCI. The proposed scheme utilizes both the neighbor-cell information and the neighbor-a-priori information, and thus is referred to as the Mixed-NCI detector. A salient feature of the proposed detection scheme is that it can acquire very accurate read-back voltages by exploiting the neighbor-cell information of the successfully decoded cells. Analyses and simulation results show that the proposed Mixed-NCI detector achieves remarkable performance gains compared with the state-of-the-art counterparts. The above advantage makes the Mixed-NCI detector extremely attractive for MLC NAND flash memory.

## Decoding Wave Velocity Analysis for SC-LDPC Ensembles on BMS Channels using Interpolation

- **Status**: ✅
- **Reason**: E: SC-LDPC 디코딩 wave velocity 분석 신규 기법(IDE), 바이너리 LDPC 코드설계 분석 도구로 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8877194
- **Type**: conference
- **Published**: 27-30 Aug.
- **Authors**: Kexin Zhang, Mingjun Dai, Dan Zeng +1
- **PDF**: https://ieeexplore.ieee.org/document/8877194
- **Abstract**: This paper is concerned with decoding waves for spatially-coupled low-density parity-check (SC-LDPC) ensembles on binary memoryless symmetric (BMS) channels. We propose an approach termed as interpolated density evolution (IDE) to predict the velocities of decoding waves. In this approach, we approximate the densities of decoding waves via interpolation and establish two transfer functions for the update of interpolation functions. Comparison results indicate that the proposed IDE approach achieves a good trade-off between computational cost and accuracy as compared with the standard coupled density evolution (CDE) approach and the extrinsic information transfer (EXIT) approach based on Gaussian approximation (GA). This highlights the attractiveness of the proposed approach in the analysis of SC-LDPC ensembles on general BMS channels.

## Small stopping sets in projective low-density parity-check codes

- **Status**: ✅
- **Reason**: E: redundant parity-check 행렬로 stopping set 제거하는 코드 구성 기법, 바이너리 LDPC error floor 개선에 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8989047
- **Type**: conference
- **Published**: 25-28 Aug.
- **Authors**: Yuichiro Fujiwara, Yu Tsunoda
- **PDF**: https://ieeexplore.ieee.org/document/8989047
- **Abstract**: It is known that redundant parity-check equations can improve the performance of an LDPC code by reducing the number of harmful substructures in the parity-check matrix. However, it is a difficult problem to design a parity-check matrix in such a way that it avoids substructures that are known to be harmful to iterative decoding while keeping the number of redundant parity-check equations moderate and ensuring other desirable properties. We explicitly give redundant parity-check matrices for cyclic regular LDPC codes of length n and minimum distance d ~ √n in which there are only n parity-check equations but no stopping sets of size d+1 or smaller except for those that correspond to the nonzero codewords of the smallest weight. We do this by showing that the well-known projective LDPC codes from the incidence matrices of projective planes PG(2, q) with q even have this property. This result may give insight into how the small number of redundant parity-check equations in the geometric LDPC codes may be contributing to the good performance reported in the literature. We also give a slightly improved upper bound on the size of a smallest generic erasure correcting set.

## LDPC Code Design for Delayed Bit-Interleaved Coded Modulation

- **Status**: ✅
- **Reason**: 제약 PEG-like 코드 구성+DE 최적화로 바이너리 LDPC 설계(E), BICM 채널의존성 있으나 구성 기법 떼어내 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8989384
- **Type**: conference
- **Published**: 25-28 Aug.
- **Authors**: Yihuan Liao, Lei Yang, Jinhong Yuan +3
- **PDF**: https://ieeexplore.ieee.org/document/8989384
- **Abstract**: This paper proposes a method to design low-density parity-check (LDPC) codes for delayed bit-interleaved coded modulation (DBICM). In the method, the code variable node (VN) degree distributions and the assignments of VNs with different degrees to DBICM subchannels are optimized via two cascaded differential evolution (DE) steps. In each step, to optimize VN degree distribution or channel assignment, a parity-check matrix is constructed, and the associated decoding threshold is calculated for each element in a generation. In constructing a parity-check matrix for each channel assignment, we propose a constraint PEGlike code construction method. Protograph-EXIT is employed to calculate the decoding threshold for each parity-check matrix. We apply the proposed method to construct irregular binary LDPC codes for both 16-QAM DBICM and BICM schemes. Simulation results demonstrate that the optimized LDPC codes are within 1 dB from the associated capacity limit at a bit error rate (BER) of 10–6. Besides, the LDPC coded DBICM achieves an SNR gain of 0.5 dB to 0.1 dB over BICM counterparts at a code rate ranges from 0.25 to 0.5.

## Enhanced Quasi-Maximum Likelihood Decoding of Short LDPC Codes Based on Saturation

- **Status**: ✅
- **Reason**: 단축 LDPC용 EQML 디코더(불신뢰 VN 선택+재처리, PPS 정지규칙)는 부호 비의존적 BP 개선 기법으로 NAND LDPC 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8989272
- **Type**: conference
- **Published**: 25-28 Aug.
- **Authors**: Peng Kang, Yixuan Xie, Lei Yang +3
- **PDF**: https://ieeexplore.ieee.org/document/8989272
- **Abstract**: In this paper, we propose an enhanced quasi-maximum likelihood (EQML) decoder for short LDPC codes. The proposed EQML decoder selects unreliable variable nodes (VNs) and performs the reprocessing if the first belief propagation (BP) decoding attempt fails. To improve the decoding error rate performance, we propose a novel node selection method based on the sign fluctuation of VNs' extrinsic messages. We also present a partial pruning stopping (PPS) rule to reduce the decoding complexity by deactivating part of the decoding tests once a valid codeword is found. Simulation results show that the proposed PPS rule achieves 20% lower decoding complexity compared to the full list decoding without sacrificing the error rate performance. In addition, the proposed EQML decoder outperforms the augmented BP decoder for short LDPC codes and approaches the performance of the ML decoder within 0.3 dB in terms of the frame error rate.

## Spatially Coupled LDPC Codes with Non-uniform Coupling for Improved Decoding Speed

- **Status**: ✅
- **Reason**: 비균일 coupling으로 윈도우 디코더 복잡도 제약 하 성능 개선하는 SC-LDPC 구성 기법(E) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8989360
- **Type**: conference
- **Published**: 25-28 Aug.
- **Authors**: Laurent Schmalen, Vahid Aref
- **PDF**: https://ieeexplore.ieee.org/document/8989360
- **Abstract**: We consider spatially coupled low-density parity-check codes with finite smoothing parameters. A finite smoothing parameter is important for designing practical codes that are decoded using low-complexity windowed decoders. By optimizing the amount of coupling between spatial positions, we show that we can construct codes with improved decoding speed compared with conventional, uniform smoothing constructions. This leads to a significantly better performance under decoder complexity constraints while keeping the degree distribution regular. We optimize smoothing configurations using differential evolution and illustrate the performance gains by means of a simulation.

## Optimizing Polar Codes Compatible with Off-the-Shelf LDPC Decoders

- **Status**: ✅
- **Reason**: C/E: polar code를 off-the-shelf LDPC 디코더로 디코딩하는 패리티검사 행렬 공동설계, LDPC 그래프 구조 기법 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8989269
- **Type**: conference
- **Published**: 25-28 Aug.
- **Authors**: Moustafa Ebada, Ahmed Elkelesh, Stephan ten Brink
- **PDF**: https://ieeexplore.ieee.org/document/8989269
- **Abstract**: Previous work showed that polar codes can be decoded using off-the-shelf LDPC decoders by imposing special constraints on the LDPC code structure, which, however, resulted in some performance degradation. In this paper we show that this loss can be mitigated; in particular, we demonstrate how the gap between LDPC-style decoding and Arıkan’s Belief Propagation (BP) decoding of polar codes can be closed by taking into account the underlying graph structure of the LDPC decoder while jointly designing the polar code and the parity-check matrix of the corresponding LDPC-like code. The resulting polar codes under conventional LDPC-style decoding are shown to have similar error-rate performance when compared to some well-known and standardized LDPC codes. Moreover, we obtain performance gains in the high SNR region.

## A Finite-Length Construction of Irregular Spatially-Coupled Codes

- **Status**: ✅
- **Reason**: E: finite-length irregular SC-LDPC 구성 프레임워크, 스토리지용 바이너리 LDPC 코드 설계로 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8989060
- **Type**: conference
- **Published**: 25-28 Aug.
- **Authors**: Homa Esfahanizadeh, Ruiyi Wu, Lara Dolecek
- **PDF**: https://ieeexplore.ieee.org/document/8989060
- **Abstract**: Spatially-coupled (SC) LDPC codes have recently emerged as an excellent choice for error correction in modern data storage and communication systems due to their outstanding performance. It has long been known that irregular graph codes offer performance advantage over their regular counterparts. In this paper, we present a novel combinatorial framework for designing finite-length irregular SC LDPC codes. Our irregular SC codes have the desirable properties of regular SC codes thanks to their structure while offering significant performance benefits that come with the node degree irregularity. Coding constructions proposed in this work contribute to the existing portfolio of finite-length graph code designs.

## Increasing the Lifetime of Flash Memories Using Multi-Dimensional Graph-Based Codes

- **Status**: ✅
- **Reason**: 플래시 메모리 직접(A), MD 그래프 코드 circulant 재배치로 absorbing set 최소화하는 신규 코드설계(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8989395
- **Type**: conference
- **Published**: 25-28 Aug.
- **Authors**: Ahmed Hareedy, Rohith Kuditipudi, Robert Calderbank
- **PDF**: https://ieeexplore.ieee.org/document/8989395
- **Abstract**: In order to meet the demands of data-hungry applications, data storage devices are required to be increasingly denser. Various sources of error appear with this increase in density. Multi-dimensional (MD) graph-based codes are capable of mitigating error sources like interference and channel non-uniformity in dense storage devices. Recently, a technique was proposed to enhance the performance of MD spatially-coupled codes that are based on circulants. The technique carefully relocates circulants to minimize the number of short cycles. However, cycles become more detrimental when they combine together to form more advanced objects, e.g., absorbing sets, including low-weight codewords. In this paper, we show how MD relocations can be exploited to minimize the number of detrimental objects in the graph of an MD code. Moreover, we demonstrate the savings in the number of relocation arrangements earned by focusing on objects rather than cycles. Our technique is applicable to a wide variety of one-dimensional (OD) codes. Simulation results reveal significant lifetime gains in practical Flash systems achieved by MD codes designed using our technique compared with OD codes having similar parameters.

## From the Spectrum of the Adjacency Matrix to the Spectrum of Directed Edge Matrix: Counting Cycles of a Bipartite Graph Through a Simple Equation

- **Status**: ✅
- **Reason**: LDPC Tanner 그래프 단축 사이클 카운팅을 O(|V|^3)로 계산하는 새 방법, girth/사이클 제거 코드설계(E) 지원 기법
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8989394
- **Type**: conference
- **Published**: 25-28 Aug.
- **Authors**: Ali Dehghan, Amir H. Banihashemi
- **PDF**: https://ieeexplore.ieee.org/document/8989394
- **Abstract**: Counting short cycles in bipartite graphs is a fundamental problem of interest in many fields including the analysis and design of low-density parity-check (LDPC) codes. There are two computational approaches to count short cycles (with length smaller than 2g, where g is the girth of the graph) in bipartite graphs. The first approach is applicable to a general (irregular) bipartite graph, and uses the spectrum {ηi} of the directed edge matrix of the graph to compute the multiplicity Nk of k-cycles with k <; 2g through the simple equation Nk =Σi ηik/(2k). This approach has a computational complexity O(|E|3), where |E| is number of edges in the graph. The second approach is only applicable to bi-regular bipartite graphs, and uses the spectrum {λi} of the adjacency matrix (graph spectrum) and the degree sequences of the graph to compute Nk. The complexity of this approach is O(|V|3), where |V| is number of nodes in the graph. This complexity is less than that of the first approach, but the equations involved in the computations of the second approach are very tedious, particularly for k ≥ g + 6. In this paper, we establish an analytical relationship between the two spectra {ηi} and {λi} for bi-regular bipartite graphs. Through this relationship, the former spectrum can be derived from the latter through simple equations. This allows the computation of Nk using Nk = Σi ηik/(2k) but with a complexity of O(|V|3) rather than O(|E|3).

## On the Computational Complexity of Finding Bipartite Graphs with a Small Number of Short Cycles and Large Girth

- **Status**: ✅
- **Reason**: E: Tanner 그래프 short cycle/girth 관련 알고리즘적 결과, 바이너리 LDPC 코드 구성에 직접 관련
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8989134
- **Type**: conference
- **Published**: 25-28 Aug.
- **Authors**: Ali Dehghan, Amir H. Banihashemi
- **PDF**: https://ieeexplore.ieee.org/document/8989134
- **Abstract**: The problem of finding bipartite (Tanner) graphs with given degree sequences that have large girth and few short cycles is of great interest in many applications including construction of good low-density parity-check (LDPC) codes. In this paper, we prove that for a given set of integers $\alpha, \beta$, and $\gamma$, and degree sequences $\pi$ and $\pi$’, the problem of determining whether there exists a simple bipartite graph with degree sequences $(\pi,\ \pi')$ that has at most $\alpha$ ($\beta$ and $\gamma$) cycles of length four (six and eight, respectively) is NP-complete. This is proved by a two-step polynomial-time reduction from the 3-Partition Problem. On the other hand, using connections to linear hypergraphs, we prove that given the degree sequence $\pi$, a polynomial time algorithm can be devised to determine whether there exists a bipartite graph whose degree sequence on one side of the bipartition is $\pi$ and has a girth of at least six.

## Optimization of Nested Array-based LDPC Codes Via Spatial Coupling

- **Status**: ✅
- **Reason**: SC-LDPC absorbing set 최소화 라인카운팅 최적화는 코드설계 기법(E)으로 이식 가능, 바이너리 LDPC
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8989313
- **Type**: conference
- **Published**: 25-28 Aug.
- **Authors**: Salman Habib, David G. M. Mitchell, Jörg Kliewer
- **PDF**: https://ieeexplore.ieee.org/document/8989313
- **Abstract**: Linear nested codes, where two or more subcodes are nested in a global code, have been proposed as candidates for reliable multi-terminal communication. In this paper, we consider nested array-based spatially coupled LDPC codes and propose a line-counting based optimization scheme for minimizing the number of dominant absorbing sets in order to improve its performance in the high signal-to-noise ratio regime. The presented multi-step optimization process is applied first to one of the nested codes, then an optimization of the remaining nested codes is carried out based on these code constraints. We also show that for certain code parameters, dominant absorbing sets in the Tanner graphs of all nested codes can be completely removed using our proposed optimization strategy.

## DIR: Dynamic Request Interleaving for Improving the Read Performance of Aged SSDs

- **Status**: ✅
- **Reason**: A. NAND/SSD 직접 — TLC LDPC read-retry 지연 감소 인터리빙 기법, NAND ECC 운용 직결
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8863520
- **Type**: conference
- **Published**: 18-21 Aug.
- **Authors**: Shiqiang Nie, Youtao Zhang, Weiguo Wu +2
- **PDF**: https://ieeexplore.ieee.org/document/8863520
- **Abstract**: TLC (Triple-Level Cell) NAND flash is increasingly adopted to build SSDs (Solid-State Drives) for modern computer systems. While TLC NAND flash effectively improves storage density, it faces severe reliability issues, in particular, the pages stored using different bits exhibit different BERs (bit error rates). Integrating strong LDPC (Low-Density Parity-Check code) helps to improve reliability but suffers from long and proportional read latency due to multiple read retries. In this paper, we propose DIR, a novel strategy for improving the performance of TLC NAND flash-based SSDs, in particular, the aged ones with large BERs. DIR exploits the observation that the latency of an I/O request is determined, without considering the queuing time, by the access of the slowest device page, i.e., the page that has the highest BER. By grouping consecutive logical pages that have high locality, and interleaving their encoded data in three different types of device pages that have different RBERs, DIR effectively reduces the number of read retries for LDPC. Our experimental results show that adopting DIR in aged SSDs exploits nearly 75% locality from I/O requests, and, on average, reduces 36% read latency over conventional aged SSDs.

## Optimizing Tail Latency of LDPC based Flash Memory Storage Systems Via Smart Refresh

- **Status**: ✅
- **Reason**: NAND 플래시 LDPC 시스템의 긴 디코딩 지연(tail latency) 완화 refresh 기법 — 카테고리 A 직접 해당
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8834728
- **Type**: conference
- **Published**: 15-17 Aug.
- **Authors**: Yina Lv, Liang Shi, Qiao Li +3
- **PDF**: https://ieeexplore.ieee.org/document/8834728
- **Abstract**: Flash memory has been developed with bit density improvement, technology scaling, and 3D stacking. With this trend, its reliability has been degraded significantly. Error correction code, low density parity code (LDPC), which has strong error correction capability, has been employed to solve this issue. However, one of the critical issues of LDPC is that it would introduce a long decoding latency on devices with low reliability. In this case, tail latency would happen, which will significantly impact the quality of service (QoS). In this work, a set of smart refresh schemes is proposed to optimize the tail latency. The basic idea of the work is to refresh data when the accessed data has a long decoding latency. Two smart refresh schemes are proposed for this work: The first refresh scheme is designed to refresh long access latency data when it is accessed several times for access performance optimization; The second refresh scheme is designed to periodical detecting data with extremely long access latency and refreshing them for tail latency optimization. Experiment results show that the proposed schemes are able to significantly improve the tail latency and access performance with little overhead.

## Speeding up LDPC Decoder by Inter-Frame Pipeline for Wireless Laser Communications

- **Status**: ✅
- **Reason**: LDPC 레이어드 디코더 inter-frame pipeline 처리량 개선 HW 기법(D), FPGA 구현. NAND 디코더 병렬화에 이식 가능
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:8855948
- **Type**: conference
- **Published**: 11-13 Aug.
- **Authors**: Jipeng Zhang, Zhongyang Yu, Ji Zhang +3
- **PDF**: https://ieeexplore.ieee.org/document/8855948
- **Abstract**: In order to meet the requirements of scenarios such as free space optical (FSO) communications using wireless laser, we need to improve the existing decoding structure of LDPC codes to achieve the goal of high throughput and high reliability. Aiming at solving a problem of idle time between layers in the column-serial layered decoder of LDPC codes, based on the dynamic multi-frame processing (DMFP) strategy we proposed a scheme called inter-frame pipeling (IFP) which can utilize the idle time for speeding up the decoder. Compared with the DMFP strategy the IFP has a doubled reduction of decoding delay. Taking a (4008,3507) LDPC code as an example, the field-programmable gate array (FPGA) based implementation shows that the IFP scheme can increase throughput by at least 30%, approximately reaching to 2.5Gbps.

## A New Low-Resolution Min-Sum Decoder Based on Dynamic Clipping for LDPC Codes

- **Status**: ✅
- **Reason**: LDPC용 저해상도 min-sum, 동적 clipping 적응형 2비트 양자화 신규 디코더(C)—NAND LLR 양자화에 직접 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8855823
- **Type**: conference
- **Published**: 11-13 Aug.
- **Authors**: Huanyu He, Lei Chu, Robert Caiming Qiu
- **PDF**: https://ieeexplore.ieee.org/document/8855823
- **Abstract**: Compared with the sum-product algorithm (SPA) with high decoding complexity for low-density parity-check (LDPC) codes, its approximated version, the min-sum algorithm (MSA), reduces the computational complexity at the cost of slight performance degradation. In order to compensate the oversized check-node messages in the MSA, the effect of clipping on variable-node messages is investigated under two-bit resolution. Our results show that the performance of clipped MSA degrades at the high bit error rate (BER) and increases at the low BER as clipping threshold enlarges. Based on these results, we propose a modified quantized MS decoding algorithm where the adaptive clipping threshold is applied on the variable-node messages according to the number of unsatisfied checks per-iteration. The adaptive rule is designed for easy hardware implementations. Numerical results show that the proposed algorithm has considerable improvement in performance compared with the MSA under two-bit precision. And it can achieve the performance near the SPA for some short-length LDPC codes.

## A Double-CNN BP Decoder on Fast Fading Channels Using Correlation Information

- **Status**: ✅
- **Reason**: CNN+BP 디코더, 상관 채널 LLR 정확 산출 기법(C). LLR 계산 개선은 NAND LDPC BP에 이식 검토 가치—애매하여 in
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8855827
- **Type**: conference
- **Published**: 11-13 Aug.
- **Authors**: Jun Li, Xiwei Zhao, Jihao Fan +3
- **PDF**: https://ieeexplore.ieee.org/document/8855827
- **Abstract**: This paper develops a novel double convolutional neural network (CNN) based belief propagation (BP) decoder to improve the error correcting performance on fast fading channels with correlated channel gain and correlated noise. The proposed double-CNN BP decoder consists of two CNNs for predicting channel gain and noise samples, respectively, concatenated with a BP decoder. The input of the BP decoder is the log-likelihood-ratio (LLR) values obtained according to the predicted channel gain along with denoised signals based on predicted noises. We note that the residual noises no longer obey a Gaussian distribution when denoising the signals. Thus, we further derive a new method to obtain the LLR values accurately. Simulation results show that the proposed double-CNN BP decoder achieves a maximum of 7dB gain compared to the conventional BP decoder and the proposed algorithm compensates the performance loss of BP decoder caused by correlation information.
