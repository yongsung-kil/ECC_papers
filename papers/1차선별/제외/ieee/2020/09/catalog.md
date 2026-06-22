# IEEE Xplore — 2020-09


## Code Design for Run-Length Control in Visible Light Communication

- **Status**: ❌
- **Reason**: VLC용 RLL(run-length limited) 부호 설계; LDPC ECC 디코더/구성 기법 아님, 떼어낼 ECC 기여 없음
- **ID**: ieee:11291610
- **Type**: journal
- **Published**: September 
- **Authors**: Zong-yan Li, Hong-lu Yu, Bao-ling Shan +2
- **PDF**: https://ieeexplore.ieee.org/document/11291610
- **Abstract**: Run-length limited (RLL) codes can facilitate reliable data transmission and provide flicker-free illumination in visible light communication (VLC) systems. We propose novel high-rate RLL codes, which can improve error performance and mitigate flicker. Two RLL coding schemes are developed by designing the finite-state machine to further enhance the coding gain by improving the minimum Hamming distance and using the state-splitting method to realize small state numbers. In our RLL code design, the construction of the codeword set is critical. This codeword set is designed considering the set-partitioning algorithm criterion. The flicker control and minimum Hamming distance of the various proposed RLL codes are described in detail, and the flicker performances of different codes are compared based on histograms. Simulations are conducted to evaluate the proposed RLL codes in on-off keying modulation VLC systems. Simulation results demonstrate that the proposed RLL codes achieve superior error performance to the existing RLL codes.

## Joint Component Design for the JSCC System Based on DP-LDPC Codes

- **Status**: ❌
- **Reason**: DP-LDPC 기반 JSCC 결합소스채널코딩 — 소스-채널 결합은 ECC 아님, 명시적 제외 대상
- **ID**: ieee:9115063
- **Type**: journal
- **Published**: Sept. 2020
- **Authors**: Sanya Liu, Lin Wang, Jun Chen +1
- **PDF**: https://ieeexplore.ieee.org/document/9115063
- **Abstract**: The joint base matrix BJ of the joint source-channel coding (JSCC) system based on double protograph low-density parity-check (DP-LDPC) codes consists of four components, namely, the source code Bs, the channel code Bc, the type1 connection edge BL1 and the type-2 connection edge BL2, each having a non-negligible influence on the system performance. Different from the traditional component-specific design approach, we propose a joint design and optimization algorithm based on the idea of multi-objective differential evolution (MODE). Specifically, we consider the optimization of the DP-LDPC JSCC system through joint design of three components Bs, Bc, BL1 and all four components Bs, Bc, BL1, BL2, respectively. The proposed algorithm has low search complexity due to the reduction in size and element value of base matrices. The joint protograph extrinsic information transfer (JPEXIT) analyses and the simulation results demonstrate that the resulting JSCC system is free from a high error floor, requires fewer number of iterations for reaching the same bit error rate (BER) and achieves significant coding gains as compared to the state-of-the-art. Our DP-LDPC JSCC system is also shown to outperform its separation-based counterpart by a wide margin.

## A Scheme for Collective Encoding and Iterative Soft-Decision Decoding of Cyclic Codes of Prime Lengths: Applications to Reed–Solomon, BCH, and Quadratic Residue Codes

- **Status**: ❌
- **Reason**: 순환부호(RS/BCH/QR)를 Galois Fourier 변환으로 바이너리 LDPC 행렬화해 반복 연판정 복호; GF(q) 비이진 기반 변환 의존이라 NAND 바이너리 LDPC 이식성 불명확하나 도메인이 코드/디코더라 애매-> 살펴보면 비이진 RS/BCH 대상이라 제외
- **ID**: ieee:9025269
- **Type**: journal
- **Published**: Sept. 2020
- **Authors**: Shu Lin, Khaled Abdel-Ghaffar, Juane Li +1
- **PDF**: https://ieeexplore.ieee.org/document/9025269
- **Abstract**: A novel scheme is presented for encoding and iterative soft-decision decoding of cyclic codes of prime lengths. The encoding of a cyclic code of a prime length is performed on a collection of codewords which are mapped through Galois Fourier transform into a codeword in a low-density parity-check code with a binary parity-check matrix for transmission. Using this matrix, binary iterative soft-decision decoding algorithm is applied to jointly decode a collection of codewords from the cyclic code. The joint-decoding allows for information sharing among the received vectors corresponding to the codewords in the collection during the iterative decoding process. For decoding Reed-Solomon and BCH codes of prime lengths, the proposed decoding scheme not only requires much lower decoding complexity than other soft-decision decoding algorithms for these codes, but also yields superior performance. The proposed decoding scheme can also achieve a joint-decoding gain over the maximum likelihood decoding of individual codewords. The decoding scheme is also applied to quadratic residue codes.

## Toward Practical Quantum Secure Direct Communication: A Quantum-Memory-Free Protocol and Code Design

- **Status**: ❌
- **Reason**: QSDC/QKD 양자보안+JEEC 코딩, 양자·보안 원칙 제외이며 고전 바이너리 LDPC 이식 기법 없음
- **ID**: ieee:9130765
- **Type**: journal
- **Published**: Sept. 2020
- **Authors**: Zhen Sun, Liyuan Song, Qin Huang +4
- **PDF**: https://ieeexplore.ieee.org/document/9130765
- **Abstract**: Quantum secure direct communication (QSDC) is capable of direct confidential communications over a quantum channel, which is achieved by dispensing with the key agreement channel of the well-known quantum key distribution (QKD). However, to make QSDC a practical reality, we have to mitigate its reliance on quantum memory, its immediate communication interruption caused by eavesdropping and its low transmission reliability due to the heavy qubit losses. Hence a new QSDC protocol is proposed based on a sophisticated coded single-photon DL04 QSDC protocol to tackle the open challenges. In particular, quantum memory is dispensed with and a high-accuracy secrecy capacity estimate is derived for this protocol by conceiving dynamic joint encryption and error-control (JEEC) coding. We demonstrate that this quantum-memory-free DL04 QSDC (QMF-DL04 QSDC) protocol inches closer to the quantum channel's capacity and significantly improves the original DL04 QSDC's robustness. Moreover, a rate-compatible low-rate JEEC coding scheme is designed for the proposed framework, and the JEEC code advocated is shown to approach the secrecy capacity, despite tolerating an extremely high loss of qubits in the time-varying wiretap channel. Our simulations and experimental results demonstrate that the QMF-DL04 QSDC scheme significantly increases both the secure information rate and the communication distance of the original DL04 protocol.

