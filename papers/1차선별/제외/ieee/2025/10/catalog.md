# IEEE Xplore — 2025-10


## An Information Theory of Compute-Optimal Size Scaling, Emergence, and Plateaus in Language Models

- **Status**: ❌
- **Reason**: LLM 스케일링 법칙을 LDPC 유한크기 스케일링 분석으로 비유한 순수 이론 논문으로, LDPC는 수학적 도구로만 사용되며 떼어낼 디코더/HW/코드설계 기법 없음
- **ID**: ieee:11223775
- **Type**: journal
- **Published**: Oct. 2025
- **Authors**: Anuj K. Nayak, Lav R. Varshney
- **PDF**: https://ieeexplore.ieee.org/document/11223775
- **Abstract**: Recent empirical studies show three phenomena with increasing size of language models: compute-optimal size scaling, emergent capabilities, and performance plateauing. We present a simple unified mathematical framework to explain all of these language model scaling phenomena, building on recent skill-text bipartite graph frameworks for semantic learning. Modeling the learning of concepts from texts as an iterative process yields an analogy to iterative decoding of low-density parity check (LDPC) codes in information theory. Thence, drawing on finite-size scaling characterizations of LDPC decoding, we derive the compute-optimal size scaling (Chinchilla rule) for language models. Further, using tools from random network theory, we provide a simple explanation for both emergence of complex skills and plateauing of performance as the size of language models scale. We see multiple plateaus.

## Error Floor of ML-Decoded Spinal Codes in the Finite Blocklength Regime

- **Status**: ❌
- **Reason**: 스파인 코드 에러 플로어 분석 — LDPC 무관 rateless 코드, 이식 가능 LDPC 기법 없음
- **ID**: ieee:11005679
- **Type**: journal
- **Published**: Oct. 2025
- **Authors**: Aimin Li, Shaohua Wu, Xiaomeng Chen +1
- **PDF**: https://ieeexplore.ieee.org/document/11005679
- **Abstract**: Spinal codes are a new family of capacity-achieving rateless codes that have been shown to achieve better rate performance compared to Raptor codes, Strider codes, and rateless Low-Density Parity-Check (LDPC) codes. This correspondence addresses the performance limitations of Spinal codes in the finite blocklength regime, uncovering an error floor phenomenon at high Signal-to-Noise Ratios (SNRs) under Maximum Likelihood (ML) Decoding. We develop an analytical expression to approximate the error floor and devise SNR thresholds at which the error floor initiates. Numerical results across Additive White Gaussian Noise (AWGN), Rayleigh, and Nakagami-m fading channels verify the accuracy of our analysis. The analysis and numerical results also show that transmitting more passes of symbols can lower the error floor but do not affect the SNR threshold, providing insights into the performance target, the operating SNR region, and the code design.

## Free Space Optical Semantic Communication for Satellite Remote Sensing Image Transmission

- **Status**: ❌
- **Reason**: FSO 위성 시맨틱 통신 — JSCC/시맨틱 통신 제외 카테고리, LDPC 내용 없음
- **ID**: ieee:10969992
- **Type**: journal
- **Published**: Oct. 2025
- **Authors**: Wenbin Chen, Cheng Ju, Tianxing Yuan +3
- **PDF**: https://ieeexplore.ieee.org/document/10969992
- **Abstract**: To further improve the transmission efficiency and link stability for free space optical (FSO)-based satellite communication (SatCom) systems when transmitting large-scale remote sensing images, a scheme based on the integration of FSO and semantic communication (FSO-SC) is proposed, which employs a vector quantized variational autoencoder with spatial normalization to extract essential semantic features of images while preserving intricate details. Additionally, the Málaga distribution model is utilized to simulate FSO channels with diverse turbulence conditions. Moreover, a comparative evaluation between the FSO-SC and traditional systems is conducted through 28 GBaud satellite-ground simulation with three modulation formats considering various effects. Compared to the traditional systems, without incurring additional bits for error corrections, the FSO-SC system achieves a power gain of over 3 dB while enabling transmission at zenith angles over 60°. Moreover, it achieves performance on par with state-of-the-art 4-receiver spatial diversity technology, while offering superior hardware and transmission efficiency. Furthermore, we conduct 10 Gbps real-time satellite-ground equivalent experiments to validate the practicality of the FSO-SC, where it achieves a 60% reduction in communication overhead compared to existing solutions while maintaining comparable received image quality and can reach a minimum receiver sensitivity gain of 4 dB. Simulation and experimental results demonstrate that the proposed FSO-SC scheme achieves high system efficiency and stability, holding promise as a viable solution for future SatCom.

## Block Circulant Codes With Application to Decentralized Systems

- **Status**: ❌
- **Reason**: 블록체인 데이터 가용성용 블록 순환 코드(RS 기반) — LDPC 무관, 이식 가능 기법 없음
- **ID**: ieee:10980112
- **Type**: journal
- **Published**: Oct. 2025
- **Authors**: Birenjith Sasidharan, Emanuele Viterbo, Son Hoang Dau
- **PDF**: https://ieeexplore.ieee.org/document/10980112
- **Abstract**: In this paper, we design a family of  $[n,k,d]$  block circulant codes that consist of many  $[n_{0} \ll n,k_{0} \ll k,d_{0} \lt d]$  local codes and that satisfy two properties: 1) code supports distributed decoding of up to  $(d-1)$  erasures relying only on local codes without a central coordinator, and 2) it is amenable to low complexity verification of code symbols using a cryptographic commitment scheme. These properties make the code ideal for use in protocols that address the data availability problem in blockchain networks. Moreover, the code outperforms the currently used 2D Reed-Solomon (RS) code with a larger relative minimum distance  $(d/n)$ , as desired in the protocol, for a given rate  $(k/n)$  in the high-rate regime. The code is designed in two steps. First, we develop the topology, i.e., the structure of linear dependence relations among code symbols, and define it as the block circulant topology  $T_{[\mu ,\lambda ,\omega]}(\rho)$ . In this topology, there are  $\mu $  local codes, each constrained by  $\rho $  parity checks. The set of symbols of a local code intersects with another in a uniform pattern, determined by two parameters, namely the overlap factor  $\lambda $  and the overlap width  $\omega $ . Next, we instantiate the topology, i.e., specify the coefficients of the linear dependence relations, to construct the block circulant codes  ${\mathcal { C}}_{\text {BC}}[\mu ,\lambda ,\omega ,\rho]$ . Every local code is a  $[\lambda \omega +\rho ,\lambda \omega ,\rho +1]$  generalized RS code. The block circulant code has  $n=\mu (\rho +\omega)$ ,  $k=\mu \omega $  and we show that, under certain conditions,  $d=\lambda \rho +1$ . For  $\lambda =2$ , we prove that  $d=2\rho +1$  always, and provide an efficient, parallelizable erasure-correcting decoder that fully recovers the codeword when there are  $\leq 2\rho $  erasures. The decoder uses a novel decoding mechanism that iteratively recovers erasures from either local codes or pairs of them.

## Coded Modulation Schemes for Voronoi Constellations

- **Status**: ❌
- **Reason**: 보로노이 성상도 소프트 FEC 변조 — 무선 채널 전용 constellation 설계, 이식 가능 LDPC 기법 없음
- **ID**: ieee:10937749
- **Type**: journal
- **Published**: Oct. 2025
- **Authors**: Shen Li, Ali Mirani, Magnus Karlsson +1
- **PDF**: https://ieeexplore.ieee.org/document/10937749
- **Abstract**: Multidimensional Voronoi constellations (VCs) have been shown to be more power-efficient than quadrature amplitude modulation (QAM) formats given the same uncoded bit error rate, and also have higher achievable information rates. However, a coded modulation scheme that sustains these gains after forward error correction (FEC) coding is still lacking. This paper designs coded modulation schemes with soft-decision FEC codes for VCs, including bit-interleaved coded modulation (BICM) and multilevel coded modulation (MLCM), together with three bit-to-integer mapping algorithms and log-likelihood ratio calculation algorithms. Simulation results show that VCs can achieve up to 1.84 dB signal-to-noise ratio (SNR) gains over QAM with BICM, and up to 0.99 dB SNR gains over QAM with MLCM for the additive white Gaussian noise channel at the bit error rate of  $1.81\times 10^{-3}$ , with a low decoding complexity.

## Balancing the Energy Consumption and Latency of Over-the-Air Firmware Updates in LoRaWAN

- **Status**: ❌
- **Reason**: LoRaWAN OTA 펌웨어 업데이트 에너지-지연 트레이드오프 — ECC와 무관
- **ID**: ieee:11045540
- **Type**: journal
- **Published**: Oct. 2025
- **Authors**: Siddhartha S. Borkotoky
- **PDF**: https://ieeexplore.ieee.org/document/11045540
- **Abstract**: Over-the-air firmware updates are crucial for mitigating security threats and maintaining up-to-date device functionality in long range wide area networks (LoRaWANs). LoRaWAN end devices are usually energy-constrained, and LoRaWAN transmissions are subject to duty-cycle restrictions. Consequently, controlling the energy expenditure and update-delivery latency of over-the-air firmware updates are key challenges. We propose a flexible scheme that achieves a tunable tradeoff between the energy consumption and delivery delay. The scheme employs the LoRa spreading factors sequentially to transmit update-carrying frames, sending a fixed number of frames with a given spreading factor before moving to the next. By adjusting the smallest spreading factor to be used and the number of transmissions per spreading factor, a suitable energy-delay tradeoff can be achieved. Thus, time-sensitive updates, such as security patches, may be sent with a low-delay-high-energy setting, whereas a more energy-efficient but higher delay setting may be used for noncritical updates.

## Partial Sampling-Based Semantic Communications

- **Status**: ❌
- **Reason**: 부분 샘플링 시맨틱 통신(RL+RNN) — ECC와 무관
- **ID**: ieee:11036176
- **Type**: journal
- **Published**: Oct. 2025
- **Authors**: Kaiwen Yu, Qi He, Gang Wu +1
- **PDF**: https://ieeexplore.ieee.org/document/11036176
- **Abstract**: Semantic communications have the potential to improve transmission efficiency and support intelligent tasks. However, the commonly used global sampling-based pattern ignores the fact that the data processing ability of edge transmitters is strictly limited and only a small part of information is available for a single sample in some scenarios. This paper proposes a novel partial sampling-based semantic communication (PSSC) framework where an edge transmitter is guided by feedback from the receiver to locate and collect only part of content relevant to the target task. Taking the vision-based task as an example, the transmitter selectively samples a small patch of a large-size image until the intelligent task is successfully executed at the receiver. The selection of sampling location is modeled as a partially observable Markov decision process problem and an intelligent approach based on reinforcement learning is proposed to solve the problem. In addition, a recurrent neural network-based receiver is designed to fuse information received over multiple transmission rounds. Besides, we prove that the feedback does not increase the semantic channel capacity. Simulation results demonstrate that the proposed framework can locate the informative areas accurately and achieve competitive performance compared to the existing global sampling-based methods.

## Tail-Biting Convolutional Codes for URLLC: Low-Complexity List Decoding and Rate-Compatible Construction

- **Status**: ❌
- **Reason**: CRC-TBCC + Viterbi(ST-SLVA) 기반 단거리 통신 코드 — LDPC 무관, 이식 가능 기법 없음
- **ID**: ieee:11030548
- **Type**: journal
- **Published**: Oct. 2025
- **Authors**: Dongming Pi, Chao Chen, Shancheng Zhao
- **PDF**: https://ieeexplore.ieee.org/document/11030548
- **Abstract**: Cyclic redundancy check-aided tail-biting convolutional code (CRC-TBCC) is considered as a competitive candidate for ultra-reliable and low-latency communications (URLLC) in short-length transmission scenarios. This paper focuses on designing efficient list decoders for CRC-TBCC and constructing rate-compatible CRC-TBCC (RC-CRC-TBCC). To reduce decoding complexity, we introduce a serial list Viterbi algorithm (SLVA) based on sectionalized trellises (ST), referred to as ST-SLVA. Comparative analysis reveals that ST-SLVA significantly lowers the decoding complexity. We then propose to use selectively multiplicative repetition (SMR) to construct high-performance rate-compatible CRC-TBCC. The resulting family of codes, called SMR-CRC-TBCCs, can be decoded with the same ST-SLVA. In SMR-CRC-TBCC, adjacent coded bits of CRC-TBCC are treated as symbols of a given finite field for multiplicative repetition, with priority given to the repetition of CRC-related symbols. Simulation results demonstrate that SMR-CRC-TBCC delivers excellent performance across various coding rates. Particularly, it performs better than CRC-aided Polar (CA-Polar) codes, LTE-Turbo codes, and parallel concatenated convolutional-block (PCCB) codes. These results strengthen the competitiveness of CRC-TBCC for 6G short-length communications.

## OGII: An Optimized Generalized Integrated Interleaved Decoder for Optical Disk Storage

