# IEEE Xplore — 2007-08 (1차선별 통과)


## Reliability-Based Iterative Decoding of LDPC Codes Using Likelihood Accumulation

- **Status**: ✅
- **Reason**: BP-OSD 디코더 개선(LLR 누적 기반 재정렬) - 이식 가능 디코더 알고리즘(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4290000
- **Type**: journal
- **Published**: August 200
- **Authors**: Ming Jiang, Chunming Zhao, Enyang Xu +1
- **PDF**: https://ieeexplore.ieee.org/document/4290000
- **Abstract**: In this work, we present an improvement on low complexity serial concatenation of belief propagation (BP) - order statistic decoding (OSD) algorithm for low-density parity-check (LDPC) codes. We introduce a more reliable method to reconstruct ordered information sequence in terms of the accumulated log-likelihood ratio (LLR) transitions of variable nodes. We give a general expression for both the existing BP-OSD algorithm and our proposed new method according to a structure similar to an infinite impulse response (IIR) filter. This improved algorithm achieves noticeable performance gains with only modest increase in computation complexity.

## Serially-Concatenated Low-Density Generator Matrix (SCLDGM) Codes for Transmission Over AWGN and Rayleigh Fading Channels

- **Status**: ✅
- **Reason**: 직렬연접 LDGM(SCLDGM) 코드 설계, EXIT 기반 최적화로 error floor 저감 - 바이너리 LDPC계 코드설계(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4290011
- **Type**: journal
- **Published**: August 200
- **Authors**: Miguel Gonzalez-Lopez, Francisco J. Vazquez-Araujo, Luis Castedo +1
- **PDF**: https://ieeexplore.ieee.org/document/4290011
- **Abstract**: Low density generator matrix (LDGM) codes are a particular class of low density parity check (LDPC) codes with very low encoding complexity. Single LDGM codes present high error-floors, which can be substantially reduced with the serial concatenation of two LDGM (SCLDGM) codes. We propose a technique to obtain good SCLDGM codes using extrinsic information transfer (EXIT) functions in a novel way. Although the optimization is performed for AWGN channels with binary signaling, the resulting codes are also optimal for AWGN and perfectly-interleaved Rayleigh fading channels with non-binary signaling and perfect CSI at reception, provided that Gray mapping is utilized. Optimized regular and irregular SCLDGM codes outperform heuristically-designed LDGM codes existing in the literature, and have a performance similar to or better than that of irregular repeat accumulate (IRA) codes.

## Relation Between Parity-Check Matrixes and Cycles of Associated Tanner Graphs

- **Status**: ✅
- **Reason**: Tanner 그래프 girth 판정/최단 사이클 카운팅 알고리즘 - 사이클 제거 코드설계 도구(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4289999
- **Type**: journal
- **Published**: August 200
- **Authors**: Ruwei Chen, Huawei Huang, Guozhen Xiao
- **PDF**: https://ieeexplore.ieee.org/document/4289999
- **Abstract**: This correspondence presents an approach to the representation of cycles of Tanner graphs on associated parity-check matrices. Several equivalent conditions for the girth of a Tanner graph to be 2k are proposed. An algorithm to determine girth of associated Tanner graphs of parity-check matrices is proposed, also with an algorithm to count shortest cycles.

## Parallel Weighted Bit-Flipping Decoding

- **Status**: ✅
- **Reason**: 병렬 weighted bit-flipping(PWBF) 신규 디코더, 빠른 수렴 - 이식 가능 디코더 알고리즘(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4289998
- **Type**: journal
- **Published**: August 200
- **Authors**: Xiaofu Wu, Chunming Zhao, Xiaohu You
- **PDF**: https://ieeexplore.ieee.org/document/4289998
- **Abstract**: A parallel weighted bit-flipping (PWBF) decoding algorithm for low-density parity-check (LDPC) codes is proposed. Compared to the best known serial weighted bit-flipping decoding, the PWBF decoding converges significantly faster but with little performance penalty. For decoding of finite-geometry LDPC codes, we demonstrate through examples that the proposed PWBF decoding converges in about 5 iterations with performance very close to that of the standard belief-propagation decoding.

## Quasi-Cyclic Low-Density Parity-Check Codes With Girth Larger Than  $12$

- **Status**: ✅
- **Reason**: QC-LDPC girth>12 신규 조합적 구성법+circulant shift 할당 규칙 제시 → E(코드설계) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4276926
- **Type**: journal
- **Published**: Aug. 2007
- **Authors**: Sunghwan Kim, Jong-Seon No, Habong Chung +1
- **PDF**: https://ieeexplore.ieee.org/document/4276926
- **Abstract**: A quasi-cyclic (QC) low-density parity-check (LDPC) code can be viewed as the protograph code with circulant permutation matrices (or circulants). In this correspondence, we find all the subgraph patterns of protographs of QC LDPC codes having inevitable cycles of length 2i, i = 6, 7, 8, 9,10, i.e., the cycles that always exist regardless of the shift values of circulants. It is also derived that if the girth of the protograph is 2g, g > 2, its protograph code cannot have the inevitable cycles of length smaller than 6g. Based on these subgraph patterns, we propose new combinatorial construction methods of the protographs, whose protograph codes can have girth larger than or equal to 14 or 18. We also propose a couple of shift value assigning rules for circulants of a QC LDPC code guaranteeing the girth 14.

## Construction of irregular LDPC codes based on Balanced Incomplete Block Designs

- **Status**: ✅
- **Reason**: BIBD 기반 비정규 구조화 LDPC 구성, girth≥6 저복잡도 — 바이너리 코드설계 기법(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4579179
- **Type**: conference
- **Published**: 9-11 Aug. 
- **Authors**: Siddarama R. Patil, Sant S. Pathak
- **PDF**: https://ieeexplore.ieee.org/document/4579179
- **Abstract**: In this paper, we present a method to design irregular structured low-density parity-check (LDPC) codes based on balanced incomplete block designs (BIBD). The problem of designing irregular structured LDPC codes that have good overall error performance for a wide range of code rates and block sizes with attractive storage requirements is attempted. The proposed codes are well structured and unlike random codes can lend themselves to a very low-complexity implementation. The codes constructed by this method have the girth at least 6 and they perform well with the sum-product iterative decoding algorithm. Furthermore, the codes are compared with known random LDPC codes, in order to assess their relative achievable performance. The proposed LDPC codes demonstrate performance that is better than an average random LDPC code of similar block length, code rate and parity check matrix sparsity.

## 3.2-Gb/s 1024-b rate-1/2 LDPC decoder chip using a flooding-type update-schedule algorithm

- **Status**: ✅
- **Reason**: C/D - flooding-type update-schedule 신규 디코딩 알고리즘+고속 칩, 부분 업데이트 메시지 기법 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4488574
- **Type**: conference
- **Published**: 5-8 Aug. 2
- **Authors**: Naoya Onizawa, Tomokazu Ikeda, Takahiro Hanyu +1
- **PDF**: https://ieeexplore.ieee.org/document/4488574
- **Abstract**: This paper presents a high-speed low-density parity-check (LDPC) decoder chip using a new decoding algorithm, called a flooding-type update-schedule algorithm. Since node computations are performed using partially updated messages in the proposed algorithm, because of the good similarity among time-consecutive messages, data-transmission bottleneck between nodes for node computation is greatly reduced. Moreover, longer wires between nodes are appropriately divided into several subwires by inserting flip-flops so that system clock frequency for the LDPC decoding scheme can be much increased while maintaining the same BER as a conventional algorithm using fully updated messages. In fact, a throughput of 3.2Gb/s in a 1024-b LDPC decoder chip under 90nm CMOS technology is attained with the sufficient BER.

## Partially-parallel irregular LDPC decoder based on improved message passing schedule

- **Status**: ✅
- **Reason**: C - irregular LDPC용 개선 message-passing schedule, 수렴속도 개선 디코더 기법 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4488821
- **Type**: conference
- **Published**: 5-8 Aug. 2
- **Authors**: Xing Li, Kazunori Shimizu, Zhen Qiu +2
- **PDF**: https://ieeexplore.ieee.org/document/4488821
- **Abstract**: In this paper, we propose a new efficient message-passing schedule for irregular LPDC code. Our approach is based on the schedule designed for regular LDPC code. We have modified the original schedule for regular LDPC code and improved it particularly for the irregular LDPC coder realization. The experimental results show that our method could achieve better performance than conventional one, and improve the converging rate as well.

## Powerful LDPC Codes for Broadband Wireless Networks: High-performance Code Construction and High-speed Encoder/Decoder Design

- **Status**: ✅
- **Reason**: shifted identity 코드 구성+error floor 10^-10 저감+joint row-column 디코딩+FPGA 고속 인코더/디코더 — 코드설계/디코더/HW(C/D/E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4294441
- **Type**: conference
- **Published**: 30 July-2 
- **Authors**: Zhiyong He, Sebastien Roy, Paul Fortier
- **PDF**: https://ieeexplore.ieee.org/document/4294441
- **Abstract**: This paper discusses high-performance code construction and high-speed encoder and decoder designs for low density parity check (LDPC) codes. Thanks to their nice structures, LDPC codes constructed from shifted identity matrices have been emphasized. Several techniques in code constructions have been proposed to lower the bit error floor down to 10-10. Characterized by a parity check matrix in a triangular plus dual-diagonal form, these structured LDPC codes can be encoded in linear time using a layered encoding algorithm. To increase the throughput of decoders, a joint row-column decoding algorithm has been proposed and parallel decoding architectures have been used. The implementation results into field programmable gate array (FPGA) devices indicate that the encoder for these high-performance LDPC codes attains a throughput of up to 115 Gbits/sec and the decoder attains a throughput of up to 1 Gbits/sec. The proposed codes are suitable for high-speed and high-performance applications which demand relatively low error floor, including application in broadband wireless networks.

## Low-Complexity Architectures of a Decoder for IEEE 802.16e LDPC Codes

- **Status**: ✅
- **Reason**: 802.16e 바이너리 LDPC 디코더 저복잡도 VLSI 아키텍처(레이어드 디코딩, 세미패럴렐 파이프라인) — 이식 가능 HW(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:4341494
- **Type**: conference
- **Published**: 29-31 Aug.
- **Authors**: Giuseppe Gentile, Massimo Rovini, Luca Fanucci
- **PDF**: https://ieeexplore.ieee.org/document/4341494
- **Abstract**: Low-density parity-check (LDPC) codes have recently been included as error-correcting codes in IEEE 802.16e, for wireless metropolitan area networks. This paper proposes a flexible, low-complexity LDPC decoder fully compliant with all 114 codes defined by the standard. The decoder runs the layered decoding algorithm to increase the convergence speed, and relies on a semi-parallel implementation with serial processing units working in pipeline to reduce the latency. Particularly, two different architectures are considered, and their RTL/memory complexity tradeoffs are analyzed. The resulting design yields a throughput ranging from 93 to 497 Mbps by means of 15 iterations at the clock frequency of 400 MHz. Synthesis on 65 nm CMOS technology, shows a chip area less than 0.59 mm2, despite the high flexibility, which compares favourably with similar implementations.

## Row-splitting design of Low-Density Parity-Check Codes for Gbps wireless transmission

- **Status**: ✅
- **Reason**: row-splitting QC-LDPC 코드 설계로 멀티레이트 지원, 바이너리 LDPC 구성 기법 (E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4299668
- **Type**: conference
- **Published**: 27-30 Aug.
- **Authors**: Jong-Ee Oh, Minho Cheong, Seokhyun Yoon +1
- **PDF**: https://ieeexplore.ieee.org/document/4299668
- **Abstract**: In this paper, we propose a design methodology of low-density parity check (LDPC) code for very high speed wireless transmission. To support various code rates with reasonable hardware a row-splitting/combining method is employed in conjunction with shortening. In row-splitting approach, a parity check matrix of a high rate mother LDPC code, saying rate 4/5, is designed first and then successively row-split the mother matrix to obtain lower rate codes. Shortening provides us another degree of freedom for rate and frame length flexibility for concatenation with MIMO system. The code performance is investigated in terms of frame error rate and compared with those of the LDPC code proposed in IEEE 802.16e standard.

## Efficient construction and implementation of short LDPC codes for wireless sensor networks

- **Status**: ✅
- **Reason**: 짧은 QC-LDPC 신규 구성 클래스 제안, 인코딩 용이·디코딩 성능 (E 코드설계)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4529693
- **Type**: conference
- **Published**: 27-30 Aug.
- **Authors**: James McDonagh, Massimiliano Sala, Antoin O'hAllmhurain +2
- **PDF**: https://ieeexplore.ieee.org/document/4529693
- **Abstract**: Wireless sensor networks gained a lot of attention in recent years due to their widespread applications. Reliability of data communication and power saving are paramount for applications which use wireless sensor network technology. We propose two classes of short quasi-cyclic LDPC codes suitable for implementation on a resource constrained system. The codes we propose are easy to encode and their decoding performance compares well with random LDPC codes with the same parameters. We implement our codes on a 25 mm mote platform provided by Tyndall and compare them with Viterbi coding schemes.

## Power-efficient LDPC code decoder architecture

- **Status**: ✅
- **Reason**: 전력효율 LDPC 디코더 HW 아키텍처(FIFO 버퍼링 빠른수렴 스케줄, 메시지 압축)로 NAND 디코더에 이식 가능(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:5514297
- **Type**: conference
- **Published**: 27-29 Aug.
- **Authors**: Kazunori Shimizu, Nozomu Togawa, Takeshi Ikenaga +1
- **PDF**: https://ieeexplore.ieee.org/document/5514297
- **Abstract**: This paper proposes the power-efficient LDPC decoder architecture which features (1) a FIFO buffering based rapid convergence schedule which enables the decoder to accelerate the decoding throughput without increasing the required number of memory bits, (2) an intermediate message compression technique based on a clock gated shift register which reduces the read and write power dissipation for the intermediate messages. Simulation results show that the proposed decoder achieves 1.66 times faster decoding throughput, and improves the power efficiency (which is defined by the power dissipation per Mbps) up to 52% compared to the decoder based on the conventional overlapped schedule.

## Performance of Optical CDMA Systems with Low Density Parity Check Codes

- **Status**: ✅
- **Reason**: OCDMA용으로 BP를 MAI 이항분포 반영해 재설계한 디코더 변형(C). BP 메시지 수정 기법은 이식 가능, 애매하나 in으로 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4300029
- **Type**: conference
- **Published**: 25-31 Aug.
- **Authors**: S. Sahuguede, A. Julien-Vergonjanne, J.P. Cances
- **PDF**: https://ieeexplore.ieee.org/document/4300029
- **Abstract**: Incoherent optical code division multiple access (OCDMA) is a potential issue for future high speed optical networks. To reduce the number of errors at the detection due in particular to Multiple Access Interference (MAI), we add to the OCDMA link a block of efficient error correction codes named Low Density Parity Check codes (LDPC). The LDPC decoding algorithm, Belief Propagation (BP), usually employed to correct errors due to Gaussian noise, is reconsidered in order to take into account the MAI binomial distribution. The performance of an OCDMA link using 1 Dimensional and 2 Dimensional code sequences along with several LDPC codes is investigated. The performance is enhanced not only in an ideal case with only MAI, but also in a noisy case with MAI and thermal noise. With such error correction coding scheme, the constraints over OCDMA parameters and the signal to noise ratio are greatly relaxed.

## Alternative Approximation of Check Node Algorithm for DVB-S2 LDPC Decoder

- **Status**: ✅
- **Reason**: DVB-S2 체크노드 min-sum을 Taylor급수로 근사하는 새 디코더 알고리즘+CNU 아키텍처(C/D). 부호 비의존적으로 NAND LDPC에 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4299991
- **Type**: conference
- **Published**: 25-31 Aug.
- **Authors**: O. Eljamaly Toumaz, P. Sweeney
- **PDF**: https://ieeexplore.ieee.org/document/4299991
- **Abstract**: In this paper, a new approximation of the check node rule algorithm is proposed for updating the check nodes messages in LDPC decoding. The new technique evaluates the check node min-sum magnitude algorithm using the Taylor series and results in reduced computational complexity and hardware implementation. The architecture of a check node processing unit, implementing the new alternative approximation of the check node, is also presented. The proposed method can achieve the same BER performance with a reduction of ~20% hardware complexity in the LDPE decoder. The simulation results obtained shows that the packet error rate performance of 10-7, which is the DVB-S2 requirement for MPEG packets transmitted, can be achieved with this new method.

## Memory Efficient Block-Serial Architecture for Programmable, Multi-Rate Multi-Length LDPC Decoder

- **Status**: ✅
- **Reason**: D/C - 802.16e LDPC 디코더 HW 아키텍처(block-serial), Approximate-Min 스킴으로 extrinsic 메모리 68% 절감, FPGA 구현
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4469593
- **Type**: conference
- **Published**: 22-24 Aug.
- **Authors**: Xiyu Zhou, Zhaoyang Zhang
- **PDF**: https://ieeexplore.ieee.org/document/4469593
- **Abstract**: This paper presents a flexible decoder architecture which supports twelve combinations of code lengths-576, 1152, 1728, 2304 bits and code rates-1/2, 2/3, 3/4 for block-serial irregular LDPC codes based on the IEEE 802.16e standard [1]. Approximate-Min Scheme is used to increase memory efficiency during message processing. At least 68.4% extrinsic message memory is saved and this reduction increases with the code rate. A prototype of the LDPC decoder has been implemented and tested on an Ateral FPGA.

## Four Intuitive Messages for LDPC Codes

- **Status**: ✅
- **Reason**: sum-product 디코딩용 신규 메시지(APPR/APP/APPD/hybrid) 저복잡도 변형 — 바이너리 LDPC 디코더 알고리즘(C) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4313292
- **Type**: conference
- **Published**: 22-24 Aug.
- **Authors**: Young Gil Kim, Norman C. Beaulieu
- **PDF**: https://ieeexplore.ieee.org/document/4313292
- **Abstract**: Four new messages for decoding of low-density parity-check (LDPC) codes are proposed. An a posteriori probability ratio (APPR) message, an a posteriori probability (APP) message, and an a posteriori probability difference (APPD) message for variable and check nodes are derived for sum-product decoding of LDPC codes. Also, we propose a hybrid APPD-APPR message, which denotes a hybrid message with an APPD variable node message and APPR check node message. All the proposed messages require only addition, subtraction, multiplication, and division operations for decoding of LDPC codes. We show that the hybrid APPD-APPR message-passing has the lowest complexity among the proposed messages.

## Implementation of a Flexible Encoder for Structured Low-Density Parity-Check Codes

- **Status**: ✅
- **Reason**: structured LDPC(802.16e)용 유연한 인코더 FPGA 아키텍처 — 코드율/길이 가변 HW, 이식 가능(D, 애매→살림)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:4313268
- **Type**: conference
- **Published**: 22-24 Aug.
- **Authors**: Sunitha Kopparthi, Don M. Gruenbacher
- **PDF**: https://ieeexplore.ieee.org/document/4313268
- **Abstract**: The hardware implementation of an encoder for randomly generated low-density parity-check (LDPC) codes requires large area. Using structured LDPC codes decreases the encoding complexity and also provides design flexibility. In this paper, an architecture for implementing an encoder is presented that adheres to the structured LDPC codes defined in the IEEE 802.16e standard. The design methodology is flexible in terms of both the code rate and code length. Results are provided for an implementation on a Stratix FPGA for codes with rates 1/2, 2/3, 3/4 and 5/6, and block lengths ranging from 576-2304. The number of logic elements, clock speed, and throughput of the encoder for the different code lengths are presented. The design achieves encoding rates in excess of 400 Mbps.

## Improved Iterative Bit Flipping Decoding Algorithms for LDPC Convolutional Codes

- **Status**: ✅
- **Reason**: LDPC convolutional용 개선 bit-flipping 디코더 — 저복잡도 HW/코딩이득, 디코더 알고리즘(C) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4313293
- **Type**: conference
- **Published**: 22-24 Aug.
- **Authors**: Xin Sheng Zhou, Bruce F. Cockburn, Stephen Bates
- **PDF**: https://ieeexplore.ieee.org/document/4313293
- **Abstract**: A new class of iterative bit flipping (BF) decoding algorithms adapted for low-density parity check (LDPC) convolutional codes is proposed. Compared with Gallager's original BF algorithm, the new BF algorithms improve both the coding gain and the error correction speed. At a bit error rate (BER) of 10 , the best of the new bit-flipping algorithms achieves, after only 6 iterations and with much simpler decoding hardware, a coding gain within 3.5 dB of that of the conventional min-sum belief propagation decoding algorithm.

## Lowering the Error Floor of LDPC Codes by a Two-stage Hybrid Decoding Algorithm

- **Status**: ✅
- **Reason**: feedback-BP 2단 하이브리드 디코딩으로 error floor 저감 — 디코더 알고리즘(C)/error floor(E) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4469460
- **Type**: conference
- **Published**: 22-24 Aug.
- **Authors**: Yueguang Bian, Youzheng Wang, Jing Wang
- **PDF**: https://ieeexplore.ieee.org/document/4469460
- **Abstract**: In this paper, a hybrid decoding scheme is proposed to lower the error floor of low-density parity-check codes. With the observation that some error bits' LLR values oscillate throughout iterative decoding procedure, a "feedback BP" (FBP) decoding algorithm is presented as second-stage decoding cell to reduce the phenomena of oscillations. The hybrid decoding scheme, which consists LLR-BP decoding algorithm and FBP decoding algorithm, detects errors in the codewords obtained by using the parity check equations of LDPC codes. Simulation results show that the new decoding scheme exhibits a lower error floor than that of belief propagation decoding algorithm in the moderate and high SNR region.

## Serial Sum-Product Architecture for Low-Density Parity-Check Codes

- **Status**: ✅
- **Reason**: 직렬 sum-product 아키텍처: 메모리 절감 bit-node centric HW 구조, NAND LDPC HW(D)에 이식 가능
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:4317812
- **Type**: conference
- **Published**: 13-16 Aug.
- **Authors**: Ruwan N.S. Ratnayake, Erich F. Haratsch, Gu-Yeon Wei
- **PDF**: https://ieeexplore.ieee.org/document/4317812
- **Abstract**: A serial sum-product architecture for low-density parity-check (LDPC) codes is presented. In the proposed architecture, a standard bit node processing unit computes the bit to check node messages sequentially, while the check node computations are broken up into several steps and computed on the fly. This bit node centric architecture requires considerably less memory compared to other serial architectures, including the check node centric architecture.

## Novel Efficient Check Node Update Implementations for Row Weight Matched Min-Sum Algorithm

- **Status**: ✅
- **Reason**: row-weight matched Min-Sum의 효율적 check node update HW 구현 — 디코더(C)/HW(D) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4392663
- **Type**: conference
- **Published**: 13-15 Aug.
- **Authors**: Lu Xin, Xu Jun
- **PDF**: https://ieeexplore.ieee.org/document/4392663
- **Abstract**: This paper has presented various Min-Sum related LDPC decoding algorithms and their typical hardware architectures of check node update in the scenario of parallel implementation. For one check node update of Normalized Min-Sum algorithm, if the current row weight is dc, dc multiplications are needed. If dc is large, dc multiplications are needed, which leads to high complexity. In this article, one innovative method for check node update has been found, which can obviously reduce the number of comparison/selection operations for the row weight matched Min-Sum algorithm of high rate LDPC codes. Simulations have claimed the performance of row weight matched Min-Sum is nearly the same as that of Log-BP, namely the optimal algorithm, which has shown that row weight matched Min-Sum are good choices for LDPC decoding.
