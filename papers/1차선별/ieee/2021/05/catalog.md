# IEEE Xplore — 2021-05 (1차선별 통과)


## On Nested Property of Root-LDPC Codes

- **Status**: ✅
- **Reason**: 바이너리 Root-LDPC 코드설계+불규칙 구성 design rules 제시(E), block-fading 특화이나 이식 가능성 애매하여 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9336043
- **Type**: journal
- **Published**: May 2021
- **Authors**: Lorenzo Ortega, Charly Poulliat
- **PDF**: https://ieeexplore.ieee.org/document/9336043
- **Abstract**: We investigate on binary Protograph Root-LDPC codes that can embed an interesting property, called nested property. This property refers to the ability for a coding scheme to achieve full diversity and equal coding gain for any number of received coded blocks and for any configuration of the received code blocks. One can take advantage of this property for “carousel”-type transmissions broadcasting cyclically coded information. For regular Root-LDPC codes, we show that these codes inherently have both properties over the nonergodic block fading channel and when message passing decoding is used. Then, we show that irregular Root-LDPC structures could not provide equal coding gain except if explicit design rules are enforced to ensure that the nested property is fulfilled when designing irregular Root-LDPC codes. Simulation results show that designed nested Root-LDPC codes achieve good performance and full diversity for coding rates R = 1/2, R = 1/3 and R = 1/4.

## High-Speed LDPC Decoders Towards 1 Tb/s

