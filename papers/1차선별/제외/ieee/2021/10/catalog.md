# IEEE Xplore — 2021-10


## On Blind Frame Synchronization of LDPC Codes

- **Status**: ❌
- **Reason**: LDPC 블라인드 프레임 동기화(syndrome likelihood) — 디코더/코드설계/HW 신규 기여 아님, NAND ECC에 이식할 기법 없음
- **ID**: ieee:9507478
- **Type**: journal
- **Published**: Oct. 2021
- **Authors**: Rodrigue Imad, Sebastien Houcke
- **PDF**: https://ieeexplore.ieee.org/document/9507478
- **Abstract**: We consider in this letter the problem of blind frame synchronization of Low Density Parity-Check (LDPC) codes. We present and compare new methods of blind frame synchronization based on the calculation of Likelihood functions of the syndrome. Simulation results show that the four proposed synchronization techniques are effective once applied to LDPC codes. The method that involves the maximization of the Likelihood Difference (LD) function of the parity-checks, presents the best results in terms of probability of false synchronization.

## Protograph LDPC-Coded BICM-ID With Irregular CSK Mapping in Visible Light Communication Systems

- **Status**: ❌
- **Reason**: VLC용 CSK 변조+BICM-ID 응용. protograph LDPC는 표준 PEXIT 구성, 무선/광통신 응용 특이적이라 떼어낼 신규 코드설계 기법 없음
- **ID**: ieee:9519519
- **Type**: journal
- **Published**: Oct. 2021
- **Authors**: Lin Dai, Yi Fang, Zhaojie Yang +2
- **PDF**: https://ieeexplore.ieee.org/document/9519519
- **Abstract**: This paper designs and analyzes the bit-interleaved coded modulation with iterative demapping and decoding (BICM-ID) framework under color-shift-keying (CSK) modulation to achieve spectrally efficient transmissions in visible light communication (VLC) systems. Specifically, we investigate the protograph low-density parity-check (LDPC) codes, bit-to-symbol mapping schemes, and constellation labeling rules in higher-order CSK-aided VLC systems. To fully explore the BICM-ID benefit, we propose an irregular CSK mapping, in which an $M$-ary standardized constellation (called “Standard constellation”) and a new $M$-ary constellation (called “Target constellation”) are separately applied to modulate two different coded sub-blocks in a codeword to optimize the error performance of the CSK-aided VLC systems. Furthermore, using a modified protograph extrinsic information transfer (PEXIT) algorithm, we construct two types of protograph LDPC codes (i.e., unpunctured and punctured protograph LDPC codes) that outperform the conventional protograph LDPC codes. Both analytical and simulation results show that the proposed irregular-CSK-mapped BICM-ID employing the new protograph LDPC codes and Target constellation is capable of achieving outstanding performance, and is a promising transmission solution for high-speed VLC applications.

## Parity Check Aided SC-Flip Decoding Algorithms for Polar Codes

- **Status**: ❌
- **Reason**: polar 코드 SC-Flip 디코딩. LDPC 아님, 이식 LDPC 기법 없음
- **ID**: ieee:9520274
- **Type**: journal
- **Published**: Oct. 2021
- **Authors**: Bin Dai, Chenyu Gao, Zhiyuan Yan +1
- **PDF**: https://ieeexplore.ieee.org/document/9520274
- **Abstract**: When polar codes are decoded by the successive cancellation (SC) decoding algorithm, erroneously decoded non-frozen bits are caused by either channel noise or error propagation. SC-Flip algorithms aim to improve error performance by first identifying erroneous hard decisions due to channel noise and then flipping them during the decoding process to reduce error propagation. In existing SC-Flip algorithms, cyclic redundancy check (CRC) is used to check the decoded codeword to detect incorrect hard decisions. Differing from this detection approach based on CRC, we propose new SC-Flip decoders that take advantage of both the CRC and distributed parity checks (PCs) to detect, identify and flip erroneously decoded non-frozen bits. The proposed decoders terminate SC decoding early when a distributed PC is not satisfied. In addition, we propose a new metric to help locate the incorrect hard decisions. Finally, simulation results demonstrate that our SC-Flip decoders achieve better performance complexity tradeoffs than prior flipping algorithms, and approach the performance and complexity of the SC-Oracle algorithms.

## Balanced Product Quantum Codes

- **Status**: ❌
- **Reason**: 양자 LDPC(qLDPC) 코드 구성. balanced product 등 양자 전용 구성으로 고전 바이너리 LDPC에 직접 이식 불가 — 원칙 제외
- **ID**: ieee:9490244
- **Type**: journal
- **Published**: Oct. 2021
- **Authors**: Nikolas P. Breuckmann, Jens N. Eberhardt
- **PDF**: https://ieeexplore.ieee.org/document/9490244
- **Abstract**: This work provides the first explicit and non-random family of [[N,K,D]] LDPC quantum codes which encode K ∈ Θ(N4/5) logical qubits with distance D ∈ Ω(N3/5). The family is constructed by amalgamating classical codes and Ramanujan graphs via an operation called balanced product. Recently, Hastings-Haah-O'Donnell and Panteleev-Kalachev were the first to show that there exist families of LDPC quantum codes which break the polylog(N)√N distance barrier. However, their constructions are based on probabilistic arguments which only guarantee the code parameters with high probability whereas our bounds hold unconditionally. Further, balanced products allow for non-abelian twisting of the check matrices, leading to a construction of LDPC quantum codes that can be shown to have K ∈ Θ(N) and that we conjecture to have linear distance D ∈ Θ(N).

## Primitive Rateless Codes

- **Status**: ❌
- **Reason**: Primitive rateless 코드(m-sequence 기반), 가중치분포/최소거리 이론. LDPC 아니고 rateless, 떼어낼 LDPC 디코더/HW 없음
- **ID**: ieee:9481932
- **Type**: journal
- **Published**: Oct. 2021
- **Authors**: Mahyar Shirvanimoghaddam
- **PDF**: https://ieeexplore.ieee.org/document/9481932
- **Abstract**: In this paper, we propose primitive rateless (PR) codes. A PR code is characterized by the message length and a primitive polynomial over  $\mathbf {GF}(2)$ , which can generate a potentially limitless number of coded symbols. We show that codewords of a PR code truncated at any arbitrary length can be represented as subsequences of a maximum-length sequence ( $m$ -sequence). We characterize the Hamming weight distribution of PR codes and their duals and show that for a properly chosen primitive polynomial, the Hamming weight distribution of the PR code can be well approximated by the truncated binomial distribution. We further find a lower bound on the minimum Hamming weight of PR codes and show that there always exists a PR code that can meet this bound for any desired codeword length. We provide a list of primitive polynomials for message lengths up to 40 and show that the respective PR codes closely meet the Gilbert-Varshamov bound at various rates. Simulation results show that PR codes can achieve similar block error rates as their BCH counterparts at various signal-to-noise ratios (SNRs) and code rates. PR codes are rate-compatible and can generate as many coded symbols as required; thus, demonstrating a truly rateless performance.

## Partially Information Coupled Bit-Interleaved Polar Coded Modulation

- **Status**: ❌
- **Reason**: polar 코드(spatially coupled polar coded modulation) 기반. LDPC 아님, 떼어낼 LDPC ECC 기법 없음
- **ID**: ieee:9491085
- **Type**: journal
- **Published**: Oct. 2021
- **Authors**: Xiaowei Wu, Min Qiu, Jinhong Yuan
- **PDF**: https://ieeexplore.ieee.org/document/9491085
- **Abstract**: In this paper, we propose partially information coupled bit-interleaved polar coded modulation (PIC-BIPCM), which is a class of spatially coupled polar coding schemes designed for  $2^{Q}$ -ary modulations. Specifically, we consider PIC-BIPCM schemes respectively constructed with three BIPCM schemes: direct BIPCM, punctured BIPCM, and multi-kernel BIPCM. We analyze the error performance of the proposed PIC-BIPCM over the binary erasure channel (BEC) via density evolution. With the analysis as a guideline, we jointly design the positions of coupled bits and the modulation bit-mapper by taking into account the partial polarization of finite length polar codes as well as the unequal error protection of high order modulations. Simulation results demonstrate significant performance improvement of the proposed PIC-BIPCM over the uncoupled BIPCM on both BEC and AWGN channels.

