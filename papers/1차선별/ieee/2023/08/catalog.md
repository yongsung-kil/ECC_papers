# IEEE Xplore — 2023-08 (1차선별 통과)


## A Task-Guided Normalized Min-Sum Decoding Network for LDPC Codes-Based DJSCC

- **Status**: ✅
- **Reason**: 공유 신경 정규화 min-sum(SNNMS) 디코딩 네트워크 — 신경망 min-sum 디코더 변형으로 NAND LDPC에 이식 가능(C). DJSCC 응용이나 디코더 기법 자체는 떼어낼 수 있음
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10138824
- **Type**: journal
- **Published**: Aug. 2023
- **Authors**: Jianhong Yang, Shaohua Hong, Lin Wang
- **PDF**: https://ieeexplore.ieee.org/document/10138824
- **Abstract**: Distributed joint source-channel coding (DJSCC) refers to the correlated sources which are encoded separately and reconstructed in the centre node by joint decoding. Therefore, the challenging problem involves designing a simple and efficient decoding algorithm to utilize the correlations among distributed sources. In this letter, a multi-task deep learning decoder is proposed for the low-density parity-check (LDPC) code-based DJSCC system to improve the performance. This proposal is based on the shared neural normalized min-sum (SNNMS) decoding network and the log likelihood ratio (LLR) shared unit is added to further exploit the source correlation. Moreover, an adaptive multi-loss function is proposed to prevent the network tilting the balance in favor of one certain task. Simulation results indicate that the proposed decoder can achieve a significant performance improvement with almost the same complexity compared with the separated SNNMS decoders.

## Improving LDPC-Coded PNC Decoders via Informed Dynamic Scheduling

- **Status**: ✅
- **Reason**: LDPC 디코더 informed dynamic scheduling(체크노드 업데이트 순서) 신기법 — PNC 무관하게 스케줄링 부분 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10138607
- **Type**: journal
- **Published**: Aug. 2023
- **Authors**: Caizheng Huang, Pingping Chen, Zhaopeng Xie +1
- **PDF**: https://ieeexplore.ieee.org/document/10138607
- **Abstract**: To decode the transmit message pairs and then obtain the exclusive OR (XOR) message, this letter proposes the double-reliability-based decoding (DRB) algorithms with informed dynamic scheduling (IDS) for low-density parity-check (LDPC) coded physical-layer network coding (PNC) systems. The proposed DRB decoding with informed stability (IS-DRB) utilizes a new stability measure to determine the update order of the check nodes. Moreover, by exploiting the principle of PNC decoding, we present an improved IS-DRB (IIS-DRB) decoding to select the check node with unsatisfied PNC mapped checksum and the large stability to update first. This is due to that message propagated from this check node can quickly correct the variable node that causes unsatisfied checksum. Simulation results show that the proposed algorithms can realize significant performance improvement of about 0.5 dB over the conventional DRB decoding with the limited increase in complexity.

## Self-Connected Spatially Coupled LDPC Codes With Improved Termination

