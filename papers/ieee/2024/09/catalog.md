# IEEE Xplore — 2024-09


## LDPC-Coded LDM Systems Employing Non-Uniform Injection Level for Combining Broadcast and Multicast/Unicast Services

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:10531810
- **Type**: journal
- **Published**: Sept. 2024
- **Authors**: Hao Ju, Yin Xu, Ruiqi Liu +6
- **PDF**: https://ieeexplore.ieee.org/document/10531810
- **Abstract**: Layered Division Multiplexing (LDM) is a Power-based Non-Orthogonal Multiplexing (P-NOM) technique that has been implemented in the Advanced Television System Committee (ATSC) 3.0 terrestrial TV physical layer to effectively multiplex services with different robustness and data rate requirements. As communication systems quickly evolve, the services to be delivered are becoming more diverse and versatile. Up to now, the LDM system adopted in the terrestrial TV system uses a uniform injection level for the lower-level (or Layer 2) signal injection. This paper investigates the non-uniform injection level LDM (NULDM). The proposed technique can explore the Unequal Error Protection (UEP) property of Low-Density Parity-Check (LDPC) codes and the flexible power allocation nature of the NULDM to improve the system performance and spectrum efficiency. NULDM enables the seamless integration of broadcast/multicast and unicast services in one RF channel, where the unicast signal can assign different resources (power, frequency, and time) based on the UE distance and service requirements. Meanwhile, more power could be allocated to improve the upper layer (or Layer 1) broadcast and datacast services. To make better use of the UEP property of LDPC codes in NULDM, the extended Gaussian mixture approximation (EGMA) method is used to design bit interleaving patterns. Additionally, inspired by the channel order of polar codes, this paper proposes an LDPC sub-block interleaving order (SBIO) scheme that performs similarly to the EGMA interleaving model, while better adapting to the diverse needs of proposed mixed service delivery scenarios for convergence of broadband wireless communications and broadcasting systems.

## On Construction of Low-Density Parity-Check Codes for Ultra-Reliable and Low Latency Communications

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:10507064
- **Type**: journal
- **Published**: Sept. 2024
- **Authors**: Linqi Zou, Hao Yan, Jie Dong +3
- **PDF**: https://ieeexplore.ieee.org/document/10507064
- **Abstract**: Low-density parity-check (LDPC) codes with protograph-based raptor-like (PBRL) structure have been chosen as the data channel coding scheme for the fifth-generation (5G) enhanced mobile broad band (eMBB) services. However, these 5G LDPC codes are not optimized for the scenarios of Ultra Reliable and Low Latency Communications (URLLC) and massive Machine Type Communications (mMTC) in which small transport block sizes are usually used. In this paper, a new method is proposed to construct PBRL LDPC codes for URLLC and mMTC. This method incorporates degree-distribution optimization, base matrix derived from parity-check matrix of quadratic residue codes, masking technique and modified progressive-edge-growth (PEG) algorithm. Simulation results show that the proposed PBRL LDPC codes outperform 5G LDPC short codes in terms of error-correcting performance.

## Improvement of SP Decoding Considering the Influence of Recording Patterns by Neural Network in SMR

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:10534790
- **Type**: journal
- **Published**: Sept. 2024
- **Authors**: Madoka Nishikawa, Yasuaki Nakamura, Yasushi Kanai +1
- **PDF**: https://ieeexplore.ieee.org/document/10534790
- **Abstract**: We study a low-density parity-check (LDPC) encoding and iterative decoding system for a shingled magnetic recording (SMR). In particular, we show the usefulness of applying a neural network in iterative decoding. We previously adopted the neural network to evaluate the log-likelihood ratio (LLR) related to row operations on the parity check matrix for the decoding target bit and improved the sum-product (SP) decoding. In this study, we propose to update the LLR considering the influence of noise depending on the recording pattern by providing the LLRs for the decoding target and its adjacent bits to the neural network in SP decoding. In addition, we explore the parameters to update the LLRs by applying the genetic algorithm (GA) to achieve more effective iterative decoding.

## High-Throughput and Hardware-Efficient ASIC-Chip Fabrication of Reconfigurable LDPC/Polar Decoder for mMTC and URLLC 5G-NR Applications

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:10607975
- **Type**: journal
- **Published**: Sept. 2024
- **Authors**: Anuj Verma, Rahul Shrestha
- **PDF**: https://ieeexplore.ieee.org/document/10607975
- **Abstract**: This manuscript proposes hardware-efficient and high-throughput reconfigurable architecture of the channel decoder for unified decoding of LDPC or polar code. It has been designed based on the new dataflow technique for reconfigurable decoding that incurs lesser hardware resources in the decoder design. In addition, this work presents memory-organized architecture that exploits the shared-memory hardware and also excludes various conventional sub modules. Furthermore, this reconfigurable LDPC/polar decoder has been ASIC fabricated in UMC 110 nm-CMOS technology node, occupying an area of 1.96 mm2. It supports multiple code-rates and code-lengths that are compliant to mMTC and URLLC applications of 5G-NR wireless communication standard. At the supply voltage of 1.2 V, the proposed decoder-chip operates at the measured clock frequency of 72.7 MHz and delivers a data throughput of 3.35 Gbps that is  $4{\times }$  higher than the state-of-the-art implementation. It also consumes 15.8% lesser area and achieves  $2.5{\times }$  better hardware-efficiency in comparison to the contemporary works.

## Trainable Joint Channel Estimation, Detection, and Decoding for MIMO URLLC Systems

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:10506472
- **Type**: journal
- **Published**: Sept. 2024
- **Authors**: Yi Sun, Hong Shen, Bingqing Li +4
- **PDF**: https://ieeexplore.ieee.org/document/10506472
- **Abstract**: The receiver design for multi-input multi-output (MIMO) ultra-reliable and low-latency communication (URLLC) systems can be a tough task due to the use of short channel codes and few pilot symbols. Consequently, error propagation can occur in traditional turbo receivers, leading to performance degradation. Moreover, the processing delay induced by information exchange between different modules may also be undesirable for URLLC. To address the issues, we advocate to perform joint channel estimation, detection, and decoding (JCDD) for MIMO URLLC systems encoded by short low-density parity-check (LDPC) codes. Specifically, we develop two novel JCDD problem formulations based on the maximum a posteriori (MAP) criterion for Gaussian MIMO channels and sparse mmWave MIMO channels, respectively, which integrate the pilots, the bit-to-symbol mapping, the LDPC code constraints, as well as the channel statistical information. Both the challenging large-scale non-convex problems are then solved based on the alternating direction method of multipliers (ADMM) algorithms, where closed-form solutions are achieved in each ADMM iteration. Furthermore, two JCDD neural networks, called JCDDNet-G and JCDDNet-S, are built by unfolding the derived ADMM algorithms and introducing trainable parameters. It is interesting to find via simulations that the proposed trainable JCDD receivers can outperform the turbo receivers with affordable computational complexities.

## CDDM: Channel Denoising Diffusion Models for Wireless Semantic Communications

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:10480348
- **Type**: journal
- **Published**: Sept. 2024
- **Authors**: Tong Wu, Zhiyong Chen, Dazhi He +4
- **PDF**: https://ieeexplore.ieee.org/document/10480348
- **Abstract**: Diffusion models (DM) can gradually learn to remove noise, which have been widely used in artificial intelligence generated content (AIGC) in recent years. The property of DM for eliminating noise leads us to wonder whether DM can be applied to wireless communications to help the receiver mitigate the channel noise. To address this, we propose channel denoising diffusion models (CDDM) for semantic communications over wireless channels in this paper. CDDM can be applied as a new physical layer module after the channel equalization to learn the distribution of the channel input signal, and then utilizes this learned knowledge to remove the channel noise. We derive corresponding training and sampling algorithms of CDDM according to the forward diffusion process specially designed to adapt the channel models. We also theoretically prove that the well-trained CDDM can effectively reduce the conditional entropy of the received signal under small sampling steps. Moreover, we apply CDDM to a semantic communications system based on joint source-channel coding (JSCC) for image transmission and design a three-stage training algorithm for combining them. Extensive experimental results demonstrate that CDDM can further reduce the mean square error (MSE) after minimum mean square error (MMSE) equalizer, and the joint CDDM and JSCC system achieves better performance than the JSCC system, the traditional JPEG2000 with low-density parity-check (LDPC) code approach and other benchmarks in diverse scenarios.

