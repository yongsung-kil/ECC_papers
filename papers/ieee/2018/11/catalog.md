# IEEE Xplore — 2018-11


## Reduced Complexity Window Decoding of Spatially Coupled LDPC Codes for Magnetic Recording Systems

- **ID**: ieee:8401538
- **Type**: journal
- **Published**: Nov. 2018
- **Authors**: Sirawit Khittiwitchayakul, Watid Phakphisut, Pornchai Supnithi
- **PDF**: https://ieeexplore.ieee.org/document/8401538
- **Abstract**: Spatially coupled low-density parity-check (SC-LDPC) codes have emerged to possess capacity-approaching performance. The SC-LDPC codes can be decoded by a sliding window, therefore, the decoding latency and complexity of SC-LDPC codes are lower than those of underlying LDPC codes when the codeword length is very large. In this paper, the SC-LDPC decoder with the sliding window is employed in turbo equalization of magnetic recording systems. We examine the bit error rates (BERs) of the output of the sliding window during the iterative decoding, and then observe that the consecutive code blocks have approximately the same BERs. Herein, to reduce decoding complexity of SC-LDPC codes, the consecutive code blocks can be considered as the output of SC-LDPC codes. In addition, the non-uniform schedule update is adopted in the window decoding to avoid unnecessary updates within a window. The simulation results show that the proposed decoding algorithms applied in bit-patterned media magnetic recording systems can achieve a significant reduction in complexity compared to the traditional decoding without any loss in BER performance.

## Memory-Reduced Non-Binary LDPC Decoding With Accumulative Bubble Check

- **ID**: ieee:8063902
- **Type**: journal
- **Published**: Nov. 2018
- **Authors**: Injun Choi, Ji-Hoon Kim
- **PDF**: https://ieeexplore.ieee.org/document/8063902
- **Abstract**: Non-binary (NB) low-density parity check (LDPC) codes offer stronger error correcting capability than binary LDPC codes. However, the improvement is accompanied by a considerable increase in the decoding complexity and a huge memory requirement, especially in the check node (CN). To overcome these limitations, we propose a memory-reduced NB-LDPC decoding method with an accumulative bubble check (a-bubble check) algorithm. The proposed a-bubble check reduces the memory requirements of the CNs by using the differences between the log-likelihood ratio entries. In addition, we propose a non-uniform memory structure to further decrease the memory capacity of the CN processor. For the GF(64)(160, 80) NB-LDPC code, the proposed memory-reduced NB-LDPC decoding architecture achieves a memory requirement reduction of 32.4% for the CNs and 16.2% for the entire decoder without degrading the error correction capability.

## Spatially-Coupled Codes for Channels with SNR Variation

- **ID**: ieee:8424449
- **Type**: journal
- **Published**: Nov. 2018
- **Authors**: Homa Esfahanizadeh, Ahmed Hareedy, Ruiyi Wu +2
- **PDF**: https://ieeexplore.ieee.org/document/8424449
- **Abstract**: In magnetic recording systems, consecutive sections experience different signal-to-noise ratios (SNRs). To perform error correction over these systems, one approach is to use an individual block code for each section. However, the performance over a section affected by a lower SNR is weaker compared to the performance over a section affected by a higher SNR. Spatially-coupled (SC) codes are a family of graph-based codes with capacity approaching performance and low latency decoding. An SC code is constructed by partitioning an underlying block code to several component matrices, and coupling copies of the component matrices together. The contribution of this paper is threefold. First, we present a new partitioning technique to efficiently construct SC codes with column weights 4 and 6. Second, we present an SC code construction for channels with SNR variation. Our SC code construction provides local error correction for each section by means of the underlying codes that cover one section each, and simultaneously, an added level of error correction by means of coupling among the underlying codes. Third, we introduce a low-complexity interleaving scheme specific to SC codes that further improves their performance over channels with SNR variation. Our simulation results show that our SC codes outperform individual block codes by more than one and two orders of magnitudes in the error floor region compared to the block codes with and without regular interleaving, respectively. This improvement is more pronounced by increasing the memory and column weight.

## Low-Power SDR Design on an FPGA for Intersatellite Communications

- **ID**: ieee:8412572
- **Type**: journal
- **Published**: Nov. 2018
- **Authors**: Xin Cai, Mingda Zhou, Tian Xia +3
- **PDF**: https://ieeexplore.ieee.org/document/8412572
- **Abstract**: Small satellite systems make space missions for communication, navigation, and scientific research more realizable and diversified. Small satellites flying in large cluster or constellation formation as a network can provide an economical access to accomplish more complex missions, such as distributed computation, high-resolution imaging, and spacecraft maintenance. An increasing number of satellites operating on lower earth orbit for complex missions require a wireless communication system that is both reliable and flexible. This paper presents a complete software-defined radio (SDR) model for intersatellite communications (ISCs) and its implementation on a field-programmable gate array (FPGA). The proposed SDR for transmitter and receiver only has a power consumption of 2.1 and 3.2 W, respectively, which is suitable for power-limited small satellite systems. Algorithms and parameters of each block are optimized aiming at reducing hardware resource utilization. A low-density parity-check code constructed by the Euclidean geometry method is adopted as the channel code for forward error correction. Implementations of the synchronization, demodulation, and decoding algorithms are optimized for hardware efficiency. The low-power SDR designs are implemented on an FPGA-based experimental platform and successful demonstrated by over-the-air transmissions.

## A Study on Iterative Decoding With LLR Modulator by Parity Check Information in SMR System

- **ID**: ieee:8369398
- **Type**: journal
- **Published**: Nov. 2018
- **Authors**: M. Nishikawa, Y. Nakamura, H. Osawa +3
- **PDF**: https://ieeexplore.ieee.org/document/8369398
- **Abstract**: In recent years, shingled magnetic recording (SMR) has attracted attention as a new recording system of the hard disk drives. Although SMR can realize narrow track by overwriting data track like tile roofing, it has remarkable performance deterioration due to the influence of inter-track interference. Therefore, the performance improvement of the low-density parity-check (LDPC) coding and iterative decoding system using the sum-product decoding is required. In this paper, we propose the LDPC encoding and iterative decoding system with the log-likelihood ratio modulator and show the error floor is eliminated and improvement of signal-to-noise ratio to achieve the error free is obtained in the SMR under an areal recording density of 4 Tbits/in2 specification for the channel bit sequence coded by run-length limited and LDPC encoders by computer simulation. Therefore, the channel bit is composed bit about five magnetic grains.

## Design of Nonbinary LDPC Codes Based on Message-Passing Algorithms

- **ID**: ieee:8388219
- **Type**: journal
- **Published**: Nov. 2018
- **Authors**: Sunghye Cho, Kyungwhoon Cheun, Kyeongcheol Yang
- **PDF**: https://ieeexplore.ieee.org/document/8388219
- **Abstract**: Short cycles in a nonbinary low-density parity-check (NB-LDPC) code may be even more harmful to its performance if they do not satisfy the so-called full rank condition (FRC). This is because they may induce low-weight codewords or absorbing sets in that case. Thus, it is important to count the number of short cycles not satisfying the FRC as well as the number of short cycles for analyzing the performance of an NB-LDPC code. In this paper, we first develop a novel message-passing algorithm and identify how it is related to the FRC. We then propose a low-complexity algorithm for counting the number of short cycles not satisfying the FRC in an NB-LDPC code, as well as the number of short cycles. Finally, we propose a low-complexity algorithm for designing an NB-LDPC code with low error floor. Depending on the modulation scheme, the codes constructed by the proposed design algorithm have similar or slightly worse performance, compared with those constructed via the method by Poulliat et al. However, the proposed design algorithm does not require a cycle enumeration algorithm with high complexity, and therefore is feasible even in the case of large code length, say ≥5000.

## Bit-Metric Decoding of Non-Binary LDPC Codes With Probabilistic Amplitude Shaping

- **ID**: ieee:8466621
- **Type**: journal
- **Published**: Nov. 2018
- **Authors**: Fabian Steiner, Georg Böcherer, Gianluigi Liva
- **PDF**: https://ieeexplore.ieee.org/document/8466621
- **Abstract**: A new approach for combining non-binary (NB) low-density parity-check codes with higher order modulation and probabilistic amplitude shaping (PAS) is presented. Instead of symbol-metric decoding, a bit-metric decoder is used so that matching the field order of the NB code to the constellation size is not needed, which increases the flexibility of the coding scheme. Information rates, density evolution thresholds, and finite-length simulations show that the flexibility comes at no loss of performance if PAS is used.

