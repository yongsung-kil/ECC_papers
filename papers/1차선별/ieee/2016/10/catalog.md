# IEEE Xplore — 2016-10 (1차선별 통과)


## A New Density Evolution Approximation for LDPC and Multi-Edge Type LDPC Codes

- **Status**: ✅
- **Reason**: 바이너리 LDPC/MET-LDPC용 신규 밀도진화 근사 — 코드설계(E) 임계값 추정 기법 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7544625
- **Type**: journal
- **Published**: Oct. 2016
- **Authors**: Sachini Jayasooriya, Mahyar Shirvanimoghaddam, Lawrence Ong +2
- **PDF**: https://ieeexplore.ieee.org/document/7544625
- **Abstract**: This paper considers density evolution for low-density parity-check (LDPC) and multi-edge type LDPC (MET-LDPC) codes over the binary input additive white Gaussian noise channel. We first analyze three single-parameter Gaussian approximations for density evolution and discuss their accuracy under several conditions, namely, at low rates, with punctured and degree-one variable nodes. We observe that the assumption of symmetric Gaussian distribution for the density-evolution messages is not accurate in the early decoding iterations, particularly at low rates and with punctured variable nodes. Thus, single-parameter Gaussian approximation methods produce very poor results in these cases. Based on these observations, we then introduce a new density evolution approximation algorithm for LDPC and MET-LDPC codes. Our method is a combination of full density evolution and a single-parameter Gaussian approximation, where we assume a symmetric Gaussian distribution only after density-evolution messages closely follow a symmetric Gaussian distribution. Our method significantly improves the accuracy of the code threshold estimation. Additionally, the proposed method significantly reduces the computational time of evaluating the code threshold compared with full density evolution thereby making it more suitable for code design.

## FPGA-Based Rate-Compatible LDPC Codes for the Next Generation of Optical Transmission Systems

- **Status**: ✅
- **Reason**: rate-compatible LDPC(puncturing+generalized LDPC)와 FPGA 아키텍처 — 코드설계(E)+HW(D) 이식 가능, 바이너리
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7548329
- **Type**: journal
- **Published**: Oct. 2016
- **Authors**: Ding Zou, Ivan B. Djordjevic
- **PDF**: https://ieeexplore.ieee.org/document/7548329
- **Abstract**: In this paper, we propose a rate-compatible forward error-correcting (FEC) scheme based on low-density-parity check (LDPC) codes together with its software reconfigurable unified field-programmable gate array (FPGA) architecture. By FPGA emulation, we demonstrate that the proposed class of rate-compatible LDPC codes based on puncturing and generalized LDPC coding with an overhead from 25% to 46% provides a coding gain ranging from 12.67 to 13.8 dB at a post-FEC bit-error rate (BER) of 10−15. As a result, the proposed rate-compatible codes represent one of the strong FEC candidates of soft-decision FEC for both short-haul and long-haul optical transmission systems.

## Optimized Design of Finite-Length Separable Circulant-Based Spatially-Coupled Codes: An Absorbing Set-Based Analysis

