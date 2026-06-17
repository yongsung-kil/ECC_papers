# IEEE Xplore — 2008-08


## Design Tradeoffs and Hardware Architecture for Real-Time Iterative MIMO Detection using Sphere Decoding and LDPC Coding

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:4586298
- **Type**: journal
- **Published**: August 200
- **Authors**: Hyungjin Kim, D.-U. Lee, John D. Villasenor
- **PDF**: https://ieeexplore.ieee.org/document/4586298
- **Abstract**: We explore the performance and hardware complexity tradeoffs associated with performing iterative multiple- input multiple-output (MIMO) detection using a sphere decoder and a low-density parity-check (LDPC) decoder. Iterations are performed both within the LDPC decoder as well as via an outer iteration loop through which refined soft information is fed back from the LDPC decoder to a MIMO detector. A hardware architecture and associated implementation results on Xilinx Virtex-5 field programmable gate array for a 4 x 4 QPSK MIMO system are presented. The system offers a performance improvement of approximately 1 dB over systems without the outer iteration loop, and provides an information bit throughput that ranges from 60 to 300 megabits per second when a length 1944 rate 1/2 LDPC code is used.

## LDPC Codes for Flat Rayleigh Fading Channels with Channel Side Information

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:4600168
- **Type**: journal
- **Published**: August 200
- **Authors**: Yibo Jiang, Alexei Ashikhmin, Naresh Sharma
- **PDF**: https://ieeexplore.ieee.org/document/4600168
- **Abstract**: In this paper, we design capacity approaching low- density parity-check (LDPC) codes in the low signal-to-noise ratio (SNR) regime for flat Rayleigh fading channels with channel side information at transmitter and receiver. We use the structure advocated by Caire et al, which uses a single codebook with dynamic power allocation. The extrinsic information transfer (EXIT) function method is used to design the LDPC codes which approach the channel capacities. We also study the EXIT function properties of various demappers.

## Combinatorial Interleavers for Systematic Regular Repeat-Accumulate Codes [Transactions Letters]

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:4600167
- **Type**: journal
- **Published**: August 200
- **Authors**: Sarah J. Johnson, Steven R. Weller
- **PDF**: https://ieeexplore.ieee.org/document/4600167
- **Abstract**: This paper proposes novel interleaver and accumulator structures for systematic, regular repeat-accumulate (RA) codes. It is well known that such codes are amenable to iterative (sum-product) decoding on the Tanner graph of the code, yet are as readily encodable as turbo codes. In this paper, interleavers for RA codes are designed using combinatorial techniques as a basis for deterministic interleaver constructions, yielding RA codes whose Tanner graphs are free of 4-cycles. Further, a generalized RA code accumulator structure is proposed, leading to codes, termed w3RA codes, whose parity-check matrices have many fewer weight-2 columns than conventional RA codes. The w3RA codes retain the low-complexity encoding of conventional RA codes and exhibit improved error-floor performance.

## Eliminating trapping sets in low-density parity-check codes by using Tanner graph covers

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:4567579
- **Type**: journal
- **Published**: Aug. 2008
- **Authors**: Milos Ivkovic, Shashi Kiran Chilappagari, Bane Vasic
- **PDF**: https://ieeexplore.ieee.org/document/4567579
- **Abstract**: We discuss error floor asympotics and present a method for improving the performance of low-density parity-check (LDPC) codes in the high SNR (error floor) region. The method is based on Tanner graph covers that do not have trapping sets from the original code. The advantages of the method are that it is universal, as it can be applied to any LDPC code/channel/decoding algorithm and it improves performance at the expense of increasing the code length, without losing the code regularity, without changing the decoding algorithm, and, under certain conditions, without lowering the code rate. The proposed method can be modified to construct convolutional LDPC codes also. The method is illustrated by modifying Tanner, MacKay and Margulis codes to improve performance on the binary symmetric channel (BSC) under the Gallager B decoding algorithm. Decoding results on AWGN channel are also presented to illustrate that optimizing codes for one channel/decoding algorithm can lead to performance improvement on other channels.

## A low-cost serial decoder architecture for low-density parity-check convolutional codes

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:4447002
- **Type**: journal
- **Published**: Aug. 2008
- **Authors**: Stephen Bates, Zhengang Chen, Logan Gunthorpe +3
- **PDF**: https://ieeexplore.ieee.org/document/4447002
- **Abstract**: We propose a low-cost serial decoder architecture for low-density parity-check convolutional codes (LDPC-CCs). It has been shown that LDPC-CCs can achieve comparable performance to LDPC block codes with constraint length much less than the block length. The proposed serial decoder architecture for LDPC-CCs uses a single decoding processor. Terminated data frames are sent through the processor iteratively until correctly decoded or a maximum number of iterations is reached. This architecture saves memory consumption and uses a very small number of logic elements, making it especially suitable for strong LDPC-CCs with large code memory. The proposed architecture is realized for a (2048,3,6) regular LDPC-CC on an Altera Stratix FPGA. With a maximum of 100 iterations, the design achieves up to 9-Mb/s throughput using only a very small portion of the field-programmable gate array resources.

