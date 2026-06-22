# IEEE Xplore — 2019-07 (1차선별 통과)


## Hardness Results on Finding Leafless Elementary Trapping Sets and Elementary Absorbing Sets of LDPC Codes

- **Status**: ✅
- **Reason**: LDPC error floor의 LETS/absorbing set 탐색 난해성 — error floor 분석/코드설계(E)에 직결, 이진 LDPC
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8667301
- **Type**: journal
- **Published**: July 2019
- **Authors**: Ali Dehghan, Amir H. Banihashemi
- **PDF**: https://ieeexplore.ieee.org/document/8667301
- **Abstract**: Leafless elementary trapping sets (LETSs) are known to be the problematic structures in the error floor region of low-density parity-check (LDPC) codes over the additive white Gaussian (AWGN) channel under iterative decoding algorithms. While problems involving the general category of trapping sets, and the subcategory of elementary trapping sets (ETSs), have been shown to be NP-hard, similar results for LETSs, which are a subset of ETSs are not available. In this paper, we prove that for a general LDPC code, finding a LETS of a given size a with minimum number of odd-degree check nodes b is NP-hard to approximate within any approximation factor. We also prove that finding the minimum size a of a LETS with a given b is NP-hard to approximate within any approximation factor. Similar results are proved for elementary absorbing sets, a popular subcategory of LETSs.

## Design of Protograph-LDPC-Based BICM-ID for Multi-Level-Cell (MLC) NAND Flash Memory

- **Status**: ✅
- **Reason**: MLC NAND 플래시 전용 protograph-LDPC BICM-ID 설계 + VS-PEXIT 알고리즘 + OARA 신규 코드 구성 (A/E 직결, 이진 LDPC)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8708250
- **Type**: journal
- **Published**: July 2019
- **Authors**: Yingcheng Bu, Yi Fang, Guojun Han +2
- **PDF**: https://ieeexplore.ieee.org/document/8708250
- **Abstract**: In this letter, the optimization of protograph-low-density parity-check (LDPC)-based bit-interleaved coded modulation with iterative detection and decoding (BICM-ID) with anti-Gray mapping is investigated over multi-level-cell (MLC) NAND flash-memory channels. Since the existing protograph-based extrinsic information transfer (PEXIT) algorithm is not applicable to the BICM-ID MLC flash-memory channels, a voltage-sensing PEXIT (VS-PEXIT) algorithm is proposed to facilitate the threshold analysis of protograph codes. Exploiting the proposed VS-PEXIT algorithm, we find that the optimal AR4JA code over AWGN channels cannot preserve its superiority over BICM-ID MLC flash-memory channels. To tackle this problem, we further propose a design scheme to construct a high-rate protograph code, referred to as optimized accumulate-repeat-accumulate (OARA) code, tailored for such scenarios. Theoretical analyses and simulation results illustrate that the proposed OARA-based BICM-ID appears to be an excellent storage scheme over MLC flash-memory channels.

## A Study on Iterative Decoding With LLR Modulator Using Neural Network in SMR System

- **Status**: ✅
- **Reason**: 신경망 기반 LLR modulator로 반복 디코딩 개선 — 부호 비의존적 LLR 보정 기법, NAND LDPC LLR 양자화/보정에 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8630047
- **Type**: journal
- **Published**: July 2019
- **Authors**: M. Nishikawa, Y. Nakamura, H. Osawa +2
- **PDF**: https://ieeexplore.ieee.org/document/8630047
- **Abstract**: This paper focuses on the shingled magnetic recording (SMR) as the recording system for further high-density hard disk drives. Previously, we applied a log-likelihood ratio (LLR) modulator to the low-density parity check coding and iterative decoding system in SMR to improve the decoding performance. In this paper, we propose a new LLR modulator using neural network. Furthermore, we clarify that the proposed LLR modulator using neural network realizes effective iterative decoding in a read/write channel with pattern-dependent medium noise.

