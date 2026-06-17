# IEEE Xplore — 2025-08


## A PEXIT Analysis of Belief Propagation Polar Decoder with Approximated LLR

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11062680
- **Type**: journal
- **Published**: August 202
- **Authors**: Shuhei Yamaguchi, Yuta Hori, Takahiko Nakamura +1
- **PDF**: https://ieeexplore.ieee.org/document/11062680
- **Abstract**: Belief propagation decoding of Polar codes suffers from performance degradation if the frozen bits are not appropriately allocated. Particularly, when simplified log-likelihood ratio (LLR) calculations are used to reduce hardware complexity, the conventional frozen bit allocation based on protograph extrinsic information transfer (PEXIT) analysis becomes ineffective due to the inaccurate EXIT function. In this paper, we propose a new EXIT function that takes into account the approximation in the LLR for PEXIT analysis. Simulation results show that PEXIT analysis with the proposed EXIT function is able to represent the degradation of bit error rate (BER) due to the LLR approximation.

## Reduced Complexity Dynamic Schedule for Layered Decoding of LDPC Codes

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:10925880
- **Type**: journal
- **Published**: Aug. 2025
- **Authors**: Xinle Jia, Yangcan Zhou, Zijian Qin +2
- **PDF**: https://ieeexplore.ieee.org/document/10925880
- **Abstract**: Low-density parity-check (LDPC) codes have been selected as the coding scheme of the data channel in 5G communication. To enhance the performance of conventional layered decoding of LDPC codes, various dynamic schedules have been proposed recently. However, these dynamic schedules suffer from high complexity. In this paper, we propose a reduced complexity dynamic layered schedule for LDPC codes, where the layer to be updated is determined based on the residual of each layer. Moreover, an adjustable parameter is introduced to achieve a better performance-complexity trade-off. Simulation results show that the proposed method maintains excellent error-correction performance while the computational complexity is greatly reduced, compared to the prior dynamic schedules.

## UniDec: A Unified Factor-Graph-Based Decoder Fully Compatible With 5G NR LDPC/Polar Codes

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11039498
- **Type**: journal
- **Published**: Aug. 2025
- **Authors**: Houren Ji, Yi Zhang, Yutai Sun +3
- **PDF**: https://ieeexplore.ieee.org/document/11039498
- **Abstract**: In comparison to 4G, 5G wireless needs to support a broader range of applications. Therefore, both low-density parity-check (LDPC) codes and polar codes have been standardized by 5G new radio (NR) to fulfill the requirements of data channel and control channel, respectively. Usually, LDPC/polar decodings are implemented by separate hardware, leading to low area efficiency. Though decoders which can handle both codes have been proposed, how to compromise between throughput and efficiency has always been a persistent dilemma due to the absence of a unified and smooth integration methodology. To this end, by fully utilizing the common parts of graph-theoretic algorithms for both codes, this paper presents a unified decoder (UniDec) which is fully compatible with 5G NR LDPC/polar codes. This UniDec enables three key approaches: 1) unified processing nodes for both codes, 2) configurable permutation networks with multi-parallelism, and 3) flexible scheduling for 5G NR parameter configuration, guaranteeing both high data throughput and area efficiency. Implemented in 40nm CMOS, the UniDec attains a maximum of  $33.64\times $  throughput and  $5.98\times $  area efficiency compared to its multi-mode counterparts. Even compared with the state-of-the-art (SOA) dedicated ones, the UniDec still maintains a competitive edge in terms of throughput, energy, and area efficiency. It is noted that this methodology can be generalized to other factor-graph based signal processing algorithms.

## AsLDPC: Improving Decoding Performance With Absorbing Set Characteristic Aware Low-Density Parity-Check Code

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11079633
- **Type**: journal
- **Published**: Aug. 2025
- **Authors**: Lanlan Cui, Fei Wu, Xiaojian Liu +4
- **PDF**: https://ieeexplore.ieee.org/document/11079633
- **Abstract**: Not AND (NAND) flash memory has been widely used in consumer electronics in recent years. Due to various interferences faced by NAND flash memory, data reliability has severely declined. Low-density parity-check (LDPC) codes are leveraged for popular triple-level cell (TLC) NAND flash due to their strong error correction capability. LDPC decoding is an iterative procedure of log-likelihood ratio (LLR). The absorbing sets cause inaccurate LLRs to continuously propagate, making decoding difficult to converge, and severely affecting decoding performance. To improve decoding performance after LLR quantization, we propose an absorbing set characteristic aware LDPC algorithm, called AsLDPC, which modifies the LLR of some nodes in the absorbing sets through two Steps. For Step One, we select variable nodes that fall into absorbing sets based on sign characteristics of LLR at the late iteration and modify the initial prior message. For Step Two, we adjust the LLR of check nodes that satisfy the variable nodes and utilize the revised LLR to continue iteration. AsLDPC abstracts the process of finding the node locations in absorbing sets into formulas, finds the erroneous nodes through calculation, and then modifies their LLR messages. Simulation results demonstrate that AsLDPC significantly reduces the frame error rate (FER) by 58% and 48.1% for two LDPC codes, respectively, when compared to the quasi-uniform quantization scheme, while also reducing decoding latency. Additionally, AsLDPC outperforms the uniform algorithm in terms of storage space efficiency and maintains accurate decoding capabilities for raw bit error rate (RBER) below  $1.2e-2$ .

## AG Codes Achieve List-Decoding Capacity Over Constant-Sized Fields

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11027159
- **Type**: journal
- **Published**: Aug. 2025
- **Authors**: Joshua Brakensiek, Manik Dhar, Sivakanth Gopi +1
- **PDF**: https://ieeexplore.ieee.org/document/11027159
- **Abstract**: The recently-emerging field of higher order MDS codes has sought to unify a number of concepts in coding theory. Such areas captured by higher order MDS codes include maximally recoverable (MR) tensor codes, codes with optimal list-decoding guarantees, and codes with constrained generator matrices (as in the GM-MDS theorem). By proving these equivalences, Brakensiek et al. (2024) showed the existence of optimally list-decodable Reed-Solomon codes over exponential sized fields. Building on this, recent breakthroughs by Guo and Zhang (2023) and Alrabiah et al. (2024) have shown that randomly punctured Reed-Solomon codes achieve list-decoding capacity (which is a relaxation of optimal list-decodability) over linear size fields. We extend these works by developing a formal theory of relaxed higher order MDS codes. In particular, we show that there are two inequivalent relaxations which we call lower and upper relaxations. The lower relaxation is equivalent to relaxed optimal list-decodable codes and the upper relaxation is equivalent to relaxed MR tensor codes with a single parity check per column. We then generalize the techniques of Guo-Zhang and Alrabiah-Guruswami-Li to show that both these relaxations can be constructed by randomly puncturing suitable algebraic-geometric codes over constant size fields. For this, we crucially use the generalized GM-MDS theorem for polynomial codes recently proved by Brakensiek et al. (2024). We obtain the following corollaries from our main result: 1) randomly punctured algebraic-geometric codes of rate R are list-decodable up to radius  $\frac {L}{L+1}(1-R-\epsilon)$  with list size L over fields of size  $\exp (O(L/\epsilon))$ . In particular, they achieve list-decoding capacity with list size  $O(1/\epsilon)$  and field size  $\exp (O(1/\epsilon ^{2}))$ . Prior to this work, AG codes were not even known to achieve list-decoding capacity; and 2) by randomly puncturing algebraic-geometric codes, we can construct relaxed MR tensor codes with a single parity check per column over constant-sized fields, whereas (non-relaxed) MR tensor codes require exponential field size.

## OTFS-Based CV-QKD Systems for Doubly Selective THz Channels

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:10857395
- **Type**: journal
- **Published**: Aug. 2025
- **Authors**: Xin Liu, Chao Xu, Soon Xin Ng +1
- **PDF**: https://ieeexplore.ieee.org/document/10857395
- **Abstract**: The feasibility of continuous variable quantum key distribution (CV-QKD) is considered in the Terahertz (THz) band, experiencing time-varying and frequency-selective fading. Advanced multi-carrier modulation is required for improving the secret key rate (SKR). However, the hostile quantum channel requires powerful classical channel coding schemes for maintaining an adequate reconciliation performance. Against this background, for the first time in the open literature, we propose a multi-carrier quantum transmission regime that incorporates both orthogonal frequency division multiplexing (OFDM) and orthogonal time frequency space (OTFS) transmission over doubly selective fading THz channels. Furthermore, we propose a modified multi-dimensional reconciliation algorithm for CV-QKD, facilitating the integration of OFDM/OTFS quantum transmission with low-density parity check (LDPC) coded key reconciliation. Moreover, we harness multiple-input multiple-output (MIMO) beamforming for mitigating the severe THz path loss. Our SKR analysis results demonstrate that the proposed OTFS-based and LDPC-assisted CV-QKD system is capable of outperforming its OFDM counterpart in mobile wireless scenarios. Moreover, we also demonstrate that increasing the MIMO dimension reduces the transmission power required for achieving the secure transmission distance target.

## Parallel Coding for Orthogonal Delay-Doppler Division Multiplexing

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:10872973
- **Type**: journal
- **Published**: Aug. 2025
- **Authors**: Qi Li, Jinhong Yuan, Min Qiu
- **PDF**: https://ieeexplore.ieee.org/document/10872973
- **Abstract**: This paper proposes a novel parallel coding transmission strategy and an iterative detection and decoding receiver signal processing technique for orthogonal delay-Doppler division multiplexing (ODDM) modulation. Specifically, the proposed approach employs a parallel channel encoding (PCE) scheme that consists of multiple short-length codewords for each delay-Doppler multicarrier (DDMC) symbol. Building upon such a PCE transmission framework, we then introduce an iterative detection and decoding algorithm incorporating a successive decoding feedback (SDF) technique, which enables instant information exchange between the detector and decoder for each DDMC symbol. To characterize the error performance of the proposed scheme, we perform density evolution analysis considering the finite blocklength effects. Our analysis results, coupled with extensive simulations, demonstrate that the proposed PCE scheme with the SDF algorithm not only showcases a better overall performance but also requires much less decoding complexity to implement, compared to the conventional benchmark scheme that relies on a single long channel code for coding the entire ODDM frame.

## On the Application of Expectation Propagation to Symbol Detection in Phase Noise Channels

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:10872962
- **Type**: journal
- **Published**: Aug. 2025
- **Authors**: Elisa Conti, Armando Vannucci, Amina Piemontese +1
- **PDF**: https://ieeexplore.ieee.org/document/10872962
- **Abstract**: In the context of signal detection in the presence of an unknown time-varying channel parameter, receivers based on the Expectation Propagation (EP) framework appear to be very promising. EP is a message-passing algorithm based on factor graphs with an inherent ability to combine prior knowledge of system variables with channel observations. This suggests that an effective estimation of random channel parameters can be achieved even with a very limited number of pilot symbols, thus increasing the payload efficiency. However, achieving satisfactory performance often requires ad-hoc adjustments in the way the probability distributions of latent variables - both data and channel parameters - are combined and projected. Here, we provide, for the first time, an analysis of EP-based algorithms for the classical problem of coded transmission on a strong Wiener phase noise channel, employing soft-input soft-output decoding. The analysis includes possible improvements over the native application of EP, in order to identify its limitations and propose new strategies which reach the performance benchmark while maintaining low complexity, with a primary focus on challenging scenarios where the state-of-the-art algorithms fail.

## Effective Application of Normalized Min-Sum Decoding for Short BCH Codes

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11048551
- **Type**: journal
- **Published**: Aug. 2025
- **Authors**: Guangwen Li, Xiao Yu
- **PDF**: https://ieeexplore.ieee.org/document/11048551
- **Abstract**: This letter introduces an enhanced normalized min-sum decoder designed to address the performance and complexity challenges associated with developing parallelizable decoders for short BCH codes in high-throughput applications. The decoder optimizes the standard parity-check matrix using heuristic binary summation and random cyclic row shifts, resulting in a Tanner graph with low density, controlled redundancy, and minimized length-4 cycles. The impact of row redundancy and rank deficiency in the dual code’s minimum-weight codewords on decoding performance is analyzed. To improve convergence, three random automorphisms are applied simultaneously to the inputs, with the resulting messages merged at the end of each iteration. Extensive simulations demonstrate that, for BCH codes with block lengths of 63 and 127, the enhanced normalized min-sum decoder achieves a 1–2 dB performance gain and  $100\times $  faster convergence compared to existing parallel and iterative decoders. Additionally, a hybrid decoding scheme is proposed, which selectively activates order statistics decoding when the enhanced normalized min-sum decoder fails. This hybrid approach is shown to approach maximum-likelihood performance while retaining the advantages of the normalized min-sum decoder across a broad SNR range.

