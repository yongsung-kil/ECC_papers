# IEEE Xplore — 2021-07


## A Miniaturized LDPC Encoder: Two-Layer Architecture for CCSDS Near-Earth Standard

- **ID**: ieee:9336038
- **Type**: journal
- **Published**: July 2021
- **Authors**: Jiaming Liu, Quanyuan Feng
- **PDF**: https://ieeexplore.ieee.org/document/9336038
- **Abstract**: Quasi-cyclic low-density parity-check (QC-LDPC) codes, which have been adopted by the Consultative Committee for Space Data Systems (CCSDS), are widely used in Deep-Space (AR4JA) and Near-Earth (C2) communications. A large number of encoder architectures with CCSDS recommended standard have been proposed. But the existing architectures are not efficient enough in high-throughput implementations, many architectures have a lot of logical resources and registers. In this brief, we introduce a novel architecture with low resource utilization. A grouping algorithm is used to extract the common subexpressions (CS) of the encoding algorithm. Similar circuit structures are integrated through a two-layer architecture, which further reduces logical resources. For the special size of the generator's matrix, we introduce a preprocessing method. In addition, configuration registers are used to replace the control unit. Implemented and verified on FPGA, the proposed architecture achieves a throughput of 4.69 Gbps using only 1658 LUTs and 1038 FFs. Compared with the previous architectures, this architecture achieves lower resource utilization and multi-Gbps throughput.

## Learning to Decode Protograph LDPC Codes

- **ID**: ieee:9427170
- **Type**: journal
- **Published**: July 2021
- **Authors**: Jincheng Dai, Kailin Tan, Zhongwei Si +4
- **PDF**: https://ieeexplore.ieee.org/document/9427170
- **Abstract**: The recent development of deep learning methods provides a new approach to optimize the belief propagation (BP) decoding of linear codes. However, the limitation of existing works is that the scale of neural networks increases rapidly with the codelength, thus they can only support short to moderate codelengths. From the point view of practicality, we propose a high-performance neural min-sum (MS) decoding method that makes full use of the lifting structure of protograph low-density parity-check (LDPC) codes. By this means, the size of the parameter array of each layer in the neural decoder only equals the number of edge-types for arbitrary codelengths. In particular, for protograph LDPC codes, the proposed neural MS decoder is constructed in a special way such that identical parameters are shared by a bundle of edges derived from the same edge-type. To reduce the complexity and overcome the vanishing gradient problem in training the proposed neural MS decoder, an iteration-by-iteration (i.e., layer-by-layer in neural networks) greedy training method is proposed. With this, the proposed neural MS decoder tends to be optimized with faster convergence, which is aligned with the early termination mechanism widely used in practice. To further enhance the generalization ability of the proposed neural MS decoder, a codelength/rate compatible training method is proposed, which randomly selects samples from a set of codes lifted from the same base code. As a theoretical performance evaluation tool, a trajectory-based extrinsic information transfer (T-EXIT) chart is developed for various decoders. Both T-EXIT and simulation results show that the optimized MS decoding can provide faster convergence and up to 1dB gain compared with the plain MS decoding and its variants with only slightly increased complexity. In addition, it can even outperform the sum-product algorithm for some short codes.

## Shortening for LDPC-Coded Multi-User Systems

- **ID**: ieee:9386076
- **Type**: journal
- **Published**: July 2021
- **Authors**: Na Gao, Yin Xu, Yihang Huang +4
- **PDF**: https://ieeexplore.ieee.org/document/9386076
- **Abstract**: This letter explores shortening technology for achieving near Gaussian multiple access channel (GMAC) capacity in low-density parity-check coded multi-user systems. To optimize the shortening patterns, a hybrid extrinsic information transfer (H-EXIT) tool, which integrates EXIT and protograph-based EXIT, is firstly developed. Based on this analysis, H-EXIT priority (HEP) algorithm is proposed to facilitate the optimization of shortening patterns. It can be observed that columns with larger degrees are prior to be selected, which differs from those for point-to-point scenarios. Inspired by this finding, we further propose largest-column-degree priority (LCDP) algorithm, which narrows the selection space to lower the complexity while maintains a comparable performance. Extensive simulation results demonstrate the superiority of proposed shortening schemes from two aspects: 1) Proposed shortening can bring nonnegligible gain over unshortening with consistent sum rate; 2) HEP and LCDP algorithms outperform benchmark algorithms.

## Self-Corrected Belief-Propagation Decoder for Source Coding With Unknown Source Statistics

- **ID**: ieee:9411898
- **Type**: journal
- **Published**: July 2021
- **Authors**: Elsa Dupraz, Mohamed Yaoumi
- **PDF**: https://ieeexplore.ieee.org/document/9411898
- **Abstract**: This letter describes a practical Slepian-Wolf source coding scheme based on Low Density Parity Check (LDPC) codes. It considers the realistic setup where the parameters of the statistical model between the source and the side information are unknown. A novel Self-Corrected Belief-Propagation (SC-BP) algorithm is proposed in order to make the coding scheme robust to incorrect model parameters by introducing some memory inside the LDPC decoder. A Two Dimensional Density Evolution (2D-DE) analysis is then developed to predict the theoretical performance of the SC-BP decoder. Both the 2D-DE analysis and Monte-Carlo simulations confirm the robustness of the SC-BP decoder. The proposed solution allows for an important complexity reduction and shows a performance very close to existing methods which jointly estimate the model parameters and the source sequence.

## Probabilistic Shaping for Protograph LDPC-Coded Modulation by Residual Source Redundancy

- **ID**: ieee:9395483
- **Type**: journal
- **Published**: July 2021
- **Authors**: Chen Chen, Qiwang Chen, Lin Wang +2
- **PDF**: https://ieeexplore.ieee.org/document/9395483
- **Abstract**: Probabilistic amplitude shaping (PAS) has proved to be a promising way to achieve the shaping gain for an additive white Gaussian noise channel with a distribution matcher (DM). However, the DM schemes may suffer a rate loss and increase both complexity and latency, when they are not suited for the input bit stream with redundancy. In this paper, a novel PAS strategy is proposed for a joint source and channel coded modulation system, where the residual source redundancy after source coding can be exploited to obtain both shaping and coding gains. It is shown that the residual source redundancy can be controlled by choosing the row weight distribution for source code, thus making the probability distribution of the modulated symbols be optimized under an appropriate interleaver design. To guarantee the error-floor performance, the source code is constrained by predicting the probability distribution of source bits within target finite-length frames. By jointly designing source and channel codes, the residual source redundancy can also be exploited to achieve the coding gain. Compared with the state-of-the-art code pairs, the proposed code pairs have better error-floor performance, and achieve higher coding and shaping gains without suffering from the rate-loss and the latency caused by DM.

## Low-Density Parity-Check Coded Direct Sequence Spread Spectrum Receiver Based on Analog Probabilistic Processing

