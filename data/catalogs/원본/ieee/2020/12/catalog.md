# IEEE Xplore — 2020-12


## Analysis and Improvement of Error-Floor Performance for JSCC Scheme Based on Double Protograph LDPC Codes

- **Status**: ❌
- **Reason**: JSCC 소스-채널 결합 DP-LDPC error floor — JSCC 베이스라인, 떼어낼 ECC 기법 없음
- **ID**: ieee:9252117
- **Type**: journal
- **Published**: Dec. 2020
- **Authors**: Qiwang Chen, Francis C. M. Lau, Huihui Wu +1
- **PDF**: https://ieeexplore.ieee.org/document/9252117
- **Abstract**: In a joint source-channel coding (JSCC) system, excessive source compression can cause an error floor. In the original JSCC scheme based on double protograph LDPC (DP-LDPC) codes, only connections exist between check nodes (CNs) of the source protograph and variable nodes (VNs) of the channel protograph, and error floors are observed. In this paper, we investigate the joint protograph that forms the basis of a DP-LDPC code. The joint protograph consists of a source protograph, a channel protograph, and connections between the two protographs. Our main focus is on the complete-source-variable-linking (CSVL) protomatrix of the joint protograph, which determines the error floor of the DP-LDPC code. We propose a generalized source protograph extrinsic information transfer (GSP-EXIT) algorithm for evaluating the source decoding thresholds of the CSVL protomatrix. Based on the proposed algorithm, we analyze CSVL protomatrices with regular or irregular source protographs. We present design criteria for connections between VNs of the source protograph and CNs of the channel protograph. Such design rules will result in a higher source decoding threshold, which implies a lower error floor. We also propose a differential evolution algorithm for optimizing the source protograph. We present/compare analytical results and/with simulation results, and conclude that they are consistent.

## Two-Layer Coded Channel Access With Collision Resolution: Design and Analysis

- **Status**: ❌
- **Reason**: 다중접속 충돌해소용 2계층 코딩; LDPC는 베이스라인이고 떼어낼 ECC 기법 없음
- **ID**: ieee:9180052
- **Type**: journal
- **Published**: Dec. 2020
- **Authors**: Mohammadreza Ebrahimi, Farshad Lahouti, Victoria Kostina
- **PDF**: https://ieeexplore.ieee.org/document/9180052
- **Abstract**: We propose a two-layer coding architecture for communication of multiple users over a shared slotted medium enabling joint collision resolution and decoding. Each user first encodes its information bits with an outer code for reliability, and then transmits these coded bits with possible repetitions over transmission time slots of the access channel. The transmission patterns are dictated by the inner collision-resolution code and collisions with other users' transmissions may occur. We analyze two types of codes for the outer layer: long-blocklength LDPC codes, and short-blocklength algebraic codes. With LDPC codes, a density evolution analysis enables joint optimization of both outer and inner code parameters for maximum throughput. With algebraic codes, we invoke a similar analysis by approximating their average erasure correcting capability while assuming a large number of active transmitters. The proposed low-complexity schemes operate at a significantly smaller gap to capacity than the state of the art. Our schemes apply both to a multiple access scenario where the number of users within a frame is known a priori, and to a random access scenario where that number is known only to the decoder. In the latter case, we optimize an outage probability due to the variability in user activity.

## A Flexible and High Parallel Permutation Network for 5G LDPC Decoders

- **Status**: ✅
- **Reason**: D: 5G QC-LDPC용 고병렬 permutation network 신규 HW — 디코더 셔플 아키텍처 이식 가능
- **ID**: ieee:9117061
- **Type**: journal
- **Published**: Dec. 2020
- **Authors**: Zhiwei Zhong, Yongming Huang, Zaichen Zhang +2
- **PDF**: https://ieeexplore.ieee.org/document/9117061
- **Abstract**: Cyclic shifting is usually applied in quasi-cyclic low-density parity-check (QC-LDPC) decoders for permutation operations. In this brief, we propose a flexible and high parallel permutation network for QC-LDPC decoders in the 5th generation (5G) communication systems, which supports LDPC codes with arbitrary code lengths and all lifting sizes in 5G standards. The proposed permutation network can cyclically shift at most 128 frames of data in parallel, which greatly improves the hardware efficiency and decoding throughput. Based on the TSMC 90-nm CMOS technology, synthesis results illustrate the superiority of the proposed design.

## Flexible High Throughput QC-LDPC Decoder With Perfect Pipeline Conflicts Resolution and Efficient Hardware Utilization

- **Status**: ✅
- **Reason**: D/C: QC-LDPC 디코더 파이프라인 해저드 해소 신규 아키텍처+스케줄 GA 최적화 — 이식 가능
- **ID**: ieee:9179021
- **Type**: journal
- **Published**: Dec. 2020
- **Authors**: Vladimir L. Petrović, Miloš M. Marković, Dragomir M. El Mezeni +2
- **PDF**: https://ieeexplore.ieee.org/document/9179021
- **Abstract**: Modern communication standards, such as 5G new radio (5G NR), require a high speed decoder for highly irregular quasi-cyclic low density parity check (QC-LDPC) codes. A widely used approach in QC-LDPC decoders is a layered decoding schedule which processes the parity check matrix in parts, thus providing faster convergence. However, pipelined layered decoding architecture suffers from data hazards that reduce the throughput. This paper presents a novel architecture, which can facilitate any QC-LDPC decoding without stall cycles caused by pipeline hazards. The decoder conveniently incorporates both the layered and the flooding schedules in cases when hazards occur. The paper also presents the genetic algorithm based optimization of the decoding schedule for better signal-to-noise ratio (SNR) performance. The proposed architecture enables insertion of a large number of pipeline stages, thus providing high operating frequency. As a case study, the FPGA implementation for WiMAX, DVB-S2X, and 5G NR provided coded throughput of up to 1.77 Gbps, 4.32 Gbps, and 4.92 Gbps at 10 iterations, respectively. The results show a strong throughput increase of 30%-109% compared with the conventional layered decoder for 5G NR for the same SNR performance. The decoder provides highly efficient utilization of resources when compared with the state-of-the-art solutions.

## Channel Coding Scheme for Relay Edge Computing Wireless Networks via Homomorphic Encryption and NOMA

- **Status**: ❌
- **Reason**: NOMA+동형암호 채널코딩; LDPC는 부수 언급, 새 ECC 기법 없음
- **ID**: ieee:9195520
- **Type**: journal
- **Published**: Dec. 2020
- **Authors**: Feng Hu, Bing Chen
- **PDF**: https://ieeexplore.ieee.org/document/9195520
- **Abstract**: Edge computing extends the service resources of cloud computing to the edge of the network, providing less latency and higher bandwidth utilization. The relay edge computing wireless network (RECWN) with intelligent edge device can effectively solve the problem of wireless signal transmission distance and attenuation. However, the relay node's forwarding brings greater risks to the leakage of private information. In this article, we propose a homomorphic encryption and non-orthogonal multiple access (NOMA) based channel coding scheme to address the problem of stealing private information from users by incompletely trusted relay node or potential malicious nodes. Specifically, the homomorphic encryption algorithm is adopted to protect the privacy of users' private information. Furthermore, the code domain NOMA and LDPC algorithm are introduced to compensate for the problem of drastic drop in communication performance caused by poor sub-channel conditions, thereby improving the efficiency of data transmission, and guaranteeing the users' QoS requirements and fairness. The simulation results demonstrate that the proposed channel coding scheme has better performance than the existing approaches in terms of privacy preservation and data transmission efficiency.

## A High-Performance Stochastic LDPC Decoder Architecture Designed via Correlation Analysis

- **Status**: ✅
- **Reason**: C/D: stochastic LDPC 디코더 신규 VN 구조·아키텍처 — 디코더/HW 기법 이식 가능
- **ID**: ieee:9126828
- **Type**: journal
- **Published**: Dec. 2020
- **Authors**: Qichen Zhang, Yun Chen, Shixian Li +2
- **PDF**: https://ieeexplore.ieee.org/document/9126828
- **Abstract**: This paper presents an area-efficient architecture for stochastic low-density parity-check (LDPC) decoder with high throughput and excellent bit-error-rate (BER) performance. The correlation effects of a stochastic Sum-Product Algorithm (SPA) are analyzed. Based on this analysis, a variable node (VN) structure is proposed and its similarity with a correlation divider (CORDIV) is pointed out. Based on the properties of CORDIV, the area of probability tracer in the VN is reduced significantly. In order to achieve more accurate results when the check-to-variable (C2V) messages are not strong enough, the 3-3 input grouping sub-node is replaced by an adder-based 5-1 input grouping sub-node of the degree-6 VN for (2048,1723) code. An unbiased stochastic sequence generator is adopted to get more accurate results from the smaller probability tracer. Furthermore, the soft bit-flipping prior-processing and the C2V-based hard decision updating method are combined in VN to reduce the decoding latency. A (2048,1723) stochastic LDPC decoder is designed in the TSMC 65 nm process to demonstrate the proposed decoder architecture. With the aid of early termination, the decoder occupies 2.34 mm2 core area and can achieve 116.17 Gb/s at 4.4 dB and 461.99 Gb/s at 5.5 dB under 970 MHz with better decoding performance. Compared with the state-of-the-art stochastic IEEE 802.3an LDPC decoders, the proposed architecture can achieve the best throughput, throughput-to-area ratio, and BER performance.

## Exploiting Error Characteristic to Optimize Read Voltage for 3-D NAND Flash Memory