## HD-Code: End-to-End High Density Code for DNA Storage

- **Status**: ❌
- **Reason**: DNA 저장용 소스 인코딩/압축 기법(HD-code). 채널코딩 ECC가 아니며 LDPC 언급 없음
- **ID**: ieee:9504568
- **Type**: journal
- **Published**: Oct. 2021
- **Authors**: Jianjun Wu, Shufang Zhang, Tao Zhang +1
- **PDF**: https://ieeexplore.ieee.org/document/9504568
- **Abstract**: With the rapid development of digital information techniques, the use of DNA media for information storage is considered as the future direction of data storage. Existing DNA storage schemes simply map compressed binary multimedia data into DNA base data, which has the disadvantages of data loss, low logical storage density and high cost of synthesis. This paper presents an end-to-end high density DNA encoding algorithm(referred to as HD-code, where HD stands for high density). The novelty and contributions of this work contain three parts. First, by taking full advantage of the statistical characteristics of the original multimedia data and considering the biological constraints on the DNA bases, the proposed scheme achieves higher logical storage density and improves the flexibility and consistency in data storage. Second, by performing data conversion, the proposed scheme can effectively encode extreme images with large proportion of single color. Third, the proposed method can reconstruct high quality images and reduce synthesis costs by yielding better rate-PSNR(Peak Signal to Noise Ratio).

## Systematic Polar Coded Modulation for Informed Receivers

- **Status**: ❌
- **Reason**: Informed receiver용 systematic polar coded modulation. Polar 코드, LDPC 아니며 떼어낼 LDPC 기법 없음
- **ID**: ieee:9476031
- **Type**: journal
- **Published**: Oct. 2021
- **Authors**: Shin-Lin Shieh, Yu-Chih Huang, Po-Ning Chen +1
- **PDF**: https://ieeexplore.ieee.org/document/9476031
- **Abstract**: The problem of coding for informed receivers (IR) is considered, where a transmitter multicasts a bunch of messages to its associated receivers, each of which already has a subset of messages as side information. Which receiver has what side information is unknown to the transmitter. A family of polar codes for IR was proposed for binary-input channels in (Huang and Shieh, 2018), which was shown to provide excellent side information gain regardless of side information configuration and content. A trial extension of this scheme to high-order modulations, however, was unsatisfactory. In this paper, two families of systematic polar coded modulations for IR are proposed. In the first family, by building a connection between the message bits and modulated symbols under systematic polar codes, we leverage the bit assignments and labeling techniques such that receiver side information can be directly translated to a minimum distance gain. In the second family, a permutation operation is added before modulation such that the message bits can be properly reordered to further advance and balance the gains among different side information configurations. Simulations show that the proposed schemes provide large and balanced side information gains and significantly outperform the system directly adapted from (Huang and Shieh, 2018) onto high-order modulations.

## A New Two-User Binary Polar Coded Multiple Access Scheme With Power and Rate Allocation

- **Status**: ❌
- **Reason**: polar 코드 기반 다중접속 방식. LDPC 아님(LDPC는 비교 베이스라인일 뿐), 이식 기법 없음
- **ID**: ieee:9496590
- **Type**: journal
- **Published**: Oct. 2021
- **Authors**: Benjamin K. Ng, Chan-Tong Lam
- **PDF**: https://ieeexplore.ieee.org/document/9496590
- **Abstract**: A new polar-code-based scheme with power and rate allocation is proposed to enhance the block error rate (BLER) performance in a two-user binary Gaussian multiple access channel (GMAC). Unlike previous works which mainly focused on the capacity-achieving capability of polar codes in the multiple access channel, we improve their finite-blocklength coding performance in the specific two-user channel. In our proposed scheme, each user employs two blocks of polar codes with unequal transmit power levels, and a notable feature of our approach is that the code construction and rate allocation of these two blocks as well as their power levels can be jointly optimized to give rise to performance improvement. We analytically derive the BLER upper bound of the proposed scheme using the information-theoretic coding performance approximation in the finite blocklength regime. We demonstrate the validity of our approach through simulations and show the performance advantages of the proposed scheme over the previously reported two-user LDPC-based and polar-coded GMAC of similar blocklength.

## Review of Joint Encoding and Encryption for Image Transmission using Chaotic Map, LDPC and AES Encryption

- **Status**: ❌
- **Reason**: 이미지 암호화+LDPC 결합 리뷰, LDPC는 신뢰성 보조 베이스라인, 새 디코더/구성 기법 없음
- **ID**: ieee:9609351
- **Type**: conference
- **Published**: 7-9 Oct. 2
- **Authors**: Kanchan Yadav, Trushita Chaware
- **PDF**: https://ieeexplore.ieee.org/document/9609351
- **Abstract**: In today’s era of communication, sharing of information is unavoidable. Analysis of security and reliability while communicating is essential. Information may get altered, copied and copyright can be infringed. Previously, digital watermarking and different encryption techniques like AES, DES, HASH and MAC were used as a primary security technique for information hiding. But, in all these methods, there are some vulnerabilities, because of which information may be hacked or changed while transmission. In addition to the security of the information, there should also be an error-free transmission of data. This review paper discusses various image encryption techniques which are using joint error correction and encryption methods. Based on the literature review, a novel method for joint encryption and encoding is suggested. Low-Density Parity-Check (LDPC) code, a highly recommended technique in 5G, is used for reliability. Chaotic sequence based on a logistic map is used for security. Proposed technique also uses the S-Box of AES algorithm for enhancing the security obtained by combining LDPC and Chaotic sequence. This paper aims to provide a general overview of image encryption techniques. Based on the study, a new system for joint encryption and encoding using LDPC, Chaotic map and AES S-Box is suggested.

## An Energy-saving Approach for Error control Codes in Wireless Sensor Networks

- **Status**: ❌
- **Reason**: WSN ECC 서베이, 무선 응용 일반론, 떼어낼 LDPC 기법 없음
- **ID**: ieee:9591677
- **Type**: conference
- **Published**: 7-9 Oct. 2
- **Authors**: Satwinder Kaur, Deepak B Kuttan, Nitin Mittal
- **PDF**: https://ieeexplore.ieee.org/document/9591677
- **Abstract**: Wireless Sensor Networks (WSNs) have limited energy resource which requires authentic data transmission at a minimum cost. The major challenge is to deploy WSN with limited energy and lifetime of nodes while taking care of secure data communication. The transmission of data from the wireless channels may cause many losses such as fading, noise, bit error rate increases as well as deplete the energy resource from the nodes. To reduce the adverse effects of losses and to save power usage, error control coding (ECC) techniques are widely used and it also brings coding gain. Since WSN have limited energy resource so the selection of ECC is very difficult as both power consumption, as well as BER, has also taken into consideration. This research paper reviews different types of models, their applications, limitations of the sensor networks, and what are different types of future works going to overcome the limitations.

## Performance Analyses of Hybrid-ARQ in Fifth Generation New Radio

