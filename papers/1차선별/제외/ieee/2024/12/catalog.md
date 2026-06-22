# IEEE Xplore — 2024-12


## Code Synchronization in Visible Light Communication System Using Dual Orthogonal Rolling Shutter Image Sensors

- **Status**: ❌
- **Reason**: VLC 코드 동기화에 LDPC 적용 — 동기화 기법이 본질, 떼어낼 디코더/코드 기법 없는 응용 특이적
- **ID**: ieee:10591719
- **Type**: journal
- **Published**: December 2
- **Authors**: Ayumu Otsuka, Zhengqiang Tang, Shan Lu +1
- **PDF**: https://ieeexplore.ieee.org/document/10591719
- **Abstract**: A visible light communication (VLC) system offers notable advantages, and leveraging image sensors as VLC receivers holds promise. The rolling shutter image sensor stands out as a popular candidate among these sensors. However, challenges arise from signal loss from inter-frame gaps or background scans. This paper addresses these issues by introducing a low-density parity check (LDPC) code and a corresponding code synchronization method suitable for LDPC decoding. Our approach employs a parallel transmitting sequence to achieve synchronization. Notably, the synchronization sequence is transmitted by modulating the luminance of the LED transmitter. Through experimentation, we validate the efficacy of our proposed method in mitigating signal loss.

## Toward Practical HARQ-Based RC-LDPC Design for Optical Satellite-Assisted Vehicular Networks

- **Status**: ❌
- **Reason**: FSO LEO 위성 IR-HARQ 링크설계, 기존 PBRL-LDPC를 그대로 사용하고 goodput/지연 분석에 그침 — 새 LDPC 기여 없는 응용 특이적
- **ID**: ieee:10613470
- **Type**: journal
- **Published**: Dec. 2024
- **Authors**: Cuong T. Nguyen, Hoang D. Le, Chuyen T. Nguyen +1
- **PDF**: https://ieeexplore.ieee.org/document/10613470
- **Abstract**: Free-space optics (FSO)-based low-Earth orbit (LEO) satellite systems have recently aroused considerable attention as an enabling technology for the Internet of Vehicles (IoVs) applications. However, such systems face critical challenges, including cloud coverage, atmospheric turbulence, and pointing errors. This article addresses a link-layer error-control design solution, which is a combination of the low-density parity check (LDPC) code and the incremental redundancy (IR)-hybrid automatic repeat request (HARQ) protocol. We consider a subclass of rate-compatible (RC)-LDPC code extension, i.e., protograph-based raptorlike (PBRL)-LDPC codes, for the proposed IR-HARQ design. In addition, we provide a comprehensive analytical framework to obtain performance metrics, including goodput, energy efficiency, and average frame delay. Numerical results highlight the outperformance of the design proposal compared to conventional link-layer solutions in FSO-based LEO satellite systems. Also, we provide a design guideline regarding the proper selection of transmitted power and decoding complexity concerns. Furthermore, we investigate the feasibility of our design proposal for a study case involving the existing Japan LEO satellite networks and the moving vehicles. Finally, we conduct the Monte-Carlo simulations to validate the correctness of theoretical results.

## 5G NR Codes and Modulation Deep-RL Optimization for uRLLC in Vehicular OCC

- **Status**: ❌
- **Reason**: 차량 OCC용 deep-RL 코드레이트/변조 최적화, 5G NR LDPC를 그대로 사용 — 새 LDPC 기여 없는 응용 특이적
- **ID**: ieee:10700659
- **Type**: journal
- **Published**: Dec. 2024
- **Authors**: Amirul Islam, Nikolaos Thomos, Leila Musavian
- **PDF**: https://ieeexplore.ieee.org/document/10700659
- **Abstract**: In dynamic and time-varying vehicular networks, existing vehicular communication systems cannot guarantee ultra-reliable and low latency communication (uRLLC). To address this, we propose a novel deep reinforcement learning-based vehicular optical camera communication (OCC) system with an aim to maximize the throughput and ensure uRLLC. To achieve this, our scheme chooses the optimal code rate, modulation scheme and speed of vehicles for multiple vehicular links. We use OCC, which offers interference-free communication as an alternative to radio frequency systems. Moreover, we employ 5G New Radio low-density parity-check codes and an adaptive modulation scheme to support variable rates and ultra-reliability. The proposed large-scale and continuous problem is solved through an actor-critic algorithm based on Wolpertinger architecture. We extendedly evaluate the system performance and compare it with several other schemes from the literature as well as with variants of our scheme. We observe from the results that the proposed method achieves higher average throughput and lower latency than all the other schemes under comparison. Further, the proposed scheme can meet the uRLLC constraints, whereas other schemes under comparison fail to respect these constraints most of the time.

## Capacity Achieving Channel Codes for an Erasure Queue-Channel

- **Status**: ❌
- **Reason**: erasure queue-channel용 interleaving wrapper와 표준 LDPC/Polar 성능 분석일 뿐, 새 디코더/구성/HW 기여 없음 — 큐채널 응용 특이적
- **ID**: ieee:10570453
- **Type**: journal
- **Published**: Dec. 2024
- **Authors**: Jaswanthi Mandalapu, Krishna Jagannathan, Andrew Thangaraj
- **PDF**: https://ieeexplore.ieee.org/document/10570453
- **Abstract**: We consider a queue-channel model that captures the waiting time-dependent degradation of information bits as they wait to be transmitted. Such a scenario arises naturally in quantum communications, where information bits become useless after a certain time. Trailing the capacity results obtained recently for certain queue-channels, this paper aims to construct practical channel codes for the erasure queue-channel (EQC)—a channel characterized by highly correlated erasures, governed by the underlying queuing dynamics. Our main contributions in this paper are twofold: (i) We propose a generic ‘wrapper’ based on interleaving across renewal blocks of the queue to convert any capacity-achieving code for a memoryless erasure channel to a capacity-achieving code for the EQC. Next, due to the complexity involved in implementing interleaved systems, (ii) we study the performance of LDPC and Polar codes without any interleaving. Motivated by the empirical performance, we show that standard Arıkan’s Polar transform polarizes the M/M/1 EQC.

## 2D-RC: Two-Dimensional Neural Network Approach for OTFS Symbol Detection

- **Status**: ❌
- **Reason**: OTFS 심볼 검출용 2D reservoir computing 신경망, LDPC ECC와 무관
- **ID**: ieee:10623419
- **Type**: journal
- **Published**: Dec. 2024
- **Authors**: Jiarui Xu, Karim Said, Lizhong Zheng +1
- **PDF**: https://ieeexplore.ieee.org/document/10623419
- **Abstract**: Orthogonal time frequency space (OTFS) is a promising modulation scheme for wireless communication in high-mobility scenarios. Recently, a reservoir computing (RC) based approach has been introduced for online subframe-based symbol detection in the OTFS system, where only a limited number of over-the-air (OTA) pilot symbols are utilized for training. However, this approach does not leverage the domain knowledge specific to the OTFS system to fully unlock the potential of RC. This paper introduces a novel two-dimensional RC (2D-RC) method that incorporates the domain knowledge of the OTFS system into the design for symbol detection in an online subframe-based manner. Specifically, as the channel interaction in the delay-Doppler (DD) domain is a two-dimensional (2D) circular operation, the 2D-RC is designed to have the 2D circular padding procedure and the 2D filtering structure to embed this knowledge. With the introduced architecture, 2D-RC can operate in the DD domain with only a single neural network, instead of necessitating multiple RCs to track channel variations in the time domain as in previous work. Numerical experiments demonstrate the advantages of the 2D-RC approach over the previous RC-based approach and compared model-based methods across different OTFS system variants and modulation orders.

## Two RRNS-Based Error Correction Schemes for DNA Storage Channels

- **Status**: ❌
- **Reason**: DNA 저장용 RRNS 코드(잔여수계+marker), LDPC ECC 무관 — 채널코딩 LDPC 기법 없음
- **ID**: ieee:10718282
- **Type**: journal
- **Published**: Dec. 2024
- **Authors**: Jia Luo, Liwei Mu, Yuanxi Huang +3
- **PDF**: https://ieeexplore.ieee.org/document/10718282
- **Abstract**: This letter proposed two novel error correction strategies that leverage the error correction and deletion correction capabilities of RRNS (redundant residue number system) codes: the RRNS+MSA (multiple sequence comparison) scheme and the RRNS+marker code scheme. These strategies aimed to address the issues of insertion, deletion and substitution in the DNA storage channel. In consideration of the specific characteristics of the DNA storage channel, the proposed study also incorporated the probabilities of deletion and insertion into the original DNA storage channel model. The simulation results demonstrated conclusively that the two error correction schemes proposed in this letter can ensure the reliability of DNA storage information. It is noteworthy that the RRNS+marker code scheme proposed in this letter demonstrated a superior balance between error correction performance and DNA reading cost.

