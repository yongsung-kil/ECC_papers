# IEEE Xplore — 2010-12 (1차선별 통과)


## On the Decomposition Method for Linear Programming Decoding of LDPC Codes

- **Status**: ✅
- **Reason**: C. LP 디코딩 분해법(D-W decomposition)으로 저장·연산 절감, LDPC 디코더 알고리즘 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5628280
- **Type**: journal
- **Published**: December 2
- **Authors**: Haiyang Liu, Wenze Qu, Bin Liu +1
- **PDF**: https://ieeexplore.ieee.org/document/5628280
- **Abstract**: In this paper, we focus on solving the linear programming (LP) problem that arises in the decoding of low-density parity-check (LDPC) codes by means of the revised simplex method. In order to take advantage of the structure of the LP problem, we reformulate the dual LP and apply the idea of Dantzig-Wolfe (D-W) decomposition method to solve the problem. Each subproblem in the D-W decomposition method is an LP over a convex polyhedral cone. We define the convex polyhedral cone as local parity-check cone and discuss its special structures. Then, we enumerate its extreme rays and use these extreme rays to design an efficient method for the general LP decoding problem. The proposed method exhibits advantages in reducing both the storage and computational requirements.

## LDPC Decoders with Informed Dynamic Scheduling

- **Status**: ✅
- **Reason**: C. Informed Dynamic Scheduling 메시지패싱 스케줄링 신규 기법, BP 디코더에 부호 비의존적으로 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5610969
- **Type**: journal
- **Published**: December 2
- **Authors**: Andres I. Vila Casado, Miguel Griot, Richard D. Wesel
- **PDF**: https://ieeexplore.ieee.org/document/5610969
- **Abstract**: Low-Density Parity-Check (LDPC) codes are usually decoded by running an iterative belief-propagation (BP), or message-passing, algorithm over the factor graph of the code. The traditional message-passing scheduling, called flooding, consists of updating all the variable nodes in the graph, using the same pre-update information, followed by updating all the check nodes of the graph, again, using the same pre-update information. Recently, several studies show that sequential scheduling, in which messages are generated using the latest available information, significantly improves the convergence speed in terms of number of iterations. Sequential scheduling introduces the problem of finding the best sequence of message updates. We propose Informed Dynamic Scheduling (IDS) strategies that select the message-passing schedule according to the observed rate of change of the messages. In general, IDS strategies require computation to select the message to update but converge in fewer message updates because they focus on the part of the graph that has not converged. Moreover, IDS yields a lower error-rate performance than either flooding or sequential scheduling because IDS strategies overcome traditional trapping-set errors. This paper presents IDS strategies that address several issues including performance for short-blocklength codes, complexity, and implementability.

## Improved Construction of Irregular Progressive Edge-Growth Tanner Graphs

- **Status**: ✅
- **Reason**: E. PEG Tanner 그래프 구성 개선(불규칙 차수분포 대응), 바이너리 LDPC 코드설계 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5606185
- **Type**: journal
- **Published**: December 2
- **Authors**: Jesus Martinez-Mateo, David Elkouss, Vicente Martin
- **PDF**: https://ieeexplore.ieee.org/document/5606185
- **Abstract**: The progressive edge-growth algorithm is a well-known procedure to construct regular and irregular low-density parity-check codes. In this paper, we propose a modification of the original algorithm that improves the performance of these codes in the waterfall region when constructing codes complying with both, check and symbol node degree distributions. The proposed algorithm is thus interesting if a family of irregular codes with a complex check node degree distribution is used.

## Reverse Concatenated Coded Modulation for High-Speed Optical Communication

