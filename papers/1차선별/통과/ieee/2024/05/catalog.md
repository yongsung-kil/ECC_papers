# IEEE Xplore — 2024-05 (1차선별 통과)


## List-Based Residual Belief-Propagation Decoding of LDPC Codes

- **Status**: ✅
- **Reason**: 리스트 기반 residual BP 디코더(L-RBP) — 스케줄링·decay 기법으로 수렴/복잡도 개선, 바이너리 LDPC 디코더 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10478612
- **Type**: journal
- **Published**: May 2024
- **Authors**: Ziqin Yan, Wu Guan, Liping Liang
- **PDF**: https://ieeexplore.ieee.org/document/10478612
- **Abstract**: This letter presents an enhanced list-based residual belief propagation (L-RBP) method for decoding low-density parity-check (LDPC) codes. L-RBP reduces computational complexity by scheduling a concise list of residuals. Moreover, the list is partially renewed to deter a small cluster of residuals from monopolizing renewal opportunities. Simultaneously, we also incorporate a decay mechanism to constrain the residuals retained within the list, further mitigating the greediness of the algorithm. The numerical results indicate that the L-RBP has an attractive convergence speed, error rate performance, and complexity of long-length and low-rate codes in the additive white Gaussian noise (AWGN) channel.

## Rate Compatible LDPC Neural Decoding Network: A Multi-Task Learning Approach