## The Velocity of the Propagating Wave for Spatially Coupled Systems With Applications to LDPC Codes

- **ID**: ieee:8419715
- **Type**: journal
- **Published**: Nov. 2018
- **Authors**: Rafah El-Khatib, Nicolas Macris
- **PDF**: https://ieeexplore.ieee.org/document/8419715
- **Abstract**: We consider the dynamics of message passing for spatially coupled codes and, in particular, the set of density evolution equations that tracks the profile of decoding errors along the spatial direction of coupling. It is known that, for suitable boundary conditions and after a transient phase, the error profile exhibits a “solitonic behavior.” Namely, a uniquely shaped wavelike solution develops, which propagates with a constant velocity. Under this assumption, we derive an analytical formula for the velocity in the framework of a continuum limit of the spatially coupled system. The general formalism is developed for spatially coupled low-density parity-check codes on general binary memoryless symmetric channels, which form the main systems of interest in this paper. We apply the formula for special channels and illustrate that it matches the direct numerical evaluation of the velocity for a wide range of noise values. A possible application of the velocity formula to the evaluation of finite size scaling law parameters is also discussed. We conduct a similar analysis for general scalar systems and illustrate the findings with applications to compressive sensing and generalized low-density parity-check codes on the binary erasure or binary symmetric channels.

## Polar Codes for Spin-Torque Transfer Magnetic Random Access Memory

- **ID**: ieee:8399859
- **Type**: journal
- **Published**: Nov. 2018
- **Authors**: Zhen Mei, Kui Cai, Bin Dai
- **PDF**: https://ieeexplore.ieee.org/document/8399859
- **Abstract**: Spin-torque transfer magnetic random access memory (STT-MRAM) is a promising non-volatile memory (NVM) technology due to its superior performance in terms of power consumption, write/read speed, endurance, and scalability. However, the reliability of STT-MRAM is affected by the process variation and thermal fluctuation, leading to both the write errors and read errors. Hence, it is important to develop error correction coding schemes to correct the memory cell errors and improve the system reliability. In this paper, we propose, for the first time, the design and optimization of polar codes for the STT-MRAM channel. In particular, as the STT-MRAM channel is asymmetric by nature, we first adopt an approach to symmetrize the channel so as to facilitate the design of effective polar codes. We then apply the density evolution method to construct polar codes and optimize their performance for the STT-MRAM channel. Furthermore, in order to mitigate the raw bit error rate diversity of STT-MRAM cells caused by process variations, we propose a rate-adaptive polar coding scheme in conjunction with an adaptive decoding algorithm. Simulation results and the decoder complexity analysis show that the constructed polar codes outperform both the Bose–Chaudhuri–Hoquenghem codes and low-density parity-check codes with lower decoding complexity, thus demonstrating the great potential of polar codes for improving the reliability of emerging NVMs.

## A UEP Method for Imaging Low-Orbit Satellites Based on CCSDS Recommendations

- **ID**: ieee:8444044
- **Type**: journal
- **Published**: Nov. 2018
- **Authors**: Christofer Schwartz, Cristiano Torezzan, Leonardo Tomazeli Duarte
- **PDF**: https://ieeexplore.ieee.org/document/8444044
- **Abstract**: Remote sensing satellites allow continuous information acquisition from large areas of the earth and have been intensively applied in a number of applications, from agriculture to defense. A major challenge in remote sensing is that satellite communication systems present bandwidth restrictions and several issues typical of time-variant channels, which justifies the need for signal coding techniques. In that sense, this letter proposes an unequal error protection method for aerospace applications using the recommendations for source and channel coding created by the Consultative Committee for Space Data System (CCSDS) as frameworks. The proposed method makes use of the CCSDS-recommended convolutional code to ensure a channel coding step as low complex as possible, which allows implementation in a wide range of embedded platforms. This letter exploits the natural data division delivered by the compressor to unequally protect the information. The proposed method, which relies on a multiobjective optimization problem, allows one to find rate arrangements that minimize the distortion of the received image for a given value of an average coding rate within a granular range. The system performance is evaluated over an additive white Gaussian noise channel model. The obtained results show that the proposed method presents several advantages over an equal error protection strategy, and paves the way for scenarios with stringent energy and bandwidth constraints.

## Performance of Bit-Patterned Media Recording According to Island Patterns

- **ID**: ieee:8383702
- **Type**: journal
- **Published**: Nov. 2018
- **Authors**: Seongkwon Jeong, Juri Kim, Jaejin Lee
- **PDF**: https://ieeexplore.ieee.org/document/8383702
- **Abstract**: Because of the exponential increase in internal and external information, we need to handle the enormous amount of data. However, there is a limit to data storage on hard disk drives because of a super-paramagnetism phenomenon which prevents the formation of a high areal density (AD). Accordingly, research about bit-patterned media recording (BPMR) that stores one bit in a single magnetic island is actively in progress. BPMR can increase stored data quantities by adjusting the distance between islands. However, inter-symbol interference and inter-track interference cause problems that degrade performance due to bit period and small track pitch, respectively. Moreover, the island pattern also affects the performance because depending on the pattern, 2-D interference is changed. In this paper, we experiment to find the case that minimizes the bit error ratio in the same AD with various distances between the islands, and compares the performance in the staggered and rectangular patterns.

## Joint Power and Modulation Optimization in Two-User Non-Orthogonal Multiple Access Channels: A Minimum Error Probability Approach

- **ID**: ieee:8449119
- **Type**: journal
- **Published**: Nov. 2018
- **Authors**: Benjamin K. Ng, Chan-Tong Lam
- **PDF**: https://ieeexplore.ieee.org/document/8449119
- **Abstract**: In this paper, we consider the joint power and modulation optimization in two-user non-orthogonal multiple access (NOMA) channels based on error-rate performance criterion and finite-alphabet inputs. Specifically, with joint maximum-likelihood detection being employed at each user's receiver, the users' transmission power levels are jointly determined with the 4-QAM constellation of one of the users being rotated such that the probability of dominant pairwise error event in the NOMA channel is minimized. Toward solving the joint power and modulation problem, our results are twofold. First, with M antennas at the receiver, closed-form expressions for the optimal angles as a function of M, the channel coefficients, and the users' power levels are derived. Second, closed-form expressions are derived for the joint power allocation with optimal rotation by casting the joint optimization as a piecewise convex optimization problem over its sub-domains. Using the proposed joint optimization, the error-rate performance of NOMA improves significantly and it outperforms traditional NOMA power allocation methods for the selected transmission rates. The proposed approach thus represents a rather distinct approach in NOMA optimization, and it is applicable in the uplink NOMA where users share the same time/frequency channel or in the downlink NOMA where users are multiplexed in the power domain.

## Dual-Polarized Faster-Than-Nyquist Transmission Using Higher Order Modulation Schemes

- **ID**: ieee:8408541
- **Type**: journal
- **Published**: Nov. 2018
- **Authors**: Mrinmoy Jana, Lutz Lampe, Jeebak Mitra
- **PDF**: https://ieeexplore.ieee.org/document/8408541
- **Abstract**: Faster-than-Nyquist (FTN) transmission employing antenna polarization multiplexing and higher order modulation (HoM) schemes can significantly increase the spectral efficiency (SE) of the existing wireless backhaul links. However, the benefits of each of these SE enhancement techniques come with a price. While FTN introduces inter-symbol interference, a dual-polarized (DP) transmission suffers from cross-polarization interference (XPI), and HoM makes a communication system vulnerable to phase-noise (PN) distortions. In this paper, we investigate, for the first time, a DP-FTN HoM transmission system. We propose a XPI cancellation and PN mitigation structure, coupled with adaptive decision-feedback equalization or linear precoding, to jointly mitigate interference and accomplish carrier-phase tracking. The DP systems combined with the FTN signaling presented in this paper offer more than 150% increase in SE compared with a single-polarized Nyquist transmission. The effectiveness of the proposed algorithms is demonstrated through computer simulations of a coded DP-FTN microwave communication system in the presence of PN. Numerical results suggest that with the proposed interference cancellation methods, a DP-FTN transmission can yield a 3-5.5-dB performance improvement over an equivalent DP-Nyquist system that employs a higher modulation order to achieve the same data rate.

## Jointly Optimizing User Association and BS Muting for Cache-Enabled Networks With Network-Coded Multicast and Reconstructed Interference Cancelation

