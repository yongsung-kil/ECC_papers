# IEEE Xplore — 2016-12


## FUN Coding: Design and Analysis

- **Status**: ❌
- **Reason**: Fountain+network coding(FUN) 멀티홉 throughput - fountain/네트워크코딩, 채널 ECC LDPC 기법 없음
- **ID**: ieee:7387794
- **Type**: journal
- **Published**: December 2
- **Authors**: Huazi Zhang, Kairan Sun, Qiuyuan Huang +2
- **PDF**: https://ieeexplore.ieee.org/document/7387794
- **Abstract**: Joint FoUntain coding and Network coding (FUN) is proposed to boost information spreading over multi-hop lossy networks. The novelty of our FUN approach lies in combining the best features of fountain coding, intra-session network coding, and cross-next-hop network coding. This paper provides an in-depth study of FUN codes. First, we theoretically analyze the throughput of FUN codes. Second, we identify several practical issues that may undermine the actual performance, such as buffer overflow, and quantify the resulting throughput degradation. Finally, we propose a systematic design to overcome these issues. Simulation results in TDMA multi-hop networks show that our methods yield near-optimal throughput and are significantly better than fountain codes and existing network coding schemes.

## Parity-Check-Concatenated Polar Codes

- **Status**: ❌
- **Reason**: polar 부호 + 패리티검사 연접, 비-LDPC 부호이며 디코더 기법이 LDPC BP로 이식되지 않음
- **ID**: ieee:7563394
- **Type**: journal
- **Published**: Dec. 2016
- **Authors**: Tao Wang, Daiming Qu, Tao Jiang
- **PDF**: https://ieeexplore.ieee.org/document/7563394
- **Abstract**: In this letter, concatenation of parity-check and polar codes is proposed to improve error correction performance. In addition, a heuristic construction of the parity-check-concatenated (PCC) polar codes is proposed. Simulation results show that the PCC polar codes with the heuristic construction have evident performance gains over the cyclic redundancy check-concatenated polar codes.

## Structural Analysis of Array-Based Non-Binary LDPC Codes

- **Status**: ❌
- **Reason**: 비이진(non-binary GF(q)) LDPC 구조 분석, 비이진 LDPC는 제외 대상
- **ID**: ieee:7569103
- **Type**: journal
- **Published**: Dec. 2016
- **Authors**: Shancheng Zhao, Xiujie Huang, Xiao Ma
- **PDF**: https://ieeexplore.ieee.org/document/7569103
- **Abstract**: Structural properties of array-based non-binary low-density parity-check (NBLDPC) codes are studied in this paper. First, we characterize graphical substructures induced by codewords of symbol weight six in array-based NBLDPC codes defined by parity-check matrices with column weight three. We also reveal necessary conditions for these graphical substructures to incur weight-6 codewords. Such conditions can be used to select nonzero elements for avoiding weight-6 codewords or reducing the multiplicity of weight-6 codewords. Second, we show that there exist weight-7 codewords in array-based NBLDPC codes defined by parity-check matrices with column weight three. As a byproduct, we find that the graphical substructure induced by a weight-7 codeword takes the graphical substructure induced by the related weight-6 codewords as a subgraph. Third, we show that there may exist codewords with symbol weight four, six, and seven in array-based NBLDPC codes defined by parity-check matrices with column weight two. These results enrich the structural analysis of array-based LDPC codes. In addition, simulation results show the performance advantage of array-based NBLDPC codes.

## Unified Scaling of Polar Codes: Error Exponent, Scaling Exponent, Moderate Deviations, and Error Floors

- **Status**: ❌
- **Reason**: polar 부호 스케일링/error floor 이론 bound, 비-LDPC이며 디코더/HW/구성으로 안 이어짐
- **ID**: ieee:7589109
- **Type**: journal
- **Published**: Dec. 2016
- **Authors**: Marco Mondelli, S. Hamed Hassani, Rüdiger L. Urbanke
- **PDF**: https://ieeexplore.ieee.org/document/7589109
- **Abstract**: Consider the transmission of a polar code of block length  $N$  and rate  $R$  over a binary memoryless symmetric channel  $W$  and let  $P_{\mathrm{ e}}$  be the block error probability under successive cancellation decoding. In this paper, we develop new bounds that characterize the relationship of the parameters  $R$ ,  $N$ ,  $P_{\mathrm{ e}}$ , and the quality of the channel  $W$  quantified by its capacity  $I(W)$  and its Bhattacharyya parameter  $Z(W)$ . In previous work, two main regimes were studied. In the error exponent regime, the channel  $W$  and the rate  $R<I(W)$  are fixed, and it was proved that the error probability  $P_{\mathrm{ e}}$  scales roughly as  $2^{-\sqrt {N}}$ . In the scaling exponent approach, the channel  $W$  and the error probability  $P_{\mathrm{ e}}$  are fixed and it was proved that the gap to capacity  $I(W)-R$  scales as  $N^{-1/\mu }$ . Here,  $\mu $  is called scaling exponent and this scaling exponent depends on the channel  $W$ . A heuristic computation for the binary erasure channel (BEC) gives  $\mu =3.627$  and it was shown that, for any channel  $W$ ,  $3.579 \le \mu \le 5.702$ . Our contributions are as follows. First, we provide the tighter upper bound  $\mu \le 4.714$  valid for any  $W$ . With the same technique, we obtain the upper bound  $\mu \le 3.639$  for the case of the BEC; this upper bound approaches very closely the heuristically derived value for the scaling exponent of the erasure channel. Second, we develop a trade-off between the gap to capacity  $I(W)-R$  and the error probability  $P_{\mathrm{ e}}$  as the functions of the block length  $N$ . In other words, we neither fix the gap to capacity (error exponent regime) nor the error probability (scaling exponent regime), but we do consider a moderate deviations regime in which we study how fast both quantities, as the functions of the block length  $N$ , simultaneously go to 0. Third, we prove that polar codes are not affected by error floors. To do so, we fix a polar code of block length  $N$  and rate  $R$ . Then, we vary the channel  $W$  and study the impact of this variation on the error probability. We show that the error probability  $P_{\mathrm{ e}}$  scales as the Bhattacharyya parameter  $Z(W)$  raised to a power that scales roughly like  ${\sqrt {N}}$ . This agrees with the scaling in the error exponent regime.

