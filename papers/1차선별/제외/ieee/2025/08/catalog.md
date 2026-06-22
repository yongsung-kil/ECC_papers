# IEEE Xplore — 2025-08


## A PEXIT Analysis of Belief Propagation Polar Decoder with Approximated LLR

- **Status**: ❌
- **Reason**: Polar 코드 BP 디코더 LLR 근사 PEXIT 분석, LDPC 무관
- **ID**: ieee:11062680
- **Type**: journal
- **Published**: August 202
- **Authors**: Shuhei Yamaguchi, Yuta Hori, Takahiko Nakamura +1
- **PDF**: https://ieeexplore.ieee.org/document/11062680
- **Abstract**: Belief propagation decoding of Polar codes suffers from performance degradation if the frozen bits are not appropriately allocated. Particularly, when simplified log-likelihood ratio (LLR) calculations are used to reduce hardware complexity, the conventional frozen bit allocation based on protograph extrinsic information transfer (PEXIT) analysis becomes ineffective due to the inaccurate EXIT function. In this paper, we propose a new EXIT function that takes into account the approximation in the LLR for PEXIT analysis. Simulation results show that PEXIT analysis with the proposed EXIT function is able to represent the degradation of bit error rate (BER) due to the LLR approximation.

## AG Codes Achieve List-Decoding Capacity Over Constant-Sized Fields

- **Status**: ❌
- **Reason**: AG 코드의 리스트 디코딩 용량 달성에 관한 순수 이론 논문 — LDPC와 무관하며 디코더/HW/구성으로 이어지지 않는 순수 이론적 bound 연구
- **ID**: ieee:11027159
- **Type**: journal
- **Published**: Aug. 2025
- **Authors**: Joshua Brakensiek, Manik Dhar, Sivakanth Gopi +1
- **PDF**: https://ieeexplore.ieee.org/document/11027159
- **Abstract**: The recently-emerging field of higher order MDS codes has sought to unify a number of concepts in coding theory. Such areas captured by higher order MDS codes include maximally recoverable (MR) tensor codes, codes with optimal list-decoding guarantees, and codes with constrained generator matrices (as in the GM-MDS theorem). By proving these equivalences, Brakensiek et al. (2024) showed the existence of optimally list-decodable Reed-Solomon codes over exponential sized fields. Building on this, recent breakthroughs by Guo and Zhang (2023) and Alrabiah et al. (2024) have shown that randomly punctured Reed-Solomon codes achieve list-decoding capacity (which is a relaxation of optimal list-decodability) over linear size fields. We extend these works by developing a formal theory of relaxed higher order MDS codes. In particular, we show that there are two inequivalent relaxations which we call lower and upper relaxations. The lower relaxation is equivalent to relaxed optimal list-decodable codes and the upper relaxation is equivalent to relaxed MR tensor codes with a single parity check per column. We then generalize the techniques of Guo-Zhang and Alrabiah-Guruswami-Li to show that both these relaxations can be constructed by randomly puncturing suitable algebraic-geometric codes over constant size fields. For this, we crucially use the generalized GM-MDS theorem for polynomial codes recently proved by Brakensiek et al. (2024). We obtain the following corollaries from our main result: 1) randomly punctured algebraic-geometric codes of rate R are list-decodable up to radius  $\frac {L}{L+1}(1-R-\epsilon)$  with list size L over fields of size  $\exp (O(L/\epsilon))$ . In particular, they achieve list-decoding capacity with list size  $O(1/\epsilon)$  and field size  $\exp (O(1/\epsilon ^{2}))$ . Prior to this work, AG codes were not even known to achieve list-decoding capacity; and 2) by randomly puncturing algebraic-geometric codes, we can construct relaxed MR tensor codes with a single parity check per column over constant-sized fields, whereas (non-relaxed) MR tensor codes require exponential field size.

## OTFS-Based CV-QKD Systems for Doubly Selective THz Channels

- **Status**: ❌
- **Reason**: CV-QKD 시스템 논문으로 LDPC는 양자 키 조정(reconciliation)의 보조 수단으로 사용됨 — 떼어낼 수 있는 LDPC 코드 설계/디코더/HW 기법이 없으며 QKD·보안 도메인 특이적
- **ID**: ieee:10857395
- **Type**: journal
- **Published**: Aug. 2025
- **Authors**: Xin Liu, Chao Xu, Soon Xin Ng +1
- **PDF**: https://ieeexplore.ieee.org/document/10857395
- **Abstract**: The feasibility of continuous variable quantum key distribution (CV-QKD) is considered in the Terahertz (THz) band, experiencing time-varying and frequency-selective fading. Advanced multi-carrier modulation is required for improving the secret key rate (SKR). However, the hostile quantum channel requires powerful classical channel coding schemes for maintaining an adequate reconciliation performance. Against this background, for the first time in the open literature, we propose a multi-carrier quantum transmission regime that incorporates both orthogonal frequency division multiplexing (OFDM) and orthogonal time frequency space (OTFS) transmission over doubly selective fading THz channels. Furthermore, we propose a modified multi-dimensional reconciliation algorithm for CV-QKD, facilitating the integration of OFDM/OTFS quantum transmission with low-density parity check (LDPC) coded key reconciliation. Moreover, we harness multiple-input multiple-output (MIMO) beamforming for mitigating the severe THz path loss. Our SKR analysis results demonstrate that the proposed OTFS-based and LDPC-assisted CV-QKD system is capable of outperforming its OFDM counterpart in mobile wireless scenarios. Moreover, we also demonstrate that increasing the MIMO dimension reduces the transmission power required for achieving the secure transmission distance target.

## Parallel Coding for Orthogonal Delay-Doppler Division Multiplexing

- **Status**: ❌
- **Reason**: ODDM 변조용 병렬 채널 부호화 전송 전략 논문 — LDPC 특정 기법 없이 무선 다중 캐리어 시스템 특이적이며 NAND ECC에 이식 가능한 기법 없음
- **ID**: ieee:10872973
- **Type**: journal
- **Published**: Aug. 2025
- **Authors**: Qi Li, Jinhong Yuan, Min Qiu
- **PDF**: https://ieeexplore.ieee.org/document/10872973
- **Abstract**: This paper proposes a novel parallel coding transmission strategy and an iterative detection and decoding receiver signal processing technique for orthogonal delay-Doppler division multiplexing (ODDM) modulation. Specifically, the proposed approach employs a parallel channel encoding (PCE) scheme that consists of multiple short-length codewords for each delay-Doppler multicarrier (DDMC) symbol. Building upon such a PCE transmission framework, we then introduce an iterative detection and decoding algorithm incorporating a successive decoding feedback (SDF) technique, which enables instant information exchange between the detector and decoder for each DDMC symbol. To characterize the error performance of the proposed scheme, we perform density evolution analysis considering the finite blocklength effects. Our analysis results, coupled with extensive simulations, demonstrate that the proposed PCE scheme with the SDF algorithm not only showcases a better overall performance but also requires much less decoding complexity to implement, compared to the conventional benchmark scheme that relies on a single long channel code for coding the entire ODDM frame.

## On the Application of Expectation Propagation to Symbol Detection in Phase Noise Channels

- **Status**: ❌
- **Reason**: Expectation Propagation 기반 위상 잡음 채널 심볼 검출 논문 — LDPC 언급 없고 무선 채널 수신기 특이적 알고리즘이며 NAND LDPC ECC에 이식 가능한 디코더/HW/코드설계 기법 없음
- **ID**: ieee:10872962
- **Type**: journal
- **Published**: Aug. 2025
- **Authors**: Elisa Conti, Armando Vannucci, Amina Piemontese +1
- **PDF**: https://ieeexplore.ieee.org/document/10872962
- **Abstract**: In the context of signal detection in the presence of an unknown time-varying channel parameter, receivers based on the Expectation Propagation (EP) framework appear to be very promising. EP is a message-passing algorithm based on factor graphs with an inherent ability to combine prior knowledge of system variables with channel observations. This suggests that an effective estimation of random channel parameters can be achieved even with a very limited number of pilot symbols, thus increasing the payload efficiency. However, achieving satisfactory performance often requires ad-hoc adjustments in the way the probability distributions of latent variables - both data and channel parameters - are combined and projected. Here, we provide, for the first time, an analysis of EP-based algorithms for the classical problem of coded transmission on a strong Wiener phase noise channel, employing soft-input soft-output decoding. The analysis includes possible improvements over the native application of EP, in order to identify its limitations and propose new strategies which reach the performance benchmark while maintaining low complexity, with a primary focus on challenging scenarios where the state-of-the-art algorithms fail.

## Polarization-Aided Multi-User Spatial Modulation

- **Status**: ❌
- **Reason**: Polar 코드 기반 다중 사용자 공간 변조 논문 — LDPC와 무관하며 무선 통신 특이적으로 NAND LDPC ECC에 이식 가능한 기법 없음
- **ID**: ieee:10935742
- **Type**: journal
- **Published**: Aug. 2025
- **Authors**: Zhaopeng Xie, Yuanping Wang, Yuehui Xu +2
- **PDF**: https://ieeexplore.ieee.org/document/10935742
- **Abstract**: In this paper, we propose a polarization-aided detection and decoding scheme for polar-coded multi-user spatial modulation (PA-MU-SM) systems. Exploiting the polar code structure, we treat the reception processing in MU-SM as a polar re-encoding that generates an extended-length polar code with nested user codes. The proposed method enables us to decode all user messages within this single polar decoder. Then, a Monte-Carlo construction is utilized to optimize the nested user codes of the extended-length polar code. Furthermore, to eliminate the interference between user layers of the PA-MU-SM, an iterative polarization-aided (I-PA) scheme is designed and can theoretically achieve MU-SM channel capacity via a four-stage channel transform. Simulation results show that the proposed PA and I-PA schemes offer better error performance than the traditional polar-coded spatial modulation (PC-SM) schemes.

