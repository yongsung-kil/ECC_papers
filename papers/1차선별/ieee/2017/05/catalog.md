# IEEE Xplore — 2017-05 (1차선별 통과)


## Multi-Bit Flipping Decoding of LDPC Codes for NAND Storage Systems

- **Status**: ✅
- **Reason**: NAND 스토리지용 hard-info multi-bit flipping 디코더+정렬기 HW 절감, A/C/D 직접해당
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7828079
- **Type**: journal
- **Published**: May 2017
- **Authors**: Jaehwan Jung, In-Cheol Park
- **PDF**: https://ieeexplore.ieee.org/document/7828079
- **Abstract**: This letter presents a new multi-bit flipping decoding algorithm for low-density parity-check codes, which can enhance hard-information-based decoding performance for NAND storage systems. Since the conventional enhancement techniques developed for bit-flipping decoding require soft information, the long latency taken to generate the soft information, makes it hard to apply them to practical NAND storage systems. The proposed algorithm requires only hard information and achieves the better performance than previous hard-information-based algorithms. The proposed method flips multiple bits in each iteration, but the maximum number of bits to be flipped in an iteration is restricted to prevent overcorrection. To relax the hardware complexity of sorting, in addition, an efficient approximation method is proposed, reducing the hardware complexity of a 512-input sorter by 48.3% without degrading the performance noticeably.

## Construction of IRA-LDPC codes based on identity column vectors