- **Status**: ✅
- **Reason**: 3D TLC NAND read voltage 최적화·RBER 저감(A) NAND 직접
- **ID**: ieee:9241228
- **Type**: journal
- **Published**: Dec. 2020
- **Authors**: Meng Zhang, Fei Wu, Qin Yu +3
- **PDF**: https://ieeexplore.ieee.org/document/9241228
- **Abstract**: 3-D NAND flash memory has become increasingly popular nonvolatile storage devices due to large capacity and high performance. With the increase of program/erase (P/E) cycles and retention periods, the threshold voltage distribution of 3-D NAND flash memory is prone to shift such that it is difficult to accurately obtain the read reference voltage (RRV). When reading data, read retry operations perform multiple flash sensing to read bit information correctly, inducing extended read latency. To mitigate the read latency, a method of precisely acquiring the RRV is urgently needed. Using an field-programmable gate array (FPGA) hardware testing platform, this article first studies error characteristics of 3-D triple-level cell (TLC) NAND flash memory with the floating gate (FG) structure, which includes the variations of raw bit error rates (RBERs) in different layers and pages, the variations of block reads under different read modes, and the threshold voltage shifting characteristic. Then, based on these characterizations, this article develops an error characteristic aware RRV acquisition scheme, called ECRRV, to gain optimal RRV by exploiting the least square method. Experimental results show that the proposed scheme can significantly diminish the RBER and block read count.

## Decoding Binary Linear Codes Over Channels With Synchronization Errors

- **Status**: ❌
- **Reason**: deletion/동기화 오류 채널의 LP 디코딩 — LDPC 아님, 떼어낼 NAND ECC 기법 없음
- **ID**: ieee:9133412
- **Type**: journal
- **Published**: Dec. 2020
- **Authors**: Kai Yang, Jie Ren, Chao Tian +2
- **PDF**: https://ieeexplore.ieee.org/document/9133412
- **Abstract**: Time synchronization is crucial for the safe and reliable operation of the fifth generation (5G) network, especially for applications requiring ultra-reliable low-latency data transmissions. The time synchronization problem, however, becomes increasingly challenging in high-mobility scenarios because the channel conditions, e.g., the multipath delay spread may vary rapidly. While there exist numerous works on the design of efficient channel decoding algorithms, decoding linear codes such as polar codes in the presence of synchronization errors is a less-explored topic. In this paper, we aim to fill this void and develop a systemic approach to decode general binary linear codes over binary symmetric channels with synchronization errors in which the lack of synchronization is modeled as the deletion channel model. The maximum likelihood (ML) decoding problem for binary linear codes over deletion channels is first formulated as a nonlinear optimization problem, in which a set of linear constraints are employed to characterize the input-output relationship of a deletion channel. It turns out that both the objective function and the constraints of this optimization problem are nonlinear, which poses significant challenges against the design of efficient decoding algorithms. As a remedy, we first replace the nonlinear objective function of this optimization problem via a lower bound. And we prove this lower bound is a linear function in the special case that the input is binary. We then apply the linear programming (LP) relaxation approach to obtain an approximate solution to the proposed nonlinear optimization problem. An adaptive branch-and-cut decoding algorithm has also been developed by making use of the ML-certificate property of the LP decoder for deletion channel. It is seen through simulation studies that the proposed decoding algorithm can achieve close-to-optimal bit error rate (BER) decoding performance at moderate computational complexity.

## Compressed Coding, AMP-Based Decoding, and Analog Spatial Coupling

- **Status**: ❌
- **Reason**: compressed sensing+AMP 디코딩, analog spatial coupling — LDPC ECC 디코더/구성 이식 기법 없음
- **ID**: ieee:9201010
- **Type**: journal
- **Published**: Dec. 2020
- **Authors**: Shansuo Liang, Chulong Liang, Junjie Ma +1
- **PDF**: https://ieeexplore.ieee.org/document/9201010
- **Abstract**: This paper considers a compressed-coding scheme that combines compressed sensing with forward error control coding. Approximate message passing (AMP) is used to decode the message. Based on the state evolution analysis of AMP, we derive the performance limit of compressed-coding. We show that compressed-coding can approach Gaussian capacity at a very low compression ratio. Further, the results are extended to systems involving non-linear effects such as clipping. We show that the capacity approaching property can still be maintained when generalized AMP is used to decode the message. To approach the capacity, a low-rate underlying code should be designed according to the curve matching principle, which is complicated in practice. Instead, analog spatial-coupling is used to avoid sophisticated low-rate code design. In the end, we study the coupled scheme in a multiuser environment, where analog spatial-coupling can be realized in a distributive way. The overall block length can be shared by many users, which reduces block length per-user.

## Multimode Integer-Forcing Receivers for Block Fading Channels

- **Status**: ❌
- **Reason**: MIMO integer-forcing 수신기 — LDPC/디코더/코드설계 무관
- **ID**: ieee:9194330
- **Type**: journal
- **Published**: Dec. 2020
- **Authors**: Daeyeol Yang, Kyeongcheol Yang
- **PDF**: https://ieeexplore.ieee.org/document/9194330
- **Abstract**: Integer-forcing (IF) receivers are a class of linear multiple-input multiple-output (MIMO) receivers to achieve near-optimal performance under quasi-static channels, with almost the same complexity as that of conventional linear receivers. Instead of trying to recover the transmitted messages directly, an IF receiver recovers their integer-linear combinations corresponding to a chosen integer-valued effective channel matrix, and then obtains them. Recently, the IF strategy has been extended to a block fading scenario. In this paper, we propose a novel IF receiver for block fading channels, called a multimode IF (M-IF) receiver. Unlike conventional IF receivers, the proposed M-IF receiver employs several integer-valued effective channel matrices for IF decoding. We also propose an efficient search algorithm for selecting such matrices with the aid of Gaussian elimination. We then show that for any channel realizations, the proposed M-IF receiver has better performance in terms of the effective noise variance than conventional IF receivers. Simulation results demonstrate that it works really well in various environments.

## On the Achievable Rate of MISO Fading Channels With Instantaneous CSI Only at the Transmitter

- **Status**: ❌
- **Reason**: MISO fading 달성률 이론 — LDPC/디코더/HW 무관
- **ID**: ieee:9154421
- **Type**: journal
- **Published**: Dec. 2020
- **Authors**: Majid Nasiri Khormuji, Peng Wang, Mohammad Javad Emadi +1
- **PDF**: https://ieeexplore.ieee.org/document/9154421
- **Abstract**: We investigate Multiple-Input Single-Output (MISO) fading channels with perfect instantaneous Channel State Information (CSI) at the transmitter and with statistical average CSI at the receiver. We outline achievable rates for maximum ratio transmission and show that the rate loss of not having instantaneous CSI at the receiver behaves like an additional noise term whose variance is equal to one fourth of the transmit power. Similar results are obtained for equal gain transmission. The simulation results are in agreement with the theoretical bounds and indicate that requirement of instantaneous CSI at the receiver becomes obsolete up to a certain transmit power.

## Fully Parallel Circular-Shift Rotation Network for Communication Standards

- **Status**: ✅
- **Reason**: D: 새 permutation network(circular-shift rotation) HW 설계 — QC-LDPC 디코더에 이식 가능
- **ID**: ieee:9099895
- **Type**: journal
- **Published**: Dec. 2020
- **Authors**: Hassan Harb, Cyrille Chavet
- **PDF**: https://ieeexplore.ieee.org/document/9099895
- **Abstract**: This brief sheds light on a formal approach to design an innovative class of permutation network called Fully Parallel Circular-shift rotation Network. Thus, the contribution of such a design is the capability to process - in parallel - more than one set of elements with different lengths and permutation constraints. Yet, processing several sets simultaneously, arises from the increasing demand for higher throughput rate for applications such as the incoming 5G codes. Furthermore, the ability to handle several different sets of elements in parallel reduces the number of idled components in the designs (which improves the $performances/area$ ratio). Meanwhile, independent circular-shifter network blocks are generated in order to process the different sets simultaneously. Hence, the cost in terms of number of Multiplexers (MUXs) is low compared to the best existing works we know in the state-of-the-art, with the same number of stages.

## Corrections to “The ADMM Penalized Decoder for LDPC Codes” [Jun 16 2966-2984]

- **Status**: ❌
- **Reason**: ADMM 페널라이즈 디코더 보정(typo/lemma 정정)일 뿐 새 기법 없음 — 단순 정오표
- **ID**: ieee:9217439
- **Type**: journal
- **Published**: Dec. 2020
- **Authors**: Haoyuan Wei, Xishuo Liu, Stark C. Draper
- **PDF**: https://ieeexplore.ieee.org/document/9217439
- **Abstract**: A correction is made in the statement and proof of a lemma used to prove codeword symmetry. In addition, an important typo is noted and corrected.

## A Reconstruction-Computation-Quantization (RCQ) Approach to Node Operations in LDPC Decoding

- **Status**: ✅
- **Reason**: LDPC 유한정밀(4비트) RCQ 디코더 + HDQ 양자화 설계 — min-sum/BP 근사 디코더 및 LLR 양자화 기법, NAND 이식성 높음(C/A).
- **ID**: ieee:9348139
- **Type**: conference
- **Published**: 7-11 Dec. 
- **Authors**: Linfang Wang, Richard D. Wesel, Maximilian Stark +1
- **PDF**: https://ieeexplore.ieee.org/document/9348139
- **Abstract**: This paper proposes a finite-precision decoding method for low-density parity-check (LDPC) codes that features the three steps of Reconstruction, Computation, and Quantization (RCQ). Unlike Mutual-Information-Maximization Quantized Belief Propagation (MIM-QBP), RCQ can approximate either belief propagation or Min-Sum decoding. MIM-QBP decoders do not work well when the fraction of degree-2 variable nodes is large. However, sometimes a large fraction of degree-2 variable nodes is used to facilitate a fast encoding structure, as seen in the IEEE 802.11 standard and the DVB-S2 standard. In contrast to MIM-QBP, the proposed RCQ decoder may be applied to any off-the-shelf LDPC code, including those with a large fraction of degree-2 variable nodes. Simulations show that a 4-bit Min-Sum RCQ decoder delivers frame error rate (FER) performance within 0.1 dB of floating point belief propagation (BP) for the IEEE 802.11 standard LDPC code in the low SNR region. The RCQ decoder actually outperforms floating point BP and Min-Sum in the high SNR region were FER less than 10-5. This paper also introduces Hierarchical Dynamic Quantization (HDQ) to design the time-varying non-uniform quantizers required by RCQ decoders. HDQ is a low-complexity design technique that is slightly sub-optimal. Simulation results comparing HDQ and optimal quantization on the symmetric binary-input memoryless additive white Gaussian noise channel show a mutual information loss of less than 10-6 bits, which is negligible in practice.

