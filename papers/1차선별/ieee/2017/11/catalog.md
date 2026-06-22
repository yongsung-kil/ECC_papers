# IEEE Xplore — 2017-11 (1차선별 통과)


## A Detector-Aware LDPC Code Optimization for Ultra-High Density Magnetic Recording Channels

- **Status**: ✅
- **Reason**: detector-aware QC-LDPC 최적화 및 protograph 병렬 디코더 구성으로 error floor 개선, E 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7919248
- **Type**: journal
- **Published**: Nov. 2017
- **Authors**: Lingjun Kong, Kui Cai, Pingping Chen +1
- **PDF**: https://ieeexplore.ieee.org/document/7919248
- **Abstract**: In this paper, a detector-aware low-density parity-check (LDPC) code optimization algorithm is proposed for the ultra-high density magnetic recording channel, such as bit-patterned magnetic recording and two-dimensional magnetic recording, where a 2-D detector (2D-DET) is employed to combat 2-D intersymbol interference (2D-ISI) effects, by acquiring the variance of the 2D-ISI channel log-likelihood ratios corresponding to the specific 2D-DET. The new parameter builds a bridge of LDPC code optimization between the ISI-channel and the additive white Gaussian noise channel. Numerical results show that our proposed algorithms are more efficient in running time than other recently proposed optimization algorithms. Moreover, the protograph-based quasi-cyclic (QC) codes using the proposed optimization strategy, which have a low-complexity QC encoder structure with an effectual parallelizable protograph decoder composition, enjoy up to one order of magnitude performance gain in bit error rate over the other random codes that suffer from high error floors.

## Iterative Channel Detection With LDPC Product Code for Bit-Patterned Media Recording

- **Status**: ✅
- **Reason**: LDPC product code 반복 채널검출 디코딩 기법, 바이너리 LDPC BP에 이식 가능성 있어 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7907319
- **Type**: journal
- **Published**: Nov. 2017
- **Authors**: Seongkwon Jeong, Jaejin Lee
- **PDF**: https://ieeexplore.ieee.org/document/7907319
- **Abstract**: Because of the explosion in data growth, the requirement for high-density storage systems has increased. Bit-patterned media recording (BPMR) is a candidate for the next-generation magnetic recording systems, and its many advantages facilitate the achievement of recording densities of 1 Tb/in2 and beyond. In BPMR, each information bit is represented by a magnetic island; however, due to the small spacings between the along- and across-track islands that are for the achievement of a high areal density, severe extents of the inter-symbol interference and inter-track interference appear. These error factors degrade the system performance of the recording system. In this paper, an iterative channel detection scheme with a low-density parity check (LDPC) product code for which the extrinsic information between the soft output Viterbi algorithm and the LDPC product code is used for the BPMR is proposed. For the improvement of the BPMR performance, the modified extrinsic information data are exploited.

## Design of LDPC Codes for Unequal ISI Channels

- **Status**: ✅
- **Reason**: 불균등 채널용 irregular LDPC 코드 설계(EXIT chart 기반 구성)로 E 코드설계 기법 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7918545
- **Type**: journal
- **Published**: Nov. 2017
- **Authors**: Watid Phakphisut, Pornchai Supnithi
- **PDF**: https://ieeexplore.ieee.org/document/7918545
- **Abstract**: In this paper, we design an irregular low-density parity-check (LDPC) codes for unequal inter-symbol interference channels based on the modified extrinsic information transfer chart. During transmission, each LDPC codeword will be divided and transmitted to the different channels. The aim of this scheme is to avoid transmitting the whole codeword in a high error rate channel. The simulation results show that the proposed code optimized for both PR! and PR2 channels can achieve a 0.2 coding gain over the codes designed specifically for each individual channel. When this simple code is applied to a perpendicular channel with these two targets, the coding gains of the proposed code is about 0.08 dB at the frame error rate of 10-3.

## Dynamic Scheduling Decoding of LDPC Codes Based on Tabu Search