- **Status**: ✅
- **Reason**: ICV 기반 IRA-LDPC 구성+4-girth 제거, 바이너리 코드설계 기법(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8230087
- **Type**: conference
- **Published**: 6-8 May 20
- **Authors**: Li Peng, Kai Tao, Kun Liang +1
- **PDF**: https://ieeexplore.ieee.org/document/8230087
- **Abstract**: A random-like framework of the IRA-LDPC codes based on the identity column vectors (ICV) was defined and created. A new family of the IRA-LDPC codes under the constraint of the framework was investigated using algebraic and random methods. Its structural features is that the large-sized sparse parity check matrix Hd corresponding to the information bits is extruded into two smaller-sized easy-to-compute matrices, respectively called base matrix and position matrix. The minimum decomposable unit of the parity-check matrix H is the ICV which can provide a wider selection range of code rates than the most extensively studied QC-LDPC codes. Some conditions for the IRA-LDPC code not to have any 4-girth were considered.

## Irregular repeat accumulate low-density parity-check codes based on residue class pair

- **Status**: ✅
- **Reason**: residue class pair 기반 IRA-LDPC 신규 구성법, 바이너리 코드설계 기법(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8230092
- **Type**: conference
- **Published**: 6-8 May 20
- **Authors**: Kai Tao, Li Peng, Kun Liang +1
- **PDF**: https://ieeexplore.ieee.org/document/8230092
- **Abstract**: This paper presents a new family of irregular repeat accumulate (IRA) low-density parity-check (LDPC) codes with the characteristic of random-like structure, a common feature of the practical LDPC codes adopted in most communication industrial standards. The systematic IRA-LDPC codes are defined by the parity-check matrix H = [Hd HP], in which Hd and HP correspond to the information bits and the parity bits respectively. We introduce the concept of residue class to create the residue class pair (RCP), from which we construct a compact representation of Hd matrix. It is demonstrated that, the family of designed RCP-based IRA-LDPC codes can provide better performance, higher structural level and lower memory consumption than the practical LDPC codes in some communication standards such as IEEE 802.16e and DVB-SII.

## Design of programmable parallel LDPC decoder

- **Status**: ✅
- **Reason**: NMS 디코딩의 프로그래머블 부분병렬 LDPC 디코더 HW 아키텍처(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:8230080
- **Type**: conference
- **Published**: 6-8 May 20
- **Authors**: Qian Yi, Zhu Xiaorong
- **PDF**: https://ieeexplore.ieee.org/document/8230080
- **Abstract**: A partial parallel architecture for LDPC (Low Density Parity Check Code) decoder is proposed. The overall architecture is based on MIMD (Multiple Instruction Stream Multiple Data Stream), the internal calculation unit is based on SIMD (single instruction Stream multiple data Stream). The processor uses the programmable method to realize the NMS (normalized minimum sum) decoding algorithm, can get a higher speed of calculation and easier chip layout. The architecture of the processor has passed the timing simulation on XILINX Kintex-7, the maximum clock frequency is 175MHz. Experimental results show that the structure is suitable for multi code long and multi bit rate LDPC decoder.

## Rate-compatible and high-throughput architecture designs for encoding LDPC codes

- **Status**: ✅
- **Reason**: LDPC 인코더 HW 아키텍처(D) - rate-compatible 고처리율 인코더, 메모리/SSD ECC 적응형 언급, 이식 가능
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:8050836
- **Type**: conference
- **Published**: 28-31 May 
- **Authors**: Nishil Talati, Zhiying Wang, Shahar Kvatinsky
- **PDF**: https://ieeexplore.ieee.org/document/8050836
- **Abstract**: Low-density parity-check (LDPC) codes are known for superior performance over a wide range of codes for communication and memory systems. In many practical scenarios, adaptive ECC system is preferred that can adapt to various codes with varying channel conditions since the behavior of errors changes with time and space. This paper presents two architectural designs for efficient encoding of LDPC codes to support different code rates and lengths, which can be used for several applications. The proposed designs allow switching among different codes without any hardware modification. The first proposed design achieves extremely high throughput by removing the memory from the encoder, while still being able to adapt to a few predefined codes. The other architecture can adapt to any arbitrary code by using the memory for configuration, and yet, it achieves up to 12.9× throughput and 17.5× area improvement as compared to fully-reconfigurable encoders proposed in literature.

## Concatenated LDPC-polar codes decoding through belief propagation

- **Status**: ✅
- **Reason**: LDPC-polar concatenated BP 복호(C) - 새 연접구성+BP 개선, 바이너리 LDPC BP 이식 여지 있어 살림(Phase3 재검토)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8050835
- **Type**: conference
- **Published**: 28-31 May 
- **Authors**: Syed Mohsin Abbas, YouZhe Fan, Ji Chen +1
- **PDF**: https://ieeexplore.ieee.org/document/8050835
- **Abstract**: Owing to their capacity-achieving performance and low encoding and decoding complexity, polar codes have drawn much research interests recently. Successive cancellation decoding (SCD) and belief propagation decoding (BPD) are two common approaches for decoding polar codes. SCD is sequential in nature while BPD can run in parallel. Thus BPD is more attractive for low latency applications. However BPD has some performance degradation at higher SNR when compared with SCD. Concatenating LDPC with Polar codes is one popular approach to enhance the performance of BPD, where a short LDPC code is used as an outer code and Polar code is used as an inner code. In this work we propose a new way to construct concatenated LDPC-Polar code, which not only outperforms conventional BPD and existing concatenated LDPC-Polar code but also shows a performance improvement of 0.5 dB at higher SNR regime when compared with SCD.

## Symmetric split-row LDPC decoders

- **Status**: ✅
- **Reason**: Split-Row LDPC 디코더 HW(D) - column-permuted PCM, QC-LDPC 지원 확장, 라우팅복잡도 감소 NAND 이식 가능
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:8050909
- **Type**: conference
- **Published**: 28-31 May 
- **Authors**: Mohammad Shahrad, Mahdi Shabany
- **PDF**: https://ieeexplore.ieee.org/document/8050909
- **Abstract**: LDPC codes are deployed in many modern wired and wireless communication systems. While fully-parallel LDPC decoders are very efficient, they typically suffer from routing complexity. The Split-Row method effectively reduces this complexity with a minor performance loss. This paper shows the importance of symmetry in Split-Row architectures and proves that the implementation of Split-Row decoders based on new proposed smart column-permuted versions of parity check matrices leads to a better error performance as well as a more efficient hardware. Moreover, in order to achieve optimized column-permuted parity check matrices, a heuristic approach is proposed. This method is then generalized to support QC-LDPC codes. Applied to IEEE 802.3an (10GBASE-T Ethernet) and IEEE 802.11n (Wi-Fi) LDPC decoders, the new technique improves the error performance, while leading to almost 3× speed-up in the synthesis compile time and about 10% reduction in the critical path.

## Efficient approximate layered LDPC decoder

- **Status**: ✅
- **Reason**: layered LDPC 디코더 approximate computing unit(C/D) - 소프트메시지 업데이트 근사연산 신규, NAND LDPC 디코더 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8050908
- **Type**: conference
- **Published**: 28-31 May 
- **Authors**: Yangcan Zhou, Jun Lin, Zhongfeng Wang
- **PDF**: https://ieeexplore.ieee.org/document/8050908
- **Abstract**: Energy efficient and high throughput LDPC decoders are highly demanded, especially in the coming 5-th generation (5G) mobile communication era. In this paper, to the best of our knowledge, approximate computing units (ACUs) for the update of soft messages in row layered LDPC decoders are proposed for the first time. Under the TSMC 90nm CMOS technology, the synthesis results demonstrate that for typical LDPC codes employed in industrial standards, the corresponding ACUs achieve significant reduction in critical path delay (CPD), area and energy consumption. Numerical results show that the presented ACUs cause negligible degradation in the error-correction performance.

## Hardware optimization of the perturbation for probabilistic gradient descent bit flipping decoders

- **Status**: ✅
- **Reason**: PGDBF 하드디시전 LDPC 디코더 HW 최적화(C/D) - perturbation block ASIC 구현, NAND LDPC 디코더 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8050695
- **Type**: conference
- **Published**: 28-31 May 
- **Authors**: Khoa Le, Fakhreddine Ghaffari, David Declercq +1
- **PDF**: https://ieeexplore.ieee.org/document/8050695
- **Abstract**: The Probabilistic Gradient Descent Bit-Flipping (PGDBF) decoder has been proposed as a very promising hard-decision Low-Density Parity-Check (LDPC) decoder with a large gain in error correction. However, this impressive decoding gain is reported to come along with a non-negligible extra complexity due to the additional Perturbation Block (PB) required on top of the Gradient Descent Bit-Flipping (GDBF) decoder. In this paper, an efficient solution to implement this PB is introduced which is shown to keep the decoding gain as good as the theoretical PGDBF decoder while requiring a very small hardware overhead compared to the non-probabilistic GDBF. The proposed architecture is designed basing on a statistical analysis conducted to find the key features of the randomness needed to maintain the decoding gain and to reveal the simplification directions. The efficiency of our proposed method is confirmed by the synthesis results of decoder implementations on ASIC with 65nm CMOS technology and performance simulations.

## On the Fault Tolerance of Stochastic Decoders

- **Status**: ✅
- **Reason**: stochastic LDPC 디코더의 soft-error 내성-저전력/고속 HW 디코더 기법(C/D), NAND 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7964994
- **Type**: conference
- **Published**: 22-24 May 
- **Authors**: Assem Hussein, Mohamed Elmasry, Vincent Gaudet
- **PDF**: https://ieeexplore.ieee.org/document/7964994
- **Abstract**: This paper investigates the capability of iterative decoders based on stochastic computing (stochastic decoders) to tolerate circuit soft errors while maintaining good bit error rate performance and low error floors in the context of low-density parity-check (LDPC) coding. Soft errors can be intended faults as a result of either VDD scaling to reduce power consumption or overclocking the system to achieve a higher throughput. They can also be unintended faults as a result of temperature or process variations. We developed two models to emulate these circuit errors at the system level. We apply our models to two standardized LDPC codes (10GBASE-T and WiMAX). Simulation results show that stochastic decoding is very tolerant to faults and errors. Hence, stochastic decoding can be very useful in systems with very low power or high performance requirements where we can push the limits of power or speed by lowering VDD or highly overclocking the system while maintaining good performance.

## Spatially coupled code design for three-phase bidirectional relaying

- **Status**: ✅
- **Reason**: SC-RA 공간결합 코드 설계+밀도진화 분석으로 SC-LDPC 구성(E) 이식 가능 소지, 애매하여 in
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7996524
- **Type**: conference
- **Published**: 21-25 May 
- **Authors**: Md. Noor-A-Rahim, Yong Liang Guan
- **PDF**: https://ieeexplore.ieee.org/document/7996524
- **Abstract**: In this paper, we propose a design of spatially coupled repeat-accumulate (SC-RA) codes over a three-phase bidirectional relay. The channels between the nodes are assumed binary input additive white Gaussian noise (BIAWGN) channels, while decode-and-forward (DF) relaying is considered at the relay. We present low complexity density evolution analysis for the proposed bidirectional relay code, which leads to a simple code design procedure. The performance of the proposed relay coding scheme significantly outperforms the performance of the relay code based on regular RA block code. We show that the decoding threshold of the proposed relay code approaches the theoretical limit for a wide range of design rates. We also show the finite-length performance of the proposed bidirectional relay code through simulation results.

## Improving read access time of high-performance solid-state drives via layered coding schemes

- **Status**: ✅
- **Reason**: NAND 플래시 SSD read access time 향상용 layered/erasure 코딩; 스토리지 ECC 직접(A/B)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7997031
- **Type**: conference
- **Published**: 21-25 May 
- **Authors**: Hyegyeong Park, Jaekyun Moon
- **PDF**: https://ieeexplore.ieee.org/document/7997031
- **Abstract**: We study potential enhancement of the read access speed in high-performance solid-state drives (SSDs) by coding, given speed variations across the multiple flash interfaces and assuming occasional local memory failures. Our analysis is based on a queuing model that incorporates both read request failures and node failures. It provides a clear picture on the coding-overhead and read-access-time trade-offs given read failures and node failures. The node failure in the present context reflects various limitations on the memory element level such as page failures, block failures or channel failures that occur during the access of stored data from NAND flash memory chips. A strong motivation for this work is to understand the reliability requirement of NAND chip components given a layer of erasure protection across nodes, under the latency/storage-overhead constraints.

## High Throughput FPGA Implementation for regular Non-Surjective Finite Alphabet Iterative Decoders

- **Status**: ✅
- **Reason**: NS-FAID min-sum 변형 디코더 + 고처리량 FPGA 구현으로 C/D 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7962783
- **Type**: conference
- **Published**: 21-25 May 
- **Authors**: Thien Truong Nguyen-Ly, Valentin Savin, Xavier Popon +1
- **PDF**: https://ieeexplore.ieee.org/document/7962783
- **Abstract**: This paper deals with the recently introduced class of Non-Surjective Finite Alphabet Iterative Decoders (NS-FAIDs). First, optimization results for an extended class of regular NS-FAIDs are presented. They reveal different possible trade-offs between decoding performance and hardware implementation efficiency. To validate the promises of optimized NS-FAIDs in terms of hardware implementation benefits, we propose two high-throughput hardware architectures, integrating NS-FAIDs decoding kernels. Implementation results show that NS-FAIDs allow significant improvements in terms of both throughput and hardware resources consumption, as compared to a baseline Min-Sum decoder, with even better or only slightly degraded decoding performance.

## A configurable FPGA FEC unit for Tb/s optical communication

- **Status**: ✅
- **Reason**: 설정가능 단일 FPGA FEC 디코더 HW(비트레이트/면적/지연 트레이드오프); 이식 가능 HW 아키텍처 가능성-Phase3 부호종류 확인
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:7996767
- **Type**: conference
- **Published**: 21-25 May 
- **Authors**: Jakob Dahl Andersen, Knud J. Larsen, Christian Bering B⊘gh +4
- **PDF**: https://ieeexplore.ieee.org/document/7996767
- **Abstract**: Decoding of FEC (forward error correction) for optical communication beyond 1 Tb/s is investigated. A configurable single FPGA solution is presented having configurations supporting bit-rates in the range from 40 Gb/s to 1.6 Tb/s. The design allows for trade-offs of bit-rate, footprint, and latency within the resources of the FPGA. A proof-of-concept lab experiment at 40 Gb/s was conducted and pre-FEC — post-FEC performance validated with simulated results.

## A family of LDPC codes for Binary Symmetric Channel with optimized rate

- **Status**: ✅
- **Reason**: BSC용 비정규 LDPC 앙상블 최적화 설계(근사 미사용), 바이너리 LDPC 코드설계 기여(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7985338
- **Type**: conference
- **Published**: 2-4 May 20
- **Authors**: Hassan Tavakoli
- **PDF**: https://ieeexplore.ieee.org/document/7985338
- **Abstract**: In this paper, we present a family of irregular Low-Density Parity-Check (LDPC) code ensemble, which is designed for Binary Symmetric Channel (BSC) with maximum achievable rate. Our proposed method is based on solving the optimization problem of maximum achievable rate problem based on the related code-design conditions. In the proposed method, approximation is not used and optimization variables does not relaxed, which are used typically. Simulation results show some good codes close to the capacity.

## FPGA implementation of layered low density parity check error correction codes

- **Status**: ✅
- **Reason**: D) Layered LDPC 디코더 FPGA 구현, 고정소수점 설계; 이식 가능 HW 아키텍처
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:7960719
- **Type**: conference
- **Published**: 15-18 May 
- **Authors**: Abdulsamet Çağlan, Erşen Balcısoy, Emre Kırkaya +3
- **PDF**: https://ieeexplore.ieee.org/document/7960719
- **Abstract**: In this study, Layered Low Density Parity Check (LDPC) Decoder algorithm in Error Correction Codes is implemented on FPGA. Firstly, Layered LDPC Decoder algorithm is designed with floating point in MATLAB, then fixed point model is developed. By testing Floating and Fixed point designs, transmitted information that is deformed by AWGN model is corrected by decoding iteratively. After this step, fixed point design is modelled in Verilog HDL. The design in Verilog HDL is matched with MATLAB model and then the Verilog HDL model is implemented on Xilinx Virtex 7 FPGA. Design that is implemented on FPGA has 280 MHz clock frequency and 25.426 Mbps data speed.

## An efficient equalization technique for multi-level cell flash memory storage systems

- **Status**: ✅
- **Reason**: A/C) MLC NAND ICI equalization과 LDPC 결합 joint equalization-coding; NAND 직접+이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7960261
- **Type**: conference
- **Published**: 15-18 May 
- **Authors**: Reza A. Ashrafi, Ali E. Pusane
- **PDF**: https://ieeexplore.ieee.org/document/7960261
- **Abstract**: NAND Flash memories, due to their several desirable characteristics, have recently dominated the storage technology and its global market. Multi-level cell (MLC) Flash memories, which have higher storage capacities as each cell contains more than one bit of data, have gained considerable amount of attention and researches to build smaller and denser memory cells continue. Studies have shown that, among various error sources in MLC memories, inter-cell interference is the significant one. Therefore, simple, feasible, and yet effective equalization techniques are vital for data reliability. In this paper, we have analyzed the error performance of the proposed effective equalizer, while low- density parity-check error control scheme has also been utilized to construct a joint equalization-coding scheme.

## Sign alterations of LLR values based early termination method for LT BP decoder

- **Status**: ✅
- **Reason**: C) LLR 부호변화 기반 BP 조기종료 기법, 부호 비의존적이고 바이너리 LDPC BP에 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7960434
- **Type**: conference
- **Published**: 15-18 May 
- **Authors**: Cenk Albayrak, Cemaleddin Şımşek, Kadir Türk
- **PDF**: https://ieeexplore.ieee.org/document/7960434
- **Abstract**: In this letter, a new early termination method is proposed for Luby transform (LT) belief propagation (BP) decoder. The proposed method is decided whether BP decoder output converges to original data bits by observing only sign alterations of log-likelihood ratio (LLR) messages in BP decoder structure. Simulation results and complexity analyzes show that proposed method has low computational complexity and small average iteration amounts compared to conventional early termination methods in literature. In addition to this, the proposed method doesn't cause any performance degradation in BP decoder. The method can be easily applied to code families which can be decoded by BP algorithm such as low density parity check (LDPC) codes, polar codes and Raptor codes.

## Characterization of TLC 3D-NAND Flash Endurance through Machine Learning for LDPC Code Rate Optimization

- **Status**: ✅
- **Reason**: 3D-NAND TLC 특성화·ML로 LDPC 코드레이트 최적화(A): NAND LDPC ECC 직접 관련
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7939074
- **Type**: conference
- **Published**: 14-17 May 
- **Authors**: Cristian Zambelli, Giuseppe Cancelliere, Fabrizio Riguzzi +4
- **PDF**: https://ieeexplore.ieee.org/document/7939074
- **Abstract**: The advent of the 3D-NAND Flash memories introduced significant issues in terms of characterization and system-level optimization that can be performed to increase the memory reliability over its lifetime. Indeed, the knobs that a system designer can leverage to this extent are many. In this work we show that the application of machine learning algorithms like data clustering on a large characterization data set of TLC 3D-NAND Flash devices can help the designers in optimizing the countermeasures for improving the memory reliability while reducing their implementation cost.

## AEP-LDPC ECC with Error Dispersion Coding for Burst Error Reduction of 2D and 3D NAND Flash Memories

- **Status**: ✅
- **Reason**: 3D-TLC NAND LDPC ECC에 Error Dispersion Coding으로 버스트 에러 저감(A): NAND 직접 코드설계 기법
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7939070
- **Type**: conference
- **Published**: 14-17 May 
- **Authors**: Toshiki Nakamura, Yoshiaki Deguchi, Ken Takeuchi
- **PDF**: https://ieeexplore.ieee.org/document/7939070
- **Abstract**: To improve the reliability of Triple-Level Cell (TLC) NAND flash memory, Advanced Error Prediction (AEP) low-density parity-check (LDPC) ECC with Error Dispersion Coding is proposed. In the conventional LDPC, error-correction capability is degraded due to burst errors [1]. To reduce burst errors and improve the error-correction capabilities of LDPC, this paper proposes Error Dispersion Coding (EDC) which reduces burst errors, decreases the worst bit-error rate (BER) of Upper/Middle/Lower pages, and finally extends the data-retention time of TLC NAND flash memory. By applying proposed EDC, in 3D-TLC NAND flash memory, the burst errors and the worst BER are decreased by 87% and 40%, respectively. As a result, the acceptable data-retention time is extended by 1.8 and 2.6 times in 2D and 3D-TLC NAND flash memory, respectively.

## FPGA implementation of min-sum algorithm for LDPC decoder

- **Status**: ✅
- **Reason**: FPGA min-sum LDPC 디코더 CNU/VNU 복잡도 저감+저장구조, 이식 가능 HW 아키텍처(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:8300818
- **Type**: conference
- **Published**: 11-12 May 
- **Authors**: P.V. Sreemohan, Nelsa Sebastian
- **PDF**: https://ieeexplore.ieee.org/document/8300818
- **Abstract**: Low-density parity-check codes (LDPC) are among the most powerful error correcting tools today available. In this paper, it has aimed a Field Programmable Gate Array (FPGA) implementation of LDPC decoder with less complexity. The proposed decoding structure reduces complexity of the check node unit (CNU) and the variable node unit (VNU) based on min-sum (MS) algorithm, thereby achieving less slice resources. A multiplexed storage structure is used for the storage of node messages which results in less slice resources. Hardware resources act as a crucial factor in many applications like deep space communications and its efficient utilization is an area which is highly explored. Both high performance and low complexity are expected from LDPC decoders used in space data systems. This low-complexity implementation is an efficient method to achieve the requirements put forward by many wired and wireless communication systems.
