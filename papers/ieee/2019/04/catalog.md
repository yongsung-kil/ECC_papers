# IEEE Xplore — 2019-04


## Design of Irregular SC-LDPC Codes With Non-Uniform Degree Distributions by Linear Programming

- **ID**: ieee:8590739
- **Type**: journal
- **Published**: April 2019
- **Authors**: Hee-Youl Kwak, Jong-Seon No, Hosung Park
- **PDF**: https://ieeexplore.ieee.org/document/8590739
- **Abstract**: In this paper, we propose new design algorithms of irregular spatially-coupled low-density parity-check (SC-LDPC) codes with non-uniform degree distributions using linear programming (LP). In general, irregular SC-LDPC codes with non-uniform degree distributions are difficult to design with low complexity because their density evolution equations are multi-dimensional. To overcome this problem, proposed design algorithms are based on three main ideas: a local design of degree distributions, pre-computation of the input/output message relationship, and selection of a proper objective function. These ideas make it possible to design degree distributions of irregular SC-LDPC codes by solving low-complexity LP problems over the binary erasure channel (BEC). It is shown that the proposed irregular SC-LDPC codes designed by the proposed algorithms are superior to regular SC-LDPC codes in terms of both asymptotic and finite-length performances over the BEC. We also confirm that the proposed irregular SC-LDPC code achieves better performance compared with an optimized irregular block LDPC code in the same blocklength, which implies that the proposed design algorithms also provide a new way to construct capacity-approaching block LDPC codes.

## Layered LDPC Decoders With Efficient Memory Access Scheduling and Mapping and Built-In Support for Pipeline Hazards Mitigation

- **ID**: ieee:8579225
- **Type**: journal
- **Published**: April 2019
- **Authors**: Oana Boncalo, Gyorgy Kolumban-Antal, Alexandru Amaricai +2
- **PDF**: https://ieeexplore.ieee.org/document/8579225
- **Abstract**: This paper proposes a holistic approach that addresses both the message mapping in memory banks and the pipeline-related data hazards in low-density parity-check (LDPC) decoders. We consider a layered hardware architecture using single read/single write port memory banks. The throughput of such an architecture is limited by memory access conflicts, due to improper message mapping in the memory banks, and by pipeline data hazards, due to delayed update effect. We solve these issues by: 1) a residue-based layered scheduling that reduces the pipeline related hazards and 2) off-line algorithms for optimizing the message mapping in memory banks and the message read access scheduling. Our estimates for different LDPC codes indicate that the hardware usage efficiency of our layered decoder is improved by 3%-49% when only the off-line algorithms are employed and by 16%-57% when both the residue-based layered architecture and the off-line algorithms are used.

## From Cages to Trapping Sets and Codewords: A Technique to Derive Tight Upper Bounds on the Minimum Size of Trapping Sets and Minimum Distance of LDPC Codes

- **ID**: ieee:8525278
- **Type**: journal
- **Published**: April 2019
- **Authors**: Ali Dehghan, Amir H. Banihashemi
- **PDF**: https://ieeexplore.ieee.org/document/8525278
- **Abstract**: Cages, defined as regular graphs with minimum number of nodes for a given girth, are well-studied in graph theory. Trapping sets are graphical structures responsible for error floor of low-density parity-check (LDPC) codes, and are well investigated in coding theory. In this paper, we make connections between cages and trapping sets. In particular, starting from a cage (or a modified cage), we construct a trapping set in multiple steps. Based on the connection between cages and trapping sets, we then use the available results in graph theory on cages and derive tight upper bounds on the size of the smallest trapping sets for variable-regular LDPC codes with a given variable degree and girth. The derived upper bounds in many cases meet the best known lower bounds and thus provide the actual size of the smallest trapping sets. Considering that non-zero codewords are a special case of trapping sets, we also derive tight upper bounds on the minimum weight of such codewords, i.e., the minimum distance, of variable-regular LDPC codes as a function of variable degree and girth.

## Resource Allocation for LDPC-Coded OFDM Downlink Channels

- **ID**: ieee:8587191
- **Type**: journal
- **Published**: April 2019
- **Authors**: Max Bluvshtein, Ofer Amrani
- **PDF**: https://ieeexplore.ieee.org/document/8587191
- **Abstract**: Various techniques have been proposed to address the problem of resource allocation in multi-carrier communications. These techniques, for the most part, arise from information-theoretic measures or otherwise associated with the channel behavior, which does not necessarily model the coding being employed. In this paper, an optimization technique is tailored for low density parity-check (LDPC) coded orthogonal frequency-division multiplexing (OFDM) systems, by employing the so-called general stability condition introduced by Richardson et al. The latter formulates a necessary condition for the belief-propagation decoder to perfectly decode a received vector with no errors. The general condition is re-formulated so as to model practical multi-carrier systems, such as OFDM. Consequently, a general resource-allocation framework is laid down for optimizing the transmitted power based on the characteristics of the LDPC code in use. The proposed optimization technique is utilized for power allocation in orthogonal frequency-division multiple access systems; and the transmitted power is minimized while guaranteeing reliable decoding. To validate the proposed approach, it is compared to information-theoretic-based methods that aim at optimizing the mutual information between the transmitter and the receiver. Both approaches are shown to provide almost identical performance for the scenarios addressed in this paper.

## Protograph-Based Folded Spatially Coupled LDPC Codes for Burst Erasure Channels

- **ID**: ieee:8515101
- **Type**: journal
- **Published**: April 2019
- **Authors**: Inayat Ali, Hyunjae Lee, Ayaz Hussain +1
- **PDF**: https://ieeexplore.ieee.org/document/8515101
- **Abstract**: In this letter, protograph-based folded spatially coupled (FSC) LDPC codes are proposed. The new folded-type structure is obtained by folding the spatial coupling chain of a conventional spatially coupled (SC) LDPC protograph and interlacing the nodes at staggered spatial positions. The proposed codes outperform the SC LDPC codes over single and multiple random-burst erasure channels. We extend the construction of the folded-type structure by connecting multiple one-sided SC LDPC chains for higher resilience to burst erasure channels. The FSC LDPC codes are also compatible with windowed decoder and outperform conventional SC LDPC codes.

