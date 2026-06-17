# IEEE Xplore — 2025-06


## A Cross-Layer Scheduling Method for Pipelined Layered Multi-Edge Type QC-LDPC Decoder With Better Conflict Resolution

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:10971375
- **Type**: journal
- **Published**: June 2025
- **Authors**: Dongxu Chang, Qingqing Peng, Guanghui Wang +1
- **PDF**: https://ieeexplore.ieee.org/document/10971375
- **Abstract**: For multi-edge type quasi-cyclic low-density parity-check (MET-QC-LDPC) codes, the presence of common variable nodes shared between rows within a single layer poses great challenges for the hardware design of the decoder. In this study, a cross-layer update scheduling method for pipelined layered MET-QC-LDPC codes is proposed to achieve improved conflict resolution. Through a probabilistic analysis, we show that by pairing layers with relatively small common degrees and performing alternating updates between the paired layers, better conflict resolution can be achieved than the layer-by-layer updating approach. Experimental results demonstrate that, at medium to low code rates, 50% to 75% of memory conflicts can be mitigated through the proposed cross-layer scheduling compared to the layer-by-layer scheduling approach, without compromising decoding performance.

## Revisiting Multiple ECC on High-Density NAND Flash memory

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:10947224
- **Type**: journal
- **Published**: June 2025
- **Authors**: Yunpeng Song, Yina Lv, Wentong Li +2
- **PDF**: https://ieeexplore.ieee.org/document/10947224
- **Abstract**: Three-dimensional nand flash memory using the advanced multibit-per-cell technique is widely adopted due to its high density. However, it faces the problem of deteriorating read performance and energy consumption due to decreased reliability. Low-density parity-check code (LDPC) is typically adopted as an error correction code (ECC) to encode data and provide fault tolerance. To reduce the cost, LDPC with a high code rate is always adopted. However, LDPC will lead to read retry operations when the accessed data are not successfully decoded, and such retry-induced performance degradation is serious, especially for modern high-density flash memory. In this work, a reliability-aware differential ECC (READECC) approach is proposed to reduce redundancy protection and storage cost of LDPC with a low code rate and optimize the read performance. The basic idea is to adopt LDPC with a suitable code rate considering both data access characteristics and flash reliability characteristics. First, hot reads are identified based on the frequency of being accessed. Second, based on the reliability variation characteristics, the life of flash memory is divided into three reliability periods. As the reliability period shifts, the code rate of the LDPC adjusts adaptively to minimize redundancy protection. Third, an adaptive-sized logical page approach is further proposed to support LDPC with strong error correction capability (a low code rate) with a low storage cost. Through careful design and evaluation on 3-D triple-level-cell nand flash memory, READECC achieves encouraging optimizations with a negligible cost.

## Implementation of Density Evolution for Polar Codes Based on Monte Carlo Simulation

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:10964027
- **Type**: journal
- **Published**: June 2025
- **Authors**: Nobuhiko Miki, Satoshi Suyama, Satoshi Nagata
- **PDF**: https://ieeexplore.ieee.org/document/10964027
- **Abstract**: Density evolution (DE) plays a fundamental role in the analysis of channel coding systems employing iterative decoding, and it is a valuable tool to design such systems. This letter discusses the implementation of DE for polar codes. In this letter, fast Fourier transform based methods are difficult to apply due to the difficulty in optimizing the parameters, and therefore, DE is performed using a Monte Carlo simulation. Finally, examples of the applications of this method are presented.

## Dual Diagonal LDPC: A Resource-Efficient Channel Coding Scheme for CubeSat Applications

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:10891713
- **Type**: journal
- **Published**: June 2025
- **Authors**: Amr Zeedan, Tamer Khattab, Ridha Hamila +1
- **PDF**: https://ieeexplore.ieee.org/document/10891713
- **Abstract**: The establishment of high-speed connectivity through CubeSats requires innovative solutions to overcome the challenges associated with the development of low-power, high-speed transceivers within the size and mass limitations inherent to CubeSats. Among the most computationally demanding tasks of any transceiver are demodulation and channel decoding, typically requiring a high utilization of hardware resources. This article proposes a channel coding scheme based on low density parity check (LDPC) coding, offering a markedly efficient allocation of resources to address these computational demands. In contrast to traditional LDPC encoding approaches, we develop a simplified algorithm based on an irregular repeat-accumulate (IRA) dual diagonal parity check matrix construction, resulting in an extremely resource-efficient code. The enhanced algorithm efficiently conserves hardware resources through the shared utilization of the parity check bit generator. Moreover, a corresponding low-complexity decoder, based on efficiently combining the Min-Sum (MS) algorithm and the Bit-Flipping (BF) algorithm, which employs the Log-Likelihood Ratio (LLR) is proposed.. We obtain the mathematical closed-form expression for the bit error rate (BER) of the proposed scheme and verify it against simulations, showing a very close match. The proposed scheme achieves high code rate, 3/4, and data rate, 30 Mbps, with a smaller number of decoding iterations, 10, while achieving better BER performance compared to various existing algorithms. Compared to the channel coding schemes currently being employed by CubeSats, our scheme demonstrates the highest information rate, the lowest number of decoding iterations and the highest efficiency.

## DNN-Based RV-Adaptive HARQ for Low-Latency Communications

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:10856411
- **Type**: journal
- **Published**: June 2025
- **Authors**: Weihang Ding, Mohammad Shikh-Bahaei
- **PDF**: https://ieeexplore.ieee.org/document/10856411
- **Abstract**: In comparison to Ultra-Reliable Low-Latency Communications (URLLC) in 5G mobile communication systems, the next generation URLLC (xURLLC) requires even lower latency and higher reliability. To address these requirements, we propose a novel redundancy version (RV)-adaptive hybrid automatic repeat request (HARQ) scheme. Our approach builds upon the existing 5G HARQ framework and 5G low-density parity-check (LDPC) codes, introducing an adaptive selection of the RV for the subsequent transmission based on the current decoding states. To determine the optimal RV, we use a modified version of the reciprocal channel approximation (RCA) algorithm to compare the decoding thresholds of all available RVs and select the one with the lowest threshold to maximize the likelihood of successful decoding. To further reduce processing delay, we apply a deep neural network (DNN) to predict the optimal RV for the next transmission. This prediction is made prior to the decoding process, ensuring that no additional delay is introduced. Since the selection is made before the decoding starts, our proposed method can seamlessly integrate with other adaptive-HARQ and fast HARQ schemes.

## U-Shaped Error Correction Code Transformers

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:10720857
- **Type**: journal
- **Published**: June 2025
- **Authors**: Dang-Trac Nguyen, Sunghwan Kim
- **PDF**: https://ieeexplore.ieee.org/document/10720857
- **Abstract**: In this work, we introduce two variants of the U-shaped error correction code transformer (U-ECCT) in combination with weight-sharing to improve the decoding performance of the error correction code transformer (ECCT) for moderate-length linear codes. The proposed models are inspired by the well-known U-Net architecture to leverage residual information for faster error estimation based on the syndrome-based reliability decoding principle. As an effort to further improve the general decoding performance of the U-ECCT, we propose the variational U-ECCT (VU-ECCT), in which the process of learning the shortcut connections is treated as a generative problem, forming a variational autoencoder (VAE) that exists intertwined with the existing U-ECCT model. This design allows the extraction of mutual information between the different levels of the U-shaped architecture, thus enhancing the performance of large syndrome sequences for low-rate codes. Additionally, to further reduce the model size, a new weight-sharing strategy, called mirror-sharing, is proposed to compress the model size as well as complement the mechanism of the proposed U-shaped architecture. In experiments, it has been demonstrated that our proposed models achieve significantly better performance than baseline conventional algorithms and other learning-based models.

## Successive Interference Cancellation-Enabled Timely Status Update in Linear Multi-Hop Wireless Networks

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:10839590
- **Type**: journal
- **Published**: June 2025
- **Authors**: Xinhui Han, Haoyuan Pan, Zhaorui Wang +1
- **PDF**: https://ieeexplore.ieee.org/document/10839590
- **Abstract**: We investigate the timely status update in linear multi-hop wireless networks, where a source tries to deliver status update packets to a destination through a sequence of half-duplex relays. Timeliness is measured by the age of information (AoI) metric. Maintaining a low AoI at the destination typically necessitates frequent transmission of update packets from the source. However, high packet transmission frequency in multi-hop scenarios can result in mutual wireless interference at intermediate relays. Specifically, when an intermediate relay receives wireless signals of a new packet from its previous node, simultaneous transmission of an old packet by its subsequent node to the next hop may cause wireless signals to interfere at the intermediate relay, conventionally leading to packet collision. A key motivation to solve this issue is that the intermediate relay has previously received the old packet (which can thus be forwarded to the subsequent node for further relaying). Hence, successive interference cancellation (SIC) can be employed to mitigate interference of the old packet and recover the new packet. This paper designs an SIC-enabled packet relaying scheme tailored to low AoI. Initially focusing on a three-hop network, we subsequently extend our approach to general multi-hop networks. We model the multi-hop relaying scheme using a Markov chain to derive the theoretical average AoI. Theoretical and simulation results indicate that the SIC-enabled packet relaying scheme significantly reduces the average AoI compared to the non-SIC approaches, owing to an increased packet transmission frequency at the source and the effectiveness of SIC techniques at the relays.

## Enhanced Codebook of Sparse Vector Coding Based on Mean-Variance Trade-Off Model for URLLC

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:10963750
- **Type**: journal
- **Published**: June 2025
- **Authors**: Yifei Yang, Changju Chen, Pengcheng Zhu
- **PDF**: https://ieeexplore.ieee.org/document/10963750
- **Abstract**: Sparse Vector Coding (SVC) is a novel coding scheme of short packet transmission in Ultra-Reliable Low-Latency Communication (URLLC). SVC is usually modeled as a standard Compressed Sensing (CS) model, so the column correlation coefficient of the encoding dictionary will directly determine the decoding performance. Starting from the point of view of optimizing codebook, this letter will first model the minimization of the maximum column correlation coefficient as a linear integer programming (LIP) problem, and obtain a tighter solution than existing studies. Then, the optimization objective was transformed into statistical parameters of column correlation coefficient distribution and modeled as mean-variance trade-off model, which was a convex optimization problem and optimized by Semi-Definite Programming (SDP) and Modern Portfolio Theory (MPT) respectively, improving the Block Error Ratio (BLER) performance about 1dB and reduced the computational complexity. Simulation results verify the effectiveness of the above algorithms and improve the decoding performance effectively.

## Soft Decision Decoding of Recursive Plotkin Constructions Based on Hidden Code Words

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:10947200
- **Type**: journal
- **Published**: June 2025
- **Authors**: Martin Bossert
- **PDF**: https://ieeexplore.ieee.org/document/10947200
- **Abstract**: The Plotkin construction combines two codes to a code of doubled length. It can be applied recursively. The class of Reed-Muller (RM) codes is a particular example. Exploiting a property of the code words constructed by the recursive Plotkin construction, we present novel soft-decision decoders. These are based on the decoding of hidden code words which are inherent contained in the constructed code words and can be uncovered by adding particular parts of the overall code word. The main idea is to use more than one decoding variant where each variant starts with the decoding of a different hidden code word. Given the decision of this first hidden code word allows error cancellation for the remaining decoding. The final decoding decision selects the best of the decisions of the used variants. The more variants are used the closer the performance gets to the maximum-likelihood (ML) decoding performance. This is verified by an ML-bound for the cases where the ML performance is not known. The decoding algorithms use only additions, comparisons, and sign operations. Further, due to the recursive structure, only relatively short codes have to be decoded, thus, the decoding complexity is very low. We also present a new decoder for first-order RM codes with low complexity. In addition, we introduce two novel classes of half-rate codes based on recursive Plotkin constructions with RM codes. We show that the novel soft decision decoders can also be applied to recursive Plotkin constructions with BCH codes and to particular classes of generalized concatenated codes (GCC).