## A Fast Polar Code List Decoder Architecture Based on Sphere Decoding

- **Status**: ❌
- **Reason**: polar SC list 디코더 sphere decoding 가속 — polar 전용 SC 구조 의존, 바이너리 LDPC BP에 이식 불가
- **ID**: ieee:7742998
- **Type**: journal
- **Published**: Dec. 2016
- **Authors**: Seyyed Ali Hashemi, Carlo Condo, Warren J. Gross
- **PDF**: https://ieeexplore.ieee.org/document/7742998
- **Abstract**: Polar codes are a recently discovered family of capacity-achieving error-correcting codes. Among the proposed decoding algorithms, successive-cancellation list decoding guarantees the best error-correction performance with codes of moderate lengths, but it yields low throughput. Speed-up techniques have been proposed in the past: most of them rely on approximations that degrade the error-correction capability of the algorithm. We propose a speed-up technique for successive-cancellation list decoding of polar codes that is exact for list size of 2, while its approximations bring negligible error-correction performance degradation (<;0.05 dB) for other list sizes. A decoder architecture is designed: the proposed technique increases the throughput of a factor of 3.16×, at the cost of 14.2% in area occupation.

## Low Complexity Message Passing Algorithm for SCMA System

- **Status**: ❌
- **Reason**: SCMA용 MPA 임계값 기반 복잡도 저감, 통신 응용 특이적 부호이며 바이너리 LDPC BP 비의존
- **ID**: ieee:7567516
- **Type**: journal
- **Published**: Dec. 2016
- **Authors**: Lin Yang, Yunyun Liu, Yunming Siu
- **PDF**: https://ieeexplore.ieee.org/document/7567516
- **Abstract**: Sparse code multiple access (SCMA) is a novel non-orthogonal air-interface technology in which several users share a same frequency resource simultaneously. The SCMA decoder is based on a message passing algorithm (MPA) for the sparsity of codeword. In the original MPA, all the users update a message until the maximum number of iterations is reached, resulting in high computational complexity. This letter puts forward a threshold-based MPA, where a belief threshold is applied to control the algorithm process. Simulation results show that the proposed scheme obtains a low computational complexity with only a slight performance degradation when the threshold is set appropriately.

## A Novel Machine-to-Machine Communication Strategy Using Rateless Coding for the Internet of Things

- **Status**: ❌
- **Reason**: Raptor 부호 기반 M2M/IoT 물리계층 네트워크코딩 - rateless/네트워크코딩 응용, 떼어낼 LDPC ECC 기법 없음
- **ID**: ieee:7384685
- **Type**: journal
- **Published**: Dec. 2016
- **Authors**: Boulos Wadih Khoueiry, Mohammad Reza Soleymani
- **PDF**: https://ieeexplore.ieee.org/document/7384685
- **Abstract**: Internet of Things (IoT) is a new paradigm where almost every physical object will be furnished with sensing, communication, and processing capabilities that allow them to communicate with other devices possibly via the internet and/or telecommunication networks. Machine-to-machine (M2M) communication, which is a key enabling technology for the IoT, enables networked devices to exchange information among themselves with minor or no human involvement. In this paper, we propose a novel coding strategy that considerably increases the efficiency of the channel in the multicast setting. Specifically, we consider the scenario where three M2M communication devices that are close by and want to exchange their messages via a low cost relay or another device in proximity. The main advantage of the proposed scheme is twofold: 1) use of joint channel and physical-layer network coding where M2M communication devices simultaneously transmit their messages and 2) no decoding at the relay where relaying can be as simple as amplify and forward or denoise and forward. Simulation results using practical Raptor codes show that the proposed scheme achieves a near-optimal sum rate performance. Furthermore, we propose an efficiently scalable technique for disseminating information among a large number of M2M communication devices.

## Partially Block Markov Superposition Transmission of a Gaussian Source With Nested Lattice Codes