## Polarization-Aided Multi-User Spatial Modulation

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:10935742
- **Type**: journal
- **Published**: Aug. 2025
- **Authors**: Zhaopeng Xie, Yuanping Wang, Yuehui Xu +2
- **PDF**: https://ieeexplore.ieee.org/document/10935742
- **Abstract**: In this paper, we propose a polarization-aided detection and decoding scheme for polar-coded multi-user spatial modulation (PA-MU-SM) systems. Exploiting the polar code structure, we treat the reception processing in MU-SM as a polar re-encoding that generates an extended-length polar code with nested user codes. The proposed method enables us to decode all user messages within this single polar decoder. Then, a Monte-Carlo construction is utilized to optimize the nested user codes of the extended-length polar code. Furthermore, to eliminate the interference between user layers of the PA-MU-SM, an iterative polarization-aided (I-PA) scheme is designed and can theoretically achieve MU-SM channel capacity via a four-stage channel transform. Simulation results show that the proposed PA and I-PA schemes offer better error performance than the traditional polar-coded spatial modulation (PC-SM) schemes.

## AUTHFi: Cross-Technology Device Authentication via Commodity WiFi

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:10908862
- **Type**: journal
- **Published**: Aug. 2025
- **Authors**: Weizheng Wang, Dusit Niyato, Zehui Xiong +1
- **PDF**: https://ieeexplore.ieee.org/document/10908862
- **Abstract**: The explosive growth of the Internet of Things (IoT) has dramatically increased the demand for secure mechanisms to protect against unauthorized access and attacks. Traditionally, expensive Software-Defined Radios (SDRs) have been utilized to gather IoT physical features, which are critical for reliable authentication. However, the high cost of SDRs makes them impractical for widespread deployment across the vast and diverse IoT ecosystem. In contrast, this paper presents AUTHFi, a novel cross-technology device authentication framework that transforms the SDR approach for collecting and authenticating IoT device signals (e.g., ZigBee and Bluetooth) by utilizing commercial WiFi devices. Specifically, AUTHFi leverages the recent advances in Cross-Technology Communication (CTC) to reconstruct the partial waveform of IoT transmission, thus eliminating the requirement for expensive SDRs. AUTHFi requires us to address several unique challenges. First, AUTHFi compensates for signal losses of the partial waveform to get more signal information. Then, it introduces an enhanced Carrier Frequency Offset (CFO) estimation and a fusion neural network that combines CFO and the reconstructed waveform for accurate device authentication. We implement AUTHFi based on RTL8812au (commodity WiFi) and CC2652P (commodity ZigBee/Bluetooth). Our thorough evaluation confirms that AUTHFi offers reliable authentication under various settings, achieving a maximum accuracy of 94.2%.

## Rényi Divergence Guarantees for Hashing With Linear Codes

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11028607
- **Type**: journal
- **Published**: Aug. 2025
- **Authors**: Madhura Pathegama, Alexander Barg
- **PDF**: https://ieeexplore.ieee.org/document/11028607
- **Abstract**: We consider the problem of distilling uniform random bits from an unknown source with a given p-entropy using linear hashing. As our main result, we estimate the expected p-divergence between the hashed output and the uniform distribution over the ensemble of random linear codes for all integer  $p\ge 2$ . The proof relies on analyzing how additive noise, determined by a random element of the code from the ensemble, acts on the source distribution. This action leads to the transformation of the source distribution into an approximately uniform one, a process commonly referred to as distribution smoothing. We also show that hashing with Reed-Muller matrices reaches intrinsic randomness of memoryless Bernoulli sources in the  $l_{p}$  sense for all integer  $p\ge 2$ .

## A Practical Indexing Scheme for Noisy Shuffling Channels Using Cosets of Polar Codes

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:10769564
- **Type**: journal
- **Published**: Aug. 2025
- **Authors**: Javad Haghighat, Tolga M. Duman
- **PDF**: https://ieeexplore.ieee.org/document/10769564
- **Abstract**: The noisy shuffling channel models the conditions encountered in DNA storage systems, where transmitted data segments experience random permutation and substitution errors. Reliable communication over this channel requires effective indexing and channel coding strategies for segment order restoration and error correction. This paper introduces a concatenated coding approach for communication over the noisy shuffling channel using Reed-Solomon (RS) codes as outer codes and polar codes as inner codes. A coset-based indexing method, derived from polar codes, is proposed. A joint decoder is designed to detect the permutation pattern and perform polar decoding simultaneously. An upper bound on the frame error rate (FER) is derived when minimum distance decoding is employed for decoding. Also, an approximate analysis of the FER using random coding is conducted. A mapping between the cosets of the polar code and subsets of its frozen bits is established to design cosets achieving lower FERs compared to a commonly used explicit indexing method. Furthermore, a low-complexity decoding approach is devised, providing a trade-off between the computational complexity of the joint decoder and its performance.

## Mobility-Aware Decentralized Federated Learning for Autonomous Underwater Vehicles

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:10964078
- **Type**: journal
- **Published**: Aug. 2025
- **Authors**: Hongyi He, Jun Du, Chunxiao Jiang +3
- **PDF**: https://ieeexplore.ieee.org/document/10964078
- **Abstract**: The underwater Internet of Things (UIoT) is crucial in developing marine resources. However, due to the low data rate of underwater channels, it is difficult to have a central server to process data from numerous devices as using terrestrial communications. Therefore, decentralized federated learning (DFL) with communication-efficient modifications is a promising alternative to empower UIoT with artificial intelligence and collaborative training. However, existing DFL strategies rely on a carefully designed small aggregation weight when aggregating parameters from neighbor nodes to mitigate the compression error, resulting in a slow convergence rate. In addition, the effect of data compression under time-varying topologies is not considered in current DFL algorithms. In response to these problems, this work studies a DFL framework with underwater acoustic channel and time-varying topology. Firstly, considering the low data rate and dynamics of the acoustic channel, we propose a practical scheme for adaptive compression and device connectivity. Moreover, we combine data compression and the error-compensation technique with time-varying topology and propose a DFL algorithm with aggregation weights decaying over time to achieve fast convergence under non-independent and identically distributed (non-IID) data. We derive a convergence bound for the proposed algorithm with respect to compression and time-varying topology and demonstrate that it achieves the same asymptotic convergence rate as centralized FL with perfect communication. Simulation results show that the proposed algorithm exhibits higher accuracy and faster convergence rate in underwater environments compared with DFL algorithms without decaying aggregation weights and centralized FL schemes.

## Residual Cross-Attention Transformer-Based Multi-User CSI Feedback With Deep Joint Source-Channel Coding

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11016076
- **Type**: journal
- **Published**: Aug. 2025
- **Authors**: Hengwei Zhang, Minghui Wu, Li Qiao +3
- **PDF**: https://ieeexplore.ieee.org/document/11016076
- **Abstract**: This letter proposes a deep-learning (DL)-based multi-user channel state information (CSI) feedback framework for massive multiple-input multiple-output systems, where the deep joint source-channel coding (DJSCC) is utilized to improve the CSI reconstruction accuracy. Specifically, we design a multi-user joint CSI feedback framework, whereby the CSI correlation of nearby users is utilized to reduce the feedback overhead. Under the framework, we propose a new residual cross-attention transformer architecture, which is deployed at the base station to further improve the CSI feedback performance. Moreover, to tackle the “cliff-effect” of conventional bit-level CSI feedback approaches, we integrated DJSCC into the multi-user CSI feedback, together with utilizing a two-stage training scheme to adapt to varying uplink noise levels. Experimental results demonstrate the superiority of our methods in CSI feedback performance, with low network complexity and better scalability.

## Joint Data Retransmission and Client Selection Optimization for Error-Tolerant Federated Learning in AAV Networks

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:10807260
- **Type**: journal
- **Published**: Aug. 2025
- **Authors**: Chao Dong, Feiyu Wu, Yuben Qu +5
- **PDF**: https://ieeexplore.ieee.org/document/10807260
- **Abstract**: The flexibility and mobility of autonomous aerial vehicles (AAV) swarms enable them to integrate with federated learning (FL), an emerging distributed machine learning framework. AAV-FL creates an edge intelligence system for AAV swarms. However, unreliable AAV networks lead to a large amount of retransmissions for the dropped data, making it difficult for FL in AAV swarms to achieve the expected accuracy within a short period. Fortunately, benefiting from the dilution effect of convolutional computations, FL can tolerate a limited amount of model parameter errors. Thus motivated, this paper proposes a novel FL framework called FedET, to jointly optimize data retransmission and client selection to achieve error-tolerant FL in AAV networks. Specifically, FedET utilizes error tolerance of FL to reduce the number of retransmissions, which navigates the trade-off between training time and model accuracy. Meanwhile, the impact of retransmission on client selection is also analyzed. We formulate the training utility maximization problem for FL via jointly optimizing data retransmission and client selection. To solve this problem, we propose an alternating optimization-based algorithm to reach the local optimal solution. We implement and evaluate FedET on widely used real-world AAV embedded devices (i.e., NVIDIA Jetson devices). Compared to existing FL algorithms, when faced with unreliable AAV networks, FedET on average reduces the total training time by ~45.8%, and transmission latency by ~67.9%, respectively.

## Fast Simulation of Channel-Coded MIMO-OFDM Transmission in Multipath Fading at Low Error Rates

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:10818518
- **Type**: journal
- **Published**: Aug. 2025
- **Authors**: You-Zong Yu, Tzu-Hsien Sang, David W. Lin
- **PDF**: https://ieeexplore.ieee.org/document/10818518
- **Abstract**: The low-error-rate requirement of ultra-reliable communication poses a significant challenge to simulation-based performance evaluation of such systems, as conventional Monte Carlo (MC) simulation becomes extremely time-consuming at very low error rates. This work considers fast simulation of multi-input multi-output (MIMO) orthogonal frequency division multiplexing (OFDM) transmission over multipath fading channels via importance sampling (IS). The efficiency of an IS simulator hinges on several key factors: 1) how sharply it can differentiate error-causing and non-error-causing subsets in the sample space, 2) how readily it can profile the probability distribution regarding these subsets, and 3) how proficiently it can generate and distribute samples over particular subsets of interest. In this perspective, we develop a novel IS method in the vein known as histogram-shaping Monte Carlo (HSMC). First, an error gauging function that is generally applicable to channel-coded MIMO-OFDM systems is proposed to highlight potentially error-causing samples in multipath fading channels. Second, we develop a sampler that not only generates random samples effectively from error-causing subsets but also facilitates fast estimation of subset-associated probabilities. New Radio (NR) link-level simulation is conducted to showcase the advantages of the proposed method, revealing approximately 10- to  $10^{7}$ -fold speedup compared to conventional MC simulation.

## Collective Bit Flipping-Based Decoding of Quantum LDPC Codes

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:10857350
- **Type**: journal
- **Published**: Aug. 2025
- **Authors**: Dimitris Chytas, Nithin Raveendran, Bane Vasić
- **PDF**: https://ieeexplore.ieee.org/document/10857350
- **Abstract**: Quantum low-density parity-check (QLDPC) codes have been proven to achieve higher minimum distances at higher code rates than surface codes. However, this family of codes must cope with the stringent latency constraints imposed by quantum technology and tends to exhibit poor performance under iterative decoding, especially when the variable degree is low. In this work, we improve both the error correction performance and decoding latency of variable degree-3 ( $d_{v}$ -3) QLDPC codes under iterative decoding. Firstly, we perform a detailed analysis of the structure of a well-known family of QLDPC codes, i.e., hypergraph product-based codes. Then, we propose a decoding approach that stems from the knowledge of harmful configurations apparent in these codes. Our decoding scheme is based on applying a modified version of bit flipping (BF) decoding, namely two-bit bit flipping (TBF) decoding, which adds more degrees of freedom to BF decoding. The granularity offered by TBF decoding helps us design sets of decoders that operate in parallel and can collectively decode error patterns appearing in harmful configurations of the code, thus addressing both the latency and performance requirements. Finally, simulation results demonstrate that the proposed decoding scheme surpasses other iterative decoding approaches for various  $d_{v}$ -3 QLDPC codes.