## Modulation and Coding for NOMA and RSMA

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:10720669
- **Type**: journal
- **Published**: Sept. 2024
- **Authors**: Hamid Jafarkhani, Hossein Maleki, Mojtaba Vaezi
- **PDF**: https://ieeexplore.ieee.org/document/10720669
- **Abstract**: The next-generation multiple access (NGMA) serves as an umbrella term encompassing transmission schemes distinct from conventional orthogonal methods. As a prominent candidate of NGMA, nonorthogonal multiple access (NOMA) emerges as a promising solution, enhancing connectivity by allowing multiple users to concurrently share time, frequency, and space. However, NOMA faces challenges in practical implementation, particularly in canceling interuser interference (IUI). In this article, first, we discuss the principles behind NOMA and review the conventional NOMA methods and results. Then, to address the above challenges, we present asynchronous transmission and interference-aware modulation techniques, leading to decoding free from successive interference cancellation (SIC). The goal is to design constellations that dynamically adapt to interference, minimizing bit error rates (BERs) and enhancing user throughput in the presence of IUI, intercarrier interference, and intercell interference (ICI). The traditional linkage between minimizing BER and increasing spectral efficiency is addressed, with the exploration of deep autoencoders (AEs) for end-to-end (E2E) communication as a new concept with significant potential for improving BERs. Interference-aware modulation techniques can revolutionize constellation design and communication over nonorthogonal channels. rate-splitting multiple access (RSMA) is another promising interference management technique in multiuser systems. Beyond addressing existing challenges and misconceptions in finite-alphabet NOMA, this article offers fresh insights into the field and provides an overview of code-domain NOMA (C-NOMA) schemes, trellis-coded NOMA (TC-NOMA), and RSMA as other potential candidates for NGMA. Additionally, we discuss the evolution of channel coding toward low-latency communication and examine the modulation and coding schemes (MCSs) in fifth-generation (5G) cellular networks. Finally, we examine future research avenues and challenges, highlighting the importance of addressing them for the practical realization of NOMA from a theoretical concept to a functional technology.

## Performance Analysis of OTSM Under Hardware Impairments and Imperfect CSI

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:10495192
- **Type**: journal
- **Published**: Sept. 2024
- **Authors**: Abed Doosti-Aref, Christos Masouros, Xu Zhu +3
- **PDF**: https://ieeexplore.ieee.org/document/10495192
- **Abstract**: Orthogonal time sequency multiplexing (OTSM) has been recently proposed as a single-carrier waveform offering similar bit error rate to orthogonal time frequency space (OTFS) and outperforms orthogonal frequency division multiplexing (OFDM) in doubly-spread channels (DSCs); however, with a much lower complexity making it a potential candidate for 6G wireless networks. In this paper, the performance of OTSM is explored by considering the joint effects of multiple hardware impairments (HWIs) such as in-phase and quadrature imbalance (IQI), direct current offset (DCO), phase noise, power amplifier non-linearity, carrier frequency offset, and synchronization timing offset for the first time in the area. First, the discrete-time baseband signal model is obtained in vector form under all mentioned HWIs. Second, the system input-output relations are derived in time, delay-time, and delay-sequency (DS) domains in which the parameters of all mentioned HWIs are incorporated. Third, analytical expressions are derived for the pairwise and average bit error probability under imperfect channel state information (CSI) as a function of the parameters of all mentioned HWIs. Analytical results demonstrate that under all mentioned HWIs, noise stays additive white Gaussian, effective channel matrix is sparse, DCO appears as a DC signal at the receiver interfering with only the zero sequency, and IQI redounds to self-conjugated sequency interference in the DS domain. Simulation results reveal the fact that by considering the joint effects of all mentioned HWIs and imperfect CSI not only OTSM outperforms OFDM by 29% in terms of energy of bit per noise but it performs same as OTFS in high mobility DSCs.

## A Threshold-Based Binary Message Passing Decoder With Memory for Product Codes

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:10485466
- **Type**: journal
- **Published**: Sept. 2024
- **Authors**: Xinwei Zhao, Shancheng Zhao, Qingyong Deng +2
- **PDF**: https://ieeexplore.ieee.org/document/10485466
- **Abstract**: Product codes (PCs) are typically decoded using iterative bounded distance decoding (iBDD) to ensure a low decoding complexity. To obtain further performance gain, a soft-aided decoding algorithm, termed the iBDD with scaled reliability (iBDD-SR), was proposed for PCs. In this paper, we propose an enhanced iBDD-SR by introducing threshold and memory when passing messages between the component decoders. The resulting algorithm is referred to as the threshold-based binary message passing (TB-BMP) with memory. In the proposed decoding algorithm, the soft reliability of the BDD output at the current half-iteration is a weighted sum of the BDD output, the channel reliability, and the content of the memory unit, where the content of the memory unit at the current half-iteration is related to the selected threshold and the BDD output at last half-iteration. Due to the existence of memory, the Bayesian network is used to model the decoding process of the TB-BMP. Based on the Bayesian network, we derive the density evolution (DE) equations for the TB-BMP under the constraint of extrinsic message passing (EMP). The analytical results of the DE analysis can be used to guide the selection of the parameters of the TB-BMP decoder. Extensive simulation results show that the TB-BMP decoder outperforms the iBDD-SR over the binary-input additive white Gaussian noise (Bi-AWGN) channels. In particular, for a PC based on a two-error-correcting extended Bose-Chaudhuri-Hocquenghem (BCH) code of length 256, the TB-BMP decoder performs about 0.28 dB better than the iBDD-SR at a bit error rate (BER) of 10−7.

## Bridging Hamming Distance Spectrum With Coset Cardinality Spectrum for Overlapped Arithmetic Codes

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:10578043
- **Type**: journal
- **Published**: Sept. 2024
- **Authors**: Yong Fang
- **PDF**: https://ieeexplore.ieee.org/document/10578043
- **Abstract**: Distributed Source Coding (DSC), a scheme that encodes multiple correlated sources separately while decoding their bitstreams jointly, is an important branch of network information theory. Due to the advantages of shifting complexity burden from the encoder to the decoder and canceling the flow of data across terminals, DSC has potential applications in many scenarios, e.g., wireless sensor network, distributed genome data compression, etc. There are two forms (lossless and lossy) of DSC. Overlapped arithmetic codes, featured by overlapped intervals, are a variant of arithmetic codes that can implement distributed lossless compression, or the so-called Slepian-Wolf coding. For uniform binary sources, an overlapped arithmetic code is essentially a nonlinear many-to-one mapping that partitions source space into unequal-sized cosets. To analyze overlapped arithmetic codes, two theoretical tools have been proposed, i.e., Coset Cardinality Spectrum (CCS) and Hamming Distance Spectrum (HDS). The former describes how source space is partitioned into cosets (equally or unequally), and the latter describes how codewords are structured within each coset (densely or sparsely). However, until now, these two tools are almost parallel to each other, and it seems that there is no intersection between them. The main contribution of this paper is tightly bridging HDS with CCS. Specifically, HDS can be quickly and accurately calculated with CCS in some cases. In addition, the paper also proves the necessary and sufficient condition for the convergence of HDS and reveals the close relation between divergent HDS and polynomial division. All theoretical analyses are verified by experimental results.

## Random Pilot Activation and Interpolated Channel Estimation for Physical-Layer Secret Key Generation in Correlated Eavesdropping Channel

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:10495199
- **Type**: journal
- **Published**: Sept. 2024
- **Authors**: Shun Kojima, Shinya Sugiura
- **PDF**: https://ieeexplore.ieee.org/document/10495199
- **Abstract**: In this paper, we propose a novel physical-layer secret key generation (SKG) scheme, which is based on reduced random pilot selection at a legitimate transmitter and channel interpolation at a legitimate receiver. As a result, the proposed scheme is capable of reducing pilot overhead and increasing secret key capacity (SKC) while suppressing information leakage to an eavesdropper in a correlated eavesdropping channel. More specifically, a subset of full pilot sequence is activated based on the legitimate channels at the legitimate transmitter, and the full channel coefficients are estimated from the received pilot symbol subset at the legitimate receiver with the aid of our channel interpolation. Additionally, despite the non-reciprocal channel due to the presence of a Doppler shift and an additive noise, our scheme achieves high SKG reliability in comparison to that without our reduced pilot selection or channel interpolation. We also derive the theoretical SKC for the proposed scheme. Our simulation results demonstrate that the proposed SKG scheme exhibits a higher performance in terms of both the SKC and key disagreement ratio.

## Mutual Information Density of Massive MIMO Systems Over Rayleigh-Product Channels

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:10495334
- **Type**: journal
- **Published**: Sept. 2024
- **Authors**: Xin Zhang, Shenghui Song
- **PDF**: https://ieeexplore.ieee.org/document/10495334
- **Abstract**: The Rayleigh-product channel model is utilized to characterize the rank deficiency caused by keyhole effects. However, the finite blocklength analysis for Rayleigh-product channels is not available in the literature. In this paper, we will characterize the mutual information density (MID) and perform the FBL analysis to reveal the impact of rank-deficiency in Rayleigh-product channels. To this end, we first set up a central limit theorem for the MID over Rayleigh-product MIMO channels in the asymptotic regime where the number of scatterers, number of antennas, and blocklength go to infinity at the same pace. Then, we utilize the CLT to obtain the upper and lower bounds for the packet error probability, whose approximations in the high and low signal to noise ratio regimes are then derived to illustrate the impact of rank-deficiency. One interesting observation is that rank-deficiency degrades the performance of MIMO systems with FBL and the fundamental limits of Rayleigh-product channels degenerate to those of the Rayleigh case when the number of scatterers approaches infinity.