## AUTHFi: Cross-Technology Device Authentication via Commodity WiFi

- **Status**: ❌
- **Reason**: WiFi 기반 IoT 기기 인증(AUTHFi) 논문 — ECC/LDPC와 무관하며 NAND 플래시 ECC에 이식 가능한 기법 없음
- **ID**: ieee:10908862
- **Type**: journal
- **Published**: Aug. 2025
- **Authors**: Weizheng Wang, Dusit Niyato, Zehui Xiong +1
- **PDF**: https://ieeexplore.ieee.org/document/10908862
- **Abstract**: The explosive growth of the Internet of Things (IoT) has dramatically increased the demand for secure mechanisms to protect against unauthorized access and attacks. Traditionally, expensive Software-Defined Radios (SDRs) have been utilized to gather IoT physical features, which are critical for reliable authentication. However, the high cost of SDRs makes them impractical for widespread deployment across the vast and diverse IoT ecosystem. In contrast, this paper presents AUTHFi, a novel cross-technology device authentication framework that transforms the SDR approach for collecting and authenticating IoT device signals (e.g., ZigBee and Bluetooth) by utilizing commercial WiFi devices. Specifically, AUTHFi leverages the recent advances in Cross-Technology Communication (CTC) to reconstruct the partial waveform of IoT transmission, thus eliminating the requirement for expensive SDRs. AUTHFi requires us to address several unique challenges. First, AUTHFi compensates for signal losses of the partial waveform to get more signal information. Then, it introduces an enhanced Carrier Frequency Offset (CFO) estimation and a fusion neural network that combines CFO and the reconstructed waveform for accurate device authentication. We implement AUTHFi based on RTL8812au (commodity WiFi) and CC2652P (commodity ZigBee/Bluetooth). Our thorough evaluation confirms that AUTHFi offers reliable authentication under various settings, achieving a maximum accuracy of 94.2%.

## Rényi Divergence Guarantees for Hashing With Linear Codes

- **Status**: ❌
- **Reason**: 소스에서 균일 랜덤 비트 추출(linear hashing)에 관한 정보이론 논문으로, 채널 코딩 ECC와 무관하며 NAND LDPC에 이식할 디코더·HW·코드설계 기법 없음.
- **ID**: ieee:11028607
- **Type**: journal
- **Published**: Aug. 2025
- **Authors**: Madhura Pathegama, Alexander Barg
- **PDF**: https://ieeexplore.ieee.org/document/11028607
- **Abstract**: We consider the problem of distilling uniform random bits from an unknown source with a given p-entropy using linear hashing. As our main result, we estimate the expected p-divergence between the hashed output and the uniform distribution over the ensemble of random linear codes for all integer  $p\ge 2$ . The proof relies on analyzing how additive noise, determined by a random element of the code from the ensemble, acts on the source distribution. This action leads to the transformation of the source distribution into an approximately uniform one, a process commonly referred to as distribution smoothing. We also show that hashing with Reed-Muller matrices reaches intrinsic randomness of memoryless Bernoulli sources in the  $l_{p}$  sense for all integer  $p\ge 2$ .

## A Practical Indexing Scheme for Noisy Shuffling Channels Using Cosets of Polar Codes

- **Status**: ❌
- **Reason**: DNA 저장소 노이즈 셔플링 채널용 Polar+RS 코드 연구, LDPC 무관
- **ID**: ieee:10769564
- **Type**: journal
- **Published**: Aug. 2025
- **Authors**: Javad Haghighat, Tolga M. Duman
- **PDF**: https://ieeexplore.ieee.org/document/10769564
- **Abstract**: The noisy shuffling channel models the conditions encountered in DNA storage systems, where transmitted data segments experience random permutation and substitution errors. Reliable communication over this channel requires effective indexing and channel coding strategies for segment order restoration and error correction. This paper introduces a concatenated coding approach for communication over the noisy shuffling channel using Reed-Solomon (RS) codes as outer codes and polar codes as inner codes. A coset-based indexing method, derived from polar codes, is proposed. A joint decoder is designed to detect the permutation pattern and perform polar decoding simultaneously. An upper bound on the frame error rate (FER) is derived when minimum distance decoding is employed for decoding. Also, an approximate analysis of the FER using random coding is conducted. A mapping between the cosets of the polar code and subsets of its frozen bits is established to design cosets achieving lower FERs compared to a commonly used explicit indexing method. Furthermore, a low-complexity decoding approach is devised, providing a trade-off between the computational complexity of the joint decoder and its performance.

## Mobility-Aware Decentralized Federated Learning for Autonomous Underwater Vehicles

- **Status**: ❌
- **Reason**: 수중 IoT용 분산 연합학습(DFL) 논문 — ECC/LDPC와 완전히 무관하며 NAND 플래시 ECC에 이식 가능한 기법 없음
- **ID**: ieee:10964078
- **Type**: journal
- **Published**: Aug. 2025
- **Authors**: Hongyi He, Jun Du, Chunxiao Jiang +3
- **PDF**: https://ieeexplore.ieee.org/document/10964078
- **Abstract**: The underwater Internet of Things (UIoT) is crucial in developing marine resources. However, due to the low data rate of underwater channels, it is difficult to have a central server to process data from numerous devices as using terrestrial communications. Therefore, decentralized federated learning (DFL) with communication-efficient modifications is a promising alternative to empower UIoT with artificial intelligence and collaborative training. However, existing DFL strategies rely on a carefully designed small aggregation weight when aggregating parameters from neighbor nodes to mitigate the compression error, resulting in a slow convergence rate. In addition, the effect of data compression under time-varying topologies is not considered in current DFL algorithms. In response to these problems, this work studies a DFL framework with underwater acoustic channel and time-varying topology. Firstly, considering the low data rate and dynamics of the acoustic channel, we propose a practical scheme for adaptive compression and device connectivity. Moreover, we combine data compression and the error-compensation technique with time-varying topology and propose a DFL algorithm with aggregation weights decaying over time to achieve fast convergence under non-independent and identically distributed (non-IID) data. We derive a convergence bound for the proposed algorithm with respect to compression and time-varying topology and demonstrate that it achieves the same asymptotic convergence rate as centralized FL with perfect communication. Simulation results show that the proposed algorithm exhibits higher accuracy and faster convergence rate in underwater environments compared with DFL algorithms without decaying aggregation weights and centralized FL schemes.

## Residual Cross-Attention Transformer-Based Multi-User CSI Feedback With Deep Joint Source-Channel Coding

- **Status**: ❌
- **Reason**: 대규모 MIMO용 CSI 피드백 딥러닝 프레임워크(DJSCC) — 소스-채널 결합 코딩 논문으로 LDPC는 언급 없으며 NAND ECC와 무관
- **ID**: ieee:11016076
- **Type**: journal
- **Published**: Aug. 2025
- **Authors**: Hengwei Zhang, Minghui Wu, Li Qiao +3
- **PDF**: https://ieeexplore.ieee.org/document/11016076
- **Abstract**: This letter proposes a deep-learning (DL)-based multi-user channel state information (CSI) feedback framework for massive multiple-input multiple-output systems, where the deep joint source-channel coding (DJSCC) is utilized to improve the CSI reconstruction accuracy. Specifically, we design a multi-user joint CSI feedback framework, whereby the CSI correlation of nearby users is utilized to reduce the feedback overhead. Under the framework, we propose a new residual cross-attention transformer architecture, which is deployed at the base station to further improve the CSI feedback performance. Moreover, to tackle the “cliff-effect” of conventional bit-level CSI feedback approaches, we integrated DJSCC into the multi-user CSI feedback, together with utilizing a two-stage training scheme to adapt to varying uplink noise levels. Experimental results demonstrate the superiority of our methods in CSI feedback performance, with low network complexity and better scalability.

## Joint Data Retransmission and Client Selection Optimization for Error-Tolerant Federated Learning in AAV Networks

- **Status**: ❌
- **Reason**: AAV 네트워크 연합학습(FL) 최적화 연구, ECC 기법 없음
- **ID**: ieee:10807260
- **Type**: journal
- **Published**: Aug. 2025
- **Authors**: Chao Dong, Feiyu Wu, Yuben Qu +5
- **PDF**: https://ieeexplore.ieee.org/document/10807260
- **Abstract**: The flexibility and mobility of autonomous aerial vehicles (AAV) swarms enable them to integrate with federated learning (FL), an emerging distributed machine learning framework. AAV-FL creates an edge intelligence system for AAV swarms. However, unreliable AAV networks lead to a large amount of retransmissions for the dropped data, making it difficult for FL in AAV swarms to achieve the expected accuracy within a short period. Fortunately, benefiting from the dilution effect of convolutional computations, FL can tolerate a limited amount of model parameter errors. Thus motivated, this paper proposes a novel FL framework called FedET, to jointly optimize data retransmission and client selection to achieve error-tolerant FL in AAV networks. Specifically, FedET utilizes error tolerance of FL to reduce the number of retransmissions, which navigates the trade-off between training time and model accuracy. Meanwhile, the impact of retransmission on client selection is also analyzed. We formulate the training utility maximization problem for FL via jointly optimizing data retransmission and client selection. To solve this problem, we propose an alternating optimization-based algorithm to reach the local optimal solution. We implement and evaluate FedET on widely used real-world AAV embedded devices (i.e., NVIDIA Jetson devices). Compared to existing FL algorithms, when faced with unreliable AAV networks, FedET on average reduces the total training time by ~45.8%, and transmission latency by ~67.9%, respectively.

