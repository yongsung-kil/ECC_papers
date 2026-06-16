# IEEE Xplore — 2014-05


## Rate-0.96 LDPC Decoding VLSI for Soft-Decision Error Correction of NAND Flash Memory

- **ID**: ieee:6547748
- **Type**: journal
- **Published**: May 2014
- **Authors**: Jonghong Kim, Wonyong Sung
- **PDF**: https://ieeexplore.ieee.org/document/6547748
- **Abstract**: The reliability of data stored in high-density Flash memory devices tends to decrease rapidly because of the reduced cell size and multilevel cell technology. Soft-decision error correction algorithms that use multiple-precision sensing for reading memory can solve this problem; however, they require very complex hardware for high-throughput decoding. In this paper, we present a rate-0.96 (68254, 65536) shortened Euclidean geometry low-density parity-check code and its VLSI implementation for high-throughput NAND Flash memory systems. The design employs the normalized a posteriori probability (APP)-based algorithm, serial schedule, and conditional update, which lead to simple functional units, halved decoding iterations, and low-power consumption, respectively. A pipelined-parallel architecture is adopted for high-throughput decoding, and memory-reduction techniques are employed to minimize the chip size. The proposed decoder is implemented in 0.13-μm CMOS technology, and the chip size and energy consumption of the decoder are compared with those of a BCH (Bose-Chaudhuri-Hocquenghem) decoding circuit showing comparable error-correcting performance and throughput.

## Enhanced Precision Through Multiple Reads for LDPC Decoding in Flash Memories

- **ID**: ieee:6804933
- **Type**: journal
- **Published**: May 2014
- **Authors**: Jiadong Wang, Kasra Vakilinia, Tsung-Yi Chen +5
- **PDF**: https://ieeexplore.ieee.org/document/6804933
- **Abstract**: Multiple reads of the same Flash memory cell with distinct word-line voltages provide enhanced precision for LDPC decoding. In this paper, the word-line voltages are optimized by maximizing the mutual information (MI) of the quantized channel. The enhanced precision from a few additional reads allows frame error rate (FER) performance to approach that of full-precision soft information and enables an LDPC code to significantly outperform a BCH code. A constant-ratio constraint provides a significant simplification in the optimization with no noticeable loss in performance. For a well-designed LDPC code, the quantization that maximizes the mutual information also minimizes the FER in our simulations. However, for an example LDPC code with a high error floor caused by small absorbing sets, the MMI quantization does not provide the lowest frame error rate. The best quantization in this case introduces more erasures than would be optimal for the channel MI in order to mitigate the absorbing sets of the poorly designed code. The paper also identifies a trade-off in LDPC code design when decoding is performed with multiple precision levels; the best code at one level of precision will typically not be the best code at a different level of precision.

## Optimization of Generalized VDMM for Protograph-Based LDPC Coded BICM

- **ID**: ieee:6777400
- **Type**: journal
- **Published**: May 2014
- **Authors**: Chengjun Tang, Hong Shen, Ming Jiang +1
- **PDF**: https://ieeexplore.ieee.org/document/6777400
- **Abstract**: In this letter, we develop a generalized variable degree matched mapping (G-VDMM) framework to accommodate any protograph structure and modulation order in bit-interleaved coded modulation (BICM) systems deploying protograph-based low-density parity-check (P-LDPC) codes. To seek for the optimal G-VDMM scheme, we also propose an efficient algorithm requiring far less computational cost than a brute-force search. Both extrinsic information transfer (EXIT) analyses and simulations verify that our optimized interleaver exhibits better performance than conventional designs.

## Density Evolution for Min-Sum Decoding of LDPC Codes Under Unreliable Message Storage

- **ID**: ieee:6774414
- **Type**: journal
- **Published**: May 2014
- **Authors**: Alexios Balatsoukas-Stimming, Andreas Burg
- **PDF**: https://ieeexplore.ieee.org/document/6774414
- **Abstract**: We analyze the performance of quantized min-sum decoding of low-density parity-check codes under unreliable message storage. To this end, we introduce a simple bit-level error model and show that decoder symmetry is preserved under this model. Subsequently, we formulate the corresponding density evolution equations to predict the average bit error probability in the limit of infinite block length. We present numerical threshold results and we show that using more quantization bits is not always beneficial in the context of faulty decoders.

## Finite Alphabet Iterative Decoders for LDPC Codes: Optimization, Architecture and Analysis

- **ID**: ieee:6776564
- **Type**: journal
- **Published**: May 2014
- **Authors**: Fang Cai, Xinmiao Zhang, David Declercq +2
- **PDF**: https://ieeexplore.ieee.org/document/6776564
- **Abstract**: Low-density parity-check (LDPC) codes are adopted in many applications due to their Shannon-limit approaching error-correcting performance. Nevertheless, belief-propagation (BP) based decoding of these codes suffers from the error-floor problem, i.e., an abrupt change in the slope of the error-rate curve that occurs at very low error rates. Recently, a new type of decoders termed finite alphabet iterative decoders (FAIDs) were introduced. The FAIDs use simple Boolean maps for variable node processing, and can surpass the BP-based decoders in the error floor region with very short word length. We restrict the scope of this paper to regular dv=3 LDPC codes on the BSC channel. This paper develops a low-complexity implementation architecture for the FAIDs by making use of their properties. Particularly, an innovative bit-serial check node unit is designed for the FAIDs, and a small-area variable node unit is proposed by exploiting the symmetry in the Boolean maps. Moreover, an optimized data scheduling scheme is proposed to increase the hardware utilization efficiency. From synthesis results, the proposed FAID implementation needs only 52% area to reach the same throughput as one of the most efficient standard Min-Sum decoders for an example (7807, 7177) LDPC code, while achieving better error-correcting performance in the error-floor region. Compared to an offset Min-Sum decoder with longer word length, the proposed design can achieve higher throughput with 45% area, and still leads to possible performance improvement in the error-floor region.

## Classification Codes for Soft Information Generation from Hard Flash Reads

- **ID**: ieee:6804934
- **Type**: journal
- **Published**: May 2014
- **Authors**: Mustafa N. Kaynak, Patrick R. Khayat, Sivagnanam Parthasarathy
- **PDF**: https://ieeexplore.ieee.org/document/6804934
- **Abstract**: In this paper, a tensor product-based classification code (CC) is proposed to generate coarse soft information based on the hard flash reads for use in soft information-utilizing error correction codes (ECCs), particularly low-density parity check (LDPC) codes. Analysis and simulation results have shown that with a small ECC overhead, CC helps the LDPC code decoder achieve better performance compared to a hard-input case. Furthermore, the proposed code has very simple encoding and decoding algorithms; therefore, it can be easily implemented in hardware to aid existing ECC systems.

## Non-Binary LDPC Decoder Based on Symbol Flipping with Multiple Votes

- **ID**: ieee:6787156
- **Type**: journal
- **Published**: May 2014
- **Authors**: F. Garcia-Herrero, D. Declercq, J. Valls
- **PDF**: https://ieeexplore.ieee.org/document/6787156
- **Abstract**: In this letter, a new algorithm to decode non-binary LDPC (NB-LDPC) codes is proposed. This algorithm is inspired from very low complexity decoders that have been proposed recently, in which only syndrome computations at the check node update are used, while performing symbol-flipping based update at the variable node. Usually, the low complexity decoders based on symbol flipping suffer from a non-negligible performance degradation compared to soft-decision NB-LDPC decoders. Our improved decoder makes use of a list of syndrome computations instead of a single one based on hard-decision, and builds soft information at the variable node input by assigning votes weighted by different amplitudes. Simulations show that using multiple votes with multiple weights yields better performance, while still maintaining the low complexity feature.

## Structured Bit-Interleaved LDPC Codes for MLC Flash Memory

- **ID**: ieee:6804932
- **Type**: journal
- **Published**: May 2014
- **Authors**: Kathryn Haymaker, Christine A. Kelley
- **PDF**: https://ieeexplore.ieee.org/document/6804932
- **Abstract**: Due to a structural feature in the programming process of MLC (two bits per cell) and TLC (three bits per cell) flash memory, the majority of errors that occur are single-bit errors. Moreover, the voltages used to store the bits typically result in different bit error probabilities for the two or three types of bits. In this work we analyze binary regular LDPC codes in the standard bit-interleaved coded modulation implementation, assuming different probabilities on the bits, to determine what ratio of each type of bit should be connected at the check nodes to improve the decoding threshold. We then propose a construction of nonbinary LDPC codes using their binary images, resulting in check node types that come close to these optimal ratios.

## The Spammed Code Offset Method

