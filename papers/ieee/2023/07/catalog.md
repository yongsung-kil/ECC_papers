# IEEE Xplore — 2023-07


## Decoding LDPC Codes by Using Negative Proximal Regularization

- **ID**: ieee:10122222
- **Type**: journal
- **Published**: July 2023
- **Authors**: Yiming Chen, Rui Wang, Jinglong Zhu +1
- **PDF**: https://ieeexplore.ieee.org/document/10122222
- **Abstract**: The low-density parity-check (LDPC) decoding problem can be expressed as an integer linear programming (ILP) problem. One efficient method to solve the ILP problem is to relax the integer constraints and add penalty terms to the objective function, and the revised problem can be solved via the alternating direction method of multipliers (ADMM) algorithm. These penalty terms can punish the non-integral solutions and improve the decoding performance of the decoder. However, ADMM decoders are easily trapped in a local solution, which limits the frame error rate (FER) performance of the decoders at low signal-to-noise ratios (SNR). In this paper, we propose a restartable ADMM-based decoder using a negative proximal regularization. The negative proximal term will be updated whenever the decoder finds a new local solution. Therefore, the decoder can be restarted several times and the candidate solution which satisfies the parity-check equations and has the lowest objective function value can be selected as the decoder’s output. Some properties, together with several choices of penalty terms are discussed. We also investigate the convergence of our proposed decoder, and prove that the possibility of decoding errors is independent of the codeword that is transmitted. Simulation results show that our proposed decoder outperforms other ADMM-based decoders in most cases, while the decoding complexity maintains the same.

## Momentum-Based Symbol Flipping Decoding Algorithms for Non-Binary LDPC Codes

- **ID**: ieee:10050147
- **Type**: journal
- **Published**: July 2023
- **Authors**: Zhanzhan Zhao, Xiaopeng Jiao, Jianjun Mu +2
- **PDF**: https://ieeexplore.ieee.org/document/10050147
- **Abstract**: This paper investigates the application of gradient descent with momentum in symbol flipping decoding algorithms based on prediction (SFDP) for non-binary low-density parity-check (NB-LDPC) codes. The momentum added in the objective function of SFDP algorithms can provide inertia to the decoding process by considering the flipping states in the past iterations. Simulation results show that the proposed momentum-based SFDP algorithms perform significantly better than the original SFDP algorithms with low extra complexity. Furthermore, to lower the error floor of momentum-based SFDP algorithms, we also introduce artificial noises into the objective functions of momentum-based SFDP algorithms to help the iterative decoding escape from local optimum.

## The Syndrome Bit Flipping Algorithm for LDPC Codes

- **ID**: ieee:10113636
- **Type**: journal
- **Published**: July 2023
- **Authors**: Emmanuel Boutillon, Chris Winstead, Fakhreddine Ghaffari
- **PDF**: https://ieeexplore.ieee.org/document/10113636
- **Abstract**: Performance of LDPC decoders at high SNR is dominated by trapping sets that induce an error floor in the performance curve. We propose a new algorithm that resolves trapping sets and lowers the error floor. The new algorithm, called Syndrome Bit Flipping (SBF), computes the sum of adjacent parity violations at each symbol node. Bits are flipped by comparing the syndrome sum against a time-varying threshold called the decoding key. SBF is compared to other bit-flipping decoders on the Binary Symmetric Channel (BSC), and is demonstrated as a post-processing step for a Noisy Gradient Descent Bit-Flipping (NGDBF) hardware decoder. We demonstrate the post-processing method for an LDPC code defined in the 802.3an standard, and find that the frame error rate is improved by at least two orders of magnitude, even as the required iterations are reduced by 33%.

## Improving the Thresholds of Generalized LDPC Codes With Convolutional Code Constraints

- **ID**: ieee:10121163
- **Type**: journal
- **Published**: July 2023
- **Authors**: Muhammad Umar Farooq, Alexandre Graell i Amat, Michael Lentmaier
- **PDF**: https://ieeexplore.ieee.org/document/10121163
- **Abstract**: CC-GLPDC codes are a class of generalized low-density parity-check (GLDPC) codes where the constraint nodes (CNs) represent convolutional codes. This allows for efficient decoding in the trellis with the forward-backward algorithm, and the strength of the component codes easily can be controlled by the encoder memory without changing the graph structure. In this letter, we extend the class of CC-GLDPC codes by introducing different types of irregularity at the CNs and investigating their effect on the BP and MAP decoding thresholds for the binary erasure channel (BEC). For the considered class of codes, an exhaustive grid search is performed to find the BP-optimized and MAP-optimized ensembles and compare their thresholds with the regular ensemble of the same design rate. The results show that irregularity can significantly improve the BP thresholds, whereas the thresholds of the MAP-optimized ensembles are only slightly different from the regular ensembles. Simulation results for the AWGN channel are presented as well and compared to the corresponding thresholds.

## Hamming-Distance Trellis Min-Max-Based Architecture for Non-Binary LDPC Decoder

- **ID**: ieee:10032576
- **Type**: journal
- **Published**: July 2023
- **Authors**: Thang Xuan Pham, Tuy Tan Nguyen, Hanho Lee
- **PDF**: https://ieeexplore.ieee.org/document/10032576
- **Abstract**: Limitations on hardware resource consumption and throughput make the use of non-binary low-density parity-check (NB-LDPC) codes challenging in practical applications. This brief first proposes a novel check-node (CN) decoding algorithm called Hamming-distance trellis min-max (H-TMM) to reduce the complexity introduced by searching for two minimum values in previous TMM-based algorithms. Then, by taking advantage of the proposed algorithm and the number appearances of reliable values, a high-performance H-TMM-based NB-LDPC decoder architecture is presented. Experiments on the 32-ary (837, 726) NB-LDPC code confirmed that the proposed decoder can obtain a high throughput on less hardware resources compared with the state-of-the-art works while maintaining a competitive error-correcting performance. In particular, the proposed CN unit architecture reduced hardware resources by almost half compared to that in the latest decoder.