## Enhancing Belief Propagation Decoding of Polar Codes: A Reinforcement Learning Approach

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:10960358
- **Type**: journal
- **Published**: June 2025
- **Authors**: Mohsen Moradi, Salman Habib, David G. M. Mitchell
- **PDF**: https://ieeexplore.ieee.org/document/10960358
- **Abstract**: Short block-length polar-like codes showcase exceptional error correction performance (ECP) using sequential decoding or successive cancellation list decoding with a large list size. However, achieving a high level of reliability with these methods involves high-latency decoding. To meet the growing demand for low-latency communication with acceptable complexity, belief propagation (BP) decoding emerges as an attractive option, although its ECP is known to fall short of those high-latency alternatives. In this letter, we propose an enhanced BP decoding approach for polar codes, leveraging reinforcement learning (RL) to optimize the message-passing schedule. Moreover, we investigate the design of the polar code rate profile and corresponding Tanner graph representation to enhance the benefits of RL. Numerical results demonstrate a performance gain of more than 1 dB for polar codes with a length of 128 and a rate of 0.5 compared to conventional BP decoding alone at high  $E_{b}/N_{0}$  values, demonstrating the promise of the proposed approach.

## Low-Complexity Neural Belief Propagation Decoding Algorithm Based on Tensor Ring Decomposition

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:10738425
- **Type**: journal
- **Published**: June 2025
- **Authors**: Yuanhui Liang, Chan-Tong Lam, Qingle Wu +2
- **PDF**: https://ieeexplore.ieee.org/document/10738425
- **Abstract**: Neural belief propagation (NBP) decoding can improve the performance of belief propagation (BP) decoding for high-density parity check (HDPC) codes, at the expense of higher memory storage requirement and computational complexity due to the addition of trainable weight coefficients. To reduce the high storage requirement of NBP, the cyclically equivariant neural BP (CENBP) algorithm makes full use of the cyclically invariant property of the cyclic code, optimizes and reuses the weight coefficients of the NBP algorithm, at the expense of further increasing the computational complexity of NBP. In this paper, we propose low-complexity, in terms of both memory storage requirement and computational complexity, NBP and CENBP decoding algorithms based on Tensor Ring (TR) decomposition. First, in order to reduce the memory storage and computational complexity of the NBP algorithm, we propose a TR-based compression algorithm to compress the messages and mathematical calculations in the NBP decoding algorithm, called TR-NBP algorithm. Second, to address the high computational complexity of the CENBP algorithm, we propose to apply TR decomposition-based compression to the odd layers of the CENBP decoding algorithm, called TR-CENBP, to reduce the computational complexity, and further reduce the required memory storage requirement of the CENBP algorithm. Furthermore, we use TR decomposition-based compression to simplify the mathematical computations associated with the tanh function in the NBP algorithm to further reduce the complexity of the hardware implementation. Experimental results show that direct compression of BP algorithm using TR decomposition results in significant performance degradation and our proposed low complexity TR-NBP algorithm and TR-CENBP algorithm can greatly reduce both the memory storage requirement and computation complexity, without significant performance degradation for typical BCH and LDPC codes.

## Over-the-Air Distributed Matrix-Vector Multiplication With Analog Coding

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:10852406
- **Type**: journal
- **Published**: June 2025
- **Authors**: Jinho Choi
- **PDF**: https://ieeexplore.ieee.org/document/10852406
- **Abstract**: Distributed matrix-vector multiplication plays a key role in numerous computing-intensive applications, including machine learning, by leveraging distributed computing resources known as workers. When workers are wirelessly connected, there is flexibility, enabling efficient resource utilization and scalability of computational tasks. This distributed approach facilitates parallel processing, leading to faster computations and improved performance of machine learning algorithms. However, two key issues arise: stragglers and limited channel resources. In this paper, we propose an approach based on analog coding to not only mitigate stragglers but also leverage over-the-air (OTA) computation. This approach offers scalability without necessitating an increase in bandwidth as the number of workers increases, by taking advantage of the superposition property of radio frequency (RF) signals. This capability addresses the limitations of digital communication-based approaches, where performance is typically constrained by available bandwidth. We derive a closed-form expression for performance in terms of mean squared error (MSE) and compare it with an ideal digital method. Simulation results and comparisons confirm that the proposed analog coding scheme is well-suited to various scenarios with a large number of workers.

## Coding Over Coupon Collector Channels for Combinatorial Motif-Based DNA Storage

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:10769527
- **Type**: journal
- **Published**: June 2025
- **Authors**: Roman Sokolovskii, Parv Agarwal, Luis Alberto Croquevielle +2
- **PDF**: https://ieeexplore.ieee.org/document/10769527
- **Abstract**: Encoding information in combinations of pre-synthesised deoxyribonucleic acid (DNA) strands (referred to as motifs) is an interesting approach to DNA storage that could potentially circumvent the prohibitive costs of nucleotide-by-nucleotide DNA synthesis. Based on our analysis of an empirical data set from HelixWorks, we propose two channel models for this setup (with and without interference) and analyse their fundamental limits. We propose a coding scheme that approaches those limits by leveraging all information available at the output of the channel, in contrast to earlier schemes developed for a similar setup by Preuss et al. We highlight an important connection between channel capacity curves and the fundamental trade-off between synthesis (writing) and sequencing (reading) costs, and offer a way to mitigate an exponential growth in decoding complexity with the size of the motif library.

## Gradient Descent Decoding of MDPC Codes Optimized with Genetic Algorithm

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11114132
- **Type**: conference
- **Published**: 9-12 June 
- **Authors**: Dimitrije Jovanović, Jovan Milojković, Zoran Čiča +1
- **PDF**: https://ieeexplore.ieee.org/document/11114132
- **Abstract**: Bit-flipping (BF) is a very simple algorithm for decoding linear block codes. For the BF to achieve high performances of belief-propagation (BP) algorithms, which are far more complex, we apply several optimizations using the genetic algorithm (GA), to optimize the parameters of our decoder. Adaptive diversity gradient descent bit-flipping with momentum (AD-GDBFwM) algorithm is designed as a cascade of multiple decoders with different parameters, which are optimized with GA. In this paper we consider AD-GDBFwM decoding of mediumdensity parity-check (MDPC) codes. We measure the decoding performance and compare it with the results of various types of decoders, including BP and neural BP.

## Iterative Decoding Algorithms Powered by Deep Learning

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11114279
- **Type**: conference
- **Published**: 9-12 June 
- **Authors**: Dimitrije Jovanović, Predrag Ivaniš
- **PDF**: https://ieeexplore.ieee.org/document/11114279
- **Abstract**: In this paper, we analyze the performance of neural belief propagation (BP) decoding on the additive white Gaussian noise (AWGN) channel, compared to the traditional BP algorithm. Previous investigations have shown that assigning pre-trained weights to BP messages can significantly improve the decoding performance in case of high-density parity-check (HDPC) codes, by reducing the negative impact of short cycles. These weights are trained by a neural network whose structure matches the trellis of the decoder. Specifically, we show that medium-density paritycheck (MDPC) codes decoded with neural BP algorithm can achieve lower bit error rate versus HDPC codes with the same codeword length and the same code rate.

## Quantization Analysis for the CRC Aided Successive Cancellation List Polar Decoder

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11114217
- **Type**: conference
- **Published**: 9-12 June 
- **Authors**: Nikola Borović, Dragomir El Mezeni, Vladimir Petrović
- **PDF**: https://ieeexplore.ieee.org/document/11114217
- **Abstract**: Polar codes have recently found application as error correction codes for the control information in 5 G wireless communication. Stringent requirements for decoding latency, power consumption, and communication reliability demand efficient hardware implementation of communication modules. One of the key aspects of efficient hardware implementation is a robust quantization scheme. In this paper, we present an empirical approach to analyzing quantization for the Cyclic Redundancy Check-Aided Successive Cancellation List (CA-SCL) decoding algorithm, which is used in the 5 G standard. The paper gives detailed quantization analysis of the CA-SCL algorithm for 11-bit CRC and 4 lists. We proposed a quantization scheme with decoding performance within 0.1 dB of the floating point performance for positive Signal-to-noise ratios (SNRs). It is shown that a decoder with one extra bit achieves performance within 0.1 dB of the floating-point model over a wide range of SNRs and code rates.

## Multi-Stage Bit-Flipping Decoder Design for Quantum Error-Correcting Codes

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11291312
- **Type**: conference
- **Published**: 9-10 June 
- **Authors**: Patrick J. Moxom, Mark F. Flanagan
- **PDF**: https://ieeexplore.ieee.org/document/11291312
- **Abstract**: This paper proposes the use of simple bit-flipping (BF) methods as a post processor for decoding quantum low-density parity check codes (qLDPC) with message passing (MP). Specifically, min-sum (MS) is used as the MP method for the first stage of the multi-stage decoder. Two methods are proposed that modify the low-complexity Gallager’s algorithm (GA). First, a weighted bit-flipping (WBF) method is developed using soft information from the MP stage. Secondly, GA is modified with a random bit-flipping (RBF) approach. Early stopping and loop detector stage switching methods are used to enhance the performance of the BF stage. These methods are shown to significantly reduce the error floor of the first stage while also being less complex than alternative multi-stage decoders.

## A New Post-Quantum Signature Based on Punctured QC-LDPC Code with Random Insertion

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11162115
- **Type**: conference
- **Published**: 8-12 June 
- **Authors**: Xin Lin, Yusun Fu, Zihao Wang +1
- **PDF**: https://ieeexplore.ieee.org/document/11162115
- **Abstract**: This paper proposes an enhanced version of the CFS signature scheme, leveraging QC-LDPC codes with puncturing and random insertion techniques. The puncturing process is designed based on the selection of minimum Hamming weight codewords, ensuring that the remaining structure of the parity-check matrix retains sufficient error-correcting capabilities. Random insertion of new rows into the punctured parity-check matrix further enhances security by introducing randomness. The cyclic structure of QC-LDPC codes greatly reduces the key size while the BP decoding algorithm improves the decoding success rate, thereby enhancing the signature generation efficiency. The scheme proposed in this paper reduces the key size to 6144 bytes compared to the original CFS scheme's 6283256 bytes under the similar parameters setting. Additionally, the average number of signing attempts is reduced from $t!$ to a constant multiple of $t$. It also greatly enhances security compared to recent improvements, particularly in resisting structural attacks, Stern's attacks, OTD attacks, and forgery attacks. Similar to the original CFS scheme, the proposed scheme can be proven to satisfy Existential Unforgeability under Chosen Message Attacks (EUF-CMA) security.

## A Practical Method for Power Saving in 4G, 5G, and Beyond 5G Channel Decoders Using RBIR

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11160748
- **Type**: conference
- **Published**: 8-12 June 
- **Authors**: Anusha Gunturu, Ashok Kumar Reddy Chavva
- **PDF**: https://ieeexplore.ieee.org/document/11160748
- **Abstract**: With sustainability as one of the key requirements and the design principles of the sixth generation (6 G) communications, implementation based power saving solutions that benefit both base station (BS) and user equipment (UE) sides have gained significant interest in the cellular industry research. Channel decoding is one of the receiver modules that can help reduce the power consumption of the receiver significantly, and is applicable to both BS and UE. In this paper, we propose a universal list size and iteration number predictor (ULIP), for reducing the power consumption, applicable for 4G, 5G and beyond-5G channel decoders. We propose to use a link abstraction abstraction metric called received bit information rate (RBIR), that captures the time-varying channel conditions to identify and choose the iteration and list sizes for these decoders, to reduce the power consumption. We evaluate the proposed ULIP for regulating the iteration number in turbo and low-density parity-check (LDPC) decoders, used in 4 G and 5 G data channels, respectively, and the list size in polar decoder, used in 5 G control channel. We also verify the proposed ULIP for regulating the list size in the recently introduced polarization-adjusted convolutional (PAC) decoder, a prospective scheme for 6 G. We show that the proposed solution has upto 54.7 % and 67.4 % reduction of iteration numbers in LDPC and turbo decoders, respectively, for a target block error rate (BLER) of 10 %, and upto $\sim 92 \%$ reduction of list sizes in both polar and PAC decoders, for a target BLER of 0.1 %, compared to conventional decoding methods.

