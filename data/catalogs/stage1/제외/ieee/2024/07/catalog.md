# IEEE Xplore — 2024-07


## Carrier Frequency Synchronization of LDPC Coded Transmissions in High Dynamic Environments

- **Status**: ❌
- **Reason**: 무선 통신 반송파 주파수 동기화·CFO 추정 중심, LDPC는 부수 언급이고 떼어낼 ECC 디코더/코드 기법 없음
- **ID**: ieee:10493842
- **Type**: journal
- **Published**: July 2024
- **Authors**: Yudan Xu, Hailiang Xiong, Gangqiang Yang +1
- **PDF**: https://ieeexplore.ieee.org/document/10493842
- **Abstract**: Modern communication systems based on LDPC coded data transmission enable the operations at low signal-to-noise ratio (SNR) conditions, close to the Shannon limit, where strict synchronization is required to ensure the optimal performance of the receiver. Residual offsets left by imprecise synchronization would lead to SNR degradation at the decoder, yet its elimination remains an issue at low SNRs. In this paper we focus on the accurate estimation of carrier frequency offset, and propose a novel frequency estimator with moderate computational complexity, which has wider, signal-length-independent estimation range and lower variance close to the Cramer–Rao bound (CRB), compared to other existing methods. Based on the proposed estimator, we establish a new structure of iterative synchronization embedded decoder by utilizing the expectation-maximization (EM) algorithm. The presented decoder exhibits a capability to significantly alleviate the performance degradation caused by residual offsets and to achieve performance enhancement for both the decoder and synchronizer. Furthermore, we develop a general frequency estimation framework for joint acquisition and fine carrier synchronization, which shows superior performance of low error metric. The proposed frequency estimator and improved frameworks will be of great significance to the implementation of the signal reception in high dynamic wireless communication systems at low SNR conditions.

## Capacity, Convergence, and Complexity Improvements for LDPC-Coded MIMO-VLC Systems With Generalized Spatial Modulation

- **Status**: ❌
- **Reason**: MIMO-VLC 응용 특이적 P-LDPC, GSM 변조·VLC 결합 설계가 핵심이고 IS-JDD도 VLC 검출-디코딩 결합 — NAND에 이식할 순수 LDPC 기법 없음
- **ID**: ieee:10436099
- **Type**: journal
- **Published**: July 2024
- **Authors**: Zhaojie Yang, Yong Liang Guan, Yi Fang +1
- **PDF**: https://ieeexplore.ieee.org/document/10436099
- **Abstract**: This paper is centered on multiple-input multiple-output visible light communication (MIMO-VLC) systems with protograph-based low-density parity-check (P-LDPC) codes. We propose a two-step design method, which is composed of spatial-domain (SpD)-based Gray-like (GL) principle and signal-domain (SiD)-based energy-optimization (EO) principle, to construct a novel class of generalized spatial modulation (GSM) schemes, referred to as GLEOGSM schemes, to enhance the system performance. We also introduce a novel internal-stopping (IS) principle into the conventional joint detection and decoding (JDD) architecture, the resultant IS-aided JDD (IS-JDD) algorithm significantly reduces the computational overhead. Inspired by the proposed IS-JDD architecture, we further conceive a low-complexity IS-aided extrinsic-information-transfer (IS-EXIT) algorithm to analyze the convergence performance of P-LDPC-coded MIMO-VLC systems. Both theoretical and simulation results verify that our proposed designs can remarkably outperform the existing benchmark schemes in terms of capacity, convergence and complexity.

## FEC-Aided Decision Feedback Blind Mismatch Calibration of TIADCs in Wireless Time-Varying Channel Environments

- **Status**: ❌
- **Reason**: TIADC mismatch 캘리브레이션에 FEC를 보조로 쓸 뿐, LDPC/디코더 기여 없음 — 통신 응용 특이적, 떼어낼 ECC 기법 없음
- **ID**: ieee:10418841
- **Type**: journal
- **Published**: July 2024
- **Authors**: Haoyang Shen, Deepu John, Barry Cardiff
- **PDF**: https://ieeexplore.ieee.org/document/10418841
- **Abstract**: Time-interleaved analog-to-digital converters (TIADCs) are widely used in communication systems due to their exceptionally high sampling rates; however, in real-world applications, the offset, gain, and time-skew mismatches in TIADCs are a significant challenge for the circuit system. This article proposes a forward error correction (FEC)-aided decision feedback blind mismatch calibration for TIADCs in the time-varying channels environment specific to the orthogonal frequency-division multiplexing (OFDM) system. In our proposed approach, we use an FEC decision feedback technique to generate a ground truth reference signal for the purpose of calibration. There are two stages. In the first stage, the offset and gain mismatches are estimated and corrected using standard techniques. In the second stage, an adaptive filter bank corrects the time-skew mismatch directly without the need for any additional calibration hardware. The coefficients of this adaptive filter are continuously adjusted in the background based on an error signal derived from the decision feedback ground truth signal. This calibration algorithm significantly reduces the bit error rate (BER) and improves the system performance. The efficacy of these approaches is validated through comprehensive simulations to attain a performance assessment, quantified by the BER, using a realistic wireless time-varying channel system configuration.

## Trends in Channel Coding for 6G

- **Status**: ❌
- **Reason**: 6G 채널코딩 트렌드 서베이 — 떼어낼 구체 신기법 없음
- **ID**: ieee:10571997
- **Type**: journal
- **Published**: July 2024
- **Authors**: Sisi Miao, Claus Kestel, Lucas Johannsen +6
- **PDF**: https://ieeexplore.ieee.org/document/10571997
- **Abstract**: Error correction coding (i.e., channel coding) is a key ingredient of any digital communications system. In mobile wireless communications, channel codes have evolved from simple convolutional codes in Global System for Mobile Communications (GSM) (2G), parallel concatenated (turbo) codes in Universal Mobile Telecommunications Service (UMTS) (3G), and long-term evolution (LTE) (4G), to carefully designed multirate/multilength low-density parity-check (LDPC) codes in 5G, combined with polar codes for short messages on the synchronization channel. Based on this rich history, and by accounting for the technological advances in very large-scale integration, this article will outline some recent trends in channel coding as they may be applied in 6G systems, ranging from novel approaches for short blocklengths such as automorphism ensemble decoding, via ideas of coding for multiple access, to concepts for unified coding schemes that may simplify encoding/decoding hardware at competitive error-correcting performance.

## A Unified Multi-Task Semantic Communication System for Multimodal Data

- **Status**: ❌
- **Reason**: 멀티모달 시맨틱 통신/딥러닝 코드북 시스템, LDPC ECC 기여 없음 — 시맨틱 통신 제외
- **ID**: ieee:10431795
- **Type**: journal
- **Published**: July 2024
- **Authors**: Guangyi Zhang, Qiyu Hu, Zhijin Qin +3
- **PDF**: https://ieeexplore.ieee.org/document/10431795
- **Abstract**: Task-oriented semantic communications have achieved significant performance gains. However, the employed deep neural networks in semantic communications have to be updated when the task is changed or multiple models need to be stored for performing different tasks. To address this issue, we develop a unified deep learning-enabled semantic communication system (U-DeepSC), where a unified end-to-end framework can serve many different tasks with multiple modalities of data. As the number of required features varies from task to task, we propose a vector-wise dynamic scheme that can adjust the number of transmitted symbols for different tasks. Moreover, our dynamic scheme can also adaptively adjust the number of transmitted features under different channel conditions to optimize the transmission efficiency. Particularly, we devise a lightweight feature selection module (FSM) to evaluate the importance of feature vectors, which can hierarchically drop redundant feature vectors and significantly accelerate the inference. To reduce the transmission overhead, we then design a unified codebook for feature representation to serve multiple tasks, where only the indices of these task-specific features in the codebook are transmitted. According to the simulation results, the proposed U-DeepSC achieves comparable performance to the task-oriented semantic communication system designed for a specific task but with significant reduction in both transmission overhead and model size.

## DNA-Based Data Storage Systems: A Review of Implementations and Code Constructions

- **Status**: ❌
- **Reason**: DNA 분자 데이터 저장 리뷰, 합성생물학·trace reconstruction 코딩 개요 — 떼어낼 LDPC 디코더/HW/구성 없음
- **ID**: ieee:10440314
- **Type**: journal
- **Published**: July 2024
- **Authors**: Olgica Milenkovic, Chao Pan
- **PDF**: https://ieeexplore.ieee.org/document/10440314
- **Abstract**: This invited review paper has the aim to acquaint the communication theory community with the emerging topic of molecular data storage. The exposition includes an overview of basic concepts in synthetic and computational biology and a discussion of diverse approaches used to implement such systems. It also describes new problems in communication and coding theory, and discusses some relevant results pertaining to DNA sequence profiles, coded trace reconstruction, coding for DNA punchcard systems and coding for unique reconstruction.

## Knowledge Distillation-Based Semantic Communications for Multiple Users

- **Status**: ❌
- **Reason**: 지식증류 기반 시맨틱 통신; LDPC/ECC 무관, 신경망 인코더-디코더 압축 응용
- **ID**: ieee:10345474
- **Type**: journal
- **Published**: July 2024
- **Authors**: Chenguang Liu, Yuxin Zhou, Yunfei Chen +1
- **PDF**: https://ieeexplore.ieee.org/document/10345474
- **Abstract**: Deep learning (DL) has shown great potential in revolutionizing the traditional communications system. Many applications in communications have adopted DL techniques due to their powerful representation ability. However, the learning-based methods can be dependent on the training dataset and perform worse on unseen interference due to limited model generalizability and complexity. In this paper, we consider the semantic communication (SemCom) system with multiple users, where there is a limited number of training samples and unexpected interference. To improve the model generalization ability and reduce the model size, we propose a knowledge distillation (KD) based system where Transformer based encoder-decoder is implemented as the semantic encoder-decoder and fully connected neural networks are implemented as the channel encoder-decoder. Specifically, four types of knowledge transfer and model compression are analyzed. Important system and model parameters are considered, including the level of noise and interference, the number of interfering users and the size of the encoder and decoder. Numerical results demonstrate that KD significantly improves the robustness and the generalization ability when applied to unexpected interference, and it reduces the performance loss when compressing the model size.

