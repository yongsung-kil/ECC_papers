# IEEE Xplore — 2014-03


## Implementation of Decoders for LDPC Block Codes and LDPC Convolutional Codes Based on GPUs

- **ID**: ieee:6470607
- **Type**: journal
- **Published**: March 2014
- **Authors**: Yue Zhao, Francis C.M. Lau
- **PDF**: https://ieeexplore.ieee.org/document/6470607
- **Abstract**: In this paper, efficient LDPC block-code decoders/simulators which run on graphics processing units (GPUs) are proposed. We also implement the decoder for the LDPC convolutional code (LDPCCC). The LDPCCC is derived from a predesigned quasi-cyclic LDPC block code with good error performance. Compared to the decoder based on the randomly constructed LDPCCC code, the complexity of the proposed LDPCCC decoder is reduced due to the periodicity of the derived LDPCCC and the properties of the quasi-cyclic structure. In our proposed decoder architecture, $(\Gamma)$ ($(\Gamma)$ is a multiple of a warp) codewords are decoded together, and hence, the messages of $(\Gamma)$ codewords are also processed together. Since all the $(\Gamma)$ codewords share the same Tanner graph, messages of the $(\Gamma)$ distinct codewords corresponding to the same edge can be grouped into one package and stored linearly. By optimizing the data structures of the messages used in the decoding process, both the read and write processes can be performed in a highly parallel manner by the GPUs. In addition, a thread hierarchy minimizing the divergence of the threads is deployed, and it can maximize the efficiency of the parallel execution. With the use of a large number of cores in the GPU to perform the simple computations simultaneously, our GPU-based LDPC decoder can obtain hundreds of times speedup compared with a serial CPU-based simulator and over 40 times speedup compared with an eight-thread CPU-based simulator.

## Decoding Algorithms of LDPC Coded Superposition Modulation

- **ID**: ieee:6784553
- **Type**: journal
- **Published**: March 2014
- **Authors**: Shancheng Zhao, Xiao Ma, Baoming Bai
- **PDF**: https://ieeexplore.ieee.org/document/6784553
- **Abstract**: This paper is concerned with the design of decoding algorithms for superposition modulation systems in which all levels are coded with an identical binary low-density parity-check (LDPC) code. First, we present a computing-based iterative multistage decoding algorithm (CB-IMSDA). Then, we show that the considered system can be treated as a nonbinary LDPC (NB-LDPC) coded modulation system. Based on this, a joint decoding algorithm (JDA) is proposed. As a by-product, we propose a time-varying signaling scheme for the JDA. Numerical results show that 1) both the CB-IMSDA and JDA perform better than the standard iterative multistage decoding algorithm, and 2) extra coding gain can be obtained when the time-varying signaling scheme is employed.

## Low-Power High-Throughput LDPC Decoder Using Non-Refresh Embedded DRAM

- **ID**: ieee:6736117
- **Type**: journal
- **Published**: March 2014
- **Authors**: Youn Sung Park, David Blaauw, Dennis Sylvester +1
- **PDF**: https://ieeexplore.ieee.org/document/6736117
- **Abstract**: The majority of the power consumption of a high-throughput LDPC decoder is spent on memory. Unlike in a general-purpose processor, the memory access in an LDPC decoder is deterministic and the access window is short. We take advantage of the unique memory access characteristic to design a non-refresh eDRAM that holds data for the necessary access window, and further improve its access time by trading off the excess retention time. The resulting 3T eDRAM cell is designed to balance wordline coupling to reliably retain data for a fast access. We integrate 32 5x210 non-refresh eDRAM arrays in a row-parallel LDPC decoder suitable for the IEEE 802.11ad standard. Memory refresh is eliminated and random access is replaced with a simple sequential addressing. With row merging and dual-frame processing, the 1.6 mm 2 65 nm LDPC decoder chip achieves a peak throughput of 9 Gb/s at 89.5 pJ/b, of which only 21% is spent on eDRAMs. With voltage and frequency scaling, the power consumption of the LDPC decoder is reduced to 37.7 mW for a 1.5 Gb/s throughput at 35.6 pJ/b.

## LDPC-RS Product Codes for Digital Terrestrial Broadcasting Transmission System

- **ID**: ieee:6678727
- **Type**: journal
- **Published**: March 2014
- **Authors**: Bo Liu, Yaqi Li, Bo Rong +2
- **PDF**: https://ieeexplore.ieee.org/document/6678727
- **Abstract**: Product code is a promising technique for the next generation digital terrestrial broadcasting transmission system, due to its superior error correction performance. In this paper, we propose an Low Density Parity Check-Reed Solomon (LDPC-RS) product code structure, along with a novel hybrid iterative decoding scheme. The decoding scheme combines a hybrid LDPC decoding technique and ${\rm RS}+{\rm LDPC}$ hard decision decoding to form a ‘turbo-like’ decoding structure. By ingeniously ranging the order of different decoding techniques as well as performing error estimation and soft value modification at proper stages, the proposed decoding scheme greatly improves the error performance in low SNR regions while reducing the computational complexity in moderate and high SNR regions compared with the simple concatenation of LDPC and RS decoding. Moreover, we propose a rate compatible LDPC-RS product code to further reduce complexity by adaptively choosing the decoding code rate. Simulation results verify the outstanding error performance and suitability for the energy saving applications.

