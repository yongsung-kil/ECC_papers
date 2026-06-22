# IEEE Xplore — 2014-10


## Unified turbo/LDPC code decoder architecture for deep-space communications

- **Status**: ✅
- **Reason**: turbo+LDPC 동일 알고리즘 기반 통합 HW 디코더(datapath/memory 공유, VLSI) — LDPC 디코더 HW 아키텍처로 이식 가능(D)
- **ID**: ieee:6978902
- **Type**: journal
- **Published**: October 20
- **Authors**: Carlo Condo, Guido Masera
- **PDF**: https://ieeexplore.ieee.org/document/6978902
- **Abstract**: Deep-space communications are characterized by extremely critical conditions; current standards foresee the usage of both turbo and low-density-parity-check (LDPC) codes to ensure recovery from received errors, but each of them displays consistent drawbacks. Code concatenation is widely used in all kinds of communication to boost the error correction capabilities of single codes; serial concatenation of turbo and LDPC codes has been recently proven effective enough for deep space communications, being able to overcome the shortcomings of both code types. This work extends the performance analysis of this scheme and proposes a novel hardware decoder architecture for concatenated turbo and LDPC codes based on the same decoding algorithm. This choice leads to a high degree of datapath and memory sharing; postlayout implementation results obtained with complementary metal-oxide semiconductor (CMOS) 90 nm technology show small area occupation (0.98 mm2) and very low power consumption (2.1 mW).

## Polar-LDPC Concatenated Coding for the AWGN Wiretap Channel

- **Status**: ❌
- **Reason**: Polar-LDPC 연접 wiretap 보안 코딩 — 비-LDPC 연접+보안, 떼어낼 바이너리 LDPC BP 기법 없음
- **ID**: ieee:6891165
- **Type**: journal
- **Published**: Oct. 2014
- **Authors**: Yingxian Zhang, Aijun Liu, Chao Gong +2
- **PDF**: https://ieeexplore.ieee.org/document/6891165
- **Abstract**: In this paper, a concatenated coding scheme based on polar codes and LDPC codes is proposed for the additive white Gaussian noise (AWGN) wiretap channel. We first analyze the bit error rate (BER) performance of the proposed coding scheme through the density evolution (DE). Then, the security gap that our coding scheme can achieve is investigated. Finally, to adapt to the dynamic environments, we present a transmission scheme using rate compatible Polar-LDPC codes. Numerical results suggest that the proposed coding scheme is more effective and flexible than other existing secure coding schemes.

## Large Girth Column-Weight Two and Three LDPC Codes

- **Status**: ✅
- **Reason**: girth-12 cycle code 및 binary QC-LDPC(column-weight 3) 신규 구성 — 바이너리 코드 설계(E)
- **ID**: ieee:6881655
- **Type**: journal
- **Published**: Oct. 2014
- **Authors**: Mohammad Gholami, Ghaffar Raeisi
- **PDF**: https://ieeexplore.ieee.org/document/6881655
- **Abstract**: In this paper, the concept of broken diagonal pair in the chess-like square board is used to define some well-structured block designs whose incidence matrices can be considered as the parity-check matrices of some high rate cycle codes with girth 12. Interestingly, the constructed regular cycle codes with row-weights  $t$,  $3\leq t\leq 20$,  $t\neq 7,15,16$, have the minimum lengths among the known regular girth-12 cycle codes. In addition, the proposed cycle codes can be easily extended to some high rate column weight-3 LDPC codes with girth 6. Simulation results show that the constructed non-binary cycle codes and binary QC LDPC codes have good performances over AWGN channel.

## Partition Optimization in LDPC-Coded OFDM Systems With PTS PAPR Reduction

- **Status**: ❌
- **Reason**: LDPC-OFDM PTS PAPR 저감용 파티션 최적화 — 무선 응용 특이적, NAND로 떼어낼 ECC/디코더 기법 없음
- **ID**: ieee:6734702
- **Type**: journal
- **Published**: Oct. 2014
- **Authors**: Li Li, Daiming Qu, Tao Jiang
- **PDF**: https://ieeexplore.ieee.org/document/6734702
- **Abstract**: A joint decoding scheme was proposed by Li and Qu to recover low-density parity-check (LDPC) codeword and partial transmit sequence (PTS) phase factors, for OFDM systems with a low peak-to-average power ratio (PAPR). However, the error-correcting performance of the joint decoding scheme heavily relies on how the OFDM subcarriers are partitioned into groups in the PTS scheme. With a pseudorandom partition, the joint decoding scheme provides satisfactory error-correcting performance only when the number of PTS groups is very small. In this paper, we formulate an optimization problem to improve the joint decoding performance by optimizing the partition. Furthermore, two greedy-based algorithms are proposed to solve the problem. Simulation results show that the joint decoding scheme with the proposed partition algorithms provides satisfactory error-correcting performance for a larger number of PTS groups than it does with the pseudorandom partition. With the improved performance, better PAPR performance can be supported.

## Efficient Decoder Architecture for Single Block-Row Quasi-Cyclic LDPC Codes

- **Status**: ✅
- **Reason**: QC-LDPC용 신규 디코더 아키텍처로 메모리 20.8% 절감, subblock-sharing 기법 — 이식 가능 HW(D)
- **ID**: ieee:6871329
- **Type**: journal
- **Published**: Oct. 2014
- **Authors**: Chuan Zhang, Zhongfeng Wang, Xiaohu You
- **PDF**: https://ieeexplore.ieee.org/document/6871329
- **Abstract**: Single block-row quasi-cyclic low-density parity-check codes have been proposed for high-speed applications recently. However, no existing work has systematically addressed the decoder design issue for such kind of codes. In this brief, an efficient decoder architecture for such kinds of codes is proposed by exploring the geometry properties of the check matrix. Compared with conventional approaches, the proposed method can achieve more than 20.8% of memory reduction. Additionally, the subblock-sharing technique and the suboptimal low-latency searching method are employed to further reduce the hardware complexity.

## High-Throughput Cognitive-Amplification Detector for LDPC Decoders

- **Status**: ✅
- **Reason**: LDPC 디코더의 min/sub-min 계산을 위한 새 HW 검출기(CAD)로 throughput/리소스 개선 — 이식 가능 HW 아키텍처(D)
- **ID**: ieee:6870670
- **Type**: journal
- **Published**: Oct. 2014
- **Authors**: Melvin Heng Li Lim, Wang Ling Goh
- **PDF**: https://ieeexplore.ieee.org/document/6870670
- **Abstract**: With the advent of technology over the recent years, the low-density parity-check (LDPC) codes, which were once seen as an impractical concept, are now poised to be the next big thing in the communication standards of today for their near-capacity performances. Nonetheless, the physical implementation of LDPC decoders is more often than not encumbered by the arithmetic of its decoding algorithm. Entangled by numerous computations of minima, LDPC decoders not only require considerable amount of resources to the implement cascaded pair-wise comparators, but also yield low decoding throughputs. In this paper, we propound a novel design for the computation of minimum and subminimum in LDPC decoding, known as the cognitive-amplification detector (CAD). By leveraging on the finite precision of fixed-point binary representation in actual hardware, our CAD proposition renders significant gains in decoding throughput and savings in resource consumption of up to 20% and 15%, respectively, not to mention negligible trade-offs in error-correcting capabilities.

## New Stopping Criterion for Fast Low-Density Parity-Check Decoders

- **Status**: ✅
- **Reason**: APP 증가를 이용한 새 T-tolerance 정지 기준으로 평균 반복수 감소 — 부호 비의존적 MP 디코더 개선(C)
- **ID**: ieee:6881612
- **Type**: journal
- **Published**: Oct. 2014
- **Authors**: Tian Xia, Hsiao-Chun Wu, Hong Jiang
- **PDF**: https://ieeexplore.ieee.org/document/6881612
- **Abstract**: Low-density parity-check (LDPC) codes are favorable in low bit-error-rate and high code-rate applications. However, the decoding complexity for LDPC codes is quite large, especially for nonbinary LDPC codes. In this paper, we propose a new  $T$-tolerance stopping criterion for LDPC decoders by exploiting the fact that the total a posteriori probability (APP) should increase across iterations when message passing (MP) algorithms are employed. Simulation results demonstrate that our proposed new  $T$-tolerance criterion can greatly reduce the average iteration number (complexity) while the decoding performance degradation is controlled within 0.1 dB in the low bit-energy-to-noise-spectral-density ratio  $(E_{b}/N_{0})$ scenarios.

## Optimized LDPC differential-encoded 16QAM scheme for high-speed transmission systems

- **Status**: ❌
- **Reason**: DE-16QAM 연접용 외부 LDPC degree distribution 최적화 — 변조 응용 특이적, 떼어낼 ECC 기법 없음
- **ID**: ieee:6961045
- **Type**: journal
- **Published**: Oct. 2014
- **Authors**: Zhanji Wu, Xiang Gao, Zhiyu Xiao
- **PDF**: https://ieeexplore.ieee.org/document/6961045
- **Abstract**: The 16-ary quadrature amplitude modulation (16QAM) is a high spectral efficient scheme for high-speed transmission systems. To remove the phase ambiguity in the coherent detection system, differential-encoded 16QAM (DE-16QAM) is usually used, however, it will cause performance degradation about 3 dB as compared to the conventional 16QAM. To overcome the performance loss, a serial concatenated system with outer low density parity check (LDPC) codes and inner DE-16QAM is proposed. At the receiver, joint iterative differential demodulation and decoding (ID) is carried out to approach the maximum likelihood performance. Moreover, a genetic evolution algorithm based on the extrinsic information transfer chart is proposed to optimize the degree distribution of the outer LDPC codes. Both theoretical analyses and simulation results indicate that this algorithm not only compensates the performance loss, but also obtains a significant performance gain, which is up to 1 dB as compared to the conventional non-DE-16QAM.

## Quasi-Cyclic LDPC Codes Based on Pre-Lifted Protographs

- **Status**: ✅
- **Reason**: 프리-리프팅 프로토그래프 기반 QC-LDPC 2단계 리프팅으로 minimum distance·girth 개선 — 바이너리 코드 설계 기법(E)
- **ID**: ieee:6863699
- **Type**: journal
- **Published**: Oct. 2014
- **Authors**: David G. M. Mitchell, Roxana Smarandache, Daniel J. Costello
- **PDF**: https://ieeexplore.ieee.org/document/6863699
- **Abstract**: Quasi-cyclic low-density parity-check (QC-LDPC) codes based on protographs are of great interest to code designers because analysis and implementation are facilitated by the protograph structure and the use of circulant permutation matrices for protograph lifting. However, these restrictions impose undesirable fixed upper limits on important code parameters, such as minimum distance and girth. In this paper, we consider an approach to constructing QC-LDPC codes that uses a two-step lifting procedure based on a protograph, and, by following this method instead of the usual one-step procedure, we obtain improved minimum distance and girth properties. We also present two new design rules for constructing good QC-LDPC codes using this two-step lifting procedure, and in each case, we obtain a significant increase in minimum distance and achieve a certain guaranteed girth compared with one-step circulant-based liftings. The expected performance improvement is verified by simulation results.

## Utilization of LDPC Code and Optical Hard-Limiter in OCDMA Communication Systems

- **Status**: ❌
- **Reason**: OCDMA에 표준 LDPC를 오류정정으로 단순 사용+optical hard-limiter — 새 디코더/구성 기여 없음, 응용 특이적
- **ID**: ieee:6842627
- **Type**: journal
- **Published**: Oct. 2014
- **Authors**: Maw-Yang Liu, Yi-Kai Hsu, Joe-Air Jiang
- **PDF**: https://ieeexplore.ieee.org/document/6842627
- **Abstract**: In this paper, we investigate the utilization of low-density parity-check (LDPC) code and optical hard-limiter in OCDMA communication systems. Since the multiple access interference will impose significant penalty on system performance, using optical hard-limiter is an effective countermeasure to relieve this adverse impact. To further increase the aggregate capacity, the LDPC code is employed as an error correction mechanism that can allow more simultaneous users accommodated in the network. As the aggregate capacity and system complexity are the main considerations in practical system design, both of which are mutually trade off. Utilization of LDPC code and optical hard-limiter can effectively reduce the system complexity to reach the maximum aggregate capacity. Our proposed scheme can accommodate large number of users in the network simultaneously and support the traffic asynchronously with each user. Furthermore, the aggregate capacity can reach above 100 Gbps; therefore, it is the preferable way as the platform for fiber distribution network in some applications.