## Low-Complexity Multi-Slot Cross-Domain MAMP Receiver and Coding Principle for MIMO-OTFS

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11161769
- **Type**: conference
- **Published**: 8-12 June 
- **Authors**: Yuhao Chi, Zhiyuan Peng, Lei Liu +3
- **PDF**: https://ieeexplore.ieee.org/document/11161769
- **Abstract**: This paper investigates a coded multiple-input multiple-output (MIMO) orthogonal time frequency space (OTFS) system in high-mobility channels. Existing coding schemes are limited by the strong assumption that the codeword length is equal to the dimension of the modulation length. Moreover, the design of low-complexity and high-reliability receivers remains a critical challenge for MIMO-OTFS systems. Therefore, this paper proposes a multi-slot cross-domain memory approximate message passing (MS-CD-MAMP) receiver as well as develops its information-theoretic (i.e., achievable rate) limit and optimal coding principle for MIMO-OTFS. The proposed MS-CD-MAMP receiver can exploit not only the time domain channel sparsity for low complexity but also the constellation constraints in DelayDoppler (DD) domain for performance enhancement. Meanwhile, limited by the high-dimensional complex state evolution (SE), a simplified single-input single-output variational SE is proposed to derive the achievable rate of MS-CD-MAMP and the optimal coding principle with the goal of maximizing the achievable rate. Numerical results show that the finite-length performances of MS-CD-MAMP with optimized low-density parity-check (LDPC) codes are about $1.1 \sim 1.4 \mathbf{d B}$ away from the associated constrained information-theoretic limit and has $0.9 \sim 4.7 \mathbf{d B}$ gain over the well-designed point-to-point LDPC codes.

## Joint Semantic-Channel Coding and Modulation for Point Cloud

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11161502
- **Type**: conference
- **Published**: 8-12 June 
- **Authors**: Jingkai Ying, Zhijin Qin, Liejun Wang +1
- **PDF**: https://ieeexplore.ieee.org/document/11161502
- **Abstract**: Despite remarkable progress in semantic communication, most current deep learning-enabled semantic communication approaches map source information into continuous channel symbols, posing significant challenges for hardware implementation and integration with existing digital communication systems. In this article, we tackle this issue with a joint semantic-channel coding and modulation scheme, enabling the transmitter to generate digital constellation points. Furthermore, a rate allocation model is proposed for assigning different lengths of constellation point sequences to source information with varying semantics. Moreover, motivated by traditional adaptive modulation schemes, we elaborated a channel adaption model to match the modulation with channel conditions. To verify our designs, point cloud, a prevailing three-dimensional representation, which urgently requires a new transmission method due to its large data volume, is investigated. Building upon the proposed methods, a semantic communication system for point cloud is developed. Simulation results demonstrate that the system outperforms existing point cloud transmission methods in terms of efficiency and reliability.

## Optimization of Irregular Repetition Slotted ALOHA with Imperfect SIC in 5G CIoT

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11161616
- **Type**: conference
- **Published**: 8-12 June 
- **Authors**: Saeed Alsabbagh, Cédric Adjih, Amine Adouane +1
- **PDF**: https://ieeexplore.ieee.org/document/11161616
- **Abstract**: Irregular Repetition Slotted ALOHA (IRSA) is an effective grant-free random access scheme that is well-suited for managing the sporadic nature of IoT traffic, particularly in dense environments prone to collisions. In this paper, we evaluate the performance of IRSA under realistic conditions involving imperfect successive interference cancellation (SIC) and non-ideal physical layer environments. Specifically, we investigate the impact of various channel conditions and physical layer impairments on IRSA's performance. Previous studies on IRSA often assume ideal physical layer conditions or use simplified models for SIC errors, which fail to fully capture practical implementation complexities. To address this gap, we propose integration of practical factors, such as channel estimation imperfections, into our model of SIC failures using detailed baseband simulations. Based on that, we employ density evolution analysis to evaluate system throughput and optimize the degree distributions to enhance IRSA performance in the presence of imperfect SIC. Additionally, we analyze the power of the residual interference to assess its impact on decoding performance under realistic conditions. Our results focusing on 5G CIoT demonstrate that optimizing IRSA parameters, while accounting for SIC errors, can significantly improve system performance, resulting in notable throughput gains.

## Filter-Banks for Ultra-Wideband for Communications, Sensing, and Localization

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11162147
- **Type**: conference
- **Published**: 8-12 June 
- **Authors**: Brian Nelson, Hussein Moradi, Behrouz Farhang-Boroujeny
- **PDF**: https://ieeexplore.ieee.org/document/11162147
- **Abstract**: Recently, filter-bank multicarrier spread spectrum (FBMC-SS) has been proposed as a candidate waveform for ultra-wideband (UWB) communications, sensing, and localization. It has been noted that FBMC-SS is a perfect match to this application, leading to a trivial method of matching to the required spectral mask at different regions of the world. FBMC-SS also allows easy rejection of high-power interfering signals that may appear over different parts of the UWB spectral band. Moreover, passing the received signal through a matched filter provides precise information for sensing and localization. In this paper, we concentrate on the use of staggered multitone spread spectrum (SMT-SS) for UWB communications. SMT makes use of offset quadrature amplitude modulation (OQAM) to transmit data symbols over overlapping subcarrier bands. This form of FBMC-SS is well-suited to UWB communications because it has good spectral efficiency and a flat power spectral density (PSD), resulting in good utilization of the UWB spectral mask.

## Quantized Feedback-enhanced Large Multimodal Model for V2X Communications

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11162198
- **Type**: conference
- **Published**: 8-12 June 
- **Authors**: Hyunsoo Kim, Seokhyun Jeong, Seonghoon Kim +3
- **PDF**: https://ieeexplore.ieee.org/document/11162198
- **Abstract**: Recent advances in large multimodal models (LMMs) have inspired the integration of vehicle-to-everything (V2X) communication and diverse sensing data. One of the key challenges in LMM-enabled V2X communication is the substantial sensing feedback overhead between vehicles and roadside unit (RSU). To address this, QF-LMMV2X extracts high-level semantic features from sensing data and then quantizes the extracted feature using vector quantization, effectively reducing redundancy while preserving essential semantic information. This quantization process in QF-LMMV2X significantly minimizes communication overhead, enabling efficient V2X information exchange. From the simulation results, we demonstrate that QF-LMMV2X outperforms conventional schemes by more than 25% in terms of car accident prediction accuracy.

## BER Analysis of Channel Coding Technique for 5G

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11136522
- **Type**: conference
- **Published**: 6-7 June 2
- **Authors**: Ashitha V. Naik, Hithesha. P, Rahul. K C +1
- **PDF**: https://ieeexplore.ieee.org/document/11136522
- **Abstract**: The channel in a communication system is usually affected by noise so channel coding is employed to avoid contamination of data due to noise in 5G networks. The Bit Error Rate (BER) performance is a key metric in achieving this goal. High-speed data transfer in such networks encounters considerable obstacles from interference and noise, which can reduce overall efficiency. To overcome these challenges, 5G systems widely incorporate error correction schemes like LDPC and Polar codes. LDPC codes are particularly effective in Additive White Gaussian Noise (AWGN) environments, whereas Polar codes are better suited for conditions involving structured noise such as Rayleigh fading. The simulation findings demonstrate that BER of LDPC codes yield better Performance in Gaussian noise scenarios while Polar codes offer improved performance in fading conditions. The MATLAB-based simulation helps to find the best channel for the 5G standard considering the bit error rate (BER) and channel capacity performance among additive white Gaussian noise (AWGN), Rayleigh and Rician channels for different channel coding and modulation techniques.

## Implementation of Low-Density Parity-Check (LDPC) Codes in Verilog HDL

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11101329
- **Type**: conference
- **Published**: 5-7 June 2
- **Authors**: Ritesh Pathak, Sateesh Kumar Awasthi
- **PDF**: https://ieeexplore.ieee.org/document/11101329
- **Abstract**: This work presents FPGA implementation of Low-Density Parity-Check (LDPC) encoder. Low-density coding is an effective method for ensuring reliable communication over noisy channels while minimizing the probability of error. We use Verilog hardware description language (HDL) to simulate this encoder for various code rates. The encoder is implemented on the Xilinx Artix-7 FPGA(XC7A35T-ICPG236C) kit using FPGA 28 nm CMOS technology and DE10-Lite FPGA Kit using FPGA 55 nm CMOS technology.

## Generating Hamiltonians with Known Minimum Energy Based on Ground-State Spin Logic for Probabilistic-Bit-Based Simulated Annealing

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11038009
- **Type**: conference
- **Published**: 5-6 June 2
- **Authors**: Naoya Onizawa, Takahiro Hanyu
- **PDF**: https://ieeexplore.ieee.org/document/11038009
- **Abstract**: A probabilistic bit (p-bit), considered a key element of probabilistic computing, has been shown to be promising in the acceleration of simulated annealing (SA) algorithms. However, benchmark Hamiltonians currently available are often characterized by the absence of a known minimum energy, making the evaluation of SA performance challenging. To address this issue, an open-source Hamiltonian generation tool based on ground-state spin logic is proposed, allowing Hamiltonians with known energy minima to be created. The tool is designed to utilize a pre-generated library of gate Hamiltonians, which are small-scale Hamiltonians representing individual logical operations (e.g., AND or OR gates), prepared through linear programming. By systematically combining these gate Hamiltonians, a target Hamiltonian can be generated to represent a larger problem. The characteristics of the target Hamiltonian, such as size and the non-zero ratio, can be customized to meet specific requirements. These Hamiltonians are evaluated using p-bit-based SA algorithms to investigate the impact of Hamiltonian properties on SA performance.

## Development of a Universal FPGA-Based Coprocessor for 5G NR and WLAN LDPC Coding

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11037065
- **Type**: conference
- **Published**: 3-6 June 2
- **Authors**: Lukasz Lopacinski, Yiyun Jian, Muhammad Nauman +3
- **PDF**: https://ieeexplore.ieee.org/document/11037065
- **Abstract**: Low-density parity-check (LDPC) codes are widely used in modern communication systems due to their near-capacity error correction performance. This paper presents a practical FPGA implementation of a universal hardware coprocessor for LDPC encoding and decoding, focusing on a system-level architecture, achievable data rate, latency measurements, and hardware resource utilization. The LDPC coding is realized by the Xilinx hardware macros available in the Xilinx RF-SoC FPGAs. We explore various design simplifications, including core combining, memory management, and data scheduling, to achieve high throughput while maintaining the lowest implementation complexity. The proposed architecture is implemented on an FPGA platform and is equipped with 10Gb/s Ethernet interfaces, demonstrating real-time decoding capabilities and improved performance compared to software-based approaches. Experimental results validate the design, showcasing its applicability in high-speed communication systems. This work can serve as a reference for engineers and researchers aiming to deploy LDPC decoding in FPGA-based environments by reusing the existing Intellectual Property (IP), which is freely available in Xilinx SoC.

