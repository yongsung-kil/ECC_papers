# IEEE Xplore — 2009-04


## High-Throughput Layered LDPC Decoding Architecture

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:4773145
- **Type**: journal
- **Published**: April 2009
- **Authors**: Zhiqiang Cui, Zhongfeng Wang, Youjian Liu
- **PDF**: https://ieeexplore.ieee.org/document/4773145
- **Abstract**: This paper presents a high-throughput decoder architecture for generic quasi-cyclic low-density parity-check (QC-LDPC) codes. Various optimizations are employed to increase the clock speed. A row permutation scheme is proposed to significantly simplify the implementation of the shuffle network in LDPC decoder. An approximate layered decoding approach is explored to reduce the critical path of the layered LDPC decoder. The computation core is further optimized to reduce the computation delay. It is estimated that 4.7 Gb/s decoding throughput can be achieved at 15 iterations using the current technology.

## Memory-efficient and high-throughput decoding of quasi-cyclic LDPC codes

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:4814348
- **Type**: journal
- **Published**: April 2009
- **Authors**: Yongmei Dai, Zhiyuan Yan, Ning Chen
- **PDF**: https://ieeexplore.ieee.org/document/4814348
- **Abstract**: We propose turbo-sum-product (TSP) and shuffled-sum-product (SSP) decoding algorithms for quasi-cyclic low-density parity-check codes, which not only achieve faster convergence and better error performance than the sum-product algorithm, but also require less memory in partly parallel decoder architectures. Compared with the turbo decoding algorithm, our TSP algorithm saves the same amount of memory and may achieve a higher decoding throughput. The convergence behaviors of our TSP and SSP algorithms are also compared with those of the SP, turbo, and shuffled algorithms by their extrinsic information transfer (EXIT) charts.

## Hybrid burst erasure correction of LDPC codes

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:4815076
- **Type**: journal
- **Published**: April 2009
- **Authors**: Marc Fossorier
- **PDF**: https://ieeexplore.ieee.org/document/4815076
- **Abstract**: In this letter, burst erasure correction of low density parity check codes based on a hybrid approach is presented. The proposed method preserves as much as possible the original low density representation and augments it by specific check sums judiciously selected.

## Fault Secure Encoder and Decoder for NanoMemory Applications

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:4796210
- **Type**: journal
- **Published**: April 2009
- **Authors**: Helia Naeimi, AndrÉ DeHon
- **PDF**: https://ieeexplore.ieee.org/document/4796210
- **Abstract**: Memory cells have been protected from soft errors for more than a decade; due to the increase in soft error rate in logic circuits, the encoder and decoder circuitry around the memory blocks have become susceptible to soft errors as well and must also be protected. We introduce a new approach to design fault-secure encoder and decoder circuitry for memory designs. The key novel contribution of this paper is identifying and defining a new class of error-correcting codes whose redundancy makes the design of fault-secure detectors (FSD) particularly simple. We further quantify the importance of protecting encoder and decoder circuitry against transient errors, illustrating a scenario where the system failure rate (FIT) is dominated by the failure rate of the encoder and decoder. We prove that Euclidean geometry low-density parity-check (EG-LDPC) codes have the fault-secure detector capability. Using some of the smaller EG-LDPC codes, we can tolerate bit or nanowire defect rates of 10% and fault rates of 10-18 upsets/device/cycle, achieving a FIT rate at or below one for the entire memory system and a memory density of 1011 bit/cm2 with nanowire pitch of 10 nm for memory blocks of 10 Mb or larger. Larger EG-LDPC codes can achieve even higher reliability and lower area overhead.

## Sinkhorn Solves Sudoku

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:4804943
- **Type**: journal
- **Published**: April 2009
- **Authors**: Todd K. Moon, Jacob H. Gunther, Joseph J. Kupin
- **PDF**: https://ieeexplore.ieee.org/document/4804943
- **Abstract**: The Sudoku puzzle is a discrete constraint satisfaction problem, as is the error correction decoding problem. We propose here an algorithm for solution to the Sinkhorn puzzle based on Sinkhorn balancing. Sinkhorn balancing is an algorithm for projecting a matrix onto the space of doubly stochastic matrices. The Sinkhorn balancing solver is capable of solving all but the most difficult puzzles. A proof of convergence is presented, with some information theoretic connections. A random generalization of the Sudoku puzzle is presented, for which the Sinkhorn-based solver is also very effective.

## Error Rate Improvement in Underwater MIMO Communications Using Sparse Partial Response Equalization

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:4815408
- **Type**: journal
- **Published**: April 2009
- **Authors**: Subhadeep Roy, Tolga M. Duman, Vincent Keyko McDonald
- **PDF**: https://ieeexplore.ieee.org/document/4815408
- **Abstract**: Shallow-water horizontal underwater acoustic (UWA) channels are characterized by a time-varying multipath structure with a long delay spread. This causes significant signal distortion in phase coherent transmissions by introducing intersymbol interference (ISI), which can span several hundreds of symbols. The multipath structure is usually very sparse. This paper proposes an adaptive sparse partial response equalizer (SPRE) well matched with the channel characteristics to mitigate the ISI efficiently, and communicate reliably. Unlike the conventional equalizers that try to eliminate the ISI completely, the proposed structure performs equalization in two steps. In the first step, the channel is equalized to a judiciously chosen target impulse response (TIR), thereby leaving controlled residual ISI at the output of the SPRE. In the second step, the residual ISI is further mitigated by a near-optimal, graph-based, low-complexity symbol detection algorithm known as belief propagation (BP). We demonstrate that due to the sparse nature of the long ISI channel, and the well-matched adaptive TIR, this two-step equalization process is particularly useful. The idea here can be compared to what is done in the magnetic recording literature [i.e., partial response maximum-likelihood (ML) equalization] to avoid excessive noise enhancement, with the difference that the TIR needs to be designed adaptively using training symbols and that in the second step, instead of using a ML detector, a BP algorithm is used. The proposed SPRE algorithm is designed for a general multiple-input-multiple-output (MIMO) system and it provides soft outputs for the transmitted bits as a by-product of the BP-type equalization algorithm. Hence, it can be efficiently employed in coded systems (e.g., turbo or low-density-parity-check-coded, interleaved systems) with an iterative decoding/equalization scheme, providing significant improvements in achievable error rates. Finally, we note that the proposed SPRE scheme also incorporates a phase locked loop (PLL) structure so as to track the Doppler shift introduced by the channel. To evaluate the effectiveness of the proposed equalizer, we compare it with several decision feedback equalizers (DFEs) proposed by Stojanovic (J. Ocean. Eng. vol. 19, no. 1, pp. 100-111, Jan. 1994), Roy (Proc. MTS/IEEE TECHNO-OCEAN Conf., vol. 1, pp. 26-33, Nov. 2004), and Roy (J. Ocean. Eng., vol. 32, no. 3, pp. 663-688, Jul. 2004) both through simulations and experimental results. The results demonstrate that the SPRE receiver outperforms the decision-feedback-based receivers when the channel has long, yet sparse (possibly, nonminimum phase) structure, by reducing the frame error rates (FERs), improving the post-equalization signal-to-noise ratio (SNR), and decreasing the required number of turbo iterations (reduced latency).

