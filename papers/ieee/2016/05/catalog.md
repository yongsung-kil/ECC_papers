# IEEE Xplore — 2016-05


## Hard-Information Bit-Reliability Based Decoding Algorithm for Majority-Logic Decodable Nonbinary LDPC Codes

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:7425163
- **Type**: journal
- **Published**: May 2016
- **Authors**: Xiangcheng Li, Tuanfa Qin, Haiqiang Chen +3
- **PDF**: https://ieeexplore.ieee.org/document/7425163
- **Abstract**: A modified bit-reliability based decoding algorithm is presented based on a recent work by Huang et al. For the presented algorithm, only one Galois field element is passed and exchanged along the edges of the Tanner graph. At variable nodes, full messages rather than extrinsic messages are processed to further reduce the computational complexity. At check nodes, only hard reliability is considered and the main operation is to compute the check-sum and send one extrinsic symbol back to variable nodes. Simulation results show that, even with lower complexity and less memory consumption, the presented algorithm still can perform very closely to the original wBRB algorithm with low quantization bits (3 ~ 4 bits) when decoding the majority-logic decodable nonbinary LDPC codes. For codes constructed in high order fields, the presented algorithm can even outperform the original wBRB algorithm.

## Low-Complexity First-Two-Minimum-Values Generator for Bit-Serial LDPC Decoding

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:7346442
- **Type**: journal
- **Published**: May 2016
- **Authors**: Jea Hack Lee, Myung Hoon Sunwoo
- **PDF**: https://ieeexplore.ieee.org/document/7346442
- **Abstract**: This brief proposes a low-complexity first-two-minimum-values generator for a bit-serial scheme. Since the hardware complexity of generators utilizes a significant portion of the min-sum low-density parity-check decoder, a low-complexity generator is crucially important. To reduce hardware complexity, an existing bit-serial generator that finds only one minimum value instead of two has been proposed; however, it can cause bit error rate (BER) degradation. By contrast, the proposed low-complexity bit-serial generator can find the exact first two minimum values and thus can improve the BER performance. Moreover, the proposed generator does not suffer from any throughput loss since its latency is almost the same as that of the existing generator.

## High-Performance NB-LDPC Decoder With Reduction of Message Exchange

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:7328322
- **Type**: journal
- **Published**: May 2016
- **Authors**: Jesús O. Lacruz, Francisco García-Herrero, María José Canet +1
- **PDF**: https://ieeexplore.ieee.org/document/7328322
- **Abstract**: This paper presents a novel algorithm based on trellis min-max for decoding non-binary low-density parity-check (NB-LDPC) codes. This decoder reduces the number of messages exchanged between check node and variable node processors, which decreases the storage resources and the wiring congestion and, thus, increases the throughput of the decoder. Our frame error rate performance simulations show that the proposed algorithm has a negligible performance loss for high-rate codes with GF(16) and GF(32) and a performance loss smaller than 0.07 dB for high-rate codes over GF(64). In addition, a layered decoder architecture is presented and implemented on a 90-nm CMOS process for the following high-rate NB-LDPC codes: (2304, 2048) over GF(16), (837, 726) over GF(32), and (1536, 1344) over GF(64). In all cases, the achieved throughput is higher than 1 Gb/s.

## Iterative Decoding of LDPC Codes Over the  $q$ -Ary Partial Erasure Channel

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:7439825
- **Type**: journal
- **Published**: May 2016
- **Authors**: Rami Cohen, Yuval Cassuto
- **PDF**: https://ieeexplore.ieee.org/document/7439825
- **Abstract**: In this paper, we develop a new channel model, which we name the  $q$ -ary partial erasure channel (QPEC). The QPEC has a  $q$ -ary input, and its output is either the input symbol or a set of  $M$  ( $2 \le M \le q$ ) symbols, containing the input symbol. This channel serves as a generalization to the binary erasure channel and mimics situations when a symbol output from the channel is known only partially; that is, the output symbol contains some ambiguity, but is not fully erased. This type of channel is motivated by non-volatile memory multi-level read channels. In such channels, the readout is obtained by a sequence of current/voltage measurements, which may terminate with a partial knowledge of the stored level. Our investigation is concentrated on the performance of low-density parity-check (LDPC) codes when used over this channel, thanks to their low decoding complexity using belief propagation. We provide the exact QPEC density-evolution equations that govern the decoding process, and suggest a cardinality-based approximation as a proxy. We then provide several bounds and approximations on the proxy density evolutions, and verify their tightness through numerical experiments. Finally, we provide tools for the practical design of LDPC codes for use over the QPEC.

## Bounds on the Belief Propagation Threshold of Non-Binary LDPC Codes

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:7429784
- **Type**: journal
- **Published**: May 2016
- **Authors**: Leonid Geller, David Burshtein
- **PDF**: https://ieeexplore.ieee.org/document/7429784
- **Abstract**: We consider low-density parity-check (LDPC) code ensembles over non-binary Galois fields when used for transmission over arbitrary discrete memoryless channels. Belief propagation decoding for these codes has been shown to achieve excellent results. However, computing the decoding threshold using density evolution is usually impractical, since one needs to propagate multi-dimensional probability distributions, and Monte Carlo simulations are required instead. By considering the evolution of the message Bhattacharyya parameter and the message expected value parameter, we derive a simple lower bound on the performance of the algorithm. This bound applies for both regular and irregular non-binary LDPC ensembles.

## Threshold Saturation for Nonbinary SC-LDPC Codes on the Binary Erasure Channel

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:7430313
- **Type**: journal
- **Published**: May 2016
- **Authors**: Iryna Andriyanova, Alexandre Graell i Amat
- **PDF**: https://ieeexplore.ieee.org/document/7430313
- **Abstract**: We analyze the asymptotic performance of nonbinary spatially coupled low-density parity-check (SC-LDPC) code ensembles defined over the general linear group on the binary erasure channel. In particular, we prove the threshold saturation of belief propagation decoding to the so-called potential threshold, using the proof technique based on potential functions introduced by Yedla et al., assuming that the potential function exists. We rewrite the density evolution of nonbinary SC-LDPC codes in an equivalent vector recursion form which is suited for the use of the potential function. We then discuss the existence of the potential function for the general case of vector recursions defined by multivariate polynomials, and give a method to construct it. We define a potential function in a slightly more general form than the one by Yedla et al., in order to make the technique based on potential functions applicable to the case of nonbinary LDPC codes. We show that the potential function exists if a solution to a carefully designed system of linear equations exists. Furthermore, we numerically show the existence of a solution to the system of linear equations for a large number of nonbinary LDPC code ensembles, which allows us to define their potential function and thus prove threshold saturation.

## SC-LDPC Code With Nonuniform Degree Distribution Optimized by Using Genetic Algorithm

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:7439792
- **Type**: journal
- **Published**: May 2016
- **Authors**: Yohei Koganei, Masanori Yofune, Cong Li +2
- **PDF**: https://ieeexplore.ieee.org/document/7439792
- **Abstract**: We propose a class of spatially-coupled low-density parity-check (SC-LDPC) codes consisting of a finite-length chain of component LDPC matrices which are assigned with different degree distributions, i.e., the strength of spatial coupling is nonuniform within an SC-LDPC code. For this class of codes, we use a modified density evolution algorithm to calculate the belief-propagation (BP) threshold on the binary erasure channel (BEC). We then optimize the degree distributions by a genetic algorithm where the BP-threshold is considered as the fitness value. The resultant codes were confirmed to exhibit improved decoding performance compared with SC-LDPC codes having uniform degree distributions.

## A Soft Decode–Compress–Forward Relaying Scheme for Cooperative Wireless Networks

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:7118747
- **Type**: journal
- **Published**: May 2016
- **Authors**: Dushantha N. K. Jayakody, Mark F. Flanagan
- **PDF**: https://ieeexplore.ieee.org/document/7118747
- **Abstract**: This paper proposes a new technique for soft information relaying, which is based on a soft decode–compress–forward relay protocol. The proposed system provides a means of using distributed low-density parity-check (LDPC) coding in conjunction with higher order modulation, such as pulse amplitude modulation (PAM) and quadrature amplitude modulation (QAM), which is effective even under poor source–relay link conditions. Ordinarily, such schemes suffer from error propagation to the destination caused by incorrect decoding at the relay when the signal-to-noise ratio (SNR) on the source–relay link is low; however, our system avoids this problem by generating soft versions of the additional (parity-bearing) PAM symbols for transmission from the relay. The proposed technique of soft compression does not suffer from parity log-likelihood ratios (LLRs) converging to zero, as do many soft re-encoding techniques for turbo and LDPC codes. In the case of Gray-coded PAM/QAM signaling, we also propose a method of performing exact expectation-based soft modulation with low computational complexity. Furthermore, we propose a new model, which we refer to as the soft scalar model, for the overall source-to-destination channel encountered by the constellation symbols, and this model is used at the destination to compute LLRs for joint decoding of the distributed LDPC code. Simulation results demonstrate that the proposed scheme can provide good coding gain, diversity gain, and spectral efficiency under poor source–relay SNR conditions.