- **ID**: ieee:6798816
- **Type**: journal
- **Published**: May 2014
- **Authors**: Boris Skoric, Niels de Vreede
- **PDF**: https://ieeexplore.ieee.org/document/6798816
- **Abstract**: Helper data schemes are a security primitive used for privacy-preserving biometric databases and physical unclonable functions. One of the oldest known helper data schemes is the code offset method (COM). We propose an extension of the COM: the helper data are accompanied by many instances of fake helper data that are drawn from the same distribution as the real one. While the adversary has no way to distinguish between them, the legitimate party has more information and can see the difference. We use a low-density parity check code in order to improve the efficiency of the legitimate party's selection procedure. Our construction provides a new kind of tradeoff: more effective use of the source entropy, at the price of increased helper data storage. We give a security analysis in terms of Shannon entropy and order-2 Rényi entropy. We also propose a variant of our scheme in which the helper data list is not stored but pseudorandomly generated, changing the tradeoff to source entropy utilization versus computation effort.

## Concatenated Raptor Codes in NAND Flash Memory

- **ID**: ieee:6804931
- **Type**: journal
- **Published**: May 2014
- **Authors**: Geunyeong Yu, Jaekyun Moon
- **PDF**: https://ieeexplore.ieee.org/document/6804931
- **Abstract**: Two concatenated coding schemes based on fixed-rate Raptor codes are proposed for error control in NAND flash memory. One is geared for off-line recovery of uncorrectable pages and the other is designed for page error correction during the normal read mode. Both proposed coding strategies assume hard-decision decoding of the inner code with inner decoding failure generating erasure symbols for the outer Raptor code. Raptor codes allow low-complexity decoding of very long codewords while providing capacity-approaching performance for erasure channels. For the off-line page recovery scheme, one whole NAND block forms a Raptor codeword with each inner codeword typically made up of several Raptor symbols. An efficient look-up-table strategy is devised for Raptor encoding and decoding which avoids using large buffers in the controller despite the substantial size of the Raptor code employed. The potential performance benefit of the proposed scheme is evaluated in terms of the probability of block recovery conditioned on the presence of uncorrectable pages. In the suggested page-error-correction strategy, on the other hand, a hard-decision-iterating product code is used as the inner code. The specific product code employed in this work is based on row-column concatenation with multiple intersecting bits to allow the use of longer component codes. In this setting the collection of bits captured within each intersection of the row-column codes acts as the Raptor symbol(s), and the intersections of failed row codes and column codes are declared as erasures. The error rate analysis indicates that the proposed concatenation provides a considerable performance boost relative to the existing error correcting system based on long Bose-Chauduri-Hocquenghem (BCH) codes.

## Fast Blind Recognition of Channel Codes

- **ID**: ieee:6816517
- **Type**: journal
- **Published**: May 2014
- **Authors**: Reza Moosavi, Erik G. Larsson
- **PDF**: https://ieeexplore.ieee.org/document/6816517
- **Abstract**: We present a fast algorithm that, for a given input sequence and a linear channel code, computes the syndrome posterior probability (SPP) of the code, i.e., the probability that all parity check relations of the code are satisfied. According to this algorithm, the SPP can be computed blindly, i.e., given the soft information on a received sequence we can compute the SPP for the code without first decoding the bits. We show that the proposed scheme is efficient by investigating its computational complexity. We then consider two scenarios where our proposed SPP algorithm can be used. The first scenario is when we are interested in finding out whether a certain code was used to encode a data stream. We formulate a statistical hypothesis test and we investigate its performance. We also compare the performance of our scheme with that of an existing scheme. The second scenario deals with how we can use the algorithm for reducing the computational complexity of a blind decoding process. We propose a heuristic sequential statistical hypotheses test to use the fact that in real applications, the data arrives sequentially, and we investigate its performance using system simulations.

## Threshold-Based One-Bit Soft Forwarding for a Network Coded Multi-Source Single-Relay System

- **ID**: ieee:6783947
- **Type**: journal
- **Published**: May 2014
- **Authors**: Jun Li, Zihuai Lin, Branka Vucetic +3
- **PDF**: https://ieeexplore.ieee.org/document/6783947
- **Abstract**: In this paper, we propose a threshold-based one-bit soft forwarding (TOB-SF) protocol for a multi-source relaying system with network coding, where two sources communicate with the destination with the help of a relay. Specifically in the TOB-SF protocol, the relay calculates the log-likelihood ratio (LLR) value of each network coded symbol, compares this LLR value with a pre-optimized threshold, and determines whether to transmit or keep silent. We are interested in optimizing the TOB-SF protocol in fading channels, and consider both the uncoded and low-density parity check coded systems. In the uncoded system, we first derive the bit error rate (BER) expressions at the destination, based on which, we derive the optimal threshold. Then we theoretically prove that the system can achieve the full diversity gain by using this threshold. Further, we optimize the power allocation at the relay to achieve a higher coding gain. In the coded system, we first optimize the LLR threshold. Then we develop a methodology to track the BER evolution at the destination by using Gaussian approximations. Based on the BER evolution, we further optimize the power allocation at the relay which minimizes the system BER. Simulation results show that the proposed TOB-SF protocol outperforms other conventional relaying protocols in terms of error performance.

## Fast Polar Decoders: Algorithm and Implementation

- **ID**: ieee:6804939
- **Type**: journal
- **Published**: May 2014
- **Authors**: Gabi Sarkis, Pascal Giard, Alexander Vardy +2
- **PDF**: https://ieeexplore.ieee.org/document/6804939
- **Abstract**: Polar codes provably achieve the symmetric capacity of a memoryless channel while having an explicit construction. The adoption of polar codes however, has been hampered by the low throughput of their decoding algorithm. This work aims to increase the throughput of polar decoding hardware by an order of magnitude relative to successive-cancellation decoders and is more than 8 times faster than the current fastest polar decoder. We present an algorithm, architecture, and FPGA implementation of a flexible, gigabit-per-second polar decoder.

## Low-Complexity Soft-Output Decoding of Polar Codes

- **ID**: ieee:6804940
- **Type**: journal
- **Published**: May 2014
- **Authors**: Ubaid U. Fayyaz, John R. Barry
- **PDF**: https://ieeexplore.ieee.org/document/6804940
- **Abstract**: The state-of-the-art soft-output decoder for polar codes is a message-passing algorithm based on belief propagation, which performs well at the cost of high processing and storage requirements. In this paper, we propose a low-complexity alternative for soft-output decoding of polar codes that offers better performance but with significantly reduced processing and storage requirements. In particular we show that the complexity of the proposed decoder is only 4% of the total complexity of the belief propagation decoder for a rate one-half polar code of dimension 4096 in the dicode channel, while achieving comparable error-rate performance. Furthermore, we show that the proposed decoder requires about 39% of the memory required by the belief propagation decoder for a block length of 32768.

## Performance Limits and Practical Decoding of Interleaved Reed-Solomon Polar Concatenated Codes

- **ID**: ieee:6816518
- **Type**: journal
- **Published**: May 2014
- **Authors**: Hessam Mahdavifar, Mostafa El-Khamy, Jungwon Lee +1
- **PDF**: https://ieeexplore.ieee.org/document/6816518
- **Abstract**: A scheme for concatenating the recently invented polar codes with non-binary MDS codes, as Reed-Solomon codes, is considered. By concatenating binary polar codes with interleaved Reed-Solomon codes, we prove that the proposed concatenation scheme captures the capacity-achieving property of polar codes, while having a significantly better error-decay rate. We show that for any ε > 0, and total frame length N, the parameters of the scheme can be set such that the frame error probability is less than 2-N1-ε, while the scheme is still capacity achieving. This improves upon 2-N0.5-ε, the frame error probability of Arikan's polar codes. The proposed concatenated polar codes and Arikan's polar codes are also compared for transmission over channels with erasure bursts. We provide a sufficient condition on the length of erasure burst which guarantees failure of the polar decoder. On the other hand, it is shown that the parameters of the concatenated polar code can be set in such a way that the capacity-achieving properties of polar codes are preserved. We also propose decoding algorithms for concatenated polar codes, which significantly improve the error-rate performance at finite block lengths while preserving the low decoding complexity.

## Optimal Detector for Multilevel NAND Flash Memory Channels with Intercell Interference

