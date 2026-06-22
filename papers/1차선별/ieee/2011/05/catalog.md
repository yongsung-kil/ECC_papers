# IEEE Xplore — 2011-05 (1차선별 통과)


## Improved Stopping Set Elimination by Parity-Check Matrix Extension of LDPC Codes

- **Status**: ✅
- **Reason**: 패리티검사행렬 확장으로 small stopping set 제거 — 바이너리 LDPC 코드설계/error floor 개선 기법(E)으로 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5741762
- **Type**: journal
- **Published**: May 2011
- **Authors**: Saejoon Kim, Jun Heo, Hyuncheol Park
- **PDF**: https://ieeexplore.ieee.org/document/5741762
- **Abstract**: Stopping sets associated with a parity-check matrix of low-density parity-check codes limit the performance of iterative decoding over the binary erasure channel. In this letter, we propose a parity-check matrix extension scheme that eliminates stopping sets of small sizes. The results show that our proposed scheme provides significant performance improvement compared to previously known parity-check matrix extension schemes.

## An LDPC-based improved decoding scheme for distributed video codec

- **Status**: ✅
- **Reason**: DVC용 LDPC 디코딩에서 confidence area별 LLR 초기화 방식 제안; LLR 초기화 기법은 NAND LDPC BP로 이식 검토 여지(C, 애매하면 살림)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5898939
- **Type**: conference
- **Published**: 8-11 May 2
- **Authors**: Bin Li, Yumei Wang, Qing Huang +1
- **PDF**: https://ieeexplore.ieee.org/document/5898939
- **Abstract**: Low-density Parity-Check (LDPC) code is widely used in distributed video coding (DVC) to realizing Wyner-Ziv (WZ) coding for its better performance than other channel codes. However, during the LDPC decoding process, most of DVC solutions do not make use of the video character to help decoding. In this paper, we propose an improved LDPC decoding scheme for DVC by utilizing the movement of the objects in the video sequence to partition different confidence areas for the side information (SI). The pixels in the SI correspond to different confidence areas, and the corresponding binary representations of the pixels will have different likelihood-ratio (LLR) initialization methods which are used to generate the LLR values for LDPC iterative decoding. The experimental results show that with the proposed decoding scheme the PSNR gain can reach up to 0.8 db without increasing the decoding complexity.

## Analysis of balanced cycles of QC-LDPC codes

- **Status**: ✅
- **Reason**: QC-LDPC balanced cycle 구조·B-girth 분석 - 사이클/girth 코드설계 기법(E), 바이너리 QC-LDPC
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5872931
- **Type**: conference
- **Published**: 24-26 May 
- **Authors**: Gao Xiao, Zhang Nan
- **PDF**: https://ieeexplore.ieee.org/document/5872931
- **Abstract**: In this paper, we analyze balanced cycles of quasi-cyclic low-density parity-check (QC-LDPC) codes. We show the structure of balanced cycles and their necessary and sufficient existence conditions. Furthermore, we determine the minimal matrices of balanced cycle. Meanwhile we propose the property of B-girth in its mother matrix. Finally, we give the proof in theory.

## Real-time DVB-S2 LDPC decoding on many-core GPU accelerators

- **Status**: ✅
- **Reason**: GPU 병렬 LDPC 디코딩 알고리즘/데이터구조(D) — 바이너리 LDPC 병렬화 기법 이식 가능
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:5946824
- **Type**: conference
- **Published**: 22-27 May 
- **Authors**: Gabriel Falcao, Joao Andrade, Vitor Silva +1
- **PDF**: https://ieeexplore.ieee.org/document/5946824
- **Abstract**: It is well known that LDPC decoding is computationally demanding and one of the hardest signal operations to parallelize. Beyond data dependencies that restrict the decoding of a single word, it requires a large number of memory accesses. In this paper we propose parallel algorithms for performing in CPUs the most demanding case of irregular and long length LDPC codes adopted in the Digital Video Broadcasting Satellite 2 (DVB-S2) standard used in data communications. By performing simultaneous multicodeword decoding and adopting special data structures, experimental results show that throughputs superior to 90 Mbps can be achieved when LDPC decoders for the DVB-S2 are implemented in the current CPUs.

## A methodology based on Transportation problem modeling for designing parallel interleaver architectures

