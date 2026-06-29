# IEEE Xplore — 2022-03 (1차선별 통과)


## Stopping-Set Assisted Reinforced Belief Propagation for Decoding Short LDPC Codes

- **Status**: ✅
- **Reason**: Stopping-set 기반 reinforced BP 디코딩, short LDPC BP 개선(C) — NAND short LDPC 디코더 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9656848
- **Type**: journal
- **Published**: March 2022
- **Authors**: Asif Ali Zamzami, Kuan-Chuan Chao, Shih-Chun Lin
- **PDF**: https://ieeexplore.ieee.org/document/9656848
- **Abstract**: The low-density parity-check (LDPC) code is chosen to be a channel coding scheme for ultra-reliable and low-latency communications (URLLC) in 5G. However, short LDPC compromises the belief propagation (BP) decoder because of the stopping set (SS) in the decoding graph. We propose to perform different node operations according to the SS. A dynamic SS selection according to the received sequence is further applied. In the length 308 5G LDPC, our decoders outperform prior work, improving BP and collaborative BP at block error probability (BLER) of  $3 \times 10^{-5}$  by around 0.176 and 0.092 dB respectively, with almost the same number of iterations.

## Area- and Energy-Efficient LDPC Decoder Using Mixed-Resolution Check-Node Processing

- **Status**: ✅
- **Reason**: Mixed-resolution check-node processing 새 디코더 HW 아키텍처(D), min-sum 변형(C) — NAND LDPC 디코더로 직접 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9530762
- **Type**: journal
- **Published**: March 2022
- **Authors**: Sangbu Yun, Byeong Yong Kong, Youngjoo Lee
- **PDF**: https://ieeexplore.ieee.org/document/9530762
- **Abstract**: A practical min-sum algorithm is associated with tree-based comparison units for the check-node operation, being a major bottleneck in designing low-cost and energy-efficient low-density parity-check (LDPC) decoders. In this brief, we present a cost-effective LDPC decoder architecture by changing its internal computing resolution for the power-hungry check-node processing. The proposed mixed-resolution comparison offers significant advantages in terms of both area and energy, while achieving error-correcting performance within 0.3 dB of the previous normalized min-sum (NMS) algorithm for a (1644, 1408) quasi-cyclic LDPC code of the 5G New Radio specifications. Compared to the baseline NMS architecture, the proposed decoder in a 65-nm CMOS technology reduces the hardware complexity and the power consumption by 28.4% and 23.1%, respectively, enhancing the area efficiency by more than 88.2%.

## High-Throughput LDPC-CC Decoders Based on Storage, Arithmetic, and Control Improvements

- **Status**: ✅
- **Reason**: LDPC-CC 디코더 storage/arithmetic/control HW 개선(D) — 바이너리 LDPC 디코더 HW 아키텍처 이식 가능
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:9647009
- **Type**: journal
- **Published**: March 2022
- **Authors**: Yuxing Chen, Hangxuan Cui, Zhongfeng Wang
- **PDF**: https://ieeexplore.ieee.org/document/9647009
- **Abstract**: This brief presents high-throughput low-density parity-check convolutional code (LDPC-CC) decoders in full compliance with the IEEE 1901 standard. The decoding architecture is improved from storage, arithmetic, and control aspects. First, to address the throughput bottleneck caused by memory bandwidth, we propose two methods, register-based and categorized memory-based (CMem-based) storage schemes. Then, the arithmetic improvement is extensively exploited for better area. Besides, the control unit is well-designed to reduce the hardware complexity. Equipped with these techniques, efficient LDPC-CC decoders for IEEE 1901 standard are developed and implemented with 55nm technology. Implementation results demonstrate that the proposed decoders can achieve more than twice the throughput of existing decoders. Furthermore, the proposed CMem-based decoder improves the area efficiency by 84.5%.

## A Polygonal Line Min-Sum Decoding Scheme for Low Density Parity Check Codes

