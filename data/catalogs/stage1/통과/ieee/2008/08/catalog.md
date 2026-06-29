# IEEE Xplore — 2008-08 (1차선별 통과)


## Design Tradeoffs and Hardware Architecture for Real-Time Iterative MIMO Detection using Sphere Decoding and LDPC Coding

- **Status**: ✅
- **Reason**: MIMO sphere decoder+LDPC 반복검출 HW 아키텍처(FPGA, Virtex-5) - LDPC 디코더 HW 구현/병렬화 이식 가능(D), 애매하나 살림
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:4586298
- **Type**: journal
- **Published**: August 200
- **Authors**: Hyungjin Kim, D.-U. Lee, John D. Villasenor
- **PDF**: https://ieeexplore.ieee.org/document/4586298
- **Abstract**: We explore the performance and hardware complexity tradeoffs associated with performing iterative multiple- input multiple-output (MIMO) detection using a sphere decoder and a low-density parity-check (LDPC) decoder. Iterations are performed both within the LDPC decoder as well as via an outer iteration loop through which refined soft information is fed back from the LDPC decoder to a MIMO detector. A hardware architecture and associated implementation results on Xilinx Virtex-5 field programmable gate array for a 4 x 4 QPSK MIMO system are presented. The system offers a performance improvement of approximately 1 dB over systems without the outer iteration loop, and provides an information bit throughput that ranges from 60 to 300 megabits per second when a length 1944 rate 1/2 LDPC code is used.

## Combinatorial Interleavers for Systematic Regular Repeat-Accumulate Codes [Transactions Letters]