- **Status**: ❌
- **Reason**: 5G NR HARQ BLER/throughput 성능분석; 표준 LDPC 사용, 신규 디코더·코드설계 기여 없음
- **ID**: ieee:9587674
- **Type**: conference
- **Published**: 5-8 Oct. 2
- **Authors**: Ural Mutlu, Yasin Kabalcı
- **PDF**: https://ieeexplore.ieee.org/document/9587674
- **Abstract**: The main design criteria of the Fifth-generation (5G) New Radio (NR) specifications are to improve the requirements that enable high-speed, high-reliability, and low-latency communications. To achieve these design requirements, 5G NR specifications have defined the use of Low Density Parity Check (LDPC) codes channel coding scheme for data channels. LDPC codes have been chosen specifically because of their support for wide range of block sizes and code rates as well as their compatibility with Hybrid Automatic Repeat Request (HARQ) protocol. HARQ combines ARQ retransmission scheme with LDPC Forward Error Correction (FEC). In HARQ, a retransmitted code block consists of a different set of parity bits belonging to the same transport block and soft combining of previous copy and retransmitted copy is performed at the receiver. The new set of parity bits effectively reduces the coding rate for the FEC and achieve higher reliability. The objective of this research is to analyse the block error rate (BLER) and throughput performance of the HARQ protocol in 5G NR. The study, first, introduces LDPC codes and explains how LDPC rate matching is combined with HARQ protocol to improve performance. Then, BLER and throughput simulation results for various coding rates and transport block sizes in Tapped Delayed Line (TDL) channel models are presented. The results show that incremental redundancy combining in HARQ improves throughput, reliability, and latency.

## Evaluating the Productivity of HDL Efficient Coding Models for 5G Information Networks

- **Status**: ❌
- **Reason**: 5G HDL 코딩 모델 성능비교(turbo/LDPC/polar); 표준 부호 비교 수준, 신규 HW 디코더 아키텍처 기여 불명확하나 떼어낼 새 기법 없음
- **ID**: ieee:9772185
- **Type**: conference
- **Published**: 5-7 Oct. 2
- **Authors**: Ilya Pyatin, Juliy Boiko, Oleksander Eromenko
- **PDF**: https://ieeexplore.ieee.org/document/9772185
- **Abstract**: The article studies the principles of constructing encoders and decoders using the hardware description language (HDL). Models of efficient coding systems for information networks of 5G technology are proposed. Evaluation of the effectiveness of the proposed models was carried out by research and comparison of the performance of turbo codes, LDPC and polar codes. The architecture of efficient coding systems, HDL coding algorithms are described, recommendations are given for the configuration, interleaving, framing, and delay procedures. The productivity of coding systems is carried out by setting the bit error rate (BER) for different information block lengths and coding rates. During the research, signal-code constructions were used that cover various scenarios of reliability and high-throughput networks. It is assumed that the results obtained will be useful in the design processes of practical coding schemes in 5G networks.

## Iterative Soft Decoding of Single Parity Check Convolutional Concatenated Code

- **Status**: ❌
- **Reason**: SPC-convolutional concatenated turbo형 디코딩 — LDPC 아님, 이식 가능한 LDPC ECC 기법 없음
- **ID**: ieee:9524973
- **Type**: conference
- **Published**: 4-7 Oct. 2
- **Authors**: Junmei Chen, Hao Chen, Zongpeng Li
- **PDF**: https://ieeexplore.ieee.org/document/9524973
- **Abstract**: By establishing a single parity check relationship between convolutional codewords, a concatenated code, termed single parity check convolutional code (SPC-CC), is proposed. By jointly en/decoding the SPC and CC, as well as carefully allocating redundant information between the pair, we can improve BER more promptly during iterative decoding. Each codeword in SPC-CC consists of only one SISO decoder, which generates one extrinsic information. The key is to simulate another using extrinsic information from other decoders. Then iteratively feed back extrinsic information to each other in a manner similar to a Turbo engine. We design en/decoding scheme of the SPC-CC, and then analyze its performance and complexity. Simulation results show that SPC-CC can effectively improve communication reliability with a moderate complexity. In addition, thanks to SPC code, SPC-CC can correct packet erasures due to fading or interference.

## Effectiveness of Using Codes With a Sparse Check Matrix for Protection against Algebraic Manipulations

- **Status**: ❌
- **Reason**: sparse check matrix를 대수적 조작 공격 방어용 보안 코드로 사용 - 채널코딩 ECC 아님, 디코더/구성 기여 없음
- **ID**: ieee:9639491
- **Type**: conference
- **Published**: 30 Sept.-2
- **Authors**: Alla Levina, Gleb Ryaskin, Sergey Taranov +1
- **PDF**: https://ieeexplore.ieee.org/document/9639491
- **Abstract**: This article presents codes with a sparse check matrix and demonstrates its possibilities for analysis error masking probability in the case of algebraic manipulations. The illustrated scheme is based on bent functions calculating redundancy using boolean functions. The paper presents the resistance of created code construction to various types of errors. Moreover, the paper considered the strong algebraic manipulation model, this model takes into account the prior knowledge of the attacker about the sparseness of the code check matrix.

## Parallel Concatenated Code Combining Polar Code and LDPC Code on AWGN Channel

- **Status**: ❌
- **Reason**: Polar+LDPC 병렬 연접 구조. LDPC는 베이스라인 연접 요소, NAND에 이식할 새 LDPC 디코더·구성 기여 없음.
- **ID**: ieee:9651728
- **Type**: conference
- **Published**: 29-31 Oct.
- **Authors**: Luyao Ma, Lijun Zhang
- **PDF**: https://ieeexplore.ieee.org/document/9651728
- **Abstract**: Both polar code and Low-Density Parity-Check (LDPC) code have been adopted in 3GPP eMBB scenario. Some scholars have proposed a serial concatenation structure combining these two codes. However, the inner code needs to add redundant bits to protect the redundant bits of the outer code in the serial concatenation. In this paper, we propose a parallel concatenation code combining polar code and LDPC code on the AWGN channel, which does not distinguish the inner code from the outer code. In the proposed concatenated structure, the BP algorithm is used to decode polar code, and the output soft information of BP decoder is logarithmically processed before LDPC decoding. According to the simulation results, compared with the serial concatenated code with the same code rate and code length, the parallel concatenated code has better BER(Bit-Error-Rate) performance.

## Research on Nonbinary LDPC-OTFS Scheme in High Mobile Communication Scenarios

- **Status**: ❌
- **Reason**: 비이진(nonbinary) LDPC-OTFS — 비이진 LDPC 즉시 제외
- **ID**: ieee:9659787
- **Type**: conference
- **Published**: 27-28 Oct.
- **Authors**: Hai Tian, Danfeng Zhao, Haoxiang Jia
- **PDF**: https://ieeexplore.ieee.org/document/9659787
- **Abstract**: The high mobility scenarios supported by B5G/6G, such as high-speed trains and satellite communications, etc., which will produce large Doppler shifts, resulting in a sharp deterioration of communication performance. In response to the demand for higher spectrum and power efficiency, as well as higher reliability and lower latency specifications for future communications, the paper investigates a nonbinary LDPC-OTFS coding and modulation scheme for high mobility scenarios. First, a layered min-max decoding algorithm based on the early termination criterion is studied to further improve the decoding performance and reduce the decoding complexity. Then the novel OTFS modulation technique is analyzed to overcome the malignant effect of large Doppler shift on the communication system and improve the spectral efficiency. Finally, a nonbinary LDPC-OTFS link scheme is built to simulate and analyze the BER performance under different scenarios. The results show that the proposed scheme has better performance and robustness compared to the 5G NR LDPC-OFDM scheme.

## Concatenated Turbo Polar Codes: An Overview

- **Status**: ❌
- **Reason**: Turbo Polar codes 개관, LDPC 아님. 떼어낼 LDPC ECC 기법 없음
- **ID**: ieee:9733079
- **Type**: conference
- **Published**: 27-28 Oct.
- **Authors**: Wallaa Y. Alebady, Ahmed A. Hamed
- **PDF**: https://ieeexplore.ieee.org/document/9733079
- **Abstract**: Although the polar codes can achieve the Binary-Input Discrete Memoryless Channel (BI-DMLC) capacity, their performance deteriorates at the finite-code lengths, especially in small SNRs. Therefore, the Turbo Polar Codes are proposed to improve the performance of polar codes in a finite-length regime. In this paper, several turbo polar codes are presented to review the state of the art in Turbo polar codes.

## New Code-Based Cryptosystem Based on Binary Image of Generalized Reed-Solomon Code

