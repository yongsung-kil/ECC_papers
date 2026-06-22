# IEEE Xplore — 2012-07 (1차선별 통과)


## Trapping Set Error Correction through Adaptive Informed Dynamic Scheduling Decoding of LDPC Codes

- **Status**: ✅
- **Reason**: 적응형 IDS(informed dynamic scheduling) 디코딩으로 trapping set 오류 정정 — 바이너리 LDPC BP 스케줄링 개선 기법, NAND LDPC에 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6196149
- **Type**: journal
- **Published**: July 2012
- **Authors**: Saejoon Kim
- **PDF**: https://ieeexplore.ieee.org/document/6196149
- **Abstract**: Recent studies indicate that sequential scheduling of iterative decoding of low-density parity-check codes can provide improved code performance in comparison with the conventional flooding in terms of decoding success rate and convergence speed. In particular, a class of sequential scheduling schemes known as informed dynamic scheduling (IDS) has shown to outperform other sequential scheduling schemes from its capability to correct trapping set errors. In this letter, we present an adaptive IDS scheme which combines and outperforms previously proposed sequential scheduling schemes.

## Analytical Solution of Covariance Evolution for Irregular LDPC Codes

- **Status**: ✅
- **Reason**: 불규칙 LDPC 유한길이 covariance evolution 해석해; 블록오류확률 scaling은 바이너리 LDPC 유한길이 설계(E)에 이식 가능 → 애매시 in
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6172583
- **Type**: journal
- **Published**: July 2012
- **Authors**: Takayuki Nozaki, Kenta Kasai, Kohichi Sakaniwa
- **PDF**: https://ieeexplore.ieee.org/document/6172583
- **Abstract**: The scaling law developed by Amraoui et al. is a powerful technique to estimate the block erasure probabilities of finite- length low-density parity-check (LDPC) codes. Solving a system of differential equations called covariance evolution, one can obtain the scaling parameter. However, the covariance evolution has not been analytically solved. In this paper, we present the analytical solution of the covariance evolution for irregular LDPC code ensembles.

## On the Pseudocodeword Redundancy of Binary Linear Codes

- **Status**: ✅
- **Reason**: 바이너리 선형코드 pseudocodeword redundancy/패리티검사 행 수와 최소 의사무게; LDPC BP 디코딩 성능 분석에 이식 가능(E), 애매시 in
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6179330
- **Type**: journal
- **Published**: July 2012
- **Authors**: Jens Zumbrägel, Vitaly Skachek, Mark F. Flanagan
- **PDF**: https://ieeexplore.ieee.org/document/6179330
- **Abstract**: For a binary linear code, the pseudocodeword redundancy with respect to the additive white Gaussian noise channel, the binary symmetric channel, or the max-fractional weight is defined to be the smallest number of rows in a parity-check matrix such that the corresponding minimum pseudoweight is equal to the minimum Hamming distance of the code. It is shown that most codes do not have a finite pseudocodeword redundancy. Also, upper bounds on the pseudocodeword redundancy for some families of codes, including codes based on designs, are provided. The pseudocodeword redundancies for all codes of small length (at most 9) are computed. Furthermore, comprehensive results are provided on the cases of cyclic codes of length at most 250 for which the eigenvalue bound of Vontobel and Koetter is sharp.

## Mathematical Programming Decoding of Binary Linear Codes: Theory and Algorithms

- **Status**: ✅
- **Reason**: 바이너리 선형코드 수리계획(LP/ILP) 디코딩 리뷰지만 BP 대안 디코딩 알고리즘 분류·기법 정리, LP decoding은 LDPC BP 이식 가능(C), 애매시 in
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6187728
- **Type**: journal
- **Published**: July 2012
- **Authors**: Michael Helmling, Stefan Ruzika, Akın Tanatmis
- **PDF**: https://ieeexplore.ieee.org/document/6187728
- **Abstract**: Mathematical programming is a branch of applied mathematics and has recently been used to derive new decoding approaches, challenging established but often heuristic algorithms based on iterative message passing. Concepts from mathematical programming used in the context of decoding include linear, integer, and nonlinear programming, network flows, notions of duality as well as matroid and polyhedral theory. This paper reviews and categorizes decoding methods based on mathematical programming approaches for binary linear codes over binary-input memoryless symmetric channels.