- **Status**: ✅
- **Reason**: RA부호용 조합적 인터리버로 4-cycle 제거+error-floor 개선, Tanner그래프 sum-product 디코딩 - 사이클 제거/코드설계 기법(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4600167
- **Type**: journal
- **Published**: August 200
- **Authors**: Sarah J. Johnson, Steven R. Weller
- **PDF**: https://ieeexplore.ieee.org/document/4600167
- **Abstract**: This paper proposes novel interleaver and accumulator structures for systematic, regular repeat-accumulate (RA) codes. It is well known that such codes are amenable to iterative (sum-product) decoding on the Tanner graph of the code, yet are as readily encodable as turbo codes. In this paper, interleavers for RA codes are designed using combinatorial techniques as a basis for deterministic interleaver constructions, yielding RA codes whose Tanner graphs are free of 4-cycles. Further, a generalized RA code accumulator structure is proposed, leading to codes, termed w3RA codes, whose parity-check matrices have many fewer weight-2 columns than conventional RA codes. The w3RA codes retain the low-complexity encoding of conventional RA codes and exhibit improved error-floor performance.

## Eliminating trapping sets in low-density parity-check codes by using Tanner graph covers

- **Status**: ✅
- **Reason**: Tanner graph cover로 trapping set 제거해 error floor 개선 — 코드설계(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4567579
- **Type**: journal
- **Published**: Aug. 2008
- **Authors**: Milos Ivkovic, Shashi Kiran Chilappagari, Bane Vasic
- **PDF**: https://ieeexplore.ieee.org/document/4567579
- **Abstract**: We discuss error floor asympotics and present a method for improving the performance of low-density parity-check (LDPC) codes in the high SNR (error floor) region. The method is based on Tanner graph covers that do not have trapping sets from the original code. The advantages of the method are that it is universal, as it can be applied to any LDPC code/channel/decoding algorithm and it improves performance at the expense of increasing the code length, without losing the code regularity, without changing the decoding algorithm, and, under certain conditions, without lowering the code rate. The proposed method can be modified to construct convolutional LDPC codes also. The method is illustrated by modifying Tanner, MacKay and Margulis codes to improve performance on the binary symmetric channel (BSC) under the Gallager B decoding algorithm. Decoding results on AWGN channel are also presented to illustrate that optimizing codes for one channel/decoding algorithm can lead to performance improvement on other channels.

## A low-cost serial decoder architecture for low-density parity-check convolutional codes

- **Status**: ✅
- **Reason**: LDPC-CC용 저비용 직렬 디코더 FPGA 아키텍처 — 이식 가능 HW(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:4447002
- **Type**: journal
- **Published**: Aug. 2008
- **Authors**: Stephen Bates, Zhengang Chen, Logan Gunthorpe +3
- **PDF**: https://ieeexplore.ieee.org/document/4447002
- **Abstract**: We propose a low-cost serial decoder architecture for low-density parity-check convolutional codes (LDPC-CCs). It has been shown that LDPC-CCs can achieve comparable performance to LDPC block codes with constraint length much less than the block length. The proposed serial decoder architecture for LDPC-CCs uses a single decoding processor. Terminated data frames are sent through the processor iteratively until correctly decoded or a maximum number of iterations is reached. This architecture saves memory consumption and uses a very small number of logic elements, making it especially suitable for strong LDPC-CCs with large code memory. The proposed architecture is realized for a (2048,3,6) regular LDPC-CC on an Altera Stratix FPGA. With a maximum of 100 iterations, the design achieves up to 9-Mb/s throughput using only a very small portion of the field-programmable gate array resources.

## Power Reduction Techniques for LDPC Decoders

- **Status**: ✅
- **Reason**: LDPC 디코더 저전력 VLSI 아키텍처+조기종료 — 이식 가능 HW(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:4578752
- **Type**: journal
- **Published**: Aug. 2008
- **Authors**: Ahmad Darabiha, Anthony Chan Carusone, Frank R. Kschischang
- **PDF**: https://ieeexplore.ieee.org/document/4578752
- **Abstract**: This paper investigates VLSI architectures for low-density parity-check (LDPC) decoders amenable to low- voltage and low-power operation. First, a highly-parallel decoder architecture with low routing overhead is described. Second, we propose an efficient method to detect early convergence of the iterative decoder and terminate the computations, thereby reducing dynamic power. We report on a bit-serial fully-parallel LDPC decoder fabricated in a 0.13-$\mu{\hbox{m}}$  CMOS process and show how the above techniques affect the power consumption. With early termination, the prototype is capable of decoding with 10.4 pJ/bit/iteration, while performing within 3 dB of the Shannon limit at a BER of 10$^{-5}$  and with 3.3 Gb/s total throughput. If operated from a 0.6 V supply, the energy consumption can be further reduced to 2.7 pJ/bit/iteration while maintaining a total throughput of 648 Mb/s, due to the highly-parallel architecture. To demonstrate the applicability of the proposed architecture for longer codes, we also report on a bit-serial fully-parallel decoder for the (2048, 1723) LDPC code in 10GBase-T standard synthesized with a 90-nm CMOS library.

## Stability analysis of an improved min-sum decoder

- **Status**: ✅
- **Reason**: 개선된 min-sum 디코더 안정성 분석+코드설계 — 이식 가능 디코더(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4601446
- **Type**: journal
- **Published**: Aug. 2008
- **Authors**: Mahdi Ramezani, Raman Yazdani, Masoud Ardakani
- **PDF**: https://ieeexplore.ieee.org/document/4601446
- **Abstract**: It has been shown that under min-sum (MS) decoding, scaling the messages at the output of check nodes can improve the performance of regular low-density parity-check (LDPC) codes. However, for irregular codes designed for the sum-product decoder, linear scaling can hinder the performance. The problem of code design for MS and linear scaling min-sum (LSMS) decoders have been recently investigated. It is shown that the gap to the capacity for LSMS codes is better than MS codes, but compared to sum-product codes the gap is still considerable. In this letter, a modified MS decoding is proposed and studied. We use the stability analysis of density evolution to show that the proposed method allows for a larger fraction of edges connected to degree-2 variable nodes than LSMS codes. Finally, by designing codes based on the modified method, we show that compared to MS and LSMS codes, a smaller gap to the capacity can indeed be achieved while the complexity of decoding remains essentially the same.

## A Construction of Linearly Encodable QC-LDPC Codes by Grouping Cyclic Shift and Block Elimination

- **Status**: ✅
- **Reason**: QC-LDPC 신규 구성(grouping cyclic shift+block elimination)으로 girth/full-rank 선형부호화 - 이식 가능 코드설계(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4609695
- **Type**: conference
- **Published**: 3-4 Aug. 2
- **Authors**: Chen Zhixiong, Yuan Jinsha
- **PDF**: https://ieeexplore.ieee.org/document/4609695
- **Abstract**: In this paper, the girth and rank property based on grouping cyclic shift of a parity-check matrix is proved firstly. Then a quasi-cyclic square matrix with full rank is constructed by grouping cyclic shift and block elimination. By proper matrix extension, we construct a parity-check matrix based on the square matrix whose column weight is close or equal to three, which is suitable for efficient encoding procedure in [3][4][11] with a near linear complexity. Simulation results show a better performance compared to array based LDPC codes and LDPC codes in 802.11n standard.

## Implementation of LDPC Decoder in DVB-S2 Using Min-Sum Algorithm

- **Status**: ✅
- **Reason**: min-sum 기반 LDPC 디코더 VHDL HW 구현 - 이식 가능 HW 아키텍처(D), 다만 표준 min-sum이라 Phase3 재검토
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:4622852
- **Type**: conference
- **Published**: 28-30 Aug.
- **Authors**: Haeseong Jeong, Jong Tae Kim
- **PDF**: https://ieeexplore.ieee.org/document/4622852
- **Abstract**: A new market on digital broadcasting is opening because of the adoption of digital video broadcasting second generation as a digital broadcasting standard in Europe. The DVB-S2 uses a low density parity check, so DVB-S2 has much fast communication speed than conventional DVB which uses Reed-Solomon code and convolutional code for error correction. In this paper, we valuate performance and implement LDPC decoder of FEC which is important sub-system of DVB-S2 using VHDL. The simulated and implemented LDPC decoder is based on the min-sum algorithm.

## Efficient code construction of (3, k) Regular LDPC codes

- **Status**: ✅
- **Reason**: (3,k) regular LDPC 신규 구성법(결정+부분랜덤, girth>=6, 인코딩 복잡도 저감) - 이식 가능 코드설계(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4632040
- **Type**: conference
- **Published**: 26-28 Aug.
- **Authors**: Silvia Anggraeni, Varun Jeoti
- **PDF**: https://ieeexplore.ieee.org/document/4632040
- **Abstract**: The efficient code construction of regular LDPC codes that can effectively reduce the encoding complexity is still attracting a lot of attention from the research community. This paper presents a code construction method for (3, k) regular LDPC code that utilizes combination of a deterministic part and a partially random part in parity check matrix design. The parity check matrix (H), consisting of parity part (Hp) and information part (Hi), is so designed as to have a girth of, at least, 6 and to generate various code rates by maintaining the number of rows in H matrix while only changing the number of columns in the information part (Hi). Our code construction is able to reduce encoding complexity by avoiding any preprocessing step during encoding.

## The F-LDPC Family: High-Performance Flexible Modern Codes for Flexible Radio

- **Status**: ✅
- **Reason**: F-LDPC 가변 부호족 — 저복잡도 고처리량 재구성 HW 친화적 설계, 이식 가능 코드설계(E)/HW(D) 여지
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4621434
- **Type**: conference
- **Published**: 25-28 Aug.
- **Authors**: Thomas R. Halford, Metin Bayram, Cenk Kose +2
- **PDF**: https://ieeexplore.ieee.org/document/4621434
- **Abstract**: Flexibility is an increasingly important aspect of radio modern design. In this paper, flexibility within the physical (PHY) layer in general, and the forward error correction (FEC) component in particular, is examined in detail. Following a discussion of the need for flexible modern code designs that exhibit universally good performance across a wide range of operational scenarios (i.e., input block size, code rate, modulation), TrellisWare Technologies, Inc.'s Flexible Low-Density Parity- Check (F-LDPC) codes are offered as an example of a high- performance modern coding solution for flexible radio designs. Specifically, the F-LDPC family offers performance within 0.8 dB of theoretical bounds across a wide range of operational scenarios with a design that is especially amenable to low-complexity, high- thoughput reconfigurable hardware implementation.

## On the Growth Rate of Irregular GLDPC Codes Weight Distribution

- **Status**: ✅
- **Reason**: 불규칙 GLDPC weight distribution 성장률·small-weight 분석 — error floor/유한길이 코드설계(E) 이식 가능 바이너리 LDPC
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4621513
- **Type**: conference
- **Published**: 25-28 Aug.
- **Authors**: E. Paolini, M. Chiani, M. Fossorier
- **PDF**: https://ieeexplore.ieee.org/document/4621513
- **Abstract**: In this paper the exponential growth rate of irregular generalized low-density parity-check (GLDPC) codes weight distribution is considered. Specifically, the Taylor series of the growth rate is expanded to the first order with the purpose of studying its behavior in correspondence with the small weight codewords. It is proved that the linear term of the Taylor series, and then the expected number of small linear-sized weight codewords of a randomly chosen GLDPC code in the irregular ensemble, is dominated by the degree-2 variable nodes and by the check nodes with minimum distance 2. A parameter is introduced, only depending on such variable and check nodes, discriminating between an exponentially small and exponentially large expected number of small weight codewords.

## Reconfigurable Architecture for LDPC and Turbo Decoding: A NoC Case Study

- **Status**: ✅
- **Reason**: LDPC/Turbo 재구성형 디코더 아키텍처(NoC/MPSoC) — 이식 가능 HW 아키텍처(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:4621490
- **Type**: conference
- **Published**: 25-28 Aug.
- **Authors**: Michelangelo Scarpellino, Ashwani Singh, Emmanuel Boutillon +1
- **PDF**: https://ieeexplore.ieee.org/document/4621490
- **Abstract**: Trends in wireless communication systems are in the direction of multi-mode systems using different algorithms to implement the baseband processing and the channel decoding. Efficient implementation of such multi-mode support requires flexible hardware. We present design and implementation of a reconfigurable processing element for a multi-processor architecture catering to both turbo and LDPC decoding needs in the context of the WiMaX (IEEE 802.16e) standard for high-throughput applications. As a case study, we evaluate the performance of our Multi Processor System on Chip (MPSoC) architecture for a 2-D Torus/Mesh interconnect topology. Evaluation results are presented based on the communication centric parameters that include network latency, network size and can be extended to any other System on Chip (SoC) interconnect topology without loss of generality.

## Hybrid decoding for one class of low-density parity-check codes

- **Status**: ✅
- **Reason**: BF 변형+OSD 캐스케이드 하이브리드 디코더로 복잡도-성능 절충, 바이너리 LDPC 이식 가능 디코더(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4685036
- **Type**: conference
- **Published**: 25-27 Aug.
- **Authors**: Guangwen Li, Xuelan Zou, Xin Wang
- **PDF**: https://ieeexplore.ieee.org/document/4685036
- **Abstract**: For high rate LDPC codes with light column weight and few redundant checks in their parity check matrix, the belief propagation (BP) decodings yield good error performance at the cost of high complexity. Aiming at seeking a effective decoder with good performance versus complexity tradeoff for this kind of LDPC codes, we present a new decoding framework which cascades a bit flipping (BF) variant with the ordered statistic decoding (OSD). During the iterative decoding of BF variant, the flipping value for each codeword bit is summed. The summation for each bit will be utilized as the reliability input for the OSD postprocessing, if no valid codeword is found after the maximum number of iterations for the BF variant is reached. With respect to the BP, simulation results show that the proposed BF-OSD achieves comparable performance with much less complexity.

## A decoding algorithm for low-density parity-check codes in impulse noise environment

- **Status**: ✅
- **Reason**: 임펄스 노이즈용 robust MPA 디코더 변형, 노이즈 모델 기반 메시지패싱 개선으로 바이너리 LDPC 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4685174
- **Type**: conference
- **Published**: 25-27 Aug.
- **Authors**: Zhijiang Xu, Limin Meng, Li Gang +1
- **PDF**: https://ieeexplore.ieee.org/document/4685174
- **Abstract**: The iterative message passing algorithm (MPA) for low-density parity-check (LDPC) codes is effective in the additive white Gaussian noise (AWGN) channels. However, the impulse interference is not negligible in many communication channels, such as power line channels, where the impulse interference greatly deteriorates the performance of MPA based on Gauss optimization. It is necessary to restudy the decoding for LDPC codes in impulse environment. We introduce symmetric alpha-stable (SαS) noise into a statistical model of impulse noise environment, and consider that interference in the receiver is a mixture of AWGN and SαS noise. Based on this noise model, we analyze the probability density function (PDF) of the mixed noise through the numerical calculation method, and propose a robust MPA (RMPA) to account for the impulse environment. The simulations show that the bit error rate (BER) performance of the proposed RMPA is robust.

## Modified min-sum decoding algorithm for LDPC codes based on classified correction

- **Status**: ✅
- **Reason**: min/sub-min 두 보정인자 적용 modified min-sum, FPGA 구현 포함 이식 가능 디코더+HW(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4685176
- **Type**: conference
- **Published**: 25-27 Aug.
- **Authors**: Zhou Zhong, Yunzhou Li, Xiang Chen +2
- **PDF**: https://ieeexplore.ieee.org/document/4685176
- **Abstract**: In this paper, a modified min-sum decoding algorithm based on classified correction is proposed for low density parity check (LDPC) codes. Different from the single correction in the normalized belief propagation (BP)-based and offset BP-based algorithms [4], the proposed algorithm utilizes two corrections for both minimum and sub-minimum magnitudes of input messages in check nodes. These two correction factors can be obtained by analyzing the offset of updated messages in check nodes between the BP and the min-sum algorithms associated with check node degree. Simulation results show that the proposed algorithm can achieve performance very close to that of the BP algorithm. Furthermore, the FPGA implementation of this algorithm can reach a throughput of 200 Mbps at BER=10-6 with lower complexity and fewer resources than the BP algorithm.

## Low-Complexity Real-Time LDPC Encoder Design for CMMB

- **Status**: ✅
- **Reason**: 저복잡도 LDPC 인코더 HW(LU분해+파이프라인+메모리구성) — 임의 H행렬 지원, 이식 가능 HW(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:4604260
- **Type**: conference
- **Published**: 15-17 Aug.
- **Authors**: Peng Wang, Yong-en Chen
- **PDF**: https://ieeexplore.ieee.org/document/4604260
- **Abstract**: Based on modified LU decomposition theory with pivoting of sparse matrix, a low-complexity real-time LDPC encoder for CMMB was presented, which can support 2 different code rate (1/2 and 3/4). Multi- staged pipeline and Pingpong buffer architectures were used to improve throughput. An efficient memory organization for storing sparse matrices was also presented. Whole design was synthesized and routed on Altera Stratix II EP2S90. Highest frequency achieved over 200 MHz, with pure encoding rate 32.44 Mbps (1/2 code rate) and 67.16 Mbps (3/4 code rate). Beside, fully-parameterized LDPC encoder can support arbitrary H matrix LDPC code with only necessary initialized data of memory blocks.

## A low power layered decoding architecture for LDPC decoder implementation for IEEE 802.11n LDPC codes

- **Status**: ✅
- **Reason**: 메모리접근 저감 layered 디코딩 + thresholding + CMOS 구현 — D(HW)/C 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5529042
- **Type**: conference
- **Published**: 11-13 Aug.
- **Authors**: Jie Jin, Chi-Ying Tsui
- **PDF**: https://ieeexplore.ieee.org/document/5529042
- **Abstract**: This paper presents a low power LDPC decoder design based on reducing the amount of memory access. By utilizing the column overlapping of the LDPC parity check matrix, the amount of access for the memory storing the posterior values is minimized. In addition, a thresholding decoding scheme is proposed which reduces the memory access by trading off the error correcting performance. The decoder was implemented in TSMC 0.18μm CMOS process. Experimental results show that for a LDPC decoder targeting for IEEE 802.11n, the power consumption of the memory and the decoder can be reduced by 72% and 24%, respectively.

## Flexible decoder architectures for irregular QC-LDPC codes

- **Status**: ✅
- **Reason**: layered + offset min-sum 기반 유연 QC-LDPC 디코더 칩 아키텍처 — C/D 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4616778
- **Type**: conference
- **Published**: 10-13 Aug.
- **Authors**: Tzu-Chieh Kuo, Alan N. Willson
- **PDF**: https://ieeexplore.ieee.org/document/4616778
- **Abstract**: A flexible and power-efficient decoder architecture employing the layered-decoding message-passing algorithm and the low-complexity offset-based Min-Sum check algorithm for irregular QC-LDPC codes is presented in this paper. The architecture is verified by implementing a programmable decoder chip compliant with the QC-LDPC codes in Mobile WiMAX standard. Compared to other published decoder implementations, the prototype decoder is 53% smaller and has better energy efficiency.
