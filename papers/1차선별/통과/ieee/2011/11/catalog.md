# IEEE Xplore — 2011-11 (1차선별 통과)


## Overlapped message passing technique with resource sharing for high speed CMMB LDPC decoder

- **Status**: ✅
- **Reason**: Overlapped Message Passing+resource sharing+메모리 그룹핑 디코더 HW 아키텍처(D); CMMB 도메인이나 이식 가능 병렬화 기법
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:6131126
- **Type**: journal
- **Published**: November 2
- **Authors**: Joo-Yul Park, Ki-Seok Chung
- **PDF**: https://ieeexplore.ieee.org/document/6131126
- **Abstract**: Today, demands for high speed digital communication are getting bigger due to wide deployment of 4G mobile communications and mobile TV services. Requirement for high speed data processing makes forward error correction crucial. LDPC is one of the most popular error correcting codes. In this paper, we propose a novel LDPC decoder for the China Multimedia Mobile Broadcasting (CMMB) standard. The LDPC decoding is carried out iteratively, which leads to relatively long decoding latency. Also, due to long code words, the amount of required memory is huge. To resolve these issues, we propose a novel Overlapped Message Passing (OMP) algorithm with an efficient resource sharing technique. Using the proposed method, we find the best permuted parity check matrix of the CMMB to improve the throughput while minimizing the memory requirement. Using the OMP algorithm only, we could improve the performance by 10%. To avoid potential memory access conflicts, a memory grouping technique to improve pipelining performance is also proposed. By applying all the techniques that we propose in this paper, we could improve the performance up to by 451.

## Degree Distribution Design for LDPC Codes: A Derivative Matching Approach

- **Status**: ✅
- **Reason**: 바이너리 LDPC degree distribution 설계(derivative-matching/EXIT) — 이식 가능 코드설계 E
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5997287
- **Type**: journal
- **Published**: November 2
- **Authors**: Enrico Paolini, Marco Chiani, Marc P. C. Fossorier
- **PDF**: https://ieeexplore.ieee.org/document/5997287
- **Abstract**: A deterministic method to design degree distributions for low-density parity-check codes over the binary erasure channel is proposed. This method consists of matching the first and high-order derivatives of the extrinsic information transfer (EXIT) function of the variable node set to the corresponding derivatives of the inverse EXIT function of the check node set, in order to reduce the gap between the two curves in the EXIT chart. A sufficient condition for a check-concentrated distribution to achieve derivative matching up to some order is first obtained, and then a deterministic design algorithm, enabled by the Fourier-Budan theorem, is developed exploiting this sufficient condition. A comparison with other deterministic design techniques is also provided, revealing the potential of the proposed algorithm.

## Flexible LDPC decoder using stream data processing for 802.11n and 802.16e

- **Status**: ✅
- **Reason**: SIMD 기반 IRRWBF bit-flipping 디코더 SW 구현·데이터구조 가속(D/C); 부호 비의존 디코더 HW 기법 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6131118
- **Type**: journal
- **Published**: November 2
- **Authors**: Honey Durga Tiwari, Huynh Ngoc Bao, Yong Beom Cho
- **PDF**: https://ieeexplore.ieee.org/document/6131118
- **Abstract**: Wireless data transmission standards like 802.16e, 802.11n, employ Low Density parity Check (LDPC) codes for error control coding. The bit flipping decoding algorithms presents a tradeoff between the error correcting capability, decoding resources and the decoding time. Software based LDPC decoders provide adaptation capabilities in system parameters such as block size and code rate. In a real-time, low-power mobile environments, the Single-Instruction Multiple-Data (SIMD) processor currently used for video processing, could also be used for the LDPC decoding. In this paper, the implementation efficient, reliability ratio-based, weighted bit flipping (IRRWBF) algorithm is presented using a flexible software based LDPC decoder. Compact data structures are proposed for performing the decoding using SIMD architecture. Based on the implementation on two commonly used SIMD architecture for mobile platform, it was found that the decoding speed can be increased by more than 2000% (using 64 bit SIMD registers with vector integer calculation) and 1800% (using 128 bit SIMD registers with vector floating point calculation). Experimental results for different code lengths of 802.16e and 802.11n show that decoding time in order of 1×10-3 ~10×10-3 seconds is achievable. Due to significantly high throughput and flexibility, the proposed design algorithm and data structure can easily be adapted to any energy-sensitive mobile devices employing SIMD processors1.