## Design of Low-Density Parity-Check Codes for Half-Duplex Three-Phase Two-Way Relay Channels

- **ID**: ieee:6733262
- **Type**: journal
- **Published**: March 2014
- **Authors**: Xinsheng Zhou, Liang-Liang Xie, Xuemin Sherman Shen
- **PDF**: https://ieeexplore.ieee.org/document/6733262
- **Abstract**: In two-way relay channels, two terminal nodes exchange information with the help of a relay node. Designing practical coding schemes for such channels is challenging, especially when messages are encoded into multiple streams and a destination node receives signals from multiple nodes. In this paper, we prove an achievable region for half-duplex three-phase two-way relay channels. Furthermore, we propose low-density parity-check (LDPC) codes for such channels where two source codewords are encoded by systematic LDPC codes at the relay node. To analyze the performance of the codes, discretized density evolution is derived for the joint decoder at terminal nodes. Based on the discretized density evolution, degree distributions are optimized by iterative linear programming in 3 steps. The length of the obtained optimized codes is 26% longer than the theoretic one.

## A Design of Physical-Layer Raptor Codes for Wide SNR Ranges

- **ID**: ieee:6784554
- **Type**: journal
- **Published**: March 2014
- **Authors**: Shiuan-Hao Kuo, Yong Liang Guan, Shih-Kai Lee +1
- **PDF**: https://ieeexplore.ieee.org/document/6784554
- **Abstract**: It is known that the Raptor code can be constructed to achieve a rate close to the capacity of the binary-input AWGN (BIAWGN) channel with a fixed signal-to-noise ratio (SNR). In this letter, we propose a constructive approach of designing the Raptor code over the BIAWGN channel such that the achieved rates are close to the associated capacities for wide SNR ranges.

## Finite Field Spreading for Multiple-Access Channel

- **ID**: ieee:6725575
- **Type**: journal
- **Published**: March 2014
- **Authors**: Guanghui Song, Yuta Tsujii, Jun Cheng +1
- **PDF**: https://ieeexplore.ieee.org/document/6725575
- **Abstract**: As a generalization of the binary spreading scheme in conventional direct-sequence code-division multiple-access (DS-CDMA) and interleave-division multiple-access (IDMA), a finite field spreading scheme is proposed for a synchronous multiple-access channel (MAC) with Gaussian noise and equal-power users. For each user, each information symbol over a finite field is spread into a length-L field vector by L-field multiplications. At the receiver, an iterative multi-user decoding algorithm on a factor graph is developed to recover each user's information symbol. To estimate the bit error rate performance of an uncoded finite field spreading system, an extrinsic information transfer analysis of the finite field despreading is given. This analysis shows that in addition to overcoming multi-user interference, the finite field spreading scheme can also provide an additional coding gain to overcome Gaussian noise compared with the conventional spreading scheme. This coding gain increases with the field order. The finite field spreading serially concatenated with a nonbinary low-density parity-check (LDPC) code, with field order 64, approaches the MAC capacity within 0.26 dB at a sum rate of 0.25.

## Impulse Noise Estimation and Removal for OFDM Systems

- **ID**: ieee:6742716
- **Type**: journal
- **Published**: March 2014
- **Authors**: Tareq Y. Al-Naffouri, Ahmed A. Quadeer, Giuseppe Caire
- **PDF**: https://ieeexplore.ieee.org/document/6742716
- **Abstract**: Orthogonal Frequency Division Multiplexing (OFDM) is a modulation scheme that is widely used in wired and wireless communication systems. While OFDM is ideally suited to deal with frequency selective channels and AWGN, its performance may be dramatically impacted by the presence of impulse noise. In fact, very strong noise impulses in the time domain might result in the erasure of whole OFDM blocks of symbols at the receiver. Impulse noise can be mitigated by considering it as a sparse signal in time, and using recently developed algorithms for sparse signal reconstruction. We propose an algorithm that utilizes the guard band null subcarriers for the impulse noise estimation and cancellation. Instead of relying on \ell_1 minimization as done in some popular general-purpose compressive sensing schemes, the proposed method jointly exploits the specific structure of this problem and the available a priori information for sparse signal recovery. The computational complexity of the proposed algorithm is very competitive with respect to sparse signal reconstruction schemes based on \ell_1 minimization. The proposed method is compared with respect to other state-of-the-art methods in terms of achievable rates for an OFDM system with impulse noise and AWGN.

## Message Passing Optimization of Harmonic Influence Centrality

- **ID**: ieee:6732931
- **Type**: journal
- **Published**: March 2014
- **Authors**: Luca Vassio, Fabio Fagnani, Paolo Frasca +1
- **PDF**: https://ieeexplore.ieee.org/document/6732931
- **Abstract**: This paper proposes a new measure of node centrality in social networks, the Harmonic Influence Centrality (HIC), which emerges naturally in the study of social influence over networks. Using an intuitive analogy between social and electrical networks, we introduce a distributed message passing algorithm to compute the HIC of each node. Although its design is based on theoretical results which assume the network to have no cycle, the algorithm can also be successfully applied on general graphs.

## TTCM-Aided Rate-Adaptive Distributed Source Coding for Rayleigh Fading Channels

