# IEEE Xplore — 2017-02


## LDPC Lattice Codes for Full-Duplex Relay Channels

- **Status**: ❌
- **Reason**: LDPC lattice 코드 릴레이 채널 응용, lattice shaping/decomposition으로 바이너리 LDPC ECC 이식 기법 없음
- **ID**: ieee:7782405
- **Type**: journal
- **Published**: Feb. 2017
- **Authors**: Hassan Khodaiemehr, Dariush Kiani, Mohammad-Reza Sadeghi
- **PDF**: https://ieeexplore.ieee.org/document/7782405
- **Abstract**: Low-density parity-check (LDPC) lattices were the first family of lattices to show efficient decoding in high dimensions. We consider a case of these lattices with one binary LDPC code as an underlying code. We employ encoding and decoding of the LDPC lattices in a cooperative transmission framework. We establish two efficient shaping based on hypercube and Voronoi shaping, to obtain LDPC lattice codes. Then, we propose the implementation of block Markov encoding for one-way and two-way relay networks using LDPC lattice codes. An efficient method is also required for decomposing full-rate codebook into lower rate codebooks. We apply different decomposition schemes for one-way and two-way relay channels, which are the altered versions of the decomposition methods of low density lattice code (LDLC) lattices. Due to the lower complexity of the decoding for LDPC lattices comparing with LDLCs, the complexity of our schemes is significantly lower than the ones proposed for LDLCs. The efficiency of the proposed schemes is presented using simulation results that indicate the outperforming behavior of LDLCs over LDPC lattice codes in the same dimensions. However, having lower decoding complexity enables us to increase the dimension of the lattice to compensate the existing gap between the performance of the LDPC lattice codes and the LDLCs.

## Practical Encoder and Decoder for Power Constrained QC LDPC-Lattice Codes

- **Status**: ❌
- **Reason**: QC LDPC-lattice 부호+nested lattice shaping, lattice/SP 알고리즘으로 바이너리 LDPC ECC 이식 기법 없음(LDA는 non-binary)
- **ID**: ieee:7762096
- **Type**: journal
- **Published**: Feb. 2017
- **Authors**: Hassan Khodaiemehr, Mohammad-Reza Sadeghi, Amin Sakzad
- **PDF**: https://ieeexplore.ieee.org/document/7762096
- **Abstract**: Low density parity check (LDPC) lattices were the first family of lattices equipped with iterative decoding algorithms. We introduce quasi-cyclic LDPC (QC LDPC) lattices as a special case of LDPC lattices with one binary QC-LDPC code as their underlying code. These lattices are obtained from the Construction A of lattices providing us to encode them efficiently using shift registers. To benefit from an encoder with linear complexity in the lattice dimension, we obtain the generator matrix of these lattices in quasi-cyclic form. We generalize the proposed quasi-cyclic form of the generator matrix for other Construction A lattices, namely the LDA lattices, with a non-binary QC-LDPC code as their underlying code. We provide a low-complexity decoding algorithm of QC LDPC-lattices based on the sum product algorithm. To design lattice codes, QC LDPC-lattices are combined with the nested lattice shaping that uses the Voronoi region of a sublattice for shaping. The shaping gain and the shaping loss of our lattice codes with dimensions 40, 50, and 60 using an optimal quantizer, are presented. The guidelines for applying efficient shaping methods, like hypercube shaping, for QC LDPC-lattices are also given. Consequently, we establish a family of lattice codes that perform practically close to the sphere bound.

## Improved Hard-Reliability Based Majority-Logic Decoding for Non-Binary LDPC Codes

- **Status**: ❌
- **Reason**: non-binary LDPC majority-logic 디코딩 - 비이진 제외
- **ID**: ieee:7728036
- **Type**: journal
- **Published**: Feb. 2017
- **Authors**: Saedong Yeo, In-Cheol Park
- **PDF**: https://ieeexplore.ieee.org/document/7728036
- **Abstract**: This letter proposes two methods to improve the iterative hard-reliability based majority-logic decoding algorithm for non-binary low-density parity-check (NB-LDPC) codes. The first method improves the error-correcting performance by modifying the initialization process, which is based on the fact that Gray coded modulation is used in general. In addition, a storage reduction method is proposed to make the proposed decoding hardware-friendly, which reduces the memory size considerably while sustaining the error-correcting performance achieved by the modified initialization. For an NB-LDPC code over Galois field of 32 elements, the memory size is reduced by about 75% compared with that of the conventional decoding algorithm.

## CRC Error Correction in IoT Applications