- **ID**: ieee:6804928
- **Type**: journal
- **Published**: May 2014
- **Authors**: Meysam Asadi, Xiujie Huang, Aleksandar Kavcic +1
- **PDF**: https://ieeexplore.ieee.org/document/6804928
- **Abstract**: In this paper we derive the optimal detector for multilevel cell (MLC) flash memory channels with intercell interference (ICI). We start with the MLC channel model proposed by Dong et al. and just slightly alter the model to guarantee mathematical tractability of the optimal detectors (maximum likelihood and maximum a-posteriori sequence and symbol detectors). The optimal detector is obtained by computing branch metrics using Fourier transforms of analytically computable characteristic functions (corresponding to likelihood functions). We derive the detectors for both simple one-dimensional (1D) channel models and more realistic page-orientated two-dimensional (2D) channel models. Simulation results show that the hard-output bit error rate (BER) performance matches some previously known detectors, but that the soft-output detector outperforms previously known detectors by 0.35 dB.

## Storing Sparse Messages in Networks of Neural Cliques

- **ID**: ieee:6658945
- **Type**: journal
- **Published**: May 2014
- **Authors**: Behrooz Kamary Aliabadi, Claude Berrou, Vincent Gripon +1
- **PDF**: https://ieeexplore.ieee.org/document/6658945
- **Abstract**: An extension to a recently introduced binary neural network is proposed to allow the storage of sparse messages, in large numbers and with high memory efficiency. This new network is justified both in biological and informational terms. The storage and retrieval rules are detailed and illustrated by various simulation results.

## Realizing Unequal Error Correction for nand Flash Memory at Minimal Read Latency Overhead

- **ID**: ieee:6803051
- **Type**: journal
- **Published**: May 2014
- **Authors**: Jiangpeng Li, Kai Zhao, Jun Ma +1
- **PDF**: https://ieeexplore.ieee.org/document/6803051
- **Abstract**: In nand Flash memory, all pages have the same storage capacity and hence accommodate the same amount of redundancy in support of error correction. In current practice, user data in all the pages are protected by the same error correction code. However, different types of pages in multibit per cell memory have largely different bit error rates, for which appropriate unequal error correction can achieve a better utilization of memory redundancy and hence improve program/erase (P/E) cycling endurance. Nevertheless, a straightforward realization of unequal error correction suffers from severe memory read latency penalty. This brief presents a design strategy to implement unequal error correction through concatenated coding, which can well match the unequal error rates among different types of pages at minimal memory read latency penalty. Based on measurement results from commercial sub-22-nm 2 bits/cell nand Flash memory chips, we carried out simulations from both the coding and storage system perspectives, and the results show that this design strategy can improve the P/E cycling endurance by 20% and only incur less than 7% increase of storage system read response time at the end of Flash memory lifetime with the P/E cycling of around 1800.

## Optimal rate-distortion based unequal error protection in the transmission electrocardiograph signal

- **ID**: ieee:6845613
- **Type**: conference
- **Published**: 8-9 May 20
- **Authors**: Minglu Fan, Jie Cai, Liang Dong +2
- **PDF**: https://ieeexplore.ieee.org/document/6845613
- **Abstract**: In this paper, we are using rate-distortion optimized embedded (RED) technology to extract relatively more important and less important bits of different electrocardiograph (ECG) signals, which are protected by different rates of low-density parity-check (LDPC) codes to realize unequal error protected (UEP) performance. The UEP performance will be reflected by comparing experiment results that under different AWGN channel, then observing the distortion of reconstruction signal.

## Reduction of encoding delay in compression of binary sources using turbo codes: A two-stage algorithm

- **ID**: ieee:6842493
- **Type**: conference
- **Published**: 7-8 May 20
- **Authors**: Javad Haghighat, Fabrice Labeau, David V. Plant
- **PDF**: https://ieeexplore.ieee.org/document/6842493
- **Abstract**: An iterative algorithm is presented in the literature, to losslessly compress binary sources by using turbo codes. This algorithm searches for the smallest codeword length to guarantee zero distortion; and offers promising compression rates at the expense of large encoding delays. In this work we propose an improved encoding algorithm that works in two stages. At the first stage we estimate the codeword length. The estimated length does not guarantee zero distortion; however, we set a criterion to make sure that the distortion is below a defined threshold. At the second stage we improve our estimation to remove the remaining distortion and achieve lossless compression. Our simulations show that by careful choice of parameters: (i) our proposed algorithm achieves the same average compression rate as the algorithm appearing in the literature, and (ii) the delay introduced by our proposed algorithm, which is the sum of delays introduced by first and second stages, is less than the delay introduced by the algorithm appearing in the literature.

## Optimizing GNSS navigation data message decoding in urban environment

- **ID**: ieee:6851419
- **Type**: conference
- **Published**: 5-8 May 20
- **Authors**: Marion Roudier, Thomas Grelier, Lionel Ries +5
- **PDF**: https://ieeexplore.ieee.org/document/6851419
- **Abstract**: Nowadays, the majority of new GNSS applications targets dynamic users in urban environments; therefore the decoder input in GNSS receivers needs to be adapted to the urban propagation channel to avoid mismatched decoding when using soft input channel decoding. The aim of this paper consists thus in showing that the GNSS signals demodulation performance is significantly improved integrating an advanced soft detection function as decoder input in urban areas. This advanced detection function takes into account some a priori information on the available Channel State Information (CSI). If no CSI is available, one has to blindly adapt the detection function in order to operate close to the perfect CSI case. This will lead to avoid mismatched decoding due to, for example, the consideration by default of the Additive White Gaussian Noise (AWGN) channel for the derivation of soft inputs to be fed to soft input decoders. As a consequence the decoding performance will be improved in urban areas. The expressions of the soft decoder input function adapted for an urban environment is highly dependent on the available CSI at the receiver end. Based on different model of urban propagation channels, several CSI contexts will be considered namely perfect CSI, partial statistical CSI and no CSI. Simulation results will be given related to the GPS L1C demodulation performance with these different advanced detection function expressions in an urban environment. The results presented in this paper are valid for any kind of soft input decoders, such as Viterbi decoding for trellis based codes, the MAP/BCJR decoding for turbo-codes and the Belief Propagation decoding for LDPC codes.

## Authentication technology using QZSS

- **ID**: ieee:6851394
- **Type**: conference
- **Published**: 5-8 May 20
- **Authors**: Koichi Chino, Dinesh Manandhar, Ryosuke Shibasaki
- **PDF**: https://ieeexplore.ieee.org/document/6851394
- **Abstract**: We address in this paper about authentication of QZSS L1C/A signal using QZSS L1SAIF signal by developing an anti-spoofing methodology. The methodology is based on transmitting a signature data embedded into L1SAIF navigation message. The signature data is generated by using a part of L1C/A navigation message to generate Reference Authentication NAV Data (RAND). The RAND data is further encoded by LDPC based on a H-matrix. The LDPC encoded data is called signature data and is formatted to make it compatible with L1SAIF navigation message structure. This data is broadcasted from QZSS L1SAIF with a new message ID for authentication purpose. The receiver receives this message and decodes the authentication message into RAND and LDPC parity bits. Based on the information of RAND, the receiver gets corresponding H-matrix and other data from Authentication Data Center (ADC). These data from ADC is used to perform LDPC encoding to received RAND data. If the parity bits from this encoding are the same as the parity bits received by the receiver from L1SAIF signal are the same, it is concluded that the signals (L1C/A and L1SAIF) are authentic. Since, this method is based on using L1C/A navigation message for RAND and L1SAIF for broadcasting the signature data, it can also be implemented to other satellite systems like GPS L1C/A, MSAS, EGNOS and GAGAN.

## Polar Codes for Low-Complexity Forward Error Correction in Optical Access Networks

- **ID**: ieee:6839983
- **Type**: conference
- **Published**: 5-6 May 20
- **Authors**: Zifeng Wu, Berthold Lankl
- **PDF**: https://ieeexplore.ieee.org/document/6839983
- **Abstract**: Optical communication systems operating at high data rates require forward error correction (FEC) to achieve reliable communication at improved power efficiency. However, telecommunications equipment in optical access networks can only accommodate restricted hardware complexity. In this contribution we study Polar codes, a recently proposed class of error-correcting codes with advantageous properties in terms of their structure, complexity and design method. We investigate if Polar codes can compete with existing ITU G.975.1 standard FEC schemes and identify the challenges which need to be tackled when implementing hardware decoders.

## Flexible non-binary LDPC decoding on FPGAs

- **ID**: ieee:6853936
- **Type**: conference
- **Published**: 4-9 May 20
- **Authors**: Joao Andrade, Gabriel Falcao, Vitor Silva +1
- **PDF**: https://ieeexplore.ieee.org/document/6853936
- **Abstract**: Despite their ability to reach within the channel capacity in shorter codeblock lengths, non-binary LDPC codes have a higher decoding complexity that poses non-trivial barriers to their generalized adoption at algorithmic and compute-intensive levels. In this work, we propose a programmable FFT-SPA decoder that delivers high decoding throughput at low power consumptions, while retaining a design flexibility at the system level which surpasses typical VLSI descriptions, guaranteeing quick retargeting and prototyping of variants of this family of signal processing algorithms with effective decoding throughputs of up to 1 Mbit/s and potential throughputs of dozens of Mbit/s.