## Unsourced Random Access via Random Scattering With Turbo Probabilistic Data Association Detector and Treating Collision as Interference

- **Status**: ❌
- **Reason**: URA 무선 다중접속 송수신기 설계; LDPC는 베이스라인 CC-LDPC로 부수 사용, 떼어낼 새 디코더/코드설계 기법 없음
- **ID**: ieee:10702503
- **Type**: journal
- **Published**: Dec. 2024
- **Authors**: Zhentian Zhang, Jian Dang, Zaichen Zhang +3
- **PDF**: https://ieeexplore.ieee.org/document/10702503
- **Abstract**: In this paper, a novel random scattering transceiver design for unsourced random access (URA) is investigated. Distinctive from the state-of-the-art such as coded compressed sensing (CCS) kind and interleaving division multiple access (IDMA) kind, the data is split into two portions and the back-and-forth interleaving/de-interleaving for soft information update is dismantled. A portion of the data is encoded by compressed sensing (CS) and the rest is encoded by convolutional code LDPC (CC-LDPC). Based on the principle of probabilistic data association (PDA), a receiver with a turbo PDA multi-user detector (MUD) is designed by the random scattering transmission. Meanwhile, the proposed turbo PDA detector can also cooperate with the CC-LDPC decoder. A sliding window decoding structure is embedded in the proposed receiver. Moreover, given that permeable collision in URA can undermine the system performance, this paper treats collision as interference and elaborates different slot-wise MUD signal models combining the feature of random scattering, based on which a collision resolution procedure is proposed. Empirically, the proposed scheme shows faster system performance convergence and more accurate MUD performance than the IDMA kind. Numerical results with fair comparisons validate the viability of the proposed scheme.

## A Secure Coded MIMO System Under Imperfect Channel Estimation

- **Status**: ❌
- **Reason**: 물리계층 보안(PLS)용 인터리빙/AFEC 기법, LDPC는 부수 언급 — 떼어낼 ECC 기법 없음
- **ID**: ieee:10620643
- **Type**: journal
- **Published**: Dec. 2024
- **Authors**: Thara Son, Hyein Lee, Sooyoung Kim
- **PDF**: https://ieeexplore.ieee.org/document/10620643
- **Abstract**: There have been many researches on physical layer security (PLS) schemes using dynamic channel information, but most of them assumed the perfect channel information, which is difficult to obtain in practical systems. This paper proposes an efficient PLS scheme for coded multi-input multi-output (MIMO) systems operating under imperfect channel estimation conditions. Since coded MIMO systems are typically equipped with an interleaver for bit-interleaved coded modulation (BICM), which is associated with soft iterative decoding, the scheme proposed herein adopts a random interleaving index, which is a function of the legitimate channel. This scheme also includes a novel strategy to prevent the performance degradation caused by channel estimation error through the combination of ancillary forward error correction (AFEC). This innovative concept can archive an advanced level of security protection without requiring any additional power. We also derive the secrecy rate of the proposed scheme. The simulation results presented in this paper demonstrate that the proposed scheme effectively protects the transmitted data without any information leakage to the eavesdropper.

## Constellations Cross Circular Auto-Correlation C4-Sequences

- **Status**: ❌
- **Reason**: C4-sequence(상관 시퀀스 설계)에 비이진 outer code 결합 — LDPC와 무관하고 떼어낼 ECC 기법 없음
- **ID**: ieee:10587014
- **Type**: journal
- **Published**: Dec. 2024
- **Authors**: Emmanuel Boutillon
- **PDF**: https://ieeexplore.ieee.org/document/10587014
- **Abstract**: This paper introduces a novel type of sequences called C4-sequences. C4-sequences share similar optimal autocorrelation properties with Zadoff-Chu sequences. However, C4-sequences offer the additional advantage of being also optimal (in the sense of minimal Euclidean distance between sequences) for four truncation lengths, providing flexibility in adapting to different channel conditions without compromising performance. Moreover, unlike Zadoff-Chu sequences, the points of a constellation associated with a C4-sequence are not limited to the unit circle. This opens up possibilities for achieving shaping gain, leading to enhanced spectral efficiency. By combining a truncated C4-sequence modulation as an inner code with a fixed-rate non-binary outer code, flexible and performant rate-adaptive communication systems can also be achieved. Finally, the notion of C4-sequences can be generalized.

## A Low-Complexity Soft-Output Massive MIMO Detector With Near-Optimum Performance

- **Status**: ❌
- **Reason**: massive MIMO 검출기(MMSE-LAS/OCD) 및 soft-output, LDPC는 코디드 시스템 베이스라인일 뿐 — LDPC 디코더/HW 기여 아님
- **ID**: ieee:10623240
- **Type**: journal
- **Published**: Dec. 2024
- **Authors**: Jinjie Hu, Suwen Song, Zhongfeng Wang
- **PDF**: https://ieeexplore.ieee.org/document/10623240
- **Abstract**: In massive multiple-input multiple-output (MIMO) detection, the likelihood ascent search (LAS) algorithm is well-known for its near-optimum performance and low complexity. It employs gradient descent to enhance the performance of suboptimal MIMO detectors, specifically the minimum mean-square error (MMSE) algorithm. In this paper, we introduce several techniques to improve the MMSE-based LAS (MMSE-LAS) algorithm in terms of both complexity and performance. To reduce complexity, the MMSE is first replaced with the low-complexity optimized coordinate descent (OCD) algorithm at the cost of negligible performance loss. Then, the conventional OCD and LAS algorithms are optimized for better computation reuse. Besides, we derive a new soft-output computation formula for LAS to improve the coded performance. The proposed modulation-based successive gradient descent (MB-SGD) detector outperforms MMSE-LAS and the latest work in terms of either complexity or performance for  $64\times 8$  and  $128\times 8$  LDPC-coded MIMO systems with multiple modulations from QPSK to 256-QAM. The corresponding architecture for a  $128\times 8$  coded MIMO system supporting multiple modulations is implemented on a Xilinx Virtex-7 FPGA and with TSMC 28-nm CMOS technology, exhibiting 74.5% lower latency and 0.24 dB gain compared to OCD on FPGA, and also achieving  $14.59\times $  energy efficiency and  $2.04\times $  area efficiency over the state-of-the-art implementation on ASIC.

## On The Minsum Decoding Algorithm For The 5G NR LDPC Codes

- **Status**: ❌
- **Reason**: 5G NR LDPC에 표준 min-sum을 적용/분석한 수준, 새 디코더 기여 없음 — 표준 기법 단순 재사용 제외
- **ID**: ieee:10934509
- **Type**: conference
- **Published**: 9-11 Dec. 
- **Authors**: Asma Alqudah
- **PDF**: https://ieeexplore.ieee.org/document/10934509
- **Abstract**: The paper presents a detailed analysis of the minsum decoding algorithm as applied to low-density parity-check (LDPC) codes used in 5G new radio (NR) systems. With the increasing demand for higher data rates and improved reliability in next-generation wireless communications, LDPC codes have emerged as a pivotal component in 5G NR's coding strategy. The minsum algorithm, known for its simplicity and efficiency in message passing, is evaluated in the context of its performance and practical implementation for these codes. Minsum decoding reduces complexity by approximating the soft-decision values using the minimum of the incoming messages, rather than applying the more computationally expensive operations such as hyperbolic tangent functions. In the context of 5G NR, this approximation makes minsum decoding particularly attractive for hardware implementation, providing a good trade-off between error-correction performance and computational efficiency. The algorithm iteratively updates messages passed along the edges of the Tanner graph, leveraging the sparsity of LDPC codes. This abstract reviews the relevance of minsum decoding to 5G NR LDPC codes, emphasizing its role in balancing performance with low computational requirements, critical in mobile and high-throughput applications.

## Restoring Unintended Model Learning by Error Correcting Code

- **Status**: ❌
- **Reason**: 모델 파라미터 복원에 ECC 적용, LDPC ECC 부호설계/디코더 기법 아님 — 채널코딩 ECC 아님
- **ID**: ieee:10917564
- **Type**: conference
- **Published**: 9-10 Dec. 
- **Authors**: Nami Ashizawa, Toshiki Shibahara, Naoto Kiribuchi +2
- **PDF**: https://ieeexplore.ieee.org/document/10917564
- **Abstract**: This paper proposes a method to restore model parameters after unintended training to those before such training by error correction. Restoring model parameters with error-correcting code helps the model avoid relearning from scratch and storing model parameters in the cloud. Error correction restores a message even with some errors through its transmission. Decoding the codeword generated by encoding a message corrects errors in the message. In this paper, we regard parameter changes caused by training as errors and restore the changed parameters to their prior by error correction. The proposed method can reduce the error-correcting costs while maintaining the accuracy of model inference by restoring only part of the more critical parameters. The metrics to select parameters for error correction are the influence of a parameter on training. We apply a technique of model pruning that observes the backpropagation process to define the influence. We experimentally evaluated the proposed error correction for model parameters under two scenarios: injecting incorrect data to mislead models and specializing the model, namely overfitting, by learning more epochs than necessary. We used Convolutional Neural Networks (CNNs) and vision transformer (ViT) trained to classify images in the experiment. The experimental results show that error correction restored inference outputs under the scenarios up to 60.75% of the inference outputs before learning the scenarios, even when it saved more than 33.97% of the computational costs and corrected errors of the 80% parameters.