- **Status**: ✅
- **Reason**: C: new polygonal-line min-sum (PMS/SPMS) decoder variant with adaptive correction factors; directly portable to NAND LDPC decoding
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9520687
- **Type**: journal
- **Published**: March 2022
- **Authors**: Yin Xu, Hao Ju, Dazhi He +4
- **PDF**: https://ieeexplore.ieee.org/document/9520687
- **Abstract**: Low-density parity-check (LDPC) codes are widely used as error correction codes in new generation digital TV standards, such as the second generation of terrestrial digital video broadcasting standard (DVB-T2), Advanced Television Systems Committee (ATSC) 3.0, etc. The nonlinear belief propagation (BP) algorithm has excellent decoding performance for LDPC codes, but is often simplified in hardware implementations by linear min-sum (MS) algorithm due to its high complexity. This simplification also leads to over-estimation problems, which can be corrected by adding factors in conventional algorithms (e.g., normalized min-sum (NMS), offset min-sum (OMS), and variable scaling normalized min-sum (VMS) algorithms). However, the correction factors of these modified MS algorithms cannot adapt to different channels and modulations, and the performance needs further improvement. In this paper, the concepts of over-estimation value (OEV) and over-estimation rate (OER) are introduced to describe the over-estimation problem of the MS algorithm. Then, under the guidance of OEV and OER, a polygonal line min-sum (PMS) algorithm with correction factors adapted to different channels and modulations is proposed according to LLR distribution. Following the properties of OEV and OER, PMS algorithm is further simplified into Simplified PMS (SPMS) algorithm. LDPC codes from ATSC 3.0 are adopted in this paper to evaluate SPMS algorithm in comparison with the conventional algorithms. Extensive simulation results show that the SPMS algorithm for ATSC 3.0 LDPC decoder has at most 1.61dB, 0.24dB and 0.36dB gain over NMS, OMS and VMS algorithms respectively when frame error rate (FER) is at 10−4 level over additive white Gaussian noise (AWGN) channel with QPSK modulation. More importantly, the simulation results show that the SPMS algorithm can achieve much better performance than these modified MS algorithms over AWGN and Rayleigh channel with higher-order modulations or under limited maximum iteration number.

## Error Floor Analysis of LDPC Column Layered Decoders

- **Status**: ✅
- **Reason**: LDPC column layered 디코더 error floor 분석 + trapping set 스케줄 최적화(C/E) — 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9656896
- **Type**: journal
- **Published**: March 2022
- **Authors**: Ali Farsiabi, Amir H. Banihashemi
- **PDF**: https://ieeexplore.ieee.org/document/9656896
- **Abstract**: In this letter, we analyze the error floor of column layered decoders, also known as shuffled decoders, for low-density parity-check (LDPC) codes under saturating sum-product algorithm (SPA). To estimate the error floor, we evaluate the failure rate of different trapping sets (TSs) that contribute to the frame error rate in the error floor region. For each such TS, we model the dynamics of SPA in the vicinity of the TS by a linear state-space model that incorporates the information of the layered message-passing schedule. Consequently, the model parameters and the failure rate of the TS change as a result of the change in the order by which the messages of different layers are updated. This, in turn, causes the error floor of the code to change as a function of scheduling. Based on the proposed analysis, we then devise an efficient search algorithm to find a schedule that minimizes the error floor. Simulation results are presented to verify the accuracy of the proposed error floor estimation technique.

## QC-LDPC Codes With Large Column Weight and Free of Small Size ETSs

- **Status**: ✅
- **Reason**: QC-LDPC large column weight + 8-cycle/ETS 제거 새 코드 설계(edge-coloring, rainbow cycle) — 이식 가능 코드설계(E), 바이너리.
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9663353
- **Type**: journal
- **Published**: March 2022
- **Authors**: Farzane Amirzade, Mohammad-Reza Sadeghi, Daniel Panario
- **PDF**: https://ieeexplore.ieee.org/document/9663353
- **Abstract**: An approach to improve the performance of QC-LDPC codes is the removal of harmful trapping sets by increasing the girth. However, constructing these LDPC codes with large column weights and girth more than 8 is not easy. We are concerned with protograph-based LDPC codes with large column weights and free of small size trapping sets. We use the edge-coloring technique and some concepts from graph theory such as rainbow cycles to show that for large column weights the removal of all 8-cycles but the ones we call  $\textit {rainbow 8-cycle}$  causes the elimination of several small size trapping sets. We provide a detailed theoretical analysis of these harmful trapping sets. Then, we apply them to array-based LDPC codes to significantly simplify and optimize the necessary and sufficient conditions to eliminate those 8-cycles from the Tanner graph. The given exponent matrices and simulation results show the impact of this simplification and the removal of the above mentioned 8-cycles.

## Hard Reliability-Based Ordered Statistic Decoding and Its Application to McEliece Public Key Cryptosystem

- **Status**: ✅
- **Reason**: 신디롬 기반 hard-reliability OSD 디코딩 알고리즘 — 이식 가능 디코더(C), 바이너리 LDPC. 응용이 McEliece지만 기법은 떼어낼 수 있음.
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9658510
- **Type**: journal
- **Published**: March 2022
- **Authors**: Shuyan Yu, Qin Huang
- **PDF**: https://ieeexplore.ieee.org/document/9658510
- **Abstract**: This letter constructs the hard reliability from the syndromes to decode low/moderate-density parity-check codes in an ordered statistic way. For regular codes with our proposed decoding algorithm, the error-correction capability can be determined by the column weight and the maximum column intersection of their parity-check matrices. Then, an upper bound is derived to verify their decoding performance in ultra-low region, which may be required by some applications, e.g., McEliece public key cryptosystem and optical communications. It allows us to reduce the size of McEliece public keys with strong security levels due to its good error-correction capability.

## Tail Latency Optimization for LDPC-Based High-Density and Low-Cost Flash Memory Devices

