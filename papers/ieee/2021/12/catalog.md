# IEEE Xplore — 2021-12


## Polar Codes: Encoding/Decoding and Rate-Compatible Jointly Design for HARQ System

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:9733299
- **Type**: journal
- **Published**: December 2
- **Authors**: Qiaoli Zeng, Quan Zhou, Xiangkun He +3
- **PDF**: https://ieeexplore.ieee.org/document/9733299
- **Abstract**: Polar coding are the first class of provable capacity-achieving coding techniques for a wide range of channels. With an ideal recursive structure and many elegant mathematical properties, polar codes are inherently implemented with low complexity encoding and decoding algorithms. Since the block length of the original polar construction is limited to powers of two, rate-compatible polar codes (RCPC) are presented to meet the flexible length/rate transmission requirements in practice. The RCPC codes are well-conditioned to combine with the hybrid automatic repeat request (HARQ) system, providing high throughput efficiency and such RCPC-HAPQ scheme is commonly used in delay-insensitive communication system. This paper first gives a survey of both the classical and state-of-the-art encoding/decoding algorithms for polar codes. Then the RCPC construction methods are discussed, including the puncturing, shortening, multi-kernel construction, etc. Finally, we investigate several RCPC-HARQ jointly design systems and discuss their encoding gain and re-transmission diversity gain.

## Some New Constructions of Girth-8 QC-LDPC Codes for Future GNSS

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:9570287
- **Type**: journal
- **Published**: Dec. 2021
- **Authors**: Inseon Kim, Hong-Yeop Song
- **PDF**: https://ieeexplore.ieee.org/document/9570287
- **Abstract**: In this letter, we propose a new construction of girth-8 Quasi-Cyclic Low-Density Parity-Check codes (QC-LDPC) with various lengths for the global navigation satellite systems (GNSS). This scheme combines two steps. The first is the construction of a family of regular girth-8 QC-LDPC codes of various lengths and rates with two designed sequences. The second is the performance improvement of those from the first construction of half-rate cases using a proposed weight matrix so that the result becomes type-II QC-LDPC codes. This results in some final codes with short lengths of 600, 1200, and 1800, especially for future GNSS. We performed a simulation and confirmed that the proposed QC-LDPC codes of lengths 600 and 1200 have an additional coding gain about 0.3 dB at frame error rate 10−5 over the LDPC codes used in the Global Positioning System.

## Transmitting Extra Bits With Cyclically Shifted LDPC Codes

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:9564241
- **Type**: journal
- **Published**: Dec. 2021
- **Authors**: Yinchu Wang, Ming Jiang, Xiao Ma
- **PDF**: https://ieeexplore.ieee.org/document/9564241
- **Abstract**: In this letter, we propose a simple yet efficient coding scheme to transmit extra bits by cyclically shifting a low-density parity-check (LDPC) coded sequence without any additional consumption in bandwidth or transmission energy. At the transmitter, the payload data is encoded into an LDPC coded sequence and then cyclically shifted under a pattern specified by the extra bits. At the decoder, the extra bits are first retrieved by estimating the number of cyclic shifts based on the hard or soft syndromes. After removing the effect of cyclic shift, the payload data is recovered by the LDPC decoder. Simulation results show that, with a 5G LDPC code of length 1910, up to 10 extra bits can be reliably transmitted with negligible influence on the reliability of the LDPC coded data.

## Semi-LDPC Convolutional Codes: Construction and Low-Latency Windowed List Decoding

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:9663105
- **Type**: journal
- **Published**: Dec. 2021
- **Authors**: Qianfan Wang, Suihua Cai, Li Chen +1
- **PDF**: https://ieeexplore.ieee.org/document/9663105
- **Abstract**: This paper presents a new coding scheme called semi-low-density parity-check convolutional code (semi-LDPC-CC), whose parity-check matrix consists of both sparse and dense sub-matrices, a feature distinguished from the conventional LDPC-CCs. We propose sliding-window list (SWL) decoding algorithms with a fixed window size of two, resulting in a low decoding latency but a competitive error-correcting performance. The performance can be predicted by upper bounds derived from the first event error probability and by genie-aided (GA) lower bounds estimated from the underlying LDPC block codes (LDPC-BCs), while the complexity can be reduced by truncating the list with a threshold on the difference between the soft metrics in the serial decoding implementation. Numerical results are presented to validate our analysis and demonstrate the performance advantage of the semi-LDPC-CCs over the conventional LDPC-CCs.

## Fast LDPC GPU Decoder for Cloud RAN

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:9328563
- **Type**: journal
- **Published**: Dec. 2021
- **Authors**: Jonathan Ling, Paul Cautereels
- **PDF**: https://ieeexplore.ieee.org/document/9328563
- **Abstract**: The graphical processing unit (GPU), as a digital signal processing accelerator for cloud RAN, is investigated. This letter presents a new design for a 5G NR low-density parity check code decoder running on a GPU. The algorithm is flexibly adaptable to GPU architecture to achieve high resource utilization as well as low latency. It improves on the layered algorithm by increasing parallelism on a single code word. The flexible GPU decoder (on a 24 core GPU) was found to have  $5\times $  higher throughput compared to a recent GPU flooding decoder and  $3\times $  higher throughput compared to a field programmable gate array (FPGA) decoder (757K gate). The flexible GPU decoder exhibits 1/3 decoding power efficiency of the FPGA typical of general-purpose processors. For rapid deployment and flexibility, GPUs may be suitable as cloud RAN accelerators.

## Efficient Parallel Decoding Architecture for Cluster Erasure Correcting 2-D LDPC Codes for 2-D Data Storage

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:9568927
- **Type**: journal
- **Published**: Dec. 2021
- **Authors**: Arijit Mondal, Shayan Srinivasa Garani
- **PDF**: https://ieeexplore.ieee.org/document/9568927
- **Abstract**: Native 2-D low-density parity-check (LDPC) codes provide 2-D burst erasure correction capability and have promising applications in two-dimensional magnetic recording (TDMR) technology. Though carefully constructed rastered 1-D LDPC codes can provide 2-D burst erasure correction, they are not as efficient as 2-D native codes constructed for handling the 2-D span of burst erasures. Our contributions are twofold. First, we propose a new 2-D LDPC code with girth greater than 4 by generating a parity-check tensor through stacking permutation tensors of size  $p\times p\times p$  along with the  $i,j,k$ -axes. The permutations are achieved through circular shifts on an identity tensor along different coordinate axes in such a way that it provides a burst erasure correction capability of at least  $p\times p$ . Second, we propose a fast, efficient, and scalable hardware architecture for a parallel 2-D LDPC decoder based on the proposed code construction for data storage applications. Through efficient indexing of the received messages in an RAM, we propose novel routing mechanisms for messages between the check nodes and variable nodes through a set of two barrel shifters, producing shifts along two axes. Through simulations, we show that the performance of the proposed 2-D LDPC codes matches a 1-D QC-LDPC code, with a sharp waterfall drop of three to four orders of magnitude over ~0.3 dB, for random errors over code sizes of ~32 kbits or equivalently ~ $180\times 180 2$ -D arrays. Furthermore, we prove that the proposed native 2-D LDPC codes outperform their 1-D counterparts in terms of 2-D cluster erasure correction ability. For  $p=16$  and code arrays of size  $48\times 48$ , we implemented the proposed design architecture on a Kintex-7 KC-705 field-programmable gate array (FPGA) kit, achieving a significantly high worst case throughput of 12.52 Gb/s at a clock frequency of 163 MHz.

## The Stability of Low-Density Parity-Check Codes and Some of its Consequences

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:9567663
- **Type**: journal
- **Published**: Dec. 2021
- **Authors**: Wei Liu, Rüdiger Urbanke
- **PDF**: https://ieeexplore.ieee.org/document/9567663
- **Abstract**: We study the stability of low-density parity-check codes under blockwise or bitwise maximum a posteriori decoding, where transmission takes place over a binary-input memoryless output-symmetric channel. Our study stems from the consideration of constructing universal capacity-achieving codes under low-complexity decoding algorithms, where universality refers to the fact that we are considering a family of channels with equal capacity. Consider, e.g., the right-regular sequence by Shokrollahi and the heavy-tail Poisson sequence by Luby et al. Both sequences are provably capacity-achieving under belief propagation decoding when transmission takes place over the binary erasure channel. In this paper we show that many existing capacity-achieving sequences of low-density parity-check codes are not universal under belief propagation decoding. We reveal that the key to showing this non-universality result is determined by the stability of the underlying codes. More concretely, for an ordered and complete channel family and a sequence of low-density parity-check code ensembles, we determine a stability threshold associated with them, which gives rise to a sufficient condition under which the sequence is not universal under belief propagation decoding. Moreover, we show that the same stability threshold applies to blockwise or bitwise maximum a posteriori decoding as well. We demonstrate how the stability threshold can determine an upper bound on the corresponding blockwise or bitwise maximum a posteriori threshold, revealing the operational significance of the stability threshold.

