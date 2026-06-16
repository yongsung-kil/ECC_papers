# IEEE Xplore — 2011-05


## Improved Stopping Set Elimination by Parity-Check Matrix Extension of LDPC Codes

- **ID**: ieee:5741762
- **Type**: journal
- **Published**: May 2011
- **Authors**: Saejoon Kim, Jun Heo, Hyuncheol Park
- **PDF**: https://ieeexplore.ieee.org/document/5741762
- **Abstract**: Stopping sets associated with a parity-check matrix of low-density parity-check codes limit the performance of iterative decoding over the binary erasure channel. In this letter, we propose a parity-check matrix extension scheme that eliminates stopping sets of small sizes. The results show that our proposed scheme provides significant performance improvement compared to previously known parity-check matrix extension schemes.

## Network Coded LDPC Code Design for a Multi-Source Relaying System

- **ID**: ieee:5740635
- **Type**: journal
- **Published**: May 2011
- **Authors**: Jun Li, Jinhong Yuan, Robert Malaney +2
- **PDF**: https://ieeexplore.ieee.org/document/5740635
- **Abstract**: We investigate LDPC code design for a multi-source single-relay system, with uniform phase-fading Gaussian channels. We specifically consider the asymmetric channels for multiple sources, where the channel condition for each source in the system is different. We focus on LDPC code design when network coding (NC) at the relay is utilized. For the asymmetric sources, we firstly introduce a binary field rate splitting theorem which is used to discover an appropriate NC scheme at the relay. This NC scheme is then used to determine the achievable rates of each source and the whole system. These steps assist us in the development of the main contribution of our work, namely, network coded multi-edge type LDPC (NCMET-LDPC) code design. Extrinsic mutual information transfer (EXIT) chart analysis is utilized to optimize the code profiles. Our results demonstrate two key points. (1) From the whole system point of view, our NCMET-LDPC codes achieve better error performance than that of LDPC codes designed for the system without NC. (2) As a consequence of the binary field rate-splitting theorem, our NCMET-LDPC codes also guarantee better error performance of each asymmetric source. The improvement in error performance is typically about 0.3 dB relative to a system without NC.

## Symbol-Level Synchronization and LDPC Code Design for Insertion/Deletion Channels

- **ID**: ieee:5733455
- **Type**: journal
- **Published**: May 2011
- **Authors**: Feng Wang, Dario Fertonani, Tolga M. Duman
- **PDF**: https://ieeexplore.ieee.org/document/5733455
- **Abstract**: We investigate a promising coding scheme over channels impaired by insertion, deletion, and substitution errors, i.e., interleaved concatenation of an outer low-density parity-check (LDPC) code with error-correction capabilities and an inner marker code for synchronization purposes. To limit the decoding latency, we start with a single-pass decoding algorithm, that is, marker code-based synchronization is performed only once per received packet and iterative decoding with information exchange between the inner decoder and outer decoder is not allowed. Through numerical evaluations, we first find the marker code structures which offer the ultimate achievable rate when standard bit-level synchronization is performed. Then, to exploit the correlations in the likelihoods corresponding to different transmitted bits, we introduce a novel symbol-level synchronization algorithm that works on groups of consecutive bits, and show how it improves the achievable rate along with the error rate performance by capturing part of the rate loss due to interleaving. When decoding latency is not an issue and multiple-pass decoding is performed, we utilize extrinsic information transfer (EXIT) charts to analyze the convergence behavior of the receiver, which leads to design of outer LDPC codes with good degree distributions. Finally, design examples are provided along with simulation results which confirm the advantage of the newly designed codes over the ones optimized for the standard additive white Gaussian noise (AWGN) channels, especially for channels with severe synchronization problems.

## Efficient LLR Calculation for Non-Binary Modulations over Fading Channels

- **ID**: ieee:5723044
- **Type**: journal
- **Published**: May 2011
- **Authors**: Raman Yazdani, Masoud Ardakani
- **PDF**: https://ieeexplore.ieee.org/document/5723044
- **Abstract**: Log-likelihood ratio (LLR) computation for non-binary modulations over fading channels is complicated. A measure of LLR accuracy on asymmetric binary channels is introduced to facilitate good LLR approximations for non-binary modulations. Considering piecewise linear LLR approximations, we prove convexity of optimizing the coefficients according to this measure. For the optimized approximate LLRs, we report negligible performance loss compared to true LLRs.

## Pseudocodeword Weights for LDPC Codes under Differential PSK Transmission over the Noncoherent AWGN Channel

- **ID**: ieee:5723052
- **Type**: journal
- **Published**: May 2011
- **Authors**: Elisa Mo, Marc A. Armand
- **PDF**: https://ieeexplore.ieee.org/document/5723052
- **Abstract**: This Letter considers the finite-length analysis of iterative decoding of low-density parity-check codes under differential binary-phase-shift-keying (DBPSK) and differential quadrature-phase-shift-keying (DQPSK) over the noncoherent additive-white-Gaussian-noise channel. Specifically, we derive the weight of the pseudocodewords of a Tanner graph under these signaling schemes and use them to explain the difference in error performance between coded DBPSK and coded DQPSK.

## A new post-viterbi processor based on soft-reliability information

- **ID**: ieee:5955231
- **Type**: journal
- **Published**: May 2011
- **Authors**: Jun Lee, Kees A. Schouhamer Immink
- **PDF**: https://ieeexplore.ieee.org/document/5955231
- **Abstract**: This paper proposes a soft-reliability informationbased post-Viterbi processor for reducing miss-correction of an error correlation filter-based post-Viterbi processor. The essential difference between the soft-reliability informationbased and the error correlation filter-based post-Viterbi processors, is how to locate the most probable error starting position. The new scheme determines an error starting position based on a soft-reliability estimate, while the conventional scheme chooses an error starting position based on likelihood value. Among all likely error starting positions for prescribed error events, the new scheme attempts to correct errortype corresponding to the position only if there exists a position where the soft-reliability estimate is negative, while the conventional scheme performs error correction based on errortype and its error starting position of an error event associated with the maximum likelihood value. A correction made by the conventional scheme may result in miss-correction because the scheme does not have any criterion for judgment whether an estimated error starting position is correct. In case error correction is only performed when a position with negative soft-reliability estimate exists, the probability of miss-correction of the new scheme is less than the one of the conventional scheme.

## Dynamic Decode-and-Forward Relaying using Raptor Codes

- **ID**: ieee:5737896
- **Type**: journal
- **Published**: May 2011
- **Authors**: Azad Ravanshid, Lutz Lampe, Johannes B. Huber
- **PDF**: https://ieeexplore.ieee.org/document/5737896
- **Abstract**: Dynamic decode-and-forward (DDF) is a version of decode-and-forward relaying in which the duration of the listening phase at relays is not fixed. In this paper, we investigate half-duplex DDF relaying based on rateless codes. The use of rateless codes allows relays to autonomously switch from listening to the source node to transmitting to the destination node. We first revisit different signal combining strategies applied at the destination node, namely energy and information combining known from literature, and propose a new combining method which we refer to as mixed combining. The different combining methods give rise to different achievable rates, i.e., constrained channel capacities, for which we provide analytical expressions. The capacity analysis reveals the conditions under which mixed combining is superior and how it can be optimized. We then consider Raptor codes as a specific implementation of rateless codes and develop a density-evolution approximation to predict the data-rate performance of these codes in DDF relaying. Furthermore, we devise an optimization of the output symbol degree distribution of Raptor codes that is mainly used to benchmark the performance of Raptor codes with a fixed degree distribution. Numerical results for exemplary three-node and four-node relay networks show that the proposed mixed combining provides significant gains in achievable data rate and that Raptor codes with a fixed degree distribution are able to realize these gains and to approach closely the constrained-capacity limits.

## Energy Efficiency and Reliability in Wireless Biomedical Implant Systems

- **ID**: ieee:5685568
- **Type**: journal
- **Published**: May 2011
- **Authors**: Jamshid Abouei, J. David Brown, Konstantinos N. Plataniotis +1
- **PDF**: https://ieeexplore.ieee.org/document/5685568
- **Abstract**: The use of wireless implant technology requires correct delivery of the vital physiological signs of the patient along with the energy management in power-constrained devices. Toward these goals, we present an augmentation protocol for the physical layer of the medical implant communications service (MICS) with focus on the energy efficiency of deployed devices over the MICS frequency band. The present protocol uses the rateless code with the frequency-shift keying (FSK) modulation scheme to overcome the reliability and power cost concerns in tiny implantable sensors due to the considerable attenuation of propagated signals across the human body. In addition, the protocol allows a fast start-up time for the transceiver circuitry. The main advantage of using rateless codes is to provide an inherent adaptive duty cycling for power management, due to the flexibility of the rateless code rate. Analytical results demonstrate that an 80% energy saving is achievable with the proposed protocol when compared to the IEEE 802.15.4 physical layer standard with the same structure used for wireless sensor networks. Numerical results show that the optimized rateless coded FSK is more energy efficient than that of the uncoded FSK scheme for deep tissue (e.g., digestive endoscopy) applications, where the optimization is performed over modulation and coding parameters.

