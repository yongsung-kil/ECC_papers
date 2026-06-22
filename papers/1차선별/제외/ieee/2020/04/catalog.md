# IEEE Xplore — 2020-04


## Interleaved Polar (I-Polar) Codes

- **Status**: ❌
- **Reason**: Interleaved polar code 구성·WEF 분석으로 polar 코드 전용, LDPC 이식 기법 없음
- **ID**: ieee:8968424
- **Type**: journal
- **Published**: April 2020
- **Authors**: Mao-Ching Chiu
- **PDF**: https://ieeexplore.ieee.org/document/8968424
- **Abstract**: By inserting interleavers between intermediate stages of the polar encoder, a new class of polar codes, termed interleaved polar (i-polar) codes, is proposed. By the uniform interleaver assumption, we derive the weight enumerating function (WEF) and the input-output weight enumerating function (IOWEF) averaged over the ensemble of i-polar codes. The average WEF can be used to calculate the upper bound on the average block error rate (BLER) of a code selected at random from the ensemble of i-polar codes. Also, we propose a concatenated coding scheme that employs P high rate codes as the outer code and Q i-polar codes as the inner code with an interleaver in between. The average WEF of the concatenated code is derived based on the uniform interleaver assumption. Simulation results show that BLER upper bounds can well predict BLER performance levels of the concatenated codes. The results show that the performance of the proposed concatenated code with P=Q=2 is better than that of the CRC-aided i-polar code with P=Q=1 of the same length and code rate at high signal-to-noise ratios (SNRs). Moreover, the proposed concatenated code allows multiple decoders to operate in parallel, which can reduce the decoding latency and hence is suitable for ultra-reliable low-latency communications (URLLC).

## A Grant-Free Random Access Scheme for M2M Communication in Massive MIMO Systems

- **Status**: ❌
- **Reason**: massive MIMO grant-free random access의 EICA 검출 알고리즘 — LDPC ECC 기법 없음, 무선 응용 특이적
- **ID**: ieee:8993804
- **Type**: journal
- **Published**: April 2020
- **Authors**: Huimei Han, Ying Li, Wenchao Zhai +1
- **PDF**: https://ieeexplore.ieee.org/document/8993804
- **Abstract**: A novel grant-free random access scheme is proposed to support massive connectivity with low access delay and overhead for machine-to-machine communication in massive multiple-input-multiple-output systems. This scheme allows all active user equipments (UEs) to transmit their pilots and uplink messages via the same time-frequency resource and performs the joint active UEs detection and uplink message decoding without channel estimation in one shot by utilizing the proposed ensemble independent component analysis (EICA) decoding algorithm. We call the proposed scheme the EICA-based pilot random access (EICA-PA). We analyze the successful access probability, probability of missed detection, and uplink throughput of the EICA-PA scheme. Numerical results show that the EICA-PA scheme significantly improves the successful access probability and uplink throughput, decreases missed detection probability and provides low-frame error rate at the same time.

## Efficient Sparse Code Multiple Access Decoder Based on Deterministic Message Passing Algorithm

- **Status**: ❌
- **Reason**: SCMA(비직교 다중접속) 디코더로 LDPC ECC가 아닌 NOMA 검출, 이식 ECC 기법 없음
- **ID**: ieee:8967122
- **Type**: journal
- **Published**: April 2020
- **Authors**: Chuan Zhang, Chao Yang, Xu Pang +5
- **PDF**: https://ieeexplore.ieee.org/document/8967122
- **Abstract**: Being an effective non-orthogonal multiple access (NOMA) technique, sparse code multiple access (SCMA) is promising for future wireless communication. Compared with orthogonal techniques, SCMA enjoys higher overloading tolerance and lower complexity because of its sparsity. In this paper, based on deterministic message passing algorithm (DMPA), algorithmic simplifications such as domain changing and probability approximation are applied for SCMA decoding. Early termination, adaptive decoding, and initial noise reduction are also employed for faster convergence and better performance. Numerical results show that the proposed optimizations benefit both decoding complexity and speed. Furthermore, efficient hardware architectures based on folding and retiming are proposed. VLSI implementation is also given in this paper. Comparison with the state-of-the-art have shown the proposed decoder's advantages in both latency and throughput (multi-Gbps).

## Blind Estimation of Code Parameters for Product Codes Over Noisy Channel Conditions