## Rate-Compatible Root-Protograph-based LDPC Codes for IR-HARQ Systems

- **Status**: ❌
- **Reason**: IR-HARQ 블록페이딩용 root-protograph RC-LDPC 코드 설계 — full-diversity는 페이딩 채널 특이적, NAND(메모리)에 이식할 코드설계 기여 약함
- **ID**: ieee:11100470
- **Type**: conference
- **Published**: 8-12 Dec. 
- **Authors**: Zhaojie Yang, Xiaoxi Yu, Yi Fang +1
- **PDF**: https://ieeexplore.ieee.org/document/11100470
- **Abstract**: This paper studies a new type of root-protograph-based low-density parity-check (RP-LDPC) codes, called rate-compatible RP-LDPC (RC-RP-LDPC) codes, designed for the incremental-redundancy hybrid ARQ (IR-HARQ) system over block-fading (BF) channels. We begin the study with analyzing the limitations of traditional RP-LDPC codes in the IR-HARQ system over BF channels, revealing that they fail to achieve full diversity in this scenario. To address this issue, we propose a design methodology for RC-RP-LDPC codes, which can guarantee that the resultant codes not only have both full-diversity property and outage-limit-approaching performance, but also can realize rate compatibility. The outage-boundary analyses and word-error-rate (WER) simulations demonstrate that the proposed RC-RP-LDPC codes significantly outperform prior-art protograph LDPC and RP-LDPC codes in the IR-HARQ system over BF channels.

## Decoding Quantum LDPC Codes Using Graph Neural Networks

- **Status**: ❌
- **Reason**: QLDPC를 GNN으로 디코딩 — 양자 코드 대상이며 GNN 디코더가 양자 그래프 구조에 특화, 고전 바이너리 이식 명확치 않아 원칙 제외
- **ID**: ieee:10901425
- **Type**: conference
- **Published**: 8-12 Dec. 
- **Authors**: Vukan Ninkovic, Ognjen Kundacina, Dejan Vukobratovic +2
- **PDF**: https://ieeexplore.ieee.org/document/10901425
- **Abstract**: In this paper, we propose a novel decoding method for Quantum Low-Density Parity-Check (QLDPC) codes based on Graph Neural Networks (GNNs). Similar to the Belief Propagation (BP)-based QLDPC decoders, the proposed GNN-based QLDPC decoder exploits the sparse graph structure of QLDPC codes and can be implemented as a message-passing decoding algorithm. We compare the proposed GNN-based decoding algorithm against selected classes of both conventional and neural–enhanced QLDPC decoding algorithms across several QLDPC code designs. The simulation results demonstrate excellent performance of GNN-based decoders along with their low complexity compared to competing methods.

## Practical Decoding for Deep Polar Codes

- **Status**: ❌
- **Reason**: 폴라 코드 + SCL-BPC 디코더; LDPC가 아니며 이식 가능한 LDPC 기법 없음
- **ID**: ieee:11100905
- **Type**: conference
- **Published**: 8-12 Dec. 
- **Authors**: Donghwa Han, Min Jang, Donghun Lee +2
- **PDF**: https://ieeexplore.ieee.org/document/11100905
- **Abstract**: Pre-transformed polar codes constitute a broad class of codes constructed through the serial concatenation of outer codes and polar codes, enhancing the performance of standalone polar codes either by improving the weight distribution or by increasing the error-decay rate. Deep polar codes, a novel variant within this class, are constructed through a pre-transformation that involves a series of nested polar codes with increasing dimensions across layers. The proposed successive cancellation list with backpropagation parity check (SCL-BPC) decoder exploits the parity equations naturally arising from this nested encoding structure. In certain scenarios, deep polar codes with SCL-BPC decoding demonstrate superior performance compared to other pre-transformed polar codes. However, the SCL-BPC algorithm incurs additional decoding complexity and results in uneven decoding times. To address these issues, we investigate the matrix representation of the pre-transformation in deep polar codes and develop efficient implementation solutions for SCL-BPC decoding. Additionally, we introduce a low-complexity approach to SCL-BPC, which exhibits only a marginal reduction in performance.

## Single Sparse Graph Enhanced Expectation Propagation Design for Uplink MIMO-SCMA

- **Status**: ❌
- **Reason**: MIMO-SCMA 수신기(SSG-EPA), LDPC는 그래프 통합 베이스라인일 뿐 무선 응용 특이적, 떼어낼 ECC 기법 없음
- **ID**: ieee:10901680
- **Type**: conference
- **Published**: 8-12 Dec. 
- **Authors**: Qu Luo, Jing Zhu, Gaojie Chen +2
- **PDF**: https://ieeexplore.ieee.org/document/10901680
- **Abstract**: Sparse code multiple access (SCMA) and multiple input multiple output (MIMO) are considered as two efficient techniques to provide both massive connectivity and high spectrum efficiency for future machine-type wireless networks. This paper proposes a single sparse graph (SSG) enhanced expectation propagation algorithm (EPA) receiver, referred to as SSG-EPA, for uplink MIMO-SCMA systems. Firstly, we reformulate the sparse codebook mapping process using a linear encoding model, which transforms the variable nodes (VNs) of SCMA from symbol-level to bit-level VNs. Such transformation facilitates the integration of the VNs of SCMA and low-density parity-check (LDPC), thereby emerging the SCMA and LDPC graphs into a SSG. Subsequently, to further reduce the detection complexity, the message propagation between SCMA VNs and function nodes (FNs) are designed based on EPA principles. Different from the existing iterative detection and decoding (IDD) structure, the proposed EPA-SSG allows a simultaneously detection and decoding at each iteration, and eliminates the use of interleavers, de-interleavers, symbol-to-bit, and bit-to-symbol LLR transformations. Simulation results show that the proposed SSG-EPA achieves better error rate performance compared to the state-of-the-art schemes.

## A Simple PHY-Aware Outer Coding (SPOC) Scheme for Reliable, Low-Latency Communication

- **Status**: ❌
- **Reason**: MAC 계층 패킷 단위 outer coding(MDS 기반); LDPC는 코드블록 단위 언급뿐, 떼어낼 LDPC ECC 기법 없음
- **ID**: ieee:11101205
- **Type**: conference
- **Published**: 8-12 Dec. 
- **Authors**: Srivathsa Acharya, Shobhit Bhatnagar, Gayathri R +7
- **PDF**: https://ieeexplore.ieee.org/document/11101205
- **Abstract**: A simple, PHY-aware, packet-level outer coding scheme (SPOC) for beyond 5G is presented that permits reliable communication over just a single Transmission Time Interval (TTI), whenever there are two or more datalink paths between transmitter and receiver. The scheme has the following features: outer coding is positioned at the MAC layer, and each packet is made to correspond to a single LDPC code block, thereby enabling the scheme to take advantage of partially-decoded transport blocks; PHY layers at the receiver end are instructed to pass on to the MAC layer all correctly-decoded code blocks even if the entire transport block has not been correctly decoded. Simulation results are presented to show that the SPOC scheme outperforms the PDCP duplication feature present in the 5G standard, at no additional cost to spectral efficiency. Performance benefits are shown to increase with increased packet sizes, thus making the scheme attractive for high data rate applications that seek reliable communication with extremely low latency. Where latency constraints permit, the scheme can also take advantage of HARQ retransmissions to improve reliability. While the base scheme employs MDS codes, the scheme can be extended to incorporate binary codes as well.

## Finite Blocklength Analysis for Optical Fiber MIMO Channels

- **Status**: ❌
- **Reason**: 광섬유 MIMO 유한블록길이 이론 bound, LDPC는 비교 베이스라인 — 순수 이론 bound 제외
- **ID**: ieee:10901230
- **Type**: conference
- **Published**: 8-12 Dec. 
- **Authors**: Xin Zhang, Dongfang Xu, Xianghao Yu +2
- **PDF**: https://ieeexplore.ieee.org/document/10901230
- **Abstract**: The multiple-input and multiple-output (MIMO) technique is considered as a promising approach for improving the throughput and reliability of optical fiber communications. However, the finite blocklength (FBL) analysis of optical fiber MIMO systems is not available in the literature. Considering the Jacobi MIMO channel, which was proposed to model the nearly lossless propagation and the crosstalks in optical fiber channels, this paper studies the optimal average error probability (OAEP) of optical fiber multicore/multimode systems in the FBL regime. In particular, we consider the case where the coding rate is in the ${\mathcal{O}}\left({\frac{1}{{\sqrt {LM} }}}\right)$ proximity of the capacity, with M and L denoting the number of transmit channels and blocklength, respectively. To this end, a central limit theorem (CLT) for the information density is first established in the asymptotic regime where the blocklength and the number of transmit, receive, and available channels approach infinity with fixed ratios. With the aid of the CLT, the closed-form upper and lower bounds for the OAEP with the concerned rate are then derived. It is shown that the derived bounds could degenerate to those for Rayleigh MIMO channels if the number of available channels goes to infinity. Numerical simulations indicate that the derived bounds are closer to the performance of low-density parity check (LDPC) coding schemes than outage probability, thus providing a better characterization with the concerned the rate.

