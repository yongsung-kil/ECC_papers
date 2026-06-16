# IEEE Xplore — 2022-10


## LDPC Codes Over GF(q) With Alterable Subset for PAPR Reduction in OFDM Systems

- **ID**: ieee:9837063
- **Type**: journal
- **Published**: Oct. 2022
- **Authors**: Yuxi Xia, Dejin Kong, Yu Xin +2
- **PDF**: https://ieeexplore.ieee.org/document/9837063
- **Abstract**: Non-binary low-density parity-check (NB-LDPC) codes can exhibit more considerable coding gain than their binary counterparts in numerous cases. To further exploit the benefit of NB-LDPC codes, in this letter, a novel type of non-binary LDPC codes, alterable subset non-binary LDPC (AS-NB-LDPC) codes, is proposed for reducing the peak-to-average power ratio (PAPR) of orthogonal frequency division multiplexing (OFDM) systems. Firstly, we design the alteration scheme of AS-NB-LDPC codes to make  $q$ -ary LDPC codes generate  $q$  valid codewords through one alterable subset, and the codeword with the minimum PAPR is selected for transmission. Then inspired by the invertible subset for binary LDPC codes, the necessary and sufficient conditions for alterable subset generation are derived. Furthermore, we propose an improved progressive edge growth (PEG) construction method to obtain AS-NB-LDPC codes with favorable frame error rate (FER) performance. Simulation results verify the effectiveness of the proposed NB-LDPC codes.

## On the Construction of QC-LDPC Codes Based on Integer Sequence With Low Error Floor

- **ID**: ieee:9810937
- **Type**: journal
- **Published**: Oct. 2022
- **Authors**: Xiongfei Tao, Xin Chen, Bifang Wang
- **PDF**: https://ieeexplore.ieee.org/document/9810937
- **Abstract**: Quasi-cyclic low-density parity-check (QC-LDPC) codes have efficient hardware implementation and excellent correcting performance. However, the existence of trapping sets can affect the decoding performance. In this letter, a novel class of QC-LDPC codes based on integer sequence with column weight 3 and girth at least 8 is proposed. If the numbers in the sequence are different, the QC-LDPC codes free of elementary trapping sets ( ${a}$ ,  ${b}$ ) with  ${a} \leq10$  and  ${b} \leq $  3 can be constructed. The row weight of the parity check matrix can be arbitrary and we give a lower bound of the circulant permutation matrix (CPM) size. Simulation results show that the generated codes have good performance with low error floor over AWGN channels.

## High-Throughput Non-Binary LDPC Decoder Architecture Using Parallel EMS Algorithm

- **ID**: ieee:9783462
- **Type**: journal
- **Published**: Oct. 2022
- **Authors**: Jeongwon Choe, Youngjoo Lee
- **PDF**: https://ieeexplore.ieee.org/document/9783462
- **Abstract**: Providing superior algorithm-level performance, the non-binary low-density parity-check (NB-LDPC) code is now expected to be one of the next-generation error-correction codes. However, it is hard to implement a high-throughput NB-LDPC decoder in practice due to its impractical processing complexity and the excessively long decoding time. Based on the previous extended min-sum (EMS) approach, in this work, we introduce the parallel EMS (pEMS) decoding algorithm that reduces the processing latency of each iteration by managing multiple message entries at a time. The previous two-phase node-level operation is modified to promote the proposed parallel processing without performance degradation, where the delay overheads are minimized by carefully optimizing the internal sorters with input attributes. In addition, the data accessing sequence is precisely adjusted to reduce the number of waiting cycles, further increasing the overall processing efficiency. Implemented in a 22-nm FinFET technology, as a result, the prototype two-parallel decoder for (160, 80) NB-LDPC codes operates at the speed of 950 MHz, achieving the decoding throughput of more than 7 Gb/s, which is 3.2 times faster than the state-of-the-art design.

## Adaptive Gradient Descent Bit-Flipping Diversity Decoding

- **ID**: ieee:9844740
- **Type**: journal
- **Published**: Oct. 2022
- **Authors**: Srdan Brkic, Predrag Ivaniš, Bane Vasić
- **PDF**: https://ieeexplore.ieee.org/document/9844740
- **Abstract**: In this letter we propose a novel framework for designing decoders, for Low-Density Parity Check (LDPC) codes, that surpasses the frame error rate performance of Belief-Propagation (BP) decoding on binary symmetric channels. Its key component is the adaptation method, based on the genetic optimization algorithm, that is incorporated into the recently proposed Gradient Descent Bit-Flipping Decoding with Momentum (GDBF-w/M). We show that the resulting decoder outperforms all state-of-the-art probabilistic bit-flipping decoders and, additionally, it can be trained to perform beyond BP decoding, which is verified by numerical examples that include codes used in IEEE 802.3an and 5GNR standards. The proposed framework provides a systematic method for decoder optimization without requiring knowledge of trapping sets. Moreover, it is applicable to both regular and irregular LDPC codes.

## A Universal Efficient Circular-Shift Network for Reconfigurable Quasi-Cyclic LDPC Decoders

- **ID**: ieee:9834322
- **Type**: journal
- **Published**: Oct. 2022
- **Authors**: Suwen Song, Hangxuan Cui, Zhongfeng Wang
- **PDF**: https://ieeexplore.ieee.org/document/9834322
- **Abstract**: Quasi-cyclic low-density parity-check (QC-LDPC) codes for modern communication standards usually have multiple code rates and block lengths. Therefore, reconfigurable LDPC decoders have received widespread attention, which require circular-shift networks to support various expansion factors. Besides, for inputs smaller than the network size, the circular-shift network is desired to process multiple frames in parallel to maximize hardware utilization efficiency. The increasing demands put severe challenges to low-complexity implementations of shift networks, especially for codes with numerous expansion factors, such as 5G LDPC codes. In this brief, we present a universal design of efficient reconfigurable circular-shift networks. Through an ingenious modification on the order of permutations, the generation of control signals is considerably simplified, leading to a significant reduction of area and critical path. Moreover, a hybrid architecture organically integrating different networks is proposed for further complexity reduction. Implementation results under TSMC 90 nm technology demonstrate that the proposed network can achieve 25% area reduction and 46% area-efficiency (AE) improvement over the state-of-the-art ones.

## ReShape: A Decoder for Hypergraph Product Codes

- **ID**: ieee:9799762
- **Type**: journal
- **Published**: Oct. 2022
- **Authors**: Armanda O. Quintavalle, Earl T. Campbell
- **PDF**: https://ieeexplore.ieee.org/document/9799762
- **Abstract**: The design of decoding algorithms is a significant technological component in the development of fault-tolerant quantum computers. Often design of quantum decoders is inspired by classical decoding algorithms, but there are no general principles for building quantum decoders from classical decoders. Given any pair of classical codes, we can build a quantum code using the hypergraph product, yielding a hypergraph product code. Here we show we can also lift the decoders for these classical codes. That is, given oracle access to a minimum weight decoder for the relevant classical codes, the corresponding  $[[n,k,d]]$  quantum code can be efficiently decoded for any error of weight smaller than  $(d-1)/2$ . The quantum decoder requires only  $O(k)$  oracle calls to the classical decoder and $O(n^{2})$  classical resources. The lift and the correctness proof of the decoder have a purely algebraic nature that draws on the discovery of some novel homological invariants of the hypergraph product codespace. While the decoder works perfectly for adversarial errors, that is errors of weight up to half the code distance, it is not suitable for more realistic stochastic noise models and therefore can not be used to establish an error correcting threshold.

## Polar Coded Repetition

- **ID**: ieee:9877856
- **Type**: journal
- **Published**: Oct. 2022
- **Authors**: Fariba Abbasi, Hessam Mahdavifar, Emanuele Viterbo
- **PDF**: https://ieeexplore.ieee.org/document/9877856
- **Abstract**: Constructing efficient low-rate error-correcting codes with low-complexity encoding and decoding has become increasingly important for applications involving ultra-low-power devices such as Internet-of-Things (IoT). To this end, schemes based on concatenating the state-of-the-art codes at moderate rates with repetition codes have emerged as practical solutions deployed in various standards. In this paper, we propose a novel mechanism for concatenating outer polar codes with inner repetition codes which we refer to as polar coded repetition. More specifically, we propose to transmit a slightly modified polar codeword by deviating from Arıkan’s standard  $2 \times 2$  Kernel in a certain number of polarization recursions at each repetition block. We show how this modification can improve the asymptotic achievable rate of the standard polar-repetition scheme, while ensuring that the overall encoding and decoding complexity is kept almost the same. The achievable rate is analyzed for the binary erasure channel (BEC) and additive white Gaussian noise (AWGN) channel. Moreover, we show that the finite-length performance of the polar coded repetition scheme under cyclic redundancy check (CRC) aided successive cancellation list (SCL) decoder over AWGN channel is better than the uncoded polar-repetition scheme at the cost of a slight increase in decoding complexity. We also compare the proposed scheme, in terms of performance and complexity, with other low-rate solution based on polar codes in the literature.

