# IEEE Xplore — 2021-09 (1차선별 통과)


## A Low-Latency BF Decoding of LDPC Codes With Dynamic Thresholds

- **Status**: ✅
- **Reason**: New dynamic-threshold bit-flipping LDPC decoder explicitly targeting flash storage low-latency; transplantable decoder (A/C).
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9452045
- **Type**: journal
- **Published**: Sept. 2021
- **Authors**: Ming Jiang, Dongli Fan
- **PDF**: https://ieeexplore.ieee.org/document/9452045
- **Abstract**: This letter proposes a high throughput bit-flipping (BF) algorithm for regular LDPC codes with dynamic thresholds. In the iterative decoding, the flipping threshold is dynamically updated according to the previous flipping results. Compared to the exiting hard-information-based BF algorithms, the proposed algorithm can get better decoding performance. At the same time, in order to accelerate the convergence speed, we limit the number of occurrences of high thresholds which effectively reduces the invalid decoding iterations. The proposed algorithm has better decoding performance and lower average number of iterations which is suitable for the flash storage systems with low latency and high throughput requirements.

## Error Floor Analysis of LDPC Row Layered Decoders

- **Status**: ✅
- **Reason**: QC-LDPC row-layered 디코더 error floor 분석 + trapping set 기반 layer ordering 최적화. 디코더/error floor 새 기여(C/E), NAND에 직접 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9492129
- **Type**: journal
- **Published**: Sept. 2021
- **Authors**: Ali Farsiabi, Amir H. Banihashemi
- **PDF**: https://ieeexplore.ieee.org/document/9492129
- **Abstract**: In this paper, we analyze the error floor of quasi-cyclic (QC) low-density parity-check (LDPC) codes decoded by the sum-product algorithm (SPA) with row layered message-passing scheduling. For this, we develop a linear state-space model of trapping sets (TSs) which incorporates the layered nature of scheduling. We demonstrate that the contribution of each TS to the error floor is not only a function of the topology of the TS, but also depends on the row layers in which different check nodes of the TS are located. This information, referred to as TS layer profile (TSLP), plays an important role in the harmfulness of a TS. As a result, the harmfulness of a TS in particular, and the error floor of the code in general, can significantly change by changing the order in which the information of different layers, corresponding to different row blocks of the parity-check matrix, is updated. We also study the problem of finding a layer ordering that minimizes the error floor, and obtain row layered decoders with error floor significantly lower than that of their flooding counterparts. As part of our analysis, we make connections between the parameters of the state-space model for a row layered schedule and those of the flooding schedule. Simulation results are presented to show the accuracy of analytical error floor estimates.

## Design of LDBCH Codes for Ultra Reliable Low Latency Communications

- **Status**: ✅
- **Reason**: LDBCH generalizes LDPC by replacing SPC with BCH check nodes plus enhanced message-passing (max-log, weighted scaling); novel binary code-design/decoder transplantable (C/E).
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9466130
- **Type**: journal
- **Published**: Sept. 2021
- **Authors**: Zhen Sun, Zhao Chen, Liuguo Yin +1
- **PDF**: https://ieeexplore.ieee.org/document/9466130
- **Abstract**: In ultra reliable low latency communications, the demanding requirements on high reliability and low latency make it a challenge to design capable channel codes. In this work, a candidate named low-density BCH-constraint (LDBCH) code is introduced, which generalizes low-density parity-check codes by replacing the single parity check code constraints with the BCH code constraints. Specifically, a design methodology is introduced to construct efficient LDBCH codes of short information lengths and low coding rates. Moreover, the message passing decoding of LDBCH is enhanced by max-log approximation and weighted scaling when updating the BCH check nodes. Numerical results show that, with tolerable increase of decoding complexity, LDBCH codes with the proposed decoding enhancement outperforms CA-Polar and 5G LDPC by about 0.3 dB and 0.5 dB in SNR, respectively, for the information length of 104 and the block error rate of  ${10^{{\mathrm{- }}6}}$  over an AWGN channel with QPSK modulation.

## Globally Coupled Finite Geometry and Finite Field LDPC Coding Schemes

