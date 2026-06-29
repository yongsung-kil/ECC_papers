# IEEE Xplore — 2013-03


## Check Node Reliability-Based Scheduling for BP Decoding of Non-Binary LDPC Codes

- **Status**: ❌
- **Reason**: 비이진(NB-LDPC) BP 스케줄링 — 비이진 LDPC는 제외 대상
- **ID**: ieee:6415954
- **Type**: journal
- **Published**: March 2013
- **Authors**: Guojun Han, Yong Liang Guan, Xinmei Huang
- **PDF**: https://ieeexplore.ieee.org/document/6415954
- **Abstract**: Scheduling strategy is considered an important aspect of belief-propagation (BP) decoding of low-density parity-check (LDPC) codes because it affects the decoder's convergence rate, decoding complexity and error-correction performance. In this paper, we propose two new scheduling strategies for the BP decoding of non-binary LDPC (NB-LDPC) codes. Both the strategies are devised based on the concept of check node reliability and employ a heuristically defined threshold which can adapt to the communication channel variations. As the scheduling strategies only update a subset of the check nodes in each iteration, they result in reduced iteration cost. Furthermore, since the BP performs suboptimally for finite-length LDPC codes, especially for short-length LDPC codes, by enhancing the message propagation over the Tanner Graphs of short-length NB-LDPC codes, the new scheduling strategies can even improve the error-correction performances of BP decoding. Simulation results demonstrate that the new scheduling strategies provide good performance/complexity tradeoffs.

## Two Informed Dynamic Scheduling Strategies for Iterative LDPC Decoders

- **Status**: ✅
- **Reason**: RBP IDS 신규 스케줄(Q-RBP, SVNF-RBP)로 BP 수렴/성능 개선 — 부호 비의존 디코더 기법(C)
- **ID**: ieee:6427624
- **Type**: journal
- **Published**: March 2013
- **Authors**: Huang-Chang Lee, Yeong-Luh Ueng, Shan-Ming Yeh +1
- **PDF**: https://ieeexplore.ieee.org/document/6427624
- **Abstract**: When residual belief-propagation (RBP), which is a kind of informed dynamic scheduling (IDS), is applied to low-density parity-check (LDPC) codes, the convergence speed in error-rate performance can be significantly improved. However, the RBP decoders presented in previous literature suffer from poor convergence error-rate performance due to the two phenomena explored in this paper. The first is the greedy-group phenomenon, which results in a small part of the decoding graph occupying most of the decoding resources. By limiting the number of updates for each edge message in the decoding graph, the proposed Quota-based RBP (Q-RBP) schedule can reduce the probability of greedy groups forming. The other phenomenon is the silent-variable-nodes issue, which is a condition where some variable nodes have no chance of contributing their intrinsic messages to the decoding process. As a result, we propose the Silent-Variable-Node-Free RBP (SVNF-RBP) schedule, which can force all variable nodes to contribute their intrinsic messages to the decoding process equally. Both the Q-RBP and the SVNF-RBP provide appealing convergence speed and convergence error-rate performance compared to previous IDS decoders for both dedicated and punctured LDPC codes.

## Stochastic Decoding of LDPC Codes over GF(q)

- **Status**: ❌
- **Reason**: GF(q) 비이진 LDPC 확률적 디코딩 — 비이진 LDPC는 제외 대상
- **ID**: ieee:6451069
- **Type**: journal
- **Published**: March 2013
- **Authors**: Gabi Sarkis, Saied Hemati, Shie Mannor +1
- **PDF**: https://ieeexplore.ieee.org/document/6451069
- **Abstract**: Despite the outstanding performance of non-binary low-density parity-check (LDPC) codes over many communication channels, they are not in widespread use yet. This is due to the high implementation complexity of their decoding algorithms, even those that compromise performance for the sake of simplicity. In this paper, we present three algorithms based on stochastic computation to reduce the decoding complexity. The first is a purely stochastic algorithm with error-correcting performance matching that of the sum-product algorithm (SPA) for LDPC codes over Galois fields with low order and a small variable node degree. We also present a modified version which reduces the number of decoding iterations required while remaining purely stochastic and having a low per-iteration complexity. The second algorithm, relaxed half-stochastic (RHS) decoding, combines elements of the SPA and the stochastic decoder and uses successive relaxation to match the error-correcting performance of the SPA. Furthermore, it uses fewer iterations than the purely stochastic algorithm and does not have limitations on the field order and variable node degree of the codes it can decode. The third algorithm, NoX, is a fully stochastic specialization of RHS for codes with a variable node degree 2 that offers similar performance, but at a significantly lower computational complexity. We study the performance and complexity of the algorithms; noting that all have lower per-iteration complexity than SPA and that RHS can have comparable average per-codeword computational complexity, and NoX a lower one.

## A Newly Designed Quarter-Rate QC-LDPC Code for the Cloud Transmission System

- **Status**: ❌
- **Reason**: 클라우드 전송용 1/4율 QC-LDPC 표준 구성, 신규 기법 없는 단순 코드 최적화
- **ID**: ieee:6459544
- **Type**: journal
- **Published**: March 2013
- **Authors**: Sung Ik Park, Heung Mook Kim, Yiyan Wu +1
- **PDF**: https://ieeexplore.ieee.org/document/6459544
- **Abstract**: In this brief, we propose a newly designed quarter-rate quasi-cyclic low density parity check (LDPC) code for the cloud transmission system. The cloud transmission system requires a near Shannon limit low-rate coding for the next generation terrestrial digital television system. The proposed LDPC code is optimized for R=1/4. At the code length of 64 K, it is only 0.6 dB away from Shannon limit.

## Multi-Layer Iterative LDPC Decoding for Broadband Wireless Access Networks: A Recursive Shortening Algorithm

