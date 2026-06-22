# IEEE Xplore — 2017-08


## Asymmetric Spatially Coupled LDPC Codes for Multiple-Burst Erasure Channels

- **Status**: ❌
- **Reason**: SC-LDPC 비대칭 결합으로 다중버스트 erasure 개선이나 채널 메모리/버스트 특화 — NAND에 이식할 신규 디코더/구성 기여 약함, 애매하나 응용 특이적
- **ID**: ieee:7922520
- **Type**: journal
- **Published**: Aug. 2017
- **Authors**: Zhaoji Zhang, Ying Li
- **PDF**: https://ieeexplore.ieee.org/document/7922520
- **Abstract**: The outstanding performances of spatially coupled low-density parity-check (SC-LDPC) codes deteriorate over the channels with memory due to burst erasures. In order to improve the performances of SC-LDPC codes over multiple-burst erasure channels, an asymmetric spatial coupling (ASC) structure is proposed, where each variable node at the same position of the coupled protograph can flexibly choose its coupling width. It is shown that the base matrices of the proposed ASC-LDPC codes possess larger minimal cardinality of stopping sets, which is beneficial to the multiple-burst erasure correcting capability of SC-LDPC codes. Simulation results further demonstrate that, aided by the ASC structure, the performances of SC-LDPC codes can be greatly improved over multiple-burst erasure channels.

## GPU-Based Gigabit LDPC Decoder

- **Status**: ✅
- **Reason**: D: GPU 기반 병렬 LDPC 디코더 구현/최적화, 고처리량 — HW/병렬화 아키텍처 이식 가능
- **ID**: ieee:7927704
- **Type**: journal
- **Published**: Aug. 2017
- **Authors**: Selcuk Keskin, Taskin Kocak
- **PDF**: https://ieeexplore.ieee.org/document/7927704
- **Abstract**: In this letter, we present design and implementation of a parallel software low-density parity-check (LDPC) decoding algorithm on graphics processing units (GPUs). As a solution for the LDPC decoder, dedicated application-specific integrated circuit or field programmable gate array implementations is proposed in recent years in order to support high throughput despite their long deployment cycle, high design, and especially fixed functionalities. On the other hand, the implementations on GPU as a software solution provide flexible, scalable, and less expensive solutions in a shorter deployment cycle. We present some GPU-based optimizations for a major LDPC decoder algorithm to obtain high throughput in digital communication systems. Experimental results demonstrate that the proposed LDPC decoder achieves more than 1.27 Gb/s peak throughput on a single GPU.

## An Expurgating-Based Method for Constructing Multi-Rate Non-Binary Quasi-Cyclic LDPC Codes

- **Status**: ❌
- **Reason**: 비이진(non-binary) QC-LDPC 구성 — 바이너리 한정 기준에 따라 제외
- **ID**: ieee:7926396
- **Type**: journal
- **Published**: Aug. 2017
- **Authors**: Xijin Mu, Gang Chen, Baoming Bai
- **PDF**: https://ieeexplore.ieee.org/document/7926396
- **Abstract**: This letter presents a new method for constructing the multi-rate non-binary quasi-cyclic low-density parity-check codes by expurgating a high-rate mother code. A matrix-theoretic approach is applied to design the parity-check matrices of the proposed codes. The resulting codes possess a quasi-cyclic structure, which is desirable for hardware implementations of the encoder and decoder. The codes can also be encoded directly with parity-check matrices due to the block dual-diagonal structure. Simulation results show that the codes can achieve good performance within a wide range of code rates both in the waterfall region and in the error-floor region.

## Thresholds of Absorbing Sets in Low-Density Parity-Check Codes

- **Status**: ✅
- **Reason**: C/E: 바이너리 LDPC absorbing set의 min-sum 고정소수점 threshold 신규 분석, error floor — 디코더/코드설계 이식 가능
- **ID**: ieee:7934127
- **Type**: journal
- **Published**: Aug. 2017
- **Authors**: Alessandro Tomasoni, Sandro Bellini, Marco Ferrari
- **PDF**: https://ieeexplore.ieee.org/document/7934127
- **Abstract**: The error floor phenomenon in many low-density parity-check (LDPC) codes is caused by combinatorial objects in their Tanner graph, known as absorbing sets. In this paper, we highlight a threshold behavior for the min-sum decoding algorithm in the graph of an absorbing set with fixed-point representation of messages. For an absorbing set of interest in a binary LDPC code we can compute the threshold, a novel real-valued parameter that is closely related to its harmfulness. We show that absorbing sets with negative thresholds cannot trap the decoder if the dynamic range of the extrinsic messages is large enough. We also prove that, in regular LDPC codes, absorbing sets with negative thresholds exist if the variable node degree is odd. The examples presented in this paper show that odd-column-weight LDPC codes can have many absorbing sets with negative thresholds, but that these absorbing sets do not trap a well-designed decoder. Simulations show a good agreement between the results of the analysis presented in this paper and the performance of practical decoders with fixed-point messages.

## Selection of Parity Check Equations For the Iterative Message-Passing Detection of M-Sequences

- **Status**: ✅
- **Reason**: Tanner 그래프 6/8-cycle 수 최소화로 패리티검사식 선별하는 알고리즘 — absorbing set·error floor 관련 코드설계 기법(E)으로 이식 가능
- **ID**: ieee:7932177
- **Type**: journal
- **Published**: Aug. 2017
- **Authors**: Mathieu des Noes, Valentin Savin, Laurent Ros +1
- **PDF**: https://ieeexplore.ieee.org/document/7932177
- **Abstract**: We consider the joint detection and decoding of m-sequences. The receiver has to decide whether an m-sequence is received and possibly to decode its initial state. To do so, it implements an iterative message-passing decoding algorithm that operates on a parity check matrix, built upon a number of reference parity-check equations satisfied by the m-sequence. This matrix concatenates several elementary parity check matrices which are derived from reference equations. Unlike the conventional decoding case, the detection problem imposes to consider false alarms that may occur when the decoder is only fed with noise. While absorbing sets are known to be responsible for the error floor phenomenon of iterative message-passing decoders, we show that they may have a beneficial effect on the detection performance, in that they may prevent the decoder to produce false alarms. We further compute the number of hybrid cycles of length six and eight in the Tanner graph of the decoder and use the minimization of this number as criterion to derive an algorithm for selecting the reference parity check equations. This algorithm was found to be efficient for minimizing the probability of false alarm and decreases also the probability of wrong detection in the very small SNR region. This has been achieved at the cost of a reduction of the probability of correct detection.