- **ID**: ieee:8421237
- **Type**: journal
- **Published**: Nov. 2018
- **Authors**: Kaiyang Guo, Chenyang Yang, Tingting Liu +1
- **PDF**: https://ieeexplore.ieee.org/document/8421237
- **Abstract**: In this paper, we strive to improve the throughput of heterogeneous cellular networks by exploiting the pre-cached files at user end to manage interference. We consider a transmission scheme, where network-coded multicast is employed to help cancel multi-user interference, and reconstructed interference cancellation (RIC) is used to help eliminate inter-cell interference. Because RIC is opportunistic, base station (BS) muting is used to coordinate the residual strong interference. Since user association affects residual interference and is coupled with BS muting while both are operated in a very different timescale from content caching, we jointly optimize user association and BS muting for a given caching policy to maximize the number of users simultaneously served by the transmission scheme. By transforming the formulated problem into a maximal independent set problem with constructed conflict graph, the global optimal solution is found with graph theory methods. By exploiting the topology feature of heterogeneous networks, we proceed to propose two low-complexity algorithms, respectively, implemented in a centralized and distributed manner, which are viable for large-scale networks. Simulation results show that the optimized transmission scheme achieves a remarkable performance gain over the existing schemes.

## Asymptotic Analysis and Spatial Coupling of Counter Braids

- **ID**: ieee:8434352
- **Type**: journal
- **Published**: Nov. 2018
- **Authors**: Eirik Rosnes, Alexandre Graell i Amat
- **PDF**: https://ieeexplore.ieee.org/document/8434352
- **Abstract**: A counter braid (CB) is a novel counter architecture introduced by Lu et al. in 2007 for per-flow measurements on high-speed links which can be decoded with low complexity using message passing (MP). CBs achieve an asymptotic compression rate (under optimal decoding) that matches the entropy lower bound of the flow size distribution. In this paper, we apply the concept of spatial coupling to CBs to improve the performance of the original CBs and analyze the performance of the resulting spatially-coupled CBs (SC-CBs). We introduce an equivalent bipartite graph representation of CBs with identical iteration-by-iteration finite-length and asymptotic performance. Based on this equivalent representation, we then analyze the asymptotic performance of single-layer CBs and SC-CBs under the MP decoding algorithm proposed by Lu et al.. In particular, we derive the potential threshold of the uncoupled system and show that it is equal to the area threshold. We also derive the Maxwell decoder for CBs and prove that the potential threshold is an upper bound on the Maxwell decoding threshold, which, in turn, is a lower bound on the maximum a posteriori (MAP) decoding threshold. We then show that the area under the extended MP extrinsic information transfer curve (defined for the equivalent graph), computed for the expected residual CB graph when a peeling decoder equivalent to the MP decoder stops, is equal to zero precisely at the area threshold. This, combined with the analysis of the Maxwell decoder and simulation results, leads us to the conjecture that the potential threshold is, in fact, equal to the Maxwell decoding threshold and hence a lower bound on the MAP decoding threshold. Interestingly, SC-CBs do not show the well-known phenomenon of threshold saturation of the MP decoding threshold to the potential threshold characteristic of spatially-coupled low-density parity-check codes and other coupled systems. However, SC-CBs yield better MP decoding thresholds than their uncoupled counterparts. Finally, we also consider SC-CBs as a compressed sensing scheme and show that low undersampling factors can be achieved.

## On the Finite Length Scaling of  $q$ -Ary Polar Codes

- **ID**: ieee:8438502
- **Type**: journal
- **Published**: Nov. 2018
- **Authors**: Dina Goldin, David Burshtein
- **PDF**: https://ieeexplore.ieee.org/document/8438502
- **Abstract**: The polarization process of polar codes over a prime q-ary alphabet is studied. Recently, it has been shown that the blocklength of polar codes with prime alphabet size scales polynomially with respect to the inverse of the gap between code rate and channel capacity. However, except for the binary case, the degree of the polynomial in the bound is extremely large. In this paper, a different approach to computing the degree of this polynomial for any prime alphabet size is shown. This approach yields a lower degree polynomial for various values of the alphabet size that were examined. It is also shown that even lower degree polynomial can be computed with an additional numerical effort.

## Channel Modeling and Multi-Island Recording Scheme on Bit-Patterned Media With Long-Range Island Orientation Fluctuations

- **ID**: ieee:8418778
- **Type**: journal
- **Published**: Nov. 2018
- **Authors**: Yao Wang, B. V. K. Vijaya Kumar, Yumei Wen +1
- **PDF**: https://ieeexplore.ieee.org/document/8418778
- **Abstract**: Media noise is inevitable in bit-patterned media (BPM) due to fabrication imperfections, and degrades the bit error rate (BER) performance of channel. In this paper, a new channel model is proposed to characterize the media noise in BPM fabricated with cost-effective self-assembled technology, which exhibits long-range island orientation fluctuations in addition to the usual local island position and size fluctuations. To alleviate the effects of the significant media noise and write errors for such BPM at 4 Tera-islands/in2 density, we have proposed a recording scheme that uses multiple islands (2 by 2 islands) for 1-bit information in contrast to the conventional recording scheme of recording 1 bit on one island. For both recording schemes using low-density parity check code at the same user areal density (0.9 Tb/in2), when the island orientation fluctuation is large (i.e.,  ${\ge} 10$ °), the proposed 4 islands/bit scheme outperforms 1 island/bit scheme. This BER improvement is because the write error and media noise become increasingly dominant compared to the readback error caused by the inter-track interference and additive white Gaussian noise when the island orientation fluctuation is large. Although the proposed multiple islands recording scheme decreases the user density significantly, the proposed model can be helpful in developing more advanced signal processing and coding techniques that can alleviate the long-range island orientation fluctuations without such a sacrifice in user density.

## A Further Research on Two-phase Decoding for GC-LDPC Codes

- **ID**: ieee:8693129
- **Type**: conference
- **Published**: 9-11 Nov. 
- **Authors**: Wei Zhou, Lijun Zhang, Qiang Sun
- **PDF**: https://ieeexplore.ieee.org/document/8693129
- **Abstract**: For GC-LDPC code, a targeted decoding scheme is the two-phase decoding scheme, i.e., the local decoding phase and the global decoding phase. For both the phases, we find the direct application of log-domin belief propagation (BP) algorithm will lead to error. Hence, we propose an improved log-domin BP algorithm and it will be used in the two-phase decoding scheme. Since the two-phase decoding scheme has a large gain loss, we present a modified two-phase decoding scheme in order to further accelerate the convergence rate. Simulation results show that the modified two-phase decoder has a gain of about 0.2 dB compared to the two-phase decoder. Moreover, it also can reduce complexity by 33.4% in high SNR compared with the whole decoder.

## Sensor Cooperation and Decision Fusion to Improve Detection in Cognitive Radio Spectrum Sensing

- **ID**: ieee:8796752
- **Type**: conference
- **Published**: 8-10 Nov. 
- **Authors**: Zafar Iqbal, Saeid Nooshabadi, Khaled Jadi +1
- **PDF**: https://ieeexplore.ieee.org/document/8796752
- **Abstract**: Cooperative spectrum sensing has been shown to significantly improve the spectrum utilization in cognitive radio networks. In this paper, we deal with the problem of error in reporting the local decisions to the fusion center by the secondary users. First, we formulate a protocol of cooperation among the secondary users to share their local decisions and then relay each others information to the fusion center. Second, we use low-density parity-check coded communication in the second hop to protect the relayed information against variations in the wireless channel. The reported information from each sensor is then combined at a fusion center and a final decision is made based on majority-voting fusion mechanism. We refer to this scheme as coded cooperative spectrum sensing (CCSS). Finally, it is shown that the proposed CCSS scheme improves the spectrum utilization of the cognitive radio network by reducing the error in reporting the local decisions to the fusion center.

## A Low-cost Mobile Infrastructure for Multi-AUV Networking

- **ID**: ieee:8729790
- **Type**: conference
- **Published**: 6-9 Nov. 2
- **Authors**: Barzin Moridian, Li Wei, John Hoffman +6
- **PDF**: https://ieeexplore.ieee.org/document/8729790
- **Abstract**: The study of underwater environments is a challenging task that can lead to discoveries in many scientific domains. Among the tools for such studies are Autonomous Underwater Vehicles (AUVs) that can be operated remotely or autonomously for gathering information. The limited communication capabilities of AUVs operating underwater restricts their effectiveness. This paper presents our recent progress towards the development of a modular yet low-cost mobile networking infrastructure for the underwater domain. Specifically, this infrastructure consists of a fleet of autonomous surface vehicles that can serve as a surrogate for research on acoustically connected AUV networks. The work involves the design and development of autonomous surface vehicles and the integration of acoustic communication units to characterize the acoustic communication channel properties when subject to motions of the transmitter or the receiver.