## Additive, Structural, and Multiplicative Transformations for the Construction of Quasi-Cyclic LDPC Matrices

- **ID**: ieee:8594652
- **Type**: journal
- **Published**: April 2019
- **Authors**: Alban Derrien, Emmanuel Boutillon, Audrey Cerqueus
- **PDF**: https://ieeexplore.ieee.org/document/8594652
- **Abstract**: The construction of a quasi-cyclic low density parity-check (QC-LDPC) matrix is usually carried out in two steps. In the first step, a prototype matrix is defined according to certain criteria (size, girth, check and variable node degrees, and so on). The second step involves the expansion of the prototype matrix. During this last phase, an integer value is assigned to each non-null position in the prototype matrix corresponding to the right-rotation of the identity matrix. The problem of determining these integer values is complex. The state-of-the-art solutions use either some mathematical constructions to guarantee a given girth of the final QC-LDPC code, or a random search of values until the target girth is satisfied. In this paper, we propose an alternative/complementary method that reduces the search space by defining large equivalence classes of topologically identical matrices through row and column permutations using additive, structural, and multiplicative transformations. Selecting only a single element per equivalence class can reduce the search space by a few orders of magnitude. Then, we use the formalism of constraint programming to list the exhaustive sets of solutions for a given girth and a given expansion factor. An example is presented in all sections of the paper to illustrate the methodology.

## A Combinatorial Methodology for Optimizing Non-Binary Graph-Based Codes: Theoretical Analysis and Applications in Data Storage

- **ID**: ieee:8466851
- **Type**: journal
- **Published**: April 2019
- **Authors**: Ahmed Hareedy, Chinmayi Lanka, Nian Guo +1
- **PDF**: https://ieeexplore.ieee.org/document/8466851
- **Abstract**: Non-binary (NB) low-density parity-check (LDPC) codes are graph-based codes that are increasingly being considered as a powerful error correction tool for modern dense storage devices. Optimizing NB-LDPC codes to overcome their error floor is one of the main code design challenges facing storage engineers upon deploying such codes in practice. Furthermore, the increasing levels of asymmetry incorporated by the channels underlying modern dense storage systems, e.g., multi-level Flash systems, exacerbate the error floor problem by widening the spectrum of problematic objects that contribute to the error floor of an NB-LDPC code. In a recent research, the weight consistency matrix (WCM) framework was introduced as an effective combinatorial NB-LDPC code optimization methodology that is suitable for modern Flash memory and magnetic recording (MR) systems. The WCM framework was used to optimize codes for asymmetric Flash channels, MR channels that have intrinsic memory, in addition to canonical symmetric additive white Gaussian noise channels. In this paper, we provide an in-depth theoretical analysis needed to understand and properly apply the WCM framework. We focus on general absorbing sets of type two (GASTs) as the detrimental objects of interest. In particular, we introduce a novel tree representation of a GAST called the unlabeled GAST tree, using which we prove that the WCM framework is optimal in the sense that it operates on the minimum number of matrices, which are the WCMs, to remove a GAST. Then, we enumerate WCMs and demonstrate the significance of the savings achieved by the WCM framework in the number of matrices processed to remove a GAST. Moreover, we provide a linear-algebraic analysis of the null spaces of WCMs associated with a GAST. We derive the minimum number of edge weight changes needed to remove a GAST via its WCMs, along with how to choose these changes. In addition, we propose a new set of problematic objects, namely oscillating sets of type two (OSTs), which contribute to the error floor of NB-LDPC codes with even column weights on asymmetric channels, and we show how to customize the WCM framework to remove OSTs. We also extend the domain of the WCM framework applications by demonstrating its benefits in optimizing column weight 5 codes, codes used over Flash channels with additional soft information, and spatially coupled codes. The performance gains achieved via the WCM framework range between 1 and nearly 2.5 orders of magnitude in the error floor region over interesting channels.

## Unequal Error Protection SCMA Codebooks

- **ID**: ieee:8637721
- **Type**: journal
- **Published**: April 2019
- **Authors**: Zeina Mheich, Lei Wen, Pei Xiao +1
- **PDF**: https://ieeexplore.ieee.org/document/8637721
- **Abstract**: This paper investigates the design of unequal error protection (UEP) codebooks for sparse code multiple access (SCMA) systems. We propose a joint low-density parity check (LDPC) code and SCMA codebook design approach by incorporating cloud partitioning of codewords in the design of SCMA codebooks with different protection levels. The protection levels of the SCMA codebooks could be optimized based on the existing error correction code. Simulation results show that significant gains could be obtained using code-aware UEP SCMA codebooks, compared to codebooks designed independently of the channel code.

## Energy-Adaptive Error Correcting for Dynamic and Heterogeneous Networks

- **ID**: ieee:8665995
- **Type**: journal
- **Published**: April 2019
- **Authors**: Haewon Jeong, Pulkit Grover
- **PDF**: https://ieeexplore.ieee.org/document/8665995
- **Abstract**: In an era of ever-increasing dynamicity and heterogeneity of wireless networks, energy is fast becoming the most constrained resource. First, we review recent studies that suggest that using one single error-correcting code (ECC) designed to meet the worst case requirement is inefficient in terms of energy consumption when there are many heterogeneous nodes in the network. These works extend the classical Shannon theory and incorporate circuit energy and signal transmit energy to optimize total energy/power consumption of today's communication systems. Then, we survey recent work on designing adaptive ECCs to operate energy efficiently even in the presence of extremely large heterogeneity in requirements and conditions. Two constructions of energy-adaptive codes are summarized: energy-adaptive low-density parity-check (LDPC) codes and energy-adaptive polar codes. These constructions have shown theoretically and empirically that having adaptivity in code design can save substantial energy, especially when the network has very diverse communication scenarios. Finally, we suggest a few possible applications where energy-adaptive codes can be employed and outline interesting future directions and challenges.

