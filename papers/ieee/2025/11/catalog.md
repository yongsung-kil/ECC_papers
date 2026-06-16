# IEEE Xplore — 2025-11


## Performance Improvement of Chaos-Coded Modulation Method with Non-Binary Error Correction Codes

- **ID**: ieee:11023168
- **Type**: journal
- **Published**: November 2
- **Authors**: Ryo Tozawa, Eiji Okamoto, Naoto Horiike +1
- **PDF**: https://ieeexplore.ieee.org/document/11023168
- **Abstract**: With the recent increase in mobile devices and Internet of Things (IoT), ensuring security against eavesdropping has become crucial. We focus on physical-layer security and propose chaos-coded modulation (CCM), which encrypts modulation in the physical layer. CCM is a type of symmetric key encryption method that achieves confidentiality against eavesdroppers by convolving multiple bits and the shared key during modulation, while enabling legitimate receivers to obtain coding gain. However, owing to the encryption in the CCM, in principle, no correlation exists between the Hamming distance of the bit sequence and the Euclidean distance of the modulated symbol sequence. Therefore, the bit labeling of CCM is imperfect when compared to the Gray labeling of linear modulation, and the log-likelihood ratio obtained at the receiver is degraded. Consequently, the CCM has significantly limited performance improvement when concatenated with external error correction codes (ECCs), despite its coding gain being uncoded. Additionally, performance degradation increases as the modulation rate increases. To solve this problem, we propose a CCM with a non-binary ECC that matches the code length to the CCM instead of a conventional binary ECC, thereby addressing the aforementioned demodulation problem and improving error-rate performance. Numerical results show that the CCM with non-binary low-density parity-check (NB-LDPC) codes with a code length of 1024 and a coding rate of 0.5 achieves a gain of 1.5 dB at a bit error rate of 10−4 compared to binary phase-shift keying and a gain of 2.9 dB compared to the CCM with binary LDPC codes under the same conditions. Furthermore, the NB-LDPC codes are more effective when the modulation rate is two or higher.

## Performance Improvement of Voronoi Constellations by Multi-Dimensional Rotation for Fading Channels

- **ID**: ieee:11157912
- **Type**: journal
- **Published**: November 2
- **Authors**: Ryo Tozawa, Eiji Okamoto, Naoto Horiike +1
- **PDF**: https://ieeexplore.ieee.org/document/11157912
- **Abstract**: High transmission quality is essential for wireless communication. To meet this demand, we propose an approach to enhance the modulation method using Voronoi constellations (VCs) based on an $N$-dimensional lattice partition. Compared to traditional methods such as $M$-ary phase-shift keying ($M$-PSK) and $M$-ary quadrature amplitude modulation ($M$-QAM) on a two-dimensional plane, $N$-dimensional VCs offer a larger Euclidean distance between signal points, resulting in superior error rate performance in additive white Gaussian noise (AWGN) channels. To further improve performance in fading channels, we introduce new VCs that achieve diversity gain by rotating the constellation in $N$-dimensional space while preserving AWGN channel characteristics. Numerical results demonstrate that VCs achieve a 25 dB gain for QPSK and a 17 dB gain for 16QAM at a block error rate of 10−4 in a symbol-independent and identically distributed (i.i.d.) Rayleigh fading channel. Additionally, as the achieved diversity gain is influenced by fading variations, the effective range of these gains was clarified in accordance with the 5G New Radio (NR) radio interface.

## Edge-Spreading Raptor-Like LDPC Codes for 6G Wireless Systems

- **ID**: ieee:11025845
- **Type**: journal
- **Published**: Nov. 2025
- **Authors**: Yuqing Ren, Leyu Zhang, Yifei Shen +4
- **PDF**: https://ieeexplore.ieee.org/document/11025845
- **Abstract**: Next-generation channel coding has stringent demands on throughput, energy consumption, and error rate performance while maintaining key features of 5G New Radio (NR) standard codes such as rate compatibility, which is a significant challenge. Due to excellent capacity-achieving performance, spatially-coupled low-density parity-check (SC-LDPC) codes are considered a promising candidate for next-generation channel coding. In this paper, we propose an SC-LDPC code family called edge-spreading Raptor-like (ESRL) codes. Unlike other SC-LDPC codes that adopt the structure of existing rate-compatible LDPC block codes before coupling, ESRL codes maximize the possible locations of edge placement and focus on constructing an optimal coupled matrix. Moreover, a new graph representation called the unified graph is introduced. This graph offers a global perspective on ESRL codes and identifies the optimal edge reallocation to optimize the spreading strategy. We conduct comprehensive comparisons of ESRL codes and 5G-NR LDPC codes. Simulation results demonstrate that when all decoding parameters and complexity are the same, ESRL codes have obvious advantages in error rate performance and throughput compared to 5G-NR LDPC codes in some specific scenarios (low and high number of iterations), making them a promising solution towards next-generation channel coding.

## SC-GC-LDPC for nand Flash Memory: Construction and Decoding

- **ID**: ieee:10974699
- **Type**: journal
- **Published**: Nov. 2025
- **Authors**: Jinhong Mo, Xiongfei Zhai, Min Yu +2
- **PDF**: https://ieeexplore.ieee.org/document/10974699
- **Abstract**: With the continuous improvement of data memory density, as the common solution for error correction of nand flash, the low-density-parity-check (LDPC) code faces more challenges, such as the increasing code length requirements, the worse raw bit error rates (RBERs), and the frequently varied channels. In this article, a new (37536, 33672) spatially coupled and globally coupled LDPC (SC-GC-LDPC) code is constructed to address the above challenge, which outperforms the traditional globally coupled LDPC (GC-LDPC) code with the gaps of 0.065 and 0.08 dB by exploiting the layered sum-product algorithm (SPA) and the layered normalized min-sum (NMS) algorithm, respectively. In the flash channel, the SC-GC-LDPC code also shows superior error correction performance than the conventional GC-LDPC codes with 25% improvement. Due to its special structure of the check matrix, an improved two-level decoding algorithm (ITLA) and an improved two-phase decoding algorithm (ITPA) are proposed in this article. Specifically, the algorithms exploit the adjacent subcodes to correct the faulty ones, which reduces the number of check-node-updating (CNU). For the case of single subcode errors, the simulation results show that the number of CNU is reduced by ranging from 6.64% to 31.14% by applying our proposed algorithms, leading to significant improvement of throughput. Compared with the conventional algorithms, the ITLA and ITPA only show slight performance loss. Moreover, ITPA also provides high flexibility of decoding in the nand flash memory, which can achieve the balance between the error-correction performance and the throughput.

## A Multi-High-Rate Structured Algebraic QC-LDPC Code for 3D TLC NAND Flash Memory

- **ID**: ieee:11028049
- **Type**: journal
- **Published**: Nov. 2025
- **Authors**: Linxin Yin, Xiongfei Zhai, Yi Fang +1
- **PDF**: https://ieeexplore.ieee.org/document/11028049
- **Abstract**: As the number of stacked layers in 3D NAND flash memory increases, the channels experience more complex noise, leading to significant fluctuations in the error detection rate. Error-correcting codes with varying error correction capabilities (ECC) are required at different flash stages. To address this issue, we investigate multi-high-rate low-density parity-check (LDPC) codes for 3D NAND flash memory in this paper. Firstly, we mathematically model the 3D triple-level cell (TLC) NAND flash channel based on the obtained data from the test platform. Then we propose a multi-high-rate structured algebraic quasi-cyclic LDPC (MHR-SA-QC-LDPC) code. Specifically, the MHR-SA-QC-LDPC code contains the fixed number of information bits and can be adjusted to various rates according to the characteristics of NAND flash channels. Both additive and multiplicative group construction methods are analyzed in the prime field. Simulation results demonstrate that the proposed LDPC codes outperform existing benchmarks in 3D TLC NAND flash channels, improving both ECC performance and device lifetime.

## BMST-LDPC Coded Transmission of Block Varying Sparse Sources

- **ID**: ieee:11025846
- **Type**: journal
- **Published**: Nov. 2025
- **Authors**: Yinchu Wang, Yixin Wang, Xiao Ma
- **PDF**: https://ieeexplore.ieee.org/document/11025846
- **Abstract**: In this paper, we propose to transmit sparse data by exploiting block Markov superposition transmission (BMST) of high-rate low-density parity-check (LDPC) codes. The high-rate LDPC codes are taken as the basic codes to lower down the error floors, while the BMST serves as joint source-channel coding (JSCC). The most distinguished feature of the BMST-LDPC codes is their flexible construction, which requires no complicated optimization and applies to a wide range of code rates. More importantly, embedding LDPC codes into the BMST system allows us to carry the sparsity information by free-ride coding without any loss of code rate, which may find applications especially in the scenario when the source sparsity varies from block to block. Numerical results show that the proposed BMST-LDPC coded system performs well for sparse sources with entropy  $\lesssim 0.5$  bits, providing an easy way to trade off between the transmission power and the system bandwidth.

## Efficient Encoding Algorithm and Architecture for 2-D Quasi-Cyclic LDPC Codes With Applications to 2-D Magnetic Recording

- **ID**: ieee:11142887
- **Type**: journal
- **Published**: Nov. 2025
- **Authors**: Karthik Bharadwaj, Shayan Srinivasa Garani
- **PDF**: https://ieeexplore.ieee.org/document/11142887
- **Abstract**: We propose an efficient encoding algorithm and architecture for 2-D quasi-cyclic (QC) low-density parity-check (LDPC) codes. The encoding algorithm is derived based on the null space of the parity-check tensor obtained by tiling random permutation tensors satisfying certain girth constraints toward improved error correction performance. Our contributions are threefold. First, the construction of 2-D LDPC codes is generalized to accommodate random tilings of permutation tensors, providing code design flexibility over prior work based on predefined shifts. We provide the conditions for obtaining girth greater than four and six, useful for deriving the parity-check tensor of the code algorithmically. Second, based on the parity-check tensor, the generator tensor of the 2-D code is derived. We prove that the generator tensor of a 2-D code whose parity-check tensor has the same i-shifts within each block row, regardless of the j-shifts, comprises tiles of circulant tensors, useful for hardware realization. Third, three different hardware architectures that trade off hardware resources with speed and throughput are proposed. Finally, we analyze the performance of the code via simulations. The proposed 2-D codes are capable of correcting random errors and cluster errors by design. Specifically, for a 2-D LDPC code of rate 0.5 and size 50  $\times$  100, the proposed approach with random shifts along with layered decoding achieves a 0.7 dB signal-to-noise ratio (SNR) gain for random errors at a code failure rate (CFR) of 10−5 and a 1.8 dB SNR gain for burst errors, compared to non-layered decoding with predefined shifts.

## Rank Analysis and Its Applications for Quasi-Cyclic Low-Density Parity-Check Codes

- **ID**: ieee:11168913
- **Type**: journal
- **Published**: Nov. 2025
- **Authors**: Po-Chun Yang, Chung-Hsuan Wang, Chi-chao Chao
- **PDF**: https://ieeexplore.ieee.org/document/11168913
- **Abstract**: In this paper, we develop a new approach for rank analysis of parity-check matrices for quasi-cyclic low-density parity-check codes based on the associated polynomials of circulant matrices, applicable to general finite fields and arbitrary circulant sizes. Some formulas on the rank for parity-check matrices with one, two, and three row-blocks are first derived. For the general case with arbitrary numbers of row-blocks, lower and upper bounds on the rank are presented, and these bounds can be combined to give the exact rank result under certain conditions. We also investigate the effect on the rank by changing the circulant size. Furthermore, we study the relations between the rank of the masked matrix and that of the masking matrix, which can be used to predict the rank of the parity-check matrix after masking. The obtained rank analysis results are then applied to several classes of existing algebraically constructed parity-check matrices, along with their masked matrices. Finally, we demonstrate how rank analysis can be used in the code design procedure.

## Multiple-Resolution Decoding Architecture for QC-LDPC Codes

- **ID**: ieee:10994196
- **Type**: journal
- **Published**: Nov. 2025
- **Authors**: In-Cheol Park, Kangjoon Choi, Hyejung Jang +1
- **PDF**: https://ieeexplore.ieee.org/document/10994196
- **Abstract**: This paper proposes a hardware-efficient multiple-resolution decoding architecture for quasi-cyclic low-density parity-check (QC-LDPC) codes, specifically designed to meet the stringent requirements of the 5G New Radio (NR) standard. The proposed architecture adopts a single-instruction multiple-data (SIMD) approach to dynamically adjust the bitwidth of log-likelihood ratio (LLR) values based on the  $Eb/N_{0}$  condition, significantly reducing hardware complexity and improving throughput area ratio. Unlike conventional single-resolution decoders, the architecture processes 2-bit LLR values in high  $Eb/N_{0}$  regions and scales up to 4-bit or 8-bit LLR values for moderate and low  $Eb/N_{0}$  conditions, maintaining robust error-correcting performance. Key innovations include SIMD-based design for variable-node units (VNUs), check-node units (CNUs), and quasi-cyclic shifting networks (QSNs), as well as optimized memory access scheduling to support all 51 lifting sizes defined in the 5G NR standard. Designed in a 65-nm CMOS process, the decoder achieves a peak throughput of 27.24 Gbps under error-free conditions with a throughput area ratio improvement of  $2.07\times $  compared to the state-of-the-art designs. Furthermore, the proposed architecture demonstrates superior throughput-area ratio and flexibility, supporting all code rates and lifting sizes specified in the 5G NR standard. Simulation results confirm that the proposed decoder meets the peak throughput requirement under error-free conditions, while maintaining robust performance in challenging channel environments.