## Spatially Coupled Codes via Partial and Recursive Superposition for Industrial IoT With High Trustworthiness

- **Status**: ❌
- **Reason**: IIoT용 block Markov superposition 전송(PrBMST) 신뢰성 기법; LDPC는 베이스라인이고 NAND ECC로 이식할 디코더/HW/코드설계 새 기여 없음
- **ID**: ieee:8957069
- **Type**: journal
- **Published**: Sept. 2020
- **Authors**: Shancheng Zhao, Jinming Wen, Shahid Mumtaz +2
- **PDF**: https://ieeexplore.ieee.org/document/8957069
- **Abstract**: For industrial Internet of Things (IIoT), data trustworthiness should be maintained both at the time of sensing and at the time of transmission. This article is concerned with trustworthiness during transmission, which is determined by transmission reliability. We present a low-complexity and flexible method via partial and recursive superposition to improve the transmission reliability of IIoT, resulting in an IIoT with high trustworthiness. In our method, a portion of the previously transmitted data are superimposed onto the current transmitted data to introduce memory among different transmissions, which are then exploited by the windowed decoder to obtain performance gain. The proposed method is referred to as partially recursive block Markov superposition transmission of low-density parity-check (PrBMST-LDPC) codes. This article is focused on the construction of low-complexity PrBMST-LDPC codes since IIoT is resource-limited in nature. The first construction is the memory-one PrBMST-LDPC code. We present a simplified density evolution algorithm to optimize the superposition ratio for memory-one PrBMST-LDPC code. Both the analytical and numerical results show that PrBMST with memory one can be used to reduce the packet loss ratio (PLR) of IIoT using LDPC codes. Particularly, around 1.0 dB performance gain is obtained by PrBMST. We then present a low-complexity construction for PrBMST-LDPC codes with encoding memory larger than one. Simulation results show that compared with memory-one PrBMST, a further PLR reduction of around one order of magnitude can be obtained.

## Design of I-Polar Codes

- **Status**: ❌
- **Reason**: i-polar 부호 비트채널 선택 알고리즘 — polar 코드 전용 기법, LDPC는 비교 베이스라인일 뿐 이식할 LDPC 기법 없음
- **ID**: ieee:9096323
- **Type**: journal
- **Published**: Sept. 2020
- **Authors**: Mao-Ching Chiu, Chun-Yin Chen
- **PDF**: https://ieeexplore.ieee.org/document/9096323
- **Abstract**: Recently, a new family of polar codes, termed interleaved polar (i-polar) codes, was proposed. It has been shown that both i-polar codes and polar codes of the same block length generate the same synthesized channels. Therefore, conventional bit channel selection algorithms designed for polar codes can be employed for i-polar codes. However, since most of the bit channel selection algorithms are optimized under successive cancellation (SC) decoding, i-polar codes as well as polar codes are still weak at short to moderate block lengths even under ML decoding. In this letter, we propose a new bit channel selection algorithm for i-polar codes which generates a sequence termed the i-polar sequence (IPS). The IPS can be used to specify the unfrozen bit sets for any code rates. Simulation results show that stand-alone i-polar codes with IPS under SCL decoding outperform the state-of-the-art 5G LDPC codes and 5G polar codes. Also, the performance levels of stand-alone polar codes with IPS are comparable to those of the 5G LDPC codes.

## Trainable Communication Systems: Concepts and Prototype

- **Status**: ❌
- **Reason**: NN 기반 trainable 통신시스템(IDD) — 표준 802.11n LDPC를 베이스라인으로 사용, 떼어낼 새 LDPC 디코더/코드 기법 없음
- **ID**: ieee:9118963
- **Type**: journal
- **Published**: Sept. 2020
- **Authors**: Sebastian Cammerer, Fayçal Ait Aoudia, Sebastian Dörner +3
- **PDF**: https://ieeexplore.ieee.org/document/9118963
- **Abstract**: We consider a trainable point-to-point communication system, where both transmitter and receiver are implemented as neural networks (NNs), and demonstrate that training on the bit-wise mutual information (BMI) allows seamless integration with practical bit-metric decoding (BMD) receivers, as well as joint optimization of constellation shaping and labeling. Moreover, we present a fully differentiable neural iterative demapping and decoding (IDD) structure which achieves significant gains on additive white Gaussian noise (AWGN) channels using a standard 802.11n low-density parity-check (LDPC) code. The strength of this approach is that it can be applied to arbitrary channels without any modifications. Going one step further, we show that careful code design can lead to further performance improvements. Lastly, we show the viability of the proposed system through implementation on software-defined radios (SDRs) and training of the end-to-end system on the actual wireless channel. Experimental results reveal that the proposed method enables significant gains compared to conventional techniques.

## Unsupervised Linear and Nonlinear Channel Equalization and Decoding Using Variational Autoencoders

- **Status**: ❌
- **Reason**: VAE 기반 블라인드 채널 등화/복호; LDPC는 베이스라인이고 ISI 등화 중심이라 NAND ECC로 떼어낼 디코더 기여 없음
- **ID**: ieee:9080094
- **Type**: journal
- **Published**: Sept. 2020
- **Authors**: Avi Caciularu, David Burshtein
- **PDF**: https://ieeexplore.ieee.org/document/9080094
- **Abstract**: A new approach for blind channel equalization and decoding, variational inference, and variational autoencoders (VAEs) in particular, is introduced. We first consider the reconstruction of uncoded data symbols transmitted over a noisy linear intersymbol interference (ISI) channel, with an unknown impulse response, without using pilot symbols. We derive an approximate maximum likelihood estimate to the channel parameters and reconstruct the transmitted data. We demonstrate significant and consistent improvements in the error rate of the reconstructed symbols, compared to existing blind equalization methods such as constant modulus, thus enabling faster channel acquisition. The VAE equalizer uses a convolutional neural network with a small number of free parameters. These results are extended to blind equalization over a noisy nonlinear ISI channel with unknown parameters. We then consider coded communication using low-density parity-check (LDPC) codes transmitted over a noisy linear or nonlinear ISI channel. The goal is to reconstruct the transmitted message from the channel observations corresponding to a transmitted codeword, without using pilot symbols. We demonstrate improvements compared to the expectation maximization (EM) algorithm using turbo equalization. Furthermore, unlike EM, the computational complexity of our method does not have exponential dependence on the size of the channel impulse response.