## Error Performance Prediction of Randomly Shortened and Punctured LDPC Codes

- **ID**: ieee:8649667
- **Type**: journal
- **Published**: April 2019
- **Authors**: Adriaan Suls, Yannick Lefevre, Jeroen Van Hecke +2
- **PDF**: https://ieeexplore.ieee.org/document/8649667
- **Abstract**: In this contribution, we show that the word error rate (WER) performance in the waterfall region of a randomly shortened and punctured low density parity check code can be accurately predicted from the WER performance of its finite-length mother code. We derive an approximate analytical expression for the mutual information (MI) required by a daughter code to achieve a given WER, based on the MI required by the mother code, which shows that the gap to the capacity of the daughter code grows the more the code is punctured or shortened. The theoretical results are confirmed by simulations (where the random shortening and puncturing pattern is either selected independently per codeword or kept the same for all codewords) for practical codes on both the binary erasure channel and the binary-input additive white Gaussian noise channel.

## Repeat-Accumulate Signal Codes

- **ID**: ieee:8584892
- **Type**: journal
- **Published**: April 2019
- **Authors**: Manato Takai, Koji Ishibashi
- **PDF**: https://ieeexplore.ieee.org/document/8584892
- **Abstract**: State-constrained signal codes directly encode modulation signals using signal processing filters, the coefficients of which are constrained over the rings of formal power series. Although the performance of signal codes is defined by these signal filters, optimal filters must be found by brute-force search in terms of the symbol error rate because the asymptotic behavior with different filters has not been investigated. Moreover, the computational complexity of the conventional BCJR used in the decoder increases exponentially, as the number of output constellations increases. We hence propose a new class of state-constrained signal codes called repeat-accumulate signal codes (RASCs). To analyze the asymptotic behavior of these codes, we employ Monte Carlo density evolution (MC-DE). As a result, the optimum filters can be efficiently found for the given parameters of the encoder. We also introduce a low-complexity decoding algorithm for RASCs called the extended min-sum (EMS) decoder. The MC-DE analysis shows that the difference between the noise thresholds of RASC and the Shannon limit is within 0.8 dB. The simulation results moreover show that the EMS decoder can reduce the computational complexity to less than 25% of that of conventional decoder without degrading the performance by more than 1 dB.

## LDPC-Coded Generalized Frequency Division Multiplexing for Intensity-Modulated Direct-Detection Optical Systems

- **ID**: ieee:8657778
- **Type**: journal
- **Published**: April 2019
- **Authors**: Dong Guo, Wei Zhang, Feng Tian +8
- **PDF**: https://ieeexplore.ieee.org/document/8657778
- **Abstract**: In this paper, a low-density parity check (LDPC) coded GFDM with high-level modulation scheme is proposed for more flexible and advanced multicarrier modulation in intensity-modulated/direct-detection (IM/DD) optical systems. Then, we experimentally demonstrate an LDPC-coded GFDM with 16-quadrature amplitude modulation (16QAM) system transmitted over 20-km standard single-mode fiber at different symbol rates to verify the applicability of the proposed scheme. Furthermore, the proposed scheme with trellis-coded 32-quadrature amplitude modulation (TC-32QAM) has also been investigated and compared with the bit error rate (BER) performance with 16QAM-modulated condition. The results indicate that TC-32QAM-modulated GFDM method has a better performance than the 16QAM-modulated case. But with LDPC coding module added, the performance of the proposed system with TC-32QAM gets worse than that with 16QAM modulation. We also experimentally compare the proposed LDPC-coded scheme and the Turbo-coded scheme in the QAM-modulated GFDM IM/DD optical system. The results show the LDPC-coded optical (LCO-) GFDM scheme has lower power penalties and better BER performance. Moreover, the proposed LCO-GFDM scheme is applied in multiband transmission by optical simulation software, and the results show that multiband LCO-GFDM scheme has a better performance than that of LCO-OFDM scheme.

## Divergence-Optimal Fixed-to-Fixed Length Distribution Matching With Shell Mapping

- **ID**: ieee:8599055
- **Type**: journal
- **Published**: April 2019
- **Authors**: Patrick Schulte, Fabian Steiner
- **PDF**: https://ieeexplore.ieee.org/document/8599055
- **Abstract**: Distribution matching (DM) transforms independent and Bernoulli(1/2) distributed bits into a sequence of output symbols with a desired distribution. A fixed-to-fixed length, invertible DM architecture based on shell mapping (SM) is presented. It is shown that SM for DM (SMDM) is the optimum DM for the informational divergence metric and that finding energy optimal sequences is a special case of divergence minimization. Additionally, it is shown how to find the required SM weight function to approximate arbitrary output distributions. SMDM is combined with probabilistic amplitude shaping to operate close to the Shannon limit. SMDM exhibits excellent performance for short blocklengths as required by ultra-reliable low-latency applications. SMDM outperforms constant composition DM by 0.7 dB when used with 64-QAM at a spectral efficiency of 3 bits/channel use and a 5G low-density parity-check code with a short blocklength of 192 bits.

## A Low Complexity Signal Detection Scheme Based on Improved Newton Iteration for Massive MIMO Systems

- **ID**: ieee:8638827
- **Type**: journal
- **Published**: April 2019
- **Authors**: Fangli Jin, Qiufeng Liu, Hao Liu +1
- **PDF**: https://ieeexplore.ieee.org/document/8638827
- **Abstract**: Massive multiple-input multiple-output (MIMO) systems need to handle a large number of matrix inversion operations during the signal detection process. Several methods have been proposed to avoid exact matrix inversion in massive MIMO systems, which can be roughly divided into approximation methods and iterative methods. In this letter, we first introduce the relationship between the two types of signal detection methods. Then, an improved Newton iteration method is proposed on the basis of the relationship. And by converting the matrix-matrix product into the matrix-vector product, the computational complexity is substantially reduced. Finally, numerical simulations further verify that the proposed Newton method outperforms Neumann series expansion and the existing Newton method, and can approach the performance of minimum mean square error (MMSE) method within a few iterations, regardless of whether the base station can obtain perfect channel state information or not.

