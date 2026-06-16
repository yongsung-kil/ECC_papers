# IEEE Xplore — 2005-01


## Estimating the PDF of the SIC-MMSE equalizer output and its applications in designing LDPC codes with turbo equalization

- **ID**: ieee:1381445
- **Type**: journal
- **Published**: Jan. 2005
- **Authors**: K.R. Narayanan, Xiaodong Wang, Guosen Yue
- **PDF**: https://ieeexplore.ieee.org/document/1381445
- **Abstract**: We consider the analysis and design of low-density parity check (LDPC) codes for intersymbol interference (ISI) channels when used with soft interference cancellation plus linear minimum mean-square error filtering (SIC-MMSE) turbo equalization. We discuss techniques to compute the probability density function (pdf) of the extrinsic information at the output of the SIC-MMSE equalizer as a function of pdf of the input extrinsic information, channel impulse response, and the signal-to-noise ratio. For static ISI channels, we show that the output pdf can be modeled as symmetric Gaussian, and show that the mean can be evaluated without simulating the equalizer. For channels with long memory, we propose to use the unscented transform technique to compute the mean, which significantly reduces the computation required. Finally, for fading channels, we model the pdf by a mixture of symmetric Gaussian densities. Using these techniques, we are able to fairly accurately compute the thresholds for LDPC codes and design good irregular LDPC codes. Simulation results are in good agreement with the computed thresholds and the designed irregular LDPC codes outperform regular ones significantly.

## Regular and irregular progressive edge-growth tanner graphs

- **ID**: ieee:1377521
- **Type**: journal
- **Published**: Jan. 2005
- **Authors**: Xiao-Yu Hu, E. Eleftheriou, D.M. Arnold
- **PDF**: https://ieeexplore.ieee.org/document/1377521
- **Abstract**: We propose a general method for constructing Tanner graphs having a large girth by establishing edges or connections between symbol and check nodes in an edge-by-edge manner, called progressive edge-growth (PEG) algorithm. Lower bounds on the girth of PEG Tanner graphs and on the minimum distance of the resulting low-density parity-check (LDPC) codes are derived in terms of parameters of the graphs. Simple variations of the PEG algorithm can also be applied to generate linear-time encodeable LDPC codes. Regular and irregular LDPC codes using PEG Tanner graphs and allowing symbol nodes to take values over GF(q) (q>2) are investigated. Simulation results show that the PEG algorithm is a powerful algorithm to generate good short-block-length LDPC codes.

## Bit-reliability mapping in LDPC-coded modulation systems

- **ID**: ieee:1375222
- **Type**: journal
- **Published**: Jan. 2005
- **Authors**: Y. Li, W.E. Ryan
- **PDF**: https://ieeexplore.ieee.org/document/1375222
- **Abstract**: In this paper, we propose a reliability-based mapping strategy in LDPC-coded modulation systems. Compared to conventional mapping methods, this strategy gives a 0.15 dB - 0.2 dB performance improvement with no added complexity. Extrinsic information transfer (EXIT) chart analyses are used to explain the reason for this improvement. LDPC-coded modulation systems with gray and natural labeling are studied. We show that the performances of gray-labeled systems are always superior.

## Verification-based decoding for packet-based low-density parity-check codes

- **ID**: ieee:1377496
- **Type**: journal
- **Published**: Jan. 2005
- **Authors**: M.G. Luby, M. Mitzenmacher
- **PDF**: https://ieeexplore.ieee.org/document/1377496
- **Abstract**: We introduce and analyze verification-based decoding for low-density parity-check (LDPC) codes, an approach specifically designed to manipulate data in packet-sized units. Verification-based decoding requires only linear time for both encoding and decoding and succeeds with high probability under random errors. We describe how to utilize code scrambling to extend our results to channels with errors controlled by an oblivious adversary.

## EXIT-chart properties of the highest-rate LDPC code with desired convergence behavior

- **ID**: ieee:1375239
- **Type**: journal
- **Published**: Jan. 2005
- **Authors**: M. Ardakani, T.H. Chan, F.R. Kschischang
- **PDF**: https://ieeexplore.ieee.org/document/1375239
- **Abstract**: We consider uniparametric LDPC decoding schemes, i.e., the class of decoding algorithms for which an extrinsic information transfer (EXIT) chart analysis of the decoder is exact. We treat the general case of code design for a desired convergence behavior and provide necessary conditions and sufficient conditions that the EXIT chart of the maximum rate low-density parity-check code must satisfy. Our results generalize some of the existing results for the binary erasure channel: our results apply to all uniparametric decoding schemes and they apply to any desired convergence behavior.

## Symmetric and asymmetric Slepian-Wolf codes with systematic and nonsystematic linear codes