## Fast Simulation of Channel-Coded MIMO-OFDM Transmission in Multipath Fading at Low Error Rates

- **Status**: ❌
- **Reason**: MIMO-OFDM 중요도 샘플링 기반 고속 시뮬레이션 방법론, LDPC 디코더·코드설계 기법 없음
- **ID**: ieee:10818518
- **Type**: journal
- **Published**: Aug. 2025
- **Authors**: You-Zong Yu, Tzu-Hsien Sang, David W. Lin
- **PDF**: https://ieeexplore.ieee.org/document/10818518
- **Abstract**: The low-error-rate requirement of ultra-reliable communication poses a significant challenge to simulation-based performance evaluation of such systems, as conventional Monte Carlo (MC) simulation becomes extremely time-consuming at very low error rates. This work considers fast simulation of multi-input multi-output (MIMO) orthogonal frequency division multiplexing (OFDM) transmission over multipath fading channels via importance sampling (IS). The efficiency of an IS simulator hinges on several key factors: 1) how sharply it can differentiate error-causing and non-error-causing subsets in the sample space, 2) how readily it can profile the probability distribution regarding these subsets, and 3) how proficiently it can generate and distribute samples over particular subsets of interest. In this perspective, we develop a novel IS method in the vein known as histogram-shaping Monte Carlo (HSMC). First, an error gauging function that is generally applicable to channel-coded MIMO-OFDM systems is proposed to highlight potentially error-causing samples in multipath fading channels. Second, we develop a sampler that not only generates random samples effectively from error-causing subsets but also facilitates fast estimation of subset-associated probabilities. New Radio (NR) link-level simulation is conducted to showcase the advantages of the proposed method, revealing approximately 10- to  $10^{7}$ -fold speedup compared to conventional MC simulation.

## A Spinal Coded System for Fading Channels: Dynamic Decoding and Puncturing Strategy

- **Status**: ❌
- **Reason**: Spinal 코드 기반 페이딩 채널 전송 논문 — LDPC와 무관하며 무선 통신 특이적 rateless 코드 기법으로 NAND ECC에 이식 가능한 기법 없음
- **ID**: ieee:10930702
- **Type**: journal
- **Published**: Aug. 2025
- **Authors**: Zixuan Zhang, Ling Zhao, Jiaming Bai
- **PDF**: https://ieeexplore.ieee.org/document/10930702
- **Abstract**: Fading channels are pivotal in mobile communication, introducing varying levels of distortion that greatly affect transmission performance. While rateless codes like Spinal codes offer enhanced spectral efficiency in time-varying channels, they encounter practical hurdles in fading environments, such as high decoding complexity and the inability to leverage frequency diversity in multi-carrier systems. To overcome these challenges, this paper presents an optimized decoding and puncturing scheme. By leveraging equalization results to estimate and classify distortion levels in received symbols, our scheme allows for targeted adjustments to the decoding tree structure. In instances of decoding failure, the scheme selectively includes varying lengths of auxiliary information in the feedback, assisting the sender in making puncturing decisions. Through extensive simulations, we demonstrate rate performance increase of 7%–42% and decoding complexity decrease of 23%–70% compared to existing algorithms in severe multi-path scenarios, thereby enhancing the reliability and applicability of Spinal codes in fading channels.

## Hardware-Efficient Architecture for Multiple Quantized Gaussian Noise Generation

- **Status**: ❌
- **Reason**: FPGA 가우시안 노이즈 생성기 HW 아키텍처, 디코더·코드설계 직접 이식 불가
- **ID**: ieee:10830277
- **Type**: journal
- **Published**: Aug. 2025
- **Authors**: Kangjoon Choi, In-Cheol Park
- **PDF**: https://ieeexplore.ieee.org/document/10830277
- **Abstract**: This paper presents two novel architectures to generate a number of quantized Gaussian noises. The first architecture exploits inversion through uniform segmentation, enabling a uniform look up table (LUT) splitting technique to efficiently generate quantized Gaussian noise while maintaining reasonable tail quality in Gaussian noise generation. The second architecture utilizes inversion through hierarchical segmentation and a probability-based LUT selection, significantly reducing the total LUT size while preserving the tail quality of the generated Gaussian noise. Both designs generate multiple uniform random numbers by cascading combinational circuits, which improves Gaussian noise generation efficiency compared to the conventional linear feedback shift register-based method. Compared to the previous architecture based on inversion through hierarchical segmentation, the proposed uniform segmentation architecture achieves a 6.02x improvement, when implemented on a field-programmable gate array device, in terms of throughput per configurable logic block, and the proposed hierarchical segmentation architecture achieves a 2.71x improvement.

## SINR-Adaptive and CBR-Controllable Semantic Cellular Communication Considering Imperfect CSI and Inter-Cell Co-Channel Interference

- **Status**: ❌
- **Reason**: 시맨틱 통신 연구에서 LDPC는 비교 벤치마크 기준으로만 언급, 이식 가능 ECC 기법 없음
- **ID**: ieee:10813024
- **Type**: journal
- **Published**: Aug. 2025
- **Authors**: Haiwen Niu, Luhan Wang, Zhaoming Lu +2
- **PDF**: https://ieeexplore.ieee.org/document/10813024
- **Abstract**: Deep learning (DL)-enabled semantic communications offer promising prospects for higher data transmission efficiency. However, most existing studies focus on point-to-point transmissions with perfect channel state information (CSI) and fixed channel bandwidth ratio (CBR). This paper investigates multi-point transmission in cellular networks with spectrum resource sharing and proposes a signal-to-interference plus noise ratio (SINR) adaptive and CBR-controllable semantic cellular communication system (SACC). In this system, we design a semantic encoder by a Transformer-convolutional neural network (CNN) mixture block to capture non-local and local latent image features simultaneously and a SINR-adaptive module based on the channel-spatial soft attention mechanism to scale image features according to SINR conditions. A model adaption strategy is proposed to handle varying inter-cell co-channel interference proportions under the same SINR. Additionally, a semantic-channel encoder-decoder forwarding paradigm, termed semantic translation, enables dynamic networking among intra-cell users. Extensive simulation results show that the proposed SACC achieves graceful degradation and better image reconstruction performance versus the current engineered “JEPG+LDPC+QAM” and DeepJSCC benchmarks across different wireless environments and CBRs. Furthermore, experimental results demonstrate substantial improvements in FLOPs, model sizes, and computing latency over the state-of-the-art ADJSCC and WITT with comparable performance.

## A FPGA Implementation of Secure Wireless Communication Based on Digital Chaotic System

- **Status**: ❌
- **Reason**: FPGA 구현이나 4차원 디지털 혼돈계 기반 보안 무선통신으로 LDPC·ECC 내용 없음
- **ID**: ieee:11430466
- **Type**: conference
- **Published**: 8-11 Aug. 
- **Authors**: Jing Li, Yuanxiang Chen, Chaoyi Du +4
- **PDF**: https://ieeexplore.ieee.org/document/11430466
- **Abstract**: To address the growing information security demands in wireless communications, this paper proposes a communication module based on a four-dimensional digital chaotic system. Implemented through an AD9361-ZYNQ platform, the module achieves wireless transceiver functionality with 16 Quadrature Amplitude Modulation(16-QAM) modulated secure transmission of textual and visual data, enabling accurate decryption at the receiving terminal. Theoretical analysis demonstrates that the system possesses a key space of approximately 10180, exhibiting robust resistance against brute-force attacks. Simulation results demonstrate that encrypted images exhibit superior performance in pixel distribution uniformity, spatial correlation elimination, and information randomness, indicating resistance to statistical analysis attacks. Hardware measurements reveal reliable transceiver operation with exceptional error correction capability, achieving a bit error rate (BER) on the order of 10-9, while unauthorized decryption attempts maintain BER of approximately 44%. These substantiate the practical viability of the proposed scheme for secure wireless communication applications.

## Optimizing LDPC Decoding with ML-Assisted Signal Refinement for Next-Gen Communications

- **Status**: ❌
- **Reason**: 무선 페이딩 채널에서 ML 회귀로 수신신호 전처리 후 LDPC 디코딩 — 신호보정은 채널특이적이고 디코더/HW/코드설계로 떼어낼 이식 기법 없음(무선 응용 특이)
- **ID**: ieee:11341206
- **Type**: conference
- **Published**: 29-30 Aug.
- **Authors**: Ambar Bajpai
- **PDF**: https://ieeexplore.ieee.org/document/11341206
- **Abstract**: Low-density parity-checks codes play a crucial role in ensuring reliable data transmission by correcting errors introduced by noisy communication channels. The study examines the performance of LDPC codes in Rayleigh and Rician fading environments, which are commonly encountered in real world wireless networks. Rayleigh fading occurs in areas with significant signal scattering, while Rician fading happens when both direct and scattered signals are present. To enhance the decoding process, this research incorporated a Machine Learning (ML) technique known as regression - polynomial and linear. The ML model is trained to predict and compensate for distortions in the received signal, making it clearer before decoding. The process starts with encoding data using LDPC codes, Followed by BPSK modulation. The modulated signal is transmitted through a Rayleigh or Rician fading channel, where noise and interference affect the transmission. Upon reception, the regression - based ML model processes the signal, reducing distortion and improving quality. Finally, the refined signal is decoded using an LDPC decoder, enhancing error correction and message recovery. BY combining LPDC codes with ML - based regression, this method significantly improves communication reliability, especially in challenging wireless conditions.