## A Spinal Coded System for Fading Channels: Dynamic Decoding and Puncturing Strategy

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:10930702
- **Type**: journal
- **Published**: Aug. 2025
- **Authors**: Zixuan Zhang, Ling Zhao, Jiaming Bai
- **PDF**: https://ieeexplore.ieee.org/document/10930702
- **Abstract**: Fading channels are pivotal in mobile communication, introducing varying levels of distortion that greatly affect transmission performance. While rateless codes like Spinal codes offer enhanced spectral efficiency in time-varying channels, they encounter practical hurdles in fading environments, such as high decoding complexity and the inability to leverage frequency diversity in multi-carrier systems. To overcome these challenges, this paper presents an optimized decoding and puncturing scheme. By leveraging equalization results to estimate and classify distortion levels in received symbols, our scheme allows for targeted adjustments to the decoding tree structure. In instances of decoding failure, the scheme selectively includes varying lengths of auxiliary information in the feedback, assisting the sender in making puncturing decisions. Through extensive simulations, we demonstrate rate performance increase of 7%–42% and decoding complexity decrease of 23%–70% compared to existing algorithms in severe multi-path scenarios, thereby enhancing the reliability and applicability of Spinal codes in fading channels.

## Hardware-Efficient Architecture for Multiple Quantized Gaussian Noise Generation

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:10830277
- **Type**: journal
- **Published**: Aug. 2025
- **Authors**: Kangjoon Choi, In-Cheol Park
- **PDF**: https://ieeexplore.ieee.org/document/10830277
- **Abstract**: This paper presents two novel architectures to generate a number of quantized Gaussian noises. The first architecture exploits inversion through uniform segmentation, enabling a uniform look up table (LUT) splitting technique to efficiently generate quantized Gaussian noise while maintaining reasonable tail quality in Gaussian noise generation. The second architecture utilizes inversion through hierarchical segmentation and a probability-based LUT selection, significantly reducing the total LUT size while preserving the tail quality of the generated Gaussian noise. Both designs generate multiple uniform random numbers by cascading combinational circuits, which improves Gaussian noise generation efficiency compared to the conventional linear feedback shift register-based method. Compared to the previous architecture based on inversion through hierarchical segmentation, the proposed uniform segmentation architecture achieves a 6.02x improvement, when implemented on a field-programmable gate array device, in terms of throughput per configurable logic block, and the proposed hierarchical segmentation architecture achieves a 2.71x improvement.

## SINR-Adaptive and CBR-Controllable Semantic Cellular Communication Considering Imperfect CSI and Inter-Cell Co-Channel Interference

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:10813024
- **Type**: journal
- **Published**: Aug. 2025
- **Authors**: Haiwen Niu, Luhan Wang, Zhaoming Lu +2
- **PDF**: https://ieeexplore.ieee.org/document/10813024
- **Abstract**: Deep learning (DL)-enabled semantic communications offer promising prospects for higher data transmission efficiency. However, most existing studies focus on point-to-point transmissions with perfect channel state information (CSI) and fixed channel bandwidth ratio (CBR). This paper investigates multi-point transmission in cellular networks with spectrum resource sharing and proposes a signal-to-interference plus noise ratio (SINR) adaptive and CBR-controllable semantic cellular communication system (SACC). In this system, we design a semantic encoder by a Transformer-convolutional neural network (CNN) mixture block to capture non-local and local latent image features simultaneously and a SINR-adaptive module based on the channel-spatial soft attention mechanism to scale image features according to SINR conditions. A model adaption strategy is proposed to handle varying inter-cell co-channel interference proportions under the same SINR. Additionally, a semantic-channel encoder-decoder forwarding paradigm, termed semantic translation, enables dynamic networking among intra-cell users. Extensive simulation results show that the proposed SACC achieves graceful degradation and better image reconstruction performance versus the current engineered “JEPG+LDPC+QAM” and DeepJSCC benchmarks across different wireless environments and CBRs. Furthermore, experimental results demonstrate substantial improvements in FLOPs, model sizes, and computing latency over the state-of-the-art ADJSCC and WITT with comparable performance.

## Optimization of LDPC Decoding Algorithms Through Approximation of the Box-Plus Operation

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11430448
- **Type**: conference
- **Published**: 8-11 Aug. 
- **Authors**: Benqian Sun, Leijing Yang, Jialong Ren +2
- **PDF**: https://ieeexplore.ieee.org/document/11430448
- **Abstract**: The high complexity of the Belief Propagation (BP) decoding algorithm in LDPC decoding leads to greater resource consumption and increased communication link latency. This has become a critical challenge in designing efficient communication systems. The Box-Plus operation can effectively transform the nonlinear equations in check nodes into an addition operation of the minimum and the logarithmic functions, but the logarithmic function still has high complexity. In this paper, we propose an Approximate Box-Plus (ABP) decoding algorithm, which reduces decoding complexity while maintaining decoding performance. We first deduced that the logarithmic function in addition operations essentially represents the error between the BP decoding algorithm and the Min-Sum (MS). Based on this insight, a low-complexity, high-precision substitute function is designed. This function utilizes the boundary control ability and symmetry of the min and max functions to effectively express the relative size changes, thereby reducing the unreliability in check node message passing. The proposed decoding algorithm based on the above function reduces the complexity by 38.9% compared to the BP algorithm, and the mean square error of the substitute function and logarithmic function is only 0.0018. Simulation results demonstrate that the decoding performance improves by approximately 0.4 dB compared to the classical Normalized Min-Sum (NMS) and Offset Min-Sum (OMS) algorithms, and the complexity is increased by only three and two new operations per operation compared to NMS and OMS, respectively.

## A FPGA Implementation of Secure Wireless Communication Based on Digital Chaotic System

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11430466
- **Type**: conference
- **Published**: 8-11 Aug. 
- **Authors**: Jing Li, Yuanxiang Chen, Chaoyi Du +4
- **PDF**: https://ieeexplore.ieee.org/document/11430466
- **Abstract**: To address the growing information security demands in wireless communications, this paper proposes a communication module based on a four-dimensional digital chaotic system. Implemented through an AD9361-ZYNQ platform, the module achieves wireless transceiver functionality with 16 Quadrature Amplitude Modulation(16-QAM) modulated secure transmission of textual and visual data, enabling accurate decryption at the receiving terminal. Theoretical analysis demonstrates that the system possesses a key space of approximately 10180, exhibiting robust resistance against brute-force attacks. Simulation results demonstrate that encrypted images exhibit superior performance in pixel distribution uniformity, spatial correlation elimination, and information randomness, indicating resistance to statistical analysis attacks. Hardware measurements reveal reliable transceiver operation with exceptional error correction capability, achieving a bit error rate (BER) on the order of 10-9, while unauthorized decryption attempts maintain BER of approximately 44%. These substantiate the practical viability of the proposed scheme for secure wireless communication applications.

## Optimizing LDPC Decoding with ML-Assisted Signal Refinement for Next-Gen Communications

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11341206
- **Type**: conference
- **Published**: 29-30 Aug.
- **Authors**: Ambar Bajpai
- **PDF**: https://ieeexplore.ieee.org/document/11341206
- **Abstract**: Low-density parity-checks codes play a crucial role in ensuring reliable data transmission by correcting errors introduced by noisy communication channels. The study examines the performance of LDPC codes in Rayleigh and Rician fading environments, which are commonly encountered in real world wireless networks. Rayleigh fading occurs in areas with significant signal scattering, while Rician fading happens when both direct and scattered signals are present. To enhance the decoding process, this research incorporated a Machine Learning (ML) technique known as regression - polynomial and linear. The ML model is trained to predict and compensate for distortions in the received signal, making it clearer before decoding. The process starts with encoding data using LDPC codes, Followed by BPSK modulation. The modulated signal is transmitted through a Rayleigh or Rician fading channel, where noise and interference affect the transmission. Upon reception, the regression - based ML model processes the signal, reducing distortion and improving quality. Finally, the refined signal is decoded using an LDPC decoder, enhancing error correction and message recovery. BY combining LPDC codes with ML - based regression, this method significantly improves communication reliability, especially in challenging wireless conditions.

## Research on the Application of LDPC Decoding Algorithm Based on Neural Network

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11459897
- **Type**: conference
- **Published**: 23-24 Aug.
- **Authors**: Hong Zhang
- **PDF**: https://ieeexplore.ieee.org/document/11459897
- **Abstract**: In this paper, an optimal implementation method of LDPC decoding algorithm under the 1553 B bus is introduced to meet the requirements of data transmission speed and quality in in-vehicle and inter-vehicle storage, interconnection and fault diagnosis. Based on the neural network algorithm, combined with the programming language and hardware structure, the parallel structure decoding is adopted, which effectively solves the difficult problems such as the generation of the check bit of the teaching evidence, enhances the communication encryption, and reduces the false baud rate in the transmission process. The comprehensive results show that while occupying less hardware resources, the design results have a smaller false baud rate, and the LDPC code has a higher accuracy rate in the codeword ratio sum product algorithm with a longer transmission code length.

## Blind Recognition of LDPC Codes via Weighted Log-Likelihood Ratio and Non-Local Attention Residual Network

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11415541
- **Type**: conference
- **Published**: 22-24 Aug.
- **Authors**: Jie Yang, Jiawen Chen, Xuhui Ding +1
- **PDF**: https://ieeexplore.ieee.org/document/11415541
- **Abstract**: Blind recognition serves as a critical technology for adaptive modulation and coding (AMC) in non-cooperative communications and the massive Internet of Things (IoT). This paper proposes a novel deep learning framework for blind recognition of low-density parity-check (LDPC) code parameters over a candidate set. First, discriminative features encoded through weighted log-likelihood ratios (WLLRs) are constructed by integrating the structural constraints of the check matrix with the soft information of received signals. Then, a nonlocal attention-enhanced deep residual network is developed to achieve code parameter classification through global dependency modeling and hierarchical feature extraction. Simulation experiments show that the proposed algorithm outperforms the existing methods in terms of recognition accuracy and noise resistance.

## Quasi-uniform Quantization based Iterative Detection and Decoding for LDPC Coded SCMA Systems

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11291843
- **Type**: conference
- **Published**: 22-24 Aug.
- **Authors**: Hao Cheng, Jun Chen, Min Zhang +1
- **PDF**: https://ieeexplore.ieee.org/document/11291843
- **Abstract**: Sparse code multiple access (SCMA) has been considered as a competitive candidate multiple access technology to address the challenge of high spectrum efficiency and massive connectivity for 6G communications. However, the use of uniform quantization with limited accuracy may lead to considerable BER performance degradation for the message passing algorithm (MPA) in SCMA detection. In practical communication systems, SCMA operates with channel coding to provide low-latency and reliable communication, and low-density parity-check (LDPC) codes are employed in this work. To address this issue, the quasi-uniform quantizer is proposed, where the uniform quantization strategy is adopted when the probability information value is small, otherwise, the non-uniform quantization is used, which improves the dynamic range of message exchanging in MPA and minimum sum algorithms. Simulation results demonstrate that the proposed quasi-uniform quantizer achieves superior BER performance even with lower quantization precision compared to the uniform quantizer, and subsequently, the computation cost for hardware implementation can be reduced.

## A Novel HARQ Scheme for LDPC-Coded SCMA Systems based on Network Coding

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11231840
- **Type**: conference
- **Published**: 22-24 Aug.
- **Authors**: Huanyu Chen, Jinglun Shi
- **PDF**: https://ieeexplore.ieee.org/document/11231840
- **Abstract**: This paper proposes an improved Hybrid Automatic Repeat Request with Incremental Redundancy (HARQ-IR) scheme for LDPC-coded SCMA systems. Unlike conventional HARQ-IR mechanisms, our solution innovatively integrates Network Coding (NC) technology—specifically, employing XOR-based linear network coding to combine two retransmission packets into a single network-coded packet. Furthermore, a decoding algorithm is designed to enable joint decoding by synergistically leveraging both the original transmission information and the network-coded packet. Experimental results demonstrate that the proposed scheme achieves a significantly lower BER and higher throughput across a wide range of SNR conditions compared to conventional approaches.

## Design and Analysis of Adaptive and Ultra-Reliable Hybrid Coded Modulated THz/FSO Systems Based on Polar Code

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11292360
- **Type**: conference
- **Published**: 22-24 Aug.
- **Authors**: Shuang Gao, Jiao Zhang, Yutong Jiang +3
- **PDF**: https://ieeexplore.ieee.org/document/11292360
- **Abstract**: With the increasing demand for ultra-high-speed and reliable wireless communication in 6G networks, hybrid Terahertz (THz) and Free-Space Optical (FSO) systems have drawn growing attention. This paper proposes an adaptive hybrid coded modulation scheme for parallel THz/FSO systems, employing polar codes to support flexible rate adjustment and robust transmission. A scenario-driven multi-dimensional adaptive strategy is introduced, dynamically adjusting coding, modulation, and resource allocation parameters based on channel state variations. Simulation results under various environmental scenarios demonstrate that the proposed method achieves reliable communication and low bit error rates, validating its potential for high-capacity and resilient 6G communication systems.