## Dynamic Compressed Sensing Approach for Unsourced Random Access

- **Status**: ❌
- **Reason**: unsourced random access용 CS/SPARC/AMP — LDPC ECC 아니고 떼어낼 디코더·코드설계 없음
- **ID**: ieee:10535261
- **Type**: journal
- **Published**: July 2024
- **Authors**: Ehsan Nassaji, Dmitri Truhachev
- **PDF**: https://ieeexplore.ieee.org/document/10535261
- **Abstract**: In compressed sensing (CS) approach for unsourced random access (URA), each user’s transmitted sequence consists of shorter sub-sequences encoded via sparse regression codes (SPARCs) over several consecutive sub-slots. The approximate message passing (AMP) technique is employed to decode the SPARCs. Stitching together each user’s sub-messages decoded over distinct sub-slots requires an outer parity-check code that adds redundancy bit interconnecting the sub-messages. This letter introduces a novel CS-based URA scheme which is free from the outer code. In the proposed scheme, the encoded sub-sequence of the first sub-slot acts as a temporary user identifier and also customises the sensing matrix used to encode the subsequent sub-messages. The technique allows each user to send several sub-messages (data streams) per sub-slot. Simulation results indicate that the proposed scheme outperforms the existing CS-based algorithms on Gaussian channel. It is also superior than the other state-of-the-art URA schemes when the number of active users exceeds 200. The proposed analysis framework closely predicts the obtained numerical results.

## Block Interleaved Chirp Spreading LoRa Modulation Over Multipath Channels

- **Status**: ❌
- **Reason**: LoRa chirp 변조의 멀티패스 ISI 완화 인터리빙 — 변조 기법, LDPC ECC 무관
- **ID**: ieee:10497883
- **Type**: journal
- **Published**: July 2024
- **Authors**: Jiaojiao Liu, Yuanmei Yan, Peng Huang +2
- **PDF**: https://ieeexplore.ieee.org/document/10497883
- **Abstract**: For actual multipath channels, inter symbol interference (ISI) may seriously degrade LoRa performance. With the path overlapping interference analyzed, the upper bound of LoRa bit error rate (BER) has been approximated. Then we propose a block interleaved chirp spreading LoRa (BICS-LoRa) modulation to split the multipath interference into small ones at different positions. The probability of interference peak being greater than the direct path peak is reduced, so does the BER. Experiment results show BICS-LoRa can reduce the peak of multipath interference and may result in BER reduction. Besides, the performance gain increases with SF value in most cases.

## Eliminating Media Noise While Preserving Storage Capacity: Reconfigurable Constrained Codes for Two-Dimensional Magnetic Recording

- **Status**: ❌
- **Reason**: TDMR 자기기록용 constrained code(LOCO), 매체 노이즈 패턴 금지 부호 — LDPC ECC가 아닌 변조/제약 부호
- **ID**: ieee:10466482
- **Type**: journal
- **Published**: July 2024
- **Authors**: Iven Guzel, Doğukan Özbayrak, Robert Calderbank +1
- **PDF**: https://ieeexplore.ieee.org/document/10466482
- **Abstract**: Magnetic recording devices are still competitive in the storage density race with solid-state devices thanks to new technologies such as two-dimensional magnetic recording (TDMR). TDMR offers remarkable storage density increase without the need for new magnetic materials; however, advanced data processing schemes are needed to guarantee reliability. Data patterns where a bit is surrounded by complementary bits at the four positions with Manhattan distance 1 on the TDMR grid are called plus isolation (PIS) patterns, and they are error-prone. Recently, we introduced lexicographically-ordered constrained (LOCO) codes, namely optimal plus LOCO (OP-LOCO) codes, with minimal redundancy that prevent these patterns from being written in a TDMR device. However, in the high-density regime or the low-energy regime (as the device ages), additional error-prone patterns emerge, specifically data patterns where a bit is surrounded by complementary bits at only three positions with Manhattan distance 1, and we call them incomplete plus isolation (IPIS) patterns. In this paper, we present capacity-achieving codes that forbid both PIS and IPIS patterns in TDMR systems with wide read heads. Because of their shape, we collectively call the PIS and IPIS patterns rotated T isolation (RTIS) patterns, and we call the new codes optimal T LOCO (OT-LOCO) codes. We analyze OT-LOCO codes and derive their simple encoding-decoding rule that allows reconfigurability. We also present a novel bridging idea for these codes to further increase the rate. Our simulation results demonstrate that OT-LOCO codes not only remarkably outperform OP-LOCO codes, but also entirely eliminate media noise effects, resulting from error-prone data patterns, at practical TD densities in the range [0.6, 0.8) with high rates in the range [0.81, 0.83]. At the TD density of 0.8, the OT-LOCO code of rate 0.8267 achieves a frame error rate (bit error rate) performance gain of about 1.15 orders (1.23 orders) of magnitude for all TDMR down (horizontal) tracks compared with the uncoded setting. To further preserve the storage capacity, we suggest using OP-LOCO codes, which have higher rates than OT-LOCO codes, early in the device lifetime, then employing the reconfiguration property to switch to OT-LOCO codes later in the device lifetime. While the point of reconfiguration on the density/energy axis is decided manually at the moment, the next step is to use machine learning to make that decision based on the TDMR device status. Moreover, we introduce another coding scheme to remove RTIS patterns in TDMR systems which offers lower complexity, lower error propagation, and track separation, at the expense of a limited rate loss.

## Turbo Receiver for Short-Block-Length Polar-Coded Direct-Access Satellite-IoT Systems

- **Status**: ❌
- **Reason**: 위성-IoT Polar 코딩 Turbo 수신기 연구로 LDPC는 비교 베이스라인일 뿐, NAND LDPC에 이식할 디코더/HW/코드설계 기법 없음
- **ID**: ieee:10621181
- **Type**: conference
- **Published**: 8-11 July 
- **Authors**: Ali Eltohamy, Christian Andreas Hofmann, Andreas Knopp +1
- **PDF**: https://ieeexplore.ieee.org/document/10621181
- **Abstract**: Anticipated direct-access satellite-communication links will be the key enabler for a plethora of new Internet of Things (IoT) applications in the field of smart farming, asset tracking, or emergency services, which are blocked by today’s limited cellular coverage. Extending the receiver-transmitter distance from a few kilometers to the nearest base station to hundreds of kilometers to a Low Earth Orbit (LEO) satellite is challenging especially given the tight cost and power budgets of IoT devices. Advanced digital-baseband processing can help to close the link as long as its impact on computational complexity is tolerable. In this work we analyze the latest advancements in high-performance soft-output Polar coding that support small packet sizes demanded by IoT devices and extend a recently proposed Satellite IoT (SIoT) physical layer by introducing Turbo detection. Simulation results demonstrate the superiority of Polar codes over SIoT-specific short-block length Low Density Parity Check (LDPC) codes showing a performance gain of up to 0.8 dB. The proposed Polar-based Turbo-detection provides an additional gain of 0.5 dB resulting in an overall performance gain of 1.3 dB over an LDPC-coded reference system.

## High-Speed OFDM Baseband Modem for a Ka-Band 3U CubeSat Transceiver

- **Status**: ❌
- **Reason**: CubeSat OFDM 베이스밴드 모뎀 설계로 ECC 일반 언급뿐, LDPC 디코더/코드설계 이식 기법 없음
- **ID**: ieee:10794304
- **Type**: conference
- **Published**: 8-11 July 
- **Authors**: Ali Al-Saifi, Amr Zeedan, Tamer Khattab
- **PDF**: https://ieeexplore.ieee.org/document/10794304
- **Abstract**: CubeSats have been considered for a wide range of applications such as Earth imaging, disaster detection, space exploration, and research. Due to their low-cost and short deployment cycles, they have gained traction in numerous applications. This paper presents the design of a high-speed OFDM baseband modem for a Ka-band 3U CubeSat. The proposed baseband design includes elaborate steps for error correction, multiplexing, and channel estimation and compensation. The aim of this work is to establish the feasibility of the theorized baseband design while considering the link budget restrictions due to the Ka-band and use of OFDM which is not commonly present in most CubeSat systems. The developed baseband system has been simulated on MATLAB and demonstrated superior performance compared with existing CubeSat systems. The obtained results are very promising, achieving less than 10−7 BER at 5 dB Signal-to-Noise Ratio (SNR).

## Fault-Tolerant Quantum LDPC Encoders

- **Status**: ❌
- **Reason**: 양자 LDPC 인코더(큐비트·얽힘 공유·횡단 구현), 양자 전용 개념 의존 — 고전 이식 불가
- **ID**: ieee:10591776
- **Type**: conference
- **Published**: 7-7 July 2
- **Authors**: Abhi Kumar Sharma, Shayan Srinivasa Garani
- **PDF**: https://ieeexplore.ieee.org/document/10591776
- **Abstract**: We propose fault-tolerant encoders for quantum low-density parity check (LDPC) codes. By grouping qubits within a quantum code over contiguous blocks and applying preshared entanglement across these blocks, we show how transversal implementation can be realized. The proposed encoder reduces the error propagation while using multi-qubit gates and is applicable for both entanglement-unassisted and entanglement-assisted quantum LDPC codes.

## Toward Quantum CSS-T Codes from Sparse Matrices

- **Status**: ❌
- **Reason**: 양자 CSS-T 부호 구성(Hull/dual 조건), 양자 전용 횡단게이트·축퇴 개념 의존 — 고전 LDPC 이식 불가
- **ID**: ieee:10591766
- **Type**: conference
- **Published**: 7-7 July 2
- **Authors**: Eduardo Camps-Moreno, Hiram H. López, Gretchen L. Matthews +1
- **PDF**: https://ieeexplore.ieee.org/document/10591766
- **Abstract**: CSS-T codes were recently introduced as quantum error-correcting codes that respect a transversal gate. A CSS-T code depends on a pair ($C_{1}, C_{2}$) of binary linear codes $C_{1}$ and $C_{2}$ that satisfy certain conditions. We prove that $C_{1}$ and $C_{2}$ form a CSS-T pair if and only if $C_{2}\subset \text{Hull}(C_{1})\cap \text{Hull}(C_{1}^{2})$, where the hull of a code is the intersection of the code with its dual. We show that if ($C_{1}, C_{2}$) is a CSS-T pair, and the code $C_{2}$ is degenerated on $\{i\}$, meaning that the $i^{th}$-entry is zero for all the elements in $C_{2}$, then the pair of punctured codes ($C_{1}\vert_{i}, C_{2}\vert_{i}$) is also a CSS-T pair. Finally, we provide Magma code based on our results and quasi-cyclic codes as a step toward finding quantum LDPC or LDGM CSS-T codes computationally.