- **Status**: ❌
- **Reason**: 광 디스크용 RS 기반 GII 디코더 HW — LDPC 무관, 이식 가능 기법 없음
- **ID**: ieee:11151302
- **Type**: journal
- **Published**: Oct. 2025
- **Authors**: Tianwei Gui, Meng Zhang, Wei Li +3
- **PDF**: https://ieeexplore.ieee.org/document/11151302
- **Abstract**: Optical disks are the ideal option for cold data storage because of their large capacity, extended lifespan, and low power consumption. To guarantee data dependability, strong error correction codes (ECCs) are needed since an increase in optical disk storage density raises the error rate. Generalized integrated interleaved (GII) codes based on Reed–Solomon (RS) codes can provide adequate data reliability at high code rates. However, the GII codes suffer from high decoding complexity due to nested decoding, which increases hardware resource consumption. Moreover, existing GII decoders are not optimized for the burst error characteristics in optical disk storage, limiting their error correction capability. In this paper, we propose an area-efficient OGII decoder architecture tailored for optical storage. The OGII decoder incorporates two key techniques: 1) a pipelining technique to reduce overall hardware resource consumption and 2) an error-erasure correction algorithm to enhance burst error correction capability. However, the key equation solver (KES) block remains the core component of the OGII decoder, and the introduction of the error-erasure correction algorithm increases complexity. Therefore, we propose a crisscross inverse-free Berlekamp–Massey architecture (CIBMA) to reduce hardware resource consumption and improve utilization efficiency in the core decoder module. Hardware implementation results demonstrate that under equivalent error correction capability, compared with traditional RS decoders in optical disk storage, the OGII achieves a 7.2% higher code rate and 15% lower power consumption with only  $1.17\times $  hardware resource utilization. Simulation experiments under identical code rates show that with a raw symbol error rate of 0.02 and additional burst errors, the OGII decoder reduces block error rate by 4–5 orders of magnitude compared with conventional GII decoders, and 3–4 orders of magnitude compared with traditional RS decoders. For the core CIBMA module in OGII, it achieves at least 20% hardware resource reduction and 50% improvement in pipeline utilization efficiency compared with other architectures based on error-erasure correction algorithms.

## Two-Component GMM Source Coding and Optimization

- **Status**: ❌
- **Reason**: P-LDPC 기반 GMM 소스 손실 압축 — 소스 코딩(압축) 제외 카테고리
- **ID**: ieee:11006292
- **Type**: journal
- **Published**: Oct. 2025
- **Authors**: Dan Song, Jinkai Ren, Lin Wang +3
- **PDF**: https://ieeexplore.ieee.org/document/11006292
- **Abstract**: A protograph low-density parity-check (P-LDPC) code-based lossy coding system is proposed for compressing the Gaussian mixture model source, as a particular case of shipping transportation systems. The compression performance is benchmarked against the rate-distortion bounds for this source. Some effective methods are developed to improve both the encoder and the decoder to reduce the compression distortion. Experimental results demonstrate that the proposed methods achieve good performance while maintaining low complexity.

## Optimized Spreading Sequences and Multi-Stage Receiver for Lattice-Code Multiple-Access

- **Status**: ❌
- **Reason**: 격자 코드 다중접속(LCMA) 확산 시퀀스 최적화 — 무선 MA 전용, LDPC ECC 이식 가능 기법 없음
- **ID**: ieee:11008493
- **Type**: journal
- **Published**: Oct. 2025
- **Authors**: Tao Yang, Jinsong Wang, Yiyu Yin +2
- **PDF**: https://ieeexplore.ieee.org/document/11008493
- **Abstract**: It was shown that by operating over the integer linear combinations (ILCs) of K users’ messages, lattice-code based multiple-access (LCMA) offers increased system load and improved error-rate performance over non-lattice based schemes. This paper advances the existing LCMA system in two aspects. 1) We formulate the spreading sequences optimization problem based on the achievable symmetric rate of LCMA. To solve this problem, we develop three new methods, namely target-switching steepest descent (TS-SD), particle swarm (PS) optimization, and Hadamard concatenation (HC). The TS-SD method always targets on the ILC with the lowest computation rate in the SD process. The PS method treats the spreading matrix as a particle and iteratively updates a swamp of particles’ positions and velocities, based on the relative distance to the best position that are currently known. To further reduce the complexity, we first obtain a solution in a lower dimension, and then apply Hadamard concatenation (HC) which yields a solution for the required dimension. The PS and HC methods are shown to approach the capacity of the MA channel. 2) We put forth a new multi-stage LCMA receiver. In each stage, the receiver attempts to compute as many ILCs as possible. Then, from these ILCs, generalized matrix inversion (GMI) is introduced to recover a subset of  $ K$  users’ messages. These recovered messages are cancelled from the original received signal, yielding an equivalent system with less users for the next stage. Such operation continues successively until all K users’ messages are recovered. System loads of up to 400% and near capacity performance are demonstrated for various MA models.

## Design of Low-Complexity DCMA Systems

- **Status**: ❌
- **Reason**: DCMA 저복잡도 코드북·메시지패싱 수신기 — 무선 다중접속 전용, LDPC 디코더 이식 불가
- **ID**: ieee:11023231
- **Type**: journal
- **Published**: Oct. 2025
- **Authors**: Shuangduo Zhang, Zheng Xiang, Peng Ren +3
- **PDF**: https://ieeexplore.ieee.org/document/11023231
- **Abstract**: Dense code multiple access (DCMA) with the fully-connected resource mapping has attracted growing attention due to the potential to achieve superior coding gain over sparse code multiple access (SCMA) systems. However, existing high-dimensional modulation DCMA systems suffer from substantial complexity in both codebook design and multi-user detection. This paper proposes low-complexity DCMA systems by leveraging low-projection (LP) codebooks and the LP message passing algorithm (LP-MPA) detector. Specifically, high-dimensional codebooks are constructed in a scalable manner based on distinct LP constellations and pre-designed constellation permutations. In addition, the message propagation of the MPA detector for the proposed LP codebooks is analyzed, and the low-complexity LP-MPA is introduced for multi-user detection. Simulation results demonstrate the superiority of the proposed DCMA system.

## Joint Detection and Decoding: A Graph Neural Network Approach

- **Status**: ❌
- **Reason**: GNN 기반 ISI 채널 수신기(JDD)로 무선 특이적; LDPC는 비교 코드 중 하나일 뿐 이식 가능 디코더 기법 없음
- **ID**: ieee:11036132
- **Type**: journal
- **Published**: Oct. 2025
- **Authors**: Jannis Clausius, Marvin Rübenacke, Daniel Tandler +1
- **PDF**: https://ieeexplore.ieee.org/document/11036132
- **Abstract**: Narrowing the performance gap between optimal and feasible detection in inter-symbol interference (ISI) channels, this paper proposes to use graph neural networks (GNNs) for detection that can also be used to perform joint detection and decoding (JDD). For detection, the GNN is build upon the factor graph representations of the channel, while for JDD, the factor graph is expanded by the Tanner graph of the parity-check matrix (PCM) of the channel code, sharing the variable nodes (VNs). A particularly advantageous property of the GNN is a) the robustness against cycles in the factor graphs which is the main problem for sum-product algorithm (SPA)-based detection, and b) the robustness against channel state information (CSI) uncertainty at the receiver. Consequently, a fully deep learning-based receiver enables joint optimization instead of individual optimization of the components, so-called end-to-end learning. Furthermore, we propose a parallel flooding schedule that also reduces the latency, which turns out to improve the error correcting performance. The proposed approach is analyzed and compared to state-of-the-art baselines for different modulations and codes in terms of error correcting capability and latency. The gain compared to SPA-based detection might be explained with improved messages between nodes and adaptive damping of messages. For a higher order modulation in a high-rate turbo detection and decoding (TDD) scenario the GNN shows a, at first glance, surprisingly high gain of 6.25dB compared to the best, feasible non-neural baseline.

## Deep Reinforcement Learning-Based Error Correction Method for Secure Data Transmission

- **Status**: ❌
- **Reason**: DRL/DQN 기반 적응형 전송 채널 제어로 LDPC는 비교 기준으로만 언급, 떼어낼 디코더·HW·코드설계 기법 없음.
- **ID**: ieee:11379643
- **Type**: conference
- **Published**: 9-10 Oct. 
- **Authors**: P Arthi Devarani, R. Balanriya, Shanmugaraja P +3
- **PDF**: https://ieeexplore.ieee.org/document/11379643
- **Abstract**: Since the communications network often adopts advanced communications systems, channel noise, jamming or badwill attacks from the hackers may be very capable of affecting the network; modelling communication channel systems may be very important for soner to correctly transfer data. Therefore, in this paper, an online dynamic adaptation mechanism based on deep reinforcement learning (DRL) and deep reinforcement learning based on deep q-network model (DQN) for an error correction scheme (DRL-ECMS). Therefore, to control the problem, the proposed system simulates the transmission channel into a DRL learning environment, which can be used to learn what does the agent need to do to make a wise transmission channel to mitigate transmission errors, while enhancing data integrity and transmission throughput. Deep learning models are implemented using the next generation cutting edge Pytorch framework, which is the leading development framework for neural architecture design and training model in GPU accelerated environment. Intensive experiments are performed to showcase the breadth of the proposed DRL-based scheme while successfully overcoming the erroneous bit-rates that are beyond any traditional Hamming coding & LDPC code with high tolerance to intrusional attacks & malicious interferences. This project will bring about a paradigm shift in smart self adaptive communications systems while providing reliability and security to the next generation networks.

## Enhancing LoRa Encryption with Post-Quantum Algorithms for IoT Security

- **Status**: ❌
- **Reason**: LDPC가 Niederreiter 암호화 기반(코드 기반 암호) 보안 목적으로만 사용되며, NAND ECC에 이식 가능한 디코더·HW·코드설계 기법 없음.
- **ID**: ieee:11288589
- **Type**: conference
- **Published**: 6-10 Oct. 
- **Authors**: Andrii Storozhko, Sergii Kibitkin, Olga Vilkhivska +2
- **PDF**: https://ieeexplore.ieee.org/document/11288589
- **Abstract**: The growing demand for secure, long-range wireless communication in the Internet of Things (IoT) has led to widespread adoption of LoRa technology. However, traditional LoRa implementations remain vulnerable to quantum computing attacks. This paper proposes the integration of post-quantum cryptographic algorithms, specifically Niederreiter encryption and LDPC codes, into LoRa systems to enhance their resilience. We explore the theoretical foundation of these algorithms, practical implementation strategies, and their impact on system performance. Experimental results and security analyses validate the feasibility of this approach, establishing a pathway for future-proof secure communication in LoRa-based IoT networks.

## SHARQ: Semantic HARQ for Reliable Distributed DNN Execution

- **Status**: ❌
- **Reason**: 유한길이 LDPC 코딩이 시맨틱 HARQ 무선 전송의 신뢰성 수단으로만 사용; LDPC는 베이스라인이며 떼어낼 ECC 기법 없음.
- **ID**: ieee:11310022
- **Type**: conference
- **Published**: 6-10 Oct. 
- **Authors**: Ian Andrew Harshbarger, Leïla Nasraoui, Marco Levorato
- **PDF**: https://ieeexplore.ieee.org/document/11310022
- **Abstract**: This paper proposes a semantic version of the hybrid automatic repeat request (SHARQ) protocol embedded within an enhanced split computing framework to optimize data transmission and inference accuracy over noisy wireless channels. The framework partitions a deep neural network between a user equipment (UE) and an edge server (ES). The UE processes the local portion of the model and sends the extracted semantic features to the ES, which performs the final segmentation. Through a cross-layer design, we aim to reduce transmission payload while maintaining high inference accuracy. Our framework utilizes dynamic and adaptive bottle-neck quantization to compress intermediate representations at the UE prior to transmission. Robustness against channel impairments is achieved through retransmission mechanism and finite-length low-density parity-check (LDPC) coding. Unlike conventional HARQ, SHARQ triggers retransmissions based on inference accuracy rather than packet error probability, aligning the retransmission logic with task-level performance. We perform a comprehensive evaluation of SHARQ across a range of signal-to-noise ratio (SNR) values, analyzing key parameters such as code rate, LDPC Hamming weight, and retransmissions number. A configuration space is established to assess inference accuracy and explore trade-offs between payload, throughput efficiency, and delay. Evaluation conducted using the Mask R-CNN model across various bottleneck sizes and code rates reveals that SHARQ significantly improves inference accuracy, particularly with the second transmission at medium SNR levels. For instance, at 0 dB and a code rate of 2/3, the second retransmission yields near-optimal accuracy, whereas additional retransmissions contribute little to no gain and increase latency. Overall, SHARQ offers an effective solution for improving semantic inference performance in wireless edge intelligence by balancing reliability, bandwidth, and delay.