## Scalable Low Complexity Distributed Message Passing Detector for Cell-Free MIMO Systems

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11292463
- **Type**: conference
- **Published**: 22-24 Aug.
- **Authors**: Yuhang Deng, Xiaosi Tan, Wenyue Zhou +2
- **PDF**: https://ieeexplore.ieee.org/document/11292463
- **Abstract**: Cell-free multiple-input multiple-output (MIMO) technology is a key enabler for future wireless communication systems, offering significant improvements in spectral efficiency and network coverage. However, its practical implementation faces challenges due to high computational complexity and excessive fronthaul load. To address these issues, we propose a low-complexity distributed message passing detection (MPD) algorithm, named deNMPD, which achieves outstanding bit error rate (BER) performance while maintaining computational efficiency. Additionally, we introduce an iterative detection and decoding (IDD)-based AP selection scheme that effectively balances BER performance and fronthaul load reduction. Simulation results validate the superiority of our proposed methods, demonstrating substantial gains in BER performance and computational efficiency while alleviating system overhead. The proposed AP selection method achieves BER performance comparable to all AP scheme while reducing fronthaul load by 33%, making it competitive with the DCC scheme.

## Enhanced Bit-Flipping Decoding Using Refined Checksum Weights and Flip Metrics for LDPC Codes

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11151954
- **Type**: conference
- **Published**: 20-22 Aug.
- **Authors**: Tofar C.-Y. Chang, Po-Ming Chou, Kai-Chieh Lin +1
- **PDF**: https://ieeexplore.ieee.org/document/11151954
- **Abstract**: Bit-flipping (BF) algorithms for decoding low-density parity-check (LDPC) codes have attracted considerable attention due to their low complexity and high parallelism. While recent improvements have enabled certain BF decoders to approach the performance of belief-propagation (BP) decoding, many of these enhancements rely on complex mechanisms such as loop detection, decoder switching, or costly online computations. In this paper, we propose enhanced BF decoding algorithms that integrate refined checksum weighting and flipping function designs. The proposed weighting scheme jointly exploits soft-valued channel information and hard-decision consistency to better reflect the reliability of each checksum, while maintaining negligible online complexity. Additionally, we propose a flipping function design that implicitly discourages repeated flipping by incorporating the accumulated flip count into its computation, thus suppressing decoding loops without requiring explicit loop detection or decoder switching. Simulation results demonstrate that the proposed decoding strategies yield notable performance gains over existing BF decoders, with only a minor complexity increase.

## Ultra-Low Power LDPC Decoder Design for NAND Flash Storage

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11449331
- **Type**: conference
- **Published**: 20-22 Aug.
- **Authors**: Duen-Yih Teng, Mao-Ruei Li, Shiuan-Hao Kuo
- **PDF**: https://ieeexplore.ieee.org/document/11449331
- **Abstract**: In the AI era, power efficiency has become a major challenge for data storage. Dynamic Single-Level Cell (SLC) technology, which enables Triple-Level or Quad-Level Cell (TLC/QLC) NAND to operate in SLC mode, is critical for balancing performance and capacity, accelerating hot data access and boosting Solid-State Drive (SSD) performance. This research proposes a practical and energy-efficient solution for sustainable NAND flash storage systems by introducing an ultra-low power bit-flipping (ULPBF) decoding algorithm. Our method adaptively switches to normal decoding when necessary and leverages the low error bit property of SLC blocks to reduce power consumption by 42% in both SLC and dynamic SLC modes.

## An OFDM Spectrum Suppressed Transmission Using FEC Metric Masking for LDPC Coding

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11151901
- **Type**: conference
- **Published**: 20-22 Aug.
- **Authors**: Tatsuya Tanaka, Takatoshi Sugiyama
- **PDF**: https://ieeexplore.ieee.org/document/11151901
- **Abstract**: An OFDM (Orthogonal Frequency Division Multiplexing) spectrum suppressed transmission is one of the most effective schemes to increase frequency utilization efficiency for wireless communications. It makes the required bandwidth of the transmitted signal narrower than the Nyquist bandwidth, while maintaining the throughput as much as possible. It has the advantage of being easy to implement in hardware by replacing some subcarriers with null subcarriers for the spectrum suppression based on OFDM modulation. Until now, the frequency utilization efficiency of OFDM spectrum suppressed transmission has previously been evaluated only for a conventional FEC (Forward Error Correction) of convolutional coding and Viterbi decoding. Moreover, FEC metric masking, which replaces the metric values of the null subcarriers with the neutral values at the receiver, has also been proposed to improve the degraded transmission quality due to the spectrum suppression.This paper proposes an OFDM spectrum suppressed transmission using FEC metric masking for a more powerful FEC of LDPC (Low Density Parity Check) coding. The quantitative evaluation clarifies that the proposed scheme can achieve better frequency utilization efficiency compared to that without FEC metric masking.

## Sparse Superposition Codes With Short Lengths Based on Zero Correlation Zone Sequence Sets

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11151936
- **Type**: conference
- **Published**: 20-22 Aug.
- **Authors**: Po-Chih Hsu, Feng-Kai Liao, Zhen-Ming Huang +3
- **PDF**: https://ieeexplore.ieee.org/document/11151936
- **Abstract**: Short packet transmission has been adopted to reduce latency in ultra-reliable and low-latency communications (URLLCs). In recent years, sparse superposition codes (SSCs) have received significant attention due to their good performance in short block lengths. This paper presents a new construction of sparse superposition codes based on the zero correlation zone (ZCZ) sequence sets. By utilizing the properties of the ZCZ sequence sets, the projection matrices of the proposed SSCs have good correlation properties. Performance evaluation reveals that the proposed SSCs based on ZCZ sequence sets outperform the SSCs based on the Zadoff-Chu (ZC) sequences for short packet transmission.

## Feasibility of 256/1024-QAM Transmission under Time-Varying Self-Interference in Full-duplex Mobile Communications

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11151906
- **Type**: conference
- **Published**: 20-22 Aug.
- **Authors**: Kazuma Matsushima, Hiroyuki Otsuka, Takatoshi Sugiyama
- **PDF**: https://ieeexplore.ieee.org/document/11151906
- **Abstract**: Full-duplex mobile communication is considered as an access method between base station (BS) and user equipment (UE) enabling simultaneous transmission and reception on the same carrier frequency, which can double spectral efficiency compared with conventional frequency division duplex (FDD) and time division duplex (TDD) methods. To achieve this, it is essential to establish a technology that eliminates self-interference (SI). We have been investigating a frequency domain adaptive SI canceller using a demodulation reference signal (DMRS) defined in 5G, as well as a time-domain SI canceller. This paper investigates the transmission performance of QAM-OFDM signals under time-varying SI conditions for frequency domain SI canceller. Specifically, the BERs of QAM-OFDM signals are demonstrated as parameters of the time variation speed of SI. The simulation results verify that the frequency domain adaptive SI canceller can sufficiently eliminate SI and high-order QAM transmission is feasible when the time variation speed of SI is relatively slow.

## High Girth Spatially-Coupled LDPC Codes with Hierarchical Structure

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11154552
- **Type**: conference
- **Published**: 18-22 Aug.
- **Authors**: Haizheng Li, Sisi Miao, Laurent Schmalen
- **PDF**: https://ieeexplore.ieee.org/document/11154552
- **Abstract**: Quasi-Cyclic (QC) low-density parity-check (LDPC) codes are a class of LDPC codes with a simple construction facilitating hardware implementation while achieving excellent performance. In this paper, we introduce an algorithm that constructs QC spatially-coupled (SC) LDPC codes with large girth while keeping the constraint length small. The algorithm offers a "protograph to basegraph" construction, focusing on finding small lifting sizes of QC codes while avoiding short cycles. This work extends the hierarchical quasi-cyclic (HQC) construction for block LDPC codes proposed by Wang et al. to the spatially coupled case. The construction is based on the cycle relevant matrix (CRM) derived from the periodic structure of time-invariant SC-LDPC codes. Numerical results show that the proposed algorithm effectively achieves the target girth with a small lifting factor, enabling low-complexity SC code construction.

## Efficient Probabilistic Parity Shaping for Irregular Repeat-Accumulate LDPC Codes

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11154639
- **Type**: conference
- **Published**: 18-22 Aug.
- **Authors**: Diego Lentner, Thomas Wiegart, Richard D. Wesel
- **PDF**: https://ieeexplore.ieee.org/document/11154639
- **Abstract**: Algorithms are presented that efficiently shape the parity bits of systematic irregular repeat-accumulate (IRA) low-density parity-check (LDPC) codes by following the sequential encoding order of the accumulator. Simulations over additive white Gaussian noise (AWGN) channels with on-off keying show a gain of up to 0.9 dB over uniform signaling.

## A class of quasi-cyclic binary parity-check codes from Reed-Solomon codes

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11154644
- **Type**: conference
- **Published**: 18-22 Aug.
- **Authors**: Kathryn Haymaker, Emily McMillon
- **PDF**: https://ieeexplore.ieee.org/document/11154644
- **Abstract**: In this paper, we explore a construction of binary parity-check codes from nonbinary codes, with a specific focus on Reed-Solomon codes. The parity-check matrices of these codes come from the 1964 construction of superimposed codes by Kautz and Singleton. While some basic bounds on parameters of these parity-check codes are known, the specific parameters are highly dependent on the nonbinary code that one starts with. In this paper, we delve more deeply into parameters of this new class of girth six codes, showing that they are quasi-cyclic, providing bounds on the dimensions of the codes, and bounds on minimum distances in some specific cases. We present a table of small code parameters and note that some of these codes meet the best known minimum distance for binary codes. We draw connections to similar constructions in the literature, but importantly, while existing literature on related codes is largely simulation-based, we present a novel algebraic approach to determining new bounds on parameters of these codes.

## rptu.de/channel-codes: An Update on the Maximum Likelihood Decoding Performance of 5G-NR Channel Codes

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11154507
- **Type**: conference
- **Published**: 18-22 Aug.
- **Authors**: Oliver Griebel, Kira Kraft, Lucas Johannsen +3
- **PDF**: https://ieeexplore.ieee.org/document/11154507
- **Abstract**: Maximum likelihood (ML) decoding is the "champions league" of all decoding algorithms. Instead of solving the decoding problem heuristically, it is solved optimally and, therefore, provides the best possible error correction performance among all decoding algorithms. On the downside, ML decoding is an NP-hard problem. Knowing the ML performance of different codes is important as it provides an ultimate benchmark for the code’s potential and the potential of any heuristic decoding algorithm, which is especially valuable for the research community. This paper provides the state of the art on simulating a code’s ML performance and new results for 5G new radio (5G-NR) low-density parity-check (LDPC) and polar codes. All results are publicly available at www.rptu.de/channel-codes, which is well known by the coding community.

## Geometric and Probabilistic Shaping to Enable LDPC Encoding with Linear Complexity

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11154629
- **Type**: conference
- **Published**: 18-22 Aug.
- **Authors**: Semira Galijasevic, Gianluigi Liva, Dariush Divsalar +1
- **PDF**: https://ieeexplore.ieee.org/document/11154629
- **Abstract**: Previous examples of probabilistic amplitude shaping (PAS) for low-density parity-check (LDPC) codes use protographs that lack the structure that facilitates low-complexity encoding. This paper optimizes the signaling positions and probability mass function (PMF), i.e. we use both geometric and probabilistic shaping, to facilitate LDPC encoders with encoding complexity that is linear in blocklength while still harvesting the capacity-approaching benefits of PAS. The new approach equalizes the conditional entropies of the bits that label the constellation points, which decouples the LDPC design from the specific signaling PMF. An example shows how the new signaling PMF and a newly designed protograph-based LDPC code with rate 2/3 and blocklength n = 64, 800 allow encoding with linear complexity while slightly outperforming previous designs by operating within 0.57 dB of the additive white Gaussian noise channel capacity at FER 10−3 with a low-complexity encoder.