- **Status**: ✅
- **Reason**: 결정비트 활용 다층 반복 디코딩+재귀적 패리티행렬 단축 알고리즘, 바이너리 LDPC BP 이식 가능(C)
- **ID**: ieee:6416890
- **Type**: journal
- **Published**: March 2013
- **Authors**: Bo Rong, Yiyan Wu, Gilles Gagnon
- **PDF**: https://ieeexplore.ieee.org/document/6416890
- **Abstract**: This paper presents a novel multi-layer iterative decoding scheme using deterministic bits to lower the decoding threshold of LDPC codes in wireless multimedia communication systems. These deterministic bits serve as known information in the LDPC decoding process to reduce the redundancy during data transmission. Unlike the existing work, our proposed scheme addresses the controllable deterministic bits, such as MPEG null packets, rather than the widely investigated protocol headers. In particular, our multi-layer scheme integrates deterministic bit identification into LDPC decoding process. This integration is able to make significant performance improvement if adequate deterministic bits are discovered. We find that the length of deterministic bits may vary from time to time, and the exploring of deterministic bits is associated to a series of shortened parity matrices during the decoding iterations. Accordingly, we develop a recursive LDPC shortening algorithm to match the dynamic length and facilitate the iterative identification of deterministic bits. Simulation results show that our proposed scheme can achieve considerable gain in today's most popular broadband wireless access networks such as WiMAX.

## An Efficient Multi-Standard LDPC Decoder Design Using Hardware-Friendly Shuffled Decoding

- **Status**: ✅
- **Reason**: 셔플드 디코딩 멀티표준 LDPC 디코더 HW: offset min-sum 양자화비트 축소+메모리 최적화, VLSI 이식 가능(C/D)
- **ID**: ieee:6459554
- **Type**: journal
- **Published**: March 2013
- **Authors**: Yeong-Luh Ueng, Bo-Jhang Yang, Chung-Jay Yang +2
- **PDF**: https://ieeexplore.ieee.org/document/6459554
- **Abstract**: This paper presents an efficient multi-standard low-density parity-check (LDPC) decoder architecture using a shuffled decoding algorithm, where variable nodes are divided into several groups. In order to provide sufficient memory bandwidth without the need for using registers, a FIFO-based check-mode memory, which dominates the decoder area, is used. Since two compensation factors, rather than a single factor, are dynamically used in the offset Min-Sum algorithm, the number of quantization bits, and, hence, the memory size, can be reduced without degradation in error performance. In order to further reduce the memory size, artificial minimum values, which do not need to be stored in memory, are used. We also propose an algorithm that can be used to partition variable nodes such that the hardware cost can be minimized. Using the proposed techniques, a multi-standard decoder that supports the LDPC codes specified in the ITU G.hn, IEEE 802.11n, and IEEE 802.16e standards was designed and implemented using a 90-nm CMOS process. This decoder supports 133 codes, occupies an area of 5.529 mm2 , and achieves an information throughput of 1.956 Gbps.

## Design of Irregular Repeat-Accumulate Coded Physical-Layer Network Coding for Gaussian Two-Way Relay Channels

- **Status**: ❌
- **Reason**: IRA 부호의 물리계층 네트워크코딩(PNC) 설계 — 양방향 중계 응용 특화, NAND ECC로 떼어낼 기법 없음
- **ID**: ieee:6450163
- **Type**: journal
- **Published**: March 2013
- **Authors**: Tao Huang, Tao Yang, Jinhong Yuan +1
- **PDF**: https://ieeexplore.ieee.org/document/6450163
- **Abstract**: This paper addresses the design of irregular repeat accumulate (IRA) codes for coded physical-layer network coding (PNC) for the binary-input Gaussian two-way relay channel, assuming perfect synchronization and equal received power at the relay. The design is based on a nontrivial extension of EXIT-chart based design. Specifically, we analyze the components of the IRA-PNC scheme and propose an approach to model the soft information exchanged between these components. Then, we develop upper and lower bounds on the extrinsic information transfer functions to characterize the iterative process of computing the network-coded information. Based on that, we construct optimized IRA codes to minimize the computation error at the relay. The optimized IRA-PNC has considerable performance improvement over the existing regular RA coded PNC. For a rate 3/4 code, as an example, we observed improvements of 2.6 dB, and the optimized IRA-PNC scheme is only about 1.7 dB away from the capacity upper bound of the Gaussian two-way relay channel.

## The Bethe Permanent of a Nonnegative Matrix

- **Status**: ❌
- **Reason**: Theoretical Bethe permanent approximation via sum-product; pure theory, no portable decoder/HW/code-construction for NAND LDPC
- **ID**: ieee:6352911
- **Type**: journal
- **Published**: March 2013
- **Authors**: Pascal O. Vontobel
- **PDF**: https://ieeexplore.ieee.org/document/6352911
- **Abstract**: It has recently been observed that the permanent of a nonnegative square matrix, i.e., of a square matrix containing only nonnegative real entries, can very well be approximated by solving a certain Bethe free energy function minimization problem with the help of the sum–product algorithm. We call the resulting approximation of the permanent the Bethe permanent. In this paper, we give reasons why this approach to approximating the permanent works well. Namely, we show that the Bethe free energy function is convex and that the sum–product algorithm finds its minimum efficiently. We then discuss the fact that the permanent is lower bounded by the Bethe permanent, and we comment on potential upper bounds on the permanent based on the Bethe permanent. We also present a combinatorial characterization of the Bethe permanent in terms of permanents of so-called lifted versions of the matrix under consideration. Moreover, we comment on possibilities to modify the Bethe permanent so that it approximates the permanent even better, and we conclude the paper with some observations and conjectures about permanent-based pseudocodewords and permanent-based kernels.

## EXIT-Chart-Matching-Aided Near-Capacity Coded Modulation Design and a BICM-ID Design Example for Both Gaussian and Rayleigh Channels

