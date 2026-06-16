# IEEE Xplore — 2014-01


## Improved Iterative Hard- and Soft-Reliability Based Majority-Logic Decoding Algorithms for Non-Binary Low-Density Parity-Check Codes

- **ID**: ieee:6880860
- **Type**: journal
- **Published**: Oct.15, 20
- **Authors**: Chenrong Xiong, Zhiyuan Yan
- **PDF**: https://ieeexplore.ieee.org/document/6880860
- **Abstract**: Non-binary low-density parity-check (LDPC) codes have some advantages over their binary counterparts, but unfortunately their decoding complexity is a significant challenge. The iterative hard- and soft-reliability based majority-logic decoding algorithms are attractive for nonbinary LDPC codes, since they involve only finite field additions and multiplications as well as integer operations and, hence, have significantly lower complexity than other algorithms. In this paper, we propose two improvements to the majority-logic decoding algorithms. Instead of the accumulation of reliability information in the existing majority-logic decoding algorithms, our first improvement is a new reliability information update. The new update not only results in better error performance and fewer iterations on average, but also further reduces computational complexity. Since existing majority-logic decoding algorithms tend to have a high error floor for codes whose parity check matrices have low column weights, our second improvement is a reselection scheme, which leads to much lower error floors, at the expense of more finite field operations and integer operations, by identifying periodic points, reselecting intermediate hard decisions, and changing reliability information.

## A Low Complexity-High Throughput QC-LDPC Encoder

- **ID**: ieee:6781047
- **Type**: journal
- **Published**: May15, 201
- **Authors**: Ahmed Mahdi, Vassilis Paliouras
- **PDF**: https://ieeexplore.ieee.org/document/6781047
- **Abstract**: This paper introduces hardware architectures for encoding Quasi-Cyclic Low-Density Parity Check (QC-LDPC) codes. The proposed encoders are based on appropriate factorization and subsequent compression of involved matrices by means of a novel technique, which exploits features of recursively-constructed QC-LDPC codes. The particular approach derives to linear encoding time complexity and requires a constant number of clock cycles for the computation of parity bits for all the constructed codes of various lengths that stem from a common base matrix. The proposed architectures are flexible, as they are parameterized and can support multiple code rates and codes of different lengths simply by appropriate initialization of memories and determination of data bus widths. Implementation results show that the proposed encoding technique is more efficient for some LDPC codes than previously proposed solutions. Both serial and parallel architectures are proposed. Hardware instantiations of the proposed serial encoders demonstrate high throughput with low area complexity for code words of many thousand bits, achieving area reduction compared to prior art. Furthermore, parallelization is shown to efficiently support multi-Gbps solutions at the cost of moderate area increase. The proposed encoders are shown to outperform the current state-of-the-art in terms of throughput-area-ratio and area-time complexity by 10 to up to 80 times for codes of comparable error-correction strength.

## A Flexible NISC-Based LDPC Decoder

- **ID**: ieee:6766729
- **Type**: journal
- **Published**: May15, 201
- **Authors**: Bertrand Le Gal, Christophe Jego, Camille Leroux
- **PDF**: https://ieeexplore.ieee.org/document/6766729
- **Abstract**: Low density parity-check (LDPC) codes, are widely used for error correction in digital communication systems. Their inclusion in communication standards requires to define decoders able to support efficiently a set of codes with different code length, code rates or code structures. In addition to this high flexibility, these decoders still have to achieve high throughputs in order to comply with standards requirements. In this paper, we propose to address the problem of designing generic and efficient LDPC decoders by using a nonsymmetric NISC-based architecture that performs layered decoding. NISC architectures provide flexibility with a limited loss in hardware efficiency. In addition, an automated design flow is used to efficiently assign computations to the processing units (PU) and to map data to the memory units (MU). Unlike previous works, the NISC decoder can include a number of PUs that is different than the number of MUs. This nonsymmetric characteristic provides a higher degree of freedom during the computation/data assignment phase of the design flow. This whole design framework automatically generates an LDPC decoder able to support any set of predetermined LDPC codes regardless of their parameters. The automated nature of the design framework enables to easily explore the design space for a given set of codes. Compared to state of the art LDPC decoders, the automatically generated decoders achieve higher hardware efficiency even for the challenging-to-implement unstructured LDPC codes.

## Coded-Aided Phase Tracking for Coherent Fiber Channels

- **ID**: ieee:6690206
- **Type**: journal
- **Published**: March15, 2
- **Authors**: Chunpo Pan, Frank R. Kschischang
- **PDF**: https://ieeexplore.ieee.org/document/6690206
- **Abstract**: In coherent optical systems laser phase noise can interact with digital equalization to cause equalization-enhanced impairments, which are a major obstacle for applying higher order modulation formats in coherent optical systems with digital chromatic dispersion compensation. In this paper a code-aided expectation maximization method to track phase noise in such systems is presented. A common measure of laser phase noise is the linewidth. It is shown that with ~ 11% redundancy, the laser linewidth tolerance for 975 km transmission distance can be increased by 50%, or the system reach for a laser linewidth of 5 MHz can be doubled. A phase-noise-robust 16-point 4-4-4-4 ring constellation was found to have better performance compared to 16QAM and a 2-6-8 ring constellations. Performance can be further improved with a lower code rate and fewer pilot symbols. It is also shown that algorithmic complexity can be reduced without significant reduction in the performance by reducing iterations and using low complexity codes.

## Distributed Source-Channel Coding Based on Real-Field BCH Codes

- **ID**: ieee:6712144
- **Type**: journal
- **Published**: March1, 20
- **Authors**: Mojtaba Vaezi, Fabrice Labeau
- **PDF**: https://ieeexplore.ieee.org/document/6712144
- **Abstract**: We use real-number codes to compress statistically dependent sources and establish a new framework for distributed lossy source coding in which we compress sources before, rather than after, quantization. This change in the order of binning and quantization blocks makes it possible to model the correlation between continuous-valued sources more realistically and compensate for the quantization error partially. We then focus on the asymmetric case, i.e., lossy source coding with side information at the decoder. The encoding and decoding procedures are described in detail for a class of real-number codes called discrete Fourier transform (DFT) codes, both for the syndrome- and parity-based approaches. We leverage subspace-based decoding to improve the decoding and by extending it we are able to perform distributed source coding in a rate-adaptive fashion to further improve the decoding performance when the statistical dependency between sources is unknown. We also extend the parity-based approach to the case where the transmission channel is noisy and thus we perform distributed joint source-channel coding in this context. The proposed system is well suited for low-delay communications, as the mean-squared reconstruction error (MSE) is shown to be reasonably low for very short block length.

## Subcarrier Reliability Aware Soft-Decision LDPC Code in CO-OFDM Systems

- **ID**: ieee:6778012
- **Type**: journal
- **Published**: June1, 201
- **Authors**: Di Che, Hamid Khodakarami, An Li +3
- **PDF**: https://ieeexplore.ieee.org/document/6778012
- **Abstract**: We propose a subcarrier reliability aware low-density parity-check (SRA-LDPC) soft-decision coding scheme for coherent optical orthogonal frequency division multiplexing (CO-OFDM) systems. The SRA-LDPC code takes consideration of varying signal-to-noise ratio performance among different OFDM subcarriers. At the SRA-LDPC encoder, flexible forward error correction is applied to different ranges of subcarriers. At the decoder, the algorithm keeps track of noise variance of each subcarrier and utilizes such variance for decoding. Our proposed algorithm is substantiated in a 120-Gb/s CO-OFDM system where near-dc noise originated from the local oscillator is detrimental to the system performance. The experimental results show that the SRA-LDPC code is effective in combating near-dc noise and enhancing the receiver sensitivity.

## Lowering the Error Floor of LDPC Codes Using Multi-Step Quantization

- **ID**: ieee:6676774
- **Type**: journal
- **Published**: January 20
- **Authors**: Sina Tolouei, Amir H. Banihashemi
- **PDF**: https://ieeexplore.ieee.org/document/6676774
- **Abstract**: A multi-step scheme is proposed for the input quantization of message-passing decoders for low-density parity-check (LDPC) codes. The proposed scheme, which is applicable to both regular and irregular codes, lowers the error floor significantly at the cost of small increase in complexity, memory and latency.

## Quantized Iterative Message Passing Decoders with Low Error Floor for LDPC Codes

- **ID**: ieee:6685976
- **Type**: journal
- **Published**: January 20
- **Authors**: Xiaojie Zhang, Paul H. Siegel
- **PDF**: https://ieeexplore.ieee.org/document/6685976
- **Abstract**: The error floor phenomenon observed with LDPC codes and their graph-based, iterative, message-passing (MP) decoders is commonly attributed to the existence of error-prone substructures - variously referred to as near-codewords, trapping sets, absorbing sets, or pseudocodewords - in a Tanner graph representation of the code. Many approaches have been proposed to lower the error floor by designing new LDPC codes with fewer such substructures or by modifying the decoding algorithm. Using a theoretical analysis of iterative MP decoding in an idealized trapping set scenario, we show that a contributor to the error floors observed in the literature may be the imprecise implementation of decoding algorithms and, in particular, the message quantization rules used. We then propose a new quantization method - (q+1)-bit quasi-uniform quantization - that efficiently increases the dynamic range of messages, thereby overcoming a limitation of conventional quantization schemes. Finally, we use the quasi-uniform quantizer to decode several LDPC codes that suffer from high error floors with traditional fixed-point decoder implementations. The performance simulation results provide evidence that the proposed quantization scheme can, for a wide variety of codes, significantly lower error floors with minimal increase in decoder complexity.

## Gallager B LDPC Decoder with Transient and Permanent Errors

- **ID**: ieee:6679370
- **Type**: journal
- **Published**: January 20
- **Authors**: Chu-Hsiang Huang, Yao Li, Lara Dolecek
- **PDF**: https://ieeexplore.ieee.org/document/6679370
- **Abstract**: This paper studies the performance of a noisy Gallager B decoder for regular LDPC codes. We assume that the noisy decoder is subject to both transient processor errors and permanent memory errors. We permit different error rates at different functional components. In addition, for the sake of generality, we allow asymmetry in the permanent error rates of component outputs, and thus we model error propagation in the decoder via a suitable asymmetric channel. We then develop a density evolution-type analysis on this asymmetric channel. The recursive expression for the bit error probability is derived as a function of the code parameters (node degrees), codeword weight, transmission error rate, and the error rates of the permanent and the transient errors. Based on this analysis, we then derive the residual error of the Gallager B decoder for the regime where the transmission error rate and the processing error rates are small. In this regime, we further observe that the residual error rate can be well approximated by a suitable combination of the transient error rate and the permanent error rate at variable nodes, provided that the check node degree is large enough. Based on this insight, we then propose and analyze a scheme for detecting permanent errors and correcting detected residual errors. The scheme exploits the parity check equations of the code and reuses the existing hardware to locate permanent errors in memory blocks. Performance analysis and simulation results show that, with high probability, the detection scheme discovers correct locations of permanent memory errors, while, with low probability, it mislabels the functional memory as being defective. The proposed error detection-and-correction scheme can be implemented in-circuit and is useful in combating failures arising from aging.

## Source Coding with Side Information at the Decoder and Uncertain Knowledge of the Correlation

- **ID**: ieee:6685982
- **Type**: journal
- **Published**: January 20
- **Authors**: Elsa Dupraz, Aline Roumy, Michel Kieffer
- **PDF**: https://ieeexplore.ieee.org/document/6685982
- **Abstract**: This paper considers the problem of lossless source coding with side information at the decoder, when the correlation model between the source and the side information is uncertain. Four parametrized models representing the correlation between the source and the side information are introduced. The uncertainty on the correlation appears through the lack of knowledge on the value of the parameters. For each model, we propose a practical coding scheme based on non-binary Low Density Parity Check Codes and able to deal with the parameter uncertainty. At the encoder, the choice of the coding rate results from an information theoretical analysis. Then we propose decoding algorithms that jointly estimate the source vector and the parameters. As the proposed decoder is based on the Expectation-Maximization algorithm, which is very sensitive to initialization, we also propose a method to produce first a coarse estimate of the parameters.

## Improved Binary DAC Codec with Spectrum for Equiprobable Sources

- **ID**: ieee:6679369
- **Type**: journal
- **Published**: January 20
- **Authors**: Yong Fang, Liang Chen
- **PDF**: https://ieeexplore.ieee.org/document/6679369
- **Abstract**: Slepian-Wolf coding (SWC) can be effectively implemented by distributed arithmetic coding (DAC) codes. A theoretical tool named spectrum has been developed to analyze the complexity of the full-search binary DAC (BDAC) decoder for equiprobable sources. Following this work, this paper aims at improving the coding efficiency of BDAC codes. To achieve this goal, this paper analyzes how BDAC codes partition source space into codebooks and links codebook cardinalities with the initial spectrum. Further, by exploiting the final spectrum, this paper proves that the decoding error probability of BDAC codes will not tend to zero as code length goes to infinity, even at rates greater than the Slepian-Wolf limit. On the basis of theoretical analyses, two techniques are proposed to reduce the decoding error probability of BDAC codes, i.e., the permutation technique, which removes "near" (in the sense of Hamming distance) codewords in each codebook, and the weighted branching technique, which reduces the mis-pruning risk of proper paths during the decoding. The effectiveness of both techniques is well verified by experimental results.

## Minimum-Variance Importance-Sampling Bernoulli Estimator for Fast Simulation of Linear Block Codes over Binary Symmetric Channels

- **ID**: ieee:6678682
- **Type**: journal
- **Published**: January 20
- **Authors**: Gianmarco Romano, Domenico Ciuonzo
- **PDF**: https://ieeexplore.ieee.org/document/6678682
- **Abstract**: In this paper the choice of the Bernoulli distribution as biased distribution for importance sampling (IS) Monte-Carlo (MC) simulation of linear block codes over binary symmetric channels (BSCs) is studied. Based on the analytical derivation of the optimal IS Bernoulli distribution, with explicit calculation of the variance of the corresponding IS estimator, two novel algorithms for fast-simulation of linear block codes are proposed. For sufficiently high signal-to-noise ratios (SNRs) one of the proposed algorithm is SNR-invariant, i.e. the IS estimator does not depend on the cross-over probability of the channel. Also, the proposed algorithms are shown to be suitable for the estimation of the error-correcting capability of the code and the decoder. Finally, the effectiveness of the algorithms is confirmed through simulation results in comparison to standard Monte Carlo method.

## Rate-Adaptive Coded Modulation for Fiber-Optic Communications

- **ID**: ieee:6634233
- **Type**: journal
- **Published**: Jan.15, 20
- **Authors**: Lotfollah Beygi, Erik Agrell, Joseph M. Kahn +1
- **PDF**: https://ieeexplore.ieee.org/document/6634233
- **Abstract**: Rate-adaptive optical transceivers can play an important role in exploiting the available resources in dynamic optical networks, in which different links yield different signal qualities. We study rate-adaptive joint coding and modulation, often called coded modulation (CM), addressing non-dispersion-managed (non-DM) links, exploiting recent advances in channel modeling of these links. We introduce a four-dimensional CM scheme, which shows a better tradeoff between digital signal processing complexity and transparent reach than existing methods. We construct a rate-adaptive CM scheme combining a single low-density parity-check code with a family of three signal constellations and using probabilistic signal shaping. We evaluate the performance of the proposed CM scheme for single-channel transmission through long-haul non-DM fiber-optic systems with electronic chromatic-dispersion compensation. The numerical results demonstrate improvement of spectral efficiency over a wide range of transparent reaches, an improvement over 1 dB compared to existing methods.

## Turbo Equalization for Digital Coherent Receivers

- **ID**: ieee:6671388
- **Type**: journal
- **Published**: Jan.15, 20
- **Authors**: Valeria Arlunno, Antonio Caballero, Robert Borkowski +3
- **PDF**: https://ieeexplore.ieee.org/document/6671388
- **Abstract**: High order modulation formats allow to reach higher spectral efficiency and data rate. However, their practical implementation is limited by their reduced tolerance to noise and to the optical signal power that can be launched into the fiber without generating excessive nonlinear signal distortions. In this paper, it is demonstrated that Turbo Equalization routines can be used to mitigate performance degradations stemming from optical fiber propagation effects both in optical fiber dispersion managed and unmanaged coherent detection links. The effectiveness of this solution is analyzed both numerically and experimentally for different transmission systems.

## An LDPC Decoder With Time-Domain Analog and Digital Mixed-Signal Processing

- **ID**: ieee:6630119
- **Type**: journal
- **Published**: Jan. 2014
- **Authors**: Daisuke Miyashita, Ryo Yamaki, Kazunori Hashiyoshi +4
- **PDF**: https://ieeexplore.ieee.org/document/6630119
- **Abstract**: Time-domain analog and digital mixed-signal processing (TD-AMS) is presented. Analog computation is more energy- and area-efficient at the cost of its limited accuracy, whereas digital computation is more versatile and derives greater benefits from technology scaling. Besides, design automation tools for digital circuits are much more sophisticated than those for analog circuits. TD-AMS exploits both advantages, and is a solution better suited to implementing a system on chip including functions for which high computational accuracy is not required, such as error correction, image processing, and machine learning. As an example, a low-density parity-check (LDPC) code decoder with the technique is implemented in 65 nm CMOS and achieves the best reported efficiencies of 10.4 pJ/bit and 6.1 Gbps/mm2.

## Correlation Noise-Based Unequal Error Protected Rate-Adaptive Codes for Distributed Video Coding

- **ID**: ieee:6560406
- **Type**: journal
- **Published**: Jan. 2014
- **Authors**: Jeffrey J. Micallef, Reuben A. Farrugia, Carl James Debono
- **PDF**: https://ieeexplore.ieee.org/document/6560406
- **Abstract**: Distributed video coding (DVC) is a paradigm that can shift most of the computational intensive tasks from the encoder to the decoder. This allows for the design of low complexity encoders that can be deployed in devices equipped with limited resources. However, the compression efficiency obtained using practical DVC codecs are still distant from those of traditional predictive video coding schemes such as H.264/AVC. One of the limitations of the existing DVC architectures is that they consider the correlation noise to be randomly distributed across the whole video frame. This paper shows that the Syner–Ziv (WZ) values that are closer to the endpoints of the quantization intervals have a higher probability of producing incorrect side information (SI) predictions. Thus, through this knowledge, rate-adaptive low-density parity-check accumulate codes that provide a higher level of protection to the unreliable SI bits can be exploited. Experimental results show that the proposed scheme can reduce the WZ bit-rate up to 13% relative to the state-of-the-art DISCOVER architecture when considering interpolation techniques and by up to 0.9 dB for extrapolation techniques.

## EXIT-Based Side Information Refinement in Wyner–Ziv Video Coding

