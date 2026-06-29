# IEEE Xplore — 2020-11 (1차선별 통과)


## Information Storage Bit-Flipping Decoder for LDPC Codes

- **Status**: ✅
- **Reason**: 바이너리 LDPC 하드디시전 비트플리핑 디코더(ISBF) 신규 제안 + HW 아키텍처 — C/D 이식 가능 디코더·HW
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9199287
- **Type**: journal
- **Published**: Nov. 2020
- **Authors**: Hangxuan Cui, Jun Lin, Zhongfeng Wang
- **PDF**: https://ieeexplore.ieee.org/document/9199287
- **Abstract**: Tabu-list random-penalty gradient descent bit-flipping (TRGDBF) decoder is the state-of-the-art hard-decision low-density parity-check (LDPC) decoder in terms of error-correction performance on binary symmetric channel (BSC). However, the TRGDBF decoder suffers from a long critical path caused by the global maximum-finding operation, limiting the achievable throughput. This brief proposes an information storage bit-flipping (ISBF) decoder to solve this problem. Different from the existing bit-flipping (BF) decoders which adopt serial decoding manner, in the ISBF decoder, by storing the previous decoding information, the global maximum-finding operation can be executed in parallel to other decoding operations, significantly shortening the critical path. Moreover, a nonuniform flipping rule is incorporated to achieve a better decoding performance. We also present an efficient architecture to implement the ISBF decoder. The design example demonstrates that compared to other hard-decision BF decoders, the ISBF decoder could provide both the best decoding performance and throughput on BSC.

## Enhanced Quasi-Maximum Likelihood Decoding Based on 2D Modified Min-Sum Algorithm for 5G LDPC Codes

- **Status**: ✅
- **Reason**: 2D 수정 min-sum + self-correction/메시지증폭 + EQML 재디코딩 + PPS 정지규칙, 바이너리 LDPC 디코더 개선으로 NAND 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9163247
- **Type**: journal
- **Published**: Nov. 2020
- **Authors**: Peng Kang, Yixuan Xie, Lei Yang +1
- **PDF**: https://ieeexplore.ieee.org/document/9163247
- **Abstract**: We propose a two-dimensional modified min-sum algorithm for the LDPC codes in the fifth generation (5G) networks standard to approach the error performance of the sum-product algorithm (SPA). In the proposed decoding algorithm, we adopt a partial self-correction method followed by message amplification to improve the reliability of the variable-to-check (V2C) messages. To further approach the performance of the maximum likelihood decoding for 5G short LDPC codes, we propose an enhanced quasi-maximum likelihood (EQML) decoding method. The proposed decoding method performs multiple rounds of decoding tests once the first decoding attempt fails, where the decoder inputs of the selected unreliable variable nodes are modified in each decoding test. A novel node selection method based on the sign fluctuation of V2C messages is proposed for the EQML decoding method. We also present a partial pruning stopping (PPS) rule to reduce the decoding complexity by deactivating part of the decoding tests once a valid codeword is found. A lower bound on the error performance is also derived by using the semi-analytical method. Simulation results show that the EQML decoding method outperforms the SPA with the same decoding complexity and other QML decoding methods, and it approaches the Polyanskiy-Poor-Verdú bound within 0.4 dB.

## Error Diluting: Exploiting 3-D nand Flash Process Variation for Efficient Read on LDPC-Based SSDs

- **Status**: ✅
- **Reason**: 3D NAND 플래시 LDPC SSD read 최적화(layer별 BER 활용 error diluting) — A NAND 직접
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9211439
- **Type**: journal
- **Published**: Nov. 2020
- **Authors**: Kong-Kiat Yong, Li-Pin Chang
- **PDF**: https://ieeexplore.ieee.org/document/9211439
- **Abstract**: 3-D NAND flash has become the mainstream in modern SSD designs because it offers superior bit storage density. However, while enjoying the large capacity, 3-D NAND flash is highly prone to bit errors due to its cylindrical cell structure. Modern SSDs employ the low-density parity-check (LDPC) error-correcting code to manage bit errors in 3-D NAND flash. Strong LDPC error correction is subject to a high time overhead, because it may require many sensing levels on read to obtain sufficiently confident bit input information. By exploiting the bit-error rate variation among vertical layers of 3-D NAND flash, we propose diluting bit errors of cells at error-prone, lower layers by mixing them with bit data of cells from reliable, upper layers. Cells at reliable layers provide highly confident bit input information that helps reduce the number of sensing levels on cell at error-prone layers. Our experimental results showed that the proposed approach improved the read throughput by 29% and reduced the read latency by 43% compared with a conventional multichip SSD design.

## Disjoint-Set Data Structure-Aided Structured Gaussian Elimination for Solving Sparse Linear Systems