- **ID**: ieee:9444629
- **Type**: journal
- **Published**: July 2021
- **Authors**: Xuhui Ding, Jianping An, Zhe Zhao +2
- **PDF**: https://ieeexplore.ieee.org/document/9444629
- **Abstract**: Forward error correction (FEC) coding is an indispensable technique in the direct sequence spread spectrum (DS-SS) systems for satellite communication applications. Both the FEC and DS-SS can be regarded as specific cases of probabilistic computing based on analog circuits, which is expected to be a promising solution for power-limited scenarios. The combination of FEC and DS-SS techniques can provide sufficient link margin and robustness for communication systems. In this paper, a probabilistic receiver chain for the Low-Density Parity-Check (LDPC) coded DS-SS system is proposed. Generically, an $m$-sequence can be regarded as a codeword of cyclic linear codes. Similar to the decoding procedure of LDPC codes, the joint detection and decoding process of $m$-sequences can be performed by factor graph-based iterative message-passing algorithms (iMPAs). In terms of the iterative signal processing, we first present an improved approach of iterative stopping criterion which can reduce the average number of iteration by 90% for the LDPC decoding approach. Furthermore, a joint detection and decoding method is developed to provide quick synchronization of the $m$-sequence. Meanwhile, stopping criterion-based iMPAs are especially suitable for analog implementation with low complexity. Finally, cascading to the analog LDPC decoder, the implementation of the $m$-sequence detector is designed. The prototyping chip is fully integrated into a 0.35-$\mu\text{m}$ CMOS technology, which can achieve higher throughput than 3 ${\textbf {Gcps}}$ with a core chip area of 2.79 ${\textbf {mm}}^2$ and power consumption of 6.99 ${\textbf {mW}}$ for its core circuit. Experimental results demonstrate the effectiveness of our proposed receiver mechanism.

## Improving the Tradeoff Between Error Correction and Detection of Concatenated Polar Codes

- **ID**: ieee:9393971
- **Type**: journal
- **Published**: July 2021
- **Authors**: Min Jang, Joohyun Lee, Sang-Hyo Kim +1
- **PDF**: https://ieeexplore.ieee.org/document/9393971
- **Abstract**: Concatenated polar codes under successive cancellation list (SCL) decoding have excellent error-correction performance. However, their expected error-detection capability becomes degraded, when we increase the list size of the SCL decoder in order to improve their error-correction performance. In this paper, we propose a configuration design scheme for the SCL decoder and a post-decoding validation check scheme in order to provide a better tradeoff between error-detection and error-correction performance. Firstly, a configuration of the SCL decoder is designed to improve its own error detection capability. Specifically, a part of dynamic frozen bits (also called parity-check bits) is used for path checking during SCL decoding rather than their original purpose of use, path pruning. Furthermore, the number of paths to be checked by the applied cyclic redundancy check (CRC) code is limited. Secondly, a new metric corresponding to the correlation between the received signal vector and the decoded one is presented to check the validity of the decoding result. These proposed schemes are analyzed to provide a proper configuration of the SCL decoder and determine a threshold for post-decoding validation check. Numerical results show that a better tradeoff between error correction and detection is achieved, compared with conventional schemes.

## Rate-Compatible Codes via Recursive BMST for Content-Sharing in Intelligent Vehicular Network

- **ID**: ieee:9098040
- **Type**: journal
- **Published**: July 2021
- **Authors**: Shancheng Zhao, Jinming Wen, Xiujie Huang +1
- **PDF**: https://ieeexplore.ieee.org/document/9098040
- **Abstract**: Content-sharing is one of the major applications of vehicular networks. To fully utilize the spectrum and the connection time, rate-compatible codes are required when sharing content. In this paper, we present a simple and flexible method to construct low-complexity rate-compatible codes for content sharing. We first present a novel construction framework for rate-compatible codes via recursive block Markov superposition transmission (rBMST). In the proposed construction, the shared content is partitioned into equal-length data chunks and transmitted directly, while their replicas are taken as the inputs of a given number of parallel systematic encoders to generate parity-check chunks. These parity-check chunks are then transmitted in parallel in a recursive block Markov superposition transmission manner. The proposed construction is flexible in the sense that codes with arbitrary rates can be obtained by adjusting the number of parallel rBMST encoders and the number of randomly punctured bits. We show that the simplest construction, using repetition to generate the parity-check chunks, leads to high-performance and low-complexity rate-compatible rBMST (RC-rBMST) codes. Specifically, the extrinsic information transfer (EXIT) chart analysis shows that asymptotic thresholds of the repetition-based RC-rBMST (RB-RC-rBMST) codes are within 0.25 dB of the channel capacities for a wide range of coding rates. Numerical results are presented to confirm the advantages of the RB-RC-rBMST codes in performance and complexity. Particularly, the RB-RC-rBMST codes perform as well as BMST-R codes but with much lower computational complexities.

## On Doped SC-LDPC Codes for Streaming

- **ID**: ieee:9389745
- **Type**: journal
- **Published**: July 2021
- **Authors**: Roman Sokolovskii, Alexandre Graell i Amat, Fredrik Brännström
- **PDF**: https://ieeexplore.ieee.org/document/9389745
- **Abstract**: In streaming applications, doping improves the performance of spatially-coupled low-density parity-check (SC-LDPC) codes by creating reduced-degree check nodes in the coupled chain. We formulate a scaling law to predict the bit and block error rate of periodically-doped semi-infinite SC-LDPC code ensembles streamed over the binary erasure channel under sliding window decoding for a given finite component block length. The scaling law assumes that with some probability doping is equivalent to full termination and triggers two decoding waves; otherwise, decoding performs as if the coupled chain had not been doped at all. We approximate that probability and use the derived scaling laws to predict the error rates of SC-LDPC code ensembles in the presence of doping. The proposed scaling law provides accurate error rate predictions. We further use it to show that in streaming applications periodic doping can yield higher rates than periodic full termination for the same error-correcting performance.

## Fast Column Message-Passing Decoding of Low-Density Parity-Check Codes

- **ID**: ieee:9314911
- **Type**: journal
- **Published**: July 2021
- **Authors**: Saleh Usman, Mohammad M. Mansour
- **PDF**: https://ieeexplore.ieee.org/document/9314911
- **Abstract**: A new fast column message-passing (FCMP) schedule for decoding LDPC codes is presented and investigated in this brief. FCMP converges in half the number of iterations compared to existing serial decoding schedules, has a significantly lower computational complexity than residual-belief-propagation (RBP)-based schedules, and consumes less power compared to state-of-the-art schedules. An FCMP decoder architecture supporting IEEE 802.11ad (WiGig) LDPC codes is presented. The architecture is synthesized using the TSMC 40 nm CMOS technology node and operates at a clock frequency of 200 MHz. The decoder achieves a throughput of 8.4 Gbps while consuming 72 mW of power. This results in an energy efficiency of 8.6 pJ/bit, which is the best-reported energy-efficiency in the literature for a WiGig LDPC decoder.

## Capacity Optimality of AMP in Coded Systems

