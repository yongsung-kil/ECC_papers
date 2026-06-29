# IEEE Xplore — 2019-04 (1차선별 통과)


## Design of Irregular SC-LDPC Codes With Non-Uniform Degree Distributions by Linear Programming

- **Status**: ✅
- **Reason**: 불규칙 SC-LDPC 비균일 차수분포 LP 설계 — 바이너리 코드설계 기법(E), 유한길이 성능 개선
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8590739
- **Type**: journal
- **Published**: April 2019
- **Authors**: Hee-Youl Kwak, Jong-Seon No, Hosung Park
- **PDF**: https://ieeexplore.ieee.org/document/8590739
- **Abstract**: In this paper, we propose new design algorithms of irregular spatially-coupled low-density parity-check (SC-LDPC) codes with non-uniform degree distributions using linear programming (LP). In general, irregular SC-LDPC codes with non-uniform degree distributions are difficult to design with low complexity because their density evolution equations are multi-dimensional. To overcome this problem, proposed design algorithms are based on three main ideas: a local design of degree distributions, pre-computation of the input/output message relationship, and selection of a proper objective function. These ideas make it possible to design degree distributions of irregular SC-LDPC codes by solving low-complexity LP problems over the binary erasure channel (BEC). It is shown that the proposed irregular SC-LDPC codes designed by the proposed algorithms are superior to regular SC-LDPC codes in terms of both asymptotic and finite-length performances over the BEC. We also confirm that the proposed irregular SC-LDPC code achieves better performance compared with an optimized irregular block LDPC code in the same blocklength, which implies that the proposed design algorithms also provide a new way to construct capacity-approaching block LDPC codes.

## Layered LDPC Decoders With Efficient Memory Access Scheduling and Mapping and Built-In Support for Pipeline Hazards Mitigation

- **Status**: ✅
- **Reason**: 레이어드 LDPC 디코더 HW: 메모리 뱅크 매핑·파이프라인 해저드 완화 스케줄링 — NAND ECC HW에 이식 가능(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:8579225
- **Type**: journal
- **Published**: April 2019
- **Authors**: Oana Boncalo, Gyorgy Kolumban-Antal, Alexandru Amaricai +2
- **PDF**: https://ieeexplore.ieee.org/document/8579225
- **Abstract**: This paper proposes a holistic approach that addresses both the message mapping in memory banks and the pipeline-related data hazards in low-density parity-check (LDPC) decoders. We consider a layered hardware architecture using single read/single write port memory banks. The throughput of such an architecture is limited by memory access conflicts, due to improper message mapping in the memory banks, and by pipeline data hazards, due to delayed update effect. We solve these issues by: 1) a residue-based layered scheduling that reduces the pipeline related hazards and 2) off-line algorithms for optimizing the message mapping in memory banks and the message read access scheduling. Our estimates for different LDPC codes indicate that the hardware usage efficiency of our layered decoder is improved by 3%-49% when only the off-line algorithms are employed and by 16%-57% when both the residue-based layered architecture and the off-line algorithms are used.

## From Cages to Trapping Sets and Codewords: A Technique to Derive Tight Upper Bounds on the Minimum Size of Trapping Sets and Minimum Distance of LDPC Codes

- **Status**: ✅
- **Reason**: variable-regular LDPC trapping set 크기·최소거리 상한 도출(cage 연결) — E(error floor/trapping set, 바이너리), 코드설계 기여
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8525278
- **Type**: journal
- **Published**: April 2019
- **Authors**: Ali Dehghan, Amir H. Banihashemi
- **PDF**: https://ieeexplore.ieee.org/document/8525278
- **Abstract**: Cages, defined as regular graphs with minimum number of nodes for a given girth, are well-studied in graph theory. Trapping sets are graphical structures responsible for error floor of low-density parity-check (LDPC) codes, and are well investigated in coding theory. In this paper, we make connections between cages and trapping sets. In particular, starting from a cage (or a modified cage), we construct a trapping set in multiple steps. Based on the connection between cages and trapping sets, we then use the available results in graph theory on cages and derive tight upper bounds on the size of the smallest trapping sets for variable-regular LDPC codes with a given variable degree and girth. The derived upper bounds in many cases meet the best known lower bounds and thus provide the actual size of the smallest trapping sets. Considering that non-zero codewords are a special case of trapping sets, we also derive tight upper bounds on the minimum weight of such codewords, i.e., the minimum distance, of variable-regular LDPC codes as a function of variable degree and girth.

## Protograph-Based Folded Spatially Coupled LDPC Codes for Burst Erasure Channels

