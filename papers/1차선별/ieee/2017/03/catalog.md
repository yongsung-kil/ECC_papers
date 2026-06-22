# IEEE Xplore — 2017-03 (1차선별 통과)


## Iterative LDPC–LDPC Product Code for Bit Patterned Media

- **Status**: ✅
- **Reason**: iterative LDPC-LDPC product code + erasure 디코딩으로 burst/random 에러 보정, 스토리지 ECC용 바이너리 LDPC 부호 설계 기법(B/E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7592444
- **Type**: journal
- **Published**: March 2017
- **Authors**: Seongkwon Jeong, Jaejin Lee
- **PDF**: https://ieeexplore.ieee.org/document/7592444
- **Abstract**: Bit patterned media aims at high density recording of more than 10 Tb per square inch, but a burst error mostly occurred by media defects, and data write failure can be a serious problem. However, if the burst errors are compensated by erasure decoding, the performance of low-density parity check (LDPC) code, which is a strong candidate for the error correcting code for storage systems, can be improved. In this paper, we propose an iterative LDPC-LDPC product code and show that it performs better than a simple LDPC-LDPC product code when there are only random errors and both random and burst errors.

## EXIT Chart Aided LDPC Code Design for Symmetric Alpha-Stable Impulsive Noise

- **Status**: ✅
- **Reason**: 바이너리 LDPC 부호 설계 최적화(EXIT chart+quantized density evolution)로 이식 가능 E 기법; 충격성 잡음용 앙상블 설계지만 코드설계 기법 떼어낼 수 있음(애매시 in)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7775000
- **Type**: journal
- **Published**: March 2017
- **Authors**: Bin Dai, Rongke Liu, Yi Hou +2
- **PDF**: https://ieeexplore.ieee.org/document/7775000
- **Abstract**: In this letter, an iterative analysis method based on an extrinsic information transfer (EXIT) chart and quantized density evolution is developed for low-density parity-check (LDPC) codes over channels with symmetric alpha-stable ( $\text{S}\alpha \text{S}$ ) impulsive noise. Based on the proposed scheme, a method to optimize ensembles of LDPC codes under different levels of impulsiveness is presented and it is shown that the information rates of our optimized code ensembles can achieve 95.4% and 94.7% of the channel capacity for  $\alpha =1.8$  and  $\alpha =1$ , respectively. Furthermore, experimental results, including EXIT curves, thresholds, and bit-error rate performance of optimized code ensembles, are obtained to verify the effectiveness of our analysis.

## Reduced Complexity Node-Wise Scheduling of ADMM Decoding for LDPC Codes

- **Status**: ✅
- **Reason**: LDPC용 ADMM LP 디코더의 node-wise 스케줄링+복잡도 저감(유클리드 사영 회피); 이식 가능 디코더 알고리즘 C
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7795194
- **Type**: journal
- **Published**: March 2017
- **Authors**: Xiaopeng Jiao, Jianjun Mu, Haoyuan Wei
- **PDF**: https://ieeexplore.ieee.org/document/7795194
- **Abstract**: Similar to the belief propagation decoder, linear programming decoding based on the alternating direction method of multipliers (ADMM) can also be seen as an iterative message-passing decoding algorithm. How to schedule messages efficiently is an important aspect since it will influence the convergence rate of iterative decoders. In this letter, we investigate the node-wise scheduling for ADMM decoders, named NS-ADMM. In particular, we propose a reduced-complexity method for the NS-ADMM decoder by avoiding Euclidean projections involved in the calculation of message residuals. Simulation results show that the proposed method converges much faster than the flooding and layered scheduling while keeping a lower complexity when compared with the NS-ADMM decoder.

## Explicit Constructions for Type-1 QC-LDPC Codes With Girth 12

- **Status**: ✅
- **Reason**: Type-1 QC-LDPC girth-12 명시적 구성(바이너리), 사이클 제거 코드 설계 기법으로 이식 가능(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7762770
- **Type**: journal
- **Published**: March 2017
- **Authors**: Guohua Zhang, Rudolf Mathar
- **PDF**: https://ieeexplore.ieee.org/document/7762770
- **Abstract**: Given any J × J (J > 3) square matrix over ZP such that the differences of any two row vectors contain each element in ZP at most once, a class of (3, L)-regular quasicyclic low-density parity-check codes is explicitly constructed with lengths P J L2 and girth 12, where L is any integer satisfying 3 <; L ≤ J. Simulation results show that the new codes perform very well for moderate rates and lengt...

## Efficient Multi-Rate Encoder of QC-LDPC Codes Based on FPGA for WIMAX Standard

- **Status**: ✅
- **Reason**: QC-LDPC 멀티레이트 인코더 FPGA HW(MVM 병렬화·메모리압축), 바이너리 QC-LDPC HW→D
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:10855182
- **Type**: journal
- **Published**: March 2017
- **Authors**: Xiumin Wang, Tingting Ge, Jun Li +2
- **PDF**: https://ieeexplore.ieee.org/document/10855182
- **Abstract**: An efficient multi-rate encoder for IEEE 802.16e LDPC codes which outperforms current single rate encoders with acceptable hardware consumption and efficient memory consumption is proposed. This design utilizes the common dual-diagonal structure in parity matrices to avoid the inverse matrix operation which requires extensive computations. Parallel Matrix-vector multiplication (MVM) units, bidirectional operation and storage compression are applied to this multi-rate encoder to increase the encoding speed and significantly reduce the quantity of memory bits required. The proposed encoding architecture also contributes to the design of multi-rate encoders whose parity matrices are dual-diagonally structured and have an Approximately lower triangular (ALT) form, such as in IEEE 802.11n and IEEE 802.22. Simulation results verified that the proposed encoder can efficiently work for all code rates specified in WIMAX standard. With a maximum clock frequency of 117 MHz, the encoder achieves 3 to 10 times higher throughput than prior works. The proposed encoder is capable to switch among six rates by adjusting the input parameter and it achieves the throughput up to 1Gbps.

## Efficient Decoding Schemes of LDPC Codes for the Layered-Division Multiplexing Systems in ATSC 3.0

- **Status**: ✅
- **Reason**: PCM 일부에만 SPA 적용하는 partial SPA 및 hybrid 디코딩 스케줄링, 디코더 구조 비변경 스케줄 기법으로 바이너리 LDPC에 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7574332
- **Type**: journal
- **Published**: March 2017
- **Authors**: Youngjun Hwang, Sunghye Cho, Seho Myung +1
- **PDF**: https://ieeexplore.ieee.org/document/7574332
- **Abstract**: A low-complexity decoding scheme of low-density parity-check codes for the layered-division multiplexing (LDM) systems in ATSC 3.0 is proposed. Based on the unique characteristic of the LDM and the special structure of a parity-check matrix (PCM) for the core layer, the proposed scheme applies the sum-product algorithm (SPA) to only a part of the PCM. For this reason, it is referred to as “the partial SPA,” compared with the conventional scheme, denoted by “the full SPA.” Clearly, it has a significantly lower complexity than the full SPA. Furthermore, we propose hybrid decoders employing both the full SPA and the partial SPA to achieve a better performance, while maintaining their complexity low. Numerical results show that the proposed schemes have a good performance enough to perform successive interference cancellation for the enhanced layer of the LDM systems in ATSC 3.0 as well as they have a low-complexity merit depending on system parameters. Since they only schedule the decoding procedure without modifying the decoder structure, they also have a benefit in the implementation of decoders.

## Low-Complexity Decoding Algorithms for the LDM Core Layer at Fixed Receivers in ATSC 3.0

- **Status**: ✅
- **Reason**: Gallager B/E(이진/정수 연산) 디코더를 ATSC LDM에 성능손실 없이 적용하는 저복잡도 디코딩 스케줄링, 바이너리 LDPC 디코더 기법으로 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7571136
- **Type**: journal
- **Published**: March 2017
- **Authors**: Sunghye Cho, Youngjun Hwang, Seho Myung +1
- **PDF**: https://ieeexplore.ieee.org/document/7571136
- **Abstract**: Gallager’s decoding algorithms  ${B}$  (GDB) and  ${E}$  (GDE) for low-density parity-check codes have much lower computational complexity and much less required memory size than the sum-product algorithm (SPA). This is because GDB and GDE only use binary or integer operations, while the SPA requires real operations and a look-up table. However, they are hardly used in commercial communication systems since they have a worse performance than the SPA. Layered-division multiplexing (LDM) is considered in ATSC 3.0 in order to deliver multiple broadcasting streams with distinct robustness in a single radio frequency channel. Due to the unique characteristic of the LDM, we propose to use GDB or GDE rather than the SPA for decoding the core layer signal at fixed receivers. Numerical results show that the computational complexity and the required memory size can be reduced without any performance loss by about 50 percent and 80 percent, respectively, when GDB and GDE are employed.

## A Greedy Search Based Method with Optimized Lower Bound for QC-LDPC Codes

- **Status**: ✅
- **Reason**: QC-LDPC 지수행렬 girth 8/10/12 저복잡도 구성법(E), 바이너리 코드설계 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7940234
- **Type**: conference
- **Published**: 22-24 Marc
- **Authors**: Ambar Bajpai, Abhishek Kalsi, Suvit Nakpeerayuth +2
- **PDF**: https://ieeexplore.ieee.org/document/7940234
- **Abstract**: Autonomous decentralized system is need of the dynamically varying society. Various autonomous decentralized systems architecture proposed and deployed, use of IEEE 802.11n/ac (Wi-Fi) and IEEE 802.16e (Wi-max) standards for surveillance purposes in different geographical region. These standards use LDPC codes as a channel code having better error correcting performance. This article deals with a construction of less computational complexity method for constructing exponent matrix (3, K) having girth 8, 10, and 12 of quasi-cyclic low-density parity-check (QC-LDPC) codes. In this method, we first generate a base matrix and then the same matrix is further used for expanding till desired size of the exponent matrix. The construction of code deals with the generation of base matrix by a simple algorithm for girth 8, 10, and 12. Our method is flexible for any block-column length K. Finally, a new method is given with less computational complexity with optimized CPM size.

## High throughput structured LDPC layered decoder

- **Status**: ✅
- **Reason**: 구조적 LDPC 레이어드 디코더의 처리량 개선(재정렬+병렬 행처리)으로 D 이식 가능 HW 아키텍처에 해당
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:8300023
- **Type**: conference
- **Published**: 22-24 Marc
- **Authors**: Jayashree C. Nidagundi, Siddarama R. Patil
- **PDF**: https://ieeexplore.ieee.org/document/8300023
- **Abstract**: Advances in communication systems are drastically changing in day today's life. Due to this the reliability of information will be always matter of concern, so there is need for improving the error correction mechanisms. The proposed work deals with improving the throughput of structured LDPC decoding defined for IEEE WiMAX 802.16e standards. BER simulation results shows improvement of 10_e at 2.5 dB SNR, 0.1 dB early convergence compared to standard IEEE 802.16e WiMAX layered LDPC decoding, by employing the reordering and parallel row processing of the parity check matrix.

## A systematic approach for achieving low bit error rate of LDPC decoder using MWD algorithm

- **Status**: ✅
- **Reason**: MWD(Minimum Weight Decoding) 알고리즘으로 LDPC error floor 개선 시도(C), 애매하여 in
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8299713
- **Type**: conference
- **Published**: 22-24 Marc
- **Authors**: Shruti Wahane, Sandeep Kakde, Atish Khobragade +1
- **PDF**: https://ieeexplore.ieee.org/document/8299713
- **Abstract**: One of the most significant barriers for using Low Density Parity Check (LDPC) codes in many wireless communication system and magnetic storage devices is the bit error rate floor phenomena with their complex message passing iterative algorithm. LDPC codes are mostly used in communication system because of its outstanding performance achievement. There are various decoding algorithm for LDPC decoder. In this paper, we presented the mathematical analysis of Minimum Weight Decoding (MWD) algorithm and its error rate performance over Additive White Gaussian Noise (AWGN) channel. A comparison of bit error rate performance over signal to noise ratio (dB) is carried out for different codes such as hamming code, BCH code and LDPC code. This paper shows bit error performance of decoder using minimum weight decoding algorithm. The main significance of this paper is that it shows efficient performance of Minimum Weight Decoding (MWD) algorithm based LDPC Decoder. We presented three classes of codes (1) hamming code, (2) BCH code and (3) LDPC Codes. We demonstrate the effectiveness of LDPC decoder over other two code decoders for the code rate 1/2 and block length (16,8) which is tarnished for its error floors.

## Design and implementation of quasi cyclic low density parity check (QC-LDPC) code on FPGA

- **Status**: ✅
- **Reason**: QC-LDPC FPGA 완전병렬 디코더 HW 구현(D), 이식 가능
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:8299744
- **Type**: conference
- **Published**: 22-24 Marc
- **Authors**: Dharmesh J. Patel, Pinalkumar Engineer
- **PDF**: https://ieeexplore.ieee.org/document/8299744
- **Abstract**: Low density parity check (LDPC) code is a widely used error correcting code in various applications such as Wi-Fi, Wi-Max and Digital Video Broadcasting - Satellite - Second Generation (DVB-S2). Proposed work is focused on LDPC decoder design using soft decision iterative message passing for a code length 222 bits, 546 bits, 642 bits, 648 bits and 1152 bits that gives BER of 10-5 with coding gain of approximately 4 dB. Proposed work shows fully parallel design on isolated shifted identity matrices based on structured construction quasi cyclic low density parity check code (QC-LDPC) that give throughput of 2 Gbps.