## SPARC-LDPC Coding for MIMO Massive Unsourced Random Access

- **Status**: ❌
- **Reason**: SPARC+LDPC를 MIMO 비소스 랜덤액세스에 응용, LDPC는 BP+SIC의 베이스라인일 뿐 떼어낼 새 ECC 기법 없음 — 무선 응용 특이적
- **ID**: ieee:9367450
- **Type**: conference
- **Published**: 7-11 Dec. 
- **Authors**: Tianya Li, Yongpeng Wu, Mengfan Zheng +2
- **PDF**: https://ieeexplore.ieee.org/document/9367450
- **Abstract**: A joint sparse-regression-code (SPARC) and low-density-parity-check (LDPC) coding scheme for multiple-input multiple-output (MIMO) massive unsourced random access (U- RA) is proposed in this paper. Different from the state-of-theart covariance based maximum likelihood (CB-ML) detection scheme, we first split users' messages into two parts. The former part is encoded by SPARCs and tasked to recover part of the messages, the corresponding channel coefficients as well as the interleaving patterns by compressed sensing. The latter part is coded by LDPC codes and then interleaved by the interleave-division multiple access (IDMA) scheme. The decoding of the latter part is based on belief propagation (BP) joint with successive interference cancellation (SIC). Numerical results show our scheme outperforms the CB-ML scheme when the number of antennas at the base station is smaller than that of active users. The complexity of our scheme is with the order $\mathcal{O}(2^{B_{p}}ML+\hat{K}ML)$ and lower than the CB-ML scheme. Moreover, our scheme has higher spectral efficiency (nearly 15 times larger) than CB-ML as we only split messages into two parts.

## MCMC Decoding of LDPC Codes with BP Preprocessing

- **Status**: ✅
- **Reason**: 단블록 LDPC용 BP-MCMC 하이브리드 디코더 — 새 디코더 알고리즘 기여(C). 바이너리.
- **ID**: ieee:9348002
- **Type**: conference
- **Published**: 7-11 Dec. 
- **Authors**: Jiun-Ting Huang, Young-Han Kim
- **PDF**: https://ieeexplore.ieee.org/document/9348002
- **Abstract**: Monte Carlo Markov chain (MCMC) decoding is a randomized algorithm which has been proven to be near-optimal in terms of decoding error probability. However, the exponentially slow mixing rate of Markov chains seems to preclude MCMC decoding from applications concerning even short blocklength codes. In contrast, belief propagation (BP) is a deterministic algorithm that is empirically fast but sub-optimal in error rate when it is used to decode low-density parity-check (LDPC) codes. In this paper, a code-independent BP-MCMC hybrid decoder is devised for short-blocklength LDPC codes. Theoretical error analysis of the hybrid algorithm is provided. Preliminary experiments show that the preprocessing of BP successfully reduces the time complexity of MCMC decoding and hence significantly improves the applicability of MCMC decoders to short LDPC codes.

## On the Design of Generalized LDPC Codes with Component BCJR Decoding

- **Status**: ✅
- **Reason**: GLDPC 코드 설계 + trellis BCJR 비트단위 컴포넌트 디코더 최적화로 새 코드설계/디코더 기여(E/C). 바이너리.
- **ID**: ieee:9322143
- **Type**: conference
- **Published**: 7-11 Dec. 
- **Authors**: Yanfang Liu, Pablo M. Olmos, David G. M. Mitchell
- **PDF**: https://ieeexplore.ieee.org/document/9322143
- **Abstract**: Generalized low-density parity-check (GLDPC) codes, where the single parity-check (SPC) nodes are replaced by generalized constraint (GC) nodes, are known to offer a reduced gap to capacity when compared with conventional LDPC codes, while also maintaining linear growth of minimum distance. However, for certain classes of practical GLDPC codes, there remains a gap to capacity even when utilizing blockwise decoding algorithm at GC nodes. In this work, we propose to optimize the design of GLDPC codes where the GC nodes are decoded with a trellis-based bit-wise Bahl-Cocke-Jelinek- Raviv (BCJR) component decoding algorithm. We analyze the asymptotic threshold behavior of GLDPC codes and determine the optimal proportion of the GC nodes in the GLDPC Tanner graph.We show significant performance improvements compared to existing designs with the same order of decoding complexity.

## Fast SD-Hamming Decoding in FPGA for High-Speed Concatenated FEC for Optical Communication

- **Status**: ❌
- **Reason**: 광통신용 SD-Hamming(Chase/MAP) FPGA 디코더 — LDPC 아님, NAND ECC 이식 기법 없음.
- **ID**: ieee:9322436
- **Type**: conference
- **Published**: 7-11 Dec. 
- **Authors**: Can Zhang, Søren Forchhammer, Jakob Dahl Andersen +3
- **PDF**: https://ieeexplore.ieee.org/document/9322436
- **Abstract**: In this paper, we consider fast decoding of soft-decision (SD) Hamming codes as inner codes in concatenated forward error-correction (FEC) schemes for high-speed optical communication. The goal is single FPGA implementations at speeds of 400 Gb/s and beyond. A low complexity maximum a posteriori (MAP) probability decoding is applied to a (128,120) Hamming code. Chase decoding of a (128,119) Hamming code is also implemented. The VHDL designs for both decoding schemes are presented. The FEC performance and FPGA resource utilization are investigated and compared. Synthesis results indicate that, both the Chase and the MAP decoder leave sufficient resources available to also accommodate a powerful outer hard decision code, on a single FPGA. Furthermore, MAP decoding of (128,120) Hamming code features lower hardware complexity and provides a higher data throughput.

## Simplified Decoding of Polar Codes by Identifying Reed-Muller Constituent Codes

- **Status**: ❌
- **Reason**: polar SC 디코딩에서 Reed-Muller 구성부호 식별 — polar 트리 특이적, NAND LDPC로 이식할 기법 없음
- **ID**: ieee:9321979
- **Type**: conference
- **Published**: 7-11 Dec. 
- **Authors**: Nadim Ghaddar, Hamid Saber, Hsien-Ping Lin +2
- **PDF**: https://ieeexplore.ieee.org/document/9321979
- **Abstract**: The throughput of successive cancellation decoding of polar codes can be improved through simplified decoders that identify specific constituent codes in the decoding tree. The identified codes include rate-0, rate-1, repetition, and single parity-check codes. In this work, constituent codes that belong to the family of first-order Reed-Muller codes, and their sub-codes, are also identified in the decoding tree. Alternative decoding schemes that utilize the structure of Reed-Muller codes are incorporated into successive cancellation decoding. Simulation results show that such an approach can improve both the block error rate performance as well as the decoding latency of polar codes.

## Approximated EM Algorithms for Estimation of Unknown Coded Discrete Memoryless Channels

- **Status**: ✅
- **Reason**: 플래시 메모리 채널(양자화 Normal-Laplace) 대상 LDPC sum-product/min-sum 기반 채널추정 근사 — NAND 채널 직접+min-sum 변형(A/C).
- **ID**: ieee:9322183
- **Type**: conference
- **Published**: 7-11 Dec. 
- **Authors**: Naoaki Kokubun, Daiki Watanabe, Hironori Uchikawa +1
- **PDF**: https://ieeexplore.ieee.org/document/9322183
- **Abstract**: Mismatch between the true channel and the channel assumed in the design of a communication system can degrade system performance. Joint channel estimation and data recovery via the Expectation-Maximization (EM) algorithm can overcome this problem. Though stable, the EM algorithm can be complex to implement and can exhibit slow convergence. We present approximations of the EM algorithm that reduce computational complexity and accelerate convergence for LDPC-coded discrete memoryless channels. In place of the exact bit-wise maximum a posteriori probability decoder in the E step of the EM algorithm, we use the sum-product decoder and min-sum decoder. In the M step, we use hard information instead of soft information to estimate the channel parameter. In order to evaluate the approximations in a practical channel mismatch scenario, we use a flash memory channel described by a quantized Normal-Laplace mixture model. The simulation results demonstrate that the approximations in the E step can estimate the true channel with low-complexity decoding and those in the M step can accelerate the convergence with reduced measurement precision.

## Average Age of Information of Irregular Repetition Slotted ALOHA

- **Status**: ❌
- **Reason**: IRSA random access의 AoI 분석 — 접속 프로토콜 성능 이론, 떼어낼 LDPC 디코더/HW 기법 없음.
- **ID**: ieee:9322355
- **Type**: conference
- **Published**: 7-11 Dec. 
- **Authors**: Andrea Munari, Alexey Frolov
- **PDF**: https://ieeexplore.ieee.org/document/9322355
- **Abstract**: Flanking traditional metrics such as throughput and reliability, age of information (AoI) is emerging as a fundamental tool to capture the performance of IoT systems. In this context, we focus on a setup in which a large number of nodes attempt delivery of time-stamped updates to a common destination over a shared channel, and investigate the ability of different grant-free access strategies to maintain fresh information at the receiver. Specifically, we derive for the first time an exact closed-form expression of the average AoI achieved by irregular repetition slotted ALOHA (IRSA), and compare its performance to that of a slotted ALOHA approach. Our analysis reveals the potential of modern random access schemes, and pinpoints some fundamental trade-offs, providing useful hints for proper system design.

