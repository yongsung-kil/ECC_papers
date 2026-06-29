# IEEE Xplore — 2023-02 (1차선별 통과)


## Design of Implicit Partial Product-LDPC Codes and Low Complexity Decoding Algorithm

- **Status**: ✅
- **Reason**: IP-LDPC(LDPC+BCH) 신규 product code 설계 + bit-flipping 디코더, 코드설계/디코더 기여(C/E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9987569
- **Type**: journal
- **Published**: Feb. 2023
- **Authors**: Yinchu Wang, Qianfan Wang, Xiao Ma
- **PDF**: https://ieeexplore.ieee.org/document/9987569
- **Abstract**: In this letter, we are concerned with a recently proposed class of product codes, called implicit partial product low-density parity-check (IP-LDPC) codes, which consist of LDPC codes for rows and Bose-Chaudhuri-Hocquenghem (BCH) codes for columns. Distinguished from the conventional product codes, only partial columns are doubly-protected and the column checks are transmitted implicitly rather than explicitly. For any given LDPC code, we present three heuristic rules to design an IP-LDPC code with the same code rate, showing how to select the number of doubly-protected columns and the BCH code (for columns). The stringent constraint is that the product of the number of doubly-protected columns and the length of syndrome per column must be less than or equal to the product of the number of the rows and the length of extra bits that can be carried reliably and implicitly per row (LDPC codeword). We also propose a simple bit-flipping algorithm for the column decoding in the case when the number of unsuccessfully decoded rows is relatively small, which occurs often especially when the iterative decoding is implemented. The simulation results show that IP-LDPC codes can lower down the word error rate (WER) of a (3,6)-regular LDPC code with length 1024 from 10−2 to 10−6 at the SNR around 2.0 dB but without any code rate loss.

## Normalized Min-Sum Neural Network for LDPC Decoding

- **Status**: ✅
- **Reason**: NMS 신경망 디코더, 파라미터 공유+12bit 양자화로 곱셈기 절감 — 이식 가능 디코더(C), LLR 양자화 NAND 적용 유망
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9913203
- **Type**: journal
- **Published**: Feb. 2023
- **Authors**: Qing Wang, Qing Liu, Shunfu Wang +5
- **PDF**: https://ieeexplore.ieee.org/document/9913203
- **Abstract**: The success of deep learning has encouraged its applications in decoding error-correcting codes, e.g., LDPC decoding. In this paper, we propose a model-driven deep learning method for normalized min-sum (NMS) low-density parity-check (LDPC) decoding, namely neural NMS (NNMS) LDPC decoding network. By unfolding the iterative decoding progress between checking nodes (CNs) and variable nodes (VNs) into a feed-forward propagation network, we can harvest the benefits of both the model-driven deep learning and the conventional normalized min-sum (NMS) LDPC decoding method. In addition, we proposed a shared parameters NNMS with the LeakyReLU and a 12-bit quantizer (SNNMS-LR-Q) which reduces the number of required multipliers and correction factors by sharing parameters, increasing the nonlinear fitting ability by adding LeakyReLU. By utilizing the 12-bit quantizer, we can improve the confrontation ability. Thorough experiments with different code lengths, code rates, channel conditions, and check matrices are implemented to demonstrate the advantages and robustness of our proposed networks. The BER performance of the proposed NNMS is 1.5 dB better than the NMS, using fewer iterations. Meanwhile, The SNNMS-LR-Q outperforms the NNMS regarding the BER performance and efficiency.

## Minimum Repair Bandwidth LDPC Codes for Distributed Storage Systems

- **Status**: ✅
- **Reason**: 분산 스토리지용 바이너리 LDPC 코드 패밀리 최적화 설계, 스토리지 ECC + 코드설계(B/E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9991130
- **Type**: journal
- **Published**: Feb. 2023
- **Authors**: Massoud Pourmandi, Ali Emre Pusane, Suayb S. Arslan +1
- **PDF**: https://ieeexplore.ieee.org/document/9991130
- **Abstract**: In distributed storage systems (DSS), an optimal code design must meet the requirements of efficient local data regeneration in addition to reliable data retention. Recently, low-density parity-check (LDPC) codes have been proposed as a promising candidate that can secure high data rates as well as low repair bandwidth while maintaining low complexity in data reconstruction. The main objective of this study is to optimize the repair bandwidth characteristics of LDPC code families for a DSS application while meeting the data reliability requirements. First, a data access scenario in which nodes contact other available nodes randomly to download data is examined. Later, a minimum-bandwidth protocol is considered in which nodes make their selections based on the degree numbers of check nodes. Through formulating optimization problems for both protocols, a fundamental trade-off between the decoding threshold and the repair bandwidth is established for a given code rate. Finally, conclusions are confirmed by numerical results showing that irregular constructions have a large potential for establishing optimized LDPC code families for DSS applications.

## Model-Driven Deep Learning ADMM Decoder for Irregular Binary LDPC Codes

- **Status**: ✅
- **Reason**: 비이진 LDPC용 model-driven ADMM 딥러닝 디코더, 바이너리 LDPC 대상이며 새 디코더 알고리즘(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9954388
- **Type**: journal
- **Published**: Feb. 2023
- **Authors**: Xiaomeng Guo, Tsung-Hui Chang, Yongchao Wang
- **PDF**: https://ieeexplore.ieee.org/document/9954388
- **Abstract**: In this letter, a model-driven deep learning (DL) decoder for irregular binary low-density parity-check (LDPC) codes is proposed via the alternating direction method of multipliers (ADMM) technique. Our technical contributions three twofold: 1) we formulate the maximum likelihood decoding problem as a non-convex quadratic program with a new penalty term and present an ADMM based decoder; 2) to alleviate hyper-parameter tuning, we employ the deep unfolding strategy to derive a model-driven ADMM-DL decoder; and 3) to save the number of learning parameters, we propose an initialization strategy which can apply to different codeword structures. Specifically, the designing procedure for the DL network structure and DL network parameters training algorithm are presented in detail for efficient implementation. Numerical results demonstrate that the proposed model-driven ADMM-DL decoder for irregular binary LDPC codes is competitive in comparison with the state-of-the-arts.

