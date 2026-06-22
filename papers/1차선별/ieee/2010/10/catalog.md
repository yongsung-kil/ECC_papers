# IEEE Xplore — 2010-10 (1차선별 통과)


## Constructing Short-Length Irregular LDPC Codes with Low Error Floor

- **Status**: ✅
- **Reason**: PEG-ACSE 신규 코드 구성으로 trapping set/error floor 저감 - 바이너리 LDPC 코드설계(E), NAND error floor에 직접 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5567183
- **Type**: journal
- **Published**: October 20
- **Authors**: Xia Zheng, Francis C. M. Lau, Chi K. Tse
- **PDF**: https://ieeexplore.ieee.org/document/5567183
- **Abstract**: Trapping sets (TSs) are known to cause error floors in regular and irregular low-density parity-check (LDPC) codes. By avoiding major error-contributing TSs during the code construction process, codes with low error floors can effectively be built. In it has been shown that TSs labeled as [w;u] are considered as being equivalent under the automorphism of the graph and are therefore contributing equally to the error floor. However, TSs with the same label [w;u] are not identical in general, particularly for the case of irregular LDPC codes. In this paper, we introduce a parameter e that can identify the number of "distinguishable" cycles in the connected subgraph induced by an elementary trapping set. Further, we propose a code construction algorithm, namely the Progressive-Edge-Growth Approximate-minimum-Cycle-Set-Extrinsic-message-degree (PEG-ACSE) method, that aims to avoid small elementary trapping sets (ETSs), particularly detrimental ETSs. We also develop theorems evaluating the minimum possible ETSs formed by PEG construction algorithms in general. We compare the characteristics of the codes built using the proposed method and those built using PEG-only or PEG-Approximate-minimum-Cycle-Extrinsic-message-degree (PEG-ACE) methods. Results from simulations show that the codes constructed using the proposed PEG-ACSE method produce lower error rates, particularly at the high signal-to-noise (SNR) region, compared with codes constructed using other PEG-based algorithms.

## Iterative Decoding Threshold Analysis for LDPC Convolutional Codes