## The BP-LCOSD Algorithm for Toric Codes

- **Status**: ❌
- **Reason**: 토릭 코드(양자 EC) BP-LCOSD, MWPM 비교 — 양자 전용 토폴로지 부호 의존, 고전 바이너리 LDPC 이식성 약함
- **ID**: ieee:10591758
- **Type**: conference
- **Published**: 7-7 July 2
- **Authors**: Jifan Liang, Qianfan Wang, Lvzhou Li +1
- **PDF**: https://ieeexplore.ieee.org/document/10591758
- **Abstract**: The ordered statistics decoding with local constraints (LCOSD) algorithm is an OSD-like decoding algorithm that has been shown to have better performance than the conventional OSD algorithm in classical error-correcting codes. As for quantum error-correcting codes (QECCs), inspired by the post-processing for the quantum LDPC codes, we have proposed a new post-processing decoding algorithm based on the classical LCOSD algorithm for the toric codes, referred to as the BP-LCOSD algorithm. We show by simulations that the BP-LCOSD algorithm has a better logical error rate and a higher fault-tolerance threshold compared to the minimum-weight perfect matching (MWPM) algorithm in decoding toric codes.

## Generalizing Quantum Tanner Codes

- **Status**: ❌
- **Reason**: 양자 Tanner 부호 일반화(군 작용·Schreier 그래프), 양자 전용 점근적 좋은 qLDPC 구성 — 고전 바이너리 LDPC 이식성 없음
- **ID**: ieee:10591772
- **Type**: conference
- **Published**: 7-7 July 2
- **Authors**: Olai Å. Mostad, Eirik Rosnes, Hsuan-Yin Lin
- **PDF**: https://ieeexplore.ieee.org/document/10591772
- **Abstract**: In this work, we present a generalization of the recently proposed quantum Tanner codes by Leverrier and Zémor, which contains a construction of asymptotically good quantum low-density parity-check codes. Quantum Tanner codes have so far been constructed equivalently from groups, Cayley graphs, or square complexes constructed from groups. We show how to enlarge this to group actions on finite sets, Schreier graphs, and a family of square complexes, which is the largest possible in a certain sense. Furthermore, we discuss how the proposed generalization opens up the possibility of finding other families of asymptotically good quantum codes.

## Energy- and Cost-Oriented Optimization of Hybrid Coded Storage in Edge Caching Systems

- **Status**: ❌
- **Reason**: 엣지 캐싱 하이브리드 코딩(LDPC/RS 선택 ML 정책), LDPC를 기성 도구로 선택만 — 떼어낼 새 디코더/구성 기법 없음
- **ID**: ieee:10707504
- **Type**: conference
- **Published**: 7-13 July 
- **Authors**: Haojuan Zhang, Yali Wang, Peiyan Yuan +1
- **PDF**: https://ieeexplore.ieee.org/document/10707504
- **Abstract**: As the size of data clusters grows, the issues of storage redundancy, data availability, and the cost of edge caching systems become the focus of attention. Although the multi-copy strategy improves data availability, its redundancy cost is high and does not fully consider file data characteristics. Erasure codes techniques have been widely studied as an alternative, but the selection of a suitable coding scheme remains a challenge. To this end, we propose a hybrid coding caching scheme. Firstly, we predict data types using machine learning methods to ensure that the most valuable content is stored. Secondly, for the characteristics of the multi-copy strategy, low-density parity check (LDPC), and Reed-Solomon coding (RS), we propose an adaptive data partitioning strategy (ADPRF) to select appropriate coding schemes for different data. Finally, by combining the ideas of dynamic programming and heuristic algorithms, we propose a redundancy-aware edge collaborative caching algorithm (RPCO) with joint optimization of energy and cost to determine the optimal set of collaborative nodes and the optimal cache locations for files. Compared with the traditional responsive caching scheme, this algorithm can reduce the system cost by 13.8% and access latency by 11.5%.

## Threshold Saturation for Quantitative Group Testing with Low-Density Parity-Check Codes

- **Status**: ❌
- **Reason**: 정량적 그룹테스트용 LDPC threshold saturation 증명 — GT 응용 순수 이론(potential threshold), 이식할 디코더/구성 새 기여 없음
- **ID**: ieee:10619188
- **Type**: conference
- **Published**: 7-12 July 
- **Authors**: Mgeni Makambi Mashauri, Alexandre Graell i Amat, Michael Lentmaier
- **PDF**: https://ieeexplore.ieee.org/document/10619188
- **Abstract**: We recently proposed a quantitative group testing (GT) scheme with low-complexity peeling decoding based on low-density parity-check (LDPC) codes. Based on finite length simulations and a density evolution analysis we were able to demonstrate that simple $(d_{\mathrm{v}},d_{\mathrm{c}})$-regular LDPC codes can be more efficient for GT than existing generalized LDPC (GLDPC) code constructions based on BCH component codes. Even larger gains were numerically observed in combination with spatial coupling. In this paper, we use vector admissible systems to prove threshold saturation and compute the corresponding potential thresholds.

## Group Codes with Low-Density Orthogonal Idempotent

- **Status**: ❌
- **Reason**: 군대수 위 LDOI 부호(LDPC의 군대수 아날로그)와 전용 BF 디코더 — 바이너리 표준 LDPC가 아닌 별도 부호족, NAND 이식성 없음
- **ID**: ieee:10619213
- **Type**: conference
- **Published**: 7-12 July 
- **Authors**: Fabian Molina, Paolo Santini, Marco Baldi
- **PDF**: https://ieeexplore.ieee.org/document/10619213
- **Abstract**: We introduce the family of Low-Density Orthogonal Idempotent (LDOI) codes, which are group codes characterized by two-sided ideals of a semisimple group algebra that have an orthogonal idempotent with low Hamming weight. These codes can be thought of as the analog, over a group algebra, of Low-Density Parity-Check (LDPC) codes over finite fields. We initiate the study of LDOI codes and characterize some of their properties in terms of weight of the orthogonal idempotent and the so-called adjacency matrix. We then show how the iterative Bit Flipping (BF) algorithm - the simplest form of decoder used for LDPC codes - can be adapted to decode LDOI codes. We show that, for certain families of LDOI codes (namely, those having a binary adjacency matrix), the BF decoder is optimal (i.e., achieves maximum error correction capability) even when just one iteration is performed.

## A Joint Code and Belief Propagation Decoder Design for Quantum LDPC Codes

- **Status**: ❌
- **Reason**: 양자 QLDPC 조인트 부호·디코더(quaternary BP, depolarizing 채널), 양자 전용 — 고전 바이너리 LDPC 이식성 없음
- **ID**: ieee:10619120
- **Type**: conference
- **Published**: 7-12 July 
- **Authors**: Sisi Miao, Jonathan Mandelbaum, Holger Jäkel +1
- **PDF**: https://ieeexplore.ieee.org/document/10619120
- **Abstract**: Quantum low-density parity-check (QLDPC) codes are among the most promising candidates for future quantum error correction schemes. However, a limited number of short to moderate-length QLDPC codes have been designed and their decoding performance is sub-optimal with a quaternary belief propagation (BP) decoder due to unavoidable short cycles in their Tanner graphs. In this paper, we propose a novel joint code and decoder design for QLDPC codes. The constructed codes have a minimum distance of about the square root of the block length. In addition, it is, to the best of our knowledge, the first QLDPC code family where BP decoding is not impaired by short cycles of length 4. This is achieved by using an ensemble BP decoder mitigating the influence of assembled short cycles. We outline two code construction methods based on classical quasi-cyclic codes and finite geometry codes. Numerical results demonstrate outstanding decoding performance over depolarizing channels.

## Progressive Reconstruction of Large QC-LDPC Codes over a Noisy Channel

- **Status**: ❌
- **Reason**: QC-LDPC 패리티검사행렬 blind 복원(비협력 통신 코드 인식) — 디코더/코드설계가 아니라 코드 식별 문제, NAND ECC 이식 기법 없음
- **ID**: ieee:10619372
- **Type**: conference
- **Published**: 7-12 July 
- **Authors**: Yuanbo Mi, Zhao Chen, Liuguo Yin +1
- **PDF**: https://ieeexplore.ieee.org/document/10619372
- **Abstract**: In non-cooperative communications, blind recognition of channel codes is the key to recover information from noisy intercepted messages. In this paper, we develop a progressive and iterative approach to reconstruct the parity-check matrices of large QC-LDPC codes under high bit error rate (BER). Specifically, in order to reduce the impact of noisy bits and improve efficiency for large codes, a novel sparse vector recovery (SVR) method based on sub-matrix sampling is first introduced. Then, SVR is operated iteratively after employing intermediate decoding with the partially reconstructed parity-check matrix on the intercepted messages. At last, the full parity-check matrix is built up progressively. Experimental results on a code of length 16200 show that the maximum bearable BER of the proposed approach to fully reconstruct is around 3E-4, at least 100 times higher than previous works.

## Multi-User SR-LDPC Codes via Coded Demixing with Applications to Cell-Free Systems

- **Status**: ❌
- **Reason**: sparse regression LDPC + coded demixing 다중접속(NOMA/cell-free) 통신 응용 특이, 떼어낼 ECC 기법 없음
- **ID**: ieee:10619473
- **Type**: conference
- **Published**: 7-12 July 
- **Authors**: Jamison R. Ebert, Jean-Francois Chamberland, Krishna R. Narayanan
- **PDF**: https://ieeexplore.ieee.org/document/10619473
- **Abstract**: Novel sparse regression LDPC (SR-LDPC) codes exhibit excellent performance over additive white Gaussian noise (AWGN) channels in part due to their natural provision of shaping gains. Though SR-LDPC-like codes have been considered within the context of single-user error correction and massive random access, they are yet to be examined as candidates for coordinated multi-user communication scenarios. This article explores this gap in the literature and demonstrates that SR-LDPC codes, when combined with coded demixing techniques, offer a new framework for efficient non-orthogonal multiple access (NOMA) in the context of coordinated multi-user communication channels. The ensuing communication scheme is referred to as MU-SR-LDPC coding. Empirical evidence suggests that MU-SR-LDPC coding can increase the sum-rate for a fixed Eb/N0 when compared to orthogonal multiple access (OMA) techniques such as time division multiple access (TDMA) or frequency division multiple access (FDMA). Importantly, MU-SR-LDPC coding enables a pragmatic solution path for user-centric cell-free communication systems with (local) joint decoding. Results are supported by numerical simulations.