- **Status**: ❌
- **Reason**: BICM-ID APSK constellation design and bit-mapping for wireless; modulation/coded-modulation design, no portable LDPC ECC technique
- **ID**: ieee:6359874
- **Type**: journal
- **Published**: March 2013
- **Authors**: Qiuliang Xie, Zhixing Yang, Jian Song +1
- **PDF**: https://ieeexplore.ieee.org/document/6359874
- **Abstract**: Bit-interleaved coded modulation with iterative decoding (BICM-ID) is investigated, wherein a novel method of designing amplitude phase-shift keying (APSK) constellations is proposed, which is capable of outperforming both traditional quadrature amplitude modulation (QAM) and nonuniformly spaced QAM (NU-QAM). It is shown that the channel capacity can be approached by the proposed $M$-APSK constellation as $M$ tends to infinity. Additionally, a new algorithm is introduced for finding the best bit-to-symbol mapping. Furthermore, when signal space diversity is also employed, our extrinsic information transfer (EXIT) chart analysis and Monte Carlo simulations demonstrate that the proposed BICM-ID schemes exhibit a near-Shannon-capacity performance for transmission over both additive white Gaussian noise (AWGN) and Rayleigh fading channels. For a block length of 64 800 bits, the bit-error-rate (BER) curve of the proposed BICM-ID 16/64-APSK scheme is only about 0.8 and 1.0 dB away from the Gaussian-input Shannon limit over AWGN and Rayleigh fading channels, respectively, at the BER of $\hbox{10}^{-5}$  and for a code rate of 1/2.

## Approximate Bayesian Probabilistic-Data-Association-Aided Iterative Detection for MIMO Systems Using Arbitrary $M$-ary Modulation

- **Status**: ❌
- **Reason**: PDA-aided iterative detection LLR for turbo-coded MIMO; MIMO detection/turbo, not LDPC ECC, no portable BP technique
- **ID**: ieee:6353994
- **Type**: journal
- **Published**: March 2013
- **Authors**: Shaoshi Yang, Li Wang, Tiejun Lv +1
- **PDF**: https://ieeexplore.ieee.org/document/6353994
- **Abstract**: In this paper, the issue of designing an iterative-detection-and-decoding (IDD)-aided receiver, relying on the low-complexity probabilistic data association (PDA) method, is addressed for turbo-coded multiple-input-multiple-output (MIMO) systems using general M -ary modulations. We demonstrate that the classic candidate-search-aided bit-based extrinsic log-likelihood ratio (LLR) calculation method is not applicable to the family of PDA-based detectors. Additionally, we reveal that, in contrast to the interpretation in the existing literature, the output symbol probabilities of existing PDA algorithms are not the true a posteriori probabilities (APPs) but, rather, the normalized symbol likelihoods. Therefore, the classic relationship, where the extrinsic LLRs are given by subtracting the a priori LLRs from the a posteriori LLRs, does not hold for the existing PDA-based detectors. Motivated by these revelations, we conceive a new approximate Bayesian-theorem-based logarithmic-domain PDA (AB-Log-PDA) method and unveil the technique of calculating bit-based extrinsic LLRs for the AB-Log-PDA, which facilitates the employment of the AB-Log-PDA in a simplified IDD receiver structure. Additionally, we demonstrate that we may dispense with inner iterations within the AB-Log-PDA in the context of IDD receivers. Our complexity analysis and numerical results recorded for Nakagami-m fading channels demonstrate that the proposed AB-Log-PDA-based IDD scheme is capable of achieving a performance comparable with that of the optimal maximum a posteriori (MAP)-detector-based IDD receiver, while imposing significantly lower computational complexity in the scenarios considered.

## Iterative Coding for Network Coding

- **Status**: ✅
- **Reason**: Error-correction via random sparse graphs with low-complexity decoder optimized over degree profile; sparse-graph code construction + decoding portable to binary LDPC design (E/C)
- **ID**: ieee:6397614
- **Type**: journal
- **Published**: March 2013
- **Authors**: Andrea Montanari, Rüdiger L. Urbanke
- **PDF**: https://ieeexplore.ieee.org/document/6397614
- **Abstract**: We consider communication over a noisy network under randomized linear network coding. Possible error mechanisms include node- or link-failures, Byzantine behavior of nodes, or an overestimate of the network min-cut. Building on the work of Kötter and Kschischang, we introduce a systematic oblivious random channel model. Within this model, codewords contain a header (this is the systematic part). The header effectively records the coefficients of the linear encoding functions, thus simplifying the decoding task. Under this constraint, errors are modeled as random low-rank perturbations of the transmitted codeword. We compute the capacity of this channel and we define an error-correction scheme based on random sparse graphs and a low-complexity decoding algorithm. By optimizing over the code degree profile, we show that this construction achieves the channel capacity in complexity which is jointly quadratic in the number of coded information bits and sublogarithmic in the error probability.

## Practical Methods for Wireless Network Coding With Multiple Unicast Transmissions

- **Status**: ❌
- **Reason**: 무선 네트워크 코딩 응용; SP 검출기는 네트워크 디코딩 특화, NAND LDPC ECC로 떼어낼 기법 없음
- **ID**: ieee:6415950
- **Type**: journal
- **Published**: March 2013
- **Authors**: Tugcan Aktas, A. Ozgur Yilmaz, Emre Aktas
- **PDF**: https://ieeexplore.ieee.org/document/6415950
- **Abstract**: We propose a simple yet effective wireless network coding and decoding technique for a multiple unicast network. It utilizes spatial diversity through cooperation between nodes which carry out distributed encoding operations dictated by generator matrices of linear block codes. In order to exemplify the technique, we make use of greedy codes over the binary field and show that the arbitrary diversity orders can be flexibly assigned to nodes. Furthermore, we present the optimal detection rule for the given model that accounts for intermediate node errors and suggest a low-complexity network decoder using the sum-product (SP) algorithm. The proposed SP detector exhibits near optimal performance. We also show asymptotic superiority of network coding over a method that utilizes the wireless channel in a repetitive manner without network coding (NC) and give related rate-diversity trade-off curves. Finally, we extend the given encoding method through selective encoding in order to obtain extra coding gains.

## Algebraic Design and Implementation of Protograph Codes using Non-Commuting Permutation Matrices

- **Status**: ✅
- **Reason**: 비가환 순열행렬 기반 프로토그래프/QC-LDPC 신규 구성+엔코더/디코더 구현 — 바이너리 코드설계 기법(E/D)
- **ID**: ieee:6427619
- **Type**: journal
- **Published**: March 2013
- **Authors**: Christine A. Kelley
- **PDF**: https://ieeexplore.ieee.org/document/6427619
- **Abstract**: Random lifts of graphs, or equivalently, random permutation matrices, have been used to construct good families of codes known as protograph codes. An algebraic analog of this approach was recently presented using voltage graphs, and it was shown that many existing algebraic constructions of graph-based codes that use commuting permutation matrices may be seen as special cases of voltage graph codes. Voltage graphs are graphs that have an element of a finite group assigned to each edge, and the assignment determines a specific lift of the graph. In this paper we discuss how assignments of permutation group elements to the edges of a base graph affect the properties of the lifted graph and corresponding codes, and present a construction method of LDPC code ensembles based on non-commuting permutation matrices. We also show encoder and decoder implementations for these codes.