- **ID**: ieee:6574264
- **Type**: journal
- **Published**: Jan. 2014
- **Authors**: Wen Ji, Pascal Frossard, Yiqiang Chen
- **PDF**: https://ieeexplore.ieee.org/document/6574264
- **Abstract**: The accuracy of the side information (SI) is critical in the performance of distributed video coding algorithms. The SI is typically built at a decoder based on the reconstructed data and on channel coding parity bits transmitted by the encoder. The optimal encoding rate is generally difficult to compute precisely due to the dynamics of video content with varying correlation. Effective methods for the refinement of imprecise SI are therefore important for improved decoding quality. In this paper, we propose to exploit the intrinsic property of channel coding algorithms in Wyner-Ziv video coding. The SI is refined via both the information-plane and the parity-plane bits, which rapidly increases the accuracy of refined SI. We use extrinsic information transfer chart analysis in order to estimate the variations of the mutual information in the iterative decoding. In particular, we characterize mutual information variations for punctured regular and irregular rate-compatible low-density parity-check codes. Tracking the mutual information changes permits to decrease the coding rate of the information and parity bitstreams, while preserving the decoding quality. Simulation results confirm that our method improves on the decoding quality of recent distributed video coding algorithms, especially for high-motion sequences or at high-coding rate regimes.

## Variable Length Lossy Coding Using an LDPC Code

- **ID**: ieee:6651840
- **Type**: journal
- **Published**: Jan. 2014
- **Authors**: Junya Honda, Hirosuke Yamamoto
- **PDF**: https://ieeexplore.ieee.org/document/6651840
- **Abstract**: In this paper, a new variable length coding scheme using a low density parity check (LDPC) code is proposed for the lossy compression of general i.i.d. finite sources. It is proved that the proposed scheme achieves the rate-distortion function asymptotically for an LDPC ensemble. For our setting, Miyake-Muramatsu already proposed an asymptotically optimal LDPC coding scheme. In their scheme, a source sequence is first vector-quantized using an LDPC matrix and then it is compressed losslessly by fixed length coding with another LDPC matrix. However, it is not shown whether their scheme can attain good performance practically. This is mainly because of the difficulty of lossless coding by a fixed length code. In the proposed scheme, the lossless compression is performed by arithmetic coding instead of the fixed length code. Combined with vector-quantization using the reinforced belief propagation, the proposed scheme attains performance near the rate-distortion function practically with time complexity roughly equal to ${\bf O}(n\log n)$ for length $n$ source sequences.

## On Classical and Quantum MDS-Convolutional BCH Codes

- **ID**: ieee:6649974
- **Type**: journal
- **Published**: Jan. 2014
- **Authors**: Giuliano Gadioli La Guardia
- **PDF**: https://ieeexplore.ieee.org/document/6649974
- **Abstract**: Several new families of multi-memory classical convolutional Bose-Chaudhuri-Hocquenghem codes as well as families of unit-memory quantum convolutional codes are constructed in this paper. Our unit-memory classical and quantum convolutional codes are optimal in the sense that they attain the classical (quantum) generalized Singleton bound. The constructions presented in this paper are performed algebraically and not by computational search.

## On Decoding Irregular Tanner Codes With Local-Optimality Guarantees

- **ID**: ieee:6626647
- **Type**: journal
- **Published**: Jan. 2014
- **Authors**: Nissim Halabi, Guy Even
- **PDF**: https://ieeexplore.ieee.org/document/6626647
- **Abstract**: We consider decoding of binary linear Tanner codes using message-passing iterative decoding and linear-programming (LP) decoding in memoryless binary-input output-symmetric (MBIOS) channels. We present new certificates that are based on a combinatorial characterization for the local optimality of a codeword in irregular Tanner codes with respect to any MBIOS channel. This characterization is a generalization of (Arora , Proc. ACM Symp. Theory of Computing, 2009) and (Vontobel, Proc. Inf. Theory and Appl. Workshop, 2010) and is based on a conical combination of normalized weighted subtrees in the computation trees of the Tanner graph. These subtrees may have any finite height h (even equal or greater than half of the girth of the Tanner graph). In addition, the degrees of local-code nodes in these subtrees are not restricted to two (i.e., these subtrees are not restricted to skinny trees). We prove that local optimality in this new characterization implies maximum-likelihood (ML) optimality and LP optimality, and show that a certificate can be computed efficiently. We also present a new message-passing iterative decoding algorithm, called normalized weighted min-sum (NWMS). NWMS decoding is a belief-propagation (BP) type algorithm that applies to any irregular binary Tanner code with single parity-check local codes (e.g., low-density and high-density parity-check codes). We prove that if a locally optimal codeword with respect to height parameter h exists (whereby notably h is not limited by the girth of the Tanner graph), then NWMS decoding finds this codeword in h iterations. The decoding guarantee of the NWMS decoding algorithm applies whenever there exists a locally optimal codeword. Because local optimality of a codeword implies that it is the unique ML codeword, the decoding guarantee also provides an ML certificate for this codeword. Finally, we apply the new local-optimality characterization to regular Tanner codes, and prove lower bounds on the noise thresholds of LP decoding in MBIOS channels. When the noise is below these lower bounds, the probability that LP decoding fails to decode the transmitted codeword decays doubly exponentially in the girth of the Tanner graph.

## Path-Congestion-Aware Adaptive Routing With a Contention Prediction Scheme for Network-on-Chip Systems

- **ID**: ieee:6685943
- **Type**: journal
- **Published**: Jan. 2014
- **Authors**: En-Jui Chang, Hsien-Kai Hsin, Shu-Yen Lin +1
- **PDF**: https://ieeexplore.ieee.org/document/6685943
- **Abstract**: Network-on-chip systems can achieve higher performance than bus systems for chip multiprocessor systems. However, as the complexity of the network increases, the channel and switch congestion problems become major performance bottlenecks. An effective adaptive routing algorithm can help minimize path congestion through load balancing. However, conventional adaptive routing schemes only use channel-based information to detect the congestion status. Due to the lack of switch-based information, channel-based information is difficult to reveal the real congestion status along the routing path. Therefore, in this paper, we remodel the path congestion information to show hidden spatial congestion information and improve the effectiveness of routing path selection. We propose a path-congestion-aware adaptive routing (PCAR) scheme based on the following techniques: 1) a path-congestion-aware selection strategy that simultaneously considers switch congestion and channel congestion, and 2) a contention prediction technique that uses the rate of change in the buffer level to predict possible switch contention. The experimental results show that the proposed PCAR scheme can achieve a high saturation throughput with an improvement of 15.4%-48.7% compared to existing routing schemes. The proposed PCAR method also includes a VLSI architecture, which has higher area efficiency with an improvement of 16%-35.7% compared with the other router designs.

## Detection-Decoding on BPMR Channels With Written-In Error Correction and ITI Mitigation

- **ID**: ieee:6600835
- **Type**: journal
- **Published**: Jan. 2014
- **Authors**: Tong Wu, Marc A. Armand, J. R. Cruz
- **PDF**: https://ieeexplore.ieee.org/document/6600835
- **Abstract**: Written-in errors and inter-track interference (ITI) are recognized as key and unique performance-limiting factors in bit-patterned media recording (BPMR). Hence, in this paper, we consider data recovery on a BPMR channel model consisting of a write channel producing data-dependent written-in errors followed by a partial response read channel with the addition of ITI. The Davey-MacKay (DM) serial concatenated coding scheme is employed to handle the written-in errors while multi-track (MT) detection and 2D-equalization are used to mitigate the inter-symbol interference (ISI) and ITI. Three detection-inner-decoding schemes are proposed to work with an outer decoder to recover the data on the BPMR channel, namely the BCJR-binary-input-inner-decoder (BCJR-BIID) algorithm, the joint detection-inner-decoder (JDD) algorithm and the BCJR-soft-input-inner-decoder (BCJR-SIID) algorithm. Media configurations leading to areal densities of 2.64 Tb/in2 and 4 Tb/in2 with comparable ISI but significantly higher ITI in the latter case are considered. Computer simulations show that at low to moderate (resp., high) signal-to-noise ratios (SNRs), BCJR-SIID (resp., BCJR-BIID) provides good performance-complexity trade-offs. It is also shown that increasing the areal density from 2.64 Tb/in2 to 4 Tb/in2 while the written-in error rates remain fixed, does not significantly affect error performance on the BPMR channel. Rather, it is the burst errors preceding and following an insertion or deletion that has a significant impact on performance.

## Terabit/s Nyquist Superchannels in High Capacity Fiber Field Trials Using DP-16QAM and DP-8QAM Modulation Formats

- **ID**: ieee:6595033
- **Type**: journal
- **Published**: Feb.15, 20
- **Authors**: Ming-Fang Huang, Akihiro Tanaka, Ezra Ip +12
- **PDF**: https://ieeexplore.ieee.org/document/6595033
- **Abstract**: We report the results of two field trials aimed at achieving high fiber capacity over regional and long-haul distances. In the first trial, 41 superchannels with digital Nyquist pulse-shaping were generated and tightly packed to fill up both $C$-band and $L$-band. Each subcarrier was modulated with 24.8-Gbaud dual-polarization 16 quadrature amplitude modulation (DP-16QAM) data. The signal carrying net 54.2 Tb/s data was transmitted over 634 km of dispersion uncompensated field-installed standard single mode fiber with the aid of hybrid EDFA and Raman amplification and digital coherent detection. In the second trial for long-haul distances, we extended the transmission distance over 1,822 km. This increase in reach was achieved by reducing the net total capacity to 40.5 Tb/s and modulating the signals with dual-polarization 8 quadrature amplitude modulation (DP-8QAM) Nyquist carrier modulation. A novel rate-adaptive low-density parity-check coding was employed, so that the transmitted channels can exhibit different code rates, adapted by the concatenation of hard-decision and soft-decision forward error correcting codes for enhancing error-correction capability. To the best of our knowledge, we achieved the highest field trial capacity to date at 54.2 Tb/s in regional distances. Furthermore, in long-haul applications, the reported capacity × distance product of 73.79 Pb/s·km is the highest to date.

## High-Throughput Energy-Efficient LDPC Decoders Using Differential Binary Message Passing

- **ID**: ieee:6675862
- **Type**: journal
- **Published**: Feb.1, 201
- **Authors**: Kevin Cushon, Saied Hemati, Camille Leroux +2
- **PDF**: https://ieeexplore.ieee.org/document/6675862
- **Abstract**: In this paper, we present energy-efficient architectures for decoders of low-density parity check (LDPC) codes using the differential decoding with binary message passing (DD-BMP) algorithm and its modified variant (MDD-BMP). We also propose an improved differential binary (IDB) decoding algorithm. These algorithms offer significant intrinsic advantages in the energy domain: simple computations, low interconnect complexity, and very high throughput, while achieving error correction performance up to within 0.25 dB of the offset min-sum algorithm. We report on fully parallel decoder implementations of (273, 191), (1023, 781), and (4095, 3367) finite geometry-based LDPC codes in 65 nm CMOS. Using the MDD-BMP algorithm, these decoders achieve respective areas of 0.28 mm2, 1.38 mm2, and 15.37 mm2, average throughputs of 37 Gbps, 75 Gbps, and 141 Gbps, and energy efficiencies of 4.9 pJ/bit, 13.2 pJ/bit, and 37.9 pJ/bit with a 1.0 V supply voltage in post-layout simulations. At a reduced supply voltage of 0.8 V, these decoders achieve respective throughputs of 26 Gbps, 54 Gbps, and 94 Gbps, and energy efficiencies of 3.1 pJ/bit, 8.2 pJ/bit, and 23.5 pJ/bit. We also report on a fully parallel implementation of IDB for the (2048, 1723) LDPC code specified in the IEEE 802.3an (10GBASE-T) standard. This decoder achieves an area of 1.44 mm2, average throughput of 172 Gbps, and an energy efficiency of 2.8 pJ/bit with a 1.0 V supply voltage; at 0.8 V, it achieves throughput of 116 Gbps and energy efficiency of 1.7 pJ/bit.

## Novel Blind Identification of LDPC Codes Using Average LLR of Syndrome a Posteriori Probability

- **ID**: ieee:6678305
- **Type**: journal
- **Published**: Feb.1, 201
- **Authors**: Tian Xia, Hsiao-Chun Wu
- **PDF**: https://ieeexplore.ieee.org/document/6678305
- **Abstract**: Blind signal processing methods have been very popular recently since they can play crucial roles in the prevalent cognitive radio research. Blind encoder identification has drawn research interest lately. In this paper, we would like to tackle the blind identification of binary low-density parity-check (LDPC) codes for binary phase-shift keying (BPSK) signals. We propose a novel blind identification system which consists of three components, namely expectation-maximization (EM) estimator for signal amplitude and noise variance, log-likelihood ratio (LLR) estimator for syndrome a posteriori probabilities, and maximum average LLR detector. Monte Carlo simulation results demonstrate that our proposed blind LDPC encoder identification scheme is very promising even for low signal-to-noise ratio conditions.

## VLSI Implementation of a Non-Binary Decoder Based on the Analog Digital Belief Propagation

- **ID**: ieee:6832658
- **Type**: journal
- **Published**: Aug.1, 201
- **Authors**: Muhammad Awais, Guido Masera, Maurizio Martina +1
- **PDF**: https://ieeexplore.ieee.org/document/6832658
- **Abstract**: This work presents the VLSI hardware implementation of a novel Belief Propagation (BP) algorithm introduced in [G. Montorsi, “Analog digital belief propagation,” IEEE Commun. Lett., vol. 16, no. 7, pp. 1106-1109, 2012] and named as Analog Digital Belief Propagation (ADBP). The ADBP algorithm works on factor graphs over linear models and uses messages in the form of Gaussian like probability distributions by tracking their parameters. In particular, ADBP can deal with system variables that are discrete and/or wrapped. A variant of ADBP can then be applied for the iterative decoding of a particular class of non binary codes and yields decoders with complexity independent of alphabet size M, thus allowing to construct efficient decoders for digital transmission systems with unbounded spectral efficiency. In this work, we propose some simplifications to the updating rules for ADBP algorithm that are suitable for hardware implementation. In addition, we analyze the effect of finite precision on the decoding performance of the algorithm. A careful selection of quantization scheme for input, output and intermediate variables allows us to construct a complete ADBP decoding architecture that performs close to the double precision implementation and shows a promising complexity for large values of M. Finally, synthesis results of the main processing elements of ADBP are reported for 45 nm standard cell ASIC technology.

## Technology Options for 400 Gb/s PM-16QAM Flex-Grid Network Upgrades

- **ID**: ieee:6739082
- **Type**: journal
- **Published**: April15, 2
- **Authors**: Danish Rafique, Talha Rahman, Antonio Napoli +2
- **PDF**: https://ieeexplore.ieee.org/document/6739082
- **Abstract**: In this letter, we report on 400 Gb/s polarization multiplexed 16-state quadrature amplitude modulation (PM-16QAM) transponder variants and flex-grid network upgrade configurations. We address transponder subcarrier granularity, and demonstrate that the performance improvement, from dual-carrier to quad-carrier super-channel configuration, is limited to ~ 1.4 dB (in Q-factor, at power spectral density of 10-1 mW/GHz), at the cost of doubled hardware requirements. In view of that, we establish the performance improvements, for a dual-carrier 400 Gb/s PM-16QAM transceiver, as a function of increasing forward error correction overhead (FEC-OH) and spectral inversion based super-channel fiber nonlinearity compensation (SNLC-SI). We show that increasing the FEC-OH improves the transmission performance, at the cost of significant power consumption requirements, alternatively, employing SNLC-SI, at a lower FEC-OH, is a more power efficient solution. In particular, for homogeneous and heterogeneous launch power based network configurations, SNLC-SI enables ~ 23% and ~ 45% reach improvements at maximum considered FEC-OH (45%). At a fixed distance, it enables ~ 25% and ~ 50% power savings, respectively, compared with FEC-OH employing linear compensation only.

## On the Equivalence Between Canonical Forms of Recursive Systematic Convolutional Transducers Based on Single Shift Registers

- **ID**: ieee:6802341
- **Type**: journal
- **Published**: 2014
- **Authors**: Horia Balta, Catherine Douillard, Alexandru Isar
- **PDF**: https://ieeexplore.ieee.org/document/6802341
- **Abstract**: Standardized turbo codes (TCs) use recursive systematic convolutional transducers of rate  $b/(b{+}d)$ , having a single feedback polynomial  $(b{+}d{\rm RSCT})$ . In this paper, we investigate the realizability of the  $b{+}d{\rm RSCT}$  set through two single shift register canonical forms (SSRCFs), called, in the theory of linear systems, constructibility, and controllability. The two investigated SSRCF are the adaptations, for the implementation of  $b{+}d{\rm RSCT}$ , of the better-known canonical forms controller (constructibility) and observer (controllability). Constructibility is the implementation form actually used for convolutional transducers in TCs. This paper shows that any  $b{+}1{\rm RSCT}$  can be implemented in a unique SSRCF observer. As a result, we build a function,  $\xi:{{\cal H}}\to{\cal G}$ , which has as definition domain the set of encoders in SSRCF constructibility, denoted by  ${\cal H}$ , and as codomain a subset of encoders in SSRCF observer, denoted by  ${\cal G}$ . By proving the noninjectivity and nonsurjectivity properties of the function  $\xi$ , we prove that  ${\cal H}$  is redundant and incomplete in comparison with  ${\cal G}$ , i.e., the SSRCF observer is more efficient than the SSRCF constructibility for the implementation of  $b{+}1{\rm RSCT}$ . We show that the redundancy of the set  ${\cal H}$  is dependent on the memory  $m$  and on the number of inputs  $b$  of the considered  $b{+}1{\rm RSCT}$ . In addition, the difference between  ${\cal G}$  and  $\xi({\cal H})$  contains encoders with very good performance, when used in a TC structure. This difference is consistent for  $m\approx b>1$ . The results on the realizability of the  $b{+}1{\rm RSCT}$  allowed us some considerations on  $b{+}d{\rm RSCT}$ , with  $b$ ,  $d>1$ , as well, for which we proposed the SSRCF controllability. These results could be useful in the design of TC based on exhaustive search. So, the proposed implementation form permits the design of new TCs, which cannot be conceived based on the actual form. It is possible, even probable, among these new TCs to find better performance than in the current communication standards, such as LTE, DVB, or deep-space communications.

## The role model estimator revisited

- **ID**: ieee:6875118
- **Type**: conference
- **Published**: 2014
- **Authors**: J. Sayir
- **PDF**: https://ieeexplore.ieee.org/document/6875118
- **Abstract**: We re-visit the role model strategy introduced in an earlier paper, which allows one to train an estimator for degraded observations by imitating a reference estimator that has access to superior observations. We show that, while it is true and surprising that this strategy yields the optimal Bayesian estimator for the degraded observations, it in fact reduces to a much simpler form in the non-parametric case, which corresponds to a type of Monte Carlo integration. We then show an example for which only parametric estimation can be implemented and discuss further applications for discrete parametric estimation where the role model strategy does have its uses, although it loses claim to optimality in this context.

## An improvement of approximate BP decoding

- **ID**: ieee:6979829
- **Type**: conference
- **Published**: 2014
- **Authors**: G. Hosoya, H. Yashima
- **PDF**: https://ieeexplore.ieee.org/document/6979829
- **Abstract**: In this study, we present new methods for piece-wise linear approximation of Min-Sum (MS) decoding algorithm with good trade-off between performance and complexity. By analysis based on density evolution, the performance of the proposed method is identical to that of the Belief-Propagation decoding algorithm. The increment of the complexity of the proposed algorithm is small compared with the MS decoding algorithm. Moreover simulation result also shows effectiveness of the proposed algorithm.

## Boosting the capacity of legacy networks using PM-64QAM and Nyquist-WDM technique