## LDPC Code Performance Analysis and BER Comparison with Uncoded QPSK

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11138832
- **Type**: conference
- **Published**: 28-30 June
- **Authors**: Dinghao Li
- **PDF**: https://ieeexplore.ieee.org/document/11138832
- **Abstract**: In the rapidly evolving landscape of modern communication systems, the demand for high-speed, reliable, and efficient data transmission has never been greater. This paper compares Low-Density Parity-Check (LDPC) codes and uncoded Quadrature Phase Shift Keying (QPSK) modulation, focusing on their technical principles, performance characteristics, and practical applications. LDPC codes, known for their near-Shannon limit error correction and efficient parallel decoding, are widely used in high-speed data transmission scenarios such as 5 G networks, digital TV broadcasting, and IoT devices. QPSK modulation offers high spectral efficiency and robustness against interference, making it suitable for satellite communication and mobile networks. The paper evaluates their performance in terms of bit error rate (BER), transmission rate, bandwidth efficiency, and implementation complexity. Simulation results show that LDPC encoding significantly outperforms uncoded QPSK in reducing BER, especially at higher signal-to-noise ratios (SNR), while maintaining competitive bandwidth efficiency. The paper also discusses their applicability in different communication scenarios, including high and low SNR environments, highspeed data transmission, and resource-constrained settings. Finally, it highlights future research directions, such as optimizing LDPC codes for IoT devices and addressing QPSK's limitations through advanced modulation techniques.

## Research on Hierarchical Recognition Method for Long Channel Coding Types Based on Deep Learning

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11151128
- **Type**: conference
- **Published**: 27-29 June
- **Authors**: Weiran Zhang, Lin Liu, Ping Wang +3
- **PDF**: https://ieeexplore.ieee.org/document/11151128
- **Abstract**: In the process of signal transmission, the receiver obtains the data without channel decoding after a series of processing such as synchronization and demodulation of the received signal. In the case of non-cooperation, the encoded data cannot be directly decoded because the coding type of the data is unknown, and the coding type needs to be recognized first. In this paper, a hierarchical channel coding recognition scheme based on deep learning is proposed, which employs CNNBiLSTM and CNN-LSTM models for multi-stage recognition. The system sequentially recognizes different coding types using raw encoded data, extracted code features, and IP matrices. Experimental results show that the proposed method achieves a recognition accuracy of 99.76% at bit error rate of 10−3, delivering robust recognition performance.

## High Performance and Resource Efficient Low Density Parity Check Decoder Design

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11112140
- **Type**: conference
- **Published**: 25-28 June
- **Authors**: Burak Ünal
- **PDF**: https://ieeexplore.ieee.org/document/11112140
- **Abstract**: Low Density Parity Check (LDPC) codes have gained popularity in communication systems due to their capacity-approaching error correction performance. In this study, a high-performance LDPC decoding algorithm with extremely low resource usage is proposed. Among the hard decision class of LDPC decoders, Gallager B (GaB) provides high-performance hardware due to its computational simplicity. However, GaB suffers from poor error-correction performance. In this study, a new intrinsic computation technique for GaB called Intrinsic Gallager B (IGaB) is introduced to improve error correction performance. Our simulation results show that the IGaB algorithm provides better error correction performance compared with GaB. GaB and IGaB algorithms are implemented on Field Programmable Gate Array (FPGA) to compare hardware performance.

## LDPC-Coded Molecular Communications with Increased Diversity

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11111940
- **Type**: conference
- **Published**: 25-28 June
- **Authors**: Alpar Türkoğlu, Berk Karabacakoğlu, Ali Emre Pusane
- **PDF**: https://ieeexplore.ieee.org/document/11111940
- **Abstract**: This paper suggests achieving diversity gains while utilizing low-density parity check (LDPC) codes in molecular communications. Intersymbol interference (ISI) causes a significant disadvantage in error performance for molecular communications. Even though decoding LDPC codes with soft decoding yields a considerable enhancement in the bit error rate (BER) curves, this can be further improved by utilizing diversity gain. In order to achieve this, two different messenger molecule types are sent to transmit the message codeword and its interleaved version. The molecular communication channel is then modeled, and the error performance of the proposed method is estimated by Monte-Carlo simulations. This approach provides considerable improvement in the error performance in the scenario where few messenger molecules are transmitted per bit.

## Modern Methods for Ensuring Data Integrity in Radio Channels

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11254355
- **Type**: conference
- **Published**: 25-27 June
- **Authors**: Valery Zolotarev, Gennady Ovechkin, Dina Satybaldina +2
- **PDF**: https://ieeexplore.ieee.org/document/11254355
- **Abstract**: This paper investigates the effectiveness of multi-threshold decoding (MTD) in multichannel wireless communication systems, taking into account various factors such as multipath signal propagation and inter-symbol interference. Particular attention is given to data transmission reliability, where MTD is applied to enhance error resilience in high-speed and interference-prone communication. The study involves simulation of a data transmission system based on self-orthogonal codes and orthogonal frequency-division multiplexing (OFDM). The focus is placed on a comparative performance analysis of MTD versus other error correction methods, such as LDPC and turbo codes, under various modulation schemes (QPSK, 8PSK, 16APSK). Evaluation was conducted using ITU-R Outdoor Channel A and SCM Urban Macro channel models, considering different noise levels, receiver speeds, and fading parameters. The results show that MTD not only provides high performance comparable to other methods but also significantly reduces computational complexity, which is critical for mobile devices with limited processing resources. These findings confirm the relevance of applying MTD in data transmission systems to improve reliability and robustness under challenging radio environments and interference-prone communication, where traditional methods require substantial computational costs.

## A Mathematical Model for Device Authentication in Trusted Interaction in Decentralized Internet of Things Environments

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11252598
- **Type**: conference
- **Published**: 25-27 June
- **Authors**: Ilia Andreev, Vyacheslav Petrenko, Fariza Tebueva +3
- **PDF**: https://ieeexplore.ieee.org/document/11252598
- **Abstract**: The paper presents a mathematical model for authentication of peripheral devices in industrial IoT networks operating in decentralized environments. The model is based on the use of SRAM-PUF to generate 512-bit identifier signals, which increases the probability of collisions to 10−154. To correct errors caused by hardware noise, a hybrid LDPC code (768512) is used, providing correction of up to 10% of bit errors while reducing computational costs by 37% compared to classical BCH codes. A decentralized rejection validation protocol from centralized servers using symmetric AES-GCM encryption to protect challenge-response pairs. Experimental results of the model's resistance to brute-force attacks (FAR = 0%), reduced false rejection rate (FRR = 1.8%) and energy efficiency (0.9 mJ per operation) are obtained. The proposed approach ensures scalability for networks with millions of devices and compatibility with modern cybersecurity standards.

## A Typology of Quantum-Classical Faults

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11071596
- **Type**: conference
- **Published**: 23-26 June
- **Authors**: Edoardo Giusto, Santiago Núñcz-Corrales, Alessandro Cilardo +2
- **PDF**: https://ieeexplore.ieee.org/document/11071596
- **Abstract**: This paper introduces an extended taxonomy of faults specific to hybrid quantum-classical systems, addressing the unique challenges that arise from integrating quantum accelerators into high-performance computing (HPC) infrastructures. Building on the foundational fault classification by Avizienis et al., we incorporate fault types unique to quantum computing-such as qubit decoherence, spontaneous gate errors, and photon loss-alongside traditional and human-induced faults including development errors, operational mistakes, and malicious attacks. Our taxonomy classifies faults by their origin (natural vs. human-made), intent (accidental, deliberate non-malicious, or malicious), system boundaries (internal vs. external), and persistence (transient to permanent). We also explore how different architectural integration patterns-ranging from tight coupling to loose on-premise and cloud-based configurations-shape the manifestation and propagation of faults. These scenarios are analyzed in terms of timing mismatches, interface inconsistencies, and security threats such as data tampering and denial-of-service attacks. Through this fault-centric lens, we aim to support the co-design of dependable quantum-classical systems and highlight the critical role that integration strategies play in ensuring reproducibility, resilience, and security across hybrid computing platforms.

## Protograph-Based LDPC Codes with Local Irregularity

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11195381
- **Type**: conference
- **Published**: 22-27 June
- **Authors**: Vincent Wüst, Erdem Eray Cil, Laurent Schmalen
- **PDF**: https://ieeexplore.ieee.org/document/11195381
- **Abstract**: Forward error correcting (FEC) codes are used in many communication standards with a wide range of requirements. FEC codes should work close to capacity, achieve low error floors, and have low decoding complexity. In this paper, we propose a novel category of low-density parity-check (LDPC) codes, based on protograph codes with local irregularity. This new code family generalizes conventional protograph-based LDPC codes and is capable of reducing the iterative decoding threshold of the conventional counterpart. We introduce an adapted version of the protograph extrinsic information transfer (PEXIT) algorithm to estimate decoding thresholds on the binaryinput additive white Gaussian noise channel, perform optimizations on the local irregularity, and simulate the performance of some constructed codes.

## Efficient Mitigation of Error Floors in Quantum Error Correction Using Non-Binary Low-Density Parity-Check Codes

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11195217
- **Type**: conference
- **Published**: 22-27 June
- **Authors**: Kenta Kasai
- **PDF**: https://ieeexplore.ieee.org/document/11195217
- **Abstract**: In this paper, we propose an efficient method to reduce error floors in quantum error correction using non-binary low-density parity-check (LDPC) codes. We identify and classify cycle structures in the parity-check matrix where estimated noise becomes trapped, and develop tailored decoding methods for each cycle type. For Type-I cycles, we propose a method to make the difference between estimated and true noise degenerate. Type-II cycles are shown to be un-correctable, while for Type-III cycles, we utilize the fact that cycles in non-binary LDPC codes do not necessarily correspond to codewords, allowing us to estimate the true noise. Our method significantly improves decoding performance and reduces error floors.

## Construction of QC-LDPC Codes with Girth $g$ from the Hermite Normal Form of a Matrix

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11195483
- **Type**: conference
- **Published**: 22-27 June
- **Authors**: Anthony Gómez-Fonseca
- **PDF**: https://ieeexplore.ieee.org/document/11195483
- **Abstract**: The problem of determining the existence of a protograph-based QC-LDPC code with girth $g$ and shortest blocklength for a prescribed protograph has been investigated in the literature. In some of these works, the goal was to obtain an algebraic expression for the blocklength in terms of the dimensions of the biadjacency matrix of the protograph and a lifting factor $N$. An algebraic expression has been found for $N$ when $g> 4$ is desired in the case of the fully connected (all-one) protograph but only lower bounds for the cases with larger girth. Computer search has been used in most cases to determine the exact value for $N$ that gives the shortest blocklength for a particular protograph. In this paper, we present a promising connection between the lifting factor $N$ (and therefore the blocklength of a QC-LDPC code) and the product of the pivots of the Hermite normal form of a matrix constructed from certain substructures in the protograph called tailless backtrackless closed (TBC) walks.

## Regular LDPC Codes on BMS Wiretap Channels

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11195323
- **Type**: conference
- **Published**: 22-27 June
- **Authors**: Madhura Pathegama, Alexander Barg
- **PDF**: https://ieeexplore.ieee.org/document/11195323
- **Abstract**: We improve the secrecy guarantees for transmission over BMS wiretap channels that relies on regular LDPC codes. Previous works (Thangaraj e.a., 2007, 2010) showed that LDPC codes achieve secrecy capacity of some classes of wiretap channels while leaking $o(n)$ bits of information over $n$ uses of the channel. We improve the security component of these results by reducing the leakage parameter to $O\left(\log ^{2} n\right)$. While this result stops short of proving strong security, it goes beyond the general uniformity properties of capacity-approaching code families.

## Analysis and Design of Improved 5G LDPC Codes for Faster-Than-Nyquist Signaling

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11195595
- **Type**: conference
- **Published**: 22-27 June
- **Authors**: Jiayi Yang, Qianfan Wang, Shuangyang Li +4
- **PDF**: https://ieeexplore.ieee.org/document/11195595
- **Abstract**: This paper focuses on the analysis and design of improved 5G low-density parity-check (LDPC) codes for faster-than-Nyquist (FTN) signaling. We first propose the protograph-based extrinsic information transfer (PEXIT) chart analysis for the LDPC-coded FTN system using the sum-product algorithm (SPA) based on the Ungerboeck observation model, where the distribution of the output mutual information from the detector is approximately derived using least squares fitting. With the proposed PEXIT chart analysis, we then design the improved LDPC codes for the coded FTN signaling aiming to achieve a lower decoding threshold and thereby better error performance. The proposed codes are optimized based on the raptor-like structure of the 5G LDPC codes and also support rate compatibility. The proposed codes reveals two distinct LDPC code design criteria for FTN signaling, i.e., 1) no information bits should be punctured; 2) columns with high column weights should be removed in the base graph. The advantages of the proposed codes are explicitly verified by our numerical results, where noticeable coding gains compared to existing codes and coded Nyquist systems can be observed.

