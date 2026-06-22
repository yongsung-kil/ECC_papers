# IEEE Xplore — 2023-05


## Comparative Performance Evaluation of LDPC Coded OFDM-IM Under Jamming Attack

- **Status**: ❌
- **Reason**: OFDM-IM 재밍 하 LDPC 성능 비교 — 표준 LDPC를 베이스라인으로 적용만, 떼어낼 새 ECC 기법 없음
- **ID**: ieee:9999530
- **Type**: journal
- **Published**: May 2023
- **Authors**: Ahmet Kaplan, Mehmet Can, Ibrahim Altunbas +2
- **PDF**: https://ieeexplore.ieee.org/document/9999530
- **Abstract**: Orthogonal frequency division multiplexing (OFDM) with index modulation (IM), OFDM-IM, is considered as a potential enabling technology for 5G and beyond wireless networks due to its advantages compared to OFDM. This paper firstly examines and compares the error performance of uncoded OFDM-IM and OFDM under barrage jamming (BJ) and partial band jamming (PBJ) attacks. In addition, we propose a novel arbitrary jamming (AJ) model and extend our analysis to this attack. We demonstrate that uncoded OFDM-IM is more resistant against jamming attacks when compared to uncoded OFDM. In the OFDM-IM system, we derive an upper bound for the average bit error probability under AJ attack to verify our simulation results. The achievable rate of OFDM-IM under jamming attack is also investigated. We then apply low-density parity-check (LDPC) coding to further enhance the strength of the system under a heavy jamming attack. The optimum log-likelihood ratios for the OFDM-IM system in the case of jamming attack are calculated. We compare and analyze the bit error rate (BER) performances of LDPC coded OFDM and OFDM-IM for different jamming types, code rates, code block lengths, and code decoding algorithms through extensive computer simulations. At high code rates under jamming attack, we prove that the coded OFDM-IM has BER performance superiority. Moreover, we demonstrate that coded OFDM-IM is more resistant against imperfect channel state information than coded OFDM under BJ. We also compare the performances of LDPC coded OFDM-IM and the higher-order OFDM-IM (HO-OFDM-IM), an enhanced version of OFDM-IM.

## New Design of Blockwise Interleaved Ideal Low-Rank Parity-Check Codes for Fast Post-Quantum Cryptography

- **Status**: ❌
- **Reason**: 비이진 low-rank parity-check(LRPC) 코드 + 포스트양자 암호 KEM - 비이진/암호 응용, 이중 제외
- **ID**: ieee:10068546
- **Type**: journal
- **Published**: May 2023
- **Authors**: Chanki Kim, Young-Sik Kim, Jong-Seon No
- **PDF**: https://ieeexplore.ieee.org/document/10068546
- **Abstract**: In this letter, a new design of blockwise interleaved ideal low-rank parity-check (BII-LRPC) codes is proposed for a fast cryptographic application. We show that the proposed ideal LRPC codes can be used as a key encapsulation mechanism (KEM) for post-quantum cryptography (PQC). The simulation results show that the KEM constructed from the proposed BII-LRPC codes is faster by 30-70% than the ROLLO-I algorithm, an existing LRPC-based cryptosystem.

## Beyond Turbo: An Integrated ADMM Receiver for URLLC MIMO Systems

- **Status**: ❌
- **Reason**: URLLC MIMO 결합검출/디코딩 ADMM 수신기, 디텍션+디코딩 결합으로 NAND ECC 단독 디코더로 이식 어려움 (통신 특이적)
- **ID**: ieee:10049426
- **Type**: journal
- **Published**: May 2023
- **Authors**: Yi Sun, Hong Shen, Wei Xu +3
- **PDF**: https://ieeexplore.ieee.org/document/10049426
- **Abstract**: The emergence of ultra-reliable and low-latency communication (URLLC) poses challenges on the receiver design. Classical turbo receivers, which exhibit excellent performance under long data packet transmissions, can suffer from non-negligible error propagation in the context of URLLC due to the use of short error correction codes. To address this issue, we advocate a novel joint detection and decoding (JDD) receiver for URLLC multi-input multi-output (MIMO) systems with short low-density parity-check (LDPC) codes. Specifically, we first establish a maximum likelihood (ML) based JDD problem formulation by incorporating the bit-to-symbol mapping and the LDPC code constraints, which circumvents the error propagation issue in turbo receivers. In order to solve this difficult large-scale non-convex problem, we develop a low-complexity alternating direction method of multipliers (ADMM) algorithm to directly acquire the ultimate decoding results. Simulation results validate the performance advantage of the proposed JDD receiver over the turbo receivers in the URLLC scenario.