## Optimizing Real-Time Freshness: Deep Joint Source–Channel Coding Based AoI in Wireless Networks

- **Status**: ❌
- **Reason**: Deep JSCC 기반 AoI 최소화, LDPC 미등장·소스채널결합 — 떼어낼 ECC 기법 없음
- **ID**: ieee:10901175
- **Type**: conference
- **Published**: 8-12 Dec. 
- **Authors**: Chathuranga M. Wijerathna Basnayaka, Dushantha Nalin K. Jayakody, Marko Beko
- **PDF**: https://ieeexplore.ieee.org/document/10901175
- **Abstract**: This paper proposes a deep joint source-channel coding (DJSCC) to minimize the age of information (AoI) for image transmission. A new content-based AoI metric called age of misclassified information (AoMI) is introduced to estimate the freshness of the information in an image classification system. AoMI is a critical metric in timely information delivery, measuring the age of the most recently received and correctly classified image at the receiver. The proposed system leverages a deep neural network at the transmitter to map image pixels directly to channel input symbols, eliminating the need for separate source and channel coding. At the receiver, the channel output is processed to perform image classification. To analyze the AoMI performance of the system, a stochastic hybrid systems (SHS) approach is employed. Closed-form expressions for the average AoMI (AAoMI) are derived, providing insights into the impact of system parameters on the AoMI. Simulation results demonstrate the effectiveness of the proposed DJSCC-based system in achieving lower AoMI compared to traditional separate source and channel coding schemes. The findings highlight the potential of deep learning techniques to maintain the freshness of the information in wireless communication systems. This work paves the way for the design of wireless communication systems that prioritize the freshness of delivered information – this is crucial in applications such as real-time monitoring, surveillance, and control systems.

## Generative Semantic Communication for Text-to-Speech Synthesis

- **Status**: ❌
- **Reason**: 생성형 세만틱 통신 TTS; ECC 디코더/코드설계 기여 없음
- **ID**: ieee:11101684
- **Type**: conference
- **Published**: 8-12 Dec. 
- **Authors**: Jiahao Zheng, Jinke Ren, Peng Xu +5
- **PDF**: https://ieeexplore.ieee.org/document/11101684
- **Abstract**: Semantic communication is a promising technology to improve communication efficiency by transmitting only the semantic information of the source data. However, traditional semantic communication methods primarily focus on data reconstruction tasks, which may not be efficient for emerging generative tasks such as text-to-speech (TTS) synthesis. To address this limitation, this paper develops a novel generative semantic communication framework for TTS synthesis, leveraging generative artificial intelligence technologies. Firstly, we utilize a pre-trained large speech model called WavLM and the residual vector quantization method to construct two semantic knowledge bases (KBs) at the transmitter and receiver, respectively. The KB at the transmitter enables effective semantic extraction, while the KB at the receiver facilitates lifelike speech synthesis. Then, we employ a transformer encoder and a diffusion model to achieve efficient semantic coding without introducing significant communication overhead. Finally, numerical results demonstrate that our framework achieves much higher fidelity for the generated speech than four baselines, in both cases with additive white Gaussian noise channel and Rayleigh fading channel.

## AdaJSCC: Instance-Adaptive Joint Source-Channel Coding for Wireless Image Transmission

- **Status**: ❌
- **Reason**: DeepJSCC 무선 이미지 전송 — 소스-채널 결합부호로 LDPC ECC 기법 아님
- **ID**: ieee:11100771
- **Type**: conference
- **Published**: 8-12 Dec. 
- **Authors**: Tianjian Dang, Shengshi Yao, Siye Wang +3
- **PDF**: https://ieeexplore.ieee.org/document/11100771
- **Abstract**: Recent works in wireless image transmission based on deep joint source-channel coding (DeepJSCC) have exhibited superior performance against many traditional source and channel coding methods. While so far, research efforts mainly concentrate on architecture and model improvements toward a static target domain. In this work, we propose a novel lightweight instance-adaptive DeepJSCC approach to further improve the transmission performance for each image instance. We leverage the idea of a dynamic convolution kernel to build the DeepJSCC codec. In such way, apart from the general coded content stream, an additional model stream is extracted from each individual image instance and transmitted to the decoder side for generating the dynamic convolutional kernel parameters. The model stream enables the codec to update the off-the-shelf pretrained models after deployment in a lightweight online fashion. Experiments over various wireless channel models verify the effectiveness and robustness of our method.

## SC-CDM: Enhancing Quality of Image Semantic Communication with a Compact Diffusion Model

- **Status**: ❌
- **Reason**: 세만틱 통신 + diffusion 이미지 전송; ECC 디코더/코드설계 기여 없음
- **ID**: ieee:11100947
- **Type**: conference
- **Published**: 8-12 Dec. 
- **Authors**: Kexin Zhang, Lixin Li, Wensheng Lin +3
- **PDF**: https://ieeexplore.ieee.org/document/11100947
- **Abstract**: Semantic Communication (SC) is an emerging technology that has attracted much attention in the sixth-generation (6G) mobile communication systems. However, few literature has fully considered the perceptual quality of the reconstructed image. To solve this problem, we propose a generative SC for wireless image transmission (denoted as SC-CDM). This approach leverages compact diffusion models to improve the fidelity and semantic accuracy of the images reconstructed after transmission, ensuring that the essential content is preserved even in bandwidth-constrained environments. Specifically, we aim to redesign the swin Transformer as a new backbone for efficient semantic feature extraction and compression. Next, the receiver integrates the slim prior and image reconstruction networks. Compared to traditional Diffusion Models (DMs), it leverages DMs’ robust distribution mapping capability to generate a compact condition vector, guiding image recovery, thus enhancing the perceptual details of the reconstructed images. Finally, a series of evaluation and ablation studies are conducted to validate the effectiveness and robustness of the proposed algorithm and further increase the Peak Signal-to-Noise Ratio (PSNR) by over 17% on top of CNN-based DeepJSCC.

## From Biology to Communication: A Practice for the Non-uniform Constellations Design

- **Status**: ❌
- **Reason**: 비균일 성상도(NUC) 설계·복조 기법으로 LDPC ECC와 무관, 떼어낼 디코더/코드설계 기법 없음
- **ID**: ieee:10901255
- **Type**: conference
- **Published**: 8-12 Dec. 
- **Authors**: Dong Wang, Shiwen Ma, Xiangying Hu +3
- **PDF**: https://ieeexplore.ieee.org/document/10901255
- **Abstract**: Non-uniform constellations (NUCs) present a promising technique to improve the spectral efficiency whereas the existing NUCs do not fully exploit the degree of freedom for the constellation design. This paper performs an interesting practice of the biology-motivated communication design to geometrically arrange the constellations. Specifically, we reformulate the traditional constellation design problem as the seed arrangement problem within a circular region. The centroidal Voronoi tessellation is employed to model the seed growth for enlarging the Euclidean distances among the constellations. Besides, we propose a particle swarm optimization based constellation design to minimize the averaged bit error probability. Finally, a lightweight machine learning enhanced demodulation is developed to reduce the complexity introduced by the asymmetric feature of NUCs. Simulation results demonstrate that the proposed scheme outperforms quadrature amplitude modulation and gold angle modulation, highlighting the potential of biology-inspired design techniques for communication systems.

## Saturation Throughput Analysis of Hybrid Access MAC Protocol in IEEE 802.11ax WLANs

- **Status**: ❌
- **Reason**: WLAN MAC 프로토콜 처리량 분석, ECC/LDPC 무관
- **ID**: ieee:10901224
- **Type**: conference
- **Published**: 8-12 Dec. 
- **Authors**: S. Arthi, Neelesh B. Mehta
- **PDF**: https://ieeexplore.ieee.org/document/10901224
- **Abstract**: Current generation wireless local area networks (WLANs) based on the IEEE 802.11ax standard employ a novel hybrid medium access control (MAC) protocol, which combines contention-based random access (UORA) and contention-free scheduled access (SA) transmissions over orthogonal resource units (RUs). We present a novel fixed-point analysis of the saturation throughput of IEEE 802.11ax that accounts for hybrid access, discrete rate adaptation, and schedulers. Our analysis captures the dynamic flow of users between UORA and SA in hybrid access. The variability in the number of users, which depends on the number of RUs allocated to UORA and the MAC contention protocol, affects the performance of the scheduler. Our approach differs from the literature, which models either UORA or SA (but not both) or assumes a fixed number of SA users. Our results verify the accuracy of the analysis despite its simplicity and reveal that the conventional approaches can overestimate the UORA and SA throughputs.