- **Status**: ❌
- **Reason**: CRC 부호 반복디코딩 IoT 적용 - 비-LDPC 부호, 떼어낼 LDPC BP 기법 없음
- **ID**: ieee:7558141
- **Type**: journal
- **Published**: Feb. 2017
- **Authors**: Evgeny Tsimbalo, Xenofon Fafoutis, Robert J. Piechocki
- **PDF**: https://ieeexplore.ieee.org/document/7558141
- **Abstract**: In this paper, error correction is introduced to the Bluetooth low energy and IEEE 802.15.4 standards by utilizing data redundancy provided by cyclic redundancy check (CRC) codes used by both protocols to detect erroneous packets. A scenario with an energy-constrained transmitter and a constraint-free infrastructure is assumed that enables additional signal processing at the receiving side, keeping the transmitter intact. CRC error correction is achieved using a novel approach of applying iterative decoding techniques. The proposed methods are evaluated based both on simulated and real packets. It is shown that by enabling CRC error correction, up to 2.5 dB of the signal to noise ratio gain can be achieved, while up to 35% of real corrupted packets can be corrected, at no extra cost for the transmitter. This results in potential range extension and longer battery life caused by a reduced number of retransmissions.

## A Novel Architecture for Elementary-Check-Node Processing in Nonbinary LDPC Decoders

- **Status**: ❌
- **Reason**: non-binary LDPC(GF(q)) elementary-check-node 아키텍처 - 비이진 제외
- **ID**: ieee:7448890
- **Type**: journal
- **Published**: Feb. 2017
- **Authors**: Oussama Abassi, Laura Conde-Canencia, Ali Al Ghouwayel +1
- **PDF**: https://ieeexplore.ieee.org/document/7448890
- **Abstract**: This brief presents an efficient architecture design for elementary-check-node processing in nonbinary low-density parity-check decoders based on the extended min-sum algorithm. This architecture relies on a simplified version of the bubble check algorithm and is implemented by the means of first-in-first-out. The adoption of this new design at the check node level results in a high-rate low-cost full-pipelined processor. A proof-of-concept implementation of this processor shows that the proposed architecture halves the occupied the field-programmable gate array (FPGA) surface and doubles the maximum frequency without modifying the input/output behavior of the previous one.

## On Frame Asynchronous Coded Slotted ALOHA: Asymptotic, Finite Length, and Delay Analysis

- **Status**: ❌
- **Reason**: coded slotted ALOHA 랜덤액세스 분석, LDPC는 분석도구일 뿐 떼어낼 ECC 디코더/구성 없음
- **ID**: ieee:7762138
- **Type**: journal
- **Published**: Feb. 2017
- **Authors**: Erik Sandgren, Alexandre Graell i Amat, Fredrik Brännström
- **PDF**: https://ieeexplore.ieee.org/document/7762138
- **Abstract**: We consider a frame asynchronous coded slotted ALOHA (FA-CSA) system for uncoordinated multiple access, where users join the system on a slot-by-slot basis according to a Poisson random process, and in contrast to standard frame synchronous CSA (FS-CSA), users are not frame-synchronized. We analyze the performance of FA-CSA in terms of packet loss rate and delay. In particular, we derive the (approximate) density evolution that characterizes the asymptotic performance of FA-CSA when the frame length goes to infinity. We show that, if the receiver can monitor the system before anyone starts transmitting, a boundary effect similar to that of spatially coupled codes occurs, which greatly improves the iterative decoding threshold. Furthermore, we derive tight approximations of the error floor (EF) for the finite frame length regime, based on the probability of occurrence of the most frequent stopping sets. We show that, in general, FA-CSA provides better performance in both the EF and waterfall regions as compared to FS-CSA. Moreover, FA-CSA exhibits better delay properties than FS-CSA.

## Broadcast Coded Slotted ALOHA: A Finite Frame Length Analysis

- **Status**: ❌
- **Reason**: coded slotted ALOHA MAC/erasure 분석 - 무선 응용 특이, 떼어낼 ECC 기법 없음
- **ID**: ieee:7736044
- **Type**: journal
- **Published**: Feb. 2017
- **Authors**: Mikhail Ivanov, Fredrik Brännström, Alexandre Graell i Amat +1
- **PDF**: https://ieeexplore.ieee.org/document/7736044
- **Abstract**: We propose an uncoordinated medium access control (MAC) protocol, called all-to-all broadcast coded slotted ALOHA (B-CSA) for reliable all-to-all broadcast with strict latency constraints. In B-CSA, each user acts as both transmitter and receiver in a half-duplex mode. The half-duplex mode gives rise to a double unequal error protection (DUEP) phenomenon: the more a user repeats its packet, the higher the probability that this packet is decoded by other users, but the lower the probability for this user to decode packets from others. We analyze the performance of B-CSA over the packet erasure channel for a finite frame length. In particular, we provide a general analysis of stopping sets for B-CSA and derive an analytical approximation of the performance in the error floor (EF) region, which captures the DUEP feature of B-CSA. Simulation results reveal that the proposed approximation predicts very well the performance of B-CSA in the EF region. Finally, we consider the application of B-CSA to vehicular communications and compare its performance with that of carrier sense multiple access (CSMA), the current MAC protocol in vehicular networks. The results show that B-CSA is able to support a much larger number of users than CSMA with the same reliability.