## Interleave-Division Multiple Access in High Rate Applications

- **ID**: ieee:8494711
- **Type**: journal
- **Published**: April 2019
- **Authors**: Yang Hu, Chulong Liang, Lei Liu +3
- **PDF**: https://ieeexplore.ieee.org/document/8494711
- **Abstract**: Interleave-division multiple access (IDMA) is a multiple access scheme that has been considered in several recent proposals for the 5th generation cellular system. In this letter, basing on evolution analysis, we show that the performance of IDMA can be enhanced using the transfer function matching principle. Such matching can be realized by superposition coded modulation, power control, repetition coding, and zero padding. Zero padding together with cyclic shifting also leads to reduced implementation complexity. Our analysis is based on additive white Gaussian noise channels and we show by simulations that the matching techniques can also provide impressive performance in fading channels.

## Outage Analysis and Finite SNR Diversity-Multiplexing Tradeoff of Hybrid-Duplex Systems for Aeronautical Communications

- **ID**: ieee:8663632
- **Type**: journal
- **Published**: April 2019
- **Authors**: Tan Zheng Hui Ernest, A. S. Madhukumar, Rajendra Prasad Sirigina +1
- **PDF**: https://ieeexplore.ieee.org/document/8663632
- **Abstract**: A hybrid-duplex aeronautical communication system (HBD-ACS) consisting of a full-duplex-enabled ground station (GS) and two half-duplex (HD) air stations (ASs) is proposed as a direct solution to the spectrum crunch faced by the aviation industry. The closed-form outage probability and finite signal-to-noise ratio (SNR) diversity gain expressions in aeronautical communications over Rician fading channels are derived for a successive interference cancellation (SIC) detector. Similar expressions are also presented for an interference ignorant (II) detector and the HD-equivalent modes at GS and ASs. Through the outage and finite SNR diversity gain analysis conducted at the nodes, and system level, residual self-interference (SI) and inter-AS interference are found to be the primary limiting factors in the proposed HBD-ACS. Further investigations revealed that the II and SIC detectors in the proposed HBD-ACS are suitable for the weak and strong interference scenarios, respectively. When compared with the HD-ACS, the proposed HBD-ACS achieves a lower outage probability and higher diversity gains at higher multiplexing gains when operating at low SNRs. The finite SNR analysis also showed the possibility of the proposed HBD-ACS being able to attain interference-free diversity gains through proper management of the residual SI. Hence, the proposed HBD-ACS is more reliable and can provide a better throughput compared with the existing HD-ACS at low-to-moderate SNRs.

## Circular-Shift Linear Network Codes With Arbitrary Odd Block Lengths

- **ID**: ieee:8594637
- **Type**: journal
- **Published**: April 2019
- **Authors**: Qifu Tyler Sun, Hanqi Tang, Zongpeng Li +2
- **PDF**: https://ieeexplore.ieee.org/document/8594637
- **Abstract**: Circular-shift linear network coding (LNC) is a class of vector LNC with low encoding and decoding complexities, and with local encoding kernels chosen from cyclic permutation matrices. When L is a prime with primitive root 2, it was recently shown that a scalar linear solution over GF(2L-1) induces an L-dimensional circular-shift linear solution at rate (L-1)/L. In this paper, we prove that for arbitrary odd L, every scalar linear solution over GF(2mL), where mL refers to the multiplicative order of 2 modulo L, can induce an L-dimensional circular-shift linear solution at a certain rate. Based on the generalized connection, we further prove that for such L with mL beyond a threshold, every multicast network has an L-dimensional circular-shift linear solution at rate φ(L)/L, where φ(L) is the Euler's totient function of L. An efficient algorithm for constructing such a solution is designed. Finally, we prove that every multicast network is asymptotically circular-shift linearly solvable.

## A Systematic Approach to Incremental Redundancy With Application to Erasure Channels

- **ID**: ieee:8586906
- **Type**: journal
- **Published**: April 2019
- **Authors**: Anoosheh Heidarzadeh, Jean-Francois Chamberland, Richard D. Wesel +1
- **PDF**: https://ieeexplore.ieee.org/document/8586906
- **Abstract**: This paper focuses on the design and evaluation of pragmatic schemes for delay-sensitive communication. Specifically, this contribution studies the operation of data links that employ incremental redundancy as a means to shield information bits from the degradation associated with unreliable channels. While this inquiry puts forth a general methodology, exposition centers around erasure channels because they are well suited for analysis. Nevertheless, the goal is to identify both structural properties and design guidelines that are broadly applicable. Conceptually, this paper leverages a methodology, termed sequential differential optimization, aimed at identifying near-optimal block sizes for hybrid ARQ. This technique is applied to erasure channels and it is extended to scenarios where throughput is maximized subject to a constraint on the feedback rate. The analysis shows that the impact of the coding strategy adopted and the propensity of the channel to erase symbols naturally decouple when maximizing throughput. Ultimately, block size selection is informed by approximate distributions on the probability of decoding success at every stage of the incremental transmission process. This novel perspective, which rigorously bridges hybrid automatic repeat request and coding, offers a computationally efficient framework to select code rates and blocklengths for incremental redundancy. These findings are supported through numerical results.

## Coupling Information Transmission With Window Decoding

- **ID**: ieee:8525313
- **Type**: journal
- **Published**: April 2019
- **Authors**: Alireza Karami, Dmitri Truhachev
- **PDF**: https://ieeexplore.ieee.org/document/8525313
- **Abstract**: We consider a coupling information transmission modulation format utilized for communication over a multiple-access channel. A multitude of packets is transmitted by a number of sources to a common receiver. Each packet is modulated via simple repetition, interleaving, and an application of a signature sequence. The packets are transmitted with time offsets that initiate coupling of the transmitted signals into a received signal that lends itself to an efficient window-based iterative estimation and interference cancellation decoding. We present the window decoding formulation, a theoretic analysis, and numerical results for the achievable sum-rate, gap to the channel capacity and the optimal window size.