## Scalable and Reliable Over-the-Air Federated Edge Learning

- **Status**: ❌
- **Reason**: AirComp 연합학습용 격자(lattice) 부호 구성으로 LDPC 무관, NAND 이식 기법 없음
- **ID**: ieee:10901264
- **Type**: conference
- **Published**: 8-12 Dec. 
- **Authors**: Maximilian Egger, Christoph Hofmeister, Cem Kaya +2
- **PDF**: https://ieeexplore.ieee.org/document/10901264
- **Abstract**: Federated edge learning (FEEL) has emerged as a core paradigm for large-scale optimization. However, FEEL still suffers from a communication bottleneck due to the transmission of high-dimensional model updates from the clients to the federator. Over-the-air computation (AirComp) leverages the additive property of multiple-access channels by aggregating the clients’ updates over the channel to save communication resources. While analog uncoded transmission can benefit from the increased signal-to-noise ratio (SNR) due to the simultaneous transmission of many clients, potential errors may severely harm the learning process for small SNRs. To alleviate this problem, channel coding approaches were recently proposed for AirComp in FEEL. However, their error-correction capability degrades with an increasing number of clients. We propose a digital lattice-based code construction with constant error-correction capabilities in the number of clients, and compare to nested-lattice codes, well-known for their optimal rate and power efficiency in the point-to-point AWGN channel.

## CRC-Aided Adaptive Successive Cancellation List Decoder for 5G NR Polar Codes Using RBIR

- **Status**: ❌
- **Reason**: Polar 코드 CA-SCL 디코더, LDPC 아님 — 대상 부호 불일치
- **ID**: ieee:10900996
- **Type**: conference
- **Published**: 8-12 Dec. 
- **Authors**: Anusha Gunturu, Ashok Kumar Reddy Chavva
- **PDF**: https://ieeexplore.ieee.org/document/10900996
- **Abstract**: Cyclic redundancy check (CRC)-aided successive cancellation list (SCL) decoder, also termed as CA-SCL decoder, is used for decoding the polar codes in practical 5G new radio (NR) systems. The list size used in CA-SCL decoder is directly proportional to the power consumption and the complexity of the decoding process. In practice, a fixed list size (L) is used for CA-SCL decoding. However, we have observed that the required list size varies with signal to noise ratio (SNR) for achieving a target block error rate (BLER) performance. In this paper, we propose an adaptive CA-SCL (CA-ASCL) decoding algorithm, that reduces the average list size and hence the complexity of the CA-SCL decoder by identifying the right list size to be used for each decoding process, using a link abstraction metric called received bit information rate (RBIR), that maps to received SNR. We show that for a target BLER of 10%, the proposed CA-ASCL decoder that chooses the list size adaptively among the set {2, 4, 8, 16, 32} has upto 61.51% reduction in list size compared to that of CA-SCL decoder with L = 32, without any loss in BLER performance, and upto 72.23% reduction with performance loss limited to 0.05 dB in SNR, respectively, for 3GPP defined 5G NR TDL-A channel model, with delay spread of 30 ns and maximum Doppler shift of 100 Hz.

## An Over-the-Air Multi-user Tailbiting Code for URLLC

- **Status**: ❌
- **Reason**: tail-biting 컨볼루션 코드(TBCC) + Viterbi; LDPC 무관
- **ID**: ieee:11101532
- **Type**: conference
- **Published**: 8-12 Dec. 
- **Authors**: Rafael Santos, Daniel Castanheira, Adão Silva +1
- **PDF**: https://ieeexplore.ieee.org/document/11101532
- **Abstract**: The strict latency and reliability requirements of URLLC are particularly difficult to comply with, due to the inherent trade-off between these two factors. Most applications falling under the URLLC umbrella rely on the exchange of small packets. Convolutional codes (CC) exhibit near-optimal performance when encoding small information blocks. In order to operate in packet based transmission, it is necessary to introduce some kind of termination to the CC. Tail-biting CCs (TBCC) avoid rate loss and maintains equal error protection for all information bits. However, its ML decoding algorithm requires a Viterbi algorithm (VA) execution for each possible initial trellis states, which rapidly becomes unpractical. This becomes increasingly problematic in a multi-user scenario, where several URLLC users need fast decoding at the same time. This work proposes a novel distributed multi-user TBCC (MU-TBCC) coding scheme, which completely eliminates the ZTCC rate-loss and reduces decoding complexity for any multi-user scenario. In fact, the decoding algorithm complexity converges to the one of the VA as the number of users increase. The results shows that, as the SNR increases, the error performance of the MU-TBCC approaches the one of orthogonal transmissions. This scheme can be also interpreted as non-orthogonal multiple access scheme, whose structure enables efficient joint detection and decoding.

## Nonlinear-Transform Source-Channel Coding for Cooperative Relay Networks

- **Status**: ❌
- **Reason**: 비선형 변환 소스-채널 결합부호(JSCC) — LDPC ECC 기법 아님, 제외 대상
- **ID**: ieee:10901839
- **Type**: conference
- **Published**: 8-12 Dec. 
- **Authors**: Tong Jiao, Yilun Zhang, Zhongwei Si
- **PDF**: https://ieeexplore.ieee.org/document/10901839
- **Abstract**: In this paper, we propose a novel nonlinear-transform source-channel encoding and decoding scheme for cooperative relay (NTSC-R) systems. This scheme initially maps the source image to a latent space using a learned nonlinear-analysis transform, generating a latent representation. This representation is then encoded into variable-length codewords, which are broadcast to both the relay and destination. At the relay, the messages are either amplified and forwarded (AF) or decoded and forwarded (DF) to the destination. The destination integrates these signals, taking into account their respective contributions to the outcome, to reconstruct a higher-quality image. Unlike existing deep joint source-channel coding (deep JSCC) methods, our approach incorporates an entropy model as a prior for the latent representation, which enables the encoder to adapt codeword lengths based on the significance of the information. At the destination, the receiver merges information considering the quality and confidence level of each received signal. The entire system is trained end-to-end to optimize rate-distortion performance under established metrics. The simulations demonstrate that the proposed NTSC-R outperforms traditional baselines using BPG compression and polar codes, as well as current deep JSCC methods in both AF and DF modes across various image resolutions.

## Wireless Video Transmission with Joint Semantic-Channel Coding

- **Status**: ❌
- **Reason**: 세만틱-채널 결합 코딩(JSCC); LDPC는 비교 베이스라인일 뿐, 떼어낼 ECC 기법 없음
- **ID**: ieee:11100878
- **Type**: conference
- **Published**: 8-12 Dec. 
- **Authors**: Yinhuan Huang, Zhijin Qin
- **PDF**: https://ieeexplore.ieee.org/document/11100878
- **Abstract**: With the advent of the 6G era, the efficient transmission of large-scale, high-resolution videos poses a significant challenge to existing communication systems. Compared to traditional video communication systems, which are becoming increasingly complex and difficult to optimize, semantic communication offers new possibilities and flexibility for optimization, effectively resisting noise interference with low-design-complexity joint coding. In this paper, we propose an efficient semantic-channel joint coding model for wireless video transmission, which adjusts the rate output based on the contextual information of video sequences and channel conditions, ensuring the reliability of video transmission even under different channel conditions. Across standard video test sequences under different scenarios, experiments show that under reliable channel state conditions, our scheme can save 22% to 56% of bandwidth compared to traditional video wireless transmission systems composed of H.265, 5G LDPC, and digital modulation, while also overcoming the cliff effect and achieving efficient video transmission under harsh channel conditions. Our scheme provides strong technical support for the practical application of semantic communication.

## Downlink and Uplink Performance of Polar Codes in 5G Standard

- **Status**: ❌
- **Reason**: 5G 폴라 코드 성능 평가, LDPC는 비교 베이스라인일 뿐 떼어낼 ECC 기법 없음
- **ID**: ieee:10899709
- **Type**: conference
- **Published**: 6-8 Dec. 2
- **Authors**: Amit Kumar Shrivastava, Tallam Sai Nithin, Rohit Bethala +3
- **PDF**: https://ieeexplore.ieee.org/document/10899709
- **Abstract**: Polar coding is primarily used as a channel coding scheme for downlink and uplink control information related to enhanced Mobile Broadband Communication service. Therefore, this work evaluates complexity and the Block Error Rate (BLER) performance of polar codes in 5G standard which use the concept of channel polarization. At first, message segmentation is performed that is followed by Cyclic Redundancy Check (CRC) encoding. Further, the input bits interleaving and sub channel al-location are carried out. Furthermore, polar code encoding, sub-block interleaving, and rate matching are performed. Moreover, decoding is performed using CRC-assisted successive cancellation list decoding. BLER for different list sizes and code rates are demonstrated at various Signal-to-Noise for both downlink and uplink. Low complexity encoding and better BLER performance than Low-Density Parity Check codes is also shown.