- **ID**: ieee:9446137
- **Type**: journal
- **Published**: July 2021
- **Authors**: Lei Liu, Chulong Liang, Junjie Ma +1
- **PDF**: https://ieeexplore.ieee.org/document/9446137
- **Abstract**: This paper studies a large random matrix system (LRMS) model involving an arbitrary signal distribution and forward error control (FEC) coding. We establish an area property based on the approximate message passing (AMP) algorithm. Under the assumption that the state evolution for AMP is correct for the coded system, the achievable rate of AMP is analyzed. We prove that AMP achieves the constrained capacity of the LRMS with an arbitrary signal distribution provided that a matching condition is satisfied. As a byproduct, we provide an alternative derivation for the constraint capacity of an LRMS using a proved property of AMP. We discuss realization techniques for the matching principle of binary signaling using irregular low-density parity-check (LDPC) codes and provide related numerical results. We show that the optimized codes demonstrate significantly better performance over un-matched ones under AMP. For quadrature phase shift keying (QPSK) modulation, bit error rate (BER) performance within 1 dB from the constrained capacity limit is observed.

## Modulated Sparse Superposition Codes for the Complex AWGN Channel

- **ID**: ieee:9433595
- **Type**: journal
- **Published**: July 2021
- **Authors**: Kuan Hsieh, Ramji Venkataramanan
- **PDF**: https://ieeexplore.ieee.org/document/9433595
- **Abstract**: This paper studies a generalization of sparse superposition codes (SPARCs) for communication over the complex additive white Gaussian noise (AWGN) channel. In a SPARC, the codebook is defined in terms of a design matrix, and each codeword is a generated by multiplying the design matrix with a sparse message vector. In the standard SPARC construction, information is encoded in the locations of the non-zero entries of the message vector. In this paper we generalize the construction and consider modulated SPARCs, where information is encoded in both the locations and the values of the non-zero entries of the message vector. We focus on the case where the non-zero entries take values from a phase-shift keying (PSK) constellation. We propose a computationally efficient approximate message passing (AMP) decoder, and obtain analytical bounds on the state evolution parameters which predict the error performance of the decoder. Using these bounds we show that PSK-modulated SPARCs are asymptotically capacity achieving for the complex AWGN channel, with either spatial coupling or power allocation. We also provide numerical simulation results to demonstrate the error performance at finite code lengths. These results show that introducing modulation to the SPARC design can significantly reduce decoding complexity without sacrificing error performance.

## Using List Decoding to Improve the Finite-Length Performance of Sparse Regression Codes

- **ID**: ieee:9398698
- **Type**: journal
- **Published**: July 2021
- **Authors**: Haiwen Cao, Pascal O. Vontobel
- **PDF**: https://ieeexplore.ieee.org/document/9398698
- **Abstract**: We consider sparse regression codes (SPARCs) over complex AWGN channels. Such codes can be efficiently decoded by an approximate message passing (AMP) decoder, whose performance can be predicted via so-called state evolution in the large-system limit. In this paper, we mainly focus on how to use concatenation of SPARCs and cyclic redundancy check (CRC) codes on the encoding side and use list decoding on the decoding side to improve the finite-length performance of the AMP decoder for SPARCs over complex AWGN channels. Simulation results show that such a concatenated coding scheme works much better than SPARCs with the original AMP decoder and results in a steep waterfall-like behavior in the bit-error rate performance curves. Furthermore, we apply our proposed concatenated coding scheme to spatially coupled SPARCs. Besides that, we also introduce a novel class of design matrices, i.e., matrices that describe the encoding process, based on circulant matrices derived from Frank or from Milewski sequences. This class of design matrices has comparable encoding and decoding computational complexity as well as very close performance with the commonly-used class of design matrices based on discrete Fourier transform (DFT) matrices, but gives us more degrees of freedom when designing SPARCs for various applications.

## Pruning and Quantizing Neural Belief Propagation Decoders

- **ID**: ieee:9281328
- **Type**: journal
- **Published**: July 2021
- **Authors**: Andreas Buchberger, Christian Häger, Henry D. Pfister +2
- **PDF**: https://ieeexplore.ieee.org/document/9281328
- **Abstract**: We consider near maximum-likelihood (ML) decoding of short linear block codes. In particular, we propose a novel decoding approach based on neural belief propagation (NBP) decoding recently introduced by Nachmani et al. in which we allow a different parity-check matrix in each iteration of the algorithm. The key idea is to consider NBP decoding over an overcomplete parity-check matrix and use the weights of NBP as a measure of the importance of the check nodes (CNs) to decoding. The unimportant CNs are then pruned. In contrast to NBP, which performs decoding on a given fixed parity-check matrix, the proposed pruning-based neural belief propagation (PB-NBP) typically results in a different parity-check matrix in each iteration. For a given complexity in terms of CN evaluations, we show that PB-NBP yields significant performance improvements with respect to NBP. We apply the proposed decoder to the decoding of a Reed-Muller code, a short low-density parity-check (LDPC) code, and a polar code. PB-NBP outperforms NBP decoding over an overcomplete parity-check matrix by 0.27–0.31 dB while reducing the number of required CN evaluations by up to 97%. For the LDPC code, PB-NBP outperforms conventional belief propagation with the same number of CN evaluations by 0.52 dB. We further extend the pruning concept to offset min-sum decoding and introduce a pruning-based neural offset min-sum (PB-NOMS) decoder, for which we jointly optimize the offsets and the quantization of the messages and offsets. We demonstrate performance 0.5 dB from ML decoding with 5-bit quantization for the Reed-Muller code.

## Capacity-Achieving Spatially Coupled Sparse Superposition Codes With AMP Decoding

- **ID**: ieee:9441022
- **Type**: journal
- **Published**: July 2021
- **Authors**: Cynthia Rush, Kuan Hsieh, Ramji Venkataramanan
- **PDF**: https://ieeexplore.ieee.org/document/9441022
- **Abstract**: Sparse superposition codes, also referred to as sparse regression codes (SPARCs), are a class of codes for efficient communication over the AWGN channel at rates approaching the channel capacity. In a standard SPARC, codewords are sparse linear combinations of columns of an i.i.d. Gaussian design matrix, while in a spatially coupled SPARC the design matrix has a block-wise structure, where the variance of the Gaussian entries can be varied across blocks. A well-designed spatial coupling structure can significantly enhance the error performance of iterative decoding algorithms such as Approximate Message Passing (AMP). In this paper, we obtain a non-asymptotic bound on the probability of error of spatially coupled SPARCs with AMP decoding. Applying this bound to a simple band-diagonal design matrix, we prove that spatially coupled SPARCs with AMP decoding achieve the capacity of the AWGN channel. The bound also highlights how the decay of error probability depends on each design parameter of the spatially coupled SPARC. An attractive feature of AMP decoding is that its asymptotic mean squared error (MSE) can be predicted via a deterministic recursion called state evolution. Our result provides the first proof that the MSE concentrates on the state evolution prediction for spatially coupled designs. Combined with the state evolution prediction, this result implies that spatially coupled SPARCs with the proposed band-diagonal design are capacity-achieving. Using the proof technique used to establish the main result, we also obtain a concentration inequality for the MSE of AMP applied to compressed sensing with spatially coupled design matrices. Finally, we provide numerical simulation results that demonstrate the finite length error performance of spatially coupled SPARCs. The performance is compared with coded modulation schemes that use LDPC codes from the DVB-S2 standard.

## Design of Successive cancellation List Decoding of Polar Codes

