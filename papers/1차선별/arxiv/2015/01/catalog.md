# arXiv — 2015-01 (1차선별 통과)


## Design of a Unified Transport Triggered Processor for LDPC/Turbo Decoder

- **Status**: ✅
- **Reason**: LDPC/turbo 공용 TTA 프로세서 + supercode 기반 sum-product 체크노드 연산, 이식 가능 HW 아키텍처(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: arxiv:1502.00076v1
- **Type**: preprint
- **Published**: 2015-01-31
- **Authors**: Shahriar Shahabuddin, Janne Janhunen, Muhammet Fatih Bayramoglu +3
- **PDF**: https://arxiv.org/pdf/1502.00076v1
- **Abstract**: This paper summarizes the design of a programmable processor with transport triggered architecture (TTA) for decoding LDPC and turbo codes. The processor architecture is designed in such a manner that it can be programmed for LDPC or turbo decoding for the purpose of internetworking and roaming between different networks. The standard trellis based maximum a posteriori (MAP) algorithm is used for turbo decoding. Unlike most other implementations, a supercode based sum-product algorithm is used for the check node message computation for LDPC decoding. This approach ensures the highest hardware utilization of the processor architecture for the two different algorithms. Up to our knowledge, this is the first attempt to design a TTA processor for the LDPC decoder. The processor is programmed with a high level language to meet the time-to-market requirement. The optimization techniques and the usage of the function units for both algorithms are explained in detail. The processor achieves 22.64 Mbps throughput for turbo decoding with a single iteration and 10.12 Mbps throughput for LDPC decoding with five iterations for a clock frequency of 200 MHz.

## Generalized Simplified Variable-Scaled Min Sum LDPC decoder for irregular LDPC Codes

- **Status**: ✅
- **Reason**: 불규칙 LDPC용 저복잡도 variable-scaled min-sum 변형 디코더 — 이식 가능 디코더 알고리즘(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: arxiv:1501.07336v1
- **Type**: preprint
- **Published**: 2015-01-29
- **Authors**: Ahmed A. Emran, Maha Elsabrouty
- **PDF**: https://arxiv.org/pdf/1501.07336v1
- **Abstract**: In this paper, we propose a novel low complexity scaling strategy of min-sum decoding algorithm for irregular LDPC codes. In the proposed method, we generalize our previously proposed simplified Variable Scaled Min-Sum (SVS-min-sum) by replacing the sub-optimal starting value and heuristic update for the scaling factor sequence by optimized values. Density evolution and Nelder-Mead optimization are used offline, prior to the decoding, to obtain the optimal starting point and per iteration updating step size for the scaling factor sequence of the proposed scaling strategy. The optimization of these parameters proves to be of noticeable positive impact on the decoding performance. We used different DVB-T2 LDPC codes in our simulation. Simulation results show the superior performance (in both WER and latency) of the proposed algorithm to other Min-Sum based algorithms. In addition to that, generalized SVS-min-sum algorithm has very close performance to LLR-SPA with much lower complexity.

## Protograph-Based LDPC Code Design for Bit-Metric Decoding

- **Status**: ✅
- **Reason**: protograph 기반 바이너리 LDPC 코드 설계 기법, surrogate 채널로 차수 최적화 — 이식 가능 코드 설계(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: arxiv:1501.05595v1
- **Type**: preprint
- **Published**: 2015-01-22
- **Authors**: Fabian Steiner, Georg Böcherer, Gianluigi Liva
- **PDF**: https://arxiv.org/pdf/1501.05595v1
- **Abstract**: A protograph-based low-density parity-check (LDPC) code design technique for bandwidth-efficient coded modulation is presented. The approach jointly optimizes the LDPC code node degrees and the mapping of the coded bits to the bit-interleaved coded modulation (BICM) bit-channels. For BICM with uniform input and for BICM with probabilistic shaping, binary-input symmetric-output surrogate channels are constructed and used for code design. The constructed codes perform as good as multi-edge type codes of Zhang and Kschischang (2013). For 64-ASK with probabilistic shaping, a blocklength 64800 code is constructed that operates within 0.69 dB of 0.5log(1+SNR) at a spectral efficiency of 4.2 bits/channel use and a frame error rate of 1e-3.

## Band Splitting Permutations for Spatially Coupled LDPC Codes Enhancing Burst Erasure Immunity

- **Status**: ✅
- **Reason**: SC-LDPC band splitting permutation으로 버스트 정정 향상 — 바이너리 SC-LDPC 코드 설계(E), NAND 버스트성 적용 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: arxiv:1501.04394v1
- **Type**: preprint
- **Published**: 2015-01-19
- **Authors**: Hiroki Mori, Tadashi Wadayama
- **PDF**: https://arxiv.org/pdf/1501.04394v1
- **Abstract**: It is well known that spatially coupled (SC) codes with erasure-BP decoding have powerful error correcting capability over memoryless erasure channels. However, the decoding performance of SC-codes significantly degrades when they are used over burst erasure channels. In this paper, we propose band splitting permutations (BSP) suitable for $(l,r,L)$ SC-codes. The BSP splits a diagonal band in a base matrix into multiple bands in order to enhance the span of the stopping sets in the base matrix. As theoretical performance guarantees, lower and upper bounds on the maximal burst correctable length of the permuted $(l,r,L)$ SC-codes are presented. Those bounds indicate that the maximal correctable burst ratio of the permuted SC-codes converges to 1/k where k=r/l. This implies the asymptotic optimality of the permuted SC-codes in terms of burst erasure correction.

## Design of LDPC Codes Robust to Noisy Message-Passing Decoding

- **Status**: ✅
- **Reason**: 노이즈 메시지패싱 디코딩에 강건한 LDPC 설계 + 2D density evolution, HW 내부노이즈 강건성 — 이식 가능 디코더/설계(C/E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: arxiv:1501.02483v3
- **Type**: preprint
- **Published**: 2015-01-11
- **Authors**: Alla Tarighati, Hamed Farhadi, Farshad Lahouti
- **PDF**: https://arxiv.org/pdf/1501.02483v3
- **Abstract**: We address noisy message-passing decoding of lowdensity parity-check (LDPC) codes over additive white Gaussian noise channels. Message-passing decoders in which certain processing units iteratively exchange messages are common for decoding LDPC codes. The exchanged messages are in general subject to internal noise in hardware implementation of these decoders. We model the internal decoder noise as additive white Gaussian noise (AWGN) degrading exchanged messages. Using Gaussian approximation of the exchanged messages, we perform a two-dimensional density evolution analysis for the noisy LDPC decoder. This makes it possible to track both the mean, and the variance of the exchanged message densities, and hence, to quantify the threshold of the LDPC code in the presence of internal decoder noise. The numerical and simulation results are presented that quantify the performance loss due to the internal decoder noise. To partially compensate this performance loss, we propose a simple method, based on EXIT chart analysis, to design robust irregular LDPC codes. The simulation results indicate that the designed codes can indeed compensate part of the performance loss due to the internal decoder noise.