## Blind Recognition of LDPC Codes via Weighted Log-Likelihood Ratio and Non-Local Attention Residual Network

- **Status**: ❌
- **Reason**: LDPC 부호 파라미터 블라인드 인식(비협력 통신)으로 ECC 디코더/구성/HW 기여 아님
- **ID**: ieee:11415541
- **Type**: conference
- **Published**: 22-24 Aug.
- **Authors**: Jie Yang, Jiawen Chen, Xuhui Ding +1
- **PDF**: https://ieeexplore.ieee.org/document/11415541
- **Abstract**: Blind recognition serves as a critical technology for adaptive modulation and coding (AMC) in non-cooperative communications and the massive Internet of Things (IoT). This paper proposes a novel deep learning framework for blind recognition of low-density parity-check (LDPC) code parameters over a candidate set. First, discriminative features encoded through weighted log-likelihood ratios (WLLRs) are constructed by integrating the structural constraints of the check matrix with the soft information of received signals. Then, a nonlocal attention-enhanced deep residual network is developed to achieve code parameter classification through global dependency modeling and hierarchical feature extraction. Simulation experiments show that the proposed algorithm outperforms the existing methods in terms of recognition accuracy and noise resistance.

## A Novel HARQ Scheme for LDPC-Coded SCMA Systems based on Network Coding

- **Status**: ❌
- **Reason**: LDPC-coded SCMA HARQ+네트워크코딩 — 무선 응용 특이적, LDPC는 베이스라인, 이식 기법 없음
- **ID**: ieee:11231840
- **Type**: conference
- **Published**: 22-24 Aug.
- **Authors**: Huanyu Chen, Jinglun Shi
- **PDF**: https://ieeexplore.ieee.org/document/11231840
- **Abstract**: This paper proposes an improved Hybrid Automatic Repeat Request with Incremental Redundancy (HARQ-IR) scheme for LDPC-coded SCMA systems. Unlike conventional HARQ-IR mechanisms, our solution innovatively integrates Network Coding (NC) technology—specifically, employing XOR-based linear network coding to combine two retransmission packets into a single network-coded packet. Furthermore, a decoding algorithm is designed to enable joint decoding by synergistically leveraging both the original transmission information and the network-coded packet. Experimental results demonstrate that the proposed scheme achieves a significantly lower BER and higher throughput across a wide range of SNR conditions compared to conventional approaches.

## Design and Analysis of Adaptive and Ultra-Reliable Hybrid Coded Modulated THz/FSO Systems Based on Polar Code

- **Status**: ❌
- **Reason**: polar code 기반 THz/FSO 시스템 — LDPC 아님, 제외
- **ID**: ieee:11292360
- **Type**: conference
- **Published**: 22-24 Aug.
- **Authors**: Shuang Gao, Jiao Zhang, Yutong Jiang +3
- **PDF**: https://ieeexplore.ieee.org/document/11292360
- **Abstract**: With the increasing demand for ultra-high-speed and reliable wireless communication in 6G networks, hybrid Terahertz (THz) and Free-Space Optical (FSO) systems have drawn growing attention. This paper proposes an adaptive hybrid coded modulation scheme for parallel THz/FSO systems, employing polar codes to support flexible rate adjustment and robust transmission. A scenario-driven multi-dimensional adaptive strategy is introduced, dynamically adjusting coding, modulation, and resource allocation parameters based on channel state variations. Simulation results under various environmental scenarios demonstrate that the proposed method achieves reliable communication and low bit error rates, validating its potential for high-capacity and resilient 6G communication systems.

## Scalable Low Complexity Distributed Message Passing Detector for Cell-Free MIMO Systems

- **Status**: ❌
- **Reason**: Cell-free MIMO 검출기(MPD/AP선택) 무선 응용 특이적, LDPC ECC 디코더로 떼어낼 기법 없음
- **ID**: ieee:11292463
- **Type**: conference
- **Published**: 22-24 Aug.
- **Authors**: Yuhang Deng, Xiaosi Tan, Wenyue Zhou +2
- **PDF**: https://ieeexplore.ieee.org/document/11292463
- **Abstract**: Cell-free multiple-input multiple-output (MIMO) technology is a key enabler for future wireless communication systems, offering significant improvements in spectral efficiency and network coverage. However, its practical implementation faces challenges due to high computational complexity and excessive fronthaul load. To address these issues, we propose a low-complexity distributed message passing detection (MPD) algorithm, named deNMPD, which achieves outstanding bit error rate (BER) performance while maintaining computational efficiency. Additionally, we introduce an iterative detection and decoding (IDD)-based AP selection scheme that effectively balances BER performance and fronthaul load reduction. Simulation results validate the superiority of our proposed methods, demonstrating substantial gains in BER performance and computational efficiency while alleviating system overhead. The proposed AP selection method achieves BER performance comparable to all AP scheme while reducing fronthaul load by 33%, making it competitive with the DCC scheme.

## An OFDM Spectrum Suppressed Transmission Using FEC Metric Masking for LDPC Coding

- **Status**: ❌
- **Reason**: OFDM 스펙트럼 억제 전송에서 FEC metric masking 적용 — LDPC는 부수 언급, NAND에 떼어낼 디코더/코드 기법 없음(무선 응용 특이적).
- **ID**: ieee:11151901
- **Type**: conference
- **Published**: 20-22 Aug.
- **Authors**: Tatsuya Tanaka, Takatoshi Sugiyama
- **PDF**: https://ieeexplore.ieee.org/document/11151901
- **Abstract**: An OFDM (Orthogonal Frequency Division Multiplexing) spectrum suppressed transmission is one of the most effective schemes to increase frequency utilization efficiency for wireless communications. It makes the required bandwidth of the transmitted signal narrower than the Nyquist bandwidth, while maintaining the throughput as much as possible. It has the advantage of being easy to implement in hardware by replacing some subcarriers with null subcarriers for the spectrum suppression based on OFDM modulation. Until now, the frequency utilization efficiency of OFDM spectrum suppressed transmission has previously been evaluated only for a conventional FEC (Forward Error Correction) of convolutional coding and Viterbi decoding. Moreover, FEC metric masking, which replaces the metric values of the null subcarriers with the neutral values at the receiver, has also been proposed to improve the degraded transmission quality due to the spectrum suppression.This paper proposes an OFDM spectrum suppressed transmission using FEC metric masking for a more powerful FEC of LDPC (Low Density Parity Check) coding. The quantitative evaluation clarifies that the proposed scheme can achieve better frequency utilization efficiency compared to that without FEC metric masking.

## Sparse Superposition Codes With Short Lengths Based on Zero Correlation Zone Sequence Sets

- **Status**: ❌
- **Reason**: Sparse superposition code(ZCZ 시퀀스 기반) — LDPC ECC가 아니고 NAND에 이식할 디코더/코드 기법 없음.
- **ID**: ieee:11151936
- **Type**: conference
- **Published**: 20-22 Aug.
- **Authors**: Po-Chih Hsu, Feng-Kai Liao, Zhen-Ming Huang +3
- **PDF**: https://ieeexplore.ieee.org/document/11151936
- **Abstract**: Short packet transmission has been adopted to reduce latency in ultra-reliable and low-latency communications (URLLCs). In recent years, sparse superposition codes (SSCs) have received significant attention due to their good performance in short block lengths. This paper presents a new construction of sparse superposition codes based on the zero correlation zone (ZCZ) sequence sets. By utilizing the properties of the ZCZ sequence sets, the projection matrices of the proposed SSCs have good correlation properties. Performance evaluation reveals that the proposed SSCs based on ZCZ sequence sets outperform the SSCs based on the Zadoff-Chu (ZC) sequences for short packet transmission.

## Feasibility of 256/1024-QAM Transmission under Time-Varying Self-Interference in Full-duplex Mobile Communications

- **Status**: ❌
- **Reason**: Full-duplex 자기간섭 제거·QAM-OFDM 전송 성능 평가 — ECC/LDPC와 무관, 떼어낼 기법 없음.
- **ID**: ieee:11151906
- **Type**: conference
- **Published**: 20-22 Aug.
- **Authors**: Kazuma Matsushima, Hiroyuki Otsuka, Takatoshi Sugiyama
- **PDF**: https://ieeexplore.ieee.org/document/11151906
- **Abstract**: Full-duplex mobile communication is considered as an access method between base station (BS) and user equipment (UE) enabling simultaneous transmission and reception on the same carrier frequency, which can double spectral efficiency compared with conventional frequency division duplex (FDD) and time division duplex (TDD) methods. To achieve this, it is essential to establish a technology that eliminates self-interference (SI). We have been investigating a frequency domain adaptive SI canceller using a demodulation reference signal (DMRS) defined in 5G, as well as a time-domain SI canceller. This paper investigates the transmission performance of QAM-OFDM signals under time-varying SI conditions for frequency domain SI canceller. Specifically, the BERs of QAM-OFDM signals are demonstrated as parameters of the time variation speed of SI. The simulation results verify that the frequency domain adaptive SI canceller can sufficiently eliminate SI and high-order QAM transmission is feasible when the time variation speed of SI is relatively slow.

## Efficient Probabilistic Parity Shaping for Irregular Repeat-Accumulate LDPC Codes