## Gaussian and Fading Multiple Access Using Linear Physical-Layer Network Coding

- **Status**: ❌
- **Reason**: q-ary(비이진) IRA 코드 + 물리계층 네트워크 코딩 MAC — 비이진이고 무선 응용 특이, 제외
- **ID**: ieee:9930671
- **Type**: journal
- **Published**: May 2023
- **Authors**: Qiuzhuo Chen, Fangtao Yu, Tao Yang +1
- **PDF**: https://ieeexplore.ieee.org/document/9930671
- **Abstract**: This paper concerns with efficient communication over Gaussian and fading multiple-access channels (MACs). Existing orthogonal multiple-access (OMA) and power-domain nonorthogonal-OMA (NOMA) cannot achieve all rate-tuples in the MAC capacity region. Meanwhile, code-domain NOMA schemes usually require big-loop receiver-iterations for multi-user decoding, which is subject to high implementation cost and latency. This paper studies a linear physical-layer network coding multiple access (LPNC-MA) scheme that is capable of achieving any rate-tuples in the MAC capacity region without receiver iterations. For deterministic Gaussian MACs with  $M$  users, we propose to utilize  $q$ -ary irregular repeat accumulate (IRA) codes over finite integer fields/rings and  $q$ -ary pulse amplitude modulation ( $q$ -PAM) as the underlying coded-modulation. The receiver sequentially computes  $M$  network coded (NC) messages of the  $M$  users. All users’ messages are then recovered by solving the computed  $M$  NC messages via the inverse of the NC coefficient matrix. A joint nested code construction and extrinsic information transfer (EXIT) chart based code optimization method is developed, yielding near-capacity performance (within 0.7 and 1.1 dB the capacity limits for two and three users respectively). For fading MAC, we study the symmetric rate of LPNC-MA, and propose a pragmatic method for identifying the mutual information (MI) maximizing network coding coefficient matrix. Numerical results demonstrate that the frame error rate (FER) of the optimized LPNC-MA is within a fraction of dB the outage probability of fading MAC capacity. LPNC-MA remarkably outperforms NOMA-SIC and IDMA while avoiding the big-loop receiver iteration.

## Index Modulation Multiple Access for Unsourced Random Access

- **Status**: ❌
- **Reason**: 비소스 랜덤액세스 IMMA, LDPC는 부수 요소이고 통신 응용 특이적 - 떼어낼 ECC 기법 없음
- **ID**: ieee:10042992
- **Type**: journal
- **Published**: May 2023
- **Authors**: Yiwei Su, Jianping Zheng
- **PDF**: https://ieeexplore.ieee.org/document/10042992
- **Abstract**: In this letter, a novel index modulation multiple access (IMMA) scheme is proposed in the quasi-static MIMO channel. In the proposed scheme, the transmit information bits are divided into two parts, IMMA bits and coded bits. The IMMA bits are employed to select the active compressed sensing codeword transmitted in the first phase, and determine the IMMA pattern. The encoding bits are LDPC encoded, modulated, and transmitted in the second phase through IMMA. In the multiuser detection, the IMMA patterns and active channels are first estimated by approximate message passing (MP) algorithm. Then, the encoding bits are decoded by MP algorithm based on the joint LDPC and IMMA factor graph. Finally, computer simulations are given to demonstrate the performance of the proposed scheme.

## RESS: A Reliable and Effcient Storage Scheme for Bitcoin Blockchain Based on Raptor Code