## The Performance of Long Quantum LDPC Codes Based on the Hypergraph Product

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11195678
- **Type**: conference
- **Published**: 22-27 June
- **Authors**: Mert Gökduman, Hanwen Yao, Henry D. Pfister
- **PDF**: https://ieeexplore.ieee.org/document/11195678
- **Abstract**: Quantum low-density parity-check (LDPC) codes based on the hypergraph product (HGP) provide a promising approach to achieving fault-tolerant quantum computation with small overheads. In this work, we investigate the performance of long HGP codes whose component codes are classical LDPC codes. We focus on the quantum erasure channel and consider both maximum-likelihood decoding and iterative decoding. For sufficiently long codes, we clearly observe a threshold behavior for the tested codes as the block length increases. Moreover, we find that the performance curves of long LDPC HGP codes exhibit both a waterfall region near the threshold and an error floor region as the channel quality increases. These observations provide some new insights about the design of LDPC HGP codes.

## Subcode Ensemble Decoding of Linear Block Codes

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11195423
- **Type**: conference
- **Published**: 22-27 June
- **Authors**: Jonathan Mandelbaum, Holger Jäkel, Laurent Schmalen
- **PDF**: https://ieeexplore.ieee.org/document/11195423
- **Abstract**: Low-density parity-check (LDPC) codes together with belief propagation (BP) decoding yield exceptional error correction capabilities in the large block length regime. Yet, there remains a gap between BP decoding and maximum likelihood decoding for short block length LDPC codes. In this context, ensemble decoding schemes yield both reduced latency and good error rates. In this paper, we propose subcode ensemble decoding (SCED), which employs an ensemble of decodings on different subcodes of the code. To ensure that all codewords are decodable, we use the concept of linear coverings and explore approaches for sampling suitable ensembles for short block length LDPC codes. Monte-Carlo simulations conducted for three LDPC codes demonstrate that SCED improves decoding performance compared to stand-alone decoding and automorphism ensemble decoding. In particular, in contrast to existing schemes, e.g., multiple bases belief propagation and automorphism ensemble decoding, SCED does not require the NP-complete search for low-weight dual codewords or knowledge of the automorphism group of the code, which is often unknown.

## Optimizing Hypergraph Product Codes with Random Walks, Simulated Annealing and Reinforcement Learning

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11195424
- **Type**: conference
- **Published**: 22-27 June
- **Authors**: Bruno Costa Alves Freire, Nicolas Delfosse, Anthony Leverrier
- **PDF**: https://ieeexplore.ieee.org/document/11195424
- **Abstract**: Hypergraph products are quantum low-density parity-check (LDPC) codes constructed from two classical LDPC codes. Although their dimension and distance depend only on the parameters of the underlying classical codes, optimizing their performance against various noise channels remains challenging. This difficulty partly stems from the complexity of decoding in the quantum setting. The standard, ad hoc approach typically involves selecting classical LDPC codes with large girth. In this work, we focus on optimizing performance against the quantum erasure channel. A key advantage of this channel is the existence of an efficient maximum-likelihood decoder, which enables us to employ optimization techniques based on sampling random codes, such as Reinforcement Learning (RL) and Simulated Annealing (SA). Our results indicate that these techniques improve performance relative to the state-of-the-art.

## Belief Propagation Decoding for Short Codes on Structured Sparse Parity-Check Matrices

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11195685
- **Type**: conference
- **Published**: 22-27 June
- **Authors**: Yifei Shen, Zongyao Li, Emmanuel Boutillon +5
- **PDF**: https://ieeexplore.ieee.org/document/11195685
- **Abstract**: As successfully adopted in standard long code scenarios, belief propagation (BP) decoding has been considered a promising universal decoding candidate for next-generation wireless communications. However, when applied to short codes, BP decoding suffers from poor error correction performance due to harmful cycle structures in the Tanner graph. In this paper, we address this issue by designing a structured, sparse parity-check matrix (ssPCM) framework, composed of multiple cycle-free parity-check row blocks (PCRBs). The resulting ssPCMs feature regular row weights and perform better than the state-of-theart 4 -cycle-free row redundant PCMs across Bose-Chaudhuri-Hocquenghem (BCH) codes of length 63.

## In-Memory BER Estimation Using Syndromes of LDPC Codes

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11195686
- **Type**: conference
- **Published**: 22-27 June
- **Authors**: Yotam Gershon, Yuval Cassuto
- **PDF**: https://ieeexplore.ieee.org/document/11195686
- **Abstract**: In-memory computing architectures highly improve computation latency and power compared to von Neumann architectures suffering the memory wall. However, maintaining reliability is challenging due to the difficulty in implementing error-correction coding within memory. We propose a scheme in which strong codes can be used for in-memory computing, while avoiding their costly decoding when error rates are sufficiently small. The key idea and thrust of the paper is to complement the design of LDPC codes to also provide accurate estimation of the input bit-error rate (BER). Toward that, we derive analytical results and give code-design insights for BER estimation in two frameworks: minimizing the mean-squared error (MSE), and estimating threshold crossing as a hypothesis-testing problem.

## BF-Max: an Efficient Bit Flipping Decoder with Predictable Decoding Failure Rate

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11195380
- **Type**: conference
- **Published**: 22-27 June
- **Authors**: Alessio Baldelli, Marco Baldi, Franco Chiaraluce +1
- **PDF**: https://ieeexplore.ieee.org/document/11195380
- **Abstract**: The Bit-Flipping (BF) decoder, thanks to its very low computational complexity, is widely employed in post-quantum cryptographic schemes based on Moderate Density Parity Check codes in which, ultimately, decryption boils down to syndrome decoding. In such a setting, for security concerns, one must guarantee that the Decoding Failure Rate (DFR) is negligible. Such a condition, however, is very difficult to guarantee, because simulations are of little help and the decoder performance is difficult to model theoretically. In this paper, we introduce a new version of the BF decoder, that we call BF-Max, characterized by the fact that in each iteration only one bit (the least reliable) is flipped. When the number of iterations is equal to the number of errors to be corrected, we are able to develop a theoretical characterization of the DFR that tightly matches with numerical simulations. We also show how BF-Max can be implemented efficiently, achieving low complexity and making it inherently constant time. With our modeling, we are able to accurately predict values of DFR that are remarkably lower than those estimated by applying other approaches.

## On the Efficacy of the Peeling Decoder for the Quantum Expander Code

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11195550
- **Type**: conference
- **Published**: 22-27 June
- **Authors**: Jefrin Sharmitha Prabhu, Abhinav Vaishya, Shobhit Bhatnagar +3
- **PDF**: https://ieeexplore.ieee.org/document/11195550
- **Abstract**: The problem of recovering from qubit erasures has recently gained attention as erasures occur in many physical systems such as photonic systems, trapped ions, superconducting qubits and circuit quantum electrodynamics. While several linear-time decoders for error correction are known, their errorcorrecting capability is limited to half the minimum distance of the code, whereas erasure correction allows one to go beyond this limit. As in the classical case, stopping sets pose a major challenge in designing efficient erasure decoders for quantum LDPC codes. In this paper, we show through simulation, that an attractive alternative here, is the use of quantum expander codes in conjunction with the peeling decoder that has linear complexity. We also discuss additional techniques including small-set-flip decoding, that can be applied following the peeling operation, to improve decoding performance and their associated complexity.

## PAC Codes with Bounded-Complexity Sequential Decoding: Pareto Distribution and Code Design

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11195375
- **Type**: conference
- **Published**: 22-27 June
- **Authors**: Mohsen Moradi, Hessam Mahdavifar
- **PDF**: https://ieeexplore.ieee.org/document/11195375
- **Abstract**: Recently, a novel variation of polar codes known as polarization-adjusted convolutional (PAC) codes has been introduced by Arıkan. These codes significantly outperform conventional polar and convolutional codes, particularly for short codeword lengths, and are shown to operate very close to the optimal bounds. It has also been shown that if the rate profile of PAC codes does not adhere to certain polarized cutoff rate constraints, the computation complexity for their sequential decoding grows exponentially. In this paper, we address the converse problem, demonstrating that if the rate profile of a PAC code follows the polarized cutoff rate constraints, the required computations for its sequential decoding can be bounded with a distribution that follows a Pareto distribution. This serves as a guideline for the rate-profile design of PAC codes. For a high-rate PAC $(1024,899)$ code, simulation results show that the PAC code with Fano decoder, when constructed based on the polarized cutoff rate constraints, achieves a coding gain of more than $0.75 \mathbf{~ d B}$ at a frame error rate (FER) of $10^{-5}$ compared to the state-of-the-art 5G polar and LDPC codes.

## Bounds and New Constructions for Girth-Constrained Regular Bipartite Graphs

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11195214
- **Type**: conference
- **Published**: 22-27 June
- **Authors**: Sheida Rabeti, Mohsen Moradi, Hessam Mahdavifar
- **PDF**: https://ieeexplore.ieee.org/document/11195214
- **Abstract**: In this paper, we explore the design and analysis of regular bipartite graphs motivated by their application in lowdensity parity-check (LDPC) codes specifically with constrained girth and in the high-rate regime. We focus on the relation between the girth of the graph, and the size of the sets of variable and check nodes. We derive bounds on the size of the vertices in regular bipartite graphs, showing how the required number of check nodes grows with respect to the number of variable nodes as girth grows large. Furthermore, we present two constructions for bipartite graphs with girth $\mathcal{G}=8$; one based on a greedy construction of ($w_{c}, w_{r}$) -regular graphs, and another based on semi-regular graphs which have uniform column weight distribution with a sublinear number of check nodes. The second construction leverages sequences of integers without any length- 3 arithmetic progression and is asymptotically optimal while maintaining a girth of 8. Also, both constructions can offer sparse parity-check matrices for high-rate codes with medium-to-large block lengths. Our results solely focus on the graph-theoretic problem but can potentially contribute to the ongoing effort to design LDPC codes with high girth and minimum distance, specifically in high code rates.

## Interplay Between Belief Propagation and Transformer: Differential-Attention Message Passing Transformer

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11195462
- **Type**: conference
- **Published**: 22-27 June
- **Authors**: Chin Wa Ken Lau, Xiang Shi, Ziyan Zheng +2
- **PDF**: https://ieeexplore.ieee.org/document/11195462
- **Abstract**: Transformer-based neural decoders have emerged as a promising approach to error correction coding, combining data-driven adaptability with efficient modeling of long-range dependencies. This paper presents a novel decoder architecture that integrates classical belief propagation principles with transformer designs. We introduce a differentiable syndrome loss function leveraging global codebook structure and a differential-attention mechanism optimizing bit and syndrome embedding interactions. Experimental results demonstrate consistent performance improvements over existing transformer-based decoders, with our approach surpassing traditional belief propagation decoders for short-to-medium length LDPC codes.

## A Strategy to Detect Error Propagation in Sliding Window Decoding of SC-LDPC Codes

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11195331
- **Type**: conference
- **Published**: 22-27 June
- **Authors**: Mauro M. M. Costantino, Massimo Battaglioni, David G. M. Mitchell
- **PDF**: https://ieeexplore.ieee.org/document/11195331
- **Abstract**: Spatially Coupled Low-Density Parity-Check (SCLDPC) codes are characterized by very long codeword lengths. For this reason, they are usually decoded with sliding window algorithms, which allow piecewise processing and decoding of the codeword symbols. In order to mitigate error propagation, it is possible to adapt strategies, such as non-uniform window sizes and node doping. In this paper, we propose a novel adaptive decoding schedule, which can be integrated with the aforementioned strategies. Numerical results confirm that the proposed approach can successfully detect error propagation events with more accuracy than conventional log-likelihood ratio-based approaches. Simulation results show that the error rate performance of time-invariant SC-LDPC codes significantly improves when the proposed strategies are adopted.