## Achieving Secrecy Capacity of the Wiretap Channel and Broadcast Channel With a Confidential Component

- **Status**: ❌
- **Reason**: polar code 기반 wiretap 보안 용량 달성, 보안+비-LDPC 부호, 떼어낼 LDPC BP 기법 없음
- **ID**: ieee:7750596
- **Type**: journal
- **Published**: Feb. 2017
- **Authors**: Talha Cihad Gulcu, Alexander Barg
- **PDF**: https://ieeexplore.ieee.org/document/7750596
- **Abstract**: The wiretap channel model of Wyner is one of the first communication models with both reliability and security constraints. Capacity-achieving schemes for various models of the wiretap channel have received considerable attention in recent literature. In this paper, we show that capacity of the general (not necessarily degraded or symmetric) wiretap channel under a “strong secrecy constraint” can be achieved using a transmission scheme based on polar codes. We also extend our construction to the case of broadcast channels with confidential messages defined by Csiszár and Körner, achieving the entire capacity region of this communication model.

## Multiuser Detection in Multibeam Satellite Systems: Theoretical Analysis and Practical Schemes

- **Status**: ❌
- **Reason**: 다중빔 위성 multiuser detection+DVB-S2 코드 재설계, 통신 응용 특이적이고 떼어낼 LDPC 기법 없음
- **ID**: ieee:7782367
- **Type**: journal
- **Published**: Feb. 2017
- **Authors**: Giulio Colavolpe, Andrea Modenini, Amina Piemontese +1
- **PDF**: https://ieeexplore.ieee.org/document/7782367
- **Abstract**: We consider the rates achievable by a user in a multibeam satellite system for unicast applications and propose alternatives to the conventional single-user symbol-by-symbol detection applied at user terminals. Single-user detection is known to suffer from strong degradation when the terminal is located near the edge of the coverage area of a beam and when aggressive frequency reuse is adopted. For this reason, we consider multiuser detection and take into account the strongest interfering signal. We also analyze two additional transmission strategies requiring modifications at medium access control layer. We describe an information-theoretic framework to compare the different strategies by computing the information rate of the user in the reference beam. Furthermore, we analyze the performance of coded schemes that could approach the information-theoretic limits. We show that classical codes from the DVB-S2(X) standard are not suitable when multiuser detection is adopted and we propose two ways to improve the performance based on the redesign of the code and of the bit mapping.

## Product Codes for Data Storage on Magnetic Tape

- **Status**: ❌
- **Reason**: 테이프 스토리지용 product code(비-LDPC), 떼어낼 LDPC BP 기법 없음
- **ID**: ieee:7577779
- **Type**: journal
- **Published**: Feb. 2017
- **Authors**: Roy D. Cideciyan, Simeon Furrer, Mark A. Lantz
- **PDF**: https://ieeexplore.ieee.org/document/7577779
- **Abstract**: For 2-D product codes used in tape storage, the mapping of error-correction-coding (ECC) blocks (EBs) into 2-D physical blocks (PBs) on magnetic tape is generalized. The 3-D product codes that have the same code rate and EB size as interleaved 2-D product codes currently used in tape storage are proposed. For 3-D product codes, a new family of mappings of EBs into 2-D PBs on magnetic tape is introduced, which fulfills the stringent burst-error-correction requirements of tape storage. The burst-error-correction capability of 2-D and 3-D product code words recorded on magnetic tape is analyzed as a function of track rotation, linear density, and ECC parameters. The performance limits of the tape-storage channel are determined based on computations of channel capacity and random coding bound. Hardware simulations of iterative hard-decision decoding of product codes implemented in a field-programmable gate array demonstrate the improved error-rate performance of 3-D product codes over 2-D product codes.

## Multi-Party Secret Key Agreement Over State-Dependent Wireless Broadcast Channels