## Efficient Schemes and Architectures for Check Node Update in Shuffled Min-Sum Decoding of LDPC Codes

- **ID**: ieee:11003883
- **Type**: journal
- **Published**: Nov. 2025
- **Authors**: Lisha Luo, Xuan He, Qin Du +3
- **PDF**: https://ieeexplore.ieee.org/document/11003883
- **Abstract**: By dividing Variable Nodes (VNs) into groups and processing groups sequentially, the Shuffled Min-Sum (SMS) decoding of Low-Density Parity-Check (LDPC) codes achieves a good trade-off between hardware resource and throughput. However, under the grouping strategy where at least one Check Node (CN) has multiple VN neighbors in one group, the CN update of State-Of-The-Art (SOTA) SMS decoding has long latency and high complexity. To address the issue, this paper presents two efficient CN update schemes. The first one uses the first two minimum Variable-to-Check (V2C) message magnitudes in each group and a size- $\lambda $  Monotone Double-ended Queue ( $\lambda $ MDQ), leading to an Improved  $\lambda $ MDQ (I- $\lambda $ MDQ) scheme. The second one called the Modified  $\lambda $ MDQ (M- $\lambda $ MDQ) scheme uses only the minimum in each group. As a result, our schemes reduce the number of Selection Modules (SMs) required by the CN update to only one. Simulation results show that both of our schemes have comparable error-correction performance to the SOTA schemes. Furthermore, we simplify the SM via a decomposition design and also present the detailed hardware architectures for our schemes. Analysis using the 90nm CMOS technology library shows that, compared to the SOTA schemes, our I- $\lambda $ MDQ scheme reduces the area and latency by up to 75% and 72%, respectively, while improving the throughput by up to 254%. Similarly, our M- $\lambda $ MDQ scheme reduces the area and latency by up to 79% and 70%, respectively, and improves the throughput by up to 229%.

## Generalized LDPC Codes With Low-Complexity Decoding and Fast Convergence

- **ID**: ieee:11131149
- **Type**: journal
- **Published**: Nov. 2025
- **Authors**: Dawit Simegn, Dmitry Artemasov, Kirill Andreev +2
- **PDF**: https://ieeexplore.ieee.org/document/11131149
- **Abstract**: We consider generalized low-density parity-check (GLDPC) codes with component codes that are duals of Cordaro–Wagner codes. Two efficient decoding algorithms are proposed: one based on Hartmann–Rudolph processing, analogous to Sum-Product decoding, and another based on evaluating two hypotheses per bit, referred to as the Min-Sum decoder. Both algorithms are derived using latent variables and a appropriate message-passing schedule. A quantized, protograph-based density evolution procedure is used to optimize GLDPC codes for Min-Sum decoding. Compared to 5G LDPC codes, the proposed GLDPC codes offer similar performance at 50 iterations and significantly better convergence and performance at 10 iterations.

## Nested Root-Protograph LDPC-Coded Multilevel-Priority IR-HARQ Systems: A New Design for Multi-Stream Transmissions With Non-Ergodic Block Fading

- **ID**: ieee:11079685
- **Type**: journal
- **Published**: Nov. 2025
- **Authors**: Zhaojie Yang, Xiaoxi Yu, Yaoyue Hu +2
- **PDF**: https://ieeexplore.ieee.org/document/11079685
- **Abstract**: To enhance the adaptability and performance of multi-stream transmissions over non-ergodic block fading (BF) channels, this paper studies a multilevel-priority incremental-redundancy hybrid ARQ (MP-IR-HARQ) system with nested root-protograph-based low-density parity-check (NRP-LDPC) codes. Specifically, we analyze the performance of traditional RP-LDPC codes and reveal that they are unable to achieve full diversity in the IR-HARQ system over non-ergodic BF channels. To address this limitation, we propose a design methodology to construct a family of NRP-LDPC codes having the full-diversity property, throughput-limit-approaching property, outage-limit-approaching performance, and rate compatibility tailored for the IR-HARQ system. Additionally, we incorporate a multilevel-priority design composed of the adaptive modulation, adaptive detection, and successive decoding into the traditional IR-HARQ framework. The designed MP-IR-HARQ system can support the transmission of multiple data streams while providing unequal error protection (UEP) across them. The outage-boundary analyses, throughput analyses, and word-error-rate (WER) simulations demonstrate that the proposed NRP-LDPC-coded MP-IR-HARQ system can not only significantly outperform prior-art counterparts over non-ergodic BF channels, but also enable the multi-data-stream-based UEP transmission.

## An Analysis and Design of Rate-Dependent Nested Scheduling in Layered Decoding of LDPC Codes

- **ID**: ieee:11069260
- **Type**: journal
- **Published**: Nov. 2025
- **Authors**: Dongxu Chang, Ke Liu, Guanghui Wang +2
- **PDF**: https://ieeexplore.ieee.org/document/11069260
- **Abstract**: In this study, we analyze the characteristics of scheduling sequences for layered belief propagation (LBP) that can result in efficient decoding of low-density parity-check (LDPC) codes. Specifically, we claim that scheduling sequences leading to high decoding efficiency should prioritize updating check nodes with lower error probabilities aggregated from neighboring variable nodes. We prove this conclusion separately on both the BEC and the BI-AWGN channels. Some observable characteristics in “good” scheduling sequences regarding row weights, rows connected to punctured columns, and column weights can serve as corollaries to this conclusion. By comprehensively considering these characteristics of good scheduling, we design a multi-sequence nested scheduling scheme of layered decoding for 5G New Radio (NR) LDPC codes. The proposed schemes can obtain scheduling sequences for various rates of rate-compatible LDPC codes using small hardware storage. What’s more, by respectively storing double-sequence, triple-sequence, or more sequences to obtain scheduling sequences at various code rates, a trade-off can be made between decoder storage and decoding performance. Experimental results demonstrate that the proposed scheme achieves performance improvements compared to existing scheduling schemes at nearly all code rates.

## Protomatrix-Based LDPC Codes for Continuous Phase Modulation

- **ID**: ieee:11071260
- **Type**: journal
- **Published**: Nov. 2025
- **Authors**: Erik Perrins
- **PDF**: https://ieeexplore.ieee.org/document/11071260
- **Abstract**: This paper develops a design methodology for constructing protomatrix-based low-density parity-check (LDPC) codes that are paired with (matched to) continuous phase modulation (CPM) waveforms. We show how a protomatrix extrinsic information transfer (PEXIT) based search can yield lower decoding thresholds than previously reported, and how a single constraint added to this search is effective at preserving the linear minimum distance growth property while remaining within one dB of capacity. We show that a two-stage lifting procedure plays an essential role in completely eliminating error floors at very low error rates. Our high-throughput joint LDPC–CPM decoder is demonstrated to be practical with execution speeds comparable to a standalone LDPC decoder. The global iterations of the joint decoder are shown to provide natural protection against undetected errors due to small minimum distance, and this protection is further enhanced by a novel check node “splitting” technique. The diverse family of three CPM waveforms that are used in aeronautical telemetry are considered as design examples.

## On the Error Correction of Iterative Bounded Distance Decoding of Generalized LDPC Codes

- **ID**: ieee:11164952
- **Type**: journal
- **Published**: Nov. 2025
- **Authors**: David Burshtein
- **PDF**: https://ieeexplore.ieee.org/document/11164952
- **Abstract**: Consider an ensemble of regular generalized LDPC (GLDPC) codes and assume that the same component code is associated with each parity check node. To decode a GLDPC code from the ensemble, we use the bit flipping bounded distance decoding algorithm, which is an extension of the bit flipping algorithm for LDPC codes. Previous work has shown conditions, under which, for a typical code in the ensemble with blocklength sufficiently large, a positive constant fraction of worst case errors can be corrected. In this work we first show that these requirements can be relaxed for ensembles with small left degrees. While previous work on GLDPC codes has considered expander graph arguments, our analysis formulates a necessary condition that the Tanner graph needs to satisfy for a failure event and then shows that the probability of this event vanishes for a sufficiently large blocklength. We then extend the analysis to random error correction and derive a lower bound on the fraction of random errors that can be corrected asymptotically. We discuss the extension of our results to non-binary GLDPC codes and present numerical examples.

## Stopping Set Analysis for Polar–Polar Concatenated Codes Under BP Decoding

- **ID**: ieee:11039767
- **Type**: journal
- **Published**: Nov. 2025
- **Authors**: Ziyuan Zhu, Paul H. Siegel
- **PDF**: https://ieeexplore.ieee.org/document/11039767
- **Abstract**: This paper investigates properties of polar-polar concatenated codes and their potential applications. We start by reviewing previous work on stopping set analysis for conventional polar codes, which we extend in this paper to concatenated architectures. Specifically, we present a stopping set analysis for the factor graph of concatenated polar codes, deriving an upper bound on the size of the minimum stopping set. To achieve this bound, we propose new bounds on the size of the minimum stopping set for conventional polar code factor graphs. The tightness of these proposed bounds is investigated empirically and analytically. We show that, in some special cases, the exact size of the minimum stopping set can be determined with a time complexity of  $O(N)$ , where N is the codeword length. The stopping set analysis motivates a novel construction method for concatenated polar codes. This method is used to design outer polar codes for two previously proposed concatenated polar code architectures: augmented polar codes and local-global polar codes. Simulation results with BP decoding demonstrate the advantage of the proposed codes over previously proposed constructions based on density evolution (DE).

## Probabilistic Shaping for Wi-Fi 8

- **ID**: ieee:11059934
- **Type**: journal
- **Published**: Nov. 2025
- **Authors**: Juan Fang, Qinghua Li, Cheng Chen +2
- **PDF**: https://ieeexplore.ieee.org/document/11059934
- **Abstract**: The IEEE 802.11 working group has formed a new Task Group, 802.11bn, to develop a new amendment to support ultra-high reliability (UHR) for Wi-Fi networks, which will eventually shape what Wi-Fi 8 will look like. In this paper, we propose a probabilistic shaping (PS) scheme to improve the spectrum and power efficiency in medium to high signal to noise ratio (SNR) regime for Wi-Fi 8. The integration and compatibility with legacy Wi-Fi systems, as well as other Wi-Fi 8 candidate technologies like unequal modulation (UEQM) are addressed. An architecture with a single low-density parity-check (LDPC) encoder and multiple shaping encoders is devised to adapt to different qualities of spatial channels. Furthermore, we propose practical techniques to resolve issues like error propagation, scrambler re-synchronization, and packet length determination to ensure compatibility with legacy scrambling, subframe detection, and packaging flow. It is shown that the proposed constellation shaping scheme provides average 0.89 dB shaping gains over the legacy Wi-Fi scheme, and the shaping gains remain when UEQM and lifted LDPC are applied.

## Hybrid Beamforming Assisted OTFS-Based CV-QKD Systems for Doubly Selective THz Channels

- **ID**: ieee:11069272
- **Type**: journal
- **Published**: Nov. 2025
- **Authors**: Xin Liu, Chao Xu, Stephen Wang +2
- **PDF**: https://ieeexplore.ieee.org/document/11069272
- **Abstract**: Continuous-variable quantum key distribution (CV-QKD) maps information onto the quadrature components of electromagnetic waves, so that off-the-shelf wireless transceivers can be utilized. This motivates the move from optical to Terahertz (THz) bands. However, wireless THz channels suffer from severe path loss, while the mobility of wireless users imposes doubly selective fading. Against this background, we propose a new CV-QKD regime that relies on hybrid beamforming (HBF) assisted multiple-input multiple-output (MIMO) orthogonal frequency division multiplexing (OFDM) and orthogonal time frequency space (OTFS) system, where the channel’s transmissivity and robustness against double selectivity are overcome by HBF and OTFS, respectively. Secondly, in order to provide channel state information (CSI) for both the transmitter (CSI-T) and receiver (CSI-R), practical channel estimation methods are conceived. They operate in the time-frequency domain for OFDM and in the delay-Doppler domain for OTFS. Thirdly, soft-decision detection is devised for our MIMO OFDM/OTFS aided multi-dimensional reconciliation (MDR) scheme. Low-density parity-check (LDPC) coding is invoked for further improving secure CV-QKD transmission distance in the THz band. Our simulation results demonstrate that the proposed HBF MIMO OTFS-based CV-QKD system relying on realistic estimated CSI is capable of achieving an adequate secret key rate (SKR) and secure transmission distance in hostile doubly selective THz channels.

## On Generalized Reed-Solomon Codes

- **ID**: ieee:11007566
- **Type**: journal
- **Published**: Nov. 2025
- **Authors**: Xiangping Zheng, Xiao Ma
- **PDF**: https://ieeexplore.ieee.org/document/11007566
- **Abstract**: In this paper, we prove that the generalized Reed-Solomon (RS) codes are capacity-achieving over binary-input output-symmetric (BIOS) channels, in terms of frame error rate (FER) under maximum likelihood (ML) decoding. In the finite-length region, we present the ordered statistics decoding with local constraints (LC-OSD) algorithm for the generalized RS codes. In particular, the extended most reliable basis (MRB) is derived based on a systematic matrix calculated by the parallel Lagrange interpolation, accelerating the conventional Gaussian elimination (GE). Additionally, we propose a joint source-channel coding (JSCC) scheme that incorporates generalized RS codes and classified enumerative (CE) coding, where the partition of the source is optimized by the k-means++ clustering algorithm. At the transmitter, we implement the CE coding to encode the source information. Then the variable-length codeword of the CE coding is transformed into a fixed-length codeword by the multiple-rate generalized RS encoding and superimposed with a class label for transmission. At the receiver, parallel LC-OSD is performed to recover the source. Simulation results demonstrate that the proposed JSCC scheme outperforms the double polar JSCC scheme (exhibiting a coding gain of up to 1.4 dB) and the JSCC scheme based on polarizing matrix extension (exhibiting a coding gain of up to 0.6 dB), as predicted by Gallager’s JSCC bound.