- **ID**: ieee:9489221
- **Type**: conference
- **Published**: 8-10 July 
- **Authors**: A.Albert Raj, M. Pooranasankari, S.Sri Abinayaa
- **PDF**: https://ieeexplore.ieee.org/document/9489221
- **Abstract**: Due to the introduction of 5G, the Polar codes have attracted researchers in the communication field. It is one of a linear block error-correcting codes. This is a kind of Information channel coding techniques with low-complexity in nature wherein the encoding and decoding operation will be performed. Moreover, when it is considered in theoretical prospective, this is considered as one of the capacitive achieving algorithm for a wide range of channel. Polar codes are shown to be instances of concatenated codes. It is proved that the effect of a polar code can be increased by showing the multistage decoding algorithm with log likelihood based Successive List decoding (SCL). As for as Frame error rate is concerned the SCL decoding is not an optimal solution. In this paper the performance of polar codes concatenated with CRC codes is presented and it is proved that it outperforms turbo or LDPC codes. The simulation result shows that with the sufficient amount of training this method can provide a lower frame-error rate for different code lengths.

## Counter Random Gradient Descent Bit-Flipping Decoder for LDPC Codes

- **ID**: ieee:9516718
- **Type**: conference
- **Published**: 7-9 July 2
- **Authors**: Keyue Deng, Hangxuan Cui, Jun Lin +1
- **PDF**: https://ieeexplore.ieee.org/document/9516718
- **Abstract**: Tabu-list random-penalty gradient descent bit-flipping (TRGDBF) is a hard-decision algorithm for decoding low-density parity-check (LDPC) codes, which offers a significant improvement in error correction. However, compared to the current gradient descent bit-flipping (GDBF) variants, it converges slower and has no obvious performance advantage unless enough iterations are allowed. To accelerate the convergence speed, this paper presents a counter random GDBF (CRGDBF) algorithm in which a bit is forbidden to flip in the next iteration after being flipped several times. Incorporating the random operation, the forbidden-mechanism shows a dynamic property, facilitating the decoder more efficiently to break trapping sets. Simulation results show that the CRGDBF can achieve up to 5 times better decoding performance than the TRGDBF algorithm within finite iterations. Additionally, an architecture is presented for implementing the CRGDBF algorithm, demonstrating it only brings limited hardware overhead compared to the TRGDBF.

## FPGA Implementation of LDPC Decoder Architecture for Wireless Communication Standards

- **ID**: ieee:9493380
- **Type**: conference
- **Published**: 5-7 July 2
- **Authors**: Ruslan Goriushkin, Pavel Nikishkin, Evgeny Likhobabin +1
- **PDF**: https://ieeexplore.ieee.org/document/9493380
- **Abstract**: This paper presents a decoder design for Quasi-Cyclic (QC) Low-Density Parity-Check (LDPC) codes. The design is parameterized and can be easily rebuilt to support various LDPC Parity-Check matrices taken from the WiMAX (IEEE 802.16e) and the WiFi (IEEE 802.11n) standards. New techniques such as parallelization of the decoding architecture cores are proposed. These cores calculate variable-to-check (VTC) and new check-to-variable (CTV) messages and also update posterior probabilities (APPs). The parallel multicore decoding architecture implies a prior shift of values based on the LDPC matrix and simultaneous calculation of values for the core. Our decoder is implemented on FPGAs of the Zynq-7000 Mini-ITX Evaluation Board (XC7Z100-2FFG900). The throughput of up to 1,2 GBit/s and the operation frequency of up to 240 MHz have been achieved.

## Performance Analysis of m-PSK/QAM Based on LDPC Code in Maritime Atmospheric Turbulence Channel

- **ID**: ieee:9866499
- **Type**: conference
- **Published**: 3-7 July 2
- **Authors**: Zhongli Yi, Fuzhai Wang, Zheng Yang +2
- **PDF**: https://ieeexplore.ieee.org/document/9866499
- **Abstract**: A LDPC-coded m-PSK/QAM communication system over maritime atmospheric turbulence channel is investigated. The performances of LDPC coded and uncoded with different modulation in turbulence channels are discussed and the design and deployment suggestions are given. © 2021 The Author(s)

## Combination of Multi-impairments Compensation and Decoding for LDPC-coded CO-OFDM via Deep Learning

- **ID**: ieee:9866227
- **Type**: conference
- **Published**: 3-7 July 2
- **Authors**: Ying Han, Yuanxiang Chen, Jia Fu +6
- **PDF**: https://ieeexplore.ieee.org/document/9866227
- **Abstract**: We propose a combination scheme of multi-impairment compensation and LDPC decoding based deep learning for LDPC-coded CO-OFDM system. Experiments show it can greatly reduce the BER and decoding complexity in different transmission scenarios.

## Probabilistic Shaped LDPC-coded 400G PM-64QAM DWDM Transmission in 50-GHz Grid

- **ID**: ieee:9866167
- **Type**: conference
- **Published**: 3-7 July 2
- **Authors**: Xiao Han, Yang Yue, Zhen Qu +2
- **PDF**: https://ieeexplore.ieee.org/document/9866167
- **Abstract**: Crosstalk tolerance of 400G PS-64QAM DWDM transmission in 50-GHz grid is investigated. In single-channel scenario, PS-64QAM outperforms uniform-64QAM by 0.6 dB, while PS-64QAM with optimized roll-off factor features a 0.9-dB gain in DWDM transmission regime. ©2021 The Author(s)

## Design of Protograph-based LDPC Codes for DVB-S2 Systems

- **ID**: ieee:9580405
- **Type**: conference
- **Published**: 28-30 July
- **Authors**: Runze Li, Jingyi Zhang, Pingping Chen +1
- **PDF**: https://ieeexplore.ieee.org/document/9580405
- **Abstract**: Since low-density parity-check (LDPC) codes have been studied and adopted in the DVB-S2 standard, many efforts have been made to improve their performance and optimize them up to the broadcasting standard. This paper proposes a family of protograph-based LDPC codes to provide a multi-rate coding for efficient DVB-S2 systems, considering low-complexity and excellent performance of the protograph codes. Moreover, we employ Bit Interleaved Code Modulation Iterative Decoding (BICM-ID) to enhance the performance of the ASK-modulated DVB systems. Both the protograph extrinsic information transfer (PEXIT) analysis and simulation results demonstrate the performance advantage of the proposed protograph-based LDPC codes over the conventional DVB-S2 codes for all the code rates. In particular, the proposed codes yield performance gains of more than 0.2 dB as compared to the conventional codes at high rates for 16-APSK modulations.

## Deep Learning Methods for Channel Decoding: A Brief Tutorial

- **ID**: ieee:9580304
- **Type**: conference
- **Published**: 28-30 July
- **Authors**: Kai Niu, Jincheng Dai, Kailin Tan +1
- **PDF**: https://ieeexplore.ieee.org/document/9580304
- **Abstract**: The recent development of deep learning methods demonstrates a new insight to optimize the decoding of linear codes. In this paper, we survey the typical neural network decoding methods, including data-driven and model-driven schemes. We investigate the design principle, algorithm mechanism, parameter assignment, and training process of these neural decoders for high-density parity check (HDPC), low-density parity-check (LDPC), and polar codes. Finally, we summarize the advantages of neural network decoding and point out some research directions in the future.