## Fault-Tolerant Polar Code Decoding Algorithm for Satellite Communication

- **Status**: ❌
- **Reason**: 폴라 코드 BP 디코더의 회로 결함 내성 기법, LDPC 부호 아님이며 NAND 이식 기법 없음
- **ID**: ieee:11117794
- **Type**: conference
- **Published**: 6-8 Dec. 2
- **Authors**: Yuanhao Yang
- **PDF**: https://ieeexplore.ieee.org/document/11117794
- **Abstract**: As the key underlying technology of communication system, channel coding determines the reliability of information transmission of satellite communication. As a control channel coding scheme in the 5G standard, polar code can realize efficient encoding and decoding of control and instruction information in satellite communications. Therefore, polar code has good performance and potential for development and improvement in satellite communication. As one of the decoding algorithms of polar codes, Belief Propagation (BP) decoding has received a lot of attention due to its high degree of parallelism. Because the high radiation environment in satellite communication may cause the circuit failure and generate errors. In this paper, an accumulating polar code decoding algorithm with hardware fault tolerance is designed based on the traditional BP decoding algorithm. The algorithm realizes the algorithm fault tolerance by accumulating the iterative information of the decoder, and does not need to change the original decoding structure. The simulation results show that under a reliable circuit, the cumulative BP decoding algorithm will not cause performance impacts compared to traditional BP decoding. In the case of transient errors in the circuit, it can improve the fault tolerance of the decoder from 10e−6 to 10e−2.

## Algebraic Construction of Non-Primitive BCH Codes on GF(2m) with Minimum Distance Checking for Degrees up to 10

- **Status**: ❌
- **Reason**: 비원시 BCH 부호 대수적 구성 — LDPC 구성에 활용 가능성 언급뿐, 제시된 새 기여는 BCH 부호 자체로 이식할 LDPC 기법 없음
- **ID**: ieee:10793348
- **Type**: conference
- **Published**: 4-6 Dec. 2
- **Authors**: Mustapha Hilia, Bouchaib Aylaj, Fouad Ayoub +3
- **PDF**: https://ieeexplore.ieee.org/document/10793348
- **Abstract**: In coding theory, Bose-Chaudhuri-Hocquenghem (BCH) codes possess an excellent error correction capability, which allows them to become crucial for use in communication and storage systems. However, non-primitive BCH codes that hide interesting properties have received less attention than their primitive counterpart. In this work, we present an algebraic method to construct non-primitive BCH codes of length and dimension fixed, with a varying minimum distance, on a Galois finite field $G F\left(2^{m}\right)$ for extensions of degree m between 4 and 10. In this method, we will describe the construction of generating polynomials using non-primitive algebraic roots and verify the parameters of the codes obtained with an Algebraic Calculator. The resultant list of these non-primitive BCH codes give optimal properties in terms of coding rate and minimum distance, providing valuable flexibility for the construction of Low-density parity check (LDPC) codes.

## Analyzing the Impact of Thresholds in Bit-Flipping Decoding for QC-MDPC based McEliece cryptosystems

- **Status**: ❌
- **Reason**: QC-MDPC McEliece 암호용 bit-flipping threshold 분석 — 코드기반 암호/보안 도메인이고 MDPC bit-flipping은 NAND 고전 LDPC ECC로 이식할 새 기법 아님
- **ID**: ieee:10793358
- **Type**: conference
- **Published**: 4-6 Dec. 2
- **Authors**: Abdellatif Kichna, Abderrazak Farchane, Said Hakimi
- **PDF**: https://ieeexplore.ieee.org/document/10793358
- **Abstract**: This paper investigates the effect of various threshold configurations in the bit-flipping decoding algorithm for quasi-cyclic moderate density parity-check (QC-MDPC) codes within the McEliece cryptosystem. The choice of threshold plays a crucial role in determining the efficiency and accuracy of error correction in these code-based cryptographic schemes. We propose and evaluate several threshold formulas, comparing their performance across different error weights and security levels. Our results highlight the impact of threshold adjustments on the average number of decoding iterations, decoding failure rates (DFR), and syndrome weight behavior over multiple iterations. Through extensive simulations, we demonstrate how optimal threshold selection can significantly enhance the decoding process, providing insights for improving the robustness of postquantum secure McEliece cryptosystems.

## On Using BERT Embeddings for Text Semantic Communication

- **Status**: ❌
- **Reason**: BERT 임베딩 기반 텍스트 시맨틱 통신; LDPC ECC 무관, 떼어낼 채널코딩 기법 없음
- **ID**: ieee:10822884
- **Type**: conference
- **Published**: 3-5 Dec. 2
- **Authors**: Asma Mahgoub, Elias Yaacoub
- **PDF**: https://ieeexplore.ieee.org/document/10822884
- **Abstract**: The current technological advancements carry stringent communication requirements. These requirements cannot be achieved by current networks. Therefore, a new paradigm called semantic communication is proposed. Semantic communication is the transmission of the meaning of data. Different semantic communication algorithms were proposed in literature, but they are complex and non-universal. In this work, a text semantic communication algorithm will be modified to be simple and universal. The modified algorithm uses a transformer network with 1 encoder layer and 3 decoder layers. The embedding layer uses pretrained embeddings from a Bidirectional Encoder Representations from Transformers (BERT) model. The algorithm is trained to optimize both the cross-entropy loss and the mutual information. Training and testing are done using the European parliament proceedings dataset. The performance of the modified algorithm is comparable to the original algorithm although it uses 50% of the layers. This work indicates the potential of using pretrained embeddings to simplify and enhance universality of existing semantic communication algorithms.

## Analysis of JPEXIT Decoding Thresholds for DP-LDPC Based on Global and Separating Strategies

- **Status**: ❌
- **Reason**: JSCC용 DP-LDPC의 JPEXIT 임계값 분석으로 소스-채널 결합 + 순수 이론, 떼어낼 ECC 기법 없음
- **ID**: ieee:10929121
- **Type**: conference
- **Published**: 27-29 Dec.
- **Authors**: Shiyao Li, Lin Zhou, Sanya Liu +2
- **PDF**: https://ieeexplore.ieee.org/document/10929121
- **Abstract**: Double Photograph LDPC Codes (DP-LDPC) demonstrate superior Bit Error Rate (BER) performance in Joint Source-Channel Coding (JSCC) systems compared to Source-Channel Separation Coding systems. To analyze the theoretical performance of DP-LDPC codes, this paper employs Joint Photograph Extrinsic Information Transfer (JPEXIT) chats as a tool for performance assessment. We design both global strategy and separating strategy JPEXIT for decoding threshold analysis. The results indicate that the decoding thresholds of the global strategy and separating strategy JPEXIT are nearly equal under the same joint base matrix. Additionally, the time complexity of both strategies is the same. However, from the perspectives of code implementation complexity and program execution time, the global strategy JPEXIT is more advantageous.

## Integration and Configuration of LDPC IP Cores in FPGAs

- **Status**: ❌
- **Reason**: 5G 무선용 LDPC IP 코어 FPGA 통합으로 표준 LDPC 적용 수준, 새 디코더/HW 아키텍처 기여 없음
- **ID**: ieee:10929261
- **Type**: conference
- **Published**: 27-29 Dec.
- **Authors**: Zhaochuan Wei, Qingfeng Guo, Jingyue Huang +1
- **PDF**: https://ieeexplore.ieee.org/document/10929261
- **Abstract**: Low-density parity check (LDPC) coding is an efficient error-correction coding technique that is widely used in modern wireless communication systems, especially excelling in high signal-to-noise ratio environments. With the increased demand for high-speed data transmission and low latency in wireless communications, LDPC coding has become a key technique to improve the performance of communication systems. In this paper, we discuss the integration and configuration of LDPC IP cores in FPGAs, focus on the integration strategy to implement the LDPC encoding and decoding process on FPGA platforms, propose an optimized integration scheme, and validate its effectiveness in 5G applications through tests. The study aims to provide theoretical basis and practical guidance for the application of LDPC coding in future FPGA designs, and to promote the wide application of this technology in the field of wireless communications.

## Performance and Optimization of Coding Techniques for Deep Space Communication Channels