## Power Reduction Techniques for LDPC Decoders

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:4578752
- **Type**: journal
- **Published**: Aug. 2008
- **Authors**: Ahmad Darabiha, Anthony Chan Carusone, Frank R. Kschischang
- **PDF**: https://ieeexplore.ieee.org/document/4578752
- **Abstract**: This paper investigates VLSI architectures for low-density parity-check (LDPC) decoders amenable to low- voltage and low-power operation. First, a highly-parallel decoder architecture with low routing overhead is described. Second, we propose an efficient method to detect early convergence of the iterative decoder and terminate the computations, thereby reducing dynamic power. We report on a bit-serial fully-parallel LDPC decoder fabricated in a 0.13-$\mu{\hbox{m}}$  CMOS process and show how the above techniques affect the power consumption. With early termination, the prototype is capable of decoding with 10.4 pJ/bit/iteration, while performing within 3 dB of the Shannon limit at a BER of 10$^{-5}$  and with 3.3 Gb/s total throughput. If operated from a 0.6 V supply, the energy consumption can be further reduced to 2.7 pJ/bit/iteration while maintaining a total throughput of 648 Mb/s, due to the highly-parallel architecture. To demonstrate the applicability of the proposed architecture for longer codes, we also report on a bit-serial fully-parallel decoder for the (2048, 1723) LDPC code in 10GBase-T standard synthesized with a 90-nm CMOS library.

## Probabilistic Analysis of Linear Programming Decoding

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:4567569
- **Type**: journal
- **Published**: Aug. 2008
- **Authors**: Constantinos Daskalakis, Alexandros G. Dimakis, Richard M. Karp +1
- **PDF**: https://ieeexplore.ieee.org/document/4567569
- **Abstract**: We initiate the probabilistic analysis of linear programming (LP) decoding of low-density parity-check (LDPC) codes. Specifically, we show that for a random LDPC code ensemble, the linear programming decoder of Feldman succeeds in correcting a constant fraction of errors with high probability. The fraction of correctable errors guaranteed by our analysis surpasses previous nonasymptotic results for LDPC codes, and in particular, exceeds the best previous finite-length result on LP decoding by a factor greater than ten. This improvement stems in part from our analysis of probabilistic bit-flipping channels, as opposed to adversarial channels. At the core of our analysis is a novel combinatorial characterization of LP decoding success, based on the notion of a flow on the Tanner graph of the code. An interesting by-product of our analysis is to establish the existence of ldquoprobabilistic expansionrdquo in random bipartite graphs, in which one requires only that almost every (as opposed to every) set of a certain size expands, for sets much larger than in the classical worst case setting.

## Mitigation of linear and nonlinear impairments in high-speed optical networks by using LDPC-coded turbo equalization

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:4588335
- **Type**: journal
- **Published**: Aug. 2008
- **Authors**: Ivan B. Djordjevic, Lyubomir L. Minkov, Hussam G. Batshon
- **PDF**: https://ieeexplore.ieee.org/document/4588335
- **Abstract**: We study a turbo equalization scheme based on low-density parity-check (LDPC) coded turbo equalization (TE). This scheme is suitable for simultaneous: (i) suppression of intra-channel nonlinearities, (ii) chromatic dispersion compensation, and (iii) polarization-mode dispersion (PMD) compensation. LDPC coding is based on large girth (g ges 8) block-circulant codes, and maximum a posteriori probability (MAP) equalizer is based on Bahl-Cocke-Jelinek-Raviv (BJCR) algorithm. The ultimate channel capacity limits, assuming an independent identically distributed (i.i.d.) source are reported as well. In the presence of intrachannel nonlinearities the LDPC-coded TE provides almost 12 dB improvement over BCJR equalizer at BER of 10-8. For an NRZ system operating at 10 Gb/s with residual dispersion of 11200 ps/nm and for differential group delay of 50 ps, the LDPC-coded TE is only 1 dB away from the i.i.d channel capacity. The efficiency of LDPC-coded TE in PMD compensation is demonstrated experimentally, with decoding performed off line.

## Rate-compatible distributed arithmetic coding

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:4601444
- **Type**: journal
- **Published**: Aug. 2008
- **Authors**: Marco Grangetto, Enrico Magli, Roberto Tron +1
- **PDF**: https://ieeexplore.ieee.org/document/4601444
- **Abstract**: Distributed arithmetic coding has been shown to be effective for Slepian-Wolf coding with side information. In this letter, we extend it to rate-compatible coding, which is useful in presence of a feedback channel between encoder and decoder. The performance loss with respect to the original version is negligible.

## An efficient algorithm for ML decoding of raptor codes over the binary erasure channel

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:4601445
- **Type**: journal
- **Published**: Aug. 2008
- **Authors**: Saejoon Kim, Seunghyuk Lee, Sae-Young Chung
- **PDF**: https://ieeexplore.ieee.org/document/4601445
- **Abstract**: In this letter, we propose an efficient algorithm for maximum-likelihood decoding of Raptor codes used over the binary erasure channel. The algorithm is inspired by the decoding scheme suggested in the 3GPP multimedia broadcast/multicast services standard and is an improved version of it.

