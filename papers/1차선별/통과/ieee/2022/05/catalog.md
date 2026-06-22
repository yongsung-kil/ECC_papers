# IEEE Xplore — 2022-05 (1차선별 통과)


## Optimization of SC-LDPC Codes for Window Decoding With Target Window Sizes

- **Status**: ✅
- **Reason**: E: new optimization metric (window mean parameter) and code construction for binary SC-LDPC under window decoding; new contribution
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9732353
- **Type**: journal
- **Published**: May 2022
- **Authors**: Hee-Youl Kwak, Jae-Won Kim, Hosung Park +1
- **PDF**: https://ieeexplore.ieee.org/document/9732353
- **Abstract**: In this paper, we propose an optimization method for protograph-based spatially coupled low-density parity-check (SC-LDPC) codes under window decoding (WD). Previous works on constructing SC-LDPC codes for WD typically focused on optimizing asymptotic performance metrics such as the WD threshold. However, in this paper, it is observed that the WD threshold is not an appropriate metric to sufficiently explain the finite-length behavior of SC-LDPC codes under WD. Thus, we propose a new performance metric, called the window mean parameter, based on a scaling analysis to capture the WD performance more accurately and formulate a code optimization algorithm that optimizes the proposed performance metric. Since the proposed metric depends on the window size, the optimization algorithm can provide a code family of SC-LDPC codes optimized for various target window sizes. Simulation results confirm that the improvement in the proposed metric leads to a finite-length performance improvement, resulting in one to two orders of the frame error rate gain over the conventional SC-LDPC codes for a wide range of window sizes. Furthermore, we investigate structural characteristics of the proposed codes to provide a supplementary explanation for the performance improvement, which also promotes a better understanding of SC-LDPC codes for WD.

## Multi-Mode QC-LDPC Decoding Architecture With Novel Memory Access Scheduling for 5G New-Radio Standard