## Reed–Solomon and Simplex Codes for Peak-to-Average Power Ratio Reduction in OFDM

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:4802318
- **Type**: journal
- **Published**: April 2009
- **Authors**: Robert F. H. Fischer, Christian Siegl
- **PDF**: https://ieeexplore.ieee.org/document/4802318
- **Abstract**: New schemes for peak-to-average power ratio reduction in orthogonal frequency-division multiplexing (OFDM) systems are proposed. Reed-Solomon (RS) and simplex codes are employed to create a number of candidates, from which the best are selected. Thereby, in contrast to existing approaches, the codes are arranged over a number of OFDM frames rather than over the carriers, hence a combination of the principles of multiple signal representation with selection (as done in selected mapping) and the use of channel coding is present. In particular, in multiple-antenna transmission, the proposed schemes do not cause any additional delay, but due to the utilization of the dimension space, additional gains can be achieved. Moreover, the schemes are very flexible; due to the selection step, any criterion of optimality can be taken into account. Besides multiple-antenna transmission, packet transmission is briefly considered, which, moreover, covers the appealing similarities with incremental redundancy check schemes in automatic repeat request (ARQ) applications and with decoding of codes transmitted over the erasure channel. The performance of the schemes is (using some approximations) derived analytically and is covered by numerical results that are in very good agreement with the theory. Significant gains can be achieved with these very flexible and versatile methods.

## Coherent continuous-phase frequency-shift keying: Parameter optimization and code design

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:4907452
- **Type**: journal
- **Published**: April 2009
- **Authors**: Shi Cheng, Matthew C. Valenti, Don Torrieri
- **PDF**: https://ieeexplore.ieee.org/document/4907452
- **Abstract**: The symmetric information rate of a modulation-constrained transmission system is the information-theoretic limit on performance under the assumption that the inputs are independent and uniformly distributed. The symmetric information rate for continuous-phase frequency-shift keying (CPFSK) over an AWGN channel may be estimated by considering the system to be a finite-state Markov channel and executing a BCJR-like algorithm. In this paper, the estimated symmetric information rate is used along with the exact expression for the 99% power bandwidth to determine the information-theoretic tradeoff between energy and spectral efficiency for CPFSK modulation. Using this tradeoff, the code rate and modulation index are jointly optimized for a particular spectral efficiency and alphabet size. Codes are then designed for the optimized system. The codes are comprised of variable nodes (which represent irregular repetition codes), check nodes (which represent single parity-check codes), and an interleaver connecting the variable and check nodes. The degree distributions of the code are optimized from the system's EXIT chart by using linear programming. Additional details of the code design, including labeling and interleaver design, are also discussed. Simulation results show that the optimized coded systems achieve bit error rates within 0.4 dB of the information-theoretic limits at BER = 10-5.

## Compress-spread-forward with multiterminal source coding and complete complementary sequences

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:4814349
- **Type**: journal
- **Published**: April 2009
- **Authors**: Chadi Khirallah, Vladimir Stankovic, Lina Stankovic +2
- **PDF**: https://ieeexplore.ieee.org/document/4814349
- **Abstract**: We propose a new technique, compress-spread forward (CSF), for high-performance wireless streaming from two base stations in parallel. CSF uses multiterminal source coding for efficient source compression and complete complementary sequences for error-free multiple access and synchronization. Our practical design shows significant performance gains due to spatial diversity and distributed source coding.

## Unequal Error Protection Low-Density Parity-Check Codes Design Based on Gaussian Approximation in Image Transmission

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:4918009
- **Type**: conference
- **Published**: 5-8 April 
- **Authors**: Piming Ma, Kyungsup Kwak
- **PDF**: https://ieeexplore.ieee.org/document/4918009
- **Abstract**: In this paper, we propose a scheme to design unequal error protection low-density parity-check (UEP-LDPC) codes based on Gaussian approximation algorithm over AWGN channel. Using this method, we can find effective UEP-LDPC code ensemble which has good overall performance and good UEP property. Simulation results show the superiority of the proposed UEP-LDPC code in improving the quality of reconstructed image in uncompressed image and set partitioning into hierarchical trees (SPIHT) coded image transmission.

## Cross-Layer Iterative Decoding of Irregular LDPC Codes using Cyclic Redundancy Check Codes

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:4917653
- **Type**: conference
- **Published**: 5-8 April 
- **Authors**: Zhimin Yang, Shiju Li, Hao Feng +2
- **PDF**: https://ieeexplore.ieee.org/document/4917653
- **Abstract**: This paper presents a cross-layer iterative decoder for irregular low-density parity-check (LDPC) codes which uses cyclic redundancy check (CRC) codes. The key idea of the decoder is to use correctly decoded frames as an aid for correcting the remaining erroneous frames. To accomplish this, the decoder exchanges the relevant information between layers by using the cross-layer design method and an iterative decoding architecture. Moreover, the unequal-error protection (UEP) property of irregular LDPC is exploited and both the multiple-error detection and single-error correction capabilities of the CRC code are used. Simulation results show that the proposed decoder outperforms the pure sum-product algorithm (SPA) decoder by a considerable gain while the increase in complexity is moderate. Furthermore, the error floor of irregular LDPC codes in the high Eb/NO regime can be lowered effectively. The proposed cross-layer iterative decoder can be used for any irregular LDPC coded wireless system to boost the performance and lower the error floor.