## A high throughput LDPC decoder using a mid-range GPU

- **ID**: ieee:6855061
- **Type**: conference
- **Published**: 4-9 May 20
- **Authors**: Xie Wen, Jiao Xianjun, Pekka Jääskeläinen +4
- **PDF**: https://ieeexplore.ieee.org/document/6855061
- **Abstract**: A standard-throughput-approaching LDPC decoder has been implemented on a mid-range GPU in this paper. Turbo-Decoding Message-Passing algorithm is applied to achieve high throughput. Different from traditional host managed multi-streams to hide host-device transfer delay, we use kernel maintained data transfer scheme to achieve implicit data transfer between host memory and device shared memory, which eliminates an intermediate stage of global memory. Data type optimization, memory accessing optimization, and low complexity Soft-In Soft-Out algorithm are also used to improve efficiency. Through these optimization methods, the 802.11n LDPC decoder on NVIDIA GTX480 GPU, which is released in 2010 with Fermi architecture, has achieved a high throughput of 295Mb/s when decoding 512 codewords simultaneously, which is close to highest bit rate 300Mb/s with 20MHz bandwidth in 802.11n standard. Decoding 1024 and 4096 codewords achieve 330 and 365Mb/s. A 802.16e LDPC decoder is also implemented, 374Mb/s (512 codewords), 435Mb/s (1024 codewords) and 507Mb/s (4096 codewords) throughputs have been achieved.

## Joint detection and decoding of LDPC coded distributed space-time signaling in wireless relay networks via linear programming

- **ID**: ieee:6853930
- **Type**: conference
- **Published**: 4-9 May 20
- **Authors**: Kun Wang, Wenhao Wu, Zhi Ding
- **PDF**: https://ieeexplore.ieee.org/document/6853930
- **Abstract**: We develop a linear programming based approach for the joint detection and decoding of LDPC coded distributed space-time signaling transmitted in a wireless relay network. Traditional receivers typically decouple the detection and decoding processes as two separate blocks or require iterative turbo exchange of extrinsic information between the soft detector and decoder. We exploit the constraints imposed on the channel input signals and jointly consider the training symbols as well as the LDPC code information by formulating a unified linear programming (LP) receiver. Moreover, in consideration of the vast amount of LDPC parity check inequalities, we present an adaptive procedure to significantly reduce the complexity of the proposed LP receiver.

## Asymptotic analysis and design of LDPC codes for laurent-based optimal and suboptimal CPM receivers

- **ID**: ieee:6854408
- **Type**: conference
- **Published**: 4-9 May 20
- **Authors**: Tarik Benaddi, Charly Poulliat, Marie-Laure Boucheret +2
- **PDF**: https://ieeexplore.ieee.org/document/6854408
- **Abstract**: In this paper, we derive an asymptotic analysis for a capacity approaching design of serially concatenated turbo schemes with low density parity check (LDPC) codes and continuous phase modulation (CPM) based on Laurent decomposition. The proposed design is based on extrinsic mutual information evolution and Gaussian approximation. By inserting partial interleavers between LDPC and CPM and allowing degree-1 variable nodes under a certain constraint we show that designed rates are very close to the maximum achievable rates. Furthermore, we discuss the selection of low complexity receivers that works with the same optimized profiles.

## Parallel programming of a symmetric transport-triggered architecture with applications in flexible LDPC encoding

- **ID**: ieee:6855236
- **Type**: conference
- **Published**: 4-9 May 20
- **Authors**: Blaine Rister, Pekka Jääskeläinen, Olli Silvén +2
- **PDF**: https://ieeexplore.ieee.org/document/6855236
- **Abstract**: Exposed-datapath architectures yield small, low-power processors that trade instruction word length for aggressive compile-time scheduling and a high degree of instruction-level parallelism. In this paper, we present a general-purpose parallel accelerator consisting of a main processor and eight symmetric clusters, all in a single core. Use of a lightweight and memory-efficient application programming interface allows for the first high-performance program executing both sequential and data-parallel code on the same TTA processor. We use the processor for LDPC encoding, a popular method of forward error correction. Demonstrating the flexibility of software-defined radio, we benchmark the processor with two programs, one which can handle almost any sort of LDPC code, and another which is optimized for a specific standard. We achieve a throughput of 5 Mb/s with the flexible program and 92 Mb/s with the standard-specific one, while consuming only 95 mW at a clock frequency of 1175 MHz.

## Metric learning with rank and sparsity constraints

- **ID**: ieee:6853550
- **Type**: conference
- **Published**: 4-9 May 20
- **Authors**: Bubacarr Bah, Stephen Becker, Volkan Cevher +1
- **PDF**: https://ieeexplore.ieee.org/document/6853550
- **Abstract**: Choosing a distance preserving measure or metric is fundamental to many signal processing algorithms, such as k-means, nearest neighbor searches, hashing, and compressive sensing. In virtually all these applications, the efficiency of the signal processing algorithm depends on how fast we can evaluate the learned metric. Moreover, storing the chosen metric can create space bottlenecks in high dimensional signal processing problems. As a result, we consider data dependent metric learning with rank as well as sparsity constraints. We propose a new non-convex algorithm and empirically demonstrate its performance on various datasets; a side benefit is that it is also much faster than existing approaches. The added sparsity constraints significantly improve the speed of multiplying with the learned metrics without sacrificing their quality.

## A fast architecture for finding maximum (or minimum) values in a set

- **ID**: ieee:6855071
- **Type**: conference
- **Published**: 4-9 May 20
- **Authors**: Andrea Dario Giancarlo Biroli, Juan Chi Wang
- **PDF**: https://ieeexplore.ieee.org/document/6855071
- **Abstract**: High speed architectures for extracting the best (maximum or minimum) values in a given set and their positions is of high importance in many signal processing applications. For example, the search of the two minimum values is an important part in iterative channel decoders for turbo and low-density-parity-check codes. In this paper, a new architecture is proposed to find the gth best value in an unsorted list of k elements, where the ranking position g can be any integer between 1 and k. The architecture can also be used to find in the assigned set a generic subset of the largest or smallest values. The proposed solution is particularly efficient in terms of hardware complexity and latency when the cardinality of the assigned set k is large and the values are represented on a reduced number of bits n. Synthesis results obtained with a 90-nm CMOS standard cell technology are provided for specific choices of g, k and n. Moreover, the nice properties of regularity and scalability of the proposed architecture are exploited to develop a QCA (quantum cellular automata) based implementation, which achieves lower power consumption or higher speed.

## FER prediction with variable codeword length

- **ID**: ieee:6853935
- **Type**: conference
- **Published**: 4-9 May 20
- **Authors**: Alberto Rico-Alvariño, Robert W. Heath, Carlos Mosquera
- **PDF**: https://ieeexplore.ieee.org/document/6853935
- **Abstract**: Frame error rate (FER) prediction in wireless communication systems is an important tool with applications to system level simulations and link adaptation, among others. Although in realistic communication scenarios it is expected to have codewords of different lengths, previous work on FER prediction marginally treated the dependency of the FER on the codeword length. In this paper, we present a method to estimate the FER using codewords of different length. We derive a low complexity FER estimator for frames of different length transmitted over a binary symmetric channel of unknown error probability. We extend this technique to coded systems by the use of effective SNR FER predictors. The proposed estimation scheme is shown to outperform other simpler estimation methods.

## LDPC coded transmissions over the Gaussian broadcast channel with confidential messages

- **ID**: ieee:6845079
- **Type**: conference
- **Published**: 4-7 May 20
- **Authors**: Marco Baldi, Nicola Maturo, Giacomo Ricciutelli +1
- **PDF**: https://ieeexplore.ieee.org/document/6845079
- **Abstract**: We design and assess some practical low-density parity-check (LDPC) coded transmission schemes for the Gaussian broadcast channel with confidential messages (BCC). This channel model is different from the classical wiretap channel model as the unauthorized receiver (Eve) must be able to decode some part of the information. Hence, the reliability and security targets are different from those of the wiretap channel. In order to design and assess practical coding schemes, we use the error rate as a metric of the performance achieved by the authorized receiver (Bob) and the unauthorized receiver (Eve). We study the system feasibility, and show that two different levels of protection against noise are required on the public and the secret messages. This can be achieved in two ways: i) by using LDPC codes with unequal error protection (UEP) of the transmitted information bits or ii) by using two classical non-UEP LDPC codes with different rates. We compare these two approaches and show that, for the considered examples, the solution exploiting UEP LDPC codes is more efficient than that using non-UEP LDPC codes.

