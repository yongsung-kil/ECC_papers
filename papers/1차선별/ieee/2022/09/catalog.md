# IEEE Xplore — 2022-09 (1차선별 통과)


## Design of Protograph-Based LDPC Codes for Two-User Gaussian Multiple Access Channel

- **Status**: ✅
- **Reason**: 프로토그래프 기저행렬 설계·JP-EXIT 분석 기법, 다중접속 특화이나 코드설계 기법 이식 여지 — 애매해 in(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9828486
- **Type**: journal
- **Published**: Sept. 2022
- **Authors**: Xiaodan Li, Pingping Chen, Yi Fang +1
- **PDF**: https://ieeexplore.ieee.org/document/9828486
- **Abstract**: In this letter, we study the performance of protograph-based low-density parity-check (LDPC) codes for two-user Gaussian multiple access channel (GMAC). Considering the characteristic of a joint protograph of two users, we first derive a joint protograph-based extrinsic information transfer (JP-EXIT) chart to analyze the iterative user decoding behavior of two-user GMAC. Guided by the JP-EXIT, we further propose a new design scheme and construct protograph base matrices of different code rates for two users, respectively. Both theoretical analyses and simulation results show that the proposed protograph-based LDPC codes of low decoding threshold outperform the conventional irregular LDPC codes for both equal-power and unequal-power GMAC with different code rates.

## Design of Protograph LDPC Codes Using Resolvable Block Designs for Block Fading Channel

- **Status**: ✅
- **Reason**: resolvable block design 기반 신규 프로토그래프 바이너리 LDPC 구성 + gamma evolution 분석, 이식 가능 코드 설계(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9826818
- **Type**: journal
- **Published**: Sept. 2022
- **Authors**: Jaewha Kim, Chanki Kim, Hosung Park +1
- **PDF**: https://ieeexplore.ieee.org/document/9826818
- **Abstract**: In this letter, we propose new protograph low-density parity-check (LDPC) codes of high code rates using resolvable block designs (RBDs) for block fading (BF) channels. To analyze the performance of the proposed LDPC codes, we derive an upper bound on bit error rate (BER) using the novel method, called the gamma evolution. Finally, we numerically show that the frame error rate (FER) of the proposed LDPC codes has a slope approaching the channel outage probability.

## Overcoming Data Availability Attacks in Blockchain Systems: Short Code-Length LDPC Code Design for Coded Merkle Tree

- **Status**: ✅
- **Reason**: 새 LDPC 코드 구성(EC-PEG/LC-PEG, PEG 변형)으로 stopping set 제어 — 바이너리 코드설계 기법(E) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9841605
- **Type**: journal
- **Published**: Sept. 2022
- **Authors**: Debarnab Mitra, Lev Tauz, Lara Dolecek
- **PDF**: https://ieeexplore.ieee.org/document/9841605
- **Abstract**: Light nodes in blockchains improve the scalability of the system by storing a small portion of the blockchain ledger. In certain blockchains, light nodes are vulnerable to a data availability (DA) attack where a malicious node makes the light nodes accept an invalid block by hiding the invalid portion of the block from the nodes in the system. Recently, a technique based on LDPC codes called Coded Merkle Tree (CMT) was proposed by Yu et al. that enables light nodes to detect a DA attack by randomly requesting/sampling portions of the block from the malicious node. However, light nodes fail to detect a DA attack with high probability if a malicious node hides a small stopping set of the LDPC code. To mitigate this problem, Yu et al. used random LDPC codes that achieve large minimum stopping set size with high probability. Although effective, these codes are not necessarily optimal for this application, especially at short code lengths, which are relevant for low latency systems, IoT blockchains, etc.. In this paper, we focus on short code lengths and demonstrate that a suitable co-design of specialized LDPC codes and the light node sampling strategy can improve the probability of detection of DA attacks. We consider different adversary models based on their computational capabilities of finding stopping sets in LDPC codes. For a weak adversary model, we devise a new LDPC code construction termed as the entropy-constrained PEG (EC-PEG) algorithm which concentrates stopping sets to a small group of variable nodes. We demonstrate that the EC-PEG algorithm coupled with a greedy sampling strategy improves the probability of detection of DA attacks. For stronger adversary models, we provide a co-design of a sampling strategy called linear-programming-sampling (LP-sampling) and an LDPC code construction called linear-programming-constrained PEG (LC-PEG) algorithm. The new co-design demonstrates a higher probability of detection of DA attacks compared to approaches in earlier literature.

## Hybrid Stochastic LDPC Decoder With Fully Correlated Stochastic Computation

- **Status**: ✅
- **Reason**: Hybrid Stochastic LDPC 디코더, min-sum 구현 새 CN/VN HW 아키텍처(C/D) — NAND LDPC 디코더 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9791320
- **Type**: journal
- **Published**: Sept. 2022
- **Authors**: Shuai Hu, Kaining Han, Fujie Wang +1
- **PDF**: https://ieeexplore.ieee.org/document/9791320
- **Abstract**: The ultra-low hardware consumption feature of stochastic decoding has made it a potential candidate for the implementation of low-density parity-check(LDPC) decoders. However, the existing stochastic LDPC decoders still suffer from performance degradation and relatively high decoding cycles caused by the correlation among stochastic bit streams. In this paper, we propose Hybrid Stochastic(HS) decoding, which achieves high performance, high throughput, and high hardware efficiency by jointly using our proposed novel stochastic check node(CN) and Two’s Complement(TCS) variable node(VN) to realize Min-Sum Algorithm(MSA) and its enhancements. Fully correlated stochastic bit streams are used to entirely eliminate the indeterminacy caused by the correlation, which results in high performance and fast convergence and inherits the low complexity of stochastic decoders at the same time. We demonstrate the HS decoding by designing a (2048,1723) decoder in a 65 nm process, which achieves the highest Bit-Error-Ratio(BER) performance, highest throughput, and top hardware efficiency among existing stochastic LDPC decoders. We also demonstrate that HS decoding can achieve excellent decoding performance for different code rates and lengths 5G New Radio(NR) LDPC codes. Thus, HS decoding can be adopted in wide applications.

## A Unifying Framework to Construct QC-LDPC Tanner Graphs of Desired Girth

- **Status**: ✅
- **Reason**: QC-LDPC Tanner 그래프 girth 구성 통합 프레임워크 — 바이너리 코드설계(E) 새 기여, NAND LDPC 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9762914
- **Type**: journal
- **Published**: Sept. 2022
- **Authors**: Roxana Smarandache, David G. M. Mitchell
- **PDF**: https://ieeexplore.ieee.org/document/9762914
- **Abstract**: This paper presents a unifying framework to construct low-density parity-check (LDPC) codes with associated Tanner graphs of desired girth. Towards this goal, we highlight the role that a certain square matrix that appears in the product of the parity-check matrix with its transpose has in the construction of codes with graphs of desired girth and further explore it in order to generate the set of necessary and sufficient conditions for a Tanner graph to have a given girth between 6 and 12. For each such girth, we present algorithms to construct codes of the desired girth and we show how to use them to compute the minimum necessary value of the lifting factor. For girth larger than 12, we show how to use multi-step graph lifting methods to deterministically modify codes in order to increase their girth. We also give a new perspective on LDPC protograph-based parity-check matrices by viewing them as rows of a parity-check matrix equal to the sum of certain permutation matrices and obtain an important connection between all protographs and those with variable nodes of degree 2. We also show that the results and methodology that we develop for the all-one protograph can be used and adapted to analyze the girth of the Tanner graph of any parity-check matrix and demonstrate how this can be done using a well-known irregular, multi-edge protograph specified by the NASA Consultative Committee for Space Data Systems (CCSDS). Throughout the paper, we exemplify our theoretical results with constructions of LDPC codes with Tanner graphs of any girth between 6 and 14 and give sufficient conditions for a multi-step lifted parity-check matrix to have girth between 14 and 22.

## Spatially Coupled PLDPC-Hadamard Convolutional Codes

- **Status**: ✅
- **Reason**: 신규 SC-PLDPC-Hadamard 부호 구성 + layered PEXIT·유전 알고리즘 설계·layered scheduling 디코딩, 바이너리 protograph 코드설계/디코더(C/E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9841586
- **Type**: journal
- **Published**: Sept. 2022
- **Authors**: Peng-Wei Zhang, Francis C. M. Lau, Chiu-Wing Sham
- **PDF**: https://ieeexplore.ieee.org/document/9841586
- **Abstract**: We propose a new type of ultimate-Shannon-limit-approaching codes called spatially coupled protograph-based low-density parity-check Hadamard convolutional codes (SC-PLDPCH-CCs), which are constructed by spatially coupling PLDPC-Hadamard block codes. We develop an efficient decoding algorithm that combines pipeline decoding and layered scheduling for the decoding of SC-PLDPCH-CCs, and analyze the latency and complexity of the decoder. To estimate the decoding thresholds of SC-PLDPCH-CCs, we first propose a layered protograph extrinsic information transfer (PEXIT) algorithm to evaluate the thresholds of spatially coupled PLDPC-Hadamard terminated codes (SC-PLDPCH-TDCs) with a moderate coupling length. With the use of the proposed layered PEXIT method, we develop a genetic algorithm to find good SC-PLDPCH-TDCs in a systematic way. Then we extend the coupling length of these SC-PLDPCH-TDCs to form good SC-PLDPCH-CCs. Results show that our constructed SC-PLDPCH-CCs can achieve comparable thresholds to the block code counterparts. Simulations illustrate the superiority of the SC-PLDPCH-CCs over the block code counterparts and other state-of-the-art low-rate codes in terms of error performance. For the rate-0.00295 SC-PLDPCH-CC, a bit error rate of 10−5 is achieved at  $E_{b}/N_{0} = -1.465$  dB, which is only 0.125 dB from the ultimate Shannon limit.

## Sub-Block Rearranged Staircase Codes

- **Status**: ✅
- **Reason**: 신규 SR-staircase 부호 구성·iBDD 임계/error floor 분석, 스토리지용 ECC 코드 설계 — 애매하나 in으로 보류(B/E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9812617
- **Type**: journal
- **Published**: Sept. 2022
- **Authors**: Min Qiu, Jinhong Yuan
- **PDF**: https://ieeexplore.ieee.org/document/9812617
- **Abstract**: We propose a new family of spatially coupled product codes, called sub-block rearranged staircase (SR-staircase) codes. Each code block of SR-staircase codes is obtained by encoding rearranged preceding code blocks and new information blocks, where the rearrangement involves sub-blocks decomposition and transposition. The proposed codes can be constructed to have each code block size of  $1/q$  to that of the conventional staircase codes while having the same rate and component codes, for any positive integer  $q$ . In this regard, we can use strong algebraic component codes to construct SR-staircase codes with a similar or the same code block size and rate as staircase codes with weak component codes. We characterize the decoding threshold of the proposed codes under iterative bounded distance decoding (iBDD) by using density evolution. We also derive the conditions under which they achieve a better decoding threshold than that of staircase codes. Further, we investigate the error floor performance by analyzing the contributing error patterns and their multiplicities. Both theoretical and simulation results show that the designed SR-staircase codes outperform staircase codes in terms of waterfall and error floor while the performance can be further improved by using a large coupling width.

## An Efficient Reconfigurable Encoder for the IEEE 1901 Standard

- **Status**: ✅
- **Reason**: IEEE1901 LDPC-CC 인코더 재구성형 병렬화 HW 아키텍처(D) — NAND LDPC HW 이식 여지, 애매하여 살림
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:9784929
- **Type**: journal
- **Published**: Sept. 2022
- **Authors**: Yuxing Chen, Hangxuan Cui, Zhongfeng Wang
- **PDF**: https://ieeexplore.ieee.org/document/9784929
- **Abstract**: The IEEE 1901 standard for power line communication (PLC) enables simple connection among Internet of Things devices. The forward error correction (FEC) codes specified in the IEEE 1901 standard include low-density parity-check convolutional codes (LDPC-CCs) and Reed-Solomon convolutional concatenated (RSCC) codes. This work introduces an efficient reconfigurable encoder in full compliance with the IEEE 1901 standard. First, we propose a reconfigurable LDPC-CC encoder to fulfill the multirate requirement and improve the architecture by fine-tuned parallelization, which takes full advantage of the characteristics of the codeword structure. Then, for area reduction, the optimization regarding the RSCC encoder is extensively exploited. Moreover, the commonality between the encoders is discovered, and some circuitries are shared to reduce the hardware complexity. Equipped with these techniques, an efficient reconfigurable encoder for the IEEE 1901 standard is developed and implemented with 28-nm technology. Implementation results demonstrate that the proposed encoder can meet the throughput requirement of the IEEE 1901 standard and is both power- and area-efficient.

## Improved Layered Normalized Min-Sum Algorithm for 5G NR LDPC

- **Status**: ✅
- **Reason**: DNN으로 정규화 인자 최적화한 layered normalized min-sum 변형 — NAND 디코더에 직접 이식(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9833913
- **Type**: journal
- **Published**: Sept. 2022
- **Authors**: Beeshanga Abewardana Jayawickrama, Ying He
- **PDF**: https://ieeexplore.ieee.org/document/9833913
- **Abstract**: Layered Normalised Min-Sum algorithm is a widely used message passing algorithm for decoding Low Density Parity Check codes. The decoding performance heavily depends on the normalisation factor. Firstly, we leverage the bit structure present in 5G transport blocks to develop an improved decoding algorithm for 5G. Secondly, we determine the optimal normalisation factors of the proposed algorithm using a Deep Neural Network. Performance evaluations show an improvement of 0.3-1.9 dB, with no extra cost on multiplier resources on hardware. Hence, the proposed method is highly attractive for practical 5G decoder implementations.

## Sneak Path Interference-Aware Adaptive Detection and Decoding for Resistive Memory Arrays

- **Status**: ✅
- **Reason**: ReRAM 비휘발성 스토리지 채널 양자화기를 상호정보 최대화로 설계 — NAND LLR 양자화/검출-디코딩에 직접 이식 가능(A/C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9807312
- **Type**: journal
- **Published**: Sept. 2022
- **Authors**: Panpan Li, Kui Cai, Guanghui Song +1
- **PDF**: https://ieeexplore.ieee.org/document/9807312
- **Abstract**: Resistive random-access memory (ReRAM) is an emerging non-volatile memory technology for high-density and high-speed data storage. However, the sneak path interference (SPI) occurred in the ReRAM crossbar array seriously affects its data recovery performance. In this letter, we first propose a quantized channel model of ReRAM, based on which we design both the one-bit and multi-bit channel quantizers by maximizing the mutual information of the channel. A key channel parameter that affects the quantizer design is the sneak path occurrence probability (SPOP) of the memory cell. We first use the average SPOP calculated statistically to design the quantizer, which leads to the same channel detector for different memory arrays. We then adopt the SPOP estimated separately for each memory array for the quantizer design, which is generated by an effective channel estimator and through an iterative detection and decoding scheme for the ReRAM channel. This results in an array-level SPI-aware adaptive detection and decoding approach. Moreover, since there is a strong correlation of the SPI that affects memory cells in the same rows/columns than that affecting cells in different rows/columns, we further derive a column-level scheme which outperforms the array-level scheme. We also propose a channel decomposition method that enables effective ways for theoretically analyzing the ReRAM channel. Simulation results show that the proposed SPI-aware adaptive detection and decoding schemes can approach the ideal performance with three quantization bits, with only one decoding iteration.

## Punctured Binary Simplex Codes as LDPC codes

- **Status**: ✅
- **Reason**: 펑처링된 심플렉스 코드를 rate-adaptive LDPC로 구성(row-column constraint 기반 soft-decision 디코딩) — 새 바이너리 코드 설계 기여(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9934548
- **Type**: conference
- **Published**: 29-30 Sept
- **Authors**: Massimo Battaglioni, Giovanni Cancellieri
- **PDF**: https://ieeexplore.ieee.org/document/9934548
- **Abstract**: Digital data transfer can be protected by means of suitable error correcting codes. Among the families of state-of-the-art codes, LDPC (Low Density Parity-Check) codes have received a great deal of attention recently, because of their performance and flexibility of operation, in wireless and mobile radio channels, as well as in cable transmission systems. In this paper, we present a class of rate-adaptive LDPC codes, obtained as properly punctured simplex codes. These codes allow for the use of an efficient soft-decision decoding algorithm, provided that a condition called row-column constraint is satisfied. This condition is tested on small-length codes, and then extended to medium-length codes. The puncturing operations we apply do not influence the satisfaction of the row-column constraint, assuring that a wide range of code rates can be obtained. We can reach code rates remarkably higher than those obtainable by the original simplex code, and the price in terms of minimum distance turns out to be relatively small, leading to interesting trade-offs in the resulting asymptotic coding gain.

## Noise-Assisted List Decoding for 5G LDPC Codes

- **Status**: ✅
- **Reason**: 바이너리 LDPC용 신규 NMS 리스트 디코더(Na-NMSL) 알고리즘 제안 — NAND LDPC에 이식 가능한 디코더 개선(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10012812
- **Type**: conference
- **Published**: 26-29 Sept
- **Authors**: Jian Gao, Hao Wang, Kuangda Tian
- **PDF**: https://ieeexplore.ieee.org/document/10012812
- **Abstract**: Weak information signals can be detected with the assistance of stochastic perturbation, and nonlinear systems benefit from this phenomenon. Inspired by this, we propose a noise-assisted NMS list (Na-NMSL) algorithm for LDPC decoding. The algorithm consists of L independent NMS decoders, and the inputs of the NMS decoders are generated by adding artificial noise with different strengths to the received signal. When lifting size Z is small, list decoding is performed in the Na-NMSL decoder by utilizing the remaining hardware resources. Therefore, the Na-NMSL decoder enhances the decoding performance of NMS without additional hardware overhead. Simulation results show that the Na-NMSL decoder has a lower block error rate (BLER) and faster convergence than traditional NMS decoding.

## Enhanced Informed Dynamic BP Decoding Scheduling Strategies for 5G NR LDPC Codes

- **Status**: ✅
- **Reason**: RBP 기반 informed dynamic scheduling 디코더 개선 + degree-one VN 자원관리 기법 — NAND LDPC 디코더로 이식 가능한 스케줄링 기여(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10013051
- **Type**: conference
- **Published**: 26-29 Sept
- **Authors**: Tofar C.-Y. Chang, I-Hsiang Lee, Pin-Han Wang +2
- **PDF**: https://ieeexplore.ieee.org/document/10013051
- **Abstract**: We present an enhanced informed dynamic scheduling (IDS) strategy to avoid propagations of unreliable messages in the residual belief-propagation (RBP) algorithm for decoding low-density parity-check (LDPC) codes. To reduce the resource needed for updating the degree-one variable nodes (VNs) in an RBP-based algorithm for decoding 5G New Radio (NR) LDPC codes, we further introduce a process consisting of several simple procedures for managing the resource consumption. Simulation results demonstrate that our RBP algorithm based on the proposed IDS strategy outperforms existing RBP-based algorithms at the early decoding iterations. By using our degree-one VN resource managing approach, the performance of both the proposed and the existing decoders is significantly improved in decoding the 5G NR codes.

## Cell-wise encoding and decoding for TLC flash memories

- **Status**: ✅
- **Reason**: A: TLC NAND 플래시 cell-wise 인코딩/디코딩 + LDPC 적용, NAND 직접
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9937136
- **Type**: conference
- **Published**: 2-6 Sept. 
- **Authors**: Daniel Nicolas Bailon, Sergo Shavgulidze, Jürgen Freudenberger
- **PDF**: https://ieeexplore.ieee.org/document/9937136
- **Abstract**: Automotive computing applications like AI databases, ADAS, and advanced infotainment systems have a huge need for persistent memory. This trend requires NAND flash memories designed for extreme automotive environments. However, the error probability of NAND flash memories has increased in recent years due to higher memory density and production tolerances. Hence, strong error correction coding is needed to meet automotive storage requirements. Many errors can be corrected by soft decoding algorithms. However, soft decoding is very resource-intensive and should be avoided when possible. NAND flash memories are organized in pages, and the error correction codes are usually encoded page-wise to reduce the latency of random reads. This page-wise encoding does not reach the maximum achievable capacity. Reading soft information increases the channel capacity but at the cost of higher latency and power consumption. In this work, we consider cell-wise encoding, which also increases the capacity compared to page-wise encoding. We analyze the cell-wise processing of data in triple-level cell (TLC) NAND flash and show the performance gain when using Low-Density Parity-Check (LDPC) codes. In addition, we investigate a coding approach with page-wise encoding and cell-wise reading.

## Reducing the Error Floor of the Sign-Preserving Min-Sum LDPC Decoder via Message Weighting of Low-Degree Variable Nodes

- **Status**: ✅
- **Reason**: Sign-preserving min-sum 디코더의 error floor를 저차수 변수노드 메시지 가중으로 낮추는 새 기법 — 이식 가능 디코더(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9979226
- **Type**: conference
- **Published**: 18-22 Sept
- **Authors**: Lotte Paulissen, Alex Alvarado, Kaiquan Wu +1
- **PDF**: https://ieeexplore.ieee.org/document/9979226
- **Abstract**: Some low-complexity LDPC decoders suffer from error floors. We apply iteration-dependent weights to the degree-3 variable nodes to solve this problem. When the 802.3ca EPON LDPC code is considered, an error floor decrease of more than 3 orders of magnitude is achieved.

## A Hardware Optimized High Throughput LDPC Decoder Supporting 3 Tb/s in 28 nm CMOS

- **Status**: ✅
- **Reason**: D: 언롤드 LDPC 디코더 파이프라인/플로어플랜 HW 최적화, 28nm 3Tb/s 아키텍처 이식 가능
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:9978104
- **Type**: conference
- **Published**: 12-15 Sept
- **Authors**: Lukasz Lopacinski, Alireza Hasani, Goran Panic +5
- **PDF**: https://ieeexplore.ieee.org/document/9978104
- **Abstract**: This paper proposes an optimized pipelined decoding architecture with seven processing stages for unrolled LDPC decoders. Pipelined design with seven register layers significantly increases the resulting clock frequency. Moreover, we investigate the optimal layout shape for unrolled decoders. This paper's fastest decoder is based on the IEEE 802.11n LDPC(1944,1620) parity-check matrix and achieves 2937 Gb/s of coded throughput after physical design. By optimizing the pipeline, floorplan, and employing a codeword length of 1944 bits, we increased the throughput by 241% compared to the previous fastest LDPC decoder presented in the literature. To the best of our knowledge, it is the fastest soft-decision decoder published so far. The standard min-sum approach is employed for decoding, and the proposed improvements consider changes only on the hardware level.