## Improved Time-Frequency Domain Linear Receiver for OFDM-Based OTFS

- **ID**: ieee:9580245
- **Type**: conference
- **Published**: 28-30 July
- **Authors**: Linfei Xu, Nan Li, Wei Xiang +4
- **PDF**: https://ieeexplore.ieee.org/document/9580245
- **Abstract**: Recently, a novel two-dimensional modulation technique termed orthogonal time frequency space modulation (OTFS) has been proposed for time- and frequency-selective wireless channels, which is designed to transform a time-varying multi-path fading channel into a time-invariant delay-Doppler (DD) channel. In this paper, we propose an improved time-frequency (TF) domain linear receiver for orthogonal frequency division multiplexing (OFDM) based OTFS systems. The proposed receiver uses the minimum mean square error (MMSE) equalizer in the TF domain considering inter-carrier interference, and implements channel normalization in the DD domain. As simulation results show, the proposed receiver can achieve a lower BER for the uncoded system, and also a BLER for the coded OTFS system using low density parity check codes (LDPC) in 5G systems. The complexity of the proposed receiver is almost the same as that of the conventional linear receiver in the TF domain, which is much lower than those of the DD domain receivers.

## Applications of Machine Learning for 5G Advanced Wireless Systems

- **ID**: ieee:9498754
- **Type**: conference
- **Published**: 28 June-2 
- **Authors**: Yingjun Zhou, Jiajun Chen, Man Zhang +2
- **PDF**: https://ieeexplore.ieee.org/document/9498754
- **Abstract**: Wireless communication is playing an important role in benefiting our daily lives. Fifth generation (5G) advanced wireless communication is anticipated to support various upcoming services. Moreover, machine learning (ML) is expected to optimize wireless systems by tackling complex problems which cannot be solved using traditional mathematical models. In this paper, applications of ML for 5G advanced wireless communication are introduced in conjunction with its research advances. Furthermore, this paper explores the challenges and future research directions of applying ML in 5G advanced wireless communication.

## Iterative Receiver of Uplink Massive MIMO Unsourced Random Access

- **ID**: ieee:9498916
- **Type**: conference
- **Published**: 28 June-2 
- **Authors**: Zijie Liang, Jianping Zheng
- **PDF**: https://ieeexplore.ieee.org/document/9498916
- **Abstract**: Massive MIMO un-sourced random access (URA) is a promising massive random access technique for massive machine-type communications. The conventional receiver of uplink URA consists of inner covariance-based multiuser detection (CB-MUD) and outer tree-based decoding, and its performance is highly dependent on the threshold used to determine the activity state of transmit codeword in CB-MUD. In general, this threshold is involved with multiple system parameters, and difficult to optimize. In this paper, an iterative receiver consisting of CB-MUD and outer decoding is proposed. In this iterative receiver, the successive interference cancellation (SIC) strategy is employed, where the covariance information associated with codewords decided in the former iteration is peeled off and the residual covariance is used for CB-MUD in the latter iteration. Noting that the sparsity increases with iterative number, in general, the performance of CB-MUD can be improved which is demonstrated by simulations. On the other hand, multiple iterations can relax the requirement of threshold selection. Concretely, an empirical formula for the threshold setting which decreases with iteration number is presented, and its robustness to system parameters is also verified by simulations.

## Library of Digital Communication Algorithms in the SimInTech Dynamic Modeling Environment. Opportunities and Prospects for Development

- **ID**: ieee:9494068
- **Type**: conference
- **Published**: 28 June-2 
- **Authors**: Aleksey A. Ovinnikov, Evgeny A. Likhobabin
- **PDF**: https://ieeexplore.ieee.org/document/9494068
- **Abstract**: This paper is devoted to the results of the creation of the Digital Communication Library, as well as to the implementation of the concept of multi-rate signal processing in the SimInTech dynamic modeling environment. When designing the library blocks, the computational complexity of the created algorithms was taken into account, which was reflected in the implementation language of the main functionality. Based on the developed elements, models were created that demonstrate the capabilities of the SimInTech system in the field of signal processing in applied and educational telecommunications tasks.

## Reliable Data Transport Protocol with FEC Mechanism for Erasure Channels

- **ID**: ieee:9522618
- **Type**: conference
- **Published**: 26-28 July
- **Authors**: Zsolt Alfred Polgar
- **PDF**: https://ieeexplore.ieee.org/document/9522618
- **Abstract**: Multimedia services generate an important part of the Internet traffic and the request for such services is increasing continuously. The characteristics of these services and their QoS requirements generate new challenges for the communication protocols. In order to cope with heavy congestions and the feedback implosion phenomenon Forward Error Correction (FEC) mechanisms were integrated into protocols controlling content distribution services and network coding techniques were proposed for peer-to-peer communications. The paper proposes a data transport protocol with integrated FEC mechanism intended to control the transmission between gateway nodes. The gateway level implementation allows protecting aggregated flows against packet drops generated by congestions and channel erasures. The proposed FEC enhanced data transport mechanism is combined with multipath transmissions between gateways, being exploited the diversity offered by such transmissions. A prototype protocol was implemented and experimentally evaluated on simulated transmission channels. The performance improvements of the proposed protocol in terms of packet erasure rate and jitter observed after decoding was demonstrated.

## A Review of Enabling Physical-Layer Technologies for Terahertz Communications

- **ID**: ieee:9549518
- **Type**: conference
- **Published**: 26-28 July
- **Authors**: Haiyao Xie, Feifei Wang, Yihao Zhang +2
- **PDF**: https://ieeexplore.ieee.org/document/9549518
- **Abstract**: With the explosive growth of mobile data demand, the contradiction between rate demand and spectrum shortage has become increasingly prominent. High-frequency communication systems such as millimeter wave and terahertz have gradually entered people/s field of vision, and they have been applied to satellite communications because of their vast bandwidth. The bottleneck of wireless bandwidth and spectrum utilization has become a vital issue for future wireless mobile networks, so terahertz communication has been proposed as an essential part of 5G and future 6G mobile networks. This article mainly investigates the enabling physical layer’s critical technologies under the background of terahertz communication, including the recent research and development trend of the high-frequency band and multi-antenna technology and coding technology. Finally, this article points out the challenges and research directions of the terahertz communication network’s physical layer technology in the future.

## Next Generation Mobile Broadcasting BICM Module to Improve T2-Lite System Robustness

- **ID**: ieee:9626794
- **Type**: conference
- **Published**: 25-26 July
- **Authors**: Hamzah Sabr Ghayyib, Samir Jasim Mohammed
- **PDF**: https://ieeexplore.ieee.org/document/9626794
- **Abstract**: Digital Video Broadcasting Next Generation Handheld (DVB-NGH) is the next-generation mobile TV broadcasting technology, which the DVB Project has developed. It’s the mobile extension of the high-performance Digital Video Broadcasting Terrestrial Second Generation (DVB-T2), with the most superior transmission technologies. One of the main modifications introduced by DVB-NGH is the advanced module of Bit-interleaved coded and modulation (BICM) based on a subset of DVB-T2 BICM elements. The diversity benefit gained by the modern features included in the DVB-NGH BICM module is examined in this study. This module incorporates two kinds of rotation schemes according to the specified coding rate: two-dimensional and four-dimensional rotated constellations (2D, 4D-RC). A comparison has been made between the acquired gain and the case of using the T2-Lite system’s fundamental BICM module, including the rotated constellations method. To confirm the efficiency of the created module, simulation results were done in MATLAB version R2020b using two fading channels: Rayleigh and 0 dB Echo. Finally, the acquired findings show a significant increase in system robustness when using the DVB-NGH BICM instead of the fundamental T2-Lite BICM module.

