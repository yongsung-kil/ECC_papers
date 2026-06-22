# IEEE Xplore — 2012-03 (1차선별 통과)


## Counting Short Cycles of Quasi Cyclic Protograph LDPC Codes

- **Status**: ✅
- **Reason**: QC-LDPC short cycle/girth 카운팅 효율 기법 — 바이너리 QC-LDPC 코드설계(E)에 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6150653
- **Type**: journal
- **Published**: March 2012
- **Authors**: Mehdi Karimi, Amir H. Banihashemi
- **PDF**: https://ieeexplore.ieee.org/document/6150653
- **Abstract**: An efficient method for counting short cycles in the Tanner graphs of quasi cyclic (QC) protograph low-density parity-check (LDPC) codes is presented. The method is based on the relationship between the number of short cycles in the graph and the eigenvalues of the directed edge matrix of the graph. We demonstrate that for a QC protograph LDPC code, the complexity of computing such eigenvalues can be reduced significantly by representing the directed edge matrix as a block circulant matrix. Numerical results are presented to show the lower complexity of the proposed method compared to the existing algorithms for counting short cycles. These results also reveal that QC LDPC codes on average have a superior short cycle and girth distribution compared to similar randomly constructed codes.

## Construction of One-Coincidence Sequence Quasi-Cyclic LDPC Codes of Large Girth