- **ID**: ieee:6697844
- **Type**: journal
- **Published**: March 2014
- **Authors**: Abdulah Jeza Aljohani, Soon Xin Ng, Lajos Hanzo
- **PDF**: https://ieeexplore.ieee.org/document/6697844
- **Abstract**: Adaptive turbo-trellis-coded modulation (TTCM)-aided asymmetric distributed source coding (DSC) is proposed, where two correlated sources are transmitted to a destination node. The first source sequence is TTCM encoded and is further compressed before it is transmitted through a Rayleigh fading channel, whereas the second source signal is assumed to be perfectly decoded and, hence, to be flawlessly shown at the destination for exploitation as side information for improving the decoding performance of the first source. The proposed scheme is capable of reliable communications within 0.80 dB of the Slepian-Wolf/Shannon (SW/S) theoretical limit at a bit error rate (BER) of 10-5. Furthermore, its encoder is capable of accommodating time-variant short-term correlation between the two sources.

## Simplified Log-MAP Algorithm for Very Low-Complexity Turbo Decoder Hardware Architectures

- **ID**: ieee:6607183
- **Type**: journal
- **Published**: March 2014
- **Authors**: Maurizio Martina, Stylianos Papaharalabos, P. Takis Mathiopoulos +1
- **PDF**: https://ieeexplore.ieee.org/document/6607183
- **Abstract**: Motivated by the importance of hardware implementation in practical turbo decoders, a simplified, yet effective, $n$-input $\max^{\ast}$  approximation algorithm is proposed with the aim being its efficient implementation for very low-complexity turbo decoder hardware architectures. The simplification is obtained using an appropriate digital circuit for finding the first two maximum values in a set of $n$ data that embeds the computation of a correction term. Various implementation results show that the proposed architecture is simpler by 30%, on average, than the constant logarithmic-maximum a posteriori (Log-MAP) one, in terms of chip area with the same delay. This comes at the expense of very small performance degradation, in the order of 0.1 dB for up to moderate bit error rates, e.g., $10^{-5}$, assuming binary turbo codes. However, when applying scaling to the extrinsic information, the proposed algorithm achieves almost identical Log-MAP turbo code performance for both binary and double-binary turbo codes, without increasing noticeably the implementation complexity.

## Robustness of Physical Layer Security Primitives Against Attacks on Pseudorandom Generators

- **ID**: ieee:6730892
- **Type**: journal
- **Published**: March 2014
- **Authors**: Rajaraman Vaidyanathaswami, Andrew Thangaraj
- **PDF**: https://ieeexplore.ieee.org/document/6730892
- **Abstract**: Physical layer security protocols exploit inviolable physical laws at the signal level for providing guarantees on secrecy of communications. These protocols invariably involve randomized encoding at the transmitter, for which an ideal random number generator is typically assumed in the literature. In this work, we study the impact of using weak Pseudo Random Number Generators (PRNGs) in physical layer security protocols for coding and forward key distribution over Binary Symmetric and Gaussian wiretap channels. In the case of wiretap channel coding, we study fast correlation attacks that aim to retrieve the initial seed used in the PRNGs. Our results show that randomized coset encoding, which forms an important part of wiretap channel coding, provides useful robustness against fast correlation attacks. In the case of single-round or forward key distribution over a Gaussian wiretap channel, the bits from a PRNG are nonlinearly transformed to generate Gaussian-distributed pseudo random numbers at the transmitter. In such cases, we design modified versions of the fast correlation attacks accounting for the effects of the nonlinear transformation and soft input. We observe that, even for moderately high memory, the success probability of the modified fast correlation attacks become the same as that of a random guess in many cases.

## Nonbinary Associative Memory With Exponential Pattern Retrieval Capacity and Iterative Learning

- **ID**: ieee:6634278
- **Type**: journal
- **Published**: March 2014
- **Authors**: Amir Hesam Salavati, K. Raj Kumar, Amin Shokrollahi
- **PDF**: https://ieeexplore.ieee.org/document/6634278
- **Abstract**: We consider the problem of neural association for a network of nonbinary neurons. Here, the task is to first memorize a set of patterns using a network of neurons whose states assume values from a finite number of integer levels. Later, the same network should be able to recall the previously memorized patterns from their noisy versions. Prior work in this area consider storing a finite number of purely random patterns, and have shown that the pattern retrieval capacities (maximum number of patterns that can be memorized) scale only linearly with the number of neurons in the network. In our formulation of the problem, we concentrate on exploiting redundancy and internal structure of the patterns to improve the pattern retrieval capacity. Our first result shows that if the given patterns have a suitable linear-algebraic structure, i.e., comprise a subspace of the set of all possible patterns, then the pattern retrieval capacity is exponential in terms of the number of neurons. The second result extends the previous finding to cases where the patterns have weak minor components, i.e., the smallest eigenvalues of the correlation matrix tend toward zero. We will use these minor components (or the basis vectors of the pattern null space) to increase both the pattern retrieval capacity and error correction capabilities. An iterative algorithm is proposed for the learning phase, and two simple algorithms are presented for the recall phase. Using analytical methods and simulations, we show that the proposed methods can tolerate a fair amount of errors in the input while being able to memorize an exponentially large number of patterns.

## Pilot-aided log-likelihood ratio for LDPC coded M-QAM CO-OFDM system