## Cybersecurity Challenges and Post-Quantum Protection in Cardiovascular Monitoring Devices

- **Status**: ❌
- **Reason**: QC-LDPC를 Niederreiter 포스트양자 암호의 키 구조로 사용; ECC 오류정정 목적이 아니며 NAND에 이식 가능한 기법 없음.
- **ID**: ieee:11288634
- **Type**: conference
- **Published**: 6-10 Oct. 
- **Authors**: Serhii Pohasii, Serhii Holdobin, Yevgen Melenti +2
- **PDF**: https://ieeexplore.ieee.org/document/11288634
- **Abstract**: This paper explores cybersecurity for Cardiovascular Monitoring Devices (CMDs) in IoT, addressing vulnerabilities in wireless networks like Wi-Fi and 5G. It compares traditional methods (AES-256, TLS 1.3) with post-quantum algorithms (CRYSTALS-Kyber, Niederreiter), emphasizing their quantum resistance. A hybrid approach using Quasi-Cyclic LDPC codes with Niederreiter is proposed to reduce key sizes, enhancing security and efficiency for CMDs against emerging quantum threats.Keywords— STM32, GD32, Glitch, Cold Boot Stepping, Electromagnetic Analysis.

## Secure Key Derivation via RF Sensing with ISAC in 5G/6G Tactical Systems (Demo)

- **Status**: ❌
- **Reason**: 5G ISAC 키 도출 데모; LDPC 내용 없고 NAND ECC와 무관.
- **ID**: ieee:11310485
- **Type**: conference
- **Published**: 6-10 Oct. 
- **Authors**: Robert Zakrzewski, Mark A. Beach
- **PDF**: https://ieeexplore.ieee.org/document/11310485
- **Abstract**: Widespread wireless communication demands robust security management to prevent adversaries from exploiting ubiquitous radio signals. Traditionally, such security is enforced through mitigation strategies implemented at higher layers using symmetric and/or asymmetric cryptography. However, this introduces increasing complexity, particularly due to the key derivation and exchange mechanisms required. This challenge is further exacerbated in private networks, which often necessitate configuration and deployment at the tactical or ad-hoc level in hostile environments, where physical interception or cryptanalysis by adversaries is a significant risk.To address this, we propose a solution that performs key derivation by exploiting 5G waveforms and integrated sensing and communication (ISAC). This approach enables the extraction of highly correlated data between legitimate parties by leveraging the reciprocity of radio channels, while preventing eavesdroppers from replicating the key derivation process.In this demonstration, we show that incorporating physical-layer information introduces geographical awareness between communicating parties, without compromising the entropy and keys generation rate. Furthermore, we demonstrate that our method effectively prevents eavesdroppers from obtaining the information needed to compromise the derived keys. Finally, we implement the system using software-defined radio within the 5G FR1 frequency bands, achieving a 100% key agreement rate with high entropy across a range of environments.

## Ensuring Authenticity and Integrity Messages on Basis Complex Modified Algorithm UMAC on Crypto-Code Constructions using Rao-Nama Symmetrical Cryptosystems

- **Status**: ❌
- **Reason**: Rao-Nama 암호코드 구성 기반 인증 프로토콜 논문; LDPC 언급 없고 ECC 기법 전혀 없음.
- **ID**: ieee:11288698
- **Type**: conference
- **Published**: 6-10 Oct. 
- **Authors**: Alla Havrylova, Andrii Tkachov, Yevhen Melenti +2
- **PDF**: https://ieeexplore.ieee.org/document/11288698
- **Abstract**: This article discusses the structural diagrams involved in generating an authenticated message using the complex modified UMAC algorithm, which is based on modified Rao-Nama crypto-code constructions (MCCC) and hybrid Rao-Nama crypto-code constructions (HCCC). Proposed improvements to the SSL/TLS transport layer protocol utilize complex algorithms derived from Rao-Nama crypto-code constructions on modified elliptic codes (lossy codes) alongside an enhanced cascade UMAC hashing algorithm.

## Environment Aware Secure Key Derivation via RF Sensing and ISAC in 5G/6G Systems

- **Status**: ❌
- **Reason**: 5G/6G CSI 기반 물리계층 키 도출 논문; LDPC 내용 없고 NAND ECC와 무관.
- **ID**: ieee:11310054
- **Type**: conference
- **Published**: 6-10 Oct. 
- **Authors**: Robert Zakrzewski, Mark A. Beach
- **PDF**: https://ieeexplore.ieee.org/document/11310054
- **Abstract**: As wireless networks evolve toward 5G and 6G, securing communications in dense, dynamic, and potentially adversarial environments becomes increasingly critical. Traditional cryptographic security, relying on symmetric or asymmetric key exchanges at higher layers or pre-provisioning, imposes significant operational complexity—especially in decentralized private networks and tactical deployments where infrastructure is limited and exposure to interception or cryptanalysis is high.This work introduces an environment-aware cryptographic key derivation method that utilizes 5G NR waveforms and Integrated Sensing and Communication (ISAC) principles, accompanied by updates to the security frameworks in 5G and next-generation 6G networks. It exploits radio channel reciprocity to extract highly correlated features observable only by legitimate transceivers, while inherently excluding spatially separated eavesdroppers.Our system derives shared secret keys directly from Channel State Information (CSI), achieving high-entropy keys with a 100% agreement rate and a high key generation rate between legitimate nodes. We demonstrate its robustness using software-defined radios operating in the 5G FR1 band, across diverse environments, while constraining the amount of publicly accessible information available to potential eavesdroppers.By embedding geographical awareness, this approach provides a physically secure key generation method, making it well-suited for 5G/6G systems, private networks, and ultra-massive Machine-Type Communication (umMTC) scenarios. The results highlight the potential of physical layer security for future wireless encryption frameworks with design considerations to maximize security and limit eavesdropping feasibility.

## A Fast Parallel Decoder for LDPC Codes Suitable for Burst Errors in QKD Reconciliation

- **Status**: ❌
- **Reason**: [기준개정:비이진제외] GF상 LDPC 구성+NC 클래스 병렬 디코더 — 비이진 코드설계(E)·병렬 디코더 알고리즘(C) 이식 가능; QKD 응용이나 기법 분리됨
- **ID**: ieee:11240409
- **Type**: conference
- **Published**: 29 Sept.-3
- **Authors**: Duarte Mateus, Ricardo Chaves
- **PDF**: https://ieeexplore.ieee.org/document/11240409
- **Abstract**: Quantum Key Distribution (QKD) relies on quantum mechanics to enable secure communication, with the reconciliation phase playing an essential role in correcting discrepancies in shared keys caused by noise. Conventional Low-Density Parity-Check (LDPC) codes, while robust against random errors, often struggle with burst errors arising from localized noise sources in practical QKD implementations. To address this challenge, we introduce specialized uniform LDPC codes over Galois fields explicitly designed to correct burst errors effectively. We further present a highly efficient parallel decoder for these LDPC codes, operating within the complexity class NC (Nick’s Class), making it particularly suitable for GPU-based implementation. Our decoder provides guaranteed high-performance reconciliation as long as the number of burst errors remains below a designated threshold. Additionally, we discuss an extension to our decoding approach: when configured to handle higher error rates, the algorithm becomes a Las Vegas algorithm, introducing a small but controlled probability of failure. Finally, we propose a basic algorithm for generating these specialized LDPC codes and highlight prospective optimizations required for constructing larger matrices.

## Understanding the Ratio of the Partition Sum to its Bethe Approximation via Double Covers

- **Status**: ❌
- **Reason**: partition sum/Bethe approximation 비율의 순수 이론 분석 — 디코더·HW·코드설계로 이어지지 않음
- **ID**: ieee:11240320
- **Type**: conference
- **Published**: 29 Sept.-3
- **Authors**: Pascal O. Vontobel
- **PDF**: https://ieeexplore.ieee.org/document/11240320
- **Abstract**: For various classes of graphical models it has been observed that the ratio of the partition sum to its Bethe approximation is often close to being the square of the ratio of the partition sum to its degree-2 Bethe approximation. This is of relevance because the latter ratio can often better be analyzed and/or quantified than the former ratio. In this paper, we give some justifications for the observed relationship between these two ratios and then analyze these ratios for two classes of log-supermodular graphical models.

## On Design and Analysis of Asynchronous Repetition Slotted ALOHA for Massive Access

- **Status**: ❌
- **Reason**: 비동기 반복 슬롯 ALOHA 랜덤액세스 프로토콜; iterative soft cancellation은 다중사용자 검출, LDPC 부호설계/디코더 기법 없음
- **ID**: ieee:11240292
- **Type**: conference
- **Published**: 29 Sept.-3
- **Authors**: Xu Li, Tao Yang, Xiaojun Yuan +2
- **PDF**: https://ieeexplore.ieee.org/document/11240292
- **Abstract**: This paper studies asynchronous repetition slotted ALOHA (a-RSA) for massive random access. Each user’s packet is repeated and allocated to randomly selected slots. Then, the users transmit simultaneously and arrive at the base station (BS) receiver with different delays, i.e., without user-synchronization. The BS receiver carries out an over-sampling-based operation, yielding an over-sampled signal space. We develop an iterative soft cancellation detection and decoding that exploits the interference structure of the over-sampled signal for powerful multi-user decoding. Afterwards, packet cancellation for a-RSA is utilized to solve packet collision. To characterize the performance of a-RSA, we analyze the achievable channel parameter region (ACPR) and outage probability. Further, we present an asymptotic analysis of the throughput of a-RSA system. It is demonstrated that the normalized throughput of a-RSA exceeds that of traditional RSA by about 20% ~ 30%.

## Polar Code Design for MIMO-OFDM with Channel Sparsity

- **Status**: ❌
- **Reason**: polar code 설계(MIMO-OFDM, RM-channel degradation) — LDPC 아니고 무선 응용 특이적, 떼어낼 LDPC 기법 없음
- **ID**: ieee:11240473
- **Type**: conference
- **Published**: 29 Sept.-3
- **Authors**: Rongchi Xu, Tongzhou Yu, Shuangyang Li +2
- **PDF**: https://ieeexplore.ieee.org/document/11240473
- **Abstract**: In this paper, we consider the design of polar codes for point-to-point (P2P) MIMO-OFDM system with channel sparsity. We first adopt singular value decomposition (SVD) precoding to obtain a parallel symbol-wise fading channel with different effective signal-to-noise ratios (SNRs) on different subchannels due to the frequency selectivity. After a detailed evaluation on the effective SNRs, we show that the received symbols not only are corrupted by channel noise but also suffer from, effectively, channel erasure since some subchannels are in deep fade. Therefore, we propose the Reed Muller (RM)-channel degradation construction based on the statistical SNRs in achieving the balance between erasure correction and error correction abilities of polar codes via adjusting a tunable parameter. Numerical results show that a noticeable coding gain can be achieved by the proposed construction comparing with 5G polar codes.

## Experimental Demonstration of Next-Generation FEC-Coded Data Transmission for GEO Satellite-to-Ground Laser Link Using LUCAS Onboard the Optical Data Relay Satellite

- **Status**: ❌
- **Reason**: GEO 위성-지상 레이저 링크 5G NR LDPC/DVB-S2 적용 실험; 기성 부호 응용, 이식 기법 없음
- **ID**: ieee:11443166
- **Type**: conference
- **Published**: 28-31 Oct.
- **Authors**: Hideaki Kotake, Yasuhiro Takahashi, Dimitar Kolev +6
- **PDF**: https://ieeexplore.ieee.org/document/11443166
- **Abstract**: This paper presents experimental demonstration of next-generation Forward Error Correction (FEC)-coded data transmission for the downlink of Geostationary Earth Orbit (GEO) satellite-to-ground laser link between Laser Utilizing Communication System (LUCAS) and NICT Okinawa Optical Ground Station (OGS). The experiment has been conducted with the support of Nagoya Institute of Technology. In this study, Digital Video Broadcasting - Satellite - Second Generation (DVB-S2) and 5G New Radio Low-Density Parity-Check (5G NR LDPC) codes have been employed as next-generation FEC schemes, both with interleaving. For comparison, a conventional Reed Solomon (RS) code with interleaving has also been utilized. The experimental results have demonstrated that both codes successfully corrected burst errors caused by fades due to atmospheric turbulence, thereby improving BER performance, in comparison with RS code. Among both codes, DVB-S2 exhibited stronger error correction capability than 5G NR LDPC.

## Investigation of Fade Mitigation Methods on Experimental FSO LEO-to-Ground Links