## Analysis of Coded Shaped QAM Signaling at Short and Moderate Lengths

- **Status**: ❌
- **Reason**: NB-LDPC 부호 shaped QAM 거리특성 분석 — 비이진 LDPC + 변조 셰이핑 응용, 제외
- **ID**: ieee:10619186
- **Type**: conference
- **Published**: 7-12 July 
- **Authors**: Irina E. Bocharova, Boris D. Kudryashov, Sander Mikelsaar
- **PDF**: https://ieeexplore.ieee.org/document/10619186
- **Abstract**: This paper studies distance properties of coded modulation systems with shaping. The relation between Hamming spectra of a code and its squared Euclidean distance (SED) spectra is analyzed. The main focus of the paper is the so-called shaping after coding. Three shaping schemes based on different mappings of the code symbols onto the shaped QAM signals are proposed and analyzed. Examples of NB LDPC codes used in communication standards are considered. An approach to optimization of shaping books, which combines a genetic algorithm with optimization of the SED for the NB LDPC coded shaped signal sets, is studied. An approximation of the two-dimensional moment generating function for pairs of Hamming distances and SEDs for coded shaped signal sets is derived. A comparison of the estimated SED spectra for coded shaped signal sets with different mappings are presented.

## Trellis-Based Construction of Polar Codes for SCL Decoding

- **Status**: ❌
- **Reason**: SCL 디코딩용 polar 부호 구성 — 폴라 부호 전용, LDPC ECC와 무관
- **ID**: ieee:10619198
- **Type**: conference
- **Published**: 7-12 July 
- **Authors**: Xinyuanmeng Yao, Xiangping Zheng, Xiao Ma
- **PDF**: https://ieeexplore.ieee.org/document/10619198
- **Abstract**: In this paper, we propose an approach to construction of polar codes for successive cancellation list (SCL) decoding with a preset list size. For a given code length, we construct a trellis through which a path corresponds to a polar code. Then, we employ a sequential search algorithm to find an expected path based on four path metrics and five path selection rules. Additionally, for polarization-adjusted convolutional (PAC) construction, we optimize the convolutional generator polynomial based on our constructed polar code. Numerical results show that our polar/PAC codes can achieve satisfactory performance.

## Efficient Decoding of a Class of Reed-Solomon Codes Over Fermat Fields

- **Status**: ❌
- **Reason**: Reed-Solomon over Fermat field + SPC nested coding — LDPC 디코더/구성 기법 아님. NAND LDPC ECC에 이식할 기법 없음
- **ID**: ieee:10619665
- **Type**: conference
- **Published**: 7-12 July 
- **Authors**: Chao Chen, Baoming Bai, Xiao Ma +3
- **PDF**: https://ieeexplore.ieee.org/document/10619665
- **Abstract**: In this paper, we present an efficient decoding algorithm for a class of Reed-Solomon (RS) codes over Fermat field $\mathbb{F}_{2^{r}+1}$. We show that the Fermat number transform can be used to speed up the syndrome computation and the Chien search. The implementation architectures are designed for the two blocks. The key equation is then derived. When using the RS code in practice, there arises the issue that a $(2^{r}+1)$ -ary symbol is less efficiently represented by a tuple of $(r+1)$ bits. We present a nested coding scheme based on RS code and single parity-check (SPC) code to harness the inefficiency. A modified Wagner algorithm is proposed for decoding the inner (nonlinear) code and is proved to be an ML decoding over the BPSK-modulated AWGN channel. Simulation results show that the proposed RS-SPC nested coding scheme yields a considerable performance gain compared to the stand-alone RS coding scheme.

## Improved Logical Error Rate via List Decoding of Quantum Polar Codes

- **Status**: ❌
- **Reason**: 양자 polar code의 SCL 디코더 — LDPC 아니고 양자 전용, 이식 기법 없음
- **ID**: ieee:10619465
- **Type**: conference
- **Published**: 7-12 July 
- **Authors**: Anqi Gong, Joseph M. Renes
- **PDF**: https://ieeexplore.ieee.org/document/10619465
- **Abstract**: The successive cancellation list decoder (SCL) is an efficient decoder for classical polar codes with low decoding error, approximating the maximum likelihood decoder (MLD) for small list sizes. Here we adapt the SCL to the task of decoding quantum polar codes and show that it inherits the high performance and low complexity of the classical case, and can approximate the quantum MLD for certain channels. We apply SCL decoding to a novel version of quantum polar codes based on the polarization weight (PW) method, which entirely avoids the need for small amounts of entanglement assistance apparent in previous quantum polar code constructions. When used to find the precise error pattern, the quantum SCL decoder (SCL-E) shows competitive performance with surface codes of similar size and low-density parity check codes of similar size and rate. The SCL decoder may instead be used to approximate the probability of each equivalence class of errors, and then choose the most likely class. We benchmark this class-oriented decoder (SCL-C) against the SCL-E decoder and find a noticeable improvement in the logical error rate. This improvement stems from the fact that the contributions from just the low-weight errors give a reasonable approximation to the error class probabilities. Both SCL-E and SCL-C maintain the complexity O(LN log N) of SCL for code size $N$ and list size L.

## Outer Code Designs for Augmented and Local-Global Polar Code Architectures

- **Status**: ❌
- **Reason**: polar code outer code 설계 — LDPC 아니고 polar 전용 구성, 이식 기법 없음
- **ID**: ieee:10619561
- **Type**: conference
- **Published**: 7-12 July 
- **Authors**: Ziyuan Zhu, Paul H. Siegel
- **PDF**: https://ieeexplore.ieee.org/document/10619561
- **Abstract**: In this paper, we introduce two novel methods to design outer polar codes for two previously proposed concatenated polar code architectures: augmented polar codes and local-global polar codes. These methods include a stopping set (SS) construction and a nonstationary density evolution (NDE) construction. Simulation results demonstrate the advantage of these methods over previously proposed constructions based on density evolution (DE) and LLR evolution.

## Precoded Polar Product Codes

- **Status**: ❌
- **Reason**: precoded polar product codes, SC list 디코딩 — 폴라 부호 계열, LDPC 이식 기법 없음
- **ID**: ieee:10619420
- **Type**: conference
- **Published**: 7-12 July 
- **Authors**: Mustafa Cemil Coskun
- **PDF**: https://ieeexplore.ieee.org/document/10619420
- **Abstract**: Precoded polar product codes are proposed, where selected component codes enable successive cancellation list decoding to generate bit-wise soft messages efficiently for iterative decoding while targeting optimized distance spectrum as opposed to eBCH or polar component codes. Rate compatibility is a byproduct of 1-bit granularity in the component code design.

## Voronoi Constellations of Generalized Construction D’ Lattices from q-ary Codes

- **Status**: ❌
- **Reason**: q-ary code 기반 격자 Voronoi constellation — 비이진/격자 변조, LDPC 디코더·구성 아님
- **ID**: ieee:10619548
- **Type**: conference
- **Published**: 7-12 July 
- **Authors**: Ana Paula S. Pierini, Franciele C. Silva, Sueli I. R. Costa
- **PDF**: https://ieeexplore.ieee.org/document/10619548
- **Abstract**: In this paper, we present a scheme for obtaining Voronoi constellations of Generalized Construction D’ lattice obtained from q-ary codes. For this, we first extend the Generalized Construction D’ to a chain of linear q-ary codes, establish a connection with Construction A and derive a generator matrix, expressions for the minimum distance and the volume of this lattice. This connection also allowed to extend an efficient previous scheme for obtaining Voronoi constellations of Construction A to Generalized Construction D’ lattices.

## Minimizing Distortion in Data Embedding Using LDGM Codes and the Cavity Method

- **Status**: ❌
- **Reason**: LDGM 부호로 스테가노그래피 lossy 소스 코딩(임베딩 효율) — 채널 ECC 아닌 소스 코딩, 떼어낼 ECC 기법 없음
- **ID**: ieee:10619127
- **Type**: conference
- **Published**: 7-12 July 
- **Authors**: Masoumeh Alinia, David G. M. Mitchell
- **PDF**: https://ieeexplore.ieee.org/document/10619127
- **Abstract**: In this paper, we propose a lossy source coding approach to improve embedding efficiency in steganography. A higher embedding efficiency (decreasing the distortion function) is desirable since it leads to better security. We propose to use a soft-hard belief propagation guided decimation (BPGD) algorithm for the encoding problem with low-density generator matrix (LDGM) codes. However, for good distortion performance, the parameters of the soft or soft-hard BPGD need to be tuned. To achieve this, we apply the cavity method to predict a value called the dynamical phase transition, which can minimize the distortion function for the soft-hard BPGD. This approach facilitates secure steganography by finding optimal parameters for the distortion function without the need for exhaustive search and simulation. Our method is shown to outperform related works in terms of embedding efficiency, performance, and complexity.

## Enhanced ODMA with Channel Code Design and Pattern Collision Resolution for Unsourced Multiple Access

- **Status**: ❌
- **Reason**: 비이진 LDPC over GF(2^6) 명시 — 바이너리 한정 원칙으로 즉시 제외. 무선 ODMA 다중접속 응용이며 떼어낼 이식 ECC 기법 없음
- **ID**: ieee:10619608
- **Type**: conference
- **Published**: 7-12 July 
- **Authors**: Jianxiang Yan, Guanghui Song, Ying Li +2
- **PDF**: https://ieeexplore.ieee.org/document/10619608
- **Abstract**: An enhanced on-off division multiple access (ODMA) transmission scheme is proposed for unsourced multiple access network. The message of each active user is divided into two parts, where the first part is used to determine an on-off pattern, and the second part is encoded and transmitted in a time-hopping manner according to an on-off pattern. Leveraging the super sparse property of ODMA, the users' on-off pattern and pattern collisions are blindly detected based on the received signal without the help of pilot. Moreover, the on-off pattern detection, data decoding and collision recovery are performed iteratively over one sparse graph to enhance the overall system reliablity. We propose a finite-length performance analysis to the on-off pattern detection and iterative multi-user decoding, based on which both the user access sparsity, and channel code are optimized. Numerical result shows that with a rate 1/ 3 low-density parity-check code over G F (26), the gap between the proposed scheme and the random coding bound is less than 1.2 dB for up to 300 active users.