## On Decoding of the (89, 45, 17) Quadratic Residue Code

- **Status**: ❌
- **Reason**: QR(이차잉여) 블록부호 대수/Chase/LP 디코딩 — 비-LDPC 부호, BP 비의존 기법으로 이식성 없음
- **ID**: ieee:6403878
- **Type**: journal
- **Published**: March 2013
- **Authors**: Lin Wang, Yong Li, Trieu-Kien Truong +1
- **PDF**: https://ieeexplore.ieee.org/document/6403878
- **Abstract**: In this paper, Three decoding methods of the (89, 45, 17) binary quadratic residue (QR) code to be presented are hard, soft and linear programming decoding algorithms. Firstly, a new hybrid algebraic decoding algorithm for the (89, 45, 17) QR code is proposed. It uses the Laplace formula to obtain the primary unknown syndromes, as done in Lin et al.'s algorithm when the number of errors v is less than or equal to 5, whereas Gaussian elimination is adopted to compute the unknown syndromes when v ≥ 6. Secondly, an appropriate modification to the algorithm developed by Chase is also given in this paper. Therefore, combining the proposed algebraic decoding algorithm with the modified Chase-II algorithm, called a new soft-decision decoding algorithm, becomes a complete soft decoding of QR codes. Thirdly, in order to further improve the error-correcting performance of the code, linear programming (LP) is utilized to decode the (89, 45, 17) QR code. Simulation results show that the proposed algebraic decoding algorithm reduces the decoding time when compared with Lin et al.'s hard decoding algorithm, and thus significantly reduces the decoding complexity of soft decoding while maintaining the same bit error rate (BER) performance. Moreover, the LP-based decoding improves the error-rate performance almost without increasing the decoding complexity, when compared with the new soft-decision decoding algorithm. It provides a coding gain of 0.2 dB at BER = 2 × 10-6.

## Belief Propagation for Large-Variable-Domain Optimization on Factor Graphs: An Application to Decentralized Weather-Radar Coordination

- **Status**: ❌
- **Reason**: Max-sum BP for decentralized weather-radar resource allocation (factor-graph optimization), not channel coding; no ECC technique
- **ID**: ieee:6301748
- **Type**: journal
- **Published**: March 2013
- **Authors**: Erik P. Vargo, Ellen J. Bass, Randy Cogill
- **PDF**: https://ieeexplore.ieee.org/document/6301748
- **Abstract**: Due to the NP-hardness of factor-graph optimization, obtaining exact solutions to problems with a large variable domain is generally not possible. Max-sum (max-product) belief propagation (BP) is a distributed message-passing heuristic that has found popularity due to its ability to generate approximate solutions to such factor-graph problems in a distributed fashion. Because max-sum BP generally provides no indication of solution quality, researchers have sought alternative algorithms to generate approximate (and, in some cases, exact) solutions, the most successful of which operate on a relaxation of the integer programming form of an equivalent maximum a posteriori estimation problem. While such linear-programming-based algorithms perform well in empirical studies, there are limits to the variable domain size for which they are tractable. Via a case study in weather-radar coordination, we demonstrate that the decentralized max-sum BP algorithm remains useful for generating quality solutions to problems with a large variable domain. Our custom simulation tool facilitates a comparison of the performance of algorithms with respect to adaptive weather-radar scanning resource allocation across three weather scenarios. In addition to no adaptive scanning, the algorithms include four max-sum-BP-based algorithms: decentralized distributed max-sum BP, self-terminating tree-based bounded approximation, tabu search implemented in a centralized fashion, and a combination of the latter two. Performance is measured by the end-user utility for all algorithms and by two types of approximation ratios for the tree-based bounded approximation. BP-based decentralized algorithms are found to exhibit comparable performance with a centralized algorithm and superior performance to no adaptive scanning. Furthermore, our analysis demonstrates that max-sum BP is capable of generating solutions within 67% of optimal (and typically much better) across the weather scenarios.

## Short LDPC codes for NB-PLC channel with a differential evolution construction method

- **Status**: ✅
- **Reason**: 단블록 바이너리 LDPC 차수분포를 differential evolution으로 최적화하는 코드설계(E) 기법, 이식 가능
- **ID**: ieee:6525856
- **Type**: conference
- **Published**: 24-27 Marc
- **Authors**: Nikoleta Andreadou, Andrea M. Tonello
- **PDF**: https://ieeexplore.ieee.org/document/6525856
- **Abstract**: In this paper, we study the performance of Low Density Parity Check (LDPC) codes and we introduce an optimized version of these codes when applied on the short data blocks of a narrowband (NB) power line communications (PLC) system. We compare their performance with the one obtained when the G3 standard coding scheme is applied on the system, namely the scheme that concatenated convolutional with Reed-Solomon codes. Multipath propagation together with two noise scenarios are considered: background AWGN noise with and without the presence of impulsive noise. The results indicate that under the considered channel and noise conditions the introduced optimized LDPC codes can operate better than the concatenated scheme used in the G3 standard. The optimized irregular LDPC codes are obtained from the well-established method of differential evolution for finding a degree distribution pair that improves the performance. The evaluation of each candidate code, is proposed to be carried out with a method that takes into account the actual channel and noise conditions. The equivalent optimized degree distribution pairs are presented.

## Robust turbo decoding in impulse noise channels