- **ID**: ieee:6887151
- **Type**: conference
- **Published**: 9-13 March
- **Authors**: Shengjiao Cao, Pooi-Yuen Kam, Changyuan Yu
- **PDF**: https://ieeexplore.ieee.org/document/6887151
- **Abstract**: Pilot-aided log-likelihood ratio as well as its approximation are derived for LDPC coded M-QAM CO-OFDM system with consideration of laser phase noise. Our metric performs better than the conventional metric in 16QAM and 64QAM simulation.

## Staircase rate-adaptive LDPC-coded modulation for high-speed intelligent optical transmission

- **ID**: ieee:6886576
- **Type**: conference
- **Published**: 9-13 March
- **Authors**: Yequn Zhang, Ivan B. Djordjevic
- **PDF**: https://ieeexplore.ieee.org/document/6886576
- **Abstract**: We propose staircase rate-adaptive LDPC-coded modulation that is suitable for high-speed intelligent optical transmission. Compared with shortening of LDPC codes, larger coding gain can be obtained and error floor can also be effectively mitigated.

## Cycle slip-mitigating turbo demodulation in LDPC-coded coherent optical communications

- **ID**: ieee:6886573
- **Type**: conference
- **Published**: 9-13 March
- **Authors**: Toshiaki Koike-Akino, Keisuke Kojima, David S. Millar +5
- **PDF**: https://ieeexplore.ieee.org/document/6886573
- **Abstract**: We show that an iterative demodulation with soft-decision feedback information from FEC decoder can efficiently mitigate cycle slips. With 3% pilot insertion, the turbo QPSK demodulation achieves 1.05dB gain even in the presence of frequent cycle slips.

## Implementation of 64QAM at 42.66 GBaud using 1.5 samples per symbol DAC and demonstration of up to 300 km fiber transmission

- **ID**: ieee:6886511
- **Type**: conference
- **Published**: 9-13 March
- **Authors**: Fred Buchali, Axel Klekamp, Laurent Schmalen +1
- **PDF**: https://ieeexplore.ieee.org/document/6886511
- **Abstract**: We demonstrate 400Gbit/s data generation using 64QAM at 42.66 GBaud with a reduced oversampling ratio of 1.5 Sample/symbol including digital Nyquist filtering and spectral pre-emphasis. Even at 24% FEC overhead a successful transmission over 300 km ULAF has been shown.

## Experimental demonstration of 24-dimensional extended Golay coded modulation with LDPC

- **ID**: ieee:6886575
- **Type**: conference
- **Published**: 9-13 March
- **Authors**: David S. Millar, Toshiaki Koike-Akino, Robert Maher +7
- **PDF**: https://ieeexplore.ieee.org/document/6886575
- **Abstract**: We experimentally demonstrate ultra-long haul transmission of 24-D extended Golay coded modulation with LDPC. Compared with LDPC coded DP-BPSK, an increase of 15% in reach was shown, with a 3 dB increase in launch power margin at a transmission distance of more than 16,000 km.

## Achievable rates for four-dimensional coded modulation with a bit-wise receiver

- **ID**: ieee:6886524
- **Type**: conference
- **Published**: 9-13 March
- **Authors**: Alex Alvarado, Erik Agrell
- **PDF**: https://ieeexplore.ieee.org/document/6886524
- **Abstract**: We study achievable rates for four-dimensional (4D) constellations for spectrally efficient optical systems based on a (suboptimal) bit-wise receiver. We show that PM-QPSK outperforms the best 4D constellation designed for uncoded transmission by approximately 1 dB. Numerical results using LDPC codes validate the analysis.

## 5 × 50 Gb/s WDM transmission of 32 Gbaud DP-3-PSK over 36,000 km fiber with spatially coupled LDPC coding

- **ID**: ieee:6886980
- **Type**: conference
- **Published**: 9-13 March
- **Authors**: Fred Buchali, Laurent Schmalen, Axel Klekamp +2
- **PDF**: https://ieeexplore.ieee.org/document/6886980
- **Abstract**: A novel 3-PSK modulation format with 2 dB SNR gain over BPSK is implemented for ultra long haul transmission. With spatially coupled LDPC coding, 50% reach extension is achieved leading to 36.000 km transmission distance.

## A simple and high-performance method for combining soft-decision FEC with differential encoding in 100 Gbps dual-polarization QPSK system

- **ID**: ieee:6886577
- **Type**: conference
- **Published**: 9-13 March
- **Authors**: Julie Karaki, Raphaël Le Bidan, Erwan Pincemin
- **PDF**: https://ieeexplore.ieee.org/document/6886577
- **Abstract**: By a joint design of FEC and modulation, we demonstrate that it is possible to associate strong SD-FEC and differentially-encoded QPSK systems with negligible coding gain penalty and minor modifications in existing transceivers. The resulting system is robust to cycle slips.

## Benefits of active stateful PCE for flexgrid networks

- **ID**: ieee:6886801
- **Type**: conference
- **Published**: 9-13 March
- **Authors**: F. Cugini, F. Paolucci, F. Fresi +7
- **PDF**: https://ieeexplore.ieee.org/document/6886801
- **Abstract**: Relevant benefits of the active stateful PCE architecture are experimentally demonstrated on a flexgrid network testbed. Two experiments are reported, including a first demo on PCE-controlled code-adaptation applied to a 1Tb/s super-channel.

