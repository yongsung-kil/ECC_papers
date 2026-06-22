# IEEE Xplore — 2015-10


## Design and Analysis of Bit-Interleaved Coded Modulation With Pseudorandom Sequence

- **Status**: ❌
- **Reason**: BICM-P 변조 기법 + density evolution으로 LDPC 최적화하나 무선 변조 응용 특이적, 떼어낼 신규 디코더/코드설계 기법 없음
- **ID**: ieee:6948239
- **Type**: journal
- **Published**: Oct. 2015
- **Authors**: Zhiyong Chen, Hui Liu, Bin Xia
- **PDF**: https://ieeexplore.ieee.org/document/6948239
- **Abstract**: In this paper, we design and analyze an improved bit-interleaved coded modulation (CM) scheme with a pseudorandom sequence (BICM-P). For the proposed scheme, the pseudorandom sequence is introduced into a systematic encoder at the transmitter and serves as side information at the receiver. With this design, the receiver can enjoy the benefit of increased Hamming distance when applying this side information at the receiver. In particular, we present a new constellation mapping principle to take advantage of the side information in the modulator, which leads to different signal constellations for the information bits and the parity-check bits. We then analytically derive the constellation-constrained capacity for BICM-P and quantify its gain as a nonlinear function associated with the two constellations. For the practical use of BICM-P, this paper indicates that the side information makes the regular low-density parity-check (LDPC) code irregular. Accordingly, the density evolution analysis tool is developed to design and optimize the regular LDPC code for BICM-P. The performance of LDPC-coded BICM-P on additive white Gaussian noise (AWGN) channels and fast Rayleigh fading channels is analyzed using extensive simulations. We observe that, at high code rates (≥1/2), LDPC-coded BICM-P has a substantial gain (0.1117-0.6558 dB) compared with LDPC-coded BICM on the AWGN channel. The performance gains will become more significant (0.7541-2.3481 dB) on the fast Rayleigh fading channel.

## Convolutional-Code-Specific CRC Code Design

- **Status**: ❌
- **Reason**: CRC 코드 설계 + convolutional code 특화, LDPC 디코더로 떼어낼 기법 없음 (비-LDPC)
- **ID**: ieee:7163569
- **Type**: journal
- **Published**: Oct. 2015
- **Authors**: Chung-Yu Lou, Babak Daneshrad, Richard D. Wesel
- **PDF**: https://ieeexplore.ieee.org/document/7163569
- **Abstract**: Cyclic redundancy check (CRC) codes check if a codeword is correctly received. This paper presents an algorithm to design CRC codes that are optimized for the code-specific error behavior of a specified feedforward convolutional code. The algorithm utilizes two distinct approaches to computing undetected error probability of a CRC code used with a specific convolutional code. The first approach enumerates the error patterns of the convolutional code and tests if each of them is detectable. The second approach reduces complexity significantly by exploiting the equivalence of the undetected error probability to the frame error rate of an equivalent catastrophic convolutional code. The error events of the equivalent convolutional code are exactly the undetectable errors for the original concatenation of CRC and convolutional codes. This simplifies the computation because error patterns do not need to be individually checked for detectability. As an example, we optimize CRC codes for a commonly used 64-state convolutional code for information length k=1024, demonstrating significant reduction in undetected error probability compared to the existing CRC codes with the same degrees. For a fixed target undetected error probability, the optimized CRC codes typically require 2 fewer bits.

## Jointly Designed Nonbinary LDPC Convolutional Codes and Memory-Based Decoder Architecture

- **Status**: ❌
- **Reason**: 비이진(GF(256)) NB-LDPC convolutional codes 및 디코더 — 비이진 LDPC 제외
- **ID**: ieee:7277127
- **Type**: journal
- **Published**: Oct. 2015
- **Authors**: Chia-Lung Lin, Chih-Lung Chen, Hsie-Chia Chang +1
- **PDF**: https://ieeexplore.ieee.org/document/7277127
- **Abstract**: In this paper, a design approach for architecture- aware nonbinary low-density parity-check convolutional codes (NB-LDPC-CCs) is presented to jointly optimizes the code performance and decoder complexity for achieving high energy-efficiency decoder. The proposed NB-LDPC-CCs not only feature simple structure and low degree, but also compete with other published NB-LDPC-CCs on error-correction capability. With these codes, we present a memory-based layered decoder architecture, where the computation units and the scheduling of the computations are optimized to increase energy efficiency. To demonstrate the feasibility of proposed techniques, a time-varying (50,2,4) NB-LDPC-CC over GF(256) is constructed, and associated decoder is implemented in 90 nm CMOS. The code can reach BER=10-5 at SNR=0.9 dB, and support multi code rates with puncturing. Comparing with the state-of-the-art designs, the proposed decoder can save 74% power under the same number of iterations, making it suitable for emerging Internet of Things (IoT) applications.

## Error-Control Coding for Physical-Layer Secrecy

- **Status**: ❌
- **Reason**: 물리계층 보안용 error-control coding, 보안 도메인이며 떼어낼 LDPC 디코더 기법 없음
- **ID**: ieee:7264976
- **Type**: journal
- **Published**: Oct. 2015
- **Authors**: Matthieu Bloch, Masahito Hayashi, Andrew Thangaraj
- **PDF**: https://ieeexplore.ieee.org/document/7264976
- **Abstract**: The renewed interest for physical-layer security techniques has put forward a new role for error-control codes. In addition to ensuring reliability, carefully designed codes have been shown to provide a level of information-theoretic secrecy, by which the amount of information leaked to an adversary may be controlled. The ability to achieve information-theoretic secrecy relies on the study of alternative coding mechanisms, such as channel resolvability and privacy amplification, in which error-control codes are exploited as a means to shape the distribution of stochastic processes. This use of error-control codes, which goes much beyond that of correcting errors, creates numerous new design challenges. The objective of this paper is threefold. First, the paper aims at providing system engineers with explicit tools to build simple secrecy codes in order to stimulate interest and foster their integration in communication system prototypes. Second, it aims at providing coding and information theorists with a synthetic overview of the theoretical concepts and techniques for secrecy. Finally, it aims at highlighting the open challenges and opportunities faced for the integration of these codes in practical systems.

## Quasi-Primitive Block-Wise Concatenated BCH Codes With Collaborative Decoding for NAND Flash Memories

- **Status**: ❌
- **Reason**: NAND용이나 BC-BCH(비-LDPC) 코드와 collaborative IHDD 디코딩 — LDPC BP로 이식 불가
- **ID**: ieee:7192620
- **Type**: journal
- **Published**: Oct. 2015
- **Authors**: Daesung Kim, Jeongseok Ha
- **PDF**: https://ieeexplore.ieee.org/document/7192620
- **Abstract**: In this work, we propose a novel design rule of block-wise concatenated Bose-Chaudhuri-Hocquenghem (BC-BCH) codes for storage devices using multi-level per cell (MLC) NAND flash memories. BC-BCH codes designed in accordance with the proposed design rule are called quasi-primitive BC-BCH codes in which constituent BCH codes are deliberately chosen for their lengths to be as close to primitive BCH codes as possible. It will be shown that such quasi-primitive BC-BCH codes can achieve significant improvements of error-correcting capability over the existing BC-BCH codes when an iterative hard-decision based decoding (IHDD) is assumed. In addition, we propose a novel collaborative decoding algorithm which targets at resolving dominant error patterns associated with the IHDD. Error-rate performances of error-control systems with the proposed quasi-primitive BC-BCH and existing BC-BCH codes are compared. For more comprehensive performance comparisons, systems with a hypothetically long BCH code and a product code are also considered in the comparisons.

## Low-Latency Successive-Cancellation List Decoders for Polar Codes With Multibit Decision

