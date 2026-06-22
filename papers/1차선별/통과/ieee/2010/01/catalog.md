# IEEE Xplore — 2010-01 (1차선별 통과)


## Multilevel LDPC-Coded High-Speed Optical Systems: Efficient Hard Decoding and Code Optimization

- **Status**: ✅
- **Reason**: 신규 LDPC 하드디시전 디코더(Gallager-B 등가, 노드차수 불필요로 회로효율↑) 제안 — 이식 가능 디코더(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5342472
- **Type**: journal
- **Published**: Sept.-Oct.
- **Authors**: Chen Gong, Xiaodong Wang
- **PDF**: https://ieeexplore.ieee.org/document/5342472
- **Abstract**: We consider a multilevel coding scheme employing low-density parity-check (LDPC) codes and high-order modulations for high-speed optical transmissions, where the coherent receiver performs either parallel independent decoding (PID) or multistage decoding (MSD). To meet the severe complexity constraint imposed by the ultrahigh data rate of the emerging optical transmission systems, we focus on hard-decision decoding of LDPC codes. A new LDPC hard decoding method is developed, which is equivalent to the Gallager decoding algorithm B, but is more efficient in terms of circuit implementation, since no variable node degree information is needed. Two variants of this decoder is also proposed, which offers significant performance gain for finite-length codes. We optimize the system by allocating rates and designing profiles for component codes. Both numerical evaluations and simulation results show that the optimized multilevel coding systems with either PID or MSD substantially outperform the optimized single-level LDPC-coded system.

## An implementation-friendly binary LDPC decoding algorithm

- **Status**: ✅
- **Reason**: 구현친화적 바이너리 LDPC 메시지패싱 디코더(degree-free, 회로구현 지향)—이식 가능 디코더/HW(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5397903
- **Type**: journal
- **Published**: January 20
- **Authors**: Guosen Yue, Xiaodong Wang
- **PDF**: https://ieeexplore.ieee.org/document/5397903
- **Abstract**: We introduce an implementation-friendly binary message-passing decoding method for low-density parity-check (LDPC) codes that does not require the degree information of variable nodes or degree dependent parameters. For hard decision decoding, given its low-complexity, the implementation cost for variable node degree information is an important consideration. We develop an estimation method for the extrinsic error probability (EEP) as well as its analysis. The proposed method offers similar performance as the existing methods for time-invariant decoding in most cases, while it facilitates efficient circuit implementations of the LDPC decoder.

## Min-Sum Decoder Architectures With Reduced Word Length for LDPC Codes

- **Status**: ✅
- **Reason**: 정규화 min-sum 개선(2개 보정인자)+비균일 양자화로 워드길이 축소, LLR 양자화·디코더 알고리즘·메모리 면적 절감은 NAND LDPC ECC에 직접 이식 가능(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4787066
- **Type**: journal
- **Published**: Jan. 2010
- **Authors**: Daesun Oh, Keshab K. Parhi
- **PDF**: https://ieeexplore.ieee.org/document/4787066
- **Abstract**: In this paper, we propose an improvement of the normalized min-sum (MS) decoding algorithm and novel MS decoder architectures with reduced word length using nonuniform quantization schemes for low-density parity-check (LDPC) codes. The proposed normalized MS algorithm introduces a more exact adjustment with two optimized correction factors for check-node-updating computations, while the conventional normalized MS algorithm applies only one correction factor. The proposed algorithm provides a significant performance gain without any additional computation or hardware complexity. The finite word-length analysis in implementing an LDPC decoder is a very important factor since it directly impacts the size of memory to store the intrinsic and extrinsic messages and the overall hardware area in the partially parallel LDPC decoder. The proposed nonuniform quantization scheme can reduce the finite word length while achieving similar performances compared to a conventional quantization scheme. From simulation results, it is shown that the proposed 4-bit nonuniform quantization scheme achieves an acceptable decoding performance, unlike the conventional 4-bit uniform quantization scheme. Finally, the proposed MS decoder architectures by the nonuniform quantization scheme provide significant reductions of 20% and up to 8% for the memory area and combinational logic area, respectively, compared to the conventional 5-bit ones.

## Flexible LDPC Decoder Design for Multigigabit-per-Second Applications

- **Status**: ✅
- **Reason**: single-min min-sum+비균일 양자화+configurable permutation network(Benes)의 고처리율 VLSI 디코더 — 디코더/HW 기법 NAND 이식 가능(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4804639
- **Type**: journal
- **Published**: Jan. 2010
- **Authors**: Chuan Zhang, Zhongfeng Wang, Jin Sha +2
- **PDF**: https://ieeexplore.ieee.org/document/4804639
- **Abstract**: Low-density parity-check (LDPC) codes are one of the most promising error-correcting codes approaching Shannon capacity and have been adopted in many applications. However, the efficient implementation of high-throughput LDPC decoders adaptable for various channel conditions still remains challenging. In this paper, a low-complexity reconfigurable VLSI architecture for high-speed LDPC decoders is presented. Shift-LDPC codes are incorporated within the design and have shown not only comparable decoding performance to computer-generated random codes but also high hardware efficiency in high-speed applications. The single-minimum Min-Sum decoding scheme and the nonuniform quantization scheme are explored to reduce the complexity of computing core and the memory requirement. The well-known Benes network is employed to construct the configurable permutation network to support multiple shift-LDPC codes with various code parameters. The ASIC implementation results of an (8192, 7168) (4, 32)-regular shift-LDPC decoder demonstrate a maximum decoding throughput of 3.6 Gbits/s at 16 iterations, which outperforms the state-of-the-art design for high-speed flexible LDPC decoders by many times with even less hardware.

## Linear Time Encoding of LDPC Codes

- **Status**: ✅
- **Reason**: 임의 바이너리 LDPC의 선형복잡도 인코딩 기법(label-and-decide) — 코드설계/구현(D/E)으로 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5361490
- **Type**: journal
- **Published**: Jan. 2010
- **Authors**: Jin Lu, JosÉ M. F. Moura
- **PDF**: https://ieeexplore.ieee.org/document/5361490
- **Abstract**: In this paper, we propose a linear complexity encoding method for arbitrary LDPC codes. We start from a simple graph-based encoding method ¿label-and-decide.¿ We prove that the ¿label-and-decide¿ method is applicable to Tanner graphs with a hierarchical structure-pseudo-trees-and that the resulting encoding complexity is linear with the code block length. Next, we define a second type of Tanner graphs-the encoding stopping set. The encoding stopping set is encoded in linear complexity by a revised label-and-decide algorithm-the ¿label-decide-recompute.¿ Finally, we prove that any Tanner graph can be partitioned into encoding stopping sets and pseudo-trees. By encoding each encoding stopping set or pseudo-tree sequentially, we develop a linear complexity encoding method for general low-density parity-check (LDPC) codes where the encoding complexity is proved to be less than 4 ·M ·((k¿- 1), where M is the number of independent rows in the parity-check matrix and k¿ represents the mean row weight of the parity-check matrix.

## Analysis of Absorbing Sets and Fully Absorbing Sets of Array-Based LDPC Codes

- **Status**: ✅
- **Reason**: array-based 바이너리 LDPC의 absorbing set/error floor 정량 분석 및 열거 기법 — 코드설계(E)로 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5361488
- **Type**: journal
- **Published**: Jan. 2010
- **Authors**: Lara Dolecek, Zhengya Zhang, Venkat Anantharam +2
- **PDF**: https://ieeexplore.ieee.org/document/5361488
- **Abstract**: The class of low-density parity-check (LDPC) codes is attractive, since such codes can be decoded using practical message-passing algorithms, and their performance is known to approach the Shannon limits for suitably large block lengths. For the intermediate block lengths relevant in applications, however, many LDPC codes exhibit a so-called “error floor,” corresponding to a significant flattening in the curve that relates signal-to-noise ratio (SNR) to the bit-error rate (BER) level. Previous work has linked this behavior to combinatorial substructures within the Tanner graph associated with an LDPC code, known as (fully) absorbing sets. These fully absorbing sets correspond to a particular type of near-codewords or trapping sets that are stable under bit-flipping operations, and exert the dominant effect on the low BER behavior of structured LDPC codes. This paper provides a detailed theoretical analysis of these (fully) absorbing sets for the class of $C_{p, \gamma}$ array-based LDPC codes, including the characterization of all minimal (fully) absorbing sets for the array-based LDPC codes for $\gamma = 2,3,4$, and moreover, it provides the development of techniques to enumerate them exactly. Theoretical results of this type provide a foundation for predicting and extrapolating the error floor behavior of LDPC codes.

## Low-Complexity Switch Network for Reconfigurable LDPC Decoders

- **Status**: ✅
- **Reason**: reconfigurable LDPC용 저복잡도 switch network(barrel shifter/permutation) HW 아키텍처 — NAND LDPC 디코더 permutation network에 이식 가능(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:4806138
- **Type**: journal
- **Published**: Jan. 2010
- **Authors**: Daesun Oh, Keshab K. Parhi
- **PDF**: https://ieeexplore.ieee.org/document/4806138
- **Abstract**: In this paper, we propose an efficient low-complexity switch network design for reconfigurable low-density parity-check (LDPC) decoders. The proposed architecture leads to significant reductions in hardware complexity. Since the structured quasi-cyclic (QC) LDPC codes for most modern wireless communication systems include multiple code rates, various block lengths, and different sizes of submatrices, a reconfigurable LDPC decoder is desirable and the barrel shifter needs to be programmable. The Benes network cannot be optimized as the barrel shifter for a reconfigurable LDPC decoder when the input size of barrel shifter is not a power of 2. Also, it is not trivial to generate all the control signals on-the-fly for numerous 2 × 2 switches in the switch network. In this paper, a novel low-complexity switch network design is proposed, which can be used efficiently when the input size of barrel shifters is not a power of 2. Furthermore, we propose a novel algorithm to generate all the control signals, which can be implemented with a small size of lookup table (LUT) or a simple combination logic on-the-fly, using the properties that both the full-size switch network can be broken into two half-size switch networks and the barrel shifters for the structured QC LDPC decoders require only cyclic shifts. Compared with conventional Benes networks using a dedicated LUT or a complicated signal generating algorithm, the proposed architectures achieve significant hardware reductions in implementing the barrel shifters for reconfigurable LDPC decoders. In synthesis result using the TSMC 0.18-¿m standard cell CMOS technology, the proposed switch network for a reconfigurable LDPC decoder of IEEE 802.16e and IEEE 802.11n can be implemented with an area of 0.772 mm2, which leads to a significant area reduction.

## Programmable Architecture for Flexi-Mode QC-LDPC Decoder Supporting Wireless LAN/MAN Applications and Beyond

- **Status**: ✅
- **Reason**: flexi-mode QC-LDPC 디코더 프로그래머블 아키텍처+알고리즘 수정으로 복잡도 감소+early stopping, HW 디코더 기법 이식 가능(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:4806043
- **Type**: journal
- **Published**: Jan. 2010
- **Authors**: Dan Bao, Bo Xiang, Rui Shen +3
- **PDF**: https://ieeexplore.ieee.org/document/4806043
- **Abstract**: A programmable architecture is proposed for a flexi-mode quasi-cyclic low-density parity-check code decoder. The proposed architecture has the following advantages: 1) Code rate, length, and pattern can be programmed on the fly; 2) decoding complexity is reduced by algorithm modification; 3) memory read/write operation is reduced by access optimization and hierarchical memory structure; and 4) an early stopping scheme is adopted to give power efficiency, particularly in the low-signal-to-noise-ratio region. A decoder chip is implemented in an SMIC 180-nm 1.8-V CMOS technology. Experimental results show the advantages in terms of flexibility, area, power, and error-correction performance.

## Using Embedded Dynamic Random Access Memory to Reduce Energy Consumption of Magnetic Recording Read Channel

- **Status**: ✅
- **Reason**: eDRAM로 반복 검출/코딩 디코더 에너지·면적 절감 — 메모리 집약적 iterative LDPC 디코더 HW 에너지 최적화 기법, NAND 디코더 메모리 설계에 이식 가능(D, 애매하면 in)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:5357506
- **Type**: journal
- **Published**: Jan. 2010
- **Authors**: Ningde Xie, Tong Zhang, Erich F. Haratsch
- **PDF**: https://ieeexplore.ieee.org/document/5357506
- **Abstract**: Although the performance of a magnetic recording read channel can be improved by employing advanced iterative signal detection and coding techniques, the method nevertheless tends to incur significant silicon area and energy consumption overhead. Motivated by recent significant improvement of high-density embedded dynamic random access memory (eDRAM) towards high manufacturability at low cost, we explored the potential of integrating eDRAM in read channel integrated circuits (IC) to minimize the silicon area and energy consumption cost incurred by iterative signal detection and coding. As a result of the memory-intensive nature of iterative signal detection and coding algorithms, the silicon cost can be reduced in a straightforward manner by directly replacing conventional SRAM with eDRAM. However, reducing the energy consumption may not be trivial. In this paper, we present two techniques that trade eDRAM storage capacity to reduce the energy consumption of iterative signal detection and coding datapath. We have demonstrated dDRAM's energy saving potential by designing a representative iterative read channel at the 65 nm technology node. Simulation shows that we can eliminate over 99.99% of post-processing computation for dominant error events detection, and achieve up to a 67% reduction of decoding energy consumption.

## Analysis of peeling decoder for MET ensembles

- **Status**: ✅
- **Reason**: MET ensemble peeling decoder 분석을 유한길이 LDPC 거동 연구로 일반화 - 바이너리 LDPC 코드설계(E)에 이식 가능한 분석 기법
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5503138
- **Type**: conference
- **Published**: 6-8 Jan. 2
- **Authors**: Ryan W. Hinton, Stephen G. Wilson
- **PDF**: https://ieeexplore.ieee.org/document/5503138
- **Abstract**: The peeling decoder introduced by Luby, et al. allows analysis of LDPC decoding for the binary erasure channel (BEC). For irregular ensembles, they analyze the decoder state as a Markov process and present a solution to the differential equations describing the process mean. Multi-edge type (MET) ensembles allow greater precision through specifying graph connectivity. We generalize the the peeling decoder for MET ensembles and derive analogous differential equations. We offer a new change of variables and solution to the node fraction evolutions in the general (MET) case. This result is preparatory to investigating finite-length ensemble behavior.

## Performance analysis of iterative decoding algorithms with memory

- **Status**: ✅
- **Reason**: 메모리 있는 반복 디코딩(SR-BP/MS, DD-BMP) density evolution 분석 - 바이너리 LDPC용 디코더 알고리즘 분석/변형(C) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5503202
- **Type**: conference
- **Published**: 6-8 Jan. 2
- **Authors**: Emil Janulewicz, Amir H. Banihashemi
- **PDF**: https://ieeexplore.ieee.org/document/5503202
- **Abstract**: Density evolution is often used to determine the performance of an ensemble of low-density parity-check (LDPC) codes under iterative message-passing algorithms. Conventional density evolution techniques over memoryless channels are based on the independence assumption amongst all the processed messages in variable and check nodes. This assumption is valid for many algorithms such as standard belief propagation (BP) and min-sum (MS) algorithms. However, there are other important iterative algorithms such as successive relaxation (SR) versions of BP and MS, and differential decoding with binary message passing (DD-BMP) algorithm of Mobini et. al., for which this assumption is not valid. The dependence created among messages for these algorithms is due to the introduction of memory in the iterative algorithm. In this work, we propose a model for iterative decoding algorithms with memory which covers SR and DD-BMP algorithms as special cases. Based on this model, we derive a Bayesian network for iterative algorithms with memory over memoryless channels and use this representation to analyze the algorithms using density evolution. The density evolution technique is developed based on truncating the memory of the decoding process and approximating it with a finite order Markov process, and can be implemented efficiently. As an example, we apply our technique to analyze the performance of DD-BMP on regular LDPC code ensembles, and make a number of interesting observations with regard to the performance/complexity trade off of DD-BMP in comparison with BP and MS algorithms.

## Windowed erasure decoding of LDPC Convolutional Codes

- **Status**: ✅
- **Reason**: LDPC Convolutional code의 windowed decoding으로 latency-성능 trade-off 및 수정 구성 제시 - 바이너리 SC-LDPC 코드설계/디코더(C/E) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5503166
- **Type**: conference
- **Published**: 6-8 Jan. 2
- **Authors**: Marco Papaleo, Aravind R. Iyengar, Paul H. Siegel +2
- **PDF**: https://ieeexplore.ieee.org/document/5503166
- **Abstract**: We consider windowed decoding of LDPC Convolutional Codes on the Binary Erasure Channel (BEC) to study the trade-off between the decoding latency and the code performance. We make some key observations about regular LDPC Convolutional code ensembles under windowed decoding and give modified constructions of these codes that allow us to efficiently trade-off performance for gains in latency.

## Pseudo Prior Belief Propagation for densely connected discrete graphs

- **Status**: ✅
- **Reason**: dense loopy 그래프용 Pseudo Prior BP - BP를 dense/short-loop 환경에서 개선하는 부호 비의존 메시지패싱 기법(C), 바이너리 LDPC BP 이식 가능성 애매하여 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5503198
- **Type**: conference
- **Published**: 6-8 Jan. 2
- **Authors**: Jacob Goldberger, Amir Leshem
- **PDF**: https://ieeexplore.ieee.org/document/5503198
- **Abstract**: This paper proposes a new algorithm for the linear least squares problem where the unknown variables are constrained to be in a finite set. The factor graph that corresponds to this problem is very loopy; in fact, it is a complete bipartite graph. Hence, applying the Belief Propagation (BP) algorithm yields very poor results. The Pseudo Prior Belief Propagation (PPBP) algorithm is a variant of the BP algorithm that can achieve near maximum likelihood (ML) performance with low computational complexity. First, we use the minimum mean square error (MMSE) detection to yield a pseudo prior information on each variable. Next we integrate this information into a loopy Belief Propagation (BP) algorithm as a pseudo prior. We show that, unlike current paradigms, the Belief Propagation (BP) algorithm can be advantageous even for dense graphs with many short loops. The performance of the proposed algorithm is demonstrated on the MIMO detection problem based on simulation results.

## A message-passing algorithm for counting short cycles in a graph

- **Status**: ✅
- **Reason**: 그래프 short cycle 개수를 세는 message-passing 알고리즘 - LDPC girth/사이클 제거 코드설계(E)에 직접 이식 가능, 바이너리 적용
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5503171
- **Type**: conference
- **Published**: 6-8 Jan. 2
- **Authors**: Mehdi Karimi, Amir H. Banihashemi
- **PDF**: https://ieeexplore.ieee.org/document/5503171
- **Abstract**: This paper presents a distributed message-passing algorithm for counting short cycles in a graph. For bipartite graphs, which are of particular interest in coding, the algorithm is capable of counting cycles of length g; g+2; ... ; 2g-2, where g is the girth of the graph. For a general (non-bipartite) graph, cycles of length g; g+1; ... ; 2g-1 can be counted. The algorithm is based on performing integer additions and subtractions in the nodes of the graph and passing extrinsic messages to adjacent nodes. The complexity of the proposed algorithm grows as O(g|E|2), where |E| is the number of edges in the graph. For sparse graphs, the proposed algorithm significantly outperforms the existing algorithms in terms of computational complexity and memory requirements.

## Common architecture for decoding turbo and LDPC codes

- **Status**: ✅
- **Reason**: convolutional/turbo를 sparse parity-check 그래프로 보고 BP 메시지패싱 디코딩 공통 아키텍처 제안, 부호 비의존 BP 기법 이식 가능(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5430239
- **Type**: conference
- **Published**: 29-31 Jan.
- **Authors**: T. S. V. Gautham, Andrew Thangaraj, Devendra Jalihal
- **PDF**: https://ieeexplore.ieee.org/document/5430239
- **Abstract**: Turbo codes and Low Density Parity Check (LDPC) codes have been shown to be practical codes that can approach Shannon capacity in several communication systems. In terms of performance and implementation complexity, LDPC codes and turbo codes are highly comparable, especially at coding rates around 1/2. In many recent wireless standards such as 3GPP LTE and WiMax, both turbo and LDPC codes have been recommended at the encoder. However, the decoder for turbo codes involves trellises and the BCJR algorithm, while the decoder for LDPC codes uses sparse graphs and the message passing algorithm. Therefore, in several implementations, a designer is forced to implement either the turbo decoder or the LDPC decoder. The main idea behind this work is to enable the implementation of both decoders using a common architecture. We view the constituent convolutional code in a turbo code as a block code, and construct a sparse parity check matrix for it. Then, the sparse matrix and the associated bipartite graph are used for decoding the convolutional code by soft message passing algorithms. Simulation results show a manageable degradation in performance with a reduction in complexity.

## Prolongation of Lifetime and the Evaluation Method of Dependable SSD

- **Status**: ✅
- **Reason**: SSD/플래시 직접(A) 신뢰성·error control 다룸, 애매하여 살림 (LDPC 디코더 기법 여부 Phase3 재검토)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5634934
- **Type**: conference
- **Published**: 2010
- **Authors**: K. Tai, M. Kitakami
- **PDF**: https://ieeexplore.ieee.org/document/5634934
- **Abstract**: Since high-density flash memory has high error rate, strong error control is necessary for the solid-state drive (SSD). The number of erasure cycles of each memory cell is limited, where the cell should be erased before writing. Wear-leveling is used for leveling the erasure cycles in a flash memory. Since the existing wear-leveling is executed in a chip, it is not effective if write operations are concentrated into specified chips. This paper proposes wear-leveling and error control method by using redundant flash memories in order to improve reliability and lifetime of the SSD. In the proposed method, error control is usually executed, and wear-leveling among the chips is executed when the bias in the erasure cycles is large. The execution frequency of wear-leveling is adjusted considering deterioration of the cell. Evaluations of bit error rate and lifetime show that the proposed method has high reliability and durability.

## Modified decoding algorithm for IRA code in MIMO-OFDM communication system

- **Status**: ✅
- **Reason**: Modified min-sum/BP simplification for IRA code reducing HW complexity; decoder approximation technique potentially transferable to binary LDPC BP (C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5688679
- **Type**: conference
- **Published**: 2010
- **Authors**: Meng Zhang, Weifeng Sun, M. Xu +2
- **PDF**: https://ieeexplore.ieee.org/document/5688679
- **Abstract**: Irregular Repeat Accumulate(IRA) code has drawn a lot of attention recently to its prominent decoding algorithm, whose performance approaches to Shannon limit. Belief propagation decoding algorithm is the best decoding algorithm for IRA code, which has great hardware complexity when implemented. Min-sum decoding algorithm modifies belief propagation decoding algorithm at the cost of decoding performance. A modified decoding algorithm is proposed to simplify belief propagation decoding algorithm with a little of loss in decoding performance according to minimum mean square error rule. The modified decoding algorithm can be applied to MIMO-OFDM communication system to decrease Inter-Carrier-Interference. Simulation results show that if MIMO-OFDM system needs SNR to be 10−5, the encoding gain of modified decoding algorithm can be 0.25dB and 0.15dB better than normalized decoding algorithm and offset decoding algorithm respectively. And the modified decoding algorithm also has lower hardware complexity.

## Latency constrained protograph-based LDPC convolutional codes

- **Status**: ✅
- **Reason**: protograph LDPC-CC용 windowed decoding으로 latency-성능 트레이드오프; SC-LDPC 디코더/구성 기법 NAND 이식 가능(C/E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5613862
- **Type**: conference
- **Published**: 2010
- **Authors**: G. E. Corazza, A. R. Iyengar, M. Papaleo +3
- **PDF**: https://ieeexplore.ieee.org/document/5613862
- **Abstract**: We propose a windowed decoding scheme for protograph-based LDPC convolutional codes (LDPC-CC) that allows us to efficiently trade-off decoding performance for gains in latency. We study the performance of regular LDPC-CC with the windowed decoding scheme. In particular, we show that the class of LDPC-CC proposed in the literature with good belief propagation performance is ill-suited for windowed decoding. Further, we establish properties of code ensembles with good windowed decoding performance over erasure channels with and without memory.

## Protograph-Based LDPC Convolutional Codes for Correlated Erasure Channels

- **Status**: ✅
- **Reason**: protograph 기반 LDPC-CC 신규 구성+윈도우 디코딩, 바이너리 LDPC 코드설계(E) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5502364
- **Type**: conference
- **Published**: 2010
- **Authors**: A. R. Iyengar, M. Papaleo, G. Liva +3
- **PDF**: https://ieeexplore.ieee.org/document/5502364
- **Abstract**: We consider terminated LDPC convolutional codes (LDPC-CC) constructed from photographs and explore the performance of these codes on correlated erasure channels including a single-burst channel (SBC) and Gilbert-Elliott channel (GEC). We consider code performance with a latency-constrained message passing decoder and the belief propagation decoder. We give theoretical bounds on the code efficiency over the SBC and describe a construction that achieves this bound.We show that the designed codes with belief propagation (BP) decoding perform as well as the regular LDPC-CCs presented in the literature on the binary erasure channel (BEC) and the GEC, while achieving significant gains on the SBC. In the case of windowed decoding, our codes perform much better than the best known regular LDPC-CCs over the BEC and the GEC, with very low decoding latencies.

## Performance evaluation of channel coding for Gbps 60-GHz OFDM-based wireless communications

- **Status**: ✅
- **Reason**: 1Gbps급 완전병렬 LDPC 디코더 칩(0.13um CMOS) 구현, 이식 가능 HW 아키텍처(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:5671892
- **Type**: conference
- **Published**: 2010
- **Authors**: M. Marinkovic, M. Piz, Chang-Soon Choi +3
- **PDF**: https://ieeexplore.ieee.org/document/5671892
- **Abstract**: In this paper, we undertake a comparison of LDPC (768,384) and convolutional (171,133) codes for 60-GHz OFDM-based wireless communication systems. The comparison is based on two parameters: Frame Error Rate (FER) for 60-GHz channels and decoding hardware complexity for a required throughput of more than 1 Gbps. Additionally, we provide performance parameters of a fully parallel LDPC decoder chip, fabricated in our IHP in-house 0.13 μm CMOS technology, achieving a throughput of more than 1 Gbps.

## Threshold saturation via spatial coupling: Why convolutional LDPC ensembles perform so well over the BEC

- **Status**: ✅
- **Reason**: spatial coupling 임계포화로 BP threshold를 MAP까지 끌어올리는 SC-LDPC 메커니즘; 바이너리 LDPC 코드설계 핵심 기법(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5513587
- **Type**: conference
- **Published**: 2010
- **Authors**: S. Kudekar, T. Richardson, R. Urbanke
- **PDF**: https://ieeexplore.ieee.org/document/5513587
- **Abstract**: Convolutional LDPC ensembles, introduced by Felström and Zigangirov, have excellent thresholds and these thresholds are rapidly increasing as a function of the average degree. Several variations on the basic theme have been proposed to date, all of which share the good performance characteristics of convolutional LDPC ensembles. We describe the fundamental mechanism which explains why “convolutional-like” or “spatially coupled” codes perform so well. In essence, the spatial coupling of the individual code structure has the effect of increasing the belief-propagation (BP) threshold of the new ensemble to its maximum possible value, namely the maximum-a-posteriori (MAP) threshold of the underlying ensemble. For this reason we call this phenomenon “threshold saturation”. This gives an entirely new way of approaching capacity. One significant advantage of such a construction is that one can create capacity-approaching ensembles with an error correcting radius which is increasing in the blocklength. Our proof makes use of the area theorem of the BP-EXIT curve and the connection between the MAP and BP threshold recently pointed out by Méasson, Montanari, Richardson, and Urbanke. Although we prove the connection between the MAP and the BP threshold only for a very specific ensemble and only for the binary erasure channel, empirically the same statement holds for a wide class of ensembles and channels. More generally, we conjecture that for a large range of graphical systems a similar collapse of thresholds occurs once individual components are coupled sufficiently strongly. This might give rise to improved algorithms as well as to new techniques for analysis.

## A novel hardware-friendly self-adjustable offset min-sum algorithm for ISDB-S2 LDPC decoder

- **Status**: ✅
- **Reason**: self-adjustable offset min-sum 신규 디코더 알고리즘(C), 도메인 무관 바이너리 LDPC BP에 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7096393
- **Type**: conference
- **Published**: 2010
- **Authors**: W. Ji, M. Hamaminato, H. Nakayama +1
- **PDF**: https://ieeexplore.ieee.org/document/7096393
- **Abstract**: In this paper, a novel self-adjustable offset min-sum LDPC decoding algorithm is proposed for ISDB-S2 (Integrated Services Digital Broadcasting via Satellite - Second Generation) application. We present for the first time a uniform approximation of the check node operation through mathematical induction on Jacobian logarithm. The approximation theoretically shows that the offset value is mainly dependent on the difference between the two most unreliable inputs from the bit nodes and the algorithm proposed can adjust the offset value according to the inputs during the iterative decoding procedure. Simulation results for all 11 code rates of ISDB-S2 demonstrate that the proposed method can achieve an average of 0.15dB gain under the same Bit Error Rate (BER) performance, compared to the Min-sum based algorithms, and consumes only 1.21% computation complexity compared to BP-based algorithms in the best case.

## Bilayer protograph codes for half-duplex relay channels

- **Status**: ✅
- **Reason**: bilayer protograph LDPC 구성 + point-to-point AWGN용 개선 protograph 코드(용량 0.07dB 이내); 바이너리 LDPC 코드설계 기법 이식 가능(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5513451
- **Type**: conference
- **Published**: 2010
- **Authors**: T. V. Nguyen, A. Nosratinia, D. Divsalar
- **PDF**: https://ieeexplore.ieee.org/document/5513451
- **Abstract**: This paper presents a high-performing LDPC code for the relay channel that addresses simultaneously two important issues: a code structure that allows low encoding complexity, and a flexible rate-compatible code that allows matching to various channel conditions. Most of the previous high-performance LDPC codes for the relay channel are tightly optimized for a given channel quality and are not easily adapted, without extensive re-optimization, for various channel conditions. This paper presents a code for the relay channel that combines structured design and easy encoding with rate compatibility to allow adaptation to the three links involved in the relay channel, and furthermore offers very good performance. The proposed code is constructed by synthesizing a bilayer structure with a protograph. In addition to the contribution to relay encoding, we also produce an improved family of protograph codes for the point-to-point AWGN channel whose high-rate members enjoy thresholds that are within 0.07 dB of capacity.

## Design and FPGA prototyping of a bit-interleaved coded modulation receiver for the DVB-T2 standard

- **Status**: ✅
- **Reason**: DVB-T2 LDPC 디코더 vertical layered schedule + FPGA 프로토타입; 레이어드 스케줄링 디코더/HW(C/D)로 NAND LDPC 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5624781
- **Type**: conference
- **Published**: 2010
- **Authors**: M. Li, C. A. Nour, C. Jégo +1
- **PDF**: https://ieeexplore.ieee.org/document/5624781
- **Abstract**: Signal Space Diversity (SSD) has been lately adopted into the second generation of the terrestrial digital video broadcasting standard DVB-T2. In this paper, a bit-interleaved coded modulation receiver for the DVB-T2 standard is detailed. An LDPC decoder based on a vertical layered schedule is the main novelty of this work. It enables an efficient exchange of extrinsic information between the rotated demapper and the LDPC decoder if an iterative receiver is considered. The design and the FPGA prototyping of the resultant architecture are then described. Low architecture complexity and good performance represent the main features of the proposed receiver.

## Performance analysis of 3-D monolithic integrated circuits

- **Status**: ✅
- **Reason**: LDPC 디코더를 3D 모놀리식 IC로 구현한 배치·배선 분석, 이식 가능 HW 아키텍처(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:5751465
- **Type**: conference
- **Published**: 2010
- **Authors**: S. Bobba, A. Chakraborty, O. Thomas +3
- **PDF**: https://ieeexplore.ieee.org/document/5751465
- **Abstract**: 3-D monolithic integration (3DMI), also termed as sequential integration, is a potential technology for future gigascale circuits. Since the device layers are processed in sequential order, the size of the vertical contacts is similar to traditional contacts unlike in the case of parallel 3-D integration with through silicon vias (FSVs). Given the advantage of such small contacts, 3DMI supports stacking active layers such that fine-grain integration of 3-D circuits can be implemented. This paper extends the idea of constructing the standard cells across two active layers, forming 3-D cells, to reduce the overall area and interconnect wirelength of a circuit. To demonstrate the effect of the 3DMI technology on these important parameters of circuit design, two important communication blocks are evaluated. Specifically, a low-density-parity-check (LDPC) decoder as a sample of interconnect-dominated circuit and a data-encryption-standard (DES) block, which is good instance of a gate dominated circuit, are investigated. By employing 3-D cells in the conventional design flow chain, there is more than 10% decrease in wirelength for both circuits (in wirelength driven placement mode). However, when subjected to timing driven placement a slight reduction in delay (1.6%) is observed for an LDPC decoder, whereas for the DES block considerable delay reduction (14.22%) is achieved.

## Towards generic low-power area-efficient standard cell based memory architectures

- **Status**: ✅
- **Reason**: standard-cell 메모리(SCM) 아키텍처를 저전력 LDPC 디코더로 예시 - NAND LDPC 디코더 HW 메모리 기법 이식 가능성(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:5548579
- **Type**: conference
- **Published**: 2010
- **Authors**: P. Meinerzhagen, C. Roth, A. Burg
- **PDF**: https://ieeexplore.ieee.org/document/5548579
- **Abstract**: Digital IC designers often use SRAM macrocells to implement on-chip memory functionality. In this paper we argue that in several situations, standard cell based memories (SCMs) can have advantages over SRAM macrocells. Various ways to implement SCMs are presented and compared to each other for different CMOS technologies and standard cell libraries and to corresponding macrocells, aiming for finding the most adequate memory option for each application. The benefits and drawbacks of SCMs compared to macrocells are illustrated with the example of a low-power low-density parity check (LDPC) decoder.

## Selecting error patters based on symbol reliability for OSD algorithm

- **Status**: ✅
- **Reason**: 심볼 신뢰도 기반 OSD 에러패턴 선택으로 복잡도 60%↓, LDPC에 적용된 이식 가능 디코더 알고리즘(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5497428
- **Type**: conference
- **Published**: 2010
- **Authors**: D. Zi-jian, Q. Guo-lei
- **PDF**: https://ieeexplore.ieee.org/document/5497428
- **Abstract**: A new scheme of selecting error pattern is proposed. OSD algorithm processes certain MRIPs of a received sequence, performs bits flip among MRIPs, forms error patterns, and then generates candidate codeword. The bits flip is equal probability among MRIPs in OSD algorithms, which leads to too many candidates generated, and seriously affects the implement of algorithm. This paper proposes an improved algorithm which adopts unequal probability strategy utilizing the reliability of received symbols. The simulation results show that the proposed algorithm is effective. With little performance degradation, the computational complexity of algorithm can be reduced by 60% or more for one class of LDPC codes.

## Iterative Decoding and Estimation of Two-Dimensional Channels with Memory

- **Status**: ✅
- **Reason**: 2D 메모리 채널 LDPC 디코더+오류추정(통계물리/영상복원) 결합 반복 디코딩 기법, 부호비의존 BP 개선으로 이식 가능성(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5532789
- **Type**: conference
- **Published**: 2010
- **Authors**: P. Ellingsen, A. Kvamme
- **PDF**: https://ieeexplore.ieee.org/document/5532789
- **Abstract**: In this paper we consider two-dimensional channels with memory and with error patterns modeled as a Markov random field. We develop an joint iterative estimation and decoding algorithm by using output from an LDPC decoder in combination with an error estimation algorithm based on techniques from statistical physics and digital image restoration to find an estimate of the error pattern and use this estimate then in turn to provide \emph{a priori} information for use in the decoder. Simulations show that this approach can significantly reduce the occurrence of bit errors compared with standard iterative decoding techniques.

## Recursive parallel interleavers for two-phase error control decoders

- **Status**: ✅
- **Reason**: 재귀 2차다항식 기반 병렬 인터리버 VLSI 메모리매핑; LDPC 디코더 병렬·고처리율 HW 아키텍처로 이식 가능(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:5613873
- **Type**: conference
- **Published**: 2010
- **Authors**: I. Ahmed, C. Vithanage, M. Ismail +2
- **PDF**: https://ieeexplore.ieee.org/document/5613873
- **Abstract**: A new memory mapping technique using a VLSI circuit based on recursive quadratic polynomial equations is described. The proposed methodology allows parallel processing elements, such as used in Turbo and Low Density Parity Check (LDPC) decoders, to work independently across memory segments, thus enabling parallel, high throughput, and power efficient LSI circuits.

## Threshold saturation on BMS channels via spatial coupling

- **Status**: ✅
- **Reason**: spatial coupling으로 BMS 채널 BP threshold가 MAP까지 saturation; SC-LDPC 코드설계 기법 이식 가능(E), rate-loss 저감도 다룸
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5613887
- **Type**: conference
- **Published**: 2010
- **Authors**: S. Kudekar, C. Méassony, T. Richardson +1
- **PDF**: https://ieeexplore.ieee.org/document/5613887
- **Abstract**: We consider spatially coupled code ensembles. A particular instance are convolutional LDPC ensembles. It was recently shown that, for transmission over the binary erasure channel, this coupling increases the belief propagation threshold of the ensemble to the maximum a-priori threshold of the underlying component ensemble. We report on empirical evidence which suggests that the same phenomenon also occurs when transmission takes place over a general binary memoryless symmetric channel. This is confirmed both by simulations as well as by computing EBP GEXIT curves and by comparing the empirical BP thresholds of coupled ensembles to the empirically determined MAP thresholds of the underlying regular ensembles. We further consider ways of reducing the rate-loss incurred by such constructions.

## Quality-driven methodology for demanding accelerator design

- **Status**: ✅
- **Reason**: LDPC 디코더 HW 가속기 아키텍처 설계 방법론 — 이식 가능 HW 아키텍처(D) 가능성, 애매하므로 살림
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:5450546
- **Type**: conference
- **Published**: 2010
- **Authors**: L. Jóźwiak, Y. Jan
- **PDF**: https://ieeexplore.ieee.org/document/5450546
- **Abstract**: This paper focuses on mastering the architecture development of hardware accelerators for demanding applications. It presents the results of our analysis of the main problems that have to be solved when designing accelerators for modern demanding applications, and illustrates the problems with an example of accelerator design for LDPC code decoders for the newest communication system standards. Based on the results of our analysis, we formulate the main requirements that have to be satisfied by an adequate methodology for demanding accelerator design, and propose an architecture design methodology which satisfies the requirements.

## Iterative weighted ℓ1 Optimization for compressed sensing and coding

- **Status**: ✅
- **Reason**: LP 디코딩 후처리 reweighted LP로 LDPC 임계값·성능 개선, 바이너리 LDPC 이식 가능 디코더(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5757668
- **Type**: conference
- **Published**: 2010
- **Authors**: M. A. Khajehnejad, A. G. Dimakis, B. Hassibi
- **PDF**: https://ieeexplore.ieee.org/document/5757668
- **Abstract**: We introduce a novel algorithm for decoding binary linear codes by linear programming. We build on the LP decoding algorithm of Feldman et al. and introduce a post-processing step that solves a second linear program that reweights the objective function based on the outcome of the original LP decoder output. Our analysis shows that for some LDPC ensembles we can improve the provable threshold guarantees compared to standard LP decoding. We also show significant empirical performance gains for the reweighted LP decoding algorithm with very small additional computational complexity.

## Squeezing the spectral lemon: Advances in signal processing and coding to improve spectral efficiency

- **Status**: ✅
- **Reason**: 새 QC-LDPC(선형복잡도 인코딩)+병렬 HW 구현(FPGA) 언급, 떼어낼 코드설계/HW 가능성 있어 애매하므로 살림(Phase3)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5672666
- **Type**: conference
- **Published**: 2010
- **Authors**: S. Roy
- **PDF**: https://ieeexplore.ieee.org/document/5672666
- **Abstract**: Over the last few years, a research program was undertaken in collaboration with InterDigital Canada under the theme “Advanced Broadband Transceivers.” The aim was the development of novel signal processing techniques, exploiting the latest in communication theory and having fundamental advantages, while keeping a focus throughout on associated implementation issues, such as algorithmic complexity, power consumption, etc. This research approach, bridging theory and implementation under a pragmatic mindset, yielded rather promising results. For example, it is known that MIMO techniques are the key to augmenting effective link throughput without bandwidth expansion. However, it is still problematic in practice to incorporate multiple antennas on handsets because of cost/power/size constraints. As a solution, virtual MIMO techniques based on sphere decoding were developed which can effectively at the receiver separate more co-channel signals than there are receive antennas. Also, new powerful quasi-cyclic LDPC codes were devised which allow encoding in linear complexity. Furthermore, new joint decoding techniques were developed as well as efficient parallel hardware implementations. Together, these techniques are capable of aggregate throughputs above 10 Gbps on an FPGA. Multi-rate codec architectures were also developed and then applied in ARQ (automated repeat request) schemes, as well as relaying / network coding scenarios. We will look at how these techniques can improve spectral efficiency in current wireless systems. Approaches for further gains will also be discussed, including distributed arrays, cognitive radio, cognitive networks, interference alignment, and network coding.

## Research on Encoding for Low-Density Parity-Check Codes

- **Status**: ✅
- **Reason**: 바이너리 LDPC 인코딩 알고리즘(하삼각/근사하삼각/greedy) 복잡도 비교 — 코드설계/HW 이식 여지(E), 애매하여 in
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5629517
- **Type**: conference
- **Published**: 2010
- **Authors**: Z. -W. Zheng, J. -G. Li
- **PDF**: https://ieeexplore.ieee.org/document/5629517
- **Abstract**: Encoding problems can usually be met in the fields of signal processing, signal transmission, networking and security (key enabling technologies supporting electrical and control engineering applications). With excellent performance, Low-Density Parity-Check Codes is one of the best channel codes. As one of the strongest candidates in the beyond 3th generation communication system, Low-Density Parity-Check Codes is pop currently topic in communication field. In this paper, for the encoding problem of Low-Density Parity-Check Codes, we study the performance and the encoding complexity of the traditional encoding algorithm, the encoding algorithm based on lower triangular parity-check matrix, the encoding algorithm based on approximate lower triangular parity-check matrix, and the encoding algorithm based on the check matrix through greedy algorithm.

## On minimal pseudo-codewords

- **Status**: ✅
- **Reason**: LP 디코딩 minimal pseudo-codeword 대수적 특성화; 바이너리 선형부호 디코더/error floor 분석에 이식 가능(C/E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5513623
- **Type**: conference
- **Published**: 2010
- **Authors**: R. Smarandache
- **PDF**: https://ieeexplore.ieee.org/document/5513623
- **Abstract**: The performance of linear-programming decoding of a binary linear code described by a parity-check matrix depends on the set of pseudo-codewords associated to this matrix and in particular, on the set of minimal pseudo-codewords. This paper attempts to provide an algebraic characterization of the minimal pseudo-codewords. It also provides a connection between the fundamental cone of a Tanner graph and the fundamental cone of its Forney-style factor graph.

## On the scalability of SIMD processing for software defined radio algorithms

- **Status**: ✅
- **Reason**: SIMD 아키텍처상 LDPC 디코딩 성능분석, 병렬 HW 이식 가능성(D) 애매하여 살림
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:5642052
- **Type**: conference
- **Published**: 2010
- **Authors**: P. Westermann, H. Schröder
- **PDF**: https://ieeexplore.ieee.org/document/5642052
- **Abstract**: Software defined radio (SDR) systems require programmable architectures that provide high performance combined with high energy efficiency. Wide single instruction, multiple data (SIMD) architectures could potentially satisfy these demands, but only few publications examine the interdependence between the SIMD width and the performance of typical SDR algorithms. In this paper, we present a detailed analysis of three SDR algorithm classes on a newly developed scalable SIMD architecture, which combines SIMD processing with long instruction word (LIW) execution. Although radix-2 and mixed-radix fast Fourier transform, sphere decoding, and low-density parity-check decoding all benefit from SIMD processing, our results show that there are different constraints on the performance.

## Multiple-bases belief-propagation decoding of high-density cyclic codes

- **Status**: ✅
- **Reason**: 고밀도 순환부호용 multiple-bases BP 디코더; 여러 패리티검사 행렬 활용 BP 개선, 바이너리 LDPC BP에 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5397887
- **Type**: journal
- **Published**: 2010
- **Authors**: T. Hehn, J. B. Huber, O. Milenkovic +1
- **PDF**: https://ieeexplore.ieee.org/document/5397887
- **Abstract**: We introduce a new method for decoding short and moderate-length linear block codes with dense parity check matrix representations of cyclic form. This approach is termed multiple-bases belief-propagation. The proposed iterative scheme makes use of the fact that a code has many structurally diverse parity-check matrices, capable of detecting different error patterns. We show that this inherent code property leads to decoding algorithms with significantly better performance when compared to standard belief-propagation decoding. Furthermore, we describe how to choose sets of parity-check matrices of cyclic form amenable for multiple-bases decoding, based on analytical studies performed for the binary erasure channel. For several cyclic and extended cyclic codes, the multiple-bases belief propagation decoding performance can be shown to closely follow that of the maximum-likelihood decoder.

## Low-Complexity Soft-Decoding Algorithms for Reed–Solomon Codes—Part II: Soft-Input Soft-Output Iterative Decoding

- **Status**: ✅
- **Reason**: RS 부호이나 BP 디코딩 위해 reduced-density 바이너리 패리티검사 행렬 구성+redundant 패리티 부분집합으로 최소신뢰비트 연결 최소화 기법이 부호 비의존적 BP 개선으로 이식 가능(예외 C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5429125
- **Type**: journal
- **Published**: 2010
- **Authors**: J. Bellorado, A. Kavcic, M. Marrow +1
- **PDF**: https://ieeexplore.ieee.org/document/5429125
- **Abstract**: In this paper, we present a practical approach to the iterative decoding of Reed-Solomon (RS) codes. The presented methodology utilizes an architecture in which the output produced by steps of belief-propagation (BP) is successively applied to a legacy decoding algorithm. Due to the suboptimal performance of BP conducted on the inherently dense RS parity-check matrix, a method is first provided for the construction of reduced-density, binary, parity-check equations. Iterative decoding is then conducted utilizing a subset of a redundant set of parity-check equations to minimize the number of connections into the least-reliable bits. Simulation results show that performance comparable to (and exceeding) the best known practical RS decoding techniques is achievable with the presented methodology. The complexity of the proposed algorithm is significantly lower than these existing procedures and permits a practical implementation in hardware.

## Design and analysis of wave-pipelined LDPC decoder

- **Status**: ✅
- **Reason**: LDPC 디코더 HW 아키텍처 (wave-pipelining, 면적·레이턴시 절감) — D 이식 가능 HW
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:5415888
- **Type**: conference
- **Published**: 2-4 Jan. 2
- **Authors**: M. Anbuselvi, S. Salivahanan, P. Saravanan
- **PDF**: https://ieeexplore.ieee.org/document/5415888
- **Abstract**: This paper presents a novel architecture for LDPC codes using wave pipelining technique. LDPC approaches the near Shannon limit and it was analyzed using sum-product algorithm. Wave pipelining technique overcomes the drawbacks of conventional pipelining, namely latency overhead and area overhead. The proposed architecture is designed with different stages of pipelining and the performance is compared with that of wave pipelined architecture. Synthesis report proves that the wave pipelined architecture reduces the area overhead and latency overhead. As an extension of the work, the multiplier module is analysed with floating point representation. LDPC codes find its applications in WLAN (IEEE 802.11n) and MIMO OFDM.

## Fast BER estimation of LDPC codes

- **Status**: ✅
- **Reason**: LDPC 저BER 추정 기법(importance sampling, dominant trapping set 선정) - trapping set/error floor 평가는 NAND LDPC 코드설계(E)에 직접 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5447125
- **Type**: conference
- **Published**: 18-21 Jan.
- **Authors**: Takakazu Sakai, Koji Shibata
- **PDF**: https://ieeexplore.ieee.org/document/5447125
- **Abstract**: In this paper, we propose an estimation method of a very low bit error rate (BER) of low-density parity-check (LDPC) codes. No analytical tool is available to evaluate performance of LDPC codes, and traditional Monte Carlo simulation methods can not estimate low HER of LDPC codes due to the limitation of time. Cole et al, show a fast frame error rate simulation method of LDPC codes by applying importance sampling (IS). At first, we extend Cole et aI.'s method to the BER estimation of LDPC codes. Since the simulation time of the BER evaluation version of the Cole et aI.'s method is proportional to the number of total dominant trapping sets used in the simulation, we should appropriately choose the dominant trapping sets to reduce the simulation time. To avoid the difficulty, we propose another simulation method, which selects a dominant trapping set as proportional to its upper bound. Additionally, we show some numerical examples to demonstrate the effectiveness of the proposed method. When we evaluate BER of 10-16, the simulation time of the proposed method is reduced to 1/6.6 of that of the BER evaluation version of the Cole et al.'s method under the condition of the same accuracy of the estimator.

## Improved iterative decoding of LDPC codes from the IEEE WiMAX standard

- **Status**: ✅
- **Reason**: multiple-bases BP 병렬 디코딩으로 표준 BP 대비 성능 개선 - 부호 비의존적 디코더 개선 기법(C), WiMAX 응용이나 떼어낼 수 있음
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5447126
- **Type**: conference
- **Published**: 18-21 Jan.
- **Authors**: Thorsten Hehn, Johannes B. Huber, Stefan Laendner
- **PDF**: https://ieeexplore.ieee.org/document/5447126
- **Abstract**: Multiple-bases belief-propagation is a parallel decoding setup which allows for improved decoding performance when compared to standard belief-propagation. Originally designed for decoding of high-density parity-check codes in an iterative manner, this method also shows good decoding results for well-designed low-density parity-check codes when signaling over the AWGN channel. We show the applicability of this scheme to channel codes defined in the IEEE WiMAX standard. It is challenging to find sets of well-performing parity-check matrices for these codes, all of them differing from each other. We propose an algorithm which makes use of the special structure of an underlying base matrix to accomplish this task. The results are compared to codes constructed by the progressive edge-growth algorithm and to bounds from information theory.