- **ID**: ieee:6843826
- **Type**: conference
- **Published**: 2014
- **Authors**: A. Nespola, M. Huchard, G. Bosco +6
- **PDF**: https://ieeexplore.ieee.org/document/6843826
- **Abstract**: We demonstrate that the traffic capacity of legacy DWDM reconfigurable networks can be boosted thanks to the Nyquist-WDM technique and PM-64QAM modulation format. To this end, dual carrier and single carrier channels with raw transmission bit rate spanning from 224 Gb/s to 600 Gb/s have been generated by means of fast DAC and electrical digital filtering.

## Binary transmissions over Gaussian wiretap channel under soft/hard decision decoding

- **ID**: ieee:6979874
- **Type**: conference
- **Published**: 2014
- **Authors**: C. Qi, Y. Chen, A. J. Han.Vinck +1
- **PDF**: https://ieeexplore.ieee.org/document/6979874
- **Abstract**: We study the secrecy capacity of the Gaussian wiretap channel with binary input under either soft or hard decision decoding. A closed-form expression of the secrecy capacity is derived by assuming that the eavesdropper uses the same decoding method as the legitimate receiver. An upper bound of the loss of secrecy capacity is provided whilst a smart eavesdropper choosing the best decoding method and a legitimate receiver employing an insufficient decoding method. Simulations show that in the low SNR (of the main channel) region, the secrecy capacity of the binary-input Gaussian wiretap channel under soft decision decoding is larger than the one under hard decision decoding; as the SNR increases, the secrecy capacity under hard decision decoding tends to overtake.

## Performance comparison of hybrid partial response detectors over frequency-selective fading channels

- **ID**: ieee:6865485
- **Type**: conference
- **Published**: 2014
- **Authors**: Y. Peng, X. Huang
- **PDF**: https://ieeexplore.ieee.org/document/6865485
- **Abstract**: Frequency-selective fading channels are encountered in many modern wireless communication systems. In order to combat the intersymbol interference (ISI) introduced by such fading, equalization is required for reliable symbol detection. The maximum-likelihood sequence detector is the optimal equalization scheme; however its implementation complexity increases exponentially with the channel length and thus can be prohibitively high. In this paper, we compare the performance of two practically implementable suboptimal symbol detectors, including the partial response maximum-likelihood (PRML) detector and the partial response belief propagation (PRBP) detector, under frequency-selective fading channels. Both detectors employ a hybrid two-stage scheme, and allow a tradeoff between performance and complexity. The first stage is a partial response equalizer implemented as a linear filter which transforms the original channel impulse response to a target impulse response with reduced ISI. The residual ISI is then cancelled in the second stage using a more sophisticated nonlinear detector. In simulations, we consider a slow fading environment and use the ITU-R 3G channel models. From the numerical results, it is shown that in frequency-selective fading wireless channels, the PRBP detector provides superior performance over both the traditional minimum mean squared error linear equalizer and the PRML detector. Due to the effect of colored noise, the PRML detector in fading wireless channels is not as effective as it is in magnetic recording applications.

## Channel capacity and achievable rates of peak power limited AWGNC, and their applications to adaptive modulation and coding

- **ID**: ieee:6979912
- **Type**: conference
- **Published**: 2014
- **Authors**: S. Ikeda, K. Hayashi, T. Tanaka
- **PDF**: https://ieeexplore.ieee.org/document/6979912
- **Abstract**: The channel conditions vary over time in wireless communications. In order to transmit information efficiently, digital wireless communication systems choose the modulation scheme and coding adaptively. This framework is called the adaptive modulation and coding (AMC). The key problem of the framework is how to design the switching strategy. In this paper, we discuss the practical strategy for AMC by comparing the channel capacity, achievable rates with common modulation schemes, and the actual rates with AMC. The channel capacity is defined for a combination of the noisy channel and the constraint on the information source. The noisy channel we assume in this paper is the discrete-time complex-valued additive white Gaussian noise channel (AWGNC). For the constraint, we focus on the peak power instead of the average power since a practical communication transmitter often suffers from the peak power. We compare the capacity and achievable rates with practical modulation schemes. Furthermore, we simulate AMC and evaluate the actual rates numerically.

## On multivariate cryptosystems based on maps with logarithmically invertible decomposition corresponding to walk on graph

- **ID**: ieee:6933073
- **Type**: conference
- **Published**: 2014
- **Authors**: V. Ustimenko
- **PDF**: https://ieeexplore.ieee.org/document/6933073
- **Abstract**: The paper illustrates the concept of the map with logarithmically invertible decomposition. We introduce families of multivariate cryptosystems such that there security level is connected with discrete logarithm problem in Cremona group. The private key of such cryptosystem is a modification of graph based stream ciphers which use stable multivariate maps. Modified version corresponds to a stable map with single disturbance. If the disturbance (or initial condition) allows fast computation then modified version is almost as robust as original one. Methods of modification improve the resistance of such stream ciphers implemented on numerical level to straightforward linearisation attacks.

## Achievable rates for reduced-complexity receivers on nonlinear satellite channels with memory

- **ID**: ieee:6883970
- **Type**: conference
- **Published**: 2014
- **Authors**: J. Peng, S. G. Wilson
- **PDF**: https://ieeexplore.ieee.org/document/6883970
- **Abstract**: We study achievable information rates for nonlinear channels with memory, in the context of satellite communication with QAM modulation. The complete channel model can be described by a Volterra expansion, but large alphabet size and/or large channel memory length may prohibit optimal soft-output demodulator processing, say with the BCJR algorithm. Thus we focus on reduced-state receivers and their achievable information rates as a function of state complexity, amplifier backoff, and receiver input sampling rate. These achievable rates for mismatched receivers are known to be attainable with powerful error control codes and optimal decoding.

## Conference proceedings

- **ID**: ieee:6986334
- **Type**: conference
- **Published**: 2014
- **Authors**: 
- **PDF**: https://ieeexplore.ieee.org/document/6986334
- **Abstract**: Presents abstracts for the articles comprising the conference proceedings.

## Counting balanced sequencesw/o forbidden patterns via the betheapproximation and loop calculus

- **ID**: ieee:6875105
- **Type**: conference
- **Published**: 2014
- **Authors**: P. O. Vontobel
- **PDF**: https://ieeexplore.ieee.org/document/6875105
- **Abstract**: Motivated by coding-theoretic questions that arise in the context of flash-memory-based data storage, we consider the problem of (approximately) counting the number of sequences of length n that are balanced and that avoid certain patterns. We do this by formulating a suitable factor graph whose total sum represents the desired quantity, by computing the Bethe approximation of the total sum, and by bounding the difference between the total sum and its Bethe approximation via the loop calculus technique. Although there are alternative techniques for counting the above-mentioned sequences, the presented counting technique has the potential to generalize more easily to other setups.

## Link adaptation in closed-loop coded MIMO systems with LMMSE-IC based turbo receivers

- **ID**: ieee:6785410
- **Type**: conference
- **Published**: 2014
- **Authors**: B. Ning, R. Visoz, A. O. Berthet
- **PDF**: https://ieeexplore.ieee.org/document/6785410
- **Abstract**: In this paper, we address the problem of link adaptation for closed-loop multiple-input multiple-output antenna systems employing iterative (turbo) linear minimum mean-square error (soft) interference cancellation and decoding. The link adaptation relies on a low rate feedback. It performs joint spatial precoder selection (e.g., antenna selection) and modulation-coding scheme (MCS) selection so as to maximize the average rate subject to a 10% target block error rate constraint. Each MCS is based on a bit interleaved coded modulation whose binary code is a punctured convolutional code. The paper first details the architecture of the turbo receiver then presents a semi-analytical performance prediction method to analyze its evolution through the stochastic modeling of each of the components. The prediction method is then used to derive the limited feedback metrics (precoder and MCS choice) used by the link adaptation algorithms. As the main contributions of the paper, the true impact of this family of iterative “turbo” receivers on the link level performance is measured. Monte Carlo simulations under limited feedback show a significant gain of around 3 and 4dB compare to the classical LMMSE receiver conditional on a data rate of 12 bits per channel use, for a 4x4 MIMO frequency flat and frequency selective channel, respectively. Moreover, they also confirm that using log a posteriori probability ratios rather than log extrinsic probability ratios on coded bits for soft interference regeneration and cancellation yields faster convergence of the iterative process and better final performance (both for finite and infinite interleaver length regimes).

## Trade-offs in execution signature compression for reliable processor systems

- **ID**: ieee:6800307
- **Type**: conference
- **Published**: 2014
- **Authors**: J. Caplan, M. I. Mera, P. Milder +1
- **PDF**: https://ieeexplore.ieee.org/document/6800307
- **Abstract**: As semiconductor processes scale, making transistors more vulnerable to transient upset, a wide variety of microarchitectural and system-level strategies are emerging to perform efficient error detection and correction computer systems. While these approaches often target various application domains and address error detection and correction at different granularities and with different overheads, an emerging trend is the use of state compression, e.g., cyclic redundancy check (CRC), to reduce the cost of redundancy checking. Prior work in the literature has shown that Fletcher's checksum (FC), while less effective where error detection probability is concerned, is less computationally complex when implemented in software than the more-effective CRC. In this paper, we reexamine the suitability of CRC and FC as compression algorithms when implemented in hardware for embedded safety-critical systems. We have developed and evaluated parameterizable implementations of CRC and FC in FPGA, and we observe that what was true for software implementations does not hold in hardware: CRC is more efficient than FC across a wide variety of target input bandwidths and compression strengths.

## Pattern-Aware Sequential Monte Carlo Detection for Generalized Space-Time Shift Keying

- **ID**: ieee:6984626
- **Type**: conference
- **Published**: 2014
- **Authors**: J. Zheng, J. Tao, J. Dou +1
- **PDF**: https://ieeexplore.ieee.org/document/6984626
- **Abstract**: In the generalized space-time shift keying (G-STSK) modulation, the constraint of the activated dispersion matrix pattern makes the application of the sequential Monte Carlo (SMC) detector become nontrivial. In this paper, the pattern-aware variants of the stochastic SMC (SSMC) detector and the deterministic SMC (DSMC) detector for the G-STSK modulation are studied. Specifically, a pattern-aware importance sampling procedure is first presented to take into account the constraint of the activated dispersion matrix pattern in the SMC framework. Then, the SSMC detector generates symbol samples based on importance sampling and resampling techniques, whereas the DSMC detector recursively performs exploration and selection steps in a greedy manner. Computer simulation results are provided to demonstrate the performance of the SMC detectors.

## Capacity and shaping in coherent fiber-optic links

- **ID**: ieee:6995366
- **Type**: conference
- **Published**: 2014
- **Authors**: J. Estaran, D. Zibar, I. T. Monroy
- **PDF**: https://ieeexplore.ieee.org/document/6995366
- **Abstract**: Overview of the concepts and latest progress of capacity and constellation shaping in coherent optical links.

## On the primitive polynomial as the characteristic polynomial of a symmetric companion matrix

- **ID**: ieee:6979863
- **Type**: conference
- **Published**: 2014
- **Authors**: M. Hagiwara, T. Sasaki
- **PDF**: https://ieeexplore.ieee.org/document/6979863
- **Abstract**: As a fundamental work on coding theory, the characteristic polynomial for symmetric companion matrix of an extended field with the characteristic number 2 is investigated. A new linear recurrence relation is obtained. The relation provides us with an algorithm to calculate the determinant corresponding to a symmetric companion matrix of a primitive element of an extended field.

## Mutual information based resource allocation in the two-way relay channel with OFDM

- **ID**: ieee:6875329
- **Type**: conference
- **Published**: 2014
- **Authors**: S. Schedler, V. Kuehn
- **PDF**: https://ieeexplore.ieee.org/document/6875329
- **Abstract**: The combination of Physical-Layer Network Coding (PLNC) and Orthogonal Frequency Division Multiple Access (OFDMA) in Two Way Relay (TWR) systems enables promising designs for future generation wireless systems. So far, existing resource allocation schemes for OFDMA in TWR systems do not exploit the advantage of PLNC, i.e. the relay is not necessarily interested in the original user messages, but their XOR combination. Recently, it was shown that the achievable throughput in a TWR system with PLNC is close to its mutual information. Thus, the mutual information might be well suited to address the power allocation problem of a PLNC system with OFDMA. However, as no closed form expression is known for the mutual information of such a system, the optimal resource allocation cannot be found easily. Thus, an appropriate approximation for the mutual information in the critical MAC phase is proposed within this paper. Afterwards, that approximation is used to optimise the power allocations in an OFDMA system with individual power constraints. Simulation results and a comparison to alternative low effort algorithms confirm the efficiency of this approach.

## Design and Implementation for GPU-based seamless rate adaptive decoder

- **ID**: ieee:7054292
- **Type**: conference
- **Published**: 2014
- **Authors**: L. Qiu, M. Wang, J. Wu +2
- **PDF**: https://ieeexplore.ieee.org/document/7054292
- **Abstract**: Recently, the research on rate adaption at receiver has caused widespread concern. Seamless rate adaptive (SRA) is one of the promising rate adaptation schemes for wireless communication system. However, the high complexity of decoding hinders its application. The graphics processor unit (GPU) is able to provide a low-cost and flexible software-based multi-core architecture for high performance computing. This paper proposes a GPU design and implementation for SRA decoder. Firstly, we discuss the parallelism of SRA decoding algorithm. In order to improve the throughput of the GPU-based SRA decoder, a massive parallel architecture is used in SRA decoder, which consists of N × L parallel threads. Given fully consideration of the hardware architecture of GPU, we partition the block and select the appropriate number of threads within an individual block to further improve the throughput of GPU-based SRA decoder. In addition, we propose an efficient memory-usage mechanism in GPU-based SRA decoder which takes fully advantage of the shared memory in one block. Finally, We implement the SRA decoder on the Compute Unified Device Architecture (CUDA) platform. The GPU-based SRA decoder is flexible for different measurement matrix, and achieves a 60x speedup compared by its single-threaded counterpart performed on central processing unit (CPU).

## Sparse binary matrices as efficient associative memories

- **ID**: ieee:7028496
- **Type**: conference
- **Published**: 2014
- **Authors**: V. Gripon, V. Skachek, M. Rabbat
- **PDF**: https://ieeexplore.ieee.org/document/7028496
- **Abstract**: Associative memories are widely used devices which can be viewed as universal error-correcting decoders. Employing error-correcting code principles in these devices has allowed to greatly enhance their performance. In this paper we reintroduce a neural-based model using the formalism of linear algebra and extend its functionality, originally limited to erasure retrieval, to handle approximate inputs. In order to perform the retrieval, we use an iterative algorithm that provably converges. We then analyze the performance of the associative memory under the assumption of connection independence. We support our theoretical results with numerical simulations.

## Study on circularly arranged non-uniform constellations in dual-polarized MIMO-OFDM transmission

- **ID**: ieee:6873477
- **Type**: conference
- **Published**: 2014
- **Authors**: T. Shitomi, S. Asakura, S. Saito +2
- **PDF**: https://ieeexplore.ieee.org/document/6873477
- **Abstract**: We have been conducting research on a transmission system using ultra-multilevel orthogonal frequency division multiplexing (OFDM) technology and dual-polarized multiple-input multiple-output (MIMO) technology for the next generation of terrestrial broadcasting. Regarding the carrier modulation scheme, we studied a non-uniform constellation (NUC) which improves transmission characteristics by optimizing the distance between the signal points. In this study, we considered a circularly arranged NUC configured by 2m signal points in which m is an odd number. We performed simulations confirming that a NUC has advantages compared with a conventional uniform constellation (UC). Furthermore, we verified that the improvement in transmission performance varies depending on the number of signal points in the carrier modulation and the code rate of forward error correction (FEC). We also used a NUC in a dual-polarized MIMO-OFDM scheme. The results show the improvement of the NUCs tends to decrease in multipath environments.

## Low power reduced-complexity error-resilient MIMO detector

- **ID**: ieee:6865478
- **Type**: conference
- **Published**: 2014
- **Authors**: C. -A. Shen, M. S. Khairy, A. M. Eltawil +1
- **PDF**: https://ieeexplore.ieee.org/document/6865478
- **Abstract**: This paper presents a reduced-complexity low power error-resilient K-Best MIMO Detector. A novel tree-enumeration method is proposed such that the error-resilient detection processes a reduced search space and is more suitable for VLSI design. Moreover, a circuit-level optimization is employed to further simplify the complexity. Experimental results are given showing that the circuit-level optimization decreases the detector area by 15% and power consumption by 41%. Moreover, we show that the proposed error-resilient MIMO detector with reduced-voltage memory can achieve a total of 19% reduction in power consumption compared with the conventional scheme, while still maintaining close-to optimal PER performance.

## Implementation of a burst error and burst erasure channel emulator using an FPGA architecture

- **ID**: ieee:7039095
- **Type**: conference
- **Published**: 2014
- **Authors**: M. Rigo, C. Travan, F. Vatta +1
- **PDF**: https://ieeexplore.ieee.org/document/7039095
- **Abstract**: In this paper, the hardware implementation of a burst error channel and a burst erasure channel simulator in Cyclone II Field Programmable Gate Array (FPGA) is proposed. In telecommunications, a burst error channel is a data transmission channel in which errors occur in a contiguous sequence of symbols, such that the first and last symbols are in error and there exists no contiguous subsequence of m correctly received symbols within the error burst. An erasure channel is one in which each transmitted symbol is either received correctly or is corrupted so badly as to be considered erased. When the erasures are clustered together we refer to the channel as a burst erasure channel. Although software simulations are easy to set up to simulate a transmission channel behavior, they are very time consuming. In order to speed up the communication system performance evaluation process and the final parameter optimization design, direct hardware emulation is proposed and presented. The implementation can be easily extended to other FPGA architectures.

## On a problem of Massey

- **ID**: ieee:6804256
- **Type**: conference
- **Published**: 2014
- **Authors**: J. Hamkins
- **PDF**: https://ieeexplore.ieee.org/document/6804256
- **Abstract**: In 1976, Massey introduced a method to compute the confidence interval for the frame error rate of a coded communications system based on the simulation of just a few frame errors [1]. He commented that his approach did not apply to bit error rate confidence intervals, because bit errors are not independent in a coded system. In this paper, we show how to overcome the limitation Massey recognized, and present a method to compute a confidence interval of the bit error rate of a coded communications system from a simulation of bit and frame error events. The proposed interval may be easily computed from the first and second sample moments of the number of bits errors per frame.

## Hybrid DFSF-BP equalization for ATSC DTV receivers