## Belief Propagation, Bethe Approximation and Polynomials

- **Status**: ✅
- **Reason**: 이진 알파벳 BP/Bethe 근사의 정확성 이론, BP 동작 이해에 기여 가능하나 순수 이론에 가까워 애매 → 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8653402
- **Type**: journal
- **Published**: July 2019
- **Authors**: Damian Straszak, Nisheeth K. Vishnoi
- **PDF**: https://ieeexplore.ieee.org/document/8653402
- **Abstract**: Factor graphs are important models for succinctly representing probability distributions in machine learning, coding theory, and statistical physics. Several computational problems, such as computing marginals and partition functions, arise naturally when working with factor graphs. Belief propagation is a widely deployed iterative method for solving these problems. However, despite its significant empirical success, several questions regarding the correctness and efficiency of belief propagation remain open. The Bethe approximation is an optimization-based method for approximating the partition functions. While it is known that the stationary points of the Bethe approximation coincide with the fixed points of belief propagation, in general, the relation between the Bethe approximation and the partition function is not well understood. It has been observed that for a few classes of factor graphs, the Bethe approximation gives a lower bound to the partition function, which distinguishes them from the general case, where neither a lower bound nor an upper bound holds universally. This has been rigorously proved for permanents and for attractive graphical models. Here, we consider bipartite factor graphs over binary alphabet and show that if the local constraints satisfy a certain analytic property, the Bethe approximation is a lower bound to the partition function, generalizing an analogous inequality between the permanent and the Bethe permanent of a matrix with non-negative entries. We arrive at this result by viewing the factor graphs through the lens of polynomials, which allows us to reformulate the Bethe approximation as an optimization problem involving polynomials. The sufficient condition for our lower bound property to hold is inspired by the recent developments in the theory of real stable polynomials. We believe that this way of viewing factor graphs and its connection to real stability might lead to a better understanding of belief propagation and factor graphs in general.

## Quasi-Cyclic LDPC Codes for Correcting Multiple Phased Bursts of Erasures

- **Status**: ✅
- **Reason**: 바이너리 QC-LDPC 신규 구성 + Tanner 그래프 cycle/adjacency 기반 phased-burst erasure 정정, 2단 반복 디코딩 — 코드설계(E)/디코더(C) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8849853
- **Type**: conference
- **Published**: 7-12 July 
- **Authors**: Xin Xiao, Bane Vasić, Shu Lin +2
- **PDF**: https://ieeexplore.ieee.org/document/8849853
- **Abstract**: This paper presents designs and constructions of two classes of binary quasi-cyclic LDPC codes for correcting multiple random phased-bursts of erasures over the binary erasure channel. The erasure correction of codes in both classes is characterized by the cycle and adjacency structure of their Tanner graphs. Erasure correction of these codes is a very simple process which requires only modulo-2 additions. The codes in the second class are capable of correcting locally and globally distributed phased-bursts of erasures with a two-phase iterative erasure-correction process.

## Girth Properties of Time-Varying SC-LDPC Convolutional Codes

- **Status**: ✅
- **Reason**: 시변 SC-LDPC의 girth 특성 개선 신규 코드설계(E), 바이너리 LDPC 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8849323
- **Type**: conference
- **Published**: 7-12 July 
- **Authors**: Massimo Battaglioni, Marco Baldi, Franco Chiaraluce +1
- **PDF**: https://ieeexplore.ieee.org/document/8849323
- **Abstract**: Time-varying spatially-coupled low-density parity-check convolutional codes (SC-LDPC-CCs) exhibit excellent features, but their representation requires a very large number of parameters. On the other hand, the description of time-invariant SC-LDPC-CCs is very convenient and their error rate performance, though usually worse, is often satisfactory. In this paper we investigate the girth properties of these codes, showing that the time-invariant ones have some weaknesses, which can be compensated by introducing a small periodicity in the code. By considering periodically time-varying codes, we achieve considerable improvements in the girth properties using few more degrees of freedom with respect to the time-invariant case.

