# IEEE Xplore — 2016-09


## An Encoder with Speed over 40Gbps for RC LDPC Codes with Rates up to 0.96

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10855823
- **Type**: journal
- **Published**: September 
- **Authors**: Zhiyong He, Qiang Zhao, Hushan Xu +2
- **PDF**: https://ieeexplore.ieee.org/document/10855823
- **Abstract**: We propose a class of Rate-compatible (RC) Low-density parity-check (LDPC) codes with a very wide range of code rates. To widen the range of rates, we have developed an optimal transmission scheme to push the upper bound of code rates to 0.96. Characterized by a parity check matrix in a dual-diagonal form, the proposed RC LDPC code can be encoded in linear time. Constructed from shifted identity sub-matrices, the proposed codes are particularly well-suited for the high-speed implementation of parallel encoders. Furthermore, the encoder can be implemented efficiently with several left circular shifters and XOR gates. To maximize the encoding speed, we have proposed a $\boldsymbol{q}-\mathbf{parallel}$ encoder architecture, where $\boldsymbol{q}$ is the size of each sub-matrix. The implementation results into Field programmable gate array (FPGA) devices indicate that a 12-parallel encoder for the proposed RC LDPC code with a code rate from 0.5 to 0.96 is capable of reaching a speed of 42 Gigabits per second (Gbps) using a clock frequency of 300MHz.

## Euclidean Geometry-Based Spatially Coupled LDPC Codes for Storage

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7553579
- **Type**: journal
- **Published**: Sept. 2016
- **Authors**: Yixuan Xie, Lei Yang, Peng Kang +1
- **PDF**: https://ieeexplore.ieee.org/document/7553579
- **Abstract**: In this paper, we construct binary spatially coupled (SC) low-density parity-check (LDPC) codes based on Euclidean geometry (EG) LDPC codes for storage applications, where high error correction capability, extremely low uncorrectable bit error rate (UBER), and low decoding complexity are required. We propose a systematic way to construct the families of SC LDPC codes from (m,2s) EG LDPC codes, which are termed EG-SC LDPC codes. In the construction method, we propose a 2-D edge-spreading process to construct the base matrix of EG-SC LDPC codes, which consists of matrix unwrapping and periodically time-varying of a protograph. A lower bound on the rank of the parity-check matrix of an EG-SC LDPC code is derived. We evaluate the error rate performance of the constructed EG-SC LDPC codes by using a weighted bit-flipping decoding algorithm for its low decoding complexity. Numerical results show that the UBER performance of the constructed EG-SC LDPC codes is superior to that of their EG LDPC code counterparts, and show no error floor compared with the constructed protograph SC LDPC codes and regular LDPC codes.

## Strategies for Reducing Decoding Cycles in Stochastic LDPC Decoders

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7419905
- **Type**: journal
- **Published**: Sept. 2016
- **Authors**: Di Wu, Yun Chen, Qichen Zhang +2
- **PDF**: https://ieeexplore.ieee.org/document/7419905
- **Abstract**: This brief presents three strategies, including initialization based on Look Up Table (LUT), postprocessing based on bit flipping and hard decision based on the posterior information, to reduce the number of decoding cycles (DCs) for stochastic low-density parity-check decoding. For the standard IEEE 802.3an code, simulation indicates a 73.6% reduction in the average number of DCs with a satisfactory bit error rate. Moreover, hardware implementation shows that the area required for the proposed decoder is significantly reduced.

## An Efficient Decoder Architecture for Nonbinary LDPC Codes With Extended Min-Sum Algorithm

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7419880
- **Type**: journal
- **Published**: Sept. 2016
- **Authors**: Chia-Lung Lin, Shu-Wen Tu, Chih-Lung Chen +2
- **PDF**: https://ieeexplore.ieee.org/document/7419880
- **Abstract**: Nonbinary low-density-parity-check (NB-LDPC) codes, an extension of binary LDPC codes, provide stronger error-correcting capability than binary LDPC codes. However, the performance gain comes together with extraordinary increase on decoding complexity and memory requirement. Many simplification algorithms have been proposed in the literature, and the extended min-sum (EMS) algorithm is the one with minimal performance loss. In this brief, we present an efficient decoder architecture for quasi-cyclic NB-LDPC codes with the EMS algorithm. The throughput is improved by not only the double-throughput elementary check node unit but also overlapped processing for both check node and variable node units (VNUs). To reduce memory usage and computing complexity, edge-message hiding and simplified VNU are proposed as well. With these schemes, the postlayout results of a decoder for a (112, 56) NB-LDPC over GF(64) are presented. The core area occupies 2.24 mm2 and consumes 274 mW with a throughput of 124.6 Mb/s. Compared to prior NB-LDPC decoders with a similar code rate, the proposed decoder achieves better hardware efficiency and energy efficiency.

## A General Non-Binary LDPC Code Optimization Framework Suitable for Dense Flash Memory and Magnetic Storage

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7553518
- **Type**: journal
- **Published**: Sept. 2016
- **Authors**: Ahmed Hareedy, Chinmayi Lanka, Lara Dolecek
- **PDF**: https://ieeexplore.ieee.org/document/7553518
- **Abstract**: Transmission channels underlying modern dense storage systems, e.g., Flash memory and magnetic recording (MR) systems, significantly differ from canonical channels, like additive white Gaussian noise (AWGN) channels. While existing low-density parity-check (LDPC) codes optimized for symmetric, AWGN-like channels are being actively considered for Flash applications, we demonstrate that, due to channel asymmetry, such approaches are inadequate. We introduce a refined definition of absorbing sets, which we call general absorbing sets of type two (GASTs), and study the combinatorial properties of GASTs. We then present the weight consistency matrix (WCM), which succinctly captures key properties in a GAST. Furthermore, we show how to customize the WCM definition such that it suits other special subclasses of GASTs. Based on these new concepts, we then develop a new, general combinatorial code optimization framework, which we call the WCM framework, and demonstrate its effectiveness on the realistic highly-asymmetric normal-Laplace mixture (NLM) Flash channel. Moreover, we show that our framework can be customized to optimize non-binary LDPC (NB-LDPC) codes for other asymmetric channels, channels with memory (incorporated in MR systems), and canonical symmetric channels. For all the channels we have simulated NB-LDPC codes over, the codes optimized using the WCM framework enjoy at least 1 order, and up to nearly 2 orders of magnitude performance gain in the uncorrectable bit error rate (UBER) or the frame error rate (FER) relative to the unoptimized codes. Our simulations also show that codes optimized for symmetric channels are not the best choice for asymmetric channels.

## LDPC Decoding Mappings That Maximize Mutual Information

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7553561
- **Type**: journal
- **Published**: Sept. 2016
- **Authors**: Francisco Javier Cuadros Romero, Brian M. Kurkoski
- **PDF**: https://ieeexplore.ieee.org/document/7553561
- **Abstract**: For low-density parity-check (LDPC) codes widely used in NAND flash memories, the bit-error rate performance is closely tied to the number of bits per message used by the message-passing decoder. This paper describes a technique to generate message-passing decoding mapping functions for LDPC codes using 3 and 4 bits per message. These maps are not derived from belief-propagation decoding or one of its approximations, instead, the maps are based on a channel quantizer that maximizes mutual information. More precisely, the construction technique is a systematic method, which uses an optimal quantizer at each step of density evolution to generate message-passing decoding mappings. Numerical results show, for high-rate codes suitable for flash memories, that 4 bits per message and a few iterations (10-20 iterations) are sufficient to approach full belief-propagation decoding, less than 5-7 bits per message typically needed. The construction technique is flexible, since it can generate maps for arbitrary number of bits per message, and can be applied to arbitrary memoryless channels.

## Nonbinary Quasi-Regular QC-LDPC Codes Derived From Cycle Codes

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7497526
- **Type**: journal
- **Published**: Sept. 2016
- **Authors**: Wojciech Sułek
- **PDF**: https://ieeexplore.ieee.org/document/7497526
- **Abstract**: Nonbinary ultra sparse codes, particularly regular cycle codes, are known to approach Shannon-limit performance as the Galois field GF(q) order is sufficiently large. Good cycle codes can result from a class of algebraically defined graphs called cages. Meanwhile, when smaller q is desirable, the cycle codes are outperformed by quasi-regular codes. In this letter, we propose a code construction method that takes a cage as a starting point and then progressively inserts a few additional edges into the graph. The edge insertion is terminated as soon as the code performance stops improving. Our simulation results show that the obtained quasi-regular codes outperform cyclic codes for fields up to GF(64) and its performance is slightly better than the quasi-regular improved-Progressive Edge Growth-based codes. The proposed algorithm preserves the block-circulant structure of the initial cage-based graph; therefore, it can be used for structured or quasi-cyclic codes design.

## Exhaustive Enumeration of Elementary Trapping Sets of an Arbitrary Tanner Graph

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7506265
- **Type**: journal
- **Published**: Sept. 2016
- **Authors**: Hossein Falsafain, Sayyed Rasoul Mousavi
- **PDF**: https://ieeexplore.ieee.org/document/7506265
- **Abstract**: An effective branch-and-bound (B&B) algorithm for exhaustively enumerating the elementary trapping sets (ETSs) in an arbitrary given Tanner graph is described. Given a Tanner graph G and a positive integer ν, we introduce a novel 0-1 integer linear programming (ILP) formulation of the NP-hard problem of finding the minimum ω for which there exists an (ω, ν)-ETS in G. The B&B procedure is then based on the LP relaxation of this 0-1 ILP formulation. Our novel 0-1 ILP description of the problem yields a strong (tight) LP relaxation, which allows the search space to be pruned very effectively, as confirmed by experimental results. An obvious advantage of the proposed approach is that it does not require the input Tanner graph to be of a particular form (e.g., variable-regular).

## Design of Spatially Coupled LDPC Codes Over GF $(q)$ for Windowed Decoding

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7469375
- **Type**: journal
- **Published**: Sept. 2016
- **Authors**: Lai Wei, David G. M. Mitchell, Thomas E. Fuja +1
- **PDF**: https://ieeexplore.ieee.org/document/7469375
- **Abstract**: In this paper, we study spatially coupled lowdensity parity-check (SC-LDPC) codes over finite fields GF(q), q ≥ 2, and develop design rules for q-ary SC-LDPC code ensembles based on their iterative belief propagation decoding thresholds, with particular emphasis on low-latency windowed decoding (WD). We consider transmission over both the binary erasure channel (BEC) and the binary-input additive white Gaussian noise channel (BIAWGNC) and present results for a variety of (J, K)-regular SC-LDPC code ensembles constructed over GF(q) using protographs. Thresholds are calculated using the protograph versions of q-ary density evolution (for the BEC) and the q-ary extrinsic information transfer analysis (for the BIAWGNC). We show that the WD of q-ary SC-LDPC codes provides significant threshold gains compared with corresponding (uncoupled) q-ary LDPC block code (LDPC-BC) ensembles when the window size W is large enough and that these gains increase as the finite-field size q = 2m increases. Moreover, we demonstrate that the new design rules provide WD thresholds that are close to capacity, even when both m and W are relatively small (thereby reducing decoding complexity and latency). The analysis further shows that, compared with standard flooding-schedule decoding, the WD of q-ary SC-LDPC code ensembles results in significant reductions in both the decoding complexity and the decoding latency and that these reductions increase as m increases. For the applications with a near-threshold performance requirement and a constraint on decoding latency, we show that using q-ary SC-LDPC code ensembles, with moderate q > 2, instead of their binary counterparts results in reduced decoding complexity.

## Error Errore Eicitur: A Stochastic Resonance Paradigm for Reliable Storage of Information on Unreliable Media

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7509624
- **Type**: journal
- **Published**: Sept. 2016
- **Authors**: Predrag Ivaniš, Bane Vasić
- **PDF**: https://ieeexplore.ieee.org/document/7509624
- **Abstract**: We give an architecture of a storage system consisting of a storage medium made of unreliable memory elements and an error correction circuit made of a combination of noisy and noiseless logic gates that is capable of retaining the stored information with the lower probability of error than a storage system with a correction circuit made completely of noiseless logic gates. Our correction circuit is based on the iterative decoding of low-density parity check codes, and uses the positive effect of errors in logic gates to correct errors in memory elements. In the spirit of Marcus Tullius Cicero's Clavus clavo eicitur (one nail drives out another), the proposed storage system operates on the principle: error errore eicitur-one error drives out another. The randomness that is present in the logic gates makes these classes of decoders superior to their noiseless counterparts. Moreover, random perturbations do not require any additional computational resources as they are inherent to unreliable hardware itself. To utilize the benefits of logic gate failures, our correction circuit relies on two key novelties: a mixture of reliable and unreliable gates and decoder rewinding. We present a method based on absorbing Markov chains for the probability of error analysis, and explain how the randomness in the variable and check node update function helps a decoder to escape to local minima associated with trapping sets.

## Spatially Concatenated Channel-Network Code for Underwater Wireless Sensor Networks

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7518674
- **Type**: journal
- **Published**: Sept. 2016
- **Authors**: Zafar Iqbal, Heung-No Lee
- **PDF**: https://ieeexplore.ieee.org/document/7518674
- **Abstract**: Underwater environment monitoring is an important application of wireless sensor networks (WSNs). However, WSNs face challenges, such as erroneous communication, ensuring the lifetime and robustness of the network, and cost constraints. The underwater acoustic channel (UAC) is highly frequency-selective, and the channel response changes over time because of variations in the channel conditions. Therefore, designing a cooperative coded orthogonal frequency division multiplexing (COFDM) system that is suitable for the doubly selective UAC and has reduced power consumption is very challenging. We propose a cooperative spatial-domain coding scheme combined with the low-density parity-check-coded OFDM system, called spatially concatenated channel-network code, for underwater acoustic WSNs. The designed underwater acoustic WSN exhibits a significant advantage regarding the required number of sensors, bit error rate (BER), and power consumption over the non-cooperative COFDM communication system. We also analyze sensor deployment schemes and find out the area in which our proposed scheme can be beneficial in terms of reduced power consumption and enhanced BER.

## Multi-Class Source-Channel Coding

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7506294
- **Type**: journal
- **Published**: Sept. 2016
- **Authors**: Irina E. Bocharova, Albert Guillén i Fàbregas, Boris D. Kudryashov +3
- **PDF**: https://ieeexplore.ieee.org/document/7506294
- **Abstract**: This paper studies an almost-lossless source-channel coding scheme in which source messages are assigned to different classes and encoded with a channel code that depends on the class index. The code performance is analyzed by means of random-coding error exponents and validated by simulation of a low-complexity implementation using existing source and channel codes. While each class code can be seen as a concatenation of a source code and a channel code, the overall performance improves on that of separate source-channel coding and approaches that of joint source-channel coding when the number of classes increases.

## A Soft Input Decoding Algorithm for Generalized Concatenated Codes

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7509654
- **Type**: journal
- **Published**: Sept. 2016
- **Authors**: Jens Spinner, Jürgen Freudenberger, Sergo Shavgulidze
- **PDF**: https://ieeexplore.ieee.org/document/7509654
- **Abstract**: This paper proposes a soft input decoding algorithm and a decoder architecture for generalized concatenated (GC) codes. The GC codes are constructed from inner nested binary Bose-Chaudhuri-Hocquenghem (BCH) codes and outer Reed-Solomon codes. In order to enable soft input decoding for the inner BCH block codes, a sequential stack decoding algorithm is used. Ordinary stack decoding of binary block codes requires the complete trellis of the code. In this paper, a representation of the block codes based on the trellises of supercodes is proposed in order to reduce the memory requirements for the representation of the BCH codes. This enables an efficient hardware implementation. The results for the decoding performance of the overall GC code are presented. Furthermore, a hardware architecture of the GC decoder is proposed. The proposed decoder is well suited for applications that require very low residual error rates.

## Lossless and Reversible Data Hiding in Encrypted Images With Public-Key Cryptography

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7107988
- **Type**: journal
- **Published**: Sept. 2016
- **Authors**: Xinpeng Zhang, Jing Long, Zichi Wang +1
- **PDF**: https://ieeexplore.ieee.org/document/7107988
- **Abstract**: This paper proposes lossless, reversible, and combined data hiding schemes for ciphertext images encrypted by public-key cryptosystems with probabilistic and homomorphic properties. In the lossless scheme, the ciphertext pixels are replaced with new values to embed the additional data into several least significant bit planes of ciphertext pixels by multilayer wet paper coding. Then, the embedded data can be directly extracted from the encrypted domain, and the data-embedding operation does not affect the decryption of original plaintext image. In the reversible scheme, a preprocessing is employed to shrink the image histogram before image encryption, so that the modification on encrypted images for data embedding will not cause any pixel oversaturation in plaintext domain. Although a slight distortion is introduced, the embedded data can be extracted and the original image can be recovered from the directly decrypted image. Due to the compatibility between the lossless and reversible schemes, the data-embedding operations in the two manners can be simultaneously performed in an encrypted image. With the combined technique, a receiver may extract a part of embedded data before decryption, and extract another part of embedded data and recover the original plaintext image after decryption.