## Beat Noise Compensation in OCDMA Systems Using Soft Decoding Based FEC

- **ID**: ieee:5766672
- **Type**: journal
- **Published**: May 2011
- **Authors**: S. Sahuguede, A. Julien-Vergonjanne, J.P. Cances
- **PDF**: https://ieeexplore.ieee.org/document/5766672
- **Abstract**: In this paper we study Forward Error Correction (FEC) under beat noise assumption in the context of incoherent Optical Code Division Multiple Access (OCDMA) systems. Due to the use of unipolar codes, Multiple Access Interference (MAI) amount and thus beatings between different user contributions known as beat noise, constitute important limitations in particular for high data rates. In order to compensate for these two major limitations, we propose a solution using FEC based on a soft decoding algorithm. For this purpose, we analyze the OCDMA received signal distribution and establish a new model, based on a mixture of chi-square distributions, valuable for any OCDMA code parameters and any source coherence time values. From this model, we establish the error probability analytical expression under beat noise assumption and determine the reliability parameters required for the FEC soft decoder initialization. To illustrate the performance, we use Low Density Parity Check (LDPC) codes and show that the LDPC adapted decoder is highly efficient in reducing beat noise and MAI for incoherent OCDMA systems, even when beat noise has a severe impact. In addition, we point out that this solution permits increasing data rates or number of active users.

## An LDPC-based improved decoding scheme for distributed video codec

- **ID**: ieee:5898939
- **Type**: conference
- **Published**: 8-11 May 2
- **Authors**: Bin Li, Yumei Wang, Qing Huang +1
- **PDF**: https://ieeexplore.ieee.org/document/5898939
- **Abstract**: Low-density Parity-Check (LDPC) code is widely used in distributed video coding (DVC) to realizing Wyner-Ziv (WZ) coding for its better performance than other channel codes. However, during the LDPC decoding process, most of DVC solutions do not make use of the video character to help decoding. In this paper, we propose an improved LDPC decoding scheme for DVC by utilizing the movement of the objects in the video sequence to partition different confidence areas for the side information (SI). The pixels in the SI correspond to different confidence areas, and the corresponding binary representations of the pixels will have different likelihood-ratio (LLR) initialization methods which are used to generate the LLR values for LDPC iterative decoding. The experimental results show that with the proposed decoding scheme the PSNR gain can reach up to 0.8 db without increasing the decoding complexity.

## An amendment to IEEE 802.17 (RPR) for wireless transport

- **ID**: ieee:5898966
- **Type**: conference
- **Published**: 8-11 May 2
- **Authors**: S. Athanasiadou, G. Stamatelos
- **PDF**: https://ieeexplore.ieee.org/document/5898966
- **Abstract**: The Resilient Packet Ring (RPR) is a packet network technology designed to provide broadband traffic transport in a metropolitan area according to IEEE 802.17 specifications. Its advantages include flexibility in bandwidth allocation, fairness and traffic shaping criteria for the acceptance of elastic transit traffic, as well as highly reliable transport. Here we focus on possible future amendments to these specifications (such as inclusion of efficient coding / modulation schemes) that would allow RPRs to support reliably wireless traffic as well.

## Link adaptation for fixed relaying with untrusted relays: Transmission strategy design and performance analysis

- **ID**: ieee:5898941
- **Type**: conference
- **Published**: 8-11 May 2
- **Authors**: Hamid Khodakarami, Farshad Lahouti
- **PDF**: https://ieeexplore.ieee.org/document/5898941
- **Abstract**: Wireless cooperative communication through link adaptation with untrusted relay assignment is considered. Using sharp channel codes in different transmission modes, reliability for destination and security in the presence of untrusted relays are provided through rate and power allocation. Scenarios with single available relay and opportunistic relaying in the presence of multiple relays are investigated. These scenarios are analyzed separately in terms of performance over Rayleigh fading channel for constant power and adaptive power transmission. In constant power case, closed form expressions for average spectral efficiency is derived through an effective approximation. Retaining the sum transmission power of source and relay unchanged, the performance of system is enhanced through power allocation. Numerical results reflect the effectiveness of the approximations for analytic performance evaluation when comparing to the simulation results.

## An efficient equivalent channel model for LDPC coded BICM-ID system

- **ID**: ieee:6013535
- **Type**: conference
- **Published**: 27-29 May 
- **Authors**: Huiyun Jiang, Lei Xie, Huifang Chen
- **PDF**: https://ieeexplore.ieee.org/document/6013535
- **Abstract**: This paper focuses on the analysis of the decoding algorithm for low-density parity-check (LDPC) coded bit-interleaved coded modulation with iterative decoding (BICM-ID) scheme. An equivalent channel model for hard-decision feedback and soft-decision feedback iterative decoding is proposed. With the theory of independent and identically distributed (i.i.d.) binary transmitted system, the equivalent model is structured by random move between different points in the constellation and elimination of the effects of it afterwards. It is proved in the literature that by using the simplified method, the transmitter only considering all-zeros codeword suffices to elaborate the error performance compared with the entire encode-decode system. Simulation results show that conventional LDPC coded BICM-ID system and the simplified all-zeros model have the same expected decoder behavior. The proposed technique is flexible in LDPC coded BICM-ID system using the binary sum-product algorithm (SPA) and can be extended to any communication systems based on linear code and binary iterative decoder, which can bring about low complexity implementation during the simulation.

## Performance of LDPC codes in wideband shortwave channel

- **ID**: ieee:6014341
- **Type**: conference
- **Published**: 27-29 May 
- **Authors**: Zhao Danfeng, Zhang Yaqian, Zhu Tielin
- **PDF**: https://ieeexplore.ieee.org/document/6014341
- **Abstract**: To reduce the effect of multi-path and Doppler on the bit error rate performance in the shortwave broadband channel, LDPC code with probable checking matrix and an improved decoding algorithm is introduced to ensure the reliability of the system as channel encoding. Combined with MC-CDMA technology which can inhibit the multi-path interference effectively, the LDPC+OFDM+DSSS scheme is proposed. Using the equalization techniques to recover received signals, the simulation model is built by the analysis of shortwave broadband channel based on ITS model. Simulation results show that: the program not only can inhibit the symbol interference effectively, but also can reduce the sensitivity of the communication system to Doppler frequency and reach a better bit error rate performance.

## Regular network low density parity check codes for multiple-access relay channel

- **ID**: ieee:6013677
- **Type**: conference
- **Published**: 27-29 May 
- **Authors**: Guanghui Song, Jun Cheng, Yoichiro Watanabe
- **PDF**: https://ieeexplore.ieee.org/document/6013677
- **Abstract**: Regular network low density parity check (NLDPC) codes are proposed for the multiple-access relay channel with two sources, one relay and one destination. A three-layer Tanner graph is used to describe the code, where the coded bits from the two sources and the coded bits from the relay are separated into two different layers. This makes it possible to design the code more flexibly. A three-layer Gaussian approximation algorithm is developed to calculate the mean values of messages propagated between the layers during decoding iterations. The separation of coded bits from the sources and the relay, which produces the three-layer graph, makes the calculation more accurate. With threshold analysis, it is shown that the regular NLDPC codes are optimal when the degrees of the variable nodes in the middle layer and the lower layer are unitary.

## An effective and efficiency anti-collusion fingerprint scheme for multimedia

- **ID**: ieee:6013615
- **Type**: conference
- **Published**: 27-29 May 
- **Authors**: Huang Jun, Li Qiaoliang
- **PDF**: https://ieeexplore.ieee.org/document/6013615
- **Abstract**: We proposed an effective and efficiency anti-collusion fingerprint scheme based on inner code with orthogonal fingerprint in tandem and outer code with LDPC code that can not only have a good collusion-free performance in the fingerprint system but also have good error correct performance and can resist many other attacks unconsciously such as noise, which protected distributor's copyright and data integrity.

## Code-aided synchronization algorithm based on posterior probability

- **ID**: ieee:6014343
- **Type**: conference
- **Published**: 27-29 May 
- **Authors**: Danfeng Zhao, Tielin Zhu, Yaqian Zhang
- **PDF**: https://ieeexplore.ieee.org/document/6014343
- **Abstract**: For the error-correcting performance deterioration of Low Density Parity Check Code (LDPC) due to the synchronization loss at very low signal to noise ratio (SNR) environment, a code-aided synchronization algorithm named maximum-mean posterior probability is proposed. Firstly, improved data-aided method is adopted. Cursory synchronization parameters are estimated using encoded training sequence to ensure the timing error less than one symbol period. And then error information is fed back according to the distribution of posterior probability. The algorithm takes the decoding information as reference and brings the error correcting function of decoder into play supporting synchronous step. Synchronization accuracy is effectively improved. Finally, LDPC-CPM simulation model is established in allusion to Continuous Phase Modulation (CPM) signal. Simulation results show that the algorithm can accurately complete the timing and phase estimates and make the iterative system achieve reliability as ideal synchronization at very low SNR.