## ABER Performance of LDPC-Coded OFDM Free-Space Optical Communication System Over Exponentiated Weibull Fading Channels With Pointing Errors

- **Status**: ❌
- **Reason**: FSO-OFDM 무선광통신 ABER 분석, LDPC는 부수적 적용일 뿐 떼어낼 디코더·구성·HW 신규 기법 없음
- **ID**: ieee:7968273
- **Type**: journal
- **Published**: Aug. 2017
- **Authors**: Xiaoxia Liu, Ping Wang, Tao Liu +3
- **PDF**: https://ieeexplore.ieee.org/document/7968273
- **Abstract**: A low-density parity-check (LDPC)-coded free space optical (FSO) orthogonal frequency-division multiplexing (OFDM) communication system over aggregated exponentiated Weibull (EW) fading channels with pointing errors considered is investigated. On the basis of the probability density function and cumulative distribution function of the composite channel gain, the analytical expressions of average bit error rate (ABER) of this FSO-OFDM system with on–off keying, K-ary quadrature amplitude modulation (QAM) and phase shift keying (PSK) modulation schemes are derived by using generalized Gauss–Lagurre quadrature rule, respectively. Monte Carlo simulations are provided to verify the validity of these three expressions. Furthermore, LDPC codes are applied in the simulation to improve the ABER performance. The results show that the ABER performance of 16-QAM-OFDM is better than that of the 16-PSK-OFDM system over composite EW fading channels, regardless of the turbulence strengths. For the modulation schemes involved, the degradation due to the increase of atmospheric turbulence strength for turbulence only scenario is more severe when compared with pointing errors included case. The study also demonstrates that significant coding gain improvement can be achieved by LDPC codes over EW fading channels, especially under strong turbulence condition. With pointing errors, more coding gain can be obtained when the jitter increases or beamwidth decreases.

## A Low-Complexity Multiuser Coding Scheme With Near-Capacity Performance

- **Status**: ❌
- **Reason**: 다중접속용 IRA(repetition-aided) 코드+다중사용자 복호, 무선 MAC 응용 특이적이며 NAND LDPC BP로 떼어낼 신규 기법 없음
- **ID**: ieee:7812743
- **Type**: journal
- **Published**: Aug. 2017
- **Authors**: Guanghui Song, Xianbin Wang, Jun Cheng
- **PDF**: https://ieeexplore.ieee.org/document/7812743
- **Abstract**: Nonorthogonal multiuser coding is an essential technique for superimposed transmission and improving spectrum efficiency of future wireless communication networks. In this paper, a low-complexity nonorthogonal coding scheme, called multiuser repetition-aided irregular repeat-accumulate (IRA) code, is proposed for a multiple access channel (MAC), and the scheme can be applied to fifth-generation (5G) nonorthogonal multiple access systems. The main idea is that not only parity checks, which are generated by an IRA encoder, but repetitions as well, are used in each user's codeword to reduce the coding and decoding complexities. Repetition is a simple way to construct a low-rate code and is shown to be beneficial for multiuser decoding iteration. With a deliberate control of the fraction of repetitions in the codeword and a degree distribution optimization of the IRA encoder, near MAC capacity performance is achieved. It is shown that as the number of users increases, more repetitions can be used, and therefore, very low encoding and decoding complexities are required.

## Binary Compressive Tracking

- **Status**: ❌
- **Reason**: LDPC 행렬을 압축 센싱(space encoding)에 사용한 트래킹 프레임워크 — 채널 ECC가 아니고 떼어낼 디코더/HW/코드설계 기법 없음
- **ID**: ieee:7859302
- **Type**: journal
- **Published**: Aug. 2017
- **Authors**: Jiang Lu, Ting Zhang, Qingquan Sun +2
- **PDF**: https://ieeexplore.ieee.org/document/7859302
- **Abstract**: This paper presents a compressive tracking framework using distributed binary sensors. The goal of this research is to achieve the minimum data throughput for an accurate multitarget tracking system through novel spatial sampling schemes. The framework consists of two main components: space encoding and measurement decoding. The space encoding scheme is based on the low-density parity-check matrix, which converts k-sparse target position vectors into different codewords. The measurement decoding scheme contains linear-programming-based localization and graphical-model-based tracking algorithms, which converts codewords into the states of multiple targets. A posterior Cramer-Rao bound analysis is utilized to achieve the tradeoff between the compression ratio of measurements and the accuracy of the tracking system. Simulation and experimental results are provided to validate the proposed framework.

## Allocating Redundancy Between Erasure Coding and Channel Coding When Fading Channel Diversity Grows With Codeword Length