- **Status**: ❌
- **Reason**: Gaussian 소스 JSCC + nested lattice code, LDPC 아님이며 떼어낼 ECC 기법 없음
- **ID**: ieee:7572010
- **Type**: journal
- **Published**: Dec. 2016
- **Authors**: Shancheng Zhao, Xiao Ma
- **PDF**: https://ieeexplore.ieee.org/document/7572010
- **Abstract**: This paper studies the transmission of Gaussian sources through additive white Gaussian noise channels in bandwidth expansion regime, i.e., the channel bandwidth is greater than the source bandwidth. To mitigate the error propagation phenomenon of conventional digital transmission schemes, we propose in this paper a new capacity-approaching joint source channel coding (JSCC) scheme based on partially block Markov superposition transmission (BMST) of nested lattice codes. In the proposed scheme, first, the Gaussian source sequence is discretized by a lattice-based quantizer, resulting in a sequence of lattice points. Second, these lattice points are encoded by a short systematic group code. Third, the coded sequence is partitioned into blocks of equal length and then transmitted in the BMST manner. The main characteristics of the proposed JSCC scheme include: 1) entropy coding is not used explicitly and 2) only parity-check sequence is superimposed, hence, termed partially BMST. This is different from the original BMST. To show the superior performance of the proposed scheme, we present extensive simulation results which show that the proposed scheme performs within 1 dB of the Shannon limits. Hence, the proposed scheme provides an attractive candidate for transmission of Gaussian sources.

## A Novel Method for Soft Error Mitigation in FPGA Using Modified Matrix Code

- **Status**: ❌
- **Reason**: FPGA 소프트에러 완화용 modified matrix code(매트릭스 코드, LDPC 아님), 떼어낼 LDPC ECC 기법 없음
- **ID**: ieee:7553578
- **Type**: journal
- **Published**: Dec. 2016
- **Authors**: Swagata Mandal, Rourab Paul, Suman Sau +2
- **PDF**: https://ieeexplore.ieee.org/document/7553578
- **Abstract**: Field programmable gate arrays (FPGAs) are readily affected by transient faults in the presence of radiation and other environmental hazards compared to application specific integrated circuits. Hence, error mitigation and recovery techniques are necessary to protect the FPGA hardware from soft errors arising from transient faults. In this letter, modified matrix code (MMC) is used for multibit error correction in FPGA-based systems, and dynamic partial reconfiguration is considered to reduce the reconfiguration time. We propose a first of its kind methodology for novel transient fault correction using MMC for FPGAs. To validate the design, the proposed method has been tested on a Kintex FPGA and its performance has been estimated in terms of hardware complexity, power consumption, overhead, and error correction efficiency.

## Coded Network Function Virtualization: Fault Tolerance via In-Network Coding

- **Status**: ❌
- **Reason**: NFV 내 in-network coding 내결함성, 채널 디코딩 분산처리 응용이며 이식할 LDPC 디코더/HW 기법 없음
- **ID**: ieee:7572035
- **Type**: journal
- **Published**: Dec. 2016
- **Authors**: A. Al-Shuwaili, O. Simeone, J. Kliewer +1
- **PDF**: https://ieeexplore.ieee.org/document/7572035
- **Abstract**: Network function virtualization (NFV) prescribes the instantiation of network functions on general-purpose network devices, such as servers and switches. While yielding a more flexible and cost-effective network architecture, NFV is potentially limited by the fact that commercial off-the-shelf hardware is less reliable than the dedicated network elements used in conventional cellular deployments. The typical solution for this problem is to duplicate network functions across geographically distributed hardware in order to ensure diversity. In contrast, this letter proposes to leverage channel coding in order to enhance the robustness on NFV to hardware failure. The proposed approach targets the network function of uplink channel decoding, and builds on the algebraic structure of the encoded data frames in order to perform in-network coding on the signals to be processed at different servers. The key principles underlying the proposed coded NFV approach are presented for a simple embodiment and extensions are discussed. Numerical results demonstrate the potential gains obtained with the proposed scheme as compared to the conventional diversity-based fault-tolerant scheme in terms of error probability.

## SHO-FA: Robust Compressive Sensing With Order-Optimal Complexity, Measurements, and Bits

- **Status**: ❌
- **Reason**: 압축센싱 sparse 행렬 복원 알고리즘 - 채널코딩 ECC 아님, LDPC BP 디코더 이식 기여 없음
- **ID**: ieee:7185441
- **Type**: journal
- **Published**: Dec. 2016
- **Authors**: Mayank Bakshi, Sidharth Jaggi, Sheng Cai +1
- **PDF**: https://ieeexplore.ieee.org/document/7185441
- **Abstract**: Suppose x is any exactly k-sparse vector in Rn. We present a class of sparse matrices A, and a corresponding algorithm that we call short and fast1 (SHO-FA) that, with high probability over A, can reconstruct x from Ax. The SHO-FA algorithm is related to the invertible bloom lookup tables recently introduced by Goodrich et al., with two important distinctions- SHO-FA relies on linear measurements, and is robust to noise. The SHO-FA algorithm is the first to simultaneously have the following properties: 1) it requires only O(k) measurements; 2) the bit precision of each measurement and each arithmetic operation is O (log(n) + P) (here, 2-P corresponds to the desired relative error in the reconstruction of x); 3) the computational complexity of decoding is O(k) arithmetic operations and that of encoding is O(n) arithmetic operations; and 4) if the reconstruction goal is simply to recover a single component of x instead of all of x, with significant probability over A, this can be done in constant time. All the above constants are independent of all problem parameters other than the desired probability of success. For a wide range of parameters, these properties are informationtheoretically order-optimal. In addition, our SHO-FA algorithm works over fairly general ensembles of sparse random matrices, and is robust to random noise and (random) approximate sparsity for a large range of k. In particular, suppose the measured vector equals A(x + z) + e, where z and e correspond to the source tail and measurement noise, respectively. Under reasonable statistical assumptions on z and e, our decoding algorithm reconstructs x with an estimation error of O(||z||2 + ||e||2). The SHO-FA algorithm works with high probability over A, z, and e, and still requires only O(k) steps and O(k) measurements over O(log(n))-bit numbers. This is in contrast to most existing algorithms that focus on the worst case z model, where it is known that Ω(k log(n/k)) measurements over O(log(n))-bit numbers are necessary. Our algorithm has good empirical performance, as validated by simulations.