## Research and design of storage systems with high availability in campus network

- **ID**: ieee:6013710
- **Type**: conference
- **Published**: 27-29 May 
- **Authors**: Li Sen, Ma Yan
- **PDF**: https://ieeexplore.ieee.org/document/6013710
- **Abstract**: This article makes a detailed analysis and discussion based on the analysis of the working principle and features of the redundant technology and in aspect of improving the availability of the system. The result indicates that the redundant technology can improve MTBF of the system effectively which can improve the availability of the system. The high availability of the storage subsystem and resource subsystem will decide the availability of the campus network. The network attached storage technology has advantages of high reliability, easy management and extensibility. Combined with the utilization of network attached storage technology and data backup technology, storage systems with high availability are designed, which can provide solutions for network storage needs with high availability.

## Analysis of balanced cycles of QC-LDPC codes

- **ID**: ieee:5872931
- **Type**: conference
- **Published**: 24-26 May 
- **Authors**: Gao Xiao, Zhang Nan
- **PDF**: https://ieeexplore.ieee.org/document/5872931
- **Abstract**: In this paper, we analyze balanced cycles of quasi-cyclic low-density parity-check (QC-LDPC) codes. We show the structure of balanced cycles and their necessary and sufficient existence conditions. Furthermore, we determine the minimal matrices of balanced cycle. Meanwhile we propose the property of B-girth in its mother matrix. Finally, we give the proof in theory.

## Real-time DVB-S2 LDPC decoding on many-core GPU accelerators

- **ID**: ieee:5946824
- **Type**: conference
- **Published**: 22-27 May 
- **Authors**: Gabriel Falcao, Joao Andrade, Vitor Silva +1
- **PDF**: https://ieeexplore.ieee.org/document/5946824
- **Abstract**: It is well known that LDPC decoding is computationally demanding and one of the hardest signal operations to parallelize. Beyond data dependencies that restrict the decoding of a single word, it requires a large number of memory accesses. In this paper we propose parallel algorithms for performing in CPUs the most demanding case of irregular and long length LDPC codes adopted in the Digital Video Broadcasting Satellite 2 (DVB-S2) standard used in data communications. By performing simultaneous multicodeword decoding and adopting special data structures, experimental results show that throughputs superior to 90 Mbps can be achieved when LDPC decoders for the DVB-S2 are implemented in the current CPUs.

## Fourier domain decoding algorithm of non-binary LDPC codes for parallel implementation

- **ID**: ieee:5946358
- **Type**: conference
- **Published**: 22-27 May 
- **Authors**: Kenta Kasai, Koichi Sakaniwa
- **PDF**: https://ieeexplore.ieee.org/document/5946358
- **Abstract**: For decoding non-binary low-density parity-check (LDPC) codes, logarithm-domain sum-product (Log-SP) algorithms were proposed for reducing quantization effects of SP algorithm in conjunction with FFT. Since FFT is not applicable in the logarithm domain, the computations required at check nodes in the Log-SP algorithms are computationally intensive. What is worse, check nodes usually have higher degree than variable nodes. As a result, most of the time for decoding is used for check node computations, which leads to a bottleneck effect. In this paper, we propose a Log-SP algorithm in the Fourier domain. With this algorithm, the role of variable nodes and check nodes are switched. The intensive computations are spread over lower-degree variable nodes, which can be efficiently calculated in parallel. Furthermore, we develop a fast calculation method for the estimated bits and syndromes in the Fourier domain.

## Low-complexity detection of golden codes in LDPC-coded OFDM systems

- **ID**: ieee:5946692
- **Type**: conference
- **Published**: 22-27 May 
- **Authors**: Iker Sobrón, Maitane Barrenechea, Pello Ochandiano +3
- **PDF**: https://ieeexplore.ieee.org/document/5946692
- **Abstract**: Recent and next-generation wireless broadcasting standards, such as DVB-T2 or DVB-NGH, are considering distributed multi-antenna transmission in order to increase bandwidth efficiency and signal quality. Full-rate full-diversity (FRFD) space-time codes (STC), such as the Golden code, have been reported to be excellent candidates, being their main drawback their detection complexity, which is enhanced when soft output is required when combined with a bit interleaved coded modulation (BICM) scheme based on low-density parity check (LDPC) codes. We present a novel low-complexity soft detection algorithm for the reception of Golden codes in LDPC based orthogonal frequency-division multiplexing (OFDM) systems. Complexity and simulation-based performance results are provided which show that the proposed detector performs close to the optimal detector in a variety of DVB-T2 broadcasting scenarios.

## Nonbinary LDPC decoding by min-sum with Adaptive Message Control

- **ID**: ieee:5946693
- **Type**: conference
- **Published**: 22-27 May 
- **Authors**: Weiguo Tang, Jie Huang, Lei Wang +1
- **PDF**: https://ieeexplore.ieee.org/document/5946693
- **Abstract**: A new decoding algorithm, referred to as Min-Sum with Adaptive Message Control (AMC-MS), is proposed to reduce the decoding complexity of nonbinary LDPC codes. The proposed algorithm adaptively trims the message length of belief information to reduce the amount of arithmetic operations. Exploiting the fact that during the decoding iteration, the distribution of belief information will become more concentrated around the correct element in the case of convergence, the messages can be truncated accordingly by considering only a few entries with large likelihood. Simulation results with a GF(16) nonbinary LDPC code indicate that the proposed approach can reduce arithmetic operations by up to 65% compared with non-truncated cases. Compared with the state-of-the-art extended MS (EMS) decoding, the proposed AMC-MS algorithm can reduce the computation by up to 50%, thereby enabling low-complexity decoding of nonbinary LDPC codes.

## Practical codes for lossy compression when side information may be absent

- **ID**: ieee:5946301
- **Type**: conference
- **Published**: 22-27 May 
- **Authors**: Sivagnanasundaram Ramanan, John MacLaren Walsh
- **PDF**: https://ieeexplore.ieee.org/document/5946301
- **Abstract**: Practical codes are developed for quadratic Gaussian lossy compression when side information may be absent by hybridizing successively refinable trellis coded quantization (SR-TCQ) and low-density parity-check (LDPC) codes. A 2-refinement level SR-TCQ is used to generate a common description for both decoders and an individual description for the decoder with side information. Then, the common description is losslessly compressed while the individual description is compressed using a LDPC code which exploits the side information in a belief propagation decoder. Simulation results show that the practical codes require no more than 0.46 extra bits at moderate rates and no more than 0.7 extra bits at low rates from the theoretical bounds.

## Multiple LDPC decoding using bitplane correlation for Transform Domain Wyner-Ziv video coding

- **ID**: ieee:5946783
- **Type**: conference
- **Published**: 22-27 May 
- **Authors**: Huynh Van Luong, Xin Huang, Søren Forchhammer
- **PDF**: https://ieeexplore.ieee.org/document/5946783
- **Abstract**: Distributed video coding (DVC) is an emerging video coding paradigm for systems which fully or partly exploit the source statistics at the decoder to reduce the computational burden at the encoder. This paper considers a Low Density Parity Check (LDPC) based Transform Domain Wyner-Ziv (TDWZ) video codec. To improve the LDPC coding performance in the context of TDWZ, this paper proposes a Wyner-Ziv video codec using bitplane correlation through multiple parallel LDPC decoding. The proposed scheme utilizes inter bitplane correlation to enhance the bitplane decoding performance. Experimental results show that the proposed scheme reduces the bit rate up to 3.9% and improves the rate-distortion (RD) performance of TDWZ.

## Correlation estimation with particle-based belief propagation for distributed video coding

- **ID**: ieee:5946779
- **Type**: conference
- **Published**: 22-27 May 
- **Authors**: Lina Stankovic, Vladimir Stankovic, Shuang Wang +1
- **PDF**: https://ieeexplore.ieee.org/document/5946779
- **Abstract**: In this paper, we propose an adaptive Distributed Video Coding (DVC) scheme that dynamically estimates correlation statistics of the scene in a video sequence to enhance belief-propagation (BP) Slepian-Wolf (SW) decoding. In order to exploit the robustness of distributed source coding (DSC) designs, we integrate particle filtering with standard BP decoding in one factor graph to estimate online correlation among source and side information. Our proposed system boasts improved performance over classical DVC without correlation estimation, due to improved knowledge of correlation statistics via the combination of bit-plane coding and particle-based BP tracking in each frame, as shown by our results.

## A flexible high-throughput hardware architecture for a gaussian noise generator