- **Status**: ❌
- **Reason**: IRA LDPC 패리티 비트 확률 성형 — 신호 성형 기법, 채널 성형 의존이라 NAND 바이너리 ECC에 떼어낼 기법 없음
- **ID**: ieee:11154639
- **Type**: conference
- **Published**: 18-22 Aug.
- **Authors**: Diego Lentner, Thomas Wiegart, Richard D. Wesel
- **PDF**: https://ieeexplore.ieee.org/document/11154639
- **Abstract**: Algorithms are presented that efficiently shape the parity bits of systematic irregular repeat-accumulate (IRA) low-density parity-check (LDPC) codes by following the sequential encoding order of the accumulator. Simulations over additive white Gaussian noise (AWGN) channels with on-off keying show a gain of up to 0.9 dB over uniform signaling.

## rptu.de/channel-codes: An Update on the Maximum Likelihood Decoding Performance of 5G-NR Channel Codes

- **Status**: ❌
- **Reason**: 5G-NR LDPC/polar의 ML 디코딩 성능 벤치마크 — 새 디코더/HW/구성 없음, 순수 기준선
- **ID**: ieee:11154507
- **Type**: conference
- **Published**: 18-22 Aug.
- **Authors**: Oliver Griebel, Kira Kraft, Lucas Johannsen +3
- **PDF**: https://ieeexplore.ieee.org/document/11154507
- **Abstract**: Maximum likelihood (ML) decoding is the "champions league" of all decoding algorithms. Instead of solving the decoding problem heuristically, it is solved optimally and, therefore, provides the best possible error correction performance among all decoding algorithms. On the downside, ML decoding is an NP-hard problem. Knowing the ML performance of different codes is important as it provides an ultimate benchmark for the code’s potential and the potential of any heuristic decoding algorithm, which is especially valuable for the research community. This paper provides the state of the art on simulating a code’s ML performance and new results for 5G new radio (5G-NR) low-density parity-check (LDPC) and polar codes. All results are publicly available at www.rptu.de/channel-codes, which is well known by the coding community.

## Geometric and Probabilistic Shaping to Enable LDPC Encoding with Linear Complexity

- **Status**: ❌
- **Reason**: 확률적 진폭성형(PAS)을 위한 LDPC 인코딩 — 변조 성형이 핵심, NAND에 떼어낼 ECC 기법 아님(채널 성형 의존)
- **ID**: ieee:11154629
- **Type**: conference
- **Published**: 18-22 Aug.
- **Authors**: Semira Galijasevic, Gianluigi Liva, Dariush Divsalar +1
- **PDF**: https://ieeexplore.ieee.org/document/11154629
- **Abstract**: Previous examples of probabilistic amplitude shaping (PAS) for low-density parity-check (LDPC) codes use protographs that lack the structure that facilitates low-complexity encoding. This paper optimizes the signaling positions and probability mass function (PMF), i.e. we use both geometric and probabilistic shaping, to facilitate LDPC encoders with encoding complexity that is linear in blocklength while still harvesting the capacity-approaching benefits of PAS. The new approach equalizes the conditional entropies of the bits that label the constellation points, which decouples the LDPC design from the specific signaling PMF. An example shows how the new signaling PMF and a newly designed protograph-based LDPC code with rate 2/3 and blocklength n = 64, 800 allow encoding with linear complexity while slightly outperforming previous designs by operating within 0.57 dB of the additive white Gaussian noise channel capacity at FER 10−3 with a low-complexity encoder.

## Advancing Finite-Length Quantum Error Correction Using Generalized Bicycle Codes

- **Status**: ❌
- **Reason**: 양자 generalized bicycle 코드 유한길이 성능, 양자전용(CSS) — 떼어낼 바이너리 기법 없음
- **ID**: ieee:11154497
- **Type**: conference
- **Published**: 18-22 Aug.
- **Authors**: Olai Å. Mostad, Hsuan-Yin Lin, Eirik Rosnes +2
- **PDF**: https://ieeexplore.ieee.org/document/11154497
- **Abstract**: Generalized bicycle (GB) codes have emerged as a promising class of quantum error-correcting codes with practical decoding capabilities. While numerous asymptotically good quantum codes and quantum low-density parity-check code constructions have been proposed, their finite block-length performance often remains unquantified. In this work, we demonstrate that GB codes exhibit comparable or superior error correction performance in finite-length settings, particularly when designed with higher or unrestricted row weights. Leveraging their flexible construction, GB codes can be tailored to achieve high rates while maintaining efficient decoding. We evaluate GB codes against other leading quantum code families, such as quantum Tanner codes, single-parity-check product codes, and bivariate bicycle codes, highlighting their versatility in practical finite-length applications.

## Quantum Error Correction with Girth-16 Non-Binary LDPC Codes via Affine Permutation Construction

- **Status**: ❌
- **Reason**: 비이진(non-binary) LDPC 기반 양자 EC — 비이진이므로 즉시 제외
- **ID**: ieee:11154564
- **Type**: conference
- **Published**: 18-22 Aug.
- **Authors**: Kenta Kasai
- **PDF**: https://ieeexplore.ieee.org/document/11154564
- **Abstract**: We propose a method for constructing quantum error-correcting codes using non-binary low-density parity-check codes whose Tanner graphs have girth 16. While conventional constructions based on circulant permutation matrices are limited to a maximum girth of 12, our approach leverages affine permutation matrices combined with a randomized sequential selection strategy to eliminate short cycles and achieve girth 16. Numerical experiments show that the proposed codes significantly reduce the number of low-weight codewords. Joint belief propagation decoding over depolarizing channels reveals that although a slight degradation appears in the waterfall region, a substantial improvement is achieved in the error floor performance. We also evaluated the minimum distance of the proposed codes and found that they achieve a larger upper bound than conventional constructions.

## Quantum CSS LDPC Codes with Quasi-Dyadic Structure

- **Status**: ❌
- **Reason**: 양자 CSS LDPC 코드 — 양자 EC, 스태빌라이저/dual-containing 등 양자 전용 구조 의존, 원칙 제외
- **ID**: ieee:11154589
- **Type**: conference
- **Published**: 18-22 Aug.
- **Authors**: Alessio Baldelli, Massimo Battaglioni, Paolo Santini
- **PDF**: https://ieeexplore.ieee.org/document/11154589
- **Abstract**: Quantum quasi-cyclic (QC) and quantum low-density parity-check (LDPC) codes have received significant attention due to their algebraic regularity and performance under low-complexity decoding. In this work, we explore a class of structured quantum codes based on reproducible matrices, which generalize known families such as cyclic, QC, and dyadic codes. Focusing on sparse quasi-dyadic (QD) structures, we investigate how their symmetries influence Tanner graph cycles. Moreover, we construct quantum LDPC codes within the Calderbank-Shor-Steane (CSS) framework, analyzing dual-containing configurations, and assess their error rates.

## Cryptanalysis of a McEliece Cryptosystem Based on Cascaded Goppa-Ldpc Code Encryption

- **Status**: ❌
- **Reason**: McEliece 암호계 안전성 분석(cryptanalysis)·키복구 공격 — 보안 영역, 떼어낼 ECC 디코더/구성 기법 없음
- **ID**: ieee:11154649
- **Type**: conference
- **Published**: 18-22 Aug.
- **Authors**: Benjamin Arnesen, David G. M. Mitchell, Willie K. Harrison
- **PDF**: https://ieeexplore.ieee.org/document/11154649
- **Abstract**: This paper provides a cryptanalysis of a recently-proposed cryptosystem that uses a cascade of McEliece cryptosystems, the first using Goppa codes and the second using low-density parity-check (LDPC) codes. This cryptosystem decreases the key size while presuming to be as secure against known attacks as the original McEliece cryptosystem with Goppa codes. We show that the security of this specific cryptosystem reduces to the security of the McEliece cryptosystem instantiated with an LDPC code, upon which a key-recovery attack can be applied. As demonstrated in this paper, this reduction in security is enabled by an efficient attack against the sum of two codewords from two different codes whose generator matrices are available to the attacker. Combining this attack with the key-recovery attack, a key assumed to have 172-bit security loses 125 bits of security.

## Decimation Strategies for Belief Propagation Decoding of Quantum LDPC Codes

- **Status**: ❌
- **Reason**: 양자 QLDPC용 BPGD 디코더 — code degeneracy 등 양자 전용 개념 의존, 바이너리 LDPC 이식 부적합
- **ID**: ieee:11154483
- **Type**: conference
- **Published**: 18-22 Aug.
- **Authors**: Masoumeh Alinia, David G. M. Mitchell, Hanwen Yao +1
- **PDF**: https://ieeexplore.ieee.org/document/11154483
- **Abstract**: Due to code degeneracy and the graph structure of quantum low-density parity-check (QLDPC) codes, the performance of conventional belief propagation (BP) decoding can be poor. Recently, belief propagation guided decimation (BPGD) has shown promise to combat these challenges. In this paper, we investigate various decimation approaches to improve the error correcting performance and convergence speed of BPGD. We first consider soft decimation, where the BP equations are modified via several tuneable parameters. This approach exhibits linear complexity relative to the length of the block code and is shown to outperform hard decimation approaches for careful selection of the algorithm parameters. We then combine the approaches in a "soft-hard" BPGD variant, where hard decisions are periodically made and those symbols are permanently fixed throughout the remainder of the decoding process. Simulation results show that further performance improvement can be observed in this case at the cost of increasing the algorithmic complexity.

## Improved Construction of Generalized Quantum Tanner Codes

