# IEEE Xplore — 2013-08 (1차선별 통과)


## An EXIT-Based Design Method for LDPC-Coded Schemes without Gaussian Assumptions

- **Status**: ✅
- **Reason**: Gaussian 가정 없는 EXIT 기반 LDPC 코드 설계 최적화 - 이식 가능 코드 설계 기법(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6522943
- **Type**: journal
- **Published**: August 201
- **Authors**: Yen-Ming Chen, Yeong-Luh Ueng, Hau-Jung Shiau
- **PDF**: https://ieeexplore.ieee.org/document/6522943
- **Abstract**: It is known that low-density parity-check (LDPC) codes are widely used to provide capacity-approaching performances in various transmission systems. However, the Gaussian assumption for soft messages in conventional EXIT (extrinsic information transfer)-chart-based optimization algorithms result in prediction gaps in the decoding threshold for certain transmission systems. In this letter, we propose an EXIT-chart-based optimization method, in which all the Gaussian assumptions for soft messages can be avoided. Compared to the conventional design methods, the proposed method provides a more accurate threshold prediction and can be used to design LDPC-coded schemes with better error performances.

## Construction of High-Rate Regular Quasi-Cyclic LDPC Codes Based on Cyclic Difference Families

- **Status**: ✅
- **Reason**: cyclic difference family 기반 고율 바이너리 QC-LDPC 신규 구성(girth 6, 최소 길이) — 코드설계 E
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6560065
- **Type**: journal
- **Published**: August 201
- **Authors**: Hosung Park, Seokbeom Hong, Jong-Seon No +1
- **PDF**: https://ieeexplore.ieee.org/document/6560065
- **Abstract**: For a high-rate case, it is difficult to randomly construct good low-density parity-check (LDPC) codes of short and moderate lengths because their Tanner graphs are prone to have short cycles. Also, the existing high-rate quasi-cyclic (QC) LDPC codes can be constructed only for very restricted code parameters. In this paper, based on special classes of cyclic difference families, we propose a new construction method of high-rate regular QC LDPC codes having parity-check matrices consisting of a single row of circulants with column-weight 3 or 4. The proposed QC LDPC codes can be constructed for various code rates and lengths including the minimum achievable length for given column-weight and design rate under girth 6. It is observed that the parity-check matrices of the proposed QC LDPC codes have full rank for column-weight 3 and just one redundant row for column-weight 4. It is shown that the error correcting performance of the proposed QC LDPC codes of short and moderate lengths is almost the same as that of the existing ones through numerical analysis.

## Rate-Compatible Protograph-Based LDPC Codes for Inter-Symbol Interference Channels

- **Status**: ✅
- **Reason**: rate-compatible protograph-based LDPC 구성(extension 방법) - 바이너리 코드 설계 기법(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6530823
- **Type**: journal
- **Published**: August 201
- **Authors**: Thuy Van Nguyen, Aria Nosratinia, Dariush Divsalar
- **PDF**: https://ieeexplore.ieee.org/document/6530823
- **Abstract**: This letter produces a family of rate-compatible protograph-based LDPC codes approaching the independent and uniformly distributed (i.u.d.) capacity of inter-symbol interference (ISI) channels. This problem is highly nontrivial due to the joint design of structured (protograph-based) LDPC codes and the state structure of ISI channels. We describe a method to design nested high-rate protograph codes by adding variable nodes to the protograph of a lower rate code. We then design a family of rate-compatible protograph codes using the extension method. The resulting protograph codes have iterative decoding thresholds close to the i.u.d. capacity. Our results are supported by numerical simulations.

## Low-complexity multi-way and reconfigurable cyclic shift network of QC-LDPC decoder for Wi-Fi/WIMAX applications

- **Status**: ✅
- **Reason**: QC-LDPC 디코더용 신규 cyclic shift network(CSD 알고리즘, permutation network) HW — D 이식 가능
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:6626226
- **Type**: journal
- **Published**: August 201
- **Authors**: Yongmin Jung, Yunho Jung, Seongjoo Lee +1
- **PDF**: https://ieeexplore.ieee.org/document/6626226
- **Abstract**: This paper proposes a cyclic shift decomposition (CSD) algorithm to perform multi-way cyclic shifts with low complexity in the quasi-cyclic low-density parity-check (QCLDPC) decoder. The proposed algorithm decomposes the cyclic shift into a common cyclic shift and a private cyclic shift. Based on the proposed CSD algorithm, a low-complexity multi-way and reconfigurable cyclic shift network (CSN) for QC-LDPC codes is proposed. The proposed CSN is composed of the shared component, which performs the common cyclic shift, and the repeated component, which performs the private cyclic shift. Each component can support reconfigurability for given QCLDPC codes. By introducing the single-path shared component, only the complexity of the multi-path repeated component increases linearly as the number of multi-way paths increases. A complexity analysis of each component is also proposed. Based on the complexity analysis, the proposed CSN can perform multi-way and reconfigurable cyclic shifts with low complexity in the QC-LDPC decoder. The implementation results show that the areas of the proposed four-way CSN are 0.227 mm2 and 0.276 mm2 for the IEEE 802.11n/ac and IEEE 802.16e QC-LDPC codes, respectively, with 130 nm CMOS technology. The area saving per each-way is from 13.8% to 86.5% compared with previously presented works.

## Coding and system design for quantize-map-and-forward relaying

- **Status**: ✅
- **Reason**: 바이너리 LDPC+LDGM factor graph 결합 BP 디코딩과 density evolution 설계는 이식 가능 디코더/코드설계 기법(C/E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6658244
- **Type**: journal
- **Published**: Aug. 2013
- **Authors**: Vinayak Nagpal, I-hsiang Wang, Milos Jorgovanovic +2
- **PDF**: https://ieeexplore.ieee.org/document/6658244
- **Abstract**: In this paper we develop a low-complexity coding scheme and system design framework for the half duplex relay channel based on the Quantize-Map-and-Forward (QMF) relaying scheme. The proposed framework allows linear complexity operations at all network terminals. We propose the use of binary LDPC codes for encoding at the source and LDGM codes for mapping at the relay. We express joint decoding at the destination as a belief propagation algorithm over a factor graph. This graph has the LDPC and LDGM codes as subgraphs connected via probabilistic constraints that model the QMF relay operations. We show that this coding framework extends naturally to the high SNR regime using bit interleaved coded modulation (BICM). We develop density evolution analysis tools for this factor graph and demonstrate the design of practical codes for the half-duplex relay channel that perform within 1dB of information theoretic QMF threshold.

## LDPC codes for soft decode-and-forward in half-duplex relay channels

- **Status**: ✅
- **Reason**: RC-LDPC 차수분포 설계(하삼각 패리티검사, K-layer doping, MET density evolution)는 바이너리 LDPC 코드설계 기법으로 이식 가능(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6658243
- **Type**: journal
- **Published**: Aug. 2013
- **Authors**: Marwan H. Azmi, Jun Li, Jinhong Yuan +1
- **PDF**: https://ieeexplore.ieee.org/document/6658243
- **Abstract**: We investigate the use of rate-compatible lowdensity parity-check (RC-LDPC) codes as part of a soft decodeand- forward (SDF) protocol over the half-duplex relay channel. We propose a new methodology to design the degree distribution of the RC-LDPC codes with a lower triangular parity-check matrix, enabling the additional parity bits to be linearly and systematically encoded at the relay. Our proposed methodology introduces the concept of a K-layer doping matrix to represent the structure of a lower triangular parity-check matrix. As a result of our methodology, the asymptotic performance of RC-LDPC codes can be analyzed and predicted using the multi-edge-type density evolution. Then, we derive the soft-re-encoding of the additional parity symbols at the relay using our designed RCLDPC codes. Moreover, we propose a novel method, which we refer to as soft fading, to compute the log-likelihood ratio (LLR) of the received signal at the destination for the SDF protocol. We demonstrate that our proposed soft fading method outperforms the best known method in the literature by up to 0.7 dB in terms of BER performance. Finally, we derive a new bound for the power multiplication factor at the relay, which limits the amount of soft-errors forwarded by the relay to the destination. The BER performance of our new RC-LDPC codes improves significantly once the power multiplication factor at the relay satisfies this bound.

## Design and Implementation of a Low-Complexity Symbol Detector for Sparse Channels

- **Status**: ✅
- **Reason**: sparse 채널용 BP detector HW 구현(파이프라인, permutation 무관 BP 메시지패싱) — 디코더/HW 기법 일부 이식 가능, 애매하여 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6294462
- **Type**: journal
- **Published**: Aug. 2013
- **Authors**: Yanjie Peng, Xinming Huang, Andrew G. Klein +1
- **PDF**: https://ieeexplore.ieee.org/document/6294462
- **Abstract**: In this paper, we present a low-complexity symbol detector for communication channels which have long spanning durations but a sparse multipath structure. Traditional maximum-likelihood sequence estimation using the Viterbi algorithm can provide optimal error performance for eliminating the multipath effect, but the hardware complexity grows exponentially with channel length and it is not practical for long sparse channels. We implement a near-optimal algorithm and its architecture by cascading an adaptive partial response equalizer (PRE) with an iterative belief propagation (BP) detector. A sparse channel is first equalized by a PRE to a target impulse response (TIR) with only a few nonzero coefficients remaining. The residual intersymbol interference is then canceled by a BP detector whose complexity is solely dependent on the number of nonzero coefficients in the TIR. Moreover, we present a pipeline high-throughput implementation of the detector for channel length 30 with quadrature phase-shift keying modulation. The detector can achieve a maximum throughput of 206 Mb/s with an estimated core area of 3.162 mm2 using 90-nm technology node. At a target frequency of 515 MHz, the dynamic power is about 1.096 W.

## Uniform quantization of LDPC codes for 8PSK modulation

- **Status**: ✅
- **Reason**: min-sum 균일 양자화(정수연산) for HW 구현 — LLR 양자화/디코더 HW 이식(C/D)에 직접 적용 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6663960
- **Type**: conference
- **Published**: 5-8 Aug. 2
- **Authors**: Chen Zhengkang, Zhang Huisheng, Li Lixin +1
- **PDF**: https://ieeexplore.ieee.org/document/6663960
- **Abstract**: It's common to use high-precision floating-point operations on theoretical study of the Low Density Parity Check (LDPC) codes, but it is difficult to implement it in practical application. Therefore, there is a great need to design effective quantitative method which enables us to implement it in hardware easily. In this paper, the min-sum decoding algorithm of LDPC codes for 8PSK modulation is studied in detail, and the method of the uniform quantization is analyzed and deduced. With this method to quantify the initial message, the variable messages and check messages are converted into integers after each iteration. Then the min-sum decoding algorithm based on integer arithmetic for 8PSK modulation is implemented. Simulation results demonstrate that the performance of the min-sum decoding algorithm with the uniform quantization is close to that of the high-precision floating-point sum-product decoding algorithm. Meanwhile, all the variables in the algorithm are fixed-length integers, so it is convenient for hardware implementation.

## Probabilistic analysis of cycles in random Tanner graphs

- **Status**: ✅
- **Reason**: random Tanner graph short cycle 기대수 해석 + 사이클 계수 알고리즘(CCA) — girth/사이클 제거 코드설계(E)에 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6663929
- **Type**: conference
- **Published**: 5-8 Aug. 2
- **Authors**: Xiaopeng Jiao, Jianjun Mu
- **PDF**: https://ieeexplore.ieee.org/document/6663929
- **Abstract**: Cycles in bipartite graphs (also called Tanner graphs in channel coding field) are of particular interest in modern coding theory, especially in capacity-achieving low-density parity-check (LDPC) codes. In this paper, the expected number of cycles of various lengths in randomly constructed regular and irregular Tanner graphs are calculated. For a given degree distribution, the expected number of cycles in randomly constructed Tanner graphs has negligible changes with the size of Tanner graphs. Based on tree expanding, we propose a cycle counting algorithm (CCA) for Tanner graphs. Numerical results by counting the average number of short cycles over 200 random ensembles using the CCA give convincing supports to our analysis.

## High throughput architecture for low density parity check (LDPC) encoder

- **Status**: ✅
- **Reason**: bit-wise 행렬-벡터 곱 LDPC 인코더 고처리율 HW 아키텍처 - HW 이식 가능(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:6674807
- **Type**: conference
- **Published**: 4-7 Aug. 2
- **Authors**: Silvia Anggraeni, Fawnizu Azmadi Hussin, Varun Jeoti
- **PDF**: https://ieeexplore.ieee.org/document/6674807
- **Abstract**: This paper proposes a bit-wise matrix-vector multiplication in the optimization of a proposed low density parity check (LDPC) encoder. Investigation of this proposed architecture is done by implementing five code lengths using one IEEE 802.16e standard code rate. It is shown that the proposed architecture outperforms other works in terms of information throughput ranging from 0.235 to 8.83 times higher. In term of ratio of throughput per area, the proposed method exceeds other works in the range of 1.19 to 6.54 times higher.

## High-parallel performance-aware LDPC decoder IP core design for WiMAX

- **Status**: ✅
- **Reason**: 고병렬 layered LDPC 디코더 IP 코어, 3-state 스케줄로 병렬성/전력효율 개선 - HW 아키텍처 이식 가능(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:6674853
- **Type**: conference
- **Published**: 4-7 Aug. 2
- **Authors**: Xiongxin Zhao, Zhixiang Chen, Xiao Peng +2
- **PDF**: https://ieeexplore.ieee.org/document/6674853
- **Abstract**: In this paper, we propose a synthesizable LDPC decoder IP core for the WiMAX system with high parallelism and enhanced error-correcting performance. The proposed fully-parallel layered decoder architecture can fully support multi-mode decoding specified in WiMAX with 12~24 clock cycles for processing one iteration. By applying the 3-state processing schedule, it achieves twice parallelism with minor circuit area increase compared to state-of-the-art work, thus results in 46.8% improvement in power efficiency.

## EXIT-chart-based threshold calculation of LDPC code in 2D ISI channels

- **Status**: ✅
- **Reason**: 2D ISI 자기기록 채널 LDPC threshold EXIT 계산 기법, 스토리지 채널 코드설계 분석으로 애매하여 in
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6765958
- **Type**: conference
- **Published**: 29-31 Aug.
- **Authors**: Lingjun Kong, Yong Liang Guan, Guojun Han +2
- **PDF**: https://ieeexplore.ieee.org/document/6765958
- **Abstract**: An algorithm based on the fitting of modified Extrinsic Information Transfer (EXIT) chart is proposed to calculate the thresholds of low-density parity-check (LDPC) codes optimized for the two-dimensional (2D) intersymbol interference (ISI) channels encountered in high-density magnetic recording, such as bit-patterned magnetic recording (BPMR) and two-dimensional magnetic recording (TDMR). The modified EXIT chart algorithm determines the LDPC threshold by fitting the EXIT curve of the variable node decoder (VND) combined with 2D detector (2D-DET) to the EXIT curve of the check node decoder (CND). Both the optimal Bahl-Cocke-Jelinek-Raviv (BCJR) 2D-DET and reduced-complexity Gaussian-approximated iterative row-column 2D-DET are considered.

## A fast convergence and area-efficient decoder for quasi-cyclic low-density parity-check codes

- **Status**: ✅
- **Reason**: QC-LDPC 병렬 파이프라인 디코더 HW 아키텍처, normalized min-sum 재구성+면적/메모리 절감(D 이식 가능)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:6765990
- **Type**: conference
- **Published**: 29-31 Aug.
- **Authors**: Zhibin Luan, Yukui Pei, Ning Ge
- **PDF**: https://ieeexplore.ieee.org/document/6765990
- **Abstract**: The quasi-cyclic low-density parity-check (QC-LDPC) codes have attracted much attention in space communication systems. However, the decoders are still difficult to be applied in practice for their large area and high memory requirements. Moreover, the clock cycles for the input and output interfaces can not be ignored due to the I/O resource is also limited on this occasion, which influences the throughput improvement significantly. This paper presents a parallel pipelined decoder architecture for QC-LDPC codes, which can largely reduce their area and memory size while maintaining a fast convergence speed. The decoding approach reformulates the original normalized min-sum algorithm and adopts a two pipelines architecture to eliminate the clock cycles for the I/O and reduce the number of clock cycles per iteration. Chip designed with TSMC 0.13-µm eight-metal-layer standard CMOS technology shows that it can achieve a throughput up to 767 Mbps with only 3.12 mm2 core area consumption. Especially, only 36 I/O ports are occupied, less than 10% of the conventional decoders.

## Combined optimization scheme for degree distributions of LDPC codes

- **Status**: ✅
- **Reason**: LDPC degree distribution 최적화 기법(differential evolution+simplex), 바이너리 코드설계 이식 가능(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6765996
- **Type**: conference
- **Published**: 29-31 Aug.
- **Authors**: Jin Soo Park, Min Kyu Song, Hong-Yeop Song
- **PDF**: https://ieeexplore.ieee.org/document/6765996
- **Abstract**: In this paper, we propose an optimization scheme for degree distributions of LDPC codes that combines differential evolution and iterative simplex algorithm. In the proposed scheme, we find good check and variable nodes degree distribution and threshold by using differential evolution, and then, we further optimize check and variable nodes degree distribution that has enhanced code rate by using an iterative simplex algorithm. An iterative simplex algorithm consists of two simplex algorithms, optimizing ρ(x) and λ(x), respectively and iteratively. Some simulation results show that the proposed scheme finds degree distributions, better than those obtained by the differential evolution only, in terms of threshold and/or code rate. As an application of the proposed scheme, we report some new degree distributions with some new maximum degrees.

## Defining Turbo Codes as Irregular LDPC Codes

- **Status**: ✅
- **Reason**: Turbo를 비순환(4-cycle 제거) sparse LDPC 패리티검사로 표현해 BP 디코딩 — 부호 비의존 BP 이식 기법(예외 C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6629832
- **Type**: conference
- **Published**: 27-30 Aug.
- **Authors**: J. Bas
- **PDF**: https://ieeexplore.ieee.org/document/6629832
- **Abstract**: Turbo Codes (TC) and Low-Density Parity-Check (LDPC) codes share similar structures in their respective error correction process (e.g. two-stage iterative decoding, Log-Likelihood based, etc.). These relationships can be used to express TCs in terms of the parity-check matrix of LDPCs but constrained to be: i) of low-density and, ii) without cycles of 4th order [1][2]. Otherwise the performance of Believe Propagation (BP) algorithm, the decoding strategy of LDPC codes, degrades notably [3],[4]. The introduction of constraints in TC's parity-check matrix determines the active shift registers of its convolutional mother codes and its permutation matrix. Simulation results show that the Bit Error Rate (BER) of Turbo Codes decoded by means of Believe Propagation (BP) algorithm is quite similar to that offers the Bahl- Cocke-Jelinek-Raviv (BCJR), the classical algorithm for decoding Turbo Codes.

## Stressing the BER simulation of LDPC codes in the error floor region using GPU clusters

- **Status**: ✅
- **Reason**: error floor 영역 BER 시뮬레이션을 GPU 클러스터로 병렬가속 — 디코더 병렬화/검증 HW 기법(D), 바이너리 LDPC
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:6629867
- **Type**: conference
- **Published**: 27-30 Aug.
- **Authors**: Gabriel Falcao, Joao Andrade, Vitor Silva +2
- **PDF**: https://ieeexplore.ieee.org/document/6629867
- **Abstract**: Low-Density Parity-Check (LDPC) codes are known for having excellent Bit Error Rate (BER) performance, even in the presence of quite low Signal-to-Noise Ratios (SNR). But the development of this type of error-correcting codes poses severe challenges since the design of new codes is based on heuristics such as girth and sparsity that not always provide the expected BER results and, consequently, can take long periods of time to be tested with Monte Carlo simulations using a massive amount of bits pseudo-randomly generated and transmitted over noisy channels. We address the computational complexity demanded by the LDPC decoder and the challenges imposed from the parallel architecture perspective, in particular targeting multicore systems that have the potential to deal more efficiently with computationally intensive applications. To handle the massive computational power required by the new and computationally more intensive generations of LDPC codes that demand lower error floors, namely optical communication ones, we propose using clusters of GPUs as a way to accelerate this type of Monte Carlo simulations from years or months to weeks or days.

## An Early Termination Strategy for Irregular LDPC Codes with Layered Decoding - Performance Evaluation and Implementation

- **Status**: ✅
- **Reason**: C: 레이어드 디코딩 NMS 조기종료 전략 + degree-2 변수노드 활용 error floor 개선, HW 효율 구현. NAND LDPC 디코더에 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6629787
- **Type**: conference
- **Published**: 27-30 Aug.
- **Authors**: Miroslav Marinkovic, Eckhard Grass, Milos Krstic
- **PDF**: https://ieeexplore.ieee.org/document/6629787
- **Abstract**: Much attention has been paid to layered structures in the design of LDPC decoders. They promise fast convergence speed as well as reduced memory requirements. However, a correct stopping criterion (Hc checking) is difficult to implement in layered decoders, which results in unnecessary iterations. In this paper, we evaluate the error-rate performance of an hardware efficient early termination (ET) strategy under the normalized min-sum (NMS) algorithm and its improved versions. The irregular LDPC codes from IEEE 802.11n (WiFi) and IEEE 802.16e (WiMax) standards have been used for our investigation. From simulation results, it is shown that the conventional NMS algorithm with one optimal correction factor causes relatively high error floor. Therefore, we propose an improvement of the NMS algorithm by utilizing properties of degree-2 variable nodes. That improvement significantly lowers the error floor of the irregular LDPC codes with the ET strategy at high channel SNR values, which is confirmed by simulations. Finally, we employ the ET strategy in a WiMax decoder to reduce power consumption (around 50 % at a FER = 10(exp -4)).

## Construction of QC-LDPC Codes on Combinatorial Sequences

- **Status**: ✅
- **Reason**: 조합수열 기반 QC-LDPC 신규 구성법(girth>=6 보장), 코드설계 기법(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6642693
- **Type**: conference
- **Published**: 26-27 Aug.
- **Authors**: Fu Chenghua, Li Xiuli
- **PDF**: https://ieeexplore.ieee.org/document/6642693
- **Abstract**: Based on the properties of pell sequences, hanoi sequences and lucas sequences, three methods are proposed to construct new families of quasi cyclic low density parity check codes. Furthermore, we will prove that the designed QC-LDPC codes have no circles shorter than six. The performance of the codes is also investigated.

## IC Design of a Low-Power Analog LDPC Decoder Employing New Stopping Iteration Method

- **Status**: ✅
- **Reason**: 아날로그 LDPC 디코더 신규 정지반복법(min-sum 기반) HW 구현, 이식 가능 D/C
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6682083
- **Type**: conference
- **Published**: 20-23 Aug.
- **Authors**: Wen-Ta Lee, Sheng-Sung Chiu, Yu-Shi Ke
- **PDF**: https://ieeexplore.ieee.org/document/6682083
- **Abstract**: This paper proposes an analog LDPC decoder employing new stopping iteration method. It is based on the min-sum algorithm and by checking parity H-matrix to decide iteration termination. The proposed method not only can increase the decoding throughput but also decrease the power consumption. Experimental results show that this decoder can save 90% power consumption speed ratio compared with traditional decoders. Finally, an analog (32, 8) min-sum decoder with new stopping iteration method is implemented by TSMC 0.18μm 1P6M CMOS technology. When the data throughput and supply voltage is 216 Mb/s and 1.8V respectively, the power consumption is only 4.98 mW. This analog decoder has low power and small area characteristics that can be applicable to green communication devices.

## Construction of quasi-cyclic LDPC codes based on euclidean geometries

- **Status**: ✅
- **Reason**: 유클리드기하 기반 QC-LDPC 신규 구성, girth>=6, error floor 개선 - 바이너리 코드설계 기법(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6694726
- **Type**: conference
- **Published**: 14-16 Aug.
- **Authors**: Yuan-hua Liu, Mei-ling Zhang
- **PDF**: https://ieeexplore.ieee.org/document/6694726
- **Abstract**: A new method for constructing quasi-cyclic (QC) low-density parity-check (LDPC) codes based on the structural properties of Euclidean geometries is presented. The proposed method changes the incidence vectors of some lines in the original Euclidean geometry method to construct much more parity check matrices and results in a large class of QC-LDPC codes with girth of at least 6. Simulations show that some codes in this class have better performance and lower error floor than the original Euclidean geometry codes.

## The modified reliability-based iterative majority-logic decoding algorithm with non-uniform quantization

- **Status**: ✅
- **Reason**: 신뢰도기반 반복 다수결 디코딩 + 비균일 양자화(3-4비트) - LLR 양자화/디코더 기법 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6694719
- **Type**: conference
- **Published**: 14-16 Aug.
- **Authors**: Haiqiang Chen, Lingshan Luo, Youming Sun +2
- **PDF**: https://ieeexplore.ieee.org/document/6694719
- **Abstract**: This paper investigates the performances of the modified reliability-based iterative majority-logic decoding (MRBI-MLGD) algorithm under different quantization schemes. An efficient non-uniform quantization method is presented for the MRBI-MLGD algorithm. With the non-uniform strategy, the real received symbols will be quantized into integer values before passing to the decoder. The quantized reliability measures exhibit a non-uniform distribution with respect to their original received signals. Furthermore, the quantization resolution can be modified as required. Simulation results show that, when combined with factor correction techniques and a proper quantization parameter r, the MRBI-MLGD with nonuniform quantization performs well with very small quantized bits (3–4 bits) and has very fast decoding convergence speed.
