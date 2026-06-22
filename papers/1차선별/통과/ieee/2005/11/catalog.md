# IEEE Xplore — 2005-11 (1차선별 통과)


## LDPC codes from generalized polygons

- **Status**: ✅
- **Reason**: generalized polygon 기반 QC-LDPC 구성, 큰 girth·최소거리 보장 바이너리 코드설계 기법(E) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1522647
- **Type**: journal
- **Published**: Nov. 2005
- **Authors**: Zhenyu Liu, D.A. Pados
- **PDF**: https://ieeexplore.ieee.org/document/1522647
- **Abstract**: We use the theory of finite classical generalized polygons to derive and study low-density parity-check (LDPC) codes. The Tanner graph of a generalized polygon LDPC code is highly symmetric, inherits the diameter size of the parent generalized polygon, and has minimum (one half) diameter-to-girth ratio. We show formally that when the diameter is four or six or eight, all codewords have even Hamming weight. When the generalized polygon has in addition an equal number of points and lines, we see that the nonregular polygon based code construction has minimum distance that is higher at least by two in comparison with the dual regular polygon code of the same rate and length. A new minimum-distance bound is presented for codes from nonregular polygons of even diameter and equal number of points and lines. Finally, we prove that all codes derived from finite classical generalized quadrangles are quasi-cyclic and we give the explicit size of the circulant blocks in the parity-check matrix. Our simulation studies of several generalized polygon LDPC codes demonstrate powerful bit-error-rate (BER) performance when decoding is carried out via low-complexity variants of belief propagation.

## Analysis of low-density parity-check codes for the Gilbert-Elliott channel