## A Soft-Network-Coded Multilevel Forwarding Scheme for Multiple-Access Relay Systems

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:7120177
- **Type**: journal
- **Published**: May 2016
- **Authors**: Dushantha N. K. Jayakody, Jun Li, Mark F. Flanagan
- **PDF**: https://ieeexplore.ieee.org/document/7120177
- **Abstract**: This paper proposes the novel technique of multilevel-threshold-based soft quantization (MLT-SQ) for a multiple-access relay system (MARS). The scheme is suitable for systems using binary phase-shift keying (BPSK) and network coding at the relay. In the proposed MLT-SQ protocol, the relay evaluates the reliabilities, which are expressed as log-likelihood ratios (LLRs), of the received signals from the two sources. It then computes the LLRs of the network-coded packet and quantizes these using a set of optimized multilevel thresholds, forwarding the resulting “quantized soft symbols” to the destination. We provide the derivation for the bit error rate (BER) at the destination, and based on this, we optimize the multilevel thresholds to minimize the BER. Simulation results are provided for the proposed MLT-SQ system, both without coding and for the case where low-density parity-check (LDPC) coding is employed. The proposed system achieves full diversity order. Compared with competing schemes, the performance of our system is superior in terms of BER when the same amount of channel state information (CSI) is exploited.

## High Capacity Reversible Data Hiding in Encrypted Images by Patch-Level Sparse Representation

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:7098386
- **Type**: journal
- **Published**: May 2016
- **Authors**: Xiaochun Cao, Ling Du, Xingxing Wei +2
- **PDF**: https://ieeexplore.ieee.org/document/7098386
- **Abstract**: Reversible data hiding in encrypted images has attracted considerable attention from the communities of privacy security and protection. The success of the previous methods in this area has shown that a superior performance can be achieved by exploiting the redundancy within the image. Specifically, because the pixels in the local structures (like patches or regions) have a strong similarity, they can be heavily compressed, thus resulting in a large hiding room. In this paper, to better explore the correlation between neighbor pixels, we propose to consider the patch-level sparse representation when hiding the secret data. The widely used sparse coding technique has demonstrated that a patch can be linearly represented by some atoms in an over-complete dictionary. As the sparse coding is an approximation solution, the leading residual errors are encoded and self-embedded within the cover image. Furthermore, the learned dictionary is also embedded into the encrypted image. Thanks to the powerful representation of sparse coding, a large vacated room can be achieved, and thus the data hider can embed more secret messages in the encrypted image. Extensive experiments demonstrate that the proposed method significantly outperforms the state-of-the-art methods in terms of the embedding rate and the image quality.

## Secure Multiplex Coding With Dependent and Non-Uniform Multiple Messages

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:7407383
- **Type**: journal
- **Published**: May 2016
- **Authors**: Masahito Hayashi, Ryutaroh Matsumoto
- **PDF**: https://ieeexplore.ieee.org/document/7407383
- **Abstract**: The secure multiplex coding (SMC) is a technique to remove rate loss in the coding for wire-tap channels and broadcast channels with confidential messages caused by the inclusion of random bits into transmitted signals. SMC replaces the random bits by other meaningful secret messages, and a collection of secret messages serves as the random bits to hide the rest of messages. In the previous studies, multiple secret messages were assumed to have independent and uniform distributions, which is difficult to be ensured in practice. We remove this restrictive assumption by a generalization of the channel resolvability technique. We also give practical construction techniques for SMC by using an arbitrary given error-correcting code as an ingredient, and channel-universal coding of SMC. By using the same principle as the channel-universal SMC, we give coding for the broadcast channel with confidential messages universal to both channel and source distributions.

## Polar Coding for the Broadcast Channel With Confidential Messages: A Random Binning Analogy

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:7426806
- **Type**: journal
- **Published**: May 2016
- **Authors**: Rémi A. Chou, Matthieu R. Bloch
- **PDF**: https://ieeexplore.ieee.org/document/7426806
- **Abstract**: We develop a low-complexity polar coding scheme for the discrete memoryless broadcast channel with confidential messages under strong secrecy and randomness constraints. Our scheme extends previous work by using an optimal rate of uniform randomness in the stochastic encoder, and avoiding assumptions regarding the symmetry or degraded nature of the channels. The price paid for these extensions is that the encoder and the decoders are required to share a secret seed of negligible size and to increase the block length through chaining. We also highlight a close conceptual connection between the proposed polar coding scheme and a random binning proof of the secrecy capacity region.

## Hamming coding for multi-relay cooperative quantize and forward networks

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:7519426
- **Type**: conference
- **Published**: 9-11 May 2
- **Authors**: Nasaruddin, Rony Kurnia
- **PDF**: https://ieeexplore.ieee.org/document/7519426
- **Abstract**: A cooperative communication system is an effective way to deal with the multipath fading in a wireless channel. However, the data sent from a source to the relay or the destination may experience some losses or corruptions during the transmission, causing error bits. Those errors can degrade the system's performance. In order to detect and correct the errors, it is important to apply a channel coding to the cooperative networks. In this paper, the Hamming Coding for multi-relay cooperative quantize and forward (QF) networks is proposed. The Hamming Codes are the simplest linear codes that can be implemented with low complexity in the proposed networks. The proposed system model is presented with the analytic expressions of the networks. Moreover, the system performance is simulated using the computer simulation in terms of bit error rate (BER). It is shown in the simulation results that the Hamming Code could significantly improve the network's performance when the number of relays is increased. The network's performance is also increased by using high quantization levels in the QF relays. Furthermore, it is found that the performance of the multi-relay QF networks with Hamming Code is better than those of the multi-relay amplify and forward (AF) networks with and without the Hamming Coding. It is concluded that the performance of multi-relay QF network is improved by the use of Hamming Code as well as the advantage of quantization levels.

## Research on LDPC code decoding algorithm based on scheduling strategy

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:7531650
- **Type**: conference
- **Published**: 28-30 May 
- **Authors**: Feng Xiao
- **PDF**: https://ieeexplore.ieee.org/document/7531650
- **Abstract**: With the rapid development of the channel coding technology, low density parity check(LDPC) code has been widely concerned by researchers all of the world as an approaching code to Shannon limit. Error floor is an important issue in the theory of LDPC codes and the research of iterative decoding algorithms. Based on the decoding of LDPC codes, a new improved decoding algorithm, Group Belief Propagation (GBP) based on variable nodes is proposed for the different scheduling strategies of the LDPC codes. According to the difference between the messages and the hard decision values, the variable nodes are divided into reliable nodes and unreliable nodes. And the unreliable nodes are priority to update. Further, the effect of threshold for judging the group on GBP strategy is analyzed. Simulation results show that the proposed algorithm can achieve better convergence and decoding performances compared to three classical scheduling algorithms. Meanwhile, it can overcome the error floor phenomenon caused by the trapping set effectively.

## Review on enhanced data rate receiver design using efficient modulation techniques for underwater acoustic communication

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:7831653
- **Type**: conference
- **Published**: 25-27 May 
- **Authors**: M. G. Ravi Kumar, Mrinal Sarvagya
- **PDF**: https://ieeexplore.ieee.org/document/7831653
- **Abstract**: Underwater acoustic (UWA) transmission schemes are an interesting area of communication research, in which achieving high data rate, low latency and high throughput is challenging task. In this paper, we trying to provide a survey on various efficient techniques which that includes channel estimation, channel equalization and efficient modulation schemes to achieve high data rate in the receiver using OFDM scheme for underwater acoustic communication. We are focusing for designing a block-by-block iterative receiver for underwater MIMO-OFDM that includes channel estimation with highly efficient modulation techniques for underwater acoustic communication. Also we found some efficient modulation techniques like BPSK, DPSK and 16-QAM for underwater channel communication which are best in achieving high data rate by considering more subcarriers.

## Transmission of correlated sources over non-orthogonal Gaussian MACs

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:7503842
- **Type**: conference
- **Published**: 23-27 May 
- **Authors**: Jiguang He, Iqbal Hussain, Markku Juntti +1
- **PDF**: https://ieeexplore.ieee.org/document/7503842
- **Abstract**: We investigate the transmission of multiple correlated binary sources to a single destination over non-orthogonal Gaussian multiple access channels (MACs). By considering a binary codebook, we derive the admissible rate regions of the two-source Gaussian MAC. It is demonstrated that the admissible rate region increases as the correlation between the sources increases. Furthermore, we develop an iterative joint source channel decoding scheme based on systematic irregular low-density parity-check codes by exploiting the correlation between the two sources. The constituent decoders corresponding to each source are implemented in parallel via local iterations, exchanging extrinsic information with each other during the global iterations. Simulation results are provided to verify the performance improvement of the transmission of correlated sources compared to its independent sources counterpart.

## Reducing repair-bandwidth using codes based on factor graphs

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:7510728
- **Type**: conference
- **Published**: 22-27 May 
- **Authors**: Dongwon Lee, Hyegyeong Park, Jaekyun Moon
- **PDF**: https://ieeexplore.ieee.org/document/7510728
- **Abstract**: Distributed storage systems suffer from significant repair traffic generated due to frequent storage node failures. This paper shows that properly designed low-density parity-check (LDPC) codes can substantially reduce the amount of required block downloads for repair thanks to the sparse nature of their factor graph representation. In particular, with a careful construction of the factor graph, both low repair-bandwidth and high reliability can be achieved for a given code rate. First, a formula for the average repair bandwidth of LDPC codes is developed. This formula is then used to establish that the minimum repair bandwidth can be achieved by forcing a regular check node degree in the factor graph. It is also shown that for a given repair-bandwidth overhead, LDPC codes can have substantially higher reliability than currently utilized Reed-Solomon (RS) codes. Our reliability analysis is based on a formulation of the general equation for the mean-time-to-data-loss (MTTDL) associated with LDPC codes. The formulation reveals that the stopping number is highly related to MTTDL. For code rates 1/2, 2/3, and 3/4, our results show that quasi-cyclic (QC) progressive-edge-growth (PEG) LDPC codes with variable node degree 2 allow 25% ~ 50% reduction in the repair bandwidth while maintaining higher MTTDL compared to currently employed RS codes.