## Stability analysis of an improved min-sum decoder

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:4601446
- **Type**: journal
- **Published**: Aug. 2008
- **Authors**: Mahdi Ramezani, Raman Yazdani, Masoud Ardakani
- **PDF**: https://ieeexplore.ieee.org/document/4601446
- **Abstract**: It has been shown that under min-sum (MS) decoding, scaling the messages at the output of check nodes can improve the performance of regular low-density parity-check (LDPC) codes. However, for irregular codes designed for the sum-product decoder, linear scaling can hinder the performance. The problem of code design for MS and linear scaling min-sum (LSMS) decoders have been recently investigated. It is shown that the gap to the capacity for LSMS codes is better than MS codes, but compared to sum-product codes the gap is still considerable. In this letter, a modified MS decoding is proposed and studied. We use the stability analysis of density evolution to show that the proposed method allows for a larger fraction of edges connected to degree-2 variable nodes than LSMS codes. Finally, by designing codes based on the modified method, we show that compared to MS and LSMS codes, a smaller gap to the capacity can indeed be achieved while the complexity of decoding remains essentially the same.

## Fixed-Complexity Soft MIMO Detection via Partial Marginalization

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:4520145
- **Type**: journal
- **Published**: Aug. 2008
- **Authors**: Erik G. Larsson, Joakim Jalden
- **PDF**: https://ieeexplore.ieee.org/document/4520145
- **Abstract**: This paper presents a new approach to soft demodulation for MIMO channels. The proposed method is an approximation to the exact a posteriori probability-per-bit computer. The main idea is to marginalize the posterior density for the received data exactly over the subset of the transmitted bits that are received with the lower signal-to-noise-ratio (SNR), and marginalize this density approximately over the remaining bits. Unlike the exact demodulator, whose complexity is huge due to the need for enumerating all possible combinations of transmitted constellation points, the proposed method has very low complexity. The algorithm has a fully parallel structure, suitable for implementation in parallel hardware. Additionally, its complexity is fixed, which makes it suitable for pipelined implementation. We also show how the method can be extended to the situation when the receiver has only partial channel state information, and how it can be modified to take soft-input into account. Numerical examples illustrate its performance on slowly fading 4 times 4 and 6 times 6 complex MIMO channels.

## A High-Throughput Maximum a Posteriori Probability Detector

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:4578762
- **Type**: journal
- **Published**: Aug. 2008
- **Authors**: Ruwan Ratnayake, Aleksandar Kavcic, Gu-Yeon Wei
- **PDF**: https://ieeexplore.ieee.org/document/4578762
- **Abstract**: This paper presents a maximum a posteriori probability (MAP) detector, based on a forward-only algorithm that can achieve high throughputs. The MAP algorithm is optimal in terms of bit error rate (BER) performance and, with Turbo processing, can approach performance close to the channel capacity limit. The implementation benefits from optimizations performed at both algorithm and circuit level. The proposed detector utilizes a deep-pipelined architecture implemented in skew-tolerant domino and experimentally measured results verify the detector can achieve throughputs greater than 750 Mb/s while consuming 2.4 W. The 16-state EEPR4 channel detector is implemented in a 0.13$\ \mu{\hbox {m}}$  CMOS technology and has a core area of 7.1  ${\hbox {mm}}^{2}$.

## Improved Data Detection Exploiting Full Cyclic Prefix for the Evolution of DVB-T

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:4600085
- **Type**: conference
- **Published**: 6-8 Aug. 2
- **Authors**: Lorenzo Vangelista, Marco Rotoloni, Alberto Morello
- **PDF**: https://ieeexplore.ieee.org/document/4600085
- **Abstract**: Orthogonal frequency division multiplexing (OFDM) has significantly reduced the complexity of the receivers, however to allow simple equalization procedures and avoid interblock interference, a cyclic prefix (CP) has to be appended to the OFDM block. CP reduces the efficiency of the transmission, because it is discarded at the receiver. This paper proposes a receiver structure which recovers the CP and exploits it to improve data detection. The performance of this structure is then analyzed comparing it with other two structures in a simulation scenario suitable for the evolution of the current Terrestrial Digital Video Broadcasting (DVB-T). The impact of low-density parity check codes (LDPC) is also outlined.

## Coding Schemes Applied to Peak-to-Average Power Ratio (PAPR) Reduction in OFDM Systems

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:4600038
- **Type**: conference
- **Published**: 6-8 Aug. 2
- **Authors**: Jyh-Horng Wen, Gwo-Ruey Lee, Chih-Chung Kung +1
- **PDF**: https://ieeexplore.ieee.org/document/4600038
- **Abstract**: High PAPR of the transmitted signal is a major drawback in the OFDM systems. In this paper, coding schemes are proposed to reduce high PAPR One is using parity check coding scheme, and the other is using selected mapping (SLM) applied scheme. With parity check coding scheme, the parity information is used to expand the signal space. Mapping from original source information to the corresponding message sequence with a low PAPR the PAPR of transmitted signal can be reduced. In the SLM applied scheme, a coding scheme with data position permutation and phase rotation is used. For the practical application to IEEE 802.11g, the performance of PAPR reduction is given. The simulation results show PAPR definitely can be greatly reduced with applying the SLM applied coding scheme in the OFDM system.