- **Status**: ❌
- **Reason**: 무선 브로드캐스트 채널 비밀키 합의(보안), 떼어낼 LDPC ECC 기법 없음
- **ID**: ieee:7574374
- **Type**: journal
- **Published**: Feb. 2017
- **Authors**: Mahdi Jafari Siavoshani, Shaunak Mishra, Christina Fragouli +1
- **PDF**: https://ieeexplore.ieee.org/document/7574374
- **Abstract**: We consider a group of m trusted and authenticated nodes that aim to create a shared secret key K over a wireless channel in the presence of an eavesdropper Eve. We assume that there exists a state-dependent wireless broadcast channel from one of the honest nodes to the rest of them including Eve. All of the trusted nodes can also discuss over a cost-free, noiseless and unlimited rate public channel which is also overheard by Eve. For this setup, we develop an information-theoretically secure secret key agreement protocol. We show the optimality of this protocol for “linear deterministic” wireless broadcast channels. This model generalizes the packet erasure model studied in the literature for wireless broadcast channels. Here, the main idea is to convert a deterministic channel into multiple independent erasure channels by using superposition coding. For “state-dependent Gaussian” wireless broadcast channels, by using insights from the deterministic problem, we propose an achievability scheme based on a multi-layer wiretap code. By using the wiretap code, we can mimic the phenomenon of converting the wireless channel into multiple independent erasure channels. Then, finding the best achievable secret key generation rate leads to solving a non-convex power allocation problem over these channels (layers). We show that using a dynamic programming algorithm, one can obtain the best power allocation for this problem. Moreover, we prove the optimality of the proposed achievability scheme for the regime of high-SNR and large-dynamic range over the channel states in the (generalized) degrees of freedom sense.

## Coded Pulse-Amplitude-Modulation for Intensity- Modulated Optical Communications

- **Status**: ❌
- **Reason**: q-ary(비이진) Polar 부호 광통신 코드변조. 비이진+비-LDPC, 제외
- **ID**: ieee:7938058
- **Type**: conference
- **Published**: 6-9 Feb. 2
- **Authors**: Zifeng Wu, Berthold Lankl
- **PDF**: https://ieeexplore.ieee.org/document/7938058
- **Abstract**: In this paper, we study the optimization of M-ary pulse-amplitude modulation (PAM) in the context of a coded modulation scheme for intensity-modulated optical communications. Building on previous approaches in literature, we propose to employ q-ary codes, in particular q-ary Polar codes, to achieve simplified mapping and a high degree of flexibility at low to moderate complexity. We focus on information-theoretic aspects and verify the performance of our coded modulation scheme using numerical simulations.

## A New Error Correction Scheme for Physical Unclonable Functions

- **Status**: ❌
- **Reason**: PUF 보안용 ECC, LDPC 사용하나 보안+helper data 없는 개별코드 구성. 보안 도메인, 떼어낼 일반 LDPC 기법 없음
- **ID**: ieee:7938055
- **Type**: conference
- **Published**: 6-9 Feb. 2
- **Authors**: Sven Mueelich, Martin Bossert
- **PDF**: https://ieeexplore.ieee.org/document/7938055
- **Abstract**: Error correction is an indispensable component when Physical Unclonable Functions (PUFs) are used in cryptographic applications. So far, there exist schemes that obtain helper data, which they need within the error correction process. We introduce a new scheme, which only uses an error correcting code without any further helper data. The main idea is to construct for each PUF instance an individual code which contains the initial PUF response as codeword. In this work we use LDPC codes, however other code classes are also possible. Our scheme allows a trade-off between code rate and cryptographic security. In addition, decoding with linear complexity is possible.

## On the Performance of Short Tail-Biting Convolutional Codes for Ultra-Reliable Communications

- **Status**: ❌
- **Reason**: tail-biting convolutional codes(비-LDPC) 성능분석+Viterbi 디코딩, 바이너리 LDPC BP에 이식할 기법 없음
- **ID**: ieee:7938068
- **Type**: conference
- **Published**: 6-9 Feb. 2
- **Authors**: Lorenzo Gaudio, Tudor Ninacs, Thomas Jerkovits +1
- **PDF**: https://ieeexplore.ieee.org/document/7938068
- **Abstract**: Motivated by the increasing interest in powerful short channel codes for low-latency ultra-reliable communications, we analyze the performance of tail-biting convolutional codes with different memories, block lengths and code rates over the additive white Gaussian noise channel. The analysis is carried out both through Monte Carlo simulations and by upper bounding the error probability via Poltyrev's tangential sphere bound at very low error rates. For the simulations, the near maximum likelihood wrap-around Viterbi algorithm is considered. We then compare the performance of tail-biting convolutional codes both with finite-length performance bounds and with that of other channel codes that have been recently considered for ultra-reliable satellite telecommand links. For the shortest block lengths, tail-biting convolutional codes outperform significantly state-of-the-art iterative coding schemes, while as expected their performance degrades visibly with increasing block lengths.

## Multi-track Recording Systems Using Non-binary Error Correction Coding Schemes for Bit-patterned Magnetic Recording