## An efficient bit-flipping decoding algorithm for LDPC codes

- **Status**: ✅
- **Reason**: 채널 독립 개선 bit-flipping 디코딩(패리티 신뢰도 계산 개선) — 이식 가능한 바이너리 LDPC 디코더 알고리즘(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6294975
- **Type**: conference
- **Published**: 23-27 July
- **Authors**: Tso-Cho Chen
- **PDF**: https://ieeexplore.ieee.org/document/6294975
- **Abstract**: In this paper, a new method for improving hard-decision bit-flipping (BF) decoding is proposed for low-density parity-check codes. The flipping criterion is derived theoretically from the soft-decision belief-propagation decoding algorithm. The proposed BF decoding algorithm is channel independent and is improved by introducing a more efficient method for computing the reliability of the parity checks. Extensive simulations are provided to demonstrate the efficiency of the proposed algorithm. Simulation results show that the proposed algorithm can achieve about 1.5dB coding gain improvement at BER = 5×10−6 while reducing up to 48% iterations for decoding and maintaining low decoding complexity, compared with the conventional weighted BF algorithm.

## An early stopping criterion for LDPC decoding based on average weighted reliability measure

- **Status**: ✅
- **Reason**: 평균 가중 신뢰도 기반 early stopping 기준 — 부호 비의존 디코더 반복중단 기법으로 NAND LDPC 디코더에 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6294956
- **Type**: conference
- **Published**: 23-27 July
- **Authors**: Tso-Cho Chen
- **PDF**: https://ieeexplore.ieee.org/document/6294956
- **Abstract**: An early stopping criterion for low-density parity-check decoding is proposed to reduce the number of decoding iterations. The proposed early stopping criterion is based on the average weighted reliability measure of the hard output of decoder to detect undecodable blocks in an early stage of the decoding process. Simulation results show that the proposed algorithm can achieve about 0.2–0.4 dB coding gain improvement on average while reducing up to about 50%–85% iteration for decoding at low to medium Eb/N0, compared with the existing method.

## Will the real error floor please stand up?

- **Status**: ✅
- **Reason**: 메시지 saturation/quantization가 SPA/MSA error floor에 미치는 영향과 quasi-uniform 양자화 기법, NAND LDPC 디코더 양자화에 직접 이식(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6290251
- **Type**: conference
- **Published**: 22-25 July
- **Authors**: Xiaojie Zhang, Paul H. Siegel
- **PDF**: https://ieeexplore.ieee.org/document/6290251
- **Abstract**: In this paper we continue our study of the influence of message saturation and quantization on the error-rate performance of iterative, message-passing decoders for low-density parity-check (LDPC) codes. We extend our previous analytical results for the min-sum algorithm (MSA) and its variants to the sum-product algorithm (SPA), demonstrating the significant impact of message saturation on the appearance and location of error floors. Simulation results for selected LDPC codes on the binary symmetric channel (BSC) and the additive white Gaussian noise channel (AWGNC) confirm that the benefits of a quasiuniform quantization scheme, already observed in the context of MSA decoding, apply also to SPA-based decoding.

## A quantitative analysis of fixed-point LDPC-decoder implementations using hardware-accelerated HDL emulations

- **Status**: ✅
- **Reason**: 고정소수점 LDPC 디코더 HW 구현 정량분석, Pareto 비용모델/HDL 에뮬레이션(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:6404189
- **Type**: conference
- **Published**: 16-19 July
- **Authors**: Matthias Korb, Tobias G. Noll
- **PDF**: https://ieeexplore.ieee.org/document/6404189
- **Abstract**: Using hardware-accelerated HDL emulators of fixed-point implementations has several advantages in comparison to C-based simulations: The high degree of parallelism for example of field-programmable gate-array based hardware accelerators promise an increased emulation throughput. Furthermore, the HDL model of the considered circuit can be used in the following design process making an additional verification dispensable. For a system analysis of different low-density parity-check (LDPC) decoders such an emulator is practically inevitable from a throughput perspective: the outstanding error correction capability of those decoders allowing for bit-error rates (BER) of well below 10-10 requires a simulative decoding of billions of blocks. In this work, an HDL-based emulator is used. The designed HDL model is highly parameterizable and includes an LDPC decoder and high-quality Box-Muller-based white Gaussian-noise generators to create rare error-events. Using this emulator a comparison of the decoding capability of different fixed-point decoder implementations has been performed. Additionally, accurate cost-models are used for estimating the hardware costs of the different decoder implementations which enable an identification of Pareto-optimal decoder implementations. Finally, the achievable emulator throughput is discussed and compared to the simulation throughput of a speed optimized C-model.

## An FPGA-based prototyping method for verification, characterization and optimization of LDPC error correction systems

- **Status**: ✅
- **Reason**: FPGA 기반 LDPC FEC 프로토타이핑/검증, error floor 영역 BER 개선 방법론(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:6404188
- **Type**: conference
- **Published**: 16-19 July
- **Authors**: P. Sakellariou, I. Tsatsaragkos, N. Kanistras +2
- **PDF**: https://ieeexplore.ieee.org/document/6404188
- **Abstract**: This paper introduces a methodology for forward error correction (FEC) architectures prototyping, oriented to system verification and characterization. A complete design flow is described, which satisfies the requirement for error-free hardware design and acceleration of FEC simulations. FPGA devices give the designer the ability to observe rare events, due to tremendous speed-up of FEC operations. A Matlab-based system assists the investigation of the impact of very rare decoding failure events on the FEC system performance and the finding of solutions which aim to parameters optimization and BER performance improvement of LDPC codes in the error floor region. Furthermore, the development of an embedded system, which offers remote access to the system under test and verification process automation, is explored. The presented here prototyping approach exploits the high-processing speed of FPGA-based emulators and the observability and usability of software-based models.

## A new parity structure with multi-weight circulants for QC LDPC codes

- **Status**: ✅
- **Reason**: E: multi-weight circulant 기반 새 BDD 패리티 구조로 error floor 저감 및 효율적 인코딩—바이너리 QC-LDPC 설계
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6284131
- **Type**: conference
- **Published**: 1-6 July 2
- **Authors**: Hosung Park, Seokbeom Hong, Jong-Seon No +1
- **PDF**: https://ieeexplore.ieee.org/document/6284131
- **Abstract**: The block dual-diagonal (BDD) parity structure is widely adopted in many practical irregular quasi-cyclic (QC) low-density parity-check (LDPC) codes. These QC LDPC codes have good error-correcting performance in waterfall region but usually show relatively high error floors in low error rate region. In this paper, by using multi-weight circulants, a new BDD structure is proposed for the parity part of irregular QC LDPC codes to lower error floors and support efficient encoding. Since the parity part of parity-check matrices has flexible degree distribution with the aid of multi-weight circulants, QC LDPC codes with the proposed BDD structure can have large minimum Hamming distance compared to those with the conventional BDD structure, especially, in the low-rate case. Simulation results show that QC LDPC codes with the proposed BDD structure have lower error floor than those with the conventional BDD structure.

## Finite-length analysis of the TEP decoder for LDPC ensembles over the BEC

- **Status**: ✅
- **Reason**: BEC상 단/유한길이 LDPC TEP 디코더 + 실용 코드 설계용 scaling law, 이식 가능 디코더(C)/설계(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6283932
- **Type**: conference
- **Published**: 1-6 July 2
- **Authors**: Pablo M. Olmos, Fernando Pérez-Cruz, Luis Salamanca +1
- **PDF**: https://ieeexplore.ieee.org/document/6283932
- **Abstract**: In this work, we analyze the finite-length performance of low-density parity check (LDPC) ensembles decoded over the binary erasure channel (BEC) using the tree-expectation propagation (TEP) algorithm. In a previous paper, we showed that the TEP improves the BP performance for decoding regular and irregular short LDPC codes, but the perspective was mainly empirical. In this work, given the degree-distribution of an LDPC ensemble, we explain and predict the range of code lengths for which the TEP improves the BP solution. In addition, for LDPC ensembles that present a single critical point, we propose a scaling law to accurately predict the performance in the waterfall region. These results are of critical importance to design practical LDPC codes for the TEP decoder.

## A greedy search for improved QC LDPC codes with good girth profile and degree distribution

- **Status**: ✅
- **Reason**: E: girth profile 기반 QC-LDPC 탐색 알고리즘으로 새 코드 도출—코드 설계 기법
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6284129
- **Type**: conference
- **Published**: 1-6 July 2
- **Authors**: Irina E. Bocharova, Florian Hug, Rolf Johannesson +1
- **PDF**: https://ieeexplore.ieee.org/document/6284129
- **Abstract**: The girth profile is introduced and search algorithms for regular and irregular quasi-cyclic LDPC block codes with both good girth profile and good degree distribution are presented. New QC LDPC block codes of various code rates are obtained and their bit error rate performance is compared with that of the corresponding LDPC block codes defined in the IEEE 802.16 WiMAX standard of the same block length and code rate.

## A new ensemble of rate-compatible LDPC codes

- **Status**: ✅
- **Reason**: 바이너리 rate-compatible LDPC 앙상블 신규 구성(Kite codes 개선, 경험식) — E 코드설계 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6283974
- **Type**: conference
- **Published**: 1-6 July 2
- **Authors**: Kai Zhang, Xiao Ma, Shancheng Zhao +2
- **PDF**: https://ieeexplore.ieee.org/document/6283974
- **Abstract**: In this paper, we presented three approaches to improve the design of Kite codes (newly proposed rateless codes), resulting in an ensemble of rate-compatible LDPC codes with code rates varying “continuously” from 0.1 to 0.9 for additive white Gaussian noise (AWGN) channels. The new ensemble rate-compatible LDPC codes can be constructed conveniently with an empirical formula. Simulation results show that, when applied to incremental redundancy hybrid automatic repeat request (IR-HARQ) system, the constructed codes (with higher order modulation) perform well in a wide range of signal-to-noise-ratios (SNRs).

## A two stage selective averaging LDPC decoding

- **Status**: ✅
- **Reason**: C: trapping set 대응 2단계 BP 디코더로 error floor 개선, 바이너리 LDPC에 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6284048
- **Type**: conference
- **Published**: 1-6 July 2
- **Authors**: A. Dinesh Kumar, Ambedkar Dukkipati
- **PDF**: https://ieeexplore.ieee.org/document/6284048
- **Abstract**: Low density parity-check (LDPC) codes are a class of linear block codes that are decoded by running belief propagation (BP) algorithm or log-likelihood ratio belief propagation (LLR-BP) over the factor graph of the code. One of the disadvantages of LDPC codes is the onset of an error floor at high values of signal to noise ratio caused by trapping sets. In this paper, we propose a two stage decoder to deal with different types of trapping sets. Oscillating trapping sets are taken care by the first stage of the decoder and the elementary trapping sets are handled by the second stage of the decoder. Simulation results on the regular PEG (504,252,3,6) code and the irregular PEG (1024,518,15,8) code shows that the proposed two stage decoder performs significantly better than the standard decoder.

## Improving spatially coupled LDPC codes by connecting chains

- **Status**: ✅
- **Reason**: SC-LDPC 체인 연결로 디코딩 임계값 개선+복잡도 감소+최소거리 선형 성장 - 바이너리 LDPC 코드설계(E) 신규 구성
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6284232
- **Type**: conference
- **Published**: 1-6 July 2
- **Authors**: Dmitri Truhachev, David G. M. Mitchell, Michael Lentmaier +1
- **PDF**: https://ieeexplore.ieee.org/document/6284232
- **Abstract**: In this paper, we study ensembles of connected spatially coupled low-density parity-check codes (SC-LDPCCs), i.e., ensembles described by graphs in which regular SC-LDPCC chains of various lengths serve as edges. We show that, by carefully connecting individual SC-LDPCC chains, we obtain LDPC code ensembles with improved iterative decoding thresholds compared to those of a single coupled chain, in addition to reducing the decoding complexity required to achieve a specific bit error probability. Moreover, we show that, like the component SC-LDPCC chains, the proposed constructions have a typical minimum distance that grows linearly with block length.

## On Generalized EXIT charts of LDPC code ensembles over binary-input output-symmetric memoryless channels

- **Status**: ✅
- **Reason**: GEXIT 차트로 capacity-approaching 바이너리 LDPC 앙상블 설계, 이식 가능 코드설계(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6283930
- **Type**: conference
- **Published**: 1-6 July 2
- **Authors**: H. Mamani, H. Saeedi, A. Eslami +1
- **PDF**: https://ieeexplore.ieee.org/document/6283930
- **Abstract**: Generalized Extrinsic Information Transfer (GEXIT) charts were introduced as an extension of EXIT charts which have an extensive use in analysis and design of many iterative schemes including Low-Density Parity-Check (LDPC) codes. While a powerful as well as an insightful concept, their full potential as a designing tool for LDPC code ensembles has not been realized due to some missing steps. This papers aims at filling these gaps by proving some important properties of GEXIT charts and using them to design capacity-approaching LDPC code ensembles. The primary results on GEXIT charts are limited to regular variable and check node degrees. Moreover, variable node GEXIT curves have only been derived for the case where no physical channel is present. In a recent paper, GEXIT curves for irregular variable node and check node degree distributions have been derived. In this paper, we derive GEXIT charts of LDPC code ensembles over binary-input output-symmetric memoryless channels with any channel parameter. For the case of binary symmetric channel, we derive closed form expression for the GEXIT curve of variable nodes. We also propose to use an alternative representation of GEXIT charts in which we plot the inverse of variable node GEXIT curve together with dual GEXIT curve of the check node. We prove that the area theorem still holds in this case. Using these results, we analyze and design capacity-approaching LDPC codes using GEXIT charts.

## Quantized min-sum decoders with low error floor for LDPC codes

- **Status**: ✅
- **Reason**: C: min-sum 디코더의 새 메시지 양자화 방법으로 error floor 저감—NAND LLR 양자화에 직접 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6284049
- **Type**: conference
- **Published**: 1-6 July 2
- **Authors**: Xiaojie Zhang, Paul H. Siegel
- **PDF**: https://ieeexplore.ieee.org/document/6284049
- **Abstract**: The error floor phenomenon observed with LDPC codes and their graph-based, iterative, message-passing (MP) decoders is commonly attributed to the existence of error-prone substructures in a Tanner graph representation of the code. Many approaches have been proposed to lower the error floor by designing new LDPC codes with fewer such substructures or by modifying the decoding algorithm. In this paper, we show that one source of the error floors observed in the literature may be the message quantization rule used in the iterative decoder implementation. We then propose a new quantization method to overcome the limitations of standard quantization rules. Performance simulation results for two LDPC codes commonly found to have high error floors when used with the fixed-point min-sum decoder and its variants demonstrate the validity of our findings and the effectiveness of the proposed quantization algorithm.

## Low-density arrays of circulant matrices: Rank and row-redundancy, and QC-LDPC codes

- **Status**: ✅
- **Reason**: E: circulant 배열의 rank/row-redundancy 분석 및 새 QC-LDPC 구성법—바이너리 QC-LDPC 코드 설계 기법
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6284127
- **Type**: conference
- **Published**: 1-6 July 2
- **Authors**: Qin Huang, Keke Liu, Zulin Wang
- **PDF**: https://ieeexplore.ieee.org/document/6284127
- **Abstract**: This paper is concerned with general analysis on the rank and row-redundancy of an array of circulants whose null space defines a QC-LDPC code. Based on the Fourier transform and the properties of conjugacy classes and Hadamard products of matrices, tight bounds on rank and row-redundancy are derived, which make it possible to consider row-redundancy in constructions of QC-LDPC codes to achieve better performance. Moreover, a new construction of QC-LDPC codes from random partitions of finite fields, which has flexible code dimensions and is abundant in row-redundancy, is presented and analyzed.

## Trapping set structure of finite geometry LDPC codes

- **Status**: ✅
- **Reason**: E: finite geometry LDPC의 trapping set 구조 분석—error floor 관련 코드 설계 통찰
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6284130
- **Type**: conference
- **Published**: 1-6 July 2
- **Authors**: Qiuju Diao, Ying Yu Tai, Shu Lin +1
- **PDF**: https://ieeexplore.ieee.org/document/6284130
- **Abstract**: The trapping set structure of LDPC codes constructed using finite geometries is analyzed. A trapping set is modeled as a sub-geometry of the geometry used to construct an LDPC code. The variable nodes of a trapping set are viewed as points of the geometry and the check nodes adjacent to the variable nodes are viewed as the lines passing through any of these points. Based on this geometrical representation of a trapping set, its configuration can be determined.

## Tackling intracell variability in TLC Flash through tensor product codes

- **Status**: ✅
- **Reason**: TLC 플래시 intracell 변동성 모델링+generalized tensor product codes ECC; NAND 직접(A)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6282078
- **Type**: conference
- **Published**: 1-6 July 2
- **Authors**: Ryan Gabrys, Eitan Yaakobi, Laura Grupp +2
- **PDF**: https://ieeexplore.ieee.org/document/6282078
- **Abstract**: Flash memory is a promising new storage technology. To fully utilize future multi-level cell Flash memories, it is necessary to develop error correction coding schemes attuned to the underlying physical characteristics of Flash. Based on a careful inspection of fine-grained, experimentally-collected error patterns of TLC (three bits per cell) Flash, we propose a mathematical model that captures the intracell variability, which is manifested by certain patterns of bit-errors. Error correction codes are constructed for this model based upon generalized tensor product codes. For fixed levels of redundancy, these codes are shown to exhibit substantially lower bit error rates than existing error correction schemes.

## On the girth of quasi cyclic protograph LDPC codes

- **Status**: ✅
- **Reason**: E: QC 프로토그래프 LDPC의 girth 상한 유도 및 lifting degree 선택 지침—코드 설계 기법
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6284128
- **Type**: conference
- **Published**: 1-6 July 2
- **Authors**: Mehdi Karimi, Amir H. Banihashemi
- **PDF**: https://ieeexplore.ieee.org/document/6284128
- **Abstract**: In this paper, we study the relationships between the girth of the Tanner graph of a quasi cyclic (QC) protograph low-density parity-check (LDPC) code, on one hand, and the lifting degree and the size and the structure of the base graph, on the other hand. As a result, for a given base graph and a given lifting degree, we derive an upper bound on the girth of the resulting lifted graphs (codes). The upper bounds derived here are generally tighter than the existing bounds. The results presented in this work can be used to select an appropriate lifting degree for a given base graph, in order to have a desired girth, or to provide some insight in designing good base graphs, or to properly select the base graph's edge permutations.

## Approaching capacity at high rates with iterative hard-decision decoding

- **Status**: ✅
- **Reason**: spatially-coupled generalized LDPC의 반복 경판정 디코딩으로 용량 접근, 바이너리 — C 디코더 기법
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6284009
- **Type**: conference
- **Published**: 1-6 July 2
- **Authors**: Yung-Yih Jian, Henry D. Pfister, Krishna R. Narayanan
- **PDF**: https://ieeexplore.ieee.org/document/6284009
- **Abstract**: A variety of low-density parity-check (LDPC) ensembles have now been observed to approach capacity with message-passing decoding. However, all of them use soft (i.e., non-binary) messages and a posteriori probability (APP) decoding of their component codes. In this paper, we analyze a class of spatially-coupled generalized LDPC codes and observe that, in the high-rate regime, they can approach capacity under iterative hard-decision decoding. These codes can be seen as generalized product codes and are closely related to braided block codes.

## Spatially coupled ensembles universally achieve capacity under belief propagation

- **Status**: ✅
- **Reason**: SC-LDPC가 BP로 capacity universal 달성 증명 - 코드설계 이론이나 SC-LDPC 구성 근거로 E 이식 가능, 애매하면 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6284229
- **Type**: conference
- **Published**: 1-6 July 2
- **Authors**: Shrinivas Kudekar, Tom Richardson, Rüdiger Urbanke
- **PDF**: https://ieeexplore.ieee.org/document/6284229
- **Abstract**: We investigate spatially coupled code ensembles. For transmission over the binary erasure channel, it was recently shown that spatial coupling increases the belief propagation threshold of the ensemble to essentially the maximum a-priori threshold of the underlying component ensemble. This explains why convolutional LDPC ensembles, originally introduced by Felström and Zigangirov, perform so well over this channel. We show that the equivalent result holds true for transmission over general binary-input memoryless output-symmetric channels. More precisely, given a desired error probability and a gap to capacity, we can construct a spatially coupled ensemble which fulfills these constraints universally on this class of channels under belief propagation decoding. In fact, most codes in that ensemble have that property. The quantifier universal refers to the single ensemble/code which is good for all channels if we assume that the channel is known at the receiver. The key technical result is a proof that under belief propagation decoding spatially coupled ensembles achieve essentially the area threshold of the underlying uncoupled ensemble. We conclude by discussing some interesting open problems.

## Enhancing the error correction of finite alphabet iterative decoders via adaptive decimation

- **Status**: ✅
- **Reason**: C: FAID(유한알파벳 반복디코더) adaptive decimation으로 보장 정정능력 향상—저비트 메시지 디코더, NAND 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6284050
- **Type**: conference
- **Published**: 1-6 July 2
- **Authors**: Shiva Kumar Planjery, Bane Vasić, David Declercq
- **PDF**: https://ieeexplore.ieee.org/document/6284050
- **Abstract**: Finite alphabet iterative decoders (FAIDs) for LDPC codes were recently shown to be capable of surpassing the Belief Propagation (BP) decoder in the error floor region on the Binary Symmetric channel (BSC). More recently, the technique of decimation which involves fixing the values of certain bits during decoding, was proposed for FAIDs in order to make them more amenable to analysis while maintaining their good performance. In this paper, we show how decimation can be used adaptively to further enhance the guaranteed error correction capability of FAIDs that are already good on a given code. The new adaptive decimation scheme proposed has marginally added complexity but can significantly improve the slope of the error floor performance of a particular FAID. We describe the adaptive decimation scheme particularly for 7-level FAIDs which propagate only 3-bit messages and provide numerical results for column-weight three codes. Analysis suggests that the failures of the new decoders are linked to stopping sets of the code.

## Distance spectrum estimation of LDPC convolutional codes

- **Status**: ✅
- **Reason**: QC-LDPC 유래 LDPC-CC 거리 스펙트럼 추정/최소자유거리 상한 - 바이너리 LDPC error floor·거리 분석(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6284234
- **Type**: conference
- **Published**: 1-6 July 2
- **Authors**: Hua Zhou, David G. M. Mitchell, Norbert Goertz +1
- **PDF**: https://ieeexplore.ieee.org/document/6284234
- **Abstract**: Time-invariant low-density parity-check convolutional codes (LDPC-CCs) derived from corresponding quasi-cyclic (QC) LDPC block codes (LDPC-BCs) can be described by a polynomial syndrome former matrix (polynomial-domain transposed parity-check matrix). In this paper, an estimation of the distance spectrum of time-invariant LDPC-CCs is obtained by splitting the polynomial syndrome former matrix into submatrices representing “super codes” and then evaluating the linear dependence between codewords of the corresponding super codes. This estimation results in an upper bound on the minimum free distance of the original code and, additionally, a lower bound on the number of codewords Aw with Hamming weight w.

## Linear-programming decoding of Tanner codes with local-optimality certificates

- **Status**: ✅
- **Reason**: Tanner 부호 LP 디코딩 local-optimality 인증서, 바이너리 MBIOS — C 디코더 기법 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6284007
- **Type**: conference
- **Published**: 1-6 July 2
- **Authors**: Nissim Halabi, Guy Even
- **PDF**: https://ieeexplore.ieee.org/document/6284007
- **Abstract**: Given a channel observation y and a codeword x, we are interested in a one-sided error test that answers the questions: is x optimal with respect to y? is it unique? A positive answer for such a test is called a certificate for the optimality of a codeword. We present new certificates that are based on combinatorial characterization for local-optimality of a codeword in irregular Tanner codes. The certificate is based on weighted normalized trees in computation trees of the Tanner graph. These trees may have any finite height h (even greater than the girth of the Tanner graph). In addition, the degrees of local-code nodes are not restricted to two (i.e., skinny trees). We prove that local-optimality in this new characterization implies ML-optimality and LP-optimality, and show that a certificate can be computed efficiently. We apply the new local-optimality characterization to regular Tanner codes, and prove lower bounds on the noise thresholds of LP-decoding in MBIOS channels. When the noise is below these lower bounds, the probability that LP-decoding fails decays doubly exponentially in the girth of the Tanner graph.

## Parallel decoding of LDPC convolutional codes using OpenMP and GPU

- **Status**: ✅
- **Reason**: LDPC-CC GPU/OpenMP 병렬 디코딩 구현. 병렬화 HW/구현 기법(D), 바이너리 LDPC.
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:6249298
- **Type**: conference
- **Published**: 1-4 July 2
- **Authors**: Chi H. Chan, Francis C. M. Lau
- **PDF**: https://ieeexplore.ieee.org/document/6249298
- **Abstract**: Recently, there have been different applications, namely 10GBase-T Ethernet, video broadcasting and satellite communication, utilizing low-density parity-check (LDPC) codes as the forward-error-correction codes. The main reason is that the error performance of LDPC codes can be very close to the Shannon limit. LDPC codes can be further categorized into LDPC block codes (LDPC-BCs) and LDPC convolutional codes (LDPC-CCs). It has also been discovered that LDPC-CCs usually outperform LDPC-BCs. Simulation of LDPC-BCs and LDPC-CCs can take a lot of time because the decoding algorithms are relatively complex. Fortunately, the decoding steps can be performed in parallel. In this paper, we create three different platforms for simulating the error performance of LDPC-CCs. The first two platforms are run on a Central Processing Unit (CPU) while the third one involves the use of a Graphics Processing Unit (GPU). We show that using GPU can improve the simulation speed substantially.

## A fast searching method for the construction of QC-LDPC codes with large girth

- **Status**: ✅
- **Reason**: 대girth QC-LDPC 신규 고속 탐색 구성법(적응적 cost로 사이클 제거). 바이너리 코드설계(E).
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6249279
- **Type**: conference
- **Published**: 1-4 July 2
- **Authors**: Francis C. M. Lau, Wai Man Tam
- **PDF**: https://ieeexplore.ieee.org/document/6249279
- **Abstract**: In this paper, we propose an effective and efficient searching method for constructing quasi-cyclic low-density parity-check (QC-LDPC) codes with a desired girth g. We begin with an arbitrary QC-LDPC code with girth-4 and we evaluate only the number of cycles with length 4. When all the cycles with length 4 are removed by adjusting the elements of the QC-LDPC code, we form a QC-LDPC code with girth-6. Subsequently, we consider only the numbers of cycles with length 4 and length 6. In general, knowing that the current QC-LDPC code has a girth of g', we only consider the numbers of cycles with length up to g' even though g' may be smaller than the desired girth g. By using an adaptive cost function, which is defined as the number of cycles of length g', in the optimization/searching process, we are able to reduce the computational effort tremendously compared with Wang's searching algorithm [1]. Consequently, our proposed method can generate QC-LDPC codes with the desired girth much more efficiently.