## Winning by Successive Failures—Enhanced Link Adaptation for Cellular Networks

- **ID**: ieee:10132391
- **Type**: journal
- **Published**: July 2023
- **Authors**: Gideon Kutz, Amit Bar-Or Tillinger, Tal Oved +3
- **PDF**: https://ieeexplore.ieee.org/document/10132391
- **Abstract**: Link adaptation algorithm that tailors the data transmission coding-rate to the dynamic channel state is an essential ingredient in any (modern) cellular network. Current link adaptation schemes are based on the usage of periodic pilots sent by the base station. The mobile terminal determines the optimal coding-rate to be employed based on processing the received pilots, and then reports its findings back to the base station. Herein, we show that these schemes perform far from optimal and do not come close to achieving the channel capacity. To address this shortcoming, we propose enhanced link adaptation scheme based on a rateless-like coding approach. According to the proposed scheme, the base station sends multiple re-transmissions, effectively combined at the receiver side, until decoding is successful. It is demonstrated that the proposed scheme can closely track the channel capacity, even for highly mobile terminals, hence achieving significant gains over current link adaptation schemes. From the practical side, we address several implementation-related issues thus paving the way for the adaptation of the proposed scheme to the use of 5G networks.

## Reinforcement-Learning-Based Overhead Reduction for Online Fountain Codes With Limited Feedback

- **ID**: ieee:10119212
- **Type**: journal
- **Published**: July 2023
- **Authors**: Zijun Qin, Zesong Fei, Jingxuan Huang +3
- **PDF**: https://ieeexplore.ieee.org/document/10119212
- **Abstract**: We investigate the application of reinforcement learning (RL) on online fountain codes, and propose two schemes to reduce the full-recovery overhead with limited feedback. First, we use RL in determining the optimal degree of coded symbols for a given number of feedback, and propose the RL-based degree determination (RL-DD), with the help of theoretical analysis of the relationship between recovery rate and buffer occupancy. Then we propose online fountain codes with no build-up phase using sectioned distribution (OFCNB-SD), where the encoder sends symbols whose degrees are sampled from different sections of an overall distribution, and the decoder is improved to utilize coded symbols that are not immediately decodable. We present theoretical analysis of OFCNB-SD, and introduce RL-based sectioned distribution (RL-SD) scheme where the sectioning of the overall distribution is optimized with RL. Simulation results show that our proposed schemes could achieve lower full-recovery overhead with limited feedback compared to existing schemes.

## Sub-4.7 Scaling Exponent of Polar Codes

- **ID**: ieee:10063203
- **Type**: journal
- **Published**: July 2023
- **Authors**: Hsin-Po Wang, Ting-Chun Lin, Alexander Vardy +1
- **PDF**: https://ieeexplore.ieee.org/document/10063203
- **Abstract**: Polar codes approach channel capacity provably and empirically and are thereby a constituent code of the 5G standard. Compared to low-density parity-check codes, however, the performance of short-length polar codes have rooms for improvement that could hinder its adoption by a wider class of applications. As part of the program that addresses the performance issue at short length, it is crucial to understand how fast binary memoryless symmetric channels polarize. A number, called scaling exponent, was defined to measure the speed of polarization and several estimates of the scaling exponent were given in literature. As of 2022, the tightest overestimate is 4.714 made by Mondelli, Hassani, and Urbanke in 2015. We lower the overestimate to 4.63. The idea behind this improvement is that, instead of describing the relation between a channel  ${W}$  and its children  ${W}^ {\scriptscriptstyle {\boxed {\star}}}$  and  ${W}^ {\bigcirc \!\!\! \star}$ , we describe the relation between  ${W}$  and its grandchildren  $ {W}^{\scriptscriptstyle {\boxed {\star}} \, {\scriptscriptstyle {\boxed {\star}}} }$ ,  ${W}^{\scriptscriptstyle {\boxed {\star}}\, {{\bigcirc \!\! \star} }}$ ,  ${W}^{{\bigcirc \!\!\! \star}\,\,{\scriptscriptstyle {\boxed {\star}}} }$ , and  $ {W}^{{\bigcirc \!\!\! \star}\,{\bigcirc \!\!\! \star} }$ . By doing so, the evolution of channels becomes “less Markovian” and hence more tighter inequalities can be obtained.

## On the Probabilistic Quantum Error Correction

- **ID**: ieee:10063938
- **Type**: journal
- **Published**: July 2023
- **Authors**: Ryszard Kukulski, Łukasz Pawela, Zbigniew Puchała
- **PDF**: https://ieeexplore.ieee.org/document/10063938
- **Abstract**: Probabilistic quantum error correction is an error-correcting procedure which uses postselection to determine if the encoded information was successfully restored. In this work, we analyze the probabilistic version of the error-correcting procedure for general noise. We generalize the Knill-Laflamme conditions for probabilistically correctable errors. We show that for some noise channels, the initial information has to be encoded into a mixed state to maximize the probability of successful error correction. Finally, the probabilistic error-correcting procedure offers an advantage over the deterministic procedure. Reducing the probability of successful error correction allows for correcting errors generated by a broader class of noise channels. Significantly, if the errors are caused by a unitary interaction with an auxiliary qubit system, we can probabilistically restore a qubit state by using only one additional physical qubit.

## Flexible transceiver for an access network: a multicarrier entropy loading approach