- **Status**: ❌
- **Reason**: BPMR용 non-binary 부호+2D 신호처리/MAP 검출, 비이진+자기기록 특이적이라 제외
- **ID**: ieee:7938081
- **Type**: conference
- **Published**: 6-9 Feb. 2
- **Authors**: Hidetoshi Saito
- **PDF**: https://ieeexplore.ieee.org/document/7938081
- **Abstract**: In this paper, a new multi-track recording system based on two-dimensional (2D) signal processing schemes is proposed for bit-patterned magnetic recording (BPMR). This system uses a non-binary error-correcting code and a modulation code with 2D run-length limited constraints. The signal processing scheme in the proposed system gets mixed readback signal sequences from the parallel adjacent tracks using a single reading head simultaneously. These readback signal sequences are equalized to a frequency response given by a desired 2D generalized partial response (GPR) system for BPMR. In decoding, a single sequence detector using maximum a posteriori (MAP) estimation combined with pattern-dependent noise-predictive detection is able to detect the equalized GPR signal sequences for recorded data written in a group of parallel adjacent tracks. Using computer simulation, this decoding scheme improves the signalto- noise ratio compared to the conventional MAP detection under media noise.

## Comparison of Geometric and Probabilistic Shaping with Application to ATSC 3.0

- **Status**: ❌
- **Reason**: geometric/probabilistic shaping 비교(ATSC 3.0), 변조 정형화 주제. LDPC 디코더/구성 기여 없음
- **ID**: ieee:7937997
- **Type**: conference
- **Published**: 6-9 Feb. 2
- **Authors**: Fabian Steiner, Georg Boecherer
- **PDF**: https://ieeexplore.ieee.org/document/7937997
- **Abstract**: In this work, geometric shaping (GS) and probabilistic shaping (PS) for the additive white Gaussian noise (AWGN) channel is reviewed. Both approaches are investigated in terms of symbol-metric decoding (SMD) and bit-metric decoding (BMD). For GS, an optimization algorithm based on differential evolution is formulated. Achievable rate analysis reveals that GS suffers from a 0.4 dB signal-to-noise ratio (SNR) performance degradation compared to PS when BMD is used. Forward-error correction simulations of the ATSC 3.0 modulation and coding formats (modcods) confirm the theoretical findings. In particular, PS enables seamless rate adaptation with one modcod and it outperforms ATSC 3.0 GS modcods by more than 0.5 dB for spectral efficiencies larger than 3.2 bits per channel use.

## Approximate Image Authentication and Correction using Spatial and Frequency Domain Features

- **Status**: ❌
- **Reason**: 이미지 인증/워터마킹+RS 코드, 채널 ECC 아님. 떼어낼 LDPC 기법 없음
- **ID**: ieee:7938051
- **Type**: conference
- **Published**: 6-9 Feb. 2
- **Authors**: Obaid Ur-Rehman, Natasa Zivic, Christoph Ruland
- **PDF**: https://ieeexplore.ieee.org/document/7938051
- **Abstract**: Images traversing from source to sink can undergo intentional and unintentional modifications. An image authentication scheme is presented in this paper which is capable of detecting modifications in the image, locating their positions and correcting some or all of them. It is also able to tolerate minor unintentional modifications. However, intentional forgeries are detected by the proposed scheme. The idea is to build a watermark using local frequency domain image features and protecting them with Reed Solomon codes. This helps in the localization of modifications and their correction to the extent possible with the used code. At the same time, the global image histogram features are protected using an approximate message authentication code. This provides tolerance in authentication in the presence of unintentional modifications such as channel noise, image transformation operations, compression etc. Security strength of the proposed image authentication scheme is analyzed in the paper. Simulation results in the presence of unintentional modifications show the noise tolerant authentication capability, whereas simulation results in the presence of intentional modifications demonstrate the forgery detection capability of the proposed scheme.

## Flexible Length Polar Codes through Graph Based Augmentation

- **Status**: ❌
- **Reason**: Polar 부호 유연 길이(graph augmentation), 비-LDPC. BP는 polar 전용이라 LDPC 이식 기법 없음
- **ID**: ieee:7938067
- **Type**: conference
- **Published**: 6-9 Feb. 2
- **Authors**: A. Elkelesh, M. Ebada, S. Cammerer +1
- **PDF**: https://ieeexplore.ieee.org/document/7938067
- **Abstract**: The structure of polar codes inherently requires block lengths to be powers of two. In this paper, we investigate how different block lengths can be realized by coupling of several short-length polar codes. For this, we first analyze "code augmentation" to better protect the semipolarized channels, improving the BER performance under belief propagation decoding. Several serial and parallel augmentation schemes are discussed. A coding gain of 0:3 dB at a BER of 10(exp -5) can be observed for the same total rate and length. Further, we extend this approach towards coupling of several "sub-polar codes", leading to a reduced computational complexity and enabling the construction of flexible length polar codes.

