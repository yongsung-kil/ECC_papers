# IEEE Xplore — 2025-03


## Constraint-Aware Annealing for CMOS-Based Ising Machine LDPC Decoder

- **Status**: ✅
- **Reason**: CMOS 이싱머신 기반 LDPC 디코더용 constraint-aware annealing 스케줄 제안 — LDPC 디코더 HW 아키텍처(D) 범주로 이식 가능성 있음.
- **ID**: ieee:10849655
- **Type**: journal
- **Published**: March 2025
- **Authors**: Eslam Elmitwalli, Zeljko Ignjatovic, Selçuk Köse
- **PDF**: https://ieeexplore.ieee.org/document/10849655
- **Abstract**: Ising machines are efficient hardware solvers for combinatorial optimization problems (COPs). In CMOS-based Ising machines, the annealing process is crucial for efficiently navigating complex energy landscapes in mapped COPs such as Max-Cut and low-density parity-check (LDPC) decoding. QuBRIM, a CMOS-based Ising machine, has recently been utilized to solve LDPC decoding problems using multi-body interactions. A constraint-aware annealing schedule is proposed that increases the efficiency of solving the mapped COP. The proposed annealing method uses knowledge of the LDPC decoding problem to guide the annealing process. The annealing schedule is demonstrated through high-level simulations. The proposed methodology demonstrates a normalized energy efficiency (NEE) of 0.68 pJ/bit/iteration, which is a 1.8x improvement over random bit-flip annealing, and an 80% increase in throughput.

## Novel LDPC Coded Modulation Scheme for Two-User Gaussian Multiple Access Channels

- **Status**: ❌
- **Reason**: 2사용자 가우시안 MAC에서의 LDPC 코딩 변조; 무선 MAC 특화 응용으로 독립 이식 가능한 디코더/코드설계 기법 없음
- **ID**: ieee:10816193
- **Type**: journal
- **Published**: March 2025
- **Authors**: Ryo Shibata, Masato Kawasumi
- **PDF**: https://ieeexplore.ieee.org/document/10816193
- **Abstract**: This letter proposes a novel coded modulation scheme for two-user Gaussian multiple access channels with higher-order modulation based on the concept of delayed bit-interleaved coded modulation. The proposed scheme effectively extracts user information from superimposed signals using previously decoded results. We demonstrate that the sum capacities of the proposed scheme can achieve the theoretical limits, while the decoding thresholds, when using spatially coupled low-density parity-check codes, closely approach these limits, even when both users employ the same constellation, bit labeling, code rate, and average power. Furthermore, we show that the proposed scheme outperforms conventional methods despite reduced complexity.

## Rate-Compatible Length-Scalable Quasi-Cyclic Spatially-Coupled LDPC Codes

- **Status**: ✅
- **Reason**: 3D-G-PEGL 기반 rate-compatible length-scalable QC-SC-LDPC 코드 설계(E); NAND flash 코드 설계에 직접 이식 가능한 PEG·lifting 구성 기법 포함
- **ID**: ieee:10795194
- **Type**: journal
- **Published**: March 2025
- **Authors**: Zhitong He, Kewu Peng, Jian Song
- **PDF**: https://ieeexplore.ieee.org/document/10795194
- **Abstract**: The capability of QC-SC-LDPC codes to be employed in broadcasting systems has been studied in previous research. However, the implementation-oriented features such as rate-compatibility and length-scalability for QC-SC-LDPC codes have not been well studied yet. In this paper, we first propose a new implementation-oriented structure of QC-SC-LDPC codes for broadcasting systems, with support for rate-compatibility and length-scalability. Then, the three-dimensional (3D-) grid-based (G-) progressive edge growth and lifting (PEGL) method is proposed to construct QC-SC-LDPC codes with that structure, which can achieve desirable performance across different code rates and code lengths within the given design complexity. Finally, a family of rate-compatible length-scalable QC-SC-LDPC codes are constructed via the 3D-G-PEGL method, and simulation results demonstrate the effectiveness of that method. Furthermore, the scaling behaviors of QC-SC-LDPC codes are observed from the provided simulation results.

## Bounded-Degree Low-Rank Parity-Check Codes

- **Status**: ❌
- **Reason**: Bounded-degree LRPC 코드는 rank-metric 기반 암호학용 코드로, LDPC 디코더·HW·코드설계 기법이 없고 NAND ECC에 이식 가능한 기법 없음.
- **ID**: ieee:10849629
- **Type**: journal
- **Published**: March 2025
- **Authors**: Ermes Franch, Chunlei Li
- **PDF**: https://ieeexplore.ieee.org/document/10849629
- **Abstract**: Low-rank parity-check (LRPC) codes are the rank-metric analogue of low-density parity-check codes and they found important applications in code-based cryptography. In this paper we investigate a sub-family of LRPC codes, which have a parity-check matrix defined over a subspace  ${\mathcal {V}}_{\alpha,d}=\langle 1,\alpha, \ldots, \alpha ^{d-1} \rangle _{\mathbb {F}_{q}}\subsetneq \mathbb {F}_{q^{m}} $ , where  $\mathbb {F}_{q^{m}}$  is the finite field of  $q^{m}$  elements,  $\alpha \in \mathbb {F}_{q^{m}}$  is an element not in any proper subfield of  $\mathbb {F}_{q^{m}}$ , and d is a positive integer significantly smaller than m. These codes are termed bounded-degree LRPC (BD-LRPC) codes. BD-LRPC codes are the same as the standard LRPC codes of density 2 when the degree  $d=2$ , while for degree  $d\gt 2$  they constitute a proper subset of LRPC codes of density d. Exploiting the structure of  ${\mathcal {V}}_{\alpha,d}$ , the BD-LRPC codes of degree d can uniquely correct errors of rank weight r when  $n-k \geq r + u$  for certain  $u \geq 1$ , in contrast to the condition  $n-k\geq dr$  required for the standard LRPC codes. This underscores the superior decoding capability of the BD-LRPC codes. Moreover, as the code length  $n\rightarrow \infty $ , when  $n/m\rightarrow 0$ , the BD-LRPC codes with a code rate of  $R=k/n$  can be uniquely decodable with radius  $\rho =r/n$  approaching the Singleton bound  $1-R$  by letting  $\epsilon =u/n\rightarrow 0$ ; and when  $n/m$  is a constant, the BD-LRPC codes can have unique decoding radius  $\rho = 1-R-\epsilon $  for a small  $\epsilon $ , allowing for  $\rho \gt (1-R)/2$  with properly chosen parameters. This superior decoding capability is theoretically proved for the case  $d=2$  and confirmed by experimental results for  $d\gt 2$ .

## Layered SEMS Decoding for Non-Binary LDPC-Coded PNC Systems

- **Status**: ❌
- **Reason**: [기준개정:비이진제외] 비이진 LDPC용 layered scaled extended min-sum(LSEMS) 알고리즘 제안 — 비이진 min-sum 변형 디코더로 NAND LDPC ECC에 이식 가능(C/E).
- **ID**: ieee:10829836
- **Type**: journal
- **Published**: March 2025
- **Authors**: Chongchong Su, Peng Kang, Pingping Chen +1
- **PDF**: https://ieeexplore.ieee.org/document/10829836
- **Abstract**: In this letter, a layered scaled extended min-sum (LSEMS) algorithm is proposed to decode non-binary low-density parity-check (LDPC) codes in physical-layer network coding (PNC) systems. The proposed LSEMS algorithm is developed for the joint channel decoding and physical-layer network coding (JCNC) over wireless fading channels. It proposes a sequential update of check nodes to decode the exclusive ORed (XORed) codewords that are generated by the non-binary LDPC codes. The LSEMS algorithm achieves almost the same decoding complexity as the scaled extended min-sum (SEMS) algorithm, while it benefits from much less complexity than the reliability-based layered BP (RLBP) algorithm. Simulation results show that the LSEMS algorithm outperforms the conventional SEMS algorithm by about 0.5 dB in non-binary LDPC-coded PNC for both q-level pulse amplitude modulation (q-PAM) and q-ary phase shift keying (q-PSK) modulations.

## Area-Efficient Non-Binary LDPC Decoder With Column-Wise Trellis Min-Max Algorithm

- **Status**: ❌
- **Reason**: [기준개정:비이진제외] NB-LDPC 디코더용 CW-TMM 신규 알고리즘 + 28nm CMOS HW 구현(D); NB-LDPC는 NAND flash ECC에 직접 이식 가능(C/D)
- **ID**: ieee:10684216
- **Type**: journal
- **Published**: March 2025
- **Authors**: Jeongwon Choe, Youngjoo Lee
- **PDF**: https://ieeexplore.ieee.org/document/10684216
- **Abstract**: Considered a next-generation error-correction solution, non-binary low-density parity-check (NB-LDPC) codes exhibit remarkable correcting capabilities, outperforming binary counterparts for severe channel conditions. However, contemporary decoder designs encounter challenges due to the demanding hardware resources required by their high processing complexity. In this work, we propose a novel column-wise trellis min-max (CW-TMM) algorithm, which significantly reduces the sorter overheads in the existing TMM method without degrading the error-correcting power. We also deploy the message compression to the trellis-based algorithm for effectively reducing hardware costs, even allowing the storage-aware long codes by accommodating large-sized on-chip memories. Through the integration of advanced low-cost optimization schemes together, the prototype CW-TMM decoder in a 28-nm CMOS technology for 4-kB 0.9-rate NB-LDPC codes demonstrates a 54% reduction in on-chip memory size and a 63% decrease in decoding complexity, enhancing the area efficiency by more than 2.4 times than the state-of-the-art approaches.