- **Status**: ❌
- **Reason**: polar 코드 SCL 디코더(multibit decision). 부호 의존적이라 바이너리 LDPC BP에 이식 불가, 비-LDPC 원칙 제외
- **ID**: ieee:6920050
- **Type**: journal
- **Published**: Oct. 2015
- **Authors**: Bo Yuan, Keshab K. Parhi
- **PDF**: https://ieeexplore.ieee.org/document/6920050
- **Abstract**: Polar codes, as the first provable capacity-achieving error-correcting codes, have received much attention in recent years. However, the decoding performance of polar codes with traditional successive-cancellation (SC) algorithm cannot match that of the low-density parity-check or Turbo codes. Because SC list (SCL) decoding algorithm can significantly improve the error-correcting performance of polar codes, design of SCL decoders is important for polar codes to be deployed in practical applications. However, because the prior latency reduction approaches for SC decoders are not applicable for SCL decoders, these list decoders suffer from the long-latency bottleneck. In this paper, we propose a multibit-decision approach that can significantly reduce latency of SCL decoders. First, we present a reformulated SCL algorithm that can perform intermediate decoding of 2 b together. The proposed approach, referred as 2-bit reformulated SCL (2b-rSCL) algorithm, can reduce the latency of SCL decoder from (3n-2) to (2n-2) clock cycles without any performance loss. Then, we extend the idea of 2-b-decision to general case, and propose a general decoding scheme that can perform intermediate decoding of any 2K bits simultaneously. This general approach, referred as 2K-bit reformulated SCL (2K b-rSCL) algorithm, can reduce the overall decoding latency to as short as n/2K-2-2 cycles. Furthermore, on the basis of the proposed algorithms, very large-scale integration architectures for 2b-rSCL and 4b-rSCL decoders are synthesized. Compared with a prior SCL decoder, the proposed (1024, 512) 2b-rSCL and 4b-rSCL decoders can achieve 21% and 60% reduction in latency, 1.66 and 2.77 times increase in coded throughput with list size 2, and 2.11 and 3.23 times increase in coded throughput with list size 4, respectively.

## Lattices Over Eisenstein Integers for Compute-and-Forward

- **Status**: ❌
- **Reason**: Eisenstein 정수 격자코드 compute-and-forward. 무선 격자코드 이론, 바이너리 LDPC 디코더/HW/구성 기법 아님
- **ID**: ieee:7154472
- **Type**: journal
- **Published**: Oct. 2015
- **Authors**: Nihat Engin Tunali, Yu-Chih Huang, Joseph J. Boutros +1
- **PDF**: https://ieeexplore.ieee.org/document/7154472
- **Abstract**: In this paper, we consider the use of lattice codes over Eisenstein integers for implementing a compute and-forward protocol in wireless networks when channel state information is not available at the transmitter. We extend the compute-and-forward paradigm of Nazer and Gastpar to decoding Eisenstein integer combinations of transmitted messages at relays by proving the existence of a sequence of pairs of nested lattices over Eisenstein integers in which the coarse lattice is good for covering and the fine lattice can achieve the Poltyrev limit. Using this result, we show that both the outage performance and error-correcting performance of the nested lattice codebooks over Eisenstein integers surpass those of lattice codebooks over integers considered by Nazer and Gastpar with no additional computational complexity.

## Unequal Message Protection: Asymptotic and Non-Asymptotic Tradeoffs

- **Status**: ❌
- **Reason**: 불균등 메시지 보호의 정보이론 bound/finite blocklength 분석 — 디코더/HW/구성으로 안 이어짐, LDPC 비의존
- **ID**: ieee:7173010
- **Type**: journal
- **Published**: Oct. 2015
- **Authors**: Yanina Y. Shkel, Vincent Y. F. Tan, Stark C. Draper
- **PDF**: https://ieeexplore.ieee.org/document/7173010
- **Abstract**: We study a form of unequal error protection that we term unequal message protection (UMP). The message set of a UMP code is a union of  $m$  disjoint message classes. Each class has its own error protection requirement, with some classes needing better error protection than others. We analyze the tradeoff between rates of message classes and the levels of error protection; our analysis reveals new tradeoffs, which were not captured by prior works on UMP codes. To obtain our results, we generalize finite block length achievability and converse bounds due to Polyanskiy–Poor–Verdú. We evaluate our bounds for the binary symmetric and binary erasure channels, and analyze the asymptotic characteristic of the bounds in the fixed error and moderate deviations regimes. In addition, we consider two questions related to the practical construction of UMP codes. First, we study a header construction that prefixes the message class into a header followed by data protection using a standard homogeneous (classical) code. We show that, in general, this construction is not optimal at finite block lengths. We further demonstrate that our main UMP achievability bound can be obtained using coset codes, which suggests a path to implementation of tractable UMP codes.

## Distributed Irregular Codes Relying on Decode-and-Forward Relays as Code Components

- **Status**: ❌
- **Reason**: 분산 비정규 convolutional code(IRCC)+릴레이. 비-LDPC이고 무선 릴레이 응용 특이적, 이식 가능 LDPC 기법 없음
- **ID**: ieee:6977955
- **Type**: journal
- **Published**: Oct. 2015
- **Authors**: Soon Xin Ng, Yonghui Li, Branka Vucetic +1
- **PDF**: https://ieeexplore.ieee.org/document/6977955
- **Abstract**: A near-capacity distributed coding scheme is conceived by incorporating multiple relay nodes (RNs) for constructing a virtual irregular convolutional code (IRCC). We first compute the relay channel's capacity and then design IRCCs for the source and relay nodes. Extrinsic information transfer (EXIT) charts are utilized to design the codes for approaching the achievable capacity of the relay channels. Additionally, we improve the transmit power efficiency of the overall system by invoking both power allocation and relay selection. We found that even a low-complexity repetition code or a unit-memory convolutional code is capable of forming a near-capacity virtual IRCC. The performance of the proposed distributed IRCC (DIRCC) scheme is shown to be perfectly consistent with that predicted from the EXIT chart. More specifically, the DIRCC scheme is capable of operating within 0.68 dB from the corresponding lower bound of the relay channel capacity, despite the fact that each RN is exposed to realistic decoding errors due to communicating over imperfect source-relay channels.

## Efficient LLR Calculation for FBMC

- **Status**: ❌
- **Reason**: FBMC 무선 변조 특화 LLR 계산, NAND LDPC로 떼어낼 ECC 기법 없음
- **ID**: ieee:7192607
- **Type**: journal
- **Published**: Oct. 2015
- **Authors**: Soonki Jo, Jong-Soo Seo
- **PDF**: https://ieeexplore.ieee.org/document/7192607
- **Abstract**: Orthogonal frequency division multiplexing (OFDM) technology has been adopted in various communications and broadcasting systems, including LTE, WiMax, and DVB-T2. However, cyclic prefix (CP) and guard band are required to limit the inter-symbol and adjacent interference, which would cause loss of spectral efficiency. Filter bank multiple carrier (FBMC) technology is one of the alternative solutions of multicarrier modulation that mitigate such problems. FBMC applies offset-QAM (OQAM) and band-limited filtering on each subcarrier, which eliminates the need of CP and guard band. FBMC filtering could maintain the orthogonality in a real signal domain by using a well localized filter. However, due to the OQAM structure, the transmitted data is mixed with an intrinsic interference, therefore, conventional log likelihood ratio (LLR) calculation for OFDM system is not applicable to FBMC system. In this letter, we propose an efficient LLR calculation method for use in FBMC system. It is found that the proposed method does not increase the implementation complexity of FBMC receiver while it performs same as that of OFDM system.

## Protograph LDPC codes for STBC Rayleigh fading channels

- **Status**: ❌
- **Reason**: STBC fading용 protograph LDPC 임계값 분석(PEXIT) — 무선 채널 특이적, NAND 이식 신규 기법 없음
- **ID**: ieee:7458315
- **Type**: conference
- **Published**: 7-9 Oct. 2
- **Authors**: Yi Fang, Guojun Han, Pingping Chen +2
- **PDF**: https://ieeexplore.ieee.org/document/7458315
- **Abstract**: In wireless communications, spatial diversity techniques, such as space-time block code (STBC) and multiple-input multiple-output (MIMO), have attracted much attention in recent years because they possess powerful robustness against signal fading. In this paper, we investigate the performance of the protograph low-density parity-check (LDPC) codes over space-time block code (STBC) Rayleigh fading channels. Taking into consideration the Alamouti STBC structure, we propose a modified protograph extrinsic information transfer (PEXIT) algorithm in order to analyze the convergence performance of protograph codes in such scenarios. We further compare the decoding thresholds and bit error rates (BERs) of two typical protograph codes, i.e., accumulate-repeat-by-3-accumulate (AR3A) code and accumulated-repeat-by-4-jagged-accumulate (AR4JA) code, with the regular LDPC code and optimized irregular LDPC codes. The results illustrate that the AR3A code outperforms other three codes in the high signal-to-noise-ratio (SNR) region. As a consequence, the AR3A code appears to be a better candidate for use in the wireless communication systems with multiple antennas.

## Improving the Bandwidth Efficiency of Multi-Terminal Satellite Communications