## Design of Practical Scrambling Schemes for Physical-Layer Security

- **ID**: ieee:9854138
- **Type**: journal
- **Published**: Oct. 2022
- **Authors**: Johannes Pfeiffer, Robert F. H. Fischer
- **PDF**: https://ieeexplore.ieee.org/document/9854138
- **Abstract**: In physical-layer security, coding and modulation are employed to prevent successful eavesdropping without the need for secret keys. Most promising coding approaches apply channel coding in combination with information-bit scrambling, which leads to error multiplication at the descrambling process. In this letter, the strategies of shift-register based scrambling and block-wise scrambling (using matrix multiplications) are assessed for a Gaussian wiretap channel scenario w.r.t. the security gap metric. We show that the former leads to an unequal protection of communicated message bits. This becomes apparent only upon the evaluation of individual bit positions’ error rates and security gaps. In contrast, the more general block scrambling enables schemes that provide equal protection. An optimized scrambling matrix design is presented, which yields the best error-rate performance. In addition to the theoretical examination of error propagation in the descrambling process, numerical results that combine low-density parity-check codes and scrambling support those findings.

## Low-Latency Nested Decoding for Short Generalized Integrated Interleaved BCH Codes

- **ID**: ieee:9794489
- **Type**: journal
- **Published**: Oct. 2022
- **Authors**: Zhenshan Xie, Yok Jye Tang, Xinmiao Zhang
- **PDF**: https://ieeexplore.ieee.org/document/9794489
- **Abstract**: Generalized integrated interleaved (GII) codes nest short BCH sub-codewords to form more powerful BCH codewords. They can potentially achieve hyper-speed decoding with excellent error-correction capability. In particular, short GII-BCH codes are among the best candidates for the new fast storage class memories (SCMs). Miscorrections severely degrade the performance of short GII-BCH codes. Although they were effectively mitigated in previous designs, the involved repeated Chien search and higher-order syndrome computation cause long latency. This brief proposes efficient and low-latency nested decoding schemes for short GII-BCH codes. A strategy is developed to select sub-words for further nested decoding to mitigate miscorrections by keeping track of the error locator polynomials, instead of waiting for the lengthy Chien search. Formulas are also derived to estimate the effects on the error-correcting performance. Besides, a low-complexity linear feedback shift register (LFSR) architecture is developed to accelerate the higher-order nested syndrome computation. For an example GII-BCH code targeting at SCMs, the proposed design reduces the worst-case nested decoding latency by 26% with 8.5% area overhead and negligible performance loss compared to prior methods.

## Joint CFO, Gridless Channel Estimation and Data Detection for Underwater Acoustic OFDM Systems

- **ID**: ieee:9797240
- **Type**: journal
- **Published**: Oct. 2022
- **Authors**: Lei Wan, Jiang Zhu, En Cheng +1
- **PDF**: https://ieeexplore.ieee.org/document/9797240
- **Abstract**: In this article, we propose an iterative receiver based on gridless variational Bayesian line spectra estimation (VALSE), named JCCD-VALSE, that jointly estimates the carrier frequency offset (CFO), the channel with high resolution and carries out data decoding. Based on a modularized point of view and motivated by the high resolution and low-complexity gridless VALSE algorithm, three modules named the VALSE module, the CFO estimation (CFO est.) module, and the decoder module are built. Soft information is exchanged between the modules to progressively improve the channel estimation and data decoding accuracy. Since the delays of multipath of the channel are treated as continuous parameters instead of on a grid, the leakage effect is avoided. Beside, the proposed approach is a more complete Bayesian approach as all the nuisance parameters, such as the noise variance, the parameters of the prior distribution of the channel, and the number of paths are automatically estimated. Numerical simulations and sea test data are utilized to demonstrate that the proposed approach performs better than the existing grid-based joint channel and data decoding approaches. Furthermore, it is also verified that joint processing, including CFO estimation, provides performance gain.

## Index Modulation Pattern Design for Non-Orthogonal Multicarrier Signal Waveforms

- **ID**: ieee:9760225
- **Type**: journal
- **Published**: Oct. 2022
- **Authors**: Yinglin Chen, Tongyang Xu, Izzat Darwazeh
- **PDF**: https://ieeexplore.ieee.org/document/9760225
- **Abstract**: Spectral efficiency improvement is a key focus in most wireless communication systems and achieved by various means such as using large antenna arrays and/or advanced modulation schemes and signal formats. This work proposes to further improve spectral efficiency through combining non-orthogonal spectrally efficient frequency division multiplexing (SEFDM) systems with index modulation (IM), which can efficiently make use of the indices of activated subcarriers as communication information. Recent research has verified that IM may be used with SEFDM to alleviate inter-carrier interference (ICI) and improve error performance. This work proposes new SEFDM signal formats based on novel activation pattern designs, which limit the locations of activated subcarriers and enable a variable number of activated subcarriers in each SEFDM subblock. SEFDM-IM system designs are developed by jointly considering activation patterns, modulation schemes and signal waveform formats, with a set of solutions evaluated under different spectral efficiency scenarios. Detailed modelling of coded systems and simulation studies reveal that the proposed designs not only lead to better bit error rate (BER) but also lower peak-to-average power ratio (PAPR) and reduced computational complexity relative to other reported index-modulated systems.

## NOMA Joint Channel Estimation and Signal Detection Using Rotational Invariant Codes and GMM-Based Clustering

- **ID**: ieee:9825630
- **Type**: journal
- **Published**: Oct. 2022
- **Authors**: Ayoob Salari, Mahyar Shirvanimoghaddam, Muhammad Basit Shahab +2
- **PDF**: https://ieeexplore.ieee.org/document/9825630
- **Abstract**: This letter studies the joint channel estimation and signal detection for the uplink power-domain non-orthogonal multiple access. The proposed technique performs both detection and estimation without the need of pilot symbols by using a clustering technique. We apply rotational-invariant coding to assist signal detection at the receiver without sending pilot symbols. We utilize Gaussian mixture model (GMM) to automatically cluster the received signals without supervision and optimize decision boundaries to improve the bit error rate (BER) performance. Simulation results show that the proposed scheme without using any pilot symbol achieves almost the same BER performance as that for the conventional maximum likelihood receiver with full channel state information.

## Age-Optimal Network Coding HARQ Transmission Scheme for Dual-Hop Satellite-Integrated Internet

- **ID**: ieee:9806312
- **Type**: journal
- **Published**: Oct. 2022
- **Authors**: Jian Jiao, Shiqi Liu, Jing Ding +4
- **PDF**: https://ieeexplore.ieee.org/document/9806312
- **Abstract**: In the upcoming satellite-integrated Internet, a noted limitation is the non-trivial propagation latency due to the long distances. To support the emergent timeliness applications, information must be transmitted within a short end-to-end latency. Hence, the traditional hybrid automatic repeat request (HARQ) strategies with frequent feedbacks do not fit anymore, because the reliable transmission needs retransmission of the lost packets, which inevitably leads to the low efficiency in the satellite-integrated Internet. In this paper, we propose an age-optimal network code HARQ (NC-HARQ) transmission scheme with the metric of information timeliness, i.e., age of information (AoI) to realize limited/no feedback dual-hop reliable transmission in the satellite-integrated Internet. We derive the closed-form expression for the average and peak AoI of the proposed dual-hop age-optimal NC-HARQ transmission scheme, and also the expression for the benchmark schemes through establishing a finite-state Markov chain. Then, by taking account of the time-varying channel and the characteristics of random update of data file, two dynamic forward transmission strategies are further designed. Simulation results illustrate that our dual-hop age-optimal NC-HARQ transmission scheme can achieve lower average and peak AoI in comparison with several state-of-the-art HARQ schemes.

## Symbol-Wise Puncturing for HARQ Integration With Probabilistic Amplitude Shaping

- **ID**: ieee:9843915
- **Type**: journal
- **Published**: Oct. 2022
- **Authors**: Li Shen, Yongpeng Wu, Derrick Wing Kwan Ng +2
- **PDF**: https://ieeexplore.ieee.org/document/9843915
- **Abstract**: In this letter, we propose a symbol-wise puncturing scheme to support hybrid automatic repeat request (HARQ) integrated probabilistic amplitude shaping (PAS). To prevent the probability distribution distortion caused by the traditional sequential puncturing and realize the promised gain of PAS, we perform symbol-wise puncturing on the label sequence of the shaped modulation symbols. Our simulation results indicate that the proposed puncturing scheme achieves a stable shaping gain across the signal-to-noise ratio of at least 0.6 dB compared with the uniform case under the same throughput, while the gain of sequential puncturing drops rapidly with retransmissions. Moreover, in each transmission, the proposed scheme is able to reduce the distribution distortion that achieves over 1.2 dB gain at a block error rate (BLER) of  $\boldsymbol {10^{-3}}$ . In contrast, for sequential puncturing, the distribution is severely distorted and the BLER performance is even worse than that of the uniform case in retransmissions.

