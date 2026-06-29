# IEEE Xplore — 2016-04 (1차선별 통과)


## Efficient Search of Girth-Optimal QC-LDPC Codes

- **Status**: ✅
- **Reason**: Binary QC-LDPC girth-optimal search with new pruning techniques, shorter girth-10/12 codes and tightened bounds (E code design)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7398027
- **Type**: journal
- **Published**: April 2016
- **Authors**: Alireza Tasdighi, Amir H. Banihashemi, Mohammad-Reza Sadeghi
- **PDF**: https://ieeexplore.ieee.org/document/7398027
- **Abstract**: In this paper, we study the cycle structure of quasi-cyclic (QC) low-density parity-check (LDPC) codes with the goal of obtaining the shortest code with a given degree distribution and girth. We focus on QC-LDPC codes, whose Tanner graphs are cyclic liftings of fully connected base graphs of size 3 × n, n ≥ 4, and obtain minimal lifting degrees that result in girths 6 and 8. This is performed through an efficient exhaustive search, and as a result, we also find all the possible non-isomorphic codes with the same minimum block length, girth, and degree distribution. The exhaustive search, which is ordinarily a formidable task, is made possible by pruning the search space of many codes that are isomorphic to those previously examined in the search process. Many of the pruning techniques proposed in this paper are also applicable to QC-LDPC codes with base graphs other than the 3 × n fully connected ones discussed here, as well as to codes with a larger girth. To further demonstrate the effectiveness of the pruning techniques, we use them to search for QC-LDPC codes with girths 10 and 12, and find a number of such codes that have a shorter block length compared with the best known similar codes in the literature. In addition, motivated by the exhaustive search results, we tighten the lower bound on the block length of QC-LDPC codes of girth 6 constructed from fully connected 3 × n base graphs, and construct codes that achieve the lower bound for an arbitrary value of n ≥ 4.

## Rate-Compatible Root-Protograph LDPC Codes for Quasi-Static Fading Relay Channels