- **Status**: ✅
- **Reason**: 희소선형계 SGE 삼각화를 disjoint-set으로 가속, LDPC 인코딩(패리티검사행렬 가우스소거)에 이식 가능한 효율화 기법으로 애매하여 살림
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:9151227
- **Type**: journal
- **Published**: Nov. 2020
- **Authors**: Xuan He, Kui Cai
- **PDF**: https://ieeexplore.ieee.org/document/9151227
- **Abstract**: Structured Gaussian elimination (SGE) is a class of methods for efficiently solving sparse linear systems. The key idea is to first triangulate the original linear systems. The maximum component (MC)-based strategies are widely used to implement the triangulation process. The most straightforward way to find the MC is through exhaustive search. Instead, in this letter, we propose to use a disjoint-set data structure (DSDS) to efficiently maintain the components. The extra storage and time complexity introduced by the DSDS are respectively linear to the number of unknowns and constraints involved in a linear system. Simulation results show that using the DSDS can be several times faster than doing the exhaustive search to find the components.

## Design of Rate-Compatible Low-Density Parity-Check Codes with Constant Check Matrix

- **Status**: ✅
- **Reason**: rate-compatible LDPC bit duplication 신규 설계법(puncturing 대비 개선), E 코드설계 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9431243
- **Type**: conference
- **Published**: 25-26 Nov.
- **Authors**: Son Le, Evgeny Likhobabin
- **PDF**: https://ieeexplore.ieee.org/document/9431243
- **Abstract**: In this paper, we propose a “bit duplication” design method for rate-compatible low-density parity-check codes (LDPC). The main idea of the method is to change the structure of codewords during its transmission over the communication system. This method can be effectively applied to create a set of codes, allowing to obtain lower-rate codes from the mother codes. To evaluate the proposed method, the dependence of the bit error probability on the signal-to-noise ratio (SNR) was simulated in Matlab. The result shows that the proposed method is superior to the conventional method of puncturing information bits.

## Generalized Very High Throughput Unrolled LDPC Layered Decoder

- **Status**: ✅
- **Reason**: D/C: unrolled layered QC-LDPC 디코더 일반화(residue 기반 layered 스케줄링) 신규 HW 기법 — 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9306537
- **Type**: conference
- **Published**: 24-25 Nov.
- **Authors**: Alexandru Amaricai, Daian Stein, Oana Boncalo
- **PDF**: https://ieeexplore.ieee.org/document/9306537
- **Abstract**: Unrolled layered LDPC architectures have been shown to obtain tens of Gbps throughputs. These types of decoders are well suited to array LDPC codes, for which they present improved throughput. In this paper, we propose a generalization for unrolled layered LDPC decoding architectures, by employing the residue-based layered scheduling when merging multiple layers. This way, we can efficiently implement unrolled decoding architecture for any QC-LDPC (Quasi-Cyclic LDPC) codes. FPGA implementation results for WiMAX Rate 5/6 show that 35-41 Gbps throughputs are achievable using this architecture.

## Reduced-Complexity Offset Min-Sum Based Layered Decoding for 5G LDPC Codes

- **Status**: ✅
- **Reason**: C: 단일최소 offset min-sum 변형·차수별 서브최소 추정 신규 min-sum 기법 — NAND LDPC 디코더로 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9306590
- **Type**: conference
- **Published**: 24-25 Nov.
- **Authors**: Vladimir L. Petrović, Dragomir M. El Mezeni
- **PDF**: https://ieeexplore.ieee.org/document/9306590
- **Abstract**: This paper presents a novel approach for the reduced-complexity Min-Sum (MS) decoding of low density parity check (LDPC) codes in the partially parallel layered decoder architecture, which contains large number of serial check node processors. Reduced complexity is obtained by using the variant of the single-minimum Offset Min-Sum (smOMS) algorithm that approximates a second minimum with the addition of the variable weight parameter to the minimum value. Although the reduced-complexity MS algorithms primarily reduce hardware resources in fully parallel implementations, the results showed that a considerable reduction can be obtained if serial check node processors are used. Additionally, the paper proposes a better subminimum estimation for irregular codes from 5G new radio (5G NR). The method uses smaller subminimum estimation weights in check nodes with higher degree and higher weights in check nodes with smaller degree, which lead to the significant improvement in the SNR performance.

## High speed LDPC decoding for optical space link