- **ID**: ieee:6865484
- **Type**: conference
- **Published**: 2014
- **Authors**: Y. Peng, A. G. Klein, X. Huang
- **PDF**: https://ieeexplore.ieee.org/document/6865484
- **Abstract**: Severe intersymbol interference (ISI) is one of the main obstacles for reliable signal reception in ATSC DTV systems. Decision feedback equalizers (DFEs) are commonly used to suppress the ISI. However, DFEs may suffer from error propagation due to incorrect symbol decisions from the symbol slicer. This phenomenon deteriorates the performance even more when the post-cursor ISI is strong. In order to reduce error propagation, we present a novel hybrid equalization scheme for ATSC channels. The proposed scheme consists of an adaptive decision feedback sparsening filter (DFSF), and an iterative maximum a posteriori (MAP) equalizer based on the belief propagation (BP) algorithm. In the first stage, instead of removing all the ISI from post cursors, the DFSF employs a modified feedback filter which leaves the strongest post-cursor ISI taps uncorrected. As a result, a long ISI channel is equalized to a sparse channel having only a small number of nonzero taps. In the second stage, a belief propagation algorithm is applied to mitigate the residual ISI. Since the channel is typically time-varying and suffers from Doppler fading, the DFSF is adapted using the least mean square (LMS) algorithm, such that the amplitude and the locations of the nonzero taps of the equalized sparse channel appear to be fixed. As such, the channel appears to be static during the second stage of equalization which consists of the BP detector. Simulation results demonstrate that the proposed scheme outperforms the traditional DFE in symbol error rate, under both static channels and dynamic ATSC channels.

## A hybrid iterative MIMO detection algorithm: Partial Gaussian approach with integer programming

- **ID**: ieee:7008322
- **Type**: conference
- **Published**: 2014
- **Authors**: L. Fang, L. Xu, Q. Guo +2
- **PDF**: https://ieeexplore.ieee.org/document/7008322
- **Abstract**: In this paper, after showing MMSE-SIC suffers from performance loss when the channel is spatially correlated for Massive MIMO, we propose an effective hybrid iterative detection algorithm named partial Gaussian approach with integer programming (PGA-IP) to handle correlated channels. In PGA-IP, a partial gaussian approach is first employed to reduce the massive MIMO detection (with large dimension Nt ×Nr MIMO channel) to a problem of marginalizing M (M is a parameter and M≪ Nt, Nr) discrete valued symbols over an M-degree quadratic function. Then we employ integer programming which is a tree based branch-and-bound search algorithm to further reduce the complexity of the M-dimensional marginalization. Simulation results show that the proposed PGA-IP outperforms MMSE-SIC by about 5dB under heavily correlated channel with only several times of increased computational complexity. At the same time, with about 5% of the complexity of the exact PGA algorithm, the proposed PGA-IP only suffers marginal performance penalty.

## A generalization of threshold saturation: application to spatially coupled BICM-ID

- **ID**: ieee:6875247
- **Type**: conference
- **Published**: 2014
- **Authors**: K. Takeuchi
- **PDF**: https://ieeexplore.ieee.org/document/6875247
- **Abstract**: Spatial coupling was proved to improve the belief-propagation (BP) performance up to the maximum-a-posteriori (MAP) performance. This paper addresses an extended class of spatially coupled (SC) systems. A potential function is derived for characterizing a lower bound on the BP performance of the extended SC systems, and shown to be different from the potential for the conventional SC systems. This may imply that the BP performance for the extended SC systems does not coincide with the MAP performance for the corresponding uncoupled system. SC bit-interleaved coded modulation with iterative decoding (BICM-ID) is also investigated as an application of the extended SC systems.

## Performance of RoFSO system with spatial diversity reception technology in strong atmospheric turbulence channel

- **ID**: ieee:7062255
- **Type**: conference
- **Published**: 2014
- **Authors**: Kang Zong, Jiang Zhu, Xuan Tang
- **PDF**: https://ieeexplore.ieee.org/document/7062255
- **Abstract**: In this paper, we analyze the performance of radio over free space optical communication (RoFSO) system with spatial diversity reception technology (SDRT) operating over the gamma-gamma (GG) atmospheric turbulence channel. The bit error rate (BER) and outage probability of the system have been derived in closed form expressions using the generalized power series. For the same aperture size of the detectors, the SDRT can significantly improve the BER performance and outage probability of the RoFSO system. For example, the BER and the outage probability will decrease from ∼6.6×10−4 to ∼2.4×10−6 and from ∼2.3×10−4 to ∼4.9×10−6 for using an extra photodetector (PD) at SNR=30dB in strong atmospheric turbulence regime.

## Low power and low voltage SRAM design for LDPC codes hardware applications

- **ID**: ieee:6920865
- **Type**: conference
- **Published**: 2014
- **Authors**: R. Deena Kumari Selvam, C. Senthilpari, L. Lini
- **PDF**: https://ieeexplore.ieee.org/document/6920865
- **Abstract**: The Low Voltage Low Power (LVLP) 8T, 11T, 13T and ZA SRAM cell is designed using the dynamic logic SRAM cell. The SRAM cells are implemented using pass transistor logic technique, which is mainly focused on read and write operation. The circuits are designed by using DSCH2 circuit editor and their layouts are generated by MICROWIND3 layout editor. The Layout Versus Simulation (LVS) design has been verified using BSIM 4 with 65nm technology and with a corresponding voltage of 0.7V respectively. The simulated SRAM layouts are verified and analyzed. The SRAM 8T gives power dissipation of 0.145 microwatts, propagation delay of 37.2 pico seconds, area of 14 × 8 micrometers and a throughput of 4.037 nano seconds.

## Faulty stochastic LDPC decoders over the binary symmetric channel

- **ID**: ieee:6955096
- **Type**: conference
- **Published**: 2014
- **Authors**: C. L. Kameni Ngassa, V. Savin, D. Declercq
- **PDF**: https://ieeexplore.ieee.org/document/6955096
- **Abstract**: The analysis of error correction decoders running on faulty hardware has attracted an increasing interest in recent years, due to the inherent unreliability of emerging nanodevices. In this paper we investigate the performance of the stochastic decoder running on faulty hardware. To this end, we first introduce two error models to describe the noisy components of the decoder. We then provide a finite-length statistical analysis for each error model and, based on the obtained performance, we conclude that stochastic decoders have an inherent fault tolerant capability.

## LDPC code optimization with joint source-channel decoding of quantized Gauss-Markov signals

- **ID**: ieee:6884152
- **Type**: conference
- **Published**: 2014
- **Authors**: R. Asvadi, T. Matsumoto, M. Juntti
- **PDF**: https://ieeexplore.ieee.org/document/6884152
- **Abstract**: This paper proposes an extrinsic information transfer (EXIT)-chart based optimization technique of LDPC codes for the transmission of quantized Gauss-Markov (GM) source samples over additive white Gaussian (AWGN) noise channels. A joint source and channel (JSC) decoding technique of the proposed code is also devised. In the proposed scheme, no interleaving is performed between the source and the JSC encoder so that the decoder can well exploit the relatively low entropy of the source with memory compared to memory-less sources. At the transmitter, the quantized samples are converted to bit sequences with an injective mapping and the bit sequences are encoded using a systematic binary LDPC code. The proposed JSC decoder is a concatenation of a multi-state BCJR Markov decoder and a sum-product (SP) LDPC decoder. Decoding thresholds of the optimized codes at certain code rates are investigated for both uniform and Lloyd-Max quantizations in different numbers of bits. The decoding thresholds are close to the Gaussian code book Shannon limits for code rate Rc ≤ 0.5, although the gap to the Shannon limit notably increases at the higher rates. Finally, the simulation results confirm the significant improvement of coding gain on the bit error rate (BER) performances of the optimized LDPC codes with both the quantization schemes.

## Adaptive iterative decoding of MISO-BICM for DVB-T2

- **ID**: ieee:6776140
- **Type**: conference
- **Published**: 2014
- **Authors**: A. A. A. El-Banna, A. A. Emran, M. Elsabrouty +1
- **PDF**: https://ieeexplore.ieee.org/document/6776140
- **Abstract**: DVB-T2 employs multiple antenna techniques and error protection coding as part of its key technologies that enhance its performance and increase the capacity by 30% over its predecessor. It defines MISO space diversity technique as an optional part in the transmission chain along with combining LDPC with BCH codes in a Bit-Interleaved Coding and Modulation (BICM) scheme to achieve high performance. Using iterative receiver between the MISO detector and the decoder can approximate the optimal receiver performance. In this paper, we propose to use a modified soft K-Best List Sphere Decoder (KB-LSD) that iteratively uses the soft output LLR from LDPC decoder to calculate a prior LLR of the Maximum A Posterior Probability (MAP) of each transmitted symbol as a cost function of each child in the tree to decode the MISO SFBC to reach near optimal soft output MAP detection. We adapt the number of K paths chosen by the KB-LSD and the number of LDPC iterations according to the channel quality to achieve optimum receiver performance with reduced complexity of the system.

## Non-binary LDPC code with multiple memory reads for multi-level-cell (MLC) flash

- **ID**: ieee:7041532
- **Type**: conference
- **Published**: 2014
- **Authors**: C. A. Aslam, Y. L. Guan, K. Cai
- **PDF**: https://ieeexplore.ieee.org/document/7041532
- **Abstract**: NAND flash memory has been dominantly used in consumer electronic products ranging from hand-held phones to personal computers. However, the stored data in NAND flash memory is subject to several impairments such as Random Telegraph Noise (RTN), Cell-to-Cell Interference (CCI) and Data Retention Effect over time. In this paper, we focus on the RTN effect over flash memory cells which becomes even more serious as the memory approaches its lifetime. When the flash cells withstand increasingly large number of Program/Erase (P/E) operation, multiple interface traps are generated at tunnel oxide layer which results into large fluctuations in cell threshold voltage. These voltage fluctuations, in turn, degrade the system error performance. To tackle with this problem, we propose a simple yet effective system-level decoding scheme in which the memory cells are read multiple times to obtain threshold voltage fluctuations caused by RTN. Since each memory read operation produces a new realization of threshold voltage, we combine the read signal with LDPC extrinsic information. The performance improvements of our scheme are validated by computer simulation which shows that the lifetime of flash memory can be extended by more than 10K P/E cycles while maintaining bit-error-rate at 10−6 using NB-LDPC code over GF (4) with frame size N = 2272. This paper also presents the trade-off between performance improvement and extra memory sensing latency.

## Short-blocklength non-binary LDPC codes with feedback-dependent incremental transmissions

- **ID**: ieee:6874868
- **Type**: conference
- **Published**: 2014
- **Authors**: K. Vakilinia, T. -Y. Chen, S. V. S. Ranganathan +3
- **PDF**: https://ieeexplore.ieee.org/document/6874868
- **Abstract**: One advantage of feedback in a point-to-point memoryless channel is the reduction of the average blocklength required to approach capacity. This paper presents a communication system with feedback that uses carefully designed non-binary LDPC (NB-LDPC) codes and incremental transmissions to achieve 92–94% of the idealized throughput of rate-compatible sphere-packing with maximum-likelihood decoding (RCSP-ML) for average blocklengths of 150–450 bits. The system uses active feedback by carefully selecting each bit of additional incremental information to improve the reliability of the least reliable variable node. The system uses post processing in the decoder to further improve performance. The average blocklengths of 150–450 bits are small enough that feedback provides a throughput advantage but also large enough that overhead that might be associated with transmitter confirmation is more easily tolerated.

## Reducing the complexity of LDPC decoding algorithms: An optimization-oriented approach

- **ID**: ieee:7136286
- **Type**: conference
- **Published**: 2014
- **Authors**: M. Sarajlić, L. Liu, O. Edfors
- **PDF**: https://ieeexplore.ieee.org/document/7136286
- **Abstract**: This paper presents a structured optimization framework for reducing the computational complexity of LDPC decoders. Subject to specified performance constraints and adaptive to environment conditions, the proposed framework leverages the adjustable performance-complexity tradeoffs of the decoder to deliver satisfying performance with minimum computational complexity. More specifically, two constraint scenarios are studied: the “good-enough” performance and “as-good-as-possible performance”. Moreover, we also investigate the effects of different degrees of freedom in performance-complexity tradeoff adjustments. The effectiveness of the proposed method has been verified by simulating a set of LDPC codes used in IEEE 802.11 and IEEE 802.16 standards. Computational complexity reductions of up to 35% have been observed.

## Towards energy effective LDPC decoding by exploiting channel noise variability

- **ID**: ieee:7004180
- **Type**: conference
- **Published**: 2014
- **Authors**: T. Marconi, C. Spagnol, E. Popovici +1
- **PDF**: https://ieeexplore.ieee.org/document/7004180
- **Abstract**: In communication systems, channel quality variation is a well known phenomenon, which fundamentally influences the decoding process. While most of the time, the transmission takes place in good signal to noise conditions, to satisfy QoS requirements in all cases, telecom platforms rely on largely over-designed hardware, which may result in energy waste during most of their operation. In this paper we propose to exploit the channel noise variability and adapt the platform operation conditions such that QoS requirements are satisfied with the minimum energy consumption. In particular, we propose a technique to exploit channel noise variability towards energy effective LDPC decoding amenable to low-energy operation. Endowed with the channel noise variability knowledge, our technique adaptively tunes the operating voltage at runtime, aiming to achieve the optimal tradeoff between decoder performance and power con-sumption, while fulfilling the QoS requirements. To demonstrate the capabilities of our proposal we implemented it and other state of the art energy reduction methods in conjunction with a fully parallel LDPC decoder on a Virtex-6 FPGA. Our experiments indicate that the proposed technique outperforms state of the art counterparts, in terms of energy reduction, with 71% to 76% and 15% to 28%, w.r.t. early termination without and with DVS, respectively, while maintaining the targeted decoding robustness. Moreover, the measurements suggest that in certain conditions Degradation Stochastic Resonance occurs, i.e., the energy consumption is unexpectedly diminished due to the fact that unpredictable underpowered components facilitate rather than impede the decoding process.

## Performance and evaluation of OFDM and SC - FDE over an AWGN propagation channel under RF impairments using simulink at 60GHz

- **ID**: ieee:6996487
- **Type**: conference
- **Published**: 2014
- **Authors**: R. Gomes, Z. Al-Daher, A. Hammoudeh +3
- **PDF**: https://ieeexplore.ieee.org/document/6996487
- **Abstract**: This paper presents an implementation of the IEEE 802.15.3c standard, in Simulink, for high data-rate applications. The recent standard IEEE 802.15.3c provides the implementation of such wireless communication system using the 60GHz frequency band. OFDM and SC-FDE are the two transmission schemes adopted by the standard. Performance of these technologies at mm-wave signals are severely affected by nonlinearity of the RF front-ends. This paper presents the impact of RF impairments for each transmission scheme along with comparative analysis, in terms of BER and PSNR.

## Simulating DVB-T to DVB-T2 migration opportunities in Croatian TV broadcasting

- **ID**: ieee:7039121
- **Type**: conference
- **Published**: 2014
- **Authors**: E. Dumic, S. Grgic, D. Frank
- **PDF**: https://ieeexplore.ieee.org/document/7039121
- **Abstract**: In this paper we analyzed possible capacity gains in transition from DVB-T to DVB-T2 standard. We compared minimum C/N ratio needed for quasi error free reception of DVB-T and DVB-T2 systems with similar transmitting parameters currently used in Croatia. C/N was calculated using simulations developed in Matlab for those standards, in three commonly used channel models: Gaussian, Ricean and Rayleigh. Results show bandwidth increase of about 63% without significant increase of the minimum C/N. By using newer compression techniques and statistical multiplexing in large pools, it can be concluded that up to 10 times more TV channels (with the same quality) can be transmitted in the same occupied frequency bandwidth.

## Reconfigurable FEC codes for software-defined optical transceivers

- **ID**: ieee:6987087
- **Type**: conference
- **Published**: 2014
- **Authors**: C. Kachris, G. Tzimpragos, D. Soudris +1
- **PDF**: https://ieeexplore.ieee.org/document/6987087
- **Abstract**: Flexible Optical Networks can optimize the network resources by offering increased spectral utilization. However, these networks require the use of novel software-defined Optical Transceivers that can adapt their features to the channel's requirements. This paper presents a novel optical transceiver architecture using a reconfigurable FEC coding scheme for flexible optical networks. The proposed approach can dynamically support different versions of FEC codes (with different overheads, code lengths, and LLR-widths) based on the network's Quality-of-Service requirements, whereas it can also be applied for the dynamic reconfiguration of the DSP units and the realization of dynamic coded-modulation schemes. The proposed approach has been implemented into an FPGA platform. The performance evaluation shows that the reconfiguration time is always less than 12 ms, which means that the proposed scheme could be utilized in many optical networks, where the reconfiguration time (e.g. for the optical switches or the WSS) is in the order of a few ms.

## Joint channel estimation and raptor decoding over fading channel

- **ID**: ieee:6841207
- **Type**: conference
- **Published**: 2014
- **Authors**: B. W. Khoueiry, M. R. Soleymani
- **PDF**: https://ieeexplore.ieee.org/document/6841207
- **Abstract**: In this paper, we present a comparative study of joint channel estimation and decoding of factor graph-based codes over flat fading channels. A new simple channel approximation scheme is proposed. Specifically, when channel state information is not available at the receiver, a simpler approach is to estimate the channel state of a group of received symbols, then use the approximated value of the channel with the received signal to compute the log likelihood ratio. Simulation results show that the proposed scheme exhibits about 0.4 dB loss compared to the optimal solution when perfect channel state information is available at the receiver.

## On the energy-efficient multidimensional coded modulation for optical transport networks

- **ID**: ieee:7114428
- **Type**: conference
- **Published**: 2014
- **Authors**: I. B. Djordjevic
- **PDF**: https://ieeexplore.ieee.org/document/7114428
- **Abstract**: Optical transport networks have been affected by the following problems: (i) limited bandwidth of information infrastructure, (ii) high power consumption, (iii) heterogeneity of network segments, and (iv) security issues. As a solution to the first three problems, the multidimensional signaling has been proposed recently by author. In multidimensional signaling, for the conveyance information over spatial domain multiplexing (SDM) based fibers (few-mode fibers, few-core fibers, few-mode few- core fibers), all available degrees of freedoms, be optical or electrical, have been employed. In electrical domain discrete-time basis functions (such as Slepian sequences) have been employed. In optical domain, both polarization states and spatial modes have been employed. Additionally, the orthogonal division multiplexing (ODM) has been employed in optical domain to enable beyond 1 Pb/s serial optical transport over single-mode fibers. With SDM, the serial optical transport over SDM fibers exceeding 10 Pb/s is achievable. Concepts of statistical physics and information theory have been used in energy-efficient multidimensional signal constellation design. To solve for the security issues problem, the use of FBGs with impulse responses derived from mutually orthogonal Slepian sequences has been advocated.

## A Study of Equipment Dependence of a Single-Dot Pattern Method for an Information-Hiding by Applying an Error-Correcting Code

- **ID**: ieee:6998376
- **Type**: conference
- **Published**: 2014
- **Authors**: K. Kaneda, H. Kitazawa, K. Iwamura +1
- **PDF**: https://ieeexplore.ieee.org/document/6998376
- **Abstract**: In this study, we focus on a technique that embeds an electronically readable watermark directly on printed materials. This technique is used in the single-dot pattern method proposed by Kaneda et al. In the existing method, we extend a media size to A4 and improve an extraction rate over 99%. In this paper, if we change the type of printer, we verified the difference of basically the same the information extraction results. We also apply this technique on paper-based document with foreground and get successful embedding and extracting information without error by using error-correcting codes.

## The effect of saturation on belief propagation decoding of LDPC codes