## Algorithms for the Iterative Estimation of Discrete-Valued Sparse Vectors

- **Status**: ❌
- **Reason**: 압축센싱 이산값 희소벡터 추정, 채널코딩 ECC 아님(소스/추정)
- **ID**: ieee:7938053
- **Type**: conference
- **Published**: 6-9 Feb. 2
- **Authors**: Susanne Sparrer, Robert F. H. Fischer
- **PDF**: https://ieeexplore.ieee.org/document/7938053
- **Abstract**: In Compressed Sensing, a real-valued sparse vector has to be estimated from an underdetermined system of linear equations. In many applications, however, the elements of the sparse vector are drawn from a finite set. For the estimation of these discrete-valued vectors, matched algorithms are required which take the additional knowledge of the discrete nature into account. In this paper, the estimation problem is treated from a communications engineering point of view. A powerful new algorithm incorporating techniques known from digital communications and information theory is derived. For comparison, Turbo Compressed Sensing is adapted to the discrete setup and a simplified and generalized notation is presented. The performance of the algorithms is covered by numerical simulations.

## Combining LDPC codes, M-QAM modulations, and IFDMA multiple-access to achieve 5G requirements

- **Status**: ❌
- **Reason**: 표준 LDPC를 M-QAM/IFDMA와 결합한 5G 무선 응용, 떼어낼 ECC 기법 없음
- **ID**: ieee:7891828
- **Type**: conference
- **Published**: 22-24 Feb.
- **Authors**: Andrés Leonardo Ortega-Ortega, Jack Fernando Bravo-Torres
- **PDF**: https://ieeexplore.ieee.org/document/7891828
- **Abstract**: In this paper we explore the advantage of combining M-QAM modulations, LDPC codes, and IFDMA multi-access techniques in order to increase the capacity of the system, reduce the peak-to-average power ratio (PAPR) and to improve the BER performance. The simulation results show that our proposal provides better performance, even allowing significant reductions, of about 1 dB, in the PARP of the high-level modulation schemes, such as 64-QAM. In addition, the spectral efficiency and BER, using LDPC codes (FEC), provides a considerable advantage and low complexity respect to traditional systems.

## [Table of contents]

- **Status**: ❌
- **Reason**: 학술대회 목차로 논문 내용 없음
- **ID**: ieee:7891807
- **Type**: conference
- **Published**: 22-24 Feb.
- **Authors**: 
- **PDF**: https://ieeexplore.ieee.org/document/7891807
- **Abstract**: The following topics are dealt with: Atila; UIDP-based educational application generator; mobile devices; epileptic seizure detection; optical and electrical recordings; analytical workspace delineation; translational underconstrained cable-based robot; switching position-force controller; two independent finger gripper; Horn & Schunck parameter characterization; gradient based method; optical flow computing; longest classical EM waves; communications carriers; sensor fusion; serious game; children nutrition education; pupillary response; spiking neural network; latent semantic analysis; Syslog correlation; liquid level system; fuzzy control; visual odometry; trilateration method; stereo images; zone based hybrid approach; wireless sensor networks; falling people detection; autonomous service robots: ROS module integration approach; diabetes; pneumatic manipulator robot; back propagation neural network; capacitive touch interfaces; depth-first search satisfiability; mu-calculus; trees; LDPC codes; M-QAM modulations; IFDMA; 5G requirements; super-resolution methods; digital mammograms: multiscale iterative resolution; wavelet transform; cosine transform; wavelet family iterative scales; direct local search operators impact; memetic differential evolution; constrained numerical optimization problems; Mexican sign language recognition; Kinect; data time warping algorithm; object recognition modular system implementation; service robotics context; feature selection; botnets detection; machine learning algorithms; mosquito larva classification method; convolutional neural networks; LOD4AIR; linked open data and OAI-PMH repositories.

## Connectivity analysis of an AUV network with OFDM based communications