- **Status**: ❌
- **Reason**: Product code(RS/BCH) 파라미터 블라인드 추정으로 LDPC ECC 기법 없음
- **ID**: ieee:8804240
- **Type**: journal
- **Published**: April 2020
- **Authors**: R. Swaminathan, A.S. Madhukumar, Guohua Wang
- **PDF**: https://ieeexplore.ieee.org/document/8804240
- **Abstract**: Product codes are multidimensional codes constructed using multiple component codes. In this paper, novel algorithms are proposed for the blind estimation of two-dimensional product code parameters over the noisy channel conditions considering Reed-Solomon and Bose-Chaudhuri-Hocquenghem as component codes. The performance of the algorithms in terms of probability of the correct estimation is investigated for different code parameters. It is observed that the accuracy improves with the decrease in modulation order and code dimension values.

## Low-Complexity Detection for Faster-than-Nyquist Signaling Based on Probabilistic Data Association

- **Status**: ❌
- **Reason**: FTN 신호 BPSK 시퀀스 검출(PDA)로 LDPC ECC 기법 아님
- **ID**: ieee:8941122
- **Type**: journal
- **Published**: April 2020
- **Authors**: Michel Kulhandjian, Ebrahim Bedeer, Hovannes Kulhandjian +2
- **PDF**: https://ieeexplore.ieee.org/document/8941122
- **Abstract**: In this letter, we investigate the sequence estimation problem of faster-than-Nyquist (FTN) signaling as a promising approach for increasing spectral efficiency (SE) in future communication systems. In doing so, we exploit the concept of Gaussian separability and propose two probabilistic data association (PDA) algorithms with polynomial time complexity to detect binary phase-shift keying (BPSK) FTN signaling. Simulation results show that the proposed PDA algorithm outperforms the recently proposed SSSSE and SSSgbKSE algorithms for all SE values with a modest increase in complexity. The PDA algorithm approaches the performance of the semidefinite relaxation (SDRSE) algorithm for SE values of 0.96 bits/sec/Hz, and it is within the 0.5 dB signal-to-noise ratio (SNR) penalty at SE values of 1.10 bits/sec/Hz for the fixed values of β = 0.3.

## Comprehensive Study on CC-LDPC, BC-LDPC and Polar Code

- **Status**: ❌
- **Reason**: Survey comparing CC-LDPC/BC-LDPC/polar for 6G; comparative study only, no new binary LDPC decoder/HW/construction to extract
- **ID**: ieee:9124897
- **Type**: conference
- **Published**: 6-9 April 
- **Authors**: Kun Zhu, Zhanji Wu
- **PDF**: https://ieeexplore.ieee.org/document/9124897
- **Abstract**: Channel coding scheme is very crucial for the next sixth generation (6G) mobile communication. In this paper, we investigate the encoding and decoding methods of the state-of-the-art channel codes, which include the convolutional code LDPC (CC-LDPC), block code LDPC (BC-LDPC) and polar code to access the benefits from CC-LDPC. And then, we present comprehensive evaluation to compare their error performance, decoding complexity and latency. Our research shows that CC-LDPC has the advantages in terms of high reliability, low complexity and low latency. Finally, we propose some open research problems and solving ideas for CC-LDPC application in 6G communication.

## Coding Techniques for 5G Networks: A Review

- **Status**: ❌
- **Reason**: 5G 코딩 기법 리뷰(LDPC/Polar) — 서베이, 신규 디코더·구성·HW 기여 없음
- **ID**: ieee:9137797
- **Type**: conference
- **Published**: 3-4 April 
- **Authors**: Mrinmayi V Patil, Sanjay Pawar, Zia Saquib
- **PDF**: https://ieeexplore.ieee.org/document/9137797
- **Abstract**: In todays world, the demand for Mobile Internet is increasing and the Internet of Things poses a challenging requirement for 5G wireless communications. Turbo Codes and Tail Bitting Convolution Codes (TBCC) have proven to be efficient for LTE communication. But these codes have failed to satisfy the conditions defined for 5G Communications. In 5G, we require advanced error correction techniques for channel coding. To fulfill 5G communications requirements, we use LDPC and Polar codes for error correction. In 5G NR (New Radio) LDPC codes used for the data channel and control channel Polar Codes are used. We get high Coding gain for this code. It has several features such as high throughput, low power dissipation, and low latency. We describe encoding and decoding methods of LDPC and Polar Codes. They use two types of Base matrices of 5G NR for this code. Polar codes depend on channel polarization and are the first code that has achieved Shannon channel capacity. Polar codes have wide applications in Information theory. Quasi Cyclic LDPC code, Irregular Repeat-Accumulate (IRA) code, Spatially Coupled LDPC (SP-LDPC), NBLDPC-Polar Codes described. For 5G Standard this code plays an important role in Channel Coding.

## Codeword Generation for a Combined Cryptography and LDPC Coding System