- **Status**: ❌
- **Reason**: erasure코딩 vs 채널코딩 전력/redundancy 배분 최적화 — 페이딩채널 응용 특이적, 떼어낼 디코더/구성 기법 없음
- **ID**: ieee:7932129
- **Type**: journal
- **Published**: Aug. 2017
- **Authors**: Sudarsan V. S. Ranganathan, Tong Mu, Richard D. Wesel
- **PDF**: https://ieeexplore.ieee.org/document/7932129
- **Abstract**: A transmitter sends a packetized message over a fading channel using packet-level erasure coding and physical-layer channel coding of each resultant packet. Given an overall code rate, this paper finds the optimal rates of the erasure code and the channel code to minimize the transmit power required for a certain message error probability. This paper considers a practically important fading model in which the number of block fades in a transmitted channel codeword increases with the codeword length. Such a model applies, for example, in a time-varying channel with a fixed coherence time. The rate at which diversity grows with codeword length plays an important role in the optimization problem. If the diversity growth factor is large enough, then the erasure code plays a minor role, having an optimal rate that is essentially nondecreasing with decreasing overall rate. We prove analytically that, on a channel with linear growth in diversity, as overall rate decreases, the optimal erasure code rate eventually increases to its maximum possible value (e.g., a rate of 1 for an erasure code with no overhead). Additionally, we also consider the optimization problem of minimizing the message error probability given a transmit power. Numerical results again show that erasure coding is not necessary when overall code rates are sufficiently low.

## Cutoff Rate of Sparse Code Multiple Access in Downlink Broadcast Channels

- **Status**: ❌
- **Reason**: SCMA cutoff rate 이론 분석, 5G NOMA codebook 설계 — LDPC ECC 아니고 순수 이론 bound
- **ID**: ieee:7926318
- **Type**: journal
- **Published**: Aug. 2017
- **Authors**: Li Li, Zheng Ma, Li Wang +2
- **PDF**: https://ieeexplore.ieee.org/document/7926318
- **Abstract**: For the sake of supporting massive connectivity in the future 5G networks, non-orthogonal multiple access (NOMA) techniques are advocated. As a promising NOMA technique, in recent years sparse code multiple access (SCMA) has attracted substantial attention. However, there is a paucity of studies on the theoretical analysis of its error-freely achievable data rate, especially, in the downlink context. Hence, we derive the cutoff rate of SCMA in downlink broadcast channels, which indicates the lower-bound of a system's error-freely achievable rate. However, we will demonstrate that when considering the conventional categorization of pairwise error events, the accuracy of the cutoff rate rapidly degrades in the low-SNR region owing to the fact that multi-user SCMA systems typically encounter an extremely large constellation size. Alternatively, by invoking Bergmans' concept from 1973 in the categorization of pairwise error events, we obtain a more accurate cutoff rate both in the low- SNR regions and the high-SNR regions. Moreover, we provide insights into the cutoff rate derivation process, which reveals some general guidelines for designing a beneficial codebook, capable of improving SCMA with respect to its original low-density signature-based counterpart.

## Protection-Level-Exchanging Hierarchical Modulation for Multiresolution Services Under Decode-and-Forward Cooperative Networks

- **Status**: ❌
- **Reason**: 협력통신 계층변조 보호레벨 교환, ECC 디코더·코드설계 기법 없음
- **ID**: ieee:7807354
- **Type**: journal
- **Published**: Aug. 2017
- **Authors**: Hao-Yun Huang, Yuh-Ren Tsai
- **PDF**: https://ieeexplore.ieee.org/document/7807354
- **Abstract**: In the two-level hierarchical modulation (HM), two data streams-the base layer and refinement layer-are transmitted with different degrees of protection according to their importance. In general, the refinement layer suffers from insufficient protection for users experiencing poor channel conditions. Although cooperative transmission can improve the reception performance via diversity combining the signals from the source node and relay node, the refinement layer may still have unacceptable performance for users with very poor signal quality. To improve the overall performance of multiresolution services, we propose protection-level-exchanging HM for multiresolution services under decode-and-forward cooperative networks. At the relay node, it exchanges the protection levels of the decoded base bits and refinement bits, and remodulates the data based on a redesigned optimal HM constellation mapping for transmission. Hence, the overall bit error rate (BER) of the refinement bits is significantly improved at the destination node. We also propose the weighted combined BER (WCB) to fairly and reasonably evaluate the overall service performance. Based on the WCB, we investigate the optimization of the constellation priority parameters used at the source node and relay node to optimize system performance. According to the simulation results, our proposed scheme achieves better performance than other existing schemes.

## A Trellis Error Modeling Approach to Decoding Distributed Turbo Codes

- **Status**: ❌
- **Reason**: 분산 터보부호 디코딩(TEM-ID), 릴레이 오류모델 — 터보 특화로 바이너리 LDPC BP에 이식 불가
- **ID**: ieee:7929359
- **Type**: journal
- **Published**: Aug. 2017
- **Authors**: Bin Qian, Wai Ho Mow
- **PDF**: https://ieeexplore.ieee.org/document/7929359
- **Abstract**: In this paper, we re-examine the decoding problem of a distributed turbo code (DTC) over the three-node one-way relay channel based on the decode-and-forward protocol. In the traditional DTC scheme, the decoder at the destination assumes the error-free Viterbi decoding at the relay. However, the error propagation effect resulting from unsuccessful decoding at the relay may cause significant performance loss in some practical scenarios. Improved decoders reported in the literature typically assume a certain memoryless error model, which ignores the fact that relay decoding errors are correlated and bursty. In this paper, we propose a novel trellis error model (TEM) to accurately represent the statistics of relay decoding errors and construct two TEM-based iterative decoders (TEM-IDs) with two and three components, respectively. The TEM-ID with three components has a lower complexity than that of the TEM-ID with two components at the cost of minor performance loss. We also derive a new BER bound for the near maximum likelihood decoding of the DTC using a uniform interleaver. In addition, the extrinsic information transfer chart analysis is applied to estimate the threshold performance of the TEM-ID for large code lengths. Extensive simulation results verify that the new decoders can perform close to the derived BER bound and outperform existing decoders. Finally, we show that the TEM-ID can be extended for general distributed concatenated coding systems.

## Mitigating Stuck Cell Failures in MLC NAND Flash Memory via Inferred Erasure Decoding