- **Status**: ❌
- **Reason**: AUV 수중 OFDM 네트워크 연결성 분석, LDPC는 부수 사용 — 떼어낼 기법 없음
- **ID**: ieee:7890334
- **Type**: conference
- **Published**: 21-24 Feb.
- **Authors**: Alper Bereketli, Muharrem Tumcakir, Ilkay Yazgi +3
- **PDF**: https://ieeexplore.ieee.org/document/7890334
- **Abstract**: Autonomous underwater vehicle (AUV) networks play a crucial role in tactical, commercial, and scientific applications, where reliable and robust communication protocols are needed due to the challenging characteristics of the channel. With this motivation, connectivity of AUV networks in different regions with varying transducer characteristics are analyzed through simulations based on real-life orthogonal frequency division multiplexing (OFDM) based communication experiments over noisy and Doppler-distorted channels. Doppler compensation is performed according to the autocorrelation using the cyclic prefix. Using binary and quadrature phase shift keying (BPSK and QPSK) modulation schemes in conjunction with low density parity check (LDPC) coding, error rate levels are investigated through shallow water pond and at-sea experiments. It is shown that, the utilized transmission scheme is capable of correcting all bit errors among nearly one million bits transmitted up to a distance of 1 km, yielding a payload rate of 15.6 kbps with 4096 subcarriers and QPSK modulation. The simulations provide key parameters that must be taken into account in the design of scalable and connected AUV networks.

## New code based identification scheme

- **Status**: ❌
- **Reason**: MDPC 기반 코드기반 신원확인(보안 프로토콜), 채널 ECC 디코더/구성 기여 없음
- **ID**: ieee:7889187
- **Type**: conference
- **Published**: 20-22 Feb.
- **Authors**: Hamza Moufek, Kenza Guenda
- **PDF**: https://ieeexplore.ieee.org/document/7889187
- **Abstract**: In this paper, we propose a new identification scheme, based on two hard problems: the syndrome decoding problem and the problem of finding the parity-check matrix from the generator matrix of an MDPC-code. Our scheme is zero-knowledge and it has a short key compared to other protocols.

## LDPC convolutional codes coded cooperation based on puncturing

- **Status**: ❌
- **Reason**: LDPC convolutional+puncturing의 5G coded cooperation 응용, MIMO/diversity 통신 특이적이고 떼어낼 신규 디코더·구성 기법 없음
- **ID**: ieee:7890141
- **Type**: conference
- **Published**: 19-22 Feb.
- **Authors**: Wenhe Jin, Shaohua Wu, Erpeng Yang +1
- **PDF**: https://ieeexplore.ieee.org/document/7890141
- **Abstract**: Coded cooperation is a kind of virtual MIMO transmission technology that can achieve both coding gain and diversity gain, which is very promising in 5G communication. To design a scheme that can be used for near-capacity transmission and can be generalized for slow and fast fading channels, this paper studies the coding cooperation based on convolutional LDPC codes. Firstly, channel coding the original information by LDPC convolutional codes, then divided the coded words into two parts by puncturing algorithm; secondly, introducing space-time transmission into the second frame of coded cooperation, so the diversity gain can be obtained under different fading scenarios. Simulation results show that the system performance can be improved generally.

## Performance of PLC synchronization for DOCSIS 3.1 receiver

- **Status**: ❌
- **Reason**: DOCSIS 3.1 PLC OFDM 동기화 기법, LDPC는 부수 언급뿐 떼어낼 ECC 기법 없음
- **ID**: ieee:7890166
- **Type**: conference
- **Published**: 19-22 Feb.
- **Authors**: Jaeho Lee, Younok Park, Seungchan Bang
- **PDF**: https://ieeexplore.ieee.org/document/7890166
- **Abstract**: A Physical layer link channel (PLC) is a narrowband signaling channel located within the downstream OFDM channel used in data-over-service-interface specifications (DOCSIS) 3.1 system. It consists of a PLC preamble and PLC data which include information about a low density parity check (LDPC) coding rate, QAM order and interleaver depth etc. PLC preamble has +1 or −1 for PLC synchronization. In this paper, a novel method of PLC synchronization in frequency domain is proposed to demodulate a received orthogonal frequency division multiplexing (OFDM) signal correctly.

## Integrated code design for a joint source and channel LDPC coding scheme

- **Status**: ❌
- **Reason**: JSCC(소스-채널 결합) LDPC 코드 설계 — 떼어낼 순수 채널 ECC 기법 없음, 기준상 JSCC 원칙 제외
- **ID**: ieee:8023458
- **Type**: conference
- **Published**: 12-17 Feb.
- **Authors**: Hsien-Ping Lin, Shu Lin, Khaled Abdel-Ghaffar
- **PDF**: https://ieeexplore.ieee.org/document/8023458
- **Abstract**: This paper presents a design of LDPC codes for a joint source-channel (JSC) coding system. In the construction of such an LDPC code, the source compression matrix and the channel code parity-check matrix are designed jointly. The integrated matrix is used for both JSC encoding and decoding. Experimental results show that the codes constructed not only perform well in the waterfall region but also achieve low error-floors.

## Correcting errors by natural redundancy