## Advancing Finite-Length Quantum Error Correction Using Generalized Bicycle Codes

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11154497
- **Type**: conference
- **Published**: 18-22 Aug.
- **Authors**: Olai Å. Mostad, Hsuan-Yin Lin, Eirik Rosnes +2
- **PDF**: https://ieeexplore.ieee.org/document/11154497
- **Abstract**: Generalized bicycle (GB) codes have emerged as a promising class of quantum error-correcting codes with practical decoding capabilities. While numerous asymptotically good quantum codes and quantum low-density parity-check code constructions have been proposed, their finite block-length performance often remains unquantified. In this work, we demonstrate that GB codes exhibit comparable or superior error correction performance in finite-length settings, particularly when designed with higher or unrestricted row weights. Leveraging their flexible construction, GB codes can be tailored to achieve high rates while maintaining efficient decoding. We evaluate GB codes against other leading quantum code families, such as quantum Tanner codes, single-parity-check product codes, and bivariate bicycle codes, highlighting their versatility in practical finite-length applications.

## Quantum Error Correction with Girth-16 Non-Binary LDPC Codes via Affine Permutation Construction

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11154564
- **Type**: conference
- **Published**: 18-22 Aug.
- **Authors**: Kenta Kasai
- **PDF**: https://ieeexplore.ieee.org/document/11154564
- **Abstract**: We propose a method for constructing quantum error-correcting codes using non-binary low-density parity-check codes whose Tanner graphs have girth 16. While conventional constructions based on circulant permutation matrices are limited to a maximum girth of 12, our approach leverages affine permutation matrices combined with a randomized sequential selection strategy to eliminate short cycles and achieve girth 16. Numerical experiments show that the proposed codes significantly reduce the number of low-weight codewords. Joint belief propagation decoding over depolarizing channels reveals that although a slight degradation appears in the waterfall region, a substantial improvement is achieved in the error floor performance. We also evaluated the minimum distance of the proposed codes and found that they achieve a larger upper bound than conventional constructions.

## Optimizing Schedulers for Layered BP Decoding: From Code-Specific to Universal Decoding

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11154636
- **Type**: conference
- **Published**: 18-22 Aug.
- **Authors**: Ahmed Elkelesh, Jonathan Ling
- **PDF**: https://ieeexplore.ieee.org/document/11154636
- **Abstract**: We show that optimized message update scheduling can enhance both the error-rate performance and the throughput of layered BP decoding of LDPC codes. As an exemplary attempt, optimized scheduling accelerates BP decoding and leads to approximately 2× throughput enhancement when compared to top-to-bottom row-layered BP decoding of 5G LDPC codes. Furthermore, scheduling enhances the error-rate performance of short-length LDPC codes via ensemble decoding. For short-length 5G LDPC codes, coding gains of up to 0.7 dB and 1.6 dB at BLER of 10−3–10−4 for both AWGN and Rayleigh fading channels can be achieved when compared to conventional BP decoders. Additionally, we show that the same concept applies to general linear block codes (e.g., polar/RM codes) facilitating a unified decoding architecture based on row-layered BP decoders ("one-silicon fits all").

## Quantum CSS LDPC Codes with Quasi-Dyadic Structure

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11154589
- **Type**: conference
- **Published**: 18-22 Aug.
- **Authors**: Alessio Baldelli, Massimo Battaglioni, Paolo Santini
- **PDF**: https://ieeexplore.ieee.org/document/11154589
- **Abstract**: Quantum quasi-cyclic (QC) and quantum low-density parity-check (LDPC) codes have received significant attention due to their algebraic regularity and performance under low-complexity decoding. In this work, we explore a class of structured quantum codes based on reproducible matrices, which generalize known families such as cyclic, QC, and dyadic codes. Focusing on sparse quasi-dyadic (QD) structures, we investigate how their symmetries influence Tanner graph cycles. Moreover, we construct quantum LDPC codes within the Calderbank-Shor-Steane (CSS) framework, analyzing dual-containing configurations, and assess their error rates.

## Deep Unfolded Optical Decoder for LDPC Codes with System Noise Mitigation

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11154547
- **Type**: conference
- **Published**: 18-22 Aug.
- **Authors**: Lantian Wei, Tadashi Wadayama, Kazunori Hayashi
- **PDF**: https://ieeexplore.ieee.org/document/11154547
- **Abstract**: We propose an all-optical low-density parity-check (LDPC) decoder using deep unfolding with learnable damping parameters to mitigate system noise. Our approach enhances the performance of tensor-computable belief propagation (Tensor-BP) algorithm in noisy optical implementation while preserving its matrix-based parallel processing capabilities. Simulation results show that our method significantly outperforms conventional BP decoder under various system noise conditions, approaching ideal noiseless BP decoder performance in high signal-to-noise ratio (SNR) region. This work advances practical optical implementations of LDPC decoders for next-generation high-speed communication systems.

## Mixed-Integer ADMM Decoding for LDPC Codes

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11154578
- **Type**: conference
- **Published**: 18-22 Aug.
- **Authors**: Anthony Ho, Stark C. Draper
- **PDF**: https://ieeexplore.ieee.org/document/11154578
- **Abstract**: In this paper, we study the use of the alternating method of multipliers (ADMM) to decode LDPC codes at moderate blocklengths (100 to 1000 bits). Placing ADMM decoding in a mixed-integer optimization framework, this allows us to leverage an exploration-exploitation paradigm to realize further error-correction performance for the same budget of total number of iterations. We demonstrate our ideas with numerical simulations for the (155,64) rate-0.4 Tanner Code and the (480,360) rate-3/4 code from the IEEE 802.22 WRAN standard.

## Cryptanalysis of a McEliece Cryptosystem Based on Cascaded Goppa-Ldpc Code Encryption

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11154649
- **Type**: conference
- **Published**: 18-22 Aug.
- **Authors**: Benjamin Arnesen, David G. M. Mitchell, Willie K. Harrison
- **PDF**: https://ieeexplore.ieee.org/document/11154649
- **Abstract**: This paper provides a cryptanalysis of a recently-proposed cryptosystem that uses a cascade of McEliece cryptosystems, the first using Goppa codes and the second using low-density parity-check (LDPC) codes. This cryptosystem decreases the key size while presuming to be as secure against known attacks as the original McEliece cryptosystem with Goppa codes. We show that the security of this specific cryptosystem reduces to the security of the McEliece cryptosystem instantiated with an LDPC code, upon which a key-recovery attack can be applied. As demonstrated in this paper, this reduction in security is enabled by an efficient attack against the sum of two codewords from two different codes whose generator matrices are available to the attacker. Combining this attack with the key-recovery attack, a key assumed to have 172-bit security loses 125 bits of security.

## Quantum LDPC Codes with Enhanced Error-Floor Performance under Min-Sum Decoding

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11154487
- **Type**: conference
- **Published**: 18-22 Aug.
- **Authors**: Michele Pacenti, Dimitris Chytas, Bane Vasić
- **PDF**: https://ieeexplore.ieee.org/document/11154487
- **Abstract**: Quantum low-density parity-check codes are a promising approach to fault-tolerant quantum computation, offering potential advantages in rate and decoding efficiency. Quantum Margulis codes are a new class of QLDPC codes derived from Margulis' classical LDPC construction via the two-block group algebra framework. We show that quantum Margulis codes, unlike bivariate bicycle codes which require ordered statistics decoding for effective error correction, can be efficiently decoded using a standard min-sum decoder with linear complexity, when decoded under depolarizing noise. This is attributed to their Tanner graph structure, which does not exhibit group symmetry, thereby mitigating the well-known problem of error degeneracy in QLDPC decoding. To further enhance performance, we propose an algorithm for constructing 2BGA codes with controlled girth, ensuring a minimum girth of 6 or 8, and use it to generate several quantum Margulis codes of length 240 and 642. We validate our approach through numerical simulations, demonstrating that quantum Margulis codes behave significantly better than BB codes in the error floor region, under min-sum decoding.

## Effect of redundancy on syndrome-based decoding for QLDPC codes

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11154620
- **Type**: conference
- **Published**: 18-22 Aug.
- **Authors**: Kirsten D. Morris, Tefjol Pllaha, Christine A. Kelley
- **PDF**: https://ieeexplore.ieee.org/document/11154620
- **Abstract**: Adding redundancy to the parity-check matrix representation has been shown to improve iterative decoder performance in the classical setting due to the consequent removal of small stopping sets or other structures that adversely affect the performance. In this paper, we examine the effect of redundancy on iterative syndrome decoder performance, with the goal of improving decoding for quantum LDPC codes. In particular, we provide a sufficient condition for the graph representation of a code to guarantee that the syndrome decoder converges to the input syndrome for any given input error.

## Action-List Reinforcement Learning Decoders

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11154588
- **Type**: conference
- **Published**: 18-22 Aug.
- **Authors**: Milad Taghipour, Bane Vasić
- **PDF**: https://ieeexplore.ieee.org/document/11154588
- **Abstract**: This paper explores the application of reinforcement learning techniques to enhance the performance of decoding based on flipping bits and finding optimal decisions. We begin by providing an overview of bit-flipping based decoders and reinforcement learning algorithms. We then describe the methodology for mapping the iterative decoding process into Markov Decision Processes (MDPs) and propose a general action-list decoding method for reinforcement learning based decoders irrespective of the class of codes to improve the performance of decoders. We design an action-list decoder based on the Deep-Q network values that substantially enhance performance. We also get benefit of automorphism group of code to further improve the code performance. Finally, we present experimental results for the Binary Symmetric Channel (BSC) to demonstrate the efficiency of the proposed methods.

## Learning Variable Node Selection for Improved Multi-Round Belief Propagation Decoding

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11154498
- **Type**: conference
- **Published**: 18-22 Aug.
- **Authors**: Ahmad Ismail, Raphaël Le Bidan, Elsa Dupraz +1
- **PDF**: https://ieeexplore.ieee.org/document/11154498
- **Abstract**: Error correction at short blocklengths remains a challenge for low-density parity-check (LDPC) codes, as belief propagation (BP) decoding is suboptimal compared to maximum-likelihood decoding (MLD). While BP rarely makes errors, it often fails to converge due to a small number of problematic, erroneous variable nodes (VNs). Multi-round BP (MRBP) decoding improves performance by identifying and perturbing these VNs, enabling BP to succeed in subsequent decoding attempts. However, existing heuristic approaches for VN identification may require a large number of decoding rounds to approach ML performance. In this work, we draw a connection between identifying candidate VNs to perturb in MRBP and estimating channel output errors, a problem previously addressed by syndrome-based neural decoders (SBND). Leveraging this insight, we propose an SBND-inspired neural network architecture that learns to predict which VNs MRBP needs to focus on. Experimental results demonstrate that the proposed learning approach outperforms expert rules from the literature, requiring fewer MRBP decoding attempts to reach near-MLD performance. This makes it a promising lead for improving the decoding of short LDPC codes.

## Decimation Strategies for Belief Propagation Decoding of Quantum LDPC Codes

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11154483
- **Type**: conference
- **Published**: 18-22 Aug.
- **Authors**: Masoumeh Alinia, David G. M. Mitchell, Hanwen Yao +1
- **PDF**: https://ieeexplore.ieee.org/document/11154483
- **Abstract**: Due to code degeneracy and the graph structure of quantum low-density parity-check (QLDPC) codes, the performance of conventional belief propagation (BP) decoding can be poor. Recently, belief propagation guided decimation (BPGD) has shown promise to combat these challenges. In this paper, we investigate various decimation approaches to improve the error correcting performance and convergence speed of BPGD. We first consider soft decimation, where the BP equations are modified via several tuneable parameters. This approach exhibits linear complexity relative to the length of the block code and is shown to outperform hard decimation approaches for careful selection of the algorithm parameters. We then combine the approaches in a "soft-hard" BPGD variant, where hard decisions are periodically made and those symbols are permanently fixed throughout the remainder of the decoding process. Simulation results show that further performance improvement can be observed in this case at the cost of increasing the algorithmic complexity.

## Improved Construction of Generalized Quantum Tanner Codes

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11154489
- **Type**: conference
- **Published**: 18-22 Aug.
- **Authors**: Olai Å. Mostad, Eirik Rosnes, Hsuan-Yin Lin
- **PDF**: https://ieeexplore.ieee.org/document/11154489
- **Abstract**: We propose a generalization of the recently proposed quantum Tanner codes by Leverrier and Zemor. These codes can be constructed equivalently from groups, Cayley graphs, or square complexes constructed from groups. In a recent work, we enlarged this to group actions on finite sets, Schreier graphs, and a family of square complexes. We extend the class of quantum Tanner codes further by replacing the tensor product code in the construction with a Tanner code on any bipartite graph. A stricter property on the other underlying graphs is required, and we show that a common variation of the construction can always be taken to satisfy this condition. This results in improved codes compared to the ones constructed based on Schreier graphs.