- **Status**: ✅
- **Reason**: 프로토그래프 기반 folded SC-LDPC 신규 구성 — E(코드설계, 바이너리), 윈도우 디코더 호환, NAND 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8515101
- **Type**: journal
- **Published**: April 2019
- **Authors**: Inayat Ali, Hyunjae Lee, Ayaz Hussain +1
- **PDF**: https://ieeexplore.ieee.org/document/8515101
- **Abstract**: In this letter, protograph-based folded spatially coupled (FSC) LDPC codes are proposed. The new folded-type structure is obtained by folding the spatial coupling chain of a conventional spatially coupled (SC) LDPC protograph and interlacing the nodes at staggered spatial positions. The proposed codes outperform the SC LDPC codes over single and multiple random-burst erasure channels. We extend the construction of the folded-type structure by connecting multiple one-sided SC LDPC chains for higher resilience to burst erasure channels. The FSC LDPC codes are also compatible with windowed decoder and outperform conventional SC LDPC codes.

## Additive, Structural, and Multiplicative Transformations for the Construction of Quasi-Cyclic LDPC Matrices

- **Status**: ✅
- **Reason**: QC-LDPC 행렬 확장 girth 보장 구성법(등가류 축소+제약프로그래밍) — 바이너리 코드설계(E) 신규 기여
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8594652
- **Type**: journal
- **Published**: April 2019
- **Authors**: Alban Derrien, Emmanuel Boutillon, Audrey Cerqueus
- **PDF**: https://ieeexplore.ieee.org/document/8594652
- **Abstract**: The construction of a quasi-cyclic low density parity-check (QC-LDPC) matrix is usually carried out in two steps. In the first step, a prototype matrix is defined according to certain criteria (size, girth, check and variable node degrees, and so on). The second step involves the expansion of the prototype matrix. During this last phase, an integer value is assigned to each non-null position in the prototype matrix corresponding to the right-rotation of the identity matrix. The problem of determining these integer values is complex. The state-of-the-art solutions use either some mathematical constructions to guarantee a given girth of the final QC-LDPC code, or a random search of values until the target girth is satisfied. In this paper, we propose an alternative/complementary method that reduces the search space by defining large equivalence classes of topologically identical matrices through row and column permutations using additive, structural, and multiplicative transformations. Selecting only a single element per equivalence class can reduce the search space by a few orders of magnitude. Then, we use the formalism of constraint programming to list the exhaustive sets of solutions for a given girth and a given expansion factor. An example is presented in all sections of the paper to illustrate the methodology.

## Energy-Adaptive Error Correcting for Dynamic and Heterogeneous Networks

- **Status**: ✅
- **Reason**: 에너지 적응형 LDPC 코드 설계 구성 제시 — E(코드 설계) 이식 여지, 애매하므로 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8665995
- **Type**: journal
- **Published**: April 2019
- **Authors**: Haewon Jeong, Pulkit Grover
- **PDF**: https://ieeexplore.ieee.org/document/8665995
- **Abstract**: In an era of ever-increasing dynamicity and heterogeneity of wireless networks, energy is fast becoming the most constrained resource. First, we review recent studies that suggest that using one single error-correcting code (ECC) designed to meet the worst case requirement is inefficient in terms of energy consumption when there are many heterogeneous nodes in the network. These works extend the classical Shannon theory and incorporate circuit energy and signal transmit energy to optimize total energy/power consumption of today's communication systems. Then, we survey recent work on designing adaptive ECCs to operate energy efficiently even in the presence of extremely large heterogeneity in requirements and conditions. Two constructions of energy-adaptive codes are summarized: energy-adaptive low-density parity-check (LDPC) codes and energy-adaptive polar codes. These constructions have shown theoretically and empirically that having adaptivity in code design can save substantial energy, especially when the network has very diverse communication scenarios. Finally, we suggest a few possible applications where energy-adaptive codes can be employed and outline interesting future directions and challenges.

## Error Performance Prediction of Randomly Shortened and Punctured LDPC Codes

- **Status**: ✅
- **Reason**: 바이너리 LDPC 단축·천공 코드의 유한길이 WER 성능 예측 — E(유한길이 코드 설계) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8649667
- **Type**: journal
- **Published**: April 2019
- **Authors**: Adriaan Suls, Yannick Lefevre, Jeroen Van Hecke +2
- **PDF**: https://ieeexplore.ieee.org/document/8649667
- **Abstract**: In this contribution, we show that the word error rate (WER) performance in the waterfall region of a randomly shortened and punctured low density parity check code can be accurately predicted from the WER performance of its finite-length mother code. We derive an approximate analytical expression for the mutual information (MI) required by a daughter code to achieve a given WER, based on the MI required by the mother code, which shows that the gap to the capacity of the daughter code grows the more the code is punctured or shortened. The theoretical results are confirmed by simulations (where the random shortening and puncturing pattern is either selected independently per codeword or kept the same for all codewords) for practical codes on both the binary erasure channel and the binary-input additive white Gaussian noise channel.