- **ID**: ieee:10153945
- **Type**: journal
- **Published**: July 2023
- **Authors**: Gengchen Liu, Ji Zhou, Yuanda Huang +9
- **PDF**: https://ieeexplore.ieee.org/document/10153945
- **Abstract**: To cope with the extraordinary bandwidth demand, an optical access network based on point-to-multipoint (P2MP) topology has been widely applied. Recently, flexible transceivers have been investigated to maximize the optical power budget of optical network units for increasing the capacity of passive optical networks. In this work, we experimentally demonstrate a low-cost, high-bandwidth P2MP solution based on multicarrier modulations and probabilistic constellation shaping technology by reusing a 10G class directly modulated laser and avalanche photodetector for the first time to our knowledge. The proposed P2MP solution is capable of achieving fine granularity data rate adjustment from 12.5 Gb/s up to 63 Gb/s. We discuss the hardware implementation aspect of the proposed multicarrier entropy loading flexible transceiver. By means of a real-time transmission experiment, we show that the proposed P2MP solution can achieve a 29 dB power budget at a symmetric 53 Gb/s line rate, which makes it well positioned to support non-residential P2MP applications such as passive optical local area networks and fiber-to-the-office.

## A Model-Driven Quasi-ResNet Belief Propagation Neural Network Decoder for LDPC Codes

- **ID**: ieee:10217911
- **Type**: conference
- **Published**: 9-12 July 
- **Authors**: Liangsi Ma, Bei Liu, Xin Su +1
- **PDF**: https://ieeexplore.ieee.org/document/10217911
- **Abstract**: For the Belief Propagation (BP) algorithm of low-density parity-check (LDPC) codes, existing deep learning methods have a limited performance improvement and it is difficult to train deep-level networks. In this paper, a model-driven quasi-residual network (Quasi-ResNet) BP decoding architecture is proposed for LDPC codes to further improve the performance of standard BP decoding. This method feeds the reliable messages calculated in current iteration into the next iteration based on the shortcut connection, and adjusts the weight of shortcut connection based on the error Back Propagation algorithm of neural network to determine the optimal genetic proportion of reliable messages. The decoding architecture is composed of a model-driven deep neural network (DNN) and shortcut connection. Simulation results show that the decoder can not only unfold more layers quickly compared with the DNN-based BP decoder, but also further improve the decoding performance.

## A Highly Robust Secret Key Reconcile System Based on Cyclic Shift Buffer and HARQ Mechanism

- **ID**: ieee:10271035
- **Type**: conference
- **Published**: 8-10 July 
- **Authors**: Haojie Han, Linning Peng, Hua Fu +3
- **PDF**: https://ieeexplore.ieee.org/document/10271035
- **Abstract**: Secret keys generated from wireless channel can provide high level of security. The error correction code (ECC) based information reconciliation method owns the benefits of high security and efficiency. In this paper, we designed a highly robust secret key reconcile system using low-density parity-check (LDPC) codes to correct disagreed key bits. In this system, we cache some high-quality secret key bits in a cyclic shift buffer (CSB) for compensation, which can effectively reduce the over-all key disagreement rate (KDR). Combined with a simple hybrid automatic repeat request (HARQ) implementation, this system significantly improves the correction success rate of information reconciliation. We built a realtime secret key generation system using universal software radio peripheral (USRP). Extensive experiments were carried out in different channel state information (CSI) scenarios. The proposed system can improve the success rate of secret key generation effectively in all experiment scenarios, especially in the case of low USRP Tx/Rx gain setups.

## FPGA Implementation of Elliptic Curve Encryption Algorithm Based on PUFs

- **ID**: ieee:10270847
- **Type**: conference
- **Published**: 8-10 July 
- **Authors**: Yi Li, Hao Yin, Caicai Wang +1
- **PDF**: https://ieeexplore.ieee.org/document/10270847
- **Abstract**: Elliptic curve encryption algorithm has a wide range of applications in the field of blockchain and information security. The traditional elliptic curve encryption scheme stores the user private key in the system hardware. When an attacker obtains the user private key in some way, the user will face serious information security problems. To improve the security of the user private key, we propose to use the response of physical unclonable functions (PUFs) as the user private key. PUFs can reduce the risk of users’ private keys being acquired by attackers due to its characteristics of non-cloning, real-time reading and unpredictability. The longest operation in elliptic curve encryption algorithm is the dot product operation. In order to solve the problem of mismatch between PUFs response generation rate and point product operation, we optimize the structure of the underlying multiplier in the binary domain to effectively reduce the consumption of hardware resources and achieve faster point product operation. The experimental results show that when the key length is 233 bits, the system clock can reach 103MHz and the minimum time of single encryption operation is only 69.4$\mu$s on Xilinx Artix-7 FPGA.

## A Doppler Reciprocity based Key Generation Method for C-V2X System

- **ID**: ieee:10270831
- **Type**: conference
- **Published**: 8-10 July 
- **Authors**: Xianzu Xue, Linning Peng, Hua Fu +1
- **PDF**: https://ieeexplore.ieee.org/document/10270831
- **Abstract**: In this paper, we design a key generation system based on the C-V2X protocol, which employs the Doppler reciprocity between two vehicles. By exploiting the symmetric measurements of the Doppler frequency offset as the secret source, nodes in vehicular networks aim to obtain identical secret keys. A simulation system is designed using the measured vehicle movement in the Next Generation Simulation (NGSIM) dataset. The effect of the frequency offset of the crystal oscillator is also taken into account. Simulation results show that the proposed Doppler reciprocity based key generation method could achieve a low key disagreement rate (KDR) and good randomness under different vehicular networks scenarios.

## Speculative ECC and LCIM Enabled NUMA Device Core