## Self-Protective and Rate-Flexible Secure Transmission towards Rail Transit Systems

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11296653
- **Type**: conference
- **Published**: 18-22 Aug.
- **Authors**: Yizhuo Wang, Qinghe Du, Meng Wang +2
- **PDF**: https://ieeexplore.ieee.org/document/11296653
- **Abstract**: With the advancement of rail transit systems, secure communication has become essential, particularly for rail transit sensor networks (RTSN), which require robust protection against eavesdropping threats. This paper introduces a novel self-protective secure transmission method that integrates traditional noise aggregation with adaptive modulation, feedback retransmission, and hash information isolation to achieve adaptive endogenous security. We designed the structure of the corresponding transmitter and receiver, and evaluated the performance of this solution through simulations using convolutional codes and low-density parity check (LDPC) codes. The results demonstrate that this method can flexibly adapt to varying channel conditions, with an adaptive and self-growing key mechanism that effectively resists eavesdropping attacks. This approach not only enhances the reception quality for legitimate receiver but also significantly degrades the reception conditions for eavesdroppers, ensuring secure transmission and greatly improving system flexibility and inherent security.

## A Novel Parallel Concatenated Convolutional Code Structure Based on Frame Decomposition

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11154568
- **Type**: conference
- **Published**: 18-22 Aug.
- **Authors**: Mohammad Bazzal, Jeremy Nadal, Stefan Weithoffer +2
- **PDF**: https://ieeexplore.ieee.org/document/11154568
- **Abstract**: This paper introduces a novel decomposed parallel concatenated convolutional code (DPCCC) structure designed to increase the minimum Hamming distance (mHD) and reduce the error floor compared to conventional PCCC structures, such as turbo codes (TCs). In DPCCC, the input frame is partitioned into subframes, each independently interleaved and encoded. This decomposition targets mHD codewords, partly through mitigating the quadratic increase in the multiplicity of periodic input weight-2 sequences, thus lowering their probability of co-occurrence in the component codes. We also propose a design algorithm that optimizes each subframe interleaver while accounting for inter-frame dependencies. Simulation results demonstrate that the proposed DPCCC structure, combined with the tailored interleaver design, achieves competitive performance compared to other code classes, with notable improvements in mHD and error floor performance over TCs, while maintaining rate compatibility and supporting low-latency decoder architectures.

## Subcode Ensemble Decoding of Polar Codes

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11154484
- **Type**: conference
- **Published**: 18-22 Aug.
- **Authors**: Henning Lulei, Jonathan Mandelbaum, Marvin Rübenacke +3
- **PDF**: https://ieeexplore.ieee.org/document/11154484
- **Abstract**: In the short block length regime, pre-transformed polar codes together with successive cancellation list (SCL) decoding possess excellent error correction capabilities. However, in practice, the list size is limited due to the suboptimal scaling of the required area in hardware implementations. Automorphism ensemble decoding (AED) can improve performance for a fixed list size by running multiple parallel SCL decodings on permuted received words, yielding a list of estimates from which the final estimate is selected. Yet, AED is limited to appropriately designed polar codes. Subcode ensemble decoding (ScED) was recently proposed for low-density parity-check codes and does not impose such design constraints. It uses multiple decodings in different subcodes, ensuring that the selected subcodes jointly cover the original code. We extend ScED to polar codes by expressing polar subcodes through suitable pre-transformations (PTs). To this end, we describe a framework classifying pre-transformations for pretransformed polar codes based on their role in encoding and decoding. Within this framework, we propose a new type of PT enabling ScED for polar codes, analyze its properties, and discuss how to construct an efficient ensemble.

## Fractional Doping of Protograph-Based Spatially Coupled LDPC Codes

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11154543
- **Type**: conference
- **Published**: 18-22 Aug.
- **Authors**: Daniel J. Costello, Min Zhu, David G. M. Mitchell +1
- **PDF**: https://ieeexplore.ieee.org/document/11154543
- **Abstract**: In this paper, we investigate ways to mitigate the problem of decoder error propagation (DEP) in sliding window decoding (SWD) of protograph-based spatially coupled low- density parity-check (SC-LDPC) codes for large frame length or streaming applications. In particular, in order to avoid subdividing a long frame into a series of shorter frames by using termination to combat DEP, we consider altering the code design by introducing occasional doped symbols into the encoded sequence, where the doping is accomplished by fixing the values of all or some of the variable nodes (VNs) at certain positions in the protograph.An important practical consideration in many applications is the ability to use systematic encoding. This necessitates that no more than a fraction of the VNs at any given position can be doped, i.e., that fractional doping be employed. We begin by showing numerically that full doping of a single position in the protograph of a long frame improves performance relative to that of terminating the frame at half its length. We then show that fractional doping of consecutive VN positions at a given location in the protograph is comparable to full doping. We also show that spreading fractionally doped positions over multiple locations in the protograph results in additional gains, where the effective code rate of a doped frame is always at least as high as that of the shorter terminated frame.

## Serially Concatenated Codes for Data Center Networks

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11154486
- **Type**: conference
- **Published**: 18-22 Aug.
- **Authors**: Balázs Matuz, Emna Ben Yacoub, Stefano Calabrò
- **PDF**: https://ieeexplore.ieee.org/document/11154486
- **Abstract**: This work investigates channel code design for next-generation data center networks employing 448G/lane attachment unit interfaces (AUIs). A three-link problem, composed of an electrical, optical, and electrical link, representative of intra- and inter-data center links ranging from a few meters to a few kilometers, is considered. To address high error rates, serially concatenated Reed Solomon (RS) and Bose-Ray-Chaudhuri-Hocquenghem (BCH) codes, both located on the host chip, are proposed. The implementation complexity of different forward error correction (FEC) component codes is discussed, different decoding schemes are compared, and analytical and semi-analytical approximations of the error rates are presented.

## AI/ML Based Encoder and Decoder Design for PUCCH HARQ-ACK Payload

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11154632
- **Type**: conference
- **Published**: 18-22 Aug.
- **Authors**: Akash Doshi, Pinar Sen, Kirill Ivanov +5
- **PDF**: https://ieeexplore.ieee.org/document/11154632
- **Abstract**: Error control coding for the systems for the previous generations (2G to 5G) has assumed the inputs bits to be uniformly distributed. However, some sources such as downlink (DL) HARQ-ACK payload are inherently non-uniformly distributed. Hence, there is room for significant performance improvement by employing joint source channel coding design aided by deep learning based techniques. We focus on AI/ML based codebook learning and decoder design for HARQ-ACK payload in order to exploit the source distribution in the control channel codebook and perform Unequal Error Protection (UEP) for the source bits encoded in the codewords. Our results demonstrate 4 - 8 dB reduction in the transmit power required to achieve the desired ACK and NACK error rates, compared to the 5G NR compliant encoder and decoder design.

## Probabilistic Shaping in MIMO: Going Beyond 1.53dB AWGN Gain With the Non-Linear Demapper

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11154592
- **Type**: conference
- **Published**: 18-22 Aug.
- **Authors**: Kirill Ivanov, Wei Yang, Jing Jiang
- **PDF**: https://ieeexplore.ieee.org/document/11154592
- **Abstract**: Constellation shaping is a well-established method to improve upon a regular quadrature amplitude modulation (QAM). It is known that the gain achieved by any shaping method for an additive white Gaussian noise (AWGN) channel is upper-bounded by 1.53dB. However, the situation becomes less clear in the multiple-input and multiple-output (MIMO) setting.In this paper, we study the application of probabilistic shaping for MIMO channels. We utilize an efficient near-optimal demapper based on sphere decoding (SD) and demonstrate that it is possible to achieve more than 2dB gains, breaking the AWGN limit. It becomes possible because both signal and interference are shaped and the non-linear methods can capture this property and leverage on it to improve the demodulation performance.

## An Error-Threshold Based Joint Phase Estimation and Decoding Method for Non-Pilot-Aided Systems

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11296777
- **Type**: conference
- **Published**: 18-22 Aug.
- **Authors**: Jiawen Chen, Xuhui Ding, Xianchao Zhang +3
- **PDF**: https://ieeexplore.ieee.org/document/11296777
- **Abstract**: In 5G/6G communication environments, synchronization technologies encounter challenges including excessive pilot overhead, poor reliability at low signal-to-noise ratio (SNR), and limited estimation accuracy. This paper proposes a joint carrier recovery and iterative decoding algorithm based on weighted and normalized syndrome satisfaction probability (WNSSP). Our architecture implements parallel phase compensation through a multi-layer factor graph model. Within this framework, WNSSP dynamically weights and fuses belief provided by the soft low-density parity-check (LDPC) codes decoder to construct a maximum likelihood estimation function that simultaneously achieves carrier recovery and information reconstruction. To address the single-metric evaluation limitation, code-modified mean square error (CM-MSE) is established according to the residual phase error threshold, which enables concurrent assessment of synchronization accuracy and demodulation reliability. Simulations demonstrate that while effectively eliminating redundancy caused by pilot sequence, the proposed algorithm achieves 0.5–0.8 dB phase estimation gains and 0.15–0.5 dB bit error rate (BER) improvements compared with existing methods.

## Physical Layer Key Generation for 5G: Leveraging Dm-Rs Channel Estimation and Ldpc Soft-Decision Quantization for Key Reconciliation

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11199443
- **Type**: conference
- **Published**: 15-17 Aug.
- **Authors**: Hongyu Ye, Dengke Guo, Dongtang Ma +1
- **PDF**: https://ieeexplore.ieee.org/document/11199443
- **Abstract**: Physical layer key generation (PLKG) offers a lightweight and low-complexity key management solution for future emerging wireless communication networks. However, current PLKG schemes face challenges in effective integration with practical communication systems, hindering their practical deployment. To solve this problem, this paper proposes a key generation scheme integrated with the 5 G physical layer protocol, leveraging the Demodulation Reference Signal (DM-RS) to extract channel estimation for PLKG, enabling efficient key generation. Furthermore, a soft-decision quantization method based on Multibit Adaptive Quantization is proposed which makes key reconciliation input compatible with the soft-decision input requirements of the Low-Density Parity-Check (LDPC) decoder in 5G channel coding module. Simulation results demonstrate that the proposed scheme successfully integrates into the 5G standard communication framework while still maintaining favorable key disagreement rate (KDR) performance, the key reconciliation using keys derived by soft-decision quantization method can achieve better key agreement performance than using keys derived by binary quantization.

## Random Constructions of Girth-Eight QC-LDPC Codes with Structural Shaping

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11148129
- **Type**: conference
- **Published**: 10-13 Aug.
- **Authors**: Songyan Xue, Guohua Zhang
- **PDF**: https://ieeexplore.ieee.org/document/11148129
- **Abstract**: In order to construct girth-8 quasi-cyclic (QC) low-density parity-check (LDPC) codes with low encoding complexity, this paper introduces structural shaping techniques to generate QC-LDPC codes with two different structures. These two structures are QC-LDPC codes constructed with vertical symmetric structure and reverse structure without 4-cycles and 6-cycles. Novel constructions assume that the structures of the parity check matrix (PCM) are symmetric and reverse, respectively, and the greedy exhaustive search algorithm is used to find the exponent matrix with the smallest possible size P of the circulant permutation matrix (CPM). Due to its symmetrical and reverse structural characteristics, the representation of the new codes is more compact than other codes. The simulation results show that the proposed codes have certain competitiveness compared to existing QC-LDPC codes.

## Construction of QC-LDPC Codes with Product-like Exponent Matrices Based on Rectangular Area

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11148120
- **Type**: conference
- **Published**: 10-13 Aug.
- **Authors**: Jian Fang, Yuxiang Zhou, Min Zhu +1
- **PDF**: https://ieeexplore.ieee.org/document/11148120
- **Abstract**: This paper proposes a novel algorithm for constructing girth-8 quasi-cyclic (QC) LDPC codes with product-like (PL) exponent matrices, termed PL-QC-LDPC codes. To simplify the analysis of cycles in the Tanner graph of PL-QC-LDPC codes, we introduce the rectangular area (RA) and present an efficient semi-search RA algorithm to determine the minimum size of circulant permutation matrices (CPMs) in the exponent matrix. Moreover, search depth is employed to balance the trade-off between search complexity and optimization of the minimum CPM-size. Numerical results demonstrate that our proposed method, combined with masking method, can achieve smaller CPM-size and lower error floor than the greatest common divisor (GCD) method.