## NoD: A Neural Network-Over-Decoder for Edge Intelligence

- **ID**: ieee:9793711
- **Type**: journal
- **Published**: Oct. 2022
- **Authors**: Arash Fouman Ajirlou, Farid Kenarangi, Eli Shapira +1
- **PDF**: https://ieeexplore.ieee.org/document/9793711
- **Abstract**: The ubiquitous applications of the Internet of Things (IoT) devices and the increasing computational capabilities of neural networks (NNs) have led to a new era of edge computing and a paradigm known as edge intelligence (EI). With EI, the goal is to maximize the utilization of resources available within an edge device, offloading only the most compute-intensive operations to the cloud. In this article, we propose to leverage the close similarity between the internal architecture of a typical network decoder and an NN for deep learning on decoders. The proposed NN-over-decoder is developed in Verilog and synthesized on field-programmable gate array (FPGA). Based on experimental results, the system exhibits power consumption of the same order of magnitude as a baseline decoder and negligible memory overhead while increasing local hardware utilization, alleviating the high communication load in typical communication devices, and offering scalable multiply–accumulate (MAC)/cycle performance compared with the state of the art.

## Achievable-Rate-Aware Retention-Error Correction for Multi-Level-Cell NAND Flash Memory

- **ID**: ieee:9586047
- **Type**: journal
- **Published**: Oct. 2022
- **Authors**: Yingcheng Bu, Yi Fang, Guohua Zhang +1
- **PDF**: https://ieeexplore.ieee.org/document/9586047
- **Abstract**: Owing to the effect of data retention noise in multi-level-cell NAND flash memory, the initial threshold-voltage distributions and read voltages can no longer be used to accurately calculate log-likelihood ratios (LLRs) as the retention time increases, thus causing retention errors. To solve this problem, we first utilize the so-called “correction factors” to optimize the LLR accuracy by maximizing the achievable rate of a flash-memory system without introducing extra memory-sensing operations. We further prove that the optimization of the correction factors is a convex optimization problem and can be solved analytically. To obtain the optimal correction factors, we propose two retention-error correction schemes, referred to as offline maximum-achievable-rate correction (MARC) algorithm and online MARC algorithm, which enable the flash-memory controller to utilize the corrected LLRs that are stored in a look-up table and correct the inaccurate LLRs in real time, respectively. Motivated by the variation characteristics of the threshold-voltage distributions, we also propose an enhanced expectation–maximization (EM) algorithm to reestimate their corresponding parameters, and then adjust the read voltages. By combining the enhanced EM algorithm with the MARC algorithms, an enhanced EM-based correction strategy is developed to further boost the retention-error endurance of flash memory while avoiding excessive memory-sensing overhead. Theoretical analyses and simulation results illustrate the superiority of the proposed correction mehtods in terms of the robustness against retention errors.

## Low-Complexity Detection for Multidimensional Codebooks Over Fading Channels

- **ID**: ieee:9751366
- **Type**: journal
- **Published**: Oct. 2022
- **Authors**: Juliana Camilo Inácio, Bartolomeu F. Uchôa-Filho, Didier Le Ruyet
- **PDF**: https://ieeexplore.ieee.org/document/9751366
- **Abstract**: Signal space diversity (SSD) introduced by Boutros and Viterbo tremendously improves the error performance over fading channels without any power or bandwidth sacrifice. Maximum benefit is obtained with full diversity (FD) multidimensional codebooks and the rather complex maximum likelihood (ML) detection. In the present work, we propose a generalized combinatorial representation and an associated low-complexity list-based detection algorithm that works for any non-full or full diversity multidimensional codebook. The algorithm includes three options of lists offering different complexity-performance trade-offs. One of the lists has random size and is guaranteed to contain the ML point, while the other two lists have fixed or limited size. Some analytical results are presented for the list sizes. The algorithm also includes a smart search to find the most probable codebook point in the list. Numerical results show that the proposed algorithm yields optimal or close-to-optimum performance with a noteworthy detection complexity reduction. Therefore, its adoption can be of practical interest, especially in applications where powerful error-correcting codes are not supported.

## Channel Condition and Outage Performance of Mode-Division-Multiplexing Enabled MIMO System With Zero-Forcing Receiver

- **ID**: ieee:9826733
- **Type**: journal
- **Published**: Oct. 2022
- **Authors**: Yi Lei, Qi Lu, Bin Chen +1
- **PDF**: https://ieeexplore.ieee.org/document/9826733
- **Abstract**: Reusing the widely deployed multimode fibers (MMFs) in buildings to transmit multiple-input multiple-output (MIMO) signals via mode-division multiplexing (MDM) is an attractive solution to provide low-cost indoor wireless coverage. However, due to the random mode coupling, MMF channel varies over time. In this letter, the MDM-based MMF MIMO channel condition for different fiber lengths is studied. Next, the influence of the fluctuation of channel condition on the outage performance of the MIMO system with zero-forcing receiver is analyzed, in terms of information-theoretic capacity and practical error probability. Finally, by using adaptive coded modulation (according to channel condition), the MDM-based  $3 \times 3$  MIMO channel achieves up to 8.62 bit/s/Hz spectral efficiency with 10% outage probability.

## EXIT-Aided Scheduled Iterative MIMO Detection Under Non-Homogeneous Antenna Propagation Gain Scenarios

- **ID**: ieee:9803283
- **Type**: journal
- **Published**: Oct. 2022
- **Authors**: Huan Li, Jing Guo, Xinyi Wang +2
- **PDF**: https://ieeexplore.ieee.org/document/9803283
- **Abstract**: The non-homogeneous antenna propagation gain, potentially caused by the diverse large-scale fading effects in wireless communication channels, has a significant impact on the reliabilities of multiple-input multiple-out (MIMO) systems. We propose to utilize extrinsic information transfer (EXIT) to analyze the convergence characteristic of the factor graph (FG) based iterative MIMO detection mechanisms in an effective way. Based on the EXIT analysis, we propose a low-complexity scheduled algorithm for FG-based iterative MIMO detection, which speeds up the convergence of the mutual information exchange between the variable nodes and the observation nodes. To address the complexity issue in 5G new radio (NR) systems, where low-density parity check (LDPC) codes are adopted for data transmission, we also extend the proposed algorithm to concatenated detection and decoding in MIMO-LDPC systems to achieve low complexity. Simulation results show that the convergence speed of MIMO detection can be improved by at most 50%, while for the MIMO-LDPC system, the proposed algorithm can achieve 2 dB gain compared to the conventional minimum mean square error (MMSE) detection mechanism.

## Discrete MMSE Precoding for Multiuser MIMO Systems With PSK Modulation

- **ID**: ieee:9767673
- **Type**: journal
- **Published**: Oct. 2022
- **Authors**: Erico S. P. Lopes, Lukas T. N. Landau
- **PDF**: https://ieeexplore.ieee.org/document/9767673
- **Abstract**: We propose an optimal MMSE precoding technique using quantized signals with constant envelope. Unlike the existing MMSE design that relies on 1-bit resolution, the proposed approach employs uniform phase quantization and the bounding step in the branch-and-bound method is different in terms of considering the most restrictive relaxation of the nonconvex problem, which is then utilized for a suboptimal design also. We also propose robust MMSE designs where we exploit second order statistics of a channel state information mismatch. Moreover, unlike prior studies, we propose three different soft detection methods and an iterative detection and decoding scheme that allow the utilization of channel coding in conjunction with low-resolution precoding. Besides an exact approach for computing the extrinsic information, we propose two approximations with reduced computational complexity. Numerical simulations show that utilizing the MMSE criterion instead of the established maximum-minimum distance to the decision threshold yields a lower bit-error-rate in many scenarios. Furthermore, when using the MMSE criterion, a smaller number of bound evaluations in the branch-and-bound method is required for low and medium SNR. Finally, results based on an LDPC block code indicate that the proposed receive processing schemes yield a lower bit-error-rate compared to the conventional design.

## Work-in-Progress: Prediction-based Fine-Grained LDPC Reading to Enhance High-Density Flash Read Performance

- **ID**: ieee:9933162
- **Type**: conference
- **Published**: 7-14 Oct. 
- **Authors**: Yajuan Du, Yuan Gao, Qiao Li
- **PDF**: https://ieeexplore.ieee.org/document/9933162
- **Abstract**: LDPC codes have been widely applied in high-density flash memories, e.g., TLC flash and QLC flash, to ensure data reliability. In order to reduce the read latency of high-density flash memories, this paper proposes a prediction-based fine-grained LDPC reading method, named as PreLDPC. From a preliminary study, we observe that the ratio of cells that lie in error-prone areas (i.e., the areas between two adjacent cell states) is closely related to the final read level for successful decoding. Based on this observation, PreLDPC predicts the read level for LDPC reading, which could avoid excessive unnecessary read-retries. Furthermore, a fine-grained read method with fine sub-levels is used in the read-retry iteration for read latency reduction. From experimental results over real-world workloads on Disksim with SSD extensions, the effectiveness of PreLDPC on reducing read latency is verified in high-density flash memories.