- **Status**: ❌
- **Reason**: deep-space용 Hamming/convolutional/turbo 코딩 성능 연구 — LDPC 아님, 이식 기법 없음
- **ID**: ieee:10869659
- **Type**: conference
- **Published**: 27-29 Dec.
- **Authors**: Wenqi Guan
- **PDF**: https://ieeexplore.ieee.org/document/10869659
- **Abstract**: In today's world, space exploration and communication advancements are critical to ensuring effective connections for scientific missions, planetary exploration, and future interstellar travel. Deep space communication plays a pivotal role in supporting these endeavors, as it enables the transmission of vital data across vast distances and harsh environments. This paper presents a comprehensive study on the performance and optimization of coding techniques for deep-space communication channels. Based on the characteristics of the deep-space environment, the channels are modeled into three stages: near-Earth link, interstellar link, and near-planet link. The modeling for each channel type is summarized, and simulation results are provided. To evaluate coding techniques, M2M4, MMSE, and DNN are employed to approximate the signal-to-noise ratio (SNR), which serves as a critical parameter in assessing various encoding schemes. Three coding techniques-Hamming, convolutional, and turbo codes-are tested in the context of these models, with a particular focus on the turbo coding method. Detailed exploration is carried out on the SOVA and Log-MAP algorithms, as well as the impact of transmission parameters such as code rate. Overall, the results aim to provide a foundation for reliable signal transmission and error correction in deep-space, addressing challenges inherent to the unique environment of deep-space communication.

## What the Cluster: An Unsupervised Framework to Segment Automotive Doppler Radar Pointclouds

- **Status**: ❌
- **Reason**: 약어 LDPC가 Layered Doppler-Position Clustering(레이더 포인트클라우드 군집화)을 지칭, LDPC 부호와 무관
- **ID**: ieee:10928021
- **Type**: conference
- **Published**: 17-19 Dec.
- **Authors**: Tim Dieter Eberhardt, Tim Brühl, Robin Schwager +2
- **PDF**: https://ieeexplore.ieee.org/document/10928021
- **Abstract**: The accurate identification of clusters from a radar point cloud is crucial for the safe operation of current Advanced Driver Assistance Systems (ADAS). Robust clustering of point clouds enables the correct identification and localization of other safety-critical traffic participants. Particularly, the case of undetected traffic participants presents an unsafe and dangerous situation. This paper introduces the Layered Doppler-Position Clustering (LDPC) framework for this task. In the first layer, static and dynamic detections are separated considering the translational and rotational movement of the vehicle. In the second layer, pre-clusters are developed based on one-dimensional hierarchical clustering using the Doppler velocity. In the final layer, each pre-cluster undergoes further clustering using DBSCAN and the position data. By separating the process into layers, LDPC effectively combines Doppler velocity and position data for clustering. Combining both variables with different units, such as meters and meters per second, in a distance function, violates the semantic integrity of the data. Furthermore, the experimental results shown in this paper prove the applicability of the proposed LDPC framework. In various driving situations, the accuracy of the clustering results can be improved compared to existing methods. Additionally, we consider the safety-critical limits concerning specific radar sensor errors. Across all validation data, we achieved higher accuracy compared to existing systems in our experimental results.

## Decoders for FEC Codes - A Review

- **Status**: ❌
- **Reason**: FEC 디코더 개괄 리뷰 — 새 기여 없는 일반 리뷰
- **ID**: ieee:10859677
- **Type**: conference
- **Published**: 16-18 Dec.
- **Authors**: Selciya Selvan, M. Bharathi, M.P. Sasirekha +3
- **PDF**: https://ieeexplore.ieee.org/document/10859677
- **Abstract**: FEC codes are a specialized type of code designed to detect and correct errors that occur during data transmission, ensuring data integrity. By intentionally introducing redundancy during encoding, FEC ensures that decoders can reliably extract original messages from received data, even if corrupted by transmission errors. This paper offers an overview of diverse decoding methods developed by various researchers.

## Data Management and Data Products of a Daily Optical Communications Ground Station for Laser Communications Relay Demonstration

- **Status**: ❌
- **Reason**: 광통신 지상국 데이터 관리 — LDPC/ECC 기법 전무
- **ID**: ieee:10850263
- **Type**: conference
- **Published**: 16-18 Dec.
- **Authors**: Christine P. Chen, Sabino Piazzolla, Tom Roberts +8
- **PDF**: https://ieeexplore.ieee.org/document/10850263
- **Abstract**: The Laser Communications Relay Demonstration (LCRD) mission is the first NASA end-to-end optical relay, operating since the Space Test Program Satellite-6 (STPSat-6) spacecraft launched in December, 2021. The feasibility of optical communications as a high-bandwidth service provider for NASA from geosynchronous orbit to ground is demonstrated through a long-term study of performance over time and varying channel conditions. Optical Ground Station 1 (OGS-1), located at Table Mountain Facility near Wrightwood, CA, has supported first-light and commissioning, and the current experiment phase, covering the recent three-year period on a largely daily operational cadence. Configured links include relays with Optical Ground Station 2 (OGS-2) in Haleakalā, Hawaii and ground-to-satellite loopbacks. This paper discusses the considerations behind OGS-1 data management and its development over the course of operations. An experimental scenario is described wherein this embedded system is demonstrated.

## A Low Complexity Segmented Parity SC Flip Decoding Algorithm for Polar Codes

- **Status**: ❌
- **Reason**: Polar 코드 SC-Flip 디코더 — LDPC 아님, NAND LDPC 이식 기법 없음
- **ID**: ieee:10898410
- **Type**: conference
- **Published**: 15-18 Dec.
- **Authors**: Dwaipayan Ghosh, Shriya Das, Leuna Das +2
- **PDF**: https://ieeexplore.ieee.org/document/10898410
- **Abstract**: The Successive Cancellation decoder cannot provide satisfactory error correcting performance for finite length polar codes. The error performance can be improved by using Successive Cancellation Flip decoders at the expense of higher complexity. In line with this, a novel decoding approach has been developed in this paper, where distributed parity bits are used to divide the codeword into multiple segments having equal probability of error occurrence, allowing early termination. The proposed Segmented Parity Successive Cancellation Flip (SP-SC Flip) Decoder achieves lower normalized complexity and average decoding latency compared to some related existing decoders, without degrading the error correcting performance. Further improvement in decoder performance is observed when code words are divided into a greater number of segments.

## FPGA Realization of a Security System for Internet of Multimedia Things

- **Status**: ❌
- **Reason**: 하이퍼카오스 기반 멀티미디어 이미지 암호화 FPGA — LDPC/ECC와 무관, 보안 도메인
- **ID**: ieee:10815713
- **Type**: conference
- **Published**: 14-17 Dec.
- **Authors**: Remas Osama, Eyad Mamdouh, Wassim Alexan +1
- **PDF**: https://ieeexplore.ieee.org/document/10815713
- **Abstract**: Multimedia encryption is essential for securing sensitive data during transmission and storage. This research work introduces a new visual data encryption technique using three hyperchaotic systems: a memristor system, a hyperchaotic 7D system, and an Erbium-doped fiber laser system and its hardware implementation. The algorithm leverages the complex dynamics and random-like behavior of these systems to achieve robust encryption across three layers. Each layer uses a pseudorandom number generator to create an S-box and an encryption key, which are then applied to the image content. Experiments demonstrate the scheme's effectiveness in terms of encryption quality, resistance to common attacks, and computational efficiency. This technique is promising for applications requiring secure image transmission and storage, such as military communications, medical imaging, and confidential document sharing. The hardware design of the proposed algorithm is implemented on Nexys 4 DDR FPGA board. For a 256 x 256 image, the hardware achieves an encryption rate of 0.49 Gbps.

## R10-Based NAVDAT: An Efficient and Reliable Maritime Broadcast System

- **Status**: ❌
- **Reason**: R10(Raptor/fountain) 코드 기반 해상 방송 시스템, 중복도 최적화 — fountain/erasure 응용, LDPC ECC 기법 없음
- **ID**: ieee:10893802
- **Type**: conference
- **Published**: 14-16 Dec.
- **Authors**: Xingguang Shen, Feng Yang
- **PDF**: https://ieeexplore.ieee.org/document/10893802
- **Abstract**: In this paper, we address the challenges faced by the NAVDAT maritime broadcasting system, such as the inability to retransmit and severe channel fluctuations, by innovatively introducing the R10 code and proposing the R10-based NAV-DAT system. To optimize redundancy settings for the R10-based NAVDAT system under different environmental conditions, we develop a mathematical model for the transmitter-receiver system. This model defines an objective function with redundancy as the decision variable, and the global optimal redundancy is determined using the Exponential Decay Inertia Weight Particle Swarm Optimization (EDIW-PSO) algorithm. Finally, extensive simulations are conducted under various scenarios for both the proposed R10-based NAVDAT system and the mathematical model. These simulations thoroughly validate the superior performance of the R10-based NAVDAT system over the original NAVDAT system, as well as the accuracy of the mathematical model.