- **Status**: ✅
- **Reason**: OCS QC-LDPC large girth 구성, CGE로 shift값 탐색 — 바이너리 QC-LDPC 코드설계(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6157090
- **Type**: journal
- **Published**: March 2012
- **Authors**: Jen-Fa Huang, Chun-Ming Huang, Chao-Chin Yang
- **PDF**: https://ieeexplore.ieee.org/document/6157090
- **Abstract**: One approach for designing the one-coincidence sequence (OCS) low-density parity-check (LDPC) codes of large girth is investigated. These OCS-LDPC codes are quasi-cyclic, and their parity-check matrices are composed of circulant permutation matrices. Generally, the cycle structures in these codes are determined by the shift values of circulant permutation matrices, and the existence of cycles in the corresponding Tanner graph is governed by certain cycle-governing equations (CGEs). Therefore, finding the proper shift values is the key point to increase the girth of these codes. In this paper, we provide an effective method to systematically find out the CGEs for these codes of girth 6, 8, and 10, respectively. Then, one less computation-intensive algorithm is used to generate the proper shift values for constructing the OCS-LDPC codes of large girth. Simulation results show that significant gains in signal-to-noise ratio over an additive white-Gaussian noise channel can be achieved by increasing the girth of the OCS-LDPC codes.

## Analysis and Design of Binary Message Passing Decoders

- **Status**: ✅
- **Reason**: 바이너리 메시지패싱 LDPC 디코더 설계(2비트 채널출력 최적화, Gallager B 개선, 사이클 조건) — 이식 가능 디코더 C
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6118253
- **Type**: journal
- **Published**: March 2012
- **Authors**: Gottfried Lechner, Troels Pedersen, Gerhard Kramer
- **PDF**: https://ieeexplore.ieee.org/document/6118253
- **Abstract**: Binary message passing decoders for low-density parity-check codes are studied by using extrinsic information transfer charts. The channel delivers hard or soft decisions and the variable node decoder performs all computations in the log-likelihood ratio (L-value) domain. A hard decision results in the Gallager B algorithm and examples show that increasing the channel output alphabet to two bits gains more than 1.0 dB in signal to noise ratio when using optimized codes. Finally, it is shown that errors on cycles consisting only of degree two and three variable nodes cannot be corrected and a necessary and sufficient condition for the existence of a cycle-free subgraph is derived.

## LDPC convolutional codes using layered decoding algorithm for high speed coherent optical transmission

- **Status**: ✅
- **Reason**: LDPC convolutional code에 layered decoding FPGA 구현(SC-LDPC 디코더/HW) - C/D 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6192118
- **Type**: conference
- **Published**: 4-8 March 
- **Authors**: Deyuan Chang, Fan Yu, Zhiyu Xiao +7
- **PDF**: https://ieeexplore.ieee.org/document/6192118
- **Abstract**: We successfully realized layered decoding for LDPC convolutional codes designed for application in high speed optical transmission systems. A relatively short code with 20% redundancy was FPGA-emulated with a Q-factor of 5.7dB at BER of 10-15.

## Rate-compatible QC-LDPC codes design in powerline communication systems

- **Status**: ✅
- **Reason**: rate-compatible QC-LDPC 부호 설계 신규 'column extension' 기법(E) — 바이너리 QC-LDPC 구성 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6201311
- **Type**: conference
- **Published**: 27-30 Marc
- **Authors**: Zaishuang Liu, Kewu Peng, Weilong Lei +2
- **PDF**: https://ieeexplore.ieee.org/document/6201311
- **Abstract**: Low-density parity-check (LDPC) codes are an important choice of the error correction codes in broadband powerline communication (PLC) systems. In this paper, a "column extension" design method for rate-compatible quasi-cyclic (QC) LDPC codes is proposed, which can provide efficient multi-rate QC-LDPC schemes for PLC systems. Based on the optimization of degree distributions among multi-rate LDPC codes, excellent performance can be achieved at each code rate. Benefiting from the nested matrix structure, the designed QC-LDPC codes facilitate the implementation of multi-rate encoder/decoder and offer the advantage of low-complexity. A comparison with the QC-LDPC codes in ITU-T G.9960 specification is performed, where the effectiveness of the proposed method and the superior performance of our designed codes are validated via extrinsic information transfer (EXIT) chart analysis and bit error rate (BER) simulations.

## Quasi-cyclic low-density parity-check codes based on decoder optimised progressive edge growth for short blocks

- **Status**: ✅
- **Reason**: E: decoder-optimised PEG로 단블록 QC-LDPC 구성, sum-product로 엣지 배치 개선 — 새 코드설계 기법, 바이너리
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6288543
- **Type**: conference
- **Published**: 25-30 Marc
- **Authors**: C. T. Healy, R. C. de Lamare
- **PDF**: https://ieeexplore.ieee.org/document/6288543
- **Abstract**: A novel construction for quasi-cyclic (QC) regular and irregular low-density parity-check (LDPC) codes based on a modification of the QC Progressive Edge Growth (PEG) algorithm is presented. Edge placement of the PEG-based algorithm is enhanced by use of the sum-product algorithm in the design of the parity-check matrix. The proposed algorithm is highly flexible in block length and rate, in particular when compared with algebraic constructions. The codes constructed by the proposed methods are tested in the AWGN channel and performance improvements are achieved. The proposed QC-LDPC codes provide an inherent trade-off between code performance and encoding/decoding complexity.

## Efficient min-sum decoding of LDPC codes based on layer schedules

- **Status**: ✅
- **Reason**: variable node 그룹화 기반 개선 layered min-sum 스케줄, FS 대비 0.3-0.5dB 이득; 이식 가능 디코더 알고리즘(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6221774
- **Type**: conference
- **Published**: 23-25 Marc
- **Authors**: Chaobo Liu, Xiaoyou Yu
- **PDF**: https://ieeexplore.ieee.org/document/6221774
- **Abstract**: Flooding schedule (FS) and shuffled schedule (SS) are the mainstream Strategy applied in LDPC iterative decoding; however, FS need lots of Hardware devices for storage and SS has low computing speed. In Deep Space communication (DSC), these shortcomings will influence performance and practicability seriously. This paper presented an improved decoding algorithm which grouping base on the variable nodes. The simulation results show that the improved decoding performance enhance 0.3-0.5dB comparing with FS in bit-error-rate (BER) of 10-7 and the decoding speed is k multiple of SS in ka wave band, k is the number of group.

## An improved LDPC decoding scheme with reverse bit order mode for distributed video codec

- **Status**: ✅
- **Reason**: LLR 계산 reverse bit order로 LDPC 디코딩 개선 — LLR 처리 기법 NAND 이식 여지(C) 애매 보존
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6310821
- **Type**: conference
- **Published**: 21-23 Marc
- **Authors**: Bin Li, Yumei Wang, Yu Liu +1
- **PDF**: https://ieeexplore.ieee.org/document/6310821
- **Abstract**: In traditional distributed video coding (DVC), considering the correlation between the adjacent bitplanes, the LDPC-based joint bitplane decoding algorithm prefers to exploiting the decoded more significant bitplanes as the prior knowledge to decode the other less significant bitplanes for the better system performance. However, the prior knowledge does not always work well, especially when the quality of the side information (SI) is not so well. Therefore, in this paper we propose a reverse bit order mode for those blocks with poor quality in the SI to improve the LDPC decoding performance. For the pixels in these blocks, their corresponding binary representations will adopt reverse bit order to calculate the likelihood-ratio (LLR) values for LDPC iterative decoding. The experimental results show that compared with the joint bitplane decoding algorithm in [5], the PSNR gain for our proposed decoding scheme can reach up to 2.4 db.

## On threshold prediction of low-density parity-check codes with structure

- **Status**: ✅
- **Reason**: 구조적 QC/RA LDPC threshold 예측·density evolution 정확화, 바이너리 코드설계 분석 이식 가능(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6310800
- **Type**: conference
- **Published**: 21-23 Marc
- **Authors**: Laurent Schmalen, Stephan ten Brink, Gottfried Lechner +1
- **PDF**: https://ieeexplore.ieee.org/document/6310800
- **Abstract**: Low-density parity-check (LDPC) codes based on structured parity check matrices are widely used due to their favorable implementation properties. Often, however, the convergence threshold is optimized based on the general LDPC code ensemble (i.e., the degree profile only) without taking into account the imposed structure, leading to a mismatch of anticipated and actual threshold performance. In this paper, we study this mismatch in more detail and restrict ourselves to the simplest yet most popular constraint: the dual-diagonal structure of the parity-check matrix of a repeat-accumulate code, enabling linear-time encoding. We show that convergence threshold predictions based on density evolution (DE) or EXIT charts need an appropriate choice of component code models. We quantify the threshold prediction error for both BEC and AWGN channels over a wide range of code rates and degree profile optimization techniques. Finally, we provide an explicit example illustrating the achievable gains by using properly designed degree profiles.

## On the performance of complexity-optimized bilayer lengthened LDPC codes for relay channels

- **Status**: ✅
- **Reason**: Bilayer lengthened LDPC 저복잡 relay 디코더 설계 — 디코더 복잡도 최적화 기법 이식 여지(C/E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6310743
- **Type**: conference
- **Published**: 21-23 Marc
- **Authors**: Osso Vahabzadeh, Masoud Salehi
- **PDF**: https://ieeexplore.ieee.org/document/6310743
- **Abstract**: In this paper, we design an extended class of complexity-optimized bilayer lengthened low-density parity-check (LDPC) codes by considering upper check nodes with different degrees. We show that by implementing a low complexity relay decoder, our designed codes outperform the rate-optimized codes in a wide range of Eb/N0's.

## Performance of efficiently-encodable iteratively-decodable block codes

- **Status**: ✅
- **Reason**: Efficiently-encodable LDPC/IRA 설계, error floor-인코딩속도 tradeoff — 바이너리 코드설계 기여(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6310815
- **Type**: conference
- **Published**: 21-23 Marc
- **Authors**: Tingjun Xie, Stephen G. Wilson
- **PDF**: https://ieeexplore.ieee.org/document/6310815
- **Abstract**: Principles for designing efficiently-encodable (EE) iteratively-decodable block codes are investigated. We assumed encoding is performed by an erasure-filling decoder and are interested in minimizing encoding time, subject to maintaining good error performance in decoding. We focus on a design parameter, called the recovery vector n, which controls the encoding speed of EE codes. When designing powerful block codes, this vector affords great flexibility in setting the encoding speed. Both analytic and simulation results indicate that faster encoding speed eventually implies a degraded error floor performance, and in practice the tradeoff between encoding speed and error floor performance should be evaluated to meet the actual application. In addition, an extra design rule is proposed for EE low-density parity-check (LDPC) codes, and we show that the popular irregular repeat accumulate (IRA) codes and efficiently-encodable rate-compatible (EERC) codes can be obtained by using such rule.

## FPGA implementation of the parity check node for min-sum LDPC decoders

- **Status**: ✅
- **Reason**: min-sum LDPC 체크노드 FPGA 구현(two-smallest 탐색 HW 최적화)으로 D 이식 가능 HW 해당
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:6211802
- **Type**: conference
- **Published**: 20-23 Marc
- **Authors**: Fernando Gutierrez, Graciela Corral-Briones, Damián Morero +2
- **PDF**: https://ieeexplore.ieee.org/document/6211802
- **Abstract**: A typical high-speed decoder implementation for an LDPC may require hundreds or even thousands of variable and check node processors. Since check node processing unit (CNPU) is far more complex than variable processing unit, hardware requirements of CNPU has a big impact on the final decoder complexity. Here, an FPGA implementation of the soft parity check node for min-sum LDPC decoders is analyzed. The hardware cost and speed of the main block of CNPU, which finds the two smallest input values, is thoroughly studied for different numbers of input values with different bit-widths. Experiments for an FPGA implementation demonstrate that hardware cost and speed vary with the number of input values in the same way as they do for an ASIC implementation. Furthermore, it is shown that more than 60% of the hardware resources of the CNPU is used for finding the two smallest input values.

## An fpga implementation of Low Density Parity-Check CodeS construction & decoding

- **Status**: ✅
- **Reason**: LDPC 구성+BP/bit-flipping 디코딩 FPGA/Verilog 구현 - 바이너리 LDPC HW 아키텍처 이식 가능(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:6188708
- **Type**: conference
- **Published**: 15-16 Marc
- **Authors**: Susmitha Remmanapudi, Balaji Bandaru
- **PDF**: https://ieeexplore.ieee.org/document/6188708
- **Abstract**: This paper presents implementation of Low Density Parity-Check (LDPC) Codes on FPGA Platform. LDPC codes has been implemented by writing Hardware Description Language (Verilog) code and targeted to a Xilinx Spartan-3E XC3S500E FPGA chip. Repeat-Accumulation LDPC codes are also constructed. Codewords have been constructed & simulated for different rates such as 1/2 rate, 1/3 rate, 1/4 rate. The iterative decoding algorithms such as Belief Propagation (BP) and Bit-Flipping has been implemented and desired simulation results were obtained using three different coding (C, Verilog-HDL, MATlab (Simulink)) styles. Synthesis has been done for LDPC codes Construction & Bit-flipping decoding using Leonardo-Spectrum and Xilinx-ISE Project Navigator. This code is useful for large and small length of block codes. So this is flexible to use for any length of code word (or) data word and also for any rate of code word. So the usage of this code leads to high performance. The above decoding algorithms can recover the original codeword in the face of large amounts of noise.

## A Network-on-Chip-based turbo/LDPC decoder architecture

- **Status**: ✅
- **Reason**: NoC 기반 turbo/LDPC 다중표준 디코더 HW 아키텍처, 병렬 라우팅/permutation 기법 NAND LDPC 디코더로 이식 가능(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:6176715
- **Type**: conference
- **Published**: 12-16 Marc
- **Authors**: Carlo Condo, Maurizio Martina, Guido Masera
- **PDF**: https://ieeexplore.ieee.org/document/6176715
- **Abstract**: The current convergence process in wireless technologies demands for strong efforts in the conceiving of highly flexible and interoperable equipments. This contribution focuses on one of the most important baseband processing units in wireless receivers, the forward error correction unit, and proposes a Network-on-Chip (NoC) based approach to the design of multi-standard decoders. High level modeling is exploited to drive the NoC optimization for a given set of both turbo and Low-Density-Parity-Check (LDPC) codes to be supported. Moreover, synthesis results prove that the proposed approach can offer a fully compliant WiMAX decoder, supporting the whole set of turbo and LDPC codes with higher throughput and an occupied area comparable or lower than previously reported flexible implementations. In particular, the mentioned design case achieves a worst-case throughput higher than 70 Mb/s at the area cost of 3.17 mm2 on a 90 nm CMOS technology.