## BER-Based Physical Layer Security With Finite Codelength: Combining Strong Converse and Error Amplification

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7513393
- **Type**: journal
- **Published**: Sept. 2016
- **Authors**: Il-Min Kim, Byoung-Hoon Kim, Joon Kui Ahn
- **PDF**: https://ieeexplore.ieee.org/document/7513393
- **Abstract**: A bit-error-rate (BER)-based physical layer security approach is proposed for the finite blocklengths. For secure communication in the sense of high BER, the information-theoretic strong converse is combined with cryptographic error amplification achieved by the substitution permutation networks based on the confusion and diffusion. For the discrete memoryless channels (DMCs), an analytical framework is provided showing the tradeoffs among the finite blocklength, the maximum/minimum possible transmission rates, and the BER requirements for the legitimate receiver and the eavesdropper. In addition, the security gap is analytically studied for the Gaussian channels and the concept is extended to other DMCs including the binary symmetric channels and binary erasure channels.

## Advantage of MAMR Read-Write Performance

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7471502
- **Type**: journal
- **Published**: Sept. 2016
- **Authors**: Ikuya Tagawa, Masato Shiimoto, Masato Matsubara +3
- **PDF**: https://ieeexplore.ieee.org/document/7471502
- **Abstract**: Microwave-assisted magnetic recording (MAMR) is one of the promising candidate technologies for next-generation hard disk drives. In MAMR, the high-frequency field from a spin-torque oscillator (STO) in the recording head is utilized to reduce the magnetization switching field of the medium. Micromagnetic modeling has shown the potential of MAMR; however, in terms of experimental results with actual heads and media, only little evidence of media magnetization reversal and improvement on overwrite has been reported. In this paper, we focus upon the experimental results of MAMR gain defined as a difference in the read-write performance when the STO is activated compared with when not activated. In conclusion, we show clear bit error rate improvement by activating the STO, giving an areal density increase of around 5-10% after considering the penalty associated with the magnetic core width increase. We also confirm that the magnetization switching in the STO is fast enough up to 2.3 GHz, and that there is no negative impact on the adjacent track interference nor on the far track interference.

## Block Markov Superposition Transmission of RUN Codes

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7539706
- **Type**: journal
- **Published**: Sept. 2016
- **Authors**: Chulong Liang, Xiao Ma, Baoming Bai
- **PDF**: https://ieeexplore.ieee.org/document/7539706
- **Abstract**: In this paper, we propose a simple procedure to construct (decodable) good codes with any given alphabet (of moderate size) for any given (rational) code rate to achieve any given target error performance (of interest) over additive white Gaussian noise channels. We start with constructing codes over groups for any given code rates. This can be done in an extremely simple way if we ignore the error performance requirement for the time being. Actually, this can be satisfied by repetition (R) codes and uncoded (UN) transmission along with time-sharing technique. The resulting codes are simply referred to as RUN codes for convenience. The encoding/decoding algorithms for RUN codes are almost trivial. In addition, the performance can be easily analyzed. It is not difficult to imagine that the RUN code usually performs far away from the corresponding Shannon limit. Fortunately, the performance can be improved as required by spatially coupling the RUN codes via block Markov superposition transmission (BMST), resulting in the BMST-RUN codes. Simulation results show that the BMST-RUN codes perform well (within around 1 dB away from Shannon limits) for a wide range of code rates and outperform the BMST with bit-interleaved coded modulation scheme.

## Signal Detection for MIMO SC-FDMA Systems Exploiting Block Circulant Channel Structure

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7286855
- **Type**: journal
- **Published**: Sept. 2016
- **Authors**: Dahoon Jeong, Jaekwon Kim
- **PDF**: https://ieeexplore.ieee.org/document/7286855
- **Abstract**: In this paper, we propose a novel receiver scheme for multiple-input-multiple-output (MIMO) single-carrier frequency-division multiple access (SC-FDMA) systems. Various optimal and near-optimal MIMO detection techniques developed for flat-fading channels are not readily applied to MIMO SC-FDMA systems due to the large dimensions of the effective channels. Recently, the system equation of single-input-single-output (SISO) SC-FDMA systems was divided into a number of disjoint subsystems with moderate dimensions, and a previous MIMO detection technique was applied to the subsystems. In this paper, instead of naively extending the previous scheme for SISO SC-FDMA to MIMO SC-FDMA systems, we first express the large system equation of MIMO SC-FDMA, such that the effective channels are block circulant for an arbitrary number of transmit and receive antennas. The block circulant channel structure is then exploited to lower the computational complexity of projections to construct nonoverlapping subsystems. The proposed circulant projection also takes advantage of the sparse channel structure, offering higher postprojection signal-to-noise ratios (SNRs) of the resulting subsystems than those of a naive projection that does not exploit the channel structure. The simulations confirm the desirable performance of the proposed scheme when a relatively small number of subcarriers are used. The proposed technique is also compared with the previous iterative block decision feedback equalization (IB-DFE) and minimum-mean-square-error-prewhitened-maximum-likelihood (MMSE-prewhitened-ML) detection techniques.

## Detector for MLC NAND Flash Memory Using Neighbor-A-Priori Information

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7407390
- **Type**: journal
- **Published**: Sept. 2016
- **Authors**: Chaudhry Adnan Aslam, Yong Liang Guan, Kui Cai
- **PDF**: https://ieeexplore.ieee.org/document/7407390
- **Abstract**: Cell-to-cell interference (CCI), arising from parasitic coupling-capacitance between adjacent cells, is a major factor for the degradation of cell threshold voltage in today's flash memory chips. In this paper, three novel postprocessing detection schemes that exploit the a priori information of neighboring/interfering cells for mitigating the CCI effect in multilevel cell NAND flash memory are presented. The proposed schemes are referred to as the Even-A-Priori (Even-AP), the All-A-Priori (All-AP), and the All-AP-coupling-capacitance ratio (CCR) detectors. The main idea is to remove the CCI component from the interfering cells before CCI cancellation from the victim cell. Specifically, the mean CCRs along the victim cell's vertical and diagonal directions are estimated to enable more accurate CCI cancellation. Performance analysis and simulation results show that the channel signal-to-noise ratio performance can be improved by up to 2 dB at a cell storage capacity of 1.8 bits/cell, which is significantly improved compared with some prior-art detection schemes.

## Turbo Equalization for Two Dimensional Magnetic Recording Using Voronoi Model Averaged Statistics

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7556284
- **Type**: journal
- **Published**: Sept. 2016
- **Authors**: Morteza Mehrnoush, Benjamin J. Belzer, Krishnamoorthy Sivakumar +1
- **PDF**: https://ieeexplore.ieee.org/document/7556284
- **Abstract**: This paper considers turbo equalization for 2-D magnetic recording. Magnetic grains are modeled as Voronoi regions of randomly distributed nuclei. Bits read from the magnetic grain model flow into a 2-D intersymbol interference (2D-ISI) model including additive white Gaussian noise. At high bit densities, some bits are not written on any grain, and hence are effectively “overwritten” by surrounding bits. The proposed system iteratively exchanges log-likelihood ratios (LLRs) between a 2D-ISI equalizer based on the forward-backward algorithm and an irregular repeat-accumulate (IRA) decoder. To combat bit overwrites, the system employs a non-linear function to map 2D-ISI extrinsic output LLRs to IRA decoder input LLRs. To pass back LLRs from the IRA decoder to the 2D-ISI equalizer, we design a simple likelihood-ratio-based LLR estimator. Simulations of the proposed system that employ the perturbed-bit-centers grain model proposed in a 2010 IEEE Transactions on Magnetics paper show a 6.5% increase in user bits per grain (U/G) and a 16.4 dB signal-to-noise ratio (SNR) gain compared with the previous paper, without iterative turbo equalization. Utilizing the LLR estimator to do iterative detection results in SNR gains of up to 1.7 dB compared with non-iterative detection. The random Voronoi model employed in this paper appears to be more difficult to equalize than the grain model in the 2010 paper. The proposed system with random Voronoi model achieves 0.4422 U/G at SNR =11.6 dB, i.e., about 8.8 Tb/in2 at (typically assumed future grain density) 20 Tgr/in2; this is almost ten times the density of current systems at 10 Tgr/in2.

## Capacity of the MLC NAND Flash Channel

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7553496
- **Type**: journal
- **Published**: Sept. 2016
- **Authors**: Thomas Parnell, Celestine Dünner, Thomas Mittelholzer +1
- **PDF**: https://ieeexplore.ieee.org/document/7553496
- **Abstract**: In this paper, we develop a framework for evaluating the symmetric capacity of multilevel-cell (MLC) NAND flash devices while making very few assumptions regarding the underlying device physics. A set of recursive equations are derived that allow one to measure the symmetric capacity for any given page in a flash device using simple conditional statistics that can be extracted experimentally. Using data captured from two different 1y nm MLC devices, we demonstrate that the symmetric capacity of a flash page not only depends on the amount of program/erase cycling and data retention stress that has accumulated, but also on the position of the page within the flash block. We then study the effect on symmetric capacity of using optimized read-back schemes (both hard and soft) and show that while there is significant benefit, not all pages in the block are improved by the same amount. Finally, we show that it is possible to design error correction architectures that harness the inherent variation of symmetric capacity within a flash block to dramatically extend the program/erase cycling endurance of flash-based storage systems.

## A Novel Design and Modeling of UEP-Based Compressed Video Broadcasting With Multilevel Coded Modulation

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7491279
- **Type**: journal
- **Published**: Sept. 2016
- **Authors**: Yoshito Watanabe, Hideki Ochiai
- **PDF**: https://ieeexplore.ieee.org/document/7491279
- **Abstract**: A novel coded modulation system design that maximizes the average quality of multimedia data, received by a given set of target users, is proposed for compressed video broadcasting based on unequal error protection. An integrated source and channel coding system with graceful degradation is introduced, where the multilevel coded modulation (MLC) with capacity-approaching codes is combined with an existing source compression technique. By assigning critical information that is required for decoding compressed data to the levels of MLC with higher reliability, we demonstrate that graceful degradation can be naturally incorporated into practical video broadcasting systems. Furthermore, a new measure of achievable average receiver quality, i.e., the quality of the received videos averaged over the users located within the coverage area of a given broadcasting service, is introduced. Based on the proposed measure, an optimal rate allocation algorithm for MLC, utilizing the code rate design based on channel capacity rule, is developed. In the case of MPEG-4 video coding, our numerical results reveal that a well-designed MLC system can achieve higher average quality experienced by target users than the conventional coded modulation as well as hierarchical modulation systems for a given coverage area.

## Extending the Routes of the Soft Information in Turbo Equalization for Bit-Patterned Media Recording

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7480408
- **Type**: journal
- **Published**: Sept. 2016
- **Authors**: Chi Dinh Nguyen, Jaejin Lee
- **PDF**: https://ieeexplore.ieee.org/document/7480408
- **Abstract**: This paper presents a new framework of turbo equalization (TE) to overcome 2-D intersymbol interference (2-D ISI) for bit-patterned media recording (BPMR). The BPMR has been developed for the next generation of hard disk drives aiming to extend storage density. One of the main challenges for the system is 2-D ISI, i.e., 1-D ISI from neighbor bits and intertrack interference from adjacent tracks. The conventional TE is the iterative process between an equalizer (or detector) and a decoder. We construct a new scheme of TE where the soft information from the decoder is fed back not only to the equalizer but, at the same time, also to the detector. The proposed scheme is to exploit full advantage of a priori information from the decoder. The results show that the proposed model is approximately 0.4 dB better than the conventional TE solution at 0% track misregistration.

## Minimal Maximum-Level Programming—Combined Cell Mapping and Coding for Faster MLC Memory

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7553436
- **Type**: journal
- **Published**: Sept. 2016
- **Authors**: Amit Berman, Yitzhak Birk
- **PDF**: https://ieeexplore.ieee.org/document/7553436
- **Abstract**: In multi-level-cell memory, such as flash and phase-change memory, shrinking cell size and the growing number of levels per cell worsen the access rate to capacity ratio and even reduce access rate. We present minimal maximum-level programming, a scheme for expediting cell programming by sharing physical cells among multiple data sectors and exploiting the fact that making moderate changes to a cell's charge level is faster than making large ones. In particular, we encode the data such that in the k th writing of data to a cell, only the lowest k+1 levels are utilized. Unlike in previously proposed cell-sharing schemes, different same-size data sectors occupy different numbers of physical cells, and a cell may hold a fraction of a bit of a given data sector. Nevertheless, the exposed sector size remains unchanged. Data are encoded, but without redundancy. In a four-level cell example, we achieve up to 75% reduction in write latency. Read latency may be degraded, depending on the percentage of utilized capacity.

## A secret key encryption scheme based on 1-level QC-LDPC lattices

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7736446
- **Type**: conference
- **Published**: 7-8 Sept. 
- **Authors**: Khadijeh Bagheri, Mohammad-Reza Sadeghi, Taraneh Eghlidos +1
- **PDF**: https://ieeexplore.ieee.org/document/7736446
- **Abstract**: We introduce a new secret-key cryptosystem based on 1-level QC-LDPC integer lattices. These lattices are practically implementable in high dimensions due to their low-complexity encoding and decoding algorithms. We exploit their efficient encoding and decoding algorithms to make a significant reduction in the complexity of lattice-based cryptosystems. Furthermore, the sparseness of the corresponding parity check matrix of 1-level QC-LDPC lattices and their good error performance, make them efficient choices in real world applications. In this paper, we propose a Rao-Nam like encryption scheme using 1-level QC-LDPC lattices. Some chosen-plaintext attacks and recent results on the Rao-Nam scheme are considered over the proposed scheme. Our scheme is secure against the chosen plaintext attack and it is efficient because of its high information rate and low overhead of the encryption and decryption algorithms.

## Improved minimum weight, girth, and ACE distributions in ensembles of short block length irregular LDPC codes constructed using PEG and cyclic PEG (CPEG) algorithms

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7593102
- **Type**: conference
- **Published**: 5-9 Sept. 
- **Authors**: Umar-Faruk Abdu-Aguye, Marcel Adrian Ambroze, Martin Tomlinson
- **PDF**: https://ieeexplore.ieee.org/document/7593102
- **Abstract**: In this paper we introduce a novel progressive edge-growth (PEG) algorithm, the cyclic PEG (CPEG) algorithm. The CPEG algorithm uses an alternative edge establishment sequence to construct low-density parity-check (LDPC) codes. Irregular LDPC codes constructed using the CPEG algorithm have improved girth and approximate cycle extrinsic message degree (ACE) compared to existing PEG algorithms. We also analyze the minimum codeword weight, minimum stopping set weight, local girth, and local ACE distributions for codes in four very large ensembles of irregular LDPC codes. The code ensembles analyzed were constructed using standard PEG, ACE modified standard PEG, CPEG, and ACE modified CPEG algorithms. Modifications to improve the ACE in PEG LDPC codes, by Xiao and Banihashemi, were implemented in the ‘ACE modified’ versions of the PEG algorithms. The ACE modified standard PEG algorithm constructed the code ensemble with the highest minimum codeword weight and minimum stopping set weight distributions, and the ACE modified CPEG algorithm constructed the code ensemble with the highest local girth and ACE distributions. Short block length irregular LDPC codes with good degree distributions which have higher minimum weights than have been published for similar LDPC codes were found in the four code ensembles.

## Improved PEG construction of large girth QC-LDPC codes

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7593094
- **Type**: conference
- **Published**: 5-9 Sept. 
- **Authors**: Madiagne Diouf, David Declercq, Marc Fossorier +2
- **PDF**: https://ieeexplore.ieee.org/document/7593094
- **Abstract**: In this paper, we present an improvement of the PEG algorithm for constructing quasi-cyclic low-density parity-check (QC-LDPC) codes with large girth. We introduce the concept of PEG-undetectable cycles on the computation tree in the PEG algorithm for QC-LDPC codes and give a predictive method to avoid these undetected cycles. The aim is to select only the candidates that ensure the maximization of local girth for a code of girth g ≥ 10 and thus avoid a posteriori verification after the creation of a new edge i.e. keep the predictive philosophy of the PEG algorithm. The proposed method is applicable to both regular and irregular codes and also protograph type-I codes. Simulation results are presented to demonstrate the efficiency of our method in terms of minimum circulant permutation matrix pmin and error performance.