- **Status**: ❌
- **Reason**: 양자 Tanner 코드, 스태빌라이저·square complex 등 양자전용 구성 의존 — 바이너리 고전 이식 불가
- **ID**: ieee:11154489
- **Type**: conference
- **Published**: 18-22 Aug.
- **Authors**: Olai Å. Mostad, Eirik Rosnes, Hsuan-Yin Lin
- **PDF**: https://ieeexplore.ieee.org/document/11154489
- **Abstract**: We propose a generalization of the recently proposed quantum Tanner codes by Leverrier and Zemor. These codes can be constructed equivalently from groups, Cayley graphs, or square complexes constructed from groups. In a recent work, we enlarged this to group actions on finite sets, Schreier graphs, and a family of square complexes. We extend the class of quantum Tanner codes further by replacing the tensor product code in the construction with a Tanner code on any bipartite graph. A stricter property on the other underlying graphs is required, and we show that a common variation of the construction can always be taken to satisfy this condition. This results in improved codes compared to the ones constructed based on Schreier graphs.

## Self-Protective and Rate-Flexible Secure Transmission towards Rail Transit Systems

- **Status**: ❌
- **Reason**: 철도 보안 전송 기법(노이즈 집성·적응 변조·재전송)이 본질, LDPC는 부수 평가용 — 이식할 ECC 기법 없음
- **ID**: ieee:11296653
- **Type**: conference
- **Published**: 18-22 Aug.
- **Authors**: Yizhuo Wang, Qinghe Du, Meng Wang +2
- **PDF**: https://ieeexplore.ieee.org/document/11296653
- **Abstract**: With the advancement of rail transit systems, secure communication has become essential, particularly for rail transit sensor networks (RTSN), which require robust protection against eavesdropping threats. This paper introduces a novel self-protective secure transmission method that integrates traditional noise aggregation with adaptive modulation, feedback retransmission, and hash information isolation to achieve adaptive endogenous security. We designed the structure of the corresponding transmitter and receiver, and evaluated the performance of this solution through simulations using convolutional codes and low-density parity check (LDPC) codes. The results demonstrate that this method can flexibly adapt to varying channel conditions, with an adaptive and self-growing key mechanism that effectively resists eavesdropping attacks. This approach not only enhances the reception quality for legitimate receiver but also significantly degrades the reception conditions for eavesdroppers, ensuring secure transmission and greatly improving system flexibility and inherent security.

## A Novel Parallel Concatenated Convolutional Code Structure Based on Frame Decomposition

- **Status**: ❌
- **Reason**: 터보/PCCC(병렬연접 컨볼루션 코드) 인터리버 설계 — LDPC 아님, NAND ECC에 이식할 LDPC 디코더/구성 기법 없음
- **ID**: ieee:11154568
- **Type**: conference
- **Published**: 18-22 Aug.
- **Authors**: Mohammad Bazzal, Jeremy Nadal, Stefan Weithoffer +2
- **PDF**: https://ieeexplore.ieee.org/document/11154568
- **Abstract**: This paper introduces a novel decomposed parallel concatenated convolutional code (DPCCC) structure designed to increase the minimum Hamming distance (mHD) and reduce the error floor compared to conventional PCCC structures, such as turbo codes (TCs). In DPCCC, the input frame is partitioned into subframes, each independently interleaved and encoded. This decomposition targets mHD codewords, partly through mitigating the quadratic increase in the multiplicity of periodic input weight-2 sequences, thus lowering their probability of co-occurrence in the component codes. We also propose a design algorithm that optimizes each subframe interleaver while accounting for inter-frame dependencies. Simulation results demonstrate that the proposed DPCCC structure, combined with the tailored interleaver design, achieves competitive performance compared to other code classes, with notable improvements in mHD and error floor performance over TCs, while maintaining rate compatibility and supporting low-latency decoder architectures.

## Serially Concatenated Codes for Data Center Networks

- **Status**: ❌
- **Reason**: 데이터센터용 RS/BCH 직렬연접 FEC, LDPC 아님 — 떼어낼 LDPC 기법 없음
- **ID**: ieee:11154486
- **Type**: conference
- **Published**: 18-22 Aug.
- **Authors**: Balázs Matuz, Emna Ben Yacoub, Stefano Calabrò
- **PDF**: https://ieeexplore.ieee.org/document/11154486
- **Abstract**: This work investigates channel code design for next-generation data center networks employing 448G/lane attachment unit interfaces (AUIs). A three-link problem, composed of an electrical, optical, and electrical link, representative of intra- and inter-data center links ranging from a few meters to a few kilometers, is considered. To address high error rates, serially concatenated Reed Solomon (RS) and Bose-Ray-Chaudhuri-Hocquenghem (BCH) codes, both located on the host chip, are proposed. The implementation complexity of different forward error correction (FEC) component codes is discussed, different decoding schemes are compared, and analytical and semi-analytical approximations of the error rates are presented.

## AI/ML Based Encoder and Decoder Design for PUCCH HARQ-ACK Payload

- **Status**: ❌
- **Reason**: PUCCH HARQ-ACK용 AI/ML 인코더/디코더 — 소스분포 활용 JSCC/UEP, LDPC 무관 통신 응용 특이적
- **ID**: ieee:11154632
- **Type**: conference
- **Published**: 18-22 Aug.
- **Authors**: Akash Doshi, Pinar Sen, Kirill Ivanov +5
- **PDF**: https://ieeexplore.ieee.org/document/11154632
- **Abstract**: Error control coding for the systems for the previous generations (2G to 5G) has assumed the inputs bits to be uniformly distributed. However, some sources such as downlink (DL) HARQ-ACK payload are inherently non-uniformly distributed. Hence, there is room for significant performance improvement by employing joint source channel coding design aided by deep learning based techniques. We focus on AI/ML based codebook learning and decoder design for HARQ-ACK payload in order to exploit the source distribution in the control channel codebook and perform Unequal Error Protection (UEP) for the source bits encoded in the codewords. Our results demonstrate 4 - 8 dB reduction in the transmit power required to achieve the desired ACK and NACK error rates, compared to the 5G NR compliant encoder and decoder design.

## Probabilistic Shaping in MIMO: Going Beyond 1.53dB AWGN Gain With the Non-Linear Demapper

- **Status**: ❌
- **Reason**: MIMO 확률적 성형/구면디코딩 — 변조·디매퍼 기법, LDPC ECC 무관
- **ID**: ieee:11154592
- **Type**: conference
- **Published**: 18-22 Aug.
- **Authors**: Kirill Ivanov, Wei Yang, Jing Jiang
- **PDF**: https://ieeexplore.ieee.org/document/11154592
- **Abstract**: Constellation shaping is a well-established method to improve upon a regular quadrature amplitude modulation (QAM). It is known that the gain achieved by any shaping method for an additive white Gaussian noise (AWGN) channel is upper-bounded by 1.53dB. However, the situation becomes less clear in the multiple-input and multiple-output (MIMO) setting.In this paper, we study the application of probabilistic shaping for MIMO channels. We utilize an efficient near-optimal demapper based on sphere decoding (SD) and demonstrate that it is possible to achieve more than 2dB gains, breaking the AWGN limit. It becomes possible because both signal and interference are shaped and the non-linear methods can capture this property and leverage on it to improve the demodulation performance.

## Layered PEXIT-based Optimization of Puncturing Patterns for 5G-LDPC Codes in Few-Iteration Decoding

- **Status**: ❌
- **Reason**: 5G-LDPC 펑처링 패턴 최적화로 통신 응용 특이적 — NAND는 펑처링 안 씀, 떼어낼 ECC 디코더/HW/구성 기법 없음
- **ID**: ieee:11148138
- **Type**: conference
- **Published**: 10-13 Aug.
- **Authors**: Qiushi Xu, Ming Jiang, Qiang Wang
- **PDF**: https://ieeexplore.ieee.org/document/11148138
- **Abstract**: In this paper, an innovative method to optimize the puncturing patterns of the 5G low-density parity-check codes, which leverages layered protograph-based extrinsic information transfer (PEXIT) analysis to evaluate decoding performance and the progressive multi-path search (PMPS) algorithm to optimizing puncturing patterns. Compared with existing methods, layered PEXIT analysis is faster and more accurate, while the PMPS algorithm effectively addresses the local optimum trap commonly encountered by greedy algorithms. Simulation results demonstrate that using optimized puncturing patterns significantly improve the few-iteration decoding performance, thereby enhancing the reliability of resource-constrained communication systems without introducing any additional complexity.

## Systematic BMST-FTP Codes and Their Application to q-ary Erasure Channels

- **Status**: ❌
- **Reason**: q-ary FTP 코드 + 블록 마르코프 중첩전송, q-ary erasure 채널 — 비이진 + erasure 소스, 채널코딩 ECC 아님
- **ID**: ieee:11148182
- **Type**: conference
- **Published**: 10-13 Aug.
- **Authors**: Yaping Lv, Xiao Ma
- **PDF**: https://ieeexplore.ieee.org/document/11148182
- **Abstract**: In this paper, q-ary Fourier Transform Pair (FTP) codes over q-ary erasure channels are investigated. To improve the performance of FTP codes, we propose an encoding and decoding scheme based on block Markov superposition transmission. Specifically, the information symbols of FTP codes are transmitted directly, while the check symbols are transmitted in a superposition way. To analyze the performance, we present a Genie-Aided (GA) lower bound, which serves as a tool to set properly the encoding memory. Simulation results show that the proposed scheme can improve the performance of FTP codes, approaching the Shannon limit within 0.06 at the symbol erasure rate of 10−4. Particularly, the simulated performance matches the GA lower bounds in the low erasure probability region. With the same code rate and similar code length, the proposed scheme performs better than the non-binary low density parity check code.