- **Status**: ✅
- **Reason**: Rate-compatible LDPC 신경망 디코더 멀티태스크 학습 - 이식 가능 신경망 디코더(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10365399
- **Type**: journal
- **Published**: May 2024
- **Authors**: Yukun Cheng, Wei Chen, Lun Li +1
- **PDF**: https://ieeexplore.ieee.org/document/10365399
- **Abstract**: Deep learning based decoding networks have shown significant improvement in decoding low density parity check (LDPC) codes, but the neural decoders are limited by rate-matching operations such as puncturing or extending, thus needing to train multiple decoders with different code rates for a variety of channel conditions. In this correspondence, we propose a Multi-Task Learning based rate-compatible LDPC decoding network, which utilizes the structure of raptor-like LDPC codes and can deal with multiple code rates. In the proposed network, different portions of parameters are activated to deal with distinct code rates, which leads to parameter sharing among tasks. Numerical experiments demonstrate the effectiveness of the proposed method. Training the specially designed network under multiple code rates makes the decoder compatible with multiple code rates without sacrificing frame error rate performance.

## A Low Valid Throughput Loss LDPC Codec Architecture With Variable Code Rate

- **Status**: ✅
- **Reason**: 가변 코드레이트 LDPC codec FPGA 아키텍처(Block Tag 인코딩, TDM) - 이식 가능 HW 아키텍처(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:10365522
- **Type**: journal
- **Published**: May 2024
- **Authors**: Jiaming Liu, Zhijian Hao, Lingxiu Zhao +4
- **PDF**: https://ieeexplore.ieee.org/document/10365522
- **Abstract**: Shortening is a rate-compatible technology that can improve LDPC error correction performance by modifying the code rate. However, as the code rate decreases, the throughput of valid data drops rapidly. Reducing the attenuation of valid throughput at low code rates is challenging. For this reason, this brief proposes two contributions. First, a Block Tag-based encoding method is presented with a non-fixed code length, which reduces the latency caused by fixed-length communications. Second, a novel Time Division Multiplexing (TDM) architecture is developed to improve valid throughput, reducing resource utilization compared to conventional multiplexers. Based on the above contributions, the codec is implemented on FPGA and the results show that the valid throughput loss is low in changing from high to low code rates.

## Belief Propagation Decoding for Short-Length Codes Based on Sparse Tanner Graph

- **Status**: ✅
- **Reason**: Tanner 그래프 sparsification으로 4-cycle 제거하는 새 코드설계 기법(G-LWPC), BP 디코딩 개선 — 바이너리 LDPC 이식 가능(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10436674
- **Type**: journal
- **Published**: May 2024
- **Authors**: Zongyao Li, Yifei Shen, Yuqing Ren +3
- **PDF**: https://ieeexplore.ieee.org/document/10436674
- **Abstract**: In this letter, we present a novel approach to improve belief propagation (BP) decoding performance by sparsifying the Tanner graph. Our proposed method first constructs a low-weight parity-check (LWPC) matrix with increased rows based on the original parity-check matrix. Then, all 4-cycles in the LWPC matrix are eliminated by adding auxiliary variable nodes and corresponding parity-check rows, resulting in the generalized LWPC (G-LWPC) matrix. Compared to the original matrix, the sparsity is greatly improved without altering the encoding constraints. Simulation results show that BP decoding based on the G-LWPC matrix is particularly effective for short code lengths. For a (128, 20) polar code with 24-bit cyclic redundancy check, our proposed G-LWPC matrix reduces the density from 17.4% to 1.3%, and with 10 iterations, BP decoding can achieve the performance of successive cancellation list decoding with a list size of 32.

## FPGA Verification of Generalized LDPC Convolutional Codes with Hamming Code

- **Status**: ✅
- **Reason**: 일반화 LDPC convolutional code(Hamming 체크노드)의 error floor를 FPGA로 검증 — 일반화 체크노드 코드설계+error floor 분석으로 이식 가능(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10728061
- **Type**: conference
- **Published**: 5-10 May 2
- **Authors**: Yinlong Shi, Kai Tao, Zitao Wei +1
- **PDF**: https://ieeexplore.ieee.org/document/10728061
- **Abstract**: Employing FPGA emulations, we investigate the performance of the hybrid check generalized LDPC convolutional code, and reveal that a small proportion of generalized check nodes can not effectively decrease the error floor down to 10−15.

## A Minimal-Resource LDPC Encoder and Decoder Design for Memory-Constrained Systems

- **Status**: ✅
- **Reason**: 최소자원 LDPC 인코더/디코더, QC-LDPC shortening/puncturing 변환 + HW — 이식 가능 코드설계/HW(D/E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10557000
- **Type**: conference
- **Published**: 20-22 May 
- **Authors**: Tomáš Páleník, Viktor Szitkey, Jakub Otruba +1
- **PDF**: https://ieeexplore.ieee.org/document/10557000
- **Abstract**: In this paper we present our LDPC encoder and decoder design focused on, but not limited to, the LDPC codes described in the recent CCSDS space data systems standard, known as the Blue Book. Two important code transformations: shortening and puncturing are described in detail with the goal of introducing a wider range of LDPC code parameters for Adaptive Coding and Modulation and minimizing the transceivers memory requirements. The effects of these transformations on the error performance of the system are evaluated using Monte-Carlo simulations and a provided along with the newly added LDPC code parameters set and memory-constraints analysis. Our custom free and open-source C implementation of both encoder and decoder is provided along with supporting MATLAB mini-toolkit for LDPC code lifting and transformations. This toolkit further includes also a full implementation and transformations of the QC-LDPC codes utilized in the Wi-Fi 6 IEEE 802.11ax standard.

## A 128 Gb/s LDPC Decoder Using Partial Syndrome-based Dynamic Decoding Scheme for Terahertz Wireless Multi-Media Networks

- **Status**: ✅
- **Reason**: 128 Gb/s LDPC decoder with novel partial syndrome-based dynamic decoding + VLSI arch (C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10558369
- **Type**: conference
- **Published**: 19-22 May 
- **Authors**: Tsung Han Wu, Ching Liang Yeh, Yi-Shan Huang +1
- **PDF**: https://ieeexplore.ieee.org/document/10558369
- **Abstract**: This paper presents a low power and high throughput multi-framed pipelined LDPC decoder architecture based on a novel partial syndrome-based dynamic decoding (PSDD) approach. The proposed PSDD can reduce clock cycle to allow the LDPC decoder to be implemented with better energy efficiency. We propose a high throughput sorting method and implement the LDPC decoder with a pipelined multi-frame VLSI architecture. The implementation results for the IEEE 802.15.3d Thz standard shows that the proposed design has a coding gain of 10−8 at the specified SNR of 18.1 dB with 16 QAM modulation. Furthermore, the proposed design can achieve a throughput rate of 128.5 Gbps with the 16nm FinFET CMOS process, respectively.

## An Efficient ADMM-Based Penalized Decoding Algorithm for Binary LDPC Code

- **Status**: ✅
- **Reason**: C: 바이너리 LDPC ADMM 페널티 디코딩에 segmented penalty function 신규 제안 + 가속 알고리즘 — 새 디코더 기여, 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10653194
- **Type**: conference
- **Published**: 10-12 May 
- **Authors**: Weipeng Duan, Jing Bai, Zedong An +1
- **PDF**: https://ieeexplore.ieee.org/document/10653194
- **Abstract**: LDPC decoding algorithm based on the alternating direction method of multipliers (ADMM) technique has increased much attentions because of its outstanding decoding performance. To enhancing performance advantages of ADMM decoding in practical application, a main challenge is to design an efficient penalty function and then customize an accelerating decoding algorithm. To address this issue, in this paper we propose an improved penalized decoding problem based on a segmented penalty function (SPF), and then develop an efficient ADMM algorithm via optimizing variable updating to solve this SPF-based decoding model. Experimental simulations demonstrate that the proposed algorithm effectively reduces the number of iterations while achieving better error-correction performance, when compared to the state-of-the-art ADMM-based decoding algorithms.

## Optimized Layered FAIDs of 5G LDPC Codes With RQNN

- **Status**: ✅
- **Reason**: C: QC-LDPC FAID LUT을 RQNN(양자화 신경망)으로 최적화 + 행가중치별 노드 분류 LUT — 새 디코더 기여, NAND 이식 유력
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10601679
- **Type**: conference
- **Published**: 10-12 May 
- **Authors**: Qiushi Xu, Yanchen Lyu, Yangming Li +1
- **PDF**: https://ieeexplore.ieee.org/document/10601679
- **Abstract**: In this paper, a recurrent quantized neural network with a layered structure is designed to optimize the look-up table (LUT) in the layered finite alphabet iterative decoders (FAIDs). By using straight-through estimators to soften the backward gradient propagation of some low-precision activation functions, the quantization thresholds and quantization levels in the LUTs are optimized as parameters in the network. Performance evaluations on decoding codewords encoded with quasi-cyclic low-density parity-check codes show significant advantages compared to the conventional optimized FAIDs using a generalized flooding structure network. The proposed approach achieves notable performance improvements without increasing the complexity of the decoding algorithm. We also classify the check nodes by row weights of the parity-check matrix, and train different LUTs for different categories of nodes for each iteration. This approach achieves further performance improvements in online decoding and significant complexity reduction compared to the exhaustive search method.

## Disjoint Difference Sets and QC-LDPC Codes With Girth 10

- **Status**: ✅
- **Reason**: 바이너리 QC-LDPC 부호 설계(E): disjoint difference set 기반 girth-10 exponent matrix 구성, 새 구성법 — NAND 코드설계 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10553056
- **Type**: conference
- **Published**: 1-2 May 20
- **Authors**: Farzane Amirzade, Mohammad-Reza Sadeghi, Daniel Panario
- **PDF**: https://ieeexplore.ieee.org/document/10553056
- **Abstract**: A method to obtain an exponent matrix of a QCLDPC code with column weight 4 appeared recently in which the entries of the matrix belong to the sets of a (v,k,2) disjoint difference set (DDS). It was also shown that the girth of the Tanner graph in these codes is at least 8. In this paper, we prove the existence of an 8-cycle in their Tanner graph which shows that the girth of these codes is exactly 8.The merits of a QC-LDPC code from a DDS motivated us to study these combinatorial designs. However, the disjoint difference sets existing in the literature are limited to small values of the parameters k and t. We present a novel approach to obtain a (v,k,t)-DDS with 3 ≤ t ≤ 5 and different values of k. Our method is based on a new relation between QC-LDPC codes with girth 10 and disjoint difference sets.