- **Status**: ✅
- **Reason**: 유한길이 SC-LDPC absorbing set 분석+최적 cutting vector로 error floor 개선, 바이너리 케이스 명시—이식가능 코드설계(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7529198
- **Type**: journal
- **Published**: Oct. 2016
- **Authors**: Behzad Amiri, Amirhossein Reisizadehmobarakeh, Homa Esfahanizadeh +2
- **PDF**: https://ieeexplore.ieee.org/document/7529198
- **Abstract**: In this paper, we characterize the finite-length performance of separable circulant-based spatially-coupled (SCB-SC) LDPC codes for transmission over the additive white Gaussian noise channel. For a general class of finite-length graph-based codes, it is known that the existence of small absorbing sets causes a performance degradation in the error floor regime. We first present the mathematical conditions for the existence of absorbing sets in binary SCB-SC codes. This analysis enables us to find the exact number of absorbing sets as a function of the design parameters. In particular, our results show that the choice of the cutting vector affects the number of absorbing sets and, therefore, the error floor performance of the code. For a fixed column weight, we find provably optimal cutting vectors that result in the least number of absorbing sets. Furthermore, we extend our analysis to nonbinary SCB-SC codes, where we show that the choice of the cutting vector is not as critical as in the binary case. We provide an algorithm which provably removes the problematic nonbinary absorbing sets from nonbinary SCB-SC codes by informed selection of edge labels. Our simulation results show the superior error floor performance of our designed binary and nonbinary SCB-SC codes compared with binary unstructured and nonbinary quasi-cyclic SC codes available in the open literature.

## Anytime Characteristics of Protograph-Based LDPC Convolutional Codes

- **Status**: ✅
- **Reason**: protograph LDPC convolutional(XS-LDPCC) 신규 구성·유한길이 성능·밀도진화 — 코드설계(E) 이식 가능, 바이너리(BEC/BIAWGN)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7549049
- **Type**: journal
- **Published**: Oct. 2016
- **Authors**: Nan Zhang, Md. Noor-A-Rahim, Badri N. Vellambi +1
- **PDF**: https://ieeexplore.ieee.org/document/7549049
- **Abstract**: Anytime transmission has been shown to be an effective means of stabilizing an unstable system over noisy channels. A crucial issue in implementing anytime transmission strategies is the design of anytime codes that offer good finite-length performance and asymptotic anytime properties. This paper introduces an efficient anytime code derived from protograph-based low-density parity-check convolutional codes known as extended S-LDPCC (XS-LDPCC) codes. The asymptotic anytime properties of XS-LDPCC codes over both the binary erasure channel (BEC) and the binary-input additive white Gaussian noise (BIAWGN) channel are demonstrated through density evolution. By means of certain observations verified by simulations, we provide accurate estimates of the delay exponents of XS-LDPCC codes over the BEC and the BIAWGN channel. Through simulations, the finite-length performance of XS-LDPCC codes and the effects of different code design parameters are quantified.

## Design and implementation of scalable throughput fast convergence LDPC decoder

- **Status**: ✅
- **Reason**: SMS+WBF 통합 빠른수렴 디코더+76% 스케일링+WBF 신규설계 FPGA 구현, 이식 가능 디코더/HW(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7867265
- **Type**: conference
- **Published**: 3-5 Oct. 2
- **Authors**: Mostafa A. Sayed, Liu Rongke, Zhao Ling
- **PDF**: https://ieeexplore.ieee.org/document/7867265
- **Abstract**: It is known that the more reliable LDPC code is the longer code, and it is also known that LDPC decoders with flooded architecture which allow parallel processing can achieve high throughputs. But, just architectures become very complex and require more hardware resources when the code length is large and random, so achieving a high error correction rate on short code lengths is considered a challenge. In this letter, an FPGA design and implementation of a scalable LDPC decoder for short code length are represented. The proposed LDPC decoder is based on the integration between Scaled MSA (SMS) with a Weighted Bit Flipping (WBF) algorithm to allow fast convergence and enhance the error rate, while high throughput is obtained from using flooded scheduling strategy. The results show that the new method can achieve BER reaches to 10-6 and FER reaches to 10-4 at 2.5 dB SNR over BAWGC using BPSK as a modulation scheme. In this letter also, the architecture of this algorithm is exploited to create a scalable design to achieve variable throughputs reaches to multi Gbps versus variable performances. A new scaling method that allows a 76% reduction, and new efficient design for WBF, are introduced.

## An IDD receiver of LDPC coded modulation scheme for flash memory applications

- **Status**: ✅
- **Reason**: 플래시메모리용 LDPC coded modulation IDD 수신기 아키텍처, 저복잡도 디코더+스케줄링 NAND 직접(A/C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7803956
- **Type**: conference
- **Published**: 25-28 Oct.
- **Authors**: Mao-Ruei Li, Ting-Yu Kuan, Huang-Chang Lee +1
- **PDF**: https://ieeexplore.ieee.org/document/7803956
- **Abstract**: A previous study shows that a low-density parity-check (LDPC) coded modulation scheme with an extremely sparse parity-check matrix and non-Gray mapping is able to achieve an error-rate performance compatible to that of a conventional Gray-mapping based scheme. This paper presents an associated iterative demodulation and decoding (IDD) receiver architecture that is targeted at flash memory applications. By adopting this extremely spare LDPC code, both the storage and the computational complexity of the decoder are lowered. The complexity of demodulator is also reduced by using the proposed simplified method. Moreover, a two-codeword scheduling approach is used so as to minimize the idles and, hence, a high throughput can be achieved. Compared to the conventional Gray-based scheme, the proposed scheme provides a similar error performance and a better hardware efficiency.

## Implementation of a high throughput LDPC codec in FPGA for QKD system

- **Status**: ✅
- **Reason**: QKD reconciliation이나 BP Min-Sum 디코더 FPGA 고처리량 구현·하삼각 인코딩이 NAND LDPC HW로 이식 가능(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:7998780
- **Type**: conference
- **Published**: 25-28 Oct.
- **Authors**: Cong Hui, Yonggang Wang, Xiaoming Lu
- **PDF**: https://ieeexplore.ieee.org/document/7998780
- **Abstract**: The contribution of this paper is implementing a high throughput LDPC codec in FPGA for quantum key distribution (QKD) system. By software, the throughput of error correction in QKD system via LDPC codec could only reach 1.8Mbps, which is not satisfactory for high speed QKD systems. Thus, it is desirable that LDPC error correction is realized in FPGA to increase the throughput. LDPC codec is implemented according to IEEE802.16e standard. The encoder directly uses a parity-check matrix of lower triangular structure without the construction of generator matrix, so that it effectively reduce the encoding complexity of Richardson encoding algorithm. The decoder uses the BP Min-Sum algorithm to balance performance and complexity. The codec is implemented in an Altera Arria II EP2AGX260 FPGA with a 2304-bit code length and 2/3 code rate. The partly parallel decoding structure achieves a 99.95 Mbps processing throughput on the condition that the maximum number of iterations for each code block is 20. The achievable throughput is much higher than the requirements of current QKD systems.

## On using the cyclically-coupled QC-LDPC codes in future SSDs

- **Status**: ✅
- **Reason**: SSD용 cyclically-coupled QC-LDPC 신규 코드설계+디코더 공동설계+FPGA 구현, NAND 직접(A/D/E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7804048
- **Type**: conference
- **Published**: 25-28 Oct.
- **Authors**: Qing Lu, Chiu-Wing Sham, Francis C. M. Lau
- **PDF**: https://ieeexplore.ieee.org/document/7804048
- **Abstract**: As the flash memory continues its capacity scaling and correspondingly decreases its reliability, a technology upgrade regarding the error-correction engine in state-of-art solid-state drives (SSDs) is intensely expected. Due to their limit-approaching decoding ability, low-density parity-check (LDPC) codes are seen as one of the most promising substitute for the traditional BCH codes, though implementation barriers remain to degrade their performance. In our recent work, a co-design of LDPC block codes and their decoder architecture are developed and found suitable to apply to address these barriers with an overall excellence in error rate, complexity as well as throughput. Four codes of 4 KB and 4/5 rate are proposed and their FPGA-based implementations are conducted. It is shown that the decoders reach 1.47 Gb/s throughput at 100 MHz clock rates, and their complexity are estimated to be 1 million gates with 1 Mb memory.

## A post-processing algorithm for reducing strong error effects in NAND flash memory

- **Status**: ✅
- **Reason**: A/C: NAND 플래시 LDPC용 신규 post-processing 디코더 알고리즘(edge-based, 강한오류 변수노드 신뢰도 감소) - 직접 이식 대상
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7804004
- **Type**: conference
- **Published**: 25-28 Oct.
- **Authors**: Sung-Rae Kim, Kijun Lee, Gyuyeol Kong +7
- **PDF**: https://ieeexplore.ieee.org/document/7804004
- **Abstract**: This paper introduces a novel post-processing algorithm for low-density parity-check (LDPC) codes adequate for NAND flash memory, to improve error correction capability of a soft decision decoding by reducing strong error effects in an efficient way. In this algorithm, it can detect variable nodes of strong errors using incoming check-to-variable (c2v) messages and reduce magnitude of channel reliability of the nodes to avoid supplying large erroneous variable-to-check (v2c) messages for the check nodes. The proposed post processing algorithm with a finite precision LDPC decoding scheme is named edge-based post processing and effectively reflects time varying characteristic of NAND flash channel.

## Reduced complexity look-up table based π-rotation LDPC decoder

- **Status**: ✅
- **Reason**: permutation mapping+normalized min-sum 최적화 LUT 기반 디코더 아키텍처, NAND LDPC HW로 이식 가능(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7998936
- **Type**: conference
- **Published**: 25-28 Oct.
- **Authors**: Hao Wang, Hongda Wang, Gerald E. Sobelman +1
- **PDF**: https://ieeexplore.ieee.org/document/7998936
- **Abstract**: This paper presents a look-up table based, configurable and serial-parallel scheduled π-rotation LDPC decoder. By using the proposed permutation mapping scheme together with an optimized normalized min-sum decoding algorithm, the LDPC decoder structure and circuit resource requirements can be greatly reduced. Furthermore, the proposed approach is compatible with different code lengths, bit widths and permutation vectors provided that the parity-check matrix has the π-rotation structure. Specifically, the proposed architecture in this work is implemented with a code length of 1968, a code rate of 1/2, 6-bit quantization and an iteration limit of 10 on a Xilinx Virtex4 XC4VLS200 FPGA. The synthesis results demonstrate the feasibility of the proposed approach to achieve a good BER-SNR performance using a simple decoding scheme and an efficient circuit implementation.

## Experimental demonstration of a variable-rate LDPC code with adaptive low-power decoding for next-generation optical networks

- **Status**: ✅
- **Reason**: 가변율 비연접 LDPC + 적응형 저전력 디코더 28nm CMOS 구현, error-floor 회피 신규 HW/디코더 기여(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7831110
- **Type**: conference
- **Published**: 2-6 Oct. 2
- **Authors**: Damian A. Morero, Mario A. Castrillón, Teodoro A. Goette +5
- **PDF**: https://ieeexplore.ieee.org/document/7831110
- **Abstract**: We design and implement a variable-rate non-concatenated LDPC code with an adaptive power-consumption decoder using 28nm CMOS technology. Experimental results obtained from a fabricated 256Gb/s optical transceiver demonstrate that the proposed LDPC achieves a NCG of 11.4dB at BER=10−15 without error-floor.

## A study on construction of Low-Density Parity-Check codes using nonlinear feedback shift registers

- **Status**: ✅
- **Reason**: NFSR de Bruijn 시퀀스 기반 LDPC 코드 구성 - 신규 코드 설계 기법(E), 바이너리 LDPC 구성
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7763564
- **Type**: conference
- **Published**: 19-21 Oct.
- **Authors**: Shotaro Moriyama, Akio Tsuneda
- **PDF**: https://ieeexplore.ieee.org/document/7763564
- **Abstract**: Digital communications are daily used in the modern society supported by ICT (Information and Communication Technology). In digital communications, an error-control technology is necessary for correcting/detecting bit errors caused by channel noise. Many kinds of error-correcting/detecting codes have been proposed. Among them, LDPC (Low-Density Parity-Check) codes are known to have error-correcting ability that is near to the Shannon limit. In this paper, we propose the construction of LDPC (Low-Density Parity-Check) codes based on de Bruijn sequences generated by NFSRs (Nonlinear Feedback Shift Registers). The BER (Bit Error Rate) performance of the proposed codes is also evaluated.

## Burst error sensing scheme for page-oriented data

- **Status**: ✅
- **Reason**: 페이지지향 데이터 버스트 에러 센싱+소거 디코딩. 스토리지/NAND 페이지 ECC 관련, 애매하나 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7763371
- **Type**: conference
- **Published**: 19-21 Oct.
- **Authors**: Seongkwon Jeong, Jaejin Lee
- **PDF**: https://ieeexplore.ieee.org/document/7763371
- **Abstract**: Burst error occurs due to various factors and degrades the system performance. In this paper, we propose a burst error sensing scheme for page-oriented data. Using this scheme, the proposed method can sense a two-dimensional burst error location. In addition, it is possible to improve the performance by using erasure decoding on the sensed burst error position.

## Decoding LDPC codes with binary perturbation

- **Status**: ✅
- **Reason**: LDPC 디코딩 perturbation 기법(m-sequence 바이너리 노이즈) 개선 - 디코더 알고리즘 변형(C), 바이너리 LDPC에 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7763563
- **Type**: conference
- **Published**: 19-21 Oct.
- **Authors**: Eun Chong Baek, Hyun Jae Lee, Sang-Hyo Kim
- **PDF**: https://ieeexplore.ieee.org/document/7763563
- **Abstract**: In this paper, we provide a simplified perturbation method for LDPC decoding using a binary noise generator with maximal length sequence (m-sequence). The proposed method provides the improved performance of the conventional perturbation-based decoding without performance degradation.

## Anti-jamming partially regular LDPC codes for follower jamming with Rayleigh block fading in frequency hopping spread spectrum

- **Status**: ✅
- **Reason**: follower jamming 대응 partially regular LDPC 신규 설계 + density evolution 최적화. 바이너리 LDPC 코드설계(E) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7763538
- **Type**: conference
- **Published**: 19-21 Oct.
- **Authors**: Chanki Kim, Jong-Seon No, Jinsoo Park +2
- **PDF**: https://ieeexplore.ieee.org/document/7763538
- **Abstract**: Frequency hopping spread spectrum is widely used for military communication. Anti-jamming scheme for the system has been one of the main topics for a long time. This paper introduces follower jamming model with random dwell time and block fading environment with M-ary frequency shift keying (MFSK) modulation. For coding perspective, new low density parity check (LDPC) codes against follower jamming are proposed. To optimize codes over jamming environment, the partially regular structure and the corresponding density evolution are used. Simulation results show that the proposed codes outperform those of IEEE 802.16e standard in the presence of follower noise jamming.

## A paired-page reading scheme for NAND flash memory

- **Status**: ✅
- **Reason**: NAND 플래시 paired-page 공동 디코딩/신호처리 + 센싱 횟수 감소. NAND 직접(A)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7763369
- **Type**: conference
- **Published**: 19-21 Oct.
- **Authors**: Sangha Lee, Daesung Kim, Jeongseok Ha
- **PDF**: https://ieeexplore.ieee.org/document/7763369
- **Abstract**: In this paper, we propose a joint decoding and signal processing scheme for NAND flash memory. The proposed scheme provides a considerable improvement of error correcting capability when the raw error rate depends on programming voltage levels, equivalently user data, of the target memory cell and/or adjacent cells. It will be shown that the proposed scheme also requires a fewer number of voltage sensing than the existing scheme, which leads to lower latency in the read operation of NAND flash memory.

## An efficient scheduling scheme for layered belief propagation decoding of regular LDPC codes

- **Status**: ✅
- **Reason**: regular LDPC layered BP의 신규 체크노드 스케줄링(저신뢰 이웃 기반 선택), 이식 가능 디코더 기법(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7765392
- **Type**: conference
- **Published**: 18-20 Oct.
- **Authors**: Hua Li, Hong Ding, Linhua Zheng +3
- **PDF**: https://ieeexplore.ieee.org/document/7765392
- **Abstract**: Schedule plays an important role in layered belief propagation (BP) decoding of low-density parity-check (LDPC) codes. It affects the error-rate performance as well as convergence rate of the decoder. In this paper, an efficient scheduling scheme is proposed to arrange the updating order of check nodes for layered BP decoder of regular LDPC codes. This scheme selects check node one at a time based on the reliability of the variable nodes. Specifically each time the check node with maximum number of low-reliability neighbors is selected. For simplicity, we introduce the updating state instead of the real-time messages to represent variable-node reliability. Simulation results on regular LDPC codes prove that the proposed scheduling scheme can obtain efficient schedules with fast convergence and good error-rate performance.

## Novel method for improving performances of normalized MS decoder using WIMAX code

- **Status**: ✅
- **Reason**: Girth-Aware NMS 신규 디코더(Tanner graph girth로 정규화계수 조정), 바이너리 LDPC 디코더 개선(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7843926
- **Type**: conference
- **Published**: 17-19 Oct.
- **Authors**: Abdelilah Kadi, Mostafa Mrabti, Said Najah +1
- **PDF**: https://ieeexplore.ieee.org/document/7843926
- **Abstract**: LDPC code is a powerful error correcting code used in many communication systems. Efficient decoding algorithm and hardware implementation of LDPC code is an important issue. The paper proposes an improved version of the Normalized Min-Sum (NMS) decoding algorithm named “Girth-Aware NMS”. The principle of the GA-NMS is to determine “offline” the optimal normalisation factor of the extrinsic message using the structure property of the Tanner Graph associated to the LDPC matrix. The idea can be expressed simply: a check node implied in one, or more, cycle of minimum size (the so-called Girth) in the Tanner Graph is more subjected to self-confirmation than other check nodes. Thus, the extrinsic messages generated by this type of check nodes should be more aggressively “normalized” (or attenuated) than other check nodes. In the context of the IEEE P802.16e standard (WIFI standard), simulation results of the GA-NMS shows both improved decoding performance and reduced average number of decoding iterations.

## A novel LDPC decoder based on coarse-grained reconfigurable array

- **Status**: ✅
- **Reason**: NMS 기반 LDPC 디코더 CGRA/VLSI HW 아키텍처(45nm), 병렬 HW 기법(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:7790506
- **Type**: conference
- **Published**: 16-19 Oct.
- **Authors**: Yu Gong, Tingting Xu, Zhuang Chen +1
- **PDF**: https://ieeexplore.ieee.org/document/7790506
- **Abstract**: This paper proposes a novel LDPC decoder based on Coarse-Grained Reconfigurable Array, named RaSP-D (Reconfigurable Signal Processor for Decoder). According to the Normalized Min-Sum (NMS) Algorithm, the fusion-step routing structure with corresponding mapping strategy is implemented in the proposed RaSP-D. The verification of RaSP-D is based on TSMC 45nm craft, and the processor works at the frequency of 300MHz. The experimental results show that the average array utilization rate of RaSP-D with proposed mapping strategy can be up to 80% in regular LDPC codes. The peak throughput of RaSP-D is over 1 Gbps, which satisfies the LTE-A standard. Besides, the RaSP-D supports 4 kinds of code rates with the code range of 576~2304 bit. Compared with the state-of-the-art architectures, such as ASICs, DSPs and CGRAs, RaSP-D achieves larger range of code rate, higher throughput and higher flexibility with dynamic reconfiguration.

## A data processing architecture for realtime decoding of extremely long LDPC codes

- **Status**: ✅
- **Reason**: BP 기반 신규 분산 디코딩 알고리즘+데이터처리 아키텍처—이식 가능 디코더/HW 기법(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7868611
- **Type**: conference
- **Published**: 16-18 Oct.
- **Authors**: Quanqiang Miao, Bo Bai, Wei Chen +1
- **PDF**: https://ieeexplore.ieee.org/document/7868611
- **Abstract**: Low-Density Parity-Check (LDPC) codes belong to a class of linear block codes that can approach the Shannon limit. However, due to the high decoding complexity, LDPC codes with extremely long block lengths will result in large decoding latency in practical applications. Recently, Cloud Radio Access Networks (C-RANs) have attracted much attention because of their innovative architecture, which involves embedding cloud computing capability into wireless networks. In this context, C-RANs provide an ideal platform for breaking the decoding bottleneck of LDPC codes with extremely long block lengths. However, given that there are currently as yet no specific cloud computing techniques proposed for C-RAN, the data processing architecture for LDPC decoding is still an open problem. In this paper, based on the Spark cloud computing platform, a data processing architecture is proposed for realtime decoding of extremely long LDPC codes. Based on the principle behind the belief propagation (BP) decoding algorithm, a novel distributed BP decoding algorithm is proposed and implemented on a Spark based cloud computing platform. Extensive experimentation illustrates that the proposed architecture enjoys a significant performance gain in decoding latency. Therefore, this work can be seen as a promising example of applying powerful cloud computing techniques to enhance the performance of wireless networks.

## An escaping scheme for gradient descent bit-flipping decoding of LDPC codes

- **Status**: ✅
- **Reason**: GDBF 디코딩의 escaping scheme(syndrome weight 기반 loop 탈출) — 이식 가능 BF 디코더 개선(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7853052
- **Type**: conference
- **Published**: 15-17 Oct.
- **Authors**: Hua Li, Hong Ding, Linhua Zheng
- **PDF**: https://ieeexplore.ieee.org/document/7853052
- **Abstract**: The gradient descent bit-flipping (GDBF) decoding algorithm offers an attractive tradeoff between performance and complexity compared with the other bit-flipping (BF) decoding algorithms. However, the performance of GDBF decoding is seriously effected by infinite decoding loop, which always results in decoding failure when maximal iteration number is reached. To avoid the decoding loop and improve the performance, an efficient escaping scheme is proposed for the GDBF algorithm in this paper. This scheme firstly introduces syndrome weight to detect the decoding loop. If a decoding loop is detected, the escaping mechanism works, where only the bit which can decrease the syndrome weight most efficiently is selected to be flipped. In addition, the excluding set is introduced to further prevent the local maximum. Simulation results show that the GDBF algorithm can obtain about 1 dB code gain by utilizing this scheme. Compared with noise GDBF, it has 0.1dB performance loss as well as lower complexity.

## A comparison study of LDPC decoding using accelerated ADMM and over-relaxed ADMM

- **Status**: ✅
- **Reason**: 바이너리 LDPC용 ADMM/over-relaxed ADMM LP 디코더 알고리즘 → 이식 가능 디코더(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7924691
- **Type**: conference
- **Published**: 14-17 Oct.
- **Authors**: Xiaopeng Jiao, Jianjun Mu, Junjun Guo
- **PDF**: https://ieeexplore.ieee.org/document/7924691
- **Abstract**: The alternating direction method of multipliers (ADMM) with over-relaxation and the accelerated ADMM are two effective methods to improve the convergence rate of ADMM. In this paper, an efficient linear programming (LP) decoder based on accelerated ADMM for low-density parity-check (LDPC) codes is proposed. Then it is shown that the ADMM update steps for decoding LDPC codes using the accelerated ADMM and the over-relaxed ADMM are quite similar. Therefore, it is impossible to obtain a more efficient ADMM decoder by combining the two improved ADMM methods. Simulation results also validate that the average number of iterations for LDPC decoding using the accelerated ADMM and the over-relaxed ADMM are close to each other.

## Analysis and elimination of short cycles in LDPC convolutional codes

- **Status**: ✅
- **Reason**: LDPC convolutional code 단주기 사이클 제거/syndrome former 설계로 BER 개선, 바이너리 → 코드설계(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7924880
- **Type**: conference
- **Published**: 14-17 Oct.
- **Authors**: Ziqin Su, Qiaoyong Qiu, Hua Zhou
- **PDF**: https://ieeexplore.ieee.org/document/7924880
- **Abstract**: Time-invariant low-density parity-check convolutional codes (TI LDPC-CCs) can be represented by a polynomial-domain parity-check matrix derived from the corresponding quasi-cyclic (QC) LDPC block codes (LDPC-BCs), while time-varying (TV) LDPC-CCs can be obtained by unwrapping the parity-check matrices of LDPC-BCs. The cycle enumerators for TI and TV LDPC-CCs are compared. Based on the analysis of the graphical structures of short cycles in HT(D), we introduce a method of designing the polynomial syndrome former matrix HCRT(D) for LDPC-CCs. It eliminates short cycles and shows improved decoding performance on an additive white Gaussian noise (AWGN) channel with lower bit error ratio (BER) curves.

## Quantization and reliability-aware iterative majority-logic decoding algorithm for LDPC code in TLC NAND flash memory

- **Status**: ✅
- **Reason**: A/C: TLC NAND 플래시 LDPC용 양자화+신뢰도기반 majority-logic 디코더 신규 제안
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7752548
- **Type**: conference
- **Published**: 13-15 Oct.
- **Authors**: Lingjun Kong, Jiaying Wen, Guojun Han +3
- **PDF**: https://ieeexplore.ieee.org/document/7752548
- **Abstract**: Multi-level per cell (MLC) /Triple-Level per cell (TLC) technique significantly improves storage density with low cost increases, which stores more than one bit per cell, but also drastically decreases reliability in NAND flash memory. As the bit number per cell increases, correspondingly cell-to-cell interference (CCI) becomes the major challenge for NAND flash memory technology scaling. Recently, low-density parity-check (LDPC) code is considered as the most appropriate scheme of next generation Error Correcting Code (ECC) in NAND flash memory. In this paper, by exploiting the intra-cell characteristics in TLC NAND flash memory channels, a low-complexity quantization and reliability-Aware iterative majority-logic decoding (QR-IMLGD) algorithm for LDPC code is proposed to reduce the memory read latency and effectively improve the throughput of LDPC decoding. The proposed algorithm takes advantage of highly unequal error probability of input log-likelihood-ratios (LLRs) in the same cells, employ small bit-level quantizer and update only less reliable variable nodes that are initiated with higher error probability LLR values. Simulation results show that the proposed QR-IMLGD algorithm can yield a noticeable improvement in decoding convergence rate without compromising the error performance in TLC NAND flash memory channels.

## Construction of multiple-rate quasi-cyclic LDPC codes with girth eight

- **Status**: ✅
- **Reason**: E: Moore graph 기반 가변 rate girth-8 QC-LDPC 신규 구성, 바이너리 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7752486
- **Type**: conference
- **Published**: 13-15 Oct.
- **Authors**: Jia-Ling Li, Wen Chen, Xue-Qin Jiang +2
- **PDF**: https://ieeexplore.ieee.org/document/7752486
- **Abstract**: This paper proposes a new approach to construct quasi-cyclic low-density parity-check (QC-LDPC) codes of girth 8. The proposed codes are based on a bipartite graph called Moore graph. By decomposing the bit nodes of the bipartite graph, the proposed QC-LDPC codes have variable code lengths and rates. Simulation results show that the proposed QC-LDPC codes have good performance with an iterative decoding over an AWGN channel.

## Grouping dynamic scheduling for LDPC codes in symmetric alpha-stable impulsive noise

- **Status**: ✅
- **Reason**: C: 그룹 동적 스케줄링 BP 디코딩 신규 기법, 바이너리 LDPC BP에 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7752594
- **Type**: conference
- **Published**: 13-15 Oct.
- **Authors**: Bin Dai, Rongke Liu, Zhen Mei +2
- **PDF**: https://ieeexplore.ieee.org/document/7752594
- **Abstract**: In some practical applications, impulsive noise can severely degrade the performance of a communication system. As a class of powerful error correction codes, Low-density parity-check (LDPC) codes ha,ve been shown superior performance on AWGN channels. In addition, belief propagation (BP) decoding algorithm of LDPC codes based on scheduling strategy has better performance and faster convergence rate than conventional BP decoding algorithm. In this paper, a dynamic scheduling of LDPC codes is first used on impulsive noise channels. Moreover, we propose a new scheduling strategy which named grouping dynamic scheduling (GDS) for impulsive noise channels to further improve the performance. Simulation results show that the dynamic scheduling on impulsive noise channels provides more performance gain than AWGN channels and the gain becomes significant when the channel is more impulsive. In addition, compared with conventional dynamic scheduling strategy, our proposed algorithm not only provides better performance, but also lowers the actual decoding computational complexity.

## A self-normalized weighted bit-flipping decoding algorithm for LDPC codes

- **Status**: ✅
- **Reason**: C: 자기정규화 weighted bit-flipping 디코딩 신규 알고리즘, 바이너리 LDPC 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7752630
- **Type**: conference
- **Published**: 13-15 Oct.
- **Authors**: Chunli Wang, Xiaofu Wu, Wei-Ping Zhu
- **PDF**: https://ieeexplore.ieee.org/document/7752630
- **Abstract**: A novel self-normalized weighted bit-flipping (SNWBF) decoding algorithm for low-density parity-check (LDPC) codes is proposed. Compared to the best known weighted bit-flipping decoding, the SNWBF algorithm converges significantly faster but with little performance penalty. For decoding of LDPC codes, the proposed SNWBF algorithm considers not only the reliability of the neighboring check nodes, but also the reliability of each variable node. Compared to the IMWBF algorithm, the proposed algorithm does not require multiplicative normalization and performs even better.

## Hybrid iterative decoding for LDPC codes based on gradient descent bit-flipping algorithm

- **Status**: ✅
- **Reason**: C: GDBF 비트플리핑에 반복 신뢰도 갱신 추가한 하이브리드 LDPC 디코더, NAND에 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7752445
- **Type**: conference
- **Published**: 13-15 Oct.
- **Authors**: Hua Li, Hong Ding, Linhua Zheng
- **PDF**: https://ieeexplore.ieee.org/document/7752445
- **Abstract**: Gradient descent bit-flipping (GDBF) decoding for low-density parity-check (LDPC) codes has gained great attentions because of low complexity and relatively good performance. However, the performance of the GDBF decoding is still much poorer than that of the MS algorithm. To further improve the performance, the iterative decoding process is introduced to GDBF decoding in this paper. At the end of each iteration, the latest information is used to update the reliability of the flipped bit, by which its reliability is greatly improved. Simulation results indicate that the proposed algorithm has about 0.4 dB performance gains compared to GDBF. Meanwhile, there is small computational complexity increased.

## Construction of quasi-cyclic low-density parity-check codes using Hamming codewords

- **Status**: ✅
- **Reason**: E: Hamming codeword 기반 girth-6/8 QC-LDPC 신규 구성(PEG 대비 우수), 바이너리 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7752623
- **Type**: conference
- **Published**: 13-15 Oct.
- **Authors**: Haijing Zhong, Shancheng Zhao, Li Chen +1
- **PDF**: https://ieeexplore.ieee.org/document/7752623
- **Abstract**: In this paper, we propose a new approach to construct quasi-cyclic low-density parity-check (QC-LDPC) codes using Hamming codewords of weight three, namely the HM-QC-LDPC codes. Thanks to the distance property of Hamming codes, length four cycles are avoided from the Tanner graph of the constructed codes, resulting in codes of girth six. This approach can be further extended to construct QC-LDPC codes of girth eight. Our numerical results show that the proposal has a better cycle profile than the progressive-edge-growth (PEG) constructed codes, and consequently prevails in performance. Moreover, the constructed QC-LDPC code prevails the LDPC code of the IEEE802.22 standard by 0.2 dB at the bit error rate (BER) of 10-8 when the codeword length is within hundreds of bits, making it a promising candidate for scenarios where strict decoding latency is imposed.

## Novel types of cyclically-coupled quasi-cyclic LDPC block codes

- **Status**: ✅
- **Reason**: 바이너리 CC-QC-LDPC 신규 구성으로 girth 확대·낮은 error floor (E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7764787
- **Type**: conference
- **Published**: 12-14 Oct.
- **Authors**: Francis C. M. Lau, Fanlu Mo, Qing Lu +2
- **PDF**: https://ieeexplore.ieee.org/document/7764787
- **Abstract**: Cyclically-coupled quasi-cyclic LDPC (CC-QC-LDPC) block codes have been shown to achieve outstanding bit error performance with extremely low error floor. In this paper, we propose two new types of CC-QC-LDPC block codes which can achieve a larger girth. We present the error performance of the CC-QC-LDPC codes constructed by the new mechanism. We show that with similar codelengths, the new codes outperform the original CC-QC-LDPC codes by 0 3 to 0 35 dB at a bit error rate of 10−12.

## The design of optimized fast decoding protograph LDPC codes

- **Status**: ✅
- **Reason**: 적은 반복수 최적 프로토그래프 LDPC 신규 코드설계 (E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7764790
- **Type**: conference
- **Published**: 12-14 Oct.
- **Authors**: Thuy Van Nguyen, Hieu T. Nguyen
- **PDF**: https://ieeexplore.ieee.org/document/7764790
- **Abstract**: This paper presents a simple method of designing a protograph-based LDPC codes which has excellent performance with a small number of decoding iterations. In addition to designing LDPC codes based on the iterative decoding threshold as before, we add one more dimension into the design process which is a predefined number of decoding iterations. Simulation results show that the proposed codes have better performance than state-of-the-art protograph codes while the number of decoding iterations is small.

## Partially-stopped probabilistic min-sum algorithm for LDPC decoding

- **Status**: ✅
- **Reason**: normalized probabilistic min-sum의 partially-stopped CNU로 전력·면적 절감 - 이식 가능 디코더/HW 기법(C/D), 스토리지 명시
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7800362
- **Type**: conference
- **Published**: 11-14 Oct.
- **Authors**: Chen-Pei Song, Cheng-Hung Lin, Shu-Yen Lin
- **PDF**: https://ieeexplore.ieee.org/document/7800362
- **Abstract**: Low-density parity check (LDPC) codes have been widely applied to many storage devices because of their good error correcting performance. However, power consumption and area cost are still the major issues for their hardware implementations. Therefore, power and area reduction techniques are necessary for the implementation of check node unit (CNU) of LDPC decoder. In this paper, a novel partially stopped criterion is proposed for the normalized probabilistic min-sum algorithm to further reduce the power consumption of the check node units. The simulation result shows the proposed CNU achieves 13% power reduction with a 1.8% area overhead and an ignorable BER degradation.