## Read Voltage Optimization in MLC NAND Flash Memory via the Density Evolution

- **Status**: ✅
- **Reason**: A: MLC NAND 플래시에서 density evolution으로 LDPC 디코더용 read voltage 최적화, NAND 직접 적용
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8798808
- **Type**: conference
- **Published**: 8-10 April
- **Authors**: Chatuporn Duangthong, Watid Phakphisut, Pornchai Supnithi
- **PDF**: https://ieeexplore.ieee.org/document/8798808
- **Abstract**: The multi-level-cell (MLC) NAND flash memory can typically use multiple reads for obtaining soft information for the LDPC decoder. The multiple reads give the soft information which is quantized to a certain level. The major challenge is that the read voltages must be precisely selected to provide better soft information. In the previous work, the read voltages are selected so that the soft information has the maximum mutual information (MMI). However, the error-correction capability of LDPC decoder is not considered. Therefore, in this work, we analyze the performance of LDPC decoder by density evolution whereby the soft information is quantized. Then the optimal read voltages for given LDPC codes are obtained. As a result, for a regular LDPC code with the read voltages optimized by density evolution can provide the lower BER performance compared with the MMI technique.

## Sliding-Window Processing of Turbo Equalization for Partial Response Channels

- **Status**: ✅
- **Reason**: C: SC-LDPC 윈도우 디코더+BCJR sliding-window turbo equalization, PR 채널 ISI 대응 디코더 기법 이식 가능 (자기기록이나 NAND도 ISI 유사)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8798835
- **Type**: conference
- **Published**: 8-10 April
- **Authors**: Sirawit Khittiwitchayakul, Watid Phakphisut, Pornchai Supnithi
- **PDF**: https://ieeexplore.ieee.org/document/8798835
- **Abstract**: Spatially coupled low-density parity-check (SC-LDPC) codes are the attractive candidates for the application requiring a practical constraint on the latency and complexity. In previous works, the turbo equalization consisting the SC-LDPC window decoder and Bahl-Cocke-Jelinek-Raviv (BCJR) detector is used to tackle the inter-symbol interferences (ISIs) in the magnetic recording systems. However, the prior works consider only the SC-LDPC codes which replace the conventional LDPC block codes. In this work, we propose the modification of turbo equalization processing whereby both the SC-LDPC decoder and BCJR detector operate using the sliding window. The results show that the proposed turbo equalization schemes used in the partial response (PR) channel can provide better bit error rate (BER) performances than the conventional turbo equalization.

## Fast DSP Implementation of a Low Complexity LDPC Decoder