## Fully parallel window decoder architecture for spatially-coupled LDPC codes

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:7511553
- **Type**: conference
- **Published**: 22-27 May 
- **Authors**: Najeeb Ul Hassan, Martin Schlüter, Gerhard P. Fettweis
- **PDF**: https://ieeexplore.ieee.org/document/7511553
- **Abstract**: Spatially-coupled low-density parity-check (SC-LDPC) codes have been shown to be superior in performance than LDPC block codes. In order to comply with the practical constraints on latency, SC-LDPC codes are decoded using a window decoder that reduces the decoder latency and complexity compared to traditional block-wise decoding. However, so far the literature only considers the structural decoding latency of window decoder, ignoring the processing latency. Note that the processing latency directly impacts the decoder's throughput and is an important parameter in any modern communication system. The throughput of an iterative decoder is directly influenced by the number of iterations and hence in this paper we propose a fully parallel window decoder architecture for SC-LDPC codes where the decoding iterations are performed in parallel. This guarantees a high throughout while fulfilling the low latency requirements. The overall decoding latency (structural and processing latency) of the proposed window decoder architecture is compared with the classical window decoder.

## An efficient exhaustive search algorithm for elementary trapping sets of variable-regular LDPC codes

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:7511551
- **Type**: conference
- **Published**: 22-27 May 
- **Authors**: Yoones Hashemi, Amir H. Banihashemi
- **PDF**: https://ieeexplore.ieee.org/document/7511551
- **Abstract**: In this paper, we propose an efficient exhaustive search algorithm for elementary trapping sets (ETS) of variable-regular low-density parity-check (LDPC) codes. Recently, Karimi and Banihashemi proposed a characterization of ETSs, which was based on viewing an ETS as a layered superset (LSS) of a short cycle in the code's Tanner graph. A notable advantage of LSS characterization is that it corresponds to a simple LSS-based search algorithm (expansion technique) that starts from short cycles of the graph and finds the ETSs with LSS structure efficiently. Compared to the LSS-based search, which is based on a single LSS expansion technique, the new search algorithm involves two additional expansion techniques. The introduction of the new techniques results in significant improvements in search efficiency compared to the LSS-based search. We prove that using the three expansion techniques, each and every ETS structure can be obtained starting from a simple cycle. We also provide extensive simulation results that show, compared to the LSS-based search, up to three orders of magnitude improvement in search speed and memory requirements can be achieved.

## Efficient transmission schemes for correcting insertions/deletions in DPPM

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:7511112
- **Type**: conference
- **Published**: 22-27 May 
- **Authors**: Weigang Chen, Yuan Liu
- **PDF**: https://ieeexplore.ieee.org/document/7511112
- **Abstract**: Differential pulse-position modulation (DPPM) shows significant power and bandwidth efficiency in wireless optical communications and does not need symbol synchronization, but suffers from serious insertion/deletion errors if the low-complexity symbol-by-symbol detection is used. In this paper, the DPPM transmission scheme combining the watermark with the low-density parity-check (LDPC) code is proposed. Specifically, the equivalent source and channel models are developed to disclose the insertion/deletion characteristics. Then, trellis graphs are built based on the watermark and the equivalent source and channel models. On the trellis, Viterbi algorithm can be executed to convert the insertions/deletions to small number of substitutions, which can be finally recovered using LDPC codes. Simulation results reveal that the scheme performs well with the insertions and deletions introduced by low complexity symbol-by-symbol detection. The proposed method lays the feasibility of the practical applications of DPPM considering the complexity and significant performance.

## Serial quasi-primitive BC-BCH codes for NAND flash memories

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:7510725
- **Type**: conference
- **Published**: 22-27 May 
- **Authors**: Daesung Kim, Jeongseok Ha
- **PDF**: https://ieeexplore.ieee.org/document/7510725
- **Abstract**: In this work, we study high-rate error-control systems with serial quasi-primitive block-wise concatenated Bose-Chaudhuri-Hocquenghem (BC-BCH) codes for storage devices using multi-level per cell (MLC) NAND flash memories. The system targets at achieving a strong error-correcting capability when only hard-decision channel outputs are available. Error-rate performance of the proposed system is compared with those of systems based on various coding schemes including LDPC codes.

## Physical-layer network-coding over block fading channels with root-LDA lattice codes

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:7511113
- **Type**: conference
- **Published**: 22-27 May 
- **Authors**: Ping-Chung Wang, Yu-Chih Huang, Krishna R. Narayanan +1
- **PDF**: https://ieeexplore.ieee.org/document/7511113
- **Abstract**: We consider the problem of physical-layer network coding when the channel exhibits block fading. Specifically, we focus on the use of lattice codes in a compute-and-forward framework for realizing physical-layer network coding. We construct a novel lattice ensemble called the root-Low-Density Construction-A (root-LDA) ensemble which uses Construction A with root-low-density parity check (LDPC) codes. Using extensive simulations, we show that the proposed lattice codes exhibit full diversity when used over the block fading channels. In addition, their performance is comparable to the performance of LDA lattice codes optimized by the progressive edge growth algorithm over the additive white Gaussian noise AWGN channel. This suggests that root-LDA lattice codes provide a robust solution to the problem of implementing physical layer network coding over fading channels.

## Practical LDPC encoders robust to hardware errors

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:7511552
- **Type**: conference
- **Published**: 22-27 May 
- **Authors**: Elsa Dupraz, Valentin Savin, Satish Kumar Grandhi +2
- **PDF**: https://ieeexplore.ieee.org/document/7511552
- **Abstract**: LDPC decoders on faulty hardware have received increasing attention over the last few years, mainly motivated by reliability issues in emerging nanotechnologies. As a main result, it was shown that LDPC decoders are naturally robust to hardware faults. LDPC encoders on faulty hardware have received less attention, and they are expected to be less robust to hardware faults. In this work, we propose an LDPC encoding solution that is robust to faulty hardware. Our encoding solution is composed of two steps. First, an Augmented Encoding method is proposed, which consists in computing an augmented codeword that contains both the codeword to be transmitted on the channel and extra parity bits. The augmented codeword is computed from a noisy encoding circuit, and then corrected by a noisy Gallager-B decoder before channel transmission. The augmented codeword is obtained from a rate-compatible construction that guarantees good decoding performance both for the augmented codeword and for the codeword to be transmitted on the channel. In order to further improve the robustness of our encoding solution, we propose a second step, consisting of a circuit-level optimization. We propose to identify the critical gates that are responsible for encoding failures, and to duplicate them in order to reduce their influence on encoding outputs. Based on Monte-Carlo simulation, we show that the proposed solution significantly improves the encoding robustness to hardware faults.

## Polar codes for noncoherent MIMO signalling

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:7511290
- **Type**: conference
- **Published**: 22-27 May 
- **Authors**: Philip R. Balogun, Ian D. Marsland, Ramy H. Gohary +1
- **PDF**: https://ieeexplore.ieee.org/document/7511290
- **Abstract**: Polar codes, ever since their introduction, have been shown to be very effective for various wireless communication channels. This together with their relatively low implementation complexity has made polar codes an attractive coding scheme for wireless communications. On the other hand, within the realm of non-coherent wireless MIMO communication, Grassmannian signalling has been shown to approach the ergodic capacity of frequency-flat block fading channels. In this paper, a novel methodology for designing polar codes that works effectively with Grassmannian signalling and a novel set partitioning algorithm for Grassmannian constellations are proposed. We compare the error rate performance of our design with that of existing schemes and show that a gain of over 1 dB over the previously known best technique, which is based on turbo codes, is possible, at much lower decoding complexity.

## Towards an analytical model of NAND flash memory and the impact on channel decoding

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:7510726
- **Type**: conference
- **Published**: 22-27 May 
- **Authors**: Hachem Yassine, Justin Coon, Mohamed Ismail +1
- **PDF**: https://ieeexplore.ieee.org/document/7510726
- **Abstract**: The underlying models of sources of noise in flash memory are exploited to compute an accurate distribution of the threshold voltage of a cell after cancelling cell to cell interference (CCI). We analytically express the mean and variance of this voltage solely as a function of number of P/E cycles, retention time and data eliminating the read overhead of the adaptive estimation methods. To reduce the computational difficulty in hardware, we approximate the accurate distribution by a moment matched Gaussian mixture and we validate this approximation by comparing the soft decision decoding performance of both models. To gain more error correction advantage, we model the residual CCI as an additional Gaussian noise term.

## Jointly optimized quadrature amplitude modulation

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:7511271
- **Type**: conference
- **Published**: 22-27 May 
- **Authors**: Sung-Joon Park
- **PDF**: https://ieeexplore.ieee.org/document/7511271
- **Abstract**: Quadrature amplitude modulation has been widely used for high-speed data transmission in modern digital communication systems. In this work, a generalized quadrature amplitude modulation which relaxes the constraint of square lattice is suggested to improve the joint performance of modulation and coding. Bitwise log-likelihood ratios and input signal-to-noise ratios for decoder are analyzed and the strategy minimizing the probability of decoding error is investigated. The analytical argument is consolidated by conducting simulations with a turbo code. According to results, the proposed scheme presents a power gain which depends on Es/N0 and a modulation order.