- **ID**: ieee:6875305
- **Type**: conference
- **Published**: 2014
- **Authors**: S. Kudekar, T. Richardson, A. Iyengar
- **PDF**: https://ieeexplore.ieee.org/document/6875305
- **Abstract**: We consider the effect of LLR saturation on belief propagation decoding of low-density parity-check codes. Saturation is commonly done in practice and is known to have a significant effect on error floor performance. Our focus is on threshold analysis and the stability of density evolution. We analyze the decoder for certain low-density parity-check code ensembles and show that belief propagation decoding generally degrades gracefully with saturation. Stability of density evolution is, on the other hand, rather strongly affected by saturation and the asymptotic qualitative effect of saturation is similar to reduction of variable node degree by one.

## Closed-form Cramér-Rao lower bounds for CFO and phase estimation from turbo-coded square-QAM-modulated signals

- **ID**: ieee:7037447
- **Type**: conference
- **Published**: 2014
- **Authors**: F. Bellili, A. Methenni, S. Affes
- **PDF**: https://ieeexplore.ieee.org/document/7037447
- **Abstract**: We consider the problem of joint phase and carrier frequency offset (CFO) estimation from turbo-coded square-QAM modulated signals. We derive for the first time the closed-form expressions for the exact Cramér-Rao lower bounds (CRLBs) of this estimation problem. In particular, we introduce a new recursive process that enables the construction of arbitrary Gray-coded square-QAM constellations. Some hidden properties of such constellations will be revealed and carefully handled in order to decompose the likelihood function (LF) into the sum of two analogous terms. This decomposition makes it possible to carry out analytically all the statistical expectations involved in the Fisher information matrix (FIM). The new analytical CRLB expressions corroborate the previous attempts to evaluate the underlying perfromance bounds empirically. In the low-to-medium signal-to-noise ratio (SNR) region, the CRLB for code-aided (CA) estimation lies between the bounds for completely blind [non-data-aided (NDA)] and completely data-aided (DA) estimation schemes, thereby highlighting the coding gain potential in CFO and phase estimation. Most interestingly, in contrast to the NDA case, the CA CRLBs start to decay rapidly and reach the DA bounds at relatively small SNR thresholds. The derived bounds are also valid for LDPC-coded systems and they can be evaluated in the same way when the latter are decoded using the turbo principal.

## Advanced coded modulation for ultrahigh speed optical transmission

- **ID**: ieee:6887154
- **Type**: conference
- **Published**: 2014
- **Authors**: I. B. Djordjevic
- **PDF**: https://ieeexplore.ieee.org/document/6887154
- **Abstract**: This article consists of a collection of slides from the author's conference presentation. Some of the specific areas/topics discussed include: LDPC code design & large (high)-girth QC-LDPC Codes; Iterative decoding algorithms; FPGA implementation of decoders for QC-LDPC codes; LDPC codes derived from QC-LDPC code design; Binary/nonbinary irregular QC-LDPC codes derived from PBDs; Optimum signal constellation design & optimized mapping rules; EXIT chart analysis; Rate-adaptive LDPC-coded modulation; Nonbinary LDPC-coded modulation; Hybrid multidimensional coded-modulation; Multilevel/multidimensional LDPC-coded turbo equalization; and Rate-adaptive multidimensional coded-modulation.

## High throughput millimeter-wave MIMO beamforming system for short range communication

- **ID**: ieee:6866623
- **Type**: conference
- **Published**: 2014
- **Authors**: E. Pisek, S. Abu-Surra, J. Mott +2
- **PDF**: https://ieeexplore.ieee.org/document/6866623
- **Abstract**: The interest in short range communication has significantly increased in the last decade with the introduction of different wireless connectivity standards and their evolution such as IEEE802.11n/ac and IEEE802.11ad. New demands for higher resolution multimedia applications such as UHD push for higher data rates to exceed 30Gbps. This high data rate demand requires short range standards to adopt a new approach to accommodate these rates. Millimeter wave enable high bandwidth usage which implies higher capacity to accommodate 10–100Gbps data rates. However, the high data rate pose big challenges to both the system algorithm and architecture. In this paper, we propose a novel FPGA-based high-throughput beamforming MIMO system for millimeter wave short range communication. We present our first realization of a complete millimeter wave short range communication system, which includes RF frontend, ADC/DAC, beamforming control, synchronization, channel estimation, MIMO precoding/detection, and channel encoder/decoder. The design works at millimeter carrier frequency with 500MHz bandwidth and 2-channel MIMO Beamforming. We show realtime application test results as captured in the millimeter wave system.

## Code-Shift-Keying (CSK) with advanced FEC coding for GNSS applications in satellite multipath channel

- **ID**: ieee:7045139
- **Type**: conference
- **Published**: 2014
- **Authors**: R. Andreotti, A. Emmanuele, D. Fontanella +2
- **PDF**: https://ieeexplore.ieee.org/document/7045139
- **Abstract**: In this paper, Code-Shift-Keying (CSK) is investigated in combination with Forward Error Correction (FEC) coding techniques, with an additional block interleaving scheme. The target of this analysis is to evaluate the CSK capability to increase data rate or data demodulation sensitivity in GNSS scenarios as compared to the use of traditional BPSK A particular set of advanced signal baselines is reported as example of application to SBAS signal formats, assessing the data delivery performance in Additive White Gaussian Noise (AWGN) channel, two-ray multipath and Land Mobile Satellite (LMS) channel in terms of Bit Error Rate (BER).

## Optimal Joint Viterbi Detector Decoder (JVDD) over AWGN/ISI channel

- **ID**: ieee:6785346
- **Type**: conference
- **Published**: 2014
- **Authors**: Kheong Sann Chan, S. S. B. Shafiee, E. M. Rachid +1
- **PDF**: https://ieeexplore.ieee.org/document/6785346
- **Abstract**: Communication channels today use a state-of-the art iterative detector/decoder system on its receiver end to detect and decode the transmitted bits. This iterative detection system is comprised of a soft output detector, either the soft output Viterbi algorithm (SOVA) or the Bahl, Cocke, Jelinek and Raviv (BCJR) algorithm, and the Sum Product Algorithm (SPA) is used in the decoder. Although iterations of the soft information between these detector and decoder blocks gives rise to good performance over an inter-symbol-interference (ISI)/additive white Gaussian noise (AWGN) channel when the codeword length (CWL) is large, the iterative detector is sub-optimal. This suboptimality originates from the SPA algorithm that itself is suboptimal whenever there are cycles in the factor graph, in particular, when there are short cycles. Any practical code will have cycles in its factor graph. A second source of suboptimality is the iterative process itself. There exist iterations both within the SPA decoder and between the decoder and the detector. In this work, the authors propose a novel detection/decoding algorithm coined the Joint Viterbi Detector Decoder (JVDD) that functionally replaces the iterative detector/decoder in the channel. Unlike the iterative detector/decoder, the proposed algorithm performs detection and decoding on a single structure and is optimal over an ISI/AWGN channel when there are sufficient computational resources. In this work we describe the JVDD algorithm and perform preliminary analysis on its performance and complexity under various conditions.

## Fast convergence and reduced complexity receiver design for LDS-OFDM system

- **ID**: ieee:7136297
- **Type**: conference
- **Published**: 2014
- **Authors**: L. Wen, R. Razavi, P. Xiao +1
- **PDF**: https://ieeexplore.ieee.org/document/7136297
- **Abstract**: Low density signature for OFDM (LDS-OFDM) is able to achieve satisfactory performance in overloaded conditions, but the existing LDS-OFDM has the drawback of slow convergence rate for multiuser detection (MUD) and high receiver complexity. To tackle these problems, we propose a serial schedule for the iterative MUD. By doing so, the convergence rate of MUD is accelerated and the detection iterations can be decreased. Furthermore, in order to exploit the similar sparse structure of LDS-OFDM and LDPC code, we utilize LDPC codes for LDS-OFDM system. Simulations show that compared with existing LDS-OFDM, the LDPC code improves the system performance.

## Fast software polar decoders

- **ID**: ieee:6855069
- **Type**: conference
- **Published**: 2014
- **Authors**: P. Giard, G. Sarkis, C. Thibeault +1
- **PDF**: https://ieeexplore.ieee.org/document/6855069
- **Abstract**: Among error-correcting codes, polar codes are the first to provably achieve channel capacity with an explicit construction. In this work, we present software implementations of a polar decoder that leverage the capabilities of modern general-purpose processors to achieve an information throughput in excess of 200 Mbps, a throughput well suited for software-defined-radio applications. We also show that, for a similar error-correction performance, the throughput of polar decoders both surpasses that of LDPC decoders targeting general-purpose processors and is competitive with that of state-of-the-art software LDPC decoders running on graphic processing units.

## High Order Modulation in Faster-Than-Nyquist Signaling Communication Systems

- **ID**: ieee:6965997
- **Type**: conference
- **Published**: 2014
- **Authors**: J. Yu, J. Park, F. Rusek +2
- **PDF**: https://ieeexplore.ieee.org/document/6965997
- **Abstract**: In this paper we investigate the highly bandwidth-efficient Faster-than-Nyquist (FTN) signaling scheme under high order modulations. The FTN system is an emerging technology which has drawn attention in the contemporary spectrum-saving communication environment. Since FTN traditionally achieves high bandwidth efficiency through increased baud-rate, binary modulation is assumed in most research of FTN. The contribution of this paper lies in the extension into high order modulations and its assessment. This enables the communication systems to achieve higher data rates for the same bandwidth and receiver complexity than binary Nyquist signaling systems. Moreover, it is shown that an additional efficiency gain can be achieved by replacing the LDPC codes from the DVB-S2 standard by new optimized quasi-cyclic (QC) LDPC codes whose parameters are matched with FTN signaling.

## Code division multiple access communications systems for CubeSats at Lunar Lagrangian L1

- **ID**: ieee:6836341
- **Type**: conference
- **Published**: 2014
- **Authors**: A. Babuscia, C. Hung, D. Divsalar +1
- **PDF**: https://ieeexplore.ieee.org/document/6836341
- **Abstract**: Interplanetary Cubesats would enable low-cost missions for high-quality scientific and exploration programs. In particular cubeSats in formation have been proposed to operate in the vicinity of the Lunar Lagrangian L1 to collect lunar scientific data and to perform surface observation. In this paper we present a low complexity CDMA system for CubeSats (M small spacecraft) for communications between the Lunar L1 and Earth station. It is well known that the complexity of a CDMA transmitter is much lower than the complexity of the CDMA receiver. Moreover, the complexity of a channel encoder is always much lower than the complexity of the channel decoder. So for downlink communications it makes sense to use encoders for modern codes such as Turbo and LDPC followed by a spread spectrum transmitter for CDMA systems for CubeSats. Here we used an LDPC coded CDMA with BPSK modulation with rectangular and half-sine pulse shaping. Except for the PN generator seed numbers, the communication structure of all CubeSats would be identical and operating at one single RF frequency. For the uplink we may choose an uncoded CDMA system since the uplink transmit power is expected to be high enough to support the use of uncoded CDMA system. In addition since there would be no multipath for the uplink (broadcast channel) the use of orthogonal spreading codes such as Walsh codes is appropriate. The choice of orthogonal codes would reduce the multiuser interference. However due to some limitation (bandwidth, data rates, and M) we may be forced to use nonorthogonal PN codes. In addition, one of the spreading codes will not carry any data, which acts as an unmodulated pilot to reduce the complexity of synchronization. The proposed uncoded CDMA yields receivers for CubeSats that have low complexity implementation. Each component of CubeSats could easily extract its own received data with almost no interference from other users in case of orthogonal spreading codes. For the downlink, depending on the available bandwidth, and the data rates, a large processing gain could be obtained if the N is not large. Thus the multiuser interference degradation due to the other CubeSats could be made small at the Earth station. If N is large, and the bandwidth and data rates do not allow large processing gains then the multiuser interference could be high. In such cases we could use a simple parallel interference cancellation method with two stages that dramatically improves the system performance for the downlink. In this paper we accurately analyzed and simulated the proposed CDMA system for a concept Constellation of 20 CubeSats (M=20). All system simulations are done using Simulink platform.

## Noisy belief propagation decoder

- **ID**: ieee:7094847
- **Type**: conference
- **Published**: 2014
- **Authors**: C. -H. Huang, Y. Li, L. Dolecek
- **PDF**: https://ieeexplore.ieee.org/document/7094847
- **Abstract**: This paper analyzes the fundamental performance limits of an LDPC Belief Propagation (BP) decoder implemented on noisy hardware and proposes a robust decoder implementation to improve the resilience to hardware errors. Assuming that the effects of hardware noise in various computational units, i.e., variable nodes and check nodes, can be approximated by Gaussian noise, we develop a Gaussian approximate density evolution for noisy BP decoders. By the Gaussian approximate density evolution, we find that zero residual error rate is achievable for noisy BP decoders as long as the message representations are of arbitrarily high precision. Noisy BP decoding thresholds are then derived for various regular LDPC codes. These decoding thresholds determine maximum allowable communication and computation noise for reliable communication. Next, we propose an averaging BP decoder implementation by averaging over the messages in all up-to-date iterations to cancel out the computation noise. Simulation results demonstrate that on noisy hardware, the averaging BP decoder significantly reduces the residual error rates when compared to the nominal BP decoder.

## Memory sharing techniques for multi-standard high-throughput FEC decoder

- **ID**: ieee:6893199
- **Type**: conference
- **Published**: 2014
- **Authors**: Z. Wu, D. Liu
- **PDF**: https://ieeexplore.ieee.org/document/6893199
- **Abstract**: Nowadays multi-standard wireless baseband, Convolutional Code (CC), Turbo code and LDPC code are widely applied and need to be integrated within one FEC module. Since memory occupies half or even more area of the decoder, memory sharing techniques for area saving purpose is valuable to consider. In this work, several memory merging techniques are proposed. A non-conflict access technique for merged path metric buffer is proposed. The results show that 41% of total memory bits are saved when integrating three different decoding schemes including CC (802.11a/g/n), LDPC (802.11n and 802.16e) and Turbo (3GPP-LTE). Synthesis result with 65nm process shows that the merged memory blocks consume merely 1.06mm2 of the chip area.

## Flexible multistandard FEC processor design with ASIP methodology

- **ID**: ieee:6868664
- **Type**: conference
- **Published**: 2014
- **Authors**: Z. Wu, D. Liu
- **PDF**: https://ieeexplore.ieee.org/document/6868664
- **Abstract**: Designing decoder for forward error correction (FEC) is more and more challenging because of the requirements on simultaneous supporting of various wireless standards within one IC module. The flexibility, silicon cost and throughput efficiency are all necessary to be traded off. In this paper, by using ASIP methodology, software-hardware co-design is introduced to offer sufficient flexibility of FEC decoding. The decoding procedure can be programmable for decoding QC-LDPC, Turbo and Convolutional Codes. Firstly, the common features from all mentioned algorithms and their corresponding datapaths are analyzed and a unified multi-standard datapath is introduced. Based on it, an application specific instruction-set is proposed and an ASIP (Application Specific Instruction-set Processor) for the FEC algorithms is designed. The firmware FEC codes are developed to adapt to standards. Synthesis results show that the proposed FEC processor is 1.54mm2 under 65nm CMOS process. It offers QC-LDPC decoding for WiMAX, Turbo decoding for 3GPP-LTE, and 64 states Convolutional code (CC) decoding at the throughput of 193 Mbps, 62 Mbps and 60 Mbps respectively under clock frequency of 200 MHz. The proposed ASIP provides programmable high throughput compared to other tri-mode hardware modules.

## High order non-uniform constellations for broadcasting UHDTV

- **ID**: ieee:6952116
- **Type**: conference
- **Published**: 2014
- **Authors**: B. Mouhouche, D. Ansorregui, A. Mourad
- **PDF**: https://ieeexplore.ieee.org/document/6952116
- **Abstract**: This paper investigates high order NonUniform Constellations (NUC) with constellation sizes of up to 4K-QAM for broadcasting over-the-air very high data rate services such as Ultra-High Definition TV (UHDTV). An iterative algorithm is proposed for fast convergence towards the optimal NUC at each Signal-to-Noise Ratio (SNR) operating point. Performance evaluation assuming DVB-T2 as a reference shows significant gains for NUC over uniform constellations, above 1 dB for orders higher than 256-QAM, and up to 2 dB with 4K-QAM. This gain in dB converts into a relative throughput gain of nearly 10% compared to DVB-T2 using 32k FFT size with LDPC code rate 1/2.

## Analysis of one-step majority logic decoding under correlated data-dependent gate failures

- **ID**: ieee:6875304
- **Type**: conference
- **Published**: 2014
- **Authors**: S. Brkic, P. Ivanis, B. Vasić
- **PDF**: https://ieeexplore.ieee.org/document/6875304
- **Abstract**: In this paper we present analysis of one-step majority logic decoders made of unreliable components in the presence of data-dependent gate failures. Gate failures are modeled by a Markov chain, and based on the combinatorial representation of the fault configurations, a closed-form expression for the average bit error rate is derived for a regular LDPC code ensemble. Presented analysis framework is then used for obtaining upper bounds on decoding performance under timing errors.

## Analog-to-stochastic converter using magnetic-tunnel junction devices

- **ID**: ieee:6880490
- **Type**: conference
- **Published**: 2014
- **Authors**: N. Onizawa, D. Katagiri, W. J. Gross +1
- **PDF**: https://ieeexplore.ieee.org/document/6880490
- **Abstract**: This paper introduces an analog-to-stochastic converter using a magnetic-tunnel junction (MTJ) device for stochastic computation. Stochastic computation has recently been exploited for area-efficient hardware implementation, such as low-density parity-check (LDPC) decoders and image processors. However, power-and-area hungry analog-to-digital and digital-to-stochastic converters are required for the analog to stochastic signal conversion. The MTJ devices exhibit probabilistic switching behaviour between two resistance states. Exploiting the probabilistic behaviour, analog signals can be directly converted to stochastic signals to mitigate the signal-conversion overhead. The analog-to-stochastic signal conversion is mathematically described and the conversion circuit is designed based on a transistor/MTJ hybrid structure. The conversion characteristic is evaluated using device and circuit parameters that determines proper parameters for designing the analog-to-stochastic converter.

## Finite alphabet iterative decoders robust to faulty hardware: Analysis and selection

- **ID**: ieee:6955095
- **Type**: conference
- **Published**: 2014
- **Authors**: E. Dupraz, D. Declercq, B. Vasić +1
- **PDF**: https://ieeexplore.ieee.org/document/6955095
- **Abstract**: In this paper, we analyze Finite Alphabet Iterative Decoders (FAIDs) running on faulty hardware. Under symmetric error models at the message level, we derive the noisy Density Evolution equations, and introduce a new noisy threshold phenomenon (called functional threshold), which accurately characterizes the convergence behavior of LDPC code ensembles under noisy-FAID decoding. The proposed functional threshold is then used to identify FAIDs which are particularly robust to the transient hardware noise. Finite-length simulations are drawn to verify the validity of the asymptotical study.

## Millimetre wave bands for 5G wireless communications