## Energy efficient FEC for optical transmission systems

- **ID**: ieee:6886571
- **Type**: conference
- **Published**: 9-13 March
- **Authors**: Laurent Schmalen
- **PDF**: https://ieeexplore.ieee.org/document/6886571
- **Abstract**: We give an overview about different options for energy efficient FEC realizations in future optical communication systems. We especially highlight different options for realizing energy efficient decoders for higher order modulation formats.

## Transoceanic transmission of dual-carrier 400G DP-8QAM at 121.2km span length with EDFA-only

- **ID**: ieee:6886982
- **Type**: conference
- **Published**: 9-13 March
- **Authors**: Shaoliang Zhang, Fatih Yaman, Ting Wang +4
- **PDF**: https://ieeexplore.ieee.org/document/6886982
- **Abstract**: 400-Gb/s dual-carrier DP-8QAM transmission over 6,787 km is reported at 121.2km span length, the longest to date with EDFA only. Spectral efficiency of 4.54 b/s/Hz is achieved thanks to Nyquist shaping and nonlinear compensation techniques.

## Filter optimization in SDN-based flexgrid networks

- **ID**: ieee:6886804
- **Type**: conference
- **Published**: 9-13 March
- **Authors**: F. Paolucci, F. Fresi, A. Castro +6
- **PDF**: https://ieeexplore.ieee.org/document/6886804
- **Abstract**: The novel super-filter technique for flexgrid optical networks is proposed to compact spectrum-contiguous lightpaths. The technique is applied in a specifically extended SDN architecture, showing significant gains in terms of spectral efficiency.

## Constellation expansion and multi-symbol detection for differentially encoded 100G systems

- **ID**: ieee:6887044
- **Type**: conference
- **Published**: 9-13 March
- **Authors**: Paolo Leoni, Vincent Sleiffer, Stefano Calabrò +1
- **PDF**: https://ieeexplore.ieee.org/document/6887044
- **Abstract**: We propose an approach to differentially encoded 100G transmission that improves both spectral efficiency and OSNR performance over conventional DQPSK-based systems, demonstrating a practical performance beyond the theoretical limit of the conventional approach.

## An efficient VLSI architecture for nonbinary LDPC decoder with adaptive message control

- **ID**: ieee:6922245
- **Type**: conference
- **Published**: 6-8 March 
- **Authors**: S. Suganya, C. Saranya
- **PDF**: https://ieeexplore.ieee.org/document/6922245
- **Abstract**: A new decoder architecture for nonbinary low-density parity check (LDPC) codes is presented in this paper to reduce the hardware operational complexity and power consumption. Adaptive message control (AMC) is to achieve the low decoding complexity, that dynamically trims the message length of belief information to reduce the amount of memory accesses and arithmetic operations. A new horizontal nonbinary LDPC decoder architecture is developed to implement AMC. Key components in the architecture have been designed with the consideration of variable message lengths to leverage the benefit of the proposed AMC. Simulation results demonstrate that the proposed nonbinary LDPC decoder architecture can significantly reduce hardware operations and power consumption as compared with existing work with negligible performance degradation.

## Design and implementation of multi-rate LDPC decoder for IEEE 802.16e wireless standard

- **ID**: ieee:6922226
- **Type**: conference
- **Published**: 6-8 March 
- **Authors**: K. Vijaya Kumar, Rahul Shrestha, Roy Paily
- **PDF**: https://ieeexplore.ieee.org/document/6922226
- **Abstract**: In this paper, a flexible architecture of multi-rate Low Density Parity Check (LDPC) decoder has been presented. It supports six different code-rates which are specified by IEEE 802.16e wireless standard. In the suggested decoder-architecture, column layered decoding technique has been employed to increase the convergence speed. Additionally, the decoder-design incorporates parallel architecture to achieve higher throughput which meets the requirement of IEEE 802.16e standard. An Application Specific Integrated Circuits (ASIC) implementation of this decoder-architecture has been performed at 130 nm Complementary Metal Oxide Semiconductor (CMOS) technology node. At the worst-case Process Voltage Temperature (PVT) corner with the supply voltage of 1.08 V, the implemented decoder has achieved a maximum information throughput of 159.6 Mbps at a clock frequency of 39.9 MHz.

## Error recognition and correction enhanced decoding of hybrid codes for memory application

- **ID**: ieee:6926127
- **Type**: conference
- **Published**: 6-8 March 
- **Authors**: S. Baskar
- **PDF**: https://ieeexplore.ieee.org/document/6926127
- **Abstract**: As technology scales, Multiple Cell Upsets (MCUs) become more common and affect a larger number of cells. In order to protect memories against MCUs as well as SEUs is to make use of advanced Error detecting and correcting codes that can correct more than one error per word. A sub-group of the low-density parity checks (LDPC) codes, which be-longs to the family of the Majority logic decoding has been recently proposed for memory application and Difference set codes are one example of these codes which contributes for error detection and correction. ML decodable Codes are suitable for memory applications due to their capability to correct a large number of errors. In this paper, the proposed scheme for fault-detection and correction method significantly makes area overhead minimal and to reduce the decoding time through DC codes than the existing technique and it gives promising option for memory applications. HDL implementation and synthesis results are included, showing that the proposed techniques can be efficiently implemented.