- **ID**: ieee:10213102
- **Type**: conference
- **Published**: 7-9 July 2
- **Authors**: You Zhang, Ke Yang, Yihan Wang +2
- **PDF**: https://ieeexplore.ieee.org/document/10213102
- **Abstract**: Advanced process technology allows high memory density while securing high bandwidth. However, the increasing disparity between the computing unit and memory known as the memory wall impedes applications like artificial intelligence (AI) related workloads. The larger area of the memory cell introduces more memory defects, and this causes a memory yield problem. Error-correction code (ECC) is a widely used technique in modern computer architecture for system robustness. The overhead introduced by ECC limits the performance in certain timing-critical applications, like caches. The real time ECC combined with in-memory computation shows great power in addressing the performance and power bottlenecks. This paper proposes a hardware architecture to support memory ECC speculative computing cache. The paper presents a memory structure that implements separate data memory and tag memory, breaking the serialization between data access and error detection. The data is fetched making the prediction that tag is correct and uncorrupted. The system is rolled back when the prediction is wrong. Further optimization involves in-memory computing, which saves memory bandwidth. The proposed ECC speculative computing cache also reduced power and area overhead by reusing the logic from the computing cache.

## Advances and Challenges in Physical Layer Security: A Comprehensive Review

- **ID**: ieee:10257614
- **Type**: conference
- **Published**: 7-9 July 2
- **Authors**: Nina Zhang, Yuxin Ai, Dehua Zhang +2
- **PDF**: https://ieeexplore.ieee.org/document/10257614
- **Abstract**: Physical layer security (PLS) has emerged as a promising approach to enhance the security of wireless communication systems. This paper provides a comprehensive review of PLS, including its basic concepts, key techniques, and recent developments. We begin by introducing the basic principles of PLS, including the concept of secrecy capacity and the key assumptions underlying PLS. We then discuss various techniques that have been proposed to enhance PLS, such as artificial noise, cooperative jamming, and beamforming. Next, we review recent research on PLS in different scenarios, including multi-user systems, cognitive radio networks, and wireless sensor networks. Finally, we conclude by discussing future research directions and open challenges in PLS.

## Addendum Parity Check Codes for Futuristic Wireless Communications

- **ID**: ieee:10193041
- **Type**: conference
- **Published**: 6-8 July 2
- **Authors**: N Radha., M. Maheswari, B. Ajay Kumar +2
- **PDF**: https://ieeexplore.ieee.org/document/10193041
- **Abstract**: In recent days, wireless communication has become an integral part of human lives. Hence, data transmitted through wireless must be highly reliable. The reliability of the wireless data will be enhanced by incorporating errorcorrecting codes. There are numerous error correction codes available in a wireless communication system. To enhance the error correction capability, in this paper, Addendum Parity Check–Error Detection and Correction (ADDPC–EDAC) code has been developed that corrects all the errors in the message bits. The proposed ADDPC-EDAC code has been designed using cadence 90 nm technology. To evaluate the errorcorrecting capability of the proposed code, BER vs. SNR analysis was carried out for modulation by BPSK over the AWGN channel. The BER vs. SNR analysis is also compared with the existing error correction codes. Compared with the existing error correction codes, the proposed ADDPC-EDAC results outperform by showing a lesser BER. The proposed code consumes less power, occupies a smaller area, and has a lesser delay compared to the existing codes. The proposed error correction scheme can be used for wireless communication.

## Uplink Performance Analysis of PD-NOMA System

- **ID**: ieee:10306916
- **Type**: conference
- **Published**: 6-8 July 2
- **Authors**: Bollineni Krishna Sai, Ranjith V, Parameswaran Ramesh +1
- **PDF**: https://ieeexplore.ieee.org/document/10306916
- **Abstract**: Non-Orthogonal Multiple Access (NOMA) is one of the potential radio access methods suggested for 5G networks to improve the performance of 5G users. This research presents the work made on the 5G PD-NOMA system. The objective of the research is to analyze the bit error rate experienced by UEs under different channel models, different encoding techniques, and different modulation schemes. The MATLAB-based Uplink system model for PD-NOMA is developed to make in-depth studies on channel parameters, a path loss model, modulation techniques, and encoding techniques. This research utilizes BPSK modulation, lognormal, two-ray, and free-space channel models, convolutional encoding, and low-density parity check (LDPC) encoding techniques for investigation purposes. From the research obtained, it is found that LDPC code exhibits a lesser probability of error compared to convolutional coding on BPSK modulated data.

## Design of Low-Power Turbo Coder for Low-Energy Mobile Communications

- **ID**: ieee:10307894
- **Type**: conference
- **Published**: 6-8 July 2
- **Authors**: G. Shanthi, Y. Vishwakanth, L. Dharma Teja +2
- **PDF**: https://ieeexplore.ieee.org/document/10307894
- **Abstract**: Mobile Communication systems use turbo codes for correcting errors. As compared to other error correction codes, turbo codes provide great error correcting capabilities. The design of the low-power Turbo decoder in this paper is suggested as a (VLSI) Very Large-Scale Integration architecture. Inter-leavers, de-inter-leavers, and soft-in-soft-out decoders are utilized on the decoder's side, which uses the (MAP) maximum-a-posterior-algorithm. The usage of the MAP algorithm reduces Number of iterations necessary to decode the information bits being transferred. This research employs an encoder component consisting of two recursive convolutional encoders and a pseudorandom interleaved on the encoder side. The Xilinx ISM tool is used to do the Turbo encoding and decoding. The clock gating method is utilized to decrease the dissipation of power in the circuit, the simulation results show before clock gating the power dissipated in the circuit was around 112m Watts, later After using clock gating in the circuit the power dissipation is reduced to around 32m Watts. we can observe the timing, clock, power, and area reports at the end of simulations and synthesis. This research is implemented by synthesizing results from Xilinx ISM and Quartus tools to know the power analysis report. By using the clock gating technique area of the circuit might increase but the power is reduced for good performance of the circuit.

## LDPC Over Multihop LoRa Nodes with Peeling Decoder