- **Status**: ✅
- **Reason**: full row parallel layered LDPC 디코더 멀티코어/프레임 인터리빙 HW 아키텍처 — 이식 가능 HW(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:9378807
- **Type**: journal
- **Published**: May 2021
- **Authors**: Meng Li, Veerle Derudder, Kaoutar Bertrand +2
- **PDF**: https://ieeexplore.ieee.org/document/9378807
- **Abstract**: Beyond 5G systems are expected to approach 1 Tb/s throughput. This poses a significant challenge to the channel decoder. In this paper, we propose a multi-core architecture based on full row parallel layered LDPC decoder with frame interleaving. Compared with conventional partially parallel layered architectures, the proposed architecture increases the throughput by applying frame interleaving into the pipeline architecture and by using multi-core architectures. Two high rate medium size QC LDPC codes are designed with fast decoding convergence speed for this architecture. Both codes are implemented with single core and multi-core architectures to explore different trade-offs between code design, communication performance and implementation. The four decoders are implemented in 16 nm CMOS FinFET technology with a clock rate of 1 GHz. The placement and routing implementation results show that the single core decoder for the LDPC (1027, 856) code is able to provide 114 Gb/s throughput at maximum 3 iterations with an area of 0.173 mm2 and energy efficiency of 1.56 pJ/bit; the multi-core decoder for the (1032, 860) code is able to provide 860 Gb/s throughput at maximum 2 iterations with an area of 1.48 mm2 and energy efficiency of 3.24 pJ/bit. The multi-core decoder achieves the highest throughput in the literature for medium size (1-2k) LDPC codes. When compared with other state-of-the-art fully parallel high speed architectures, the proposed architectures bring a significant gain both in area efficiency and energy efficiency while keeping the ability to offer flexibility in code rate, number of iterations and early stop.

## Quasi-Cyclic LDPC Codes With Parity-Check Matrices of Column Weight Two or More for Correcting Phased Bursts of Erasures

- **Status**: ✅
- **Reason**: 열무게 2 QC-LDPC를 phased burst erasure 정정용으로 새로 구성/globally coupling — 스토리지 erasure 코드 설계 기여(B/E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9353574
- **Type**: journal
- **Published**: May 2021
- **Authors**: Xin Xiao, Bane Vasić, Shu Lin +2
- **PDF**: https://ieeexplore.ieee.org/document/9353574
- **Abstract**: In his pioneering work on LDPC codes, Gallager dismissed codes with parity-check matrices of weight two after proving that their minimum Hamming distances grow at most logarithmically with their code lengths. In spite of their poor minimum Hamming distances, it is shown that quasi-cyclic LDPC codes with parity-check matrices of column weight two have good capability to correct phased bursts of erasures which may not be surpassed by using quasi-cyclic LDPC codes with parity-check matrices of column weight three or more. By modifying the parity-check matrices of column weight two and globally coupling them, the erasure correcting capability can be further enhanced. Quasi-cyclic LDPC codes with parity-check matrices of column weight three or more that can correct phased bursts of erasures and perform well over the AWGN channel are also considered. Examples of such codes based on Reed-Solomon and Gabidulin codes are presented.

## Error Floor Estimation of LDPC Coded Modulation Systems Using Importance Sampling

- **Status**: ✅
- **Reason**: 트래핑셋 식별 + error floor 추정(중요도 샘플링)은 바이너리 LDPC error floor 분석 기법(E)으로 NAND ECC에 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9349511
- **Type**: journal
- **Published**: May 2021
- **Authors**: Peyman Neshaastegaran, Amir H. Banihashemi, Ramy H. Gohary
- **PDF**: https://ieeexplore.ieee.org/document/9349511
- **Abstract**: One of the key weaknesses of low-density parity-check (LDPC) codes is the error floor that they typically exhibit at high signal-to-noise ratios (SNRs). Such an error floor is usually attributed to problematic structures known as trapping sets (TSs). The overwhelming majority of existing error floor estimation schemes consider the case of binary phase shift keying (BPSK) signalling. Unfortunately, these schemes are not readily extensible to estimate the error floor of high order LDPC coded modulation systems considered herein. To provide such a scheme, in this work, we use mean-shift importance sampling (MS-IS) to develop a novel error floor estimation methodology for high-order pulse amplitude modulation (PAM) and quadrature amplitude modulation (QAM) LDPC coded systems. First, a computationally efficient graphical-based approach is used to identify the TSs of a given LDPC code. Subsequently, a novel analytical approach is devised to identify the TSs that are likely to have a higher contribution in the error floor. These TSs are referred to as potentially dominant TSs (PDTSs). Finally, a new methodology for categorizing the PDTSs into equivalence classes is developed. A representative PDTS of each equivalence class is chosen and an MS-IS framework is devised to obtain the error rate corresponding to each equivalence class. To arrive at the desired MS-IS scheme, we develop an algorithm that invokes the geometry of the constellation to determine the MS value. In contrast with the conventional MS-IS method used in BPSK signalling, in the proposed MS-IS scheme, the MS value is a variable that is determined based on the TS and the transmitted codeword. The computational complexity of the three main steps of our methodology, viz. extracting the PDTSs, determining the MS values, and applying the MS-IS scheme, depends merely on the size of the constellation and the structure of the code, but not on the SNR. Numerical simulations confirm the efficacy and accuracy of the proposed technique at different SNRs.

## Spatially Coupled LDPC Codes With Sub-Block Locality

- **Status**: ✅
- **Reason**: 스토리지 동기 SC-LDPC, 서브블록 로컬리티 구성 + density evolution — 바이너리 코드 설계 기여(B/E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9354799
- **Type**: journal
- **Published**: May 2021
- **Authors**: Eshed Ram, Yuval Cassuto
- **PDF**: https://ieeexplore.ieee.org/document/9354799
- **Abstract**: A new type of spatially coupled low-density parity-check (SC-LDPC) codes motivated by practical storage applications is presented. SC-LDPCL codes (suffix `L' stands for locality) can be decoded locally at the level of sub-blocks that are much smaller than the full code block, thus offering flexible access to the coded information alongside the strong reliability of the global full-block decoding. Toward that, we propose constructions of SC-LDPCL codes that allow controlling the trade-off between local and global correction performance. In addition to local and global decoding, the paper develops a density-evolution analysis for a decoding mode we call semi-global decoding, in which the decoder has access to the requested sub-block plus a prescribed number of sub-blocks around it. SC-LDPCL codes are also studied under a channel model with variability across sub-blocks, for which decoding-performance lower bounds are derived.

## Information Bottleneck Message Passing for Military Applications

- **Status**: ✅
- **Reason**: Information Bottleneck 기반 양자화 메시지패싱으로 SPA 대체 — 이식 가능한 저정밀 LDPC 디코더 기법(C), LLR 양자화와 연관
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9486405
- **Type**: conference
- **Published**: 4-5 May 20
- **Authors**: Jan Lewandowsky, Marc Adrat, Gerhard Bauch
- **PDF**: https://ieeexplore.ieee.org/document/9486405
- **Abstract**: Military communication systems naturally have strong requirements concerning the reliability and the robustness of their physical layer data transmission schemes. Modern channel coding and modulation schemes can meet these requirements in general, but their detection and decoding at the receiving end requires complex and power demanding high-precision implementations of digital algorithms, which are often not suitable for military applications. This motivates to explore novel techniques to build simple detection and decoding algorithms with good performance. In this article, we present novel results on the recent idea of using a machine learning framework termed the Information Bottleneck method to replace demanding implementations of the sum-product algorithm with very simple quantized message passing schemes. We provide a novel explanation, which links the Information Bottleneck decoder processing to the sum-product algorithm. Moreover, we present a novel Information Bottleneck demodulation scheme for quadrature amplitude modulation and discuss special advantages of the Information Bottleneck system design approach for military applications.

## A High Throughput QC-LDPC Decoder Architecture for Near-Earth Satellite Communication

- **Status**: ✅
- **Reason**: QC-LDPC 고처리율 FPGA 디코더 아키텍처(메모리 충돌 회피, 파이프라이닝) — 이식 가능 HW 아키텍처(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:9464195
- **Type**: conference
- **Published**: 26-28 May 
- **Authors**: K. M. Sankar Nampoothiri, Kalyani N Menon, Sayed Muhsin +4
- **PDF**: https://ieeexplore.ieee.org/document/9464195
- **Abstract**: This paper presents a high throughput decoder architecture for the (8176,7154) quasi-cyclic (QC) low density parity check (LDPC) code (C2) recommended by the Consultative Committee for Space Data Systems (CCSDS) for near-earth applications. The architecture avoids memory conflict through the use of multiple shift register based memory circuits and a pipe stage forwarding mechanism, thus allowing for heavy pipelining of the core processing unit. The decoder is implemented on the Xilinx XCVU9P FPGA platform and achieves a throughput of 2.65 Gbps at 10 iterations at a clock frequency of 253 MHz.

## A Low Complexity Parallel QC-LDPC Encoder

- **Status**: ✅
- **Reason**: 저복잡도 병렬 QC-LDPC 인코더 알고리즘·FPGA 아키텍처 — 이식 가능 HW/인코딩 기법(D/E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9499562
- **Type**: conference
- **Published**: 23-26 May 
- **Authors**: Xiaoxia Yao, Lintao Li, Jihong Liu +1
- **PDF**: https://ieeexplore.ieee.org/document/9499562
- **Abstract**: In this paper, a low complexity parallel QC (quasi-cyclic)-LDPC (low-density parity-check) Codes encoding algorithm and encoder architecture is introduced. In traditional encoder architectures, the complexity of multiplication operation of information sequence and generator matrix is very high. The proposed encoding algorithm bit selection (BS) directly selects the valid information bits according to position set of non-zero elements in the first column of the sub-matrix, which avoids the operation of invalid information bits. The proposed parallel QC-LDPC encoder architectures is realized for FPGA implementation based on CCSDS (7154, 8176) LDPC codes.

## High Energy-Efficient LDPC Decoder with AVFS System for NAND Flash Memory

- **Status**: ✅
- **Reason**: NAND 플래시용 AVFS LDPC 디코더, RBER 명시 — NAND 직접(A) + HW 아키텍처(D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9401163
- **Type**: conference
- **Published**: 22-28 May 
- **Authors**: Chao Zhang, Jingtong Mo, Zihan Lian +1
- **PDF**: https://ieeexplore.ieee.org/document/9401163
- **Abstract**: In conventional Low-Density Parity-Check (LDPC) decoders, the real-time processing performance should meet its maximum decoding iterations for all packets and the work frequency or supply voltage is always fixed at a high level, which decreases its energy efficiency. In this paper, an energy- efficient LDPC decoding architecture with an adaptive voltage-frequency scaling (AVFS) scheme is presented. According to the usage of input packet FIFO related to variable decoding iterations, the architecture can dynamically adjust decoder's work frequency and supply voltage to reduce the processing energy while meeting its real-time processing requirement. Finally, the decoder is implemented with 28 nm CMOS process. Experimental results show that our decoder has a throughput of 1590 Mb/s when the raw bit error rate (RBER) of Flash memory is up to 10-2. The power consumption of the decoder can be reduced by 25%-62% and energy efficiency can be increased to 1.3-2.5 times under different AWGN noise.

## A 33.2 Gbps/Iter. Reconfigurable LDPC Decoder Fully Compliant with 5G NR Applications

- **Status**: ✅
- **Reason**: 재구성 LDPC 디코더 HW: 레이어드 NMS 파이프라인 해저드 해소·명령어 재정렬 등 이식 가능한 새 디코더/HW 기법 (C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9401329
- **Type**: conference
- **Published**: 22-28 May 
- **Authors**: Chieh-Yu Lin, Li-Wei Liu, Yen-Chin Liao +1
- **PDF**: https://ieeexplore.ieee.org/document/9401329
- **Abstract**: This paper presents a reconfigurable LDPC decoder implementation fully compliant with all the configurations in the 5G NR standard. Based on the row-based layered normalized Min-Sum (NMS) algorithm, the optimization approaches are proposed to solve the data dependency hazard in the pipeline process. The proposed instruction-level reordering diminishes the redundant latency of our pipelined decoder architecture. Moreover, the proposed data-level rescheduling optimizes the decoding sequence to remove the remaining pipeline stalls in the high- throughput design without decoding performance degradation. Evaluated in Xilinx VCU1525 FPGA, our design achieves a throughput of 6.7 Gbps per iteration. Implemented in TSMC 28nm CMOS process at the post-layout stage, a 33.2 Gbps, in one iteration, throughput can be achieved at a clock rate 556 MHz with the core area 1.97 mm2.

## Segmented Reconfigurable Cyclic Shifter for QC-LDPC Decoder

- **Status**: ✅
- **Reason**: QC-LDPC용 segmented reconfigurable cyclic shifter — 이식 가능한 permutation network HW(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:9401118
- **Type**: conference
- **Published**: 22-28 May 
- **Authors**: Hing-Mo Lam, Silin Lu, Hezi Qiu +3
- **PDF**: https://ieeexplore.ieee.org/document/9401118
- **Abstract**: In various wireless communication standards, such as Wi-Fi, WiMAX, and 5G standards, QC-LDPC decoders are required to decode a codeword of variable length. Part of the decoder is in idle if the length of codeword is not the maximum. A reconfigurable cyclic shifter is a key element of a QC-LDPC decoder. If the shifter can only shift one input at a time, the QC- LDPC decoder can only decode one codeword at a time as well. A segmented reconfigurable cyclic shifter is proposed in this paper to enable a QC-LDPC decoder to parallelly decode multiple codewords. The proposed shifter can be reconfigured into multiple segments of different sizes. Each segment can perform a cyclic shift of different shift values independently. Therefore, the proposed shifter can enhance the QC-LDPC decoder to decode multiple codewords parallelly by inputting another codeword (or codewords) to re-activate the idle hardware. The test chip of QC- LDPC decoder with the proposed segmented reconfigurable cyclic shifter has been fabricated in 0.18μ CMOS technology which can parallelly decode six codewords.

## BER Evaluation System Considering Device Characteristics of TLC and QLC NAND Flash Memories in Hybrid SSDs with Real Storage Workloads

- **Status**: ✅
- **Reason**: NAND TLC/QLC BER 평가 및 LDPC ECC 적용 결정 — A 카테고리 직접 해당
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9401203
- **Type**: conference
- **Published**: 22-28 May 
- **Authors**: Mamoru Fukuchi, Shun Suzuki, Kyosuke Maeda +2
- **PDF**: https://ieeexplore.ieee.org/document/9401203
- **Abstract**: This paper proposes BER evaluation system that evaluates BER of TLC and QLC NAND flash memories with reliability information such as write and erase (W/E) cycle and data-retention time by combining SSD model emulator and device characteristics of NAND flash memories. Proposed system decides which ECC type should be used in TLC and QLC NAND flash in SCM/TLC/QLC NAND flash tri-hybrid SSD, corresponding to various applications and memory capacity ratio. For hm_0 (write- cold application), BCH ECC is enough to correct bit errors in TLC NAND flash. On the other hand, for prxy_0 (write-hot application), LDPC ECC must be applied to TLC NAND flash in case of small SCM capacity, large W/E cycles and high BER in TLC NAND flash. In contrast, this paper concludes that QLC NAND flash needs LDPC ECC regardless of application and memory capacity.

## Performance Analysis of LDPC Decoding Algorithms for CCSDS Telecommand Space Data Link Protocol

- **Status**: ✅
- **Reason**: CCSDS LDPC 디코딩 알고리즘·4비트 양자화·스케줄링 분석 — 양자화/디코더 분석 이식 여지, 애매해 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9456163
- **Type**: conference
- **Published**: 21-23 May 
- **Authors**: P. Rajagopalan, Pradeesh Madavan, H Ramamurthy +1
- **PDF**: https://ieeexplore.ieee.org/document/9456163
- **Abstract**: This paper presents the simulation of the encoding scheme defined by CCSDS for satellite Telecommand operations and analysis of various soft decision and hard decision decoding algorithms for the same. The G(Generator), H (Parity-check) matrices are designed and verified for encoding and decoding of the message respectively. The decoding algorithms are implemented and the performances are analyzed and non-convergence of decoding algorithms, scheduling restrictions of the defined H, G matrix are explored. It is found that soft decision algorithms give 6dB coding gain and hard decision algorithms give 4 dB coding gain for the 4-bit quantized inputs.

## Joint Design of Channel Output Quantizer and LUT-Based LDPC Decoder

- **Status**: ✅
- **Reason**: 채널 출력 양자화기와 LUT 기반 LDPC 디코더 결합 설계(density evolution로 오류확률 최소화) — LLR 양자화+LUT 디코더는 NAND LDPC에 직접 이식 가능 (C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9454862
- **Type**: conference
- **Published**: 19-22 May 
- **Authors**: Chatuporn Duangthong, Pornchai Supnithi, Watid Phakphisut
- **PDF**: https://ieeexplore.ieee.org/document/9454862
- **Abstract**: Recently, the LUT-based LDPC decoder has been designed by maximizing mutual information, where the performances of channel output quantizer and LUT-based decoder are considered separately. In this work, we propose the joint design of the channel output quantizer and LUT-based decoder. Our joint design aims to minimize the error probability of LDPC decoding through the density evolution algorithm. We found that the joint design outperforms the previous work at the waterfall region.