## Construction of structured q-ary LDPC codes over small fields using sliding-window method

- **Status**: ❌
- **Reason**: q-ary(비이진 GF(q)) LDPC 구성 및 QSPA 디코딩 — 비이진 LDPC 제외
- **ID**: ieee:6955957
- **Type**: journal
- **Published**: Oct. 2014
- **Authors**: Haiqiang Chen, Yunyi Liu, Tuanfa Qin +2
- **PDF**: https://ieeexplore.ieee.org/document/6955957
- **Abstract**: In this paper, we consider the construction of cyclic and quasi-cyclic structured (/-ary low-density parity-check (LDPC) codes over a designated small field. The construction is performed with a pre-defined sliding-window, which actually executes the regular mapping from original field to the targeted field under certain parameters. Compared to the original codes, the new constructed codes can provide better flexibility in choice of code rate, code length and size of field. The constructed codes over small fields with code length from tenths to hundreds perform well with (/-ary sum-product decoding algorithm (QSPA) over the additive white Gaussian noise channel and are comparable to the improved sphere-packing bound. These codes may found applications in wireless sensor networks (WSN), where the delay and energy are extremely constrained.

## Constructing Linear Encoders With Good Spectra

- **Status**: ❌
- **Reason**: 무손실 JSCC용 선형 인코더 스펙트럼 구성(Gabidulin+LDGM) — JSCC/소스코딩 영역, 떼어낼 채널 ECC 디코더 기법 없음
- **ID**: ieee:6862007
- **Type**: journal
- **Published**: Oct. 2014
- **Authors**: Shengtian Yang, Thomas Honold, Yan Chen +2
- **PDF**: https://ieeexplore.ieee.org/document/6862007
- **Abstract**: Linear encoders with good joint spectra are suitable candidates for optimal lossless joint source-channel coding (JSCC), where the joint spectrum is a variant of the input–output complete weight distribution and is considered good if it is close to the average joint spectrum of all linear encoders (of the same coding rate). In spite of their existence, little is known on how to construct such encoders in practice. This paper is devoted to their construction. In particular, two families of linear encoders are presented and proved to have good joint spectra. The first family is derived from Gabidulin codes, a class of maximum-rank-distance codes. The second family is constructed using a serial concatenation of an encoder of a low-density parity-check code (as outer encoder) with a low-density generator matrix encoder (as inner encoder). In addition, criteria for good linear encoders are defined for three coding applications: 1) lossless source coding; 2) channel coding; and 3) lossless JSCC. In the framework of the code-spectrum approach, these three scenarios correspond to the problems of constructing linear encoders with good kernel spectra, good image spectra, and good joint spectra, respectively. Good joint spectra imply both good kernel spectra and good image spectra, and for every linear encoder having a good kernel (respectively, image) spectrum, it is proved that there exists a linear encoder not only with the same kernel (respectively, image) but also with a good joint spectrum. Thus, a good joint spectrum is the most important feature of a linear encoder.

## Coding and Detection for Channels With Written-In Errors and Inter-Symbol Interference

- **Status**: ❌
- **Reason**: 비트패턴드 매체 written-in error+ISI용 marker code+BCJR 검출 — LDPC 아니고 동기/검출 기법, NAND LDPC 이식 대상 아님
- **ID**: ieee:6825879
- **Type**: journal
- **Published**: Oct. 2014
- **Authors**: Guojun Han, Yong Liang Guan, Kui Cai +2
- **PDF**: https://ieeexplore.ieee.org/document/6825879
- **Abstract**: Written-in errors (WIEs), which include written-in substitutions, insertions, and deletions, as well as 2-D inter-symbol interference (2-D-ISI), form one of the major challenges for the new emerging bit-patterned media recording technology. Coding and detection scheme with performance/complexity tradeoffs is expected to address such a challenge. In this paper, a new channel model with WIEs and ISI (WIE-ISI) is presented, and the embedded marker code scheme (EMCS) with Bahl–Cocke–Jelinek–Raviv (BCJR) detector is employed to perform channel detection. By investigating the effect of ISI on the WIE-ISI channel considering BCJR detector, a virtual written-in substitution probability is introduced and a new synchronization algorithm with written-in substitution detection (SA-WSD) is developed. The EMCS employing the proposed SA-WSD demonstrates better error correction performance than that of the original SA. Furthermore, the SA-WSD is found to be robust to small estimation errors in the written-in substitution probability.

## Noisy Gradient Descent Bit-Flip Decoding for LDPC Codes

- **Status**: ✅
- **Reason**: Noisy GDBF 비트플립 디코더 — 바이너리 LDPC AWGN, 완전 병렬 신규 디코더+HW(C/D)
- **ID**: ieee:6894606
- **Type**: journal
- **Published**: Oct. 2014
- **Authors**: Gopalakrishnan Sundararajan, Chris Winstead, Emmanuel Boutillon
- **PDF**: https://ieeexplore.ieee.org/document/6894606
- **Abstract**: A modified Gradient Descent Bit Flipping (GDBF) algorithm is proposed for decoding Low Density Parity Check (LDPC) codes on the binary-input additive white Gaussian noise channel. The new algorithm, called Noisy GDBF (NGDBF), introduces a random perturbation into each symbol metric at each iteration. The noise perturbation allows the algorithm to escape from undesirable local maxima, resulting in improved performance. A combination of heuristic improvements to the algorithm are proposed and evaluated. When the proposed heuristics are applied, NGDBF performs better than any previously reported GDBF variant, and comes within 0.5 dB of the belief propagation algorithm for several tested codes. Unlike other previous GDBF algorithms that provide an escape from local maxima, the proposed algorithm uses only local, fully parallelizable operations and does not require computing a global objective function or a sort over symbol metrics, making it highly efficient in comparison. The proposed NGDBF algorithm requires channel state information which must be obtained from a signal to noise ratio (SNR) estimator. Architectural details are presented for implementing the NGDBF algorithm. Complexity analysis and optimizations are also discussed.

## Iterative Detection-Decoding of Interleaved Hermitian Codes for High Density Storage Devices

- **Status**: ❌
- **Reason**: Interleaved Hermitian(AG) 코드 ABP+KV 리스트 디코딩 — 비-LDPC 부호, RS 대체용 AG 코드 전용 기법
- **ID**: ieee:6895251
- **Type**: journal
- **Published**: Oct. 2014
- **Authors**: Li Chen, Martin Johnston, Gui Yun Tian
- **PDF**: https://ieeexplore.ieee.org/document/6895251
- **Abstract**: Traditionally, Reed-Solomon (RS) codes have been employed in magnetic data storage devices due to their effectiveness in correcting random errors and burst errors caused by thermal asperities and inter-symbol interference (ISI). However, as storage densities increase the effect of ISI becomes more severe and much longer RS codes are needed, but this requires significantly increasing the size of the finite field. A possible replacement for RS codes are the one-point Hermitian codes, which are a class of algebraic-geometric (AG) code that have larger block sizes and minimum Hamming distances over the same finite field. In this paper, we present a novel iterative soft detection-decoding algorithm for interleaved Hermitian codes. The soft decoding employs a joint adaptive belief propagation (ABP) algorithm and Koetter-Vardy (KV) list decoding algorithm. It is combined with a maximum a posteriori (MAP) partial response (PR) equalizer and likelihoods from the output of the KV or the ABP algorithm are fed back to the equalizer. The proposed scheme's iterative detection-decoding behavior will be analyzed by utilizing the Extrinsic Information Transfer (ExIT) chart. Our simulation results demonstrate the performance gains achieved by iterations and Hermitian codes' performance advantage over RS codes.

## Codes on Graphs: Fundamentals

- **Status**: ❌
- **Reason**: 그래프 코드 실현의 순수 이론(group duality, observability) — 디코더/HW/구성으로 안 이어지는 이론 bound
- **ID**: ieee:6873277
- **Type**: journal
- **Published**: Oct. 2014
- **Authors**: G. David Forney
- **PDF**: https://ieeexplore.ieee.org/document/6873277
- **Abstract**: This paper develops a fundamental theory of realizations of linear and group codes on general graphs using elementary group theory, including basic group duality theory. Principal new and extended results include: normal realization duality; analysis of systems-theoretic properties of fragments of realizations and their connections; minimal  \(\Leftrightarrow \)  trim and proper theorem for cycle-free codes; results showing that all constraint codes except interface nodes may be assumed to be trim and proper, and that the interesting part of a cyclic realization is its 2-core; notions of observability and controllability for fragments, and related tests; and relations between state-trimness and controllability, and dual state-trimness and observability.

## A Queueing Characterization of Information Transmission Over Block-Fading Rayleigh Channels in the Low-SNR Regime

- **Status**: ❌
- **Reason**: 블록페이딩 채널 큐잉 이론 분석 — LDPC/디코더/HW 무관 순수 통신 이론
- **ID**: ieee:6746641
- **Type**: journal
- **Published**: Oct. 2014
- **Authors**: Yunquan Dong, Pingyi Fan
- **PDF**: https://ieeexplore.ieee.org/document/6746641
- **Abstract**: Unlike the additive white Gaussian noise (AWGN) channel, fading channels suffer from random channel gains, in addition to the additive Gaussian noise. As a result, the instantaneous channel capacity varies randomly along time, which makes it insufficient to characterize the transmission capability of a fading channel using data rate only. In this paper, the transmission capability of a buffer-aided Rayleigh block-fading channel is examined by a constant-rate input data stream and is reflected by several parameters, such as the average queue length, stationary queue length distribution, packet delay, and overflow probability. Both infinite-buffer and finite-buffer models are considered. Taking advantage of the memoryless property of the service provided by the channel in each block in the low-SNR regime, the information transmission over the channel is formulated as a discrete-time discrete-state  $D/G/\hbox{1}$ queueing problem. The obtained results show that block-fading channels are unable to support a data rate close to their ergodic capacity, no matter how long the buffer is, even when seen from the application layer. For the finite-buffer model, the overflow probability is derived with explicit expression and is shown to decrease exponentially when buffer size is increased, even when the buffer size is very small.

## Performance of Repeat-Accumulate Codes (RAC) for decode-and-forward wireless relay channel

- **Status**: ❌
- **Reason**: Repeat-Accumulate codes for wireless relay; non-LDPC, no portable LDPC BP technique
- **ID**: ieee:7007928
- **Type**: conference
- **Published**: 7-8 Oct. 2
- **Authors**: Daryus Chandra, Adhi Susanto, Sri Suning Kusumawardani
- **PDF**: https://ieeexplore.ieee.org/document/7007928
- **Abstract**: Repeat-Accumulate Codes (RAC) are one of alternative choice code besides turbo codes and low-density parity-check (LDPC) codes. This paper presented decode-and-forward protocol for wireless relay channel by utilizing repeat-accumulate codes as the coding scheme in the relay. The main advantages of the RAC over another code that makes the RAC is more considered for this research are the complexity of encoding is linear in the code length, have a simpler design, and easier to combine with modulator or detector. Simplicity is the main factor for using RAC in this research because in the multihop wireless communication concept, the information processing that occurs in every node or in every relay should not be complicated. In this paper, RAC is employed in wireless relay channel for the LOS model and urban model. The result shows that in the LOS model, RAC only show BER improvement when the relay position is exactly in the mid between information source (S) and destination (D). In urban channel model, the BER improvement can be observed, whether the relay is positioned ¼, ½ or ¾ between the information source (S) and the destination (D).

## Ultra-low complexity early termination scheme for layered LDPC decoding

- **Status**: ✅
- **Reason**: Ultra-low complexity early termination for layered LDPC decoding; portable decoder/HW technique (C/D)
- **ID**: ieee:7031199
- **Type**: conference
- **Published**: 7-10 Oct. 
- **Authors**: Yuan-Syun Wu, Cheng-Hung Lin, Shu-Yen Lin
- **PDF**: https://ieeexplore.ieee.org/document/7031199
- **Abstract**: Energy consumption is a major issue for LDPC decoding. To save LDPC iterative process energy, early terminations are commonly used. Traditional parity check equation is used but has a growing complexity as the block size increases. This requires a large overhead in term of area. This paper proposes an ultra-low complexity early termination (ET) scheme with a small loss of bit error rate performance based on the layer stopping (LS) criterion. The proposed ET scheme is performed by checking the number of convergent layers stopped by the LS criterion with a preset threshold. Compared with other ET schemes, the proposed ET scheme has a negligible hardware overhead and an acceptable bit error rate performance.

## Thermal-aware kernel mapping for three-dimensional multi-mode channel decoding

