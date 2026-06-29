# IEEE Xplore — 2018-05 (1차선별 통과)


## Characterization of Elementary Trapping Sets in Irregular LDPC Codes and the Corresponding Efficient Exhaustive Search Algorithms

- **Status**: ✅
- **Reason**: 비정규 LDPC elementary trapping set 특성화 및 효율적 exhaustive 탐색 알고리즘 - error floor 코드설계(E) 직접 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8279531
- **Type**: journal
- **Published**: May 2018
- **Authors**: Yoones Hashemi, Amir H. Banihashemi
- **PDF**: https://ieeexplore.ieee.org/document/8279531
- **Abstract**: In this paper, we propose a characterization of elementary trapping sets (ETSs) for irregular low-density paritycheck (LDPC) codes. These sets are known to be the main culprits in the error floor region of such codes. The characterization of ETSs for irregular codes has been known to be a challenging problem due to the large variety of nonisomorphic ETS structures that can exist within the Tanner graph of these codes. This is a direct consequence of the variety of the degrees of the variable nodes that can participate in such structures. The proposed characterization is based on a hierarchical graphical representation of ETSs, starting from simple cycles of the graph, or from single variable nodes, and involves three simple expansion techniques: degree-one tree (dot), path, and lollipop, thus, the terminology dpl characterization. A similar dpl characterization was proposed in an earlier work by the authors for the leafless ETSs of variable-regular LDPC codes. The present paper generalizes the prior work to codes with a variety of variable node degrees and to ETSs that are not leafless. The proposed dpl characterization corresponds to an efficient search algorithm that, for a given irregular LDPC code, can find all the instances of (a, b) ETSs with size a and with the number of unsatisfied check nodes b within any range of interest a amax and b bmax, exhaustively. Although branch-&-bound exhaustive search algorithms for finding ETSs of irregular LDPC codes exist, to the best of our knowledge, the proposed search algorithm is the first of its kind, in that, it is devised based on a characterization of ETSs that makes the search process efficient. For a constant degree distribution and range of search, the worst-case complexity of the proposed dpl algorithm increases linearly with the block length n. The average complexity, excluding the search for the input simple cycles, is constant in n. Extensive simulation results are presented to show the versatility of the search algorithm, and to demonstrate that, compared to the literature, significant improvement in search speed can be obtained.

## PEG-Like Design of Binary QC-LDPC Codes Based on Detecting and Avoiding Generating Small Cycles

- **Status**: ✅
- **Reason**: 바이너리 QC-LDPC 부호 설계(E): 새 MM-QC-PEG 알고리즘으로 small-cycle 검출/회피, masking 기법 신규 기여
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8241708
- **Type**: journal
- **Published**: May 2018
- **Authors**: Xuan He, Liang Zhou, Junyi Du
- **PDF**: https://ieeexplore.ieee.org/document/8241708
- **Abstract**: In this paper, we propose a new multi-edge metric-constrained quasi-cyclic progressive edge-growth algorithm (MM-QC-PEGA), which is suitable for constructing both single- and multi-weighted (binary) QC low-density parity-check (LDPC) codes with arbitrary lengths, rates, circulant sizes, and variable node (VN)-degree distributions. The MM-QC-PEGA is able to detect all cyclic-edge-set-minimum-virtual cycles (CMVCs), as it accurately computes the metric value of each CMVC with an a posteriori test. In addition, we propose a new greatest-common-divisor (GCD)-approximation for time efficiently approximating the metric value of a CMVC without a posteriori tests, and propose a new GCD-approximated MM-QC-PEGA (G-MM-QC-PEGA) by using the GCD-approximation to replace the a posteriori test involved in the MM-QC-PEGA. As a result, the G-MM-QC-PEGA is faster than the MM-QC-PEGA, and the CMVCs undetectable to the G-MM-QC-PEGA under multi- and single-weighted QC-LDPC code graphs have minimum lengths of eight and ten, respectively. Moreover, we propose a new masking technique that is efficient in masking the parity-check matrix consisting of an array of arbitrary circulants of the same size. Compared with the several existing works, our proposed algorithms could perform better or comparably in terms of avoiding generating small cycles and error performances. Our proposed algorithms somewhat perfect the works of QC-LDPC code construction.

