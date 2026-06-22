# IEEE Xplore — 2023-05 (1차선별 통과)


## LIAD: A Method for Extending the Effective Time of 3-D TLC NAND Flash Hard Decision

- **Status**: ✅
- **Reason**: 3D TLC NAND 직접: 추가 read 없이 sensing 결과로 LLR 보정하는 LIAD 연판정 기법 — 카테고리 A
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9878117
- **Type**: journal
- **Published**: May 2023
- **Authors**: Xiaolei Yu, Jing He, Qianhui Li +6
- **PDF**: https://ieeexplore.ieee.org/document/9878117
- **Abstract**: Triple-level cell NAND flash memory is widely used today due to its higher storage density and capacity. However, with the increase in the storage density, lower reliability results in more read times for flash memory and significantly reduces the read performance. In order to avoid unnecessary read operations, this article proposes a hard decision–soft decoding method called location information-assisted decoding (LIAD) method, which determines the additional information required for decoding by mutual information, and then transmits the required information to correct the log-likelihood ratio (LLR). Different from the conventional LLR correction algorithm, this method does not require additional read operations and correct data. Only using sensing results, our method can reduce uncorrectable error bit rate (UBER) by up to 99%, and the system read latency under SSDsim (Hu et al. 2011) simulation can be reduced by up to 53%.

## 3.8-Gbps Polar Belief Propagation Decoder on GPU

- **Status**: ✅
- **Reason**: D: GPU BP 디코더 병렬화 아키텍처, polar용이나 병렬 BP HW/소프트 최적화 기법을 LDPC BP 디코더로 이식 가능 (애매하나 살림)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:10086485
- **Type**: journal
- **Published**: May 2023
- **Authors**: Yuxing Chen, Xinyuan Qiao, Keyue Deng +2
- **PDF**: https://ieeexplore.ieee.org/document/10086485
- **Abstract**: In this work, a high-throughput belief propagation (BP) decoder of polar codes on graphics processing unit (GPU) is proposed for software-defined communication systems. The decoder is jointly optimized from algorithm and architecture aspects. From the algorithm aspect, the storage pattern and computation flow are optimized to reduce complexity. From the architecture aspect, different granularities of parallelism are extensively exploited to achieve high throughput. Equipped with these techniques, a high-speed GPU-based BP decoder is developed, and experimental results show that the proposed decoder can improve the normalized throughput by 64.1% to 294.1% compared to the state-of-the-art GPU-based BP decoder.

## A Simplified Soft-output MLSE Concatenated with LDPC Decoding in 112-Gb/s PAM-4 Transmissions

- **Status**: ✅
- **Reason**: 간소화 soft-output MLSE를 LDPC 디코딩과 연접, 복잡도 49.6% 감축 — 연접 디코딩 구조가 NAND LDPC에 이식 가능성 있어 Phase3 재검토(애매하면 in).
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10260100
- **Type**: conference
- **Published**: 7-12 May 2
- **Authors**: Xue Zhao, Jiahao Zhou, Jing Zhang +4
- **PDF**: https://ieeexplore.ieee.org/document/10260100
- **Abstract**: We propose and experimentally demonstrate a simplified soft-output MLSE and LDPC decoding in a 112-Gb/s PAM-4 signal transmission over 2-km SSMF. We achieve almost the same performance as conventional soft-output MLSE with 49.6% complexity reduce.

## Optimization Strategies for Low-Latency 5G NR LDPC Decoding on General Purpose Processor