## On the Impact of Imperfect Cophasing in Uncoded and LDPC-Coded EGC Receivers over Generalized Fading Channels

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:4917856
- **Type**: conference
- **Published**: 5-8 April 
- **Authors**: Goran T. Djordjevic, Ivan B. Djordjevic, George K. Karagiannidis
- **PDF**: https://ieeexplore.ieee.org/document/4917856
- **Abstract**: We study the performance of unbalanced partially coherent uncoded and low-density parity-check (LDPC)-coded equal gain combining (EGC) receiver operating over generalized a-mu fading channels, when the binary phase-shift keying (BPSK) and quaternary phase-shift keying (QPSK) are used. We determine the bit-error ratio (BER) performance degradation due to the imperfect reference signal recovery, receiver unbalancing and fading. Furthermore, we design large girth quasi-cyclic LDPC code with high code rate, suitable for use in communications over generalized fading channels. The proposed LDPC code does not exhibit the error floor phenomena, in the region of interest, even in the presence of imperfect cophasing and receiver unbalances.

## Thresholds Calculation of LDPC Code Ensembles Using a Novel Gaussian Approximation Algorithm

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:4917989
- **Type**: conference
- **Published**: 5-8 April 
- **Authors**: Piming Ma, Kyungsup Kwak
- **PDF**: https://ieeexplore.ieee.org/document/4917989
- **Abstract**: A novel Gaussian approximation algorithm is proposed for calculating the thresholds of low-density parity- check (LDPC) code ensembles under sum-product decoding. The updating rules of means and error probability are derived. Numerical results show that the thresholds obtained by the proposed algorithm closely coincide with the values computed by density evolution (DE). Moreover, our algorithm can calculate the thresholds of irregular LDPC codes with higher accuracy than the algorithm proposed by Lehmann and Maggio.

## Log-Likelihood Ratios for LDPC Codes with Pilot-Symbol-Assisted BPSK Transmission over the Noncoherent Channel

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:4917788
- **Type**: conference
- **Published**: 5-8 April 
- **Authors**: Elisa Mo, Pooi Yuen Kam
- **PDF**: https://ieeexplore.ieee.org/document/4917788
- **Abstract**: Iterative decoding of low-density parity-check codes transmitted over noncoherent channels using pilot-symbol- assisted binary phase-shift keying (BPSK) is studied. The log- likelihood ratio of the two values of each transmitted code bit is derived using the joint probability density function of the received signal that carries that bit and a set of reference pilot signals. We establish the relationship of our metric with that derived for differential BPSK transmission and also prove that our metric converges to that for coherent BPSK transmission. The theoretical analysis is further verified through simulation studies. In addition, two approximations of the metric that yield lower computational cost with negligible performance losses are introduced. Finally, we study the effects of signal-to-noise ratio estimation error on the performance of these metrics.

## On the Designs and Challenges of Practical Binary Dirty Paper Coding

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:4917852
- **Type**: conference
- **Published**: 5-8 April 
- **Authors**: Gyu Bum Kyung, Chih-Chun Wang
- **PDF**: https://ieeexplore.ieee.org/document/4917852
- **Abstract**: We propose a practical scheme for binary dirty-paper channels. By exploiting the concept of random binning instead of superposition coding, the complexity of the system is greatly reduced. For comparison, the existing approaches require one of the native codes to be of non-uniform a priori distribution, which is generally achieved by combining a symbol mapper and high-order-alphabet low-density parity-check (LDPC) codes. Using high-order alphabets increases significantly the complexity and the resulting method is not flexible for designing systems of practical channel parameters. In contrast, we propose to implement the random binning concept using only binary LDPC and binary convolutional codes. In this work, some design challenges of this random binning approach are identified and addressed. Our systems are optimized by the joint use of density evolution (DE) and the extrinsic information transfer (EXIT) analysis. Simulation results using practical Quasi-Cyclic LDPC codes show that our system achieves similar performance to the state-of-the-art, high-order-alphabet LDPC-based systems while demonstrating significant advantages in terms of complexity and flexibility of system design.

## Code-Matched Interleaver Design over Surrogate Channels

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:4917627
- **Type**: conference
- **Published**: 5-8 April 
- **Authors**: Jing Lei, Wen Gao
- **PDF**: https://ieeexplore.ieee.org/document/4917627
- **Abstract**: Recently, the universality of a well-designed LDPC code ensemble has been recognized. Take the DVB standards for example. The structured LDPC codes originally developed for satellite communications have been reused in terrestrial and cable channels. To this end, a bit interleaver can be employed to adapt the profile of the given code to the variation of channel conditions. In this paper, we focus on the design of code-dependent bit interleavers for parallel non-uniform channels. Since the channel- dependence of a given code ensemble is dominated by the mutual information between the channel input and output, we propose to simplify the analysis about the decoding behavior by using a set of surrogate binary erasure channels (BEC). The approximation of the actual channel by the surrogate BEC is established on the equivalence of bitwise capacities, which represent the mutual information between the uniformly-distributed binary input and the likelihood ratios of the effective parallel AWGN channels. Moreover, the transition of the erasure probabilities is modeled by a linear difference equation around the decoding threshold SNR, from which we can derive a necessary condition on the convergence of decoding iterations and achieve a useful guideline for the configuration of the bit interleavers.

## A Robust Dynamic Watermarking Scheme Based on STBDW

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:5170389
- **Type**: conference
- **Published**: 31 March-2
- **Authors**: Zhu Jian-qi, Liu Yan-heng, Yin Ke +1
- **PDF**: https://ieeexplore.ieee.org/document/5170389
- **Abstract**: Software piracy is a major concern for organizations that create, use, and distribute digital content. Software watermarking is such a technique for protecting software by embedding secret information into the software to identify its copyright owner. This paper presents a novel robust dynamic watermarking scheme based on STBDW that first utilizes the Shamir threshold scheme to split the watermark number into pieces, which help to retrieve the original watermark with partial information and increase resilience. Then the pieces are run through the block cipher and self isomorphic mapping operations that makes the unrelated pieces become associated, which improves STBDW robustness further. In this article, we describe a software watermark embedding prototype in which the watermark pieces are embedded into the dynamic branch structure of program. Experiment shows that our technique has great robustness, it can effectively resist semantics-preserving code transform attacks and immune from most obfuscation attacks.

## QC-LDPC codes and their performance on Power Line Communications Channel

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:4913437
- **Type**: conference
- **Published**: 29 March-1
- **Authors**: Nikoleta Andreadou, Fotini-Niovi Pavlidou
- **PDF**: https://ieeexplore.ieee.org/document/4913437
- **Abstract**: In this paper Low Density Parity Check Codes (LDPC) are introduced in the Power Line Communications Channel (PLC). We investigate how different decoding algorithms, which are applied on LDPC codes, affect the system's performance. Therefore, an iterative belief propagation decoding algorithm as well as a proposed variation of the original bit flipping algorithm are exploited. In addition, a hybrid technique combining these two algorithms is proposed. Irregular LDPC codes of various code rates are studied. Specifically, the cases of 1/2, 1/3, 2/3, 3/4 and 4/5 code rates are investigated. Regarding the irregular LDPC codes, they are constructed in a Quasi-Cyclic form. The system's performance is expressed in terms of the resultant Bit Error Rate (BER) versus the Signal to Noise Ratio (SNR). In order to design the power line communications channel, Middleton's class A noise model is used to account for the system's background and impulsive noise, while Zimmermann's channel model is also used. The OFDM transmission technique is taken into account. Results are derived via computer simulations.