## A Two-Bit Weighted Bit-Flipping Decoding Algorithm for LDPC Codes

- **Status**: ✅
- **Reason**: 이진 LDPC용 새 two-bit weighted bit-flipping 디코더(C) - 간단한 비트연산으로 고속화, NAND ECC 디코더에 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8302884
- **Type**: journal
- **Published**: May 2018
- **Authors**: Jieun Oh, Jeongseok Ha
- **PDF**: https://ieeexplore.ieee.org/document/8302884
- **Abstract**: This letter proposes a novel two-bit weighted bit-flipping algorithm (TB-WBFA) for low-density parity-check (LDPC) codes on the binary symmetric channel. The proposed TB-WBFA produces reliability bits for the bit-decision results and syndrome values at bit and check nodes, respectively. The reliability bits are exchanged between bit and check nodes as the decoding proceeds. The message update in check nodes is carefully devised with simple bitwise operations, which are especially suitable for high-speed operations. It will be demonstrated that the proposed TB-WBFA achieves a significant performance improvement over existing bit-flipping decoding algorithms by conducting performance comparisons for LDPC codes under various setups, i.e., different rates, lengths, and structures.

## Low Decoding Complexity of LDPC Codes Over the Binary Erasure Channel

- **Status**: ✅
- **Reason**: C. BEC에서 BP 실패 시 체크노드 기반 추측으로 복잡도 절감하는 신규 바이너리 LDPC 디코더 알고리즘
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8472553
- **Type**: conference
- **Published**: 8-10 May 2
- **Authors**: Sareh Majidi Ivari, M. Reza Soleymani, Yousef R. Shayan
- **PDF**: https://ieeexplore.ieee.org/document/8472553
- **Abstract**: In this paper, we present a new low complexity decoding algorithm outperforming existing schemes. When the Belief Propagation fails and cannot solve all the erased bits, the guessing algorithm makes assumptions on a set of erased bits. However, in our new algorithm instead of guessing the values of a set of message bits, the decoder selects a set of check nodes and makes assumption on bits connected to them. The number of possibilities is reduced by half because the field is binary resulting in lower decoding complexity. The proposed decoding algorithm is applied to two regular half rate LDPC codes with lengths of 1000 and 2000. The theoretical belief propagation (BP) threshold for these two codes is 0.429. It is shown that the actual BP threshold is improved using the new algorithm. Setting the number of possibilities to two, we achieve a threshold of 0.43 which is higher than the BP theoretical.

## Reconfigurable Decoder for LDPC and Polar Codes

- **Status**: ✅
- **Reason**: LDPC와 polar의 BP 유사성을 이용한 재구성 가능 디코더 — 바이너리 LDPC BP에 이식 가능한 HW 효율화 기법(D), 애매하나 살림
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:8351337
- **Type**: conference
- **Published**: 27-30 May 
- **Authors**: Ningyuan Yang, Shusen Jing, Anlan Yu +4
- **PDF**: https://ieeexplore.ieee.org/document/8351337
- **Abstract**: With low-density parity-check (LDPC) code and polar code selected as the standard codes for 5G eMBB scenario, one challenge is how to improve the hardware efficiency when both decoders are required by one system. Since LDPC and polar codes can be decoded with belief propagation (BP) algorithms, this similarity allows us to design a reconfigurable decoder, which can decode both codes at the cost of only one decoder. Numerical and implementation results are also given in this paper to show that the proposed decoder achieves higher hardware efficiency than stand-alone LDPC or polar decoder, without harming the error performance.

## Perfect Column-Layered Two-Bit Message-Passing LDPC Decoder and Architectures