## A Low-Complexity RS-SPC Product Coding Scheme for Optical Systems

- **Status**: ✅
- **Reason**: RS-SPC product code의 하이브리드 반복 디코딩+조기정지 기법, LDPC 대안이나 디코더 기법 이식 가능(C), 애매하여 in
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9999449
- **Type**: journal
- **Published**: Feb. 2023
- **Authors**: Mingyang Zhu, Ming Jiang, Chunming Zhao +1
- **PDF**: https://ieeexplore.ieee.org/document/9999449
- **Abstract**: This paper presents a product coding scheme based on binary images of Reed-Solomon (RS) codes and single-parity-check (SPC) codes for high-speed communications. Utilizing the special selection of components, we propose hybrid soft- and hard-decision iterative decoding (ID) algorithms for these codes, during which many RS component decoders can be early terminated. The proposed hybrid ID only exchanges ternary messages between component decoders and early stops the RS component decoders satisfying a proposed stopping criterion, thus low hardware and computational complexities are guaranteed. The hybrid ID of RS-SPC product codes not only performs comparable to the soft-decision decoding of low-density parity-check (LDPC) codes and block turbo codes (BTCs), but also takes much lower computational complexity and smaller decoder data flow. We also propose semi-analytical methods to estimate the waterfall and error-floor performances of the proposed scheme, which yield relatively accurate estimated results. The simulation results and error-floor estimations indicate that some good RS-SPC product codes have very low error floors that satisfy the requirements of optical systems.

## Irregular-Mapped Protograph LDPC-Coded Modulation: A Bandwidth-Efficient Solution for 6G-Enabled Mobile Networks