## Four-dimensional constellations for dual-polarized satellite communications

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:7511493
- **Type**: conference
- **Published**: 22-27 May 
- **Authors**: Nicolò Mazzali, Farbod Kayhan, R Bhavani Shankar Mysore
- **PDF**: https://ieeexplore.ieee.org/document/7511493
- **Abstract**: In this paper, we investigate the performance of constellations optimized for transmissions in dual-polar mobile satellite applications. These four-dimensional constellations (inphase and quadrature per polarization) are designed for joint transmission over the two polarizations. Such constellations enhance the reliability of the system by providing certain redundancy into their design. Their performance is compared with transmission of independent 2D constellations over each polarization. As performance metrics, the pragmatic achievable mutual information and the bit error rate have been considered. The gains serve to indicate the need to further investigate 4D constellation design and its application in dual-polar MIMO systems.

## Enhanced spatial multiplexing — A novel approach to MIMO signal design

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:7511274
- **Type**: conference
- **Published**: 22-27 May 
- **Authors**: Chien-Chun Cheng, Hikmet Sari, Serdar Sezginer +1
- **PDF**: https://ieeexplore.ieee.org/document/7511274
- **Abstract**: In this paper, we present a new type of Spatial Multiplexing (SMX) schemes based on the multiple signal constellation concept, which was recently introduced in the context of Spatial Modulation (SM) by the present authors. The proposed technique, which we refer to as Enhanced SMX or E-SMX, conveys information not only by the transmitted symbols, but also by the antenna and constellation combinations used. In addition to the primary constellation, these schemes make use of one or more specifically-designed secondary constellations, obtained through geometric interpolation in the signal constellation plane. We present the general concept and describe specific schemes for different numbers of transmit antennas and using 16QAM as primary modulation. Our analysis and the simulation results indicate that the proposed schemes provide a significant performance gain over conventional SMX.

## BICM-ID in two-way relaying communications

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:7511175
- **Type**: conference
- **Published**: 22-27 May 
- **Authors**: Hongzhong Yan, Ha H. Nguyen
- **PDF**: https://ieeexplore.ieee.org/document/7511175
- **Abstract**: This paper studies the technique of bit-interleaved coded modulation with iterative decoding (BICM-ID) in a two-way relaying communication system. Iterative decoding based on the quaternary code representation is adopted at the relay for the multiple access (MA) phase. An upper-bound of the bit error probability (BEP) under the error-free (EF) feedback assumption for BICM-ID in the MA phase is obtained. Based on the obtained EF bound of the BEP, it is found that the multiple-access interference (MAI) is successfully eliminated by performing the iterative decoding and XOR based network coding at the relay. Simulation results are provided to corroborate the analysis and demonstrate the performance superiority of the proposed framework.

## Optimum message mapping LDPC decoders derived from the sum-product algorithm

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:7510906
- **Type**: conference
- **Published**: 22-27 May 
- **Authors**: Jan Lewandowsky, Maximilian Stark, Gerhard Bauch
- **PDF**: https://ieeexplore.ieee.org/document/7510906
- **Abstract**: Starting from a discrete density evolution scheme originally introduced by Brian M. Kurkoski et al. which we improved by applying the Information Bottleneck method, we recently presented results on message passing decoders for Low Density Parity Check codes that have much lower complexity than state of the art decoders. In the decoders all node operations are replaced by discrete message mappings of unsigned integers what yields a great complexity reduction. Anyway the decoders perform very close to belief propagation decoding. New included simulation results prove that using a 4 bit integer architecture these decoders loose only 0.1 dB over Eb/No in comparison to an exact belief propagation decoder applied to the quantized output of a Gaussian channel. The most important contribution of this paper is the derivation of the message mapping decoders from the sum-product algorithm. Until now these decoders are assumed to not be linked to this algorithm. In order to reveal the hidden connection, we explain the decoding principle of the message mapping decoders in general factor graphs.

## Bit-flipping LDPC under noise conditions and its application to physically unclonable functions

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:7527440
- **Type**: conference
- **Published**: 22-25 May 
- **Authors**: Takao Marukame, Alexandre Schmid
- **PDF**: https://ieeexplore.ieee.org/document/7527440
- **Abstract**: A low-density parity check (LDPC) circuit and its properties as a post-processor is proposed for physically unclonable functions (PUFs) applications. PUFs can be realized using process variations or signal noises in SRAM or other PUF circuits, whereas the generated data needs to be processed by error check and correction (ECC) because of their inherent intra-PUF variabilities. The bit-flip LDPC circuits that have been developed in this study reveal compact constructions as well as notable noise tolerances during the ECC calculations. Unlike conventional deterministic post-processing, the LDPC circuits made even under unreliable fabrication conditions keep capable of guaranteeing robustness against noises.

## Construction of parallelized-decoding LDPC codes

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:7527261
- **Type**: conference
- **Published**: 22-25 May 
- **Authors**: Tsung-Che Wu, Chang-Ming Lee, Cheng-Kuei Wang
- **PDF**: https://ieeexplore.ieee.org/document/7527261
- **Abstract**: In the parallelization for high-throughput applications, the number of independent memory access usually dominates the coding throughput. Moreover, a class of large-girth low-density parity check (LDPC) codes usually has difficulties to realize the parallelization in the decoder. To cope with these obstacles, we propose an efficient code construction to take the number of required parallel decoding unit and the large-girth constraint into considerations at once. First, the parity check matrix would be split into the block-wise structure to fit the parallelization in the decoder. Second, the conversion of the cycle-checking inequalities can transform the girth issue into a linear system. Finally, based on the decomposition of the polyhedral set, the Smith normal form can efficiently solve inequalities of the proposed system. Simulation results show that the proposed code construction can satisfy the requirements of parallelization and high-performance coding with girth g = 12.

## Hardware decoders for polar codes: An overview

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:7527192
- **Type**: conference
- **Published**: 22-25 May 
- **Authors**: Pascal Giard, Gabi Sarkis, Alexios Balatsoukas-Stimming +5
- **PDF**: https://ieeexplore.ieee.org/document/7527192
- **Abstract**: Polar codes are an exciting new class of error correcting codes that achieve the symmetric capacity of memoryless channels. Many decoding algorithms were developed and implemented, addressing various application requirements: from error-correction performance rivaling that of LDPC codes to very high throughput or low-complexity decoders. In this work, we review the state of the art in polar decoders implementing the successive-cancellation, belief propagation, and list decoding algorithms, illustrating their advantages.

## A cost-effective approach for ubiquitous broadband access based on hybrid PLC-VLC system

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:7539178
- **Type**: conference
- **Published**: 22-25 May 
- **Authors**: Jian Song, Sicong Liu, Guangxin Zhou +6
- **PDF**: https://ieeexplore.ieee.org/document/7539178
- **Abstract**: Visible light communication (VLC) using the light emitting diode (LED) will become an appealing alternative to the radio frequency communication technology for indoor wireless broadband access. However, VLC needs a ubiquitous network as its backbone to avoid becoming an information isolated island. Power line communication (PLC) systems could easily solve the informative problem of VLC while powering the LED lamps at the same time, which is considered as a good partner of VLC for the cost-effective implementation. In this paper, a novel and cost-effective framework of ubiquitous indoor broadband access based on deeply integrated VLC and PLC technology with only low-cost modification to the current infrastructure is therefore proposed. The broadband access network supports duplex transmission through each LED using the decode-and-forward (DF) working mode. This paper will present our recent research progress in this area, including a prototyping of duplex voice communications network based on hybrid PLC and VLC in our lab. Our research and development plan in this area for the near future will also be covered.

## Joint detection and decoding for MIMO systems with polar codes

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:7527195
- **Type**: conference
- **Published**: 22-25 May 
- **Authors**: Junmei Yang, Chuan Zhang, Wenqing Song +2
- **PDF**: https://ieeexplore.ieee.org/document/7527195
- **Abstract**: As well known, the near-optimal K-best detection is popular in multiple-input and multiple-output (MIMO) systems. In this paper, we first propose the joint approaches of K-best detection and polar decoding. For joint detection and decoding (JDD) approach, both hard and soft decisions are considered. The simplified successive cancellation (SSC) decoding is exploited for hard decision, and the successive cancellation list (SCL) decoding is used as soft decision. The system setup for JDD is als o introduced, in which the modulation points across several channels are considered together. Simulation results have demonstrated the performance advantage of the JDD algorithms over the separated ones. For 1/2-rate polar codes, JDD schemes show 50% complexity reduction compared to the separated ones. Furthermore, by employing SSC hard decoding, the JDD algorithm is promising for high-throughput and low-complexity application s.

## Concatenations of systematic polar codes with inner repeat accumulate codes

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:7506571
- **Type**: conference
- **Published**: 21-23 May 
- **Authors**: Hao Ye, Zhi Zhang
- **PDF**: https://ieeexplore.ieee.org/document/7506571
- **Abstract**: Polar codes, proposed by Erdal Arikan, have attracted a lot of interest in the field of channel coding for their capacity-achieving trait as well as their low encoding and decoding complexity of the order O(NlogN) under successive cancellation (SC) decoder. However, there remains one significant drawback, that is, the error correction performance of small and moderate length polar codes is unsatisfactory, especially when compared with low density parity check (LDPC) codes and turbo codes. To this end, We propose a novel concatenation scheme which employs interleaved repeat accumulate (RA) codes as inner codes and systematic polar codes as outer codes. At the end of this paper, we present the simulation results in binary-input additive white Gaussian noise (BI-AWGN) channel with binary phase shift keying (BPSK) modulation, and we observe that, our proposed concatenation scheme significantly outperforms the conventional non-systematic inner polar codes in the high signal-to-noise (SNR) regime.