- **Status**: ✅
- **Reason**: Flash 메모리용 2-bit message-passing LDPC 디코더의 column-layered 스케줄링 및 VLSI 아키텍처 — C/D, NAND 직접 언급
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8351684
- **Type**: conference
- **Published**: 27-30 May 
- **Authors**: Xinmiao Zhang, Alexander Bazarsky
- **PDF**: https://ieeexplore.ieee.org/document/8351684
- **Abstract**: Flash and other memories may adopt multi-stage low-density parity-check (LDPC) decoders to reduce the average decoding latency and power consumption. To meet the increasingly tighter latency constraints of next-generation data centers, the earlier-stage decoders need to have better error-correcting capability and lower latency. To achieve this goal, this paper first develops a column-layered scheduling scheme for the 2-bit message-passing (TBMP) LDPC decoding algorithm, which has significant coding gain over the 3-bit Min-sum algorithm. The proposed column-layered scheme is perfect in the sense that it does not cause any coding gain degradation. Also by utilizing the 2-bit property, efficient VLSI architectures are designed for the column-layered and non-layered TBMP algorithms. Complexity analysis shows that, the layered (non-layered) TBMP decoder has more than 10 (8) times shorter latency at the cost of 53% (8%) larger area compared to a row-layered 3-bit Min-sum decoder for an example (17664, 16560) LDPC code.

## Lightweight Hardware Architecture for Probabilistic Gradient Descent Bit Flipping on QC-LDPC Codes

- **Status**: ✅
- **Reason**: QC-LDPC용 PGDBF 디코더의 경량 HW 아키텍처(확률신호 생성기 없이 확률거동 에뮬레이션, ASIC 구현) — D
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:8351055
- **Type**: conference
- **Published**: 27-30 May 
- **Authors**: Khoa Le, Fakhreddine Ghaffari, Lounis Kessal +3
- **PDF**: https://ieeexplore.ieee.org/document/8351055
- **Abstract**: The Probabilistic Gradient Descent Bit-Flipping (PGDBF) decoder offers a significant improvement in decoding performance for Low-Density Parity-Check (LDPC) codes on Binary Symmetric Channel (BSC). However, this outstanding decoding performance comes along with a non-negligible extra hardware cost to realize the probabilistic behavior on top of the deterministic Gradient Descent Bit-Flipping (GDBF) decoder. This paper presents a novel solution to implement PGDBF decoder on Quasi-Cyclic LDPC codes. The proposed architecture takes advantage of the cyclic shift permutation nature of QC-LDPC and changes the message flow such that a probabilistic behavior is emulated without the cost of an actual probabilistic signal generator. It is shown that, the proposed architecture improves the PGDBF decoding performance with respect to the state-of-the-art implementation while reducing hardware complexity, even being lower than that of the deterministic GDBF. The efficiency of our proposed method is verified through the ASIC 90nm CMOS technology implementations and decoding simulations.

## Probabilistic Gradient Descent Bit-Flipping Decoders for Flash Memory Channels

- **Status**: ✅
- **Reason**: NAND flash 채널용 신규 저복잡도 반복 디코더 PGDBF(global computation+randomness) 및 HW 합성 — A/C
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8351713
- **Type**: conference
- **Published**: 27-30 May 
- **Authors**: Fakhreddine Ghaffari, Bane Vasic
- **PDF**: https://ieeexplore.ieee.org/document/8351713
- **Abstract**: Low-density parity check (LDPC) codes are an attractive error correction scheme for ensuring data integrity in new generation of NAND flash memories. A quick assessment of the iterative decoders for LDPC codes reveals a wide range of varying complexities. The simple Bit-Flipping (BF) and binary-message-passing algorithms such as the Gallager A/B algorithms occupy one end of the spectrum, while Belief Propagation (BP) and A Posteriori Probability (APP) decoders lie at the other end. The gamut of existing decoders filling the intermediate space can simply be understood as the implementation of BP (and its variants, such as the min-sum algorithm) at different levels of message precision. Decoders with low-precision messages are desirable because of their low complexity and power efficiency, but in such decoders it is highly nontrivial to prevent performance degradation known to as error floor and to guarantee fast convergence to a codeword. In this paper we present our results on a new class of low-complexity iterative decoders for flash memory channels. They involve two main innovations: global computation and randomness. Our decoding algorithm, Probabilistic Gradient Descent Bit-Flipping (PGDBF) is motivated by the analogy between Tanner graphs and the graphical models used in statistical mechanics, and prescribe a rule for flipping a bit based on the so-called energy function and a binary random sequence associated to that bit. Energy function is computationally simple, but involves all the bits. We present the PGDBF algorithm analysis, explain how it benefits from global computation and randomness, and present the hardware synthesis results as well as comparisons with the state-of-the-art decoders.