- **Status**: ✅
- **Reason**: Protograph LDPC for NAND flash with IMARA code construction (EPEXIT) and read-voltage optimization; direct NAND + new binary code design (A/E).
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9600574
- **Type**: journal
- **Published**: Feb. 2023
- **Authors**: Yi Fang, Yingcheng Bu, Pingping Chen +2
- **PDF**: https://ieeexplore.ieee.org/document/9600574
- **Abstract**: The huge amount of data produced in the 6G networks not only brings new challenges to the reliability and efficiency of mobile devices but also drives rapid development of new storage techniques. With the benefits of fast access speed and high reliability, NAND flash memory has become a promising storage solution for the 6G networks. In this paper, we investigate a protograph-coded bit-interleaved coded modulation with iterative detection and decoding (BICM-ID) utilizing irregular mapping (IM) in the NAND flash-memory systems. First, we propose an enhanced protograph-based extrinsic information transfer (EPEXIT) algorithm to facilitate the analysis of protograph codes in the IM-BICM-ID systems. With the use of EPEXIT algorithm, a simple design method is conceived for the construction of a family of high-rate protograph codes, called irregular-mapped accumulate-repeat-accumulate (IMARA) codes, which possess excellent decoding thresholds and linear-minimum-distance-growth property. Furthermore, motivated by the voltage-region iterative gain characteristics of IM-BICM-ID systems, a novel read-voltage optimization scheme is developed to acquire accurate read-voltage levels, thus minimizing the decoding thresholds (in dB) of protograph codes. Analyses and simulations indicate that the proposed IMARA-aided IM-BICM-ID scheme and read-voltage optimization scheme remarkably improve the convergence and decoding performance of flash-memory systems. Thus, the proposed protograph-coded IM-BICM-ID can be viewed as a reliable and efficient storage solution for the new-generation mobile networks, such as Internet of Vehicles.

## Breaking the Computational Bottleneck: Probabilistic Optimization of High-Memory Spatially-Coupled Codes