- **ID**: ieee:5946821
- **Type**: conference
- **Published**: 22-27 May 
- **Authors**: I. Paraskevakos, V. Paliouras
- **PDF**: https://ieeexplore.ieee.org/document/5946821
- **Abstract**: In this paper a flexible, high-throughput, low-complexity additive white gaussian noise (AWGN) channel generator is presented. The proposed generator employs a Mersemie-Twister to generate a long random number uniformly distributed sequence and a Box-Muller transformation implementation to derive gaussian noise samples. Emphasis is given on developing a high-throughput approximation unit for die elementary functions required for die transformation. The proposed techniques are shown to lead to solutions that provide four samples per clock, which in turn can sustain throughputs of 584MSps, with moderate clock frequency and hardware complexity.

## Gaussian approximation of the LLR distribution for the ML and partial marginalization MIMO detectors

- **ID**: ieee:5946710
- **Type**: conference
- **Published**: 22-27 May 
- **Authors**: Mirsad Čirkić, Daniel Persson, Erik G. Larsson +1
- **PDF**: https://ieeexplore.ieee.org/document/5946710
- **Abstract**: We derive a Gaussian approximation of the LLR distribution conditioned on the transmitted signal and the channel matrix for the soft-output via partial marginalization MIMO detector. This detector performs exact ML as a special case. Our main results consist of discussing the operational meaning of this approximation and a proof that, in the limit of high SNR, the LLR distribution of interest converges in probability towards a Gaussian distribution.

## Factor graph-based structural equilibria in dynamical games

- **ID**: ieee:5946894
- **Type**: conference
- **Published**: 22-27 May 
- **Authors**: Liming Wang, Vikram Krishnamurthy, Dan Schonfeld
- **PDF**: https://ieeexplore.ieee.org/document/5946894
- **Abstract**: Correlated equilibria are a generalization of Nash equilibria that permit agents to act in a correlated manner and can there fore, model learning in games. In this paper we define a special class of correlated equilibria that have hierarchical structure based on the factor graph. Such factor graph-based structural equilibria are more general than Nash equilibria and can model constrained dependencies than general correlated equilibria. We provide the numerical example for using non cooperative stochastic game model on the gene regulatory network under three solution concepts.

## A methodology based on Transportation problem modeling for designing parallel interleaver architectures

- **ID**: ieee:5946806
- **Type**: conference
- **Published**: 22-27 May 
- **Authors**: Awais Sani, Philippe Coussy, Cyrille Chavet +1
- **PDF**: https://ieeexplore.ieee.org/document/5946806
- **Abstract**: For high-data-rate applications, turbo-like iterative decoders are implemented with parallel hardware architecture. However, to achieve high throughput, concurrent accesses to each memory bank has to be performed without any conflict. The consideration applies to the two main classes of turbo-like codes: Low Density Parity Check (LDPC) and Turbo-Codes. In this paper, we present an original approach based on Transportation problem modeling which finds conflict free memory mapping for every type of turbo codes and which optimizes the resulting interleaving architecture.

## Bridging Lithography Processes with NAND Flash ECC Complexity

- **ID**: ieee:5873235
- **Type**: conference
- **Published**: 22-25 May 
- **Authors**: P. Poliakov, P. Blomme, A. Vaglio Pret +3
- **PDF**: https://ieeexplore.ieee.org/document/5873235
- **Abstract**: The NAND Flash memory is the technological driver for both critical dimensions scaling and process technologies. In order to keep pace with the Moore's Law, the scale chip dimensions decrease to the point where variability effects become significant. Particularly, when printed features go down below the 20 nm, transistors structures are strongly affected by pattern roughness caused by the randomness in advanced lithographies (e.g. Extreme UV), leading to variability induced data errors in the memory functionality. Two treatments for variability are known: roughness smoothing processes at the process stage and on-chip error correcting algorithms. This paper describes a holistic framework, which trades-off between lithography processes and error control codes complexity to ensure data integrity in probabilistic 16 nm memories.

## Decoding of long-block soft decision LDPC codes for optical communication systems

- **ID**: ieee:5953744
- **Type**: conference
- **Published**: 18-20 May 
- **Authors**: M. N. Sakib, A. J. Wong, W. J. Gross +1
- **PDF**: https://ieeexplore.ieee.org/document/5953744
- **Abstract**: We investigate a soft decision decoder for LDPC codes with long-block size. The results show a coding gain of 5.9 dB compared to an uncoded system and 1.5 dB over a hard decision receiver.

## Design of multi-edge-type LDPC codes for high-order coded modulation

- **ID**: ieee:5872111
- **Type**: conference
- **Published**: 17-20 May 
- **Authors**: Lei Zhang, Frank R. Kschischang
- **PDF**: https://ieeexplore.ieee.org/document/5872111
- **Abstract**: A design method for bandwidth-efficient LDPC coded modulation for 22m-QAM constellations at rate (2m - 1)/(2m) in complex AWGN is presented. A multi-edge-type parameterization is used to exploit the distinct bit-channel capacities unique to high-order modulation using LDPC structures. EXIT analysis is adapted to multi-edge by introducing multi-dimensional EXIT iterated-function system analysis. Under this conceptualization, a successful decoding condition is developed by estimating fixed points of the dynamical system using its numerical gradient. Optimized ensembles are found for 16-QAM with thresholds matching the best known ensembles of equal complexity. For 64 to 1024-QAM, sufficiently high bit-channel capacities allow for extension of lower-order optimized ensembles, leading a practical nested code structure. The nested structure provides flexible rate selection with a single decoder. The gap to constrained, non-iterative capacity of all optimized code ensembles of maximum variable degree of 15 is within 0.21 dB.

## A new approach for FEC decoding based on the BP algorithm in LTE and WiMAX systems

- **ID**: ieee:5872112
- **Type**: conference
- **Published**: 17-20 May 
- **Authors**: Ahmed Refaey, Sébastien Roy, Paul Fortier
- **PDF**: https://ieeexplore.ieee.org/document/5872112
- **Abstract**: Many wireless communication systems such as IS-54, enhanced data rates for the GSM evolution (EDGE), worldwide interoperability for microwave access (WiMAX) and long term evolution (LTE) have adopted low-density parity-check (LDPC), tail-biting convolutional, and turbo codes as the forward error correcting codes (FEC) scheme for data and overhead channels. Therefore, many efficient algorithms have been proposed for decoding these codes. However, the different decoding approaches for these two families of codes usually lead to different hardware architectures. Since these codes work side by side in these new wireless systems, it is a good idea to introduce a universal decoder to handle these two families of codes. The present work exploits the parity-check matrix (H) representation of tail-biting convolutional and turbo codes, thus enabling decoding via a unified belief propagation (BP) algorithm. Indeed, the BP algorithm provides a highly effective general methodology for devising low-complexity iterative decoding algorithms for all convolutional code classes as well as turbo codes. While a small performance loss is observed when decoding turbo codes with BP instead of MAP, this is offset by the lower complexity of the BP algorithm and the inherent advantage of a unified decoding architecture.

## Combinatorial Properties as Predictors for the Performance of the Sum-Product Algorithm

- **ID**: ieee:5872141
- **Type**: conference
- **Published**: 17-20 May 
- **Authors**: Sotiria Lampoudi, John Brevik, Michael E. O'Sullivan
- **PDF**: https://ieeexplore.ieee.org/document/5872141
- **Abstract**: We examine various algebraic/combinatorial properties of Low-Density Parity-Check codes as predictors for the performance of the sum-product algorithm on the AWGN channel in the error floor region. We consider three families of check matrices, two algebraically constructed and one sampled from an ensemble, expurgated to remove short cycles. The three families have similar properties, all are (3; 6)-regular, have girth 8, and have code length roughly 280. The best predictors are small trapping sets, and the predictive value is much higher for the algebraically constructed families than the random ones.

## Low complexity piecewise linear LLR calculation for MIMO-BICM systems

- **ID**: ieee:5872149
- **Type**: conference
- **Published**: 17-20 May 
- **Authors**: Chao Zheng, Raman Yazdani, Masoud Ardakani
- **PDF**: https://ieeexplore.ieee.org/document/5872149
- **Abstract**: Log-likelihood ratios (LLRs) are efficient metrics used in the decoding of modern channel codes such as low-density parity-check and turbo codes. LLR calculation, however, can be a complex task since LLRs are usually complicated nonlinear functions of the channel output. In multi-input multioutput (MIMO) channels, the complexity of the calculation increases exponentially with the number of antennas. In this paper, an LLR approximation method is proposed for MIMO-BICM systems. In particular, piecewise linear approximation functions are introduced and an accuracy measure is provided to optimize the parameters. Simulations verify that the performance of the optimized approximate LLRs is better than the existing approximation method and quite close to that of true LLRs.

## Using variable-length codes to correct Insertion, Deletion and substitution errors