## Refined Belief-Propagation Decoding of Quantum Codes with Scalar Messages

- **Status**: ✅
- **Reason**: 양자코드용 BP지만 스칼라 메시지로 binary BP 복잡도 달성+message normalization+serial schedule 개선 — 고전 바이너리 BP에서 유래한 이식 가능 디코더 기법(C), 예외 포함
- **ID**: ieee:9367482
- **Type**: conference
- **Published**: 7-11 Dec. 
- **Authors**: Kao-Yueh Kuo, Ching-Yi Lai
- **PDF**: https://ieeexplore.ieee.org/document/9367482
- **Abstract**: Codes based on sparse matrices have good performance and can be efficiently decoded by belief-propagation (BP). Decoding binary stabilizer codes needs a quaternary BP for (additive) codes over GF(4), which has a higher check-node complexity compared to a binary BP for codes over GF(2). Moreover, BP decoding of stabilizer codes suffers a performance loss from the short cycles in the underlying Tanner graph. In this paper, we propose a refined BP algorithm for decoding quantum codes by passing scalar messages. For a given error syndrome, this algorithm decodes to the same output as the conventional quaternary BP but with a check-node complexity the same as binary BP. As every message is a scalar, the message normalization can be naturally applied to improve the performance. Another observation is that the message-update schedule affects the BP decoding performance against short cycles. We show that running BP with message normalization according to a serial schedule (or other schedules) may significantly improve the decoding performance and error-floor in computer simulation.

## Performance of Coded MIMO Spatial Modulation with Scaling Matched-Filter Detector

- **Status**: ❌
- **Reason**: MIMO 공간변조 검출기(scaling MF) 연출력 — 무선 검출 특이적, 떼어낼 LDPC 기법 없음.
- **ID**: ieee:9347961
- **Type**: conference
- **Published**: 7-11 Dec. 
- **Authors**: Yuto Hama, Hideki Ochiai
- **PDF**: https://ieeexplore.ieee.org/document/9347961
- **Abstract**: Spatial modulation (SM) exploits multiple transmit antennas for index modulation and thus alleviates the complexity issues inherent in the conventional MIMO schemes. Even though a significant amount of studies have been devoted to SM, its coded performance combined with low-complexity linear detectors has not been well investigated. In this work, we propose a practical low-complexity SM approach based on the combination of the scaling matched-filter (MF) detector and capacity-approaching channel codes. The scaling MF detector is sub-optimal but can be implemented with significantly less complexity than the maximum likelihood (ML) detector. The major challenge in the design of detectors for coded SM is how to calculate the soft output corresponding to the coded bits associated with index modulation that will be processed by the subsequent binary channel decoder, and we develop suitable soft output metrics based on the theoretical analysis of the associated scaling MF detector output. Through computer simulations, the effectiveness of our proposed coded SM system is demonstrated.

## Communication-Channel Optimized Impurity Partition

- **Status**: ❌
- **Reason**: DMC용 양자화/분류기 설계(impurity partition) — 소스 양자화 영역, 채널코딩 ECC 디코더 기법 아님.
- **ID**: ieee:9322342
- **Type**: conference
- **Published**: 7-11 Dec. 
- **Authors**: Thuan Nguyen, Thinh Nguyen
- **PDF**: https://ieeexplore.ieee.org/document/9322342
- **Abstract**: Given an original discrete source X with the distribution pX that is corrupted by noise to produce a noisy data Y with the given joint distribution p(X,Y). A quantizer/classifier Q : Y → Z is then used to classify/quantize Y to a discrete partitioned output Z having probability distribution pZ. Next, Z is transmitted over a discrete memoryless channel (DMC) with a given channel matrix A that produces the final discrete output T . One wants to design an optimal quantizer/classifier Q* to minimize the end-to-end impurity/cost function F(X, T) between the input X and the final output T. Our result generalizes some previous results. First, an iteration linear time complexity algorithm is proposed to find the locally optimal quantizer. Second, we show that the optimal quantizers produce the hard partitions that are equivalent to the cuts by hyper-planes in the space of the posterior distribution pX|Y. This result provides a polynomial-time complexity algorithm to find the globally optimal quantizer. Finally, in the special case where the source X is binary, an efficient algorithm is proposed to find the truly global optimal partition.

## Low-Complexity Iterative Soft-output Demodulation for Hierarchical Quadrature Amplitude Modulation

- **Status**: ❌
- **Reason**: HQAM 무선용 저복잡도 연복조/디매핑 — LDPC 아닌 변조 특이적, 떼어낼 ECC 기법 없음.
- **ID**: ieee:9322213
- **Type**: conference
- **Published**: 7-11 Dec. 
- **Authors**: Daniel Kekrt, Zdenek Becvar
- **PDF**: https://ieeexplore.ieee.org/document/9322213
- **Abstract**: This paper proposes a novel design of low-complexity soft-output demodulation and soft-output demapping for multi-level iterative decoding of any double-binary code and high-order hierarchical quadrature amplitude modulation (HQAM) schemes. The proposed solution exploits two techniques of self-interference cancellation. The fist one, a blind successive self-interference cancellation, provides a coarse synchronization in an acquisition mode of a receiver. The second one, a hard decision directed parallel self-interference cancellation, is exploited in a tracking mode. The proposed solution is of a very low complexity corresponding only to QPSK demodulation even for modulations of higher orders. Such low complexity allows an efficient implementation of HQAM in mobile and wireless networks with no signaling or coordination between transmitter and receiver required for a selection of modulation. Thus, the proposed approach is suitable for many up-to-date solutions including communication via drones, transparent relaying, or device-to-device communication. The designed solution is verified via a reference implementation of 256-HQAM scheme in FPGA. The results confirm a suitability of the proposed scheme for HQAM demodulation and show that a low bit error rate is achieved by the proposed solution in a wide range of signal to noise ratio.

## Achieving Ordered Data Block Delivery in CCSDS-DTN Space Networks: a Case Study

- **Status**: ❌
- **Reason**: CCSDS-DTN 우주망 순서 전달 프로토콜 성능 모델 — ECC/LDPC 무관.
- **ID**: ieee:9322634
- **Type**: conference
- **Published**: 7-11 Dec. 
- **Authors**: Tomaso de Cola
- **PDF**: https://ieeexplore.ieee.org/document/9322634
- **Abstract**: Future space missions are expected to implement a fully compliant CCSDS-DTN protocol stack in order to exploit the intrinsic store-forward capabilities. DTN technology, however, is not aimed at providing ordered data delivery, which is instead delegated to the application layer. More recently, the Delay-Tolerant Payload Conditioning (DTPC) has been introduced into the DTN protocol suite in order to mitigate such a limitation, although its interactions with application layer and the rest of the CCSDS protocol stack are not completely understood. To this end, this paper proposes a theoretical model for thoroughly investigating the performance of file-based data transfer through a CCSDS-DTN protocol architecture. A qualitative performance analysis allowed to summarise some important findings about overall protocols' configuration and the related impact on the overall system performance.

## Spatial Coupling In Turbo Equalization

- **Status**: ✅
- **Reason**: 스페이셜 커플링(SC) 코드로 waterfall/error-floor 트레이드오프 해소, window decoder 활용 — E(코드설계) 이식 가능, 바이너리 LDPC 계열
- **ID**: ieee:9348218
- **Type**: conference
- **Published**: 7-11 Dec. 
- **Authors**: Mgeni Makambi Mashauri, Michael Lentmaier
- **PDF**: https://ieeexplore.ieee.org/document/9348218
- **Abstract**: In this paper we consider spatial coupling in turbo equalization and demonstrate that the code design trade-off between the performance in waterfall and error floor regions can be avoided. We introduce three coupling schemes and compare their performances, where the first method introduces coupling between the encoder and the channel, while the second uses a spatially coupled (SC) code. In the third scheme we use both a coupled code and couple between the code and the channel. We show by computer simulations that, with spatial coupling, we can have good performance in both the error floor and the waterfall region with reasonable decoding latency by using a window decoder. We show this for both the maximum a posteriori (MAP) and linear minimum mean square (MMSE) equalizers.

## An Evaluation of Design Framework for Min-Sum Irregular LDPC Decoders

- **Status**: ✅
- **Reason**: Min-Sum 비정칙 LDPC 디코더의 범용 설계 프레임워크+회로면적 절감 — D(HW 아키텍처) 이식 가능
- **ID**: ieee:9306369
- **Type**: conference
- **Published**: 7-10 Dec. 
- **Authors**: Jimpu Suzuki, Hiroshi Tsutsui, Takeo Ohgane
- **PDF**: https://ieeexplore.ieee.org/document/9306369
- **Abstract**: Design of LDPC decoder depends on its check matrix. Since there exist a lot of check matrices with various sizes, it is not feasible to design a dedicated LDPC decoder for each check matrix. This work aims to make a versatile design framework to generate an LDPC decoder for each given check matrix. We consider a method to reduce the circuit area, focusing on the feature of the check matrix of 5G. In this paper, we present evaluation results of our framework, including gate count evaluations. We evaluated circuit areas of the decoders conforming to 5G. In the case of a check matrix where the number of information bits is about 120, the number of gates is about 3.7 M gates.

## Packet Aggregation Based on Encryption-Then-Compression for Highly Efficient Multi-Hop Transmission