- **Status**: ❌
- **Reason**: 위성 3-way relay 결합 채널/네트워크 코딩; LDPC 무관, NAND 이식 기법 없음
- **ID**: ieee:7324464
- **Type**: conference
- **Published**: 4-7 Oct. 2
- **Authors**: Boulos Wadih Khoueiry, M. Reza Soleymani
- **PDF**: https://ieeexplore.ieee.org/document/7324464
- **Abstract**: This paper presents a new coding scheme that considerably increases the efficiency of the channel in multicast setting. Specifically, we study the scenario where three terminals exchange their messages via a satellite gateway. The main difference between the proposed scheme and conventional three-way relay channel is the use of joint channel and network coding. This allows three terminals to transmit simultaneously, therefore, reducing the number of time slots. In our scheme, the relay may either amplify and forward or de-noise and forward, whereas in the conventional scheme the relay decodes and performs bit-wise exclusive OR on the packets or simply decodes the bit-wise XOR of the two messages and broadcasts it to all terminals. So while conventional schemes assume a binary channel on the downlink, we assume a ternary channel on the downlink. Furthermore, while in the conventional scheme each terminal removes its own message from the downlink signal in order to recover the other terminal's message, in our scheme after removing its own message, a terminal can decode a second terminal's encoded message treating the third terminal message as interference and finally recover the third terminal's message interference-free. We show that our scheme achieves a total rate of 2.

## Cryptocoding system based on AES and concatenated coding scheme involving BCH and QC-LDPC

- **Status**: ❌
- **Reason**: 플래시 언급하나 AES 암호화+BCH/QC-LDPC 표준 직렬연접만, 새 디코더·구성 기여 없음
- **ID**: ieee:7456880
- **Type**: conference
- **Published**: 29-31 Oct.
- **Authors**: Karthika Viswanath, P. V. Pearlsy
- **PDF**: https://ieeexplore.ieee.org/document/7456880
- **Abstract**: In single-level cell flash memory, the most popular error correction code used for protection of the stored data is Bose-Chaudhuri-Hocquenghem (BCH) codes. However, BCH codes are not adequate to meet the error requirements of multi-level cell flash memory. Serial concatenation of codes increases the error correcting capability of the resulting system. Hence, a favorable concatenated coding scheme for next-generation flash memory is proposed which is the combination of BCH and QC-LDPC codes. Encryption schemes can be integrated with error-correction in order to achieve more security and reliability of the communication system. Here, Advanced Encryption Standard(AES-128) is used to encrypt the information first, and then the encrypted data is encoded by the concatenated coding scheme. This ensures the security and reliability of data to be stored or transmitted.

## FPGA implementation of BCH decoder for memory systems

- **Status**: ❌
- **Reason**: 비-LDPC(BCH) 디코더 FPGA 구현, 이식 가능한 LDPC 기법 없음
- **ID**: ieee:7456944
- **Type**: conference
- **Published**: 29-31 Oct.
- **Authors**: B. S. Chandrashekhara, K L Sudha
- **PDF**: https://ieeexplore.ieee.org/document/7456944
- **Abstract**: BCH (Bose-Chaudhuri-Hocquenghem) coding is very useful to detect and correct the errors in communication system and also on-chip (computer) memory systems. This paper presents a High-speed BCH decoder that corrects double-adjacent and single-bit errors in parallel and serially corrects multiple-bit errors instead of double-adjacent errors. Its operation is based on extending an existing decoder that corrects only single-bit errors in parallel and serially corrects double-adjacent errors at low speed. The proposed constructed decoder design is suitable for nanoscale memory systems, in which double-adjacent and single-bit errors occur at a higher probability compared to the multiple-bit errors. This paper also shows that the area and delay overheads incurred by the proposed scheme are significantly lower than traditional BCH decoders capable of correcting any double-bit errors in parallel.

## Concentration to zero bit-error probability for regular LDPC codes on the binary symmetric channel: Proof by loop calculus

- **Status**: ❌
- **Reason**: 정규 LDPC BSC bit-error 0 수렴의 순수 이론 증명(loop calculus), 디코더/HW/구성으로 안 이어짐
- **ID**: ieee:7446993
- **Type**: conference
- **Published**: 29 Sept.-2
- **Authors**: Marc Vuffray, Theodor Misiakiewicz
- **PDF**: https://ieeexplore.ieee.org/document/7446993
- **Abstract**: In this paper we consider regular low-density parity-check codes over a binary-symmetric channel in the decoding regime. We prove that up to a certain noise threshold the bit-error probability of the bit-sampling decoder converges in mean to zero over the code ensemble and the channel realizations. To arrive at this result we show that the bit-error probability of the sampling decoder is equal to the derivative of a Bethe free entropy. The method that we developed is new and is based on convexity of the free entropy and loop calculus. Convexity is needed to exchange limit and derivative and the loop series enables us to express the difference between the bit-error probability and the Bethe free entropy. We control the loop series using combinatorial techniques and a first moment method. We stress that our method is versatile and we believe that it can be generalized for LDPC codes with general degree distributions and for asymmetric channels.

## Deployment strategy analysis for underwater cooperative wireless sensor networks

- **Status**: ❌
- **Reason**: 수중 WSN 배치 전략 분석, LDPC-coded OFDM은 베이스라인일 뿐 떼어낼 ECC 기법 없음
- **ID**: ieee:7354642
- **Type**: conference
- **Published**: 28-30 Oct.
- **Authors**: Zafar Iqbal, Heung-No Lee
- **PDF**: https://ieeexplore.ieee.org/document/7354642
- **Abstract**: Wireless sensor networks (WSNs) are widely used for underwater environment monitoring. Because of the harsh underwater environment, WSNs face the challenges of erroneous communication, lower lifetime, less robustness, and cost constraints. In this paper, we propose a cooperative WSN which uses a cooperative coded OFDM (COFDM) system and network coding to deal with the shadowing phenomenon present in the underwater communication channel. The proposed scheme is cooperative spatial-domain coding combined with the LDPC-coded OFDM system. The designed system is analyzed using random and grid deployment strategies for the required number of sensors, bit-error rate (BER), and cost of the network.

## On performance analysis of IEEE 802.22 (PHY) for COST-207 channel models

- **Status**: ❌
- **Reason**: 802.22 성능분석, LDPC 디코더는 표준 log-domain SPA 베이스라인 비교에 불과
- **ID**: ieee:7390449
- **Type**: conference
- **Published**: 28-30 Oct.
- **Authors**: Abhijeet Bishnu, Vimal Bhatia
- **PDF**: https://ieeexplore.ieee.org/document/7390449
- **Abstract**: With rapid increase in demand for bandwidth, several researchers around the world have found that, majority of licensed bands are either unused or underused. These under-utilised bands allocated for TV transmission are known as TV white space (TVWS). The IEEE 802.22 wireless regional area network (WRAN) is the latest standard for effective utilization of TV bands. This standard is based on orthogonal frequency division multiplexing (OFDM) with different cyclic prefix and modulation techniques. In this paper, we analyse the performance of IEEE 802.22 on different environments such as rural area (RA), typical urban (TU) and hilly terrain (HT) of COST-207 channel models. The performance analysis has been done for different modulation techniques, without channel coding, with channel coding of rate 1/2, punctured channel coding and comparison is drawn for Viterbi decoder and simplified logdomain sum-product algorithm based low density parity check (LDPC) decoder. We have also done separate analysis of digital TV (DTV) interference on customer premise equipments of IEEE 802.22 standard for TU model. The analysis will be useful for both academic and industry researchers and practitioners.

## Performance of MIMO detectors with a capacity-approaching code

- **Status**: ❌
- **Reason**: MIMO 검출기 LLR 근사 비교, 떼어낼 LDPC 디코더·HW·코드설계 기법 없음
- **ID**: ieee:7354756
- **Type**: conference
- **Published**: 28-30 Oct.
- **Authors**: Seol-Jun Yoon, Joongho Lee, Seokhyun Yoon
- **PDF**: https://ieeexplore.ieee.org/document/7354756
- **Abstract**: In this paper, we provides a comparison of low-complexity MIMO detector, including linear MMSE receiver with a capacity-approaching channel code. The impact of soft-decision provided by MIMO detection plays an important role especially when using capacity-approaching codes. Here, our focus is on linear MMSE receiver with soft-decision output, a.k.a., log-likelihood ratio, and its approximate version. This paper will provides a correction on the performance of MMSE receiver in our previous paper [8].

## Optimal pilot design for space-time coded multi-user MIMO OFDM/SDMA systems

- **Status**: ❌
- **Reason**: MIMO OFDM 파일럿 설계/채널추정, LDPC/ECC 무관
- **ID**: ieee:7354700
- **Type**: conference
- **Published**: 28-30 Oct.
- **Authors**: Zhe Zhang, Jiankang Zhang, Shuangzhi Li +1
- **PDF**: https://ieeexplore.ieee.org/document/7354700
- **Abstract**: In this paper, we propose an optimal pilot design scheme for multi-user Multiple-Input Multiple-Output (MIMO) Orthogonal Frequency Division Multiplexing/Space Division Multiple Access (OFDM/SDMA) systems. We derive the optimal pilot design criterion with regard to the computational complexity and the Mean Square Error (MSE) of the Least Square (LS) estimator. Furthermore, we propose a binary-tree based search scheme in order to find the optimal position for placement the Space-Time Coded pilot symbols. Through our analysis and simulations, it is shown that the pilot design complied with the our proposed placement criteria could obtain the lowest computational complexity and the optimum estimate performance.