## A Proposal to Use ROUTE/DASH in the Advanced ISDB-T

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:10546480
- **Type**: journal
- **Published**: Sept. 2024
- **Authors**: George Henrique Maranhão Garcia de Oliveira, Gustavo de Melo Valeira, Cristiano Akamine
- **PDF**: https://ieeexplore.ieee.org/document/10546480
- **Abstract**: In Brazil, the Television (TV) 3.0 project has been underway since 2020 and is currently in its third phase. The aim of this project is to study, test and validate state-of-the-art technologies in order to define the techniques that will make up the next-generation of Brazilian Digital Terrestrial Television Broadcasting (DTTB) System. All the technologies involved in this system must be compatible with the transportation method defined in Phase 02 of the project: the Real-Time Object Delivery over Unidirectional Transport (ROUTE)/Dynamic Adaptive Streaming over HTTP (DASH) method from the Advanced Television Systems Committee (ATSC) 3.0 standard. Therefore, this paper proposes the use of the ROUTE/DASH transportation method in the Advanced Integrated Services Digital Broadcasting Terrestrial (ISDB-T) system, presenting the theory involved and the results obtained in the first transmission carried out involving the two aforementioned technologies.

## Exploiting Device Heterogeneity in Grant-Free Random Access: A Data-Driven Approach

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:10520829
- **Type**: journal
- **Published**: Sept. 2024
- **Authors**: Alix Jeannerot, Malcolm Egan, Jean-Marie Gorce
- **PDF**: https://ieeexplore.ieee.org/document/10520829
- **Abstract**: Grant-free random access (GFRA) is now a popular protocol for large-scale wireless multiple access systems in order to reduce control signaling. Resource allocation in GFRA can be viewed as a form of frame slotted ALOHA, where a ubiquitous design assumption is device homogeneity. In particular, the probability that a device seeks to transmit data is common to all devices. Recently, there has been an interest in designing frame slotted ALOHA algorithms for networks with heterogeneous activity probabilities. These works have established that the throughput can be significantly improved over the standard uniform allocation. However, the algorithms for optimizing the probability a device accesses each slot require perfect knowledge of the active devices within each frame. In practice, this assumption is limiting as device identification algorithms in GFRA rarely provide activity estimates with zero errors. In this paper, we develop a new algorithm based on stochastic gradient descent for optimizing slot allocation probabilities in the presence of activity estimation errors. Our algorithm exploits importance weighted bias mitigation for stochastic gradient estimates, which is shown to provably converge to a stationary point of the throughput optimization problem. In moderate size systems, our simulations show that the performance of our algorithm depends on the type of error distribution. We study symmetric bit flipping, asymmetric bit flipping and errors resulting from a generalized approximate message passing (GAMP) algorithm. In these scenarios, we observe gains up to 40%, 66%, and 19%, respectively.

## Learned Soft MIMO Detection via Search Path Selection and Symbol Distribution Fitting

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:10559435
- **Type**: journal
- **Published**: Sept. 2024
- **Authors**: Mingyang Yue, Hao Wang, Jing Qian +2
- **PDF**: https://ieeexplore.ieee.org/document/10559435
- **Abstract**: We propose a learning-aided soft multi-input multi-output (MIMO) detection method, consisting of a search path selection module and a symbol distribution fitting module. The search path selection module uses a neural network to generate a set of candidate paths. Different from traditional tree search algorithms, we utilize the soft estimates output by a neural network to calculate and cancel the symbol interference. The symbol distribution fitting module aims to solve the missing counter-hypotheses problem, where an additional neural network is employed to estimate the marginal posterior probability distribution of each symbol. Numerical results demonstrate the effectiveness of the proposed method especially when the allowed computational complexity is highly limited.

## Impulsive Noise Estimator With Minimization Methods (INEMM) on Software

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:10480616
- **Type**: journal
- **Published**: Sept. 2024
- **Authors**: Lucas A. Rabioglio, M. C. Cebedio, L. Arnone +2
- **PDF**: https://ieeexplore.ieee.org/document/10480616
- **Abstract**: This letter introduces the design of an estimator for parameters of Middleton Class A noise using its canonical formula and classical numerical methods. The main focus is to acquire parameters to characterize communication channels in intelligent systems or those based on cognitive paradigms. A comprehensive analysis of the first-order characteristics of the Middleton Class A noise model is conducted to establish the foundational understanding necessary for developing the presented estimator model, named impulsive noise estimator with minimization methods (INEMM). Subsequently, the method is introduced, substantiated, and compared to various established estimators concerning precision and complexity. Results show a distinct advantage in terms of overall performance.

## Pilot-Free Slotted ALOHA for Massive Access

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:10461062
- **Type**: journal
- **Published**: Sept. 2024
- **Authors**: Xu Li, Lou Zhao, Tao Yang
- **PDF**: https://ieeexplore.ieee.org/document/10461062
- **Abstract**: This correspondence proposes a pilot-free slotted ALOHA scheme for a massive random access system. The user equipment (UE) utilizes coded differential modulation and transmits with the repetition-based slotted ALOHA (RSA) protocol. The base station employs non-coherent detection and cancellation for recovering all UEs' messages. We develop a belief propagation (BP) based non-coherent detection and estimation, which offers improved load-throughput performance. It is demonstrated that the pilot-free slotted ALOHA scheme can achieve almost the identical throughput of the conventional pilot-based RSA while relaxing the need for pilot sequences, further avoiding the pilot collision. We also show that the pilot-free slotted ALOHA is applicable to massive access with asynchrony and large Doppler shift.

## Improving QoS of Satellite Broadcasting Against Rain Attenuation by LLR Sharing Method With IP Network Integration at FEC Layer

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:10599863
- **Type**: journal
- **Published**: Sept. 2024
- **Authors**: Yuki Koizumi, Yoichi Suzuki, Masashi Kamei
- **PDF**: https://ieeexplore.ieee.org/document/10599863
- **Abstract**: We are developing a diverse reception system (DRS) to compensate for rain attenuation in satellite broadcasting that utilizes path diversity between a satellite channel and a best-effort (BE)-IP network for end users. The proposed DRS recovers signals lost on a satellite channel due to significant rain attenuation by supplementing them via a BE-IP network. The unique point of the DRS is that it uses a common forward error correction (FEC) for both channels by applying a FEC for satellite broadcasting to the error correction in BE-IP network. This allows both channels to be integrated at the FEC layer and improves the quality of service (QoS) in the satellite broadcasting thanks to sharing the decoding information between the two. In this paper, we propose an advanced error-correction technique that achieves a high QoS in the DRS by sharing each log-likelihood ratio (LLR) utilized for the FEC decoding of bits received over both channels. This technique, which we call the LLR sharing method, enables successful error correction even when neither a satellite channel nor a BE-IP network can individually achieve error-free transmission due to significant rain attenuation or burst packet loss, respectively. Computer simulation results confirm that the LLR sharing method can improve the required C/N in the satellite broadcasting. In addition, we discuss how to suppress the load of the BE-IP network and integrate both channels efficiently.

## Guest Editorial Special Issue on Intelligent Multicast/Broadcast Services Over 5G/6G

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:10680477
- **Type**: journal
- **Published**: Sept. 2024
- **Authors**: Bo Rong, Eneko Iradier, Jordi Joan Gimenez +8
- **PDF**: https://ieeexplore.ieee.org/document/10680477
- **Abstract**: N/A

## A Relaxation Oscillator-Based Probabilistic Combinatorial Optimization Engine for Soft Decoding of LDPC Codes

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:10719549
- **Type**: conference
- **Published**: 9-12 Sept.
- **Authors**: Evangelos Dikopoulos, Luke Wormald, Ying-Tuan Hsu +4
- **PDF**: https://ieeexplore.ieee.org/document/10719549
- **Abstract**: Drawing insights from quantum computing, oscillator-based computing leverages continuous-time operation and massive parallelism to accelerate challenging computational tasks. This work advances the field to demonstrate a Combinatorial Optimization Problem (COP) engine for efficient, robust, one-shot oscillator-based soft decoding of LDPC codes for the first time. We present a 28 nm CMOS prototype that achieves a Frame, Bit Error Rate (FER, BER) of $1.38 \times 10^{-5}, 1.25 \times 10^{-6}$ respectively at 7 dB SNR and an energy efficiency of $5.26 \mathrm{pJ} / \mathrm{bit}$, which surpasses the normalized efficiencies of recent state-of-the-art decoders [1][2][3] by 11x, 3 x, 1.5 x respectively. Tested with more than 100 million frame decodings, the prototype demonstrates consistent performance across a range of SNRs, supply voltages, and temperatures.

## Neural Network-Based Self-Interference Cancellation for Frequency Division Duplex

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:10925912
- **Type**: conference
- **Published**: 9-11 Sept.
- **Authors**: Mike Beckworth, Ephraim Fuchs, Moritz Benedikt Fischer +1
- **PDF**: https://ieeexplore.ieee.org/document/10925912
- **Abstract**: In frequency division duplex systems with simultaneous transmission and reception, receivers suffer from outof- band emissions by the wireless transmitter leaking into the receive band. This so-called self-interference can be cancelled by means of estimating the interfering signal from the known transmit signal and subtracting it from the received signal. Conventional cancellation approaches rely on a mathematical model of the self-interference generation. However, these cannot capture effects beyond their model assumptions. With neural networkbased cancellation, present interference-generating effects are captured during data-driven training. In this work, we combine such a cancellation method with a neural network-based receiver for the demodulation of the signal-of-interest. Simulation results with 5G NR-conform waveforms show that this approach is both well-performing and adaptive to many self-interference and radio channel scenarios. Our approach is able to cancel selfinterference that has undergone power amplifier nonlinearity, IQ imbalance, and a frequency-selective channel down to a signalto- interference ratio of 0.0 dB.