- **Status**: ✅
- **Reason**: Globally coupled FG/FF-LDPC 새 부호 구성 + 2-phase iterative 디코딩. 바이너리 LDPC 코드설계 새 기여(E/C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9507258
- **Type**: journal
- **Published**: Sept. 2021
- **Authors**: Mona Nasseri, Xin Xiao, Bane Vasić +1
- **PDF**: https://ieeexplore.ieee.org/document/9507258
- **Abstract**: This paper presents two types of concatenated LDPC coding schemes which are viewed as generalized globally coupled (GC) LDPC coding schemes in which outer codes serve as the local codes for correcting local errors and inner codes serve as global coupling codes to correct global errors. The first type of concatenated LDPC coding scheme globally couples a finite geometry (FG) LDPC code as the local code and a finite field (FF) LDPC code as the global coupling code. This type of global coupling, called GC-FG/FF-LDPC coupling, combines the distinct features of both FG- and FF-LDPC codes to achieve low error rates at a rapid decoding convergence and an error performance close to the Shannon limit. Decoding of a GC-FG/FF-LDPC code is carried out in two iterative phases, global/local or local/global. In the second type of concatenated LDPC coding scheme, both local and global coupling codes are FF-LDPC codes. If both local and global coupling codes are constructed from the same finite field and have the same graphical structures, a GC-FF/FF-LDPC code can be decoded in one phase or two phases iteratively, otherwise, it can be decoded in two phases. Construction of GC-FF/FF-LDPC codes is very flexible in lengths and rates. The proposed two-phase iterative decoding is practically implementable.

## Relation Between GCD Constraint and Full-Length Row-Multiplier QC-LDPC Codes With Girth Eight

- **Status**: ✅
- **Reason**: QC-LDPC girth-8 GCD constraint 필연성 증명 + 최단부호 탐색 알고리즘. 바이너리 코드설계 새 기여(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9481154
- **Type**: journal
- **Published**: Sept. 2021
- **Authors**: Guohua Zhang, Yulin Hu, Yi Fang +1
- **PDF**: https://ieeexplore.ieee.org/document/9481154
- **Abstract**: The greatest-common-divisor (GCD) method is a general framework employing a set of simple inequalities (called GCD constraint) to guarantee girth eight for a class of  $(J,L)$  quasi-cyclic (QC) low-density parity-check (LDPC) codes. However, an important problem, i.e., whether the GCD constraint is necessary for this class of codes to have girth eight, remains open. In this letter, the question is answered affirmatively, following which a novel algorithm aiming to find the shortest codes with girth eight in such a class is proposed. Besides, a close connection is established between the GCD method and the base expansion method, which are both applicable for any  $J$  and any  $L$ .

## Protograph LDPC-Coded BICM-ID With Irregular Mapping: An Emerging Transmission Technique for Massive Internet of Things

- **Status**: ✅
- **Reason**: 프로토그래프 LDPC 코드 설계(enhanced PLDPC, PEXIT 기반) — 바이너리 LDPC 코드설계 신기여로 이식 가능(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9367298
- **Type**: journal
- **Published**: Sept. 2021
- **Authors**: Zhaojie Yang, Yi Fang, Yu Cheng +2
- **PDF**: https://ieeexplore.ieee.org/document/9367298
- **Abstract**: Bit-interleaved coded modulation with iterative decoding (BICM-ID) is a key technology enabling the communication systems to realize reliable and efficient data transmission. In this work, we present a study on the adaptive irregular-mapping (AIM)-aided BICM-ID systems with the use of protograph low-density parity-check (PLDPC) codes. To be specific, we first propose a three-step design strategy to generate a type of adaptive constellations, which can be combined with their corresponding initial constellations to formulate an AIM scheme for improving the BICM-ID performance. Then, we put forward a theoretical-analysis tool, called AIM-based protograph extrinsic information transfer (PEXIT) algorithm, to estimate the convergence performance of PLDPC codes in the AIM-aided BICM-ID systems. By making use of such an algorithm, we further develop a code-design method to construct a new type of PLDPC codes, called enhanced PLDPC codes, tailored for the AIM-aided BICM-ID systems. Both convergence analysis and simulations indicate that the proposed AIM-aided BICM-ID systems perform better than the existing counterparts, and their performance can be significantly improved by using the enhanced PLDPC codes. Consequently, the proposed designs have great potential to meet the high-reliability, high-throughput, and strong link-adaptation requirements of future wireless-communication scenarios, such as green Internet of Things (IoT).

## Exploiting Resistance Drift Characteristics to Improve Reliability of LDPC-Assisted Phase-Change Memory

- **Status**: ✅
- **Reason**: Drift-aware LDPC decoding scheme for memory reliability; drift-compensation soft-input/LLR idea transplantable to NAND read (B/C).
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9449933
- **Type**: journal
- **Published**: Sept. 2021
- **Authors**: Meng Zhang, Fei Wu, Qin Yu +3
- **PDF**: https://ieeexplore.ieee.org/document/9449933
- **Abstract**: Phase-change memory (PCM) as emerging non-volatile memory has attracted more attention and considered as the promising replacement of the main memory. PCM has shown good scalability and high storage density, but data storage reliability has become a challenge and concern. When data are written into PCM cells by a phase transition between amorphous and crystalline, the resistance of each state drifts as the increase of storage time due to structural relaxation. As a result, raw bit error rates (RBER) become higher and higher, severely degrading the data storage reliability (i.e., an important problem in PCM). In this paper, we first find that high error percentage exists between the full amorphous and amorphous states in multilevel cell (MLC) PCM via a preliminary experiment, which is the main factor leading to high RBER. Then, we analyze why this phenomenon exists in PCM from the view of the resistance drift. Finally, by exploiting the resistance drift characteristics, we propose drift compensation and drift-aware LDPC decoding schemes to improve reliability of PCM. Simulation results show that the proposed schemes can significantly reduce the RBER and LDPC decoding iterations.

## The LDPC Challenge in Software-Based 5G New Radio Physical Layer Processing

- **Status**: ✅
- **Reason**: FPGA LDPC 디코더 오프로딩 프로토타입 + 데이터전송 오버헤드 정량분석 — 이식 가능 HW 아키텍처(D).
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:9647697
- **Type**: conference
- **Published**: 7-10 Sept.
- **Authors**: Elissaios Alexios Papatheofanous, Dionysios Reisis, Konstantinos Nikitopoulos
- **PDF**: https://ieeexplore.ieee.org/document/9647697
- **Abstract**: While the realization of 5G has already began, we are also experiencing a paradigm shift towards Open Radio Access Network (RAN) environments. This new paradigm promotes open and flexible RAN architectures, which can benefit by the physical layer processing being executed on open-source software and general purpose processors. However, meeting the real-time latency requirements for the computationally intensive process of Low Density Parity Check (LDPC) Decoding, as defined in the 3GPP 5G New Radio (NR), poses a challenge for such software based systems. Based on that, we report the design and implementation our novel FPGA LDPC offloading prototype which we integrate and evaluate with the OpenAirInterface (OAI) codebase, the fastest growing open-source project towards supporting 5G NR. For the first time, we present a detailed quantitative analysis of the capabilities of LDPC offloading into an FPGA in the context of a 3GPP compliant system, with up to 5 times faster execution times for the decoding. Our contribution includes the finding that offloading to specialized hardware does not necessarily improve processing latency in all LDPC configurations, due to overheads related to data transfers.

## Decoding of Moderate Length LDPC Codes via Learned Clustered Check Node Scheduling

- **Status**: ✅
- **Reason**: RL 기반 LDPC CN 클러스터 스케줄링 디코딩, flooding 대비 0.8dB 이득 — 이식 가능 디코더 스케줄링 기법(C).
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9562199
- **Type**: conference
- **Published**: 6-9 Sept. 
- **Authors**: Salman Habib, Allison Beemer, Jörg Kliewer
- **PDF**: https://ieeexplore.ieee.org/document/9562199
- **Abstract**: In this work, we consider the sequential decoding of moderate length low-density parity-check (LDPC) codes via reinforcement learning (RL). The sequential decoding scheme is modeled as a Markov decision process (MDP), and an optimized decoding policy is subsequently obtained via RL. In contrast to our previous works, where an agent learns to schedule only a single check node (CN) within a group (cluster) of CNs per iteration, in this work we train the agent to schedule all CNs in a cluster, and all clusters in every iteration. That is, in each RL step, an agent learns to schedule CN clusters sequentially depending on the reward associated with the outcome of scheduling a particular cluster. We also propose a modified MDP and a uniform sequential decoding policy, enabling the RL-based decoder to be suitable for much longer LDPC codes than the ones studied in our previous work. The proposed RL-based decoder exhibits an SNR gain of almost 0.8 dB for fixed bit error probability over the standard flooding approach.

## Quaternary Message Passing Decoding of LDPC Codes: Density Evolution Analysis and Error Floor

- **Status**: ✅
- **Reason**: 거친 양자화 quaternary message passing 디코딩 밀도진화+error floor — LLR 양자화 디코더 신기여(C), NAND LLR 양자화와 직결
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9594240
- **Type**: conference
- **Published**: 30 Aug.-3 
- **Authors**: Emna Ben Yacoub, Balazs Matuz, Alexandre Graell i Amat +1
- **PDF**: https://ieeexplore.ieee.org/document/9594240
- **Abstract**: We revisit a coarsely quantized message passing decoding algorithm for low-density parity-check (LDPC) code ensembles, named quaternary message passing (QMP). Particularly, we analyze the performance of unstructured LDPC codes under QMP decoding by means of density evolution. The impact of degree-2 and degree-3 variable nodes on the error floor performance is also discussed. We design a code for QMP that performs within 0.55 dB of the 5G LDPC code at a block error rate of 10−4.

## On the Decoding Performance of Spatially Coupled LDPC Codes with Sub-block Access

- **Status**: ✅
- **Reason**: SC-LDPC 서브블록 접근 semi-global 디코딩, 데이터 스토리지 응용 동기 — 디코더/구성 기법 이식 가능(B/C/E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9594186
- **Type**: conference
- **Published**: 30 Aug.-3 
- **Authors**: Eshed Ram, Yuval Cassuto
- **PDF**: https://ieeexplore.ieee.org/document/9594186
- **Abstract**: We study spatially coupled LDPC codes that allow access to sub-blocks much smaller than the full code block. Sub-block access is realized by a semi-global decoder that decodes a chosen target sub-block by only accessing the target, plus a prescribed number of helper sub-blocks adjacent in the code chain. This paper analyzes the semi-global decoding performance of spatially coupled LDPC codes constructed from protographs. The main result shows that semi-global decoding thresholds can be derived from certain thresholds we define for the single-sub-block graph. These characterizing thresholds are also used for deriving lower bounds on the decoder’s performance over channels with variability and memory across sub-blocks, which are motivated by applications in data storage.

## Balanced Incomplete Block Designs, Partial Geometries, and Their Associated QC-LDPC Codes

- **Status**: ✅
- **Reason**: BIBD/부분기하 기반 새 바이너리 QC-LDPC 구성 — 이식 가능 코드 설계(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9594122
- **Type**: conference
- **Published**: 30 Aug.-3 
- **Authors**: Juane Li, Yi Gong, Shu Lin +1
- **PDF**: https://ieeexplore.ieee.org/document/9594122
- **Abstract**: This paper presents two classes of partial geometries (PaGs) derived from balanced incomplete block designs (BIBDs) of a special type. Based on these two classes of partial geometries, quasi-cyclic (QC) LDPC codes can be constructed. These codes not only perform well over AWGN channels (AWGNCs) but also can correct bursts of erasures over binary erasure channels (BECs) effectively.

## Error Structure Aware Parallel BP-RNN Decoders for Short LDPC Codes

- **Status**: ✅
- **Reason**: 짧은 LDPC용 오류구조 인식 병렬 BP-RNN 디코더, 새 학습법 — 신경망 디코더 신기여(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9594200
- **Type**: conference
- **Published**: 30 Aug.-3 
- **Authors**: Joachim Rosseel, Valérian Mannoni, Valentin Savin +1
- **PDF**: https://ieeexplore.ieee.org/document/9594200
- **Abstract**: This article deals with the decoding of short block length Low Density Parity Check (LDPC) codes. It has already been demonstrated that Belief Propagation (BP) can be adjusted to the short coding length, thanks to its modeling by a Recurrent Neural Network (BP-RNN). To strengthen this adaptation, we introduce a new training method for the BP-RNN. Its aim is to specialize the BP-RNN on error events sharing the same structural properties. This approach is then associated with a new decoder composed of several parallel specialized BP-RNN decoders, each trained on correcting a different type of error events. Our results show that the proposed specialized BP-RNNs working in parallel effectively enhance the decoding capacity for short block length LDPC codes.

## Towards an Accurate High-Level Energy Model for LDPC Decoders

- **Status**: ✅
- **Reason**: LDPC 디코더 고수준 에너지 모델+밀도진화 — HW 설계 단계 평가 기법 이식 가능(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:9594187
- **Type**: conference
- **Published**: 30 Aug.-3 
- **Authors**: Jérémy Nadal, Simon Brown, Elsa Dupraz +1
- **PDF**: https://ieeexplore.ieee.org/document/9594187
- **Abstract**: Estimating the energy consumption of LDPC decoders is a long and difficult task due to the large number of factors involved. Modern circuit synthesis tools can provide a satisfactory estimation of the power consumption, but this requires that the circuit be already implemented and it can take hours to provide the estimate. Currently, no accurate models are available to evaluate the decoding energy early in the design process. We propose a high-level energy model for flip-flop memory elements in LDPC architectures. The originality of the model is that it can analytically evaluate the variation of the energy due to the switching activity of the circuit gates, depending on the probability mass function (PMF) of the circuit inputs. Such PMFs are obtained through an adapted density evolution method that we propose. Therefore, the energy can be profiled for each decoding iteration and SNR value while considering several architecture choices. We illustrate the validity of the model by comparing the obtained energy estimates with measurements based on circuit simulations.

## Neural-Network-Optimized Degree-Specific Weights for LDPC MinSum Decoding

- **Status**: ✅
- **Reason**: 차수별 가중치 공유 N-2D-NMS min-sum 디코더, 대폭 파라미터 절감+error floor 개선 — 디코더 신기여(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9594227
- **Type**: conference
- **Published**: 30 Aug.-3 
- **Authors**: Linfang Wang, Sean Chen, Jonathan Nguyen +2
- **PDF**: https://ieeexplore.ieee.org/document/9594227
- **Abstract**: Neural Normalized MinSum (N-NMS) decoding delivers better frame error rate (FER) performance on linear block codes than conventional Normalized MinSum (NMS) by assigning dynamic multiplicative weights to each check-to-variable node message in each iteration. Previous N-NMS efforts primarily investigated short block codes (N < 1000), because the number of N-NMS parameters required to be trained scales proportionately to the number of edges in the parity check matrix and the number of iterations. This imposes an impractical memory requirement for conventional tools such as Pytorch and Tensorflow to create the neural network and store gradients. This paper provides efficient methods of training the parameters of N-NMS decoders that support longer block lengths. Specifically, this paper introduces a family of Neural 2-dimensional Normalized (N-2D-NMS) decoders with various reduced parameter sets and shows how performance varies with the parameter set selected. The N-2D-NMS decoders share weights with respect to check node and/or variable node degree. Simulation results justify a reduced parameter set, showing that the trained weights of N- NMS have a smaller value for the neurons corresponding to larger check/variable node degree. Further simulation results on a (3096,1032) Protograph-Based Raptor-Like (PBRL) code show that the N-2D-NMS decoder can achieve the same FER as N- NMS while also providing at least a 99.7% parameter reduction. Furthermore, the N-2D-NMS decoder for the (16200,7200) DVBS- 2 standard LDPC code shows a lower error floor than belief propagation. Finally, this paper proposes a hybrid decoder training structure that utilizes a neural network which combines a feedforward module with a recurrent module. The decoding performance and parameter reduction of the hybrid training depends on the length of recurrent module of the neural network.

## Necessary and Sufficient Girth Conditions for LDPC Tanner Graphs with Denser Protographs

- **Status**: ✅
- **Reason**: QC-LDPC girth 6-12 조건과 빠른 부호 구성 알고리즘 제시 — 이식 가능한 코드 설계 신기여(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9594176
- **Type**: conference
- **Published**: 30 Aug.-3 
- **Authors**: Anthony Gómez-Fonseca, Roxana Smarandache, David G. M. Mitchell
- **PDF**: https://ieeexplore.ieee.org/document/9594176
- **Abstract**: This paper gives necessary and sufficient conditions for the Tanner graph of a quasi-cyclic (QC) low-density parity-check (LDPC) code based on the all-one protograph to have girth 6, 8, 10, and 12, respectively, in the case of parity-check matrices with column weight 4. These results are a natural extension of the girth results of the already-studied cases of column weight 2 and 3, and it is based on the connection between the girth of a Tanner graph given by a parity-check matrix and the properties of powers of the product between the matrix and its transpose. The girth conditions can be easily incorporated into fast algorithms that construct codes of desired girth between 6 and 12; our own algorithms are presented for each girth, together with constructions obtained from them and corresponding computer simulations. More importantly, this paper emphasizes how the girth conditions of the Tanner graph corresponding to a parity-check matrix composed of circulants relate to the matrix obtained by adding (over the integers) the circulant columns of the parity-check matrix. In particular, we show that imposing girth conditions on a parity-check matrix is equivalent to imposing conditions on a square circulant submatrix obtained from it.

## FAID Diversity via Neural Networks

- **Status**: ✅
- **Reason**: 바이너리 LDPC FAID 디코더 diversity를 RQNN으로 학습, error floor 저감 - 신경망 디코더 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9594253
- **Type**: conference
- **Published**: 30 Aug.-3 
- **Authors**: Xin Xiao, Nithin Raveendran, Bane Vasić +2
- **PDF**: https://ieeexplore.ieee.org/document/9594253
- **Abstract**: Decoder diversity is a powerful error correction framework in which a collection of decoders collaboratively correct a set of error patterns otherwise uncorrectable by any individual decoder. In this paper, we propose a new approach to design the decoder diversity of finite alphabet iterative decoders (FAIDs) for Low-Density Parity Check (LDPC) codes over the binary symmetric channel (BSC), for the purpose of lowering the error floor while guaranteeing the waterfall performance. The proposed decoder diversity is achieved by training a recurrent quantized neural network (RQNN) to learn/design FAIDs. We demonstrated for the first time that a machine-learned decoder can surpass in performance a man-made decoder of the same complexity. As RQNNs can model a broad class of FAIDs, they are capable of learning an arbitrary FAID. To provide sufficient knowledge of the error floor to the RQNN, the training sets are constructed by sampling from the set of most problematic error patterns - trapping sets. In contrast to the existing methods that use the cross-entropy function as the loss function, we introduce a frame-error-rate (FER) based loss function to train the RQNN with the objective of correcting specific error patterns rather than reducing the bit error rate (BER). The examples and simulation results show that the RQNN-aided decoder diversity increases the error correction capability of LDPC codes and lowers the error floor.

## A Two-stage Decoding Algorithm for Spatially Coupled Algebraic LDPC Codes

- **Status**: ✅
- **Reason**: SC-LDPC용 2단 디코딩(sliding-window BP + majority logic), 선형복잡도 새 디코더 - 이식 가능(C/E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9594252
- **Type**: conference
- **Published**: 30 Aug.-3 
- **Authors**: Juewei Wang, Xiao Ma
- **PDF**: https://ieeexplore.ieee.org/document/9594252
- **Abstract**: In this paper, we propose a two-stage decoding algorithm for spatially-coupled algebraic low-density paritycheck (LDPC) codes with linear computational complexity, which consists of a sliding-window belief propagation (BP) decoding algorithm and a majority logic decoding algorithm. Simulation results are presented, showing that the error rate performance of SC-LDPC codes can be further improved by the majority logic decoding algorithm.

## Towards Fully Pipelined Decoding of Spatially Coupled Serially Concatenated Codes

- **Status**: ✅
- **Reason**: 공간결합 직렬연접부호의 jumping window 디코딩+파이프라인 HW — 스케줄링/병렬화 기법 이식 가능(C/D), 애매하나 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9594185
- **Type**: conference
- **Published**: 30 Aug.-3 
- **Authors**: Mojtaba Mahdavi, Liang Liu, Ove Edfors +3
- **PDF**: https://ieeexplore.ieee.org/document/9594185
- **Abstract**: Having close-to-capacity performance and low error floor, even for small block lengths, make spatially coupled serially concatenated codes (SC-SCCs) a very promising class of codes. However, classical window decoding of SC-SCCs either limits the minimum block length or requires a large number of iterations, which increases the complexity and constrains the degree to which an SC-SCC decoder architecture can be parallelized. In this paper we propose jumping window decoding (JWD), an algorithmic modification to the scheduling of decoding such that it enables pipelined implementation of SC-SCCs decoder. Also, it provides flexibility in terms of block length and number of iterations and makes them independent of each other. Simulation results show that our scheme outperforms classical window decoding of both SC-SCCs and uncoupled SCCs, in terms of performance. Furthermore, we present a fully pipelined hardware architecture to realize JWD of SC-SCCs along with area estimates in 12 nm technology for the respective case study.

## Gradient Descent Bit-Flipping Decoding with Momentum

- **Status**: ✅
- **Reason**: Momentum 적용 GDBF 비트플립 디코더, error-floor 개선 — 새 디코더 알고리즘(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9594128
- **Type**: conference
- **Published**: 30 Aug.-3 
- **Authors**: Valentin Savin
- **PDF**: https://ieeexplore.ieee.org/document/9594128
- **Abstract**: In this paper, we propose a Gradient Descent Bit-Flipping (GDBF) decoding with momentum, which considers past updates to provide inertia to the decoding process. We show that GDBF or randomized GDBF decoders with momentum may closely approach the floating-point Belief-Propagation decoding performance, and even outperform it in the error-floor region, especially for graphs with high connectivity degree.

## Shuffled Decoding of Serial Concatenated Convolutional Codes

- **Status**: ✅
- **Reason**: shuffled decoding을 직렬 연접 부호에 적용, HW 효율(메모리 29%↓)·throughput 2배 - 이식 가능 디코더/HW 기법(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9594068
- **Type**: conference
- **Published**: 30 Aug.-3 
- **Authors**: Aomar Bourenane, Matthieu Arzel, Frédéric Guilloud +1
- **PDF**: https://ieeexplore.ieee.org/document/9594068
- **Abstract**: Shuffled decoding enables to accelerate the extrinsic information exchange during iterative decoding of concatenated codes. It has already been applied to parallel convolutional codes or low-density parity-check codes. In this article, we propose to apply shuffled decoding to serial concatenation convolutional codes. We take advantage of their systematic encoding to propose an efficient shuffled decoding scheme. Compared to a standard iterative decoding scheme, the convergence of our shuffled implementation is obtained within fewer iterations, each one requiring also less time to be completed. This convergence acceleration yields doubling the throughput. We finally show that doubling the throughput comes at a lower cost than doubling the hardware resources, making this shuffled scheme efficient in term of implementation. For instance, the memory usage is 29% more efficient thanks to our proposal than a baseline scheme, which significantly reduces the power consumption of hardware decoders.

## Forward-Error-Correction for Beyond-5G Ultra-High Throughput Communications

- **Status**: ✅
- **Reason**: 1Tbit/s급 LDPC 디코더 아키텍처 신규 설계 언급 — 이식 가능 HW(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:9594126
- **Type**: conference
- **Published**: 30 Aug.-3 
- **Authors**: Norbert Wehn, Onur Sahin, Matthias Herrmann
- **PDF**: https://ieeexplore.ieee.org/document/9594126
- **Abstract**: Forward-Error-Correction (FEC) constitutes a dominant power consuming and throughput limiting component in the end-to-end digital baseband chain for wireless systems. With the progress in THz and Tbit/s link-level technologies towards practical solutions and deployments arguably in beyond-5G and 6G era, the performance and implementation bottleneck due to FEC in these systems becomes increasingly clear. In this paper, we explore FEC performance requirements for various beyond-5G wireless use-cases from a practical implementation perspective. We then provide some recent designs in Low Density Parity Check (LDPC) and Polar Codes, and their decoder architectures that demonstrate significant potential towards achieving throughputs approaching 1 Tbit/s.

## Coding Schemes for Crossbar Resistive Memory with High Line Resistance in SCM Applications

- **Status**: ✅
- **Reason**: Crossbar resistive memory(SCM 스토리지) ECC 코딩 스킴 — 스토리지 ECC 일반(B)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9594163
- **Type**: conference
- **Published**: 30 Aug.-3 
- **Authors**: Zehui Chen, Lara Dolecek
- **PDF**: https://ieeexplore.ieee.org/document/9594163
- **Abstract**: Crossbar resistive memory with 1 Selector 1 Resistor (1S1R) structure is attractive for low-cost, power efficient, and high-density storage class memory (SCM) applications. As technology scales down to the single-nm regime, the increasing resistivity of wordline/bitline becomes a limiting factor to device reliability. Due to the line resistance, reliability of memory cells in an array is spatially non-uniform. In this paper, by mitigating and leveraging this spatial non-uniformity, we propose two simple yet effective coding schemes, one that utilizes interleaving and one that utilizes multiple codes based on a proposed location dependent code allocation (LDCA) framework, to reduce the undetected bit-error rate (UBER) or to allow for lower write voltage for power efficiency in the studied crossbar resistive memories.

## Energy Efficient FEC Decoders

- **Status**: ✅
- **Reason**: LDPC/Polar 디코더 전력·에너지 최적화 설계 — HW 구현 기법 이식 가능(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:9594237
- **Type**: conference
- **Published**: 30 Aug.-3 
- **Authors**: Matthias Herrmann, Claus Kestel, Norbert Wehn
- **PDF**: https://ieeexplore.ieee.org/document/9594237
- **Abstract**: Channel coding, or Forward Error Correction (FEC), is a crucial technology component in any digital baseband processing. Decoder IPs for advanced coding schemes like Turbo, LDPC, and Polar codes are major sources of power consumption and silicon area in baseband SOCs and largely contribute to the baseband latency and throughput limitations. Although we observe a continuous increase in throughput and lower latency requirements in emerging communication standards, the available power and energy budget does not increase due to, e.g., thermal design power constraints. If we look on the silicon technology progress, the transistor density still follows Moore’s law, but the power improvement largely slows down, that exacerbates the power density problem. Hence, for use cases with high throughput requirements like B5G, power, power density and energy efficiency become a major bottleneck for the successful application of advanced channel coding from a silicon implementation perspective. In this paper we focus especially on LDPC and Polar codes since they are part of many communication standards. Challenges, power and energy optimizations on the different design levels for decoders targeting throughput towards 1Tb/s and various trade-offs are presented.

## Machine Learning Scaled Belief Propagation for Short Codes

- **Status**: ✅
- **Reason**: short code용 학습된 스케일링 BP(MLS-BP) 디코더 개선, C(신경망/BP 개선)로 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9625308
- **Type**: conference
- **Published**: 27-30 Sept
- **Authors**: Matthias Hummert, Dirk Wübben, Armin Dekorsy
- **PDF**: https://ieeexplore.ieee.org/document/9625308
- **Abstract**: The problem of finding good error correcting codes for short block lenghts and its corresponding decoders is an open research topic. A frequently applied soft decoder is the Belief Propagation (BP) decoder, however with degraded performance in case of short loops in the Tanner graph. This is especially problematic for short length codes as loops of small length are more likely to occur. In this paper, we propose the Machine Learning Scaled Belief Propagation (MLS-BP) to mitigate the performance loss of BP decoding for short length codes by introducing a learned scaling factor for the receive signals. The key point of this approach is the fact that the implementation of the BP decoder is not changed and the simple scaling leads to performance results comparable to other proposed BP improvements.

## Search for Good Irregular Low-Density Parity-Check Codes Via Graph Spectrum

- **Status**: ✅
- **Reason**: 비이진 명시 없는 LDPC 코드 설계: graph spectrum 기반 irregular LDPC 탐색 메트릭 제안 — 이식 가능 코드설계(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9569696
- **Type**: conference
- **Published**: 13-16 Sept
- **Authors**: Dawei Yin, Xiaojing Zhang, Xichao Shu +2
- **PDF**: https://ieeexplore.ieee.org/document/9569696
- **Abstract**: Research on the expander code shows that for a regular low-density parity-check (LDPC) code, the Tanner graph’s spectrum determines its properties, such as the minimum distance and the size of stopping sets. In this study, we demonstrate theoretically and experimentally that the performance of irregular LDPC codes is related to the graph spectrum. Our observations may provide an efficient metric to search for good irregular LDPC codes.