- **Status**: ❌
- **Reason**: Thermal-aware 3D kernel mapping for multi-mode channel decoder; physical placement/thermal, no LDPC algorithm or code-design contribution
- **ID**: ieee:7031240
- **Type**: conference
- **Published**: 7-10 Oct. 
- **Authors**: Shu-Yen Lin, Cheng-Hung Lin, Ho-Yun Su
- **PDF**: https://ieeexplore.ieee.org/document/7031240
- **Abstract**: In this work, three thermal-aware kernel mappings are proposed for a three-dimensional multi-mode channel decoding architecture. The proposed kernel mappings can reduce the peak temperature and support different thermal and latency constraints. In our experiments, we show the peak temperature can be reduced from 16.2°C∼33.8°C. Besides, we also demonstrate that different mapping is chosen under different thermal and latency constraints.

## Adaptive Redundant Data Allocation Using Unused Blocks for Improving Access Efficiency in Dependable Storage Systems

- **Status**: ❌
- **Reason**: 스토리지 데이터 할당 기법, erasure 코딩 응용일 뿐 LDPC ECC 이식 기법 없음
- **ID**: ieee:6983417
- **Type**: conference
- **Published**: 6-9 Oct. 2
- **Authors**: Ta Hong Viet
- **PDF**: https://ieeexplore.ieee.org/document/6983417
- **Abstract**: This paper has presented a data allocation method with erasure correction coding to design dependable storage system. This adaptive data allocation can reduce the number of access to unavailable storage elements, moreover it also improve the reliability of the system. We proposed variable information word length method which can reduce the number of blocking accesses, and two ideas are presented to reduce the allocation map size and update cost.

## Adaptive Erasure Correction Coding for Energy Efficient Dependable Storage Systems

- **Status**: ❌
- **Reason**: Reed-Solomon 기반 스토리지 데이터 할당, 비-LDPC이고 ECC 디코더 기법 없음
- **ID**: ieee:7000146
- **Type**: conference
- **Published**: 6-9 Oct. 2
- **Authors**: Kousuke Ota, Viet Ta Hong, Haruhiko Kaneko
- **PDF**: https://ieeexplore.ieee.org/document/7000146
- **Abstract**: Erasure correction coding is an effective technique to improve the dependability of distributed storage systems and disk arrays, in which codeword symbols are distributed over multiple storage elements (SEs), e.g., storage nodes and disk drives. One of the major drawbacks of such storage systems is increased data update cost, that is, data update in one SE induces simultaneous multiple update accesses to a specified set of SEs to keep consistency of codewords. The SEs sometimes have high access cost due to, for example, large delay caused by access collision with other workloads, temporary network cutoff, and malicious attack, and high energy consumption caused by resume operations from power suspension mode. This paper proposes an adaptive coding and data allocation method which can reduce the number of update accesses to SEs having high access cost. The proposed method is based on adaptive allocation of codeword symbols of Reed-Solomon code with conditional overwrites of check symbols, and also on background relocation of codeword symbols. Preliminary simulation results show that the proposed method provides sufficiently low data loss probability with reduced energy consumption compared to RAID-1 and -6.

## Optimal Choice of Transmission Parameters for LDPC-Coded CPM

- **Status**: ❌
- **Reason**: LDPC-coded CPM 전송 파라미터 최적화 — 무선/전술 응용 파라미터 선택, 표준 LDPC 사용, 떼어낼 신규 ECC 기법 없음.
- **ID**: ieee:6956787
- **Type**: conference
- **Published**: 6-8 Oct. 2
- **Authors**: Mahsa Foruhandeh, Murat Uysal, Ibrahim Altunbas +2
- **PDF**: https://ieeexplore.ieee.org/document/6956787
- **Abstract**: Continuous phase modulation (CPM) has attractive features such as spectral efficiency and constant envelope making it attractive for tactical waveforms. Serial concatenation of CPM with Low Density Parity Check Codes (LDPCs) provides a superior performance due to coding gains of this powerful code family. The choice of proper combination of LDPC and CPM is crucial to satisfy the targeted tactical waveform requirements of spectral efficiency, power efficiency and receiver complexity. In this paper, we address the problem of selecting the optimal transmission parameters in an LDPC-coded CPM system to satisfy a given spectral efficiency subject to a constraint on the demodulator complexity. Specifically, we consider modulation index, alphabet size, pulse shape duration, and code rate as transmission parameters. Utilizing a systematic search procedure, we identify the proper transmission parameters to achieve a targeted spectral efficiency and error rate. Finally, we present a Monte Carlo simulation study to demonstrate the performance of selected LDPC-CPM schemes with and without jamming.

## Faster-than-Nyquist Signaling and Optimized Signal Constellation for High Spectral Efficiency Communications in Nonlinear Satellite Systems

- **Status**: ❌
- **Reason**: FTN 신호 + Turbo Volterra 수신기(위성) — 비-LDPC, LDPC BP 이식 기법 없음.
- **ID**: ieee:6956863
- **Type**: conference
- **Published**: 6-8 Oct. 2
- **Authors**: Bassel F. Beidas, Rohit Iyer Seshadri, Mustafa Eroz +1
- **PDF**: https://ieeexplore.ieee.org/document/6956863
- **Abstract**: We here consider utilizing faster-than-Nyquist (FTN) signaling to increase spectral efficiency in combination with using tight frequency roll-off, optimized signal constellations that have better energy efficiency, and allowing the satellite transponder to operate near its saturation. FTN provides a degree of freedom that allows for increasing the spectral efficiency without the need for introducing additional rings in the signal constellation, which is helpful in the presence of nonlinear transponders. Also, FTN allows for increasing the symbol rate without being adversely affected by the input multiplexing and output multiplexing (IMUX/OMUX) filters. This is because FTN does not alter the signal spectral shape. However, these advantages are gained at the expense of introducing distortion that needs to be compensated successfully. We then utilize an advanced Turbo Volterra receiver that compensates for FTN-induced distortion and nonlinear impairments. Through extensive simulations, we demonstrate substantial performance gains over a wide range of spectral efficiencies in nonlinear satellite systems with adjacent carriers.

## Design and Implementation of Seamless Rate Adaptive Decoder

- **Status**: ✅
- **Reason**: Seamless rate adaptive 디코더 ASIC 구현(부분병렬 아키텍처, fixed-point, Jacobian 근사 병렬화) — 카테고리 D HW 기법 이식 가능성, 애매하여 살림.
- **ID**: ieee:6956785
- **Type**: conference
- **Published**: 6-8 Oct. 2
- **Authors**: Lu Qiu, Min Wang, Jun Wu +2
- **PDF**: https://ieeexplore.ieee.org/document/6956785
- **Abstract**: Seamless rate adaptation (SRA) is one of the promising rate adaptive schemes for wireless communication system. However, the high complexity of decoding hinders its application. We propose an optimized Application-specific integrated circuit (ASIC) design and implementation for SRA decoder in this paper. In order to balance speed and resource consumption, a partial parallel architecture is used in SRA decoder, which consists of 8x8 parallel computation unit, each computation unit calculates decoding metrics in pipelining way. In order to further improve the throughput of the decoder, a parallel structure for multivariable Jacobian logarithm approximation is designed. We also illustrate how fixed-point SRA decoder is designed. Numerical simulation shows the decoding performance of our design has neglect able performance loss. The optimized decoder ASIC can achieve 84Mbps throughput running at 300Mhz, occupying an area of 5 5mm2 and consuming power 4.21W. Compared to our previous design in FPGA, the throughput of this ASIC increases about 17:5 times.

## How to achieve the capacity of asymmetric channels

- **Status**: ❌
- **Reason**: 비대칭채널 용량달성 부호화 이론(polar/SC, 소스-채널 결합) — 순수 이론, 떼어낼 LDPC ECC 기법 없음
- **ID**: ieee:7028535
- **Type**: conference
- **Published**: 30 Sept.-3
- **Authors**: Marco Mondelli, Rüdiger Urbanke, S. Hamed Hassani
- **PDF**: https://ieeexplore.ieee.org/document/7028535
- **Abstract**: We describe coding techniques that achieve the capacity of a discrete memoryless asymmetric channel. To do so, we discuss how recent advances in coding for symmetric channels yield more efficient solutions also for the asymmetric case. In more detail, we consider three basic approaches. The first one is Gallager's scheme that concatenates a linear code with a non-linear mapper, in order to bias the input distribution. We explicitly show that both polar codes and spatially coupled codes can be employed in this scenario. Further, we derive a scaling law between the gap to capacity, the cardinality of channel input and output alphabets, and the required size of the mapper. The second one is an integrated approach in which the coding scheme is used both for source coding, in order to create codewords with the capacity-achieving distribution, and for channel coding, in order to provide error protection. Such a technique has been recently introduced by Honda and Yamamoto in the context of polar codes, and we show how to apply it also to the design of sparse graph codes. The third approach is based on an idea due to Böcherer and Mathar and separates completely the two tasks of source coding and channel coding by “chaining” together several codewords. We prove that we can combine any suitable source code with any suitable channel code in order to provide optimal schemes for asymmetric channels. In particular, polar codes and spatially coupled codes fulfill the required conditions.

## Uniformly reweighted APP decoder for memory efficient decoding of LDPC Codes

- **Status**: ✅
- **Reason**: reweighted APP 디코더 + 메모리 효율 구현 — 이식 가능한 BP 변형 디코더(C)
- **ID**: ieee:7028595
- **Type**: conference
- **Published**: 30 Sept.-3
- **Authors**: Velimir Ilić, Elsa Dupraz, David Declercq +1
- **PDF**: https://ieeexplore.ieee.org/document/7028595
- **Abstract**: In this paper we propose a uniformly reweighted a posteriori probability (APP) decoder. The APP decoder is well-known to be suboptimal compared to the BP decoder. Here, we derive the APP decoder as an algorithm of approximate Bayesian inference on the LDPC code graph and introduce a correction parameter to overcome the suboptimaly of the APP decoder. We optimize numerically the correction parameter and show that it improves the BER performance of the APP decoder compared to its non-corrected version. In addition, the original APP decoder requires memory that is linear in the number of edges in the code graph. Here, we propose a memory efficient implementation of the algorithm that requires memory that is linear only in the codeword length.

## The capacity of non-identical adaptive group testing

- **Status**: ❌
- **Reason**: 그룹테스트/스펙트럼 할당 알고리즘 — LDPC ECC와 무관
- **ID**: ieee:7028442
- **Type**: conference
- **Published**: 30 Sept.-3
- **Authors**: Tom Kealy, Oliver Johnson, Robert Piechocki
- **PDF**: https://ieeexplore.ieee.org/document/7028442
- **Abstract**: We consider the group testing problem, in the case where the items are defective independently but with non-constant probability. We introduce and analyse an algorithm to solve this problem by grouping items together appropriately. We give conditions under which the algorithm performs essentially optimally in the sense of information-theoretic capacity. We use concentration of measure results to bound the probability that this algorithm requires many more tests than the expected number. This has applications to the allocation of spectrum to cognitive radios, in the case where a database gives prior information that a particular band will be occupied.

## Information integrity in lossy source coding with side information

- **Status**: ❌
- **Reason**: Wyner-Ziv 손실 소스코딩의 정보무결성 — 채널 ECC 아님(소스 코딩)
- **ID**: ieee:7028601
- **Type**: conference
- **Published**: 30 Sept.-3
- **Authors**: Eric Graves, Tan F. Wong
- **PDF**: https://ieeexplore.ieee.org/document/7028601
- **Abstract**: In this paper we investigate how to achieve information integrity in two common models of source coding with side information. We first look at the classical Wyner-Ziv problem, where the side information is available only to the decoder, with an adversary whom may arbitrarily change the “bin” index sent to the decoder. Interestingly, it is easy to show that standard Wyner-Ziv coding suffices to guarantee no adversary attack strategy may achieve arbitrarily small probability of fooling the decoder if the side information is correlated with the source. Subsequently, we consider the case where the side information is available also at the encoder, and hence joint source encoding can be performed. Here we show the result of Wyner-Ziv problem also extends to joint encoding without needing the side information to be correlated with the source. Moreover, no loss in the optimal compression rate is incurred in order to guarantee information integrity in either case.

## LP-decodable multipermutation codes