## Coding Solutions for Robust Performance in Wireless Systems

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:10774754
- **Type**: conference
- **Published**: 6-8 Sept. 
- **Authors**: Vaishali Singh, Rajesh Gupta, K S Srinivasa Rao
- **PDF**: https://ieeexplore.ieee.org/document/10774754
- **Abstract**: Wi-Fi structures require reliable coding solutions to ensure robust overall performance. Latest advances in wireless technologies have accelerated the want for reliable coding strategies to catch up on signal losses because of shadowing, fading, and imperfect channel situations. Traditional coding techniques, together with forward mistakes correction (FEC) and variety coding, conflict to hold strong performance underneath challenging conditions. New coding strategies are needed to ensure a reliable Wi-Fi communiqué in difficult propagation environments. Recent research in coding answers for robust wireless systems has explored a selection of methods, such as faster codes, Low-Density Parity-test (LDPC) codes, and area-time coding. LDPC codes offer extended code lengths, which boosts coding benefits and features quite low computational complexity. Area-time codes are a block coding method that improves blunder resilience by utilizing a couple of antennas and transmitting the identical sign in more than one direction simultaneously. These coding answers were implemented to provide improved overall performance in diverse Wi-Fi systems, which include cell, WLAN, and satellite TV for PC communiqué networks. Particularly, turbo codes, LDPC codes, and area-time codes have been used effectively in WLAN networks to reduce channel mistakes and growth records prices, in addition to in mobile networks to enhance spectral efficiency and offer better throughput.

## On the Comparative Study of Recent Information Set Decoding (ISD) Attacks for QC-LDPC Code-Based McEliece Cryptosystem

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:10727868
- **Type**: conference
- **Published**: 5-6 Sept. 
- **Authors**: Sourabh Biswas, Indivar Gupta, Debasish Bera
- **PDF**: https://ieeexplore.ieee.org/document/10727868
- **Abstract**: Code-based cryptography is one of the main candidates in quantum-resistant cryptographic techniques. LEDAcrypt is a code-based cryptographic scheme submitted in the 2nd round to the National Institute of Standards and Technology (NIST) postquantum cryptography contest. Information set decoding (ISD) attacks, first introduced by Eugene Prange, are well-known non-structural attacks used effectively for code-based cryptography. After several improvements of the basic ISD algorithm, Stern's ISD $(ISD_{Stern})$ and two recent improvements by Finiasz and Sendrier's ISD $(ISD_{FS})$ and May, Meurer and Thomae's ISD $(ISD_{MMT})$ draw significant attention. This paper demonstrates a detailed security analysis of key-recovery attacks using ISD and a comparative study of three ISD algorithms concerning the QC-LDPC-based McEliece cryptosystem variant of LEDAcrypt. Additionally, we have updated the LEDAcrypt parameter table from the original submission, incorporating two new parameters based on the ISD analysis. Simulation results show that the computational cost of $ISD_{MMT}$ is lower than the $ISD_{Stern}$ and $ISD_{FS}$ when applied for LEDAcrypt.

## Optimized Rate-Adaptive Error Correction Through Puncturing and Shortening of Simplex Codes

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:10736808
- **Type**: conference
- **Published**: 25-27 Sept
- **Authors**: Massimo Battaglioni, Gianmarco Greganti, Giovanni Cancellieri
- **PDF**: https://ieeexplore.ieee.org/document/10736808
- **Abstract**: This paper presents a strategy for obtaining efficient rate-adaptive error correction by puncturing and shortening simplex codes. We derive a family of punctured cyclic codes from a parent cyclic simplex code. Using a polynomial approach based on the parity-check polynomial $h(x)$, we analyze key properties of these codes. We introduce a procedure to optimize code design with predefined values of the code rate $R$ and length $n$ through optimal multiple code shortening, aiming to increase the minimum distance by eliminating residual minimum distance codewords after puncturing operations. The effectiveness of this approach is demonstrated through practical examples, with BER vs. SNR curves obtained through numerical simulations.

## Quantum Margulis Codes

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:10735283
- **Type**: conference
- **Published**: 24-27 Sept
- **Authors**: Michele Pacenti, Bane Vasić
- **PDF**: https://ieeexplore.ieee.org/document/10735283
- **Abstract**: Recently, Lin and Pryadko [1] presented the quan-tum two-block group algebra codes, a generalization of bicycle codes obtained from Cayley graphs of non-Abelian groups. We notice that their construction is naturally suitable to obtain a quantum equivalent of the well-known classical Margulis code. In this paper, we first present an alternative description of the two-block group algebra codes using the left-right Cayley complex; then, we show how to modify the construction of Margulis to get a two-block group algebra code. Finally, we construct several quantum Margulis codes and evaluate their performance with numerical simulations.

## Erasure Decoding for Quantum LDPC Codes via Belief Propagation with Guided Decimation

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:10735275
- **Type**: conference
- **Published**: 24-27 Sept
- **Authors**: Mert Gökduman, Hanwen Yao, Henry D. Pfister
- **PDF**: https://ieeexplore.ieee.org/document/10735275
- **Abstract**: Quantum low-density parity-check (LDPC) codes are a promising family of quantum error-correcting codes for fault tolerant quantum computing with low overhead. Decoding quantum LDPC codes on quantum erasure channels has received more attention recently due to advances in erasure conversion for various types of qubits including neutral atoms, trapped ions, and superconducting qubits. Belief propagation with guided decimation (BPGD) decoding of quantum LDPC codes has demonstrated good performance in bit-flip and depolarizing noise. In this work, we apply BPGD decoding to quantum erasure channels. Using a natural modification, we show that BPGD offers competitive performance on quantum erasure channels for multiple families of quantum LDPC codes. Furthermore, we show that the performance of BPGD decoding on erasure channels can sometimes be improved significantly by either adding damping or adjusting the initial channel log-likelihood ratio for bits that are not erased. More generally, our results demonstrate BPGD is an effective general-purpose solution for erasure decoding across the quantum LDPC landscape.

## Graph Codes for Dual-Parameter Barrier Channels

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:10735324
- **Type**: conference
- **Published**: 24-27 Sept
- **Authors**: Yuval Ben-Hur, Saar Stern, Yoav Cohen +1
- **PDF**: https://ieeexplore.ieee.org/document/10735324
- **Abstract**: A ternary barrier channel is a non-symmetric error model defined previously to address emerging applications. Conveniently, it admits a code-construction method comprising two binary constituent codes. In this paper we propose a decoding algorithm that decodes the two constituent codes jointly by message passing on a graph representing the two codes' parity-check constraints. The messages exchanged by the algorithm are likelihoods calculated from incoming messages, and they are derived in the paper based on the exact dependence between the binary values of the two codewords. Simulation results demonstrate that the proposed decoder has superior error-rate performance compared to prior decoding approaches.

## An Efficient Approach on Image Encryption Steganography based on 2D SWT with Chaotic Techniques

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:10917943
- **Type**: conference
- **Published**: 24-25 Sept
- **Authors**: N. Naveen Kumar, R. Viswanathan, P. Seshu Kumar
- **PDF**: https://ieeexplore.ieee.org/document/10917943
- **Abstract**: Image encryption and steganography are crucial techniques for securing digital imagery, ensuring confidentiality, integrity, and authenticity. This paper proposes a novel and efficient approach that integrates 2D Stationary Wavelet Transform (SWT) with chaotic techniques for image encryption steganography. The 2D SWT provides a multi-resolution representation of images, enabling effective analysis and processing in both frequency and spatial domains. Chaotic techniques introduce randomness and complexity into the encryption process, enhancing security and resistance against attacks. In this approach, the image encryption process involves employing chaotic maps to generate encryption keys or masks, which are then used to modify the coefficients obtained from the SWT. The secret information is embedded into the image using the modified coefficients, ensuring its invisibility and robustness against various attacks. The proposed method offers enhanced security, efficiency, and flexibility for secure transmission, storage, and manipulation of digital images. Experimental results demonstrate the effectiveness of the proposed approach in terms of security, robustness, and computational efficiency, making it suitable for a wide range of image security applications.

## Development of an Adaptive Protocol for Packet Data Transmission

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:10762925
- **Type**: conference
- **Published**: 23-27 Sept
- **Authors**: Leonid M. Chervyakov, Maxim A. Kocharov, Maxim S. Mikhailov
- **PDF**: https://ieeexplore.ieee.org/document/10762925
- **Abstract**: The development of telecommunication networks is determined both by global trends and the specific situation in which this industry has been for a long time. When using such networks, it is important to maintain a sufficient level of data transmission quality. Therefore, the purpose of this work is to create a technique that allows making adaptive tuning of protocol parameters at the link layer. This technique should also include a channel testing mechanism. The analysis showed that the current existing codes couldn't cope with a large number of errors, so it is proposed to create a new method of data encapsulation, which provides a lower value of loss. The application of the method proposed in our work for adjusting protocol parameters at the link level showed that the quality of communication is maintained significantly longer, even with a high degree of loss (50%), compared to analogues.