## Performance analysis of MC-CDMA system when image transmission is involved

- **ID**: ieee:6866742
- **Type**: conference
- **Published**: 29-31 May 
- **Authors**: Razvan Craciunescu, Carmen Voicu, Alexandru Vulpe +1
- **PDF**: https://ieeexplore.ieee.org/document/6866742
- **Abstract**: Multi-Carrier Code Division Multiple Access (MC-CDMA) is a multiple access technique that inherits the features of both OFDM and CDMA. The current paper proposes an evaluation of MC-CDMA performances when image transmission is involved. The performances are evaluated both in terms of BER vs SNR and in terms of image quality metrics.

## Two-bit representation of the extrinsic LLR messages in the variable node processor of NB-LDPC decoder

- **ID**: ieee:6991185
- **Type**: conference
- **Published**: 29 April-1
- **Authors**: Ali Chamas Al Ghouwayel, Hussein Sharafeddin, Hussein Hijazi +1
- **PDF**: https://ieeexplore.ieee.org/document/6991185
- **Abstract**: This paper investigates a 2-bit binary representation of the reliability messages generated by the Variable Node (VN) processor of Non-Binary Low Density Parity Check (NB-LDPC) Decoder. The NB-LDPC family of error correcting codes, considered as a potential alternative to both binary LDPC and convolutional Turbo Codes, suffers from high computational complexity as well as large memory requirements. In order to reduce temporary storage requirements for extrinsic LLR messages, we propose a coding technique based on the 2-bit representation of the Log-Likelihood Ratio (LLR) messages generated locally in the VN processors. This simplified representation facilitates a size reduction of VN processor memory by 33% of the total memory size of extrinsic LLR messages. Monte Carlo simulations show that the 2-bit representation scheme has a negligible impact on the code performance.

## Decoding of short non-binary LDPC codes using a non iterative decoding algorithm

- **ID**: ieee:6991187
- **Type**: conference
- **Published**: 29 April-1
- **Authors**: Mahmoud El Kobi, Mohamad Zein, Ali Chamas Al Ghouwayel +1
- **PDF**: https://ieeexplore.ieee.org/document/6991187
- **Abstract**: In this paper, we investigate the decoding of short Non-Binary (NB)-LDPC codes of rate 1/2 using a non-iterative approach based on the Maximum-Likelihood (ML) principle. The traditional decoding algorithms used to decode the NB-LDPC codes are by nature iterative where the Variables Nodes (VN) and Check Nodes (CN) exchange data iteratively during, at least, eight iterations which imposes a long decoding time to achieve good performance in terms of Frame Error Rate (FER). In this paper we propose a decoding algorithm based on the Maximum Likelihood (ML) search named Near ML approach where the number of tested words considered as potential codewords is highly reduced. Simulation of codes of lengths 16 and 48 are presented and the results show that the proposed algorithm achieves the performance offered by the EMS algorithm. The NB-LDPC of length 16 is shown to outperform the EMS algorithm.

## An efficient component-interleaved nonbinary Low Density Parity Check Code scheme on Rayleigh fading channels

- **ID**: ieee:6849016
- **Type**: conference
- **Published**: 27-30 May 
- **Authors**: Zhanji Wu, Yongtao Shi, Xiang Chen +1
- **PDF**: https://ieeexplore.ieee.org/document/6849016
- **Abstract**: An efficient component-interleaved nonbinary Low Density Parity Check Code (LDPC) scheme is proposed, which can significantly outperform the binary LDPC codes scheme without a component interleaver on fading channels. In this paper, the bit-error-rate (BER) performances of nonbinary LDPC codes are compared with the binary LDPC codes on the independent Rayleigh fading channel. And then we use a fast decoding algorithm to reduce the complexity of nonbinary LDPC decoding, so that the nonbinary LDPC codes scheme becomes more practical. Besides, the influence of a component interleaver on the performance of nonbinary LDPC codes is also analyzed. Simulation results prove that nonbinary LDPC codes significantly outperform the binary LDPC codes, especially for low code rate and high order Galois field, which is up to 1.5dB. The component interleaver also can obviously improve the performance of nonbinary LDPC codes on fading channels, which is up to 0.3 dB.

## Asymptotic and finite-length performance of irregular spatially-coupled codes

- **ID**: ieee:6849017
- **Type**: conference
- **Published**: 27-30 May 
- **Authors**: Reza A. Ashrafi, Abdullah Sarıduman, Ali E. Pusane
- **PDF**: https://ieeexplore.ieee.org/document/6849017
- **Abstract**: The newest family of low-density parity-check (LDPC) codes, spatially-coupled (SC) codes, is shown to have several desirable characteristics including low implementation complexity and close-to-optimal performance over a range of channels. Furthermore, because of their ribbon-shaped parity-check matrices, window decoding can be used to decode these codes, which leads to low-delay implementations. Researchers have focused on asymptotically regular SC code ensembles and have examined several aspects of the code construction processes. In this paper, we concentrate on irregular SC code ensembles. We evaluate their decoding thresholds over the binary erasure channel and show that their performance is better than their regular SC counterparts. It is also shown that the gap between asymptotic coding thresholds of irregular SC ensembles and the fundamental Shannon limit gets negligibly small. For the sake of a better comparison, we have also evaluated the finite-length error performance of selected regular and irregular SC codes over the additive white Gaussian channel and it is also observed that finite-length error performance of these irregular SC codes outperforms regular SC codes. To further improve the error performance of these codes and to lower the possible error floors, progressive edge growth algorithm has also been considered in the finite-length performance analysis.

## Communication through collisions: Opportunistic utilization of past receptions

- **ID**: ieee:6848202
- **Type**: conference
- **Published**: 27 April-2
- **Authors**: Alireza Vahid, Mohammad Ali Maddah-Ali, A. Salman Avestimehr
- **PDF**: https://ieeexplore.ieee.org/document/6848202
- **Abstract**: When several wireless users are sharing the spectrum, packet collision is a simple, yet widely used model for interference. Under this model, when transmitters cause interference at any of the receivers, their collided packets are discarded and need to be retransmitted. However, in reality, that receiver can still store its analog received signal and utilize it for decoding the packets in the future (for example, by successive interference cancellation techniques). In this work, we propose a physical layer model for wireless packet networks that allows for such flexibility at the receivers. We assume that the transmitters will be aware of the state of the channel (i.e. when and where collisions occur, or an unintended receiver overhears the signal) with some delay, and propose several coding opportunities that can be utilized by the transmitters to exploit the available signal at the receivers for interference management (as opposed to discarding them). We analyze the achievable throughput of our strategy in a canonical interference channel with two transmitter-receiver pairs, and demonstrate the gain over conventional schemes. By deriving an outer-bound, we also prove the optimality of our scheme for the corresponding model.

## Scheduling of multicast and unicast services under limited feedback by using rateless codes

- **ID**: ieee:6848104
- **Type**: conference
- **Published**: 27 April-2
- **Authors**: Yin Sun, C. Emre Koksal, Kyu-Han Kim +1
- **PDF**: https://ieeexplore.ieee.org/document/6848104
- **Abstract**: Many opportunistic scheduling techniques are impractical because they require accurate channel state information (CSI) at the transmitter. In this paper, we investigate the scheduling of unicast and multicast services in a downlink network with a very limited amount of feedback information. Specifically, unicast users send imperfect (or no) CSI and infrequent acknowledgements (ACKs) to a base station, and multicast users only report infrequent ACKs to avoid feedback implosion. We consider the use of physical-layer rateless codes, which not only combats channel uncertainty, but also reduces the overhead of ACK feedback. A joint scheduling and power allocation scheme is developed to realize multiuser diversity gain for unicast service and multicast gain for multicast service. We prove that our scheme achieves a near-optimal throughput region. Our simulation results show that our scheme significantly improves the network throughput over schemes employing fixed-rate codes or using only unicast communications.

## Iterative receiver for Qc-LDPC coded underwater acoustic communication systems