- **Status**: ❌
- **Reason**: 암호화-후-압축 패킷 집약 기법, 채널코딩 ECC 아님(소스 코딩/보안)
- **ID**: ieee:9306344
- **Type**: conference
- **Published**: 7-10 Dec. 
- **Authors**: Ryota Yatsu, Takanori Hara, Koji Ishibashi +2
- **PDF**: https://ieeexplore.ieee.org/document/9306344
- **Abstract**: In this paper, we tackle a critical bottleneck problem appeared in multi-hop transmissions; only a single node can forward packets from the other nodes in the network to a common destination. Since every node encrypts data before transmission for privacy protection, typical compression techniques cannot be applied to the aggregated packet. We hence propose the packet aggregation based on encryption-then-compression (EtC) technique enabling the efficient compression of the encrypted data. Assuming intermittent receiver-driven data transmission (IRDT) as a multi-hop transmission protocol, numerical results show that our proposed method can achieve the lower decompression error probability than the conventional EtC and significantly reduce the energy consumption per a correctly received packet.

## Coded Modulation for Four-Dimensional Signal Constellations with Concatenated Non-Binary Forward Error Correction

- **Status**: ❌
- **Reason**: 비이진(non-binary) LDPC 기반 4D coded modulation — 비이진 LDPC는 즉시 제외
- **ID**: ieee:9333330
- **Type**: conference
- **Published**: 6-10 Dec. 
- **Authors**: Sebastian Stern, Masoud Barakatain, Felix Frey +3
- **PDF**: https://ieeexplore.ieee.org/document/9333330
- **Abstract**: A concatenated coded-modulation scheme for 4D constellations is proposed that consists of an inner complexity-optimized non-binary LDPC code and an outer zipper code. The related packing, shaping, and coding gains reduce the required SNR by 1 dB over conventional BICM with DP-16QAM.

## After FEC Performance of 50G PON with Deep Neural Network Equalization

- **Status**: ❌
- **Reason**: DNN equalization before LDPC FEC in 50G PON; LDPC is baseline only, equalization is the contribution, no portable ECC technique
- **ID**: ieee:9333249
- **Type**: conference
- **Published**: 6-10 Dec. 
- **Authors**: Amitkumar Mahadevan, Vincent Houtsma, Noriaki Kaneda +1
- **PDF**: https://ieeexplore.ieee.org/document/9333249
- **Abstract**: Performance of Deep Neural Network receiver equalization is investigated after LDPC FEC. It is shown that DNN equalization results in a lower level of error clustering and higher performing equalization relative to more traditional equalization for bandwidth-limited and dispersion-limited channels for 50G PON.

## NN-based PCS distribution optimization for practical channels

- **Status**: ❌
- **Reason**: NN 기반 확률 성형(PCS) 분포 최적화, LDPC 디코더/코드설계 기법 없음
- **ID**: ieee:9333286
- **Type**: conference
- **Published**: 6-10 Dec. 
- **Authors**: Xueyang Li, Zhenping Xing, Md Samiul Alam +3
- **PDF**: https://ieeexplore.ieee.org/document/9333286
- **Abstract**: We propose an optimization scheme for the distribution of probabilistically shaped signals in practical non-AWGN channels based on a neural network and genetic algorithm. The optimized input distribution enables 23.5% higher throughput than the Maxwell-Boltzmann distribution in a short reach channel with a SiP transmitter.

## Single-channel 1.61 Tb/s Optical Coherent Transmission Enabled by Neural Network-Based Digital Pre-Distortion

- **Status**: ❌
- **Reason**: NN-based digital pre-distortion for optical transmitter; no LDPC/ECC technique to port
- **ID**: ieee:9333267
- **Type**: conference
- **Published**: 6-10 Dec. 
- **Authors**: Vinod Bajaj, Fred Buchali, Mathieu Chagnon +2
- **PDF**: https://ieeexplore.ieee.org/document/9333267
- **Abstract**: We propose a novel digital pre-distortion (DPD) based on neural networks for high-baudrate optical coherent transmitters. We demonstrate experimentally that it outperforms an optimized linear DPD giving a 1.2 dB SNR gain in a 128GBaud PCS-256QAM single-channel transmission over 80km of standard single-mode fiber resulting in a record 1.61 Tb/s net data rate.

## Fast Convergence by Machine Learning Optimizer for Adaptive MIMO Equalizer Used in SDM Transmission over Coupled-Core 4-Core Fiber and 4-Core EDFA

- **Status**: ❌
- **Reason**: SDM 전송용 MIMO 이퀄라이저 ML 최적화, LDPC ECC 기법 없음
- **ID**: ieee:9333396
- **Type**: conference
- **Published**: 6-10 Dec. 
- **Authors**: Manabu Arikawa, Hidemi Noguchi
- **PDF**: https://ieeexplore.ieee.org/document/9333396
- **Abstract**: We applied several optimizers from the machine learning field to an adaptive MIMO equalizer for SDM transmission. We experimentally compared their convergence properties in a SDM transmission over a 52-km coupled-core 4-core fiber and 4-core EDFA and showed over 22% faster convergence with Adam.

## Experimental Quantification of Implementation Penalties from Laser Phase Noise for Ultra-High-Order QAM Signals

- **Status**: ❌
- **Reason**: Experimental QAM laser phase-noise tolerance; no LDPC/ECC content
- **ID**: ieee:9333253
- **Type**: conference
- **Published**: 6-10 Dec. 
- **Authors**: Xi Chen, Junho Cho, Di Che
- **PDF**: https://ieeexplore.ieee.org/document/9333253
- **Abstract**: We experimentally characterize ultra-high order QAM (256-, 1024-, and 4096- QAM) signals' tolerance to laser phase noise. The studied phase noise covers a wide range from 200 Hz to 10 MHz.

## Challenges in Coding, DSP and Parallel Operation of Quantum Key Distribution and Coherent Data Transmission

- **Status**: ❌
- **Reason**: QKD coding/DSP challenges; quantum key distribution, no classical binary LDPC technique to port
- **ID**: ieee:9333170
- **Type**: conference
- **Published**: 6-10 Dec. 
- **Authors**: Tobias A. Eriksson, Ruben S. Luís, Georg Rademacher +9
- **PDF**: https://ieeexplore.ieee.org/document/9333170
- **Abstract**: We discuss challenges and recent progress on coding, digital signal processing and joint transmission with classical data channels, for quantum key distribution.

## Sparse-Dense MLC for Peak Power Constrained Channels

- **Status**: ❌
- **Reason**: Sparse-dense MLC coded modulation for peak-power optical channels; modulation technique, no portable binary LDPC ECC
- **ID**: ieee:9333148
- **Type**: conference
- **Published**: 6-10 Dec. 
- **Authors**: Tsuyoshi Yoshida, Koji Igarashi, Magnus Karlsson +1
- **PDF**: https://ieeexplore.ieee.org/document/9333148
- **Abstract**: Probabilistic amplitude shaping with Maxwell-Boltzmann distributions can degrade system budgets due to a large peak-to-average power ratio at a low spectral efficiency and at a short reach transmission with few optical amplifiers. We propose a novel coded modulation technique, which is useful in such scenarios.

## LDPC Code based Pseudonym Scheme for Vehicular Networks

- **Status**: ❌
- **Reason**: 차량 네트워크 익명 인증 가명 스킴, LDPC를 credential 인코딩에 응용한 보안 기법 — ECC 디코더/코드설계 기여 없음
- **ID**: ieee:9409462
- **Type**: conference
- **Published**: 4-6 Dec. 2
- **Authors**: Jin Zhou, Changsong Zheng, Yuedi Li +3
- **PDF**: https://ieeexplore.ieee.org/document/9409462
- **Abstract**: In this paper, an innovative pseudonym scheme based on Direct Anonymous Attestation (DAA) and Low-Density Parity-Check (LDPC) is proposed. For the sake of improving the efficiency of generating pseudonyms, the proposed scheme uses the LDPC code to encode the credential to produce more available versions. To detect whether a vehicle's On-Board Unit (OBU) is compromised, the proposed scheme grants the Revocation Authority (RA) to check if the compromised OBU uses a revoked pseudonym. Compared with the existing pseudonym scheme, the proposed scheme has a higher level of security and lower computation overhead.

## Design of Time-Invariant SC-LDPC Codes Based on PEG Algorithm

- **Status**: ❌
- **Reason**: PEG 기반 SC-LDPC 구성+CPM으로 4/6-cycle 제거; 교과서 수준 girth/cycle 제거의 표준 조합으로 새 기여 미미하나 SC-LDPC 신규 coupling 알고리즘 주장이라 애매—그러나 표준 PEG+CPM 재사용 수준으로 판단해 제외
- **ID**: ieee:9398883
- **Type**: conference
- **Published**: 20-22 Dec.
- **Authors**: Xiang-Yi Shi, Dan-Feng Zhao, Hai Tian +1
- **PDF**: https://ieeexplore.ieee.org/document/9398883
- **Abstract**: In order to meet the reliability requirements of 6G mobile communication, this paper proposes a method of constructing time-invariant spatially coupled low-density parity-check (SC-LDPC) codes based on the progressive edge growth (PEG) algorithm. The base matrix for coupling is constructed by the PEG algorithm. We design a new coupling algorithm by constraining the coupling edges, and use circular permutation matrix (CPM) algorithm to eliminate 4-cycles and reduce the number of 6-cycles. Compared to 5G NR LDPC codes, simulation results show the design has obvious coding gain over AWGN channel.

## Constellation Design with Equal-probability Partition of a Cropped Gaussian Distribution

- **Status**: ❌
- **Reason**: PAM constellation 설계(변조); ECC/LDPC 무관
- **ID**: ieee:9348432
- **Type**: conference
- **Published**: 18 Nov.-16
- **Authors**: Brett Wiens, Daniel C. Lee
- **PDF**: https://ieeexplore.ieee.org/document/9348432
- **Abstract**: In this paper, we present a method of constructing PAM constellations with non-uniform spacing by determining the symbol amplitudes based on warping the uniform distancing by applying the inverse error function. The construction method can adapt to symbol energy (SNR) constraints by adjusting one parameter. This parameter determines the degree of separation of the outermost pair of constellation symbols from the inner symbols and the degree of spacing uniformity. Optimization of this parameter is discussed for maximizing the equiprobable mutual information of the channel having the constellation. The equiprobable mutual information of the constellation constructed by the suggested method is compared against the uniform spacing and the Gaussian approximated spacing, which asymptotically approaches the AWGN capacity.