## MRB Decoding of LT Codes Over AWGN Channels

- **ID**: ieee:8520872
- **Type**: journal
- **Published**: April 2019
- **Authors**: Valerio Bioglio
- **PDF**: https://ieeexplore.ieee.org/document/8520872
- **Abstract**: In this letter we propose a novel decoder for Luby transform codes over noisy channel based on Gaussian elimination algorithm. The proposed soft-on-the-fly Gaussian elimination algorithm permits to perform most reliable basis decoding while distributing the complexity all along the symbols reception, and reducing the latency due to new decoding attempts in case of decoding failures.

## Optimization of Non Binary Parity Check Coefficients

- **ID**: ieee:8536465
- **Type**: journal
- **Published**: April 2019
- **Authors**: Emmanuel Boutillon
- **PDF**: https://ieeexplore.ieee.org/document/8536465
- **Abstract**: This paper generalizes the method proposed by Poulliat et al. for the determination of the optimal Galois field coefficients of a non-binary LDPC parity check constraint based on the binary image of the code. Optimal, or almost-optimal, parity check coefficients are given for check degree varying from 4 to 20 and Galois field varying from GF (64) up to GF (1024). For all given sets of coefficients, no codeword of Hamming weight two exists. A reduced complexity algorithm to compute the binary Hamming weight 3 of a parity check is proposed. When the number of sets of coefficients is too high for an exhaustive search and evaluation, a local greedy search is performed. Explicit tables of coefficients are given. The proposed sets of coefficients can effectively replace the random selection of coefficients often used in NB-LDPC construction.

## Read Voltage Optimization in MLC NAND Flash Memory via the Density Evolution

- **ID**: ieee:8798808
- **Type**: conference
- **Published**: 8-10 April
- **Authors**: Chatuporn Duangthong, Watid Phakphisut, Pornchai Supnithi
- **PDF**: https://ieeexplore.ieee.org/document/8798808
- **Abstract**: The multi-level-cell (MLC) NAND flash memory can typically use multiple reads for obtaining soft information for the LDPC decoder. The multiple reads give the soft information which is quantized to a certain level. The major challenge is that the read voltages must be precisely selected to provide better soft information. In the previous work, the read voltages are selected so that the soft information has the maximum mutual information (MMI). However, the error-correction capability of LDPC decoder is not considered. Therefore, in this work, we analyze the performance of LDPC decoder by density evolution whereby the soft information is quantized. Then the optimal read voltages for given LDPC codes are obtained. As a result, for a regular LDPC code with the read voltages optimized by density evolution can provide the lower BER performance compared with the MMI technique.

## Sliding-Window Processing of Turbo Equalization for Partial Response Channels

- **ID**: ieee:8798835
- **Type**: conference
- **Published**: 8-10 April
- **Authors**: Sirawit Khittiwitchayakul, Watid Phakphisut, Pornchai Supnithi
- **PDF**: https://ieeexplore.ieee.org/document/8798835
- **Abstract**: Spatially coupled low-density parity-check (SC-LDPC) codes are the attractive candidates for the application requiring a practical constraint on the latency and complexity. In previous works, the turbo equalization consisting the SC-LDPC window decoder and Bahl-Cocke-Jelinek-Raviv (BCJR) detector is used to tackle the inter-symbol interferences (ISIs) in the magnetic recording systems. However, the prior works consider only the SC-LDPC codes which replace the conventional LDPC block codes. In this work, we propose the modification of turbo equalization processing whereby both the SC-LDPC decoder and BCJR detector operate using the sliding window. The results show that the proposed turbo equalization schemes used in the partial response (PR) channel can provide better bit error rate (BER) performances than the conventional turbo equalization.

## High Throughput and Low Complexity Implementation for Uplink Scheme of 5G Technology

- **ID**: ieee:8798862
- **Type**: conference
- **Published**: 8-10 April
- **Authors**: Pham Chi Bao, Dang Van Xuan Huong, Duc Ngoc Minh Dang +2
- **PDF**: https://ieeexplore.ieee.org/document/8798862
- **Abstract**: In order to increase the efficiency of utilizing transmission bandwidth on 5G technology, a non-orthogonal multiple access (NOMA) scheme is emerging on this research topic to support multiple users for uplink transmission. In this paper, we present an Uplink Sparse code multiple access (SCMA) system based on the euclidean distance between received constellation points and the reference constellation points set and the biding relationship of resources. Low-density Parity-check (LDPC) decoding is used for channel coding in our system. In order to speed up processing latency, a 2-level piplined decoder is proposed. Firstly, we have designed and simulated for 6 users-Uplink SCMA system using MATLAB code, then we have implemented the system using Xilinx Generator. The results show that the system not only ensures BER requirements but also significantly reduces hardware resources and increases transmission throughput compared to the reference system.

## Fast DSP Implementation of a Low Complexity LDPC Decoder

- **ID**: ieee:8723838
- **Type**: conference
- **Published**: 3-4 April 
- **Authors**: Mouhcine Razi, Anas Mansouri, Mhammed Benhayoun +2
- **PDF**: https://ieeexplore.ieee.org/document/8723838
- **Abstract**: The Belief Propagation (BP) algorithm is known as the most efficient algorithm in terms of convergence speed. But this algorithm has a very high level of computational complexity. The Min Sum Algorithm (MSA) permits to reduce this computational complexity but with some performances degradations. In this paper we recommend a new approach with more simplified algorithm, that allows to get performances near to these of the BP algorithm by adopting a new version of the MSA algorithm. This last uses Horizontal Shuffled (HS) scheduling instead of the usually used flooding scheduling. This algorithm was successfully implemented on the Digital Signal Processor (DSP). The results obtained after implementation show that the proposed version of the MSA algorithm does not only improve the decoding performance but also decreases the number of iterations necessary for the decoding of the LDPC codes.

