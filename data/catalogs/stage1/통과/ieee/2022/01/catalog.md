# IEEE Xplore — 2022-01 (1차선별 통과)


## A High-Efficiency Segmented Reconfigurable Cyclic Shifter for 5G QC-LDPC Decoder

- **Status**: ✅
- **Reason**: QC-LDPC 디코더용 분할 재구성형 cyclic shifter(permutation network) 새 HW 아키텍처 — NAND LDPC 디코더 HW로 이식 가능(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:9559711
- **Type**: journal
- **Published**: Jan. 2022
- **Authors**: Hing-Mo Lam, Silin Lu, Hezi Qiu +3
- **PDF**: https://ieeexplore.ieee.org/document/9559711
- **Abstract**: A reconfigurable cyclic shifter is a key element of a QC-LDPC decoder, which is crucial for 5G communication systems. If a traditional reconfigurable cyclic shifter can only shift one input of variable size at a time, a traditional QC-LDPC decoder can only decode one codeword at a time as well. Part of the circuitry of the traditional QC-LDPC decoder inevitably stays in idle during the decoding process if the length (or the lifting parameter) of a codeword is not the maximum, resulting in low hardware efficiency. A segmented reconfigurable cyclic shifter is proposed in this paper, which can be divided into multiple segments of different sizes. Each segment can perform a cyclic shift of an input of different sizes and of different shift values independently. Furthermore, a methodology is proposed to upgrade any state-of-the-art QC-LDPC decoder to a segmented QC-LDPC decoder, by using the proposed segmented shifter. The upgraded segmented QC-LDPC decoder is able to parallelly decode multiple codewords (or inputs) of different lengths at a time. A test chip of the proposed segmented QC-LDPC decoder with the proposed segmented reconfigurable cyclic shifter has been fabricated in a 0.18-<inline-formula> <tex-math notation="LaTeX">$\mu \text{m}$ </tex-math></inline-formula> CMOS technology to demonstrate the feature of parallelly decoding multiple codewords. The performance analysis shows that when the number of small codewords is increased from 0 to 100000 per second, the throughput of the traditional QC-LDPC decoder drops from 844.80 Mbps to 4.40 Mbps, while the QC-LDPC decoder with the proposed segmented shifter only slightly drops to 814.01 Mbps. By applying the segmented QC-LDPC decoder in 5G base stations, the base stations are enabled to support more low-traffic users.

## Integer Ring Sieve for Constructing Compact QC-LDPC Codes With Girths 8, 10, and 12

- **Status**: ✅
- **Reason**: girth 8/10/12 compact QC-LDPC 구성의 새 정수환 sieve 기법 — 짧은 부호 설계로 바이너리 QC-LDPC 코드 설계에 직접 이식 가능(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9552834
- **Type**: journal
- **Published**: Jan. 2022
- **Authors**: Alireza Tasdighi, Emmanuel Boutillon
- **PDF**: https://ieeexplore.ieee.org/document/9552834
- **Abstract**: This paper proposes a new method of constructing compact fully-connected Quasi-Cyclic Low Density Parity Check (QC-LDPC) codes with girth  $g$  = 8, 10, and 12. The originality of the proposed method is to impose constraints on the exponent matrix P to reduce the search space drastically. For a targeted lifting degree of  $N$ , the first step of the method is to sieve the integer ring  $\mathbb {Z}_{N}$  to make a particular sub-group with specific properties to construct the second column of P (the first column being filled with zeros). The remaining columns of P are determined recursively as multiples of the second column by adapting the sequentially multiplied column (SMC) method whereby a controlled greedy search is applied at each step. The codes constructed with the proposed semi-algebraic method show lengths that can be significantly shorter than their best counterparts in the literature.

## Error-and-Erasure Decoding of Product and Staircase Codes

- **Status**: ✅
- **Reason**: product/staircase 코드 error-and-erasure 디코딩 + ternary message passing DE 분석, 양자화 레벨 설계 — 반복 디코더/양자화 기법이 NAND LDPC에 이식 가능(C/E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9564072
- **Type**: journal
- **Published**: Jan. 2022
- **Authors**: Lukas Rapp, Laurent Schmalen
- **PDF**: https://ieeexplore.ieee.org/document/9564072
- **Abstract**: High-rate product codes (PCs) and staircase codes (SCs) are ubiquitous codes in high-speed optical communication achieving near-capacity performance on the binary symmetric channel. Their success is mostly due to very efficient iterative decoding algorithms that require very little complexity. In this paper, we extend the density evolution (DE) analysis for PCs and SCs to a channel with ternary output and ternary message passing, where the third symbol marks an erasure. We investigate the performance of a standard error-and-erasure decoder and of its simplification using DE. The proposed analysis can be used to find component code configurations and quantizer levels for the channel output. We also show how the use of even-weight BCH subcodes as component codes can improve the decoding performance at high rates. The DE results are verified by Monte-Carlo simulations, which show that additional coding gains of up to 0.6dB are possible by ternary decoding, at only a small additional increase in complexity compared to traditional binary message passing.

## A Class of Optimal Structures for Node Computations in Message Passing Algorithms

- **Status**: ✅
- **Reason**: message passing 노드 연산 최소복잡도/지연 구조 설계 — LDPC 디코더 노드 계산 HW 최적화에 직접 이식 가능(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9570373
- **Type**: journal
- **Published**: Jan. 2022
- **Authors**: Xuan He, Kui Cai, Liang Zhou
- **PDF**: https://ieeexplore.ieee.org/document/9570373
- **Abstract**: Consider the computations at a node in a message passing algorithm. Assume that the node has incoming and outgoing messages  $\mathbf {x} = (x_{1}, x_{2}, \ldots, x_{n})$  and  $\mathbf {y} = (y_{1}, y_{2}, \ldots, y_{n})$ , respectively. In this paper, we investigate a class of structures that can be adopted by the node for computing  $\mathbf {y}$  from  $\mathbf {x}$ , where each  $y_{j}, j = 1, 2, \ldots, n$  is computed via a binary tree with leaves  $\mathbf {x}$  excluding  $x_{j}$ . We make three main contributions regarding this class of structures. First, we prove that the minimum complexity of such a structure is  $3n - 6$ , and if a structure has such complexity, its minimum latency is  $\delta + \lceil \log (n-2^{\delta }) \rceil $  with  $\delta = \lfloor \log (n/2) \rfloor $ , where the logarithm always takes base two. Second, we prove that the minimum latency of such a structure is  $\lceil \log (n-1) \rceil $ , and if a structure has such latency, its minimum complexity is  $n \log (n-1)$  when  $n-1$  is a power of two. Third, given  $(n, \tau)$  with  $\tau \geq \lceil \log (n-1) \rceil $ , we propose a construction for a structure which we conjecture to have the minimum complexity among structures with latencies at most  $\tau $ . Our construction method runs in  $O(n^{3} \log ^{2}(n))$  time, and the obtained structure has complexity at most (generally much smaller than)  $n \lceil \log (n) \rceil - 2$ .

## A Reliability Profile Based Low-Complexity Dynamic Schedule LDPC Decoding

- **Status**: ✅
- **Reason**: 신뢰도 프로파일 기반 저복잡도 동적 스케줄 LDPC 디코딩(RPD), 정수연산. 바이너리 LDPC 디코더 신규 기법으로 NAND 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9663312
- **Type**: journal
- **Published**: 2022
- **Authors**: Ruijia Yuan, Tianjiao Xie, Zhongfeng Wang
- **PDF**: https://ieeexplore.ieee.org/document/9663312
- **Abstract**: In order to improve the Bit Error Rate (BER) performance of Low-Density Parity-Check (LDPC) codes, In this paper, we propose a Reliability Profile (RP) Based Low-Complexity Dynamic Schedule, called RPD. In terms of dynamic scheduling, the new RPD method is distinct from the existing residual belief propagation (RBP) and its variations, since RPD is based on residual criterion. Reliability divides nodes message into two categories: reliable and unreliable. By using as many messages as possible from the latest available current iteration instead of the previous iteration to update unreliable messages multiple times to speed up the convergence speed and increase the total number of updates of effective nodes message, so as to improve the BER performance. By not updating the reliable message, the number of ineffective nodes message updates is reduced, thereby reducing the decoding complexity. Besides, the more iterations increase, the fewer calculations of these reliable nodes. Moreover, based on reliability profile, RPD has an advantage over RBP for dynamic scheduling in that the former only needs integer operations, while the latter requires float operations. Therefore, the RPD algorithm not only accelerates the convergence speed of LDPC decoding and but also improves the BER performance while reducing the complexity. The analysis and simulation results show that the RPD strategy not only retains the fast-convergence advantage of RBP, but also has a better convergence BER performance compared to that of node-wise residual belief propagation (NW RBP). Furthermore, the simulation results show that the RPD can significantly improve the convergence speed of protograph LDPC decoding.

## LDPC Coded Multi-User Massive MIMO Systems With Low-Complexity Detection

- **Status**: ✅
- **Reason**: LDPC 차수분포 설계를 EXIT 분석으로 최적화(JDD) — 이식 가능한 바이너리 LDPC 코드설계 기법(E), 애매하나 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9726213
- **Type**: journal
- **Published**: 2022
- **Authors**: Han Jin Park, Jeong Woo Lee
- **PDF**: https://ieeexplore.ieee.org/document/9726213
- **Abstract**: We design a low-density parity-check (LDPC) coded multi-user (MU) massive multiple-input multiple-output (MIMO) system with an iterative joint detection and decoding (JDD) algorithm. As a low-complexity MU detection scheme, we consider a factor graph based belief propagation detection with Gaussian approximation of interference, called a FG-GAI BP detection. We introduce a factor graph representation of LDPC coded MU massive MIMO system and define the message updating rule in the JDD process. We devise a design tool for analyzing extrinsic information transfer (EXIT) characteristics of messages exchanged in JDD, based on which degree distribution of LDPC codes and a JDD strategy are efficiently designed for coded MU massive MIMO systems. A JDD strategy and LDPC codes are designed such that a fast convergence of JDD and a low bit error probability are attained. It is observed that the coded MU massive MIMO system equipped with LDPC codes and the JDD strategy designed by the proposed method shows a lower bit error rate than conventional ones with a given number of iterations.

## High-Throughput Multi-Frame Decoding of QC-LDPC Codes With Modified Rejection-Based Minimum Finding

- **Status**: ✅
- **Reason**: QC-LDPC min-sum 디코더의 새 rejection-based 최소값 탐색+멀티프레임 파이프라인 HW(28nm) — 이식 가능 디코더/HW 신규 기여(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9674935
- **Type**: journal
- **Published**: 2022
- **Authors**: Alireza Hasani, Lukasz Lopacinski, Goran Panic +1
- **PDF**: https://ieeexplore.ieee.org/document/9674935
- **Abstract**: The key computation in the min-sum decoding algorithm of a Low-Density Parity-Check (LDPC) is finding the first two minima and also the location of the first minimum among a set of messages passed from Variable Nodes (VNs) to Check Nodes (CNs) in a Tanner graph. In this paper, we propose a modified rejection-based scheme for this task which is able to find the one-hot sequence of the minimum location instead of its index. We show that this modification effectively reduces the complexity of min-sum decoding algorithm. Additionally, we reveal a pipelining potential in such a rejection-based architecture which facilitates the multi-frame decoding of Low-Density Parity-Check (LDPC) codes and therefore results in an improvement in decoding throughput with bearable hardware overhead. Synthesis and floorplanning in an industrial 28 nm CMOS technology show improved results in terms of throughput, power, and chip area.

## Construction of Protograph-Based Partially Doped Generalized LDPC Codes

- **Status**: ✅
- **Reason**: 프로토그래프 기반 GLDPC partial doping 코드설계, 바이너리, error floor 개선 (E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9877796
- **Type**: journal
- **Published**: 2022
- **Authors**: Jaewha Kim, Jae-Won Kim, Hee-Youl Kwak +1
- **PDF**: https://ieeexplore.ieee.org/document/9877796
- **Abstract**: In this paper, we propose a new code design technique, called partial doping, for protograph-based generalized low-density parity-check (GLDPC) codes. While the conventional construction method of protograph-based GLDPC codes is to replace some single parity-check (SPC) nodes with generalized constraint (GC) nodes applying to multiple variable nodes (VNs) that are connected in the protograph, the proposed technique can select any VNs in the protograph to be protected by GC nodes. In other words, the partial doping technique facilitates finer tuning of doping, which in turn enables a sophisticated code optimization with higher degree of freedom. We construct the proposed partially doped GLDPC (PD-GLDPC) codes using the partial doping technique and optimize the PD-GLDPC codes by the protograph extrinsic information transfer (PEXIT) analysis. In addition, we propose a condition guaranteeing the linear minimum distance growth of the PD-GLDPC codes and use the condition for the optimization. Experimental results show that the optimized PD-GLDPC codes outperform the conventional GLDPC codes and have competitive performance compared to the state-of-the-art protograph-based LDPC codes without the error floor phenomenon over the binary erasure channel (BEC).

## UP-GDBF: A 19.3 Gbps Error Floor Free 4KB LDPC Decoder for NAND Flash Applications

- **Status**: ✅
- **Reason**: A: UP-GDBF, a new error-floor-free GDBF bit-flipping decoder and 16nm HW directly for NAND Flash LDPC.
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9902993
- **Type**: journal
- **Published**: 2022
- **Authors**: Li-Wei Liu, Yen-Chin Liao, Hsie-Chia Chang
- **PDF**: https://ieeexplore.ieee.org/document/9902993
- **Abstract**: An error floor phenomenon, decoding performance, and throughput are three major concerns for LDPC decoders in NAND Flash applications. With a penalty method and an active iteration mechanism, we present a Unified Penalty Gradient Descent Bit Flipping (UP-GDBF) decoding algorithm, which not only possesses error-floor free property but also improves convergence speed in decoding performance. To fulfill the high-throughput requirement while maintaining reliable error correction capability, we propose an energy-based backtracking scheme to reduce 40% latency with a negligible 0.8% area overhead. Implemented in TSMC 16nm process, the proposed 4KB LDPC decoder can achieve a throughput of 19.3 Gbps with 0.120 mm2 area to satisfy ONFI 5.0 throughput requirement. Compared to existing approaches, our decoder architecture provides superior data rate and decoding performance in both 1KB and 4KB LDPC codes.

## A 58.6/91.3 pJ/b Dual-Mode Belief-Propagation Decoder for LDPC and Polar Codes in the 5G Communications Standard

- **Status**: ✅
- **Reason**: 5G LDPC/polar 듀얼모드 BP 디코더 IC — 모듈 공유·메모리 재사용·CNU 설계 등 NAND LDPC HW에 이식 가능(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:9757139
- **Type**: journal
- **Published**: 2022
- **Authors**: Bei-Sheng Su, Chia-Heng Lee, Tzi-Dar Chiueh
- **PDF**: https://ieeexplore.ieee.org/document/9757139
- **Abstract**: This letter presents the first belief propagation (BP) decoder IC implementation for the two forward error correction (FEC) codes in the 5G communication standard. The LDPC mode supports 5G BG2 with 128 lifting size, while the polar mode supports code length  $N = 1024$ . The 40-nm CMOS chip features BP module sharing, memory reuse, check node unit design, forwarding and layer pipelining, and dataflow rearrangement. Compared to two single-mode decoders, this dual-mode decoder saved 37% in the overall die area, 32% in the computation circuit area, and 41% in the memory area. The chip delivers throughputs of 2.38 and 1.85 Gb/s from 0.9-V Vdd with energy efficiencies of 58.6 and 91.3 pJ/b in the LDPC mode and the polar mode, respectively.

## A 38.64-Gb/s Large-CPM 2-KB LDPC Decoder Implementation for nand Flash Memories

- **Status**: ✅
- **Reason**: NAND 플래시용 QC-LDPC 디코더 VLSI 구현, large-CPM 라우팅 혼잡 해소 아키텍처 (A/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9874844
- **Type**: journal
- **Published**: 2022
- **Authors**: Li-Wei Liu, Mu-Hua Yuan, Yen-Chin Liao +1
- **PDF**: https://ieeexplore.ieee.org/document/9874844
- **Abstract**: The routing congestion over a QC-LDPC decoder with a large circular permutation matrix (CPM) size has long been an obstacle to high throughput designs. This paper presents a large-CPM congestion-free decoder for (18396, 16416) quasi-cyclic Euclidean geometry low-density parity-check (QC-EG-LDPC) code in NAND flash application. Considering area efficiency in scheduling schemes and the array dispersion structure, the Array-Disperse Based Dual Variable Node Unit (VNU) Cluster Architecture fully leverages the code structure to support at least two physical channels of the Open NAND Flash Interface 5.0 (ONFI 5.0). In addition, the proposed congestion-aware analysis and implementation method achieve a highly parallel decoder at a 70% utilization ratio. Implemented in TSMC 28nm process, the presented decoder provides 38.64 Gbps throughput at RBER=1.456% Bi-AWGN channel with an area of 2.97 mm2.

## Two Novel Semi-/Auto-Adaptive SNR Algorithms to Efficiently Train Deep Neural SPA Decoders

- **Status**: ✅
- **Reason**: 신경망 SPA 디코더 학습용 적응형 SNR 알고리즘, LDPC에 0.2~0.6dB 개선+학습시간 단축 — 이식 가능 디코더 학습 기법(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9693899
- **Type**: journal
- **Published**: 2022
- **Authors**: Chun-Ming Huang
- **PDF**: https://ieeexplore.ieee.org/document/9693899
- **Abstract**: In the past few years, deep learning has been widely used in various fields due to its outstanding progress. One of the latest applications of deep learning is to use a neural network (NN) with trainable multiplicative weights to design decoders for error-correcting codes. High quality data are essential for deep learning to train robust NN models. In this study, two novel semi-/auto-adaptive SNR algorithms are proposed to efficiently train the neural decoders based on the Sum-Product Algorithm (SPA). For illustration, several neural SPA decoders for the Bose-Chaudhuri-Hocquenghem (BCH) code and low-density parity-check (LDPC) code have been constructed as examples. Simulation results show that, compared with the original neural decoders, the performance of these neural decoders trained by the proposed algorithms can be improved in the range of 0.2 to 0.6 dB. Moreover, the training time required for these decoders to achieve convergence can be reduced by up to 28.8% for the BCH code, and up to 35.6% for the LDPC code, without increasing decoding complexity.

## An LDPC Encoder Architecture With Up to 47.5 Gbps Throughput for DVB-S2/S2X Standards

- **Status**: ✅
- **Reason**: DVB-S2/S2X IRA(바이너리)-LDPC 인코더 HW 아키텍처, 고처리율 FPGA 구현 — D(이식 가능 HW)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:9712323
- **Type**: journal
- **Published**: 2022
- **Authors**: Decai Liu, Yanfei Luo, Yunfeng Li +5
- **PDF**: https://ieeexplore.ieee.org/document/9712323
- **Abstract**: Low-Density Parity-Check (LDPC) code is a type of forward error-correction code with excellent performance, and has been widely used in many modern communication standards. The second-generation satellite broadcasting standard (DVB-S2) and its extension (DVB-S2X) adopt a special Irregular Repeated Accumulate (IRA) LDPC code as inner coding scheme. However, due to the large block size, most of the architectures proposed so far use Random Access Memory (RAM) to store and update the encoding results, and the delay caused by address-controlled read and write operations and barrel shift during computation inevitably limits the upper bound of encoder throughput. In this paper, by extracting the periodicity of the parity-check matrix, we introduce a fast encoding algorithm that can efficiently process the multiplication of the information sequence and a large-dimensional sparse matrix, and propose an encoder architecture with low encoding delay and high throughput. The proposed architecture has been implemented and tested on a Xilinx Kintex-7 FPGA, and the result show that the encoder architecture can achieve the highest throughput of 47.5 Gbps at a clock frequency of 280 MHz.

## Iterative Multihead Multitrack Detection Scheme for Bit-Patterned Media Recording

- **Status**: ✅
- **Reason**: BPMR 반복 등화·복호(IED)에서 LDPC 디코더와 2D PRML 결합 + 트랙별 코드레이트 설계 — 스토리지 ECC 반복복호 기법, 이식 검토 가치(애매시 in)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9937050
- **Type**: journal
- **Published**: 2022
- **Authors**: Gyuyeol Kong, Taehyoung Kim, Minchae Jung
- **PDF**: https://ieeexplore.ieee.org/document/9937050
- **Abstract**: An iterative multihead multitrack detection scheme for bit-patterned media recording is described in this letter. The scheme employs two iterative strategies with multihead, multitrack detection where three tracks are simultaneously processed to accurately estimate the channel with track misregistration (TMR) and effectively detect the data by using intertrack interference (ITI) information with high reliability. The first outer iteration aims to compensate for the TMR effect, and the second inner iteration aims to improve the reliability of the data. In the outer iteration, the TMR effect is compensated by modifying the generalized partial response (GPR) target to a channel that reflects the TMR estimated by a TMR estimator using an expectation and maximization algorithm. In the inner iteration, iterative equalization and decoding (IED) is conducted between the two-dimensional partial response maximum-likelihood detector and the low-density parity check decoder based on the revised GPR target. Since each track has a different channel performance according to the amount of ITI information in the multitrack detection, we design the GPR target and the code rate separately for each track to maximize the overall channel performance. The bit error rate performances of the proposed IED scheme are compared with the conventional IED scheme when the areal density is 2 $\text{Tb/in}^{2}$. Simulation results show that the IED scheme has more than 2 dB gain compared with the conventional IED scheme for 30$\%$ TMR.

## Sliding-Window Turbo Equalization and Its Reduced-Complexity Decoding Techniques

- **Status**: ✅
- **Reason**: SC-LDPC 디코더 기반 sliding-window turbo equalization, P-EXIT 분석 및 복잡도 저감 디코딩 기법 — SC-LDPC 디코딩 기법 이식 가능(C/E), 애매하나 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9761867
- **Type**: journal
- **Published**: 2022
- **Authors**: Sirawit Khittiwitchayakul, Watid Phakphisut
- **PDF**: https://ieeexplore.ieee.org/document/9761867
- **Abstract**: Turbo equalization is a cooperative error-correcting approach to achieve a target bit-error rate over inter-symbol interference channels. In this paper, we proposed a new turbo equalization, called sliding-window turbo equalization (SW-TE), consisting of the Bahl-Cocke-Jelinek-Raviv detector and a spatially coupled, low-density, parity-check decoder. Moreover, the Protograph-based Extrinsic Information Transfer (P-EXIT) chart was modified to investigate the asymptotic behavior of SW-TE. Our analyses showed that SW-TE outperformed conventional turbo equalization in terms of decoding threshold. Based on the P-EXIT chart analysis, we further proposed a guideline of the reduced-complexity decoding techniques for SW-TE, eliminating unnecessary branch metric updates during turbo iterative decoding. Our simulations corroborated the analytical results, showing that SW-TE outperformed conventional turbo equalization while maintaining an acceptable level of complexity.

## Horizontal Layered Scheduling ADMM Penalized Decoder Based on the Improved Penalty Function for LDPC

- **Status**: ✅
- **Reason**: LDPC용 수평 계층 스케줄링 ADMM penalized 디코더+개선 페널티함수 — 새 바이너리 LDPC 디코더 알고리즘(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9961207
- **Type**: journal
- **Published**: 2022
- **Authors**: Biao Wang, Zhongfei Wang
- **PDF**: https://ieeexplore.ieee.org/document/9961207
- **Abstract**: For low-density parity-check (LDPC) codes, reducing the number of Euclidean projections, choosing a suitable scheduling strategy, and devising an improved penalty function are three effective ways to increase the alternating direction method of multipliers (ADMM) penalized decoding speed. By combining the above three ways, this paper proposes a horizontal layered scheduling ADMM penalized decoder based on the improved penalty function to speed up decoding. The experimental data indicate that the proposed decoder can obtain better performance and lower average number of iterations than the existing ADMM penalized decoders.

## Dynamic Error Recovery Flow Prediction Based on Reusable Machine Learning for Low Latency NAND Flash Memory Under Process Variation

- **Status**: ✅
- **Reason**: NAND 플래시 LDPC 다중 디코딩모드 동적 ERF를 ML(전이·메타학습)로 예측해 read latency 감소 — NAND/SSD 직접(A)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9940942
- **Type**: journal
- **Published**: 2022
- **Authors**: Minyoung Hwang, Jeongju Jee, Joonhyuk Kang +3
- **PDF**: https://ieeexplore.ieee.org/document/9940942
- **Abstract**: NAND flash memory is becoming smaller and denser to have a larger storage capacity as technologies related to fine processes are developed. As a side effect of high-density integration, the memory can be vulnerable to circuit-level noise such as random telegraph noise, decreasing the reliability of the memory. Therefore, low-density parity-check code that provides multiple decoding modes is adopted in the NAND flash memory systems to have a strong error correcting capability. Conventional static error recovery flow (ERF) applies decoding modes sequentially, and read latency can increase when preceding decoding modes fail. In this paper, we consider a dynamic ERF using machine learning (ML) that predicts an optimal decoding mode guaranteeing successful decoding and minimum read latency and applies it directly to reduce read latency. Due to process variation incurred in the manufacturing of memory, memory characteristics are different by chips and it becomes difficult to apply a trained prediction model to different chips. Training the customized prediction model at each memory chip is impractical because the computational burden of training is heavy, and a large number of training data is required. Therefore, we consider ERF prediction based on reusable ML to deal with varying input and output relationships by chips due to process variation. Reusable ML methods reuse pre-trained model architecture or knowledge learned from source tasks to adapt the model to perform its task without any loss of performance in different chips. We adopt two reusable ML approaches for ERF prediction based on transfer learning and meta learning. Transfer learning method reuses the pre-trained model by reducing domain shift between a source chip and a target chip using a domain adaptation algorithm. On the other hand, meta learning method learns shared features from multiple source chips during the meta training procedure. Next, the meta-trained model reuses previously learned knowledge to fastly adapt to the different chips. Numerical results validate the advantages of the proposed methods with high prediction accuracy in multiple chips. In addition, the proposed ERF prediction based on transfer and meta learning can yield a noticeable reduction in average read latency as compared to conventional schemes.

## Look-Ahead Bit-Flipping Decoding of MDPC Code

- **Status**: ✅
- **Reason**: Modified bit-flipping decoder for MDPC codes; new hard-decision BF algorithm transferable to NAND LDPC decoding (C).
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9834767
- **Type**: conference
- **Published**: 2022
- **Authors**: H. Kaneko
- **PDF**: https://ieeexplore.ieee.org/document/9834767
- **Abstract**: This paper presents a modified bit-flipping (BF) decoding algorithm for moderate-density parity-check codes using a property of the number of unsatisfied parity checks (NUPCs) in uncorrected error positions. The proposed BF algorithm selects candidate flipping positions using the current NUPC, and then selects one flipping position based on a sum of NUPCs in suspicious positions after tentative flipping of each candidate position. The block error rate (BLER) is evaluated by computer simulation, and the results show that the presented BF algorithm gives lower BLERs compared to existing decoding algorithms.

## Ternary Message Passing Decoding of RS-SPC Product Codes

- **Status**: ✅
- **Reason**: 터너리 메시지패싱 디코딩 알고리즘 + DE 분석 — 바이너리 이미지 RS-SPC 대상, 저복잡도 MP 디코더 기법 이식 가능(C), 애매하여 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9834619
- **Type**: conference
- **Published**: 2022
- **Authors**: M. Zhu, M. Jiang, C. Zhao
- **PDF**: https://ieeexplore.ieee.org/document/9834619
- **Abstract**: This paper presents a ternary message passing (TMP) decoding algorithm for product codes constructed from binary image Reed-Solomon (RS) codes and single-parity-check (SPC) codes. All exchanged messages among component decoders in TMP decoding take value from a ternary alphabet {–1, 0, +1}, which gives a potential for designing fast decoders. In particular, intersymbol interference (ISI) channels are considered due to their applications in many high-speed systems. Moreover, we propose the density evolution (DE) analysis for RS-SPC product codes over AWGN and ISI channels. The DE analyses and simulation results show RS-SPC product codes under TMP decoding performs well in various channels.

## Fully Analog Noise-Resilient Dynamical Systems Storing Binary Sequence

- **Status**: ✅
- **Reason**: 패리티검사행렬 기반 아날로그 경사하강 디코딩 동역학 — 이식 가능한 새 디코더 아키텍처(C/D) 후보, 애매하여 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9834448
- **Type**: conference
- **Published**: 2022
- **Authors**: T. Wadayama
- **PDF**: https://ieeexplore.ieee.org/document/9834448
- **Abstract**: This paper presents fully analog noise-resilient dynamical systems for storing a binary sequence. The proposed dynamical system is a gradient descent dynamical system based on a potential energy function defined based on a parity check matrix of a binary linear code. We assume that the dynamical system operates with stochastic disturbances such as thermal noises. We formulate the whole system, including stochastic disturbances, using stochastic differential equations (SDE). From a discretized stochastic difference equation, i.e., the Euler-Maruyama equation, we can study the covariance evolution of error vectors regarding the random walk of the system state around an equilibrium state. Some numerical evaluations for the (7,4) Hamming code and related codes indicate the robustness of the proposed dynamical system against the stochastic disturbances.

## Code-Aware Storage Channel Modeling via Machine Learning

- **Status**: ✅
- **Reason**: A: NAND 플래시 채널 모델링(ML 생성모델)으로 부호 설계 보조 — NAND ECC 직접 관련, 코딩 설계 도구
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9965920
- **Type**: conference
- **Published**: 2022
- **Authors**: S. Zheng, P. H. Siegel
- **PDF**: https://ieeexplore.ieee.org/document/9965920
- **Abstract**: With the reduction in device size and the increase in cell bit-density, NAND flash memory suffers from larger inter-cell interference (ICI) and disturbance effects. Constrained coding can mitigate the ICI effects by avoiding problematic error-prone patterns, but designing powerful constrained codes requires a comprehensive understanding of the flash memory channel. Recently, we proposed a modeling approach using conditional generative networks to accurately capture the spatio-temporal characteristics of the read signals produced by arrays of flash memory cells under program/erase (P/E) cycling. In this paper, we introduce a novel machine learning framework for extending the generative modeling approach to the coded storage channel. To reduce the experimental overhead associated with collecting extensive measurements from constrained program/read data, we train the generative models via transferring knowledge from models pre-trained with pseudo-random data. This technique can accelerate the training process and improve model accuracy in reconstructing the read voltages induced by constrained input data throughout the flash memory lifetime. We analyze the quality of the model by comparing flash page bit error rates (BERs) derived from the generated and measured read voltage distributions. We envision that this machine learning framework will serve as a valuable tool in flash memory channel modeling to aid the design of stronger and more efficient coding schemes.

## Graph-based codes for hierarchical recovery

- **Status**: ✅
- **Reason**: Tanner/graph-based codes with hierarchical locality and stopping-set analysis for erasure recovery — code-design technique (E) potentially portable to storage LDPC.
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9834902
- **Type**: conference
- **Published**: 2022
- **Authors**: A. Beemer, R. Kshirsagar, G. L. Matthews
- **PDF**: https://ieeexplore.ieee.org/document/9834902
- **Abstract**: In this paper, we consider approaches to designing Tanner codes to protect against symbol loss from multiple erasures. First, we note that Tanner codes inherit locality and availability from their inner codes, allowing one to design longer codes with specified locality and availability. Availability is desirable in that multiple disjoint repair groups increase the likelihood that symbols are available to repair erased ones. Even so, particular patterns of erasures well-distributed across the repair groups may prevent recovery. Hence, we consider an alternative using hierarchical locality which implements tiered recovery, where the tier utilized depends on the number of erasures. Finally, we define hierarchical stopping sets to characterize local message-passing decoder failure at the various repair levels.

## ECC-Aided RAID for Reliability Improvement of SSD

- **Status**: ✅
- **Reason**: 3-bit MLC NAND 대상 ECC-aided RAID, soft-decision 협력 ECC 디코딩으로 정정능력 향상 — NAND/SSD ECC 직접(A/B)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10000968
- **Type**: conference
- **Published**: 2022
- **Authors**: K. Lee, G. Yu, Y. Hwang +3
- **PDF**: https://ieeexplore.ieee.org/document/10000968
- **Abstract**: In the field of solid state drive (SSD), redundant array of inexpensive disk (RAID) is of great use due to its reliability and performance. In terms of reliability, RAID can be further enhanced with the help of error-correction code (ECC), which is another core technology for SSD applications. Recently, joint ECC-RAID schemes have been proposed for the reliability of SSD. Especially, due to high reliability with low computational complexity, joint ECC-RAID schemes based on RAID-5, denoted as ECC-RAID-5, are popularly adopted to devices as well as systems of data storage. In this paper, a new family of joint ECC-RAID schemes, called ECC-aided RAID (EA-RAID), are proposed to further improve the reliability of the joint ECC-RAID schemes in the data storage applications. In the EA-RAID, new types of data checking and regenerating algorithms based on soft-decision (SD) are introduced to enhance the error-correcting capability of the cooperative ECC decoding. The EA-RAID increases error-correction capability as at least 15% and 7% gain compared with the ECC-only schemes and the conventional ECC-RAID-5, respectively. The improvement is demonstrated by productized SSD based on virtuaI3-bit-over multi-level cell (MLC) NAND. It is expected that the proposed technologies can be introduced as a potential solution for next generation NAND.

## A new type of ultimate-Shannon-limit channel codes

- **Status**: ✅
- **Reason**: protograph 기반 LDPC-Hadamard 코드, 새 코드 구성 — 바이너리 LDPC 코드설계 신기여(E), 이식 가능성 있음
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9943021
- **Type**: conference
- **Published**: 2022
- **Authors**: F. C. M. LAU
- **PDF**: https://ieeexplore.ieee.org/document/9943021
- **Abstract**: In most existing digital communication systems, the received signal strength is usually larger than the noise level. Alternatively, the bit-energy-to-noise-power-spectral-density (Eb/N0) is assumed to be greater than 0 dB. However, in some specific applications such as deepspace communications and quantum key distribution, the received signal power is smaller than the noise power. Under such circumstances, strong error correction codes are required to provide a reliable link between the transmitter and the receiver. In this talk, a new type of error-correction code called “protograph-based low-density parity-check Hadamard codes” is introduced. The codes are shown to provide excellent error performance not only when Eb/N0 is smaller than 0 dB, but also when Eb/N0 approaches the ultimate Shannon limit -1.59 dB.

## Neural Belief Propagation Auto-Encoder for Linear Block Code Design

- **Status**: ✅
- **Reason**: Neural BP-like 디코더와 선형블록부호 공동학습 오토인코더, 이식 가능 신경망 디코더 (C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9896912
- **Type**: journal
- **Published**: 2022
- **Authors**: G. Larue, L. -A. Dufrene, Q. Lampin +2
- **PDF**: https://ieeexplore.ieee.org/document/9896912
- **Abstract**: The growing number of Internet of Thing (IoT) and Ultra-Reliable Low Latency Communications (URLCC) use cases in next generation communication networks calls for the development of efficient Forward Error Correction (FEC) mechanisms. These use cases usually imply using short to mid-sized information blocks and requires low-complexity and/or fast decoding procedures. This paper investigates the joint learning of short to mid block-length coding schemes and associated Belief-Propagation (BP) like decoders using Machine Learning (ML) techniques. An interpretable auto-encoder (AE) architecture is proposed, ensuring scalability to block sizes currently challenging for ML-based linear block code design approaches. By optimizing a coding scheme w.r.t. the targeted decoder, the proposed system offers a good complexity/performance trade-off compared to various codes from literature with length up to 128 bits.

## High-Throughput and Energy-Efficient VLSI Architecture for Ordered Reliability Bits GRAND

- **Status**: ✅
- **Reason**: ORBGRAND 고처리율 VLSI 아키텍처 — 임의 코드 적용 가능한 이식형 디코더 HW(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9732212
- **Type**: journal
- **Published**: 2022
- **Authors**: S. M. Abbas, T. Tonnellier, F. Ercan +2
- **PDF**: https://ieeexplore.ieee.org/document/9732212
- **Abstract**: Ultrareliable low-latency communication (URLLC), a major 5G new-radio (NR) use case, is the key enabler for applications with strict reliability and latency requirements. These applications necessitate the use of short-length and high-rate channel codes. Guessing random additive noise decoding (GRAND) is a recently proposed maximum likelihood (ML) decoding technique for these short-length and high-rate codes. Rather than decoding the received vector, GRAND tries to infer the noise that corrupted the transmitted codeword during transmission through the communication channel. As a result, GRAND can decode any code, structured or unstructured. GRAND has hard-input as well as soft-input variants. Among these variants, ordered reliability bits GRAND (ORBGRAND) is a soft-input variant that outperforms hard-input GRAND and is suitable for parallel hardware implementation. This work reports the first hardware architecture for ORBGRAND, which achieves an average throughput of up to 42.5 Gb/s for a code length of 128 at a target frame error rate (FER) of 10−7. Furthermore, the proposed hardware can be used to decode any code as long as the length and rate constraints are met. In comparison to the GRAND with ABandonment (GRANDAB), a hard-input variant of GRAND, the proposed architecture enhances decoding performance by at least 2 dB. When compared to the state-of-the-art fast dynamic successive cancellation flip decoder (Fast-DSCF) using a 5G polar code (PC) (128, 105), the proposed ORBGRAND VLSI implementation has  $49\times $  higher average throughput,  $32\times $  times more energy efficiency, and  $5\times $  more area efficiency while maintaining similar decoding performance.

## Iterative Hard-Decision Decoding Algorithms for Binary Reed-Muller Codes

- **Status**: ✅
- **Reason**: 바이너리 RM 코드용 반복 비트플리핑(BF/NBF/MBF) 경판정 디코더 — bit-flipping 계열은 NAND LDPC 저복잡도 디코더로 이식 가능, 애매하므로 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9789141
- **Type**: journal
- **Published**: 2022
- **Authors**: Y. -T. Ni, D. N. Nguyen, F. -K. Liao +2
- **PDF**: https://ieeexplore.ieee.org/document/9789141
- **Abstract**: In this paper, novel hard-decision iterative decoding algorithms for binary Reed-Muller (RM) codes are presented. First, two algorithms are devised based on the majority-logic decoding algorithm with reliability measures of the received sequence. The bit-flipping (BF) and the normalized bit-flipping (NBF) decoding algorithms are hard-decision decoding algorithms. According to the updated hard reliability measures, the BF and NBF algorithms flip one bit of the received hard-decision sequence at a time in each iteration. The NBF decoding algorithm performs better than the BF decoding algorithm by normalizing the reliability measures of the information bits. Moreover, the BF and NBF algorithms are modified to flip multiple bits in one iteration to reduce the average number of iterations. The modified decoding algorithms are called the multiple-bits-flipping (MBF) algorithm and the normalized multiple-bits-flipping (NMBF) algorithm, respectively. The proposed algorithms have low computational complexities and can converge rapidly after a small number of iterations. The simulation results show that the proposed hard-decision decoding algorithms outperform the conventional decoding algorithm.

## A Code Rate-Compatible High-Throughput Hardware Implementation Scheme for QKD Information Reconciliation

- **Status**: ✅
- **Reason**: QC-LDPC+puncturing rate-compatible 화해 알고리즘과 NMSA HLS 구현(ZCU102, 136Mbps); QKD지만 고전 바이너리 LDPC 디코더/HW 기법 이식 가능(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9707626
- **Type**: journal
- **Published**: 15 June15,
- **Authors**: Ming Zhu, Ke Cui, Simeng Li +3
- **PDF**: https://ieeexplore.ieee.org/document/9707626
- **Abstract**: For high-speed quantum key distribution (QKD) post processing, information reconciliation is the most computational step, which usually acts as the system speed bottleneck. Reconciliation efficiency and operation throughput are the two most important performance parameters, but they are often compromised to each other in actual realization due to the available hardware resources. Another characteristic of the information reconciliation is that its channel is time-varying, and in order to guarantee high efficiency, some rate-compatible error correction scheme should be adopted. To cope with the above problems, this paper proposes a rate-compatible high-efficiency reconciliation algorithm based on quasi-cyclic (QC) low-density parity-check (LDPC) codes and puncturing algorithms. On the other hand, in order to obtain high throughput while maintaining low implementation complexity, the normalized min-sum algorithm (NMSA) is realized and optimized by using the fast prototyping tool of high-level synthesis (HLS). The proposed information reconciliation module was implemented on the Xilinx Zynq Ultrascale+ ZCU102 development board. Experimental results show that the maximum throughput rate of the implemented reconciliation module in this paper can reach 136 Mbps, while the efficiency factor is kept lower than 1.32 across the error rate range of 1.7%∼10.6% under the remaining frame error rate level of 10−3. The comprehensive good performance obtained by our design can strongly support the development of modern high-speed QKD systems.

## Speed up QC-LDPC decoder through memory subsystem optimization

- **Status**: ✅
- **Reason**: QC-LDPC 디코더 메모리 서브시스템 최적화·ASIP/SIMD 병렬화로 throughput 개선 — 이식 가능 HW 아키텍처(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:9750799
- **Type**: conference
- **Published**: 14-16 Jan.
- **Authors**: Yajie Li, Dake Liu, Xinbing Zhou +1
- **PDF**: https://ieeexplore.ieee.org/document/9750799
- **Abstract**: In this paper, we proposed a QC-LDPC decoder for 5G NR, WiMAX, and WLAN applications. The decoder can flexibly support arbitrary code length and rate under 5G NR standard. This design follows programmable ASIP (Application Specific Instruction-set Processor) design method and uses data parallel SIMD (Single Instruction Multiple Data) architecture. We doubled the logic computing speed to improve the throughout instead of using double speed memory architecture. Compared with the design mentioned in [1], the original design could achieve the highest QC-LDPC decoding throughput of 533Mbps (12 SISO in parallel) when the clock frequency is 200MHz (memory clock frequency is 400MHz). The existing design saved 47% of the decoding clock cycle without lossing decoding circuit quality. We achieved a maximum QC-LDPC decoding throughput of 1984 Mbps (with 48 SISO in parallel) when the system frequency is 400MHz (memory clock frequency is also 400MHz). Further, through circuit optimization, the upper limit of the system clock is promoted from 344MHz to 1.1GHz. The throughput can possibly be upto 5456Mbps. Finally, through the logic synthesis using 28nm SMIC CMOS cell library, the design is physically verified, and the logic gate count is reported 1716K. It is similar to that of the original design per SISO.