- **Status**: ✅
- **Reason**: Self-connected SC-LDPC 부호 설계 — 새 종단(termination) 방법과 self-connection으로 디코딩 임계값 개선, 바이너리 코드 설계 기여(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10172070
- **Type**: journal
- **Published**: Aug. 2023
- **Authors**: Yihuan Liao, Min Qiu, Jinhong Yuan
- **PDF**: https://ieeexplore.ieee.org/document/10172070
- **Abstract**: This letter investigates the design of self-connected spatially coupled low-density parity-check (SC-LDPC) codes. First, a termination method is proposed to reduce rate loss. Particularly, a single-side open SC-LDPC ensemble is introduced, which halves the rate loss of a conventional terminated SC-LDPC by reducing the number of check nodes. We further propose a self-connection method that allows reliable information to propagate from several directions to improve the decoding threshold. We demonstrate that the proposed ensembles not only achieve a better trade-off between rate loss and gap to capacity than several existing protograph SC-LDPC codes with short chain lengths but also exhibit threshold saturation behavior. Finite blocklength error performance is provided to exemplify the superiority of the proposed codes over conventional protograph SC-LDPC codes.

## Rate-Diverse Multiple Access Over Gaussian Channels

- **Status**: ✅
- **Reason**: rate-diverse용 LDPC 행렬 구성(row-combining/row-extending) 신기법 — 코드 설계(E)로 이식 가능성 있어 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10014659
- **Type**: journal
- **Published**: Aug. 2023
- **Authors**: Pingping Chen, Long Shi, Yi Fang +2
- **PDF**: https://ieeexplore.ieee.org/document/10014659
- **Abstract**: In this work, we develop a pair of rate-diverse encoder and decoder for a two-user Gaussian multiple access channel (GMAC). The proposed scheme enables the users to transmit with the same codeword length but different coding rates under diverse user channel conditions. First, we propose the row-combining (RC) method and row-extending (RE) method to design practical low-density parity-check (LDPC) channel codes for rate-diverse GMAC. Second, we develop an iterative rate-diverse joint user messages decoding (RDJD) algorithm for GMAC, where all user messages are decoded with a single parity-check matrix. In contrast to the conventional network-coded multiple access (NCMA) and compute-forward multiple access (CFMA) schemes that first recover a linear combination of the transmitted codewords and then decode both user messages, this work can decode both the user messages simultaneously. Extrinsic information transfer (EXIT) chart analysis and simulation results indicate that RDJD can achieve gains up to 1.0 dB over NCMA and CFMA in the two-user GMAC. In particular, we show that there exists an optimal rate allocation for the two users to achieve the best decoding performance given the channel conditions and sum rate.

## Finite-Length Scaling of SC-LDPC Codes With a Limited Number of Decoding Iterations

- **Status**: ✅
- **Reason**: 제한된 반복수 하 SC-LDPC 유한길이 스케일링 법칙 — 이식 가능 코드 설계/디코더 분석(E), 바이너리
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10068559
- **Type**: journal
- **Published**: Aug. 2023
- **Authors**: Roman Sokolovskii, Alexandre Graell i Amat, Fredrik Brännström
- **PDF**: https://ieeexplore.ieee.org/document/10068559
- **Abstract**: We propose four finite-length scaling laws to predict the frame error rate (FER) performance in the waterfall region of spatially-coupled low-density parity-check code ensembles under full belief propagation (BP) decoding with a limit on the number of decoding iterations and a scaling law for sliding window decoding, also with limited iterations. The laws for full BP decoding provide a choice between accuracy and computational complexity; a good balance between them is achieved by the law that models the number of decoded bits after a certain number of BP iterations by a time-integrated Ornstein-Uhlenbeck process. This framework is developed further to model sliding window decoding as a race between the integrated Ornstein-Uhlenbeck process and an absorbing barrier that corresponds to the left boundary of the sliding window. The proposed scaling laws yield accurate FER predictions for the semi-structured code ensembles proposed by Olmos and Urbanke.

## Efficient FPGA-based LDPC Encoder Implementation for Optical Communication Systems

- **Status**: ✅
- **Reason**: ITU-T G975.1 LDPC 인코더 FPGA 구현, RU 알고리즘 변형·전처리로 자원/지연 감소 — 이식 가능 HW(D)/구성, 바이너리 스토리지급 LDPC
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:10236181
- **Type**: conference
- **Published**: 31 July-3 
- **Authors**: Yu Liu, Wenhua Gu, Zhen Mei +1
- **PDF**: https://ieeexplore.ieee.org/document/10236181
- **Abstract**: The low-density-parity-code (LDPC) code has been suggested as a forward error correction code in the ITU-T G975.1 protocol for optical communications. However, the traditional LDPC encoding method causes high latency or excessive resource usage, which may degrade the encoder’s throughput and performance. In this paper, we propose an efficient encoder implementation of the LDPC code in the ITU-T G975.1 protocol based on field programmable gate arrays (FPGA). Specifically, the Richardson-Urbanke (RU) algorithm is modified by incorporating the structural characteristics of the parity check matrix that corresponds to the ITU-T G975.1 protocol, along with specific preprocessing techniques. This approach not only simplifies the encoding process but also makes it more suitable for hardware implementation. Our implementation significantly reduces resource consumption and encoding delay compared with existing methods, achieving a throughput of 10Gbps rate.

## Layered Asymmetrically Clipped Optical SCFDM based on Adaptive LDPC Puncturing for IM/DD Transmission System

- **Status**: ✅
- **Reason**: 적응형 LDPC puncturing 기법 제안 — 코드 레이트 조정/펑처링은 NAND LDPC 코드설계에 이식 가능(E), 애매하므로 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10236264
- **Type**: conference
- **Published**: 31 July-3 
- **Authors**: Yikun Yang, Dong Guo, Qi Zhang +6
- **PDF**: https://ieeexplore.ieee.org/document/10236264
- **Abstract**: An adaptive LDPC puncturing method suitable for L-ACO-SCFDM is proposed. The simulation results show that it can obtain 6~7dB sensitivity gain compared with conventionalL-ACO-SCFDM and have potential application in short-distance IM/DD optical transmission system.

## Performance of IR-HARQ-based RC-LDPC Code Extension in Optical Satellite Systems

- **Status**: ✅
- **Reason**: code extension 기반 RC-LDPC 코드 패밀리 구성(IR-HARQ); rate-compatible LDPC 코드 설계(E)로 이식 가능성 있어 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10234057
- **Type**: conference
- **Published**: 23-25 Aug.
- **Authors**: Cuong T. Nguyen, Hoang D. Le, Anh T. Pham
- **PDF**: https://ieeexplore.ieee.org/document/10234057
- **Abstract**: This paper studies the link-layer error-control solutions for low Earth orbit (LEO) satellite-based free-space optical (FSO) communications. Specifically, we address the design of low-density parity check (LDPC) codes for incremental redundancy (IR) hybrid automatic repeat request (HARQ) protocols. To facilitate the IR-HARQ operation, a rate-compatible (RC)-LDPC code family constructed by the code extension method is used. Performance metrics, including goodput and energy efficiency, are investigated. Simulation results confirm the effectiveness of our proposed design compared to existing solutions over the state-of-the-art. The results also support the proper selection of the LEO satellite’s transmitted powers based on the trade-off between goodput and energy efficiency.

## On Disjoint Difference Sets and Their Associated QC-LDPC Codes with Large Girth

- **Status**: ✅
- **Reason**: DDS 기반 QC-LDPC 신규 구성(all-zero circulant 포함, girth 8/10) — 바이너리 코드 설계 기법 이식 가능(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10233824
- **Type**: conference
- **Published**: 10-12 Aug.
- **Authors**: Guohua Zhang, Mengdi Ni, Yi Fang
- **PDF**: https://ieeexplore.ieee.org/document/10233824
- **Abstract**: The disjoint difference set (DDS) has been utilized in recent years to construct quasi-cyclic (QC) low-density parity-check (LDPC) codes without small cycles. However, the existing DDS-based QC-LDPC codes have no all-zero circulants, which limits the decoding performance of such codes to some extent. In this paper, two new types of DDS-based QC-LDPC codes are proposed, which contain all-zero circulants and possess girth at least eight and girth at least ten, respectively. Numerical simulations show that the new codes have good performance in AWGN channels. Besides, a new result on existence for DDSs and two novel deterministic constructions for DDSs are put forward.

## An Efficient Joint Decoding Scheme for Outer Codes in DNA-Based Data Storage

- **Status**: ✅
- **Reason**: DNA 스토리지 outer code joint decoding, 바이너리 LDPC 신뢰도 기반 재디코딩 기법 이식 검토 가치(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10233840
- **Type**: conference
- **Published**: 10-12 Aug.
- **Authors**: Yi Ding, Xuan He, Kui Cai +3
- **PDF**: https://ieeexplore.ieee.org/document/10233840
- **Abstract**: In this paper, we consider a simplified system model for DNA-based data storage, where each DNA string is either correctly transmitted, or being erased, or being corrupted by random substitution errors, and all strings are randomly shuffled with each other. Any linear block error-correction code can be used as the outer code to encode bits among different strings. We derive soft/hard information of all bits, which allows to independently decode each bit within a string, leading to an independent decoding scheme. To improve the decoding performance, we measure the reliability of each string based on the independent decoding result, and perform a further step of decoding over the most reliable strings, leading to a joint decoding scheme. Simulations with low-density parity-check codes confirm that the joint decoding scheme can reduce the frame error rate by more than 3 orders of magnitude compared to the independent decoding scheme.

## Soft OSD-Sliding Window Decoding for Staircase LDPC Codes in Deep Space Communications

- **Status**: ✅
- **Reason**: Soft OSD sliding-window decoder for staircase binary LDPC — new SOSD-SWD decoding algorithm transplantable to NAND LDPC (C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10233519
- **Type**: conference
- **Published**: 10-12 Aug.
- **Authors**: Yaosheng Zhang, Jian Jiao, Yasong Wang +3
- **PDF**: https://ieeexplore.ieee.org/document/10233519
- **Abstract**: In this paper, we propose a soft ordered statistic decoder (SOSD) sliding window decoding (SWD) algorithm for staircase low density parity check (LDPC) codes in deep space optical communications. First, according to the relative position variation of Earth-to-Mars during a conjunction cycle, we model a related optical channel model by calculating the scintillation index in the Gamma-Gamma distribution, which divide three states due to the Sun-Earth-Mars (SEM) angle. Then, we propose the SOSD-SWD algorithm for the rate-adaptive staircase LDPC codes for the channel model, which can approach to 10−4bit error rate (BER) under the three channel states with adjustable decoding parameters. Simulation results validate the impact of different parameters of the SOSD-SWD algorithm, and shed light to tradeoff the achievable BER and complexities under different channel conditions, and the proposed SOSD-SWD algorithm can achieve lower BER than the related SWD algorithms for staircase LDPC codes.

## A Low-Latency Iterative Decoding Architecture for MIMO-VLC Systems with GSM

- **Status**: ✅
- **Reason**: Internal-stopping JDD for protograph binary LDPC — new joint detection/decoding stopping technique, transplantable decoder method (C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10233708
- **Type**: conference
- **Published**: 10-12 Aug.
- **Authors**: Zhaojie Yang, Yi Fang, Liang Lv +2
- **PDF**: https://ieeexplore.ieee.org/document/10233708
- **Abstract**: This paper investigates a low-latency iterative decoding architecture for multiple-input multiple-output (MIMO) visible light communication (VLC) systems. Particularly, protograph-based low-density parity-check (P-LDPC) codes are considered. To be specific, we introduce a novel internal-stopping (IS) principle into the conventional joint detection and decoding (JDD) algorithm, and then develop an IS-based JDD (IS-JDD) version. The proposed IS-JDD algorithm can reduce the computational overhead without sacrificing system performance. Numerical results verify that the proposed design can outperform existing benchmark algorithms.