## New Memory Load Optimization Approach for Software Implementation of Irregular LDPC Encoder/Decoder

- **ID**: ieee:8723841
- **Type**: conference
- **Published**: 3-4 April 
- **Authors**: Mhammed Benhayoun, Mouhcine Razi, Anas Mansouri +1
- **PDF**: https://ieeexplore.ieee.org/document/8723841
- **Abstract**: This paper presents a soft implementation of the joint approach for irregular Low Density Parity Check (LDPC) encoding and decoding. The principal idea is to construct excellent irregular LDPC codes focus to two constraints that make certain the effective LDPC encoder and decoder implementations. This work propose a new model for memory loading of the LDPC parity-check matrix aiming to use only the Level one (L1) of cache memory, to take advantage of its high speed latency.

## Performance Analysis of Layered Normalized Min-Sum for LDPC Codes over Weibull Fading Channels

- **ID**: ieee:8723865
- **Type**: conference
- **Published**: 3-4 April 
- **Authors**: Nejwa El Maammar, Jaouad Foshi, Seddik Bri +2
- **PDF**: https://ieeexplore.ieee.org/document/8723865
- **Abstract**: Normalized Min-Sum Algorithms (NMSA) are extensively employed in trading LDPC (Low Density Parity Check) decoders due to their low complexity and reasonable performance close to the performance of sum product algorithm in terms of Error Rate. Our work is focused on the enhancement of error rate performances of NMS algorithm for the decoding of LDPC decoding. In this context we have proposed a Layered Normalized Min-Sum algorithm (LNMS), which employs an adaptive normalization factor to ameliorate the reliability of the information transmitted during the decoding process. To perform this analysis study LDPC coded communication system has been examined over Weibull fading channels and was analyzed for different decoding techniques by the help of comparative computer simulations. Simulation results indicate that the proposed decoding algorithm can achieve better Bit Error Rate (BER) performances closer to SP algorithm with the preservation of the principal characteristics of the MS algorithm.

## Comparison between Different Decoding Algorithms For Low Density Parity Check

- **ID**: ieee:9019379
- **Type**: conference
- **Published**: 29-30 Apri
- **Authors**: Mahmood F. Mosleh, Fadhil S. Hasan, Ruaa M. Azeez
- **PDF**: https://ieeexplore.ieee.org/document/9019379
- **Abstract**: Forward error correction code with Low Density Parity Check (LDPC) gives substantial results very close to Shannon limit. This can be achieved when complexity and delay time is unlimited. Thus, it is significant to recognize the limitation of those parameters in the decoding of LDPC. In this research, a study of LDPC performance with three decoding algorithms namely; bit-flipping, log domain, and prob domain are presented. The first one is related to hard decision family while the last two types are the soft decision that follows the sum-product algorithm. A simulation model of a wireless communication system included LDPC are evaluated with the motioned three types of decoding using Matlab Package, version 2018a. The results show that the log domain and prob domain are outperforming the bit-flipping algorithm by a significant amount of Signal to Noise Ratio (SNR). Finally, optimum values of LDPC parameters are chosen according to the achieved results that will give better results are presented.

## Performance Analysis of Elastic MIMO-RF/FSO Communication Over Lutz Model with LDPC

- **ID**: ieee:8770187
- **Type**: conference
- **Published**: 27-28 Apri
- **Authors**: Sanaz Baradaran Rowhani, Alireza Ghaneizadeh, Iman Ahadi Akhlaghi
- **PDF**: https://ieeexplore.ieee.org/document/8770187
- **Abstract**: Elastic radio frequency (RF)/free space optical (FSO) system is a promising solution to access high reliability and quality of performance in satellite-ground communications. It is introduced as a reconfigurable system since RF and FSO links suffer from some unfavorable atmospheric conditions individually. Elastic RF/FSO system has considered RF as a back-up link while FSO stops working due to aforementioned destructive effects. This work has analyzed the performance of two kinds of channel coding schemes named low density parity check (LDPC) and space time block codes (STBC) the former is applied to provide coding gain and the latter to provide spatial diversity over Lutz model considered as a statistical model in RF communication. Finally, the bit error rate (BER) performance of coding schemes has been evaluated over Lutz model with Rayleigh and Rician fading distributions. Simulation results demonstrate a considerable BER reduction even in low signal to noise ratios particularly when FSO meets undesirable atmospheric effects.

## Modeling and Design of a DVB-S2X system

- **ID**: ieee:8727700
- **Type**: conference
- **Published**: 25-26 Apri
- **Authors**: Abdoul-Fattah Ben Ali Bachir, Madini Zhour, Mnijel Ahmed
- **PDF**: https://ieeexplore.ieee.org/document/8727700
- **Abstract**: The DVB-S standard is an application of DVB (Digital Video Broadcasting) to satellite communications. The standard has several versions to meet different requirements for each era. Each version has its specifications among which factor RO (Roll-Off) and techniques of modulation. The latest version is DVB-S2X which is an extension of DVB-S2. This paper emphasizes a comparison design of a DVB-S2/S2X system by using Matlab/Simulink software. This comparative study is essentially based of the RO (Roll Off) factor and the type of modulation. DVB-S2X uses very small values for the RO factor whose consequences are of gaining spectral space inside the carrier. It also works with the superior modulation techniques called APSK (Amplitude and Phase-Shift Keying). These new APSK modulation techniques used in DVB-S2X provide a higher capacity but require a high-level SNR (Signal to Noise Ratio).

## A Survey on Cognitive Radio Networks for Detecting Unwanted Access of Malicious Nodes