- **ID**: ieee:5872143
- **Type**: conference
- **Published**: 17-20 May 
- **Authors**: Victor Buttigieg
- **PDF**: https://ieeexplore.ieee.org/document/5872143
- **Abstract**: A maximum likelihood metric is derived for the decoding of variable-length codes over a Binary Substitution, Insertion and Deletion channel. Using this metric a near-maximum likelihood decoder is derived. It is shown that variable-length codes can be used effectively to correct for insertion, deletion and substitution errors.

## Implementation of LDPC Encoding to DTMB Standard Based on FPGA

- **ID**: ieee:6086476
- **Type**: conference
- **Published**: 16-18 May 
- **Authors**: Xiang Ouyang, Changcheng Ruan, Lingxiang Zheng
- **PDF**: https://ieeexplore.ieee.org/document/6086476
- **Abstract**: In this paper, an implementation of Low-Density Parity-Check (LDPC) encoder is introduced, which meets the demand of Chinese Digital Terrestrial Multimedia Broadcasting (DTMB) standard. A design of the LDPC encoder which uses a partially-parallel encoding structure based on the Shift Register Adder Accumulator (SRAA) circuit is studied according to the irregular quasi-cyclic characteristic of LDPC encoding specified by the standard. Then we use the FPGA to implement the design. The simulation and implementation results show that the design meets the requirement of DTMB standard and reduces the resource usage.

## Memory efficient layered decoder design with early termination for LDPC codes

- **ID**: ieee:5938161
- **Type**: conference
- **Published**: 15-18 May 
- **Authors**: Jiangpeng Li, Guanghui He, Hexi Hou +2
- **PDF**: https://ieeexplore.ieee.org/document/5938161
- **Abstract**: Layered structure is widely used in the design of Low-Density Parity-Check (LDPC) code decoders due to its fast convergence speed. However, correct checking process is difficult to implement in layered decoder, which results in unnecessary iterations. In this paper, an early termination strategy is presented for layered LDPC decoder to avoid redundant number of iterations. This approach makes use of the comparison between current log-likelyhood ratios (LLRs) and updated LLRs of all variable nodes to determine termination criteria of iterations. Furthermore, a non-uniform quantization scheme and an extrinsic messages memory optimization scheme are developed for memory savings. Based on these proposed methods, an LDPC decoder for the Chinese digital mobile TV applications is implemented using a SMIC 130nm CMOS process. The decoder consumes only 171 Kbits memory while achieving 267Mbps for code rate 1/2, and 401Mbps for code rate 3/4.

## Low power LDPC decoder with efficient stopping scheme for undecodable blocks

- **ID**: ieee:5937929
- **Type**: conference
- **Published**: 15-18 May 
- **Authors**: Tinoosh Mohsenin, Houshmand Shirani-mehr, Bevan Baas
- **PDF**: https://ieeexplore.ieee.org/document/5937929
- **Abstract**: An efficient technique for early detection of undecodable blocks during LDPC decoding is introduced. The proposed method avoids unnecessary decoding iterations by predicting decoding failure and therefore results in significant improvement in power and latency in low SNR values. The proposed method which has a low hardware overhead compares the parity checksum against predefined threshold values for three iterations and terminates decoding if a condition is met. A 5.25 mm2 10GBASE-T Split-Row Threshold decoder is implemented using the proposed technique in 65 nm CMOS. The postlayout results show that at low SNR value of 3.0 dB, the decoder requires 2.3 times fewer decoding iterations which results in 23 pJ/bit energy dissipation. This is 2.4 times lower than the energy dissipation of Split-Row Threshold decoder without the proposed early stopping technique.

## Area, throughput, and energy-efficiency trade-offs in the VLSI implementation of LDPC decoders

- **ID**: ieee:5937927
- **Type**: conference
- **Published**: 15-18 May 
- **Authors**: C. Roth, A. Cevrero, C. Studer +2
- **PDF**: https://ieeexplore.ieee.org/document/5937927
- **Abstract**: Low-density parity-check (LDPC) codes are key ingredients for improving reliability of modern communication systems and storage devices. On the implementation side however, the design of energy-efficient and high-speed LDPC decoders with a sufficient degree of reconfigurability to meet the flexibility demands of recent standards remains challenging. This survey paper provides an overview of the state-of-the-art in the design of LDPC decoders using digital integrated circuits. To this end, we summarize available algorithms and characterize the design space. We analyze the different architectures and their connection to different codes and requirements. The advantages and disadvantages of the various choices are illustrated by comparing state-of-the-art LDPC decoder designs.

## LDPC decoder architecture for high-data rate personal-area networks

- **ID**: ieee:5937930
- **Type**: conference
- **Published**: 15-18 May 
- **Authors**: Matthew Weiner, Borivoje Nikolić, Zhengya Zhang
- **PDF**: https://ieeexplore.ieee.org/document/5937930
- **Abstract**: Emerging standards for wireless communications in the 60GHz band, such as WiGig, IEEE 802.11ad, and IEEE 802.15.3c, require throughputs between 1.5 and 6Gb/s and use rate adaptive low-density parity-check (LDPC) codes as the main form of forward error correction. State-of-the-art flexible LDPC decoders cannot simultaneously achieve the high throughput mandated by these standards and the low power needed for mobile applications. This work develops a flexible, fully pipelined architecture for the IEEE 802.11ad standard capable of achieving both goals. Based on a decoder synthesized in a low-power 65nm CMOS technology, the decoder dissipates 42mW at the 1.5Gb/s throughput and 84mW at the 3Gb/s throughput for the worst-case matrix in the standard.

## An approach based on edge coloring of tripartite graph for designing parallel LDPC interleaver architecture

- **ID**: ieee:5937914
- **Type**: conference
- **Published**: 15-18 May 
- **Authors**: Awais Sani, Philippe Coussy, Cyrille Chavet +1
- **PDF**: https://ieeexplore.ieee.org/document/5937914
- **Abstract**: A practical and feasible solution for LDPC decoder is to design partially-parallel hardware architecture. These architectures are efficient in terms of area, cost, flexibility and performances. However, this type of architecture is complex to design since concurrent read and write accesses to data have to be performed at each time instance without any conflict. To solve this memory mapping problem, we present in this paper, an original approach based on a tripartite graph modeling and a modified edge coloring algorithm to design parallel LDPC interleaver architecture.

## Regular and Irregular Quasi-Cyclic LDPC Codes

- **ID**: ieee:5956127
- **Type**: conference
- **Published**: 15-18 May 
- **Authors**: Xueqin Jiang, Moon Ho Lee, Jia Hou
- **PDF**: https://ieeexplore.ieee.org/document/5956127
- **Abstract**: This paper presents methods to the construction of regular and irregular low-density parity-check (LDPC) codes based on Euclidean geometries. Codes constructed by these methods are quasi-cyclic. The degree distributions of proposed LDPC codes can be optimized by the curve fitting approach in the extrinsic information transfer (EXIT) charts. Simulation results show that these codes perform very well with the iterative decoding.

## Low-complexity architectures for reliability-based message-passing non-binary LDPC decoding

- **ID**: ieee:5937810
- **Type**: conference
- **Published**: 15-18 May 
- **Authors**: Xinmiao Zhang, Fang Cai
- **PDF**: https://ieeexplore.ieee.org/document/5937810
- **Abstract**: When the code is not long, non-binary low-density parity- check (NB-LDPC) codes can achieve better error-correcting performance than binary LDPC codes at the cost of higher decoding complexity. The recently developed iterative reliability-based majority-logic NB- LDPC decoding can achieve better performance-complexity tradeoffs than previous algorithms. Many existing NB-LDPC code construction schemes lead to quasi-cyclic or cyclic codes. In this paper, efficient low- complexity NB-LDPC decoder architectures are developed for these two types of codes based on the newly proposed iterative hard reliability-based majority-logic decoding (IHRB-MLGD). Particularly, novel schemes are designed to keep a small proportion of messages in order to reduce the memory requirement without causing noticeable performance loss. Moreover, a shift-message structure is proposed by using memories concatenated with variable node units to enable efficient partial-parallel decoding for cyclic NB-LDPC codes. Compared to previous decoders based on the Min-max algorithm, the proposed IHRB-MLGD decoder architectures can achieve tens of times higher efficiency for codes with similar length and rate with moderate coding gain loss.

## Low Complexity Joint Channel Estimation and Decoding for LDPC Coded MIMO-OFDM Systems

- **ID**: ieee:5956229
- **Type**: conference
- **Published**: 15-18 May 
- **Authors**: Xiang Xu, Rudolf Mathar
- **PDF**: https://ieeexplore.ieee.org/document/5956229
- **Abstract**: In this paper, a joint iterative channel estimation and low-density parity-check (LDPC) decoding algorithm based on factor graphs and the sum-product algorithm is proposed for orthogonal frequency division multiplexing (OFDM) systems employing multiple transmit and receive antennas (MIMO). By modeling time-varying frequency-selective fading channels as autoregressive processes and approximating messages as Gaussian pdf, this receiver algorithm is able to maintain a low complexity. Moreover, with the help of strong channel coding and proper pilot allocation, the signal overhead can be significantly reduced.