- **Status**: ❌
- **Reason**: FSO LEO 위성 페이드 완화 비교(FEC/인터리빙/ARQ) 시스템 성능분석; LDPC 부수언급, 이식 기법 없음
- **ID**: ieee:11443140
- **Type**: conference
- **Published**: 28-31 Oct.
- **Authors**: Cuong T. Nguyen, Hoang D. Le, Dimitar R. Kolev +5
- **PDF**: https://ieeexplore.ieee.org/document/11443140
- **Abstract**: In recent years, the standardization of free-space optics (FSO)-based low-earth orbit (LEO) satellite communication systems has aroused growing interest. This is thanks to the ability to provide high data rates and global coverage of the optical satellite systems. However, one of the key challenges lies in selecting effective techniques to combat channel fading and improve system reliability. To address this, current standards consider forward error correction (FEC) codes and/or interleaving at the physical layer, along with automatic repeat request (ARQ) protocols at the link layer. This work aims to investigate and compare the performance of various fade mitigation strategies, which aligns with current standardization efforts. In particular, we conduct both information-theoretic analysis and simulation for key link-layer performance metrics, i.e., frame loss probability (FLP), goodput, and average system delay. Through this study, we provide insightful discussions and practical design guidelines that benefit the development of reliable optical satellite systems.

## Forward Error Correction Considerations for Optical Satellite Links

- **Status**: ❌
- **Reason**: 광위성 링크 FEC 선택 고찰; 채널특성 논의 위주로 떼어낼 디코더/HW/코드설계 없음
- **ID**: ieee:11443150
- **Type**: conference
- **Published**: 28-31 Oct.
- **Authors**: Eugenio Estinto, Scott Allwine, Luca Estinto
- **PDF**: https://ieeexplore.ieee.org/document/11443150
- **Abstract**: The worldwide adoption of Free-Space Optical Communications (FSOC) continues to advance due to its free spectrum and high bandwidth, including in the area of satellite communications. As with RF communications, forward error correction (FEC) is often employed in optical links to improve performance. qBeam has been researching and developing FSOC modems for nearly a decade, and has gained valuable insight into which FEC schemes are best suited for optical links. This paper will propose that treating optical communications in the same manner as RF satellite links is usually not the best approach from a FEC-selection perspective. This is due to the unique properties of optical detectors and the atmospheric turbulence effects associated with many optical links. This paper will describe two transmission channel regimes applicable to FSOC, compare the effectiveness of a few FEC approaches, and discuss ongoing qBeam optical modem efforts.

## 651-Gb/s Net Bitrate IMDD Transmission Using Electrical Bandwidth Multiplexing and Demultiplexing Techniques Based on Ultra-Broadband InP-DHBT Mixers

- **Status**: ❌
- **Reason**: InP-DHBT 믹서 기반 IMDD 고속전송 데모, ECC/LDPC 무관 광통신 하드웨어
- **ID**: ieee:11262960
- **Type**: conference
- **Published**: 28 Sept.-2
- **Authors**: Masanori Nakamura, Munehiko Nagatani, Teruo Jyo +10
- **PDF**: https://ieeexplore.ieee.org/document/11262960
- **Abstract**: We demonstrated 232-264-GBd IMDD signal generation and detection using electrical bandwidth multiplexing and demultiplexing configuration based on in-house 150-GHz InP-DHBT mixers with an adaptive reconstruction technique, achieving a record net bitrate per wavelength of 660-Gb/s back-to-back and 651-Gb/s 11-km transmission with 248-GBd PS-PAM12 signals. ©2025 The Author(s)

## Long-Haul 2000-Km Single-Mode Fibre Transmission with Net Bitrate of 105.6 Tb/S in S+C+L Band Using Low-Noise Forward-Pumped Distributed Raman Amplification

- **Status**: ❌
- **Reason**: Raman 증폭 장거리 전송, ECC 기법 없음
- **ID**: ieee:11263320
- **Type**: conference
- **Published**: 28 Sept.-2
- **Authors**: Fukutaro Hamaoka, Hiroto Kawakami, Kosuke Kimura +5
- **PDF**: https://ieeexplore.ieee.org/document/11263320
- **Abstract**: We have successfully demonstrated that our proposed forward-pumped distributed Raman amplification (DRA), which reduces noise transfer by using pump light with polarisation-interleaved narrow longitudinal modes, can dramatically extend transmission distance in conjunction with backwardpumped DRA, achieving net 105.6 Tb/s over 2000-km transmission in S+C+L band.

## Experimental Demonstration of Rate-Adaptation via Hybrid Polar-BCH Product Code for Flexible PON

- **Status**: ❌
- **Reason**: Polar-BCH product code(비LDPC)·하이브리드 디코더, PON 응용 특이로 LDPC ECC 이식 기법 약함
- **ID**: ieee:11263381
- **Type**: conference
- **Published**: 28 Sept.-2
- **Authors**: Yifan Ye, Bin Chen, Xiang Li +5
- **PDF**: https://ieeexplore.ieee.org/document/11263381
- **Abstract**: The flexible-rate Polar-BCH product codes are experimentally demonstrated in a coherent passive optical network system with 16QAM for the first time. Using a new hybrid soft- and hard-decision decoder, we achieve a power gain of upto 1.75 dB over traditional BCH-BCH product codes after 48 km transmission.

## 11.5 Gbit/s Transmission Using a 660 mW LiFi Transmitter

- **Status**: ❌
- **Reason**: LiFi 송신기 데모, LDPC FEC rate 5/6은 베이스라인 언급뿐
- **ID**: ieee:11263327
- **Type**: conference
- **Published**: 28 Sept.-2
- **Authors**: Malte Hinrichs, Giulio Boniello, Atiyeh Pouralizadeh +3
- **PDF**: https://ieeexplore.ieee.org/document/11263327
- **Abstract**: We demonstrate LiFi transmission at a net data rate of 11.5 Gbit/s after LDPC FEC with rate 5/6, using 9 VCSEL arrays with a combined optical power of 660 mW and OFDM with adaptive bit and power loading. ©2025 The Author(s)

## Short Range Optical Wireless Communication at 67.8 Gbit/s using a Multiaperture VCSEL

- **Status**: ❌
- **Reason**: 광무선 VCSEL 링크, LDPC FEC는 베이스라인 부수 언급, 이식 가능 기법 없음
- **ID**: ieee:11263098
- **Type**: conference
- **Published**: 28 Sept.-2
- **Authors**: Matthias Koepp, Christoph Kottke, Ronald Freund +4
- **PDF**: https://ieeexplore.ieee.org/document/11263098
- **Abstract**: We demonstrate a point-to-point optical wireless communication link for fixed wireless access scenarios using a multiaperture VCSEL. At 5 meters distance, a data rate of $67.8 \text{Gbit} / \mathrm{s}$ is reached after LDPC FEC. ©2025 The Author(s)

## Experimental Evaluation of Throughput Gains from Distributed Raman Amplification in Ultra-Wideband Escl Transmission

- **Status**: ❌
- **Reason**: 분산 라만 증폭 광전송 처리량 측정 실험, LDPC/ECC 무관 광통신 물리계층
- **ID**: ieee:11262926
- **Type**: conference
- **Published**: 28 Sept.-2
- **Authors**: D. A. Shaji, B. J. Puttnam, R. S. Luís +12
- **PDF**: https://ieeexplore.ieee.org/document/11262926
- **Abstract**: We investigate and quantify the throughput gains of distributed Raman amplification over ultrawideband ESCL transmission systems. Our results show distance-dependent data-rate improvements of $1.5 \%, 5.3 \%$, and 40.0 % at $50 ~\text{km}, 100 ~\text{km}$, and 150 km, respectively. ©2025 The Author(s)

## Super-Rated IM/DD PON Downstream Demonstration at 100G Net Rate Using Line Rates up to 124 Gb/s

- **Status**: ❌
- **Reason**: PON PAM2/PAM4 광전송 데모, LOPC 코드 언급뿐 떼어낼 디코더·HW·코드설계 기법 없음(무선/통신 응용 특이)
- **ID**: ieee:11263040
- **Type**: conference
- **Published**: 28 Sept.-2
- **Authors**: M. Verplaetse, C. Füllner, W. Lanneer +3
- **PDF**: https://ieeexplore.ieee.org/document/11263040
- **Abstract**: We demonstrate super-rated PON downstream transmission at 100Gb/s net rate using PAM2 and PAM4 line rates ranging between 109 and 124Gb/s, exploiting an optimized LOPC code set. We showcase loss budgets >30dB for transmission equivalent to 20km at 1320nm.

## Digital vs Analog Equalization in FEC Supported 50G-PON

- **Status**: ❌
- **Reason**: 디지털 vs 아날로그 등화 비교 연구, soft/hard-input FEC 비교뿐 떼어낼 ECC 기법 없음
- **ID**: ieee:11263416
- **Type**: conference
- **Published**: 28 Sept.-2
- **Authors**: D. Chevalier, L. Anet Neto, G. Simon +8
- **PDF**: https://ieeexplore.ieee.org/document/11263416
- **Abstract**: We compare digital equalizer with soft-input FEC versus analog equalizer with hard-input FEC for 50G-PON. Only 0.4 dB penalty with analog implementation is obtained allowing low ONU costs while ensuring D/E2 classes compliance with 5 dB margin.

## Compact Continuous-Variable Quantum Key Distribution System Employing Monolithically Integrated Silicon Photonic Transceiver

- **Status**: ❌
- **Reason**: CV-QKD 실리콘 포토닉 송수신기 데모, 양자키분배·보안 영역으로 떼어낼 고전 LDPC 부호설계 없음
- **ID**: ieee:11263038
- **Type**: conference
- **Published**: 28 Sept.-2
- **Authors**: Denis Fatkhiev, João dos Reis Frãzao, Alireza H. Derkani +4
- **PDF**: https://ieeexplore.ieee.org/document/11263038
- **Abstract**: We demonstrate the first CV-QKD system featuring a custom-designed monolithic silicon photonic dual-polarisation transceiver. Leveraging PS-64-QAM, we achieved 1.9 Mbit/s secret key rate across 25 km of standard single-mode fibre, highlighting the potential of electronic-photonic integration for practical QKD. © 2025 The Authors

## Digital Subcarrier-Based Synthesis for On-Site Transceiver Calibration with Separate Tx/Rx Frequency Responses

- **Status**: ❌
- **Reason**: 트랜시버 IQ 왜곡 캘리브레이션, ECC/LDPC 기법 전무
- **ID**: ieee:11263148
- **Type**: conference
- **Published**: 28 Sept.-2
- **Authors**: Masaki Sato, Hidemi Noguchi, Junichiro Matsui +2
- **PDF**: https://ieeexplore.ieee.org/document/11263148
- **Abstract**: We proposed transceiver calibration using digital subcarrier-based synthesising to separate Tx/Rx frequency-dependent IQ common distortion. A flat signal spectrum and up to 0.1-dB Q-penalty within a ±3-GHz frequency offset range were demonstrated with 128-Gbaud PM-64QAM transmission over 120-km SMF, performing comparably to calibrating at back-to-back.

## Experimental Investigation of Availability in a 4.6 Km Terrestrial Urban Coherent Free-Space Optical Communications Link

- **Status**: ❌
- **Reason**: 자유공간 광통신 링크 가용성 측정, LDPC/ECC 무관 채널 측정 실험
- **ID**: ieee:11263027
- **Type**: conference
- **Published**: 28 Sept.-2
- **Authors**: Vincent Van Vliet, Menno Van Den Hout, Kadir Gümüş +2
- **PDF**: https://ieeexplore.ieee.org/document/11263027
- **Abstract**: We measured the outage probability of a 4.6-km urban free-space optical communication link over six days. High-speed power measurements reveal slow and fast fading effects, with link availabilities of 92% including and 99% excluding slow fades for $500 \text{Gb} / \mathrm{s}$ transmission. ©2025 The Author(s)

## Iterative Time-Varying Channel Tracking for Multiple-RIS Assisted MIMO Systems

- **Status**: ❌
- **Reason**: RIS-MIMO 채널추정에 LDPC를 보조로 활용 — LDPC가 부수 언급, 떼어낼 디코더·코드설계 기법 없음(무선 응용 특이적)
- **ID**: ieee:11443928
- **Type**: conference
- **Published**: 26-29 Oct.
- **Authors**: Roberto C. G. Porto, Rodrigo C. de Lamare
- **PDF**: https://ieeexplore.ieee.org/document/11443928
- **Abstract**: The use of multiple Reconfigurable Intelligent Surfaces (RIS) has gained attention in 6G networks to enhance coverage. However, the feasibility of deploying multiple RIS relies on efficient channel estimation and reduced pilot overhead. To address these challenges, this work proposes an iterative channel estimation scheme that exploits low-density parity-check (LDPC) codes, channel coherence time, and iterative processing to improve estimation accuracy while minimizing pilot length. Encoded pilots are used to strengthen the iterative processing, leveraging both pilot and parity bits, while previous estimates are incorporated to further reduce overhead. Simulations consider a sub-6 GHz scenario with non-sparse channels and multiple RIS under both LOS and NLOS conditions. The results show that the proposed method outperforms existing approaches, achieving significant gains with substantially lower pilot overhead.