## Design of Code Pair for Protograph-LDPC Codes-Based JSCC System With Joint Shuffled Scheduling Decoding Algorithm

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:9537752
- **Type**: journal
- **Published**: Dec. 2021
- **Authors**: Zhiping Xu, Lin Wang, Shaohua Hong +1
- **PDF**: https://ieeexplore.ieee.org/document/9537752
- **Abstract**: Although there are many studies on code optimization of the joint source-channel coding (JSCC) system based on double protograph low-density parity-check codes with the joint belief propagation (JBP) algorithm, but it is still unknown whether the source code and channel code (as a code pair) can perform well when the joint shuffled scheduling decoding (JSSD) algorithm is adopted. In this letter, two decoding threshold analysis algorithms, including joint shuffled protograph extrinsic information transfer (PEXIT) and source shuffled PEXIT algorithm, are proposed to calculate joint/source decoding thresholds for this system with the JSSD algorithm. With the proposed algorithms, it is found that the optimized code pairs for this system with the JBP algorithm may not perform well with the JSSD algorithm, implying that code pair with the JSSD algorithm needs to be redesigned. Then, a two-stage optimized framework is proposed to design the code pair for this system with the JSSD algorithm. Simulations and decoding threshold analysis both show that the proposed code pair for this system with the JSSD algorithm can obtain lower error floor and better waterfall performance than the existing code pairs.

## Reliable Coded Caching Design Over Wireless Networks

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:9608974
- **Type**: journal
- **Published**: Dec. 2021
- **Authors**: Hui Wang, Qingchun Chen, Qin Huang +1
- **PDF**: https://ieeexplore.ieee.org/document/9608974
- **Abstract**: In this paper, we will show how to interpret the coded caching design from error control coding perspective. It is shown that, when the cached and non-cached contents in the placement phase is thought of as the shortened system packets and the punctured system packets, respectively, while those coded contents transmitted in the delivery phase specify the parity packets, the coded caching design can be reformulated as a collaborative error control coding problem. The challenges for arbitrary user requests and noncooperative decoding nature at every user will be highlighted to address the design criteria in order to exploit the coding gain residing in the coded caching. Our analysis unveils that, with some supplementary parity packets (SPPs) included in either the placement phase or the delivery phase, noticeable transmission reliability improvement can be realized. It is shown that the proposed design is able to flexibly fulfill the asymmetric reliable transmission requirement by placing or transmitting some SPPs only for those users in adverse conditions. It is also shown that the proposed reliable coded caching and channel coding can be further integrated into the joint network-channel coding (JNCC) framework to fully exploit the benefits of those two schemes.

## Improved generalized successive cancellation list flip decoder of polar codes with fast decoding of special nodes

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:9684773
- **Type**: journal
- **Published**: Dec. 2021
- **Authors**: Fedor Ivanov, Valerii Morishnik, Evgenii Krouk
- **PDF**: https://ieeexplore.ieee.org/document/9684773
- **Abstract**: In this paper, an improvement for SC list flip (SCL-Flip) decoding is presented for polar codes. A novel bit-selection metric for critical set (set of information symbols of polar codes being flipped during additional decoding attempts) based on path metric of successive cancellation list (SCL) decoding is suggested. With the proposed metric, the improved SCL scheme based on special nodes (SN) decoders was developed. This decoder will be denoted by GSCLF. The main idea of the proposed decoder is joint using of two approaches: first one is a fast decoding of special nodes in binary tree representation of polar code (e.g., some special nodes in tree representation of polar code that allow efficient list decoding with low complexity) and the second one is an applying of additional decoding attempts (flips) in the case when initial decoding was erroneous. The simultaneous use of these two approaches results in both a significant reduction in spatial complexity and a significant reduction in the number of computations required for decoding whereas keeping excellent performance. Simulation results presented in this paper allow us to conclude that the computational complexity of the proposed GSCLF decoder is from 66% to 80% smaller than the one of SCL-32 decoder.

## Improved Block Oriented Unit Memory Convolutional Codes

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:9534893
- **Type**: journal
- **Published**: Dec. 2021
- **Authors**: Junjie Li, Suihua Cai, Wenchao Lin +2
- **PDF**: https://ieeexplore.ieee.org/document/9534893
- **Abstract**: This paper is concerned with a special class of unit memory convolutional codes (UMCCs), called block oriented UMCCs (BOUMCCs). Distinguished from conventional UMCCs, which usually have small constraint lengths, the BOUMCCs have relatively large constraint lengths. We conduct the performance analysis by assuming a first-order Markov model, which indicates that the performance of the BOUMCCs depends critically on both the error propagation and the sub-frame error rate of the first layer. The error propagation can be alleviated by the use of partial superposition, which is specified by a superposition matrix with a fraction of columns being nulled. Given a superposition fraction, we propose a tree growing and pruning algorithm (TGPA) with a tunable sliding window, which provides a convenient way to trade off the decoding delay and the performance. We also present a structured construction and show by simulation that there is no performance degradation compared with random construction. Numerical results also show that, by taking the TBCCs as basic codes, the performance of BOUMCCs with TGPA is comparable to that of other short codes but with a more flexible construction or a lower complexity.

## A Unified Convolutional Neural Network Classifier Aided Intelligent Channel Decoder for Coexistent Heterogeneous Networks

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:9404186
- **Type**: journal
- **Published**: Dec. 2021
- **Authors**: Xiaoling Yang, Lin Zhang, Zhiqiang Wu
- **PDF**: https://ieeexplore.ieee.org/document/9404186
- **Abstract**: In coexistent heterogeneous wireless networks, receivers have to process the signaling and the data following different specifications. With the aim to automatically and intelligently identify the received signal type and then recover the data, in this paper, we propose a unified intelligent channel decoder serially concatenated by a convolutional-neural-network-based classifier and a deep learning (DL)-aided decoder. The classifier mainly consists of the convolutional layer, the batch normalization layer, and the max-pooling layer, while the DL decoder is constituted by four full connection layers. At the training stage, the unified decoder is trained to learn the distinct characteristics of encoded codewords following different specifications. Then, at the deployment stage, the classifier will extract the distinct structural features and identify the coding pattern. Thus, the DL decoder could choose an appropriate set of neural network parameters for information recovery. Simulation results demonstrate that our proposed intelligent decoder achieves better reliability performances than benchmark schemes over both additive white Gaussian noise and Rayleigh fading channels.

## Two Birds With One Stone: Simultaneous Jamming and Eavesdropping With the Bayesian-Stackelberg Game

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:9535143
- **Type**: journal
- **Published**: Dec. 2021
- **Authors**: Nan Qi, Wei Wang, Fuhui Zhou +4
- **PDF**: https://ieeexplore.ieee.org/document/9535143
- **Abstract**: In adversarial scenarios, it is crucial to timely monitor what tactical messages that opponent transmitters are sending to intended receiver(s), and disrupt the transmissions immediately if in need. The issue becomes more challenging in face of an intelligent transmitter. To address the above-stated issue, a full-duplex (FD) technique is utilized to enable simultaneous jamming and eavesdropping (SJE) at a friendly jammer node. In particular, the “Two Birds with One Stone” strategy is utilized at the jammer node to realize effective rate degradation and information eavesdropping. A confrontation game between an intelligence-empowered FD jammer and its opponent is investigated. Specifically, to capture their adversarial relationship in an environment with incomplete information, a power-domain Bayesian-Stackelberg game is proposed. The existence of a Stackelberg equilibrium (SE) power solution is proved. The semi-closed-form solutions of SE are derived, which are proved to be asymptotically optimal (have a gap of less than 1% with the exact utility), and improves the jammer node 10% utility compared with the Nash equilibrium. Additionally, the SJE strategy outperforms the half-duplex (HD) and other benchmark schemes.

## Sparsity-Exploiting Blind Receiver Algorithms for Unsourced Multiple Access in MIMO and Massive MIMO Channels

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:9551997
- **Type**: journal
- **Published**: Dec. 2021
- **Authors**: Jiaai Liu, Xiaodong Wang
- **PDF**: https://ieeexplore.ieee.org/document/9551997
- **Abstract**: We propose new transmission schemes and receiver algorithms for unsourced multiple access (UMA) in MIMO and massive MIMO channels. Each active transmitter’s information bits are first channel encoded. The coded bits are divided into sub-blocks and each sub-block is modulated and transmitted. For both MIMO and massive MIMO channels, the conventional nonlinear modulation can be employed where each sub-block of coded bits is mapped to a transmitted signal vector. For the massive MIMO channel, we propose a new hybrid modulation scheme to reduce the receiver complexity, where the first sub-block is nonlinearly modulated, and the subsequent sub-blocks are linearly modulated and spread by the first sub-block signal. We also propose sparsity-exploiting blind receiver algorithms. Specifically, for the MIMO case, we exploit the codeword sparsity inherent in the UMA system, and a channel clustering technique, to estimate the channel and the transmitted signal of each transmitter. For the massive MIMO, in addition to the codeword sparsity, we further exploit the channel sparsity and user sparsity in estimating the channel and transmitted signal of each transmitter. The proposed receiver algorithms for both MIMO and massive MIMO channels output either hard or soft estimates of the coded bits, and therefore single-user channel decoding of the information bits can be performed for each transmitter. Extensive simulation results are provided to demonstrate the performances of the proposed algorithms.