- **Status**: ❌
- **Reason**: 블록체인 스토리지에 Raptor/erasure 코드 적용 — fountain/rateless 코드로 이식할 바이너리 LDPC ECC 기법 없음
- **ID**: ieee:10124693
- **Type**: journal
- **Published**: May 2023
- **Authors**: Dongxian Shi, Xiaoqing Wang, Ming Xu +2
- **PDF**: https://ieeexplore.ieee.org/document/10124693
- **Abstract**: The Bitcoin system uses a fully replicated data storage mechanism in which each node keeps a full copy of the blockchain. As the number of nodes in the system increases and transactions get more complex, more and more storage space are needed to store block data. The scalability of storage has become a bottleneck, limiting the practical application of blockchain. This paper proposes a node storage scheme, called RESS, to integrate erasure coding technology into the blockchain to encode multiple blocks. Under the proposed block grouping method, nodes can reduce the times of coded block decoding. In addition, the coding scheme based on Raptor codes proposed in this paper has linear coding and decoding complexity. The rateless feature of Raptor code helps to achieve high decentralization and scalability of the Bitcoin network. RESS ensures data availability, efficiency and blockchain robustness based on achieving storage space scalability. Experimental results show that the proposed scheme reduces the storage requirements of nodes by nearly an order of magnitude.

## BP-Based Sparse Graph List Decoding of Polar Codes

- **Status**: ❌
- **Reason**: Polar 코드 BP 리스트 디코더(BP-SGL), LDPC-like BP를 차용했으나 polar 디코딩용이며 LDPC 코드 디코더 기여 아님
- **ID**: ieee:10068527
- **Type**: journal
- **Published**: May 2023
- **Authors**: Han Liu, Erry Gunawan, Hu Yaoyue +1
- **PDF**: https://ieeexplore.ieee.org/document/10068527
- **Abstract**: How to construct an effective polar decoding scheme has attracted researchers in the field of communication. The belief propagation list (BPL) decoder has performance improvement over the traditional BP decoder but comes with much higher complexity. To solve the issue of high complexity & latency, a low-density parity-check (LDPC) like BP decoder was proposed but it suffered from performance degradation over the original BP decoder. In this letter, a BP-based sparse graph list (BP-SGL) decoder is proposed by leveraging both list decoding scheme and LDPC-like BP decoding algorithm to achieve performance improvement while maintaining low complexity & latency. The key idea of the proposed list generation method is the similarity comparison of decoding graphs. Testing results verify that selecting graphs with large structural differences helps to construct a list with good overall performance. Simulation results show that the proposed scheme is superior to LDPC-like BP, and even outperforms the original BPL and some state-of-the-art (SOTA) BP-based decoding algorithms with significant reduction in complexity & latency.

## On OAMP: Impact of the Orthogonal Principle

- **Status**: ❌
- **Reason**: OAMP 직교원리 이론, AMP류 추정기 일반론으로 순수 이론, LDPC 디코더/HW 이식 기법 없음
- **ID**: ieee:10082977
- **Type**: journal
- **Published**: May 2023
- **Authors**: Lei Liu, Yiyao Cheng, Shansuo Liang +2
- **PDF**: https://ieeexplore.ieee.org/document/10082977
- **Abstract**: Approximate Message Passing (AMP) is an efficient iterative parameter-estimation technique for certain high-dimensional linear systems with non-Gaussian distributions, such as sparse systems. In AMP, a so-called Onsager term is added to keep estimation errors approximately Gaussian. Orthogonal AMP (OAMP) does not require this Onsager term, relying instead on an orthogonalization procedure to keep the current errors uncorrelated with (i.e., orthogonal to) past errors. In this paper, we show the generality and significance of the orthogonality in ensuring that errors are “asymptotically independently and identically distributed Gaussian” (AIIDG). This AIIDG property, which is essential for the attractive performance of OAMP, holds for separable functions. We present a simple and versatile procedure to establish the orthogonality through Gram-Schmidt (GS) orthogonalization, which is applicable to any prototype. We show that different AMP-type algorithms, such as expectation propagation (EP), turbo, AMP and OAMP, can be unified under the orthogonal principle. The simplicity and generality of OAMP provide efficient solutions for estimation problems beyond the classical linear models. As an example, we study the optimization of OAMP via the GS model and GS orthogonalization. More related applications will be discussed in a companion paper where new algorithms are developed for problems with multiple constraints and multiple measurement variables.

## Binary Modeling and Capacity-Approaching Coding for the IM/DD Channel