## An adaptive analog low-density parity-check decoder based on margin propagation

- **ID**: ieee:5937813
- **Type**: conference
- **Published**: 15-18 May 
- **Authors**: Ming Gu, Shantanu Chakrabartty
- **PDF**: https://ieeexplore.ieee.org/document/5937813
- **Abstract**: One of the key factors underlying the popularity of low-density parity-check (LDPC) codes is its iterative decoding algorithm which is amenable to efficient analog and digital implementation. However, different applications of LDPC codes (e.g. wireless sensor networks) impose different sets of constraints which include speed, bit error rates (BER) and energy efficiency. Our previous work reported an algorithmic framework for designing margin propagation (MP) based LDPC decoders where the BER performance can be traded off with its energy efficiency. In this paper we present an analog current-mode implementation of an MP-based (32,8) LDPC decoder. The implementation uses only addition, subtraction and threshold operations and hence is independent of transistor biasing and robust to variations in environmental conditions (e.g. temperature). Measured results from prototypes fabricated in a 0.5 μm CMOS process verify the functionality of a (32,8) LDPC decoder and demonstrate superior BER performance compared to the state-of-the-art analog min- sum decoder at SNR greater than 3.5 dB.

## Multi-layer parallel decoding algorithm and vlsi architecture for quasi-cyclic LDPC codes

- **ID**: ieee:5937928
- **Type**: conference
- **Published**: 15-18 May 
- **Authors**: Yang Sun, Guohui Wang, Joseph R. Cavallaro
- **PDF**: https://ieeexplore.ieee.org/document/5937928
- **Abstract**: We propose a multi-layer parallel decoding algorithm and VLSI architecture for decoding of structured quasi-cyclic low-density parity-check codes. In the conventional layered decoding algorithm, the block-rows of the parity check matrix are processed sequentially, or layer after layer. The maximum number of rows that can be simultaneously processed by the conventional layered decoder is limited to the sub-matrix size. To remove this limitation and support layer-level parallelism, we extend the conventional layered decoding algorithm and architecture to enable simultaneously processing of multiple (K) layers of a parity check matrix, which will lead to a roughly K-fold throughput increase. As a case study, we have designed a double-layer parallel LDPC decoder for the IEEE 802.11n standard. The decoder was synthesized for a TSMC 45-nm CMOS technology. With a synthesis area of 0.81 mm2 and a maximum clock frequency of 815 MHz, the decoder achieves a maximum throughput of 3.0 Gbps at 15 iterations.

## Joint Non-Binary LDPC-BICM and Network Coding with Iterative Decoding for the Multiple Access Relay Channel

- **ID**: ieee:5956367
- **Type**: conference
- **Published**: 15-18 May 
- **Authors**: Mikel Hernaez, Pedro M. Crespo, Javier Del Ser
- **PDF**: https://ieeexplore.ieee.org/document/5956367
- **Abstract**: In this paper we present a novel joint network-channel coding scheme for the time-division Multiple Access Relay Channel (MARC), which combines Bit-Interleaved Coded Modulation with iterative decoding (BICM-ID) based on nonbinary Low-Density Parity Check (LDPC) codes, along with the linear combination of blocks of data at the relay. The common receiver iteratively exchanges soft information between a joint soft demapper and the LDPC decoder associated to the transmitting nodes. The performance of the proposed system is compared, in terms of Frame Error Rate (FER) and through intensive Monte Carlo simulations, with the corresponding theoretical outage rate for different values of the spectral efficiency of the overall setup. Two main conclusions are drawn: 1) small FER degradation is obtained as the spectral efficiency increases; and 2) no diversity is lost with respect to the theoretical outage rate.

## Sliding Window Method for stochastic LDPC decoder

- **ID**: ieee:5937811
- **Type**: conference
- **Published**: 15-18 May 
- **Authors**: Jienan Chen, Jianhao Hu
- **PDF**: https://ieeexplore.ieee.org/document/5937811
- **Abstract**: This paper proposes a Sliding Window Method (SWM) for stochastic Low Density Parity Check (LDPC) decoder designing. The SWM is formulated for solving the latch-up problem in the Variable Nodes (VN) information updating. The bit in the latch-up state is evolved from the information bit in the sliding window. Then, an optimized hardware structure is proposed for SWM. Compared with traditional VN structure, the SWM require about 35% less hardware resources to achieve the same BER performance.

## Performance Bound for LDPC Codes over Mobile LOS Wireless Optical Channel

- **ID**: ieee:5956176
- **Type**: conference
- **Published**: 15-18 May 
- **Authors**: N. Barbot, S. Sahuguede, A. Julien-Vergonjanne +1
- **PDF**: https://ieeexplore.ieee.org/document/5956176
- **Abstract**: In this paper we investigate performance of indoor Line of Sight (LOS) Wireless Optical Communication (WOC) considering non stationnarity due to emitter and/or receiver mobility. The transmission scheme uses Low Density Parity Check (LDPC) codes to mitigate performance degradation due to mobility. We evaluate a performance bound for LDPC codes in indoor environment and for a given mobility scenario. We show that this bound directly depends on the Signal to Noise Ratio (SNR) distribution and considering density evolution, on the LDPC code rate. Two methods are developed to evaluate SNR distribution. One is based on Monte Carlo simulations and the other one, on geometrical considerations linked to the room configuration. The obtained results for the performance bound are compared to finite length LDPC code performance.

## A high-throughput LDPC decoder architecture for high-rate WPAN systems

- **ID**: ieee:5937812
- **Type**: conference
- **Published**: 15-18 May 
- **Authors**: Kyung-Il Baek, Hanho Lee, Chang-Seok Choi +2
- **PDF**: https://ieeexplore.ieee.org/document/5937812
- **Abstract**: This paper presents a high-throughput memory- efficient decoder architecture for Quasi-Cyclic Low-Density Parity-Check (QC-LDPC) codes in the high-rate wireless personal area network applications. Two novel techniques which can apply to our selected QC-LDPC codes are proposed, including four-parallel block layered decoding architecture and simplification of the switch networks. The proposed architecture based on a block parallel decoding scheme replaces a crossbar- based interconnect network with a fixed wire network for a switch network. In addition, two-stage pipelining is used to improve the clock speed. A 672-bit, rate-1/2 LDPC decoder is implemented using 90 nm CMOS technology. The design achieves an information throughput of 1.45 Gbps at a clock speed of 285 MHz with a maximum of 16 iterations.

## QC-LDPC Decoding Architecture based on Stride Scheduling

- **ID**: ieee:5937814
- **Type**: conference
- **Published**: 15-18 May 
- **Authors**: Bongjin Kim, In-Cheol Park
- **PDF**: https://ieeexplore.ieee.org/document/5937814
- **Abstract**: In this paper, an area-efficient decoder architecture is proposed for the quasi-cyclic low-density parity check (QC-LDPC) codes specified in the WiMAX 802.16e standard. In order to achieve low area and maximize hardware utilization, the decoder utilizes 4 decoding function units, which is the greatest common divisor of the expansion factors. Furthermore, the decoder adopts a novel scheduling scheme, named as stride scheduling, to remove the conventional flexible permutation network and also minimize the number of memory accesses. The synthesized decoder costs 49K of logic gates and 54,144 bits of memory, while maintaining the throughput over the requirement of the WiMAX.

## Decoder Optimised Progressive Edge Growth Algorithm

- **ID**: ieee:5956769
- **Type**: conference
- **Published**: 15-18 May 
- **Authors**: C. T. Healy, R. C. de Lamare
- **PDF**: https://ieeexplore.ieee.org/document/5956769
- **Abstract**: A novel construction for irregular low density parity check (LDPC) codes based on a modification of the Progressive Edge Growth (PEG) algorithm is presented. The edge placement procedure of the PEG algorithm is enhanced by the use of the Sum-Product decoder in the design of the parity-check matrix. The proposed algorithm, like the PEG algorithm, is highly flexible in block length and rate. The codes constructed by the methods presented are tested in the AWGN channel and significant performance improvements are achieved. The flexibility of the proposed decoder optimisation operation in its application to PEG-based construction methods is then demonstrated by its use in modifying the Improved PEG (IPEG) extension to the PEG algorithm to achieve further performance gains.

## Analysis of Packet-Level Forward Error Correction for Video Transmission

- **ID**: ieee:5956635
- **Type**: conference
- **Published**: 15-18 May 
- **Authors**: Matteo Mazzotti, Enrico Paolini, Marco Chiani +3
- **PDF**: https://ieeexplore.ieee.org/document/5956635
- **Abstract**: In this paper, packet-level coding is considered in the framework of H.264/AVC video transmission. Two distinct solutions are proposed and compared in different realistic communication scenarios. The first is based on classical Reed-Solomon (RS) codes applied at the RTP layer, while the second on modern LDPC codes implemented at the UDP-Lite layer. An end-to-end Quality of Experience (QoE) evaluation is presented, in terms of achieved peak signal-to-noise power ratio (PSNR). Our numerical results show that, in low-latency video applications across communication channels introducing errors and erasures, the adoption of a packet-level coding scheme becomes essential to guarantee a satisfactory quality. The solution based on LDPC codes exhibits better performances in presence of severe packet loss rates.