## Design of Coded Slotted ALOHA With Interference Cancellation Errors

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:9573456
- **Type**: journal
- **Published**: Dec. 2021
- **Authors**: Charles Dumas, Lou Salaün, Iman Hmedoush +2
- **PDF**: https://ieeexplore.ieee.org/document/9573456
- **Abstract**: Coded Slotted ALOHA (CSA) is a random access scheme based on the application of packet erasure correcting codes to transmitted packets and the use of successive interference cancellation at the receiver. CSA has been widely studied and a common assumption is that interference cancellation can always be applied perfectly. In this paper, we study the design of CSA protocol, accounting for a non-zero probability of error due to imperfect interference cancellation (IC). A classical method to evaluate the performance of such protocols is density evolution, originating from coding theory, and that we adapt to our assumptions. Analyzing the convergence of density evolution in asymptotic conditions, we derive the optimal parameters of CSA, i.e., the set of code selection probabilities of users that maximizes the channel load. A new parameter is introduced to model the packet loss rate of the system, which is non-zero due to potential IC errors. Multi-packet reception (MPR) and the performance of 2-MPR are also studied. We investigate the trade-off between optimal load and packet loss rate, which sheds light on new optimal distributions that outperform known ones. Finally, we show that our asymptotic analytical results are consistent with simulations obtained on a finite number of slots.

## Clustering-Based Blind Detection Aided by SC-LDGM Codes

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:9573301
- **Type**: journal
- **Published**: Dec. 2021
- **Authors**: Xing Li, Qianfan Wang, Jiachen Sun +2
- **PDF**: https://ieeexplore.ieee.org/document/9573301
- **Abstract**: In this paper, we propose clustering-based blind detection methods with the aid of systematic convolutional low density generator matrix (SC-LDGM) codes. Inspired by the fact that the received signals naturally fall into clusters in the block-fading channels, we develop a system constrained Gaussian mixture model (SCGMM) by taking into account the inherent characteristics of communication systems, in which the parameters can be estimated by the expectation-maximization (EM) algorithm. We also present an initialization method for the proposed SCGMM to accelerate convergence. After clustering, a decoding algorithm of SC-LDGM codes is designed to resolve the centroid ambiguity. To further improve the detection performance in the low signal-to-noise (SNR) and deep fading scenarios, we propose an improved label-assisted (ILA) method, which integrates the label-assisted (LA) information into the blind detection algorithm. Numerical results show that the performance of our methods can closely approach the performance with perfect channel state information (CSI). The simulation results also show that the performance can be improved by increasing the encoding memory.

## Spinal Codes Over Fading Channel: Error Probability Analysis and Encoding Structure Improvement

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:9468924
- **Type**: journal
- **Published**: Dec. 2021
- **Authors**: Aimin Li, Shaohua Wu, Jian Jiao +2
- **PDF**: https://ieeexplore.ieee.org/document/9468924
- **Abstract**: In order to facilitate the reliability of data transmission of Spinal codes over the fading channel, performance analysis of Spinal codes is conducted, and an improved encoding structure is proposed. First, we derive an approximate frame error rate (FER) upper bound for Spinal codes over the Rayleigh fading channel in the finite block length (FBL) regime. Then, inspired by the FER analysis process, we propose an improved encoding structure, named self-concatenation structure, to reduce the FER of Spinal codes. In addition, a parallel structure is proposed for Spinal codes to improve the decoding throughput. For the self-concatenation structure, simulation results show that it exhibits a significant gain in anti-noise performance compared with the original Spinal codes over the Rayleigh fading channel. For the parallel structure, we find that by combining the parallel structure with the self-concatenation structure, not only is the encoding and decoding throughput of Spinal codes significantly improved but also the FER of Spinal codes is reduced.

## Convolutional Neural Network (CNN)-Based Detection for Multi-Level-Cell NAND Flash Memory

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:9537753
- **Type**: journal
- **Published**: Dec. 2021
- **Authors**: Zhifang Shi, Yi Fang, Yingcheng Bu +1
- **PDF**: https://ieeexplore.ieee.org/document/9537753
- **Abstract**: With the increase of program/erase (PE) cycles and retention time, it is difficult to predict the threshold-voltage distributions for detection in NAND flash memory. To accurately acquire the log-likelihood ratios (LLRs) without the knowledge of threshold-voltage distributions, a convolutional neural network (CNN)-based detection algorithm is proposed for the multi-level-cell (MLC) flash memory. The CNN-based detection algorithm employs the trained CNN to accurately calculate the LLRs for each threshold-voltage region. Furthermore, we develop a CNN-aided read-voltage design scheme to optimize the read voltages by maximizing the mutual information between the coded bits and their corresponding LLRs. Exploiting the proposed scheme, we first design three hard-decision read voltages, and then formulate more soft-decision read voltages to further improve the detection performance. Simulation results demonstrate that the CNN-based detection algorithm can achieve performance approaching that of the optimal detection algorithm.

## Low-Complexity Blind Equalization in Q/V Band Satellite Links: An Experimental Assessment

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:9535298
- **Type**: journal
- **Published**: Dec. 2021
- **Authors**: Tommaso Rossi, Mauro De Sanctis, Simone Di Domenico +2
- **PDF**: https://ieeexplore.ieee.org/document/9535298
- **Abstract**: In the near future, high-throughput satellite systems are expected to reach the milestone of terabit/s capacity through the exploitation of “beyond Ka-band” frequencies in the feeder link, in particular, Q and V bands (and possibly beyond). The use of such high-frequency bands, combined with the need to build radio-frequency (RF) chains with an affordable cost, leads analog RF circuits to work far from their ideal operating point, thus producing relevant linear and nonlinear signal distortions. In this article, an experimental assessment has been performed to evaluate the effectiveness of a low-complexity blind equalizer, namely the constant-modulus algorithm (CMA), to reduce the performance degradation due to such signal distortions. Benefits introduced by the CMA equalizer have been evaluated in a real Q/V-band satellite link using the DVB-S2 standard, in the framework of the experimental campaign of the Italian Space Agency, carried out through the Alphasat TDP#5 “Aldo Paraboni” payload.

## A Low-Complexity Hybrid Linear and Nonlinear Precoder for Line-Of-Sight Massive MIMO With Max-Min Power Control

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:9474948
- **Type**: journal
- **Published**: Dec. 2021
- **Authors**: Amirashkan Farsaei, Ulf Gustavsson, Alex Alvarado +1
- **PDF**: https://ieeexplore.ieee.org/document/9474948
- **Abstract**: In line-of-sight (LOS) massive MIMO, there is a nonnegligible probability that the channel vectors of some users become correlated. In these correlated scenarios, nonlinear precoders can be used instead of linear precoders at the cost of high computational complexity. To reduce the complexity of nonlinear precoders, hybrid linear and nonlinear precoders have been suggested in 5G New Radio (NR). In this paper, we find the probability that there is at least one pair of correlated users and we find the average number of correlated users. We propose a hybrid linear and nonlinear precoder (HLNP) with max-min power control for which the served users are divided into two groups. By employing a proposed modified Tomlinson-Harashima Precoding (THP), we design and combine the transmit vectors of the two groups such that inter-group interference is removed. Simulation results show that by employing HLNP instead of zero-forcing, the required transmit power to assure a given average block error rate (BLER) with 95% probability is reduced. For a 64-antennas BS, when modified THP is used for 3 out of 10 users in HLNP, the transmit power is reduced by up to 4.70 dB to assure an average BLER of 10−2 using 16QAM and 64QAM constellations with NR low-density parity-check codes.