## Channel adaptation for time-varying powerline channel and noise synchronized with AC cycle

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:4913438
- **Type**: conference
- **Published**: 29 March-1
- **Authors**: Kyong-Hoe Kim, Han-Byul Lee, Yong-Hwa Kim +1
- **PDF**: https://ieeexplore.ieee.org/document/4913438
- **Abstract**: Broadband Power Line Communications (PLC) technology allows the usage of electrical power supply networks for communications purposes, such as audio/video streaming and broadband internet access. The powerline has an inherent characteristic that is the cyclic variation of channel and noise with the phase of the AC line cycle. To achieve either high throughput or high robustness, we apply dynamic channel adaptation scheme that exploits the cyclic variation of powerline characteristics. In this paper, we introduce an expedient, dynamic channel adaptation which is robust against the short-time variation of the AC synchronized powerline channel and noise. We analyze the performance enhancement for the measured powerline channel and noise when the proposed adaptation scheme is applied to the Korean standard on high speed powerline communications.

## LDPC coded MIMO OFDM-based IEEE 802.11n wireless LAN

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:5010560
- **Type**: conference
- **Published**: 28-30 Apri
- **Authors**: Salwa Serag Eldin, Mohamed Nasr, Salah Khamees +2
- **PDF**: https://ieeexplore.ieee.org/document/5010560
- **Abstract**: Recently, to meet higher data rate requirements, LDPC coded MIMO-OFDM systems are investigated widely. Multiple-input multiple-output (MIMO) wireless technology in combination with orthogonal frequency division multiplexing (OFDM) is an attractive solution for next-generation wireless local area networks (WLANs). Space-time block coded OFDM is capable of achieving substantial diversity gains, while supporting high bit-rates in wireless communications. By concatenating a space-time block coded OFDM scheme with powerful channel codes, such as low-density parity-check (LDPC) coding, the performance of the system can be further enhanced. In this contribution the performance of the latest WLAN standard, IEEE 802.11n, based on MIMO-OFDM with LDPC coding is being investigated. The achievable performance is studied as a function of MIMO mode, code rate, bandwidth, and modulation type.

## Performance enhancement of IEEE802.11n wireless LAN using irregular LDPCC

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:5010561
- **Type**: conference
- **Published**: 28-30 Apri
- **Authors**: Salwa Serag Eldin, Mohamed Nasr, Salah Khamees +2
- **PDF**: https://ieeexplore.ieee.org/document/5010561
- **Abstract**: The need for flexible network structures has created a successful Wireless Local Area Network (WLAN) market, promising to replace many wired LANs in the near future. The latest draft of IEEE 802.11n offers the potential of throughputs beyond 200 Mbps, based on physical layer data rates up to 600 Mbps. IEEE 802.11n standard adopts low density parity check coding as optional coding scheme to offer higher reliability in PHY level. LDPC may end up as the standard scheme in a host of sectors including communications, broadcasting and even hard disk drives. This paper presents LDPC efficient encoder and decoder then the performance of LDPC based on IEEE 802.11n standard is studied. Different modulation and coding schemes were compared to get the best choice.

## Switchable-rate error control coding for HF-IP systems

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:5235581
- **Type**: conference
- **Published**: 28-30 Apri
- **Authors**: S. R. Kariyawasam, B. M. Heravi, B. Honary +1
- **PDF**: https://ieeexplore.ieee.org/document/5235581
- **Abstract**: This paper provides analysis of high performance forward error control (FEC) coding scheme suitable for next generation HF-IP systems, which can be used as an optional scheme according to the requirements of the application. Present HF-IP systems comply with NATO STANAG 4539 Physical layer standards which use convolutional encoding for forward error protection and correction. The FEC that has been proposed in this paper is a class of quasi cyclic Low Density Parity Check (LDPC) coding scheme suitable for HF-IP systems. Additive groups of Finite Fields have been used to construct short-length structured LDPC codes with 4 different rates suitable for different HF channel conditions. The codes have been simulated with ITU-R F1487 HF channel model for performance analysis with different conditions and latitudes.

## Multi-Rate QC-LDPC Encoder

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:4960843
- **Type**: conference
- **Published**: 28-29 Apri
- **Authors**: Huxing Zhang, Hongyang Yu
- **PDF**: https://ieeexplore.ieee.org/document/4960843
- **Abstract**: A multi-rate memory-efficient encoder for low-density parity-check (LDPC) codes is proposed in this paper based on shift-register-adder-accumulator (SRAA). The SRAA algorithm simplifies the encoder computation module and reduces the complexity of the operation. The LDPC code generator matrix is constructed by lots of quasi-cyclic square matrices in the Chinese digital TV terrestrial broadcasting standard (DMB-T), and the encoder is presented based on the quasi-cyclic character that reduces the memory cost. Simulations demonstrate that the proposed encoder can satisfy the DMB-T in three-rate according to different bit-rate option with lower complexity.

## Modified Iterative Two-Stage Hybrid Decoding Algorithm for Low-Density Parity-Check (LDPC) Codes

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:5073688
- **Type**: conference
- **Published**: 26-29 Apri
- **Authors**: Hany R. Zeidan, Maha M. Elsabrouty
- **PDF**: https://ieeexplore.ieee.org/document/5073688
- **Abstract**: This paper considers a modified iterative version of the two-stage hybrid algorithm for decoding low-density parity- check (LDPC) codes. The hybrid-decision scheme is a decoding scheme used that combines two iterative decoding algorithms for decoding LDPC codes. This scheme is suitable for many applications such as audio and video transmission that are sensitive to time. The hybrid-decision scheme mixes between the characteristics of the soft-decision decoding scheme and the hard- decision decoding scheme to reduce the computational complexity of the whole decoding algorithm. The modification proposed in this paper is applied to the implementation-efficient reliability ratio weighted bit-flipping (IERRWBF) algorithm which represents hard-decision scheme in the hybrid algorithm. This modification is capable of achieving better performance than that of the hybrid decoding algorithm with reducing the number of iterations required at each SNR and approaching more to the performance of the SPA. This reduction is more observable as the maximum number of iterations assigned for the algorithm increases or as the code length increases with improving the error performance as proved by simulation results.