## Analysis of Non-binary Polar Codes over GF(3) and GF(5) with Phase Shift Keying for Short Messages

- **Status**: ❌
- **Reason**: 비이진 polar code(GF(3)/GF(5)) 분석; 비-LDPC이며 비이진, 원칙 제외
- **ID**: ieee:9348796
- **Type**: conference
- **Published**: 18 Nov.-16
- **Authors**: Melanie Falk, Gerhard Bauch, Ivor Nissen
- **PDF**: https://ieeexplore.ieee.org/document/9348796
- **Abstract**: In this work, non-binary polar codes are investigated for input alphabets sizes being a prime number. The similarities and differences in the encoding and decoding process are shown with respect to binary polar codes. The performance of polar codes over GF(3) and GF(5) in combination with 3-PSK and 5-PSK is evaluated for short messages in comparison to binary polar codes with common phase shift keying constellations.

## Novel Pilot Allocation Random Access Protocol for Integrated Terrestrial-Satellite Networks

- **Status**: ❌
- **Reason**: 무선 위성-지상망 랜덤액세스 파일럿 할당 프로토콜; LDPC 무관, 떼어낼 ECC 기법 없음
- **ID**: ieee:9348758
- **Type**: conference
- **Published**: 18 Nov.-16
- **Authors**: Liang Xu, Jian Jiao, Fei Wang +3
- **PDF**: https://ieeexplore.ieee.org/document/9348758
- **Abstract**: In this paper, we propose a novel pilot allocation with desired reliability (PA-DR) random access protocol for integrated terrestrial-satellite network (ITSN). ITSN is regarded as an effective solution to achieve massive connectivity and ubiquitous coverage in future communication systems. To provide massive machine type communications (mMTC) to a backbone satellite in ITSN, the dense user equipments (UEs) are permitted to jointly transmit randomly chosen pilot sequences along with their data packets over multi-slot in our PA-DR random access protocol, which allows for the potential performance gain in resolving more intra-cell pilot collisions with high probability. By utilizing the finite length analysis of pilot allocation over muti-slot, we derive the closed-form expressions to the access failure probability and system throughout in the finite length regime, which is highly desired for practical-interest ITSN. With the help of the derived expressions, we propose a guideline for mMTC ITSN that target on satisfying desired reliability of UEs, and optimize the number of allocated pilots and minimum access latency under diverse access failure probability requirements. In addition, simulation results show that our PA-DR random access protocol outperforms the existing protocols in achieving high throughput and shortening the access latency.

## Deep Generative Model based Channel Agnostic Communication System for Efficient Data Transmission

- **Status**: ❌
- **Reason**: GAN 기반 채널 비종속 통신/대역폭 절감; LDPC ECC 무관
- **ID**: ieee:9328992
- **Type**: conference
- **Published**: 17-18 Dec.
- **Authors**: S Yogeeshwar, B S Vishwath Kumar, Velmathi Guruviah +1
- **PDF**: https://ieeexplore.ieee.org/document/9328992
- **Abstract**: In this modern era, where there is a great shift in momentum towards AI and data science, data-driven approach has substantiated to have diverse talents. This type of approach specifically in the field of wireless communication has proven to be highly efficient in modelling an end to end wireless communication channel with a completely unknown channel state information (CSI). Though there has been some work done in this direction they are not focusing on high dimension data like audio and image. Further with the tremendous growth in multimedia technologies and with higher resolution data being transmitted, there is an increasing need for bandwidth. Hence in this paper, we propose a novel idea where a Conditional Generative Adversarial Network is used to represent the channel effects of an end to end wireless communication channel which adapts to different noise levels with having the memory of the channel state information (CSI). Further to address this issue with bandwidth, Variational Adversarial Network is used where the input data is encoded into a condensed latent space and impacted with noise which is then passed through a Generative Adversarial Network which would be able to extract the original information. This reduces a lot of bandwidth and thereby increasing the overall data rate. To strengthen our proposal, we provide a comparative analysis with our conditional GAN and with extensive experiment results with both quantitative and qualitative analysis on images and voice signals.

## Poster: Performance analysis of early HARQ retransmission scheme in highway environments

- **Status**: ❌
- **Reason**: Early-HARQ retransmission in highway V2X; channel-estimation/HARQ study, no LDPC ECC technique
- **ID**: ieee:9318354
- **Type**: conference
- **Published**: 16-18 Dec.
- **Authors**: Yusaku Shiomitsu, Eiji Okamoto, Manabu Mikami +1
- **PDF**: https://ieeexplore.ieee.org/document/9318354
- **Abstract**: Ultra-reliable and low-latency communication (URLLC) is one of the main requirements of the fifth-generation mobile communications system (5G), intended for realizing autonomous driving and telemedicine. We have proposed an early-feedback hybrid automatic repeat request (early HARQ) that provides high reliability and low latency. However, we have only studied at the link level with ideal channel estimation, and the performance in a more practical environment was not clear. In this paper, we use reference signals for channel estimation and evaluate the early HARQ in a highway environment. Through the numerical simulations, we show the superiority of the early HARQ under real conditions to a conventional closed-loop HARQ.

## Design and Implementation of Reconfigurable Integrated FPGA-based PSK Demodulator

- **Status**: ❌
- **Reason**: 재구성형 PSK 복조기 FPGA 설계, LDPC 디코더 아님
- **ID**: ieee:9345835
- **Type**: conference
- **Published**: 15-17 Dec.
- **Authors**: Seyedeh Fatemeh Ghamkhari, Shokrollah Karimian
- **PDF**: https://ieeexplore.ieee.org/document/9345835
- **Abstract**: In this paper, a new approach is presented for design of digital demodulator, which relies on use of highest demodulation order as a platform to simultaneously realize lower order demodulators, with minimum hardware resources and within a single integrated design. In doing so, an 8PSK demodulator is designed and reconfigured to QPSK demodulator by realizing suitable decision block. It is shown that this approach offers the possibility of reducing by about 40% the resource allocation required to implement the decision block. The proposed method can lead to higher performance with lower FPGA resources, meaning that higher number of processing blocks can be used for a given system. Implementation results of the digital demodulator on Virtex-7 485t FPGA from Xilinx are also presented to validate the approach and verify the results. This method can be adapted to other PSK and QAM demodulators as well.

## Performance of iterative Successive interference cancellation receiver for LDPC coded OTFS

- **Status**: ❌
- **Reason**: LDPC 코딩 OTFS용 SIC 수신기, LDPC는 베이스라인이고 떼어낼 디코더 기법은 OTFS 수신처리에 한정
- **ID**: ieee:9342760
- **Type**: conference
- **Published**: 14-17 Dec.
- **Authors**: Suvra Sekhar Das, Shashank Tiwari, Vivek Rangamgari +1
- **PDF**: https://ieeexplore.ieee.org/document/9342760
- **Abstract**: Orthogonal Time Frequency Space (OTFS) modulation is a recently developed transmission technology, where contellation symbols are placed in the delay Doppler lattice. It is shown in literature that, OTFS is more resilient to inter carrier interference than OFDM. However, the required signal processing complexity of OTFS at the receiver side is much higher than that of OFDM. In this work we present the performance of an iterative SIC receiver for LDPC coded OTFS based on a earlier developed MMSE receiver. It is observed that improvement up to 7.5 dB can be achieved using the proposed receiver. It is also shown that the proposed SIC receiver has lower complexity than a message passing receiver available in literature, yet provides comparable performance for lower order modulation and low SNR. For higher order modulations and at high SNR the proposed receiver achieves better reliability, i.e. coded block error rates up to 105, which is aligned with the higher reliability requirement of 6G mobile communication systems.

## Performance of Lossy P-LDPC Codes over GF(2)

- **Status**: ❌
- **Reason**: P-LDPC 손실 소스압축(rate-distortion), 채널 ECC가 아닌 소스코딩이라 제외
- **ID**: ieee:9310025
- **Type**: conference
- **Published**: 14-16 Dec.
- **Authors**: Yin Liu, Lin Wang, Huihui Wu +1
- **PDF**: https://ieeexplore.ieee.org/document/9310025
- **Abstract**: This paper presents a low complexity lossy compression algorithm with protograph LDPC codes (Lossy P-LDPC Codes) over GF(2), for binary symmetric sources. The proposed scheme takes a shuffled reinforced belief propagation (SRBP) algorithm for encoding, which achieves asymptotically the theoretical rate-distortion function. Additionally, the proposed coding algorithm converges fast and performs very close to the counterparts using ultra sparse LDPC codes over GF(256). Simulation results also reveal that the code structures need to be further optimized, in order to adapt to different source statistics.

## LDPC Decoder Based on Chisel

- **Status**: ✅
- **Reason**: AA-LDPC 디코더 HW 아키텍처: 4-cycle 회피 H생성+TDMP/Log-Map, 메모리 6/8bit 양자화 절감, 이식 가능 HW/디코더(C/D)
- **ID**: ieee:9353021
- **Type**: conference
- **Published**: 14-16 Dec.
- **Authors**: Bingrui Wu
- **PDF**: https://ieeexplore.ieee.org/document/9353021
- **Abstract**: This paper proposes a sparse check matrix H generation method and a regular AA-LDPC (architecture-aware low-density parity-check) code decoder architecture. The generated H matrix is suitable for regular LDPC codes, avoiding the appearance of four-line loops. The decoder uses TDMP (turbo-decoding message-passing) and Log-Map algorithms, which can achieve faster convergence speed and higher throughput compared with traditional decoding algorithms. Use the scoreboard algorithm to solve the problem of data conflict between TDMP algorithm initialization and the first iteration. Extrinsic messages and posterior messages are stored in 6bit and 8bit respectively, the memory usage is reduced by more than 60% compared with the traditional method, and the chip area is reduced. The decoder module is written in high-level Chisel language, which effectively improves the development efficiency compared with verilog. Uvm (Universal Verification Methodology) was used to randomly generate 10,000 stimuli to verify the verilog code generated by Chisel. With a clock frequency of 290MHz, this architecture can decode any regular AA-LDPC(3, 27) code with a code rate of 8/9 9216-bit, with ten iterations and a data throughput rate of 450Mbps.