## Bias-Enhanced Successive Cancellation List Decoder for Polar Codes

- **Status**: ❌
- **Reason**: Polar code SCL 디코더 bias 기법 — polar 전용 list 디코딩 개선이며 LDPC 부호설계·디코더로 이식할 기법 없음
- **ID**: ieee:11443908
- **Type**: conference
- **Published**: 26-29 Oct.
- **Authors**: Jiajie Li, Sihui Shen, Warren J. Gross
- **PDF**: https://ieeexplore.ieee.org/document/11443908
- **Abstract**: Polar codes with the successive cancellation (SC) de-coder are proven to achieve the channel capacity asymptotically. However, polar codes with SC decoding suffer from performance degradation when decoding short-to-medium length polar codes. The successive cancellation list (SCL) decoder improves the decoding performance of the SC decoder when decoding short-to-medium-length polar codes. The SCL decoder faces many implementation challenges, such as the decoding latency and the area overhead. A recently proposed perturbation-enhanced (PE) SCL decoder with a list size of L reaches the error correction performance of the SCL decoder with a list size of 2L. However, the reason behind this improved decoding performance needs to be investigated. An ablation study on the PE SCL decoder is performed in this work, and we found that the bias added to the received soft information is key for improved error correction performance. Hence, we propose to remove the random noise added to the PE SCL decoder, and we call our simplified decoder the bias-enhanced decoder. From experimental results, our bias-enhanced SCL decoder returns similar decoding performance to the PE SCL decoder under various code lengths and rates.

## Demonstration of Enabling Computational Technologies for RF Convergence

- **Status**: ❌
- **Reason**: DASH SoC 기반 5G-PHY/RF convergence HW 데모 — LDPC ECC 디코더 특정 기법 없음, 시스템 통합 데모
- **ID**: ieee:11443752
- **Type**: conference
- **Published**: 26-29 Oct.
- **Authors**: S. Siddiqui, A. Chiriyath, N. Luhana +2
- **PDF**: https://ieeexplore.ieee.org/document/11443752
- **Abstract**: As technological advances in wireless communications and similar trends in reconfigurable computing converge, there is an increasing need to design systems that demonstrate high-throughput, low-latency, multi-functionality, and security, along with realistic application implementation capabilities. The DASH SoC has emerged as a viable platform for implementing RF Convergence-based applications such as integrated sensing and communications (ISAC), which require a high degree of flexibility and energy efficiency to support concurrent multi-function tasks. Our work focuses on the hardware implementation of a 5G-PHY surrogate system comprising of both the transmit and receive chains. The design of 5G PHY (Physical layer) is an interesting problem that coincides with the ongoing development of the open RAN (Radio Access Network). We have utilized the DASH SoC platform for implementation purposes, demonstrating the high degree of domain adaptation and feasibility of coarse-scale heterogeneous SoCs serving as a system solution for multi-function tasks such as ISAC. In this work, we have also enabled real-time runtime scheduler performance monitoring that helps in optimizing resource selection across the SoC to provide optimal performance in terms of resource utilization, latency, and throughput.

## A Self-Refining Multi-Layer Receiver Pipeline

- **Status**: ❌
- **Reason**: 5G DMRS 채널추정·등화 self-refining 수신 파이프라인 — 무선 채널추정 특이적, LDPC ECC 기법 없음
- **ID**: ieee:11443343
- **Type**: conference
- **Published**: 26-29 Oct.
- **Authors**: Shahab Hamidi-Rad, Akshay Malhotra
- **PDF**: https://ieeexplore.ieee.org/document/11443343
- **Abstract**: In the 5G/NR standard, DeModulation Reference Signals (DMRS) are used for channel estimation and equalization. However, their performance is tightly coupled with resource allocation: increasing DMRS resources improves estimation quality but reduces the capacity available for user data, leading to a lower overall throughput. To address this tradeoff, this paper proposes a self-refining receiver pipeline that leverages information from successfully decoded code blocks to iteratively enhance channel estimation, thereby improving equalization and reducing block errors. In addition, a novel deep learning–based multi-layer channel estimation method is introduced, which integrates decoded code-block information with DMRS reference signals to further improve estimation accuracy. We evaluate the efficacy of this approach using an end-to-end 3GPP-compliant communication pipeline. The results demonstrate a significant reduction in the Block Error Rate (BLER), showing performance that approaches the theoretical throughput achieved with perfect channel knowledge.

## Optimizing LoRa for Underwater Acoustic Links: Carrier Frequency and Spreading Factor Trade-Offs

- **Status**: ❌
- **Reason**: 수중음향 LoRa SF 최적화 — LDPC ECC 기법 없음
- **ID**: ieee:11232417
- **Type**: conference
- **Published**: 25-27 Oct.
- **Authors**: Mohamed Farag Elshahat, Mohamed R. M. Rizk, Said E. El-Khamy
- **PDF**: https://ieeexplore.ieee.org/document/11232417
- **Abstract**: Underwater Acoustic Communication (UWAC) is critical in environments where RF/Optical signals attenuate rapidly. This paper validates Long Range (LoRa) as a robust UWAC solution, leveraging its resilience to multipath fading and Doppler shifts. Comprehensive simulations analyzed low (10 kHz), medium (30 kHz), and high (50 kHz) frequencies with spreading factors (SF) (7-12). Higher SFs have been validated to reduce required SNR by 18 dB, while carrier frequencies govern range-data rate tradeoffs. We provide practical guidelines: low frequencies with high SFs for sensor networks, medium frequencies with mid-range SFs for underwater vehicles, and higher frequencies with lower SFs for short-range applications. This work presents a novel adaptive optimization framework for LoRa-based UWAC systems, enabling robust long-range networks for various underwater applications.

## Generalized Index Modulation with Error Propagation Mitigation for OFDM

- **Status**: ❌
- **Reason**: OFDM 인덱스 변조 기법 — LDPC/디코더 무관
- **ID**: ieee:11231781
- **Type**: conference
- **Published**: 25-27 Oct.
- **Authors**: A. Atef Ibrahim, Amr A. Nagy, Amr Abdelaziz +1
- **PDF**: https://ieeexplore.ieee.org/document/11231781
- **Abstract**: Recent researches have focused on enhancing Orthogonal Frequency Division Multiplexing with Index Modulation (OFDM-IM) to create a more generalized framework capable of accommodating various configurations without restrictions. However, implementing a Generalized Index Modulation (GIM) presents several key challenges. First, spectral efficiency (SE) suffers when subcarriers are deactivated, particularly with higher-order modulation (M-ary), as each inactive subcarrier causes a reduction in spectral efficiency (SE) by log2 M bits. Second, varying the number of active subcarriers in M-ary systems can lead to error propagation across the data frames if index bits detection is incorrect. This paper introduces a streamlined method for generating and detecting OFDM-IM frames by directly converting input bit streams into ON/OFF symbols. Additionally, utilizing all possible subcarrier activation patterns (SAP) by dynamically adjusting the number of active subcarriers based on input data eliminates the need for frame segmentation into smaller sub-blocks, thereby simplifying receiver detection. The derived symbol error rate (SER) expressions for two implementations of this scheme demonstrate close agreement with simulation results, validating the analytical approach.

## ANFIS-Guided Region-Adaptive Semantic Compression Under QoS Constraints

- **Status**: ❌
- **Reason**: ANFIS 기반 시맨틱 이미지 압축, BPG+LDPC는 baseline 비교용 — 소스코딩/시맨틱 통신, 떼어낼 채널 ECC 기법 없음
- **ID**: ieee:11335965
- **Type**: conference
- **Published**: 24-26 Oct.
- **Authors**: Chao Wu, Zhaoyang Du, Yangfei Lin +4
- **PDF**: https://ieeexplore.ieee.org/document/11335965
- **Abstract**: With the rise of emerging applications such as augmented reality (AR) and autonomous driving, traditional communication techniques based on pixel-level reconstruction are inadequate for coping with the growing network load. In contrast, semantic communication based on semantic-level reconstruction effectively reduces data redundancy and preserves key semantic features required by downstream tasks, thereby achieving more quickly communication. To achieve practical deployment, semantic communication still requires to ensure the quality of services (QoS) by adapting to bandwidth, channel noise, and user requirements under different environments. Motivated by this, we propose an ANFIS-guided region-adaptive semantic compression system under QoS constraints. The system segments images into regions of interest (ROI) and regions of non interest (Non-ROI) based on region importance, and then takes QoS factors (bandwidth, channel noise, and user-defined clarity level) into account to achieve differentiated image transmission and compression. The experiment results show that the accuracy of compression inference using the adaptive network based fuzzy inference system (ANFIS) exceeds 92 %, and the proposed autoencoder outperforms the existing W_RA and W_RA_SA methods in PSNR performance under all CBRs. When the CBRs are less than 0.125, the PSNR performance is better than that of BPG+LDPC. These results highlight the effectiveness of integrating ANFIS into the compression scheduling of image semantic communication systems, particularly in extreme communication environments. Moreover, the system shows promising potential for extension to scenarios such as edge intelligent monitoring, disaster warning, and low orbit satellite communication.

## Enhanced Polynomial Interpolation Protocol for Secure and Efficient Quantum Key Distribution

- **Status**: ❌
- **Reason**: QKD reconciliation용 다항식 보간 프로토콜, LDPC는 복잡도 비교 대상일 뿐 — QKD/보안, 떼어낼 LDPC 기법 없음
- **ID**: ieee:11383077
- **Type**: conference
- **Published**: 24-26 Oct.
- **Authors**: Hong Chen, Jiahua Zhang, Cong Wu
- **PDF**: https://ieeexplore.ieee.org/document/11383077
- **Abstract**: Quantum key distribution (QKD) enables unconditional secure communication by exploiting the principles of quantum mechanics. However, existing reconciliation protocols face a trade-off between error correction efficiency and information leakage. To address this challenge, we propose an enhanced QKD reconciliation scheme based on polynomial interpolation. The protocol introduces a block-wise algebraic structure to unify error detection and correction, significantly reducing interactive rounds while maintaining high efficiency. A comprehensive information-theoretic leakage model is established, covering polynomial interpolation, verification, and iterative error localization. To further ensure unconditional security, a cascaded privacy amplification mechanism is integrated, combining two compression stages tailored to reconciliation leakage and quantum channel leakage, respectively. Moreover, an adaptive parameter optimization strategy dynamically adjusts block size and polynomial order according to the quantum bit error rate (QBER), achieving robustness under diverse channel conditions. Theoretical analysis and simulations demonstrate that the proposed scheme achieves a secure key rate of 65–72% at QBER < 3%, outperforming the classical CASCADE protocol by 8–12%, and maintains 30–50% efficiency under moderate error rates. Computational complexity analysis shows performance comparable to LDPC-based approaches while offering superior leakage control. These results confirm that the proposed protocol provides a balanced trade-off among efficiency, security, and implementation complexity, making it suitable for deployment in practical QKD systems.

## Finite Blocklength Analysis for Short Packet MIMO Systems with Optimal ML Receiver

- **Status**: ❌
- **Reason**: MIMO URLLC 유한블록길이 ML 수신기 오류확률 이론 분석 — 순수 bound, 디코더/HW/구성으로 안 이어짐
- **ID**: ieee:11352229
- **Type**: conference
- **Published**: 23-25 Oct.
- **Authors**: Rui Zhang, Hong Shen, Zhicheng Li +3
- **PDF**: https://ieeexplore.ieee.org/document/11352229
- **Abstract**: This paper performs finite blocklength error probability analysis for multiple-input multiple-output (MIMO) ultra-reliable and low-latency communications (URLLC) systems equipped with an optimal maximum likelihood (ML) receiver, which moves beyond a recent relevant study using the linear minimum mean-squared error (LMMSE) combining scheme. In particular, we first characterize the upper bound of the block error probability of the considered system via the random-coding union bound with parameter $s$ (RCUs). Then, in order to lower the computational cost of the RCUs bound, we provide asymptotic analysis utilizing both normal approximation and saddlepoint approximation. The derived theoretical results turn out to be quite different from existing ones based on the LMMSE receiver. Moreover, the significant performance gain achieved by the optimal ML receiver is also revealed via the derived results.

## Implementation of a HARQ-Assisted Hybrid SCMA-OMA System Using USRP