## A Sub-block Interleaving Algorithm to Mitigate Pilot Interference in LDPC-coded AFDM Systems

- **Status**: ❌
- **Reason**: LDPC-coded AFDM 파일럿 간섭 완화 서브블록 인터리빙 — 통신 응용 특이적, LDPC는 베이스라인
- **ID**: ieee:11148845
- **Type**: conference
- **Published**: 10-13 Aug.
- **Authors**: Siyuan Huang, Yin Xu, Tianyao Ma +5
- **PDF**: https://ieeexplore.ieee.org/document/11148845
- **Abstract**: High-power pilot symbols are essential for accurate channel state estimation in affine frequency division multiplexing (AFDM) systems, but they introduce significant interference to data symbols. While inserting guard intervals around the pilot symbols can reduce the impact of pilot interference, it comes at the cost of reduced spectral efficiency. This paper proposes a sub-block interleaving algorithm for low-density parity-check (LDPC)-coded AFDM systems that mitigates pilot interference while eliminating guard interval requirements. The algorithm provides differentiated protection at the sub-block level, ensuring sufficient protection for bits that are substantially impacted by pilot interference. The algorithm utilizes feedback from channel estimation and classifies interference-affected bits based on the proposed residual pilot interference model. LDPC sub-blocks are then ranked according to their protection capabilities, which are characterized by unequal error protection (UEP), and matched with the corresponding interference-affected bits. Simulation results demonstrate that the sub-block interleaving algorithm significantly improves bit error rate (BER) performance under various channel estimation conditions.

## Low-complexity Decoding Method of Generalized LDPC with Polar Component Codes

- **Status**: ❌
- **Reason**: GLDPC-PC(폴라 컴포넌트) 6G용, SO-SCL 디코딩 — 폴라 컴포넌트 의존적이라 NAND 고전 LDPC에 떼어내기 어려움
- **ID**: ieee:11148625
- **Type**: conference
- **Published**: 10-13 Aug.
- **Authors**: Wenxue Sun, Yin Xu, Hao Ju +5
- **PDF**: https://ieeexplore.ieee.org/document/11148625
- **Abstract**: Generalized low-density parity-check with polar component (GLDPC-PC) codes exhibit promising potential for 6G wireless systems with higher demands on reliability and data rate. The decoding method for GLDPC-PC codes involves belief propagation (BP), where the soft information of the component code is used as extrinsic information for check nodes. Although the Bahl-Cocke-Jelinek-Raviv (BCJR) decoding algorithm provides bitwise optimal soft information for linear block codes, its decoding complexity increases exponentially with the code length, making it impractical for applications. Therefore, the near-optimal soft-output successive cancellation list (SO-SCL) decoding with fixed scaling is proposed to reduce decoding complexity. However, the complexity of SO-SCL decoding still holds potential for further optimization. In this work, we propose an offline approximation of the unvisited probability codebook and a staged scaling strategy for the extrinsic information to reduce decoding complexity while maintaining low performance loss.

## An Improved Full Rank Condition for Nonbinary LDPC Codes over BI-AWGN Channel

- **Status**: ❌
- **Reason**: 비이진(nonbinary) LDPC full rank condition — 비이진 LDPC는 원칙 제외
- **ID**: ieee:11148204
- **Type**: conference
- **Published**: 10-13 Aug.
- **Authors**: Yuhao Liu, Qin Huang
- **PDF**: https://ieeexplore.ieee.org/document/11148204
- **Abstract**: This paper improves the full rank condition (FRC) to construct nonbinary LDPC codes for binary AWGN channels, in which there is usually a one-bit error in one erroneous symbol. When assigning values to symbols in a cycle, our improved FRC condition not only considers rank deficiency, but also prefers values with the smallest probability that the related checks are mistakenly satisfied due to one-bit errors in these symbols. Finally, we present the IFRC-based optimization algorithm performs row-wise optimization on the non-zero elements of the parity-check matrix. Simulation results show the effectiveness of IFRC compared to FRC: the error-correcting performance is improved by 0.1dB to 0.5dB, and the error floor can be reduced by up to an order of magnitude.

## MAMP Detector for AFDM under Doubly Dispersive Channels

- **Status**: ❌
- **Reason**: AFDM 무선 통신용 MAMP 신호 검출기 — LDPC ECC 아닌 채널 검출 응용 특이적, 떼어낼 기법 없음
- **ID**: ieee:11148104
- **Type**: conference
- **Published**: 10-13 Aug.
- **Authors**: Yilin Qi, Haoran Yin, Yanqun Tang +2
- **PDF**: https://ieeexplore.ieee.org/document/11148104
- **Abstract**: With the increasing demand for multi-carrier communication in high-mobility scenarios, it is urgent to design new multi-carrier communication waveforms that can resist large delay-Doppler spreads. Affine frequency division multiplexing (AFDM) is a promising solution for next-generation wireless access to achieve strong delay-Doppler spreads resilience in possible scenarios. By adjusting AFDM parameters to match the multipath delay and Doppler shift of the doubly dispersive channels, AFDM can obtain optimal diversity gain. However, AFDM encounters symbol dispersion in the underlying modulation domain, i.e., the discrete affine Fourier transform (DAFT) domain, which poses significant challenges for signal detection. To overcome this challenge, we proposed an efficient detector for AFDM based on the memory approximate message passing (MAMP) algorithm. It uses a memory matched filter (memory MF) to achieve a high-precision reconstruction of the original signal at the cost of low complexity. We compare the bit error ratio (BER) performance of the proposed MAMP and traditional linear minimum mean square error (LMMSE) detector, and simulation results show that MAMP significantly outperforms LMMSE under integral delay-Doppler conditions.

## Air-to-Water Optical Wireless Communication with a Photon-Counting Receiver

- **Status**: ❌
- **Reason**: 공중-수중 광무선통신 광자계수 수신기 — ECC/LDPC 무관
- **ID**: ieee:11148665
- **Type**: conference
- **Published**: 10-13 Aug.
- **Authors**: Siyan Sun, Tianrui Lin, Tianjian Wei +5
- **PDF**: https://ieeexplore.ieee.org/document/11148665
- **Abstract**: In this paper, we establish an air-to-water optical wireless communication (A2W-OWC) through dynamic air-water interface, where the received signal can be characterized by discrete photons. We initially conduct numerical evaluations using Monte Carlo simulation. Subsequently, we conduct experiments in the swimming pool to observe the influence of waves on the signal and background radiation. The results verify that A2W-OWC system satisfies Poisson model. We investigate the performance improvement of adopting arrays at the transmitter and receiver.

## Lattice-based Linear Equalization for Single Carrier and Multi Carrier Transmission over Doubly Selective Channels

- **Status**: ❌
- **Reason**: 격자 기반 선형 등화 + 이중층 반복복호, 무선 doubly-selective 채널 특이적 — 떼어낼 LDPC 디코더 기여 미약
- **ID**: ieee:11149328
- **Type**: conference
- **Published**: 10-13 Aug.
- **Authors**: Yuxin Lai, Tao Yang
- **PDF**: https://ieeexplore.ieee.org/document/11149328
- **Abstract**: This paper studies a lattice-based linear equalization (LLE) approach over doubly selective channels (DSCs). At the transmitter, the message sequence is encoded using a ring code, which is also a simple yet powerful lattice code. The resultant coded digits are one-to-one mapped to PAM symbols. The receiver carries out linear filtering and computes the a posteriori probabilities (APPs) of some integer linear combinations (ILCs) of the coded digits. Next the APPs of the ILCs are converted into APPs of the coded digits, which are then utilized for channel-code decoding. The optimized linear filter and and integer coefficient matrices for the proposed LLE based scheme are presented. Featuring a parallel processing architecture, our proposed LLE approach outperforms the traditional linear equalizers, such as linear minimum mean square error (MMSE) without significantly increased complexity. Further, we put forth a double-layer iterative (DLI) decoding method for a linear block codes coded LLE scheme. The integer coefficient matrices and the paritycheck matrix code are concatenated to form the effective Tanner graph, and based on which the soft-in-soft-out (SISO) decoding is carried out. Extensive numerical results demonstrate that the developed LLE approach achieves considerably improved bit error rate performance over DSCs for both single-carrier and multi-carrier systems.

## On Design of Interleave-Division Multiple Access with Correlated Sources

- **Status**: ❌
- **Reason**: IDMA + 분산 소스코딩, 다중사용자 검출 — 통신 응용 특이적, LDPC ECC 기법 없음
- **ID**: ieee:11148657
- **Type**: conference
- **Published**: 10-13 Aug.
- **Authors**: Xu Li, Tao Yang, Rongke Liu +1
- **PDF**: https://ieeexplore.ieee.org/document/11148657
- **Abstract**: This paper proposes interleave-division multiple access with correlated sources (IDMA-CS) scheme. Message sequence of each user is compressed by distributed source coding (DSC). Then, compressed sequences are encoded, modulated and sent to a common base station (BS). The BS carries out multiuser detection (MUD) and DSC decoding to recover original message. We develop a separate DSC decoding and MUD (SDSC-MUD) method, which explicitly accounts for the impact of MUD and achieves an integrated processing framework. Further, we propose a “turbo-like” joint DSC decoding and MUD (JDSC-MUD) method that exploits the source correlation to facilitate MUD. It demonstrates that the proposed IDMA-CS scheme can increase the system load to more than 1.3~ 3 times that of conventional IDMA. Numerical results also validate the effectiveness of the JDSC-MUD method.

## Sparse Regression Codes for Covert Communication over Multiple Access Channels