- **Status**: ❌
- **Reason**: 암호+LDPC 결합 시스템의 cyphertext 생성(보안 응용), 떼어낼 채널 ECC 디코더·구성 기법 없음
- **ID**: ieee:9198715
- **Type**: conference
- **Published**: 22-24 Apri
- **Authors**: Bradley Comar
- **PDF**: https://ieeexplore.ieee.org/document/9198715
- **Abstract**: This paper describes a method of generating the cyphertext for a combined cryptographic and LDPC encoding system. This combined system is used for the purpose of enhancing privacy. However, to create the cyphertext, 2 matrix inversions must occur and one of these matrices may sometimes be singular. In addition to this inversion issue, this combined system may use many more PRNG bits per message bit than the standard XORing system. Both issues are addressed here.

## On Efficient and Low-Complexity Decoding of Binary LDPC-Coded CSK Signals for GNSS Links with Increased Data Rates

- **Status**: ❌
- **Reason**: GNSS CSK 신호 복조/iterative demapping 복잡도 저감; LDPC는 베이스라인, CSK demapping에 특화돼 NAND LDPC로 이식할 새 기법 없음
- **ID**: ieee:9110196
- **Type**: conference
- **Published**: 20-23 Apri
- **Authors**: Rémi Chauvat, Axel Garcia-Pena, Matteo Paonni
- **PDF**: https://ieeexplore.ieee.org/document/9110196
- **Abstract**: GNSS with high data rate links are of interest to accommodate new needs and applications (e.g. precise positioning, authentication, reduction of TTFFD). In this context, a binary LDPC-coded CSK signal is an attractive candidate to increase data rates with a high data recovery robustness. However, such a proposal requires an increase of receiver's computational complexity with respect to receivers for current coded DSSS/BPSK GNSS links. The computational complexity required for data recovery is analysed in this article and insights on crucial technical choices are given for the reception of binary LDPC-coded CSK signals. CSK demodulation is shown to dominate the overall computational cost and the use of digital chip-matched filtering prior to demodulation is proposed to reduce this cost. In addition, iterative demapping, which is crucial to optimize the power efficiency of binary LDPC-coded CSK links is also shown to have high computational complexity. Therefore, low-complexity iterative demapping strategies are studied and simple yet efficient solutions are proposed.

## LDPC Decoding Based On Statistical Mechanics Of Spin-Glasses: A Study

- **Status**: ❌
- **Reason**: Spin-glass/statistical-mechanics review of LDPC decoding; no concrete new decoder/HW/construction
- **ID**: ieee:9092331
- **Type**: conference
- **Published**: 16-19 Apri
- **Authors**: Z. JADDI, A. AIT MADI, M. BENBRAHIM
- **PDF**: https://ieeexplore.ieee.org/document/9092331
- **Abstract**: In this paper, the LDPC (Low Density Parity Check Codes) decoding algorithm has been investigated using statistical mechanics properties. The main advantage of LDPC codes is their performance that works in near Shannon limit, and the ability to use iterative decoding algorithms. In 1989 N. Sourlas showed that error-correcting codes can be considered as Spin-Glass systems thus making it possible to model LDPC codes as an Ising model, opening the way for information theorists to solve coding problems with the power of statistical mechanics. According to N. Sourlas, the decoding problem can be solved by finding the ground state of the corresponding spin-system Hamiltonian. The main goal of this paper is to review as simple as possible the statistical properties of LDPC codes, and how it is used especially facing the decoding problem.

## Investigation of Harmonic Frequency Multiplication on Transmitted Data through Pulse Shaping for 6G Communication

- **Status**: ❌
- **Reason**: 6G 펄스셰이핑/주파수 체배 RF 연구, LDPC/디코더/ECC 기법 없음
- **ID**: ieee:9102565
- **Type**: conference
- **Published**: 14-16 Apri
- **Authors**: Özgün Ersoy, Asaf Behzat Şahin
- **PDF**: https://ieeexplore.ieee.org/document/9102565
- **Abstract**: Communication shifts to high carrier frequencies with increasing data rates and the need for quality transmission. In this context, studies are carried out at 28 GHz in 5G technology, and communication systems in the frequency band of 60–70 GHz are studied. In addition, communication systems in the frequency band of 140–180 GHz are planned for 6G technology. However, amplifier active balanced mixers cannot be found at high frequencies in existing technology, frequency multiplication via Schottky diode only viable solution for these ahead of the technology curve frequency bands. We investigated the effects of frequency upconversion through harmonic frequency multiplication on the transmitted digital data pulse shape and data rate. These studies were simulated in the MATLAB simulation environment and corroborated in our experimental 50–75 GHz carrier wireless communication system. We showed that through pulse shaping the transmitted data eye diagram SNR can be improved by 3 dB or data rate can be increased by 20% alternatively.