- **Status**: ❌
- **Reason**: IM/DD 광무선 채널 binary 모델링, polar 코드 기반이며 LDPC 디코더/코드설계 기여 없음
- **ID**: ieee:10078291
- **Type**: journal
- **Published**: May 2023
- **Authors**: Sarah Bahanshal, Ahmad Abdel-Qader, Anas Chaaban
- **PDF**: https://ieeexplore.ieee.org/document/10078291
- **Abstract**: The paper provides a new perspective on peak- and average-constrained Gaussian channels. Such channels model optical wireless communication (OWC) systems which employ intensity-modulation with direct detection (IM/DD). First, the paper proposes a new, capacity-preserving vector binary channel (VBC) model, consisting of dependent binary noisy bit-pipes. Then, to simplify coding over this VBC, the paper proposes coding schemes with varying levels of complexity, building on the capacity of binary-symmetric channels (BSC) and channels with state. The achievable rates are compared to capacity and capacity bounds, showing that coding for the BSC with state over the VBC achieves rates close to capacity at moderate to high signal-to-noise ratio (SNR), whereas simpler schemes achieve lower rates at lower complexity. The presented coding schemes are realizable using capacity-achieving codes for binary-input channels, such as polar codes. Numerical results are provided to validate the theoretical results and demonstrate the applicability of the proposed schemes.

## Energy-time entangled and Einstein-Podolsky-Rosen steerable large-alphabet quantum key distribution

- **Status**: ❌
- **Reason**: 고차원 양자키분배(QKD) 얽힘 실험, ECC 디코더 기법 없음.
- **ID**: ieee:10259321
- **Type**: conference
- **Published**: 7-12 May 2
- **Authors**: Kai-Chi Chang, Murat Can Sarihan, Xiang Cheng +1
- **PDF**: https://ieeexplore.ieee.org/document/10259321
- **Abstract**: We experimentally demonstrated the violation of energy-time entanglement and Einstein-Podolsky-Rosen steering inequality, toward high-dimensional quantum key distribution with secure photon information efficiency of 3.68 bits/coincidences, and secure key rate of 1.77 Mbits/s.

## Experimental symmetric private information retrieval with measurement-device-independent quantum network

- **Status**: ❌
- **Reason**: 양자 SPIR/PIR 보안 검색 실험, LDPC ECC 기법 없음.
- **ID**: ieee:10259085
- **Type**: conference
- **Published**: 7-12 May 2
- **Authors**: Chao Wang, Wen Yu Kon, Hong Jie Ng +1
- **PDF**: https://ieeexplore.ieee.org/document/10259085
- **Abstract**: We report the first realisation of a provably-secure symmetric private information retrieval (SPIR) scheme supported by a quantum-secure key-exchange network, offering secure retrieval of fingerprint data from a database with 800 entries.

## An Efficient Single and Double Error Correcting Block Codes with Low Redundancy for Digital Communications

- **Status**: ❌
- **Reason**: Hamming/BCH/RS 단·이중오류 정정 블록코드, 저잉여 — LDPC 무관
- **ID**: ieee:10141727
- **Type**: conference
- **Published**: 5-6 May 20
- **Authors**: Madan Lal Saini, Vivek Kumar Sharma, Ashok Kumar
- **PDF**: https://ieeexplore.ieee.org/document/10141727
- **Abstract**: In digital communication there are various single and double bit error correcting and detecting codes are available. The efficiency of an error correcting code is evaluated by its errors correction capabilities and redundancy. This paper presents a new single bit and double bit error correcting codes which have lower redundancy compare to the other existing codes. In this paper the number of parity bits over the message bits for Hamming, BCH,RS Code, and DEC are examined and overhead is calculated. The proposed codes having less parity bits compared to other existing and having up to double bit error correction capabilities and minimize the encoding/decoding time delay.

## Estimate BLER for Coded Modulation Based on Finite Block Coding

- **Status**: ❌
- **Reason**: LDPC/터보 coded modulation의 BLER 추정 이론 — 디코더/HW/구성으로 안 이어지는 성능 추정 기법
- **ID**: ieee:10139402
- **Type**: conference
- **Published**: 5-6 May 20
- **Authors**: Eva C. Song, Guosen Yue
- **PDF**: https://ieeexplore.ieee.org/document/10139402
- **Abstract**: In this paper11The work was done when the authors were with Futurewei Technologies, Bridgewater, NJ., we present a state-of-the-art method to estimate block error rate (BLER) for coded modulation with practical channel codes, e.g., turbo or low-density parity-check (LDPC) codes. The method is based on the theoretic breakthrough on the finite block coding and a novel rate combining model. With tuning on a very limited number of parameters, the estimates from the proposed method match very well with the simulation results. The proposed method can have wide ranges of applications for wireless communications.