## Simplified BATS codes for deep space multihop networks

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:7560372
- **Type**: conference
- **Published**: 20-22 May 
- **Authors**: Zhao Huakai, Dong Guangliang, Li Haitao
- **PDF**: https://ieeexplore.ieee.org/document/7560372
- **Abstract**: Deep space multihop networks suffer many challenges such as long propagation delay, high error rate and frequent disturption. Channels above these networks are supposed as multihop erasure channels, on which BATS codes work well. BATS codes is a coding scheme that consists of an outer code and an inner code. The outer code is a matrix generation of a fountain code. It works with the inner code that comprises random linear network coding at the intermediate network nodes. BATS codes are suitable for deep space multihop networks, but have complicated coding rule. This paper proposes a simplified BATS codes. Simulations and analyses are made to evaluate the performance of the simplified BATS codes.

## Performance analysis of concatenated codes for different channels

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:7807917
- **Type**: conference
- **Published**: 20-21 May 
- **Authors**: N K Sharanya, S Jayashree
- **PDF**: https://ieeexplore.ieee.org/document/7807917
- **Abstract**: Forward Error Correction codes are required to remove errors such as noise, crosstalk etc that transpire in communication channel. In this paper, we propose a concatenated (Single Parity Check, BCH and Low Density Parity Check) coding method to remove the errors and improve the efficiency of the system. Simulation results shows that Single Parity Check method along with BCH and Low Density Parity Check gives better results. Performance of these coding methods in different channels such as AWGN, Rayleigh and Rician channels are also simulated. SPC method having simple encoding and decoding mechanism does not give good BER. LDPC in contrast to BCH achieves higher performance and better error correction capability.

## REAL: A retention error aware LDPC decoding scheme to improve NAND flash read performance

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:7897085
- **Type**: conference
- **Published**: 2-6 May 20
- **Authors**: Meng Zhang, Fei Wu, Xubin He +3
- **PDF**: https://ieeexplore.ieee.org/document/7897085
- **Abstract**: Continuous technology scaling makes NAND flash cells much denser. As a result, NAND flash is becoming more prone to various interference errors. Due to the hardware circuit design mechanisms of NAND flash, retention errors have been recognized as the most dominant errors, which affect the data reliability and flash lifetime. Furthermore, after experiencing a large number of programm/erase (P/E) cycles, flash memory would suffer a much higher error rate, rendering traditional ECC codes (typically BCH codes) insufficient to ensure data reliability. Therefore, low density parity check (LDPC) codes with stronger error correction capability are used in NAND flash-based storage devices. However, directly using LDPC codes with belief propagation (BP) decoding algorithm introduces non-trivial overhead of decoding latency and hence significantly degrades the read performance of NAND flash. It has been observed that flash retention errors show the so-called numerical-correlation characteristic (i.e., the 0-1 bits stored in the flash cell affect each other with the leakage of the charge) in each flash cell. In this paper, motivated by the observed characteristic, we propose REAL: a retention error aware LDPC decoding scheme to improve NAND flash read performance. The developed REAL scheme incorporates the numerical-correlation characteristic of retention errors into the process of LDPC decoding, and leverages the characteristic as additional bits decision information to improve its error correction capabilities and decrease the decoding latency. Our simulation results show that the proposed REAL scheme can reduce the LDPC decoding latency by 26.44% and 33.05%, compared with the Logarithm Domain Min-Sum (LD-MS) and Probability Domain BP (PD-BP) schemes, respectively.

## Exploiting latency variation for access conflict reduction of NAND flash memory

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:7897088
- **Type**: conference
- **Published**: 2-6 May 20
- **Authors**: Jinhua Cui, Weiguo Wu, Xingjun Zhang +2
- **PDF**: https://ieeexplore.ieee.org/document/7897088
- **Abstract**: NAND flash memory has been widely used in storage systems by offering greater read/write performance and lower power consumption than mechanical hard drives. Recently, the tradeoff between endurance, write speed, and read speed has been exploited from many ways for I/O performance improvement, which also induce the read/write latency variation. In this paper, the latency variation is exploited in I/O scheduling for access characteristic guided read and write latency minimization. First, with the understanding of the relationship among read latency, write latency and raw bit error rates (RBER), different ways to exploit the relationship for read and write latency reduction is discussed. Then, an I/O scheduling scheme is proposed by using hotness and retention age of accessed data to determine the speed of writes or reads, giving scheduling priority to fast writes and fast reads for conflict reduction. Experiments with various traces reveal that the proposed technique achieves significant read and write performance improvements.

## Iterative Detection using MMSE-PIC Demapping for MIMO-GFDM Systems

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:7499256
- **Type**: conference
- **Published**: 18-20 May 
- **Authors**: Maximilian Matthe, Dan Zhang, Gerhard Fettweis
- **PDF**: https://ieeexplore.ieee.org/document/7499256
- **Abstract**: Diverse requirements are foreseen for the 5G cellular system and new waveforms are being researched for the physical layer (PHY), where the non-orthogonal Generalized Frequency Division Multiplexing (GFDM) is one candidate. Its inherent self-interference makes receiver design challenging, particularly when besides inter-carrier interference (ICI) and inter-symbol interference (ISI) also inter-antenna interference (IAI) occurs, as in systems that employ spatial multiplexing (SM) to increase the throughput. To encounter this interference, we apply the prominent minimum mean squared error with parallel interference cancellation (MMSE-PIC) iterative receiver structure to GFDM, and provide a formulation that is suitable for a low-complexity implementation. We analyze the decoding performance employing a well-known current WiMax LDPC code. The proposed demapping algorithm can be implemented with complexity that scales linearly with the number of subcarriers of the system. Analysis of information transfer characteristics shows that the MMSE-PIC demapper for GFDM exhibits potential to outperform the OFDM demapper with a matching code, however, simulations of frame error rate (FER) show inferior performance of GFDM. These results emphasize the importance of a joint waveform and code design in order to exploit the full potential of the MMSE-PIC receiver structure for GFDM.

## A heuristic method for adaptive linear programming decoding

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:7496077
- **Type**: conference
- **Published**: 16-19 May 
- **Authors**: Abdullah Sarıduman, Ali Emre Pusane, Z. Caner Taşkın
- **PDF**: https://ieeexplore.ieee.org/document/7496077
- **Abstract**: Adaptive linear programming (ALP) decoders are mainly used for decoding low-density parity-check (LDPC) codes. The principle of ALP decoders is based on generating redundant-parity check equations, which could eliminate fractional solutions of linear programming (LP) decoders. These generated redundant parity check equations increase the error rate performance of decoder. In this paper, LP model is defined with auxiliary variables to facilitate finding redundant-parity check equations, and redundant parity check equations are searched over proposed LP model with a heuristic method. Simulation results demonstrate that the proposed algorithm could find redundant-parity check equations in a shorter time than other ALP decoders.

## BP-based approximation methods for rateless codes

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:7496135
- **Type**: conference
- **Published**: 16-19 May 
- **Authors**: Cenk Albayrak, Kadir Türk
- **PDF**: https://ieeexplore.ieee.org/document/7496135
- **Abstract**: In this letter, belief propagation (BP) based approximation methods for low density parity check (LDPC) codes are adapted to the Luby transform (LT) soft decoder structure in order to reduce its computational complexity. The bit error rate (BER) performances of the algorithms over the binary input additive white Gaussian noise (BIAWGN) channel are obtained by both theoretically and simulations. For theoretical analysis, the Monte-Carlo density evolution (MC-DE) method is used. In addition, computational complexity analyzes of methods are presented. Results show that the computational complexity can be significantly decreased with a limited performance loss cost.

## Non-binary LDPC codes over finite division near rings

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:7500492
- **Type**: conference
- **Published**: 16-18 May 
- **Authors**: Matthias Korb, Andrew Blanksby
- **PDF**: https://ieeexplore.ieee.org/document/7500492
- **Abstract**: It is almost always assumed that the algebraic structure underlying non-binary Low-Density Parity-Check (LDPC) codes are Finite Fields. However, when considering non-binary LDPC belief-propagation (BP) decoding, Finite Fields are actually over constrained. In this contribution, we discuss the minimal requirements of the algebraic structure used for non-binary LDPC decoding which we denote Finite Division Near Ring over a Subtractive Near Group. To verify the requirements, a general Min-Max decoding algorithm is derived that incorporates any algebraic structure fulfilling this minimal requirement set. It is shown that by relaxing the mathematical constraints, the decoding performance of non-binary LDPC codes can be incrementally improved compared to a Finite-Field-based LDPC code without any additional hardware cost.