- **ID**: ieee:10335410
- **Type**: conference
- **Published**: 6-7 July 2
- **Authors**: Rustanto, M. S. Arifianto
- **PDF**: https://ieeexplore.ieee.org/document/10335410
- **Abstract**: Wireless radio communication is expected to reach long distances and be of good quality. To achieve long-distance radio communication, relay stations can be added between the source to the destination points as needed. The utilization of wireless radio introduces vulnerabilities to the quality of communication due to noise and interference. In this research a multihop communications is created using four stationary LoRa nodes. Error correction and detection were added to the multihop communication. The Low-Density Parity Check (LDPC) regular binary 16x32 technique is used in this research for multihop communication at encoder node 1 and decoder node 4. Meanwhile, node 2 and node 3 serve as repeaters between node 1 and node 4. The type of LDPC used is binary encoder, and the decoder uses the peeling technique. Each node's implementation involves the use of hardware modules BeagleBone Black Industrial and LoRa Ebyte. The software utilized includes the debian console and Python programming. This multihop communication has undergone testing for parameters such as processing time, RSSI field test, and peeling error detection and correction ability.

## Looping for Encryption Key Generation Over the Internet: A New Frontier in Physical Layer Security

- **ID**: ieee:10201818
- **Type**: conference
- **Published**: 4-7 July 2
- **Authors**: Amir K. Khandani
- **PDF**: https://ieeexplore.ieee.org/document/10201818
- **Abstract**: Current key sharing techniques rely on the hardness of solving a solvable, but complex, mathematical problem. This entails, in Information Theoretical sense, the encryption key is not secret, it can be found by solving the underlying mathemat-ical problem. Sensitive data we encrypt today using traditional techniques can be recorded by malicious parties and be deciphered in the future whenever improved hacking techniques and supporting computing technology permit. Information Theory proves the existence of methods for sharing of encryption keys that are unconditionally secure, but does not show how to bring such theoretical results to practical use. One of the central information theoretical approaches to key sharing is based on exploiting common randomness. This theoretical result states that if two dependent random variables, $A$ and B, are available at Alice and Bob, then, by communicating through a public channel between $A$ and B, it is possible to securely share a key of size I(A;B). To bridge the gap between theory and practice, one needs a method to generate two sets of dependent random variables, one at Alice‘s side and the other one at the Bob’ side, as well as a method to extract two identical keys from these dependent random variables. This article presents a novel technique to achieve this goal over the Internet. Dependent random variables are generated by measuring packet travel times between Alice and Bob, and error-free key extraction from dependent random variables is realized by using a randomized Low Density Parity Check Code (LDPC). Through looping of packets between Alice and Bob, the mutual information between random variables is increased. Finally, methods are presented to measure the likelihood values required in decoding the underlying LDPC. It is shown that the key rate is approximately equal to $0.5\log_{9}(4L^{2}/(4L-1))\approx 0.5\log_{2}(L)$ where $L$ is the number of round trips (loops). Test results (based on measurements between distant nodes over the Internet) are presented, demonstrating the feasibility of the proposed technique. The proposed method is implemented entirely in software (through high-level programming, e.g., using C-language, at the application layer). This operation does not require modifying the underlying network.

## Design and Performance Analysis of a Novel HQAM for Telecommunication Systems

- **ID**: ieee:10212916
- **Type**: conference
- **Published**: 30 June-2 
- **Authors**: Zhanyang Zhou, Yingtao Niu, Boyu Wan +1
- **PDF**: https://ieeexplore.ieee.org/document/10212916
- **Abstract**: QAM (Quadrature Amplitude Modulation) formats are widely used in today's digital wireless communications systems. Most of the existing QAM constellations have adopted rectangular constellation design for higher information transmission efficiently. However, rectangular QAM constellations have unequal Euclidian distance among their adjacent constellation points in their constellation schemes, which reduces their energy efficiency. In this paper, a novel regular hexagonal QAM (hereinafter referred to as “HQAM”) is proposed to enhance the signal energy efficiency of QAM constellations. In the proposed constellation, the distribution of its constellation points is based on regular hexagon patterns, therefore the Euclidean distance among its adjacent constellation points is equal, which can make the best use of the signal transmission energy. In order to verify the proposed scheme, regular hexagonal 18QAM is used as an example. In this 18HQAM based on our proposed novel constellation formation, every 8 codes are taken as a group, and an extra 1bit information is used for parity check. Theoretical analysis shows that the novel HQAM constellation design has higher energy efficiency than that of the existing rectangular QAM constellation. The simulation results show that the SER (Symbol Error Rate) of the proposed 18HQAM is better than that of the existing 16QAM, and the information carried by every signal symbol is also more than that of the existing 16QAM. Therefore, the proposed HQAM constellation can improves the efficiency and reliability of signal transmission in digital wireless communication systems.

## A Bit-Interleaved Coded Modulation Scheme Based on the Polar Code in Underwater Acoustic OFDM Communication System

- **ID**: ieee:10212576
- **Type**: conference
- **Published**: 30 June-2 
- **Authors**: Mei-Qi Wen, Chuan-Lin He, Si-Yu Xing
- **PDF**: https://ieeexplore.ieee.org/document/10212576
- **Abstract**: A Bit-Interleaved Code Modulation (BICM) scheme based on the polar codes (Polar-BICM), suitable for the underwater acoustic (UWA) communication system utilizing orthogonal frequency division multiplexing (OFDM) is proposed in this paper. In the proposed scheme, the design and implementation of the encoder and the modulator are combined to improve the communication rate, while the traditional schemes usually consider independently. The system BER performance affected by variance interleaver types, interleaver lengths and code lengths are carefully discussed in this paper. The LDPC-BICM system and the Trellis Coded Modulation (TCM) scheme are chosen as the control schemes. Simulation and experimental results show that the BER performance of the UWA OFDM communication system based on Polar-BICM is much better than that based on the TCM scheme. Moreover, a higher coding gain than the LDPC-BICM UWA OFDM system is obtained because of the Polar Code. At the same time, the compiled code implementation of Polar Code is relatively simpler than that of the LDPC coding scheme. Therefore, the Polar-BICM system improves the transmission efficiency of the system effectively without losing reliability, which contributes a lot to the practical application of the coding and modulation combination technology in UWA communication.