## Weighting Factors Optimization for NB-LDPC Codes Based on Extended Min-Sum Algorithm

- **Status**: ❌
- **Reason**: 비이진 NB-LDPC(GF(q)) EMS 가중치 최적화, 비이진 LDPC라 제외
- **ID**: ieee:9407981
- **Type**: conference
- **Published**: 14-16 Dec.
- **Authors**: Mingjuan Qiu, Ming Zhan, Liangxi Liu +2
- **PDF**: https://ieeexplore.ieee.org/document/9407981
- **Abstract**: The decoding algorithms of Nonbinary low-density parity-check (NB-LDPC) codes mainly include Belief Propagation (BP), Fast Fourier Transforms (FFT) and Extended Min-Sum (EMS). Among these decoding algorithms, although EMS has the lowest decoding complexity, there is still room for improvement. Therefore, this paper proposes a new algorithm based on the EMS algorithm to further improve the decoding complexity and performance. In order to reduce complexity, an adaptive truncation rule is added to the decoding process. The adaptive truncation rule chooses the length of automatic truncation to reduce the average number of iterations. Thus, the complexity of decoding algorithm is reduced. Besides the weighting factors is added to the variable update iteration process, which effectively improves the decoding performance. The results show that the proposed algorithm has about 0.9 dB gain compared with the EMS decoding algorithm when the bit error rate (BER) is 10--4 and the Galois field GF(q) (q16).

## Optimizing Parametrized Information Bottleneck Compression Mappings with Genetic Algorithms

- **Status**: ✅
- **Reason**: information bottleneck 기반 채널출력 양자화 LUT 디코딩(min-sum 양자화 LLR에 이식 가능), 유전알고리즘 파라미터화 압축 매핑(C)
- **ID**: ieee:9310016
- **Type**: conference
- **Published**: 14-16 Dec.
- **Authors**: Jan Lewandowsky, Sumedh J. Dongare, Marc Adrat +2
- **PDF**: https://ieeexplore.ieee.org/document/9310016
- **Abstract**: Preserving relevant mutual information under compression is the fundamental challenge of the information bottleneck method and has numerous applications in machine learning and in communications. The literature describes very successful applications of this concept in quantized detection and channel decoding schemes. The resulting receiver algorithms only use simple lookup tables and process quantization indices, but can achieve performance close to that of conventional high-precision systems. In some applications, however, it is desirable to design a parametrized compression rule instead of a possibly huge lookup table. Genetic algorithms are very powerful generic optimization algorithms which are inspired from the natural evolution of the species. In this paper, we show that genetic algorithms can be used to optimize parametrized compression mappings that aim for maximum preservation of relevant information, especially in cases where standard optimization methods cannot be applied straightforwardly. We exemplarily investigate the receiver-sided channel output quantization as an important application in communications to illustrate the notable performance and the flexibility of the proposed concept.

## OFDM Covert Communication System Based on the QC-LDPC and Symbol Spread Spectrum

- **Status**: ❌
- **Reason**: QC-LDPC+심볼확산 OFDM 은닉통신; 표준 QC-LDPC 사용, 떼어낼 ECC 기법 없음(보안 응용)
- **ID**: ieee:9372605
- **Type**: conference
- **Published**: 13-16 Dec.
- **Authors**: Baojian Gao, Zhenzhen Fan, Xingyuan Liu +2
- **PDF**: https://ieeexplore.ieee.org/document/9372605
- **Abstract**: As a new technology to solve wireless communication security problems, covert communication can not only hide the transmitted secret information, but also hide the communication process. Therefore, it has become a hot research issue in wireless communication security in recent years. Aiming at the problems of the square root law model in the practical process, this paper deduces and analyzes a constraint condition of the signal-to-noise ratio to measure the covert system. Thus, a covert communication model of OFDM system based on the combination of QC-LDPC and symbol spread spectrum is constructed. Through theoretical and simulation analysis methods, we respectively proved the Gaussian-like, low probability of detection characteristics of the model's radio frequency signal and the reliable communication performance of the system under low signal-to-noise ratio. It is proved that the model can successfully realize the covert communication with limited parameters.

## Performance of UV Spread Spectrum Communication System based on LDPC Codes

- **Status**: ❌
- **Reason**: UV 확산스펙트럼 통신 시스템 설계, 표준 LDPC를 DSSS+BPSK와 조합 — 신규 디코더/코드설계 기여 없음
- **ID**: ieee:9325771
- **Type**: conference
- **Published**: 12-13 Dec.
- **Authors**: Yiwei Peng, Dong Zhou
- **PDF**: https://ieeexplore.ieee.org/document/9325771
- **Abstract**: In the UV scattering communication system, pulse broadening and noise will have a serious impact on the signal. LDPC code is a kind of error correcting code with excellent performance. It can improve the quality of UV communication to a great extent by combining it with spread spectrum technology which can effectively suppress multipath interference. Through the analysis and modeling of UV channel, a system scheme of LDPC + DSSS + BPSK is proposed, which can suppress multipath interference and improve the BER performance of the system.

## Two families of LRCs with availability based on iterative matrix

- **Status**: ❌
- **Reason**: 분산저장 LRC(locally repairable code) 구성 — 비-LDPC erasure/repair 부호, NAND 채널 LDPC ECC 기법 없음
- **ID**: ieee:9325761
- **Type**: conference
- **Published**: 12-13 Dec.
- **Authors**: Mao Zhang, Ruihu Li
- **PDF**: https://ieeexplore.ieee.org/document/9325761
- **Abstract**: Locally repairable code (LRC) in distributed storage system decreases repair degree of failed nodes. LRC with availability is extremely desired in distributed storage system because it permits local repair of failed nodes and parallel access of hot data. In this paper, a novel construction of LRCs with availability is proposed. Explicitly, by matrix iteration, two families of LRCs with all symbol locality and availability are constructed. The first family LRC is SA-LRC and keeps the code structure binary which is convenient to apply. The second family LRC is systematic code and possesses inspiring information rate r/r+2. Our construction is concise and explicit parity-check matrices of LRCs are given.

## Syndrome-Aided Gradient Descent Bit Flipping Algorithm for LDPC Decoding

- **Status**: ✅
- **Reason**: 신드롬 기반 적응 임계값 GDBF 비트플립 디코딩(SAGDBF) 신규 제안, 저복잡도 바이너리 LDPC 디코더로 직접 이식 가능(C)
- **ID**: ieee:9345227
- **Type**: conference
- **Published**: 11-14 Dec.
- **Authors**: Yuang Huang, Haiyang Liu
- **PDF**: https://ieeexplore.ieee.org/document/9345227
- **Abstract**: Gradient descent bit flipping (GDBF) algorithm is an important low-complexity method for decoding LDPC codes. In particular, the multi-bit GDBF decoding has the best decoding performance among BF algorithms if a suitable threshold is prescribed. However, extensive computer searches are needed to find such a threshold for a specific LDPC code. In this paper, we propose a syndrome-aided GDBF (SAGDBF) algorithm to address the problem. The thresholds in our algorithm are adaptively adjusted according to the syndrome values in the iterative process. Simulation results for different LDPC codes suggest that the error performances of the proposed SAGDBF algorithm are close to and even better than the original multi-bit GDBF algorithm at a relatively small number of iterations. In addition, the complexity increased in our proposed algorithm is negligible compared with the original multi-bit GDBF algorithm. Hence, the proposed algorithm is suitable for practical purposes.

## A Novel Soft-Output Demapper for DOCSIS 3.1

- **Status**: ✅
- **Reason**: DOCSIS 3.1 LDPC용 개선 bit LLR 식 제안, 저부호율 QAM LLR 정확도 향상은 NAND LDPC LLR 양자화/연판정 디코딩에 이식 가능(C)
- **ID**: ieee:9345192
- **Type**: conference
- **Published**: 11-14 Dec.
- **Authors**: Feng Zheng, Bowen Pang
- **PDF**: https://ieeexplore.ieee.org/document/9345192
- **Abstract**: DOCSIS 3.1, the new international standard for high-speed cable television (CATV), uses Low Density Parity Check (LDPC) code for forward error correction (FEC). It is widely known that accurate soft information is critical to the performance of LDPC decoding, but existing bit log-likelihood ratio (LLR) expression only works well under high code rate. In this paper, an improved bit LLR expression is proposed to compensate the difference between the existing LLR expression under low code rate for Gray coded M-ary quadrature amplitude modulation (QAM). In addition to high accuracy, the improved LLR is simple and efficient to manipulate. Besides LDPC, the improved LLR is also applicable to other codes that require soft information. Simulation results show that the improved LLR expression achieves a significant improvement in performance for both LDPC and Turbo decoding.

## Semi-LDPC Convolutional Codes with Low-latency Decoding Algorithm