## Layer-by-layer Adaptively Optimized ECC of NAND flash-based SSD Storing Convolutional Neural Network Weight for Scene Recognition

- **Status**: ✅
- **Reason**: TLC NAND flash SSD 직접 — layer-by-layer iteration-optimized LDPC ECC, 디코딩 시간/오버헤드 절감 (A)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8351440
- **Type**: conference
- **Published**: 27-30 May 
- **Authors**: Keita Mizushina, Toshiki Nakamura, Yoshiaki Deguchi +1
- **PDF**: https://ieeexplore.ieee.org/document/8351440
- **Abstract**: Layer-by-layer Adaptively Optimized Error Correcting Code (ECC) is proposed to improve the reliability of triple-level cell (TLC) NAND flash-based SSD for the scene recognition using convolutional neural network (CNN) of IoT edge devices. Layer-by-layer Adaptively Optimized ECC is composed of Layer-by-layer Iteration-Optimized Low Density Parity-Check (LBL-LDPC) and Layer-by-layer Code-length Adjusted Asymmetric Coding (LBL-AC). The conventional techniques like LDPC ECC and Asymmetric Coding (AC) improve the reliability. However, they require large overheads of the ECC decoding time and the flag/parity cell. Proposed LBL-LDPC and LBL-AC decrease the ECC decoding time by 14% and the data overhead by 26%, respectively, without recognition accuracy degradation. In addition, the data-retention time extends by 230%.

## Optimization of Finite-Length SC-LDPC for Uplink NOMA

- **Status**: ✅
- **Reason**: 유한길이 SC-LDPC 구성 최적화(프로토그래프/coupling length 공동최적화), 바이너리 LDPC 코드설계 기법 E 해당
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8403618
- **Type**: conference
- **Published**: 20-24 May 
- **Authors**: Shuang Chen, Kewu Peng, Yushu Zhang +1
- **PDF**: https://ieeexplore.ieee.org/document/8403618
- **Abstract**: Due to lack of universality, the achievable channel parameter regions (ACPRs) of conventional channel codes are far from the outer boundary of non-orthogonal multiple access (NOMA) channel capacity region. Spatially coupled low-density parity-check (SC-LDPC) codes show excellent asymptotic performance and their ACPRs are able to approach the outer boundary of NOMA channels. However, the performance of finite-length SC-LDPC codes is not as excellent as its asymptotic counterpart. In this paper, a two-phase algorithm is proposed to construct capacity-approaching SC-LDPC codes with finite codeword length. By jointly optimizing the protograph, the spatial coupling length and the uncoupled code length, the performance loss of SC-LDPC code caused by finite codeword length is minimized. Simulation results show that the ACPR of the optimized SC-LDPC code is only 1.2 dB from the theoretical limit of NOMA channels when the codeword length is 9600.

## Subcode-Based Early HARQ for 5G