- **Status**: ✅
- **Reason**: A: LDPC-based flash memory tail-latency optimization via refresh/dual-ECC schemes; direct NAND/SSD application
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9365694
- **Type**: journal
- **Published**: March 2022
- **Authors**: Yina Lv, Liang Shi, Longfei Luo +3
- **PDF**: https://ieeexplore.ieee.org/document/9365694
- **Abstract**: Flash memory has been developed with bit density improvement, technology scaling, and 3-D stacking. With this trend, its reliability has been significantly degraded. Error correction code (ECC), such as low-density parity code (LDPC), which has strong error correction capability, has been deployed to solve this problem. However, one of the critical issues of LDPC is that it would introduce a long decoding latency on devices with low reliability. In this case, tail latency would happen, which will significantly impact the quality of service. In this work, a set of smart refresh schemes is proposed to optimize the tail latency. The basic idea of the work is to refresh data when the accessed data have a long decoding latency. Two smart refresh schemes are proposed for this work. The first refresh scheme is designed to refresh data with a long access latency when they are accessed several times. The second refresh scheme is designed to periodically check data with an extremely long access latency and refresh them. To further optimize the refresh overhead caused by the above refresh schemes, a dual-ECC-based refresh scheme is proposed. Besides, a mathematical model for all proposed schemes is constructed to clarify the benefit of each scheme. The experimental results show that the proposed schemes can significantly improve the tail latency with acceptable overhead. What is more, the access performance is well maintained compared with the state-of-the-art work.

## Flexible Upstream FEC for Higher Throughput, Efficiency, and Robustness for 50G PON

- **Status**: ✅
- **Reason**: G.hsp 50G PON 바이너리 LDPC 모자코드 shortening/puncturing 레이트 적응; 코드설계 기법 NAND 이식 가능(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9748605
- **Type**: conference
- **Published**: 6-10 March
- **Authors**: Amitkumar Mahadevan, Yannick Lefevre, Ed Harstead +3
- **PDF**: https://ieeexplore.ieee.org/document/9748605
- **Abstract**: A low-complexity flexible forward error correction scheme based on different shortening and puncturing of the standard G.hsp 50G PON LDPC mother code to achieve enhanced throughput and robustness in upstream PON is motivated and presented. © 2022 The Author(s)

## DWR: Differential Wearing for Read Performance Optimization on High-Density NAND Flash Memory

- **Status**: ✅
- **Reason**: 3D TLC NAND 플래시 read 성능/수명 최적화(차등 마모) — 카테고리 A NAND 직접
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9774738
- **Type**: conference
- **Published**: 14-23 Marc
- **Authors**: Yunpeng Song, Qiao Li, Yina Lv +2
- **PDF**: https://ieeexplore.ieee.org/document/9774738
- **Abstract**: With the cost reduction and density optimization, the read performance and lifetime of high-density NAND flash memory have been significantly degraded during the last decade. Previous works proposed to optimize lifetime with wear leveling and optimize read performance with reliability improvement. However, with wearing, the reliability and read performance will be degraded along with the life of the device. To solve this problem, a differential wearing scheme (DWR) is proposed to optimize the read performance. The basic idea of DWR is to partition the flash memory into two areas and wear them at different speeds. For the area with low wearing speed, read operations are scheduled for read performance optimization. For the area with high wearing speed, write operations are scheduled but designed to avoid generating bad blocks early. Through careful design and real workloads evaluation on 3D TLC NAND flash, DWR achieves encouraging read performance optimization with negligible impacts to the lifetime.

## Area efficient implementation of short length QC-LDPC codes for Ultra-Reliable Low-Latency Communication (URLLC) application

- **Status**: ✅
- **Reason**: 짧은 QC-LDPC 인코더 면적효율 HW 구현(barrel shifter 하드웨어 공유로 mux 37% 감소). 이식 가능 HW 아키텍처(D).
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:9774211
- **Type**: conference
- **Published**: 10-12 Marc
- **Authors**: Lakshmi J L, Jayakumari J
- **PDF**: https://ieeexplore.ieee.org/document/9774211
- **Abstract**: This paper presents an area efficient implementation of short block length and low rate Quasi cyclic (QC)-Low Density parity check code (LDPC) encoder for binary input additive white Gaussian noise channel (BIAWGN) targeting the Ultra-reliable low-latency communication (URLLC) application. The stringent prerequisites like ultra-high reliability and lesser latency have made URLLC applications most critical feature of the 5G wireless communication. In the proposed architecture the dual diagonal encoding is used to generate the codeword. The primary building block in the dual diagonal encoding is the barrel shifter, which performs the cyclic shift operations. Thus, it occupies larger part of area next to the memory blocks. This works aims at drastically reducing the number of barrel shifters using hardware sharing technique. The implementation of the encoder for short length code is done in Xilinx Virtex-7 FPGA platform. The simulation results show that the proposed architecture can reduce the number of multiplexers in the encoder architecture by 37%, thus considerably reducing the area compared to the existing architectures.
