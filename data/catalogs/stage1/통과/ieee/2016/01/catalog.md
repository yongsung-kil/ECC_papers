# IEEE Xplore — 2016-01 (1차선별 통과)


## A Survey of FPGA-Based LDPC Decoders

- **Status**: ✅
- **Reason**: FPGA LDPC 디코더 서베이지만 140개 설계의 정량 비교·성능 트레이드오프를 담아 예외 포함(범주 D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:7360870
- **Type**: journal
- **Published**: Secondquar
- **Authors**: Peter Hailes, Lei Xu, Robert G. Maunder +2
- **PDF**: https://ieeexplore.ieee.org/document/7360870
- **Abstract**: Low-density parity check (LDPC) error correction decoders have become popular in communications systems, as a benefit of their strong error correction performance and their suitability to parallel hardware implementation. A great deal of research effort has been invested into LDPC decoder designs that exploit the flexibility, the high processing speed, and the parallelism of field-programmable gate array (FPGA) devices. FPGAs are ideal for design prototyping and for the manufacturing of small-production-run devices, where their in-system programmability makes them far more cost-effective than application-specific integrated circuits (ASICs). However, the FPGA-based LDPC decoder designs published in the open literature vary greatly in terms of design choices and performance criteria, making them a challenge to compare. This paper explores the key factors involved in FPGA-based LDPC decoder design and presents an extensive review of the current literature. In-depth comparisons are drawn amongst 140 published designs (both academic and industrial) and the associated performance tradeoffs are characterized, discussed, and illustrated. Seven key performance characteristics are described, namely, their processing throughput, processing latency, hardware resource requirements, error correction capability, processing energy efficiency, bandwidth efficiency, and flexibility. We offer recommendations that will facilitate fairer comparisons of future designs, as well as opportunities for improving the design of FPGA-based LDPC decoders.

## Searching for Binary and Nonbinary Block and Convolutional LDPC Codes

- **Status**: ✅
- **Reason**: 바이너리 QC-LDPC 및 컨볼루션 LDPC 탐색·girth 최적화 그리디 알고리즘 제시(E), 비이진 부분은 무시하고 바이너리 구성 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7312464
- **Type**: journal
- **Published**: Jan. 2016
- **Authors**: Irina E. Bocharova, Boris D. Kudryashov, Rolf Johannesson
- **PDF**: https://ieeexplore.ieee.org/document/7312464
- **Abstract**: A unified approach to search for and optimize codes determined by their sparse parity-check matrices is presented. Replacing the nonzero elements of a binary parity-check matrix (the base or parent matrix) either by circulants or by companion matrices of elements from a finite field GF $(2^{m})$ , we obtain quasi-cyclic low-density parity-check (LDPC) block codes and binary images of nonbinary LDPC block codes, respectively. By substituting monomials of a formal variable  $D$ , we obtain the polynomial description of an LDPC convolutional code. A set of performance measures applicable to different classes of LDPC codes is considered, and a greedy algorithm for code performance optimization is presented. The heart of the new optimization algorithm is a fast procedure for searching for LDPC codes with large girth of their Tanner graphs. For a few classes of LDPC codes, examples of codes combining good error-correcting performance with compact representation are obtained. In particular, we present optimized convolutional LDPC codes and conclude that the LDPC block codes are still superior to their convolutional counterparts if both decoding complexity and coding delay are considered. Moreover, a specific channel model can easily be embedded into the optimization loop. Thereby, the code can be optimized for a specific channel. The efficiency of such an optimization is demonstrated via an example of faster than Nyquist (FTN) signaling using LDPC codes. The FTN strategy combined with a rate  $R=1/2$  LDPC code of length 64 800 optimized for effective data rate  $R=3/4$  gains more than 0.5 dB compared with the standard LDPC codes of the same rate and length. The obtained gain corresponds to transmission at the capacity of the binary input additive white Gaussian noise channel. In most numerical examples, we consider codes with bidiagonal structure of the parity-check matrix. This restriction preserves low encoding complexity and allows fair comparison with codes selected for communication standards.

## Breaking the Trapping Sets in LDPC Codes: Check Node Removal and Collaborative Decoding

- **Status**: ✅
- **Reason**: trapping set 제거를 위한 check node removal·collaborative decoding 신규 디코더(C), 스토리지 error floor 대응으로 NAND에 직접 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7320999
- **Type**: journal
- **Published**: Jan. 2016
- **Authors**: Soonyoung Kang, Jaekyun Moon, Jeongseok Ha +1
- **PDF**: https://ieeexplore.ieee.org/document/7320999
- **Abstract**: Trapping sets strongly degrade performance of low-density parity check (LDPC) codes in the low-error-rate region. This creates significant difficulties for the deployment of LDPC codes to low-error-rate applications such as storage and wireless systems with no or limited retransmission options. We propose a novel technique for breaking trapping sets based on collaborative decoding that utilizes two different decoding modes. While the main decoding mode executes message passing based on the original parity check matrix of the corresponding LDPC code, the sub-decoding mode operates on a modified parity check matrix formed by removing a portion of check nodes in the factor graph representation of the given code. The modified parity check matrix is designed to promote a passing of correct information into erroneous variable nodes in the trapping set. Theoretical properties of the proposed trapping-set-breaking technique have been established based on the notion of the improved separation for the trapped variable nodes. Simulation results show that the proposed collaborative LDPC decoding scheme switching between the two decoding modes back and forth effectively breaks dominant trapping sets of various known types of regular and irregular LDPC codes.

## LDPC Decoding Over Nonbinary Queue-Based Burst Noise Channels

- **Status**: ✅
- **Reason**: 비이진 큐 기반 버스트 노이즈 채널의 바이너리 LDPC SPA 디코딩(채널메모리 활용 LLR)·하드/소프트 양자화 — 떼어낼 디코더 기법 있음, 애매하여 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7017574
- **Type**: journal
- **Published**: Jan. 2016
- **Authors**: Pedro Melo, Cecilio Pimentel, Fady Alajaji
- **PDF**: https://ieeexplore.ieee.org/document/7017574
- **Abstract**: Iterative decoding based on the sum-product algorithm (SPA) is examined for sending low-density parity check (LDPC) codes over a discrete nonbinary queue-based Markovian burst noise channel. This channel model is adopted due to its analytical tractability and its recently demonstrated capability in accurately representing correlated flat Rayleigh fading channels under antipodal signaling and either hard or soft output quantization. SPA equations are derived in closed form for this model in terms of its parameters. It is then numerically observed that potentially large coding gains can be realized with respect to the Shannon limit by exploiting channel memory as opposed to ignoring it via interleaving. Finally, the LDPC decoding performance under both matched and mismatched decoding regimes is evaluated. It is shown that the Markovian model provides noticeable gains over channel interleaving and that it can effectively capture the underlying fading channel behavior when decoding LDPC codes.

## Construction of Near-Capacity Protograph LDPC Code Sequences With Block-Error Thresholds

- **Status**: ✅
- **Reason**: protograph LDPC density evolution·block-error threshold·유한길이 구성(E), 바이너리 채널 대상 코드 설계 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7328274
- **Type**: journal
- **Published**: Jan. 2016
- **Authors**: Asit Kumar Pradhan, Andrew Thangaraj, Arunkumar Subramanian
- **PDF**: https://ieeexplore.ieee.org/document/7328274
- **Abstract**: Density evolution for protograph low-density parity-check (LDPC) codes is considered, and it is shown that the message-error rate falls double-exponentially with iterations whenever the degree-2 subgraph of the protograph is cycle-free and noise level is below threshold. Conditions for stability of protograph density evolution are established and related to the structure of the protograph. Using large-girth graphs, sequences of protograph LDPC codes with block-error threshold equal to bit-error threshold and block-error rate falling near-exponentially with blocklength are constructed deterministically. Small-sized protographs are optimized to obtain thresholds near capacity for binary erasure and binary-input Gaussian channels.

## Row and Column Extensions of 4-Cycle Free LDPC Codes

- **Status**: ✅
- **Reason**: 4-cycle free LDPC의 row/column 확장으로 girth-6 보장하는 새 구성법(E), 바이너리 사이클 제거 기법 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7317762
- **Type**: journal
- **Published**: Jan. 2016
- **Authors**: Mohammad Gholami, Akram Nassaj
- **PDF**: https://ieeexplore.ieee.org/document/7317762
- **Abstract**: In this letter, an approach is proposed to increase the row (column)-weight of the parity-check matrix of a 4-cycle free LDPC code such that the constructed LDPC code has girth of at least 6. In fact, to each parity-check matrix H, a new graph Gr(H) (Gc(H)) is assigned in which the vertices correspond to the rows (columns) of H and two vertices are adjacent if and only if the associated rows (columns) have in common at least one nonzero element. Now, in a proper vertex coloring of Gr(H) (Gc(H)), each color is considered as a new column (row) whose nonzero elements happen in the rows (columns) in which the corresponding vertices have the same color. Based on this method, some high-rate LDPC codes with girth 6 and column-weight of at least 4 can be constructed from the recently proposed column-weight three LDPC codes with girth 6. Moreover, using the mutually orthogonal Latin squares, this approach is applied on the incidence matrices of some complete bipartite graphs to generate some girth-6 LDPC codes with different column-weights and large minimum-distances.

## A 3.0 Gb/s Throughput Hardware-Efficient Decoder for Cyclically-Coupled QC-LDPC Codes

- **Status**: ✅
- **Reason**: 신규 cyclically-coupled QC-LDPC 코드설계 + RAM기반 FPGA 디코더 아키텍처(3Gb/s, error floor 없음) — D/E 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7370816
- **Type**: journal
- **Published**: Jan. 2016
- **Authors**: Qing Lu, Jianfeng Fan, Chiu-Wing Sham +2
- **PDF**: https://ieeexplore.ieee.org/document/7370816
- **Abstract**: In this paper, we propose a new class of quasi-cyclic low-density parity-check (QC-LDPC) codes, namely cyclically-coupled QC-LDPC (CC-QC-LDPC) codes, and their RAM-based decoder architecture. CC-QC-LDPC codes have a simple structure and are constructed by cyclically-coupling a number of QC-LDPC subcodes. They can achieve throughput and error performance as excellent as LDPC convolutional codes, but with much lower hardware requirements. They are therefore promising candidates for future generations of communication systems such as long-haul optical communication systems. In particular, a rate-5/6 CC-QC-LDPC decoder has been implemented onto a field-programmable gate array (FPGA) and it achieves a throughput of 3.0 Gb/s at 100 MHz clock rate with 10-iteration decoding. No error floor is observed up to an $E_{b}/N_{0}$ of 3.50 dB, where all $1.14\times 10^{16}$ transmitted bits have been decoded correctly.

## A base matrix method to construct column weight 3 quasi-cyclic LDPC codes with high girth

- **Status**: ✅
- **Reason**: column weight 3 QC-LDPC high girth(8/10/12) base matrix 신규 구성법(E, 바이너리), 사이클 제거 코드설계
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7562999
- **Type**: conference
- **Published**: 27-30 Jan.
- **Authors**: Abhishek Kalsi, Ambar Bajpai, Lunchakorn Wuttisittikulkij +1
- **PDF**: https://ieeexplore.ieee.org/document/7562999
- **Abstract**: This article presents a simple, less computational complexity method for constructing exponent matrix (3, K) of girth 8, 10 and 12 of quasi-cyclic low-density parity-check codes (QC-LDPC) based on generation of base matrix. The construction of code deals with generation of base matrix by a simple algorithm and element wise element method for girth 8, while only element wise element method for girth 10 and 12. These methods are flexible for block-column length K. The simulations are shown in comparison with some existing appreciable work.

## Rapid prototyping of multi-mode QC-LDPC decoder for 802.11n/ac standard

- **Status**: ✅
- **Reason**: multi-mode QC-LDPC 디코더 재구성형 FPGA 아키텍처, NAND LDPC HW로 이식 가능(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:7427981
- **Type**: conference
- **Published**: 25-28 Jan.
- **Authors**: Qing Lu, Chiu-Wing Sham, Francis C. M. Lau
- **PDF**: https://ieeexplore.ieee.org/document/7427981
- **Abstract**: A multi-mode QC-LDPC decoder is proposed to satisfy the 802.11n/ac WiFi standard. With code-specific design, the overall performance of the decoder is enhanced while ensuring an on-the-fly reconfigurable ability. The proposed architecture has been synthesized using an FPGA for measurements. A state-of-art error rate and implementation complexity are reported. Meanwhile, the throughput has been increased to range from 382 MHz to 1852 MHz.

## A Survey on Programmable LDPC Decoders

- **Status**: ✅
- **Reason**: 프로그래머블 LDPC 디코더 서베이지만 GPU/멀티코어 병렬 디코더 아키텍처를 구체 비교·논의 → D(HW 아키텍처) 이식 가능, 예외 포함
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:7523326
- **Type**: journal
- **Published**: 2016
- **Authors**: Joao Andrade, Gabriel Falcao, Vitor Silva +1
- **PDF**: https://ieeexplore.ieee.org/document/7523326
- **Abstract**: Low-density parity-check (LDPC) block codes are popular forward error correction schemes due to their capacity-approaching characteristics. However, the realization of LDPC decoders that meet both low latency and high throughput is not a trivial challenge. Usually, this has been solved with the ASIC and FPGA technology that enables meeting the decoder design constraints. But the rise of parallel architectures, such as graphics processing units, and the scaling of CPU streaming extensions has shown that multicore and many-core technology can provide a flexible alternative to the development of dedicated LDPC decoders for the compute-intensive prototyping phase of the design of new codes. Under this light, this paper surveys the most relevant publications made in the past decade to programmable LDPC decoders. It looks at the advantages and disadvantages of parallel architectures and data-parallel programming models, and assesses how the design space exploration is pursued regarding key characteristics of the underlying code and decoding algorithm features. This paper concludes with a set of open problems in the field of communication systems on parallel programmable and reconfigurable architectures.

## Improving the Tolerance of Stochastic LDPC Decoders to Overclocking-Induced Timing Errors: A Tutorial and a Design Example

- **Status**: ✅
- **Reason**: Stochastic LDPC 디코더의 overclocking 타이밍에러 내성 개선 및 신규 디코더 설계; 이식 가능 디코더/HW 기법(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7446275
- **Type**: journal
- **Published**: 2016
- **Authors**: Xin Zuo, Isaac Perez-Andrade, Robert G. Maunder +2
- **PDF**: https://ieeexplore.ieee.org/document/7446275
- **Abstract**: Channel codes, such as low-density parity-check (LDPC) codes, may be employed in wireless communication schemes for correcting transmission errors. This tolerance to channel-induced transmission errors allows the communication schemes to achieve higher transmission throughputs, at the cost of requiring additional processing for performing LDPC decoding. However, this LDPC decoding operation is associated with a potentially inadequate processing throughput, which may constrain the attainable transmission throughput. In order to increase the processing throughput, the clock period may be reduced, albeit this is at the cost of potentially introducing timing errors. Previous research efforts have considered a paucity of solutions for mitigating the occurrence of timing errors in channel decoders, by employing additional circuitry for detecting and correcting these overclocking-induced timing errors. Against this background, in this paper, we demonstrate that stochastic LDPC decoders (LDPC-SDs) are capable of exploiting their inherent error correction capability for correcting not only transmission errors, but also timing errors, even without the requirement for additional circuitry. Motivated by this, we provide the first comprehensive tutorial on LDPC-SDs. We also propose a novel design flow for timing-error-tolerant LDPC decoders. We use this to develop a timing error model for LDPC-SDs and investigate how their overall error correction performance is affected by overclocking. Drawing upon our findings, we propose a modified LDPC-SD, having an improved timing error tolerance. In a particular practical scenario, this modification eliminates approximately 1-dB performance degradation that is suffered by an overclocked LDPC-SD without our modification, enabling the processing throughput to be increased by up to 69.4%, which is achieved without compromising the error correction capability or processing energy consumption of the LDPC-SD.

## Finite Length Analysis of Low-Density Parity-Check Codes on Impulsive Noise Channels

- **Status**: ✅
- **Reason**: 바이너리 LDPC 유한길이 분석(density evolution, BEP/BLEP 폐형식)으로 코드설계(E)에 이식 가능한 분석기법 — NAND LLR 채널에 응용 여지, 애매하면 in
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7809141
- **Type**: journal
- **Published**: 2016
- **Authors**: Zhen Mei, Martin Johnston, Stéphane Le Goff +1
- **PDF**: https://ieeexplore.ieee.org/document/7809141
- **Abstract**: Low-density parity-check (LDPC) codes with very long block lengths are well known for their powerful error correction, but it is not always desirable to employ long codes in communication systems, where latency is a serious issue, such as voice and video communication between multiple users. Finite length analyses of LDPC codes have already been presented in the literature for the additive white Gaussian noise channel, but in this paper, we consider the finite length analysis of LDPC codes for channels that exhibit impulsive noise. First, an exact uncoded bit error probability (BEP) of an impulsive noise channel, modeled as a symmetric α-stable (SαS) distribution, is derived. Then, to obtain the LDPC-coded performance, density evolution is applied to evaluate the asymptotic performance of LDPC codes on SαS channels and determine the threshold signal-to-noise ratio. Finally, we derive closed-form expressions for the BEP and block error probability of short LDPC codes on these channels, which are shown to match closely with simulated results on channels with different levels of impulsiveness, even for block lengths as low as 1000 b.

## Stochastic Computing Improves the Timing-Error Tolerance and Latency of Turbo Decoders: Design Guidelines and Tradeoffs

- **Status**: ✅
- **Reason**: 스토캐스틱 컴퓨팅 디코더 HW 기법, LDPC 디코더에도 동일 적용되는 HW 아키텍처(D)로 이식 가능
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:7403849
- **Type**: journal
- **Published**: 2016
- **Authors**: Isaac Perez-Andrade, Shida Zhong, Robert G. Maunder +2
- **PDF**: https://ieeexplore.ieee.org/document/7403849
- **Abstract**: Stochastic computing has been recently proposed for the hardware implementation of both low-density parity-check (LDPC) decoders and turbo decoders, which facilitate near-optimal error correction capabilities in wireless communication applications. Previous contributions have demonstrated that stochastic LDPC decoders offer an attractive tradeoff between their error correction capabilities, hardware performance, and timing-error tolerance. Motivated by this, we propose a pair of stochastic turbo decoder (STD) designs having significantly enhanced timing-error tolerance and significantly reduced processing latency. Moreover, we characterize the tradeoffs between chip area, energy efficiency, latency, throughput, and error correction capabilities of both the timing-error-tolerant STD and of the reduced-latency STD. We demonstrate that our proposed timing-error-tolerant STD operated at 1.20 V, with a clock period of 2.2 ns and in the presence of a three-standard deviation power supply variation of 7%, exhibits an unimpaired performance, compared with the state-of-the-art STD, operated at 1.20 V and 4 ns and with no power supply variations. This corresponds processing throughput improvement by a factor of 2.42 and energy consumption reduction by a factor of 4. Finally, we demonstrate that our proposed reduced-latency STD has a processing latency that is an order of magnitude lower than that of the state-of-the-art STD. This is despite reducing the chip area by a factor of 4, increasing the processing throughput by a factor of 65, while consuming only 0.005 times the energy of the state-of-the-art STD, when using binary phase-shift keying for communication over an additive white Gaussian noise channel having Eb/N0 = 3 dB.

## Hardware complexity reduction of LDPC-CC decoders based on message-passing approaches

- **Status**: ✅
- **Reason**: LDPC-CC 디코더의 Min-Sum 근사 선택으로 HW 복잡도/성능 개선; min-sum 변형+HW(C/D) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7952003
- **Type**: conference
- **Published**: 2016
- **Authors**: H. Ben Thameur, C. Bouzouita, N. Khouja +3
- **PDF**: https://ieeexplore.ieee.org/document/7952003
- **Abstract**: LDPC convolutional codes (LDPC-CC) are a family of error-correcting codes (ECC) used in digital communication systems like the IEEE 1901 standard. High throughput and low complexity hardware architectures were designed for real time systems. In this article we demonstrate that an efficient selection of the message passing (MP) algorithm for LDPC-CC decoding improves the architecture features of related works. In fact, considering the LDPC-CC decoders proposed for the IEEE 1901 standard, we show that an appropriate Min-Sum approximation selection can significantly improve the error correction performance by 0.1 to 0.2 dB in terms of Bit Error Ratio. It can also reduce the hardware complexity by 10% to 20% with no impact on the Bit Error Ratio performance.

## Noise-aided gradient descent bit-flipping decoders approaching maximum likelihood decoding

- **Status**: ✅
- **Reason**: noise-aided GDBF 비트플리핑 LDPC 디코더, trapping set 탈출·ML 근접 — 신규 이식 가능 디코더 알고리즘(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7593125
- **Type**: conference
- **Published**: 2016
- **Authors**: D. Declercq, C. Winstead, B. Vasic +3
- **PDF**: https://ieeexplore.ieee.org/document/7593125
- **Abstract**: In the recent literature, the study of iterative LDPC decoders implemented on faulty-hardware has led to the counter-intuitive conclusion that noisy decoders could perform better than their noiseless version. This peculiar behavior has been observed in the finite codeword length regime, where the noise perturbating the decoder dynamics help to escape the attraction of fixed points such as trapping sets. In this paper, we will study two recently introduced LDPC decoders derived from noisy versions of the gradient descent bit-flipping decoder (GDBF). Although the GDBF is known to be a simple decoder with limited error correction capability compared to more powerful softdecision decoders, it has been shown that the introduction of a random perturbation in the decoder could greatly improve the performance results, approaching and even surpassing belief propagation or min-sum based decoders. For both decoders, we evaluate the probability of escaping from a Trapping set, and relate this probability to the parameters of the injected noise distribution, using a Markovian model of the decoder transitions in the state space of errors localized on isolated trapping sets. In a second part of the paper, we present a modified scheduling of our algorithms for the binary symmetric channel, which allows to approach maximum likelihood decoding (MLD) at the cost of a very large number of iterations.

## Non-surjective finite alphabet iterative decoders

- **Status**: ✅
- **Reason**: NS-FAID(min-sum 변형 유한알파벳 반복디코더), density evolution 최적화·HW 메모리 절감 — 이식 가능 디코더/HW(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7511111
- **Type**: conference
- **Published**: 2016
- **Authors**: T. T. Nguyen-Ly, K. Le, V. Savin +3
- **PDF**: https://ieeexplore.ieee.org/document/7511111
- **Abstract**: This paper introduces a new theoretical framework, akin to the use of imprecise message storage in Low Density Parity Check (LDPC) decoders, which is seen as an enabler for cost-effective hardware designs. The proposed framework is the one of Non-Surjective Finite Alphabet Iterative Decoders (NS-FAIDs), and it is shown to provide a unified approach for several designs previously proposed in the literature. NS-FAIDs are optimized by density evolution for WiMAX irregular LDPC codes and we show they provide different trade-offs between hardware complexity and decoding performance. In particular, we derive a set of 27 NS-FAIDs that provide decoding gains up to 0.36 dB, while yielding a memory/interconnect reduction up to 25%/30% compared to the Min-Sum decoder.

## Weight distribution of the syndrome of linear codes and connections to combinatorial designs

- **Status**: ✅
- **Reason**: Tanner 그래프 4-사이클 제거 및 신드롬 가중치 분포 분석, 바이너리 LDPC 코드설계 분석(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7541857
- **Type**: conference
- **Published**: 2016
- **Authors**: C. Pacher, P. Grabenweger, D. E. Simos
- **PDF**: https://ieeexplore.ieee.org/document/7541857
- **Abstract**: The expectation and the variance of the syndrome weight distribution of linear codes after transmission of codewords through a binary symmetric channel are derived exactly in closed form as functions of the code's parity-check matrix and of the degree distributions of the associated Tanner graph. The influence of (check) regularity of the Tanner graph is studied. Special attention is payed to Tanner graphs that have no cycles of length four. We further study the equivalence of some classes of combinatorial designs and important classes of LDPC codes and apply our general results to those more specific structures. Simulations validate the analytical results and show that the actual cumulative distribution function of the syndrome weight is close to that of a normal distribution.

## Improved Soft-Decision Forward Error Correction via Post-Processing of Mismatched Log-Likelihood Ratios

- **Status**: ✅
- **Reason**: mismatched LLR 후처리/선형 스케일링으로 LDPC SD-FEC 이득, LLR 양자화·보정 기법 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7767651
- **Type**: conference
- **Published**: 2016
- **Authors**: A. Alvarado, L. Szczecinski, T. Fehenberger +2
- **PDF**: https://ieeexplore.ieee.org/document/7767651
- **Abstract**: Correction of soft information based on achievable information rates for SD-FEC is discussed. Linear scaling of LLRs is shown to offer gains of up to 0.75 dB for a rate 0.8 LDPC code in a channel dominated by phase noise.

## A high coding-gain reduced-complexity serial concatenated error-control coding solution for wireless sensor networks

- **Status**: ✅
- **Reason**: truncated-iteration layered-decoding LDPC + Viterbi serial concatenation; layered LDPC 디코딩 기법은 NAND BP에 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7888352
- **Type**: conference
- **Published**: 2016
- **Authors**: D. P. Nguyen, T. H. Tran, Y. Nakashima
- **PDF**: https://ieeexplore.ieee.org/document/7888352
- **Abstract**: Error-Control Coding (ECC) now plays an important role in wireless transceivers because it helps to increase link reliability and lower required transmit power. One popular problem of ECC implementation is the trade-off between high coding-gain and decoder's complexity. In this paper, we propose a serial concatenated ECC solution which is a combination of truncated-iteration layered-decoding LDPC block code with low-constraint Viterbi decoder at low code rate. Simulation results show that very high coding-gain and reduced-complexity are achieved. This paper also gives a supposition about applying low code rate ECC for less-active wireless nodes in Wireless Sensor Networks (WSN) to reduce transmit power and expand sensor network topology.

## Spatially-coupled codes approach symmetric information rate of finite-state Markov fading channels

- **Status**: ✅
- **Reason**: SC-LDPC + 결합 반복 채널추정/디코딩 구성, 바이너리 SC-LDPC 코드설계 기법 이식 가능(애매하나 살림)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7541793
- **Type**: conference
- **Published**: 2016
- **Authors**: H. Abe, K. Kasai
- **PDF**: https://ieeexplore.ieee.org/document/7541793
- **Abstract**: Fukushima et al. proved that spatially-coupled codes, without pilot symbols and any optimization for the channels, universally achieve the symmetric information rate (SIR) of generalized erasure channels with memory. We expect that the universality is also valid for fading channels. The receiver performs joint iterative channel estimation and decoding where factor-graphs-based BCJR channel estimator for finite-state Markov channels and the LDPC decoder are considered. We demonstrate that the reliable transmission is possible at a rate close to the SIR.

## Variable-Rate Anytime Transmission with Feedback

- **Status**: ✅
- **Reason**: SC(LDPC convolutional) 코드 구성·유한길이 설계(E), 신규 저율 코드 구조 제시
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7881963
- **Type**: conference
- **Published**: 2016
- **Authors**: L. Grosjean, R. Thobaben, L. K. Rasmussen +1
- **PDF**: https://ieeexplore.ieee.org/document/7881963
- **Abstract**: A generalization of the ensemble of non-terminated systematic LDPC convolutional codes developed in our previous work is proposed that allows us to design codes with lower rates than the original structure. We show that over the BEC, the modified codes have improved asymptotic and finite-length behavior and we determine the operational anytime exponent. Having shown the advantages of lowering the rate of the code, we propose a feedback protocol that permits encoder and decoder to operate at a variable rate. The rate is set on-the-fly and depends on the decoding success of the decoder. We describe the construction of the variable rate code structure and demonstrate by simulations the superiority of the variable rate scheme as compared to a scheme using a fixed rate.

## Multi-pass joint Viterbi detector decoder (MP-JVDD) over AWGN/ISI channels

- **Status**: ✅
- **Reason**: 패리티검사행렬 기반 joint Viterbi detector-decoder; 패리티검사 제약을 trellis에서 활용하는 디코더 기법으로 LDPC BP에 이식 검토 여지(C, 애매하여 살림)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7440725
- **Type**: conference
- **Published**: 2016
- **Authors**: A. James, K. S. Chan
- **PDF**: https://ieeexplore.ieee.org/document/7440725
- **Abstract**: In this paper, a new two-stage joint detector/decoder named the multi-pass joint Viterbi detector decoder (MP-JVDD) is proposed as an alternative to the iterative detector-decoder (IDD) and the originally proposed JVDD. The MP-JVDD operates on a trellis with the first stage estimating the minimum metric sequence (MMS) similar to a normal Viterbi algorithm, while the second stage utilizes the estimated MMS to perform a decoding search for the minimum metric legal codeword (MMLC). This is achieved by utilizing the parity check matrix (H) to identify survivor path transitions and illegal survivors in the trellis. The survivor path transitions occur only at nodes in the trellis corresponding to each parity check constraint. The corresponding survivors in the trellis are checked for parity upon reaching the last node of each parity check constraint in turn. The survivors violating the parity checks are discarded and thus only survivors corresponding to legal codewords make it through. In contrast to JVDD, the MP-JVDD considers path transitions of survivors only at the parity check nodes. However, this has to be repeated for every parity check in H. Herein lies the multi-pass nature of the algorithm - one pass per parity check. Each pass has substantially fewer survivors, since possible path transitions are considered for only the parity check nodes. This results in lower memory and computational requirements for the algorithm which has been verified through extensive simulation studies.

## CPE: Codeword Prediction Encoder

- **Status**: ✅
- **Reason**: 불신뢰 HW(게이트 오류)하 min-sum 디코딩 기반 부호워드예측 인코더, min-sum 디코더 강건성 기법 이식 가능성(C) — Phase 3 재검토
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7519283
- **Type**: conference
- **Published**: 2016
- **Authors**: S. Grandhi, E. Dupraz, C. Spagnol +2
- **PDF**: https://ieeexplore.ieee.org/document/7519283
- **Abstract**: A novel fault tolerant methodology known as Codeword Prediction Encoder (CPE) for reliable data transmission using unreliable hardware is proposed. Simulation results show that performance of CPE is much better as compared to transmitting data by employing traditional encoding methodology. It is shown that by employing Min-sum decoding mechanisms and a strong encoder r = 1/2 and dv = 4, it is possible to correct all errors given that gate errors smaller than Pg = 6e-4. In general, CPE performance improvement of upto 10K is observed when compared to the normal encoding mechanism.

## Information Bottleneck Graphs for receiver design

- **Status**: ✅
- **Reason**: Information Bottleneck Graph로 정수만 사용하는 이산 LDPC 디코더 설계 — 이식 가능한 양자화 디코더 기법(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7541827
- **Type**: conference
- **Published**: 2016
- **Authors**: J. Lewandowsky, M. Stark, G. Bauch
- **PDF**: https://ieeexplore.ieee.org/document/7541827
- **Abstract**: A generic design method for low complexity receivers is presented. The method pairs factor graphs and the Information Bottleneck method in one framework. Consequently, the method is called Information Bottleneck Graphs. The main idea of Information Bottleneck Graphs is optimizing the flow of relevant information through the signal processors. In contrast to most topical receivers with high precision signal processing units, Information Bottleneck Graphs yield receivers purely working on unsigned integers. All signal processing degenerates to lookup operations in tables of integers. Information Bottleneck Graphs are exemplarily applied to develop a complete coherent receiver including analog-to-digital conversion, channel estimation and decoding of Low Density Parity Check codes that only works on unsigned integers. This receiver uses recently introduced discrete decoders for Low Density Parity Check codes.

## An improved scheme for large scale complex field network coding based on user clustering and relay selection strategy in wireless cooperative communication

- **Status**: ✅
- **Reason**: LDPC BP에서 개량한 complex-field BP + 결합 네트워크-채널 반복디코더 — 네트워크코딩 특이적이나 디코더 기법 LDPC 유래라 애매, Phase3 재검토
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7587210
- **Type**: conference
- **Published**: 2016
- **Authors**: Y. Huang, Z. Wu, C. Jiang +1
- **PDF**: https://ieeexplore.ieee.org/document/7587210
- **Abstract**: Complex field network coding can earn larger diversity gain, better system reliability and higher network throughput in wireless communication with relay cooperative. An improved complex filed network coding scheme for large scale density network with user clustering and relay selection strategy will be proposed in this paper. The multiuser detector we employ is not based on maximum likelihood algorithm, but based on complex filed belief propagation algorithm improved from belief propagation decode algorithm of low density parity check code. As the same time, network decoding and channel decoding are combined together to form a joint network channel iterative decoder, in which the extrinsic information derive from network decode and that derive from channel decode can work well for each other. Numerical results are given to illustrate that our proposed scheme can provide better reliability, larger network diversity gain and higher throughput, more importantly, it can be well applied to large scale dense network when compared with traditional schemes.

## Channel Models for Multi-Level Cell Flash Memories Based on Empirical Error Analysis

- **Status**: ✅
- **Reason**: MLC 플래시 메모리 채널 모델(beta-binomial), NAND ECC 성능 평가에 직결(A)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7498575
- **Type**: journal
- **Published**: 2016
- **Authors**: V. Taranalli, H. Uchikawa, P. H. Siegel
- **PDF**: https://ieeexplore.ieee.org/document/7498575
- **Abstract**: We propose binary discrete parametric channel models for multi-level cell (MLC) flash memories that provide accurate error-correcting code (ECC) performance estimation by modeling the empirically observed error characteristics under program/erase cycling stress. Through a detailed empirical error characterization of 1X-nm and 2Y-nm MLC flash memory chips from two different vendors, we observe and characterize the overdispersion phenomenon in the number of bit errors per ECC frame. A well-studied channel model, such as the binary asymmetric channel model, is unable to provide accurate ECC performance estimation. Hence, we propose a channel model based on the beta-binomial probability distribution [2-beta-binomial (2-BBM) channel model], which is a good fit for the overdispersed empirical error characteristics, and show through statistical tests and simulation results for BCH, low density parity check, and polar codes, that the 2-BBM channel model provides accurate ECC performance estimation in MLC flash memories.

## Low-Power 400-Gbps Soft-Decision LDPC FEC for Optical Transport Networks

- **Status**: ✅
- **Reason**: 신규 'adaptive degeneration' 디코딩 알고리즘 + FPGA 에뮬레이션 + 28nm ASIC 합성 (이식 가능 디코더/HW, C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7542134
- **Type**: journal
- **Published**: 15 Sept.15
- **Authors**: Kevin Cushon, Per Larsson-Edefors, Peter Andrekson
- **PDF**: https://ieeexplore.ieee.org/document/7542134
- **Abstract**: We present forward error correction systems based on soft-decision low-density parity check (LDPC) codes for applications in 100-400-Gbps optical transport networks. These systems are based on the low-complexity “adaptive degeneration” decoding algorithm, which we introduce in this paper, along with randomly-structured LDPC codes with block lengths from 30 000 to 60 000 bits and overhead (OH) from 6.7% to 33%. We also construct a 3600-bit prototype LDPC code with 20% overhead, and experimentally show that it has no error floor above a bit error rate (BER) of 10-15 using a field-programmable gate array (FPGA)-based hardware emulator. The projected net coding gain at a BER of 10-15 ranges from 9.6 dB at 6.7% OH to 11.2 dB at 33% OH. We also present application-specific integrated circuit synthesis results for these decoders in 28 nm fully depleted silicon on insulator technology, which show that they are capable of 400-Gbps operation with energy consumption of under 3 pJ per information bit.

## Iteration-Aware LDPC Code Design for Low-Power Optical Communications

- **Status**: ✅
- **Reason**: 유한반복 제약하 LDPC 부호 설계법(EXIT 트래젝토리·Pareto 최적), 바이너리 LDPC 코드설계 (E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7254117
- **Type**: journal
- **Published**: 15 Jan.15,
- **Authors**: Toshiaki Koike-Akino, David S. Millar, Keisuke Kojima +4
- **PDF**: https://ieeexplore.ieee.org/document/7254117
- **Abstract**: Recent low-density parity-check (LDPC) codes have shown capacity-approaching performance for various communications systems. However, their promising performance cannot always be obtained due to practical constraints, such as finite codeword length, finite iteration, finite memory, and finite precision. In this paper, we focus on a practical design method of high-performance LDPC codes under a constraint of finite-iteration decoding for low-power optical communications. We introduce an iteration-aware LDPC code design approach, which is based on decoding trajectory in extrinsic information transfer chart analysis. It is demonstrated that an LDPC code designed by the conventional curve-fitting method exhibits nearly 2 dB of penalty, when the maximum number of iterations is limited. The results suggest that the LDPC code should be adaptively changed, e.g., when the number of decoding iterations is decreased to save power consumption. We also extend our design method to a multi-objective optimization concept by taking average degrees into account, so that the threshold and the computational complexity are minimized at the same time. The proposed Pareto-optimal codes can achieve additional 2-dB gain or 50% complexity reduction at maximum, in low-power decoding scenarios.

## Submarine Transmission Systems Using Digital Nonlinear Compensation and Adaptive Rate Forward Error Correction

- **Status**: ✅
- **Reason**: 공간결합(SC) LDPC FEC + 신규 rate 최적화 알고리즘 (코드설계 E, 바이너리)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7389319
- **Type**: journal
- **Published**: 15 April15
- **Authors**: Amirhossein Ghazisaeidi, Ivan Fernandez de Jauregui Ruiz, Laurent Schmalen +6
- **PDF**: https://ieeexplore.ieee.org/document/7389319
- **Abstract**: We report on a full C + L-band erbium-doped fiber amplified (EDFA) submarine transmission experiment of 178 wavelength-division multiplexed channels of 49-GBd polarization multiplexed 16QAM signals, achieving 54.2 Tb/s after 6600 km, with a record per-channel average net bit rate of 304.5 Gb/s. Digital backpropagation and time-domain perturbative nonlinearity compensation were alternatively applied to all channels and their respective benefits, in terms of throughput increase, reach increase, and complexity, were addressed. Multiple-rate spatially coupled low density parity check forward error correction codes with a novel rate optimization algorithm were employed. The power consumption of the power feeding equipment of our EDFA-only amplification scheme was analyzed and compared with that of hybrid EDFA Raman amplification. We also provided numerical and theoretical performance analysis of nonlinear uncompensated/compensated systems.

## Decoding Genetic Variations: Communications-Inspired Haplotype Assembly

- **Status**: ✅
- **Reason**: haplotype assembly에 bit-flipping/belief propagation 디코더 적용; 부호 비의존 BP 변형 기법 이식 가능성(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7172486
- **Type**: journal
- **Published**: 1 May-June
- **Authors**: Zrinka Puljiz, Haris Vikalo
- **PDF**: https://ieeexplore.ieee.org/document/7172486
- **Abstract**: High-throughput DNA sequencing technologies allow fast and affordable sequencing of individual genomes and thus enable unprecedented studies of genetic variations. Information about variations in the genome of an individual is provided by haplotypes, ordered collections of single nucleotide polymorphisms. Knowledge of haplotypes is instrumental in finding genes associated with diseases, drug development, and evolutionary studies. Haplotype assembly from high-throughput sequencing data is challenging due to errors and limited lengths of sequencing reads. The key observation made in this paper is that the minimum error-correction formulation of the haplotype assembly problem is identical to the task of deciphering a coded message received over a noisy channel-a classical problem in the mature field of communication theory. Exploiting this connection, we develop novel haplotype assembly schemes that rely on the bit-flipping and belief propagation algorithms often used in communication systems. The latter algorithm is then adapted to the haplotype assembly of polyploids. We demonstrate on both simulated and experimental data that the proposed algorithms compare favorably with state-of-the-art haplotype assembly methods in terms of accuracy, while being scalable and computationally efficient.