- **Status**: ✅
- **Reason**: BCH(내부 MAP)-LDPC(외부) reverse concatenation에서 min-sum-with-correction-term LDPC 디코더와 신뢰도 전달 구조, LDPC 디코더 기법 이식 가능(C) — 애매하여 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5634050
- **Type**: journal
- **Published**: Dec. 2010
- **Authors**: Ivan B. Djordjevic, Lei Xu, Ting Wang
- **PDF**: https://ieeexplore.ieee.org/document/5634050
- **Abstract**: We propose the reverse concatenated code as a forward error correction (FEC) scheme suitable for beyond 100-Gb/s optical transmission. In this scheme, BCH code is used as inner code and low-density parity-check (LDPC) code as outer code. The BCH decoder is implemented based on maximum a posteriori (MAP) decoding such as the BCJR/Ashikmin's algorithm, and an LDPC decoder is based on a min-sum-with-correction-term algorithm. Because maximum a posteriori (MAP) decoding is used as the inner decoder, it provides high accuracy reliabilities to be used in LDPC decoding. We show that proposed FEC scheme performs comparably with much longer LDPC codes of girth 12 for a smaller number of LDPC decoder iterations. Because the outer LDPC code is of medium length and the number of required iterations is low, the proposed concatenated scheme represents an interesting candidate to be used in beyond 100-Gb/s optical transmission. The net coding gain (NCG) of concatenated LDPC(16935,14819)-BCH(64,57) code is 9.62 dB at a bit error rate (BER) of 10-9, whereas the expected NCG at BER of 10-13 is 11.38 dB. This concatenated code outperforms the corresponding turbo-product counterpart with a Chase II decoding algorithm by 0.94 dB at BER of 10-9.

## Norm-Product Belief Propagation: Primal-Dual Message-Passing for Approximate Inference

- **Status**: ✅
- **Reason**: sum/max-product·TRBP를 일반화한 수렴성 norm-product 메시지패싱(convex-free-energy) 신규 BP 알고리즘, 바이너리 LDPC BP 디코더로 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5625635
- **Type**: journal
- **Published**: Dec. 2010
- **Authors**: Tamir Hazan, Amnon Shashua
- **PDF**: https://ieeexplore.ieee.org/document/5625635
- **Abstract**: Inference problems in graphical models can be represented as a constrained optimization of a free-energy function. In this paper, we treat both forms of probabilistic inference, estimating marginal probabilities of the joint distribution and finding the most probable assignment, through a unified message-passing algorithm architecture. In particular we generalize the belief propagation (BP) algorithms of sum-product and max-product and tree-reweighted (TRW) sum and max product algorithms (TRBP) and introduce a new set of convergent algorithms based on “convex-free-energy” and linear-programming (LP) relaxation as a zero-temperature of a convex-free-energy. The main idea of this work arises from taking a general perspective on the existing BP and TRBP algorithms while observing that they all are reductions from the basic optimization formula of f +Σihi where the function f is an extended-valued, strictly convex but nonsmooth and the functions hi are extended-valued functions (not necessarily convex). We use tools from convex duality to present the “primal-dual ascent” algorithm which is an extension of the Bregman successive projection scheme and is designed to handle optimization of the general type f + Σihi. We then map the fractional-free-energy variational principle for approximate inference onto the optimization formula above and introduce the “norm-product” message-passing algorithm. Special cases of the norm-product include sum-product and max-product (BP algorithms), TRBP and NMPLP algorithms. When the fractional-free-energy is set to be convex (convex-free-energy) the norm-product is globally convergent for the estimation of marginal probabilities and for approximating the LP-relaxation. We also introduce another branch of the norm-product which arises as the “zero-temperature” of the convex-free-energy which we refer to as the “convex-max-product”. The convex-max-product is convergent (unlike max-product) and aims at solving the LP- relaxation.

## On the reduced-complexity of LDPC decoders for beyond 400 Gb/s serial optical transmission

- **Status**: ✅
- **Reason**: 감소복잡도 LDPC 디코더(optimally attenuated RC min-sum), large-girth 코드 — 카테고리 C/E 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5682631
- **Type**: conference
- **Published**: 8-12 Dec. 
- **Authors**: Ivan B. Djordjevic, Lei Xu, Ting Wang
- **PDF**: https://ieeexplore.ieee.org/document/5682631
- **Abstract**: Two reduced-complexity (RC) LDPC decoders, which can be used in combination with large-girth LDPC codes to enable beyond 400 Gb/s serial optical transmission, are proposed. We show that optimally attenuated RC min-sum sum algorithm performs only 0.45 dB worse than conventional sum-product algorithm, while having lower storage memory requirements and much lower latency.