- **Status**: ❌
- **Reason**: 터보 디코딩 trellis clipping 기법 - 터보 전용이라 LDPC BP에 이식 불가
- **ID**: ieee:6525855
- **Type**: conference
- **Published**: 24-27 Marc
- **Authors**: Der-Feng Tseng, Tsung-Ru Tsai, Yunghsiang S. Han
- **PDF**: https://ieeexplore.ieee.org/document/6525855
- **Abstract**: Powerline communications, an enabling technology for data networking alternative, susceptible to impulse noise such that it is likely to miss an assured quality of service. Turbo coding has long served as an essential tool to overcome this obstacle. However, this comes at the cost of estimating the statistics of impulse noise, which is generally not time-invariant and may change rapidly over time, further increasing receiver complexity. This study proposes clipping on trellis to avoid this problem. A corresponding decoder metric dictated by the clipping threshold, which is a function of the probability of guessing for the unknown impulse arrival probability, was properly formulated to leverage the coding gain. Regardless of the impulse noise model assumed, the simulation results in this study, in terms of bit error probability, show that the proposed decoding scheme is robust to impulse and performs fairly close to its sophisticated counterpart, which however fully exploits the statistics of the impulse noise.

## An efficient LDPC encoder based on block-row-cycle structure for CMMB

- **Status**: ✅
- **Reason**: CMMB용 block-row-cycle 구조 LDPC 인코더로 HW 메모리 절감—구조 활용 인코더 HW 기법 이식 가능(D), 애매해 살림
- **ID**: ieee:6747811
- **Type**: conference
- **Published**: 23-25 Marc
- **Authors**: Lei Liu, Peng Zhang, Ziliang Lin
- **PDF**: https://ieeexplore.ieee.org/document/6747811
- **Abstract**: Concerning the high encoding complexity of LDPC codes, an efficient encoder based on block-row-cycle structure for CMMB is proposed, which is able to take full advantage of the characteristics of the sparse parity-check matrix, such as cyclicity and equality of row weight. Experimental results show that the proposed encoder can reduce dramatically the memory requirements in hardware implementation, and improve the encoding rate at the same time.

## Linear LLR approximation for LDPC decoding using a Gaussian approximation

- **Status**: ✅
- **Reason**: 페이딩 채널 CSI 없이 LLR PDF의 Gaussian 근사로 LLR 계산 복잡도 감소—LLR 양자화/근사 기법은 NAND 디코더에 이식 가능(A/C)
- **ID**: ieee:6747759
- **Type**: conference
- **Published**: 23-25 Marc
- **Authors**: Xinyi Zhong, Youyun Xu, Kui Xu
- **PDF**: https://ieeexplore.ieee.org/document/6747759
- **Abstract**: In fading channels, the computation of Loglikelihood ratio (LLR) without channel state information (CSI) is complicated. The maximum capacity linear approximation (MCLA) has been proposed to reduce the computational complexity of LLR. However, the computation of LLR' probability density function (PDF) is still complicated due to numerical integrations. To overcome this shortage, we propose a simple Gaussian approximation to PDF of LLR. Using our proposed method, the computational complexity is significantly reduced and the BER performance is still very close to that of the MCLA in uncorrelated Rayleigh fading channels.

## Design of improved LDPC encoder for CMMB based on SIMD architecture

- **Status**: ✅
- **Reason**: LU분해 기반 SIMD 병렬 LDPC 인코더, 파이프라인/Ping-Pong 버퍼로 throughput 개선—이식 가능 HW 아키텍처(D)
- **ID**: ieee:6747774
- **Type**: conference
- **Published**: 23-25 Marc
- **Authors**: Hang Yin, Weitao Du, Nanhao Zhu
- **PDF**: https://ieeexplore.ieee.org/document/6747774
- **Abstract**: This paper designs and implements a novel parallel LDPC encoder. It based on LU decomposition, according to the inherent characteristics of LDPC Parity-Check Matrix in CMMB. It is applied to design CMMB baseband exciter, which can support 2 different code rates (1/2 and 3/4). The SIMD parallel architecture is proposed to solve the encoding delay caused by iteration of LU algorithm, full pipeline and multistage Ping-Pong buffer structure are also used to improve throughput in high-speed encoding. It meets the requirements both in real-time performance and resource utilization. Furthermore, this method is generic and can be adapted easily for other LDPC codes; thus, it has a significant practical value.

## LDPC code design for OOK modulated Poisson optical channels

- **Status**: ❌
- **Reason**: Poisson/OOK 광채널용 표준 density evolution LDPC 앙상블 최적화, 새 디코더·구성 없는 무선/통신 응용 특이적
- **ID**: ieee:6552291
- **Type**: conference
- **Published**: 20-22 Marc
- **Authors**: Tingjun Xie, Stephen G. Wilson, Maite Brandt-Pearce +1
- **PDF**: https://ieeexplore.ieee.org/document/6552291
- **Abstract**: The Poisson channel is a popular direct-detection model in optical communication. In this paper, we study efficient data communication over the on-off keyed (OOK) modulated Poisson channel. We first analyze the channel capacity, and based on the analysis we study the application of low-density parity-check (LDPC) codes on such channels. The asymmetric density evolution (ADE) method is used to determine the decoding threshold of an LDPC ensemble, and it is demonstrated that optimized LDPC ensembles have near-capacity performance, for various code rates. We also point out that the robustness of LDPC codes for the Poisson channel, i.e. a certain optimized LDPC ensemble remain (essentially) optimal over a wide range of channel conditions, making LDPC codes an attractive forward correcting coding (FEC) scheme for optical communication.

## A scaling method for stochastic LDPC decoding over the binary symmetric channel

- **Status**: ✅
- **Reason**: BSC용 stochastic LDPC 디코딩 scaling 기법 — error floor 개선, HW 라우팅혼잡 완화로 이식 가능(C/D)
- **ID**: ieee:6552331
- **Type**: conference
- **Published**: 20-22 Marc
- **Authors**: Kuo-Lun Huang, Vincent Gaudet, Masoud Salehi
- **PDF**: https://ieeexplore.ieee.org/document/6552331
- **Abstract**: Stochastic decoding is a decoding algorithm for Low-Density Parity-Check (LDPC) codes that leads to lowered routing congestion. Randomization is crucial for generating stochastic bits in stochastic decoders. In this paper, we propose a scaling method for stochastic LDPC decoding over the binary symmetric channel model that is independent of the channel error probability, and thus reduces the complexity in the conversion of received messages into stochastic streams. The scaling method not only improves the error rate performance, but lowers the error floor for stochastic decoding.

## Cooperative communication using protograph-based low-density parity-check codes