- **Status**: ❌
- **Reason**: 멀티퍼뮤테이션 부호의 LP 디코딩 — LDPC가 아닌 순열부호, 이식 대상 아님
- **ID**: ieee:7028540
- **Type**: conference
- **Published**: 30 Sept.-3
- **Authors**: Xishuo Liu, Stark C. Draper
- **PDF**: https://ieeexplore.ieee.org/document/7028540
- **Abstract**: In this paper, we introduce a new way of constructing and decoding multipermutation codes. Multipermutations are permutations of a multiset that may consist of duplicate entries. We first introduce a new class of matrices called multipermutation matrices. We characterize the convex hull of multipermutation matrices. Based on this characterization, we propose a new class of codes that we term LP-decodable multipermutation codes. Then, we derive two LP decoding algorithms. We first formulate an LP decoding problem for memoryless channels. We then derive an LP algorithm that minimizes the Chebyshev distance. Finally, we show a numerical example of our algorithm.

## Blind detection approach for LDPC, convolutional, and turbo codes in non-noisy environment

- **Status**: ❌
- **Reason**: LDPC/convolutional/turbo 부호 파라미터 블라인드 추정(Gauss-Jordan); 디코딩 ECC 기법 아닌 인식 문제
- **ID**: ieee:6997525
- **Type**: conference
- **Published**: 29-31 Oct.
- **Authors**: Ahmed Refaey, Raheleh Niati, Xianbin Wang +1
- **PDF**: https://ieeexplore.ieee.org/document/6997525
- **Abstract**: In a non-cooperative context such as military or spectrum surveillance application, a passive adversary has to solve the problem of estimating the transmitter parameters. In addition, wireless systems cause signaling overhead since their transmitter must inform the receiver about the chosen bit allocation table or the Forward Error Correction (FEC) scheme. In this work, a perception of a smart receiver able to blindly estimate a specific transmission context based on an intercepted stream is proposed. In particular, a new technique addressing the blind recognition of low-density parity-check (LDPC), convolutional, and turbo codes' encoding parameters at the receiver is introduced. The proposed blind detection for the FEC code technique considers a new iterative method based on Gauss-Jordan elimination through a pivoting algorithm devoted to the blind estimation of these codes encoding parameters in a non-noisy context.

## Parity modifications and stopping sets in high-rate codes for physical-layer security

- **Status**: ❌
- **Reason**: BEC wiretap 물리계층 보안용 stopping-set 천공 코드; 보안 전용 기법으로 NAND ECC에 떼어낼 부분 없음
- **ID**: ieee:6997475
- **Type**: conference
- **Published**: 29-31 Oct.
- **Authors**: Willie K. Harrison, Parker Boyce
- **PDF**: https://ieeexplore.ieee.org/document/6997475
- **Abstract**: In this paper, we present two variations on a linear physical-layer security code for the binary erasure wiretap channel, and examine their performance using small blocklength LDPC codes at rates above the secrecy capacity. We consider the maximum-likelihood attack, along with a message-passing attack, and show how the proposed codes enhance security in each case. Unique security metrics are employed for each attack algorithm as necessary to showcase the security enhancements of the new codes, which are built on the notion of random stopping-set-conscious puncturing of encoded bits followed by the addition of sets of edges in the Tanner graph corresponding to the parity-check matrix. The new codes are shown to provide enhanced security without decreasing the coding rate.

## Uniform distributed source coding for the multiple access wiretap channel

- **Status**: ❌
- **Reason**: 다중접속 wiretap 분산 소스코딩 보안 코딩; ECC 채널코딩 아님, 떼어낼 LDPC 기법 없음
- **ID**: ieee:6997477
- **Type**: conference
- **Published**: 29-31 Oct.
- **Authors**: Rémi A. Chou, Matthieu R. Bloch
- **PDF**: https://ieeexplore.ieee.org/document/6997477
- **Abstract**: We study the transmission of public and secret messages over the l-input multiple-access wiretap channel with deterministic encoders. Specifically, we assume that no additional source of randomness is available at the encoders and that public messages may be non-uniform and correlated. We develop a coding scheme that achieves information-theoretic security by combining existing constructions for wiretap codes with a distributed source code with nearly independent and nearly uniform encoder outputs.

## Signal alignment for secure underwater coordinated multipoint transmissions

- **Status**: ❌
- **Reason**: 수중음향 CoMP 보안 신호정렬; LDPC 무관, 통신 응용 특이적
- **ID**: ieee:6997480
- **Type**: conference
- **Published**: 29-31 Oct.
- **Authors**: Chaofeng Wang, Zhaohui Wang, Saeid Nooshabadi
- **PDF**: https://ieeexplore.ieee.org/document/6997480
- **Abstract**: Although considerable advances in underwater acoustic (UWA) communications and networking have been made in the last decade, research on the secure UWA communications and networking is limited. In this work, we consider the underwater distributed antenna systems (DAS) consisting of geographically distributed antenna elements (DAEs) that are connected via fibers or high-speed radio links, and address the security issue in the coordinated multipoint (CoMP) transmission of DAEs in the presence of an eavesdropper. The information message from DAS to a legitimate user is partitioned into multiple blocks, and each block is assigned to one DAE for transmission. Exploiting the low sound speed in water, the active DAE set and the corresponding transmission schedule, including the transmission starting time and the transmission power of each active DAE, are optimized with an aim of aligning the transmission blocks at the eavesdropper while keeping the blocks well-separated at the legitimate user. A practical design tailored to the orthogonal frequency-division multiplexing (OFDM) modulation is developed. Simulation results are presented to validate the performance of proposed schemes.

## LDPC decoder for WiMAX on NOC based multiprocessor platform

- **Status**: ✅
- **Reason**: WiMAX binary LDPC decoder on NoC multiprocessor with layered decoding + parallelism/data-exchange strategy; portable HW/parallel architecture (D)
- **ID**: ieee:7021351
- **Type**: conference
- **Published**: 28-31 Oct.
- **Authors**: Lingyun Zeng, Tengyue Yuan, Jun Han +1
- **PDF**: https://ieeexplore.ieee.org/document/7021351
- **Abstract**: Low density parity check (LDPC) code is an error correct code that can achieve performance close to Shannon limit and it is widely adopted in communication systems such as WiMAX and Wi-Fi. This paper presents a design of a flexible LDPC decoder for WiMAX based on the NoC platform. The implementation adopts layered decoding algorithm and exploits high parallelism that lies in the algorithm. Considering large quantity of data exchange between cores, we use stepped data exchange strategy and master-slave structure to reduce communication cost. The Cycle accurate simulation results show high speed-up and scalability of code rate of 5/6 with different code length in WiMAX in 4/8/16 processor systems.

## An new approach to reliable FSRs lDesign

- **Status**: ❌
- **Reason**: FSR 트랜지언트 결함 정정(duplication+parity), LDPC 무관 — 신뢰성 회로 설계, ECC 부호 기법 아님
- **ID**: ieee:7004730
- **Type**: conference
- **Published**: 27-28 Oct.
- **Authors**: Ming Liu, Elena Dubrova
- **PDF**: https://ieeexplore.ieee.org/document/7004730
- **Abstract**: Since the invention of integrated circuits in 1950s, the great budget of reliability of semiconductors have prompted the 60 years of glory of electrical industry. However, as the technology shrinks in recent years, the continuing rising of circuit density and the reduction of device sizes cause a lot of new constrains and problems, such as high power consumption and leakage currents in nano-meter designs. One of the serious consequences of these changes is the reduction of circuit reliability. In this paper, we introduce a new method for correcting transient faults in Feedback Shift Registers (FSRs) based on duplication and parity checking. The presented method is more reliable than Triple Model Redundancy (TMR) for large FSRs, while the area overhead of the two approaches is comparable. The presented approach might be important for applications using large FSRs, e.g. cryptography.

## A construction of LDPC convolutional codes with close distance bounds

- **Status**: ✅
- **Reason**: LDPC convolutional code 신규 구성, 4-cycle free 설계로 BP 디코딩 효율화 — 이식 가능 코드설계(E)
- **ID**: ieee:6979809
- **Type**: conference
- **Published**: 26-29 Oct.
- **Authors**: Tien-Hui Chen, Kuan-Chen Chen, Mao-Chao Lin
- **PDF**: https://ieeexplore.ieee.org/document/6979809
- **Abstract**: A trellis code constructed by concatenating a delay processor and a signal mapper to a convolutional code with a short constraint length can be regarded as a convolutional code with a large constraint length. We can obtain a close upper bound and a close lower bound for such a code. In this paper, we use this code structure to construct low-density parity check convolutional codes which are 4-cycles free and hence can be efficiently decoded by the iterative message-passing algorithm.

## Optimized degree distributions for binary and non-binary LDPC codes in Flash memory

- **Status**: ✅
- **Reason**: Flash 메모리 직접(A): hard/soft read 양자화 기반 LDPC degree distribution 최적화, EXIT/RCA 분석으로 바이너리 LDPC 설계 기법 이식 가능
- **ID**: ieee:6979792
- **Type**: conference
- **Published**: 26-29 Oct.
- **Authors**: Kasra Vakilinia, Dariush Divsalar, Richard D. Wesel
- **PDF**: https://ieeexplore.ieee.org/document/6979792
- **Abstract**: This paper uses extrinsic-information-transfer (EXIT)-function analysis employing the reciprocal channel approximation (RCA) to obtain optimal LDPC code degree distributions for initial hard decoding (one-bit quantization of the channel output) and for decoding with the soft information provided by additional reads in both SLC (two-level cell) and MLC (four-level-cell) Flash memory. These results indicate that design for hard decoding can provide irregular degree distributions that have good thresholds across the range of possible decoding precisions. These results also quantify the potential benefit of irregular LDPC codes as compared to regular LDPC codes in the flash setting and compare the RCA-EXIT thresholds of word-line voltages optimized for maximum mutual information (MMI) and word-line voltages that explicitly minimize the RCA-EXIT threshold of a specific LDPC degree distribution. Along the way, this paper illustrates that the MMI optimization of word-line voltages for five reads is a quasi-convex problem for the Gaussian model of SLC Flash. The paper also uses RCA-based EXIT analysis to show that for the same spectral efficiency of 0.9 bits per cell, rate-0.45 non-binary LDPC codes on MLC Flash systems provide thresholds more than 0.5 dB better than rate-0.9 binary LDPC codes on SLC Flash with the same number of reads (i.e. three reads that would provide hard decisions for MLC and limited soft information for SLC). The MLC approach has a potential threshold improvement of more than 1.5 dB over the SLC approach when both systems have access to the full soft information.

## Low complexity construction of low density lattice codes based on array codes

- **Status**: ❌
- **Reason**: Low density lattice code(LDLC) — 유클리드 공간 격자부호, 바이너리 LDPC ECC가 아님
- **ID**: ieee:6979845
- **Type**: conference
- **Published**: 26-29 Oct.
- **Authors**: Ricardo Antonio Parrao Hernandez, Brian M. Kurkoski
- **PDF**: https://ieeexplore.ieee.org/document/6979845
- **Abstract**: Recently a variety of lattices called low density lattices codes (LDLC) have been studied because they can be decoded efficiently using belief propagation, and can be seen as a Euclidean space codes analogue to low density parity check codes (LDPC). Previous LDLC lattice designs, like Latin square, are based on high-complexity computer search to eliminate 4-cycles. Array codes have been used to construct LDPC codes efficiently. This work describes the design of LDLC based on array codes. This construction is 4-cycle free and a systematic construction of the parity check matrix. For all cases considered, the LDLC based on array codes have a better symbol error rate performance than the latin square. For example, there is a 0.5 dB gain for dimension n = 91.

## On computing the weight distribution of non-binary ldpc codes using the probabilistic algorithm

- **Status**: ❌
- **Reason**: 비이진 LDPC weight distribution 추정 — non-binary 전용이라 제외
- **ID**: ieee:6979793
- **Type**: conference
- **Published**: 26-29 Oct.
- **Authors**: Masanori Hirotomo, Jun'ichi Tsurumi, Masakatu Morii
- **PDF**: https://ieeexplore.ieee.org/document/6979793
- **Abstract**: Non-binary low-density parity-check (LDPC) codes are linear block codes defined by the sparse parity-check matrix over finite fields. The weight distribution is a significant factor to evaluate error floors of LDPC codes. In this paper, we propose a probabilistic method for estimating the low part of the weight distribution of non-binary LDPC codes. Using the proposed method, we can estimate the low part of the weight distribution with small failure probability.

## Non-binary LDPC decoding using truncated messages in the Walsh-Hadamard domain