## Blind Classification of Linear Block Codes Based on Multi-Dimensional Features

- **Status**: ❌
- **Reason**: 선형 블록 부호 블라인드 분류(코드 식별), 디코딩/구성 아님 — 이식할 ECC 기법 없음
- **ID**: ieee:10941892
- **Type**: conference
- **Published**: 13-16 Dec.
- **Authors**: Yuanqing Wang, Pengjiang Hu, Junan Yang +1
- **PDF**: https://ieeexplore.ieee.org/document/10941892
- **Abstract**: Linear Block Codes (LBCs) classification is a critical component of non-cooperative communication. Existing researches mainly rely on semi-blind classification techniques based on predefined candidate sets, while few research directed towards blind classification of new scheme LBCs widely used in modern communication systems. Therefore, this paper concentrates on classifying new scheme LBCs, including Polar code, Low Density Parity Check (LDPC) code, Bose-Chaudhuri-Hocquenghem (BCH) code, and Reed-Solomon (RS) code. Addressing the existing issues, this paper proposes an innovative method to classify key LBCs types based on multi-dimensional codeword features. To achieve better classification of new scheme LBCs types in error scenarios, a classification method based on multi-dimensional codeword features is proposed. This method utilizes four key features, including code length, frozen bits feature of Polar code, sparse parity check matrix feature of LDPC, and Galois Field Fourier Transform (GFFT) spectrum of RS and BCH codes. And the proposed method is not limited to the specific candidate sets. The experimental results have verified the effectiveness and practicality of the proposed method.

## Soft-Aided Error-and-Erasure Decoding of BCH-SPC Product Codes with Bit Marking

- **Status**: ❌
- **Reason**: BCH-SPC 곱 부호 소프트 error-and-erasure 디코딩 — LDPC 아닌 BCH/SPC 곱부호 디코더, NAND LDPC 이식성 낮음
- **ID**: ieee:10942076
- **Type**: conference
- **Published**: 13-16 Dec.
- **Authors**: Yangming Li, Ming Jiang, Qiang Wang
- **PDF**: https://ieeexplore.ieee.org/document/10942076
- **Abstract**: In this paper, we propose a novel soft-aided error-and-erasure decoding method for product codes with Bose-Chaudhuri-Hocquenghem (BCH) and single parity check (SPC) component codes based on bit marking. We mark all the reliable bits in the decoding of BCH component codes according to scaled reliability to reduce miscorrection, and we only flip the unreliable bits in the decoding of SPC component codes. A backtrack scheme is introduced to further improve the performance. The complexity of our proposed decoder is much lower than those of conventional soft-aided iterative decoders as the reliability of each bit remains unchanged when decoding, and only ternary message is exchanged between the component decoders. Simulations show that the proposed decoding method outperforms previous decoder by 0.1 dB, and the computational complexity is reduced by about 60% compared with 5G-LDPC codes at the cost of about 0.5dB performance loss.

## Understanding and Optimizing Nonlinear Chirp Spread Spectrum Modulation in LoRa Networks

- **Status**: ❌
- **Reason**: LoRa 비선형 chirp CSS 변조 분석·간단 오류정정 — LDPC 무관, 떼어낼 디코더/코드 기법 없음
- **ID**: ieee:11083128
- **Type**: conference
- **Published**: 13-15 Dec.
- **Authors**: Haoran Shi, Yichuan Yang, Xiuzhen Guo +3
- **PDF**: https://ieeexplore.ieee.org/document/11083128
- **Abstract**: LoRa has emerged as a crucial technology that provides ubiquitous connectivity for geographically distributed Internet of Things devices. LoRa employs linear Chirp Spread Spectrum (CSS) modulation in its physical layer to enable long-range communication. Recently, nonlinear chirp has been proposed to replace linear chirp in CSS, to enhance the capacity and scalability of LoRa technology. However, the characteristics and advantages of nonlinear chirps are not yet fully understood. To unleash the potential of nonlinear CSS modulation, this paper presents a comprehensive theoretical and experimental analysis of the nonlinear chirp, focusing on key aspects such as noise resilience, error correction, and bandwidth expansion. Our findings reveal that nonlinear chirps are intrinsically more resilient to noise than linear chirps. Moreover, nonlinear chirps typically exhibit a single-place demodulation error under strong noise conditions, which has informed our development of a simple yet effective error correction design. Additionally, users should carefully manage signal power compensation to avoid distortion while benefiting from the bandwidth expansion offered by nonlinear chirps. Building on these insights, we further refine nonlinear CSS modulation and implement our optimized design on USRPs. Field experiments demonstrate that our design achieves significant performance improvements, marking a step forward in the practical application of nonlinear CSS modulation in LoRa networks.

## A comparison of binary and non-binary codes approaches on the reliability and security performance of full-duplex transmission

- **Status**: ❌
- **Reason**: 풀듀플렉스 보안 통신에서 바이너리/비이진 LDPC 비교, 새 디코더·구성 없고 비이진 포함
- **ID**: ieee:10916019
- **Type**: conference
- **Published**: 11-13 Dec.
- **Authors**: Bao Quoc Vuong
- **PDF**: https://ieeexplore.ieee.org/document/10916019
- **Abstract**: This paper presents a comparative analysis of binary and non-binary coding approaches on the security performance of Full-Duplex transmission systems. In the context of modern communication networks, where data integrity and confidentiality are paramount, the study evaluates the effectiveness of Low-Density Parity-Check (LDPC) codes in both binary and non-binary formats. By employing security gap and Bit Error Rate (BER) as key performance indicators, we explore how each coding scheme impacts the resilience of Full-Duplex transmissions against potential eavesdropping and self-interference. Our findings indicate that while binary LDPC codes exhibit certain advantages in terms of lower complexity and implementation ease, non-binary LDPC codes demonstrate superior performance in mitigating bit errors and enhancing security under adverse conditions especially in high order of modulation. This comparative study aims to provide a comprehensive understanding of the trade-offs involved in selecting binary versus non-binary LDPC codes for secure and efficient Full-Duplex communication systems and offers insights into optimizing data communication protocols for improved reliability and security performance.

## Simulating a Finite-State Markov Chain for Rayleigh Block-Fading Channel based on its Mathematical Model, and Practical Representation

- **Status**: ❌
- **Reason**: Rayleigh block-fading 채널의 FSMC 모델링·시뮬레이션, 떼어낼 디코더/HW/코드설계 기법 없음
- **ID**: ieee:10877166
- **Type**: conference
- **Published**: 10-12 Dec.
- **Authors**: Hani Attar, Jafar Ababneh, Mohammad Al-Hihi +2
- **PDF**: https://ieeexplore.ieee.org/document/10877166
- **Abstract**: In the proposed paper, simulating the Finite State Markov Chain (FSMC) to be implemented as Rayleigh Block-fading channel. Indeed, FSMC is regarded as a practical fading channel because of its random choice for future transmission probability. Accordingly, this paper introduces the FSMC technology with the theoretical limits and equations; moreover, the uplink and downlink Rayleigh Block-fading channel scenarios are also investigated and supported by the simulation set-up. The results for the Rayleigh fading channel for the Long-Term Evaluation-Advanced network were obtained as an example of the channel's attitude. The findings demonstrate that FSMC provides such reliable results and is suitable for use as a practical fading channel, particularly in terms of burst error behavior.

## Quantum Key Distribution Optimization: Reducing Communication Overhead in Post-Processing Steps

- **Status**: ❌
- **Reason**: QKD 후처리 오버헤드 감소(PRNG·해시), 양자 보안 영역으로 원칙 제외, LDPC 디코더 기여 없음
- **ID**: ieee:10903120
- **Type**: conference
- **Published**: 1-4 Dec. 2
- **Authors**: Ashutosh Bhatia, Sainath Bitragunta, Kamlesh Tiwari
- **PDF**: https://ieeexplore.ieee.org/document/10903120
- **Abstract**: Quantum Key Distribution (QKD) is a ground-breaking method in modern cryptography that uses quantum mechanics to establish secure communication channels. Unlike classical cryptographic techniques, QKD provides unconditional security based on quantum principles, such as the no-cloning theorem and the uncertainty principle. However, existing QKD systems often suffer from high overhead in key post-processing, affecting efficiency and scalability, especially in resource-constrained environments such as IoT. This paper addresses these challenges by introducing two key optimizations to enhance the efficiency and security of QKD systems. First, we propose a method using Pseudorandom Number Generators (PRNGs) to determine key bit positions for verification by Alice and Bob, significantly reducing communication over-head. Second, we employ hash-based subsequence comparison to minimize data exchange and leverage the cryptographic strength of hash functions. Results demonstrate that these strategies effectively reduce key post-processing overhead and improve the efficiency of QKD systems in real-world conditions making QKD more practical and scalable for diverse application contexts.