## PSG-Codes: An Erasure Codes Family with High Fault Tolerance and Fast Recovery

- **Status**: ❌
- **Reason**: XOR 기반 non-MDS erasure code(PSG), LDPC BP 아닌 패리티체인 방식, 이식 기법 없음
- **ID**: ieee:7371567
- **Type**: conference
- **Published**: 28 Sept.-1
- **Authors**: Shiyi Li, Qiang Cao, Lei Tian +3
- **PDF**: https://ieeexplore.ieee.org/document/7371567
- **Abstract**: As hard disk failure rates are rarely improved and the reconstruction time for TB-level disks typically amounts to days, multiple concurrent disk/storage node failures in datacenter storage systems become common and frequent. As a result, the erasure coding schemes used in datacenters must meet the critical requirements of high fault tolerance, high storage efficiency, and fast fault recovery. In this paper, we introduce a new XOR-based non-MDS erasure code family with an ability of tolerating up to 12-disk/node failures, called PSG-Codes. The basic idea behind PSG-Codes is to partition disks into groups, and exploit short parity chains to generate parity units. Then, the parity chain is further shortened by varying the number of parity elements for each strip. We conduct a simulation-based study to search configuration parameter space of PSG-Codes, and prove that PSG-Codes can tolerate up to 12 disk/node failures. Compared with a well-known XOR-based non-MDS code, WEAVER codes, PSG-Codes have higher storage efficiency and lower reconstruction cost. Moreover, the storage efficiency and performance of PSG-Codes are also competitive with another stat-of-the-art GF-based non-MDS codes, LRC codes.

## Fast decoding and LLR-computation algorithms for high-order set-partitioned 4D-QAM constellations

- **Status**: ❌
- **Reason**: 4D-QAM 성좌의 LLR 계산/고속 디코딩이지만 변조 패리티검사함수 기반으로 LDPC BP 이식 불가, 비-LDPC
- **ID**: ieee:7341738
- **Type**: conference
- **Published**: 27 Sept.-1
- **Authors**: Shota Ishimura, Kazuro Kikuchi
- **PDF**: https://ieeexplore.ieee.org/document/7341738
- **Abstract**: We propose digital-signal-processing algorithms that achieve fast decoding and LLR-computation for high-order set-partitioned 4D-QAM formats based on their parity-check functions. Computer-simulation results show that computational complexity of the decoder can significantly be reduced with negligible power penalty using such algorithms.

## Experimental demonstration of multi-pilot aided carrier phase estimation for DP-64QAM and DP-256QAM

- **Status**: ❌
- **Reason**: 광통신 캐리어 위상추정(CPE) 알고리즘으로 LDPC는 baseline 부수 언급일 뿐 ECC 기법 없음
- **ID**: ieee:7341655
- **Type**: conference
- **Published**: 27 Sept.-1
- **Authors**: Milutin Pajovic, David S. Millar, Toshiaki Koike-Akino +9
- **PDF**: https://ieeexplore.ieee.org/document/7341655
- **Abstract**: We present a statistical inference based multi-pilot aided CPE algorithm and analyze its performance via simulations. We experimentally verify LDPC coded back-to-back performance using 10 GBd DP-64QAM and DP-256QAM modulation, with transmitter and receiver linewidths of 100 kHz.

## 2.05 Peta-bit/s super-nyquist-WDM SDM transmission using 9.8-km 6-mode 19-core fiber in full C band

- **Status**: ❌
- **Reason**: SDM/WDM 광전송 용량 데모, LDPC 무관, ECC 기법 없음
- **ID**: ieee:7341686
- **Type**: conference
- **Published**: 27 Sept.-1
- **Authors**: D. Soma, K. Igarashi, Y. Wakayama +6
- **PDF**: https://ieeexplore.ieee.org/document/7341686
- **Abstract**: We demonstrate ultra-dense SDM transmission of 360-channel Super-Nyquist-WDM DP-QPSK signals over 9.8-km 6-mode 19-core fiber, achieving the record fiber capacity of 2.05 Pbit/s (360WDM×114SDM×50Gbit/s) with the highest aggregate spectral efficiency of 456 bit/s/Hz.

## A study on power-scaling of triple-concatenated FEC for optical transport networks

- **Status**: ❌
- **Reason**: 삼중연접 FEC 전력 스케일링 측정 연구, 신규 LDPC 디코더/구성/HW 기여 없음
- **ID**: ieee:7341944
- **Type**: conference
- **Published**: 27 Sept.-1
- **Authors**: Kenji Ishii, Keisuke Dohi, Kazuo Kubo +3
- **PDF**: https://ieeexplore.ieee.org/document/7341944
- **Abstract**: We studied the power scaling using the measured power consumption and error correction performance of a triple-concatenated FEC. It was confirmed that the triple-concatenated FEC enabled 98% power reduction by controlling the NCG to suit the OSNR of the link.

## Optimized BICM-8QAM formats based on generalized mutual information

- **Status**: ❌
- **Reason**: BICM-8QAM 변조/매핑 최적화로 LDPC ECC와 무관, 떼어낼 디코더/코드설계 기법 없음
- **ID**: ieee:7341639
- **Type**: conference
- **Published**: 27 Sept.-1
- **Authors**: Shaoliang Zhang, Kohei Nakamura, Fatih Yaman +3
- **PDF**: https://ieeexplore.ieee.org/document/7341639
- **Abstract**: Through the expansion of non-Gray-mapping symbols, the pre-FEC and post-FEC Q-factors of the proposed optimized Circle-8QAM outperform Circle-8QAM and Star-8QAM by ∼0.3 dB and ∼0.6dB at the coding rate of 0.8 in experiments.

## Fiber-remoted 20-Gbaud QPSK transmission at 300 GHz

- **Status**: ❌
- **Reason**: 300GHz THz/광 전송 데모로 LDPC ECC와 무관
- **ID**: ieee:7356694
- **Type**: conference
- **Published**: 26-29 Oct.
- **Authors**: Atsushi Kanno, Norihiko Sekine, Iwao Hosako +3
- **PDF**: https://ieeexplore.ieee.org/document/7356694
- **Abstract**: 300-GHz multilevel signal transmission over optical fibers and air is demonstrated using advanced optical communication technology including optical frequency comb generation. Local oscillator signal transport over optical fibers to optical-terahertz converters removes the need for setting any terahertz-capable oscillators in the converters. This fiber-remoted configuration with seamless conversion between the optical and terahertz signals is compatible with high-speed terahertz backhaul and fronthaul links.

## Low-density generator matrix code for correcting errors with a small optical transponder

- **Status**: ❌
- **Reason**: 위성 광통신 LDGM/RS 부호 데모, LDGM은 비-LDPC 생성행렬 부호이고 신규 디코더/구성 기여 없음
- **ID**: ieee:7425069
- **Type**: conference
- **Published**: 26-28 Oct.
- **Authors**: Hideki Takenaka, Eiji Okamoto, Morio Toyoshima
- **PDF**: https://ieeexplore.ieee.org/document/7425069
- **Abstract**: Space optical communications is studied at National Institute of Information and Communications Technology, where the Small Optical TrAnsponder (SOTA) was developed and embarked on a 50-kg-class satellite. Atmospheric fluctuation is an issue to be solved in ground-to-satellite optical communication links. The SOTA has error-correcting functions using Reed-Solomon code and low-density generator matrix (LDGM) code to prevent the omission of data from signal fading owing to atmospheric fluctuations. In this paper, we present a demonstration that involves sending image data taken by an onboard camera with LDGM code via satellite-to-ground optical communication links. Our demonstration reveals how to correct the omission of data resulting from atmospheric turbulence and tracking errors.

## Performance of frequency hopping D-BLAST MIMO Architecture using LDPC and BPSK