## Multi-Kernel Polar Codes: Concept and Design Principles

- **Status**: ❌
- **Reason**: 폴라 부호 설계(다중 커널)로 LDPC가 아니며 NAND LDPC로 떼어낼 기법 없음
- **ID**: ieee:9130741
- **Type**: journal
- **Published**: Sept. 2020
- **Authors**: Valerio Bioglio, Frédéric Gabry, Ingmar Land +1
- **PDF**: https://ieeexplore.ieee.org/document/9130741
- **Abstract**: In this paper, we propose a new polar code construction by employing kernels of different sizes in the Kronecker product of the transformation matrix, thus generalizing the original construction by Arikan. These multi-kernel polar codes allow for more flexibility in terms of the code length and for various new design principles. Next to the common reliability design, we provide a design to maximize the minimal distance and a hybrid design combining reliability and distance properties. Numerical results demonstrate the advantage of multi-kernel polar codes under the new design principles compared to punctured and shortened Arikan polar codes.

## Local Decode and Update for Big Data Compression

- **Status**: ❌
- **Reason**: 빅데이터 압축 local decode/update — 소스코딩(압축), 채널 ECC 아님
- **ID**: ieee:9115085
- **Type**: journal
- **Published**: Sept. 2020
- **Authors**: Shashank Vatedka, Aslan Tchamkerten
- **PDF**: https://ieeexplore.ieee.org/document/9115085
- **Abstract**: This paper investigates data compression that simultaneously allows local decoding and local update. The main result is a universal compression scheme for memoryless sources with the following features. The rate can be made arbitrarily close to the entropy of the underlying source, contiguous fragments of the source can be recovered or updated by probing or modifying a number of codeword bits that is on average linear in the size of the fragment, and the overall encoding and decoding complexity is quasilinear in the blocklength of the source. In particular, the local decoding or update of a single message symbol can be performed by probing or modifying on average a constant number of codeword bits. This latter part improves over previous best known results for which local decodability or update efficiency grows logarithmically with blocklength.

## Coding for Two-User Energy Harvesting Interference Channel

- **Status**: ❌
- **Reason**: 에너지 하베스팅 간섭채널 코딩(NLTC+외부 LDPC); LDPC는 부수적, 떼어낼 ECC 기법 없음
- **ID**: ieee:8972570
- **Type**: journal
- **Published**: Sept. 2020
- **Authors**: Mehdi Dabirnia, Tolga M. Duman
- **PDF**: https://ieeexplore.ieee.org/document/8972570
- **Abstract**: A two-user interference channel with energy harvesting transmitters, each equipped with a finite battery, is considered. Achievable rate regions (ARRs) considering independent and identically distributed Shannon strategies at both users and ignoring the memory in the battery state are obtained for both single-user decoding and joint decoding at the receivers. Explicit and implementable codes based on concatenation of a nonlinear trellis code (NLTC) with an outer low-density parity-check code are designed, and it is demonstrated that rate pairs close to the boundary of ARR can be obtained with this approach. Furthermore, an improved alternative decoding scheme which exploits the memory in the battery state is developed, and it is shown to be highly superior to the simple decoding approach via numerical examples. Superiority of the newly developed practical channel coding solutions over the previously known alternative approaches are illustrated via extensive set of examples as well.

## On Secure Communications Over Gaussian Wiretap Channels via Finite-Length Codes

- **Status**: ❌
- **Reason**: Gaussian wiretap 보안 coset coding + MINE 검증; LDPC ECC 기법 아님, 보안/물리계층 응용 특이적
- **ID**: ieee:9093879
- **Type**: journal
- **Published**: Sept. 2020
- **Authors**: Alireza Nooraiepour, Sina Rezaei Aghdam, Tolga M. Duman
- **PDF**: https://ieeexplore.ieee.org/document/9093879
- **Abstract**: Practical codes for the Gaussian wiretap channel are designed aiming at satisfying information-theoretic metrics to ensure security against a passive eavesdropper (Eve). Specifically, a design criterion is introduced for the coset coding scheme in order to satisfy a strong secrecy condition described with the mutual information between the secret message and Eve's observation. In addition, mutual information neural estimation (MINE) powered from deep learning tools is applied in order to directly compute the information-theoretic security constraint, and verify the proposed solutions. It is shown that finite-length coset codes can indeed ensure secure transmission from an information-theoretic perspective.

## Machine Learning Based Iterative Detection and Multi-Interference Cancellation for Cognitive IoT

- **Status**: ❌
- **Reason**: 인지 IoT 간섭제거용 ML 클러스터링(AP 알고리즘) — LDPC ECC와 무관, 떼어낼 디코더/코드 기법 없음
- **ID**: ieee:9099310
- **Type**: journal
- **Published**: Sept. 2020
- **Authors**: Yi Liu, Xiaojun Yuan, Ying-Chang Liang +1
- **PDF**: https://ieeexplore.ieee.org/document/9099310
- **Abstract**: In this letter, a machine learning approach is proposed to cancel the interference from multiple sources in the concurrent spectrum access (CSA) model of the cognitive Internet of Things (C-IoT). We assume that the C-IoT system is non-cooperative with the primary user (PU) system, and has little knowledge on the interference caused by PU transmitters. In order to recover the C-IoT signal under power strong multi-interference, we employ an iterative receiver consisting of a linear estimation module, and a demodulation-and-decoding module, as well as a clustering module by following the idea of iterative detection and interference cancellation. Conventional clustering algorithms, such as the K-means algorithm and the Gaussian mixture model (GMM) based expectation maximization (EM) algorithm, can potentially be used to realize the clustering module. However, their performance is poor under the existence of multiple interferers since the performance of these algorithms heavily relies on the initialization of cluster centroids. To address this problem, we use the affinity propagation (AP) algorithm, which works well without the initialization of cluster centroids, to realize the clustering module. Numerical results demonstrate that the AP algorithm has much better performance than the K-means and GMM-EM algorithms in handling multi-interference.