- **ID**: ieee:8741455
- **Type**: conference
- **Published**: 25-26 Apri
- **Authors**: Dinokumar Kongkham, M. Sundararajan
- **PDF**: https://ieeexplore.ieee.org/document/8741455
- **Abstract**: Spectrum sensing is an essential job used for cognitive radio. One note worthy test used for cognitive radio systems is the sampling rate blockage related through wide band range detecting. This article projects a novel wideband range detecting system utilizing multicoset testing and symmetrical coordinating interest calculation. Multicoset testing is a sub-Nyquist examining method that can be utilized to decrease the implementation multifaceted nature related with the Nyquist inspecting based wideband detecting strategies. Symmetrical coordinating interest is a ravenous interest calculation used to recoup the obscure ghastly help of compressive detected scanty signs. The proposed strategy not just diminishes the multifaceted nature related with Nyquist examining based frameworks yet additionally gives a solid recognition capacity even at low flag to-commotion proportions. When the obscure ghostly files are distinguished, the empty range is designated to the auxiliary clients. Since the empty range is constantly inclined to essential client impedance, the optional client utilizes the LDPC codes for dependable information transfers. Bit-error rates are also analyzed to find the system performance.

## Channel Coding and Low Latency HARQ for Industrial Wireless Sensor Networks

- **ID**: ieee:8734232
- **Type**: conference
- **Published**: 24-26 Apri
- **Authors**: Bashar Husain, Andreas Czylwik
- **PDF**: https://ieeexplore.ieee.org/document/8734232
- **Abstract**: Industrial wireless sensor networks (IWSN) begin to occupy wide areas in the industry for applications such as factory automation. To meet the strict latency and reliability requirements for (IWSN), channel coding is proposed to be used in the physical layer. To this aim, a comparison study is carried out in this paper among three different modern coding techniques, i.e. turbo, LDPC, and convolutional coding. The goal of this study is to define which coding technique better meets IWSN requirements. LDPC is shown to provide a good performance by means of latency and reliability. In addition, low latency HARQ based on error rate estimation is proposed in this paper. The proposed scheme utilizes few LDPC decoder iterations and can provide up to 5 dB gain compared to another scheme where the decoding process is completely skipped.

## Improved MS LDPC Decoder Based on Jacobian Logarithm

- **ID**: ieee:8834961
- **Type**: conference
- **Published**: 24-26 Apri
- **Authors**: Ruizhen Wu, Lin Wang, Tao Yuan +1
- **PDF**: https://ieeexplore.ieee.org/document/8834961
- **Abstract**: An improved MS LDPC decoder is proposed in this paper. The degradation factor of BP to MS is found and optimized based on Jacobian Logarithm and hardware working mode. An offset factor is added to improve the decoding accuracy rate and is optimized to two constants for different SNR environments thus only need an adder and a selector as hardware cost to implement it. The simulation is based on LDPC NR 3GPP 38.212 release and the comparison results showed the proposed improved MS LDPC decoder have a better BER and iteration time performance than other existing decoders in different SNR environments.

## Binary Multilevel Coding over Eisenstein Integers for MIMO Broadcast Transmission

- **ID**: ieee:8727219
- **Type**: conference
- **Published**: 24-26 Apri
- **Authors**: Sebastian Stern, Daniel Rohweder, Juergen Freudenberger +1
- **PDF**: https://ieeexplore.ieee.org/document/8727219
- **Abstract**: It is well known that signal constellations which are based on a hexagonal grid, so-called Eisenstein constellations, exhibit a performance gain over conventional QAM ones. This benefit is realized by a packing and shaping gain of the Eisenstein (hexagonal) integers in comparison to the Gaussian (complex) integers. Such constellations are especially relevant in transmission schemes that utilize lattice structures, e.g., in MIMO communications. However, for coded modulation, the straightforward approach is to combine Eisenstein constellations with ternary channel codes. In this paper, a multilevel-coding approach is proposed where encoding and multistage decoding can directly be performed with state-of-the-art binary channel codes. An associated mapping and a binary set partitioning are derived. The performance of the proposed approach is contrasted to classical multilevel coding over QAM constellations. To this end, both the single-user AWGN scenario and the (multiuser) MIMO broadcast scenario using lattice-reduction-aided preequalization are considered. Results obtained from numerical simulations with LDPC codes complement the theoretical aspects.

## Approximate Message Passing for Joint Activity Detection and Decoding in Non-orthogonal CDMA

- **ID**: ieee:8727194
- **Type**: conference
- **Published**: 24-26 Apri
- **Authors**: Stefan C. Birgmeier, Norbert Goertz
- **PDF**: https://ieeexplore.ieee.org/document/8727194
- **Abstract**: In Compressive Sensing, the knowledge of an unknown vector's statistical properties together with a small number of linear measurements makes it possible to reconstruct the vector with high accuracy in terms of minimum mean-squared error. A popular statistical property is sparsity of the unknown vector. The model can thus be applied to multi-user systems, where only a small number of users is active at a given time. In this paper, we show how the properties of the users channel code and approximate knowledge of the fraction of active users can be used to simultaneously detect user activity and the transmitted codeword, when the users code-symbols are transmitted by nonorthogonal spreading sequences. The main goal is to provide a unified framework (based on compressed-sensing techniques) in which to describe and solve the joint detection-and-decoding problem by a single computationally highly efficient algorithm.

## Design and Implementation of Parallel Branches for Concatenated BCH and LDPC Coding on FPGA

- **ID**: ieee:8734628
- **Type**: conference
- **Published**: 16-18 Apri
- **Authors**: Ahmed Mahdy, Mohamed Helmy, Mohamed Hassan
- **PDF**: https://ieeexplore.ieee.org/document/8734628
- **Abstract**: Recently, satellite services applications are of wide utilization as in radio and television broadcast, voice and data communication, and location services communication. Error correction codes are continuously designed to accomplish reliable communication with low Bit-Error-Rate (BER) in satellite communication link. Modern techniques are using concatenation of different codes, to achieve low BER. This paper presents an implementation for Bose-Chaudauri Hocquenghem (BCH) on FPGA. Also, it provides an implementation for low density parity check (LDPC) on FPGA. Finally, a design and implementation for multiple branches of BCH concatenated with LDPC on FPGA, where the encoder is designed such that two parallel BCH branches are concatenated with one LDPC, while the decoder design is four parallel BCH branches concatenated with one LDPC. This proposed design improves the link reliability and increases the throughput when compared with the serial concatenated coding systems, where the encoder throughput increased from 100 Mbps to 200 Mbps, and the decoder enhanced from 10.5 Mbps to 50 Mbps.