## Bit-Interleaved LDPC-Coded Modulation with Iterative Demapping and Decoding

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:5073425
- **Type**: conference
- **Published**: 26-29 Apri
- **Authors**: Qiuliang Xie, Kewu Peng, Jian Song +1
- **PDF**: https://ieeexplore.ieee.org/document/5073425
- **Abstract**: Bit-interleaved coded modulation (BICM) is a sub- optimal scheme from the average mutual information (AMI) point of view due to independent demapping. However, this AMI loss can be neglected for signal constellations with Gray mapping at high coding rates. AMI of amplitude-phase shift keying (APSK) constrained additive white Gaussian noise (AWGN) channel is provided in this paper, which shows that the BICM scheme has considerable loss with APSK constellations since no Gray mapping exists. Bit-interleaved low-density parity-check (LDPC) coded modulation (BILCM) is an excellent scheme and has been employed in many broadcasting and communication systems, however, such scheme also suffers from the independent demapping loss. Therefore, BILCM with iterative demapping and decoding (BILCM-ID) is proposed in this paper to overcome such loss. Simulation results show that the BILCM-ID scheme outweighs BILCM scheme by about 0.5 and 0.3 dB over AWGN channel for 32-APSK constellation at coding rates 2/3 and 4/5, respectively.

## Optimization of Group Layered Multi-Antenna Architectures with LDPC Codes

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:5073749
- **Type**: conference
- **Published**: 26-29 Apri
- **Authors**: Hyo-Jin Lee, Dong-Min Shin, Kyeongcheol Yang
- **PDF**: https://ieeexplore.ieee.org/document/5073749
- **Abstract**: Group layered multi-antenna architectures (GLAs) employing orthogonal space-time block codes and spatial multiplexing techniques may simultaneously exploit diversity and multiplexing gains with simple decoding algorithms based on successive interference cancellation (SIC). In this paper we first describe a decoding method of a SIC receiver based on QR decomposition in a GLA using LDPC codes, and then find a combination of code rate and modulation order which optimizes the asymptotic performance of the GLA. Simulation results show that the performance of the GLA using code rates and modulation orders found by our method is better by 2 dB than that of a GLA using the same code rate and modulation order in all layers. Our optimization method can be applied to adaptive modulation and coding schemes for GLAs.

## Symbol-Based Belief Propagation Decoding of Reed-Solomon Codes

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:5073872
- **Type**: conference
- **Published**: 26-29 Apri
- **Authors**: C. Zhong, J. R. Cruz
- **PDF**: https://ieeexplore.ieee.org/document/5073872
- **Abstract**: We propose a symbol-based belief propagation (BP) algorithm for iterative soft-decision decoding of Reed-Solomon (RS) codes. Complexity reduction is achieved by using a fast Fourier transform (FFT)-based BP algorithm. Parity-check matrix adaptation based on the reliability of the codeword symbols is an essential step to make the BP algorithm effective on high-density parity-check matrices characteristic of RS codes. The matrix adaptation, as well as all other operations, is performed at symbol level such that bit-to-symbol and symbol-to- bit conversions are avoided. A moderate coding gain over algebraic hard-decision decoding is achieved on additive white Gaussian noise channels. The symbol-based algorithm presented in this paper addresses the main weakness of its bit-based counterpart, namely the prohibitively high complexity for practical applications that use long codes and large finite fields, albeit with less coding gain.

## Joint Source Coding and Higher-Dimension Modulation

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:5073638
- **Type**: conference
- **Published**: 26-29 Apri
- **Authors**: Tze C. Wong, Hyuck M. Kwon
- **PDF**: https://ieeexplore.ieee.org/document/5073638
- **Abstract**: This paper proposes a novel joint source coding and modulation scheme. The modulation constellation points are selected according to their prior symbol probabilities for better bandwidth as well as better bit error rate performance. Both the analysis and simulation results are presented to verify that the proposed scheme can achieve better performance than the conventional disjoint source coding and modulation schemes if the modulation and source coding are designed jointly and efficiently.

## Non-Binary LDPC Codes Defined Over the General Linear Group: Finite Length Design and Practical Implementation Issues

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:5073713
- **Type**: conference
- **Published**: 26-29 Apri
- **Authors**: W. Chen, C. Poulliat, D. Declercq +3
- **PDF**: https://ieeexplore.ieee.org/document/5073713
- **Abstract**: Non-binary LDPC codes are now recognized as a potential competitor to binary coded solutions, especially when the codeword length is small or moderate. More and more works are reported with good performance/complexity tradeoffs, which make non-binary solutions interesting for practical applications, such as 4G-wireless systems or DVB-like systems. In this paper, we show that proposing non-binary LDPC codes built on finite fields is actually a limitation, both from performance and implementation points of view. By considering non-binary codes on the general linear group, we show in particular that a slight performance improvement can be obtained, compared to Galois Field codes, with reasonable additional cost in the hardware implementation. The performance gain is quite small, but comes at a slight extra decoding cost, and is obtained by proper generalization of the code optimization techniques that are standard for non-binary LDPC codes on fields.

## Low Complexity DVB-S2 LDPC Decoder

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:5073653
- **Type**: conference
- **Published**: 26-29 Apri
- **Authors**: Botao Zhang, Hengzhu Liu, Xucan Chen +2
- **PDF**: https://ieeexplore.ieee.org/document/5073653
- **Abstract**: The decoding complexity is the main issue in designing DVB-S2 Low Density Parity Check (LDPC) decoder. This paper proposes a low complexity decoder, which is based on a new row message passing Offset Min-Sum algorithm. The proposed algorithm can reduce the complexity of the decoder with no performance loss. The simplified node update units based on the proposed algorithm and the memory organization optimized across different code rates play the key role in reducing the complexity. The synthesized area of the decoder is 9.6 mm2 in Chartered 90 nm COMS technology. When the code rate is 9/10 and the work frequency is 320 MHz, the net throughput of the decoder is 998 Mbps.