## Turbo DFE Assisted Time-Frequency Packing for Probabilistically Shaped Terabit Superchannels

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:9594678
- **Type**: journal
- **Published**: Dec. 2021
- **Authors**: Mrinmoy Jana, Lutz Lampe, Jeebak Mitra
- **PDF**: https://ieeexplore.ieee.org/document/9594678
- **Abstract**: We present a probabilistically shaped (PS) time-frequency-packing (TFP) wavelength-division multiplexing superchannel system employing higher order modulation (HoM) formats, with an objective to improve the spectral efficiency (SE). However, TFP systems suffer from inter-symbol interference (ISI) and/or inter-carrier interference (ICI). Additionally, the bandwidth limitations of the wavelength selective switches in the fiber link may cause severe ISI for the edge sub-channels (SCs) in a superchannel. Mitigation of such interferences is particularly challenging for HoM systems, since the implementation of the well-known turbo equalization schemes, such as the Bahl-Cocke-Jelinek-Raviv equalizer, is computationally challenging for larger constellations. In this paper, we investigate an expectation propagation based, computationally efficient, turbo decision feedback equalizer for ISI cancellation, in tandem with a parallel interference cancellation based ICI mitigation. By optimizing the parameters in the shaping and the packing dimensions, we show through our numerical results that the proposed PS-TFP superchannels enabling 1.8 Tbps data rates offer up to 1.05 dB packing gain over an unpacked system using the same modulation format, and a 1.15 dB shaping gain over an unshaped system that uses a lower modulation order to achieve the same SE.

## Algebraic Design of a Class of Rate 1/3 Quasi-Cyclic LDPC Codes

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:9685071
- **Type**: conference
- **Published**: 7-11 Dec. 
- **Authors**: R. Michael Tanner
- **PDF**: https://ieeexplore.ieee.org/document/9685071
- **Abstract**: An algebraic design procedure is given for constructing rate 1/3 quasi-cyclic LDPC codes with Tanner graphs with girth 6. Parity check matrices consist of 2 × 3 block matrices of circulants of size p, a prime, exhibiting invariance under the action of a subgroup of the multiplicative group mod p. The group invariance converts the problem of avoiding short cycles into that of choosing orbits to solve connectivity constraints. A series of very low density H matrix codes constructed show surprisingly good minimum distances.

## Chained LDPC Codes via Partial Information Coupling and Partial Parity Superposition

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:9682151
- **Type**: conference
- **Published**: 7-11 Dec. 
- **Authors**: Qianfan Wang, Li Chen, Xiao Ma
- **PDF**: https://ieeexplore.ieee.org/document/9682151
- **Abstract**: This paper presents a new class of chained low-density parity-check (LDPC) codes for the transport block (TB) based transmission protocol, in which a TB consists of multiple code blocks (CBs). The proposed chained LDPC codes are constructed by coupling together all CBs of a TB into a single chain, where partial information bits between every two adjacent LDPC CBs are shared using the partial information coupling (PIC) technique and partial parity bits are superimposed onto the following LDPC CB using the partial superposition (PS) technique, resulting in a PIC-PS-LDPC code. The proposed construction is universal in the sense that it is applicable to any existing LDPC codes including the random LDPC codes and the structured LDPC codes to obtain extra coding gains. More importantly, the proposed PIC-PS-LDPC codes can have encoder/decoder implemented using the structure of the underlying LDPC codes. Numerical results show that the PS technique can further improve the PIC-LDPC codes, and the PIC technique can further improve the PS-LDPC codes. They also show that the proposed PIC-PS-LDPC codes with the 5G New Radio (5G-NR) LDPC codes as the mother codes can yield a coding gain of up to 0.6 dB over the conventional 5G-NR LDPC codes.

## Modeling a Sliding Window Decoder for Spatially Coupled LDPC Codes

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:9682064
- **Type**: conference
- **Published**: 7-11 Dec. 
- **Authors**: Min Zhu, David G. M. Mitchell, Michael Lentmaier +1
- **PDF**: https://ieeexplore.ieee.org/document/9682064
- **Abstract**: Due to their capacity achieving performance with sliding window decoding (SWD), spatially coupled LDPC (SC-LDPC) codes are emerging as candidates for next generation channel coding applications. In this paper we present a general model of SWD of SC-LDPC codes and develop an analysis that allows us to estimate error probability performance under decoder error propagation conditions that can occur when low latency operation is desired. We also show how the model parameters can be estimated and indicate how the model can be used to predict the performance of code doping techniques used to mitigate the effects of decoder error propagation.

## FPGA Implementations of Layered MinSum LDPC Decoders Using RCQ Message Passing

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:9685732
- **Type**: conference
- **Published**: 7-11 Dec. 
- **Authors**: Caleb Terrill, Linfang Wang, Sean Chen +4
- **PDF**: https://ieeexplore.ieee.org/document/9685732
- **Abstract**: Non-uniform message quantization techniques such as reconstruction-computation-quantization (RCQ) improve error-correction performance and decrease hardware complexity of low-density parity-check (LDPC) decoders that use a flooding schedule. Layered MinSum RCQ (L-msRCQ) enables message quantization to be utilized for layered decoders and irregular LDPC codes. We investigate field-programmable gate array (FPGA) implementations of L-msRCQ decoders. Three design methods for message quantization are presented, which we name the Lookup, Broadcast, and Dribble methods. The decoding performance and hardware complexity of these schemes are compared to a layered offset MinSum (OMS) decoder. Simulation results on a (16384, 8192) protograph-based raptor-like (PBRL) LDPC code show that a 4-bit L-msRCQ decoder using the Broadcast method can achieve a 0.03 dB improvement in error-correction performance while using 12% fewer registers than the OMS decoder. A Broadcast-based 3-bit L-msRCQ decoder uses 15% fewer lookup tables, 18% fewer registers, and 13% fewer routed nets than the OMS decoder, but results in a 0.09 dB loss in performance.

## Parity Check Matrix Partitioning for Layered Decoding of QC-LDPC Codes

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:9682155
- **Type**: conference
- **Published**: 7-11 Dec. 
- **Authors**: Teng Lu, Xuan He, Peng Kang +1
- **PDF**: https://ieeexplore.ieee.org/document/9682155
- **Abstract**: In this paper, we propose two algorithms to partition the parity check matrices (PCMs) for the layered decoding of quasi-cyclic low-density parity-check (QC-LDPC) codes, which targets to reduce the hardware complexity and computation delay. We formulate the optimization problem of PCM partitioning, and systematically propose the principle of partitioning to guarantee a block cyclic shift property for different decoding layers. After that, we develop both greedy and enumerative partitioning algorithms, aiming at minimizing the maximum column weight of each decoding layer. We further derive a tight lower bound for the minimum achievable maximum column weight, which can help to early terminate a searching process once the lower bound is achieved. Simulation results show that the proposed algorithms are generally capable of achieving the lower bound or differ by one.

## Refined Density Evolution Analysis of LDPC Codes for Successive Interference Cancellation

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:9685529
- **Type**: conference
- **Published**: 7-11 Dec. 
- **Authors**: Satoshi Takabe, Tadashi Wadayama, Masahito Hayashi
- **PDF**: https://ieeexplore.ieee.org/document/9685529
- **Abstract**: Successive interference cancellation (SIC) is a fundamental decoding technique for Gaussian multiple access channels (GMAC). In SIC, transmit signals of each user are separately decoded. In this paper, we analyze an asymptotic decoding threshold of SIC decoding for practical low-density parity-check (LDPC) codes over $N$-user GMAC. Conventionally, the decoding thresholds are evaluated based on the so-called channel approximation (CA) in which the channel model of each decoding stage of a SIC decoder is approximated by simple Gaussian noise channels resulting in errors of decoding thresholds. To avoid this, we propose a refined density evolution (DE) analysis called DE-SIC which uses mixed-Gaussian noise channels corresponding to each decoding stage. We demonstrate DE-SIC by solving a received power optimization problem in GMAC and comparing it to the conventional DE analysis with CA. The results show that DE-SIC accurately evaluates the decoding thresholds whereas the conventional analysis underestimates the thresholds.

## SISO Decoding of U-UV Codes

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:9682136
- **Type**: conference
- **Published**: 7-11 Dec. 
- **Authors**: Changyu Wu, Li Chen
- **PDF**: https://ieeexplore.ieee.org/document/9682136
- **Abstract**: U-UV structural coding with algebraic component codes can provide competent error-correction performance in the short-to-medium length regime. Constituted by BCH component codes and its ordered statistics decoding (OSD), the successive cancellation list (SCL) decoding of U-UV codes can outperform that of polar codes. However, the current SCL decoding is a soft-in hard-out (SIHO) process. Exploiting its list decoding feature, this paper proposes a soft-in soft-out (SISO) decoding for U-UV codes, providing the key technique for the codes to be further engaged in an iterative system. The proposal is designed based on the recursive structure of U-UV codes and the list decoding feature for both the component and the structural codes. Both the decoding complexity and its soft information transfer characteristics are also shown.