- **Status**: ✅
- **Reason**: 충돌 없는 병렬 인터리버/메모리 매핑 HW 아키텍처(D) — LDPC 디코더 병렬화에 이식 가능
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:5946806
- **Type**: conference
- **Published**: 22-27 May 
- **Authors**: Awais Sani, Philippe Coussy, Cyrille Chavet +1
- **PDF**: https://ieeexplore.ieee.org/document/5946806
- **Abstract**: For high-data-rate applications, turbo-like iterative decoders are implemented with parallel hardware architecture. However, to achieve high throughput, concurrent accesses to each memory bank has to be performed without any conflict. The consideration applies to the two main classes of turbo-like codes: Low Density Parity Check (LDPC) and Turbo-Codes. In this paper, we present an original approach based on Transportation problem modeling which finds conflict free memory mapping for every type of turbo codes and which optimizes the resulting interleaving architecture.

## Decoding of long-block soft decision LDPC codes for optical communication systems

- **Status**: ✅
- **Reason**: long-block soft-decision LDPC 디코더 조사, soft/hard 이득 정량 비교 - 애매하나 디코더 기법 이식 가능성으로 살림(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5953744
- **Type**: conference
- **Published**: 18-20 May 
- **Authors**: M. N. Sakib, A. J. Wong, W. J. Gross +1
- **PDF**: https://ieeexplore.ieee.org/document/5953744
- **Abstract**: We investigate a soft decision decoder for LDPC codes with long-block size. The results show a coding gain of 5.9 dB compared to an uncoded system and 1.5 dB over a hard decision receiver.

## Design of multi-edge-type LDPC codes for high-order coded modulation

- **Status**: ✅
- **Reason**: multi-edge-type LDPC ensemble 설계+다차원 EXIT 분석으로 임계값 최적화 — 바이너리 코드설계 기법(E) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5872111
- **Type**: conference
- **Published**: 17-20 May 
- **Authors**: Lei Zhang, Frank R. Kschischang
- **PDF**: https://ieeexplore.ieee.org/document/5872111
- **Abstract**: A design method for bandwidth-efficient LDPC coded modulation for 22m-QAM constellations at rate (2m - 1)/(2m) in complex AWGN is presented. A multi-edge-type parameterization is used to exploit the distinct bit-channel capacities unique to high-order modulation using LDPC structures. EXIT analysis is adapted to multi-edge by introducing multi-dimensional EXIT iterated-function system analysis. Under this conceptualization, a successful decoding condition is developed by estimating fixed points of the dynamical system using its numerical gradient. Optimized ensembles are found for 16-QAM with thresholds matching the best known ensembles of equal complexity. For 64 to 1024-QAM, sufficiently high bit-channel capacities allow for extension of lower-order optimized ensembles, leading a practical nested code structure. The nested structure provides flexible rate selection with a single decoder. The gap to constrained, non-iterative capacity of all optimized code ensembles of maximum variable degree of 15 is within 0.21 dB.

## A new approach for FEC decoding based on the BP algorithm in LTE and WiMAX systems

- **Status**: ✅
- **Reason**: convolutional/turbo를 H행렬 표현해 통합 BP 디코딩 — 부호 비의존 BP 기법(C)이지만 H표현·통합디코더 아이디어 이식 여지, 애매하므로 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5872112
- **Type**: conference
- **Published**: 17-20 May 
- **Authors**: Ahmed Refaey, Sébastien Roy, Paul Fortier
- **PDF**: https://ieeexplore.ieee.org/document/5872112
- **Abstract**: Many wireless communication systems such as IS-54, enhanced data rates for the GSM evolution (EDGE), worldwide interoperability for microwave access (WiMAX) and long term evolution (LTE) have adopted low-density parity-check (LDPC), tail-biting convolutional, and turbo codes as the forward error correcting codes (FEC) scheme for data and overhead channels. Therefore, many efficient algorithms have been proposed for decoding these codes. However, the different decoding approaches for these two families of codes usually lead to different hardware architectures. Since these codes work side by side in these new wireless systems, it is a good idea to introduce a universal decoder to handle these two families of codes. The present work exploits the parity-check matrix (H) representation of tail-biting convolutional and turbo codes, thus enabling decoding via a unified belief propagation (BP) algorithm. Indeed, the BP algorithm provides a highly effective general methodology for devising low-complexity iterative decoding algorithms for all convolutional code classes as well as turbo codes. While a small performance loss is observed when decoding turbo codes with BP instead of MAP, this is offset by the lower complexity of the BP algorithm and the inherent advantage of a unified decoding architecture.

## Combinatorial Properties as Predictors for the Performance of the Sum-Product Algorithm

- **Status**: ✅
- **Reason**: trapping set/조합적 성질로 error floor 예측 — 사이클제거·error floor 코드설계(E) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5872141
- **Type**: conference
- **Published**: 17-20 May 
- **Authors**: Sotiria Lampoudi, John Brevik, Michael E. O'Sullivan
- **PDF**: https://ieeexplore.ieee.org/document/5872141
- **Abstract**: We examine various algebraic/combinatorial properties of Low-Density Parity-Check codes as predictors for the performance of the sum-product algorithm on the AWGN channel in the error floor region. We consider three families of check matrices, two algebraically constructed and one sampled from an ensemble, expurgated to remove short cycles. The three families have similar properties, all are (3; 6)-regular, have girth 8, and have code length roughly 280. The best predictors are small trapping sets, and the predictive value is much higher for the algebraically constructed families than the random ones.

## Low complexity piecewise linear LLR calculation for MIMO-BICM systems

- **Status**: ✅
- **Reason**: MIMO-BICM LLR 구간선형 근사 — LLR 계산 단순화는 NAND LDPC LLR 양자화/근사로 이식 여지(C), 애매하므로 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5872149
- **Type**: conference
- **Published**: 17-20 May 
- **Authors**: Chao Zheng, Raman Yazdani, Masoud Ardakani
- **PDF**: https://ieeexplore.ieee.org/document/5872149
- **Abstract**: Log-likelihood ratios (LLRs) are efficient metrics used in the decoding of modern channel codes such as low-density parity-check and turbo codes. LLR calculation, however, can be a complex task since LLRs are usually complicated nonlinear functions of the channel output. In multi-input multioutput (MIMO) channels, the complexity of the calculation increases exponentially with the number of antennas. In this paper, an LLR approximation method is proposed for MIMO-BICM systems. In particular, piecewise linear approximation functions are introduced and an accuracy measure is provided to optimize the parameters. Simulations verify that the performance of the optimized approximate LLRs is better than the existing approximation method and quite close to that of true LLRs.

## Implementation of LDPC Encoding to DTMB Standard Based on FPGA

- **Status**: ✅
- **Reason**: irregular QC-LDPC 인코더의 SRAA 부분병렬 구조 FPGA 구현, 자원 절감 — 이식 가능 HW 인코더 아키텍처(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:6086476
- **Type**: conference
- **Published**: 16-18 May 
- **Authors**: Xiang Ouyang, Changcheng Ruan, Lingxiang Zheng
- **PDF**: https://ieeexplore.ieee.org/document/6086476
- **Abstract**: In this paper, an implementation of Low-Density Parity-Check (LDPC) encoder is introduced, which meets the demand of Chinese Digital Terrestrial Multimedia Broadcasting (DTMB) standard. A design of the LDPC encoder which uses a partially-parallel encoding structure based on the Shift Register Adder Accumulator (SRAA) circuit is studied according to the irregular quasi-cyclic characteristic of LDPC encoding specified by the standard. Then we use the FPGA to implement the design. The simulation and implementation results show that the design meets the requirement of DTMB standard and reduces the resource usage.

## Memory efficient layered decoder design with early termination for LDPC codes

- **Status**: ✅
- **Reason**: layered LDPC 조기종료+비균일 양자화+메시지 메모리 최적화 디코더 HW 기법, 이식 가능 (C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5938161
- **Type**: conference
- **Published**: 15-18 May 
- **Authors**: Jiangpeng Li, Guanghui He, Hexi Hou +2
- **PDF**: https://ieeexplore.ieee.org/document/5938161
- **Abstract**: Layered structure is widely used in the design of Low-Density Parity-Check (LDPC) code decoders due to its fast convergence speed. However, correct checking process is difficult to implement in layered decoder, which results in unnecessary iterations. In this paper, an early termination strategy is presented for layered LDPC decoder to avoid redundant number of iterations. This approach makes use of the comparison between current log-likelyhood ratios (LLRs) and updated LLRs of all variable nodes to determine termination criteria of iterations. Furthermore, a non-uniform quantization scheme and an extrinsic messages memory optimization scheme are developed for memory savings. Based on these proposed methods, an LDPC decoder for the Chinese digital mobile TV applications is implemented using a SMIC 130nm CMOS process. The decoder consumes only 171 Kbits memory while achieving 267Mbps for code rate 1/2, and 401Mbps for code rate 3/4.

## Low power LDPC decoder with efficient stopping scheme for undecodable blocks

- **Status**: ✅
- **Reason**: 저전력 LDPC 디코더의 효율적 조기종료(undecodable block 검출) 기법, 이식 가능 디코더/HW 기여 (C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5937929
- **Type**: conference
- **Published**: 15-18 May 
- **Authors**: Tinoosh Mohsenin, Houshmand Shirani-mehr, Bevan Baas
- **PDF**: https://ieeexplore.ieee.org/document/5937929
- **Abstract**: An efficient technique for early detection of undecodable blocks during LDPC decoding is introduced. The proposed method avoids unnecessary decoding iterations by predicting decoding failure and therefore results in significant improvement in power and latency in low SNR values. The proposed method which has a low hardware overhead compares the parity checksum against predefined threshold values for three iterations and terminates decoding if a condition is met. A 5.25 mm2 10GBASE-T Split-Row Threshold decoder is implemented using the proposed technique in 65 nm CMOS. The postlayout results show that at low SNR value of 3.0 dB, the decoder requires 2.3 times fewer decoding iterations which results in 23 pJ/bit energy dissipation. This is 2.4 times lower than the energy dissipation of Split-Row Threshold decoder without the proposed early stopping technique.

## Area, throughput, and energy-efficiency trade-offs in the VLSI implementation of LDPC decoders

- **Status**: ✅
- **Reason**: VLSI LDPC 디코더 서베이지만 아키텍처 정량 비교 포함(서베이 예외 조항), Phase3 재검토
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:5937927
- **Type**: conference
- **Published**: 15-18 May 
- **Authors**: C. Roth, A. Cevrero, C. Studer +2
- **PDF**: https://ieeexplore.ieee.org/document/5937927
- **Abstract**: Low-density parity-check (LDPC) codes are key ingredients for improving reliability of modern communication systems and storage devices. On the implementation side however, the design of energy-efficient and high-speed LDPC decoders with a sufficient degree of reconfigurability to meet the flexibility demands of recent standards remains challenging. This survey paper provides an overview of the state-of-the-art in the design of LDPC decoders using digital integrated circuits. To this end, we summarize available algorithms and characterize the design space. We analyze the different architectures and their connection to different codes and requirements. The advantages and disadvantages of the various choices are illustrated by comparing state-of-the-art LDPC decoder designs.

## LDPC decoder architecture for high-data rate personal-area networks

- **Status**: ✅
- **Reason**: 60GHz용 LDPC 디코더지만 fully pipelined 저전력 flexible HW 아키텍처라 NAND ECC 디코더에 이식 가능 (D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:5937930
- **Type**: conference
- **Published**: 15-18 May 
- **Authors**: Matthew Weiner, Borivoje Nikolić, Zhengya Zhang
- **PDF**: https://ieeexplore.ieee.org/document/5937930
- **Abstract**: Emerging standards for wireless communications in the 60GHz band, such as WiGig, IEEE 802.11ad, and IEEE 802.15.3c, require throughputs between 1.5 and 6Gb/s and use rate adaptive low-density parity-check (LDPC) codes as the main form of forward error correction. State-of-the-art flexible LDPC decoders cannot simultaneously achieve the high throughput mandated by these standards and the low power needed for mobile applications. This work develops a flexible, fully pipelined architecture for the IEEE 802.11ad standard capable of achieving both goals. Based on a decoder synthesized in a low-power 65nm CMOS technology, the decoder dissipates 42mW at the 1.5Gb/s throughput and 84mW at the 3Gb/s throughput for the worst-case matrix in the standard.

## An approach based on edge coloring of tripartite graph for designing parallel LDPC interleaver architecture

- **Status**: ✅
- **Reason**: tripartite 그래프 edge-coloring 기반 병렬 LDPC 인터리버/메모리매핑 신규 HW 기법, 카테고리D
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:5937914
- **Type**: conference
- **Published**: 15-18 May 
- **Authors**: Awais Sani, Philippe Coussy, Cyrille Chavet +1
- **PDF**: https://ieeexplore.ieee.org/document/5937914
- **Abstract**: A practical and feasible solution for LDPC decoder is to design partially-parallel hardware architecture. These architectures are efficient in terms of area, cost, flexibility and performances. However, this type of architecture is complex to design since concurrent read and write accesses to data have to be performed at each time instance without any conflict. To solve this memory mapping problem, we present in this paper, an original approach based on a tripartite graph modeling and a modified edge coloring algorithm to design parallel LDPC interleaver architecture.

## An adaptive analog low-density parity-check decoder based on margin propagation

- **Status**: ✅
- **Reason**: margin-propagation 기반 아날로그 LDPC 디코더 신규 알고리즘/구현, 카테고리C/D
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5937813
- **Type**: conference
- **Published**: 15-18 May 
- **Authors**: Ming Gu, Shantanu Chakrabartty
- **PDF**: https://ieeexplore.ieee.org/document/5937813
- **Abstract**: One of the key factors underlying the popularity of low-density parity-check (LDPC) codes is its iterative decoding algorithm which is amenable to efficient analog and digital implementation. However, different applications of LDPC codes (e.g. wireless sensor networks) impose different sets of constraints which include speed, bit error rates (BER) and energy efficiency. Our previous work reported an algorithmic framework for designing margin propagation (MP) based LDPC decoders where the BER performance can be traded off with its energy efficiency. In this paper we present an analog current-mode implementation of an MP-based (32,8) LDPC decoder. The implementation uses only addition, subtraction and threshold operations and hence is independent of transistor biasing and robust to variations in environmental conditions (e.g. temperature). Measured results from prototypes fabricated in a 0.5 μm CMOS process verify the functionality of a (32,8) LDPC decoder and demonstrate superior BER performance compared to the state-of-the-art analog min- sum decoder at SNR greater than 3.5 dB.

## Multi-layer parallel decoding algorithm and vlsi architecture for quasi-cyclic LDPC codes

- **Status**: ✅
- **Reason**: 멀티레이어 병렬 디코딩 알고리즘+QC-LDPC VLSI 아키텍처(층 병렬화로 처리량 K배), 이식 가능 HW/디코더 기법 (C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5937928
- **Type**: conference
- **Published**: 15-18 May 
- **Authors**: Yang Sun, Guohui Wang, Joseph R. Cavallaro
- **PDF**: https://ieeexplore.ieee.org/document/5937928
- **Abstract**: We propose a multi-layer parallel decoding algorithm and VLSI architecture for decoding of structured quasi-cyclic low-density parity-check codes. In the conventional layered decoding algorithm, the block-rows of the parity check matrix are processed sequentially, or layer after layer. The maximum number of rows that can be simultaneously processed by the conventional layered decoder is limited to the sub-matrix size. To remove this limitation and support layer-level parallelism, we extend the conventional layered decoding algorithm and architecture to enable simultaneously processing of multiple (K) layers of a parity check matrix, which will lead to a roughly K-fold throughput increase. As a case study, we have designed a double-layer parallel LDPC decoder for the IEEE 802.11n standard. The decoder was synthesized for a TSMC 45-nm CMOS technology. With a synthesis area of 0.81 mm2 and a maximum clock frequency of 815 MHz, the decoder achieves a maximum throughput of 3.0 Gbps at 15 iterations.

## Sliding Window Method for stochastic LDPC decoder

- **Status**: ✅
- **Reason**: stochastic LDPC 디코더 SWM 신규 기법+HW 절감(바이너리), 카테고리C/D
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5937811
- **Type**: conference
- **Published**: 15-18 May 
- **Authors**: Jienan Chen, Jianhao Hu
- **PDF**: https://ieeexplore.ieee.org/document/5937811
- **Abstract**: This paper proposes a Sliding Window Method (SWM) for stochastic Low Density Parity Check (LDPC) decoder designing. The SWM is formulated for solving the latch-up problem in the Variable Nodes (VN) information updating. The bit in the latch-up state is evolved from the information bit in the sliding window. Then, an optimized hardware structure is proposed for SWM. Compared with traditional VN structure, the SWM require about 35% less hardware resources to achieve the same BER performance.

## A high-throughput LDPC decoder architecture for high-rate WPAN systems

- **Status**: ✅
- **Reason**: QC-LDPC 고처리율 디코더 신규 HW(블록 레이어드+스위치망 단순화), 카테고리D
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:5937812
- **Type**: conference
- **Published**: 15-18 May 
- **Authors**: Kyung-Il Baek, Hanho Lee, Chang-Seok Choi +2
- **PDF**: https://ieeexplore.ieee.org/document/5937812
- **Abstract**: This paper presents a high-throughput memory- efficient decoder architecture for Quasi-Cyclic Low-Density Parity-Check (QC-LDPC) codes in the high-rate wireless personal area network applications. Two novel techniques which can apply to our selected QC-LDPC codes are proposed, including four-parallel block layered decoding architecture and simplification of the switch networks. The proposed architecture based on a block parallel decoding scheme replaces a crossbar- based interconnect network with a fixed wire network for a switch network. In addition, two-stage pipelining is used to improve the clock speed. A 672-bit, rate-1/2 LDPC decoder is implemented using 90 nm CMOS technology. The design achieves an information throughput of 1.45 Gbps at a clock speed of 285 MHz with a maximum of 16 iterations.

## QC-LDPC Decoding Architecture based on Stride Scheduling

- **Status**: ✅
- **Reason**: QC-LDPC stride 스케줄링 신규 기법으로 permutation network 제거, 카테고리D
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:5937814
- **Type**: conference
- **Published**: 15-18 May 
- **Authors**: Bongjin Kim, In-Cheol Park
- **PDF**: https://ieeexplore.ieee.org/document/5937814
- **Abstract**: In this paper, an area-efficient decoder architecture is proposed for the quasi-cyclic low-density parity check (QC-LDPC) codes specified in the WiMAX 802.16e standard. In order to achieve low area and maximize hardware utilization, the decoder utilizes 4 decoding function units, which is the greatest common divisor of the expansion factors. Furthermore, the decoder adopts a novel scheduling scheme, named as stride scheduling, to remove the conventional flexible permutation network and also minimize the number of memory accesses. The synthesized decoder costs 49K of logic gates and 54,144 bits of memory, while maintaining the throughput over the requirement of the WiMAX.

## Decoder Optimised Progressive Edge Growth Algorithm

- **Status**: ✅
- **Reason**: PEG 변형 코드설계(E): Sum-Product 디코더로 패리티검사 구성 최적화하는 신규 구성법
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5956769
- **Type**: conference
- **Published**: 15-18 May 
- **Authors**: C. T. Healy, R. C. de Lamare
- **PDF**: https://ieeexplore.ieee.org/document/5956769
- **Abstract**: A novel construction for irregular low density parity check (LDPC) codes based on a modification of the Progressive Edge Growth (PEG) algorithm is presented. The edge placement procedure of the PEG algorithm is enhanced by the use of the Sum-Product decoder in the design of the parity-check matrix. The proposed algorithm, like the PEG algorithm, is highly flexible in block length and rate. The codes constructed by the methods presented are tested in the AWGN channel and significant performance improvements are achieved. The flexibility of the proposed decoder optimisation operation in its application to PEG-based construction methods is then demonstrated by its use in modifying the Improved PEG (IPEG) extension to the PEG algorithm to achieve further performance gains.

## Computationally-efficient iterative decoding for storage system design: Min-Sum refined

- **Status**: ✅
- **Reason**: 스토리지용 Dual-Scaling Min-Sum(DS-MSA) 신규 디코더, min-sum 변형으로 NAND LDPC에 직접 이식 가능 (A/C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5937960
- **Type**: conference
- **Published**: 15-18 May 
- **Authors**: Ben-Yue Chang, Milos Ivkovic, Lara Dolecek
- **PDF**: https://ieeexplore.ieee.org/document/5937960
- **Abstract**: In this paper we propose a computationally-efficient, iterative decoding algorithm that is well-suited for storage systems with very stringent reliability constraints and low redundancy/high code rate requirements. The proposed Dual-Scaling Min-Sum (DS-MSA) overcomes certain deficiencies of the Min-Sum approximation when used for decoding graph-based codes. We observe that a small but non-negligible fraction of check-to-variable messages is underestimated by the Normalized Min-Sum algorithm in the low error rate region. By carefully adjusting the scaling factor for the variable-to-check message with the smallest magnitude, we develop the DS-MSA algorithm characterized by two scaling parameters. The proposed algorithm (1) outperforms Sum-Product and (Normalized) Min-Sum algorithms in the very low error rate regime, (2) maintains the low-complexity feature of the Min-Sum, and (3) can be easily combined with existing decoder implementations.

## A New High-Performance and Low-Complexity Turbo-LDPC Code

- **Status**: ✅
- **Reason**: Turbo-LDPC: LDPC product code+EIN(extrinsic info normalization)으로 BP distortion 완화. BP 개선 기법 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5957374
- **Type**: conference
- **Published**: 14-15 May 
- **Authors**: Jui-Hui Hung, Jin-Shun Shyu, Sau-Gee Chen
- **PDF**: https://ieeexplore.ieee.org/document/5957374
- **Abstract**: In this paper, a new coding scheme, named Turbo-LDPC code, is proposed. It applies LDPC codes to the product coding scheme, and performs the decoding operation iteratively between the two component codes. Besides, to boost the decoding performance, a linear extrinsic information normalization (EIN) method is also devised, which greatlyreduces the problem of belief propagation distortion ofextrinsic information after message interleaving. Altogether,the decoding performances of Turbo-LDPC codes are muchhigher than those of the original LDPC codes undercomparable computational complexities. Compared to blockturbo code combined with BCH codes, the proposed Turbo-LDPC code also has much better decoding performance as wellas lower computational complexity.

## A 16Gbps Real-Time BF-based LDPC Decoder for IEEE 802.3an Standard

- **Status**: ✅
- **Reason**: BF(bit-flipping) 기반 고처리율 LDPC 디코더, low-correlation bit flipping+syndrome vote 신규 전략. 이식 가능 디코더(C)+HW(D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5957373
- **Type**: conference
- **Published**: 14-15 May 
- **Authors**: Jui-Hui Hung, Sau-Gee Chen
- **PDF**: https://ieeexplore.ieee.org/document/5957373
- **Abstract**: Existing LDPC decoders are mostly based on belief-propagation (BP) algorithms for high decoding performance but demand high hardware cost, especially for applications with very high throughputs. In order to alleviate the problem, this work proposes a high-throughput LDPC decoder based on the much simpler bit-flipping (BF) algorithms, for the (2048, 1723) RS-LDPC code adopted in the IEEE 802.3an standard. High decoding performances and low iteration numbers are achieved by introducing a strategy of flipping low-correlation bits and an additional syndrome vote scheme. As a result, the decoding performance is comparable to the most popular BP-based min-sum algorithm (MSA) but with much lower computational complexity. Besides, the decoder achieves high hardware utilization with real-time processing capability. Synthesized with UMC 90nm process, the decoder chip area, throughput and average power dissipation are 1.22M gates, 16Gbps and 315mW,respectively, at 500MHz clock rate.

## Low complexity soft decision circuit for LDPC decoders

- **Status**: ✅
- **Reason**: LDPC soft decision 디코더의 저복잡도 회로 구현 제시, 이식 가능 HW 기법(D) 가능성
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:5951155
- **Type**: conference
- **Published**: 1-6 May 20
- **Authors**: M. N. Sakib, V. Mahalingam, A. J. Wong +2
- **PDF**: https://ieeexplore.ieee.org/document/5951155
- **Abstract**: A reduced complexity implementation is proposed of an optical receiver for the soft decoding of low density parity check codes. Coding gain of 9.4 dB is achieved using 20% of the incoming optical signal.

## Using Functional Programming to Generate an LDPC Forward Error Corrector

- **Status**: ✅
- **Reason**: 함수형 프로그래밍 기반 LDPC FEC의 FPGA 생성 툴체인, 이식 가능 HW 구현 방법론(D) 가능성
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:5771264
- **Type**: conference
- **Published**: 1-3 May 20
- **Authors**: Andy Gill, Tristan Bull, Dan DePardo +3
- **PDF**: https://ieeexplore.ieee.org/document/5771264
- **Abstract**: FPGAs as commodities offer a resource for high-performance computation that is unmatched in flexibility and price/performance. As a lab, we are interested in high-level descriptions of computation and data, and how they may be customized to map effectively on FPGA fabrics. This paper describes our tool-chain, approach and methodology to FPGA utilization. We give a case study of the generation of a low density parity checking forward error correction algorithm, and discuss the specific challenges we faced with using FPGAs as our target.