- **Status**: ✅
- **Reason**: Tabu search 기반 동적 스케줄링 LDPC 디코딩(TSDS) - 부호 비의존 BP 스케줄링 개선으로 바이너리 LDPC에 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7995043
- **Type**: journal
- **Published**: Nov. 2017
- **Authors**: Xingcheng Liu, Chunlei Fan, Xuechen Chen
- **PDF**: https://ieeexplore.ieee.org/document/7995043
- **Abstract**: The informed dynamic scheduling (IDS) strategy decoding algorithms performed exceptionally well for low-density parity-check codes in terms of the error-rate performance. However, the IDS decoding algorithm is greedy because of the unfair computation resources allocation among different variables nodes, which leads to poor convergence performance. In order to reduce the greediness of the IDS algorithm, the tabu search (TS) algorithm is introduced to the dynamic scheduling-based decoding in this paper. In the TS-based dynamic scheduling (TSDS) algorithm, the variable nodes in the Tanner graph are temporarily stored in a tabu list. In the decoding process with the TSDS algorithm, variable nodes stored in the tabu list will not be selected and updated until they are shifted out of the tabu list. Besides, an improved updating order is provided for the TSDS algorithm, by which the computational complexity can be decreased without the loss of error correction performance. Simulation results show that the proposed algorithm outperforms other decoding algorithms of interest in terms of bit error rate and convergence performance over the additive white Gaussian noise channel.

## Reliability-Oriented Decoding Strategy for LDPC Codes-Based D-JSCC System

- **Status**: ✅
- **Reason**: 신뢰도 기반 LDPC 디코딩 전략(RODS), LLR 부호·진동 기반 노드 신뢰도 평가 - JSCC 베이스라인이나 떼어낼 수 있는 BP 메시지 억제 기법(C), 애매하여 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8016398
- **Type**: journal
- **Published**: Nov. 2017
- **Authors**: Yibo Lyu, Shaohua Hong, Lin Wang +1
- **PDF**: https://ieeexplore.ieee.org/document/8016398
- **Abstract**: In this letter, a reliability oriented decoding strategy (RODS) for low density parity check codes-based distributed joint source and channel coding system is proposed. During each local decoding iteration, the reliability of each variable node is evaluated based on the sign of received log-likelihood ratios (LLRs) and its oscillation situation. Then, by employing reliability-oriented updating operation, the negative influence of those inaccurate messages is suppressed. Moreover, extra operations are performed on a group of most unreliable source nodes so that more accurate posteriori LLRs can be obtained. During global iteration, offset operation is performed to reduce error propagation. The simulation results illustrate that the proposed RODS outperforms other decoding algorithms at the aspects of error correction performance and convergence speed, especially when the correlation between distributed sources is low.

## Accumulate Repeat Accumulate Check Accumulate Codes

- **Status**: ✅
- **Reason**: 새 프로토그래프 LDPC 부호족(ARACA) 설계 - 바이너리 LDPC 코드설계 기법(E), LMDG·임계값·효율적 인코더 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7973156
- **Type**: journal
- **Published**: Nov. 2017
- **Authors**: Ki Jun Jeon, Kwang Soon Kim
- **PDF**: https://ieeexplore.ieee.org/document/7973156
- **Abstract**: In this paper, a novel accumulate-repeat-accumulate-check-accumulate (ARACA) code is proposed as a subclass of protograph-based low-density parity-check (LDPC) codes. The key feature of the proposed ARACA code is represented by the outer connection doping in the protograph. This feature can provide the linear minimum distance growth (LMDG) property at a good iterative decoding threshold while maintaining an efficient encoder structure. The effect of the outer connection doping on the typical minimum distance, the iterative decoding threshold, and the LMDG property is discussed and analyzed by comparing case examples and using the asymptotic protograph ensemble weight enumerator. Some good ARACA code protographs are provided for a wide range of code rates. In addition, an efficient and universal encoding procedure and the corresponding encoder structure are provided for them. The performance of the proposed ARACA code is evaluated and compared with well-known good LDPC codes. The simulation results confirm the superiority of the proposed ARACA codes in terms of encoding complexity and frame error rate performance, especially at low-rates in an ultra-reliable regime.

## LDPC coded modulation for TLC flash memory