- **Status**: ✅
- **Reason**: A/C: MLC NAND 직접, stuck cell을 erasure로 추론하는 신규 ISED BP 디코더+LLR 감쇠 기법 — NAND LDPC 직접 이식
- **ID**: ieee:7889015
- **Type**: journal
- **Published**: Aug. 2017
- **Authors**: Adnan Aslam Chaudhry, Cai Kui, Yong Liang Guan
- **PDF**: https://ieeexplore.ieee.org/document/7889015
- **Abstract**: The multilevel-cell NAND flash memory experiences permanent hard errors due to cell defects (stuck cells). To overcome this problem, stuck cells are either regarded as erasures by the decoder based upon the knowledge of stuck cell location, or the entire memory block containing the stuck cells is marked as bad block and made unavailable for future usage. In this paper, a multiround inferred stuck-cell erasure belief-propagation (BP) decoding (ISED) is proposed in which the stuck cell locations are assumed to be unknown to the decoder. To perform the inferred erasure decoding, the input channel log-likelihood ratio (LLR) information is attenuated before BP decoding by modifying the threshold voltage distribution functions. In case of decoding failure, the probable stuck cell locations are inferred by using the flash's read-back voltage signal and the decoded code-word bits. For all such inferred stuck cells, the input LLRs are set to zero for subsequent rounds of BP decoding. As the likely incorrect LLRs corresponding to the stuck cells are erased, the performance of BP decoder is substantially improved. Simulation results show that the error-rate performance is improved by more than two orders of magnitude with a moderate increase in decoding complexity under the proposed ISED scheme.

## Ring-Type Magnitude Modulation for LINC: A Pragmatic Approach to the Efficiency Challenge

- **Status**: ❌
- **Reason**: LINC 전력증폭/OQPSK 변조 기법, RMM 보상용 iterative decoding은 LDPC와 무관 — 떼어낼 ECC 기법 없음
- **ID**: ieee:7903638
- **Type**: journal
- **Published**: Aug. 2017
- **Authors**: António Simões, Mário Castanheira, Marco Gomes +2
- **PDF**: https://ieeexplore.ieee.org/document/7903638
- **Abstract**: This paper considers the use of the linear amplification with nonlinear components (LINC) technique for the power amplification of spectrally compact offset quadrature phase shift keying (OQPSK) signals allowing the use of highly efficient, low cost, and strongly nonlinear high power amplifiers (HPAs). However, the performance of the LINC signal separation and power combining procedures decreases with the rise of the signal's peak-to-average power ratio (PAPR). A new ring-type magnitude modulation (RMM) method is proposed for OQPSK signals that limits both its maximum and minimum complex envelope excursions avoiding zero crossings, without spreading the transmitted signal's spectrum. The performance results show that band-limited OQPSK signals whose envelope has low fluctuations produce LINC components with a narrower spectrum, with a considerable impact on the LINC transmitter regardless of the type of combiner chosen: when using a passive/matched combiner, the transmitter's power efficiency is significantly increased without spreading the combined signal's spectrum; for the highly efficient non-linear Chireix combiner, there is a reduction of the amount of spectral leakage produced by nonlinearly combining the LINC signal components. Finally, an iterative decoding scheme is also proposed, which employs estimates of the received symbols' RMM coefficients to compensate the RMM distortion.

## A scheme of ultraviolet communication system with polar channel coding

- **Status**: ❌
- **Reason**: UV 통신 polar 부호 BER 비교, LDPC는 베이스라인 비교용. 떼어낼 LDPC 기법 없음
- **ID**: ieee:8121355
- **Type**: conference
- **Published**: 7-10 Aug. 
- **Authors**: Wenxiu Hu, Zhenfu Luo, Dahai Han +3
- **PDF**: https://ieeexplore.ieee.org/document/8121355
- **Abstract**: We propose a scheme of ultraviolet (UV) communication system, with polar channel coding method. The bit error rate (BER) performance of the UV polar code scheme is analyzed by simulations and offline experiments, in contrast with low-density parity-check (LDPC) scheme. Results suggest that the polar code scheme has a better BER performance than LDPC scheme in the UV communication system.

## Special session: Low power LDPC deocder using adaptive forced convergence algorithm

- **Status**: ✅
- **Reason**: adaptive forced convergence로 VN/CN 비활성화하는 저복잡도 LDPC 디코더 알고리즘(C)
- **ID**: ieee:8052922
- **Type**: conference
- **Published**: 6-9 Aug. 2
- **Authors**: JeongHyeon Bae, Byung Jun Choi, Myung Hoon Sunwoo
- **PDF**: https://ieeexplore.ieee.org/document/8052922
- **Abstract**: LDPC codes have been applied in recent communication standards, such as WiFi, WiGig, and 10GBased-T Ethernet as a forward error correction code. However, LDPC codes require a large number of computational complexity for high performances. To solve this problem, various studies have been continuously performed for reducing computational complexity. In this paper, we propose an adaptive forced convergence algorithm to deactivate the variable nodes and check nodes for reducing the computational complexity using only one adaptive threshold value.

## A high-performance FPGA-based LDPC decoder for solid-state drives

- **Status**: ✅
- **Reason**: SSD용 FPGA 반병렬 QC-LDPC 디코더 아키텍처+adaptive normalization(A/D)
- **ID**: ieee:8053152
- **Type**: conference
- **Published**: 6-9 Aug. 2
- **Authors**: Yanhuan Liu, Chun Zhang, Pengcheng Song +1
- **PDF**: https://ieeexplore.ieee.org/document/8053152
- **Abstract**: In order to improve the throughput of error correction decoding for the high-performance solid-state drives (SSDs), a semi-parallel low-density parity-check (LDPC) decoding architecture is proposed in this paper. The circuit of the LDPC decoder which can be dynamically configured with bit rate and code length is implemented using the scheduling control flow mode of single instruction multiple data (SIMD) instruction. The Peripheral Component Interconnect Express (PCIe) interface is designed and the adaptive normalization factor is applied to achieve an average improvement of 35% in throughput with a signal-to-noise ratio (SNR) of 6.08 dB. The LDPC decoder is implemented on the Xilinx VC709 FPGA. With a rate-0.94 length-35840 quasi-cyclic LDPC code, the decoder achieves a throughput of 1.97 Gb/s which compares favorably with previously proposed architectures.