- **ID**: ieee:7000244
- **Type**: conference
- **Published**: 2014
- **Authors**: V. Bhargava
- **PDF**: https://ieeexplore.ieee.org/document/7000244
- **Abstract**: Current interest in the millimeter wave technology is motivated by both old and new factors. Over the past decade, regulators have allocated up to 9 GHz of Spectrum near 60 GHz for license-exempt world-wide use. The emergence of numerous high-speed applications, including uncompressed HDTV, uncompressed multi-video streaming, very high-speed -file downloading and now potential use in wireless access and backhaul for future 5G heterogeneous networks, has provided the motivation for developing the technologies required to exploit this bandwidth. Moreover recent advances in realizing low-cost CMOS technology suitable for use at such high frequencies, improved algorithms for adaptively steering directive antenna beams; protocols for medium access control (MAC) and implementation of LDPC coding to improve link margins have made such exploitation a commercially viable prospect. In this talk we present technical challenges and opportunities for the application of millimeter-wave technologies in 5G era. It will be seen that it is a viable technology to provide multi-Gigabits per second access to mobile users and sustain the traffic growth.

## Instanton search algorithm for the ADMM penalized decoder

- **ID**: ieee:6874922
- **Type**: conference
- **Published**: 2014
- **Authors**: X. Liu, S. C. Draper
- **PDF**: https://ieeexplore.ieee.org/document/6874922
- **Abstract**: Linear programming (LP) decoding using the alternating direction method of multipliers (ADMM) has been shown to be an efficient algorithm. A non-convex variation based on the ADMM LP decoder called the ADMM penalized decoder was introduced by Liu et al. (IEEE ITW, Sep. 2012) to close the signal-to-noise ratio (SNR) gap between LP decoding and classic belief propagation (BP) decoding. This algorithm was shown to achieve or outperform BP decoding at all SNRs, including high SNRs where BP decoding suffers from the error floor effect. In this paper, we study the behaviors of the ADMM penalized decoder at high SNRs where simulation is infeasible. We use a generic tool called instanton analysis and propose an instanton search algorithm for the ADMM penalized decoder. We then apply the algorithm to the [155, 64] Tanner code and a [1057, 813] LDPC code. We show that the instanton information we obtained provides good predictions for word-error-rate curve at high SNRs. In addition, our results suggest that the ADMM penalized decoder can suffer from trapping sets.

## Adaptive joint carrier recovery and turbo decoding for nyquist terabit optical transmission in the presence of phase noise

- **ID**: ieee:6887153
- **Type**: conference
- **Published**: 2014
- **Authors**: Y. Zhao, N. Stojanovic, D. Chang +5
- **PDF**: https://ieeexplore.ieee.org/document/6887153
- **Abstract**: An adaptive joint carrier recovery and soft LDPC turbo decoding scheme in the presence of nonlinear phase noise is proposed and experimentally verified with 1.9dB coding gain in Nyquist Terabit PDM-DQPSK systems.

## A transmission method to combat multiple carrier frequency offsets (MCFOS) in coordinated multiple point (COMP) schemes

- **ID**: ieee:7041626
- **Type**: conference
- **Published**: 2014
- **Authors**: T. -H. Sang, S. -Y. Shan
- **PDF**: https://ieeexplore.ieee.org/document/7041626
- **Abstract**: In CoMP, two or multiple transmitters are coordinated to establish links with users. For example, a pair of coordinated base stations can transmit Alamouti-coded data, which has two streams, with one base station being responsible for one stream. When multiple carrier frequency offsets exist, the performance of Alamouti-type schemes in CoMP degrades seriously. MCFOs can exist when transmitters are not synchronized on the level of carrier generation, or can exist when the data streams face different Doppler situations caused by the movement of the users. Many works have been devoted to solving MCFOs for Alamouti-type signaling or space multiplexing. These techniques focus on the receiver algorithms, yet they work with limited success and usually are costly in implementation. We propose a transmission method which can facilitate a simple receiver to combat MCFOs. The receiver mainly uses a parallel ICI canceller to mitigate the effect of ICI. Simulation results of a system consisting of two cooperative transmitters with LDPC as the outer code are provided to illustrate our arguments.

## Soft intertrack interference cancellation for two-dimensional magnetic recording

- **ID**: ieee:6785322
- **Type**: conference
- **Published**: 2014
- **Authors**: E. B. Sadeghian, J. R. Barry
- **PDF**: https://ieeexplore.ieee.org/document/6785322
- **Abstract**: We propose a detection strategy for the two-dimensional magnetic recording channel with multiple read heads, in which intertrack interference is suppressed by a combination of linear combining and soft interference cancellation. This suppression reduces the detection problem to a traditional one-dimensional detection problem, so that we may leverage existing iterative detection strategies based on turbo equalization. Simulation results show that the proposed detector is able to reliably recover five tracks from an array of five read heads at an Eb/N0 value of 8.4 dB, when the tracks are independently coded with a rate-1/2 length-65536 LDPC code.

## Partial Constrained Group Decoding: A New Interference Mitigation Technique for the Next Generation Networks

- **ID**: ieee:6814042
- **Type**: conference
- **Published**: 2014
- **Authors**: O. Abu-Ella, M. Elmusrati
- **PDF**: https://ieeexplore.ieee.org/document/6814042
- **Abstract**: This paper investigates performance of the constrained partial group decoding (CPGD) technique in interference channel (IC) environment. It demonstrates the CPGD capability to manage and mitigate interference comparing with other interference mitigation schemes which are based on interference alignment strategy; this comparison is carried out for MIMO interference channel. Numerical results show that CPGD achieves one of the highest capacities comparing to other considered schemes. As well, evaluation of bit error rate (BER) using very long low density parity-check (LDPC) codes demonstrates the competency of the CPGD which significantly outperforms the other techniques. This makes the CPGD a promising scheme for interference mitigation for the next generation of wireless communication systems; especially, if we take into account that CPGD is only based on receive-side processing; and that means, there is no need for any overwhelming feedback in such a system. Also, and more importantly, if we keep in mind the reduction of its required computational complexity, due to its complexity controlling feature, i.e., by it's flexibility to limit the group size of the jointly decoded users, comparing with the huge computational complexity of the iterative multi- user detection (MUD) schemes, as interference alignment approach.

## Advanced techniques for spectrally efficient DVB-S2X systems

- **ID**: ieee:6934538
- **Type**: conference
- **Published**: 2014
- **Authors**: A. Ugolini, A. Modenini, G. Colavolpe +3
- **PDF**: https://ieeexplore.ieee.org/document/6934538
- **Abstract**: We investigate different techniques to improve the spectral efficiency of systems based on the DVB-S2 standard, when the transmitted signal bandwidth cannot be increased because it has already been optimized to the maximum value allowed by transponder filters. We will investigate and compare several techniques to involve different sections of the transceiver scheme. The techniques that will be considered include the use of advanced detection algorithms, the adoption of time packing, and the optimization of the constellation and shaping pulses. The LDPC codes recently proposed for the evolution of the DVB-S2 standard will be considered, as well as the adoption of iterative detection and decoding. Information theoretical analysis will be followed by the study of practical modulation and coding schemes.

## Software polar decoder on an embedded processor

- **ID**: ieee:6986083
- **Type**: conference
- **Published**: 2014
- **Authors**: B. Le Gal, C. Leroux, C. Jego
- **PDF**: https://ieeexplore.ieee.org/document/6986083
- **Abstract**: This paper presents the software implementation of a Polar Codes decoder on an embedded processor. An efficient use of computation and memory resource is made in order to devise a fast polar decoder on an embedded ARM processor. Memory footprint reduction and algorithmic simplifications are applied in order to increase the throughput of the decoder. The NEON instruction set of ARM processors is used to exploit the parallelism of the algorithm. The resulting decoder description is implemented on a Cortex A9 ARM processor. The throughput of the resulting decoder is reported and discussed for several parameters : the code rate, the code length and the multithreading mode. To the best of our knowledge, this is the first reported implementation of a polar decoder on an embedded processor core. The proposed software decoder reaches >100Mbps for a codelength of 16K. Moreover, it compares favorably with state of the art LDPC decoders implemented on embedded processors.

## Asynchronous baseband processor design for cooperative MIMO satellite communication

- **ID**: ieee:6908544
- **Type**: conference
- **Published**: 2014
- **Authors**: E. Rohani, J. Xu, T. Che +3
- **PDF**: https://ieeexplore.ieee.org/document/6908544
- **Abstract**: The challenges in satellite communication (SatCom) include but not limited to the customary complications of telecommunication such as channel condition, signal to noise ratio (SNR), etc. SatCom system is also prone to transient and permanent radiations hazards. Hence, in spite of the harsh environmental factors (weather phenomena, solar events, etc), a SatCom system must maintain reliable and predictable communication functions with limited source of power. This paper presents a SatCom system design for achieving both low-power and high fidelity communication. The design uses cooperative multiple input multiple output (MIMO) for spectral efficiency and diversity, low-density parity-check (LDPC) decoding for near Shannon-limit gain, and dynamic voltage and frequency scaling (DVFS)-assisted asynchronous circuit designs to achieve low-power and fault tolerance. The MIMO system permits uninterrupted service in the event of temporary/permanent link or unit failures. The results show that the resilience against injected radiation levels of upto about 25 fempto-Coulombs on critical path is achieved. This is more than 600 times the minimum charge required to logically flip a gate output in ordinary static CMOS gate.

## FPGA implementation of a FEC decoding subsystem for a DVB-S2 receiver

- **ID**: ieee:7002218
- **Type**: conference
- **Published**: 2014
- **Authors**: D. C. Alves, C. G. Chaves, E. R. de Lima +2
- **PDF**: https://ieeexplore.ieee.org/document/7002218
- **Abstract**: This paper presents the implementation of a FEC decoding subsystem for a DVB-S2 compliant receiver. The FEC decoder is composed by three blocks: De-interleaver, LDPC and BCH decoders, and its main goal is correcting the bits that were corrupted by the channel during transmission. The DVB-S2 standard defines several coding schemes and interleaving methods for protecting the data, and all the configurations were considered in this implementation. This work presents the structure and functionality of the FEC subsystem, the platform that was assembled for measuring its performance, and the FPGA synthesis and BER performance results.

## Achievable rates and forward-backward decoding algorithms for the Gaussian relay channels under the one-code constraint

- **ID**: ieee:6883639
- **Type**: conference
- **Published**: 2014
- **Authors**: X. Huang, H. Chen, X. Ma
- **PDF**: https://ieeexplore.ieee.org/document/6883639
- **Abstract**: This paper is concerned with the Gaussian relay channel (GRC) under the one-code constraint, where the source and the relay utilize the same code to send message. An advantage of such one-code constraint is that the error propagation resulting from re-encoding can be mitigated as the relay can forward directly the decoded “codeword” to the destination. The maximal achievable rate of the considered GRC is derived using the technique of superposition block Markov encoding based on the single code. Moreover, the forward-backward (FB) decoding strategies over the sliding window are developed both at the destination and at the relay. When LDPC codes are applied to the GRC system, a practical FB message passing decoding algorithm is presented. Simulation results show that the decoding performance can be improved as the window length increases and a small length (no greater than 4) is good enough for the FB decoding, and that re-encoding at relay may degrade the decoding performance at the destination.

## FPGA implementation of a multi-algorithm parallel FEC for SDR platforms

- **ID**: ieee:6927446
- **Type**: conference
- **Published**: 2014
- **Authors**: Zhenzhi Wu, D. Liu, Zheng Yang +2
- **PDF**: https://ieeexplore.ieee.org/document/6927446
- **Abstract**: Forward Error Correction (FEC) consumes excessive computation in a Software Defined Radio (SDR) system. In this work, a high-throughput flexible FEC processor is proposed for the decoding acceleration. The FEC processor enables Turbo/QC-LDPC/Convolutional Code decoding with software-hardware co-reconfigurability. A multi-algorithm unified trellis processing unit is introduced for resource sharing. A parallel architecture is proposed for high-throughput decoding. The Software Defined FEC (SD-FEC) with Application Specific Instruction-set Processor architecture is introduced for improving flexibility and enabling fast reconfiguration. The proposed SD-FEC can be applied to both low-cost low power applications and high performance applications. Results show that the proposed tri-mode FEC processor achieves high decoding efficiency and enough flexibility, which suits for the flexible SDR platforms.

## Table of contents

- **ID**: ieee:7016720
- **Type**: conference
- **Published**: 2014
- **Authors**: 
- **PDF**: https://ieeexplore.ieee.org/document/7016720
- **Abstract**: The following topics are dealt with: Generalized supercodes decoding; collision-secure video fingerprinting; multicomponent network codes; iterative turbo code list decoder; Mersenne matrices; Hadamard matrices; cyclic generalized codes; resource allocation algorithm; multiple-access channel; separable Goppa polynomial; tail-biting convolutional codes; random multiple access system; S-user vector adder channel coding; lossless image compression scheme; binary layers scanning; machine-type communications; low-density parity-check codes; partial unit memory codes; slotted ALOHA; embedded space-time block codes; concatenated codes systems; transport layer coding; variable coding rate; jamming-proof signal-code constructions; OFDM systems; interference cancellation; error-correcting code; low-complexity decoded H-LDPC code; irregular LDPC code; random coding; GPT cryptosystem; optimal weighted image watermarking and error concealment techniques.

## Program

- **ID**: ieee:6955072
- **Type**: conference
- **Published**: 2014
- **Authors**: 
- **PDF**: https://ieeexplore.ieee.org/document/6955072
- **Abstract**: The following topics are dealt with: coded modulation; soft decoding; analog processing; trapping sets and graphs; spatially coupled codes; hardware design; source-channel coding; genetic codes; satellite channels; nonbinary LDPC codes; latency, polar codes, erasure codes; relay codes; and MIMO codes.

## Table of contents

- **ID**: ieee:6947684
- **Type**: conference
- **Published**: 2014
- **Authors**: 
- **PDF**: https://ieeexplore.ieee.org/document/6947684
- **Abstract**: The following topics are dealt with: Fe-Ni-Mn nanoparticles; self healing magnet-ionomer composites; linear-rotary electromagnetic induction sensor; printed circuit coils; magnetic tunnel junctions; spin-torque transfer magnetic random access memory (STT-MRAM); spin torque oscillator; heat assisted magnetic recording (HAMR); microwave assisted magnetic recording; PM motor vibration; and iterative joint detection and decoding for nonbinary LDPC coded partial-response channels with written-in errors.

## Table of contents

- **ID**: ieee:7000246
- **Type**: conference
- **Published**: 2014
- **Authors**: 
- **PDF**: https://ieeexplore.ieee.org/document/7000246
- **Abstract**: The following topics are dealt with: high mobility wireless communications; antennas; VANET; MIMO system; OFDM; wireless local area network; cognitive radio; relay network; cooperative wireless network; LDPC codes; railway communication; and fading channel.

## Session 27 overview: Energy-efficient digital circuits: Energy-efficient digital subcommittee

- **ID**: ieee:6757573
- **Type**: conference
- **Published**: 2014
- **Authors**: B. Sheu, M. Verhelst
- **PDF**: https://ieeexplore.ieee.org/document/6757573
- **Abstract**: Next-generation computing devices for mobile applications require energy efficiency, while achieving increased system performance and programmability. This is enabled through ultra-low-voltage operation, application kernel hardware acceleration, and embedded reconfigurable logic. The papers in this session present several advanced implementation techniques to take these trends to the next level and bring them to the market. Examples include back-biasing techniques, variation-resilient near-threshold operation, charge-recovery schemes, and multi-granularity reconfigurable logic. These techniques are demonstrated in real-world applications such as a DSP processor, low-density parity check (LDPC) decoders, a speech-recognition processor, an FFT core, and a JPEG encoder.

## Taber of contents

- **ID**: ieee:7062387
- **Type**: conference
- **Published**: 2014
- **Authors**: 
- **PDF**: https://ieeexplore.ieee.org/document/7062387
- **Abstract**: The following topics are dealt with: UWB Communications; Electric Power Systems; LTCC Technology; OFDM Systems; UWB Waveguide Bandpass Filter; Lossy Filter; Pulse-Radiating Bow-Tie Antenna; Waveguide Band-pass Filter; Multipath Channel; Low-Power Phase-Locked Loop; RFIC; Spread Spectrum Sliding Correlator Channel; Circular Polarization Microstrip Antenna Array; Wireless Sensor Networks; Coaxial Feed Microstrip Patch Antenna; Power Combiner; MAC Layer Multicast Protocol; Frequency Reconfigurable Antenna; Particle Swarm Optimization; Direction-of-Arrival Estimation; Heterogeneous Cellular Networks; LDPC Codes; Compressed Sensing; Light-weighted Cooperative Adaptive Channel Hopping Mechanism; Speech Signal Processing; Dual-Polarized Dielectric Resonator Antenna; Stepped Impedance Resonators; Microwave High Power Amplifier; MIMO Underwater Acoustic Communication; Nematic Liquid Crystal Broadband Tunable Power Divider; Sparse Signal Recovery; HEMT Technology; Range-Doppler Spectral Image Processing; Wideband Double-Balanced Mixer Chip; Rectangular Waveguide Filter; Substrate Integrated Waveguide; and Wireless Indoor Positioning.

## Technical program

- **ID**: ieee:6979790
- **Type**: conference
- **Published**: 2014
- **Authors**: 
- **PDF**: https://ieeexplore.ieee.org/document/6979790
- **Abstract**: The following topics are dealt with: LDPC codes; Shannon theory; data hiding; network security; image processing; signal processing; convolutional codes; computational security; quantum information; quantum channels; coding theory; stochastic process; source coding; data security; data compression; cryptography; quantum secure network; algebraic codes; information theoretic security; OFDM systems; multiuser information theory; cryptology; multiple access systems; constrained codes; flash codes; MIMO relay channel; and 2D magnetic recording.

## [Front cover]

- **ID**: ieee:6979788
- **Type**: conference
- **Published**: 2014
- **Authors**: 
- **PDF**: https://ieeexplore.ieee.org/document/6979788
- **Abstract**: The following topics are dealt with: LDPC codes; Shannon theory; data hiding; network security; image processing; signal processing; convolutional codes; computational security; quantum information; quantum channels; coding theory; stochastic process; source coding; data security; data compression; cryptography; quantum secure network; algebraic codes; information theoretic security; OFDM systems; multiuser information theory; cryptology; multiple access systems; constrained codes; flash codes; MIMO relay channel; and 2D magnetic recording.

## Table of contents

- **ID**: ieee:7017220
- **Type**: conference
- **Published**: 2014
- **Authors**: 
- **PDF**: https://ieeexplore.ieee.org/document/7017220
- **Abstract**: The following topics are dealt with: opportunistic mobile social networks; data center networks; WLAN; COFDM systems; home location estimation; device-to-device communication; multipath DS-UWB system; QC-LDPC codes; authentication scheme; mobile applications; encryption; wireless sensor network; software defined satellite networks; context-aware service composition; P2P service; checkpointing; ZigBee; virtual network reconfiguration; computational grid; cloud computing; Web service; real-time systems; search engine; and smart-grid powered point-to-point cognitive radio system.

## Table of contents