## AVX-512 Based, High-Throughput LDPC Decoders

- **ID**: ieee:9527002
- **Type**: conference
- **Published**: 23-25 July
- **Authors**: Jingxin Dai, Hang Yin, Sihan Liu +1
- **PDF**: https://ieeexplore.ieee.org/document/9527002
- **Abstract**: Low Density Parity Check (LDPC) codes can approach the Shannon limit in digital communication systems and have good error correction performance. At present, with the continuous development of communication technology, the demand for the throughput of the communication system is also increasing. In order to further improve the throughput of the LDPC decoder, this paper uses the AVX512 instruction set based on the parallel structure of the LDPC codes decoding algorithm, and proposes a design scheme based on the layered OMS-LDPC decoding algorithm. This solution can be implemented on a general-purpose processor (GPP) and achieve higher throughput. The experimental results show that, in the case of 10 iterations, the decoder based on the X86 processor supporting AVX512 can reach a throughput of 53Mbps to 131Mbps.

## Hardware Implementation Method of LDPC Efficient Decoding Based on FPGA

- **ID**: ieee:9603866
- **Type**: conference
- **Published**: 23-25 July
- **Authors**: Yuyang Ji, Yanjun Ji
- **PDF**: https://ieeexplore.ieee.org/document/9603866
- **Abstract**: In this paper,the logarithmic domain efficient decoding algorithm of LDPC code has been deeply studied,and the efficient algorithm with tree topology structure has been improved. The fixed-point representation and reweighting analysis of the receiving and processing information of LDPC code decoding has been carried out. At the same time,based on Quartus development software platform and Verilog HDL language,the efficient parallel decoding algorithm of regular LDPC code with length of 8designed by geometric construction method is designed, and the circuit design and simulation results of some main modules are given. The logic synthesis and implementation of the whole algorithm are carried out on StatixL EP2S60F484C3.The highest data processing rate is 10Mbps,and the error correction performance is ideal. After the reprocessing method is adopted,all the information in the decoding implementation process is the same standard,and there is no need for additional processing , which reduces the hardware complexity and calculation delay,and meets the needs of engineering implementation.

## Evaluation of Low-density parity-check code with 16-QAM OFDM in a time-varying channel

- **ID**: ieee:9530811
- **Type**: conference
- **Published**: 17-18 July
- **Authors**: A. Y. Kuti, A. E. Abdelkareem
- **PDF**: https://ieeexplore.ieee.org/document/9530811
- **Abstract**: In wireless networks, multipath interference in a time-varying channel is a significant and major challenge to effective data transmission. Bit error rate (BER) efficiency is improved using Forward Error Correction (FEC) coding, such as Low-Density Parity-Check (LDPC) coding. LDPC, which can accomplish near Shannon limit efficiency and has recently gained considerable attention because of these properties. The efficiency of an LDPC coded orthogonal frequency division multiplexing (OFDM) communication scheme for time-varying channels is evaluated in this paper. Then we study the bandwidth-efficient coded modulation system based on LDPC codes that have low implementation complexity and high BER efficiency. Simulation is used to investigate the effects of modulation and coding schemes on the performance of the LDPC code.The results show that the device can significantly boost the efficiency of wireless channels while lowering the code rate and improving overall system performance.

## Concatenated Coset Coding in a Multi-tone DHA FH OFDMA System with Order Statistics-based Reception

- **ID**: ieee:9530807
- **Type**: conference
- **Published**: 17-18 July
- **Authors**: Dmitry Osipov
- **PDF**: https://ieeexplore.ieee.org/document/9530807
- **Abstract**: A coded modulation scheme for a single-band multi-tone DHA FH OFDMA system that employs order statistics-based reception and a concatenation of coset codes is proposed. It is demonstrated that this coded modulation scheme provides profound performance gain over the conventional coded single-band multi-tone DHA FH OFDMA while preserving the effective transmission rate at the expense of minor complexity increase.

## A Study of Anti-jamming Pseudo Random Partial Band Hopping for OFDM Communication System

- **ID**: ieee:9513938
- **Type**: conference
- **Published**: 13-15 July
- **Authors**: Mohamed A. Soliman, Shady A Deraz, Walid M. Saad +1
- **PDF**: https://ieeexplore.ieee.org/document/9513938
- **Abstract**: Orthogonal frequency-division-multiplexing (OFDM approach) is regarded as one of the most well-known robust methods for mitigating jamming and exploiting hopping schemes across multiple-frequency sub-bands or bands, and is notable for its ability to improve the overall performance of wireless communication schemes, particularly in military communications. Combining the two methods should help to mitigate interference caused by accidental or deliberate jamming, particularly in military applications. The bit-error rate (BER) performance of an enhanced OFDM communication system over a multi-path Rayleigh fading channel is demonstrated in this paper using frequency sub-band hopping techniques in the presence of various types of jammers. The jamming scenarios vary from narrow band-jammer to barrage jammer depending on the jamming ratio are presented. Also, it includes two different hopping strategies, which are 3-band hopping and 6-band hopping. According to the simulation results, by increasing the amount of hopping sub-bands, the BER performance of the entire-regarded hopping schemes is significantly improved.

## Quasi-Cyclic Protograph-Based Raptor-Like LDPC Codes With Girth 6 and Shortest Length

- **ID**: ieee:9518125
- **Type**: conference
- **Published**: 12-20 July
- **Authors**: Farzane Amirzade, Mohammad-Reza Sadeghi, Daniel Panario
- **PDF**: https://ieeexplore.ieee.org/document/9518125
- **Abstract**: We consider multiple-edge QC-LDPC codes with a base matrix of large size. We propose a new method, the degree reduction method, to obtain exponent matrices of these codes which considerably reduces the complexity of the search algorithm. We also provide a necessary and sufficient condition to avoid 4-cycles from occurrence in the Tanner graph of codes obtained using our method. Then, we apply our method to quasi-cyclic protograph-based Raptor-Like LDPC (QC-PBRL-LDPC) codes whose base matrices are multiple-edge. Numerical results show that as a consequence of this study we can obtain the minimum lifting degree of QC-PBRL-LDPC codes with girth at least 6. Thus, the lengths of the obtained codes are much smaller than those of their counterpart short-length codes in the literature.

## Euclidean Distance Spectra of Irregular NB LDPC Coded QAM Signals with Optimized Mappings