## Community detection in signed networks: An error-correcting code approach

- **Status**: ❌
- **Reason**: 신호 네트워크 커뮤니티 검출에 BP/bit-flip 디코딩을 응용한 것으로, NAND LDPC ECC에 이식할 새 디코더 기법 없음(기존 알고리즘 응용)
- **ID**: ieee:8397662
- **Type**: conference
- **Published**: 4-8 Aug. 2
- **Authors**: Cheng-Shang Chang, Duan-Shin Lee, Li-Heng Liou +1
- **PDF**: https://ieeexplore.ieee.org/document/8397662
- **Abstract**: In this paper, we consider the community detection problem in signed networks, where there are two types of edges: positive edges (friends) and negative edges (enemies). One renowned theorem of signed networks, known as Harary's theorem, states that structurally balanced signed networks are clusterable. By viewing each cycle in a signed network as a parity-check constraint, we show that the community detection problem in a signed network with two communities is equivalent to the decoding problem for a parity-check code. We also show how one can use two renowned decoding algorithms in error-correcting codes for community detection in signed networks: the bit-flipping algorithm, and the belief propagation algorithm. In addition to these two algorithms, we also propose a new community detection algorithm, called the Hamming distance algorithm, that performs community detection by finding a codeword that minimizes the Hamming distance. We compare the performance of these three algorithms by conducting various experiments with known ground truth. Our experimental results show that our Hamming distance algorithm outperforms the other two.

## Irregular QC-LDPC based multi-level coded modulation scheme for the next generation optical communication systems

- **Status**: ✅
- **Reason**: EXIT chart 기반 irregular QC-LDPC 코드 구성 최적화 — 바이너리 QC-LDPC 코드설계(E) 이식 가능
- **ID**: ieee:8114859
- **Type**: conference
- **Published**: 31 July-4 
- **Authors**: Dongdong Wang, Liqian Wang, Xue Chen +5
- **PDF**: https://ieeexplore.ieee.org/document/8114859
- **Abstract**: In this paper, we mainly focus on the optimization of multi-level coded modulation scheme in terms of sub-channel code rate optimal assignment and irregular QC-LDPC code construction with the aid of EXIT chart analysis. Simulation results show that the proposed MLCM scheme can achieve additional 0.1dB NCG compared with the UEP coded modulation scheme.

## 100/150/200 Gb/s real-time demonstration of SD-FEC employing MSSC-LDPC codes for flexible coherent transport

- **Status**: ❌
- **Reason**: SC-LDPC+BCH 실시간 광전송 데모, modulation/rate-adaptability 중심 — 떼어낼 신규 바이너리 LDPC 디코더/구성 기법 불명확, 비-LDPC 결합
- **ID**: ieee:8114879
- **Type**: conference
- **Published**: 31 July-4 
- **Authors**: Kenji Ishii, Keisuke Dohi, Takafumi Fujimori +8
- **PDF**: https://ieeexplore.ieee.org/document/8114879
- **Abstract**: To support forthcoming flexible coherent transport, we demonstrate a multiple-structured spatially-coupled LDPC with BCH codes which offers modulation flexibility, rate-adaptability and pilot-aided cycle-slip mitigation.

## Channel coding for optical transmission systems

- **Status**: ❌
- **Reason**: 광통신용 바이너리/비이진 LDPC+FPGA 서베이성 invited paper — 비이진 포함, 구체적 신규 기여 불명확
- **ID**: ieee:8114842
- **Type**: conference
- **Published**: 31 July-4 
- **Authors**: Ivan B. Djordjevic
- **PDF**: https://ieeexplore.ieee.org/document/8114842
- **Abstract**: In this invited paper, both binary and nonbinary LDPC codes suitable for optical transmission systems are described. The corresponding FPGA implementation has been discussed as well. The use of adaptive LDPC coding to deal with time-varying optical channel conditions is described as well.

## Multi-Mode Low-Latency Software-Defined Error Correction for Data Centers

- **Status**: ✅
- **Reason**: 플래시 메모리용 적응형 ECC, hard/soft LDPC 디코더(BF+BP) 조합 및 FPGA 구현 — NAND 직접(A)+디코더(C/D)
- **ID**: ieee:8038467
- **Type**: conference
- **Published**: 31 July-3 
- **Authors**: Fakhreddine Ghaffari, Ali Akoglu, Bane Vasic +1
- **PDF**: https://ieeexplore.ieee.org/document/8038467
- **Abstract**: Flash memories are gaining prominence for utilizing in large scale data centers (DCs) due to their high memory density, low power consumption and heat dissipation, and high access speed characteristics. The rate of degradation for a flash memory is largely affected by the amount and frequency of the erase/write operations, which is a challenge in the DC context that serves dynamically changing workloads. Adaptive Error Correction Code (AECC) schemes have been introduced for changing the error correction algorithm based on the reliability state of the flash. In this study we show that hard decision (bit-flipping) and soft decision decoding (Belief Propagation) class of algorithms for Low Density Parity Check (LDPC) decoders complement each other for utilizing in the flash based DCs in order to meet the dynamically changing reliability level. We propose a new family of ECC to improve the reliability of flash memory. Our Monte-Carlo simulations and Field Programmable Gate Array (FPGA) based hardware implementation analysis show that LDPC decoders are suitable for balancing the throughput, decoding performance and reliability requirements in DCs.

## Complexity-constrained spatially coupled LDPC codes based on protographs