## Optimized codes for bidirectional relaying

- **ID**: ieee:6811264
- **Type**: conference
- **Published**: 28 Feb.-2 
- **Authors**: Karthik Ravindran, Vinay Praneeth Boda, Andrew Thangaraj +3
- **PDF**: https://ieeexplore.ieee.org/document/6811264
- **Abstract**: In this article, we study coding strategies and code optimization for bidirectional relaying using Low-Density Parity-Check codes. We attempt to achieve extreme points in the rate region using density-evolution-based optimization and a combination of nesting and shortening of codes. The proposed method with specific choice of codes achieves rates close to capacity outer bounds.

## An improved puncturing method for rate-compatible LDPC codes

- **ID**: ieee:6811346
- **Type**: conference
- **Published**: 28 Feb.-2 
- **Authors**: Kuntal Deka, A. Rajesh, P. K. Bora
- **PDF**: https://ieeexplore.ieee.org/document/6811346
- **Abstract**: This paper presents an improvement of a puncturing technique for rate-compatible low density parity check (LDPC) codes originally proposed by Asvadi and Banihashemi. In the original technique, the puncturing bits are selected by progressively reducing the search space according to a certain sequence of criteria. The last criterion is based on the ACE (approximate cycle extrinsic message degree) values of the short cycles present in the Tanner graph of the code. In this paper, we propose to substitute the last criterion with one which is based on the absorbing sets of the code. Simulation results show that this scheme improves the performance compared to the original and some other scheme available in the literature.

## Node-splitting constructions for large girth irregular and protograph LDPC codes

- **ID**: ieee:6811288
- **Type**: conference
- **Published**: 28 Feb.-2 
- **Authors**: Srinivas Subramanian, Asit Kumar Pradhan, Andrew Thangaraj
- **PDF**: https://ieeexplore.ieee.org/document/6811288
- **Abstract**: Low Density Parity Check (LDPC) codes have capacity-approaching performance over several channels of interest. In practice, for good block-error rate performance, the girth of the Tanner graph of an LDPC code needs to be as high as possible. In theory, to show that block-error rate approaches zero for increasing block-lengths, the girth of the Tanner graph sequence needs to tend to infinity with block-length. To meet these requirements, we construct sequences of large-girth irregular LDPC codes for a given degree-distribution pair (DDP) by applying a general node splitting algorithm on large girth graphs. The obtained Tanner graph meets the required DDP up to a suitable approximation. By optimizing the node-splitting method and using suitable large-girth graphs, we show code constructions with smaller block length for the same girth, when compared to previous constructions. Similar gains in block length are observed in the construction of sequences of large-girth protograph LDPC codes. Simulations, over a binary erasure channel, confirm the gains in block-error rate obtained by the large girth construction.

## Optimal communication scheduling for iterative decoding of irregular codes

- **ID**: ieee:6811240
- **Type**: conference
- **Published**: 28 Feb.-2 
- **Authors**: Hrishikesh Sharma, S. Sivasubramanian, S. Patkar
- **PDF**: https://ieeexplore.ieee.org/document/6811240
- **Abstract**: Many important and newer classes of error-correction codes, such as LDPC, expander, repeat-accumulate or polar codes have a bipartite graph representation of their computation. Decoders for such codes are practically implemented using iterative decoding over such bipartite graphs. The iterative decoding progresses as per various communication schedules between the nodes on both sides of the graph. The schedules are designed to be optimal typically in the latency or the throughput of decoding process. Designing optimal schedules for irregular or partial regular codes, which have found way in communication standards such as DVB-S2 and WiMAX, is a challenging problem. In our work, we have tried to design VLSI decoding schemes having optimal communication schedule for such codes. We employed edge-coloring based greedy approach for communication scheduling during the decoding process for such codes. The communication throughput of such decoder systems is provably optimal. As such, it is well-known that the irregular-graph based codes can asymptotically achieve the Shannon limit on erasure channels. Hence we are hopeful that irregular graphs will be used in many other practical error correction systems in future, for which usage of such optimal communication scheduling will lead to efficient design of decoders.

## Implementation and evaluation of error control schemes in Industrial Wireless Sensor Networks

- **ID**: ieee:6895022
- **Type**: conference
- **Published**: 26 Feb.-1 
- **Authors**: Yonas Hagos Yitbarek, Kan Yu, Johan Åkerberg +2
- **PDF**: https://ieeexplore.ieee.org/document/6895022
- **Abstract**: Industrial Wireless Sensor Networks (IWSNs) have been increasingly adopted in process automation due to a number of advantages such as cost reduction and enhanced flexibility. Nevertheless, transmission over wireless channels in industrial environments is prone to interference, resulting in frequent erroneous packet deliveries. Existing IWSN standards based on the IEEE 802.15.4 specification only prescribe Automatic Repeat Request (ARQ) for packet retransmission, without providing any means for error recovery, which leads to unexpected transmission delay. Forward Error Correction (FEC) code as an alternative approach is able to effectively improve reliability and reduce the number of retransmissions. However, FEC computation requires extra memory and processing time. In this paper, we discuss the timing constraints of employing FEC codes for IWSNs according to the IWSN standards. Then we benchmark a number of different FEC codes in a typical wireless sensor node in terms of memory consumption and processing time. Our results show that LDPC and Turbo code, as the state of the art FEC codes, fail to fulfill the requirement from the IWSN standards while other FEC candidates, such as RS code, are proven to be suitable for the practical implementation in IWSNs.