## Work-in-Progress: High-Precision Short-Term Lifetime Prediction in TLC 3D NAND Flash Memory as Hot-data Storage

- **ID**: ieee:9933059
- **Type**: conference
- **Published**: 7-14 Oct. 
- **Authors**: Xiaotong Fang, Meng Zhang, Yifan Guo +6
- **PDF**: https://ieeexplore.ieee.org/document/9933059
- **Abstract**: In this paper, read disturb (RD) at various program/erase (P/E) stages has been thoroughly explored, and short-term lifetime prediction models of RD and endurance are proposed. Based on these, a new short-term warning system (STWS) is proposed, which can extend the lifetime of 3D NAND-based storage by adjusting LDPC codes dynamically. The experimental result shows that the proposed prediction models have high reliabilities, and STWS can effectively prolong the lifetime of NAND flash.

## Reliable and energy-efficient transmission scheme based on error correction codes and clustered routing protocol for WSN

- **ID**: ieee:9934530
- **Type**: conference
- **Published**: 6-7 Oct. 2
- **Authors**: Ikram Daanoune, Abdennaceur Baghdad
- **PDF**: https://ieeexplore.ieee.org/document/9934530
- **Abstract**: WSNs are getting to occupy a large part of daily life for many applications such as healthcare, military, environment, home, and so forth. Sensor nodes in WSNs are powered by small batteries and can be deployed in a hostile environment, where replacing or recharging them is difficult. As a result, WSNs are energy-constrained. In this context, several routing protocols are proposed to extend the network lifetime and optimize energy consumption. However, routing protocols can not guarantee communication reliability. To achieve the high-reliability requirements of data transmitted using the routing protocols, using channel coding in the physical layer is proposed. For this purpose, a comparative study is carried out in this work by comparing two different modern coding techniques, namely LDPC and RS coding. The objective of this paper is to determine which coding scheme better satisfies the requirements of clustered routing protocols, in particular the LEACH protocol. Simulations have shown that LDPC coding achieves good reliability performance over RS when implemented with the LEACH protocol by increasing the coding gain by 62.5% at a BER of 10−2.

## High Throughput FPGA Implementation of LDPC Decoder Architecture for DVB-S2X Standard

- **ID**: ieee:9976733
- **Type**: conference
- **Published**: 3-7 Oct. 2
- **Authors**: E. A. Likhobabin, A. A. Ovinnikov, R. S. Goriushkin +2
- **PDF**: https://ieeexplore.ieee.org/document/9976733
- **Abstract**: This paper is devoted to the design of a decoder structure for Quasi-Cyclic (QC) Low-Density Parity-Check (LDPC) codes of the DVB-S2X standard. The quasi-cyclic form of the matrix representation is the most convenient for the hardware implementation of the LDPC decoder, so the matrices of the DVB-S2X standard are converted to the QC form. The implementation of an LDPC decoder for the DVB-S2X standard is a challenging task, especially because of the long code words and large parity-check matrices. We propose a highly parallel FPGA implementation of LDPC decoder design based on the layered architecture and Min-Sum decoding algorithm. The structure of the decoder consists of 360 parallel cores responsible for the sequential calculation of variable-to-check (VTC), check-to-variable (CTV) messages and update posterior probabilities (APPs). Block RAM memory was used to store intermediate values of APP and CTVs. The decoder design is applicable to all code rates and allows to achieve throughput up to 500 Mbps at a clock frequency of 250 MHz

## High-Speed SC Decoder for Polar Codes achieving 1.7 Tb/s in 28 nm CMOS

- **ID**: ieee:9939603
- **Type**: conference
- **Published**: 3-5 Oct. 2
- **Authors**: L. Lopacinski, A. Hasani, G. Panic +4
- **PDF**: https://ieeexplore.ieee.org/document/9939603
- **Abstract**: This paper compares three hardware variants of successive cancelation (SC) decoders for polar codes. The fastest implementation, based on the basic SC, provides decoding throughput up to 1700 Gb/s, when implemented in a 28 nm CMOS technology at the worst-case timing corner. This is the fastest polar decoder published so far, to the best of our knowledge. We also discuss the difficulties of implementing single-parity-check nodes and repetition nodes in fast simplified SC (Fast-SSC) decoding algorithm. These two node types are the primary sources of clock frequency reduction, and special care needs to be taken when these elements are implemented. The Fast-SSC decoder requires ~3 times fewer hardware resources than the base version of SC, but achieves ~10% lower decoding throughput.

## High-Performance Hardware Accelerators for Next Generation On-Board Data Processing

- **ID**: ieee:9939616
- **Type**: conference
- **Published**: 3-5 Oct. 2
- **Authors**: Antonis Paschalis, Panagiotis Chatziantoniou, Dimitris Theodoropoulos +2
- **PDF**: https://ieeexplore.ieee.org/document/9939616
- **Abstract**: Hyperspectral imaging is a key remote sensing technology. The explosive growth in hyperspectral image data volume (several TBs per orbit) and instrument data rates (in the range of 20 Gbps), compete with limited available on-board storage resources and downlink bandwidth, making hyperspectral image data compression a mission critical on-board data processing task. In order to provide continuous and reliable data transfer from the on-board systems to the ground stations, channel coding is being applied at the end of the data processing pipeline to guarantee reliable communications even at low signal-to-noise ratio regimes. Moreover, erasure correcting codes working on information packets rather than bits or symbols, can provide downlink reliability in future RF and optical links especially when Automatic Repeat Queuing (ARQ) strategies are either problematic or impossible due to specific service delay constraints and intermittent connectivity. Committed to the vision for "Space Technology Designed in Greece", in this special session paper, we provide an overview of cutting-edge technology high-performance hardware accelerators developed in the NKUA Digital Systems and Computer Architecture Laboratory (DSCAL), applicable to next-generation payloads for earth observation, optical/RF communication and connectivity, including CCSDS hyperspectral image compression and channel-coding at bit-level and packet-level.

## Highly Efficient FDD Secret Key Generation using ESPRIT and Jump Removal on Phase Differences

- **ID**: ieee:9947224
- **Type**: conference
- **Published**: 3-5 Oct. 2
- **Authors**: Ehsan Olyaei Torshizi, Utkrist Uprety, Werner Henkel
- **PDF**: https://ieeexplore.ieee.org/document/9947224
- **Abstract**: In this study, a highly efficient simple approach to generate secret keys for Frequency-Division Duplexing (FDD) systems is proposed. We use phase differences between neighboring antennas in a linear array to construct the channel profile and the ESPRIT (Estimation of Signal Parameters using Rotational Invariance Techniques) algorithm for estimating the direction of arrival (DOA). In order to increase the channel reciprocity, we approximate the frequency behavior of the phase differences by polynomial curve-fitting. Rather than using unwrapping to prevent jumps, we propose two jump-removing and outlier-correction algorithms which can bring the efficiency to 100 %. Numerical results verify that the measurements have a minimum variance after using both proposed pre-processing algorithms. Furthermore, the corrected version of measurements has perfect efficiency and better performance on curve-fitting results and key disagreement rate.

## Design and Implementation of Hard-Decision LDPC Decoder

- **ID**: ieee:10011285
- **Type**: conference
- **Published**: 28-31 Oct.
- **Authors**: Yi Dong, Huimin Du, Shengfei Bai +3
- **PDF**: https://ieeexplore.ieee.org/document/10011285
- **Abstract**: Hard-decision LDPC decoders are widely used in communication and storage systems due to their simple circuits. However, existing hard decision LDPC decoding circuits lead to slow decoding convergence due to flipping according to the maximum energy value, reducing decoding performance. This paper proposes the Dual-Energy Probabilistic Gradient Descent Bit-Flipping (DPGDBF) hard-decision algorithm. If the energy value of the variable node reaches the threshold, all nodes with the threshold energy will be flipped, and the node with the sub-maximum threshold energy will be flipped with a certain probability. otherwise, only all variable nodes with the maximum energy value are flipped. The simulation results show that, in a limited iterative range, compared with Tabu-list Random-Penalty Gradient Descent Bit-Flipping (TRGDBF), for (2048, 1024) codes, the average number of decoding iterations of the algorithm is reduced by 12%, and the decoding performance is improved to a certain extent; for (9216,7680) codes, the average number of decoding iterations of the DPGDBF algorithm is reduced by 18%, and the decoding performance is improved by 4 times. In addition, this paper proposes a hardware implementation of the DPGDBF algorithm for (2048, 1024) codes, with a maximum clock frequency of 305.53MHz and a through-put of 19.52Gbps.