## Structural analysis of array-based non-binary LDPC codes

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7593070
- **Type**: conference
- **Published**: 5-9 Sept. 
- **Authors**: Shancheng Zhao, Xiujie Huang, Xiao Ma
- **PDF**: https://ieeexplore.ieee.org/document/7593070
- **Abstract**: Motivated by the superior performance of array-based non-binary low-density parity-check (LDPC) codes, we study in this paper their structural properties by combinational and graphical techniques. The main results are summarized as follows. First, we show that there exist codewords with symbol weight six and seven in array-based non-binary LDPC (NBLDPC) codes with column weight 3. Second, we characterize the graphical substructures induced by weight-6 and weight-7 codewords. Finally, we carry out comparisons to confirm the performance advantage of array-based NBLDPC codes.

## A linear model for the iterative decoding of random LDPC codes in the high SNR region

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7593100
- **Type**: conference
- **Published**: 5-9 Sept. 
- **Authors**: Kuntal Deka, A. Rajesh, P. K. Bora
- **PDF**: https://ieeexplore.ieee.org/document/7593100
- **Abstract**: This paper presents a linear model for the sum-product decoding of random low-density parity-check (LDPC) codes, specifically in the high signal-to-noise ratio (SNR) region. The sum-product algorithm is first approximated as the min-sum algorithm and then a linear model is estimated for the latter. To formulate the model, the dominant trapping sets of the particular code are found. We consider a criterion based on the channel log-likelihood-ratio values to estimate the linear model. The bit error rate performance predicted by the linear model is compared with that obtained through importance sampling. This confirms that the linear model can accurately predict the performance of LDPC codes in the high SNR region.

## Multi-edge-type LDPC code concatenated with Trellis Shaping for PAR reduction

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7593114
- **Type**: conference
- **Published**: 5-9 Sept. 
- **Authors**: Abdul Wakeel, Werner Henkel
- **PDF**: https://ieeexplore.ieee.org/document/7593114
- **Abstract**: This manuscript addresses optimization of irregular Low-Density Parity-Check (LDPC) code concatenated with Trellis Shaping for Peak-to-Average Ratio (PAR) reduction in Orthogonal Frequency Division Multiplexing (OFDM) systems. It takes into account the different error probabilities inside a QAM constellation and from the decoding of the MSBs of the Trellis Shaping.

## NB-LDPC check node with pre-sorted input

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7593104
- **Type**: conference
- **Published**: 5-9 Sept. 
- **Authors**: Cédric Marchand, Emmanuel Boutillon
- **PDF**: https://ieeexplore.ieee.org/document/7593104
- **Abstract**: Non-binary low-density parity-check codes have better communication performance compared to their binary counterparts but they suffer from higher complexity, especially for the check node processing. In this paper a sorting of the input vectors based on a reliability criteria is performed prior to the check node processing. This presorting process allows the Extended Min-Sum (EMS) check node process to focus its effort mainly on the weakest inputs. Proof is given for a check node of degree 12 in GF(64) for the syndrome based algorithm with a number of computed syndromes reduced by a factor of four which directly impacts the check node complexity without performance degradation.

## Construction of high-rate QC-LDPC codes with multi-weight circulants

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7593069
- **Type**: conference
- **Published**: 5-9 Sept. 
- **Authors**: Xiaoning Wu, Ming Jiang, Chunming Zhao
- **PDF**: https://ieeexplore.ieee.org/document/7593069
- **Abstract**: In this paper, we propose a construction method of quasi-cyclic low-density parity-check (QC-LDPC) codes with multi-weight circulants (MQC-LDPC codes) which is suitable for high-rate LDPC codes with moderate length. MQC-LDPC codes can achieve better degree distributions, Hamming weight distributions, and stopping set weight distributions than conventional QC-LDPC codes with single-weight circulants (SQC-LDPC codes). Within the same framework, we generalize and simplify the error minimization progressive edge growth (EMPEG) algorithm for supporting the structure with multi-weight circulants. Simulation results show that the constructed MQC-LDPC codes offer better performance at both high and low signal to noise ratio (SNR) regions in additive white Gaussian noise (AWGN) channels than the conventional SQC-LDPC codes defined in 802.11ad and 802.16e.

## (3, L) quasi-cyclic LDPC codes: Simplified exhaustive search and designs

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7593119
- **Type**: conference
- **Published**: 5-9 Sept. 
- **Authors**: Cheng Sun, Hengzhou Xu, Dan Feng +1
- **PDF**: https://ieeexplore.ieee.org/document/7593119
- **Abstract**: There exist lots of (3, L)-regular quasi-cyclic (QC) LDPC codes constructed from finite fields, protographs, array codes, and computer search under some design rules. For a given code length and rate, how to select the best one from these codes is considerable. In this paper, we study (3, L)-regular QC LDPC codes from the perspective of graph isomorphism, and non-isomorphic (3, L)-regular QC LDPC codes are determined. By analyzing the cycle structures of the resulting non-isomorphic codes, an efficient algorithm for counting cycles is presented. Also proposed is a simplified exhaustive search of non-isomorphic (3, L)-regular QC LDPC codes free of cycles of length less than g0, where g0 is the estimated optimal girth value for a given code length. Based on these two algorithms, we can easily construct a (3, L)-regular QC LDPC code with optimized cycle distribution for a given L and code length. Numerical results show that the constructed codes have better performance under the iterative decoding algorithms.

## Comparison of different schedulings for the ADMM based LDPC decoding

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7593075
- **Type**: conference
- **Published**: 5-9 Sept. 
- **Authors**: Imen Debbabi, Bertrand Le Gal, Nadia Khouja +2
- **PDF**: https://ieeexplore.ieee.org/document/7593075
- **Abstract**: This paper proposes a general framework aiming at describing and comparing LDPC decoders based on the ADMM approach. ADMM is a linear programming decoding method. When applied on LDPC codes, it acts as an iterative message passing technique and enhances the error correction performance compared with the usual belief propagation based decoders. In this paper, three ADMM decoding algorithms classified according to their scheduling type are described and compared. Simulation results show that the layered scheduling is efficient to enhance the error correction performance while decreasing the average number of decoding iterations for the considered LDPC codes.

## Wrap-around sliding-window near-ML decoding of binary LDPC codes over the BEC

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7593068
- **Type**: conference
- **Published**: 5-9 Sept. 
- **Authors**: Irina E. Bocharova, Boris D. Kudryashov, Eirik Rosnes +2
- **PDF**: https://ieeexplore.ieee.org/document/7593068
- **Abstract**: A novel method of low-complexity near-maximum-likelihood (ML) decoding of quasi-cyclic (QC) low-density parity-check (LDPC) codes over the binary erasure channel is presented. The idea is similar to wrap-around decoding of tail-biting convolutional codes. ML decoding is applied to a relatively short window which is cyclically shifted along the received sequence. The procedure is repeated until either all erasures have been corrected, or no new erasures are corrected at a certain round. A new upper bound on the ensemble-average ML decoding error probability for a finite-length row-regular LDPC code family is derived and presented. Furthermore, a few examples of regular and irregular QC LDPC codes are studied by simulations and their performance is compared with the ensemble-average performance. Finally, the impact of the codeword weight and stopping set size spectra on the ML and belief-propagation decoding performance is discussed.

## Spatially Coupled LDPC codes affected by a single random burst of erasures

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7593098
- **Type**: conference
- **Published**: 5-9 Sept. 
- **Authors**: Vahid Aref, Narayanan Rengaswamy, Laurent Schmalen
- **PDF**: https://ieeexplore.ieee.org/document/7593098
- **Abstract**: Spatially-Coupled LDPC (SC-LDPC) ensembles achieve the capacity of binary memoryless channels (BMS), asymptotically, under belief-propagation (BP) decoding. In this paper, we study the BP decoding of these code ensembles over a BMS channel and in the presence of a single random burst of erasures. We show that in the limit of code length, codewords can be recovered successfully if the length of the burst is smaller than some maximum recoverable burst length. We observe that the maximum recoverable burst length is practically the same if the transmission takes place over binary erasure channel or over binary additive white Gaussian channel with the same capacity. Analyzing the stopping sets, we also estimate the decoding failure probability (the error floor) when the code length is finite.

## A new approach to optimise Non-Binary LDPC codes for coded modulations

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7593124
- **Type**: conference
- **Published**: 5-9 Sept. 
- **Authors**: Ahmed Abdmouleh, Emmanuel Boutillon, Laura Conde-Canencia +2
- **PDF**: https://ieeexplore.ieee.org/document/7593124
- **Abstract**: This paper is dedicated to the optimisation of Non-Binary LDPC codes when associated to high-order modulations. To be specific, we propose to specify the values of the non-zero NB-LDPC parity matrix coefficients depending on the corresponding check node equation and the Euclidean distance of the coded modulation. In other words, we explore the joint optimisation of the modulation mapping and the non-binary matrix. The performance gains announced by a theoretical analysis based on the Union Bound are confirmed by simulations results. We obtain an 0.2-dB gain in the high SNR regime compared to other state-of-the-art matrices.

## LDPC codes and iterative decoding over symbol-tuple error channels

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7593120
- **Type**: conference
- **Published**: 5-9 Sept. 
- **Authors**: Kenta Kasai, Masanori Hirotomo, Masakatu Morii
- **PDF**: https://ieeexplore.ieee.org/document/7593120
- **Abstract**: This paper deals with symbol-pair error channels. First, we generalize the channels to symbol-tuple error channels whose read length is D. Then, we derive a message passing algorithm for decoding LDPC codes over the generalized channels. Furthermore, we investigate the Hamming distance distributions of LDPC codes in terms of D symbol-tuple metric.

## Finite-length quasi-synchronous LDPC decoders

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7593130
- **Type**: conference
- **Published**: 5-9 Sept. 
- **Authors**: François Leduc-Primeau, Warren J. Gross
- **PDF**: https://ieeexplore.ieee.org/document/7593130
- **Abstract**: Quasi-synchronous systems aim to reduce energy consumption by allowing timing violations in a synchronous circuit, while performance guarantees are provided by analyzing the system with a suitable deviation model. This paper studies the performance of quasi-synchronous LDPC decoders for regular codes of finite length. We present an approach to accurately predict the decoding performance and energy consumption of the decoder for a specific average channel quality and maximum number of iterations. These analytical results are then compared with gate-level circuit simulations of a quasi-synchronous decoder.

## Universal rate-compatible LDPC code families for any increment ordering

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7593085
- **Type**: conference
- **Published**: 5-9 Sept. 
- **Authors**: Sudarsan V. S. Ranganathan, Kasra Vakilinia, Dariush Divsalar +1
- **PDF**: https://ieeexplore.ieee.org/document/7593085
- **Abstract**: Rate-compatible (RC) codes are at the core of systems with incremental redundancy. Usually, an RC code family supports successively lower code rates by sending specific increments of additional redundancy at each rate. That is, the order of the increments is fixed. However, in some multi-hop communication systems and also in recently proposed inter-frame coding, the order in which the decoder of the RC code receives the increments is not predetermined. A different ordering of the increments at the decoder may change the codes of various rates. This paper seeks RC codes that are universally good over all increment orderings. We call RC codes satisfying this requirement universal for any increment ordering (UIO) codes. We design protograph-based Raptor-like (PBRL) low-density parity-check (LDPC) code ensembles for UIO codes using protograph thresholds as components of two design metrics. One metric seeks codes that, at each code rate, have exactly the same frame error rate for all increment orderings. The other metric sacrifices strictly identical performance for every ordering to seek codes that achieve the best possible throughput in a variable-length setting with random increment ordering, as would occur with inter-frame coding. Simulation results of UIO-PBRL codes from the new ensembles show that our designs satisfy the two metrics.

## Design of robust, protograph based LDPC codes for rate-adaptation via probabilistic shaping

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7593076
- **Type**: conference
- **Published**: 5-9 Sept. 
- **Authors**: Fabian Steiner, Patrick Schulte
- **PDF**: https://ieeexplore.ieee.org/document/7593076
- **Abstract**: In this work, the design of robust, protograph-based low-density parity-check (LDPC) codes for rate-adaptive communication via probabilistic shaping is considered. Recently, probabilistic amplitude shaping (PAS) by Böcherer et al. has been introduced for capacity approaching and rate-adaptive communication with a bitwise-demapper and binary decoder. Previous work by the authors considered the optimization of protograph based LDPC codes for PAS and specific spectral efficiencies (SEs) to jointly optimize the LDPC code node degrees and the mapping of the coded bits to the bit-interleaved coded modulation (BICM) bit-channels. We show that these codes tend to perform poor when operated at other rates and propose the design of robust LDPC codes by employing a min-max approach in the search for good protograph ensembles via differential evolution. The considered design uses a single 16 amplitude-shift-keying (ASK) constellation and a robust 13/16 ≈ 0.813 rate LDPC code to operate between 0.7 to 2.7 bits per channel use. For a blocklength of 16 224 bits and a target frame error rate of 10-3 the proposed code operates within 1.32 dB of continuous AWGN capacity for 0.7 bpcu to 1.3 bpcu and within 1.05 dB for 1.3 bpcu to 2.7 bpcu.

## Increasing the rate of spatially-coupled codes via optimized irregular termination

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7593071
- **Type**: conference
- **Published**: 5-9 Sept. 
- **Authors**: Mohammad Reza Sanatkar, Henry D. Pfister
- **PDF**: https://ieeexplore.ieee.org/document/7593071
- **Abstract**: In this paper, we consider the rate-loss problem for spatially-coupled LDPC (SC-LDPC) codes on the binary erasure channel. Although SC-LDPC codes have good noise thresholds under belief-propagation (BP) decoding, they also suffer a rate-loss due to termination that is significant at moderate blocklengths. Our idea is to attach additional variable nodes at the boundary using an irregular degree distribution. Then, this degree distribution is optimized to improve the code rate without reducing the BP threshold. The optimization is formulated as an linear program and solved numerically. Our results show that the code rate can be increased by a reasonable amount without decreasing the BP threshold.

## Coding theory for robust computing: Models, tools, and applications

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7593087
- **Type**: conference
- **Published**: 5-9 Sept. 
- **Authors**: Lara Dolecek
- **PDF**: https://ieeexplore.ieee.org/document/7593087
- **Abstract**: Computing under uncertainty has become increasingly important in modern information processing systems. In this work, we first review exciting recent results on the multi-faceted role coding approaches can play in this important discipline, including fundamental performance limits of noisy iterative algorithms and decoders, implications on system design, and coding-theoretic methods for approximate computing. We also explore connections between coding theory and other disciplines in modern computing, and we present several new and promising research directions in coding for modern computing and noisy iterative information processing.

## Some properties of Homogenous Trellis-Constrained Codes

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7593118
- **Type**: conference
- **Published**: 5-9 Sept. 
- **Authors**: Christian Franck, Uli Sorger
- **PDF**: https://ieeexplore.ieee.org/document/7593118
- **Abstract**: We consider Homogenous Trellis-Constrained Codes (HTCC), a generalization of Turbo-codes where all bits are constrained. No efficient decoding algorithm is known for these codes, so our results are primarily of theoretical interest. We propose a technique to derive an upper bound for the maximum-likelihood (ML) decoding of BSC errors. Our technique is based on the weight distributions of the constituent codes and it can also be used when a specific number of errors e is known. We observe that with an ML-decoder some HTCC codes exhibit an error correcting performance close to that of random codes. For those codes we also observe a significant performance gap between ML-decoding and practical decoding based on belief-propagation.