## Fault-Tolerant Computation Meets Network Coding: Optimal Scheduling in Parallel Computing

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:9685369
- **Type**: conference
- **Published**: 7-11 Dec. 
- **Authors**: Congduan Li, Chee Wei Tan, Jingting Li +1
- **PDF**: https://ieeexplore.ieee.org/document/9685369
- **Abstract**: We propose an optimal scheduling strategy to enable fault-tolerant reliable computation to protect the integrity of computation. Specifically, we determine the optimal redundancy-failure rate tradeoff to incorporate redundancy into parallel computing units running multiple-precision arithmetic that are useful for applications such as asymmetric cryptography and fast integer multiplication. Inspired by network coding, we propose coding matrices to strategically map partial computation to available computing units, so that the central unit can reliably reconstruct the results of any failed machine without recalculations to yield the final correct computation output. We propose optimization-based algorithms to efficiently construct the optimal coding matrices subject to fault tolerance specifications. Performance evaluation demonstrates that the optimal scheduling effectively reduces the overall running time of parallel computing while resisting wide-ranging failure rates.

## A Hybrid MLC and BICM Coded-Modulation Framework for 6G

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:9682143
- **Type**: conference
- **Published**: 7-11 Dec. 
- **Authors**: Ruimin Yuan, Jian Fang, Rongchi Xu +2
- **PDF**: https://ieeexplore.ieee.org/document/9682143
- **Abstract**: To meet requirements of higher spectral efficiency and higher throughput in future 6G communications, we propose a hybrid multilevel coding (MLC) and bit-interleaved coded modulation (BICM) scheme based on the Ungerboeck set partitioning. Then an optimized signal mapper is designed to improve the error-correcting performance. Simulation results show that, when 256-QAM is used, our scheme gains up to 2.5 dB at a BER of 10−5 for the spectral efficiency of 7 bits/s/Hz over AWGN channels compared with the conventional BICM scheme. And the gap may increase further with the use of larger constellations. With the aid of an outer code, our scheme performs 0.5 dB better than the BICM scheme over independent Rayleigh fading channels.

## Neural Joint Source-Channel Decoding using Arithmetic Codes

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:9682040
- **Type**: conference
- **Published**: 7-11 Dec. 
- **Authors**: Zijian Liang, Kai Niu, Jincheng Dai
- **PDF**: https://ieeexplore.ieee.org/document/9682040
- **Abstract**: Traditional iterative joint source-channel coding (JSCD) scheme based on soft-in-soft-out (SISO) decoding for arithmetic codes (AC) has a very high implementation complexity, which will cause an unbearable decoding latency due to a plenty of AC decoding steps and cross-layer interactions between physical layer and application layer. To tackle this, we propose a learning-based joint source-channel decoding approach, neural-JSCD, which consists of a series of AC SISO decoders and channel SISO decoders. The proposed approach introduces weights and offset factors to the simplified AC SISO decoders and damping factors to the output extrinsic information of both AC and channel SISO decoders, cooperated with trainable low-density parity-check (LDPC) neural decoders to realize the iterative decoding for AC. Through a greedy training method based on gradient descent, the learnable factors of neural-JSCD can be tuned to learn the a priori information of arithmetic codes, thus avoiding the great number of AC decoding steps together with cross-layer interactions during the iterative decoding process and rapidly reducing the implementation complexity of iterative AC decoding. Simulation results show that with a better decoding performance, neural-JSCD can reduce the number of iterations by at least 50% with no AC decoding steps and cross-layer interactions compared to traditional JSCD, in consequence, it greatly reduces the decoding latency of iterative decoding.

## Federated Learning based Audio Semantic Communication over Wireless Networks

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:9685654
- **Type**: conference
- **Published**: 7-11 Dec. 
- **Authors**: Haonan Tong, Zhaohui Yang, Sihua Wang +3
- **PDF**: https://ieeexplore.ieee.org/document/9685654
- **Abstract**: In this paper, the problem of audio based semantic communication is investigated over wireless networks. In the considered model, wireless edge devices must transmit large-sized audio data to a server using semantic communication techniques. The techniques enable the transmission of audio semantic information which captures the contextual features of audio signals. To extract the semantic information from audio signals, a wave to vector (wav2vec) architecture based autoencoder that consists of convolutional neural networks (CNNs) is proposed. The proposed autoencoder enables high-accuracy audio transmission with small amounts of data. To further improve the accuracy of semantic information extraction, federated learning (FL) is implemented over multiple devices and a server. Simulation results show that the proposed algorithm can converge effectively and can reduce the mean square error (MSE) between the recovered audio signals and the source audio signals by nearly 100 times, compared to a traditional coding scheme.

## Negentropy-Aware Loss Function for Trainable Belief Propagation in Coded MIMO Detection

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:9685863
- **Type**: conference
- **Published**: 7-11 Dec. 
- **Authors**: Daichi Shirase, Takumi Takahashi, Shinsuke Ibi +3
- **PDF**: https://ieeexplore.ieee.org/document/9685863
- **Abstract**: We consider large multi-user detection (MUD) via deep unfolding-aided belief propagation (BP) in coded multi-user MIMO (MU-MIMO) systems. A BP detector optimized (trained) by data-driven-tuning of embedded internal parameters achieves low-complexity and high-accuracy MUD while compensating practical imperfections. However, in actual implementation, these parameters should be optimized according to system parameters, e.g., modulation and coding scheme (MCS). In particular, when channel coding is used, it is vital not only to minimize the mean square error (MSE) but also to enhance the Gaussianity of the output log-likelihood ratio (LLR), in order to maximize the error correction capability of the subsequent soft-decision decoder. To that end, a novel loss function based on a weighted average of negentropy, which is a key measure to evaluate the Gaussianity, and MSE of the detector output is proposed. Simulation results show that the trainable Gaussian BP (T-GaBP) detector optimized with the proposed negentropy-aware loss function significantly improves the bit error rate (BER) performance of the decoder output and substantially outperforms the T-GaBP optimized with the typical MSE loss function.

## Coded Random Access for 6G: Intra-Frame Spatial Coupling with ACKs

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:9682156
- **Type**: conference
- **Published**: 7-11 Dec. 
- **Authors**: Lorenzo Valentini, Alberto Faedi, Marco Chiani +1
- **PDF**: https://ieeexplore.ieee.org/document/9682156
- **Abstract**: A massive multiple access scheme, capable of serving a large number of uncoordinated devices while fulfilling reliability and latency constraints, is proposed. The scheme belongs to the class of coded random access protocols and is tailored to massive multiple input multiple output (MIMO) base station processing. It achieves high reliability owing to an intra-frame spatial coupling effect, obtained by a simple device access protocol combined with acknowledgements (ACKs) from the base station. The proposed scheme is particularly interesting to address the challenges of massive machine-type communications in the framework of the future 6G systems.

## Analysis of Pointing Loss Effects in Deep Space Optical Links

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:9685465
- **Type**: conference
- **Published**: 7-11 Dec. 
- **Authors**: Lorenzo Valentini, Alberto Faedi, Enrico Paolini +1
- **PDF**: https://ieeexplore.ieee.org/document/9685465
- **Abstract**: Owing to the extremely narrow beams, a main issue in optical deep space communications is represented by miss-pointing errors, which may severely degrade the system performance and availability. In this paper, we address pointing losses in the case in which both the receiver and the transmitter are affected by angular errors. Pointing losses are evaluated through two approaches. The first approach is deterministic and only requires knowledge of a maximum angular error. The second approach requires knowledge of the angular error statistical distribution and tackles the problem from an outage probability viewpoint. These tools are then applied to analyze the impact of pointing losses in deep space optical links in which both terminals suffer from miss-pointing effects. The antenna gains are first optimized to maximize the effective system gain. The optimum antenna gains are then applied to evaluate maximum achievable ranges and to perform link design by means of optical link budgets.

## A New Discrete-Time Model for Channels Impaired by Phase Noise

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:9685737
- **Type**: conference
- **Published**: 7-11 Dec. 
- **Authors**: Amina Piemontese, Giulio Colavolpe, Thomas Eriksson
- **PDF**: https://ieeexplore.ieee.org/document/9685737
- **Abstract**: We propose a novel discrete-time model for the phase noise signal, in case of free-running and phase-locked oscillators. In particular, we show how the PN can be described by an autoregressive process. The strength of the proposed model is that it can be easily expressed in terms of measurement parameters of practical oscillators. We then analyse the most common discrete-time phase noise channel model with reference to the measurement parameters and to the system bandwidth. The derived analytical models for the discrete-time phase noise signal can be used for the design of estimation/detection algorithms, for performance evaluation, or simply for fast simulations.

## Comparison between the physical layer of the 4G and 5G standards

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:9702888
- **Type**: conference
- **Published**: 6-9 Dec. 2
- **Authors**: Raúl Haro-Báez, Byron P. Motoche, Cyntia I. Rosero +2
- **PDF**: https://ieeexplore.ieee.org/document/9702888
- **Abstract**: This paper analyzes and compares the most representative characteristics of the physical layer of Fourth Generation (4G) and the Fifth Generation (5G) cellular mobile technologies, highlighting the variable bandwidths, the use of millimeter waves, beamforming, massive Multiple Input and Multiple Output (MIMO) high-speed modulation schemes, and the low latency of 1ms. By comprehending these characteristics, it is possible to understand the benefits of high data transmission and real-time communication that the new 5G mobile generation will offer, improving how human beings have communicated wirelessly up to now.