## Post-FEC BER Assessment with Optimized Decoding Latency for 400 Gbps Transmission Over a 1.8km FSO Field Trial

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:10926067
- **Type**: conference
- **Published**: 22-26 Sept
- **Authors**: Manuel M. Freitas, Marco A. Fernandes, Bruno T. Brandao +8
- **PDF**: https://ieeexplore.ieee.org/document/10926067
- **Abstract**: We experimentally assess the post-FEC BER performance of 400 Gbps FSO transmission over a 1.8 km field-trial, minimizing the LDPC decoding latency to achieve error-free communication with/without optical pre-amplification. Pre-amplification is shown to provide reliability gains exceeding 70%, typically necessitating 3× fewer decoding iterations.

## Comparison of Methods for Distance-Adaptive Continuous-Variable Quantum Key Distribution

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:10926409
- **Type**: conference
- **Published**: 22-26 Sept
- **Authors**: Jonas Berl, Erdem Eray Cil, Utku Akin +2
- **PDF**: https://ieeexplore.ieee.org/document/10926409
- **Abstract**: We demonstrate that CV-QKD with a single error-correcting code is severely constrained in distance and compare three alternative strategies for distance-adaptivity. Numerical simulations show that rate-adaptive coding outperforms adding controlled amounts of trusted noise and optimizing the modulation variance.

## Single-Carrier 1.6-Tb/s Transmission with Digital Inverse Multiplexing on 89-GHz Bandwidth Doublers

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:10926361
- **Type**: conference
- **Published**: 22-26 Sept
- **Authors**: Akira Kawai, Masanori Nakamura, Takayuki Kobayashi +6
- **PDF**: https://ieeexplore.ieee.org/document/10926361
- **Abstract**: We generated coherent signals at up to 168 Gbaud based on 32-GHz DACs and 89-GHz InP bandwidth doubler modules supported by a tailored digital pre-distortion scheme (digital inverse multiplexing). We achieved a net bit rate of 1.61 Tb/s at 144 Gbaud after 100-km transmission.

## 339.1 Tb/s OESCLU-band transmission over 100 km SMF

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:10926467
- **Type**: conference
- **Published**: 22-26 Sept
- **Authors**: B. J. Puttnam, R. S. Luis, I. Phillips +20
- **PDF**: https://ieeexplore.ieee.org/document/10926467
- **Abstract**: We investigate wideband signal transmission over 100 km single-mode fiber (SMF) links with transmission of a 36 THz aggregate bandwidth covering OESCLU-bands using 6 doped-fiber amplifier variants with lumped and distributed Raman-amplification for a GMI-estimated data-rate of 339.1 Tb/s and decoded data-rate of 322.8 Tb/s.

## High Gain Incoherently Pumped Discrete Raman Amplifiers for U-band Coherent Transmission Systems

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:10926092
- **Type**: conference
- **Published**: 22-26 Sept
- **Authors**: D. Pratiwi, D. Orsuti, M. Tan +7
- **PDF**: https://ieeexplore.ieee.org/document/10926092
- **Abstract**: We investigate high gain incoherently pumped U-band discrete Raman amplifiers, achieving up to 22.3dB net gain with HNLF and 4.2-5.8dB noise figure, and demonstrate their use in a C+L+U-band coherent transmission system using 516x24.5GBd/s DP-64/256QAM channels with a total GMI data rate of 136.2Tb/s.

## >11-dB SNR and 3-dB Sensitivity Enhancement for Fronthaul with Delta-Sigma Modulation and Equal Length Level Conversion

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:10926125
- **Type**: conference
- **Published**: 22-26 Sept
- **Authors**: Zijun Yan, Yixiao Zhu, Gengming Lin +3
- **PDF**: https://ieeexplore.ieee.org/document/10926125
- **Abstract**: We propose an equal length level conversion scheme to convert delta-sigma modulation (DSM) output from 6-level to 4-level with approximately equivalent entropy. Compared to 4-level DSM systems, our proposed scheme achieves 11.6-dB gain in wireless signal SNR and 3.0-dB enhancement in received optical power sensitivity.

## Demonstration of Joint Blind Clock Recovery in a 1.92 Tbit/s Transmission Over 50 km Randomly-Coupled 4-Core Fiber

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:10926081
- **Type**: conference
- **Published**: 22-26 Sept
- **Authors**: Patrick Matalla, Lennart Schmitz, Jonas Krimmer +3
- **PDF**: https://ieeexplore.ieee.org/document/10926081
- **Abstract**: We present for the first time a digital joint clock recovery in feedforward architecture, that is tolerant to spatial-and-polarization-mode dispersion. We demonstrate clock recovery for a 60-GBd 16-QAM signal over a 50-km randomly-coupled 4-core fiber (RC-4CF).

## Multiband DWDM Transmission Using a Deployed Fibre-Optic Cable

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:10926394
- **Type**: conference
- **Published**: 22-26 Sept
- **Authors**: Daiki Soma, Tomoyuki Kato, Shohei Beppu +9
- **PDF**: https://ieeexplore.ieee.org/document/10926394
- **Abstract**: Increasing capacity per fibre requires extending the optical signal bandwidth in the wavelength and spatial axes. This paper presents O+S+C+L+U band 45 km single-mode fibre transmission and C+L band 2,160 km uncoupled four-core fibre transmission using deployed fibre-optic cables for multi-band DWDM transmission.

## Single-Carrier 224-GBaud 2.3-Tbps Transmission Using 30-GHz DACs and Electro-Optic Bandwidth Quadrupler

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:10926393
- **Type**: conference
- **Published**: 22-26 Sept
- **Authors**: Hiroshi Yamazaki, Munehiko Nagatani, Hitoshi Wakita +9
- **PDF**: https://ieeexplore.ieee.org/document/10926393
- **Abstract**: We demonstrate a transmitter combining electronic and optical intermediate-frequencyinvolved multiplexing techniques. With DACs each generating signals with a bandwidth of only 30 GHz, 224-GBaud PCS-QAM signals could be generated, achieving net bit rates of 2.36 Tbps/lambda back-to-back and 2.32 Tbps/lambda after 80-km SSMF transmission.

## Flexible and Intelligent Latency Management Scheme Using Joint Resource Optimization in PTMP Fronthaul Networks

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:10926570
- **Type**: conference
- **Published**: 22-26 Sept
- **Authors**: Xi Chen, Yixiao Zhu, Yicheng Xu +4
- **PDF**: https://ieeexplore.ieee.org/document/10926570
- **Abstract**: We propose and demonstrate a flexible and intelligent latency management scheme for PTMP fronthaul networks. The latency is controlled by the optimization of power allocation and FEC decoding. The RMSE of latency is reduced by 73.8%. Multi-objective optimization provides Pareto solutions adapted to different needs.

## Record 202.3 Tb/s Transmission over Field-Deployed Fibre using 15.6 THz S+C+L-Bands

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:10926417
- **Type**: conference
- **Published**: 22-26 Sept
- **Authors**: Jiaqian Yang, Eric Sillekens, Benjamin J. Puttnam +8
- **PDF**: https://ieeexplore.ieee.org/document/10926417
- **Abstract**: Ultra-wideband, field-deployed metropolitan fibre transmission is experimentally demonstrated, measuring a record 202.3 Tb/s GMI and 189.5 Tb/s after decoding with 20.9 dBm launch power and lumped amplification only. An experimentally-optimised 5 dB pre-tilt over the 15.6 THz optical bandwidth was applied to overcome ISRS.

## In-Service Transceiver Calibration with Extracting IQ Difference via Offloaded Adaptive Multi-layer Filters

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:10926173
- **Type**: conference
- **Published**: 22-26 Sept
- **Authors**: Masaki Sato, Hidemi Noguchi, Junichiro Matsui +2
- **PDF**: https://ieeexplore.ieee.org/document/10926173
- **Abstract**: We demonstrated in-service transceiver calibration for 128-GBd PM-PCS-64QAM via adaptive multi-layer filters over 120-km SMF. After compensating the Tx/Rx-IQ difference only, Q-penalties of 0.1 dB with 2 ps Tx-IQ skew, 3 ps Rx-IQ-skew, 2 dB IQ peaking error, and 60-GHz Rx-IQ bandwidth imbalance were achieved.

## 126-Tb/s 2-Core Fibre Transmission over 114.6 km × 5 Spans with Ultra-Low-Loss Fibre Bundle Fan-in/Fan-out

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:10926093
- **Type**: conference
- **Published**: 22-26 Sept
- **Authors**: Kosuke Komatsu, Shohei Beppu, Daiki Soma +12
- **PDF**: https://ieeexplore.ieee.org/document/10926093
- **Abstract**: Full C+L-band 2-core fibre transmission is experimentally demonstrated with five spans for a total distance of 573 km. The transmission capacity of 126 Tb/s is achieved with the longest span length for weakly-coupled multi-core fibres, which is enabled by ultra-low-loss fibres and fan-in/fan-out devices.

