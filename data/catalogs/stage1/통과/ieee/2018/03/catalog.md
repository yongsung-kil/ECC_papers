# IEEE Xplore — 2018-03 (1차선별 통과)


## Design and Analysis of Time-Invariant SC-LDPC Convolutional Codes With Small Constraint Length

- **Status**: ✅
- **Reason**: 이진 SC-LDPC-CC 직접 설계로 작은 제약길이+girth 기반 사이클 하한 새 구성기법(E), NAND LDPC 코드설계에 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8114265
- **Type**: journal
- **Published**: March 2018
- **Authors**: Massimo Battaglioni, Alireza Tasdighi, Giovanni Cancellieri +2
- **PDF**: https://ieeexplore.ieee.org/document/8114265
- **Abstract**: In this paper, we deal with time-invariant spatially coupled low-density parity-check convolutional codes (SC-LDPC-CCs). Classic design approaches usually start from quasi-cyclic low-density parity-check block codes and exploit suitable unwrapping procedures to obtain SC-LDPC-CCs. We show that the direct design of the SC-LDPC-CCs syndrome former matrix or, equivalently, the symbolic parity-check matrix, leads to codes with smaller syndrome former constraint lengths with respect to the best solutions available in the literature. We provide theoretical lower bounds on the syndrome former constraint length for the most relevant families of SC-LDPC-CCs, under constraints on the minimum length of cycles in their Tanner graphs. We also propose new code design techniques that approach or achieve such theoretical limits.

## Analysis and Design of Cost-Effective, High-Throughput LDPC Decoders