- **ID**: ieee:6951851
- **Type**: conference
- **Published**: 2014
- **Authors**: 
- **PDF**: https://ieeexplore.ieee.org/document/6951851
- **Abstract**: The following topics are dealt with: Channel Modeling; Game Theory; LDPC; Massive MIMO; mmWave; Network Coding; Optical Communications; Secrecy and Security; Synchronization; Polar and Fountain Codes; Device-to-Device Communications; Interference Alignment; Future Cellular; Modulation; Spectrum Sensing; OFDM Design; Coding; Cognitive Relay Networks; Delayed CSI; Beamforming; Distributed and Collaborative Sensing; Resource Allocation in Relay Networks; Resource Allocation in Cognitive Networks; Synchronization and Estimation; Communication Theory; Small-cell and Multi-cell Networks; Space-time Coding for Relay Networks; OFDM Optimization; MIMO Communications; Heterogeneous Networks; LTE/LTE-Advanced; Small Cell Networks; Cognitive Radio; MAC Protocols; Green Communications; Sensor Networks; Multimedia Communications; Relaying in Wireless Networks; Routing; Mobile and Wireless Networks; Cellular Networks; Femtocells Networks; Energy Efficient Networks; Scheduling; Ad Hoc Networks; Vehicular Networks; Power Consumption and Allocation; and Internet of Things.

## Hardware-Oriented Construction of a Family of Rate-Compatible Raptor Codes

- **ID**: ieee:6814837
- **Type**: journal
- **Published**: 2014
- **Authors**: H. Zeineddine, L. M. A. Jalloul, M. M. Mansour
- **PDF**: https://ieeexplore.ieee.org/document/6814837
- **Abstract**: A family of architecture-aware Raptor codes is constructed. The proposed construction scheme is targeted to design rate-compatible structured codes that span a wide range of rates and block sizes while still having hardware-efficient decoder implementations. The codes match the corresponding fixed-rate LDPC codes in error-correcting performance, decoding convergence speed, and message-memory requirements. Three novel steps are incorporated in the scheme: 1) a new group-based design of the code source matrix; 2) an architecture-aware row splitting-after-merging technique to construct irregular precodes; and 3) structured LT row-encoding. A code instance was designed accordingly and compared to standardized LDPC codes. The error-rate performance closely matches that of LDPC, whereas the convergence speed and message count gaps are narrowed down to values between  $[1.1\times, 1.8\times]$ and  $[1.1\times, 1.3\times]$, respectively.

## Cloud Transmission: System Performance and Application Scenarios

- **ID**: ieee:6746098
- **Type**: journal
- **Published**: 2014
- **Authors**: J. Montalbán, L. Zhang, U. Gil +9
- **PDF**: https://ieeexplore.ieee.org/document/6746098
- **Abstract**: Cloud transmission (Cloud Txn) is a flexible multilayer system that uses spectrum overlay technology to simultaneously deliver multiple program streams with different characteristics and robustness for different services (mobile TV, HDTV, and UHDTV) in one radio frequency channel. Cloud Txn is a multilayer transmission system like layered-division multiplexing. The transmitted signal is formed by superimposing a number of independent signals at desired power levels to form a multilayered signal. The signals of different layers can have different coding, bit rate, and robustness. The upper layer system parameters are chosen to provide very robust transmission that can be used for high-speed mobile broadcasting. The bit rate is traded for powerful coding and robustness so that the signal-to-noise ratio (SNR) threshold at the receiver is in the range of ${-}{2}$ to ${-}{\rm 3}~{\rm dB}$ . The top layer is designed to withstand combined noise, co-channel interference and multipath distortion power levels higher than the desired signal power. The lower-layer signal can be a DVB-T2 signal or another new system to deliver HDTV/UHDTV to fixed receivers. The system concept is open to technological advances that might come in the future: BICM/non uniform-QAM, rotated constellations, time frequency slicing or MIMO techniques can be implemented in the Cloud Txn lower (high data rate) layer. The system can have backward compatible future extensions, adding more lower layers for additional services without impact legacy services. This paper describes the performance of Cloud Txn broadcasting system.

## Multiple-Vote Symbol-Flipping Decoder for Nonbinary LDPC Codes

- **ID**: ieee:6731592
- **Type**: journal
- **Published**: 2014
- **Authors**: F. García-Herrero, E. Li, D. Declercq +1
- **PDF**: https://ieeexplore.ieee.org/document/6731592
- **Abstract**: A multiple-vote symbol-flipping (MV-SF) decoding algorithm for nonbinary low-density parity-check (NB-LDPC) codes is proposed in this paper. Our algorithm improves the generalized bit-flipping algorithm (GBFDA) by considering the multiplicity of the candidates at the check-node output, to perform a more accurate symbol-flipping decision at the variable node update. The MV-SF algorithm greatly improves the frame error rate performance of GBFDA and approaches the performance of the best state-of-the-art decoders [extended min-sum and min-max (Min–Max)] with lower complexity. For a  $(N=837,K=723)$  NB-LDPC code over GF(32), the decoder derived from the proposed algorithm can reach a throughput higher than 500 Mb/s and a coding gain of 0.44 dB compared with the most efficient GBFDA architecture with only twice the silicon area. Our architecture has 27% efficiency gain compared with the best Min–Max architecture found in the literature, with a performance loss of just 0.21 dB at frame error rate  $10^{-4}$ .

## Soft-Decision Feedback Turbo Equalization for LDPC-Coded MIMO Underwater Acoustic Communications

- **ID**: ieee:6479709
- **Type**: journal
- **Published**: 2014
- **Authors**: A. Rafati, H. Lou, C. Xiao
- **PDF**: https://ieeexplore.ieee.org/document/6479709
- **Abstract**: In this paper, a low-complexity turbo-detection scheme is proposed for single-carrier multiple-input-multiple-output (MIMO) underwater acoustic (UWA) communication systems that employ low-density parity-check (LDPC) channel coding. The proposed iterative soft-decision feedback equalization (SDFE) algorithm offers a novel approach to combat error propagation by utilizing the past soft decisions to mitigate intersymbol interference. In addition, we utilize an iterative data detection and channel estimation scheme to reduce the pilot overhead used in the data communication system. Performance of the proposed detection scheme is demonstrated through extensive communication data from two undersea experiments. The results show that the proposed SDFE algorithm provides robust detection for MIMO UWA communications with different modulations and different symbol rates, at different transmission ranges.

## On Detection Method for Soft Iterative Decoding in the Presence of Impulsive Interference

- **ID**: ieee:6809154
- **Type**: journal
- **Published**: 2014
- **Authors**: V. Dimanche, A. Goupil, L. Clavier +1
- **PDF**: https://ieeexplore.ieee.org/document/6809154
- **Abstract**: This paper deals with the performance improvement of soft iterative decoders in impulsive interference modeled by additive noise. In case of  $\alpha$-stable noise, the inputs of the belief propagation decoder are too complex to compute. We propose to use an approximation of the log likelihood ratio in an impulsive environment. Even with this simplification, we show that the performance stays close to the one obtained using the true probability density function. Moreover, the robustness of our solution against the parameter estimation is investigated.

## Closed-Form CRLBs for SNR Estimation From Turbo-Coded BPSK-, MSK-, and Square-QAM-Modulated Signals

- **ID**: ieee:6850016
- **Type**: journal
- **Published**: 2014
- **Authors**: F. Bellili, A. Methenni, S. Affes
- **PDF**: https://ieeexplore.ieee.org/document/6850016
- **Abstract**: In this contribution, we derive for the first time the closed-form expressions for the Cramér-Rao lower bounds (CRLBs) of the signal-to-noise ratio (SNR) estimates from BPSK-, MSK- and square-QAM modulated signals over turbo-coded transmissions. These CRLBs, relatively easy to derive from BPSK, MSK and QPSK transmissions, become extremely challenging with higher-order square-QAM-modulated signals. In the latter, by exploiting the structure of the Gray mapping, we are able to factorize the likelihood function thereby linearizing all the derivation steps for the Fisher information matrix (FIM) elements. We also propose another approach that allows the evaluation of the considered bounds using extensive Monte Carlo computer simulations. The analytical CRLBs coincide exactly with their empirical counterparts validating thereby our new analytical expressions. Numerical results suggest that the CLRBs for code-aided (CA) SNR estimates range between the CRLBs for non-data-aided (NDA) SNR estimates and those for data-aided (DA) ones, thereby highlighting the expected potential in SNR estimation improvement from the coding gain. Indeed, the CA CRLBs improve by decreasing the overall coding rate due to enhanced decoding capabilities. However they do increase with the modulation order for a given code rate. Finally, the derived bounds are also valid for LDPC coded systems and they can be evaluated when the latter are decoded using the turbo principal.

## Adaptive HARQ With Non-Binary Repetition Coding

- **ID**: ieee:6780990
- **Type**: journal
- **Published**: 2014
- **Authors**: S. Pfletschinger, D. Declercq, M. Navarro
- **PDF**: https://ieeexplore.ieee.org/document/6780990
- **Abstract**: We consider Incremental Redundancy Hybrid Automatic Repeat reQuest (IR-HARQ) in which the code rate and modulation of the initial transmission and all retransmissions are adjusted based on average channel statistics. In the absence of instantaneous channel state information at the transmitter (CSIT), we present a method which computes, prior to transmission, the optimum code rates and modulations and explicitly considers a given maximum number of retransmissions. For the case that additional feedback on CSI of previous transmission attempts is available, we present two heuristic schemes which exploit this knowledge and offer increased throughput at the cost of higher computational complexity. We employ a rate-adaptive non-binary LDPC coding scheme which makes use of non-binary repetitions. While this coding scheme is particularly well-suited for adaptive IR-HARQ, we note that the presented analysis can be applied to any other channel code which employs soft decoding.

## A 16-Core Processor With Shared-Memory and Message-Passing Communications

- **ID**: ieee:6634267
- **Type**: journal
- **Published**: 2014
- **Authors**: Z. Yu, R. Xiao, K. You +12
- **PDF**: https://ieeexplore.ieee.org/document/6634267
- **Abstract**: A 16-core processor with both message-passing and shared-memory inter-core communication mechanisms is implemented in 65 nm CMOS. Message-passing communication is enabled in a 3 $\times$  6 Mesh packet-switched network-on-chip, and shared-memory communication is supported using the shared memory within each cluster. The processor occupies 9.1 ${\rm mm}^{2}$  and operates fully functional at a clock rate of 750 MHz at 1.2 V and maximum 800 MHz at 1.3 V. Each core dissipates 34 mW under typical conditions at 750 MHz and 1.2 V while executing embedded applications such as an LDPC decoder, a 3780-point FFT module, an H.264 decoder and an LTE channel estimator.

## Channel Coding and Lossy Source Coding Using a Generator of Constrained Random Numbers

- **ID**: ieee:6750723
- **Type**: journal
- **Published**: 2014
- **Authors**: J. Muramatsu
- **PDF**: https://ieeexplore.ieee.org/document/6750723
- **Abstract**: Stochastic encoders for channel coding and lossy source coding are introduced with a rate close to the fundamental limits, where the only restriction is that the channel input alphabet and the reproduction alphabet of the lossy source code are finite. Random numbers, which satisfy a condition specified by a function and its value, are used to construct stochastic encoders. The proof of the theorems is based on the hash property of an ensemble of functions, where the results are extended to general channels/sources and alternative formulas are introduced for channel capacity and the rate-distortion region. Since an ensemble of sparse matrices has a hash property, we can construct a code by using sparse matrices.

## Multidimensional Optical Transport Based on Optimized Vector-Quantization-Inspired Signal Constellation Design

- **ID**: ieee:6877631
- **Type**: journal
- **Published**: 2014
- **Authors**: I. B. Djordjevic, A. Z. Jovanovic, Z. H. Peric +1
- **PDF**: https://ieeexplore.ieee.org/document/6877631
- **Abstract**: An optimized vector-quantization-inspired signal constellation design (OVQ-SCD) suitable for multidimensional optical transport is proposed, in which signal constellation radii transformation function is optimized and near-uniform distribution of points is achieved. The proposed OVQ-SCD is used in a tandem with a hybrid multidimensional coded-modulation scheme employing Slepian sequences as electrical discrete-time basis functions, orthogonal prolate spheroidal wave functions as impulse responses of optical filters in orthogonal-division multiplexing, and spatial modes as optical continuous-time basis functions. It has been shown that the proposed multidimensional coded-modulation schemes based on OVQ-SCDs outperform corresponding counterparts and can be used to enable beyond 10 Pb/s serial optical transport over spatial division multiplexing (SDM) fibers as well as beyond 1 Pb/s transport over SMFs. The proposed OVQ-SCD-based hybrid multidimensional coded modulation scheme can simultaneously solve the problems related to the limited bandwidth of information-infrastructure, high energy consumption, and heterogeneity of network segments; while enabling elastic and dynamic bandwidth allocation.

## Iterative Decoding Algorithms for a Class of Non-Binary Two-Step Majority-Logic Decodable Cyclic Codes

- **ID**: ieee:6805582
- **Type**: journal
- **Published**: 2014
- **Authors**: H. -C. Chang, H. -C. Chang
- **PDF**: https://ieeexplore.ieee.org/document/6805582
- **Abstract**: This paper presents two iterative decoding algorithms for a class of non-binary two-step majority-logic (NB-TS-MLG) decodable cyclic codes. A partial parallel decoding scheme is also introduced to provide a balanced trade-off between decoding speed and storage requirements. Unlike non-binary one-step MLG decodable cyclic codes, the Tanner graphs of which are 4-cycle-free, NB-TS-MLG decodable cyclic codes contain a large number of short cycles of length 4, which tend to degrade decoding performance. The proposed algorithms utilize the orthogonal structure of the parity-check matrices of the codes to resolve the degrading effects of the short cycles of length 4. Simulation results demonstrate that the NB-TS-MLG decodable cyclic codes decoded with the proposed algorithms offer coding gains as much as 2.5 dB over Reed-Solomon codes of the same lengths and rates decoded with either hard-decision or algebraic soft decision decoding.

## Channel Hardening-Exploiting Message Passing (CHEMP) Receiver in Large-Scale MIMO Systems

- **ID**: ieee:6781619
- **Type**: journal
- **Published**: 2014
- **Authors**: T. L. Narasimhan, A. Chockalingam
- **PDF**: https://ieeexplore.ieee.org/document/6781619
- **Abstract**: In this paper, we propose a multiple-input multiple-output (MIMO) receiver algorithm that exploits channel hardening that occurs in large MIMO channels. Channel hardening refers to the phenomenon where the off-diagonal terms of the HHH matrix become increasingly weaker compared to the diagonal terms as the size of the channel gain matrix H increases. Specifically, we propose a message passing detection (MPD) algorithm which works with the real-valued matched filtered received vector (whose signal term becomes HTHx, where x is the transmitted vector), and uses a Gaussian approximation on the off-diagonal terms of the HTH matrix. We also propose a simple estimation scheme which directly obtains an estimate of HTH (instead of an estimate of H), which is used as an effective channel estimate in the MPD algorithm. We refer to this receiver as the channel hardening-exploiting message passing (CHEMP) receiver. The proposed CHEMP receiver achieves very good performance in large-scale MIMO systems (e.g., in systems with 16 to 128 uplink users and 128 base station antennas). For the considered large MIMO settings, the complexity of the proposed MPD algorithm is almost the same as or less than that of the minimum mean square error (MMSE) detection. This is because the MPD algorithm does not need a matrix inversion. It also achieves a significantly better performance compared to MMSE and other message passing detection algorithms using MMSE estimate of H. Further, we design optimized irregular low density parity check (LDPC) codes specific to the considered large MIMO channel and the CHEMP receiver through EXIT chart matching. The LDPC codes thus obtained achieve improved coded bit error rate performance compared to off-the-shelf irregular LDPC codes.

## Multidimensional Optimal Signal Constellation Sets and Symbol Mappings for Block-Interleaved Coded-Modulation Enabling Ultrahigh-Speed Optical Transport

- **ID**: ieee:6844916
- **Type**: journal
- **Published**: 2014
- **Authors**: T. Liu, I. B. Djordjevic
- **PDF**: https://ieeexplore.ieee.org/document/6844916
- **Abstract**: In this paper, we introduce the optimal signal constellation design (OSCD) in both 2-D and multidimensional cases, which is obtained by minimization of mean square error of optimal source distribution. In addition, by analyzing block-interleaved coded modulation with iterative decoding, in which the bit error rate is reduced by iteration of extrinsic information between a multilevel/multidimensional demapper and an LDPC decoder, with the help of EXIT chart, we propose new mapping methods for OSCDs outperforming previously known ones. The simulation results show that optimized mappings for LDPC-coded OSCDs outperform natural mappings by 0.5 dB in 8-ary 2-D case and 0.6 dB in 16-ary 2-D case. Meanwhile, our proposed optimized mappings for 3-D-8-ary OSCD outperform natural mapping by 0.2 dB and sphere packing constellation by 0.5 dB in coherent optical OFDM few-mode fiber system.

## Low Complexity Optimal Soft-Input Soft-Output Demodulation of MSK Based on Factor Graph

- **ID**: ieee:6819011
- **Type**: journal
- **Published**: 2014
- **Authors**: S. Tong, D. Huang, Q. Guo +2
- **PDF**: https://ieeexplore.ieee.org/document/6819011
- **Abstract**: The soft-input–soft-output (SISO) MSK demodulator is a key component in the iterative receiver for coded MSK systems. To reduce the complexity of the optimal SISO MSK demodulator using the BCJR algorithm, a low complexity suboptimal MSK demodulator was developed by K. R. Narayanan et al. However, our investigation on the symmetric information rate of MSK with the suboptimal demodulator shows that it incurs a significant information rate loss compared with the BCJR demodulator. To avoid the rate loss, a low complexity SISO MSK demodulator is derived based on a new factor graph for MSK, which is found to have comparable complexity to the suboptimal demodulator. Moreover, the proposed algorithm is equivalent to the BCJR algorithm and thus achieves optimal performance. Simulation results for LDPC coded MSK systems are provided to demonstrate the effectiveness of the proposed algorithm.

## Channel Estimation for OFDM

- **ID**: ieee:6814271
- **Type**: journal
- **Published**: 2014
- **Authors**: Y. Liu, Z. Tan, H. Hu +2
- **PDF**: https://ieeexplore.ieee.org/document/6814271
- **Abstract**: Orthogonal frequency division multiplexing (OFDM) has been widely adopted in modern wireless communication systems due to its robustness against the frequency selectivity of wireless channels. For coherent detection, channel estimation is essential for receiver design. Channel estimation is also necessary for diversity combining or interference suppression where there are multiple receive antennas. In this paper, we will present a survey on channel estimation for OFDM. This survey will first review traditional channel estimation approaches based on channel frequency response (CFR). Parametric model (PM)-based channel estimation, which is particularly suitable for sparse channels, will be also investigated in this survey. Following the success of turbo codes and low-density parity check (LDPC) codes, iterative processing has been widely adopted in the design of receivers, and iterative channel estimation has received a lot of attention since that time. Iterative channel estimation will be emphasized in this survey as the emerging iterative receiver improves system performance significantly. The combination of multiple-input multiple-output (MIMO) and OFDM has been widely accepted in modern communication systems, and channel estimation in MIMO-OFDM systems will also be addressed in this survey. Open issues and future work are discussed at the end of this paper.

## 2013 IEEE Information Theory Society Paper Award

- **ID**: ieee:6690279
- **Type**: journal
- **Published**: 2014
- **Authors**: 
- **PDF**: https://ieeexplore.ieee.org/document/6690279
- **Abstract**: The recipients of the 2013 IEEE Information Theory Society Paper Award are Shrinivas Kudekar, Thomas J. Richardson, and Rudiger L. Urbanke, for the paper "Threshold saturation via spatial coupling: Why convolutional LDPC ensembles perform so well over the BEC," which appeared in the IEEE Transactions on Information Theory, vol. 57, no. 2, pp. 803-834, February 2011.