## Improvement of Chaotic Image Encryption Method Based on LDPC Code

- **ID**: ieee:10066764
- **Type**: conference
- **Published**: 28-30 Oct.
- **Authors**: Ya-He Zhao, Zhong-Xun Wang
- **PDF**: https://ieeexplore.ieee.org/document/10066764
- **Abstract**: Chaotic image encryption algorithm based on Low-Density Parity-Check (LDPC) code algorithm has the problem of high complexity and poor real-time performance. We choose the quasi-cyclic Low-Density Parity-Check (QC-LDPC) code instead of the Gallagher code in the algorithm and achieve better results than the previous one, especially in high-intensity noise. The watermark obtained by this method has high attack resistance and more resource saving in hardware. The QC-LDPC used in this paper is a code word constructed by the Fibonacci sequence, which has the advantages of small storage space, high flexibility, and high performance. Its excellent performance is also proved by its application in digital watermarking technology, which provides a reference for applying LDPC codes in more directions. Meanwhile, the practical applicability of LDPC digital image watermarking is further improved.

## Performance Improvement in Cellular V2X (CV2X) by Using Low Density Parity Check (LDPC) Code

- **ID**: ieee:9965719
- **Type**: conference
- **Published**: 26-29 Oct.
- **Authors**: Utpal Kumar Dey, Robert Akl, Robin Chataut
- **PDF**: https://ieeexplore.ieee.org/document/9965719
- **Abstract**: Cellular Vehicle-to-Everything (CV2X) has recently piqued the interest of both industry and academia. CV2X extends communication coverage by using the cellular infrastructure as a standard for vehicular communication. CV2X also enables the communication between vehicles and pedestrians, vehicles and the cellular network, along with vehicle to vehicle communication. The CV2X standard’s expectations are gradually rising as the number of vehicles, cell phone users, smart devices connected to vehicles, and other factors increase. A more efficient CV2X framework is needed to fulfill these expectations. We focused on the PHY layer of the CV2X standard and proposed a model featuring Low Density Parity Check (LDPC) code. Our experimental results suggest that our proposed model is able to improve reliability by reducing the bit error rate compared to the existing PHY layer framework. In addition, our proposed model can increase the throughput up to 1.4 times and 2 times at 10 MHz and 20 MHz channels, respectively.

## Blind Recognition of Convolutional Codes: A Matrix Transformation-Aided Deep Learning Approach

- **ID**: ieee:9984596
- **Type**: conference
- **Published**: 25-27 Oct.
- **Authors**: Yao Wang, Hongyu You, Xiang Wang +1
- **PDF**: https://ieeexplore.ieee.org/document/9984596
- **Abstract**: This paper focuses on the blind recognition of convolutional codes, a significant research problem in cognitive radios and signal interception. The existing methods based on deep learning (DL) usually directly take the received sequence as the input of a network, of which the recognition accuracy for high-rate convolutional codes is often poor. An identification framework called MT-CNN, combining matrix transformation with convolutional neural networks (CNN), is proposed in this paper. We offer a novel matrix transformation algorithm of which the result can highlight the differences between different encoders. Our proposed MT-CNN method adopts a feature fusion strategy, employing the codeword matrix and its feature map obtained through matrix transformation as the network's input. Simulations show that the proposed approach could provide significant improvements compared to existing methods, especially for the convolutional codes with a high rate.

## Impulsive Noise Suppression and Concatenated Code for OFDM Underwater Acoustic Communications

- **ID**: ieee:9984322
- **Type**: conference
- **Published**: 25-27 Oct.
- **Authors**: Gang Tan, Shefeng Yan, Binbin Yang
- **PDF**: https://ieeexplore.ieee.org/document/9984322
- **Abstract**: Underwater acoustic (UWA) information transmission is vulnerable to the interference of impulsive noise, which has short duration, high energy and random occurrence, decreasing the reliability of the orthogonal frequency-division multiplexing (OFDM) systems seriously. In this paper, we introduce the symmetric alpha stable (SαS) distribution to model the underwater impulsive noise firstly, and verifies the accuracy by measured noise data. For strong impulsive interference, an adaptive window median filter algorithm based on Chebyshev inequality (AWMF-C) is proposed, which applies the Chebyshev inequality twice to filter out the impulses and designs an adaptive window median filter to suppress them. Secondly, the serial concatenated code with RS code as outer code and interleaver are applied to suppress the residual impulsive interference further. Simulation results show that the proposed algorithm can suppress impulsive noise effectively, and the concatenated coding system given in this paper can further reduce the bit error rate (BER) of the communications system under impulsive noise background.

## MIMO TFT-OFDM for Underwater Acoustic Communication with Bidirectional Soft Decision Feedback Equalization

- **ID**: ieee:9984271
- **Type**: conference
- **Published**: 25-27 Oct.
- **Authors**: Zihao Ye, Shefeng Yan, Binbin Yang
- **PDF**: https://ieeexplore.ieee.org/document/9984271
- **Abstract**: Conventional underwater acoustic multiple input multiple output orthogonal frequency division multiplexing (MIMO-OFDM) system adopts orthogonal pilots, which leads to low spectral efficiency. In this paper, we propose an iterative time-frequency training OFDM (TFT-OFDM) scheme for underwater acoustic MIMO systems to improve spectral efficiency. Each TFT-OFDM symbol contains the time-domain training sequence and frequency-domain orthogonal pilots. The time-domain training sequence is used to estimate the path delays without eliminating the influence of OFDM symbols. By using the estimated path delays and the sparse characteristics of the underwater acoustic channel, the path amplitudes can be obtained with fewer pilots. In addition, the bidirectional soft decision feedback equalizer (BiSDFE) is introduced into the underwater acoustic MIMO system. BiSDFE eliminates intercarrier interference from both directions by combining the results of forward and backward decision feedback equalization to mitigate error propagation. Simulation results demonstrate that the proposed MIMO TFT-OFDM system achieves better bit error rate (BER) performance and higher spectral efficiency than the MIMO ZP-OFDM system.

## An Improved Codec Design Architecture for Irregular LDPC Codes Applicable to WiMAX

- **ID**: ieee:9970908
- **Type**: conference
- **Published**: 24-26 Oct.
- **Authors**: Divita Shri, Arijit Mondal, Shayan Srinivasa Garani
- **PDF**: https://ieeexplore.ieee.org/document/9970908
- **Abstract**: We propose the design architecture of the Low-density parity-check (LDPC) encoder and decoder based on the WiMAX standard (IEEE 802.16e). The design architectures were implemented on a Kintex-7 KC705 field-programmable gate array (FPGA) kit, for a rate 1/2 WiMAX LDPC code with a code length of 2304, containing twelve layers in the parity check matrix. A new null bypassing logic for irregular LDPC decoder is proposed. The tool reported a total power of 0.677 W for encoder with a throughput of 364 Gbps. The tool reported a total power of 1.009 W for the decoder with a throughput of 0.0785 Gbps (78.5 Mbps) for five iterations. Our architecture is also amenable for constructing non-binary LDPC codes where each bit of the non-binary code is binary coded and interleaved, useful for applications in optical transmission channels. Our architecture is also scalable for a wide range of quasi-cyclic code parameters.

## A Fast Decoding Convergence of SISO Repetition - QC-LDPC Codes Concatenated at the Receiver

- **ID**: ieee:9942436
- **Type**: conference
- **Published**: 22-24 Oct.
- **Authors**: Amr Tarek, Amr Abdelaziz, Hisham Al–Dahshan
- **PDF**: https://ieeexplore.ieee.org/document/9942436
- **Abstract**: Low-Density Parity Check (LDPC) is one of the contemporary error-correcting codes that has shown near Shannon capacity performance; it has been implemented into various stan-dards such as the second-generation Digital Video Broadcasting for Satellite (DVB-S2) and eventually made its way toward the 5G New Radio (NR) for the data channel. In an effort to enhance the LDPC decoding performance without a significant increase in the decoding complexity, in this paper, a receiver-based concatenated decoding approach is proposed, which is composed of the soft-input soft-output (SISO) repetition and offset min-sum (OMS) algorithm representing outer and inner decoders, respectively. At the receiver, the received signal is oversampled with an oversampling rate (OSR) faster than multiple integers of the Nyquist rate to produce repeated symbols. Moreover, the repetition employed at the receiver to handle the repeated symbols will not impact the coding rate. Finally, the simulation results revealed that the proposed scheme could accomplish faster-decoding convergence compared to the conventional LDPC decoders and achieve coding gain up to 2.3 dB with OSR = 2. Additionally, the computational complexity does not increase significantly; on the contrary, the achieved gain can be exploited to reduce the number of iterations.

## Modified Noisy Gradient Descent Bit-Flipping Decoding Algorithms for LDPC Codes