- **Status**: ❌
- **Reason**: HARQ-보조 SCMA-OMA 다중접속 USRP 프로토타입 — LDPC 무관 무선 응용 특이적
- **ID**: ieee:11352166
- **Type**: conference
- **Published**: 23-25 Oct.
- **Authors**: Zhonghao Li, Jintao Wang, Zheng Shi +4
- **PDF**: https://ieeexplore.ieee.org/document/11352166
- **Abstract**: To support massive connectivity in the future Internet of Things (IoT), sparse code multiple access (SCMA) is recognized as a promising technique with high spectral efficiency within limited time and frequency resources. However, its reception reliability cannot be guaranteed under harsh propagation conditions. To address this limitation, we propose a hybrid automatic repeat request (HARQ)-assisted multiple access system that dynamically switches between SCMA and orthogonal multiple access (OMA), enhancing reliability through retransmissions while reducing decoding complexity. A communication prototype is developed using LabVIEW and multiple universal software radio peripheral (USRP) B210s to experimentally validate the theoretical findings. Experimental results demonstrate that the proposed HARQ-assisted hybrid SCMA-OMA scheme achieves superior bit error rate (BER) performance compared to conventional multiple access approaches.

## Sub-7GHz-Aided Adaptive MCS Selection for Millimeter-Wave Beamforming

- **Status**: ❌
- **Reason**: mmWave 빔포밍 적응형 MCS 선택 프레임워크 — ECC/LDPC 무관 무선 응용
- **ID**: ieee:11352304
- **Type**: conference
- **Published**: 23-25 Oct.
- **Authors**: Wei Jiang, Yi Zhong
- **PDF**: https://ieeexplore.ieee.org/document/11352304
- **Abstract**: Millimeter-wave (mmWave) beamforming training (BFT) in IEEE 802.11ad/ay systems incurs significant time overhead due to constraints from a static Modulation and Coding Scheme (MCS) and redundant signaling. This study proposes a Sub-7GHz-aided adaptive MCS selection framework for mmWave beamforming training. Using dual-band cooperation and a quantitative SNR-PER-throughput model, the protocol dynamically selects optimal MCS levels, achieving balanced robustness while minimizing time overhead. The proposed framework introduces two MCS mapping schemes. Scheme 1 prioritizes throughput maximization through probabilistic SNR thresholds, while Scheme 2 incorporates error vector magnitude (EVM) constraints from IEEE 802.11ad for enhanced robustness. Link-level simulations demonstrate that adaptive MCS application reduces the duration of the BFT by 39.85 % (to $572 \mu ~\mathrm{s}$) under high SNR conditions compared to legacy MCS 0 baselines, with Scheme 1 achieving effective throughput gains of $1.16 x$ and Scheme 2 maintaining the probability of success of BFT 100 %. This work establishes a lightweight BFT paradigm compatible with Multi-Link Operation (MLO) in IEEE 802.11be, offering scalable solutions for high-mobility mmWave scenarios through Sub-7GHz control plane offloading.

## Outdoor Experiment of Deep Joint Source-Channel Coding Using FFT-Enabled Convolutional Neural Network for Image Transmission

- **Status**: ❌
- **Reason**: DeepJSCC 시맨틱 통신 — 떼어낼 LDPC ECC 기법 없음, 제외
- **ID**: ieee:11249228
- **Type**: conference
- **Published**: 22-24 Oct.
- **Authors**: Tomoka Mori, Hiroshi Tatsukawa, Yuji Kawai +3
- **PDF**: https://ieeexplore.ieee.org/document/11249228
- **Abstract**: Deep Joint Source-Channel Coding (DeepJSCC) has gained attention as a form of semantic communication that conveys not only information but also meaning and intent. It leverages deep learning, utilizing an autoencoder to map information sources such as images directly to IQ symbols. DeepJSCC has been extensively studied for image transmission, demonstrating advantages such as avoiding the cliff effect and achieving a high Peak Signal-to-Noise Ratio (PSNR) even in low Signal-to-Noise Ratio (SNR) regions. Traditionally, convolutional neural network (CNN)-based autoencoders are used in DeepJSCC for image transmission. However, depending on the terminal used, these methods can be computationally intensive. To address this challenge, the authors have proposed FFT-DeepJSCC, which replaces the 2D convolutional layer within the CNN with Fast Fourier Transform (FFT) and element-wise product operations. This modification aims to reduce the computational burden while maintaining performance. The study evaluates the computational load reduction achieved by FFT-DeepJSCC and examines the impact of the altered layer structure on PSNR. Furthermore, the authors validate the method's effectiveness through actual image transmission experiments using a modified commercially available 5G base station and user terminal. The results demonstrate the performance and feasibility of the proposed approach.

## Logical Qubit Initialization and Measurement in the Heavy-Hexagonal Lattice

- **Status**: ❌
- **Reason**: 표면부호 양자 EC(heavy-hex 레이아웃), 순수 양자 오류정정으로 제외
- **ID**: ieee:11224815
- **Type**: conference
- **Published**: 22-23 Oct.
- **Authors**: Aziz Kerem Özkan, Muhammet Talha Kakız, Erkan Güler +1
- **PDF**: https://ieeexplore.ieee.org/document/11224815
- **Abstract**: Improvements in quality of life and technological advancement are often accompanied by increasingly complex societal challenges. When formulated as computational problems, these challenges can exceed the processing capacity of classical computing. Quantum algorithms can solve these problems more efficiently by leveraging the principles of superposition and entanglement. However, in practice, quantum computation is highly susceptible to qubit errors, which can compromise the results. Various quantum error correction methods were proposed to eliminate these errors. In this paper, the application of one such method-the surface code-to the heavy-hexagonal quantum processor layout is studied and the future research directions are highlighted.

## A Maximum-Likelihood Decoding of BCH Codes

- **Status**: ❌
- **Reason**: BCH 코드 ML 디코딩(FPT/TEP), LDPC 아닌 대수부호 디코더
- **ID**: ieee:11478537
- **Type**: conference
- **Published**: 20-23 Oct.
- **Authors**: Qianfan Wang, Yiwen Wang, Jifan Liang +2
- **PDF**: https://ieeexplore.ieee.org/document/11478537
- **Abstract**: This paper presents the maximum-likelihood (ML) decoding of BCH codes, where the test error patterns (TEPs) are generated by the flipping pattern tree (FPT) based on soft weights and the hard-decision decoding algorithm is then applied to identify valid TEPs, with the most likely one selected as the output. We introduce ordered search strategies with earlystopping criteria and prove that the resulting decoder is an ML algorithm without exhaustive search. To determine the maximum number of searches, we propose a simple rule based on the upper bound on the performance gap to ML decoding, which can be efficiently computed using saddlepoint methods. Numerical results show that the proposed algorithm outperforms the Chase-BM algorithm in terms of the average number of searches, thanks to the optimized search order and early termination. They also show that for medium-to-high rate BCH codes, the proposed algorithm approaches the finite-length bound, while for lower rates, it offers significant advantages over both single-stage FPT and BM decoding, despite a gap to the finite-length capacity.

## Overlapped Arithmetic Code is a Many-to-Many Mapping for Nonuniform Sources

- **Status**: ❌
- **Reason**: 중첩 산술부호 소스코딩(Slepian-Wolf), 채널코딩 ECC 아님
- **ID**: ieee:11478558
- **Type**: conference
- **Published**: 20-23 Oct.
- **Authors**: Yong Fang
- **PDF**: https://ieeexplore.ieee.org/document/11478558
- **Abstract**: It is well known that lossless multi-terminal source coding, or the so-called Slepian-Wolf coding, can be implemented by coset codes. A coset code generated by a linear block code is a linear many-to-one mapping, and a coset code generated by an overlapped arithmetic code is a nonlinear many-to-one mapping for uniform sources. In this paper, we find for the first time that an overlapped arithmetic code is a messy many-to-many mapping for nonuniform sources. To solve this problem, a Local Encoder at Decoder (LED) structure is proposed, whose significant effectiveness is verified by experimental results.

## Sparse Code Transceiver Design for Unsourced Random Access with Analytical Power Division in Gaussian MAC

- **Status**: ❌
- **Reason**: 비인가 랜덤접속용 sparse code 송수신기·전력분할; LDPC ECC 디코더/구성 기법 아닌 다중접속 코딩
- **ID**: ieee:11310294
- **Type**: conference
- **Published**: 19-22 Oct.
- **Authors**: Zhentian Zhang, Mohammad Javad Ahmadi, Jian Dang +3
- **PDF**: https://ieeexplore.ieee.org/document/11310294
- **Abstract**: In this work, we discuss the problem of unsourced random access (URA) over a Gaussian multiple access channel (GMAC). To address the challenges posed by emerging massive machine-type connectivity, URA reframes multiple access as a coding-theoretic problem. The sparse code-oriented schemes are highly valued because they are widely used in existing protocols, making their implementation require only minimal changes to current networks. However, drawbacks such as the heavy reliance on extrinsic feedback from powerful channel codes and the lack of transmission robustness pose obstacles to the development of sparse codes. To address these drawbacks, a novel sparse code structure based on a universally applicable power division strategy is proposed. Comprehensive numerical results validate the effectiveness of the proposed scheme. Specifically, by employing the proposed power division method, which is derived analytically and does not require extensive simulations, a performance improvement of approximately 2.8 dB is achieved compared to schemes with identical channel code setups.

## Leveraging Code-Domain Perturbations for Enhancing Data Sensing in ISAC Systems

- **Status**: ❌
- **Reason**: ISAC 센싱용 코드도메인 섭동; 정보비트 섭동·센싱 기법, ECC/LDPC 디코더·설계 기여 아님
- **ID**: ieee:11310286
- **Type**: conference
- **Published**: 19-22 Oct.
- **Authors**: Lei Zhang, Zhifan Ye, Shichao Jin +1
- **PDF**: https://ieeexplore.ieee.org/document/11310286
- **Abstract**: To fully leverage communication resources for pervasive sensing within existing architectures, it is crucial to enable perception through the use of transmitted data. Unlike traditional waveform designs that focus exclusively on modulation, this paper introduces a novel approach starting from the information bit level. By applying controlled perturbations, approximate codewords are aligned with deterministic optimization waveforms, effectively suppressing sidelobe levels and enhancing data-driven sensing capabilities. Additionally, to address decoding impairments caused by these perturbations, we propose a closed-loop reception algorithm that progressively removes residual disturbances while maintaining decoding accuracy. Simulations confirm the algorithm’s effectiveness in balancing communication and sensing performance. Compared to current time-division processing technologies, such as 5G frame structure perception based on reference signals, the proposed waveforms more effectively resolves the trade-off between communication and sensing.

## Service-Driven Physical Layer Function Orchestration Algorithm Based on Meta-Reinforcement Learning

- **Status**: ❌
- **Reason**: 메타-RL 물리계층 함수 오케스트레이션; 채널코딩은 구성요소로만 언급, 떼어낼 LDPC 기법 없음
- **ID**: ieee:11310285
- **Type**: conference
- **Published**: 19-22 Oct.
- **Authors**: Jiajia Liao, Luping Xiang, Chao Tong +1
- **PDF**: https://ieeexplore.ieee.org/document/11310285
- **Abstract**: The diverse services offered by 5G and future 6G pose challenges to the rapid adaptability of the communication physical layer, which demand quick responsiveness and dynamic orchestration of physical layer functional components, but existing systems cannot fully support. Motivated by this context, this paper proposes a service-driven physical layer function orchestration algorithm. Firstly, an integrated physical layer function library is established. Secondly, multi-dimensional metrics, including the achievable rate, reliability and complexity, are introduced to evaluate the system performance, based on the function library, reflecting the varying requirements of different services. Subsequently, a meta-reinforcement learning algorithm is designed, which adaptively optimizes the orchestration of channel coding, modulation, and beamforming, to jointly optimize multidimensional metrics. Finally, simulation results demonstrate that the proposed algorithm achieves a 50% improvement in convergence rate and a 10% increase in training reward compared to baseline algorithms.

## Phase Noise and Residual CFO Compensation in 5G NR LEO Satellite OFDMA Uplinks

- **Status**: ❌
- **Reason**: 5G LEO 위성 위상잡음/CFO 보상; ECC·LDPC 기법 전혀 없음
- **ID**: ieee:11310189
- **Type**: conference
- **Published**: 19-22 Oct.
- **Authors**: Tzu-Hsien Sang, Chun-Chieh Chao, Li-Gang Chen +1
- **PDF**: https://ieeexplore.ieee.org/document/11310189
- **Abstract**: Low Earth orbit (LEO) satellites is regarded as a promising solution for supporting Non-Terrestrial Network (NTN); for instance, third Generation Partnership Project (3GPP) includes LEO satelites in 5G New Radio (NR). In the LEO-enabling NTN scenario, a distinct issue is the receivers’ impairments caused by different sources of phase variations, mainly phase noise (PN) and Doppler effects. Current compensation methods are challenging to implement in Orthogonal Frequency-Division Multiple-Access (OFDMA) systems due to the high overhead of pilots required. This paper proposes a technique that can work with very low overhead of reference signals and jointly compensate the effects of PN and residual Carrier Frequency Offset. Key factors to achieve effective compensation are also identified, and significant improvement in system performance is demonstrated in simulations.

## Uniform Random EP Allocation for FFMA Systems over Rayleigh Fading Channels