## An HARQ scheme with large rate adaptation range and inter-packet cooperative decoding

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7593109
- **Type**: conference
- **Published**: 5-9 Sept. 
- **Authors**: Chia-Chi Lu, Tofar C.-Y. Chang, Tsu-Hsuan Chien +1
- **PDF**: https://ieeexplore.ieee.org/document/7593109
- **Abstract**: The throughput of a conventional rate-compatible code based hybrid automatic repeat request (HARQ) protocol is lower-bounded by the rate of the mother code used. The mother code rate along with the highest puncture rate determine the operation range of the protocol in terms of the average received signal-to-noise ratio (SNR). In this paper, we propose a new HARQ protocol based on rate-compatible punctured and shortened low-density parity-check (LDPC) code so that it admits a large operating SNR range. The large dynamic coding rate range is also useful for link adaptation applications. A distinct feature of the new HARQ protocol is: when a packet (frame) fails to pass the cyclic redundancy check (CRC) test and the system is operating at a rate lower than that of the mother code, the corresponding re-transmitted packet will consists of a coded payload resulted from systematic encoding a fraction of the CRC-failed bits plus new data bits. The re-encoded part plays the role of bridging two (component) codes, or equivalently, building a larger code out of smaller codes. Various decoding schedules that exchange messages between two or among more packets (component codes) become available and much decoding performance improvement can be obtained. Numerical results show that, compared with the conventional HARQ protocol, our approach provides significant better throughput performance in the low SNR region.

## LDPC codes for the q-ary bit-measurement channel

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7593117
- **Type**: conference
- **Published**: 5-9 Sept. 
- **Authors**: Rami Cohen, Yuval Cassuto
- **PDF**: https://ieeexplore.ieee.org/document/7593117
- **Abstract**: In this paper, we introduce a new channel model we term the q-ary bit-measurement channel (QBMC). This channel models a memory device, where q-ary symbols (q = 2s) are stored in the form of current/voltage levels. The symbols are read by measuring a single bit from the symbol in each read step, starting from the most significant bit. An error event occurs when not all the symbol bits are known, e.g., due to a premature termination of the read sequence. To deal with such error events, we propose the use of GF(q) low-density parity-check (LDPC) codes and analyze their iterative-decoding performance. In particular, we show how to exploit the algebraic structure of the QBMC channel for efficient analysis, and study the effect of the Tanner graph's edge-label distribution on the decoding performance. It is shown that for q = 4 the optimal correction of single-bit erasures is achieved by a distribution different from the uniform distribution on the non-zero elements of GF(4).

## Balanced locally repairable codes

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7593121
- **Type**: conference
- **Published**: 5-9 Sept. 
- **Authors**: Katina Kralevska, Danilo Gligoroski, Harald Øverby
- **PDF**: https://ieeexplore.ieee.org/document/7593121
- **Abstract**: We introduce a family of balanced locally repairable codes (BLRCs) [n, k, d] for arbitrary values of n, k and d. Similar to other locally repairable codes (LRCs), the presented codes are suitable for applications that require a low repair locality. The novelty that we introduce in our construction is that we relax the strict requirement the repair locality to be a fixed small number l, and we allow the repair locality to be either l or l + 1. This gives us the flexibility to construct BLRCs for arbitrary values of n and k which partially solves the open problem of finding a general construction of LRCs. Additionally, the relaxed locality criteria gives us an opportunity to search for BLRCs that have a low repair locality even when double failures occur. We use metrics such as a storage overhead, an average repair bandwidth, a Mean Time To Data Loss (MTTDL) and an update complexity to compare the performance of BLRCs with existing LRCs.

## Iterative decoding for Noisy Network Coding for Two-Way Relay channels

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7593083
- **Type**: conference
- **Published**: 5-9 Sept. 
- **Authors**: Michael Heindlmaier, Markus Staudacher
- **PDF**: https://ieeexplore.ieee.org/document/7593083
- **Abstract**: This paper presents a practical implementation of Noisy Network Coding (NNC) for half-duplex Two-Way Relay channels (TWRC). With Noisy Network Coding, the relay quantizes the incoming signals and forwards them digitally. The receivers do not try to recover the relay quantization index but the codewords that are embedded in the quantized signal. Our approach uses irregular repeat-accumulate low-density parity check (LDPC) codes to implement NNC. We derive the joint factor graph and the message passing rules for the corresponding joint iterative decoding scheme. Our simulation results confirm the performance advantages predicted by random coding arguments.

## Analysis of LDPC code syndrome entropy based on subgraphs

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7593128
- **Type**: conference
- **Published**: 5-9 Sept. 
- **Authors**: David Matas, Meritxell Lamarca
- **PDF**: https://ieeexplore.ieee.org/document/7593128
- **Abstract**: We propose a method to bound the syndrome entropy of linear block codes from their factor graph representation. It is specially suited for sparse graphs such as those of low density parity check codes. It is based on the chain rule decomposition of the entropy and the confinement of dependencies within code subgraphs. After forcing or assuming the subgraphs to have a tree structure, the computation is done by means of density evolution as for a belief propagation analysis. We employ this method to compute upper bounds of the LDPC code syndrome entropy, which allows us to obtain asymptotic MAP upper bounds that match the ones obtained by the generalized area theorem.

## Design of LDPC codes with tunable slope of their EXIT charts

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7593090
- **Type**: conference
- **Published**: 5-9 Sept. 
- **Authors**: Guido Montorsi
- **PDF**: https://ieeexplore.ieee.org/document/7593090
- **Abstract**: In this paper we consider the problem of designing LDPC codes to be used in bit turbo-receivers, where an outer binary (turbo) decoder iterates with a bit-detector computing LLR of coded bits from the channel outputs. This receiver structure has been proposed for several scenarios, including systems for high order modulations, MIMO, ISI, and Multi User systems. It has been shown that the bit turbo-receiver provides performance close to the optimal receiver if the bit-detector EXIT chart “matches” that of the outer code. Motivated by the observation that most bit-detector EXIT charts exhibit an almost linear behavior we then introduce the “slope” of the EXIT chart as a new parameter for the LDPC design. A family of binary LDPC codes having the possibility of tuning not only the rate, but also the slope of their EXIT chart, as well as the decoder complexity, is then an ideal candidate for being considered in future advanced transmission systems where the bit turbo-receiver will replace the more common BICM receiver that does not consider possible iterations with the bit detector. In this paper we provide an efficient algorithm for the design of LDPC codes ensembles with excellent performances with those constraints and derive some conclusions. It is shown that with a given performance threshold the complexity of LDPC decoder actually decreases when increasing the target slope, confirming the already observed fact that bit turbo-receiver requires weaker outer codes.

## Wave-like decoding of tail-biting spatially coupled LDPC codes through iterative demapping

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7593089
- **Type**: conference
- **Published**: 5-9 Sept. 
- **Authors**: Sebastian Cammerer, Laurent Schmalen, Vahid Aref +1
- **PDF**: https://ieeexplore.ieee.org/document/7593089
- **Abstract**: For finite coupling lengths, terminated spatially coupled low-density parity-check (SC-LDPC) codes show a non-negligible rate-loss. In this paper, we investigate if this rate loss can be mitigated by tail-biting SC-LDPC codes in conjunction with iterative demapping of higher order modulation formats. Therefore, we examine the BP threshold of different coupled and uncoupled ensembles. A comparison between the decoding thresholds approximated by EXIT charts and the density evolution results of the coupled and uncoupled ensemble is given. We investigate the effect and potential of different labelings for such a set-up using per-bit EXIT curves, and exemplify the method for a 16-QAM system, e.g., using set partitioning labelings. A hybrid mapping is proposed, where different sub-blocks use different labelings in order to further optimize the decoding thresholds of tail-biting codes, while the computational complexity overhead through iterative demapping remains small.

## Towards Gaussian capacity, universality and short block length

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7593147
- **Type**: conference
- **Published**: 5-9 Sept. 
- **Authors**: Chulong Liang, Junjie Ma, Li Ping
- **PDF**: https://ieeexplore.ieee.org/document/7593147
- **Abstract**: Forward error control (FEC) codes based on turbo, low-density parity-check (LDPC) and polar principles provide practical approaches towards channel capacity. There are, however, remaining challenges. Some of these are listed below. · How to achieve performance with Gaussian signaling'? · How to design codes that are universally good over different channel conditions'? · How to reduce code length while maintain good performance? In this paper, we introduce a scheme based on the recent progresses on spatial coupling and compressed sensing. The new scheme offers a potential solution to the above mentioned challenges.

## ADMM versus simplex algorithm for LP decoding

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7593107
- **Type**: conference
- **Published**: 5-9 Sept. 
- **Authors**: Florian Gensheimer, Stefan Ruzika, Stefan Scholl +1
- **PDF**: https://ieeexplore.ieee.org/document/7593107
- **Abstract**: In this paper, we investigate the complexity of different algorithms for LP decoding for short BCH and LDPC codes. Two approaches have gained particular interest: The simplex algorithm and the alternating direction method of multipliers (ADMM). For the adaptive LP decoding algorithm, we propose a special implementation of the dual simplex algorithm that uses the same simplex tableau in every linear program of the adaptive scheme. We compare this algorithm with another variant of the adaptive decoder and two variants of the recently proposed ADMM regarding the required arithmetic operations. These are important measures for design decisions for future hardware implementations.

## Min-Sum decoding of irregular LDPC codes with adaptive scaling based on mutual information

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7593079
- **Type**: conference
- **Published**: 5-9 Sept. 
- **Authors**: Florence Alberge
- **PDF**: https://ieeexplore.ieee.org/document/7593079
- **Abstract**: Min-Sum decoding (MS) is an alternative to belief propagation decoding with substantially lower complexity. MS often results in an overestimation of the log likelihood ratio (LLR) in particular in the early stage of the iterative process. A linear post-processing is usually performed as a compensation. With regular low density parity check codes (LDPC), a fixed scaling of the LLR yields sufficiently good results. In contrast, adaptive strategies are mandatory with irregular codes. It is well known that the scaling factor is an increasing function of the reliability of the LLR. In most of the publications, the scaling factor is envisioned as a function of both the iteration number and the signal-to-noise ratio. It is proposed here to use the mutual information between extrinsics as a measure of the reliability of the LLR. A practical implementation is derived with reasonable complexity. Compared to the literature, the proposed method yields slightly better results in terms of BER and a significant reduction in the number of iterations.

## Punctured parallel concatenated convolutional lattice codes

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7593088
- **Type**: conference
- **Published**: 5-9 Sept. 
- **Authors**: Toshiki Matsumine, Hideki Ochiai
- **PDF**: https://ieeexplore.ieee.org/document/7593088
- **Abstract**: Convolutional lattice codes, also known as signal codes, are shown to achieve a good performance but with considerably high decoding complexity due to the unbounded number of resulting trellis states. Recently, an alternative approach that can restrict the trellis states based on the recursive convolutional lattice codes is proposed, and its parallel concatenation extension, referred to as turbo signal codes, is shown to achieve the frame error rate (FER) performance close to the Shannon limit. The main drawback is its reduced information rate associated with parallel concatenation and lack of flexibility in its design. This paper thus proposes a symbol puncturing approach to enhance the flexibility in achievable information rate of the turbo signal codes. Simulation results demonstrate that with the information rate of 2.85 bits per two dimension and the block length of 8200 symbols before puncturing, the FER of 10-2 can be achieved within the SNR gap of 0.91 dB from the Shannon limit.

## Modified augmented belief propagation for general memoryless channels

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7593103
- **Type**: conference
- **Published**: 5-9 Sept. 
- **Authors**: Benjamin Gadat, Charly Poulliat
- **PDF**: https://ieeexplore.ieee.org/document/7593103
- **Abstract**: In this paper, we propose an efficient implementation of the augmented belief propagation (ABP) algorithm for low-density parity-check codes over general memoryless channels. ABP is a multistage BP based decoder that uses a backtracking processing when decoding fails. The algorithm proceeds in two main steps, namely a symbol selection step and an augmented decoding step. The former is based on a criterion related both to the stopping subgraph connectivity and to the input reliability, while the latter can be either implemented using a list based or a greedy approach. Compared to the original implementation, we consider a different approach for both steps. First, the proposed node selection is only based on the dynamic of sign changes of the extrinsic messages at the variable nodes output. This enables us to consider indifferently general memoryless channels, while still taking into account the graph irregularity. Then, we propose a simple yet efficient implementation of the augmented decoding procedure based on pruning of the branching tree The proposed algorithm shows near maximum likelihood decoding performance while decreasing the overall complexity (computation and memory) of the original algorithm. Moreover, complexity-performance trade-off is an built-in feature for this kind of algorithm.

## Fault-tolerant parallel linear filtering using compressive sensing

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7593105
- **Type**: conference
- **Published**: 5-9 Sept. 
- **Authors**: Yaoqing Yang, Pulkit Grover, Soummya Kar
- **PDF**: https://ieeexplore.ieee.org/document/7593105
- **Abstract**: In this paper, we study the problem of designing fault-tolerant parallel linear filters. We assume that a linear filter can either function perfectly or fail completely, i.e., generate arbitrary outputs. We use real-number error correcting codes based on linear programming decoding to introduce redundancy into the linear filters and detect faulty filters. We prove that all faulty filters can be detected and corrected if the number of faulty filters is smaller than a threshold value. We also obtain simulation results to support our statement. To the best of our knowledge, we believe that this work is the first to connect the information-theoretic idea of real-number error control coding with parallel linear filtering systems.

## Density evolution for deterministic generalized product codes with higher-order modulation

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7593112
- **Type**: conference
- **Published**: 5-9 Sept. 
- **Authors**: Christian Häger, Alexandre Graell i Amat, Henry D. Pfister +1
- **PDF**: https://ieeexplore.ieee.org/document/7593112
- **Abstract**: Generalized product codes (GPCs) are extensions of product codes (PCs) where coded bits are protected by two component codes but not necessarily arranged in a rectangular array. It has recently been shown that there exists a large class of deterministic GPCs (including, e.g., irregular PCs, half-product codes, staircase codes, and certain braided codes) for which the asymptotic performance under iterative bounded-distance decoding over the binary erasure channel (BEC) can be rigorously characterized in terms of a density evolution analysis. In this paper, the analysis is extended to the case where transmission takes place over parallel BECs with different erasure probabilities. We use this model to predict the code performance in a coded modulation setup with higher-order signal constellations. We also discuss the design of the bit mapper that determines the allocation of the coded bits to the modulation bits of the signal constellation.

## Performance analysis for transmission of correlated sources over non-orthogonal MARCs

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7593078
- **Type**: conference
- **Published**: 5-9 Sept. 
- **Authors**: Jiguang He, Iqbal Hussain, Valtteri Tervo +2
- **PDF**: https://ieeexplore.ieee.org/document/7593078
- **Abstract**: Non-orthogonal transmission is considered as one of the promising approaches to improve the throughput of current and future wireless communication networks. We focus on the transmission of correlated sources over a non-orthogonal multiple access relay channel (MARC), which consists of two sources, one relay, and one destination. For non-orthogonal transmission over such networks, only two time slots are required as compared to three time slots used in the conventional orthogonal MARC. At the relay node, physical-layer network coding technique is employed to decode the bit-wise exclusive OR (XOR) version of the sources' information sequences rather than decode their original individual information sequences. Subsequently, the relay re-encodes the decoded combined sequence and forwards it to the destination. The destination then exploits this sequence as a helper to recover the sources' original individual information sequences. We analyze the outage probability of the non-orthogonal MARC based on the theorem of multiple access channel (MAC) with a helper, which combines Slepian-Wolf compression rate region and MAC capacity region. Simulation results are provided to verify the accuracy of the theoretical analysis.

## On adaptive linear programming decoding of nonbinary linear codes over prime fields

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7593086
- **Type**: conference
- **Published**: 5-9 Sept. 
- **Authors**: Eirik Rosnes, Michael Helmling
- **PDF**: https://ieeexplore.ieee.org/document/7593086
- **Abstract**: In this work, we study linear programming (LP) decoding of nonbinary linear codes over prime fields. In particular, we develop a novel separation algorithm for valid inequalities describing the codeword polytope of the so-called constant-weight embedding of a single parity-check (SPC) code over any prime field. The algorithm has linear (in the length of the SPC code) complexity, is structurally different from the one for binary codes, and is based on the principle of dynamic programming. Furthermore, it is the basis of the proposed efficient (relaxed) adaptive LP (ALP) decoder for general (non-SPC) linear codes over any prime field, generalizing the well-known ALP decoding algorithm for binary codes. Numerical results show that the ALP decoding algorithm is very efficient compared to a static approach.

## Asymptotic and finite frame length analysis of frame asynchronous coded slotted ALOHA

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7593081
- **Type**: conference
- **Published**: 5-9 Sept. 
- **Authors**: Erik Sandgren, Alexandre Graell i Amat, Fredrik Brännström
- **PDF**: https://ieeexplore.ieee.org/document/7593081
- **Abstract**: We consider a frame-asynchronous coded slotted ALOHA (FA-CSA) system where users join according to a Poisson random process. In contrast to standard frame-synchronous CSA (FS-CSA), when a user joins the system, it transmits a first replica of its message in the following slot and other replicas uniformly at random in a number of subsequent slots. We derive the (approximate) density evolution that characterizes the asymptotic performance of FA-CSA when the frame length goes to infinity. We show that, if the receiver can monitor the system before users start transmitting, a boundary effect similar to that of spatially-coupled codes occurs, which greatly improves the decoding threshold as compared to FS-CSA. We also derive analytical approximations of the error floor (EF) in the finite frame length regime. We show that FA-CSA yields in general lower EF, better performance in the waterfall region, and lower average delay, as compared to FS-CSA.