## Inspection of Error Performance and Interference Avoidance Technique for Cooperative Relay in Underlay D2D Networks

- **ID**: ieee:8734671
- **Type**: conference
- **Published**: 16-18 Apri
- **Authors**: Rna Ghallab, Mona Shokair, Ali Sakr +1
- **PDF**: https://ieeexplore.ieee.org/document/8734671
- **Abstract**: 5G wireless standard has significant participation for Device to Device (D2D) communication system, channel state estimation and cooperative relay techniques. This paper investigates the great role of the cohabitation of these technologies by proposing the electronic relay. This relay is a collection of collaborative techniques. The selection between them is accomplished automatically after inspecting the channel state information (CSI). In addition, interference avoidance techniques with the electronic relay are proposed to reduce the interference. A deeper construe of these techniques is illustrated. Also, the term of outage probability of both communication links is demonstrated. MATLAB simulator is used. The outage performance of proposed techniques is compared with the corresponding previous techniques. As illustrated in the simulation results. The SNR gain increases by 2.9 dB due to utilizing the interference avoidance. Moreover, the effect of increasing the D2D numbers on the system outage probability is introduced.

## Robust and Simple Log-Likelihood Approximation for Receiver Design

- **ID**: ieee:8886114
- **Type**: conference
- **Published**: 15-18 Apri
- **Authors**: Yasser Mestrah, Anne Savard, Alban Goupil +2
- **PDF**: https://ieeexplore.ieee.org/document/8886114
- **Abstract**: In impulsive noise, the inputs of the belief propagation decoder can be complex to compute or even impossible when the noise distribution is not known. We propose a simple approximation of the log-likelihood ratio that maps the channel output to the input of the error correcting decoder, for instance, LDPC decoders. This approximation is designed for additive impulsive noise channels, nevertheless, it is not computationally demanding and easy to be implemented. It requires the estimation of three parameters and we propose an efficient way to do it. Moreover, in terms of performance, our solution is barely discernible from the optimal receiver which is computationally prohibitive.

## Achievability Bounds for T-Fold Irregular Repetition Slotted ALOHA Scheme in the Gaussian MAC

- **ID**: ieee:8885472
- **Type**: conference
- **Published**: 15-18 Apri
- **Authors**: Anton Glebov, Nikolay Matveev, Kirill Andreev +2
- **PDF**: https://ieeexplore.ieee.org/document/8885472
- **Abstract**: We address the problem of uncoordinated massive random-access in the Gaussian multiple access channel (MAC). The performance of low-complexity T-fold irregular repetition slotted ALOHA (IRSA) scheme is investigated and achievability bounds are derived. The main difference of this scheme in comparison to IRSA is as follows: any collisions of order up to T can be resolved with some probability of error introduced by noise. In order to optimize the parameters of the scheme we combine the density evolution method (DE) proposed by G. Liva and a finite length random coding bound for the Gaussian MAC proposed by Y. Polyanskiy. As energy efficiency is of critical importance for massive machine-type communication (mMTC), then our main goal is to minimize the energy-per-bit required to achieve the target packet loss ratio (PLR). We consider two scenarios: (a) the number of active users is fixed; (b) the number of active users is a Poisson random variable.

## Construction and Decoding of Product Codes with Non-Systematic Polar Codes

- **ID**: ieee:8886100
- **Type**: conference
- **Published**: 15-18 Apri
- **Authors**: Valerio Bioglio, Carlo Condo, Ingmar Land
- **PDF**: https://ieeexplore.ieee.org/document/8886100
- **Abstract**: Product codes are widespread in optical communications, thanks to their high throughput and good error-correction performance. Systematic polar codes have been recently considered as component codes for product codes. In this paper, we present a novel construction for product polar codes based on non-systematic polar codes. We prove that the resulting product code is actually a polar code, having a frozen set that is dependent on the frozen sets of the component polar codes. We propose a low-complexity decoding algorithm exploiting the dual nature of the constructed code. Performance analysis and simulations show high decoding speed, that allows to construct long codes while maintaining low decoding latency. The resulting high throughput and good error-correction performance are appealing for optical communication systems and other systems where high throughput and low latency are required.

## Implementation of Network Coding with Recoding for Unequal-sized and Header Compressed Traffic

- **ID**: ieee:8885446
- **Type**: conference
- **Published**: 15-18 Apri
- **Authors**: Maroua Taghouti, Máté Tömösközi, Malte Howeler +4
- **PDF**: https://ieeexplore.ieee.org/document/8885446
- **Abstract**: Coding techniques that are employed to resolve packet losses on wireless channels, such as Random Linear Network Coding (RLNC), market themselves with the advantage of requiring less signalling, as well as, retransmissions of missing packets to compensate for losses on unreliable links. However, as packet sizes of IP-based protocols can be distributed irregularly over the available maximum frame size and can vary considerably packet-by-packet, the current implementations of RLNC suffer from shifting header and/or payload lengths and lack a suitable way of compensation. The simplest solution adopted by most RLNC approaches is to pad the unequal packets with zeros to the maximum packet size, thus creating an unnecessary transmission overhead of 100 % or more. This paper presents a practical implementation of the new progressive shortening based RLNC for the first time. This scheme utilizes fixed-sized regions inside the packets to resolve the zero-padding overhead and generates unequal-sized coded packets. Furthermore, it introduces a recoding feature for this scheme, which is another advantage of RLNC over other coding techniques, and breaks with the point-to-point topology considered in previous works. Moreover, we combine this novel macro-symbol based coding scheme with Robust Header Compression version 2 (RoHCv2) to show the gain over traditional implementation of RLNC in a real-life application where varying packet lengths dominate during transmissions. Our implementations results, using the KODO network coding library, show that the encoding throughput is as good as the established RLNC methods, and the payload delivery efficiency can be enhanced by up to 20 %.
