# IEEE Xplore — 2013-03 (1차선별 통과)


## Two Informed Dynamic Scheduling Strategies for Iterative LDPC Decoders

- **Status**: ✅
- **Reason**: RBP IDS 신규 스케줄(Q-RBP, SVNF-RBP)로 BP 수렴/성능 개선 — 부호 비의존 디코더 기법(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6427624
- **Type**: journal
- **Published**: March 2013
- **Authors**: Huang-Chang Lee, Yeong-Luh Ueng, Shan-Ming Yeh +1
- **PDF**: https://ieeexplore.ieee.org/document/6427624
- **Abstract**: When residual belief-propagation (RBP), which is a kind of informed dynamic scheduling (IDS), is applied to low-density parity-check (LDPC) codes, the convergence speed in error-rate performance can be significantly improved. However, the RBP decoders presented in previous literature suffer from poor convergence error-rate performance due to the two phenomena explored in this paper. The first is the greedy-group phenomenon, which results in a small part of the decoding graph occupying most of the decoding resources. By limiting the number of updates for each edge message in the decoding graph, the proposed Quota-based RBP (Q-RBP) schedule can reduce the probability of greedy groups forming. The other phenomenon is the silent-variable-nodes issue, which is a condition where some variable nodes have no chance of contributing their intrinsic messages to the decoding process. As a result, we propose the Silent-Variable-Node-Free RBP (SVNF-RBP) schedule, which can force all variable nodes to contribute their intrinsic messages to the decoding process equally. Both the Q-RBP and the SVNF-RBP provide appealing convergence speed and convergence error-rate performance compared to previous IDS decoders for both dedicated and punctured LDPC codes.

## Multi-Layer Iterative LDPC Decoding for Broadband Wireless Access Networks: A Recursive Shortening Algorithm

- **Status**: ✅
- **Reason**: 결정비트 활용 다층 반복 디코딩+재귀적 패리티행렬 단축 알고리즘, 바이너리 LDPC BP 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6416890
- **Type**: journal
- **Published**: March 2013
- **Authors**: Bo Rong, Yiyan Wu, Gilles Gagnon
- **PDF**: https://ieeexplore.ieee.org/document/6416890
- **Abstract**: This paper presents a novel multi-layer iterative decoding scheme using deterministic bits to lower the decoding threshold of LDPC codes in wireless multimedia communication systems. These deterministic bits serve as known information in the LDPC decoding process to reduce the redundancy during data transmission. Unlike the existing work, our proposed scheme addresses the controllable deterministic bits, such as MPEG null packets, rather than the widely investigated protocol headers. In particular, our multi-layer scheme integrates deterministic bit identification into LDPC decoding process. This integration is able to make significant performance improvement if adequate deterministic bits are discovered. We find that the length of deterministic bits may vary from time to time, and the exploring of deterministic bits is associated to a series of shortened parity matrices during the decoding iterations. Accordingly, we develop a recursive LDPC shortening algorithm to match the dynamic length and facilitate the iterative identification of deterministic bits. Simulation results show that our proposed scheme can achieve considerable gain in today's most popular broadband wireless access networks such as WiMAX.

## An Efficient Multi-Standard LDPC Decoder Design Using Hardware-Friendly Shuffled Decoding

- **Status**: ✅
- **Reason**: 셔플드 디코딩 멀티표준 LDPC 디코더 HW: offset min-sum 양자화비트 축소+메모리 최적화, VLSI 이식 가능(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6459554
- **Type**: journal
- **Published**: March 2013
- **Authors**: Yeong-Luh Ueng, Bo-Jhang Yang, Chung-Jay Yang +2
- **PDF**: https://ieeexplore.ieee.org/document/6459554
- **Abstract**: This paper presents an efficient multi-standard low-density parity-check (LDPC) decoder architecture using a shuffled decoding algorithm, where variable nodes are divided into several groups. In order to provide sufficient memory bandwidth without the need for using registers, a FIFO-based check-mode memory, which dominates the decoder area, is used. Since two compensation factors, rather than a single factor, are dynamically used in the offset Min-Sum algorithm, the number of quantization bits, and, hence, the memory size, can be reduced without degradation in error performance. In order to further reduce the memory size, artificial minimum values, which do not need to be stored in memory, are used. We also propose an algorithm that can be used to partition variable nodes such that the hardware cost can be minimized. Using the proposed techniques, a multi-standard decoder that supports the LDPC codes specified in the ITU G.hn, IEEE 802.11n, and IEEE 802.16e standards was designed and implemented using a 90-nm CMOS process. This decoder supports 133 codes, occupies an area of 5.529 mm2 , and achieves an information throughput of 1.956 Gbps.

## Iterative Coding for Network Coding

- **Status**: ✅
- **Reason**: Error-correction via random sparse graphs with low-complexity decoder optimized over degree profile; sparse-graph code construction + decoding portable to binary LDPC design (E/C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6397614
- **Type**: journal
- **Published**: March 2013
- **Authors**: Andrea Montanari, Rüdiger L. Urbanke
- **PDF**: https://ieeexplore.ieee.org/document/6397614
- **Abstract**: We consider communication over a noisy network under randomized linear network coding. Possible error mechanisms include node- or link-failures, Byzantine behavior of nodes, or an overestimate of the network min-cut. Building on the work of Kötter and Kschischang, we introduce a systematic oblivious random channel model. Within this model, codewords contain a header (this is the systematic part). The header effectively records the coefficients of the linear encoding functions, thus simplifying the decoding task. Under this constraint, errors are modeled as random low-rank perturbations of the transmitted codeword. We compute the capacity of this channel and we define an error-correction scheme based on random sparse graphs and a low-complexity decoding algorithm. By optimizing over the code degree profile, we show that this construction achieves the channel capacity in complexity which is jointly quadratic in the number of coded information bits and sublogarithmic in the error probability.

## Algebraic Design and Implementation of Protograph Codes using Non-Commuting Permutation Matrices

- **Status**: ✅
- **Reason**: 비가환 순열행렬 기반 프로토그래프/QC-LDPC 신규 구성+엔코더/디코더 구현 — 바이너리 코드설계 기법(E/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6427619
- **Type**: journal
- **Published**: March 2013
- **Authors**: Christine A. Kelley
- **PDF**: https://ieeexplore.ieee.org/document/6427619
- **Abstract**: Random lifts of graphs, or equivalently, random permutation matrices, have been used to construct good families of codes known as protograph codes. An algebraic analog of this approach was recently presented using voltage graphs, and it was shown that many existing algebraic constructions of graph-based codes that use commuting permutation matrices may be seen as special cases of voltage graph codes. Voltage graphs are graphs that have an element of a finite group assigned to each edge, and the assignment determines a specific lift of the graph. In this paper we discuss how assignments of permutation group elements to the edges of a base graph affect the properties of the lifted graph and corresponding codes, and present a construction method of LDPC code ensembles based on non-commuting permutation matrices. We also show encoder and decoder implementations for these codes.

## Short LDPC codes for NB-PLC channel with a differential evolution construction method

- **Status**: ✅
- **Reason**: 단블록 바이너리 LDPC 차수분포를 differential evolution으로 최적화하는 코드설계(E) 기법, 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6525856
- **Type**: conference
- **Published**: 24-27 Marc
- **Authors**: Nikoleta Andreadou, Andrea M. Tonello
- **PDF**: https://ieeexplore.ieee.org/document/6525856
- **Abstract**: In this paper, we study the performance of Low Density Parity Check (LDPC) codes and we introduce an optimized version of these codes when applied on the short data blocks of a narrowband (NB) power line communications (PLC) system. We compare their performance with the one obtained when the G3 standard coding scheme is applied on the system, namely the scheme that concatenated convolutional with Reed-Solomon codes. Multipath propagation together with two noise scenarios are considered: background AWGN noise with and without the presence of impulsive noise. The results indicate that under the considered channel and noise conditions the introduced optimized LDPC codes can operate better than the concatenated scheme used in the G3 standard. The optimized irregular LDPC codes are obtained from the well-established method of differential evolution for finding a degree distribution pair that improves the performance. The evaluation of each candidate code, is proposed to be carried out with a method that takes into account the actual channel and noise conditions. The equivalent optimized degree distribution pairs are presented.

## An efficient LDPC encoder based on block-row-cycle structure for CMMB

- **Status**: ✅
- **Reason**: CMMB용 block-row-cycle 구조 LDPC 인코더로 HW 메모리 절감—구조 활용 인코더 HW 기법 이식 가능(D), 애매해 살림
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:6747811
- **Type**: conference
- **Published**: 23-25 Marc
- **Authors**: Lei Liu, Peng Zhang, Ziliang Lin
- **PDF**: https://ieeexplore.ieee.org/document/6747811
- **Abstract**: Concerning the high encoding complexity of LDPC codes, an efficient encoder based on block-row-cycle structure for CMMB is proposed, which is able to take full advantage of the characteristics of the sparse parity-check matrix, such as cyclicity and equality of row weight. Experimental results show that the proposed encoder can reduce dramatically the memory requirements in hardware implementation, and improve the encoding rate at the same time.

## Linear LLR approximation for LDPC decoding using a Gaussian approximation

- **Status**: ✅
- **Reason**: 페이딩 채널 CSI 없이 LLR PDF의 Gaussian 근사로 LLR 계산 복잡도 감소—LLR 양자화/근사 기법은 NAND 디코더에 이식 가능(A/C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6747759
- **Type**: conference
- **Published**: 23-25 Marc
- **Authors**: Xinyi Zhong, Youyun Xu, Kui Xu
- **PDF**: https://ieeexplore.ieee.org/document/6747759
- **Abstract**: In fading channels, the computation of Loglikelihood ratio (LLR) without channel state information (CSI) is complicated. The maximum capacity linear approximation (MCLA) has been proposed to reduce the computational complexity of LLR. However, the computation of LLR' probability density function (PDF) is still complicated due to numerical integrations. To overcome this shortage, we propose a simple Gaussian approximation to PDF of LLR. Using our proposed method, the computational complexity is significantly reduced and the BER performance is still very close to that of the MCLA in uncorrelated Rayleigh fading channels.

## Design of improved LDPC encoder for CMMB based on SIMD architecture

- **Status**: ✅
- **Reason**: LU분해 기반 SIMD 병렬 LDPC 인코더, 파이프라인/Ping-Pong 버퍼로 throughput 개선—이식 가능 HW 아키텍처(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:6747774
- **Type**: conference
- **Published**: 23-25 Marc
- **Authors**: Hang Yin, Weitao Du, Nanhao Zhu
- **PDF**: https://ieeexplore.ieee.org/document/6747774
- **Abstract**: This paper designs and implements a novel parallel LDPC encoder. It based on LU decomposition, according to the inherent characteristics of LDPC Parity-Check Matrix in CMMB. It is applied to design CMMB baseband exciter, which can support 2 different code rates (1/2 and 3/4). The SIMD parallel architecture is proposed to solve the encoding delay caused by iteration of LU algorithm, full pipeline and multistage Ping-Pong buffer structure are also used to improve throughput in high-speed encoding. It meets the requirements both in real-time performance and resource utilization. Furthermore, this method is generic and can be adapted easily for other LDPC codes; thus, it has a significant practical value.

## A scaling method for stochastic LDPC decoding over the binary symmetric channel

- **Status**: ✅
- **Reason**: BSC용 stochastic LDPC 디코딩 scaling 기법 — error floor 개선, HW 라우팅혼잡 완화로 이식 가능(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6552331
- **Type**: conference
- **Published**: 20-22 Marc
- **Authors**: Kuo-Lun Huang, Vincent Gaudet, Masoud Salehi
- **PDF**: https://ieeexplore.ieee.org/document/6552331
- **Abstract**: Stochastic decoding is a decoding algorithm for Low-Density Parity-Check (LDPC) codes that leads to lowered routing congestion. Randomization is crucial for generating stochastic bits in stochastic decoders. In this paper, we propose a scaling method for stochastic LDPC decoding over the binary symmetric channel model that is independent of the channel error probability, and thus reduces the complexity in the conversion of received messages into stochastic streams. The scaling method not only improves the error rate performance, but lowers the error floor for stochastic decoding.