## Lightweight Joint Coding-Modulation Optical Fiber Communication System for Point Cloud

- **Status**: ❌
- **Reason**: LDPC는 비교 베이스라인(G-PCC+LDPC)으로만 언급; 포인트클라우드 광섬유 통신 결합코딩 논문으로 이식 가능한 ECC 기법 없음
- **ID**: ieee:10666722
- **Type**: journal
- **Published**: March 2025
- **Authors**: Wei Zhang, Zhenming Yu, Hongyu Huang +3
- **PDF**: https://ieeexplore.ieee.org/document/10666722
- **Abstract**: Achieving efficient point cloud (PC) transmission is a fundamental requirement for immersive holographic-type communication. However, traditional optical fiber communication (TOFC), based on separated coding modulation for PC transmission, faces challenges related to massive data transmission and heavy computational resource requirements. To achieve lightweight and efficient PC transmission, we propose and experimentally demonstrate a joint coding-modulation optical fiber communication system for PC transmission (JCMPC). A joint encoding-modulation (JEM) network based on 3D convolution is designed to encode the PC into symbols for transmission directly. At the receiver, a joint decoding-demodulation (JDD) network is used to reconstruct the signals transmitted through the communication channel into the received PC. The experimental results indicate that the proposed JCMPC outperforms transmission schemes based on separate coding modulation and exhibits gradual performance degradation with the deterioration of channel conditions. We evaluate the decoding computational complexity of our proposed JCMPC scheme against the separate transmission schemes using Geometry-based Point Cloud Compression (G-PCC) and Low-Density Parity-Check (LDPC) codes. The results demonstrate that JCMPC reduces the decoding computational operations by over 80% compared to G-PCC+LDPC.

## LDPC Codes for Quantitative Group Testing With a Non-Binary Alphabet

- **Status**: ❌
- **Reason**: 양적 그룹 테스팅(group testing)용 LDPC 기반 스킴으로, 채널 ECC 디코더·코드설계 기법이 아니며 NAND LDPC ECC에 이식할 기법 없음.
- **ID**: ieee:10872965
- **Type**: journal
- **Published**: March 2025
- **Authors**: Mgeni Makambi Mashauri, Alexandre Graell i Amat, Michael Lentmaier
- **PDF**: https://ieeexplore.ieee.org/document/10872965
- **Abstract**: We propose and analyze a novel scheme based on LDPC codes for quantitative group testing. The key underlying idea is to augment the bipartite graph by introducing hidden non-binary variables to strengthen the message-passing decoder. This is achieved by grouping items into bundles of size q within the test matrix, while keeping the testing procedure unaffected. The decoder, inspired by some works on counter braids, passes lower and upper bounds on the bundle values along the edges of the graph, with the gap between the two shrinking with the decoder iterations. Through a density evolution (DE) analysis and finite length simulations, we show that the proposed scheme significantly outperforms its binary counterpart with limited increase in complexity.

## BANQ: BayesOpt-Based Automatic Non-Uniform Quantization for SCL Polar Decoding

- **Status**: ✅
- **Reason**: Polar SCL 디코더용 비균일 양자화(NUQ)를 BayesOpt로 자동 설계하며, 5G LDPC min-sum 디코딩에도 적용 검증 — LLR 양자화 기법이 NAND LDPC 디코더에 이식 가능(C).
- **ID**: ieee:10839357
- **Type**: journal
- **Published**: March 2025
- **Authors**: Yutai Sun, Houren Ji, Yuwei Zeng +2
- **PDF**: https://ieeexplore.ieee.org/document/10839357
- **Abstract**: Successive cancellation list (SCL) polar decoding is well-known for its outstanding error correction performance. To achieve a better balance between performance and complexity in SCL decoders, non-uniform quantization (NUQ) is commonly employed. NUQ strategically adjusts the quantization steps to improve the decoder’s performance within specific bitwidth constraints. However, existing NUQ schemes rely on the designers’ expertise and lack an automated design methodology. To address this issue, this letter formulates the NUQ optimization problem and solves it using Bayesian-optimization (BayesOpt), resulting in an automated NUQ scheme termed BANQ. Utilizing BayesOpt to fine-tune the quantization steps, BANQ empowers the SCL decoder to deliver enhanced error correction performance with comparable complexity. For a  $(512,410)~5$ G polar code, compared to uniform quantization (UQ), BANQ cuts bitwidth by 20% and bit operations (BOPs) by 19.5%, achieving near floating-point accuracy. Furthermore, a case study verifies that BANQ can be effectively adapted for 5G LDPC min-sum decoding.

## Rate Matching and Interleaving Hardware Sharing Design for Wireless Terminal in Internet of Vehicles

- **Status**: ❌
- **Reason**: 4G/5G/6G 인터리버 HW 공유 설계로 LDPC는 4종 코드 중 하나로만 언급; 독립적으로 이식할 LDPC 디코더/코드 설계 기법 없음
- **ID**: ieee:10742908
- **Type**: journal
- **Published**: March 2025
- **Authors**: Wei Chen, Kejia Huo, Zhuhua Hu +1
- **PDF**: https://ieeexplore.ieee.org/document/10742908
- **Abstract**: Reducing the power consumption of baseband chips in wireless terminals of the Internet of Vehicles (IoV) is a great challenge. Among them, the rate matching and interleaving hardware module occupies a significant portion of power consumption in the baseband chip, so it is of great significance to design a low power rate matching and interleaving hardware. The interleavers used in 4G LTE and 5G NR/ 6G have not been merged into a single architecture. It is possible to use the same hardware for different communication standards to reduce hardware resources and power consumption. This paper studies the rate matching and block interleaving of turbo codes, convolutional codes, polar codes, and LDPC codes used in 4G LTE and 5G NR/ 6G communication links. With regard to the different algorithms for these four types of encoding, the sharing design is carried out on the hardware structure. In this experiment, according to the proposed storage and interleaving sharing scheme for hardware design and hardware implementation, the memory area of 0.1 μm2 and power consumption overhead of 4.33 mW are obtained based on the SMIC 28 nm process and the operating frequency of 50 MHZ. This achieves the maximum hardware reuse of four encoding schemes in the downlink communication link of 4G LTE and 5G NR/ 6G, and reduces power consumption.

## Adaptive Semantic Generation and NOMA-Based Interference-Aware Transmission for 6G Networks

- **Status**: ❌
- **Reason**: 6G 시맨틱 통신 + NOMA 기반 전송; 소스-채널 결합 통신, LDPC ECC 기법 없음
- **ID**: ieee:10818533
- **Type**: journal
- **Published**: March 2025
- **Authors**: Yuna Yan, Lixin Li, Xin Zhang +3
- **PDF**: https://ieeexplore.ieee.org/document/10818533
- **Abstract**: Existing deep learning-based semantic communication (DeepSC) systems are typically trained for specific single-channel condition, which restricts the overall adaptability and resilience to interference. To address this limitation, we propose an innovative semantic adaptive feature extraction (SAFE) network that dynamically generates and fuses multiple sub-semantics, each characterized by unique features that can be tailored to different channel conditions. This paper also introduces three advanced learning algorithms to refine and enhance the generated sub-semantics, optimizing the semantic successive refinement performance of the SAFE network. Furthermore, we integrate a novel interference-aware semantic transmission method based on non-orthogonal multiple access (NOMA) into this framework. This approach enables users to adaptively select appropriate subsets for efficient transmission and image reconstruction, tailored to the prevailing channel interference conditions. Through extensive simulation experiments, we demonstrate the framework’s capability to generate and transmit semantics under diverse channel interference scenarios adaptively, and verify the effectiveness through both objective and subjective quality evaluations.

## A Critical-Set-Based Multi-Bit Successive Cancellation List Decoder for Polar Codes: Algorithm and Implementation

- **Status**: ❌
- **Reason**: Polar 코드 SCL 디코더 HW 설계; LDPC 관련 없음
- **ID**: ieee:10738838
- **Type**: journal
- **Published**: March 2025
- **Authors**: Shan Cao, Shan Chen, Limin Jiang +1
- **PDF**: https://ieeexplore.ieee.org/document/10738838
- **Abstract**: With the evolution of wireless communication systems, there is a growing demand for high reliability and low latency in channel coding, particularly in 5G and beyond wireless systems used in applications such as autonomous driving and remote medical services. For the decoding of polar codes, the multi-bit successive cancellation list (MSCL) decoding technique was recently introduced to decrease the decoding latency by decoding several short inner codes in parallel, which preserves high reliability compared to the conventional successive cancellation list (SCL) decoding. However, as parallelism increases, the complexity of the decoding path sorting also increases significantly, which makes it resource-intensive for hardware implementation. To address this issue, this paper proposes a configurable critical-set-based multi-bit successive cancellation list (CS-MSCL) decoding algorithm, which first introduces critical sets to the MSCL decoding for the optimization of path pruning. Subsequently, an enhanced CS-MSCL algorithm is introduced for large list-size MSCL decoding, which can boost the error correction performance. Then, an area-efficient decoding architecture is introduced, which supports the cyclic redundancy check (CRC) and the CS-MSCL decoding compatible with the 5G standard. The proposed decoder is implemented in SMIC 40 nm CMOS technology with a parallelism degree of 8, which has a peak area efficiency of  $4.64~\mathrm {Gbps/mm^{2}}$  for list size 4 and  $2.01~\mathrm {Gbps/mm^{2}}$  for list size 8. Compared to state-of-the-art SCL-based decoders, the normalized area efficiency is improved by 7.16% and 17.54% for list sizes 4 and 8, respectively.