- **Status**: ❌
- **Reason**: 비이진 LDPC EMS/Walsh-Hadamard 디코딩 — non-binary GF(q) 전용이라 제외
- **ID**: ieee:6979794
- **Type**: conference
- **Published**: 26-29 Oct.
- **Authors**: Jossy Sayir
- **PDF**: https://ieeexplore.ieee.org/document/6979794
- **Abstract**: The Extended Min-Sum (EMS) algorithm for non-binary low-density parity-check (LDPC) defined over an alphabet of size q operates on truncated messages of length q' to achieve a complexity of the order q'2. In contrast, Walsh-Hadamard (WH) transform based iterative decoders achieve a complexity of the order q log q, which is much larger for q' ≪ q. In this paper, we demonstrate that considerable savings can be achieved by letting WH based decoders operate on truncated messages as well. We concentrate on the direct WH transform and compute the number of operations required if only q' of the q inputs are non-zero. Our paper does not cover the inverse WH transform and hence further research is needed to construct WH based decoders that can compete with the EMS algorithm on complexity terms.

## Entanglement-assisted quantum error-correcting codes based on the circulant permutation matrix

- **Status**: ❌
- **Reason**: Entanglement-assisted 양자 EC 코드, 스태빌라이저 기반 — 양자 전용 개념 의존이라 제외
- **ID**: ieee:6979823
- **Type**: conference
- **Published**: 26-29 Oct.
- **Authors**: Mihoko Wada, Keisuke Kodaira, Tomoharu Shibuya
- **PDF**: https://ieeexplore.ieee.org/document/6979823
- **Abstract**: Entanglement-assisted quantum error-correcting (EAQEC) codes, a wider class of stabilizer codes, allow us to construct quantum error-correcting codes from arbitrary classical codes with the help of ebits, i.e. maximally entangled quantum states. However, in the construction of EAQEC codes, it is desirable to use as small number of ebits as possible because of the high cost in the preparation of those entangled states. In addition, it is also desired that the error-correcting capability of classical codes from which EAQEC codes are constructed is as high as possible. In order to solve those problems, we consider in this paper a class of EAQEC codes that are based on classical LDPC codes whose parity check matrices are designed by the circulant permutation matrix. Then we give some sufficient conditions on those parity check matrices so that the obtained EAQEC codes need only one ebits. Moreover, we also clarify the condition on which parity check matrices satisfying above sufficient conditions have no 4-cycle, which is one of the important characteristics for the sum-product decoding to exhibit high error-correcting capability.

## Spectral shape of non-binary LDPC code ensembles with separated variable nodes

- **Status**: ❌
- **Reason**: 비이진 LDPC 앙상블의 spectral shape 이론, 바이너리 아니고 디코더/HW로 안 이어짐
- **ID**: ieee:6979791
- **Type**: conference
- **Published**: 26-29 Oct.
- **Authors**: Giuliano Garrammone, Enrico Paolini, Marco Chiani
- **PDF**: https://ieeexplore.ieee.org/document/6979791
- **Abstract**: The non-binary weight distribution and its spectral shape is developed for a partially-structured ensemble of low-density parity-check codes over finite fields. The ensemble is characterized by all degree-2 variable nodes and some of the degree-3 variable nodes being separated. It is shown that, under node separation, the typical minimum distance is strictly positive and significantly higher than the one of the corresponding unstructured ensemble.

## Precoding by Priority: A UEP scheme for RaptorQ codes

- **Status**: ❌
- **Reason**: RaptorQ fountain code UEP — fountain/erasure 응용, 떼어낼 바이너리 LDPC ECC 기법 없음
- **ID**: ieee:6979846
- **Type**: conference
- **Published**: 26-29 Oct.
- **Authors**: Keshava M Elliadka, Robert Morelos-Zaragoza
- **PDF**: https://ieeexplore.ieee.org/document/6979846
- **Abstract**: Raptor codes are the first class of fountain codes with linear time encoding and decoding. These codes are recommended in standards such as Third Generation Partnership Project (3GPP) and digital video broadcasting. RaptorQ codes are an extension to Raptor codes, having better coding efficiency and flexibility. Standard Raptor and RaptorQ codes are systematic with equal error protection of the data. However, in many applications such as MPEG transmission, there is a need for Unequal Error Protection (UEP): namely, some data symbols require higher error correction capabilities compared to others. We propose an approach that we call Priority Based Precode Ratio (PBPR) to achieve UEP for systematic RaptorQ and Raptor codes. Our UEP assumes that all symbols in a source block belong to the same importance class. The UEP is achieved by changing the number of precode symbols depending on the priority of the information symbols in the source block. PBPR provides UEP with the same number of decoding overhead symbols for source blocks with different importance classes. We demonstrate consistent improvements in the error correction capability of higher importance class compared to the lower importance class across the entire range of channel erasure probabilities. We also show that PBPR does not result in a significant increase in decoding and encoding times compared to the standard implementation.

## Fountain codes based on zigzag decodable coding

- **Status**: ❌
- **Reason**: 비이진 LDPC 기반 fountain code(zigzag) — non-binary + fountain이라 제외
- **ID**: ieee:6979847
- **Type**: conference
- **Published**: 26-29 Oct.
- **Authors**: Takayuki Nozaki
- **PDF**: https://ieeexplore.ieee.org/document/6979847
- **Abstract**: Fountain codes based on non-binary low-density parity-check (LDPC) codes have good decoding performance when the number of source packets is finite. However, the space complexity of the decoding algorithm for fountain codes based on non-binary LDPC codes grows exponentially with the degree of a field extension. Zigzag decodable codes generate the output packets from source packets by using shift and exclusive or. It is known that the zigzag decodable codes are efficiently decoded by the zigzag decoder. In this paper, by applying zigzag decodable coding to fountain codes, we propose a fountain code whose space decoding complexity is nearly equal to that for the Raptor codes. Simulation results show that the proposed fountain coding system outperforms Raptor coding system in terms of the overhead for the received packets.

## Estimation of areal density gains of TDMR system with 2D detector

- **Status**: ✅
- **Reason**: HDD 스토리지 ECC, 새 cross-track LDPC 코딩 스킴(코드워드가 2트랙 span) (B/E)
- **ID**: ieee:6979929
- **Type**: conference
- **Published**: 26-29 Oct.
- **Authors**: Rathnakumar Radhakrishnan, Nedeljko Varnica, Mats Öberg
- **PDF**: https://ieeexplore.ieee.org/document/6979929
- **Abstract**: Two-dimensional magnetic recording (TDMR) is expected to drive continued areal density growth of hard-disk drives (HDDs) as the growth for conventional perpendicular magnetic recording (PMR)-based HDDs is slowing down. Feasibility of manufacturing more than one reader in a single head has hastened the development of TDMR and considerable effort is underway in developing read channels that can exploit the availability of multiple readers. First generation of TDMR-based HDDs will likely derive its gains from the SNR improvement obtained by combining multiple readback signals to remove inter-track interference (ITI). In this case, data belonging to a single track of interest is subsequently detected. A natural extension to this system is to combine the readback signals without removing ITI and jointly detecting data belonging to two tracks using a two-dimensional detector. Under the assumption that tracks are written synchronously, in this paper, we explore from a systems perspective if further areal density gains can be obtained from such a system. We employ a grain-based channel model for our investigation and estimate gains by appropriate optimization of the dual-reader systems, including optimizing reader placement. Furthermore, for the set of reader placement configurations, which affords reliable detection of both tracks, we introduce a new coding scheme called cross-track coding and show that additional areal density gains can be obtained. In this scheme, user data is LDPC-encoded and written such that every codeword spans two tracks as opposed to one track as in conventional PMR.

## Symbol-level synchronization using probability lookup-table for IDS error correction

- **Status**: ✅
- **Reason**: 스토리지(BPM) 외부 LDPC+inner marker 연접; 기여는 마커 동기화지만 LDPC ECC 인접이라 Phase3 재검토
- **ID**: ieee:6979900
- **Type**: conference
- **Published**: 26-29 Oct.
- **Authors**: Haruhiko Kaneko
- **PDF**: https://ieeexplore.ieee.org/document/6979900
- **Abstract**: Insertion/Deletion/Substitution (IDS) error correction will become important for future high-density storage devices, e.g., bit-patterned media. For IDS error correction, concatenated codings of an outer LDPC code and an inner marker code have been proposed. To improve the synchronization capability, marker decoder can employ symbol-level synchronization (SLS) with a large symbol size, while the computational time complexity of the SLS increases exponentially with the symbol size. This paper proposes an SLS using a probability lookup table to reduce the complexity. Probabilities in the table are precomputed for given channel and code parameters, and computationally intensive calculations of the SLS are replaced by table lookups. The proposed method is applicable to both single-path and multipath decodings. The bit error rate (BER) is evaluated for SLS of symbols sizes bS = 1, 2, 4, and 8 bits, and it is confirmed that larger symbol size gives lower BER.

## On generator polynomial matrices of generalized pseudo-cyclic codes

- **Status**: ❌
- **Reason**: 비-LDPC 부호(generalized pseudo-cyclic), 떼어낼 BP 디코더·HW 기법 없음
- **ID**: ieee:6979864
- **Type**: conference
- **Published**: 26-29 Oct.
- **Authors**: Hajime Matsui
- **PDF**: https://ieeexplore.ieee.org/document/6979864
- **Abstract**: In this paper, generalized pseudo-cyclic (GPC) codes are proposed and their basic properties are investigated. Generator polynomial matrices of GPC codes are constructively defined and thereby a dimension formula for GPC codes is provided. While a pseudo-cyclic code is equal to an ideal of the ring which consists of polynomials modulo a fixed polynomial, a GPC code is equal to a submodule of the direct sum of the rings which consist of polynomials modulo fixed polynomials. In the theory of cyclic codes and PC codes, Euclidean division algorithm for polynomials is essential; its generalization for polynomial vectors is obtained and enables us with generator polynomial matrices to encode GPC codes fast and systematically.

## Permuted successive cancellation decoder for polar codes

- **Status**: ❌
- **Reason**: polar 전용 SC 디코더 그래프 순열, 코드 비의존 BP 이식 불가
- **ID**: ieee:6979881
- **Type**: conference
- **Published**: 26-29 Oct.
- **Authors**: Harish Vangala, Emanuele Viterbo, Yi Hong
- **PDF**: https://ieeexplore.ieee.org/document/6979881
- **Abstract**: We study a new variant of Arikan's successive cancellation decoder (SCD) for polar codes. We first propose a new decoding algorithm on a new decoder graph, where the various stages of the graph are permuted. We then observe that, even though the usage of the permuted graph doesn't affect the encoder, it can significantly affect the decoding performance of a given polar code. The new permuted successive cancellation decoder (PSCD) typically exhibits a performance degradation, since the polar code is optimized for the standard SCD. We then present a new polar code construction rule matched to the PSCD and show their performance in simulations. For all rates we observe that the polar code matched to a given PSCD performs the same as the original polar code with the standard SCD. We also see that a PSCD with a reversal permutation can lead to a natural decoding order, avoiding the standard bit-reversal decoding order in SCD without any loss in performance.

## Enhancement of punctured turbo code with UTPA in optical wireless channel

- **Status**: ❌
- **Reason**: 광무선 turbo code + 전력할당(UTPA) — 비-LDPC, 떼어낼 LDPC BP 기법 없음
- **ID**: ieee:6979828
- **Type**: conference
- **Published**: 26-29 Oct.
- **Authors**: Sachin Rai, Hiromasa Habuchi
- **PDF**: https://ieeexplore.ieee.org/document/6979828
- **Abstract**: In this paper, the performance of rate r=1/2 punctured turbo code using a technique called Unequal Transmission Power Allocation (UTPA) is studied in optical wireless communication (OWC) with intensity modulation and direct detection (IM/DD). UTPA scheme is applied at the outputs of rate r=1/2 punctured turbo encoder. Different powers are allocated to systematic bit and parity bits keeping the total transmission power fixed. BPPM is used as modulation technique and the system's performance is evaluated through simulation in an optical wireless channel. Obtained results suggest that punctured turbo code combined with UTPA technique is an effective method which leads to better Bit Error Rate (BER) performance in an optical wireless channel. Furthermore, suitable power allocation ratio is located for the given channel condition.

## Finite-length analysis for secret random number generation and coding theorems