- **Status**: ❌
- **Reason**: FFMA 유한체 다중접속·Turbo-BMD 디코딩; LDPC 아님, 다중화/유한체 기법으로 이식 가능 바이너리 LDPC 기여 없음
- **ID**: ieee:11309855
- **Type**: conference
- **Published**: 19-22 Oct.
- **Authors**: Hao-Jun Sun, Qi-Yue Yu
- **PDF**: https://ieeexplore.ieee.org/document/11309855
- **Abstract**: The finite-field multiple-access (FFMA) technique reverses the order of channel coding and multiplexing, thereby enhancing the error performance of multiuser transmission, which is particularly promising for next-generation communication systems. In an FFMA system, element-pairs (EPs) serve as virtual resources. Previous studies on FFMA systems focused on assigning a single EP to each bit. In this paper, we investigate the case where multiple EPs are assigned to each bit, with the EPs selected from the orthogonal EP set Ψo,B. We propose a uniform random EP allocation scheme (UR-EPA), in which each bit is assigned an identical number of EPs with a randomized assignment feature. We prove that the orthogonal EPs assigned by the UR-EPA scheme satisfy the unique sum-pattern mapping (USPM) constraint. Under this scheme, the orthogonal EP code Ψo,B transforms into a single codeword EP code (S-CWEP), effectively forming an interleave-division multiple-access system in the finite-field domain (FF-IDMA). Furthermore, we propose a Turbo bifurcated minimum distance (Turbo-BMD) decoding algorithm for decoding multiuser signals. Simulation results show that, with 100 users and an average BER of 10−5, the FF-IDMA system achieves approximately 1.2 dB of coding gain compared to the classical IDMA system.

## AI-Assisted End-to-End Video Transmission with cGAN for 6G E-MIMO Systems

- **Status**: ❌
- **Reason**: 6G 영상 전송용 신경망 JSCC, LDPC는 H.264+LDPC 베이스라인일 뿐 떼어낼 ECC 기법 없음 (JSCC 제외)
- **ID**: ieee:11310753
- **Type**: conference
- **Published**: 19-22 Oct.
- **Authors**: Xinran Ren, Lihua Li
- **PDF**: https://ieeexplore.ieee.org/document/11310753
- **Abstract**: We propose a novel two-stage deep learning-based joint source-channel coding (JSCC) framework for robust video transmission over time-varying wireless channels. Unlike traditional separation-based schemes prone to the cliff effect, our method jointly optimizes video compression and error correction via end-to-end neural networks. The transmitter and receiver are first pre-trained under AWGN to establish a stable baseline. Subsequently, a conditional GAN (cGAN)-based equalizer is introduced at the receiver side to adaptively mitigate unknown fading effects without requiring explicit channel state information (CSI). The framework is validated in practical multi-antenna wireless environments, demonstrating strong compatibility with modern communication systems. Additionally, a quality-aware loss function balances pixel fidelity and perceptual video quality. Experimental results show that our approach outperforms conventional H.264+LDPC baselines, achieving up to 4.2 dB PSNR gain under fast-fading channels.

## A Low Complexity C-Transform Based OFDM with LDPC Codes

- **Status**: ❌
- **Reason**: VLC OFDM + LDPC(SPA/MSA 표준 디코더) - 표준 min-sum/SPA 단순 사용, 새 LDPC 기여 없음, 통신 응용 특이적
- **ID**: ieee:11374148
- **Type**: conference
- **Published**: 16-18 Oct.
- **Authors**: Tongqi Sun, Martin Johnston, Jummah Abdulwali
- **PDF**: https://ieeexplore.ieee.org/document/11374148
- **Abstract**: This paper investigates a nonlinear visible light communication (VLC) system incorporating two orthogonal frequency division multiplexing (OFDM) variants: discrete cosine transform-based OFDM (F-OFDM) and a proposed C-transform-based OFDM (C-OFDM), each combined with low-density parity-check (LDPC) error correction coding. To over-come the challenges imposed by LED nonlinearity, high peak-to-average power ratio (PAPR), and real-valued signal requirements of VLC systems, the C-OFDM system leverages the benefits of both Discrete Cosine Transform (DCT) and Walsh-Hadamard Transform (WHT). Furthermore, two decoding strategies, namely the Sum-Product Algorithm (SPA) and the Min-Sum Algorithm (MSA), are analysed in depth. Simulation results under varying nonlinear LED operating conditions demonstrate that C-OFDM consistently outperforms F-OFDM in terms of BER, especially in high signal-to-noise ratio (SNR) regimes. The proposed approach provides a computationally efficient and distortion-resilient solution for practical VLC deployment.

## A Wireless Capsule Endoscopy SoC and Recorder System Supporting 1080p, 12FPS and 720p, 24FPS Image Transmission

- **Status**: ❌
- **Reason**: 캡슐내시경 SoC, LDPC 인코더/디코더 언급뿐 새 코드설계/디코더 기여 없는 통신 응용 특이적
- **ID**: ieee:11327949
- **Type**: conference
- **Published**: 16-18 Oct.
- **Authors**: Huimin Guo, Yat Tung Lai, Jianhui Wang
- **PDF**: https://ieeexplore.ieee.org/document/11327949
- **Abstract**: This paper introduces a low-power asymmetrical 4FSK/OOK system-on-a-chip (SoC), designed for high speed high resolution image transmission in next generation wireless capsule endoscopy. The proposed asymmetrical chip and system enables high speed image transmission from capsule to image recorder via 4-frequency shift keying (4FSK) modulation, and simple control command transmission via on-off keying (OOK) modulation from image recorder to capsule. The SoC is fabricated in 40 nm CMOS technology with die area of $11.4 \mathrm{~mm}^{2}$. The SoC operates at $\mathbf{4 0 7 ~ M H z}-\mathbf{4 4 0 ~ M H z}$ and the transmitter (TX) outputs maximum 5 dBm power with a power consumption of 77.8 mW, achieving a raw data rate of 19.2 Mbps. Meanwhile, the OOK receiver (RX) achieves - 85 dBm sensitivity with 1% bit error rate (BER) with a power consumption of 20.8 mW and a data rate of 200 kbps. With proposed low density parity check (LPDC) low complexity encoder and high throughput decoder, the SoC and image recorder system are capable of transmitting $1080 \times 1080$ images at a frame rate of 12 frames per second (FPS) and 720x720 images at 24 FPS from capsule to image recorder.

## Performance Analysis of Coded MIMO Systems Using Superposition 64-Ary Constellation with Protograph LDPC and Low-Resolution ADCs

- **Status**: ❌
- **Reason**: MIMO + 저해상도 ADC용 P-LDPC 결합/PEXIT 분석 - 무선 검출-디코딩 결합 특이적, 떼어낼 NAND용 LDPC 기법 없음
- **ID**: ieee:11268568
- **Type**: conference
- **Published**: 16-18 Oct.
- **Authors**: Thang Le Nhat, Duc A. Hoang
- **PDF**: https://ieeexplore.ieee.org/document/11268568
- **Abstract**: This paper introduces a new coded modulation framework for massive MIMO systems that leverages low-resolution analog-to-digital converters (ADCs) alongside superposition-based 64-ary QAM modulation to increase spectral utilization efficiency. To address the complexity of signal detection, the proposed approach reformulates the original 64-ary QAM channel into an equivalent BPSK model. This reformulation supports a two-layer Tanner graph structure for the combined tasks of signal detection and channel decoding, with computational complexity that grows quadratically with the number of transmit antennas. Protograph LDPC (P-LDPC) codes are adopted in the system due to their excellent error correction performance, and integrates an "equal-weight" superposition constellation, which delivers a 0.7–1 dB gain in performance compared to the traditional "equal-distance" design under coarse quantization. Furthermore, the paper introduces a modified PEXIT analysis method that holistically accounts for the combined effects of MIMO fading, quantization noise from ADCs, and LDPC decoding characteristics. Simulation results confirm the reliability of the analytical approach and highlight the critical role of optimized power allocation in maintaining high energy and spectral efficiency in emerging 5G and 6G networks utilizing low-resolution receivers.

## Tomlinson Harashima Precoding Design for OTFS System

- **Status**: ❌
- **Reason**: OTFS THP 프리코딩 + soft detection - 무선 채널 프리코딩 특이적, LDPC 베이스라인, 떼어낼 ECC 기법 없음
- **ID**: ieee:11374043
- **Type**: conference
- **Published**: 16-18 Oct.
- **Authors**: Yonghua Liu, Tao Yang, Rongke Liu
- **PDF**: https://ieeexplore.ieee.org/document/11374043
- **Abstract**: An orthogonal time frequency space (OTFS) scheme that operates in the delay-Doppler (DD) domain has competitive performance in high-mobility wireless environments. However, its complexity for tackling the interferences among the DD grids remains too high for many practical applications. In this paper, we study a DD-domain Tomlinson-Harashima precoding (THP) approach for OTFS system. First, a new DD-domain selective zero-padding (SZP) scheme is developed, which addresses the non-causality of the time-frequency doubly-selective channel (DSC) matrix is introduced. Based on that, THP that pre-cancels the DD domain interference on a symbol-by-symbol basis is carried out, where the requirement of large matrix inversion is avoided. Further, we derive the exact a posteriori probability (APP) for optimal soft detection in the THP-OTFS system with state-of-the art channel codes. Numerical results demonstrate that our proposed THP-OTFS scheme brings up to 5 dB improvement in complex multipath scenario over the benchmark system operated with linear precoding. For channel-coded THP-OTFS system, our developed optimal soft detection brings about 2 dB improvement over exisiting THP method.

## The Approximate Universality of LTE-Turbo, NR-LDPC, and SC-LDPC Codes

- **Status**: ❌
- **Reason**: LTE-Turbo/NR-LDPC/SC-LDPC의 근사 보편성 분석 — 표준 부호 성능평가 이론, 새 디코더/구성/HW로 안 이어짐
- **ID**: ieee:11253847
- **Type**: conference
- **Published**: 16-17 Oct.
- **Authors**: Xiaohan Zhou, Kewu Peng, Dmitry A. Tkachenko +3
- **PDF**: https://ieeexplore.ieee.org/document/11253847
- **Abstract**: Bit-Interleaved Coded Modulation with Orthogonal Frequency Division Multiplexing (BICM-OFDM) is a key scheme for physical layer transmission in broadcasting and communication systems. Its performance evaluation is computationally demanding due to diverse channel coding, fading, and modulation choices. To facilitate the performance evaluation and system design, average mutual information has been proposed as a transfer parameter to help decouple the whole physical layer link-level system into channel coding subsystem and bit-wise equivalent channel subsystem, yet the universality of coding schemes-essential to validate the decoupling-remains underexplored. This paper addresses the approximate universality of LTE-Turbo, NR-LDPC, and SC-LDPC codes via link-level simulations. A capacity loss factor is introduced as the key performance index to evaluate the approximate universality. Results demonstrate that all three codes exhibit approximate universality, providing practical guidance for efficient BICM-OFDM system design and performance evaluation.

## Beyond DVB-S2X: Optimal Signals for High-Throughput CubeSat Communications

- **Status**: ❌
- **Reason**: CubeSat용 FTN/펄스파형 최적화 — LDPC 언급 없는 신호설계, ECC 기법 없음
- **ID**: ieee:11252458
- **Type**: conference
- **Published**: 16-17 Oct.
- **Authors**: Sergey Zavjalov, Anna Orlova, Ilya Lavrenyuk +3
- **PDF**: https://ieeexplore.ieee.org/document/11252458
- **Abstract**: This paper addresses the critical challenge of enhancing data throughput in CubeSat communication systems, which are limited by possible onboard power. The study proposes a novel solution for DVB-S2X standard by replacing the conventional Root-Raised Cosine (RRC) pulses with optimal signals with joint application of Faster-Than-Nyquist (FTN) signaling. The synthesized optimal signals are designed to minimize out-of-band emissions under restrictions on BER performance taking into account characteristics of APSK modulations used in DVB-S2X. A digital test bench was developed to simulate a CubeSat downlink scenario, comparing the bit error rate (BER) performance of the proposed optimal signals against traditional RRC pulses at increased symbol rates. The optimal signals can provide double symbol rate (from 1/T to 2/T) with energy loss equal to 0.05 dB for QPSK and 0.55 dB for 64APSK compared to a standard RRC signals without increased symbol rate. This result leads to potential downlink data rates of up to 2.4 Gbps in a 500 MHz band, making highthroughput CubeSat communications feasible under strict power budgets. The research concludes that optimal signals are a potent method for drastically increasing the data rate of DVB-S2X-based CubeSat modems without a proportional increase in transmitter power.

## Single Station Large-scale Coverage Scheme and Field Testing of DTMB-A at Islamabad