## On the Error Exponents of Capacity Approaching Construction of LDPC code

- **ID**: ieee:8631262
- **Type**: conference
- **Published**: 5-9 Nov. 2
- **Authors**: Pavel Rybin, Alexey Frolov
- **PDF**: https://ieeexplore.ieee.org/document/8631262
- **Abstract**: In this paper we consider low-density parity-check (LDPC) codes with special construction. We obtain the lower-bounds on the error exponents for these codes under proposed low-complexity decoding algorithm and under a well known maximum likelihood decoding algorithm. We show that such LDPC code with special construction exists, that the error probability of the low-complexity decoding algorithm exponentially decreases with the code length for all code rates below the channel capacity. We also show that obtained lower-bound on the error exponent under the maximum likelihood decoding almost reaches the lower-bound on the error exponent of good linear codes under the maximum likelihood decoding. The error exponents are computed numerically for different code parameters.

## On the Implementation of Vertical Shuffle Scheduling Decoder for Joint MIMO Detection and Channel Decoding System

- **ID**: ieee:8672710
- **Type**: conference
- **Published**: 28-30 Nov.
- **Authors**: Ali Haroun, Rawad Nasr, Ali Al-Ghouwayel
- **PDF**: https://ieeexplore.ieee.org/document/8672710
- **Abstract**: This paper presents a novel architecture of a soft NB-LDPC decoder for joint iterative MIMO receivers. The architecture is able to decode the rate R= 1/2 with frame length N=384 LDPC code using a 64 QAM modulation. To our knowledge, it is the first soft decoder architecture that implements the belief propagation algorithm based on vertical shuffle schedule. The proposed architecture implements a single variable node processor where the Log Likelihood Ratio (LLR) computation block is removed. It also implements a single Check Node processor that is composed of six Elementary Check Nodes. Synthesis results show that the proposed architecture consumes 6.476 K slices and run at a maximum clock frequency of 70 MHz. Taking only the decoding process part alone, 188 clock cycles are required to perform decoding iterations.

## Hybrid Decoding of LDPC Codes in Discrete Communication Channels

- **ID**: ieee:8604309
- **Type**: conference
- **Published**: 26-30 Nov.
- **Authors**: A. A. Ovchinnikov, D. V. Ilina
- **PDF**: https://ieeexplore.ieee.org/document/8604309
- **Abstract**: Decoding of low-density parity-check codes with bit-flip algorithm is considered. The majority-logic decoding is described as bit-flip algorithm with modified decoding threshold. The hybrid decoding combining both algorithms is considered and simulation results in Gaussian channel with hard decision demodulation are given. Described scheme may be effective in high-speed channels with low number of decoding iterations demands together with the requirements of low decoding error probabilities and low error-floors.

## Optimization of Collision Resolution Algorithm in Multiple Access Systems

- **ID**: ieee:8604399
- **Type**: conference
- **Published**: 26-30 Nov.
- **Authors**: A. A. Gorokhov, A. A. Ovchinnikov
- **PDF**: https://ieeexplore.ieee.org/document/8604399
- **Abstract**: The algorithm of collision resolution in random multiple access system with successive interference cancellation is investigated and implemented as well as differential evolution algorithm. The weight polynomial is obtained which in some cases outperforms known solutions in random multiple access systems.

## NEURAL LATTICE DECODERS

- **ID**: ieee:8646560
- **Type**: conference
- **Published**: 26-29 Nov.
- **Authors**: Vincent Corlay, Joseph J. Boutros, Philippe Ciblat +1
- **PDF**: https://ieeexplore.ieee.org/document/8646560
- **Abstract**: Lattice decoders constructed with neural networks are presented. Firstly, we show how the fundamental parallelotope is used as a compact set for the approximation by a neural lattice decoder. Secondly, we introduce the notion of Voronoi-reduced lattice basis. As a consequence, a first optimal neural lattice decoder is built from Boolean equations and the facets of the Voronoi cell. This decoder needs no learning. Finally, we present two neural decoders with learning. It is shown that L1 regularization and a priori information about the lattice structure lead to a simplification of the model.

## Generalized Globally-Coupled Low-Density Parity-Check Codes

- **ID**: ieee:8613362
- **Type**: conference
- **Published**: 25-29 Nov.
- **Authors**: Yen-Chin Liao, Hsie-Chia Chang, Shu Lin
- **PDF**: https://ieeexplore.ieee.org/document/8613362
- **Abstract**: In this paper, two globally-coupled low-density parity check (GC-LDPC) code constructing methods are presented. The first is a Reed-Solomon-like GC-LDPC code that eases the design parameter searching in algebraic code constructions. The parameters such as the finite field, the associated prime factors, or the number of local codes can be more easily determined. The directly masking approach, the second proposed scheme, facilitates flexible structure designs of the parity check matrices. The two approaches can be regarded as generalizations of the original GC-LDPC codes. The design examples and the simulation results show the feasibility of the proposed techniques. In addition to code constructions, some applications and usage scenarios of GC-LDPC codes are addressed as well.

## Coding Theorem for Systematic LDGM Codes Under List Decoding

- **ID**: ieee:8613510
- **Type**: conference
- **Published**: 25-29 Nov.
- **Authors**: Wenchao Lin, Suihua Cai, Baodian Wei +1
- **PDF**: https://ieeexplore.ieee.org/document/8613510
- **Abstract**: This paper is concerned with three ensembles of systematic low density generator matrix (LDGM) codes, all of which were provably capacity-achieving in terms of bit error rate (BER). This, however, does not necessarily imply that they achieve the capacity in terms of frame error rate (FER), as seen from a counterexample constructed in this paper. We then show that the first and second ensembles are capacity-achieving under list decoding over binary-input output symmetric (BIOS) memoryless channels. We point out that, in principle, the equivocation due to list decoding can be removed with negligible rate loss by the use of the concatenated codes. Simulation results show that the considered convolutional (spatially-coupled) LDGM code is capacity-approaching with an iterative belief propagation decoding algorithm.

## Free Pseudodistance Growth Rates for Spatially Coupled LDPC Codes over the BEC

- **ID**: ieee:8613507
- **Type**: conference
- **Published**: 25-29 Nov.
- **Authors**: Cunlu Zhou, David G. M. Mitchell, Roxana Smarandache
- **PDF**: https://ieeexplore.ieee.org/document/8613507
- **Abstract**: The minimum pseudoweight is an important parameter related to the decoding performance of LDPC codes with iterative message-passing decoding. In this paper, we consider ensembles of periodically time-varying spatially coupled LDPC (SC-LDPC) codes and the pseudocodewords arising from their finite graph covers of a fixed degree. We show that for certain (J,K)-regular SC-LDPC code ensembles and a fixed cover degree, the typical minimum pseudoweight of the unterminated (and associated tail-biting/terminated) SC-LDPC code ensembles grows linearly with the constraint (block) length as the constraint (block) length tends to infinity. We prove that one can bound the the free pseudodistance growth rate over a BEC from below (respectively, above) using the associated tail-biting (terminated) SC-LDPC code ensemble and show empirically that these bounds coincide for a sufficiently large period, which gives the exact free pseudodistance growth rate for the SC-LDPC ensemble considered.

## On Generalized LDPC Codes for 5G Ultra Reliable Communication

- **ID**: ieee:8613515
- **Type**: conference
- **Published**: 25-29 Nov.
- **Authors**: Yanfang Liu, Pablo M. Olmos, David G. M. Mitchell
- **PDF**: https://ieeexplore.ieee.org/document/8613515
- **Abstract**: Generalized low-density parity-check (GLDPC) codes, where single parity-check (SPC) constraint nodes are replaced with generalized constraint (GC) nodes, are a promising class of codes for low latency communication. In this paper, a practical construction of quasi-cyclic (QC) GLDPC codes is proposed, where the proportion of generalized constraints is determined by an asymptotic analysis. We analyze the message passing process and complexity of a GLDPC code over the additive white gaussian noise (AWGN) channel and present a constraint-to-variable update rule based on the specific codewords of the component code. The block error rate (BLER) performance of the GLDPC codes, combined with a complementary outer code, is shown to outperform a variety of state-of-the-art code and decoder designs with suitable lengths and rates for the 5G Ultra Reliable Communication (URC) regime over an additive white gaussian noise (AWGN) channel with quadrature PSK (QPSK) modulation.

## Geometric shaping: low-density coding of Gaussian-like constellations

