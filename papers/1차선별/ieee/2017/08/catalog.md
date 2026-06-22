# IEEE Xplore — 2017-08 (1차선별 통과)


## GPU-Based Gigabit LDPC Decoder

- **Status**: ✅
- **Reason**: D: GPU 기반 병렬 LDPC 디코더 구현/최적화, 고처리량 — HW/병렬화 아키텍처 이식 가능
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:7927704
- **Type**: journal
- **Published**: Aug. 2017
- **Authors**: Selcuk Keskin, Taskin Kocak
- **PDF**: https://ieeexplore.ieee.org/document/7927704
- **Abstract**: In this letter, we present design and implementation of a parallel software low-density parity-check (LDPC) decoding algorithm on graphics processing units (GPUs). As a solution for the LDPC decoder, dedicated application-specific integrated circuit or field programmable gate array implementations is proposed in recent years in order to support high throughput despite their long deployment cycle, high design, and especially fixed functionalities. On the other hand, the implementations on GPU as a software solution provide flexible, scalable, and less expensive solutions in a shorter deployment cycle. We present some GPU-based optimizations for a major LDPC decoder algorithm to obtain high throughput in digital communication systems. Experimental results demonstrate that the proposed LDPC decoder achieves more than 1.27 Gb/s peak throughput on a single GPU.

## Thresholds of Absorbing Sets in Low-Density Parity-Check Codes

- **Status**: ✅
- **Reason**: C/E: 바이너리 LDPC absorbing set의 min-sum 고정소수점 threshold 신규 분석, error floor — 디코더/코드설계 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7934127
- **Type**: journal
- **Published**: Aug. 2017
- **Authors**: Alessandro Tomasoni, Sandro Bellini, Marco Ferrari
- **PDF**: https://ieeexplore.ieee.org/document/7934127
- **Abstract**: The error floor phenomenon in many low-density parity-check (LDPC) codes is caused by combinatorial objects in their Tanner graph, known as absorbing sets. In this paper, we highlight a threshold behavior for the min-sum decoding algorithm in the graph of an absorbing set with fixed-point representation of messages. For an absorbing set of interest in a binary LDPC code we can compute the threshold, a novel real-valued parameter that is closely related to its harmfulness. We show that absorbing sets with negative thresholds cannot trap the decoder if the dynamic range of the extrinsic messages is large enough. We also prove that, in regular LDPC codes, absorbing sets with negative thresholds exist if the variable node degree is odd. The examples presented in this paper show that odd-column-weight LDPC codes can have many absorbing sets with negative thresholds, but that these absorbing sets do not trap a well-designed decoder. Simulations show a good agreement between the results of the analysis presented in this paper and the performance of practical decoders with fixed-point messages.

## Selection of Parity Check Equations For the Iterative Message-Passing Detection of M-Sequences

- **Status**: ✅
- **Reason**: Tanner 그래프 6/8-cycle 수 최소화로 패리티검사식 선별하는 알고리즘 — absorbing set·error floor 관련 코드설계 기법(E)으로 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7932177
- **Type**: journal
- **Published**: Aug. 2017
- **Authors**: Mathieu des Noes, Valentin Savin, Laurent Ros +1
- **PDF**: https://ieeexplore.ieee.org/document/7932177
- **Abstract**: We consider the joint detection and decoding of m-sequences. The receiver has to decide whether an m-sequence is received and possibly to decode its initial state. To do so, it implements an iterative message-passing decoding algorithm that operates on a parity check matrix, built upon a number of reference parity-check equations satisfied by the m-sequence. This matrix concatenates several elementary parity check matrices which are derived from reference equations. Unlike the conventional decoding case, the detection problem imposes to consider false alarms that may occur when the decoder is only fed with noise. While absorbing sets are known to be responsible for the error floor phenomenon of iterative message-passing decoders, we show that they may have a beneficial effect on the detection performance, in that they may prevent the decoder to produce false alarms. We further compute the number of hybrid cycles of length six and eight in the Tanner graph of the decoder and use the minimization of this number as criterion to derive an algorithm for selecting the reference parity check equations. This algorithm was found to be efficient for minimizing the probability of false alarm and decreases also the probability of wrong detection in the very small SNR region. This has been achieved at the cost of a reduction of the probability of correct detection.