## Random Modulation: Achieving Asymptotic Replica Optimality Over Arbitrary Norm-Bounded and Spectrally Convergent Channel Matrices

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11195253
- **Type**: conference
- **Published**: 22-27 June
- **Authors**: Lei Liu, Yuhao Chi, Shunqi Huang
- **PDF**: https://ieeexplore.ieee.org/document/11195253
- **Abstract**: This paper introduces a random modulation technique that is decoupled from the channel matrix, allowing it to be applied to arbitrary norm-bounded and spectrally convergent channel matrices. The proposed random modulation constructs an equivalent dense and random channel matrix, ensuring that the signals undergo sufficient statistical channel fading. It also guarantees the asymptotic replica maximum a posteriori (MAP) bit-error rate (BER) optimality of approximate message passing (AMP)-type detectors for linear systems with arbitrary norm-bounded and spectrally convergent channel matrices when their state evolution has a unique fixed point. Then, a lowcomplexity cross-domain memory approximate message passing (CD-MAMP) detector is proposed for random modulation, leveraging the sparsity of the time-domain channel and the randomness of the random transform-domain channel. Furthermore, the optimal power allocation schemes are derived to minimize the replica MAP BER and maximize the replica constrained capacity of random-modulated linear systems, assuming the availability of channel state information (CSI) at the transceiver. Numerical results show that the proposed random modulation can achieve BER and block-error rate (BLER) performance gains of up to $2 \sim 3 \mathbf{d B}$ compared to existing OFDM/OTFS/AFDM with 5G-NR LDPC codes, under both average and optimized power allocation.

## High-Rate Spatially Coupled LDPC Codes Based on Massey's Convolutional Self-Orthogonal Codes

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11195322
- **Type**: conference
- **Published**: 22-27 June
- **Authors**: Daniel J. Costello, Min Zhu, David G. M. Mitchell +1
- **PDF**: https://ieeexplore.ieee.org/document/11195322
- **Abstract**: We propose a new class of high-rate spatially coupled LDPC (SC-LDPC) codes based on the convolutional selforthogonal codes (CSOCs) first introduced by Massey. The SCLDPC codes are constructed by treating the irregular graph corresponding to the parity-check matrix of a systematic rate $R=(n-1) / n$ CSOC as a convolutional protograph. The protograph can then be lifted using permutation matrices to generate a high-rate SC-LDPC code whose strength depends on the lifting factor. The SC-LDPC codes constructed in this fashion can be decoded using iterative belief propagation based sliding window decoding. To improve performance, a non-systematic version of a C SOC parity-check matrix is then proposed by making a slight modification to the systematic construction. Even though the parity-check matrix is in non-systematic form, we show how systematic encoding can still be performed. We also show that the non-systematic convolutional protograph has a guaranteed girth and free distance and that these properties carry over to the lifted versions. Numerical results are included demonstrating that CSOC-based SC-LDPC codes (i) have performance at least as good as that of SC-LDPC codes commonly found in the literature, and (ii) have iterative decoding thresholds comparable to those of existing SC-LDPC code designs.

## Binary BMST Coding for Near-Lossless Compression of Q-Ary Source

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11195246
- **Type**: conference
- **Published**: 22-27 June
- **Authors**: Xiao Ma, Yinchu Wang, Qianli Ma +2
- **PDF**: https://ieeexplore.ieee.org/document/11195246
- **Abstract**: In this paper, we propose a new coding approach to near-lossless compression of $Q$-ary sources by utilizing a sparsifier and block Markov superposition transmission (BMST) codes. The symbols from a $Q$-ary source are mapped to fixedlength binary vectors by the sparsifier such that the symbols with higher probabilities are mapped to vectors of lower weights. The binary sparse sequences are then compressed in a BMST manner. The most distinguished feature of the proposed source coding is that the error propagation can be mitigated in the presence of noise. Numerical results show that the proposed scheme performs well for $Q$-ary sources, providing a universal but simple way to achieve near-lossless coding at rates approaching the source entropy.

## Transformer-Based Decoding in Concatenated Coding Schemes Under Synchronization Errors

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11195598
- **Type**: conference
- **Published**: 22-27 June
- **Authors**: Julian Streit, Franziska Weindel, Reinhard Heckel
- **PDF**: https://ieeexplore.ieee.org/document/11195598
- **Abstract**: We consider the reconstruction of a codeword from multiple noisy copies, each independently corrupted by insertion, deletion, and substitution errors. This problem arises, for example, in DNA data storage. A common code construction uses a concatenated code with an outer linear block code and an inner marker code, decoded via Belief Propagation (BP) and the Bahl-Cocke-Jelinek-Raviv (BCJR) algorithm, respectively. However, the BCJR algorithm scales exponentially with the number of nois copies, making reconstruction from more than about four copies infeasible. In this paper, we introduce BCJRFormer, a transformer-based neural inner decoder for marker codes. BCJRFormer achieves error rates comparable to the BCJR algorithm for single-message transmissions while scaling only quadratically with the number of noisy copies. This makes BCJRFormer well suited for DNA data storage, where multiple reads of the same DNA sequence are common. To further reduce the bit error rate, we replace the BP outer decoder with a transformer-based decoder. Combined, this results in a performant and efficient end-to-end transformer-based pipeline for decoding multiple noisy copies corrupted by insertion, deletion, and substitution errors.

## Probability Distribution of Sneak Path Rate in Resistive Random-Access Memory Arrays

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11195609
- **Type**: conference
- **Published**: 22-27 June
- **Authors**: Guanghui Song, Junqi Wang, Meiru Gao +2
- **PDF**: https://ieeexplore.ieee.org/document/11195609
- **Abstract**: The sneak path (SP) issue presents a substantial challenge for resistive random-access memory (ReRAM), significantly affecting data storage reliability. The SP rate, which represents the proportion of memory cells impacted by SPs, is a crucial parameter influencing the probability of data detection errors. In this paper, we concentrate on analyzing the probability distribution of the SP rate in ReRAM arrays that incorporate imperfect selectors. Our research indicates that when ReRAM stores data following an independent and identically distributed (i.i.d.) Bernoulli distribution with parameter $q$, and the array size is large, the SP rate approximates a Gaussian distribution. The mean and variance of this distribution can be explicitly derived as functions of the number of selector failures, parameter $q$, and the array size.

## Enhanced Min-Sum Decoding of Quantum Codes with Iteration Dynamics Memory

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11195509
- **Type**: conference
- **Published**: 22-27 June
- **Authors**: Dimitris Chytas, Nithin Raveendran, Bane Vasić
- **PDF**: https://ieeexplore.ieee.org/document/11195509
- **Abstract**: In this paper, we propose a novel message-passing decoding approach that leverages the degeneracy of quantum low-density parity-check codes to enhance decoding performance, eliminating the need for serial scheduling or post-processing. Our focus is on two-block Calderbank-Shor-Steane (CSS) codes, which are composed of symmetric stabilizers that hinder the performance of conventional iterative decoders with uniform update rules. Specifically, our analysis shows that, under the isolation assumption, the min-sum decoder fails to converge when constant-weight errors are applied to symmetric stabilizers, as variable-to-check messages oscillate in every iteration. To address this, we introduce a decoding technique that exploits this oscillatory property by applying distinct update rules: variable nodes in one block utilize messages from previous iterations, while those in the other block are updated conventionally. Logical error-rate results demonstrate that the proposed de-coder significantly outperforms the normalized min-sum decoder and achieves competitive performance with belief propagation enhanced by order-zero ordered statistics decoding, all while maintaining linear complexity in the code's block length.

## Improved Decoding of Tanner Codes

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11195639
- **Type**: conference
- **Published**: 22-27 June
- **Authors**: Zhaienhe Zhou, Zeyu Guo
- **PDF**: https://ieeexplore.ieee.org/document/11195639
- **Abstract**: In this paper, we present improved decoding algorithms for expander-based Tanner codes. We begin by developing a randomized linear-time decoding algorithm that, under the condition that $\delta d_{0}>2$, corrects up to $\alpha n$ errors for a Tanner code $T\left(G, C_{0}\right)$, where $G$ is a ($c, d, \alpha, \delta$) bipartite expander with $n$ left vertices, and $C_{0} \subseteq \mathbb{F}_{2}^{d}$ is a linear inner code with minimum distance $d_{0}$. This result improves upon the previous work of Cheng, Ouyang, Shangguan, and Shen (RANDOM 2024), which required $\delta d_{0}>3$. We further derandomize the algorithm to obtain a deterministic linear-time decoding algorithm with the same decoding radius. Our algorithm improves upon the previous deterministic algorithm of Cheng et al. by achieving a decoding radius of $\alpha n$, compared with the previous radius of $\frac{2 \alpha}{d_{0}(1+0.5 c \delta)} n$. Additionally, we investigate the size-expansion trade-off introduced by the recent work of Chen, Cheng, Li, and Ouyang (IEEE TIT 2023), and use it to provide new bounds on the minimum distance of Tanner codes. Specifically, we prove that the minimum distance of a Tanner code $T\left(G, C_{0}\right)$ is approximately $f_{\delta}^{-1}\left(\frac{1}{d_{0}}\right) \alpha n$, where $f_{\delta}(\cdot)$ is the Size-Expansion Function. As another application, we improve the decoding radius of our decoding algorithms from $\alpha n$ to approximately $f_{\delta}^{-1}\left(\frac{2}{d_{0}}\right) \alpha n$.

## Removal of Small Weight Stopping Sets for Asynchronous Unsourced Multiple Access

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11195696
- **Type**: conference
- **Published**: 22-27 June
- **Authors**: Frederik Ritter, Jonathan Mandelbaum, Alexander Fengler +2
- **PDF**: https://ieeexplore.ieee.org/document/11195696
- **Abstract**: In this paper, we analyze the formation of small stopping sets in joint factor graphs describing a frame-asynchronous two-user transmission. Furthermore, we propose an algorithm to completely avoid small stopping sets in the joint factor graph over the entire range of symbol delays. The error floor caused by these stopping sets is completely mitigated. Our key observation is that, while the order of bits in the codeword is irrelevant in a single-user environment, it turns out to be crucial in an asynchronous, unsourced two-user system. Subsequently, our algorithm finds a reordering of variable nodes which avoids the smallest stopping set in the joint graph. We show that further improvements can be achieved when girth optimization of the single-user graphs by progressive edge growth (PEG) is used in combination with our proposed algorithm. Starting with a randomized code construction with optimized degree distribution, our simulation results show that PEG followed by the proposed algorithm can improve the average per user probability of error in a noiseless channel by almost two orders of magnitude for a broad range of frame delays.

## Belief Propagation Decoding on a Sparsified Graph Ensemble of the Surface Code

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11195585
- **Type**: conference
- **Published**: 22-27 June
- **Authors**: Boqing Zhang, Hanwen Yao, Henry D. Pfister
- **PDF**: https://ieeexplore.ieee.org/document/11195585
- **Abstract**: This work exploits the product structure of surface codes to improve their belief propagation (BP) decoding performance. To promote BP convergence, we sparsify the original surface code graph with respect to its topological product structure to break its dominant short cycles. Analytical justification of the proposed sparsification methods is provided through analysis and minimum-weight perfect matching (MWPM) on sparsified graphs. The results demonstrate that the increase in logical error is well-controlled in both worst-case and average-case scenarios. Practically, we show that BP on a single sparsified graph significantly outperforms BP on the original graph in terms of convergence and total error rate. To further address the performance loss relative to MWPM caused by sparsification, we construct an ensemble of sparsified decoding graphs. Numerical results show that running standard BP on the ensemble, without any post-processing or auxiliary subroutines, achieves a threshold of 9. 0 \% on surface codes under Pauli- $X$ noise, closely matching the BP-OSD threshold of approximately 9. 1 \%.