- **Status**: ❌
- **Reason**: 협력통신용 표준 AR4JA protograph LDPC 적용, 떼어낼 신규 디코더·구성 없음
- **ID**: ieee:6552308
- **Type**: conference
- **Published**: 20-22 Marc
- **Authors**: Osso Vahabzadeh, Masoud Salehi
- **PDF**: https://ieeexplore.ieee.org/document/6552308
- **Abstract**: We propose a novel two-user cooperation scheme that employs protograph-based low-density parity-check (LDPC) codes. The proposed scenario is based on time division where each user transmits its message to the base station (BS) in two successive intervals. In the first interval, the user sends its message to the BS as well as its partner user. If the partner user successfully decodes the received signal, the two users cooperatively send the main user's message using the Alamouti scheme during the second interval. Otherwise, the main user simply retransmits its message to the BS. The users change roles during the next two intervals. Furthermore, the users encode their information over a class of protograph-based LDPC codes called the Accumulate-Repeat-4-Jagged-Accumulate (AR4JA) codes that allow flexible selections of rate and length. Using this technique, a three-level diversity is achieved when there exists a strong interuser link, whereas when the interuser channel has a poor quality, at least a two-level diversity is achieved.

## A Binning Design for Wyner-Ziv Video Coding

- **Status**: ❌
- **Reason**: Wyner-Ziv 비디오 binning + Fountain coding 소스코딩/JSCC, 떼어낼 LDPC ECC 기법 없음
- **ID**: ieee:6543108
- **Type**: conference
- **Published**: 20-22 Marc
- **Authors**: Wen Ji, Yiqiang Chen
- **PDF**: https://ieeexplore.ieee.org/document/6543108
- **Abstract**: In this work, we proposes a two-tier binning scheme. First, we develop a Fountain coding with side information to construct the inner binning structure. Second, for the the outer binning, we model the WZ video coding architecture as a multi-access channel and exploit the duality property between the WZ coding and channel coding techniques. Third, we provide both the primal and dual solutions. For the primal distortion minimization problem, we use dynamic programming approach to find the optimal binning policy, and for the dual capacity maximization problem, we give a near sum-capacity binning algorithm. The objective is to lower the coding rate under same video reconstruction quality.

## Distributed reception with coarsely-quantized observation exchanges

- **Status**: ❌
- **Reason**: 분산수신 coarse quantization 통신 응용, LDPC는 baseline — 떼어낼 ECC 기법 없음
- **ID**: ieee:6624254
- **Type**: conference
- **Published**: 20-22 Marc
- **Authors**: D. Richard Brown, Min Ni, Upamanyu Madhow +1
- **PDF**: https://ieeexplore.ieee.org/document/6624254
- **Abstract**: This paper considers the problem of jointly decoding binary phase shift keyed (BPSK) messages from a single distant transmitter to a cooperative receive cluster connected by a local area network (LAN). A distributed reception technique is proposed based on the exchange of coarsely-quantized observations among some or all of the nodes in the receive cluster. By taking into account the differences in channel quality across the receive cluster, the quantized information from other nodes in the receive cluster can be appropriately combined with locally unquantized information to form aggregate posterior likelihoods for the received bits. The LAN throughput requirements of this technique are derived as a function of the number of participating nodes in the receive cluster, the forward link code rate, and the quantization parameters. Using information theoretic analysis and simulations of an LDPC coded system in fading channels, numerical results show that the performance penalty (in terms of outage probability and block error rate with respect to ideal receive beamforming) due to coarse quantization is small in the low SNR regimes enabled by cooperative distributed reception.

## A modified bethe free energy approximation for codeword quantization

- **Status**: ❌
- **Reason**: codeword quantization(소스코딩) 메시지패싱, 채널 ECC 아니며 LDGM 기반
- **ID**: ieee:6552316
- **Type**: conference
- **Published**: 20-22 Marc
- **Authors**: José M. Fernández, Phillip A. Regalia
- **PDF**: https://ieeexplore.ieee.org/document/6552316
- **Abstract**: A novel codeword quantization algorithm based on message-passing using a low density generator matrix formulation is proposed and analyzed. The scheme is a seemingly subtle variant on a recently proposed “truthiness” propagation algorithm, but one which affords a more explicit connection to a modified Bethe free energy function. Applications to distributed coding in sensor networks are also included in the simulation examples, where the algorithm is observed to outperform conventional LDPC belief propagation decoding using side information, in a practical setting when the reliability of the side information diminishes.

## Genome Sequence Compression with Distributed Source Coding

- **Status**: ❌
- **Reason**: 유전체 압축 분산소스코딩(DSC), LDPC가 소스코딩용 — 채널 ECC 아님
- **ID**: ieee:6543135
- **Type**: conference
- **Published**: 20-22 Marc
- **Authors**: Shuang Wang, Xiaoqian Jiang, Lijuan Cui +6
- **PDF**: https://ieeexplore.ieee.org/document/6543135
- **Abstract**: In this paper, we develop a novel genome compression framework based on distributed source coding (DSC)[3], which is specially tailored to the need of miniaturized devices. At the encoder side, subsequences with adaptive code length can be compressed flexibly through either low complexity DSC based syndrome coding or hash coding with the decision determined by the existence of variations between source and reference known from the decoder feedback. Moreover, to tackle the variations between source and reference at the decoder, we carefully designed a factor graph based low-density parity-check (LDPC) decoder, which automatically detects insertion, deletion and substitution.

## Variable Coded Modulation software simulation

- **Status**: ❌
- **Reason**: CCSDS 표준 turbo/LDPC 코드를 그대로 쓴 VCM 소프트웨어 시뮬레이션, 신규 기여 없음
- **ID**: ieee:6497354
- **Type**: conference
- **Published**: 2-9 March 
- **Authors**: Thomas A. Sielicki, Jon Hamkins, Denise Thorsen
- **PDF**: https://ieeexplore.ieee.org/document/6497354
- **Abstract**: This paper reports on the design and performance of a new Variable Coded Modulation (VCM) system. This VCM system comprises eight of NASA's recommended codes from the Consultative Committee for Space Data Systems (CCSDS) standards, including four turbo and four AR4JA/C2 low-density parity-check codes, together with six modulations types (BPSK, QPSK, 8-PSK, 16-APSK, 32-APSK, 64-APSK). The signaling protocol for the transmission mode is based on a CCSDS recommendation. The coded modulation may be dynamically chosen, block to block, to optimize throughput.