## Mitigating Stuck Cell Failures in MLC NAND Flash Memory via Inferred Erasure Decoding

- **Status**: ✅
- **Reason**: A/C: MLC NAND 직접, stuck cell을 erasure로 추론하는 신규 ISED BP 디코더+LLR 감쇠 기법 — NAND LDPC 직접 이식
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7889015
- **Type**: journal
- **Published**: Aug. 2017
- **Authors**: Adnan Aslam Chaudhry, Cai Kui, Yong Liang Guan
- **PDF**: https://ieeexplore.ieee.org/document/7889015
- **Abstract**: The multilevel-cell NAND flash memory experiences permanent hard errors due to cell defects (stuck cells). To overcome this problem, stuck cells are either regarded as erasures by the decoder based upon the knowledge of stuck cell location, or the entire memory block containing the stuck cells is marked as bad block and made unavailable for future usage. In this paper, a multiround inferred stuck-cell erasure belief-propagation (BP) decoding (ISED) is proposed in which the stuck cell locations are assumed to be unknown to the decoder. To perform the inferred erasure decoding, the input channel log-likelihood ratio (LLR) information is attenuated before BP decoding by modifying the threshold voltage distribution functions. In case of decoding failure, the probable stuck cell locations are inferred by using the flash's read-back voltage signal and the decoded code-word bits. For all such inferred stuck cells, the input LLRs are set to zero for subsequent rounds of BP decoding. As the likely incorrect LLRs corresponding to the stuck cells are erased, the performance of BP decoder is substantially improved. Simulation results show that the error-rate performance is improved by more than two orders of magnitude with a moderate increase in decoding complexity under the proposed ISED scheme.

## Special session: Low power LDPC deocder using adaptive forced convergence algorithm