## Hardware implementation of a Reed-Solomon soft decoder based on information set decoding

- **ID**: ieee:6800423
- **Type**: conference
- **Published**: 24-28 Marc
- **Authors**: Stefan Scholl, Norbert Wehn
- **PDF**: https://ieeexplore.ieee.org/document/6800423
- **Abstract**: Soft decision decoding of Reed-Solomon codes can largely improve frame errors rates over currently used hard decision decoding. In this paper, we present a new hardware implementation for soft decoding of Reed-Solomon codes based on information set decoding. To our best knowledge this is the first hardware implementation of information set decoding for long Reed-Solomon codes. We propose a reduced complexity version of the decoding algorithm, that is optimized for efficient hardware implementation and enables high throughput. The decoder was implemented on a Virtex 7 FPGA, achieving a gain of 0.75 dB compared to conventional hard decision decoding and a throughput of up to 1.19 GBit/s for the widely used RS(255,239). This gain in FER is achieved with less complexity and more than 15x larger throughput than other state-of-the-art architectures.

## LDPC coded S-FSK modulation for power line communications

- **ID**: ieee:6840922
- **Type**: conference
- **Published**: 19-22 Marc
- **Authors**: Mohamed Chaker Bali, Chiheb Rebai
- **PDF**: https://ieeexplore.ieee.org/document/6840922
- **Abstract**: With the advancement in various fields of energy and communication sector, there is a strong need to achieve simple and reliable data transmission that will enable various entities connected to the Smart Grids (SG) to exchange vital information at all times. This paper propose a transmission scheme combining spread frequency shift keying (S-FSK) modulation with a low-density parity-check (LDPC) code to make the narrow-band power-line communications (PLC) robust against frequency selective channel. Numerical simulations show that the proposed scheme outperforms the standard specifications with more than 10 dB.

## A new optimization of group shuffled LDPC decoding

- **ID**: ieee:6840905
- **Type**: conference
- **Published**: 19-22 Marc
- **Authors**: Nassib Laouini, Larbi Ben Hadj Slama, Ammar Bouallegue
- **PDF**: https://ieeexplore.ieee.org/document/6840905
- **Abstract**: Shuffled decoding is known to provide efficient and high-throughput implementation of LDPC decoders. In this paper, a new grouping technique of variable nodes to accelerate the message-passing rate is presented. In this algorithm, unlike other group-shuffled decoding methods, we consider for the first sub-group a set of variable nodes that has a low value of the intrinsic information, where the variable nodes of the code graph are divided into sub-groups called layers to perform group-by-group message-passing decoding and each iteration is broken into multiple sub-iterations. This paper proposes a simplification of the Variable Node group-shuffled Belief Propagation (Optimized VN group-shuffled BP) to lower the complexity of the check node update rule. Simulation results, verify that the Optimized VN group-shuffled BP does yield a faster convergence rate than both Belief Propagation (BP) and Check Node group-shuffled Belief Propagation (CN group-shuffled BP) decoder.

## PEG-like algorithm for LDPC codes

- **ID**: ieee:6925956
- **Type**: conference
- **Published**: 19-21 Marc
- **Authors**: Gan Srirutchataboon, Ambar Bajpai, Lunchakorn Wuttisittikulkij +1
- **PDF**: https://ieeexplore.ieee.org/document/6925956
- **Abstract**: Progressive Edge-Growth (PEG) algorithm is one of the promising methods to construct a parity-check matrix (or H matrix) with a large girth for low-density parity-check (LDPC) codes. However, generating a large H matrix based on a PEG algorithm usually requires a lot of computations because of its complexity. This paper proposes an alternative method based on a topology matrix to construct the H matrix, which has lower complexity than the PEG algorithm. We refer to the proposed method as a “PEG-like” algorithm. Results indicate that the proposed method can provide the same H matrix as the PEG algorithm does but with lower complexity.

## Output decisions for stochastic LDPC decoders

- **ID**: ieee:6814072
- **Type**: conference
- **Published**: 19-21 Marc
- **Authors**: Kuo-Lun Huang, Vincent Gaudet, Masoud Salehi
- **PDF**: https://ieeexplore.ieee.org/document/6814072
- **Abstract**: Stochastic decoding is a method to iteratively decode error-correcting codes such as low-density parity-check codes. Due to the computational simplicity of its decoding algorithm, stochastic decoding provides not only low silicon area but also competitive performance. In this paper, we research the different techniques used to determine the code bits generated by stochastic decoders during the final decision process. We investigate an efficient method where code bits are directly decided based on the final stochastic bits generated at output nodes. This observation contributes to saving chip area and providing high throughput for stochastic decoders.

## Low-density MDS array codes based on rigid graph structure

