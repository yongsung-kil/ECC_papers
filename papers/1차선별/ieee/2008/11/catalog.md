# IEEE Xplore — 2008-11 (1차선별 통과)


## LDPC Code Design for Half-Duplex Cooperative Relay

- **Status**: ✅
- **Reason**: rate-compatible 바이너리 LDPC 코드설계+수정 가우시안근사 density evolution+미분진화 최적화로 코드설계(E) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4686837
- **Type**: journal
- **Published**: November 2
- **Authors**: Chuxiang Li, Guosen Yue, Xiaodong Wang +1
- **PDF**: https://ieeexplore.ieee.org/document/4686837
- **Abstract**: The authors consider the design of LDPC codes for cooperative relay systems in the half-duplex mode. The capacity of halfduplex relay channels has been studied previously but the design of good channel codes for such channels remains a challenging problem. Employing an efficient relay protocol, we transform the half-duplex relay code design problem into a problem of ratecompatible LDPC code design where different code segments experience different SNRs. The density evolution with conventional Gaussian approximation for single user channels, which assumes invariant SNR within one codeword, is not capable of accurately predicting the code performance for this system. Here we develop a density evolution with a modified Gaussian approximation that takes into account the SNR variation in one received codeword as well as the rate-compatibility constraint. We then optimize the code ensemble using a modified differential evolution procedure. Extensive simulations are carried out to demonstrate that the proposed algorithm offers more accurate prediction of code performance in half-duplex relay channels than the conventional methods, and the optimized codes achieve a significant gain over existing codes.

## A New Burst Detection Scheme Using Parity Check Matrix of LDPC Code for Bit Flipping Burst-like Signal Degradation