- **Status**: ✅
- **Reason**: QC-LDPC 디코더 VLSI 아키텍처, 부분 병렬화 및 신규 메모리 접근 스케줄링(65nm 20Gbps) — 이식 가능 HW 아키텍처(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:9714891
- **Type**: journal
- **Published**: May 2022
- **Authors**: Seongjin Lee, Sangsoo Park, Boseon Jang +1
- **PDF**: https://ieeexplore.ieee.org/document/9714891
- **Abstract**: As the low-density parity-check (LDPC) code has a powerful error-correcting performance and can achieve high throughput, it is being used in many application areas and recently adopted as a channel coding method in the 5G New-Radio communication standard. Unlike other LDPC codes, the 5G LDPC code has various irregular lifting sizes to support diverse message lengths. To meet the demanding requirements of the 5G standard, many solutions have been presented, but all of them are either impractical or fail to satisfy all the requirements. This paper, for the first time, proposes an area-efficient QC-LDPC decoder that satisfies the peak throughput requirements of the 5G standard and supports all the lifting sizes specified in the 5G standard. Instead of relying on full parallelism like in the previous works, this work tries partial parallelism to mitigate the hardware complexity, which leads to high efficiency in hardware complexity. In addition, a novel memory access scheduling method is proposed to solve the data access and alignment problems caused by the partially parallel structure, which is effective in supporting all the lifting sizes. A LDPC decoder realized in 65-nm CMOS technology demonstrates that its decoding throughput is greater than 20Gbps and its area is smaller than the existing decoders.

## Lower Bounds of Regular QC-LDPC Codes and SES Generation Algorithm

- **Status**: ✅
- **Reason**: E: new lower bounds + SES algorithm for binary QC-LDPC construction with girth up to 12 (new contribution beyond textbook girth removal)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9721882
- **Type**: journal
- **Published**: May 2022
- **Authors**: Aleksei Kharin, Aleksei Dryakhlov, Konstantin Zavertkin +2
- **PDF**: https://ieeexplore.ieee.org/document/9721882
- **Abstract**: In this letter we propose a new approach to generation of regular QC-LDPC codes with girth up to 12. The aim of the proposed smart exhaustive search (SES) algorithm is to construct codes with the desired lifting factor or to check whether codes with this parameter even exist. We define new lower bounds on the lifting degree as a necessary condition for the lifted graph to have a certain girth from fully connected base graphs. This modification opens space for improvement of the lifting factor minimisation problem for QC-LDPC code construction. With a more precisely defined search region it is possible to achieve better results with existing algorithms.

## Deep-Learning for Breaking the Trapping Sets in Low-Density Parity-Check Codes

- **Status**: ✅
- **Reason**: C: novel deep-learning decoder breaking trapping sets, improves error-floor for storage devices; directly portable to NAND LDPC
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9729722
- **Type**: journal
- **Published**: May 2022
- **Authors**: Seokju Han, Jieun Oh, Kyungmok Oh +1
- **PDF**: https://ieeexplore.ieee.org/document/9729722
- **Abstract**: In the low-error rate regime, message-passing (MP) decoding for low-density parity-check (LDPC) codes is known to have performance degradation due to trapping sets (TSs), which often limits the use of LDPC codes for applications with low target error rates like storage devices. This work proposes a novel deep-learning based decoding algorithm which is tailored for breaking TSs. In particular, when MP decoding fails due to TSs, there exist pairs of unsatisfied check nodes (CNs) which are connected through paths only with error variable nodes (VNs), i.e., VNs with erroneous hard-decision results. The proposed algorithm efficiently identifies the paths with error VNs between unsatisfied CNs with the aid of deep-learning techniques. Then, the decoding failures are resolved by repeating the MP decoding after re-initializing the channel outputs for the error VNs in the identified paths. In addition, by analyzing the behaviors of the deep-learning based algorithm, we propose a low-complexity algorithm, called adaptive-error-path (AEP) detector. Simulation results show that the proposed algorithms efficiently break the TSs and significantly improve the error-floor performance in the low error-rate regime.

## Low Complexity Majority-Logic Decoding for LDPC-Coded PNC Systems

- **Status**: ✅
- **Reason**: LDPC용 저복잡도 majority-logic decoding 및 reliability-based 변형 제안 — 이식 가능 디코더 알고리즘(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9714392
- **Type**: journal
- **Published**: May 2022
- **Authors**: Xiaoqian Xie, Pingping Chen, Yi Fang +1
- **PDF**: https://ieeexplore.ieee.org/document/9714392
- **Abstract**: In this letter, we propose majority-logic decoding (MLGD) algorithms of low complexity for low-density parity-check (LDPC) coded physical-layer network coding (PNC) in a two-way relay channel (TWRC). In particular, we decode the transmit combination of two-user messages from the superimposed signal and then map the XOR message of two users. By exploiting the superposition rules of PNC, we develop hard decision-based and reliability-based decoding algorithms, i.e., modified one-step MLGD (M-OSMLGD) and iterative soft reliability-based decoding (M-ISRB), to iteratively update the combination of two-user messages. Moreover, we propose an improved M-ISRB (IM-ISRB) decoding to update the external reliability of the combination of two-user messages in each iteration. Simulation results show that the proposed decoding algorithms can achieve effective an trade-off between complexity and decoding performance for LDPC-coded PNC systems.

## An Improved EPA-Based Receiver Design for Uplink LDPC Coded SCMA System

- **Status**: ✅
- **Reason**: LDPC-SCMA에 EPA 기반 joint detection-decoding을 aggregated factor graph로 수행 — BP/EPA 디코더 변형(C) 이식 여지, 애매하나 in
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9714274
- **Type**: journal
- **Published**: May 2022
- **Authors**: Lingyun Chai, Zilong Liu, Pei Xiao +2
- **PDF**: https://ieeexplore.ieee.org/document/9714274
- **Abstract**: Sparse code multiple access (SCMA) is an emerging paradigm for efficient enabling of massive connectivity in future machine-type communications (MTC). In this letter, we conceive the uplink transmissions of the low-density parity check (LDPC) coded SCMA system. Traditional receiver design of LDPC-SCMA system, which is based on message passing algorithm (MPA) for multiuser detection followed by individual LDPC decoding, may suffer from the drawback of the high complexity and large decoding latency, especially when the system has large codebook size and/or high overloading factor. To address this problem, we introduce a novel receiver design by applying the expectation propagation algorithm (EPA) to the joint detection and decoding (JDD) involving an aggregated factor graph of LDPC code and sparse codebooks. Our numerical results demonstrate the superiority of the proposed EPA based JDD receiver over the conventional Turbo receiver in terms of both significantly lower complexity and faster convergence rate without noticeable error rate performance degradation.

## Performance Evaluation of Bit-Flipping Based Algorithms for LDPC Convolutional Codes

- **Status**: ✅
- **Reason**: LDPC-CC용 BF/WBF/MWBF/IRRWBF 비트플립 디코더 평가; 저복잡도 디코더 기법 NAND 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9955830
- **Type**: conference
- **Published**: 6-10 May 2
- **Authors**: Oulfa Laouar, Imed Amamra, Nadir Derouiche
- **PDF**: https://ieeexplore.ieee.org/document/9955830
- **Abstract**: It has previously been shown that ensembles of terminated LDPC convolutional codes (LDPC-CC) have an error performance comparable to that of their counterparts LDPC codes. Also they are capable of achieving capacity approaching performance with iterative message-passing decoding on the AWGN channel. In terms of complexity, throughput and latency of iterative decoding algorithms, various interesting tradeoffs have been compared between the two different types of codes. In this paper, we review Bit-Flipping (BF) decoding algorithm and its variants. We adapt BF, WBF (Weighted Bit-Flipping), MWBF (Improved Weighted Bit-Flipping) and IRRWBF (Implementation-Efficient Reliability Ratio-based WBF) decoding variants, in order to evaluate the bit error rate (BER) performance of LDPC-CCs. Extensive computer simulations and comparisons are provided to demonstrate the efficiency of LDPC-CCs and the differences between the considered variants of BF decoding algorithm.

## Multilayer Perceptron-based Detector for a Coded Two-Dimensional Magnetic Recording

- **Status**: ✅
- **Reason**: MLP 기반 soft-output(LLR) 검출기 + LDPC turbo 디코딩 — 신경망 LLR 추정 기법 이식 가능(C), 애매하나 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9795450
- **Type**: conference
- **Published**: 24-27 May 
- **Authors**: Chaiwat Buajong, Chanon Warisam
- **PDF**: https://ieeexplore.ieee.org/document/9795450
- **Abstract**: Recently, magnetic recording technology is on the verge of reaching its recording density limit. Two-dimensional (2- D) magnetic recording (TDMR) becomes a candidate for next- generation magnetic recording because of its compatibility with the current technology and powerful 2-D signal processing tools. However, the degradation in signal quality due to 2-D interference is inevitable. In this paper, we introduce the multilayer perceptron (MLP)-based detector that can produce soft-output information in the form of a log-likelihood ratio (LLR). Such a detector can also execute turbo decoding by exchanging information with a low- density parity-check (LDPC) code. The simulation result shows that the proposed system outperforms the systems that use the conventional detector based on the Viterbi algorithm.

## A Clustering-based ML Scheme for Capacity Approaching Soft Level Sensing in 3D TLC NAND

- **Status**: ✅
- **Reason**: 3D TLC NAND soft-level sensing 클러스터링 ML로 LDPC 디코딩 성능 개선 — A 직접 해당
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9746590
- **Type**: conference
- **Published**: 23-27 May 
- **Authors**: Li-Wei Liu, Yen-Ching Liao, Hsie-Chia Chang
- **PDF**: https://ieeexplore.ieee.org/document/9746590
- **Abstract**: In a 3D TLC solid-state storage system, the LDPC decoding performance is significantly affected by the quality of soft-level sensing. Inspired by the capacity-approaching maximum mutual-information method, this work presents the data-driven approach to collect all the optimal 2-bit soft-read level pairs over the 3D TLC NAND. Due to the data transmission latency and limited configuration resources, a clustering method is proposed to extract the soft-read level pairs in the experiment data. Under the 3K Program Erase Cycles 228-hour data retention at 85°C channel condition, the proposed soft-read level pairs could provide an additional 73-error-bit tolerance in the 2K LDPC decoder.

## Implicit Partial Product-LDPC Codes Using Free-Ride Coding

- **Status**: ✅
- **Reason**: LDPC 행+대수 열 보호 product code 새 구성 + 4단계 디코딩 알고리즘, error rate 개선 (C/E, 바이너리)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9839082
- **Type**: conference
- **Published**: 16-20 May 
- **Authors**: Xiao Ma, Qianfan Wang, Suihua Cai +1
- **PDF**: https://ieeexplore.ieee.org/document/9839082
- **Abstract**: In this paper, we propose a new construction of product codes, where the whole information array is protected row-by-row by a low-density parity-check (LDPC) code while only a portion of the information array is protected column-by-column by an algebraic code. The most distinguished feature of the proposed product code is that, thanks to the free-ride coding technique, the additional column check bits are transmitted implicitly rather than explicitly. The constructed codes are referred to as implicit partial product-LDPC codes, which have the same rates as the row component LDPC codes. The decoding algorithm can be divided into four stages, including decoding of the free-ride codes, first-round decoding of the row codes, decoding of the column codes, and second-round decoding of the row codes by exploiting the messages associated with those successfully decoded columns. To predict the extremely low error rate of the doubly-protected (by both the row code and the column code) information bits, we derive an approximate upper bound. The simulation results show that, with a (3,6)-regular LDPC code of length 1024 as the component code, the proposed product code can lower the word error rate (WER) from 10−2 down to 10−6 at the SNR around 2 dB. The numerical results also show that the doubly-protected information bits are more reliable, which can have a bit error rate (BER) down to 10−15 at SNR around 2.6 dB as implied by the presented approximate upper bound.

## Protograph-Based Raptor-Like LDPC Codes with Edge Addition for URLLC

- **Status**: ✅
- **Reason**: PBRL LDPC protograph에 edge addition으로 error floor 낮추는 새 코드 설계 기법 (E, 바이너리)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9839059
- **Type**: conference
- **Published**: 16-20 May 
- **Authors**: Hyejin Ro, Hosung Park
- **PDF**: https://ieeexplore.ieee.org/document/9839059
- **Abstract**: For ultra-reliable low-latency communications (URLLC), low error floors are required for channel codes. In this paper, we propose a method of adding some edges to the protograph of the protograph-based raptor-like (PBRL) low-density parity-check (LDPC) codes. The added edges play a role of boosting up the reliability of weak variable nodes so that the code with edge addition can achieve low error floors. The edge addition is applied to an instance of 5G new radio (NR) LDPC code and it is shown that the edge addition lowers the error floor of the 5G NR LDPC code. Since the edge addition does not change the existing edge connections in the protograph, an adaptive use with/without edge addition have an effect of implementing two PBRL LDPC codes for enhanced mobile broadband (eMBB) and URLLC in an efficient way while keeping the system compatible with the original PBRL LDPC code.

## ProductAE: Toward Training Larger Channel Codes based on Neural Product Codes

- **Status**: ✅
- **Reason**: product code 기반 신경망 (encoder,decoder) 쌍으로 대형 부호 학습, 이식 가능한 신경망 디코더/구성 (C, 바이너리 product 구조)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9839215
- **Type**: conference
- **Published**: 16-20 May 
- **Authors**: Mohammad Vahid Jamali, Hamid Saber, Homayoon Hatami +1
- **PDF**: https://ieeexplore.ieee.org/document/9839215
- **Abstract**: There have been significant research activities in recent years to automate the design of channel encoders and decoders via deep learning. Due the dimensionality challenge in channel coding, it is prohibitively complex to design and train relatively large neural channel codes via deep learning techniques. Consequently, most of the results in the literature are limited to relatively short codes having less than 100 information bits. In this paper, we construct ProductAEs, a computationally efficient family of deep-learning driven (encoder, decoder) pairs, that aim at enabling the training of relatively large channel codes (both encoders and decoders) with a manageable training complexity. We build upon the ideas from classical product codes, and propose constructing large neural codes using smaller code components. More specifically, instead of directly training the encoder and decoder for a large neural code of dimension k and blocklength n, we provide a framework that requires training neural encoders and decoders for the code parameters (n1,k1) and (n2,k2) such that n1n2 = n and k1k2 = k. Our training results show significant gains, over all ranges of signal-to-noise ratio (SNR), for a code of parameters (225,100) and a moderate-length code of parameters (441,196), over polar codes under successive cancellation (SC) decoder. Moreover, our results demonstrate meaningful gains over Turbo Autoencoder (TurboAE) and state-of-the-art classical codes. This is the first work to design product autoencoders and a pioneering work on training large channel codes.

## Robust Performance Over Changing Intersymbol Interference Channels by Spatial Coupling

- **Status**: ✅
- **Reason**: 공간결합(SC) LDPC 부호 설계 + threshold saturation — 바이너리 LDPC 코드 설계 기법, 이식 가능(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9838435
- **Type**: conference
- **Published**: 16-20 May 
- **Authors**: Mgeni Makambi Mashauri, Alexandre Graell i Amat, Michael Lentmaier
- **PDF**: https://ieeexplore.ieee.org/document/9838435
- **Abstract**: We show that spatially coupled low-density parity-check (LDPC) codes yield robust performance over changing intersymbol interfere (ISI) channels with optimal and suboptimal detectors. We compare the performance with classical LDPC code design which involves optimizing the degree distribution for a given (known) channel. We demonstrate that these classical schemes, despite working very good when designed for a given channel, can perform poorly if the channel is exchanged. With spatially coupled LDPC codes, however, we get performances close to the symmetric information rates with just a single code, without the need to know the channel and adapt to it at the transmitter. We also investigate threshold saturation with the linear minimum mean square error (LMMSE) detector and show that with spatial coupling its performance can get remarkably close to that of an optimal detector for regular LDPC codes.

## Neural Normalized Min-Sum Message-Passing vs. Viterbi Decoding for the CCSDS Line Product Code

- **Status**: ✅
- **Reason**: Neural-Normalized Min-Sum(N-NMS) 신경망 디코더로 ML 근접, 저복잡도 — 이식 가능 디코더 알고리즘(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9838412
- **Type**: conference
- **Published**: 16-20 May 
- **Authors**: Jonathan Nguyen, Linfang Wang, Chester Hulse +5
- **PDF**: https://ieeexplore.ieee.org/document/9838412
- **Abstract**: The Consultative Committee for Space Data Systems (CCSDS) 141.11-O-1 Line Product Code (LPC) provides a rare opportunity to compare maximum-likelihood decoding and message passing. The LPC considered in this paper is intended to serve as the inner code in conjunction with a (255,239) Reed Solomon (RS) code whose symbols are bytes of data. This paper represents the 141.11-O-1 LPC as a bipartite graph and uses that graph to formulate both maximum likelihood (ML) and message passing algorithms. ML decoding must, of course, have the best frame error rate (FER) performance. However, a fixed point implementation of a Neural-Normalized MinSum (N-NMS) message passing decoder closely approaches ML performance with a significantly lower complexity.

## A High-speed Satellite Internet Physical Layer LDPC Decoder Design and FPGA-based Implementation

- **Status**: ✅
- **Reason**: 위성 LDPC 디코더 FPGA 구현, normalized min-sum 부분병렬 아키텍처 — 이식 가능 HW/디코더(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:9824734
- **Type**: conference
- **Published**: 13-15 May 
- **Authors**: Zhang Cong, Gao Feng
- **PDF**: https://ieeexplore.ieee.org/document/9824734
- **Abstract**: Under the boom of low-orbit satellite Internet constellation construction, an LDPC decoder design method is proposed for the outgoing physical layer of satellite Internet in order to carry out effective monitoring for typical satellite signals with high bandwidth and low time delay. The scheme uses a partially parallel architecture, where the node update step based on the normalized min-sum algorithm omits the resource consumption and compresses the number of clocks consumed by operations such as multi-level comparison of message values, which helps to improve the decoder throughput rate. Based on Virtex-7 series hardware platform, we realize the high rate decoding of long and short frame LDPC codes with different modulation methods in DVB-S2/S2X standard. At 204.8 MHz operating frequency, the decoder can reach 768 Mbps throughput. The decoder implemented in this paper is capable of meeting the rate and performance requirements of typical satellite systems for targeted signal monitoring.

## A Novel LDPC Construction Scheme for NAND Flash Memory

- **Status**: ✅
- **Reason**: NAND Flash용 QC-LDPC 구성(cycle-4 free, 대각 코딩, low error floor) — NAND 직접(A)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9802213
- **Type**: conference
- **Published**: 13-15 May 
- **Authors**: Hongyuan Li, Xiaobo Jiang, Zhenghong Yu +1
- **PDF**: https://ieeexplore.ieee.org/document/9802213
- **Abstract**: The storage capacity of NAND Flash memory has increased by scaling down to smaller cell size and using multi-level storage technology, but data reliability is degraded by severer retention errors. As adopting a very powerful error-correcting code gradually becomes a strategic demand for the endurance of nowadays NAND Flash memory, Low Density Parity Check (LDPC) codes are recently proposed due to their outstanding error correcting capability. Herein, a novel construction scheme of LDPC for NAND Flash memory is proposed. By using the proposed scheme, a high code-rate, high performance of Bit Error Rate (BER), low error floor Quasi Cyclic Low Density Parity Check (QC-LDPC) code is constructed to meet the needs of NAND Flash memory. In the proposed LDPC construction scheme, iterative cycle elimination technique is introduced to ensure that the checksum matrix is cycle-4 free and has minimal cycle-6, which is beneficial to achive high performance of BER and low error floor for high code-rate LDPC. A diagonal coding structure is used in the QC-LDPC code to achieve linear-time coding and meet the high throughput requirements of NAND Flash memory. Simulation results show that NAND Flash memory can be used more 1800 times for Program/Erase (P/E) cycle by using the proposed QC-LDPC codes compared with Euclidean-Geometry LDPC codes. The error floor of the constructed QC-LDPC codes is below 1$0^{-12}$.