- **Status**: ✅
- **Reason**: LDPC convolutional(SC-LDPC) 임계값 분석·density evolution — 이식 가능 바이너리 코드설계(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5571910
- **Type**: journal
- **Published**: Oct. 2010
- **Authors**: Michael Lentmaier, Arvind Sridharan, Daniel J. Costello +1
- **PDF**: https://ieeexplore.ieee.org/document/5571910
- **Abstract**: An iterative decoding threshold analysis for terminated regular LDPC convolutional (LDPCC) codes is presented. Using density evolution techniques, the convergence behavior of an iterative belief propagation decoder is analyzed for the binary erasure channel and the AWGN channel with binary inputs. It is shown that for a terminated LDPCC code ensemble, the thresholds are better than for corresponding regular and irregular LDPC block codes.

## QSN—A Simple Circular-Shift Network for Reconfigurable Quasi-Cyclic LDPC Decoders

- **Status**: ✅
- **Reason**: QC-LDPC 재구성형 circular-shift network(QSN) HW — permutation network 아키텍처(D), NAND QC-LDPC 디코더 직접 이식
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:5587879
- **Type**: journal
- **Published**: Oct. 2010
- **Authors**: Xiaoheng Chen, Shu Lin, Venkatesh Akella
- **PDF**: https://ieeexplore.ieee.org/document/5587879
- **Abstract**: There is an increasing need for configurable quasi-cyclic low-density parity-check (QC-LDPC) decoders that can support a family of structurally compatible codes instead of a single code. The key component in a configurable QC-LDPC decoder is a programmable circular-shift network that supports cyclic shifts of any size up to a predefined maximum submatrix size. This paper presents a QC-LDPC shift network (QSN), which has two key advantages over state-of-the-art solutions in recent literature. First, the QSN reduces the number of stages in the critical path, which improves the clock frequency and makes it scalable, particularly in a field-programmable gate array (FPGA)-based implementation where an interconnect delay is dominant. Second, the QSN's control logic is simple to generate and occupies a significantly smaller area. The QSNs for a variety of codes suitable for emerging applications are implemented, targeting both a 180-nm Taiwan Semiconductor Manufacturing Company Ltd. complimentary metal-oxide-semiconductor library and a Xilinx Virtex 4 FPGA. The proposed implementation is shown to be 2.1 times faster than the best known implementation in literature and requires almost eight times less control area. Furthermore, this paper presents analytical models of the critical-path and datapath complexity for arbitrary-sized submatrices and proves that the QSN indeed generates all the output combinations required for implementing reconfigurable QC-LDPC decoders.

## A Multimode Shuffled Iterative Decoder Architecture for High-Rate RS-LDPC Codes

- **Status**: ✅
- **Reason**: RS-LDPC 멀티모드 셔플드 디코더 HW(configurable permutator, 노드 분할 critical-path 단축) - 부호 비의존 디코더/HW 기법 NAND 이식 가능(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5464385
- **Type**: journal
- **Published**: Oct. 2010
- **Authors**: Yeong-Luh Ueng, Chung-Jay Yang, Kuan-Chieh Wang +1
- **PDF**: https://ieeexplore.ieee.org/document/5464385
- **Abstract**: For an efficient multimode low-density parity-check (LDPC) decoder, most hardware resources, such as permutators, should be shared among different modes. Although an LDPC code constructed based on a Reed-Solomon (RS) code with two information symbols is not quasi-cyclic, in this paper, we reveal that the structural properties inherent in its parity-check matrix can be adopted in the design of configurable permutators. A partially parallel architecture combined with the proposed permutators is used to mitigate the increase in implementation complexity for the multimode function. The high check-node degree of a high-rate RS-LDPC code leads to challenges in the efficient implementation of a high-throughput decoder. To overcome this difficulty, the variable nodes have been partitioned into several groups, and each group is processed sequentially in order to shorten the critical-path delay and hence increase the maximum operating frequency. In addition, shuffled message-passing decoding is adopted, since fewer iterations can be used to achieve the desired bit-error-rate performance. In order to demonstrate the usefulness of the proposed flexible-permutator-based architecture, one single-mode rate-0.84 decoder and two multimode decoders whose code rates range between 0.79 and 0.93 have been implemented. These decoders can achieve multigigabit-per-second throughput. Using the proposed architecture to support lower rate RS-LDPC codes, e.g., rate-0.568 code, is also investigated.

## Interior Point Decoding for Linear Vector Channels Based on Convex Optimization

- **Status**: ✅
- **Reason**: convex 최적화 기반 interior point LDPC 디코딩 신규 알고리즘 - 부호 비의존 디코더(C), 바이너리 LDPC BP 대안으로 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5571870
- **Type**: journal
- **Published**: Oct. 2010
- **Authors**: Tadashi Wadayama
- **PDF**: https://ieeexplore.ieee.org/document/5571870
- **Abstract**: In the present paper, a novel decoding algorithm for low-density parity-check (LDPC) codes based on convex optimization is presented. The decoding algorithm, which is referred to hereinafter as interior point decoding, is designed for linear vector channels. The linear vector channels include several practically important channels, such as inter-symbol interference channels and partial response (PR) channels. It is shown that the maximum likelihood decoding (MLD) rule for a linear vector channel can be relaxed to a convex optimization problem, which is called a relaxed MLD problem. The proposed decoding algorithm is based on a numerical optimization technique known as the interior point method with barrier functions. Approximate variations of an interior point method based on the gradient descent and Newton methods are used to solve the relaxed MLD problem. Compared with a conventional joint message-passing decoder, from computer simulations, it is observed that the proposed decoding algorithm achieves better BER performance on PR channels with less decoding complexity in several cases. Furthermore, an extension of the proposed algorithm for high-order modulation formats, such as PAM and QAM, is presented.

## An Area-Efficient and Low-Power Multirate Decoder for Quasi-Cyclic Low-Density Parity-Check Codes

- **Status**: ✅
- **Reason**: QC-LDPC용 저면적/저전력 멀티레이트 디코더 칩, normalized min-sum+양자화+메시지패싱 재배치 - 이식 가능 HW 아키텍처(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:5229115
- **Type**: journal
- **Published**: Oct. 2010
- **Authors**: Bo Xiang, Rui Shen, An Pan +2
- **PDF**: https://ieeexplore.ieee.org/document/5229115
- **Abstract**: The quasi-cyclic low-density parity-check (QC-LDPC) codes are widely applied in digital broadcast and communication systems. However, the decoders are still difficult to be put into practice due to their large area and high power, especially in the wireless mobile devices. This paper presents an improved all-purpose multirate iterative decoder architecture for QC-LDPC codes, which can largely reduce their area and power. The architecture implements the normalized min-sum algorithm, rearranges the original two-phase message-passing flow, and adopts an efficient quantization method for the second minimum absolute values, an optimized storing scheme for the position indexes and signs, and an elaborate clock gating technique for substantive memories and registers. It is also configurable for any regular and irregular QC-LDPC codes, and can be easily tuned up to different code rates and code word lengths. The chip is fabricated in an SMIC 0.18- six-metal-layer standard CMOS technology. It attains a throughput of 104.5 Mb/s, and dissipates an average power of 486 mW at 125 MHz, and 15 decoding iterations. The core area is only 9.76 mm2. The chip has been applied into the China digital terrestrial/television multimedia broadcasting system.

## Architecture and finite precision optimization for layered LDPC decoders

- **Status**: ✅
- **Reason**: layered LDPC 유한정밀도/양자화 최적화 HW(C/D), 메모리 축소 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5624816
- **Type**: conference
- **Published**: 6-8 Oct. 2
- **Authors**: Cédric Marchand, Laura Conde-Canencia, Emmanuel Boutillon
- **PDF**: https://ieeexplore.ieee.org/document/5624816
- **Abstract**: Layered decoding is known to provide efficient and high-throughput implementation of LDPC decoders. In the practical hardware implementation of layered decoders, the performance is strongly affected by quantization. The finite precision model determines the area of the decoder, which is mainly composed of memory, especially for long frames. To be specific, in the DVB-S2,-T2 and -C2 standards, the memory can occupy up to 70% of the total area. In this paper, we focus our attention on the optimization of the number of quantization bits. Message saturation and memory size optimization are considered for the case of a DVB-S2 decoder. We show that the memory area can be reduced by 28% compared to the state-of-the-art, without performance loss.

## Impact of LLR saturation and quantization on LDPC min-sum decoders

- **Status**: ✅
- **Reason**: LLR 양자화/saturation이 min-sum 디코더에 미치는 영향 분석(A/C), NAND LLR 양자화에 직결
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5624882
- **Type**: conference
- **Published**: 6-8 Oct. 2
- **Authors**: N. Kanistras, I. Tsatsaragkos, I. Paraskevakos +2
- **PDF**: https://ieeexplore.ieee.org/document/5624882
- **Abstract**: In this paper we quantify the power of noise due to quantization and saturation of the LLRs. Subsequently a model is constructed using the obtained noise power expressions that can be used to estimate the performance of various LLR quantization schemes. The model is validated by comparing the estimation with experimental BER results for an LDPC-based system that uses the min-sum layered decoding algorithm.

## Error performance and decoder hardware comparison between EG-LDPC and BCH codes

- **Status**: ✅
- **Reason**: EG-LDPC layered bit-flipping 디코더 HW 비교(C/D), 바이너리 LDPC 디코더 기법 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5624877
- **Type**: conference
- **Published**: 6-8 Oct. 2
- **Authors**: Jonghong Kim, Junho Cho, Wonyong Sung
- **PDF**: https://ieeexplore.ieee.org/document/5624877
- **Abstract**: Low-density parity-check (LDPC) codes are promising for low code rate applications, however its competitiveness over BCH codes in the high code rate region is not well studied. In this work, we compare the Euclidean geometry (EG) LDPC and BCH codes of the length 1,023, 4,095, and 16,383 that have the code rates of 0.75~0.85. Hard-decision input data are applied to both decoders, and the EG-LDPC codes are decoded using the layered bit-flipping (BF) algorithm. Since the number of needed iterations for LDPC decoding depends on the channel condition, both decoders are designed to have the similar minimum throughput. Not only error performance but also hardware complexity and power consumption of these decoders are compared.

## A BER performance-aware early termination scheme for layered LDPC decoder

- **Status**: ✅
- **Reason**: layered LDPC early termination 기법(C), BER 손실 없는 종료로 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5624881
- **Type**: conference
- **Published**: 6-8 Oct. 2
- **Authors**: Xiongxin Zhao, Zhixiang Chen, Xiao Peng +2
- **PDF**: https://ieeexplore.ieee.org/document/5624881
- **Abstract**: This paper presents a novel early termination scheme for layered LDPC decoder. By solving the bit error rate (BER) performance degradation which will occur when other early termination schemes are applied in layered LDPC decoder, the proposed method achieves very fast termination speed without BER performance loss. It is the best solution for BER performance-aware layered LDPC decoders, such as satellite video broadcasting applications.

## Applying transparent lossless data compression to improve the feasibility of using advanced error correction codes in solid-state drives

- **Status**: ✅
- **Reason**: NAND 플래시 LDPC soft decoding 직접(A), 압축으로 read latency 절감
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5624760
- **Type**: conference
- **Published**: 6-8 Oct. 2
- **Authors**: Ningde Xie, Guiqiang Dong, Tong Zhang
- **PDF**: https://ieeexplore.ieee.org/document/5624760
- **Abstract**: As advanced error correction codes (ECC) which support soft decoding is suggested to use in the future NAND flash memories, the requirement of sensing and transferring multi-bit soft information from the flash cells to controller will incur a large read access latency. This paper proposes to exploit the lossless compressibility of files in LDPC coded NAND flash memories to reduce such latency overhead, other than saving storage space as in conventional practice. The key idea is to apply run-time lossless data compression to enable an opportunistic use of a stronger LDPC code with more coding redundancy, and trade such opportunistic extra error correction capability to allow more coarser-grained memory sensing and hence lead to less read response speed overhead without sacrificing the overall performance. Since the basic operation of NAND flash is typically realized in the unit of page (e.g., 4KB user data per page in the current NAND flash), we only apply this strategy to each individual page independently in order to be completely transparent to the firmware, operating systems and users. This paper quantitatively studies the effectiveness of this design strategy in 2bits/cell NAND flash memories. Results in the case study show that with this design strategy, up to 95.24% on-chip memory sensing latency reduction and 66.67% flash-to-controller data transfer latency can be achieved respectively.

## Toward realtime side information decoding on multi-core processors

- **Status**: ✅
- **Reason**: 멀티코어 BP 병렬화(Sum-Product/Min-Sum/Algorithm E) 디코더 가속 기법, 부호 비의존적 BP 병렬화로 이식 가능(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5662040
- **Type**: conference
- **Published**: 4-6 Oct. 2
- **Authors**: Svetislav Momcilovic, Yige Wang, Shantanu Rane +1
- **PDF**: https://ieeexplore.ieee.org/document/5662040
- **Abstract**: Most distributed source coding schemes involve the application of a channel code to the signal and transmission of the resulting syndromes. For low-complexity encoding with superior compression performance, graph-based channel codes such as LDPC codes are used to generate the syndromes. The encoder performs simple XOR operations, while the decoder uses belief propagation (BP) decoding to recover the signal of interest using the syndromes and some correlated side information. We consider parallelization of BP decoding on general-purpose multi-core CPUs. The motivation is to make BP decoding fast enough for realtime applications. We consider three different BP decoding algorithms: Sum-Product BP, Min-Sum BP and Algorithm E. The speedup obtained by parallelizing these algorithms is examined along with the tradeoff against decoding performance. Parallelization is achieved by dividing the received syndrome vectors among different cores, and by using vector operations to simultaneously process multiple check nodes in each core. While Min-Sum BP has intermediate decoding complexity, a “vectorized” version of Min-Sum BP performs nearly as fast as the much simpler Algorithm E with significantly fewer decoding errors. Our experiments indicate that, for the best compromise between speed and performance, the decoder should use Min-Sum BP when the side information is of good quality and Sum-Product BP otherwise.

## Bit Flipping-Sum Product Algorithm for regular LDPC codes

- **Status**: ✅
- **Reason**: Sum-Product+Bit-Flipping 결합 신규 디코딩 알고리즘(BFSP), 동일복잡도로 BER 개선. 이식 가능 디코더(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5656207
- **Type**: conference
- **Published**: 30 Sept.-2
- **Authors**: R. El Alami, C. B. Gueye, M. Boussetta +2
- **PDF**: https://ieeexplore.ieee.org/document/5656207
- **Abstract**: In this paper we present Low Density Parity Check decoding algorithm that assemble two different algorithms: Sum-Product and Bit-Flipping; we denote Bit Flipping-Sum Product Algorithm (BFSP). To reduce the bit error rate, we perform the Bit-Flipping algorithm after the Sum-Product algorithm. Simulation results over an additive white Gaussian channel show that the error performance of a LDPC codes with Bit Flipping-Sum Product decoding is within 0.2 dB of the standard Sum-Product decoding algorithms. Furthermore, the decoding complexity of the proposed BFSP algorithm is maintained at the same level as that of the standard Sum-Product algorithm.

## A Novel Low Complexity LDPC Encoder Based on Optimized RU Algorithm with Backtracking

- **Status**: ✅
- **Reason**: RU 인코딩 알고리즘에 backtracking 추가한 신규 저복잡도 인코더+FPGA 구현(D), NAND LDPC 인코딩 이식 가능
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:5631468
- **Type**: conference
- **Published**: 29-31 Oct.
- **Authors**: Xiangran Sun, Zhibin Zeng, Zhanxin Yang
- **PDF**: https://ieeexplore.ieee.org/document/5631468
- **Abstract**: We present a low-complexity high-efficiency LDPC encoder, based on classic method of Richardson and Urbanke with a novel backtracking algorithm, which we propose to substitute greedy algorithm for approximate triangulation with sparse matrix of LDPC codes. For the LDPC code in CMMB, for example, the complexity of encoding is reduced effectively, and an implementation of LDPC encoder for two different code rate (1/2 and 3/4) on Altera Stratix II EP1S180F102014 can achieve encoding rate 34 Mbps and 69 Mbps.

## The design of rate-compatible protograph LDPC codes

- **Status**: ✅
- **Reason**: protograph 확장 기반 rate-compatible 바이너리 LDPC 신규 구성법(E), NAND ECC 코드 설계에 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5706880
- **Type**: conference
- **Published**: 29 Sept.-1
- **Authors**: Thuy Van Nguyen, Aria Nosratinia, Dariush Divsalar
- **PDF**: https://ieeexplore.ieee.org/document/5706880
- **Abstract**: This paper presents a simple yet powerful method for designing embedded rate-compatible families of LDPC codes. Rate compatible codes are essential for many communication applications, e.g. hybrid automatic repeat request (HARQ) systems, and their design is nontrivial due to the difficulty of simultaneously guaranteeing the quality of several related codes. Puncturing can be used to generate rate-compatible LDPC codes, but it produces a gap to capacity that, in practice, often significantly exceeds the gap of the mother code. We propose an alternative method based on successively extending a high-rate protograph. The resulting codes not only inherit the advantages of protograph codes, namely low encoding complexity and efficient decoding algorithms, but also cover a wide range of rates and have very good performance with thresholds that are all within 0.15 dB of their capacity limits.

## A decoding algorithm for LDPC codes over erasure channels with sporadic errors

- **Status**: ✅
- **Reason**: erasure+sporadic error용 SEME 디코딩 알고리즘을 LDPC ML erasure 디코더에 통합—패리티검사 희소성 활용 신규 디코더 기법(C/B), 바이너리
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5706942
- **Type**: conference
- **Published**: 29 Sept.-1
- **Authors**: Gianluigi Liva, Enrico Paolini, Balazs Matuz +1
- **PDF**: https://ieeexplore.ieee.org/document/5706942
- **Abstract**: An efficient decoding algorithm for low-density parity-check (LDPC) codes on erasure channels with sporadic errors (i.e., binary error-and-erasure channels with error probability much smaller than the erasure probability) is proposed and its performance analyzed. A general single-error multiple-erasure (SEME) decoding algorithm is first described, which may be in principle used with any binary linear block code. The algorithm is optimum whenever the non-erased part of the received word is affected by at most one error, and is capable of performing error detection of multiple errors. An upper bound on the average block error probability under SEME decoding is derived for the linear random code ensemble. The bound is tight and easy to implement. The algorithm is then adapted to LDPC codes, resulting in a simple modification to a previously proposed efficient maximum likelihood LDPC erasure decoder which exploits the parity-check matrix sparseness. Numerical results reveal that LDPC codes under efficient SEME decoding can closely approach the average performance of random codes.

## Short column-weight-three LDPC codes without small trapping sets

- **Status**: ✅
- **Reason**: E: column-weight-3 바이너리 LDPC를 trapping set 회피로 구성, error floor 개선 — NAND ECC 코드설계 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5706904
- **Type**: conference
- **Published**: 29 Sept.-1
- **Authors**: Dung Viet Nguyen, Martin Leslie, Bane Vasić
- **PDF**: https://ieeexplore.ieee.org/document/5706904
- **Abstract**: We introduce a method to construct regular column-weight-three low-density parity-check (LDPC) codes with low error floors for the sum product algorithm (SPA) on the binary symmetric channel (BSC). The Tanner graphs of these codes are free of certain small trapping sets. These trapping sets are selected from the Trapping Set Ontology for the Gallager A/B decoder and are selected based on their relative harmfulness for the SPA. We evaluate the relative harmfulness of different trapping sets for the SPA by using the topological relations among them and by analyzing decoding failures on one trapping set in the presence or absence of other trapping sets. To the best of our knowledge, these codes outperform the best known short length, regular column-weight-three LDPC codes.

## Reweighted LP decoding for LDPC codes

- **Status**: ✅
- **Reason**: C: 바이너리 LDPC용 reweighted LP 디코딩 신규 알고리즘 — 부호 비의존 디코더 기법 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5706905
- **Type**: conference
- **Published**: 29 Sept.-1
- **Authors**: M. Amin Khajehnejad, Alexandros G. Dimakis, Babak Hassibi +1
- **PDF**: https://ieeexplore.ieee.org/document/5706905
- **Abstract**: We introduce a novel algorithm for decoding binary linear codes by linear programming. We build on the LP decoding algorithm of Feldman et al. and introduce a post-processing step that solves a second linear program that reweights the objective function based on the outcome of the original LP decoder output. Our analysis shows that for some LDPC ensembles we can improve the provable threshold guarantees compared to standard LP decoding. We also show significant empirical performance gains for the reweighted LP decoding algorithm with very small additional computational complexity.

## A design of nonprime block irregular LDPC codes via CRT

- **Status**: ✅
- **Reason**: CRT 기반 nonprime sub-matrix QC-LDPC 구성법(임의 블록길이 지원) — 바이너리 코드설계(E) 신규 기여, NAND 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5665144
- **Type**: conference
- **Published**: 26-29 Oct.
- **Authors**: Chalit Chusin, Chutima Prasartkaew, Sekson Timakul +1
- **PDF**: https://ieeexplore.ieee.org/document/5665144
- **Abstract**: This paper presents a new design of irregular LDPC codes that supports arbitrary block length. We propose the efficient construction method when nonprime size sub-matrices are used. The problem where GCD (L1,L2) ≠ 1 that left unsolved has been tackled. We also consider the case GCD (L1,L2) = 1 but L1 or L2 is a nonprime number. The results show that our designed codes have superior performance compared to MAC. The resulted codes still hold the attractive properties of LDPC codes. The performances of interleaved codes are higher than noninterleaved codes and it goes higher as SNR is increased.

## Construction of protograph LDPC codes based on Jacket matrices

- **Status**: ✅
- **Reason**: Jacket 행렬 기반 protograph LDPC 신규 구성+girth-4 회피(E) — 바이너리 LDPC 코드설계 기여
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5656484
- **Type**: conference
- **Published**: 24-28 Oct.
- **Authors**: Kaiyao Wang, Shaohai Hu, Yang Xiao +2
- **PDF**: https://ieeexplore.ieee.org/document/5656484
- **Abstract**: In this paper, we propose a method to construct the protograph LDPC codes based on Jacket matrices. In the proposed code construction, the Jacket matrices are regarded as derived protograph matrices, the column weights of permutation matrices in parity check matrix depend on the elements' values of Jacket matrices. While the shift rule of the permutation matrices needs to ensure no girth 4. The proposed LDPC codes are easy to be applied for the codec of mobile digital multimedia. The simulation results in AWGN channels show that the BER performance of the proposed codes is better by about 0.5 dB than that of GB20600 LDPC codes.

## An efficient stopping criterion of LDPC decoding for optical transmission

- **Status**: ✅
- **Reason**: 신규 early stopping criterion(check 식+hard decision 결합, check-node 업데이트 파이프라인)(C/D) — 디코더/HW 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5778466
- **Type**: conference
- **Published**: 24-27 Oct.
- **Authors**: Ming Jiang, Jinfang Dou
- **PDF**: https://ieeexplore.ieee.org/document/5778466
- **Abstract**: The stopping criterion based on parity-check constraints is an inherent advantage of low-density parity-check (LDPC) codes. However, the parity-check computation with signs of the posterior information costs additional hardware or decoding delays, which may be a particular problem for the full-parallel LDPC decoding in optical transmission. Furthermore, the performance degradation caused by using simplified stopping criterions should also be considered, where the maximum number of the iterations is usually limited by the very high decoding speed in optical transmission. In this paper, we propose an efficient early stopping criterion with the consideration of the complexity/performance tradeoffs. The new method is based an intelligent combination of check equations and temporary hard decisions, and can be pipelined with check-node updating, thus leading to lower complexity and power consumption, which are desirable for both optical and wireless communications. Simulation results show that the hybrid criterion not only achieves the same performance as the conventional stopping criterions, but also provides a noticeable gain for the other simplified stopping criterions.

## Application of vectorization loop in the process of LDPC code decoding

- **Status**: ✅
- **Reason**: BP 반복디코딩의 벡터화 루프로 디코딩 속도 향상 — 디코더 구현/병렬화 기법(C/D) 이식 가능, 애매하므로 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5622592
- **Type**: conference
- **Published**: 22-24 Oct.
- **Authors**: Jian-Bing Han, Chen He, He Yun He
- **PDF**: https://ieeexplore.ieee.org/document/5622592
- **Abstract**: In the process of decoding emulation of LDPC code, belief propagation algorithm is adopted. According to this iterative decoding algorithm, a new vectorization idea is proposed, integrating iterative process and vector operation. Compared with use of simple loop statement, it has improved decoding speed greatly.

## An effective puncturing scheme for rate-compatible LDPC codes

- **Status**: ✅
- **Reason**: rate-compatible LDPC용 새 펑처링 패턴(MSCN, 생존 체크노드 최대화) → 바이너리 코드 설계 기법으로 이식 가능(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5632510
- **Type**: conference
- **Published**: 21-23 Oct.
- **Authors**: He-Guang Su, Ming-Qiu Wang, Shu-Tao Xia
- **PDF**: https://ieeexplore.ieee.org/document/5632510
- **Abstract**: We consider the problem of finding good puncturing patterns for rate-compatible LDPC codes over additive white Gaussian noise (AWGN) channels. When studying the recovered process of punctured nodes, Ha et al maximized the number of lower Ä-SR nodes and obtained a so-called grouping and sorting puncturing scheme, where only single survived check node was guaranteed. In this paper, we investigate the effect of multiple survived check nodes and afford theoretical analysis to them. Based on the analysis, we propose an effective puncturing scheme called MSCN, which maximizes the number of survived check nodes. The MSCN scheme is quite different from the grouping and sorting scheme in the rules of finding nodes and update. By simulations, the MSCN scheme is shown to be superior to the grouping and sorting scheme over AWGN channels at low rates for rate-compatible LDPC codes.

## An improved variable length coding scheme using structured LDPC codes

- **Status**: ✅
- **Reason**: 구조화 LDPC 코드설계(E): shortening/puncturing+lifting, cycle/ACE 스펙트럼 고려한 PEG base-matrix 설계 — 바이너리 LDPC 신규 구성으로 NAND 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5633982
- **Type**: conference
- **Published**: 21-23 Oct.
- **Authors**: Ming Jiang, Chen Wang, Yuan Zhang +1
- **PDF**: https://ieeexplore.ieee.org/document/5633982
- **Abstract**: This paper proposes an improved coding scheme for various transmission lengths by combining shortening and puncturing with the conventional lifting method. Considering both of cycle conditions and ACE spectrum, we design the base-matrix in the framework of PEG construction. Only one base-matrix is required to support a wide rage of coding lengths for our proposed scheme, where the lifting factors are set in non-uniformly distributed values. The transmission configurations with arbitrary lengths within the coding range can be achieved by shortening and puncturing. Moreover, our proposed scheme provides better error performance than the traditional structured LDPC codes lifted by many different factors, when the shortening and puncturing patters are optimally selected by numerical methods.

## An improved HARQ scheme based on irregular LDPC coding

- **Status**: ✅
- **Reason**: 불규칙 LDPC 기반 Type-II HARQ에서 노드 차수별 패리티 비트 재전송 순서 설계 → 바이너리 불규칙 LDPC 구성/rate-compatible 기법으로 이식 가능성 있어 애매하므로 살림(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5633746
- **Type**: conference
- **Published**: 21-23 Oct.
- **Authors**: Long Guo, Youyun Xu, Wenfeng Ma +1
- **PDF**: https://ieeexplore.ieee.org/document/5633746
- **Abstract**: The hybrid auto repeat request (HARQ) is an efficient retransmission technique which can guarantee highly reliable communication over noisy channels, and nowadays it has been widely adopted in packet-based data communication systems. In this paper, we propose an improved Type-II Hybrid-ARQ scheme that can degrade the average number of the iteration and improve the performance. In this scheme, the source transmits the whole codeword to the destination, and only the parity bits are retransmitted, if the decoder fails. Irregular LDPC codes, which have different degrees, are utilized in the proposed HARQ scheme. Before the retransmission, the parity bits have been treated as a set of bits specified by the node's degrees. The nodes with same degree are classified into one subset. When the retransmissions are needed, only the parity bits are retransmitted, and the subset which has the larger degree is transmitted firstly, then the smaller subset is transmitted. The simulation results demonstrate that the proposed HARQ scheme can outperform the Type-II HARQ scheme.

## Good high-rate π-rotation LDPC codes based on novel puncturing techniques

- **Status**: ✅
- **Reason**: π-rotation LDPC 고부호율 puncturing 기법—바이너리 코드설계/구성(E) 신규 기여
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5649442
- **Type**: conference
- **Published**: 17-20 Oct.
- **Authors**: Rich Echard, Shih-Chun Chang
- **PDF**: https://ieeexplore.ieee.org/document/5649442
- **Abstract**: In this paper we introduce puncturing techniques to produce high-rate π-rotation low-density parity-check (LDPC) codes. The techniques rely on symmetry considerations to maintain simple description and to achieve excellent performance. We also extend the bounds on the minimum d2 for the high-rate codes.

## Adaptive quantization for low-density-parity-check decoders

- **Status**: ✅
- **Reason**: LDPC 디코더 적응적 양자화로 양자화 비트수 절감 — NAND LLR 양자화에 직접 이식 가능(A/C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5649830
- **Type**: conference
- **Published**: 17-20 Oct.
- **Authors**: Cha-Hao Chung, Yeong-Luh Ueng, Ming-Che Lu +1
- **PDF**: https://ieeexplore.ieee.org/document/5649830
- **Abstract**: For the implementation of low-density parity-check (LDPC) decoders, the associated error performance and the complexity are significantly affected by the number of quantization bits used. In this paper, we propose an adaptive quantization scheme, which uses different quantization schemes at different iteration numbers based on a fixed number of quantization bits. Simulation results show that the proposed adaptive quantization can reduce the number of quantization bits without error performance degradation.

## Low-density parity-check accumulate codes

- **Status**: ✅
- **Reason**: 바이너리 LDPC+accumulator 직렬연접 신규 코드 설계, error floor 개선·HW 친화 인코딩·DE 임계 — 코드설계 이식 가능(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5650090
- **Type**: conference
- **Published**: 17-20 Oct.
- **Authors**: Chung-Li Wang, Shu Lin
- **PDF**: https://ieeexplore.ieee.org/document/5650090
- **Abstract**: This paper presents a class of high-rate codes called low-density parity-check accumulate (LDPCA) codes. The code design is the serial concatenation of an LDPC outer code and an accumulator with an interleaver. The iterative decoding for the LDPCA code design has complexity linear to the code length. When using regular LDPC codes with column weight 2, the proposed codes have low encoding complexity and are advantageous for hardware implementation. Simulation results show that the regular LDPCA codes have the same error performance with the regular LDPC codes at the waterfall region and outperform product accumulate codes at the error floor region. The investigation on weight distributions proves that regular LDPCA codes have the asymptotic minimum distance proportional to the code length. In addition, iterative decoding thresholds under density evolution are obtained with a Gaussian approximation.

## Optimization of memory utilization for partially parallel QC-LDPC decoder

- **Status**: ✅
- **Reason**: 부분병렬 QC-LDPC 디코더 메모리 최적화(efficient chunk/predictor), 이식 가능 HW 아키텍처(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:5650137
- **Type**: conference
- **Published**: 17-20 Oct.
- **Authors**: Tsung-Che Wu, Yao-Wen Hu, Chang-Ming Lee
- **PDF**: https://ieeexplore.ieee.org/document/5650137
- **Abstract**: Quasi-cyclic (QC) low-density parity-check (LDPC) codes have advantages over other types of LDPC codes due to their cyclic shifting property. In this paper, a partially parallel QC-LDPC decoder with efficient memory design is proposed. To improve the memory utilization, the structures of efficient chunk and predictor are realized. The efficient chunk can store parts of check-to-variable messages. This design can effectively reduce the memory requirement. Furthermore, the predictor verifies variable-to-check messages and updates efficient chunks instantly. With less check-to-variable messages and variable-to-check messages stored in the memory, this decoding architecture only deposits few messages in several efficient chunks, such that the cost of memory is less. Eventually, the proposed approach dramatically reduces memory requirement about 65% compared to the traditional method while maintaining the same low-cost.

## Detailed evaluation of error floors of LDPC codes using the probabilistic algorithm

- **Status**: ✅
- **Reason**: 트래핑셋/error floor FER 정밀 평가법(확률·중요도 샘플링), error floor 분석으로 코드설계에 이식(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5654357
- **Type**: conference
- **Published**: 17-20 Oct.
- **Authors**: Masanori Hirotomo, Masakatu Morii
- **PDF**: https://ieeexplore.ieee.org/document/5654357
- **Abstract**: The performance of LDPC codes decoded by iterative algorithm depends on the structural properties of their underlying Tanner graphs. For discrete memoryless channels, error patterns dominating the frame error rate (FER) in the error floor region are termed trapping set. We have shown approximate examinations of small trapping sets of LDPC codes using the probabilistic algorithm. In this paper, we propose an efficient method for the detailed evaluation of the FER of LDPC codes in the error floor region. The accuracy of the FER lies on the failure probability of the number of trapping sets determined by our probabilistic algorithm and the FER estimated by the importance sampling.

## A new construction of irregular LDPC convolutional codes with cycle removal

- **Status**: ✅
- **Reason**: 불규칙 LDPC-CC 신규 구성 + length-8 cycle 제거 절차, 이식 가능 코드설계(E, 바이너리)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5650164
- **Type**: conference
- **Published**: 17-20 Oct.
- **Authors**: Chi-Jen Wu, Chung-Hsuan Wang, Chi-chao Chao
- **PDF**: https://ieeexplore.ieee.org/document/5650164
- **Abstract**: In this paper, a new construction of irregular low-density parity-check convolutional codes (LDPC-CCs) is presented. Both upper and lower bounds on the free distance are derived as well. Compared with previously constructed irregular LDPC-CCs, our design can not only avoid a girth less than 8 but also provide an enlarged free distance. Since some undesired cycles occur due to the binomial terms in the parity-check matrices of general LDPC-CCs, we provide a specific procedure to remove this kind of length-8 cycles. It can also be applied to our irregular construction. Simulation results show that the codes based on the new construction and the cycle-removal procedure can achieve better bit-error-rate performance and a lower error-floor.

## Importance sampling for LDPC codes based on optimal simulation probability density function

- **Status**: ✅
- **Reason**: LDPC importance sampling 고속 시뮬레이션(최적 PDF)—error floor 평가 도구로 이식 가능, 애매하여 in
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5649219
- **Type**: conference
- **Published**: 17-20 Oct.
- **Authors**: Takakazu Sakai, Koji Shibata
- **PDF**: https://ieeexplore.ieee.org/document/5649219
- **Abstract**: This paper shows a fast simulation method of low-density parity-check (LDPC) codes by using importance sampling (IS). In IS, the design of the simulation probability density function (PDF) plays a very important role to reduce the simulation time. We derive the optimal simulation PDF, which can reduce the variance of the estimator to zero. Since the optimal simulation PDF includes true error probability, it can not be utilized in the practical simulation. The simulation PDF which approximates the optimal simulation PDF is proposed. In addition, we show some numerical examples to show the effectiveness of the proposed simulation method.

## Circulant decomposition: Cyclic, quasi-cyclic and LDPC codes

- **Status**: ✅
- **Reason**: 순환 패리티검사행렬 분해로 새 cyclic/QC-LDPC 코드 구성—바이너리 코드설계(E) 신규 기여
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5649214
- **Type**: conference
- **Published**: 17-20 Oct.
- **Authors**: Qin Huang, Qiuju Diao, Shu Lin
- **PDF**: https://ieeexplore.ieee.org/document/5649214
- **Abstract**: This paper shows that a cyclic code can be put into quasi-cyclic form by decomposing a circular parity-check matrix through column and row permutations. Such a decomposition of a circular parity-check matrix of a cyclic code produces a group of shorter cyclic or quasi-cyclic codes and leads to a new method for constructing long cyclic codes from short cyclic codes. Also in this paper, new classes of cyclic and quasi-cyclic LDPC codes are derived from cyclic Euclidean geometry LDPC codes by decomposing their circular parity-check matrices. These new LDPC codes perform well and enlarge the repertoire of cyclic and quasi-cyclic LDPC codes.

## An iterative decoding algorithm for rate-compatible punctured low-density parity-check codes of high coding rates

- **Status**: ✅
- **Reason**: RCP-LDPC 고부호율 punctured bit 복구 반복 디코딩 알고리즘—BP 변형 디코더(C) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5649247
- **Type**: conference
- **Published**: 17-20 Oct.
- **Authors**: Gou Hosoya, Hideki Yagi, Manabu Kobayashi
- **PDF**: https://ieeexplore.ieee.org/document/5649247
- **Abstract**: An iterative decoding algorithm of rate-compatible punctured low-density parity-check (RCP-LDPC) codes of high coding rates is developed. This algorithm performs a predetermined recovering process of punctured bits sums at the beginning of each iteration of the standard belief-propagation (BP) decoding algorithm. By propagating messages of two punctured bits sum, this algorithm can recover much more punctured bits than the standard BP decoding algorithm. It is shown that the proposed algorithm is applicable for RCP-LDPC codes of higher coding rates with little increase of decoding complexity.

## Analysis of Quasi-Cyclic LDPC codes under ML decoding over the erasure channel

- **Status**: ✅
- **Reason**: QC-LDPC를 ML 디코딩에 맞춰 행/열 permutation으로 pseudo-band 변형, 복잡도 감소 — 바이너리 LDPC 디코더/구성 이식 가능(C/E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5649581
- **Type**: conference
- **Published**: 17-20 Oct.
- **Authors**: Mathieu Cunche, Valentin Savin, Vincent Roca
- **PDF**: https://ieeexplore.ieee.org/document/5649581
- **Abstract**: In this paper, we show that over the binary erasure channel, Quasi-Cyclic LDPC codes can efficiently accommodate the hybrid iterative/ML decoding. We demonstrate that the quasi-cyclic structure of the parity-check matrix can be advantageously used in order to significantly reduce the complexity of the ML decoding. This is achieved by a simple row/column permutation that transforms a QC matrix into a pseudo-band form. Based on this approach, we propose a class of QC-LDPC codes with almost ideal error correction performance under the ML decoding, while the required number of row/symbol operations scales as k√k, where k is the number of source symbols.

## Error-trellis state complexity of LDPC convolutional codes based on circulant matrices

- **Status**: ✅
- **Reason**: QC순환행렬 기반 LDPC convolutional 코드의 error-trellis state 복잡도 축소(행 시프트)—코드 구조/구성 기법(E) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5648981
- **Type**: conference
- **Published**: 17-20 Oct.
- **Authors**: Masato Tajima, Koji Okino, Takashi Miyagoshi
- **PDF**: https://ieeexplore.ieee.org/document/5648981
- **Abstract**: Let H(D) be the parity-check matrix of an LDPC convolutional code corresponding to the parity-check matrix H of a QC code obtained using the method of Tanner et al. We see that the entries in H(D) are all monomials and several rows (columns) have monomial factors. Let us cyclically shift the rows of H. Then the parity-check matrix H'(D) corresponding to the modified matrix H' defines another convolutional code. However, its free distance is lower-bounded by the minimum distance of the original QC code. Also, each row (column) of H'(D) has a factor different from the one in H(D). We show that the statespace complexity of the error-trellis associated with H'(D) can be significantly reduced by controlling the row shifts applied to H with the error-correction capability being preserved.

## A novel low complexity LDPC encoder based on RU algorithm with dynamic programming

- **Status**: ✅
- **Reason**: RU 인코더의 근사 삼각화에 동적계획법을 도입한 저복잡도 인코더 + FPGA 구현 — 코드설계/HW 기여로 이식 가능(D/E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5647849
- **Type**: conference
- **Published**: 16-18 Oct.
- **Authors**: Xiangran Sun, Zhibin Zeng, Zhanxin Yang
- **PDF**: https://ieeexplore.ieee.org/document/5647849
- **Abstract**: In this paper, we present a low-complexity high-efficiency LDPC encoder, based on classic method of Richardson and Urbanke with a novel dynamic programming algorithm, which we propose to substitute greedy algorithm for approximate triangulation with sparse matrix of LDPC codes. For the LDPC code in CMMB, for example, the complexity of encoding is reduced effectively, and an implementation of LDPC encoder for two different code rate (1/2 and 3/4) on Altera Stratix II EP1S180F102014 can achieve encoding rate 34 Mbps and 69 Mbps.

## Data conflict resolution for layered LDPC decoding algorithm by selective recalculation

- **Status**: ✅
- **Reason**: layered LDPC 디코딩의 data conflict를 선택적 재계산으로 해결 — 부호 비의존적 디코더 스케줄링 기법으로 NAND LDPC 디코더에 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5647529
- **Type**: conference
- **Published**: 16-18 Oct.
- **Authors**: Wen Ji, Makoto Hamaminato, Hiroshi Nakayama +1
- **PDF**: https://ieeexplore.ieee.org/document/5647529
- **Abstract**: Layered LDPC decoding algorithm is known to achieve high Bit Error Rate (BER) performance and high throughput for LDPC decoders. However, for ISDB-S2 (Integrated Services Digital Broadcasting via Satellite - Second Generation) LDPC decoder, applying layered algorithm directly will result in data conflict problem. In this paper, a novel selective recalculation method is proposed to solve the data conflict problem. It determines the inaccurately calculated values based on a recalculation decision rule, and correct them accordingly. By applying this selective recalculation method, the layered algorithm can achieve conflict free BER performance. Simulation results demonstrate that the proposed method can achieve 0.1dB gain for the code with most conflicts in ISDB-S2, under the same BER performance compared to the previous strategy to solve data conflict problem.

## Regular Quasi-cyclic LDPC Codes with Girth 6 from Prime Fields

- **Status**: ✅
- **Reason**: prime field 기반 girth-6 regular QC-LDPC 구성법 제안(E), 바이너리 코드설계 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5635634
- **Type**: conference
- **Published**: 15-17 Oct.
- **Authors**: Qingji Zheng, Xiangxue Li, Dong Zheng +1
- **PDF**: https://ieeexplore.ieee.org/document/5635634
- **Abstract**: The short paper proposes a method for constructing regular quasi-cyclic (QC) LDPC codes based on circulant permutation matrices via simple prime field operations. The main advantage is that regular QC LDPC codes with a variety of block lengths and rates can be easily constructed which have no cycles of length four or less. Simulation results show that within only a maximum of ten decoding iterations of sum-product algorithm(SPA) the constructed regular codes of high rates have no error floor down to the bit-error rate of 10-7.