- **ID**: ieee:9518126
- **Type**: conference
- **Published**: 12-20 July
- **Authors**: Irina E. Bocharova, Boris D. Kudryashov, Vitaly Skachek
- **PDF**: https://ieeexplore.ieee.org/document/9518126
- **Abstract**: Properties of non-binary (NB) LDPC codes used in conjunction with coded modulation systems are studied. It is observed that the performance of the NB LDPC coded transmission schemes strongly depends on the mapping between the NB symbols and the signal constellation points. The Euclidean distance spectra for an ensemble of random NB LDPC codes for specific mappings are derived. The simulation results for belief-propagation decoding in the coded modulation schemes with the NB QC-LDPC codes under different mappings are presented.

## Deep Learning-Based Bit Reliability Based Decoding for Non-binary LDPC Codes

- **ID**: ieee:9517790
- **Type**: conference
- **Published**: 12-20 July
- **Authors**: Taishi Watanabe, Takeo Ohseki, Kosuke Yamazaki
- **PDF**: https://ieeexplore.ieee.org/document/9517790
- **Abstract**: The bit reliability based (BRB) and weighted bit reliability based (wBRB) algorithms are non-binary low-density parity-check (LDPC) code decoding algorithms with an excellent tradeoff between computational complexity and performance. However, the performance of these algorithms needs further improvement. We apply deep learning to these algorithms. Weights are assigned to each edge of the Tanner graphs of the non-binary LDPC codes in the proposed algorithms. We demonstrate the effectiveness of applying deep learning to the BRB and wBRB algorithms in terms of implementation and performance. The proposed algorithms achieve an approximately 0.3 dB higher bit error rate performance than the original algorithms in the high SNR region. The increase in computational complexity and memory consumption does not significantly change the implementation of the algorithms.

## A Class of Non-Binary Doubly-Generalized LDPC codes for Moderate and High Code Rates

- **ID**: ieee:9518035
- **Type**: conference
- **Published**: 12-20 July
- **Authors**: Gada Rezgui, Iryna Andriyanova, Asma Maalaoui +1
- **PDF**: https://ieeexplore.ieee.org/document/9518035
- **Abstract**: In this paper, a new class of doubly-generalized LDPC codes is proposed. The particular point of the proposed construction is the presence of a small fraction of single parity-check codes at the variable nodes side. Together with the use of extended alphabets, the existence of such a fraction has been shown to improve the asymptotic decoding threshold, without harming the minimum distance behaviour of the code ensemble. Note that the improvement is more significant in cases where the code initially contains check nodes of high degrees, which corresponds to the region of moderate and high code rates.

## Nested LDPC Codes for Random Access Communication

- **ID**: ieee:9518171
- **Type**: conference
- **Published**: 12-20 July
- **Authors**: Yuxin Liu, Michelle Effros
- **PDF**: https://ieeexplore.ieee.org/document/9518171
- **Abstract**: This paper proposes a nested low-density parity-check (LDPC) code design. Combining this nested LDPC code with the random access coding strategy introduced by Yavas, Kostina, and Effros yields a random access LDPC (RA-LDPC) code for reliable communication in random access communication environments where neither the transmitters nor the receiver knows which or even how many transmitters wish to communicate at each moment. Coordination is achieved using sparse scheduled feedback. Bounds on the finite-blocklength performance of the RA-LDPC code under maximum likelihood (ML) decoding are derived using both error exponent and dispersion style analyses. Results include bounds on the penalty of the RA-LDPC code as a function of the LDPC code densities.

## Construction of Algebraic-Based Variable-Rate QC-LDPC Codes

- **ID**: ieee:9518132
- **Type**: conference
- **Published**: 12-20 July
- **Authors**: Huaan Li, Baoming Bai, Hengzhou Xu +1
- **PDF**: https://ieeexplore.ieee.org/document/9518132
- **Abstract**: In this paper, we concentrate on one algebraic-based quasi-cyclic low-density parity-check (QC-LDPC) code constructed from two subsets of a finite field and generalize it to propose a class of variable-rate QC-LDPC (VR-QC-LDPC) codes, whose parity-check matrices are nested horizontally and have constant number of rows. Thus the proposed codes are significant at least in terms of storage complexity and can be simply implemented. The constructed codes also inherit the original algebraic-based QC-LDPC codes and their exponent matrices can be obtained from two subsets of the given finite field. We hereby analyze the structural properties from the isomorphism perspective, and present some rules to significantly prune the size of search space and determine the non-isomorphic exponent matrices. By distinguishing the smaller quantities of non-isomorphic matrices with cycle property metric, we can easily construct a series of nested exponent matrices with better cycle distributions and obtain the VR-QC-LDPC codes. Numerical results demonstrate that the constructed codes have better iterative decoding performance within a range of code rates and decoding iterations.

## Necessary and Sufficient Girth Conditions for Tanner Graphs of Quasi-Cyclic LDPC Codes

- **ID**: ieee:9518241
- **Type**: conference
- **Published**: 12-20 July
- **Authors**: Roxana Smarandache, David G. M. Mitchell
- **PDF**: https://ieeexplore.ieee.org/document/9518241
- **Abstract**: This paper revisits the connection between the girth of a protograph-based LDPC code given by a parity-check matrix and the properties of powers of the product between the matrix and its transpose in order to obtain the necessary and sufficient conditions for a code to have given girth between 6 and 12, and to show how these conditions can be incorporated into simple algorithms to construct codes of that girth. To this end, we highlight the role that certain submatrices that appear in these products have in the construction of codes of desired girth. In particular, we show that imposing girth conditions on a parity-check matrix is equivalent to imposing conditions on a square submatrix obtained from it and we show how this equivalence is particularly strong for a protograph based parity-check matrix of variable node degree 2, where the cycles in its Tanner graph correspond one-to-one to the cycles in the Tanner graph of a square submatrix obtained by adding the permutation matrices (or products of these) in the composition of the parity-check matrix. We end the paper with exemplary constructions of codes with various girths and computer simulations. Although, we mostly assume the case of fully connected protographs of variable node degree 2 and 3, the results can be used for any parity-check matrix/protograph-based Tanner graph.

## Codes approaching the Shannon limit with polynomial complexity per information bit

- **ID**: ieee:9517788
- **Type**: conference
- **Published**: 12-20 July
- **Authors**: Ilya Dumer, Navid Gharavi
- **PDF**: https://ieeexplore.ieee.org/document/9517788
- **Abstract**: We consider codes for channels with extreme noise that emerge in various low-power applications. Simple LDPC codes with parity checks of weight 3 are first studied for any code dimension m → ∞. These codes form modulation schemes: they improve the original channel outputs for any SNR > -6 dB (per information bit) and gain 3 dB over uncoded modulation as SNR grows. However, they also have a floor on the output bit error rate (BER) irrespective of their length. Tight lower and upper bounds, which are virtually identical to simulation results, are then obtained for BER at any SNR. We also study a combined scheme that splits $m$ information bits into $b$ blocks and protects each with some polar code. Decoding moves back and forth between polar and LDPC codes, every time using a polar code of a higher rate. For m → ∞and a sufficiently large parameter b, this design yields a vanishing BER at any SNR above the Shannon limit of -1.59 dB and has complexity order of m log m per information bit.

## Some Results on Density Evolution of Nonbinary SC-LDPC Ensembles Over the BEC