## Spatially Coupled LDPC Codes via Partial Superposition

- **Status**: ✅
- **Reason**: partial superposition 기반 신규 SC-LDPC 구성, 낮은 error floor·LDPC-BC HW 재사용(E/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8849384
- **Type**: conference
- **Published**: 7-12 July 
- **Authors**: Qianfan Wang, Suihua Cai, Wenchao Lin +2
- **PDF**: https://ieeexplore.ieee.org/document/8849384
- **Abstract**: In this paper, we present a new class of spatially coupled low-density parity-check (SC-LDPC) codes, which are constructed by sending codewords of LDPC block code (LDPCBC) in a block Markov superposition transmission (BMST) manner. Different from the conventional SC-LDPC codes, the proposed SC-LDPC codes can have encoder/decoder implemented with the basis of the hardware components of the corresponding LDPC-BCs. The proposed SC-LDPC codes are also a special class of BMST-LDPC codes. Distinguished from other types of BMST codes, BMST-LDPC codes have lower error floors even with an encoding memory of one and hence have lower decoding latency. Also different from the original BMST codes, partial superposition is implemented to alleviate error propagation. To analyze the bit error rate (BER) performance, we present the genie-aided (GA) bounds, which can be obtained by simulation or estimated from the performance of the basic code. Numerical results are presented to validate our analysis and demonstrate the performance advantage of the BMST-LDPC codes over the LDPC-BCs.

## AVN-based Elimination of Short Cycles in Tanner Graphs of QC LDPC Codes

- **Status**: ✅
- **Reason**: 바이너리 QC-LDPC 단주기 사이클 제거 AVN-RPC 신규 기법 + 개선된 반복 디코딩(C/E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8849632
- **Type**: conference
- **Published**: 7-12 July 
- **Authors**: Irina E. Bocharova, Boris D. Kudryashov, Vitaly Skachek
- **PDF**: https://ieeexplore.ieee.org/document/8849632
- **Abstract**: One of the most efficient approaches to improving the frame error rate (FER) performance of low-density parity-check (LDPC) codes is based on adding both auxiliary variable nodes (AVN) and the corresponding redundant parity checks (RPC) to the binary parity-check matrices of the code. It is known that for the LDPC codes, whose Tanner graphs contain length four cycles, this technique allows for substantial improvement in the FER performance of the belief-propagation (BP) decoding on the binary erasure channel (BEC) channel. The AVN-based technique followed by adding orthogonal redundant parity-checks is known to be efficient for both the BEC and additive white Gaussian noise (AWGN) channels. In this paper, firstly, the AVN-based approach is generalized to efficiently removing cycles of length larger than four. Secondly, the AVN-based technique is reformulated in terms of labeled base matrices of quasi-cyclic (QC) LDPC codes. An improved iterative decoding of QC LDPC codes is proposed, which is applied to the labeled base matrices of QC LDPC codes extended by the AVN-RPC technique.

## A Modified Min-Sum Algorithm for Quantized LDPC Decoders

- **Status**: ✅
- **Reason**: 양자화 바이너리 LDPC 디코더용 신규 MSA 변형(error floor 저감), NAND ECC에 직결되는 이식 가능 디코더(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8849308
- **Type**: conference
- **Published**: 7-12 July 
- **Authors**: Homayoon Hatami, David G. M. Mitchell, Daniel J. Costello +1
- **PDF**: https://ieeexplore.ieee.org/document/8849308
- **Abstract**: It is well known that for decoding low-density parity-check (LDPC) codes, the attenuated min-sum algorithm (AMSA) and the offset min-sum algorithm (OMSA) can outperform the conventional min-sum algorithm (MSA) at low signal-to-noise-ratios (SNRs). In this paper, we demonstrate that, for quantized LDPC decoders, although the MSA achieves better high SNR performance than the AMSA and OMSA, each of the MSA, AMSA, and OMSA all suffer from a relatively high error floor. Therefore, we propose a novel modification of the MSA for decoding quantized LDPC codes with the aim of lowering the error floor. Compared to the quantized MSA, the proposed modification is also helpful at low SNRs, where it matches the waterfall performance of the quantized AMSA and OMSA. The new algorithm is designed based on the assumption that trapping/absorbing sets (or other problematic graphical objects) are the major cause of the error floor for quantized LDPC decoders, and it aims to reduce the probability that these problematic objects lead to decoding errors.

## LDPC Codes for Portable DNA Storage

- **Status**: ✅
- **Reason**: 바이너리 LDPC + turbo-like 디코더를 DNA 스토리지 채널에 설계 — 스토리지 ECC(B)/이식 가능 디코더(C) 가능성, 애매하므로 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8849814
- **Type**: conference
- **Published**: 7-12 July 
- **Authors**: Peng Fei, Zhiying Wang
- **PDF**: https://ieeexplore.ieee.org/document/8849814
- **Abstract**: DNA becomes an attractive storage medium in recent years for its ultra-high density, millennial-long endurance, and efficient replication. In this work we consider DNA storage that uses the affordable and portable nanopore sequencing as the reading mechanics. Unlike traditional data storage systems, errors occur asymmetrically among the four types of nucleotide bases of DNA. Quaternary codes can be employed for error correction, but suffer from high complexity. In this paper, we design binary LDPC codes with a turbo-like decoder for the DNA storage channel. Simulation results show that our binary LDPC codes have a similar bit-error rate but with a speed up by a factor of 4 compared to quaternary codes.

## On Decoding Random-Access SC-LDPC Codes

- **Status**: ✅
- **Reason**: 데이터스토리지 동기 SC-LDPC의 신규 semi-global 디코딩 전략(B/C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8849558
- **Type**: conference
- **Published**: 7-12 July 
- **Authors**: Eshed Ram, Yuval Cassuto
- **PDF**: https://ieeexplore.ieee.org/document/8849558
- **Abstract**: We study a new decoding strategy of multi-block SC-LDPC codes motivated by data-storage applications. To decode a sub-block out of the full code block, our proposed decoder accesses a small number of sub-blocks around the desired sub-block. We call this decoding strategy "semi-global decoding", and parametrize it by its access cost: the number of accessed sub-blocks. We provide a theoretical characterization of decoding performance, and evaluate this performance for random-access SC-LDPC ensembles.

## Convolutional LPDC codes for Distributed Storage Systems

- **Status**: ✅
- **Reason**: B/E: 분산저장용 binary erasure channel convolutional LDPC, message passing 디코더+패리티검사 행렬 구성, 스토리지 ECC/코드설계 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8849292
- **Type**: conference
- **Published**: 7-12 July 
- **Authors**: Roberta Barbi, Pascal Felber, Laurent Hayez +1
- **PDF**: https://ieeexplore.ieee.org/document/8849292
- **Abstract**: We study convolutional LDPC codes over the binary erasure channel for immutable distributed storage systems. These codes allow the archival of data objects in a sequential fashion on an increasing number of storage nodes as they arrive in the system, as well as fast repair using a simple message passing decoder. We further target systematic codes, high code rates and low locality, which are paramount in this setting. We describe a family of codes that split each archived data object in s blocks, entangle them with t = s + p blocks already archived, and generate p parity blocks per archived data object. We carefully choose the parity-check matrix and the blocks already archived to maximize the repair capability of the resulting codes, and describe the best constructions for 1 ≤ s ≤ 5 and p = 2. A Markov analysis shows that for the same storage overhead, our codes are orders of magnitude more reliable than state-of-the-art Reed-Solomon and locally repairable codes.

## Deep Learning-Aided Trainable Projected Gradient Decoding for LDPC Codes

- **Status**: ✅
- **Reason**: C: LDPC용 신경망 기반 trainable projected gradient 디코더, BP 초과 성능, 신경망 디코더로 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8849215
- **Type**: conference
- **Published**: 7-12 July 
- **Authors**: Tadashi Wadayama, Satoshi Takabe
- **PDF**: https://ieeexplore.ieee.org/document/8849215
- **Abstract**: We present a novel optimization-based decoding algorithm for LDPC codes that is suitable for hardware architectures specialized to feed-forward neural networks. The algorithm is based on the projected gradient descent algorithm with a penalty function for solving a non-convex minimization problem. The proposed algorithm has several internal parameters such as step size parameters, a softness parameter, and the penalty coefficients. We use a standard tool set of deep learning, i.e., back propagation and stochastic gradient descent type algorithms, to optimize these parameters. Several numerical experiments show that the proposed algorithm outperforms the belief propagation decoding in some cases.

## Linear Permutation Polynomial Codes

- **Status**: ✅
- **Reason**: QC-LDPC girth-12 한계 돌파하는 신규 LPP 코드 구성(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8849422
- **Type**: conference
- **Published**: 7-12 July 
- **Authors**: Ryoichiro Yoshida, Kenta Kasai
- **PDF**: https://ieeexplore.ieee.org/document/8849422
- **Abstract**: Quasi-cyclic low-density parity-check (QC-LDPC) codes are one of the most important code classes of LDPC codes. They have two drawbacks: lack of randomness and limited girth lead to a degraded decoding performance in the waterfall and error floor regions, respectively. To tackle these problems, we present a new class of LDPC codes, named linear permutation polynomial (LPP) codes, whose parity-check matrix consists of permutation matrices based on LPPs. The girth of regular QC-LDPC codes is upper bounded by 12, while LPP codes break this limit. We demonstrate that LPP codes have error performance almost equivalent to random ones.

## A simplified LLR of SD-LDPC for probabilistically shaped QAM constellation

- **Status**: ✅
- **Reason**: PS-QAM용 단순화된 LLR 계산을 LDPC 디코딩에 적용 — LLR 양자화/계산 단순화는 NAND LDPC 디코더(C)에 이식 여지, 애매하므로 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8818080
- **Type**: conference
- **Published**: 7-11 July 
- **Authors**: Wenjing Zhang, Shaohua Hu, Jing Zhang +2
- **PDF**: https://ieeexplore.ieee.org/document/8818080
- **Abstract**: We present a simplified log likelihood ratio (LLR) for LDPC decoding and compare the post-FEC BER performances of PS-16QAM in coherent optical communications systems. The improvement of post-FEC BER is 1.17dB for PS-16QAM.

## Constructing QC-LDPC codes based on dimension reduction for physical layer security

- **Status**: ✅
- **Reason**: QC-LDPC base matrix 구성+사이클 제거 알고리즘, 코드설계(E) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8969774
- **Type**: conference
- **Published**: 29 June-3 
- **Authors**: Manfei Zhang, Renyong Wu
- **PDF**: https://ieeexplore.ieee.org/document/8969774
- **Abstract**: As a recently proposed physical layer security scheme, the two-dimensional transmission scheme prevents eavesdropping, but the bit error rate (BER) of the receiver becomes high. A new coding scheme for Quasi-Cyclic Low-Density Parity-Check (QC-LDPC) codes to improve the performance of the receiver is proposed and named as dimension reduction coding. This new scheme constructs the base matrix, which is necessary to obtain the parity check matrix of QC-LDPC codes, from the channel coefficient matrix of two-dimensional transmission scheme. Then, by analyzing the relationship between the base matrix and the parity check matrix of QC-LDPC codes, we find out the conditions that the base matrix must satisfy so that the corresponding parity check matrix has no shortest cycle in Tanner graph. Furthermore, a dimension reduction algorithm is presented to modify the base matrix and obtain parity check matrices with good performance. Finally, simulation results are given and validate the feasibility of this method.

## A Check Nodes Correction Approximate Min-sum Decoding Algorithm For LDPC

- **Status**: ✅
- **Reason**: C/D: check-node correction approximate Min-sum 디코딩 신규 알고리즘, HW 친화(shifter+adder), BER/iteration 개선 — NAND LDPC 디코더 직접 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8835237
- **Type**: conference
- **Published**: 24-26 July
- **Authors**: Ruizhen Wu, Lin Wang, Tao Yuan +1
- **PDF**: https://ieeexplore.ieee.org/document/8835237
- **Abstract**: A check nodes correction approximate Min-sum decoding algorithm for LDPC is proposed in this paper. The degradation factor of BP to MS is found to do expansion and optimization based on hardware working manner. The decoding algorithm summarized a correction approximate algorithm based on different SNR situations and hardware implementation. The simulation is based on LDPC NR 3GPP 38.212 release and the comparison results showed the proposed check nodes correction approximate Min-sum decoding algorithm can have a better BER and iteration time performance. The hardware of this proposed algorithm is based on Min-sum decoder and the extra cost is only a shifter and an adder besides the memory.

## Lowered-Complexity Decoding Algorithms of LDPC Codes for Agricultural-WSNs

- **Status**: ✅
- **Reason**: 패턴기반 XOR 저복잡도 LDPC 디코딩 알고리즘 제안, 바이너리 LDPC 디코더(C) 이식 여지로 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8806113
- **Type**: conference
- **Published**: 2-5 July 2
- **Authors**: Dong-Hee Noh, Sung-Hwan Jeong, Ju-Hwan Choi +1
- **PDF**: https://ieeexplore.ieee.org/document/8806113
- **Abstract**: This paper proposes a pattern based Low-density parity-check (LDPC) codes scheme to reduce the decoding complexity using logical XOR. New approaches to this paper describe the pattern based encoder which using logical XOR operation. The proposed scheme can reduce iteration, complexity and packet errors while decoding procedures. It can obtain enhanced throughput performance and at receiver sides in several Signal to Noise Ratio (SNR) levels. Simulation results show that the proposed method can improve the throughput and transmission delay for wireless sensor networks.

## Guessing the Code: Learning Encoding Mappings Using the Back Propagation Algorithm

- **Status**: ✅
- **Reason**: backprop 신경망으로 바이너리 LDPC 패리티검사식 학습, 신경망 디코더(C) 인접—Phase3 재검토
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8852203
- **Type**: conference
- **Published**: 14-19 July
- **Authors**: Amrutha Machireddy, Shayan Srinivasa Garani
- **PDF**: https://ieeexplore.ieee.org/document/8852203
- **Abstract**: Error correction codes such as low density parity check (LDPC) codes are popularly used to enhance the performance of digital communication systems. The current decoding framework relies on exchanging beliefs over a Tanner graph, which the encoder and decoder are aware of. However, this information may not be available readily, for example in covert communication. The main idea of this paper is to build a neural network to learn the encoder mappings in the absence of knowledge of the Tanner graph. We propose a scheme to learn the mappings using the back propagation algorithm. We investigate into the choice of different cost functions and the number of hidden neurons for learning the encoding function. The proposed scheme is capable of learning the parity check equations over a binary field towards identifying the validity of a codeword. Simulation results over synthetic data show that our algorithm is indeed capable of learning the encoder mappings and identifying the parity check equations.

## Construction of High Performance Block and Convolutional Multi-Edge Type QC-LDPC codes

- **Status**: ✅
- **Reason**: MET QC-LDPC 블록/콘볼루션 부호 구성(code sieving, SA lifting, EMD 최대화) + 양자화 box-plus 디코더 — 코드설계(E)/디코더(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8769083
- **Type**: conference
- **Published**: 1-3 July 2
- **Authors**: Vasiliy Usatyuk, Ilya Vorobyev
- **PDF**: https://ieeexplore.ieee.org/document/8769083
- **Abstract**: We present code sieving method for construction of long-length high performance Block and Convolutional Multi-Edge Type QC-LDPC codes (MET QC-LDPCC) under the fixed point (Quantized) reduced complexity box-plus (QRCBP) decoder. Proposed method use iterative decoding threshold protograph sieving and simulated annealing method for QC lifting with cycles EMD maximization. Using proposed method we construct base matrix of MET-LDPC code with size 92 20, maximal column weight 17, with weight one circulants, code rate 0.8, 2 variable nodes punctured which have iterative decoding threshold Eb/No = 2.333 dB under 200 iterations of QRCBP over an AWGN channel with QPSK modulation on Bit Error Rate below 10-, 0.289 dB from Shannon limit. Simulation results of Block with code length N = 261924 and MET QC-LDPCC codes, equivalent block length N = 785772 constructed using simulated annealing lifting of base matrix under 32 iterations of QRCBP show Eb/No = 2.56dB, Eb/No = 2.478dB below BER10-15, respectively. Cole's importance sampling under QRCBP show that proposed codes error-floor BER ≈ 10-16.

## Cost-effective Resilient FPGA-based LDPC Decoder Architecture

- **Status**: ✅
- **Reason**: FPGA LDPC 디코더 결함내성 아키텍처(설정메모리 SEU 특성화 + 비용효율 fault tolerance) — 이식 가능 HW 아키텍처(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:8854457
- **Type**: conference
- **Published**: 1-3 July 2
- **Authors**: Eduardo N. de Souza, Gabriel L. Nazar
- **PDF**: https://ieeexplore.ieee.org/document/8854457
- **Abstract**: Low-Density Parity-Check (LDPC) codes have been used in many communication standards due to their capacity-approaching performance with feasible decoding architectures. Field-Programmable Gate Arrays (FPGAs) have been shown to be appropriate for the implementation of LDPC decoders, due to their ability to exploit the fine-grained parallelism found in such codes, as well as due to their reconfigurability, which allows to easily adapt the decoder to different codes. The susceptibility of FPGAs to faults affecting their configuration memories, however, demands specific fault tolerance strategies when these devices are used in harsh environments, such as aerospace applications, or even in ground-level critical systems. Thus, in this work we present a characterization of the behavior of LDPC decoders when subject to configuration errors and show that a single error can substantially degrade decoding performance, differently from what is observed in application-specific circuits. Based on this characterization, we propose a cost-effective fault tolerance scheme able to cope with faults in the FPGA fabric. Identifying the most critical components allowed reducing performance degradation by 89 % while only covering 55 % of their area.

## Concatenated Error Correction Code Implementation on FPGA

- **Status**: ✅
- **Reason**: DVB-S2 LDPC 내부부호 FPGA codec 구현(아키텍처/처리율 향상) — RS는 외부 cascade지만 LDPC 디코더 HW 기여 있음(D), 애매하므로 in
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:8814048
- **Type**: conference
- **Published**: 1-3 July 2
- **Authors**: M. Y. Zinchenko, A. M. Levadniy, Y. A. Grebenko
- **PDF**: https://ieeexplore.ieee.org/document/8814048
- **Abstract**: The requirements of highly reliable data transmission over interference and noisy channels are imposed on modern radio communication systems. In this connection, forward error correction has become an indispensable step in the digital processing of information data during transmission. Today there are a large number of FEC codes, one of the most popular are low density parity check codes (LDPC). The paper presents the results of the development of the FPGA cascade codec with the internal LDPC code of the DVB-S2 standard and the external Reed-Solomon code. The use of the cascade encoding method allows to get rid of residual errors arising from the decoding of LDPC-code. The developed architectures, methods for increasing productivity and the used FPGA resources are presented.