- **Status**: ✅
- **Reason**: 5G LDPC 소프트웨어 디코더 GPP 최적화(AVX-512/unrolling) — 디코더 구현 가속 기법 이식 가능(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:10165378
- **Type**: conference
- **Published**: 19-21 May 
- **Authors**: Mody Sy
- **PDF**: https://ieeexplore.ieee.org/document/10165378
- **Abstract**: In recent years, with the progression of the computational abilities of General-Purpose Processors (GPPs), there has been a heightened interest in the implementation of software Low-Density Parity-Check (LDPC) decoders. This investigation provides a comprehensive analysis of the most effective strategies for optimizing the decoding latency of 5G LDPC on GPPs. Our proposed optimization mechanisms consist of the implementation of Advanced Vector Extensions 512 (AVX-512) instructions in computationally intensive routines and the application of code transformation techniques, specifically optimization through unrolling to tackle the primary computational challenges and minimize the overall latency of the decoder. To assess the efficiency of our proposed techniques, thorough simulations were carried out to determine the decoding time. Our findings indicate that the implementation of the aforementioned optimization techniques on computational routines causing time bottlenecks can lead to a significant reduction of at least 30% in computational delay, even under unfavorable conditions. This discovery demonstrates the feasibility of developing a low-latency software 5G NR LDPC decoder on an x86 architecture.

## A Second Minimum Approximation Method for Layered Min-Sum Decoding of QC-LDPC Codes

- **Status**: ✅
- **Reason**: QC-LDPC layered min-sum의 single-min 기반 제2최소값 근사 신규 기법 — 디코더 알고리즘(C) NAND 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10154580
- **Type**: conference
- **Published**: 17-19 May 
- **Authors**: Zijian Qin, Yangcan Zhou, Zhongfeng Wang
- **PDF**: https://ieeexplore.ieee.org/document/10154580
- **Abstract**: Low-density parity-check (LDPC) codes have attracted tremendous attention for their excellent error-correction performance and inherent fitness for high-parallelism implementation. With great complexity reduction and friendly for hardware implementation, the min-sum (MS) decoding algorithm for LDPC codes gains widespread applications in practical. In the MS decoding algorithm, finding the first two minima among input variable-to-check messages is the most complex part. To further reduce the complexity of the MS decoding algorithm, an efficient single-minimum (single-min) based layered MS decoding for quasi-cyclic LDPC (QC-LDPC) codes is proposed in this paper. It is found that statistically the difference between the first minimum and second minimum increases as the decoding becomes more convergent. Accordingly, in the proposed single-min scheme, the second minimum is approximately derived based on the first minimum and an index indicating the convergence degree. Besides, some other metrics that are easily obtained are used to refine the second minimum. Simulation results show that the proposed method can significantly improve the error-correction performance and lower the average number of iterations, compared with the state-of-the-art single-min based MS decoding algorithms.

## Construction and Performance Evaluation of QC-LDPC Codes With Low Error Floor

- **Status**: ✅
- **Reason**: 낮은 error floor QC-LDPC 구성 + harmful substructure 탐색 알고리즘 신규 제안 — 코드설계(E) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10154643
- **Type**: conference
- **Published**: 17-19 May 
- **Authors**: Ying Wang, Xiaojian Liu, Ming Jiang +1
- **PDF**: https://ieeexplore.ieee.org/document/10154643
- **Abstract**: In the paper, we propose a novel construction method for quasi-cyclic (QC) low-density parity-check (LDPC) codes with lower error floor. This approach aims at eliminating the most harmful substructures by choosing proper shift values for cyclic permutation matrices (CPM). To search these harmful substructures, we introduce a high-efficiency searching algorithm, based on cycle combination and leaf cutting. In addition, a high throughput decoding platform based on multi-core CPU with SIMD instruction sets are implemented and utilized to reach the error floors of different LDPC codes efficiently. Simulation results show that for given base matrices, our method can achieve excellent performance in the high SNR region.

## A Study on Accelerating SP decoding by Neural Network in SMR System

- **Status**: ✅
- **Reason**: SMR/HDD 스토리지 SP 디코더에 신경망 적용해 반복 가속 — 이식 가능 NN 디코더(C)+스토리지(B)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10228247
- **Type**: conference
- **Published**: 15-19 May 
- **Authors**: Madoka Nishikawa, Yasuaki Nakamura, Yasushi Kanai +1
- **PDF**: https://ieeexplore.ieee.org/document/10228247
- **Abstract**: We have previously studied low-density parity-check (LDPC) coding and iterative decoding in shingled magnetic recording (SMR) system as a signal processing method to realize ultra-high-density hard disk drive (HDD). In addition, we have proposed the application of the neural network to improve decoding performance and realize the automation of iterative decoding. In this study, we apply a neural network to accelerate iterative decoding in the sum-product (SP) decoder. As the result, the SP decoder with the neural network realized "no errors" at the fewest times of the iterative decoding compared to our previous studies.

## An adjustable decoding scheme for robust and efficient transmission in FTTR C-WAN architecture

- **Status**: ✅
- **Reason**: 채널상태 기반 LDPC 디코딩 조정+OMS로 반복횟수/복잡도 절감, 이식 가능 디코더 기법(C) 소지
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10277087
- **Type**: conference
- **Published**: 14-17 May 
- **Authors**: Zhihao Chen, Fuzhou Peng, Xiang Chen
- **PDF**: https://ieeexplore.ieee.org/document/10277087
- **Abstract**: This paper investigates an effective adjustment scheme of the LDPC decoding algorithm according to the channel states in the Fiber-to-the-Room (FTTR) system with Centralized/Cloud Wireless-optical Access Network (C-WAN) architecture. The family scenarios of Distributed-MIMO (D-MIMO) channels of 5GHz Wi-Fi are measured and analyzed. According to the proposed scheme, the gain brought by the C-WAN architecture is transformed to the decrease of computation and time complexity of LDPC algorithm, which matches burst transmission character of Wi-Fi system. Simulations and experiments show that D-MIMO technology certainly improves the performance of family network system and an average 3dB gain of Signal-to-Noise ratio (SNR) is achieved. When using the Offset Min-Sum (OMS) algorithm, the LDPC decoding performance can approach the Belief Propagation (BP) algorithm at lower complexity, which also can improve the throughput of LDPC by reducing the number of iterations.

## Low Complexity Log Likelihood Ratio Estimation Algorithm Based on Neural Network in Decoding

- **Status**: ✅
- **Reason**: C - 신경망 기반 저복잡도 LLR 추정 알고리즘, 부호 비의존적이며 NAND LDPC 디코더의 LLR 계산에 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10211434
- **Type**: conference
- **Published**: 12-15 May 
- **Authors**: Yuqing Zhang, Yiqun Pan, Qinghua Tian +4
- **PDF**: https://ieeexplore.ieee.org/document/10211434
- **Abstract**: This paper proposes a low complexity algorithm for calculating the soft decision metric of forward error correction codes. In order to reduce the complexity of LLR calculation, neural network training can be used to fit the relationship between input and output during exact LLR calculation. The trained network can skip the complex training process and directly estimate the LLR value. We use random signal-to-noise ratio (SNR) and received signals as the input layer of the neural network, and use the precisely calculated soft decision information as the output layer of the network. After training, the network can accurately estimate the LLR of the received symbols. The performance of 16QAM and 64QAM transmission system using the proposed algorithm and the exact LLR calculation algorithm in the AWGN channel with polar code as the encoding algorithm are presented, respectively. The simulation results show that the proposed algorithm has a similar bit error rate performance to traditional exact calculation algorithms, but with much lower complexity. The proposed algorithm can be applied in various decoding situations that require LLR calculation.

## Quasi-cyclic Concatenated Spatially Coupled LDPC Codes Based Joint Source-Channel Coding

- **Status**: ✅
- **Reason**: E - SC-LDPC QC 구성, 저장친화적 base matrix + QC 확장법(랜덤 대비 HW 저장 효율). 바이너리 LDPC 코드설계로 NAND에 이식 가능. JSCC 맥락이나 구성기법 분리 가능 → 애매하여 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10217292
- **Type**: conference
- **Published**: 12-14 May 
- **Authors**: Yupeng Li, Lin Zhou, Qiwang Chen +2
- **PDF**: https://ieeexplore.ieee.org/document/10217292
- **Abstract**: This paper investigates the quasi-cyclic construction method for Joint Source-Channel Coding (JSCC) based on Spatially Coupled Low-Density Parity-Check (SC-LDPC) codes. For existing source and channel matrix construction methods, their structures are simple, and to achieve a low overall error rate, random construction is generally used for the expansion matrix. However, in practical hardware implementation, this method is not conducive to data storage and retrieval. To alleviate these effects, a readily-stored base matrix construction and quasi-cyclic expansion method is proposed, which achieves a trade-off between error rate performance and storage complexity with given code rate and other basic parameters, and has a certain degree of flexibility. In simulations, the proposed quasi-cyclic construction method with easy storage shows improved error rate performance compared to existing construction methods, and the difference in error rate performance compared to similar structures that sacrifice more storage space for random construction is within an acceptable range.