## A Construction of Linearly Encodable QC-LDPC Codes by Grouping Cyclic Shift and Block Elimination

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:4609695
- **Type**: conference
- **Published**: 3-4 Aug. 2
- **Authors**: Chen Zhixiong, Yuan Jinsha
- **PDF**: https://ieeexplore.ieee.org/document/4609695
- **Abstract**: In this paper, the girth and rank property based on grouping cyclic shift of a parity-check matrix is proved firstly. Then a quasi-cyclic square matrix with full rank is constructed by grouping cyclic shift and block elimination. By proper matrix extension, we construct a parity-check matrix based on the square matrix whose column weight is close or equal to three, which is suitable for efficient encoding procedure in [3][4][11] with a near linear complexity. Simulation results show a better performance compared to array based LDPC codes and LDPC codes in 802.11n standard.

## Implementation of LDPC Decoder in DVB-S2 Using Min-Sum Algorithm

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:4622852
- **Type**: conference
- **Published**: 28-30 Aug.
- **Authors**: Haeseong Jeong, Jong Tae Kim
- **PDF**: https://ieeexplore.ieee.org/document/4622852
- **Abstract**: A new market on digital broadcasting is opening because of the adoption of digital video broadcasting second generation as a digital broadcasting standard in Europe. The DVB-S2 uses a low density parity check, so DVB-S2 has much fast communication speed than conventional DVB which uses Reed-Solomon code and convolutional code for error correction. In this paper, we valuate performance and implement LDPC decoder of FEC which is important sub-system of DVB-S2 using VHDL. The simulated and implemented LDPC decoder is based on the min-sum algorithm.

## Efficient code construction of (3, k) Regular LDPC codes

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:4632040
- **Type**: conference
- **Published**: 26-28 Aug.
- **Authors**: Silvia Anggraeni, Varun Jeoti
- **PDF**: https://ieeexplore.ieee.org/document/4632040
- **Abstract**: The efficient code construction of regular LDPC codes that can effectively reduce the encoding complexity is still attracting a lot of attention from the research community. This paper presents a code construction method for (3, k) regular LDPC code that utilizes combination of a deterministic part and a partially random part in parity check matrix design. The parity check matrix (H), consisting of parity part (Hp) and information part (Hi), is so designed as to have a girth of, at least, 6 and to generate various code rates by maintaining the number of rows in H matrix while only changing the number of columns in the information part (Hi). Our code construction is able to reduce encoding complexity by avoiding any preprocessing step during encoding.

## Low-Complexity LDPC Codes with Near-Optimum Performance over the BEC

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:4620277
- **Type**: conference
- **Published**: 26-28 Aug.
- **Authors**: Enrico Paolini, Michela Varrella, Marco Chiani +2
- **PDF**: https://ieeexplore.ieee.org/document/4620277
- **Abstract**: Recent works showed how low-density parity-check (LDPC) erasure correcting codes, under maximum likelihood (ML) decoding, are capable of tightly approaching the performance of an ideal maximum-distance-separable code on the binary erasure channel. Such result is achievable down to low error rates, even for small and moderate block sizes, while keeping the decoding complexity low, thanks to a class of decoding algorithms which exploits the sparseness of the parity-check matrix to reduce the complexity of Gaussian elimination (GE). In this paper the main concepts underlying ML decoding of LDPC codes are recalled. A performance analysis among various LDPC code classes is then carried out, including a comparison with fixed-rate Raptor codes. The results confirm that a judicious LDPC code design allows achieving achieving a near-optimum performance on the erasure channel, with very low error floors. Furthermore, it is shown that LDPC and Raptor codes, under ML decoding, provide almost identical performance in terms of decoding failure probability vs. overhead.

## Short IRA Codes for Mobile DVB-RCS

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:4620274
- **Type**: conference
- **Published**: 26-28 Aug.
- **Authors**: Gianluigi Liva, Cristina Parraga Niebla, S. Scalise +4
- **PDF**: https://ieeexplore.ieee.org/document/4620274
- **Abstract**: In this paper, the design of the new short low-density parity-check introduced in the upcoming version of DVB-RCS standard targeting interactive mobile services will be described. The codes performance evaluation on the additive white Gaussian noise sand on a mobile (Rice-distributed) fading channels will be carried out assuming QPSK, 8PSK, 16APSK, and 32APSK modulations.

## Recovering from Packet Losses in CCSDS Links

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:4620278
- **Type**: conference
- **Published**: 26-28 Aug.
- **Authors**: Enrico Paolini, Michela Varrella, Marco Chiani +1
- **PDF**: https://ieeexplore.ieee.org/document/4620278
- **Abstract**: Data unit losses in deep space communications are currently faced using retransmission techniques which are however inefficient due to the large round trip delays. For this reason, the Consultative Committee for Space Data Systems (CCSDS) has recently considered packet erasure correcting codes for inclusion in its recommendations for space data system standards. Erasure correcting codes are expected to replace (or drastically reduce) retransmission requests. Erasure codes operate on packets instead of bits and are usually implemented above at the upper layers of the communication stack. In this paper, the implementation of erasure codes within the CCSDS communication stack is considered. Moreover, a comparison in terms of decoding complexity when using a maximum likelihood (ML) erasure decoder in the Control Center is performed between possible solutions, namely Raptor codes and low-density parity-check (LDPC) codes.