## Comparative Assessment of Physical Layer Performance: ATSC 3.0 vs. 5G Broadcast in Laboratory and Field Tests

- **Status**: ❌
- **Reason**: ATSC 3.0 vs 5G Broadcast 물리계층 성능 비교; LDPC가 주제 아님, 이식 가능한 ECC 기법 없음
- **ID**: ieee:10763425
- **Type**: journal
- **Published**: March 2025
- **Authors**: Sunhyoung Kwon, Seok-Ki Ahn, Sungjun Ahn +7
- **PDF**: https://ieeexplore.ieee.org/document/10763425
- **Abstract**: This paper presents a comparative analysis of the physical layer performance of ATSC 3.0 and 3GPP 5G Broadcast through comprehensive laboratory and field tests. The study evaluates various reception scenarios, including fixed and mobile environments and various channel conditions, such as additive white Gaussian noise and mobile channels. Key performance metrics such as threshold of visibility (ToV) and erroneous second ratio (ESR) are measured to assess the reception quality of each standard. The results demonstrate that ATSC 3.0 generally outperforms 5G Broadcast due to its advanced bit-interleaved coded modulation and time interleaving techniques, effectively mitigating burst errors in mobile channels.

## Deterministic Patterns for Multiple Access With Latency and Reliability Guarantees

- **Status**: ❌
- **Reason**: K-반복 코딩·Steiner System 기반 다중접속 패턴 연구; LDPC 미언급, 이식 가능한 ECC 기법 없음
- **ID**: ieee:10684228
- **Type**: journal
- **Published**: March 2025
- **Authors**: Radosław Kotaba, Roope Vehkalahti, Čedomir Stefanović +2
- **PDF**: https://ieeexplore.ieee.org/document/10684228
- **Abstract**: We study a scenario in which multiple uncoordinated devices aim to achieve reliable transmissions within a given time frame. The devices are intermittently active and access a shared pool of channel resources in a grant-free manner by utilizing multiple transmissions (K-repetition coding). This allows them to achieve diversity and improve the reliability within a certain latency constraint. We focus on two access methods: one where devices choose K slots at random and another one where the access patterns are deterministic and follow a specific code design, namely the Steiner System. We analyze the problem under two signal models that involve different complexity for the receiver. First, collision model is considered, where only interference-free transmissions can be used and combined. Second, a model treating interference as noise is analyzed, where the receiver is capable of utilizing all K replicas, applying maximum ratio combining (MRC). For both signal models, we investigate receivers with and without successive interference cancellation (SIC). We develop approximations and bounds for the outage probabilities that very closely match simulation results. Overall, we show that deterministic access patterns have the potential to significantly outperform random selection in terms of reliability. Furthermore, deterministic access patterns offer a simplified system design.

## Protecting the CCSDS 123.0-B-2 Compression Algorithm Against Single-Event Upsets for Space Applications

- **Status**: ❌
- **Reason**: 위성 FPGA상 CCSDS 압축 알고리즘 SEU 내성 기법; ECC/LDPC와 무관
- **ID**: ieee:10785575
- **Type**: journal
- **Published**: March 2025
- **Authors**: Daniel Báscones, Francisco García-Herrero, Óscar Ruano +3
- **PDF**: https://ieeexplore.ieee.org/document/10785575
- **Abstract**: Hyperspectral imaging is an excellent tool to remotely analyze the Earth from in-orbit devices. Satellites capture these images containing vast information about the ground pixels. To optimize storage and transmission speeds, compression is often performed onboard the satellite. To that end, algorithms such as the CCSDS 123.0-B-2 are implemented on FPGAs, enabling this process in an efficient and fast manner. Single-Event Upsets (SEU) are commonplace in this scenario, e.g. bit flips in the FPGA’s configuration memory which can catastrophically alter the algorithm’s output. In this paper, we propose a fault tolerance technique for this specific case. The compression core is checked periodically by running a golden model designed to excite the full internal datapath based on a synthetic image. A failure in this check will trigger a reconfiguration of the compression core. Results show better detection rates than Dual Modular Redundancy (DMR) at a fraction of the resource cost, proving this technique as a viable alternative. Furthermore, other algorithms with similar processing flows might benefit as well from this technique.

## Cholesky Precoded Faster Than Nyquist Signalling with High Compression

- **Status**: ❌
- **Reason**: FTN 신호용 Cholesky 프리코딩 논문이며 LDPC는 성능 평가용 베이스라인 코드로만 사용, 이식 가능한 LDPC 기법 없음
- **ID**: ieee:10983598
- **Type**: conference
- **Published**: 6-9 March 
- **Authors**: Shubham Paul, Nambi Seshadri, R. David Koilpillai
- **PDF**: https://ieeexplore.ieee.org/document/10983598
- **Abstract**: Developing equalizers for Faster- Than-Nyquist (FTN) signals presents a significant challenge, and precoding offers a low-complexity alternative. In particular, employing a Cholesky factorization-based precoding enables us to achieve a symbol-by-symbol maximum likelihood decoding. Existing literature has established constraints on the FTN compression as a function of roll-off factors. This paper presents the feasibility of exceeding these conventional FTN compression limits while employing Cholesky precoding and ML decoding for FTN signals with small block sizes. Furthermore, it is shown that the bandwidth expansion is minimal in these precoded systems. Simulation results of the error performance of the precoded FTN system with Low-Density Parity Check (LDPC) codes are presented.

## Comparisons of Verification-based Decodings for Nonbinary Codes in Error and Error-Erasure Channels

- **Status**: ❌
- **Reason**: [기준개정:비이진제외] 비이진 부호 verification-based 디코딩 비교+error-erasure 채널, 이식 가능 디코더 알고리즘(C)
- **ID**: ieee:10987681
- **Type**: conference
- **Published**: 5-7 March 
- **Authors**: Usana Tuntoolavest, Yosita Tinjunchay, Peerawat Changchaisri +2
- **PDF**: https://ieeexplore.ieee.org/document/10987681
- **Abstract**: Recently, new algorithms on verification-based decoding for codes with nonbinary symbols have been proposed. Namely, there are 1) Vector Symbol Decoding (VSD) that corrects only the data part, 2) hard-decision Message Passing (hMP) that uses a group common idea and 3) limited complexity VSD for partial retransmission ARQ. This paper compares them in terms of their decoding time and decoding performance in various error channels and an error-erasure channel. Symbol error rates (SER) for these channels are necessary and are reported for the 32-bit symbol case. Results show that while VSD: correct data only has the best performance in all channels, hMP group common has the least decoding time and better performance than limited complexity VSD in error channels. The idea of converting erasures to errors is investigated in comparison with the previous idea of converting errors to erasures. Results show that VSD: correct data only is still the best for any overhead. Other methods give good performance for different ranges of overhead.

## Analysis of Rate Adaptation Algorithms in 5G D2D Wireless Link

- **Status**: ❌
- **Reason**: 5G D2D MAC 레이어 rate adaptation 알고리즘 — LDPC/ECC 무관
- **ID**: ieee:10960922
- **Type**: conference
- **Published**: 4-6 March 
- **Authors**: M Joseph Auxilius Jude, K Kodeeswari, N Mohamed Riyas +2
- **PDF**: https://ieeexplore.ieee.org/document/10960922
- **Abstract**: In wireless devices, device-to-device (D2D) links between users are what allow data transmission. A number of factors, including platform noise, interference, and environmental noise might influence 5G D2D communication between devices. In order to get around this, the rate adaptation algorithm of the MAC layer which selects appropriate modulation techniques and dynamically adjusts the data rate based on the prevailing medium conditions to optimize communication efficiency and minimize transmission errors. Depending on the level of noise, each of these seven RAAs dynamically alter the various transmission bits per second. Seven rate adaptation methods are used in D2D communication to select the best modulation scheme. While the data rate varies, the RAA is selected depending on the conditions of the channel and other variables. To improve the effectiveness of data transmission, the seven RAAs selected the best one. For varying SNR values, we choose different modulation techniques. However, additional bits might be transmitted if the SNR improved even just slightly. To address this problem, seven RAAs are implemented under two parametric circumstances. Every node gets subjected to mobility conditions, which include adjusting the device's rate of movement and monitoring the RAA implementation. Out of a total of seven RAAs, the most effective one is selected by applying the following parametric conditions in different types, which boost device throughput while decreasing effectiveness and packet loss.

## Dependable Static PPM Code Using LDPC Code

- **Status**: ✅
- **Reason**: PPM 압축(소스코딩) 맥락이나 LDPC 후보 다중 디코딩 기법 제안 — 소스코딩 제외 대상이라 애매, Phase 3 재검토 위해 살림
- **ID**: ieee:11012791
- **Type**: conference
- **Published**: 29-31 Marc
- **Authors**: Masato Kitakami, Masahiko Suzuki
- **PDF**: https://ieeexplore.ieee.org/document/11012791
- **Abstract**: In recent years, with the increasing amount of data processed by computers, data compression technology is used to reduce data traffic and storage requirements. However, compressed data is vulnerable to errors. To address this issue, various data compression methods with error correction functions have been proposed. Among these error-correcting codes, LDPC code is notable for achieving a rate very close to the Shannon limit, the theoretical upper bound of information transmission. In this research, we propose a method to improve error correction capability when encoding data compressed by Static PPM, an extension of PPM compression, allowing partial decompression using LDPC codes. When large errors occur, Error correcting codes fail to correct them. However, this method can present multiple candidates, including large errors, during decoding. This allows the correct error to be selected from the candidates.