## An Adaptive Process-Variation-Aware Technique for Power-Gating-Induced Power/Ground Noise Mitigation in MPSoC

- **Status**: ❌
- **Reason**: MPSoC 파워게이팅 P/G 노이즈 완화 - LDPC/ECC와 무관한 전력관리 기법
- **ID**: ieee:7463494
- **Type**: journal
- **Published**: Dec. 2016
- **Authors**: Zhe Wang, Xuan Wang, Jiang Xu +6
- **PDF**: https://ieeexplore.ieee.org/document/7463494
- **Abstract**: Power gating (PG) is one of the most effective techniques to reduce the leakage power in multiprocessor system-on-chips (MPSoCs). However, the power-mode transition during the PG period of an individual processing unit (PU) will introduce serious power/ground (P/G) noise to the neighboring PUs. As technology scales, the P/G noise problem becomes a severe reliability threat to MPSoCs. At the same time, the increasing manufacturing process variations (PVs) also bring uncertainties to the P/G noise problem and make it difficult to predict and mitigate. To tackle this problem, in this paper, we analyze the PG-induced P/G noise in the presence of PVs and propose a hardware–software collaborated runtime technique to adaptively protect PUs from P/G noise. Sensor network-on-chip is used to gather noise information and coordinate different system components. An online PV-aware algorithm is developed to effectively decide the noise impact range and arrange protections for affected PUs based on the collected noise information. We evaluate the proposed technique through cycle-level Monte Carlo simulations of NoC-based MPSoCs in different scales. The experimental results on various realistic applications show that our technique could achieve comparable reliability to the most reliable static technique while improve on average 3.78%–29.5% the system energy efficiency and reduce 15.7%–70.4% the performance penalty on different MPSoC scales.

## Performance evaluation of Underwater Communication system using block codes

- **Status**: ❌
- **Reason**: 수중통신 OFDM에서 표준 LDPC 적용해 BER 개선 확인만, 이식할 신규 ECC 기법 없음
- **ID**: ieee:7893242
- **Type**: conference
- **Published**: 8-9 Dec. 2
- **Authors**: B. Pranitha, L. Anjaneyulu
- **PDF**: https://ieeexplore.ieee.org/document/7893242
- **Abstract**: Underwater Communications (UWC) is a very demanding application in spite of issues like time varying multipath propagation, attenuation of the signal, underwater noise, and interference etc., Orthogonal Frequency Division Multiplexing (OFDM) is a suitable modulation technique for UWC as it has the ability to solve Inter symbol interference (ISI), Inter channel interference (ICI) and also multipath propagation. Bit error rate (BER) versus Signal to noise ratio (SNR) is used as the figure of merit to indicate the performance of the system. In this work it is established that coding at the transmitter in addition to OFDM using Hamming code improves the BER. It is also proved that LDPC code further improves the BER.

## Reliable Quantum LDPC Codes over GF(4)

- **Status**: ❌
- **Reason**: 양자 LDPC over GF(4): 비이진+양자, symplectic 직교성 의존으로 이식 불가
- **ID**: ieee:7849021
- **Type**: conference
- **Published**: 4-8 Dec. 2
- **Authors**: Yixuan Xie, Jinhong Yuan
- **PDF**: https://ieeexplore.ieee.org/document/7849021
- **Abstract**: We propose a method of constructing quantum LDPC codes from multiplicative groups of order p - 1, where p = 4n + 1 is a prime for some positive integer n. The proposed quantum LDPC codes of non-CSS structure are constructed from a pair of classical regular quasi-cyclic (QC) LDPC codes. We show that these classical regular QC-LDPC codes without cycles of length 4 are orthogonal with respect to the symplectic inner product. Moreover, the proposed construction method yields a large number of new quantum LDPC codes with various code lengths and rates. The performance of the proposed quantum LDPC codes over quantum depolarizing channels with an iterative belief-propagation decoding algorithm is evaluated by simulations.

## A Comparison of Channel Coding Schemes for 5G Short Message Transmission

- **Status**: ❌
- **Reason**: 5G 단문 코딩 스킴 비교 서베이성, 신규 LDPC 디코더·구성 기여 없음
- **ID**: ieee:7848804
- **Type**: conference
- **Published**: 4-8 Dec. 2
- **Authors**: Onurcan Iscan, Diego Lentner, Wen Xu
- **PDF**: https://ieeexplore.ieee.org/document/7848804
- **Abstract**: Different coding schemes (Turbo, Polar, binary and non-binary LDPC and tail-biting convolutional codes) which can be potentially used in the next generation mobile communication systems for the short message length regime (message length k < 512) are discussed. Their error correction performances are compared with finite length bounds and the complexities of the corresponding decoders are evaluated in terms of number of basic operations. It is shown that significant performance improvement can be obtained in the short message length regime by replacing the LTE Turbo code with other modern coding schemes, however, at a cost of increased decoder complexity.