## Dynamic Interval-based Watermarking for Tracking down Network Attacks

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:9724843
- **Type**: conference
- **Published**: 6-10 Dec. 
- **Authors**: Lian Yu, Lei Zhang, Yuanyuan Zhang +3
- **PDF**: https://ieeexplore.ieee.org/document/9724843
- **Abstract**: Transaction systems, such as e-commerce, banking systems, and blockchain-based transaction systems, take the advantages of great developments of network technologies. At the same time, such systems face a variety of threats and attacks. Passive traffic analysis (TA) usually consumes a lot of resources, and responds with tardiness, and no longer meets the current requirements. Network flow watermarking is a typical active TA technique, and IPD, IBW and ICBW are the typical ones, which can track attacks in a covert way. However, these approaches are also disturbed by the complex network conditions, e.g., packet splitting and merging during the transmissions. To improve the robustness of network flow watermarking, this paper proposes an improved scheme, dynamic interval-based watermark (DIBW). The experiments compare DIBW performance with that of IPD, IBW, and ICBW under packet splitting and merging conditions; and change the parameters of DIBW to observe the impacts on the performance of DIBW. The results show that DIBW can improve the robustness of the system. This paper utilizes LDPC code that consumes less time than the traditional ones. In addition, this paper proposes a hybrid watermark scheme of DIBW and IPD to adapt to the file sizes and the situations of network flow, and analyzes the feasibility of the adaptability by experiments.

## Normalized Neural Network for Belief Propagation LDPC Decoding

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:9702213
- **Type**: conference
- **Published**: 3-5 Dec. 2
- **Authors**: Yiduo Tang, Lin Zhou, Shuying Zhang +2
- **PDF**: https://ieeexplore.ieee.org/document/9702213
- **Abstract**: BP decoding algorithm is one of the commonly used decoding algorithms for LDPC codes. To adapt LDPC codes to different 5G scenarios and further improve the decoding performance of short LDPC codes, a scheme combining model-driven deep learning with a traditional BP decoding algorithm is proposed. With the advantages of model-driven, this solution expands the decoding iteration process between the check node and the variable node into a neural network and proposes a parameter normalization optimization solution to solve the problem of the program with many training parameters, the edge weights of the optimized Tanner graph are re-assigned and bound. Simulation results show that the proposed scheme can improve the decoding performance of LDPC codes with short lengths.

## Blind Recognition of Channel Coding Based on CNN-BLSTM

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:9702153
- **Type**: conference
- **Published**: 3-5 Dec. 2
- **Authors**: Shuying Zhang, Lin Zhou, Yiduo Tang +2
- **PDF**: https://ieeexplore.ieee.org/document/9702153
- **Abstract**: In cognitive radio or military communication systems, the channel coding type recognition of the primary user signal is an important task to realize full awareness of the wireless communication environment. Previous methods to solve this problem usually have high computational complexity, which are not suitable for real-time applications and require rich experience and professional knowledge in manual feature extraction. In this paper, a blind channel coding recognition algorithm based on CNN-BLSTM is proposed. Firstly, this method uses convolutional neural network to extract the data features of coding sequence and also avoids the problem of low recognition accuracy caused by inputting the original codeword data with inconspicuous features directly into neural network. Then, the context dependence of features is obtained through bidirectional long short-term memory network. Finally, the classification task is accomplished by softmax function. The experiments use spatially coupled LDPC codes and 5G NR LDPC codes as candidate codes. The experimental results show that the algorithm achieves quite high recognition accuracy under good channel conditions.

## Hybrid-ARQ Protocols using Iterative Threshold Decoding of OSMLD Product Codes

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:9641872
- **Type**: conference
- **Published**: 3-5 Dec. 2
- **Authors**: Fouad Ayoub, Mustapha Hilia, Faissal El Bouanani +2
- **PDF**: https://ieeexplore.ieee.org/document/9641872
- **Abstract**: In this paper, we investigate the impact of cyclic One-Step Majority-Logic Decodable (OSMLD) Product Codes, when decoded with the Iterative Threshold decoding algorithm, proposed by [2]. We propose to evaluate Hybrid Automatic Repeat Request (HARQ) Protocols using these attractive codes. The idea behind this study is to prove the attracting ARQ/FEC scheme offered by the proposed codes, and to show that we can reach a good trade-off between error rates, the average throughput and complexity. Numerical results shows that the proposed scheme may be interesting to compete many concatenated schemes applied to HARQ protocols.

## Network Coding-based Multi-Path Forward Erasure Correction for Tactical Scenarios

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:9653103
- **Type**: conference
- **Published**: 29 Nov.-2 
- **Authors**: Bertram Sch&#x00FC;tz, Stefanie Thieme, Christoph Fuchs +2
- **PDF**: https://ieeexplore.ieee.org/document/9653103
- **Abstract**: This paper formalizes and evaluates a promising technique to overcome packet loss in tactical scenarios, called Network Coding-based Multi-Path Forward Erasure Correction (CoMPEC). Thereby, encoded redundancy packets are sent over a secondary path to correct packet loss on the main path without the usage of feedback or retransmissions. Formal equations are presented to calculate the benefits in terms of packet loss rate after decoding and coding gain. To evaluate the potential for tactical scenarios, a simulation was conducted, which is based on the Anglova path loss data. The presented evaluation verifies CoMPEC's ability to significantly reduce the packet loss rate at the receiver, if the scheme is applicable.

## An Enhanced Check-Node Architecture for 5G New Radio LDPC Decoders

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:9665587
- **Type**: conference
- **Published**: 28 Nov.-1 
- **Authors**: Fakhreddine Ghaffari, Khoa Le
- **PDF**: https://ieeexplore.ieee.org/document/9665587
- **Abstract**: This paper presents an efficient hardware architecture of the Check Node (CN) units for the fifth generation (5G) new-radio Low-Density Parity-Check (LDPC) decoders. The proposed CN architecture is designed by splitting the high-degree CN operations into several phases and simplifying computing circuitry and connection wires. The critical path is shortened while the latency increment for one decoding iteration is negligible. Also, the proposed architecture allows to apply adaptively different offset factors when decoding different CN degree. This technique enhances the error rate and performance of our quantized LDPC decoder. The ASIC synthesis results confirm the advantages of the proposed architecture. This later helps reduce the decoder complexity by up to 30% while the operating frequency is enhanced by 10% compared to the conventional solution.

## A 5G-code based iterative Non-Binary LDPC decoder

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:9665548
- **Type**: conference
- **Published**: 28 Nov.-1 
- **Authors**: Dimitris Chytas, Vassilis Paliouras
- **PDF**: https://ieeexplore.ieee.org/document/9665548
- **Abstract**: This paper proposes an iterative Non-Binary LDPC (NB-LDPC) decoder for non-binary codes constructed using the 5G base matrices. Motivated by the binary to non-binary replacement method, we construct NB-LDPC matrices devised directly from the 5G base matrices. Subsequently, we develop an iterative decoding scheme able to facilitate parallelism due to its low complexity and to offer high performance due to its fast convergence. BER plots comparing Min-sum binary decoder (over 5G base matrices) to our proposed NB decoder reveal a performance gain of 0.5 dB in certain cases. Furthermore, hardware synthesis results obtained for a 45-nm ASIC technology are provided in order to quantify the throughput rate and area requirements of the proposed architecture. It is shown that the proposed decoding architecture, because of its independence on the lifting size factor, can offer higher throughput rate than the binary ones for small codeword lengths and code rates. In addition, as Galois Field (GF) order increases, the throughput rate increases too. Finally, the throughput-to-area show that the proposed NB architecture is generally suitable for small lifting size factors.

## The Decoding Method of LDPC based on Dynamic Maximum Iteration in Physical Downlink Shared Channel data

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:9742216
- **Type**: conference
- **Published**: 27-29 Dec.
- **Authors**: Liang Yan
- **PDF**: https://ieeexplore.ieee.org/document/9742216
- **Abstract**: In order to decode Physical Downlink Shared Channel data in 5G new radio, a method is proposed for Low Density Parity Check decoder in terminal equipment. It can hold the downlink throughput and lower down the power. According to the characteristics of low density parity check codes in 3GPP standard, this method simplifies the layering scalefactor min-sum method. The dynamic maximum iteration method is used to lower down the parallel processing and decrease the time delay. The simulation result shows that it is fast in decoding Physical Downlink Shared Channel data of lower SNR.