- **Status**: ❌
- **Reason**: FHSS D-BLAST MIMO 무선 시스템 성능 평가, LDPC는 BPSK 테스트케이스로 부수 언급, 떼어낼 디코더/HW/코드설계 기법 없음
- **ID**: ieee:7357553
- **Type**: conference
- **Published**: 26-28 Oct.
- **Authors**: Janek J. Mroczek, Michael. J. Gans, Laurie L. Joiner
- **PDF**: https://ieeexplore.ieee.org/document/7357553
- **Abstract**: In this paper we introduce frequency hopping spread spectrum (FHSS) into Diagonal Bell Laboratories Layered Space-Time (D-BLAST) Multiple Input Multiple Output (MIMO) architecture. We evaluate the performance of the system containing a single interference affecting the system with various probabilities and power. An LDPC code and BPSK modulation is used as a test case to obtain message bit error rate and is compared to non-frequency hopping D-BLAST MIMO architecture.

## Code selection approach for partitioned cyclic code shift keying to improve multinet capability

- **Status**: ❌
- **Reason**: RS 코드 선택 기반 PCCSK 스프레드 스펙트럼 기법, 비-LDPC 무선 응용
- **ID**: ieee:7357549
- **Type**: conference
- **Published**: 26-28 Oct.
- **Authors**: Hongjun Noh, Jepung Yu, Kyuman Lee +1
- **PDF**: https://ieeexplore.ieee.org/document/7357549
- **Abstract**: In this paper, we propose a new code selection approach for partitioned cyclic code shift keying (PCCSK) to improve the multinet capability of Joint Tactical Information Distribution Systems (JTIDS). The multinet capability of JTIDS enables concurrent operations in battle fields by allowing simultaneous data transmission and reception. PCCSK is a spread spectrum technique that supports various data rates and improves the data rate of JTIDS. The existing approach to PCCSK employs Reed Solomon (RS) code selection, and allows the dissemination of multiple access interference from the contaminated pulse to other pulses, and degrades the multinet capability. To prevent this error propagation, the proposed code selection approach restricts the RS symbol to be transmitted within one pulse. Simulation results show that the waveforms obtained using the proposed scheme outperform the previous waveforms including the JTIDS waveform with respect to both the multinet capability and the data rate.

## The Min-Max in LC and Max-Log MAP in LC for MTR Decoding in Two-Track Magnetic Recording Systems

- **Status**: ❌
- **Reason**: MTR 부호 soft-decision 디코딩(자기상관 채널 특이적), LDPC는 부수 concatenation — 무선/기록채널 특이적, 떼어낼 LDPC 기법 없음
- **ID**: ieee:7371391
- **Type**: conference
- **Published**: 21-23 Oct.
- **Authors**: Nikola Djuric, Vojin Senk
- **PDF**: https://ieeexplore.ieee.org/document/7371391
- **Abstract**: The soft-decision decoding methods for maximum-transition-run (MTR) codes have been considered extensively, in order to enable a wider implementation of MTR codes in magnetic recording systems. The approaches, named as the min-max in LC and the max-log MAP in LC have been proposed, emerging as reasonable solutions for MTR codes. Both methods force the soft-values propagation through the Boolean logic circuits of decoder, encouraging the concatenation of MTR with some powerful error-correcting codes, such as low-density parity-check (LDPC) codes. In this paper, the min-max in LC and the max-log MAP in LC have been analyzed in the framework of a simple LDPC-MTR concatenation, over the two-track two-head interfering E2PR4 magnetic recording channel. In the case of a rate 4/5 (2, k = 8) MTR code utilization and the low-level of inter-track interference, the proposed methods offer 1.9 dB and 1.7 dB of decoding gain, for BER = 10-5. However, the complexity analysis shows that the min-max in LC is in advantage comparing to the max-log MAP in LC.

## Gallager mapping based constellation shaping for LDPC-coded modulation systems

- **Status**: ❌
- **Reason**: 비이진 LDPC coded-modulation + constellation shaping 응용 — non-binary 제외, 떼어낼 ECC 기법 없음
- **ID**: ieee:7354347
- **Type**: conference
- **Published**: 21-23 Oct.
- **Authors**: Dan Feng, Qi Li, Baoming Bai +1
- **PDF**: https://ieeexplore.ieee.org/document/7354347
- **Abstract**: This paper focuses on the signal constellation shaping in LDPC coded modulation system. A novel constellation is presented by combining geometric shaping with probabilistic shaping based on quadrature amplitude modulation (QAM)constellation. With the shaped signal constellation, the signal mapping is optimized by using the extrinsic information transfer (EXIT) chart analysis. We further consider the nonbinary LDPC coded-modulation by combining with the proposed constellation shaping. Numerical results reveal that the proposed constellation can get the shaping gain without increasing the complexity of detection.

## Obtaining diversity gain by block Markov superposition transmission

- **Status**: ❌
- **Reason**: 실수영역 BMST 다이버시티 기법, PEG-LDPC는 시뮬레이션 베이스라인일 뿐; 떼어낼 LDPC 디코더/구성 기법 없음
- **ID**: ieee:7354337
- **Type**: conference
- **Published**: 21-23 Oct.
- **Authors**: Jinshun Zhu, Xiao Ma
- **PDF**: https://ieeexplore.ieee.org/document/7354337
- **Abstract**: In time-varying wireless channels, the radio signals suffer from time-varying fading which may cause severe signal attenuation. In this paper, we present a new approach, called block Markov superposition transmission (BMST) over real field, to obtain diversity which increases the transmission reliability under the fading channels. The proposed scheme is similar to BMST over binary field, which has been used to construct big convolutional codes from short codes. However, unlike superposition in BMST over binary field, superposition in the proposed scheme is over real field. We also present an iterative sliding-window detection/decoding algorithm for the proposed transmission scheme. The performance of BMST over real field can be lower bounded by that of the equivalent system. Progressive edge-growth (PEG) constructed LDPC code of rate 0.5 with length 504 and bipolar basic mapping are chosen for simulation, and numerical results show that: 1) in additive white gaussian noise (AWGN) channels, no performance gain is obtained; 2) in fast Rayleigh fading channels, an extra diversity gain of 1.3 dB can be obtained by the proposed approach at bit-error-rate (BER) of 10−5; 3) in block Rayleigh fading channels, about 22 dB performance gain are obtained by the proposed approach at BER of 10−5.

## Spatial coupling of RUN codes via block Markov superposition transmission

- **Status**: ❌
- **Reason**: 비이진(그룹/임의 알파벳) RUN 코드의 BMST 공간결합; 비이진+비-LDPC 부호로 제외
- **ID**: ieee:7353345
- **Type**: conference
- **Published**: 21-23 Oct.
- **Authors**: Chulong Liang, Xiao Ma, Baoming Bai
- **PDF**: https://ieeexplore.ieee.org/document/7353345
- **Abstract**: In this paper, we propose a simple procedure to construct (decodable) good codes with any given alphabet (of moderate size) for any given (rational) code rate to achieve any given target error performance (of interest) over the additive white Gaussian noise (AWGN) channels. We start with constructing codes over groups for any given code rates. This can be done in an extremely simple way if we ignore the error performance requirement for the time being. Actually, this can be satisfied by repetition (R) codes and uncoded (UN) transmission along with time-sharing technique. The resulting codes are simply referred to as RUN codes for convenience. The encoding/decoding algorithms for RUN codes are almost trivial. In addition, the performance can be easily analyzed. It is not difficult to imagine that a RUN code usually performs far away from the corresponding Shannon limit. Fortunately, the performance can be improved as required by spatially coupling the RUN codes via block Markov superposition transmission (BMST), resulting in the BMST-RUN codes. Simulation results show that the BMST-RUN codes perform well (within one dB away from Shannon limits) for a wide range of code rates.

## A survey on packet scheduling over DVB-S2 through GSE encapsulation

- **Status**: ❌
- **Reason**: DVB-S2 패킷 스케줄링/RRM 서베이 — LDPC ECC 기법 없음, 무선 자원관리 응용
- **ID**: ieee:7381318
- **Type**: conference
- **Published**: 20-23 Oct.
- **Authors**: Youness Arjoune, Ahmed Tamtaoui, Hassan El Ghazi +1
- **PDF**: https://ieeexplore.ieee.org/document/7381318
- **Abstract**: A key features of the second generation for video broadcasting (DVB-S2) is the adoption of Adaptive Coding and Modulation (ACM) technology and Generic Stream Encapsulation (GSE) standards. In order to increase the system performance up to the Shannon limit a suitable resource management (RRM) exploiting this key features is a needed. Packet scheduling mechanisms particularly play a fundamental role to guarantee a better RRM, because they are responsible for choosing, with a fine time how to distribute the satellite resources among different terrestrial stations, taking into account channel condition and the quality-of-service requirements. This goal should be accomplish by providing, at the same time, an optimal trade-off between spectral efficiency, given the limited resources on satellite systems, while granting the requirements for quality-of-service. In this context, this paper provides an overview on the key issues that arise with the use of ACM technology and GSE encapsulation in the design of a scheduler to allocate satellite resources. Moreover, a survey on the most recent scheduling techniques is reported, including a comparison between different approaches presented in literature.

