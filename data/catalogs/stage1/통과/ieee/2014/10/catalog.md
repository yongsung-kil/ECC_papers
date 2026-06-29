# IEEE Xplore — 2014-10 (1차선별 통과)


## Unified turbo/LDPC code decoder architecture for deep-space communications

- **Status**: ✅
- **Reason**: turbo+LDPC 동일 알고리즘 기반 통합 HW 디코더(datapath/memory 공유, VLSI) — LDPC 디코더 HW 아키텍처로 이식 가능(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:6978902
- **Type**: journal
- **Published**: October 20
- **Authors**: Carlo Condo, Guido Masera
- **PDF**: https://ieeexplore.ieee.org/document/6978902
- **Abstract**: Deep-space communications are characterized by extremely critical conditions; current standards foresee the usage of both turbo and low-density-parity-check (LDPC) codes to ensure recovery from received errors, but each of them displays consistent drawbacks. Code concatenation is widely used in all kinds of communication to boost the error correction capabilities of single codes; serial concatenation of turbo and LDPC codes has been recently proven effective enough for deep space communications, being able to overcome the shortcomings of both code types. This work extends the performance analysis of this scheme and proposes a novel hardware decoder architecture for concatenated turbo and LDPC codes based on the same decoding algorithm. This choice leads to a high degree of datapath and memory sharing; postlayout implementation results obtained with complementary metal-oxide semiconductor (CMOS) 90 nm technology show small area occupation (0.98 mm2) and very low power consumption (2.1 mW).

## Large Girth Column-Weight Two and Three LDPC Codes

- **Status**: ✅
- **Reason**: girth-12 cycle code 및 binary QC-LDPC(column-weight 3) 신규 구성 — 바이너리 코드 설계(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6881655
- **Type**: journal
- **Published**: Oct. 2014
- **Authors**: Mohammad Gholami, Ghaffar Raeisi
- **PDF**: https://ieeexplore.ieee.org/document/6881655
- **Abstract**: In this paper, the concept of broken diagonal pair in the chess-like square board is used to define some well-structured block designs whose incidence matrices can be considered as the parity-check matrices of some high rate cycle codes with girth 12. Interestingly, the constructed regular cycle codes with row-weights  $t$,  $3\leq t\leq 20$,  $t\neq 7,15,16$, have the minimum lengths among the known regular girth-12 cycle codes. In addition, the proposed cycle codes can be easily extended to some high rate column weight-3 LDPC codes with girth 6. Simulation results show that the constructed non-binary cycle codes and binary QC LDPC codes have good performances over AWGN channel.

## Efficient Decoder Architecture for Single Block-Row Quasi-Cyclic LDPC Codes

- **Status**: ✅
- **Reason**: QC-LDPC용 신규 디코더 아키텍처로 메모리 20.8% 절감, subblock-sharing 기법 — 이식 가능 HW(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:6871329
- **Type**: journal
- **Published**: Oct. 2014
- **Authors**: Chuan Zhang, Zhongfeng Wang, Xiaohu You
- **PDF**: https://ieeexplore.ieee.org/document/6871329
- **Abstract**: Single block-row quasi-cyclic low-density parity-check codes have been proposed for high-speed applications recently. However, no existing work has systematically addressed the decoder design issue for such kind of codes. In this brief, an efficient decoder architecture for such kinds of codes is proposed by exploring the geometry properties of the check matrix. Compared with conventional approaches, the proposed method can achieve more than 20.8% of memory reduction. Additionally, the subblock-sharing technique and the suboptimal low-latency searching method are employed to further reduce the hardware complexity.

## High-Throughput Cognitive-Amplification Detector for LDPC Decoders

- **Status**: ✅
- **Reason**: LDPC 디코더의 min/sub-min 계산을 위한 새 HW 검출기(CAD)로 throughput/리소스 개선 — 이식 가능 HW 아키텍처(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:6870670
- **Type**: journal
- **Published**: Oct. 2014
- **Authors**: Melvin Heng Li Lim, Wang Ling Goh
- **PDF**: https://ieeexplore.ieee.org/document/6870670
- **Abstract**: With the advent of technology over the recent years, the low-density parity-check (LDPC) codes, which were once seen as an impractical concept, are now poised to be the next big thing in the communication standards of today for their near-capacity performances. Nonetheless, the physical implementation of LDPC decoders is more often than not encumbered by the arithmetic of its decoding algorithm. Entangled by numerous computations of minima, LDPC decoders not only require considerable amount of resources to the implement cascaded pair-wise comparators, but also yield low decoding throughputs. In this paper, we propound a novel design for the computation of minimum and subminimum in LDPC decoding, known as the cognitive-amplification detector (CAD). By leveraging on the finite precision of fixed-point binary representation in actual hardware, our CAD proposition renders significant gains in decoding throughput and savings in resource consumption of up to 20% and 15%, respectively, not to mention negligible trade-offs in error-correcting capabilities.

## New Stopping Criterion for Fast Low-Density Parity-Check Decoders

- **Status**: ✅
- **Reason**: APP 증가를 이용한 새 T-tolerance 정지 기준으로 평균 반복수 감소 — 부호 비의존적 MP 디코더 개선(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6881612
- **Type**: journal
- **Published**: Oct. 2014
- **Authors**: Tian Xia, Hsiao-Chun Wu, Hong Jiang
- **PDF**: https://ieeexplore.ieee.org/document/6881612
- **Abstract**: Low-density parity-check (LDPC) codes are favorable in low bit-error-rate and high code-rate applications. However, the decoding complexity for LDPC codes is quite large, especially for nonbinary LDPC codes. In this paper, we propose a new  $T$-tolerance stopping criterion for LDPC decoders by exploiting the fact that the total a posteriori probability (APP) should increase across iterations when message passing (MP) algorithms are employed. Simulation results demonstrate that our proposed new  $T$-tolerance criterion can greatly reduce the average iteration number (complexity) while the decoding performance degradation is controlled within 0.1 dB in the low bit-energy-to-noise-spectral-density ratio  $(E_{b}/N_{0})$ scenarios.

## Quasi-Cyclic LDPC Codes Based on Pre-Lifted Protographs

- **Status**: ✅
- **Reason**: 프리-리프팅 프로토그래프 기반 QC-LDPC 2단계 리프팅으로 minimum distance·girth 개선 — 바이너리 코드 설계 기법(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6863699
- **Type**: journal
- **Published**: Oct. 2014
- **Authors**: David G. M. Mitchell, Roxana Smarandache, Daniel J. Costello
- **PDF**: https://ieeexplore.ieee.org/document/6863699
- **Abstract**: Quasi-cyclic low-density parity-check (QC-LDPC) codes based on protographs are of great interest to code designers because analysis and implementation are facilitated by the protograph structure and the use of circulant permutation matrices for protograph lifting. However, these restrictions impose undesirable fixed upper limits on important code parameters, such as minimum distance and girth. In this paper, we consider an approach to constructing QC-LDPC codes that uses a two-step lifting procedure based on a protograph, and, by following this method instead of the usual one-step procedure, we obtain improved minimum distance and girth properties. We also present two new design rules for constructing good QC-LDPC codes using this two-step lifting procedure, and in each case, we obtain a significant increase in minimum distance and achieve a certain guaranteed girth compared with one-step circulant-based liftings. The expected performance improvement is verified by simulation results.

## Noisy Gradient Descent Bit-Flip Decoding for LDPC Codes

- **Status**: ✅
- **Reason**: Noisy GDBF 비트플립 디코더 — 바이너리 LDPC AWGN, 완전 병렬 신규 디코더+HW(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6894606
- **Type**: journal
- **Published**: Oct. 2014
- **Authors**: Gopalakrishnan Sundararajan, Chris Winstead, Emmanuel Boutillon
- **PDF**: https://ieeexplore.ieee.org/document/6894606
- **Abstract**: A modified Gradient Descent Bit Flipping (GDBF) algorithm is proposed for decoding Low Density Parity Check (LDPC) codes on the binary-input additive white Gaussian noise channel. The new algorithm, called Noisy GDBF (NGDBF), introduces a random perturbation into each symbol metric at each iteration. The noise perturbation allows the algorithm to escape from undesirable local maxima, resulting in improved performance. A combination of heuristic improvements to the algorithm are proposed and evaluated. When the proposed heuristics are applied, NGDBF performs better than any previously reported GDBF variant, and comes within 0.5 dB of the belief propagation algorithm for several tested codes. Unlike other previous GDBF algorithms that provide an escape from local maxima, the proposed algorithm uses only local, fully parallelizable operations and does not require computing a global objective function or a sort over symbol metrics, making it highly efficient in comparison. The proposed NGDBF algorithm requires channel state information which must be obtained from a signal to noise ratio (SNR) estimator. Architectural details are presented for implementing the NGDBF algorithm. Complexity analysis and optimizations are also discussed.

## Ultra-low complexity early termination scheme for layered LDPC decoding

- **Status**: ✅
- **Reason**: Ultra-low complexity early termination for layered LDPC decoding; portable decoder/HW technique (C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7031199
- **Type**: conference
- **Published**: 7-10 Oct. 
- **Authors**: Yuan-Syun Wu, Cheng-Hung Lin, Shu-Yen Lin
- **PDF**: https://ieeexplore.ieee.org/document/7031199
- **Abstract**: Energy consumption is a major issue for LDPC decoding. To save LDPC iterative process energy, early terminations are commonly used. Traditional parity check equation is used but has a growing complexity as the block size increases. This requires a large overhead in term of area. This paper proposes an ultra-low complexity early termination (ET) scheme with a small loss of bit error rate performance based on the layer stopping (LS) criterion. The proposed ET scheme is performed by checking the number of convergent layers stopped by the LS criterion with a preset threshold. Compared with other ET schemes, the proposed ET scheme has a negligible hardware overhead and an acceptable bit error rate performance.

## Design and Implementation of Seamless Rate Adaptive Decoder

- **Status**: ✅
- **Reason**: Seamless rate adaptive 디코더 ASIC 구현(부분병렬 아키텍처, fixed-point, Jacobian 근사 병렬화) — 카테고리 D HW 기법 이식 가능성, 애매하여 살림.
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:6956785
- **Type**: conference
- **Published**: 6-8 Oct. 2
- **Authors**: Lu Qiu, Min Wang, Jun Wu +2
- **PDF**: https://ieeexplore.ieee.org/document/6956785
- **Abstract**: Seamless rate adaptation (SRA) is one of the promising rate adaptive schemes for wireless communication system. However, the high complexity of decoding hinders its application. We propose an optimized Application-specific integrated circuit (ASIC) design and implementation for SRA decoder in this paper. In order to balance speed and resource consumption, a partial parallel architecture is used in SRA decoder, which consists of 8x8 parallel computation unit, each computation unit calculates decoding metrics in pipelining way. In order to further improve the throughput of the decoder, a parallel structure for multivariable Jacobian logarithm approximation is designed. We also illustrate how fixed-point SRA decoder is designed. Numerical simulation shows the decoding performance of our design has neglect able performance loss. The optimized decoder ASIC can achieve 84Mbps throughput running at 300Mhz, occupying an area of 5 5mm2 and consuming power 4.21W. Compared to our previous design in FPGA, the throughput of this ASIC increases about 17:5 times.

## Uniformly reweighted APP decoder for memory efficient decoding of LDPC Codes

- **Status**: ✅
- **Reason**: reweighted APP 디코더 + 메모리 효율 구현 — 이식 가능한 BP 변형 디코더(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7028595
- **Type**: conference
- **Published**: 30 Sept.-3
- **Authors**: Velimir Ilić, Elsa Dupraz, David Declercq +1
- **PDF**: https://ieeexplore.ieee.org/document/7028595
- **Abstract**: In this paper we propose a uniformly reweighted a posteriori probability (APP) decoder. The APP decoder is well-known to be suboptimal compared to the BP decoder. Here, we derive the APP decoder as an algorithm of approximate Bayesian inference on the LDPC code graph and introduce a correction parameter to overcome the suboptimaly of the APP decoder. We optimize numerically the correction parameter and show that it improves the BER performance of the APP decoder compared to its non-corrected version. In addition, the original APP decoder requires memory that is linear in the number of edges in the code graph. Here, we propose a memory efficient implementation of the algorithm that requires memory that is linear only in the codeword length.

## LDPC decoder for WiMAX on NOC based multiprocessor platform

- **Status**: ✅
- **Reason**: WiMAX binary LDPC decoder on NoC multiprocessor with layered decoding + parallelism/data-exchange strategy; portable HW/parallel architecture (D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:7021351
- **Type**: conference
- **Published**: 28-31 Oct.
- **Authors**: Lingyun Zeng, Tengyue Yuan, Jun Han +1
- **PDF**: https://ieeexplore.ieee.org/document/7021351
- **Abstract**: Low density parity check (LDPC) code is an error correct code that can achieve performance close to Shannon limit and it is widely adopted in communication systems such as WiMAX and Wi-Fi. This paper presents a design of a flexible LDPC decoder for WiMAX based on the NoC platform. The implementation adopts layered decoding algorithm and exploits high parallelism that lies in the algorithm. Considering large quantity of data exchange between cores, we use stepped data exchange strategy and master-slave structure to reduce communication cost. The Cycle accurate simulation results show high speed-up and scalability of code rate of 5/6 with different code length in WiMAX in 4/8/16 processor systems.

## A construction of LDPC convolutional codes with close distance bounds

- **Status**: ✅
- **Reason**: LDPC convolutional code 신규 구성, 4-cycle free 설계로 BP 디코딩 효율화 — 이식 가능 코드설계(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6979809
- **Type**: conference
- **Published**: 26-29 Oct.
- **Authors**: Tien-Hui Chen, Kuan-Chen Chen, Mao-Chao Lin
- **PDF**: https://ieeexplore.ieee.org/document/6979809
- **Abstract**: A trellis code constructed by concatenating a delay processor and a signal mapper to a convolutional code with a short constraint length can be regarded as a convolutional code with a large constraint length. We can obtain a close upper bound and a close lower bound for such a code. In this paper, we use this code structure to construct low-density parity check convolutional codes which are 4-cycles free and hence can be efficiently decoded by the iterative message-passing algorithm.

## Optimized degree distributions for binary and non-binary LDPC codes in Flash memory

- **Status**: ✅
- **Reason**: Flash 메모리 직접(A): hard/soft read 양자화 기반 LDPC degree distribution 최적화, EXIT/RCA 분석으로 바이너리 LDPC 설계 기법 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6979792
- **Type**: conference
- **Published**: 26-29 Oct.
- **Authors**: Kasra Vakilinia, Dariush Divsalar, Richard D. Wesel
- **PDF**: https://ieeexplore.ieee.org/document/6979792
- **Abstract**: This paper uses extrinsic-information-transfer (EXIT)-function analysis employing the reciprocal channel approximation (RCA) to obtain optimal LDPC code degree distributions for initial hard decoding (one-bit quantization of the channel output) and for decoding with the soft information provided by additional reads in both SLC (two-level cell) and MLC (four-level-cell) Flash memory. These results indicate that design for hard decoding can provide irregular degree distributions that have good thresholds across the range of possible decoding precisions. These results also quantify the potential benefit of irregular LDPC codes as compared to regular LDPC codes in the flash setting and compare the RCA-EXIT thresholds of word-line voltages optimized for maximum mutual information (MMI) and word-line voltages that explicitly minimize the RCA-EXIT threshold of a specific LDPC degree distribution. Along the way, this paper illustrates that the MMI optimization of word-line voltages for five reads is a quasi-convex problem for the Gaussian model of SLC Flash. The paper also uses RCA-based EXIT analysis to show that for the same spectral efficiency of 0.9 bits per cell, rate-0.45 non-binary LDPC codes on MLC Flash systems provide thresholds more than 0.5 dB better than rate-0.9 binary LDPC codes on SLC Flash with the same number of reads (i.e. three reads that would provide hard decisions for MLC and limited soft information for SLC). The MLC approach has a potential threshold improvement of more than 1.5 dB over the SLC approach when both systems have access to the full soft information.

## Estimation of areal density gains of TDMR system with 2D detector

- **Status**: ✅
- **Reason**: HDD 스토리지 ECC, 새 cross-track LDPC 코딩 스킴(코드워드가 2트랙 span) (B/E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6979929
- **Type**: conference
- **Published**: 26-29 Oct.
- **Authors**: Rathnakumar Radhakrishnan, Nedeljko Varnica, Mats Öberg
- **PDF**: https://ieeexplore.ieee.org/document/6979929
- **Abstract**: Two-dimensional magnetic recording (TDMR) is expected to drive continued areal density growth of hard-disk drives (HDDs) as the growth for conventional perpendicular magnetic recording (PMR)-based HDDs is slowing down. Feasibility of manufacturing more than one reader in a single head has hastened the development of TDMR and considerable effort is underway in developing read channels that can exploit the availability of multiple readers. First generation of TDMR-based HDDs will likely derive its gains from the SNR improvement obtained by combining multiple readback signals to remove inter-track interference (ITI). In this case, data belonging to a single track of interest is subsequently detected. A natural extension to this system is to combine the readback signals without removing ITI and jointly detecting data belonging to two tracks using a two-dimensional detector. Under the assumption that tracks are written synchronously, in this paper, we explore from a systems perspective if further areal density gains can be obtained from such a system. We employ a grain-based channel model for our investigation and estimate gains by appropriate optimization of the dual-reader systems, including optimizing reader placement. Furthermore, for the set of reader placement configurations, which affords reliable detection of both tracks, we introduce a new coding scheme called cross-track coding and show that additional areal density gains can be obtained. In this scheme, user data is LDPC-encoded and written such that every codeword spans two tracks as opposed to one track as in conventional PMR.

## Symbol-level synchronization using probability lookup-table for IDS error correction

- **Status**: ✅
- **Reason**: 스토리지(BPM) 외부 LDPC+inner marker 연접; 기여는 마커 동기화지만 LDPC ECC 인접이라 Phase3 재검토
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6979900
- **Type**: conference
- **Published**: 26-29 Oct.
- **Authors**: Haruhiko Kaneko
- **PDF**: https://ieeexplore.ieee.org/document/6979900
- **Abstract**: Insertion/Deletion/Substitution (IDS) error correction will become important for future high-density storage devices, e.g., bit-patterned media. For IDS error correction, concatenated codings of an outer LDPC code and an inner marker code have been proposed. To improve the synchronization capability, marker decoder can employ symbol-level synchronization (SLS) with a large symbol size, while the computational time complexity of the SLS increases exponentially with the symbol size. This paper proposes an SLS using a probability lookup table to reduce the complexity. Probabilities in the table are precomputed for given channel and code parameters, and computationally intensive calculations of the SLS are replaced by table lookups. The proposed method is applicable to both single-path and multipath decodings. The bit error rate (BER) is evaluated for SLS of symbols sizes bS = 1, 2, 4, and 8 bits, and it is confirmed that larger symbol size gives lower BER.

## Lower error floor of LDPC codes based on trapping sets elimination

- **Status**: ✅
- **Reason**: 트래핑셋 제거로 error floor 저감하는 노드 재배열 알고리즘 — 바이너리 LDPC 코드설계(E) 이식 가능, 디스크 스토리지 언급
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6992175
- **Type**: conference
- **Published**: 23-25 Oct.
- **Authors**: Le Dong, Ziyu Zhao, Jing Lei +1
- **PDF**: https://ieeexplore.ieee.org/document/6992175
- **Abstract**: LDPC codes with excellent performance have great potential in applications of wireless mobile communications. However, the error floor phenomenon existing in LDPC codes limits its further application in disk storage and deep-space communications which require very low bit error rate (BER) system. The researchers find that trapping sets are the major reason why the LDPC codes have error floor. In this paper, we proposed an elimination algorithm to reduce small trapping sets. It was applying node rearrangement method to optimize the neighborhood of target nodes. In this way, cycles will be broken and the small size of trapping sets can be eliminated. The experimental results show that it can lower the error floor to improve the performance of LDPC codes. Besides, we also can keep the degree distribution, code rates and girth features of the original code with this method.

## The hardware design of LDPC decoder in IEEE 802.11n/ac

- **Status**: ✅
- **Reason**: IEEE 802.11n/ac LDPC 디코더 부분병렬 HW 아키텍처 + permutation network 생성기 — HW 아키텍처(D) 이식 가능
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:7090144
- **Type**: conference
- **Published**: 23-25 Oct.
- **Authors**: Hyobeen Park, Seongjoo Lee
- **PDF**: https://ieeexplore.ieee.org/document/7090144
- **Abstract**: In this paper, the design of the LDPC decoder architecture in IEEE 802.11n/ac is proposed. The proposed decoder is used to the partial parallel architecture to provide 2 Gbps throughput at 200 MHz clock frequency. In IEEE 802.11n/ac, 12 parity check metrics is provide to support diverse code rates and block lengths. Therefore the network between nodes is configured to be satisfied parity check metrics. However, the structure of the network increases the complexity of LDPC decoder. Hence, the optimized network generator is also proposed to reduce the complexity of the network.

## On the design of MLC-LDPC-OFDM in DRM MF and HF channels

- **Status**: ✅
- **Reason**: MLC-LDPC LLR(우도비) 계산을 채널모델 따라 수정 — LLR 계산 변형은 NAND 디코더에 이식 가능, 애매하므로 보류
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6992075
- **Type**: conference
- **Published**: 23-25 Oct.
- **Authors**: Yuan Liang, Shulin Zhang, Pinbiao Gu +1
- **PDF**: https://ieeexplore.ieee.org/document/6992075
- **Abstract**: Orthogonal Frequency Division Multiplexing (OFDM), aided by proper channel coding schemes, can realize very dependable transmission in fading channels. For the purpose of improving the performance of the OFDM based DRM digital AM broadcasting in MF and HF channels, this paper designs MLC-LDPC-OFDM transmission scheme that is suitable for MF and HF channels. The equivalent channel capacities of MLC-LDPC-OFDM with two different decoding strategies, namely IMSD and PDL, are analyzed, basing on which this paper redesigns the code rates of MLC. In addition, the calculation of likelihood ratio in LDPC decoding is modified according to channel models. The simulation results show that the proposed schemes have better performance than the existing ones in MF and HF channels.

## Performance optimization of generalized low-density parity-check codes with EXIT chart method for data transmission over partial-band jamming channels

- **Status**: ✅
- **Reason**: GLDPC 부호 EXIT chart 최적화로 저부호율 설계 — 이식 가능 코드 설계 기법(E), 애매하나 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6983179
- **Type**: conference
- **Published**: 22-24 Oct.
- **Authors**: Qi Li, Xinru Qu, Liuguo Yin +1
- **PDF**: https://ieeexplore.ieee.org/document/6983179
- **Abstract**: The design and optimization of low coding-rate channel codes is a hot topic for frequency-hopping spread-spectrum (FH-SS) transmission systems over harsh wireless channels. In this paper, we use extrinsic mutual information transfer (EXIT) chart to optimize a class of generalized low-density parity-check (GLDPC) codes over partial-band jamming (PBJ) transmission environment. With the proposed method, the channel capacity of the PBJ channel is illustrated, and based on which three code optimization methods are presented for achieving near-capacity performance. Simulation results show that, the GLDPC codes designed with the proposed method can achieve an information rate of 91.2% of the channel capacity, over the PBJ channel with 50% frequency band jammed and the channel signal-to-noise ratio (SNR) of the unjammed frequency band equals to -8 dB.

## Optimal voltage signal sensing of NAND flash memmory for LDPC code

- **Status**: ✅
- **Reason**: NAND 플래시 LDPC용 임계전압 센싱 전략(Ununiform-SOR)으로 LLR/센싱 최적화 — A 직접 해당
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6986077
- **Type**: conference
- **Published**: 20-22 Oct.
- **Authors**: Shigui Qi, Dan Feng, Jingning Liu
- **PDF**: https://ieeexplore.ieee.org/document/6986077
- **Abstract**: Low-density parity-check (LDPC) code can provide stronger error correcting performance in NAND flash memory. LDPC decoder requires accurate soft-decision log-likelihood ratio (LLR) information which demands fine-grained flash memory threshold voltage sensing operations. The threshold voltage sensing operations incur energy consumption and access latency penalty. Therefore, it is important to minimize the flash memory sensing operations without noticeable error correcting performance decreasing. We propose a new flash memory sensing strategy Ununiform-SOR (ununiform sensing in overlapping region) which can reduce 20% flash memory sensing operations than traditional non-uniform threshold voltage sensing without reducing the error correcting performance of LDPC code in NAND flash memory noise channel. The new Ununiform-SOR sensing strategy can reduce more than 20% reading energy consumption than the non-uniform sensing strategy. The abstract goes here.

## FPGA implementation of a clockless stochastic LDPC decoder

- **Status**: ✅
- **Reason**: FPGA clockless stochastic LDPC 디코더 HW 구현 — 이식 가능 HW 아키텍처(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:6986088
- **Type**: conference
- **Published**: 20-22 Oct.
- **Authors**: Chris Ceroici, Vincent C. Gaudet
- **PDF**: https://ieeexplore.ieee.org/document/6986088
- **Abstract**: This paper demonstrates a clockless stochastic low-density parity-check (LDPC) decoder implemented on a Field-Programmable Gate Array (FPGA). Stochastic computing reduces the wiring complexity necessary for decoding by replacing operations such as multiplication and division with simple logic gates and serial processing. Clockless decoding increases the throughput of the decoder by eliminating the requirement for node signals to be synchronized after each decoding cycle. The design is implemented on an ALTERA Stratix IV EP4SGX230 FPGA and the frame error rate (FER), throughput, and power performance are presented for (96,48) and (204,102) LDPC decoders.

## Dual port ram based layered decoding for Multi Rate Quasi-Cyclic LDPC codes

- **Status**: ✅
- **Reason**: 멀티레이트 QC-LDPC layered 디코딩 dual-port RAM FPGA 아키텍처(permutation→address) — D 이식 가능 HW
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:7015253
- **Type**: conference
- **Published**: 19-23 Oct.
- **Authors**: Soner Yeşil, Murat Arslan
- **PDF**: https://ieeexplore.ieee.org/document/7015253
- **Abstract**: This paper presents a generic RAM based FPGA architecture for decoding of Multi Rate Quasi-Cycling LDPC codes. RAM based decoding enables us to reduce permutation networks into simple address controllers. Moreover, utilizing Block RAMs with various aspect ratios in an FPGA provides flexibility ranging from area driven compact designs to fully parallelized high throughput designs. Utilizing the read-first property of the RAMs, the proposed design efficiently exploits the dual port Block RAM resources by accessing all the four ports at the same time. Such facilities of recent FPGA devices have been combined with the well known layered decoding algorithm with non-linearly mapped Min-Sum approximation in order to obtain area efficient yet high throughput decoders. The proposed decoder architecture has been verified on Xilinx XC7Z020 FPGA device for IEEE 802.16e Wimax LDPC codes. 340Mbps of information throughput has been observed at an operating frequency of 150MHz.

## Low Density Parity Check codes with quasi-cyclic structure and zigzag pattern

- **Status**: ✅
- **Reason**: 바이너리 QC-LDPC 신규 구성(IRA-like, zigzag, 저중량 코드워드·짧은 사이클 제거) — 코드 설계 기법 이식 가능(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7015290
- **Type**: conference
- **Published**: 19-23 Oct.
- **Authors**: Wenwen Li, Bin Chen, Jing Lei +1
- **PDF**: https://ieeexplore.ieee.org/document/7015290
- **Abstract**: Low-Density Parity-Check (LDPC) codes with linear time encoding complexity and low hardware storage are a hot issue recently. We propose a general method for constructing LDPC codes with quasi-cyclic (QC) structure and improved zigzag pattern to obtain both linear time encoding and low hardware storage. We call it irregular repeat accumulate like (IRA-like) codes for its similarity with irregular repeat accumulate (IRA) codes. Through the optimization-constraint of QC-LDPC codes and the modification of dual diagonal structure we have acquired IRA-like codes with reduced number of low-weight codewords and short cycles. Extensive simulation results show that the IRA-like codes not only achieve better performance than some kinds of classical LDPC codes but also have much better practicability. Compared with the LDPC code applied in China Mobile Multimedia Broadcasting (CMMB), IRA-like code significantly outperforms the CMMB-LDPC code about 0.18 dB at BER=10-5.

## A new simplified RRWBF decoding algorithm for LDPC decoder in CMMB

- **Status**: ✅
- **Reason**: 단순화된 RRWBF 소프트값 비트플리핑 LDPC 디코딩 알고리즘 신규 제안, 부호 비의존적 바이너리 LDPC 디코더로 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7003892
- **Type**: conference
- **Published**: 14-16 Oct.
- **Authors**: Xiangran Sun, Yunyun Wei
- **PDF**: https://ieeexplore.ieee.org/document/7003892
- **Abstract**: A new soft-value bit-flipping low-density parity-check (LDPC) decoding is proposed based on a simplified reliability ratio based on weighted bit-flipping (RRWBF) algorithm. Moreover, we design a soft-output demapping and soft-decision decoding for the LDPC code in China Mobile Multimedia Broadcasting (CMMB). In addition, the complexity of decoding and the consumption of hardware is reduced effectively by our proposed simplified algorithm.

## Design of a multi-rate quasi-cyclic low-density parity-check encoder based on pipelined rotate-left-accumulator circuits

- **Status**: ✅
- **Reason**: 멀티레이트 QC-LDPC 인코더 파이프라인 RLA 회로 FPGA HW 구현, 이식 가능 HW 아키텍처(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:7003945
- **Type**: conference
- **Published**: 14-16 Oct.
- **Authors**: Fei Wang, Peng Zhang, Xin Wan +1
- **PDF**: https://ieeexplore.ieee.org/document/7003945
- **Abstract**: A serial-input serial-output encoder based on pipelined rotate-left-accumulator (RLA) circuits is designed for multi-rate Quasi-Cyclic Low-Density Parity-Check (QC-LDPC) codes of Chinese digital terrestrial/television multimedia broadcasting (DTMB) standard. The RLA circuit can make the area usage economical, and the pipelined architecture can simplify the memory structure. The encoder is implemented on FPGA. Simulation results demonstrate that the design meets the requirement of DTMB standard with lower energy consumption and fewer hardware resources.

## Simplified partially parallel DVB-S2 LDPC decoder architectural design based on FPGA

- **Status**: ✅
- **Reason**: D: DVB-S2 LDPC FPGA 부분병렬 디코더, 신규 barrel shifter·BNU/CNU 최적화 — HW 이식 가능
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:7008293
- **Type**: conference
- **Published**: 13-15 Oct.
- **Authors**: Wenjing Wang, Lixin Li, Huisheng Zhang
- **PDF**: https://ieeexplore.ieee.org/document/7008293
- **Abstract**: In this paper, a simplified partially parallel decoder architectural based on field programmable gate array (FPGA) devices for Digital Video Broadcasting-Satellite 2 low-density parity-check(DVB-S2-LDPC) codes has been presented. We introduce the current research status about decoder design for LDPC code and described the motivation of this paper in the first part. Then, we present the simulating results on parameter selection and architectural design. The primary contribution of this paper is summarized as follows: firstly, we proposed a novel and more efficient barrel shifter design. secondly, we optimized sub-modules architecture including: Bit Node Update, Check Node Update and combined and flexible data storage strategy so that this decoder can achieve both high data throughput and low resource-on-chip consumption.

## A non-linear LLR approximation for LDPC decoding over impulsive noise channels

- **Status**: ✅
- **Reason**: C: 임펄스(alpha-stable) 노이즈 채널용 비선형 LLR 근사 — LLR 계산 기법, NAND LLR 양자화에 참고 가능(애매하나 in)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7008248
- **Type**: conference
- **Published**: 13-15 Oct.
- **Authors**: Yi Hou, Rongke Liu, Ling Zhao
- **PDF**: https://ieeexplore.ieee.org/document/7008248
- **Abstract**: The performance of Low-Density Parity-Check codes over symmetric alpha-stable impulsive noise channels is considered in this paper. Due to the lack of closed-form expressions for the probability density functions of almost all the alpha-stable distributions, an efficient non-linear approximation method for channel log-likelihood ratio is presented to achieve high decoding performance covering the range of characteristic exponent from 1 to 2 and avoid the use of complicated numerical integrations. The simulations for both long and short codes show that the parameter selection of the proposed method is not sensitive to the noise level. Even fixed parameter setting for the proposed non-linear approximation can obtain a satisfying decoding performance.

## Matrix reordering techniques for memory conflict reduction for pipelined QC-LDPC decoder

- **Status**: ✅
- **Reason**: D: 파이프라인 QC-LDPC layered(TDMP) 디코더 메모리 충돌 감소 행렬 재배열 기법 — HW 이식 가능
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:7008301
- **Type**: conference
- **Published**: 13-15 Oct.
- **Authors**: Zhenzhi Wu, Dake Liu, Yanjun Zhang
- **PDF**: https://ieeexplore.ieee.org/document/7008301
- **Abstract**: Layered Decoding (LD) algorithm is widely applied in high throughput QC-LDPC decoders. Among all check node update algorithms in LD, Turbo-Decoding Message-Passing (TDMP) is adopted by many proposals. A-posteriori memory access conflict under pipelined TDMP decoder incurs serious throughput decline. In this paper, several matrix reordering techniques are introduced to reduce the conflict occurrences without incurring the performance loss, which includes Row Exchange method, element Sequence Reordering method, and a conflict detector with pipeline stall insertion. They are integrated in a joint recursive deep-first searching procedure. Test results show that the efficiency improvement reaches up to 60% compared to non-optimized scenarios for 802.11n and 802.16e standards.