- **ID**: ieee:9518021
- **Type**: conference
- **Published**: 12-20 July
- **Authors**: Mengnan Xu, Dan Zeng, Zhichao Sheng +2
- **PDF**: https://ieeexplore.ieee.org/document/9518021
- **Abstract**: In this paper, we present several theoretic results on density evolution (DE) for nonbinary spatially-coupled low-density parity-check (SC-LDPC) ensembles when the transmission takes place on the binary erasure channel (BEC). In specific, we establish the duality rule for entropy for the nonbinary variable-node (VN) and check-node (CN) operators in such a scenario. We define the partial order between densities and show that the VN and CN operators exhibit the property of partial order preservation. More importantly, we explicitly construct the potential functions for uncoupled and coupled DE recursions, the forms of which almost coincide with those for binary LDPC and SC-LDPC ensembles over general binary memoryless symmetric (BMS) channels. These theoretic findings greatly facilitate the proof of threshold saturation for nonbinary SC-LDPC ensembles on the BEC. Finally, we develop the threshold saturation theorem and its converse, following the lines established by S. Kumar et al.

## Capacity Optimality of AMP in Coded Systems

- **ID**: ieee:9518062
- **Type**: conference
- **Published**: 12-20 July
- **Authors**: Lei Liu, Chulong Liang, Junjie Ma +1
- **PDF**: https://ieeexplore.ieee.org/document/9518062
- **Abstract**: This paper studies a large random matrix system (LRMS) model involving an arbitrary signal distribution and forward error control (FEC) coding. We establish an area property based on the approximate message passing (AMP) algorithm. Under the assumption that the state evolution for AMP is correct for the coded system, the achievable rate of AMP is analyzed. We prove that AMP achieves the constrained capacity of the LRMS with an arbitrary signal distribution provided that a matching condition is satisfied. We provide related numerical results of binary signaling using irregular low-density parity-check (LDPC) codes. We show that the optimized codes demonstrate significantly better performance over unmatched ones under AMP. For quadrature phase shift keying (QPSK) modulation, bit error rate (BER) performance within 1 dB from the constrained capacity limit is observed.

## Proximal Decoding for LDPC-coded Massive MIMO Channels

- **ID**: ieee:9517988
- **Type**: conference
- **Published**: 12-20 July
- **Authors**: Tadashi Wadayama, Satoshi Takabe
- **PDF**: https://ieeexplore.ieee.org/document/9517988
- **Abstract**: We propose a novel optimization-based decoding algorithm for LDPC-coded massive MIMO channels. The proposed decoding algorithm is based on a proximal gradient method for solving an approximate maximum a posteriori (MAP) decoding problem. The key idea is the use of a code-constraint polynomial penalizing a vector far from a codeword as a regularizer in the approximate MAP objective function. The code proximal operator is naturally derived from code-constraint polynomials. The proposed algorithm, called proximal decoding, can be described by a simple recursion consisting of the gradient descent step for a negative log-likelihood function and the code proximal operation. Several numerical experiments show that the proposed algorithm outperforms known massive MIMO detection algorithms, such as an MMSE detector with belief propagation decoding.

## Trapping Set Analysis of Finite-Length Quantum LDPC Codes

- **ID**: ieee:9518154
- **Type**: conference
- **Published**: 12-20 July
- **Authors**: Nithin Raveendran, Bane Vasić
- **PDF**: https://ieeexplore.ieee.org/document/9518154
- **Abstract**: Iterative decoders for finite length quantum low-density parity-check (QLDPC) codes are impacted by short cycles, detrimental graphical configurations known as trapping sets (TSs) present in a code graph as well as symmetric degeneracy of errors. In this paper, we develop a systematic methodology by which quantum trapping sets (QTSs) can be defined and categorized according to their topological structure. Conventional definition of a TS from classical error correction is generalized to address the syndrome decoding scenario for QLDPC codes. We show that QTS information can be used to design better QLDPC code and decoder. For certain finite-length QLDPC codes, frame error rate improvements of two orders of magnitude in the error floor regime are demonstrated without needing any post-processing steps.

## Encoding and Decoding Construction D' Lattices for Power-Constrained Communications

- **ID**: ieee:9518122
- **Type**: conference
- **Published**: 12-20 July
- **Authors**: Fan Zhou, Arini Fitri, Khoirul Anwar +1
- **PDF**: https://ieeexplore.ieee.org/document/9518122
- **Abstract**: This paper focuses on the encoding and decoding of Construction D' coding lattices that can be used with shaping lattices for power-constrained channels. Two encoding methods and a decoding algorithm for Construction D' lattices are given. A design of quasi-cyclic low-density parity-check (QC-LDPC) codes to form Construction D' lattices is presented. This allows construction of nested lattice codes which are good for coding, good for shaping, and have low-complexity encoding and decoding. Numerical results using $E_{8},\ BW_{16}$ and Leech lattices for shaping a Construction D' lattice indicate that the shaping gains 0.65 dB, 0.86 dB and 1.03 dB are preserved, respectively.

## Iterative Detection and Decoding for Multiuser MIMO Systems with Low Resolution Precoding and PSK Modulation

- **ID**: ieee:9513787
- **Type**: conference
- **Published**: 11-14 July
- **Authors**: Erico S. P. Lopes, Lukas T. N. Landau
- **PDF**: https://ieeexplore.ieee.org/document/9513787
- **Abstract**: Low-resolution precoding techniques have gained considerable attention in the wireless communications area recently. Vital but hardly discussed in literature, discrete precoding in conjunction with channel coding is the subject of this study. Unlike prior studies, we propose three different soft detection methods and an iterative detection and decoding scheme that allow the utilization of channel coding in conjunction with low-resolution precoding. Besides an exact approach for computing the extrinsic information, we propose two approximations with reduced computational complexity. Numerical results based on PSK modulation and an LDPC block code indicate a superior performance as compared to the system design based on the common AWGN channel model in terms of bit-error-rate.

## Blind Joint Nonlinear Equalizer for mmWave Communications

- **ID**: ieee:9509989
- **Type**: conference
- **Published**: 10-11 July
- **Authors**: Bo-Henq Yeh, Fang-Biau Uenq, Cheng-Feng Wu
- **PDF**: https://ieeexplore.ieee.org/document/9509989
- **Abstract**: In this paper, we study the blind joint nonlinear receiver for millimeter wave (mmWave) communication systems. The mmWave system operates in a very high-frequency band and has a lot of bandwidth resources. The RF power amplifier (PA) used by the system poses a huge challenge to signal detection and demodulation. Instead of using high-complexity and difficult-to-implement digital predistortion at the transmitter, the blind joint nonlinear receiver is proposed to make mmWave communication a new possibility in 5G NR. Due to the non-linearity and edge integration, the posteriori probability of the received signal is quite difficult to analyze, which makes existing linear equalization techniques unusable. Therefore, we use the particle filter that is based on Monte Carlo sequence importance sampling. With the aid of LDPC (low-density parity-check) decoding, the proposed blind receiver can operate without training sequence. In this way, the unknown transmitting signal can be successfully recursively estimated. The simulation results validate the proposed method.