## Iterative erasure correcting algorithm for q-ary reed-muller codes based on local correctability

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7593072
- **Type**: conference
- **Published**: 5-9 Sept. 
- **Authors**: Shinya Fukumoto, Tadashi Wadayama
- **PDF**: https://ieeexplore.ieee.org/document/7593072
- **Abstract**: In this paper, we propose a novel iterative erasure correcting algorithm for q-ary RM codes based on their local correctability. The proposed algorithm consists of two phases. In the first phase, the algorithm tries to find all the lines that help to correct as many erasure symbols as possible, and then local erasure correction procedures based on Lagrange interpolation are executed in the second phase. These two phases are repeated until the number of iterations reaches a given number. In both phases, most of computation processes are independent and thus the proposed algorithm provides massive parallelism. Computer experiments show that the convergence of an iterative decoding process is very fast in many cases. With some parameter setting, it is observed that the algorithm yields near ML decoding performance. If an decoding process is carried out with n-parallel processors (n represents the code length), the algorithm runs with sublinear-time on n if certain conditions are met.

## Construction-A full-diversity lattices

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7593126
- **Type**: conference
- **Published**: 5-9 Sept. 
- **Authors**: Joseph J. Boutros, Jean-Claude Belfiore
- **PDF**: https://ieeexplore.ieee.org/document/7593126
- **Abstract**: Lattices from Construction A and non-binary codes are considered. These lattices are built from number fields as coset codes of the ring of integers OK modulo an ideal I. Diversity of a Construction-A lattice Λ on block-fading channels is guaranteed by the chain Im ⊂ Λ ⊂ OKm. We study how the code alphabet size should be chosen in order to avoid error floors on the Gaussian channel due to the sublattice Im. Our aim is to get Construction-A lattices that are good for both Gaussian and block-fading channels.

## Pragmatic code-aided phase synchronization in iterative multi-sample receivers

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7593065
- **Type**: conference
- **Published**: 5-9 Sept. 
- **Authors**: M. Asim, M. Martalò, G. Ferrari +1
- **PDF**: https://ieeexplore.ieee.org/document/7593065
- **Abstract**: In this paper, we consider communications impaired by phase noise and we propose an iterative multi-sample receiver, where the received signal is sampled with more than one sample per symbol interval. The approach is pragmatic in the sense that demodulation/decoding is performed separately from synchronization and relies on “off-the-shelf” subblocks. In particular, we extend a recently proposed Maximum A-posteriori Probability (MAP)-based algorithm for phase synchronization by exploiting oversampling at the receiver. Our simulation results show an improved performance with respect to a “classical” receiver, where phase synchronization relies on one sample per symbol interval only, for high phase noise scenarios.

## Turbo code design for short blocks

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7601543
- **Type**: conference
- **Published**: 5-7 Sept. 
- **Authors**: Thomas Jerkovits, Balazs Matuz
- **PDF**: https://ieeexplore.ieee.org/document/7601543
- **Abstract**: This work considers the design of short parallel turbo codes (PTCs) with block lengths in the order of (a few) hundred code bits. In particular we aim at designing codes with large minimum distance. To this end a structured approach is presented to find suitable component code configurations, as well as interleavers. As a result the proposed turbo codes possess low error floors and outperform competing binary low-density parity-check (LDPC) codes by approximately 0:9 dB and state-of-the-art binary turbo codes by 0:4 dB at a code word error rate (CER) of about ≈10-7. The loss w.r.t. the random coding bound (RCB) is only about 0:8 dB.

## System capacity evaluation of DVB-S2X based medium earth orbit satellite network operating at Ka band

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7601471
- **Type**: conference
- **Published**: 5-7 Sept. 
- **Authors**: C. Kourogiorgas, D. Tarchi, A. Ugolini +4
- **PDF**: https://ieeexplore.ieee.org/document/7601471
- **Abstract**: In this paper, the performance of a Medium Earth Orbit (MEO) satellite trunking system operating in Ka-band in terms of capacity statistics is studied, taking into account sophisticated propagation and physical layer tools. First, the satellite system model is presented and some general considerations of the MEO constellation and network are given. Afterwards, a tool for generating atmospheric attenuation time series induced on links operating at Ka-band with time dependent elevation angle, such as Earth-MEO links, is described. The tool is derived modifying the atmospheric attenuation time series generators for links with fixed elevation angles. Moreover, an optimized in terms of spectral efficiency physical layer design is provided, employing also some higher constellation modulations from the recent DVB-S2X standard. Finally, considering Adaptive Coding and Modulation which allows providing the instantaneously highest data rate for a given link budget, we evaluate the total system capacity provided by the MEO constellation. In the numerical results section, capacity results are presented for a variety of ground stations located in different climatic areas.

## QAM to circular isomorphic constellations

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7601550
- **Type**: conference
- **Published**: 5-7 Sept. 
- **Authors**: Farbod Kayhan
- **PDF**: https://ieeexplore.ieee.org/document/7601550
- **Abstract**: Employing high order constellations is inevitable in order to achieve higher spectral efficiency in satellite communication systems. In DVB-S2X standard, constellations with up to 256 points have been included. However, optimizing such high order constellations is a difficult task. In this paper we propose a very simple constellation design based on the radial map from QAM constellations to non-uniform APSK constellations. Our method provides a systematic way to generate a family of optimized high order constellations. We show that gains larger than 0.5 dB can be obtained with respect to the DVB- S2X constellations with 256 points. Even though the proposed constellations are essentially sub-optimal (in terms of maximizing the mutual information), they provide a very competitive test benchmark for the performance of high order constellations. Moreover, the proposed construction potentially allows for an efficient one-dimensional soft detection by an inverse mapping to the QAM. Finally, further optimization techniques are discussed.

## Advanced signal processing techniques for fixed and mobile satellite communications

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7601468
- **Type**: conference
- **Published**: 5-7 Sept. 
- **Authors**: Pol Henarejos, Ana Perez-Neira, Nicolo Mazzali +1
- **PDF**: https://ieeexplore.ieee.org/document/7601468
- **Abstract**: Enabling ultra fast systems has been widely investigated during recent decades. Although polarization has been deployed from the beginning in satellite communications, nowadays it is being exploited to increase the throughput of satellite links. More precisely, the application of diversity techniques to the polarization domain may provide reliable, robust, and fast satellite communications. Better and more flexible spectrum use is also possible if transmission and reception can take place simultaneously in close or even overlapping frequency bands. In this paper we investigate novel signal processing techniques to increase the throughput of satellite communications in fixed and mobile scenarios. First, we investigate four-dimensional (4D) constellations for the forward link. Second, we focus on the mobile scenario and introduce an adaptive algorithm which selects the optimal tuple of modulation order, coding rate, and MIMO scheme that maximizes the throughput constraint to a maximum packet error rate. Finally, we describe the operation of radio transceivers which cancel actively the self-interference posed by the transmit signal when operating in full-duplex mode.

## A Software Defined Radio based DOCSIS 3.1 measurement receiver

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7684733
- **Type**: conference
- **Published**: 5-7 Sept. 
- **Authors**: Florian Jackisch, Daniel Rother, Christoph Juchems
- **PDF**: https://ieeexplore.ieee.org/document/7684733
- **Abstract**: The Data Over Cable Service Interface Specification (DOCSIS) provides Internet access via cable TV networks. The latest version 3.1 replaces the Physical Layer of previous DOCSIS versions. With DOCSIS 3.1, broadband cable network operators want to accelerate their networks to gigabit-per-second speeds. Enhancements include an increased bandwidth per downstream channel of up to 192MHz, Orthogonal Frequency-Division Multiplex with a 4096 Quadrature Amplitude Modulation, and Low Density Parity Check Codes. These changes require new high performance hard- and software decoders. This paper presents the concept of a measurement receiver based on Software Defined Radio (SDR). The measurement receiver features a novel hardware frontend, an improved pre-FFT timing and frequency offset estimation under Roll-Off conditions, a high-performance LDPC decoder, and a Graphical User Interface for data analysis. It is shown that the SDR approach achieves good performance and is suitable for a DOCSIS 3.1 measurement decoder that focuses primarily on the Physical Link Channel.

## Analysis and design of rate compatible LDPC codes

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7794684
- **Type**: conference
- **Published**: 4-8 Sept. 
- **Authors**: Fulvio Babich, Matteo Noschese, Francesca Vatta
- **PDF**: https://ieeexplore.ieee.org/document/7794684
- **Abstract**: The main concern in nowadays digital communications standards, such as IEEE802.11n, 802.16e (Wi-MAX), 100BaseT Ethernet, and Digital Video Broadcasting (DVB), is the need of adaptive and flexible communication techniques. The request for higher efficiency, both in bandwidth use and power consumption, increases the need for limit-achieving, flexible techniques of channel coding. Low Density Parity Check (LDPC) Codes are very interesting because of their high performances and potential flexibility introduced by puncturing. In this paper, the design of rate-compatible LDPC is addressed. A class of punctured LDPC codes is defined through their equivalent parity check matrices. A formal analysis is provided, based on a simplified approach on the decoding belief propagation algorithm, i.e., considering a Gaussian approximation for message densities under density evolution. A suitable design criterion for the puncturing patterns is then addressed.

## Fast convergence of joint demodulation and decoding based on joint sparse graph for spatially coupling data transmission

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7794756
- **Type**: conference
- **Published**: 4-8 Sept. 
- **Authors**: Zhengxuan Liu, Yanyan Guo, Guixia Kang +2
- **PDF**: https://ieeexplore.ieee.org/document/7794756
- **Abstract**: Spatially coupling data transmission (SCDT) is a multiple access technique. Since both SCDT and low density parity-check (LDPC) codes can be represented by a factor graph, a joint sparse graph (JSG) including the single graphs of SCDT and LDPC codes is constructed. Based on the JSG, the joint demodulation and decoding (JDD) by applying belief propagation (BP) algorithm in the parallel schedule is performed, but its convergence rate is slow. In order to accelerate convergence rate, a new serial schedule is proposed. The extrinsic information transfer (EXIT) charts of iterative JDD are investigated for the two schedules and employed to evaluate their converge behaviour. EXIT analysis and simulation results demonstrate that about half iteration number can be saved at the cost of marginal system performance loss. Furthermore, compared with separate demodulation and decoding, turbo-structured JDD and the uncoupling structured JDD, the JDD based on JSG for SCDT by utilizing serial schedule achieves the best performance.

## The design of protograph LDPC codes for channel-coded physical-layer network coding

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7794683
- **Type**: conference
- **Published**: 4-8 Sept. 
- **Authors**: Pingping Chen, Kaixiong Su, Yi Fang +1
- **PDF**: https://ieeexplore.ieee.org/document/7794683
- **Abstract**: For two-way relay channel-coded physical network coding (CPNC) systems with sufficiently low code rate, the separate complete decoding (SCD) scheme outperforms the joint channel-physical network coding (JCNC) scheme. Hence, this paper addresses the design of protograph LDPC codes to approach the SCD-based CPNC capacity. In fact, due to virtual erasures induced by CPNC transmission, the conventional protograph that approaches point to point (P2P) AWGN capacity may not perform well in SCD-based CPNC channel in terms of error rates. We then use the finite-length EXIT chart to calculate iterative decoding threshold of a joint code graph formed by two codes in the SCD. Furthermore, we investigate the serial separate complete decoding (S-SCD) and parallel separate decoding (P-SCD). Simulation results show that with the S-SCD, the proposed protograph codes have within 0.9 dB of their capacity limits for rates from 1/3 to 3/5.

## On physical-layer Raptor coded modulation with Gray-mapped 16QAM

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7794682
- **Type**: conference
- **Published**: 4-8 Sept. 
- **Authors**: Shiuan-Hao Kuo, Hsuan-Kuan Wu, Mao-Chao Lin
- **PDF**: https://ieeexplore.ieee.org/document/7794682
- **Abstract**: Binary physical-layer Raptor (PLR) codes are known to be capable of approaching the channel capacity over the binary-input additive white Gaussian noise (BIAWGN) channel efficiently. It is desired to apply PLR codes to high order modulations to achieve good spectral efficiency. Herein we study the designs of using conventional PLR codes and protograph-based PLR codes by taking standard Gray-mapped 16QAM into consideration. Simulation results are presented to show the advantages of various designs.

## QC-LDPC Gear-Like Decoder Architecture with Multi-domain Quantization

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7723560
- **Type**: conference
- **Published**: 31 Aug.-2 
- **Authors**: Oana Boncalo
- **PDF**: https://ieeexplore.ieee.org/document/7723560
- **Abstract**: This paper proposes multi-domain quantization for a partially-parallel QC-LDPC decoder, which allows efficient memory bandwidth utilization. The change of quantization during decoding is dynamic. In addition to this, the proposed decoder targets speedup and energy efficient processing, with negligible error correction capability degradation. From the message storage perspective, it uses 2 quantization modes: a high resolution based q-bit messages, and a low resolution q/2-bit messages. Regarding the lower quantization domain, the variable node units operate on q/2+1 resolution, while check node units process q/2-bit messages. In order to evaluate the efficiency of this approach, we have analyzed the decoding performance for both AWGN and BSC channel models. In addition to this, we have implemented the proposed units and evaluated the overhead with respect to the baseline.

## Flexible, Cost-Efficient, High-Throughput Architecture for Layered LDPC Decoders with Fully-Parallel Processing Units

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7723558
- **Type**: conference
- **Published**: 31 Aug.-2 
- **Authors**: Thien T. Nguyen-Ly, Tushar Gupta, Manuel Pezzin +3
- **PDF**: https://ieeexplore.ieee.org/document/7723558
- **Abstract**: In this paper, we propose a layered LDPC decoder architecture targeting flexibility, high-throughput, low cost, and efficient use of the hardware resources. The proposed architecture provides full design time flexibility, i.e., it can accommodate any Quasi-Cyclic (QC) LDPC code, and also allows redefining a number of parameters of the QC-LDPC code at the run time. The main novelty of the paper consists of: (1) a new low-cost processing unit that merges the logical functionalities of the Variable-Node Unit (VNU) and the A Posteriori Log-Likelihood Ratio (AP-LLR) unit in an efficient way, (2) a high speed, low-cost Check-Node Unit (CNU) architecture, which is executed twice at each iteration in order to complete the computation of the check-node messages, (3) a splitting of the iteration processing in two perfectly symmetric stages, executed in two consecutive clock cycles, each one using exactly the same processing resources, the processing load is perfectly balanced between the two clock cycles, thus yielding an optimal clock frequency. Synthesis results targeting a 65nm CMOS technology for a (3,6)-regular (648,1296) Quasi-Cyclic LDPC code and for the WiMax (1152,2304) irregular QC-LDPC code show significant improvements in terms of area and throughput compared to the baseline architecture discussed in this paper, as well as several state of the art implementations.

## Multi-bit transient fault control for NoC links using 2D fault coding method

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7579328
- **Type**: conference
- **Published**: 31 Aug.-2 
- **Authors**: Xiaowen Chen, Zhonghai Lu, Yuanwu Lei +2
- **PDF**: https://ieeexplore.ieee.org/document/7579328
- **Abstract**: In deep nanometer scale, Network-on-Chip (NoC) links are more prone to multi-bit transient fault. Conventional ECC techniques brings heavy area, power, and timing overheads when correcting and detecting multiple transient faults. Therefore, a cost-effective ECC technique, named 2D fault coding method, is adopted to overcome the multi-bit transient fault issue of NoC links. Its key innovation is that the wires of a link are treated as its matrix appearance and light-weight Parity Check Coding (PCC) is performed on the matrix's two dimensions (horizontal matrix rows and vertical matrix columns). Horizontal PCCs and vertical PCCs work together to find the faults' position and then correct them by simply inverting them. The procedure of using the 2D fault coding method to protect a NoC link is proposed, its correction and detection capability is analyzed, and its hardware implementation is carried out. Comparative experiments show that the proposal can largely reduce the ECC hardware cost, have much higher fault detection coverage, maintain almost zero silent fault percentages, and have higher fault correction percentages normalized under the same area, demonstrating that it is cost-effective and suitable to the multi-bit transient fault control for NoC links.