- **Status**: ✅
- **Reason**: E: protograph 기반 SC-LDPC 구성 + sliding window 디코더 복잡도-성능 트레이드오프(PEXIT) — 바이너리 코드설계/디코더 기법 이식 가능
- **ID**: ieee:8108160
- **Type**: conference
- **Published**: 28-31 Aug.
- **Authors**: Massimo Battaglioni, Marco Baldi, Enrico Paolini
- **PDF**: https://ieeexplore.ieee.org/document/8108160
- **Abstract**: Spatially coupled low-density parity-check (SC-LDPC) codes are often thought as codes with very long block lengths. However, they can be decoded through sliding window (SW) decoders achieving near-optimal performance when the window size is a few times larger than the code syndrome former constraint length. This makes SC-LDPC codes with short constraint length suitable for low-latency transmissions, and they can even outperform their block code counterparts. Complexity of SW decoders increases linearly with the window size and with the number of decoding iterations. When complexity is constrained, an optimal trade-off between the window size and the maximum number of decoding iterations has to be found. In this paper, we propose a PEXIT-based method to find the best trade-off for codes with short syndrome former constraint length. We consider codes based on protographs, and validate the results of the PEXIT-based method through Monte Carlo simulations.

## Finite blocklength performance of a multi-relay network with best single relay selection

- **Status**: ❌
- **Reason**: polar 코드 유한블록길이 성능 bound(비-LDPC) - 다중 릴레이 선택 무선 응용, LDPC BP로 떼어낼 기법 없음
- **ID**: ieee:8108095
- **Type**: conference
- **Published**: 28-31 Aug.
- **Authors**: Yulin Hu, Christopher Schnelling, Yassine Amraue +1
- **PDF**: https://ieeexplore.ieee.org/document/8108095
- **Abstract**: We consider a multi-relay system where the best single relay is selected to assist transmissions. We study the performance bound of the system in the finite blocklength regime. On the one hand, we extend Polyanskiy's finite blocklength model of a single-hop scenario to the considered relaying system and derive the corresponding achievable throughput. On the other hand, by employing a practical coding scheme, namely polar codes, a finite blocklength performance bound attainable by a low-complexity coding scheme is provided. Through simulation and numerical investigations, we show the appropriateness of the proposed bounds. Moreover, we evaluate both the achievable performance with finite blocklengths and the performance of polar codes in the best single relay scenario in comparison to direct transmission.

## On cooperation in DVB-S2X receivers through a capacity constrained link

- **Status**: ❌
- **Reason**: 위성 수신기 협력·LLR 양자화이나 BCJR/MMSE 기반 비-LDPC 무선 응용 특이적, 떼어낼 LDPC ECC 기법 없음
- **ID**: ieee:8108165
- **Type**: conference
- **Published**: 28-31 Aug.
- **Authors**: Michelangelo Ricciulli, Fredrik Rusek
- **PDF**: https://ieeexplore.ieee.org/document/8108165
- **Abstract**: A scheme for exploiting cooperation in satellite receivers is proposed. The cooperation takes place through a capacity-constrained link, and we assume that a relay node quantizes its received signal and sends it to the destination node. We demonstrate its effectiveness with three different schemes on satellite channels with high-order APSK modulations. The first two schemes employ equidistant quantization levels and the proposed receivers are respectively based on Minimum Mean Square Error (MMSE) filtering and on a simple modification of the BCJR transition probabilities. The third scheme works with a quantized version of LLRs. We show that the latter has higher gains when the number of quantization bits is lower than the number necessary to represent all the modulation symbols and that in this case there is a simple approach to cluster together symbols and design a quantization scheme.

## Single-carrier 400G unrepeatered WDM transmission using nonlinear compensation and DD-LMS with FEC feedback

- **Status**: ❌
- **Reason**: 광전송 비선형보상+DD-LMS, SC-LDPC는 표준 FEC limit 베이스라인 — 새 디코더/구성 기여 없음
- **ID**: ieee:8121038
- **Type**: conference
- **Published**: 27-30 Aug.
- **Authors**: C. José Hélio, André L. N. Souza, João C. S. S. Januário +5
- **PDF**: https://ieeexplore.ieee.org/document/8121038
- **Abstract**: In this paper, we investigate the performance of unrepeatered optical transmission using nonlinear compensation, and dynamic equalization enhanced by forward error correction (FEC) feedback. The digital back-propagation (DBP) algorithm is used for nonlinear compensation, while error correction is provided by spatially-coupled low-density parity-check (SC-LDPC) codes. The technique is experimentally evaluated by the unrepeatered WDM transmission of 16×400 Gb/s single-carrier channels (66 GBd DP-16QAM) within a 75 GHz grid over 403 km (64.7 dB span loss), achieving 2.58 Pb/s km. The results indicated Q2 margins to the FEC limit of up to 0.4 and 0.5 dB for 3 and 6-dBm average launch powers, respectively, exhibiting a tangible improvement compared with previous works.

## A merged BP decoding algorithm for polar-LDPC concatenated codes

- **Status**: ✅
- **Reason**: polar-LDPC 연접 부호의 merged BP 복호 알고리즘으로 인자그래프 결합 기반 BP 개선, 부호 비의존 메시지패싱 기법으로 바이너리 LDPC BP 이식 여지(C), 애매하여 살림
- **ID**: ieee:8096145
- **Type**: conference
- **Published**: 23-25 Aug.
- **Authors**: Jiaai Liu, Shusen Jing, Xiaohu You +1
- **PDF**: https://ieeexplore.ieee.org/document/8096145
- **Abstract**: Recently, both polar codes and low-density parity-check (LDPC) codes have been adopted by 3GPP eMBB scenario. Since both codes exist in one system, it is natural to consider the concatenation scheme of them. In this paper, a merged belief propagation (BP) decoding algorithm for the concatenated codes of polar and LDPC codes is proposed. By jointing factor graphs, this merged algorithm is designed by serially executing the LDPC and polar decoding. According to numerical results, the bit error rate (BER) of this proposed algorithm can achieve a notable improvement for different code rates compared with the conventional separated approach. For (1024, 512) polar code, the performance gain of the proposed scheme is at least 0 5 dB even at a low BER of 1 × 10-2. Finally, further refinements of computational complexity and hardware implementation are also provided in this paper.