- **ID**: ieee:6859617
- **Type**: conference
- **Published**: 26-30 May 
- **Authors**: Liang Zhao
- **PDF**: https://ieeexplore.ieee.org/document/6859617
- **Abstract**: Quasi Cyclic-Low Density Parity Check (QC-LDPC) codes are easy to construct and provide the considerable coding gain, which is suitable for underwater acoustic communication (UWAC). Single-carrier (SC) transmission with frequency-domain equalization (FDE) is today recognized as an attractive alternative to orthogonal frequency-division multiplexing (OFDM) for communication application with the inter-symbol interference (ISI) caused by multi-path propagation, especially in shallow water channel. In this paper, the turbo theory is applied on the QC-LDPC codes and minimum mean square error (MMSE) decision feedback equalizer (DFE) to design iterative data processing for underwater acoustic communication system. In the proposed iterative structure, the MMSE based FD-DFE and QC-LDPC decoder exchange soft information through an iterative manner so that the performance of underwater acoustic communication system can be improved greatly. Based on sound speed profiles (SSP) measured in the lake and finite-element ray tracking method, the shallow water channel is constructed to verify the validity of the proposed system structure.

## Software simulation of LDPC codes and performance analysis

- **ID**: ieee:6859553
- **Type**: conference
- **Published**: 26-30 May 
- **Authors**: C. Sandu, I. Florescu, C. Rotaru
- **PDF**: https://ieeexplore.ieee.org/document/6859553
- **Abstract**: In this paper we will analyze the influence of using Low Density Parity Check LDPC codes in different channels environment. The performances of LDPC codes are estimated in several scenarios. The simulation software gives us the possibilities to choose between different communications channels according to the encoding matrix used. Also we can adjust a number of parameters, thing that help to find the optimal solution depending on the decoding error rate or Bit Error Ratio (BER). Optimal combinations between parameters, the encoding matrix and structures design are obtained, related to required performance or Signal Noise Ratio (SNR) ranges. The sets of parameters and criteria introduced are discussed as the simulation results, also.

## Implementation of LDPC decoder for L1 signaling in DVB-T2 transmission frame

- **ID**: ieee:6904098
- **Type**: conference
- **Published**: 26-28 May 
- **Authors**: Shingchern D. You, Shun-Jie Huang
- **PDF**: https://ieeexplore.ieee.org/document/6904098
- **Abstract**: The L1 signaling part of the DVB-T2 system uses punctured low-density parity check (LDPC) codes. This paper provides some implementation details regarding decoding punctured LDPC codes. The implemented program can successfully decode digitalized DVB-T2 signal from a generator.

## A new hybrid decoding algorithm based on multi-dimensional searching for regular LDPC codes in finite geometries

- **ID**: ieee:6999766
- **Type**: conference
- **Published**: 20-22 May 
- **Authors**: Ehsan Olyaei Torshizi, Hossein Sharifi, Azadeh Daneshgar +1
- **PDF**: https://ieeexplore.ieee.org/document/6999766
- **Abstract**: In this paper, a new fast convergence hybrid decoding algorithm based on multi-dimensional searhing is proposed for decoding LDPC codes. The main idea of this algorithm is flipping variable multi bits in each iteration, change in which leads to the syndrome vector with least hamming weight. To this end, the algorithm does multidimensional searching between all possible bit positions that could flip in each iteration to select the best choices. Simulation results illustrate that the proposed algorithm converge significantly faster and have reduction in iteration number and also have excellent performance but with little performance difference than the robust Sum-Product algorithm.

## A concatenated scheme to improve the performance of polar codes on symmetric memoryless channels

- **ID**: ieee:6999836
- **Type**: conference
- **Published**: 20-22 May 
- **Authors**: Pirouz Majdolashrafi, Hamid Saeedi
- **PDF**: https://ieeexplore.ieee.org/document/6999836
- **Abstract**: The performance of Polar codes has been proved to achieve the Shannon capacity when N, the block length, tends to infinity. However, finite block length performance of Polar codes is rather poor compared to other capacity approaching codes such as LDPC (Low-Density Parity-Check) codes. In this paper, we propose a concatenated scheme with a polar code as an inner code and a Reed-Solomon code as an outer code to improve the performance over the binary erasure channel. Since the error pattern at the output of the polar decoder is not uniform, it is necessary to carefully devise an interleaver to map those bits with higher error probability to certain symbols of the Reed-Solomon code. To use the proposed scheme on other symmetric channels, one has to redesign the polar code component using density evolution technique which may not be practical. We therefore use a simplified scheme where the design is achieved using the erasure channel code design. We then show that the proposed concatenated scheme outperforms polar codes as well as Spatially-Coupled LDPC codes of the same rate and block length on symmetric channels.

## Both transmitter and receiver IQ imbalance compensation and CFO synchronization for LDPC-coded MIMO-OFDM systems using OSTBC algorithms

- **ID**: ieee:6999749
- **Type**: conference
- **Published**: 20-22 May 
- **Authors**: Mohamad Hossein Moghaddam, Ghasem Assarzade
- **PDF**: https://ieeexplore.ieee.org/document/6999749
- **Abstract**: MIMO OFDM is a very promising technique for highspeed wireless transmission. Implementation of MIMO-OFDM systems suffers from impairments such as carrier frequency offset (CFO) due to the Doppler effect and, in-phase and quadrature-phase (IQ) imbalances due to analog processing of the radio frequency signal at both transmitter and receiver. CFO could affect the orthogonality between subcarriers and ruining system performance. On the other hand the IQ imbalance degrades the achievable SNR and restricts the desired data rate. In this paper, the effect of both CFO-STO impairment and IQ imbalance distortion in a LDPC-coded MIMO-OFDM system is studied and a set of simulations is done for such a system considering CFO-STO synchronization and IQ imbalance compensation according to OSTBC algorithms.

## A Low-Latency Algorithm and FPGA Design for the Min-Search of LDPC Decoders

- **ID**: ieee:6969398
- **Type**: conference
- **Published**: 19-23 May 
- **Authors**: Georgios Tzimpragos, Christoforos Kachris, Dimitrios Soudris +1
- **PDF**: https://ieeexplore.ieee.org/document/6969398
- **Abstract**: The problem of finding efficiently the first k minimum or maximum values is generally met in many application fields, such as error control coding. More specifically, optimized solutions for the selection of the two or three smallest elements out of a given set of numbers are greatly needed for the design of high-speed Low-Density Parity-Check (LDPC) decoders, as this min-search can be the bottleneck. This paper aims to tackle current limitations by proposing a novel algorithm for solving this problem, where the searching is based on scanning from the most significant bit (MSB) to the least significant bit (LSB) of each input data. A design mapped to reconfigurable logic and a software tool for the automatic generation of synthesizable VHDL codes, implementing such low-latency components are presented as well. Experimental results show that compared to existing solutions, the proposed scheme achieves an up to 42% reduction in latency even at worst case. Since the hardware unit is repeatedly used in the LDPC decoder design, the described high-speed approach is strongly recommended.

## Advanced error prediction LDPC for high-speed reliable TLC nand-based SSDs

- **ID**: ieee:6849375
- **Type**: conference
- **Published**: 18-21 May 
- **Authors**: Tsukasa Tokutomi, Shuhei Tanakamaru, Tomoko Ogura Iwasaki +1
- **PDF**: https://ieeexplore.ieee.org/document/6849375
- **Abstract**: Highly reliable solid-state drives (SSDs) with triple-level-cell (TLC) NAND flash and Advanced Error-Prediction Low-Density Parity-Check (AEP-LDPC) are proposed. To increase NAND flash's capacity, bits/cell have been doubled and tripled, which causes reliability to drastically degrade due to narrower VTH margins. Previously proposed Error-Prediction LDPC (EP-LDPC) error-correcting code (ECC) improved reliability for Multi-Level-Cell (MLC) NAND flash [4]. However, in EP-LDPC program disturb is not modeled, so precision is limited, especially in short data retention <; 2 days. Here, AEP-LDPC is proposed for TLC NAND flash. By considering effects of program disturb, data retention and floating-gate capacitive coupling, the most accurate SSDs can be realized, with high speed read capability. The SSD's data-retention time increases by more than 12x, decode iterations decrease 57% and acceptable TLC NAND BER increases by more than 2.8 ×.

## Iterative Decoding of Network Coding HARQ in LDPC System

- **ID**: ieee:7022961
- **Type**: conference
- **Published**: 18-21 May 
- **Authors**: Yue Wu, L. A. Olawoyin, Hongwen Yang
- **PDF**: https://ieeexplore.ieee.org/document/7022961
- **Abstract**: This paper proposes an iterative decoding algorithm for network coding HARQ (NC-HARQ) retransmission scheme in LDPC system. Including two erroneous codewords and one retransmitted network coded word, a larger Tanner graph is applied in the decoding algorithm. We modify the process of iterative decoding and separate the external information into two parts which come from channel coding and network coding respectively. Different iteration numbers are set in these two parts and a weighting factor is multiplied to the latter one. Simulation results show that, compared with traditional HARQ in which the repeat codewords are the erroneous codewords themselves, the proposed scheme can not only reduce the retransmission number but also improve the throughput significantly.