## MIMO-SC-FDMA system with iterative decision feedback equalization

- **Status**: ❌
- **Reason**: MIMO-SC-FDMA 반복 결정궤환 등화 — LDPC 무관, 떼어낼 ECC 기법 없음
- **ID**: ieee:7399785
- **Type**: conference
- **Published**: 18-20 Oct.
- **Authors**: Deliang Liu, Lihua Chen, Yimin Wei +2
- **PDF**: https://ieeexplore.ieee.org/document/7399785
- **Abstract**: The BER performance of MIMO-SC-FDMA system may degrade quickly when the frequency-selective deep fading occurs in the channel. In order to solve this problem the IB-DFEIC (iterative block decision-feedback equalization & interference cancellation) algorithm applied in MIMO-SCFDMA system is proposed in this paper. In this algorithm the inter-layer interference and inter-symbol interference will be cancelled at the same time in the iterative equalization. But the IB-DFEIC algorithm includes complex matrix inversion. In order to reduce the computation complexity the suboptimum IB-IC-DFE (iterative block interference cancellation and then decision-feedback equalization) algorithm is also put forward. In this algorithm the interference cancellation operation will be firstly executed to cancel the inter-layer interference, and then the decision-feedback equalization will be executed to cancel the inter-symbol interference. The simulation results that comparing with the general MMSE (minimum mean square error) algorithm, these two algorithms have great performance improvement. So they can be used for MIMO-SC-FDMA system to overcome the frequency selective deep fading in the channel.

## Quantum Expander Codes

- **Status**: ❌
- **Reason**: 양자 expander/hypergraph-product LDPC 디코더 — 양자 EC 원칙 제외, 고전 바이너리 LDPC로 직접 이식되는 신규 기법 없음
- **ID**: ieee:7354429
- **Type**: conference
- **Published**: 17-20 Oct.
- **Authors**: Anthony Leverrier, Jean-Pierre Tillich, Gilles Zémor
- **PDF**: https://ieeexplore.ieee.org/document/7354429
- **Abstract**: We present an efficient decoding algorithm for constant rate quantum hyper graph-product LDPC codes which provably corrects adversarial errors of weight proportional to the code minimum distance, or equivalently to the square-root of the block length. The algorithm runs in time linear in the number of qubits, which makes its performance the strongest to date for linear-time decoding of quantum codes. The algorithm relies on expanding properties, not of the quantum code's factor graph directly, but of the factor graph of the original classical code it is constructed from.

## The performance analysis of LDPC coded SFH/BPSK anti-jamming system

- **Status**: ❌
- **Reason**: SFH/BPSK 항재밍 시스템에 LDPC를 적용·파라미터 비교한 무선 응용, 새 디코더/구성/HW 기여 없음
- **ID**: ieee:7341171
- **Type**: conference
- **Published**: 15-17 Oct.
- **Authors**: Kongzhe Yang, Bangning Zhang, Hangxian Wang +1
- **PDF**: https://ieeexplore.ieee.org/document/7341171
- **Abstract**: In order to improve the anti-jamming ability of frequency hopping (FH) system, a low-density parity-check (LDPC) coded SFH/BPSK anti-jamming communication system is established in this paper, and the simulations of the antijamming performance are carried out. Firstly, the system model which is used in simulations is established. Then, the antijamming ability against partial band jamming (PBJ) with different jamming factors is simulated and compared using different coding parameters. At the end, the superiority of the combination of LDPC codes and FH systems is proved, the effect of code rate and code length on the proposed system model is measured, and some numerical results of the anti-jamming performance are obtained, which can be used as guidance by determining applicable coding parameters for adaptive antijamming LDPC coded FH systems.

## Iterative carrier recovery in an LDPC coded QPSK system at low SNRs

- **Status**: ❌
- **Reason**: LDPC 코딩 QPSK 반복 캐리어 복원 — 무선 동기화 응용, 떼어낼 LDPC ECC 기법 없음
- **ID**: ieee:7340999
- **Type**: conference
- **Published**: 15-17 Oct.
- **Authors**: Jianrong Bao, Xiqi Gao, Chao Liu +1
- **PDF**: https://ieeexplore.ieee.org/document/7340999
- **Abstract**: This paper presents an iterative carrier recovery (ICR) via soft decision metrics (SDMs) of low-density parity-check (LDPC) decoding in an LDPC coded quadrature phase shift keying (QPSK) system. It is crucial for wireless communication systems to work effectively, especially at low signal-to-noise ratios (SNRs). By maximizing the sum of the square of the SDMs of LDPC decoding with gradient oriented optimization of the objective function, it adaptively updates the carrier phase and frequency parameter accurately. The structure of the proposed scheme is also given, along with the phase ambiguity solution. Meanwhile, it is combined with the Costas loop tracking and the LDPC decoding feedback to eliminate residual carrier offsets. Simulation results indicate that the proposed ICR algorithm achieves good performance in an LDPC coded QPSK system under rather large carrier phase offsets, which is just within 0.1 dB of the ideal code performance at the cost of some moderate complexity. By the proposed scheme, a rate-1/2 LDPC coded QPSK system can even work at low bit SNR (Eb/N0) about 1-2 dB, which is useful in energy-limited wireless communications.

## Analysis and optimization design of P-LDPC coded hybrid FSO/RF systems

- **Status**: ❌
- **Reason**: 하이브리드 FSO/RF에 P-LDPC 적용, 기여는 심볼매핑·인터리버 최적화로 무선응용 특이적, 떼어낼 디코더/구성 기법 없음
- **ID**: ieee:7341331
- **Type**: conference
- **Published**: 15-17 Oct.
- **Authors**: Chengjun Tang, Ming Jiang, Chunming Zhao
- **PDF**: https://ieeexplore.ieee.org/document/7341331
- **Abstract**: In this paper, we study a hybrid free-space optical/radio-frequency (FSO/RF) communication system deploying protograph-based low-density parity-check (P-LDPC) codes. We use the protograph-based extrinsic information transfer (PEXIT) algorithm to accurately evaluate the system performance and employ the hybrid FSO/RF symbol mapping technique and the generalized variable degree matched mapping (G-VDMM) interleaver to enhance the performance. To make the optimization feasible and simpler for high-level modulation, we propose a much simpler but efficient design method: select a conventional Gray-labeled mapping scheme and then optimize the G-VDMM interleaver. Both numerical analyses and simulations verify that the performance of a hybrid FSO/RF system can be greatly improved by optimizing the symbol mapping and bit interleaving.

## An unequal coding scheme for space image transmission within the framework of CCSDS recommendations

- **Status**: ❌
- **Reason**: CCSDS 표준 LDPC를 그대로 쓴 우주영상 UEP 전송 코딩 스킴, 표준부호 단순재사용·새 LDPC 기여 없음
- **ID**: ieee:7341247
- **Type**: conference
- **Published**: 15-17 Oct.
- **Authors**: Jiachen Sun, Kechao Huang, Xiying Liu +1
- **PDF**: https://ieeexplore.ieee.org/document/7341247
- **Abstract**: In this paper, we propose a new coding scheme for space image transmission, which combines the unequal error protection (UEP) by partial superposition transmission (referred to as UEP-by-PST) with coded modulation standards recommended by the Consultative Committee for Space Data Systems (CCSDS). The raw image is first processed by the recommended image compressor, and then encoded by the UEP-by-PST system. In the UEP-by-PST system, the compressed image sequence is distinguished as two parts, the more important data (MID) and the less important data (LID). Both of the MID and LID are encoded by the CCSDS recommended low-density parity-check (LDPC) code. The codeword corresponding to the LID is superimposed with the codeword (in its interleaved version) corresponding to the MID. Finally, the encoded sequences are modulated by the Gaussian minimum shift keying (GMSK) and transmitted. Numerical results show that, over additive white Gaussian noise (AWGN) channels, the proposed UEP coding scheme outperforms the traditional equal error protection (EEP) coding scheme up to 30 dB in terms of the peak signal to noise ratio (PSNR).

## Low complexity K-Best algorithm based iterative detectors for MIMO-FBMC systems