## On the Performance of LDPC Codes over Radio Stripes System

- **ID**: ieee:10221509
- **Type**: conference
- **Published**: 3-6 July 2
- **Authors**: Ali Gashtasbi, Mário Marques Da Silva, Rui Dinis
- **PDF**: https://ieeexplore.ieee.org/document/10221509
- **Abstract**: In the scope of beyond 5G and the forthcoming 6G, Radio Stripes (RS) have been proposed as a potential technique to enhance communications quality for new users. In this paper, we examine the functionality of an RS-aided wireless communication systems, where the transmitted signal is encoded with low-density parity check (LDPC) codes to improve the signal quality. In order to provide high-power, low-latency in 5G communications, LDPC codes, which permit encoding-decoding, have been used. Inter-channel interferences and performances are aimed to be improved with LDPC codes by achieving over 2.5 dB gain, in terms of Bit Error Rate. Using Monte Carlo simulations for various numbers of RS-reflecting elements, we show the validity of the beneficial effect of this type of codes.

## Aircraft Optical Video Transmission Communication based on the Forward Error Correction Codes

- **ID**: ieee:10221478
- **Type**: conference
- **Published**: 3-6 July 2
- **Authors**: Aleksandr Krotov, Mihail Krotov, Svitlana Matsenko +2
- **PDF**: https://ieeexplore.ieee.org/document/10221478
- **Abstract**: Modern aircraft information and telecommunication systems are segmented into two separate networks: data transmission and video networks. This differs from the typical approach for modern telecommunications in which all types of traffic are transmitted through one network (for example, access NGN-IMS networks). The external aircraft electromagnetic environment is constantly becoming more complicated: the high intensity of the electromagnetic field $(E_{mf})$ due to the increase of radio frequencies quantity and their frequencies spectrum expansion, which occupies a band from 10 kHz to 3 GHz that affects the quality of service of electronic devices on board. A new method of image representation with forward error correction (FEC) codes was developed and considered. The method decreases the Bit Error Ratio (BER) for asymmetric data transmission via fiber optics and computational complexity for video correction. The paper investigates the superior performance of Low-Density Parity-Check (LDPC-) based on Irregular Repeat-Accumulate (IRA) codes over regular LDPC codes for the same code rate with Gaussian noise to match a certain signal-to-noise ratio (SNR). The LDPC FEC codes are simulated with code rates $R_{c}\in\{1/2\}$ from the digital video broadcasting by satellite - second-generation (DVB-S2) standard. This setup has 17 low-data network subscribers and one highly loaded network section for video transmission. This approach makes it possible to increase the load in the asymmetric networks for aircraft onboard electronic systems and to ensure the quality of video images in the pickup environment to avionics during operation, for example, radar devices.

## On the LIS System Performance with and without Equalization

- **ID**: ieee:10221448
- **Type**: conference
- **Published**: 3-6 July 2
- **Authors**: Ali Gashtasbi, Mário Marques da Silva, Rui Dinis
- **PDF**: https://ieeexplore.ieee.org/document/10221448
- **Abstract**: The Large Intelligent Antenna System (LIS) is a noteworthy development in wireless communications by targeted propagation waves. The LIS idea goes beyond massive MIMO. The LIS consists of a surface that radiates continuously and is made up of a number of small panels that are placed close to the users and can exchange signals. This paper shows the results of a combination of LIS systems with Low-Density Parity-Check (LDPC), comprising Single Carrier with Frequency Domain Equalization (SC-FDE) with four different receiver types: Equal Gain Combining (EGC), Maximum Ratio Combining (MRC), Zero Forcing (ZF), and Minimum Mean Squared Error (MMSE). It is shown that, in the above-described scenario, for some receiver types, equalization can be avoided without degrading performance, while the complexity is reduced.

## Design of F-L-QC-LDPC Decoder Based on LNMS Decoding Algorithm

- **ID**: ieee:10280802
- **Type**: conference
- **Published**: 29-31 July
- **Authors**: Youyao Liu, Haimei Huang, Jialei Gao +1
- **PDF**: https://ieeexplore.ieee.org/document/10280802
- **Abstract**: Low Density Parity Check Code (LDPC) can meet the decoding requirements of a variety of code lengths and rates in different communication scenarios, but the LDPC code check matrix is irregular, which has problems with difficult storage and reading of the check matrix and high coding complexity. For the decoding requirements of multi-code length, this paper proposes a Quasi Crystal Low Density Parity Check Codes (QCLDPC) code based on Fibonacci Lucas sequence, which can obtain the codewords with different code length and code rate by changing the number of rows and columns of the exponential matrix. In terms of decoding algorithms, the Layered Non-Maximum Suppression (LNMS) decoding algorithm, which combines the minimum sum decoding algorithm with the layered algorithm, is proposed to improve the convergence speed of decoding iteration and decoder throughput. Through simulation and comparative experiments, it is proved that this design can support a variety of bit rates, block lengths and sub matrix sizes, and meet the requirements of high throughput and low complexity decoder in modern communication systems.

## Fast Bit-Flipping Decoding of Polar Codes with Additional Nodes