## 7.75 Gbit/s LiFi Transmitter Using High-Power VCSEL Arrays

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:10926372
- **Type**: conference
- **Published**: 22-26 Sept
- **Authors**: Malte Hinrichs, Giulio Boniello, Dominic Schulz +2
- **PDF**: https://ieeexplore.ieee.org/document/10926372
- **Abstract**: We report on a wide-beam LiFi transmitter using multiple VCSEL arrays with digital drivers. We transmit a 3.75 GBd PAM-3 signal at a gross data rate of 5.625 Gbit/s. Single-driver OOK operation yields 7.75 GBd.

## NONBINARY: A High-Speed Information Reconciliation Algorithm for High Dimensional Quantum Key Distribution

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:10926235
- **Type**: conference
- **Published**: 22-26 Sept
- **Authors**: R. Mueller, J. Riebesehl, D. Bacco +2
- **PDF**: https://ieeexplore.ieee.org/document/10926235
- **Abstract**: The Information Reconciliation phase in Quantum Key Distribution requires specialized error correction methods to achieve high secret key rates. We propose a novel algorithm, NONBINARY, for high-dimensional implementations. NONBINARY is one of the simplest and fastest algorithms so far, reaching speeds up to 750 Mbps

## Study of EEPN effect in 800G QAM16 DSP for coherent plug-gables

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:10926070
- **Type**: conference
- **Published**: 22-26 Sept
- **Authors**: Hai Xu, Charles Chen, Shih-Cheng Wang
- **PDF**: https://ieeexplore.ieee.org/document/10926070
- **Abstract**: We experimentally compare the EEPN-induced penalty to OFEC, LDPC, LDPC with PCS for 800G DP-QAM16. We incorporate a laser phase noise model in an 800G system simulation and show that it achieves a good agreement with measured laser frequency characteristics and measured Q factor distribution.

## First Real-Time Softwarization of Flexible-Rate Coherent DSP Enabling Converged Heterogeneous PON Service

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:10926245
- **Type**: conference
- **Published**: 22-26 Sept
- **Authors**: Sang-Yuep Kim, Takahiro Suzuki, Jun-ichi Kani +1
- **PDF**: https://ieeexplore.ieee.org/document/10926245
- **Abstract**: We demonstrate the first GPU platform to softwarize flexible-rate coherent DSP; it can receive 2-, 4-, 8- and 16-PSK frames by changing the coding description. Receiver sensitivity is measured in real-time for Gbaud-class rate frames, with LDPC thresholds of −50.5, −46.5, −40.5 and −33.5dBm, respectively.

## Design and Implementation of Partially Parallel LDPC Decoder for Low Earth Orbit Micro-Nano Satellites Data Transmission

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:10881440
- **Type**: conference
- **Published**: 22-25 Sept
- **Authors**: Chong Huang, Zhi Hou, Peng Li +1
- **PDF**: https://ieeexplore.ieee.org/document/10881440
- **Abstract**: This paper proposes a LDPC decoder for Low Orbit Micro-Nano Satellites Date Transmision. By analyzing the H-matrix characteristic, each cyclic sub matrix of the H-matrix is mapped to a Ramdom Access Memory(RAM). The address and data lines of the RAM are fully utilized to realize that RAM can be represented as both an H -matrix and an information storage matrix. The results on FPGA platform show that when the Eb/N0 is 4dB, the throughput of the decoder reaches 145Mbps, which improves the margin of data transmission links and meets the demand for data transmission. The decoder has completed in orbit verification on the experiment verification satellites.

## Semantic Communication for Cooperative Perception with HARQ

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:10734724
- **Type**: conference
- **Published**: 22-25 Sept
- **Authors**: Yucheng Sheng, Hao Ye, Le Liang +1
- **PDF**: https://ieeexplore.ieee.org/document/10734724
- **Abstract**: Cooperative perception, offering a wider field of view than standalone perception, is becoming increasingly crucial in autonomous driving. This advanced perception is enabled through vehicle-to-vehicle (V2V) communication, allowing connected automated vehicles (CAVs) to exchange sensor data, such as LiDAR point clouds, thereby enhancing the collective understanding of the environment. In this paper, we leverage an importance map to distill critical semantic information, introducing a cooperative perception semantic communication framework that employs intermediate fusion. Furthermore, recognizing the necessity for reliable transmission, especially in low SNR scenarios, we introduce a novel semantic error detection method that is integrated within our semantic communication framework in the spirit of hybrid automatic repeated request (HARQ). Simulation results show that our model surpasses traditional separate source-channel coding methods in perception performance. Additionally, in terms of throughput, our proposed HARQ schemes demonstrate superior efficiency compared to conventional coding approaches.

## Constellation Design with Metaheuristic Deep Learning for Future Wireless Networks

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:10734778
- **Type**: conference
- **Published**: 22-25 Sept
- **Authors**: Yidi Zhang, Ming Jiang, Chunming Zhao
- **PDF**: https://ieeexplore.ieee.org/document/10734778
- **Abstract**: Geometric constellation shaping is a promising technique for improving the transmission capacity of future communication systems. In this paper, we propose a hybrid automatic repeat request scheme with chase combining (CC-HARQ) that utilizes a metaheuristic learning-based neural network for geometric shaping. Based on a fixed mapper for the first transmission, we employ an autoencoder to train the geometric symmetry constellation used for retransmission, with metaheuristic initialization and data preprocessing. Simulation results show that the proposed CC-HARQ scheme significantly outperforms the conventional square constellation rearrangement scheme in terms of bit error rate performance and is comparable to the incremental redundancy HARQ scheme specified by the 5G standard.

## High-Speed Design Approaches for CCSDS LDPC Encoder Systems

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:10775118
- **Type**: conference
- **Published**: 21-22 Sept
- **Authors**: Jeeshma T.N, Pargunarajan K
- **PDF**: https://ieeexplore.ieee.org/document/10775118
- **Abstract**: In this paper, the implementation of a QC-LDPC encoder using AR4JA photograph LDPC is presented. This design utilizes a block-cyclic generator matrix from a quasi-cyclic parity check matrix to reduce encoder complexity. Additionally, an increase in speed of 22.87 % and a reduction in resource utilization of 14.28 % is also achieved through this method. The synthesis report of the utilization summary and delay from Vivado is shown and compared with an efficient QC- LDPC encoder using the Richardson Urbanke algorithm. FPGA implementation is also performed for the proposed design.

## Parallel optimization design of LDPC decoder with variable normalization factor

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:10762031
- **Type**: conference
- **Published**: 20-22 Sept
- **Authors**: Kaidi Liu, Ziwei Guo
- **PDF**: https://ieeexplore.ieee.org/document/10762031
- **Abstract**: In order to solve the problem of poor decoding performance of the fixed normalization factor in the normalized minimum sum algorithm, the article proposes a variable normalization factor LDPC decoder, which improves the decoding performance compared to the fixed normalization factor. 0.2dB. At the same time, in order to solve the problems of low throughput and high storage resource usage of some parallel LDPC decoders, the parallelism of the system is increased by adopting the intra-layer parallel structure, and the consumption of storage resources is saved by time-division multiplexing of node data cache units. Experimental results show that compared with the traditional partially parallel structure, the decoder designed in this paper uses 13% more LUT resources, reduces storage resource consumption by 38%, and increases the decoding throughput by 14.5M.

## Inception-ResNet Assisted Iterative Decoding Algorithm Based on Alternating Direction Multiplier Method

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:10691538
- **Type**: conference
- **Published**: 20-22 Sept
- **Authors**: Cunrui Feng, Fan Zhou, Dengyun Cao
- **PDF**: https://ieeexplore.ieee.org/document/10691538
- **Abstract**: The application of deep learning to channel decoding methods has gradually become a hot research topic. However, the high complexity of deep neural network (DNN) parameters hinders the application of deep neural networks to long codes, and the difficulty of decoding increases exponentially with the increase of code length. To address this problem, this paper proposes a low-density parity-check (LDPC) decoding based on alternating direction multiplier method (ADMM) assisted by Inception-RestNet network. After passing through the channel with the noise codeword through the Inception-RestNet network to achieve the denoising process is input to the traditional ADMM decoder, and then according to the traditional this algorithm calculates the codeword with the original with the noise codeword to be processed and then go to reverse optimization of the denoising network, iterative operation between the Inception-RestNet and the hard verdict decoder can be reduce the effect of noise on the coded modulation system, thus enabling the decoder to obtain more accurate estimates. Experimental results show that the BER performance of this IR-ADMM decoder is improved by 0.5 dB with fewer iterations than the conventional LDPC decoder.