## Detection and Decoding in Large-Scale MIMO Systems: A Non-Binary Belief Propagation Approach

- **ID**: ieee:7022876
- **Type**: conference
- **Published**: 18-21 May 
- **Authors**: T. Lakshmi Narasimhan, A. Chockalingam
- **PDF**: https://ieeexplore.ieee.org/document/7022876
- **Abstract**: In this paper, we propose a non-binary belief propagation approach (NB-BP) for detection of M-ary modulation symbols and decoding of q-ary LDPC codes in large-scale multiuser MIMO systems. We first propose a message passing based symbol detection algorithm which computes vector messages using a scalar Gaussian approximation of interference, which results in a total complexity of just O(KN √M), where K is the number of uplink users and N is the number of base station (BS) antennas. We then design optimized q-ary LDPC codes by matching the EXIT charts of the proposed detector and the LDPC decoder. Simulation results show that the proposed NB-BP detection-decoding approach using the optimized LDPC codes achieve significantly better performance (by about 1 dB to 7 dB at 10-5 coded BER for various system loading factors with number of users ranging from 16 to 128 and number of BS antennas fixed at 128) compared to using linear detectors and off-the-shelf q-ary irregular LDPC codes.

## Ultra fast, two-bit ECC for Emerging Memories

- **ID**: ieee:6849370
- **Type**: conference
- **Published**: 18-21 May 
- **Authors**: P. Amato, C. Laurent, M. Sforzin +3
- **PDF**: https://ieeexplore.ieee.org/document/6849370
- **Abstract**: Emerging Memories (EMs) could benefit from Error Correcting Codes (ECCs) able to correct a few errors in just a few nanoseconds; for example to cope with failure mechanisms that could arise in new storage physics. Fast ECCs are also desired for eXecuted-in-Place (XiP) and DRAM applications. This paper shows the key elements to implement a BCH code able to correct 2 errors in a page of 256 data bits in no more than 10ns with 180nm-CMOS logic, and with low energy consumption. The decoding time can be further reduced to few ns using smaller gate length logics. Moreover, the proposed solution is soundly rooted in BCH theory, and can be applied to any user data size. Basically the ideas are to avoid the division in the computation of the coefficients of the Error Locator Polynomial (ELP) of the BCH code, to optimize the implementation of the multiplication in the Galois Fields (GF) and to fully implement the decoder in a parallel combinatorial architecture. Such a BCH code has been embedded in a 45nm 1Gbit Phase Change Memory (PCM) device.

## Stopping a Rapid Tornado with a Puff

- **ID**: ieee:6956584
- **Type**: conference
- **Published**: 18-21 May 
- **Authors**: José Lopes, Nuno Neves
- **PDF**: https://ieeexplore.ieee.org/document/6956584
- **Abstract**: RaptorQ is the most advanced fountain code proposed so far. Its properties make it attractive for forward error correction (FEC), offering high reliability at low overheads (i.e., for a small amount of repair information) and efficient encoding and decoding operations. Since RaptorQ's emergence, it has already been standardized by the IETF, and there is the expectation that it will be adopted by several other standardization bodies, in areas related to digital media broadcast, cellular networks, and satellite communications. The paper describes a new attack on RaptorQ that breaks the near ideal FEC performance, by carefully choosing which packets are allowed to reach the receiver. Furthermore, the attack was extended to be performed over secure channels with IPsec/ESP. The paper also proposes a few solutions to protect the code from the attack, which could be easily integrated into the implementations.

## Evaluation of Cramer-Rao Bounds for Phase Estimation of Coded Linearly Modulated Signals

- **ID**: ieee:7022915
- **Type**: conference
- **Published**: 18-21 May 
- **Authors**: Nan Wu, Hua Wang, Hongjie Zhao +2
- **PDF**: https://ieeexplore.ieee.org/document/7022915
- **Abstract**: The evaluation of Cramer-Rao Bounds (CRBs) for phase estimation of coded linearly modulated signals are difficult due to the intractable expectations of the likelihood function with respect to coded symbols. In this paper, we propose two methods towards this end. The first one is a semi-analytical method for coded QPSK signals. Based on Gaussian approximation of extrinsic information, the expression of CRB is derived in terms of signal-to-noise ratio (SNR) and the mean of extrinsic information in closed form. For high-order modulations, e.g., 16QAM signal, we propose a numerical method based on multidimensional Gauss-Hermite Quadrature (GHQ). It is shown that, without suffering from the linearization error, the results of numerical method by GHQ outperform the semi-analytical results, and the former are consistent with that of the Monte Carlo simulations for systems with different codes and numbers of decoding iterations.

## Iterative Interference Modulation Classification

- **ID**: ieee:7022962
- **Type**: conference
- **Published**: 18-21 May 
- **Authors**: Yoojin Choi, Dongwoon Bai, Jungwon Lee +1
- **PDF**: https://ieeexplore.ieee.org/document/7022962
- **Abstract**: In the presence of co-channel interference in cellular networks, interference mitigation by detecting the desired signal jointly with the interference promises considerable gain over the conventional way of handling the interference as colored Gaussian. Even though such interference-aware detection can improve the performance, it requires some information on the interference. In particular, the modulation format of the interference has to be classified to this end, when it is not signaled by the network explicitly. This paper investigates interference modulation classification methods for interference-aware joint detection. We propose an iterative interference modulation classification algorithm that utilizes the decoded information of the desired signal in order to cancel the desired signal from the received signal. After the cancellation, the remaining signal can be treated as interference plus noise so that we can classify the modulation format of the interference at reduced complexity with small performance loss due to decoding errors.

## Link Adaptation Scheme for Uplink MIMO Transmission with Turbo Receivers

- **ID**: ieee:7022972
- **Type**: conference
- **Published**: 18-21 May 
- **Authors**: Yun Xue, Qiang Sun, Bin Jiang +1
- **PDF**: https://ieeexplore.ieee.org/document/7022972
- **Abstract**: In this paper, the turbo minimum mean square error- parallel interference cancelation (Turbo MMSE-PIC) receiver is incorporated with link adaptation schemes to achieve promising performance gains for uplink MIMO transmission, in parallel, adapt the link in the actual channel conditions with assist from performance prediction technology. We first predict the turbo receiver's performance as a basic metric for link adaptation scheme. Then, a new strategy of selecting the precoding matrices, the number of spatially multiplexed layers as well as modulation coding schemes are proposed, resulting in the proposed three-steps selection. In this method, the number of layers and modulation coding schemes to be feedback is initialized and used to set a shortened range of them. Then the number of layers is updated to take full advantage of iterative processing, instead of the initial value in the conventional strategy. In so doing, the benefit of turbo receivers is efficiently claimed while low computational complexity can be achieved.

## Artificial noise and LDPC code aided physical layer security enhancement

- **ID**: ieee:6913670
- **Type**: conference
- **Published**: 15-17 May 
- **Authors**: Zhiliang Yang, Yuanzhang Fan, Aihua Wang
- **PDF**: https://ieeexplore.ieee.org/document/6913670
- **Abstract**: Low density parity check (LDPC) code and artificial noise are combined in wiretap channel to enhance the security in physical layer. Artificial noise is added at the transmitter using pre-coding. The artificial noise is designed that it spans a null space at the legitimate receiver but acts as random interference at the eavesdropper receiver. Moreover, a scrambling matrix is designed and then used in LDPC code to enhance the physical layer security. The outage probability of the wiretap channel is deduced, and then used in outage probability minimization. The performance of the proposed scheme is demonstrated with simulations.

## The performance of LDPC coded frequency hopping system under follower jamming

- **ID**: ieee:6913666
- **Type**: conference
- **Published**: 15-17 May 
- **Authors**: Jingke Dai, Wenpu Guo, Donghui Xu
- **PDF**: https://ieeexplore.ieee.org/document/6913666
- **Abstract**: Follower jamming is a class of jamming way which is very harmful to the frequency hopping system. Low density parity check (LDPC) code is employed in frequency hopping system to combat follower jamming in this paper. The characteristics of follower jamming is introduced firstly, and then the model of LDPC coded FH system is built. The classical Progressive edge growth algorithm is used to construct the parity check matrix of LDPC code, and the sum-product algorithm is applied to obtain the optimum decoding performance. The simulation results show that the proposed system has outstanding anti-jamming capability, which is also compared with the traditional Reed-Solomon (RS) coded system.

## The performance of LDPC coded FFH/BFSK system over Rician fading channel under multitone jamming