- **ID**: ieee:10225069
- **Type**: conference
- **Published**: 29 June-3 
- **Authors**: Ilya S. Timokhin, Fedor I. Ivanov
- **PDF**: https://ieeexplore.ieee.org/document/10225069
- **Abstract**: Polar codes have gained significant a ttention in recent years due to their superior performance, making them an attractive choice for use in modern communication systems. In this paper, we present a novel approach for implementing a fast decoding method for polar codes with additional nodes. Specifically, we propose a modification of the fast decoding method with bit-flipping capability, called the GSCLAF, which is designed to improve the correction capability of the decoder. To achieve this, we consider additional nodes of five types, which are obtained by a combination of basic generalized nodes, namely information, frozen, SPC, and REP nodes. To evaluate the performance of our proposed algorithm, numerical experiments were conducted using the 5G NR polar code. The results of these experiments demonstrate the effectiveness of GSCLAF relative to other popular polar decoding algorithms. Overall, our proposed algorithm provides a powerful tool for improving the decoding performance of polar codes with additional nodes, making it a promising solution for modern communication systems that require high data rates and reliable communication.

## Enhanced Bluetooth with Low-Density Parity-Check Codes

- **ID**: ieee:10202150
- **Type**: conference
- **Published**: 28 June-1 
- **Authors**: Pawarit Manakul, Usana Tuntoolavest, La-or Kovavisaruch +1
- **PDF**: https://ieeexplore.ieee.org/document/10202150
- **Abstract**: In order to enhance Bluetooth, this paper proposes to employ a low-density parity-check (LDPC) code instead of S2 and S8 coding schemes in Bluetooth Low Energy (BLE) coded standard. Since decoding LDPC codes requires log-likelihood ratios (LLRs), the Viterbi algorithm is modified so that it can obtain the LLR from the correlation between received and reference signals. Simulation results under the additive white Gaussian noise (AWGN) channel condition show that when signal-to-noise ratio (SNR) is greater than or equal to 3 dB, Bluetooth LDPC performance with LDPC is superior to both of the standard BLE coded schemes. Moreover, the average decoding time is 16.954 times shorter than that of BLE coded S8. Thus, enhanced Bluetooth LDPC is suitable for the AWGN channel with SNR greater than or equal to 3 dB because it needs fewer redundancy bits to provide lower packet error rate (PER) with shorter decoding time.

## Efficient Genetic Algorithm-based LDPC Code Design for IoT Applications

- **ID**: ieee:10227247
- **Type**: conference
- **Published**: 27-28 July
- **Authors**: Loc Nguyen-Van-Thanh, Tan Do-Duy
- **PDF**: https://ieeexplore.ieee.org/document/10227247
- **Abstract**: In this paper, we propose an improved Low-Density Parity-Check (LDPC) code design scheme based on the existing genetic optimization-based LDPC code design scheme proposed in [1]. In particular, we perform the removal of the girth-4 property of the parity check matrix (H-matrix) and utilize the min-sum decoding algorithm instead of the Belief Propagation (BP) algorithm in order to enhance the performance of the LDPC code. Furthermore, an (32,64) LDPC code is considered in this paper. Finally, we evaluate the block error rate (BLER) of the LDPC code over white Gaussian noise channels. By means of evaluation results using Matlab, we indicate that our proposed approach can achieve a gain of more than 11% in terms of BLER compared to the existing schemes without significantly increasing the complexity of the decoding scheme.

## Effect of Pointing Errors on BER Performance of Multidimensional LDPC-Coded OAM Modulation with Direct Detection over Turbulent FSO Channels

- **ID**: ieee:10207427
- **Type**: conference
- **Published**: 2-6 July 2
- **Authors**: Goran T. Djordjevic, Ivan B. Djordjevic
- **PDF**: https://ieeexplore.ieee.org/document/10207427
- **Abstract**: In this invited paper, we study orbital angular momentum (OAM) - based signal transmission over free-space optical (FSO) link. After low-density parity-check (LDPC) encoding and multidimensional mapping, intensity modulation is implemented, and OAM multiplexing is performed. Signal is transmitted over FSO channel with atmospheric turbulence, pointing errors, and atmospheric loss. At the receiver end, signal is firstly demultiplexed by OAM demultiplexer, detected by photodiode, and further decoded by applying the multidimensional posterior-probability demapper and LDPC decoder. The bit-error rate (BER) performances are estimated by Monte Carlo simulations. The numerical results show that even when there is a strong misalignment between transmitter and receiver apertures, BER of the system can be reduced by applying appropriate quasi-cyclic LDPC codes. We show that BER values under 10-6 can be achieved for some typical values of electrical energy per information bit - to - noise spectral density ratio even when turbulence is strong.

## Impact of Non-Gaussian Noise Distribution by Artificial Neural Network-based Equalizers

- **ID**: ieee:10209616
- **Type**: conference
- **Published**: 2-6 July 2
- **Authors**: Weiqi Lu, Zexu Liu, Lei Liu +3
- **PDF**: https://ieeexplore.ieee.org/document/10209616
- **Abstract**: The non-Gaussian noise distribution by an artificial neural network (ANN) equalizer causes degradation to LDPC performance. Accurate estimation of LLR based on non-Gaussian noise distribution can improve receiver sensitivity by about 0.7 dB.

## Multi-dimensional reconciliation encoder with quasi-cyclic LDPC codes on FPGA

- **ID**: ieee:10207471
- **Type**: conference
- **Published**: 2-6 July 2
- **Authors**: M. Origlia, N. Andriolli, L. Maggiani +5
- **PDF**: https://ieeexplore.ieee.org/document/10207471
- **Abstract**: Information reconciliation (IR) is an integral part of classical data post-processing in quantum key distribution (QKD) and often constitutes a performance bottleneck. Due to the low signal-to-noise ratio, continuous-variable QKD systems require a IR scheme, such as multi-dimensional reconciliation (MDR), which is particularly computationally intensive.In this work we present the hardware architecture of an MDR encoder employing Quasi-Cyclic Low Density Parity Check (QC-LDPC) codes. We estimate the required number of flip-flops and the latency of its FPGA implementation. Finally, we investigate the computational bottlenecks and identify solutions to improve the scalability of the proposed implementation.

