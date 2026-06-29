# IEEE Xplore — 2007-10 (1차선별 통과)


## A Versatile Variable Rate LDPC Codec Architecture

- **Status**: ✅
- **Reason**: 가변레이트 LDPC 코덱 HW 아키텍처, HW 수정 없이 코드 동적 전환—이식 가능 HW (D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:4346665
- **Type**: journal
- **Published**: Oct. 2007
- **Authors**: Colm P. Fewer, Mark F. Flanagan, Anthony D. Fagan
- **PDF**: https://ieeexplore.ieee.org/document/4346665
- **Abstract**: This paper presents a system architecture for low-density parity-check (LDPC) codes that allows dynamic switching of LDPC codes within the encoder and decoder without hardware modification of these modules. Thus, rate compatibility is facilitated without the performance degradation inherent in a puncture-based system. This versatility also allows the LDPC system to be used in a variety of applications since the encoder and decoder can be used with codes that span a wide range of lengths and rates.

## Improved Data Recovery from Patterned Media With Inherent Jitter Noise Using Low-Density Parity-Check Codes

- **Status**: ✅
- **Reason**: 패턴드미디어 스토리지에 바이너리 LDPC+반복디코딩 적용(스토리지 ECC 일반 B), 애매하나 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4303212
- **Type**: journal
- **Published**: Oct. 2007
- **Authors**: Ioannis T. Ntokas, Paul W. Nutter, Cen J. Tjhai +1
- **PDF**: https://ieeexplore.ieee.org/document/4303212
- **Abstract**: Patterned magnetic media promises areal densities in excess of 1 Tbit/in2 for data storage. However, current imperfect patterning techniques result in a variation in the dimensions and distribution of the fabricated islands. As a result, this variation introduces jitter in the replay waveform that makes data recovery difficult. In this paper, we investigate the use of low-density parity-check (LDPC) codes and iterative decoding for mitigating the effects of lithography jitter and improving the read channel performance in patterned media storage systems. In addition, we show that the adoption of LDPC coding techniques permits an increase in the data storage capability of the medium to approximately 1.6 Tbit/in2 with acceptable bit-error-rate performance.

## Design and Test of a 175-Mb/s, Rate-1/2 (128,3,6) Low-Density Parity-Check Convolutional Code Encoder and Decoder

- **Status**: ✅
- **Reason**: LDPC-CC 인코더/디코더 VLSI 아키텍처(180nm, 10-PU 파이프라인 175Mb/s)—이식 가능 HW 디코더 (D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:4317713
- **Type**: journal
- **Published**: Oct. 2007
- **Authors**: R. Swamy, S. Bates, T.L. Brandon +4
- **PDF**: https://ieeexplore.ieee.org/document/4317713
- **Abstract**: Low-density parity-check block codes (LDPC-BCs) are quickly becoming the forward error correcting code of choice for emerging communication standards. However, low-density parity-check convolutional codes (LDPC-CCs), the convolutional counterpart of LDPC-BCs, seem to be better suited in applications with streaming data or variable sized packets. A rate-1/2, (128,3,6) LDPC-CC ASIC has been implemented in 180-nm, 1.8-V CMOS technology. We present the VLSI architecture of a register-based LDPC-CC encoder and decoder that includes an on-chip, pseudo-random additive white Gaussian noise channel emulator. The decoder comprises a pipeline of ten identical processing units and attains up to 175 Mb/s of decoded throughput.

## Implementing a 2-Gbs 1024-bit ½-rate low-density parity-check code decoder in three-dimensional integrated circuits

- **Status**: ✅
- **Reason**: 3D-IC 풀패럴렐 바이너리 LDPC 디코더 HW 구현, 이식 가능 HW 아키텍처(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:4601900
- **Type**: conference
- **Published**: 7-10 Oct. 
- **Authors**: Lili Zhou, Cherry Wakayama, Robin Panda +3
- **PDF**: https://ieeexplore.ieee.org/document/4601900
- **Abstract**: A 1024-bit, ½-rate fully parallel low-density parity-check (LDPC) code decoder has been designed and implemented using a three-dimensional (3D) 0.18??m fully depleted silicon-on-insulator (FDSOI) CMOS technology based on wafer bonding. The 3D-IC decoder was implemented with about 8M transistors, placed on three tiers, each with one active layer and three metal layers, using 6.9mm by 7.0mm of die area. It was simulated to have a 2Gbps throughput, and consume only 260mW. This first large-scale 3D application-specific integrated circuit (ASIC) with fine-grain (5μm) vertical interconnects is made possible by jointly developing a complete automated 3D design flow from a commercial 2-D design flow combined with the needed 3D-design tools. The 3D implementation is estimated to offer more than 10x power-delay-area product improvement over its corresponding 2D implementation. The work demonstrated the benefits of fine-grain 3D integration for interconnect-heavy very-large-scale digital ASIC implementation.

## Maximizing the throughput-area efficiency of fully-parallel low-density parity-check decoding with C-slow retiming and asynchronous deep pipelining

- **Status**: ✅
- **Reason**: C-slow retiming+비동기 딥파이프라이닝으로 풀패럴렐 LDPC 디코더 처리량 최적화, 이식 가능 HW(D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4601964
- **Type**: conference
- **Published**: 7-10 Oct. 
- **Authors**: Ming Su, Lili Zhou, C.-J. Richard Shi
- **PDF**: https://ieeexplore.ieee.org/document/4601964
- **Abstract**: In this paper, we apply C-slow retiming and asynchronous deep pipelining to maximize the throughput-area efficiency of fully parallel low-density-parity-check (LDPC) decoding. Pipelined decoders are implemented in a 0.18 mum FDSOI CMOS process. Experimental results show that our pipelining technique is an efficient approach to maximizing LDPC decoding throughput while minimizing the area consumption. First, pipelined decoders can achieve extraordinary high throughput which non-pipelined design cannot. Second, for the same throughput, pipelined decoders use less area than non-pipelined design. Our approach can improve the throughput of a published implementation by 4 times with only about 80% area overhead. Without using clocks, proposed asynchronous pipelined decoders are more scalable in design complexity and more robust to process-voltage-temperature variations than existing clock-based LDPC decoders.

## A Fast-Convergence Decoding Method and Memory-Efficient VLSI Decoder Architecture for Irregular LDPC Codes in the IEEE 802.16e Standards

- **Status**: ✅
- **Reason**: QC-LDPC 고속수렴 디코딩법+메모리효율 VLSI 디코더 신규(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4349918
- **Type**: conference
- **Published**: 30 Sept.-3
- **Authors**: Yeong-Luh Ueng, Chung-Chao Cheng
- **PDF**: https://ieeexplore.ieee.org/document/4349918
- **Abstract**: In this paper, we propose a modified iterative decoding algorithm to decode a special class of quasi-cyclic low- density parity-check (QC-LDPC) codes such as QC-LDPC codes used in the IEEE 802.16e standards. The proposed decoding is implemented by serially decoding block codes with identical parity-check matrix H1 derived from the parity-check matrix H of the QC-LDPC codes. The dimensions of H1 are much smaller than those of H. Extrinsic values can be passed among these block codes since the code bits of these block codes are overlapped. Hence, the proposed decoding can reduce the number of iterations required by up to forty percent without error performance loss as compared to the conventional message- passing decoding algorithm. A partially-parallel very large-scale integration (VLSI) architecture is proposed to implement such a decoding algorithm. The proposed VLSI decoder can fully take advantage of the proposed decoding to increase its throughput. In addition, the proposed decoder only needs to store check-to- variable messages and hence is memory efficient.

## Design of Rate-Compatible Irregular LDPC Codes Based on Edge Growth and Parity Splitting

- **Status**: ✅
- **Reason**: edge growth+parity splitting 기반 rate-compatible irregular LDPC 구성(E) - 바이너리 LDPC 구성 기법 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4349877
- **Type**: conference
- **Published**: 30 Sept.-3
- **Authors**: Noah Jacobsen, Robert Soni
- **PDF**: https://ieeexplore.ieee.org/document/4349877
- **Abstract**: This paper considers the design of rate-compatible low-density parity-check (LDPC) codes with optimized degree distributions for their corresponding rates. The proposed design technique is based on extension, where a high-rate base code, or daughter code, is progressively extended to lower and lower rates such that each extension code is compatible with the previously obtained codes. Specifically, two well-known parity matrix construction methodologies, edge growth and parity splitting, are adapted to yield a flexible framework for constructing rate- compatible parity check matrices with a uniform performance characteristic. The design examples provided are based on extrinsic information transfer (EXIT) chart optimizations and demonstrate good performance up to rates as low as 1/5.

## Row-Splitting Design of Low-Density Parity-Check Codes for Gbps Transmission

- **Status**: ✅
- **Reason**: row-splitting으로 다중 rate 바이너리 LDPC 부호 설계 신규 구성(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4349893
- **Type**: conference
- **Published**: 30 Sept.-3
- **Authors**: Jong-Ee Oh, Minho Cheong, Cheol-Hui Ryu +2
- **PDF**: https://ieeexplore.ieee.org/document/4349893
- **Abstract**: In this paper, we propose a design methodology of low-density parity check (LDPC) code for very high speed transmission. To support various code rates with reasonable hardware and, possibly, the type-II hybrid automatic repeat request (HARQ), a row-splitting/combining method is employed in conjunction with shortening. In row-splitting approach, a parity check matrix of a high rate mother LDPC code, saying rate 5/6, is designed first and then successively row-split the mother matrix to obtain lower rate codes. Shortening provides us another degree of freedom for rate and frame length flexibility for concatenation with MIMO system. The code performance is investigated in terms of frame error rate and compared with those of the LDPC code proposed in IEEE 802.16e standard.

## Tail-Biting LDPC Convolutional Codes Based on Protographs

- **Status**: ✅
- **Reason**: protograph 기반 tail-biting LDPC convolutional code 구성+PEG 변형+디코더 아키텍처 - 바이너리 코드설계(E)/디코더 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4349876
- **Type**: conference
- **Published**: 30 Sept.-3
- **Authors**: Marcos B. S. Tavares, Kamil Sh. Zigangirov, Gerhard P. Fettweis
- **PDF**: https://ieeexplore.ieee.org/document/4349876
- **Abstract**: In this paper, we introduce and investigate the tail- biting low-density parity-check convolutional codes (LDPCCCs) based on protographs. We show a construction algorithm for these codes, which is based on a modified version of the PEG algorithm [1] and on the unwrapping [2] technique. The basic ideas behind the decoder architecture for these codes are also discussed. Finally, the performances of the tail-biting LDPCCCs based on protographs are evaluated through computer simulations, where we also examine a family of rate-compatible codes.

## Architecture and Design Methodology for Structured LDPC Decoder

- **Status**: ✅
- **Reason**: 구조적 LDPC 디코더 아키텍처+수렴개선 코드설계 방법론 공동설계(C/D/E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4349896
- **Type**: conference
- **Published**: 30 Sept.-3
- **Authors**: Jean-Baptiste Dore, Pierre Penard, Marie-Helene Hamon
- **PDF**: https://ieeexplore.ieee.org/document/4349896
- **Abstract**: In this paper we propose a decoding architecture for turbo-like decoding algorithm of a particular class of Low-Density Parity Check codes. We define a methodology to design codes. In a first step a hardware architecture and the decoding scheduling are first selected. Then rules for the design of these codes are derived, aiming at improving the convergence of the decoding algorithm, while fitting with the proposed architecture. Last, performance results and details on the decoder implementation are provided to illustrate the interest of the approach.

## Size Compatible (SC)-Array LDPC Codes

- **Status**: ✅
- **Reason**: 임의 길이 지원 SC-Array 바이너리 LDPC 신규 코드 구성(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4349897
- **Type**: conference
- **Published**: 30 Sept.-3
- **Authors**: Daisuke Abematsu, Tomoaki Ohtsuki, Sigit P. W. Jarot +1
- **PDF**: https://ieeexplore.ieee.org/document/4349897
- **Abstract**: Array low density parity check (LDPC) codes are high-rate codes that can achieve good error rate performance in additive white Gaussian noise (AWGN) channels. However, array LDPC codes do not support arbitrary code lengths, because the code length of an array LDPC code with good error rate performance is limited to a multiple of a prime number. This paper proposes Size Compatible (SC)-array LDPC codes; they achieve good error rate performance while supporting arbitrary code lengths. We conduct computer simulations to evaluate the block error rate (BLER) performance of SC-array LDPC codes in AWGN channels. We also evaluate the corresponding performance of SC-array LDPC coded multiband OFDM systems for data transmission rates over 1 Gbps in the UWB multipath channel model CM 3. We show that if the submatrix size is a non- prime number, SC-array LDPC codes achieve better error rate performance than the conventional array LDPC codes in AWGN channels. We also show that the SC-array LDPC codes achieve better error rate performance than the punctured array LDPC codes in AWGN channels. We also show that if the submatrix size is a prime number, SC-array LDPC codes achieve the same error rate performance as conventional array LDPC codes in AWGN channels. Moreover, we show that for multiband OFDM systems with data transmission rates of over 1 Gbps, SC-array LDPC codes achieve better error rate performance than conventional array LDPC codes.

## Short Protograph-Based LDPC Codes

- **Status**: ✅
- **Reason**: short protograph 기반 바이너리 LDPC 구성(최소거리·stopping set·girth 트레이드오프), 유한길이 코드설계 E → 포함
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4454752
- **Type**: conference
- **Published**: 29-31 Oct.
- **Authors**: Dariush Divsalar, Sam Dolinar, Christopher Jones
- **PDF**: https://ieeexplore.ieee.org/document/4454752
- **Abstract**: In this paper we design protograph-based LDPC codes with short block sizes. Mainly we consider rate 1/2 codes with input block sizes 64, 128, and 256 bits. To simplify the encoder and decoder implementations for high data rate transmission, the structure of the codes is based on protographs and circulants. These codes are designed for short block sizes based on maximizing the minimum distance and stopping set size subject to a constraint on the maximum variable node degree. In particular, we consider codes with variable node degrees between 3 and 5. Increasing the node degree leads to larger minimum distances, at the expense of smaller girth. Therefore, there is a trade-off between undetected error rate performance (improved by increasing minimum distance) and the degree of sub-optimality of the iterative decoders typically used (which are adversely affected by graph loops). Various LDPC codes are compared and simulation results are provided.

## A Reliable Scheme for Cluster Storage System

- **Status**: ✅
- **Reason**: 클러스터 스토리지에 small LDPC erasure coding 적용(B 스토리지 ECC), 애매하지만 in으로 살림
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:4438578
- **Type**: conference
- **Published**: 29-31 Oct.
- **Authors**: Xu Li, Changsheng Xie, Qinqi Wei +1
- **PDF**: https://ieeexplore.ieee.org/document/4438578
- **Abstract**: An important issue in the design of large-scale cluster storage systems is their vulnerability to nodes crash and network failures. To explore the feasibility of implementing a reliable, high performance distributed cluster storage system, we adopt a reliable scheme that data are distributed across storage nodes using erasure coding with small low-density parity-check (LDPC) code. We implement our new scheme in RSC, a proof-of-concept reliable cluster storage system, along with two other well known RAID-1 and RAID-5 schemes. Performance test results show that such a reliable scheme can provide high reliability while keeping the performance overhead small.

## An Area-Efficient FPGA-Based Architecture for Fully-Parallel Stochastic LDPC Decoding

- **Status**: ✅
- **Reason**: 실용 LDPC용 첫 stochastic 완전병렬 디코딩 HW 아키텍처(FPGA) — 신규 디코더+HW(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4387554
- **Type**: conference
- **Published**: 17-19 Oct.
- **Authors**: Saeed Sharifi Tehrani, Shie Mannor, Warren J. Gross
- **PDF**: https://ieeexplore.ieee.org/document/4387554
- **Abstract**: Stochastic decoding is a new alternative method for low complexity decoding of error-correcting codes. This paper presents the first hardware architecture for stochastic decoding of practical Low-Density Parity-Check (LDPC) codes on factor graphs. The proposed architecture makes fully-parallel decoding of (long) state-of-the-art LDPC codes viable on FP-GAs. Implementation results for a (1024, 512) fully-parallel LDPC decoder shows an area requirement of about 36% of a Xilinx Virtex-4 XC4VLX200 device and a throughput of 706 Mbps at a bit-error-rate of about 1-6 with performance loss0 of about 0.1 dB, with respect to the nearly ideal floating-point sum-product algorithm with 32 iterations.

## On the Optimized Patent-Free LDPC Code Design for Content Distribution Systems

- **Status**: ✅
- **Reason**: 유한길이+점근 LDPC 코드 설계 방법론(E). 콘텐츠 분배가 응용이나 부호 설계 기법 이식 가능하므로 애매시 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4392363
- **Type**: conference
- **Published**: 17-19 Oct.
- **Authors**: Dejan Vukobratovic, Vojin Senk
- **PDF**: https://ieeexplore.ieee.org/document/4392363
- **Abstract**: In this paper, we analyze the application of asymptotic and finite-length analysis and design of low-density parity-check (LDPC) codes for the large scale content distribution systems over packet based networks, such as MBMS or DVB-H. We show connections of the classical coding theory performance measure, the Bit Error Rate (BER) performance, and the measure called the overhead factor which is of interest in the content distribution systems. We point out to LDPC codes design methods that can provide an excellent overhead factor performance. Particularly, we are interested in performance limits of the class of patent-free LDPC codes.

## Studies on Practical Low Complexity Decoding of Low-Density Parity-Check Codes

- **Status**: ✅
- **Reason**: WBF 기반 디코딩의 VLSI 이슈 분석 + 최적화된 2비트 소프트 디코딩 제안 — 이식 가능 디코더(C)+HW(D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4387547
- **Type**: conference
- **Published**: 17-19 Oct.
- **Authors**: Zhiqiang Cui, Zhongfeng Wang
- **PDF**: https://ieeexplore.ieee.org/document/4387547
- **Abstract**: This paper studies practical low complexity decoding of Low Density Parity-Check (LDPC) codes. We first investigate VLSI implementation issues of two state-of-the-art Weighted Bit Flipping (WBF) based decoding algorithms that were recently proposed in the literature. Then we present an optimized 2-bit soft decoding approach. It is shown that the proposed approach has comparable hardware complexity with either of the two WBF-based algorithms while it has significantly better decoding performance.

## Design and Analysis of LDPC Decoders for Software Defined Radio

- **Status**: ✅
- **Reason**: SDR용 스케일러블 LDPC 디코더 HW: 다중 rate/블록 지원, 데이터패스 가속·메모리·명령어로 throughput 개선 — 이식 가능 HW 아키텍처(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:4387546
- **Type**: conference
- **Published**: 17-19 Oct.
- **Authors**: Sangwon Seo, Trevor Mudge, Yuming Zhu +1
- **PDF**: https://ieeexplore.ieee.org/document/4387546
- **Abstract**: Low Density Parity Check (LDPC) codes are one of the most promising error correction codes that are being adopted by many wireless standards. This paper presents a case study for a scalable LDPC decoder supporting multiple code rates and multiple block sizes on a software defined radio (SDR) platform. Since technology scaling alone is not sufficient for current SDR architectures to meet the requirements of the next generation wireless standards, this paper presents three techniques to improve the throughput performance. The techniques are use of data path accelerators, addition of memory units and addition of a few assembly instructions. The proposed LDPC decoder implementation achieved 30.4 Mbps decoding throughput for the n=2304 and R=5/6 LDPC code outlined in the IEEE 802.16e standard.

## A minimum-latency block-serial architecture of a decoder for IEEE 802.11n LDPC codes

- **Status**: ✅
- **Reason**: 802.11n LDPC layered 디코더의 최소지연 block-serial 아키텍처+메모리 분할 최적화, NAND 이식 가능 HW 기법(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:4402504
- **Type**: conference
- **Published**: 15-17 Oct.
- **Authors**: Massimo Rovini, Giuseppe Gentile, Francesco Rossi +1
- **PDF**: https://ieeexplore.ieee.org/document/4402504
- **Abstract**: This paper describes a scalable architecture of a decoder for IEEE 802.11n low-density parity-check (LDPC) codes. The decoder runs the layered decoding algorithm and its architecture is arranged in clusters of serial functional units, which are configured to process all codes in the standard. The decoder works in pipeline, and a very effective technique to re- arrange the sequence of its elaborations is proposed in order to minimize the iteration latency; this relates to the order of the messages input and output by the processing units, as well as the sequence of layers followed for decoding. Moreover, memory optimization techniques have been applied to get a very efficient partitioning, allowing the pipeline of the operations. The synthesis on 65 nm CMOS technology with low-power standard- cell library, shows that the proposed design is suitable for portable devices, the throughput ranging from 136 to 355 Mbps, and the power consumption being below 185 mW.