## Power efficient column operation-based message-passing schedule for regular ldpc decoder

- **Status**: ✅
- **Reason**: column operation 기반 메시지패싱 스케줄로 전력/메모리 절감(C/D), 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5775072
- **Type**: conference
- **Published**: 6-9 Dec. 2
- **Authors**: Eun Ji Kim, Myung Hun Lee, Myung Hoon Sunwoo
- **PDF**: https://ieeexplore.ieee.org/document/5775072
- **Abstract**: This paper proposes a power efficient column operation-based message passing schedule for an LDPC decoder. Redundant memory accesses and column operations are removed by using the improved column operation-based message passing schedule. Therefore, the number of memory accesses can be significantly reduced, and thus, power consumption can be also reduced. As a result, the experimental results show that the proposed LDPC decoder can save about 27% power consumption and reduce 25% column operations compared with existing designs with the same error correcting performance.

## Memory size reduction for LDPC layered decoders

- **Status**: ✅
- **Reason**: LDPC layered 디코더 메모리 축소 HW 아키텍처(D), NAND ECC에 이식 가능
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:5774863
- **Type**: conference
- **Published**: 6-9 Dec. 2
- **Authors**: Shuang Zhao, Xiaofang Zhou, Fanglong Ying +1
- **PDF**: https://ieeexplore.ieee.org/document/5774863
- **Abstract**: LDPC coding has attracted much attention due to its high performance, and it has been widely used in telecommunication systems. This paper focuses on the decoder hardware architecture, especially on memory size reduction, which is an important part of the entire area cost. The design has been post-layout simulated using a UMC 0.18 micron technology at a clock speed of 74 MHz. Using the proposed 3-level memory structure together with the described control logic, the required number of bits of memory can be reduced by up to 34.9% compared to prior approaches.

## Design of turbo decoder based on Min-Sum decoding algorithm of LDPC code

- **Status**: ✅
- **Reason**: min-sum 디코더 메시지 압축 저장 기법(C/D) 부호 비의존적, 바이너리 LDPC BP에 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5774882
- **Type**: conference
- **Published**: 6-9 Dec. 2
- **Authors**: Pengjun Wang, Fanglong Yi
- **PDF**: https://ieeexplore.ieee.org/document/5774882
- **Abstract**: Turbo code has been used by multiple communication standards due to its performance near Shannon limit. However, its decoding algorithm is complicated. Through the research on Turbo code, a novel design of Turbo decoder is presented in this paper. Turbo code is decoded by the Min-Sum decoding algorithm of LDPC code, which is a low complicated decoding algorithm. Moreover, messages are stored compressively, and the check-to-variable messages and the variable-to-check messages are stored alternately. This design reduced the required memory significantly. Finally, the decoder is simulated by ModelSim SE6.0 and the simulation results show that the decoder has high decoding speed.

## Efficient encoding for hardware implementation of IRA LDPC on 802.16 standard