- **Status**: ❌
- **Reason**: 압축데이터의 natural redundancy 활용 소스코딩+채널코딩 결합, 떼어낼 LDPC ECC 기법 없음
- **ID**: ieee:8023455
- **Type**: conference
- **Published**: 12-17 Feb.
- **Authors**: Anxiao Jiang, Pulakesh Upadhyaya, Erich F. Haratsch +1
- **PDF**: https://ieeexplore.ieee.org/document/8023455
- **Abstract**: For the storage of big data, there are significant challenges with its long-term reliability. This paper studies how to use the natural redundancy in data for error correction, and how to combine it with error-correcting codes to effectively improve data reliability. It explores several aspects of natural redundancy, including the discovery of natural redundancy in compressed data, the efficient decoding of codes with random structures, the capacity of error-correcting codes that contain natural redundancy, and the time-complexity tradeoff between source coding and channel coding.

## Using QAM-9 and ternary noise-immune codes to approach the Shannon bound

- **Status**: ❌
- **Reason**: QAM-9+삼진 부호 변조/코딩 방식, 비이진·비-LDPC이며 이식 기법 없음.
- **ID**: ieee:7910520
- **Type**: conference
- **Published**: 1-3 Feb. 2
- **Authors**: Vitaly Kuznetsov, Vladimir Batura, Alexey Solodkov +1
- **PDF**: https://ieeexplore.ieee.org/document/7910520
- **Abstract**: Analysis of experimental results of the binary noise-immune coding with one-dimensional modulation best achievements points out the impossibility of achievement the continuous Gaussian channel parameters of such scheme in practice. In the paper is exhibited that changeover to more effective two-dimensional non-binary PAM modulation with ternary noise-immune codes in each quadrature branch of a modem allows to work with high enough reliability and to reach frequency-energetical system parameters that are equal to analogous parameters of continuous channel with AWGN. Symbol error probability Qs=10-4 for Eb/N0=4.963 and total spectral efficiency 4.036 bit/s/Hz have achieved for best modulation and coding scheme from proposed set.

## Error probability bounds for SCMA signals

- **Status**: ❌
- **Reason**: SCMA 오류확률 bound 분석, LDPC 부호 아니고 떼어낼 디코더·구성 기법 없음.
- **ID**: ieee:7910519
- **Type**: conference
- **Published**: 1-3 Feb. 2
- **Authors**: Vyacheslav P. Klimentyev, Alexander B. Sergienko
- **PDF**: https://ieeexplore.ieee.org/document/7910519
- **Abstract**: In this paper, we investigated error probability bounds for sparse code multiple access (SCMA) signals. SCMA is one of proposed non-orthogonal multiple access schemes for Fifth generation (5G) wireless communication standard. This scheme allows to increase the number of active users inside a given time-frequency resource. For AWGN and Rayleigh (without diversity) channels, we calculated union bounds for symbol and bit error probability. Asymptotic bound based on minimal distance between signals is also calculated. Analytical bounds are compared with simulations results (Maximum Likelihood (ML) Algorithm and Message Passing Algorithm (MPA) were used for signal reception). For AWGN channel, the results show that analytical bounds (symbol and bit error probabilities) are tight in the high-SNR region. For Rayleigh channel, analytical bound for symbol error probability are pessimistic with the gap of approximately 0.7 dB in the medium- and high-SNR regions.

## Soft Hint Enabled Adaptive Visible Light Communication over Screen-Camera Links

- **Status**: ❌
- **Reason**: VLC screen-camera용 rateless/erasure 코딩 응용, LDPC ECC로 떼어낼 디코더/구성 기법 없음
- **ID**: ieee:7448931
- **Type**: journal
- **Published**: 1 Feb. 201
- **Authors**: Wan Du, Jansen Christian Liando, Mo Li
- **PDF**: https://ieeexplore.ieee.org/document/7448931
- **Abstract**: Screen-camera links for Visible Light Communication (VLC) are diverse, as the link quality varies according to many factors, such as ambient light and camera's performance. This paper presents SoftLight, a channel coding approach that considers the unique channel characteristics of VLC links and automatically adapts the transmission data rate to the link qualities of various scenarios. SoftLight incorporates two new ideas: (1) an expanded color modulation interface that provides soft hint about its confidence in each demodulated bit and establishes a bit-level VLC erasure channel, and (2) a rateless coding scheme that achieves bit-level rateless transmissions with low computation complexity and tolerates the false positive of bits provided by the soft hint enabled erasure channel. SoftLight is orthogonal to the visual coding schemes and can be applied atop any barcode layouts. We implement SoftLight on Android smartphones and evaluate its performance under a variety of environments. The experiment results show that SoftLight can correctly transmit a 22-KByte photo between two smartphones within 0.6 second and improves the average goodput of the state-of-the-art screen-camera VLC solution by 2.2×.