- **ID**: ieee:9942999
- **Type**: conference
- **Published**: 20-22 Oct.
- **Authors**: Yidong Li, Wai M. Tam, Francis C.M. Lau
- **PDF**: https://ieeexplore.ieee.org/document/9942999
- **Abstract**: In this paper, we propose modified multi-bit noisy gradient descent bit flipping (M-NGDBF) algorithms for decoding low-density parity-check codes. To simplify the decoder design, we eliminate the use of Gaussian noise generators at the decoder and replace them with received signals after simple transformations. We then improve the convergence rate by removing the randomness in the M-NGDBF algorithm during the first few iterations. Subsequently, we construct a tabu-list to record bits that are flipped in the current iteration and allows these bits to be flipped in the next iteration only with a very small probability. Simulation results show that our proposed algorithms outperform the original M-NGDBF algorithm in terms of both bit error rate and convergence rate.

## Log-likelihood Ratio for Low-Density Parity-Check Codes Under Binary Symmetric Erasure Channel in DNA Storage

- **ID**: ieee:9943019
- **Type**: conference
- **Published**: 20-22 Oct.
- **Authors**: Xiaozhou Lu, Sunghwan Kim
- **PDF**: https://ieeexplore.ieee.org/document/9943019
- **Abstract**: Due to the DNA storage system has the advantages such as high densities, longevityand efficient data duplication, more and more researchers have already focused on it. The writing/reading cost is an important indicator of the efficiency of synthesis and sequencing process. In this paper, we kept the encoding and decoding of LDPC unchanged for fair comparison. However, we propose a binary symmetric erasure channel (BSEC) model for the DNA storage system since substitution and deletion errors occurred during the synthesis and sequencing process. And then, the corresponding log-likelihood ratio (LLR) is calculated by observed error statistics under the BSEC model to achieve the lower reading cost, which is the input of the decoder for low-density parity-check (LDPC) code. Since an exact DNA channel model has not been proposed and the mismatch between the observed and theoretical error statistics, a scaling method for LLR is proposed, which can achieve a lower reading cost for DNA storage. We present the relation between total substitution and deletion error rates and scaling coefficients by curve fitting methods. From the simulation results, we can obtain that the performance of our proposed scheme is equal to or slightly better than that from the conventional scheme.

## Detecting Minimum Distance of LDPC Codes with Improved Approximately Nearest Codeword Method

- **ID**: ieee:9950957
- **Type**: conference
- **Published**: 20-21 Oct.
- **Authors**: Zhewei Tong, Kewu Peng, Zhitong He
- **PDF**: https://ieeexplore.ieee.org/document/9950957
- **Abstract**: Approximately nearest codeword (ANC) is a classic approach for detecting minimum distance of low-density parity-check (LDPC) codes. With the principle of local search, ANC method is capable of detecting minimum distance of LDPC codes within acceptable time. However, the message passing (MP) decoding algorithm and scheduling scheme, as well as the local search strategy, still have much space to improve. To fill the gap, this paper proposes an improved-ANC method which employs novel noise introduction method, decoding algorithm, scheduling scheme and searching strategy, to accelerate the computation of the minimum distance of LDPC codes significantly. Finally, we run simulations on LDPC codes in Wi-Fi5 and 5G-NR standards. The simulation results are presented and demonstrate the effectiveness of our proposal.

## A 3D-DCT and Convolutional FEC Approach to Agile Video Streaming

- **ID**: ieee:9973675
- **Type**: conference
- **Published**: 19-23 Oct.
- **Authors**: Han Yang, Xiangyu Chen, Xi Chen +4
- **PDF**: https://ieeexplore.ieee.org/document/9973675
- **Abstract**: On today's Internet, including both wide area networks and wireless access networks, multimedia content (images, audio and video) represents a dominating fraction of network data traffic. Efficient encoding and transmission of multimedia data are of considerable importance to smooth operation of the network as well as quality of experience of network users. Wireless users particularly prefer algorithms that are both robust, and lightweight in terms of computation and communication. This work takes a holistic approach to source compression and network transmission of videos. A 3D-DCT module is employed for spatio-temporal compression of pixel cubes, working in concert with a convolutional network coding module, for unequal error protection and forward error correction. We outline the overall framework for such a joint algorithm design, discuss detailed algorithm blocks, while many interesting design choices are still open for future exploration.

## An Adaptive Fault-Tolerant Transmission Mechanism for CMT in Unreliable Wireless Networks

- **ID**: ieee:9973471
- **Type**: conference
- **Published**: 19-23 Oct.
- **Authors**: Wenfeng Du, Liqian Lai, Kaishun Wu
- **PDF**: https://ieeexplore.ieee.org/document/9973471
- **Abstract**: Concurrent multipath transfer (CMT) using SCTP can improve the transmission ability of multi-homed devices such as smartphones and laptops with multiple heterogeneous network interfaces. However, the unreliable nature of wireless network makes the performance of concurrent multipath transfer significantly worsen. To address this issue, we propose an adaptive fault-tolerant transmission mechanism to reduce the impact brought by packet loss, which tries to avoid chunk retransmission with specialized forward error correction and adjusts the redundant rate dynamically according to the transmission loss rate. A chunk forwarding algorithms for CMT is also presented to minimize the impact of long-term path error. The simulation results demonstrate that the proposed fault-tolerant transmission mechanism outperforms the standard SCTP and CMT association in most scenarios, especially in unreliable networks.

## List-Based Detector and Access Points Selection in Cell-Free Massive MIMO Using LDPC Codes

- **ID**: ieee:9940407
- **Type**: conference
- **Published**: 19-22 Oct.
- **Authors**: Tonny Ssettumba, Roberto B. Di Renna, Lukas T.N. Landau +1
- **PDF**: https://ieeexplore.ieee.org/document/9940407
- **Abstract**: This paper proposes a cell-free massive multiple-input multiple-output (CF-mMIMO) architecture with joint list-based detection with soft interference cancellation (soft-IC) and access points (APs) selection. In particular, we derive a new closed-form expression for the minimum mean-square error receive filter while taking the uplink transmit powers and APs selection into account. This is achieved by optimizing the receive combining vector by minimizing the mean square error between the detected symbol estimate and transmitted symbol, after canceling the multi-user interference (MUI). By using low-density parity check (LDPC) codes, an iterative detection and decoding (IDD) scheme based on a message passing is devised. In order to perform joint detection at the central processing unit (CPU), the access points locally estimate the channel and send their received sample data to the CPU via the front haul links. In order to enhance the system's bit error rate performance, the detected symbols are iteratively exchanged between the joint detector and the LDPC decoder in log likelihood ratio form. Furthermore, we draw insights into the derived detector as the number of IDD iterations increase. Finally, the proposed list detector is compared with existing detection techniques.

## Low-Complexity Architecture of Finding First Four Minimum Values for Non-binary LDPC Decoders

- **ID**: ieee:10031266
- **Type**: conference
- **Published**: 19-22 Oct.
- **Authors**: Thang Xuan Pham, Phap Duong-Ngoc, Hanho Lee +1
- **PDF**: https://ieeexplore.ieee.org/document/10031266
- **Abstract**: Looking for a set of minimum values is considering as an important part in reducing the computational complexity introduced by the conventional non-binary low-density parity-check (NB-LDPC) decoding algorithms. In which, looking for a set of four min-value has been using i $n$ recent NB-LDPC decoders. In this paper, a low-complexity architecture is proposed for the first four minimum values finder. Experimental results confirmed that the proposed design is able to achieve a high flexibility in adapting to changing input sequence size while maintaining a low hardware complexity.

## Low Power Decoder Architecture of Product Code for Storage Controller

- **ID**: ieee:10031469
- **Type**: conference
- **Published**: 19-22 Oct.
- **Authors**: Sumin Kim, Byungmin Ahn, Bohwan Jun +3
- **PDF**: https://ieeexplore.ieee.org/document/10031469
- **Abstract**: Error correction codes (ECCs) are essential for correcting the errors caused by the physical characteristics of 3D NAND flash in flash solution products. In this paper, we introduce low power decoder architecture for product code. Precisely, by using Hamming product code and Chase-Pyndiah algorithm, this work takes not only the same correction capability and area as low-density parity-check decoder, but also less power with relatively simple operation for decoding. Only the log likelihood ratios of error-suspicious bits are gathered in SRAM for the next iteration of decoding, so that the power consumption and area of SRAM read/write decrease. Compared with the conventional ECC decoder with the same correction capability and area, our decoder has achieved an average power reduction of 22.4%.

## A DNN-based Decoding Scheme for Communication Transmission System over AWGN Channel

- **ID**: ieee:9940380
- **Type**: conference
- **Published**: 19-22 Oct.
- **Authors**: Meilin He, Yanchao Lei, Huina Song +3
- **PDF**: https://ieeexplore.ieee.org/document/9940380
- **Abstract**: A communication transmission system with channel coding and deep neural network (DNN)-based decoding is considered. A DNN-based decoding scheme is proposed for reliable transmission. The decoding scheme is accomplished by efficient local decoding at all the neurons and interactions in the input, hidden and output layer. Specifically, firstly, the nonlinear operations at each neuron and the linear operations of the weights and biases at each edge are performed by the local decoding. Secondly, the weights and biases are updated by gradient descent (GD) algorithm, based on the estimated loss value. This process above is performed iteratively until the message sequence has been recovered. Simulation results show that our proposed decoding scheme performs well. Moreover, our decoding scheme performs significantly better than the conventional hard decision.