- **Status**: ✅
- **Reason**: QC-LDPC 실시간 인코더 HW 아키텍처(누산 재귀식, 레지스터 재사용) - 이식 가능 HW(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:5704653
- **Type**: conference
- **Published**: 6-8 Dec. 2
- **Authors**: Trio Adiono, Agi Prasetiadi, Anugrah Salbiyono
- **PDF**: https://ieeexplore.ieee.org/document/5704653
- **Abstract**: We propose an encoding scheme for quasi-cyclic low-density parity check (QC-LDPC) suitable for LDPC codes in IEEE 802.16e. We developed accumulated recursive formula to calculate parity bits, so we can encode the message in real time. Basic idea from our method is, use first parity vector recursively to produce another parity vector efficiently. While parity vector is chosen as an output, it also saved in another register for being used in next operation. An encoder architecture is proposed and implemented to verify the results. Later, we discuss the hardware simulation results.

## Multi-rate LDPC decoder implementation for CMMB

- **Status**: ✅
- **Reason**: 멀티레이트 LDPC 디코더 HW: 특수 양자화/메모리충돌/layered 메시지압축 - 이식 가능 C/D
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5704699
- **Type**: conference
- **Published**: 6-8 Dec. 2
- **Authors**: Xiaobo Jiang, Qun Yuan
- **PDF**: https://ieeexplore.ieee.org/document/5704699
- **Abstract**: In this paper, a multi-rate Low Density Parity Check (LDPC) decoder for China Mobile Multimedia Broadcasting (CMMB) is proposed. The architecture of proposed decoder only utilizes a parallel with 2 for ½ rate and 1 for ¾ rate can meet the throughput requirements for the CMMB standard. Various techniques are employed to significantly reduce memory and logic resources, including a special quantization scheme, solution for memory collision, the reuse properties of layered decoding, compressing of check-to-variable messages and the layered algorithm, which lead to a reduction of memory and logic resources by a half.

## An overlapping min-sum LDPC decoder for IEEE 802.11n

- **Status**: ✅
- **Reason**: min-sum 디코더용 overlapping HW 기법(행/열 사이클타임 감소) - 이식 가능 HW(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:5704671
- **Type**: conference
- **Published**: 6-8 Dec. 2
- **Authors**: Sekson Timakul, Itsara Tanyanon, Somsak Choomchuay
- **PDF**: https://ieeexplore.ieee.org/document/5704671
- **Abstract**: This paper presents overlapping techniques designed for a compact hardware LDPC decoder with MS algorithm. The design is applicable to IEEE 802.11n standard. We elaborate how to reduce hardware and cycle time between row and column operation. The hardware utilization can be better enhanced and 16-40% cycle time reduction compared to a non-overlapping decoder can be achieved.

## Low Complexity Decoding Algorithm of QC-LDPC Code

- **Status**: ✅
- **Reason**: QC-LDPC 저복잡도 layered 디코딩, sub-min을 보정인자+min으로 대체 — 이식 가능 디코더(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5708616
- **Type**: conference
- **Published**: 6-10 Dec. 
- **Authors**: Fanglong Yi, Pengjun Wang
- **PDF**: https://ieeexplore.ieee.org/document/5708616
- **Abstract**: Through the research on the decoding algorithm of low-density parity-check (LDPC) code, a low complexity decoding algorithm suitable for quasi-cyclic LDPC (QC-LDPC) code is proposed in this paper. The algorithm adopts layered decoding (LD), and the sub-minimum is replaced by the sum of an optimal correction factor and the minimum during the process of the check nodes update. Therefore, it is not required to find the sub-minimum and the computational complexity reduces significantly. Matlab simulation results show that the decoding performance of this algorithm is very near to min-sum (MS) algorithm, and more superior than single min-sum (SMS) algorithm.

## Analysis of performance and implementation complexity of simplified algorithms for decoding Low-Density Parity-Check codes

- **Status**: ✅
- **Reason**: LDPC 디코더 복잡도 감소(extrinsic 메시지 길이 스케일다운)+FPGA 구현 — 이식 디코더/HW(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5700356
- **Type**: conference
- **Published**: 6-10 Dec. 
- **Authors**: Vikram Arkalgud Chandrasetty, Syed Mahfuzul Aziz
- **PDF**: https://ieeexplore.ieee.org/document/5700356
- **Abstract**: This paper presents a novel technique to significantly reduce the implementation complexity of Low-Density Parity-Check (LDPC) decoders. The proposed technique uses high precision soft messages at the variable nodes but scales down the extrinsic message length, which reduces the number of interconnections between variable and check nodes. It also simplifies the check node operation. The effect on performance and complexity of the decoders due to such simplification is analyzed. A prototype model of the proposed decoders compliant with the WiMax application standard has been implemented and tested on Xilinx Virtex 5 FPGA. The implementation results show that the proposed decoders can achieve significant reduction in hardware complexity with comparable decoding performance to that of Min-Sum algorithm based decoders. The proposed decoders are estimated to achieve an average throughput in the range of 6-11 Gbps, even with short code lengths.

## An Improvement on the Soft Reliability-Based Iterative Majority-Logic Decoding Algorithm for LDPC Codes

- **Status**: ✅
- **Reason**: 이진 LDPC용 reliability-based iterative majority-logic 디코딩 개선 알고리즘 — 이식 가능 디코더(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5684111
- **Type**: conference
- **Published**: 6-10 Dec. 
- **Authors**: T. M. N. Ngatched, Attahiru S. Alfa, Jun Cai
- **PDF**: https://ieeexplore.ieee.org/document/5684111
- **Abstract**: This paper presents an improvement of the reliability-based iterative majority-logic decoding algorithms for regular low-density parity-check (LDPC) codes proposed by Huang et al. We improve the computation of the extrinsic information that is used to update the reliability measure of each received bit in each iteration with some kind of reliability measures of the check-sums that are orthogonal on the considered bit. The improved algorithm achieves a significant gain over the standard one with only a modest increase in computational complexity.

## LDPC Codes for Memory Systems with Scrubbing

- **Status**: ✅
- **Reason**: 메모리(우주방사선) 대상 LDPC soft-decision ECC, 메모리 채널모델/LLR 계산 - 스토리지 ECC(B)에 가까움
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5683367
- **Type**: conference
- **Published**: 6-10 Dec. 
- **Authors**: Seungjune Jeon, Euiseok Hwang, B. V. K. Vijaya Kumar +1
- **PDF**: https://ieeexplore.ieee.org/document/5683367
- **Abstract**: In space, radiation particles can introduce temporary or permanent errors in memory systems. To protect against potential memory faults, either thick shielding or error correcting codes (ECC) are used. Thick shielding translates into increased mass and conventional ECCs designed for memories are typically capable of only correcting a single error and detecting a double error. Decoding is usually performed through hard-decisions where bits are treated as either correct or flipped in polarity. In this work, we demonstrate that low-density parity-check (LDPC) codes that are already prevalent in many communication applications can also be used to protect memories in space. We develop a channel that models memory error events in a space radiation environment. We describe how to compute soft symbol reliabilities on our channel and compare the performance of soft-decision decoding LDPC codes against conventional hard-decision decoding of Reed-Solomon (RS) codes and Bose-Chaudhuri-Hoquenghem (BCH) codes for a specific memory structure.

## A Class of Generalized Quasi-Cyclic LDPC Codes: High-Rate and Low-Complexity Encoder for Data Storage Devices

- **Status**: ✅
- **Reason**: 바이너리 high-rate QC/GQC-LDPC 코드설계(no 4-cycle, finite geometry)와 O(n) 선형 인코더 HW 아키텍처 제시 — E/D 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5683369
- **Type**: conference
- **Published**: 6-10 Dec. 
- **Authors**: Vo Tam Van, Hajime Matsui, Seiichi Mita
- **PDF**: https://ieeexplore.ieee.org/document/5683369
- **Abstract**: In this paper, we study no 4-cycle, high-rate LDPC codes based on finite geometries for use in data storage devices and prove that these codes cannot be classified as quasi-cyclic (QC) codes but should be considered as broader generalized quasi-cyclic (GQC) codes. Because of the GQC structure of such codes, they can be systematically encoded using Groebner bases and their encoder can be implemented using simple feedback-shift registers. In order to demonstrate the efficiency of the encoder, we show that the hardware complexity of the serial-in serial-out encoder architecture of these codes is of linear order O(n). To encode a binary codeword of length n, less than 2n adders and 3n memory elements are required. Furthermore, we evaluated the error performances of these codes with sum product algorithm (SPA) decoding over additive white Gaussian noise (AWGN) channels. At a bit error rate (BER) of 10^-5, they perform 1-dB away from the Shannon limit after 10 decoding iterations.

## Error characterization and coding schemes for flash memories

- **Status**: ✅
- **Reason**: 플래시 메모리 에러 특성화+코딩 스킴(MLC/SLC), NAND 직접(A)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5700263
- **Type**: conference
- **Published**: 6-10 Dec. 
- **Authors**: Eitan Yaakobi, Jing Ma, Laura Grupp +3
- **PDF**: https://ieeexplore.ieee.org/document/5700263
- **Abstract**: In this work, we use an extensive empirical database of errors induced by write, read, and erase operations to develop a comprehensive understanding of the error behavior of flash memories. Error characterization of MLC and SLC flash is given on the block, page, and bit level. Based on our error characterization in MLC flash, we propose an error-correcting scheme which outperforms the conventional BCH code. We compare several schemes which use an MLC block as an SLC block. Finally, an implementation of two-write WOM-codes in SLC flash is given as well as the BER for the first and second write.

## Attenuated iterative reliability-based decoding algorithm for LDPC codes

- **Status**: ✅
- **Reason**: 신규 AIML reliability-based majority-logic 디코딩 알고리즘, error floor 개선·병렬 디코딩 = 이식 가능 디코더(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5690829
- **Type**: conference
- **Published**: 4-6 Dec. 2
- **Authors**: Minghua Liu, Lijun Zhang
- **PDF**: https://ieeexplore.ieee.org/document/5690829
- **Abstract**: An attenuated iterative reliability-based majority-logic (AIML) decoding algorithm for low-density parity-check (LDPC) codes is proposed. This novel algorithm is devised based on the orthogonal check-sums of the one-step majority-logic decoding algorithm in conjunction with certain of reliability measures of the received symbols. The computation of reliability measure of the syndrome sum is refined by introducing an attenuation factor. Simulation results show that in binary input-additive white Gaussian noise channel, the AIML algorithm outperforms other popular iterative reliability-based majority-logic decoding algorithms with a slight increase in computational complexity. With maximum iterations five and fifty, the AIML algorithm can achieve almost identical error performance for LDPC codes. No error floor effect can be observed for AIML algorithm down to the bit error rate (BER) of 10−8, while error floor appears for sum product algorithm (SPA) around the BER of 10−7 even with maximum iteration 100. The inherent feature of parallel decoding for AIML algorithm enforces the decoding speed in contrast to those serial decoding schemes, such as weighted bit-flipping algorithm.

## Low-complexity high-performance LDPC decoder for CMMB

- **Status**: ✅
- **Reason**: CMMB LDPC 디코더 신규 메모리 압축 전략(50%↓)·semi-parallel FPGA 구현 = 이식 가능 HW(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:5688606
- **Type**: conference
- **Published**: 4-6 Dec. 2
- **Authors**: Taiqiu Tan, Yubai Li, Chang Wu
- **PDF**: https://ieeexplore.ieee.org/document/5688606
- **Abstract**: A low-complexity semi-parallel low density parity check (LDPC) decoder for China Mobile Multimedia Broadcasting (CMMB) system is designed based on the structure of LDPC codes. The designed decoder utilizes turbo decoding message passing algorithm. A new memory compressing strategy for message updating was proposed, which can reduce more than 50% memories. By using them appropriately, two different code rates can reuse memories without increasing any hardware resource. The decoder is implemented on FPGA of Altera Stratix II. The throughput of the LDPC decoder is up to 40Mbps under CMMB work point, which can fulfill the request of real time decoding.

## Iterative soft decoding of Reed-Solomon codes using information correction

- **Status**: ✅
- **Reason**: RS 코드용이나 bit-level BP에서 4-cycle 줄인 확장 패리티검사 + 정보보정(최저신뢰 비트 채널정보 변경) 기법은 부호 비의존적이고 바이너리 LDPC BP에 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5734050
- **Type**: conference
- **Published**: 4-6 Dec. 2
- **Authors**: Farnaz Shayegh, M. Reza Soleymani
- **PDF**: https://ieeexplore.ieee.org/document/5734050
- **Abstract**: A new iterative soft decision decoding method with very low complexity for Reed-Solomon (RS) codes is proposed. This method is based on bit level belief propagation (BP) decoding. In order to make BP decoding effective for RS codes, we use an extended binary parity check matrix with a lower density and reduced number of 4-cycles compared to the original binary parity check matrix of the code. Our proposed method is based on information correction in BP decoding. It means that we determine least reliable bits and by changing their channel information, the convergence of the decoder is improved. Our method results in considerable performance improvement of RS codes compared to hard decision decoding. The performance is also superior or comparable to some popular soft decision decoding methods.

## Differential Decoding of Low-Density Parity-Check Codes Based on Min Sum Algorithm

- **Status**: ✅
- **Reason**: min-sum 기반 차분 디코딩 알고리즘 신규 제안, 바이너리 LDPC BP에 이식 가능한 디코더 기법(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5945169
- **Type**: conference
- **Published**: 24-26 Dec.
- **Authors**: Shizhang Peng, Zemao Zhao, Jianrong Bao
- **PDF**: https://ieeexplore.ieee.org/document/5945169
- **Abstract**: To improve performance and reduce computation complexity of the low-density parity-check (LDPC) codes, a min-sum based differential decoding algorithm is proposed. The main principle is that the messages passing in the bipartite graph of the codes are the probability differences and the updates of the check nodes adopt min sum algorithm. Simulation results show that the proposed algorithm can achieve about 0.4dB performance gain over the UMP BP-Based decoding algorithm at bit error rate (BER) of under an additive white Gaussian noise (AWGN) channel. And it can obtain good performance very close to that of the BP decoding algorithm with much lower complexity.

## Construction of a multi-level Hierarchical Quasi-Cyclic matrix with layered permutation for partially-parallel LDPC decoders

- **Status**: ✅
- **Reason**: 다층 Hierarchical QC 행렬 구성 기법(코드설계 E) + 부분병렬 디코더 HW 자원절감(D), 바이너리 LDPC
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:5723842
- **Type**: conference
- **Published**: 23-25 Dec.
- **Authors**: Vikram Arkalgud Chandrasetty, Syed Mahfuzul Aziz
- **PDF**: https://ieeexplore.ieee.org/document/5723842
- **Abstract**: Implementation of partially-parallel (Low-Density Parity-Check) LDPC decoders using unstructured random matrices is very complex and requires huge hardware resources. To alleviate the complexity and minimize resource requirements, structured LDPC matrices are used. This paper presents a novel technique for constructing a multi-level Hierarchical Quasi-Cyclic (HQC) structured matrix for LDPC decoders. A unique multi-level structure of the proposed matrix provides flexibility in generating different code lengths and code rates for various applications such as WiMAX, WLAN and DVB-S2. In addition, different combinations of permuted sub-matrices are inserted in layers, to provide virtual randomness in the LDPC matrix. Simulations results show that the HQC matrices generated using the proposed technique have a marginal loss of less than 0.1 dB at a bit error rate (BER) performance of 10-5, compared to unstructured random matrices. The proposed matrix therefore provides BER performance close to random matrices while significantly reducing hardware resource requirements.

## Improved method for detecting the short cycles of LDPC codes

- **Status**: ✅
- **Reason**: LDPC 단주기(4/6/8/10-cycle) 검출 개선 기법 — 사이클 제거/코드설계(E)에 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5689706
- **Type**: conference
- **Published**: 17-19 Dec.
- **Authors**: Pan Hu, Hongyu Zhao
- **PDF**: https://ieeexplore.ieee.org/document/5689706
- **Abstract**: It is well known that the short cycles in Tanner Graph (TG) greatly impact on the iterative decoding performance of low density parity check (LDPC) codes. In previous literature two methods can be found for detecting such short cycles. This paper presents an improved version of previous Jun Fan's method, which is based on combinational analysis and enumeration of the check matrix patterns caused by cycles of length of 4, 6, 8 and 10 in the corresponding TG. The improved method can more exactly detect the cycles of length greater than 4 in comparison with Jun Fan's method. The validation of the proposed method can be verified by the detection results of short cycles for some LPDC codes.

## Quantifying the wave-effect of irregular LDPC codes based on majority-based hard-decoding

- **Status**: ✅
- **Reason**: 불규칙 LDPC 유한길이 wave-effect 정량화로 런타임 degree profile 최적화 — 코드설계 기법(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5709742
- **Type**: conference
- **Published**: 13-15 Dec.
- **Authors**: Asad Mahmood
- **PDF**: https://ieeexplore.ieee.org/document/5709742
- **Abstract**: Irregular LDPC codes have shown to give performances closer to capacity than their regular counterparts. The intuitive reasoning backed by experimental evidence given by its founder (Luby et al.) was the presence of a wave-effect. It was shown that only with the presence of a carefully optimized irregularity degree profile, comes the better performance. Conventionally this irregularity profile is optimized employing asymptotic assumptions which studies have shown result in poor performance measures in finite-length codes. Also, the conventional techniques are computationally expensive which makes their use inappropriate in cases, e.g. multicarrier, where run-time optimization of the irregularity profile may be needed. This paper proposes a simplistic technique for precise quantification of the wave-effect phenomenon in irregular codes and hence can be used for run-time optimization of irregularity in finite length codes which may not be possible with classical methods.

## Analog realization of iterative threshold decoding based on high-order recurrent neural networks

- **Status**: ✅
- **Reason**: 바이너리 선형부호 반복 임계디코딩의 아날로그/RNN VLSI 구현 — 이식 가능 HW 아키텍처(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:5709726
- **Type**: conference
- **Published**: 13-15 Dec.
- **Authors**: Mohamad Mostafa, Werner G. Teich, Jürgen Lindner
- **PDF**: https://ieeexplore.ieee.org/document/5709726
- **Abstract**: Artificial neural networks (ANN) are known for their ability to solve classification and optimization tasks and have been applied in many fields of communications such as equalization and multiuser detection, among others. In this paper an analog realization of iterative threshold decoding for binary linear codes is presented. It is shown that the iterative threshold decoding algorithm matches well with the structure of a continuous high-order recurrent neural network. The performance of the analog realization has been evaluated by simulation and is compared with the corresponding digital realisation. The motivation of this work is that analog decoding improves the power/speed ratio and minimizes the area consumption on the very large scale integration (VLSI) chip.

## Design of parallel LDPC interleaver architecture: A bipartite edge coloring approach

- **Status**: ✅
- **Reason**: 병렬 LDPC 인터리버 아키텍처: 메모리 맵핑 충돌 해결 bipartite edge coloring — 이식 가능 HW(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:5724550
- **Type**: conference
- **Published**: 12-15 Dec.
- **Authors**: Awais Sani, Philippe Coussy, Cyrille Chavet +1
- **PDF**: https://ieeexplore.ieee.org/document/5724550
- **Abstract**: Parallel hardware architecture proves to be an excellent compromise between area, cost, flexibility and high throughput in the hardware design of LDPC decoder. However, this type of architecture suffers from memory mapping problem: concurrent read and write accesses to data have to be performed at each time instance without any conflict. In this paper, we present an original approach based on the tanner graph modeling and a modified bipartite edge coloring algorithm to design parallel LDPC interleaver architecture.

## Design of a novel multi-rate QC-LDPC decoder

- **Status**: ✅
- **Reason**: 신규 멀티레이트 QC-LDPC 디코더 HW 아키텍처(layered+semi-parallel, 간접 메시지 저장, 동시 처리) 제시 → 이식 가능 HW(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:5687430
- **Type**: conference
- **Published**: 10-12 Dec.
- **Authors**: Pengjun Wang, Fanglong Yi, Xiaofang Zhou
- **PDF**: https://ieeexplore.ieee.org/document/5687430
- **Abstract**: Based on layered decoding and semi-parallel structure, a novel architecture of multi-rate QC-LDPC decoder is proposed in this paper. It can support any code rates without any changes in hardware to achieve higher hardware utilization. The update of current layer and the comparison of next layer are processed simultaneously to improve the throughput. The check-to-variable messages are stored indirectly to reduce the storage space. Based on the proposed architecture, a QC-LDPC decoder of 2304 bits and 6-encodings style is presented. Then ModelSim SE6.0 simulation results verify that the proposed decoder is correct and effective. Finally, the decoder is synthesized by Synopsys Design Compiler on SMIC 0.18 µm CMOS technology, and the maximum throughput can achieve 318 Mbps at 145 MHz and 15 iterations.