## Generalized Belief Propagation Based Deliberate Bit Flipping Modulation Coding

- **Status**: ❌
- **Reason**: GBP 기반 변조 제약 코딩으로 TDMR(자기기록) 2D 제약 특이적, NAND ECC에 떼어낼 일반 디코더 기법 약함
- **ID**: ieee:7841858
- **Type**: conference
- **Published**: 4-8 Dec. 2
- **Authors**: Mohsen Bahrami, Bane Vasic
- **PDF**: https://ieeexplore.ieee.org/document/7841858
- **Abstract**: We propose a novel approach to modulation coding using the Generalized Belief Propagation (GBP) algorithm. The idea is to completely eliminate a constrained encoder and, instead, embed a constraint into an error correction codeword by deliberately flipping the bits that violate the constraint. The GBP algorithm is used to keep the number of flipped bits small in order not to overburden the decoder. We incorporate our method to impose the two-dimensional (2D) no isolated bit constraint on a low-density parity check (LDPC) coded 2D data array. Furthermore, we show that the number of flipped bits can be optimized so that it is not beyond the error correcting capability of the code. Applied to Two Dimensional Magnetic Recording (TDMR) systems, our approach results in an order of magnitude gain in the frame error rate.

## Bit Mapping Design for LDPC Coded BICM Schemes with Binary Physical-Layer Network Coding

- **Status**: ❌
- **Reason**: PNC용 bit mapper/PEG 설계로 무선 BICM 변조 특이적, NAND LDPC ECC에 떼어낼 디코더·코드설계 기법 없음
- **ID**: ieee:7841632
- **Type**: conference
- **Published**: 4-8 Dec. 2
- **Authors**: Junyi Du, Lei Yang, Jinhong Yuan +2
- **PDF**: https://ieeexplore.ieee.org/document/7841632
- **Abstract**: We propose a new low-density parity-check (LDPC) coded binary physical-layer network coding (PNC) scheme for Gaussian two-way relay channels. In this scheme, we introduce a bit mapper between the LDPC encoder and the modulator, which considers the unequal error protections brought by the high order PSK modulations. We add a new bipartite sub-channel graph consisting of sub-channels and variable nodes (VNs) to the Tanner graph and propose a progressive edge growth (PEG) algorithm to design the bit mapper. The design paradigm is to search for the bit mapping distribution with the lowest decoding threshold by using the extrinsic information transfer (EXIT) chart, and then establish the edges progressively between VNs and sub-channels according to the distribution. The proposed PEG algorithm is employed to design the bit mappers of the schemes with 8-PSK, 16-PSK, 64-PSK and 256-PSK. Simulation results show that the proposed schemes can considerably improve the bit error performance of the PNC XOR messages, compared to the schemes without bit mappers.

## A High Performance Joint Detection and Decoding Scheme for LDPC Coded SCMA System

- **Status**: ❌
- **Reason**: SCMA-specific joint detection+decoding; LDPC은 채널부호일 뿐 다중접속 검출에 종속, NAND로 떼어낼 디코더/HW 없음
- **ID**: ieee:7848813
- **Type**: conference
- **Published**: 4-8 Dec. 2
- **Authors**: Kaining Han, Zhenbing Zhang, Jianhao Hu +1
- **PDF**: https://ieeexplore.ieee.org/document/7848813
- **Abstract**: Sparse Code Multiple Access (SCMA) is a promising candidate multiple access technology for the fifth generation (5G) mobile communication system. In this paper, we propose a factor graph based high performance Joint Detection and Decoding scheme (JDD) for the Low Density Parity Check code (LDPC) coded SCMA system. Also, we propose a message damping aided reduced complexity JDD scheme (RC-JDD) to achieve a lower complexity. According to the simulation results, the proposed JDD scheme has 2.6dB Bit Error Rate (BER) performance gain compared with the traditional methods and approximates to the single user detection performance bound with only 0.5dB loss. The RC-JDD scheme has only 10% complexity of JDD scheme with only 0.5dB loss. Thus the proposed RC-JDD scheme can be a good candidate for 5G system.

## A Low Complexity SCMA Decoder Based on List Sphere Decoding

- **Status**: ❌
- **Reason**: SCMA 디코더(MPA/list sphere), 비-LDPC 다중접속 부호 응용으로 제외.
- **ID**: ieee:7841513
- **Type**: conference
- **Published**: 4-8 Dec. 2
- **Authors**: Fan Wei, Wen Chen
- **PDF**: https://ieeexplore.ieee.org/document/7841513
- **Abstract**: Non-orthogonal multiple access is one of the key techniques developed for the future 5G communication systems among which, the recent proposed sparse code multiple access (SCMA) has attracted a lots of researchers' interests. By exploring the shaping gain of the multi-dimensional complex codewords, SCMA is shown to have a better performance compared with some other non-orthogonal schemes such as low density signature (LDS). However, although the sparsity of the codewords makes the near optimal message passing algorithm (MPA) possible, the decoding complexity is still very high. In this paper, we propose a low complexity decoding algorithm based on list sphere decoding. Complexity analysis and simulation results show that the proposed algorithm can reduce the computational complexity substantially while achieve the near maximum likelihood (ML) performance.

## Joint Source-Channel Decoding of Polar Codes for Language-Based Sources