## Data Encoding Techniques for Reducing Energy Consumption in Network-On-Chip

- **Status**: ❌
- **Reason**: NoC 에너지 저감 데이터 인코딩 개요 — ECC/LDPC 무관
- **ID**: ieee:10157433
- **Type**: conference
- **Published**: 5-6 May 20
- **Authors**: N. Ashokkumar, Bathala RedddiPrasanna, Biruduraju Varshitha +3
- **PDF**: https://ieeexplore.ieee.org/document/10157433
- **Abstract**: Energy consumption has become a major challenge in on-chip communication architectures such as Network-on-Chip as a result of the growing complexity of system-on-chips (SoCs) (NoC). Encoding techniques have recently gained attention as a potentially useful strategy for lowering the amount of power that a NoC design requires. These techniques intend to alter the manner in which data is transmitted through the communication stack in order to cut down on the number of transitions in the data and, as a consequence, lower the amount of power that is consumed. This paper presents an overview of data encoding techniques that can be used for NoC and discusses the effectiveness of these techniques in lowering the amount of energy that is consumed. Additionally, the importance of energy efficiency as a design constraint for modern SoCs is emphasised throughout the course of this paper. Based on the findings, it appears that data encoding techniques are a viable option for lowering the level of energy consumption in NoCs and have a significant bearing on the level of energy efficiency achieved by contemporary SoCs.

## SPELS: Scalable and Programmable Testbed for Evaluating LEO Satellite Swarm Communications

- **Status**: ❌
- **Reason**: LEO 위성 swarm 테스트베드+5G딥러닝 LDPC를 갖다 씀; 신규 디코더/구성 기여 없음, 응용 특이적
- **ID**: ieee:10225764
- **Type**: conference
- **Published**: 20-20 May 
- **Authors**: Venkata Srirama Rohit Kantheti, Shih-Chun Lin, Liang C. Chu
- **PDF**: https://ieeexplore.ieee.org/document/10225764
- **Abstract**: Low earth orbit (LEO) satellite communications promise next-generation mobile networks with seamless connectivity to rural, remote, and inaccessible areas. Notably, due to low-cost deployment and quick turn-around times in production, proliferated LEOs deployed and orchestrated as a swarm of satellites can support ultra-broad transmissions for the ever-evolving communications and aid current wireless network infrastructure. This paper introduces a scalable and programmable OTA (over-the-air) testbed, called SPELS, to provide a real-time architectural implementation of satellite swarm systems and demonstrate the testbed's effectiveness in online swarm communications. First, the in-lab SPELS testbed is established with COTS (commercial off-the-shelf) software-defined radios, a high-performance host computer, and wireless softwarization. Accordingly, the latest AI-enabled wireless communications and real-time signal processing constraints can be easily realized upon various frontends by decoupling radio swarm networks' control and data planes. Furthermore, based on the designed infrastructure, an end-to-end module is proposed for timely and resilient satellite swarm communications. This module consists of swarm-MRC, an optimal swarm combining technique, and a 5G-compliant deep learning-based LDPC scheme. Experimental evaluations validate the superiority of our swarm combiner with learning-enabled channel coding for online frontend operations, thus facilitating LEO swarm readiness.

## Content-Aware Semantic Communication for Goal-Oriented Wireless Communications

- **Status**: ❌
- **Reason**: 시맨틱 통신 JSCC 프레임워크, LDPC는 베이스라인; 떼어낼 ECC 기법 없음
- **ID**: ieee:10226153
- **Type**: conference
- **Published**: 20-20 May 
- **Authors**: Yuzhou Fu, Wenchi Cheng, Wei Zhang
- **PDF**: https://ieeexplore.ieee.org/document/10226153
- **Abstract**: While semantic communications can remarkably reduce the amount of the data transmission traffic without missing critical information, its applications to the efficient goal-oriented wireless communications remain limited. In this paper, we proposed the Content-Aware Semantic Communication (CA-SC) framework, which fuses both global and task-related semantic information via the semantic decoder, thus achieving the goal-oriented wireless communications. In particular, the CA-SC is based on the attention map to locate the task-related semantic information for supporting an adaptive rate allocation scheme. In order to further improve the coding rate as well as reconstructing intended data, we formulate a rate-distortion optimization problem as the loss function for the CA-SC framework, which aims to jointly optimize the semantic codec and the channel codec. Numerical results show that the CA-SC scheme can achieve better performance compared with existing semantic codec scheme and the traditional codec scheme in the image reconstruction task and the object detection task.