- **ID**: ieee:8613506
- **Type**: conference
- **Published**: 25-29 Nov.
- **Authors**: Joseph J. Boutros, Uri Erez, Johannes Van Wonterghem +2
- **PDF**: https://ieeexplore.ieee.org/document/8613506
- **Abstract**: Constellation shaping is necessary to approach channel capacity for information rates above 1 bit/dim. Probabilistic shaping shows a small gap to capacity, however a complex distribution matcher is required to modify the source distribution. Spherical shaping of lattice constellations also reduces the gap to capacity, but practical Voronoi shaping is feasible in small dimensions only. In this paper, our codebook is a real geometrically non-uniform Gaussian-like constellation. We prove that this discrete codebook achieves channel capacity when the number of points goes to infinity. Then we build a special mapping to interface between non-binary low-density codes and the codebook, allowing the code alphabet size to be equal to the square root of the codebook size. Excellent performance is shown with fast-encoding and practical iterative probabilistic decoding, e.g. 0.7 dB gap to capacity at 6 bits/s/Hz with a code defined over the ring Z/8Z.

## Type-II Quasi-Cyclic LDPC Codes with Girth Eight from Sidon Sequence

- **ID**: ieee:8613426
- **Type**: conference
- **Published**: 25-29 Nov.
- **Authors**: Guohua Zhang, Yulin Hu, Qinwei He +1
- **PDF**: https://ieeexplore.ieee.org/document/8613426
- **Abstract**: In this work, we consider type-II quasi-cyclic LDPC codes with girth eight from a Sidon sequence. We first derive the necessary and sufficient conditions guaranteeing girth-eight type-II QC-LDPC codes. By combining these conditions and the concept of a Sidon sequence, two classes of type-II codes are subsequently proposed with girth up to eight. We discuss the distance upper bounds of the two classes of codes and show that the second class provides a larger distance upper bound. In particular, to the best of our knowledge, the second class we proposed yields the first algebraic construction for girth-eight type-II codes with rates larger than a half and distance upper bounds exceeding twelve. Via simulations, we show that the girth-eight type-II codes from the second class significantly outperform the existing CDF-based girth-eight type-II codes, and that they perform better than or almost identically to the randomly generated girth-eight quadr. congr. codes.

## Read-Voltage Optimization for Finite Code Length in MLC NAND Flash Memory

- **ID**: ieee:8613523
- **Type**: conference
- **Published**: 25-29 Nov.
- **Authors**: Kang Wei, Jun Li, Lingjun Kong +2
- **PDF**: https://ieeexplore.ieee.org/document/8613523
- **Abstract**: In this paper, we propose an effective read-voltage optimization method for multi-level-cell (MLC) NAND flash memory to improve the performance of error correcting codes (ECCs) with finite blocklength. Specifically, we first obtain the maximal channel coding rate achievable at a given blocklength and error probability of quantized channel. Based on this finite-blocklength channel-coding rate (FCR), we convert the optimization problem into minimizing the error probability instead of the channel coding rate. Then, we develop a cross iterative search (CIS) method and the genetic algorithm to solve this optimization problem. In our simulations, for a well-designed LDPC code, our read-voltage optimization method improves program-and-erase (PE) endurance up to about 900 and 600 cycles against the maximizing the mutual information (MMI) and entropy-based optimization methods, respectively, at a frame-error-rate (FER) of 2×10-4.

## Binary Linear Codes with Optimal Scaling: Polar Codes with Large Kernels

- **ID**: ieee:8613428
- **Type**: conference
- **Published**: 25-29 Nov.
- **Authors**: Arman Fazeli, Hamed Hassani, Marco Mondelli +1
- **PDF**: https://ieeexplore.ieee.org/document/8613428
- **Abstract**: We prove that, at least for the binary erasure channel, the polar-coding paradigm gives rise to codes that not only approach the Shannon limit but, in fact, do so under the best possible scaling of their block length as a function of the gap to capacity. This result exhibits the first known family of binary codes that attain both optimal scaling and quasi-linear complexity of encoding and decoding. Specifically, for any fixed δ > 0, we exhibit binary linear codes that ensure reliable communication at rates within ε > 0 of capacity with block length n = O(1/ε2+δ), construction complexity Θ(n), and encoding/decoding complexity Θ(n log n).

## An Iterative Soft-Decision Decoding Algorithm with Dynamic Saturation for Short Reed-Solomon Codes

- **ID**: ieee:8613470
- **Type**: conference
- **Published**: 25-29 Nov.
- **Authors**: Bryan Liu, Yixuan Xie, Lei Yang +1
- **PDF**: https://ieeexplore.ieee.org/document/8613470
- **Abstract**: This paper proposes a new iterative soft-decision decoding algorithm which combines list decoding and adaptive belief propagation (ABP) algorithm for short Reed-Solomon (RS) codes. The proposed algorithm generates a list of codewords by restarting the decoder with log-likelihood ratio saturations to the dynamically selected suspicious bits based on an up-to-date best decoded codeword. The suspicious bits are selected according to a joint evaluation of the decoded codeword and the initial channel information. The damping coefficient used in the ABP decoder is set to be proportional to the channel noise variance to achieve a proper convergence speed for the decoder at different SNRs. The performance of the proposed algorithm for short RS codes is investigated. It shows that the proposed algorithm brings a considerable coding gain for short RS codes over additive white Gaussian noise channels.

## Joint Channel-Network Decoding for Asynchronous Physical-Layer Network Coding

- **ID**: ieee:8613512
- **Type**: conference
- **Published**: 25-29 Nov.
- **Authors**: Xiaokang Wang, Wai Ho Mow
- **PDF**: https://ieeexplore.ieee.org/document/8613512
- **Abstract**: Symbol asynchrony is an important issue in practical implementation of physical-layer network coding (PNC). In this paper, we investigate the asynchronous convolutionally coded PNC over the two-way relay network (TWRN). Symbols from two users arrive at the relay with symbol misalignment. A joint channel-network decoder (JCND) for the relay is proposed. A salient feature for the proposed JCND is that it incorporates the code structure and the symbol misalignment jointly, and the cyclic structure for the channel code is not required to combat the integer symbol misalignment. Furthermore, we derive the bit error rate (BER) bound at the relay utilizing the error state diagram. Simulation results indicate that the performance of the proposed algorithm matches well with the bound.

## Secure physical layer network coding versus secure network coding

- **ID**: ieee:8613305
- **Type**: conference
- **Published**: 25-29 Nov.
- **Authors**: Masahito Hayashi
- **PDF**: https://ieeexplore.ieee.org/document/8613305
- **Abstract**: Secure network coding realizes the secrecy of the message when the message is transmitted via noiseless network and a part of edges or a part of intermediate nodes are eavesdropped. In this framework, if the channels of the network has noise, we apply the error correction to noisy channel before applying the secure network coding. In contrast, secure physical layer network coding is a method to securely transmit a message by a combination of coding operation on nodes when the network is given as a set of noisy channels. In this paper, we give several examples of network, in which, secure physical layer network coding realizes a performance that cannot be realized by secure network coding.

## Information Theoretic Bounds Based Channel Quantization Design for Emerging Memories

- **ID**: ieee:8613421
- **Type**: conference
- **Published**: 25-29 Nov.
- **Authors**: Zhen Mei, Kui Cai, Long Shi
- **PDF**: https://ieeexplore.ieee.org/document/8613421
- **Abstract**: Channel output quantization plays a vital role in high-speed emerging memories such as the spin-torque transfer magnetic random access memory (STT-MRAM), where high-precision analog-to-digital converters (ADCs) are not applicable. In this paper, we investigate the design of the 1-bit quantizer which is highly suitable for practical applications. We first propose a quantized channel model for STT-MRAM. We then analyze various information theoretic bounds for the quantized channel, including the channel capacity, cutoff rate, and the Polyanskiy-Poor-Verdu ́(PPV) finite-length performance bound. By using these channel measurements as criteria, we design and optimize the 1-bit quantizer numerically for the STTMRAM channel. Simulation results show that the proposed quantizers significantly outperform the conventional minimum mean-squared error (MMSE) based Lloyd-Max quantizer, and can approach the performance of the 1-bit quantizer optimized by error rate simulations.

## Circular-shift Linear Network Codes with Arbitrary Odd Block Lengths