- **Status**: ❌
- **Reason**: polar 코드 JSCC(소스-채널 결합) 언어소스 리스트 디코딩, polar 전용+JSCC라 제외
- **ID**: ieee:7841934
- **Type**: conference
- **Published**: 4-8 Dec. 2
- **Authors**: Ying Wang, Minghai Qin, Krishna R. Narayanan +2
- **PDF**: https://ieeexplore.ieee.org/document/7841934
- **Abstract**: We propose a joint list decoder and language decoder that exploits the redundancy of language- based sources during polar decoding. By judging the validity of decoded words in the decoded sequence with the help of a dictionary, the polar list decoder constantly detects erroneous paths after the decoding of every few bits. This path-pruning technique based on joint decoding has advantages over stand-alone polar list decoding in that most decoding errors in early stages are corrected. We show that if the language structure can be modeled as erasure correcting outer block codes, the rate of inner polar code can be increased while still guaranteeing a vanishing probability of error. To facilitate practical joint decoding, we first propose a construction of a dynamic dictionary using a trie and show an efficient way to trace the dictionary during decoding. Then we propose a joint decoding scheme for polar codes taking into account both information from the channel and the source. The proposed scheme has the same decoding complexity as the list decoding of polar codes. A list-size adaptive joint decoding is further implemented to largely reduce the decoding complexity. Simulation results show that the joint decoding schemes outperform stand-alone polar codes with CRC-aided successive cancellation list decoding by over 0.6 dB.

## Low-Complexity List Successive-Cancellation Decoding of Polar Codes Using List Pruning

- **Status**: ❌
- **Reason**: polar 리스트 SC 디코딩 list pruning, polar 전용 RPM 기반이라 바이너리 LDPC BP에 이식 불가
- **ID**: ieee:7841969
- **Type**: conference
- **Published**: 4-8 Dec. 2
- **Authors**: Ji Chen, YouZhe Fan, ChenYang Xia +4
- **PDF**: https://ieeexplore.ieee.org/document/7841969
- **Abstract**: The performance of List Successive-Cancellation Decoding (LSCD) of Polar Codes with large list size have exceeded that of Turbo codes and Low-Density Parity-Check codes. However, large list size results in huge computation complexity and this limits the applicability of LSCD in high-throughput and power- sensitive applications. In this work, a low complexity design for LSCD with large list size based on list pruning is proposed. In particular, the property of the relative path metric (RPM) of each list candidate with respect to that of the most-likely candidate is investigated. It is found that the correct candidate has a low possibility of having a large value of RPM and based on this property, a list pruning method and the corresponding low-complexity LSCDs are proposed. From the simulation results, as compared to the conventional LSCD, the proposed LSCDs have negligible performance loss while the computation complexity is reduced by more than 80%. In addition, the proposed design is hardware-friendly and easily adaptable to the existing LSCDs hardware architectures.

## Experimental Throughput Analysis in Screen-Camera Visual MIMO Communications

- **Status**: ❌
- **Reason**: 스크린-카메라 VLC throughput 분석이며 비이진 채널코딩 사용, 바이너리 LDPC ECC 기법 없음
- **ID**: ieee:7841827
- **Type**: conference
- **Published**: 4-8 Dec. 2
- **Authors**: Takuya Fujihashi, Toshiaki Koike-Akino, Philip V. Orlik +1
- **PDF**: https://ieeexplore.ieee.org/document/7841827
- **Abstract**: Screen-camera communication, which uses a liquid crystal display (LCD) screen and camera image sensors, has been an attractive variant of visible light communications (VLC) since display and camera have been equipped with in various mobile devices. To improve transmission rates, we investigate the impact of nonlinear channel equalization and nonbinary channel coding as well as high-order modulation schemes. Equalization techniques can reduce the effect of channel impairments, such as color mixing. Nonbinary coding improves reliability of high-order modulation and thus increases the transmission rate. Experimental evaluations using an LCD screen and camera demonstrate that our proposed scheme achieves 3.6-2.4 times higher transmission rates compared to existing schemes for a communication distance of 40-100 cm.

## Dynamics and Steady-State Behavior of Self-Healing Cyber-Physical Networks in Light of Cyber-Node Delays

- **Status**: ❌
- **Reason**: 사이버-물리 네트워크 자가치유 동역학, LDPC/ECC 무관
- **ID**: ieee:7848886
- **Type**: conference
- **Published**: 4-8 Dec. 2
- **Authors**: Ali Behfarnia, Ali Eslami
- **PDF**: https://ieeexplore.ieee.org/document/7848886
- **Abstract**: The interconnected nature of cyber-physical networks gives rise to numerous engineering challenges and opportunities. An important challenge is the propagation of failure from one network to another, that can lead to large-scale cascading failures. On the other hand, the self-healing ability emerges as a valuable opportunity where the overlaying cyber network can cure failures in the underlying physical network. This paper extends an analytical framework established in a previous work to study the interaction of failure propagation and healing in cyber-physical networks. In particular, the case where propagation of failure in the physical network is faster than the healing response of the cyber network is investigated. Such scenarios are of interest in many real-life applications such as smart grid. The analysis results in a closed-form formula that captures the dynamics of failure propagation and healing in the network. In addition, it is shown that as the time goes by, the network reaches a steady state condition that would be either a complete healing or a complete collapse. Extensive numerical results are provided to verify the analysis and investigate the impact of the network parameters on the resiliency of the network. Particularly, it is shown that even small delays in cyber-nodes' response to physical failures may significantly reduce the network resiliency.