- **Status**: ✅
- **Reason**: 고메모리 SC-LDPC 유한길이 구성 신규 확률적 최적화, 플래시 채널서도 이득 — 이식 가능 바이너리 코드 설계(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9893853
- **Type**: journal
- **Published**: Feb. 2023
- **Authors**: Siyi Yang, Ahmed Hareedy, Robert Calderbank +1
- **PDF**: https://ieeexplore.ieee.org/document/9893853
- **Abstract**: Spatially-coupled (SC) codes, known for their threshold saturation phenomenon and low-latency windowed decoding algorithms, are ideal for streaming applications and data storage systems. SC codes are constructed by partitioning an underlying block code, followed by rearranging and concatenating the partitioned components in a convolutional manner. The number of partitioned components determines the memory of SC codes. In this paper, we investigate the relation between the performance of SC codes and the density distribution of partitioning matrices. While adopting higher memories results in improved SC code performance, obtaining finite-length, high-performance SC codes with high memory is known to be computationally challenging. We break this computational bottleneck by developing a novel probabilistic framework that obtains (locally) optimal density distributions via gradient descent. Starting from random partitioning matrices abiding by the obtained distribution, we perform low-complexity optimization algorithms that minimize the number of detrimental objects to construct high-memory, high-performance quasi-cyclic SC codes. We apply our framework to various objects of interest, from the simplest short cycles, to more sophisticated objects such as concatenated cycles aiming at finer-grained optimization. Simulation results show that codes obtained through our proposed method notably outperform state-of-the-art SC codes with the same constraint length and optimized SC codes with uniform partitioning. The performance gain is shown to be universal over a variety of channels, from canonical channels such as additive white Gaussian noise and binary symmetric channels, to practical channels underlying flash memory and magnetic recording systems.

## A Low-Complexity Ordered Statistic Decoding of Short Block Codes

- **Status**: ✅
- **Reason**: LC-OSD: 새 OSD 변형(SLVA 트렐리스 + 조기정지)으로 short block 디코더 기법, 카테고리 C 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9954013
- **Type**: journal
- **Published**: Feb. 2023
- **Authors**: Jifan Liang, Yiwen Wang, Suihua Cai +1
- **PDF**: https://ieeexplore.ieee.org/document/9954013
- **Abstract**: This letter is concerned with a generalized ordered statistic decoding (OSD) algorithm, called locally constrained OSD (LC-OSD). Instead of order- $t$  reprocessing on the most reliable independent bits, the LC-OSD searches for test error patterns using the serial list Viterbi algorithm (SLVA) over a trellis specified by a local parity-check matrix. We derive several early stopping criteria that can be used to reduce the number of searches. Numerical results show that the LC-OSD algorithm with the proposed stopping criteria has much lower time complexity than the original OSD but incurs negligible performance loss.

## Ensemble Belief Propagation Decoding for Short Linear Block Codes

- **Status**: ✅
- **Reason**: Multiple-Bases BP(MBBP) 앙상블 디코딩, 다양한 parity-check matrix 생성 — BP 디코더 개선 기법 LDPC에 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10104564
- **Type**: conference
- **Published**: 27-27 Feb.
- **Authors**: Kira Kraft, Matthias Herrmann, Oliver Griebel +1
- **PDF**: https://ieeexplore.ieee.org/document/10104564
- **Abstract**: The upcoming communication standard 6G is expected to specify high demands on the efficiency of current communication systems, especially on the latency and error correction performance of the decoding unit. A well-investigated algorithm that allows a low-latency implementation is Belief Propagation (BP) decoding on the Tanner graph, which is the state-of-the-art decoding algorithm for Low-Density Parity-Check (LDPC) codes. In this paper, we present a methodology to apply this BP algorithm to non-LDPC codes while achieving a good error correction performance. In addition, we propose a method to generate a diverse ensemble of parity-check matrices for short linear block codes to enable the use of Multiple-Bases Belief Propagation (MBBP), an extension to BP, further improving the error correction performance of LDPC and non-LDPC codes. At the example of LTE Turbo codes, our results show that this approach is capable of achieving the error-correcting performance of the Turbo code’s state-of-the-art max-Log MAP algorithm, while being a universal approach for decoding any kind of short linear block code.

## Boost Sum-Product Performance for Multiuser Detection in mMTC at Millimeter Wave

- **Status**: ✅
- **Reason**: factor-graph 단축사이클 제거(node-split/contraction)와 동적계획 기반 메시지 근사로 sum-product 개선 — 부호 비의존적 BP 디코더 기법으로 바이너리 LDPC에 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9456076
- **Type**: journal
- **Published**: 1 Feb. 202
- **Authors**: Tao Huang, Baoliu Ye, Bin Tang +3
- **PDF**: https://ieeexplore.ieee.org/document/9456076
- **Abstract**: We consider the multiuser detection (MUD) problem, i.e., how to separate and decode colliding data streams, in the uplink of massive Machine Type Communications (mMTC) at millimeter wave (mmWave). Operating on factor-graphs by passing messages, the sum-product algorithm and its variants are widely applied in many other scenarios. However, in this paper, we find that their performance in mMTC at mmWave could be dramatically degraded due to the ill-conditioned MUD channel gain matrix and the existence of enormous short cycles in their corresponding factor-graphs, which are caused by the limited scattering of mmWave and the sharing of a same codebook for error correction among densely located user equipments. Assuming LDPC codes are used for error correction, we further propose a novel sum-product based approach to dealing with the MUD problem in mMTC at mmWave. It first leverages the propagation characteristics of mmWave to optimize the factor-graph for MUD by removing short cycles based on node-split and node-contraction, and then takes a dynamic-programming based method to approximate the messages passing on the resulted factor-graph, which can achieve a higher decoding accuracy. Extensive simulation results show that our approach outperforms the state-of-the-art sum-product based approaches significantly.