- **Status**: ❌
- **Reason**: MIMO-FBMC K-Best 검출기 기법, LDPC는 concatenation 베이스라인 언급뿐, 이식할 LDPC ECC 기법 없음
- **ID**: ieee:7341133
- **Type**: conference
- **Published**: 15-17 Oct.
- **Authors**: Ying Fang, Jie Zhong, Minjian Zhao +1
- **PDF**: https://ieeexplore.ieee.org/document/7341133
- **Abstract**: Filter bank multicarrier (FBMC) modulation has many nice features compared with conventional cyclic prefix-based orthogonal frequency multiplexing (CP-OFDM) and has been considered as a promising waveform candidate for future 5G wireless communication. Combining FBMC with multiple-input multiple-output (MIMO) technology may achieve high data rate. In this paper, we propose the K-Best algorithm based uncoded and coded iterative detectors for MIMO-FBMC systems to approach near maximum-likelihood (ML) performance with low computational complexity. The proposed coded detector is capable of supporting soft-outputs, we can concatenate it with soft-input code, such as the LDPC code, to achieve additional performance gain. Meanwhile, we propose interference cancellation method to eliminate the intrinsic interference in the MIMO-FBMC system. Simulation results prove that the proposed detectors achieve approximate ML performance with moderate complexity.

## Design and analysis of irregular sparse code multiple access

- **Status**: ❌
- **Reason**: SCMA(sparse code multiple access) 5G 다중접속 설계로 비-LDPC, 떼어낼 바이너리 LDPC ECC 기법 없음
- **ID**: ieee:7341327
- **Type**: conference
- **Published**: 15-17 Oct.
- **Authors**: Shutian Zhang, Baicen Xiao, Kexin Xiao +2
- **PDF**: https://ieeexplore.ieee.org/document/7341327
- **Abstract**: Sparse Code Multiple Access (SCMA) is an excellent approach to support massive connections and short time-delay, which are the two key requirements in the future fifth generation (5G) communication system. Due to the drawback that traditional SCMA can't serve users with different business needs in the same scenario, we propose an irregular Sparse Code Multiple Access (SCMA) in this paper. In contrast with the traditional SCMA system based on the regular structure, the irregular SCMA can handle massive connections and short time delay in the same system simultaneously by assigning different codebooks with various dimensions for different users who demand for divers performance needs. Simulation results illustrate that irregular SCMA can achieve about 0.7 dB gain over regular SCMA in terms of the same bit error rate (BER) condition.

## Low-complexity soft-output detectors for LDPC coded spatial modulation systems

- **Status**: ❌
- **Reason**: MIMO 공간변조용 soft-output detector (검출기) 기법으로 LDPC는 부수 언급, 떼어낼 LDPC 디코더/HW/코드설계 기법 없음
- **ID**: ieee:7341061
- **Type**: conference
- **Published**: 15-17 Oct.
- **Authors**: Cong Li, Yunpeng Cheng, Yuming Zhang +1
- **PDF**: https://ieeexplore.ieee.org/document/7341061
- **Abstract**: In this paper, we present an efficient transmission scheme for multiple-input multiple-output (MIMO) systems, i.e., low density parity check (LDPC) coded spatial modulation (SM) systems. To exploit the powerful error correction of LDPC code, the key challenge of LDPC coded SM systems is on designing a reliable but low complexity soft-output detector. To tackle this problem, we propose two soft-output detection algorithms based on hard-decision detectors by exploiting the features of M-PSK and M-QAM constellations, namely, PSK-based soft-output detector (PBSOD) and QAM-based soft-output detector (QBSOD). The analytical results show that the number of the searched signal candidates is reduced from NtM to Nt, where Nt is the number of transmit antennas, M is the modulation order. Furthermore, we propose a more general simpler detector, that is, using the absolute value instead of the Frobenius norm to calculate the soft bit metrics. The findings of this paper suggest that the proposed three soft-output detectors for LDPC coded SM systems exhibit lower complexity compared to optimal maximum a posteriori (MAP) log likelihood ratio (LLR) detector and Max-Log detector while imposing only marginal performance degradation. In addition, a comprehensive performance and computational complexity comparison between the proposed detectors and the state-of-the-art detectors is provided to validate the proposed low-complexity detectors. The achieved performance and complexity of the proposed detectors make them suitable candidates for practical coded SM-MIMO systems.

## Experimental evaluation of LDPC-coded OAM based FSO communication in the presence of atmospheric turbulence

- **Status**: ❌
- **Reason**: FSO/OAM 무선광 통신에서 LDPC 코딩이득 실험 — 떼어낼 신규 디코더/구성 기법 없음, LDPC 부수 언급
- **ID**: ieee:7357751
- **Type**: conference
- **Published**: 14-17 Oct.
- **Authors**: Zhen Qu, Ivan B. Djordjevic
- **PDF**: https://ieeexplore.ieee.org/document/7357751
- **Abstract**: A low-density parity check (LDPC)-coded orbital angular momentum (OAM)-based free-space optical (FSO) transmission system is experimentally studied in both the absence and presence of emulator-induced atmospheric turbulence. In the presence of turbulence, the coding gains larger than 6.8 dB are obtained at BER of 10−4 for single OAM mode and dramatic improvement is found in case of LDPC-coded OAM multiplexing of states ±2, ±5 as uncoded case enters into an early error floor phenomenon.

## Complexity and performance of QC-MDPC code-based McEliece cryptosystems

- **Status**: ❌
- **Reason**: McEliece 암호시스템(QC-MDPC 기반) 보안 분석 — 보안/암호 도메인, 채널 ECC 아님. GDBF 언급은 표준 수준
- **ID**: ieee:7357731
- **Type**: conference
- **Published**: 14-17 Oct.
- **Authors**: Omran Al Rasheed, Predrag Ivaniš
- **PDF**: https://ieeexplore.ieee.org/document/7357731
- **Abstract**: In this paper, we analyze security of McEliece cryptosystem based on Low Density Parity Check (LDPC) and Moderate (MDPC) codes, as well as the complexity of the corresponding cryptosystem. Several approaches are proposed to improve the cryptosystem security for the case when complexity of cryptosystem has to be below the prescribed level. A certain modifications of Gradient Descent Bit Flipping (GDBF) decoding algorithm are identified as the crucial part of the cryptosystem that could provide a good trade-off between the complexity cost, decryption latency and security level.

## A channel-adaptive nonbinary LDPC decoder

- **Status**: ❌
- **Reason**: 비이진(nonbinary) LDPC 디코더 — 비이진 LDPC는 제외 대상
- **ID**: ieee:7344983
- **Type**: conference
- **Published**: 14-16 Oct.
- **Authors**: Wenjie Huang, Lei Wang
- **PDF**: https://ieeexplore.ieee.org/document/7344983
- **Abstract**: We propose a low-complexity decoding message truncation technique for nonbinary LDPC decoders by exploiting the extended min-sum algorithm. The proposed technique dynamically adjusts the decoding message length according to channel conditions, thereby reducing the decoding complexity while conforming to the desired level of decoding performance. Utilizing the proposed technique, the decoding operations as well as the power consumption of the non-binary LDPC decoder can be greatly reduced. Simulation results demonstrate that the proposed technique can achieve a better power-performance tradeoff over conventional techniques.

## Parallel block-layered nonbinary QC-LDPC decoding on GPU

- **Status**: ❌
- **Reason**: 비이진(NB) QC-LDPC GPU 디코더 — 비이진 LDPC 제외 대상
- **ID**: ieee:7345000
- **Type**: conference
- **Published**: 14-16 Oct.
- **Authors**: Huyen Thi Pham, Sabooh Ajaz, Hanho Lee
- **PDF**: https://ieeexplore.ieee.org/document/7345000
- **Abstract**: This paper presents an efficient implementation of a parallel block-layered nonbinary quasi-cyclic low-density parity-check (NB-QC-LDPC) decoder on a graphics processing unit (GPU) to achieve significant improvements in both flexibility and scalability. An efficient block-layered scheme and a data structure suitable for parallel computing are proposed to perform decoding on the GPU. The scheme is applied to a min-max decoding algorithm that exploits the inherent massive parallelization capabilities of NB-QC-LDPC decoder. The results of the proposed approach demonstrate that the layered scheme can be efficiently implemented in a GPU device. Moreover, experimental results show that the proposed GPU-based block-layered NB-QC-LDPC decoder provides a faster decoding runtime compare to CPU-based implementation and obtains a coding gain under a low 10-10 BER and low 10-7 FER.

## Low complexity belief propagation polar code decoder