- **Status**: ❌
- **Reason**: GRS 코드 기반 McEliece 암호시스템 — 코드 기반 암호, ECC 디코더/구성 기여 아님
- **ID**: ieee:9606467
- **Type**: conference
- **Published**: 25-29 Oct.
- **Authors**: Fedor Ivanov, Eugenii Krouk, Victor Zyablov
- **PDF**: https://ieeexplore.ieee.org/document/9606467
- **Abstract**: McEliece cryptosystem represents a smart open key system based on the hardness of the decoding of an arbitrary linear code, which is believed to be able to resist the advent of quantum computers. But the original McEliece cryptosystem, based on Goppa codes, has just very limited interest in practice, partly because it requires a very large public key. In this paper we propose a new instance of McEliece cryptosystem that reduces a public key size. This cryptosystem is based on images of Generalized Reed-Solomon (GRS) codes. It was shown that in order to break the proposed system, intruder has to solve a decoding problem for a code that is not equivalent to private GRS code.

## Novel order statistics–based detector and coded modulation for a DHA FH OFDMA system

- **Status**: ❌
- **Reason**: DHA FH OFDMA 검출기/coded modulation, LDPC ECC 무관 무선 응용 특이적
- **ID**: ieee:9606461
- **Type**: conference
- **Published**: 25-29 Oct.
- **Authors**: Dmitry Osipov
- **PDF**: https://ieeexplore.ieee.org/document/9606461
- **Abstract**: Coded DHA FH OFDMA communication systems that use order statistics-based detectors are promising candidates for applications such as IoT and M2M. For the majority of order statistics-based reception techniques the high throughput coded modulation schemes development remains an open problem. In what follows a novel order-statistics based detector that outperforms the classical Maximum Rank Sum detector is introduced. The proposed detector is then used to design a practical coded modulation scheme for a multi-tone multi-band DHA FH OFDMA that provides better latency-performance tradeoff than any order statistics-based reception method proposed so far.

## Linear Programming Decoding of Non-Linear Sparse-Graph Codes

- **Status**: ❌
- **Reason**: 비선형 sparse-graph 코드(LDMC) — NAND 표준 바이너리 선형 LDPC와 무관한 비선형 코드 클래스, 이식성 없음
- **ID**: ieee:9606454
- **Type**: conference
- **Published**: 25-29 Oct.
- **Authors**: Gleb Balitskiy, Alexey Frolov, Pavel Rybin
- **PDF**: https://ieeexplore.ieee.org/document/9606454
- **Abstract**: In modern coding theory, linear code constructions are mainly used. Their properties and fundamental theoretical limits are well studied, and they are successfully applied to different classes of problems. Until now, non-linear codes did not attract much attention from specialists because linear structures have coped with their tasks and have the required research tools developed earlier. But in a series of works devoted to the study of codes with graceful degradation, H. Roozbehani, and Y. Polyanskiy proposed the construction of non-linear low-density majority codes (LDMC) and effective encoding and decoding algorithms for them. Moreover, they showed that LDMC has a lower bit error rate (BER) than any linear code in the error-reducing regime for the binary erasure channel (BEC). Given this motivation, we consider non-linear sparse-graph codes (a generalized version of LDMC) and investigate their performance in the AWGN channel. For this class of codes, we proposed efficient generalized BP-based and LP-based decoding algorithms. We accurately estimated BER under ML decoding of non-linear codes based on the LP-based decoder. Also, by simulation, we carried out the analysis and comparison of performances of various non-linear codes.

## SDN/NFV based Secure SCMA design in SDR

- **Status**: ❌
- **Reason**: SDN/NFV SCMA 코드할당·보안 설계, LDPC 무관 — 떼어낼 ECC 기법 없음
- **ID**: ieee:9615517
- **Type**: conference
- **Published**: 25-29 Oct.
- **Authors**: Müge Erel-Özçevik, Ferdi Tekçe
- **PDF**: https://ieeexplore.ieee.org/document/9615517
- **Abstract**: Due to increased mMTC devices in 5G, OFDMA has not been a solution for resource allocation in SDR. Therefore; SCMA which is one of the code domain NOMA has been using in such overloaded cases. As distinct from OFDMA, it uses also the constellation diagram as an addition to frequency and time domains in resource mapping to the mobile user equipment. The current studies do not consider UE prioritization while code allocation in SCMA is believed to enhance QoS of the whole topology. Moreover, due to the nature of SCMA, protecting the privacy of UE has become harder than conventional allocation strategies. The implementation details of secure SCMA does not consider by handling low OPEX/CAPEX. Therefore, in this paper, we introduce a novel SDN/NFV based SDR by handling these 5G paradigms into the same platform to overcome the aforementioned challenges. With SDN, we newly define a QoS metric; i.e. received power over overloading of SDR, for UE prioritization such as Micro and Macro UE in an SDR. With NFV, SDR can have two virtual roles shown to UEs by Macrocell and Microcell virtual network functions. With SDR, the SCMA code allocation is performed according to defined Macro and Micro codes are taken from generated codebooks. Afterward, it performs the asymmetric encryption algorithm to provide security of code allocations and the privacy of the user. According to performance evaluation; when overloading is 150%, the Micro UEs have 10x better BER than Macro UEs where the QoS is acceptable for the whole topology.

## End-to-end Learning Based Bit-wise Autoencoder for Optical OFDM Communication System

- **Status**: ❌
- **Reason**: 광 OFDM 비트단위 오토인코더 성상도 최적화; LDPC ECC 무관
- **ID**: ieee:9737838
- **Type**: conference
- **Published**: 24-27 Oct.
- **Authors**: Wenshan Jiang, Tao Xu, Qun Liu +5
- **PDF**: https://ieeexplore.ieee.org/document/9737838
- **Abstract**: We propose an end-to-end autoencoder for optical OFDM communication system, which is trained based on bit-wise mutual information (BMI). The simulation results show that the autoencoder can optimize the constellations and achieve BER performance improvement.

## EFM: Elastic Flash Management to Enhance Performance of Hybrid Flash Memory

- **Status**: ❌
- **Reason**: NAND 플래시 관리(ISPP/지연/수명) 스킴; ECC·LDPC 디코더 기여 없음, ISPP 운영만
- **ID**: ieee:9643814
- **Type**: conference
- **Published**: 24-27 Oct.
- **Authors**: Bingzhe Li, Bo Yuan, David Du
- **PDF**: https://ieeexplore.ieee.org/document/9643814
- **Abstract**: NAND-based flash memory has become a prevalent storage media due to its low access latency and high performance. By setting up different incremental step pulse programming (ISPP) values and threshold voltages, the tradeoffs between lifetime and access latency in NAND-based flash memory can be exploited. The existing studies that exploit the tradeoffs by using heuristic algorithms do not consider the dynamically changed access latency due to wearing-out, resulting in low access performance. In this paper, we proposed a new Elastic Flash Management scheme, called EFM, to manage data in hybrid flash memory, which consists of multiple physical regions with different read/write latencies according to their ISPP values and threshold voltages. EFM includes a Long-Term Classifier (LT-Classifier) and a Short-Term Classifier (ST-Classifier) to accurately track dynamically changed workloads by considering current quantitative differences of read/write latencies and workload access patterns. Moreover, a reduced effective wearing management is proposed to prolong the lifetime of flash memory by scheduling write-intensive workloads to the region with a reduced threshold voltage and the lowest write cost. Experimental results indicate that EFM reduces the average read/write latencies by about 54% - 296% and obtain 17.7% lifetime improvement on average compared to the existing studies.

## Concatenated RS-LDPC Coding for Water-to-Air Visible Light Communication Through Wavy Water Surface