## CRYSTALS-Kyber With Lattice Quantizer

- **Status**: ❌
- **Reason**: Kyber/M-LWE 격자 양자화 KRM 암호 — ECC LDPC 아님, 보안 도메인
- **ID**: ieee:10619497
- **Type**: conference
- **Published**: 7-12 July 
- **Authors**: Shuiyin Liu, Amin Sakzad
- **PDF**: https://ieeexplore.ieee.org/document/10619497
- **Abstract**: Module Learning with Errors (M-LWE) based key reconciliation mechanisms (KRM) can be viewed as quantizing an M-LWE sample according to a lattice codebook. This paper describes a generic M-LWE-based KRM framework, valid for any dimensional lattices and any modulus $q$ without a dither. Our main result is an explicit upper bound on the decryption failure rate (DFR) of M-LWE-based KRM. This bound allows us to construct optimal lattice quantizers to reduce the DFR and communication cost simultaneously. Moreover, we present a KRM scheme using the same security parameters $(q, k, \eta_{1}, \eta_{2})$ as in Kyber. Compared with Kyber, the communication cost is reduced by up to 36.47% and the DFR is reduced by a factor of up to 299. The security arguments remain the same as Kyber.

## Flexible Field Sizes in Secure Distributed Matrix Multiplication via Efficient Interference Cancellation

- **Status**: ❌
- **Reason**: secure distributed matrix multiplication, GRS 코드 기반 — LDPC ECC 무관, 이식 기법 없음
- **ID**: ieee:10619357
- **Type**: conference
- **Published**: 7-12 July 
- **Authors**: Okko Makkonen
- **PDF**: https://ieeexplore.ieee.org/document/10619357
- **Abstract**: In this paper, we propose a new secure distributed matrix multiplication (SDMM) scheme using the inner product partitioning. We construct a scheme with a minimal number of workers and no redundancy, and another scheme with redundancy against stragglers. Unlike previous constructions in the literature, we do not utilize algebraic methods such as locally repairable codes or algebraic geometry codes. Our construction, which is based on generalized Reed-Solomon codes, improves the flexibility of the field size as it does not assume any divisibility constraints among the different parameters. We achieve a minimal number of workers by efficiently canceling all interference terms with a suitable orthogonal decoding vector. Finally, we discuss how the MDS conjecture impacts the smallest achievable field size for SDMM schemes and show that our construction almost achieves the bound given by the conjecture.

## Low-Complexity Constrained Coding Schemes for Two-Dimensional Magnetic Recording

- **Status**: ❌
- **Reason**: TDMR 제약 코딩(LOCO, GF(2)/GF(4)) — LDPC ECC 아닌 constrained coding, 비이진 포함
- **ID**: ieee:10619509
- **Type**: conference
- **Published**: 7-12 July 
- **Authors**: Doğukan Özbayrak, Duru Uyar, Ahmed Hareedy
- **PDF**: https://ieeexplore.ieee.org/document/10619509
- **Abstract**: The two-dimensional magnetic recording (TDMR) technology promises a remarkable increase in data storage density using the already-existing magnetic materials. Advanced TD signal processing techniques are required for this technology to fulfill its potential. Constrained coding, which prevents TD error-prone data patterns from being written, is among those techniques. In this paper, we propose lexicographically-ordered constrained (LOCO) coding schemes that offer low complexity, low latency, and low error propagation for TDMR systems with wide read heads, where coding can be applied on groups of 3 down tracks each. In particular, we introduce simple plus LOCO (SP-LOCO) and simple T LOCO (ST-LOCO) coding schemes, where codes defined over GF(2) and GF(4), respectively, are used instead of codes defined over GF (8), allowing the separation of uncoded streams. To better understand the behavior of the constrained-coded system, we derive the probability of transition, both in the horizontal and vertical directions, for the case of SP-LOCO and ST-LOCO coding, and we compare them to the case of optimal, rate-wise, LOCO codes. Moreover, we introduce simulation results on a practical TDMR model that demonstrate the performance gains achieved via the proposed schemes.

## Upper Bound on Coding Rate over Resistive Random-Access Memory Channel under Arbitrary Input Distribution

- **Status**: ❌
- **Reason**: ReRAM 채널 coding rate 상한 — 순수 정보이론 bound, 디코더/HW/코드구성으로 안 이어짐
- **ID**: ieee:10619343
- **Type**: conference
- **Published**: 7-12 July 
- **Authors**: Guanghui Song, Qi Cao, L. Ying +2
- **PDF**: https://ieeexplore.ieee.org/document/10619343
- **Abstract**: The achievable rate of code over resistive random-access memory (ReRAM) channel with finite selector failures was published in our recent work. The rate was derived under the assumption of independent and identically distributed (i.i.d.) input. In this work, focusing on the ReRAM channel in the case of single selector failure, we derive an upper bound on achievable rate under arbitrary input distribution. This upper bound is within 0.02 bits from the achievable rate of i.i.d. input, indicating that i.i.d. is very close to optimal for large memory arrays.

## Potential Functions and Percolation Thresholds of Coded Poisson Receivers

- **Status**: ❌
- **Reason**: Coded Poisson Receiver(IRSA 일반화) 안정영역·potential function 이론 — 다중접속 SIC 응용 이론, 떼어낼 LDPC ECC 기법 없음
- **ID**: ieee:10619176
- **Type**: conference
- **Published**: 7-12 July 
- **Authors**: Cheng-En Lee, Kuo-Yu Liao, Cheng-Shang Chang +1
- **PDF**: https://ieeexplore.ieee.org/document/10619176
- **Abstract**: As a generalization of Irregular Repetition Slotted ALOHA (IRSA), the probabilistic framework of coded Poisson receivers (CPR) offers a unified approach to analyze coded multiple access with successive interference cancellation (SIC). One crucial performance metric of CPRs is the stability region in which every packet can be successfully received with probability 1. In this paper, we use the potential function for convolutional Low Density Parity Check (LDPC) codes to derive the potential function for CPRs. Based on such a potential function, we derive three thresholds: the single-system threshold $G_{s}^{*}$ (for the original CPRs), the potential threshold $G_{conv}^{*}$ (for the convolutional CPRs), and the potential upper bound $G_{up}^{*}$. We prove that $G_{s}^{*} < G_{conv}^{*} < G_{up}^{*}$ • Our numerical results show that these thresholds match very well with existing works for D-fold ALOHA.

## Performance Analysis of Generalized Product Codes with Irregular Degree Distribution

- **Status**: ❌
- **Reason**: 일반화 곱부호(GPC) 비정칙 차수분포의 점근 성능 이론분석 — 디코더/HW/구성으로 안 이어지는 순수 이론 분석
- **ID**: ieee:10619134
- **Type**: conference
- **Published**: 7-12 July 
- **Authors**: Sisi Miao, Jonathan Mandelbaum, Lukas Rapp +2
- **PDF**: https://ieeexplore.ieee.org/document/10619134
- **Abstract**: This paper investigates the theoretical analysis of intrinsic message passing decoding for generalized product codes (GPCs) with irregular degree distributions, a generalization of product codes that allows every code bit to be protected by a minimum of two and potentially more component codes. We derive a random hypergraph-based asymptotic performance analysis for GPCs, extending previous work that considered the case where every bit is protected by exactly two component codes. The analysis offers a new tool to guide the code design of GPCs by providing insights into the influence of degree distributions on the performance of GPCs.

## Efficient Binary Batched Network Coding Employing Partial Recovery

- **Status**: ❌
- **Reason**: batched network coding(BATS) 디코더 — LDPC ECC 아닌 네트워크 코딩, 이식 대상 아님
- **ID**: ieee:10619504
- **Type**: conference
- **Published**: 7-12 July 
- **Authors**: Licheng Mao, Shenghao Yang
- **PDF**: https://ieeexplore.ieee.org/document/10619504
- **Abstract**: Batched network codes are a class of efficient random linear network coding schemes employing an outer-code-inner-code structure. In existing designs of efficient batched network codes, the decoding algorithm is a combination of intra-batch Gaussian elimination and inter-batch belief propagation, a process known as GE-BP decoding. To ensure close-to-optimal performance of GE-BP decoding, a large finite field is usually required in either the outer code or the inner code. However, GE-BP decoding over a large field incurs a high computation cost in both software and hardware implementations. In this paper, we introduce a new decoding algorithm that can achieve both the low computation cost of a binary outer code and a binary inner code, and the close- to-optimal decoding performance. Our algorithm takes advantage of the partial recovery property, which states that even when a system of linear equation has many solutions, certain variables may have a unique solution. This property can substantially improve the decoding performance for coding over the binary field. We provide the design and analysis of the decoding algorithm that employs partial recovery for BATS codes.

## Generalized Concatenated Polarization Kernels

- **Status**: ❌
- **Reason**: 극성 부호(polarization kernel) 기반 generalized concatenated codes로 SC list 디코더용 — LDPC가 아니고 이식할 LDPC 기법 없음
- **ID**: ieee:10619247
- **Type**: conference
- **Published**: 7-12 July 
- **Authors**: P. Trifonov
- **PDF**: https://ieeexplore.ieee.org/document/10619247
- **Abstract**: A novel class of polarization kernels is proposed, which is based on the construction of generalized concatenated codes. The complexity of the kernel processing operation, which is the computational core of the (list) successive cancellation decoder, for the obtained kernels of size 64 is several orders of magnitude less compared to BCH and Yao-Fazeli-Vardy kernels. Polar subcodes based on the obtained kernels under list successive cancellation decoder provide both performance and complexity improvement with respect to those based on the Arikan kernel.

## Blind Reconstruction of Binary Primitive BCH Code Based on Error Codeword Correction

