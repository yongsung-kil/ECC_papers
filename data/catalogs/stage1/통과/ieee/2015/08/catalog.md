# IEEE Xplore — 2015-08 (1차선별 통과)


## Improving the Belief-Propagation Convergence of Irregular LDPC Codes Using Column-Weight Based Scheduling

- **Status**: ✅
- **Reason**: 불규칙 LDPC용 column-weight 기반 shuffled BP 스케줄링 신규 제안 — 부호 비의존 디코더 수렴 개선 기법(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7122232
- **Type**: journal
- **Published**: Aug. 2015
- **Authors**: Chaudhry Adnan Aslam, Yong Liang Guan, Kui Cai
- **PDF**: https://ieeexplore.ieee.org/document/7122232
- **Abstract**: In this letter, a novel scheduling scheme for decoding irregular low-density parity-check (LDPC) code, based on the column weight of variable nodes in the code graph, is introduced. In this scheme, the irregular LDPC code is decoded using the shuffled belief-propagation (BP) algorithm by selecting the variable nodes in descending order of their column weight. Via numerical simulation, it is shown that the proposed high-to-low column-weight based decoding schedule can noticeably increase the convergence speed at medium to high signal-to-noise ratio (SNR) over AWGN and Rayleigh fading channels without introducing additional complexity or error rate degradation. Furthermore, it is found that the improvement in decoding convergence is proportional to the maximum column-weight in the code graph.

## Rate-compatible LDPC codes based on the PEG algorithm for relay communication systems

- **Status**: ✅
- **Reason**: PEG 알고리즘 변형으로 large-girth full-diversity LDPC 구성 — 코드 설계 기법(E), 바이너리
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7265216
- **Type**: journal
- **Published**: Aug. 2015
- **Authors**: Yangzhao Zhou, Xueqin Jiang, Moon Ho Lee
- **PDF**: https://ieeexplore.ieee.org/document/7265216
- **Abstract**: It is known that the progressive edge-growth (PEG) algorithm can be used to construct low-density parity-check (LDPC) codes at finite code lengths with large girths through the establishment of edges between variable and check nodes in an edge-by-edge manner. In [1], the authors derived a class of LDPC codes for relay communication systems by extending the full-diversity root-LDPC code. However, the submatrices of the parity-check matrix H corresponding to this code were constructed separately; thus, the girth of H was not optimized. To solve this problem, this paper proposes a modified PEG algorithm for use in the design of large girth and full-diversity LDPC codes. Simulation results indicated that the LDPC codes constructed using the modified PEG algorithm exhibited a more favorable frame error rate performance than did codes proposed in [1] over block-fading channels.

## Approximate Algorithms for Identifying Minima on Min-Sum LDPC Decoders and Their Hardware Implementation

- **Status**: ✅
- **Reason**: Min-sum LDPC 디코더의 최소값 식별 근사 알고리즘 + HW 구현, 체크노드 단순화 (C/D) 직접 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7108020
- **Type**: journal
- **Published**: Aug. 2015
- **Authors**: Ioannis Tsatsaragkos, Vassilis Paliouras
- **PDF**: https://ieeexplore.ieee.org/document/7108020
- **Abstract**: This brief introduces algorithms and corresponding circuits that identify minimum values among a set of incoming messages. The problem of finding two minima in a set of messages is approximated by the different problem of finding the minimum of all messages in the set and the second minimum among a subset of the messages. This approximation is here shown to be suitable for hardware low-density parity-check decoders that implement a min-sum (MS) decoding algorithm and its variations. The introduced approximation simplifies the operation performed in a check-node processor and leads to hardware reduction. The proposed schemes outperform other state-of-the-art simplified MS architectures, approaching the error-corrective performance of the normalized MS decoding algorithm.

## New decoding scheme for LDPC codes based on simple product code structure

- **Status**: ✅
- **Reason**: LDPC product code 구조 기반 고SNR 후처리 디코딩 신규 — error floor 개선 디코더(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7265217
- **Type**: journal
- **Published**: Aug. 2015
- **Authors**: Beomkyu Shin, Seokbeom Hong, Hosung Park +2
- **PDF**: https://ieeexplore.ieee.org/document/7265217
- **Abstract**: In this paper, a new decoding scheme is proposed to improve the error correcting performance of low-density parity-check (LDPC) codes in high signal-to-noise ratio (SNR) region by using post-processing. It behaves as follows: First, a conventional LDPC decoding is applied to received LDPC codewords one by one. Then, we count the number of word errors in a predetermined number of decoded codewords. If there is no word error, nothing needs to be done and we can move to the next group of codewords with no delay. Otherwise, we perform a proper post-processing which pro-ducesa new soft-valued codeword (this will befully explained in the main body of this paper) and then apply the conventional LDPC decoding to it again to recover the unsuccessfully decoded codewords. For the proposed decoding scheme, we adopt a simple product code structure which contains LDPC codes and simple algebraic codes as its horizontal and vertical codes, respectively. The decoding capability of the proposed decoding scheme is defined and analyzed using the parity-check matrices of vertical codes and, especially, the combined-decodability is derived for the case of single parity-check (SPC) codes and Hamming codes used as vertical codes. It is also shown that the proposed decoding scheme achieves much better error correcting capability in high SNR region with little additional decoding complexity, compared with the conventional LDPC decoding scheme.

## Iterative reliability-based modified majority-logic decoding for structured binary LDPC codes

- **Status**: ✅
- **Reason**: 구조화 바이너리 LDPC용 반복 신뢰도기반 수정 majority-logic 디코딩, 비균일 양자화 3-4bit 신규 — 저복잡 디코더(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7265215
- **Type**: journal
- **Published**: Aug. 2015
- **Authors**: Haiqiang Chen, Lingshan Luo, Youming Sun +4
- **PDF**: https://ieeexplore.ieee.org/document/7265215
- **Abstract**: In this paper, we present an iterative reliability-based modified majority-logic decoding algorithm for two classes of structured low-density parity-check codes. Different from the conventional modified one-step majority-logic decoding algorithms, we design a turbo-like iterative strategy to recover the performance degradation caused by the simply flipping operation. The main computational loads of the presented algorithm include only binary logic and integer operations, resulting in low decoding complexity. Furthermore, by introducing the iterative set, a very small proportion (less than 6%) of variable nodes are involved in the reliability updating process, which can further reduce the computational complexity. Simulation results show that, combined with the factor correction technique and a well-designed non-uniform quantization scheme, the presented algorithm can achieve a significant performance improvement and a fast decoding speed, even with very small quantization levels (3–4 bits resolution). The presented algorithm provides a candidate for trade-offs between performance and complexity.

## On Fault Tolerance of the Gallager B Decoder Under Data-Dependent Gate Failures

- **Status**: ✅
- **Reason**: Gallager B 디코더의 게이트 고장 내성 분석 및 디코더 수정안 제시 — 이식 가능한 BP 디코더 알고리즘 개선(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7120101
- **Type**: journal
- **Published**: Aug. 2015
- **Authors**: Srdan Brkic, Omran Al Rasheed, Predrag Ivaniš +1
- **PDF**: https://ieeexplore.ieee.org/document/7120101
- **Abstract**: In this letter, we characterize the effect of data-dependent gate failures on the performance of the Gallager B decoder of low-density parity-check codes. We show that this type of failures makes the decoder dependent on a transmitted codeword, thus rendering inapplicable the traditional analysis tools such as density evolution and trapping sets. By using Monte Carlo simulations, we identify two operating regions: one in which hardware unreliability leads to significant performance degradation and another in which the performance loss is negligible. Based on these results, we propose a simple modification of the decoder that ensures its fault tolerance.

## Parallel LDPC decoding on a GPU using OpenCL and global memory for accelerators

- **Status**: ✅
- **Reason**: Parallel LDPC decoder on GPU via OpenCL — transferable decoder HW/parallelization technique (category C/D).
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7255228
- **Type**: conference
- **Published**: 6-7 Aug. 2
- **Authors**: Jung-Hyun Hong, Ki-Seok Chung
- **PDF**: https://ieeexplore.ieee.org/document/7255228
- **Abstract**: This paper introduces a parallel software decoder of Low Density Parity Check (LDPC) codes with an Open Computing Language (OpenCL) framework including Global Memory for ACcelerators (GMAC). The LDPC code is one of the most popular and strongest error correcting codes for mobile communication systems. OpenCL is an open standard programming framework that supports programming languages and application programming interfaces (APIs) for heterogeneous platforms. GMAC is a software implementation of Asymmetric Distributed Shared Memory (ADSM) that maintains a shared logical memory space for the host to access memory objects in the physical memory of an OpenCL device. In this paper, we parallelize the iterative LDPC decoding steps on a graphics processing unit (GPU) using OpenCL. To improve the performance of the proposed decoder, data transfer optimization techniques between the host and the GPU including pre-pinned OpenCL memory objects for GMAC are applied. In terms of the entire decoding time, the speedup of the proposed LDPC decoder over a conventional OpenCL implementation is 1.28.

## Cost-effectively improving life endurance of MLC NAND flash SSDs via hierarchical data redundancy and heterogeneous flash memory

- **Status**: ✅
- **Reason**: MLC NAND flash SSD endurance via hierarchical data redundancy + ECC — NAND/SSD direct (category A).
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:7255200
- **Type**: conference
- **Published**: 6-7 Aug. 2
- **Authors**: Shishi Tan, Ruirong Yu, Shenggang Wan +1
- **PDF**: https://ieeexplore.ieee.org/document/7255200
- **Abstract**: As an alternative to conventional spinning HDDs, MLC NAND flash memory based SSDs suffer from a low life endurance. To cost-effectively address this problem, we propose integrating both Hierarchical data redundancy and Heterogeneous flash memory techniques into those SSDs, named as H2-SSD. By deploying across-chips data redundancy in addition to the conventional in-page ECCs, the error correction capacity of H2-SSD can be dramatically enhanced. As a result, the life endurance can be significantly improved. Furthermore, an extra small sized SLC chip is deployed in H2-SSD to store the across-chips parity. Due to the high Program/Erase performance and life endurance of that SLC chip, the degradation of I/O performance induced by the hierarchical data redundancy will be slight in most cases, even under a strict synchronous parity update strategy. Both quantitatively analysis and trace-driven simulation are conducted to evaluate the effectiveness of H2-SSD. The results demonstrate that H2-SSD outperforms the conventional SSDs in the maximum Program/Erase cycles by 23% to 178% and suffer from a less than 10% degradation of I/O performance under most cases.

## Genie-aided adaptive normalized min-sum algorithm for LDPC decoding

- **Status**: ✅
- **Reason**: 적응 정규화 min-sum(NMS) 변형 디코더, 채널 비의존 LUT 기반 정규화계수 조정 — 이식 가능 디코더 알고리즘(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7289086
- **Type**: conference
- **Published**: 24-28 Aug.
- **Authors**: Yue Liu, Kewu Peng, Changyong Pan +1
- **PDF**: https://ieeexplore.ieee.org/document/7289086
- **Abstract**: This paper proposes an algorithm for the decoding of low-density parity check (LDPC) codes, aiming to retrieve the performance degradation of conventional normalized min-sum algorithm, especially for irregular LDPC code. In our proposed algorithm, normalization factors are adjusted dynamically and adaptively during iterative decoding process according to look-up tables obtained by training and simulation in our proposal. The look-up tables construct the relationship between normalization factor a and the failed parity-check equation proportion p, which could be calculated in each decoding process. Simulation results demonstrate that the proposed algorithm can achieve a performance closer to the sum-product algorithm and a coding gain of around 0.2dB compared to the conventional normalized min-sum algorithm for rate 2/3 irregular LDPC codes over the AWGN channel. Our proposal is independent from the channel characteristics and retains low complexity. The implementation facility and the excellent performance make the proposed algorithm expect a wide application.

## A New Solution Based on Multi-rate LDPC for Flash Memory to Reduce ECC Redundancy

- **Status**: ✅
- **Reason**: NAND 플래시용 Switch/Multi-rate LDPC로 ECC redundancy 절감 — A 카테고리 직접 해당
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7345373
- **Type**: conference
- **Published**: 20-22 Aug.
- **Authors**: Shigui Qi, Dan Feng, Nan Su +2
- **PDF**: https://ieeexplore.ieee.org/document/7345373
- **Abstract**: Low-density parity-check (LDPC) code can provide powerful error correcting performance for NAND flash memory. Different LDPC code rate has different error correcting performance. Moreover, the raw bit error rate of flash memory is very low in the early lifetime. This will generate ECC redundancy that the error correcting performance of LDPC cannot be completely released. We propose a new Switch LDPC (S-LDPC) algorithm based on Multi-Rate LDPC code to reduce ECC redundancy and meet different error correcting requirement in the different periods of flash memory. S-LDPC algorithm can achieve optimal tradeoff among error correcting performance, decoding energy consumption and read performance. The extensive experiments show that S-LDPC algorithm can improve the average read response time of flash memory 25%-54% without reducing the reliability of flash memory. We further demonstrate that LDPC code with code rate 0.96 can save about 40% decoding energy consumption than LDPC code with code rate 0.7.

## Streaming data transmission by using spatially coupled LDPC codes

- **Status**: ✅
- **Reason**: Spatially-coupled LDPC의 recursive encoder + sliding-window 저지연/저복잡 디코더, ensemble 구성 — SC-LDPC 구성/디코더 기법 이식 가능(C/E).
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7332557
- **Type**: conference
- **Published**: 19-20 Aug.
- **Authors**: Sijie Wang, Zhongwei Si, Xuehong Lin
- **PDF**: https://ieeexplore.ieee.org/document/7332557
- **Abstract**: With the tremendous development of mobile Internet and big data, much attention has been attracted on streaming data transmission. In this paper, we propose a quasi real-time transmission scheme using spatially coupled LDPC codes for forward error correction. Recursive encoder and sliding-window decoder with low-latency and low-complexity are employed for data transmission. When any error is reported, additional information is requested and retransmitted. Capacity-approaching performance can be achieved by constructing proper ensembles according to channel conditions. Theoretical thresholds and simulation results are provided, which illustrate the good performance.

## LDPC codes for low-complexity analog decoders

- **Status**: ✅
- **Reason**: 아날로그 디코더용 LDPC 코드 구성법(설계복잡도↓) 신규 제안 — 코드설계(E)/HW 이식 가능성, CCSDS 대비 정량비교
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7497931
- **Type**: conference
- **Published**: 15-17 Aug.
- **Authors**: Hao Zheng, Xuhui Ding, Zhiyuan Wang +2
- **PDF**: https://ieeexplore.ieee.org/document/7497931
- **Abstract**: Compared with their digital counterparts, LDPC analog decoders own higher power efficiency which is suitable for low-power-consumptions applications. However, the high designing complexity of analog decoders with long block length has impeded their real-world applications. This paper presents a method to construct LDPC codes that can lower the designing complexity significantly by using identical models to form the whole decoder, as well as rules that codes should satisfy. Simulation results show that the proposed LDPC codes could lower the designing complexity with little performance lose and have better error-correcting performance than codes in CCSDS standard.

## Improved decoding of LDPC codes by variable-to-check residual belief propagation

- **Status**: ✅
- **Reason**: Lazy-RBP — variable-to-check residual BP 동적스케줄 신규 디코더 알고리즘, 바이너리 LDPC BP에 직접 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7497930
- **Type**: conference
- **Published**: 15-17 Aug.
- **Authors**: Lingyan Song, Shujuan Hou
- **PDF**: https://ieeexplore.ieee.org/document/7497930
- **Abstract**: This paper proposes an improved variable-to-check residual belief propagation algorithm, called Lazy-RBP, in which a new informed dynamic schedule (IDS) combined with the lazy schedule (LS) is adopted. Firstly, Lazy-RBP exploits the probabilistic girth-based approach, one of the LS strategies, to decide the set of updated variable nodes in each iteration. Then among this set, a new IDS scheme is introduced, where both the unreliable variable nodes and the residual of the variable-to-check messages are utilized to locate the message to be propagated first. Simulation results show that the Lazy-RBP algorithm can not only improve the error performance but accelerate the convergence compared with the VC-RBP algorithm.