- **Status**: ❌
- **Reason**: RS-LDPC concatenation for underwater VLC; LDPC는 표준 베이스라인이고 떼어낼 신규 디코더·구성·HW 기여 없음. 무선 응용 특이적.
- **ID**: ieee:9613593
- **Type**: conference
- **Published**: 20-22 Oct.
- **Authors**: Chunfang Fu, Chen Gong, Nuo Huang +2
- **PDF**: https://ieeexplore.ieee.org/document/9613593
- **Abstract**: Considering large variation range of water-to-air (W2A) channel, we adopt concatenated Reed Solomon-Low Density Parity Check (RS-LDPC) code for W2A visible light communication (VLC), where LDPC code is adopted for error-correcting and RS code is adopted for erasure-correcting caused by LDPC decoding failure. A W2A-VLC link is established using green light emitting diode (LED) to investigate the code performance under wavy water surface condition. We test two coding schemes with different lengths and rates under 10 MSym/s transmission symbol rate. Experimental results show that the concatenated RS-LDPC code can improve the reliability of the W2A-VLC system.

## Quantum-Assisted Decoding for Non-Binary Low-Density Parity-Check Codes

- **Status**: ❌
- **Reason**: 비이진(NB-LDPC) 양자보조 디코딩 — 비이진 LDPC라 즉시 제외(NAND는 바이너리 LDPC).
- **ID**: ieee:9621026
- **Type**: conference
- **Published**: 20-22 Oct.
- **Authors**: Hyunwoo Jung, Jeonghwan Kang, Jeongseok Ha
- **PDF**: https://ieeexplore.ieee.org/document/9621026
- **Abstract**: It is generally known that the log sum-product-algorithm (log-SPA) for non-binary low-density parity-check (NB-LDPC) codes requires a high decoding complexity. The complexity grows exponentially fast and becomes prohibitive as the check node degree and/or the field size increase. In this work, we propose a quantum-assisted decoding (QD) for NB-LDPC codes to resolve the complexity issue associated with the log-SPA. We utilize the quantum amplitude estimation algorithm (QAEA) to calculate the check node messages in the form of log-likelihood ratio vector (LLRV). This work realizes the QAEA with the following two blocks, 1) state preparation and 2) amplitude estimation (AE). In particular, the state preparation provides the AE with the input state. It will be shown that the proposed QD achieves a significant complexity reduction, which becomes more distinctive as the check node degree and/or the field size grows.

## Sparse vs. Dense Signatures for Grant-Free NOMA with Deep Learning Based Activity Detection

- **Status**: ❌
- **Reason**: LDPC를 NOMA 시그니처 마스크로 사용 — 채널 ECC 디코더 아님, 떼어낼 ECC 기법 없음
- **ID**: ieee:9613274
- **Type**: conference
- **Published**: 20-22 Oct.
- **Authors**: Chunxiang Li, Xiaofu Wu, Renxiang Zhang +2
- **PDF**: https://ieeexplore.ieee.org/document/9613274
- **Abstract**: Joint signature design and activity detection with deep learning has been extensively investigated for grant-free Non-Orthogonal Multiple Access (NOMA) in massive machine-type communications. In this paper, we propose to use sparse-pattern masked signatures for the purpose of joint signature design and activity detection. With a sparse mask matrix derived from a regular Low-Density Parity-Check (LDPC) code, we show that the use of regular sparse learnable signatures performs comparable to that of dense learnable signatures. Furthermore, there is no any observable performance advantage for the use of complex signatures compared to that of simple real signatures.

## On the Performance of SC-Flip and SC-Perturbation Decoders for Parallel Decoding of Polar Codes

- **Status**: ❌
- **Reason**: polar SC-Flip/SC-Perturbation 디코더 비교 — SC 계열은 polar 전용, BP/LDPC로 이식 불가. 비-LDPC 제외.
- **ID**: ieee:9621083
- **Type**: conference
- **Published**: 20-22 Oct.
- **Authors**: Jisang Park, Hyosang Ju, Chanho Yoon +2
- **PDF**: https://ieeexplore.ieee.org/document/9621083
- **Abstract**: In ultra-high frequency band communication for 5G or beyond 5G, high-speed transmission of the Tbps-level is targeted [1]. To reach that level, parallelization of decoding algorithms and architecture is crucial. There have been studies that have implemented the high-speed polar decoder, but it was possible to implement only under compromise in the error-rate performance, because of the use of successive cancellation (SC) decoding [2] instead of SC-list (SCL) [3] decoding. Therefore, it is essential to study decoder with improved performance whose performance can be comparable to the SCL decoder while using the SC decoder. The SC-Flip (SCF) [4]–[6] and SC-Perturbation (SCP) decoding [7], [8] as post-processing decoding techniques, improve the performance through re-decoding when the initial SC decoding fails. As the signal-to-noise ratio (SNR) increases, the average complexity converges to the SC decoding level while attaining better error-rate performance than the SC decoder. However, the performance of this post-processing schemes has not been compared nor extensively investigated. Therefore, we analyze the performance of SCF and SCP decoders with respect to the maximum number of decoding iterations for various coding parameters. We confirm that the SCF is better when the maximum number of decoding iterations is small, and the SCP outperforms the SCF as the number of iteration increases.

## An Adaptive Distributed Source Coding Design for Distributed Learning

- **Status**: ❌
- **Reason**: 분산학습용 분산 소스코딩(Slepian-Wolf/Wyner-Ziv) LDPC — 채널 ECC 아닌 소스코딩
- **ID**: ieee:9613333
- **Type**: conference
- **Published**: 20-22 Oct.
- **Authors**: Naifu Zhang, Meixia Tao
- **PDF**: https://ieeexplore.ieee.org/document/9613333
- **Abstract**: A major bottleneck in distributed learning is the communication overhead of exchanging intermediate model update parameters between the worker nodes and the parameter server. Existing works reconstruct each model update from worker nodes and implicitly assume that the local model updates are independent over worker nodes. In distributed learning, however, the model update is an indirect multi-terminal source coding problem, also called as the CEO problem. The existing works do not leverage the redundancy in the information transmitted by different worker nodes. This paper studies the practical distributed source coding (DSC) scheme for distributed learning. Our goal is to reduce the communication cost by leveraging the correlation in the local gradients. We first propose a DSC framework, named successive Wyner-Ziv coding, for distributed learning based on quantization and Slepian-Wolf (SW) coding. The practical SW coding is implemented by low density parity check (LDPC) code when gradients statistics are known. Finally, we propose an adaptive SW coding scheme that estimates the gradient statistics based on the observed quantized gradients at the parameter server and then dynamically adjusts the LDPC codes in each iteration.

## Hardware Implementation of 5G NR Deinterleaver and De-rate Matcher

- **Status**: ❌
- **Reason**: 5G NR 디인터리버·디레이트매처 HW — LDPC 디코더 자체가 아닌 주변회로, 이식할 디코더/코드설계 없음
- **ID**: ieee:9606247
- **Type**: conference
- **Published**: 20-22 Oct.
- **Authors**: Nemanja Filipovic, Dragomir El Mezeni, Andreja Radošević
- **PDF**: https://ieeexplore.ieee.org/document/9606247
- **Abstract**: 5G new radio (NR) represents the newest standard for mobile communications. It introduced LDPC channel coding which enables increased spectral efficiency in comparison to turbo codes used in LTE. It also specifies throughputs in the order of tens of Gb/s at lower latencies, putting a challenging constraint on all components in the data chain. In this paper, a parallel high throughput architecture of a joint deinterleaver and derate matcher for 5G NR is proposed. Efficient and scalable nature of the architecture allows easy tuning of throughput versus utilization over a large range of values. Proposed scheme for LLR value storage enables efficient memory utilization with full read and write throughput. The proposed architecture was implemented on a Zynq Ultrascale+ RFSoC FPGA from Xilinx in order to verify the functionality. Implementation achieves clock frequency close to the highest possible on the given architecture. To the best of our knowledge, this is currently the highest throughput implementation available.

## Implementation of Low-Density Parity Check on Field Programmable Gate Array DE1-SoC