## Experimental Validation of Advanced Mobile Broadcasting Waveform in S-Band

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:4620255
- **Type**: conference
- **Published**: 26-28 Aug.
- **Authors**: A. Heuberger, H. Stadali, Balazs Matuz +6
- **PDF**: https://ieeexplore.ieee.org/document/4620255
- **Abstract**: Herein, the results of the ESA co-funded research project named "ORTIGIA" are summarized The scope of the project was to validate experimentally the techniques introduced by the DVB-SH working group to counteract fading in satellite and terrestrial environments. The experiments include measurements both on the field and in the laboratory.

## Random discrete measure of the phase posterior pdf in turbo synchronization

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:7080329
- **Type**: conference
- **Published**: 25-29 Aug.
- **Authors**: Nicolas Paul, Didier Le Ruyet, Tanya Bertozzi +1
- **PDF**: https://ieeexplore.ieee.org/document/7080329
- **Abstract**: In this paper we consider the iterative decoding of channels with strong phase noise. We propose to use a random discrete measure to estimate the phase posterior pdf given the past observations (forward pdf) and another random discrete measure to estimate the phase posterior pdf given the future observations (backward pdf). The particle filter algorithm is used to recursively generate the supports in the relevant phase space area and recursively update the weights associated to these supports. An estimation of the phase posterior pdf given all the past and future observations is then derived from the forward and backward measures. The relevance of our proposal is finally illustrated through simulation of binary LDPC codes and QPSK modulation over a severe Wiener-Levy phase noise with a standard deviation of πΔ = 6 degrees. Our algorithm is compared with a forward-backward message passing algorithm performed over a trellis resulting from the discretization of the phase. The proposed algorithm leads to a a slight performance degradation compared to the optimal treillis based method.

## Practical distributed source coding with impulse-noise degraded side information at the decoder

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:7080715
- **Type**: conference
- **Published**: 25-29 Aug.
- **Authors**: Claudio Weidmann, Francesca Bassi, Michel Kieffer
- **PDF**: https://ieeexplore.ieee.org/document/7080715
- **Abstract**: This paper introduces a practical method for distributed lossy compression (Wyner-Ziv quantization) with side information available only at the decoder, where the side information is equal to the signal affected by background noise and additional impulse noise. At the core of the method is an LDPC-based lossless distributed (Slepian-Wolf) source code for q-ary alphabets, which is matched to the impulse probability and allows to remove the scalar-quantized impulse noise. Applications of this method to distributed compressed sensing of signals that differ in a sparse set of locations is also discussed, as well as some differences and similarities of variable- and fixed-length coding of sparse signals.

## Lossless compression of encrypted grey-level and color images

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:7080641
- **Type**: conference
- **Published**: 25-29 Aug.
- **Authors**: Riccardo Lazzeretti, Mauro Barni
- **PDF**: https://ieeexplore.ieee.org/document/7080641
- **Abstract**: The feasibility of lossless compression of encrypted images has been recently demonstrated by relying on the analogy with source coding with side information at the decoder. However previous works only addressed the compression of bilevel images, namely sparse black and white images, with asymmetric probabilities of black and white pixels. In this paper we investigate the possibility of compressing encrypted grey level and color images, by decomposing them into bit-planes. A few approaches to exploit the spatial and cross-plane correlation among pixels are discussed, as well as the possibility of exploiting the correlation between color bands. Some experimental results are shown to evaluate the gap between the proposed solutions and the theoretically achievable performance.

## Analysis of error propagation due to frame losses in a distributed video coding system

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:7080668
- **Type**: conference
- **Published**: 25-29 Aug.
- **Authors**: Thomas Maugey, Thomas André, Béatrice Pesquet-Popescu +1
- **PDF**: https://ieeexplore.ieee.org/document/7080668
- **Abstract**: In this paper, we propose a theoretical model for the error propagation phenomenon generated by a frame loss in a distributed video coding framework. Using rate-distortion functions, we analyze the impact of a frame loss on the average distortion of a group of pictures depending on the position of the lost frame within the GOP, as well as the level of motion in each frame and the quantization errors in the key frames and the Wyner-Ziv frames. This theoretical analysis is further confirmed by a practical implementation of the DVC framework using different configurations of frame losses.