## Optimized constellation design for P-LDPC coded multi-color visible light communications

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:7500474
- **Type**: conference
- **Published**: 16-18 May 
- **Authors**: Chengjun Tang, Ming Jiang, Hong Shen +1
- **PDF**: https://ieeexplore.ieee.org/document/7500474
- **Abstract**: In this paper, we advocate a novel constellation design methodology for multi-color visible light communication (VLC) systems deploying protograph-based low-density parity-check (P-LDPC) codes. We utilize the protograph-based extrinsic information transfer (PEXIT) analysis to evaluate the coded system performance accurately and employ the differential evolution algorithm for the optimal constellation design. Both numerical analyses and simulations show performance gains of more than 0.9 dB and demonstrate that our constellation design exhibits much better performance than the conventional ones such as the commonly used minimum Euclidean distance maximization design.

## Incremental Decoding Schedules for Puncture-Based Rate-Compatible LDPC Codes

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:7504285
- **Type**: conference
- **Published**: 15-18 May 
- **Authors**: Huang-Chang Lee, Yeong-Luh Ueng
- **PDF**: https://ieeexplore.ieee.org/document/7504285
- **Abstract**: This paper shows that the decoding convergence of the punctured low-density parity-check (LDPC) codes can be significantly increased using edge wise scheduling belief-propagation. If rate- compatible (RC)-LDPC codes constructed based on puncturing are considered, the maximum mutual information increase (M^2I^2)-based algorithm can be used to arrange fixed schedules for incremental decoding, and further reduce the required number of iterations. With the assistance of the proposed decoding schedules, the puncture-based RC-LDPC codes can be a potential solution for delay- sensitive HARQ (Hybrid-Automatic Repeat reQuest) applications.

## 17x Reliability Enhanced LDPC Code with Burst-Error Masking and High-Precision LLR for Highly Reliable Solid-State-Drives with TLC NAND Flash Memory

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:7493561
- **Type**: conference
- **Published**: 15-18 May 
- **Authors**: Tsukasa Tokutomi, Ken Takeuchi
- **PDF**: https://ieeexplore.ieee.org/document/7493561
- **Abstract**: Highly reliable LDPC ECC is introduced to improve the reliability of solid-state drives (SSDs). Although conventional AEP-LDPC ECC [3] is 12x highly reliable than BCH ECC, its error-correction capability is degraded due to the burst-errors and inaccurate log- likelihood ratio (LLR). To improve the reliability of TLC NAND flash, this paper proposes the burst-error masking (BEM) and program-disturb merged LLR estimation (PMLE). The first proposal, BEM eliminates the burst- errors by recording the error-location to the table. The second proposal, PMLE calculates the ratio of program-disturb errors to data-retention errors. As a result, more precise LLR is obtained. By combining BEM and PMLE, the SSD lifetime is extended by 17x and the table size overhead is reduced by 81%.

## Adaptive granular HARQ LDPC-based coding for secrecy enhancement in wiretap channels

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:7726710
- **Type**: conference
- **Published**: 15-18 May 
- **Authors**: Ahmadreza Amirzadeh, Mohamed Haj Taieb, Jean-Yves Chouinard
- **PDF**: https://ieeexplore.ieee.org/document/7726710
- **Abstract**: In this work, reliable and secure transmission over generic-Gaussian wiretap channel model is investigated. An Adaptive Granular Hybrid Automatic Repeat reQuest (AG-HARQ) protocol is proposed which tries to minimize the required rate for successful decoding by the legitimate parties while amplifying the privacy by minimizing the information leakage to a wiretapper. In the case of LDPC decoding failure at the legitimate receiver (Bob), a retransmission is requested until correct decoding or until the maximum number of transmitted packets is reached. As soon as Bob is able to correctly decode the LDPC codeword, the retransmissions are stopped to avoid any additional bits leakage to the eavesdropper (Eve). In our proposed method, to minimize the leakage, a confidence level index, Cj, for correct decoding is defined as the mean of absolute value of the Log-Likelihood Ratio (LLR). In the case of failure, only the sub-packets with the smallest Cj values will be retransmitted since they represent the most unreliable information sub-packets. Frame Error Rate (FER) is used as a metric to show the effectiveness of the proposed method.

## A New Architecture for High Speed, Low Latency NB-LDPC Check Node Processing for GF(256)

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:7504085
- **Type**: conference
- **Published**: 15-18 May 
- **Authors**: V. Rybalkin, P. Schlafer, N. Wehn
- **PDF**: https://ieeexplore.ieee.org/document/7504085
- **Abstract**: Non-binary low-density parity-check codes have superior communications performance compared to their binary counterparts. However, to be an option for future standards, efficient hardware architectures are mandatory. State-of-the-art decoding algorithms result in architectures suffering from low throughput and high latency. The check node function accounts for the largest part of the decoders overall complexity. To the best of our knowledge, we propose the first architecture for high speed, low latency Non-Binary Low-Density Parity-Check Check Node processing for GF(256). It has state-of-the-art communications performance while largely reducing the hardware complexity. The presented architecture has a 3.3 times higher area efficiency, increases the energy efficiency by factor 2.5 and reduces the latency by factor of 5.5 compared to the first implementation of Check Node for GF(256) based on the state-of-the-art FWBW scheme that was also implemented in the scope of this work.

## Design of Short Quasi-Cyclic LDPC Codes for Next Generation Broadcast Wireless Systems

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:7504191
- **Type**: conference
- **Published**: 15-18 May 
- **Authors**: Fang Wang, Yajun Kou, Ming Jiang +1
- **PDF**: https://ieeexplore.ieee.org/document/7504191
- **Abstract**: Chinese next generation broadcast wireless (NGB-W) systems are aimed to provide high-speed, ubiquitous, and secure broadcast services and tri-play services to massive users. New terrestrial broadcast techniques are needed to support these services in NGB-W systems. In this paper, a new set of quasi-cyclic (QC) low density parity check (LDPC) codes with a moderate code length and a wide operation range are proposed for NGB-W systems. It is shown by simulations that the perfor-mance of the proposed LDPC codes is much better than that of the LDPC codes used in the second generation television broad-cast of digital video broadcasting (DVB-T2/NGH) systems.

## Construction of Structured LDPC Code Based on Correlation Limitation

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:7504175
- **Type**: conference
- **Published**: 15-18 May 
- **Authors**: Jun Xu, Dongming Wang, Jin Xu +3
- **PDF**: https://ieeexplore.ieee.org/document/7504175
- **Abstract**: Channel coding for the next generation communication system needs to support higher data throughput and transmission rate. Due to the inherent parallel feature, low density parity check (LDPC) codes comply with the target. In this paper, we propose a complete channel coding scheme based on structured LDPC codes. In our design, the correlation among different parity check matrices for different code rates is established, meanwhile the correlation between adjacent rows is established, then matrix design should be restricted by these two type defined correlations in order to make great progress in the support of multiple code rates and layered decoding algorithm. Our scheme includes the definition of the four matrices and five constraint features of these matrices, also the benefits of these features are analyzed. Simulation result shows that the performance of the proposed scheme is the same as or a little better than that of 11ad LDPC codes. The proposed LDPC scheme obviously decreases route complexity and increases decoder throughput. So, this scheme is very suitable for high speed decoder with more than 1Gbps throughput in various future communication systems.

## Modulation assisted preprocessing for non-binary LDPC decoding with extended min-sum algorithm

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:7726728
- **Type**: conference
- **Published**: 15-18 May 
- **Authors**: Tianqing Wu, Hong-Chuan Yang, Jingwen Yan
- **PDF**: https://ieeexplore.ieee.org/document/7726728
- **Abstract**: We propose a modulation assisted preprocessing scheme to reduce the computational complexity of non-binary LDPC decoding. With the proposed scheme, the received signal is directly mapped onto a truncated symbol vector through table lookup. The mapping table can be built off-line based on the characteristics of the constellation structure. The receiver needs only to calculate and, if necessary, rank the reliability of the symbols in the truncated vectors, which avoids unnecessary reliability calculation and ranking during on-line operation. The complexity analysis shows that the proposed preprocessing scheme leads to much lower computational complexity, in terms of ranking and addition operations, while offering the same error rate performance as conventional EMS preprocessing scheme.

## Construction of High-Rate Generalized Concatenated Codes for Applications in Non-Volatile Flash Memories

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:7493571
- **Type**: conference
- **Published**: 15-18 May 
- **Authors**: Jens Spinner, Mohammed Rajab, Jurgen Freudenberger
- **PDF**: https://ieeexplore.ieee.org/document/7493571
- **Abstract**: This work proposes a construction for high-rate generalized concatenated (GC) codes. The proposed codes are well suited for error correction in flash memories for high reliability data storage. The GC codes are constructed from inner nested binary Bose-Chaudhuri-Hocquenghem (BCH) codes and outer Reed-Solomon (RS) codes. For the inner codes we propose extended BCH codes, where we apply single parity-check codes in the first level of the GC code. This enables high-rate codes.

## Implementation of decoders for symmetric low density parity check codes on parallel computation platforms using OpenCL

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:7726832
- **Type**: conference
- **Published**: 15-18 May 
- **Authors**: Andrew J. Maier, Bruce F. Cockburn
- **PDF**: https://ieeexplore.ieee.org/document/7726832
- **Abstract**: OpenCL is a high-level language that allows mixed hardware/software systems to be specified and compiled to run on heterogeneous parallel computing platforms. The hardware parallelism can take the form of multi-core central processing units (CPUs), massively parallel graphics processing units (GPUs), and, most recently, field-programmable gate array (FPGA) fabrics. OpenCL compilers for CPUs and GPUs have been available for over 6 years, but only recently has compiler support been extended to include FPGAs. This paper investigates OpenCL designs for the computationally demanding standard iterative decoding algorithm for low-density parity check (LDPC) codes. The LDPC decoding algorithm offers several kinds of potentially exploitable parallelism. Our objective was to investigate the design trade-offs in OpenCL that will produce the best performance when compiled by the Altera Offline Compiler (AOC v15.1) for OpenCL-to-FPGA. Within a relatively short design time we were able to implement a decoder that achieved 5.12 Mbps with a length-1024 (3,6)-regular code.