- **Status**: ❌
- **Reason**: 유한길이 secret random number generation/source coding 이론 — 디코더/HW/구성으로 안 이어지는 순수 이론, 보안 영역
- **ID**: ieee:6979857
- **Type**: conference
- **Published**: 26-29 Oct.
- **Authors**: Masahito Hayashi
- **PDF**: https://ieeexplore.ieee.org/document/6979857
- **Abstract**: Shannon theory had been considered as an unpractical engineering theory because the obtained optimizations focused on the asymptotic analysis, which are far from a practical setting. However, recent progresses are resolving this defect from achieving finite-length analysis on several information theoretical topics based on the traditional asymptotic results. These progresses enable us to evaluate the performances of realizable systems. The main factors of this research stream are the reflection for the traditional stream and the progress of the method of information spectrum, which has mainly been developed in Japan. However, we cannot ignore the effect by the min entropy developed in cryptography community and the practical demands required by the quantum cryptography system. As results, the finite-length theory has been developed in an interdisciplinary area across information theory community, the communication theory, cryptography theory, and quantum information theory. In this talk, we review the finite-length analysis for the secure random number generation as the most successful case, and briefly explain its extension to source coding, channel coding, and the quantum extension.

## Write-Once Memory codes for low-complexity decoding of Asymmetric Multiple Access Channel

- **Status**: ❌
- **Reason**: WOM 부호 무선 AMAC 응용, LDPC 무관
- **ID**: ieee:6979916
- **Type**: conference
- **Published**: 26-29 Oct.
- **Authors**: Ryota Sekiya, Erick Christian Garcia Alvarez, Brian M. Kurkoski +1
- **PDF**: https://ieeexplore.ieee.org/document/6979916
- **Abstract**: Write-Once Memory (WOM) codes are designed for data storage, which allow re-writing on n cells that can change their bit value from 0 to 1 but not vice versa. This paper focuses on applying “WOM codes” to cooperative wireless communications. Due to the characteristics of WOM codes, the Asymmetric Multiple Access Channel (AMAC) (also referred to as the MAC with degraded messages) is considered, which is a conventional Multiple Access Channel (MAC), where one user can observe the other user's message. We describe an AMAC system where WOM codes are used to deal with the interference between two users. For a specific AMAC model, WOM codes can achieve the AMAC capacity, and using WOM codes for the AMAC with no errors leads to a low-complexity decoder. Finally, we comment of how the AMAC model can be applied to the relay channel. While we consider primarily the AMAC with no errors, this study forms a foundation for future work on the AMAC with errors.

## Sequential decoding of Reed-Solomon codes

- **Status**: ❌
- **Reason**: RS/polar 순차 디코딩, LDPC BP로 이식되는 기법 아님
- **ID**: ieee:6979884
- **Type**: conference
- **Published**: 26-29 Oct.
- **Authors**: Vera Miloslavskaya, Peter Trifonov
- **PDF**: https://ieeexplore.ieee.org/document/6979884
- **Abstract**: The problem of efficient soft-decision decoding of Reed-Solomon codes is considered. Low-complexity sequential algorithm was recently proposed for decoding of polar codes. A generalization of this algorithm to the case of Reed-Solomon codes, represented as polar codes with dynamic frozen symbols, is proposed. Simplification of the proposed decoding algorithm to the case of transmission of binary image of Reed-Solomon code is derived.

## Faulty successive cancellation decoding of polar codes for the binary erasure channel

- **Status**: ❌
- **Reason**: polar SC 디코딩 결함 모델(BEC), 이식 가능한 LDPC BP 기법 없음
- **ID**: ieee:6979883
- **Type**: conference
- **Published**: 26-29 Oct.
- **Authors**: Alexios Balatsoukas-Stimming, Andreas Burg
- **PDF**: https://ieeexplore.ieee.org/document/6979883
- **Abstract**: We study faulty successive cancellation decoding of polar codes for the binary erasure channel. To this end, we introduce a simple erasure-based fault model and we show that, under this model, polarization does not happen, meaning that fully reliable communication is not possible at any rate. Moreover, we provide numerical results for the frame erasure rate and bit erasure rate and we study an unequal error protection scheme that can significantly improve the performance of the faulty successive cancellation decoder with negligible overhead.

## Lower error floor of LDPC codes based on trapping sets elimination

- **Status**: ✅
- **Reason**: 트래핑셋 제거로 error floor 저감하는 노드 재배열 알고리즘 — 바이너리 LDPC 코드설계(E) 이식 가능, 디스크 스토리지 언급
- **ID**: ieee:6992175
- **Type**: conference
- **Published**: 23-25 Oct.
- **Authors**: Le Dong, Ziyu Zhao, Jing Lei +1
- **PDF**: https://ieeexplore.ieee.org/document/6992175
- **Abstract**: LDPC codes with excellent performance have great potential in applications of wireless mobile communications. However, the error floor phenomenon existing in LDPC codes limits its further application in disk storage and deep-space communications which require very low bit error rate (BER) system. The researchers find that trapping sets are the major reason why the LDPC codes have error floor. In this paper, we proposed an elimination algorithm to reduce small trapping sets. It was applying node rearrangement method to optimize the neighborhood of target nodes. In this way, cycles will be broken and the small size of trapping sets can be eliminated. The experimental results show that it can lower the error floor to improve the performance of LDPC codes. Besides, we also can keep the degree distribution, code rates and girth features of the original code with this method.

## D-GLDPC codes with 3-D single parity-check product codes as super check nodes

- **Status**: ❌
- **Reason**: D-GLDPC에 3-D SPC 곱부호를 super-check node로 사용 — 일반화 LDPC 구조 EXIT 분석, 표준 바이너리 LDPC에 직접 이식할 신규 디코더·구성 부재(SPC-PC 의존), 경계지만 NAND 이식성 약함
- **ID**: ieee:6992199
- **Type**: conference
- **Published**: 23-25 Oct.
- **Authors**: Yejun He, Guiyuan Sun, Jie Yang +1
- **PDF**: https://ieeexplore.ieee.org/document/6992199
- **Abstract**: A doubly-generalized low-density parity-check (D-GLDPC) code is a low-density parity-check (LDPC) code, where both of the check nodes and variable nodes use linear block codes instead of repetition and single parity-check (SPC) codes. In this paper, we propose a class of D-GLDPC codes in which 3-dimensional (3-D) single parity-check product-codes (SPC-PCs) are used as super-check nodes (SCNs). We derive the extrinsic information transfer (EXIT) function of 3-D SPC-PCs used as SCNs, and analyze the performance of the proposed D-GLDPC codes over the additive white Gaussian noise (AWGN) channel with EXIT charts. Numerical analysis from EXIT charts shows that our proposed D-GLDPC codes can offer better decoding threshold than D-GLDPC codes with 2-D SPC-PCs as SCNs.

## The hardware design of LDPC decoder in IEEE 802.11n/ac

- **Status**: ✅
- **Reason**: IEEE 802.11n/ac LDPC 디코더 부분병렬 HW 아키텍처 + permutation network 생성기 — HW 아키텍처(D) 이식 가능
- **ID**: ieee:7090144
- **Type**: conference
- **Published**: 23-25 Oct.
- **Authors**: Hyobeen Park, Seongjoo Lee
- **PDF**: https://ieeexplore.ieee.org/document/7090144
- **Abstract**: In this paper, the design of the LDPC decoder architecture in IEEE 802.11n/ac is proposed. The proposed decoder is used to the partial parallel architecture to provide 2 Gbps throughput at 200 MHz clock frequency. In IEEE 802.11n/ac, 12 parity check metrics is provide to support diverse code rates and block lengths. Therefore the network between nodes is configured to be satisfied parity check metrics. However, the structure of the network increases the complexity of LDPC decoder. Hence, the optimized network generator is also proposed to reduce the complexity of the network.

## Enhancement of indoor VLC communication system with optical path design and FEC code

- **Status**: ❌
- **Reason**: VLC 통신 시스템에 표준 RS/LDPC 적용 실험, 새 디코더·구성 없음, 응용 특이적 제외
- **ID**: ieee:6992113
- **Type**: conference
- **Published**: 23-25 Oct.
- **Authors**: Xiang Zhang, Min Zhang, Dahai Han +1
- **PDF**: https://ieeexplore.ieee.org/document/6992113
- **Abstract**: The enhanced visible light communications (VLC) system with transmission distance of 7m is demonstrated using transmission path design and forward error correction code in this paper. Moreover, RS (160, 128) and LDPC (960, 480) code are implemented and experimented via VLC test-bed. The results suggest that based on the given power, 5Mbps transmission bit rate and 10-3 bit error rate (BER), in comparison with uncoded system, average communication distance increases 18% with RS code and 39% with LDPC code, effective communication area increases 154% with RS code and 236% with LDPC code.

## On the design of MLC-LDPC-OFDM in DRM MF and HF channels

- **Status**: ✅
- **Reason**: MLC-LDPC LLR(우도비) 계산을 채널모델 따라 수정 — LLR 계산 변형은 NAND 디코더에 이식 가능, 애매하므로 보류
- **ID**: ieee:6992075
- **Type**: conference
- **Published**: 23-25 Oct.
- **Authors**: Yuan Liang, Shulin Zhang, Pinbiao Gu +1
- **PDF**: https://ieeexplore.ieee.org/document/6992075
- **Abstract**: Orthogonal Frequency Division Multiplexing (OFDM), aided by proper channel coding schemes, can realize very dependable transmission in fading channels. For the purpose of improving the performance of the OFDM based DRM digital AM broadcasting in MF and HF channels, this paper designs MLC-LDPC-OFDM transmission scheme that is suitable for MF and HF channels. The equivalent channel capacities of MLC-LDPC-OFDM with two different decoding strategies, namely IMSD and PDL, are analyzed, basing on which this paper redesigns the code rates of MLC. In addition, the calculation of likelihood ratio in LDPC decoding is modified according to channel models. The simulation results show that the proposed schemes have better performance than the existing ones in MF and HF channels.

## Gibbs sampling based parameter estimation for RSC sub-codes of turbo codes

- **Status**: ❌
- **Reason**: turbo RSC 서브코드 파라미터 추정(Gibbs sampling), 비-LDPC, 디코더 이식 기법 없음
- **ID**: ieee:6992195
- **Type**: conference
- **Published**: 23-25 Oct.
- **Authors**: Peidong Yu, Jing Li, Hua Peng
- **PDF**: https://ieeexplore.ieee.org/document/6992195
- **Abstract**: This paper deals with the Bayesian parameter estimation for recursive convolutional sub-codes of turbo codes. A Monte Carlo method named Gibbs sampling is employed for this problem. The involved conditional probabilities of the encoder coefficients and the coded sequences are derived. Simulation results show that the proposed algorithm improves the estimation accuracy substantially.

## Research on improved coding and decoding algorithm for fountain codes

- **Status**: ❌
- **Reason**: Fountain(erasure) 부호 인코딩/디코딩 개선 — fountain/erasure 제외, 비-LDPC 채널 ECC 아님
- **ID**: ieee:6992155
- **Type**: conference
- **Published**: 23-25 Oct.
- **Authors**: Zhifeng Zhu, Liulei Zhou, Jia Hou
- **PDF**: https://ieeexplore.ieee.org/document/6992155
- **Abstract**: Fountain code is a class of graph-based linear erasure codes, which can effectively solve the problems such as network congestion and feedback cracking for its characteristics of rateless and can resume when interrupted, and has a lower complexity of encoding and decoding. However, there are still some problems in the process of encoding and decoding, including the degree distribution structure may be destroyed, parameters of the generating matrix are not fixed, and it cannot recover source datas from the remaining encoded packets with no degree one. So, the basic theory of fountain codes from three aspects are introduced in this paper, i.e., degree distribution, encoding and decoding principles. Therefore the improved algorithms according to the above three aspects are presented. Simulation results show that the proposed algorithm is more efficient than the previous one.

## Performance analysis of symbol interleaving for next generation mm-Wave MIMO WLAN

- **Status**: ❌
- **Reason**: mm-Wave MIMO WLAN 심볼 인터리빙/톤매핑, LDPC는 부수 언급, 떼어낼 ECC 기법 없음
- **ID**: ieee:6992035
- **Type**: conference
- **Published**: 23-25 Oct.
- **Authors**: Changgeng Li, Shiwen He, Su Gao +4
- **PDF**: https://ieeexplore.ieee.org/document/6992035
- **Abstract**: Interleaving, as an important module of wireless communication system, is used to resist burst errors caused by frequency-selective fading. Low Density Parity Check Code (LDPC) tone mapping would be adopted for Orthogonal Frequency Division Multiplexing (OFDM) systems in IEEE 802.11aj (45GHz). In this paper, an optimal symbol interleaving parameter selecting (OSIPS) algorithm is proposed to get the optimal interleaving parameter. Based on this algorithm, the optimal tone mapping distance for conventional bandwidth based tone mapping (BTM) mechanism is obtained. This paper also presents two adaptive tone mapping mechanisms, including spatial streams based adaptive tone mapping (SSATM) and MCS based adaptive tone mapping (MATM). Adopting the tone mapping distance selected by OSIPS algorithm can bring the best packet error rate gain (up to 4dB) for BTM. And SSATM and MATM perform better than BTM, especially for small number of spatial streams and low MCS.