## Bi-Evaluated Chase-Like Decoding for QC-MDPC Code

- **Status**: ✅
- **Reason**: QC-MDPC용 bit-flipping 변형 디코더(Chase-like, NUPC 기반 사전 플립) — NAND LDPC에 이식 가능한 디코더 알고리즘(C)
- **ID**: ieee:11012775
- **Type**: conference
- **Published**: 29-31 Marc
- **Authors**: Takuzo Hirata, Haruhiko Kaneko
- **PDF**: https://ieeexplore.ieee.org/document/11012775
- **Abstract**: This paper presents a decoding algorithm for quasi-cyclic moderate-density parity-check (QC-MDPC) code. The method flips certain positions beforehand, and then a decoder for QC-MDPC code is executed. This process repeats if decoding fails. The positions to be flipped are determined using the number of unsatisfied parity checks (NUPCs) and $\beta$, which is the sum of NUPCs in suspicious positions after tentatively flipping a position. The proposed method is applied to a variant of bit-flipping (BF), and the block error rate (BLER) is evaluated through computer simulation. The result shows that the proposed method significantly reduces the BLER of the BF variant.

## Efficient FPGA Implementation of a High- Performance, Low-Complexity LDPC Decoder for Next-Gen Communication Systems

- **Status**: ✅
- **Reason**: QC-LDPC 구조+병렬 Min-Sum+파이프라인 FPGA 디코더 — NAND LDPC ECC HW 아키텍처로 직접 이식 가능(D, 코드설계 E)
- **ID**: ieee:11031516
- **Type**: conference
- **Published**: 27-28 Marc
- **Authors**: M. Paramaiyappan, S.Palanivel Rajan
- **PDF**: https://ieeexplore.ieee.org/document/11031516
- **Abstract**: Modern communication systems rely on Low- Density Parity-Check (LDPC) decoders to provide reliable error correction for wireless networks of the next generation including 5G as well as satellite communications and Internet of Things (IoT). The research brings forth a real- time optimized implementation of a high-performance low-complexity LAPC decoder designed for FPGAs. The proposed architecture combines QC-LDPC code structures with parallel Min-Sum decoding and pipeline processing to reduce power usage and latency while maintaining high decoding precision. The FPGA hardware shows a Binary Error Rate (BER) measurement of 3.2 × 10–3 when the Signal-to-Noise Ratio (SNR) reaches 2.5 dB and achieves overall 98.6% decoding precision. The proposed decoder design reaches 3.85 Gbps throughput which is better than GPU-based systems by 20% while maintaining 7.8 µs latency for real-time applications. The implemented FPGA system operates at a low power level below 4.80W which exceeds the power requirements of GPU-based systems. The successful outcomes prove that FPGA-based LDPC decoders work as both power-efficient and fast communication system solutions. The designed solution demonstrates scalability and adaptability which constitutes a dependable framework to meet requirements of changing wireless communication standards.

## LUT-Optimized Decoding of QC-LDPC Codes for Flash Memory with EoL Layers Variation Model

- **Status**: ✅
- **Reason**: NAND flash QC-LDPC 디코더 최적화(RCQ 디코더, LUT 양자화, EoL read threshold 조정) — 카테고리 A/C 직접 부합
- **ID**: ieee:10977875
- **Type**: conference
- **Published**: 26-28 Marc
- **Authors**: Yury A. Zamaraev, Vasiliy S. Usatyuk, Sergey I. Egorov
- **PDF**: https://ieeexplore.ieee.org/document/10977875
- **Abstract**: NAND flash memory is a pivotal technology in contemporary data storage, but its reliability diminishes due to retention noise and wear-out effects. This paper proposes a novel decoding optimization for Quasi-Cyclic Low-Density Parity-Check (QC-LDPC) codes tailored for NAND flash memory. The methodology incorporates Lookup Table (LUT)-based reconstruction and quantization, complemented by adaptive read threshold adjustments at the End-of-Life (EoL) stage. Key contributions include a Reconstruction Computation Quantization (RCQ) decoder, which achieves reduced computational and routing complexity through a two-stage optimization process, and a dynamic read threshold adjustment mechanism addressing layer-to-layer variation to improve error correction under evolving threshold voltage distributions. Simulation results demonstrate enhanced reliability and performance, with improvements in Raw Bit Error Rate (RBER) of over 0.004 and a throughput-to-area ratio increase of up to 16%. Additionally, the proposed approach extends the endurance of TLC 3D NAND memory by over 30% at a fixed error probability compared to single-layer model and 12% compared to the Neural Network model. This work offers a step forward in improving SSD reliability at the EoL stage.

## Accelerate QC-LDPC FEC for High-Throughput 5G/6G Wireless & Satellite on CPU and GPU SDRs

- **Status**: ✅
- **Reason**: QC-LDPC layered min-sum 디코더의 SIMD/GPU 고처리량 구현·메모리 최적화 — 이식 가능한 HW/디코더 기법(C/D)
- **ID**: ieee:10977910
- **Type**: conference
- **Published**: 26-28 Marc
- **Authors**: Vasiliy S. Usatyuk, Sergey I. Egorov
- **PDF**: https://ieeexplore.ieee.org/document/10977910
- **Abstract**: This paper presents a high-throughput decoding method for quasi-cyclic low-density parity-check (QC-LDPC) codes, optimized for both CPU and GPU-based Software-Defined Radios (SDRs). The approach leverages a SIMD data alignment architecture that minimizes cache misses and is designed to take full advantage of modern CPUs and GPUs with rich registers and caches. An innovative decoding algorithm is introduced, exploiting the SIMD capabilities of contemporary CPUs to enhance parallelism, while optimizing memory access patterns to align SIMD operations and minimize branching and cache misses on AMD EPYC CPUs (2xEPYC-9754). This results in significant throughput improvements. The method is further extended to GPUs, utilizing their large-scale parallelism through efficient use of registers and local memory. To maximize performance, a memory-efficient check node decoding strategy is employed, ensuring that operations fit within the cache of the Streaming Multiprocessors (SM) to reduce memory access overhead. Simulation results demonstrate the effectiveness of this approach: the CPU-based 8-iteration layered min-sum decoder with early termination achieves coded bit throughputs of up to 72.9 Gbps for 16200-bit codes and 50.9 Gbps for 64800-bit DVB-S2 QC-LDPC codes. On GPUs, the decoder reaches 132 Gbps for short 802.11n Wi-Fi 1944-bit codes and 22.3 Gbps for 5G Base Graph 1 26112-bit codes on an NVIDIA RTX 4090. For 6G prototype QC-LDPC codes, the proposed 3-layer design achieves up to 76 Gbps for 1920-bit codes, with surpassing 104 Gbps on the NVIDIA RTX 5090. Compared to the open-source AFF3CT CPU framework, the proposed method offers 5 to 12 times higher throughput across various code lengths. Even when AFF3CT is optimized with MIPP intrinsics, the new decoder provides 3.2 to 5.7 times better throughput. The GPU implementation delivers up to 120 times the speed of previously published results and offers 13 to 40 times improvement over older GPUs like the GTX 1080 Ti and Titan X, scaling effectively with modern GPUs like the RTX 4090. This approach establishes new performance benchmarks for QC-LDPC decoding, positioning it as an ideal solution for next-generation 5G/6G wireless and satellite communications.

## Flattening Images Manifold at the Nishimori Point: Exploring Linearity in Polysemantic Embedding for Human-Aware Bayesian CNN Image Classification

- **Status**: ❌
- **Reason**: 그래프 스펙트럼 임베딩 기반 이미지 분류 — LDPC ECC와 무관, 떼어낼 기법 없음
- **ID**: ieee:10977938
- **Type**: conference
- **Published**: 26-28 Marc
- **Authors**: Vasiliy S. Usatyuk, Denis A. Sapozhnikov, Sergey I. Egorov
- **PDF**: https://ieeexplore.ieee.org/document/10977938
- **Abstract**: Efficient image classification often requires a balance between accuracy and computational complexity. In this paper, we propose a graph-based spectral embedding method that leverages improved Nishimori temperature estimation to achieve low-dimensional feature representations while maintaining high classification performance. Our approach reduces image features extracted by MobileNetV2 to a 32-dimensional manifold using graph embeddings, significantly decreasing the parameter count compared to conventional methods like bottleneck ResNet-18. On the ImageNet10 dataset, the proposed method achieved 98% accuracy with only 32 dimensions, while on the ImageNet-100 dataset, it matched the performance of a 64-dimensional bottleneck layer using half the dimensionality. Furthermore, with polysemantic multigraph embeddings exceeding 64 dimensions, the method demonstrated a 1.5% accuracy improvement. The computational efficiency, achieved by reducing parameters from 51200 to 3200, highlights the potential of this method for resource-constrained applications. These results demonstrate that the proposed graph-based embedding framework is a scalable and effective solution for image classification tasks, offering a compelling alternative to conventional deep learning architectures. Future work will extend this approach to coarsely quantized feature extracting, improved discriminators, Diffusions and Transformers neural networks.

## Boosting DNN Efficiency: Replacing FC Layers with Graph Embeddings for Hardware Acceleration

