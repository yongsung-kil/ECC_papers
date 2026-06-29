# IEEE Xplore — 2014-06 (1차선별 통과)


## Raptor-Like Rate Compatible LDPC Codes and Their Puncturing Performance for the Cloud Transmission System

- **Status**: ✅
- **Reason**: raptor-like rate-compatible 바이너리 LDPC 구성+puncturing 성능 — 신규 QC/rate-compatible 코드설계로 이식 여지(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6744572
- **Type**: journal
- **Published**: June 2014
- **Authors**: Sung Ik Park, Yiyan Wu, Heung Mook Kim +2
- **PDF**: https://ieeexplore.ieee.org/document/6744572
- **Abstract**: This paper proposes a class of raptor-like rate compatible low-density parity check (LDPC) codes for the cloud transmission (CTxN) system. The proposed LDPC codes have lengths of 16,200 and 64,800 which are the same as those of DVB T2/S2 LDPC codes so that the CTxn system can easily be combined with the DVB-T2/S2 system for a second layer service. As the proposed LDPC codes are optimized at low coding rate range (R <;1/2), their performance is not only close to the Shannon limit, but also better than the DVB-T2/S2 LDPC codes. Moreover, the proposed LDPC codes have raptor code's property so that they can be decoded with a punctured codeword at the receiver for power saving and less latency under high signal-to-noise ratio regions.

## Optimized geometric LDPC codes with quasi-cyclic structure

- **Status**: ✅
- **Reason**: 유클리드기하 기반 QC-LDPC 신규 구성 + EXIT 차수분포 최적화(large girth, 가변 열/행 가중치); 바이너리 LDPC 코드설계(E) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6856622
- **Type**: journal
- **Published**: June 2014
- **Authors**: Xueqin Jiang, Moon Ho Lee, Shangce Gao +1
- **PDF**: https://ieeexplore.ieee.org/document/6856622
- **Abstract**: This paper presents methods to the construction of regular and irregular low-density parity-check (LDPC) codes based on Euclidean geometries over the Galois field. Codes constructed by these methods have quasi-cyclic (QC) structure and large girth. By decomposing hyperplanes in Euclidean geometry, the proposed irregular LDPC codes have flexible column/row weights. Therefore, the degree distributions of proposed irregular LDPC codes can be optimized by technologies like the curve fitting in the extrinsic information transfer (EXIT) charts. Simulation results show that the proposed codes perform very well with an iterative decoding over the AWGN channel.

## LDPC Codes for 2D Arrays

- **Status**: ✅
- **Reason**: 2D 어레이 바이너리 LDPC 스토리지 코드, 저복잡도 반복 디코딩 신규 구성 — B/E
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6778036
- **Type**: journal
- **Published**: June 2014
- **Authors**: Yuval Cassuto, Amin Shokrollahi
- **PDF**: https://ieeexplore.ieee.org/document/6778036
- **Abstract**: Binary codes over 2D arrays are very useful in data storage, where each array column represents a storage device or unit that may suffer failure. In this paper, we propose a new framework for probabilistic construction of codes on 2D arrays. Instead of a pure combinatorial erasure model used in traditional array codes, we propose a mixed combinatorial-probabilistic model of limiting the number of column failures, and assuming a binary erasure channel in each failing column. For this model, we give code constructions and detailed analysis that allow sustaining a large number of column failures with graceful degradation in the fraction of erasures correctable in failing columns. Another advantage of the new framework is that it uses low-complexity iterative decoding. The key component in the analysis of the new codes is to analyze the decoding graphs induced by the failed columns, and infer the decoding performance as a function of the code design parameters, as well as the array size and failure parameters. A particularly interesting class of codes, called probabilistically maximum distance separable (MDS) array codes, gives fault-tolerance that is equivalent to traditional MDS array codes. The results also include a proof that the 2D codes outperform standard 1D low-density parity-check codes.

## A High Throughput Efficient Approach for Decoding LDPC Codes onto GPU Devices

- **Status**: ✅
- **Reason**: LDPC layered schedule GPU 디코더 구현, throughput 개선 — 이식 가능 HW/디코더 기법(D/C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6762823
- **Type**: journal
- **Published**: June 2014
- **Authors**: Bertrand Le Gal, Christophe Jego, Jérémie Crenne
- **PDF**: https://ieeexplore.ieee.org/document/6762823
- **Abstract**: Low density parity check (LDPC) decoding process is known as compute intensive. This kind of digital communication applications was recently implemented onto graphic processing unit (GPU) devices for LDPC code performance estimation and/or for real-time measurements. Overall previous studies about LDPC decoding on GPU were based on the implementation of the flooding-based decoding algorithm that provides massive computation parallelism. More efficient layered schedules were proposed in literature because decoder iteration can be split into sublayer iterations. These schedules seem to badly fit onto GPU devices due to restricted computation parallelism and complex memory access patterns. However, the layered schedules enable the decoding convergence to speed up by two. In this letter, we show that: 1) layered schedule can be efficiently implemented onto a GPU device; and 2) this approach—implemented onto a low-cost GPU device—provides higher throughputs with identical correction performances (BER) compared to previously published results.