## Improved quantum LDPC decoding strategies for the misidentified quantum depolarization channel

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7760297
- **Type**: conference
- **Published**: 29 Aug.-2 
- **Authors**: Yixuan Xie, Jun Li, Robert Malaney +1
- **PDF**: https://ieeexplore.ieee.org/document/7760297
- **Abstract**: In this work, the importance of the channel mismatch effect in degrading the performance of deployed quantum LDPC codes has been pointed out. We help remedy this situation by proposing new quantum LDPC decoding strategies that can significantly reduce performance degradation by as much as 50%. Our new strategies for the quantum LDPC decoder are based on previous insights from classical LDPC decoders in mismatched channels, where an asymmetry in performance is known as a function of the estimated channel noise. We show how similar asymmetries carry over to the quantum depolarizing channel, and how an estimate of the depolarization flip parameter weighted to larger values leads to significant performance improvement.

## Multiple description vector quantizer design based on redundant representation of central code

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7760219
- **Type**: conference
- **Published**: 29 Aug.-2 
- **Authors**: Akinori Ito
- **PDF**: https://ieeexplore.ieee.org/document/7760219
- **Abstract**: A design method of a multiple description vector quantizer (VQ) is proposed. VQ is widely used for data compression, transmission and other processing. Here, we assume transmission channels with data erasure such as a packet-based network. Multiple description coding is a coding method used to achieve “graceful degradation” when transmitting signals through lossy channels. The proposed method is inspired by the vector quantizer design of Poggi et al., which combines VQ design based on the self-organizing map (SOM) and the multiple description scalar quantizer (MDSQ). The method also uses the SOM-based VQ; the difference is that the proposed method combines a bit-error-tolerant VQ designed by SOM and a novel scheme for cell arrangement of SOM based on Redundant Representation of Central Code (RRCC). The method is not only easy to design for any bit rate but is also more robust against data erasure compared with the conventional VQ.