- **Status**: ❌
- **Reason**: polar code BP 디코더(sub-factor-graph freezing) — polar 구조 특화, 바이너리 LDPC BP에 직접 이식되는 기법 아님
- **ID**: ieee:7344986
- **Type**: conference
- **Published**: 14-16 Oct.
- **Authors**: Syed Mohsin Abbas, YouZhe Fan, Ji Chen +1
- **PDF**: https://ieeexplore.ieee.org/document/7344986
- **Abstract**: Since their invention, polar codes have received a lot of attention because of their capacity-achieving performance and low encoding and decoding complexity. Successive cancellation decoding (SCD) and belief propagation decoding (BPD) are two approaches for decoding polar codes. SCD is able to achieve good error-correcting performance and is less computationally expensive as compared to BPD. However SCD suffers from long latency due to the serial nature of the successive cancellation algorithm. BPD is parallel in nature and hence is more attractive for low latency applications. However, since it is iterative, the required latency and energy dissipation increases linearly with the number of iterations. In this work, we borrow the idea of SCD and propose a novel scheme based on sub-factor-graph freezing to reduce the average number of computations as well as the average number of iterations required by BPD, which directly translates into lower latency and energy dissipation. Simulation results show that the proposed scheme has no performance degradation and achieves significant reduction in computation complexity over the existing methods.

## Reduced complexity belief propagation decoders for polar codes

- **Status**: ❌
- **Reason**: polar code BP 디코더, 비-LDPC 부호. SC/factor-graph 의존적이라 바이너리 LDPC BP에 직접 이식 곤란
- **ID**: ieee:7344984
- **Type**: conference
- **Published**: 14-16 Oct.
- **Authors**: Jun Lin, Chenrong Xiong, Zhiyuan Yan
- **PDF**: https://ieeexplore.ieee.org/document/7344984
- **Abstract**: Polar codes are newly discovered capacity-achieving codes, which have attracted lots of research efforts. Polar codes can be efficiently decoded by the low-complexity successive cancelation (SC) algorithm and the SC list (SCL) decoding algorithm. The belief propagation (BP) decoding algorithm not only is an alternative to the SC and SCL decoders, but also provides soft outputs that are necessary for joint detection and decoding. Both the BP decoder and the soft cancelation (SCAN) decoder were proposed for polar codes to output soft information about the coded bits. In this paper, first a belief propagation decoding algorithm, called reduced complexity soft cancelation (RCSC) decoding algorithm, is proposed. Let N denote the block length. Our RCSC decoding algorithm needs to store only 5N - 3 log-likelihood ratios (LLRs), significantly less than 4N - 2+ N log2N/2 and N(log2 N +1) LLRs needed by the BP and SCAN decoders, respectively, when N ≥ 64. Besides, compared to the SCAN decoding algorithm, our RCSC decoding algorithm eliminates unnecessary additions over the real field. Then the simplified SC (SSC) principle is applied to our RCSC decoding algorithm, and the resulting SSC-aided RCSC (S-RCSC) decoding algorithm further reduces the computational complexity. Finally, based on the S-RCSC decoding algorithm, we propose a corresponding memory efficient decoder architecture, which has better error performance than existing architectures. Besides, our decoder architecture consumes less energy on updating LLRs.

## Link-adaptable vector-perturbation ZFBF precoder for multi-point 3D-beamformers

- **Status**: ❌
- **Reason**: VP-ZFBF MIMO 프리코딩/링크적응, LDPC 무관, 떼어낼 ECC 기법 없음
- **ID**: ieee:7412602
- **Type**: conference
- **Published**: 14-16 Oct.
- **Authors**: Masaaki Fujii
- **PDF**: https://ieeexplore.ieee.org/document/7412602
- **Abstract**: A link adaptation scheme is devised for vector-perturbation (VP) zero-forcing beamforming (ZFBF) MIMO precoding and a link-adaptable VP-ZFBF precoder is applied to multi-point three-dimensional (3D) beamformers to be used in mmWave-band wireless access systems. Channel coding schemes used in current systems, e.g., turbo codes, possess systematic code structures. The perturbation gain can thus be predicted by searching for perturbation vectors for the symbol vectors mapped from information bits. On the basis of this principle, we constructed an efficient iterative modulation-and-coding-set (MCS) selection procedure for VP-ZFBF precoding. Simulation results demonstrate that our proposed scheme suitably passed on the perturbation gain to the selection of higher MCS and thus achieved high throughputs by incorporating with multi-point 3D-beamformers.

## Construction of polar codes for channels with memory

- **Status**: ❌
- **Reason**: 메모리 채널용 polar code SC 디코더 — 비-LDPC, polar 전용 기법으로 LDPC BP에 이식 불가
- **ID**: ieee:7360760
- **Type**: conference
- **Published**: 11-15 Oct.
- **Authors**: Runxin Wang, Junya Honda, Hirosuke Yamamoto +2
- **PDF**: https://ieeexplore.ieee.org/document/7360760
- **Abstract**: Polar codes for channels with memory are considered in this paper. ŗaşoğlu proved that Arikan's polarization applies to finite-state memory channels but practical decoding algorithms of polar codes for such channels have been unknown. This paper proposes a generalization of successive cancellation algorithm for channels with memory where the complexity is polynomial in the number of states. In addition, two polar coding scheme are proposed to generate codewords following non-i.i.d. process required to achieve the capacity. Whereas one is a simple application of the polar coding scheme for asymmetric memoryless channels, the other one combines a polar code with a fixed-to-variable length homophonic coding scheme, which can realize the input distribution exactly equal to the target process.

## Threshold saturation for spatially coupled turbo-like codes over the binary erasure channel

- **Status**: ❌
- **Reason**: SC turbo/braided convolutional code BEC threshold saturation 증명 — 비-LDPC, 이론 분석, 이식 BP 기법 없음
- **ID**: ieee:7360750
- **Type**: conference
- **Published**: 11-15 Oct.
- **Authors**: Saeedeh Moloudi, Michael Lentmaier, Alexandre Graell i Amat
- **PDF**: https://ieeexplore.ieee.org/document/7360750
- **Abstract**: In this paper we prove threshold saturation for spatially coupled turbo codes (SC-TCs) and braided convolutional codes (BCCs) over the binary erasure channel. We introduce a compact graph representation for the ensembles of SC-TC and BCC codes which simplifies their description and the analysis of the message passing decoding. We demonstrate that by few assumptions in the ensembles of these codes, it is possible to rewrite their vector recursions in a form which places these ensembles under the category of scalar admissible systems. This allows us to define potential functions and prove threshold saturation using the proof technique introduced by Yedla et al‥

## Toward limits of constructing reliable memories from unreliable components

- **Status**: ❌
- **Reason**: 불신뢰 부품 신뢰메모리 구성 converse 정리 — 순수 이론 bound, 디코더/HW/구성으로 안 이어짐
- **ID**: ieee:7360745
- **Type**: conference
- **Published**: 11-15 Oct.
- **Authors**: Lav R. Varshney
- **PDF**: https://ieeexplore.ieee.org/document/7360745
- **Abstract**: There has been long-standing interest in constructing reliable memory systems from unreliable components like noisy bit-cells and noisy logic gates, under circuit complexity constraints. Prior work has focused exclusively on constructive achievability results, but here we develop converse theorems for this problem for the first time. The basic technique relies on entropy production/dissipation arguments and balances the need to dissipate entropy with the redundancy of the code employed. A bound from the entropy dissipation capability of noisy logic gates is used via a sphere-packing argument. Although a large gap remains between refined achievability results stated herein and the converse, some suggestions for ways to move forward beyond this first step are provided.

## Analysis of spatially-coupled counter braids

- **Status**: ❌
- **Reason**: Spatially-coupled counter braid 플로우 측정 압축 분석 — 채널 ECC 아닌 측정/소스코딩
- **ID**: ieee:7360749
- **Type**: conference
- **Published**: 11-15 Oct.
- **Authors**: Eirik Rosnes, Alexandre Graell i Amat
- **PDF**: https://ieeexplore.ieee.org/document/7360749
- **Abstract**: A counter braid (CB) is a novel counter architecture introduced by Lu et al. in 2007 for per-flow measurements on high-speed links. CBs achieve an asymptotic compression rate (under optimal decoding) that matches the entropy lower bound of the flow size distribution. Spatially-coupled CBs (SC-CBs) have recently been proposed. In this work, we further analyze single-layer CBs and SC-CBs using an equivalent bipartite graph representation of CBs. On this equivalent representation, we show that the potential and area thresholds are equal. We also show that the area under the extended belief propagation (BP) extrinsic information transfer curve (defined for the equivalent graph), computed for the expected residual CB graph when a peeling decoder equivalent to the BP decoder stops, is equal to zero precisely at the area threshold. This, combined with simulations and an asymptotic analysis of the Maxwell decoder, leads to the conjecture that the area threshold is in fact equal to the Maxwell decoding threshold and hence a lower bound on the maximum a posteriori (MAP) decoding threshold. Finally, we present some numerical results and give some insight into the apparent gap of the BP decoding threshold of SC-CBs to the conjectured lower bound on the MAP decoding threshold.