- **Status**: ❌
- **Reason**: BCH 부호 blind reconstruction(생성다항식 식별) — LDPC 아니고 디코더/구성 이식 기법 없음
- **ID**: ieee:10695907
- **Type**: conference
- **Published**: 5-7 July 2
- **Authors**: Haochen Mu, Yunzhi Wu, Li Li
- **PDF**: https://ieeexplore.ieee.org/document/10695907
- **Abstract**: In this paper, a blind reconstruction method of binary primitive BCH code is proposed, which can identify the generator polynomial of BCH code from received noisy bitstreams. Firstly, error codewords are exposed according to the fact that correct codeword polynomials shall have consecutive roots. Secondly, the recovery of error codewords will be fast completed by leveraging the parity-check matrix of BCH code. Then, the consecutive roots of BCH code are determined by measuring the discrepancy between their experimental occurring probability and their theoretical occurring probability. Finally, the generator polynomial of BCH code are reconstructed based on the detected roots. Simulation results show that for the BCH codes whose error correction capability exceed 2 bits, the proposed method outperforms the reconstruction method using single-error correction.

## Dual-Use Secure Key Distribution Protocol Based on FEC-Aided Unidirectional BER Estimation

- **Status**: ❌
- **Reason**: FEC 기반 보안 키 분배 프로토콜. LDPC ECC 디코더/구성 기법 없음, 보안 응용 — 제외.
- **ID**: ieee:10975472
- **Type**: conference
- **Published**: 30 June-4 
- **Authors**: Di Wu, Lei Deng, Qi Yang +4
- **PDF**: https://ieeexplore.ieee.org/document/10975472
- **Abstract**: We propose a unidirectional dual-use secure key distribution protocol based on the forward-error-correction-aided bit error rate estimation. Hybrid automatic repeat request and adaptive coding techniques are integrated to enhance the reliability of communication section. A simulation is conducted in a turbulent channel to verify the feasibility of the proposed protocol.

## Data rates with microcomb distillation and adaptable LDPC codes rates

- **Status**: ❌
- **Reason**: adaptable LDPC rate로 microcomb 광전송 SNR/데이터레이트 계산. LDPC가 부수 도구, 떼어낼 디코더/구성 기법 없음 — 제외.
- **ID**: ieee:10975618
- **Type**: conference
- **Published**: 30 June-4 
- **Authors**: Jorge Acosta, Bill Corcoran
- **PDF**: https://ieeexplore.ieee.org/document/10975618
- **Abstract**: We calculate SNR gains and data rates using LDPC codes in a transmission model with frequency combs. The model incorporates distillation which is a method to filter noise between comb lines. Our simulations find the range of optical powers from which distillation will outperform a microcomb system without it.

## FPGA-based acceleration of QC-LDPC syndrome encoding for QKD systems

- **Status**: ❌
- **Reason**: QKD 정보 reconciliation용 QC-LDPC 신드롬 인코딩 FPGA 가속이나 표준 QC-LDPC를 그대로 사용, 양자 키분배 응용 — 제외.
- **ID**: ieee:10975689
- **Type**: conference
- **Published**: 30 June-4 
- **Authors**: Marco Origlia, Maximilien Pinaud, Luca Maggiani +2
- **PDF**: https://ieeexplore.ieee.org/document/10975689
- **Abstract**: Quantum Key Distribution (QKD) systems will be fundamental in ensuring secure communications in future networks. However, due to device imperfections and the random nature of quantum physics itself, these systems need an information reconciliation phase to correct for errors in the key exchange. In particular, for Continuous Variable QKD (CV-QKD) systems, it is possible to employ Multi-Dimensional Reconciliation (MDR) with Quasi-Cyclic LDPC (QC-LDPC) error correction codes. To achieve good reconciliation with low SNR or to limit finite- size effects, large input block codes should be employed. FPGA acceleration is here envisioned. In this work we implemented the encoding for syndromes as large as 1Mbit with a QC-LDPC lift factor of 512 bits and achieve a throughput exceeding 3.55 Gb/s.

## Complexity Reduction of Soft-decision FEC Using Nested Polar Code with Successive Cancelation Decoder

- **Status**: ❌
- **Reason**: Polar code + SC decoder 복잡도 감소. LDPC 아니며 떼어낼 LDPC 기법 없음 — 제외.
- **ID**: ieee:10975458
- **Type**: conference
- **Published**: 30 June-4 
- **Authors**: Zhiyuan Song, Yohei Koganei, Koji Igarashi
- **PDF**: https://ieeexplore.ieee.org/document/10975458
- **Abstract**: We propose a polar coding method to reduce complexity of soft-decision FEC in less than half with flexible FEC overhead. The degradation of BER performance is suppressed by less than 0.6 dB compared with BICM method.

## Nonlinear Tolerant Sphere Shaping with Dispersion-Aware Sequence Selection

- **Status**: ❌
- **Reason**: 비선형 광통신 sphere shaping/sequence selection — LDPC 무관, ECC 기법 아님
- **ID**: ieee:10975346
- **Type**: conference
- **Published**: 30 June-4 
- **Authors**: Jingtian Liu, Élie Awwad, Yves Jaouën
- **PDF**: https://ieeexplore.ieee.org/document/10975346
- **Abstract**: Energy dispersion index of dispersed sequences (DEDI) with sequence selection demonstrates nonlinear shaping gains of 0.3 and 0.03 bits/4D-symbol over single-span and multi-span links respectively against conventional sphere shaping.

## Enhancing Cloud Computing Data Security in Attribute-based Encryption Schemes using Cryptographic Algorithm

- **Status**: ❌
- **Reason**: 속성기반암호(ABE) post-quantum 보안 스킴, rank metric/low rank parity check 코드 기반 암호; 채널코딩 ECC 아니고 보안 도메인, 이식 기법 없음
- **ID**: ieee:10660882
- **Type**: conference
- **Published**: 3-4 July 2
- **Authors**: R. Yuvarani, R Mahaveerakannan
- **PDF**: https://ieeexplore.ieee.org/document/10660882
- **Abstract**: Attribute-Based Encryption (ABE) is a powerful cryptographic technology used in cloud computing and data security. It allows data owners to control access to encrypted data based on specific characteristics rather than individual user IDs. This makes sure that only systems that satisfy certain requirements or people, who are allowed may decode and view the data. Because of its dynamic and adaptable approach to access management, ABE is a great fit for situations with complex and dynamic access requirements. In response to the threat posed by Quantum Computing, this research study focused on developing Post-Quantum ABE schemes that maintain security while also addressing attributes like verifiability, user privacy, and revocability. A novel ABE system founded on rank metric codes has been proposed. The proposed approach is built on low rank parity check codes with a robust resistance against diverse forms of attacks with a compact key size and rapid execution time, demonstrating notable efficiency when compared to other cryptographic systems. This represents a substantial stride forward in enhancing Cloud Computing in the era of Quantum Computing.

## An Enhanced Polar-LDPC Concatenated Protection Scheme Utilizing Optimized Critical Sets

- **Status**: ❌
- **Reason**: Polar-LDPC 연접 보호에서 polar critical set 선택이 핵심 기여, LDPC는 베이스라인이고 떼어낼 LDPC 기법 없음
- **ID**: ieee:10648465
- **Type**: conference
- **Published**: 26-29 July
- **Authors**: Chen Hou, Hongjun Zhu, Yunlong Han +2
- **PDF**: https://ieeexplore.ieee.org/document/10648465
- **Abstract**: Polar codes are a class of coding schemes that have been theoretically proven to achieve the capacity in binary-input memoryless symmetric channels, thereby becoming a prominent research focus in communications research. Although polar codes theoretically approach the Shannon limit as the code length increases indefinitely, their performance is inherently limited at finite-length codes due to incomplete channel polarization. To address this limitation, we propose an optimized critical sets(OCS) selection method specifically designed for error sets within polar codes, aiming to optimize the selection strategy for intermediate-quality channels. Subsequently, a polar-LDPC concatenated protection scheme is introduced, which utilizes the OCS to effectively protect the error set information bits, thus enhancing the overall protection scheme. The simulation results show that the OCS approach exhibits a more precise selection of intermediate-quality channels, resulting in a significant performance improvement of approximately 1 dB compared to alternative protection schemes.

## Research on the Cascaded KP4 and Zipper Codes Based on Optimized Sliding Window Decoder

- **Status**: ❌
- **Reason**: KP4+zipper 코드 cascaded 슬라이딩윈도우 디코더 - LDPC가 아닌 광통신 FEC, 이식 LDPC 기법 없음
- **ID**: ieee:10648407
- **Type**: conference
- **Published**: 26-29 July
- **Authors**: Qianhui Guo, Feng Tian, Ze Dong +5
- **PDF**: https://ieeexplore.ieee.org/document/10648407
- **Abstract**: We adopt a novel structure of cascaded KP4 and zipper codes based on optimized sliding window decoder. By optimizing the hard-decision decoder and interleaver length, the pre-FEC BER threshold of error-free transmission is approximately 0.7E-2.

## Experimental Demonstration on Modified CAZAC Matrix-Based Precoding for OFDM/QNSC

- **Status**: ❌
- **Reason**: OFDM/QNSC용 CAZAC 행렬 프리코딩으로 LDPC 무관, 무선 광통신 특이적
- **ID**: ieee:10648394
- **Type**: conference
- **Published**: 26-29 July
- **Authors**: Mengwen Pan, Jing Yan, W. Ying +6
- **PDF**: https://ieeexplore.ieee.org/document/10648394
- **Abstract**: This paper proposes a modified CAZAC Matrix-based precoding scheme for OFDM/QNSC system. Experimental results verify that our scheme achieves a ~1.2dB PAPR reduction and ~2dB BER improvement compared to original CAZAC matrix.

## Performance of CA-Polar Codes Serial Concatenated with RLL Code Using SCL-SGRAND on VLC