- **Status**: ✅
- **Reason**: LDPC subcode 부분수신 codeword로 조기 피드백 HARQ. LDPC 부구조 활용 신규 기법, C/E 이식 가능성 애매하여 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8403491
- **Type**: conference
- **Published**: 20-24 May 
- **Authors**: Baris Goektepe, Stephan Faehse, Lars Thiele +2
- **PDF**: https://ieeexplore.ieee.org/document/8403491
- **Abstract**: Tactile Internet (TI) constitutes one of the major use cases for the development of the fifth generation (5G) mobile specification. TI services put high demand on the latency and reliability requirement, which is covered in the ultra-reliable low-latency communication (URLLC) discussion in 5G standardization. Hybrid Automatic Repeat Request (HARQ) is used in LTE to achieve high robustness in an efficient way with the cost of introducing additional latency. In this paper, we propose a new early HARQ scheme based on LDPC subcodes (SC E- HARQ), which enables to provide faster feedback and thus an earlier retransmission. The SC E-HARQ technique makes use of substructures in LDPC codes to start feedback calculation already on partially received codewords. This paper investigates the performance of SC E-HARQ in comparison with a second E-HARQ scheme based on log-likelihood ratio (LLR) estimation. The results show that SC E-HARQ achieves a comparable reliability to regular HARQ. In SNR regions relevant for URLLC, it clearly outperforms also the LLR-based E-HARQ in means of reliability as well as latency. Sub-millisecond latency with a total block error rate (BLER) of less than 10^(-4) is attained in TDL-C by allowing 1% false negative retransmissions.

## Scattered EXIT Charts for Finite Length LDPC Code Design

- **Status**: ✅
- **Reason**: 유한길이 LDPC degree profile 최적화용 S-EXIT 차트 신규 코드설계 기법(E), 바이너리 LDPC 대상
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8422961
- **Type**: conference
- **Published**: 20-24 May 
- **Authors**: Moustafa Ebada, Ahmed Elkelesh, Sebastian Cammerer +1
- **PDF**: https://ieeexplore.ieee.org/document/8422961
- **Abstract**: We introduce the Scattered Extrinsic Information Transfer (S-EXIT) chart as a tool for optimizing degree profiles of short length Low-Density Parity-Check (LDPC) codes under iterative decoding. As degree profile optimization is typically done in the asymptotic length regime, there is space for further improvement when considering the finite length behavior. We propose to consider the average extrinsic information as a random variable, exploiting its specific distribution properties for guiding code design. We explain, step-by-step, how to generate an S-EXIT chart for short-length LDPC codes. We show that this approach achieves gains in terms of bit error rate (BER) of 0.5 dB and 0.6 dB over the additive white Gaussian noise (AWGN) channel for codeword lengths of 128 and 180 bits, respectively, at a target BER of 10-4 when compared to conventional Extrinsic Information Transfer (EXIT) chart-based optimization. Also, a performance gain for the Binary Erasure Channel (BEC) for a block (i.e., codeword) length of 180 bits is shown.

## A GPS Synchronized, Long-Range Uplink-Only Radio Designed for IoT

- **Status**: ✅
- **Reason**: IoT용 새로 설계한 LDPC를 ECC로 사용; 신규 코드 설계 언급으로 애매하여 Phase 3 재검토로 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8422798
- **Type**: conference
- **Published**: 20-24 May 
- **Authors**: Seiji Kobayashi, Nabil Loghin, Ryoji Ikegaya +6
- **PDF**: https://ieeexplore.ieee.org/document/8422798
- **Abstract**: Targeting IoT, we have developed an efficient radio system. The system uses GPS (Global Positioning System) for time and frequency calibration. The system uses a newly designed LDPC as error correction, an efficient π/2 shift BPSK modulation and linear chirp modulation for spectrum spreading. In this system, the transmission channel is estimated using evenly-distributed sync symbols and the channel deterioration is corrected. Together with these technologies, we have experimentally confirmed that the system exhibits -144 dBm of sensitivity. We also confirmed that it could achieve long-range communication in an urban environment. Another experiment shows that signals from a fast moving object can also be decoded.

## Trapping Set Analysis of Horizontal Layered Decoder