- **ID**: ieee:8613312
- **Type**: conference
- **Published**: 25-29 Nov.
- **Authors**: Qifu Tyler Sun, Hanqi Tang, Zongpeng Li +2
- **PDF**: https://ieeexplore.ieee.org/document/8613312
- **Abstract**: Circular-shift linear network coding (LNC) is a class of vector LNC with low encoding and decoding complexities, with local encoding kernels chosen from cyclic permutation matrices. When L is a prime with primitive root 2, it was recently shown that a scalar linear solution over GF(2L-1) induces an Ldimensional circular-shift linear solution at rate (L-1)/L. In this work, we prove that for an arbitrary odd L, every scalar linear solution over GF(2(m)L), where mL refers to the multiplicative order of 2 modulo L, can induce an L-dimensional circularshift linear solution at a certain rate. Based on the generalized connection, we further prove that every multicast network has an L-dimensional circular-shift linear solution at rate φ(L)/L, where φ(L) is the Euler's totient function of L and (m)L is beyond a threshold. Stemming from this, we last prove that every multicast network is asymptotically circular-shift linearly solvable.

## Algebraic Optimization of Binary Spatially Coupled Measurement Matrices for Interval Passing

- **ID**: ieee:8613339
- **Type**: conference
- **Published**: 25-29 Nov.
- **Authors**: Salman Habib, Jörg Kliewer
- **PDF**: https://ieeexplore.ieee.org/document/8613339
- **Abstract**: We consider binary spatially coupled (SC) low density measurement matrices for low complexity reconstruction of sparse signals via the interval passing algorithm (IPA). The IPA is known to fail due to the presence of harmful sub-structures in the Tanner graph of a binary sparse measurement matrix, so called termatiko sets. In this work we construct array-based (AB) SC sparse measurement matrices via algebraic lifts of graphs, such that the number of termatiko sets in the Tanner graph is minimized. To this end, we show for the column-weight-three case that the most critical termatiko sets can be removed by eliminating all length-12 cycles associated with the Tanner graph, via algebraic lifting. As a consequence, IPA-based reconstruction with SC measurement matrices is able to provide an almost error free reconstruction for significantly denser signal vectors compared to uncoupled AB LDPC measurement matrices.

## EXIT Analysis for Decoding Behaviour and Performances of 5G NR QC-LDPC Codes

- **ID**: ieee:8713114
- **Type**: conference
- **Published**: 25-28 Nov.
- **Authors**: Yoga Julian, Rina Pudji Astuti, Khoirul Anwar
- **PDF**: https://ieeexplore.ieee.org/document/8713114
- **Abstract**: Quasi-Cyclic (QC) Low Density Parity Check (LDPC) codes having capability of incremental redundancy (IR) with extended parity (EP) have been standardized as channel coding schemes for the fifth telecommunication generation (5G) New Radio (NR). This paper analyses the behaviour of QC-LDPC codes of 5G NR based on Base Graph 1 (BG1) to ensure the performance for further practical development and applications. In this paper, we consider a single carrier transmission under additive white Gaussian noise (AWGN) channels. We use Extrinsic Information Transfer (EXIT) chart to evaluate and predict the performances as well as the behaviour of the QC-LDPC codes. We reveal the mechanism of IR and the decrease of channel coding rate due to the use of EP. When all EPs are transmitted, the EXIT chart keeps open at about 3 dB lower in Eb/N0 compared to the case of without EP, which is indicating that EP can be optionally transmitted depending on the condition of the channels leading to the changes of channel coding rates.

## Analysis of Channel Coding Methods in Multipath OFDM 5G

- **ID**: ieee:8713083
- **Type**: conference
- **Published**: 25-28 Nov.
- **Authors**: San Hlaing Myint, Takuro Sato
- **PDF**: https://ieeexplore.ieee.org/document/8713083
- **Abstract**: In fifth generation wireless network, it becomes the critical challenge to offer high-bit rate data transmission and extensive networking services with low bit error rate (BER) performance. To achieve the requirements of 5G services, Orthogonal Frequency Division Multiplexing (OFDM) is a considerable technique for high quality communications. In addition, many channel coding schemes have been applied for mitigating performance degradation in terms of BER. Among them, LDPC and Turbo coding methods become the standard specification for high-bit rate data transmission in 5G network. There are so many difficulties and challenges how to apply this coding methods in OFDM with 5G standard specifications.In this paper, we conduct the analysis on two channel coding methods in multipath fading environment of 5G network: LDPC according to 5G specifications of Verizon 5G Technology Forum and Turbo codes by considering backward compatibility. According to our experimental results, we found that our coded OFDM in 5G network outperforms uncoded OFDM in 5G network. Moreover, Turbo coded OFDM with 5G specification achieve better performance with smaller BER than the LDPC coded Multipath OFDM in 5G network. That finding motivates to select Turbo codes as 5G channel coding resulting in cost savings because of backward compatibility to 3G and 4G.

## Comparative Analysis of LDPC decoding by Bit flipping Algorithm using QAM and QPSK modulation techniques for DVB-S2

- **ID**: ieee:8820274
- **Type**: conference
- **Published**: 24-26 Nov.
- **Authors**: Jitendra Pratap, Singh Mathur, Alpana Pandey
- **PDF**: https://ieeexplore.ieee.org/document/8820274
- **Abstract**: Digital communication played important role in wireless system for development of human society for the efficient digital transmission, it is necessary to receive errorless data at receiver. Low-density parity-check (LDPC) codes are comparable with different coding techniques like convolution, block coding, BCH, trellis coding, turbo coding etc. in terms of performance and complexity. This paper presents more efficient modulation and demodulation techniques using QAM and QPSK for DVB-S2 (Digital Video Broadcasting Satellite) standard with LDPC encoder and decoder. BER performance of LDPC coding with Bit flipping Algorithm using QAM and QPSK modulation technique for DVB-S2 standard has been compared.

## Energy-Efficient and Low Complexity Channel Coding for Wireless Body Area Networks

- **ID**: ieee:8606883
- **Type**: conference
- **Published**: 23-24 Nov.
- **Authors**: Hieu T. Nguyen, Thuy V. Nguyen
- **PDF**: https://ieeexplore.ieee.org/document/8606883
- **Abstract**: A new design framework based on the modified protograph extrinsic information transfer (PEXIT) algorithm is proposed for wireless body area networks (WBAN) communication systems. Using the proposed framework, a protograph LDPC code of rate 1/2 is designed for the WBAN channel which is statistically modelled as Rician distribution with K-factor obtained from the path loss model. The proposed protograph LDPC coded system achieves a significant coding gain of 17.5 dB over the uncoded system. This coding gain is much higher than the coding gain (6.1 dB) of irregular LDPC coded system in the additive white Gaussian noise (AWGN) channel reported previously for wireless sensor networks. This significant coding gain together with the low complexity encoder/decoder makes the protograph LDPC code an excellent candidate for WBAN communication systems where energy and complexity are among very demanding technical requirements.

## Layered Offset Min-Sum Decoding for Low Density Parity Check Codes

- **ID**: ieee:8618780
- **Type**: conference
- **Published**: 21-23 Nov.
- **Authors**: Nejwa El Maammar, Seddik Bri, Jaouad Foshi
- **PDF**: https://ieeexplore.ieee.org/document/8618780
- **Abstract**: Offset Min-Sum Algorithm (OMSA) and Normalized Min-Sum Algorithm (NMSA) are widely used in commercial LDPC decoders due to low complexity and reasonable performance. In this paper we proposes an Adaptive Layered Offset min- sum algorithm for the decoding of LDPC codes, which utilizes an adaptive offset factor to improve the accuracy of the soft information transferred during the iterative decoding process, and it provides good performance accordingly. The performed simulations showed that the layered offset min-sum decoding for LDPC codes can provide significant improvement compared to existing MS based algorithm, OMSA and NMSA.

## Performance of Self-Corrected APP-Based Decoding Algorithm for Decoders with Quantized Input

- **ID**: ieee:8612112
- **Type**: conference
- **Published**: 20-21 Nov.
- **Authors**: Aleksei Kharin, Igor Volkov, Aleksei Ovinnikov +2
- **PDF**: https://ieeexplore.ieee.org/document/8612112
- **Abstract**: In this paper we explore the impact of self-correction (SC) modification on performance of a posteriori probability (APP) based decoding algorithm for LDPC codes. Influence of self-correction technique was investigated for decoders with 3, 2 and 1 bit input quantization. It was shown that performance of decoders with quantized input can be significantly improved in comparison with regular APP-based decoding algorithm, and in some cases with Min-Sum algorithm. Convergence of algorithm is almost the same as for Min-Sum decoding. Performance and convergence results are presented for two CCSDS (8176, 7156) and IEEE 802.3an (2048, 1723) LDPC codes for APP-based, SC APP-based and Min-Sum decoding algorithms.