## A Serial Layered Scheduling Algorithm for Factor Graph Equalization

- **Status**: ✅
- **Reason**: factor graph BP serial layered scheduling 신규 알고리즘, 수렴 2배·SNR 개선 — 바이너리 LDPC BP에 이식 가능(C). 애매하나 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6799179
- **Type**: journal
- **Published**: June 2014
- **Authors**: Jianjun Zhang, Yiming Lei, Mingke Dong +1
- **PDF**: https://ieeexplore.ieee.org/document/6799179
- **Abstract**: This letter proposes a novel factor graph equalization based on a serial layered scheduling (SLS) algorithm of belief propagation, where the channel convolutional matrix is decomposed according to the distribution of its non-zero elements. In the SLS algorithm based factor graph equalization, factor nodes are classified into multiple layers referring to the decomposition of channel convolutional matrix, and the a posteriori probabilities message is updated based on a serial layer-by-layer mechanism. This proposed SLS algorithm clearly decreases the signal-to-noise ratio (SNR) threshold and also increases the convergence speed of equalization process, which results in a higher reliability and a lower latency of equalization process. Compared with current parallel flooding scheduling (PFS) algorithm, the convergence speed of SLS algorithm increases almost by twice, and its SNR threshold reduces by 7 dB over the Proakis-C channel.

## A high throughput and low BER implementation method in TG wireless transmission system

- **Status**: ✅
- **Reason**: regular/irregular LDPC 디코더의 병렬 메시지 업데이트 및 VLSI 구현 복잡도 감소 기법(D) — 도메인은 열차통신이나 HW 아키텍처 이식 가능.
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:6931155
- **Type**: conference
- **Published**: 9-11 June 
- **Authors**: Guochun Wan, Guizhu Yin, Lan Chen +2
- **PDF**: https://ieeexplore.ieee.org/document/6931155
- **Abstract**: Along with the development of high-speed railway, higher and higher technical requirements for the mobile communication system in it are raised. Communication Based Train Control (CBTC) will be based on mobile communication, of which the key problem is how to support high reliability of data transmission in order to improve utilization of tracks and enhance train's safety. The applications of LDPC in reliable high-speed data transmission which serves fault monitor and early-warning system in train-ground (TG) wireless communication are proposed. The design of high-throughput and complexity reduction for regular and irregular LDPC codes has been considered in decoding algorithm and architectural in order to accord with the performance of reliable train-ground information transmission. A parallel message updates and implement method are presented for LDPC decoder of train-ground system that bring negligible loss in performance compared to the ideal case. A new implement method which is designed of very large scale integration have been proposed in this paper. The LDPC decoder has been applied in reliable train-ground high throughput fault monitor and digital early-warning communication system. Testing result demonstrates that the proposed architecture achieves a throughput of 18.629Mbps, which meets the performance requirements of reliable high data transmission and higher throughout.

## On the generalized LDPC codes from multiple component codes suitable for high-speed optical transport