## The F-LDPC Family: High-Performance Flexible Modern Codes for Flexible Radio

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:4621434
- **Type**: conference
- **Published**: 25-28 Aug.
- **Authors**: Thomas R. Halford, Metin Bayram, Cenk Kose +2
- **PDF**: https://ieeexplore.ieee.org/document/4621434
- **Abstract**: Flexibility is an increasingly important aspect of radio modern design. In this paper, flexibility within the physical (PHY) layer in general, and the forward error correction (FEC) component in particular, is examined in detail. Following a discussion of the need for flexible modern code designs that exhibit universally good performance across a wide range of operational scenarios (i.e., input block size, code rate, modulation), TrellisWare Technologies, Inc.'s Flexible Low-Density Parity- Check (F-LDPC) codes are offered as an example of a high- performance modern coding solution for flexible radio designs. Specifically, the F-LDPC family offers performance within 0.8 dB of theoretical bounds across a wide range of operational scenarios with a design that is especially amenable to low-complexity, high- thoughput reconfigurable hardware implementation.

## Convolutional codes for iterative decoding

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:4621512
- **Type**: conference
- **Published**: 25-28 Aug.
- **Authors**: Michael Lentmaier, Gerhard P. Fettweis, Kamil Sh. Zigangirov +1
- **PDF**: https://ieeexplore.ieee.org/document/4621512
- **Abstract**: This paper gives an overview of three different classes of convolutional codes that are suitable for iterative decoding. They are characterized by the type of component codes that are used to construct the overall codes, which can be trivial parity-check constraints, block component codes, or convolutional component codes. Distance properties and iterative decoding performance are considered. All three classes of codes are asymptotically good, allow simple encoding, and can be decoded efficiently using iterative pipeline decoding architectures.

## Adapted LDPC Error Correction Scheme for 2D Optical CDMA Multimedia System

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:4621510
- **Type**: conference
- **Published**: 25-28 Aug.
- **Authors**: Stephanie Sahuguede, Anne Julien-Vergonjanne, Jean-Pierre Cances
- **PDF**: https://ieeexplore.ieee.org/document/4621510
- **Abstract**: To provide multimedia services in optical networks, 2 dimensional optical code division multiple access (2D OCDMA) system is considered as a potential solution. We focus here on a 2D OCDMA system using 2D multi-weight codes and parallel mapping technique to provide respectively quality of service (QoS) and data rate differentiation. To improve the performance of such a scheme, we investigate forward error correction (FEC) based on low density parity check (LDPC) codes known to have an efficient error correction power for Gaussian channels. We particularly propose an adaptation of the LDPC decoding scheme to the 2D OCDMA multimedia channel which has a specific noise distribution due to multiple access interference (MAI). We evaluate the system robustness to additive white Gaussian noise (AWGN) perturbation in addition to MAI and the gain provided in term of SNR. Finally, we show that the adapted FEC scheme we propose, not only permits improving the data rate per service but also the number of simultaneously communicating users.

## Soft Detection of Modulation Diversity Schemes for Next Generation Digital Terrestrial Television

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:4621429
- **Type**: conference
- **Published**: 25-28 Aug.
- **Authors**: Alberto Vigato, Stefano Tomasin, Lorenzo Vangelista +2
- **PDF**: https://ieeexplore.ieee.org/document/4621429
- **Abstract**: The next generation of digital terrestrial television (DVB-T2) standard requires to improve performance of the current DVB-T standard. Commercial and technical reasons suggest that orthogonal frequency division multiplexing (OFDM) could still be adopted. As multiple-input multiple-output antennas techniques are not backward compatible with current constellations, new modulation methods suitable for OFDM in the presence of Rayleigh fading channels could be developed in order to provide diversity gain without spectral or power inefficiencies. In this paper we compare three modulation methods, namely, (1) re-mapped repetition, (2) rotational multi-carrier and (3) multidimensional rotated QAM, in a low-density parity-check (LDPC) block code scenario. As most of the modulation methods were introduced for an uncoded scenario, indeed it is seen that in the presence of coding, the bit error rate deeply differs from that in an uncoded scenario.

## On the Growth Rate of Irregular GLDPC Codes Weight Distribution

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:4621513
- **Type**: conference
- **Published**: 25-28 Aug.
- **Authors**: E. Paolini, M. Chiani, M. Fossorier
- **PDF**: https://ieeexplore.ieee.org/document/4621513
- **Abstract**: In this paper the exponential growth rate of irregular generalized low-density parity-check (GLDPC) codes weight distribution is considered. Specifically, the Taylor series of the growth rate is expanded to the first order with the purpose of studying its behavior in correspondence with the small weight codewords. It is proved that the linear term of the Taylor series, and then the expected number of small linear-sized weight codewords of a randomly chosen GLDPC code in the irregular ensemble, is dominated by the degree-2 variable nodes and by the check nodes with minimum distance 2. A parameter is introduced, only depending on such variable and check nodes, discriminating between an exponentially small and exponentially large expected number of small weight codewords.

## Multiuser Detection Algorithm for CDMA Based on the Belief Propagation Algorithm

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:4621400
- **Type**: conference
- **Published**: 25-28 Aug.
- **Authors**: Shunsuke Horii, Tota Suko, Toshiyasu Matsushima +1
- **PDF**: https://ieeexplore.ieee.org/document/4621400
- **Abstract**: Optimum detection for the multiuser code-division multiple-access channel is prohibitively complex. This paper considers new iterative multiuser detection algorithm based on the belief propagation algorithm. Previously, the idea to apply the belief propagation algorithm to multiuser detection problem was suggested , however, it was believed that to apply the belief propagation algorithm to the detection problem is impossible because it requires an exponentially large amount of computation. It was the only fact that the parallel interference canceller is derived as an approximation of the belief propagation. In this paper, we show that the belief propagation algorithm can be applied to the detection problem by converting the factor graph structure. Performance of the detector based on the belief propagation algorithm is better than that of the parallel interference canceller.