## A High-Throughput QC-LDPC Decoder for Near-Earth Application

- **ID**: ieee:8631641
- **Type**: conference
- **Published**: 19-21 Nov.
- **Authors**: Shixian Li, Qichen Zhang, Yun Chen +1
- **PDF**: https://ieeexplore.ieee.org/document/8631641
- **Abstract**: Turbo-like decoding message passing (TDMP) scheduling, which is suitable for quasi-cyclic low-density parity-check (QC-LDPC) codes, can obtain better decoding performance and shorter convergence time than two-phase message passing (TPMP). Normalized min-sum algorithm (NMSA) is used to reduce complexity of soft message processing unit. In this paper, we propose a (8176, 7154) QC-LDPC decoder for Consultative Committee for Space Data Systems (CCSDS) standard. In order to avoid memory access conflicts, two cyclic-shifted identity matrices forming a submatrix are processed individually. The decoder is synthesized by TSMC 65nm CMOS process and can achieve a throughput of 4.1Gb/s at clock frequency of 380MHz.

## A Novel Jointed Detection Scheme for MIMO-LDPC Systems

- **ID**: ieee:8631790
- **Type**: conference
- **Published**: 19-21 Nov.
- **Authors**: Guiwu Yang, Jianhao Hu, Guoqiang Yao +2
- **PDF**: https://ieeexplore.ieee.org/document/8631790
- **Abstract**: High performance and high efficiency detection scheme is one of the key issues for MIMO-LDPC system designs. In this paper, we proposed a hybrid jointed detection scheme for MIMO-LDPC detection, in which the expectation propagation (EP) algorithm is used in MIMO detection and the belief propagation (BP) algorithm is adopted for the low density parity check code (LDPC) decoding. In the proposed scheme, we provide a jointed detection algorithm (EP-BP JDD) with the integrated factor graph for MIMO-LDPC systems. Compared with conventional MMSE-PIC IDD and BP-BP JDD, the proposed method can achieve low computational complexity with high performance. The complexity and performance gains become more significant with the number of antennas increasing.

## Girth Analysis of Tanner (5,11) Quasi-Cyclic LDPC Codes

- **ID**: ieee:8564291
- **Type**: conference
- **Published**: 16-19 Nov.
- **Authors**: Hengzhou Xu, Hai Zhu, Mengmeng Xu +2
- **PDF**: https://ieeexplore.ieee.org/document/8564291
- **Abstract**: Motivated by the works on the girth of Tanner (3,5), (3,7), (3,11), and (5,7) quasi-cyclic (QC) LDPC codes, we in this paper study the girth of Tanner (5,11) QC-LDPC codes. We first analyze the cycles of Tanner (5,11) QC-LDPC codes, and obtain the conditions for the existence of cycles of length less than 12 in Tanner (5,11) QC-LDPC codes of length 11p where p is a prime number and p =1 (mod 55). Notice that the condition is represented by the polynomial equations in a 55th root of unity of the prime field Fp. By checking the existence of solutions for these equations over Fp, the girths of Tanner (5,11) QC-LDPC codes are obtained.

## Smart Construct High Girth LDPC Codes Based on Permutation Groups

- **ID**: ieee:8564322
- **Type**: conference
- **Published**: 16-19 Nov.
- **Authors**: Qiang Wang, Tingting Lan
- **PDF**: https://ieeexplore.ieee.org/document/8564322
- **Abstract**: In the field of wireless communications, it is of great significance to structure LDPC codes (Low-density Parity-check codes) with large girth. We propose a method to construct high girth LDPC codes based on algebra permutation group of intelligent. Girth larger parity check matrix can be found in Gallager parity check matrix set using genetic algorithm based on permutation group in a relatively short period of time. Simulation results show that the algorithm is efficient, versatile, and consistent with the theoretical analysis.

## Rate-Compatible Protograph LDPC Codes for Spin-Torque Transfer Magnetic Random Access Memory (STT-MRAM)

- **ID**: ieee:8601078
- **Type**: conference
- **Published**: 15-17 Nov.
- **Authors**: Xingwei Zhong, Kui Cai, Pingping Chen +1
- **PDF**: https://ieeexplore.ieee.org/document/8601078
- **Abstract**: This paper proposes novel rate-compatible protograph LDPC (RCP-LDPC) codes to correct memory cell errors and mitigate the raw bit error rate (BER) diversity for spin-torque transfer magnetic random access memory (STT-MRAM). Since the STT-MRAM channel is asymmetric, we first apply an independent and identically distributed (i.i.d.) channel adapter to force the channel to be symmetric. We then propose to use the protograph extrinsic information transfer (PEXIT) algorithm, the asymptotic weight distribution (AWE) analysis, as well as the actual error rate performance as the combined guideline for designing protograph LDPC codes with short codeword lengths for STT-MRAM. By further applying a code extension approach, we construct novel RCP-LDPC codes that can work with a single encoder/decoder. Simulation results show that our proposed RCP-LDPC codes outperform the well-known rate-compatible AR4JA protograph codes.

## On the Design of DC-Free K-Constrained LDPC Codes

- **ID**: ieee:8601099
- **Type**: conference
- **Published**: 15-17 Nov.
- **Authors**: Chi Dinh Nguyen, Kui Cai, Bingrui Wang +1
- **PDF**: https://ieeexplore.ieee.org/document/8601099
- **Abstract**: A novel design of de-free k-constraint low-density parity-check (LDPC) code is proposed in this study. The input user data is first converted into a k-constraint code using a nibble replacement method. After that, a guided scrambling (GS) technique and a (4,6) balance code are deployed together to construct de-free channel coded sequences. The designed de-free k constrained code is further combined with the LDPC code such that the modulation constraints are satisfied in both the systematic and parity parts. Simulation results show that the proposed design not only provides an improved bit-error-rate (BER) performance, but also achieves significant dc suppression.

## Design and Analysis of Spatially Coupled Protograph LDPC Codes for Two-Dimensional Magnetic Recording Systems

- **ID**: ieee:8601100
- **Type**: conference
- **Published**: 15-17 Nov.
- **Authors**: Zhaojie Yang, Yi Fang, Guojun Han +2
- **PDF**: https://ieeexplore.ieee.org/document/8601100
- **Abstract**: In this paper, a turbo-like extrinsic information transfer (EXIT) algorithm is proposed for two-dimensional magnetic recording (TDMR) systems. Based on the proposed turbo-like EXIT algorithm, we not only analyze the decoding threshold of spatially coupled protograph (SC-P) low-density parity-check (LDPC) codes over TDMR channels under turbo detection, but also conceive a design methodology to construct capacity-approaching terminated SC-P codes. Compared with the original protograph codes, the terminated SC- P codes possess desirable performance gains in both low and high signal-to-noise-ratio (SNR) regions.

## Polar Code Design for Ultra-High Density Magnetic Recording Channels

- **ID**: ieee:8601037
- **Type**: conference
- **Published**: 15-17 Nov.
- **Authors**: Lingjun Kong, Jianhui Bian, Siqi Zhang +2
- **PDF**: https://ieeexplore.ieee.org/document/8601037
- **Abstract**: A simple Polar code optimization algorithm for a two-dimensional (2D) inter-symbol interference (ISI) channel is proposed for ultra-high density magnetic recording, such as bit-patterned magnetic recording (BPMR) and two-dimensional magnetic recording (TDMR), by exploiting the mutual information (MI) between input and output of 2D detector (2D-DET) to re-model the log-likelihood ratio (LLR) messages as Gaussian distribution. The new method, which captures the error characteristics of magnetic recording, builds a bridge of Polar code optimization between the 2D-ISI channels and AWGN channels. The “gap” due to the 2D-ISI, can be computed by the new modeling, so the classic polar code optimization techniques previously developed for the AWGN channel that are not effective can be re-used in 2D-ISI channels.

## Short Length LDPC Code-Candidate for Satellite Control Channel

- **ID**: ieee:8757376
- **Type**: conference
- **Published**: 15-16 Nov.
- **Authors**: Luiza R. Medova, Pavel S. Rybin, Ivan V. Filatov
- **PDF**: https://ieeexplore.ieee.org/document/8757376
- **Abstract**: In this paper we consider the experimental specification for "Short Block Length LDPC codes for TC Synchronization and Channel Coding" by the Consultative Committee for Space Data Systems (CCSDS 231.1-O-1). We consider the methods of constructing LDPC codes and propose the new construction of LDPC code. Numerical results show that proposed construction of LDPC code significantly outperforms one from considered specification under the same decoding algorithm.