- **Status**: ✅
- **Reason**: full-diversity rate-compatible root-protograph LDPC 신규 구성법+PEXIT 분석→바이너리 protograph 코드설계 이식 가능(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7080854
- **Type**: journal
- **Published**: April 2016
- **Authors**: Yi Fang, Yong Liang Guan, Guoan Bi +2
- **PDF**: https://ieeexplore.ieee.org/document/7080854
- **Abstract**: We investigate the protograph low-density parity-check (LDPC) codes over quasi-static fading (QSF) relay channels with coded cooperation (CC) in this paper. A new construction method is proposed for designing the full-diversity rate-compatible root-protograph (RCRP) codes for such a relaying protocol. The asymptotic word error rate (WER) and bit error rate (BER) of the RCRP codes are analyzed by exploiting a new protograph extrinsic information transfer (PEXIT) algorithm. Furthermore, the expression of outage probability is also developed to characterize the error performance of RCRP codes. Both theoretical and simulated results suggest that the RCRP codes not only outperform the conventional regular rate-compatible protograph (RCP) codes in terms of error performance with code rates ranging from 0 to 1/2 but approach the outage limit as well.

## Informed Decoding Algorithms of LDPC Codes Based on Dynamic Selection Strategy

- **Status**: ✅
- **Reason**: New dynamic-selection message scheduling for binary LDPC BP (V-VCRBP/V-CVRBP) improving BER and convergence (C decoder)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7403966
- **Type**: journal
- **Published**: April 2016
- **Authors**: Xingcheng Liu, Zhenzhu Zhou, Ru Cui +1
- **PDF**: https://ieeexplore.ieee.org/document/7403966
- **Abstract**: Among most of the message scheduling strategies for low-density parity-check (LDPC) codes, the dynamic scheduling strategy behaves best in error correction performance. Dynamic selection is an integral part of dynamic scheduling decoding, which plays a decisive role throughout the decoding process. Usually, the dynamic selection strategy based on the message residuals only is employed in dynamic decoding algorithms, while other potentials of the dynamic selection strategy are rarely cared about. In this paper, we propose the triple judgment dynamic selection strategy combined with a Stability Criterion. Interestingly, the new strategy can be well applied to two different dynamic algorithms, namely, the V-VCRBP and the V-CVRBP algorithms. The proposed strategy has a great advantage: locating the message to be preferentially updated is extremely quick and accurate. Simulation results demonstrate that the V-VCRBP algorithm outperforms existing decoding algorithms in terms of BER performance and convergence speed, while the V-CVRBP algorithm has good error correction performance with a lower computational complexity.

## A Generator-Matrix-Based Approach for Adaptively Generating Cut-Inducing Redundant Parity Checks

- **Status**: ✅
- **Reason**: GM-based adaptive cut-inducing RPC generation improving adaptive LP decoding of binary linear codes; transferable decoder technique (C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7407566
- **Type**: journal
- **Published**: April 2016
- **Authors**: Hossein Falsafain, Sayyed Rasoul Mousavi
- **PDF**: https://ieeexplore.ieee.org/document/7407566
- **Abstract**: A generator matrix (GM)-based approach for adaptively deriving cut-inducing redundant parity checks (RPCs) during the adaptive linear programming decoding algorithm is presented. More precisely speaking, if the decoder gets stuck in a non-integral pseudocodeword, then the resulting RPCs are likely to provide violated forbidden-set inequalities that can separate this non-integral optimal solution from the feasible region. The described approach can be viewed as a GM-based counterpart of the approach proposed by Zhang and Siegel in 2012. For binary linear codes of low rate, while providing the same error-correcting performance, our approach requires much less computational time compared to its analogue.

## A 520k (18900, 17010) Array Dispersion LDPC Decoder Architectures for NAND Flash Memory

- **Status**: ✅
- **Reason**: NAND 플래시용 array dispersion LDPC 코드 구성+masking+normalized min-sum VNC 시퀀셜 스케줄링 디코더 VLSI 구현(A/D/E 직접)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7208881
- **Type**: journal
- **Published**: April 2016
- **Authors**: Kin-Chu Ho, Chih-Lung Chen, Hsie-Chia Chang
- **PDF**: https://ieeexplore.ieee.org/document/7208881
- **Abstract**: Although Latin square is a well-known algorithm to construct low-density parity-check (LDPC) codes for satisfying long code length, high code-rate, good correcting capability, and low error floor, it has a drawback of large submatrix that the hardware implementation will be suffered from large barrel shifter and worse routing congestion in fitting NAND flash applications. In this paper, a top-down design methodology, which not only goes through code construction and optimization, but also hardware implementation to meet all the critical requirements, is presented. A two-step array dispersion algorithm is proposed to construct long LDPC codes with a small submatrix size. Then, the constructed LDPC code is optimized by masking matrix to obtain better bit-error rate (BER) performance and lower error-floor. In addition, our LDPC codes have a diagonal-like structure in the parity-check matrix leading to a proposed hybrid storage architecture, which has the advantages of better area efficiency and large enough data bandwidth for high decoding throughput. To be adopted for NAND flash applications, an (18900, 17010) LDPC code with a code-rate of 0.9 and submatrix size of 63 is constructed and the field-programmable gate array simulations show that the error floor is successfully suppressed down to BER of 10-12. An LDPC decoder using normalized min-sum variable-node-centric sequential scheduling decoding algorithm is implemented in UMC 90-nm CMOS process. The postlayout result shows that the proposed LDPC decoder can achieve a throughput of 1.58 Gb/s at six iterations with a gate count of 520k under a clock frequency of 166.6 MHz. It meets the throughput requirement of both NAND flash memories with Toggle double data rate 1.0 and open NAND flash interface 2.3 NAND interfaces.

## Read and Write Voltage Signal Optimization for Multi-Level-Cell (MLC) NAND Flash Memory

- **Status**: ✅
- **Reason**: MLC NAND 플래시 read/write 전압 최적화+soft LDPC용 양자화 레벨 설계(A) 직접 해당
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7416649
- **Type**: journal
- **Published**: April 2016
- **Authors**: Chaudhry Adnan Aslam, Yong Liang Guan, Kui Cai
- **PDF**: https://ieeexplore.ieee.org/document/7416649
- **Abstract**: The multi-level-cell (MLC) NAND flash channel exhibits nonstationary behavior over increasing program and erase (PE) cycles and data retention time. In this paper, an optimization scheme for adjusting the read (quantized) and write (verify) voltage levels to adapt to the nonstationary flash channel is presented. Using a model-based approach to represent the flash channel, incorporating the programming noise, random telegraph noise (RTN), data retention noise and cell-to-cell interference as major signal degradation components, the write-voltage levels are optimized by minimizing the channel error probability. Moreover, for selecting the quantization levels for the read-voltage to facilitate soft LDPC decoding, an entropy-based function is introduced by which the voltage erasure regions (error dominating regions) are controlled to produce the lowest bit/frame error probability. The proposed write and read voltage optimization schemes not only minimize the error probability throughout the operational lifetime of flash memory, but also improve the decoding convergence speed. Finally, to minimize the number of read-voltage quantization levels while ensuring LDPC decoder convergence, the extrinsic information transfer (EXIT) analysis is performed over the MLC flash channel.

## Fast Converging ADMM-Penalized Algorithm for LDPC Decoding

- **Status**: ✅
- **Reason**: ADMM-penalized LDPC 디코딩의 새 스케줄링 기법-바이너리 LDPC 디코더 알고리즘(C) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7409989
- **Type**: journal
- **Published**: April 2016
- **Authors**: Imen Debbabi, Bertrand Le Gal, Nadia Khouja +2
- **PDF**: https://ieeexplore.ieee.org/document/7409989
- **Abstract**: The alternate direction method of multipliers (ADMM) approach has been recently considered for LDPC decoding. It has been approved to enhance the error rate performance compared with conventional message passing (MP) techniques in both the waterfall and error floor regions at the cost of a higher computation complexity. In this letter, a formulation of the ADMM decoding algorithm with modified computation scheduling is proposed. It increases the error correction performance of the decoding algorithm and reduces the average computation complexity of the decoding process thanks to a faster convergence. Simulation results show that this modified scheduling speeds up the decoding procedure with regards to the ADMM initial formulation while enhancing the error correction performance. This decoding speed-up is further improved when the proposed scheduling is teamed with a recent complexity reduction method detailed in Wei et al. IEEE Commun. Lett., 2015.

## Improved LDPC decoding algorithms based on min-sum algorithm

- **Status**: ✅
- **Reason**: min-sum 기반 개선 LDPC 디코딩 알고리즘 2종 제안(카테고리 C, 이식 가능 디코더)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7480124
- **Type**: conference
- **Published**: 5-6 April 
- **Authors**: Y.V.A.C. Kumara, C.B. Wavegedara
- **PDF**: https://ieeexplore.ieee.org/document/7480124
- **Abstract**: Low-Density Parity check (LDPC) codes offer high-performance error correction near the Shannon limit which employs large code lengths and some iterations in the decoding process. The conventional decoding algorithm of LDPC is the Log Likelihood Ratio based Belief Propagation (LLR BP) which is also known as the `Sum-Product algorithm' which gives the best decoding performance and requires the most computational complexity and implementations with increased hardware complexity. Another simpler variant of this algorithm is used which is known as `min-sum algorithm' which reduces computational complexity as well as hardware complexity but with reduced accuracy. This paper analyzes the reason min-sum algorithm is more prone to errors when compared to the sum-product algorithm, and puts forward two improved algorithms which improve the performance of the min-sum algorithm with comparable algorithmic complexity.

## Evaluation of the hardware complexity of the ADMM approach for LDPC decoding

- **Status**: ✅
- **Reason**: ADMM LP LDPC 디코더의 HW 복잡도 분석+부분병렬 아키텍처 제안, 이식 가능 HW(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:7565042
- **Type**: conference
- **Published**: 3-6 April 
- **Authors**: Imen Debbabi, Nadia Khouja, Fethi Tlili +2
- **PDF**: https://ieeexplore.ieee.org/document/7565042
- **Abstract**: Linear Programming (LP) is a novel technique for LDPC decoding. With the advance of the Alternate Direction Method of Multipliers (ADMM) approach, a significant step towards LP LDPC decoding scalability and optimization is made possible. Yet, this innovative decoding technique has not been implemented in hardware. Its hardware complexity has neither been estimated nor compared with traditional techniques. In this paper, an overview of the ADMM approach and its error correction performances for LDPC decoding is provided. Then, its computation complexity is evaluated to show the hardware feasibility of ADMM-based LDPC decoders. Our analysis is mainly carried at two levels. First, a quantitative complexity analysis is reported and a comparison with traditional LDPC decoders is given. Second, a proposal of a partially parallel architecture is described and its hardware complexity is evaluated then compared with state-of-the-art LDPC decoders.

## FPGA architecture of multi-codeword LDPC decoder with efficient BRAM utilization

- **Status**: ✅
- **Reason**: QC-LDPC FPGA 디코더 HW 아키텍처(멀티-코드워드 BRAM 패킹, 3/4비트 양자화)로 NAND ECC에 명시 언급+이식 가능(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:7482452
- **Type**: conference
- **Published**: 20-22 Apri
- **Authors**: Sergiu Nimara, Oana Boncalo, Alexandru Amaricai +1
- **PDF**: https://ieeexplore.ieee.org/document/7482452
- **Abstract**: Implementation of Quasi-Cyclic (QC) Low Density Parity-Check (LDPC) decoder on FPGA devices has shown great interest in both wireless communication, as well as error correction for Flash memories. This paper presents an FPGA flooded LDPC decoder which uses multiple codeword processing for efficient memory utilization. It is based on a partially parallel implementation, which relies on memory blocks for message passing between the processing units. We obtain efficient memory utilization by packing multiple messages corresponding to multiple codewords into the same Block RAM word. The increase in throughput is linear with the number of processed codewords. The proposed LDPC decoder can process up to 9 codewords in parallel, for 4-bit message quantization, or up to 12 codewords, for 3-bit message quantization, without introducing significant memory overhead.

## System-level error correction by read-disturb error model of 1Xnm TLC NAND Flash memory for read-intensive enterprise solid-state drives (SSDs)

- **Status**: ✅
- **Reason**: TLC NAND read-disturb 에러모델 기반 RDM-LDPC ECC, NAND 직접(A)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7574622
- **Type**: conference
- **Published**: 17-21 Apri
- **Authors**: Yoshiaki Deguchi, Tsukasa Tokutomi, Ken Takeuchi
- **PDF**: https://ieeexplore.ieee.org/document/7574622
- **Abstract**: Read-disturb Modeled LDPC (RDM-LDPC) ECC is proposed. Conventional Advanced Error-Prediction LDPC (AEP-LDPC) [1] corrects data-retention errors of data-storage-purpose SSDs storing photos, movies, etc. but cannot correct read-disturb errors. For read-intensive computing-purpose enterprise SSDs, this paper analyzes the read-disturb errors, develops the error model of 1Xnm TLC NAND Flash memory and proposes ECC suitable for read-disturb errors. It is experimentally demonstrated that proposed RDM-LDPC extends the read cycle of SSDs by 5000-times.

## Improving Read Performance of NAND Flash SSDs by Exploiting Error Locality

- **Status**: ✅
- **Reason**: NAND 플래시 SSD의 LDPC ECC 디코딩 오버헤드를 error locality 캐싱으로 줄이는 컨트롤러 기법(카테고리 A 직접)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6879446
- **Type**: journal
- **Published**: 1 April 20
- **Authors**: Ren-Shuo Liu, Meng-Yen Chuang, Chia-Lin Yang +3
- **PDF**: https://ieeexplore.ieee.org/document/6879446
- **Abstract**: NAND flash-based solid-state drives (SSDs), which can serve as the caches of hard disk drives, have gained popularity in large-scale, high-performance storage. A type of advanced error correction code for SSDs, low-density parity-check (LDPC), is required to mitigate a considerable number of errors in the raw data of NAND flash. However, LDPC imposes read performanceoverhead due to the complex decoding procedure of LDPC. In this paper, we propose an error-correcting cache (EC-Cache) that exploits “error locality”, a characteristic of NAND flash memory, to improve the read performance of SSDs. We use the term “error locality” to refer to the property that the majority of errors in reads to the same flash page appear at the same positions until thepage is erased. By caching detected errors, we can correct a significant portion of errors in the requested flash page prior to the LDPC decoding process. This design significantly reduces LDPC decoding overhead because the latency of LDPC is correlated with thenumber of errors in the input data. We conduct experiments, including flash characterization, LDPC simulation, and SSD simulation,to evaluate EC-Cache. The experimental results demonstrate that EC-Cache can improve the read performance of LDPC-based SSDs by up to $2.6\times$ .