## On Lattice-Code Based Multiple Access With Imperfect Channel State Information

- **ID**: ieee:11152029
- **Type**: journal
- **Published**: Nov. 2025
- **Authors**: Yiyu Yin, Junren Qin, Tao Yang +2
- **PDF**: https://ieeexplore.ieee.org/document/11152029
- **Abstract**: This letter studies lattice-code based multiple access (LCMA) degraded with imperfect channel state information (CSI). We present the achievable rate of the LCMA scheme under imperfect CSI, and formulate a new LCMA design problem. We then present a two-step approach to solve this problem. Numerical results demonstrate that our optimized LCMA significantly outperforms conventional MMSE and MMSE with successive interference cancellation (MMSE-SIC) at practical levels of channel estimation error by 5 dB when BLER $\leq 10^{-2}$  in 8-by-4 MIMO configuration with BPSK and rate 1/2 LDPC code.

## PAC Codes With Bounded-Complexity Sequential Decoding: Pareto Distribution and Code Design

- **ID**: ieee:11155881
- **Type**: journal
- **Published**: Nov. 2025
- **Authors**: Mohsen Moradi, Hessam Mahdavifar
- **PDF**: https://ieeexplore.ieee.org/document/11155881
- **Abstract**: Recently, a novel variation of polar codes known as polarization-adjusted convolutional (PAC) codes has been introduced by Arıkan. These codes significantly outperform conventional polar and convolutional codes, particularly for short codeword lengths, and are shown to operate very close to the optimal bounds. It has also been shown that if the rate profile of PAC codes does not adhere to certain polarized cutoff rate constraints, the computation complexity for their sequential decoding grows exponentially. In this paper, we address the converse problem, demonstrating that if the rate profile of a PAC code follows the polarized cutoff rate constraints, the required computations for its sequential decoding can be bounded with a distribution that follows a Pareto distribution. This serves as a guideline for the rate-profile design of PAC codes. For a high-rate PAC  $(1024,899)$  code, simulation results show that the PAC code with Fano decoder, when constructed based on the polarized cutoff rate constraints, achieves a coding gain of more than 0.75 dB at a frame error rate (FER) of  $10^{-5}$  compared to the state-of-the-art 5G polar and LDPC codes.

## New Constructions of q-Ary MDS Array Codes Derived From Fq[x]/xm + λ and Their Efficient Erasure Encoding/Decoding