## Reconfigurable Architecture for LDPC and Turbo Decoding: A NoC Case Study

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:4621490
- **Type**: conference
- **Published**: 25-28 Aug.
- **Authors**: Michelangelo Scarpellino, Ashwani Singh, Emmanuel Boutillon +1
- **PDF**: https://ieeexplore.ieee.org/document/4621490
- **Abstract**: Trends in wireless communication systems are in the direction of multi-mode systems using different algorithms to implement the baseband processing and the channel decoding. Efficient implementation of such multi-mode support requires flexible hardware. We present design and implementation of a reconfigurable processing element for a multi-processor architecture catering to both turbo and LDPC decoding needs in the context of the WiMaX (IEEE 802.16e) standard for high-throughput applications. As a case study, we evaluate the performance of our Multi Processor System on Chip (MPSoC) architecture for a 2-D Torus/Mesh interconnect topology. Evaluation results are presented based on the communication centric parameters that include network latency, network size and can be extended to any other System on Chip (SoC) interconnect topology without loss of generality.

## Hybrid decoding for one class of low-density parity-check codes

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:4685036
- **Type**: conference
- **Published**: 25-27 Aug.
- **Authors**: Guangwen Li, Xuelan Zou, Xin Wang
- **PDF**: https://ieeexplore.ieee.org/document/4685036
- **Abstract**: For high rate LDPC codes with light column weight and few redundant checks in their parity check matrix, the belief propagation (BP) decodings yield good error performance at the cost of high complexity. Aiming at seeking a effective decoder with good performance versus complexity tradeoff for this kind of LDPC codes, we present a new decoding framework which cascades a bit flipping (BF) variant with the ordered statistic decoding (OSD). During the iterative decoding of BF variant, the flipping value for each codeword bit is summed. The summation for each bit will be utilized as the reliability input for the OSD postprocessing, if no valid codeword is found after the maximum number of iterations for the BF variant is reached. With respect to the BP, simulation results show that the proposed BF-OSD achieves comparable performance with much less complexity.

## Construction of quantum low density parity check code based on quasi-cyclic sparse sequence

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:4685067
- **Type**: conference
- **Published**: 25-27 Aug.
- **Authors**: Sheng-mei Zhao, Bao-yui Zheng, Wan-nai Wang
- **PDF**: https://ieeexplore.ieee.org/document/4685067
- **Abstract**: In this paper, a construction method of quantum low density parity check codes (quantum LDPC) which based on classical quasi-cyclic sparse sequence is proposed, and the quantum code QLDPC(3,8)(16,6) and QLDPC(3,8)(64,24) are selected as examples to illustrate this construction method. The performances of this kind quantum LDPC codes are discussed over the bit-flipping channel by numerical simulations. The results show that these quantum codes have good ability to correct error in quantum channel.

## A decoding algorithm for low-density parity-check codes in impulse noise environment

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:4685174
- **Type**: conference
- **Published**: 25-27 Aug.
- **Authors**: Zhijiang Xu, Limin Meng, Li Gang +1
- **PDF**: https://ieeexplore.ieee.org/document/4685174
- **Abstract**: The iterative message passing algorithm (MPA) for low-density parity-check (LDPC) codes is effective in the additive white Gaussian noise (AWGN) channels. However, the impulse interference is not negligible in many communication channels, such as power line channels, where the impulse interference greatly deteriorates the performance of MPA based on Gauss optimization. It is necessary to restudy the decoding for LDPC codes in impulse environment. We introduce symmetric alpha-stable (SαS) noise into a statistical model of impulse noise environment, and consider that interference in the receiver is a mixture of AWGN and SαS noise. Based on this noise model, we analyze the probability density function (PDF) of the mixed noise through the numerical calculation method, and propose a robust MPA (RMPA) to account for the impulse environment. The simulations show that the bit error rate (BER) performance of the proposed RMPA is robust.

## EXIT-chart-based power allocations for superposition multilevel coding systems

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:4685037
- **Type**: conference
- **Published**: 25-27 Aug.
- **Authors**: Xiuni Wang, Xiao Ma
- **PDF**: https://ieeexplore.ieee.org/document/4685037
- **Abstract**: Multilevel coding with sigma-mapping is one simple way to obtain coding gain as well as shaping gain, while power-allocation, by allocating proper powers to different levels, can facilitate the iterative decoding/detection algorithms. In this paper, we utilize the EXIT chart to calculate the convergence threshold for each level by treating the signals from other levels as Gaussian noise. Based on the threshold, we propose a simple power allocation scheme. Numerical results show that the proposed EXIT-based power allocation scheme improves the performance when compared with the existing Gaussian approximation power allocation scheme while still keeping a reasonable complexity.