## A CNN-Aided Post-Processing Scheme for Channel Decoding Under Correlated Noise

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:10762738
- **Type**: conference
- **Published**: 20-22 Sept
- **Authors**: Junhao Liu, Shaoli Kang, Jing Cheng +2
- **PDF**: https://ieeexplore.ieee.org/document/10762738
- **Abstract**: In this paper, a convolutional neural network-aided post-processing scheme (CNNAPS) is proposed for improving the channel decoding performance of the denoiser under correlated noise. In this scheme, the CNN estimates actual channel noise for computing the error pattern, and then error nodes are identified by a threshold discrimination method. Specifically, the channel log-likelihood ratio (LLR) value of the identified error node is set to zero, while the received signal of the identified correct node is denoised. Furthermore, one of the key dvantages of CNNAPS is that it does not require knowledge of code structure properties, making it applicable to all linear block codes. Simulation results demonstrate that CNNAPS effectively identifies error nodes within error blocks. It is also shown that by implementing the post-processing along with a single redecoding, CNNAPS can significantly improve the error correction performance of the denoiser with minimal increase in complexity.

## QC-LDPC Standards for Optimized 5G Architecture

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:10994168
- **Type**: conference
- **Published**: 20-21 Sept
- **Authors**: Manish Gupta, Rajesh Kumar Singh, L. Suvonova +3
- **PDF**: https://ieeexplore.ieee.org/document/10994168
- **Abstract**: In the future phase of inventive television, quasi-cyclic minimum parity-check circuits are the suggested option for data streams. Signal words from the QC-LDPC encoding are promptly received by the rate matcher at the transmitter end. The rate matcher's duty is to choose the appropriate number of code bits by repetition and/or puncturing. Code segments that are not selected need not be encoded. The de-rate matcher at the receiver side combines code bits from many broadcast attempts before sending the code bits to the QC-LDPC decoder. Only the necessary systematic bits must be included in the output of the QC-LDPC decoder. Parity bits and unnecessary systematic bits may be completely removed from the decoding process. Instead of using a full-base matrix throughout the protection and decoding process, these variables permit the use of a lower sub-base matrix. In this study, we provide an effective implementation of 5G NR QC-LDPC codes. The full-base matrix is reduced before usage. Compared to earlier systems, the proposed method improves the 5G NR QC-LDPC upload performance..

## Probabilistic Shaping for Rotationally Symmetrical Two-Dimensional Constellations

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:10817302
- **Type**: conference
- **Published**: 2-5 Sept. 
- **Authors**: Ruimin Yuan, Xinyuanmeng Yao, Jiayi Yang +2
- **PDF**: https://ieeexplore.ieee.org/document/10817302
- **Abstract**: A ring-based constant composition distribution matcher (R-CCDM) is designed for shaping rotationally symmetrical two-dimensional (RS-2D) constellations. The procedure of distribution matching can be divided into two steps. First, nonuniformly distributed rings are generated by CCDM to approach a probability distribution calculated from that of modulation symbols. Second, a uniform mapping is performed to select one amplitude signal point from each ring. Compared with CCDM, the proposed DM contains multiple amplitude compositions, and hence achieves less rate loss. Numerical results show that, at moderate spectral efficiency, probabilistic shaping with R-CCDM outperforms that with CCDM by about $0.2 \sim 0.3 \mathrm{~dB}$ for different modulation formats.

## Deep Learning-Aided Phase Noise Mitigation for Backhaul Communication: A Model-Driven Approach

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:10817322
- **Type**: conference
- **Published**: 2-5 Sept. 
- **Authors**: Peyman Neshaastegaran, Ming Jian
- **PDF**: https://ieeexplore.ieee.org/document/10817322
- **Abstract**: This paper introduces a novel Model-Driven Deep Learning Assisted (MDLA) approach for phase noise (PN) estimation in wideband wireless backhaul scenarios. MDLA estimation combines a model-driven foundation for problem formulation with the computational power of Convolutional Neural Networks (CNN) to tackle the derived problem effectively. Exploiting inherent inter-correlations among PN-affected signals, MDLA method incorporates preceding and subsequent received signals in the PN estimation process. Moreover, a dedicated neural network is crafted to capitalize on input dependencies. This hybrid methodology demonstrates superior performance across diverse wideband scenarios, including constellation sizes, pilot overhead ratios, PN levels, and signal-to-noise ratios. The proposed MDLA scheme exhibits robustness in the face of reduced pilot overhead and achieves nearly optimal results in mitigating PN effects. In a 2 GHz bandwidth system with strong PN, MDLA remains within 0.2 dB and 0.5 dB of the PN -free system in 64-QAM and 256-QAM scenarios, respectively, at a coded bit-error-rate of $10^{-6}$.

## Coherence, Distance and Error: Understanding Coded Demodulation in PB-ToF Imaging

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:10720373
- **Type**: conference
- **Published**: 18-20 Sept
- **Authors**: Alvaro Lopez Paredes, Felipe Gutierrez-Barragan, Miguel Heredia Conde
- **PDF**: https://ieeexplore.ieee.org/document/10720373
- **Abstract**: One of the main objectives in coded Time-of-Flight is to precisely determine the position of the recovered target(s) with very few measurements or, in other words, to increase the resolution of the sensing system at high frame rates. In this scenario, we may cope with highly-coherent sensing matrices, i. e., there exist several columns very similar to each other. This may yield severe errors during the depth’s retrieval. In this paper, we show that the foreseen potential (probable) mismatches in the support estimation are related to the distance between the most cross-correlated columns over the sensing matrix, and propose a, to our knowledge, new metric which allows for estimating the average (absolute) recovery error. The metric is given by the mean absolute distance between each column and the most cross-correlated columns over the sensing matrix. We numerically evaluate various state-of-the-art demodulation schemes, and demonstrate that our metric reliably provides an estimation of their recovery performance, and complements other metrics traditionally used in Computational Sensing.

## Impact of Diffraction on Terahertz Compressed Sensing Single-Pixel Imaging

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:10720355
- **Type**: conference
- **Published**: 18-20 Sept
- **Authors**: Adolphe Ndagijimana, Iñigo Ederra, Miguel Heredia Conde
- **PDF**: https://ieeexplore.ieee.org/document/10720355
- **Abstract**: Terahertz (THz) single-pixel imaging, through compressive sensing, enables sampling below Nyquist rates and bypasses the need for mechanical scanning and the limitation of availability of high-resolution cost-effective THz imaging array detectors off-the-shelf. This research investigates how diffraction phenomena affect THz single-pixel imaging and properties of sensing matrices, along with the sparse signal reconstruction process. We introduce a variety of strategies designed to mitigate the effects of diffraction, along with novel methods to counteract the disruptions caused by THz physics, thereby preserving the integrity of the original sensing matrix and improving signal recoverability. A comprehensive simulation study sheds light on the effects of diffraction on the sensing matrices and their impact on signal reconstruction. Our results highlight the importance of accurate diffraction minimization techniques and sophisticated modelling in enhancing THz imaging systems.

## Fault-Tolerant Quantum Computing with the Parity Code: Discrete and Bosonic Concatenations

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:10821199
- **Type**: conference
- **Published**: 15-20 Sept
- **Authors**: Christophe Goeller, Anette Messinger, Michael Fellner +3
- **PDF**: https://ieeexplore.ieee.org/document/10821199
- **Abstract**: We present a fault-tolerant quantum computing architecture based on a code concatenation of the parity code. In addition to the recently explored concatenation with bosonic (i.e. continuous-variable) qubits, we propose and study a concatenation with discrete-variable stabilizer codes. The parity code can be understood as a low-density-parity-check (LDPC) code tailored specifically to obtain any desired logical connectivity from nearest neighbor physical interactions. On the bosonic side, the proposed scheme enables codes with better encoding rate compared to the repetition code with the same code distances, while requiring only weight-3 and weight-4 stabilizers and nearest neighbor 2D square-lattice connectivity. On the discrete-variable side, the proposed scheme enables Calderbank-Shor-Steane (CSS) codes with less physical qubits overhead compared to the surface code but they do not form a quantum LDPC family.

## Non-Binary Hypergraph Product Codes for Qudit Error Correction

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:10821254
- **Type**: conference
- **Published**: 15-20 Sept
- **Authors**: Shantom K. Borah, Asit K. Pradhan, Nithin Raveendran +2
- **PDF**: https://ieeexplore.ieee.org/document/10821254
- **Abstract**: Quantum low-density parity-check (QLDPC) codes are an important class of quantum error-correcting codes that have low-weight stabilizer generators and typically offer encoding rates much higher than popular topological quantum codes such as surface and toric codes. While recent constructions of QLDPC codes have been aimed at two-level quantum systems, several hardware platforms for quantum computing, including superconducting and photonic systems, support a much larger Hilbert space. This makes the design of qudit-based quantum LDPC codes an issue of paramount significance in harnessing the increased flexibility afforded by high -dimensional quantum systems. In this paper, we forge the first steps in addressing this gap and explore the generalization of QLDPC constructions to qudit systems. We review two methods of generalizing binary quantum codes to qudit codes, namely, the stack and merge constructions, and investigate the application of these two meth-ods to the well-known hypergraph product and lifted-product codes. Subsequently, we provide upper and lower bounds for the encoding rates of the resulting qudit codes. We also prove an interesting relationship between the qudit hypergraph product and qudit lifted-product codes: the merge construction applied to the lifted product code is equivalent to the stack construction applied to the hypergraph product code under certain conditions. We evaluate the performance of these qudit codes under non-binary belief-propagation decoding and observe that qudit codes offer us a greater degree of flexibility in optimizing their rate-performance trade-off. We also demonstrate that, under certain conditions, qudit codes can simultaneously achieve higher rates and higher frame error rate (FER) performance than their binary counterparts.