## New iterative decoding algorithms of 2D product block codes

- **ID**: ieee:6916585
- **Type**: conference
- **Published**: 17-19 Jan.
- **Authors**: Abdeslam Ahmadi, Hussain Ben-Azza, Faissal El Bouanani
- **PDF**: https://ieeexplore.ieee.org/document/6916585
- **Abstract**: This paper presents four new iterative decoders for two dimensional product block codes (2D-PBC) based on Genetic Algorithms. Each of these iterative decoders runs in parallel on a number of processors connected by a network. They have almost the same complexity as the conventional iterative decoder, but their performances are improved since at each iteration, they trap the better of extrinsic information computed by the elementary decoders running simultaneously on all processors.

## Parametric curve for data reconstruction method for reliable communication

- **ID**: ieee:6914445
- **Type**: conference
- **Published**: 15-18 Jan.
- **Authors**: Agi Prasetiadi, Dwi Agung Nugroho, Dong-Seong Kim
- **PDF**: https://ieeexplore.ieee.org/document/6914445
- **Abstract**: This paper proposes a method to reconstruct data using parametric curve called Bezier curve. The proposed method suggests the possibility to approximate the damaged data, which have been processed by the error correction scheme. By using the Bezier curve the transmitted data which damaged is reconstructed. This method provides a smoothing effect on damaged data.

## End-to-End Energy Modeling and Analysis of Long-Haul Coherent Transmission Systems

- **ID**: ieee:6837441
- **Type**: journal
- **Published**: 15 Sept.15
- **Authors**: Bipin Sankar Gopalakrishna Pillai, Behnam Sedighi, Kyle Guan +4
- **PDF**: https://ieeexplore.ieee.org/document/6837441
- **Abstract**: In this paper, we model and analyze the end-to-end energy consumption of 100-Gbps coherent long-haul transmission systems. In particular, we investigate the impact of forward error correction (FEC) on the end-to-end energy consumption. We compare the energy efficiency of commonly used modulation formats in 100-Gbps transmission, namely dual polarization-quadrature phase-shift-keying (DP-QPSK) and dual polarization-16-quadrature amplitude modulation (DP-16-QAM), for different transmission distance and input bit error rate. Our energy model includes consumption of transmitter, booster, link amplifier as well as receiver. Compared with previous digital signal processing models, we provide a very detailed model that not only includes all the significant functional blocks (such as timing and carrier recovery, chromatic and polarization mode dispersion compensation, and FEC), but also takes into account impact of the number of samples processed every clock cycle and of operations other than multiplications. We have found that receiver energy consumption dominates in transmission systems that use electronic dispersion compensation over long transmission distances. Our results show that for short transmission distances where hard-decision decoding is adequate for both modulation formats, DP-16-QAM is more energy efficient than DP-QPSK. However, as the transmission distance increases, the energy saving due to the low symbol rate of DP-16-QAM is offset by the energy consumption of soft-decision decoding. In this case, the two modulation formats have approximately similar energy consumption.

## Iterative Receiver for Hybrid Asymmetrically Clipped Optical OFDM

- **ID**: ieee:6901211
- **Type**: journal
- **Published**: 15 Nov.15,
- **Authors**: Qi Wang, Zhaocheng Wang, Linglong Dai
- **PDF**: https://ieeexplore.ieee.org/document/6901211
- **Abstract**: This paper proposes an iterative receiver to enhance the performance of hybrid asymmetrically clipped optical orthogonal frequency division multiplexing (HACO-OFDM) in optical wireless communication systems. In HACO-OFDM scheme, asymmetrically clipped optical OFDM (ACO-OFDM) and pulse-amplitude-modulated discrete multitone (PAM-DMT) signals are transmitted simultaneously, which is more spectrally efficient compared with ACO-OFDM and PAM-DMT. However, the existing HACO-OFDM receiver directly recovers the signals in the frequency domain, which could not eliminate the interference thoroughly between ACO-OFDM and PAM-DMT signals and limits its performance. In our proposed receiver, the ACO-OFDM and PAM-DMT signals are detected in the frequency domain and regenerated in the time domain. After that, they are subtracted from the received signals iteratively. Thus, ACO-OFDM and PAM-DMT signals can be distinguished. By taking advantage of the signal symmetry properties of ACO-OFDM and PAM-DMT in the time domain, pairwise clipping is utilized to further reduce the effect of noise and estimation error, resulting in improved performance. In addition, unequal power allocation is proposed to guarantee that ACO-OFDM and PAM-DMT signals have similar performance in HACO-OFDM systems. Simulation results show that the proposed method provides significant signal-to-noise ratio gain over the conventional receiver for both equal and unequal power allocations at the cost of slightly increased complexity.

## Staircase Codes With 6% to 33% Overhead

- **ID**: ieee:6787025
- **Type**: journal
- **Published**: 15 May15, 
- **Authors**: Lei M. Zhang, Frank R. Kschischang
- **PDF**: https://ieeexplore.ieee.org/document/6787025
- **Abstract**: We design staircase codes with overheads between 6.25% and 33.3% for high-speed optical transport networks. Using a reduced-complexity simulation of staircase coded transmission over the BSC, we select code candidates from within a limited parameter space. Software simulations of coded BSC transmission are performed with algebraic component code decoders. The net coding gain of the best code designs are competitive with the best known hard-decision decodable codes over the entire range of overheads. At 20% overhead, staircase codes are within 0.92 dB of BSC capacity at a bit error-rate of $10^{-15}$. Decoding complexity and latency of the new staircase codes are also significantly reduced from existing hard-decision decodable schemes.

## A Silicon Photonic Integrated Packaged Coherent Receiver Front-End For Soft-Decision Decoding

- **ID**: ieee:6937063
- **Type**: journal
- **Published**: 15 Dec.15,
- **Authors**: Meer Nazmus Sakib, Mohammed Shafiqul Hai, Odile Liboiron-Ladouceur
- **PDF**: https://ieeexplore.ieee.org/document/6937063
- **Abstract**: In this paper, a packaged integrated coherent receiver and optical front-end for soft decision based on 25 Gbaud/s quadrature phase-shift keying (QPSK) is investigated for on-chip applications. The front-end consists of a 90° hybrid, balanced photodetectors, and unbalanced couplers monolithically integrated in a CMOS compatible silicon-on-insulator technology. The silicon photonic device is packaged onto a ceramic substrate with RF and dc connectors. The proposed front-end is an example of integration of system on chip. The integrated solution is able to provide 6.2 dB performance improvements over uncoded system without error correction. The front-end outperforms optical system with hard-decision forward error correction by 2.2 dB at the BER of 10-7.

## Status and Recent Advances on Forward Error Correction Technologies for Lightwave Systems

- **ID**: ieee:6805157
- **Type**: journal
- **Published**: 15 Aug.15,
- **Authors**: Andreas Leven, Laurent Schmalen
- **PDF**: https://ieeexplore.ieee.org/document/6805157
- **Abstract**: Since the introduction of coherent transponders, forward error correction based on soft decision is now established in optical communication. In this paper, we give a tutorial-style introduction of one class of commonly used codes, namely low-density parity-check (LDPC) codes. Also we discuss new developments such as convolutional LDPC codes and show how they can be employed as potential candidates for future optical communication systems.

## Bandwidth-Variable Transceivers based on Four-Dimensional Modulation Formats

- **ID**: ieee:6803879
- **Type**: journal
- **Published**: 15 Aug.15,
- **Authors**: Johannes Karl Fischer, Saleem Alreesh, Robert Elschner +4
- **PDF**: https://ieeexplore.ieee.org/document/6803879
- **Abstract**: In this invited contribution, we discuss technology options for bandwidth-variable transceivers which are key components for the realization of flexible software-defined optical networking. Bandwidth-variable transceivers enable the software-controlled adaptation of physical layer parameters such as transmitted bit rate, spectral efficiency and transparent reach according to the traffic demands at hand. In particular, we focus on recent advances in four-dimensional modulation formats and in modulation format transparent data-aided digital signal processing. It is argued that four-dimensional modulation formats present an attractive complement to conventional polarization-multiplexed formats in the context of bandwidth-variable transceivers, where they enable a smooth transition with respect to spectral efficiency while requiring marginal additional hardware effort. Results of numerical simulations and experiments supporting this statement are presented. For the cost-efficient hardware implementation of bandwidth-variable transceivers supporting several polarization-multiplexed and four-dimensional modulation formats, digital signal processing algorithms are required which operate format transparent and consume little hardware resources. We discuss data-aided signal processing as one possible option, in particular with respect to carrier frequency recovery and channel estimation in combination with frequency domain equalization.

## Simplified variable-scaled min sum LDPC decoder for irregular LDPC codes

- **ID**: ieee:6940497
- **Type**: conference
- **Published**: 10-13 Jan.
- **Authors**: Ahmed A. Emran, Maha Elsabrouty
- **PDF**: https://ieeexplore.ieee.org/document/6940497
- **Abstract**: Min-Sum decoding is widely used for decoding LDPC codes in many modern digital video broadcasting decoding due to its relative low complexity and robustness against quantization error. However, the suboptimal performance of the Min-Sum affects the integrated performance of wireless receivers. In this paper, we present the idea of adapting the scaling factor of the Min-Sum decoder with iterations through a simple approximation. For the ease of implementation the scaling factor can be changed in a staircase fashion. The stair step is designed to optimize the decoder performance and the required storage for its different values. The variable scaling factor proposed algorithm produces a nontrivial improvement of the performance of the Min-Sum decoding as verified by simulation results.

## Efficient implementation of enhanced min-sum algorithm for DVB-S2 LDPC decoder

- **ID**: ieee:6776078
- **Type**: conference
- **Published**: 10-13 Jan.
- **Authors**: Sung Ik Park, Heung Mook Kim, Jeongchang Kim
- **PDF**: https://ieeexplore.ieee.org/document/6776078
- **Abstract**: This paper proposes an efficient implementation of enhanced min-sum algorithm (EMSA) for DVB-S2 LDPC decoding. In order to minimize complexity of check node update, the proposed method uses forward and backward algorithm. Simulation results show that the EMSA does not cause serious performance degradation, as compared with sum-product algorithm when decoder input is 9-bit quantized.

## Improvement on a block-serial fully-overlapped QC-LDPC decoder for IEEE 802.11n

- **ID**: ieee:6776079
- **Type**: conference
- **Published**: 10-13 Jan.
- **Authors**: Chu Yu, Ho-Sheng Chuang, Bor-Shing Lin +2
- **PDF**: https://ieeexplore.ieee.org/document/6776079
- **Abstract**: This paper presents a block-serial fully-overlapped Quasi-Cyclic Low Density Parity Check (QC-LDPC) decoder for IEEE 802.11n. Based on the circuit retiming and message bypassing techniques, this decoder effectively improved the previous work proposed by Xiang et al. with an 11% clock-rate increase and a 3% decoding time reduction on average. Moreover, the proposed chip spends about 3.67 mm in 90 nm CMOS technology, its power approximately consumes 171 mW at 250 MHz, and throughput of the proposed design can reach 672 Mbps.

## Flexible Optical Networks: An Energy Efficiency Perspective

- **ID**: ieee:6842600
- **Type**: journal
- **Published**: 1 Nov.1, 2
- **Authors**: Hamid Khodakarami, Bipin Sankar Gopalakrishna Pillai, Behnam Sedighi +1
- **PDF**: https://ieeexplore.ieee.org/document/6842600
- **Abstract**: High energy efficiency is expected to become a mandatory design criterion in optical networks of the future. This paper investigates schemes for enhancing the energy efficiency of core optical networks based on multicarrier transmission. Such networks of the future will incorporate flexible techniques, namely: 1) adaptive modulation and coding, 2) flexible spectrum allocation, 3) wavelength conversion, and 4) traffic grooming. We investigate the problem of energy efficient routing and spectrum allocation in core optical networks incorporating these flexible techniques. We propose a heuristic solution that provides an energy minimized design of long-haul optical networks by avoiding under-utilization of network resources such as optical fibers, transponders, and amplifiers. A fixed architecture that does not employ the aforementioned flexible techniques is used as a benchmark for comparison. The numerical results in the west European (24-node US) core optical network show that the energy efficiency of the flexible architecture can outperform the fixed architecture by a factor of 4.2 (6.4) for low and 1.8 (1.9) for high traffic demands, respectively.

## Dimensioning BCH Codes for Coherent DQPSK Systems With Laser Phase Noise and Cycle Slips

- **ID**: ieee:6872779
- **Type**: journal
- **Published**: 1 Nov.1, 2
- **Authors**: Miu Yoong Leong, Knud J. Larsen, Gunnar Jacobsen +3
- **PDF**: https://ieeexplore.ieee.org/document/6872779
- **Abstract**: Forward error correction (FEC) plays a vital role in coherent optical systems employing multi-level modulation. However, much of coding theory assumes that additive white Gaussian noise (AWGN) is dominant, whereas coherent optical systems have significant phase noise (PN) in addition to AWGN. This changes the error statistics and impacts FEC performance. In this paper, we propose a novel semianalytical method for dimensioning binary Bose-Chaudhuri-Hocquenghem (BCH) codes for systems with PN. Our method involves extracting statistics from pre-FEC bit error rate (BER) simulations. We use these statistics to parameterize a bivariate binomial model that describes the distribution of bit errors. In this way, we relate pre-FEC statistics to post-FEC BER and BCH codes. Our method is applicable to pre-FEC BER around $10^{-3}$ and any post-FEC BER. Using numerical simulations, we evaluate the accuracy of our approach for a target post-FEC BER of  $10^{-5}$. Codes dimensioned with our bivariate binomial model meet the target within 0.2-dB signal-to-noise ratio.

## Programmable Transponder, Code and Differentiated Filter Configuration in Elastic Optical Networks

- **ID**: ieee:6805143
- **Type**: journal
- **Published**: 1 June1, 2
- **Authors**: Nicola Sambo, Gianluca Meloni, Francesco Paolucci +5
- **PDF**: https://ieeexplore.ieee.org/document/6805143
- **Abstract**: Next generation optical networks will require high levels of flexibility both at the data and control planes, being able to fit rate, bandwidth, and optical reach requirements of different connections. Optical transmission should be able to support very high rates (e.g., 1 Tb/s) and to be distance adaptive while optimizing spectral efficiency (i.e., the information rate transmitted over a given bandwidth). Similarly, the control plane should be capable of performing effective routing and spectrum assignment as well as proper selection of the transmission parameters (e.g., modulation format) depending on the required optical reach. In this paper we present and demonstrate a software-defined super-channel transmission based on time frequency packing and on the proposed differentiated filter configuration (DFC). Time frequency packing is a technique able to achieve high spectral efficiency even with low-order modulation formats (e.g., quadrature phase-shift keying). It consists in sending pulses that overlap in time or frequency or both to achieve high spectral efficiency. Coding and detection are properly designed to account for the introduced inter-symbol and inter-carrier interference. We present a software defined network (SDN) controller that sets transmission parameters (e.g., code rate) both at the transmitter and the receiver side. In particular, at the transmitter side, a programmable encoder adding redundancy to the data is controlled by SDN. At the receiver side, the digital signal processing is set by SDN based on the selected transmission parameters (e.g., code rate). Thus, extensions to the OpenFlow architectures are presented to control super-channel transmission based on time frequency packing. Then, the SDN-based DFC is proposed. According to DFC, the passband of the filters traversed by the same connection can be configured to different values. Experiments including data and control planes are shown to demonstrate the feasibility of optical-reach-adaptive super-channel at 1 Tb/s controlled by extended OpenFlow. Then, the effectiveness of the proposed SDN-based DFC is demonstrated in a testbed with both wavelength selective switches and spectrum selective switches, where filters traversed by a connection requires different passband values. Extended OpenFlow messages for time frequency packing and supporting DFC have been captured and shown in the paper.

## Trading Regeneration and Spectrum Utilization in Code-Rate Adaptive Flexi-Grid Networks

- **ID**: ieee:6905711
- **Type**: journal
- **Published**: 1 Dec.1, 2
- **Authors**: Isabella Cerutti, Francesca Martinelli, Nicola Sambo +2
- **PDF**: https://ieeexplore.ieee.org/document/6905711
- **Abstract**: Introduced to improve the spectral efficiency, time-frequency packing technique allows the exploitation of different code rates, leading to different levels of spectral utilization and all-optical reach. To ensure quality of transmission of the optical signal, opto-electronic regeneration must be used to propagate the transmission beyond the maximum optical reach and can inherently offer conversion of spectrum and code rate. In this way, multiple code rates can be enabled in optical networks, leading to a flexible design in which spectrum utilization and regeneration can be properly optimized and traded. This paper addresses for the first time the joint problem of selecting the code rate, the regeneration nodes, the spectrum allocation and the route for the requested lightpaths in an optical network with a flexi-grid. A genetic algorithm is proposed that balances the contrasting objectives of minimizing the regeneration nodes and the spectrum utilization. Results show that when regeneration nodes are minimized, code-rate adaptation is able to reduce the regeneration nodes as well as the spectrum utilization with respect to rate-fixed optical networks. In general, a balance of the two contrasting objectives is preferred to achieve a low resource utilization.

## Pilot-Tone Assisted Log-Likelihood Ratio for LDPC Coded CO-OFDM System

- **ID**: ieee:6826532
- **Type**: journal
- **Published**: 1 Aug.1, 2
- **Authors**: Shengjiao Cao, Pooi-Yuen Kam, Changyuan Yu +1
- **PDF**: https://ieeexplore.ieee.org/document/6826532
- **Abstract**: Pilot-tone assisted log-likelihood ratio (PT-LLR) is derived for low-density parity-check coded, coherent optical orthogonal frequency division multiplexing systems in the presence of linear phase noise. The knowledge of common phase error (CPE) obtained from the pilot-tone is incorporated into the new LLR metric, which eliminates the need for prior CPE estimation and compensation. We compare our metric with the conventional LLR (C-LLR) through extensive simulation using their approximate versions (APT-LLR, AC-LLR). APT-LLR has the same order of complexity as AC-LLR while it outperforms AC-LLR for higher order modulation formats (16-QAM, 64-QAM) at smaller pilot-tone-to-signal power ratios. In addition, we show that with the help of time-domain blind intercarrier interference mitigation, both metrics perform better in the presence of larger laser linewidth.

## Parity Check Encoded QPSK for Rate Adaptation in Coherent DSP-Based Receivers

- **ID**: ieee:6853387
- **Type**: journal
- **Published**: 1 Aug.1, 2
- **Authors**: Timo Pfau, Jeffrey Lee, Noriaki Kaneda
- **PDF**: https://ieeexplore.ieee.org/document/6853387
- **Abstract**: An ultrashort rate-1/2 parity check (PC) code is used to switch the net data rate of a coherent quadrature phase shift keying (QPSK) transmission system to the equivalent of a binary phase shift keying (BPSK) system. Simulation results of PC encoded-QPSK show an improvement in receiver sensitivity of 0.8 dB over BPSK at the soft-FEC threshold of BER  \(=2\times 10^{-2}\) . In addition, the code allows establishing an absolute phase reference at the receiver; i.e., differential coding is not required.