- **Status**: ❌
- **Reason**: LDPC를 DNN FC층 대체 그래프 임베딩으로 사용 — 채널코딩 ECC가 아니며 이식 가능한 디코더/코드설계 기법 없음
- **ID**: ieee:10977895
- **Type**: conference
- **Published**: 26-28 Marc
- **Authors**: Vasiliy S. Usatyuk, Sergey I. Egorov
- **PDF**: https://ieeexplore.ieee.org/document/10977895
- **Abstract**: Fully connected (FC) layers present a significant bottleneck in the throughput of Convolutional Neural Networks (CNNs) and Transformers when deployed on hardware accelerators such as FPGAs, ASICs, and analog AI chips. This paper proposes a novel approach to mitigate this limitation by replacing FC layers with sparse graph embedding techniques derived from Low-Density Parity-Check (LDPC) codes, enabling robust weight compression. Using VGG16 as a case study, we demonstrate that our method reduces the parameters in the FC layers from 123,642,856 to just 64,000-a 1,931-fold reduction-while maintaining high-precision classification performance. Following aggressive pruning (72% weight reduction), our LDPC-based embeddings, combined with 8-bit fixed-point quantization, achieve an accuracy of 70.21%, compared to 70.89% achieved by unpruned float32. On the Xilinx Alveo U50 platform, this translates to processing up to 1119 images per second with parallel computation of 64-dimensional embeddings. Moreover, by replacing the top FC layers with the proposed graph embedding method and leveraging fast analog feature extraction (via supervised or random projections), our approach demonstrates the potential to achieve peak performance on the Alveo U50 of 4.8 million images per second for float32 100-class classification and 39.86 million images per second for 10-class classification using 16-bit fixed-point representation. These findings underscore the capability of graph embeddings to significantly enhance DNN efficiency on data center and resource-constrained edge AI hardware platforms. We hypothesize that exploiting the inherent sparsity of graph embeddings, combined with the energy efficiency of analog computation for feature extraction, can yield substantial reductions in CNN, Transformer and Diffusion DNN inference power consumption, potentially surpassing GPU efficiency by three to four orders of magnitude. This paper presents preliminary results and outlines directions for future research to validate this hypothesis.

## Multi-Hypothesis based Distributed Video Coding using Error-Correction Decoder Feedback

- **Status**: ❌
- **Reason**: 분산 비디오 코딩(DVC)에서 ECC 디코더 피드백 활용 — LDPC가 베이스라인이고 떼어낼 디코더/HW/코드설계 기법 없음
- **ID**: ieee:10977881
- **Type**: conference
- **Published**: 26-28 Marc
- **Authors**: Karam Mahfod, Andrei Belitsckiy, Evgeny Belyaev
- **PDF**: https://ieeexplore.ieee.org/document/10977881
- **Abstract**: This paper is dedicated to Distributed Video Coding (DVC) which allows to shift the encoding complexity to the decoder side. We consider DVC architecture, where a side information (SI), which is needed for the error-correction decoder, are selected from multiple hypothesis obtained from set of different traditional and deep learned frame interpolation algorithms. First, we show that the interpolation algorithms could provide different quality of SI depending on a motion model, i.e. the SI averaging proposed in earlier works is not efficient. Therefore, for each bit plane we propose to select the best SI from the available set of hypothesis using feedback of the error-correction decoder: the best hypothesis corresponds to successful error-correction decoding with minimum syndrome bits received from the encoder. Second, in contrast to the previous approaches, we modified the correlation noise model (CNM), so that each bit plane can be processed with the variance obtained from different frame interpolators allowing for more precise noise modeling. Experimental results demonstrate that comparing with DVC with a single frame interpolator this adaptive selection strategy offering significant bitrate savings and gain in peak signal-to-noise ratio (PSNR), particularly in sequences with complex motion and varying group of picture (GOP) lengths.

## Spatially Coupled 5G LDPC Codes via Superposition

- **Status**: ✅
- **Reason**: 공간결합 LDPC와 적응형 슬라이딩윈도 디코딩(ASWD) 알고리즘 — SC-LDPC 코드설계(E)·디코더(C) 이식 가능
- **ID**: ieee:10978794
- **Type**: conference
- **Published**: 24-27 Marc
- **Authors**: Jiayi Yang, Qianfan Wang, Zhiyuan Tan +2
- **PDF**: https://ieeexplore.ieee.org/document/10978794
- **Abstract**: We propose in this paper to enhance the 5G low-density parity-check (LDPC) codes by transmitting the codewords in a block Markov superposition transmission (BMST) manner, resulting in a class of spatially coupled LDPC codes. We present a generalized extrinsic information transfer (EXIT) chart for performance analysis, showing that the decoding thresholds can be improved by increasing the memory size (coupled width) $m$. However, for m > 1, the receiver requires a relatively large window size for the sliding window decoding (SWD) algorithm, potentially causing unacceptable decoding latency. To address this issue, we propose an adaptive sliding window decoding (ASWD) algorithm, in which the decoding window size depends on the decoding state of the BMST system. The proposed EXIT chart analysis can also effectively guide the setting of the maximum decoding window in the ASWD algorithm, as well as the setting of the superposition fractions for the BMST-5G-LDPC system. Simulation results show that: 1) the ASWD algorithm can effectively reduce the average decoding window size in the medium to high signal-to-noise ratio (SNR) region, without the performance loss compared to the conventional SWD algorithm; 2) the proposed BMST-5G-LDPC code can achieve about 0.4, 0.5 and 1.7 dB performance gains compared to the 5G LDPC code over the AWGN channel, the fast fading channel, and the quasi-static block fading channel, respectively.

## Packet Superposition HARQ Scheme Enabled by LDPC Coupled Codes

- **Status**: ✅
- **Reason**: LDPC coupled code 기반 HARQ 패킷중첩, 전용 LDPC 행렬 결합 설계 — 코드설계 관점 살림(E, 애매하여 in)
- **ID**: ieee:10978369
- **Type**: conference
- **Published**: 24-27 Marc
- **Authors**: Yiyun Jian, Lukasz Lopacinski, Eckhard Grass
- **PDF**: https://ieeexplore.ieee.org/document/10978369
- **Abstract**: In this paper, we propose an improved Hybrid Automatic Repeat reQuest (HARQ) scheme based on cross-packet superposition retransmission by employing dedicated low-density parity-check (LDPC) matrices. Simulation results demonstrate that the scheme improves Bit Error Rate (BER) and Packet Error Rate (PER) performance up to 0.4 dB at the cost of increased packet handling complexity. The key element of our system is the combination of the systematic part of a codeword with the parity part of another codeword without any reductions in the code rate. Thus, to some extent, retransmission can be performed without any need to send additional parity bits.

## Mixed Gamma Approximation for Check Node Updates in Density Evolution of LDPC Codes

- **Status**: ✅
- **Reason**: 밀도진화 검사노드 갱신용 Mixed Gamma 근사 — LDPC 부호 설계·최적화 직접 기여(E)
- **ID**: ieee:10978371
- **Type**: conference
- **Published**: 24-27 Marc
- **Authors**: Ziyang Wu, Jian Jiao, Yaosheng Zhang +3
- **PDF**: https://ieeexplore.ieee.org/document/10978371
- **Abstract**: To assist the design and optimization of low-density parity-check (LDPC) codes via density evolution (DE) on binary input additive white Gaussian noise (BIAWGN) channels, we propose a novel mixed Gamma approximation (MGA) scheme to obtain more accurate distribution of messages updated and output by the check nodes during DE iterations. Firstly, we highlight the inaccuracy of existing Gaussian approximation (GA) methods in approximating the distribution of check node output messages, especially when the messages from variable nodes are small with high probability (i.e. low signal-to-noise ratio), and the check nodes have a large degree, which leads to inexact results in GA methods. Then, we establish the MGA scheme by utilizing the statistical properties of Gamma distribution and combine it with GA, which outperforms the existing GA methods in the metrics of error of output mean and Kullback-Leibler (KL) divergence of output distribution for a wide range of parameters. Simulation and analysis validate that our MGA scheme has the potential for the design and optimization of LDPC codes, which can provide adequately accurate estimation of check node outputs with moderate complexity for a variety of approximation methods, such as Gaussian capacity approximation, and significantly reduce the computational complexity by sacrificing minor accuracy.

## Machine Learning-Based Tail Sequence Detection in LDPC-Coded Space Transmissions

- **Status**: ❌
- **Reason**: LDPC 디코딩 중 메트릭을 ML로 분석해 tail 시퀀스를 검출하는 우주통신 특이적 응용 — NAND ECC로 떼어낼 디코더/HW/코드설계 기법 없음
- **ID**: ieee:10978413
- **Type**: conference
- **Published**: 24-27 Marc
- **Authors**: Massimo Battaglioni, Rebecca Giuliani, Franco Chiaraluce +1
- **PDF**: https://ieeexplore.ieee.org/document/10978413
- **Abstract**: In the context of space communications, as per the recommendation from the Consultative Committee for Space Data Systems regarding TeleCommand synchronization and coding, the Communications Link Transmission Unit is composed of a start sequence, coded data, and a tail sequence, which might be optional depending on the employed error correcting code. The task of detecting the tail sequence must be handled along with that of decoding the codewords containing the transmitted data, and this poses some challenges. In this paper, we propose a machine learning model for recognizing the tail sequence based on the analysis of metrics calculated during decoding, when the transmission is coded with Low-Density Parity-Check (LDPC) codes. The model is trained on data produced by an iterative decoder, commonly used in LDPC decoding, with noisy (random) codewords or the noisy tail sequence as inputs. We report the results of some preliminary experiments showing that this approach is capable of achieving very high levels of accuracy using multiple classifiers.