## A Network Linear Block Coding Approach to Selective Detect-and-Forward Multi-Way Relaying With Differential Modulation

- **Status**: ❌
- **Reason**: 다중웨이 릴레이용 네트워크 선형블록코딩 프레임워크 — LDPC는 예시 베이스라인, 떼어낼 새 LDPC ECC 기법 없음
- **ID**: ieee:9104013
- **Type**: journal
- **Published**: Sept. 2020
- **Authors**: Xiaoxian Hou, Harry Leib
- **PDF**: https://ieeexplore.ieee.org/document/9104013
- **Abstract**: This paper introduces a network linear block coding framework for multi-way relaying with differential MPSK modulation. We consider a system with K user terminals and L relays employing a selective detect-and-forward protocol. We show that such a system can be represented as a systematic (K+L,K) linear block code. This framework allows the use of linear systematic block codes as network codes yielding power saving gains at user terminals. We analyse the theoretical performance of our scheme with optimal decoding, showing that our system can achieve a diversity order that equals to the minimum Hamming distance of the associated code. Then we consider a sub-optimal decoder based on log-domain belief propagation, and present numerical results for three 4-ary linear block codes and two binary LDPC codes as examples. Theoretical and simulation results demonstrate a significant performance gain of our scheme over uncoded transmission, even though some relays may be silent occasionally. We present a technique based on hard thresholding the received samples at the terminals, that makes the performance closer to the case when no relay is silent, without any significant increase in complexity. Furthermore, we also present guidelines for choosing suitable codes, and show that systematic block codes with sparse generator matrices are in particular desirable for our system.

## PEG-LDPC Coding for Critical Communications in Factory Automation

- **Status**: ❌
- **Reason**: 표준 QC-PEG-LDPC를 공장자동화에 적용해 5G와 비교한 work-in-progress, 새 코드/디코더 기여 없음
- **ID**: ieee:9211899
- **Type**: conference
- **Published**: 8-11 Sept.
- **Authors**: L. Fanari, E. Iradier, J. Montalban +3
- **PDF**: https://ieeexplore.ieee.org/document/9211899
- **Abstract**: Critical communication requirements included in Factory Automation applications are complex to implement due to the difficulties encountered in guaranteeing high reliability and ultra-low latencies at the same time. In this work-in-progress, a technical solution for the physical layer is proposed: the Quasi-Cyclic LDPC of the Progressive Edge Growth family (QC-PEGLDPC). This coding scheme is considered as a promising candidate due to two main factors: the good decoding performance for short packet transmissions and the low latency that can be obtained by using full parallel decoding architectures. The obtained results are compared with the 5G New Radio coding scheme, which includes LDPCs as part of the solution for Ultra Reliable Low Latency (URLLC) use cases. In these first results, QC-PEG-LDPC shows a performance improvement of 1 dB when compared with the 5G LDPC codes for a message length of 128 bits. Latency analysis indicate that QC-PEG-LDPC could allow decoding latencies of 0.13 µs providing that the full parallel decoding architecture is enabled.

## FPGA Implementation of LDPC Encoder Architecture for Wireless Communication Standards

- **Status**: ❌
- **Reason**: 표준 IEEE 802.16e QC-LDPC 인코더의 FPGA 구현으로, 새 디코더/코드설계 기여 없이 표준 부호를 그대로 구현한 수준
- **ID**: ieee:9200293
- **Type**: conference
- **Published**: 7-9 Sept. 
- **Authors**: Ruslan Goriushkin, Pavel Nikishkin, Aleksei Ovinnikov +2
- **PDF**: https://ieeexplore.ieee.org/document/9200293
- **Abstract**: In this paper a pipeline architecture is proposed for FPGA implementation of a quasi-cyclic LDPC (QC-LDPC) encoder. The results are provided for implementation on a Xilinx ZYNQ-7 ZC706 Evaluation Board for code with rate 5/6 and block lengths from 576 to 2304. The design is parameterized and can be easily rebuilt to support various code rates and code lengths. The base matrices H and code parameters are taken from the IEEE 802.16e standard. The number of logic elements (LUT), clock speed, and throughput of the encoder are presented for different code lengths. The throughput of up to 16 Gbps for IEEE 802.16e codes has been achieved.

## A Digital Root Based Modular Reduction Technique for Power Efficient, Fault Tolerance in FPGAs

- **Status**: ❌
- **Reason**: FPGA digital root 기반 결함검출 기법, LDPC 디코더는 error-tolerant 테스트 벤치로만 사용 — 떼어낼 LDPC ECC 기법 없음
- **ID**: ieee:9221606
- **Type**: conference
- **Published**: 31 Aug.-4 
- **Authors**: Richard Dorrance, Andrey Belogolovy, Hechen Wang +1
- **PDF**: https://ieeexplore.ieee.org/document/9221606
- **Abstract**: Recent advancements in performance, logic density, and power consumption of Field-Programmable Gate Arrays (FPGAs) have made them attractive for their widespread adoption into automotive, aircraft, space, military, and other safety-critical applications, in both embedded systems and cloud computing platforms. Every year, though, it becomes harder and harder to benefit from such advances in technology scaling due to smaller voltage margins, more aggressive clocking schemes, and greater device variability. FPGAs are often expected to last years or even decades in a variety of different environments before replacement. In some applications, they can be susceptible to soft and transient errors due to Single Event Upsets (SEUs), environment, and aging related effects. In this paper, we propose a simplified modular arithmetic technique based upon the concept of the digital root (DR) to monitor soft and transient errors, with low area overhead and high rates of detectability. The technique can be easily implemented at the register-transfer level (RTL) with no need to modify the underlying hardware of the FPGA. In one experiment, after dropping the supply voltage well below recommended design margins, we show in situ measurements on the instantaneous error rate in an Intel Arria 10 GX FPGA, which can be leveraged to optimize the power-performance trade-off of already deployed designs. We demonstrate this tradeoff, using an inherently error tolerant low-density parity-check (LDPC) decoder block, by either increasing the system clock beyond its synthesized target to achieve a 50% improvement in throughput, or by lowering the FPGA's supply voltage below synthesized design margins for a 65% reduction in power.