## Utilisation of multipath phenomenon to improve the performance of BCH and RS codes

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7835880
- **Type**: conference
- **Published**: 28-30 Sept
- **Authors**: Alyaa Al-Barrak, Ali Al-Sherbaz, Triantafyllos Kanakis +1
- **PDF**: https://ieeexplore.ieee.org/document/7835880
- **Abstract**: In wireless communication, there exists a phenomenon know as `multipath'. This phenomenon is considered as a disadvantage because it causes interference. The multipath phenomenon results in an antenna receiving two or more signals from the same sent signal from different paths. This paper considers them as redundant copies of the transmitted data and utilises them to improve the performance of forward error correction (FEC) codes without extra redundancy, in order to improve data transmission reliability and increase the bit rate over wireless communication channels. The system was evaluated in bit error rate (BER) and used Bose, Ray-Chaudhuri and Hocquenghem (BCH) and Reed-Solomon (RS) codes as FEC. The results showed that the utilisation of the multipath improves the performance of FEC. Furthermore, the performance of FEC codes had t1 error correction capability and employed the multipath is better than FEC codes have t2 error correction capability and without the multipath, where t1 <; t2. Consequently, the bit rate is increased, and communication reliability is improved without extra redundancy.

## Error correction for approximate computing

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7852336
- **Type**: conference
- **Published**: 27-30 Sept
- **Authors**: Hang Zhang, Afshin Abdi, Faramarz Fekri +1
- **PDF**: https://ieeexplore.ieee.org/document/7852336
- **Abstract**: Approximate computing, which sacrifices the accuracy during computation, is a promising technology to save energy. However, large number of computation errors may violate the accuracy requirement of certain applications and should be corrected. Consider a Graphical Processing Unit (GPU) with multiple Streaming Multiprocessors (SMs), where some of these SMs perform accurate computation while the others perform approximate computation. Provided the approximate outputs are correlated with other accurate outputs, we exploit this relation and model the approximate computation process as a communication process. Then the problem of error correction transforms to a problem of decoding and we want to solve it with certain error correction code. Different from the classical communications process, approximate computing raises additional constraints on the code design. In this paper, we propose a semi-regular LDPC code satisfying these constraints and prove this code can be perfectly decoded. Certain properties of the code are analyzed and simulations are provided to verify the statement.

## Learning to decode linear codes using deep learning

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7852251
- **Type**: conference
- **Published**: 27-30 Sept
- **Authors**: Eliya Nachmani, Yair Be'ery, David Burshtein
- **PDF**: https://ieeexplore.ieee.org/document/7852251
- **Abstract**: A novel deep learning method for improving the belief propagation algorithm is proposed. The method generalizes the standard belief propagation algorithm by assigning weights to the edges of the Tanner graph. These edges are then trained using deep learning techniques. A well-known property of the belief propagation algorithm is the independence of the performance on the transmitted codeword. A crucial property of our new method is that our decoder preserved this property. Furthermore, this property allows us to learn only a single codeword instead of exponential number of codewords. Improvements over the belief propagation algorithm are demonstrated for various high density parity check codes.

## On failing sets of the interval-passing algorithm for compressed sensing

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7852245
- **Type**: conference
- **Published**: 27-30 Sept
- **Authors**: Yauhen Yakimenka, Eirik Rosnes
- **PDF**: https://ieeexplore.ieee.org/document/7852245
- **Abstract**: In this work, we analyze the failing sets of the interval-passing algorithm (IPA) for compressed sensing. The IPA is an efficient iterative algorithm for reconstructing a k-sparse nonnegative n-dimensional real signal x from a small number of linear measurements y. In particular, we show that the IPA fails to recover x from y if and only if it fails to recover a corresponding binary vector of the same support, and also that only positions of nonzero values in the measurement matrix are of importance for success of recovery. Based on this observation, we introduce termatiko sets and show that the IPA fails to fully recover x if and only if the support of x contains a nonempty termatiko set, thus giving a complete (graph-theoretic) description of the failing sets of the IPA. Finally, we present an extensive numerical study showing that in many cases there exist termatiko sets of size strictly smaller than the stopping distance of the binary measurement matrix; even as low as half the stopping distance in some cases.

## Compressed sensing using sparse-graph codes for the continuous-alphabet setting

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7852309
- **Type**: conference
- **Published**: 27-30 Sept
- **Authors**: Dong Yin, Ramtin Pedarsani, Xiao Li +1
- **PDF**: https://ieeexplore.ieee.org/document/7852309
- **Abstract**: In this paper, we consider the compressive sensing (CS) problem in the presence of noise. The problem is to recover a K-sparse signal s ∈ ℝn from noisy linear measurements y = As + w. We propose a fast recovery algorithm that can reconstruct any K-sparse signal s with time complexity that grows linearly in K and sublinearly in n. Specifically, with high probability, our algorithm is able to recover an arbitrarily large fraction of the support of the sparse signal using Θ(K log(n) log log(n)) samples and Θ(K log1+r(n)) computational cost, where r > 0 is an arbitrarily small constant. The sample and time complexities are near order-optimal. Further, our algorithm is able to recover the exact support with Θ(K log(K) log(n) log log(n)) measurements and time complexity of Θ(K log(K) log1+r(n)). With a mild technical assumption on the existence of a code with universal decoding algorithm and small decoding complexity, our algorithm can achieve Θ(K log(n)) sample and time complexities for the large fraction recovery, and furthermore, Θ(K log(K) log(n)) sample and time complexities for the full support recovery. The design of measurements and the recovery algorithm are based on sparse graph codes. We also justify our theoretical results with numerical experiments.

## LDPC decoder implementation using FPGA

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7881803
- **Type**: conference
- **Published**: 27-28 Sept
- **Authors**: Mahdie Kiaee, Hossein Gharaee, Naser Mohammadzadeh
- **PDF**: https://ieeexplore.ieee.org/document/7881803
- **Abstract**: This paper presents a partial-parallel LDPC decoder based on sum-product algorithm with high throughput. The hardware implementation of decoder considers design issues with respect to FPGA and time scheduling is proposed based on modified TPMP1 algorithm in order to reduce the number of clock cycles, hardware resources and power. The decoder is implemented for a code length of 672 whit rate of 3/4, maximum throughput of 3360 Mbps in maximum frequency of 280 MHz and provides power of 150 mW.

## On iterative LDPC-based joint decoding scheme for binary input Gaussian multiple access channel

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7779328
- **Type**: conference
- **Published**: 26-29 Sept
- **Authors**: Alexey Frolov, Pavel Rybin, Fedor Ivanov
- **PDF**: https://ieeexplore.ieee.org/document/7779328
- **Abstract**: Non-orthogonal multiple access schemes are of great interest for next generation wireless systems, as such schemes allow to reduce the total number of resources (frequencies or time slots) in comparison to orthogonal transmission (TDMA, FDMA, CDMA). In this paper we consider an iterative LDPC-based joint decoding scheme suggested in [1]. We investigate the most difficult and important problem where all the users have the same power constraint and the same rate. For the case of 2 users we use a known scheme and analyze it by means of simulations. We found the optimal relation between the number of inner and outer iterations. We further extend the scheme for the case of any number of users and investigated the cases of 3 and 4 users by means of simulations. Finally, we showed, that considered non-orthogonal transmission scheme is more efficient (for 2 and 3 users), than orthogonal transmission.

## Linear codes for an effective quantization of data

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7779342
- **Type**: conference
- **Published**: 26-29 Sept
- **Authors**: Vladimir N. Potapov
- **PDF**: https://ieeexplore.ieee.org/document/7779342
- **Abstract**: We consider the problem of finding a set S of vertices (code) of the Boolean n-cube having cardinality 2n-k and intersecting with maximum number of k-dimensional faces. We prove that the ratio between the numbers of the k-faces containing codewords and all k-faces is less than 1 - 1+o(1)/√(2πk) as n → ∞ for sufficiently large k. The solution of the problem in the class of linear codes is found. For n = 2k - 1 the best ratio is reached on 1-error correcting Hamming codes. Connections between this problem and an efficiency of quantization are discussed.

## Directed search decoding of polar codes with Reed-Solomon kernel

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7779336
- **Type**: conference
- **Published**: 26-29 Sept
- **Authors**: Ruslan Morozov, Peter Trifonov
- **PDF**: https://ieeexplore.ieee.org/document/7779336
- **Abstract**: The directed search algorithm, introduced originally for decoding of polar codes with Arikan kernel, is generalized to the case of a Reed-Solomon kernel. The algorithm relies heavily on the knowledge of symbol subchannel error probabilities of the polarizing transformation. A method to approximate these probabilities is suggested. The proposed method results in almost the same complexity and performance as in the case of the decoder using exact values of error probabilities.

## An image pre-processing approach for JSCC scheme based on double protograph LDPC codes

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7751602
- **Type**: conference
- **Published**: 26-28 Sept
- **Authors**: Qiwang Chen, Lin Wang, Shaohua Hong
- **PDF**: https://ieeexplore.ieee.org/document/7751602
- **Abstract**: An image pre-processing approach is proposed for joint source-channel coding (JSCC) scheme based on double protograph low-density parity-check (DP-LDPC) codes. Firstly, discrete cosine transform (DCT) and quantization are applied to the transmitted images. Different from the data processing of the previous approach for the quantized DCT coefficients, the representation of true form takes the place of complement form. Meanwhile, the high entropy frames will be pre-processed into low entropy frames through frame decomposition procedure due to the entropy of source frame limited by the code-rate of source code. Simulation results indicate that the JSCC scheme with the proposed image pre-processing approach improves the transmission efficiency and can recover the images with good quality at a very low signal-to-noise ratio (SNR).

## Optimization of LDPC codes for bit-patterned media recording with media noise

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7751601
- **Type**: conference
- **Published**: 26-28 Sept
- **Authors**: Lingjun Kong, Shengmei Zhao, Ming Jiang +1
- **PDF**: https://ieeexplore.ieee.org/document/7751601
- **Abstract**: Challenges in bit-pattered magnetic recording (BPMR) include two-dimensional (2D) inter-symbol interference (ISI) constituted by both one-dimensional ISI and inter-track interference (ITI), and media noise arising from island position jitter (PJ) and island size fluctuations (SF) in both the down-track and cross-track directions. A LDPC code optimization approach is proposed for BPMR channel with media noise, where a reduced-complexity 2D detector based on the iterative row-column soft detection feedback with Gaussian approximation (IRCSDF-GA) detector is employed. Also, the threshold of the proposed LDPC codes is calculated for different percentage of media noise in BPMR. Simulations results show that about 0.3 dB performance gain can be achieved when BPMR is only suffered from the PJ.

## A joint abnormal event detection scheme based on compressed sensing for Internet of Things

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7751684
- **Type**: conference
- **Published**: 26-28 Sept
- **Authors**: Xuan Sun, Xin Gao, Chen Li
- **PDF**: https://ieeexplore.ieee.org/document/7751684
- **Abstract**: In order to improve the efficiency of abnormal event detection for Internet of Things, this paper proposes an abnormal event detection scheme based on compressed sensing. Due to the low energy consumption target constraints, the cluster-head often has no ability to collect all the data of the terminal nodes. Therefore, a sparse model of terminal nodes is proposed, which is applied to the WSNs scenario. When the number of nodes to be collected is far beyond the ability to collect data, the sparse model is used to propose a distributed abnormal event detection scheme. Each cluster-head uses the compressed sensing method to collect the data. During the procedure, data collection rules are in accordance with the sparse parity check matrix of LDPC code. In the fusion center, the compressed sensing equations of these cluster-heads will be combined into a complete equation. Then the Message Passing algorithm based on Tanner Graph is used to reconstruct the abnormal event sensing results of the sensor nodes.

## A novel multi-LDPC-NPPM modulation coding scheme for satellite ground laser communications

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7875711
- **Type**: conference
- **Published**: 24-27 Sept
- **Authors**: Jing Liu, Qi Zhang, Qinghua Tian +8
- **PDF**: https://ieeexplore.ieee.org/document/7875711
- **Abstract**: An efficient modulation and coding scheme combined with multiple LDPC codes and PPM modulation is proposed to mitigate the effect of atmospheric turbulence, which can have an unfavorable impact on the reliability of the communication link in the laser channel of the integration network of satellite and ground. The research is mainly about the reliability of the communication link under different orders and parameters of the PPM modulation. The result shows that it can effectively enhance the link reliability if the system uses the scheme of 8PPM and 1/2 code rate binary LDPC coding under different turbulent intensity. Comparing and analyzing the scheme of binary and multiple LPDC coding system, we found that the scheme combined with the multiple LDPC codes and PPM modulation and coding is more efficient than binary LDPC codes related programs.

## Two-bit bit-flipping algorithm for decoding low-density parity-check codes based on syndrome weight

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7875795
- **Type**: conference
- **Published**: 24-27 Sept
- **Authors**: Hua Li, Liangjun Xiang, Linhua Zheng
- **PDF**: https://ieeexplore.ieee.org/document/7875795
- **Abstract**: In this paper, a novel two-bit bit-flipping (BF) decoding algorithm is proposed for low-density parity-check (LDPC) codes. The proposed algorithm flips two bits per iteration based on the syndrome-weight metric. Since the algorithm requires only logical operations during the iterations. The proposed tow-bit BF algorithm has low complexity. Simulation results show that the proposed algorithm has faster convergence speed and about 0.2 dB gain compared to standard BF decoding algorithm.

## Cooperative video coding scheme with fountain code on the concentration on data size

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7974592
- **Type**: conference
- **Published**: 23-25 Sept
- **Authors**: Hao Yu, Yumei Wang, Yu Liu
- **PDF**: https://ieeexplore.ieee.org/document/7974592
- **Abstract**: In wireless video broadcast system, Cooperative coding technique combines the cooperative communications with channel coding technique so as to guarantees high performance, which could bring better experience for users. But the high performance is as the cost of more bandwidth to serve more data size. In this paper, we propose a cooperative coding scheme using fountain code to decrease the data size we need to transport. We present the cooperative coding schemes with decode-forward (DF) mode. The experiment results show that this scheme decreases the data size that we need to transport compared with those using LDPC codes and improves the throughput.

## Lowering the error floor of short-to-medium length LDPC codes using optimal low-correlated-edge density (OED) PEG Tanner graphs

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7772157
- **Type**: conference
- **Published**: 22-24 Sept
- **Authors**: Umar-Faruk Abdu-Aguye, Marcel Adrian Ambroze, Martin Tomlinson
- **PDF**: https://ieeexplore.ieee.org/document/7772157
- **Abstract**: We propose a simple modification to the progressive edge-growth (PEG) algorithm in order to control the girth of low-density parity-check (LDPC) code Tanner graphs constructed. Using the modified algorithm, the edge densities in short irregular rate-% LDPC code graphs can be increased without increasing the correlation between edges in graphs by creating cycles of undesired length. Density evolution (DE) optimized symbol node degree distributions used for constructing short-to-medium length codes were further optimized (slightly altered) while maintaining the maximum edge correlation (minimum local girths) that exists in graphs constructed using the unaltered DE optimized distributions. As a result of improved degree sequences (and graph densities) which were derived, short-to-medium length LDPC codes with lower error floors than published for LDPC codes of identical length and rate were found. These slightly denser codes have lower error floor than codes constructed using DE optimized degree distributions in PEG algorithms modified for improved approximate cycle extrinsic message degrees (ACE). Simulation results show that, at a code length of 512, efficient irregular rate-% PEG codes have significantly lower error floors than a rate-% IEEE 802.16e (WiMAX) LDPC code of length 576.

## Design of spatially coupled LDPC codes based on symbolic hyper-graphs

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7772132
- **Type**: conference
- **Published**: 22-24 Sept
- **Authors**: Massimo Battaglioni, Marco Baldi, Giovanni Cancellieri
- **PDF**: https://ieeexplore.ieee.org/document/7772132
- **Abstract**: We consider a special family of spatially coupled low-density parity-check (LDPC) codes known as LDPC convolutional codes and propose a design technique based on symbolic hyper-graphs aimed at achieving good codes with small syndrome former memory order. We define conditions on the minimum syndrome former memory order that must be imposed in order to avoid short local cycles in the codes Tanner graphs and to achieve good minimum distance. Code design examples are provided, accompanied by error rate performance assessments based on Montecarlo simulations.

## A novel and efficient design of golay encoder for ultra deep submicron technologies

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7732059
- **Type**: conference
- **Published**: 21-24 Sept
- **Authors**: Chiranjeevi Sheelam, Jvr Ravindra
- **PDF**: https://ieeexplore.ieee.org/document/7732059
- **Abstract**: This paper lays out two different approaches for generation of binary golay code (23, 12). Namely, Linear feedback shift register (LFSR) based CRC and hardware architecture based on CRC. There are certain disadvantages associated with these two architectures. To overcome those disadvantages, a new architecture has been proposed for binary golay code (23, 12) generation. This paper also presents an efficient hardware architecture to generate extended golay code (24, 12). High speed, low latency, low area and low power architecture has been designed and verified.

## Novel UEP product code scheme with protograph-based linear permutation and iterative decoding for scalable image transmission

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7813407
- **Type**: conference
- **Published**: 21-23 Sept
- **Authors**: Huihui Wu, Sorina Dumitrescu
- **PDF**: https://ieeexplore.ieee.org/document/7813407
- **Abstract**: This paper introduces a linear permutation module before the inner encoder of the iteratively decoded product coding structure, for the transmission of scalable bit streams over error-prone channels1. This can improve the error correction ability of the inner code when some source bits are known from the preceding outer code decoding stages. The product code consists of a protograph low-density parity-check code (inner code) and Reed-Solomon (RS) codes of various strengths (outer code). Further, an algorithm relying on protograph-based extrinsic information transfer analysis is devised to design good base matrices from which the linear permutations are constructed. In addition, an analytical formula for the expected fidelity of the reconstructed sequence is derived and utilized in the optimization of the RS codes redundancy assignment. The experimental results reveal that the proposed approach consistently outperforms the scheme without the linear permutation module, reaching peak improvements of 1.98 dB and 1.30 dB over binary symmetric channels (BSC) and additive white Gaussian noise (AWGN) channels, respectively.

## A new AL-FEC coding scheme with limited feedback

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7813360
- **Type**: conference
- **Published**: 21-23 Sept
- **Authors**: Wei Huang, Hao Chen, Yiling Xu +2
- **PDF**: https://ieeexplore.ieee.org/document/7813360
- **Abstract**: For the next generation mobile video broadcasting, especially in-band solutions that serves the mobile devices, a limited feedback scheme via cellular channel polling is feasible to give accurate real-time information on the broadcast receivers' channel erasure rate, and decoding buffer status. In this work, we propose an AL-FEC coding degree scheme based on this feedback, to achieve a better decode efficiency and save the code redundancy. Simulation results demonstrate the effectiveness of this solution, and open up new opportunities in the next generation broadcasting system design.

## On link combining methods for highly reliable future wireless communication

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7600909
- **Type**: conference
- **Published**: 20-23 Sept
- **Authors**: Maciej Soszka, Meryem Simsek, Gerhard Fettweis
- **PDF**: https://ieeexplore.ieee.org/document/7600909
- **Abstract**: The future fifth generation (5G) wireless system is expected not only to provide high throughput and coverage but also to enable highly reliable and low-latency wireless connections that are required in mission critical use cases, e.g., machine-type communication or industrial automation. Robust and low-latency connection can be enabled by channel diversity in the frequency domain. Thus, we study various diversity combining methods and propose a novel combining scheme, which is based on Low-Density Parity-Check (LDPC) codes. This application of LDPC is studied, and the features of the desired LDPC code are highlighted. The results show that the diversity combining methods significantly gain reliability as compared to non-combining methods.

## Iterative frequency domain equalization combined with LDPC decoding for single-carrier underwater acoustic communications

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7761116
- **Type**: conference
- **Published**: 19-23 Sept
- **Authors**: Shunde Zhao, Xin Zhang, Xiaoji Zhang
- **PDF**: https://ieeexplore.ieee.org/document/7761116
- **Abstract**: This paper investigates the detection schemes for single-carrier underwater acoustic communications over the severe time-dispersive channels. A low-density parity-check (LDPC) code is employed for the improvement of the equalization performance. A detection scheme with Turbo conception is proposed which includes a LDPC decoder in the feedback loop of an iterative block decision feedback equalizer (IB-DFE), combining the iterative frequency domain equalization of IB-DFE with the iterative LDPC decoding. The external messages are fully exchanged between the IB-DFE and the decoder during the processing of the joint iterative equalization and decoding. The numerical results demonstrate that the decision signals with higher reliability from the LDPC decoder accelerate the convergence of the equalizer and enhance the detection performance, yielding up to 6 dB performance gains when compared with the scheme without LDPC code. Compared with the concatenated scheme in which the process of the iterative frequency domain equalization is serial concatenated with that of the iterative LDPC decoding, the combined scheme obtains about 2 dB performance gains.

## Simple adaptive progressive edge-growth construction of LDPC codes for close(r)-to-optimal sensing in pulsed ToF

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7745704
- **Type**: conference
- **Published**: 19-22 Sept
- **Authors**: Miguel Heredia Conde, Klaus Hartmann, Otmar Loffeld
- **PDF**: https://ieeexplore.ieee.org/document/7745704
- **Abstract**: In pulsed Time-of-Flight (ToF) systems the pulse width establishes a tradeoff between depth resolution and range. Ideally, one would wish to emit a pulse that is as short as allowed by the hardware, while keeping the depth range arbitrarily large, being able to sense more than one return per pixel. This suggests the use of compressive sensing (CS) as sensing paradigm, in order to exploit the sparsity of the light echo, s. Unfortunately, the best CS sensing matrices are dense matrices of random nature, thus expensive to generate and store when the signal dimensionality n (desired range over desired depth resolution) is high. The computational cost of the recovery also becomes prohibitive for large n. Additionally, dense matrices lead to measurements with poor SNR if the ratio s/n is too low or, conversely, require prohibitive amplitudes of the nonzero components. Deterministically-generated low-density parity-check (LDPC) sensing matrices can leverage these problems, but perform worse than random matrices if the density is too low compared to the sparsity. In this paper we present a simple method for deterministic construction of LDPC sensing matrices that builds upon progressive edge-growth (PEG) methods and integrates adaptiveness, that is, each new LDPC code is generated using information on the sparse signal captured by the previously-generated codes. Sensing matrices constructed via our adaptive PEG (APEG) algorithm exhibit superior sparse recovery performance than their PEG counterparts. If the density is appropriately adjusted (still low), APEG-LDPC matrices outperform classical CS random matrices.

## FPGA-accelerated simulation of a hybrid-ARQ system using high level synthesis

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7846753
- **Type**: conference
- **Published**: 19-21 Sept
- **Authors**: Swapnil Mhaske, Hojin Kee, Tai Ly +1
- **PDF**: https://ieeexplore.ieee.org/document/7846753
- **Abstract**: Physical layer processing for 5G wireless is expected to operate at a very high-throughput with very low latency. Developing a channel coding system based on Hybrid Automatic Repeat reQuest (HARQ) for evolving requirements necessitates extensive experimentation involving undesirably long development cycles. We demonstrate the use of a High-level Synthesis (HLS) compiler in LabVIEW Communications to prototype a real world HARQ system using Low-Density Parity-Check (LDPC) codes, however, without the expertise of an Hardware Description Language (HDL) designer. This implementation consumed 54% of the resources on our FPGA and allowed us to measure error-rate performance of the system over large, realistic data sets using accelerated, in-hardware simulation with a system throughput that is 4× greater than the CPU-based implementation. Furthermore, use of the HLS methodology significantly reduced time to explore the HARQ system parameter space and optimize in terms of error-rate performance and resource utilization.

## A novel video steganography algorithm in DCT domain based on hamming and BCH codes

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7846757
- **Type**: conference
- **Published**: 19-21 Sept
- **Authors**: Ramadhan J. Mstafa, Khaled M. Elleithy
- **PDF**: https://ieeexplore.ieee.org/document/7846757
- **Abstract**: In the past decade, the science of information hiding has gained tremendous significance due to advances in information and communication technology. The performance of any steganographic algorithm relies on the embedding efficiency, embedding payload, and robustness against attackers. Low hidden ratio, less security, and low quality of stego videos are the major issues of many existing steganographic methods. In this paper, we propose a novel video steganography method in DCT domain based on Hamming and BCH codes. To improve the security of the proposed algorithm, a secret message is first encrypted and encoded by using BCH codes. Then, it is embedded into the discrete cosine transform (DCT) coefficients of video frames. The hidden message is embedded into DCT coefficients of each Y, U, and V planes excluding DC coefficients. The proposed algorithm is tested under two types of videos that contain slow and fast moving objects. The experiential results of the proposed algorithm are compared with three existing methods. The comparison results show that our proposed algorithm outperformed other algorithms. The hidden ratio of the proposed algorithm is approximately 27.53%, which is considered as a high hiding capacity with a minimal tradeoff of the visual quality. The robustness of the proposed algorithm was tested under different attacks.

## Experimental Investigation of GF(3(exp 2)) Nonbinary LDPC-coded Non-uniform 9-QAM Modulation Format

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7769398
- **Type**: conference
- **Published**: 18-22 Sept
- **Authors**: Zhen Qu, Changyu Lin, Tao Liu +1
- **PDF**: https://ieeexplore.ieee.org/document/7769398
- **Abstract**: A specially designed GF(32) nonbinary LDPC-coded non-uniform 9-quadrature amplitude modulation (QAM) is proposed. The experimental and numerical results show that the proposed scheme outperforms nonbinary GF(2(exp 3)) LDPC-coded uniform 8-QAM by ~0.8-dB.

## Experimental Demonstration of Nonbinary LDPC Convolutional Codes for DP-64QAM/256QAM

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7767647
- **Type**: conference
- **Published**: 18-22 Sept
- **Authors**: Toshiaki Koike-Akino, Kenya Sugihara, David S. Millar +11
- **PDF**: https://ieeexplore.ieee.org/document/7767647
- **Abstract**: We show the great potential of nonbinary LDPC convolutional codes (NB-LDPC-CC) with low-latency windowed decoding. It is experimentally demonstrated that NB-LDPC-CC can offer a performance improvement of up to 5 dB compared with binary coding.

## On the Design of Capacity-Approaching Unit-Memory Spatially Coupled LDPC Codes for Optical Communications

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7767824
- **Type**: conference
- **Published**: 18-22 Sept
- **Authors**: Laurent Schmalen, Detlef Suikat, Vahid Aref +1
- **PDF**: https://ieeexplore.ieee.org/document/7767824
- **Abstract**: We consider unit-memory spatially coupled LDPC codes for optical communications. We analyze the region of wave-like convergence using an FPGA-based windowed decoding emulator. We show that the post-FEC errors occur in long bursts and highlight some design guidelines.

## Optimal Layered Scheduling for Hardware-Efficient Windowed Decoding of LDPC Convolutional Codes

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7767648
- **Type**: conference
- **Published**: 18-22 Sept
- **Authors**: Toshiaki Koike-Akino, Stark C. Draper, Ye Wang +6
- **PDF**: https://ieeexplore.ieee.org/document/7767648
- **Abstract**: We propose an optimal design method for layered scheduling in low-power windowed decoding of LDPC convolutional codes. Our optimal scheduling achieves up to a 70% complexity reduction and a 1 dB gain over conventional scheduling for limited decoding iterations.

## Scalable SD-FEC for Efficient Next-generation Optical Networks

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7767649
- **Type**: conference
- **Published**: 18-22 Sept
- **Authors**: Kenya Sugihara, Kenji Ishii, Keisuke Dohi +3
- **PDF**: https://ieeexplore.ieee.org/document/7767649
- **Abstract**: An SD-FEC has an even potential of a further optimization of a spectral efficiency and a power consumption in optical networks. A scalable SD-FEC is the key idea that improves efficiency of next-generation optical networks.

## High-spectral-efficiency transmission of PDM 256-QAM with Parallel Probabilistic Shaping at Record Rate-Reach Trade-offs

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7765586
- **Type**: conference
- **Published**: 18-22 Sept
- **Authors**: Sethumadhavan Chandrasekhar, Borui Li, Junho Cho +4
- **PDF**: https://ieeexplore.ieee.org/document/7765586
- **Abstract**: We demonstrate the transmission of near-optimal low-complexity probabilistically shaped PDM 256-QAM over multiple low-loss all-Raman amplified 50-km large effective area fiber spans, with spectral efficiencies from 14.1 b/s/Hz to 8.9 b/s/Hz at reaches from 500 km to 4000 km.

## Characterization of a Wavelength Converter for 256-QAM Signals Based on an AlGaAs-On-Insulator Nano-waveguide

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7767680
- **Type**: conference
- **Published**: 18-22 Sept
- **Authors**: Francesco Da Ros, Metodi P. Yankov, E. P. da Silva +9
- **PDF**: https://ieeexplore.ieee.org/document/7767680
- **Abstract**: High efficiency and broadband wavelength conversion in a 9-mm AlGaAs-On-Insulator waveguide is shown to provide high-quality (OSNR > 30 dB) idler generation over a 28-nm bandwidth enabling error-free conversion of 10-GBd 256-QAM with OSNR penalty below 2.5 dB.

## Experimental Demonstration of Physical-Layer Security in a Fiber-Optic Link by Information Scrambling

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7767751
- **Type**: conference
- **Published**: 18-22 Sept
- **Authors**: Junho Cho, Kyle Guan, Sethumadhavan Chandrasekhar +1
- **PDF**: https://ieeexplore.ieee.org/document/7767751
- **Abstract**: We experimentally demonstrate a physical-layer secure optical fiber communication link that prohibits an eavesdropper from detecting any useful information. Our classical approach is based on a simple linear feedback shift register, thus scaling to multi-Terabits/s of secure bit rates.

## Precoded Faster-than-Nyquist Coherent Optical Transmission

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7767726
- **Type**: conference
- **Published**: 18-22 Sept
- **Authors**: Mrinmoy Jana, Ahmed Medra, Lutz Lampe +1
- **PDF**: https://ieeexplore.ieee.org/document/7767726
- **Abstract**: In this paper we propose a novel symbol-by-symbol memoryless soft demapping method for coded coherent optical systems that employ Faster-than-Nyquist (FTN) transmission for improved spectral efficiency and Tomlinson-Harashima precoding for low-complexity equalization of FTN.

## Area-Efficient Fault-Tolerant Design for Low-Density Parity-Check Decoders

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7880909
- **Type**: conference
- **Published**: 18-21 Sept
- **Authors**: Bohua Li, Yukui Pei, Ning Ge
- **PDF**: https://ieeexplore.ieee.org/document/7880909
- **Abstract**: As technology moves into nano-realm, large area of the chip is especially vulnerable to single event upset (SEU) in space applications. In this paper, low cost fault-tolerant schemes are presented for the key modules of Low-Density Parity-Check (LDPC) code decoder to save logic resources. For counters, a fault-tolerant scheme based on m-sequence and Hamming coding is proposed, whereby the soft errors generated by SEUs can be located and corrected by a simple Hamming decoder. For RAM contents, we first propose a layered pipelined architecture absorbing LLR RAM into V2C RAM to reduce memory bits, which will lower the impact of SEUs. Then, a RAM hardening scheme is proposed, which only requires to detect soft errors by parity check, while the error correction is accomplished by decoder's own iterative decoding capability that has not been exploited sufficiently. Simulation results show that the proposed fault-tolerant counter could totally avoid SEUs and saves 42% of cell area compared with TMR method and the layered pipelined architecture saves 42% and 12% of memory bits compared with [4] and [15]. In addition, the hardened RAM cells will not cause extra bit errors when a soft error happens under the environments of high signal-to-noise ratio (SNR). The cost is only one parity bit for each RAM content, which is much less than conventional hardening schemes.

## LDPC Coded Angular Modulation Scheme for Cooperative Wireless Networks

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7881067
- **Type**: conference
- **Published**: 18-21 Sept
- **Authors**: Dushantha Nalin K. Jayakody
- **PDF**: https://ieeexplore.ieee.org/document/7881067
- **Abstract**: This paper investigates a new methodology for soft information forwarding (SIF) based on a novel technique known as soft angular modulation (SAM). In this new relay scheme, the soft symbols are embedded into phases at the relay. This is more advantageous as we refrain to forward real values (under bandwidth constraints) via wireless channels. This makes the proposed scheme practically feasible. The proposed system provides a means of using distributed low-density parity- check (LDPC) coding in conjunction with a new soft encoding scheme (puncturing), which is useful even under indigent source-relay link conditions. This also precludes the amplitudes of generated symbols descent to zero, as happens with most of the existing soft forwarding methods. Ordinarily, such schemes suffer from error propagation to the destination when the signal-to-noise ratio (SNR) of the source-relay link is low; however, our system avoids this problem by regenerating soft versions of the source symbols at the relay. Furthermore, we also propose a computationally efficient formula for log-likelihood ratio (LLR) at the destination. Simulation results demonstrate that the proposed scheme can maintain very good performance under poor source relay SNR conditions.

## Spatially-Coupled LDPC Coding in Threshold-Based Lossy Forwarding Scheme

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7881231
- **Type**: conference
- **Published**: 18-21 Sept
- **Authors**: Dushantha Nalin K. Jayakody, Eirik Rosnes
- **PDF**: https://ieeexplore.ieee.org/document/7881231
- **Abstract**: In this work, we propose a new technique of spatially-coupled low-density parity-check coding within a threshold-based lossy forwarding protocol for a multiple access relaying system. Here, block Rayleigh fading is assumed for all transmission links and error-free decoding at the relay is not required. Two schemes are presented in which the relay computes log-likelihood ratios (LLRs) of the network-coded symbols (from the sources) based on the received signals. By comparing the LLRs to a preset threshold, the relay decides to forward hard decisions when the network-coded symbol reliability is higher than the preset threshold. Otherwise, the relay decides to stay silent (first scheme) or to forward the LLRs to the destination (second scheme). Finally, we modify the LLR combining at the destination, based on an expression for the uncoded bit-error probability which is tailored to the proposed schemes. Simulation results demonstrate that the proposed relay protocol yields an improved bit-error rate performance compared to competitive schemes proposed in the literature.

## Construction of Polar Codes Concatenated to Space-Time Block Coding in MIMO System

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7880938
- **Type**: conference
- **Published**: 18-21 Sept
- **Authors**: Bowen Feng, Jian Jiao, Sha Wang +2
- **PDF**: https://ieeexplore.ieee.org/document/7880938
- **Abstract**: To enhance the performance in practical communications, a novel construction of polar code is designed for a rational polar and space-time block coding (Polar-STBC) system. The Polar-STBC system can be equivalent to a single transmission channel for each polar code bit in Rayleigh fading MIMO channels, and the equivalent channel can be regarded as a fading channel, of which the gain coefficient and additive noise are studied. Moreover, the distribution of the additive noise is also derived. Finally, we show that the bit error rate performance of our Polar-STBC system in 2 × 2, 4 ×⌉ 2 and 4 × 4 MIMOs.

## Time-Interleaved Block-Windowed Burst OFDM

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7881580
- **Type**: conference
- **Published**: 18-21 Sept
- **Authors**: Telmo Fernandes, Marco Gomes, Vitor Silva +1
- **PDF**: https://ieeexplore.ieee.org/document/7881580
- **Abstract**: The growing progress in wireless communication services lead to a demand in high data rates, spectral efficiency and flexibility requirements. The recently proposed Block-Windowed Burst Orthogonal Frequency Division Multiplexing (BWB-OFDM) transceiver proved to be a reliable alternative scheme to face these current demands. BWB-OFDM employs smoother, non- rectangular windows, allowing a power spectral density similar to the filtered OFDM approach; also, it packs together several OFDM symbols, with the addition of a sole zero- padding to accommodate the multipath channel's propagation delay. This means better overall power and spectral efficiencies. Nevertheless, the system has the same drawback of OFDM when transmitting over hostile channel conditions, such as deep fading in time-dispersive channels. To overcome this problem, a new Time-Interleaved BWB- OFDM (TIBWB- OFDM) transceiver is proposed. This scheme employs interleaving on the time-samples of each BWB- OFDM block, thus creating a sort of diversity at the frequency domain, aiming to preserve the data symbols severely corrupted by the channel's deep fades. The new TIBWB-OFDM transceiver presents considerable power gains relatively to the BWB-OFDM,while maintaining their spectral efficiency.

## A low-delay encoding algorithm of LT code for data loss recovery in telemetry systems

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7802838
- **Type**: conference
- **Published**: 13-16 Sept
- **Authors**: Jinrong Zhang, Ling Wu, Shengli Liu
- **PDF**: https://ieeexplore.ieee.org/document/7802838
- **Abstract**: A serially concatenated code is developed to guarantee reliable transmission of telemetry signals. The inner error correcting code is responsible for removing bit errors while the outer LT code plays the role of recovering data loss. Therefore, the serially concatenated code is able to provide reliability even though there exist bit errors and frame loss in telemetry links. However, the application of LT code to a telemetry system will bring a large system delay since a conventional LT encoder will not start to work until all source symbols are available. Aiming at reducing the system delay, an improved encoding algorithm of LT code is proposed. Different from the conventional LT encoder, the proposed LT encoder begins to generate coded symbols when it collects only a subset of source symbols. The coded symbol is generated as the modulo-2 addition of several source symbols which are selected from the available source symbols. The novelty of the new algorithm consists in the issue that how many source symbols and which source symbols are chosen to generate the coded symbol when only partial source symbols are available. The strategies of determining the degree of the coded symbol and the related source symbols are elaborately designed to make sure that the actualized degree distribution of coded symbols is very close to the predefined one and the actualized frequencies of selecting each source symbol are almost the same at the end of one block encoding. In addition, a reasonable encoding delay is necessary to ensure that coded symbols are transmitted in even rate and all source symbols can be recovered even though the telemetry channel is a fading channel with the maximum tolerable fade duration. Finally, the simulation of the proposed algorithm is implemented to obtain the encoding delay and the necessary encoding redundancy at different symbol loss ratio. The results demonstrate that the proposed algorithm can significantly reduce the encoding delay of a telemetry system at the cost of a slightly increase of the signal bandwidth compared with the conventional algorithm.

## NEXCODE: Next generation uplink coding techniques

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7802826
- **Type**: conference
- **Published**: 13-16 Sept
- **Authors**: M. Baldi, M. Bertinelli, F. Chiaraluce +10
- **PDF**: https://ieeexplore.ieee.org/document/7802826
- **Abstract**: NEXCODE is a project promoted by the European Space Agency aimed at research design development and demonstration of a receiver chain for telecomm and links in space missions including the presence of new short low-density parity-check codes for error correction. These codes have excellent performance from the error rate viewpoint but also put new challenges as regards synchronization issues and implementation. In this paper after a short review of the results obtained through numerical simulations we present an overview of the breadboard designed for practical testing and the test-plan proposed for the verification of the breadboard and the validation of the new codes and novel synchronization techniques under relevant operation conditions.

## Coding for space telemetry and telecommand transmissions in presence of solar scintillation

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7802831
- **Type**: conference
- **Published**: 13-16 Sept
- **Authors**: M. Baldi, F. Chiaraluce, N. Maturo +7
- **PDF**: https://ieeexplore.ieee.org/document/7802831
- **Abstract**: We discuss some of the results achieved in the RESCUe project funded by the European Space Agency whose goal is improving the reliability and capacity of radio links near superior conjunctions i.e. in the presence of phase and amplitude scintillation due to solar wind and solar corona. In this paper in particular the focus is on the error correcting codes that can be used to maintain acceptable values of the signal-to-noise ratio to achieve prefixed error rate targets even in the presence of very unfavorable propagation conditions. Both the cases of telemetry and telecommand are considered. We report several numerical results and propose a procedure to finalize the design in order to determine the maximum data rates achievable.

## Low-power analogue receiver ASIC for space telecommand applications

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7802824
- **Type**: conference
- **Published**: 13-16 Sept
- **Authors**: M. Bacci, F. Bigongiari, S. Chicca +10
- **PDF**: https://ieeexplore.ieee.org/document/7802824
- **Abstract**: An ASIC implementation of analogue receiver focused on telecommand applications for Category A missions (Return-to-Earth, lunar and even Lagrangian missions) is presented. In addition to embedded Low-Density Parity Check (LDPC) 128 bit analogue decoder, the ASIC integrates IF coherent demodulation, carrier tracking, clock recovery, SP-L to NRZ codify data conversion and telecommand-communication unit fields recognition. Start Frame pattern analogue recognition and 2-banks analogue memory for input codeword storing are embedded too. Operation with both decoder insertion and decoder in not-correcting mode is supported. The ASIC is manufactured in XFAB 0.18um technology and assembled in PGA100 package: the die size is 5326 × 3465 um2. The chip features almost constant parametric performances during continuous reception and decoding from a minimum dynamic power consumption of 151mW up to a maximum of 518mW, settable by external adjustable resistance. During no-reception static operation, power consumption can be decreased by selective stand-by commands on power-demanding blocks down to 82.5mW.

## Finite-length analysis for wireless super-dense networks exploiting coded random access over Rayleigh fading channels

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7811441
- **Type**: conference
- **Published**: 13-15 Sept
- **Authors**: Khoirul Anwar, Rina Pudji Astuti
- **PDF**: https://ieeexplore.ieee.org/document/7811441
- **Abstract**: This paper presents finite-length performance analysis for wireless super-dense networks comprising two multiway relays (SDN-2MWR) to support full data-exchange among massive number of users/devices over Rayleigh fading channels. In practice, finite-length analysis is important since the networks should serve users/devices with low latency indicated by short number of time-slots. Due to the nature of massive number of users/devices, where scheduling over massive number of users (usually in hundred or thousand) is difficult, we exploit random access with a capability of error correction resembling low density parity check (LDPC) codes. In this paper, we show that the dynamic of Rayleigh fading is even beneficial to generate two independent graphs captured by the first and the second relay without requiring all users send messages independently to each relay. Independent graphs are essential in SDN-2MWR to ensure the probability of successful decoding as high as possible and to significantly reduce error-floor in finite-length setting. Based on the theoretical network capacity bound indicating the maximum achievable traffic supported by the networks, we found that for SDN-2MWR a significant gain closer to the bound with lower packet-loss-rate (compared to the dense network with a single relay) is achievable without assuming ideal independent graph even with simple degree distributions without irregularity.

## Improving Belief Propagation decoding of polar codes using scattered EXIT charts

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7606802
- **Type**: conference
- **Published**: 11-14 Sept
- **Authors**: A. Elkelesh, M. Ebada, S. Cammerer +1
- **PDF**: https://ieeexplore.ieee.org/document/7606802
- **Abstract**: For finite length polar codes, channel polarization leaves a significant number of channels not fully polarized. Adding a Cyclic Redundancy Check (CRC) to better protect information on the semi-polarized channels has already been successfully applied in the literature, and is straightforward to be used in combination with Successive Cancellation List (SCL) decoding. Belief Propagation (BP) decoding, however, offers more potential for exploiting parallelism in hardware implementation, and thus, we focus our attention on improving the BP decoder. Specifically, similar to the CRC strategy in the SCL-case, we use a short-length “auxiliary” LDPC code together with the polar code to provide a significant improvement in terms of BER. We present the novel concept of “scattered” EXIT charts to design such auxiliary LDPC codes, and achieve net coding gains (i.e. for the same total rate) of 0.4dB at BER of 10-5 compared to the conventional BP decoder.

## The velocity of the propagating wave for general coupled scalar systems

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7606833
- **Type**: conference
- **Published**: 11-14 Sept
- **Authors**: Rafah El-Khatib, Nicolas Macris
- **PDF**: https://ieeexplore.ieee.org/document/7606833
- **Abstract**: We consider spatially coupled systems governed by a set of scalar density evolution equations. Such equations track the behavior of message-passing algorithms used, for example, in coding, sparse sensing, or constraint-satisfaction problems. Assuming that the “profile” describing the average state of the algorithm exhibits a solitonic wave-like behavior after initial transient iterations, we derive a formula for the propagation velocity of the wave. We illustrate the formula with two applications, namely Generalized LDPC codes and compressive sensing.

## On the block error rate performance of spatially coupled LDPC codes for streaming applications

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7606831
- **Type**: conference
- **Published**: 11-14 Sept
- **Authors**: David G. M. Mitchell, Ali E. Pusane, Michael Lentmaier +1
- **PDF**: https://ieeexplore.ieee.org/document/7606831
- **Abstract**: In this paper, we study the block error rate (BLER) performance of spatially coupled low-density parity-check (SC-LDPC) codes using a sliding window decoder suited for streaming applications. Previous studies of SC-LDPC have focused on the bit error rate (BER) performance or the frame error rate (FER) performance over the entire length of the code. Here, we consider protograph-based constructions of SC-LDPC codes in which a window decoder continuously outputs blocks in a streaming fashion, and we examine the BLER associated with these blocks. We begin by examining the effect of protograph design on the streaming BLER by varying the block size and the coupling width in such a way that the overall constraint length of the SC-LDPC code remains constant. Next, we investigate the BLER scaling behavior with block size and coupling width. Lastly, we consider the effect of employing an outer code to protect blocks, so that small numbers of residual errors can be corrected by the outer code. Simulation results for the additive white Gaussian noise channel (AWGNC) are included and comparisons are made to LDPC block codes (LDPC-BCs).

## Binary distributed hypothesis testing via Körner-Marton coding

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7606813
- **Type**: conference
- **Published**: 11-14 Sept
- **Authors**: Eli Haim, Yuval Kochman
- **PDF**: https://ieeexplore.ieee.org/document/7606813
- **Abstract**: We consider the problem of distributed binary hypothesis testing of two sequences that are generated by a doubly binary symmetric source. Each sequence is observed by a different terminal. The two hypotheses correspond to different levels of correlation between the two source components, i.e., the i.i.d. probability of the difference between the two sequences. The terminals communicate with a decision function via equal-rate noiseless links. We analyze the tradeoff between the exponential decay of the error probabilities of the hypothesis test and the communication rate. As Körner-Marton coding is known to minimize the rate in the corresponding distributed compression problem of conveying the difference sequence, it constitutes a natural candidate for the present setting. Indeed, using this scheme we derive achievable error exponents. Interestingly, these coincide with part of the optimal tradeoff without communication constraints, even when the rate is below the Körner-Marton rate for one of the hypotheses.

## Algebraic lattices achieving the capacity of the ergodic fading channel

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7606876
- **Type**: conference
- **Published**: 11-14 Sept
- **Authors**: Antonio Campello, Cong Ling, Jean-Claude Belfiore
- **PDF**: https://ieeexplore.ieee.org/document/7606876
- **Abstract**: In this work we show that algebraic lattices constructed from error-correcting codes achieve the ergodic capacity of the fading channel. The main ingredients for our construction are a generalized version of the Minkowski-Hlawka theorem and shaping techniques based on the lattice Gaussian distribution. The structure of the ring of integers in a number field plays an important role in the proposed construction. In the case of independent and identically distributed fadings, the lattices considered exhibit full diversity and an exponential decay of the probability of error with respect to the blocklength.