## Car-to-Car Safety Broadcast with Interference Using Raptor Codes

- **ID**: ieee:5956272
- **Type**: conference
- **Published**: 15-18 May 
- **Authors**: Nor Fadzilah Abdullah, Angela Doufexi, Robert J. Piechocki
- **PDF**: https://ieeexplore.ieee.org/document/5956272
- **Abstract**: Car-to-car safety applications that demand real-time and reliable communications in vehicular ad hoc networks (VANETs) requires a new paradigm of coding techniques. In this paper, we propose a novel coding approach using a systematic Raptor code for car-to-car post-crash warning broadcast applications. A cross-layer simulator model is developed to evaluate the performance of Raptor codes against repetition codes using also multiple antennas spatial diversity techniques. The end-to-end delay and packet delivery ratio are used as performance metrics to demonstrate the latency and reliability problems of repetition codes that are addressed using Raptor codes.

## Performance of Hybrid-ARQ with Incremental Redundancy over Double Rayleigh Fading Channels

- **ID**: ieee:5956312
- **Type**: conference
- **Published**: 15-18 May 
- **Authors**: Ali Chelli, John R. Barry, Matthias Patzold
- **PDF**: https://ieeexplore.ieee.org/document/5956312
- **Abstract**: In this paper, we study the performance of hybrid automatic repeat request (HARQ) with incremental redundancy (IR) over double Rayleigh channels. Such channels can be used to model the fading amplitude for vehicle-to-vehicle (V2V) communications. We study the performance of HARQ from an information theoretic perspective. Analytical expressions are derived for the e-outage capacity, the average number of trans missions, and the average transmission rate for HARQ with IR, assuming a maximum number of rounds for the HARQ protocol. In our study, the communication rate per HARQ round is adjusted to the average signal-to-noise ratio (SNR) such that a target outage probability is not exceeded. This setting conforms with communication systems in which a quality of service is expected regardless of the channel conditions. It is well known that the ergodic capacity is achievable only if the power is adapted to the channel conditions, which requires channel state information (CSI) at the transmitter. We demonstrate that HARQ allows to communicate at a rate close to the ergodic capacity even in absence of CSI at the transmitter. Our analysis underscores the importance of HARQ in improving the spectral efficiency and reliability of communication systems.

## Decode-Quantize-Forward for OFDM-Based Relaying Systems

- **ID**: ieee:5956713
- **Type**: conference
- **Published**: 15-18 May 
- **Authors**: Dirk Wubben, Meng Wu
- **PDF**: https://ieeexplore.ieee.org/document/5956713
- **Abstract**: In this paper, we present a new relaying protocol for coded OFDM-based relaying systems. The classical Decode-Forward (DF) protocol exploits the coding gain within the relay, however the overall performance suffers from error propagation in case of decodings errors at the relay as no reliability information about the source-relay (SR) link can be exploited. This drawback is avoided by the proposed Decode-Quantize-Forward (DQF) scheme, where the code bits estimated by the decoder in the relay are directly forwarded to the destination. Based on the observation, that code bit errors at the relay occur likely on subcarriers with low signal to noise ratio (SNR) on the SR link, we propose a modified maximum ratio combining (cMRC) scheme for the destination. As this approach exploits the varying channel reliability per subcarrier it outperforms the well-known DF protocol significantly.

## Reliable Broadcast Transmission in Vehicular Networks Based on Fountain Codes

- **ID**: ieee:5956793
- **Type**: conference
- **Published**: 15-18 May 
- **Authors**: Robert Budde, Stefan Nowak, Ruediger Kays
- **PDF**: https://ieeexplore.ieee.org/document/5956793
- **Abstract**: Car-to-car and car-to-infrastructure communications are currently under intense research as they enable a wide variety of applications. Besides security-driven applications which require only small amounts of individual data there are also applications which require medium to high amounts of uniform data delivered to an unknown number of nodes. For this kind of broadcast and multicast applications, the use of fountain codes is highly suitable. In this paper, we investigate the applicability of fountain codes in an infrastructure-based automotive communication system and introduce an expedient method to design a system deploying IEEE 802.11p and fountain codes. By means of simulation results obtained for three representative vehicular scenarios we compare the performance of our method to an alternative method also applied in this field, i.e. the data carousel. For specific configurations the system based on fountain codes outperforms the conservative approach by a factor of four in terms of the overall throughput and thus provides the potential to significantly increase the overall efficiency.

## Performance of Type-I and Type-II Hybrid ARQ in Decode and Forward Relaying

- **ID**: ieee:5956530
- **Type**: conference
- **Published**: 15-18 May 
- **Authors**: Hirley Alves, Richard Demo Souza, Glauber Brante +1
- **PDF**: https://ieeexplore.ieee.org/document/5956530
- **Abstract**: Truncated Type-I and Type-II HARQ schemes are compared, in terms of throughput, when incremental decode and forward relaying is used. The comparison is based on the outage analysis of both schemes. Two different scenarios are considered: ad-hoc relaying, where all users are at ground level, and infra-structured relaying, where the relay and the destination antennas are at a higher height than the user. Moreover, we also consider the effect of rate adaptation. Results show that Type-II (incremental redundancy) only significantly outperforms Type-I schemes (selection and Chase combining) in the case of ad-hoc relaying without rate adaptation, and in the low SNR region.

## Hardware implementation challenges of modern error control decoders

- **ID**: ieee:5937931
- **Type**: conference
- **Published**: 15-18 May 
- **Authors**: Christian Schlegel, Vincent Gaudet
- **PDF**: https://ieeexplore.ieee.org/document/5937931
- **Abstract**: The basic design challenges for large-scale modern error control decoders based on message passing are examined in this review and exploratory paper. Space, complexity, and power consumption figures are of most interest to the design engineer, and the state-of-the art of current implementations are presented. Fundamental limits of performance versus power and complexity are discussed, and innovative state-of-the art approaches to address these challenges are highlighted.

## Adaptive Partial Decode-and-Forward Relaying with Quantized Feedback

- **ID**: ieee:5956306
- **Type**: conference
- **Published**: 15-18 May 
- **Authors**: Chen Luo, Yi Wu, Zesong Fei +2
- **PDF**: https://ieeexplore.ieee.org/document/5956306
- **Abstract**: In this paper, we propose two spectrally efficient adaptive partial decode-and-forward (DF) cooperative communication schemes with quantized feedback: adaptive partial repetition DF scheme and adaptive partial coded cooperation DF scheme. We assume that the relay node only has partial channel-state information, which is obtained via an quantized feedback link. We use the so-called mutual information (MI) model to adaptively optimize the amount of message transmitted by the relay node under a given block-error-rate constraint. We develop adaptive algorithms and implementation details for both schemes. Simulation results show that with the quantized feedback, the MI model can predict well the amount of message that needs to be transmitted by the relay node, and that the two proposed schemes can substantially increase the spectral efficiency of the system.

## Computationally-efficient iterative decoding for storage system design: Min-Sum refined

- **ID**: ieee:5937960
- **Type**: conference
- **Published**: 15-18 May 
- **Authors**: Ben-Yue Chang, Milos Ivkovic, Lara Dolecek
- **PDF**: https://ieeexplore.ieee.org/document/5937960
- **Abstract**: In this paper we propose a computationally-efficient, iterative decoding algorithm that is well-suited for storage systems with very stringent reliability constraints and low redundancy/high code rate requirements. The proposed Dual-Scaling Min-Sum (DS-MSA) overcomes certain deficiencies of the Min-Sum approximation when used for decoding graph-based codes. We observe that a small but non-negligible fraction of check-to-variable messages is underestimated by the Normalized Min-Sum algorithm in the low error rate region. By carefully adjusting the scaling factor for the variable-to-check message with the smallest magnitude, we develop the DS-MSA algorithm characterized by two scaling parameters. The proposed algorithm (1) outperforms Sum-Product and (Normalized) Min-Sum algorithms in the very low error rate regime, (2) maintains the low-complexity feature of the Min-Sum, and (3) can be easily combined with existing decoder implementations.

## A New High-Performance and Low-Complexity Turbo-LDPC Code