## Performance Evaluation of OFDM Index Modulation with LDPC Code

- **Status**: ❌
- **Reason**: OFDM 인덱스 변조 성능평가, NR LDPC를 표준 그대로 사용 — 새 ECC 기여 없음
- **ID**: ieee:9217242
- **Type**: conference
- **Published**: 31 Aug.-3 
- **Authors**: Xiaopu Yu, Jiyong Pang
- **PDF**: https://ieeexplore.ieee.org/document/9217242
- **Abstract**: In this paper, performance of orthogonal frequency division multiplexing (OFDM) with index modulation (IM) based schemes is evaluated. We consider the well known OFDM-IM, where partial subcarriers are activated and the corresponding indices convey extra information, and its variant multiple-mode OFDM-IM (MM-OFDM-IM) which provides better spectral efficiency (SE) and uncoded bit error rate (BER) by activating all subcarriers and using distinguishable constellations. Although uncoded performance has been extensively discussed for these techniques, performance with channel codes involved lacks of evaluation and discussion. Therefore, we present both uncoded and coded BER performance with new radio (NR) low density parity check (LDPC) code in this paper, where LDPC codes with different code rates are employed. Simulation results show that OFDM-IM based scheme with LDPC code outperforms the conventional OFDM with LDPC code only within a limited code rate range, although its uncoded performance offers large gains at high SNR.

## Prediction and Voting Based Symbol Flipping Non-Binary LDPC Decoding Algorithms

- **Status**: ❌
- **Reason**: non-binary GF(q) LDPC 심볼 플리핑 디코더 — 비이진 LDPC라 제외 원칙
- **ID**: ieee:9217108
- **Type**: conference
- **Published**: 31 Aug.-3 
- **Authors**: Waheed Ullah, Ling Cheng, Fambirai Takawira
- **PDF**: https://ieeexplore.ieee.org/document/9217108
- **Abstract**: In this paper, we present two low complexity algorithms to decode non-binary LDPC codes. The proposed decoding algorithms update iteratively the hard decision received vector to search for a valid codeword in the vector space of Galois field (GF). The selection criterion for the position of unreliable symbols is based on failed checks and the information from the Galois field structure. In the first proposed algorithm, the flipping function is calculated for all symbols of the received sequence and multiple symbols are flipped in each iteration while in the second proposed algorithm, a single symbol is flipped per iteration. In the second method, unreliable positions are short-listed by using a majority voting scheme, and then the flipping function is computed to predict candidate symbols from the set of symbols in GF(q) while not violating the field order q. The proposed methods reduce the decoding complexity and memory use. The results of the algorithms show appealing tradeoffs between complexity and bit error rate performance for non-binary LDPC codes.

## A Soft Cancellation Decoder for Parity-Check Polar Codes

- **Status**: ❌
- **Reason**: Polar code용 soft-cancellation 디코더 — LDPC 아님
- **ID**: ieee:9217144
- **Type**: conference
- **Published**: 31 Aug.-3 
- **Authors**: Jiajie Tong, Huazi Zhang, Xianbin Wang +3
- **PDF**: https://ieeexplore.ieee.org/document/9217144
- **Abstract**: Polar codes has been selected as the channel coding scheme for 5G new radio (NR) control channel. Specifically, a special type of parity-check polar (PC-Polar) codes was adopted in uplink control information (UCI). In this paper, we propose a parity-check soft-cancellation (PC-SCAN) algorithm and its simplified version to decode PC-Polar codes. The potential benefits are two-fold. First, PC-SCAN can provide soft output for PCPolar codes, which is essential for advanced turbo receivers. Second, the decoding performance is better than that of successive cancellation (SC). This is due to the fact that paritycheck constraints can be exploited by PC-SCAN to enhance the reliability of other information bits over the iterations. Moreover, we describe a cyclic-shift-register (CSR) based implementation "CSR-SCAN" to reduce both hardware cost and latency with minimum performance loss.

## Variable Quantization for Memory-Efficient Successive Cancellation Decoding of Polar Codes - A Heuristic Approach

- **Status**: ❌
- **Reason**: Polar code SC decoder LLR 비트폭 양자화 휴리스틱 — polar 전용 SC 디코더라 바이너리 LDPC BP에 이식 안 됨
- **ID**: ieee:9217289
- **Type**: conference
- **Published**: 31 Aug.-3 
- **Authors**: Muhammad Farooq, Humera Hameed, Muhammad Usman +1
- **PDF**: https://ieeexplore.ieee.org/document/9217289
- **Abstract**: This paper presents an algorithm to reduce the hardware complexity of the successive-cancellation decoder for polar codes. It has already been discussed in the literature that allocating 6 bits to all log-likelihood ratios instead of using floating point values, can keep performance degradation within 0.1 dB at frame-error rate of 10^-3. It has been shown in the paper that if we allocate different bits to different set of log-likelihood ratios rather than assigning the same number of bits to all log-likelihood ratios, the performance degradation is within 0.4 dB at frame-error rate of 10^-3. The results show that the proposed variable bit assignment strategy can save the processing elements in the architecture proposed by Arikan and it was observed that the bit width of N/2-1 processing elements out of total N-1 processing elements can be reduced up to 4 bits for a block length of N. In summary, this work has established a trade-off between the number of six bit processing elements and frame-error rate performance of the successive-cancellation decoder.

## Blind Twins: Siamese Networks for Non-Interactive Information Reconciliation

- **Status**: ❌
- **Reason**: Siamese CNN 기반 비대화형 정보조정(키생성) — LDPC ECC 기법 무관
- **ID**: ieee:9217278
- **Type**: conference
- **Published**: 31 Aug.-3 
- **Authors**: Paul Walther, Thorsten Strufe
- **PDF**: https://ieeexplore.ieee.org/document/9217278
- **Abstract**: Through Information Reconciliation, two legitimate parties of Channel Reciprocity-based Key Generation assure that they extract the same key from local channel measurements. Current protocols exchange messages: Interactivity both causes delays and energy expenditure, and leaks information about the keying material to adversaries.We suggest non-interactive reconciliation, using a Siamese Network of CNNs that extracts reciprocal and suppresses nonreciprocal components in the measurements. Training and evaluating on real-world and synthetic data, we demonstrate that it blindly achieves higher correlation of the outputs at legitimate parties than the interactive state of the art, thus eliminating cost and information leakage at superior performance.