- **ID**: ieee:6925897
- **Type**: conference
- **Published**: 19-21 Marc
- **Authors**: Nattakan Puttarak, Phisan Kaewprapha
- **PDF**: https://ieeexplore.ieee.org/document/6925897
- **Abstract**: In data communications system including wired and wireless transmissions, the reliability, integrity, speed, and cost efficiency are the main issues that people desire. An error correcting code is one of the efficient and nearly-optimal methods to improve the system performance. Based on the idea of constructing MDS codes called CGR codes in [3] for disk arrays, this paper introduces a new perspective and construction of LDPC codes due to its sparsity and advantage complexity in implementation. The performance of this code in Additive White Gaussian Noise (AWGN) and fading channels gains about 1.0 dB at the 10-3 of bit error rate (BER) compared with an EVENODD code.

## Hybrid analog-digital coding scheme based on parallel concatenation of linear random projections and LDGM codes

- **ID**: ieee:6814118
- **Type**: conference
- **Published**: 19-21 Marc
- **Authors**: Lu Li, Javier Garcia-Frias
- **PDF**: https://ieeexplore.ieee.org/document/6814118
- **Abstract**: This paper aims at designing a hybrid analog-digital coding scheme that can be applied for rate adaption in a broad dynamic range of channel conditions. The hybrid scheme is constructed by generating most of the output symbols from standard linear combinations of the input bits, as in Rate Compatible Modulation (RCM), and a few of them using a Low Density Generator Matrix (LDGM) code. RCM is able to achieve smooth rate adaption, but its performance is far from the Shannon theoretical limits. The few coded bits proceeding from the LDGM code are able to substantially reduce the number of uncorrected errors in the RCM scheme, substantially improving the system performance.

## Analog mappings for flexible rate transmission of Gaussian sources with side information

- **ID**: ieee:6814102
- **Type**: conference
- **Published**: 19-21 Marc
- **Authors**: Bo Lu, Javier Garcia-Frias
- **PDF**: https://ieeexplore.ieee.org/document/6814102
- **Abstract**: This paper considers the problem of designing bandwidth expansion zero-delay analog joint source-channel coding (JSCC) schemes for the transmission of memoryless Gaussian samples over additive white Gaussian noise (AWGN) channels when side information is present at the receiver (Wyner-Ziv scenario). We first propose a 1 : 1 scheme and a 1 : M scheme based on the use of Shannon-Kotel'nikov mappings in a periodic fashion. Then, we combine the two proposed mappings to construct a flexible rate bandwidth expansion mapping whose rate can be anywhere from 1 : 1 to 1 : M. Different from digital systems, the proposed scheme offers low delay, low complexity and high robustness. Simulation results show that the performance of the proposed 1 : 2 scheme is better than that of existing zero-delay systems for a wide range of signal to noise ratios, but especially for high signal to noise ratios and highly correlated side information. The proposed flexible rate bandwidth expansion system also offers satisfactory performance, specially when considering its great flexibleness in terms of rate.

## Designing and implementing Low Density Parity Check (LDPC) Decoders using FPGAs

- **ID**: ieee:6836261
- **Type**: conference
- **Published**: 1-8 March 
- **Authors**: John C. Porcello
- **PDF**: https://ieeexplore.ieee.org/document/6836261
- **Abstract**: Low Density Parity Check (LDPC) Codes offer remarkable error correction performance and therefore increase the design space for communication systems. When implementation complexity and latency are not system limitations, LDPC codes can offer near Shannon Limit performance by using large code lengths and increasing the number of iterations in the decoding process. Furthermore, LDPC codes with smaller block sizes are also of value to the communications system designer and LDPC codes have found practical use in DVB-S2 and other standards. This paper considers design issues with respect to FPGA implementation of LDPC Decoders. Specifically, this paper presents a scalable FPGA architecture for LDPC soft decision decoding based on the Sum Product Algorithm (SPA) for regular LDPC codes. The paper begins with an overall discussion of issues surrounding the use of LDPC codes, followed by a discussion of LDPC decoding using the SPA. A scalable FPGA implementation of an SPA LDPC Decoder is introduced. Design data is provided to support FPGA implementation of this approach for LDPC decoding and quantify required hardware resources. A discussion of trade space for LDPC code implementation based on the FPGA resources is also provided. Finally, an example design is provided based on a Xilinx Virtex-7 to illustrate the concepts discussed in the paper and provide insight into the challenging task of implementing an LDPC decoder in FPGAs.

## AES-TURBO as a single primitive for land mobile satellite channel

- **ID**: ieee:6804443
- **Type**: conference
- **Published**: 1-2 March 
- **Authors**: Rajashri Khanai, G. H. Kulkarni, Dattaprasad A. Torse
- **PDF**: https://ieeexplore.ieee.org/document/6804443
- **Abstract**: The data transmission of encrypted blocks over a noisy channel requires an additional step of error-correction coding. In this paper, we study a 25 years old question of combining encryption and error-correction coding, named here as Crypto-Coding. For reliable and secure data transmission over unreliable channel, we have introduced an algorithm that combines Advanced Encryption Standard (AES) for encryption and Turbo code for error correction as a single primitive. The combined system's performances are evaluated over Land Mobile Satellite (LMS) Channel. Simulation results show that the BER performance of the system is close to the traditional cryptcoding, for data length equal to 1024 bits, and achieves a BER of about 4 × 10-5 at an SNR of 10 dB. The proposed algorithms are well suited for implementation on a VLSI-platform.