- **Status**: ❌
- **Reason**: DE1-SoC FPGA에 표준 1/2 LDPC 단순 구현(4비트 메시지, BSC) — 교과서 수준 구현, 신규 HW 아키텍처 기여 없음.
- **ID**: ieee:9649567
- **Type**: conference
- **Published**: 20-21 Oct.
- **Authors**: Muhammad Dyanis Fajrinada, Ari Wijayanti, Mohamad Ridwan
- **PDF**: https://ieeexplore.ieee.org/document/9649567
- **Abstract**: Recently, telecommunications technology is growing rapidly, one of the devices that can support this development is a FPGA (Field Programmable Gate Array) which is an IC (Integrated Circuit) component and can be developed using programming. In this study, the authors use the DEl-SoC as an information bit transceiver board with LDPC (Low-Density Parity Check) coding technique because it can minimize errors approaching the Shannon limit with low BER (Bit Error Ratio). The information data that will be entered into the system is a binary bit which will be processed using a Linear Block Code encoder method, then the data is sent from the first FPGA DEl-SoC board as a transmitter to the second FPGA DEl-SoC board as a receiver. After that, the information data received at the second FPGA DEl-SoC as a receiver will be processed using a decoder so that it can be converted into binary bits of information data that are sent from the transmitter. This study successfully implemented the LDPC code on the DEl-SoC FPGA which was carried out through the Binary Symmetric Channel by utilizing UART (Universal Asynchronous Receiver-Transmitter) serial communication, where information is sent using 4 bits of binary as message input and 8 bits as the output codeword (1/2 code rate). Then in UART serial communication, the error percentage obtained is 0% because the data sent is the same as the data received.

## Analysis of Delayed Bit-Interleaved Coded Modulation for APSK

- **Status**: ❌
- **Reason**: APSK DBICM 용량 분석 — LDPC는 시뮬레이션 베이스라인일 뿐, 떼어낼 ECC 기법 없음. 무선/변조 특이적.
- **ID**: ieee:9590576
- **Type**: conference
- **Published**: 19-22 Oct.
- **Authors**: Gou Hosoya
- **PDF**: https://ieeexplore.ieee.org/document/9590576
- **Abstract**: In this work, we study delayed bit-interleaved coded modulation (DBICM) on amplitude and phase-shift keying (APSK) constellation. APSK is attractive for satellite communications, including DVB-S2. We find that the capacities of DBICM are identical to the coded modulation capacity. We also show that good performance can be achieved with a small delay value. We show these results by channel capacity analysis and the simulation results using low-density parity-check codes.

## Parallel CN-VN processing for NB-LDPC decoders

- **Status**: ❌
- **Reason**: NB-LDPC(비이진) 디코더의 CN-VN 병렬 EMS 아키텍처 — 비이진 LDPC는 제외 대상
- **ID**: ieee:9604993
- **Type**: conference
- **Published**: 19-21 Oct.
- **Authors**: Hassan Harb, Cédric Marchand, Laura Conde-Canencia +2
- **PDF**: https://ieeexplore.ieee.org/document/9604993
- **Abstract**: In this paper, a novel and innovative approach to implement the check node and variable node phases of the EMS algorithm is proposed. The novelty is not only from the hardware side, but also from the algorithmic point of view. An unusual manner of processing some steps of the check and variable nodes are shown. The performance and implementation results are promising to dig deeper in this work. Compared to its serial counterpart, the synthesis results of the proposed architecture show a factor gain greater than two in terms of area efficiency, with negligible performance loss.

## A Random Coding Bound on the ML Decoding Error Probability for NB LDPC Coded QAM Signals

- **Status**: ❌
- **Reason**: 비이진(NB) QC-LDPC ML 디코딩 오류확률 random coding bound — 비이진 LDPC + 순수 이론 bound, 판단절차 0번 즉시 제외
- **ID**: ieee:9611390
- **Type**: conference
- **Published**: 17-21 Oct.
- **Authors**: Irina E. Bocharova, Boris D. Kudryashov, Evgenii P. Ovsyannikov +1
- **PDF**: https://ieeexplore.ieee.org/document/9611390
- **Abstract**: A finite-length random coding bound on the maximum-likelihood decoding error probability for an ensemble of irregular nonbinary (NB) low-density parity-check (LDPC) codes with QAM signaling for specific code symbol-to-signal mappings is derived. Simulation results for the frame error rate (FER) performance of belief-propagation decoding for the optimized NB quasi-cyclic (QC)-LDPC codes used in various coded modulation schemes are presented. Comparison with the same performance of the optimized binary QC-LDPC block codes in the WiFi and 5G standards, as well as with the new bound, is performed.

## On the Universality of Spatially Coupled LDPC Codes Over Intersymbol Interference Channels

- **Status**: ❌
- **Reason**: ISI 채널에서 SC-LDPC 보편성 + BP/MAP threshold 엔트로피 분석 — 표준 SC-LDPC 사용한 순수 임계값 이론, 새 디코더/구성/HW 기여 없음
- **ID**: ieee:9611454
- **Type**: conference
- **Published**: 17-21 Oct.
- **Authors**: Mgeni Makambi Mashauri, Alexandre Graell i Amat, Michael Lentmaier
- **PDF**: https://ieeexplore.ieee.org/document/9611454
- **Abstract**: In this paper, we derive the exact input/output transfer functions of the optimal a-posteriori probability channel detector for a general ISI channel with erasures. Considering three channel impulse responses of different memory as an example, we compute the BP and MAP thresholds for regular spatially coupled LDPC codes with joint iterative detection and decoding. When we compare the results with the thresholds of ISI channels with Gaussian noise we observe an apparent inconsistency, i.e., a channel which performs better with erasures performs worse with AWGN. We show that this anomaly can be resolved by looking at the thresholds from an entropy perspective. We finally show that with spatial coupling we can achieve the symmetric information rates of different ISI channels using the same code.

## A General Framework for the Design of Compressive Sensing using Density Evolution

- **Status**: ❌
- **Reason**: compressive sensing용 sparse sensing matrix를 density evolution으로 설계 — 채널 ECC가 아닌 신호복원, 떼어낼 LDPC ECC 기법 없음
- **ID**: ieee:9611415
- **Type**: conference
- **Published**: 17-21 Oct.
- **Authors**: Hang Zhang, Afshin Abdi, Faramarz Fekri
- **PDF**: https://ieeexplore.ieee.org/document/9611415
- **Abstract**: This paper proposes a general framework to design a sparse sensing matrix ${\mathbf {A}} \in \mathbb{R}^{m\times n}$, in a linear measurement system ${\mathbf {y = Ax}}^{\sharp } + {\mathbf {w}}$, where ${\mathbf {y}} \in \mathbb{R}^{n}, {\mathbf {x}}^{\sharp } \in \mathbb{R}^{n}$, and w denote the measurements, the signal with certain structures, and the measurement noise, respectively. By viewing the signal reconstruction from the measurements as a message passing algorithm over a graphical model, we leverage tools from coding theory in the design of low density parity check codes, namely the density evolution, and provide a framework for the design of matrix A. Particularly, compared to the previous methods, our proposed framework enjoys the following desirable properties: (i) Universality: the design supports both regular sensing and preferential sensing, and incorporates them in a single frame-work; (ii) Flexibility: the framework can easily adapt the design of A to a signal $x^{\sharp }$ with different underlying structures. As an illustration, we consider the $\ell_{1}$ regularizer, which correspond to Lasso, for both the regular sensing and preferential sensing scheme. Noteworthy, our framework can reproduce the classical result of Lasso, i.e., $m \geq c_{0}k\log (n/k)$ (the regular sensing) with regular design after proper distribution approximation, where $c_{0}\gt 0$ is some fixed constant. We also provide numerical experiments to confirm the analytical results and demonstrate the superiority of our framework whenever a preferential treatment of a sub-block of vector $x^{\sharp }$ is required.

## Design of Short Blocklength Wiretap Channel Codes: Deep Learning and Cryptography Working Hand in Hand