## Learning to Decode Non-Binary LDPC Codes

- **Status**: ❌
- **Reason**: [기준개정:비이진제외] 비이진 LDPC용 neural min-sum 디코더, 짧은 girth 보정·CN 업데이트 가중치 학습 — 이식 가능 디코더 알고리즘(C)이자 비이진 코드(E)
- **ID**: ieee:10978743
- **Type**: conference
- **Published**: 24-27 Marc
- **Authors**: Yujie Tian, Xinyi Sui, Zhongwei Si
- **PDF**: https://ieeexplore.ieee.org/document/10978743
- **Abstract**: We propose a neural min-sum (MS) decoder for non-binary LDPC codes by applying deep learning to the decoding with short to moderate code lengths. In this algorithm, the iterations are unfolded into hidden layers of the neural network, and trainable weights are added to the check node updates to mitigate the correlation in the message passing due to short girths in the Tanner graph. To avoid gradient vanishing and to converge faster, we adopt an iterative training mechanism for parameter tuning. Furthermore, we investigate the impact of girth distribution on the proposed neural MS decoder, which reveals the reasons for the expected performance improvement. Numerical results in terms of bit error rate are provided, which show that the neural MS decoder achieves significant gains for decoding non-binary LDPC codes.

## Multi-Block UAMP Detection for AFDM Under Fractional Delay-Doppler Channel

- **Status**: ❌
- **Reason**: AFDM 분수 지연-도플러 채널 UAMP 신호검출, LDPC 무관 메시지패싱 검출기
- **ID**: ieee:10978213
- **Type**: conference
- **Published**: 24-27 Marc
- **Authors**: Jin Xu, Zijian Liang, Kai Niu
- **PDF**: https://ieeexplore.ieee.org/document/10978213
- **Abstract**: Affine Frequency Division Multiplexing (AFDM) is considered as a promising solution for next-generation wireless systems due to its satisfactory performance in high-mobility scenarios. By adjusting AFDM parameters to match the multi-path delay and Doppler shift, AFDM can achieve two-dimensional time-frequency diversity gain. However, under fractional delay-Doppler channels, AFDM encounters energy dispersion in the affine domain, which poses significant challenges for signal detection. This paper first investigates the AFDM system model under fractional delay-Doppler channels. To address the energy dispersion in the affine domain, a unitary transformation based approximate message passing (UAMP) algorithm is proposed. The algorithm performs unitary transformations and message passing in the time domain to avoid the energy dispersion issue. Additionally, we implemented block-wise processing to reduce computational complexity. Finally, the empirical extrinsic information transfer (E-EXIT) chart is used to evaluate iterative detection performance. Simulation results show that UAMP significantly outperforms Gaussian approximate message passing (GAMP) under fractional delay-Doppler conditions.

## Design of Spreading Sequences for Lattice-Coded Based Multiple Access

- **Status**: ❌
- **Reason**: 격자부호 기반 다중접속(LCMA)용 spreading sequence 설계 — LDPC와 무관, 떼어낼 ECC 기법 없음
- **ID**: ieee:10978594
- **Type**: conference
- **Published**: 24-27 Marc
- **Authors**: Jinsong Wang, Tao Yang, Yiyu Yin
- **PDF**: https://ieeexplore.ieee.org/document/10978594
- **Abstract**: It was shown that by operating over the integer linear combinations (ILCs) of $K$ users' messages, lattice-code based multiple-access (LCMA) offers increased system load and improved error-rate performance over non-lattice based schemes. This paper advances the existing LCMA system by designing the spreading sequences. We first formulate the spreading sequences optimization problem based on the achievable symmetric rate of LCMA. To solve this problem, we develop three new methods, namely target-switching steepest descent (TS-SD), particle swarm (PS) optimization, and Hadamard concatenation (HC). The TS-SD method always targets on the ILC with the lowest computation rate in the SD process. The PS method treats the spreading matrix as a particle and iteratively updates a swamp of particles' positions and velocities, based on the relative distance to the best position that are currently known. To further reduce the complexity, we first obtain a solution in a lower dimension, and then apply Hadamard concatenation (HC) which yields a solution for the required dimension. The PS and HC methods are shown to approach the capacity of the MA channel.

## Energy-Efficient LDPC Acceleration in Open Radio Access Networks Using DRL and QRF

- **Status**: ✅
- **Reason**: FPGA LDPC 디코더 가속 + DRL 오프로딩/에너지효율 — HW 디코더 가속 관점 이식 가능(D)
- **ID**: ieee:10978275
- **Type**: conference
- **Published**: 24-27 Marc
- **Authors**: Aerman Tuerxun, Akihiro Nakao
- **PDF**: https://ieeexplore.ieee.org/document/10978275
- **Abstract**: In the evolving landscape of Open Radio Access Networks (O-RAN), achieving both high energy efficiency and computational acceleration is crucial for optimizing network performance. Low-Density Parity-Check (LDPC) decoding, a computationally intensive process widely used in wireless communication, is commonly accelerated by hardware to meet the stringent demands of real-time processing. However, balancing this acceleration with energy efficiency remains a significant challenge. In this paper, we propose a Deep Reinforcement Learning (DRL)-based smart offloading strategy to achieve low-latency, energy-efficient LDPC acceleration using an FPGA-based hardware accelerator. We introduce a Quantile Regression Forest (QRF)-based method for predicting latency and energy consumption in real time, enabling per-block decision-making, alongside a Proximal Policy Optimization (PPO)-based algorithm for dynamically adapting offloading weights to optimize energy efficiency. The proposed strategy is implemented on the OpenAir-Interface5G (OAI) and FlexRIC platforms to demonstrate its feasibility within an O-RAN testbed. Evaluation results show that the method adapts dynamically to varying network conditions in under 5 seconds, making offloading decisions in less than 5 µs, resulting in up to 20% energy savings and 14% latency reduction.

## SOVA Decoded Serially Concatenated Continuous Phase Modulations with Binary Markov Source

- **Status**: ❌
- **Reason**: SOVA 기반 SCCPM(CPM+RSC) 디코딩, Markov 소스정보 활용 — LDPC 아니고 떼어낼 ECC 기법 없음
- **ID**: ieee:10971460
- **Type**: conference
- **Published**: 22-30 Marc
- **Authors**: Zhijie Guo, Lei Cao
- **PDF**: https://ieeexplore.ieee.org/document/10971460
- **Abstract**: We investigate a method to utilize source memory information for a Soft-Output Viterbi algorithm (SOVA) decoded Serially Concatenated Continuous Phase Modulation (SCCPM) system. The system concatenates a recursive systematic convolutional (RSC) code with a binary full-response continuous phase modulation (CPM) signal. We apply the SOVA as the Soft-Input Soft-Output (SISO) decoder for both the CPM and RSC components. We modify the RSC SOVA decoder to combine the a priori information provided by the CPM SOVA decoder with the a priori information from a Markov source. Simulation results show that incorporating source statistics information improves the error performance of the SCCPM system and accelerates decoding convergence during iterative decoding.

## A Self-Correcting Minimum Sum Algorithm with Dual Reliability

- **Status**: ✅
- **Reason**: DRD-SCMS — Self-Correcting Min-Sum 변형 신규 신뢰도 판정, 이식 가능 디코더 알고리즘(C)
- **ID**: ieee:11009386
- **Type**: conference
- **Published**: 21-23 Marc
- **Authors**: Zhaochuan Wei, Xiaoqian Zhou, Yuanfa Ji +1
- **PDF**: https://ieeexplore.ieee.org/document/11009386
- **Abstract**: In order to improve the performance and reliability of Low-Density Parity-Check (LDPC) code decoding algorithms, this paper proposes a Self-Correcting Minimum Sum algorithm with Dual Reliability Determination (DRD-SCMS) to address the limitations of the Self-Correcting Minimum Sum (SCMS) algorithm in determining the reliability of variable nodes. Unlike the traditional SCMS algorithm, which relies solely on the symbols from the previous and current iterations to assess the reliability of variable nodes, the DRD-SCMS algorithm combines the number of connections between variable nodes and check nodes with check failures, along with the results of symbol iterations, to provide a more accurate reliability evaluation. By categorizing variable nodes into three groups and prioritizing the updating of the most unreliable nodes, the algorithm optimizes the iteration order in the decoding process. Simulation results demonstrate that the DRD-SCMS algorithm significantly reduces the number of iterations and improves decoding efficiency compared to the SCMS algorithm, offering better applicability and reliability.

## Performance Analysis of Normalized Min-Sum Decoder for LDPC using non-uniform Quantization

- **Status**: ✅
- **Reason**: 정규화 min-sum 디코더에 비균일 양자화를 적용해 복잡도 감소·error floor 개선 — 이식 가능 디코더/양자화 기법(C). NAND LLR 양자화와 직결.
- **ID**: ieee:11004875
- **Type**: conference
- **Published**: 20-22 Marc
- **Authors**: Pargunarajan K, Gandhiraj R, Jayakumar M
- **PDF**: https://ieeexplore.ieee.org/document/11004875
- **Abstract**: Very high data rates and decoding computational complexity place strict constraints in 5G and 6G communications. In this paper, non-uniform Quantized Decoding algorithm is proposed for Low-density Parity Check codes (LDPC). In the proposed algorithm, the check node updating process is carried out using quantization, which reduces complexity. The Sum Product Algorithm (SPA) is iterative message passing decoding techniques offer the optimal performance for LDPC codes. Implementations use message-passing decoding with more precision, results extremely high complexity. In Iterative, message-passing (MP), trapping sets and absorbing sets causes low error floor. In this article non-uniform quantization proposed to overcome dynamic range of values over uniform quantization. Simulation results provide coding gain increases closer to of 0.5 dB in higher SNR and has good error floor at 10−5.