## CSI-Adaptive Encoded Pilot-Symbols for Iterative OFDM Receiver with IRA Coding

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:5073485
- **Type**: conference
- **Published**: 26-29 Apri
- **Authors**: Amitav Mukherjee, Hyuck M. Kwon
- **PDF**: https://ieeexplore.ieee.org/document/5073485
- **Abstract**: This paper proposes a novel orthogonal frequency- division multiplexing (OFDM)-based iterative channel estimation and irregular repeat-accumulate (IRA) decoding scheme where the pilot symbols are encoded along with the input data and are used for both channel estimation and decoding. To achieve the objective of minimizing the bit error rate, this paper employs systematic IRA codes so that pilot symbols can be encoded as part of the data. In this way, initial channel estimation can be performed using the systematic encoded pilot symbols before channel decoding. In addition, the known pilot symbol positions have higher reliability than data and can significantly improve the initial decoding. The availability of channel state information (CSI) at the transmitter via feedback from the receiver is also exploited by introducing a second pilot permutation that adapts to the receiver channel conditions, which is shown to outperform the conventional uniform pilot spacing within the OFDM symbol. Simulation results verify the improvement in performance compared to iterative OFDM receivers with either un-encoded or encoded uniformly-spaced pilot symbols without CSI feedback.

## Spectral Efficiency Analysis in OFDM and OFDM/OQAM Based Cognitive Radio Networks

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:5073859
- **Type**: conference
- **Published**: 26-29 Apri
- **Authors**: Haijian Zhang, Didier Le Ruyet, Michel Terre
- **PDF**: https://ieeexplore.ieee.org/document/5073859
- **Abstract**: The future wireless communication is expected to be able to improve the efficiency of spectrum usage. To solve the challenge of spectrum shortage, an innovative opportunistic spectrum access strategy, called cognitive radio (CR) has been proposed. Conventional orthogonal frequency division multiplexing (OFDM) has already been suggested as a physical layer candidate for CR system. Herein another potential candidate for CR, OFDM offset quadrature amplitude modulation (OFDM/OQAM) is introduced, and its spectral efficiency for coded multicarrier transmission is compared with cyclic prefix based OFDM (CP-OFDM) and raised cosine windowed OFDM (RC-OFDM) in CR context. Simulated results of spectral efficiency comparison (SEC) for different multicarrier systems are interpreted by theoretically analyzing the out-of-band radiation of their prototype pulses shaping. Both theoretic analysis and experimental results can show that OFDM/OQAM is a more natural candidate than CP-OFDM and RC-OFDM for CR networks application.

## Reconfigurable Rateless Codes

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:5073827
- **Type**: conference
- **Published**: 26-29 Apri
- **Authors**: Nicholas Bonello, Rong Zhang, Sheng Chen +1
- **PDF**: https://ieeexplore.ieee.org/document/5073827
- **Abstract**: We propose novel reconfigurable rateless codes, that are capable of not only varying the block length but also adaptively modify their encoding strategy by incrementally adjusting their degree distribution according to the prevalent channel conditions without the availability of the channel state information at the transmitter. In particular, we characterize a reconfigurable rateless code designed for the transmission of 9,500 information bits that achieves a performance, which is approximately 1 dB away from the discrete-input continuous-output memoryless channel's (DCMC) capacity over a diverse range of channel signal-to-noise (SNR) ratios.

## Parallel Stack Decoding for MIMO Schemes

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:5073768
- **Type**: conference
- **Published**: 26-29 Apri
- **Authors**: Abdellatif Salah, Samuel Guillouard, Ghaya Rekaya Ben-Othman
- **PDF**: https://ieeexplore.ieee.org/document/5073768
- **Abstract**: Classical ML decoders for multiple input multiple output (MIMO) systems like the sphere decoder, the Schnorr-Euchner algorithm, the Fano and the stack decoders suffer from high complexity for high number of antennas and large constellation sizes. In this paper, we propose the use of parallel processing for stack decoding, to decode signals transmitted on linear MIMO channels to reduce time consumption of hardware architecture. It will be shown that the parallel stack decoder allows a 50% less of run time compared to the classical stack decoder.

## Total Power Control for Cooperative Base Stations Uplink

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:5073887
- **Type**: conference
- **Published**: 26-29 Apri
- **Authors**: Sara Bavarian, James K. Cavers
- **PDF**: https://ieeexplore.ieee.org/document/5073887
- **Abstract**: In this paper, we introduce a novel power control strategy based on the total received power in the uplink of cooperative base stations (CBSs). Power control via channel inversion is common practice in the uplink of cellular systems as it maintains constant received signal power at the controlling base station (BS) regardless of the position of the mobile station (MS). Unlike the conventional cellular system, CBSs share information in detecting the MSs and they are shown to increase the system capacity. We propose a power control approach based on sustaining the total received power in CBSs. We investigate the performance of this method through simulations and show that it reduces the intercell interference in the CBS systems, saves power and improves the BER performance in both coded and uncoded scenarios.

## Analysis of threshold of regular and irregular LDPC codes using Gaussian approximation

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:5068932
- **Type**: conference
- **Published**: 22-24 Apri
- **Authors**: Chia-Lu Ho
- **PDF**: https://ieeexplore.ieee.org/document/5068932
- **Abstract**: We present the formulas for searching for the thresholds of regular and irregular low-density parity-check (LDPC) codes under message-passing (MP) algorithm. A Gaussian approximation is applied to studying the evolution of the means of the messages of the variable nodes and the check nodes. Accurate numerical integration methods by using transformations are shown for evaluating the expected values of the message of the check nodes. Tables are built first and interpolations are used for further evaluations. Two curves are used to locate the threshold. We utilize an iterative decoding tunnel between these two curves and study the decoding performance by evaluating conditions of the derivatives of these two curves. Using this method the performance of both regular and irregular LDPC codes can be studied in a unified manner without using simulation.

## Cooperative relay channel with LDPC codes constructed from array codes

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:5068956
- **Type**: conference
- **Published**: 22-24 Apri
- **Authors**: Mingkwan Somphruek, Rolando Carrasco, Stephane Le Goff
- **PDF**: https://ieeexplore.ieee.org/document/5068956
- **Abstract**: Cooperative communication represents a new class of diversity techniques in which multiple nodes each with a single antenna cooperate to generate a virtual multiple-antenna transmission system and thus offer the benefits of spatial diversity. This paper proposes suitable array codes used as low-density parity-check (LDPC) codes to be applied in the cooperative amplify-and-forward (AF) network. A mathematical description of the construction of suitable array codes for a relay fading channel is also presented. Compared with quasi-cyclic (QC) LDPC codes, the array codes have similar encoding complexity and can adaptively generate various desired girth values. This paper shows that array codes with large girths can achieve substantial system performance improvements. Simulation results in this paper show that using array codes as LDPC codes for cooperative relay transmission provides a significant performance improvement over direct transmission. Moreover, it is also shown that its performance is superior to some structured LDPC codes such as QC-LDPC codes, particularly, a coding gain of about 1dB at BER of 10-3 can be provided over its counterpart.