## Signal processing of WiMAX physical layer based on low-density parity-check codes

- **Status**: ❌
- **Reason**: WiMAX 물리계층에 표준 array code LDPC + 표준 MP 알고리즘 적용—무선 응용, 신규 기여 없는 표준 기법 재사용
- **ID**: ieee:6987841
- **Type**: conference
- **Published**: 22-25 Oct.
- **Authors**: Chawalit Benjangkaprasert, Torpong Inchan
- **PDF**: https://ieeexplore.ieee.org/document/6987841
- **Abstract**: WiMAX technology supports very high data rate, high capacity and high quality in mobile broadband wireless access system. The performance of the WiMAX system can be enhanced by incorporating a better channel coding technique. This paper presents the excellent performance channel coding known as low-density parity check (LDPC) codes which is a part of WiMAX system. A modified array code parity check matrix for LDPC encoder is used and the message passing (MP) algorithm for LDPC decoder is used, respectively. Both systems are modulated by the basic standard modulation scheme. The computer simulation results confirm that the bit error rate (BER) performance of the WiMAX system that incorporate with the powerful LDPC coding technique has been improved over the conventional standard WiMAX system. However, the computational complexity of the proposed WiMAX system is higher than the previous one.

## Performance evaluation of LDPC codes on patterned WBAN data

- **Status**: ❌
- **Reason**: WBAN ECG 데이터에 표준 LDPC 성능 평가—응용 특이적 BER 측정, 떼어낼 신규 디코더/구성/HW 기법 없음
- **ID**: ieee:7022496
- **Type**: conference
- **Published**: 22-25 Oct.
- **Authors**: Buncha Sansoda, Somak Choomchuay, Sekson Timakul +1
- **PDF**: https://ieeexplore.ieee.org/document/7022496
- **Abstract**: In this decade, WBAN plays vital role in health care monitoring environment. It has been used more intensively in wider applications. This paper proposes error control coding applied to WBAN. LDPC codes with the block size of 255 bytes are particularly of interest. Patterned information such as MIT-BIH's arrhythmia datasets extracted from Electrocardiography (ECG) of the patients who encountered heart disease. To measure the system performance, random data are also examined. The system was simulated on Rician channel where severe noise are quite nature to WBAN compared to AWGN channel. Rician channel with some K-factors was investigated. The obtained result shows that both patterned data and random data can be recovered well when Eb/N0 equals 3 dB and above. While the code rates were made varied from 0.50 to 0.75, we can obtain the gain of 3 dB, 5 dB, and 6 dB respectively.

## Performance optimization of generalized low-density parity-check codes with EXIT chart method for data transmission over partial-band jamming channels

- **Status**: ✅
- **Reason**: GLDPC 부호 EXIT chart 최적화로 저부호율 설계 — 이식 가능 코드 설계 기법(E), 애매하나 살림
- **ID**: ieee:6983179
- **Type**: conference
- **Published**: 22-24 Oct.
- **Authors**: Qi Li, Xinru Qu, Liuguo Yin +1
- **PDF**: https://ieeexplore.ieee.org/document/6983179
- **Abstract**: The design and optimization of low coding-rate channel codes is a hot topic for frequency-hopping spread-spectrum (FH-SS) transmission systems over harsh wireless channels. In this paper, we use extrinsic mutual information transfer (EXIT) chart to optimize a class of generalized low-density parity-check (GLDPC) codes over partial-band jamming (PBJ) transmission environment. With the proposed method, the channel capacity of the PBJ channel is illustrated, and based on which three code optimization methods are presented for achieving near-capacity performance. Simulation results show that, the GLDPC codes designed with the proposed method can achieve an information rate of 91.2% of the channel capacity, over the PBJ channel with 50% frequency band jammed and the channel signal-to-noise ratio (SNR) of the unjammed frequency band equals to -8 dB.

## The performance analysis of QC-LDPC codes constructed by Dayan sequence for coded cooperative relay

- **Status**: ❌
- **Reason**: Dayan sequence QC-LDPC 구성 + 협력중계 응용; 새 구성이라 보이나 무선 응용 특이적이고 표준 QC 변형 수준—애매하나 떼어낼 신규성 약함
- **ID**: ieee:7017175
- **Type**: conference
- **Published**: 20-22 Oct.
- **Authors**: Yan Zhang, Feng-fan Yang
- **PDF**: https://ieeexplore.ieee.org/document/7017175
- **Abstract**: This paper presents Dayan sequence to construct QC-LDPC codes through the combination of mathematical theory. The paper introduces the procedure of the coding principle and coding. Dayan sequence constructed QC-LDPC codes is compared with rate compatible QC-LDPC, Simulation results show that the bit error rate (BER)performance of Dayan sequence constructed QC-LDPC is improved by 0.5dB. Then QC-LDPC codes constructed by the Dayan sequence are used in coded cooperative communication. Compared it with PEG algorithm, array code and Mackey code,the results show that the performance of Dayan sequence is superior. That is to say that Dayan sequence code constructed QC-LDPC is effective in coded cooperative communication.

## Optimal voltage signal sensing of NAND flash memmory for LDPC code

- **Status**: ✅
- **Reason**: NAND 플래시 LDPC용 임계전압 센싱 전략(Ununiform-SOR)으로 LLR/센싱 최적화 — A 직접 해당
- **ID**: ieee:6986077
- **Type**: conference
- **Published**: 20-22 Oct.
- **Authors**: Shigui Qi, Dan Feng, Jingning Liu
- **PDF**: https://ieeexplore.ieee.org/document/6986077
- **Abstract**: Low-density parity-check (LDPC) code can provide stronger error correcting performance in NAND flash memory. LDPC decoder requires accurate soft-decision log-likelihood ratio (LLR) information which demands fine-grained flash memory threshold voltage sensing operations. The threshold voltage sensing operations incur energy consumption and access latency penalty. Therefore, it is important to minimize the flash memory sensing operations without noticeable error correcting performance decreasing. We propose a new flash memory sensing strategy Ununiform-SOR (ununiform sensing in overlapping region) which can reduce 20% flash memory sensing operations than traditional non-uniform threshold voltage sensing without reducing the error correcting performance of LDPC code in NAND flash memory noise channel. The new Ununiform-SOR sensing strategy can reduce more than 20% reading energy consumption than the non-uniform sensing strategy. The abstract goes here.

## FPGA implementation of a clockless stochastic LDPC decoder

- **Status**: ✅
- **Reason**: FPGA clockless stochastic LDPC 디코더 HW 구현 — 이식 가능 HW 아키텍처(D)
- **ID**: ieee:6986088
- **Type**: conference
- **Published**: 20-22 Oct.
- **Authors**: Chris Ceroici, Vincent C. Gaudet
- **PDF**: https://ieeexplore.ieee.org/document/6986088
- **Abstract**: This paper demonstrates a clockless stochastic low-density parity-check (LDPC) decoder implemented on a Field-Programmable Gate Array (FPGA). Stochastic computing reduces the wiring complexity necessary for decoding by replacing operations such as multiplication and division with simple logic gates and serial processing. Clockless decoding increases the throughput of the decoder by eliminating the requirement for node signals to be synchronized after each decoding cycle. The design is implemented on an ALTERA Stratix IV EP4SGX230 FPGA and the frame error rate (FER), throughput, and power performance are presented for (96,48) and (204,102) LDPC decoders.

## Increasing the speed of polar list decoders

- **Status**: ❌
- **Reason**: polar list 디코더 속도 개선; 비-LDPC, LDPC와 비교만 할 뿐 이식 기법 없음
- **ID**: ieee:6986089
- **Type**: conference
- **Published**: 20-22 Oct.
- **Authors**: Gabi Sarkis, Pascal Giard, Alexander Vardy +2
- **PDF**: https://ieeexplore.ieee.org/document/6986089
- **Abstract**: In this work, we present a simplified successive cancellation list decoder that uses a Chase-like decoding process to achieve a six time improvement in speed compared to successive cancellation list decoding while maintaining the same error-correction performance advantage over standard successive-cancellation polar decoders. We discuss the algorithm and detail the data structures and methods used to obtain this speed-up. We also propose an adaptive decoding algorithm that significantly improves the throughput while retaining the error-correction performance. Simulation results over the additive white Gaussian noise channel are provided and show that the proposed system is up to 16 times faster than an LDPC decoder of the same frame size, code rate, and similar error-correction performance, making it more suitable for use as a software decoding solution.

## Symbol-based successive cancellation list decoder for polar codes

- **Status**: ❌
- **Reason**: polar code SC list 디코더; 비-LDPC이고 LDPC BP 이식 기법 없음
- **ID**: ieee:6986086
- **Type**: conference
- **Published**: 20-22 Oct.
- **Authors**: Chenrong Xiong, Jun Lin, Zhiyuan Yan
- **PDF**: https://ieeexplore.ieee.org/document/6986086
- **Abstract**: Polar codes is promising because they can provably achieve the channel capacity while having an explicit construction method. Lots of work have been done for the bit-based decoding algorithm for polar codes. In this paper, generalized symbol-based successive cancellation (SC) and SC list decoding algorithms are discussed. A symbol-based recursive channel combination relationship is proposed to calculate the symbol-based channel transition probability. This proposed method needs less additions than the maximum-likelihood decoder used by the existing symbol-based polar decoding algorithm. In addition, a two-stage list pruning network is proposed to simplify the list pruning network for the symbol-based SC list decoding algorithm.

## Dual port ram based layered decoding for Multi Rate Quasi-Cyclic LDPC codes

- **Status**: ✅
- **Reason**: 멀티레이트 QC-LDPC layered 디코딩 dual-port RAM FPGA 아키텍처(permutation→address) — D 이식 가능 HW
- **ID**: ieee:7015253
- **Type**: conference
- **Published**: 19-23 Oct.
- **Authors**: Soner Yeşil, Murat Arslan
- **PDF**: https://ieeexplore.ieee.org/document/7015253
- **Abstract**: This paper presents a generic RAM based FPGA architecture for decoding of Multi Rate Quasi-Cycling LDPC codes. RAM based decoding enables us to reduce permutation networks into simple address controllers. Moreover, utilizing Block RAMs with various aspect ratios in an FPGA provides flexibility ranging from area driven compact designs to fully parallelized high throughput designs. Utilizing the read-first property of the RAMs, the proposed design efficiently exploits the dual port Block RAM resources by accessing all the four ports at the same time. Such facilities of recent FPGA devices have been combined with the well known layered decoding algorithm with non-linearly mapped Min-Sum approximation in order to obtain area efficient yet high throughput decoders. The proposed decoder architecture has been verified on Xilinx XC7Z020 FPGA device for IEEE 802.16e Wimax LDPC codes. 340Mbps of information throughput has been observed at an operating frequency of 150MHz.

## Low Density Parity Check codes with quasi-cyclic structure and zigzag pattern

- **Status**: ✅
- **Reason**: 바이너리 QC-LDPC 신규 구성(IRA-like, zigzag, 저중량 코드워드·짧은 사이클 제거) — 코드 설계 기법 이식 가능(E)
- **ID**: ieee:7015290
- **Type**: conference
- **Published**: 19-23 Oct.
- **Authors**: Wenwen Li, Bin Chen, Jing Lei +1
- **PDF**: https://ieeexplore.ieee.org/document/7015290
- **Abstract**: Low-Density Parity-Check (LDPC) codes with linear time encoding complexity and low hardware storage are a hot issue recently. We propose a general method for constructing LDPC codes with quasi-cyclic (QC) structure and improved zigzag pattern to obtain both linear time encoding and low hardware storage. We call it irregular repeat accumulate like (IRA-like) codes for its similarity with irregular repeat accumulate (IRA) codes. Through the optimization-constraint of QC-LDPC codes and the modification of dual diagonal structure we have acquired IRA-like codes with reduced number of low-weight codewords and short cycles. Extensive simulation results show that the IRA-like codes not only achieve better performance than some kinds of classical LDPC codes but also have much better practicability. Compared with the LDPC code applied in China Mobile Multimedia Broadcasting (CMMB), IRA-like code significantly outperforms the CMMB-LDPC code about 0.18 dB at BER=10-5.