## Federated Transfer Learning for Two-Stage Decoding of LDPC Codes

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11244494
- **Type**: conference
- **Published**: 10-13 Aug.
- **Authors**: Linh Nguyen, Quoc Bao Phan, Cheol-Hong Min +1
- **PDF**: https://ieeexplore.ieee.org/document/11244494
- **Abstract**: The performance of fifth-generation (5G) coding techniques, such as low-density parity-check (LDPC) codes, is significantly affected by the error floor, which occurs in high signal-to-noise ratio (SNR) regions. Federated transfer learning (FTL), with its ability to learn from distributed data, can effectively improve error correction in low-SNR environments and extract crucial decoding features for high-SNR conditions. This paper introduces a two-stage decoding method that integrates layered LDPC decoding with FTL to mitigate the error floor and enhance system performance. Experimental results demonstrate that this approach significantly reduces error rates and improves decoding efficiency.

## Layered PEXIT-based Optimization of Puncturing Patterns for 5G-LDPC Codes in Few-Iteration Decoding

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11148138
- **Type**: conference
- **Published**: 10-13 Aug.
- **Authors**: Qiushi Xu, Ming Jiang, Qiang Wang
- **PDF**: https://ieeexplore.ieee.org/document/11148138
- **Abstract**: In this paper, an innovative method to optimize the puncturing patterns of the 5G low-density parity-check codes, which leverages layered protograph-based extrinsic information transfer (PEXIT) analysis to evaluate decoding performance and the progressive multi-path search (PMPS) algorithm to optimizing puncturing patterns. Compared with existing methods, layered PEXIT analysis is faster and more accurate, while the PMPS algorithm effectively addresses the local optimum trap commonly encountered by greedy algorithms. Simulation results demonstrate that using optimized puncturing patterns significantly improve the few-iteration decoding performance, thereby enhancing the reliability of resource-constrained communication systems without introducing any additional complexity.

## Systematic BMST-FTP Codes and Their Application to q-ary Erasure Channels

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11148182
- **Type**: conference
- **Published**: 10-13 Aug.
- **Authors**: Yaping Lv, Xiao Ma
- **PDF**: https://ieeexplore.ieee.org/document/11148182
- **Abstract**: In this paper, q-ary Fourier Transform Pair (FTP) codes over q-ary erasure channels are investigated. To improve the performance of FTP codes, we propose an encoding and decoding scheme based on block Markov superposition transmission. Specifically, the information symbols of FTP codes are transmitted directly, while the check symbols are transmitted in a superposition way. To analyze the performance, we present a Genie-Aided (GA) lower bound, which serves as a tool to set properly the encoding memory. Simulation results show that the proposed scheme can improve the performance of FTP codes, approaching the Shannon limit within 0.06 at the symbol erasure rate of 10−4. Particularly, the simulated performance matches the GA lower bounds in the low erasure probability region. With the same code rate and similar code length, the proposed scheme performs better than the non-binary low density parity check code.

## A Sub-block Interleaving Algorithm to Mitigate Pilot Interference in LDPC-coded AFDM Systems

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11148845
- **Type**: conference
- **Published**: 10-13 Aug.
- **Authors**: Siyuan Huang, Yin Xu, Tianyao Ma +5
- **PDF**: https://ieeexplore.ieee.org/document/11148845
- **Abstract**: High-power pilot symbols are essential for accurate channel state estimation in affine frequency division multiplexing (AFDM) systems, but they introduce significant interference to data symbols. While inserting guard intervals around the pilot symbols can reduce the impact of pilot interference, it comes at the cost of reduced spectral efficiency. This paper proposes a sub-block interleaving algorithm for low-density parity-check (LDPC)-coded AFDM systems that mitigates pilot interference while eliminating guard interval requirements. The algorithm provides differentiated protection at the sub-block level, ensuring sufficient protection for bits that are substantially impacted by pilot interference. The algorithm utilizes feedback from channel estimation and classifies interference-affected bits based on the proposed residual pilot interference model. LDPC sub-blocks are then ranked according to their protection capabilities, which are characterized by unequal error protection (UEP), and matched with the corresponding interference-affected bits. Simulation results demonstrate that the sub-block interleaving algorithm significantly improves bit error rate (BER) performance under various channel estimation conditions.

## Low-Complexity BP-ORBOSD Algorithm for Short 5G LDPC Codes

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11148135
- **Type**: conference
- **Published**: 10-13 Aug.
- **Authors**: Qianfan Wang, Yiwen Wang, Jiayi Yang +2
- **PDF**: https://ieeexplore.ieee.org/document/11148135
- **Abstract**: Belief propagation (BP) combined with ordered statistics decoding (OSD) achieves near-optimal frame error rate (FER) for short LDPC codes, but the extensive re-encoding overhead of OSD limits its practicality. To address this, we propose the BPORBOSD, a low-complexity and high-performance decoder that replaces conventional OSD with the ordered reliability bits OSD (ORBOSD), where the test error patterns are produced by the ORB technique. Moreover, in contrast to conventional BP-OSD, which directly adopts the soft information from standard BP into OSD after BP fails, we employ a modified BP scheme with a normalization factor α to produce soft reliability metrics better suited for ORBOSD. We derive the decoder’s complexity and demonstrate that, in the high-SNR regime, the average decoding complexity of BPORBOSD approaches that of standard BP. Simulation results confirm that BP-ORBOSD achieves FERs close to those of conventional BPOSD and the finite-length bound while significantly reducing the average number of re-encodings.

## Quasi-Cyclic Spatially Coupled LDPC Codes Construction with Girth Eight

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11148217
- **Type**: conference
- **Published**: 10-13 Aug.
- **Authors**: Shikui Guo, Guohua Zhang
- **PDF**: https://ieeexplore.ieee.org/document/11148217
- **Abstract**: Small cycles in spatially coupled low-density paritycheck (SC-LDPC) codes have a detrimental effect on the error floor. Recently, an explicit simple method has been proposed to construct a class of 4-cycle free SC-LDPC codes by partitioning a spreading matrix into a number of component matrices. Using a quasi-cyclic (QC) lifting, we propose a component matrices construction method to obtain QC-SC-LDPC codes with a girth eight in this paper. The component matrices of the new method are completely defined by a spreading matrix and an exponent matrix. The spreading matrix is constructed from a finite sequence of integers, and the exponent matrix is constructed from the greatest common divisor (GCD) framework. The novel construction method demonstrates the capacity to entirely eliminate 6-cycles. Compared to the recently proposed explicit structural design, the proposed code achieves a girth of eight and exhibits better bit-error rate (BER) performance.

## Low-complexity Decoding Method of Generalized LDPC with Polar Component Codes

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11148625
- **Type**: conference
- **Published**: 10-13 Aug.
- **Authors**: Wenxue Sun, Yin Xu, Hao Ju +5
- **PDF**: https://ieeexplore.ieee.org/document/11148625
- **Abstract**: Generalized low-density parity-check with polar component (GLDPC-PC) codes exhibit promising potential for 6G wireless systems with higher demands on reliability and data rate. The decoding method for GLDPC-PC codes involves belief propagation (BP), where the soft information of the component code is used as extrinsic information for check nodes. Although the Bahl-Cocke-Jelinek-Raviv (BCJR) decoding algorithm provides bitwise optimal soft information for linear block codes, its decoding complexity increases exponentially with the code length, making it impractical for applications. Therefore, the near-optimal soft-output successive cancellation list (SO-SCL) decoding with fixed scaling is proposed to reduce decoding complexity. However, the complexity of SO-SCL decoding still holds potential for further optimization. In this work, we propose an offline approximation of the unvisited probability codebook and a staged scaling strategy for the extrinsic information to reduce decoding complexity while maintaining low performance loss.

## An Improved Full Rank Condition for Nonbinary LDPC Codes over BI-AWGN Channel

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11148204
- **Type**: conference
- **Published**: 10-13 Aug.
- **Authors**: Yuhao Liu, Qin Huang
- **PDF**: https://ieeexplore.ieee.org/document/11148204
- **Abstract**: This paper improves the full rank condition (FRC) to construct nonbinary LDPC codes for binary AWGN channels, in which there is usually a one-bit error in one erroneous symbol. When assigning values to symbols in a cycle, our improved FRC condition not only considers rank deficiency, but also prefers values with the smallest probability that the related checks are mistakenly satisfied due to one-bit errors in these symbols. Finally, we present the IFRC-based optimization algorithm performs row-wise optimization on the non-zero elements of the parity-check matrix. Simulation results show the effectiveness of IFRC compared to FRC: the error-correcting performance is improved by 0.1dB to 0.5dB, and the error floor can be reduced by up to an order of magnitude.

## Adaptive Normalized Min-Sum Decoding Algorithm For LDPC Codes in Flash Memory

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11149292
- **Type**: conference
- **Published**: 10-13 Aug.
- **Authors**: Min Yu, Xiongfei Zhai, Mengxin Hu +3
- **PDF**: https://ieeexplore.ieee.org/document/11149292
- **Abstract**: For globally coupled low density parity check (GCLDPC) codes, the normalized Min-Sum (NMS) algorithm is a widely-used decoding algorithm but suffers from the degraded performance and the slow convergence speed. To address this issue, in this paper, by analyzing the relation between the bit error ratio (BER) and the degree of polarization of log-likelihood ratio (LLR) information, we propose an adaptive NMS decoding algorithm. In particular, the normalized factor is dynamically adjusted based on the average LLR information in the initial and the current iterations. Besides, the two-level decoding scheme is considered. Simulation results show that, in the additive white Gaussian noise (AWGN) channels and the flash memory channels, as compared with the NMS algorithm, our algorithm significantly improves the decoding performance and the convergence speed.

## A Fast Messages-Passing Algorithm for Counting Short Cycles in Bipartite Graphs

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11148122
- **Type**: conference
- **Published**: 10-13 Aug.
- **Authors**: Hong Chen, Xuan He
- **PDF**: https://ieeexplore.ieee.org/document/11148122
- **Abstract**: As short cycles have significant impact on the low-density parity-check (LDPC) decoding performance, counting short cycles for LDPC code graphs (more generally, for bipartite graphs) are important. In this paper, we first develop a new efficient implementation for the improved message-passing algorithm (IMPA) for counting short cycles of lengths between g and 2lmax in bipartite graphs for any given lmax ∈ [g/2, g − 1], where g is the girth. Building upon this, we further propose a fast message-passing algorithm (FMPA) by employing a level-wise activation strategy. The FMPA has storage complexity ${\mathcal{O}}(\delta |E|)$ and computational complexity ${\mathcal{O}}\left( {\left( {{l_{\max }} - g/2 + 1} \right)|E{|^2}} \right)$, where δ is the minimum of the maximum node degree of each partition and |E| is the number of edges. Extensive numerical results demonstrate that, the FMPA can always run significantly faster than the IMPA for any lmax, and generally run faster than the modified breadth-first search algorithm for lmax = g/2+1, g/2+2.

## Automation and High-Level Synthesis of Analog Computing Processors Based on Margin Propagation

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11244472
- **Type**: conference
- **Published**: 10-13 Aug.
- **Authors**: Ankita Nandi, Krishil Gandhi, Mahendra Pratap Singh +2
- **PDF**: https://ieeexplore.ieee.org/document/11244472
- **Abstract**: The Margin-Propagation (MP) is a paradigm for designing analog computing circuits that, like digital circuits, are scalable across biasing conditions and process nodes. Like digital circuits, MP-based analog circuits and systems are modular and robust to process, voltage, and temperature variations. These features make MP-based analog circuit design amenable to automation and high-level synthesis. This paper proposes such a design framework using factor graphs as the foundational descriptors to specify the interdependency between different analog computational primitives. Using Python scripting language, the proposed framework translates an input factor graph to its equivalent SPICE-compatible circuit netlist that can be used to validate the intended functionality using an MP-based messagepassing algorithm. The proposed framework also allows for the integration of design optimization strategies such as precision tuning, variable elimination, and mathematical simplification. We demonstrate the versatility of our framework for tasks such as Bayesian inference, Low-Density Parity Check (LDPC) decoding, and analog Artificial Neural Networks (ANN). Netlist simulation results align closely with software implementations, affirming the efficacy of our proposed automation tool.