## Fast Parallel Weighted Bit Flipping decoding algorithm for LDPC codes

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:5068982
- **Type**: conference
- **Published**: 22-24 Apri
- **Authors**: Miroslav Vanek, Peter Farkas
- **PDF**: https://ieeexplore.ieee.org/document/5068982
- **Abstract**: In this paper a fast version of the parallel weighted bit flipping LDPC decoding algorithm (PWBF) is presented. The idea, which allowed decreasing the computational complexity of the PWBF method, is based on the observation that in dependency on signal to noise ratio, many of the received bits in the codeword of LDPC code could be without error. The augmented algorithm makes tests based on syndromes and symbol involvement in parity checks, which are given by the factor graph corresponding to the chosen LDPC code in order to define so called guaranteed bits. These guaranteed bits do not participate in the decoding calculations further. Simulation results are presented, which show that there is not visible any significant performance deterioration by application of this method and that the approximate speed up of the decoding for the tested codes is about 25% on the selected hardware in comparison with the known PWBF.

## Efficiency comparison of LDPC-LDGM and Raptor codes for PL-FEC with very large block sizes

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:5068986
- **Type**: conference
- **Published**: 22-24 Apri
- **Authors**: Rafael Montalban Gutierrez, Gonzalo Seco-Granados
- **PDF**: https://ieeexplore.ieee.org/document/5068986
- **Abstract**: In this paper the performance of LDPC-LDGM codes and Raptor codes is studied and compared in terms of efficiency. LDPC-LDGM and Raptor are FEC codifications that can be applied at packet level. PL-FEC consists in including redundant packets in the transmission to ensure correct reception. Althought these techniques have been previously studied in the literature, they have usually been compared with the performance of small block Reed Solomon codes. This paper presents a novel comparison between the performance of LDPC-LDGM codes and Raptor codes as alternatives for packet level FEC when large codification blocks are needed. The results obtained show that Raptor codes clearly outperform LDPC-LDGM codes in almost all scenarios.

## Use of extrinsic information transfer chart to predict behavior of turbo codes

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:5068930
- **Type**: conference
- **Published**: 22-24 Apri
- **Authors**: Teodor Iliev, Izabella Lokshina, Dimitar Radev
- **PDF**: https://ieeexplore.ieee.org/document/5068930
- **Abstract**: In this paper, we consider turbo codes that are now introduced in various international standards, including the UMTS standard for third generation personal communications and the ETSI DVB-T standard for Terrestrial Digital Video Broadcasting, and review the method of extrinsic information transfer. The convergence properties of the iterative decoding process associated with a given turbo-coding scheme are assessed using the so-called extrinsic information transfer (EXIT) chart analysis technique. This approach provides an opportunity to foresee the bit error rate (BER) of a turbo code system using only the EXIT chart. It is shown that EXIT charts are powerful tools to analyze and optimize the convergence behavior of iterative systems utilizing the turbo principle, i.e., systems exchanging and refining extrinsic information. The idea is to consider the associated SISO stages as information processors that map input a priori LLR's onto output extrinsic LLR's, the information content being obviously assumed to increase from input to output, and introduce them to the design of turbo systems without the reliance on extensive simulation. Compared with existing methods for generating EXIT functions, a suggested approach provides insight into the iterative behavior of linear turbo systems with substantial reduction in numerical complexity.

## A generic architecture of CCSDS Low Density Parity Check decoder for near-earth applications

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:5090854
- **Type**: conference
- **Published**: 20-24 Apri
- **Authors**: Fabien Demangel, Nicolas Fau, Nicolas Drabik +2
- **PDF**: https://ieeexplore.ieee.org/document/5090854
- **Abstract**: Low Density Parity Check (LDPC) codes have recently been chosen in the CCSDS standard for uses in near-earth applications. The specified code belongs to the class of Quasi-Cyclic LDPC codes which provide very high data rates and high reliability. Even if these codes are suited to high data rate, the complexity of LDPC decoding is a real challenge for hardware engineers. This paper presents a generic architecture for a CCSDS LDPC decoder. This architecture uses the regularity and the parallelism of the code and a genericity based on an optimized storage of the data. Two FPGA implementations are proposed: the first one is low-cost oriented and the second one targets high-speed decoder.

## A novel LDPC decoder for DVB-S2 IP

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:5090867
- **Type**: conference
- **Published**: 20-24 Apri
- **Authors**: Stefan Muller, Manuel Schreger, Marten Kabutz +3
- **PDF**: https://ieeexplore.ieee.org/document/5090867
- **Abstract**: In this paper a programmable Forward Error Correction (FEC) IP for a DVB-S2 receiver is presented. It is composed of a Low-Density Parity Check (LDPC), a Bose-Chaudhuri-Hoquenghem (BCH) decoder, and pre- and postprocessing units. Special emphasis is put on LDPC decoding, since it accounts for the most complexity of the IP core by far. We propose a highly efficient LDPC decoder which applies Gauss-Seidel decoding. In contrast to previous publications, we show in detail how to solve the well known problem of superpositions of permutation matrices. The enhanced convergence speed of Gauss-Seidel decoding is used to reduce area and power consumption. Furthermore, we propose a modified version of the lambda-Min algorithm which allows to further decrease the memory requirements of the decoder by compressing the extrinsic information. Compared to the latest published DVB-S2 LDPC decoders, we could reduce the clock frequency by 40% and the memory consumption by 16%, yielding large energy and area savings while offering the same throughput.

## Accelerating FPGA-based emulation of quasi-cyclic LDPC codes with vector processing

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:5090905
- **Type**: conference
- **Published**: 20-24 Apri
- **Authors**: Xiaoheng Chen, Jingyu Kang, Shu Lin +1
- **PDF**: https://ieeexplore.ieee.org/document/5090905
- **Abstract**: FPGAs are widely used for evaluating the error-floor performance of LDPC (low-density parity check) codes. We propose a scalable vector decoder for FPGA-based implementation of quasi-cyclic (QC) LDPC codes that takes advantage of the high bandwidth of the embedded memory blocks (called Block RAMs in a Xilinx FPGA) by packing multiple messages into the same word. We describe a vectorized overlapped message passing algorithm that results in 3.5times to 5.5times speedup over state-of-the-art FPGA implementations in literature.