- **Status**: ✅
- **Reason**: min-sum 변형(Horizontal Shuffled 스케줄링)+DSP 구현 — 이식 가능 디코더 알고리즘(C)/HW(D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8723838
- **Type**: conference
- **Published**: 3-4 April 
- **Authors**: Mouhcine Razi, Anas Mansouri, Mhammed Benhayoun +2
- **PDF**: https://ieeexplore.ieee.org/document/8723838
- **Abstract**: The Belief Propagation (BP) algorithm is known as the most efficient algorithm in terms of convergence speed. But this algorithm has a very high level of computational complexity. The Min Sum Algorithm (MSA) permits to reduce this computational complexity but with some performances degradations. In this paper we recommend a new approach with more simplified algorithm, that allows to get performances near to these of the BP algorithm by adopting a new version of the MSA algorithm. This last uses Horizontal Shuffled (HS) scheduling instead of the usually used flooding scheduling. This algorithm was successfully implemented on the Digital Signal Processor (DSP). The results obtained after implementation show that the proposed version of the MSA algorithm does not only improve the decoding performance but also decreases the number of iterations necessary for the decoding of the LDPC codes.

## New Memory Load Optimization Approach for Software Implementation of Irregular LDPC Encoder/Decoder

- **Status**: ✅
- **Reason**: 비정규 LDPC 패리티검사행렬 메모리 로딩 최적화(L1캐시) — SW 디코더 HW/메모리 이식 기법(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:8723841
- **Type**: conference
- **Published**: 3-4 April 
- **Authors**: Mhammed Benhayoun, Mouhcine Razi, Anas Mansouri +1
- **PDF**: https://ieeexplore.ieee.org/document/8723841
- **Abstract**: This paper presents a soft implementation of the joint approach for irregular Low Density Parity Check (LDPC) encoding and decoding. The principal idea is to construct excellent irregular LDPC codes focus to two constraints that make certain the effective LDPC encoder and decoder implementations. This work propose a new model for memory loading of the LDPC parity-check matrix aiming to use only the Level one (L1) of cache memory, to take advantage of its high speed latency.

## Performance Analysis of Layered Normalized Min-Sum for LDPC Codes over Weibull Fading Channels

- **Status**: ✅
- **Reason**: Layered Normalized Min-Sum(적응 정규화계수) — 이식 가능 min-sum 변형 디코더(C), 채널은 응용일 뿐
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8723865
- **Type**: conference
- **Published**: 3-4 April 
- **Authors**: Nejwa El Maammar, Jaouad Foshi, Seddik Bri +2
- **PDF**: https://ieeexplore.ieee.org/document/8723865
- **Abstract**: Normalized Min-Sum Algorithms (NMSA) are extensively employed in trading LDPC (Low Density Parity Check) decoders due to their low complexity and reasonable performance close to the performance of sum product algorithm in terms of Error Rate. Our work is focused on the enhancement of error rate performances of NMS algorithm for the decoding of LDPC decoding. In this context we have proposed a Layered Normalized Min-Sum algorithm (LNMS), which employs an adaptive normalization factor to ameliorate the reliability of the information transmitted during the decoding process. To perform this analysis study LDPC coded communication system has been examined over Weibull fading channels and was analyzed for different decoding techniques by the help of comparative computer simulations. Simulation results indicate that the proposed decoding algorithm can achieve better Bit Error Rate (BER) performances closer to SP algorithm with the preservation of the principal characteristics of the MS algorithm.

## Improved MS LDPC Decoder Based on Jacobian Logarithm

- **Status**: ✅
- **Reason**: Jacobian Logarithm 기반 개선 MS LDPC 디코더, offset factor 최적화로 adder+selector만으로 HW 구현 — 이식 가능 디코더/HW(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8834961
- **Type**: conference
- **Published**: 24-26 Apri
- **Authors**: Ruizhen Wu, Lin Wang, Tao Yuan +1
- **PDF**: https://ieeexplore.ieee.org/document/8834961
- **Abstract**: An improved MS LDPC decoder is proposed in this paper. The degradation factor of BP to MS is found and optimized based on Jacobian Logarithm and hardware working mode. An offset factor is added to improve the decoding accuracy rate and is optimized to two constants for different SNR environments thus only need an adder and a selector as hardware cost to implement it. The simulation is based on LDPC NR 3GPP 38.212 release and the comparison results showed the proposed improved MS LDPC decoder have a better BER and iteration time performance than other existing decoders in different SNR environments.

## Design and Implementation of Parallel Branches for Concatenated BCH and LDPC Coding on FPGA

- **Status**: ✅
- **Reason**: BCH+LDPC concatenated FPGA 병렬 디코더 구현, 이식 가능한 LDPC HW 병렬화 기법(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:8734628
- **Type**: conference
- **Published**: 16-18 Apri
- **Authors**: Ahmed Mahdy, Mohamed Helmy, Mohamed Hassan
- **PDF**: https://ieeexplore.ieee.org/document/8734628
- **Abstract**: Recently, satellite services applications are of wide utilization as in radio and television broadcast, voice and data communication, and location services communication. Error correction codes are continuously designed to accomplish reliable communication with low Bit-Error-Rate (BER) in satellite communication link. Modern techniques are using concatenation of different codes, to achieve low BER. This paper presents an implementation for Bose-Chaudauri Hocquenghem (BCH) on FPGA. Also, it provides an implementation for low density parity check (LDPC) on FPGA. Finally, a design and implementation for multiple branches of BCH concatenated with LDPC on FPGA, where the encoder is designed such that two parallel BCH branches are concatenated with one LDPC, while the decoder design is four parallel BCH branches concatenated with one LDPC. This proposed design improves the link reliability and increases the throughput when compared with the serial concatenated coding systems, where the encoder throughput increased from 100 Mbps to 200 Mbps, and the decoder enhanced from 10.5 Mbps to 50 Mbps.

## Robust and Simple Log-Likelihood Approximation for Receiver Design

- **Status**: ✅
- **Reason**: 부호 비의존 LLR 근사로 BP/LDPC 디코더 입력 매핑, LLR 양자화에 이식 가능 (C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8886114
- **Type**: conference
- **Published**: 15-18 Apri
- **Authors**: Yasser Mestrah, Anne Savard, Alban Goupil +2
- **PDF**: https://ieeexplore.ieee.org/document/8886114
- **Abstract**: In impulsive noise, the inputs of the belief propagation decoder can be complex to compute or even impossible when the noise distribution is not known. We propose a simple approximation of the log-likelihood ratio that maps the channel output to the input of the error correcting decoder, for instance, LDPC decoders. This approximation is designed for additive impulsive noise channels, nevertheless, it is not computationally demanding and easy to be implemented. It requires the estimation of three parameters and we propose an efficient way to do it. Moreover, in terms of performance, our solution is barely discernible from the optimal receiver which is computationally prohibitive.
