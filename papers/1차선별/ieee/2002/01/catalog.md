# IEEE Xplore — 2002-01 (1차선별 통과)


## ECC-less LDPC coding for magnetic recording channels

- **Status**: ✅
- **Reason**: 반복디코더의 erasure 보상 기법(TA/미디어결함) 제시 — 이레이저 처리는 NAND 디펙트 대응으로 BP 디코더에 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1001121
- **Type**: conference
- **Published**: 2002
- **Authors**: T. Morita, Y. Sato, T. Sugawara
- **PDF**: https://ieeexplore.ieee.org/document/1001121
- **Abstract**: Summary form only given. Low-density parity check (LDPC) codes are receiving considerable attention as a next-generation coding technique for magnetic recording channels, because they show a 5 dB gain over the conventional PRML method. The gain, however, reduces to 1-1.5 dB if the code is combined with an error correcting code (ECC). After the LDPC code, the ECC is not effective in the sense that its gain is less than the rate loss. In fact, we found that ECC-less LDPC codes perform better than LDPC codes with ECC. However, it is still difficult to avoid use of the ECC since the iterative decoder is unable to correct erasures caused by thermal asperity (TA) or media defects. This paper presents a method of erasure compensation for the iterative decoder. The method enables the use of ECC-less LDPC codes, which leads to better performance than using LDPC codes with ECC.

## LDPC codes and thresholds for partial response channels

- **Status**: ✅
- **Reason**: density evolution threshold로 LDPC degree sequence 최적화 및 디코더 스케줄 설계 — 코드설계/스케줄링 기법 이식 가능(E/C), 애매하나 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1001122
- **Type**: conference
- **Published**: 2002
- **Authors**: A. Thangaraj, S. W. McLaughlin
- **PDF**: https://ieeexplore.ieee.org/document/1001122
- **Abstract**: Summary form only given. The ultimate performance limit or threshold of low-density parity-check (LDPC) codes is close to capacity over various memoryless channels (S.-Y. Chung, IEEE Trans. Info. Theory, vol. 47, pp. 657-670, 2001). Since the capacity of binary-input partial response (PR) channels is unknown, we estimate the capacity by calculating the threshold of capacity-approaching LDPC codes over these channels. We assume a BCJR equalizer for the channel and a sum-product message-passing decoder for the LDPC code. We also assume that the log-likelihood ratios (LLRs) in the channel BCJR and the LDPC decoder are Gaussian. We use our results to guide the design of decoder schedules that minimize the number of computationally expensive BCJR steps. The threshold calculation method can be used to optimize the left and right degree sequences of the LDPC code factor graph, using fast linear programming methods, to provide better thresholds than regular codes.

## Regular lattice LDPC codes in perpendicular magnetic recording