## Robust Counting Via Counter Braids: An Error-Resilient Network Measurement Architecture

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:5061958
- **Type**: conference
- **Published**: 19-25 Apri
- **Authors**: Y. Lu, B. Prabhakar
- **PDF**: https://ieeexplore.ieee.org/document/5061958
- **Abstract**: A novel counter architecture, called counter braids, has recently been proposed for accurate per-flow measurement on high-speed links. Inspired by sparse random graph codes, counter braids solves two central problems of per-flow measurement: one-to-one flow-to-counter association and large amount of unused counter space. It eliminates the one-to-one association by randomly hashing a flow label to multiple counters and minimizes counter space by incrementally compressing counts as they accumulate. The random hash values are reproduced offline from a list of flow labels, with which flow sizes are decoded using a fast message passing algorithm. The decoding of counter braids introduces the problem of collecting flow labels active in a measurement epoch. An exact solution to this problem is expensive. This paper complements the previous proposal with an approximate flow label collection scheme and a novel error-resilient decoder that decodes despite missing flow labels. The approximate flow label collection detects new flows with variable-length signature counting Bloom filters in SRAM, and stores flow labels in high-density DRAM. It provides a good trade-off between space and accuracy: more than 99 percent of the flows are captured with very little SRAM space. The decoding challenge posed by missing flow labels calls for a new algorithm as the original message passing decoder becomes error-prone. In terms of sparse random graph codes, the problem is equivalent to decoding with graph deficiency, a scenario beyond coding theory. The error-resilient decoder employs a new message passing algorithm that recovers most flow sizes exactly despite graph deficiency. Together, our solution achieves a 10-fold reduction in SRAM space compared to hash-table based implementations, as demonstrated with Internet trace evaluations.

## Robust and fast non asymmetric distributed source coding using turbo codes on the syndrome trellis

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:4960124
- **Type**: conference
- **Published**: 19-24 Apri
- **Authors**: V. Toto-Zarasoa, A. Roumy, C. Guillemot +1
- **PDF**: https://ieeexplore.ieee.org/document/4960124
- **Abstract**: We consider the distributed compression of two (binary memoryless) correlated sources and propose a unique codec that can reach any point in the Slepian-Wolf region. In a previous method based on channel codes, the decoder multiply the compressed data by an inverse submatrix of the code. This multiplication presents two drawbacks. First, if turbo codes are used, the submatrix has no periodic structure s.t. the whole inverse has to be stored and no fast implementation exists for the multiplication. Second, this multiplication may lead to error propagation. In this paper, we propose a method that is both robust and fast.

## Didstributed source coding authentication of images with affine warping

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:4959875
- **Type**: conference
- **Published**: 19-24 Apri
- **Authors**: Yao-Chung Lin, David Varodayan, Bernd Girod
- **PDF**: https://ieeexplore.ieee.org/document/4959875
- **Abstract**: Media authentication is important in content delivery via untrusted intermediaries, such as peer-to-peer (P2P) file sharing. Many differently encoded versions of a media file might exist. Our previous work applied distributed source coding not only to distinguish the legitimate diversity of encoded images from tampering but also to localize tampered regions in an image already deemed to be in authentic. In both cases, authentication requires a Slepian-Wolf encoded image projection that is supplied to the decoder. We extend our scheme to authenticate images that have undergone affine warping. Our approach incorporates an expectation maximization algorithm into the Slepian-Wolf decoder. Experimental results demonstrate that the proposed algorithm can distinguish legitimate encodings of authentic images from illegitimately modified versions, despite an arbitrary affine warping, using authentication data of less than 250 bytes per image.

## Rate-constrained distributed distance testing and its applications

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:4959707
- **Type**: conference
- **Published**: 19-24 Apri
- **Authors**: Chuohao Yeo, Parvez Ahammad, Hao Zhang +1
- **PDF**: https://ieeexplore.ieee.org/document/4959707
- **Abstract**: We investigate a practical approach to solving one instantiation of a distributed hypothesis testing problem under severe rate constraints that shows up in a wide variety of applications such as camera calibration, biometric authentication and video hashing: given two distributed continuous-valued random sources, determine if they satisfy a certain Euclidean distance criterion. We show a way to convert the problem from continuous-valued to binary-valued using binarized random projections and obtain rate savings by applying a linear syndrome code. In finding visual correspondences, our approach uses just 49% of the rate of scalar quantization to achieve the same level of retrieval performance. To perform video hashing, our approach requires only a hash rate of 0.0142 bpp to identify corresponding groups of pictures correctly.

## Log-likelihood ratio clipping in MIMO-BICM systems: Information geometric analysis and impact on system capacity

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:4960113
- **Type**: conference
- **Published**: 19-24 Apri
- **Authors**: Stefan Schwandter, Peter Fertl, Clemens Novak +1
- **PDF**: https://ieeexplore.ieee.org/document/4960113
- **Abstract**: The clipping of log-likelihood ratios (LLRs) in soft demodulators for multiple-input multiple-output (MIMO) systems with bit-interleaved coded modulation (BICM) was recently observed to allow for enormous complexity savings. In this paper we first provide an information-geometric interpretation of LLR clipping as information projection onto a log-convex manifold. Then we study the system capacity of MIMO-BICM systems that use LLR clipping. Our results show that strong LLR clipping is possible without significant capacity loss. We finally propose an LLR transformation scheme which is necessary for approaching capacity in case of strong clipping. The usefulness of this LLR transformation is illustrated by numerical simulations for MIMO-BICM systems employing low-density parity check (LDPC) codes.

## Dialog codes for secure wireless communications

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:5211946
- **Type**: conference
- **Published**: 13-16 Apri
- **Authors**: Anish Arora, Lifeng Sang
- **PDF**: https://ieeexplore.ieee.org/document/5211946
- **Abstract**: We investigate the feasibility of achieving perfect secrecy in wireless network communications without shared secrets. We introduce a secure coding problem in which not only the sender but also the receiver participates in the coding. In essence, the receiver's role is to selectively jam the sender's transmission at the level of bits, bytes, or packets. We then design a class of secure codes, which we call dialog codes, for diverse channel models and receiver models. Our codes are simple and efficient, with only O(1) complexity in both the encoding and the decoding process, and achieve optimal coding rate in some channel models. This, along with their potential for augmenting security and/or simplifying security bootstrapping, makes them worthy of consideration for resource-constrained wireless sensor network devices. By way of experimental validation, we study the channel jamming characteristics of extant mote radios - specifically, CC2420 (IEEE 802.15.4) and CC1000 - in experiments, observe their time-varying channel behavior, and demonstrate the correctness and robustness of implementations of our dialog codes at the byte-level and at the packet-level in the presence of dynamic channel fluctuations.