- **Status**: ❌
- **Reason**: DTMB-A 디지털TV 단일국 커버리지 현장시험 — 네트워크 배치 사례, LDPC/ECC 기법 없음
- **ID**: ieee:11252459
- **Type**: conference
- **Published**: 16-17 Oct.
- **Authors**: Lu Tong, Ke Mao, Haidong Fang +3
- **PDF**: https://ieeexplore.ieee.org/document/11252459
- **Abstract**: At the beginning of 2024, China-Aided Project of DTMB-A in Pakistan was completed and handed over. The main components of the construction of the Pakistan Digital Television Project include establishing three independent ground digital television trial networks in Islamabad and surrounding areas. In the paper, the scheme and transmission parameters of DTMB-A network coverage in Pakistan Islamabad and the surrounding area were proposed. Each site uses the independent front-end system with multi frequency network coverage and it is the typical case for the oversea application of DTMB-A standard. The design of the Pakistan digital TV coverage integrates both fixed reception and mobile reception, with the goal of ensuring extensive coverage from a single station. After the completion of this project, a large number of fixed and mobile site tests were conducted. The test results show that DTMB-A single site coverage can not only achieve ultra large area coverage, but also take into account the mobile reception in major areas.

## Implementation of a Quaternary Message Passing Low-Density Parity-Check Decoder

- **Status**: ❌
- **Reason**: Quaternary(4진) 메시지 패싱 LDPC 디코더 — 비이진 LDPC이므로 즉시 제외
- **ID**: ieee:11330135
- **Type**: conference
- **Published**: 15-18 Oct.
- **Authors**: Oliver Griebel, Alexander Sauter, Gianluigi Liva +1
- **PDF**: https://ieeexplore.ieee.org/document/11330135
- **Abstract**: We present a hardware implementation and evaluation of a quaternary message-passing (QMP) low-density parity-check (LDPC) decoder. The design targets high-throughput applications, where routing complexity and energy efficiency are large challenges from an implementation perspective. A comparison of the QMP decoder to a state-of-the-art normalized min-sum (NMS) decoder using a 12 nm fin field-effect transistor (FinFET) technology node shows that the QMP decoder achieves a 14.1 % increase in throughput and a 178.5 % improvement in energy efficiency. However, this is at the cost of a 0.35 dB loss in error correction performance.

## Latency Analysis of LDPC Kernel Launch Modes in cuPHY PUSCH Multi-Pipe Processing

- **Status**: ❌
- **Reason**: cuPHY GPU 커널 런치 모드 지연 분석, 디코더 알고리즘/구성 새 기여 없는 운영 가이드
- **ID**: ieee:11388876
- **Type**: conference
- **Published**: 14-17 Oct.
- **Authors**: Hyebin Cho, Jee-Hyeon Na, Nam-I Kim
- **PDF**: https://ieeexplore.ieee.org/document/11388876
- **Abstract**: Low-density parity-check (LDPC) decoding is a key component in physical uplink shared channel (PUSCH) reception of modern wireless systems, and its processing latency directly affects end-to-end performance. In this paper, we compare and analyze the latency characteristics of different LDPC decoding modes for PUSCH reception within the NVIDIA cuBB SDK 24-1 environment. The performance of each mode is evaluated under both single and multiple transport block scenarios, with various traffic conditions, to identify the optimal LDPC decoding mode for different situations. Based on these results, this paper provides practical guidelines for selecting the appropriate LDPC processing modes for future 5G/6G networks that require ultra-low-latency services.

## On the Performance of Channel Coding in Digital Semantic Communication

- **Status**: ❌
- **Reason**: 시맨틱 통신에서 LDPC는 베이스라인 비교 대상, 떼어낼 새 ECC 기법 없음
- **ID**: ieee:11389065
- **Type**: conference
- **Published**: 14-17 Oct.
- **Authors**: Seonjung Kim, Yo-Seb Jeon
- **PDF**: https://ieeexplore.ieee.org/document/11389065
- **Abstract**: Semantic communication aims to transmit task-relevant meaning, not just raw data. This paper evaluates the performance of repetition, polar, and low-density parity-check (LDPC) codes in a digital semantic communication system. The probabilities are obtained via end-to-end training with a fixed bitflip probability. Experiments on image transmission over additive white Gaussian noise channels show that the trade-off between image reconstruction quality and energy efficiency is controlled by the bit-flip probability.

## On the Impact of Training Mismatch in Deep-Learning-Based Channel Denoising

- **Status**: ❌
- **Reason**: DL 기반 채널 추정 denoising, LDPC ECC 기법 없음
- **ID**: ieee:11388143
- **Type**: conference
- **Published**: 14-17 Oct.
- **Authors**: Sungyoung Ha, Yo-Seb Jeon
- **PDF**: https://ieeexplore.ieee.org/document/11388143
- **Abstract**: To further improve the accuracy of channel estimation in multiple-input multiple-output orthogonal frequency-division multiplexing (MIMO-OFDM) systems, we study deep-learning (DL)-based channel denoising. We train a denoising neural network offline on simulated realizations from a single baseline channel scenario and evaluate the pre-trained model—without adaptation—across multiple online deployment environments. When the deployment environment aligns with the training scenario, the denoiser provides the strongest gains; however, under distribution shift (e.g., differing delay/Doppler characteristics or signal-to-noise ratio regimes), estimation accuracy degrades, revealing limited cross-scenario generalization. These findings highlight the sensitivity of DL-based denoising to channel mismatch and motivate further investigation into online robustness to sustain performance in dynamic wireless settings.

## Evaluation of Interleaving-based PLS Scheme for Satellite Communications

- **Status**: ❌
- **Reason**: 물리계층 보안(인터리빙 PLS), 채널코딩 ECC 기법 아님
- **ID**: ieee:11388871
- **Type**: conference
- **Published**: 14-17 Oct.
- **Authors**: Thara Son, Sooyoung Kim
- **PDF**: https://ieeexplore.ieee.org/document/11388871
- **Abstract**: Physical layer security (PLS) schemes exploit the randomness and unpredictability of a wireless channel to establish secure communication links, and they can be considered as one of the effective techniques to provide security protection. On the other hand, satellite systems have difficulties of fully exploiting randomness and often have consistent spatial channel characteristics due to a long round trip delay and wide coverage areas, which make it difficult to apply the same PLS techniques developed originally for the terrestrial systems. This paper first reviews several PLS techniques developed for multi-antenna systems and evaluates their applicability to satellite systems, particularly dynamic interleaving-based PLS techniques. The results presented in this paper reveal that the examined PLS scheme effectively degrades the eavesdropper’s decoding capability under dynamically changing satellite channel conditions.

## Impact of Number of DMRS Symbols on Self-interference Cancellation in Full-duplex Mobile Communications

- **Status**: ❌
- **Reason**: 전이중 자기간섭 제거/DMRS 채널추정, LDPC ECC 무관
- **ID**: ieee:11388177
- **Type**: conference
- **Published**: 14-17 Oct.
- **Authors**: Kazuma Matsushima, Takatoshi Sugiyama
- **PDF**: https://ieeexplore.ieee.org/document/11388177
- **Abstract**: Full-duplex mobile communication, which allows bidirectional transmission and reception over the same frequency band, offers doubled spectral efficiency compared with duplexing methods, such as frequency division duplex (FDD) and time division duplex (TDD). This technique is gaining attention as an access method for mobile communication systems between base station (BS) and user equipment (UE). Self-interference (SI) which occurs between the transmitter (TX) and receiver (RX) of BS must be eliminated to achieve full-duplex mobile communication. We have been investigating a transmission performance of QAM-OFDM signals when applying an adaptive self-interference canceller (SIC) based on channel estimation using demodulation reference signal (DMRS) in full-duplex mobile communication environments. This paper investigates BER performances of QAM-OFDM signals under full-duplex environments where SI channel fluctuates over time. Specifically, the BERs are demonstrated as parameters of number of DMRS symbols per resource block. The simulation results verify that increasing the number of DMRS symbols can achieve the better BER performance under the time-varying self-interference conditions.

## From Shelf to Space: A Practical Evaluation of Radiation Hardness of COTS NVMe SSDs

- **Status**: ❌
- **Reason**: COTS NVMe SSD 방사선 내성 평가 — NAND 디바이스 물리 신뢰성 연구로 LDPC ECC 기법 기여 없음
- **ID**: ieee:11326196
- **Type**: conference
- **Published**: 13-17 Oct.
- **Authors**: Mathieu Erbas
- **PDF**: https://ieeexplore.ieee.org/document/11326196
- **Abstract**: Commercial off-the-shelf (COTS) NVMe solid-state drives (SSDs) present a compelling solution for high-density data storage in space, but their radiation tolerance is highly variable and poorly understood. This paper evaluates six industrial-grade COTS NVMe SSDs with diverse architectures under total ionizing dose (TID) and single-event effect (SEE) radiation. Active, in-situ testing was performed using a 60Co source for TID and a 200 MeV proton beam for SEE. The results reveal a significant lack of correlation between TID and SEE performance. TID tolerance varied by over 4×, with failure doses ranging from 7 krad(Si) to over 33.6 krad(Si); two DRAM-less models survived the full irradiation. SEE susceptibility spanned nearly two orders of magnitude, with failure fluences from 1.5×109 to over 1×1011 p/cm2. Notably, a pseudo-single-level cell (pSLC) device demonstrated superior SEE resilience, surviving to the test limit of 1×1011 p/cm2 without failure. The primary failure mode for TID was permanent loss of enumeration, while for SEE it was unrecoverable single-event functional interrupts (SEFIs). These findings indicate that controller architecture and NAND configuration are the dominant factors in radiation hardness, rather than the presence of DRAM cache alone. While the limited sample size (n=1 per model) precludes statistical conclusions, this work establishes a critical baseline for COTS SSD selection and underscores the necessity of device-specific radiation screening for space applications.

## CEC-LoRa: A Codeless Error Correction Method for Corrupted LoRa Packet Decoding

- **Status**: ❌
- **Reason**: LoRa 코드리스 오류정정 — 칩 변조 특성 기반 패킷 복원, ECC를 아예 안 쓰는 방식으로 이식 기법 없음
- **ID**: ieee:11146374
- **Type**: conference
- **Published**: 13-16 Oct.
- **Authors**: Daniel Szafranski, Andreas Reinhardt
- **PDF**: https://ieeexplore.ieee.org/document/11146374
- **Abstract**: For various wireless sensing and IoT applications, LoRa has emerged as an energy-efficient and long range solution for wireless data transfers. However, real-world deployments face multiple challenges, including packet collisions and variable link qualities, which generally lead to packet corruptions and data loss. Even though LoRa relies on forward error correction to restore corrupted packets, its usage comes with a significant energy overhead and only provides limited capabilities. In our paper, we present CEC-LoRa as an alternative to LoRa’s forward error correction feature. Its key innovation is that CEC-LoRa allows to restore corrupted packets without any error correction codes. Our approach exploits two symbiotic properties in LoRa’s encoding and chirp-based modulation scheme. On the one hand, misinterpreted chirps are often confused with neighboring symbols. On the other hand, neighboring symbol values only differ by one, keeping high similarity between misinterpreted and correct symbols. We leverage these properties by pre-computing a set of all plausible LoRa packets based on the expected payload permutations and compare them with the received packet. This allows us to identify the closest match and thus the most probable candidate packet. While the pre-computations incur a quite substantial energy overhead, CEC-LoRa shifts this from the energy-constrained end devices to the receiver side. The benefits greatly outweigh the energy demand, though: CEC-LoRa reduces the number of corrupted packets by 86.5 % on average without any additional overhead on the end device and while still being fully compliant to the LoRa specification. By including symbol information, CEC-LoRa can reduce the number of corrupt packets even further, by 99.5 % on average. This translates into SNR gains in the range of 0.79 dB to 0.93 dB.

## Using Data Redundancy Techniques to Detect and Correct Errors in Logical Data

- **Status**: ❌
- **Reason**: RAID 기반 논리 데이터 중복/복구 소프트웨어; LDPC ECC 기법 없음
- **ID**: ieee:11428699
- **Type**: conference
- **Published**: 1-2 Oct. 2
- **Authors**: Ahmed Sharuvan, Ahmed Naufal Abdul Hadee
- **PDF**: https://ieeexplore.ieee.org/document/11428699
- **Abstract**: Data redundancy techniques have been tested in several different applications to provide fault tolerance and performance gains. The use of these techniques is mostly seen at the hardware, device driver, or file system level. In practice, the use of data integrity techniques with logical data has largely been limited to verifying the integrity of transferred files using cryptographic hashes. In this paper, we study the RAID scheme used with disk arrays and adapt it for use with logical data. An implementation for such a system is devised in theory and implemented in software, providing the specifications for the procedures and file formats used. Rigorous experimentation is conducted to test the effectiveness of the developed system for multiple use cases. With computer-generated benchmarks and simulated experiments, the system demonstrates robust performance in recovering arbitrary faults in large archive files only using a small fraction of redundant data. This was achieved by leveraging computing power for the process of data recovery.
