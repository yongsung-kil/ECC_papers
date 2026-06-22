# IEEE Xplore — 2022-08 (1차선별 통과)


## Design of LUT-Based LDPC Decoders for Spin-Transfer Torque Magnetic Random Access Memory

- **Status**: ✅
- **Reason**: STT-MRAM용 LUT 기반 LDPC 디코더 + 채널양자화/DE 공동설계 — C/D(디코더/HW) 메모리 ECC 이식 가능, 바이너리
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9658546
- **Type**: journal
- **Published**: Aug. 2022
- **Authors**: Chatuporn Duangthong, Watid Phakphisut, Pornchai Supnithi
- **PDF**: https://ieeexplore.ieee.org/document/9658546
- **Abstract**: Recently, low-density parity-check (LDPC) codes have been proposed to improve the reliability of spin-transfer torque magnetic random access memory (STT-MRAM). While several research works focus on the design of LDPC codes to combat the process variation and thermal fluctuation of the STT-MRAM, we aim to tackle the high decoding latency issues by the novel design of a lookup table (LUT)-based LDPC decoder for the forward and backward (FB) processes. In this work, the channel quantizer and LUT operations of the LDPC decoder are jointly designed by minimizing the error probability estimated from the density evolution (DE) algorithm. The simulation results show that the proposed design method for a code rate of 0.9 outperforms the previous methods in terms of bit error rate (BER) performance. Furthermore, the proposed design can support the channel model of the STT-MRAM without an independent and identically distributed (i.i.d.) channel adapter.

## Construction of QC-LDPC Codes from Sidon Sequence Using Permutation and Segmentation