- **ID**: ieee:1375242
- **Type**: journal
- **Published**: Jan. 2005
- **Authors**: N. Gehrig, P.L. Dragotti
- **PDF**: https://ieeexplore.ieee.org/document/1375242
- **Abstract**: We propose a constructive approach for distributed source coding of correlated binary sources using linear channel codes that can achieve any point of the Slepian-Wolf achievable rate region. Our approach is very intuitive and can be used with systematic and nonsystematic linear codes. Moreover, the proposed coding strategy can easily be extended to the case of more than two sources.

## Distributed Video Coding

- **ID**: ieee:1369699
- **Type**: journal
- **Published**: Jan. 2005
- **Authors**: B. Girod, A.M. Aaron, S. Rane +1
- **PDF**: https://ieeexplore.ieee.org/document/1369699
- **Abstract**: Distributed coding is a new paradigm for video compression, based on Slepian and Wolf's and Wyner and Ziv's information-theoretic results from the 1970s. This paper reviews the recent development of practical distributed video coding schemes. Wyner-Ziv coding, i.e., lossy compression with receiver side information, enables low-complexity video encoding where the bulk of the computation is shifted to the decoder. Since the interframe dependence of the video sequence is exploited only at the decoder, an intraframe encoder can be combined with an interframe decoder. The rate-distortion performance is superior to conventional intraframe coding, but there is still a gap relative to conventional motion-compensated interframe coding. Wyner-Ziv coding is naturally robust against transmission errors and can be used for joint source-channel coding. A Wyner-Ziv MPEG encoder that protects the video waveform rather than the compressed bit stream achieves graceful degradation under deteriorating channel conditions without a layered signal representation.

## Stochastic analysis of turbo decoding

- **ID**: ieee:1377494
- **Type**: journal
- **Published**: Jan. 2005
- **Authors**: M. Fu
- **PDF**: https://ieeexplore.ieee.org/document/1377494
- **Abstract**: This paper proposes a stochastic framework for dynamic modeling and analysis of turbo decoding. By modeling the input and output signals of a turbo decoder as random processes, we prove that these signals become ergodic when the block size of the code becomes very large. This basic result allows us to easily model and compute the statistics of the signals in a turbo decoder. Using the ergodicity result and the fact that a sum of lognormal distributions is well approximated using a lognormal distribution, we show that the input-output signals in a turbo decoder, when expressed using log-likelihood ratios (LLRs), are well approximated using Gaussian distributions. Combining the two results above, we can model a turbo decoder using two input parameters and two output parameters (corresponding to the means and variances of the input and output signals). Using this model, we are able to reveal the whole dynamics of a decoding process. We have discovered that a typical decoding process is much more intricate than previously known, involving two regions of attraction, several fixed points, and a stable equilibrium manifold at which all decoding trajectories converge. Some applications of the stochastic framework are also discussed, including a fast decoding scheme

## Coding approaches to fault tolerance in linear dynamic systems

- **ID**: ieee:1377502
- **Type**: journal
- **Published**: Jan. 2005
- **Authors**: C.N. Hadjicostis, G.C. Verghese
- **PDF**: https://ieeexplore.ieee.org/document/1377502
- **Abstract**: This paper discusses fault tolerance in discrete-time dynamic systems, such as finite-state controllers or computer simulations, with focus on the use of coding techniques to efficiently provide fault tolerance to linear finite-state machines (LFSMs). Unlike traditional fault tolerance schemes, which rely heavily-particularly for dynamic systems operating over extended time horizons-on the assumption that the error-correcting mechanism is fault free, we are interested in the case when all components of the implementation are fault prone. The paper starts with a paradigmatic fault tolerance scheme that systematically adds redundancy into a discrete-time dynamic system in a way that achieves tolerance to transient faults in both the state transition and the error-correcting mechanisms. By combining this methodology with low-complexity error-correcting coding, we then obtain an efficient way of providing fault tolerance to k identical unreliable LFSMs that operate in parallel on distinct input sequences. The overall construction requires only a constant amount of redundant hardware per machine (but sufficiently large k) to achieve an arbitrarily small probability of overall failure for any prespecified (finite) time interval, leading in this way to a lower bound on the computational capacity of unreliable LFSMs.

## Serial concatenated TCM with an inner accumulate code-part I: maximum-likelihood analysis

- **ID**: ieee:1391191
- **Type**: journal
- **Published**: Jan. 2005
- **Authors**: H.M. Tullberg, P.H. Siegel
- **PDF**: https://ieeexplore.ieee.org/document/1391191
- **Abstract**: We propose a serial concatenated trellis-coded modulation system using one or more inner rate-1 accumulate codes and a mapping to a higher order, Gray-labeled signal constellation. As outer codes, we consider repeat codes, single parity-check codes, and convolutional codes. We show that under maximum-likelihood decoding, there exists a signal-to-noise ratio threshold beyond which the bit-error probability goes to zero as the blocklength goes to infinity. We then evaluate the performance for finite blocklengths using a modified union bound. Computer simulations demonstrate that the proposed system, despite its use of a simple rate-1 inner code, achieves performance in additive white Gaussian noise and Rayleigh fading that is comparable to, or better than, that of more complex systems suggested in the literature.