## MAMP Detector for AFDM under Doubly Dispersive Channels

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11148104
- **Type**: conference
- **Published**: 10-13 Aug.
- **Authors**: Yilin Qi, Haoran Yin, Yanqun Tang +2
- **PDF**: https://ieeexplore.ieee.org/document/11148104
- **Abstract**: With the increasing demand for multi-carrier communication in high-mobility scenarios, it is urgent to design new multi-carrier communication waveforms that can resist large delay-Doppler spreads. Affine frequency division multiplexing (AFDM) is a promising solution for next-generation wireless access to achieve strong delay-Doppler spreads resilience in possible scenarios. By adjusting AFDM parameters to match the multipath delay and Doppler shift of the doubly dispersive channels, AFDM can obtain optimal diversity gain. However, AFDM encounters symbol dispersion in the underlying modulation domain, i.e., the discrete affine Fourier transform (DAFT) domain, which poses significant challenges for signal detection. To overcome this challenge, we proposed an efficient detector for AFDM based on the memory approximate message passing (MAMP) algorithm. It uses a memory matched filter (memory MF) to achieve a high-precision reconstruction of the original signal at the cost of low complexity. We compare the bit error ratio (BER) performance of the proposed MAMP and traditional linear minimum mean square error (LMMSE) detector, and simulation results show that MAMP significantly outperforms LMMSE under integral delay-Doppler conditions.

## Air-to-Water Optical Wireless Communication with a Photon-Counting Receiver

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11148665
- **Type**: conference
- **Published**: 10-13 Aug.
- **Authors**: Siyan Sun, Tianrui Lin, Tianjian Wei +5
- **PDF**: https://ieeexplore.ieee.org/document/11148665
- **Abstract**: In this paper, we establish an air-to-water optical wireless communication (A2W-OWC) through dynamic air-water interface, where the received signal can be characterized by discrete photons. We initially conduct numerical evaluations using Monte Carlo simulation. Subsequently, we conduct experiments in the swimming pool to observe the influence of waves on the signal and background radiation. The results verify that A2W-OWC system satisfies Poisson model. We investigate the performance improvement of adopting arrays at the transmitter and receiver.

## Lattice-based Linear Equalization for Single Carrier and Multi Carrier Transmission over Doubly Selective Channels

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11149328
- **Type**: conference
- **Published**: 10-13 Aug.
- **Authors**: Yuxin Lai, Tao Yang
- **PDF**: https://ieeexplore.ieee.org/document/11149328
- **Abstract**: This paper studies a lattice-based linear equalization (LLE) approach over doubly selective channels (DSCs). At the transmitter, the message sequence is encoded using a ring code, which is also a simple yet powerful lattice code. The resultant coded digits are one-to-one mapped to PAM symbols. The receiver carries out linear filtering and computes the a posteriori probabilities (APPs) of some integer linear combinations (ILCs) of the coded digits. Next the APPs of the ILCs are converted into APPs of the coded digits, which are then utilized for channel-code decoding. The optimized linear filter and and integer coefficient matrices for the proposed LLE based scheme are presented. Featuring a parallel processing architecture, our proposed LLE approach outperforms the traditional linear equalizers, such as linear minimum mean square error (MMSE) without significantly increased complexity. Further, we put forth a double-layer iterative (DLI) decoding method for a linear block codes coded LLE scheme. The integer coefficient matrices and the paritycheck matrix code are concatenated to form the effective Tanner graph, and based on which the soft-in-soft-out (SISO) decoding is carried out. Extensive numerical results demonstrate that the developed LLE approach achieves considerably improved bit error rate performance over DSCs for both single-carrier and multi-carrier systems.

## On Design of Interleave-Division Multiple Access with Correlated Sources

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11148657
- **Type**: conference
- **Published**: 10-13 Aug.
- **Authors**: Xu Li, Tao Yang, Rongke Liu +1
- **PDF**: https://ieeexplore.ieee.org/document/11148657
- **Abstract**: This paper proposes interleave-division multiple access with correlated sources (IDMA-CS) scheme. Message sequence of each user is compressed by distributed source coding (DSC). Then, compressed sequences are encoded, modulated and sent to a common base station (BS). The BS carries out multiuser detection (MUD) and DSC decoding to recover original message. We develop a separate DSC decoding and MUD (SDSC-MUD) method, which explicitly accounts for the impact of MUD and achieves an integrated processing framework. Further, we propose a “turbo-like” joint DSC decoding and MUD (JDSC-MUD) method that exploits the source correlation to facilitate MUD. It demonstrates that the proposed IDMA-CS scheme can increase the system load to more than 1.3~ 3 times that of conventional IDMA. Numerical results also validate the effectiveness of the JDSC-MUD method.

## Sparse Regression Codes for Covert Communication over Multiple Access Channels

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11148720
- **Type**: conference
- **Published**: 10-13 Aug.
- **Authors**: Haolin Jiang, Yiming Wang, Zhuangfei Wu +1
- **PDF**: https://ieeexplore.ieee.org/document/11148720
- **Abstract**: We study a covert multiple access channel (MAC) with two users. Specifically, each user aims to transmit a message through a noisy channel with a low probability of detection by the adversary. We propose two coding schemes based on sparse regression codes (SPARC), with either a joint approximate message passing (JAMP) decoder or a successive interference cancellation-AMP (SIC-AMP) decoder. Furthermore, we derive an upper bound for the transmission power with given noise power under covert constraint and perform several simulations. The results show that our schemes not only have near-optimal performance and low complexity under Gaussian noise but also perform consistently under other noise distributions.

## Efficient Realization of Multi-channel Visible Light Communication System for Dynamic Cross-Water Surface Channels

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11148852
- **Type**: conference
- **Published**: 10-13 Aug.
- **Authors**: Han Qi, Tianrui Lin, Tianjian Wei +5
- **PDF**: https://ieeexplore.ieee.org/document/11148852
- **Abstract**: This paper explores the transmission schemes for multi-channel water-to-air optical wireless communication (W2AOWC) and introduces a prototype of a real-time W2A-OWC system based on a field-programmable gate array (FPGA). Utilizing an LED array as the transmitter and an APD array as the receiver, the system establishes a multi-channel transmission module. Such configuration enables parallel operation of multiple channels, facilitating the simultaneous transmission of multiple data streams and enhancing overall throughput. The FPGA serves as a real-time signal processing unit, handling both signal transmission and reception. By integrating low-density parity-check (LDPC) codes from 5G New Radio, the system significantly boosts its detection capabilities for dynamic W2AOWC scenarios. The system also optimizes FPGA resource usage through time-multiplexing operation of an LDPC decoder’s IP core. To evaluate the system’s practicality, experiments were conducted under background radiation in an indoor water tank, measuring the frame error rate under both calm and fluctuating water surfaces. The experimental results confirm the feasibility and effectiveness of the developed W2A-OWC system.

## Low Complexity Turbo Receiver using Interference Sparsity for Massive MIMO

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11149269
- **Type**: conference
- **Published**: 10-13 Aug.
- **Authors**: Yanbo Yu, Linfeng Song, An-An Lu +2
- **PDF**: https://ieeexplore.ieee.org/document/11149269
- **Abstract**: In this paper, we propose a low complexity receiver for massive multiple-input multiple-output (MIMO) communications. We first introduce the beam based statistical channel model (BSCM). By using the sparsity of the beam domain channel and interference, we then derive the low-complexity turbo receiver, which reduces the complexity of the minimum mean square error (MMSE) receiver by reducing the dimension of matrix operations. We also present efficient implementation of the low-complexity turbo receiver. Simulation results show that the proposed receiver can achieve performance close to the MMSE turbo receiver with low computational cost.

## Data-Aided Learning for Multi-Antenna OFDM Systems with Superimposed Pilot in Time-Varying Channel

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11148898
- **Type**: conference
- **Published**: 10-13 Aug.
- **Authors**: Lin Zhao, Hongmei Kang, Fan Ding +1
- **PDF**: https://ieeexplore.ieee.org/document/11148898
- **Abstract**: Deep learning (DL) is now widely applied in the physical layer, with particular attention to end-to-end learning-based communication transceivers. In this paper, we focus on superimposed pilots and propose a novel data-aided end-to-end learning scheme, which is applied to orthogonal frequency division multiplexing (OFDM) systems in time and frequency selective fading environment. Specifically, we conduct multidimensional joint training including time-frequency, power, and geometric shaping of constellation. And we perform the end-to-end training on the transmitter and the proposed data-aided receiver, achieving more reliable data transmission in multi-antenna mobile scenarios.

## Iterative Equalization-Decoding Algorithm with Coded OTFS for LEO Satellite Communications

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11149322
- **Type**: conference
- **Published**: 10-13 Aug.
- **Authors**: Siyuan Bai, Jian Jiao, Yaosheng Zhang +3
- **PDF**: https://ieeexplore.ieee.org/document/11149322
- **Abstract**: To satisfy the stringent reliability requirements of next-generation wireless systems, low Earth orbit (LEO) satellite communication receivers must address the challenges posed by doubly-selective (time frequency) fading in satellite-terrestrial links, while ensuring seamless global connectivity. In this paper, we propose a novel iterative equalization-decoding algorithm integrated with coded orthogonal time frequency space (COTFS) to overcome the reliability limitations of conventional receivers. By leveraging the sparse channel estimation results obtained from COTFS signal processing in the delay-Doppler domain, we design a distributed equalization-decoding algorithm coupled with pathwise maximum ratio combining (MRC) to effectively mitigate interference. To address error propagation inherent in conventional iterative detection and balance reliability with complexity, we integrate ordered likelihood decoding (OLD) with a lowcomplexity implementation. Simulation results demonstrate that the proposed algorithm achieves superior reliability compared to conventional COTFS receivers.

## Temporal Context Based Video Semantic Transmission

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11144399
- **Type**: conference
- **Published**: 1-3 Aug. 2
- **Authors**: Yongda Fei, Haoge Jia, Sheng Wu +1
- **PDF**: https://ieeexplore.ieee.org/document/11144399
- **Abstract**: With the increasing demand for low-latency wireless video transmission applications, the limitations of classical separation-based coding schemes are difficult to effectively capture long-term dependencies and spatiotemporal correlations. To address this challenges, this paper proposes a novel approach called Temporal Context Based Video Semantic Transmission (TCVST) that effectively preserves motion and texture details across multiple scales. TCVST enhances both spatial and temporal accuracy, enabling the model to better captures non-uniform motion and texture variations. Experimental results show that our TCVST achieves better coding gain and Rate-distortion (RD) performance in various established metrics such as Peak Signal-to-Noise Ratio (PSNR) and Multiscale-Structure Similarity (MSSSIM). In terms of transmission performance under complex scene video datasets, the proposed TCVST method can save up to $44.4 \%$ of the channel bandwidth cost, compared to the classical H.264/H. 265 combined with low-density parity-check (LDPC) and digital modulation schemes.

## Development of an Optimized QuantumTechniques for Secure Remote Medical Image Sharing

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11252021
- **Type**: conference
- **Published**: 1-2 Aug. 2
- **Authors**: S. Princy Sophia Rani, Ahmad Abdelhafiz Ali Samhan, Ramisetti Venkata Rao +3
- **PDF**: https://ieeexplore.ieee.org/document/11252021
- **Abstract**: Secure remote sharing of medical images is essential for advancing telemedicine, accurate diagnostics, and collaborative healthcare delivery. The traditional cryptography techniques are fast turning to be susceptible to quantum computing risks and generally are less efficient in high throughput medical settings. To counter such a shortcoming, we present an innovative quantum-oriented solution that utilizes optimized methods of secure and real-time medical image transmission over a long-distance network. In this method, Quantum Key Distribution (BB84 protocol), hybrid cryptography, quantum informed optimization, and quantum steganography are used to provide efficient high-fidelity and low latency transmission of images. The QKD is used to securely create symmetric keys that are to be used in the AES 256 encryption of the image and Elliptic Curve Cryptography is applied so that the metadata can be kept confidential. Immutable and transparent access logs are kept by using the blockchain technology. In order to even improve the performance, a dynamically tuning encryption parameters using a Quantum Genetic Algorithm can be applied to eliminate the computing overhead. Experimental testing with NIH Chest X-ray dataset shows an average encryption and decryption speed of 38.1 milliseconds, with a success rate of more than 25% relative to the conventional post-quantum cryptographic system. The results of a secure transmission show a decrease in latency of 12.5% over the TLS-enhanced QKD. The system keeps the Quantum Bit Error Rate at less than 5% under realistic noise levels and retains more than 75% of the key material obtained. In quantum steganography, the level of accuracy to detect tampering is 98.6%, hence data integrity. The solution has shown the capability to integrate quantum-level security, computing performance, and regulatory durability to become a trusted and long-term process of safe sharing of medical images in modern healthcare systems.