## An optimal filter for signals with time-varying cyclostationary statistics

- **Status**: ❌
- **Reason**: 시변 순환정상 통계 필터로 간섭 제거, LDPC는 비교 베이스라인일 뿐 떼어낼 ECC 기법 없음
- **ID**: ieee:8096078
- **Type**: conference
- **Published**: 23-25 Aug.
- **Authors**: Matt Carrick, Jeffrey H. Reed, Fred Harris
- **PDF**: https://ieeexplore.ieee.org/document/8096078
- **Abstract**: This paper presents a filter for exploiting time-varying cyclostationary statistics. The motivating example is designing redundancies into an OFDM signal to reject in-band, strong, wideband interference. Combining the filter with error correcting codes gives a 10 dB gain over LDPC codes and more than a 1000x reduction in BER. This allows the creation of multicarrier waveforms that are robust, reliable and resistant to interference. The filter improves upon existing techniques thought the ability to exploit time-varying spectral redundancy, a capability unique to this filter. The design equations for the optimal filter weights are derived, showing the upper bound for the performance of the filter. The applications range from control channel protection for next generation commercial broadband to mission-critical communications.

## Performance of MC-CDMA system with various orthogonal spreading codes in multipath Rayleigh fading channel

- **Status**: ❌
- **Reason**: MC-CDMA 스프레딩 코드 BER 분석, LDPC는 부수 언급이고 떼어낼 기법 없음
- **ID**: ieee:8089175
- **Type**: conference
- **Published**: 2-4 Aug. 2
- **Authors**: K. Sai Priyanjali, B. Seetha Ramanjaneyulu
- **PDF**: https://ieeexplore.ieee.org/document/8089175
- **Abstract**: In multi-user wireless communication system, there is huge demand for higher data rates. One promising solution to achieve it is through the amalgamation of Code Division Multiple Access (CDMA) and Orthogonal Frequency Division Multiplexing (OFDM) technologies which results in Multi Carrier-CDMA (MC-CDMA) system. In CDMA system, the multiple access interference (MAI) can be reduced through proper selection of spreading codes. Bit error rate (BER) is an effective measure to evaluate the interference performance of a multi-user communication system. In this paper the BER and Peak to Average Power Ratio (PAPR) of MC-CDMA system is analyzed for different orthogonal spreading codes such as Walsh codes, complementary Golay codes and Orthogonal Gold codes in Rayleigh multipath fading channel employing Low Density Parity Check (LDPC) channel coding technique.

## Channel concatenated coding transmission scheme for TSV array transmission

- **Status**: ❌
- **Reason**: TSV array concatenated LDPC+Hamming; standard concatenation, app-specific, no new LDPC technique
- **ID**: ieee:8046546
- **Type**: conference
- **Published**: 16-19 Aug.
- **Authors**: Xiaoyang Duan, Zhensong Li, Tianfang Chen +2
- **PDF**: https://ieeexplore.ieee.org/document/8046546
- **Abstract**: In order to improve the signal transmission performance of the TSV array transmission, TSV arrays are seen as transmission channels. And a communication channel model with high noise and high crosstalk is established for TSV array transmission. In this paper, a channel concatenated coding transmission scheme is proposed to apply the concatenated code to the TSV array transmission model. Its purpose is to optimize the transmission performance and realize the efficient transmission of the signal in the TSV array. In this case, channel noise is seen as White Gaussian Noise, and crosstalk is determined by the S parameters. Taking into account the coding efficiency and transmission efficiency, the Low Density Parity Check (LDPC) code is used as the inner code and the Hamming code is used as the outer code. The simulation results show that the bit error rate (BER) performance improved at any information transmission rate, and the BER is lower than using LDPC code alone. Therefore, the channel concatenated coding transmission scheme can be used to achieve better TSV array signal transmission, overcome the transmission problem and improve transmission performance.

## Implementation of a decoder based on low-density parity-check code for 8 bit logical ALU

- **Status**: ❌
- **Reason**: 8bit ALU용 LDPC 로직 디코더; NAND ECC와 무관, 떼어낼 디코더/코드설계 기법 없음
- **ID**: ieee:8079598
- **Type**: conference
- **Published**: 16-18 Aug.
- **Authors**: Dibyendu Deogharia, Jayanta Bhattacharya, Sutapa Ray +8
- **PDF**: https://ieeexplore.ieee.org/document/8079598
- **Abstract**: A Decoder working on the logic of LDPC is designed for a 8 bit Logical ALU. The Simulation has been done to minimize the Voltage Leakage and Maximum throughput.

## Enhancing SSD performance with LDPC-aware garbage collection

- **Status**: ✅
- **Reason**: A) SSD에서 LDPC read 지연 고려한 garbage collection; NAND/SSD 직접 컨트롤러 기법
- **ID**: ieee:8064481
- **Type**: conference
- **Published**: 16-18 Aug.
- **Authors**: Yajuan Du, Yunpei Jia, Meng Zhang +2
- **PDF**: https://ieeexplore.ieee.org/document/8064481
- **Abstract**: With the technology scaling of solid state drives (SSDs), data reliability has to be ensured by advanced Low-Density Parity-Check (LDPC) codes. As LDPC reads often take high latency, read performance involved in traditional garbage collection, called external GC, is largely decreased, which affects system performance. GC can choose not to correct data with LD-PC codes but just copy valid pages into registers of NAND flash, which we call internal GC. Although this method avoids long latency in LDPC reads, the data integrity is sacrificed because of error aggregation in valid pages. To balance performance and reliability, this paper proposes a new garbage collection method, named as LDPC-aware Garbage Collection (LaGC), to selectively choose blocks with high error rates to perform external GC. These blocks are often close to uncorrectable error rates, which take a small portion during a long flash life period. Thus, most of blocks perform internal GC and keep advantage of low read latency. Experimental results show that LaGC can reduce 78% of read latency in external GC and achieve about 2% system performance improvement.