## Performance Analysis of DVB-T2 System Based on MIMO Using Low Density Parity Check (LDPC) Code Technique and Maximum Likelihood (ML) Detection

- **Status**: ❌
- **Reason**: DVB-T2 MIMO/ML 검출 BER 시뮬레이션, LDPC는 표준 부수 언급뿐 — 떼어낼 신규 디코더/HW/구성 기법 없음
- **ID**: ieee:9231792
- **Type**: conference
- **Published**: 29-30 Sept
- **Authors**: Maudy Arini Fitria Chakiki, I Gede Puja Astawa, Anang Budikarso
- **PDF**: https://ieeexplore.ieee.org/document/9231792
- **Abstract**: The MIMO (Multiple Input Multiple Output) system works very well on multipath components. Some multipath components are exploited to increase bandwidth diversity and efficiency. In addition, this system also provides a significant increase in data throughput and communication coverage without expand the frequency and transmit power. Even so, this system is still vulnerable to InterSymbol Interference. Low Density Parity Check (LDPC) technique which is has the ability to correct errors near the Shannon limit (theoretical maximum error correction limit) and Maximum likelihood (ML) detection which is able to provide performance minimum bit errors are believed to be able to handle interference arising when passing through a channel.This research made a MIMO 2X2 simulation system on DVB-T2 technology with LDPC coding technique and Maximum Likelihood detector. The results obtained from running this simulation system indicate that the system which is has smaller rate is the better system. The ideal system without error correction code shows the Maximum Likelihood performance forming a waterfall curve and no more errors at 20 dB. While the system with LDPC and Maximum Likelihood is able to reaches BER (bit error rate) 10-2 at SNR (Signal to Noise Ratio) around 1 dB from the 1/2 rate system, and the 3/4 rate system reaches BER 10-2 at around 4 dB, and the 5/6 rate system reaches BER 10-2 at SNR around 6 dB.

## Performance Analysis of MIMO Detection Techniques in DVB-T2 Systems

- **Status**: ❌
- **Reason**: DVB-T2 MIMO 검출기(V-BLAST/MMSE/ZF) 성능 비교 — LDPC ECC 기법 무관
- **ID**: ieee:9231868
- **Type**: conference
- **Published**: 29-30 Sept
- **Authors**: Ani Rosyidah, I Gede Puja Astawa, Anang Budiknrso
- **PDF**: https://ieeexplore.ieee.org/document/9231868
- **Abstract**: Digital Video Broadcasting-Terrestrial Second Generation (DVB-T2) is a digital television broadcasting system that is being implemented in the world. This system can send large amounts of data at high point-to-multipoint speed. Multiple Input Multiple Output (MIMO) is a transmission technique that is implemented in many new technologies nowadays. This technique can increase the data rate without increasing the bandwidth. In this study, a DVB-T2 system simulation was made by applying 2x2 MIMO-OFDM technology. For better system performance, it is necessary to use a detector to minimize the noise in the data transmission process. In this study, simulations and analyzation were performed to determine the performance of MIMO detectors on a DVB-T2 system. The analysis was done by comparing the BER curve to the generated SNR value by each detector system. The simulation results show that the Vertical Bell Labs Layered Space-Time/Minimum Mean Square Error (V-BLAST/MMSE) detection technique is the best technique in improving system performance, followed by V-BLAST/ZF, Minimum Mean Square Error (MMSE), and Zero Forcing (ZF) detectors.

## Interleaved Non-Binary LDPC Code for Synchronization Error Correction in DNA Storage

- **Status**: ❌
- **Reason**: DNA 스토리지용 비이진(non-binary) LDPC + sum-product — 비이진 LDPC는 제외 대상
- **ID**: ieee:9258250
- **Type**: conference
- **Published**: 28-30 Sept
- **Authors**: Haruhiko Kaneko
- **PDF**: https://ieeexplore.ieee.org/document/9258250
- **Abstract**: DNA storage devices are generally prone to synchronization errors, and hence these devices will require strong synchronization error correction coding to improve the reliability. This paper presents a insertion/deletion/substitution (IDS) error correction coding based on interleaving of non-binary LDPC codes. We employ an iterative decoding using a belief propagation on drift factor graph and a non-binary sum-product algorithm. This decoding successively recovers synchronization from both ends to center in a received word. Simulation results show that the presented coding of block size 4096×100 with rate-3/4 gives decoded block error rate 2.0×10-3 for IDS channel of insertion/deletion error probability 2.1 ×10-2 and substitution error probability 1.0×10-2.

## Probabilistic Amplitude Shaping in Power Line Communication

- **Status**: ❌
- **Reason**: PLC 확률적 진폭 성형(PAS) — LDPC는 베이스라인 부수 언급, 떼어낼 ECC 기법 없음
- **ID**: ieee:9236908
- **Type**: conference
- **Published**: 27-29 Sept
- **Authors**: Yingxue Li, Huiyun Peng, Jing Lei +4
- **PDF**: https://ieeexplore.ieee.org/document/9236908
- **Abstract**: Power Line Communication (PLC) is a communication method that using the existing power line network as the information transmission carrier. Medium voltage (MV) underground power line can provide functions such as power quality measurement and remote control of the electrical network. However, due to the complex channel and noise model, the transmission reliability in PLC suffers a lot. As probabilistic amplitude shaping (PAS) shows a significant improvement in frame error rate (FER) in wireless channels, we aim to apply PAS in MV power line channels in this paper to evaluate its performance. First, the MV power line channel is modeled as a multiple-input multiple-output (MIMO) channel in the presence of impulsive noise and background noise. Next, we introduce the basic idea of PAS and implement it with bipolar amplitude shift keying (ASK) modulation and low-density parity-check (LDPC) codes. Finally, we compare the FER with or without PAS in the power line channel. Numerical results show that, to achieve the same FER, adopting PAS in the power line channel can save 40% transmitting power under 64-QAM modulation.

## Design Issues and Challenges of an FPGA-based Orthogonal Matching Pursuit Implementation for Compressive Sensing Reconstruction