- **ID**: ieee:11165514
- **Type**: journal
- **Published**: Nov. 2025
- **Authors**: Jingjie Lv, Hongwei Zhu, Weijun Fang +2
- **PDF**: https://ieeexplore.ieee.org/document/11165514
- **Abstract**: The q-ary maximum distance separable (MDS) array codes, especially  $q=2^{v}$ , have important applications in the storage systems to prevent data loss. At now, almost all algebraic constructions of such codes are carried out over the quotient ring  $\mathbb {R}_{m}=\mathbb {F}_{q}[x]/\langle x^{m}+1\rangle $  or its subring  $\mathbb {F}_{q}[x]/\langle x^{m-1}+x^{m-2}+\cdots +1\rangle $ . In this paper, we consider the construction of MDS array codes derived form  $\mathbb {R}_{m,\lambda }=\mathbb {F}_{q}[x]/\langle x^{m}+\lambda \rangle $ , where  $\lambda \in \mathbb {F}^{*}_{q}=\mathbb {F}_{q}\backslash \{0\}$ ,  ${\mathrm { gcd}}(m,q)=1$ . By giving  $\lambda $ -GCD Constraint of polynomials and the punctured  $\lambda $ -twisted circulant matrices, a generic construction and its extensions of such codes are presented. Under this framework, four new explicit constructions are also provided. Specifically, some low-density MDS array codes are obtained in Explicit Constructions I and I  ${}^{\mathbf {'}}$ . Explicit Constructions II and III provide long MDS array codes that can be applied in the large-scale storage systems. Explicit Construction IV gives MDS array codes both with the optimal repair bandwidth and the lowest update complexity, whose sub-packetization level is smaller than that of codes in (Li et al., 2024). In addition, by the LU factorization, a decoding method for erasures is obtained. For long codes, the syndromes can be computed fast. When the erased number  $\rho \leq 3$  (the most common errors in the storage systems), its computational complexity is asymptotically optimal. By an example, the new encoder possesses fewer exclusive ORs per data bit than that of MDS array codes constructed over  $\mathbb {R}_{m}$  in (Lv et al., 2023).

## Task-Oriented Low-Label Semantic Communication With Self-Supervised Learning

- **ID**: ieee:11024114
- **Type**: journal
- **Published**: Nov. 2025
- **Authors**: Run Gu, Wei Xu, Zhaohui Yang +2
- **PDF**: https://ieeexplore.ieee.org/document/11024114
- **Abstract**: Task-oriented semantic communication enhances transmission efficiency by conveying semantic information rather than exact messages. Deep learning (DL)-based semantic communication can effectively cultivate the essential semantic knowledge for semantic extraction, transmission, and interpretation by leveraging massive labeled samples for downstream task training. In this paper, we propose a self-supervised learning-based semantic communication framework (SLSCom) to enhance task inference performance, particularly in scenarios with limited access to labeled samples. Specifically, we develop a task-relevant semantic encoder using unlabeled samples, which can be collected by devices in real-world edge networks. To facilitate task-relevant semantic extraction, we introduce self-supervision for learning contrastive features and formulate the information bottleneck (IB) problem to balance the tradeoff between the informativeness of the extracted features and task inference performance. Given the computational challenges of the IB problem, we devise a practical and effective solution by employing self-supervised classification and reconstruction pretext tasks. We further propose efficient joint training methods to enhance end-to-end inference accuracy over wireless channels, even with few labeled samples. We evaluate the proposed framework on image classification tasks over multipath wireless channels. Extensive simulation results demonstrate that SLSCom significantly outperforms conventional digital coding methods and existing DL-based approaches across varying labeled data set sizes and SNR conditions, even when the unlabeled samples are irrelevant to the downstream tasks.

## Wi-Fi: 25 Years and Counting

- **ID**: ieee:11429621
- **Type**: journal
- **Published**: Nov. 2025
- **Authors**: Giovanni Geraci, Francesca Meneghello, Francesc Wilhelmi +7
- **PDF**: https://ieeexplore.ieee.org/document/11429621
- **Abstract**: Today, Wi-Fi is over 25 years old. Yet, despite sharing the same branding name, today’s Wi-Fi boasts entirely new capabilities that were not even on the roadmap 25 years ago. This article aims to provide a holistic and comprehensive technical and historical tutorial on Wi-Fi, beginning with Institute of Electrical and Electronics Engineers (IEEE) 802.11b (Wi-Fi 1) and looking forward to IEEE 802.11bn (Wi-Fi 8). This is the first tutorial article to span these eight generations. Rather than a generation-by-generation exposition, we describe the key mechanisms that have advanced Wi-Fi. We begin by discussing spectrum allocation and coexistence, and detailing the IEEE 802.11 standardization cycle. Second, we provide an overview of the physical layer (PHY) and describe key elements that have enabled data rates to increase by over  $1000\times $ . Third, we describe how Wi-Fi medium access control (MAC) has been enhanced from the original distributed coordination function (DCF) to now include capabilities spanning from frame aggregation to wideband spectrum access. Fourth, we describe how Wi-Fi 5 first broke the one-user-at-a-time paradigm and introduced multi-user (MU) access. Fifth, given the increasing use of mobile, battery-powered devices, we describe Wi-Fi’s energy-saving mechanisms over the generations. Sixth, we discuss how Wi-Fi was enhanced to seamlessly aggregate spectrum across 2.4-, 5-, and 6-GHz bands to improve throughput, reliability, and latency. Finally, we describe how Wi-Fi enables nearby access points (APs) to coordinate in order to improve performance and efficiency. In the Appendix, we further discuss Wi-Fi developments beyond 802.11bn, including integrated millimeter-wave (IMMW) operations, sensing, security and privacy extensions, and the adoption of artificial intelligence (AI)/machine learning (ML).

## Enhanced ODMA With Pattern Collision Resolution and Parameter Design for Unsourced Multiple Access

- **ID**: ieee:11006717
- **Type**: journal
- **Published**: Nov. 2025
- **Authors**: Jianxiang Yan, Ying Li, Guanghui Song +1
- **PDF**: https://ieeexplore.ieee.org/document/11006717
- **Abstract**: An enhanced on-off division multiple access (ODMA) transmission scheme is introduced for unsourced multiple access networks. Building upon the foundational ODMA transmission scheme, we have implemented further refinements to the original joint on-off pattern and data detection algorithm. Specifically, we propose a pattern collision resolution technique that can recognize the collision degree of each on-off pattern without pilot assistance, and then iteratively recover the data of collided users over a joint factor graph. Furthermore, we introduce a finite-length performance analysis for on-off pattern detection and iterative multi-user decoding. Through this analysis, we derive numerous numerical results, revealing the impact of various parameters on the performance of collision degree detection and multi-user decoding, respectively. By summarizing the rules observed from these numerical results, we formulate design strategies for these parameters, aiming to optimize the overall performance of our scheme. The inherent super sparse property of ODMA ensures that our scheme maintains low decoding complexity. Numerical results demonstrate that, with the implementation of our pattern collision resolution method and meticulous parameter design, the proposed scheme achieves a gap of less than 1.2 dB compared to the random coding bound for up to 300 active users. This performance surpasses state-of-the-art schemes across a broad range of user numbers.

## Generalized Nearest Neighbor Decoding: General Input Constellation and a Case Study of Interference Suppression

- **ID**: ieee:11030549
- **Type**: journal
- **Published**: Nov. 2025
- **Authors**: Shuqin Pang, Wenyi Zhang
- **PDF**: https://ieeexplore.ieee.org/document/11030549
- **Abstract**: In this work, generalized nearest neighbor decoding (GNND), a recently proposed receiver architecture, is studied for channels under general input constellations, and multiuser uplink interference suppression is employed as a case study for demonstrating its potential. In essence, GNND generalizes the well-known nearest neighbor decoding, by introducing a symbol-level memoryless processing step, which can be rendered seamlessly compatible with Gaussian channel-based decoders. First, criteria of the optimal GNND are derived for general input constellations, expressed in the form of conditional moments matching, thereby generalizing the prior work which has been confined to Gaussian input. Then, the optimal GNND is applied to the use case of multiuser uplink, for which the optimal GNND is shown to be capable of achieving information rates nearly identical to the channel mutual information. By contrast, the commonly used channel linearization (CL) approach incurs a noticeable rate loss. A coded modulation scheme is subsequently developed, aiming at implementing GNND using off-the-shelf channel codes, without requiring iterative message passing between demodulator and decoder. Through numerical experiments it is validated that the developed scheme significantly outperforms the CL-based scheme.

## Quantitative Group Testing and Pooled Data in the Linear Regime With Sublinear Tests

- **ID**: ieee:11168964
- **Type**: journal
- **Published**: Nov. 2025
- **Authors**: Nelvin Tan, Pablo Pascual Cobo, Ramji Venkataramanan
- **PDF**: https://ieeexplore.ieee.org/document/11168964
- **Abstract**: In the pooled data problem, the goal is to identify the categories associated with a large collection of items via a sequence of pooled tests. Each pooled test reveals the number of items in the pool belonging to each category. A prominent special case is quantitative group testing (QGT), which is the case of pooled data with two categories. We consider these problems in the non-adaptive and linear regime, where the fraction of items in each category is of constant order. We propose a scheme with a spatially coupled Bernoulli test matrix and an efficient approximate message passing (AMP) algorithm for recovery. We rigorously characterize its asymptotic performance in both the noiseless and noisy settings, and prove that in the noiseless case, the AMP algorithm achieves almost-exact recovery with a number of tests sublinear in the total number of items p. Although there exist other efficient schemes for noiseless QGT and pooled data that achieve recovery with order-optimal sample complexity ( $\Theta \left ({{\frac {p}{\log p}}}\right)$  tests), there are no guarantees on their performance in the presence of noise, even at low noise-levels. In comparison, our scheme achieves recovery in the noiseless case with a number of tests sublinear in p, and its performance degrades gracefully in the presence of noise. Numerical simulations illustrate the benefits of the spatially coupled scheme at finite dimensions, showing that it outperforms i.i.d. test designs as well as other recovery algorithms based on convex programming.

## Spatially-Coupled Constant-Weight Code for Random Access in Fast Fading Channels

- **ID**: ieee:11146730
- **Type**: journal
- **Published**: Nov. 2025
- **Authors**: Shuai Lu, Jianping Zheng
- **PDF**: https://ieeexplore.ieee.org/document/11146730
- **Abstract**: In this letter, we propose a novel signature code, spatially-coupled (SC) constant-weight (CW) code, for random access in fast fading channels. Concretely, first, the spatial coupling base matrix is constructed with coupling width  $\omega $  and uniform coupling strength, and one CW mother code is partitioned into  $\omega $  subcodes. Then, the SC-CW signature code matrix is obtained by replacing all the  $\omega $  non-zero entries in each column of the base matrix with the  $\omega $  subcodes. Taking the CW code constructed recently based on the on-off pattern of the binary subspace chirps as the mother code, the generated SC-CW code inherits the CW and low fading coherence properties of the mother code. Moreover, the recent SC generalized approximate message passing algorithm was utilized to identify the active users with tailored input and output denoising functions. Finally, simulation results show that the proposed SC-CW code can achieve better performance than the conventional CW code.

## Recursively Extended Permutation Codes Under Chebyshev Distance

- **ID**: ieee:11168942
- **Type**: journal
- **Published**: Nov. 2025
- **Authors**: Tomoya Hirobe, Kenta Kasai
- **PDF**: https://ieeexplore.ieee.org/document/11168942
- **Abstract**: This paper investigates the construction and analysis of permutation codes under the Chebyshev distance. Direct product group permutation (DPGP) codes, independently introduced by Kløve et al. and Tamo et al., represent the best-known class of permutation codes in terms of both size and minimum distance, while also allowing for algebraic and efficient encoding and decoding. In contrast, this study focuses on recursively extended permutation (REP) codes, proposed by Kløve et al. as a recursive alternative. We analyze the properties of REP codes and prove that, despite their distinct construction principles, optimal REP codes achieve exactly the same size and minimum distance as the best DPGP codes under the Chebyshev metric. This surprising equivalence uncovers a deep connection between two structurally dissimilar code families and establishes REP codes as a structurally flexible yet equally powerful alternative to DPGP codes. In addition, we present efficient encoding and decoding algorithms for REP codes, including a sequential encoder with  $O(n \log n)$  complexity and a bounded-distance decoder with  $O(n \log ^{2} n)$  complexity.

## A Cross-Residual BP Decoding Algorithm for Dual-Polar JSCC

- **ID**: ieee:11123431
- **Type**: journal
- **Published**: Nov. 2025
- **Authors**: Xiaojun Zhang, Xin Song, Haiyang Li +2
- **PDF**: https://ieeexplore.ieee.org/document/11123431
- **Abstract**: In this letter, we propose a Cross-Residual BP (CR-BP) decoding algorithm for dual-polar joint source-channel coding (JSCC). In CR-BP, through constraining the number of skip connections, we reduce the additional complexity brought about by Cross-Residual architecture. Additionally, an information shuffling strategy between iterations is designed for CR-BP. Through enriching the information propagation paths across different iterations, historical information is efficiently inherited in subsequent iterations. The numerical results show that the CR-BP decoder can improve error correction and accelerate convergence compared to traditional decoding at a low complexity cost.

## Physical-Layer Key Generation Efficient UAV Swarm Trajectory Planning

- **ID**: ieee:11037556
- **Type**: journal
- **Published**: Nov. 2025
- **Authors**: Xiaoyang Li, Tao Chen, Fangqi Wang +2
- **PDF**: https://ieeexplore.ieee.org/document/11037556
- **Abstract**: In order to enhance the secrecy transmission of uncrewed aerial vehicle (UAV) swarm, a novel physical-layer key generation (PLKG) efficient UAV swarm trajectory planning method is proposed in this work. Different from the existing UAV trajectory planning methods that only focus on collision avoidance, energy saving and improving transmission quality, the proposed method incorporates the PLKG capability into the UAV trajectory design. Based on the findings of the fact that the wireless scattering experienced by UAV signals from different UAV trajectories are typically distinct, the channel randomness oriented PLKG behaves differently for various UAV trajectories. As a result, we propose to incorporate the PLKG metric into the UAV trajectory planning objectives, in order to improve the secrecy of UAV swarm transmissions. The theoretical derivation between UAV swarm PLKG metric and the wireless scattering entropy is obtained, and we propose a channel entropy knowledge sharing mechanism for UAV swarm to achieve PLKG efficient swarm trajectory planning. Simulation results show that the key generation performance can be largely improved in comparison to the traditional secrecy rate maximization oriented UAV swarm trajectory planning.

## Robustness in Wireless Distributed Learning: An Information-Theoretic Analysis

- **ID**: ieee:11069261
- **Type**: journal
- **Published**: Nov. 2025
- **Authors**: Yangshuo He, Guanding Yu, Huaiyu Dai
- **PDF**: https://ieeexplore.ieee.org/document/11069261
- **Abstract**: In recent years, the application of artificial intelligence (AI) in wireless communications has demonstrated inherent robustness against wireless channel distortions. Most existing works empirically leverage this robustness to yield considerable performance gains through AI architectural designs. However, there is a lack of direct theoretical analysis of this robustness and its potential to enhance communication efficiency, which restricts the full exploitation of these advantages. In this paper, we adopt an information-theoretic approach to evaluate the robustness in wireless distributed learning by deriving an upper bound on the task performance loss due to imperfect wireless channels. Utilizing this insight, we define task outage probability and characterize the maximum transmission rate under task accuracy guarantees, referred to as the task-aware  $\epsilon $ -capacity resulting from the robustness. To achieve the utility of the theoretical results in practical settings, we present an efficient algorithm for the approximation of the upper bound. Subsequently, we devise a robust training framework that optimizes the trade-off between robustness and task accuracy, enhancing the robustness against channel distortions. Extensive experiments validate the effectiveness of the proposed upper bound and task-aware  $\epsilon $ -capacity and demonstrate that the proposed robust training framework achieves high robustness, thus ensuring a high transmission rate while maintaining inference performance.

## Single Carrier SCMA Detection Schemes for Frequency Selective Channels

- **ID**: ieee:11024121
- **Type**: journal
- **Published**: Nov. 2025
- **Authors**: Tianzhu Qin, Ziyi Yang, Jia'ao Liang +2
- **PDF**: https://ieeexplore.ieee.org/document/11024121
- **Abstract**: Sparse code multiple access (SCMA) is a candidate technology for future wireless communication systems to enhance network access capacity. Existing multi-carrier techniques, such as orthogonal frequency division multiplexing (OFDM) that are based on SCMA schemes, are well-researched and considered promising for future 6G mobile communication networks. However, the high peak-to-average power ratio (PAPR) issue stemmed from the multi-carrier schemes limits the applications of SCMA in long-distance transmission scenarios and low-cost sensor networks. To address this issue, single-carrier based SCMA transmission scheme (SC-SCMA) with low PAPR has been proposed. However multi-user signal detection remains a significant challenge for SC-SCMA, particularly with frequency-selective channels (FSC). In this paper, we establish the self-interference analysis model of the SC-SCMA system in FSC and construct an extended factor graph (EFG) for multi-user detection. Based on that, we propose the Gaussian approximate interference based belief propagation algorithm processing on EFG (E-GAIBP) to realize efficient detection over FSC with reduced complexity. Meanwhile, an extrinsic information transfer (EXIT) chart is introduced to analyze the detection performance and convergence properties of the E-GAIBP detector. Finally, to further improve performance gains, we propose two joint E-GAIBP detection and LDPC decoding schemes, E-GAIBP-JDD and layered E-GAIBP-JDD. Numerical results and complexity evaluations show that the layered E-GAIBP-JDD excels in detection performance and convergence speed, offering an effective receiver design strategy.

## Impact of Distributed Raman Amplification on OSNR in Unrepeatered ESCL Transmission

- **ID**: ieee:11282420
- **Type**: conference
- **Published**: 9-13 Nov. 
- **Authors**: D. A. Shaji, B. J. Puttnam, R. S. Luís +12
- **PDF**: https://ieeexplore.ieee.org/document/11282420
- **Abstract**: We investigate the impact of distributed Raman amplification on OSNR in ESCL wideband transmission, comparing short and extended-reach links. While a marginal improvement in OSNR is observed at 50 km, a significant enhancement is observed at 150 km, yielding a 39.0 % improvement in FEC-decoded throughput.

## Experimental Evaluation of an OFDM THz Communication System with LDPC and Turbo Codes

- **ID**: ieee:11351268
- **Type**: conference
- **Published**: 9-12 Nov. 
- **Authors**: Kazuya Takashima, Masafumi Moriyama, Hirokazu Sawada +1
- **PDF**: https://ieeexplore.ieee.org/document/11351268
- **Abstract**: With the recent increase in demand for high-capacity communications, terahertz (THz) communications, which take advantage of largely unused spectrum resources, have attracted significant attention as terabit-per-second (Tb/s) throughput will be required in beyond-6G systems. However, THz bands suffer from severe free-space path loss and multipath fading. In this study, we conducted a wireless transmission experiment employing orthogonal frequency division multiplexing (OFDM) modulation at 289.44 GHz and evaluated the error correction performance of advanced coding schemes, low-density parity-check (LDPC) and turbo codes. Using a transceiver for 8 GHz band IF signals and mixers capable of frequency conversion to THz band, transmission was carried out over distances of 0.5–3 m at a maximum sampling rate of 250 MSamples/s, while receiver demodulates signal and measures bit error rate (BER). As a result, with 0.5 m transmission and LDPC-coded 64 quadrature amplitude modulation (64-QAM), a maximum bit rate of approximately 0.48 Gb/s was achieved under the condition of BER ≤ 10−3. These results demonstrate the effectiveness of error correction coding and modulation scheme selection for future THz communication systems, highlighting their potential for improved reliability and extended transmission distance.

## Characterization of Power-Domain NOMA Versus MIMO in 6G OFDM Networks

- **ID**: ieee:11365759
- **Type**: conference
- **Published**: 9-12 Nov. 
- **Authors**: Fabbryccio Akkazzha Chaves Machado Cardoso, Francisco Raimundo Albuquerque Parente, Maykon Renan Pereira da Silva
- **PDF**: https://ieeexplore.ieee.org/document/11365759
- **Abstract**: The evolution towards Sixth-Generation (6G) systems requires strategies to increase spatial capacity beyond conventional methods. This paper analyzes the feasibility of Power-Domain Non-Orthogonal Multiple Access (PD-NOMA) as a complement to Multiple-Input Multiple-Output Orthogonal Frequency-Division Multiplexing (MIMO-OFDM) in dense 6G cellular networks. Using an open-source simulation framework developed on Sionna 0.16, we model MIMO systems with $1\times 2,\ 2 \times 2$, and $4 \times 4$ antenna configurations. We incorporate PD-NOMA by superimposing two non-orthogonal streams per MIMO layer under clustered delay line channel models from 3GPP Technical Report 38.901, while preserving the same spectral efficiency. Simulation results demonstrate that PD-NOMA can double the number of streams (or users) with minimal Eb/N0 overhead. In non-line-of-sight environments, reception diversity helps mitigate the resulting interference, whereas line-of-sight scenarios benefit from stronger channel eigenvalues, which reduce error propagation. We further quantify the influence of power allocation ratios and MIMO order on the block error rate, providing practical guidelines for system parameter tuning under diverse channel conditions. Finally, we analyze limitations due to interstream interference remaining after minimum mean square error detection and propose residual leakage metrics, highlighting open research challenges in advanced interference cancellation. Overall, the results support PD-NOMA as a low-complexity and costeffective strategy for enhancing spatial capacity in 6 G networks, assuming sufficiently accurate channel state information and feasible iterative decoding at the receiver.

## ICA-Based Grant-Free Access With DPSK-Aided Carrier Frequency Offset Compensation

- **ID**: ieee:11351025
- **Type**: conference
- **Published**: 9-12 Nov. 
- **Authors**: Mitsutoshi Nakata, Takanori Hara, Kenichi Higuchi
- **PDF**: https://ieeexplore.ieee.org/document/11351025
- **Abstract**: This paper proposes a carrier frequency offset (CFO) compensation scheme using differential phase-shift keying (DPSK) for grant-free access based on independent component analysis (ICA). The proposed scheme applies DPSK-aided phase correction, eliminating the need for channel estimation and mitigating performance degradation in active user detection and data detection caused by CFO. Furthermore, by introducing LLR-based thresholding, the scheme reduces the false-alarm probability (FAP) compared to the conventional classifier-diversity-combining based ICA (CDC-ICA). Simulation results demonstrate that, under CFO, the proposed scheme achieves lower bit error rate (BER) and miss detection probability than the conventional scheme, while effectively balancing FAP and BER.

## Simulation and Performance Analysis of the Communication Link Between Earth and Moon

- **ID**: ieee:11383966
- **Type**: conference
- **Published**: 8-10 Nov. 
- **Authors**: Lijuan Gao, Jiong Li, Long Chen
- **PDF**: https://ieeexplore.ieee.org/document/11383966
- **Abstract**: The communication link between Earth and Moon is a bridge connecting the Earth station and the lunar probe, which is crucial for conducting lunar exploration. It analyzes the tasks, operating frequencies, modulation methods of the communication link between the Earth and the Moon, and further analyzes the physical factors, space environment factors, equipment factors, orbit factors, which affect the performance of the communication link between the Earth and the Moon. Combined with simulation software, it simulates and analyzes the link performance parameters corresponding to these factors, including signal loss, duration, Doppler frequency shift, etc. Then it analyzes the C/n0 and information transmission rate of the communication link between the Earth and the Moon, in order to provide the high-speed data transmission in subsequent lunar exploration.

## Adaptive Layered Enhanced Min-Sum Decoding for Short-Block LDPC Codes in Low-SNR and Burst-Prone Communication Systems

- **ID**: ieee:11455032
- **Type**: conference
- **Published**: 7-9 Nov. 2
- **Authors**: Guangyi Luo, Dasheng Zhao, Yidu Zhang
- **PDF**: https://ieeexplore.ieee.org/document/11455032
- **Abstract**: Low-bitrate voice and telemetry systems require short LDPC codes with low decoding complexity. This paper presents ALEMS, an Adaptive Layered Enhanced Min-Sum framework for short codes operating under low SNR and bursty conditions. ALEMS combines layered scheduling for fast convergence, an improved Min-Sum core with normalized or offset correction, and adaptive control with an early-stopping policy. These techniques retain the simplicity of Min-Sum decoding while reducing message saturation and trapping effects common in short codes. Simulations using rate-1/2 short LDPC codes over AWGN and Gilbert-Elliott channels show consistent BER and FER gains over normalized Min-Sum and sum-product algorithms, together with fewer iterations and lower stall probability. Under bursty conditions, modest interleaving further enhances robustness without added cost. Fully compatible with QC-LDPC structures and fixed-point realizations, ALEMS offers a balanced solution between theoretical reliability and hardware efficiency for short-block, low-rate applications such as digital voice and narrowband modems.

## High-Performance Secret Sharing Using Low-Density Parity-Check Codes

- **ID**: ieee:11385099
- **Type**: conference
- **Published**: 7-9 Nov. 2
- **Authors**: Guangfu Wu, Ruyun Wang, Rui Wu
- **PDF**: https://ieeexplore.ieee.org/document/11385099
- **Abstract**: Traditional Shamir secret sharing, while offering information-theoretic security, relies on polynomial interpolation with O(n^2) computational complexity, creating a performance bottleneck in large-scale distributed storage scenarios. This paper presents an LDPC-code-based secret sharing scheme that leverages the sparse matrix properties and linear-time encoding/decoding to significantly boost performance. Experimental results show that the LDPC scheme is faster than the Shamir scheme in both share generation and secret reconstruction and also demonstrates good scalability.

## FPGA Implementation of 5G NR QC-LDPC Codes

- **ID**: ieee:11350474
- **Type**: conference
- **Published**: 7-8 Nov. 2
- **Authors**: Susan G Varghese, Rishika Prabeed Kumar, Inshal Hamidi
- **PDF**: https://ieeexplore.ieee.org/document/11350474
- **Abstract**: The rapid development of $\mathbf{5 G}$ communications technology has triggered higher demands for efficient error correction techniques to meet the needs of ultra-reliable, low-latency, and high-throughput data transmission. Quasi-Cyclic Low-Density Parity-Check (QC-LDPC) codes have been chosen as the 5 G New Radio (NR) standard because they can overcome conventional error correction techniques. These codes are crucial to enable enhanced Mobile Broadband (eMBB) and Ultra-Reliable Low Latency Communication (URLLC) applications by providing strong data integrity with low processing requirements. Nevertheless, hardware implementation of QC-LDPC encoding is extremely challenging because of its high computational complexity and need for adaptability to enable a wide range of code rates and block sizes. This paper is focused on designing and implementing a low-latency, high-throughput QC-LDPC encoder based on FPGA technology that overcomes these issues through optimized algorithms and architectural advancements. The approach encompasses the study of 5 G NR encoding needs, the development of an extremely parallel QC-LDPC encoding algorithm, and implementation on a programmable hardware platform. The encoder features pipeline optimization and parallel cyclic shift networks for enhancing efficiency. The design is synthesized in Verilog HDL and implemented on Nexys 4 DDR FPGA board to support various base graph configurations and lift sizes needed by 5G NR requirements. FPGA testing shows significant improvements in encoding latency, throughput, and resource utilization. With the realization of a fully functional and adaptive encoding chain, this research offers a high-performance and scalable solution for 5G applications and facilitates the development of next-generation wireless communication systems.

## Performance Evaluation of Polar Coded GFDM in Massive MIMO Systems for Next-Generation Wireless Networks

- **ID**: ieee:11350801
- **Type**: conference
- **Published**: 7-8 Nov. 2
- **Authors**: Divya Jain, Debendra Kumar Panda
- **PDF**: https://ieeexplore.ieee.org/document/11350801
- **Abstract**: This paper provides an investigation into the performance of Polar Coded Generalized Frequency Division Multiplexing (GFDM) in a Massive MIMO environment for future generation wireless communication networks. The GFDM system is combined with Polar codes to provides high capacity and low complex decoding and enhances the reliability and spectral efficiency. In this scenario 8 transmitting antennas are considered while the receiving antennas are varied as 16, 32 and 64. Bit Error Rate (BER) and spectral efficiency are used as performance indicators to measure system performance. The simulation is executed using MATLAB over a Rayleigh fading channel with 512-QAM modulation. The results clearly show that as the number of receiving antennas increases, both spectral efficiency and BER improve significantly. This validates the benefit of combining polar coding with GFDM, as it provides the system with improved error rate and highly spectrally efficient system in massive MIMO environment.

## A Comprehensive Survey on Power Optimization in Wired Ethernet Platforms: From Cpus, Tcams, Ethernet Ports and Layer 3 Routing Extensions

- **ID**: ieee:11401902
- **Type**: conference
- **Published**: 7-8 Nov. 2
- **Authors**: Sivakumar Ashokkumar
- **PDF**: https://ieeexplore.ieee.org/document/11401902
- **Abstract**: As artificial intelligence has become increasingly prevalent, the energy consumption of data centers is anticipated to increase significantly. Network infrastructure is projected to contribute substantially to the overall power consumption of datacenters. With escalating demand for network resources, this percentage is expected to grow rapidly. Numerous studies have been conducted by both academic and industry sectors to develop energy-efficient network components. Most existing surveys have focused on generalized energy-saving strategies across network ecosystems. This study aimed to investigate the energy efficiency at the component level. The survey delineates the methods, test results, and key findings on components such as CPU cores, Ethernet ports, and TCAMs, offering reference and guidance for hardware and platform engineering in component selection, CPU scheduling, TCAM sizing, and routing decisions.

## Building Reliable Covert Timing Channels via Error Correction Codes

- **ID**: ieee:11309533
- **Type**: conference
- **Published**: 6-8 Nov. 2
- **Authors**: Manh Hung Ngo, Van Tong, Duc Tran +2
- **PDF**: https://ieeexplore.ieee.org/document/11309533
- **Abstract**: Improving the reliability of covert timing channels (CTCs) influenced by varying network factors such as latency and packet loss is a critical challenge. To address this difficulty, we empirically assess the effectiveness of applying error correction code (ECC) techniques as potential solutions. The results indicate that ECCs greatly increase data recovery; however, the performance between schemes differs significantly. Our research reveals the Reed-Solomon code as the most successful way to handle erroneous data in CTCs, while other ECC techniques, such as LDPC in the employed configuration, do not demonstrate an effective fit for these types of channels. We also quantify the reliability-time trade-off for processing larger data, establishing a practical limit on the size of fully recoverable messages. This study gives in-depth quantitative insights and practical design criteria, contributing to the building of more reliable hidden network channels.

## A Comprehensive Review of Signal Processing Applications

- **ID**: ieee:11388350
- **Type**: conference
- **Published**: 6-8 Nov. 2
- **Authors**: Kapil Sethi, Vivek Sharma, Neha Gupta +3
- **PDF**: https://ieeexplore.ieee.org/document/11388350
- **Abstract**: Signal processing is an essential technology that is common to a vast array of modern technologies since it allows raw data to be analyzed, interpreted, and transformed into useful information. This review paper has provided a forum for each application's use of signal processing technique and it has also covered a lot of ground. This paper has reviewed the extensive applications of signal processing in each of the main domains discussed, namely communication systems, medical imaging, speech recognition, and emerging technologies like AI and IoT. In addition to traditional signal processing methods (e.g., filtering, Fourier methods, and wavelet transforms) we have reviewed more modern approaches including deep learning and quantum computing. We incorporated a comparative evaluation of how the classical approaches and machine learning provides its own opportunities and challenges. We provided an overview of limitations such as model interpretability and explain ability, benefits of real-time processing and missing data, and limitations of multi-sensory or multimodal data. We also provided a concise outline of each of the techniques we have reviewed and their application area, and even reported some of the current deficiencies of research in these areas in figure 3. We hope this review paper provides a comprehensive overview and direction to researchers, practitioners and students for learning about signal processing, both in terms of foundational principles and its dynamic frontiers.

## Deep Learning-Based Interference Mitigation for MRC and EGC Receivers in LIS Systems

- **ID**: ieee:11394350
- **Type**: conference
- **Published**: 5-9 Nov. 2
- **Authors**: M. Marques da Silva, G. Pembele, R. Dinis
- **PDF**: https://ieeexplore.ieee.org/document/11394350
- **Abstract**: Large Intelligent Surfaces (LISs) are key enablers of 6 G networks, providing ultrahigh data rates and low latency through massive antenna arrays. Low-complexity receivers such as Maximum Ratio Combining (MRC) and Equal Gain Combining (EGC) are attractive for LIS but suffer from interference, while Zero-Forcing (ZF) and Minimum Mean Square Error (MMSE) require computationally expensive matrix inversion. This paper proposes a deep-learning-based receiver that enhances MRC and EGC by replacing iterative interference cancellation with a neural network. The model estimates transmitted symbols directly from interference-corrupted signals, avoiding channel inversion. Simulation results show that the neural approach outperforms ZF, MMSE, and iterative MRC/EGC receivers, achieving performance gains of up to 5 dB with significantly lower complexity, making it suitable for largescale LIS deployments.

## FPGA-based Implementation of Low-Complexity QC-LDPC for Real-Time 50G-PON Systems

- **ID**: ieee:11350830
- **Type**: conference
- **Published**: 5-8 Nov. 2
- **Authors**: Kim KwangOk, Doo KyeongHwan, Chung HwanSeok
- **PDF**: https://ieeexplore.ieee.org/document/11350830
- **Abstract**: A low-complexity QC-LDPC codec for high-speed 50G-PON is implemented on FPGA-based OLT and ONU prototypes. The proposed QC-LDPC achieves 50 Gbps performance with reduced hardware resource utilization. An optical gain of about 8.7 dB and error-free 40 Gbps transmission are demonstrate through real-time testing.

## Received Response Based Heuristic Non-binary LDPC Code for NLOS Ultraviolet Communications

- **ID**: ieee:11350880
- **Type**: conference
- **Published**: 5-8 Nov. 2
- **Authors**: Tian Luo, Yong Zuo, Dong Zhu +3
- **PDF**: https://ieeexplore.ieee.org/document/11350880
- **Abstract**: This paper proposes a heuristic encoding algorithm for non-binary LDPC parity-check matrices. Simulation results indicate that the proposed scheme significantly lowers the system bit error rate resulting from pulse spreading in ultraviolet communication channels.

## Hybrid Check Generalized LDPC Convolutional Codes for Optical Fiber Communications

- **ID**: ieee:11350500
- **Type**: conference
- **Published**: 5-8 Nov. 2
- **Authors**: Yinlong Shi, Kai Tao, Zitao Wei +5
- **PDF**: https://ieeexplore.ieee.org/document/11350500
- **Abstract**: With the increasing throughput in optical fiber communication networks, Forward Error Correction (FEC) design plays a crucial role in countering channel noise and interference. To improve the BER performance, we construct a class of 28%-overhead HC-GLDPC-CCs with the BCH codes as component code. In this paper, we investigate the effects of code length, the number of iterations, and the proportion of GC nodes on GLDPC codes with software implementation, and emulate the error floor performance with FPGA platform. As shown in the FPGA simulation result, the error floor of the concatenated code with 24 iterations is below 10-15 for an input BER of 4.51e-2, and the net coding gain(NCG) is 12.28dB.

## Reliable Raptor Code based OAM division multiplexing free space optical communication system

- **ID**: ieee:11349847
- **Type**: conference
- **Published**: 5-8 Nov. 2
- **Authors**: Zian Wang, Shanyong Cai, Zhiguo Zhang +1
- **PDF**: https://ieeexplore.ieee.org/document/11349847
- **Abstract**: We proposes an OAM-DM FSO system based on Raptor Code. Simulation results show that compared with adaptive LPDC coding (switching between 0.7 and 0.5 code rate), the OAM1 / OAM3 multiplexing system, using the Raptor code with the non-uniform LDPC code (0.7 code rate) as the precoding, has a more stable performance to resist atmospheric turbulence under different turbulence intensities.

## Iterative Demodulation and Decoding of Combined Trellis-Coded Modulation and LDPC Coding for Optical Fiber Communications

- **ID**: ieee:11349848
- **Type**: conference
- **Published**: 5-8 Nov. 2
- **Authors**: Tiancheng Sun, Zhongxing Tian, Qing Wang +3
- **PDF**: https://ieeexplore.ieee.org/document/11349848
- **Abstract**: We propose an iterative demodulation and decoding scheme that integrates trellis-coded modulation with low-density parity-check coding through a unified iterative receiver architecture, The proposed scheme offers a 0.8 dB gain over its counterparts with the same spectral efficiency.

## Efficient Rate-Adaptive Information Reconciliation with LightGBM-Assisted Syndrome Estimation in QKD-Classical Coexistence Networks

- **ID**: ieee:11349946
- **Type**: conference
- **Published**: 5-8 Nov. 2
- **Authors**: Zhuoming Yang, Xun Zhu, Qianhui Guo +4
- **PDF**: https://ieeexplore.ieee.org/document/11349946
- **Abstract**: A rate-adaptive information reconciliation scheme with LightGBM-assisted syndrome estimation is proposed for QKD-classical coexistence networks. Simulation results show that the proposed estimator achieves millisecond-level runtime and consumes less than 0.1% of the computation time demanded by the existing methods. Moreover, the proposed scheme remains effective under QBER fluctuations ranging from 0.012 to 0.074, induced by up to 15 coexisting C-band classical channels with total signal power of 11.76 dBm, achieving an overall average reconciliation efficiency improvement of 10.2% compared to conventional blind schemes.

## Joint Polar-coded Modulation Scheme for Bandwidth-Efficient Short-Reach Optical Interconnnection

- **ID**: ieee:11350889
- **Type**: conference
- **Published**: 5-8 Nov. 2
- **Authors**: Hailian He, Yujia Mu, Junyuan Song +3
- **PDF**: https://ieeexplore.ieee.org/document/11350889
- **Abstract**: We propose a joint polar coded modulation to mitigate system bandwidth limitations in intensity modulation and directly detected (IM/DD) optical interconnection. Experiments demonstrate >2.6 dB improvement in receiver power sensitivity versus conventional PAM4 over 2-km standard single-mode fiber transmission.

## Experimental Validation of 6-Mode Transmission with Neural Network-aided Soft Demapper

- **ID**: ieee:11350726
- **Type**: conference
- **Published**: 5-8 Nov. 2
- **Authors**: Chenxu Huang, Ziyang Lu, Can Zhao +4
- **PDF**: https://ieeexplore.ieee.org/document/11350726
- **Abstract**: We experimentally validate our proposed neural network-aided soft-decision demapper via a 6-mode space-division multiplexing fiber transmission system. The experimental results demonstrate that the proposed demapper outperforms the conventional approach under the assumption of independent and identically distributed Gaussian noise by up to a factor of 80 in terms of bit error rate for 1 Tbps/λ transmission over 73 km.

## FEC-assisted Volterra Nonlinear Equalization for IM/DD Optical interconnection

- **ID**: ieee:11350864
- **Type**: conference
- **Published**: 5-8 Nov. 2
- **Authors**: Xuanwei Liu, Junyuan Song, Rui Wang +3
- **PDF**: https://ieeexplore.ieee.org/document/11350864
- **Abstract**: We propose a FEC-assisted Volterra nonlinear equalization scheme for effective mitigation of MZM-induced nonlinear impairments in high-speed IM/DD systems. Experimental validation on a 80 Gbaud optical PAM4 interconnection demonstrates over 1.5 dB receiver sensitivity improvement compared with conventional methods.

## 50G and B50G Optical Access Networks

- **ID**: ieee:11350772
- **Type**: conference
- **Published**: 5-8 Nov. 2
- **Authors**: Ji Zhou, Haide Wang, Liangchuan Li +2
- **PDF**: https://ieeexplore.ieee.org/document/11350772
- **Abstract**: The telecom operator has already begun commercially deploying 50G passive optical networks (PONs) to enable 10G access for end-users. The standardization of Beyond 50G (B50G) PON will soon be prioritized on the agendas of the International Telecommunication Union Telecommunication Standardization Sector and European Telecommunication Standards Institute. This talk will present the 50G and B50G optical access networks, including the architectures and algorithms.

## FEC-assisted Soft Radius Directed Equalization in Coherent Optical Interconnection

- **ID**: ieee:11349870
- **Type**: conference
- **Published**: 5-8 Nov. 2
- **Authors**: Junyuan Song, Ze Dong, Xiangjun Xin +3
- **PDF**: https://ieeexplore.ieee.org/document/11349870
- **Abstract**: This paper proposes an FEC-assisted soft radius directed equalization with recursive least squares algorithm (FEC-assisted RLS-SoftRDE) algorithm for robust polarization demultiplexing in bandwidth-limited coherent systems. Using soft information from FEC-decoder to generate probabilistic "soft ring" symbol radius estimates, our created a more reliable error reference than hard decisions. Demonstrated in a challenging 60 GBaud DP-64QAM system, the algorithm overcomes bandwidth-induced ISI limitations and mitigates rapid polarization rotation (RSOP). Results show significant gains: >3 dB lower EVM (~-18 dB), LDPC decoding to 1e-5 BER in 3-5 iterations, and 4.5 MHz RSOP tracking capability.

## Decoding of Generalized LDPC Codes Using the BCJR Algorithm

- **ID**: ieee:11301108
- **Type**: conference
- **Published**: 5-7 Nov. 2
- **Authors**: Alexey A. Bandyukov, Andrey A. Metlyakov, Fedor I. Ivanov
- **PDF**: https://ieeexplore.ieee.org/document/11301108
- **Abstract**: Generalized low-density parity-check (GLDPC) codes have emerged as a promising class of error-correcting codes that extend the capabilities of traditional LDPC codes by incorporating more powerful component codes. This paper investigates an approach to construct long GLDPC codes using short component codes. In this scheme, the BCJR algorithm is used as a component decoder and integrated into the belief propagation algorithm. Simulation results demonstrate that constructions incorporating quasi-cyclic LDPC codes yield the best performance. Compared to the conventional decoding approach for LDPC codes, the proposed generalized constructions demonstrated better bit and frame error rate performance. This approach is promising for communication systems that require low latency. A comparison is also provided with LDPC codes constructed using the Progressive Edge-Growth (PEG) algorithm.

## Sampling Rate Optimization for LDPC-Based Information Reconciliation Protocol in QKD

- **ID**: ieee:11301492
- **Type**: conference
- **Published**: 5-7 Nov. 2
- **Authors**: Vladimir Morozov, Oleg Evsutin, Nikita Yarygin
- **PDF**: https://ieeexplore.ieee.org/document/11301492
- **Abstract**: Quantum Key Distribution (QKD) is a promising field in modern cryptography where the security of key information is guaranteed by the laws of quantum mechanics. One of the key stages in QKD protocols is error estimation and reconciliation in the secret key. This procedure requires the transmission of a certain number of secret key bits over a public channel. Such transmission leads to disclosing these bits to a potential eavesdropper. The fraction of disclosed bits—the sampling rate-largely depends on the chosen approach for preliminary error estimation in the channel. This work is devoted to the optimization of the sampling rate for an LDPC code from the $\mathbf{5 G}$ standard. The results of our experiments show that for a QBER below 0.2 and key lengths of 264, 528, 792, and 1056 bits, it is necessary to disclose no more than $18 \%, 11 \%, 10 \%$, and $7 \%$ of the key bits for error estimation, respectively. Furthermore, the proposed algorithm allows for similar optimization for any information reconciliation protocols and actual quantum bit error rates.

## Codes from Layers of Hamming Graphs

- **ID**: ieee:11301429
- **Type**: conference
- **Published**: 5-7 Nov. 2
- **Authors**: Vitaly Danilko, Ivan Mogilnykh
- **PDF**: https://ieeexplore.ieee.org/document/11301429
- **Abstract**: We study the class of codes defined by the row space of the minimum distance relation matrix of t th and l th layers of Hamming graph $H(m, q)$. By concatenating such matrices we obtain many distance-optimal codes of length up to 128. For arbitrary $q, t, n, k$ we prove an analogue of a well-known Wilson rank formula [12] and find the dimensions of the codes in this class. For $t=l-1$, the codes are locally recoverable and include the codes from work of [11] for $q=2$. We show that the codes with $q=2$ are optimal locally-recoverable codes in our class.

## Construction of LDPC Codes for Single Bursts Correction by Masking

- **ID**: ieee:11301552
- **Type**: conference
- **Published**: 5-7 Nov. 2
- **Authors**: Alina Veresova, Andrei Ovchinnikov
- **PDF**: https://ieeexplore.ieee.org/document/11301552
- **Abstract**: This paper addresses the problem of constructing codes for correcting single error bursts. The construction is based on a block-circulant design of low-density parity-check codes. For such a design, the maximal correctable burst length is limited by the block size, which forces consideration of codes whose parity-check matrix contains only a small number of large blocks. However, this significantly restricts the attainable sets of code lengths and code rates, and, aside from a few special cases, such codes may be turned out to be rather far from the Reiger bound on the maximum correctable burst length. To overcome these limitations we introduce a masking procedure and propose a method for constructing a masking matrix based on evaluating the burst correcting capability of a code. Experiments estimating the correcting capability of the proposed codes in comparison with both the original block-circulant construction and with random codes defined by dense parity-check matrices were performed. The proposed methodology provides quasicyclic low-density parity-check codes whose correcting capability substantially exceeds that of block-circulant codes without zero subblocks and, for certain parameter choices, approaches the Reiger bound. The resulting codes also provide greater flexibility in varying the number and size of blocks, enabling more versatile adjustment of code lengths and code rates. Finally, the burst correcting capability of the proposed construction is comparable to that of codes defined by dense parity-check matrices, while its quasi-cyclic structure enables more computationally efficient encoding and decoding procedures.

## On the Correcting Capability of Hard-Decision Error-and-Erasure Iterative Decoding of LDPC Codes for Data Storage

- **ID**: ieee:11301418
- **Type**: conference
- **Published**: 5-7 Nov. 2
- **Authors**: Vladimir Kuzmin, Ilia Chevtaev, Maya Chernaya +2
- **PDF**: https://ieeexplore.ieee.org/document/11301418
- **Abstract**: Modern storage systems such as NAND flash solidstate drives are increasingly exposed to channels where both errors and erasures coexist. Classical Reed-Solomon (RS) codes provide strong error-and-erasure protection but suffer from high decoding complexity and latency, limiting their applicability in high-throughput storage architectures. Low-Density ParityCheck (LDPC) codes, with iterative message-passing decoders, offer near-capacity performance at low complexity and are therefore the preferred solution in practice. While the decoding behavior of LDPC codes has been well studied for pure error or pure erasure channels, the mixed error-and-erasure case has received less attention, despite its direct relevance to storage. In this work, we analyze the potential correction capability of iterative error-and-erasure decoding for LDPC codes under hard-decision channels. Using density evolution, we derive recursion equations for the joint evolution of error and erasure probabilities and establish bounds on the region of correctable error-erasure patterns. The presented results provide theoretical correction bounds that complement existing studies on error-only and erasure-only channels, and offer guidelines for LDPC code and decoder design in storage systems where errors and erasures naturally coexist.

## Analysis of 4K-QAM and 16K-QAM Performance with Chase Combining HARQ under Hardware Non- Idealities in IEEE 802.11bn (Wi-Fi 8)

- **ID**: ieee:11345390
- **Type**: conference
- **Published**: 5-7 Nov. 2
- **Authors**: Roger Pierre Fabris Hoefel
- **PDF**: https://ieeexplore.ieee.org/document/11345390
- **Abstract**: Considering the 2028 IEEE 802.11bn physical layer (PHY) that schedules modulation code schemes (MCS) with either 4096 quadrature amplitude modulation (4K-QAM) or 16K-QAM signaling schemes impaired with phase noise (PN) and carrier frequency offset (CFO), this paper analyses the performance of Chase Combining Hybrid Automatic Repeat Request (CC-HARQ) protocol with Low-Density Parity-Check (LDPC) codes using the following transceiver architecture: transmit beamforming singular value decomposition precoder (SVD) and minimum mean squared error (MMSE) detector. Simulation results show that standard schemes can mitigate the power losses due to CFO, while the system performance is dramatically affected by the joint effects of PN and CFO. Fortunately, the implementation of CC-HARQ protocol can reduce these power losses due to PN and CFO hardware impairments, e.g., from 6.4 dB to 1.6 dB for MCS13 (4K-QAM, LDPC code with code rate 5/6), and from 7.6 dB to 2.0 dB for MCS15 (16K-QAM, LDPC code with code rate 5/6), assuming only two retransmissions. Notably, as quantified in this paper, these performance enhancements due to CC-HARQ protocol depend strongly on PN power, channel model (block fading or independent), and the time scale of channel state information (CSI) feedback mechanism.

## 6G Short Range Wireless Quantum Optical Communications with Sophisticated Channel Coding

- **ID**: ieee:11439655
- **Type**: conference
- **Published**: 4-6 Nov. 2
- **Authors**: Peter Jung, Hamza Almujahed, Kushtrim Dini +1
- **PDF**: https://ieeexplore.ieee.org/document/11439655
- **Abstract**: Research has shown that radio applications above $300 \mathbf{G H z}$ require a very careful analog design that takes into account the frequency-dependent nature of ohmic resistance at these frequencies, bringing optical communication solutions for the sixth generation $(6 \mathrm{G}) \text{THz}$ band located between 300 GHz and 10 THz, being well suited for short range links, into focus. The authors propose wireless quantum optical communications concepts replacing the classical radio frequency based inner physical layer transceivers used in classical channel coded short range wireless systems. Owing to low environmental interaction of such short range links, the coherence and interference ability when knowing and maintaining the carrier phase permits a beneficially robust transmission. Also, on the basis of today's wireless communication systems considering sophisticated channel codes such as the LTE turbo code and the WLAN LDPC code seems to be of greatest interest. Thus, besides illustrating the proposed wireless quantum optical communications concept, the optimum soft output quantum data detector for coherent reception with known carrier phase is discussed and both uncoded as well as novel channel coded bit error ratio performance results are presented.

## Application of BCH-Turbo Product Codes to Electromagnetic Wave Communication in Oil and Gas Wellbores

- **ID**: ieee:11322161
- **Type**: conference
- **Published**: 28-30 Nov.
- **Authors**: Zhilin Li, Xiong Han, Huabin Yang
- **PDF**: https://ieeexplore.ieee.org/document/11322161
- **Abstract**: In the electromagnetic wave command downlink communication system, the electromagnetic wave signal transmission from the ground to the bottom of the well will be subject to very serious interference caused by the industrial frequency, the electrical noise caused by the complex environment of the well, and the natural electrical noise, which leads to the difficulty of the receiver to extract the accurate signals, and the signal error code is serious. Aiming at this problem, this paper proposes a BCH-Polar cascade code constructed based on improved genetic algorithm, evaluates the adaptability of individuals in the genetic algorithm by building a simulation system with fading channel and specific decoding algorithm, constructs a Polar code applicable to BCH-Polar cascade scheme under fading channel, combines with the random interleaving technique to disrupt the burst errors into random errors, and proposes a BCH-SCL decoding scheme to reduce the error in the BCH-Polar cascade scheme, and proposes a BCH-SCL decoding scheme to reduce the error in the BCH-SCL decoding scheme. A BCH-SCL decoding algorithm is proposed to further improve the error correction performance of the decoding algorithm. The experimental results show that the proposed method has better performance in high noise fading channels, when the BER reaches 10-6, the 1/3 code rate BCH-Polar cascade code has a performance gain of nearly 2dB compared with the (3, 1, 7) convolutional code, and a performance gain of about 1.2dB compared with the (255, 99) BCH code, and the inevitable BER level of the Turbo multiply-convolutional code is greatly reduced. Flat layer. After laboratory and real-well testing, the communication distance is 544m, basically it can realize error-free transmission, and it can meet the requirements of the electromagnetic wave command downlink communication system of oil and gas wellbore, and it has strong advantages in the communication system of oil and gas wellbore electromagnetic wave transmission with serious attenuation and strong noise interference.

## Real-time Transmission and Remote Intelligent Diagnosis of Oscillation Wave Detection Data for Dry-Type Reactors Based on 5G+MEC

- **ID**: ieee:11322151
- **Type**: conference
- **Published**: 28-30 Nov.
- **Authors**: Minhu Xu, Chengnan Cui, Hang Zhang +3
- **PDF**: https://ieeexplore.ieee.org/document/11322151
- **Abstract**: To address the poor real-time data transmission performance of oscillation wave detection in dry-type reactors and the insufficient diagnostic capabilities of traditional algorithms using small sample sizes, a diagnostic solution combining a 5G+MEC real-time transmission system and an improved temporal convolutional network (ITCN) is proposed. The transmission system utilizes a "one-station-one-node" MEC deployment, combining Kalman filter preprocessing with LZ77 compression (reducing data volume by 60%). A dedicated 5G slice (uplink/downlink bandwidth of 20/10 Mbps) and HARQ+LDPC security are designed, resulting in end-to-end latency of ≤50ms and packet loss rate of ≤0.5%. The ITCN embeds a channel-temporal dual attention mechanism, adds three-scale parallel branches (K=3/5/7), and uses depthwise separable convolution for lightweighting (reducing the number of parameters by 68.3%). A 10,000-set data set (split 7:3) was constructed based on a 10kV reactor platform. Simulations showed that 5G+MEC achieved a latency of 22ms (a 74.1% reduction compared to 4G) and a 1.1% packet loss rate for 25MB of data (compared to 8.7% for 4G). The ITCN test set achieved an accuracy of 98.7%, representing improvements of 6.2%, 10.5%, and 8.3% over traditional TCN (92.5%), CNN (88.2%), and LSTM (90.4%), respectively. The recall rate for mild inter-turn short circuits reached 96.5%, and the inference time was 18ms, meeting the real-time diagnostic requirements of the project.

## An Emerging Wireless Technology With Progressive Approach Visible Light Communication

- **ID**: ieee:11450627
- **Type**: conference
- **Published**: 28-29 Nov.
- **Authors**: Nidhi Bhukar, Surender K. Grewal
- **PDF**: https://ieeexplore.ieee.org/document/11450627
- **Abstract**: Visible light communication technology is an emerging futuristic approach wireless technology in which transmission of data is based on the utilization of visible part of (380 nm-750 nm) electromagnetic spectrum. VLC is considered as an optimal alternative to RF communication in order to satisfy the users need of lighting and communication. This paper represents the introduction of VLC with its applications, evolution from origin to till now and basic components of VLC including transmitters and their types followed by different types of channels and receiver. Lastly different filtering stages and some of research concerns in VLC has been discussed. This review of VLC technology provides users a very clear comprehensible, sorted understanding of existing research issues and emphasises potential concerns and prospects to guide further research in this area.

## Deep-Learning-Assisted Vector Symbol Decoding

- **ID**: ieee:11279869
- **Type**: conference
- **Published**: 26-28 Nov.
- **Authors**: Thitikorn Suwannapeng, Usana Tuntoolavest
- **PDF**: https://ieeexplore.ieee.org/document/11279869
- **Abstract**: Locating error symbol positions is a necessary step for Vector Symbol Decoding (VSD). The existing method is done algebraically. Deep learning (DL) is proposed to locate the error symbol positions either more accurately (DL-assisted VSD) or more quickly with fixed time (DL-driven VSD). VSD can be used to provide more reliable data transmission in channels with burst errors such as wireless, mobile and power line channels. Using the feature that VSD knows when it fails to decode, DL is proposed to further decode after VSD fails. This leads to more successful decoding. Thus, this DL-assisted VSD always provides the same or better decoding performance than VSD. On the other hand, replacing the algebraic calculation of error-locating vector with DL-driven VSD provides lower decoding performance than VSD, but leads to faster decoding time. Thus, DL-driven VSD can be considered when time is more critical than performance.

## GPU implementation of binary and non-binary LDPC decoding

- **ID**: ieee:11318914
- **Type**: conference
- **Published**: 25-28 Nov.
- **Authors**: Mark Mizzi, Johann A. Briffa
- **PDF**: https://ieeexplore.ieee.org/document/11318914
- **Abstract**: Since their rediscovery in the 1990s, Low-Density Parity-Check (LDPC) codes have dominated the field of capacity-approaching error correcting codes, and are currently used in a number of practical applications. The recent use of these codes in quantum key distribution (QKD) systems often requires much larger codeword sizes than previously considered, and has renewed interest in LDPC codes with non-binary alphabets. Both aspects introduce a significant increase in computational complexity, so that real-time implementation in practical QKD systems remains a challenge. In this work we propose a GPU-accelerated LDPC decoder for binary and non-binary alphabets, evaluating its performance in comparison to a reference CPU implementation and to earlier GPU and CPU implementations, for a range of field sizes and codeword lengths.

## FIT-IRSA: Feedback-Integrated Two-Phase IRSA with Deep Reinforcement Learning

- **ID**: ieee:11304049
- **Type**: conference
- **Published**: 25-27 Nov.
- **Authors**: Andrei-Valentin Stirbu, Cédric Adjih
- **PDF**: https://ieeexplore.ieee.org/document/11304049
- **Abstract**: Efficient random access can be used in scenarios with a massive number of IoT devices. Among modern random access protocols, Irregular Repetition Slotted ALOHA (IRSA) offers excellent asymptotic performance (for large frame sizes), but its finite-frame efficiency is lower and difficult to optimize analytically. In this work, we introduce limited mid-frame feedback to better coordinate users and improve performance: Feedback-Integrated Two-phase IRSA (FIT-IRSA). We formulate IRSA with feedback as a deep reinforcement learning (DRL) problem. Using policy gradient methods, we learn transmission strategies that improve throughput under varying loads, as demonstrated in our simulation results. This provides a practical alternative to classical density-evolution–based optimization, which applies mainly to large frames.

## An Implementation Method of a Ultra-High Speed Variable Block Code Data Encoding and Decoding Structure

- **ID**: ieee:11398590
- **Type**: conference
- **Published**: 21-23 Nov.
- **Authors**: Qiang Zhang, Qi Shan, Zhenyu Song
- **PDF**: https://ieeexplore.ieee.org/document/11398590
- **Abstract**: With the increase of satellite communication data, the modem in the ground application system is required to have a higher codec rate and communication capacity. This paper proposes a method for implementing an ultra-high speed variable block code data encoding and decoding structure, which supports serial frame input of correlated ultra-high speed block code data, completes ultra-high speed parallel encoding and decoding, and achieves independent and stable output of ultra-high speed data serial frames. The method proposed in this paper is applicable to FPGA based ultra-high speed variable block code data encoding and decoding, compatible with various block codes such as LDPC, RS, BCH, and multi rate encoding and decoding; Adopting a parallel structure processing approach to rapidly improve the modem throughput of satellite ground application systems; The software calculates the number of parallel loop modules for highspeed data caching, drives the loading of corresponding FPGA bitstreams, quickly reconstructs FPGA encoding and decoding structures, flexibly allocates resources, and improves resource utilization.

## Design of a Realistic Device-Independent QKD System

- **ID**: ieee:11344594
- **Type**: conference
- **Published**: 2-5 Nov. 2
- **Authors**: Ugo Chirico, Salvatore Cuomo, Miriam Del Latte +1
- **PDF**: https://ieeexplore.ieee.org/document/11344594
- **Abstract**: Device-Independent Quantum Key Distribution (DI-QKD) represents the pinnacle of secure quantum communication, offering cryptographic guarantees that are independent of the trustworthiness of the devices used. Unlike traditional QKD schemes that rely on specific assumptions about internal device behaviour, DI-QKD leverages the violation of Bell inequalities to certify security solely from observed statistics. This approach eliminates a wide range of side-channel and implementation attacks, making it especially attractive for critical infrastructures and defense applications. The core concept hinges on the ability of the communicating parties, traditionally named Alice and Bob, to generate shared secret keys through the violation of Bell inequalities verified at a central node, named Charlie, regardless of hardware imperfections. Previous works demonstrated the feasibility of a Bell-certified key exchange over a real optical channel using a heralded entanglement scheme. This work aims to build on that foundation, presenting a full-stack engineering implementation of a DI-QKD system that includes industrial-grade entangled photon sources, high-efficiency SNSPD detectors, central-node heralding logic, and a real-time software stack for key management, observability, and integration with classical IT infrastructure.

## ORSGRAND: Hardware-Efficient Ordered Reliability Symbol GRAND Decoder for Low-Latency Multiuser IoT Applications

- **ID**: ieee:11270656
- **Type**: conference
- **Published**: 17-19 Nov.
- **Authors**: Arslan Hassan, Muhammad Adeel Pasha, Momin Uppal
- **PDF**: https://ieeexplore.ieee.org/document/11270656
- **Abstract**: The development of next-generation communication systems has made it possible to realize Ultra Low-Latency Communication (ULLC). For these applications, bandwidth and energy efficiency requirements are only met by short-length high-rate codes. To decode these codes, in resource-constrained reconfigurable devices, universal code-agnostic decoders such as GRAND are making breakthroughs. However, their treatment in modern communication scenarios like Non-Orthogonal Multiple Access (NOMA) and multiuser communication has not yet been fully explored as GRAND decoders have been primarily designed for single-user settings. To address this challenge, we present symbol decoding with Ordered Reliability Symbols GRAND (ORSGRAND) decoder and its comparison with a more straightforward choice of multiuser detection using GRAND and NOMA with Successive Interference Cancellation (NOMA-SIC). Our results demonstrate a comparative analysis of both approaches. The NOMA-SIC design provides comparatively better Frame Error Rate (FER) performance. However, its sequential processing leads to higher latency and reduced throughput. In contrast, the ORSGRAND design operates at the symbol level and simultaneously decodes data for two users, significantly reducing latency and achieving higher throughput with an acceptable FER performance. This makes ORSGRAND a superior candidate for latency-sensitive Internet-of-Things (IoT) applications where throughput is a key performance metric.

## PUF-Enhanced Physical-Layer Key Generation for Secure Drone Communication with Untrusted Relays

- **ID**: ieee:11354957
- **Type**: conference
- **Published**: 14-17 Nov.
- **Authors**: Tao Chen, Dongming Li, Xianglin Fan +1
- **PDF**: https://ieeexplore.ieee.org/document/11354957
- **Abstract**: Physical-layer key generation (PLKG) has attracted significant attention due to its lightweight and strong randomness, making it highly suitable for drones with energy and computational constraints. However, when drone communications rely on relay nodes, untrusted relay nodes may launch attacks such as eavesdropping, tampering, replay and man-in-the-middle, leading to key leakage. To address this problem, we propose a drone -physical unclonable functions (PUFs) - PLKG (DPPLKG) scheme that enhances resistance to untrusted relay attacks. In DPPLKG, legitimate drones are equipped with paired PUF hardware, and artificial noise is injected during the PLKG process to reduce the accuracy of untrusted relay channel estimation. The generated physical-layer key serves as the PUFs challenge, and the unique hardware response of PUFs generates the final session key, ensuring consistent and secure key generation among legitimate drones. After analysis, DPPLKG can effectively resist various threats such as relay eavesdropping, tampering, replay, and impersonation attacks. The simulation results show that DPPLKG outperforms traditional PLKG in terms of key generation rate, bit error rate, and key entropy. It can also resist Doppler frequency changes caused by drone mobility and hardware noise caused by temperature changes in PUF devices. In addition, the proposed scheme has an acceptable delay time, making it a practical and efficient solution for achieving drone secure communications in the presence of untrusted relays.

## Privacy-Preserving Facial Authentication with Hybrid Fuzzy Commitment and Cancelable Transformation

- **ID**: ieee:11354628
- **Type**: conference
- **Published**: 14-17 Nov.
- **Authors**: Weilai Guo, Shuaichao Song, Yeming Yang +3
- **PDF**: https://ieeexplore.ieee.org/document/11354628
- **Abstract**: The widespread deployment of deep learning-based face recognition systems raises significant concerns regarding the security and privacy of their stored facial templates. Unlike passwords, a compromised template is irrevocable and can be inverted to reconstruct the user’s original biometric data, leading to permanent privacy loss. To address this problem, various biometric cryptosystems based on fuzzy commitment(FC) have been introduced. However, FC suffers from two critical challenges when applied to facial templates: the real-valued templates and their high intra-class variations, which typically exceed the error-correction capacity of FC. Our scheme addresses these issues by binarizing the deep features via Sliding Window Grouping MinHash, subsequently applying a Fisher score-based mask to select stable bits, ultimately minimizing intra-class dissimilarity to enable robust matching with LDPC codes. Extensive experiments were conducted on publicly available benchmark datasets, including LFW, ColorFERET, CASIA-WebFace, and FEI. The results demonstrate that our scheme achieves high authentication accuracy while also fulfilling the critical security requirements for template protection: irreversibility, revocability, and unlinkability.

## Design and Implementation of an Efficient Parallel Decoding Algorithm for Regular LDPC Codes with Girth Length of Eight

- **ID**: ieee:11512606
- **Type**: conference
- **Published**: 14-16 Nov.
- **Authors**: Yanjun Ji, Xiao Ji Wei, Qinwei Yao +1
- **PDF**: https://ieeexplore.ieee.org/document/11512606
- **Abstract**: The rapid expansion of the Internet of Things (IoT), robotics, and automated control systems has created a critical demand for high-throughput, low-latency wireless communication. This paper presents the hardware implementation of an efficient parallel decoding algorithm for regular Low-Density Parity-Check (LDPC) codes, constructed with a girth of eight to avoid short cycles. The codes are constructed using a geometric approach based on balanced incomplete block designs (BIBD) to ensure a minimum girth of eight. The design was developed using geometric methods, implemented on the Quartus platform with Verilog Hardware Description Language (HDL), and includes the circuit design and simulation for core modules. Synthesized and deployed on a Stratix II FPGA (EP2S90F1020C3), the decoder achieves a maximum data processing rate of 10 Mbps with robust error correction capabilities. A key innovation is the standardization of all internal information in the decoding process to a uniform format, which eliminates the need for additional data conversion, thereby reducing hardware complexity and computational delay. This makes the design particularly suitable for real-time applications in IoT and robotic systems. In summary, the proposed decoder achieves a 25% reduction in clock cycles for check node updates and a processing throughput of 10 Mbps on FPGA hardware. This work demonstrates a practical and efficient decoding solution that meets the stringent requirements of modern real-time communication systems in IoT and robotics.

## Anti-Screen-Shot Digital Watermarking Technology in DWT-DCT Hybrid Domain with Optimized LDPC Coding

- **ID**: ieee:11385203
- **Type**: conference
- **Published**: 14-16 Nov.
- **Authors**: Xibin Xu, Xiaolei Zhao
- **PDF**: https://ieeexplore.ieee.org/document/11385203
- **Abstract**: In order to solve the problem of copyright protection of digital image in the scene of screen shooting, a digital watermarking technology in DWT-DCT mixed domain based on LDPC coding optimization is proposed. Taking the Y channel as a carrier, screening a high texture area through block variance, performing DWT decomposition and DCT transformation on the selected area, dynamically adjusting the embedding strength at the position of the middle frequency of the low-frequency sub-band, embedding the watermark, and repeatedly embedding the watermark; The watermark is LDPC encoded to enhance the error correction capability. The embedded block is located during extraction, and the watermark is recovered through mixed domain feature extraction, LDPC iterative decoding and multi-region weighted voting. Experiments show that the technology has both invisibility and anti-interference under the typical interference of screen shooting, and provides a reliable scheme for digital image copyright protection.

## Impact of Forward—Error—Correction Codes on Bit Error Rate in DVB-S2 System under Wide-Band Interference

- **ID**: ieee:11383947
- **Type**: conference
- **Published**: 14-16 Nov.
- **Authors**: HongYu Wu, Langzheng Zhou, Zhaodong Gao +6
- **PDF**: https://ieeexplore.ieee.org/document/11383947
- **Abstract**: This paper investigates the impact of forward error correction (FEC) codes, specifically the concatenated Low-Density Parity-Check (LDPC) and Bose-Chaudhuri-Hocquenghem (BCH) codes, on the bit error rate (BER) performance of the DVB-S2 system under wide-band interference. Through controlled experiments, we evaluate the capabilities for the LDPC-BCH concatenated coding against additive white gaussian noise (AWGN) interference by measuring BERs under different carrier-to-interference ratios, symbol rates, and interference bandwidths. The experimental results show that the concatenated FEC codes significantly enhance the system's resistance to AWGN interference, improving receiver sensitivity and reducing bit error rate (BER) under different operating parameters. Under various QPSK code rate conditions, after FEC is added, the SNR required for demodulation is reduced by 1.25dB to 9 dB compared to that without coding; and the signal-to-interference ratio (SIR) required for correct demodulation after interference injection is decreased by 1.21dB to 9 dB.

## Multi-Contour Intellectual Cyber Protection System Methodology

- **ID**: ieee:11267930
- **Type**: conference
- **Published**: 14-16 Nov.
- **Authors**: Yevhen Melenti, Serhii Yevseiev, Stanislav Milevskyi +3
- **PDF**: https://ieeexplore.ieee.org/document/11267930
- **Abstract**: The development of quantum technologies requires the construction of fundamentally new information protection systems for any security object. The authors propose a methodology for building a multi-contour intelligent system for cyber protection of critical infrastructure objects (security) based on an objective assessment of the current state of the object's security based on post-quantum algorithms and the distribution of infrastructure elements onto separate platforms, taking into account possible targeted attacks on the internal and external circuits. At the same time, for each platform, possible emergent properties of the constituent platforms of socio-cyberphysical systems – social networks, cloud and physical platform – are taken into account. Synthesis of the intellectual component for the assessment of the current state, taking into account the influence not only of social engineering methods, but also of the signs of hybridity, synergy of modern cyber threats, as well as active threats of cybercriminals (cyberterrorists). This approach provides consideration of security in the form of three components: cybersecurity, information security and security of information, and ensures the construction of an intelligent multi-contour information protection system of the protected object. In addition, the integration of post-quantum algorithms (crypto-code constructions based on LDPC codes) with digital information methods provides not only the necessary level of stability, but also the secrecy of the very fact of transmitting any information (by any communication channels).

## Adaptive Modulation with Target-BER Thresholding: BPSK/QPSK/16-QAM Over AWGN

- **ID**: ieee:11416407
- **Type**: conference
- **Published**: 14-16 Nov.
- **Authors**: Yue Wang
- **PDF**: https://ieeexplore.ieee.org/document/11416407
- **Abstract**: Adaptive Modulation Control (AMC) is a key technology for enhancing spectrum efficiency in 5G and future networks, with its performance determined by the switching threshold based on signal-to-noise ratio (SNR). However, a systematic quantitative analysis of how different threshold strategies impact system performance tradeoffs remains lacking. This paper conducts an in-depth investigation into the inherent tradeoff between throughput and reliability for various SNR threshold strategies in AMC systems. This study employs Monte Carlo simulation to design three AMC strategies within an Additive White Gaussian Noise (AWGN) channel model: First, a baseline threshold is calculated based on the target bit error rate. Subsequently, aggressive and conservative strategies are defined by applying $\pm 2.5 ~\text{dB}$ offsets to this baseline. The results quantitatively reveal this performance trade-off: the aggressive strategy achieves maximum throughput at the expense of reliability, with its error rate even exceeding the quality of service (QoS) target in certain intervals; conversely, the conservative strategy guarantees optimal reliability by sacrificing throughput. This study demonstrates that there is no universal AMC strategy. The selection of threshold strategies must align with the specific QoS requirements of the business scenario, such as enhanced mobile broadband (eMBB) or ultra-reliable and low-latency communications (URLLC). These findings provide important reference for the adaptive design of next-generation wireless links.

## A Performance-Aware Framework For LDPC Code Enhancement Using Shortening Techniques

- **ID**: ieee:11430116
- **Type**: conference
- **Published**: 12-13 Nov.
- **Authors**: Bhawna Kamra, Ankit Srivastav, Vamshidhar Kamuganti +1
- **PDF**: https://ieeexplore.ieee.org/document/11430116
- **Abstract**: In Release 15, 3GPP introduced the New-Radio $(5 \mathrm{G})$ wireless technology to support a wide range of use-cases across industries into three main service types: enhanced mobile broadband (eMBB), ultra reliable low latency communication (uRLLC) and massive-machine type communication (mMTC). However, numerous emerging use-cases exhibit requirements that lie in between the defined boundaries of the aforementioned service types. These use-cases do not demand the complete capabilities offered by full-fledged 5 G networks. To address such use-cases, in Release 17, 3GPP introduced the reduced capability NR devices (RedCap) as a tailored solution. The standardized low-density parity check (LDPC) scheme lacks the necessary optimizations for low-complexity hardware requirements for the RedCap Devices. In this paper, a customized LDPC code design framework is proposed to meet the low-complexity requirements of NR RedCap devices, while maintaining acceptable BER levels. Specifically, a shortening technique is implemented to reduce the check node (CN) degree, thereby inherently minimizing both decoder complexity and memory requirements. Shortening method must be meticulously selected to avoid significant performance loss, while maintaining the desired properties like girth and sparsity. Simulation results demonstrate that the achieved BER performance remains within the permissible range recommended by the standard for NR RedCap devices with Check node degree reduction.

## Enhancing Key-Recovery Chosen-Ciphertext Side-Channel Attacks on NTRU Using LDPC

- **ID**: ieee:11310913
- **Type**: conference
- **Published**: 10-12 Nov.
- **Authors**: Denis Nabokov, Xiaofei Tong, Qian Guo
- **PDF**: https://ieeexplore.ieee.org/document/11310913
- **Abstract**: In this work, we introduce novel techniques for adapting the SCA-LDPC framework to NTRU-style Key Encapsulation Mechanisms (KEMs). Our approach significantly reduces the required measurements compared to prior analyses under similar oracle noise, validated through extensive simulations, and shows robustness against decision errors in the constructed oracle. Furthermore, we present the first documented power analysis attack targeting a first-order masked NTRU implementation. We constructed a plaintext-checking (PC) oracle achieving a low 0.5% decision error rate, importantly, within a practical cross-device setting where training and attack devices differ. Our results show that approximately 1250 side-channel measurements are sufficient to recover the secret key in this challenging scenario.

## On the Design, Performance Assessment, and Implementation of Channel codes for improving information integrity in data storage systems

- **ID**: ieee:11288988
- **Type**: conference
- **Published**: 10-12 Nov.
- **Authors**: Achala G, U. Shripathi Acharya, Pathipati Srihari
- **PDF**: https://ieeexplore.ieee.org/document/11288988
- **Abstract**: NAND flash is the primary storage technology in most modern electronic devices. Its evolution has been driven by scaling to increase bit density per cell, which has led to high raw bit error rates (RBER) and reduced data integrity. Multi-level flash devices have greater complexity and even higher RBER. Addressing this requires designing accurate channel models and error correction coding (ECC) algorithms tailored to these models. Our research focuses on modeling the NAND flash channel and synthesizing, implementing both classical and modern ECC techniques optimized for NAND flash architectures, enhancing reliability in contemporary storage systems.

## 3GPP Based LDPC Encoder For 5G-NR Over FPGA

- **ID**: ieee:11317207
- **Type**: conference
- **Published**: 10-12 Nov.
- **Authors**: Puspendra K Upadhyay, Pallav Maheshwari, Gaurav Jajoo
- **PDF**: https://ieeexplore.ieee.org/document/11317207
- **Abstract**: 5G New Radio (NR) offers significantly higher throughput and lower latency compared to its predecessors in communication standards. In 5G, Low Density Parity Check (LDPC) encoding serves as the channel coding scheme for data transmission via shared channels. This work focuses on the Field Programmable Gate Array (FPGA)-based implementation of an LDPC encoder compliant with the 5G-NR Third Generation Partnership Project (3GPP) standards. This paper details the design, development, and evaluation of a generalized LDPC encoder capable of generating codewords for all code rates and payload sizes. The generated Intellectual Property (IP) selects the base graph, calculates the parity matrix, and encodes the data in accordance with T S 38.212. Implementation was carried out using the Xilinx MPSoC ZCU-102 board. The developed IP is tested and verified using the reference output generated by the MATLAB 5G-NR built-in library. Our results demonstrate the efficiency of the LDPC encoder implementation in terms of latency and resource utilization on the evaluation board making it suitable for practical applications.

## SAT–Terrestrial Coexistence With Adaptive Beam and Power Control: An SDR-Based Emulation

- **ID**: ieee:11317599
- **Type**: conference
- **Published**: 10-12 Nov.
- **Authors**: Sreeram Mandava, Rifat Bin Rashid, Donglin Gao +5
- **PDF**: https://ieeexplore.ieee.org/document/11317599
- **Abstract**: With increasing demand for spectrum, the 12 GHz band is ideal for future 5G deployments, due to its abundant bandwidth and favorable propagation characteristics. Despite these benefits, aspiring 5G terrestrial networks pose critical interference and coexistence challenges for incumbent, in-band, and susceptible satellite (SAT) Digital Broadcasting Stations (DVB-S2). This paper leverages directional beam control and power adaptation through a spectrum sharing framework, minimizing interference on terrestrial SAT receivers. Opposing traditionally rigid spectrum sharing regulations, our framework implements an efficient and reproducible Joint Q-Learning algorithm through a Software-Defined Radio (SDR) emulation on the COSMOS testbed. Evaluating this model against realistic 5G transmission parameters and ETSI Rural Macro case study, a notable highlight of our method is demonstrated through the DVB-S2 Receiver Packet Error Rate (PER), restoring up to 98% of the DVB-S2 link’s ideal performance through coordinated Radio Resource Management (RRM). Furthermore, our model sustains a maximum of 48% standalone 5G network capacity in the presence of SAT downlink, showcasing acceptable coexistence despite simultaneous band usage.