- **ID**: ieee:6913657
- **Type**: conference
- **Published**: 15-17 May 
- **Authors**: Jingke Dai, Heng He, Donghui Xu +1
- **PDF**: https://ieeexplore.ieee.org/document/6913657
- **Abstract**: Fast frequency hopping (FFH) is a very effective way to combat jamming. In this paper, low density parity check (LDPC) code is employed to enhance the performance of FFH systems over a frequency-nonselective Rician fading channel under band multitone jamming (BMTJ). Moreover, maximum likelihood (ML) diversity combining and various robust diversity combining techniques which need partial or no side information (SI), are considered to improve the system capability of anti-jamming. Simulation results show that the proposed LDPC coded frequency hopping system provides excellent performance against band multitone jamming.

## A high rate non-binary QC-LDPC codes in high order Galois Field for PR2 and EPR2 channels

- **ID**: ieee:6839791
- **Type**: conference
- **Published**: 14-17 May 
- **Authors**: Mongkol Kupimai
- **PDF**: https://ieeexplore.ieee.org/document/6839791
- **Abstract**: In this paper, the new structure of high rate non-binary QC-LDPC codes based on the circulant permutation matrices is proposed. The construction of parity-check matrix of the proposed codes is obtained from (2, L) regular QC-LDPC codes. The parity-check matrix of the proposed codes has girth greater than 8. Simulation results over PR channels with the high order Galois Field show that the bit error rate and the symbol error rate performance of the proposed codes is better than those of the random non-binary LDPC codes, both in PR2 channel and EPR2 channel.

## A novel structure of variable rate non-binary LDPC codes for MIMO channels

- **ID**: ieee:6839769
- **Type**: conference
- **Published**: 14-17 May 
- **Authors**: Puripong Suthisopapan, Mongkol Kupimai, Virasit Imtawil +1
- **PDF**: https://ieeexplore.ieee.org/document/6839769
- **Abstract**: Slow decoding convergence and performance loss are two main drawbacks of the conventional variable rate non-binary LDPC codes based on puncturing. To alleviate these problems, we study in this paper the variable rate non-binary LDPC code that has a mother code of high rate and a series of lower rate codes obtained from the concept of shortening. A novel shortening technique to construct variable rate non-binary LDPC codes is proposed in this paper. By using this technique, the performance loss between variable rate code and independently-designed code, in MIMO channels, at any given rate no longer exists and the decoding convergence of the proposed scheme is very fast, e.g., only 5 iterations on average to achieve BER of 10−5. Moreover, the proposed shortening is done in symbol-wise manner (inherently low-complexity) which is more suitable for realistic MIMO communications.

## Low-complexity key reconciliation algorithm using LDPC bit-flipping decoding for quantum key distribution

- **ID**: ieee:6839886
- **Type**: conference
- **Published**: 14-17 May 
- **Authors**: Tharathorn Phromsa-ard, Paramin Sangwongngam, Keattisak Sripimanwat +3
- **PDF**: https://ieeexplore.ieee.org/document/6839886
- **Abstract**: Quantum key reconciliation is an essential process of quantum key distribution (QKD). It aims to correct the transmission errors after the distribution of quantum objects over a quantum channel, where two legitimate parties use a classical public authenticated channel to disclose correlated bits for agreeing on their common key. This work proposes an alternative promising method employing LDPC-codes bit-flipping decoding to practical implementation of quantum key reconciliation. In our proposed scheme, the low-complexity code bit-flipping decoding based on syndrome decoding is modified and applied to conventional Winnow protocol to achieve both error correcting performance and low complexity of hardware realization, i.e. FPGA logic cells and/or memory. From numerical simulation while the performance of our proposed scheme in terms of final bit error rate (BER) and disclosed bits is superior to conventional Winnow and CASCADE protocols, it yields low complexity in LDPC decoding comparable to the existing LDPC-based reconciliation protocols. Therefore, the technique is promising to high-speed discrete-variable QKD applications.

## Diversity Performance of Physical Layer Network Coding based on Reed-Solomon Codes

- **ID**: ieee:6843206
- **Type**: conference
- **Published**: 14-16 May 
- **Authors**: Dong Fang, Alister Burr
- **PDF**: https://ieeexplore.ieee.org/document/6843206
- **Abstract**: We propose a novel scheme for physical-layer network coding (PNC), constructed from linear block codes for multiple-user multiple-relay wireless networks. In the proposed design, each relay computes a linear combination of source symbols, namely, the network coded symbol (NCS) and forwards it to the destination. The destination collects all NCSs and the original source symbols to form a valid codeword of the linear code. The resulting codeword can be decoded to reliably extract the original source symbols. The numerical results show that our proposed design provides m-th order diversity when there are m relays. Moreover, the proposed design provides a significant sumrate enhancement over the orthogonal multiple access scheme with network coding described in previous literature.

## Design and Test of Adaptive Computing Fabrics for Scalable and High-Efficiency Cognitive SoC Applications

- **ID**: ieee:6875448
- **Type**: conference
- **Published**: 14-16 May 
- **Authors**: Pascal Nsame, Guy Bois, Yvon Savaria
- **PDF**: https://ieeexplore.ieee.org/document/6875448
- **Abstract**: In this paper, a new adaptive computing fabric (ACF) that achieves both real-time multi-mode/multi-rate adaptation and lower error floor for cognitive SoC applications is presented. The VLSI architecture of the ACF is experimentally shown to meet the DVB, 802.3an and 802.ad target specifications. Our design delivers a 10-14 bit error rate (BER) with a bit energyto- noise density of Eb/N0=5dB with an energy-efficiency of 0.61pJ/bit. Experiments are conducted comparing Low-Density Parity-Check (LDPC) codes error correction performance in the presence of unreliable circuits due to aggressive manufacturing defect rates and/or run-time defect rates from components enabled by SoC integration. We report on a 201.6Gbps 65nm CMOS design and Xilinx FPGA prototype, which demonstrates in hardware how real-time adaptive techniques can accelerate decoding convergence and lower the error floor. Finally, We show experimentally that our ACF design can achieve energyefficiency throughput speed-ups at scale in the range of 200x to 5000x as compared to the same algorithm running in software (optimized C program) on a single CPU core.

## Mitigating Constant Jamming in Cognitive Radio Networks Using Hybrid FEC Code

- **ID**: ieee:6838733
- **Type**: conference
- **Published**: 13-16 May 
- **Authors**: Victor Balogun, Axel Krings
- **PDF**: https://ieeexplore.ieee.org/document/6838733
- **Abstract**: The task of detecting and mitigating Cognitive Radios (CRs) operating as constant jammers in a Cognitive Radio network (CRN) can be very daunting. The CR constant jammers prey on the adaptable functionalities of CRN so as to cause serious denial of service to the users of the network. In addition, these jammers are capable of introducing value faults in pathological cases as a result of being able to manipulate transmitted data. In previous research, we have investigated the performance of CRNs operating in the presence of jamming attacks that are capable of introducing value faults. The results obtained show that CR constant jammers are very effective in their operations and they are capable of bringing down the entire CRN when their jamming rate is just about 30%. In this paper, we show that none of the existing anti-jamming solutions are able to mitigate CR jammers that are capable of manipulating communicated data. As a result, we propose a hybrid forward error correction (FEC) code that incorporates data integrity checking into an efficient forward error correction mechanism. The approach uses data redundancy to remove the need for retransmission of lost or detected manipulated data caused by jamming attacks by exploring the recovery block component of the proposed solution. We present the algorithm for our proposed solution and evaluate its performance through simulation. The result of our analysis using suitable performance metrics shows that the solution is very efficient and robust against the different rates of jamming perpetrated by constant jammers.

## Space-time storage codes for wireless distributed storage systems

- **ID**: ieee:6934407
- **Type**: conference
- **Published**: 11-14 May 
- **Authors**: Camilla Hollanti, David Karpuk, Amaro Barreal +1
- **PDF**: https://ieeexplore.ieee.org/document/6934407
- **Abstract**: Distributed storage systems (DSSs) have gained a lot of interest recently, thanks to their robustness and scalability compared to single-device storage. Majority of the related research has exclusively concerned the network layer. At the same time, the number of users of, e.g., peer-to-peer (p2p) and device-to-device (d2d) networks as well as proximity based services is growing rapidly, and the mobility of users is considered more and more important. This motivates, in contrast to the existing literature, the study of the physical layer functionality of wireless distributed storage systems. In this paper, we take the first step towards protecting the storage repair transmissions from physical layer errors when the transmission takes place over a fading channel. To this end, we introduce the notion of a space-time storage code, drawing together the aspects of network layer and physical layer functionality and resulting in cross-layer robustness. It is also pointed out that existing space-time codes are too complex to be utilized in storage networks when the number of helpers involved is larger than the number of receive antennas at the newcomer or data collector, hence creating a call for less complex transmission protocols.