- **Status**: ❌
- **Reason**: 압축센싱 OMP의 FPGA 구현 리뷰 — LDPC 무관, 소스 복원 알고리즘
- **ID**: ieee:9250973
- **Type**: conference
- **Published**: 27-29 Sept
- **Authors**: Muhammad Muzakkir Mohd Nadzri, Afandi Ahmad, Zarina Tukiran
- **PDF**: https://ieeexplore.ieee.org/document/9250973
- **Abstract**: Compressive sensing (CS) is as an evolving research area in signal processing due to the advantages offered for signal compression. Based on the sparsity of signals, CS allows the sampling of sparse signals under the sub-Nyquist rate, and yet promises a reliable data recovery. To date, the implementation of practical applications of CS in hardware platforms, especially in real-time applications, still faces challenging issues due to the high computational complexity of its algorithms, hence leading to high power-consuming processes. There are several CS reconstruction approaches, and orthogonal matching pursuit (OMP) is one of the best and popular algorithms implemented. However, this algorithm faces two (2) major process issues: optimisation and the least square problem. Due to OMP's significant contribution, this paper presents an overview of the design issues and challenges of OMP algorithm implementation for CS reconstruction. The field-programmable gate array (FPGA) as a viable hardware solution for OMP implementation is reviewed and discussed based on reconstruction time, signal size, number of measurements, sparsity and features.

## Low Density Parity Check Code (LDPC) for Enhancement of Visible Light Communication (VLC) Performance

- **Status**: ❌
- **Reason**: VLC에 표준 QC-LDPC+bit-flipping 단순 적용, 새 기여 없는 무선응용; 표준 기법 재사용 제외
- **ID**: ieee:9234285
- **Type**: conference
- **Published**: 19-20 Sept
- **Authors**: Brian Pamukti, Fernaldy Arifin, Nachwan Mufti Adriansyah
- **PDF**: https://ieeexplore.ieee.org/document/9234285
- **Abstract**: Visible Light Communication (VLC) that utilizes free space optics as a transmission channel has a high-speed data communication capability, which uses Light Emitting Diode (LED) as a transmitter. Problems occurred in this wireless communication is the distance. VLC can only reach relatively short distance if compared to Radio Frequency (RF). There are many ways to reach a better distance performance on VLC and one of them is the error correction. In this paper, a comparison between uncoded and Quasi-Cyclic-Low Density Parity Check (QC-LDPC) codes implementation on VLC has been compared and the number of decoding iterations is simulated to reach better performance. The encoding technique of QC-LDPC codes is using the G-Matrix and Bit Flipping algorithm as the decoding. The result shows that distance increases 7% in case of QC-LDPC codes from the uncoded VLC system and 27.5% energy efficiency are increased. The number of decoding iterations also contributes an impact to Bit Error Rate (BER) performance. The simulation results proof that on VLC system using QC-LDPC codes shows better performance compared to the uncoded system.

## Evaluation of Intensity Modulated WDM FOTS with Interleaved RS-FEC Code Schemes

- **Status**: ❌
- **Reason**: RS-FEC 코드 광전송 평가; 비-LDPC 부호, 떼어낼 LDPC 기법 없음
- **ID**: ieee:9238320
- **Type**: conference
- **Published**: 17-19 Sept
- **Authors**: Svitlana Matsenko, Sandis Spolitis, Vjaceslavs Bobrovs
- **PDF**: https://ieeexplore.ieee.org/document/9238320
- **Abstract**: In this paper, through the development of the simulation model, we researched the schemes of forward error correction (FEC) code based on the Reed-Solomon (RS-FEC) code within the 25 Gb/s intensity-modulated non-return-to-zero on-off-keying (NRZ-OOK) modulated wavelength division multiplexed fiber-optical transmission system (WDM FOTS). The performance of error correction of RS- FEC code schemes such as RS (255, 227) with 12% overhead (OH), RS (255, 239) with 6.7% OH, RS (255, 235) with 8.5% OH and RS (511, 479) with 6.7% OH and with block interleaver was evaluated. The performance of implemented RS-FEC code schemes was investigated by using the bit error rate (BER) monitoring based on the Monte Carlo (MC) method.

## Evaluation of Channel Coding Techniques for Massive Machine-Type Communication in 5G Cellular Network

- **Status**: ❌
- **Reason**: 5G mMTC LDPC vs Polar 성능 비교 — 표준 부호 단순 평가, 신규 기여 없음
- **ID**: ieee:9232037
- **Type**: conference
- **Published**: 12-15 Sept
- **Authors**: Muhammad Huseen Khan, Gongxuan Zhang
- **PDF**: https://ieeexplore.ieee.org/document/9232037
- **Abstract**: Recently, an intensive discussion on candidate channel coding schemes for the fifth-generation (5G) mobile communication systems has been carried out both in academia and industry. We added to this discussion by providing a comparison between two capacity-achieving channel codes: Low-density Parity-Check (LDPC) codes and Polar codes. The considered codes have been selected as the standard for 5G New Radio (NR) by the 3rd Generation Partnership Project (3GPP). We investigate these codes in terms of Frame Error Rate (FER) on small and moderate length message transmission in the context of Massive Machine type communication (mMTC). Multiple decoding implementation schemes are considered for both codes and compare their error correction performance over an Additive White Gaussian Noise (AWGN) channel. The simulation results reveal that polar codes under the Cyclic redundancy code (CRC) aided Successive Cancellation list (CA-SCL) decoding performs better as compared to other decoding patterns in terms of reliability. Furthermore, we analyze the impact of CRC length on the decoding performance of CA-SCL.

## A Novel Demodulation Network for Binary Partial Response CPM Signals

- **Status**: ❌
- **Reason**: CPM 신호 CNN 복조 — LDPC/ECC 무관, 떼어낼 기법 없음
- **ID**: ieee:9232041
- **Type**: conference
- **Published**: 12-15 Sept
- **Authors**: Haowei Wu, Qihao Peng, Jiaying Wang +2
- **PDF**: https://ieeexplore.ieee.org/document/9232041
- **Abstract**: Continuous phase modulation (CPM) is a promising modulation scheme, due to its constant envelope and compact spectrum. However, the application of CPM is limited by the demodulation and the strict requirements of synchronization. A novel method based on the convolution neural network (CNN) is proposed for binary partial response CPM signals, where the structure of the neural network is designed according to the traditional demodulation processing. Specifically, the convolution kernels are applied to extract the high-dimensional features, which are different from the branch metrics calculated by the matched filters and phase rotation. And then the extracted features are mapped in the fully-connected layers, which plays the same role as the Viterbi decoder. Besides, the moving step of the convolution kernels is small, so that the extracted features can obtain more information than the branch metrics, even though there are some timing errors. Our numerical evaluations demonstrate that the performance of the proposed method approaches that of the theoretical optimal method. Moreover, the designed network is robust to normalized timing variance with no extra training.