- **Status**: ✅
- **Reason**: LDPC 패리티검사행렬을 이용한 신규 버스트 검출 기법 - 떼어낼 수 있는 BP/디코딩 보조 기법(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4717796
- **Type**: journal
- **Published**: Nov. 2008
- **Authors**: Yasuaki Nakamura, Mitsuhiro Nishimura, Yoshihiro Okamoto +2
- **PDF**: https://ieeexplore.ieee.org/document/4717796
- **Abstract**: In this paper, a new burst detection method using the check matrix of low-density parity-check (LDPC) code is proposed. The burst detection for the bit flipping burst-like signal degradation which the conventional burst detection using a reproducing waveform, an equalizer output, an a posteriori probability (APP) decoder output and so on cannot detect is studied. The performance of the LDPC coding and iterative decoding system with the proposed burst detector is evaluated by computer simulation for a perpendicular magnetic recording channel with bit flipping burst-like signal degradation, and it is compared with that of the RS encoding and decoding system using the erasure correction. The results show that the LDPC coding and iterative decoding system with our burst detector shows the better performance and has the resistance to the bit flipping burst-like signal degradation of about 1500 bits.

## Fully Parallel Stochastic LDPC Decoders

- **Status**: ✅
- **Reason**: fully parallel stochastic 바이너리 LDPC 디코더 FPGA 아키텍처로 디코더(C)+HW(D) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4602535
- **Type**: journal
- **Published**: Nov. 2008
- **Authors**: Saeed Sharifi Tehrani, Shie Mannor, Warren J. Gross
- **PDF**: https://ieeexplore.ieee.org/document/4602535
- **Abstract**: Stochastic decoding is a new approach to iterative decoding on graphs. This paper presents a hardware architecture for fully parallel stochastic low-density parity-check (LDPC) decoders. To obtain the characteristics of the proposed architecture, we apply this architecture to decode an irregular state-of-the-art (1056,528) LDPC code on a Xilinx Virtex-4 LX200 field-programmable gate-array (FPGA) device. The implemented decoder achieves a clock frequency of 222 MHz and a throughput of about 1.66 Gb/s at  $E_{b}/N_{0}={\hbox {4.25~dB}}$ (a bit error rate of $10^{-8}$). It provides decoding performance within 0.5 and 0.25 dB of the floating-point sum-product algorithm with 32 and 16 iterations, respectively, and similar error-floor behavior. The decoder uses less than 40% of the lookup tables, flip-flops, and IO ports available on the FPGA device. The results provided in this paper validate the potential of stochastic LDPC decoding as a practical and competitive fully parallel decoding approach.

## Average Stopping Set Weight Distributions of Redundant Random Ensembles

- **Status**: ✅
- **Reason**: redundant random ensemble의 stopping set 분포 분석으로 BEC BP 성능과 error floor 관련 바이너리 LDPC 코드설계(E) 통찰 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4655474
- **Type**: journal
- **Published**: Nov. 2008
- **Authors**: Tadashi Wadayama
- **PDF**: https://ieeexplore.ieee.org/document/4655474
- **Abstract**: In this paper, redundant random ensembles are defined and their average stopping set (SS) weight distributions are analyzed. A redundant random ensemble consists of a set of binary matrices with linearly dependent rows. These linearly dependent rows significantly reduce the number of stopping sets (SS) of small size. Upper and lower bounds on the average SS weight distribution of the redundant random ensembles are proved based on a combinatorial argument. Asymptotic forms of these bounds reveal asymptotic behavior of the average SS weight distributions. From these bounds, a tradeoff between the number of redundant rows (corresponding to decoding complexity of belief propagation on binary erasure channel) and the average SS weight distribution (corresponding to decoding performance) can be derived.

## A reconfigurable FPGA implementation of an LDPC decoder for unstructured codes

- **Status**: ✅
- **Reason**: D/C: FPGA LDPC 디코더 HW + min-sum with correction factor 변형, NAND 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4746952
- **Type**: conference
- **Published**: 7-9 Nov. 2
- **Authors**: S. M. Ehsan Hosseini, Kheong Sann Chan, Wang Ling Goh
- **PDF**: https://ieeexplore.ieee.org/document/4746952
- **Abstract**: This paper describes the implementation of a general and embedded decoder for the evaluation of unstructured low-density parity-check (LDPC) codes over additive-white Gaussian noise (AWGN) channels. The decoder, which has a serial architecture and moderate throughput, is a peripheral connected to the embedded Power PC processor of a Xilinx Virtex-II Pro FPGA and is managed by the processor. This method of hardware/software implementation provides the maximum flexibility for the development and rapid prototyping of the hardware-based simulator system. The decoding algorithm proposed in this paper belongs to the class of min-sum with correction factor in which the correction factor updates with the log-likelihood ratio (LLR) values.

## A 7.39mm2 76mW (1944, 972) LDPC decoder chip for IEEE 802.11n applications

- **Status**: ✅
- **Reason**: QC-LDPC 디코더 칩의 Group Comparison·Dynamic Wordlength·Data Packet 기법으로 면적·처리량 개선 — 이식 가능 HW(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:4708787
- **Type**: conference
- **Published**: 3-5 Nov. 2
- **Authors**: Xin-Yu Shih, Cheng-Zhou Zhan, An-Yeu Wu
- **PDF**: https://ieeexplore.ieee.org/document/4708787
- **Abstract**: This paper presents the LDPC decoder chip for (1944,972) QC-LDPC codes in IEEE 802.11n communication system. The efficient LDPC decoder chip is designed with three design techniques, including Group Comparison (GC), Dynamic Wordlength Assignment (DWA), and Data Packet Scheme (DPS). When the target BER is 10−6, the decoding performance can be improved by the coding gain of 0.48 dB and 0.63 dB with respect to (4,3) and (3,2) fixed-point NMSA, respectively. In addition, the total decoder design area can be reduced by 25% and the decoding throughput can be enhanced by 3X times with respect to conventional direct-mapping method. By using TSMC 0.13um VLSI technology, the core area and die size are only 3.88 mm2 and 7.39 mm2, respectively. The maximum operating frequency is measured at 111.1MHz and the power dissipation is only 76 mW.

## Low complexity iterative decoding algorithm for low-density parity-check (LDPC) codes

- **Status**: ✅
- **Reason**: RRWBF 비트플립 변형(반복수 절감) - 이식 가능 디코더 알고리즘(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4812877
- **Type**: conference
- **Published**: 24-27 Nov.
- **Authors**: Hany R. Zeidan, Maha M. Elsabrouty
- **PDF**: https://ieeexplore.ieee.org/document/4812877
- **Abstract**: The reliability ratio weighted based bit-flipping (RRWBF) algorithm for decoding low-density parity-check (LDPC) codes has recently been developed to provide the best performance among all existing bit-flipping based algorithms. The implementation efficient reliability ratio weighted based bit-flipping (IERRWBF) algorithm speedup the original algorithm to decrease the processing time used. A drawback for this algorithm is the decrease in the improvement as the maximum number of iterations assigned for the algorithm increase as a large percentage of decoding time is spent on the iteration part without any change in the performance. In this paper, a modified version for this algorithm is proposed to solve this drawback by reducing the number of iterations required to achieve the same performance of the existing IERRWBF algorithm using efficient number of iterations instead of using the maximum number of iterations for decoding without any change in the performance of the IERRWBF.

## Decoding architectures for Projective Geometry based LDPC codes

- **Status**: ✅
- **Reason**: PG-LDPC 병렬/반병렬 디코더 아키텍처(BP+MLD 재구성) - HW 아키텍처(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:4812880
- **Type**: conference
- **Published**: 24-27 Nov.
- **Authors**: S.G Harihara, M. Girish Chandra, Tarakapraveen Uppalapati +1
- **PDF**: https://ieeexplore.ieee.org/document/4812880
- **Abstract**: Projective Geometry (PG) based Low Density Parity Check (LDPC) codes have many useful properties, including easy encoding and decoding by simple majority logic technique. With these useful features, they can be useful error control codes in future. In this paper, we present three novel architectures comprising of one parallel and two semi-parallel decoder architectures for popular PG-based LDPC codes. These architectures have no memory clash and further are reconfigurable for different lengths (and their corresponding rates). The three architectures can be configured either for the regular belief propagation based decoding or majority logic decoding (MLD).

## New sum-product algorithm using approximation method for low complexity LDPC decoding

- **Status**: ✅
- **Reason**: C: sum-product 근사(곱셈→덧셈, 양자화 테이블)로 저복잡도 LDPC 디코더 기법 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4815676
- **Type**: conference
- **Published**: 24-25 Nov.
- **Authors**: Jae Hee Han, Myung Hoon Sunwoo
- **PDF**: https://ieeexplore.ieee.org/document/4815676
- **Abstract**: This paper proposes a new sum-product algorithm to improve BER performance for low-density parity-check codes. The proposed algorithm can replace multiplications and divisions with additions and subtractions by adding the logarithmic and exponential functions. In addition, the proposed algorithm can simplify both the ln[tanh(x)] and tanh-1[exp(x)] functions by using two quantization tables which can reduce tremendous computational complexity. Moreover, the simulation results show that the proposed SP algorithm can improve maximum of 0.8 dB BER performance compared with the existing modified sumproduct algorithm.

## Compressing construction of QC-LDPC codes

- **Status**: ✅
- **Reason**: QC-LDPC 압축 구성법(recursive/single-compressing), high girth 유지 — 코드 설계(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4737397
- **Type**: conference
- **Published**: 19-21 Nov.
- **Authors**: Shuqi Sun, Wuyang Zhou
- **PDF**: https://ieeexplore.ieee.org/document/4737397
- **Abstract**: Two compressing construction methods of Quasi-Cyclic LDPC (QC-LDPC) codes are proposed, which can be called recursive-compressing and single-compressing respectively. Selecting a good QC-LDPC code as the Mother, the son codes constructed through the compressing methods are still good codes, i.e., have high girth and few short cycles, moreover, they have continuous code length and require smaller memory space. Analysis and simulation results show they can perform well over the AWGN channel.

## Good encodable irregular quasi-cyclic LDPC codes

- **Status**: ✅
- **Reason**: 바이너리 irregular QC-LDPC 구성, girth/최소거리 동시 보존 신규 구성법 — 코드 설계(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4737391
- **Type**: conference
- **Published**: 19-21 Nov.
- **Authors**: Yang Xiao, Kiseon Kim
- **PDF**: https://ieeexplore.ieee.org/document/4737391
- **Abstract**: The existing encodable irregular LDPC codes may have a degraded BER performance when it is derived from classical regular QC LDPC codes since both girth property and weight property are not carefully given attention to two or more thing, which lead to some codes with large girths have small minimum weights and poor BER performance. To solve the problem, we propose a new approach to construct the encodable irregular QC codes, which can not produce new short girths and can keep the large minimum weight and minimum distance of the codes. The theorems of girth 4 and girth 6 are provided to test the girth variance of the obtained irregular QC codes. Simulations verify the construction of the QC LDPC codes to be valid, since better BER performance than that of existing encodable irregular LDPC codes is obtained.

## The analysis of cycle structure for a class of quasi-cyclic LDPC codes

- **Status**: ✅
- **Reason**: QC-LDPC 사이클 구조 분석 및 분류로 구성 알고리즘 개선 — 코드 설계(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4737394
- **Type**: conference
- **Published**: 19-21 Nov.
- **Authors**: Jing Lei, Jianhui Wang, Yongqiang Gao
- **PDF**: https://ieeexplore.ieee.org/document/4737394
- **Abstract**: In this paper, we analyse the cycle structure of a class of quasi-cyclic LDPC codes, and divide the cycles of this kind of LDPC codes into three classes. It offers some help for improving the existing construction algorithms of this kind of LDPC codes. The cycles in base matrix could be extended as long as possible when p the row¿s(or column¿s) number of block-elements was prime.

## Improved performance irregular quasi-cyclic LDPC code design from BIBD’s using threshold minimization

- **Status**: ✅
- **Reason**: BIBD 기반 irregular QC-LDPC 신규 설계 + density evolution threshold 최소화, 바이너리 코드설계 기법 이식 가능(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4766569
- **Type**: conference
- **Published**: 19-21 Nov.
- **Authors**: Siddarama R. Patil, Sant S. Pathak
- **PDF**: https://ieeexplore.ieee.org/document/4766569
- **Abstract**: In this paper we propose a novel method for designing irregular quasi-cyclic low-density parity-check (LDPC) codes from Balanced Incomplete Block Designs (BIBDpsilas). The design method hinges around finding the optimum degree profile by minimizing the threshold using density evolution. The approach for designing short block length codes is robust for practical implementation and has been found to exhibit considerable performance gain that may be attributed to a good degree profile for the codes. The design takes into consideration the code rate and code length as variable parameters. The simulation results for the designed codes are compared with regular and irregular quasi-cyclic BIBD based LDPC codes and found a relatively higher performance in terms of BER.

## Flexible low-complexity decoding architecture for QC-LDPC codes

- **Status**: ✅
- **Reason**: QC-LDPC 유연 저복잡도 디코딩 아키텍처, 신규 time-sharing 스킴 — HW(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:4737396
- **Type**: conference
- **Published**: 19-21 Nov.
- **Authors**: Nan Jiang, Kewu Peng, Zhixing Yang
- **PDF**: https://ieeexplore.ieee.org/document/4737396
- **Abstract**: A novel flexible decoding architecture for quasi-cyclic (QC) low-density parity-check (LDPC) code is proposed in this paper to reduce decoding complexity. The novelty of this architecture lies in a new time-sharing scheme of processing units, which provides low complexity and flexible serial factor of decoding hardware. Without loss of coding performance, the architecture requires significantly less processing units compared with known semi-parallel decoders at the expense of throughput decrease, while keeping memory requirement unchanged. As demonstrated by hardware and software implementation results, the proposed architecture is advisable and competent for wireless mobile systems and portable devices.

## Comparison of decoding turbo Gallager codes in hybrid decoding arrangements with different iterative decoders over the erasure channel

- **Status**: ✅
- **Reason**: turbo Gallager(LDPC계) 반복 디코더 비교, erasure 채널 BP vs BCJR-LUT+ML 하이브리드 디코더 — 디코더 기법 이식 가능성, Phase3 재검토
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4737183
- **Type**: conference
- **Published**: 19-21 Nov.
- **Authors**: Li Yang, Marcel Ambroze, Martin Tomlinson
- **PDF**: https://ieeexplore.ieee.org/document/4737183
- **Abstract**: In this paper, different iterative decoders for turbo Gallager codes are optimised and compared for the binary erasure channel. The complexity and performance differences between turbo decoder, BCJR-based Look-Up Table decoder and belief propagation decoder are analysed and evaluated. A hybrid decoding arrangement, which uses an iterative decoder followed by a maximum likelihood ¿In-Place¿ matrix inversion algorithm, is compared for the different iterative decoders. Results are presented which show that the BCJR-based iterative decoders achieve better performance than using the belief propagation decoder for turbo Gallager codes in the erasure channel. When small encoder memory is selected, the optimised Look-Up Table decoder provides a good balance between convergence performance and complexity.

## An efficient early stopping scheme for LDPC decoding based on check-node messages

- **Status**: ✅
- **Reason**: 체크노드 LLR 기반 LDPC 조기정지 기법 — 이식 가능 디코더 알고리즘(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4737398
- **Type**: conference
- **Published**: 19-21 Nov.
- **Authors**: Z. H. Cai, J. Hao, L. Wang
- **PDF**: https://ieeexplore.ieee.org/document/4737398
- **Abstract**: An efficient early stopping method is proposed in this paper to reduce the average number of iterations for low density parity check (LDPC) decoders. The method is very efficient especially when the channel signal-to-noise ratio (SNR) is low. It is based on the estimation of the log-likelihood ratio (LLR) messages of the check nodes.

## Soft-quantized demodulation for BPSK over discrete-time memoryless fading channel

- **Status**: ✅
- **Reason**: BPSK 균일 소프트 양자화의 채널용량 기준 최적 양자기 설계 — LLR 양자화 기법 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4737307
- **Type**: conference
- **Published**: 19-21 Nov.
- **Authors**: Qiuliang Xie, Kewu Peng, Jian Song +2
- **PDF**: https://ieeexplore.ieee.org/document/4737307
- **Abstract**: The demapping method that simply multiplies the received symbols with channel state information (CSI) coefficients is proved optimal in this paper for any BPSK modulated discrete-time memoryless fading channel (DMFC) from the viewpoint of channel capacity, when CSI is available at the receiver. A generic method to calculate the channel capacity of BPSK modulated DMFC subjected to uniform soft quantization is proposed, which offers a powerful criterion for optimal quantizer design. Numeric results of the Rayleigh fading case are presented, showing that 6-bit uniform quantization offers effective demodulation compared with unquantized demodulation, losing less than 0.1 dB for both with and without CSI cases.

## Bounded angle iterative decoding of LDPC codes

- **Status**: ✅
- **Reason**: BA-I 디코딩: 반복 디코더 구조에 추가 조건으로 undetected error rate 감소시키는 신규 BP 변형, C 카테고리 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4753226
- **Type**: conference
- **Published**: 16-19 Nov.
- **Authors**: Sam Dolinar, Kenneth Andrews, Fabrizio Pollara +1
- **PDF**: https://ieeexplore.ieee.org/document/4753226
- **Abstract**: A modification to the usual iterative decoding algorithm for LDPC codes, called bounded angle iterative (BA-I) decoding, is introduced. The modified decoder erases codewords detected during iterations that fall outside a maximum decoding angle with respect to the received observation. The new algorithm is applicable in scenarios that demand a very low undetected error rate but require short LDPC codes that are too vulnerable to undetected errors when the usual iterative decoding algorithm is used. BA-I decoding provides a means of reducing the maximum undetected error rate for short LDPC codes significantly, by incorporating a simple extra condition into the iterative decoder structure without redesigning the code. The reduction in undetected error rate comes at a price of increasing the threshold signal-to-noise ratio (SNR) required for achieving a good overall error rate, but this increase in channel threshold can be minimized by allowing the decoderpsilas maximum decoding angle to vary with SNR.

## Performance under delay constraints on iterative decoding of LDPC codes

- **Status**: ✅
- **Reason**: QC-LDPC 지연제약 하 SPA vs TDMP 메시지패싱 디코딩 비교 — 이식 가능 디코더 알고리즘(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4753232
- **Type**: conference
- **Published**: 16-19 Nov.
- **Authors**: JaWone Kennedy, Daniel L. Noneaker
- **PDF**: https://ieeexplore.ieee.org/document/4753232
- **Abstract**: The performance of a system with a quasi-cyclic low-density parity-check code is examined under various constraints on the decoding delay. Two alternatives are considered for the message-passing decoding algorithm: the sum-product algorithm and the turbo-decoding message-passing algorithm. It is shown that their relative performance depends heavily on the stringency of the delay constraint; the TDMP algorithm results in substantially better performance than the SPA if the constraint is stringent.

## Error floor analysis for an ensemble of easily implementable irregular (2048, 1024) LDPC codes

- **Status**: ✅
- **Reason**: 바이너리 (2048,1024) 불규칙 LDPC 코드 설계 + error floor/저오류영역 성능 분석 — 이식 가능 코드설계(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4753229
- **Type**: conference
- **Published**: 16-19 Nov.
- **Authors**: Chad A. Cole
- **PDF**: https://ieeexplore.ieee.org/document/4753229
- **Abstract**: The following paper describes a design process for constructing semirandom LDPC codes with characteristics that are suitable for a relatively simple implementation for both the encoding and decoding operation. The paper will focus on two particular code ensembles - both rate-1/2 (2048, 1024) designs with a specified irregular degree distribution. These code parameters were chosen simply because they satisfied a project design constraint, but the process described can be extended to most other low-density designs. Some new insights into the codepsilas performance curve behavior in the low error region under message passing decoding are presented.

## Efficient quantization schemes for LDPC decoders

- **Status**: ✅
- **Reason**: LDPC 디코더 고정소수점 양자화 기법(3/4/5비트) + sum-product 구현/density evolution — 이식 가능 디코더/HW(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4753231
- **Type**: conference
- **Published**: 16-19 Nov.
- **Authors**: Radivoje Zarubica, Ryan Hinton, Stephen G. Wilson +1
- **PDF**: https://ieeexplore.ieee.org/document/4753231
- **Abstract**: LDPC codes have attracted much attention recently for their near-capacity performance and high throughput owing to parallel decoding architectures. While simulations are normally done with floating point computation, any practical implementation (ASIC or FPGA) will be built with fixed-point computation. Obviously, decoder speed will increase, and resource requirements will drop, with low-precision implementations, say 3,4, or 5-bit architectures. In this paper we study the effects of quantization in this regime, using density evolution and decoder simulation. Detailed sum-product decoder implementations are given, and performance losses relative to floating point decoding are given. In particular, 4-bit decoder architectures sustain only 0.1 dB penalty.