## Experimental Demonstration of Neural Network-based Soft Demapper for Long-haul Optical Transmission

- **ID**: ieee:10209891
- **Type**: conference
- **Published**: 2-6 July 2
- **Authors**: Wenkai Fang, Bin Chen, Yi Lei +7
- **PDF**: https://ieeexplore.ieee.org/document/10209891
- **Abstract**: Experimental validation for a proposed neural network-based soft demapper is demonstrated. A reach increase of 9.8% and a demapping complexity reduction of 28.6% for PM-64QAM with 11$\times$ 450Gbps DWDM is achieved over the conventional demapper.

## Probabilistic Shaping over Multi-Dimensional Constellations for Optical Fiber Transmissions: Trade-offs and Insights

- **ID**: ieee:10209722
- **Type**: conference
- **Published**: 2-6 July 2
- **Authors**: Jingtian Liu, Élie Awwad, Yves Jaouën
- **PDF**: https://ieeexplore.ieee.org/document/10209722
- **Abstract**: In this work, we combine probabilistic constellation shaping (PCS) using a Maxwell Boltzmann distribution with multi-dimensional modulations with the purpose of increasing performance gains in both the linear and non-linear regimes of optical fiber transmission systems. We particularly study the case of polarization division multiplexed long-haul coherent systems. By applying set partitioning and energy constraints on four-dimensional (4D) modulations followed by probabilistic shaping, we give insights into constructing novel modulations with enhanced performance compared to conventional PCS constellations in which shaping is performed separately over each real dimension.

## FPGA based High Bandwidth LDPC using Channel Coding Technique

- **ID**: ieee:10212353
- **Type**: conference
- **Published**: 19-21 July
- **Authors**: S. Yuvaraj, P. Latha, E. Malarvizhi +1
- **PDF**: https://ieeexplore.ieee.org/document/10212353
- **Abstract**: Error-correcting codeword's using Low-Density Parity Check (LDPC) have been the subject of many studies in the communications field. Because of excellent error correction performance, low-complexity calculations, and appropriateness for parallel hardware design, this has also become typical digital modulation schemes in various protocols. Meanwhile, significant work has gone into creating LDPC decoders that can run on Field-Programmable Gate Array (FPGA) devices instead of Application-Specific Integrated Circuit (ASIC) systems due to their faster processing speeds and parallel processing capabilities. However, it is difficult to compare and even more difficult to implement the FPGA-based LDPC encoder solutions that are available in the open literature. A corrected signal decoding method with several design optimizations that lower the expenses of supporting several different codes The decoder's development findings show that it can achieve better bandwidth utilization than earlier flexible FPGA-based LDPC decoders while still meeting the requisite amount of extensibility and satisfactory error-correcting effectiveness.

## Channel Coding Challenges for Short and Moderate Block Lengths-based Applications

- **ID**: ieee:10206234
- **Type**: conference
- **Published**: 18-20 July
- **Authors**: Amr Tarek, Amr Abdelaziz, Hisham Al-Dahshan
- **PDF**: https://ieeexplore.ieee.org/document/10206234
- **Abstract**: Advanced channel coding schemes have recently gained much interest due to their capacity-approaching behavior, rendering them a vital choice for many applications in commercial systems such as satellite standards and cellular communications networks. Furthermore, the low-density parity-check (LDPC) codes have already been chosen for user data in 5G New Radio (NR) systems since they provide high throughput and efficient error-correcting capabilities. In contrast, Polar in 5G NR is used for control information with enhanced mobile broadband (eMBB) and broadcast channels (BCH) since they can introduce an efficient decoding performance for short block lengths. Furthermore, LDPC is used in broadband satellite applications (DVB-S2) and DVB-S2 extensions (DVB-S2X), where LDPC and BCH codes are serially concatenated. This paper examines and addresses the merits of Polar and LDPC codes and their ability to adhere to the stringent requirements of satellite communications and the Ultra-Reliable and Low-Latency Communication (URLLC) applications. Moreover, simulation is performed to evaluate the performance of the LDPC and Polar codes used in 5G’s eMBB for short and moderate block lengths. More specifically, the convergence behavior regarding the number of iterations (LDPC) and list size (polar) is studied. Additionally, the performance and computational complexity are evaluated with various Polar and LDPC decoding algorithms.

## Updating Not Just Payload but Payload and Extra Data Simultaneously in Real-Time IoT Networks

- **ID**: ieee:10226950
- **Type**: conference
- **Published**: 17-19 July
- **Authors**: Mangang Xie, Baozhen An, Changhao Song +3
- **PDF**: https://ieeexplore.ieee.org/document/10226950
- **Abstract**: A real-time Internet of Things (IoT) status update system is considered, where the IoT device needs to send not only the interested sensing information (payload) but also the controlling information (extra) to the destination for improving the quality of service. To simultaneously transmit these two types of information, a promising coding scheme, i.e., free-ride code, is utilized, in which the 5G low-density parity-check coded sensing sequence is superposed on randomly coded controlling sequence and is delivered to the destination without consuming additional bandwidth and power resources. The average age of information (AAoI) is evaluated for both two types of information. Numerical simulations indicate that the AAoI of extra can be reduced by free-ride codes without impairing the one of payload.

## A family of error correcting codes for automotive applications

- **ID**: ieee:10217205
- **Type**: conference
- **Published**: 17-19 July
- **Authors**: Massimo Battaglioni, Giovanni Cancellieri
- **PDF**: https://ieeexplore.ieee.org/document/10217205
- **Abstract**: In this paper we propose a class of error correcting codes for automotive applications. The main merits of the proposed codes are the low-complexity encoding and decoding circuits, and a fine rate adaptability. A special chip for encoding and decoding operations could be designed, with promising market perspectives.