- **Status**: ✅
- **Reason**: layered Gallager-B 디코더 trapping set/error floor 분석(C/E), 바이너리 LDPC BSC 대상 이식 가능 디코더 기법
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8422965
- **Type**: conference
- **Published**: 20-24 May 
- **Authors**: Nithin Raveendran, Bane Vasic
- **PDF**: https://ieeexplore.ieee.org/document/8422965
- **Abstract**: In this paper, we present how the decoding performance of layered decoder can be analyzed using trapping sets. Surprisingly, a simple horizontal layered Gallager-B decoder breaks all weight-3 error patterns on a (5,3) trapping set successfully, resulting in a steeper slope in frame error rate (FER) curves compared to a flooding schedule decoder. Theoretical validation of the results is also done using a semi- analytical method for computing the error floors of LDPC codes on a binary symmetric channel decoded using layered Gallager-B algorithm.

## Exploiting Noise Correlation for Channel Decoding with Convolutional Neural Networks

- **Status**: ✅
- **Reason**: BP-CNN 반복 디코더로 상관잡음 활용, 신경망 디코더(C)로 바이너리 LDPC BP에 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8422290
- **Type**: conference
- **Published**: 20-24 May 
- **Authors**: Fei Liang, Cong Shen, Feng Wu
- **PDF**: https://ieeexplore.ieee.org/document/8422290
- **Abstract**: Inspired by the recent advances in deep learning, we propose a novel iterative belief propagation-convolutional neural network (BP-CNN) architecture to exploit noise correlation for channel decoding under correlated noise. The standard BP decoder is used to estimate the coded bits, followed by a CNN to remove the estimation errors of the BP decoder and obtain a more accurate estimation of the channel noise. Iterating between BP and CNN will gradually improve the decoding SNR and hence result in better decoding performance. To train a well-behaved CNN model, we define a new loss function which involves not only the accuracy of the noise estimation but also the normality test for the estimation errors, i.e., to measure how likely the estimation errors follow a Gaussian distribution. The introduction of the normality test to the CNN training shapes the residual noise distribution and further reduces the BER of the iterative decoding, compared to using the standard quadratic loss function. We carry out extensive experiments to analyze and verify the proposed framework.

## Two Improved Algorithms for Layered QC-LDPC Decoding Algorithm

- **Status**: ✅
- **Reason**: layered QC-LDPC 디코딩 개선 알고리즘 2종 제안(수렴 가속+오류정정 보정)으로 BP/layered 디코더 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8447564
- **Type**: conference
- **Published**: 13-16 May 
- **Authors**: Xiao Zheng, Qingsheng Hu, Jun Feng
- **PDF**: https://ieeexplore.ieee.org/document/8447564
- **Abstract**: Low-Density Parity-Check code is a kind of near-optimal error correction code. In order to improve the performance of layered decoding algorithms, two algorithms are put forward in this paper. In the first algorithm, additional messages are employed for the messages updating operation of each layer by using another layered part, making it possible to accelerate the speed of convergence. In the second one, a correction operation for certain type of errors is performed to improve the decoding performance. Simulation results show that more decoding gain and accelerated convergence can be obtained compared with the conventional layered decoding algorithms.

## Iterative Soft-Decision Decoding of Binary Cyclic Codes Based on Extended Parity-Check Transformation Algorithm

- **Status**: ✅
- **Reason**: 바이너리 cyclic code 반복 연판정 디코딩(확장 패리티체크+BP/ABP 비교) - 부호 비의존적 메시지패싱 기법으로 바이너리 LDPC BP 이식 가능(C), 애매하나 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8447536
- **Type**: conference
- **Published**: 13-16 May 
- **Authors**: Oluwaseyi Babalola, Jaco Versfeld
- **PDF**: https://ieeexplore.ieee.org/document/8447536
- **Abstract**: In this paper, an iterative soft-decision (SD) decoding algorithm for cyclic codes based on extended parity-check equations is developed. The algorithm does not necessarily utilize the algebraic properties of the code, but operates on transforming the systematic parity-check matrix using the soft reliability information matrix obtained from the received vector. Results show a significant performance gain when compared with the hard decision Berlekamp-Massey(B-M) and belief propagation (BP) algorithms, but present a similar bit error rate (BER) performance when compared to the adaptive belief propagation (ABP) algorithm. An important feature of the decoder is that it functions within a practical decoding time complexity, and can be generally implemented for the class of linear block codes.