## Performance of decoder-based algorithms for signal synchronization for DSSS waveforms

- **Status**: ❌
- **Reason**: DSSS 반송파 동기화(디코더 피드백 활용)로 ECC 기법이 아님, 동기화 알고리즘
- **ID**: ieee:6497140
- **Type**: conference
- **Published**: 2-9 March 
- **Authors**: Adina Matache, Esteban L. Vallés
- **PDF**: https://ieeexplore.ieee.org/document/6497140
- **Abstract**: This paper presents results on the implementation of pilotless carrier synchronization algorithms at low SNRs using joint decoding and decision-directed tracking. A software test bed was designed to simulate the effects of decision-directed carrier synchronization (DDCS) techniques. These techniques are compared to non-decision directed algorithms used in phase-locked loops (PLLs) or Costas loops. In previous work by the authors, results for direct M-ARY modulation constellations, with no code spreading were introduced. This paper focuses on the application of the proposed family of decision directed algorithms to direct sequence spread spectrum (DSSS) waveforms, typical of GPS signals. The current algorithm can utilize feedback from turbo codes in addition to the prior support of LDPC codes.

## Multi-service data dissemination for space-based augmentation systems

- **Status**: ❌
- **Reason**: SBAS 신호에 generalized LDPC 적용, 응용 특이적이고 새 디코더/구성 기여 없음(표준 LDPC 사용)
- **ID**: ieee:6496948
- **Type**: conference
- **Published**: 2-9 March 
- **Authors**: Mariano Vergara, Felix Antreich, Gianluigi Liva +1
- **PDF**: https://ieeexplore.ieee.org/document/6496948
- **Abstract**: New SBAS (Satellite Based Augmentation System) signals could include the provision of new additional services alongside the defined SBAS L1/L5 aeronautical service [1], if additional power becomes available. In this paper we present a solution that efficiently makes use of the additional available power in order to increase the overall data rate of a new multi-service SBAS signal. These new SBAS signals will be backward compatible. The high power efficiency of the proposed scheme is guaranteed by a variation of the interplex scheme that is characterized by a variable envelope signal constellation. A coding scheme based on generalized low density parity check (LDPC) codes ensures that service requirements can be met with a lower SNR (Signal-to-Noise Ratio).

## Radio science measurements with suppressed carrier

- **Status**: ❌
- **Reason**: 억압반송파 라디오과학 측정·CRB 분석, LDPC ECC 기법 무관
- **ID**: ieee:6497156
- **Type**: conference
- **Published**: 2-9 March 
- **Authors**: Sami Asmar, Dariush Divsalar, Kamal Oudrhiri +1
- **PDF**: https://ieeexplore.ieee.org/document/6497156
- **Abstract**: Radio Science started when it became apparent with early deep space missions that occultations by planetary atmospheres would affect the quality of radio communications. Since then the atmospheric properties and other aspects of planetary science, solar science, and fundamental physics were studied by scientists. Radio Science data was always extracted from a received pure residual carrier (without data modulation). For some missions, it is very desirable to obtain Radio Science data from a suppressed carrier modulation. In this paper we propose a method to extract Radio Science data when a coded suppressed carrier modulation is used in deep space communications. The type of modulation can be BPSK, QPSK, OQPSK, MPSK or even GMSK. However we concentrate mostly on BPSK modulation. The proposed method for suppressed carrier simply tries to wipe out data that acts as an interference for Radio Science measurements. In order to measure the estimation errors in amplitude and phase of the Radio Science data we use the Cramer-Rao bound (CRB). The CRB for suppressed carrier modulation with non-ideal data wiping is then compared with residual carrier modulation under the same noise condition. The method of derivation of the CRB for non-ideal data wiping is an innovative method that is presented here. Some numerical results are provided for a coded system.

## Space and frequency multiplexing for MM-wave multi-gigabit point-to-point transmission links

- **Status**: ❌
- **Reason**: MM-wave 점대점 링크 space-frequency multiplexing, LDPC 무관 — 통신 응용 특이적
- **ID**: ieee:6496822
- **Type**: conference
- **Published**: 2-9 March 
- **Authors**: Claudio Sacchi, Cosimo Stallo, Tommaso Rossi
- **PDF**: https://ieeexplore.ieee.org/document/6496822
- **Abstract**: During last 10 years, the use of frequencies at E-band from 71 GHz to 76 GHz, from 81 GHz to 86 GHz and from 92 GHz to 95 GHz to licensed users has been regulated in US, Europe, Australia and Japan. Due to the large amount of available bandwidth and reasonable atmospheric attenuation, these frequency bands are suitable for very high data rate radio communication for medium to long range wireless links. However, in order to convert the bandwidth availability into real capacity, suitable transmission techniques should be designed. In the present paper, we propose a space-frequency multiplexing technique using FDM, coded modulation and 4×4 MIMO spatial multiplexing for point-to-point multi-gigabit connection in the 81-86 GHz bandwidth. We tested the proposed system, considering different link distances, different values of pathloss and atmospheric and rain attenuations. Simulation results evidenced the possibility of achieving a 48 Gb/s net capacity over 5GHz bandwidth (spectral efficiency 9.6 b/s/Hz) with 99.98% availability at link distances up to 1 Km.

## Error correcting codes for next generation spacecraft telecommand

- **Status**: ❌
- **Reason**: 우주 telecommand용 ECC 제안이나 일반론적 코드 선택 논의, NAND 바이너리 LDPC에 떼어낼 신규 디코더/HW/설계 기법 없음
- **ID**: ieee:6496915
- **Type**: conference
- **Published**: 2-9 March 
- **Authors**: Kenneth Andrews, Dariush Divsalar, Jon Hamkins +1
- **PDF**: https://ieeexplore.ieee.org/document/6496915
- **Abstract**: With the advent of modern coding techniques, considerable improvement is possible over the BCH codes specified in the current Consultative Committee for Space Data Systems (CCSDS) telecommand standard. Two broad classes of applications are identified, one for low-data-rate transfer of simple commands and protocol information, and the other for transfer of files and complex command sequences. New error correcting codes are proposed for each, and their interactions with the surrounding protocol layers are discussed. Feasibility of each is also demonstrated with prototype implementations of the coding systems.