- **Status**: ✅
- **Reason**: adaptive forced convergence로 VN/CN 비활성화하는 저복잡도 LDPC 디코더 알고리즘(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8052922
- **Type**: conference
- **Published**: 6-9 Aug. 2
- **Authors**: JeongHyeon Bae, Byung Jun Choi, Myung Hoon Sunwoo
- **PDF**: https://ieeexplore.ieee.org/document/8052922
- **Abstract**: LDPC codes have been applied in recent communication standards, such as WiFi, WiGig, and 10GBased-T Ethernet as a forward error correction code. However, LDPC codes require a large number of computational complexity for high performances. To solve this problem, various studies have been continuously performed for reducing computational complexity. In this paper, we propose an adaptive forced convergence algorithm to deactivate the variable nodes and check nodes for reducing the computational complexity using only one adaptive threshold value.

## A high-performance FPGA-based LDPC decoder for solid-state drives

- **Status**: ✅
- **Reason**: SSD용 FPGA 반병렬 QC-LDPC 디코더 아키텍처+adaptive normalization(A/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8053152
- **Type**: conference
- **Published**: 6-9 Aug. 2
- **Authors**: Yanhuan Liu, Chun Zhang, Pengcheng Song +1
- **PDF**: https://ieeexplore.ieee.org/document/8053152
- **Abstract**: In order to improve the throughput of error correction decoding for the high-performance solid-state drives (SSDs), a semi-parallel low-density parity-check (LDPC) decoding architecture is proposed in this paper. The circuit of the LDPC decoder which can be dynamically configured with bit rate and code length is implemented using the scheduling control flow mode of single instruction multiple data (SIMD) instruction. The Peripheral Component Interconnect Express (PCIe) interface is designed and the adaptive normalization factor is applied to achieve an average improvement of 35% in throughput with a signal-to-noise ratio (SNR) of 6.08 dB. The LDPC decoder is implemented on the Xilinx VC709 FPGA. With a rate-0.94 length-35840 quasi-cyclic LDPC code, the decoder achieves a throughput of 1.97 Gb/s which compares favorably with previously proposed architectures.

## Irregular QC-LDPC based multi-level coded modulation scheme for the next generation optical communication systems

- **Status**: ✅
- **Reason**: EXIT chart 기반 irregular QC-LDPC 코드 구성 최적화 — 바이너리 QC-LDPC 코드설계(E) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8114859
- **Type**: conference
- **Published**: 31 July-4 
- **Authors**: Dongdong Wang, Liqian Wang, Xue Chen +5
- **PDF**: https://ieeexplore.ieee.org/document/8114859
- **Abstract**: In this paper, we mainly focus on the optimization of multi-level coded modulation scheme in terms of sub-channel code rate optimal assignment and irregular QC-LDPC code construction with the aid of EXIT chart analysis. Simulation results show that the proposed MLCM scheme can achieve additional 0.1dB NCG compared with the UEP coded modulation scheme.

## Multi-Mode Low-Latency Software-Defined Error Correction for Data Centers

- **Status**: ✅
- **Reason**: 플래시 메모리용 적응형 ECC, hard/soft LDPC 디코더(BF+BP) 조합 및 FPGA 구현 — NAND 직접(A)+디코더(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8038467
- **Type**: conference
- **Published**: 31 July-3 
- **Authors**: Fakhreddine Ghaffari, Ali Akoglu, Bane Vasic +1
- **PDF**: https://ieeexplore.ieee.org/document/8038467
- **Abstract**: Flash memories are gaining prominence for utilizing in large scale data centers (DCs) due to their high memory density, low power consumption and heat dissipation, and high access speed characteristics. The rate of degradation for a flash memory is largely affected by the amount and frequency of the erase/write operations, which is a challenge in the DC context that serves dynamically changing workloads. Adaptive Error Correction Code (AECC) schemes have been introduced for changing the error correction algorithm based on the reliability state of the flash. In this study we show that hard decision (bit-flipping) and soft decision decoding (Belief Propagation) class of algorithms for Low Density Parity Check (LDPC) decoders complement each other for utilizing in the flash based DCs in order to meet the dynamically changing reliability level. We propose a new family of ECC to improve the reliability of flash memory. Our Monte-Carlo simulations and Field Programmable Gate Array (FPGA) based hardware implementation analysis show that LDPC decoders are suitable for balancing the throughput, decoding performance and reliability requirements in DCs.

## Complexity-constrained spatially coupled LDPC codes based on protographs

- **Status**: ✅
- **Reason**: E: protograph 기반 SC-LDPC 구성 + sliding window 디코더 복잡도-성능 트레이드오프(PEXIT) — 바이너리 코드설계/디코더 기법 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8108160
- **Type**: conference
- **Published**: 28-31 Aug.
- **Authors**: Massimo Battaglioni, Marco Baldi, Enrico Paolini
- **PDF**: https://ieeexplore.ieee.org/document/8108160
- **Abstract**: Spatially coupled low-density parity-check (SC-LDPC) codes are often thought as codes with very long block lengths. However, they can be decoded through sliding window (SW) decoders achieving near-optimal performance when the window size is a few times larger than the code syndrome former constraint length. This makes SC-LDPC codes with short constraint length suitable for low-latency transmissions, and they can even outperform their block code counterparts. Complexity of SW decoders increases linearly with the window size and with the number of decoding iterations. When complexity is constrained, an optimal trade-off between the window size and the maximum number of decoding iterations has to be found. In this paper, we propose a PEXIT-based method to find the best trade-off for codes with short syndrome former constraint length. We consider codes based on protographs, and validate the results of the PEXIT-based method through Monte Carlo simulations.

## A merged BP decoding algorithm for polar-LDPC concatenated codes

- **Status**: ✅
- **Reason**: polar-LDPC 연접 부호의 merged BP 복호 알고리즘으로 인자그래프 결합 기반 BP 개선, 부호 비의존 메시지패싱 기법으로 바이너리 LDPC BP 이식 여지(C), 애매하여 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8096145
- **Type**: conference
- **Published**: 23-25 Aug.
- **Authors**: Jiaai Liu, Shusen Jing, Xiaohu You +1
- **PDF**: https://ieeexplore.ieee.org/document/8096145
- **Abstract**: Recently, both polar codes and low-density parity-check (LDPC) codes have been adopted by 3GPP eMBB scenario. Since both codes exist in one system, it is natural to consider the concatenation scheme of them. In this paper, a merged belief propagation (BP) decoding algorithm for the concatenated codes of polar and LDPC codes is proposed. By jointing factor graphs, this merged algorithm is designed by serially executing the LDPC and polar decoding. According to numerical results, the bit error rate (BER) of this proposed algorithm can achieve a notable improvement for different code rates compared with the conventional separated approach. For (1024, 512) polar code, the performance gain of the proposed scheme is at least 0 5 dB even at a low BER of 1 × 10-2. Finally, further refinements of computational complexity and hardware implementation are also provided in this paper.

## Enhancing SSD performance with LDPC-aware garbage collection

- **Status**: ✅
- **Reason**: A) SSD에서 LDPC read 지연 고려한 garbage collection; NAND/SSD 직접 컨트롤러 기법
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8064481
- **Type**: conference
- **Published**: 16-18 Aug.
- **Authors**: Yajuan Du, Yunpei Jia, Meng Zhang +2
- **PDF**: https://ieeexplore.ieee.org/document/8064481
- **Abstract**: With the technology scaling of solid state drives (SSDs), data reliability has to be ensured by advanced Low-Density Parity-Check (LDPC) codes. As LDPC reads often take high latency, read performance involved in traditional garbage collection, called external GC, is largely decreased, which affects system performance. GC can choose not to correct data with LD-PC codes but just copy valid pages into registers of NAND flash, which we call internal GC. Although this method avoids long latency in LDPC reads, the data integrity is sacrificed because of error aggregation in valid pages. To balance performance and reliability, this paper proposes a new garbage collection method, named as LDPC-aware Garbage Collection (LaGC), to selectively choose blocks with high error rates to perform external GC. These blocks are often close to uncorrectable error rates, which take a small portion during a long flash life period. Thus, most of blocks perform internal GC and keep advantage of low read latency. Experimental results show that LaGC can reduce 78% of read latency in external GC and achieve about 2% system performance improvement.

## A comparison and simulation of LDPC decoders for Chinese digital television multimedia broadcasting(CDTMB) standard

- **Status**: ✅
- **Reason**: min-sum 변형(SSMSD/NSSMSD) 메모리·연산 절감 디코더 비교 — 이식 가능 디코더(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8389609
- **Type**: conference
- **Published**: 1-2 Aug. 2
- **Authors**: Vijaykumar T. Korishetti, V. Jayashree, V. C. Patil
- **PDF**: https://ieeexplore.ieee.org/document/8389609
- **Abstract**: For the last 20 years intense research has been carried out on Low Density Parity Check(LDPC) decoders for supporting various transmission technologies. There are various proven LDPC decoder algorithms such as Log domain sum product algorithm(LDSPA), Min sum decoder(MSD), Single scan min sum decoder(SSMSD) and normalized single scan min sum decoder(NSSMSD) which are currently in use. Each of these algorithm have its own distinct pros and cons from implementation point of view that comes to support various transmission standards. In this paper four LDPC decoding algorithms are implemented to test and support CDTMB standard for its three code rates viz. 0.4, 0.6 and 0.8. The performance evaluation of all four decoder algorithms mentioned above are carried out with Additive White Gaussian Noise(AWGN) channel with BPSK modulation scheme. The software implementation of these algorithms show that min sum decoder algorithm reduces complexity when compared to LDSPA. Also SSMSD and NSSMSD contributes to conservation of memory to 23% and take at least 35% less computation time compared to LDSPA and MSD. LDSPA is preferred for low data rate applications for its good BER performance, but it has the drawback of increase in hardware complexity due to the presence of tanh and log functions. SSMSD and NSSMSD is preferable for high data rate applications as this showed low memory requirement and faster performance.