## Construction Methods and Performance Evaluation of Regular LDPC Convolutional Codes

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:9678497
- **Type**: conference
- **Published**: 27-28 Dec.
- **Authors**: Oulfa Laouar, Nadir Derouiche, Imed Amamra
- **PDF**: https://ieeexplore.ieee.org/document/9678497
- **Abstract**: In this paper, we present three construction methods of systematic regular LDPC-CCs based on randomly or algebraically structured sparse matrices. We provide an overview of LDPC-CCs and compares between Gallager’s, Mackay-Neal and Quasi-Cyclic (QC) construction methods, which are a good choice for many wireless applications due to their errors correction efficiency and low decoding complexity. At a rate-1/2, for the same size of the parity matrix to obtain the same encoding and decoding complexity, and using the Bit Flipping (BF) decoding algorithm over Additive White Gaussian Noise (AWGN) channel, we simulated the BER performance of a (3,6) regular LDPC convolutional codes, where the results showed that Gallager’s construction method (random) outperforms Mackay-Neal and QC ones.

## Performance analysis of multi-user mixed RF and hybrid RF/FSO cooperative systems with buffers based on GC-LDPC codes

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:9768382
- **Type**: conference
- **Published**: 20-22 Dec.
- **Authors**: Ibrahima Gueye, Idy Diop, Ibra Dioum
- **PDF**: https://ieeexplore.ieee.org/document/9768382
- **Abstract**: This article analyzes the impact of the use of error correcting codes, in particular globally coupled LDPC codes (GC-LDPC) in a double-hop relay system composed a multiuser mixed radio frequency (RF) and hybrid RF/FSO (free-space optical). For this configuration, communication between mobile users and a destination is via a buffer assisted decoding and retransmission relay node. Users transmit their data to the relay node over RF links using a virtual multiple input multiple output (MIMO) system. The relay node after decoding the data of all users using two-phase local-global decoding, this data will be transmitted to the destination via an FSO link supported by an RF MIMO backup system to the destination. A multi-antenna listener listens to information by decoding data received from users. The relay temporally stores user data in its buffer memory until the best channel conditions on the relay-destination link are met. For this communication setup, we first suggest using GC-LDPC codes for data encoding and decoding. The numerical results validate that buffering in the physical layer and the use of GC-LDPC codes significantly improve system performance. It is also found that the use of the relay buffer memory, the back-up RF link (in the second hop) and the use of GC-LDPC codes help protect user data against atmospheric turbulence.

## Optimized QC-LDPC Coded Cooperation for Single Relay Wireless Cooperative Communication System

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:9674081
- **Type**: conference
- **Published**: 17-19 Dec.
- **Authors**: Harit Rijal, Yang Fengfan, Gershon Rodor
- **PDF**: https://ieeexplore.ieee.org/document/9674081
- **Abstract**: This literature proposes an optimized design of a coded cooperative system using QC LDPC codes with joint decoding at the destination based on the bilayered Tanner graph. Firstly, the literature first introduces QC-LDPC and its construction method based on exponent matrix and base matrix. Then equivalent parity check matrix was constructed in the destination using the bi-layer Tanner graph for the coded cooperation. The literature implemented the iterative Belief Propagation (BP) algorithm-based decoding method to decode equivalent parity check matrix at the destination. Finally, BER performance analysis was performed. The performance analysis result illustrated that the optimized QC-LDPC coded cooperation has a better performance compared to the non-cooperative coded systems over similar channel conditions.

## Rate Matching and Interleaved Hardware Sharing Design

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:9674248
- **Type**: conference
- **Published**: 17-19 Dec.
- **Authors**: Kejia Huo, Zhuhua Hu, Dake Liu
- **PDF**: https://ieeexplore.ieee.org/document/9674248
- **Abstract**: Based on 3GPP standards, this paper investigates the interleaving and rate matching parts of turbo, convolutional, polar and LDPC codes used in 4G and 5G communication links. For the four different algorithms, this paper optimizes the address mapping formulas and proposes the interleaving storage sharing and module sharing methods, and the structure design of the shared modules. The feasibility of the algorithms is demonstrated through interleaving of codes and simulation verification, and a certain degree of hardware multiplexing of the 4G and 5G communication links is achieved.

## Design and Performance Evaluation of Channel Coding Schemes for Information Technologies

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:9678589
- **Type**: conference
- **Published**: 15-17 Dec.
- **Authors**: Juliy Boiko, Ilya Pyatin, Ruslan Chornyi +1
- **PDF**: https://ieeexplore.ieee.org/document/9678589
- **Abstract**: The article studies the efficiency of channel codes coding. The study covered issues related to determining the energy gain of coding. For this purpose, turbo codes, LDPC codes, polar codes were compared. The work contains the developed schemes of encoders and decoders of channel codes for those developed using a hardware description language (HDL). The results of comparing the resources used for the implementation of encoders and decoders and comparing their performance are obtained. Research indicates a high efficiency of turbo codes in coding schemes. The results of comparing the productivity of different channel codes can be used to design practical coding and decoding schemes in information channels.

## Design of Lossy Compression of the Gaussian Source with Protograph LDPC Codes

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:9660280
- **Type**: conference
- **Published**: 13-15 Dec.
- **Authors**: Huan Deng, Dan Song, Meiyuan Miao +1
- **PDF**: https://ieeexplore.ieee.org/document/9660280
- **Abstract**: The low-density parity-check (LDPC) code has been employed for the lossy compression of the binary symmetric source (BSS). However, the BSS application is limited in digital signal processing. In this paper, the BSS is extended to implement the lossy compression of the Gaussian source (LCGS) by using the protograph LDPC (P-LDPC) code. First, to improve the accuracy of the signal reconstruction, a multilevel coding (MLC) structure is designed with multiple P-LDPC codes for realizing the lossy compression. Then, a novel weighted rate allocation method is proposed to deploy an appropriate code rate at each coding level. Furthermore, the P-LDPC codes are optimized by a short cycle diminishing design to approach the theoretical distortion-rate limit. The simulation results demonstrate that the MLC structure based on the optimized P-LDPC codes outperforms the existing works.

## Full-Duplex Efficient Channel Codes for Residual Self-Interference/Quantization Noise Cancellation

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:9660220
- **Type**: conference
- **Published**: 13-15 Dec.
- **Authors**: Bao Quoc Vuong, Roland Gautier, Anthony Fiche +1
- **PDF**: https://ieeexplore.ieee.org/document/9660220
- **Abstract**: Full-Duplex (FD) systems are became very attractive technique for 5G and beyond transmissions by offering higher spectral efficiency. The implementation of a real FD system can be a challenging task due to the analog and residual Self-Interference (SI) and some imperfections introduced by analog components such as quantization error of Digital-to-Analog/Analog-to-Digital Converters (DAC/ADC). This paper investigates in the digital domain different channel coding schemes to compensate the residual SI and quantization noise cancellation process in case of Single Input Single Output (SISO) FD transmission. The promising channel coding schemes from the Third Generation Partnership Project (3GPP) such as 5G Quasi-Cyclic Low Density Check (QC-LDPC), 5G Polar Codes and LTE Turbo codes have been considered. Several numerical simulations are performed to evaluate the Bit Error Rate (BER) performance.

## FORTRESS: FORtified Tamper-Resistant Envelope with Embedded Security Sensor

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:9647783
- **Type**: conference
- **Published**: 13-15 Dec.
- **Authors**: Kathrin Garb, Johannes Obermaier, Elischa Ferres +1
- **PDF**: https://ieeexplore.ieee.org/document/9647783
- **Abstract**: Protecting security modules from attacks on the hardware level presents a very challenging endeavor since the attacker can manipulate the device directly through physical access. To address this issue, different physical security enclosures have been developed with the goal to cover entire hardware modules and, hence, protect them from external manipulation.Novel concepts are battery-less and based on Physical Unclonable Functions (PUFs), aiming at overcoming the most severe drawbacks of past devices; the need for active monitoring and, thus, limited battery life-time. Although some progress has already been made for certain aspects of PUF-based enclosures, the combination and integration of all required components and the creation of a corresponding architecture for Hardware Security Modules (HSMs) is still an open issue. In this paper, we present FORTRESS, a PUF-based HSM that integrates the tamper-sensitive capacitive PUF-based envelope and its embedded security sensor IC into a secure architecture. Our concept proposes a secure life cycle concept including shipment aspects, a full key generation scheme with re-enrollment capabilities, and ourthe next generation Embedded Key Management System. With FORTRESS, we take the next step towards the productive operation of PUF-based HSMs.

## A GenAlg Optimization of Length-Scalable QC-LDPC Codes

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:9674585
- **Type**: conference
- **Published**: 10-13 Dec.
- **Authors**: Yunxiao Liu, Ming Jiang, Yidi Zhang
- **PDF**: https://ieeexplore.ieee.org/document/9674585
- **Abstract**: In this paper, we propose an optimization scheme of quasi-cyclic low-density parity-check (QC-LDPC) codes based on an evolutionary algorithm, the Genetic Algorithm (GenAlg). By changing the positions and shift values of non-negative entries in the base matrix, the optimized codes can achieve better decoding performances. The optimized construction of the base matrix compatible for multiple lengths with different lifting sizes is discussed and a statistic metric used to measure the effectiveness of optimization is introduced to quantitatively evaluate the decoding performances with different code lengths. Simulation results of the proposed GenAlg optimized QC-LDPC codes with different lengths can significantly outperform those of the codes in various existing standards.