## A spatially-coupled type LDPC Code with an NCG of 12 dB for optical transmission beyond 100 Gb/s

- **Status**: ❌
- **Reason**: SC-type irregular LDPC+BCH 연접 광전송 응용, 표준 SC-LDPC 사용 수준이고 신규 구성·디코더 기여 불명
- **ID**: ieee:6532740
- **Type**: conference
- **Published**: 17-21 Marc
- **Authors**: Kenya Sugihara, Yoshikuni Miyata, Takashi Sugihara +4
- **PDF**: https://ieeexplore.ieee.org/document/6532740
- **Abstract**: We propose a novel SD-FEC employing the concatenation of a spatially-coupled type irregular LDPC code with a BCH code. Numerical simulations show an NCG of 12.0 dB at a BER of 10-15 with 25.5% redundancy.

## Impact of interleaving on SD-FEC operating in highly non-linear XPM-limited regime

- **Status**: ❌
- **Reason**: interleaving이 SD-FEC BER에 미치는 영향 실험, 떼어낼 디코더/구성 기법 없음
- **ID**: ieee:6533103
- **Type**: conference
- **Published**: 17-21 Marc
- **Authors**: Paolo Leoni, Vincent Sleiffer, Stefano Calabrò +4
- **PDF**: https://ieeexplore.ieee.org/document/6533103
- **Abstract**: We experimentally investigate the behavior of two SD codes in a 100G-PDM-DQPSK system with high-power 10G-OOK neighbors. We show that in the presence of sufficient interleaving the input-output BER relationship of both codes remains unaffected.

## Real-time DSP for 100+ Gb/s

- **Status**: ❌
- **Reason**: 100G coherent ASIC 설계 논의 개관, 구체적 LDPC 디코더/구성 기여 없음
- **ID**: ieee:6533098
- **Type**: conference
- **Published**: 17-21 Marc
- **Authors**: C. Rasmussen, Y. Pan, M. Aydinlik +9
- **PDF**: https://ieeexplore.ieee.org/document/6533098
- **Abstract**: We discuss the commercial context and technical requirements to 100G coherent interfaces and illustrate ASIC design decisions and challenges, looking beyond 100G as well.

## 1-Tbit/s dual-carrier DP 64QAM transmission at 64Gbaud with 40% overhead soft-FEC over 320km SSMF

- **Status**: ❌
- **Reason**: 1Tbit/s 광전송 데모, soft-FEC는 베이스라인, 떼어낼 ECC 기법 없음
- **ID**: ieee:6532955
- **Type**: conference
- **Published**: 17-21 Marc
- **Authors**: F. Buchali, K. Schuh, L. Schmalen +3
- **PDF**: https://ieeexplore.ieee.org/document/6532955
- **Abstract**: We demonstrate 1-Tbit/s dual-carrier dual-polarization 64QAM transmission at 64Gbaud over 320km of standard single-mode fiber with EDFAs only. Error free performance is validated by sFEC decoding of the received data after fiber transmission.

## Collaborative signal processing with FEC in digital coherent systems

- **Status**: ❌
- **Reason**: 비선형 equalizer+soft FEC 조합 개념 논의, 구체적 디코더/구성 기여 없음
- **ID**: ieee:6532739
- **Type**: conference
- **Published**: 17-21 Marc
- **Authors**: Takashi Sugihara, Tsuyoshi Yoshida, Takashi Mizuochi
- **PDF**: https://ieeexplore.ieee.org/document/6532739
- **Abstract**: We discuss the concept of combination of nonlinearity equalizer and soft-decision FEC decoder. The appropriate choice of equalization performance and error correcting capability of FEC is essential for performance optimization with existing nonlinear phase noise.

## Performance evaluation of coded optical subcarrier index modulation OFDM format

- **Status**: ❌
- **Reason**: 광 OFDM subcarrier index modulation 변조 성능비교, 떼어낼 LDPC ECC 기법 없음
- **ID**: ieee:6532621
- **Type**: conference
- **Published**: 17-21 Marc
- **Authors**: Abdullah Al Amin, Xiao Yue, William Shieh
- **PDF**: https://ieeexplore.ieee.org/document/6532621
- **Abstract**: We compare the performance of coded subcarrier index modulation for coherent optical OFDM transmission. An improvement over standard QPSK is confirmed at the lower SE, though for equal SE cases coded performance gets worse.

## Design of optimum physical layer architecture for a high data rate LTE uplink transceiver

- **Status**: ❌
- **Reason**: LTE 상향링크 SC-FDMA 물리계층 설계, LDPC는 부수 ECC - 떼어낼 신규 디코더/구성 기법 없음
- **ID**: ieee:6533926
- **Type**: conference
- **Published**: 14-15 Marc
- **Authors**: G. Indumathi, D. Allin Joe
- **PDF**: https://ieeexplore.ieee.org/document/6533926
- **Abstract**: The Third Generation Partnership Project (3GPP) provides the Long Term Evolution (LTE) standards for the fourth generation (4G) wireless communication systems. Single Carrier Frequency Division Multiple Access (SC-FDMA) and Orthogonal Division Multiple Access (OFDMA) are the two major techniques used in LTE. The main drawback of OFDMA over SC-FDMA is its high peak to average power ratio (PAPR). Hence OFDMA is used in the downlink of the fourth generation (4G) wireless communication systems for its high spectral efficiency and high PAPR. SC-FDMA is used in the uplink of the fourth generation (4G) wireless communication systems since it is more power efficient. The main objective of this paper is to design optimum physical layer architecture of a high data rate LTE uplink transceiver using SC-FDMA multiple access scheme with error correction mechanism using Low dense parity check codes (LDPC) to provide lesser Bit Error Rate (BER) and avoiding packet loss by Interleaving. The optimum physical layer architecture for the fourth generation (4G) wireless communication systems is chosen by comparing the LDPC coded SC-FDMA with the LDPC coded OFDMA. The chosen architecture must be more power efficient and support high data rates, which is the main prerequisite for the mobile user.