## Tree LDPC codes for IEEE 802.16 broadband wireless Internet

- **ID**: ieee:1429863
- **Type**: conference
- **Published**: 8-12 Jan. 
- **Authors**: Jun Heo, Kyuhyuk Chung
- **PDF**: https://ieeexplore.ieee.org/document/1429863
- **Abstract**: This work presents a new tree-LDPC code, which has a structured parity check matrix, in the application of IEEE 802.16 broadband wireless Internet. The proposed tree-LDPC code shows better performance with low encoding complexity compared to the regular LDPC codes and RA codes.

## Irregular LDPC coded BICM in image transmission over Rayleigh fading channel

- **ID**: ieee:1405204
- **Type**: conference
- **Published**: 6-6 Jan. 2
- **Authors**: Piming Ma, Dongfeng Yuan
- **PDF**: https://ieeexplore.ieee.org/document/1405204
- **Abstract**: If the degree distribution is chosen carefully, the irregular LDPC codes can outperform the regular ones. In this paper, we proposed an LDPC coded BICM scheme in image transmission system to improve both efficiency and reliability. Simulation results show that LDPC codes are good coding schemes over fading channel in image communication. Simultaneously, irregular codes can obtain a code gain of about 0.7 dB than regular ones when BER is 10/sup -4/. So the irregular LDPC codes are more suitable for image transmission than the regular codes.

## Research on decoding of LDPC coded modulation in OFDM wireless communication system

- **ID**: ieee:1405205
- **Type**: conference
- **Published**: 6-6 Jan. 2
- **Authors**: Piming Ma, Dongfeng Yuan
- **PDF**: https://ieeexplore.ieee.org/document/1405205
- **Abstract**: This paper investigates a low-density parity-check (LDPC) coded orthogonal frequency-division multiplexing (OFDM) wireless communication system based on IEEE 802.11a standard. And an initialization algorithm is proposed for the decoding of LDPC coded modulation in OFDM system. The LDPC decoding procedure is simplified without the estimation of channel noise power. Simulation results show that this algorithm is effective and the decoding performance is satisfied when maximum iteration number is 10.

## Implementing LDPC decoding on network-on-chip

- **ID**: ieee:1383266
- **Type**: conference
- **Published**: 3-7 Jan. 2
- **Authors**: T. Theocharides, G. Link, N. Vijaykrishnan +1
- **PDF**: https://ieeexplore.ieee.org/document/1383266
- **Abstract**: Low-density parity check codes are a form of error correcting codes used in various wireless communication applications and in disk drives. While LDPC codes are desirable due to their ability to achieve near Shannon-limit communication channel capacity, the computational complexity of the decoder is a major concern. LDPC decoding consists of a series of iterative computations derived from a message-passing bipartite graph. In order to efficiently support the communication intensive nature of this application, we present a LDPC decoder architecture based on a network-on-chip communication fabric that provides a 1.2 Gbps decoded throughput rate for a 3/4 code rate, 1024-bit block LDPC code. The proposed architecture can be reconfigured to support other LDPC codes of different block sizes and code rates. We also propose two novel power-aware optimizations that reduce the power consumption by up to 30%.

## A soft error mitigation scheme for safety-critical computer systems

- **ID**: ieee:1408414
- **Type**: conference
- **Published**: 24-27 Jan.
- **Authors**: Y. Yu, B.W. Johnson
- **PDF**: https://ieeexplore.ieee.org/document/1408414
- **Abstract**: The simplest method of mitigating errors in memory/data stream is to employ information redundancy as the mitigation scheme. This paper presents two most commonly used error detection and correction codes, the parity check code and the Hamming code, are compared in order to achieve high reliability and safety for the memory word-line design of safety-critical applications.

## An FPGA implementation of low-density parity-check code decoder with multi-rate capability

- **ID**: ieee:1466451
- **Type**: conference
- **Published**: 21-21 Jan.
- **Authors**: Lei Yang, Manyuan Shen, Hui Liu +1
- **PDF**: https://ieeexplore.ieee.org/document/1466451
- **Abstract**: With superior error correction capability, low-density parity-check (LDPC) has initiated wide scale interests in wireless telecommunication fields. In the past, various structures of single code rate LDPC decoders have been implemented for different applications. However, in order to cover a wide range of service requirements and diverse interference conditions in wireless applications, LDPC decoders that can operate in both high and low code rates are desired. In this paper, a new multi-rate LDPC decoder architecture is presented and implemented in a Xilinx FPGA device. Through selection pins, three operating modes with the irregular 1/2 rate, regular 5/8 rate and regular 7/8 rate are supported. The measurement results show LDPC decoder can achieve BER below 10/sup -5/ at SNR of 1.4dB in the most critical case with the irregular 1/2 mode.