## Second-Order Memory Based LT Encoder Design

- **Status**: ❌
- **Reason**: LT 분수부호 인코더(BEC/fountain), 채널 ECC 아님이며 떼어낼 바이너리 LDPC 기법 없음
- **ID**: ieee:7849036
- **Type**: conference
- **Published**: 4-8 Dec. 2
- **Authors**: Luyao Shang, Erik S. Perrins
- **PDF**: https://ieeexplore.ieee.org/document/7849036
- **Abstract**: Increasing communication reliability and decreasing latency is an increasing demand in wireless multihop networks. In this regards, fountain codes have been widely adopted in cooperative transmissions. The Luby transform (LT) code is considered as a fundamental fountain code that is used to improve the performance of the fountain code family. Previous work on LT code design has focused mainly on the degree distribution of the output symbols, leaving the input symbols as being Poisson distributed. It has been proved that by introducing memory to the encoder, the degree distribution of the input symbols can be designed to improve the code performance. However, existing work focuses only on first- order memory based LT encoders (MBLTEs); the performance with higher memory orders is not investigated. Therefore, in this paper we study the second-order MBLTE with the belief propagation (BP) decoder over the binary erasure channel (BEC) and show that it outperforms the first-order MBLTE in terms of the decoder convergence speed, the bit error rate (BER) and the error floor.

## An Analysis of Unified SU-MIMO Channel Model for mmWave Communications

- **Status**: ❌
- **Reason**: mmWave SU-MIMO 채널모델, LDPC/ECC 무관
- **ID**: ieee:7848832
- **Type**: conference
- **Published**: 4-8 Dec. 2
- **Authors**: Alphan Sahin, Hanqing Lou, Li-Hsiang Sun +1
- **PDF**: https://ieeexplore.ieee.org/document/7848832
- **Abstract**: In this study, we propose a unified framework to analyze single-user MIMO (SU-MIMO) for various antenna configurations. The proposed framework is generic enough to capture the polarization issues and consider different phased antenna array (PAA) settings under realistic 3-D deployment scenarios. In particular, we discuss the impact of PAA geometry on the baseband channel characteristics, e.g., power delay profile and channel response, and evaluate the empirical distribution of the orthogonality of the columns of the MIMO channel matrix under the IEEE 802.11ay channel model. We show the impact of the link distance and the orientation of the PAAs on the channel capacity and discuss the factors that affect the MIMO performance, e.g., polarization. Finally, we consider practical radios and compare the open- loop and the closed-loop SU-MIMO schemes with link-level simulations using the proposed channel model.

## Throughput Enhancements on Cellular Downlink Channels Using Rateless Codes

- **Status**: ❌
- **Reason**: rateless 코드 셀룰러 다운링크 throughput 분석, ECC 디코더/구성 기법 없음
- **ID**: ieee:7842327
- **Type**: conference
- **Published**: 4-8 Dec. 2
- **Authors**: Amogh Rajanna, Martin Haenggi
- **PDF**: https://ieeexplore.ieee.org/document/7842327
- **Abstract**: Rateless codes have been shown to provide robust error correction over wireless channels. Using a stochastic geometry model, this paper studies the performance of cellular downlink with packet transmission based on rateless codes. For the case of Rayleigh fading, a novel and accurate approximation is proposed for the distribution of the packet transmission time of rateless codes. The performance of rateless codes is compared to that of fixed rate codes by evaluating the user rate and success probability achievable with the two channel coding schemes. Based on both the proposed analysis and network simulation, the paper shows that rateless coding provides both coverage and throughput gains relative to fixed rate coding, not only for the typical user but for all users in the cellular network.

## Hash Division Multiple Access

- **Status**: ❌
- **Reason**: Hash Division Multiple Access는 PHY 다중접속 기법, LDPC ECC와 무관
- **ID**: ieee:7841868
- **Type**: conference
- **Published**: 4-8 Dec. 2
- **Authors**: Lu Wang, Xiaoke Qi, Kaishun Wu +1
- **PDF**: https://ieeexplore.ieee.org/document/7841868
- **Abstract**: Recent advances in rateless codes facilitate the utilization of dense constellation. By exploiting more constellation points with controlled symbol distance, they ensure higher transmission date rate and better diversity gain against fading. In this paper, we observe that there exists certain redundancy in the existing dense constellation diagram. With proper design, such redundancy can be can be optimized, and exploited to enable a new orthogonal dimension for multiple access. We termed it as hash division multiple access (HDMA). HDMA incorporates a orthogonal, linear and random encoder in PHY layer to construct orthogonal hash space for user separation. An AP-driven MAC protocol is then proposed to fully utilize this transmission concurrency for uplink and downlink multiple access. We verify the feasibility of HDMA via a GNU radio testbed, and further conduct trace-driven simulations to evaluate the multiplexing gain of HDMA. The results reveal that HDMA provides a maximum number of 3 to 5 concurrent transmissions, with performance gain over 131% and 39% compared to 802.11 and AutoMAC.

## Narrowband interference mitigation with LRPC code and OFDM for smart grid applications