- **Status**: ❌
- **Reason**: Gaussian wiretap 채널 short blocklength 보안 코드(autoencoder+hash) — LDPC 아닌 보안/오토인코더, 이식 가능 LDPC 디코더 기법 없음
- **ID**: ieee:9611401
- **Type**: conference
- **Published**: 17-21 Oct.
- **Authors**: Vidhi Rana, Rémi A. Chou
- **PDF**: https://ieeexplore.ieee.org/document/9611401
- **Abstract**: We design short blocklength codes for the Gaussian wiretap channel under information-theoretic security guarantees. Our approach consists in decoupling the reliability and secrecy constraints in our code design. Specifically, we handle the reliability constraint via an autoencoder, and handle the secrecy constraint via hash functions. For blocklengths smaller than 16, we evaluate through simulations the probability of error at the legitimate receiver and the leakage at the eavesdropper of our code construction. This leakage is defined as the mutual information between the confidential message and the eavesdropper’s channel observations, and is empirically measured via a recent mutual information neural estimator. Simulation results provide examples of codes with positive rates that achieve a leakage inferior to one percent of the message length.

## A new coded communication modulation scheme in very low frequency communication

- **Status**: ❌
- **Reason**: VLF 통신에 표준 LDPC+OFDM-MSK 적용 — LDPC는 부수 적용, 새 디코더/구성/HW 기여 없음, 무선 응용 특이적
- **ID**: ieee:9725027
- **Type**: conference
- **Published**: 15-17 Oct.
- **Authors**: Peipei Cao, Kaijie Zhou
- **PDF**: https://ieeexplore.ieee.org/document/9725027
- **Abstract**: Very low frequency (VLF) radio waves have very effective long-distance propagation characteristics. Therefore, they have a wide application prospect in underwater and underground communication. To effectively suppress the interference of channel noise and improve the performance of the VLF communication system, a low-density parity check (LDPC) coded orthogonal frequency division multiplexing-minimum frequency shift keying (OFDM-MSK) communication scheme is designed according to the characteristics of the VLF channel. Considering that the harmonic interference in the VLF channel can be regarded as frequency selective fading, the OFDM technology is applied to the VLF channel. In addition, the performance of VLF communication system is mainly affected by strong impulse atmospheric noise, which can be successfully simulated by symmetrical alpha stable (SαS) distribution. To reduce the impact of SαS noise on the OFDM system and data loss in frequency selective fading channel, LDPC channel coding technology is proposed. Finally, the robustness of the LDPC coded OFDM-MSK scheme is tested and evaluated from the perspective of the bit error rate (BER). The results show that the LDPC coded OFDM-MSK communication scheme has better performance than the independent OFDM-MSK communication scheme.

## A Low-Complexity EMS Algorithm with Dynamic Message Truncation for Non-Binary LDPC Codes

- **Status**: ❌
- **Reason**: Non-binary LDPC(GF(q=16)) EMS 알고리즘 — 비이진 LDPC 즉시 제외(절차 0)
- **ID**: ieee:9611936
- **Type**: conference
- **Published**: 14-15 Oct.
- **Authors**: Fulong Wang, Ming Zhan, Qian Zhang +4
- **PDF**: https://ieeexplore.ieee.org/document/9611936
- **Abstract**: The extended min-sum (EMS) algorithm is adopted for non-binary low density parity check (NB-LDPC) codes. The high complexity of EMS algorithm is a hot topic in recent years. Aiming at the problem, a low-complexity EMS algorithm based on NB-LDPC codes is proposed. Dynamic bubble-check (DBC) algorithm in elementary check node (ECN) steps is adopted to reduce the complexity of check node. Furthermore, the proposed algorithm dynamically truncates the length of the message vector by the number of decoding iterations. Taking the length of message vector truncated again as half of the original one as an example, the simulation results and complexity are analyzed. Analysis shows that, compared to the EMS algorithm, computational complexity of comparisons and real additions of check node of the proposed algorithm have reduced by about 70% and 25% respectively. Meantime, the decoding performance of the proposed algorithm approach that of EMS algorithm and the loss is only near 0.08 dB when the bit error rate (BER) is 10−3 and the Galois field $GF(q)(q=16)$.

## Design of Interleaver under Unbalanced Channels in LDPC-BICM MIMO System

- **Status**: ❌
- **Reason**: MIMO-BICM 환경 인터리버 설계로 무선 응용 특이적; QC-LDPC는 베이스라인일 뿐 NAND에 떼어낼 디코더·구성 기법 없음
- **ID**: ieee:9657918
- **Type**: conference
- **Published**: 13-16 Oct.
- **Authors**: Rui Zhao, Jingwen Zhang, Xinyi Wang +1
- **PDF**: https://ieeexplore.ieee.org/document/9657918
- **Abstract**: The unbalanced channel gain caused by multiple antennas in the multiple-input multiple-output (MIMO) wireless system will cause multi-stream data to pass through channels with an unbalanced signal-to-noise ratio (SNR). In this paper, we proposed a design methodology for the interleaver in the bit-interleaved coded modulation (BICM) systems deploying quasi-cyclic low-density parity-check (QC-LDPC) codes under unbalanced channels. The interleaver for irregular LDPC codes considering three unequal error protection characteristics including channels, modulation and irregular LDPC codes. The simulation results prove that our proposed algorithm can work well in most cases. Protograph extrinsic information transfer (PEXIT) chart analyses considering unbalance channels are used to explain the reason for this improvement.

## New McEliece Cryptosystem Based on Polar-LDPC Concatenated Codes as a Post-quantum Cryptography

- **Status**: ❌
- **Reason**: Polar-LDPC concatenated 기반 McEliece 암호시스템(보안), 채널 ECC 아님; 비-LDPC 부호 결합·보안 도메인으로 원칙 제외
- **ID**: ieee:9657958
- **Type**: conference
- **Published**: 13-16 Oct.
- **Authors**: Ruyi Wang, Yong Wang, Hao Xie
- **PDF**: https://ieeexplore.ieee.org/document/9657958
- **Abstract**: With the increase of computing power of quantum computers, classical cryptography schemes such as RSA and ECC are no longer secure in the era of quantum computers. The Cryptosystem based on coding has the advantage of resisting quantum computing and has a good application prospect in the future. McEliece Public Key Cryptography is a cryptosystem based on coding theory, whose security can be reduced to the decoding problem of general linear codes and can resist quantum attacks. Therefore, this paper proposes a cryptosystem based on the Polar-LDPC Concatenated Codes, which is an improvement on the original McEliece cipher scheme. The main idea is to take the generation matrix of Polar code and LDPC code as the private key, and the product of their hidden generation matrix as the public key. The plain text is encoded by Polar code and LDPC code in turn to obtain the encrypted ciphertext. The decryption process is the corresponding decoding process. Then, the experimental data presented in this paper prove that the proposed scheme can reduce key size and improve security compared with the original McEliece cryptosystem under the condition of selecting appropriate parameters. Moreover, compared with the improvement schemes based on McEliece proposed in recent years, the proposed scheme also has great security advantages.

## The LDPC-Coded High-Dimensional SCMA Codebook Design

- **Status**: ❌
- **Reason**: SCMA 코드북 설계 + SIC 검출기, LDPC는 표준 채널코딩 부수 사용 — 무선 응용 특이적, 떼어낼 LDPC 기법 없음
- **ID**: ieee:9657878
- **Type**: conference
- **Published**: 13-16 Oct.
- **Authors**: Tuofeng Lei, Shuyan Ni, Naipinz Cheng +3
- **PDF**: https://ieeexplore.ieee.org/document/9657878
- **Abstract**: Sparse code multiple access (SCMA) and low density parity check (LDPC) are two promising technologies in 5G New Radio communications. In this paper, the LDPC codes are adopted as the channel coding to ensure the transmitted data is revived with minimal errors. Then, we propose a new method for constructing the high-dimensional SCMA codebook. However, the complexity of the message passing algorithms (MPA) based detectors are extremely high, which conflicts with the low latency demand of the 5G wireless communication systems. To save the computational costs of the SCMA detector, we fully exploited the information of the SCMA codebook, and introduce the successive interference cancellation (SIC) algorithm as the detector. In the LDPC-coded scheme, the SIC decoding algorithm lose the information of minimum Euclidean distance of other codewords, which cause the better BER performance disobeys the principles of increased code length and the decreased code rate while the coding scheme can also improve the BER performance. The simulation results show the LDPC-coded SCMA scheme can achieve preferable bit error rate (BER) performance, and the SIC detector can significantly reduce the complexity at the receiver.