- **Status**: ✅
- **Reason**: QC-LDPC용 horizontal layered Gallager E 디코더 FPGA 아키텍처(D), 하드입력 고속 디코딩 기법 이식 가능
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:9294911
- **Type**: conference
- **Published**: 23-25 Nov.
- **Authors**: Vincent Pignoly, Bertr Le Gal, Christophe Jego +2
- **PDF**: https://ieeexplore.ieee.org/document/9294911
- **Abstract**: In this paper, an architecture to implement horizontal layered Gallager E is proposed to decode QC-LDPC codes onto Field-Programmable Gate Array (FPGA). It arises as an attractive solution for wireless optical up-link space communication because of its low hardware complexity considering constraints in space. Very high throughput of several Gpbs is aimed. Moreover, at this bit rate, space systems imply hard inputs for the decoding process. Gallager E implementation represents an efficient trade-off between throughput, error correction capability and computational complexity. More than 1.5 Gbps are reached by the proposed decoders onto a Xilinx space-grade FPGA. One can note that higher throughput (3 Gbps) can be achieved on other recent FPGAs with increased working frequency.

## Fair comparison of hardware and software LDPC decoder implementations for SDR space links

- **Status**: ✅
- **Reason**: HW/SW LDPC 디코더 구현 비교(FPGA vs multi-core), 바이너리 QC-LDPC 디코더 HW 아키텍처(D)로 이식 가능
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:9294906
- **Type**: conference
- **Published**: 23-25 Nov.
- **Authors**: Vincent Pignoly, Bertr Le Gal, Christophe Jego +2
- **PDF**: https://ieeexplore.ieee.org/document/9294906
- **Abstract**: LDPC codes are a family of error correcting codes used in most wireless and space communication standards such as CCSDS [1] and DVB [2] ones. Thanks to their high error correction features and their parallelism capabilities, different technical solutions nowadays enable their real-time implementations in Software Defined Radio (SDR) contexts. Indeed, even if Error Correction Code (ECC) decoders were previously implemented on dedicated hardware targets (ASIC/FPGA), their real-time implementations on multi-core devices [3]-[5], is now possible. Software implementations currently provide high-throughput and low-latency features, scalability and also flexibility that makes them attractive for SDR systems. However, multi-core power consumption, throughput performance level and prices could be worse compared to ASIC/FPGA solutions for very high-throughput SDR systems. In this paper, a fair comparison of multi-core and FPGA solutions for the development of a 10 Gbps communication system for space communications is detailed.

## A new LDPC decoding scheme based on BP and Gated Neural Network

- **Status**: ✅
- **Reason**: BP-게이트신경망-BP 새 LDPC 디코더, 상관잡음 대응 신경망 디코더; 이식 가능 디코더(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9363835
- **Type**: conference
- **Published**: 13-15 Nov.
- **Authors**: Yong Liu, Xiaolin Liu, Zhongyi Ding +2
- **PDF**: https://ieeexplore.ieee.org/document/9363835
- **Abstract**: In long wave communication scenarios, channel interferences lead to noise correlation. Since traditional belief propagation (BP) decoding algorithm is designed based on additive white Gaussian noise (AWGN), a performance cost will appear when it comes to correlated noise. In this paper, a new LDPC decoding scheme that applies to correlated Gaussian noise is proposed. We design a BP-gated neural network-BP structure to carry on two rounds of BP decoding with the second round based on optimized noise. By adopting gated neurons in typical NN, CNN, training performance is improved. Simulation shows that compared with BP decoding algorithm, the new decoding scheme outperforms traditional method by 0.5~0.61 dB when bit error rate is 10-6. This decoding scheme also works on pectinate noise with performance gain of 1.5 dB.

## Design of Parallelly Concatenated Spatially Coupled RA Codes

- **Status**: ✅
- **Reason**: PC-SCRA(병렬연접 공간결합 RA) 새 코드구성+밀도진화 임계, SC-LDPC 능가 주장; 바이너리 코드설계 이식 가능(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9334198
- **Type**: conference
- **Published**: 13-15 Nov.
- **Authors**: Yang Liu, Xin Liu, Shuangyi Cheng +1
- **PDF**: https://ieeexplore.ieee.org/document/9334198
- **Abstract**: In this paper, parallelly concatenated spatially coupled RA (PC-SCRA) codes was presented based on spatially coupled RA (SCRA) codes with the advantages of simple coding structure, threshold saturation and low decoding complexity. When encoding, the same message bits are respectively encoded by two same SCRA codes to obtain respective check bits. During transmission, the message bits and the obtained parity bits are merged into one codeword for transmission. Besides, density evolution algorithm was proposed to compute the iterative decoding threshold of PC-SCRA code ensemble over the binary erasure channel. Simulation results show that the proposed PC-SCRA code ensemble has excellent BP threshold performance close to Shannon limit and is superior to the spatially coupled LDPC (SC-LDPC) code with same coderate, which provides a new way for construrting capacity-approaching SC-LDPC codes.