- **Status**: ✅
- **Reason**: semi-LDPC convolutional code 신규 구성 + 윈도우=2 슬라이딩 윈도우 list 디코딩으로 저지연 코딩이득, 바이너리 LDPC 구성/디코더 기법 이식 가능(E/C)
- **ID**: ieee:9344992
- **Type**: conference
- **Published**: 11-14 Dec.
- **Authors**: Zengzhe Chen, Suihua Cai, Li Chen +1
- **PDF**: https://ieeexplore.ieee.org/document/9344992
- **Abstract**: In this paper, we propose a new coding scheme called semi-low-density parity-check (semi-LDPC) convolutional code, whose parity-check matrix consists of both sparse and dense sub-matrices. We propose a sliding-window decoding algorithm with a window size of two, in which a list decoding algorithm is utilized to reduce decoding latency. Simulation results show the proposed semi-LDPC convolutional code with list decoding can obtain a coding gain up to 1 dB over the existing LDPC convolutional codes with the same decoding latency.

## A Lightweight and Efficient Physical Layer Key Generation Mechanism for MANETs

- **Status**: ❌
- **Reason**: MANET 물리계층 키 생성(보안/정보조정)에 LDPC를 reconciliation에 사용, 채널 ECC 아님, 떼어낼 디코더/HW 없음
- **ID**: ieee:9345082
- **Type**: conference
- **Published**: 11-14 Dec.
- **Authors**: Xiaomiao Gao, Wenjie Du, Weijiang Liu +2
- **PDF**: https://ieeexplore.ieee.org/document/9345082
- **Abstract**: Due to the reciprocity of wireless channels, the communication parties can directly extract the shared key from channel. This solution were verified through several schemes. However, in real situations, channel sampling of legitimate transceivers might be impacted by noises and other interferences, which makes the channel states obtained by initiator and responder might be obvious different. The efficiency and even availability of physical layer key generation are thus reduced. In this paper, we propose a lightweight and efficient physical layer key generation scheme, which extract shared secret keys from channel state information (CSI). To improve the key generation process, the discrete cosine transform (DCT) is employed to reduce differences of channel states of legitimate transceivers. Then, these outputs are quantified and encoded through multi-bit adaptive quantization(MAQ) quantizer and gray code to generate binary bit sequence, which can greatly reduce the bit error rate. Moreover, the low density parity check (LDPC) code and universal hashing functions are used to achieve information reconciliation and privacy amplifification. By adding preprocessing methods in the key generation process and using the rich information of CSI, the security of communications can be increased on the basis of improving the key generation rate. To evaluate this scheme, a number of experiments in various real environments are conducted. The experimental results show that the proposed scheme can effificiently generate shared secret keys for nodes and protect their communication.

## A Method of Phase Noise Estimation and Compensation Based on Golay Sequence in Time Domain for SC-FDE Millimeter-Wave Communication Systems

- **Status**: ❌
- **Reason**: 밀리미터파 SC-FDE 위상잡음 추정/보상이 주제, LDPC는 1/2 표준 부호로 성능 보조용 부수 언급
- **ID**: ieee:9344982
- **Type**: conference
- **Published**: 11-14 Dec.
- **Authors**: Tingting Yao, Xiangyang Wang, Huan Zhou +2
- **PDF**: https://ieeexplore.ieee.org/document/9344982
- **Abstract**: A method of phase noise (PHN) estimation and compensation based on the Golay sequence is proposed in the article for single-carrier frequency-domain equalization (SC-FDE) Millimeter-Wave Systems. First, the channel is estimated based on the correlation with the Golay sequence. Then, the 64-length cyclic prefix (CP) between data blocks is adopted to estimate the common phase error (CPE) of the data blocks after equalization in the frequency domain. Finally, the PHN estimation and compensation after equalization is computed so that the phase deviation can be avoided. Different from previous researches, the algorithm is developed in SC-FDE Systems, using a system symbol transmission rate of 2.4576G sym/s, 64QAM modulation, and each transmission frame structure of 9600 data blocks. In this case, the effect of PHN will be magnified. 1/2 LDPC encoding and decoding are also introduced into this system to further improve the performance. Compared with present algorithms, the algorithm shows better comprehensive performance in MSE of PHN before and after equalization, with the complexity of integrated computation taken into consideration.

## Research on Polar Coding Application for Underwater Acoustic OFDM Communication System

- **Status**: ❌
- **Reason**: 수중음향 OFDM용 polar code 구성/디코딩이 주제, 비-LDPC 부호이며 LDPC는 비교 베이스라인일 뿐 이식 기법 없음
- **ID**: ieee:9345071
- **Type**: conference
- **Published**: 11-14 Dec.
- **Authors**: Yushuang Zhai, Jilong Li, Haihong Feng
- **PDF**: https://ieeexplore.ieee.org/document/9345071
- **Abstract**: This paper proposes a polar coding mechanism for the underwater acoustic (UWA) channel, which improves the performance in the bit error rate (BER) compared with the original code construction algorithms and decoding methods invented by Arikan. It studied the performance of polar coding in the UWA communication system with the Orthogonal Frequency Division Multiplexing (OFDM) technique in theory and simulation. The simulation results show that the BER of the polar code with the code rate 1/2 in the underwater time-varying channel can reach 10-4~10-5 when the signal-to-noise ratio (SNR) is at 4 dB, which is about 0.5~1 dB better than LDPC and Turbo codes. Moreover, the BER performance of polar codes under different UWA channel models and parameters, code lengths, and code rates were also compared. The results demonstrate that the proposed mechanism matches the UWA channel well, thus making polar codes suitable and reliable for the UWA communication systems.

## Data Transfer Rates in HFC Networks

- **Status**: ❌
- **Reason**: HFC/DOCSIS 네트워크 전송속도, FEC-LDPC는 표준 단순 언급. 신규 디코더/구성 기여 없음
- **ID**: ieee:9505550
- **Type**: conference
- **Published**: 1-4 Dec. 2
- **Authors**: Grela Abel Alejandro, Monzón Jorge Emilio
- **PDF**: https://ieeexplore.ieee.org/document/9505550
- **Abstract**: Current access networks need to transmit data with increasingly higher rates. HFC (Hybrid Fiber Coaxial) networks offer growth capacity. To obtain maximal transfer rates, we propose releasing the 500 MHz spectrum -currently assigned to the transmission of analog and even digital television-, to convert HFC networks into entirely data networks, by using the first 200 MHz of the total spectrum for upstream, and from 258 MHz and up to 1.8 GHz for downstream. As the architecture of HFC networks must decrease the number of active amplifiers, we use an N + 0 design, which allows serving smaller service areas while decreasing the noise and distortion indexes. The DOCSIS 3.1 standard uses the OFDM (Orthogonal Frequency Division Multiplexing) system for transmission in downstream and OFDMA (Orthogonal Frequency Division Multiple Access) for upstream, employing multiple sub-carrier schemes, each of which is modulated with up to 16K QAM in downstream and up to 4K QAM in upstream. Multiple modulation profiles (MMP) are associated to the quality of the channel. FEC-LDPC (Forward Error CorrectionLow Density Parity Check) is used for error correction. The maximal transfer rate calculated in downstream is 16.9 Gbps, and 1.86 Gbps in upstream. To achieve these values, it is necessary to maintain a SNR higher than 40 dB in the HFC network. In this way, HFC networks represent a valid alternative to meet demand for transfer rates in the short and medium term.

## Improving SSD Read Latency via Coding

- **Status**: ✅
- **Reason**: SSD read latency 향상 코딩, NAND 소자 실패+ECC 큐잉 모델. 스토리지 ECC 일반(B) 범주.
- **ID**: ieee:9026817
- **Type**: journal
- **Published**: 1 Dec. 202
- **Authors**: Hyegyeong Park, Jaekyun Moon
- **PDF**: https://ieeexplore.ieee.org/document/9026817
- **Abstract**: We study the potential enhancement of the read access speed in high-performance solid-state drives (SSDs) by coding, given speed variations across the multiple flash interfaces and assuming occasional local memory failures. Our analysis is based on a queuing model that incorporates both read request failures and NAND element failures. The NAND element failure in the present context reflects various limitations on the memory element level such as bad blocks, dies or chips that cannot be corrected by error control coding (ECC) typically employed to protect pages read off the NAND cells. Our analysis provides a clear picture of the storage-overhead and read-latency trade-offs given read failures and NAND element failures. We investigate two different ways to mitigate the effect of NAND element failures using the notion of multi-class jobs with different priorities. A strong motivation for this work is to understand the reliability requirement of NAND chip components given an additional layer of failure protection, under the latency/storage-overhead constraints.

## Secure TDD MIMO Networks Against Training Sequence Based Eavesdropping Attack

- **Status**: ❌
- **Reason**: MIMO 보안/CSI 추정 도청 방어. LDPC ECC와 무관, 떼어낼 디코더/HW/코드설계 기법 없음.
- **ID**: ieee:8812917
- **Type**: journal
- **Published**: 1 Dec. 202
- **Authors**: Yunlong Mao, Ying He, Yuan Zhang +2
- **PDF**: https://ieeexplore.ieee.org/document/8812917
- **Abstract**: Multi-User MIMO (MU-MIMO) has attracted much attention due to its significant advantage of increasing the utilization ratio of wireless channels. However, Frequency-Division Duplex (FDD) systems are vulnerable to eavesdropping, since the explicit CSI feedback can be manipulated. In this paper, we show that Time-Division Duplex (TDD) systems are insecure as well. In particular, we show that it is possible to eavesdrop on other users' downloads by tuning training sequences. In order to defend MU-MIMO against such threats, we propose a secure CSI estimation scheme, which can provide correct estimates of CSI when adversarial users are in presence. We prove that our scheme is secure against training sequence based eavesdropping attack. We have implemented our scheme for TDD MU-MIMO systems and performed a series of experiments. Results demonstrate that our secure CSI estimation scheme is highly effective in protecting TDD MIMO networks against eavesdropping attack. Furthermore, we extend our scheme to support massive MU-MIMO networks, with a carefully redesigned uplink protocol and optimized power allocation to achieve higher spectral efficiency. To be more practical, we also take mismatch channel issue into our consideration. An enhancement scheme is proposed and we show that our scheme with enhancement is secure and correct under mismatch channel.