- **Status**: ❌
- **Reason**: Polar/GRAND 기반 SCL-SGRAND 복조(VLC) — Polar 코드 대상이고 LDPC 디코더 기법 아님
- **ID**: ieee:10796049
- **Type**: conference
- **Published**: 24-25 July
- **Authors**: Igor Novid, Hiroshi Kamabe, Shan Lu
- **PDF**: https://ieeexplore.ieee.org/document/10796049
- **Abstract**: The Guessing Random Additive Noise Decoding (GRAND) algorithm is a well-established hard-decision technique that achieves maximum likelihood (ML) decoding performance. A recent variant, Soft-GRAND (SGRAND), can utilize soft information as input and is applicable to various short, high-rate block codes. We propose a scheme called successive-cancellation list (SCL)-SGRAND, where SCL decoding is employed to generate both soft information (reliability estimates) and initial hard bit decisions. These decisions are then improved using SGRAND when they fail to satisfy the cyclic redundancy check (CRC) condition. This combined approach allows SCL-SGRAND to outperform both the original SCL and SGRAND decoders. To evaluate its performance, we compare SCL-SGRAND's performance on CRC-aided Polar (CA-Polar) codes, serially concatenated with Run-Length Limited (RLL) codes (a common configuration for Visible Light Communication (VLC)), against SCL decoding and SGRAND under identical channel conditions (e.g., AWGN channel). The simulation results demonstrate that the proposed SCL-SGRAND scheme outperforms both SCL and SGRAND, achieving gains of between 0.2 and 1 dB for bit error rate (BER) and between 0.3 and 0.6 dB for block error rate (BLER).

## Leveraging mmWave Channel Coding for Enhanced Reliability in 6G High-Throughput Satellite Communications

- **Status**: ❌
- **Reason**: 6G 위성 mmWave에서 Turbo/LDPC/polar를 응용 서베이; 떼어낼 새 기법 없음
- **ID**: ieee:10668326
- **Type**: conference
- **Published**: 22-23 July
- **Authors**: Ambar Bajpai, Nagarjuna Telagam
- **PDF**: https://ieeexplore.ieee.org/document/10668326
- **Abstract**: This paper explores the potential of leveraging millimeter-wave (mmWave) channel coding techniques to enhance reliability in 6G high-throughput satellite communications. With the increasing demand for high data rates and low latency in future wireless networks, mmWave frequencies have emerged as a promising solution to achieve ultra-high throughput. However, mmWave communications are susceptible to atmospheric attenuation and fading, posing significant challenges to reliable data transmission. This paper investigates the application of advanced channel coding schemes, such as Turbo codes, LDPC codes, and polar codes, to mitigate the effects of channel impairments and improve the reliability of mmWave communications in 6G systems.

## Blind Detection of Channel Coding and Interleaving Using Convolutional Neural Networks in Tactical Communications

- **Status**: ❌
- **Reason**: CNN blind detection of channel coding/interleaving; no LDPC ECC technique
- **ID**: ieee:10625139
- **Type**: conference
- **Published**: 2-5 July 2
- **Authors**: Seok-Jin Hong, Woong-Jong Yun, Eui-Rim Jeong
- **PDF**: https://ieeexplore.ieee.org/document/10625139
- **Abstract**: This paper proposes two Convolutional Neural Network (CNN) models for classifying types of channel codings and interleavings blindly in military communications. In tactical communications, eavesdropping of enemy's signal requires blind recognition of the channel coding and interleaving methods. In this study, we introduce a channel coding estimation CNN model that classifies between two widely used convolutional error correction codes and one Reed-Solomon error correction code in military communications. Additionally, our interleaver classifier distinguishes between data processed with block interleavers and data without interleaving. The performance of the proposed CNN models is evaluated through computer simulations and compared with well-known CNN models, VGG and ResNet. The proposed models demonstrate comparable performance with significantly fewer parameters, highlighting their potential for efficient implementation in military communication systems.

## Consideration of Frequency Domain Adaptive SIC for Full-Duplex Communication

- **Status**: ❌
- **Reason**: Full-duplex self-interference cancellation; no LDPC content
- **ID**: ieee:10625503
- **Type**: conference
- **Published**: 2-5 July 2
- **Authors**: Kazuma Matsushima, Takumi Yasaka, Hiroyuki Otsuka
- **PDF**: https://ieeexplore.ieee.org/document/10625503
- **Abstract**: Full-duplex communication has gained attention as a potential solution for increasing the spectral efficiency which allows simultaneous transmission and reception on the same carrier frequency. Self-interference canceller (SIC) must be needed in scenarios where full-duplex communication is desired. We propose frequency domain adaptive SIC using a specific demodulation reference signal (DMRS) which is special type of physical layer signal. The proposed SIC can estimate the channel response of SI in real time using DMRS and eliminate the SI. In this paper, we first show the configuration of the proposed adaptive SIC using the DMRS. Then, we show the BER performance of OFDM signals whose symbol modulations are QPSK to 1024-QAM for different types of DMRS mapping. The simulation results verify that the proposed adaptive SIC can sufficiently eliminate SI and improve the BERs of OFDM signals under the enormous amount of SI.

## Distributed Source Coding for the Quantum Communication

- **Status**: ❌
- **Reason**: 분산 소스 코딩(DSC) + 압축, 채널코딩 ECC 아님 — 소스 코딩 제외
- **ID**: ieee:10704443
- **Type**: conference
- **Published**: 19-21 July
- **Authors**: Hui Chen, Lizhen Wang
- **PDF**: https://ieeexplore.ieee.org/document/10704443
- **Abstract**: Considering the shortcomings of distributed source coding (DSC) in quantum communication, such as the high bit error rate and low compression ratio, an improved distributed source coding is proposed in this paper. In the design of the source encoder, redundancy technology is used to provide error protection, and then the joint design of Low-Density Parity Check code (LDPC) with redundancy is adopted to conduct distributed source coding. Experiment results show that the proposed method can be kept the compression ratio well and be easily implemented when a strong internal correlation of the quantum communication areas. The the reconstructed sequence can reach low bit error rate when the correlation between sources are weak. It is a practical, efficient DSC scheme.

## Simulation and Thinking of QPSK Modulation and Demodulation

- **Status**: ❌
- **Reason**: QPSK 변복조 MATLAB 시뮬레이션 — LDPC/ECC 무관
- **ID**: ieee:10704452
- **Type**: conference
- **Published**: 19-21 July
- **Authors**: Xuenan Liang, Binnian Wang, Delong Li +1
- **PDF**: https://ieeexplore.ieee.org/document/10704452
- **Abstract**: Multi-input frequency shift keyying can overcome the problem of low band utilization rate in the process of binary frequency shift keyying, and has a wide practical application range. In order to better and more intuitively understand the modulation and demodulation principle of multi-carry frequency shift keyying, this paper analyzes the modeling and demodulation of QPSK with the help of MATLAB simulation software. The simulation experimental data show that the simulation results and the theoretical analysis content are consistent, which verifies the correctness of the simulation model. QPSK RF direct modulation anti-interference ability, high transmission code rate and high reliability can be applied to the environment of remote sensing satellite communication.

## Blind Reconciliation with Protograph LDPC Code Extension for FSO-Based Satellite QKD Systems

- **Status**: ❌
- **Reason**: QKD key reconciliation용 protograph LDPC 확장 구성 — 양자/QKD 보안 도메인이고 reconciliation은 채널 ECC가 아닌 정보 조정. 떼어낼 고전 ECC 신규 기법 없음
- **ID**: ieee:10636513
- **Type**: conference
- **Published**: 17-19 July
- **Authors**: Cuong T. Nguyen, Hoang D. Le, Vuong V. Mai +2
- **PDF**: https://ieeexplore.ieee.org/document/10636513
- **Abstract**: A significant breakthrough in space-based quantum key distribution (QKD) inaugurated by the Micius satellite has brought us closer to the era of global QKD networks. An essential step in the post-processing QKD is key reconciliation (KR), which eliminates the mismatch in the raw keys between two legitimate users. However, the fluctuation in the quantum bit-error rate (QBER) caused by the free-space optical (FSO) turbulence channels poses various challenges for the KR design. This paper addresses the design of blind KR schemes for FSO-based low Earth orbit (LEO) satellite QKD systems, which allow operating without a prior QBER estimation. Specifically, we present a novel blind KR scheme with a protograph low-density parity check (LDPC) code extension. The proposed LDPC structure is constructed by gradually extending and exhaustively searching among all possible solutions. The proposed design is evaluated in terms of the final key rate performance over the QKD systems using a dual-threshold/direct detection (DT/DD) scheme. Simulation results confirm the effectiveness of our proposed design compared to the state-of-the-art design in different turbulence channel conditions.

## Energy Efficient Non-Orthogonal Signalling with Probabilistic Shaping for Wireless Transmissions

- **Status**: ❌
- **Reason**: 무선 SEFDM + probabilistic shaping. LDPC는 표준 SD-FEC 베이스라인으로 부수 언급, 떼어낼 ECC 기법 없음
- **ID**: ieee:10636633
- **Type**: conference
- **Published**: 17-19 July
- **Authors**: Xinyue Liu, Izzat Darwazeh
- **PDF**: https://ieeexplore.ieee.org/document/10636633
- **Abstract**: This work explores the realistic operation of a recently reported concept by the authors11The probabilistically shaped-SEFDM concept was first reported by the authors in the IEEE VTC-Spring 2021. This paper extends earlier transmission systems design by using channel estimation and equalisation system components. The results of this work are published here openly for the first time. They form part of Xinyue Liu's PhD 2023 thesis [1]., which considers the use of probabilistic shaping for the non-orthogonal multicarrier spectrally efficient frequency division multiplexing (SEFDM) system. In this paper, we extend the operation of earlier signal and system designs, which considered only a simple AWGN channel, to realistic wireless environments with the focus of the studies on two frequency selective channels, namely a four-tap channel and Rummler's channel. The special system design for probabilistic shaping adopts a reverse concatenation architecture that cascades the constant composition distribution matching (CCDM) algorithm together with soft-decision forward error correction (SD-FEC) - LDPC code. The paper presents detailed system modelling and simulation results, which clearly establish that, with pilot tone based channel estimation and equalisation, SEFDM with probabilistic shaping shows significant advantages, in both energy efficiency and robust-ness against wireless channel impairments, when compared to OFDM of the same spectral efficiencies.

## Flexible Blind Information Reconciliation for QKD based on Rateless Protograph LDPC codes