- **Status**: ✅
- **Reason**: Gilbert-Elliott 메모리 채널에서 LDPC+채널상태 결합 추정디코딩(SPA) — NAND 메모리 채널에 이식 가능 디코더 기법(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1522646
- **Type**: journal
- **Published**: Nov. 2005
- **Authors**: A.W. Eckford, F.R. Kschischang, S. Pasupathy
- **PDF**: https://ieeexplore.ieee.org/document/1522646
- **Abstract**: Density evolution analysis of low-density parity-check (LDPC) codes in memoryless channels is extended to the Gilbert-Elliott (GE) channel, which is a special case of a large class of channels with hidden Markov memory. In a procedure referred to as estimation decoding, the sum-product algorithm (SPA) is used to perform LDPC decoding jointly with channel-state detection. Density evolution results show (and simulation results confirm) that such decoders provide a significantly enlarged region of successful decoding within the GE parameter space, compared with decoders that do not exploit the channel memory. By considering a variety of ways in which a GE channel may be degraded, it is shown how knowledge of the decoding behavior at a single point of the GE parameter space may be extended to a larger region within the space, thereby mitigating the large complexity needed in using density evolution to explore the parameter space point-by-point. Using the GE channel as a straightforward example, we conclude that analysis of estimation decoding for LDPC codes is feasible in channels with memory, and that such analysis shows large potential gains.

## Efficient Encoding of Quasi-Cyclic Low-Density Parity-Check Codes

- **Status**: ✅
- **Reason**: QC-LDPC 효율적 인코딩 회로(systematic-circulant 생성행렬, shift register 직렬/병렬)—바이너리 LDPC HW 인코더 기법 이식 가능(D/E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1532496
- **Type**: journal
- **Published**: Nov. 2005
- **Authors**: Z. Li, L. Chen, L. Zeng +2
- **PDF**: https://ieeexplore.ieee.org/document/1532496
- **Abstract**: Efficient Encoding of Quasi-Cyclic Low-Density Parity-Check Codes Quasi-cyclic (QC) low-density parity-check (LDPC) codes form an important subclass of LDPC codes. These codes have encoding advantage over other types of LDPC codes. This paper addresses the issue of efficient encoding of QC-LDPC codes. Two methods are presented to find the generator matrices of QC-LDPC codes in systematic-circulant form from their parity-check matrices given in circulant form. Based on the systematic-circulation form of the generator matrix of a QC-LDPC code, various types of encoding circuits using simple shift registers are devised. It is shown that the encoding complexity of a QC-LDPC code is linearly proportional to the number of parity bits of the code for serial encoding, and to the length of the code for high-speed parallel encoding.

## Iteratively decodable codes on m flats for WDM high-speed long-haul transmission

- **Status**: ✅
- **Reason**: 유한기하 m-flats 구조적 바이너리 LDPC 구성+고정소수점 양자화 디코더(HW용 정밀도 제어)—코드설계+디코더 양자화 이식 가능(E/C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1561398
- **Type**: journal
- **Published**: Nov. 2005
- **Authors**: S. Sankaranarayanan, I.B. Djordjevic, B. Vasic
- **PDF**: https://ieeexplore.ieee.org/document/1561398
- **Abstract**: In an earlier paper, we reported that the low-density parity-check (LDPC) codes from finite planes outperform any other known forward error-correction (FEC) scheme for optical communications. However, the number of different LDPC codes of code rate above 0.8 is rather small. As a natural extension of the prior work, in this paper, we consider LDPC codes on m flats derived from projective and affine geometries, which outperform codes from finite planes. The codes on m flats also provide a greater selection of structured LDPC codes of rate 0.8 or higher. The performance of the codes in a long-haul optical-communication system was assessed using an advanced simulator able to capture all important transmission impairments. Specifically, they achieve a coding gain of 10 dB at a bit error rate (BER) of 10/sup -9/, outperforming, therefore, the best turbo product codes proposed for optical communications. In addition, the simulator implements a fixed-point (FP) iterative decoder that allows control of the precision of the soft information used in the decoder. Such quantization is required to facilitate hardware implementations of the iterative decoder, and the high-speed operations for long-haul optical transmission systems. The loss in performance due to reduced precision of the soft information can be as low as 0.2 dB.

## Iterative Decoding of Low-Density Parity-Check Codes Over Compound Channels

- **Status**: ✅
- **Reason**: LDPC 반복디코딩+채널추정 결합, density evolution 기반 추정기 설계—디코더 기법 이식 검토 가치(C), 애매하여 in
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1532497
- **Type**: journal
- **Published**: Nov. 2005
- **Authors**: I. Sutskover, S. Shamai
- **PDF**: https://ieeexplore.ieee.org/document/1532497
- **Abstract**: Iterative Decoding of Low-Density Parity-Check Codes Over Compound Channels We present a setting for decoding of low-density parity-check (LDPC) codes jointly with channel estimation, suitable for transmission over memoryless compound channels. We show that the performance of the combined scheme can be rigorously evaluated by means of density evolution, and focus on density evolution as a tool for designing a channel estimator that matches not only to the channel, but also to the LDPC ensemble, as well. The utility of the concept is exemplified for a compound binary symmetric channel and an unknown-phase additive white Gaussian channel.

## MAP estimation via agreement on trees: message-passing and linear programming

- **Status**: ✅
- **Reason**: tree-reweighted max-product(min-sum) 메시지패싱+LP완화, 부호 비의존 디코더 기법으로 BP 개선에 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1522634
- **Type**: journal
- **Published**: Nov. 2005
- **Authors**: M.J. Wainwright, T.S. Jaakkola, A.S. Willsky
- **PDF**: https://ieeexplore.ieee.org/document/1522634
- **Abstract**: We develop and analyze methods for computing provably optimal maximum a posteriori probability (MAP) configurations for a subclass of Markov random fields defined on graphs with cycles. By decomposing the original distribution into a convex combination of tree-structured distributions, we obtain an upper bound on the optimal value of the original problem (i.e., the log probability of the MAP assignment) in terms of the combined optimal values of the tree problems. We prove that this upper bound is tight if and only if all the tree distributions share an optimal configuration in common. An important implication is that any such shared configuration must also be a MAP configuration for the original distribution. Next we develop two approaches to attempting to obtain tight upper bounds: a) a tree-relaxed linear program (LP), which is derived from the Lagrangian dual of the upper bounds; and b) a tree-reweighted max-product message-passing algorithm that is related to but distinct from the max-product algorithm. In this way, we establish a connection between a certain LP relaxation of the mode-finding problem and a reweighted form of the max-product (min-sum) message-passing algorithm.

## High-rate irregular-LDPC coded OFDM BLAST systems

- **Status**: ✅
- **Reason**: 고부호율 irregular LDPC 생성 위한 3가지 construction rule로 낮은 인코딩 복잡도 달성 — 코드설계(E) 이식 가능 여지
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4222778
- **Type**: conference
- **Published**: 7-9 Nov. 2
- **Authors**: Yuanliang Huang, Jiangzhou Wang, Kenichi Higuchi +1
- **PDF**: https://ieeexplore.ieee.org/document/4222778
- **Abstract**: This paper is focused on the study of high coding rate irregular low-density parity-check (LDPC) coded Orthogonal Frequency Division Multiplexing (OFDM) Bell Laboratories Layered Space-Time (BLAST) [1] systems for high-speed wireless transmission. One modified LDPC-coded OFDM BLAST scheme is proposed. To generate high coding rate irregular LDPC codes, three construction rules are adopted to obtain low encoding complexity with little loss of decoding performance. The list sphere decoding is adopted for BLAST detection [2]. The simulation results show that with sphere decoding for BLAST detection and LDPC as channel code, this proposed OFDM BLAST scheme can jointly exploit the available spatial, frequency and temporal diversity as effectively as the OFDM-based BLAST applying coding across the whole data stream [3], and reduce the code length and processing rate for LDPC construction and the implementation of LDPC encoder and decoder as much as the OFDM-based BLAST assuming independent coding within each sub-stream [3].

## Optimized Message Passing Schedules for LDPC Decoding

- **Status**: ✅
- **Reason**: LDPC 메시지패싱 스케줄링(turbo-scheduling, check/bit-node 하이브리드)로 수렴 가속 - 부호 비의존 디코더 개선, NAND BP 이식 가능 (C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1599818
- **Type**: conference
- **Published**: 30 Oct.-2 
- **Authors**: P. Radosavljevic, A. de Baynast, J.R. Cavallaro
- **PDF**: https://ieeexplore.ieee.org/document/1599818
- **Abstract**: The major drawback of the LDPC codes versus the turbo-codes is their comparative low convergence speed: 25-30 iterations vs. 8-10 iterations for turbo-codes. Recently, Hocevar showed by simulations that the convergence rate of the LDPC decoder can be accelerated by exploiting a `turbo-scheduling' applied on the bit-node messages (rows of the parity check matrix). In this paper, we show analytically that the convergence rate for this type of scheduling is about two times increased for most of the regular LDPC codes. Second we prove that `turbo-scheduling' applied on the rows of the parity check matrix is identical belief propagation algorithm as standard message passing algorithm. Furthermore, we propose two new message passing schedules: 1) a turbo-scheduling is applied on the check-node messages (columns of the parity check matrix); and 2) a hybrid version of both previous schedules where the turbo-effect is applied on both check-nodes and bit-nodes. Frame error rate simulations validate the effectiveness of the proposed schedules

## Stochastic Implementation of LDPC Decoders

- **Status**: ✅
- **Reason**: stochastic LDPC 디코더 아키텍처(FPGA) - factor graph의 실리콘 매핑, 이식 가능 HW (D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:1599845
- **Type**: conference
- **Published**: 30 Oct.-2 
- **Authors**: W.J. Gross, V.C. Gaudet, A. Milner
- **PDF**: https://ieeexplore.ieee.org/document/1599845
- **Abstract**: LDPC codes are found in many recent communications standards such as 10GBASE-T, DVB-S2 and IEEE 802.16 (WiMAX). We present a review of a new class of "stochastic" iterative decoding architectures. Stochastic decoders represent probabilistic messages by the frequency of ones in a binary stream. This results in a simple mapping of the factor graph of the code into silicon. An FPGA implementation of a LDPC decoder with 8 information bits and 8 coded bits is described. On an Altera Cyclone FPGA, the throughput is 5 Mbps when clocked at 100 MHz and is expected to increase nearly linearly with the code length. Simulations of the decoder on an Altera Stratix FPGA indicate a potential throughput of 8 Mbps

## A Hybrid Early Decision-Probability Propagation Decoding Algorithm for Low-Density Parity-Check Codes

- **Status**: ✅
- **Reason**: LDPC early-decision+확률전파 하이브리드 디코더로 메모리접근 32% 감소(C/D) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1599817
- **Type**: conference
- **Published**: 30 Oct.-2 
- **Authors**: A. Blad, O. Gustafsson, L. Wanhammar
- **PDF**: https://ieeexplore.ieee.org/document/1599817
- **Abstract**: Low-density parity-check codes have recently received extensive attention as a forward error correction scheme in a wide area of applications. The decoding algorithm is inherently parallelizable, allowing communication at high speeds. One of the main disadvantages, however, is large memory requirements for interim storing of decoding data. In this paper, we investigate the performance of a hybrid decoding algorithm, using an approximating early decision algorithm and a regular probability propagation algorithm. When the early decision algorithm fails, the block is re-decoded using a probability propagation decoder. As almost all errors are detectable, the error correction performance of the hybrid algorithm is negligibly detonated. However, simulations still achieve a 32% decrease of memory accesses

## A Memory Efficient Partially Parallel Decoder Architecture for QC-LDPC Codes

- **Status**: ✅
- **Reason**: QC-LDPC용 메모리 효율 partial-parallel 디코더 + min-sum 변형 + rank order filter CNU - 이식 가능 HW/디코더 (C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1599848
- **Type**: conference
- **Published**: 30 Oct.-2 
- **Authors**: Zhongfeng Wang, Zhiqiang Cui
- **PDF**: https://ieeexplore.ieee.org/document/1599848
- **Abstract**: In this paper, a memory efficient partially parallel decoder architecture suited for high rate quasi-cyclic low-density parity-check codes using (modified) min-sum decoding algorithm is proposed. In general, more than thirty percent of memory can be saved over conventional partially parallel decoder architectures. To reduce the computation delay of check-node processing unit, an efficient architecture based on variants of rank order filter is presented. The optimized partially parallel decoder architecture can linearly increase the decoding throughput with small hardware overhead. Consequently, the proposed approach facilitates the applications of LDPC codes in area/power sensitive high speed communication systems

## A Reconfigurable Fabric and Associated CAD Algorithms for Multirate LDPC Decoding

- **Status**: ✅
- **Reason**: multirate LDPC 디코딩용 reconfigurable VLSI 아키텍처+스케줄링 CAD - 이식 가능 HW (D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:1599846
- **Type**: conference
- **Published**: 30 Oct.-2 
- **Authors**: M. Mohiyuddin, A. Prakash, Xiang Wu +1
- **PDF**: https://ieeexplore.ieee.org/document/1599846
- **Abstract**: We present the design of a reconfigurable VLSI architecture suitable for multirate LDPC decoding. The basic decoder fabric is a square matrix of processing elements which communicate with each other through an interconnection network. The interconnection network consists of links and switches. The connectivity between processing elements is completely defined by scheduling the interconnection network; we describe a CAD algorithm for computing efficient schedules

## VLSI Design for High-Speed Sparse Parity-Check Matrix Decoders

- **Status**: ✅
- **Reason**: sparse parity-check matrix(LDPC 포함) 고속 디코더 VLSI 설계, structured code + TDMP 확장성 아키텍처 - 이식 가능 HW (D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:1599844
- **Type**: conference
- **Published**: 30 Oct.-2 
- **Authors**: M.M. Mansour
- **PDF**: https://ieeexplore.ieee.org/document/1599844
- **Abstract**: In this paper, the design of high-speed iterative decoders for sparse parity-check matrix (SPCM) codes such as LDPC, repeat-accumulate and turbo-like codes is addressed. The random nature of the underlying Tanner graph associated with these codes is problematic for a high-speed decoder implementation. This issue is addressed by designing structured SPCM codes tailored for low-complexity scalable decoders using the turbo-decoding message-passing (TDMP) algorithm. Analysis using EXIT charts shows that a better performance/complexity tradeoff is achieved when the number of decoding iterations is small which is attractive for high-speed applications. A scalable decoder architecture for structures SPCM codes employing the TDMP algorithm is presented

## Design and Implementation of LDPC Codes for DVB-S2

- **Status**: ✅
- **Reason**: DVB-S2 LDPC FPGA 구현 - 다중 rate LDPC 디코더 HW 구현, 이식 가능 HW (D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:1599847
- **Type**: conference
- **Published**: 30 Oct.-2 
- **Authors**: M.K. Yadav, K.K. Parhi
- **PDF**: https://ieeexplore.ieee.org/document/1599847
- **Abstract**: In this paper, we present the design and FPGA implementation of 11 LDPC codes with code rates 1/4, 1/3, 2/5, 1/2, 3/5, 2/3, 3/4, 4/5, 5/6, 8/9 and 9/10 for normal frame length of 64800 bits as used in DVB-S2. Out of these 11 codes, 7 are regular and 4 are irregular. All of them have been synthesized into Xilinx Virtex-II XC2V8000 FPGA

## Improvements on Accelerating Iterative Decoding Using Eigenmessages

- **Status**: ✅
- **Reason**: eigenmessage 디코더로 LDPC 반복횟수 감소, 비국소성 도입 - 이식 가능 디코더 알고리즘 (C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1599819
- **Type**: conference
- **Published**: 30 Oct.-2 
- **Authors**: T.K. Moon, J.S. Crockett, J.H. Gunther
- **PDF**: https://ieeexplore.ieee.org/document/1599819
- **Abstract**: The eigenmessage decoder has been shown to reduce the number of decoding iterations required for LDPC and other iteratively-decoded codes by introducing a degree of nonlocality into the decoding algorithm. In this paper, the multiple loop eigenmessage approach is extended using normalized matrices. Performance is examined via EXIT charts, showing that eigenmessage algorithms have wider channels in the chart. Performance as a function of the girth of the graph is examined, showing the performance to be largely invariant to girth. Finally, performance on matrices denser than typical "low density" parity check matrices is examined, showing that eigenmessage methods perform better than message passing, but still break down as the matrix density increases

## An Improvement of the PEG Algorithm for LDPC Codes in the Waterfall Region

- **Status**: ✅
- **Reason**: PEG 알고리즘 개선으로 waterfall+error floor 동시 개선; 바이너리 LDPC 코드 설계(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1630128
- **Type**: conference
- **Published**: 21-24 Nov.
- **Authors**: G. Richter
- **PDF**: https://ieeexplore.ieee.org/document/1630128
- **Abstract**: There exist many different algorithms to construct good low-density parity-check (LDPC) codes. To maximize the girth of the bipartite graph, which represents the LDPC code, the progressive edge-growth (PEG) algorithm was introduced. This construction methods leads for irregular LDPC codes to a lower error floor, but also to a performance loss in the waterfall region compared with randomly constructed LDPC codes. In this paper, we describe a modification of the PEG algorithm that improves the performance in the waterfall region. Furthermore, this modified PEG algorithm yields codes with lower error floors and a slightly better performance in the waterfall region than randomly constructed LDPC codes

## Implementation aspects of an early decision decoder for LDPC codes

- **Status**: ✅
- **Reason**: early decision 디코딩 아키텍처로 메모리 접근 감소; 이식 가능 HW(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:1597013
- **Type**: conference
- **Published**: 21-22 Nov.
- **Authors**: A. Blad, O. Gustafsson, L. Wanhammar
- **PDF**: https://ieeexplore.ieee.org/document/1597013
- **Abstract**: Low-density parity-check codes have recently received extensive attention as a forward error correction scheme in a wide area of applications. The decoding algorithm is inherently parallelizable, allowing communication at high speeds. One of the, main disadvantages, however, is large memory requirements for interim storing of decoding data. In this paper, we propose an architecture for an early decision decoding algorithm. The algorithm significantly reduces the number of memory accesses. Simulation results show that the increased energy dissipation of the components is small compared to the reduced dissipation of the memories.

## Diagonal low-density parity-check code for simplified routing in decoder

- **Status**: ✅
- **Reason**: diagonal-LDPC로 라우팅 단순화한 fully-parallel 디코더 코드/HW 설계, 이식 가능(D/E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1579966
- **Type**: conference
- **Published**: 2-4 Nov. 2
- **Authors**: E. Kim, G.S. Choi
- **PDF**: https://ieeexplore.ieee.org/document/1579966
- **Abstract**: We propose a novel low-density parity-check (LDPC) decoder design methodology by introducing a special code named diagonal-LDPC (DLDPC) code. An LPDC code, defined by a parity check matrix H, can be represented by a bipartite graph. To address the complex routing problem in the LDPC decoder implementation, a partitioned bipartite-graph code is proposed and generalized to a DLDPC code having constraint of positioning 1's near the diagonal area. This structured code simplifies the routing problem [Y. Kou et al, 2001] [R.M. Tanner et al, 2001] [H. Zhang et al, 2003] and enables cell-based highly regular fully-parallel decoder design without compromising the code performance.

## Tiling parity-check matrix for reduced complexity high throughput low-density parity-check decoders

- **Status**: ✅
- **Reason**: H행렬 타일링으로 라우팅/메모리 단순화한 고처리율 디코더 HW, 이식 가능(D/E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1579964
- **Type**: conference
- **Published**: 2-4 Nov. 2
- **Authors**: A. Selvarathinam, G. Choi
- **PDF**: https://ieeexplore.ieee.org/document/1579964
- **Abstract**: An approach for reducing hardware complexity of LDPC decoders is presented in this paper. Low-density parity-check (LDPC) codes have a sparse parity-check matrix (H matrix). In LDPC decoder, the H matrix is stored in memory and contains information about the parity check constraints. The approach presented in this paper constructs several sub-matrices (pseudo random patterns) that are repeatedly used to form the H matrix. The merits of this approach on the decoder architecture are two-fold. First, the switch logic associated with data forwarding in and out of the memory blocks, or alternately the routing of bit nodes to check nodes is simplified. Second, this approach reduces information stored in the design about the H matrix. Thus, the hardware complexity of the decoder is significantly reduced with an added advantage of increased throughput. LDPC code performance simulation results show that the proposed approach does not compromise the bit error rate performance (BER) compared to that of ideal/optimal H matrix for same code length (N = 2040) and rate.

## A dynamic normalization technique for decoding LDPC codes

- **Status**: ✅
- **Reason**: min-sum용 dynamic normalization 디코더 기법+HW 단순화, 이식 가능 디코더(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1579968
- **Type**: conference
- **Published**: 2-4 Nov. 2
- **Authors**: Yen-Chin Liao, Chien-Ching Lin, Chih-Wei Liu +1
- **PDF**: https://ieeexplore.ieee.org/document/1579968
- **Abstract**: In this paper, a dynamic normalization technique is proposed to approximate the nonlinear operation in decoding LDPC codes. The criterion in determining the normalization factor is also presented with theoretical analysis. The proposed method improves the approximation accuracy as well as the error performance of min-sum algorithm. Furthermore, the hardware implementation benefits from a simplified normalization scheme, leading to reductions in complexity and implementation loss.

## Coset-based quasi-cyclic LDPC codes for optimal overlapped message passing decoding

- **Status**: ✅
- **Reason**: coset 기반 QC-LDPC 신규 구성+girth/최소거리, overlapped message passing 스케줄링, 코드설계(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1579967
- **Type**: conference
- **Published**: 2-4 Nov. 2
- **Authors**: Yongmei Dai, Zhiyuan Yan
- **PDF**: https://ieeexplore.ieee.org/document/1579967
- **Abstract**: Due to the regular structures of quasi-cyclic (QC) low-density parity-check (LDPC) codes, the message passing decoding of these codes not only has efficient hardware implementation, but also can be overlapped to improve throughput and hardware utilization efficiency (HUE). In previous work, we proposed a scheduling scheme for the overlapped message passing (OMP) decoding of the SFT codes. In this paper, we first show that our scheduling scheme produces the minimum intra-iteration waiting time for QC LDPC codes. Then we propose a coset-based construction of QC LDPC codes, and study the girth and minimum distance properties of our new codes. Given the same parameters, the ensemble of the SFT codes is a subset of the ensemble of our coset-based QC LDPC codes. Our coset-based QC LDPC codes allow the OMP decoding to achieve greater throughput gain and higher HUE while maintaining the same theoretical performances as the SFT codes.

## A low-power termination criterion for iterative LDPC code decoders

- **Status**: ✅
- **Reason**: 반복 LDPC 디코더 저전력 종료기준 VLSI 아키텍처, 이식 가능 HW 기법(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:1579850
- **Type**: conference
- **Published**: 2-4 Nov. 2
- **Authors**: G. Glikiotis, V. Paliouras
- **PDF**: https://ieeexplore.ieee.org/document/1579850
- **Abstract**: This paper introduces a novel criterion for the termination of iterations in iterative LDPC Code decoders. The proposed criterion is amenable for VLSI implementation, and it is here shown that it can enhance previously reported LDPC code decoder architectures substantially, by reducing the corresponding power dissipation. The concept of the proposed criterion is the detection of cycles in the sequences of soft words. The soft-word cycles occur in some cases of low signal-to-noise ratios and indicate that the decoder is unable to decide on a codeword, which in turn results in unnecessary power consumption due to iterations that do not improve the bit error rate. The proposed architecture terminates the decoding process when a soft-word cycle occurs, allowing for substantial power savings at a minimal performance penalty. The proposed criterion is applied to hardware-sharing and parallel decoder architectures.

## A 1.1-Gb/s 4092-bit Low-Density Parity-Check Decoder

- **Status**: ✅
- **Reason**: staggered 스케줄·시프트레지스터 직렬 LDPC 디코더 HW 및 유한체 기하 부호, 이식 가능 HW/코드설계(D/E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4017575
- **Type**: conference
- **Published**: 1-3 Nov. 2
- **Authors**: Engling Yeo, Borivoje Nikolic
- **PDF**: https://ieeexplore.ieee.org/document/4017575
- **Abstract**: A 4092-bit low-density parity-check decoder, based on staggered decoding schedule, is implemented in a 130nm 6M CMOS technology. The rate 0.75 code is based on finite-field geometries. Serial, shift-register based architecture enables a compact decoder implementation. The chip has a 4.0mm2 core and operates at 1.1 GHz with 1.2V supply, resulting in a throughput of 1.1Gb/s per iteration.