- **ID**: ieee:5957374
- **Type**: conference
- **Published**: 14-15 May 
- **Authors**: Jui-Hui Hung, Jin-Shun Shyu, Sau-Gee Chen
- **PDF**: https://ieeexplore.ieee.org/document/5957374
- **Abstract**: In this paper, a new coding scheme, named Turbo-LDPC code, is proposed. It applies LDPC codes to the product coding scheme, and performs the decoding operation iteratively between the two component codes. Besides, to boost the decoding performance, a linear extrinsic information normalization (EIN) method is also devised, which greatlyreduces the problem of belief propagation distortion ofextrinsic information after message interleaving. Altogether,the decoding performances of Turbo-LDPC codes are muchhigher than those of the original LDPC codes undercomparable computational complexities. Compared to blockturbo code combined with BCH codes, the proposed Turbo-LDPC code also has much better decoding performance as wellas lower computational complexity.

## A 16Gbps Real-Time BF-based LDPC Decoder for IEEE 802.3an Standard

- **ID**: ieee:5957373
- **Type**: conference
- **Published**: 14-15 May 
- **Authors**: Jui-Hui Hung, Sau-Gee Chen
- **PDF**: https://ieeexplore.ieee.org/document/5957373
- **Abstract**: Existing LDPC decoders are mostly based on belief-propagation (BP) algorithms for high decoding performance but demand high hardware cost, especially for applications with very high throughputs. In order to alleviate the problem, this work proposes a high-throughput LDPC decoder based on the much simpler bit-flipping (BF) algorithms, for the (2048, 1723) RS-LDPC code adopted in the IEEE 802.3an standard. High decoding performances and low iteration numbers are achieved by introducing a strategy of flipping low-correlation bits and an additional syndrome vote scheme. As a result, the decoding performance is comparable to the most popular BP-based min-sum algorithm (MSA) but with much lower computational complexity. Besides, the decoder achieves high hardware utilization with real-time processing capability. Synthesized with UMC 90nm process, the decoder chip area, throughput and average power dissipation are 1.22M gates, 16Gbps and 315mW,respectively, at 500MHz clock rate.

## LDPC-coded OAM modulation and multiplexing for deep-space and near-Earth optical communications

- **ID**: ieee:5783692
- **Type**: conference
- **Published**: 11-13 May 
- **Authors**: Ivan B. Djordjevic
- **PDF**: https://ieeexplore.ieee.org/document/5783692
- **Abstract**: In order to achieve multi-gigabit transmission (projected for 2020) for the use in interplanetary communications, the usage of large number of time slots in pulse-position modulation (PPM), typically used in deep-space applications, is needed, which imposes stringent requirements on system design and implementation. As an alternative satisfying high-bandwidth demands of future interplanetary communications, while keeping the system cost and power consumption reasonably low, in this invited paper, we describe the use of orbital angular momentum (OAM) as an additional degree of freedom. The OAM is associated with azimuthal phase of the complex electric field. Because OAM eigenstates are orthogonal the can be used as basis functions for multidimensional signaling. The OAM modulation and multiplexing can, therefore, be used, in combination with other degrees of freedom, to solve the high-bandwidth requirements of future deep-space and near-Earth optical communications. The main challenge for OAM deep-space communication represents the link between a spacecraft probe and the Earth station because in the presence of atmospheric turbulence the orthogonality between OAM states is not longer preserved. We will show that in combination with LDPC codes, the OAM-based modulation schemes can operate even under strong atmospheric turbulence regime.

## On approaching the ultimate limits of photon-efficient and bandwidth-efficient optical communication

- **ID**: ieee:5783682
- **Type**: conference
- **Published**: 11-13 May 
- **Authors**: Sam Dolinar, Kevin M. Birnbaum, Baris I. Erkmen +1
- **PDF**: https://ieeexplore.ieee.org/document/5783682
- **Abstract**: It is well known that ideal free-space optical communication at the quantum limit can have unbounded photon information efficiency (PIE), measured in bits per photon. High PIE comes at a price of low dimensional information efficiency (DIE), measured in bits per spatio-temporal-polarization mode. If only temporal modes are used, then DIE translates directly to bandwidth efficiency. In this paper, the DIE vs. PIE tradeoffs for known modulations and receiver structures are compared to the ultimate quantum limit, and analytic approximations are found in the limit of high PIE. This analysis shows that known structures fall short of the maximum attainable DIE by a factor that increases linearly with PIE for high PIE. The capacity of the Dolinar receiver is derived for binary coherent-state modulations and computed for the case of on off keying (OOK). The DIE vs. PIE tradeoff for this case is improved only slightly compared to OOK with photon counting. An adaptive rule is derived for an additive local oscillator that maximizes the mutual information between a receiver and a transmitter that selects from a set of coherent states. For binary phase-shift keying (BPSK), this is shown to be equivalent to the operation of the Dolinar receiver. The Dolinar receiver is extended to make adaptive measurements on a coded sequence of coherent state symbols. Information from previous measurements is used to adjust the a priori probabilities of the next symbols. The adaptive Dolinar receiver does not improve the DIE vs. PIE tradeoff compared to independent transmission and Dolinar reception of each symbol.

## Adaptive channel coding for maritime FSO channels with RF feedback link

- **ID**: ieee:5783696
- **Type**: conference
- **Published**: 11-13 May 
- **Authors**: Mark Gregory, Peter Adam Hoeher
- **PDF**: https://ieeexplore.ieee.org/document/5783696
- **Abstract**: Free-space optical data links (FSO) can provide high bandwidth and secure data transmission. Since channel impacts like fog or atmospheric turbulence are decreasing the network availability, a microwave (RF) backup link is desirable. In this paper, the maritime environment is considered. The impact of channel coding is studied for multi-aperture (MIMO) FSO links with different scintillation index. In addition, an adaptive coding scheme is proposed, maximizing the availability of the combined hybrid (RF/FSO) network regarding the full range of possible signal distortions.

## Analysis of advanced FEC versus traditional FEC in GNSS data structures

- **ID**: ieee:5935361
- **Type**: conference
- **Published**: 10-12 May 
- **Authors**: Aditya Kakkar, Ashish Agrawal, Mohit Kumar +1
- **PDF**: https://ieeexplore.ieee.org/document/5935361
- **Abstract**: Global Navigation Satellite Systems (GNSS), presently a USD 20 billion industry, has steadily growing applications in all possible spheres with some new high precision applications like indoor navigation etc. are at the cutting edge of the technology, thus requiring sophisticated FECs. In lieu of these facts and more, in this paper we undertake thorough analysis and comparison of Advanced FEC (such as LDPC Convolutional Code) versus Traditional FEC for finite length GNSS data frames on parameters such as computational complexity, processor complexity, delay, memory requirement and BER performance (depending on block length, memory) etc. Based on the above analysis, finally we shall be proposing the best fit FEC for present and future generation GNSS.

## Low complexity soft decision circuit for LDPC decoders

- **ID**: ieee:5951155
- **Type**: conference
- **Published**: 1-6 May 20
- **Authors**: M. N. Sakib, V. Mahalingam, A. J. Wong +2
- **PDF**: https://ieeexplore.ieee.org/document/5951155
- **Abstract**: A reduced complexity implementation is proposed of an optical receiver for the soft decoding of low density parity check codes. Coding gain of 9.4 dB is achieved using 20% of the incoming optical signal.

## Designing a fast and adaptive error correction scheme for increasing the lifetime of phase change memories

- **ID**: ieee:5783773
- **Type**: conference
- **Published**: 1-5 May 20
- **Authors**: Rudrajit Datta, Nur A. Touba
- **PDF**: https://ieeexplore.ieee.org/document/5783773
- **Abstract**: This paper proposes an adaptive multi-bit error correcting code for phase change memories that provides a manifold increase in the lifetime of phase change memories thereby making them a more viable alternative for DRAM main memory. A novel aspect of the proposed approach is that the error correction code (ECC) is adapted over time as the number of failed cells in the phase change memory accumulates. The operating system (OS) monitors the number of errors corrected on a memory line, and when the number of errors on a line begins to exceed the strength of the ECC present, the ECC strength is adaptively increased. As this happens, the performance of the memory system gracefully degrades because more storage is taken up by check bits rather than data bits thereby reducing the effective size of a cache line since less data can be brought to the cache on each read operation to the PCM main memory. Experimental results show that the lifetime of a phase change memory can be significantly extended while keeping the fraction of data to check bits as high as possible at each stage in the lifetime of the phase change memory.

## Using Functional Programming to Generate an LDPC Forward Error Corrector

- **ID**: ieee:5771264
- **Type**: conference
- **Published**: 1-3 May 20
- **Authors**: Andy Gill, Tristan Bull, Dan DePardo +3
- **PDF**: https://ieeexplore.ieee.org/document/5771264
- **Abstract**: FPGAs as commodities offer a resource for high-performance computation that is unmatched in flexibility and price/performance. As a lab, we are interested in high-level descriptions of computation and data, and how they may be customized to map effectively on FPGA fabrics. This paper describes our tool-chain, approach and methodology to FPGA utilization. We give a case study of the generation of a low density parity checking forward error correction algorithm, and discuss the specific challenges we faced with using FPGAs as our target.