- **Status**: ❌
- **Reason**: QKD 정보조정용 rateless protograph LDPC — QKD 보안용, 떼어낼 고전 ECC 새 기여 없음 제외
- **ID**: ieee:10648040
- **Type**: conference
- **Published**: 14-18 July
- **Authors**: Marco Ferrari, Alberto Tarable, Rudi P. Paganelli
- **PDF**: https://ieeexplore.ieee.org/document/10648040
- **Abstract**: Information Reconciliation (IR) is a crucial step in the process of distillation of unconditionally secure keys in Quantum key distribution (QKD). Novel IR rateless codes based on protograph low-density parity-check (LDPC) codes have been recently designed to replace Cascade. In this paper, a blind IR protocol is described that exploits all the features of rateless protograph LDPC codes.

## Impact of Limited Classical Channel Bandwidth on the Secret Key Rate of a CV-QKD System

- **Status**: ❌
- **Reason**: CV-QKD 고전채널 대역폭/조정 분석 — QKD 보안, LDPC 부수 언급, 제외
- **ID**: ieee:10648210
- **Type**: conference
- **Published**: 14-18 July
- **Authors**: Nuno A. Silva, Margarida Almeida, Nelson J. Muga +1
- **PDF**: https://ieeexplore.ieee.org/document/10648210
- **Abstract**: Continuous-variable quantum key distribution (CV-QKD) can extract secret keys in an efficient and practical manner using off-the-shelf telecommunication equipment. This sets CV-QKD as a key technology for implementation in optical fiber networks already deployed in the field. Notwithstanding, the extraction of secret keys in CV-QKD requires the exchange of information, not only on a quantum channel, but also on an authenticated and public classical channel. The classical channel is required to exchange part of the coherent states to aid with the parameter estimation step to conclude on the secrecy of the extracted key, and to exchange side information essential to the reconciliation step. Here, we study the bandwidth demand of the information exchanged in the classical channel and how it can impact the extraction key rate of a CV-QKD system. The post-processing step consuming the highest bandwidth of the classical channel is the reconciliation step, due to the exchange of the side information. We consider different dimensions for the multidimensional reconciliation demanding different bandwidths on the classical channel and compute the allowed extraction key rate depending on the performance of the method, in terms of frame error rate.

## Iterative Detection and Decoding for RIS-Assisted Multiuser Multiple-Antenna Systems

- **Status**: ❌
- **Reason**: RIS 다중안테나 IDD에 표준 LDPC 결합 — 떼어낼 새 디코더/구성 없음, 무선 응용 특이적 제외
- **ID**: ieee:10639075
- **Type**: conference
- **Published**: 14-17 July
- **Authors**: Roberto C. G. Porto, Rodrigo C. de Lamare
- **PDF**: https://ieeexplore.ieee.org/document/10639075
- **Abstract**: We present a novel iterative detection and decoding (IDD) scheme for Reconfigurable Intelligent Surface (RIS)assisted multiuser multiple-antenna systems. The proposed approach introduces a joint iterative detection strategy that integrates Low-Density Parity-Check (LDPC) codes, RIS processing and iterative detection and decoding. In particular, we employ a minimum mean square error receive filter that performs truncation at the RIS and soft interference cancelation at the receiver. Simulation results evaluate the system’s overall capacity and bit error rate, and demonstrate substantial improvements in bit error rate across block-fading channels.

## Coding Solutions for Robust Performance in Wireless Systems

- **Status**: ❌
- **Reason**: Wi-Fi 무선용 코딩(터보·LDPC·space-time) 일반 서베이성 언급 — LDPC 부수 언급, 새 기법 없음
- **ID**: ieee:10691978
- **Type**: conference
- **Published**: 12-14 July
- **Authors**: Vaishali Singh, Rajesh Gupta, K S Srinivasa Rao
- **PDF**: https://ieeexplore.ieee.org/document/10691978
- **Abstract**: Wi-Fi structures require reliable coding solutions to ensure robust overall performance. Latest advances in wireless technologies have accelerated the want for reliable coding strategies to catch up on signal losses because of shadowing, fading, and imperfect channel situations. Traditional coding techniques, together with forward mistakes correction (FEC) and variety coding, conflict to hold strong performance underneath challenging conditions. New coding strategies are needed to ensure a reliable Wi-Fi communique in difficult propagation environments. Recent research in coding answers for robust wireless systems has explored a selection of methods, such as faster codes, Low-Density Parity-test (LDPC) codes, and area-time coding. LDPC codes offer extended code lengths, which boosts coding benefits and features quite low computational complexity. Area-time codes are a block coding method that improves blunder resilience by utilizing a couple of antennas and transmitting the identical sign in more than one direction simultaneously. These coding answers were implemented to provide improved overall performance in diverse Wi-Fi systems, which include cell, WLAN, and satellite TV for PC communiqué networks. Particularly, turbo codes, LDPC codes, and area-time codes have been used effectively in WLAN networks to reduce channel mistakes and growth records prices, in addition to in mobile networks to enhance spectral efficiency and offer better throughput.

## New Constructions of Even-Length Perfect Gaussian Integer Sequences

- **Status**: ❌
- **Reason**: 완전 가우시안 정수 시퀀스(PGIS) 구성 — 시퀀스 설계로 LDPC ECC 디코더/코드 무관
- **ID**: ieee:10671559
- **Type**: conference
- **Published**: 12-14 July
- **Authors**: Chong-Dao Lee, Kun-Lin Lee
- **PDF**: https://ieeexplore.ieee.org/document/10671559
- **Abstract**: Perfect Gaussian integer sequences (PGISs) with ideal periodic autocorrelation functions have been extensively used to communication systems and cryptosystems. This paper propose several new families of even-length PGISs based on novel base sequences. The resulting sequences consists of at most 12 Gaussian integers. The new developed construction method is to use Gaussian integers of different Euclidean norms as the coefficients of a linear combination of the newly presented and previously developed base sequences. Both theoretical proofs and illustrated examples for new PGISs are given. The advantages of these new PGISs are either low energy or large degree when compared to the existing sequences.

## CosinePrism: An Unequal Error Protection Scheme for Progressive Image Transmission Over Half-Duplex Channels

- **Status**: ❌
- **Reason**: 이미지 점진 전송용 UEP(FEC 할당) 기법, 채널코딩 LDPC ECC 기법 아님
- **ID**: ieee:10631588
- **Type**: conference
- **Published**: 1-4 July 2
- **Authors**: Aravind Voggu, Madhav Rao
- **PDF**: https://ieeexplore.ieee.org/document/10631588
- **Abstract**: In this work, we propose an Unequal Error Pro-tection technique suitable for scenarios that demand low power consumption and are equipped with limited computationally ca-pabilities. CosinePrism incorporates colour theory and techniques from lossy image compression methods towards optimizing the allocation of Forward Error Correction factor. CosinePrism can progressively deliver RGB and non-RGB images over half-duplex links, and includes a JPEG re-compression mode. The proposed technique achieves compression efficiency and image quality comparable to JPEG, and on an average offers DSSIM score improvement of 55.5% over Equal Error Protection method. An open-source reference encoder is provided for further research and development to the community.

## On Progressive Edge Growth Parity Check Matrix Generation for NB-LDPC Codes in HF Communications

- **Status**: ❌
- **Reason**: HF 채널용 NB-LDPC(비이진) PEG 파라미터 조정, 비이진 LDPC로 즉시 제외
- **ID**: ieee:10617767
- **Type**: conference
- **Published**: 1-3 July 2
- **Authors**: E. M. Lobov, A. D. Grigorieva, V. O. Varlamov
- **PDF**: https://ieeexplore.ieee.org/document/10617767
- **Abstract**: This work explores the research and development of a Progressive Edge Growth (PEG) algorithm parameter setting method for the forming parity-check matrices of Low- density parity-check (LDPC) codes, which is an important task in the field of communications in the development of radio links operating in the high frequency ionospheric channel. This channel is characterised by a particularly complex interference environment, which, when using non-binary signal-code constructions with high redundancy on the basis of direct sequence spectrum spread makes it impossible to use noise- resistant codes with a large code block length. This article describes in detail the method of effective adjustment of the PEG algorithm of LDPC parity check matrix generation in order to increase reliability and noise immunity of communication in conditions with restrictions on the code length. The result of the article is a quantitative performance assessment of the choice of parameters of PEG in noise immunity using LDPC codes for the communication system used in the ionospheric channel. The bit error rate was used as a criterion for noise immunity.

## Performance Evaluation of LDPC Codes in 5G NR

- **Status**: ❌
- **Reason**: 5G NR 표준 LDPC를 MATLAB로 시뮬레이션한 성능 평가, 표준 부호 단순 재사용·새 기여 없음
- **ID**: ieee:10617595
- **Type**: conference
- **Published**: 1-3 July 2
- **Authors**: Sergey Portnoy, Andrey Tikhonyuk, Sergey Nikitin +1
- **PDF**: https://ieeexplore.ieee.org/document/10617595
- **Abstract**: The evolution of mobile communication systems demands the integration of advanced error correction techniques, such as Low-Density Parity-Check (LDPC), to ensure reliable data transmission with low latency. This paper focuses on software implementation of LDPC codec simulation, specified in the 5G NR standard (3GPP TS 38.212), using MATLAB.

## Investigation of Digital Communication Lines Noise Immunity in Hydroacoustic Channel Using Various Types of Product Turbo Code

- **Status**: ❌
- **Reason**: 수중음향 채널 product turbo code 잡음내성 연구, LDPC 아님·이식 기법 없음
- **ID**: ieee:10617661
- **Type**: conference
- **Published**: 1-3 July 2
- **Authors**: L. M. Kazadaev, A. I. Sattarova, K. Yu. Ryumshin
- **PDF**: https://ieeexplore.ieee.org/document/10617661
- **Abstract**: The acoustic method of communication and data transmission is widely used for seabed exploration, transmission of various sonar signals, message transmission etc. due to its ability to transmit data over long distances. The transmission speed is a secondary, but still important characteristic of the communication and data transmission system. The hydroacoustic communication channel is noted for its negative characteristics, which directly affect the transmission of the acoustic signal. In addition, acoustic noise of industrial and natural origin introduces additional interference into the process of transmitting a useful signal. The purpose of this article is to study the noise immunity of a communication and data transmission system with various types of product turbo codes in order to increase the noise immunity of the transmitted signal with minimal damage to the data rate.