## Improved Linear Programming Decoding of LDPC Codes and Bounds on the Minimum and Fractional Distance

- **Status**: ✅
- **Reason**: LP 디코딩 개선(relaxation tightening)+최소거리/fractional distance 하한 알고리즘(C); 바이너리 LDPC 디코더·구성 기여 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5955120
- **Type**: journal
- **Published**: Nov. 2011
- **Authors**: David Burshtein, Idan Goldenberg
- **PDF**: https://ieeexplore.ieee.org/document/5955120
- **Abstract**: We examine LDPC codes decoded using linear programming (LP). Four contributions to the LP framework are presented. First, a new method of tightening the LP relaxation, and thus improving the LP decoder, is proposed. Second, we present an algorithm which calculates a lower bound on the minimum distance of a specific code. This algorithm exhibits complexity which scales quadratically with the block length. Third, we propose a method to obtain a tight lower bound on the fractional distance, also with quadratic complexity, and thus less than previously-existing methods. Finally, we show how the fundamental LP polytope for generalized LDPC codes and nonbinary LDPC codes can be obtained.

## Delayed Stochastic Decoding of LDPC Codes

- **Status**: ✅
- **Reason**: 신규 Delayed Stochastic 디코딩 알고리즘+VLSI 구현으로 HW 복잡도·메모리 절감, 바이너리 LDPC 디코더 HW 이식 가능(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5975253
- **Type**: journal
- **Published**: Nov. 2011
- **Authors**: Ali Naderi, Shie Mannor, Mohamad Sawan +1
- **PDF**: https://ieeexplore.ieee.org/document/5975253
- **Abstract**: A new stochastic decoding algorithm, called Delayed Stochastic (DS) decoding, is introduced to implement low-density-parity-check (LDPC) decoders. The delayed stochastic decoding uses an alternative method to track probability values, which results in reduction of hardware complexity and memory requirement of the stochastic decoders. It is therefore suitable for fully-parallel implementation of long LDPC codes with applications in optical communications. Two decoders are implemented using the DS algorithm for medium (2048, 1723) and long (32768, 26624) LDPC codes. The decoders occupy 3.93- mm2 and 56.5- mm2 silicon area using 90-nm CMOS technology and provide maximum core throughputs of 172.4 and 477.7 Gb/s at [(Eb)/(No)]=5.5 and 4.8 dB, respectively.

## Construction of irregular quasi-cyclic LDPC codes based on Euclidean geometries

- **Status**: ✅
- **Reason**: Euclidean geometry 기반 irregular QC-LDPC 구성(large girth, hyperplane 분해, degree 분포 최적화) — 바이너리 코드 설계(E) 기여
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6096743
- **Type**: conference
- **Published**: 9-11 Nov. 
- **Authors**: Xueqin Jiang, Moon Ho Lee, Xiaofei Liao +1
- **PDF**: https://ieeexplore.ieee.org/document/6096743
- **Abstract**: This paper presents a method to the construction of irregular low-density parity-check (LDPC) codes based on Euclidean geometries over the Galois field. Codes constructed by this method are quasi-cyclic (QC) and have large girths. The proposed irregular LDPC codes having flexible column/row weights are obtained with a hyperplane decomposing method in Euclidean geometries. Therefore, the degree distributions of proposed irregular LDPC codes can be optimized by technologies like the curve fitting approach in the extrinsic information transfer (EXIT) charts. Simulation results show that these codes perform very well with an iterative decoding over the AWGN channel.

## A technique to improve the performance of fixed-point TDMP decoding of QC-LDPC codes in the presence of SNR estimation error

- **Status**: ✅
- **Reason**: QC-LDPC TDMP 디코더의 고정소수점 8비트 양자화/포화 완화 기법 - C/D 이식 가능 (NAND LLR 양자화와 직결)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6127748
- **Type**: conference
- **Published**: 7-10 Nov. 
- **Authors**: JaWone A. Kennedy, Daniel L. Noneaker
- **PDF**: https://ieeexplore.ieee.org/document/6127748
- **Abstract**: Most high-throughput, fixed-point processors offer at least two options for arithmetic operations: 8-bit arithmetic, and 16-bit arithmetic. The lower resolution provides higher computational throughput at the cost of poorer performance in many applications. We investigate the effect of the resolution of saturating, fixed-point arithmetic on the performance of the turbo-decoding message-passing algorithm with quasi-cyclic low-density parity-check codes. We consider limits on the magnitude of extrinsic updates as a means to mitigate the effect of posterior-value saturation on the decoder's performance. We show that a fixed limit on updates only partially overcomes the greater effect of saturation in 8-bit operations, whereas a limit that depends on the degree of the variable node results in performance almost as good as what is possible with 16-bit operations.

## GPU accelerated scalable parallel decoding of LDPC codes

- **Status**: ✅
- **Reason**: GPU 기반 스케일러블 병렬 LDPC 디코더 + 적응 성능튜닝; 이식 가능한 병렬화 HW/SW 아키텍처(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:6190388
- **Type**: conference
- **Published**: 6-9 Nov. 2
- **Authors**: Guohui Wang, Michael Wu, Yang Sun +1
- **PDF**: https://ieeexplore.ieee.org/document/6190388
- **Abstract**: This paper proposes a flexible low-density parity-check (LDPC) decoder which leverages graphic processor units (GPU) to provide high decoding throughput. LDPC codes are widely adopted by the new emerging standards for wireless communication systems and storage applications due to their near-capacity error correcting performance. To achieve high decoding throughput on GPU, we leverage the parallelism embedded in the check-node computation and variable-node computation and propose a parallel strategy of partitioning the decoding jobs among multi-processors in GPU. In addition, we propose a scalable multi-codeword decoding scheme to fully utilize the computation resources of GPU. Furthermore, we developed a novel adaptive performance-tuning method to make our decoder implementation more flexible and scalable. The experimental results show that our LDPC decoder is scalable and flexible, and the adaptive performance-tuning method can deliver the peak performance based on the GPU architecture.

## LDPC codes based on Progressive Edge Growth techniques for block fading channels

- **Status**: ✅
- **Reason**: PEG 기반 Root-Check LDPC 구성, girth 최대화 제약 — 바이너리 코드설계(E) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6125390
- **Type**: conference
- **Published**: 6-9 Nov. 2
- **Authors**: André G. D. Uchôa, Cornelius Healy, Rodrigo C. de Lamare +1
- **PDF**: https://ieeexplore.ieee.org/document/6125390
- **Abstract**: We propose an algorithm to design Root-Check LDPC codes based on Progressive Edge Growth (PEG) techniques for block-fading channels. The proposed algorithm imposes some restrictions on the traditional PEG algorithm to ensure that the LDPC code generated is Root-Check with the largest possible girth. The performance is investigated by means of the outage probability. By doing so, the codes generated by our proposed algorithm are shown to outperform the existing methods for generating Root-Check LDPC codes.

## Rate-compatible LDPC codes using optimized dummy bit insertion

- **Status**: ✅
- **Reason**: 단일 mother LDPC에서 dummy bit 삽입으로 rate 매칭+error floor 개선 신규 규칙 — 바이너리 LDPC 코드설계(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6125400
- **Type**: conference
- **Published**: 6-9 Nov. 2
- **Authors**: Moritz Beermann, Tobias Breddermann, Peter Vary
- **PDF**: https://ieeexplore.ieee.org/document/6125400
- **Abstract**: Much attention has been paid to Low-Density Parity-Check (LDPC) codes since their rediscovery by MacKay. They belong to the most powerful channel coding techniques known today and have a broad range of applications. In wireless communication systems it is desirable to be able to adjust the code rate of the employed channel coding scheme (rate-matching) to allow for a flexible strength of error protection for different services and to be able to adapt to the varying quality of the wireless transmission channel. Many of the current systems that employ LDPC codes like, e.g., WiMAX or WLAN specify separate codes for each supported code rate. This paper, in contrast, addresses the problem of using only one mother code and matching (almost) arbitrary code rates that are lower than the mother code rate by inserting known (dummy) bits into the information bit sequence before encoding (also known as pruning or code shortening). We present a novel rule of determining (heuristically) optimized positions of dummy bits within the information bit sequence suitable for LDPC codes. Simulation results show that the frame error rate performance can be improved by the novel approach of dummy bit insertion especially in the error floor region.

## Achieving flexibility in LDPC code design by absorbing set elimination

- **Status**: ✅
- **Reason**: 바이너리 SCB(circulant) LDPC absorbing set 제거·error floor 개선 코드설계 기법(E) — 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6190087
- **Type**: conference
- **Published**: 6-9 Nov. 2
- **Authors**: Jiajun Zhang, Jiadong Wang, Shayan Garani Srinivasa +1
- **PDF**: https://ieeexplore.ieee.org/document/6190087
- **Abstract**: Low-density parity-check (LDPC) codes are attractive since their performance is known to approach the Shannon limits for suitably large block lengths. However, for moderate block lengths, error floors still jeopardize the performance even of well-designed LDPC codes. Previous work has shown that the error floor of a broad class of LDPC codes is due to certain graphical structures called absorbing sets. Separable, circulant-based (SCB) codes represent a general family of high-performance, hardware-friendly LDPC codes built out of circulants. A recently proposed technique applies row selection and column elimination methods to SCB codes to dramatically decrease error floors by avoiding certain small dominant absorbing sets in a principled way. This paper focuses on improving the greedy column elimination method to achieve greater flexibility in code rate while provably avoiding small dominant absorbing sets. Flexibility and low implementation complexity are therefore possible without sacrificing SCB code performance.

## Finite-length rate-compatible LDPC codes based on extension techniques

- **Status**: ✅
- **Reason**: 유한길이 rate-compatible LDPC 구성(cycle counting+ACE 기반 확장) - E 코드설계 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6125306
- **Type**: conference
- **Published**: 6-9 Nov. 2
- **Authors**: Jingjing Liu, Rodrigo C. de Lamare
- **PDF**: https://ieeexplore.ieee.org/document/6125306
- **Abstract**: We propose two innovative extension schemes for Rate-Compatible (RC) Low-Density Parity-Check (LDPC) codes with short/moderate block lengths. The proposed designs are based on the counting cycles algorithm and the Approximate Cycle Extrinsic Message Degree (EMD). Our layer-structured extension schemes enjoy a linear-time encodable ability and relatively low decoding complexity thanks to low degree profiles with limited decoding iterations, such that they intrinsically fit in a type-II hybrid automatic repeat-request (ARQ) system. Simulation results show that the proposed approaches manage to yield a performance gain of up to 0.3 dB when compared to the existing extension technique.

## Construction of SeIRA QC-LDPC codes with low error floor

- **Status**: ✅
- **Reason**: SeIRA QC-LDPC 구성, circle length+connectivity 결합 신규 metric으로 error floor 개선 — 바이너리 코드설계(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6125358
- **Type**: conference
- **Published**: 6-9 Nov. 2
- **Authors**: Wenyan Zhang, Minjian Zhao, Jie Zhong +2
- **PDF**: https://ieeexplore.ieee.org/document/6125358
- **Abstract**: We investigate the construction method of structured extended irregular repeated-accumulate quasi-cyclic low-density parity-check (SeIRA QC-LDPC) codes with short to moderate length. A new metric is proposed that jointly considers both circle length and circle connectivity, which aims to improve the error correcting performance in the error floor region. Meanwhile, iterative searching method is proposed that increase the possibility of finding out good solution based on the new metric. At last, we apply our construct method to design codes with different length by expanding them from the same mother matrix. Simulation results show that FER of the codes constructed by this method outperform the corresponding codes in the 802.16 standard expanded from the same mother matrix by 0.15~0.4dB at FER around 10-5.

## A flexible layered LDPC decoder

- **Status**: ✅
- **Reason**: QC-LDPC flexible layered 디코더 아키텍처(병렬도 가변, 메모리충돌 없음, 확장성 인터커넥트) - D 이식 가능
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:6125305
- **Type**: conference
- **Published**: 6-9 Nov. 2
- **Authors**: I. Tsatsaragkos, V. Paliouras
- **PDF**: https://ieeexplore.ieee.org/document/6125305
- **Abstract**: We introduce a flexible layered decoder architecture for Quasi-Cyclic Low Density Parity Check (LDPC) codes. An iterative construction of the parity check matrix is exploited by the proposed decoder to achieve various degrees of parallelism, characterized by a high utilization of variable and check processing nodes, absence of memory conflicts, and a simple and scalable interconnection network. Furthermore, the proposed LDPC decoder supports variable code rate, information-word length and order of modulation. A comparison to prior-art decoders proves the efficiency of the proposed scheme.

## A reduced routing network architecture for partial parallel LDPC decoders

- **Status**: ✅
- **Reason**: 부분병렬 LDPC 디코더의 라우팅 네트워크 축소(permutation network); 면적/속도/전력 개선 HW 아키텍처(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:6190420
- **Type**: conference
- **Published**: 6-9 Nov. 2
- **Authors**: Houshmand Shirani-Mehr, Tinoosh Mohsenin, Bevan Baas
- **PDF**: https://ieeexplore.ieee.org/document/6190420
- **Abstract**: A novel partial parallel decoding scheme based on the matrix structure of LDPC codes proposed in IEEE 802.15.3c and IEEE 802.11ad standards is presented that significantly simplifies the routing network of the decoder, and the class of parity-check matrices for which the method can be used is defined. The proposed method results in an almost complete elimination of logic gates on the routing network, which yields improvements in area, speed and power, with an identical error correction performance to conventional partial-parallel decoders. A decoder for the (672,588) LDPC code adopted in the IEEE 802.15.3c is implemented in a 65 nm CMOS technology including place & route with both proposed permutational decoder, and conventional partial-parallel architecture. The proposed permutational LDPC decoder operates at 235 MHz and delivers a throughput of 7.9 Gbps with 5 decoding iterations per block. The proposed permutational decoder has a throughput 30% higher and is approximately 24% smaller than the conventional partial-parallel decoder.

## Construction of QC-LDPC codes based on PSO algorithm

- **Status**: ✅
- **Reason**: PSO 기반 인코더블 QC-LDPC 구성(girth-4/BER 제약) 신규 코드설계(E), 바이너리 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6197838
- **Type**: conference
- **Published**: 27-30 Nov.
- **Authors**: Yang Yang, Yang Xiao
- **PDF**: https://ieeexplore.ieee.org/document/6197838
- **Abstract**: The well known Tanner codes are not encodable, in this paper, we derived an encodable QC LDPC codes and use PSO algorithm to determine the parameters of the parity check matrices of the QC LDPC codes. The proposed PSO code construction considers the girth 4 and BER performance to be the constrained conditions in the fitness function of PSO algorithm. Simulation results show that the QC codes constructed by the proposed method have better performance than that of random LDPC codes.

## A class of (3, k) quasi-cyclic LDPC codes from difference sequences with girth 8

- **Status**: ✅
- **Reason**: difference sequence 기반 (3,k) QC-LDPC girth-8 신규 구성법, 바이너리 코드설계(E) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6197836
- **Type**: conference
- **Published**: 27-30 Nov.
- **Authors**: Bing Li, Lijun Zhang, Lee Lung Cheng
- **PDF**: https://ieeexplore.ieee.org/document/6197836
- **Abstract**: An approach for constructing a class of (3, k)-regular quasi-cyclic low-density parity-check (QC-LDPC) codes is proposed, which is based on combinatorial objects termed difference sequences. By an efficient algorithm for searching good difference sequences, codes in this class have girth at least eight. Simulation results show that the codes slightly outperform the counterpart PEG codes and have better performance than the corresponding MacKay codes and array codes.

## A flexible NoC-based LDPC code decoder implementation and bandwidth reduction methods

- **Status**: ✅
- **Reason**: NoC 기반 유연 LDPC 디코더+early/message stopping으로 면적·전력 절감 VLSI 아키텍처(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:6136889
- **Type**: conference
- **Published**: 2-4 Nov. 2
- **Authors**: Carlo Condo, Guido Masera
- **PDF**: https://ieeexplore.ieee.org/document/6136889
- **Abstract**: The need for efficient and flexible LDPC (Low Density parity Check) code decoders is rising due to the growing number and variety of standards that adopt this kind of error correcting codes in wireless applications. From the implementation point of view, the decoding of LDPC codes implies intensive computation and communication among hardware components. These processing capabilities are usually obtained by allocating a sufficient number of processing elements (PEs) and proper interconnect structures. In this paper, Network on Chip (NoC) concepts are applied to the design of a fully flexible decoder, capable to support any LDPC code with no constraints on code structure. It is shown that NoC based decoders also achieve relevant throughput values, comparable to those obtained by several specialized decoders. Moreover, the paper explores the area and power overhead introduced by the NoC approach. In particular, two methods are proposed to reduce the traffic injected in the network during the decoding process, namely early stopping of iterations and message stopping. These methods are usually adopted to increase throughput. On the contrary, in this paper, we leverage iteration and message stopping to cut the area and power overhead of NoC based decoders. It is shown that, by reducing the traffic injected in the NoC and the number of iterations performed by the decoding algorithm, the decoder can be scaled to lower degrees of parallelism with small losses in terms of BER (Bit Error Rate) performance. VLSI synthesis results on a 130 nm technology show up to 50% area and energy reduction while maintaining an almost constant throughput.

## Erasing Bit Nodes on the Bipartite Graph for Enhanced Performance of LDPC Codes

- **Status**: ✅
- **Reason**: 비트노드 erasing으로 cycle/trapping set 대응하는 신규 BP 디코딩 전략 - 카테고리 C 이식 가능 디코더
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6120564
- **Type**: conference
- **Published**: 18-20 Nov.
- **Authors**: P.C. Catherine, K.M.S. Soyjaudah
- **PDF**: https://ieeexplore.ieee.org/document/6120564
- **Abstract**: The proposed work is based on the fact that the complete set of bit nodes for an LDPC code may not always be required at the receiving side for successful decoding. A corresponding strategy is therefore built up. In contrast to common practice, the total number of iterations available is shared among different sets. The first set runs the decoding algorithm with all its bit nodes. Successive sets (in case of decoding failure) runs each with a different selection of "erased" bit nodes, leading to an overall non-monotonic behavior. The end result is a system capable of effectively dealing with the problem of cycles and trapping sets without even being aware of their existence. Reported results show an important coding gain over conventional systems.

## Efficient Reed-Solomon based LDPC decoders

- **Status**: ✅
- **Reason**: RS-based LDPC 디코더 HW — 메모리 주소생성·셔플네트워크·TM 폴딩 아키텍처가 바이너리 QC-LDPC 디코더에 이식 가능(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:6138645
- **Type**: conference
- **Published**: 17-18 Nov.
- **Authors**: Chuan Zhang, Sang-Min Kim, Jin Sha
- **PDF**: https://ieeexplore.ieee.org/document/6138645
- **Abstract**: By exploring the specific characteristics of the matrices of Reed-Solomon (RS) based low-density parity-check (LDPC) codes, the authors manage to propose an efficient memory address generation (MAG) method for time-multiplexed (TM) RS-based LDPC code decoder architecture. This unique feature directly results in the MAG scheme which works perfectly with the TM decoders. Furthermore, along with the sum and sign accumulation unit (SSAU), a methodology for designing TM RS-based LDPC code decoder supporting high decoding throughput applications such as a 10GBASE-T system is presented. By developing and evaluating three decoder architectures with different folding factors, this approach proves to be suitable for variable design requirements. In addition, a shuffle network composed of de-multiplexers (deMUX's) and routing blocks is also incorporated to reduce the decoding latency.

## A common flexible architecture for Turbo/LDPC codes

- **Status**: ✅
- **Reason**: Turbo/LDPC 공용 ASIC 아키텍처 — 메모리/로직 공유 HW 설계가 바이너리 LDPC 디코더에 이식 가능(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:6138644
- **Type**: conference
- **Published**: 17-18 Nov.
- **Authors**: Yuebin Huang, Chen Chen, Changsheng Zhou +2
- **PDF**: https://ieeexplore.ieee.org/document/6138644
- **Abstract**: Turbo codes and LDPC codes are two of the most powerful error correction codes that can approach Shannon limit in many communication systems. But there are little architecture presented to support both LDPC and Turbo codes, especially by the means of ASIC. This paper have implemented a common architecture that can decode LDPC and Turbo codes, and it is capable of supporting the WiMAX, WiFi, 3GPP-LTE standard on the same hardware. In this paper, we will carefully describe how to share memory and logic devices in different operation mode. The chip is design in a 130nm CMOS technology, and the maximum clock frequency can reach up to 160MHz. The maximum throughput is about 104Mbps@5.5 iteration for Turbo codes and 136Mbps@10iteration for LDPC codes. Comparing to other existing structure, the design speed, area have significant advantage.

## A 115mW 1Gbps QC-LDPC decoder ASIC for WiMAX in 65nm CMOS

- **Status**: ✅
- **Reason**: QC-LDPC 디코더 ASIC, fully parallel layered scheduling 아키텍처+메모리 절감 HW(D) 이식 가능
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:6123576
- **Type**: conference
- **Published**: 14-16 Nov.
- **Authors**: Xiao Peng, Zhixiang Chen, Xiongxin Zhao +2
- **PDF**: https://ieeexplore.ieee.org/document/6123576
- **Abstract**: Structured quasi-cyclic low-density parity-check (QC-LDPC) code is a part of many emerging wireless communication standards, such as WiMAX, WiFi and WPAN. This paper presents a high parallel decoder architecture for the QC-LDPC codes and the corresponding decoder ASIC for WiMAX system. Through utilizing the proposed fully parallel layered scheduling architecture, the decoder chip saves 22.2% memory bits and takes 24~48 clock cycles per iteration for different code rates. It occupies 3.36 mm2 in SMIC 65nm CMOS, and realizes 1Gbps (1056Mbps) throughput at 1.2V, 110MHz and 10 iterations with the power 115mW and power efficiency 10.9pJ/bit/iteration. The energy/bit/iteration reduces 63.6% in normalized comparison with the state-of-art publication.

## A 1pJ/cycle Processing Engine in LDPC application with charge recovery logic

- **Status**: ✅
- **Reason**: LDPC 처리엔진 PE에 charge-recovery logic 저전력 회로기법, 디코더 HW 구현(D) 이식 가능
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:6123640
- **Type**: conference
- **Published**: 14-16 Nov.
- **Authors**: Yimeng Zhang, Mengshu Huang, Nan Wang +2
- **PDF**: https://ieeexplore.ieee.org/document/6123640
- **Abstract**: This paper presents a Processing Engine (PE) which is used in Low Density Parity Codec (LDPC) application with a novel charge-recovery logic called pseudo-NMOS boost logic (pNBL), to achieve high-speed and low power dissipation. pNBL is a high-overdriven, low area consuming charge recovery logic, which belongs to boost logic family. Proposed Processing Engine is used in LDPC circuit to reduce power dissipation and increase the processing speed. To demonstrate the performance of proposed PE, a test chip is designed and fabricated with 0.18μm CMOS technology. Simulation results indicate that proposed PE with pNBL dissipates only 1pJ/cycle when working at the frequency of 403MHz, which is only 36% of PE with conventional static CMOS gates. The measurement results shows that the test chip can work as high as 609MHz with the energy dissipation of 2.1pJ/cycle.
