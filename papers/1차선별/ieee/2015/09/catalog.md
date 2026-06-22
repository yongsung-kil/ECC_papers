# IEEE Xplore — 2015-09 (1차선별 통과)


## Spatially Coupled LDPC Codes Constructed From Protographs

- **Status**: ✅
- **Reason**: 프로토그래프 기반 SC-LDPC 구성 기법(E), 바이너리, BP 임계값/최소거리 설계 — NAND LDPC 코드설계 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7152893
- **Type**: journal
- **Published**: Sept. 2015
- **Authors**: David G. M. Mitchell, Michael Lentmaier, Daniel J. Costello
- **PDF**: https://ieeexplore.ieee.org/document/7152893
- **Abstract**: In this paper, we construct protograph-based spatially coupled low-density parity-check (LDPC) codes by coupling together a series of L disjoint, or uncoupled, LDPC code Tanner graphs into a single coupled chain. By varying L , we obtain a flexible family of code ensembles with varying rates and frame lengths that can share the same encoding and decoding architecture for arbitrary L . We demonstrate that the resulting codes combine the best features of optimized irregular and regular codes in one design: capacity approaching iterative belief propagation (BP) decoding thresholds and linear growth of minimum distance with block length. In particular, we show that, for sufficiently large L , the BP thresholds on both the binary erasure channel and the binary-input additive white Gaussian noise channel saturate to a particular value significantly better than the BP decoding threshold and numerically indistinguishable from the optimal maximum a posteriori decoding threshold of the uncoupled LDPC code. When all variable nodes in the coupled chain have degree greater than two, asymptotically the error probability converges at least doubly exponentially with decoding iterations and we obtain sequences of asymptotically good LDPC codes with fast convergence rates and BP thresholds close to the Shannon limit. Further, the gap to capacity decreases as the density of the graph increases, opening up a new way to construct capacity achieving codes on memoryless binary-input symmetric-output channels with low-complexity BP decoding.

## Efficient Puncturing Scheme for Irregular LDPC Codes Based on Serial Schedules

- **Status**: ✅
- **Reason**: 불규칙 LDPC 직렬스케줄 기반 신규 puncturing 기법; 바이너리 LDPC 코드설계(E) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7152871
- **Type**: journal
- **Published**: Sept. 2015
- **Authors**: Hua Li, Linhua Zheng
- **PDF**: https://ieeexplore.ieee.org/document/7152871
- **Abstract**: In practice, low-density parity-check (LDPC) codes are usually decoded by serial schedules. However, the existing schemes for rate-compatible puncturing LDPC codes are proposed on the assumption that the flooding schedules are employed in decoding algorithm. In this letter, an efficient puncturing scheme is proposed for irregular LDPC codes based on serial schedule. The scheme selects variable nodes to be punctured one at a time. At each time, a check node is selected firstly based on the idea that the punctured variable nodes are allocated evenly to all the check nodes. Then the puncturing variable node is selected among its neighbors. Furthermore, the order of the check nodes in the selection serves as the updating order in the serial schedule, which ensures that all the punctured codes can be recovered at the first iteration. Simulation results demonstrate that the scheme performs better for a wide range of code rates compared with the existing puncturing scheme, especially for high-rate punctured codes.

## Spatially Coupled LDPC Codes Constructed by Parallelly Connecting Multiple Chains

- **Status**: ✅
- **Reason**: 바이너리 SC-LDPC 다중체인 병렬연결 신규 구성으로 디코딩 임계값 개선; 코드설계(E) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7130575
- **Type**: journal
- **Published**: Sept. 2015
- **Authors**: Yang Liu, Ying Li, Yuhao Chi
- **PDF**: https://ieeexplore.ieee.org/document/7130575
- **Abstract**: A particular class of spatially coupled low-density parity-check (SC-LDPC) codes are constructed by parallelly connecting multiple different coupled chains. The connection structure is realized by edge exchanges between adjacent chains, which can help these chains support each other and improve the iterative decoding thresholds. By varying the number of the connected chains and the degree of each chain, a family of SC-LDPC codes with wide rate range can be obtained. Density evolution analysis shows that the decoding thresholds of the proposed codes are very close to Shannon limits and are slightly better than that constructed by a single chain over the binary erasure channel.

## Analysis of low-bit soft-decision error correction in optical front ends