## Introducing Ambiguity Clustering: An Accurate and Efficient Decoder for qLDPC Codes

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:10821172
- **Type**: conference
- **Published**: 15-20 Sept
- **Authors**: Stasiu Wolanski, Ben Barber
- **PDF**: https://ieeexplore.ieee.org/document/10821172
- **Abstract**: We introduce Ambiguity Clustering, a new decoder for general quantum low-density parity check codes. On the recently proposed bivariate bicycle codes we find an order of magnitude speedup compared to the state-of-the-art BP-OSD decoder with no reduction in logical fidelity at physically realistic error rates. In particular, a single-threaded CPU implementation of Ambiguity Clustering is fast enough to decode the 144-qubit Gross code in real time for neutral atom and trapped ion systems.

## Parallel Minimum-Weight Parity Factor Decoding for Quantum Error Correction

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:10821203
- **Type**: conference
- **Published**: 15-20 Sept
- **Authors**: Liu Yang, Yue Wu, Lin Zhong
- **PDF**: https://ieeexplore.ieee.org/document/10821203
- **Abstract**: The Minimum-Weight Parity Factor (MWPF) de-coder is renowned for its accuracy in Quantum Error Correction (QEC) for various space-time codes, including surface codes and quantum LDPC codes. This work explores the scalability of MWPF decoders through parallelization, similar to parallel MWPM decoders. We introduce a dynamic fusion graph to schedule fusion operations in dynamic quantum circuits. It allows parts of the decoding graph to be solved and fused at a later stage, without having the full fusion tree at the very beginning. It also reduces the overhead caused by the traversing of the fusion tree. The dynamic fusion graph represents a novel and efficient method for real-time QEC decoding, providing enhancements in throughput and scalability for fault-tolerant quantum computing.

## A Quantum Approximate Optimization Algorithm-Based Decoder Architecture for NextG Wireless Channel Codes

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:10821436
- **Type**: conference
- **Published**: 15-20 Sept
- **Authors**: Srikar Kasi, James Sud, Kyle Jamieson +1
- **PDF**: https://ieeexplore.ieee.org/document/10821436
- **Abstract**: Forward Error Correction (FEC) provides reliable data flow in wireless networks despite the presence of noise and interference. However, its processing demands significant fraction of a wireless network's resources, due to its computationally-expensive decoding process. This forces network designers to compromise between performance and implementation complexity. In this paper, we investigate a novel processing architecture for FEC decoding, one based on the quantum approximate optimization algorithm (QAOA), to evaluate the potential of this emerging quantum compute approach in resolving the decoding performance-complexity tradeoff. We present FDeQ, a QAOA-based FEC Decoder design targeting the popular NextG wireless Low Density Parity Check (LDPC) and Polar codes. To accelerate QAOA-based decoding towards practical utility, FDeQ exploits temporal similarity among the FEC decoding tasks. This similarity is enabled by the fixed structure of a particular FEC code, which is independent of any time-varying wireless channel noise, ambient interference, and even the payload data. We evaluate FDeQ at a variety of system parameter settings in both ideal (noiseless) and noisy QAOA simulations, and show that FDeQ achieves successful decoding with error performance at par with state-of-the-art classical decoders at low FEC code block lengths. Furthermore, we present a holistic resource estimation analysis, projecting quantitative targets for future quantum devices in terms of the required qubit count and gate duration, for the application of FDeQ in practical wireless networks, highlighting scenarios where FDeQ may outperform state-of-the-art classical FEC decoders.

## Rate Adjustable Bivariate Bicycle Codes for Quantum Error Correction

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:10821206
- **Type**: conference
- **Published**: 15-20 Sept
- **Authors**: Ming Wang, Frank Mueller
- **PDF**: https://ieeexplore.ieee.org/document/10821206
- **Abstract**: This work (1) proposes a novel numerical algorithm to accelerate the search process for good Bivariate Bicycle (BB) codes and (2) defines a new variant of BB codes suitable for quantum error correction. In contrast to vanilla BB codes, where parameters remain unknown prior to code discovery, the rate of the proposed code can be determined before the search by specifying a factor polynomial. A number of new BB codes found by this algorithm are reported. In particular, by using the proposed construction of BB codes, we found a number of surprisingly short to medium-length codes that were previously unknown.

## GNarsil: Splitting Stabilizers into Gauges

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:10821364
- **Type**: conference
- **Published**: 15-20 Sept
- **Authors**: Oskar Novak, Narayanan Rengaswamy
- **PDF**: https://ieeexplore.ieee.org/document/10821364
- **Abstract**: Quantum subsystem codes have been shown to improve error-correction performance, ease the implementation of logical operations on codes, and make stabilizer measurements easier by decomposing stabilizers into smaller-weight gauge operators. In this paper, we present two algorithms that produce new subsystem codes from a “seed” CSS code. They replace some stabilizers of a given CSS code with smaller-weight gauge operators that split the remaining stabilizers, while being compatible with the logical Pauli operators of the code. The algorithms recover the well-known Bacon-Shor code computationally as well as produce a new [9, 1, 2, 2] rotated surface subsystem code with weight-3 gauges and weight-4 stabilizers. We illustrate using a [100, 25, 3] subsystem hypergraph product (SHP) code that the algorithms can produce more efficient gauge operators than the closed-form expressions of the SHP construction. However, we observe that the stabilizers of the lifted product quantum LDPC codes are more challenging to split into small-weight gauge operators. Hence, we introduce the subsystem lifted product (SLP) code construction and develop a new [775, 124, 20] code from Tanner's classical quasi-cyclic LDPC code. The code has high-weight stabilizers but all gauge operators that split stabilizers have weight 5, except one. In contrast, the LP stabilizer code from Tanner's code has parameters [1054, 124, 20]. This serves as a novel example of new subsystem codes that outperform stabilizer versions of them. Finally, based on our experiments, we share some general insights about non-locality's effects on the performance of splitting stabilizers into small-weight gauges.

## Research on Anti-Tampering Method of Convolutional Coding for Power Internet of Things Sensing

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:10754036
- **Type**: conference
- **Published**: 12-13 Sept
- **Authors**: Qilin Li, Hui He, Qiyue Zhou +1
- **PDF**: https://ieeexplore.ieee.org/document/10754036
- **Abstract**: With the development of Internet of Things technology, traditional power grids are gradually integrating with the Internet of Things to form the power Internet of Things, greatly improving the level of informatisation and intelligence. The terminal sensors in the perception layer of the power Internet of Things cannot apply complex security technologies due to device performance limitations, thus facing information security risks. This paper proposes a data tamper proof method for power IoT sensors based on convolutional encoding and decoding. This method can recover erroneous data to correct data when transmission information is disturbed and errors occur. Moreover, terminal devices of the power Internet of Things are usually embedded systems, and the communication, storage, and computing capabilities of the devices are limited to a certain extent. Convolutional codes have lower algorithm complexity and less computational overhead, and can adapt to most scenarios.

## Effective Diversity and Coding Gain over Fluid Antenna Channels

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:10694412
- **Type**: conference
- **Published**: 10-13 Sept
- **Authors**: Nikoloz Vashakidze, Joseph J. Boutros, Ghassan M. Kraidy +1
- **PDF**: https://ieeexplore.ieee.org/document/10694412
- **Abstract**: In this work, fluid antenna channels are investigated from the diversity and coding gain perspectives. From the dominant eigenvalues of the channel correlation matrix, the maximum diversity of the channel is estimated based on the Jakes’ correlation model. Two examples of Reed-Solomon-coded QAM constellations are then proposed that achieve the diversity limits of the channel. In addition, transmit port selection is analyzed, and finally two code constructions that achieve the diversity-security tradeoff of fluid compound channels are proposed. Results show that, for a fixed array width, diversity (and coding gain) quickly saturates with the increasing number of antennas where the performance is dictated by the number of dominant eigenvalues. Also, in absence of CSI at the transmitter side, the best option is to transmit over all ports rather than selecting a subset of ports by minimizing their correlation.

## PyJama: Differentiable Jamming and Anti-Jamming with NVIDIA Sionna

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:10694375
- **Type**: conference
- **Published**: 10-13 Sept
- **Authors**: Fabian Ulbricht, Gian Marti, Reinhard Wiesmayr +1
- **PDF**: https://ieeexplore.ieee.org/document/10694375
- **Abstract**: Despite extensive research on jamming attacks on wireless communication systems, the potential of machine learning for amplifying the threat of such attacks, or our ability to mitigate them, remains largely untapped. A key obstacle to such research has been the absence of a suitable framework. To resolve this obstacle, we release PyJama, a fully-differentiable open-source library that adds jamming and anti-jamming functionality to NVIDIA Sionna. We demonstrate the utility of PyJama (i) for realistic MIMO simulations by showing examples that involve forward error correction, OFDM waveforms in time and frequency, realistic channel models, and mobility; and (ii) for learning to jam. Specifically, we use stochastic gradient descent to optimize jamming power allocation over an OFDM resource grid. The learned strategies are non-trivial, intelligible, and effective.