## The Effect of PEG-Lifting Order on the Performance of Protograph GLDPC Codes

- **ID**: ieee:9943671
- **Type**: conference
- **Published**: 19-21 Oct.
- **Authors**: Dae-Young Yun, Jae-Won Kim, Jong-Seon No
- **PDF**: https://ieeexplore.ieee.org/document/9943671
- **Abstract**: Generalized low density parity check (GLDPC) codes can be constructed by replacing some single parity check (SPC) nodes in LDPC codes with generalized constraint (GC) nodes. GC nodes are defined by component codes whose minimum distance is larger than that of SPC nodes. Therefore, the variable nodes (VNs) connected to GC nodes, which are called doped VNs, are more protected than the undoped VNs. Due to this effect, we observe that the doped VNs are more robust to local cycles. The distribution of local cycles is affected by the processing VN order of the progressive edge growth (PEG) algorithm, where the latter processed (lifted) VNs tend to have more local cycles. Based on the property of doped VNs and the PEG algorithm, we show that a tangible performance gain is achieved by placing the doped VNs in the latter order of the PEG algorithm compared to the former order. The performance gain is shown with a well known GLDPC code in the literature and over both the binary erasure channel and addictive white Gaussian noise channel.

## Current Trends on Deep Learning-aided Channel Coding

- **ID**: ieee:9952535
- **Type**: conference
- **Published**: 19-21 Oct.
- **Authors**: Tuyet-Mai Dang, Eunyoung Cho, Sang-Hyo Kim
- **PDF**: https://ieeexplore.ieee.org/document/9952535
- **Abstract**: Artificial intelligence (AI)-aided approaches are emerging in solving physical layer communication problems. In this paper, we focus on applications of deep learning (DL) in channel coding for wireless communications and provide a survey on related topics. We describe various decoding problems of short linear codes and LDPC codes assisted by deep neural networks. The survey will be concluded with a list of future research directions.

## Sneak Path Aware Bit-Flipping Algorithm for ReRAM Crossbar Array

- **ID**: ieee:9952863
- **Type**: conference
- **Published**: 19-21 Oct.
- **Authors**: Myungin Kim, Jeongseok Ha
- **PDF**: https://ieeexplore.ieee.org/document/9952863
- **Abstract**: Resistive random access memory (ReRAM) has unique features such as fast data processing speed, non-volatility and high density and thus has been gaining popularity in a wider range storage applications. Meanwhile, ReRAM suffers from read errors mainly due to the variations of cell resistance and the sneak path problem. There have been efforts to cope with the read errors using error-correcting codes such as low-density parity-check (LDPC) codes and Bose-Chaudhuri-Hocquenghem (BCH) codes. In this paper, we propose a simple bit-flipping (BF) decoding algorithm for correcting read errors in ReRAM due to the sneak paths and show that the proposed algorithm efficiently resolves the sneak path problem at reduced complexity. In particular, we assume that ReRAM provides certain side information about the reliability of retrieved bits, and the proposed algorithm utilizes the side information in the decoding. Error-rate performance of the proposed algorithm is compared with that of an existing BF algorithm, which shows a clear performance improvement with the proposed one.

## Selective Layered BP Decoding for low-latency NR LDPC Codes

- **ID**: ieee:9952457
- **Type**: conference
- **Published**: 19-21 Oct.
- **Authors**: Chanho Yoon, Woncheol Cho, Young-Jo Ko
- **PDF**: https://ieeexplore.ieee.org/document/9952457
- **Abstract**: In this paper, we propose selective layered BP decoding approach for decoding 3GPP NR rate compatible punctured LDPC codes that eliminates the ambiguity of BP decoding for information bit punctured codes. Conventional BP or layered BP decoding approach for NR LDPC codes does not perform well in frequency selective fading channels, and, with the sub iteration applying to the sub matrix portion, the proposed SL layered BP decoding improves the performance drastically. We show that faster decoding speed by applying the proposed scheme to the 3GPP NR LDPC code is achieved in terms of decoding latency.

## LDPC coded massive MIMO systems with FG-GAI BP detector

- **ID**: ieee:9952680
- **Type**: conference
- **Published**: 19-21 Oct.
- **Authors**: Han Jin Park, Jeong Woo Lee
- **PDF**: https://ieeexplore.ieee.org/document/9952680
- **Abstract**: In this paper, We design the LDPC code in the Massive MIMO system. We use EXIT analysis for efficient LDPC code design. We use FG-GAI-BP detection techniques suitable for low complexity. We make sure that LDPC code design methods exhibit good performance with low complexity.

## Performance Analysis of QC-LDPC codes constructed by using Golomb rulers

- **ID**: ieee:9943662
- **Type**: conference
- **Published**: 19-21 Oct.
- **Authors**: Daekyeong Kim, Inseon Kim, Hyunwoo Cho +2
- **PDF**: https://ieeexplore.ieee.org/document/9943662
- **Abstract**: In this paper, we analyzes performance of girth-8 regular QC-LDPC codes constructed using Golomb ruler. We conducted simulations to measure FER performance of QC-LDPC codes constructed by changing the last mark of some optimal Golomb ruler and found the value of the mark that shows the best performance.

## Evaluation of the Effects of SEUs on Configuration Memories in FPGA Implemented QC-LDPC Decoders

- **ID**: ieee:9962337
- **Type**: conference
- **Published**: 19-21 Oct.
- **Authors**: Zhen Gao, Yinghao Cheng, Pedro Reviriego
- **PDF**: https://ieeexplore.ieee.org/document/9962337
- **Abstract**: LDPC codes are widely used in wireless communication systems for reliable data transmission due to their excellent error correction capabilities. SRAM-FPGAs are a popular option for the implementation of LDPC decoders due to their excellent computing capabilities and re-configurability. However, when applied in critical environments, e.g. space platforms, the SRAM-FPGA based LDPC decoders will suffer single-event upsets (SEUs) that can cause failures and disrupt communications. Therefore, analyzing the reliability of LDPC decoders to SEUs on the FPGA is important. This paper first analyzes the effects of SEUs on different parts of the FPGA implemented LDPC decoder based on the module functions, including the influence of the parallelism on the decoder reliability. Then fault injection experiments are performed to validate the conclusions of the analysis. Experiment results show that about 98% of SEUs on the configuration memories can be tolerated by the decoder itself, and the modules with more interconnections are less robust to SEUs. In addition, the reliability of LDPC decoders decreases for lower levels of parallelism due to the larger computation load of each unit. These results will be a valuable input to design efficient SEU protection schemes for LDPC decoders.

## Implementation for JSCC Scheme Based on QC-LDPC Codes

- **ID**: ieee:10014340
- **Type**: conference
- **Published**: 18-21 Oct.
- **Authors**: Longyu Ma, Chiu Wing Sham, Jia Zhan +1
- **PDF**: https://ieeexplore.ieee.org/document/10014340
- **Abstract**: In this paper, we explored the feasibility of implementing a JSCC system using LDPC codes in an FPGA. QC-LDPC codes were employed instead of normal LDPC codes. Also, 6-bit quantization has been applied in the proposed system. The performance test and the synthesized logic usage confirmed the implementation.

## The IEEE 802.15.13 Standard for Optical Wireless Communications in Industry 4.0

- **ID**: ieee:9968724
- **Type**: conference
- **Published**: 17-20 Oct.
- **Authors**: Kai Lennert Bober, Eric Ackermann, Ronald Freund +3
- **PDF**: https://ieeexplore.ieee.org/document/9968724
- **Abstract**: Multiple standardization activities have been started for optical wireless communications. In this paper, we summarize the ongoing work in the IEEE P802.15.13 task group. The goal is to make optical wireless communication usable for specialty applications, e.g., in industrial wireless networks. The current draft standard defines a medium access control (MAC) sublayer, supporting deterministic channel access for low latency/jitter through dynamic time division multiple access (TDMA), distributed multiple-input multiple-output (MIMO) operation for increased robustness, as well as two physical layers for high spectral efficiency and long reach, respectively. Currently, the specification is being finalized for publication. It is prepared for future updates to add support for the group of time-sensitive networking (TSN) standards. In this paper, we provide an overview over the upcoming standard.

## Real-time Video Transmission through Underwater MIMO Acoustic Communication Channels