## LDPC-Coded Index-Modulation Aided OFDM for In-Vehicle Power Line Communications

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:7504318
- **Type**: conference
- **Published**: 15-18 May 
- **Authors**: Hongming Zhang, Lie-Liang Yang, Lajos Hanzo
- **PDF**: https://ieeexplore.ieee.org/document/7504318
- **Abstract**: The recently developed orthogonal frequency-division multiplexing relying on index modulation (OFDM-IM) is adopted to the in-vehicle power line communications (PLCs) in order to combat the deleterious effects of frequency-selective fading and impulsive noise, whilst improving the energy efficiency of data communications. Furthermore, the low density parity check (LDPC) coding is invoked to further enhance the reliability of in-vehicle PLCs, which is of particular importance in light-weight airborne vehicles. For aiding LDPC decoding, a reduced complexity soft-decision detection scheme is proposed. The performance of the LDPC-coded OFDM-IM system is studied by simulation, when assuming communications over in-vehicle PLC channels. Our studies show that LDPC-coded OFDM-IM is capable of combating frequency-selective fading, mitigating impulsive noise, as well as striking a compelling trade-off between the spectral efficiency and energy efficiency for in-vehicle PLCs.

## Design of LDPC Coded CPM over Burst-Error Channels

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:7504189
- **Type**: conference
- **Published**: 15-18 May 
- **Authors**: Chunhui Shen, Li Bing, Baoming Bai
- **PDF**: https://ieeexplore.ieee.org/document/7504189
- **Abstract**: In the paper, a class of LDPC coded continuous phase modulation (CPM) systems is proposed for reliable communication over burst-error channels. A series of binary LDPC codes with code rates 1/4, 1/2 and 2/3 are chosen for binary and quaternary CPM schemes. A non-recursive decomposition of CPM is incorporated to eliminate the error propagation caused by burst errors. To reduce the complexity, an improved demodulation algorithm for noncoherent soft in soft out (N-SISO) is considered. Simulation results show that the proposed LDPC coded CPM offers a better error performance and is abler to recover the transmitted information under severe burst errors than current systems.

## Finite Length Design of Precoded EWF Codes

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:7504247
- **Type**: conference
- **Published**: 15-18 May 
- **Authors**: Lei Yuan, Huaan Li, Yi Wan
- **PDF**: https://ieeexplore.ieee.org/document/7504247
- **Abstract**: Novel precoded Expanding Window Fountain (EWF) codes, based on low rate low-density parity-check (LDPC) codes, are investigated for finite message length over binary erasure channels (BECs). The proposed codes are obtained by utilizing low rate LDPC codes as precodes and degree distributions with high intermediate symbol recovery rate for EWF codes. Simulation results show that, compared with conventional precoded EWF codes, our proposed codes have better performance in the scenarios of small and moderate message lengths over the BEC.

## Graph-Based Decoding for High-Dense Vehicular Multiway Multirelay Networks

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:7504263
- **Type**: conference
- **Published**: 15-18 May 
- **Authors**: Khoirul Anwar
- **PDF**: https://ieeexplore.ieee.org/document/7504263
- **Abstract**: Densely deployed wireless networks is one of the most important solutions for spectrum shortage expected by 2020 with a huge economic impact. This paper proposes decoding schemes for high- dense vehicular multiway multirelaying (HDV-MWMR) systems comprising multiple multiway relays to serve huge number of users or devices. Due to the nature of huge number, instead of using perfect scheduling, we consider coded random access schemes, where all users transmit their messages uncoordinatedly. Although the transmission is random, the network structures still can be seen as codes-on-the-graph, resembling Low Density Parity Check (LDPC) codes structure, expected to provide an additional gain. The theoretical network capacity bound for HDV-MWMR systems exploiting multiple multiway relays is derived and confirmed via extrinsic information transfer (EXIT) chart analysis and computer simulations. To achieve the network capacity bound, we propose simple decoding schemes based on successive interference cancellation over a sparse graph involving multiple multiway relays. Suitable degree distributions for Rayleigh fading channels are investigated. The results confirm that multiple relays help both on (i) improving the throughput performances, and (ii) capturing the network diversity, which are highly required for future wireless networks.

## Comparison of Interference Cancellation Schemes for Non-Orthogonal Multiple Access System

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:7504172
- **Type**: conference
- **Published**: 15-18 May 
- **Authors**: Guanghui Song, Xianbin Wang
- **PDF**: https://ieeexplore.ieee.org/document/7504172
- **Abstract**: Three potential interference cancellation schemes are compared for the application to a non-orthogonal multiple access communication system. One is the conventional hard successive interference cancellation (SIC) scheme based on independent single-user decodings. The other two, proposed in this paper, are a soft-in soft-out parallel interference cancellation (SISO-PIC) and a hybrid interference cancellation (HIC). The SISO-PIC is an improved joint iterative multi-user detection scheme, which has lower complexity than the prevalent multi-user detection. The HIC combines the advantages of the above two schemes to permit users to be successively processed by a SISO-PIC window according to their receive power levels. A comprehensive comparison is given for these three schemes in aspects of error propagation, detection delay, and complexity when a practical channel code, repeat-accumulate code, is employed. Numerical results show that HIC is a trade-off scheme of the three aspects.

## Hybrid Beamforming with Time Delay Compensation for Millimeter Wave MIMO Frequency Selective Channels

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:7504275
- **Type**: conference
- **Published**: 15-18 May 
- **Authors**: Gaojian Wang, Jiaxin Sun, Gerd Ascheid
- **PDF**: https://ieeexplore.ieee.org/document/7504275
- **Abstract**: The fading channel in mmWave communications has a very high chance to be frequency selective owing to the large transmission bandwidth. To overcome the frequency selectivity we propose a novel method, namely RF beamforming with time delay compensation. Simultaneously, baseband precoder at the transmitter side and the combiner at the receiver side are employed to maximize the capacity of the system. For effectively flattening the channel by beamforming on both sides, it is necessary to separate the individual rays. Motivated by achieving the best case beam separation, a signal-to-interference ratio (SIR) constrained capacity maximization algorithm is proposed in this paper. We also study the influence of the parameters such as the number of antennas at the transmitter side and the SIR threshold on the capacity and the system performance. Finally, the proposed method is validated by providing numerical examples by means of simulation.

## Low-Delay Transmission Scheme Based on LT Code Employing Hybrid Decoding

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:7504331
- **Type**: conference
- **Published**: 15-18 May 
- **Authors**: Qixian Zhang, Xuan Feng, Guixing Cao +2
- **PDF**: https://ieeexplore.ieee.org/document/7504331
- **Abstract**: Satellite communication plays an important role in the ubiquitous global communication. However, for a long time, the communication provided by satellite suffers from serious signal attenuation and transmission delay. Conventional techniques such as HARQ couldn't provide timely service unless powerful channel codes are used. Once channel code fails, retransmission will be inevitable, and unbearable delay may be incurred. Fortunately, things started to change when Luby proposed the landmark LT code. As a practical implementation of fountain code, LT code avoids frequent feedback during the transmission. However, due to the high packet error rate (PER), the original LT code couldn't work stably in satellite communication. In this paper, we propose a novel hybrid decoding scheme for LT code. It consists of two decoding procedures: normal decoding using BP algorithm and mining decoding. The idea behind mining decoding is to release as many corrupted original packets as possible and combine the "identical" ones as in HARQ. Actually we develop three types of packet mining techniques to make a tradeoff between performance and computation complexity. The final simulation shows that, the proposed hybrid decoding scheme makes LT code work more stably, and achieves significant advantages over HARQ in terms of delay.

## Performance Advantage of Joint Source-Channel Decoder over Iterative Receiver under M-ary Differential Chaotic Shift Keying Systems

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:7504399
- **Type**: conference
- **Published**: 15-18 May 
- **Authors**: Yibo Lyu, Lin Wang, Zixiang Xiong
- **PDF**: https://ieeexplore.ieee.org/document/7504399
- **Abstract**: In order to improve the error performance of M-ary differential chaotic shift keying (DCSK) systems over multi-path fading channel, two types of iterative structures have been employed in receiver design. One is joint source-channel decoder (JSCD), the other is iterative receiver (IR). Although several works have separately addressed the advantages of IR and JSCD, it is not clear which design provides more iterative gain for M-ary DCSK systems over multi-path fading channels. In this work, we employ the extrinsic information transfer (EXIT) chart technique to analyze the iteration behavior of JSCD and IR. Simulation results suggest that with enough source redundancy, JSCD outperforms IR under M-ary DCSK systems over multi-paths fading channels.