- **Status**: ❌
- **Reason**: Sparse regression codes(SPARC) + AMP 디코더, covert MAC — LDPC 아님, 떼어낼 LDPC 기법 없음
- **ID**: ieee:11148720
- **Type**: conference
- **Published**: 10-13 Aug.
- **Authors**: Haolin Jiang, Yiming Wang, Zhuangfei Wu +1
- **PDF**: https://ieeexplore.ieee.org/document/11148720
- **Abstract**: We study a covert multiple access channel (MAC) with two users. Specifically, each user aims to transmit a message through a noisy channel with a low probability of detection by the adversary. We propose two coding schemes based on sparse regression codes (SPARC), with either a joint approximate message passing (JAMP) decoder or a successive interference cancellation-AMP (SIC-AMP) decoder. Furthermore, we derive an upper bound for the transmission power with given noise power under covert constraint and perform several simulations. The results show that our schemes not only have near-optimal performance and low complexity under Gaussian noise but also perform consistently under other noise distributions.

## Efficient Realization of Multi-channel Visible Light Communication System for Dynamic Cross-Water Surface Channels

- **Status**: ❌
- **Reason**: 5G NR LDPC IP코어를 그대로 갖다 쓴 W2A-OWC FPGA 시스템 — 표준 부호 단순 재사용, 떼어낼 새 ECC 기법 없음
- **ID**: ieee:11148852
- **Type**: conference
- **Published**: 10-13 Aug.
- **Authors**: Han Qi, Tianrui Lin, Tianjian Wei +5
- **PDF**: https://ieeexplore.ieee.org/document/11148852
- **Abstract**: This paper explores the transmission schemes for multi-channel water-to-air optical wireless communication (W2AOWC) and introduces a prototype of a real-time W2A-OWC system based on a field-programmable gate array (FPGA). Utilizing an LED array as the transmitter and an APD array as the receiver, the system establishes a multi-channel transmission module. Such configuration enables parallel operation of multiple channels, facilitating the simultaneous transmission of multiple data streams and enhancing overall throughput. The FPGA serves as a real-time signal processing unit, handling both signal transmission and reception. By integrating low-density parity-check (LDPC) codes from 5G New Radio, the system significantly boosts its detection capabilities for dynamic W2AOWC scenarios. The system also optimizes FPGA resource usage through time-multiplexing operation of an LDPC decoder’s IP core. To evaluate the system’s practicality, experiments were conducted under background radiation in an indoor water tank, measuring the frame error rate under both calm and fluctuating water surfaces. The experimental results confirm the feasibility and effectiveness of the developed W2A-OWC system.

## Low Complexity Turbo Receiver using Interference Sparsity for Massive MIMO

- **Status**: ❌
- **Reason**: Massive MIMO 저복잡도 turbo 수신기 — LDPC 디코더/코드 기여 없음, 무선 응용 특이적
- **ID**: ieee:11149269
- **Type**: conference
- **Published**: 10-13 Aug.
- **Authors**: Yanbo Yu, Linfeng Song, An-An Lu +2
- **PDF**: https://ieeexplore.ieee.org/document/11149269
- **Abstract**: In this paper, we propose a low complexity receiver for massive multiple-input multiple-output (MIMO) communications. We first introduce the beam based statistical channel model (BSCM). By using the sparsity of the beam domain channel and interference, we then derive the low-complexity turbo receiver, which reduces the complexity of the minimum mean square error (MMSE) receiver by reducing the dimension of matrix operations. We also present efficient implementation of the low-complexity turbo receiver. Simulation results show that the proposed receiver can achieve performance close to the MMSE turbo receiver with low computational cost.

## Data-Aided Learning for Multi-Antenna OFDM Systems with Superimposed Pilot in Time-Varying Channel

- **Status**: ❌
- **Reason**: OFDM 수신기 딥러닝 파일럿 기법 — LDPC 무관, 떼어낼 ECC 기법 없음
- **ID**: ieee:11148898
- **Type**: conference
- **Published**: 10-13 Aug.
- **Authors**: Lin Zhao, Hongmei Kang, Fan Ding +1
- **PDF**: https://ieeexplore.ieee.org/document/11148898
- **Abstract**: Deep learning (DL) is now widely applied in the physical layer, with particular attention to end-to-end learning-based communication transceivers. In this paper, we focus on superimposed pilots and propose a novel data-aided end-to-end learning scheme, which is applied to orthogonal frequency division multiplexing (OFDM) systems in time and frequency selective fading environment. Specifically, we conduct multidimensional joint training including time-frequency, power, and geometric shaping of constellation. And we perform the end-to-end training on the transmitter and the proposed data-aided receiver, achieving more reliable data transmission in multi-antenna mobile scenarios.

## Iterative Equalization-Decoding Algorithm with Coded OTFS for LEO Satellite Communications

- **Status**: ❌
- **Reason**: LEO 위성 COTFS 반복 등화-복호 + OLD — 무선 채널 특이적, 떼어낼 바이너리 LDPC ECC 기법 없음
- **ID**: ieee:11149322
- **Type**: conference
- **Published**: 10-13 Aug.
- **Authors**: Siyuan Bai, Jian Jiao, Yaosheng Zhang +3
- **PDF**: https://ieeexplore.ieee.org/document/11149322
- **Abstract**: To satisfy the stringent reliability requirements of next-generation wireless systems, low Earth orbit (LEO) satellite communication receivers must address the challenges posed by doubly-selective (time frequency) fading in satellite-terrestrial links, while ensuring seamless global connectivity. In this paper, we propose a novel iterative equalization-decoding algorithm integrated with coded orthogonal time frequency space (COTFS) to overcome the reliability limitations of conventional receivers. By leveraging the sparse channel estimation results obtained from COTFS signal processing in the delay-Doppler domain, we design a distributed equalization-decoding algorithm coupled with pathwise maximum ratio combining (MRC) to effectively mitigate interference. To address error propagation inherent in conventional iterative detection and balance reliability with complexity, we integrate ordered likelihood decoding (OLD) with a lowcomplexity implementation. Simulation results demonstrate that the proposed algorithm achieves superior reliability compared to conventional COTFS receivers.

## Temporal Context Based Video Semantic Transmission

- **Status**: ❌
- **Reason**: 시맨틱 비디오 전송; LDPC는 베이스라인 비교 대상일 뿐 떼어낼 ECC 기법 없음
- **ID**: ieee:11144399
- **Type**: conference
- **Published**: 1-3 Aug. 2
- **Authors**: Yongda Fei, Haoge Jia, Sheng Wu +1
- **PDF**: https://ieeexplore.ieee.org/document/11144399
- **Abstract**: With the increasing demand for low-latency wireless video transmission applications, the limitations of classical separation-based coding schemes are difficult to effectively capture long-term dependencies and spatiotemporal correlations. To address this challenges, this paper proposes a novel approach called Temporal Context Based Video Semantic Transmission (TCVST) that effectively preserves motion and texture details across multiple scales. TCVST enhances both spatial and temporal accuracy, enabling the model to better captures non-uniform motion and texture variations. Experimental results show that our TCVST achieves better coding gain and Rate-distortion (RD) performance in various established metrics such as Peak Signal-to-Noise Ratio (PSNR) and Multiscale-Structure Similarity (MSSSIM). In terms of transmission performance under complex scene video datasets, the proposed TCVST method can save up to $44.4 \%$ of the channel bandwidth cost, compared to the classical H.264/H. 265 combined with low-density parity-check (LDPC) and digital modulation schemes.

## Development of an Optimized QuantumTechniques for Secure Remote Medical Image Sharing

- **Status**: ❌
- **Reason**: 양자 키 분배(BB84)·암호·스테가노그래피 보안; LDPC ECC와 무관
- **ID**: ieee:11252021
- **Type**: conference
- **Published**: 1-2 Aug. 2
- **Authors**: S. Princy Sophia Rani, Ahmad Abdelhafiz Ali Samhan, Ramisetti Venkata Rao +3
- **PDF**: https://ieeexplore.ieee.org/document/11252021
- **Abstract**: Secure remote sharing of medical images is essential for advancing telemedicine, accurate diagnostics, and collaborative healthcare delivery. The traditional cryptography techniques are fast turning to be susceptible to quantum computing risks and generally are less efficient in high throughput medical settings. To counter such a shortcoming, we present an innovative quantum-oriented solution that utilizes optimized methods of secure and real-time medical image transmission over a long-distance network. In this method, Quantum Key Distribution (BB84 protocol), hybrid cryptography, quantum informed optimization, and quantum steganography are used to provide efficient high-fidelity and low latency transmission of images. The QKD is used to securely create symmetric keys that are to be used in the AES 256 encryption of the image and Elliptic Curve Cryptography is applied so that the metadata can be kept confidential. Immutable and transparent access logs are kept by using the blockchain technology. In order to even improve the performance, a dynamically tuning encryption parameters using a Quantum Genetic Algorithm can be applied to eliminate the computing overhead. Experimental testing with NIH Chest X-ray dataset shows an average encryption and decryption speed of 38.1 milliseconds, with a success rate of more than 25% relative to the conventional post-quantum cryptographic system. The results of a secure transmission show a decrease in latency of 12.5% over the TLS-enhanced QKD. The system keeps the Quantum Bit Error Rate at less than 5% under realistic noise levels and retains more than 75% of the key material obtained. In quantum steganography, the level of accuracy to detect tampering is 98.6%, hence data integrity. The solution has shown the capability to integrate quantum-level security, computing performance, and regulatory durability to become a trusted and long-term process of safe sharing of medical images in modern healthcare systems.