- **Status**: ✅
- **Reason**: 정수격자 기반 well-structured 고율·저복잡도 LDPC 신규 구성 제시 — 바이너리 구조적 LDPC 코드설계로 이식 가능(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1001449
- **Type**: conference
- **Published**: 2002
- **Authors**: B. Vasic, E. M. Kurtas, A. V. Kuznetsov
- **PDF**: https://ieeexplore.ieee.org/document/1001449
- **Abstract**: Summary form only given. It has been well recognized that random low-density parity check (LDPC) codes perform close to the theoretical limit. However, iterative decoders employed for their decoding have very high complexity and are incapable of operating in the >1 Gbps regime, the expected data rates of the next generation of magnetic recording channels. Efficient regular LDPC codes were proposed by B. Vasic (Proc. Globecom 2001). These codes are based on balanced incomplete block designs (BIBD), known as Steiner systems, and have reduced complexity of the LDPC encoders. In this paper, using integer lattices, we introduce a new class of well structured LDPC codes that have high rates and low hardware complexity, and investigate their performance in perpendicular magnetic recording channels.

## Analysis of belief-propagation decoding of LDPC codes over the biAWGN channel using improved Gaussian approximation based on the mutual information measure

- **Status**: ✅
- **Reason**: BP density evolution의 개선된 가우시안 근사(상호정보 기반)로 임계값 분석·불규칙 LDPC 설계, 바이너리 LDPC 코드설계 이식(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1178446
- **Type**: conference
- **Published**: 2002
- **Authors**: E. Sharon
- **PDF**: https://ieeexplore.ieee.org/document/1178446
- **Abstract**: Summary form only given. The capacity of the message-passing decoder for LDPC codes can be computed by the density evolution algorithm by iteratively computing message densities. The infinite-dimensional problem of iteratively calculating the message densities in the case of the binary input AWGN channel and the belief propagation decoder can be simplified to a one-dimensional problem by using a Gaussian approximation. By assuming Gaussian densities the density evolution simplifies to updating means of Gaussian densities. An improved Gaussian approximation algorithm is suggested for computing the capacity of the BP decoder based on the mutual information measure. An analytical method for computing the mutual information of a transmitted bit with the message corresponding to it is proposed. Using this method we can approximate the non-Gaussian message by a Gaussian message that has the same mutual information with the transmitted bit. Computationally, the algorithm is similar to the Gaussian approximation algorithm proposed in Chung (2001). For various regular LDPC codes that were examined, the algorithm computed threshold values within 0.01dB or less from the exact threshold which is an improvement over the Gaussian approximation. Furthermore, additional insight on the convergence process can be gained from EXIT charts that can be derived from the algorithm. This can assist in designing better irregular LDPC codes.

## Near optimal reduced-complexity decoding algorithms for LDPC codes

- **Status**: ✅
- **Reason**: normalized/offset min-sum 계열 reduced-complexity BP 디코더 — C 이식 가능 디코더, NAND ECC 핵심 기법
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1023727
- **Type**: conference
- **Published**: 2002
- **Authors**: J. Chen, A. Dholakia, E. Eleftheriou +2
- **PDF**: https://ieeexplore.ieee.org/document/1023727
- **Abstract**: In this paper, two families of reduced-complexity algorithms for decoding low-density parity-check (LDPC) codes based on incorporating either a normalization or a correction term in the check-node update are presented. A simplified symbol-node update can also be used. Using simulations, it is shown that these simplified belief propagation (BP) approaches provide near optimum performance with different classes of LDPC codes.

## A 54 Mbps (3,6)-regular FPGA LDPC decoder

- **Status**: ✅
- **Reason**: (3,6)-regular 바이너리 LDPC partly parallel FPGA 디코더 아키텍처 — D(HW) 이식 가능
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:1049697
- **Type**: conference
- **Published**: 2002
- **Authors**: Tong Zhang, K. K. Parhi
- **PDF**: https://ieeexplore.ieee.org/document/1049697
- **Abstract**: Applying a joint code and decoder design methodology, we develop a high-speed (3, k)-regular LDPC code partly parallel decoder architecture, based on which a 9216-bit, rate-1/2 (3,6)-regular LDPC code decoder is implemented on an Xilinx FPGA device. When performing maximum 18 iterations for each code block decoding, this partly parallel decoder supports a maximum symbol throughput of 54 Mbps and achieves BER 10/sup -6/ at 2 dB over an AWGN channel.

## Finite-length analysis of LDPC codes with large left degrees

- **Status**: ✅
- **Reason**: large left degree LDPC 앙상블의 유한길이 오류확률 재귀식 — 유한길이 코드설계 분석(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1023275
- **Type**: conference
- **Published**: 2002
- **Authors**: Junan Zhang, A. Orlitsky
- **PDF**: https://ieeexplore.ieee.org/document/1023275
- **Abstract**: Extending the results of Proietti et al. (see IEEE Trans. on Information Theory, vol.48, June 2002) we derive a recursion for calculating the average error probability of random bipartite graph ensembles of LDPC codes with large left degrees over erasure channels.

## Optimized LDPC codes for partial response channels

- **Status**: ✅
- **Reason**: ISI 채널용 LDPC degree sequence 최적화 — 바이너리 LDPC 코드설계(E) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1023469
- **Type**: conference
- **Published**: 2002
- **Authors**: N. Varnica, A. Kavcic
- **PDF**: https://ieeexplore.ieee.org/document/1023469
- **Abstract**: We construct codes that can closely approach (and possibly ultimately achieve) the i.i.d. capacity of an intersymbol interference (ISI) channel with inputs confined to binary values. We use the low-density-parity-check (LDPC) degree sequences optimization method proposed by Richardson, Shokrollahi and Urbanke (see IEEE Trans. Inform. Theory, vol.47, p.619-37, February 2001) and appropriately modify it for ISI channels.

## An approximate analytical model of the message passing decoder of LDPC codes

- **Status**: ✅
- **Reason**: LDPC 메시지패싱 디코더의 1-D 가우시안 모델/안정성 분석은 BP 디코더 동작 이해·임계값 분석 기법으로 바이너리 LDPC에 이식 가능(C/E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1023303
- **Type**: conference
- **Published**: 2002
- **Authors**: R. Lehmann, G. M. Maggio
- **PDF**: https://ieeexplore.ieee.org/document/1023303
- **Abstract**: In this paper we introduce a novel one-dimensional model of the message passing decoding algorithm of low-density parity-check (LDPC) codes, based on Gaussian densities. The model consists of a closed-form 1-D map whose iterates directly represent the error probability. This map allows a qualitative analysis of the nonlinear dynamics of the decoding algorithm. Moreover, it is shown that our approach leads to the correct stability condition and that the corresponding threshold values are in good agreement with density evolution.

## A general class of LDPC finite geometry codes and their performance

- **Status**: ✅
- **Reason**: 유한기하 LDPC + 반복/다단계 다수결 하이브리드 디코딩으로 4-cycle 존재에도 저복잡도 성능 — 디코더(C)/코드설계(E) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1023581
- **Type**: conference
- **Published**: 2002
- **Authors**: Jun Xu, Heng Tang, Yu Kou +2
- **PDF**: https://ieeexplore.ieee.org/document/1023581
- **Abstract**: We present a general class of finite geometry LDPC codes which perform well with iterative decoding although their Tanner graphs may contain many cycles of length 4. A hybrid two-stage decoding algorithm is proposed that combines iterative and multi-step majority-logic decodings to achieve good performance with low decoding complexity.

## Memory-efficient turbo decoder architectures for LDPC codes

- **Status**: ✅
- **Reason**: LDPC용 TDMP 메시지패싱 알고리즘+메모리효율 디코더+permutation 기반 패리티검사 구성 — C/D/E 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1049702
- **Type**: conference
- **Published**: 2002
- **Authors**: M. M. Mansour, N. R. Shanbhag
- **PDF**: https://ieeexplore.ieee.org/document/1049702
- **Abstract**: In this paper, we propose a turbo decoding message-passing (TDMP) algorithm to decode regular and irregular low-density parity-check (LDPC) codes. The TDMP algorithm has two main advantages over the commonly employed two-phase message-passing algorithm. First, it exhibits a faster convergence behavior (up to 50% less iterations), and improvement in coding gain (up to an order of magnitude for moderate-to-high SNR and small number of iterations). Second, the corresponding decoder architecture has a significantly reduced memory requirement that amounts to a savings of (75 + 25n//spl Sigma/ node-degrees)% > 75% for code-length n. A decoder architecture featuring the TDNW algorithm is also presented. Furthermore, we propose a new structure on the parity-check matrix of an LDPC code based on permutation matrices aimed at reducing interconnect complexity and improving decoding throughput. In addition, we construct a wide range of LDPC codes based on Ramanujan graphs which possess this structure.

## On implementation of min-sum algorithm for decoding low-density parity-check (LDPC) codes

- **Status**: ✅
- **Reason**: C/D: min-sum 양자화 비트수·클리핑·개선 변형, NAND LDPC 디코더에 직접 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1188418
- **Type**: conference
- **Published**: 2002
- **Authors**: F. Zarkeshvari, A. H. Banihashemi
- **PDF**: https://ieeexplore.ieee.org/document/1188418
- **Abstract**: This paper is concerned with the implementation issues of the so-called min-sum algorithm (also referred to as max-sum or max-product) for the decoding of low-density parity-check (LDPC) codes. The effects of clipping threshold and the number of quantization bits on the performance of the min-sum algorithm at short and intermediate block lengths are studied. It is shown that min-sum is robust against quantization effects, and in many cases, only four quantization bits suffices to obtain close to ideal performance. We also propose modifications to the min-sum algorithm that improve the performance by a few tenths of a dB with just a small increase in decoding complexity.

## Performance analysis of LDPC codes for time-selective complex fading channels

- **Status**: ✅
- **Reason**: 페이딩 채널 LDPC density evolution 분석 + 메시지패싱 추정/디코딩 알고리즘 — 무선 특이적이나 디코딩 변형 이식 여지로 살림(Phase3 재검토)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1188403
- **Type**: conference
- **Published**: 2002
- **Authors**: Kaiann Fu, A. Anastasopoulos
- **PDF**: https://ieeexplore.ieee.org/document/1188403
- **Abstract**: Low-density parity-check (LDPC) codes are analyzed using density evolution techniques for a frequency-nonselective, time-selective fading channel where the fading affects both the amplitude and the phase of the transmitted signal. To aid the channel estimation process, pilot symbols are transmitted periodically. The performance of several message-passing estimation/decoding algorithms is investigated, and the optimal energy allocation between the pilot and coded symbols is evaluated. The results show that optimal power allocation can improve the performance by more than 1 dB for moderate channel dynamics. Finally, necessary and sufficient conditions for the convergence to error-free transmission are derived that take into account the channel coherence time.

## Irregular /spl pi/-rotation LDPC codes

- **Status**: ✅
- **Reason**: 불규칙 π-rotation LDPC 신규 구성(불규칙 열무게·다중 부호율, 인코딩 회로 재사용) — 바이너리 코드설계/HW(E/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1188402
- **Type**: conference
- **Published**: 2002
- **Authors**: R. Echard, Shih-Chun Chang
- **PDF**: https://ieeexplore.ieee.org/document/1188402
- **Abstract**: We present irregular /spl pi/-rotation LDPC codes by extending the classic /spl pi/-rotation parity check matrix to allow irregular column weight and choice of many code rates. The irregular /spl pi/-rotation codes are defined with a small set of parameters providing the exact definition of the code with its performance. The encoding circuit is based on the original /spl pi/-rotation design and thus users have the choice of using regular or irregular matrix patterns and various code rates without changing the encoding circuitry. We compare the performance of the irregular /spl pi/-rotation code against the binary Shannon limit for several rates.

## High-performance LDPC codes for CDMA applications

- **Status**: ✅
- **Reason**: LDPC 구성 수정으로 저BER error floor 개선(반복 알고리즘); 바이너리 LDPC 코드설계(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1045704
- **Type**: conference
- **Published**: 2002
- **Authors**: J. Haghighat, S. H. Jamali, H. Behroozi +1
- **PDF**: https://ieeexplore.ieee.org/document/1045704
- **Abstract**: Recently, V. Sorokine et al. (see IEEE Trans. Commun., vol.48, no.10, p.1660-8, 2000; vol.48, no.11, p.1818-28, 2000) have introduced a class of low-density parity-check (LDPC) codes which, when applied on an IS-95 CDMA system, show, at BER=10/sup -3/, a five-fold and two-fold increase in capacity compared to the traditional uncoded scheme and to state-of-the-art low-rate orthogonal convolutional codes, respectively. However, these codes suffer from an error-floor at lower BERs which are needed for high-quality services, such as data. To enhance the capacity of CDMA systems, not only for moderate BER values but also for lower BER values, we modify the construction of these codes slightly, to improve their performance at lower BERs. We use a simple and fast iterative algorithm instead of an exhaustive search for this purpose. Our results show a three-fold increase in capacity at BER=10/sup -5/ compared to the low-rate orthogonal convolutional codes and 1.5 times increase compared to a typical code of the Sorokine et al. ensemble.

## Low complexity LDPC codes for partial response channels

- **Status**: ✅
- **Reason**: E: column-weight-2 binary LDPC 구성으로 6-cycle 제거 + 저복잡도 구현, 코드설계 기법 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1188406
- **Type**: conference
- **Published**: 2002
- **Authors**: Hongwei Song, Jingfeng Liu, B. V. K. V. Kumar
- **PDF**: https://ieeexplore.ieee.org/document/1188406
- **Abstract**: This paper constructs and analyzes a class of regular LDPC codes with column weight of j=2, in contrast to the often-used j/spl ges/3 setting. These codes possess several significant features. First, they are free of 6-cycle, and can be easily constructed for a large range of code rates. Secondly, the parity check matrix of the code can be represented by a simple set, thus lending itself to a low complexity implementation. Thirdly, the proposed codes concatenated with proper precoder outperform j/spl ges/3 LDPC codes for partial response (PR) channels. Finally, they exhibit block error statistics significantly different from LDPC codes with j/spl ges/3, making them more compatible with Reed-Solomon error correction codes. The LDPC coded partial response (PR) channel is formulated as a dynamical model and analyzed using density evolution technique, which is used to explain the behavior of the concatenated system. A high rate (8/9) code with block size 4608 is constructed as an example, and its bit error rate (BER), block error statistics, and decoding convergence over ideal PR channel are investigated using simulation. The simulation results are consistent with the density evolution analysis, both indicating that LDPC codes with j=2 are attractive for partial response channels. PR targets for magnetic recording channel are used as examples to illustrate the performance of the proposed codes.

## Low-power VLSI decoder architectures for LDPC codes

- **Status**: ✅
- **Reason**: 저전력 VLSI LDPC 디코더 아키텍처 + 코드-디코더 공동설계로 구조적 규칙성 유도 — D/E 이식 가능.
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1029622
- **Type**: conference
- **Published**: 2002
- **Authors**: M. M. Mansour, N. R. Shanbhag
- **PDF**: https://ieeexplore.ieee.org/document/1029622
- **Abstract**: Iterative decoding of low-density parity check codes (LDPC) using the message-passing algorithm have proved to be extraordinarily effective compared to conventional maximum-likelihood decoding. However, the lack of any structural regularity in these essentially random codes is a major challenge for building a practical low-power LDPC decoder. In this paper, we jointly design the code and the decoder to induce the structural regularity needed for a reduced-complexity parallel decoder architecture. This interconnect-driven code design approach eliminates the need for a complex interconnection network while still retaining the algorithmic performance promised by random codes. Moreover, we propose a new approach for computing reliability metrics based on the BCJR algorithm that reduces the message switching activity in the decoder compared to existing approaches. Simulations show that the proposed approach results in power savings of up to 85.64% over conventional implementations.

## Low-density parity-check codes for multilevel modulation

- **Status**: ✅
- **Reason**: 바이너리 LDPC 코드 설계(error-floor 회피, 결정론적 H 생성, 선형시간 인코딩) — E 이식 가능 코드 설계. 다중레벨 변조는 채널, 부호는 바이너리
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1023714
- **Type**: conference
- **Published**: 2002
- **Authors**: E. Eleftheriou, S. Olcer
- **PDF**: https://ieeexplore.ieee.org/document/1023714
- **Abstract**: The application of low-density parity-check (LDPC) codes to multilevel modulation systems is studied. A family of binary LDPC codes that offer good performance and do not suffer from error-floor effects at low bit-error rates is introduced. A number of properties render these codes attractive for practical applications: they are specified via a small number of parameters, are encodable in linear time, and the generation of their parity-check matrix is deterministic, involving a small number of preprocessing operations. In addition, the symbol-mapping technique based on "double Gray-code labeling" for obtaining coded multilevel transmit symbols is described. Finally, it is shown that the proposed LDPC coding technique is well suited for multicarrier digital-subscriber-line transmission applications as it permits a wide range of trade-offs between latency, complexity, and system performance.

## Codes for iterative decoding from partial geometries

- **Status**: ✅
- **Reason**: 부분기하 기반 정규 바이너리 LDPC 구성과 최소거리/랭크 분석 — 코드설계(E) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1023582
- **Type**: conference
- **Published**: 2002
- **Authors**: S. J. Johnson, S. R. Weller
- **PDF**: https://ieeexplore.ieee.org/document/1023582
- **Abstract**: This work develops codes suitable for iterative decoding using the sum-product algorithm. We consider regular low-density parity-check (LDPC) codes derived from partial geometries, a large class of combinatorial structures which include several of the previously proposed algebraic constructions for LDPC codes as special cases. We derive bounds on minimum distance and rank/sub 2/(H) for codes from partial geometries, and present constructions and performance results for two classes of partial geometries which have not previously been proposed for use with iterative decoding.

## Soft decoding of several classes of array codes

- **Status**: ✅
- **Reason**: MDS 어레이코드를 LDPC로 보고 연판정 반복 디코딩, 스토리지 ECC 맥락 — 디코더(C) 이식 가능성 있어 살림(Phase3 재검토)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1023640
- **Type**: conference
- **Published**: 2002
- **Authors**: M. Blaum, J. L. Fan, Lihao Xu
- **PDF**: https://ieeexplore.ieee.org/document/1023640
- **Abstract**: The potential of using various classes of MDS array codes as LDPC codes is examined. These codes include the BR code, a modified EVENODD code, and the X-code. The algebraic structures of the array codes can enable more efficient encoding and decoding in terms of memory space and computation time. Experimental results show iterative decoding of these array codes provides comparable or slightly better error correction performance than a regular LDPC code with similar parameters. In addition, these codes can be decoded as array codes.

## Irregular codes from regular graphs

- **Status**: ✅
- **Reason**: 불규칙 LDPC를 정규 그래프에서 구성하고 차수분포 최적화로 성능 개선 — 바이너리 LDPC 코드설계(E) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1023556
- **Type**: conference
- **Published**: 2002
- **Authors**: P. O. Vontobel, H. . -A. Loeliger
- **PDF**: https://ieeexplore.ieee.org/document/1023556
- **Abstract**: It has been recognized that appropriately chosen irregular low-density parity-check (LDPC) codes have a remarkable performance advantage compared to regular LDPC codes and that their threshold is much better. Starting with regular graphs, we construct codes consisting of more sophisticated subcodes (compared to simple XORs) and show that performance gains can be achieved by optimizing the proportions of the high-degree bit nodes and the different subcodes being used.

## Irregular progressive edge-growth (PEG) Tanner graphs

- **Status**: ✅
- **Reason**: PEG 그래프 구성으로 large-girth LDPC 생성 — E 코드 설계(girth)의 대표 기법, 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1023752
- **Type**: conference
- **Published**: 2002
- **Authors**: Xiao-Yu Hu, E. Eleftheriou, D. . -M. Arnold
- **PDF**: https://ieeexplore.ieee.org/document/1023752
- **Abstract**: A general method for constructing Tanner graphs having a large girth by progressively establishing edges between symbol and check nodes in an edge-by-edge manner, called progressive edge-growth (PEG) construction, is proposed. Such an approach is powerful for generating good regular and irregular LDPC codes of short and moderate block lengths.

## Combinatorial constructions of low-density parity check codes for iterative decoding

- **Status**: ✅
- **Reason**: 차집합족·아핀기하 기반 정규 바이너리 LDPC 조합 구성과 최소거리 한계 — 코드설계(E) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1023584
- **Type**: conference
- **Published**: 2002
- **Authors**: B. Vasic
- **PDF**: https://ieeexplore.ieee.org/document/1023584
- **Abstract**: We introduce a combinatorial construction of regular low-density parity check (LDPC) codes based on balanced incomplete block designs, or more specifically on cyclic difference families of Abelian groups and affine geometries. Several constructions are presented, and the bounds on minimal distance are derived by using the concept of Pasch configurations.

## Matched information rate codes for binary ISI channels

- **Status**: ✅
- **Reason**: ISI 채널 직렬연접(inner MIR + outer irregular LDPC) 반복디코딩 — 바이너리 LDPC 디코딩/구성(C/E) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1023541
- **Type**: conference
- **Published**: 2002
- **Authors**: Xiao Ma, N. Varnica, A. Kavcic
- **PDF**: https://ieeexplore.ieee.org/document/1023541
- **Abstract**: We propose a coding/decoding strategy to approach the channel capacities for binary intersymbol interference (ISI) channels. The proposed codes are serially concatenated codes: inner matched information rate codes and outer irregular low-density parity-check (LDPC) codes. The whole system is iteratively decodable.

## Improved bit flipping decoding of low-density parity check codes

- **Status**: ✅
- **Reason**: 개선된 bit-flipping LDPC 디코더(확률적 flip) — 이식 가능 디코더 알고리즘(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1023501
- **Type**: conference
- **Published**: 2002
- **Authors**: N. Miladinovic, M. P. C. Fossorier
- **PDF**: https://ieeexplore.ieee.org/document/1023501
- **Abstract**: A new method for improving bit flipping decoding of LDPC codes is presented. In this method, bits with a number of unsatisfied check sums larger than a predetermined threshold are flipped with a probability p which is determined based on the code considered. With a proper choice of p, the proposed improved bit flipping algorithm achieves a gain not only in performance, but also in the average decoding time for SNR values of interest with respect to p=1.

## Tree-based reparameterization analysis of belief propagation and related algorithms for approximate inference on graphs with cycles

- **Status**: ✅
- **Reason**: 사이클 있는 그래프에서 BP/sum-product 재파라미터화 분석·고정점·오차 한계는 LDPC BP 디코더 분석/개선에 직접 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1023385
- **Type**: conference
- **Published**: 2002
- **Authors**: M. Wainwright, T. Jaakkola, A. Willsky
- **PDF**: https://ieeexplore.ieee.org/document/1023385
- **Abstract**: Although it is straightforward to compute the marginals of a distribution p(x) defined by a tree-structured graphical model, this same task is often difficult for graphs with cycles. The belief propagation (BP) or sum-product algorithm is an approximate method for computing such marginals; it is used in various applications (e.g., iterative decoding of turbo and LDPC codes). Belief propagation is typically presented and analyzed as a sequence of message-passing operations. We develop a different conceptual perspective that involves reparameterizing the original distribution in terms of so-called pseudomarginals on cliques of the graph. This view gives rise to a simple characterization of the fixed points, as well as an exact expression and bounds on the error for an arbitrary graph with cycles.

## Low density parity check (LDPC) codes for optical data storage

- **Status**: ✅
- **Reason**: 스토리지용 구조화 LDPC 구성(저복잡도 HW 친화 구성) — B/E, 바이너리 LDPC 코드설계 이식 가능.
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1028670
- **Type**: conference
- **Published**: 2002
- **Authors**: V. Bhagavatula, Hongwei Song, Jingfeng Liu
- **PDF**: https://ieeexplore.ieee.org/document/1028670
- **Abstract**: Low-density parity check (LDPC codes, first introduced by Gallager (1962), are error-correcting codes based on very sparse parity check matrices. Recently, in the wake of excellent performance of turbo codes, LDPC codes were rediscovered as another category of random codes approaching the Shannon capacity limit with practical decoding complexity. Extensive investigation of the applications of turbo codes and LDPC codes for data storage channels has been reported. While LDPC codes can be iteratively decoded using the sum-product algorithm with moderate complexity, the memory required to specify the nonzero elements in the random parity check matrix can be a major challenge for hardware implementation. Construction of good LDPC codes with structure is particularly desired in data storage channels to facilitate low complexity implementation. We address this issue by introducing a class of low complexity structured LDPC codes which are useful for optical data storage.

## Iterative decoding of turbo codes based on factor graphs

- **Status**: ✅
- **Reason**: turbo 부호이지만 factor graph+sum-product 디코딩을 적용—부호비의존 메시지패싱으로 바이너리 LDPC BP에 이식 가능성(C), 애매하여 in
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1180310
- **Type**: conference
- **Published**: 2002
- **Authors**: Lianxiang Zhu, Wenjiang Feng, Shizhong Yang
- **PDF**: https://ieeexplore.ieee.org/document/1180310
- **Abstract**: Turbo codes and low-density parity-check (LDPC) codes both have their advantages and can achieve the Shannon limited performance. The constituent recursive systematic convolutional (RSC) codes in turbo codes are more structural and this lends the encoding problem easier with a shift-register circuit. While the encoding of LDPC codes is performed via matrix multiplication, and this is more complex than it appears for capacity-approaching LDPC codes. On the other hand, the soft-input soft-output BCJR algorithm, or the sub-optimal version of it, used for turbo-decoding is rather complex while sum-product algorithm used for LDPC decoding lends itself to parallel implementation and is computationally simpler. Combining the turbo codes encoding and LDPC decoding, a new scheme based on factor graphs and sum-product algorithm is developed, it can reduce the decoding complexity of turbo codes greatly, and also has some guides in the designing of interleaver and the choosing of RSC constituent codes. Simulation shows the correctness of the scheme.

## Performance evaluation of LDPC code on VR2 channel

- **Status**: ✅
- **Reason**: 자기기록 채널용 바이너리 LDPC 성능평가(스토리지 ECC, B) — 초록만으로 떼어낼 기법 판단 애매해 in으로 살림
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:1000642
- **Type**: conference
- **Published**: 2002
- **Authors**: D. Yang, R. Molstad, Y. Yip
- **PDF**: https://ieeexplore.ieee.org/document/1000642
- **Abstract**: Summary form only given. LDPC (low density parity check) codes are error correcting codes with sparse parity check matrices. They can be iteratively decoded with a message passing algorithm. The application of LDPC codes to magnetic recording channels has been previously reported. LDPC codes offer great potential to mitigate the dropout effects present in magnetic tape recording systems.

## Low-density parity-check codes for digital subscriber lines

- **Status**: ✅
- **Reason**: DSL용 linear-time encodable 바이너리 LDPC 코드 패밀리 신규 구성 + 인코딩/복잡도 분석, 코드설계(E)로 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:997149
- **Type**: conference
- **Published**: 2002
- **Authors**: E. Eleftheriou, S. Olcer
- **PDF**: https://ieeexplore.ieee.org/document/997149
- **Abstract**: The paper investigates the application of low-density parity-check (LDPC) codes to digital subscriber-line (DSL) transmission systems that employ discrete multitone modulation. A family of linear-time encodable binary LDPC codes that are well-suited for DSL transmission is introduced. Encoding and symbol mapping for multilevel modulation are described. Simulation results show that even under tight latency constraints good net coding gains can be achieved. Implementation complexity is analyzed and compared with that of trellis-coded modulation as employed in current asymmetric DSL transceivers. The incorporation of powerful LDPC coding techniques into next-generation DSL modems appears to be possible with reasonable increase in transceiver complexity.

## Turbo decoder architectures for low-density parity-check codes

- **Status**: ✅
- **Reason**: C/D: LDPC turbo 디코딩 스케줄/아키텍처(수렴 가속·메모리 절감), 바이너리 LDPC 디코더 이식 가능. GLD 확장은 부수
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1188425
- **Type**: conference
- **Published**: 2002
- **Authors**: M. M. Mansour, N. R. Shanbhag
- **PDF**: https://ieeexplore.ieee.org/document/1188425
- **Abstract**: Turbo decoding of low-density parity-check (LDPC) and generalized low-density (GLD) codes and the corresponding decoder architectures are considered. A regular (c, r)-LDPC code of length n is viewed as the intersection of c interleaved super-codes where each super-code is the direct sum of n/r independent single parity-check sub-codes. Extensions to GLD codes simply utilize more powerful sub-codes. The turbo decoding schedule is employed to decode LDPC and GLD codes using constituent soft-input soft-output (SISO) decoders that communicate through c interleavers. The proposed schedule exhibits a faster convergence behavior, and hence lower decoding latency, than the commonly employed two-phase schedule, and has a reduced memory requirement that is a function of the number of super-codes. The performance of the turbo decoding schedule is evaluated through simulations over an AWGN channel.

## Code rate and the area under extrinsic information transfer curves

- **Status**: ✅
- **Reason**: EXIT 차트 area property가 LDPC 반복디코딩 수렴 분석에 적용되는 모델 제시, 코드설계/디코더 수렴 분석 기법 이식 가능(C/E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1023387
- **Type**: conference
- **Published**: 2002
- **Authors**: A. Ashikhmin, G. Kramer, S. ten Brink
- **PDF**: https://ieeexplore.ieee.org/document/1023387
- **Abstract**: Extrinsic information transfer (EXIT) charts predict the convergence behavior of iterative decoding and detection schemes. The EXIT analysis is made precise by introducing a model that applies to iterative decoding of parallel concatenated, serially concatenated, and low-density parity-check codes. The model leads to an area property of EXIT charts.

## Efficient encoding and minimum distance bounds of Reed-Solomon-type array codes

- **Status**: ✅
- **Reason**: RS-array 기반 바이너리 QC-LDPC 구성 + 선형복잡도 인코딩 + 최소거리 bound — 코드설계(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1023554
- **Type**: conference
- **Published**: 2002
- **Authors**: T. Mittelholzer
- **PDF**: https://ieeexplore.ieee.org/document/1023554
- **Abstract**: Array codes that are based on Reed-Solomon codes have been recognized to give a simple deterministic construction of binary low-density parity-check codes, which for moderate lengths and high rates achieve similar performance as randomly constructed codes. New sparse generator matrices for these quasi-cyclic codes are presented that lead to fast encoding schemes with linear complexity in the code length. From the low-density properties of these generator matrices upper bounds on the minimum Hamming distance of the codes are derived.

## On circulant low density parity check codes

- **Status**: ✅
- **Reason**: 유한기하 기반 cyclic/QC-LDPC 구성, 반복디코딩 — 바이너리 LDPC 코드설계(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1023472
- **Type**: conference
- **Published**: 2002
- **Authors**: Yu Kou, Jun Xu, Heng Tang +2
- **PDF**: https://ieeexplore.ieee.org/document/1023472
- **Abstract**: This paper presents three classes of low density parity check codes constructed based on the cyclic structure of lines in finite geometries. Codes in these classes are either cyclic or quasi-cyclic, and they perform well with iterative decoding.

## On algebraic construction of Gallager low density parity check codes

- **Status**: ✅
- **Reason**: Gallager LDPC의 대수적 구성 두 클래스 — E 코드 설계, 바이너리 LDPC
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1023754
- **Type**: conference
- **Published**: 2002
- **Authors**: Heng Tang, Jun Xu, Yu Kou +2
- **PDF**: https://ieeexplore.ieee.org/document/1023754
- **Abstract**: This paper presents two classes of low density parity check codes. Codes in these two classes perform well with iterative decoding.

## Lattice low-density parity check codes and their application in partial response systems

- **Status**: ✅
- **Reason**: 격자 기반 doubly-circulant(QC) 바이너리 LDPC 구성, 최소거리 경계 — E 이식 가능 코드 설계
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1023725
- **Type**: conference
- **Published**: 2002
- **Authors**: B. Vasic, A. Kuznetsov, E. Kurtas
- **PDF**: https://ieeexplore.ieee.org/document/1023725
- **Abstract**: This paper introduces a combinatorial construction of high rate low-density parity check codes based on two-dimensional integer lattices. A class of codes with a wide range of lengths, column weights and minimum distances is obtained. The resulting codes are doubly circulant, i.e. the matrix of parity checks is an array of circulant matrices. The bounds on the minimum distance are established and the performance of these codes in partial response channels is investigated.

## Iterative decoding for two-dimensional intersymbol interference channels

- **Status**: ✅
- **Reason**: 스토리지 read-back 2D ISI 반복 디코딩, 채널+ECC 결합 그래프 메시지패싱(C) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1023470
- **Type**: conference
- **Published**: 2002
- **Authors**: J. A. O'Sullivan, N. Singla, Yunxiang Wu +1
- **PDF**: https://ieeexplore.ieee.org/document/1023470
- **Abstract**: We study iterative decoding and equalization for information storage systems that have two-dimensional (2-D) intersymbol interference (ISI) during read-back. Four iterative schemes for 2-D equalization are introduced and evaluated. Two schemes are based on turbo equalization, the third on minimum mean squared error estimation, and the fourth on message passing on the combined graph of the channel ISI and the error correction code.

## On the suboptimality of iterative decoding for finite length codes

- **Status**: ✅
- **Reason**: 유한길이 부호의 반복복호 준최적성·그래프 사이클 영향 분석 — 디코더/사이클 이해(C/E) 이식 가능, 애매하면 in
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1023276
- **Type**: conference
- **Published**: 2002
- **Authors**: M. Isaka, M. Fossorier, H. Imai
- **PDF**: https://ieeexplore.ieee.org/document/1023276
- **Abstract**: We investigate the property of iterative decoding for finite length codes, and give some insights on the suboptimality of iterative decoding due to the cycles in the graph representation of the codes, for several different types of iteratively decodable codes.

## An alternate algorithm for calculating generalized posterior probability and decoding

- **Status**: ✅
- **Reason**: 일반화 사후확률 계산을 짧은 루프 코드 디코딩에 적용, 병렬화 가능한 메시지패싱류 알고리즘 — 디코더(C) 이식 가능성 있어 애매하므로 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1023610
- **Type**: conference
- **Published**: 2002
- **Authors**: T. Matsushima, T. K. Matsushima, S. Hirasawa
- **PDF**: https://ieeexplore.ieee.org/document/1023610
- **Abstract**: The accurate and efficient calculation of ordinary and generalized posterior distributions is an important problem in the several research fields such as decoding, AI, statistics and statistical mechanics. The condition of generalized posterior distributions is not given by the deterministic values such as X = x, but by the distributions such as P(X = x) = p. If the condition is P(X = x) = 1 then the generalized posterior distribution is an ordinary posterior distribution. A procedure using the sum of the e-projection 1 vectors is proposed. Since the procedure is suitable for parallel algorithms, an alternate algorithm for calculating generalized posterior distributions on log linear models is given by the procedure. The proposed algorithm works well for codes with short loops.

## Architectures and implementations of low-density parity check decoding algorithms

- **Status**: ✅
- **Reason**: LDPC 디코더 VLSI 아키텍처/병렬 처리요소/복잡도 절감—이식 가능 HW 아키텍처(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:1187067
- **Type**: conference
- **Published**: 2002
- **Authors**: E. Yeo, B. Nikolic, V. Anantharam
- **PDF**: https://ieeexplore.ieee.org/document/1187067
- **Abstract**: Architectures for low-density parity-check (LDPC) decoders are discussed, with methods to reduce their complexity. Serial implementations similar to traditional microprocessor datapaths are compared against implementations with multiple processing elements that exploit the inherent parallelism in the decoding algorithm. Several classes of LDPC codes, such as those based on irregular random graphs and geometric properties of finite fields are evaluated in terms of their suitability for VLSI implementation and performance as measured by bit-error rate. Efficient realizations of low-density parity check decoders under area, power, and throughput constraints are of particular interest in the design of communications receivers.

## Factor graphs based iterative decoding of turbo codes

- **Status**: ✅
- **Reason**: factor graph+sum-product 기반 디코딩(1180310 동류), 부호비의존 메시지패싱 이식 가능성(C), 애매하여 in
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1180569
- **Type**: conference
- **Published**: 2002
- **Authors**: Lianxiang Zhu, Jifeng Wang, Shizhong Yang
- **PDF**: https://ieeexplore.ieee.org/document/1180569
- **Abstract**: Turbo codes and low-density parity-check (LDPC) codes both have their advantages and can achieve the Shannon limited performance. Combining the turbo codes encoding and LDPC decoding, a new scheme based on factor graphs and sum-product algorithm is developed in this paper. It can reduce the decoding complexity of turbo codes greatly, and also has some guides in the designing of interleaver and the choosing of recursive systematic convolutional (RSC) constituent codes.

## Density evolution for BP-based decoding algorithms of LDPC codes and their quantized versions

- **Status**: ✅
- **Reason**: C: normalized/offset BP-based(min-sum 변형) 밀도진화 최적화 + 유한 양자화 효과, 디코더 직접 이식
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1188424
- **Type**: conference
- **Published**: 2002
- **Authors**: Jinghu Chen, P. M. C. Fossorier
- **PDF**: https://ieeexplore.ieee.org/document/1188424
- **Abstract**: In this paper, we analyze the performance of two improved BP-based decoding algorithms for LDPC codes, namely the normalized BP-based and the offset BP-based algorithms, by means of density evolution. The numerical calculations show that with one properly chosen parameter for each of these two improved BP-based algorithms, performances very close to that of the BP algorithm can be achieved. Simulation results for LDPC codes with code length moderately long validate the proposed optimization. Finite quantization effects on the BP-based and the offset BP-based decoding algorithms are evaluated.

## Shuffled belief propagation decoding

- **Status**: ✅
- **Reason**: Shuffled BP는 부호 비의존적 BP 스케줄링 개선(직렬/병렬, 빠른 수렴) — C(이식 가능 디코더 알고리즘)에 직접 해당
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1197141
- **Type**: conference
- **Published**: 2002
- **Authors**: Juntan Zhang, M. Fossorier
- **PDF**: https://ieeexplore.ieee.org/document/1197141
- **Abstract**: In this paper, we propose a shuffled version of the belief propagation (BP) algorithm for the decoding of low-density parity-check (LDPC) codes. We show that when the Tanner graph of the code is acyclic and connected, the proposed scheme is optimal in the sense of MAP decoding and converges faster (or at least no slower) than the standard BP algorithm. Interestingly, this new version keeps the computational advantages of the forward-backward implementations of BP decoding. Both serial and parallel implementations are considered. We show by simulation that the new schedule offers better performance/complexity trade-offs.

## Iterative encoding of low-density parity-check codes

- **Status**: ✅
- **Reason**: 그래프 기반 LDPC 반복 인코딩(디코더 아키텍처 재사용, 4-cycle 제거, Jacobi 메시지패싱) — HW/코드설계(D/E) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1188405
- **Type**: conference
- **Published**: 2002
- **Authors**: D. Haley, A. Grant, J. Buetefuer
- **PDF**: https://ieeexplore.ieee.org/document/1188405
- **Abstract**: Motivated by the potential to reuse the decoder architecture, and thus reduce circuit space, we explore the use of iterative encoding techniques which are based upon the graphical representation of the code. We design codes by identifying associated encoder convergence constraints and also eliminating some well known undesirable properties for sum-product decoding such as 4-cycles. In particular we show how the Jacobi method for iterative matrix inversion can be viewed as message passing and employed as the core of an iterative encoder. Example constructions of both regular and irregular LDPC codes that are encodable using this method are investigated.

## Application of Gaussian approximation to iterative decoding with finite blocklengths

- **Status**: ✅
- **Reason**: 유한블록길이 반복디코딩 가우시안근사 수렴분석(워터폴/에러플로어 구분) — LDPC 포함, 코드설계 해석기법 이식 가능(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1040519
- **Type**: conference
- **Published**: 2002
- **Authors**: A. Ozgur Yilmaz, W. E. Stark
- **PDF**: https://ieeexplore.ieee.org/document/1040519
- **Abstract**: In this paper, the convergence analysis based on Gaussian approximation is extended to small and medium blocklengths. Gaussian approximation to extrinsic information has been instrumental in understanding and predicting the behavior of iterative decoding for codes that would allow iterative decoding such as turbo codes and LDPC codes. It enables a procedure to predict the "waterfall" region behavior where a steep slope of error rate curves is observed. As is well known, combination of transfer function and union bound techniques can be applied to predict the "error floor" region performance with necessary assumptions. This paper provides a framework to distinguish the different regions of behavior through defining a decoding failure probability.

## Iterative decoding of low-density parity check codes over compound channels

- **Status**: ✅
- **Reason**: LDPC 반복 결합 채널추정+복호, 바이너리 LDPC 디코더 기법 이식 가능성(C), 애매하면 in
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1178448
- **Type**: conference
- **Published**: 2002
- **Authors**: I. Sutskover, S. Shamai, J. Ziv
- **PDF**: https://ieeexplore.ieee.org/document/1178448
- **Abstract**: An iterative joint-channel estimation and decoding system is proposed for decoding of low-density parity-check (LDPC) codes over compound channels. The bit-error-rate performance of the complete system is numerically evaluated and a new concept for design of good channel estimators follows.

## Design of LDPC graphs for hardware implementation

- **Status**: ✅
- **Reason**: HW 구현 친화적 LDPC 그래프 설계(loopiness/HW 비용 동시 최소화) — D/E HW 친화 코드 설계, 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1023755
- **Type**: conference
- **Published**: 2002
- **Authors**: J. Thorpe
- **PDF**: https://ieeexplore.ieee.org/document/1023755
- **Abstract**: A methodology for generating bipartite graphs for LDPC codes which both exhibit good performance under message passing decoding and are amenable to direct hardware implementation is described. To this end, we define a novel quantitative measure of the "loopiness" of a graph, as well as a quantitative measure of the cost of direct hardware implementation, and use the well-known simulated annealing algorithm to simultaneously minimize both quantities. Finally, we simulate the decoding of several rather short codes to show that the performance is indeed predicted by our loopiness measure.

## Parallel VLSI architectures for a class of LDPC codes

- **Status**: ✅
- **Reason**: LDPC 클래스의 병렬 VLSI 인/디코더 아키텍처, 6비트 양자화/희소 행렬; 이식 가능 디지털 HW(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:1010932
- **Type**: conference
- **Published**: 2002
- **Authors**: Sungwook Kim, G. E. Sobelman, Jaekyun Moon
- **PDF**: https://ieeexplore.ieee.org/document/1010932
- **Abstract**: This paper presents high-performance encoder and decoder architectures for a class of low density parity check (LDPC) codes. The codes considered here are based on the parallelly concatenated parity check encoder structure. A major advantage of these codes is that the generator matrix and the parity check matrix are both sparse, which leads to efficient VLSI implementations for the encoder and the decoder. Our designs use 6-bit quantization with a code rate of 8/9 and a block size of 576 bits. An evaluation of the speed and hardware complexity is given, and simulation results for the bit error rate are obtained.

## Decoding algorithms for LDPC codes transmitted over channels with ISI

- **Status**: ✅
- **Reason**: ISI 채널용 Gallager 복호 확장(BCJR 결합·일반화 메시지) 신규 디코더 알고리즘, 바이너리 LDPC BP 이식(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1178450
- **Type**: conference
- **Published**: 2002
- **Authors**: T. Friedlander, D. Burshtein
- **PDF**: https://ieeexplore.ieee.org/document/1178450
- **Abstract**: Summary form only given. LDPC (low density parity check) codes (Gallager (1963)) are linear parity check codes with a sparse parity check matrix. In our work Gallager's original decoding algorithm is extended to alleviate the problem of channel with finite memory. Two decoding algorithms are derived. The basic algorithm tracks the original derivation of Gallager with the necessary adaptations. This results in a single usage of the BCJR algorithm, whereas the iterative part remains intact.. The second algorithm is a generalization of the first. While the basic algorithm only utilizes the correlation among adjacent digits to achieve an improved estimation of the prior probabilities, the generalized algorithm also exploits the information lying in the parity checks in which the adjacent digits participate. This results in modified rightbound messages. The generalized algorithm is asymptotically optimal in the sense of achieved bit error rate based on the information extracted from a given number of adjacent digits.

## Decoding turbo-like codes via linear programming

- **Status**: ✅
- **Reason**: LP 디코딩 도입—LP decoding은 LDPC BP 대안 디코더로 이식되는 기법(C), 애매하여 in
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1181948
- **Type**: conference
- **Published**: 2002
- **Authors**: J. Feldman, D. R. Karger
- **PDF**: https://ieeexplore.ieee.org/document/1181948
- **Abstract**: We introduce a novel algorithm for decoding turbo-like codes based on linear programming. We prove that for the case of repeat-accumulate (RA) codes, under the binary symmetric channel with a certain constant threshold bound on the noise, the error probability of our algorithm is bounded by an inverse polynomial in the code length. Our linear program (LP) minimizes the distance between the received bits and binary variables representing the code bits. Our LP is based on a representation of the code where code words are paths through a graph. Consequently, the LP bears a strong resemblance to the min-cost flow LP. The error bounds are based on an analysis of the probability, over the random noise of the channel, that the optimum solution to the LP is the path corresponding to the original transmitted code word.

## High-rate low-density parity check codes based on anti-Pasch affine geometries

- **Status**: ✅
- **Reason**: girth-6, 최소거리>=6 보장하는 조합론적 정규 LDPC 구성(E) — error floor 개선용 바이너리 코드설계로 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:997067
- **Type**: conference
- **Published**: 2002
- **Authors**: B. Vasic
- **PDF**: https://ieeexplore.ieee.org/document/997067
- **Abstract**: We introduce a combinatorial construction of regular low-density parity check codes based on balanced incomplete block designs whose bipartite graphs have girth six. Our construction employs a special type of anti-Pasch affine geometry that result in codes having minimum distance of at least six. We are primarily concerned with very high-rate codes and low column weights, but the proposed construction can be used to generate long codes as well as codes of arbitrary column weight.

## Optimized irregular Gallager codes for OFDM transmission

- **Status**: ✅
- **Reason**: 불규칙 Gallager(LDPC) 차수분포 최적화 코드설계(E), 바이너리 LDPC; OFDM은 응용일 뿐 기법 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1046693
- **Type**: conference
- **Published**: 2002
- **Authors**: V. Mannoni, D. Declereq, G. Gelle
- **PDF**: https://ieeexplore.ieee.org/document/1046693
- **Abstract**: We present an optimized channel coding scheme for OFDM transmitter. Traditional coding methods use regular codes, in the sense that each bit participates in the same way to the channel encoding. Our approach consists in using a priory assumption on the channel available at the transmitter in order to optimize the coding scheme. We have considered the irregular Gallager block codes in our study. Simulations provide evidence of the usefulness of our approach with a gain of 2 dB at a bit error rate equal to 10/sup -5/ for optimized irregular coding scheme compared to regular one.

## Simple erasure correcting codes with capacity achieving performance

- **Status**: ✅
- **Reason**: 세미랜덤 LDPC 기반 erasure 정정 부호 신규 구성(간단한 enc/dec, capacity-achieving) — 스토리지 ECC/코드설계(B/E) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1188354
- **Type**: conference
- **Published**: 2002
- **Authors**: Li Ping, Rong Sun
- **PDF**: https://ieeexplore.ieee.org/document/1188354
- **Abstract**: This paper presents a simple erasure correcting coding scheme based on semi-random low-density-parity-check codes. Compared with tornado codes, the proposed scheme has much simpler encoder and decoder structures, yet still has proven capacity-achieving performance.

## LDPC decoding using multiple representations

- **Status**: ✅
- **Reason**: 다중 패리티검사 표현 기반 BP 디코더 아키텍처 개선 — C 이식 가능 디코더
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1023728
- **Type**: conference
- **Published**: 2002
- **Authors**: K. Andrews, S. Dolinar, F. Pollara
- **PDF**: https://ieeexplore.ieee.org/document/1023728
- **Abstract**: For a particular block code, a multitude of different parity check matrices could be chosen to represent the code constraints. We demonstrate that belief propagation decoders based on different parity check matrices often respond in different ways, and that for a given complexity, it may be preferable to use several decoders for fewer iterations, than to run a single decoder for many iterations. We also propose some additional decoder architectures that use multiple representations of the parity constraints.

## A new construction for low density parity check convolutional codes

- **Status**: ✅
- **Reason**: LDPC convolutional code 신규 구성(대수+랜덤), 바이너리 SC-LDPC 코드설계 이식 가능(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1115468
- **Type**: conference
- **Published**: 2002
- **Authors**: A. Sridharan, D. J. Costello
- **PDF**: https://ieeexplore.ieee.org/document/1115468
- **Abstract**: Low density parity check (LDPC) block codes have been shown to achieve near capacity performance for binary transmission over noisy channels. Block codes, however, require splitting the data to be transmitted into frames, which can be a disadvantage in some applications. Convolutional codes, on the other hand, have no such requirement, and are well suited for continuous transmission. Felstrom and Zigangirov (1999) proposed the construction of periodic time-varying convolutional codes with LDPC matrices. A set of time-invariant LDPC convolutional codes was described by Sridharan et al. (2002). The codes of Felstrom and Zigangirov were obtained by random construction techniques whereas those of Sridharan et al. were essentially algebraic constructions. The new LDPC convolutional codes described here are obtained by introducing a degree of randomness into the latter construction.

## Designing irregular LPDC codes using EXIT charts based on message error rate

- **Status**: ✅
- **Reason**: 수정 EXIT 차트 기반 비정규 LDPC 설계 기법 — E 코드 설계에 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1023726
- **Type**: conference
- **Published**: 2002
- **Authors**: M. Ardakani, F. R. Kschischang
- **PDF**: https://ieeexplore.ieee.org/document/1023726
- **Abstract**: A new analysis of irregular low density parity check (LDPC) codes on AWGN channels based on modified extrinsic information transfer (EXIT) charts is presented. We modify EXIT charts to track the message error rate transfer characteristics of the constituent codes. Previous analyses, which make a Gaussian assumption for all messages passed, are inaccurate at low SNRs. We more accurately track the message error rate transfer by making a Gaussian approximation only for messages sent from variable nodes, with statistics of messages from check nodes computed by simulation. This makes the analysis more accurate, particularly for low rate codes where, at low SNR, the messages from check nodes are far from Gaussian. The new analysis simplifies understanding of the irregular codes to the level of regular case, leading to a simple approach to the design of irregular codes. We have used this method to design irregular LDPC codes that perform close to the Shannon limit over a wider range of rates and variable degrees as compared to previous work. The same method can be used for many other codes defined on graphs.

## Construction of low density parity check codes: a combinatoric design approach

- **Status**: ✅
- **Reason**: BIBD 조합설계 기반 바이너리 LDPC 구성법 — 코드설계(E) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1023583
- **Type**: conference
- **Published**: 2002
- **Authors**: B. Ammar, B. Honary, Y. Kou +1
- **PDF**: https://ieeexplore.ieee.org/document/1023583
- **Abstract**: This paper presents a method for constructing low density parity check (LDPC) codes based on a special type of combinatoric designs, known as the balanced incomplete block designs (BIBDs). Several classes of BIBDs suitable for constructing LDPC codes are presented. Codes constructed based on these classes of BIBDs perform well with iterative decoding.

## Iterative majority logic decoding of a class of Euclidean Geometry codes

- **Status**: ✅
- **Reason**: EG 바이너리 LDPC의 임계최적화 반복 다수결 경판정 디코딩(스토리지 응용 명시) — 디코더(C)/코드설계(E) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1023637
- **Type**: conference
- **Published**: 2002
- **Authors**: A. Thangaraj, S. W. McLaughlin
- **PDF**: https://ieeexplore.ieee.org/document/1023637
- **Abstract**: Hard decision decoding of low density parity check (LDPC) codes has potential applications in practical settings like data storage. For this purpose, it is important for the code to have an assured minimum distance and, hence, guaranteed error correction capability. In this paper, we show that with very high probability the guaranteed error correction capability of Euclidean geometry (EG) codes using threshold-optimized, iterative majority logic (ML) decoding is much greater than the usual single iteration ML decoding, making these codes much more attractive for hard decision decoding. For instance, the (262143, 242461, t/spl ges/256) EG code (a (512, 512)-regular LDPC code) can correct t=580 bit errors with probability better than 1-1/spl times/10/sup -58/.

## Finite-length analysis of various low-density parity-check ensembles for the binary erasure channel

- **Status**: ✅
- **Reason**: BEC 유한길이 LDPC 앙상블 error floor 분석 + degree-2 노드 구조 제어로 좋은 유한길이 코드 설계 지침 — 코드설계(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1023273
- **Type**: conference
- **Published**: 2002
- **Authors**: T. Richrdson, A. Shokrollahi, R. Urbanke
- **PDF**: https://ieeexplore.ieee.org/document/1023273
- **Abstract**: We investigate the average erasure probability of the belief propagation algorithm over the binary erasure channel (BEC) for various finite-length low-density parity-check (LDPC) ensembles. In particular, we give tight upper bounds on the "error floor", i.e., on the contribution to the erasure probability stemming from relatively small deficiencies in the graph. We also define and analyse "expurgated" ensembles and give upper bounds on the error floor of "typical" codes. Finally, we show that typical codes of properly chosen ensembles have an erasure correcting radius which grows linearly in the block length. The presented method provides valuable insight into how finite-length codes should be designed. Although the standard ensemble can achieve capacity on the BEC, the construction of good finite-length codes requires careful control of the structure of the degree two variable nodes. In this paper, we investigate the standard ensemble, the Poisson ensemble, an ensemble in which degree two nodes are added in a cycle, and an ensemble in which different degree two variable nodes have distinct neighboring check nodes.

## ECC-less LDPC coding for magnetic recording channels

- **Status**: ✅
- **Reason**: 스토리지(자기기록) 바이너리 LDPC + erasure 보상 디코딩 — B/C 해당, NAND erasure(MD/TA 유사 결함)에 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1042169
- **Type**: journal
- **Published**: 2002
- **Authors**: T. Morita, Y. Sato, T. Sugawara
- **PDF**: https://ieeexplore.ieee.org/document/1042169
- **Abstract**: This paper presents a system for magnetic recording channels, using low-density parity check (LDPC) codes and a novel method of erasure compensation that can correct thermal asperity (TA) and media defects (MDs). The system does not require error-correction codes (ECC) based on the Reed-Solomon codes, and thus is ECC-less. Simulation results show that the performance of ECC-less LDPC codes is better than that of the LDPC codes with ECC. It is also shown that LDPC codes of rate 0.814 can correct 48-byte TA and 24-byte MD, which are sufficient for practical hard disk drives.

## Thresholds and scheduling for LDPC-coded partial response channels

- **Status**: ✅
- **Reason**: LDPC 디코더 스케줄링 설계(가우시안근사 threshold 기반 schedule 최적화) — C/E, NAND LDPC 디코더 스케줄 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1042170
- **Type**: journal
- **Published**: 2002
- **Authors**: A. Thangaraj, S. W. McLaughlin
- **PDF**: https://ieeexplore.ieee.org/document/1042170
- **Abstract**: Low-density parity check (LDPC) codes exhibit a threshold phenomenon over a wide variety of channels. The threshold serves as a good parameter for system and code design, and is usually very close to channel capacity. There has been a great deal of recent work surrounding the use of LDPC and turbo codes with iterative decoding for partial response (PR) channels. In this paper, we calculate thresholds for LDPC codes over binary-input PR channels using a Gaussian approximation. We show that the threshold varies according to decoder schedule, and we identify schedules that result in good thresholds. Conversely, we use our results to guide the design of decoder schedules that minimize the number of computationally expensive Bahl-Cocke-Jelinek-Raviv algorithm steps.

## LDPC codes based on mutually orthogonal latin rectangles and their application in perpendicular magnetic recording

- **Status**: ✅
- **Reason**: 상호직교 라틴직사각형 기반 고율 바이너리 LDPC 구조적 구성(E) + 저복잡도 인코더/디코더 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1042183
- **Type**: journal
- **Published**: 2002
- **Authors**: B. Vasic, E. M. Kurtas, A. V. Kuznetsov
- **PDF**: https://ieeexplore.ieee.org/document/1042183
- **Abstract**: We present a large family of low-density parity-check (LDPC) codes constructed from mutually orthogonal Latin rectangles. The construction is conceptually simple and gives high-rate LDPC codes with a structure of the parity check matrix that leads to a low complexity implementation of encoders and decoders. The bit-error rate characteristics are characterized by simulations of the soft iterative decoding in perpendicular magnetic read channels with different partial-response targets and types of noise.

## Joint message-passing decoding of LDPC codes and partial-response channels

- **Status**: ✅
- **Reason**: LDPC와 partial-response 채널의 결합 메시지패싱 디코더 제안(detector/decoder 매칭); 이식 가능 BP/디코더 기법(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1003830
- **Type**: journal
- **Published**: 2002
- **Authors**: B. M. Kurkoski, P. H. Siegel, J. K. Wolf
- **PDF**: https://ieeexplore.ieee.org/document/1003830
- **Abstract**: Ideas of message passing are applied to the problem of removing the effects of intersymbol interference (ISI) from partial-response channels. Both bit-based and state-based parallel message-passing algorithms are proposed. For a fixed number of iterations less than the block length, the bit-error rate of the state-based algorithm approaches a nonzero constant as the signal-to-noise ratio (SNR) approaches infinity. This limitation can be removed by using a precoder. It is well known that low-density parity-check (LDPC) codes can be decoded using a message-passing algorithm. Here, a single message-passing detector/decoder matched to the combination of a partial-response channel and an LDPC code is investigated.

## Finite-length analysis of low-density parity-check codes on the binary erasure channel

- **Status**: ✅
- **Reason**: 바이너리 LDPC의 유한길이 분석(BEC), 정규 앙상블 정확/상한 erasure 확률; 코드설계 기여(E, error floor/finite-length)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1003839
- **Type**: journal
- **Published**: 2002
- **Authors**: Changyan Di, D. Proietti, I. E. Telatar +2
- **PDF**: https://ieeexplore.ieee.org/document/1003839
- **Abstract**: In this paper, we are concerned with the finite-length analysis of low-density parity-check (LDPC) codes when used over the binary erasure channel (BEC). The main result is an expression for the exact average bit and block erasure probability for a given regular ensemble of LDPC codes when decoded iteratively. We also give expressions for upper bounds on the average bit and block erasure probability for regular LDPC ensembles and the standard random ensemble under maximum-likelihood (ML) decoding. Finally, we present what we consider to be the most important open problems in this area.

## Bootstrap decoding of low-density parity-check codes

- **Status**: ✅
- **Reason**: Bootstrap 디코딩(신뢰도 낮은 비트 소거 후 재할당) + weighted bit-flipping 개선 — C 이식 가능 바이너리 LDPC 디코더 기법.
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1033202
- **Type**: journal
- **Published**: 2002
- **Authors**: A. Nouh, A. H. Banihashemi
- **PDF**: https://ieeexplore.ieee.org/document/1033202
- **Abstract**: An initial bootstrap step for the decoding of low-density parity-check (LDPC) codes is proposed. Decoding is initiated by first erasing a number of less reliable bits. New values and reliabilities are then assigned to erasure bits by passing messages from nonerasure bits through the reliable check equations. The bootstrap step is applied to the weighted bit-flipping algorithm to decode a number of LDPC codes. Large improvements in both performance and complexity are observed.

## Pseudorandom construction of low-density parity-check codes using linear congruential sequences

- **Status**: ✅
- **Reason**: 선형합동수열 기반 LDPC 그래프 구성(저장 없이 recursion으로 생성, girth>4) — E 코드설계 + HW 친화, 바이너리 LDPC 이식 가능.
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1032997
- **Type**: journal
- **Published**: 2002
- **Authors**: A. Prabhakar, K. Narayanan
- **PDF**: https://ieeexplore.ieee.org/document/1032997
- **Abstract**: We consider maximal-length linear congruential sequences generated using a simple recursion to generate the bipartite graph of a low-density parity-check (LDPC) code. The main advantage is that the graph structure of the codes (edge connections) can be generated using a recursion, rather than having to store the graph connections in memory, which facilitates hardware implementation of the decoder. For this class of codes, sufficient conditions on the recursion parameters are derived, such that regular LDPC codes can be constructed with no cycles of length four or less. Simulation results show that these codes provide almost the same performance of a constrained pseudorandom construction that explicitly avoids cycles of length less than or equal to four.

## Density evolution for two improved BP-Based decoding algorithms of LDPC codes

- **Status**: ✅
- **Reason**: normalized/offset BP-based 디코딩(min-sum 변형) 파라미터 최적화 density evolution 분석 — NAND 디코더에 직접 이식되는 핵심 기법(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1001666
- **Type**: journal
- **Published**: 2002
- **Authors**: J. Chen, M. P. C. Fossorier
- **PDF**: https://ieeexplore.ieee.org/document/1001666
- **Abstract**: In this letter, we analyze the performance of two improved belief propagation (BP) based decoding algorithms for LDPC codes, namely the normalized BP-based and the offset BP-based algorithms, by means of density evolution. The numerical calculations show that with one properly chosen parameter for each of these two improved BP-based algorithms, performances very close to that of the BP algorithm can be achieved. Simulation results for LDPC codes with code length moderately long validate the proposed optimization.

## Near optimum universal belief propagation based decoding of low-density parity check codes

- **Status**: ✅
- **Reason**: 정규화 기반 단순화 BP 디코더(C) — 채널 독립적 normalized min-sum류, 덧셈만으로 구현 가능해 NAND LDPC 디코더로 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:990903
- **Type**: journal
- **Published**: 2002
- **Authors**: Jinghu Chen, M. P. C. Fossorier
- **PDF**: https://ieeexplore.ieee.org/document/990903
- **Abstract**: In this paper, we propose a belief-propagation (BP)-based decoding algorithm which utilizes normalization to improve the accuracy of the soft values delivered by a previously proposed simplified BP-based algorithm. The normalization factors can be obtained not only by simulation, but also, importantly, theoretically. This new BP-based algorithm is much simpler to implement than BP decoding as it requires only additions of the normalized received values and is universal, i.e., the decoding is independent of the channel characteristics. Some simulation results are given, which show this new decoding approach can achieve an error performance very close to that of BP on the additive white Gaussian noise channel, especially for low-density parity check (LDPC) codes whose check sums have large weights. The principle of normalization can also be used to improve the performance of the max-log-MAP algorithm in turbo decoding, and some coding gain can be achieved if the code length is long enough.

## A 690-mW 1-Gb/s 1024-b, rate-1/2 low-density parity-check code decoder

- **Status**: ✅
- **Reason**: D: 1024b rate-1/2 LDPC 디코더의 병렬 VLSI 구현(저전력); 디지털 HW 아키텍처로 NAND ECC에 이식 가능
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:987093
- **Type**: journal
- **Published**: 2002
- **Authors**: A. J. Blanksby, C. J. Howland
- **PDF**: https://ieeexplore.ieee.org/document/987093
- **Abstract**: A 1024-b, rate-1/2, soft decision low-density parity-check (LDPC) code decoder has been implemented that matches the coding gain of equivalent turbo codes. The decoder features a parallel architecture that supports a maximum throughput of 1 Gb/s while performing 64 decoder iterations. The parallel architecture enables rapid convergence in the decoding algorithm to be translated into low decoder switching activity resulting in a power dissipation of only 690 mW from a 1.5-V supply.

## Iterative decoding and equalization for 2-D recording channels

- **Status**: ✅
- **Reason**: 스토리지(자기기록) LDPC + ISI 결합그래프 메시지패싱; 떼어낼 기법 약하나 애매하여 Phase3 재검토로 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1042177
- **Type**: journal
- **Published**: 2002
- **Authors**: N. Singla, J. A. O'Sullivan, R. S. Indeck +1
- **PDF**: https://ieeexplore.ieee.org/document/1042177
- **Abstract**: We study iterative decoding and equalization for information storage systems that have two-dimensional (2-D) intersymbol interference (ISI) during read-back. Two iterative schemes for 2-D equalization are introduced and evaluated. The first is based on minimum mean squared error (MMSE) estimation and the second is based on message passing on the combined graph of the ISI and the error correction code. Low-density parity-check codes are used for error correction. For the form of the ISI considered in our simulations the best performance is achieved by using the iterative decoding and MMSE equalization method.

## Kirkman systems and their application in perpendicular magnetic recording

- **Status**: ✅
- **Reason**: Kirkman 시스템 기반 신규 고율 구조적 바이너리 LDPC 구성 + 저복잡 HW 인코딩 — 코드설계(E)·HW(D) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1017760
- **Type**: journal
- **Published**: 2002
- **Authors**: B. Vasic, E. M. Kurtas, A. V. Kuznetsov
- **PDF**: https://ieeexplore.ieee.org/document/1017760
- **Abstract**: A novel class of a very high-rate low-density parity check codes is introduced, and investigated in the context of its application in a perpendicular magnetic recording system. New codes are well structured and, unlike random codes, can lead to a very low-complexity implementation. A systematic way of constructing codes is based on Kirkman systems. A hardware efficient encoding algorithm is proposed. The bit-error-rate characteristics are characterized by simulation of the soft iterative decoding in perpendicular magnetic read channel with different partial response targets and types of noise.

## High-performance iterative Viterbi algorithm for conventional serial concatenated codes

- **Status**: ✅
- **Reason**: 비-LDPC(serial concatenated/Viterbi)지만 small-loop 그래프를 min-sum류로 효율 디코딩하는 부호 비의존적 기법 — 바이너리 LDPC BP에 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1013124
- **Type**: journal
- **Published**: 2002
- **Authors**: Lei Wei
- **PDF**: https://ieeexplore.ieee.org/document/1013124
- **Abstract**: The Viterbi algorithm (1967) and conventional serial concatenated codes (CSCC) have been widely applied in digital communication systems over the last 30 years. We show that the Shannon capacity of additive white Gaussian noise (AWGN) channels can be approached by CSCCs and the iterative VA (IVA). We firstly study the algebraic properties of CSCCs. We then present the IVA to decode these codes. We also analyze the performance of the IVA and conclude that a better performance can be achieved if we replace the powerful block codes by some simple parity codes. One of the key results in this paper shows that by using a proper design for the decoding method, codes with small loops can be very efficiently decoded using a min-sum type algorithm. The numerical results show that the IVA can closely approach the Shannon sphere-packing lower bound and the Shannon limit. For block sizes ranging from 56 information bits to 11970 information bits, the IVA can perform to within about 1 dB of the Shannon sphere-packing lower bound at a block error rate of 10/sup -4/. We show that the IVA has a very low complexity and can be applied to many current standard systems, for example, the Qualcomm code-division multiple-access (CDMA) system and the NASA concatenated system, with very little modification or, for some cases, without any modification.

## Cycle-slip-detector-aided iterative timing recovery

- **Status**: ✅
- **Reason**: LDPC 반복 타이밍복구용 cycle-slip detector(채널 soft-output 활용) — 스토리지 LDPC 반복디코더 주변 기법, 애매하나 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1042165
- **Type**: journal
- **Published**: 2002
- **Authors**: Xiaowei Jin, A. Kavcic
- **PDF**: https://ieeexplore.ieee.org/document/1042165
- **Abstract**: The latest developments in low-density parity-check codes have shown performances very close to the channel capacity. However, in order to use these capacity-approaching codes in the magnetic recording channel, the cycle-slip problem in the synchronizer has to be solved. In this paper, we develop a cycle-slip detector (CSD) for the binary intersymbol interference channel that uses the channel soft-output information as its input. This CSD is then used in an iterative timing recovery scheme to eliminate cycle slips. Our simulation results show that utilizing the CSD improves the convergence speed of iterative timing recovery.

## Bounds for low-density parity-check codes over partial response channels

- **Status**: ✅
- **Reason**: 고율 바이너리 LDPC 성능 bound·finite-geometry LDPC — 순수 bound지만 유한기하 LDPC 구성 포함, 애매하여 살림(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1042171
- **Type**: journal
- **Published**: 2002
- **Authors**: Weijun Tan, R. M. Todd, J. R. Cruz
- **PDF**: https://ieeexplore.ieee.org/document/1042171
- **Abstract**: A bounding technique is used to evaluate the performance of high-rate low-density parity-check codes over partial response channels. Performance bounds for an ensemble of random codes, as well as for particular finite-geometry codes, are computed. Simulations are used to evaluate the bounds. The results show that the bounds appear to be valid for signal-to-noise ratios and code rates of interest in magnetic recording.

## A construction for low density parity check convolutional codes based on quasi-cyclic block codes

- **Status**: ✅
- **Reason**: QC 블록부호 기반 LDPC convolutional(SC-LDPC) 구성 — E 코드 설계. 바이너리 LDPC
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1023753
- **Type**: conference
- **Published**: 2002
- **Authors**: A. Sridharan, D. J. Costello, R. M. Tanner
- **PDF**: https://ieeexplore.ieee.org/document/1023753
- **Abstract**: A set of convolutional codes with low density parity check matrices is derived from a class of quasi-cyclic low density parity check block codes. Their performance when decoded using the belief propagation algorithm is investigated.