## Application Optimized Adaptive ECC with Advanced LDPCs to Resolve Trade-Off among Reliability, Performance, and Cost of Solid-State Drives

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:7493568
- **Type**: conference
- **Published**: 15-18 May 
- **Authors**: Yusuke Yamaga, Chihiro Matsui, Shogo Hachiya +1
- **PDF**: https://ieeexplore.ieee.org/document/7493568
- **Abstract**: The performance of NAND flash based solid-state drives (SSDs) is highly dependent on the application's read and write characteristics [3], where "intensity" is defined as ratio of read:write requests, and "write- hot/cold" considers the write frequency. Moreover, NAND flash memory's reliability degrades with write/erase (W/E) cycling. To optimize performance and reliability, conventional error-correcting code (ECC) scheme switches from fast conventional Bose-Chaudhuri- Hocquenghem (BCH) to slower conventional Low Density Parity Check (LDPC), when the page error rate exceeds BCH's decoding capability. However, advanced LDPCs have been reported, called Quick-LDPC [8] and Error- Prediction (EP-) LDPC without (w/o) upper/lower cells [8], which have (i) higher error correction capability compared to conventional BCH and (ii) shorter decoding time than conventional soft-decoding LDPC. Therefore, this paper proposes an application optimized adaptive (AOA-) ECC for Multi-Level-Cell (MLC) NAND flash-based enterprise SSDs. AOA-ECC includes a new algorithm to efficiently combine the two advanced LDPCs, considering the application's characteristics and memory's W/E cycles. A firmware in the proposed SSD system chooses the optimal advanced LDPC, based on whether the application is read/write-intensive and/or write- hot/cold. Using the proposed AOA-ECC SSD with MLC NAND flash, performance improves by up to 3-times, the reliability improves by 57% and the ECC decoder area decreases by 25%.

## On the Simultaneous Exploitation of Multiple Source-to-Relay Channels in Buffer-Aided Two-Hop Cooperative Networks

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:7504380
- **Type**: conference
- **Published**: 15-18 May 
- **Authors**: Miharu Oiwa, Shinya Sugiura
- **PDF**: https://ieeexplore.ieee.org/document/7504380
- **Abstract**: Motivated by the recent buffer-aided cooperative protocols that select the single best link at each time slot, in this paper we introduce additional design degree of freedom into them, by simultaneously exploiting broadcast channels between the source node and the multiple buffer- aided relay nodes. More specifically, our proposed scheme is designed to allow multiple relay nodes to receive a specific source packet through source-to-relay broadcast channels, hence resulting in multiple copies of the source packet, which are stored in buffers of the relay nodes. As the results, our proposed protocol is capable of reducing the overhead required for monitoring the available links and the end-to-end packet delay, in comparison to the conventional buffer-aided cooperative protocols, while attaining a high diversity order comparable to that of the max-link protocol.

## Code-Aided Joint Carrier Phase Estimation and Ambiguity Resolution for APSK Signals

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:7504164
- **Type**: conference
- **Published**: 15-18 May 
- **Authors**: Desheng Shi, Nan Wu, Hua Wang +2
- **PDF**: https://ieeexplore.ieee.org/document/7504164
- **Abstract**: A maximum likelihood-based code-aided joint carrier phase estimation and ambiguity resolution algorithm is proposed for coded amplitude and phase shift keying (APSK) signals. The proposed estimator iteratively uses the a posteriori probability of coded bits obtained from the channel decoder to improve the performance of phase estimation and ambiguity resolution. Two initialization schemes are employed for systems with and without pilot symbols, which reduce the number of initial phase values required to bootstrap the iterative estimation algorithm. Compared with the existing estimators, simulation results demonstrate the performance improvement of the proposed algorithm in both mean-squared estimation error and bit error rate with lower computational complexity.

## A subtraction based method for the construction of quasi-cyclic LDPC codes of girth eight

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:7491830
- **Type**: conference
- **Published**: 12-14 May 
- **Authors**: Ambar Bajpai, Lunchakorn Wuttisittikulkij, Abhishek Kalsi +1
- **PDF**: https://ieeexplore.ieee.org/document/7491830
- **Abstract**: This article presents a simple, less computational complexity method for constructing exponent matrix (3, K) having girth at least 8 of quasi-cyclic low-density parity-check (QC-LDPC) codes based on subtraction method. The construction of code deals with the generation of exponent matrix by three formulas. This method is flexible for any block-column length K. The simulations are shown in comparison with some existing appreciable work. The codes with girth 8 are constructed with circulant permutation matrix (CPM) size P ≥ max{a2, r, a2, r,….a2, k} + 1.

## Novel multi-Gbps bit-flipping decoders for punctured LDPC codes

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:7495161
- **Type**: conference
- **Published**: 12-14 May 
- **Authors**: Christina Archonta, Nikos Kanistras, Vassilis Paliouras
- **PDF**: https://ieeexplore.ieee.org/document/7495161
- **Abstract**: Conventional bit-flipping (BF) algorithms spectacularly fail to handle punctured LDPC codes as they use hard decisions and, therefore, they cannot effectively cope with zero-reliability punctured symbols. However, BF techniques lead to low-cost high-speed decoders. This paper introduces a novel method that enables the use of BF-based iterative decoders for punctured LDPC codes. An erasure preprocessor is introduced and is shown to successfully mitigate the impact of puncturing, substantially improving the coding gain achieved for punctured codes under BF decoding. The proposed technique renders BF decoding of punctured codes useful, something that was not possible so far to our knowledge. Furthermore, two hardware architectures are introduced and evaluated. Hardware sharing is shown to efficiently exploit common structures in the proposed combined erasure and BF decoder, leading to a new architecture found to be particularly efficient. The proposed architecture requires extremely low hardware resources, facilitating full-parallel architectures that sustain multi-Gbps throughput rates when implemented on Virtex-7 FPGA devices.

## Architecture of a NVM-based storage system using adaptive LDPC codes

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:7495149
- **Type**: conference
- **Published**: 12-14 May 
- **Authors**: Stelios Korkotsides, Theodore A. Antonakopoulos
- **PDF**: https://ieeexplore.ieee.org/document/7495149
- **Abstract**: Low Density Parity Check (LDPC) codes have been widely used in communications systems due to their high error correction capabilities. Recently these codes are also investigated for being exploited in high performance storage systems, especially when Non-Volatile Memory (NVM) technologies are used. The main drawback of using LDPC codes in storage systems with a high number of parallel channels is the increased hardware complexity and cost, especially when variable rate codes are used. In this work, we present an architecture of a NVM-based storage system that dynamically adapts the LDPC's rate to the aging conditions of the storage device in order to maximize its lifetime capacity while keeping low its hardware complexity. In order to decrease the system's complexity we propose a PCIe-based architecture that uses a pool of LDPC decoders shared by all NVM channels and we study its effect on the system's lifetime capacity and the achievable I/O data rate.

## High data rate link modulation and coding scheme modeling

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:7491793
- **Type**: conference
- **Published**: 12-14 May 
- **Authors**: Alexander Bakhtin, Anastasia Semenova, Alexey Solodkov
- **PDF**: https://ieeexplore.ieee.org/document/7491793
- **Abstract**: This paper shows the results of simulation of high spectral efficiency modulation and coding scheme (MSC) which consist of modulation PSK-16+4PCM and error-correction Reed-Solomon code in comparison with other high spectral efficiency schemes for different radio link signal distortion ways. Proposed MSC show close result with PSK-64 with FEC and in comparison with QAM-64 with FEC proposed MSC showed faster performances degradation in non-ideal transmission conditions. But overall due the inherent features like low envelope amplitude variation and simple demodulation algorithm with moderate hardware complexity MSC PSK-16+4PCM+RS(253,244,13) can be applied in high-speed satellite radio downlink effectively.

## A low complexity hardware for compressive sensing matrix generation

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:7585600
- **Type**: conference
- **Published**: 10-12 May 
- **Authors**: Mohammad Fardad, Sayed Masoud Sayedi
- **PDF**: https://ieeexplore.ieee.org/document/7585600
- **Abstract**: In this paper a low complexity hardware is designed to generate a deterministic matrix for compressive sensing systems. The construction of the matrix is based on the connection between the parity check matrix of LDPC codes and the measurement matrix of compressive sensing. For efficient hardware realization, a geometric approach to the construction of LDPC codes is used for matrix generation on the fly without requiring a lot of storage. The performance of generated matrix is approved under ℓ1-minimization and OMP recovery algorithms, and it performs comparably to the corresponding random matrix. The described hardware has been implemented on a Xilinx Spartan 6 FPGA.

## High-Throughput Multi-Core LDPC Decoders Based on x86 Processor

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:7110620
- **Type**: journal
- **Published**: 1 May 2016
- **Authors**: Bertrand Le Gal, Christophe Jego
- **PDF**: https://ieeexplore.ieee.org/document/7110620
- **Abstract**: Low-Density Parity-Check (LDPC) codes are an efficient way to correct transmission errors in digital communication systems. Although initially targeting strictly to ASICs due to computation complexity, LDPC decoders have been recently ported to multicore and many-core systems. Most works focused on taking advantage of GPU devices. In this paper, we propose an alternative solution based on a layered OMS/NMS LDPC decoding algorithm that can be efficiently implemented on a multi-core device using Single Instruction Multiple Data (SIMD) and Single Program Multiple Data (SPMD) programming models. Several experimentations were performed on a x86 processor target. Throughputs up to 170 Mbps were achieved on a single core of an INTEL Core i7 processor when executing 20 layered-based decoding iterations. Throughputs reaches up to 560 Mbps on four INTEL Core-i7 cores. Experimentation results show that the proposed implementations achieved similar BER correction performance than previous works. Moreover, much higher throughputs have been achieved by comparison with all previous GPU and CPU works. They range from x1.4 to x8 by comparison with recent GPU works.