- **Status**: ✅
- **Reason**: NS-FAID(finite alphabet iterative decoder) 신규 min-sum 변형+고처리율 HW 아키텍처—이식 가능 디코더/HW(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8207775
- **Type**: journal
- **Published**: March 2018
- **Authors**: Thien Truong Nguyen-Ly, Valentin Savin, Khoa Le +3
- **PDF**: https://ieeexplore.ieee.org/document/8207775
- **Abstract**: This paper introduces a new approach to cost-effective, high-throughput hardware designs for low-density parity-check (LDPC) decoders. The proposed approach, called nonsurjective finite alphabet iterative decoders (NS-FAIDs), exploits the robustness of message-passing LDPC decoders to inaccuracies in the calculation of exchanged messages, and it is shown to provide a unified framework for several designs previously proposed in the literature. NS-FAIDs are optimized by density evolution for regular and irregular LDPC codes, and are shown to provide different tradeoffs between hardware complexity and decoding performance. Two hardware architectures targeting high-throughput applications are also proposed, integrating both Min-Sum (MS) and NS-FAID decoding kernels. ASIC post synthesis implementation results on 65-nm CMOS technology show that NS-FAIDs yield significant improvements in the throughput to area ratio, by up to 58.75% with respect to the MS decoder, with even better or only slightly degraded error correction performance.

## Modeling and Energy Optimization of LDPC Decoder Circuits With Timing Violations

- **Status**: ✅
- **Reason**: offset min-sum LDPC 디코더의 타이밍위반 허용 quasi-synchronous 회로 에너지 최적화—이식 가능 HW 아키텍처(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:8123836
- **Type**: journal
- **Published**: March 2018
- **Authors**: François Leduc-Primeau, Frank R. Kschischang, Warren J. Gross
- **PDF**: https://ieeexplore.ieee.org/document/8123836
- **Abstract**: This paper proposes a “quasi-synchronous” design approach for signal processing circuits, in which timing violations are permitted, but without the need for a hardware compensation mechanism. The case of a low-density parity-check (LDPC) decoder is studied, and a method for accurately modeling the effect of timing violations at a high level of abstraction is presented. The error-correction performance of code ensembles is then evaluated using density evolution, while taking into account the effect of timing faults. Following this, several quasi-synchronous LDPC decoder circuits based on the offset min-sum algorithm are optimized, providing a 23%-40% reduction in energy consumption or energy-delay product, while achieving the same performance and occupying the same area as conventional synchronous circuits.

## 4.7-Gb/s LDPC Decoder on GPU

- **Status**: ✅
- **Reason**: GPU LDPC 디코더 신규 message updating/메모리 절감으로 throughput 개선—이식 가능 디코더/HW(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8125078
- **Type**: journal
- **Published**: March 2018
- **Authors**: Jinyang Yuan, Jin Sha
- **PDF**: https://ieeexplore.ieee.org/document/8125078
- **Abstract**: Graphics processing units (GPUs) are well-suited for decoding low-density parity-check (LDPC) codes because of their massive parallelisms and high flexibility. Implementations of high-throughput GPU-based LDPC decoders are described in this letter. By applying a novel message updating scheme and reducing shared memory consumption, the flooding-based and layered-based decoders outperform the corresponding state-of-the-art designs, with 55% and 34% improvements of normalized throughputs. On a single GeForce GTX 1080 Ti GPU, the two decoders achieve 4.77- and 3.67-Gb/s throughputs by incorporating early termination criterion. Throughputs of the GPU-based decoders are comparable with an implementation on the largest density field-programmable gate array.

## Combating Bit Errors From Stuck Cells in Flash Memory Using Novel Information Theory Techniques

- **Status**: ✅
- **Reason**: A: NAND 3D 플래시 stuck cell 대응 LDPC erasure 플래깅+FNW 기법, 직접 적용
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8390326
- **Type**: conference
- **Published**: 5-8 March 
- **Authors**: Ravi Motwani, Zion S. Kwok, Poovaiah M. Palangappa
- **PDF**: https://ieeexplore.ieee.org/document/8390326
- **Abstract**: Recently, low-density parity-check (LDPC) codes have been successfully deployed in NAND Flash memory based Solid State Drives. As Flash memory scales and has now advanced from two-dimensional architectures to three-dimensional ones, defects in the form of stuck cells have increased. As far as algebraic codes like BCH are concerned, the errors from the stuck cells impact it just as any other errors. However, for LDPC codes, the stuck cells are three times as detrimental compared to other soft errors. In this work, we first propose to flag the bits read from stuck cells as erasures. It turns out that it is better that the LDPC code be informed that bits are lost as erasures rather than being erroneously informed with high confidence about the stuck cells' values. This erasures and errors correction improves the performance of the LDPC code. To realize further improvements in performance, we propose a method to reduce the raw bit error rate due to stuck cells in NAND Flash memory. We propose a divide and conquer strategy whereby we do not use all the available redundancy for LDPC parity. Instead we use some redundancy to first shape the data using sectionalized Flip and Write (FNW) so that it matches with the stuck cells read with high probability. This reduces the bit errors due to stuck cells. The residual small number of errors due to stuck cells needs to be corrected by the LDPC code. Both of the proposals have been validated with simulation results based on a one kilobyte information block encoded for an LDPC code of rate 0.9. Errors and erasures decoding, and sectionalized FNW result in 1.92× and 1.94× raw bit error gains for soft-decision decoding, respectively.

## High throughput GPU LDPC encoder and decoder for DVB-S2

- **Status**: ✅
- **Reason**: QC-LDPC GPU 인코더/디코더, intra-codeword 병렬화+조기종료 - 이식 가능 HW/병렬화 기법(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:8396831
- **Type**: conference
- **Published**: 3-10 March
- **Authors**: David Kun
- **PDF**: https://ieeexplore.ieee.org/document/8396831
- **Abstract**: Previous studies that used Graphics Processing Units (GPUs) to decode Low Density Parity Check (LDPC) codes for DVB-S2 employed inter-codeword parallelism and/or Turbo Decoding Message Passing (TDMP) to achieve high throughput. By converting the LDPC parity check matrix into a quasi-cyclic structure, we show that LDPC encoding can be efficiently implemented on a GPU, and a different approach to LDPC decoding with intra-codeword parallelism and early termination that can achieve approximately 100 Mbps increase in throughput per 0.1 dB increase in signal-to-noise ratio and, for some cases, achieve 1 Gbps or greater overall throughput.

## On the Use of Hard-Decision LDPC Decoders on MLC NAND Flash Memory

- **Status**: ✅
- **Reason**: MLC NAND에 hard-decision BF 디코더 적용·retention 특성 활용 적응 — NAND 직접(A) 및 디코더(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8570595
- **Type**: conference
- **Published**: 19-22 Marc
- **Authors**: Khoa Le, Fakhreddine Ghaffari
- **PDF**: https://ieeexplore.ieee.org/document/8570595
- **Abstract**: The soft-decision Low-Density Parity-Check (LDPC) decoders are widely used in the multi-level per cell (MLC) NAND flash memory to ensure the correctness of stored data. However, to obtain the good error correction capability, these soft-decision decoders require the soft-information, which results a long on-chip memory sensing and dramatically extends the memory read latency. In this paper, we explore the possibility of using some recent introduced Bit Flipping (BF) hard decision decoders, in replacing the soft-decision decoders, to correct the retention errors appeared in the MLC NAND flash memory. The applied BF decoders require only the hard information read from that memory to decode and thus, by avoiding soft-information sensing, the memory read latency is improved. Furthermore, by using the characteristic of the retention error where some information bits can be determined as error-free, we propose the adaptation of the BF decoders to be better adapted to MLC NAND flash memory. We show that, the adapted BF decoders can correct more erroneous bits thanks to these error-free values. The simulation results show that, the adapted BF decoders running on the flash memory provide a good error correction performance, being close to that of the soft-decision decoders, with only the hard information of the memory. In addition, it is shown that, the BF decoders provide a higher decoding speed compared to the soft-decision decoder.

## Rate-Adaptive LDPC Convolutional Coding with Joint Layered Scheduling and Shortening Design

- **Status**: ✅
- **Reason**: LDPC convolutional code의 layered scheduling+shortening+puncturing 신규 joint 설계 — 카테고리 C/E 이식 가능, 애매하여 in
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8385941
- **Type**: conference
- **Published**: 11-15 Marc
- **Authors**: Toshiaki Koike-Akino, David S. Millar, Kieran Parsons +1
- **PDF**: https://ieeexplore.ieee.org/document/8385941
- **Abstract**: We propose a joint design method of layered scheduling, shortening and puncturing for LDPC convolutional codes to be scalable across a variety of overhead ranges. Our method achieves greater than 0.4 dB gain over conventional methods.

## Error elimination ECC by horizontal error detection and vertical-LDPC ECC to increase data-retention time by 230% and acceptable bit-error rate by 90% for 3D-NAND flash SSDs

- **Status**: ✅
- **Reason**: 3D-TLC NAND 플래시 SSD용 LDPC ECC(XEE/HED/V-LDPC)로 retention 개선 — 카테고리 A NAND 직접
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8353680
- **Type**: conference
- **Published**: 11-15 Marc
- **Authors**: Shun Suzuki, Yoshiaki Deguchi, Toshiki Nakamura +2
- **PDF**: https://ieeexplore.ieee.org/document/8353680
- **Abstract**: Cross Error Elimination (XEE) ECC with Horizontal Error Detection (HED) and Vertical-LDPC (V-LDPC) is proposed to extend the data-retention lifetime of 3D-TLC NAND flash-based SSD. HED improves the error correction capability of LDPC ECC by evaluating the error bits in the horizontal direction which means the column direction. Moreover, V-LDPC improves the worst reliability in each WL in the vertical row direction through three (Upper/Middle/Lower) pages. This paper investigates the reliability improvement of 3D-TLC NAND flash memory by XEE ECC. As a result, the data-retention lifetime and the acceptable bit-error rate (BER) are extended by 230% and 90%, respectively.