## A Survey on Various Decoding Algorithms for McEliece Cryptosystem Based on QC-MDPC Codes

- **Status**: ❌
- **Reason**: QC-MDPC McEliece 암호 디코딩 서베이, 비-LDPC(MDPC) 보안·서베이 — 제외
- **ID**: ieee:10152992
- **Type**: conference
- **Published**: 18-19 May 
- **Authors**: Abdellatif Kichna, Abderrazak Farchane
- **PDF**: https://ieeexplore.ieee.org/document/10152992
- **Abstract**: The McEliece cryptosystem has proven to be a secure and efficient method for protecting sensitive information in communication infrastructure. Among the variants of this cryptosystem, the quasi-cyclic moderate density parity-check (QC-MDPC) McEliece Cryptosystem has received significant attention due to its compact key size. This paper presents a comprehensive survey of the various decoding algorithms used for the QC-MDPC McEliece Cryptosystem. The performance and effectiveness of each algorithm in securing data in the face of quantum computing challenges is thoroughly evaluated. This survey provides valuable insights into the strengths and weaknesses of each decoding algorithm, and offers guidance for future research in the area of code-based cryptography for quantum computing.

## A Hybrid technique based on Zadoff-chu and Simplified Selective Mapping for PAPR Reduction in GFDM System

- **Status**: ❌
- **Reason**: GFDM PAPR 저감(SLM+ZCT), 변조 기법으로 LDPC ECC 무관 — 제외
- **ID**: ieee:10152931
- **Type**: conference
- **Published**: 18-19 May 
- **Authors**: Karima Ait Bouslam, Asma Khabba, Fatim-Zahra Bennioui +3
- **PDF**: https://ieeexplore.ieee.org/document/10152931
- **Abstract**: The GFDM modulation, a block of non- orthogonal modulation based on filtering in time and frequency axes, offers several benefits, including, high data rate, high flexibility, and high spectrum efficiency, which make it attractive to several 5G applications. However, GFDM suffers from a high PAPR reduction, which decreases GFDM system's performance. In this work, we propose novel hybrid technique for PAPR reduction based on Simplified Selective Mapping (SLM) and Zadoff-Chu Transform (ZCT). The simulations results show that our proposed technique outperforms the conventional SLM and ZCT techniques with about 53.52% in the improvement of the PAPR reduction.

## Realizing Uplink MU-MIMO Communication in mmWave WLANs: Bayesian Optimization and Asynchronous Transmission

- **Status**: ❌
- **Reason**: mmWave MU-MIMO 업링크 통신 스킴; LDPC 무관, 떼어낼 ECC 기법 없음
- **ID**: ieee:10228888
- **Type**: conference
- **Published**: 17-20 May 
- **Authors**: Shichen Zhang, Bo Ji, Kai Zeng +1
- **PDF**: https://ieeexplore.ieee.org/document/10228888
- **Abstract**: With the rapid proliferation of mobile devices, the marriage of millimeter-wave (mmWave) and MIMO technologies is a natural trend to meet the communication demand of data-hungry applications. Following this trend, mmWave multiuser MIMO (MU-MIMO) has been standardized by the IEEE 802.11ay for its downlink to achieve multi-Gbps data rate. Yet, its uplink counterpart has not been well studied, and its way to wireless local area networks (WLANs) remains unclear. In this paper, we present a practical uplink MU-MIMO mmWave communication (UMMC) scheme for WLANs. UMMC has two key components: i) an efficient Bayesian optimization (BayOpt) framework for joint beam search over multiple directional antennas, and ii) a new MU-MIMO detector that can decode asynchronous data packets from multiple user devices. We have built a prototype of UMMC on a mmWave testbed and evaluated its performance through a blend of over-the-air experiments and extensive simulations. Experimental and simulation results confirm the efficiency of UMMC in practical network settings.

## Rate-Compatible Joint Source-Channel Coding Scheme Based on 5GNR LDPC Codes