- **Status**: ✅
- **Reason**: Sidon 시퀀스 기반 4-cycle/6-cycle 제거 QC-LDPC 새 구성법. 바이너리 코드설계 기법으로 NAND LDPC에 이식 가능(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9780420
- **Type**: journal
- **Published**: Aug. 2022
- **Authors**: Lintao Zhang, Juhua Wang
- **PDF**: https://ieeexplore.ieee.org/document/9780420
- **Abstract**: By utilizing a Sidon sequence, two new methods are proposed to construct quasi-cyclic (QC) low-density parity-check (LDPC) codes. The first method yields a QC-LDPC code without 4-cycles and the second method gives a QC-LDPC code without 4-cycles and 6-cycles. In the literature there are two methods which employ mathematical objects somewhat resembling a Sidon sequence to remove 4-cycles, and there are two explicit constructions which guarantee the absence of 4-cycles and 6-cycles. Compared with the former, our first method is much more flexible in selecting parameters while providing identical or better performance. Compared with the latter, our second method provides much better performance.

## Adaptive Belief Propagation Decoding of CRC Concatenated NR LDPC and Polar Codes

- **Status**: ✅
- **Reason**: CRC 연접 LDPC/polar 대상 적응형 BP(R-ABP) 새 디코더 알고리즘. 바이너리 LDPC BP 개선으로 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9800962
- **Type**: journal
- **Published**: Aug. 2022
- **Authors**: Mingyang Zhu, Ming Jiang, Chunming Zhao
- **PDF**: https://ieeexplore.ieee.org/document/9800962
- **Abstract**: In this paper, we propose a modified adaptive belief propagation (ABP) algorithm, which is referred to as the random ABP (R-ABP) algorithm, for decoding short channel codes adopted in the fifth generation (5G) New Radio (NR) wireless systems. Based on the cyclic redundancy check (CRC) concatenation structure of 5G channel codes, we can take partial or even all CRC bits into iterative R-ABP decoding to improve the error correction performance, while the error detection capability can still be guaranteed by the remaining CRC bits and a proposed threshold-based acceptance criterion. We call this improved R-ABP decoding the threshold-and-CRC-aided R-ABP (TCA-R-ABP) decoding. The simulation results show that our proposed TCA-R-ABP algorithm outperforms the state-of-the-art decoding algorithms for many 5G low-density parity-check (LDPC) and polar codes. Moreover, the proposed TCA-R-ABP algorithm leads to a unified decoder for LDPC and polar codes, which has the potential to be a lower-complexity decoder over the combination of the belief propagation (BP) and CRC-aided successive cancellation list (CA-SCL) decoders.

## Automorphism Ensemble Decoding of Quasi-Cyclic LDPC Codes by Breaking Graph Symmetries

- **Status**: ✅
- **Reason**: QC-LDPC의 automorphism 앙상블 디코딩(AED): 패리티행렬 수정으로 대칭 깨고 BP 앙상블 이득 확보하는 새 디코더 기법으로 NAND 바이너리 QC-LDPC에 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9772648
- **Type**: journal
- **Published**: Aug. 2022
- **Authors**: Marvin Geiselhart, Moustafa Ebada, Ahmed Elkelesh +2
- **PDF**: https://ieeexplore.ieee.org/document/9772648
- **Abstract**: We consider automorphism ensemble decoding (AED) of quasi-cyclic (QC) low-density parity-check (LDPC) codes. Belief propagation (BP) decoding on the conventional factor graph is equivariant to the quasi-cyclic automorphisms and therefore prevents gains by AED. However, by applying small modifications to the parity-check matrix at the receiver side, we can break the symmetry without changing the code at the transmitter. This way, we can leverage a gain in error-correcting performance using an ensemble of identical BP decoders, without increasing the worst-case decoding latency. The proposed method is demonstrated using LDPC codes from the CCSDS, 802.11n and 5G standards and produces gains of 0.2 to 0.3 dB over conventional BP decoding. Compared to the similarly performing saturated BP (SBP), the proposed algorithm reduces the average decoding latency by more than eight times.

## Simplified Ordered Statistic Decoding for Short-Length Linear Block Codes

- **Status**: ✅
- **Reason**: 단축 선형블록부호 OSD 복잡도 저감 기법(segment size/stopping bound 근사). 이식 가능한 OSD 디코더 개선으로 포함(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9779155
- **Type**: journal
- **Published**: Aug. 2022
- **Authors**: Changhyeon Kim, Dongyun Kam, Seokki Kim +2
- **PDF**: https://ieeexplore.ieee.org/document/9779155
- **Abstract**: The ordered statistic decoding (OSD) algorithm for short-length linear block codes provides an attractive ML-approaching performance, expected to be used for the ultra-reliable low latency communication (URLLC) at the next-generation wireless solutions. To find the corrected codeword among numerous candidates, however, the decoding process requires a considerable amount of computational costs, which need to be simplified to achieve low-latency processing. In this letter, we present several schemes that relax the overall complexity of the state-of-the-art segmentation discarding algorithm. Without degrading the error-correcting power, our method approximate the internal steps for computing the segment sizes and the stopping bounds at the run time, reducing the average processing costs by  $1.6\times 10 ^{4}$  times for achieving the low-BLER performance.

## A LDPC Decoding Algorithm based on Convolutional Neural Network

- **Status**: ✅
- **Reason**: C: DenseNet 기반 신경망 LDPC 디코더 - 이식 가능 디코더 알고리즘
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9914424
- **Type**: conference
- **Published**: 4-5 Aug. 2
- **Authors**: Jiamei Gao, Bo Zhang, Bin Wang +1
- **PDF**: https://ieeexplore.ieee.org/document/9914424
- **Abstract**: At present, low density parity check code (LDPC) has been widely used in channel coding and decoding because of its excellent performance, but with the increase of code length, the complexity of decoding algorithm has became higher and higher. In view of the limitations of decoding algorithm and the rapid development of artificial intelligence technology, it has great research prospects to solve the above problems through deep neural network. Therefore, this paper mainly focuses on the design and improvement of LDPC decoding process, and proposes an LDPC decoding model based on DenseNet neural network structure, which improves the LPDC decoding performance by optimizing DenseNet neural network structure. This method can recover information at the decoding end, avoiding the limitations of traditional short decoding loop and high complexity of decoding algorithm. The simulation results show that the LDPC decoding algorithm based on DenseNet neural network structure improves the decoding performance.

## Performance Evaluation of Burst Error Correction by LDPC Coding and Iterative Decoding System in Magnetic Tape Drive Using a BaFe Magnetic Tape

- **Status**: ✅
- **Reason**: 인터리브드 LDPC + 버스트 에러 검출기(LDPC-BD) 반복디코딩이 스토리지(테이프) ECC — 버스트 대응 디코딩 기법이 NAND 결함/버스트에 이식 가능(B/C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9918619
- **Type**: conference
- **Published**: 29-31 Aug.
- **Authors**: Yasuaki Nakamura, Taisei Akamatsu, Madoka Nishikawa +1
- **PDF**: https://ieeexplore.ieee.org/document/9918619
- **Abstract**: The tolerance for burst error of the interleaved low-density parity-check (LDPC) code is evaluated with the cross-interleaved Reed-Solomon code (CIRC) in the magnetic tape drive using a BaFe magnetic tape. We evaluate the interleaved LDPC coding and iterative decoding system with burst error detector (LDPC-BD) system by required signal-to-noise ratio (SNR) to achieve “No errors” for the burst-like deterioration such as media defects to the CIRC with erasure error correction (CIRC-EC) system by computer simulation. The results clarify that the LDPC-BD system tolerates the longer burst error than the CIRC-EC system. In addition, they also clarified that the LDPC-BD system achieves “No errors” with the 3.0-4.5 dB lower SNR than the CIRC-EC system.

## Reliable Transceiver Design of LEO Satellite Communication Systems with Doppler Effect and Multipath and Amplification Nonlinear Distortions

- **Status**: ✅
- **Reason**: 제안한 hybrid LDPC soft decoding 기법이 min-sum 단독보다 우수하다고 주장 — 새 디코더 변형(C) 이식 가능성, 애매하나 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9906513
- **Type**: conference
- **Published**: 24-26 Aug.
- **Authors**: Sheng-Hsuan Hsu, Juinn-Horng Deng
- **PDF**: https://ieeexplore.ieee.org/document/9906513
- **Abstract**: With the advancement of wireless communication technology, satellite communications have the advantages of wide coverage and low latency. Low-earth-orbit (LEO) satellite communication systems have an important role in 6G technology development in the future. However, high-frequency and high-relative speed lead to Doppler effect, which will seriously affect the performance of the demodulator at the receiver. Meanwhile, for the high transmission power of the antenna, signal distortion caused by the non-linear effect of power amplifier (PA) needs to be considered. In this paper, we use Gaussian Minimum Shift Keying (GMSK) modulation technique as the main transceiver. It is found that under the non-ideal transmission, e.g., Doppler frequency offset and multipath channels effects, the continuous phase modulation (CPM) characteristics can effectively reduce multipath channel interference and nonlinear distortion. Also, the demodulation scheme using cross-coupled detector method can reduce the frequency offset effect. Moreover, the proposed modem scheme combined with the Quasi Cyclic LDPC (QC-LDPC) channel coding and the hybrid LDPC soft decoding method proposed herein, the error rate performance has better than using the min-sum algorithm decoding method alone.

## Exploiting Binary Equilibrium for Efficient LDPC Decoding in 3D NAND Flash

- **Status**: ✅
- **Reason**: 3D NAND flash LDPC read latency 저감 위한 reference voltage 고속 조정 기법 — A 직접 해당
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9904783
- **Type**: conference
- **Published**: 23-25 Aug.
- **Authors**: Hsiang-Sen Hsu, Li-Pin Chang
- **PDF**: https://ieeexplore.ieee.org/document/9904783
- **Abstract**: 3D NAND flash is prone to bit errors due to severe charge leakage. Modern SSDs adopt LDPC for bit error management, but LDPC can incur a high read latency through iterative adjustment to the reference voltage. Bit scrambling helps reduce inter-cell interference, and with it, ones and zeros equally contribute to raw data. We observed that as bit errors develop, the 0-bit ratio in raw data deviates from 50%. Inspired by this property, we propose a method for fast adjustment to the reference voltage, involving a placement step and a fine-tuning step. Our method uses only a few hundreds of bytes of RAM but improves the average read latency upon existing methods by up to 24%.

## Intelligent and Reliable Coded Bit Stream Recovery over Correlated Fast Fading Channels

- **Status**: ✅
- **Reason**: ResCNN로 soft LLR 추정해 디코더 입력 제공 — 신경망 기반 LLR 생성, C 이식 가능성, 애매하나 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10006524
- **Type**: conference
- **Published**: 23-24 Aug.
- **Authors**: Xiaoling Yang, Lin Zhang, Yuan Jiang
- **PDF**: https://ieeexplore.ieee.org/document/10006524
- **Abstract**: In this paper, we propose an intelligent coded-bits stream recovery scheme for improving reliability performance. In this design, a residual learning aided convolutional neural network (ResCNN) architecture with BCEwithLogits loss function is proposed to achieve the intelligent distortion compensation for the received data. In addition, at the online deployment stage, the ResCNN will calculate and output the float estimates of coded-bit streams, which act as the soft information to be regarded as the initial log likelihood ratio (LLR) for the subsequent decoding algorithm. Thus no channel state information (CSI) is required, then pilots used for the channel condition estimation can be removed to improve both the efficiency and the practicality. Subsequently, we analyze the computational complex and provide simulation results, which demonstrate that the proposed system can effectively improve the reliability performance of the receivers with no need of the CSI estimates to achieve higher practicality.

## Configurable Universal QC-LDPC Encoder Architecture Design

- **Status**: ✅
- **Reason**: Configurable QC-LDPC 인코더 FPGA 아키텍처(병렬/핫스위칭) — 이식 가능 HW/코드설계(D/E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9909148
- **Type**: conference
- **Published**: 21-23 Aug.
- **Authors**: Mingbo Hao, Guangzu Liu, Jun Zou +1
- **PDF**: https://ieeexplore.ieee.org/document/9909148
- **Abstract**: Quasi-cyclic low-density parity-check (QC-LDPC) codes are widely used owning to its good performance and easy hardware implementation. However, most classical LDPC encoder designs do not support changing the LDPC code types or parameters according to different communication services and channel conditions. In this paper, we propose an encoder architecture with configurable code types, input information block lengths, coding rates and degrees of parallelism, which can realize “hot-switching” of configuration parameters. A new scheme that makes full use of the characteristics of the generation matrix is used in the core of parallel coding. The implementation on field programmable gate array (FPGA) shows that the throughput of the encoder can reach 1.6 Gbps under the condition of 7/8 coding rate (8176, 7154) and the degree of parallelism set to 8.

## Optimized LDPC Code Concatenated with Trellis Shaping for PAPR Reduction in SISO-OFDM Systems

- **Status**: ✅
- **Reason**: LDPC variable node degree distribution 최적화(bit error prob 기반)는 이식 가능한 코드 설계 기법(E)이라 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9990252
- **Type**: conference
- **Published**: 16-20 Aug.
- **Authors**: Amna Arif, Abdul Wakeel, Alina Mirza +1
- **PDF**: https://ieeexplore.ieee.org/document/9990252
- **Abstract**: Different techniques have been used for the peak-to-average power ratio (PAPR) reduction of orthogonal frequency division multiplexing (OFDM) systems. Among these, trellis shaping provides state of the art performance in terms of PAPR reduction as well as mean power reduction with moderate computational complexity. Therefore, this manuscript addresses the effect of using shaping codes with higher trellis depths for PAPR reduction of the OFDM systems. Using shaping codes of higher depths improve the PAPR reduction as well as bit error rate (BER) of the system. Moreover, we concatenate an optimized low-density parity-check (LDPC) code with Trellis shaping to further improve the performance of the OFDM system in terms of BER. For the LDPC code, the variable node degree distribution is optimized based on the error probabilities of the individual bits inside a quadrature amplitude modulation (QAM) constellation taking into consideration the error probabilities of the shaping codes used. Simulation results show that the proposed technique has better PAPR reduction as well as better BER as compared to the already existing systems using Trellis shaping with a shaping code of 4 states concatenated with an optimized LDPC code.

## Partial Product-LDPC Codes Without Rate Loss

- **Status**: ✅
- **Reason**: Partial Product-LDPC 무손실 새 코드구성 + free-ride 반복디코딩, error-floor/waterfall 트레이드오프 — 새 코드설계·디코더(E/C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9880620
- **Type**: conference
- **Published**: 11-13 Aug.
- **Authors**: Qianfan Wang, Suihua Cai, Fanhui Meng +2
- **PDF**: https://ieeexplore.ieee.org/document/9880620
- **Abstract**: In this paper, we present a new construction of product codes, where all rows of the information array are encoded using the low-density parity-check (LDPC) codes while only partial columns of the information array are encoded using the algebraic codes. Also distinguished from the conventional product codes, the actual code rates of the presented partial product codes are the same as those of the row component LDPC codes, without any rate loss. This is achieved by using the free-ride coding to transmit the additional column checks along with the LDPC codewords. For decoding, an iterative decoding algorithm, which is scheduled as free-ride decoding, row decoding and column decoding, is proposed. At the column decoding stage, the messages associated with those successfully decoded columns are hardened and exploited to improve the free-ride decoding and the row decoding. By assuming a binary symmetric channel model after row decoding, we present an approximated bound on the word error rate (WER) of the doubly-protected (by both the row code and the column code) information bits. To predict the performance of the proposed codes, a genie aided (GA) lower bound derived from the original LDPC coded system with partial known bits is presented. These bounds and the simulation results reveal that the presented product-LDPC codes can have a significant performance improvement over the row component LDPC codes (about one dB at the WER of 10–5). They also reveal that the presented product-LDPC codes can have a flexible trade off between the error-floor and the waterfall performances, by using different row codes and column codes.

## Design of 4-cycles Free Short-length LDPC Codes Based on the Kirkman Triple Systems

- **Status**: ✅
- **Reason**: E: Kirkman triple system 기반 4-cycle-free 단길이 바이너리 LDPC 부호 설계, NAND용 girth/유한길이 구성에 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9896662
- **Type**: conference
- **Published**: 11-13 Aug.
- **Authors**: Dongliang Guo, Yuejiao Feng, Congduan Li
- **PDF**: https://ieeexplore.ieee.org/document/9896662
- **Abstract**: Short-length codes may play a crucial role in delay-sensitive scenarios. Low-density parity-check (LDPC) codes, as a class of Shannon limit approaching codes, perform well with long code length. However, the design of short-length LDPC codes with good performance is still challenging. This paper investigates the construction of short-length LDPC codes based on the combinatorial design theory. Specifically, Kirkman triple systems (KTS), as a type of balanced incomplete block design (BIBD) techniques, are used to construct the parity-check matrices of LDPC codes, which are guaranteed to be 4-cycles free. Some other properties of such designed LDPC codes are also investigated. For instance, a lower bound on the girth, the code rate and minimum code distance. The simulation results show that the designed short-length LDPC codes based on KTS outperform that of randomly constructed ones.

## Parallel Decoding of PIC-LDPC Codes Aided by Free-Ride Coding

- **Status**: ✅
- **Reason**: PIC-LDPC 병렬 디코딩 free-ride 결합으로 고속 디코더 구현 가능 — 이식 가능 디코더 병렬화 기법(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9880658
- **Type**: conference
- **Published**: 11-13 Aug.
- **Authors**: Fanhui Meng, Qianfan Wang, Suihua Cai +1
- **PDF**: https://ieeexplore.ieee.org/document/9880658
- **Abstract**: In this paper, we apply free-ride coding, a recently proposed technique, to the partial information coupling (PIC) low-density parity-check (LDPC) codes. Such an integration admits parallel decoding of PIC-LDPC codes, suggesting that high-speed decoders can be implemented. At the transmitter, the coupled information bits are periodically sampled and transmitted by the free-ride coding. At the receiver, these free-ride coded bits are first decoded and then used to decouple the whole PICLDPC coded chain into multiple shorter chains, each of which can be decoded separately and in parallel. This benefits from the fact that free-ride coded bits typically have higher reliability than others, as confirmed by the numerical results. Numerical results also show that the word error rate (WER) performance of the proposed codes is close to the genie-aided (GA) lower bound in the high SNR region.

## An Improved 5G NR LDPC Decoding Algorithm Based On Box-Plus Operation

- **Status**: ✅
- **Reason**: 5G NR LDPC box-plus(BP) 근사 함수 제안, NMS/OMS 대비 개선 — 이식 가능 BP 디코더 근사 알고리즘(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9880684
- **Type**: conference
- **Published**: 11-13 Aug.
- **Authors**: Liming Lu, Yi Li, Li Fang
- **PDF**: https://ieeexplore.ieee.org/document/9880684
- **Abstract**: Iterative box-plus operation is an equivalent function of BP algorithm used in fifth generation(5G) new radio Low-Density Parity-Check (LDPC) decoders, which has gathered significant interest in the past few years. However, it is very challenging to approximate iterative Box-Plus operation effectively since it contains continuous logarithmic and exponential operation. In this paper, the problem is solved gracefully by proposing a simple yet efficient approximate function. The corresponding optimal parameters are given by density evolution and Monte Carlo simulation, which could greatly reduce the unreliability of check-to-variable messages. The extensive experiments in error-correction performance have show the feasibility of the proposed method, compared to existing NMS and OMS algorithms, which makes it more attractive in practical 5G LDPC decoding applications.

## A Transmission Scheme based on QC-LDPC Codes with Matrix Q over AWGN Channel

- **Status**: ✅
- **Reason**: QC-LDPC + invertible Matrix Q + 신뢰도 기반 RQ 디코딩 알고리즘, BF/WBF 대비 개선 — 새 디코더 기법(C), 애매하나 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9880641
- **Type**: conference
- **Published**: 11-13 Aug.
- **Authors**: Jiayun Bao, Cuican Shen, Zhiping Shi +1
- **PDF**: https://ieeexplore.ieee.org/document/9880641
- **Abstract**: In this paper, a transmission scheme based on Quasi-Cyclic Low-Density Parity-Check (QC-LDPC) codes with an invertible quasi-cyclic Matrix Q is proposed over Additive White Gaussian Noise (AWGN) channel in order to obtain faster convergence of hard-decision decoding. Combined with the soft information from channel, another improved Reliability-based Q (RQ) decoding algorithm is proposed. The new design can also be applied to QC-LDPC codes in IEEE 802.16e Standards. The simulation results show that the proposed scheme with Q or RQ decoding algorithm has better error correction performance and lower average number of iterations than Bit-Flipping (BF) or weighted Bit-Flipping (WBF) decoding algorith

## BCH-SPC based Cubic Turbo Product Coding

- **Status**: ✅
- **Reason**: Turbo Product code의 개선 adaptive BP 디코딩(PL-RC-TAB 스케줄링), 이식 가능 BP 스케줄링 기법(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9870585
- **Type**: conference
- **Published**: 1-5 Aug. 2
- **Authors**: Li Deng, Yong Liang Guan, Zilong Liu +2
- **PDF**: https://ieeexplore.ieee.org/document/9870585
- **Abstract**: In this paper, we propose a cubic Turbo Product code (TPC) with the Bose-Chaudhuri-Hocquenghem (BCH) code and the single parity-check (SPC) code as components, as well as an improved turbo-oriented adaptive belief propagation decoding based on the partial layered and row-column weight scheduling (PL-RC-TAB). The proposed coding scheme has comparable encoding and decoding complexities with the two dimensional (2D) TPC based on the classical turbo-oriented adaptive belief propagation (TAB) decoding, but can achieve faster decoding convergence rate and improved error correction performance.