## Algorithm of multithreshold decoding for non-binary self-orthogonal concatenated codes

- **Status**: ❌
- **Reason**: 비이진 q-ary 자기직교부호 다중임계 디코딩, non-binary라 제외
- **ID**: ieee:7035905
- **Type**: conference
- **Published**: 15-17 Oct.
- **Authors**: Valery Zolotarev, Yerzhan Seitkulov, Gennady Ovechkin +3
- **PDF**: https://ieeexplore.ieee.org/document/7035905
- **Abstract**: Non-binary multithreshold decoding (qMTD) for q-ary self-orthogonal codes (qSOC) is considered. The SER performance of qMTD is shown to be close to the results provided by optimum total search methods, which are not realizable for non-binary codes in general. qMTD decoders are compared with different decoders for Reed-Solomon codes. The performance provided with qMTD in some cases is unattainable with classical decoders for arbitrary long Reed-Solomon codes. The result of concatenation of qSOC with simple to decode outer codes is described. Method of improving of qMTD decoder's performance for qSOC is offered. Some simulated results obtained by using these two decoding techniques (the base and modified ways) are presented as well. Comparison of the results showed that the change in the threshold element's algorithm can significantly improve speed of qMTD work. It's shown that for a larger gain this modification qMTD should be used after conventional decoding iterations.

## A new simplified RRWBF decoding algorithm for LDPC decoder in CMMB

- **Status**: ✅
- **Reason**: 단순화된 RRWBF 소프트값 비트플리핑 LDPC 디코딩 알고리즘 신규 제안, 부호 비의존적 바이너리 LDPC 디코더로 이식 가능(C)
- **ID**: ieee:7003892
- **Type**: conference
- **Published**: 14-16 Oct.
- **Authors**: Xiangran Sun, Yunyun Wei
- **PDF**: https://ieeexplore.ieee.org/document/7003892
- **Abstract**: A new soft-value bit-flipping low-density parity-check (LDPC) decoding is proposed based on a simplified reliability ratio based on weighted bit-flipping (RRWBF) algorithm. Moreover, we design a soft-output demapping and soft-decision decoding for the LDPC code in China Mobile Multimedia Broadcasting (CMMB). In addition, the complexity of decoding and the consumption of hardware is reduced effectively by our proposed simplified algorithm.

## Design of a multi-rate quasi-cyclic low-density parity-check encoder based on pipelined rotate-left-accumulator circuits

- **Status**: ✅
- **Reason**: 멀티레이트 QC-LDPC 인코더 파이프라인 RLA 회로 FPGA HW 구현, 이식 가능 HW 아키텍처(D)
- **ID**: ieee:7003945
- **Type**: conference
- **Published**: 14-16 Oct.
- **Authors**: Fei Wang, Peng Zhang, Xin Wan +1
- **PDF**: https://ieeexplore.ieee.org/document/7003945
- **Abstract**: A serial-input serial-output encoder based on pipelined rotate-left-accumulator (RLA) circuits is designed for multi-rate Quasi-Cyclic Low-Density Parity-Check (QC-LDPC) codes of Chinese digital terrestrial/television multimedia broadcasting (DTMB) standard. The RLA circuit can make the area usage economical, and the pipelined architecture can simplify the memory structure. The encoder is implemented on FPGA. Simulation results demonstrate that the design meets the requirement of DTMB standard with lower energy consumption and fewer hardware resources.

## Design of LDPC codes for binary-input Gaussian interference channels

- **Status**: ❌
- **Reason**: 간섭채널용 LDPC degree distribution 최적화(무선 다중사용자 특이적), NAND에 이식할 신규 구성 기법 아님
- **ID**: ieee:7008245
- **Type**: conference
- **Published**: 13-15 Oct.
- **Authors**: Shancheng Zhao, Xiao Ma, Baoming Bai
- **PDF**: https://ieeexplore.ieee.org/document/7008245
- **Abstract**: Due to the existence of multiuser interference, codes optimized for point-to-point links may be unsuitable for multiuser networks. In this paper, we are concerned with the design of low-density parity-check (LDPC) codes for binary-input Gaussian interference channels (GIFC). We utilize a Monte-Carlo approach based on the downhill-simplex algorithm to obtain good LDPC degree distributions for GIFC. Simulation results show that the constructed codes perform better than codes optimized only for point-to-point links. For symmetric GIFC with coefficient h2 = 0.75, coding gain about 0.6 dB is obtained. These results indicate that, as opposed to using off-the-shell codes designed for point-to-point links, new codes should be designed in multiuser networks.

## Simplified partially parallel DVB-S2 LDPC decoder architectural design based on FPGA

- **Status**: ✅
- **Reason**: D: DVB-S2 LDPC FPGA 부분병렬 디코더, 신규 barrel shifter·BNU/CNU 최적화 — HW 이식 가능
- **ID**: ieee:7008293
- **Type**: conference
- **Published**: 13-15 Oct.
- **Authors**: Wenjing Wang, Lixin Li, Huisheng Zhang
- **PDF**: https://ieeexplore.ieee.org/document/7008293
- **Abstract**: In this paper, a simplified partially parallel decoder architectural based on field programmable gate array (FPGA) devices for Digital Video Broadcasting-Satellite 2 low-density parity-check(DVB-S2-LDPC) codes has been presented. We introduce the current research status about decoder design for LDPC code and described the motivation of this paper in the first part. Then, we present the simulating results on parameter selection and architectural design. The primary contribution of this paper is summarized as follows: firstly, we proposed a novel and more efficient barrel shifter design. secondly, we optimized sub-modules architecture including: Bit Node Update, Check Node Update and combined and flexible data storage strategy so that this decoder can achieve both high data throughput and low resource-on-chip consumption.

## A non-linear LLR approximation for LDPC decoding over impulsive noise channels

- **Status**: ✅
- **Reason**: C: 임펄스(alpha-stable) 노이즈 채널용 비선형 LLR 근사 — LLR 계산 기법, NAND LLR 양자화에 참고 가능(애매하나 in)
- **ID**: ieee:7008248
- **Type**: conference
- **Published**: 13-15 Oct.
- **Authors**: Yi Hou, Rongke Liu, Ling Zhao
- **PDF**: https://ieeexplore.ieee.org/document/7008248
- **Abstract**: The performance of Low-Density Parity-Check codes over symmetric alpha-stable impulsive noise channels is considered in this paper. Due to the lack of closed-form expressions for the probability density functions of almost all the alpha-stable distributions, an efficient non-linear approximation method for channel log-likelihood ratio is presented to achieve high decoding performance covering the range of characteristic exponent from 1 to 2 and avoid the use of complicated numerical integrations. The simulations for both long and short codes show that the parameter selection of the proposed method is not sensitive to the noise level. Even fixed parameter setting for the proposed non-linear approximation can obtain a satisfying decoding performance.

## Matrix reordering techniques for memory conflict reduction for pipelined QC-LDPC decoder

- **Status**: ✅
- **Reason**: D: 파이프라인 QC-LDPC layered(TDMP) 디코더 메모리 충돌 감소 행렬 재배열 기법 — HW 이식 가능
- **ID**: ieee:7008301
- **Type**: conference
- **Published**: 13-15 Oct.
- **Authors**: Zhenzhi Wu, Dake Liu, Yanjun Zhang
- **PDF**: https://ieeexplore.ieee.org/document/7008301
- **Abstract**: Layered Decoding (LD) algorithm is widely applied in high throughput QC-LDPC decoders. Among all check node update algorithms in LD, Turbo-Decoding Message-Passing (TDMP) is adopted by many proposals. A-posteriori memory access conflict under pipelined TDMP decoder incurs serious throughput decline. In this paper, several matrix reordering techniques are introduced to reduce the conflict occurrences without incurring the performance loss, which includes Row Exchange method, element Sequence Reordering method, and a conflict detector with pipeline stall insertion. They are integrated in a joint recursive deep-first searching procedure. Test results show that the efficiency improvement reaches up to 60% compared to non-optimized scenarios for 802.11n and 802.16e standards.

## Irregular repeat-accumulate coded physical-layer network coding design for two-way relay channels

- **Status**: ❌
- **Reason**: 비이진(GF(q)) IRA 부호 + PNC 양방향 중계 설계, 비이진 LDPC 제외
- **ID**: ieee:7008249
- **Type**: conference
- **Published**: 13-15 Oct.
- **Authors**: Lei Yang, Tao Yang, Jinhong Yuan +1
- **PDF**: https://ieeexplore.ieee.org/document/7008249
- **Abstract**: We propose a new irregular repeat-accumulate (IRA) coded physical-layer network coding (PNC) scheme for Gaussian two-way relay channels (TWRCs). In the scheme, a same random-coset IRA code over GF(q) is employed at the two users, which directly maps the q-ary message sequences into coded q-PAM symbol sequences. The relay computes the network coded message sequence directly from the superimposed signal using an iterative belief propagation algorithm. By exploring the symmetry and permutation-invariance properties of the decoder's soft information distribution, a two-dimension extrinsic information transfer (EXIT) chart is developed to analyze and optimize the nonbinary IRA coded PNC scheme. Numerical results demonstrate that our developed scheme achieves near-capacity performance in Gaussian TWRCs.

## A Provable Secure Mutual RFID Authentication Protocol Based on Error-Correct Code

- **Status**: ❌
- **Reason**: QC-MDPC McEliece 기반 RFID 인증 보안 프로토콜, 채널 ECC 아니고 보안 도메인 제외
- **ID**: ieee:6984284
- **Type**: conference
- **Published**: 13-15 Oct.
- **Authors**: Zehui Li, Ruoqing Zhang, Yatao Yang +1
- **PDF**: https://ieeexplore.ieee.org/document/6984284
- **Abstract**: The security of radio frequency identification (RFID) has become an increasingly severe issue. We propose a mutual RFID authentication secure protocol, based on the QC-MDPC McEliece type public cryptography in order to protect the information interaction security in wireless channel of RFID system. It owns low storage of public key, perfect efficiency of encryption and decryption, and high security. The security proofed for this novel protocol was given by using the reduction method, and the hardness of attacking protocol was reduced to the decoding hard problem of the linear codes. The performance results also show that compared to other authentication protocols, this protocol is more feasible for RFID system which has low cost and high efficiency.

## A channel coder design for a novel high speed communication system

- **Status**: ❌
- **Reason**: QC/Random/Turbo 단순 비교, 신규 디코더/HW 기여 없음
- **ID**: ieee:7002412
- **Type**: conference
- **Published**: 10-11 Oct.
- **Authors**: Nivia George, A. N Neshma, K Nanditha +4
- **PDF**: https://ieeexplore.ieee.org/document/7002412
- **Abstract**: A technique used for controlling the errors in data transmission over a noisy channel is known as Channel coding. Low Density Parity Check(LDPC) codes and also Turbo codes approaches Shannon capacity limit. In this paper, the performance of Quasi Cyclic(QC) LDPC codes and Random LDPC codes are compared in terms of error. The code which is appropriate for hardware implementation in terms of structural complexity is identified here. The BER performances of QC-LDPC and Turbo codes are analysed. The channel coder which is more suitable for a high speed communication system is identified in this paper.

## Analysis of BER and energy efficiency of raptor codes under BEC for wireless sensor network

- **Status**: ❌
- **Reason**: Raptor 코드 BEC 에너지효율 분석(WSN) — fountain/erasure, LDPC는 baseline, 신규 ECC 기법 없음
- **ID**: ieee:7091647
- **Type**: conference
- **Published**: 1-3 Oct. 2
- **Authors**: V. Nithya, B. Ramachandran, S. Subashini
- **PDF**: https://ieeexplore.ieee.org/document/7091647
- **Abstract**: This paper has explored the energy efficiency of Raptor codes; a first known class of fountain codes in an energy constrained network. Transmission power is adjusted dynamically to overcome unreliability over lossy links in wireless sensor network. One of the most felicitous key for this reliability issue is using Forward Error Correction (FEC) codes. This paper investigates the energy bagged by one such FEC code called Raptor codes in the Binary Erasure Channel (BEC) scenario. The performance analysis of Raptor codes in terms of energy by varying its precoder is carried out. The network parameters such as Bit Error Rate (BER), Throughput and Energy Spent per Bit are considered for the study. The simulation results show that Raptor code with BCH code as a precoder improves the network lifetime over Raptor code alongside LDPC (Low Density Parity Check) code as a precoder by 88.24%.