## Sparse parity random linear codes for URLLC in channels with memory

- **Status**: ✅
- **Reason**: MacKay-Neal LDPC 기반 sparse random linear code의 GRAND-MO/매칭퍼슈잇 디코딩 — 바이너리 sparse 부호용 디코더 기법, 이식 가능성(C) 애매하여 살림
- **ID**: ieee:10944695
- **Type**: conference
- **Published**: 19-21 Marc
- **Authors**: Steven Jones, A. Brinton Cooper
- **PDF**: https://ieeexplore.ieee.org/document/10944695
- **Abstract**: The use of short error-correcting codes is vital for achieving an Ultra-Reliable Low Latency Communications capability for supporting the Internet of Things with minimal decoding complexity. Here we examine the performance and decoding complexity of two code-agnostic decoders for a new class of full-rank sparse random linear codes derived from the MacKay-Neal LDPC construction. We consider decoding by a noise guessing decoder such as GRAND-MO and by a binary matching pursuit decoder to which list decoding is added. Comparisons are made in the context of error correction performance and computational complexity.

## SOGRAND Decoding of Non-binary Product Codes

- **Status**: ❌
- **Reason**: 비이진(확장체) 곱부호 SOGRAND 디코딩 — non-binary 부호로 즉시 제외
- **ID**: ieee:10944696
- **Type**: conference
- **Published**: 19-21 Marc
- **Authors**: Lukas Rapp, Muriel Médard, Ken R. Duffy
- **PDF**: https://ieeexplore.ieee.org/document/10944696
- **Abstract**: Non-binary product codes are matrices with entries in an extension field, where the rows and columns are protected by linear non-binary component codes. As with binary product codes, non-binary product codes can be decoded via turbo product decoding and are referred to as turbo product codes (TPCs). This paper assesses the performance of non-binary TPCs with the recently developed soft-input soft-output GRAND decoder (SOGRAND). Owing to the more accurate soft output, decoding of non-binary TPCs with SOGRAND outperforms existing turbo product decoders. We demonstrate that non-binary TPCs can also provide a better block error rate performance than a selection of low-density parity-check (LDPC) codes found in the 5G New Radio standard. This extends the design space of TPCs beyond binary TPCs, demonstrating their potential as a viable alternative to LDPC codes. Empirical results show that non-binary TPCs converge in fewer iterations than binary TPCs of the same size. We show TPCs that converge with up to three times fewer decoding iterations than the corresponding LDPC code from the 5G New Radio standard. This indicates they hold promise for low-latency, high-throughput applications.

## Turbo product decoding of cubic tensor codes

- **Status**: ❌
- **Reason**: 입방 텐서 곱부호 turbo product 디코딩, LDPC 대안 제시이며 LDPC에 이식할 디코더/구성 기법 아님
- **ID**: ieee:10944669
- **Type**: conference
- **Published**: 19-21 Marc
- **Authors**: Sarah Khalifeh, Ken R. Duffy, Muriel Médard
- **PDF**: https://ieeexplore.ieee.org/document/10944669
- **Abstract**: Long, powerful soft detection forward error correction codes are typically constructed by concatenation of shorter component codes that are decoded through iterative Soft-Input Soft-Output (SISO) procedures. The current gold-standard is Low Density Parity Check (LDPC) codes, which are built from weak single parity check component codes that are capable of producing accurate SO. Due to the recent development of SISO decoders that produce highly accurate SO with codes that have multiple redundant bits, square product code constructions that can avail of more powerful component codes have been shown to be competitive with the LDPC codes in the 5G New Radio standard in terms of decoding performance while requiring fewer iterations to converge. Motivated by applications that require more powerful low-rate codes, in the present paper we explore the possibility of extending this design space by considering the construction and decoding of cubic tensor codes.

## Channel Decoding from Multiple Looks Under Receiver Impairments

- **Status**: ❌
- **Reason**: 수신기 클럭 지터 보상용 ML 디코더; LDPC 부호·디코더 기법 아님, NAND 이식성 없음
- **ID**: ieee:10944726
- **Type**: conference
- **Published**: 19-21 Marc
- **Authors**: Bo Guan, Dennis L. Goeckel
- **PDF**: https://ieeexplore.ieee.org/document/10944726
- **Abstract**: Receiver impairments play a significant role in determining system performance, particularly in adversarial environments subject to intentional jamming that seek to impair operation by collapsing the dynamic range of the receiver. Clock jitter is one of the key impairments that limits analog-to-digital (A/D) converters, and it causes significant challenges for channel decoding as it distorts the received signal’s timing, making compensation difficult. Motivated by this challenge, we consider performance and design for the two-look channel, which utilizes two receivers with independent clock jitter. Using a statistical characterization of the jitter, we derive the degree to which mutual information is increased in the two-look scenario versus the case when a single receiver is employed. This analysis motivates the consideration of optimal decoder design, but this is complicated by the nonlinear timing jitter model. Hence, we turn to a machine learning (ML)-based decoding framework. Numerical results demonstrate the improvement in mutual information from having two looks, and simulation results demonstrate the improved channel decoding performance.

## Code Design in Almost Lossless Onion Peeling Data Compression

- **Status**: ❌
- **Reason**: Slepian-Wolf 분산 소스 압축(onion peeling)에 LDPC 소스코딩 사용 — 채널코딩 ECC 아님(소스 코딩 제외)
- **ID**: ieee:10992554
- **Type**: conference
- **Published**: 18-21 Marc
- **Authors**: Siming Sun, Michelle Effros
- **PDF**: https://ieeexplore.ieee.org/document/10992554
- **Abstract**: Onion peeling codes address a distributed data compression scenario related to Slepian-Wolf (SW) data compression. In a 2-user onion peeling code, as in a 2-user SW code, two dependent sources are compressed independently; while the SW code decodes both sources jointly using both source descriptions, the onion peeling code reconstructs the first source using only the first source description and then uses the first source reconstruction and the second source description to reconstruct the second source. The authors' prior results show that first-stage compressors that are almost identical in first-source reconstruction reliability and efficiency can exhibit extremely different best-case performance for the second source. This paper proposes the use of low density parity check (LDPC) source coding in the first stage of an onion peeling code and shows that, with high probability, the random LDPC code design used in the evaluation of this approach generates a first-stage code that performs well both in compressing the first source and in assisting the compressor of the second source. The method works universally for any conditional distribution on the second source given the first, meaning that one does not have to know the conditional distribution of the second source given the first to design a first-stage code with good performance on the second source.

## Research on Non Direct Sight Infrared Laser Scattering Communication Technology in IoT Applications

- **Status**: ❌
- **Reason**: NLoS 적외선 레이저 산란 통신 기술 — LDPC/ECC 무관, 떼어낼 디코더/HW/코드설계 기법 없음
- **ID**: ieee:10968842
- **Type**: conference
- **Published**: 14-16 Marc
- **Authors**: Lingwei Wang, Fuyu Zhu, Hua Wang
- **PDF**: https://ieeexplore.ieee.org/document/10968842
- **Abstract**: This study delves into non line of sight (NLoS) infrared laser atmospheric scattering communication technology in the Internet of Things (IoT) environment. By constructing precise signal transmission models and developing efficient signal encoding and decoding techniques, efficient and stable data transmission under non line of sight conditions has been achieved. This article also discusses the potential applications of this technology in IoT fields such as smart cities and emergency rescue, providing new communication solutions for it.

## Enhancing Emerging Trends in Underwater Acoustic Communication Systems with Queuing Models

- **Status**: ❌
- **Reason**: 수중음향통신 큐잉 모델, LDPC/ECC 기법 자체가 없음
- **ID**: ieee:11076535
- **Type**: conference
- **Published**: 12-14 Marc
- **Authors**: T. Deepa, S. Maragathasundari, K. Karthikeyan +1
- **PDF**: https://ieeexplore.ieee.org/document/11076535
- **Abstract**: Underwater acoustic communication (UAC) plays a crucial role in applications such as oceanographic data collection, underwater sensing, and unmanned vehicle operations. However, challenges such as limited bandwidth, variable propagation conditions, and high delays hinder its performance. This study explores how advanced signal processing techniques and emerging communication technologies can enhance UAC systems. Through experimental evaluations, the proposed models demonstrate significant improvements in packet arrival rates, reduced transmission delays, and minimized network congestion. Performance metrics such as queue length, delay, and throughput are analyzed, with results showing a increase in throughput and a reduction in delay compared to conventional methods. These findings highlight the potential of innovative communication techniques in improving the efficiency and reliability of UAC systems.

## Spiking Neural Belief Propagation Decoder for LDPC Codes with Small Variable Node Degrees