- **Status**: ❌
- **Reason**: 5GNR LDPC 기반 joint source-channel coding 소스코딩 행렬 구성 — JSCC/소스코딩, 채널 ECC 떼어낼 기법 아님, 제외
- **ID**: ieee:10154810
- **Type**: conference
- **Published**: 17-19 May 
- **Authors**: Hao Dong, Kai Niu, Bichai Wang +1
- **PDF**: https://ieeexplore.ieee.org/document/10154810
- **Abstract**: In this paper, we propose a simple source coding matrix construction method. At first, the entropy rate H of the source is evaluated. The source coding rate Rs is determined by the height-to-width ratio of the source coding matrix. Therefore, the base matrix B1 of 5GNR is transposed and cropped to the needed size, and the source coding base matrix Bs is generated. Finally, the source coding base matrix is transformed into the purpose-sized source coding matrix Hs via the Lifting operation. In addition, this paper proposes a method to optimize the decoding threshold. Replacing the unit matrix in the joint parity-check matrix with the permutation matrix can reduce the decoding threshold. The proposed method in this paper is easy to integrate into existing 5GNR coding systems and can accommodate many different code length-code rate combinations just like the LDPC codes of 5GNR. In terms of complexity, the construction process is relatively simple and can share parameters with the 5GNR LDPC codes to avoid the storage space overhead of storing an additional set of coding matrices.

## PAC Code Construction for Spin-Torque Transfer Magnetic Random Access Memory

- **Status**: ❌
- **Reason**: 10228359과 동일 STT-MRAM PAC 코드 구성(중복) — 비-LDPC, 이식 기법 없음
- **ID**: ieee:10265017
- **Type**: conference
- **Published**: 15-19 May 
- **Authors**: Bin Dai, Zhen Mei, Kui Cai +2
- **PDF**: https://ieeexplore.ieee.org/document/10265017
- **Abstract**: Spin-torque transfer magnetic random access memory (STT-MRAM) is one potential candidate to replace the dynamic random access memory (DRAM) due to its superior features of nonvolatility, fast read/write speed, and high scalability. The error correction coding methods are applied to improve the reliability of STT-MRAM which is affected by the process variation and thermal fluctuation. In this paper, we investigate, for the first time, the design and optimization of the polarization-adjusted convolutional (PAC) code for the STT-MRAM channel. A crucial problem for the application of PAC codes to the STT-MRAM channel is the optimization of the index set of the non-frozen bits of the PAC codes. Hence, a rate-profile optimization method based on the genetic-algorithm-assisted bit-swapping is proposed. Simulation results show that the PAC code with the optimized rate-profile outperforms both the polar code and the PAC code with existing generic rate-profiles.

## PAC Code Construction for Spin-Torque Transfer Magnetic Random Access Memory

- **Status**: ❌
- **Reason**: STT-MRAM용 PAC(polar 계열) 코드 구성 — 비-LDPC, 바이너리 LDPC BP로 떼어낼 기법 없음
- **ID**: ieee:10228359
- **Type**: conference
- **Published**: 15-19 May 
- **Authors**: Bin Dai, Zhen Mei, Kui Cai +2
- **PDF**: https://ieeexplore.ieee.org/document/10228359
- **Abstract**: In this paper, we investigate, for the first time, the design and optimization of the polarization-adjusted convolutional (PAC) code for the spin-torque transfer magnetic random access memory (STT-MRAM) channel. A crucial problem for the application of PAC codes to the STT-MRAM channel is to optimize the index set of the non-frozen bits of the PAC codes. Hence, a rate-profile optimization method based on the genetic algorithm assisted bit-swapping is proposed. Simulation results show that the PAC code with the optimized rate-profile outperforms both the polar code and the PAC code with existing generic rate-profiles.

## The Main Factors Influencing the Effectiveness of the Noise-Resistant Method of Information Transmission

- **Status**: ❌
- **Reason**: 잡음내성 신호처리/2채널 동기수신 — LDPC 부호·디코더 기법 없음, 떼어낼 ECC 기법 부재
- **ID**: ieee:10139176
- **Type**: conference
- **Published**: 15-19 May 
- **Authors**: Dmitrii Artamonov, Nikolay Grachev, Boris Utkin
- **PDF**: https://ieeexplore.ieee.org/document/10139176
- **Abstract**: One of the most important indicators of the quality of radio information transmission systems is noise immunity. The most significant impact is caused by interference exceeding the level of the useful signal. In the author's previous work, a method of digital signal processing was published to combat interference of this kind. The article describes a mathematical and software model of two-channel synchronous signal reception with the results in the form of a dependence of the probability of block errors in the transmitted information on the signal / (interference + noise) ratio, where the result of the noise immunity of the system to minus 26.5 dB was achieved. However, like any other method, the proposed one has its weaknesses. This work describes and analyzes the main factors affecting the effectiveness of the method under study.