- **Status**: ✅
- **Reason**: TLC NAND 플래시용 sparse LDPC coded modulation, IDD+인터리버로 error floor 저감 - NAND 직접(A)+디코더(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8278036
- **Type**: conference
- **Published**: 6-10 Nov. 
- **Authors**: Huang-Chang Lee, Jieng-Heng Shy, Yen-Ming Chen +1
- **PDF**: https://ieeexplore.ieee.org/document/8278036
- **Abstract**: In this paper, a coded modulation scheme using extremely sparse low-density parity-check (LDPC) codes is proposed for the stored signal of triple-level-cell (TLC) NAND flash, where both the encoding and the decoding complexity can be significantly reduced with the advantage of the extremely sparse code graph. In order to enhance the performance of decoder, iterative detection decoding (IDD) is introduced to extract the extrinsic information from the symbol detector, and the cooperative non-Gray mapping is also designed. In addition, for error floor lowering, an interleaver is inserted to ensure the cascaded degree-2 variable nodes are separated to individual symbols. The simulation results show that the proposed coded modulation scheme can provide a practical error floor performance with a low decoding complexity.

## Spatially-coupled LDPC codes for two dimensional erasure channel

- **Status**: ✅
- **Reason**: 2D array erasure 채널용 SC-LDPC 신규 구성+density evolution - 바이너리 SC-LDPC 코드설계(E) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8277987
- **Type**: conference
- **Published**: 6-10 Nov. 
- **Authors**: Gou Hosoya, Hiroyuki Yashima
- **PDF**: https://ieeexplore.ieee.org/document/8277987
- **Abstract**: In this study, we developed spatially coupled LDPC (SC-LDPC) codes on the two-dimensional array erasure (2DAE) channel. We propose a method of generating new SC-LDPC codes with the restriction on the check node constraint. We evaluate by density evolution analysis that the improvement of the threshold for the proposed two-dimensional SC-LDPC codes over the one-dimensional SC-LDPC codes. Moreover we verify that the BP threshold of the proposed codes can approach the corresponding maximum a posteriori (MAP) threshold of the original residual graph on the 2DAE channel.

## Lowering the error floors of low-density parity-check codes with additional check nodes

- **Status**: ✅
- **Reason**: 추가 체크노드로 trapping set 완화해 error floor 저감 — 부호 비의존 코드설계 기법(E), 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8277936
- **Type**: conference
- **Published**: 6-10 Nov. 
- **Authors**: Dongming Yuan, Lu Li, Yuanan Liu
- **PDF**: https://ieeexplore.ieee.org/document/8277936
- **Abstract**: This paper proposes a novel scheme for bit recovery of Low-Density Parity-Check (LDPC) Codes. Firstly, the most erroneous and the most reliable bits are located by searching the codeword bits. Subsequently, new check nodes are added to connect them, thus the negative effects of the most erroneous bits along with the corresponding trapping sets are avoided. Eventually, the BER performance is dramatically improved in the error-floor region according to the simulated results. This idea could be a more concise and simple alternative to weaken the effects of trapping sets in LDPC applications.

## Improved sliding window decoding of spatially coupled low-density parity-check codes

- **Status**: ✅
- **Reason**: SC-LDPC 개선 슬라이딩윈도우 디코딩(ISWD) — 부호 비의존 BP 디코더 개선 기법(C/E), 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8277945
- **Type**: conference
- **Published**: 6-10 Nov. 
- **Authors**: Shiyuan Mo, Li Chen
- **PDF**: https://ieeexplore.ieee.org/document/8277945
- **Abstract**: Spatially coupled low-density parity-check (SC-LDPC) codes can achieve capacity approaching performance with a small message recovery latency due to the sliding window decoding (SWD). Using a partial Tanner graph, the SWD performs iterative message passing until the average error probability Pe of the target symbols falls below a threshold or the maximum iteration number is reached. However, Pe does not decrease monotonically as iteration progresses. This implies the symbol likelihoods that were yielded when the decoding terminates may not be optimal for making decisions. Therefore, this paper proposes an improved SWD (ISWD) for SC-LDPC codes. The proposal monitors the achievable minimum of Pe and stores its associated likelihoods, so that when the decoding terminates the target symbols will be estimated based on the stored likelihoods. Our research shows the ISWD is able to enhance the decoding performance, especially in the waterfall region. It exhibits an asymptotic convergence to the SWD performance. A complexity reducing variant of the ISWD is also proposed to facilitate the decoding but at the cost of error-correction performance.

## On practical LDPC code construction for NAND flash applications

- **Status**: ✅
- **Reason**: 3D NAND 플래시 LDPC 코드 구성, error floor·trapping set·사이클 회피 — NAND 직접(A)+코드설계(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8277929
- **Type**: conference
- **Published**: 6-10 Nov. 
- **Authors**: Shiuan-Hao Kuo, Zhen-U Liu, Jeff Yang
- **PDF**: https://ieeexplore.ieee.org/document/8277929
- **Abstract**: As increasing storage density accompanies increasing adoption of 3D NAND flash, the data integrity turns to more important. The error floor problem is known to have critical impact on the correction capability of LDPC code in NAND flash storage. Herein we propose an analytical method based on a simplified NAND flash error model to relate harmful trapping sets to small cycles, by which we can avoid certain cycle combination during code construction for NAND flash memory applications.

## Analysis of practical LDPC decoders in tanner graphs with absorbing sets

- **Status**: ✅
- **Reason**: absorbing set이 유발하는 LDPC error floor를 min-sum/scaled-MS 디코더 관점에서 분석하는 알고리즘 - 디코더(C)/error floor(E) 직접 이식
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8277973
- **Type**: conference
- **Published**: 6-10 Nov. 
- **Authors**: Marco Ferrari, Alessandro Tomasoni, Sandro Bellini
- **PDF**: https://ieeexplore.ieee.org/document/8277973
- **Abstract**: Absorbing sets (ASs) cause the error floor phenomenon in many Low-Density Parity-Check (LDPC) codes. A recent, simplified system model for Min-Sum (MS) LDPC decoding [1] predicts that ASs exhibit a threshold behavior: if all variable nodes in an AS have channel messages above the threshold, the AS cannot trap the decoder. The threshold is a real-valued parameter that depends on the topology of the AS, and can be evaluated by a nonlinear optimization. In this paper we describe a simple, fast algorithm for evaluating the AS threshold. Additionally, we show that the algorithm is valid also for scaled-MS decoding. We show with an example that the threshold values under scaled-MS decoding are smaller than under MS decoding. Accordingly, scaling decreases the error floor.

## LDPC turbo decoder using generalized belief propagation over two-dimensional inter-symbol interference channel

- **Status**: ✅
- **Reason**: GBP 기반 검출+복호 joint, region graph 수렴조건 및 구성법 제시 - 일반화 BP 디코더(C) 기법 이식 가능, NAND ISI성 채널에도 유효
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8277988
- **Type**: conference
- **Published**: 6-10 Nov. 
- **Authors**: Kenta Kasai, Akiyoshi Hashimoto
- **PDF**: https://ieeexplore.ieee.org/document/8277988
- **Abstract**: Due to many small cycles in factor graphs, detection and decoding over two-dimensional inter-symbol interference (2D-ISI) channels has been considered difficult. It is reported that generalized belief propagation (GBP) detection for 2D-ISI performs much better than BP. However, conventional studies for GBP for 2D-ISI were restricted to the separate uses of detection and decoding. Joint usage of detection and decoding were proposed in [1] but hard-decisions are inserted between detector and decoder. This makes a gap to the optimal performance. In this paper, we study full-joint use of GBP for detector and decoder for 2D-ISI, i.e., we use only soft-messages. Furthermore, we clarify a necessary condition with respect to the region graph that messages converge to a GBP fixed point. We found most of regions graph proposed in the literature do not satisfy the convergence condition. This prevents the full-joint use of GBP for 2D-ISI. Moreover, we propose a method to construct region graphs which satisfy the condition. Numerical experiments show that the proposed joint detector and decoder perform better than the conventional separate detector and decoder [2] in a simple 2D-ISI channels.

## Syndrome-coupled rate-compatible error-correcting codes

- **Status**: ✅
- **Reason**: 코셋/신드롬 기반 rate-compatible ECC 구성 프레임워크 - 바이너리 nested 선형코드 기반 코드설계(E) 이식 가능, NAND rate-compatible에 유용
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8277969
- **Type**: conference
- **Published**: 6-10 Nov. 
- **Authors**: Pengfei Huang, Yi Liu, Xiaojie Zhang +2
- **PDF**: https://ieeexplore.ieee.org/document/8277969
- **Abstract**: Rate-compatible error-correcting codes (ECCs), which consist of a set of extended codes, are of practical interest in both wireless communications and data storage. In this work, we first study the lower bounds for rate-compatible ECCs, thus proving the existence of good rate-compatible codes. Then, we propose a general framework for constructing rate-compatible ECCs based on cosets and syndromes of a set of nested linear codes. We evaluate our construction from two points of view. From a combinatorial perspective, we show that we can construct rate-compatible codes with increasing minimum distances. From a probabilistic point of view, we prove that we are able to construct capacity-achieving rate-compatible codes.

## CooECC: A Cooperative Error Correction Scheme to Reduce LDPC Decoding Latency in NAND Flash

- **Status**: ✅
- **Reason**: NAND Flash LDPC 디코딩 지연 감소 협력 ECC(CooECC), LSB→MSB 초기 LLR 활용 직접 NAND ECC (A)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8119288
- **Type**: conference
- **Published**: 5-8 Nov. 2
- **Authors**: Meng Zhang, Fei Wu, Yajuan Du +3
- **PDF**: https://ieeexplore.ieee.org/document/8119288
- **Abstract**: The storage capacity of NAND Flash has increased by scaling down to smaller cell size and using multi-level storage technology, but data reliability is degraded by severer retention errors. To ensure data reliability, error correction codes (ECC) are adopted, such as BCH and low-density parity check (LDPC) codes. However, BCH codes are insufficient when raw bit error rates (RBER) caused by retention errors are high. As a result, BCH codes are inevitably replaced with LDPC codes with stronger error correction capability. Traditional LDPC codes are used to independently correct bit errors in the LSB and MSB pages. Unfortunately, decoding latency in such two pages is significantly unbalanced, MSB pages take much higher latency due to higher RBER, leading to suboptimal flash read performance. This paper proposes a cooperative error correction scheme, called CooECC, to reduce LDPC decoding latency of the MSB page in NAND Flash. By exploiting data error characteristics introduced by retention errors, CooECC integrates the decoding result of the LSB page into the initial information of LDPC decoding for the MSB page, making it more accurate. This in turn enables decoding to converge at a higher rate. Simulation results show that for LDPC schemes with information lengths of 2KB and 4KB, the decoding latency can be reduced by up to 87% and 84%, respectively, when RBER is as high as 8.0 × 10^-3.

## Exploiting Process Variation for Read Performance Improvement on LDPC Based Flash Memory Storage Systems

- **Status**: ✅
- **Reason**: LDPC 기반 플래시의 PV 이용 읽기성능 개선, NAND/SSD 직접 LDPC ECC 시스템 (A)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8119291
- **Type**: conference
- **Published**: 5-8 Nov. 2
- **Authors**: Qiao Li, Liang Shi, Yejia Di +3
- **PDF**: https://ieeexplore.ieee.org/document/8119291
- **Abstract**: With the development of bit density and technology scaling, the process variation (PV) has become much severe on NAND flash memory. As PV presents reliability among flash blocks, which causes read performance variation to read data on different blocks. This paper proposes to improve read performance of LDPC based flash memory by exploiting the reliability characteristics of PV. First, a block grouping approach is proposed to classify the flash blocks based on their reliability. Then, a read data placement scheme is proposed, which is designed to place read-hot data on flash blocks with high reliability and move read-cold data to blocks with low reliability. Experiment results show that, with negligible overhead, the proposed scheme is able to significantly improve the read performance.

## LDPC-Based Adaptive Multi-Error Correction for 3D Memories

- **Status**: ✅
- **Reason**: 3D 메모리용 LDPC ECC 아키텍처+스크러빙+40nm CMOS 코덱 구현, 스토리지 ECC HW로 NAND 이식 가능 (B/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8119220
- **Type**: conference
- **Published**: 5-8 Nov. 2
- **Authors**: Mihai Lefter, George Voicu, Thomas Marconi +2
- **PDF**: https://ieeexplore.ieee.org/document/8119220
- **Abstract**: In this paper we introduce a novel error resilient memory architecture potentially applicable to a large range of memory technologies. In contrast with state of the art memory error correction schemes, which rely on (extended Hamming) Error Correcting Codes (ECC), we make use of Low Density Parity Check (LDPC) codes due to their close to the Shannon performance limit error correction capabilities. To allow for a cost-effective implementation we build our approach on top of a 3D memory organization which inherently fast and customizable wide-I/O vertical access allows for a smooth transfer of the required LDPC long code-words to/from an error correction dedicated die. To make the error correction process transparent to the memory users, e.g., processing cores, we propose an online memory scrubbing policy that performs the LDPC-based error detection and correction decoupled from the normal memory operation. For evaluation purposes we consider 3D memories protected by the proposed LDPC mechanism with various data width codes implementations. Simulation results indicate that our proposal clearly outperforms state of the art ECC schemes with fault tolerance improvements by a 4710× factor being obtained when compared to extended Hamming ECC. Furthermore, we evaluate instances of the proposed memory concept equipped with different LDPC codecs implemented on a commercial 40nm low-power CMOS technology and evaluate them on actual memory traces in terms of error correction capability, area, latency, and energy. Our results indicate that the LDPC protected memories offer substantially improved error correction capabilities, when compared to state of the art extended Hamming ECC, being able to assure clean runs for memory error rates α

## Unequal protection approach for RLL-constrained LDPC coded recording system using deliberate flipping

- **Status**: ✅
- **Reason**: UEP LDPC + 인터리버로 flipping 에러 집중·반복디코딩 복구, 바이너리 LDPC 디코딩 기법 이식 가능 (C/E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8368811
- **Type**: conference
- **Published**: 5-8 Nov. 2
- **Authors**: Hong-Fu Chou, Chiu-Wing Sham
- **PDF**: https://ieeexplore.ieee.org/document/8368811
- **Abstract**: For alleviating Run-Length-Limited (RLL) code, the deliberate flipping approach imposes some bit errors before recording in order to meet the RLL constraint. However, high coding rate of recording system limits the correcting capability of RLL flipping errors. In this paper, we propose a decoding scheme using Unequal Protection (UEP) Low-Density Parity-Check (LDPC) code by means of regular inter-leaver to confine the occurrence of flipping errors into a section of codeword. Specified section with flipping errors are attributed to the high degree nodes with high error protection capability. Iterative decoding within several iterations can solve the hard errors at the reading side. Experimental results reveal that our approach has a better BER performance compared to the recording system with RLL code. Experimental results show that our proposed scheme can efficiently exploit the correction capability to recover flipping bits.

## On the Nested Family of LDPC Codes Based on Golomb Rulers

- **Status**: ✅
- **Reason**: Golomb ruler 기반 신규 nested 바이너리 LDPC 부호족 구성(rate adaption) — 카테고리 E 코드설계
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8241257
- **Type**: conference
- **Published**: 29-30 Nov.
- **Authors**: Fedor I. Ivanov, Pavel S. Rybin
- **PDF**: https://ieeexplore.ieee.org/document/8241257
- **Abstract**: In this paper we present a new ensemble of Low- Density Parity-Check codes (LDPC Codes) based on modular Golomb rulers and permutation matrices. We suggest a designing rule for these codes that allows obtaining a nested family of LDPC codes with wide range of rates from one matrix of lowest rate code. Moreover, the regular way that we apply to construct our codes allows describing parity-check matrices with minimal number of parameters. The simulation results in the case of transmission via AWGN channel with QAM-4 modulation are presented.

## Joint constellation and code design for the Gaussian multiple access channel

- **Status**: ✅
- **Reason**: 두 LDPC 코드워드 동시 디코딩 위한 BP 확장+GA 수렴분석+LP 코드설계 — 카테고리 C/E 신규 기여, 바이너리
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8335656
- **Type**: conference
- **Published**: 29 Oct.-1 
- **Authors**: Yu-Chung Liang, Stefano Rini, Jörg Kliewer
- **PDF**: https://ieeexplore.ieee.org/document/8335656
- **Abstract**: The joint design of both transmit constellation and low-density parity-check codes (LDPC) for the two-user, symbol-synchronous, binary-input Gaussian multiple access channel is considered. A transmission scheme is proposed to approach the symmetric capacity without the use of time-sharing or rate-splitting by joint decoding of the noisy sum of two LDPC codewords. This scheme relies on an extension of the classic belief propagation (BP) algorithm which allows for the simultaneous decoding of two LDPC codewords. We use a Gaussian approximation (GA) of the message distribution to investigate the convergence of the decoding process and derive a linear programming technique for joint code design. We also implement a superposition modulation scheme to achieve higher rate. This code design is applied to different input constellation choices which attain the symmetric capacity in different SNR regimes. It is shown that, quite surprisingly, in the moderate SNR regime the best performance is obtained by an asymmetric constellation.

## Flash memories in high radiation environments: LDPC decoder study

- **Status**: ✅
- **Reason**: 플래시 메모리 LDPC 디코더(A) - 방사선 환경 멀티스테이트 채널 모델+Gallager B/E 디코더 신규 제안, NAND 직접 응용
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8335729
- **Type**: conference
- **Published**: 29 Oct.-1 
- **Authors**: Frederic Sala, Clayton Schoeny, Shahroze Kabir +2
- **PDF**: https://ieeexplore.ieee.org/document/8335729
- **Abstract**: Flash memory devices are increasingly being used in deep-space missions as on-board data storage in spacecraft. The harsh environment these missions take place in involves high levels of radiation which can cause decoding circuitry failures for the device error-correction module. For this reason, the decoder must be robust to radiation-induced errors. Previous works have studied hardware failure problem by modeling the circuitry noise as independent and constant in each component of the decoder. We propose a multi-state radiation channel which is designed to account for the dependence and duration of radiation-induced errors on different components. This model also subsumes some previously studied cases and allows for a more refined analysis. We introduce a corresponding LDPC combined Gallager B/E decoder and perform a density evolution analysis to characterize the idealized decoder performance. We optimize the decoder voting threshold parameter and apply our findings to a finite length case.

## Parallel LDPC decoder implementation on a mobile GPU

- **Status**: ✅
- **Reason**: 모바일 GPU상 BP 디코더 병렬화 + 정밀도/리소스 조합 최적화 — 이식 가능 병렬 디코더 구현(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8249333
- **Type**: conference
- **Published**: 21-22 Nov.
- **Authors**: Aleksei Kharin, Igor Volkov, Evgeny Mirokhin +6
- **PDF**: https://ieeexplore.ieee.org/document/8249333
- **Abstract**: In this paper we explore acceleration of the belief propagation (BP) and BP-based algorithms for decoding LDPC codes, using parallel computation on graphics processing units (GPUs) for mobile hardware platform. Different modifications of BP decoding algorithm are considered in search for best error correction performance in limited decoding time. Possible combinations of decoding algorithms, number precision and compute resources were found. Error correction performance for each found combination was measured. Best combination of decoding algorithm, number precision and compute resource was found for data transmission system with LDPC coding for DVB-T2/S2 (16200, 7200) code.

## Hard-decision decoding of LDPC codes under timing errors: Overview and new results

- **Status**: ✅
- **Reason**: timing error 하 bit-flipping/Gallager-B 디코딩, trapping set 회피 — 디코더 견고성 기법(C), 서베이지만 신규 결과 포함
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8249332
- **Type**: conference
- **Published**: 21-22 Nov.
- **Authors**: Srdan Brkic, Predrag Ivanis, Bane Vasić
- **PDF**: https://ieeexplore.ieee.org/document/8249332
- **Abstract**: This paper contains a survey on iterative decoders of low-density parity-check (LDPC) codes built form unreliable logic gates. We assume that hardware unreliability comes from supply voltage reduction, which causes probabilistic gate failures, called timing errors. We are able to demonstrate robustness of simple Gallager B decoder to timing errors, when applied on codes free of small trapping sets, as well as positive effects that timing errors have on the decoding of codes with contain small trapping sets. Furthermore, we show that concept of guaranteed error correction can be applied to the decoders made partially from unreliable components. In contrast to the decoding under uncorrelated gate failures, we prove that bit-flipping decoding under timing errors can achieve arbitrary low error probability. Consequently, we formulate condition sufficient that memory architecture, which employs bit-flipping decoder, preserved all stored information.

## Improved belief propagation based on the estimation backtracking

- **Status**: ✅
- **Reason**: estimation backtracking 기반 BP 개선(하드/소프트), 다수 바이너리 LDPC서 BER 향상 — 이식 가능 디코더 개선(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8249335
- **Type**: conference
- **Published**: 21-22 Nov.
- **Authors**: Jan Broulim, Vjaceslav Georgiev, Michael Holik +1
- **PDF**: https://ieeexplore.ieee.org/document/8249335
- **Abstract**: We propose a general method to improve the decoding performance of hard-decision and soft-decision belief propagation decoders. The performance of the proposed algorithm is tested on MacKay's widely known LDPC (504,252) code, CCSDS LDPC (256,128) and our irregular LDPC (128,64) code. The bit error rate indicated by our novel solution is up to five times lower for a particular signal-to-noise ratio of tested codes measured through AWGN simulations. Furthermore, a decoding time required for the same bit error rate as the bit error rate of a traditional BP decoder is up to three times lower when our approach is used in a non-pipelined implementation.

## Flexible parallel implementation of LLR BP decoding simulation on multicores using OpenCL

- **Status**: ✅
- **Reason**: OpenCL 멀티코어 LLR-BP 병렬 구현(전 디코딩 단계 병렬화) — 이식 가능 디코더 병렬화(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8249334
- **Type**: conference
- **Published**: 21-22 Nov.
- **Authors**: Igor Volkov, Aleksei Kharin, Aleksei Dryakhlov +6
- **PDF**: https://ieeexplore.ieee.org/document/8249334
- **Abstract**: In this paper we explore acceleration of the logarithmic likelihood ratio (LLR) belief propagation (BP) algorithm for LDPC codes decoding simulation, using parallel computation on graphics processing units (GPUs) with OpenCL technology. The proposed parallel implementation of the LLR BP algorithm includes parallel version of all decoding steps: decoder initialization, check and variable nodes update, a posteriori LLR calculation and decoding termination check. Decoder throughput was measured by simulating data transmission system with LDPC coding for DVB-T2/S2 (64800, 32400) and PEG (1008, 504) codes.

## Modified decoding algorithm of LDPC codes for physical-layer key reconciliation

- **Status**: ✅
- **Reason**: 키 재조정용이나 offset 기반 디코딩으로 check node 연산 축소 — 부호 비의존 디코더 복잡도 저감 기법 이식 여지 (C, Phase3 재검토)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8248431
- **Type**: conference
- **Published**: 11-13 Nov.
- **Authors**: Ying-wei Lu, Ze-liang Zheng, Xiao-yun Hou
- **PDF**: https://ieeexplore.ieee.org/document/8248431
- **Abstract**: Key extraction based on wireless channel-characteristics (Physical-Layer Key) is the new technology to ensure communication security. To solve the problem that the channel characteristics are not completely consistent in the process of key generation, low density parity check (LDPC) codes was proposed. But due to the process of the traditional decoding algorithm of LDPC codes, the computation of check nodes renew is too high and the efficiency of key reconciliation is too low. To overcome this problem, we propose the modified decoding algorithm of LDPC codes that combine traditional decoding algorithm and Offset-base decoding algorithm. This algorithm can reduce the computational complexity efficiently, and improve the efficiency of key reconciliation. Finally, the simulation results demonstrate that, the BER and success ratio of the key reconciliation is improving.

## New hard decision decoder of LDPC codes using single Bit Flipping algorithm

- **Status**: ✅
- **Reason**: LDPC용 신규 Single Bit-Flipping 하드결정 디코더 제안, 이식 가능 디코더 알고리즘(C).
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8238191
- **Type**: conference
- **Published**: 1-4 Nov. 2
- **Authors**: Soufian Addi, Ahlam Berkani, Ahmed Azouaoui +1
- **PDF**: https://ieeexplore.ieee.org/document/8238191
- **Abstract**: The Bit-Flipping (BF) algorithm is considered as a hard decoding method for LDPC codes. It is much simpler than the probabilistic methods like Sum Product Algorithm (SPA), and can be efficiently implemented by electronic circuits. In this paper, we propose a new Bit Flipping algorithm for Low-Density Parity-Check codes (LDPC) called Single Bit-Flipping (SBF). Compared to the Gallager Bit-Flipping algorithm, the proposed algorithm employs criteria of flipping single bit chosen carefully. This method eliminates the risk for flipping more than one bit at a time that can induce additional error bits and propagate the errors to the later iterations. We present some results obtained by applying this new method that provides a gain in performance in comparison to the standard Gallager Bit-Flipping with low complexity.