## LDPC Assisted Blind Frame Synchronization: Efficient Measurement Mechanism and Low-Complexity Algorithm

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:9674430
- **Type**: conference
- **Published**: 10-13 Dec.
- **Authors**: Zhongxiu Feng, Mengting Xu, Lixia Xiao +3
- **PDF**: https://ieeexplore.ieee.org/document/9674430
- **Abstract**: In this paper, low-density parity-check (LDPC) assisted blind frame synchronization (BFS) is studied to balance a tradeoff between the frame synchronization error rate performance and computational complexity. Specifically, we develop an efficient measurement mechanism related to the parity-check matrix to choose suitable LDPC codes for BFS. Furthermore, a low-complexity multi-stage search (MSS)-BFS algorithm is proposed, where the number of candidate positions gradually decreases as the growth of iteration number. Finally, simulation results show that the proposed measurement mechanism is reliable to choose LDPC codes for BFS, and the MSS-BFS algorithm can achieve comparable performance to conventional algorithm with eminently reduced iterations.

## McEliece Coding Method based on LDPC Code with Application to Physical Layer Security

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:9674295
- **Type**: conference
- **Published**: 10-13 Dec.
- **Authors**: Lintao Li, Yiran Xing, Xiaoxia Yao +1
- **PDF**: https://ieeexplore.ieee.org/document/9674295
- **Abstract**: The ubiquity of wireless communication systems has resulted in extensive concern regarding their security issues. Combination of signaling and secrecy coding can provide greater improvement of confidentiality than tradition methods. In this work, we mainly focus on the secrecy coding design for physical layer security in wireless communications. When the main channel and wiretap channel are noisy, we propose a McEliece secure coding method based on LDPC which can guarantee both reliability between intended users and information security with respect to eavesdropper simultaneously. Simulation results show that Bob’s BER will be significantly decreased with the SNR increased, while Eve get a BER of 0.5 no matter how the SNR changes.

## Research on the Application of Polar Codes in Underwater Acoustic Communication

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:9674601
- **Type**: conference
- **Published**: 10-13 Dec.
- **Authors**: Lijuan Xing, Zhuo Li, Zedong Zhang +1
- **PDF**: https://ieeexplore.ieee.org/document/9674601
- **Abstract**: Aiming at the analysis of the underwater acoustic channel such as complex and changeable, strong multi-path and large fluctuation interference, this article establishes an underwater acoustic communication system with polar codes as the channel coding scheme to improve the reliability of underwater acoustic data transmission. A Monte Carlo construction is proposed as a construction scheme of polar codes, and simulation results are obtained in three typical underwater acoustic channels. The results show that the construction scheme of polar codes proposed in this article is feasible and effective in these three channels. Compared with the Low Density Parity Check Code (LDPC) with similar code length, the comprehensive performance of the polar codes is better at the same Eb/N0. Relatively speaking, when the Eb/N0 is improved, the bit error ratio (BER) curve drops faster, which means that it can provide a higher coding gain. This article proves that the polar codes can obviously improve the performance of the underwater acoustic communication system, which will have a good application prospect in the complicated underwater acoustic channel.

## An Unequal Error Protection Scheme of H.265 Video Stream in Unmanned Aerial Vehicle System

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:9674644
- **Type**: conference
- **Published**: 10-13 Dec.
- **Authors**: Yue Zhang, Xiaoxia Yao, Jiaxuan Li +2
- **PDF**: https://ieeexplore.ieee.org/document/9674644
- **Abstract**: Under the technological development nowadays, bit error remains hard to be solved in Unmanned Aerial Vehicle (UAV) video transmission system. The common Equal Error Protection (EEP) scheme ignores the reality that the importance of different components of the video stream varies, leading to limitation of protection performance. This paper proposes an Unequal Error Protection (UEP) scheme of H.265 video stream based on Low Density Parity Check Code (LDPC). In this scheme, the video stream information is encoded and transmitted hierarchically according to its varying degrees of sensitivity to bit error. It can reduce the influence of the bit error, which is generated during transmission, on the video’s quality and improve the reliability of the UAV video transmission system without additional need of transmission bandwidth.

## Code-Aided Blind Iterative Channel Estimation for OFDM Systems

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:9674615
- **Type**: conference
- **Published**: 10-13 Dec.
- **Authors**: Jiaxuan Li, Xuhui Ding, Yue Zhang +4
- **PDF**: https://ieeexplore.ieee.org/document/9674615
- **Abstract**: In this paper, we propose a novel blind iterative channel estimation algorithm for the Orthogonal frequency division multiplexing (OFDM) communication system, where pilot symbols for estimating multipath channel are no longer needed. Since channel coding can introduce sufficient coding gain to enhance the robustness of communication systems, we iteratively feed the hard-decision bit information output by Low-density parity-check (LDPC) decoder back to the channel estimator to improve parameter estimation accuracy. Furthermore, we apply a denoising algorithm based on the discrete Fourier transform (DFT) method to deal with the estimation result of the least square (LS) algorithm, which further optimizes the performance of the estimator. Simulation results verify that the bit error rate (BER) performance of our proposed blind iterative channel estimation method is about 8 dB better than that of the conventional pilot-assisted LS estimation method when BER is 10-6.

## Packet Scheduling for Wireless Powered Communication Systems in the Finite Blocklength Regime: A POMDP Approach

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:9674485
- **Type**: conference
- **Published**: 10-13 Dec.
- **Authors**: Chenhui Wang, Xin Liu, Siyuan Zheng +3
- **PDF**: https://ieeexplore.ieee.org/document/9674485
- **Abstract**: This paper proposes a packet scheduling scheme in a wireless powered internet-of-things (WP-IoT) system with the consideration of some recent results on finite blocklength (FBL). The system includes one source node (SN) and one hybrid access point (HAP). The SN is assumed to have no embedded energy supply and thus need to firstly perform energy harvesting (EH) from radio signals of HAP. Before performing EH and data transmitting, we assume that the SN needs to first estimate the channel quality. With the assumption of imperfect channel estimation process, the packet scheduling problem in the proposed system is formulated as a partially observable Markov decision (POMDP) problem. To maximize the system long-term throughput, the optimal policy for packet scheduling is derived by a dynamic programming approach. Simulation results demonstrates that the proposed packet scheduling scheme outperforms the corresponding myopic scheme.

## A High Precision Refresh Method to Improve The Performance of Flash Storage Devices

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:9680340
- **Type**: conference
- **Published**: 10-12 Dec.
- **Authors**: Peixuan Li, Yaofang Zhang, Deli Yin +1
- **PDF**: https://ieeexplore.ieee.org/document/9680340
- **Abstract**: With the development of flash memory, its storage density has gradually increased, but its reliability has been greatly reduced. Now, flash memory relies on LDPC to solve this problem. Although LDPC (Low Density Parity Check Code) can correct data with a high error rate, it will cause a lot of delays. The refresh operation can cause the LDPC decoding delay. In the work of this article, we propose a precise refresh strategy. On the basis of high latency pages, according to the characteristics of data access frequency, we take the read-hot data in the write-cold data as our refresh target. We test the performance of the precise refresh scheme through different workloads. Compared with ordinary refresh schemes, the average response time of flash memory storage devices is reduced by 16%-49% and the lifetime of flash memory is extended.

## Performance Analysis of Sub-Optimal LDPC Decoder for 5G using Belief Propagation Algorithm

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:9689078
- **Type**: conference
- **Published**: 1-2 Dec. 2
- **Authors**: Avinash Subramaniam M, Jay Sejpal, Pasupuleti Rithvij +2
- **PDF**: https://ieeexplore.ieee.org/document/9689078
- **Abstract**: Today's modern wireless communication systems demand extensive quality and computational power with an increase in day-to-day data-rate standards. The latest com-munication standards focus on low latency, high throughput, and reliable error correction capabilities which inspired us to explore the 5G New Generation (NR) technology. Low-Density Parity-Check Codes (LDPC) are known to have error correction capabilities that can achieve Shannon's maximum channel ca-pacity. Encoding of LDPC Codes features a sparse property that enables effortless decoding at the receiver end. Advancements in deep learning have helped in estimating the channel noise more accurately. The Iterative Belief Propagation-Convolutional Neural Network (BP-CNN) architecture involves a CNN block which is trained with a quadratic loss function concatenated to a standard BP Decoder. The proposed Iterative BP-CNN architecture with a Batch Normalization layer results in a better performance compared to the Iterative BP-CNN architecture as it standardizes the input to the CNN block and also solves the problem of vanishing gradients during backpropagation.