- **Status**: ❌
- **Reason**: LRPC(랭크메트릭, GF(q) 벡터공간 디코딩) - 비이진/비-LDPC 부호, 암호용, 떼어낼 바이너리 LDPC 기법 없음
- **ID**: ieee:7843300
- **Type**: conference
- **Published**: 19-21 Dec.
- **Authors**: Abdul Karim Yazbek, Jean-Pierre Cances, Vahid Meghdadi
- **PDF**: https://ieeexplore.ieee.org/document/7843300
- **Abstract**: We investigate the use of Low Rank Parity Check Codes (LRPC), originally designed for cryptography applications in the context of Power Line Communication (PLC). Particularly we propose a new code design and an efficient probabilistic decoding algorithm. The main idea of decoding LRPC codes is based on calculations of vector spaces over a finite field Fq. This family of codes can be seen as the equivalent of classical LDPC codes for the rank metric. We compare the performance of this code against the Reed-Solomon Code (RS) through a PLC channel. We show by simulation that the proposed system outperforms the traditional scheme where the PLC channel is subjected to both impulsive noise and narrowband interference.

## Implementation and performance study of the LDPC coding in the DVB-S2 link system using MATLAB

- **Status**: ❌
- **Reason**: DVB-S2 LDPC+BCH MATLAB BER 성능 평가 - 표준 부호 단순 시뮬레이션, 신규 디코더·구성·HW 기여 없음
- **ID**: ieee:7951982
- **Type**: conference
- **Published**: 19-21 Dec.
- **Authors**: Lamia Fathi Abusedra, Amer Mohamed Daeri, Amer Ragab Zerek
- **PDF**: https://ieeexplore.ieee.org/document/7951982
- **Abstract**: Low Density Parity Check (LDPC) and Bose-Chaudhuri-Hochquenghem (BCH) are channel coding that have been recently developed associated with QPSK, 8PSK, 16APSK, and 32APSK modulations for the system to work properly on the nonlinear satellite channel. The likelihood of either system bit error or block error probability is one of the most commonly used features in modern communication systems. This paper initially introduces the main components used to build a video broadcast digital system model - satellite second generation (DVB-S2). The next part of this work implement's MATLAB Simulink model to use low-density parity check code (LDPC) since it is a key element in this system. Next this paper examines the extent of performance of this application at small set of ModCods with (QPSK) at different values of (ES/No) of energy per symbol noise ratio PSD's. Finally the relationship between (BER) and (ES/No) is presented as the output values obtained by this order.

## A New Parallel Instruction Model Based on Multi-Tasking Bluetooth Communication

- **Status**: ❌
- **Reason**: Bluetooth 멀티태스킹 통신 모델, LDPC/ECC와 무관
- **ID**: ieee:7820545
- **Type**: conference
- **Published**: 16-19 Dec.
- **Authors**: Haiyan Jin, Shaopeng Zhao
- **PDF**: https://ieeexplore.ieee.org/document/7820545
- **Abstract**: For multitasking concurrency problems in Bluetooth communication, a kind of security instruction model is put forward. The model realize multitasking concurrency-safe communication between mobile phone and hardware devices with Bluetooth function. It not only ensures the safety and efficiency of communication, but also good reusability has. This model is pulled out from the actual project and forms a communication reference in different application systems.

## Protograph LDPC-based distributed joint source-channel coding

- **Status**: ❌
- **Reason**: 분산 결합 소스-채널 코딩(DJSCC), LDPC는 베이스라인이고 떼어낼 ECC 디코더/구성 기법 없음
- **ID**: ieee:7833624
- **Type**: conference
- **Published**: 14-16 Dec.
- **Authors**: Shaohua Hong, Lin Wang
- **PDF**: https://ieeexplore.ieee.org/document/7833624
- **Abstract**: This paper proposes a distributed joint source-channel coding (DJSCC) scheme using a single protograph low-density parity-check (P-LDPC) code for the symmetric problem. In the proposed scheme, the distributed source encoder sends the uniformly-spaced information bits together with the parity bits to simultaneously achieve both distributed compression and channel error correction. Moreover, iterative joint decoding is introduced to further exploit the source correlation. Simulation results show that the proposed DJSCC scheme can obtain relatively large additional coding gains and guarantee that the distributed source shows almost the same performance, which is suitable for equal error protection applications.

## Integrating network coding and superposition coding in wireless broadcast networks

- **Status**: ❌
- **Reason**: 무선 브로드캐스트 네트워크코딩+중첩코딩, erasure 채널로 떼어낼 LDPC ECC 기법 없음
- **ID**: ieee:8070216
- **Type**: conference
- **Published**: 10-11 Dec.
- **Authors**: Teng Niu, Dongmei Zhang, Kui Xu +1
- **PDF**: https://ieeexplore.ieee.org/document/8070216
- **Abstract**: Multimedia streaming applications have high throughput requirement and stringent Quality-of-Service (QoS) guarantee. In this paper, we aim at designing a novel transmission and retransmission scheme, which integrates both the Network Coding and the Superposition Coding for wireless video broadcast networks by packet-erasure channel. Specifically, the Scalable Video Coding (SVC) technology is introduced into our model which is perfectly suitable for Superposition Coding (SC) multi-layer modulation. We also propose the transmission architecture of INSC scheme, and explore the suitable SC constellation diagram and the optimal power allocation parameter. Then, we analyze the transmission performance of INSC scheme in bit and packet level. Extensive simulations have been conducted and the simulation results verify that the proposed INSC scheme achieves higher transmission efficiency, lower video distortion in comparison to the conventional SC and NC scheme.
