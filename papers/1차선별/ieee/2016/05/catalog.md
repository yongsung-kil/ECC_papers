# IEEE Xplore — 2016-05 (1차선별 통과)


## Low-Complexity First-Two-Minimum-Values Generator for Bit-Serial LDPC Decoding

- **Status**: ✅
- **Reason**: bit-serial min-sum LDPC용 first-two-minimum-values 생성기 — 이식 가능 HW(D) 기여, 바이너리
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:7346442
- **Type**: journal
- **Published**: May 2016
- **Authors**: Jea Hack Lee, Myung Hoon Sunwoo
- **PDF**: https://ieeexplore.ieee.org/document/7346442
- **Abstract**: This brief proposes a low-complexity first-two-minimum-values generator for a bit-serial scheme. Since the hardware complexity of generators utilizes a significant portion of the min-sum low-density parity-check decoder, a low-complexity generator is crucially important. To reduce hardware complexity, an existing bit-serial generator that finds only one minimum value instead of two has been proposed; however, it can cause bit error rate (BER) degradation. By contrast, the proposed low-complexity bit-serial generator can find the exact first two minimum values and thus can improve the BER performance. Moreover, the proposed generator does not suffer from any throughput loss since its latency is almost the same as that of the existing generator.

## Iterative Decoding of LDPC Codes Over the  $q$ -Ary Partial Erasure Channel

- **Status**: ✅
- **Reason**: q-ary 부분소거채널(NVM 멀티레벨 read 동기)용 LDPC DE/설계 — 비휘발성 메모리 read 채널 직결, 애매하나 NAND 관련성으로 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7439825
- **Type**: journal
- **Published**: May 2016
- **Authors**: Rami Cohen, Yuval Cassuto
- **PDF**: https://ieeexplore.ieee.org/document/7439825
- **Abstract**: In this paper, we develop a new channel model, which we name the  $q$ -ary partial erasure channel (QPEC). The QPEC has a  $q$ -ary input, and its output is either the input symbol or a set of  $M$  ( $2 \le M \le q$ ) symbols, containing the input symbol. This channel serves as a generalization to the binary erasure channel and mimics situations when a symbol output from the channel is known only partially; that is, the output symbol contains some ambiguity, but is not fully erased. This type of channel is motivated by non-volatile memory multi-level read channels. In such channels, the readout is obtained by a sequence of current/voltage measurements, which may terminate with a partial knowledge of the stored level. Our investigation is concentrated on the performance of low-density parity-check (LDPC) codes when used over this channel, thanks to their low decoding complexity using belief propagation. We provide the exact QPEC density-evolution equations that govern the decoding process, and suggest a cardinality-based approximation as a proxy. We then provide several bounds and approximations on the proxy density evolutions, and verify their tightness through numerical experiments. Finally, we provide tools for the practical design of LDPC codes for use over the QPEC.

## SC-LDPC Code With Nonuniform Degree Distribution Optimized by Using Genetic Algorithm