## An Adaptive Modulation for Relay-Assisted Wireless Optical Network

- **ID**: ieee:8587883
- **Type**: conference
- **Published**: 15-16 Nov.
- **Authors**: Fethullah Sipahioglu, Volkan Ozduran, Siddik Binboga Yarman
- **PDF**: https://ieeexplore.ieee.org/document/8587883
- **Abstract**: This paper investigates the relay effects on band-width efficiency. The investigation considers that the relay terminals are serially placed between the transmitter and the receiver terminals. The investigation considers that the transmitter terminal possesses the channel state information and also considers log-normal fading channel for the performance analysis. Based on the channel conditions, the transmitter adjusts the modulation sizes in each slot by using the channel state information. During the adaptive transmission, the peak power constraint is addressed to provide eye safety. Results show that the proposed adaptive modulation system significantly enhances bandwidth efficiency in comparison to the non-adaptive system.

## Soft-Decision Statistical Decoder for Coded DHA FH OFDMA

- **ID**: ieee:8757497
- **Type**: conference
- **Published**: 15-16 Nov.
- **Authors**: Alexey Kreshchuk
- **PDF**: https://ieeexplore.ieee.org/document/8757497
- **Abstract**: Statistical decoders have good performance in channels with very low signal to interference ratio (SIR) such as uncoordinated multiple access systems like Dynamic Hopset Allocation Frequency Hopping OFDMA (DHA FH OFDMA). But there was no soft-output statistical decoder developed before. In this work we present such decoder. To get accurate likelihood values we also need to change the structure of statistical decoders. We estimate the performance of the proposed decoder by simulating a concatenated code with outer convolutional code. Having soft decision increases energy gain by 1.5 dB.

## Efficient Four-way Row-splitting Layered QC-LDPC Decoder Architecture

- **ID**: ieee:8649976
- **Type**: conference
- **Published**: 12-15 Nov.
- **Authors**: Tram Thi Bao Nguyen, Hanho Lee
- **PDF**: https://ieeexplore.ieee.org/document/8649976
- **Abstract**: This paper presents a four-way row-splitting architecture for layered low-density parity-check (LDPC) decoder. Based on the proposed method, an efficient partially parallel pipelined QC-LDPC decoder is proposed. The synthesis results using TSMC 40-nm standard cell CMOS technology show that the proposed decoder achieves the maximum required throughput of 7.05 Gb/s and outperforms its predecessors in terms of area efficiency.

## Improved SIFT Feature-Based Watermarking Method for IHC Ver. 5

- **ID**: ieee:8659458
- **Type**: conference
- **Published**: 12-15 Nov.
- **Authors**: Masato Hayashi, Masaki Kawamura
- **PDF**: https://ieeexplore.ieee.org/document/8659458
- **Abstract**: The current scale-invariant feature transform (SIFT) feature-based watermarking method proposed by Kawamura and Uchida was evaluated using Information Hiding Criteria (IHC) ver. 5. The marked regions were selected around the SIFT feature points then normalized to a uniform size against scaling attack, and watermarks were embedded into these normalized regions. There are two problems with this method. One is that the marked regions are distorted by normalization. The other is that the feature points are not detectable due to embedding on the points. Therefore, we propose an improved version of this method to solve these problems. We introduce two improvements called as a gradual magnification factor for normalization and concentric square regions for marked regions. The proposed method was evaluated using IHC ver. 5, and the feature detection rate improved and the bit error rate decreased.

## Multiple Differential Detection with Channel Prediction Employing Soft-Output Per-Survivor Processing

- **ID**: ieee:8659608
- **Type**: conference
- **Published**: 12-15 Nov.
- **Authors**: Kazuki Shimomura, Hiroshi Kubo
- **PDF**: https://ieeexplore.ieee.org/document/8659608
- **Abstract**: In order to improve tracking performance on fast time-varying channels, this paper proposes a soft-output Viterbi algorithm (SOVA) for multiple differential detection (MDD) employing channel prediction and forward error correction. Although QPSK are generally demodulated based on LLR (log-likelihood ratio) for its soft-decisions, it is difficult for joint detection (JD), which does not explicitly estimate channel state information, to derive LLR. This paper proposes soft-output PSP (per-survivor processing), which derives metrics difference between the two paths in the Viterbi algorithm (VA) of PSP, where PSP is JD based on the VA. The proposed scheme can improve tracking performance for time-varying channels without an increase of computational complexity. Finally, computer simulation results confirm that the proposed scheme can track four times larger maximum Doppler frequency normalized by symbol rate in fading than the conventional schemes.

## Construction of Reed-Solomon Based Quasi-Cyclic LDPC Codes Based on Protograph

- **ID**: ieee:8633521
- **Type**: conference
- **Published**: 12-14 Nov.
- **Authors**: Inseon Kim, Hong-Yeop Song
- **PDF**: https://ieeexplore.ieee.org/document/8633521
- **Abstract**: In this paper, we propose construction of Reed-Solomon(RS) based Quasi-Cyclic Low-Density Parity-Check(QC-LDPC) codes using protograph combining two existing QC-LDPC codes construction. One is the construction RS based QC-LDPC codes whose girth is at least 8 and another is protograph based QC-LDPC codes to increase the upper bounds of minimum Hamming distance. We construct the protographs to increase the upper bound of minimum Hamming distance for Proto-RS-QC-LDPC codes and simulate some experiment to show coding gain in sense of BER compare to existing QC-LDPC codes.

## LDPC Code Design via Masking Technology and Progressive Optimization

- **ID**: ieee:8599317
- **Type**: conference
- **Published**: 10-12 Nov.
- **Authors**: Dongliang Guo
- **PDF**: https://ieeexplore.ieee.org/document/8599317
- **Abstract**: A design of low-density parity-check (LDPC) code via the masking technology and progressive optimization is proposed. The code generated by this method has lower computational complexity, and their parity-check matrices can effectively refrain from the girth -4 phenomenon. The proposed method has the superiorities such as better girth-length characteristic and more flexible trim in the length and rate of the code. Experiment results indicate that the error-correction performance of the new code should be better than or as good as the capability of the code which is constructed without been masking. Futhermore, under the condition of short code length, the performance is better than that of LDPC codes via the randomized construction methods.

## Weighted Hard-Reliability Decoding Method for Non-binary LDPC Codes

- **ID**: ieee:8599296
- **Type**: conference
- **Published**: 10-12 Nov.
- **Authors**: Tao Gao, Xiu-rong Ma, Ming-xin Liu
- **PDF**: https://ieeexplore.ieee.org/document/8599296
- **Abstract**: In this paper, we propose a weighted hard-reliability based one step majority-logic decoding algorithm for NON-Binary Low-Density Parity-Check (NB-LDPC) codes. To improve the information reliable of check nodes and the use efficiency of receive message, a weight reliability message method is proposed where only the weight values generated in the decoding initialization are reserved for the iterate decoding process. We also propose a new message reliability updating rule for each iterate decoding, in which only the unreliable variable nodes are updated. Simulation results show that our proposed weighted iterative hard-reliability (WIHRB) algorithm significantly improves the error-floor performance compared to the conventional truncate iterative hard-reliability (TIHRB) algorithms.

## Low-Reliable Low-Latency Networks Optimized for HPC Parallel Applications

- **ID**: ieee:8548063
- **Type**: conference
- **Published**: 1-3 Nov. 2
- **Authors**: Truong Thao Nguyen, Hiroki Matsutani, Michihiro Koibuchi
- **PDF**: https://ieeexplore.ieee.org/document/8548063
- **Abstract**: High-end network standards, such as 400GbE, have been introduced Forwarding Error Correction (FEC) for maintaining the same bit error rate (BER) as that in traditional low-bandwidth interconnection networks. However, FEC operation latency overhead surprisingly becomes higher than the sum of all the other switch operation overheads, e.g., routing computation and switch allocation. FEC operation latency overhead significantly degrades the performance of parallel applications in HPC systems. Instead, in this study, we exploit the low-latency network design using a Hamming code that does not provide rigid error-free communication. Since it is consistent with existing frame format based on standard Reed-Solomon RS(544,514) with DC(64b/66b) direct linecode and TC(256b/257b) transcode, respectively, the influences upon the other network layer design are limited. Interestingly, a large number of parallel applications can accept the BER in such a Hamming code. Since lowering such a BER improves switch operation latency, the proposed network using the Hamming code improves the execution time of NAS Parallel Benchmarks by 56% on average when compared to the counterpart RS-FEC networks.