## Capacities of Entanglement Distribution from a Central Source

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11195480
- **Type**: conference
- **Published**: 22-27 June
- **Authors**: Xinan Chen, Stefano Chessa, Ian George +2
- **PDF**: https://ieeexplore.ieee.org/document/11195480
- **Abstract**: Distribution of entanglement is an essential task in quantum information processing and the realization of quantum networks. In our work, we theoretically investigate the scenario where a central source prepares an N-partite entangled state and transmits each entangled subsystem to one of $N$ receivers through noisy quantum channels. The receivers are then able to perform local operations assisted by unlimited classical communication to distill target entangled states from the noisy channel output. In this operational context, we define the EPR distribution capacity and the GHZ distribution capacity of a quantum channel as the largest rates at which Einstein-Podolsky-Rosen (EPR) states and Greenberger-Horne-Zeilinger (GHZ) states can be faithfully distributed through the channel, respectively. We establish lower and upper bounds on the EPR distribution capacity by connecting it with the task of assisted entanglement distillation. We also construct an explicit protocol consisting of a combination of a quantum communication code and a classical-post-processing-assisted entanglement generation code, which yields a simple achievable lower bound for generic channels. As applications of these results, we give an exact expression for the EPR distribution capacity over two erasure channels and bounds on the EPR distribution capacity over two generalized amplitude damping channels. We also bound the GHZ distribution capacity, which results in an exact characterization of the GHZ distribution capacity when the most noisy channel is a dephasing channel.

## Threshold Selection for Iterative Decoding of $(v,\ w)$-Regular Binary Codes

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11195438
- **Type**: conference
- **Published**: 22-27 June
- **Authors**: Alessandro Annechini, Alessandro Barenghi, Gerardo Pelosi
- **PDF**: https://ieeexplore.ieee.org/document/11195438
- **Abstract**: Iterative bit flipping decoders are an efficient and effective choice for decoding codes which admit a sparse parity-check matrix. Among these, sparse $(v,\ w)$-regular codes, which include LDPC and MDPC codes, are of particular interest both for efficient data correction and the design of cryptographic primitives. Throughout the iterative decoding process, the bit flipping thresholds can be determined either statically or during the decoder execution, by using information coming from the initial syndrome value and its updates. In this work, we analyze a two-iterations parallel hard decision bit flipping decoder and propose concrete criteria for threshold determination, backed by a closed form model. In doing so, we introduce a new tightly fitting model for the distribution of the Hamming weight of the syndrome after the first decoder iteration and substantial improvements on the decoding failure rate (DFR) estimation with respect to existing approaches.

## Optimal Moments on Redundancies in Job Cloning

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11195588
- **Type**: conference
- **Published**: 22-27 June
- **Authors**: Sahasrajit Sarmasarkar, Harish Pillai
- **PDF**: https://ieeexplore.ieee.org/document/11195588
- **Abstract**: We consider the problem of job assignment where a master server aims to compute some tasks and is provided a few child servers to compute under a uniform straggling pattern where each server is equally likely to straggle. We distribute tasks to the servers so that the master is able to receive most of the tasks even if a significant number of child servers fail to communicate. We first show that all balanced assignment schemes have the same expectation on the number of distinct tasks received and then study the variance. We show constructions using a generalization of “Balanced Incomplete Block Design” [1], [2] minimizes the variance, and constructions based on repetition coding schemes attain the largest variance. Note: An extended version is available at https://arxiv.org/pdf/2402.12584.

## Sequential Interval Passing for Compressed Sensing

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11195431
- **Type**: conference
- **Published**: 22-27 June
- **Authors**: Salman Habib, Taejoon Kim, Rémi A. Chou
- **PDF**: https://ieeexplore.ieee.org/document/11195431
- **Abstract**: The reconstruction of sparse signals from a limited set of measurements poses a significant challenge as it necessitates a solution to an underdetermined system of linear equations. Compressed sensing (CS) deals with sparse signal reconstruction using techniques such as linear programming (LP) and iterative message passing schemes. The interval passing algorithm (IPA) is an attractive CS approach due to its low complexity when compared to LP. In this paper, we propose a sequential IPA that is inspired by sequential belief propagation decoding of low-density-parity-check (LDPC) codes used for forward error correction in channel coding. In the sequential setting, each check node (CN) in the Tanner graph of an LDPC measurement matrix is scheduled one at a time in every iteration, as opposed to the standard “flooding” interval passing approach in which all CNs are scheduled at once per iteration. The sequential scheme offers a significantly lower message passing complexity compared to flooding IPA on average, and for some measurement matrix and signal sparsity, a complexity reduction of 36% is achieved. We show both analytically and numerically that the reconstruction accuracy of the IPA is not compromised by adopting our sequential scheduling approach.

## A Novel Covert Timing Channel for Cloud FPGAs

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11133099
- **Type**: conference
- **Published**: 22-25 June
- **Authors**: Brian Udugama, Darshana Jayasinghe, Hassaan Saadat +2
- **PDF**: https://ieeexplore.ieee.org/document/11133099
- **Abstract**: This paper presents a novel covert timing channel (CTC) that enables a malicious entity to exfiltrate data from a benign cloud FPGA user without requiring dedicated outgoing messages from the cloud FPGA, minimizing the detection risk by both the victim and the cloud service provider. The proposed CTC exploits the handshake signals of the Advanced eXtensible Interface (AXI) protocol and interpacket delay of the Internet to establish the CTC from a cloud FieldProgrammable Gate Array (FPGA) to an off-cloud computer. This paper analyzes the bit-error rate (BER) of the AXI-based CTC under varying conditions and demonstrates its effectiveness in truly enabling remote power analysis attacks on cloud services, such as Amazon Web Services Elastic Compute Cloud (AWS EC2). The proposed CTC achieves a BER as low as 0.01988%.

## Enhancing Learning Experience: A Step-by-Step Guide for Reed-Solomon Code Decoding

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11083501
- **Type**: conference
- **Published**: 19-21 June
- **Authors**: Adriana Borodzhieva, Dimitar Stoyanov
- **PDF**: https://ieeexplore.ieee.org/document/11083501
- **Abstract**: This paper explores innovative methods for teaching Reed-Solomon decoding to enhance student engagement and understanding of error-correcting codes. As a widely used technique in digital communication, Reed-Solomon codes present certain challenges, including the complexity of their encoding and decoding processes. Students often struggle with issues involved in the decoding process. To address these difficulties, we propose using color-coded visual aids and step-by-step explanations that simplify the decoding workflow. Additionally, the paper highlights the importance of collaborative group activities and real-world applications to showcase the practical significance of Reed-Solomon codes. These strategies aim to create a more effective and engaging learning environment, fostering a deeper comprehension of coding theory among students.

## Advancements and Challenges in Error Control Coding for Modern Communication Systems: A Comprehensive Review

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11085375
- **Type**: conference
- **Published**: 19-20 June
- **Authors**: Vivek Arya, Basit Mohi Ud Din Naikoo
- **PDF**: https://ieeexplore.ieee.org/document/11085375
- **Abstract**: Error control coding (ECC) forms the backbone of modern communication systems, ensuring reliable data transfer despite channel impairments. Over the decades, ECC techniques have evolved significantly to address the increasing demands of high-speed and robust communication. This paper provides a detailed review of recent advancements in ECC techniques, including block codes, convolutional codes, LDPC, turbo, and polar codes, with a particular focus on their theoretical foundations, practical implementations, and performance in real-world systems. Applications of these techniques in diverse communication systems such as 5G, IoT, satellite communications, and data storage are thoroughly explored. Furthermore, this review discusses key challenges in implementing ECC in modern systems, including achieving low latency, high energy efficiency, and adaptability to dynamic channel conditions. Emerging trends, such as the integration of machine learning in code design and decoding and the role of quantum error correction in future networks, are highlighted. The paper concludes by identifying potential research directions that can shape the future of ECC and ensure its continued relevance in next-generation communication systems.

## UAV/HAPS Feeder Link in W and D Bands: A Feasibility Study

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11114548
- **Type**: conference
- **Published**: 18-20 June
- **Authors**: Alberto Tarable, Giuseppe Virone, Roberto Nebuloni +7
- **PDF**: https://ieeexplore.ieee.org/document/11114548
- **Abstract**: The airborne segment is of capital importance for TN-NTN integration, in 6 G -and-beyond telecommunication systems. This paper deals with the practical design, in terms of hardware, antennas and bandwidth, of a feeder link for UAV/HAPS in W and D bands, where currently there are no operational air or space systems. Our results show that delivering 2 Gbits/s for the UAV and 5 Gbits/s for the HAPS in the downlink is possible even in rainy conditions. Exploiting dual-polarization links and using a bandwidth of 5 GHz, a downlink throughput as high as 40 Gbits/s is achievable for both considered bands in clear-sky conditions.

## Performance Analysis of an Advanced HARQ Scheme Based on LDPC Coupled Codes

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11174663
- **Type**: conference
- **Published**: 17-20 June
- **Authors**: Yiyun Jian, Lukasz Lopacinski, Eckhard Grass
- **PDF**: https://ieeexplore.ieee.org/document/11174663
- **Abstract**: In this paper, we investigate the effectiveness of a newly proposed frame superposition Hybrid Automatic Repeat reQuest (HARQ) scheme, which adopts different variants of spatially coupled low-density parity-check (LDPC) codes. The construction of the method with the use of 5 G new radio (NR) LDPC codes is explained in detail. Bit error rate (BER), frame error rate (FER), and the projected data goodput in additive white Gaussian noise (AWGN) and Rayleigh block fading channels are investigated. The HARQ scheme is based on frame combination by using spatially coupled LDPC codes. It outperforms all classical variants of HARQ and can, hence, be seen as a potential successor of the classical methods. The main cost is the need for more complicated LDPC decoding, whereby the decoder needs to support the decoding of two or even more blocks at the same time.

## Attention-Based Semantic Communication Systems for Artificial Intelligence of Things

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11174402
- **Type**: conference
- **Published**: 17-20 June
- **Authors**: Fan Jiang, Hongjian Yan, Lei Liu +1
- **PDF**: https://ieeexplore.ieee.org/document/11174402
- **Abstract**: With the rapid growth in demand for intelligent services and the corresponding surge in massive data, semantic communication has emerged as a promising paradigm for intelligent service applications. However, existing approaches are limited by their capability to effectively extract semantic features. To address this challenge and improve the quality of transmitted image, this paper proposes an attention-based semantic communication system for image transmission. Specifically, by adaptively weighting spatial and channel features through the Convolutional Block Attention Module (CBAM), the proposed approach enhances the representation of crucial information. Furthermore, focusing on Artificial Intelligence of Things (AIoT) applications, where intelligent tasks require autonomous decision-making based on perceived information, the system is trained on two receiver tasks: reconstruction and classification, enabling it to adapt to diverse application. Experimental results demonstrate that our proposed method outperforms both deep learning based joint source and channel coding (JSCC) and the combination of joint photographic experts group(JPEG) and low-density parity-check (LDPC) in terms of image reconstruction quality. Furthermore, the proposed system achieves high classification accuracy and exhibits robustness across varying compression ratios.

## GSVD Based Precoding Scheme for Nonlinear Massive MIMO-RSMA Networks

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11174910
- **Type**: conference
- **Published**: 17-20 June
- **Authors**: Oussama Ben Haj Belkacem, Rui Dinis
- **PDF**: https://ieeexplore.ieee.org/document/11174910
- **Abstract**: In this paper, we consider the precoder design for multiuser multiple input multiple output (MU-MIMO) systems based on orthogonal frequency domain multiplexing (OFDM) with rate splitting at the transmitter. We propose precoding and decoding schemes based on generalized singular value decomposition (GSVD), both for underloaded and overloaded communication systems that support the transmission of multiple common and private streams. To address performance degradation caused by nonlinearities from GSVD-RSMA, an iterative distortion canellation receiver-aided precoding method is introduced. The approach improves stream detection without requiring successive interference cancellation, enhancing robustness in nonlinear environments1.

