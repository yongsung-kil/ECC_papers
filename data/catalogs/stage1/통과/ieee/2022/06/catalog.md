# IEEE Xplore — 2022-06 (1차선별 통과)


## Some Short-Length Girth-8 QC-LDPC Codes From Primes of the Form t2 + 1

- **Status**: ✅
- **Reason**: girth-8 QC-LDPC 단길이 대수적 구성 신규 기법, 바이너리 코드설계 기여 — 이식 가능 (E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9734044
- **Type**: journal
- **Published**: June 2022
- **Authors**: Inseon Kim, Tetsuya Kojima, Hong-Yeop Song
- **PDF**: https://ieeexplore.ieee.org/document/9734044
- **Abstract**: We propose a simple algebraic construction for girth-8 regular QC-LDPC codes of short lengths, a few hundreds, based on the square matrix from some prime integers of the form  $t^{2}+1=P$  and a multiplication table method. We generalize the conventional multiplication table method in a way that the size  $T$  of the circular permutation matrix (CPM) can be different from the modulus  $M$  in the calculation of the exponent matrix. We classify and suggest the parameters  $P\leq M\leq T$  with  $M=kP$  so that the resulting codes have girth 8. In particular, we prove the existence of a threshold  $T_{0}$  so that the resulting code will always have girth 8 if  $T > T_{0}$  is used, given that  $M=kP$ . Finally, we present various simulation results and theoretical analysis, one of which shows that the proposed codes of length around 250 have an additional coding gain of about 0.4 dB over the 5G NR LDPC codes.

## A Low Bit-Width LDPC Min-Sum Decoding Scheme for NAND Flash

- **Status**: ✅
- **Reason**: NAND 플래시용 저비트폭 QC-LDPC row-layered normalized min-sum 개선(최소·차소값 진폭 제한) — A/C 직접 부합.
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9496601
- **Type**: journal
- **Published**: June 2022
- **Authors**: Lanlan Cui, Xiaojian Liu, Fei Wu +2
- **PDF**: https://ieeexplore.ieee.org/document/9496601
- **Abstract**: For NAND flash memory, designing a good low-density parity-check (LDPC) decoding algorithm could ensure data reliability. When the decoding algorithm is implemented in hardware, it is necessary to achieve an attractive tradeoff between implementation complexity and decoding performance. In this article, a novel low-bit-width decoding scheme is introduced. In this scheme, the quasi-cyclic LDPC (QC-LDPC) is used, and the row-layered normalized min-sum algorithm is improved by restricting the amplitude of minimum and second-minimum values in each check node (CN) updating. The simulation shows that our approach achieves a lower uncorrectable bit error rate (UBER) with a negligible increase in computational complexity, especially with low-precision input log-likelihood ratio (LLR).

## Sliding Window Decoding for QC-SC-LDPC Codes Under the Constraint of Implementation Complexity

- **Status**: ✅
- **Reason**: QC-SC-LDPC 슬라이딩 윈도우 디코딩 최적 윈도우 크기+조기종료, 바이너리 LDPC 디코더/코드설계 신규 기여 (C/E 이식 가능)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9690704
- **Type**: journal
- **Published**: June 2022
- **Authors**: Zhitong He, Kewu Peng, Jian Song +1
- **PDF**: https://ieeexplore.ieee.org/document/9690704
- **Abstract**: Sliding window decoding has been employed as the decoding scheme of quasi-cyclic spatially-coupled low-density parity-check (QC-SC-LDPC) codes, with the decoding latency and complexity independent of the coupling length but proportional to the window size. The window size was empirically chosen at least three times the constraint length in previous works, which results in the preference of QC-SC-LDPC codes with small constraint length, to reduce the decoding latency and complexity in practical systems. However, the code design freedom and the decoder throughput are limited for these QC-SC-LDPC codes. In this paper, the optimal window size under the constraint of practical decoding complexity is analyzed employing multi-edge-type density evolution (MET-DE). It can be verified from the MET-DE analytical result that the optimal window size could achieve less than twice the constraint length for several edge spreading patterns, which largely loose this restriction in practical code design. Furthermore, it could be observed that besides the constraint length, the specific structure of the edge spreading pattern could affect the optimal window size as well, and thus the MET-DE analytical method for the optimal window size could effectively guide the design of QC-SC-LDPC codes in practical systems. Then an improved sliding window decoding scheme is proposed, including the optimal choice of window size and a parity-check based early termination scheme. Finally, the performance and robustness of the proposed sliding window decoding scheme for QC-SC-LDPC codes are demonstrated via simulation, with the decoding complexity at most twice as that of the conventional LDPC coded schemes.

## Exploiting Uncorrectable Data Reuse for Performance Improvement of Flash Memory

- **Status**: ✅
- **Reason**: 플래시 retention/refresh 시 ECC parity 재계산·remapping 기법(ApproxRefresh, RFR) — NAND/SSD 컨트롤러·ECC 직접(A).
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9496603
- **Type**: journal
- **Published**: June 2022
- **Authors**: Jinhua Cui, Cheng Liu, Junwei Liu +2
- **PDF**: https://ieeexplore.ieee.org/document/9496603
- **Abstract**: With the increased density and the technology scaling, flash memory is more vulnerable to noise effects, overwhelmingly lowering the data retention time. The periodic data refresh technique is commonly used to retain the long-term data integrity. However, the frequent refresh requests introduce the increased access conflict and severe write amplification, leading to suboptimal performance and lifetime improvement of flash memory-based storage systems. In this article, we propose ApproxRefresh, which enables the uncorrectable data reuse with the assistance of approximate-computing applications to reduce the refresh costs. Specifically, we design a lightweight remapping-free refresh technique, called RFR, to periodically correct, compute an enhanced ECC, and only remap new ECC parity bits, which dramatically reduces the refresh costs. Then, with approximate-read and precise-read hotness awareness, ApproxRefresh selectively adopts RFR or the traditional remapping-based refresh technique to reduce the refresh costs and the read disturbance. Besides, ApproxRefresh further improves flash access performance based on data hotness and process variations. In addition, a corresponding ApproxRefresh-aware garbage collection algorithm is proposed to complete the design. Evaluations show that ApproxRefresh reduces the refresh latency by 36.19% over the state of the art.

## On the Decoding Performance of Spatially Coupled LDPC Codes With Sub-Block Access

- **Status**: ✅
- **Reason**: Sub-block 접근 SC-LDPC 디코딩 임계값 분석, 데이터 스토리지 응용 명시 — 코드설계/디코더 기법 이식 가능 (B/C/E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9716111
- **Type**: journal
- **Published**: June 2022
- **Authors**: Eshed Ram, Yuval Cassuto
- **PDF**: https://ieeexplore.ieee.org/document/9716111
- **Abstract**: We study spatially coupled LDPC codes that allow access to sub-blocks much smaller than the full code block. Sub-block access is realized by a semi-global decoder that decodes a chosen target sub-block by only accessing the target, plus a prescribed number of helper sub-blocks adjacent in the code chain. This paper develops a theoretical methodology for analyzing the semi-global decoding performance of spatially coupled LDPC codes constructed from protographs. The main result shows that semi-global decoding thresholds can be derived from certain thresholds we define for the single-sub-block graph. These characterizing thresholds are also used for deriving lower bounds on the decoder’s performance over channels with variability across sub-blocks, which are motivated by applications in data storage.

## An FPGA Implementation of Two-Input LUT Based Information Bottleneck LDPC Decoders

- **Status**: ✅
- **Reason**: D/C: information bottleneck LUT 기반 QC-LDPC 디코더의 FPGA HW 구현(min-sum 대비 우수), NAND LDPC 디코더 HW로 직접 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9837601
- **Type**: conference
- **Published**: 8-10 June 
- **Authors**: Bo-Yu Tseng, Brian M. Kurkoski, Philipp Mohr +1
- **PDF**: https://ieeexplore.ieee.org/document/9837601
- **Abstract**: A lookup table-based check and variable node are considered for designing low-density parity check (LDPC) decoder architectures, using the principle of the information bottleneck method. It has been shown that an information bottleneck LUT operation can outperform conventional minsum arithmetic operation in terms of error-correction capability. This paper presents a cost-efficient hardware implementation of LUT-based node processing units in the decoder architecture. It exploits the symmetry of the communication channel and multi-input LUT decomposition to generate a reduced-size LUT structure. The LUT operations are designed as a two-level memory subsystem enabling LUT mappings reconfiguration at runtime. As a case study, a rate-7/10 7650-bit regular QC-LDPC decoder is implemented on an FPGA, achieving a throughput of up to 1.345 Gbps at 10 iterations. Compared with the conventional offset min-sum decoder, the proposed decoder increases the throughput-to-area ratio up to 39.22% at a cost of no more than 0.08 dB decoding performance loss. In addition, the hardware complexities of node design variants are investigated.

## 550 Gbps Fully Parallel Fully Unrolled LDPC Decoder in 28 nm CMOS Technology

- **Status**: ✅
- **Reason**: D — fully unrolled fully parallel min-sum LDPC 디코더 28nm CMOS, 4-bit 양자화 등 NAND로 이식 가능한 HW 아키텍처
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:9815814
- **Type**: conference
- **Published**: 7-10 June 
- **Authors**: A. Hasani, L. Lopacinski, G. Panic +1
- **PDF**: https://ieeexplore.ieee.org/document/9815814
- **Abstract**: A fully unrolled fully parallel decoding architecture for Low-Density Parity-Check (LDPC) codes is proposed in this paper. Specifically, the iterations of a min-sum decoding scheme are also unrolled and each is implemented with a separate dedicated hardware. The proposed architecture implemented in a 28 nm CMOS technology is able to achieve the throughput of 550 Gbps, occupying an area of 4.98mm2. These results are accomplished with 4-bit quantization of the min-sum decoding messages and six iterations in the case of a (648,540)-LDPC code from IEEE 802.11n. The results show improvements compared with the adaptive degeneration [1] and finite-alphabet [2] decoding algorithms, in terms of both throughput and chip area.

## Protograph-based LDPC codes with chordless short cycles and large minimum distance

- **Status**: ✅
- **Reason**: Protograph LDPC 무현 짧은사이클 제거로 최소거리 향상 — 이식 가능 코드 설계(E), 트래핑셋/girth 신규 기여
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9817675
- **Type**: conference
- **Published**: 5-8 June 2
- **Authors**: Farzane Amirzade, Mohammad-Reza Sadeghi, Daniel Panario
- **PDF**: https://ieeexplore.ieee.org/document/9817675
- **Abstract**: Controlling small size trapping sets and short cycles can result in LDPC codes with large minimum distance $d_{\min}$. We prove that short cycles with a chord are the root of several trapping sets and eliminating these cycles increases $d_{\min}$. We show that the lower bounds on $d_{\min}$ of an LDPC code with chordless short cycles, girth 6 and column weights $\gamma$ is $2\gamma$. This is a significant improvement compared to the existing bounds $\gamma+1$ • Several exponent matrices of protograph-based LDPC codes with chordless short cycles are proposed for any type of pro-tographs, single-edge and multi-edge. These numerical results as well as simulations show that the removal of short cycles with a chord improves previous results in the literature.

## SAPA: Sparse Affine Projection Algorithm in ADMM-LP Decoding of LDPC Codes

- **Status**: ✅
- **Reason**: SAPA: ADMM-LP 디코딩 근사 투영 간소화 — 이식 가능 디코더 알고리즘, 고처리량 신규 기여(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9817674
- **Type**: conference
- **Published**: 5-8 June 2
- **Authors**: Amirreza Asadzadeh, Masoud Barakatain, Stark. C. Draper +1
- **PDF**: https://ieeexplore.ieee.org/document/9817674
- **Abstract**: We present a simplified alternating direction method of multipliers with linear programming (ADMM-LP) decoder for LDPC codes by developing a method of approximate projection onto the parity polytope. The algorithm projects onto the affine hull of the $X$ closest local codewords for each check of degree d, where $X$ can be much smaller than d. We name this SAPA, the “sparse affine projection algorithm”. In contrast to exact projection, SAPA does not require a water-filling step and thus can be implemented with lower per-iteration complexity. We present numerical results which demonstrate not only that SAPA's performance, when used as part of an overall decoder, is close to that of exact projection, but also that the use of SAPA does not incur many additional iterations. This is in contrast to other approximate algorithms. Thus, SAPA is appropriate for use in limited-iteration decoders in high-throughput applications. Moreover, we analyze sparsity of polytope projections in the exact ADMM-LP decoding to explain the suitability of the proposed sparse approximation.

## Single-Minimum LDPC Decoding Offset Optimization Methods

- **Status**: ✅
- **Reason**: Single-minimum 양자화 min-sum 디코더 오프셋 최적화+DE — 이식 가능 디코더 알고리즘 신규 기여(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9817664
- **Type**: conference
- **Published**: 5-8 June 2
- **Authors**: Daniel B. Dermont, Jérémy Nadal, François Leduc-Primeau
- **PDF**: https://ieeexplore.ieee.org/document/9817664
- **Abstract**: Low-density parity-check codes are widely used in communication systems. To meet the high throughput and energy efficiency requirements of current and future systems, it is desirable to further simplify the decoder. Quantized min-sum (MS) decoders are of particular interest for their low implementation complexity, which can be further reduced by computing a single minimum (SM) during check node update, instead of two. However, this simplification can lead to poor decoding performance unless it is carefully incorporated. In this paper, we formalize a general optimization problem for SM decoding, and propose search heuristics to solve it. In addition, we provide density evolution (DE) equations for the first two decoding iterations that properly take into account the lack of extrinsic update rule, and show that this DE result can be used to obtain good solutions to the SM optimization problem with low computational complexity.

## Check-ratio-aided Layer-based Rescaling ANMSA and Its Application for 5G-NR LDPC Codes

- **Status**: ✅
- **Reason**: min-sum 변형(CL-RANMSA) 새 디코더 알고리즘 — NAND LDPC 디코더로 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9824284
- **Type**: conference
- **Published**: 30 May-3 J
- **Authors**: Ziqi Zhou, Kewu Peng, Zhitong He
- **PDF**: https://ieeexplore.ieee.org/document/9824284
- **Abstract**: As a kind of iterative decoding algorithms based on belief propagation (BP), sum-product algorithm (SPA) is capacity-approaching but scale-variant. Currently, however, excellent performance and great stability are still incompatible for min-sum algorithm (MSA) and its improvements. To remedy above problems, we firstly introduce the concept of rescaling, and disclose the causes of the performance loss of MSA. Then introduce the asymptotic optimal decoding algorithm, as well as the suboptimal one. Finally, a more practicable algorithm is proposed, called check-ratio-aided layer-based rescaling adaptive normalized MSA (CL-RANMSA). Compared with the first two algorithms, CL-RANMSA is both capacity-approaching and characteristically robust. In particular, the practicably optimal factors for base graph 2 in 5G new radio low-density parity check (5G-NR LDPC) codes are provided. Simulations are also carried out whose results depict its scale-invariance and excellent performance.

## CRC-Aided Adaptive Belief Propagation Decoding of NR LDPC Codes

- **Status**: ✅
- **Reason**: CRC 보조 적응형 BP(CA-ABP) 디코딩 — 이식 가능 디코더 알고리즘 개선(C), 바이너리 LDPC
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9860767
- **Type**: conference
- **Published**: 19-22 June
- **Authors**: Xianwen Zhang, Ming Jiang, Mingyang Zhu +2
- **PDF**: https://ieeexplore.ieee.org/document/9860767
- **Abstract**: In this paper, we focus on how to further improve the performance of short block-length low-density parity-check (LDPC) codes, especially the short LDPC codes in 5th generation (5G) New Radio (NR) systems. We propose an enhanced adaptive belief propagation (ABP) decoding algorithm with the assistance of partial cyclic redundancy check (CRC) bits. Meanwhile, the error detection ability can still be guaranteed by the remaining CRC bits and adaptive decoder parameters. Moreover, the proposed partial CRC-aided ABP (CA-ABP) decoding can be combined with the conventional BP decoding to further improve the performance. Simulation results show that compared with the BP decoding our proposed decoding method achieves an improvement in the error-correction performance.

## Ultra high speed 802.11n LDPC decoder with seven-stage pipeline in 28 nm CMOS

- **Status**: ✅
- **Reason**: 28nm CMOS 풀언롤 min-sum LDPC 디코더 HW(7단 파이프라인, 4비트 양자화) — 이식 가능 HW 아키텍처(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:9860730
- **Type**: conference
- **Published**: 19-22 June
- **Authors**: L. Lopacinski, A. Hasani, G. Panic +6
- **PDF**: https://ieeexplore.ieee.org/document/9860730
- **Abstract**: This paper reports our latest implementation results of a fully unrolled LDPC decoder prototyped in 28 nm CMOS technology. The decoder achieves 1218 Gbps coded throughput and consumes a 5.49 mm2 chip area. The standard min-sum decoding algorithm with four-bit quantization, five unrolled iterations, (648,540) parity matrix, and a seven-stage pipeline is employed. Such implementation achieves a higher data rate than adaptive degeneration and finite-alphabet decoding algorithms, requires less silicon than the solutions mentioned above, and is fully compliant with the IEEE 802.11n WLAN standard.

## Improvement of L1 Signaling Protection Based on ATSC 3.0 LDPC Codes

- **Status**: ✅
- **Reason**: modulo lifting로 QC-LDPC exponent matrix 조정하는 새 부호 구성(E) — 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9828695
- **Type**: conference
- **Published**: 15-17 June
- **Authors**: Seok-Ki Ahn, Sung-Ik Park
- **PDF**: https://ieeexplore.ieee.org/document/9828695
- **Abstract**: This paper proposes a new low-density parity-check (LDPC) coding scheme for physical-layer [layer-1 (L1)] signaling (L1 signaling) protection based on modulo lifting operation. The proposed LDPC coding scheme uses the same base matrices as those in ATSC 3.0, but adjusts the lifting size depending on the number of signaling bits. Since L1 signaling protection utilizes quasi-cyclic (QC) LDPC codes, their exponent matrices are obtained from those in ATSC 3.0 by modulo lifting operation for the proposed scheme. Numerical results show that the proposed scheme can give better block error rate (BLER) performance than the existing ATSC 3.0 signaling protection because the proposed one can dramatically reduce the portions of information shortening and parity puncturing than those in ATSC 3.0.

## An Optimal Block-Scheduling Algorithm for Pipelined Block-Parallel LDPC Decoder

- **Status**: ✅
- **Reason**: QC-LDPC block-parallel 파이프라인 디코더의 read-write conflict 최소 NOP 스케줄링 — 이식 가능 HW 아키텍처 신규 기법(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:9828749
- **Type**: conference
- **Published**: 15-17 June
- **Authors**: Fengshuang Li, Chao Zhang, Kewu Peng
- **PDF**: https://ieeexplore.ieee.org/document/9828749
- **Abstract**: Since the low-density parity-check (LDPC) code is widely used in today's wireless communication standards, its decoder architecture has been discussed in many works. To achieve high universality in hardware implementation, block-parallel is applied in the decoder for quasi-cyclic (QC) LDPC code. Configurability can be easily achieved by designing the operation instructions for blocks. The pipeline is also introduced as a traditional scheme for higher throughput. However, because of the data dependence in the decoding process, the pipeline would cause read-write conflicts, and some techniques should be utilized to solve them. Thanks to the block-parallel architecture, re-scheduling of the blocks can reduce the conflicts, but cannot guarantee the total avoidance of them. Inserting no-operation instructions (NOPs) is another solution that can remove all potential conflicts at the cost of lower throughput. In this paper, we combine these two techniques and propose an optimal algorithm for the instruction design aiming at the pipelined block-parallel decoder. It is proved that our algorithm can generate decoding instructions with no read-write conflict by inserting the minimum number of NOPs.