## Modified min-sum decoding algorithm for LDPC codes based on classified correction

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:4685176
- **Type**: conference
- **Published**: 25-27 Aug.
- **Authors**: Zhou Zhong, Yunzhou Li, Xiang Chen +2
- **PDF**: https://ieeexplore.ieee.org/document/4685176
- **Abstract**: In this paper, a modified min-sum decoding algorithm based on classified correction is proposed for low density parity check (LDPC) codes. Different from the single correction in the normalized belief propagation (BP)-based and offset BP-based algorithms [4], the proposed algorithm utilizes two corrections for both minimum and sub-minimum magnitudes of input messages in check nodes. These two correction factors can be obtained by analyzing the offset of updated messages in check nodes between the BP and the min-sum algorithms associated with check node degree. Simulation results show that the proposed algorithm can achieve performance very close to that of the BP algorithm. Furthermore, the FPGA implementation of this algorithm can reach a throughput of 200 Mbps at BER=10-6 with lower complexity and fewer resources than the BP algorithm.

## Constructing linear codes with good joint spectra

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:4685175
- **Type**: conference
- **Published**: 25-27 Aug.
- **Authors**: Shengtian Yang, Yan Chen, Thomas Honold +2
- **PDF**: https://ieeexplore.ieee.org/document/4685175
- **Abstract**: The problem of finding good linear codes for joint source-channel coding (JSCC) is investigated in this paper. By the code-spectrum approach, it has been proved in the authors' previous paper that a good linear code for the authors' JSCC scheme is a code with a good joint spectrum, so the main task in this paper is to construct linear codes with good joint spectra. First, the code-spectrum approach is developed further to facilitate the calculation of spectra. Second, some general principles for constructing good linear codes are presented. Finally, we propose an explicit construction of linear codes with good joint spectra based on low density parity check (LDPC) codes and low density generator matrix (LDGM) codes.

## Security Research on an Information-Theoretically Secure Secret Key Agreement Using LDPC Matrices

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:4624489
- **Type**: conference
- **Published**: 20-22 Aug.
- **Authors**: Jia Yu, Yuan Luo, Minglu Li
- **PDF**: https://ieeexplore.ieee.org/document/4624489
- **Abstract**: Secret key agreement is a major task in network security solutions using secret-key cryptosystems. An information-theoretically secure secret key agreement protocol using LDPC matrices was introduced by Jun Muramatsu. In this paper, the enemy can obtain not only full transmitted messages but also partial side information. We are interested in the equivocation of the generated key to this more powerful enemy. A relation between the security of the secret key agreement protocol and the LDPC matrices used in it is also discussed.

## Low-Complexity Real-Time LDPC Encoder Design for CMMB

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:4604260
- **Type**: conference
- **Published**: 15-17 Aug.
- **Authors**: Peng Wang, Yong-en Chen
- **PDF**: https://ieeexplore.ieee.org/document/4604260
- **Abstract**: Based on modified LU decomposition theory with pivoting of sparse matrix, a low-complexity real-time LDPC encoder for CMMB was presented, which can support 2 different code rate (1/2 and 3/4). Multi- staged pipeline and Pingpong buffer architectures were used to improve throughput. An efficient memory organization for storing sparse matrices was also presented. Whole design was synthesized and routed on Altera Stratix II EP2S90. Highest frequency achieved over 200 MHz, with pure encoding rate 32.44 Mbps (1/2 code rate) and 67.16 Mbps (3/4 code rate). Beside, fully-parameterized LDPC encoder can support arbitrary H matrix LDPC code with only necessary initialized data of memory blocks.

## A low power layered decoding architecture for LDPC decoder implementation for IEEE 802.11n LDPC codes

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:5529042
- **Type**: conference
- **Published**: 11-13 Aug.
- **Authors**: Jie Jin, Chi-Ying Tsui
- **PDF**: https://ieeexplore.ieee.org/document/5529042
- **Abstract**: This paper presents a low power LDPC decoder design based on reducing the amount of memory access. By utilizing the column overlapping of the LDPC parity check matrix, the amount of access for the memory storing the posterior values is minimized. In addition, a thresholding decoding scheme is proposed which reduces the memory access by trading off the error correcting performance. The decoder was implemented in TSMC 0.18μm CMOS process. Experimental results show that for a LDPC decoder targeting for IEEE 802.11n, the power consumption of the memory and the decoder can be reduced by 72% and 24%, respectively.

## Flexible decoder architectures for irregular QC-LDPC codes

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:4616778
- **Type**: conference
- **Published**: 10-13 Aug.
- **Authors**: Tzu-Chieh Kuo, Alan N. Willson
- **PDF**: https://ieeexplore.ieee.org/document/4616778
- **Abstract**: A flexible and power-efficient decoder architecture employing the layered-decoding message-passing algorithm and the low-complexity offset-based Min-Sum check algorithm for irregular QC-LDPC codes is presented in this paper. The architecture is verified by implementing a programmable decoder chip compliant with the QC-LDPC codes in Mobile WiMAX standard. Compared to other published decoder implementations, the prototype decoder is 53% smaller and has better energy efficiency.