- **Status**: ✅
- **Reason**: 스파이킹 신경망 기반 BP 디코더(ML-ELENA-SNN), 바이너리 LDPC용 새 디코더 알고리즘 — C 이식 가능
- **ID**: ieee:10949115
- **Type**: conference
- **Published**: 10-13 Marc
- **Authors**: Alexander von Bank, Eike-Manuel Edelmann, Jonathan Mandelbaum +1
- **PDF**: https://ieeexplore.ieee.org/document/10949115
- **Abstract**: Spiking neural networks (SNNs) promise energyefficient data processing by imitating the event-based behavior of biological neurons. In previous work, we introduced the enlarge-likelihood-each-notable-amplitude spiking-neural-network (ELENA-SNN) decoder, a novel decoding algorithm for low-density parity-check (LDPC) codes. The decoder integrates SNNs into belief propagation (BP) decoding by approximating the check node (CN) update equation using SNNs. However, when decoding LDPC codes with a small variable node (VN) degree, the approximation gets too rough, and the ELENASNN decoder does not yield good results. This paper introduces the multi-level ELENA-SNN (ML-ELENA-SNN) decoder, which is an extension of the ELENA-SNN decoder. Instead of a single SNN approximating the CN update, multiple SNNs are applied in parallel, resulting in a higher resolution and higher dynamic range of the exchanged messages. We show that the ML-ELENASNN decoder performs similarly to the ubiquitous normalized min-sum decoder for the $(38400,30720)$ regular LDPC code with a VN degree of $d_{v}=3$ and a CN degree of $d_{\mathrm{c}}=15$.

## Soft-Decision Decoding for LDPC Code-Based Quantitative Group Testing

- **Status**: ❌
- **Reason**: 양자 그룹 테스팅용 LDPC BP 디코더 — 채널코딩 ECC가 아닌 group testing 검출 문제로 NAND 이식 기법 없음
- **ID**: ieee:10949110
- **Type**: conference
- **Published**: 10-13 Marc
- **Authors**: Marvin Xhemrishi, Johan Östman, Alexandre Graell i Amat
- **PDF**: https://ieeexplore.ieee.org/document/10949110
- **Abstract**: We consider the problem of identifying defective items in a population with non-adaptive quantitative group testing. For this scenario, Mashauri et al. recently proposed a low-density parity-check (LDPC) code-based quantitative group testing scheme with a hard-decision decoding approach (akin to peeling decoding). This scheme outperforms generalized LDPC code-based quantitative group testing schemes in terms of the misdetection rate. In this work, we propose a belief-propagationbased decoder for quantitative group testing with LDPC codes, where the messages being passed are purely soft. Through extensive simulations, we show that the proposed soft-information decoder outperforms the hard-decision decoder Mashauri et al..

## A Comparative Study of Ensemble Decoding Methods for Short Length LDPC Codes

- **Status**: ✅
- **Reason**: 짧은 LDPC용 ensemble 디코딩(MBBP/AED/SED/NED/SBP) 비교 - 이식 가능 BP 개선 디코더(C)
- **ID**: ieee:10949101
- **Type**: conference
- **Published**: 10-13 Marc
- **Authors**: Felix Krieg, Jannis Clausius, Marvin Rübenacke +1
- **PDF**: https://ieeexplore.ieee.org/document/10949101
- **Abstract**: To alleviate the suboptimal performance of belief propagation (BP) decoding of short low-density parity-check (LDPC) codes, a plethora of improved decoding algorithms has been proposed over the last two decades. Many of these methods can be described using the same general framework, which we call ensemble decoding: A set of independent constituent decoders works in parallel on the received sequence, each proposing a code-word candidate. From this list, the maximum likelihood (ML) decision is designated as the decoder output. In this paper, we qualitatively and quantitatively compare different realizations of the ensemble decoder, namely multiple-bases belief propagation (MBBP), automorphism ensemble decoding (AED), scheduling ensemble decoding (SED), noise-aided ensemble decoding (NED) and saturated belief propagation (SBP). While all algorithms can provide gains over traditional BP decoding, ensemble methods that exploit the code structure, such as MBBP and AED, typically show greater performance improvements.

## Soft Reverse Reconciliation for Discrete Modulations

- **Status**: ❌
- **Reason**: CV-QKD 연속변수 양자키분배 reconciliation softening — 양자·보안 응용 특이적, LDPC는 베이스라인, 떼어낼 ECC 기법 없음
- **ID**: ieee:10949121
- **Type**: conference
- **Published**: 10-13 Marc
- **Authors**: Marco Origlia, Marco Secondini
- **PDF**: https://ieeexplore.ieee.org/document/10949121
- **Abstract**: The performance of the information reconciliation phase is crucial for quantum key distribution (QKD). Reverse reconciliation ($\mathbf{R R}$) is typically preferred over direct reconciliation (DR) because it yields higher secure key rates. However, a significant challenge in continuous-variable (CV) QKD with discrete modulations (such as QAM) is that Alice lacks soft information about the symbol decisions made by Bob. This limitation restricts error correction to hard-decoding methods, with low reconciliation efficiency. This work introduces a reverse reconciliation softening (RRS) procedure designed for CVQKD scenarios employing discrete modulations. This procedure generates a soft metric that Bob can share with Alice over a public channel, enabling her to perform soft-decoding error correction without disclosing any information to a potential eavesdropper. After detailing the RRS procedure, we investigate how the mutual information between Alice's and Bob's variables changes when the additional metric is shared. We show numerically that RRS improves the mutual information with respect to RR with hard decoding, practically achieving the same mutual information as DR with soft decoding. Finally, we test the proposed RRS for PAM-4 signalling with a rate $\mathbf{1 / 2}$ binary LDPC code and bit-wise decoding through numerical simulations, obtaining more than 1dB SNR improvement compared to hard-decoding RR.

## On the Design and Performance of Machine Learning Based Error Correcting Decoders

- **Status**: ✅
- **Reason**: ML/transformer 기반 FEC 디코더(ECCT, CrossMPT)와 OSD 성능 비교 분석 — 이식 가능 디코더 알고리즘 평가, C 관련
- **ID**: ieee:10949122
- **Type**: conference
- **Published**: 10-13 Marc
- **Authors**: Yuncheng Yuan, Péter Scheepers, Lydia Tasiou +3
- **PDF**: https://ieeexplore.ieee.org/document/10949122
- **Abstract**: This paper analyzes the design and competitiveness of four neural network (NN) architectures recently proposed as decoders for forward error correction (FEC) codes. We first consider the so-called single-label neural network (SLNN) and the multi-label neural network (MLNN) decoders which have been reported to achieve near maximum likelihood (ML) performance. Here, we show analytically that SLNN and MLNN decoders can always achieve ML performance, regardless of the code dimensions-although at the cost of computational complexityand no training is in fact required. We then turn our attention to two transformer-based decoders: the error correction code transformer (ECCT) and the cross-attention message passing transformer (CrossMPT). We compare their performance against traditional decoders, and show that ordered statistics decoding outperforms these transformer-based decoders. The results in this paper cast serious doubts on the application of NN-based FEC decoders in the short and medium blocklength regime.

## Construction of Low-Rate LDPC Codes from Rate-1/2 CCSDS Standard LDPC Codes

- **Status**: ✅
- **Reason**: CCSDS rate-1/2에서 PBRL로 저레이트 LDPC 구성, error floor 회피 — 이식 가능 바이너리 코드 설계(E)
- **ID**: ieee:11068439
- **Type**: conference
- **Published**: 1-8 March 
- **Authors**: Semira Galijasevic, Linfang Wang, Jon Hamkins +2
- **PDF**: https://ieeexplore.ieee.org/document/11068439
- **Abstract**: The existing Consultative Committee for Space Data Systems (CCSDS) standard uses low-density parity-check (LDPC) codes for higher code rates including 1/2, 2/3, and 4/5, supporting message block lengths of 1024,4096, and 16384. For lower code rates, the CCSDS standard uses turbo codes, providing rates of 1/3, 1/4 and 1/6 and supporting message block lengths of 1784, 3568, and 16384. However, the frame error rate (FER) performance of the turbo codes shows an error floor where the slope of frame error rate curve begins to flatten between FERs of 10–3 and 10-5. The resulting FER performance is undesirable for certain space applications. This paper uses the Protograph-Based Raptor-Like (PBRL) approach to provide new lower LDPC code rates of 1/3,1/4 and 1/6 for the existing LDPC message lengths of 1024,4096, and 16384 that are rate-compatible with the existing CCSDS rate-1/2 LDPC codes and do not suffer from an error floor (at least above FER 10–7).

## Fast Software Implementation of a CCSDS LDPC Encoder

- **Status**: ❌
- **Reason**: CCSDS LDPC 인코더 소프트웨어 고속화(CPU 매핑) — 인코더 최적화만, 디코더/코드설계 새 기여 없음
- **ID**: ieee:11068497
- **Type**: conference
- **Published**: 1-8 March 
- **Authors**: N.J. Wei, N.B. Chen, E. Grayver
- **PDF**: https://ieeexplore.ieee.org/document/11068497
- **Abstract**: The CCSDS LDPC codes are used by NASA and other space agencies in modern transceivers. These codes were designed to be easy to decode by ensuring the parity check matrix is sparse. However, the encoding requires multiplication by a non-sparse generator matrix. The encoder can be efficiently mapped to an FPGA by exploiting the high level of parallelism. All published work on the CCSDS LDPC encoders describes FPGA implementations. With the almost universal acceptance of software defined radio (SDR) in modern ground stations, the LDPC codec must be implemented in software operating on standard CPUs. The authors encountered a counter-intuitive situation where the decoder operates faster than the encoder when implemented in software. This surprising result is mainly due to the availability of highly optimized software decoders, and lack of such optimized encoders. This paper provides an in-depth discussion of mapping the encoder to a modern CPU. The optimized encoder achieves over 100x higher throughput than the fastest open-source version.