## Index Modulation of OAM-UCA with LDPC Transmission

- **Status**: ❌
- **Reason**: OAM-UCA 인덱스 변조에 표준 LDPC 부수 적용 — 무선 응용 특이적, 새 LDPC 기법 없음
- **ID**: ieee:9657882
- **Type**: conference
- **Published**: 13-16 Oct.
- **Authors**: Fusheng Zhu, Jin Jiang, Yongjun Li +3
- **PDF**: https://ieeexplore.ieee.org/document/9657882
- **Abstract**: The Orbital Angular Momentum (OAM) is utilized as a new dimension to improve wireless communication spectral efficiency. combination of OAM and Multi-Input Multi-Output (MIMO) with Uniform Circular Array (UCA) scheme is expected to be easily applied in the existing communication network. Similarly, the Index Modulation (IM) utilizes the indices of the building blocks of the corresponding communication systems in the Low Density Parity Code (LDPC) to improve error performance and transmit addition information bits. In this paper, we propose the index modulation of OAM-UCA with LDPC transmission technology. Combining LDPC with OAM-UCA index modulation, the simulation results show that when the index number of OAM mode is 5, LDPC coding can bring the gain of 4 dB when the Bit Error Rate (BER) is 10−5• In addition, the combination of OAM-UCA and index modulation with LDPC scheme is expected to be applied in 6G.

## An Efficient Two-Dimension OTFS-NOMA Scheme Based on Heterogenous Mobility Users Grouping

- **Status**: ❌
- **Reason**: OTFS-NOMA/SCMA 다중접속·코드북 설계로 무선 통신 특이적; LDPC 무관, 떼어낼 ECC 기법 없음
- **ID**: ieee:9657979
- **Type**: conference
- **Published**: 13-16 Oct.
- **Authors**: Ziqi Kang, Hang Zhao, Hua Wang
- **PDF**: https://ieeexplore.ieee.org/document/9657979
- **Abstract**: Orthogonal time frequency space (OTFS) modulation recently has been widely studied for its superior performance in high-mobility scenarios. In order to explore the efficiency potential and performance, the concept of non-orthogonal multiple access (NOMA) is extended to OTFS as a key technique to enhance its spectral efficiency. As for diverse schemes of NOMA formulated in different domains, we propose a two-dimension OTFS-NOMA (2D-OTFS-NOMA) transmission scheme based on heterogenous mobility users grouping by exploiting both power-domain and code-domain. Specifically, power-domain NOMA (PD-NOMA) is implemented between the users under high-mobility and low-mobility, while sparse code multiple access (SCMA) technique is applied to the users under the subgroup of low-mobility. Moreover, a high dimensional codebook design is also proposed based on Signature matrix construction methodology, which has a great extensibility for larger number of users' scenarios. We also validate the corresponding detection approach and present the analyses of its performance. Simulation results demonstrate that the proposed two-dimension OTFS-NOMA transmission scheme outperforms the other existing PD-NOMA scheme for OTFS systems in terms of spectral efficiency performance.

## Adaptive Modulation and Coding in Satellite-Integrated 5G Communication System

- **Status**: ❌
- **Reason**: 위성-5G 적응형 변조·코딩(AMC) 시스템 설계, LDPC 부수 언급; 떼어낼 디코더·구성 기법 없음
- **ID**: ieee:9658103
- **Type**: conference
- **Published**: 13-16 Oct.
- **Authors**: Dechao Chen, Jingwen Zhang, Rui Zhao
- **PDF**: https://ieeexplore.ieee.org/document/9658103
- **Abstract**: In order to achieve wide coverage, high-speed communication and the global interconnection of everything, satellites communications and 5G mobile communication will be complementary and integrated in the future. Aiming at different channel conditions, this paper designs 21 modulation and coding schemes in satellite-integrated 5G communication system through simulation. In addition, in order to adapt to changes in the channel environment, an adaptive modulation and coding (AMC) technology suitable for the integration systems is proposed. The simulation results show that, in terms of block error rate (BLER) and throughput performance, AMC technology is better than constant modulation and coding scheme (MCS). In addition, because the random jitter of the channel estimator will cause the ping-pong effect in MCS switching, the simulation results show hysteresis technology effectively slow down the ping-pong effect.

## A Turbo Coded LoRa-Index Modulation Scheme for IoT Communication

- **Status**: ❌
- **Reason**: Turbo 부호 + LoRa 인덱스 변조 IoT — 비-LDPC, 부호 비의존 이식 기법 없음
- **ID**: ieee:9657863
- **Type**: conference
- **Published**: 13-16 Oct.
- **Authors**: Shixiang An, Zhiping Lu, Hua Wang +1
- **PDF**: https://ieeexplore.ieee.org/document/9657863
- **Abstract**: Long-Range (LoRa) is one of the emerging technologies in low-power wide-area networks (LPWANs). LoRa physical layer (PHY) employs chirp spread spectrum (CSS) on top of a variant of frequency shift keying (FSK), and noncoherent detection is employed at the receiver for obtaining the transmitted data symbols. In this paper, we focus on data transmission performance in Internet-of-Things (IoT) networks. This paper first analyzes the BER performance of LoRa modulation. To improve the spectral efficiency and energy efficiency, we propose a method for LoRa physical layer improvement based on index modulation and derive the theoretical error rate of the index bit and information bits. Furthermore, Turbo code is employed to improve the BER performance of the scheme. Simulation results are presented and the transmission performance is analyzed.

## Research on LDPC channel coding technology in satellite communication system

- **Status**: ❌
- **Reason**: 위성통신 LDPC 연구 핫스팟 개관(서베이) 수준, 구체적 신규 디코더·구성·HW 기여나 정량 비교 없음
- **ID**: ieee:9627463
- **Type**: conference
- **Published**: 13-15 Oct.
- **Authors**: Shikang Nie, Guangting Li, Xin Liu +3
- **PDF**: https://ieeexplore.ieee.org/document/9627463
- **Abstract**: This paper discusses in detail the development of several research hotspots of Low-Density Parity Check (LDPC) codes and their joint optimization design with other communication technologies, and points out that LDPC codes have broad development and application space in the future communication field.

## Design of an OFDM-based Differential Cyclic-Shifted DCSK System for Underwater Acoustic Communications

- **Status**: ❌
- **Reason**: 수중음향 OFDM-DCSK 변조/검출 시스템, LDPC 무관
- **ID**: ieee:9609854
- **Type**: conference
- **Published**: 11-13 Oct.
- **Authors**: Xiangming Cai, Luyao Hu, Weikai Xu +1
- **PDF**: https://ieeexplore.ieee.org/document/9609854
- **Abstract**: Given the high transmission loss, severe Doppler spread and large multipath delay in the underwater acoustic (UWA) channel, the channel estimation and tracking in the conventional orthogonal frequency division multiplexing (OFDM) based UWA systems are severely unaffordable. In this paper, we propose a low-complexity and cost-friendly OFDM-based differential cyclic-shifted differential chaos shift keying (OFDM-DCS-DCSK) system which offers a high data rate, superior robustness and enhanced system security for UWA communications without the need for channel state information (CSI). In the system, the information bits are carried by different step lengths of the cyclic shifts. At the receiver, a low-complexity detection method is used to search the position of maximum from the cyclic correlation values and therefore estimate the information bits. Finally, simulation results demonstrate the proposed OFDM-DCS-DCSK system outperforms its competitors both in bit error rate (BER) performance and in system security.