- **Status**: ✅
- **Reason**: 광 수신단 저비트 soft-decision FEC 디코딩 성능/노이즈 분석, LLR 양자화·thermometer code 관련 — 저비트 양자화 디코더 이식 가능성, 애매하여 보존(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7255255
- **Type**: journal
- **Published**: Sept. 2015
- **Authors**: M. Moayedi Pour Fard, G. Cowan, O. Liboiron-Ladouceur
- **PDF**: https://ieeexplore.ieee.org/document/7255255
- **Abstract**: A novel methodology for analyzing the advantageous decoding performance of multibranch configurations of low-bit optical soft-decision forward error correction receivers is presented. The decoding performance and noise behavior of three front-end schemes are evaluated and compared. Arising from a multiple-branch configuration, the concept of inconsistency in the decoder (thermometer code) is presented and used to optimize decoding performance. The experimentally validated methodology considers both optically amplified long-haul and short-reach applications.

## Novel ECC structure and evaluation method for NAND flash memory

- **Status**: ✅
- **Reason**: A — NAND 플래시 ECC 직접, adaptive LDPC 구조 및 error-free information capacity 평가법 제시
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7406921
- **Type**: conference
- **Published**: 8-11 Sept.
- **Authors**: Jiang Xiao-bo, Tan Xue-qing, Huang Wei-pei
- **PDF**: https://ieeexplore.ieee.org/document/7406921
- **Abstract**: The evaluation of error correction code (ECC) for NAND flash memory is increasingly complicated by the increasing bit error rate in memory. The concept of error-free information capacity is proposed to evaluate the performance ECC of NAND flash memory. The new method simultaneously considers the capacity and reliability of NAND flash memory. Low-density parity-check (LDPC) codes with a medium code rate can improve the integrated performance of NAND flash memory in order of magnitudes. Observations provide guides for the development of ECC schemes in NAND flash memory in future. An ECC structure based on adaptive LDPC codes is also presented in this paper. The new structure achieves integrated performance of both capacity and reliability in NAND flash memory.

## Efficient stochastic list successive cancellation decoder for polar codes

- **Status**: ✅
- **Reason**: C 후보 — stochastic list SC 디코더는 polar용이나 stochastic decoding은 부호 비의존적 BP 기법이라 바이너리 LDPC BP HW에 이식 여지, 애매하여 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7406997
- **Type**: conference
- **Published**: 8-11 Sept.
- **Authors**: Xiao Liang, Chuan Zhang, Menghui Xu +2
- **PDF**: https://ieeexplore.ieee.org/document/7406997
- **Abstract**: Representing continuous values by streams of random binary bits, stochastic decoding has shown advantages in both hardware efficiency and fault tolerance, therefore has been widely adopted by iterative decoding of error correction codes such as low-density parity-check (LDPC) codes and so on. Recently, polar codes, the first codes that can provably achieve the capacity of symmetric binary-input discrete memoryless channels (B-DMCs), have drawn a lot of attentions from both academia and industry. Although, polar codes with list successive cancellation (SC) decoding can outperform several best-known LDPC codes even within high error-rate regions, the linearly increasing hardware complexity makes its efficient implementation difficult. To this end, the stochastic list SC polar decoding algorithm is proposed in this paper to provide a good tradeoff between performance and complexity. In order to increase the decoding performance of stochastic list SC polar decoder, doubling probability approach is presented. The corresponding hardware architecture is also given. The approximate doubling approach is employed to facilitate the efficient implementation. Implementation results have shown that the proposed stochastic list SC polar decoder can achieve a good trade-off between performance and complexity.

## High-Throughput FPGA-Based QC-LDPC Decoder Architecture

- **Status**: ✅
- **Reason**: 바이너리 QC-LDPC 디코더 신규 PCM 표현/superlayer 파이프라이닝 FPGA 아키텍처 — 이식 가능 HW(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:7390967
- **Type**: conference
- **Published**: 6-9 Sept. 
- **Authors**: Swapnil Mhaske, Hojin Kee, Tai Ly +2
- **PDF**: https://ieeexplore.ieee.org/document/7390967
- **Abstract**: We propose without loss of generality strategies to achieve a high-throughput FPGA-based architecture for a binary Quasi-Cyclic Low-Density Parity-Check (QC-LDPC) code based on a circulant-1 identity matrix construction. We present a novel representation of the parity-check matrix (PCM) providing a multi-fold throughput gain. Splitting of the node processing algorithm enables us to achieve pipelining of blocks and hence layers. By partitioning the PCM into not only layers but superlayers we derive an upper bound on the two-layer pipelining depth for the compact representation. To validate the architecture, a decoder for the IEEE 802.11n (2012) QC-LDPC is implemented on the Xilinx Kintex-7 FPGA with the help of the FPGA IP compiler available in the NI LabVIEW Communication System Design Suite (CSDS). It offers an automated and systematic compilation flow where an optimized hardware implementation from the LDPC algorithm was generated, achieving an overall throughput of 608Mb/s (at 260MHz). As per our knowledge this is the fastest implementation of the IEEE 802.11n QC-LDPC decoder using an algorithmic compiler.

## Performance Improvement of Accumulate-Repeat-Accumulate Codes with Bounded Complexity

- **Status**: ✅
- **Reason**: SC-ARA(spatially-coupled ARA) 신규 부호 구성+DE 분석, 바이너리 SC-LDPC 계열 코드설계 기법 이식 가능(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7391080
- **Type**: conference
- **Published**: 6-9 Sept. 
- **Authors**: Waleed Saad, Shady M. Ibraheem, Maher M. Abd Elrazzak +2
- **PDF**: https://ieeexplore.ieee.org/document/7391080
- **Abstract**: In this paper, we introduce a new family of codes named as systematic spatially-coupled accumulate repeat accumulate SC-ARA codes based on chain of interconnected proto-graphs over the binary erasure channels (BEC). It has been observed that Spatially-coupled low density parity check (SC-LDPC) codes are able to approach the capacity universally across the binary-input memoryless (BMS) channels. A density evolution (DE) analysis is provided for this class of codes which categorized by bounded density and/or complexity per information bit. Simulation results show that the spatially coupling of ensembles of ARA codes, with bounded density and/or complexity, drives the message-passing belief propagation decoding threshold (BP) to be closed to the maximum a posterior (MAP) threshold of the underlying codes over the BEC.

## Recursive encoding of spatially coupled LDPC codes with arbitrary rates

- **Status**: ✅
- **Reason**: 임의 rate SC-LDPC 재귀 인코딩용 수정 패리티검사 구조+시프트레지스터 구현, BP threshold 개선 — 바이너리 코드설계 이식 가능(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7343281
- **Type**: conference
- **Published**: 30 Aug.-2 
- **Authors**: Junyang Ma, Zhongwei Si, Zhiqiang He +1
- **PDF**: https://ieeexplore.ieee.org/document/7343281
- **Abstract**: Spatially coupled LDPC codes have attracted much attention due to the promising performance. Recursive encoding with low delay and low complexity has been proposed in the literature for selected node degrees. To realize the recursive encoding of spatially coupled LDPC codes with arbitrary rates, we propose in this paper a modified structure of the parity-check matrix and implement the encoding using a shift-register regardless of the node degrees. By rearranging the edge connections, the parity bits at each coupling position can be jointly determined by the information bits at the current position and the encoded bits at former positions. Performance analysis in terms of design rate and density evolution has been provided. It can be observed that the modified code structure leads to a better belief-propagation threshold. Finite-length simulation results are provided, which verify the theoretical analysis.

## Modified forced convergence decoding of LDPC codes with optimized decoder parameters

- **Status**: ✅
- **Reason**: forced convergence 결합 복잡도 저감 디코딩+최적 파라미터 탐색, 연산 55%·메모리접근 75% 감소 — 바이너리 LDPC 디코더 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7343339
- **Type**: conference
- **Published**: 30 Aug.-2 
- **Authors**: Muris Sarajlić, Liang Liu, Ove Edfors
- **PDF**: https://ieeexplore.ieee.org/document/7343339
- **Abstract**: Reducing the complexity of decoding algorithms for LDPC codes is an important prerequisite for their practical implementation. In this work we propose a reduction of computational complexity targeting the highly reliable codeword bits and show that this approach can be seamlessly merged with the forced convergence scheme. We also show how the minimum achievable complexity of the resulting scheme for given performance constraints can be found by solving a constrained optimization problem, and successfully apply a gradient-descent based stochastic approximation (SA) method for solving this problem. The proposed methods are tested on LDPC codes from the IEEE 802.11n standard. Computational complexity reduction of 55% and a 75% reduction of memory access have been observed.

## Two-staged Weighted Bit Flipping (WBF) decoding algorithm for LDPC codes

- **Status**: ✅
- **Reason**: LDPC용 2단 WBF/BF 비트플립 복호로 error floor 저감; 이식 가능 디코더 알고리즘(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7405679
- **Type**: conference
- **Published**: 25-27 Sept
- **Authors**: Kexiang Ma, Jing Jin, Wei Li +1
- **PDF**: https://ieeexplore.ieee.org/document/7405679
- **Abstract**: In this paper, a two-staged decoding strategy which can be used for the Weighted Bit Flipping (WBF) based decoding algorithm for LDPC codes is presented. At the two stages, a parallel WBF and bit-flipping (BF) algorithms are adopted separately. Correspondingly, by the study of the iterative decoding process of the PWBF algorithm, a simple function is introduced to dynamically implement the switch of two decoding stages. The proposed algorithm can noticeably lower the error floor of PWBF algorithm with a modest increase in computation complexity and hardware cost. The validation of the proposed algorithm is verified by simulation.

## Hybrid construction of LDPC codes with (14, 8) Hamming code

- **Status**: ✅
- **Reason**: (14,8) Hamming 기반 하이브리드 LDPC 패리티검사행렬 구성+SPA 복호; 코드 설계 기법(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7405682
- **Type**: conference
- **Published**: 25-27 Sept
- **Authors**: Huan Ma, Yangwen Yu, Lijun Zhang +1
- **PDF**: https://ieeexplore.ieee.org/document/7405682
- **Abstract**: A method for constructing LDPC codes is presented based on a (14, 8) extended Hamming code which is formed via column splitting of the (7, 4) Hamming code. With this code and hybrid construction, it is effortless to generate an LDPC code by mapping the (14, 8) extended Hamming code to components of the parity-check matrix of the LDPC code. Simulation results show that the capacity of hybrid construction of PEG code and the (14, 8) extended Hamming code with rate 0.9288 is only a difference of 2 dB around to the Shannon limit owing to the gorgeous property of the (14, 8) code with sum-product algorithm decoding.

## (7, 4)-Hamming generalized LDPC code for Rayleigh fading channel

- **Status**: ✅
- **Reason**: (7,4)Hamming GLDPC 구성·짧은사이클 제거·MLD 복호; 바이너리 코드설계 기법(E), 애매하나 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7405686
- **Type**: conference
- **Published**: 25-27 Sept
- **Authors**: Yangwen Yu, Yanan Han, Lijun Zhang +1
- **PDF**: https://ieeexplore.ieee.org/document/7405686
- **Abstract**: To get a generalized version of LDPC code, we construct (7, 4)-Hamming GLDPC code with (7, 4) Hamming component code in this paper, and give the number of short cycles of this GLDPC code as well as the code weight distribution. Via MLD, the negative effects of short cycles limited in the Hamming block can be eliminated. Simulation results show that, up to 2 dB coding gain can be obtained for GLDPC code, with faster convergence rate, in comparison with the counterpart standard code, at BER of 10−7 in Rayleigh fading channel. Even compared with the standard LDPC code which has no 4-cycles, the better behaviors for GLDPC code, with still faster convergence rate, are achieved in several limits. These results may enhance the implementation of this GLDPC code in real world.

## Complexity reduced turbo differential decoding based on layered LDPC decoding

- **Status**: ✅
- **Reason**: 차동 디코더-LDPC 간 반복 디코딩에 layered scheduling 적용, 반복수 50% 감소 — 부호 비의존 layered decoding 기법은 바이너리 LDPC BP에 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7365145
- **Type**: conference
- **Published**: 23-25 Sept
- **Authors**: Christian Cabirol, Wolfgang Sauer-Greff, Andreas Bisplinghoff +1
- **PDF**: https://ieeexplore.ieee.org/document/7365145
- **Abstract**: In case of unknown carrier phase and/or imperfect channel estimation in communication systems using QPSK it is well known that phase and channel uncertainty can be resolved by differential modulation at the expense of doubling the bit error ratio. Such a differentially modulated QPSK approach has to be applied in wavelength division multiplexing (WDM) fiber optical communication systems using coherent transmission due to the phase ambiguity of carrier phase estimation (CPE) and potential cycle slips. However, this penalty can be diminished by using an iterative decoding procedure which passes information between the differential decoder and the decoder of a low-density parity-check (LDPC) code, a powerful state-of-the art forward error correction (FEC) code. In addition, it is shown that by applying a layered decoding schedule in the LDPC decoder, the number of required iterations can be reduced by up to 50%.

## FFT-based parallel encoding algorithm for structured LDPC codes

- **Status**: ✅
- **Reason**: 구조적 QC-LDPC용 FFT 기반 병렬 인코딩 알고리즘; 인코더 측이지만 코드설계/구현 기여(E/D), 애매하므로 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7446776
- **Type**: conference
- **Published**: 21-23 Sept
- **Authors**: Yanan Fan, Xin Meng, Xiujuan Yao +1
- **PDF**: https://ieeexplore.ieee.org/document/7446776
- **Abstract**: Structured LDPC, such as RA, IRA, ARA, QC-LDPC etc., are some important LDPC codes, these codes usually have very good performance and facilitate the implementation of encoding and decoding for the structural features they have. A new method for the encoding of the structured LDPC codes has been presented, namely FFT-based parallel encoding algorithm, which uses FFT to realize the parallel encoding of LDPC codes by achieving the circular convolution in the frequency domain. The study shows that the proposed algorithm has lower computational complexity than the previously proposed encoding algorithm. Although transforming to the frequency domain requires complex operations in real domain which increasing the number of the quantization points, the throughput of the encoder has greatly improved because of the increase of the degree of parallelism. The simulation results show that the computational complexity of the FFT-based encoding algorithm has an approximately linear relationship with the size of sub-circulate matrix, and when this size goes larger, the newly proposed algorithm will possess a lower computational complexity and a higher throughput compared with the previously proposed algorithms.

## A simplifed joint demapping and decoding for LDPC coded BICM systems

- **Status**: ✅
- **Reason**: LDPC-BICM 결합 디매핑/디코딩에서 UMP-BP 단순화 + LLR 최적화 제안; 이식 가능 BP 디코더 변형(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7446764
- **Type**: conference
- **Published**: 21-23 Sept
- **Authors**: Ping Huang, Yueheng Li, Meiyan Ju
- **PDF**: https://ieeexplore.ieee.org/document/7446764
- **Abstract**: To make full use of the characteristics of LDPC decoding, Stephan ten Brink had proposed a joint iterative demapping and decoding algorithm for LDPC coded BICM systems. Based on Brink proposed algorithm, we propose a modified joint iterative scheme to further reduce the computation complex. Different from the algorithm presented by Brink, in the process of iterative demapping and decoding, the proposed method simplifies the update calculation of the LDPC parity check nodes by adopting the UMP-BP. More importantly, to compensate for the performance degradation brought by UMP-BP, LLRs optimization based on certain optimality criterion is employed for the proposed method. Numerical analysis shows that the complexity of the proposed method is less than traditional joint iterative algorithm. Simulation results also show that by LLRs optimization the proposed method achieves noticeable performance improvement compared with the BICM-ID and the joint iterative algorithm.

## A 2.48Gb/s FPGA-based QC-LDPC decoder: An algorithmic compiler implementation

- **Status**: ✅
- **Reason**: 2.48Gb/s QC-LDPC FPGA 디코더 병렬화 아키텍처 — HW(D) 이식 가능
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:7324649
- **Type**: conference
- **Published**: 20-22 Sept
- **Authors**: Swapnil Mhaske, David Uliana, Hojin Kee +3
- **PDF**: https://ieeexplore.ieee.org/document/7324649
- **Abstract**: The increasing data rates expected to be of the order of Gb/s for future wireless systems directly impact the throughput requirements of the modulation and coding systems of the physical layer. In an effort to design a suitable channel coding solution for 5G wireless systems, in this brief we present two approaches to improve the throughput of a Quasi-Cyclic Low-Density Parity-Check (QC-LDPC) decoder architecture. While providing an algorithmic method to enhance parallel processing within the decoder in the first approach, in the second approach we apply the decoder architecture to achieve another highly-parallel architecture. We have successfully validated the second approach to get a 2.48Gb/s QC-LDPC decoder implementation operating at 200MHz on the Xilinx Kintex-7 FPGA in the NI USRP-2953R. For rapid-prototyping our research findings, the high-level description of the entire decoder was translated to a Hardware Description Language (HDL), namely VHDL, using the algorithmic compiler in the National Instruments LabVIEW™ Communication System Design Suite (CSDS™). As per our knowledge, at the time of writing this paper, this is the fastest FPGA-based implementation of a standard compliant QC-LDPC decoder on a USRP using an algorithmic compiler.

## Optimized metric clipping decoder design for impulsive noise channels at high signal-to-noise ratios

- **Status**: ✅
- **Reason**: 임펄스 잡음용 metric clipping 디코더 기법, 부호 비의존적이라 LDPC BP의 LLR 클리핑으로 이식 가능성 — 애매하여 살림(C, Phase3)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7324641
- **Type**: conference
- **Published**: 20-22 Sept
- **Authors**: Changsheng Chen, Wai Ho Mow
- **PDF**: https://ieeexplore.ieee.org/document/7324641
- **Abstract**: In many practical communication systems, the channel is corrupted by non-Gaussian impulsive noise (IN). It introduces decoding metric mismatch for the traditional Euclidean metric decoders and limits system performance. The situation is worsen by the practical difficulty in accurately estimating the IN statistics. Recently, some metric clipping based decoders with a properly chosen clipping threshold has been shown to be very effective in mitigating the effect of IN, even without a precise knowledge of its statistics. However, we observe that such a clipping threshold is derived based on some assumptions which lead to an error floor in the bit error probability curve at high signal-to-noise ratio (SNR). In this work, a clipping threshold is derived by an optimization approach without exploiting the IN statistics. It is demonstrated by experiment that with our proposed clipping threshold, the optimized metric clipping decoder is able to perform close to the maximum likelihood decoding performance at high SNR under the Bernoulli Gaussian noise model with various parameters.

## A Novel Approach for Design, Implementation and Construction of Low Density Parity Check (LDPC) Memory

- **Status**: ✅
- **Reason**: LDPC용 Majority Logic 디코딩에서 무오류 시 디코딩 사이클을 줄이는 신규 ML 디코더 기법 — 이식 가능 디코더(C)/메모리 ECC(B)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7433907
- **Type**: conference
- **Published**: 2-4 Sept. 
- **Authors**: B. Harshitha, M. Karthik, Vinayak Tambralli
- **PDF**: https://ieeexplore.ieee.org/document/7433907
- **Abstract**: Memory is an important part of any digital circuit in which data is stored and retrieved. Technology scaling, lower operating voltages and high integration densities leads for failures in the reliability of memories. The main problem is Single Event Upsets (SEUs) that alters the memories from its normal way of functioning. This paper presents design and implementation of Majority Logic (ML) detecting/decoding on different cyclic codes for error detection and correction. ML decoding method is more capable to detect and correct large number of errors but it takes same high access time for both error and error free codes which impacts memory performance. In this paper, the proposed advanced ML method reduces decoding cycles when there is no error in the data read. The error detection and correction method is done by majority logic decoding and is made effective for Low Density Parity Check (LDPC) codes. This method lowers the power consumption and latency for wide range sizes of code words.

## Updating conflict solution for pipelined layered LDPC decoder

- **Status**: ✅
- **Reason**: 파이프라인 layered LDPC 디코더 데이터 갱신 충돌 해결(레이어 순서 조정) — 이식 가능 HW 아키텍처(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:7338879
- **Type**: conference
- **Published**: 19-22 Sept
- **Authors**: Zijing Wu, Kaixiong Su
- **PDF**: https://ieeexplore.ieee.org/document/7338879
- **Abstract**: Due to the overlap of nonzero sub-matrices in the successive layers of check matrix, the pipeline process might introduce data updating conflict in pipelined layered LDPC decoder. A solution to solve this problem by adjusting the decoding order of layers in check matrix and nonzero sub-matrices in the same layer is proposed in this paper. Furthermore the corresponding fast algorithm is given. In term of hardware implementation, this method which can be achieved simply by changing the order of the corresponding data in the ROMs will not increase any extra hardware overhead. Experimental results show that due to fewer idle clocks even zero idle clock need to be inserted into decoding pipeline when using this solution, the decoding rate is improved effectively. More importantly, the method will not degrade the decoding performance for LDPC codes.

## Research on Performance of Visible Light Communication Based on LDPC Code

- **Status**: ✅
- **Reason**: girth-4 제거 QC-LDPC 구성 + multiplicative factor 도입 개선 MS 디코딩(복잡도 저감) — 코드설계(E)+디코더(C) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7406090
- **Type**: conference
- **Published**: 18-20 Sept
- **Authors**: Yishuo Chen, Yanyong Su, Dong Xue +1
- **PDF**: https://ieeexplore.ieee.org/document/7406090
- **Abstract**: Visible light communication (VLC) technology is a new high-speed wireless access technology, finding a appropriate channel coding scheme is one of its main research directions. This paper proposed a new scheme to construct quasi-cyclic low-density parity-check (QC-LDPC) code. It is proved by the simulation result that the QC-LDPC code can help to improve the BER performance of the system because there is no girth four in its parity-check matrix. Then this paper studied the decoding algorithms of QC-LDPC code and proposed an improved decoding algorithm which can decrease the complexity of decoding process by introducing the multiplicative factor. The simulation results show that the QC-LDPC code is a suitable channel code for VLC, and the improved MS decoding algorithm reduces the complexity to a large extent on the basis of ensuring the BER performance of the VLC system.

## Low-rate LDPC convolutional codes with short constraint length

- **Status**: ✅
- **Reason**: LDPC convolutional code 설계 — graph 기법으로 최소거리 최대화·local cycle 분석, symbolic graph 신규 도구 (E 코드설계)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7314104
- **Type**: conference
- **Published**: 16-18 Sept
- **Authors**: Marco Baldi, Giovanni Cancellieri
- **PDF**: https://ieeexplore.ieee.org/document/7314104
- **Abstract**: We study a family of LDPC convolutional codes having code rate of the type 1/a, and analyze their minimum distance and local cycles length properties. We consider some low weight codewords that are known from the literature, and are easily obtained from the symbolic parity-check matrix of these codes. Starting from the structure of such codewords, we follow a twofold approach: i) we exploit graph-based techniques to design these codes with the aim to maximize their minimum distance while keeping the syndrome former constraint length as small as possible and ii) we provide a simple form for their generator matrices that allows to perform exhaustive searches through which we verify that the code design actually reaches its target. We also estimate the normalized minimum distance multiplicity for the codes we consider, and introduce the notion of symbolic graphs as a new tool to study the code properties.

## Threshold upper bounds and optimized design of protograph LDPC codes for the Binary Erasure Channel

- **Status**: ✅
- **Reason**: protograph LDPC threshold 상계 + capacity 근접 protograph 최적화 구성법, 바이너리 코드 설계(E) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7458400
- **Type**: conference
- **Published**: 14-18 Sept
- **Authors**: Surajkumar Harikumar, Jayanth Ramesh, Manikandan Srinivasan +1
- **PDF**: https://ieeexplore.ieee.org/document/7458400
- **Abstract**: Exact density evolution of protograph Low Density Parity Check (LDPC) codes over the Binary Erasure Channel (BEC) is considered. Upper bounds on the threshold are derived and expressed as single-variable minimizations. A simplified version of the upper bound is expressed in closed form in terms of the degrees of the nodes in the protograph. By maximizing the upper bound, useful conditions are derived for optimizing protographs to get thresholds close to capacity bounds. Using these conditions, a randomized construction method for good small-sized protographs is presented.

## VLSI architecture design and implementation of a LDPC encoder for the IEEE 802.22 WRAN standard

- **Status**: ✅
- **Reason**: 802.22 LDPC 인코더 VLSI/ASIC 아키텍처 — 이식 가능 HW(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:7347589
- **Type**: conference
- **Published**: 1-4 Sept. 
- **Authors**: Nelson Alves Ferreira Neto, Joaquim Ranyere S. de Oliveira, Wagner Luiz A. de Oliveira +1
- **PDF**: https://ieeexplore.ieee.org/document/7347589
- **Abstract**: This paper presents two architectures for the Low Density Parity Check (LDPC) encoder, the first one based on a fully serial approach and the second one in a mixed way, as well as their respective realizations in ASIC. The proposed designs are capable of operating in 84 combinations of code rate and word size, according to the IEEE 802.22 Wireless Regional Area Network (WRAN) standard, aiming low power and small area. Although the proposed architectures are primarily designed for the mentioned standard, they can be easily adapted to other wireless broadband standards.