## M-JSCC: An Asymmetric Semantic Communication Architecture for 6G Intelligent Networks

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11174786
- **Type**: conference
- **Published**: 17-20 June
- **Authors**: Pengfei Ren, Jingjing Wang, Zhiwei Wang +3
- **PDF**: https://ieeexplore.ieee.org/document/11174786
- **Abstract**: Semantic communication (SC) is considered a critical technology for breaking through the Shannon limit and achieving low-latency, high-capacity 6 G transmission. However, previous SC systems have typically employed a symmetrical architecture to enhance data recovery capabilities, resulting in a strong coupling between the encoder and decoder. In this paper, we introduce a novel asymmetric SC system, termed masked joint source-channel coding (M-JSCC), which significantly enhances the encoder's versatility by allowing it to adapt to different decoder models tailored to specific task requirements. Moreover, we abandon traditional convolutional neural networks and adopt the innovative transformer to increase model capacity further. Additionally, we empower the model with data generation capabilities to combat interference and distortion during wireless transmission, achieving robust semantic transmission. As a result, extensive experiments verify that our M-JSCC achieves better semantic understanding and performance across various tasks and different channel conditions.

## DNN-Assisted Constellation Design for SIC-Free Hierarchical QAM-Based Multiple Access

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11174455
- **Type**: conference
- **Published**: 17-20 June
- **Authors**: Xuan Liu, Ming Zhao, Shengli Zhou
- **PDF**: https://ieeexplore.ieee.org/document/11174455
- **Abstract**: QAMA, a recently proposed multiple access technology, utilizes hierarchical quadrature amplitude modulation (QAM) to achieve the same rate region as conventional multi-user superposition transmission (MUST) without requiring successive interference cancellation (SIC) at receivers. This is particularly advantageous for low-cost Internet of Things (IoT) devices. The key process involves adjusting the constellation to generate transmission modes that enable SIC-free operation and span the desired rate region. However, determining the optimal constellation currently requires either an exhaustive search over all Euclidean distances, which is computationally intensive, or storing a lookup codebook, which demands significant memory. To address this, a deep neural network (DNN)-based approach is proposed for QAMA constellation design. The approach employs a binary classification network to identify transmission modes under given user signal-to-noise ratios (SNRs), followed by a regression network to predict optimal Euclidean distances. Numerical results demonstrate that the DNN-based method significantly reduces computational complexity while maintaining performance comparable to exhaustive search.

## Enhancing Reliability of Smart Systems Using In-Memory Computing

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11058664
- **Type**: conference
- **Published**: 16-19 June
- **Authors**: Mojtaba Mahdavi
- **PDF**: https://ieeexplore.ieee.org/document/11058664
- **Abstract**: In the era of smart computing, efficient and reliable communication is paramount for applications spanning from IoT devices to large-scale cyber-physical systems. Error correction coding schemes play a critical role in ensuring data integrity and enhancing performance in smart communication systems. Traditional implementations of coding schemes often face challenges with latency and energy consumption. This paper proposes an innovative approach utilizing in-memory computing (IMC) to implement channel coding mechanisms. By integrating computation directly within memory, the proposed IMC-based channel coding scheme significantly reduces data transfer bottlenecks, leading to improved latency and energy efficiency. Performance evaluations demonstrate that this approach not only meets the stringent requirements of modern smart systems but also offers scalability and high-reliability across various application domains.

## Polar-OTFS System for Underwater Acoustic Communication

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11104571
- **Type**: conference
- **Published**: 16-19 June
- **Authors**: Aiwen Xuan, Kai Niu, Zhiqiang He +4
- **PDF**: https://ieeexplore.ieee.org/document/11104571
- **Abstract**: In underwater communication environments, significant delays and Doppler spread pose challenges to the reliability of traditional communication schemes. In this paper, we present a polar coded orthogonal time frequency space (Polar-OTFS) system that significantly improves transmission performance in underwater communication. On the transmitting side, the system first performs polar encoding, followed by OTFS mapping and transmission. On the receiving side, the system incorporates the unitary approximate message passing (UAMP) detection algorithm, ensuring efficient and precise time-frequency synchronization detection. Furthermore, to mitigate the impact of deep fading in offshore environments, the system incorporates a Dual-Threshold Successive Cancellation List decoding algorithm (DT-SCL), which adaptively adjusts the initial and maximum list size based on channel estimation, thereby enhancing decoding efficiency. Ocean experiment results demonstrate that the proposed system achieves error-free transmission over a distance of 25 kilometers at a transmission rate of 3 kbps in a marine environment at a depth of 1200 meters, showcasing exceptional communication performance and robustness.

## Neural Adaptive Offest Min-Sum Algorithm for LDPC Decoding

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11165549
- **Type**: conference
- **Published**: 11-13 June
- **Authors**: Haojia Zhang, Shuai Han, Hao Chen
- **PDF**: https://ieeexplore.ieee.org/document/11165549
- **Abstract**: With the rapid development of deep learning and its applications in physical layer communication, deep learning-based channel coding has gradually become a research hotspot. In this paper, based on the neural offset min-sum (NOMS) low-density parity-check (LDPC) decoding network, we propose a neural adaptive offset min-sum (NAOMS) LDPC decoding network. By considering the current input values of the check nodes when learning the additive offset parameters and introducing an adaptive offset weight vector, we can better leverage deep learning techniques. Experimental results show that, with a slight increase in complexity, the proposed decoder achieves a 0.8dB improvement in bit error rate (BER) over the NOMS LDPC decoding network. Moreover, the NAOMS decoder requires fewer learning offset parameters compared to the NOMS decoder.

## Adaptive Quantized and Normalized QC-LDPC Universal Block-Parallel Decoder

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11165566
- **Type**: conference
- **Published**: 11-13 June
- **Authors**: Xia An, Chao Zhang, Jian Song
- **PDF**: https://ieeexplore.ieee.org/document/11165566
- **Abstract**: As wireless communication systems evolve, new frameworks place increasing demands on terminal performance, including throughput, latency, power consumption, and size. Software-Defined Radio (SDR) systems have the potential to support multiple communication standards and enabling on-demand upgrades due to their flexibility. However, purely software-based implementations for physical layer protocols reduce efficiency, necessitating the use of external accelerators such as FPGA for specialized computation. Specifically, channel decoding contributes a lot to the physical layer’s complexity, and thus is highly demand for FPGA specialized implementation while retaining the universality of the decoding architecture in some level. This paper presents an adaptive quantized and normalized QC-LDPC universal decoder based on a block-parallel architecture with pipeline and instruction-driven approach. The proposed decoder improves throughput and reduces computational complexity while maintaining flexibility for various QC-LDPC codes. Experimental results demonstrate that the adaptive quantization and normalization scheme significantly outperforms existing methods in terms of decoding performance and maximum frequency, offering a more efficient solution for SDR systems.

## A Comparative Study of Short-length Error Correction Codes in Datacasting Scenarios

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11165540
- **Type**: conference
- **Published**: 11-13 June
- **Authors**: Yiqiao Lu, Yin Xu, Hao Ju +4
- **PDF**: https://ieeexplore.ieee.org/document/11165540
- **Abstract**: This paper evaluates and compares the performance of short-length error correction codes for datacasting in Geographically Segmented Localcasting (GSL) scenarios. While GSL enhances spectrum efficiency and coverage, challenges such as synchronization and interference remain. Robust error correction codes are essential to optimize datacasting, particularly for short code lengths. This study investigates polar codes, Polarization-Adjusted Convolutional (PAC) codes, Bose-Chaudhuri-Hocquenghem (BCH) codes, and Low-Density Parity-Check (LDPC) codes over different channels. Polar and PAC codes demonstrate strong performance for short block lengths but suffer from decoding complexity and latency. BCH codes are efficient but their effectiveness declines with hard-decision decoding and longer code lengths. Although the performance of LDPC codes may underperform under short-length code conditions, they exhibit high adaptability to diverse channel conditions and can achieve lower decoding delays in high signal-to-noise ratio (SNR) scenarios.

## New 5G-NR-Like LDPC Code Design for HRLLC Scenarios

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11165523
- **Type**: conference
- **Published**: 11-13 June
- **Authors**: Zhitong He, Kewu Peng, Jian Song
- **PDF**: https://ieeexplore.ieee.org/document/11165523
- **Abstract**: To meet the requirements of hyper-reliable and low-latency communication (HRLLC) scenarios, a new design of 5G-NR-Like LDPC codes is proposed, which majorly optimizes the minimum distance property, to lower the error floor for short to medium code lengths. Meanwhile, progressive row extension techniques are employed for base matrix design, and progressive edge growth and lifting techniques are employed for lifting design, to achieve desirable decoding performance across the nested code rates and code lengths under given design complexity. The hybrid list decoding algorithm is employed to further improve the decoding performance for short block lengths. Simulation results demonstrate the effectiveness of our new 5G-NR-Like LDPC code design and hybrid list decoding algorithm.

## Implementation and Field Verification of ATSC 3.0 Channel Bonding

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11165621
- **Type**: conference
- **Published**: 11-13 June
- **Authors**: Bo-Mi Lim, Hoiyoon Jung, Sungjun Ahn +5
- **PDF**: https://ieeexplore.ieee.org/document/11165621
- **Abstract**: To overcome the capacity limitation of a single radio frequency (RF) channel, Advanced Television Systems Committee (ATSC) 3.0 incorporates channel bonding technology. This technology combines two adjacent or non-adjacent RF channels, promising to double system capacity while maintaining the required signal-to-noise ratio (SNR). ATSC 3.0 defines two modes of channel bonding: plain channel bonding and SNR-averaged channel bonding. This paper experimentally verifies the ATSC 3.0 channel bonding in a real field environment. Furthermore, the features and potential applications of each channel bonding mode are discussed based on the test results.

## Analysis of the Possibilities of Implementation Correcting Linear Block Codes into the Modbus Protocol

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11049181
- **Type**: conference
- **Published**: 10-14 June
- **Authors**: Stepan A. Chapliyov, Alla B. Levina, Andrey I. Plotnikov
- **PDF**: https://ieeexplore.ieee.org/document/11049181
- **Abstract**: Correcting linear block codes offer a more robust approach to ensuring the integrity of transmitted data. Unlike traditional checksum algorithms, they not only detect transmission errors but also enable their correction. Modbus, a widely used communication protocol in industrial automation systems, currently relies on basic error detection mechanisms such as cycle redundancy check (CRC). This article analyzes the feasibility of integrating linear block codes into the Modbus protocol to enhance its reliability. The study evaluates various implementation scenarios and demonstrates that incorporating such codes can significantly improve error resilience with acceptable overhead.

## Comparison of wavelet-based codes with linear cyclic codes

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:11049119
- **Type**: conference
- **Published**: 10-14 June
- **Authors**: Alla B. Levina, Sergey V. Boyko
- **PDF**: https://ieeexplore.ieee.org/document/11049119
- **Abstract**: Error-correcting codes, such as classical BCH codes, are widely used in noisy channels, but emerging wavelet-based approaches offer adaptive alternatives. This article compares linear codes constructed via wavelet signal decomposition with BCH codes, analyzing their theoretical foundations: generator matrix design, syndrome decoding for BCH, and wavelet adaptation for code generation.The results show that wavelet codes achieve error correction comparable to BCH codes, while their hybrid integration retains the strengths of both methods. This validates wavelet-based codes as a viable alternative to algebraic codes, particularly in scenarios requiring flexibility or computational efficiency.