- **Status**: ✅
- **Reason**: GLDPC 코드 구성(다중 로컬코드)과 FPGA/ASIC 병렬화 디코더 제시 — 이식 가능 코드설계·HW(E/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6990026
- **Type**: conference
- **Published**: 8-13 June 
- **Authors**: Ivan B. Djordjevic, Ting Wang
- **PDF**: https://ieeexplore.ieee.org/document/6990026
- **Abstract**: A class of GLDPC-codes is proposed consisting of multiple local-codes suitable for code-rate-adaptation in high-speed optical-transport-networks, providing excellent coding-gains. GLDPC-decoder for this class of codes is more suitable for parallelization in FPGA/ASIC-hardware compared to LDPC-decoder.

## Optimized encoder architecture for structured low density parity check codes of short length

- **Status**: ✅
- **Reason**: 구조적 QC-LDPC 인코더 FPGA 아키텍처(barrel shifter 제거, 처리량/면적) — 이식 가능 HW(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:6869526
- **Type**: conference
- **Published**: 3-5 June 2
- **Authors**: Silvia Anggraeni, Fawnizu Azmadi Hussin, Varun Jeoti
- **PDF**: https://ieeexplore.ieee.org/document/6869526
- **Abstract**: This paper proposes an architecture for structured low density parity check encoder. The proposed architecture supports the limitation of input/output pins of field programmable gate array using division of information bits. The division of information bits generates latency of encoding. The proposed architecture does not store the required matrix for bit-wise multiplication and does not use cyclic shift of barrel shifter. The proposed architecture is investigated using code length below 1000 bits and implementation of high code rate R = 5/6 and code length between 1000 and 2000 bits. Even though this architecture is optimized for short code length, it is shown that the proposed architecture achieves information throughput of 30.178 Gbps and area of 2737 logic element when code length N = 1944 and code rate R = 5/6.

## A general folded encoding structure for quasi-cyclic LDPC codes

- **Status**: ✅
- **Reason**: 이식 가능 HW(D): QC-LDPC용 folded 인코딩 구조, 자원 66% 절감·가변 병렬성 — HW 인코더 아키텍처 신규 기여
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:6933736
- **Type**: conference
- **Published**: 27-29 June
- **Authors**: Chen Qi, Guo Xuan, Yang Zhanxin
- **PDF**: https://ieeexplore.ieee.org/document/6933736
- **Abstract**: A general folded encoding structure for multi-rate quasi-cyclic LDPC codes is proposed in this paper to implement LDPC encoder with the advantages of few resources consumption, adjustable parallelism and high coding rate. For the quasi-cyclic LDPC codes mentioned in this paper, folded encoding structure can provide high coding rate and save 66% of the resources compared with the traditional encoding structure.

## Construction of multi-rate high performance QC-LDPC codes with low implementation complexity

- **Status**: ✅
- **Reason**: RCSEV-CD 신규 다중률 QC-LDPC 구성 기법(E) — 바이너리 코드설계 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6873508
- **Type**: conference
- **Published**: 25-27 June
- **Authors**: Yue Liu, Kewu Peng
- **PDF**: https://ieeexplore.ieee.org/document/6873508
- **Abstract**: Multi-rate LDPC codes with near Shannon limit performance are highly demanded in digital television terrestrial broadcasting (DTTB) system. Several proposals have been carried out to construct multi-rate LDPC codes, among which, Row-combining and Row-splitting with Edge Variation (RCSEV) helps construct LDPC codes with constant code length and simple hardware architecture. Besides, Column Extension (CE) is also an effective method for rate-compatible LDPC code design. This paper proposes an improved scheme of Row-Combining and splitting with Edge Variation and Column Deletion (RCSEV-CD), which is the rational combination of RCSEV and CE. RCSEV is carried out to generate multi-rate LDPC codes sharing the same code length in basic code group. The codes in extended code group are generated via CD, ensuring same code length in each extended code groups. Multi-rate codes within a code group improves the flexibility of a service while the code groups meet the requirement of multiple services. EXIT chart analysis helps guide the trade-off between column degree distributions among multiple rates. A comparison with multi-rate codes in DVB-S2 is performed via bit error rate (BER) simulation and the result shows the superior performance of our designed codes at typical code rates.

## Technologies for the next generation of digital terrestrial television broadcasting — A study on spatially coupled LDPC codes

- **Status**: ✅
- **Reason**: SC-LDPC 부호로 BER 개선 제안, 바이너리 SC-LDPC 코드 설계 기여 — 이식 가능 코드설계(E), 애매하나 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6873475
- **Type**: conference
- **Published**: 25-27 June
- **Authors**: Shingo Asakura, Takuya Shitomi, Susumu Saito +2
- **PDF**: https://ieeexplore.ieee.org/document/6873475
- **Abstract**: NHK is conducting research on the next generation of digital terrestrial broadcasting to enable large-volume content services such as 8K Super Hi-Vision. In our previous study, we used a low-density parity-check (LDPC) block code scheme and proposed a decoding method that uses the channel response of a dual polarized MIMO transmission to further improve the bit error ratio (BER) performance [3]. LDPC block codes are robust forward error correction (FEC) codes and are Shannon-limit-approaching over an additive white Gaussian noise (AWGN) channel. Despite this feature, there is still room for improving the BER performance. In this paper, we propose spatially coupled (SC-) LDPC codes to further improve the BER performance. We also report on our verification using a computer simulation.

## Variable Min-Sum decoding based on generalized mutual information metric

- **Status**: ✅
- **Reason**: GMI 기반 가변 스케일링 Min-Sum 변형 디코더 — NAND BP에 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6873481
- **Type**: conference
- **Published**: 25-27 June
- **Authors**: Yin Xu, Dazhi He, Yunfeng Guan +2
- **PDF**: https://ieeexplore.ieee.org/document/6873481
- **Abstract**: Min Sum algorithm simplifies the non-linear check node operation of Belief Propagation algorithm via linear approximation, which greatly reduces the complexity of realization of decoder but degrades the performance as well. The resulting sub-optimality could be tempered via scaling of LLRs, e.g. fixed optimal scaling applied to Min Sum output resulting in the Normalized Min Sum algorithm, and variable scaling schemes gradually appear in literature. In this paper, we study the variable scaling decoding algorithm, and propose to generate variable scaling sequences via generalized mutual information (GMI) metric. Simulation results on real LDPC codes for different decoding algorithms have shown that our GMI metric performs better than the variable scaling scheme appearing in literature, and meanwhile improves substantially in terms of BER over the conventional Normalized Min Sum algorithm.

## LDPC-RS two dimensional code for the next generation cloud transmission system

- **Status**: ✅
- **Reason**: raptor-like rate-compatible LDPC+RS 2D 부호로 error-floor 제거 — 애매하나 error-floor 관련 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6873509
- **Type**: conference
- **Published**: 25-27 June
- **Authors**: Sung Ik Park, Yiyan Wu, Heung Mook Kim +5
- **PDF**: https://ieeexplore.ieee.org/document/6873509
- **Abstract**: This paper proposes a two dimensional (2D) code, which has vertical raptor-like rate-compatible LDPC code and horizontal Reed Solomon (RS) code, for the terrestrial CTxn system. The proposed 2D code not only removes error-floor phenomenon with a help of RS code, but also does not require a complex interleaver for stable reception under fading channels because the 2D code itself provides block-type interleaver.

## An efficient check node operation circuit for Min-Sum based LDPC decoder

- **Status**: ✅
- **Reason**: D. Min-Sum LDPC 디코더용 저전력/면적효율 check node 회로—비교기 개선 HW 아키텍처, 이식 가능
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:6884452
- **Type**: conference
- **Published**: 22-25 June
- **Authors**: Keol Cho, Ki-Seok Chung
- **PDF**: https://ieeexplore.ieee.org/document/6884452
- **Abstract**: This paper presents a low power and area-efficient check node operation circuit for LDPC decoders based on Min-Sum algorithm. By improving a heavily used comparator circuit, our proposed check node unit reduces area and power consumption by 8% and 13%, respectively, without decoding speed degradation compared to conventional LDPC decoders.

## Efficient check-node-stopped LDPC decoder design

- **Status**: ✅
- **Reason**: C/D. Check Node Stopping 기준으로 수렴 체크노드 연산 감소—디코더 알고리즘+HW(90nm CMOS) 신규 기법, NAND LDPC 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6884305
- **Type**: conference
- **Published**: 22-25 June
- **Authors**: Tzu-Hsuan Huang, Cheng-Hung Lin, Shu-Yen Lin
- **PDF**: https://ieeexplore.ieee.org/document/6884305
- **Abstract**: In this paper, we propose a reduced check node operation design for the LDPC decoder. The proposed Check Node Stopping criterion (CNS) reduces the operations of convergent check nodes when the reliability of check node messages that depends on the magnitude of check node messages is larger than a threshold. Thus, the proposed LDPC decoder can can efficiently terminate the redundant check node calculations in the following iterations. From the simulations under the rate-1/2 WiMAX LDPC decoding, the operation of check nodes can be reduced by about 12% at Eb/N0 of 3.6 dB with a small coding coding gain degradation. A 2.85mm2 LDPC decoder with CNS is implemented in a 90nm CMOS process. The area overhead of the the CNS is about 0.7% of the total area. The proposed LDPC decoder can decrease 4% power consumption for the stopped check node.

## An encoder/decoder with throughput over Gigabits/sec for rate-compatible LDPC codes with wide code rates

- **Status**: ✅
- **Reason**: D/E. Rate-compatible QC-LDPC 구성(shifted identity, dual-diagonal) + FPGA 병렬 인코더/디코더—코드설계+HW 신규 기법, 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6934013
- **Type**: conference
- **Published**: 22-25 June
- **Authors**: Zhiyong He, Paul Fortier, Sébastien Roy +1
- **PDF**: https://ieeexplore.ieee.org/document/6934013
- **Abstract**: A challenge in the design of rate-compatible (RC) low-density parity-check (LDPC) codes is how to maximize the range of code rates. In this paper, we propose a class of RC LDPC codes with a very wide range of code rates. To ensure linear encoding, dual-diagonal form for the parity part of the mother parity-check matrix is used. Constructed from shifted identity matrices, the proposed codes are particularly well-suited for the high-speed implementation of parallel encoders and parallel decoders. To widen the range of code rates, we have proposed an optimal transmission scheme, which keeps the optimal degree distribution unchanged for the mother code and all daughter codes. Thus, the proposed technique pushes the upper bound of code rates to 0.96, which is the highest rate in RC LDPC codes in the world, based on our best knowledge. The implementation results into field programmable gate array (FPGA) devices indicate that a parallel encoder (decoder) for the proposed RC LDPC codes is capable of reaching a throughput of 7.2 (1.8) Gigabits per second using a clock frequency of 150 MHz.

## Improving min-sum LDPC decoding throughput by exploiting intra-cell bit error characteristic in MLC NAND flash memory

- **Status**: ✅
- **Reason**: A/C: MLC NAND 셀내 비트오류 특성 기반 min-sum 디코더 변형 및 데이터 배치 인터리빙, NAND LDPC 직접
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6855550
- **Type**: conference
- **Published**: 2-6 June 2
- **Authors**: Wenzhe Zhao, Hongbin Sun, Minjie Lv +3
- **PDF**: https://ieeexplore.ieee.org/document/6855550
- **Abstract**: Multi-level per cell (MLC) technique significantly improves storage density, but also poses new challenge to data integrity in NAND flash memory. Therefore, low-density parity-check (LDPC) code and soft-decision memory sensing have become indispensable in future NAND flash-based solid state drive design. However, these more powerful technologies inevitably increase the memory read latency and hence degrade the decoding throughput. Motivated by intra-cell unbalanced bit error probability and data dependency in MLC NAND flash memory, this paper proposes two techniques, i.e. intra-cell data placement interleaving and intra-cell data dependency aware min-sum decoding, to effectively improve the throughput of LDPC decoding. Experimental results show that, the proposed techniques used in an integrated way can improve the LDPC decoding throughput by up to 85% when the MLC NAND flash chip is heavily cycled, compared with conventional design practice.

## Energy-efficient gear-shift LDPC decoders

- **Status**: ✅
- **Reason**: gear-shift LDPC 디코더(다단 알고리즘 전환) + ASIC, NAND LDPC HW/디코더로 이식 가능(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6868665
- **Type**: conference
- **Published**: 18-20 June
- **Authors**: Kevin Cushon, Saied Hemati, Shie Mannor +1
- **PDF**: https://ieeexplore.ieee.org/document/6868665
- **Abstract**: In this paper, we present LDPC decoder designs based on gear-shift algorithms, which can use multiple decoding algorithms or update rules over the course of decoding a single frame. By first attempting to decode using low-complexity algorithms, followed by high-complexity algorithms, we increase energy efficiency without sacrificing error correction performance. We present the GSP and IGSP algorithms, and ASIC designs of these algorithms for the 10 Gbps Ethernet (2048,1723) LDPC code. In 65nm CMOS, our pipelined GSP decoder achieves a core area of 5.29mm2, throughput of 88.1 Gbps, and energy efficiency of 39.3 pJ/bit, while our IGSP decoder achieves a core area of 6.00mm2, throughput of 100.3 Gbps, and energy efficiency of 14.6 pJ/bit. Both algorithms achieve error correction performance equivalent to the offset min-sum algorithm. The throughput per unit area and energy efficiency of these decoders improve upon state-of-the-art decoders with comparable error correction performance.

## Combining flexibility with low power: Dataflow and wide-pipeline LDPC decoding engines in the Gbit/s era

- **Status**: ✅
- **Reason**: FPGA dataflow/wide-pipeline LDPC 디코더 아키텍처, NAND LDPC HW로 이식 가능(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:6868671
- **Type**: conference
- **Published**: 18-20 June
- **Authors**: Joao Andrade, Frederico Pratas, Gabriel Falcao +2
- **PDF**: https://ieeexplore.ieee.org/document/6868671
- **Abstract**: Power and flexibility are important constraints in the design of new chips. The efficiency extracted from a design is increasingly becoming a dominant question, and several techniques and technological advances can be used to optimize efficiency in its energy and functionality domains. These two characteristics are critical in digital communication systems that must work accordingly with multiple communication standards at different power, throughput and latency requirements. In this work, we focus on the physical layer Forward Error Correcting (FEC) system, due to the tight throughput and latency constraints they are required to meet, and develop specialized processing engines for Low-Density Parity-Check (LDPC) codes decoding, a class of widely standardized codes. The engines were developed for execution on Field-Programmable Gate Array (FPGA) devices by exploring dataflow and wide-pipeline design approaches, and have the design flexibility to target different LDPC codes, since they were implemented using recent High-Level Synthesis (HLS) tools. The generated engines and architectures allow achieving highly efficient decoders with decoding throughputs ranging from 16 Mbit/s to 1.2 Gbit/s at energy efficiencies of 42 to 908 Mbit/Joule/iteration, while the achieved clock frequencies of operation vary from 80 to 300 MHz. Furthermore, our bandwidth analysis shows that workload boundaries do not impose limitations on a system bus.

## Min-sum algorithm-structure based decoding algorithms for LDPC codes

- **Status**: ✅
- **Reason**: min-sum 변형 및 신규 a-min*-min 디코딩 알고리즘 제안, 바이너리 LDPC BP에 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6862710
- **Type**: conference
- **Published**: 15-19 June
- **Authors**: V. V. Vityazev, E. A. Likhobabin, E. A. Ustinova
- **PDF**: https://ieeexplore.ieee.org/document/6862710
- **Abstract**: Review of various reduced-complexity min-sum based decoding algorithms for LDPC codes are presented. New BP-based approach for LDPC decoding was proposed, and one new a-min∗-min decoding algorithm was presented. Complexity, effectiveness, and average number of iteration for each algorithm are shown.

## Spatially-coupled nearly-regular LDPC code ensembles for rate-flexible code design

- **Status**: ✅
- **Reason**: Spatially-coupled nearly-regular 바이너리 LDPC ensemble의 rate-flexible 신규 구성 — E(코드 설계) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6883621
- **Type**: conference
- **Published**: 10-14 June
- **Authors**: Walter Nitzold, Gerhard P. Fettweis, Michael Lentmaier
- **PDF**: https://ieeexplore.ieee.org/document/6883621
- **Abstract**: Spatially coupled regular LDPC code ensembles have outstanding performance with belief propagation decoding and can perform close to the Shannon limit. In this paper we investigate the suitability of coupled regular LDPC code ensembles with respect to rate-flexibility. Regular ensembles with good performance and low complexity exist for a variety of specific code rates. On the other hand it can be observed that outside this set of favorable rational rates the complexity and performance penalty become unreasonably high. We therefore propose ensembles with slight irregularity that allow us to smoothly cover the complete range of rational rates. Our simple construction allows a performance with negligible gap to the Shannon limit while maintaining complexity as low as for the best regular code ensembles. At the same time the construction guarantees that asymptotically the minimum distance grows linearly with the length of the coupled blocks.

## Optimized bit mappings for spatially coupled LDPC codes over parallel binary erasure channels

- **Status**: ✅
- **Reason**: Spatially coupled LDPC의 bit mapper 최적화로 디코딩 threshold/wave 개선 — 바이너리 SC-LDPC 구성/성능 기법 이식 가능(E), 애매하지만 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6883627
- **Type**: conference
- **Published**: 10-14 June
- **Authors**: Christian Häger, Alexandre Graell i Amat, Alex Alvarado +2
- **PDF**: https://ieeexplore.ieee.org/document/6883627
- **Abstract**: In many practical communication systems, one binary encoder/decoder pair is used to communicate over a set of parallel channels. Examples of this setup include multi-carrier transmission, rate-compatible puncturing of turbo-like codes, and bit-interleaved coded modulation (BICM). A bit mapper is commonly employed to determine how the coded bits are allocated to the channels. In this paper, we study spatially coupled low-density parity check codes over parallel channels and optimize the bit mapper using BICM as the driving example. For simplicity, the parallel bit channels that arise in BICM are replaced by independent binary erasure channels (BECs). For two parallel BECs modeled according to a 4-PAM constellation labeled by the binary reflected Gray code, the optimization results show that the decoding threshold can be improved over a uniform random bit mapper, or, alternatively, the spatial chain length of the code can be reduced for a given gap to capacity. It is also shown that for rate-loss free, circular (tail-biting) ensembles, a decoding wave effect can be initiated using only an optimized bit mapper.

## An analysis into the loopy belief propagation algorithm over short cycles

- **Status**: ✅
- **Reason**: 바이너리 LDPC 짧은 girth에서 메시지 의존성 고려한 수정 BP 알고리즘 제안 — error floor 개선, 이식 가능 디코더(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6883618
- **Type**: conference
- **Published**: 10-14 June
- **Authors**: Nithin Raveendran, Shayan Garani Srinivasa
- **PDF**: https://ieeexplore.ieee.org/document/6883618
- **Abstract**: We investigate into the loopy belief propagation algorithm for binary low density parity check (LDPC) codes having cycles of small girth. Independence assumption among messages passed, assumed reasonable in all configurations of graphs, fails the most in graphical structures with short cycles. We investigate into this limitation and propose a modified algorithm, by considering dependency in the probability domain. This improves the performance of decoding over such graphs when compared to the original message passing algorithm at higher signal-to-noise ratio (SNR), thereby, yielding lower error floors.

## All-bit-line MLC flash memories: Optimal detection strategies

- **Status**: ✅
- **Reason**: MLC flash memory 채널 모델·optimal soft-output MAP 검출기 — A(NAND/플래시 직접), soft LLR 검출 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6883927
- **Type**: conference
- **Published**: 10-14 June
- **Authors**: Xiujie Huang, Meysam Asadi, Aleksandar Kavcic +1
- **PDF**: https://ieeexplore.ieee.org/document/6883927
- **Abstract**: We are concerned with the optimal detector design for the all-bit-line MLC flash memory. We provide a channel model of the MLC flash memory, where the channel parameters are mathematically tractable. Then we present an optimal maximum a-posteriori sequence detector. The optimal detector can be executed over a trellis whose branch metrics can be computed by using Fourier transforms of analytically computable characteristic functions (corresponding to likelihood functions). The soft-output detectors for both simple one-dimensional channel models and more realistic page-orientated two-dimensional channel models are derived. Simulation results show not only that the soft-output detector has the same hard-output bit-error-rate performance as some previously known detectors did, but that the soft-output detector outperforms previously known detectors by a gain of 0.23 dB.

## A low power and ultra high reliability LDPC error correction engine with Digital Signal Processing for embedded NAND Flash Controller in 40nm COMS

- **Status**: ✅
- **Reason**: NAND 플래시 컨트롤러용 LDPC ECC 엔진, DSP 기반 LLR 적응 계산·soft decoding·HW(40nm) — A/C/D 직접 해당
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6858405
- **Type**: conference
- **Published**: 10-13 June
- **Authors**: Wei Lin, Shao-Wei Yen, Yu-Cheng Hsu +7
- **PDF**: https://ieeexplore.ieee.org/document/6858405
- **Abstract**: A multi-mode Low-Density Parity-Check (LDPC) error correction engine with a Digital Signal Processing (DSP) module is presented for low power and ultra high reliability NAND Flash memory controllers. The DSP module improves the reliability of the storage systems via calculating the adaptive reliability information and translating the information into Log-Likelihood Ratio (LLR) for soft bit decoding. According to the experiment results on sub-20nm Triple Level per Cell (TLC) NAND Flash memory, the retention ability of LDPC with DSP is a 20 times improvement over BCH code and 2 to 5 times improvement over conventional LDPC. Moreover, the proposed decoder reaches a throughput over 400MB/s as well as a power consumption of 21.8mW under 40nm CMOS technology at 45 bit errors.

## Efficient column-layered decoders for single block-row quasi-cyclic LDPC codes

- **Status**: ✅
- **Reason**: binary QC-LDPC column-layered 디코더 아키텍처 + single-min 단순화, 이식 가능 HW (D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:6865153
- **Type**: conference
- **Published**: 1-5 June 2
- **Authors**: Chuan Zhang, Xiaohu You, Zhongfeng Wang
- **PDF**: https://ieeexplore.ieee.org/document/6865153
- **Abstract**: The recently proposed single block-row quasi-cyclic low-density parity-check (QC-LDPC) codes are favorable for high-speed applications. However, conventional decoder design methods are not suitable for this kind of codes. To tackle this issue, this paper aims at designing efficient column-layered single block-row QC-LDPC decoder architecture without affecting the decoding performance. Moreover, the simplified version which only requires single minimum value is also proposed for further hardware reduction. Results show that, for the rate-0.9006 (1640, 1477) single block-row QC-LDPC code, the proposed two designs achieves significant advantages in both hardware and latency over their row-layered counterpart.

## High-throughput QC-LDPC decoder with cost-effective early termination scheme for non-volatile memory systems

- **Status**: ✅
- **Reason**: NVM용 binary QC-LDPC layered min-sum 디코더 + 컬럼기반 조기종료(CB-ET) 기법, HW 구현 (A/C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6865738
- **Type**: conference
- **Published**: 1-5 June 2
- **Authors**: Yu-Min Lin, Yu-Hao Chen, Ming-Han Chung +1
- **PDF**: https://ieeexplore.ieee.org/document/6865738
- **Abstract**: This paper presents a high-throughput layered min-sum quasi-cyclic LDPC (QC-LDPC) decoder for non-volatile memory systems (NVMs). A cost-effective column-based early termination (CB-ET) scheme is proposed to early terminate decoding process within iteration. The throughput improvement is 37.7% compared to the state-of-the-art early termination scheme when raw bit error rate of flash memory is 3×10−3. The QC-LDPC decoder with proposed early termination scheme is synthesized by TSMC 90nm CMOS technology, and the area overhead is only 2.20%.

## A low-complexity LDPC decoder for NAND flash applications

- **Status**: ✅
- **Reason**: NAND 플래시 직접 대상 binary LDPC min-sum 디코더 + 2nd-min 비균일 양자화/정규화 기법 (A/C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6865103
- **Type**: conference
- **Published**: 1-5 June 2
- **Authors**: Mao-Ruei Li, Hsueh-Chih Chou, Yeong-Luh Ueng +1
- **PDF**: https://ieeexplore.ieee.org/document/6865103
- **Abstract**: This paper presents an efficient min-sum-based decoder for high-rate low-density parity-check (LDPC) codes, where the first minimum and second minimum values are stored in registers. In order to meet a strict cost requirement imposed by NAND flash applications, we provide different upper limits for the first and second minimum values. Furthermore, we use non-uniform quantization for the second minimum value so as to reduce storage complexity. In order to enhance the error-rate performance, the normalization factor is determined based on the difference between the first two minimum values. Using the proposed techniques, a reduction in gate count of 13.36% can be achieved without suffering any degradation in error-rate performance. The implementation results for a rate-0.896 length-18624 layered decoder show that this decoder can achieve a throughput of 765.24 Mb/s at a clock frequency of 166 MHz with a gate count of 620K.

## The error-correcting capabilities of low-complexity decoded H-LDPC code as irregular LDPC code

- **Status**: ✅
- **Reason**: H-LDPC(불규칙 LDPC)용 신규 하드결정 저복잡도 반복 디코딩 알고리즘 제시 — 디코더 기법(C) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7016711
- **Type**: conference
- **Published**: 1-5 June 2
- **Authors**: Pavel Rybin
- **PDF**: https://ieeexplore.ieee.org/document/7016711
- **Abstract**: This paper deals with the Low-Density Parity-Check codes with the constituent Hamming codes (H-LDPC codes) and two different iterative hard-decision low-complexity decoding algorithms. Both algorithms are based on the same main idea: the decreasing of the syndrome weight on each step of the decoding algorithm. The first decoding algorithm uses the properties of the constituent Hamming code. The best known lower-bound on the guaranteed corrected errors fraction for the H-LDPC codes under the first decoding algorithm was obtained in 2011. The second decoding algorithm considers H-LDPC as the irregular LDPC code and uses the well-known majority decoding algorithm. The lower-bound on the guaranteed corrected errors fraction for H-LDPC code under the second decoding algorithm is introduced for the first time in this paper. Numerical results for the lower-bound, obtained in this paper for H-LDPC code under the second decoding algorithm, significantly exceed the numerical results for the best known lower-bounds, obtained previously for H-LDPC code under the first decoding algorithm.

## Low-Density Parity-Check codes based on Partial Unit Memory codes

- **Status**: ✅
- **Reason**: binary LDPC 블록부호를 PUM 부호 기반으로 구성, BP/SPA 디코딩 — 이식 가능 코드설계 (E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7016705
- **Type**: conference
- **Published**: 1-5 June 2
- **Authors**: Fedor Ivanov, Victor Zyablov
- **PDF**: https://ieeexplore.ieee.org/document/7016705
- **Abstract**: In this paper we describe ensemble of Low-Density Parity-Check (LDPC) block codes based on Partial Unit Memory (P)UM codes. We study a decoding performance of received ensemble in the case of different parameters of constituent LDPC codes. The results of simulation of obtained code constructions for an iterative “belief propagation” (Sum-Product) decoding algorithm, applied in the case of transmission of a code word via a binary channel with an additive Gaussian white noise and BPSK modulation, are presented.

## LDPC code construction as a generalized concatenated code

- **Status**: ✅
- **Reason**: LDPC 성분부호 일반연접 구성+BP 결합 신규 소프트 디코딩 — 코드설계(E)/디코더(C) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7016716
- **Type**: conference
- **Published**: 1-5 June 2
- **Authors**: Igor Zhilin, Victor Zyablov
- **PDF**: https://ieeexplore.ieee.org/document/7016716
- **Abstract**: We propose a construction of general concatenated code that uses low-density parity check codes as component codes. This construction itself can also be considered as low-density parity-check code and decoded using Belief Propagation algorithm. Performances of several decoders are compared; it's shown that this code can be efficiently decoded by proposed soft decoding algorithm or combining BP and proposed algorithm.

## Multilevel error correction scheme for MLC flash memory

- **Status**: ✅
- **Reason**: MLC 플래시용 multilevel FEC + LDPC codec — NAND 직접(A)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6865100
- **Type**: conference
- **Published**: 1-5 June 2
- **Authors**: Zhiqiang Cui, Zhongfeng Wang, Xinming Huang
- **PDF**: https://ieeexplore.ieee.org/document/6865100
- **Abstract**: Storing multiple bits in a flash memory cell is a primary technique to linearly increase flash memory capacity, but memory endurance is tremendously sacrificed. This paper presents a multilevel fault tolerance technique for MLC flash memories. The main idea is to explore multi-level forward error correction (FEC) for multiple bits in a flash cell. The associated practical implementation issues are well addressed in this paper. Compared to the conventional error protection methods for flash memory, the proposed multi-level FEC approach can obtain much larger system coding gain using the same amount of redundant bits. As a result, the proposed technique reduces power consumption considerably compared to the conventional methods since the required throughout of LDPC codec is drastically reduced. It can also increase flash memory endurance as it can allocate more redundancy to LDPC code while maintaining overall redundancy ratio.

## EC-Cache: Exploiting error locality to optimize LDPC in NAND flash-based SSDs

- **Status**: ✅
- **Reason**: NAND SSD LDPC 디코딩 지연 완화용 error-locality 캐시 — NAND 직접 ECC 시스템 기법 (A)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6881472
- **Type**: conference
- **Published**: 1-5 June 2
- **Authors**: Ren-Shuo Liu, Meng-Yen Chuang, Chia-Lin Yang +3
- **PDF**: https://ieeexplore.ieee.org/document/6881472
- **Abstract**: Low-density parity-check (LDPC) is widely accepted as the baseline error-correction codes offering strong error-correcting capability for future NAND flash-based SSDs. However, LDPC incurs read performance overhead because of its complex decoding procedure. To mitigate such overhead, we propose the error-correcting cache (EC-Cache) that exploits the “error locality” of NAND flash. Error locality means that the majority of errors in reads to the same NAND flash page appear in the same positions until the page is erased. By caching detected errors, EC-Cache can correct a significant portion of errors present in a requested flash page before the associated LDPC decoding process begins. EC-Cache can greatly speed up LDPC decoding because LDPC's latency is directly correlated to the number of errors present in the input data. Experimental results show that EC-Cache achieves up to 2.6× SSD read performance gain.

## Architectures for polar BP decoders using folding

- **Status**: ✅
- **Reason**: polar BP 디코더 HW(folding/overlapped scheduling); polar 전용이나 BP 스케줄링/folding 기법 이식 여지, 애매하여 살림(Phase 3)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:6865101
- **Type**: conference
- **Published**: 1-5 June 2
- **Authors**: Bo Yuan, Keshab K. Parhi
- **PDF**: https://ieeexplore.ieee.org/document/6865101
- **Abstract**: Capacity-achieving polar codes have received significant attention in past few years. These codes can be decoded using either the successive-cancellation (SC) approach or the belief propagation (BP) approach. Several VLSI architectures of SC polar decoders have been reported in the literature. However, SC decoders suffer from long latency and low throughput due to their sequential decoding nature. On the other hand, although the BP decoders can be operated in an inherently parallel manner with high throughput, the functional units in these decoders are underutilized. In this paper, we exploit various architecture transformation techniques to further improve hardware performance of polar BP decoders. First, we propose an overlapped-scheduling approach at iteration level to reduce the overall decoding latency. Second, we propose codeword-level overlap to further improve hardware utilization efficiency. Third, we show that the above two overlapping approaches can be unified into a general framework into a joint overlapping approach. Fourth, we exploit the folding technique to design low-complexity polar BP decoders, and present two types of folded architectures. Synthesis results show that the proposed two (1024, 512) polar BP decoder designs can achieve 1.50 and 2.43 times reduction in hardware complexity, respectively. In addition, the proposed two designs can also achieve 7.4 and 2.5 times improvement in hardware efficiency, respectively.