- **ID**: ieee:9977135
- **Type**: conference
- **Published**: 17-20 Oct.
- **Authors**: Xiyuan Zhu, Jinfeng Li, Y. Rosa Zheng
- **PDF**: https://ieeexplore.ieee.org/document/9977135
- **Abstract**: Video transmission requires 100 kbps – 500 kbps channel capacity which presents tremendous challenges over underwater acoustic wireless channels. This paper implements a prototype of a 4-by-4 multiple-input multiple-output (MIMO) acoustic transmitter and receiver at the carrier frequency of 200 kHz, and achieves an information data rate of 100 kbps. The transmitter prototype is capable of real-time video transmission at 2 - 8 frames per second using H.264 video compression. The receiver uses a multi-core CPU for base-band processing and can achieve real-time recovery of transmitted videos with 2 frames per second.

## Bit-Level Informed Dynamic Scheduling for Decoding Non-binary LDPC Codes

- **ID**: ieee:10683923
- **Type**: conference
- **Published**: 17-19 Oct.
- **Authors**: Chia-Hao Lin, Tzu-Hsuan Huang, Chung-Hsuan Wang +1
- **PDF**: https://ieeexplore.ieee.org/document/10683923
- **Abstract**: Non-Binary Low-Density Parity-Check (NB-LDPC)codes have excellent error rate performance, which outperform their binary counterpart for short and moderate code length. In this work, we propose the first bit-level informed dynamic scheduling decoding algorithm for NB-LDPC codes in binary field. The simulation results show that the proposed decoding algorithm can provide about 1.2 dB gain compared to the state-of-the-art adaptive full bit-reliability-based algorithm (FBRBA). Moreover, the performance can be close to the symbol-based extended min-sum (EMS) decoding algorithm.

## A Class of Cyclic Partial Geometries and Their Associated Constant Weight and LDPC Codes

- **ID**: ieee:10683925
- **Type**: conference
- **Published**: 17-19 Oct.
- **Authors**: Juane Li, Yi Gong, Xin Xiao +2
- **PDF**: https://ieeexplore.ieee.org/document/10683925
- **Abstract**: This paper presents a class of cyclic partial geometries, called triplet partial geometries, which are constructed based on finite fields of characteristic 2. Using these partial geometries, constant-weight codes and LDPC codes with cyclic and quasi-cyclic structure are constructed.

## Lossy Source Coding of Binary Memoryless Source by Trained LDGM Encoder

- **ID**: ieee:10683905
- **Type**: conference
- **Published**: 17-19 Oct.
- **Authors**: Kazuki Ogawa, Hiromu Takata, Motohiko Isaka
- **PDF**: https://ieeexplore.ieee.org/document/10683905
- **Abstract**: Use of low-density generator matrix codes as codebook and encoding with message-passing algorithm is an efficient approach for lossy coding of the i.i.d. binary source. We propose lossy source encoder which is trained on the associated unfolded Tanner graph for improving the rate-distortion performance and/or reducing computational cost.

## Some Girth-8 Linear Code is a 3-SEQ LRC

- **ID**: ieee:10683941
- **Type**: conference
- **Published**: 17-19 Oct.
- **Authors**: Zhi Jing, Hyojeong Choi, Hong-Yeop Song
- **PDF**: https://ieeexplore.ieee.org/document/10683941
- **Abstract**: In this paper, we prove that a linear code with girth 8 is a 3-seq LRC with locality r if its parity-check matrix has row weight at most r + 1 and column weight at least 2.

## Implementation of Multi Bit Error Detection and Correction using Low Density Parity Check Codes

- **ID**: ieee:9970166
- **Type**: conference
- **Published**: 15-16 Oct.
- **Authors**: Banoth Suman, M. Jagadeesh Chandra Prasad
- **PDF**: https://ieeexplore.ieee.org/document/9970166
- **Abstract**: Data transmission in advanced space communications are suffering with the different types of noises. Further, these noises cause burst errors in data. Thus, the low-density parity checking codes (LDPC) plays the major role to detect and correct the errors. However, the conventional hamming encoders, decoders were detected and corrected only one bit error. Therefore, this work implementation the Multi-Bit Error Detection and Correction Codes (MBE-DCC) for multiple bits error detection and correction. Initially, MBE-DCC encoding operation is implemented by using generator matrix, which contains both identity bits and parity bits. Then, encoded code word is transmitted into the channel of space communication, where encoded data corrupted by different types of noises, errors. Therefore, the MBE-DCC decoding operation performed at receiver side of space communications, which corrected all the errors using syndrome detection, error location detection, and error correction modules. The simulations revealed that the proposed MBE-DCC resulted in superior performance than conventional LDPC methods.

## Decoder Implementation of Spatially Coupled LDPC Codes

- **ID**: ieee:9998153
- **Type**: conference
- **Published**: 14-16 Oct.
- **Authors**: Jian Yang, Danfeng Zhao, Hai Tian +2
- **PDF**: https://ieeexplore.ieee.org/document/9998153
- **Abstract**: In order to meet the requirements of high reliability and high flexibility of wireless communication, the Space-coupled Low-Density Parity-Check (SC-LDPC) codes are deeply studied. At present, the main research direction of SC-LDPC codes is to reduce the complexity of the algorithm and reduce the occupation of decoding resources. In terms of hardware implementation, there is relatively little research. Therefore, in view of the above problems, considering hardware resource occupation and coding and decoding performance, the FPGA design and implementation of the SC-LDPC code codec are carried out, and the functional correctness test is carried out on the Xilinx xc7k325tffg900-2 chip.

## An Improved Hybrid LDPC Decoder over Rayleigh Fading Channel

- **ID**: ieee:10013650
- **Type**: conference
- **Published**: 12-14 Oct.
- **Authors**: Reza Biazaran, Hermann J. Helgert
- **PDF**: https://ieeexplore.ieee.org/document/10013650
- **Abstract**: Soft decision decoders applicable to low density parity check codes such as sum product algorithms provide excellent error performance, however, it comes at the expense of computational complexity. Additionally, many iterations may be required of these decoders to achieve desired error performance. The processing delay associated with too many iterations may be a drawback for cases where low latency is a critical requirement. Conversely, performance of hard decision decoders such as bit flipping decoder and its variants, while improved, generally are not on par with that of soft decision decoders. Such decoders also require many iterations to achieve a given error performance. We have proposed a two-stage hybrid decoder with a simplified sum product algorithm (SPA) in the first stage, and an improved noisy gradient decent bit flipping decoder in the second stage. We have shown that our proposed hybrid decoder outperforms the legacy individual decoders, studied in this paper, from error performance point of view as well as required number of iterations that will reduce the overall network latency.

## Turbo Codes in Satellite Communication

- **ID**: ieee:9986805
- **Type**: conference
- **Published**: 12-14 Oct.
- **Authors**: Juntao Ni
- **PDF**: https://ieeexplore.ieee.org/document/9986805
- **Abstract**: This article introduces the basic principle of turbo codes and the basic overview of satellite communication system and analyzes the feasibility of turbo codes in satellite communication and proves its unique advantages over other coding methods in satellite communication through simulation. Finally, we analyze the performance of multiple turbo codes and discuss the feasibility of their application in satellite communication by combining the previous studies and make limitations on their performance above triple turbo codes.

## OpenAirInterface as a platform for 5G-NTN Research and Experimentation

- **ID**: ieee:10056682
- **Type**: conference
- **Published**: 10-14 Oct.
- **Authors**: Sumit Kumar, Ashish Kumar Meshram, Abdelrahman Astro +12
- **PDF**: https://ieeexplore.ieee.org/document/10056682
- **Abstract**: Technical advancements and experimental works for the integration of 5G and Non-Terrestrial Networks (NTN) have gained significant traction over the past few years. NTN components have been officially included in the 5G ecosystem by 3GPP in the latest Release-17. 5G-NTN research is ongoing and it is desirable to have a platform that facilitates quick prototyping of the proof-of-concept methods. OpenAirInterface(OAI) is an open-source experimental yet 3GPP standard-compliant Software Defined Radio (SDR) based protocol stack that has been widely known for implementing 4G/5G technologies. Due to its proven capabilities and flexibility, OAI is currently in the developmental process of integrating adaptations for the 5G-NTN. In this work, we discuss the peculiar features of OAI which are shaping it towards becoming a preferred tool for research and experimentation related to 5G-NTN. We provide details of completed/ongoing 5G-NTN projects leveraging OAI to achieve their objectives. In particular, we discuss 5G-GOA and 5G-LEO where critical adaptations in OAI are being done to support 5G-NTN use-cases. Such adaptations enable direct-access between UE and gNB via transparent payload Geostationary (5G-GOA) and Non-geostationary satellites (5G-LEO). Both projects have closely followed 3GPP discussions over 5G-NTN and the adaptations are compliant with the currently frozen 3GPP Release-17. OAI adaptations from both projects will be merged into the main development branch of OAI. We also provide a future roadmap of OAI towards 5G-NTN development. We believe that the pioneering steps taken in the course of the aforementioned projects will establish OAI as a preferred tool for 5G-NTN research and experimentations.
