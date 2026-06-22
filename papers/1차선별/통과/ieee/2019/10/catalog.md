# IEEE Xplore — 2019-10 (1차선별 통과)


## Asymptotic Average Multiplicity of Structures Within Different Categories of Trapping Sets, Absorbing Sets, and Stopping Sets in Random Regular and Irregular LDPC Code Ensembles

- **Status**: ✅
- **Reason**: LDPC trapping/absorbing/stopping set의 점근적 다중도 분석 — error floor 구조 이해/코드설계에 이식 가능(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8736998
- **Type**: journal
- **Published**: Oct. 2019
- **Authors**: Ali Dehghan, Amir H. Banihashemi
- **PDF**: https://ieeexplore.ieee.org/document/8736998
- **Abstract**: The performance of low-density parity-check (LDPC) codes in the error floor region is closely related to some substructures of the code's Tanner graph, collectively referred to as trapping sets (TSs). In this paper, we study the asymptotic average number of different types of trapping sets such as elementary TSs (ETS), leafless ETSs (LETS), absorbing sets (ABS), elementary ABSs (EABS), and stopping sets (SS), in random variable-regular and irregular LDPC code ensembles. We demonstrate that, regardless of the type of the TS, as the code's length tends to infinity, the average number of a given structure tends to infinity, to a positive constant, or to zero, if the structure contains no cycle, only one cycle, or more than one cycle, respectively. For the case where the structure contains a single cycle, we derive the asymptotic expected multiplicity of the structure by counting the average number of its constituent cycles and all the possible ways that the structure can be constructed from the cycle. This, in general, involves computing the expected number of cycles of a certain length with a certain given combination of node degrees, or computing the expected number of cycles of a certain length expanded to the desired structure by the connection of trees to its nodes. The asymptotic results obtained in this work, which are independent of the block length and only depend on the code's degree distributions, are shown to be accurate even for finite-length codes.

## Efficient Post-Processors for Improving Error-Correcting Performance of LDPC Codes

- **Status**: ✅
- **Reason**: LDPC error floor 완화를 위한 신규 post-processor(simulated annealing 기반 quenching/heating)를 BP 디코더에 통합 — 이식 가능 디코더/error floor 기법(C/E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8725915
- **Type**: journal
- **Published**: Oct. 2019
- **Authors**: Yaoyu Tao, Shuanghong Sun, Zhengya Zhang
- **PDF**: https://ieeexplore.ieee.org/document/8725915
- **Abstract**: The error floor phenomenon, associated with iterative decoders, is one of the most significant limitations to the applications of low-density parity-check (LDPC) codes. A variety of techniques from code design to decoder implementation have been proposed to address the error floor problem, among which post-processors have shown to be both effective and implementation-friendly. In this paper, we take the inspiration from simulated annealing to generalize the post-processor design using three methods: quenching, extended heating, and focused heating, each of which targets a different error structure. The resulting post-processor is demonstrated to lower the error floors by two orders of magnitude for two structured code examples, a (2209, 1978) array LDPC code and a (1944, 1620) LDPC code used by the IEEE 802.11n standard. The post-processor can be integrated with a belief-propagation decoder with minimal overhead. The post-processor design is equally applicable to other structured LDPC codes.

## On the Design of Multi-Edge Type Low-Density Parity-Check Codes

- **Status**: ✅
- **Reason**: Multi-edge type 바이너리 LDPC의 신규 설계 규칙(탐색공간 제약 제거, threshold 개선) — 이식 가능 코드 설계(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8758347
- **Type**: journal
- **Published**: Oct. 2019
- **Authors**: Suhwang Jeong, Jeongseok Ha
- **PDF**: https://ieeexplore.ieee.org/document/8758347
- **Abstract**: Since multi-edge type low-density parity-check (MET-LDPC) codes were first proposed, the design of MET-LDPC codes has been extensively studied for various applications. However, the existing design rules assume that check node degrees are in the so-called concentrated form which enables one to conveniently find pairs of edge and node distributions satisfying the socket count equalities (SCEs). However, it in return makes the code design conducted in a limited search space, which may lead to a sub-optimal design. This paper proposes a novel design rule for MET-LDPC codes together with a scheme to efficiently sort out invalid distributions, i.e., ones not satisfying the SCEs, in the design process. The proposed design rule does not require check node degrees to be in the concentrated form and can find out optimized MET-LDPC codes without any restriction on the search space. Based on the proposed design rule, MET-LDPC codes are designed across a wide range of code rates on binary-erasure channel and binary-input additive-white Gaussian channel. The designed codes are compared with ones reported in the open literature, which confirms that MET-LDPC codes with the proposed design rule have better threshold performances regardless of channel and code rate even with sets of limited code parameters.

## Thresholds of Absorbing Sets Under Scaled Min-Sum LDPC Decoding

- **Status**: ✅
- **Reason**: Scaled min-sum LDPC 디코딩에서 absorbing set threshold 분석 및 scaling factor로 비활성화 — 이식 가능 디코더/error floor 기법(C/E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8752015
- **Type**: journal
- **Published**: Oct. 2019
- **Authors**: Marco Ferrari, Alessandro Tomasoni, Ramon Marenzi +1
- **PDF**: https://ieeexplore.ieee.org/document/8752015
- **Abstract**: In this paper, the definition of threshold of elementary absorbing sets is extended to scaled Min-Sum low-density parity-check (LDPC) decoding. Based on the analysis of the behavior of scaled Min-Sum LDPC decoders in the Tanner graph of the absorbing set, it is proven that correct decoding is guaranteed with received channel messages above threshold. A fast algorithm for the threshold computation is derived. Many examples of absorbing sets taken from LDPC codes of various variable node degrees are investigated, and it is shown that all of them can be deactivated with low enough scaling factors.

## A sectional degree match approximate Min-sum decoding algorithm for LDPC

- **Status**: ✅
- **Reason**: 바이너리 LDPC용 sectional degree match 근사 min-sum 신규 알고리즘, HW 구현 고려 — 이식 가능 디코더(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8911623
- **Type**: conference
- **Published**: 30 Sept.-2
- **Authors**: Ruizhen Wu, Lin Wang, Tao Yuan +1
- **PDF**: https://ieeexplore.ieee.org/document/8911623
- **Abstract**: A sectional degree match approximate Min-sum decoding algorithm for LDPC is proposed in this paper. The degradation factor from BP to MS is analyzed and a proposal to offset it, is explained, with expansion and optimization based on principles of hardware implementation. The decoding algorithm summarizes three correction approximate algorithms considering different LLR values, matrix degrees and rules of hardware implementation. Simulation is following LDPC NR 3GPP 38.212 release and the comparison results demonstrate that the proposed sectional degree match approximate Min-sum decoding algorithm has a better BER and less iteration time. The hardware implementation of this algorithm is strived from Min-Sum decoder and the extra cost is minor besides the memory.

## Joint Equalization and LDPC Decoding

- **Status**: ✅
- **Reason**: DFE 등화를 LDPC 메시지패싱에 직접 통합하는 새 디코더 구조 제안; 부호 비의존 BP 개선으로 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8970730
- **Type**: conference
- **Published**: 28-30 Oct.
- **Authors**: Werner Henkel, Nazia S. Islam, M. Ahmed Leghari
- **PDF**: https://ieeexplore.ieee.org/document/8970730
- **Abstract**: Encoding and channel convolution and the corresponding equalization and decoding are a serial concatenation. One might consider the solution to be iterative equalization and decoding in a Turbo fashion. We are showing that it is not necessary to run LDPC decoding and equalization as separate entities in a Turbo manner, but integrate decision-feedback equalization (DFE) directly into the LDPC decoder, performing DFE-like operations as part of the LDPC message passing.

## Concatenated Reed-Solomon/Spatially Coupled LDPC Codes

- **Status**: ✅
- **Reason**: SC-LDPC를 large girth·locally systematic로 설계해 error floor 제거 — 이식 가능 바이너리 LDPC 코드설계 기법(E). RS는 외부 concatenation일 뿐
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8928034
- **Type**: conference
- **Published**: 23-25 Oct.
- **Authors**: Jie Qiu, Shiqiu Liu, Li Chen
- **PDF**: https://ieeexplore.ieee.org/document/8928034
- **Abstract**: Spatially coupled (SC) low-density parity-check (LDPC) codes can achieve capacity approaching belief propagation (BP) decoding performance with low message recovery latency when using the sliding window decoding (SWD). The SWD is suitable for data stream transmission but cannot always correct all errors in the targeted symbol set. A further decoding stage would be desirable to eliminate the remaining errors from SWD. This paper proposes a novel concatenated coding scheme where the Reed-Solomon (RS) codes and the SC-LDPC codes are chosen as the outer code and the inner code, respectively, namely the RS-SC-LDPC codes. Consequently, the remaining errors from SWD can be corrected by the outer RS codes. In the concatenated coding scheme, the inner SC-LDPC code is designed such that it has a large girth and locally systematic encoding property. Our simulation results show the RS-SC-LDPC codes can achieve a high decoding performance, while the error floor of the inner code can be removed.

## A Reduced-Complexity ADMM Based Decoding Algorithm for LDPC Codes

- **Status**: ✅
- **Reason**: ADMM LP 디코딩의 check polytope projection 복잡도 저감(trend extrapolation) 신규 디코더 알고리즘 — 바이너리 LDPC 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8928121
- **Type**: conference
- **Published**: 23-25 Oct.
- **Authors**: Zhibiao Liang, Xiang Chen, Xinghua Sun +1
- **PDF**: https://ieeexplore.ieee.org/document/8928121
- **Abstract**: Alternating Direction Method of Multipliers (ADM-M) is an effective method for Linear Programming (LP) decoding of Low-Density Parity-Check (LDPC) codes. In the ADMM-based LDPC decoding algorithm, Euclidean projection on the check polytope is the key step. Current Euclidean projection algorithms in general require either sorting or iterative operations. However, when decoding LDPC codes with high coding rate, the sorting operation brings a high level of computation complexity. Moreover, although the current iterative projection algorithms do not involve the complex operation of sorting, its convergence speed is slow. In this paper, based on trend extrapolation, a reduced-complexity iterative check polytope projection algorithm is proposed. In the proposed algorithm, the target projection point can be found based on the variation trend of the geometric position of the projection points obtained from previous iterations. Therefore, it ensures fast convergence and does not sacrifice on bit error rate (BER) performance. The simulation results confirm that the proposed algorithm can effectively reduce the decoding complexity, especially for LDPC codes with high coding rate.

## Tabu-List Noisy Gradient Descent Bit Flipping Decoding of LDPC Codes

- **Status**: ✅
- **Reason**: LDPC용 Tabu-List NGDBF 비트플립 디코더 개선 — 이식 가능 디코더 알고리즘 (C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8927932
- **Type**: conference
- **Published**: 23-25 Oct.
- **Authors**: Li Zhang, Nan Liu, Zhiwen Pan +1
- **PDF**: https://ieeexplore.ieee.org/document/8927932
- **Abstract**: The Noisy Gradient Descent Bit Flipping (NGDBF) algorithm surpasses the previous Gradient Descent Bit Flipping (GDBF) and other Bit Flipping (BF) algorithms for decoding Low-Density Parity-Check (LDPC) codes. However, the NGDBF decoder sometimes cannot escape from the local maxima. To further enhance the performance of the NGDBF algorithm, an improved NGDBF algorithm called Tabu-List Noisy Gradient Descent Bit Flipping (TNGDBF) is proposed in this paper. A tabu-list is employed to help the NGDBF decoder escape from the local maxima. It is shown in the simulation results that the TNGDBF algorithm gains about 0.2 dB performance compared with NGDBF at the cost of a small amount of complexity increase.

## Construction of Finite Field Based QC-LDPC Codes from Isomorphism Perspective

- **Status**: ✅
- **Reason**: 유한체 기반 QC-LDPC 동형 관점 구성으로 girth↑·단주기↓ — 바이너리 코드 설계 (E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8927973
- **Type**: conference
- **Published**: 23-25 Oct.
- **Authors**: Huaan Li, Hengzhou Xu, Baoming Bai +2
- **PDF**: https://ieeexplore.ieee.org/document/8927973
- **Abstract**: There are many algebraic tools, e.g., finite fields and combinatorial designs, for constructing good quasi-cyclic LDPC (QC-LDPC) codes. In particular, QC-LDPC codes designed based on two arbitrary subsets of a given finite field perform very well and some well-known algebraic constructions of QC-LDPC codes have been verified as special cases of this method. How to choose these two subsets to further improve the performance of finite field based QC-LDPC codes is of interest. In this paper, we study such codes and analyze their structural properties from isomorphism perspective, and generalize some rules to efficiently determine the non-isomorphic finite field based codes. By comparing the cycle distributions of non-isomorphic codes, we can easily construct the finite field based QC-LDPC codes with larger girth and fewer short cycles. These codes generally perform very well and can be used as the ingredients of some further processings, e.g., masking. Numerical results show that the constructed codes have better performance with the iterative decoding algorithms.

## Polarized Low-Density Parity-Check Codes on the BSC

- **Status**: ✅
- **Reason**: polar 생성행렬 구조에서 영감받은 새 LDPC 구성(polarized LDPC)으로 BSC error floor 저감 — 신규 바이너리 LDPC 코드설계(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8928082
- **Type**: conference
- **Published**: 23-25 Oct.
- **Authors**: Binbin Gao, Huarui Yin, Zhengdao Wang
- **PDF**: https://ieeexplore.ieee.org/document/8928082
- **Abstract**: The connections between variable nodes and check nodes have a great influence on the performance of low-density parity-check (LDPC) codes. Inspired by the unique structure of polar code's generator matrix, we proposed a new method of constructing LDPC codes that achieves a polarization effect. The new code, named as polarized LDPC codes, is shown to achieve lower or no error floor in the binary symmetric channel (BSC).

## On the performance analysis of short LDPC codes

- **Status**: ✅
- **Reason**: 단척 (128,256) LDPC 2250개 FPGA 시뮬, Tanner그래프 특성(Laplacian eigenvalue)으로 디코딩 임계 예측 — 코드설계(E) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9003310
- **Type**: conference
- **Published**: 21-25 Oct.
- **Authors**: Luiza R. Medova, Pavel S. Rybin, Ivan V. Filatov
- **PDF**: https://ieeexplore.ieee.org/document/9003310
- **Abstract**: This paper presents the research on LDPC codes performance depending on several Tanner graph properties. We have simulated 2250 (128,256) different LDPC codes in FPGA and explored their waterfall region as a function of the graph characteristics. These characteristics are different graph centralization measures and the second smallest Laplacian eigenvalue. We have received numerical values that distinguish LDPC codes with a good decoding threshold (less or equal 3.5 dB) from others. In addition, we developed a polynomial regression model that accurately predicts the LDPC decoding threshold with a coefficient of determination equal to 0.87 and RMSE equal 0.16 dB.

## On the Hard-Decision Multi-Threshold Decoding of Binary and Non-Binary LDPC Codes

- **Status**: ✅
- **Reason**: 바이너리 LDPC hard-decision 다중임계 디코딩 신규 기법(C), 비이진 부분은 제외하되 바이너리 디코더 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9003311
- **Type**: conference
- **Published**: 21-25 Oct.
- **Authors**: Andrei Dzis, Pavel Rybin, Alexey Frolov
- **PDF**: https://ieeexplore.ieee.org/document/9003311
- **Abstract**: In this paper, we investigate the effect of single and multiple thresholds approaches applied to iterative hard-decision decoders for binary and non-binary low-density parity-check (LDPC) codes in terms of error correction and managed to optimize the performance of decoding algorithms for these codes.

## Decoding Scheduling for Unequal Error Protection Quasi-Cyclic Low-Density Parity-Check Codes

- **Status**: ✅
- **Reason**: UEP QC-LDPC 전용 신규 디코딩 스케줄링 3종 제시, 수렴가속·복잡도 절감 — 이식 가능 디코더(C)/구성(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8966090
- **Type**: conference
- **Published**: 20-24 Oct.
- **Authors**: Jia-Jyun Wu, Chung-Hsuan Wang, Chi-chao Chao
- **PDF**: https://ieeexplore.ieee.org/document/8966090
- **Abstract**: Algebraic constructions of quasi-cyclic (QC) low-density parity-check (LDPC) codes with unequal error protection (UEP) capabilities have recently been proposed, which can provide different error-correcting capabilities for different parts of the coded bits. However, conventional decoding algorithms are not designed for LDPC codes with UEP. In this paper, we propose three decoding schemes for UEP QC-LDPC codes extended from existing scheduling strategies, tailored to the special structures of the parity-check matrices. Simulation results show that the proposed schemes can provide improved error rate performance especially for coded bits on low protection levels. The decoding convergence can also be accelerated, thereby reducing the computational complexity.

## A Channel-Blind Decoding for LDPC Based on Deep Learning and Dictionary Learning

- **Status**: ✅
- **Reason**: 채널 추정 불필요 blind LDPC 디코딩(딕셔너리+딥러닝, Min-Sum/BP 개선) — 이식 가능 디코더 알고리즘(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9020628
- **Type**: conference
- **Published**: 20-23 Oct.
- **Authors**: Xu Pang, Chao Yang, Zaichen Zhang +2
- **PDF**: https://ieeexplore.ieee.org/document/9020628
- **Abstract**: Low-density parity-check (LDPC) codes are used to correct encoding errors that occur during transmission, which enjoys an excellent performance. The performance of existing Min-Sum decoders for LDPC codes relies heavily on accurate channel estimation. A two-dimensional blind channel decoding algorithm that does not require precise channel estimation is presented in this paper. The algorithm converts the original one-dimensional signal into a two-dimensional LDPC signal according to the template. Dictionary learning is introduced for pre-filtering, and deep learning is adopted for further denoising and decoding. It is revealed that the two-dimensional blind decoding algorithm has a significant improvement over the traditional belief propagation (BP) decoding algorithm when the channel noise is unknown. Moreover, the combination of dictionary learning and deep learning has a great improvement in performance and data size reduction.

## AVX-512 Based Software Decoding for 5G LDPC Codes

- **Status**: ✅
- **Reason**: 5G LDPC AVX-512 SIMD 소프트웨어 디코딩, 레이어드 디코딩 병렬화 기법 — 이식 가능 디코더/구현 병렬화(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9020587
- **Type**: conference
- **Published**: 20-23 Oct.
- **Authors**: Yi Xu, Wenjin Wang, Zhen Xu +1
- **PDF**: https://ieeexplore.ieee.org/document/9020587
- **Abstract**: In this paper, we investigate how the 5G NR LDPC codes can be decoded by GPP effectively with single instruction-multiple-data (SIMD) acceleration and evaluate the corresponding achievable throughput on newly released Intel Xeon CPUs. Firstly, a general software implementation architecture with SIMD acceleration for horizontal-layered LDPC decoding is presented, where the parallelism can be achieved in an intra-block manner. By utilizing Intel advanced vector extended 512 (AVX-512) instruction set, the efficiency of parallelism are maximized and therefore the capacity of x86 processors can be fully exploited. In addition, new features of AVX-512 are further exploited to optimize load and store operations as well as preprocessing to reduce the operation cost. Experiments results also show that Intel Xeon Gold 6154 processors can achieve 42 to 272 Mbps throughput with a single core for ten layered decoding iterations for various code rate and block length. The typical processing latency is below 100 $\mu s$. Consequently, an 18-core Intel Xeon CPU can achieve up to 5 Gbps decoding throughput.

## Deep Unfolding for Communications Systems: A Survey and Some New Directions

- **Status**: ✅
- **Reason**: deep unfolding 서베이지만 BP 디코딩 unfolding을 구체적으로 다룸 — 이식 가능 디코더 기법 정리(C), 예외 포함
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9020494
- **Type**: conference
- **Published**: 20-23 Oct.
- **Authors**: Alexios Balatsoukas-Stimming, Christoph Studer
- **PDF**: https://ieeexplore.ieee.org/document/9020494
- **Abstract**: Deep unfolding is a method of growing popularity that fuses iterative optimization algorithms with tools from neural networks to efficiently solve a range of tasks in machine learning, signal and image processing, and communication systems. This survey summarizes the principle of deep unfolding and discusses its recent use for communication systems with focus on detection and precoding in multi-antenna (MIMO) wireless systems and belief propagation decoding of error-correcting codes. To showcase the efficacy and generality of deep unfolding, we describe a range of other tasks relevant to communication systems that can be solved using this emerging paradigm. We conclude the survey by outlining a list of open research problems and future research directions.

## Analysis of the Short Cycles on the Performance of LDPC Coded OFDM Underwater Acoustic System

- **Status**: ✅
- **Reason**: 규칙 LDPC 행렬에서 short cycle 제거 신규 2기법 제안 — 바이너리 LDPC 사이클 제거(E)로 이식 가능, 응용은 UWA지만 코드설계 기법 분리 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9095155
- **Type**: conference
- **Published**: 18-20 Oct.
- **Authors**: Lu Ma, Feng Xiao, Xinyu Liu
- **PDF**: https://ieeexplore.ieee.org/document/9095155
- **Abstract**: In recent years, OFDM technology has been increasingly used in the underwater acoustic (UWA) communication systems due to its high spectral efficiency. Since the underwater environment noise is high and the multipath and Doppler effects are serious, it is necessary to introduce error correction code in the OFDM system. LDPC code, with its excellent error correction capability, is close to the Shannon limit under the AWGN channel, and the implementation complexity is low, which is more and more applied to various communication systems. The existence of short cycles in random matrix has great influence on LDPC code performance when the decoding method is determined. In this paper, we design a set of OFDM UWA system combined with LDPC coding. Based on the regular random matrix, two methods for eliminating short cycles are proposed, and the performance of the two method is evaluated in the simulated UWA channel.

## FPGA Design and Implementation of DVB-S2/S2X LDPC Encoder

- **Status**: ✅
- **Reason**: DVB-S2/S2X LDPC 인코더 FPGA 아키텍처(저자원·패리티계산기 재사용) — 이식 가능 HW 기여(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:8906811
- **Type**: conference
- **Published**: 17-18 Oct.
- **Authors**: A.V. Lazarenko
- **PDF**: https://ieeexplore.ieee.org/document/8906811
- **Abstract**: A new FPGA architecture of the DVB-S2/S2X LDPC FEC encoder with low number of resources consumption is proposed. The encoder is full rate compatible and supports all code rates from DVB-S2/S2X standards. In addition, all frame types (normal, medium and short) are supported. The proposed architecture is based on iterative addresses calculation of parity bits accumulators and actively reuses parity calculators and parity storage. The Kintex FPGA implementation of the proposed architecture is done resulting in less than 3000 look-up-tables and flip-flops and only 6 block memories usage.

## A Robust Uplink Transmission Scheme for Interactive Services in Future Broadcasting Systems

- **Status**: ✅
- **Reason**: QC-SC-LDPC 코드를 IDMA용으로 유한길이·반복제약 고려해 구성 — 이식 가능 코드설계(E) 가능성, 애매하여 in
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8906824
- **Type**: conference
- **Published**: 17-18 Oct.
- **Authors**: Yushu Zhang, Kewu Peng, Jian Song +1
- **PDF**: https://ieeexplore.ieee.org/document/8906824
- **Abstract**: A dedicated return channel (DRC) for terrestrial broadcasting systems is considered to support interactive services. Compared with orthogonal multiple access based random access, non-orthogonal multiple access (NOMA) based random access technology is capable of supporting massive connectivity with higher reliability. In this paper, quasi-cyclic spatially coupled low-density parity-check (QC-SC-LDPC) coded interleave-division multiple access (IDMA) is proposed as a robust uplink physical layer solution for DRC in future terrestrial broadcasting systems. More specifically, QC-SC-LDPC codes, which have been recently proven to be universally capacity-achieving over different channels, are constructed for IDMA to exploit the inherent universality against the variations of spectral efficiencies, while the practical constraints of finite code length and number of decoding iterations are taken into account. Finally, simulations are carried out to verify the performance and robustness of the constructed QC-SC-LDPC coded IDMA scheme.

## The Optimized Scheme for FPGA-based LDPC codes using Particle Swarm Optimization

- **Status**: ✅
- **Reason**: PSO로 LDPC BP 디코딩 차수분포 최적화하는 새 디코딩 기법(C/E), 부호 비의존적 이식 가능성
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8939842
- **Type**: conference
- **Published**: 16-18 Oct.
- **Authors**: Dong-Hee Noh, Sung-Hwan Jeong, JuHwan Choi
- **PDF**: https://ieeexplore.ieee.org/document/8939842
- **Abstract**: This paper proposes the enhanced BP decoding scheme of Low-density parity-check (LDPC) codes scheme using Particle Swarm Optimization (PSO) algorithm. New approaches to this paper describe the BP decoding scheme using PSO algorithm. Its scheme can optimize the degree distribution pairs of check and variable node over rician channel. Therefore, proposed scheme can improve the throughput performance for wireless sensor networks over the industrial environment such as military or agriculture application.

## Density Evolution of the Bit-Flipping Decoding Algorithm of Regular Low-Density Parity-Check Codes

- **Status**: ✅
- **Reason**: 정규 LDPC bit-flipping 디코더의 density evolution 신규 분석(C), 바이너리 LDPC 디코더 분석 기법
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8939981
- **Type**: conference
- **Published**: 16-18 Oct.
- **Authors**: Myungin Kim, Jeongseok Ha
- **PDF**: https://ieeexplore.ieee.org/document/8939981
- **Abstract**: In this paper, we develop the density evolution of bit-flipping algorithm (BFA) for regular low-density parity-check (LDPC) codes and analyze the evolution of probability density for the bit-decision error. In contrast to the sum-product algorithm (SPA) and min-sum algorithm (MSA), the density evolution for BFA has remained untouched, which motivates this work. In the developed density evolution for BFA, we first introduce a state variable which is a function of bit-decision result and the flipping function value at each iteration. Then, the state probability is derived, with which the density of bit-decision error is obtained. To confirm the derivations, we design regular LDPC codes and compare the empirical evaluations of bit-error rates and the derived probability of bit-decision errors.

## Performance Analysis and Implementation of LDPC for DOCSIS 3.1 Uplink

- **Status**: ✅
- **Reason**: DOCSIS 3.1 LDPC 인코더/디코더 구현, 떼어낼 수 있는 HW 구현 기법(D) 존재 가능성 — 애매하여 살림
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:8939712
- **Type**: conference
- **Published**: 16-18 Oct.
- **Authors**: Jewon Lee, Joon-Young Jung
- **PDF**: https://ieeexplore.ieee.org/document/8939712
- **Abstract**: Data over cable service interface specification 3.1 (DOCSIS 3.1) is released to provide multi-gigabit data service in hybrid fiber coaxial (HFC) networks. To support the data rate of DOCSIS 3.1 uplink, the low density parity check (LDPC) decoding processing speed is required as corresponding to the data rate. We implement the LDPC encoder and decoder based on the DOCSIS 3.1 uplink and verify them by the laboratory test. The results of the laboratory test show that the implemented LDPC encoder and decoder conforms to the DOCSIS 3.1 uplink.

## A Novel Data Packing Technique for QC-LDPC Decoder Architecture applied to NAND flash controller

- **Status**: ✅
- **Reason**: NAND flash QC-LDPC 디코더 신규 data packing + shift network 아키텍처 (A/D 직접)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9015393
- **Type**: conference
- **Published**: 15-18 Oct.
- **Authors**: Longyu Ma, Hong-Fu Chou, Chiu-Wing Sham
- **PDF**: https://ieeexplore.ieee.org/document/9015393
- **Abstract**: This paper presents a data packing technique for Quasi-Cyclic LDPC codes decoder applied to NAND flash controller which has the challenge of long code length implementation due to high complexity and routing congestion on floor planning. Firstly, we introduce a proposed shift network to reorder the channel data sequence. The data packing mechanism is designed to be generic. Secondly, the proposed LDPC architecture is desgined to overcome complicated routing problems caused by random accessing of massage passing within the LDPC decoder. Based on the proposed architecture, the hardware description has been synthesized on Design Compiler using a TSMC 0.18um model and an FPGA-based floor planning with the implementing result has also been provided. Synthesis results also show that the area and throughput of the proposed decoder has desirable performance for the application of NAND flash controller.

## Work-in-Progress: ECC Management with Rate Compatible LDPC Code for NAND Flash Storage

- **Status**: ✅
- **Reason**: A: NAND 플래시 직접 — rate-compatible LDPC 인코딩/디코딩 + 잉여 패리티 관리로 P/E 주기별 코드레이트 조정
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8944379
- **Type**: conference
- **Published**: 13-18 Oct.
- **Authors**: Jae-Bin Lee, Geon-Myeong Kim, Seung-Ho Lim
- **PDF**: https://ieeexplore.ieee.org/document/8944379
- **Abstract**: The NAND flash memory has rapidly increased in storage capacity per unit area, and the rate of occurrence of errors per P/E cycle is also rapidly increasing accordingly. ECC modules such as LDPC have been added to flash controller for recovering from the errors. However, the system designs to increase the lifetime of the flash memory storage device are still in great demand. In this paper, we design the LDPC encoding and decoding scheme to get stepwise code rate according to the P/E cycle by applying rate-compatible LDPC, as well as the management scheme of excessive parity data. Through this, we can improve the error recovery rate of flash memory storage system and extend the lifetime of NAND flash storage system while reducing the system read and write overhead due to the increase in additional parity data.