- **Status**: ✅
- **Reason**: SC-LDPC 비균일 차수분포 GA 최적화로 BP threshold 개선 — 바이너리, 이식 가능 코드설계(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7439792
- **Type**: journal
- **Published**: May 2016
- **Authors**: Yohei Koganei, Masanori Yofune, Cong Li +2
- **PDF**: https://ieeexplore.ieee.org/document/7439792
- **Abstract**: We propose a class of spatially-coupled low-density parity-check (SC-LDPC) codes consisting of a finite-length chain of component LDPC matrices which are assigned with different degree distributions, i.e., the strength of spatial coupling is nonuniform within an SC-LDPC code. For this class of codes, we use a modified density evolution algorithm to calculate the belief-propagation (BP) threshold on the binary erasure channel (BEC). We then optimize the degree distributions by a genetic algorithm where the BP-threshold is considered as the fitness value. The resultant codes were confirmed to exhibit improved decoding performance compared with SC-LDPC codes having uniform degree distributions.

## Research on LDPC code decoding algorithm based on scheduling strategy

- **Status**: ✅
- **Reason**: 신규 스케줄링 디코딩 GBP(신뢰/비신뢰 변수노드 우선 갱신)로 trapping set/error floor 개선 — 이식 가능 BP 디코더 기법(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7531650
- **Type**: conference
- **Published**: 28-30 May 
- **Authors**: Feng Xiao
- **PDF**: https://ieeexplore.ieee.org/document/7531650
- **Abstract**: With the rapid development of the channel coding technology, low density parity check(LDPC) code has been widely concerned by researchers all of the world as an approaching code to Shannon limit. Error floor is an important issue in the theory of LDPC codes and the research of iterative decoding algorithms. Based on the decoding of LDPC codes, a new improved decoding algorithm, Group Belief Propagation (GBP) based on variable nodes is proposed for the different scheduling strategies of the LDPC codes. According to the difference between the messages and the hard decision values, the variable nodes are divided into reliable nodes and unreliable nodes. And the unreliable nodes are priority to update. Further, the effect of threshold for judging the group on GBP strategy is analyzed. Simulation results show that the proposed algorithm can achieve better convergence and decoding performances compared to three classical scheduling algorithms. Meanwhile, it can overcome the error floor phenomenon caused by the trapping set effectively.

## Reducing repair-bandwidth using codes based on factor graphs

- **Status**: ✅
- **Reason**: 분산 스토리지용 QC-PEG 바이너리 LDPC 팩터그래프 구성(repair-bandwidth/MTTDL 최적화 코드설계) — B/E
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7510728
- **Type**: conference
- **Published**: 22-27 May 
- **Authors**: Dongwon Lee, Hyegyeong Park, Jaekyun Moon
- **PDF**: https://ieeexplore.ieee.org/document/7510728
- **Abstract**: Distributed storage systems suffer from significant repair traffic generated due to frequent storage node failures. This paper shows that properly designed low-density parity-check (LDPC) codes can substantially reduce the amount of required block downloads for repair thanks to the sparse nature of their factor graph representation. In particular, with a careful construction of the factor graph, both low repair-bandwidth and high reliability can be achieved for a given code rate. First, a formula for the average repair bandwidth of LDPC codes is developed. This formula is then used to establish that the minimum repair bandwidth can be achieved by forcing a regular check node degree in the factor graph. It is also shown that for a given repair-bandwidth overhead, LDPC codes can have substantially higher reliability than currently utilized Reed-Solomon (RS) codes. Our reliability analysis is based on a formulation of the general equation for the mean-time-to-data-loss (MTTDL) associated with LDPC codes. The formulation reveals that the stopping number is highly related to MTTDL. For code rates 1/2, 2/3, and 3/4, our results show that quasi-cyclic (QC) progressive-edge-growth (PEG) LDPC codes with variable node degree 2 allow 25% ~ 50% reduction in the repair bandwidth while maintaining higher MTTDL compared to currently employed RS codes.

## Fully parallel window decoder architecture for spatially-coupled LDPC codes

- **Status**: ✅
- **Reason**: SC-LDPC용 완전병렬 윈도우 디코더 아키텍처 신규 제시(병렬화 HW, D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:7511553
- **Type**: conference
- **Published**: 22-27 May 
- **Authors**: Najeeb Ul Hassan, Martin Schlüter, Gerhard P. Fettweis
- **PDF**: https://ieeexplore.ieee.org/document/7511553
- **Abstract**: Spatially-coupled low-density parity-check (SC-LDPC) codes have been shown to be superior in performance than LDPC block codes. In order to comply with the practical constraints on latency, SC-LDPC codes are decoded using a window decoder that reduces the decoder latency and complexity compared to traditional block-wise decoding. However, so far the literature only considers the structural decoding latency of window decoder, ignoring the processing latency. Note that the processing latency directly impacts the decoder's throughput and is an important parameter in any modern communication system. The throughput of an iterative decoder is directly influenced by the number of iterations and hence in this paper we propose a fully parallel window decoder architecture for SC-LDPC codes where the decoding iterations are performed in parallel. This guarantees a high throughout while fulfilling the low latency requirements. The overall decoding latency (structural and processing latency) of the proposed window decoder architecture is compared with the classical window decoder.

## An efficient exhaustive search algorithm for elementary trapping sets of variable-regular LDPC codes

- **Status**: ✅
- **Reason**: variable-regular 바이너리 LDPC의 elementary trapping set 탐색 알고리즘 신규 제시(error floor 관련 코드설계, E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7511551
- **Type**: conference
- **Published**: 22-27 May 
- **Authors**: Yoones Hashemi, Amir H. Banihashemi
- **PDF**: https://ieeexplore.ieee.org/document/7511551
- **Abstract**: In this paper, we propose an efficient exhaustive search algorithm for elementary trapping sets (ETS) of variable-regular low-density parity-check (LDPC) codes. Recently, Karimi and Banihashemi proposed a characterization of ETSs, which was based on viewing an ETS as a layered superset (LSS) of a short cycle in the code's Tanner graph. A notable advantage of LSS characterization is that it corresponds to a simple LSS-based search algorithm (expansion technique) that starts from short cycles of the graph and finds the ETSs with LSS structure efficiently. Compared to the LSS-based search, which is based on a single LSS expansion technique, the new search algorithm involves two additional expansion techniques. The introduction of the new techniques results in significant improvements in search efficiency compared to the LSS-based search. We prove that using the three expansion techniques, each and every ETS structure can be obtained starting from a simple cycle. We also provide extensive simulation results that show, compared to the LSS-based search, up to three orders of magnitude improvement in search speed and memory requirements can be achieved.

## Practical LDPC encoders robust to hardware errors

- **Status**: ✅
- **Reason**: 결함 HW 견딜 LDPC 인코더(증강부호화+Gallager-B 노이지 디코딩+회로 최적화), 디코더/HW 견고화 기법 이식 가능(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7511552
- **Type**: conference
- **Published**: 22-27 May 
- **Authors**: Elsa Dupraz, Valentin Savin, Satish Kumar Grandhi +2
- **PDF**: https://ieeexplore.ieee.org/document/7511552
- **Abstract**: LDPC decoders on faulty hardware have received increasing attention over the last few years, mainly motivated by reliability issues in emerging nanotechnologies. As a main result, it was shown that LDPC decoders are naturally robust to hardware faults. LDPC encoders on faulty hardware have received less attention, and they are expected to be less robust to hardware faults. In this work, we propose an LDPC encoding solution that is robust to faulty hardware. Our encoding solution is composed of two steps. First, an Augmented Encoding method is proposed, which consists in computing an augmented codeword that contains both the codeword to be transmitted on the channel and extra parity bits. The augmented codeword is computed from a noisy encoding circuit, and then corrected by a noisy Gallager-B decoder before channel transmission. The augmented codeword is obtained from a rate-compatible construction that guarantees good decoding performance both for the augmented codeword and for the codeword to be transmitted on the channel. In order to further improve the robustness of our encoding solution, we propose a second step, consisting of a circuit-level optimization. We propose to identify the critical gates that are responsible for encoding failures, and to duplicate them in order to reduce their influence on encoding outputs. Based on Monte-Carlo simulation, we show that the proposed solution significantly improves the encoding robustness to hardware faults.

## Towards an analytical model of NAND flash memory and the impact on channel decoding

- **Status**: ✅
- **Reason**: NAND 플래시 임계전압 분포 해석모델·CCI 제거·소프트디코딩 LLR — A(NAND 직접) 채널모델/LLR 기법
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7510726
- **Type**: conference
- **Published**: 22-27 May 
- **Authors**: Hachem Yassine, Justin Coon, Mohamed Ismail +1
- **PDF**: https://ieeexplore.ieee.org/document/7510726
- **Abstract**: The underlying models of sources of noise in flash memory are exploited to compute an accurate distribution of the threshold voltage of a cell after cancelling cell to cell interference (CCI). We analytically express the mean and variance of this voltage solely as a function of number of P/E cycles, retention time and data eliminating the read overhead of the adaptive estimation methods. To reduce the computational difficulty in hardware, we approximate the accurate distribution by a moment matched Gaussian mixture and we validate this approximation by comparing the soft decision decoding performance of both models. To gain more error correction advantage, we model the residual CCI as an additional Gaussian noise term.

## Optimum message mapping LDPC decoders derived from the sum-product algorithm

- **Status**: ✅
- **Reason**: Information Bottleneck 기반 discrete message-mapping LDPC 디코더(4비트 정수, BP 근사) — 이식 가능 저복잡 디코더(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7510906
- **Type**: conference
- **Published**: 22-27 May 
- **Authors**: Jan Lewandowsky, Maximilian Stark, Gerhard Bauch
- **PDF**: https://ieeexplore.ieee.org/document/7510906
- **Abstract**: Starting from a discrete density evolution scheme originally introduced by Brian M. Kurkoski et al. which we improved by applying the Information Bottleneck method, we recently presented results on message passing decoders for Low Density Parity Check codes that have much lower complexity than state of the art decoders. In the decoders all node operations are replaced by discrete message mappings of unsigned integers what yields a great complexity reduction. Anyway the decoders perform very close to belief propagation decoding. New included simulation results prove that using a 4 bit integer architecture these decoders loose only 0.1 dB over Eb/No in comparison to an exact belief propagation decoder applied to the quantized output of a Gaussian channel. The most important contribution of this paper is the derivation of the message mapping decoders from the sum-product algorithm. Until now these decoders are assumed to not be linked to this algorithm. In order to reveal the hidden connection, we explain the decoding principle of the message mapping decoders in general factor graphs.

## Bit-flipping LDPC under noise conditions and its application to physically unclonable functions

- **Status**: ✅
- **Reason**: bit-flipping LDPC 디코더 회로(노이즈 내성, PUF용 ECC) - 비트플립 디코더 HW 기법 이식 가능(C/D), 애매하나 in으로 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7527440
- **Type**: conference
- **Published**: 22-25 May 
- **Authors**: Takao Marukame, Alexandre Schmid
- **PDF**: https://ieeexplore.ieee.org/document/7527440
- **Abstract**: A low-density parity check (LDPC) circuit and its properties as a post-processor is proposed for physically unclonable functions (PUFs) applications. PUFs can be realized using process variations or signal noises in SRAM or other PUF circuits, whereas the generated data needs to be processed by error check and correction (ECC) because of their inherent intra-PUF variabilities. The bit-flip LDPC circuits that have been developed in this study reveal compact constructions as well as notable noise tolerances during the ECC calculations. Unlike conventional deterministic post-processing, the LDPC circuits made even under unreliable fabrication conditions keep capable of guaranteeing robustness against noises.

## Construction of parallelized-decoding LDPC codes

- **Status**: ✅
- **Reason**: 병렬 디코딩용 large-girth QC-LDPC 코드 구성(block-wise 분할+Smith normal form으로 girth 처리)=이식 가능 코드설계(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7527261
- **Type**: conference
- **Published**: 22-25 May 
- **Authors**: Tsung-Che Wu, Chang-Ming Lee, Cheng-Kuei Wang
- **PDF**: https://ieeexplore.ieee.org/document/7527261
- **Abstract**: In the parallelization for high-throughput applications, the number of independent memory access usually dominates the coding throughput. Moreover, a class of large-girth low-density parity check (LDPC) codes usually has difficulties to realize the parallelization in the decoder. To cope with these obstacles, we propose an efficient code construction to take the number of required parallel decoding unit and the large-girth constraint into considerations at once. First, the parity check matrix would be split into the block-wise structure to fit the parallelization in the decoder. Second, the conversion of the cycle-checking inequalities can transform the girth issue into a linear system. Finally, based on the decomposition of the polyhedral set, the Smith normal form can efficiently solve inequalities of the proposed system. Simulation results show that the proposed code construction can satisfy the requirements of parallelization and high-performance coding with girth g = 12.

## REAL: A retention error aware LDPC decoding scheme to improve NAND flash read performance

- **Status**: ✅
- **Reason**: NAND 플래시 retention error 인지 LDPC 디코딩 기법(REAL), 직접 A 카테고리
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7897085
- **Type**: conference
- **Published**: 2-6 May 20
- **Authors**: Meng Zhang, Fei Wu, Xubin He +3
- **PDF**: https://ieeexplore.ieee.org/document/7897085
- **Abstract**: Continuous technology scaling makes NAND flash cells much denser. As a result, NAND flash is becoming more prone to various interference errors. Due to the hardware circuit design mechanisms of NAND flash, retention errors have been recognized as the most dominant errors, which affect the data reliability and flash lifetime. Furthermore, after experiencing a large number of programm/erase (P/E) cycles, flash memory would suffer a much higher error rate, rendering traditional ECC codes (typically BCH codes) insufficient to ensure data reliability. Therefore, low density parity check (LDPC) codes with stronger error correction capability are used in NAND flash-based storage devices. However, directly using LDPC codes with belief propagation (BP) decoding algorithm introduces non-trivial overhead of decoding latency and hence significantly degrades the read performance of NAND flash. It has been observed that flash retention errors show the so-called numerical-correlation characteristic (i.e., the 0-1 bits stored in the flash cell affect each other with the leakage of the charge) in each flash cell. In this paper, motivated by the observed characteristic, we propose REAL: a retention error aware LDPC decoding scheme to improve NAND flash read performance. The developed REAL scheme incorporates the numerical-correlation characteristic of retention errors into the process of LDPC decoding, and leverages the characteristic as additional bits decision information to improve its error correction capabilities and decrease the decoding latency. Our simulation results show that the proposed REAL scheme can reduce the LDPC decoding latency by 26.44% and 33.05%, compared with the Logarithm Domain Min-Sum (LD-MS) and Probability Domain BP (PD-BP) schemes, respectively.

## A heuristic method for adaptive linear programming decoding

- **Status**: ✅
- **Reason**: LDPC adaptive LP 디코딩의 redundant parity check 탐색 휴리스틱 — 바이너리 디코더 알고리즘(C), 애매하나 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7496077
- **Type**: conference
- **Published**: 16-19 May 
- **Authors**: Abdullah Sarıduman, Ali Emre Pusane, Z. Caner Taşkın
- **PDF**: https://ieeexplore.ieee.org/document/7496077
- **Abstract**: Adaptive linear programming (ALP) decoders are mainly used for decoding low-density parity-check (LDPC) codes. The principle of ALP decoders is based on generating redundant-parity check equations, which could eliminate fractional solutions of linear programming (LP) decoders. These generated redundant parity check equations increase the error rate performance of decoder. In this paper, LP model is defined with auxiliary variables to facilitate finding redundant-parity check equations, and redundant parity check equations are searched over proposed LP model with a heuristic method. Simulation results demonstrate that the proposed algorithm could find redundant-parity check equations in a shorter time than other ALP decoders.

## Incremental Decoding Schedules for Puncture-Based Rate-Compatible LDPC Codes

- **Status**: ✅
- **Reason**: LDPC edge-wise 스케줄링 BP, M2I2 기반 incremental decoding 스케줄 - 디코더 스케줄 기법 NAND BP에 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7504285
- **Type**: conference
- **Published**: 15-18 May 
- **Authors**: Huang-Chang Lee, Yeong-Luh Ueng
- **PDF**: https://ieeexplore.ieee.org/document/7504285
- **Abstract**: This paper shows that the decoding convergence of the punctured low-density parity-check (LDPC) codes can be significantly increased using edge wise scheduling belief-propagation. If rate- compatible (RC)-LDPC codes constructed based on puncturing are considered, the maximum mutual information increase (M^2I^2)-based algorithm can be used to arrange fixed schedules for incremental decoding, and further reduce the required number of iterations. With the assistance of the proposed decoding schedules, the puncture-based RC-LDPC codes can be a potential solution for delay- sensitive HARQ (Hybrid-Automatic Repeat reQuest) applications.

## 17x Reliability Enhanced LDPC Code with Burst-Error Masking and High-Precision LLR for Highly Reliable Solid-State-Drives with TLC NAND Flash Memory

- **Status**: ✅
- **Reason**: TLC NAND flash LDPC ECC 직접: burst-error masking, 고정밀 LLR 추정 (카테고리 A)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7493561
- **Type**: conference
- **Published**: 15-18 May 
- **Authors**: Tsukasa Tokutomi, Ken Takeuchi
- **PDF**: https://ieeexplore.ieee.org/document/7493561
- **Abstract**: Highly reliable LDPC ECC is introduced to improve the reliability of solid-state drives (SSDs). Although conventional AEP-LDPC ECC [3] is 12x highly reliable than BCH ECC, its error-correction capability is degraded due to the burst-errors and inaccurate log- likelihood ratio (LLR). To improve the reliability of TLC NAND flash, this paper proposes the burst-error masking (BEM) and program-disturb merged LLR estimation (PMLE). The first proposal, BEM eliminates the burst- errors by recording the error-location to the table. The second proposal, PMLE calculates the ratio of program-disturb errors to data-retention errors. As a result, more precise LLR is obtained. By combining BEM and PMLE, the SSD lifetime is extended by 17x and the table size overhead is reduced by 81%.

## Construction of Structured LDPC Code Based on Correlation Limitation

- **Status**: ✅
- **Reason**: 구조적 LDPC 구성(상관 제약)으로 다중부호율·layered 디코딩 지원, 디코더 throughput 개선 (카테고리 E/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7504175
- **Type**: conference
- **Published**: 15-18 May 
- **Authors**: Jun Xu, Dongming Wang, Jin Xu +3
- **PDF**: https://ieeexplore.ieee.org/document/7504175
- **Abstract**: Channel coding for the next generation communication system needs to support higher data throughput and transmission rate. Due to the inherent parallel feature, low density parity check (LDPC) codes comply with the target. In this paper, we propose a complete channel coding scheme based on structured LDPC codes. In our design, the correlation among different parity check matrices for different code rates is established, meanwhile the correlation between adjacent rows is established, then matrix design should be restricted by these two type defined correlations in order to make great progress in the support of multiple code rates and layered decoding algorithm. Our scheme includes the definition of the four matrices and five constraint features of these matrices, also the benefits of these features are analyzed. Simulation result shows that the performance of the proposed scheme is the same as or a little better than that of 11ad LDPC codes. The proposed LDPC scheme obviously decreases route complexity and increases decoder throughput. So, this scheme is very suitable for high speed decoder with more than 1Gbps throughput in various future communication systems.

## Implementation of decoders for symmetric low density parity check codes on parallel computation platforms using OpenCL

- **Status**: ✅
- **Reason**: OpenCL FPGA/GPU LDPC 디코더 구현, 병렬화 HW 아키텍처 이식 가능(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:7726832
- **Type**: conference
- **Published**: 15-18 May 
- **Authors**: Andrew J. Maier, Bruce F. Cockburn
- **PDF**: https://ieeexplore.ieee.org/document/7726832
- **Abstract**: OpenCL is a high-level language that allows mixed hardware/software systems to be specified and compiled to run on heterogeneous parallel computing platforms. The hardware parallelism can take the form of multi-core central processing units (CPUs), massively parallel graphics processing units (GPUs), and, most recently, field-programmable gate array (FPGA) fabrics. OpenCL compilers for CPUs and GPUs have been available for over 6 years, but only recently has compiler support been extended to include FPGAs. This paper investigates OpenCL designs for the computationally demanding standard iterative decoding algorithm for low-density parity check (LDPC) codes. The LDPC decoding algorithm offers several kinds of potentially exploitable parallelism. Our objective was to investigate the design trade-offs in OpenCL that will produce the best performance when compiled by the Altera Offline Compiler (AOC v15.1) for OpenCL-to-FPGA. Within a relatively short design time we were able to implement a decoder that achieved 5.12 Mbps with a length-1024 (3,6)-regular code.

## Application Optimized Adaptive ECC with Advanced LDPCs to Resolve Trade-Off among Reliability, Performance, and Cost of Solid-State Drives

- **Status**: ✅
- **Reason**: MLC NAND SSD 적응형 LDPC ECC 직접, advanced LDPC 결합 알고리즘 (카테고리 A)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7493568
- **Type**: conference
- **Published**: 15-18 May 
- **Authors**: Yusuke Yamaga, Chihiro Matsui, Shogo Hachiya +1
- **PDF**: https://ieeexplore.ieee.org/document/7493568
- **Abstract**: The performance of NAND flash based solid-state drives (SSDs) is highly dependent on the application's read and write characteristics [3], where "intensity" is defined as ratio of read:write requests, and "write- hot/cold" considers the write frequency. Moreover, NAND flash memory's reliability degrades with write/erase (W/E) cycling. To optimize performance and reliability, conventional error-correcting code (ECC) scheme switches from fast conventional Bose-Chaudhuri- Hocquenghem (BCH) to slower conventional Low Density Parity Check (LDPC), when the page error rate exceeds BCH's decoding capability. However, advanced LDPCs have been reported, called Quick-LDPC [8] and Error- Prediction (EP-) LDPC without (w/o) upper/lower cells [8], which have (i) higher error correction capability compared to conventional BCH and (ii) shorter decoding time than conventional soft-decoding LDPC. Therefore, this paper proposes an application optimized adaptive (AOA-) ECC for Multi-Level-Cell (MLC) NAND flash-based enterprise SSDs. AOA-ECC includes a new algorithm to efficiently combine the two advanced LDPCs, considering the application's characteristics and memory's W/E cycles. A firmware in the proposed SSD system chooses the optimal advanced LDPC, based on whether the application is read/write-intensive and/or write- hot/cold. Using the proposed AOA-ECC SSD with MLC NAND flash, performance improves by up to 3-times, the reliability improves by 57% and the ECC decoder area decreases by 25%.

## A subtraction based method for the construction of quasi-cyclic LDPC codes of girth eight

- **Status**: ✅
- **Reason**: 뺄셈 기반 girth-8 QC-LDPC 신규 구성법 (E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7491830
- **Type**: conference
- **Published**: 12-14 May 
- **Authors**: Ambar Bajpai, Lunchakorn Wuttisittikulkij, Abhishek Kalsi +1
- **PDF**: https://ieeexplore.ieee.org/document/7491830
- **Abstract**: This article presents a simple, less computational complexity method for constructing exponent matrix (3, K) having girth at least 8 of quasi-cyclic low-density parity-check (QC-LDPC) codes based on subtraction method. The construction of code deals with the generation of exponent matrix by three formulas. This method is flexible for any block-column length K. The simulations are shown in comparison with some existing appreciable work. The codes with girth 8 are constructed with circulant permutation matrix (CPM) size P ≥ max{a2, r, a2, r,….a2, k} + 1.

## Novel multi-Gbps bit-flipping decoders for punctured LDPC codes

- **Status**: ✅
- **Reason**: 펑처드 LDPC용 신규 bit-flipping 디코더+FPGA HW (C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7495161
- **Type**: conference
- **Published**: 12-14 May 
- **Authors**: Christina Archonta, Nikos Kanistras, Vassilis Paliouras
- **PDF**: https://ieeexplore.ieee.org/document/7495161
- **Abstract**: Conventional bit-flipping (BF) algorithms spectacularly fail to handle punctured LDPC codes as they use hard decisions and, therefore, they cannot effectively cope with zero-reliability punctured symbols. However, BF techniques lead to low-cost high-speed decoders. This paper introduces a novel method that enables the use of BF-based iterative decoders for punctured LDPC codes. An erasure preprocessor is introduced and is shown to successfully mitigate the impact of puncturing, substantially improving the coding gain achieved for punctured codes under BF decoding. The proposed technique renders BF decoding of punctured codes useful, something that was not possible so far to our knowledge. Furthermore, two hardware architectures are introduced and evaluated. Hardware sharing is shown to efficiently exploit common structures in the proposed combined erasure and BF decoder, leading to a new architecture found to be particularly efficient. The proposed architecture requires extremely low hardware resources, facilitating full-parallel architectures that sustain multi-Gbps throughput rates when implemented on Virtex-7 FPGA devices.

## Architecture of a NVM-based storage system using adaptive LDPC codes

- **Status**: ✅
- **Reason**: NVM 스토리지용 적응 LDPC, 디코더 풀 공유 HW 아키텍처 (A/B/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7495149
- **Type**: conference
- **Published**: 12-14 May 
- **Authors**: Stelios Korkotsides, Theodore A. Antonakopoulos
- **PDF**: https://ieeexplore.ieee.org/document/7495149
- **Abstract**: Low Density Parity Check (LDPC) codes have been widely used in communications systems due to their high error correction capabilities. Recently these codes are also investigated for being exploited in high performance storage systems, especially when Non-Volatile Memory (NVM) technologies are used. The main drawback of using LDPC codes in storage systems with a high number of parallel channels is the increased hardware complexity and cost, especially when variable rate codes are used. In this work, we present an architecture of a NVM-based storage system that dynamically adapts the LDPC's rate to the aging conditions of the storage device in order to maximize its lifetime capacity while keeping low its hardware complexity. In order to decrease the system's complexity we propose a PCIe-based architecture that uses a pool of LDPC decoders shared by all NVM channels and we study its effect on the system's lifetime capacity and the achievable I/O data rate.

## High-Throughput Multi-Core LDPC Decoders Based on x86 Processor

- **Status**: ✅
- **Reason**: layered OMS/NMS LDPC 디코더의 x86 SIMD/SPMD 고속 구현; 이식 가능 디코더 알고리즘+병렬 아키텍처(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7110620
- **Type**: journal
- **Published**: 1 May 2016
- **Authors**: Bertrand Le Gal, Christophe Jego
- **PDF**: https://ieeexplore.ieee.org/document/7110620
- **Abstract**: Low-Density Parity-Check (LDPC) codes are an efficient way to correct transmission errors in digital communication systems. Although initially targeting strictly to ASICs due to computation complexity, LDPC decoders have been recently ported to multicore and many-core systems. Most works focused on taking advantage of GPU devices. In this paper, we propose an alternative solution based on a layered OMS/NMS LDPC decoding algorithm that can be efficiently implemented on a multi-core device using Single Instruction Multiple Data (SIMD) and Single Program Multiple Data (SPMD) programming models. Several experimentations were performed on a x86 processor target. Throughputs up to 170 Mbps were achieved on a single core of an INTEL Core i7 processor when executing 20 layered-based decoding iterations. Throughputs reaches up to 560 Mbps on four INTEL Core-i7 cores. Experimentation results show that the proposed implementations achieved similar BER correction performance than previous works. Moreover, much higher throughputs have been achieved by comparison with all previous GPU and CPU works. They range from x1.4 to x8 by comparison with recent GPU works.
