# IEEE Xplore — 2011-12


## Cognitive Base Stations in LTE/3GPP Femtocells: A Correlated Equilibrium Game-Theoretic Approach

- **ID**: ieee:6042302
- **Type**: journal
- **Published**: December 2
- **Authors**: Jane Wei Huang, Vikram Krishnamurthy
- **PDF**: https://ieeexplore.ieee.org/document/6042302
- **Abstract**: This paper considers downlink spectrum allocation in a long term evolution (LTE) system macrocell which contains multiple femtocells. By incorporating cognitive capabilities into femtocell base stations, the Home evolved Node Bs (HeNBs) can be formulated as secondary base stations seeking to maximize the spectrum utility while minimizing interference to primary base stations (evolved Node-Bs). The competition amongst cognitive HeNBs for spectrum resources is formulated as a non-cooperative game-theoretic learning problem where each agent (HeNB) seeks to adapt its strategy in real time. We formulate the resource block (RB) allocation among HeNBs in the downlink of a LTE system using a game-theoretic framework, where the correlated equilibrium solutions of the formulated game are being investigated. A distributed RB access algorithm is proposed to compute the correlated equilibrium RB allocation policy..

## A Unified Framework for Linear-Programming Based Communication Receivers

- **ID**: ieee:6042890
- **Type**: journal
- **Published**: December 2
- **Authors**: Mark F. Flanagan
- **PDF**: https://ieeexplore.ieee.org/document/6042890
- **Abstract**: It is shown that a large class of communication systems which admit a sum-product algorithm (SPA) based receiver also admit a corresponding linear-programming (LP) based receiver. The two receivers have a relationship defined by the local structure of the underlying graphical model, and are inhibited by the same phenomenon, which we call pseudoconfigurations. This concept is a generalization of the concept of pseudocodewords for linear codes. It is proved that the LP receiver has the `maximum likelihood certificate' property, and that the receiver output is the lowest cost pseudoconfiguration. Equivalence of graph-cover pseudoconfigurations and linear-programming pseudoconfigurations is also proved. A concept of system pseudodistance is defined which generalizes the existing concept of pseudodistance for binary and nonbinary linear codes. It is demonstrated how the LP design technique may be applied to the problem of joint equalization and decoding of coded transmissions over a frequency selective channel, and a simulation-based analysis of the error events of the resulting LP receiver is also provided. For this particular application, the proposed LP receiver is shown to be competitive with other receivers, and to be capable of outperforming turbo equalization in bit and frame error rate performance.

## Multidimensional Hybrid Modulations for Ultrahigh-Speed Optical Transport

- **ID**: ieee:6059467
- **Type**: journal
- **Published**: Dec. 2011
- **Authors**: Ivan B. Djordjevic, Lei Xu, Ting Wang
- **PDF**: https://ieeexplore.ieee.org/document/6059467
- **Abstract**: From Shanon's theory, we know that information capacity is a logarithmic function of signal-to-noise ratio (SNR) but a linear function of the number of dimensions. By increasing the number of dimensions $D$, we can dramatically improve the spectral efficiency. At the same time, in $D$-dimensional space  $(D\ >\ 2)$, for the same average symbol energy, we can increase the Euclidean distance between signal constellation points compared with the conventional in-phase (I)/quadrature (Q) 2-D signal space. The 4-D space, with two phase coordinates per polarization, has already been intensively studied. To satisfy the ever-increasing bandwidth demands, in this paper, we propose the $D$ -dimensional signaling $(D\ >\ 4)$ by employing all available degrees of freedom for transmission over a single carrier including amplitude, phase, polarization, and orbital angular momentum (OAM). The proposed modulation scheme can be called hybrid $D$-dimensional modulation as it employs all available degrees of freedom. The proposed hybrid 8-D coded-modulation scheme outperforms its 4-D counterpart by 3.97 dB at a bit error rate (BER) of $10^{-8}$ while outperforming its corresponding polarization-division-multiplexed (PDM) iterative polar quantization (IPQ)-based counterpart by even a larger margin of 6.41 dB (at the same BER). The improvement of the proposed scheme for two amplitude levels per dimension and $D = 8$ over conventional PDM 64-quadrature amplitude modulation (QAM) is indeed a striking 8.28 dB at a BER of  $2 \times 10^{-8}$.

## Hardware Implementation of a Backtracking-Based Reconfigurable Decoder for Lowering the Error Floor of Quasi-Cyclic LDPC Codes

- **ID**: ieee:5954141
- **Type**: journal
- **Published**: Dec. 2011
- **Authors**: Xiaoheng Chen, Jingyu Kang, Shu Lin +1
- **PDF**: https://ieeexplore.ieee.org/document/5954141
- **Abstract**: Emerging applications such as flash-based storage systems and 10 gigabit Ethernet require that there is no error floor even at bit error rates as low as 10-12 or so. It has been found that trapping sets are responsible for the error floors of many LDPC codes with AWGN channels. This paper presents a hardware based backtracking scheme to break the trapping sets at runtime for lowering the error floor of quasi-cyclic LDPC codes. Backtracking is implemented as a self-contained module that can be interfaced to any generic reconfigurable iterative decoder for QC-LDPC codes. The backtracking module and a reconfigurable decoder are implemented with a FPGA and an 180 nm standard cell library. The results indicate that the overhead of backtracking is modest - about 5% in terms of logic and 13% in terms of memory for the first level backtracking and 14% in terms of logic and 46% in terms of memory for a two-level backtracking scheme. Furthermore, it is shown that the increase in latency due to backtracking is modest in the average case and can be controlled by the system designer by choosing the appropriate values for the number of trials and the number of iterations of the backtracking module.

## Joint Decoding of LDPC Codes and Finite-State Channels Via Linear-Programming

- **ID**: ieee:5993490
- **Type**: journal
- **Published**: Dec. 2011
- **Authors**: Byung-Hak Kim, Henry D. Pfister
- **PDF**: https://ieeexplore.ieee.org/document/5993490
- **Abstract**: This paper considers the joint-decoding problem for finite-state channels (FSCs) and low-density parity-check (LDPC) codes. In the first part, the linear-programming (LP) decoder for binary linear codes is extended to perform joint-decoding of binary-input FSCs. In particular, we provide a rigorous definition of LP joint-decoding pseudo-codewords (JD-PCWs) that enables evaluation of the pairwise error probability between codewords and JD-PCWs in AWGN. This leads naturally to a provable upper bound on decoder failure probability. If the channel is a finite-state intersymbol interference channel, then the joint LP decoder also has the maximum-likelihood (ML) certificate property and all integer-valued solutions are codewords. In this case, the performance loss relative to ML decoding can be explained completely by fractional-valued JD-PCWs. After deriving these results, we discovered some elements were equivalent to earlier work by Flanagan on linear-programming receivers. In the second part, we develop an efficient iterative solver for the joint LP decoder discussed in the first part. In particular, we extend the approach of iterative approximate LP decoding, proposed by Vontobel and Koetter and analyzed by Burshtein, to this problem. By taking advantage of the dual-domain structure of the joint-decoding LP, we obtain a convergent iterative algorithm for joint LP decoding whose structure is similar to BCJR-based turbo equalization (TE). The result is a joint iterative decoder whose per-iteration complexity is similar to that of TE but whose performance is similar to that of joint LP decoding. The main advantage of this decoder is that it appears to provide the predictability and superior performance of joint LP decoding with the computational complexity of TE. One expected application is coding for magnetic storage where the required block-error rate is extremely low and system performance is difficult to verify by simulation.

## Study of the Concatenation of Irregular LDPC Code with Equalizer of Low Complexity for 4G Mobile Wireless Network

- **ID**: ieee:6129697
- **Type**: journal
- **Published**: Dec. 2011
- **Authors**: W. Fernandez, R. Cifuentes, F. Rivera
- **PDF**: https://ieeexplore.ieee.org/document/6129697
- **Abstract**: The performance of a system of communication for 4G mobile wireless networks, using the irregular low density parity check code and equalizer of low complexity is studied. The transmitter uses the codification of irregular LDPC encoder, with low error floor. The receiver is composes of a sum product decoder and equalizer with a maximum algorithm probability estimation sequence which a big decrease of the probability of error of the system is achieved. The channel of transmission is an additive, white, Gaussian noise and fast fading with Rayleigh distribution. A speed of 150 Km/Hr to the mobile is considered.

## Investigation of Two-Dimensional Magnetic Recording (TDMR) With Position and Timing Uncertainty at 4 Tb/in$^{2}$

- **ID**: ieee:5765692
- **Type**: journal
- **Published**: Dec. 2011
- **Authors**: Euiseok Hwang, Rohit Negi, B. V. K. Vijaya Kumar +1
- **PDF**: https://ieeexplore.ieee.org/document/5765692
- **Abstract**: The feasibility of two-dimensional magnetic recording (TDMR) at 4 Tb/in2 customer areal-density is investigated via numerical simulations. In addition to the coding overhead needed to correct possible errors in a TDMR channel, the overhead required to obtain accurate position and timing estimates is taken into account in determining achievable customer density. The TDMR channel model used for this investigation is based on a random Voronoi granular medium, a two-dimensional (2-D) Gaussian read sensitivity function with random position and timing offsets and additive white Gaussian noise (AWGN). Read channel signal processing consists of a 2-D linear minimum mean square error (LMMSE) equalizer, a Gaussian mixture model (GMM) based log likelihood ratio (LLR) extractor and a low-density parity-check (LDPC) decoder. This work suggests that reliable performance may be achieved on media with 14 × 1012 grains/in2 by TDMR at a net customer areal-density of 0.29 bits per grain, including the overhead required for the LDPC code and the position and the timing fields.

## SigSag: Iterative Detection Through Soft Message-Passing

- **ID**: ieee:6025245
- **Type**: journal
- **Published**: Dec. 2011
- **Authors**: Arash Saber Tehrani, Alexandros G. Dimakis, Michael J. Neely
- **PDF**: https://ieeexplore.ieee.org/document/6025245
- **Abstract**: The multiple-access framework of ZigZag decoding (Gollakota and Katabi 2008) is a useful technique for combating interference via multiple repeated transmissions, and is known to be compatible with distributed random access protocols. However, in the presence of noise this type of decoding can magnify errors, particularly when packet sizes are large. We show that ZigZag decoding can be seen as an instance of belief propagation in the high signal-to-noise ratio (SNR) limit. Building on this observation, we present a simple soft-decoding version, called SigSag, that improves performance. We show that for two users, collisions result in a cycle-free factor graph that can be optimally decoded via belief propagation. For collisions between more than two users, we show that if a simple bit-permutation is used then the graph is locally tree-like with high probability, and hence belief propagation is near-optimal. Further, we introduce the joint channel-collision decoding which decodes the collided packets while the packets are coded by an LDPC code. Through simulations we show that our scheme performs better than coordinated collision-free time division multiple access (TDMA) and the ZigZag decoder. Furthermore, we investigate the performance of the joint channel-collision decoder in different scenarios and show that it performs better than TDMA and ZigZag decoder accompanied by sum-product decoding.

## SISO Detection Over Linear Channels With Linear Complexity in the Number of Interferers

- **ID**: ieee:6024433
- **Type**: journal
- **Published**: Dec. 2011
- **Authors**: Giulio Colavolpe, Dario Fertonani, Amina Piemontese
- **PDF**: https://ieeexplore.ieee.org/document/6024433
- **Abstract**: We consider detection over linear channels impaired by additive white Gaussian noise. For this general model, which describes a large variety of scenarios, novel detection algorithms are derived by applying the sum-product algorithm to a suitably designed factor graph. Being soft-input soft-output (SISO) in nature, the proposed detectors can be adopted in turbo processing without additional modifications. Among various applications, we focus on channels with known intersymbol interference, on frequency-division-multiplexed systems where adjacent signals are allowed to overlap in frequency to increase the spectral efficiency, and on code division multiple access systems. When compared with the existing interference-cancellation algorithms, the proposed schemes result very appealing in terms of tradeoff between performance and computational complexity. Particularly, the proposed schemes can approach or even outperform the performance provided by much more complex algorithms.

## Limits on Support Recovery of Sparse Signals via Multiple-Access Communication Techniques

- **ID**: ieee:6080743
- **Type**: journal
- **Published**: Dec. 2011
- **Authors**: Yuzhe Jin, Young-Han Kim, Bhaskar D. Rao
- **PDF**: https://ieeexplore.ieee.org/document/6080743
- **Abstract**: In this paper, we consider the problem of exact support recovery of sparse signals via noisy linear measurements. The main focus is finding the sufficient and necessary condition on the number of measurements for support recovery to be reliable. By drawing an analogy between the problem of support recovery and the problem of channel coding over the Gaussian multiple-access channel (MAC), and exploiting mathematical tools developed for the latter problem, we obtain an information-theoretic framework for analyzing the performance limits of support recovery. Specifically, when the number of nonzero entries of the sparse signal is held fixed, the exact asymptotics on the number of measurements sufficient and necessary for support recovery is characterized. In addition, we show that the proposed methodology can deal with a variety of models of sparse signal recovery, hence demonstrating its potential as an effective analytical tool.

## Iterative Tomographic Solution of Integer Least Squares Problems With Applications to MIMO Detection

- **ID**: ieee:6032063
- **Type**: journal
- **Published**: Dec. 2011
- **Authors**: Jacob Goldberger, Amir Leshem
- **PDF**: https://ieeexplore.ieee.org/document/6032063
- **Abstract**: Least squares (LS) fitting is one of the most fundamental techniques in science and engineering. It is used to estimate parameters from multiple noisy observations. In many problems the parameters are known a priori to be bounded integer valued, or they come from a finite set of values on an arbitrary finite lattice. Integer least squares is also an important problem in multichannel communication systems and GPS applications. In this case finding the closest vector becomes NP-hard problem. In this paper, we propose two novel algorithms, the Tomographic Least Squares Decoder (TLSD), that not only solves the ILS problem, better than other sub-optimal techniques, but can also provide the a posteriori probability distribution for each element in the solution vector and a belief propagation version termed two-dimensional belief propagation (2DBP). Both algorithms are based on reconstruction of the vector from multiple two-dimensional projections. The projections are carefully chosen to provide low computational complexity. We show that the projections are equivalent to the two-dimensional marginals of the soft zero forcing linear decoder. We also provide simulated experiments comparing the algorithm to other sub-optimal algorithms. We end with a discussion of possible extensions to coded systems and combinations with sphere decoding.

## Allocation of Computational Resources for Soft MIMO Detection

- **ID**: ieee:5961604
- **Type**: journal
- **Published**: Dec. 2011
- **Authors**: Mirsad Cirkic, Daniel Persson, Erik G. Larson
- **PDF**: https://ieeexplore.ieee.org/document/5961604
- **Abstract**: We consider soft multiple-input multiple-output (MIMO) detection for the case of block fading. That is, the transmitted codeword spans over several independent channel realizations and several instances of the detection problem must be solved for each such realization. We develop methods that adaptively allocate computational resources to the detection problems of each channel realization, under a total per-codeword complexity constraint. Our main results are a formulation of the problem as a mathematical optimization problem with a well-defined objective function and constraints, and algorithms that solve this optimization problem efficiently computationally.

## Channel State Feedback Over the MIMO-MAC

- **ID**: ieee:6094251
- **Type**: journal
- **Published**: Dec. 2011
- **Authors**: K. Raj Kumar, Giuseppe Caire
- **PDF**: https://ieeexplore.ieee.org/document/6094251
- **Abstract**: In order to exploit the full multiplexing gain of multi-antenna multi-user downlink schemes, accurate channel state information at the transmitter (i.e., at the base station) is required. We consider the design of a closed-loop channel state information feedback scheme, where user terminals feed back their channel state information simultaneously to a multi-antenna base station. The underlying information theoretic problem consists of lossy source-channel coding of multiple independent analog sources (i.e., the users' channel coefficients) over a Gaussian multiple-input multiple-output multi-access channel (MIMO-MAC). Unlike the classical source-channel coding setting, this application requires low latency, otherwise the channel state information would be outdated. Hence, source-channel codewords can span only a single fading state of the uplink (feedback) channel. Furthermore, the transmitters are ignorant of the realization of the uplink channel coefficients. In this scenario, the scaling of the maximum of the estimated downlink channel mean-square errors with the SNR dominates the performance of the multiuser downlink. This scaling is described by the distortion SNR exponent, previously introduced in a single-user MIMO setting. This paper analyzes the max-min distortion SNR exponent of the MIMO-MAC for both separated source-channel coding, and a particular hybrid digital-analog joint source-channel coding scheme. For the case of single-antenna users, we prove that the distortion SNR exponent of separated source-channel coding can be achieved by the concatenation of scalar quantization and uncoded quadrature-amplitude modulation (QAM) transmission, with lattice decoding at the base-station receiver. The resulting scheme has very low encoding latency (only a few symbols of the uplink slot) and generally outperforms currently proposed channel state feedback schemes based on analog unquantized transmission or vector quantization with fixed codebooks.

## Iterative Source–Channel Decoding With Reduced Error Floors

- **ID**: ieee:6009164
- **Type**: journal
- **Published**: Dec. 2011
- **Authors**: Laurent Schmalen, Peter Vary
- **PDF**: https://ieeexplore.ieee.org/document/6009164
- **Abstract**: Audio-visual source encoders for digital mobile communications extract parameters that-due to delay and complexity constraints-exhibit some residual redundancy. This residual redundancy can be exploited by iterative source-channel decoding (ISCD) to improve the robustness against transmission noise by performing soft parameter detection as part of the decoding process. Systems employing ISCD at the receiving end often exhibit an observable error floor. While this error floor can be tolerated in some cases, it is often desirable to perfectly reconstruct the source codec parameters. In this paper, we explain the reasons for the error floor and propose two solutions for realizing ISCD systems with optimized error floor performance while maintaining the desired near-capacity waterfall behavior. All approaches aim at optimizing the distance properties of the (redundant) mapping of bit patterns to the source codec parameters. In some cases, especially if small quantizer code books are employed, good mappings cannot be found-in this case, the novel multi-dimensional bit mapping allows to reduce the error floor after decoding.

## Quasi Cyclic-LDPC codes based on PEG algorithm with maximized girth property

- **ID**: ieee:6146165
- **Type**: conference
- **Published**: 7-9 Dec. 2
- **Authors**: Patanasak Prompakdee, Watid Phakphisut, Pornchai Supnithi
- **PDF**: https://ieeexplore.ieee.org/document/6146165
- **Abstract**: In this paper, we propose a method to construct parity-check matrices of Quasi Cyclic (QC) LDPC codes based on the progressive edge-growth (PEG) algorithm with maximized girth property. The proposed algorithm can eliminate short cycles and improve the decoding performance. Simulation results illustrate that the codes constructed with the proposed algorithm have superior performance to the previous PEG-QC codes over the additive white Gaussian noise (AWGN) channel. At the BER of 10-7, the coding gain of 0.005 dB.

## LDPC decoder with modified LLR for bit patterned media with write errors

- **ID**: ieee:6146112
- **Type**: conference
- **Published**: 7-9 Dec. 2
- **Authors**: Warangrat Wiriya, Watid Phakphisut, Pornchai Supnithi
- **PDF**: https://ieeexplore.ieee.org/document/6146112
- **Abstract**: Write-in error is a crucial issue that needs to be tackled in bit patterned media (BPM) recording. Previous works apply the low-density parity-check (LDPC) codes to improve the system performance and the write margin. However, LDPC codes are not designed for the write error channel (WEC). Therefore, the log-likelihood ratio (LLR) is modified at the LDPC decoder by incorporating the information write error probability (p) for the performance improvement. In practice, such probability is not precisely known, therefore, in this work, we investigate the effects of the mismatch of expected write error probability and the actual one in the BPM system. The results show that the performance of LDPC decoding is worse when p mismatches with the write error probability of the WEC.

## Construction of quasi-cyclic LDPC codes form SFT structure and cyclic shift

- **ID**: ieee:6146084
- **Type**: conference
- **Published**: 7-9 Dec. 2
- **Authors**: Sekson Timakul, Somsak Choomchuay
- **PDF**: https://ieeexplore.ieee.org/document/6146084
- **Abstract**: This paper presents an alternative a method for designing a parity matrix of low density parity check codes. The proposed method can be viewed as a generalized version of Sridara-Fuja-Tanner (SFT) technique which is ideal for regular quasi cyclic code design. Upon the current investigation, the designed code has delivered a comparable BER-SNR performance when compared with that of more complicate designed matrix. The designed code offers similar performance when compared with Sridara-Fuja-Tanner code and Quadratic Congruences structure. In additions, the resulted matrix also has a desirable structure that it suits well the hardware implementation.

## Distributed source coding: Theorem and its application to video coding

- **ID**: ieee:6146218
- **Type**: conference
- **Published**: 7-9 Dec. 2
- **Authors**: Takayuki Nakachi
- **PDF**: https://ieeexplore.ieee.org/document/6146218
- **Abstract**: Distributed Source Coding (DSC) implements inter source redundancy by encoding correlated information sources, without letting the sources communicate with each other. The DSC theorem states that the optimal rate achieved by joint encoding and decoding can be reached by separate encoding and joint decoding. Video coding based on the DCS theorem is Distributed Video Coding (DVC). DVC is attracting attention as a new paradigm for video compression. While conventional video coding schemes such as H.264/AVC reduce inter-frame redundancy at the encoder, DVC reduces inter-frame redundancy at the decoder by using distributed channel coding. The architecture suits applications that require low-complexity encoders. Examples of such applications include wireless video surveillance and mobile camera phones. In this paper, after describing the DSC theorem, we offer a survey of recent trends and problems in DVC and then introduce our contributions.

## Reduced-complexity modified per-survivor iterative timing recovery using M-algorithm for magnetic recording system

- **ID**: ieee:6146175
- **Type**: conference
- **Published**: 7-9 Dec. 2
- **Authors**: Chanon Warisarn, Pornchai Supnithi, Piya Kovintavewat
- **PDF**: https://ieeexplore.ieee.org/document/6146175
- **Abstract**: A modified per-survivor iterative timing recovery (MPS-ITR), which jointly performs timing recovery, equalization, and error-correction decoding, has been proposed in [1] to deal with the problem of timing recovery operating at low signal-to-noise ratio. Practically, this scheme exploits a split-preamble strategy in conjunction with a per-survivor soft-output Viterbi algorithm equalizer to make it more robust against severe timing jitters or cycle slips. Although the MPS-ITR outperforms other iterative timing recovery schemes [1], it still has very high complexity. In this paper, we propose a reduced-complexity MPS-ITR scheme (denoted as MPS-ITR-M) to make it more implementable in real-life applications. This is achieved by applying the M-algorithm [2] to the MPS-ITR. Numerical results indicate that at low-to-moderate complexity, the MPS-ITR-M will perform better than other schemes.

## Prioritized 3-D Video Transmission over Cooperative MIMO-OFDM Systems

- **ID**: ieee:6128686
- **Type**: conference
- **Published**: 6-8 Dec. 2
- **Authors**: Omar Hazim Salim, Wei Xiang
- **PDF**: https://ieeexplore.ieee.org/document/6128686
- **Abstract**: Multi-input multi-output (MIMO) systems with orthogonal frequency division multiplexing (OFDM), cooperative communication and three-dimensional (3-D) video coding are state-of-the-art techniques. The combination between cooperative and MIMO systems is crucial to provide high data rates with high quality of 3-D video services. By taking their advantages, this paper presents 3-D video transmission over cooperative MIMO-OFDM systems. Unequal error protection schemes are proposed to protect the 3-D video signal with different important levels. This is achieved by partitioning the compressed 3-D video sequences based on packets partitioning or sending the 3-D video signal with different levels of protection. A concatenating form of the rate-variable low-density parity-check (LDPC) codes and MIMO system based on diversity space-time block code (STBC) is employed, where the sum-product algorithm (SPA) is utilized for LDPC. For channel adaptation, a switching operation between UEP schemes is proposed to achieve a trade-off between performance of the 3-D video system and changes in the wireless channel. Simulation results demonstrate the effectiveness of proposed schemes.

## Joint Channel Estimation and Decoding of Root-LDPC Codes in Block-Fading Channels

- **ID**: ieee:6134331
- **Type**: conference
- **Published**: 5-9 Dec. 2
- **Authors**: Iryna Andriyanova, Ezio Biglieri, David Declercq
- **PDF**: https://ieeexplore.ieee.org/document/6134331
- **Abstract**: We study iterative receivers for joint decoding and channel-state estimation for transmission on block-fading channels of root- LDPC-coded signals. Root-LDPC codes are known to be most performant codes for block-fading channels, as their spacial "root" structure allows to get the full-diversity property. This property ensures a good error decoding performance of root LDPC codes, especially in contrast with the performance standard LDPC codes (having the maximum diversity equal to 1). However, as any channel code, root-LDPC codes also suffer from the diversity loss when the channel state information is not known at the receiver. In this work we propose a joint channel estimation- decoding scheme for root- LDPC codes that helps to overcome this problem and still to have the full-diversity.

## Soft Information for LDPC Decoding in Flash: Mutual-Information Optimized Quantization

- **ID**: ieee:6134417
- **Type**: conference
- **Published**: 5-9 Dec. 2
- **Authors**: Jiadong Wang, Thomas Courtade, Hari Shankar +1
- **PDF**: https://ieeexplore.ieee.org/document/6134417
- **Abstract**: High-capacity NAND flash memory can achieve high density storage by using multi-level cells (MLC) to store more than one bit per cell. Although this larger storage capacity is certainly beneficial, the increased density also increases the raw bit error rate (BER), making powerful error correction coding necessary. Traditional flash memories employ simple algebraic codes, such as BCH codes, that can correct a fixed, specified number of errors. This paper investigates the application of low-density parity-check (LDPC) codes which are well known for their ability to approach capacity in the AWGN channel. We obtain soft information for the LDPC decoder by performing multiple cell reads with distinct word-line voltages. The values of the word-line voltages (also called reference voltages) are optimized by maximizing the mutual information between the input and output of the multiple-read channel. Our results show that using this soft information in the LDPC decoder provides a significant benefit and enables us to outperform BCH codes over a range of block error rates.

## Enhancing Binary Images of Non-Binary LDPC Codes

- **ID**: ieee:6134315
- **Type**: conference
- **Published**: 5-9 Dec. 2
- **Authors**: Aman Bhatia, Aravind R. Iyengar, Paul H. Siegel
- **PDF**: https://ieeexplore.ieee.org/document/6134315
- **Abstract**: We investigate the reasons behind the superior performance of belief propagation decoding of non- binary LDPC codes over their binary images when the transmission occurs over the binary erasure channel. We show that although decoding over the binary image has lower complexity, it has worse performance owing to its larger number of stopping sets relative to the original non-binary code. We propose a method to find redundant parity-checks of the binary image that eliminate these additional stopping sets, so that we achieve performance comparable to that of the original non-binary LDPC code with lower decoding complexity.

## Performance Analysis of Enhanced Verification-Based Decoding for Packet-Based LDPC Codes over Binary Symmetric Channel

- **ID**: ieee:6133747
- **Type**: conference
- **Published**: 5-9 Dec. 2
- **Authors**: Bin Zhu, Defeng Huang, Sven Nordholm +1
- **PDF**: https://ieeexplore.ieee.org/document/6133747
- **Abstract**: In this paper, frame error rate (FER) performance of enhanced verification-based decoding algorithm (EVA) is investigated for packet-based low-density parity-check (LDPC) codes over binary symmetric channel (BSC). By taking the false verification into account, a recursive statistical model is proposed to analyze the FER performance based on the packet-level analysis. Simulation results demonstrate that the proposed model works for various packet sizes and channel parameters of practical interest with different verification constraints.

## Threshold of Protograph-Based LDPC Coded BICM for Rayleigh Fading

- **ID**: ieee:6133952
- **Type**: conference
- **Published**: 5-9 Dec. 2
- **Authors**: Thuy Van Nguyen, Aria Nosratinia, Dariush Divsalar
- **PDF**: https://ieeexplore.ieee.org/document/6133952
- **Abstract**: Protograph-based bit-interleaved coded modulation (BICM) provides an elegant way of designing coded modulation over Rayleigh faded channels, however, to date the available designs have been limited to specific modulations and the corresponding decoding thresholds have not been known for Rayleigh faded channels. In this work, we present a simple method for designing protograph-based BICM that is general and applies to any modulation, and furthermore we calculate the iterative decoding thresholds of the protograph codes while mapped to higher order modulations. This general coding framework can support not only multiple rates but also adaptive modulation. We report that certain families of protograph codes achieve a threshold within a gap of approximately 0.2 - 0.4 dB of BICM capacity limit across a wide range of rates and modulations.

## LDPC code design for the BPSK-constrained Gaussian wiretap channel

- **ID**: ieee:6162586
- **Type**: conference
- **Published**: 5-9 Dec. 2
- **Authors**: Chan Wong Wong, Tan F. Wong, John M. Shea
- **PDF**: https://ieeexplore.ieee.org/document/6162586
- **Abstract**: A coding scheme based on irregular low-density parity-check (LDPC) codes is proposed to send secret messages from a source over the Gaussian wiretap channel to a destination in the presence of a wiretapper, with the restriction that the source can send only binary phase-shift-keyed (BPSK) symbols. The secrecy performance of the proposed coding scheme is measured by the secret message rate through the wiretap channel as well as the equivocation rate about the message at the wiretapper. A code search procedure is suggested to obtain irregular LDPC codes that achieve good secrecy performance in such context.

## Protograph-Based Raptor-Like LDPC Codes for Rate Compatibility with Short Blocklengths

- **ID**: ieee:6134051
- **Type**: conference
- **Published**: 5-9 Dec. 2
- **Authors**: Tsung-Yi Chen, Dariush Divsalar, Jiadong Wang +1
- **PDF**: https://ieeexplore.ieee.org/document/6134051
- **Abstract**: This paper presents a new class of rate-compatible LDPC codes, protograph-based Raptor-like (PBRL) codes. The proposed PBRL codes are jointly decodable with an iterative belief propagation decoder. As with Raptor codes, additional parity bits can be easily produced by exclusive-or operations on the precoded bits, providing extensive rate compatibility. This paper provides a design procedure that optimizes this class of rate- compatible LDPC codes. The new PBRL codes outperform 3GPP rate-compatible turbo codes with the same short blocklength at high SNR and show no sign of an error floor at the FER region of 10-7.

## Noise Adaptive LDPC Decoding Using Expectation Propagation

- **ID**: ieee:6133838
- **Type**: conference
- **Published**: 5-9 Dec. 2
- **Authors**: Shuang Wang, Lijuan Cui, Samuel Cheng
- **PDF**: https://ieeexplore.ieee.org/document/6133838
- **Abstract**: Belief propagation (BP) is a powerful algorithm to decode low- density parity check (LDPC) codes over additive white Gaussian noise (AWGN) channels. However, the traditional BP algorithm cannot adapt efficiently to the statistical change of SNR in an AWGN channel. This paper proposes an adaptive scheme that incorporates expectation propagation (EP) into the BP based LDPC decoding process. The proposed scheme is able to perform online estimation of both stationary and time-varying SNR at the bit-level, and enhance the BP decoding performance simultaneously. Moreover, the proposed EP estimator shows a very fast convergence speed, and the additional computational overhead of the proposed decoder is less than 10% of the standard BP decoder.

## Efficient Algorithms to Find All Small Error-Prone Substructures in LDPC Codes

- **ID**: ieee:6133832
- **Type**: conference
- **Published**: 5-9 Dec. 2
- **Authors**: Xiaojie Zhang, Paul H. Siegel
- **PDF**: https://ieeexplore.ieee.org/document/6133832
- **Abstract**: Exhaustively enumerating all small error-prone sub structures in arbitrary, finite-length low-density parity-check (LDPC) codes has been proven to be NP-complete. In this paper, we present two exhaustive search algorithms to find such small error-prone substructures of an arbitrary LDPC code given its parity-check matrix. One algorithm is guaranteed to find all error-prone substructures including stopping sets, trapping sets, and absorbing sets, which have no more than αmax variable nodes and up to bmax induced odd-degree neighboring check nodes. The other algorithm is specially designed to find fully absorbing sets (FAS). Numerical results show that both of our proposed algorithms are more efficient in terms of execution time than another recently proposed exhaustive search algorithm [13]. Moreover, by properly initialization of the algorithm, the efficiency can be further improved for quasi-cyclic (QC) codes.

## On q-ary LDPC Code Design for a Low Error Floor

- **ID**: ieee:6134057
- **Type**: conference
- **Published**: 5-9 Dec. 2
- **Authors**: Andrea Marinoni, Pietro Savazzi, Richard D. Wesel
- **PDF**: https://ieeexplore.ieee.org/document/6134057
- **Abstract**: This paper explores protograph-based and ACE-based methods for constructing q-ary low-density parity-check (LDPC) matrices. The ACE approach maximizes approximate cycle extrinsic message degree, explicitly avoiding small q-ary stopping sets and implicitly avoiding small absorbing sets. In addition to ACE, this paper applies linear-dependent-set maximization (LDSM) to the binary image of the q-ary LDPC matrix. Performance is studied for binary and q-ary instances of erasure channels and additive white Gaussian noise channels. The combination of the ACE approach and LDSM provides dramatic error floor improvement for the binary erasure channel and both binary and q-ary AWGN channels.

## Non-Concatenated FEC Codes for Ultra-High Speed Optical Transport Networks

- **ID**: ieee:6133616
- **Type**: conference
- **Published**: 5-9 Dec. 2
- **Authors**: Damian A. Morero, M. Alejandro Castrillon, Facundo A. Ramos +3
- **PDF**: https://ieeexplore.ieee.org/document/6133616
- **Abstract**: This paper presents a non-concatenated forward error correction (FEC) code suitable for applications in 100Gb/s optical transport networks (OTN). A typical requirement in this application is a net coding gain (NCG) >10 dB at a bit error rate (BER) of 10^{-15} with an overhead (OH) of ~20%. As discussed in [1], non-concatenated codes are the ultimate frontier in terms of performance for OTN applications, because of their superior performance, lower latency, and lower overhead than concatenated codes. However, a major stumbling block for the use of these codes has been the existence of BER floors at levels significantly higher than the required 10^{-15} (typically 10^{- 10}). In this paper we present a new coding scheme based on a low density parity check (LDPC) code with an expected net coding gain of 11.30dB at 10^{-15}, 20% OH, and a block size of 24576 bits. This represents a significant improvement over the previous state of the art [2], based on a concatenated code with a block size of 74844 bits and 20.5% OH. The code is designed to minimize the BER floor while simultaneously reducing the memory requirements and the interconnection complexity of the iterative decoder [3]. Experimental results obtained with an FPGA-based hardware emulator demonstrate an NCG of 10.70 dB at a BER of 10^{-13} and no error floors. These experimental results are extrapolated to 10^{-15} using importance sampling techniques, resulting in the expected performance stated above. Moreover, we find that fixed-point implementation is the main cause of error floors below 10^{-13}. Based on this finding, we introduce a new low complexity postprocessing technique to push BER floors down to 10^{-15}.

## LLR Approximation for Wireless Channels Based on Taylor Series and Its Application to BICM with LDPC Codes

- **ID**: ieee:6133575
- **Type**: conference
- **Published**: 5-9 Dec. 2
- **Authors**: Reza Asvadi, Amir H. Banihashemi, Mahmoud Ahmadian-Attari +1
- **PDF**: https://ieeexplore.ieee.org/document/6133575
- **Abstract**: A new approach for the approximation of the channel log-likelihood ratio (LLR) for wireless channels based on Taylor series is proposed. The approximation is applied to the uncorrelated flat Rayleigh fading channel with unknown channel state information at the receiver. It is shown that the proposed approximation greatly simplifies the calculation of channel LLRs, and yet provides results almost identical to those based on the exact calculation of channel LLRs. The results are obtained in the context of bit-interleaved coded modulation (BICM) schemes with low-density parity-check (LDPC) codes, and include threshold calculations and error rate performance of finite-length codes. Compared to the existing approximations, the proposed method is either significantly less complex, or considerably more accurate.

## Stability of Iterative Decoding of Multi-Edge Type Doubly-Generalized LDPC Codes over the BEC

- **ID**: ieee:6134025
- **Type**: conference
- **Published**: 5-9 Dec. 2
- **Authors**: Enrico Paolini, Mark F. Flanagan, Marco Chiani +1
- **PDF**: https://ieeexplore.ieee.org/document/6134025
- **Abstract**: Using the EXIT chart approach, a necessary and sufficient condition is developed for the local stability of iterative decoding of multi-edge type (MET) doubly-generalized low-density parity-check (D-GLDPC) code ensembles. In such code ensembles, the use of arbitrary linear block codes as component codes is combined with the further design of local Tanner graph connectivity through the use of multiple edge types. The stability condition for these code ensembles is shown to be succinctly described in terms of the value of the spectral radius of an appropriately defined polynomial matrix.

## Adaptive Extended Min-Sum Algorithm for Nonbinary LDPC Decoding

- **ID**: ieee:6134511
- **Type**: conference
- **Published**: 5-9 Dec. 2
- **Authors**: Xuan Guan, Yunsi Fei
- **PDF**: https://ieeexplore.ieee.org/document/6134511
- **Abstract**: Low Density Parity Check (LDPC) codes over a Galois Field GF(q) can provide significantly better error- correcting quality than binary LDPC codes with moderate code length. However, the computational complexity and memory requirement of nonbinary codes are much higher, limiting the application of non- binary LDPC codes. In this paper, we propose an adaptive message truncation algorithm for non-binary LDPC decoding, guided by the estimated code error rates. Compared to the previous fixed message truncation method, it can cut the messages adaptively, and therefore provide better decoding quality and computation complexity reduction. To further reduce the computation, we propose another adaptive check node update algorithm, simplifying the decoding by reducing the number of check nodes updating. Our simulation results demonstrate that by combining these two algorithms together, the average message size can be reduced greatly and good decoding quality is achieved, at a little cost of iterations. Compared to the existing truncation algorithms, our approach can reduce the order of complexity to O(nalog2(na)) (where na is messages size), with less performance degradation.

## Progressive Coding and Iterative Source-Channel Decoding in Wireless Data Gathering Networks

- **ID**: ieee:6133958
- **Type**: conference
- **Published**: 5-9 Dec. 2
- **Authors**: Congduan Li, Paul G. Flikkema, Sheryl L. Howard
- **PDF**: https://ieeexplore.ieee.org/document/6133958
- **Abstract**: Wireless data gathering networks are often tasked to gather correlated data under severe energy constraints. The use of simple channel codes with source-channel decoding can potentially provide good performance with low energy consumption. Here we consider progressive coding in multi-hop networks, where an intermediate node decodes its received noisy codewords. The estimated information is concatenated with the node's own information word and encoded; the resulting progressively-encoded codeword is then transmitted to the next node. In non-progressive coding, the node simply forwards the received noisy codewords along with its own encoded data. Here we compare the performance of two codes with low decoding complexity, Repeat-Accumulate (RA) and Low-Density Parity-Check (LDPC) codes, in combination with two progressive coding schemes. Progressive channel coding uses only channel decoding at the intermediate node, while progressive source-channel coding uses source-channel decoding, exploiting the probabilistic dependency of the information words (caused by the correlation structure of the data) jointly with the deterministic dependency induced by channel coding. Two decoding schemes are considered at the data center: channel decoding only and iterative source-channel decoding. In simulation experiments, we consider a line network topology with systematic RA and LDPC coding. Results show that progressive coding performs better than non-progressive coding, and RA codes perform better with lower computational complexity than LDPC codes, both for channel-decoding-only and iterative source-channel decoding.

## High-Throughput Low-Power LDPC Decoder and Code Design

- **ID**: ieee:6134485
- **Type**: conference
- **Published**: 5-9 Dec. 2
- **Authors**: Thomas Henige, Shadi Abu-Surra, Eran Pisek
- **PDF**: https://ieeexplore.ieee.org/document/6134485
- **Abstract**: In this paper, we present a method for creating LDPC codes which are specifically designed to be hardware friendly. Our method involves constraining the cyclic shift values in the base H-matrix to reduce the complexity of the cyclic shift hardware. We show that the decoder hardware implementation for these codes has higher throughput and lower power consumption than decoders designed for traditional LDPC codes. We provide results showing that these codes maintain the error rate performance expected of LDPC codes while achieving these throughput and power consumption improvements.

## Concatenated Signal Codes with Applications to Compute and Forward

- **ID**: ieee:6134136
- **Type**: conference
- **Published**: 5-9 Dec. 2
- **Authors**: Nihat Engin Tunali, Krishna R. Narayanan
- **PDF**: https://ieeexplore.ieee.org/document/6134136
- **Abstract**: We present a new coding scheme based on concatenating a newly introduced class of lattice codes called signal codes with interleaved Low Density Parity Check (LDPC)codes. These codes are shown to possess a special algebraic structure which makes them suitable for recovering linear combinations (over a finite field) of the transmitted signals in a multiple access channel. This facilitates their use as a coding scheme for the recently proposed compute and forward paradigm. The decoding algorithm is based on an appropriate combination of the stack decoder with a message passing algorithm. Simulation results show that our proposed scheme can approach the uniform input AWGN capacity within 1.5 db, which is a 2 db improvement compared to using only signal codes when decoding using a stack algorithm with the same stack size. Simulation results for our proposed scheme applied to compute and forward are also presented.

## Channel Coding for IDM: High-Rate Convolutional Code Concatenated with Irregular Repetition Code

- **ID**: ieee:6133686
- **Type**: conference
- **Published**: 5-9 Dec. 2
- **Authors**: Meelis Noemm, Najeeb ul Hassan, Peter Adam Hoeher +1
- **PDF**: https://ieeexplore.ieee.org/document/6133686
- **Abstract**: Currently, combining turbo or low-density parity-check (LDPC) codes with bit-interleaved coded modulation (BICM) is the most common coding scheme for bandwidth-limited channels. However, in order to be capacity achieving, shaping is necessary, which is difficult in conjunction with iterative processing. An alternative is interleave-division multiplexing (IDM), which can be either treated as a coded modulation scheme or a multiplexing scheme. In IDM, coded data sequences are linearly superimposed, thus avoiding the necessity of active signal shaping. The characteristics of IDM can be controlled by power and phase allocation. With typical parameter settings, IDM is non- bijective. In that case, the main task of channel coding is aiding to resolve the data sequences ("layers") at the receiver side, whereas noise mitigation is a secondary task. In this paper, we demonstrate that classical channel codes (like LDPC and turbo codes) fail when applied with IDM. In fact, repetition coding is quite useful. It is shown by means of an EXIT chart analysis that a concatenation of a high-rate convolutional code with an irregular repetition code matches well with the characteristics of an IDM a posteriori probability (APP) demapper.

## A Multi-Level Design for Dirty-Paper Coding with Applications to the Cognitive Radio Channel

- **ID**: ieee:6134130
- **Type**: conference
- **Published**: 5-9 Dec. 2
- **Authors**: Momin Uppal, Guosen Yue, Yan Xin +2
- **PDF**: https://ieeexplore.ieee.org/document/6134130
- **Abstract**: We propose a close-to-capacity dirty-paper coding framework which employs multi-level low density parity-check (LDPC) and trellis coded quantization. The proposed coding framework is robust in the sense that it performs close to capacity in the high as well as the low rate regimes. This is in contrast to existing practical DPC schemes which perform well at one of these regimes, but never both. In order to evaluate the performance of our scheme, we consider its application to a cognitive radio channel. At a block length of 2 × 105, the designed dirty-paper coding scheme operates within 0.95, 0.58 and 0.6 dB of the theoretical limit at transmission rates of 0.5, 1.0 and 1.5 bits/sample, respectively. As far as the authors are aware, this is the best performance reported in the literature so far.

## Energy-Efficient Free-Space Optical Communication by Coded OAM Modulation

- **ID**: ieee:6133703
- **Type**: conference
- **Published**: 5-9 Dec. 2
- **Authors**: Ivan B. Djordjevic, Jaime Anguita, Bane Vasic
- **PDF**: https://ieeexplore.ieee.org/document/6133703
- **Abstract**: We study communication over atmospheric turbulence channels based on LDPC-coded signaling using multidimensional orbital angular momentum (OAM) signal constellations. Multidimensional signal constellation is obtained as the N-dimensional Cartesian product of a one-dimensional signal constellation originating from non-negative pulse-amplitude modulation. This scheme represents an energy efficient alternative, since a larger number of bits per symbol can be transmitted using a given bandwidth. We evaluate the performance of this scheme by determining conditional symbol probability density functions (PDFs) from numerical propagation data. Two cases are considered: (i) when conditional PDFs are known on the receiver side, and (ii) when conditional PDFs are not known and Gaussian approximation is used instead. We show that the OAM modulation is more sensitive to atmospheric turbulence as the number of dimensions increases. We also describe several applications of interest ranging from indoor wireless communications to intersatellite communications.

## Novel SISO Detection Algorithms for Nonlinear Satellite Channels

- **ID**: ieee:6134173
- **Type**: conference
- **Published**: 5-9 Dec. 2
- **Authors**: Giulio Colavolpe, Amina Piemontese
- **PDF**: https://ieeexplore.ieee.org/document/6134173
- **Abstract**: We propose novel detection algorithms for linear modulations transmitted over nonlinear satellite channels, also impaired by additive white Gaussian noise. These algorithms are derived by using a Volterra-series expansion of the useful signal and by applying the sum-product algorithm to a suitably-designed factor graph. Being soft-input soft-output (SISO) in nature, the proposed detectors can be adopted in turbo processing without additional modifications. Typical linear modulations employed in satellite transmissions are considered in the numerical results. When compared with the optimal detection algorithm for these channels, whose complexity is exponential in the channel memory, the proposed schemes result very appealing in terms of tradeoff between performance and computational complexity. Particularly, the proposed schemes can approach the optimal performance with a complexity only linear in the channel memory.

## Application Layer Joint Coding for Image Transmission over Deep Space Channels

- **ID**: ieee:6133825
- **Type**: conference
- **Published**: 5-9 Dec. 2
- **Authors**: Igor Bisio, Fabio Lavagetto, Mario Marchese
- **PDF**: https://ieeexplore.ieee.org/document/6133825
- **Abstract**: In this paper a method to realize the joint application layer coding for image transmission over deep space channels has been presented. In more technical detail, both image compression, based on algorithms such as JPEG2000 and CCSDS, and encoding techniques, such as LDPC codes, to protect the sent images are simultaneously applied by the proposed mechanism. It acts on the bases of the deep space channel conditions, in terms of Bit Error Rate, and it is based on the Multi-Attribute Decision Making theory. In practice, the proposal is aimed at protecting the essential informative contents of images sent through a deep space network and, at the same time, allows minimizing the load offered (the total amount of data to transmit) by the overall application layer coding process to the deep space network. The presented mechanism has been tested through simulations. The obtained results show the effectiveness of the proposal and open the door to further developments of the method in real systems.

## Iterative Cross-Entropy Encoding for Memory Systems with Stuck-At Errors

- **ID**: ieee:6134073
- **Type**: conference
- **Published**: 5-9 Dec. 2
- **Authors**: Euiseok Hwang, Balakrishnan Narayanaswamy, Rohit Negi +1
- **PDF**: https://ieeexplore.ieee.org/document/6134073
- **Abstract**: In this paper, a novel iterative encoding scheme is proposed for memory systems suffering from stuck-at errors. The stuck-at errors can be efficiently managed by using side information about stuck-at memory cells during encoding, while encoding for unconstrained number of stuck-at errors is intractable due to its exponential complexity. The proposed coding scheme employs an iterative encoding algorithm using cross-entropy method, which has a polynomial time complexity. In addition, any linear block code (LBC) can be concatenated with the proposed code, to correct for both residual stuck-at errors and random (soft) errors. The proposed coding schemes are evaluated by numerical simulations using a memory channel undergoing both stuck-at and random errors. Simulation results show that the cross-entropy based coding scheme provides an improved block error rate (BLER) performance, or alternatively, a higher overall storage capacity.

## Analysis of Mutual Information Based Soft Forwarding Relays in AWGN Channels

- **ID**: ieee:6133667
- **Type**: conference
- **Published**: 5-9 Dec. 2
- **Authors**: Md Anisul Karim, Jinhong Yuan, Zhuo Chen +1
- **PDF**: https://ieeexplore.ieee.org/document/6133667
- **Abstract**: In this paper, we analyze the error performance of the mutual information based forwarding (MIF) scheme for a memoryless parallel relay network in additive white Gaussian noise (AWGN) channels. The analytical expression for soft noise variance is first derived. Note that in the literature, the exact soft noise variance could only be evaluated by Monte Carlo simulation due to the lack of its analytical form. The derived soft noise variance expression only relies on the transmit signal-to-noise ratio (SNR), without the need to have the knowledge of actual or estimated information bits. With the expression of the soft noise variance, we derive an approximate bit error rate (BER) expression for a parallel relay network employing MIF scheme. The derived soft noise variance and system BER expressions are shown to be in tight match with Monte Carlo simulation results.

## Robust Reputation Management Using Probabilistic Message Passing

- **ID**: ieee:6133861
- **Type**: conference
- **Published**: 5-9 Dec. 2
- **Authors**: Erman Ayday, Faramarz Fekri
- **PDF**: https://ieeexplore.ieee.org/document/6133861
- **Abstract**: In a typical reputation management system, after each transaction, the buyer (who receives a service or purchases a product) provides its report/rating about the quality of the seller for that transaction. In such a system, the problem of reputation management is to compute two sets of variables: 1. the (global) reputation parameters of entities who act as sellers, and 2. the trustworthiness parameters of the entities who act as the raters (i.e., buyers). In this paper, for the first time, we introduce an iterative probabilistic method for reputation management. The proposed scheme, referred to as RPM, relies on a probabilistic message passing algorithm in the graph-based representation of the reputation management problem on an appropriately chosen factor graph. In the graph representation of the problem, the sellers and buyers are arranged as two sets of variable and factor nodes, respectively, that are connected via some edges. Then, the reputation and trustworthiness parameters are computed by a fully iterative and probabilistic message passing algorithm between these nodes in the graph. We provide a detailed evaluation of RPM via computer simulations. We observe that RPM iteratively reduces the error in the reputation estimates of the sellers due to the malicious raters. Finally, comparison of RPM with some well- known and commonly used reputation management techniques (e.g., Averaging Scheme, Bayesian Approach and Cluster Filtering) indicates the superiority of the proposed scheme both in terms of robustness against attacks (e.g., ballot-stuffing, bad-mouthing) and computational efficiency.

## Optimum and Suboptimum Combining of Independent Class-A Noise Channels

- **ID**: ieee:6133826
- **Type**: conference
- **Published**: 5-9 Dec. 2
- **Authors**: Stephen W. Lai, Geoffrey G. Messier
- **PDF**: https://ieeexplore.ieee.org/document/6133826
- **Abstract**: Optimum and suboptimum combining is investigated for a 2-branch diversity system containing unique Class-A noise in each branch. Expressions for log-likelihood ratio (LLR) reveal that the optimum scheme can be viewed as a linear combiner which is conditioned on the Class-A state. Bit-error rate (BER) performance curves for BPSK demonstrate that use of a saturated Gaussian metric for low-complexity signal combining results in good performance. However, maximal ratio combining (MRC) performs poorly due to mismatch between the MRC LLR and the LLR for optimum schemes.

## Efficient architecture design for mobile sensor networks

- **ID**: ieee:6123089
- **Type**: conference
- **Published**: 30 Nov.-1 
- **Authors**: Nabih Alaoui, Jean-Pierre Cances, Vahid Meghdadi
- **PDF**: https://ieeexplore.ieee.org/document/6123089
- **Abstract**: Optimizing architecture of sensor networks is a current topic of research. This research field can be applied in several contexts such as environmental monitoring or body area network. Performance improvement in terms of bit error rate is a major challenge. Reducing processing time and simplifying the operations of the network are the two main key points to be improved. A number of architectures have been designed to optimize the BER at destination. These architectures are mainly based on the LDPC codes (Low Density Parity Check) which have the disadvantage of the floor effect. The challenge is to find an optimal distribution of links between the sensors and relays to optimize the matrix H of the dual code and to avoid this floor effect. In this paper, we propose and simulate an efficient architecture for sensor network in a quasi-static Rayleigh fading channel environment. The new main idea is to enable communications between relays. Simulation results clearly show that the floor effect is significantly reduced with this kind of architecture.

## Distributed video coding with Multiple Reference Frame motion estimation

- **ID**: ieee:6182497
- **Type**: conference
- **Published**: 24-26 Dec.
- **Authors**: Rui Min, Le-nan Wu, Bao-min Qiao +1
- **PDF**: https://ieeexplore.ieee.org/document/6182497
- **Abstract**: Side information construction in Wyner-Ziv video coding plays an important role which strongly influences the final quality of restructured images. In this paper we proposed an Improved Backward Multiple Reference Frame (IBMRF) motion estimation algorithm, which obtained motion vector with hierarchical block matching method, and then adopted backward multiple reference frame motion compensated interpolation to generate the side information. The simulation results showed that the proposed algorithm achieves a significant improvement both in PSNR and in visual effect.

## Improved log domain decoding algorithm for LDPC codes over GF (q)

- **ID**: ieee:6164824
- **Type**: conference
- **Published**: 22-24 Dec.
- **Authors**: Md. Murad Hossain, Mohammad Rakibul Islam
- **PDF**: https://ieeexplore.ieee.org/document/6164824
- **Abstract**: An improved log domain decoding algorithm of Low density parity check (LDPC) codes over GF (q) using permutation to simplify the parity check equation is presented in this paper. This approach is different from the conventional log domain decoding algorithm of Low Density Parity Check (LDPC) codes over GF (q). The difference between improved log domain decoding and conventional log domain is that in improved log domain decoding permutation is applied in check node process where permutation is applied in between check node process and variable node process for conventional log domain decoding. Improved Log domain is mathematically equivalent to the conventional log domain decoding, however improved log-domain has advantages in terms of implementation, computational complexity and numerical stability. The proposed algorithm and the conventional log domain decoding algorithm are compared both in terms of memory requirement and simulated BER performance of (1008, 504) regular LDPC codes over GF (4) having row weight 3 & column weight 6, BPSK modulation.

## Combined normalized and offset extended min sum decoding algorithm for LDPC codes over GF (q)

- **ID**: ieee:6164866
- **Type**: conference
- **Published**: 22-24 Dec.
- **Authors**: Md. Murad Hossain, Mohammad Rakibul Islam
- **PDF**: https://ieeexplore.ieee.org/document/6164866
- **Abstract**: In this paper the combined normalized and offset extended min sum (EMS) is proposed for efficient decoding of non-binary low density parity check (LDPC) codes. EMS is the approximation of the sum product algorithm for reducing the computation complexity. However there is a performance gap between EMS and SP algorithm due to this approximation. The approximate check node messages of the extended min sum are compensated by both normalized and offset factor. The normalized factor and offset factor is determined for one iteration and is kept constant for all SNRs and iterations. It will shown in bit error rate simulation of (1008, 504) LDPC code over GF (4) that combined normalized offset extended min sum has superior performance than normalized and offset extended min sum. However, it requires only extra one multiplication for each cycle.

## Improved sub-block encoder of irregular LDPC code for image transmission

- **ID**: ieee:6147416
- **Type**: conference
- **Published**: 20-22 Dec.
- **Authors**: Tanaporn Payommai, Werapon Chiracharit, Kosin Chamnongthai
- **PDF**: https://ieeexplore.ieee.org/document/6147416
- **Abstract**: This paper presents irregular low-density parity-check (LDPC) code for image transmission system with any desired code lengths. Parity position of sub-block encoder is easily constructed over additive white Gaussian noise (AWGN) channel. The code is used as forward error correction (FEC) technique to protect transmitted source data over the channel. The sub-block encoder is designed with various AWGNs at three code lengths of 522, 2,021 and 4,183. The proposed irregular LDPC code reduces bit error when the code length increases. The performance is evaluated by bit error rate (BER) improvement 33.33% and peak signal-to-noise ratio (PSNR) more than 30 at SNR equals 7 dB.

## A new interconnection structure method for QC-LDPC codes

- **ID**: ieee:6150451
- **Type**: conference
- **Published**: 17-19 Dec.
- **Authors**: Farid Ghani, Abid Yahya, Md. Abdul Kader +1
- **PDF**: https://ieeexplore.ieee.org/document/6150451
- **Abstract**: A new technique for constructing the Quasi Cyclic Low density Parity Check (QC-LDPC) codes based on splitting rows into sub rows method is proposed. The proposed QC-LDPC code, at BER of 10-6 achieves 0.1dB coding gain over the PEG-LDPC codes. Moreover, in the high Eb / N0 region, the proposed code with girths 16 and 20 respectively, achieve 0.056 dB and 0.27 dB at a BER of 10-5 over the randomly constructed code. Simulation results portray that large girth QC-LDPC codes achieve a 0.1dB coding gain over randomly constructed codes and perform 1.3dB from the Shannon-limit at a BER of -6 with a code rate of 0.89 for block length of 1332.

## Low-complexity architecture design for modified WiMAX Low-Density Parity-Check codes

- **ID**: ieee:6174313
- **Type**: conference
- **Published**: 13-16 Dec.
- **Authors**: Kuang-Hao Lin, Meng-Yi Lin, Jan-Dong Tseng
- **PDF**: https://ieeexplore.ieee.org/document/6174313
- **Abstract**: In this paper, a modified WiMAX Low-Density Parity-Check (LDPC) codes for realistic LDPC coding system architectures is presented. The LDPC code, which is a special class of quasi-cyclic LDPC (QC-LDPC), has an efficient encoding algorithm owing to the simple structure of their parity-check matrices. A proposed distribution of irregular parity-check matrix for the modified WiMAX LDPC is developed so that we can obtain a low-complexity architecture design, and achievable circuit implementation. The modified WiMAX LDPC code decoding employs the iterative min-sum algorithm (MSA) and its decoder architecture design uses the bit node unit (BNU) and check node unit (CNU). Different word-length of hardware design for LDPC decoder can be simulated. Therefore, the word-length with 8-bit is enough for hardware implementation.

## A 6.72-Gb/s 8pJ/bit/iteration IEEE 802.15.3c LDPC decoder chip

- **ID**: ieee:6131868
- **Type**: conference
- **Published**: 12-14 Dec.
- **Authors**: Zhixiang Chen, Xiao Peng, Xiongxin Zhao +4
- **PDF**: https://ieeexplore.ieee.org/document/6131868
- **Abstract**: In this paper, we introduce an LDPC decoder design for decoding length-672 code adopted in IEEE 802.15.3c standard. The proposed decoder features high performance in both data rate and power efficiency. A macro-layer level fully parallel layered decoding architecture is proposed to support the throughput requirement in the standard. The decoder takes only 4 clock cycles to process one decoding iteration. While parallelism increases, the chip routing congestion problem becomes more severe because of the more complicated interconnection network used for message passing. This problem is nicely solved by our proposed efficient message permutation scheme utilizing the parity check matrix features. The proposed message permutation network features high compatibility and zero-logic-gate VLSI implementation, which contribute to the remarkable improvements in both area utilization ratio and total gate count. To verify the above techniques, the proposed decoder is implemented on a chip fabricated using Fujitsu 65nm 1P12L LVT CMOS process. The chip occupies a core area of 1.30mm2 with area utilization ratio 86.3%. According to the measurement results, working at 1.2V, 400 MHz and 10 iterations the proposed decoder delivers a 6.72Gb/s data throughput and dissipates a power of 537.6mW, resulting in an energy efficiency 8.0pJ/bit/iteration.

## Design of high-rate long-length structured QC-LDPC with good error performance

- **ID**: ieee:6140871
- **Type**: conference
- **Published**: 12-14 Dec.
- **Authors**: Xiong Yin, Zhaoxia Zheng, Yi Dan +1
- **PDF**: https://ieeexplore.ieee.org/document/6140871
- **Abstract**: In order to improve error performance of data storage, this paper presents a code-design algorithm for a class of structured quasi-cyclic low-density parity-check (SQC-LDPC) codes with high rate ( R >;= 0.9 ) and long-length (104 <; 60 n). In the design of parity-check matrix, optimized degree distribution pairs are obtained based on the combination of density evolution and differential evolution with a modified cost function. Moreover, both fewer short block-cycles and larger approximated cycle extrinsic message degree (ACE) are also considered. Simulation results indicate that codes in this design method its simulation curve is close to Shannon limit and have lower error floor.

## Digital baseband challenges for a 60GHz gigabit link

- **ID**: ieee:6122284
- **Type**: conference
- **Published**: 11-14 Dec.
- **Authors**: N. Kanistras, I. Tsatsaragkos, A. Mahdi +9
- **PDF**: https://ieeexplore.ieee.org/document/6122284
- **Abstract**: This paper presents the algorithms and corresponding hardware architectures developed in the context of the nexgen miliwave project, that compose the digital baseband processor of a 60GHz point-to-point link. The nexgen baseband processor provides all basic functionality required from a digital transmitter and receiver, including filtering, synchronization, equalization, and error correction. The techniques selected are capable of compensating impairments due to millimeter-wave front-end and yet support a throughput rate of more than one Gbp, with moderate hardware cost. As the nexgen link targets backhauling applications, a particularly low bit error rate specification of 10-12 has been adopted. Meeting the particular specification, as well as performance and complexity constraints, requires the adoption of sophisticated FEC techniques. Furthermore, extensive verification tasks need to be adopted which include hardware prototyping.