## Improving read performance via selective Vpass reduction on high density 3D NAND flash memory

- **Status**: ❌
- **Reason**: 3D NAND read disturb 완화 Vpass 조정; ECC/LDPC 기법이 아닌 셀 동작 기법
- **ID**: ieee:8064482
- **Type**: conference
- **Published**: 16-18 Aug.
- **Authors**: Qiao Li, Liang Shi, Yejia Di +5
- **PDF**: https://ieeexplore.ieee.org/document/8064482
- **Abstract**: 3D NAND flash memory has been well developed due to its high density and decreasing cost compared with planar flash. However, one issue for 3D NAND flash, which has not been well solved, is its worse read disturb. The worse read disturb of 3D NAND flash stems from its much more word lines in a block. In this case, it receives much more read operations, leading to increased read disturb. Previous work proposed to relax the read disturb on planar flash through reducing the pass-through voltage, Vpass, on the unread word lines. However, this is not viable for 3D NAND flash with the increased number of word lines in a block. In this work, a new read disturb reduction scheme is proposed for 3D NAND flash. First, a read error model is presented, which demonstrates that selective Vpass reduction is a viable approach. Then, a read-hotness aware Vpass reduction scheme is proposed to improve performance without violating the reliability requirement. Simulation shows that the proposed scheme achieves encouraging performance improvement.

## Performance analysis of LDPC MIMO-OFDM system for frequency selective fading channels

- **Status**: ❌
- **Reason**: LDPC concatenated가 베이스라인인 무선 MIMO-OFDM 응용, 떼어낼 LDPC 기법 없음
- **ID**: ieee:8389759
- **Type**: conference
- **Published**: 1-2 Aug. 2
- **Authors**: P Arya Bhaskar, Basil K Jeemon, S Dhanya
- **PDF**: https://ieeexplore.ieee.org/document/8389759
- **Abstract**: The Orthogonal Frequency Division Multiplexing (OFDM) is a very attractive technique for high-bit — rate data transmission in multipath path environments. Multiple input multiple output (MIMO) communication systems along with OFDM systems in Rayleigh fading channel increases the system performance. A new trend of space-time block code (STBC)-OFDM system and space-frequency block code (SFBC)-OFDM system and a comparison between them are introduced. A channel matrix shaping method is introduced in STBC-OFDM and SFBC-OFDM systems. The proposed system presents a performance analysis of serially concatenated LDPC codes with alamouti space time block coded (STBC)-MIMO-OFDM systems for high data rate wireless transmission. The simulation results show the proposed system outperforms the conventional STBC method and STBC with channel matrix shaping. Proposed system has low computational complexity, because it is based on WHT.

## A comparison and simulation of LDPC decoders for Chinese digital television multimedia broadcasting(CDTMB) standard

- **Status**: ✅
- **Reason**: min-sum 변형(SSMSD/NSSMSD) 메모리·연산 절감 디코더 비교 — 이식 가능 디코더(C)
- **ID**: ieee:8389609
- **Type**: conference
- **Published**: 1-2 Aug. 2
- **Authors**: Vijaykumar T. Korishetti, V. Jayashree, V. C. Patil
- **PDF**: https://ieeexplore.ieee.org/document/8389609
- **Abstract**: For the last 20 years intense research has been carried out on Low Density Parity Check(LDPC) decoders for supporting various transmission technologies. There are various proven LDPC decoder algorithms such as Log domain sum product algorithm(LDSPA), Min sum decoder(MSD), Single scan min sum decoder(SSMSD) and normalized single scan min sum decoder(NSSMSD) which are currently in use. Each of these algorithm have its own distinct pros and cons from implementation point of view that comes to support various transmission standards. In this paper four LDPC decoding algorithms are implemented to test and support CDTMB standard for its three code rates viz. 0.4, 0.6 and 0.8. The performance evaluation of all four decoder algorithms mentioned above are carried out with Additive White Gaussian Noise(AWGN) channel with BPSK modulation scheme. The software implementation of these algorithms show that min sum decoder algorithm reduces complexity when compared to LDSPA. Also SSMSD and NSSMSD contributes to conservation of memory to 23% and take at least 35% less computation time compared to LDSPA and MSD. LDSPA is preferred for low data rate applications for its good BER performance, but it has the drawback of increase in hardware complexity due to the presence of tanh and log functions. SSMSD and NSSMSD is preferable for high data rate applications as this showed low memory requirement and faster performance.

## Analysis of OFDM system using different encoding and time-frequency localization techniques

- **Status**: ❌
- **Reason**: OFDM 인코딩/time-freq 리뷰, LDPC 신규 기여 없음
- **ID**: ieee:8389920
- **Type**: conference
- **Published**: 1-2 Aug. 2
- **Authors**: Manmohit Singh, Komal Arora
- **PDF**: https://ieeexplore.ieee.org/document/8389920
- **Abstract**: Orthogonal Frequency Division Multiplexing (OFDM) has been existing since last few decades as the base of wireless networks. It is used in high-data craved applications with minimum interference and channel fading effect. Switching towards multiple carrier transmission from single carrier transmission with some added flavors of advanced features makes Orthogonal Frequency Division Multiplexing, a base need of the high data required applications such as IEEE standard on 802.11g, 802.11a, WIMAX and various other broadband services. Various researchers had carried out with different results and views for the enhancement in OFDM systems depending on different modulation, interleaving, encoding, and decoding schemes and algorithms. This paper reviews a study about the OFDM system in aspect of improved encoding and time-frequency localization techniques.