## Optimization of Root-Protograph LDPC Codes for Joint Source Channel Coding System over Block Fading Channel

- **Status**: ❌
- **Reason**: JSCC 소스-채널 결합 RPLDPC 코드 설계. JSCC가 베이스, 채널 ECC로 떼어낼 신규 기법 부족
- **ID**: ieee:10217261
- **Type**: conference
- **Published**: 12-14 May 
- **Authors**: Jihua Wu, Mengyao Wang, Qiwang Chen +1
- **PDF**: https://ieeexplore.ieee.org/document/10217261
- **Abstract**: Double protograph low-density parity-check (DP-LDPC) codes based on the joint source channel coding (JSCC) system has been demonstrated to have outstanding error performance over additive white Gaussian noise (AWGN) channels. However, because of the non-ergodic nature of the block-fading (BF) channels, the protograph low-density parity-check (PLDPC) codes cannot perform well over BF channel. Whereby the excellent error performance of root protograph LDPC (RPLDPC) codes under BF channel, we utilize RPLDPC codes for channel coding in DP_LDPC systems over BF channels. Then, we design a modified joint protograph extrinsic information transfer (JPEXIT) algorithm to calculate the decoding threshold of this system. utilizing the modified JPEXIT algorithm, to improve the error performance of the system. The traditional root protograph LDPC (RPLDPC) code for this system has been redesigned. The research results display that the systems with improved RPLDPC codes have lower decoding thresholds and faster convergence trend than existing RPLDPC codes and PLDPC codes.

## Protograph LDPC-Based Joint Source-Channel Coding for Markov Sources

- **Status**: ❌
- **Reason**: JSCC(소스-채널 결합) 프로토그래프 LDPC, 소스코드 최적화 중심 — 떼어낼 NAND ECC 기법 없음, 기준상 JSCC 제외
- **ID**: ieee:10217316
- **Type**: conference
- **Published**: 12-14 May 
- **Authors**: Shiwei Zhu, Haoyu Xu, Xin Feng +1
- **PDF**: https://ieeexplore.ieee.org/document/10217316
- **Abstract**: In this paper, we investigate the protograph LDPC-based joint source-channel coding (JSCC) system for transmitting Markov sources and propose a re-design approach for source codes in this system. To sufficiently utilize the memory structure inherent within the source sequence, firstly, we propose a novel joint source-channel (JSC) decoding technique with a three-stage serially concatenated framework. Secondly, the source protograph extrinsic information transfer (PEXIT) algorithm is modified to evaluate the source decoding threshold, which can analyze the error-floor performance for this system. Finally, the conventional source codes are optimized to improve the performance on the error-floor region. Both the bit-error-rate (BER) results and the modified source PEXIT algorithm show considerable performance gains over the systems in which the temporal correlations are not utilized. Also, the optimized source codes can acquire better source decoding thresholds than traditional codes, which perform better the error-floor performance in the JSCC system.

## A code-assisted carrier synchronization algorithm based on Expectation-Maximum algorithm

- **Status**: ❌
- **Reason**: LDPC 디코더 사후확률을 이용한 EM 기반 반송파 동기화. 동기화 응용이 핵심, 떼어낼 LDPC ECC 기법 없음
- **ID**: ieee:10176829
- **Type**: conference
- **Published**: 12-14 May 
- **Authors**: Jiahao Sun
- **PDF**: https://ieeexplore.ieee.org/document/10176829
- **Abstract**: The performance of the LDPC decoder suffers from deterioration when receiving a signal with residual carrier bias. To address this problem, a carrier synchronization algorithm assisted by LDPC code is proposed. The proposed algorithms include rough carrier estimation and carrier fine estimation based on Expectation-Maximum (EM) algorithm. To reduce the problem of high resource consumption, a cost function that is only related to residual frequency bias is proposed in this article. An iterative carrier fine estimation algorithm using posteriori probability obtained by the LDPC decoder is proposed based on EM algorithm, and the analytic solution of the algorithm is derived in this article. The simulation results validated that the proposed algorithm has a large estimation range, and realizes effective carrier synchronization at a low signal-to-noise ratio (SNR).