## An Efficient Low-Latency Algorithm and Implementation for Rate-Matching and Bit-Interleaving in 5G NR

- **Status**: ❌
- **Reason**: 5G NR rate-matching/bit-interleaving 알고리즘, LDPC 인코딩 후단 처리로 디코더/코드설계 ECC 기법 아님
- **ID**: ieee:9221397
- **Type**: conference
- **Published**: 10-12 Sept
- **Authors**: Khitish C Behera
- **PDF**: https://ieeexplore.ieee.org/document/9221397
- **Abstract**: 5G New Radio (NR) is primarily characterized by multi-Gbps throughput and up to 10X lower latency than LTE. 5G adopts Low-Density Parity Check (LDPC) code as the channel coding candidate for data channels. Rate-Matching and Bit-Interleaving functions are performed after LDPC encoding in the transmit signal chain. The purpose of Rate Matching is to select a specific set of encoded bits for transmission by the process of puncturing and/or repetition to support HARQ operation. The output of the Rate-Matching buffer goes through row-column permutation function in Bit-Interleaving process. The rate-matched bits from the circular buffer are written in row-first order into another buffer and read in column-first order. While copying the bits from the rate-matching circular buffer, the filler bits are skipped and does not enter the row-column buffer. The rate-matching buffer to row-column buffer copy operation accounts for the overall latency in the transmit chain. This paper addresses the latency aspects while processing the large Transport Blocks corresponding to the maximum downlink (DL) throughput. An efficient M-parallel look-ahead pointers generation algorithm is proposed to read M-interleaved bits directly from rate-matching buffer, avoiding row-column permutation operation, and thus the need of a separate buffer, where M is programmed for a target latency.

## Low Complexity LDPC Error Correction Code for Modified Anderson PUF to Improve its Uniformity

- **Status**: ❌
- **Reason**: PUF 보안 키생성용 LDPC, 교과서 bit-flip 디코더만 사용, 새 기여 없고 보안 도메인
- **ID**: ieee:9215273
- **Type**: conference
- **Published**: 10-12 Sept
- **Authors**: Manasa kalya, Sathish Kumar
- **PDF**: https://ieeexplore.ieee.org/document/9215273
- **Abstract**: This paper introduced a new LDPC error correction algorithm to Modified Anderson PUF key generation for hardware security. Most of the time PUFs are easily affected by the environmental conditions. To avoid those effects, introducing a new error correction scheme called Low-density parity checker error correction (LDPC). LDPC code helps to find the position of the error and also error has been corrected, using the Bit flipping algorithm at the decoder end. For better PUF key generation than the previously used BCH error correction algorithm, LDPC helps to perform the responses with good uniformity and less complexity. LDPC error code for Modified Anderson PUF can be used for many applications like WiMax, DVB, DAB, UMTS, multimedia Applications.

## Performance of Downlink SISO NR System using MMSE-IRC Receiver

- **Status**: ❌
- **Reason**: 5G NR SISO MMSE-IRC 수신기 성능평가, LDPC 부수 언급, 떼어낼 기법 없음
- **ID**: ieee:9221267
- **Type**: conference
- **Published**: 10-12 Sept
- **Authors**: Rahul Makkar, Venugopalachary Kotha, M Sheeba Kumari +3
- **PDF**: https://ieeexplore.ieee.org/document/9221267
- **Abstract**: In this work, we investigated the performance of single input single output (SISO) downlink channel considering 5G new radio (NR). A number of parameters such as different modulation schemes, channel coding with varying code rates, scalable numerology μ and 3GPP channel models have been considered for evaluation. In addition, the minimum mean square error-interference rejection combining (MMSE-IRC) technique for interference mitigation and bit error rate (BER) performance is analyzed and presented. We also compared the sum-rate performance of LTE and 5G NR. It is observed that MMSE-IRC receiver successfully mitigates the interferences compared to only MMSE based receiver. Simulation results also show performance improvement over various parameters like sum-rate, interference mitigation and BER compared to prior technologies i.e. 4G-LTE, WiMAX, etc.

## CURE: A High-Performance, Low-Power, and Reliable Network-on-Chip Design Using Reinforcement Learning

- **Status**: ❌
- **Reason**: NoC 설계+RL, 라우터 오류정정 HW지만 LDPC ECC 무관. 떼어낼 LDPC 디코더 기법 없음
- **ID**: ieee:9061016
- **Type**: journal
- **Published**: 1 Sept. 20
- **Authors**: Ke Wang, Ahmed Louri
- **PDF**: https://ieeexplore.ieee.org/document/9061016
- **Abstract**: We propose CURE, a deep reinforcement learning (DRL)-based NoC design framework that simultaneously reduces network latency, improves energy-efficiency, and tolerates transient errors and permanent faults. CURE has several architectural innovations and a DRL-based hardware controller to manage design complexity and optimize trade-offs. First, in CURE, we propose reversible multi-function adaptive channels (RMCs) to reduce NoC power consumption and network latency. Second, we implement a new fault-secure adaptive error correction hardware in each router to enhance reliability for both transient errors and permanent faults. Third, we propose a router power-gating and bypass design that powers off NoC components to reduce power and extend chip lifespan. Further, for the complex dynamic interactions of these techniques, we propose using DRL to train a proactive control policy to provide improved fault-tolerance, reduced power consumption, and improved performance. Simulation using the PARSEC benchmark shows that CURE reduces end-to-end packet latency by 39 percent, improves energy efficiency by 92 percent, and lowers static and dynamic power consumption by 24 and 38 percent, respectively, over conventional solutions. Using mean-time-to-failure, we show that CURE is 7.7× more reliable than the conventional NoC design.
