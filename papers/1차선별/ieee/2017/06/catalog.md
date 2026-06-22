# IEEE Xplore — 2017-06 (1차선별 통과)


## Explicit APM-LDPC Codes With Girths 6, 8, and 10

- **Status**: ✅
- **Reason**: E: 새로운 명시적 바이너리 LDPC(APM-LDPC) 구성 + girth 6/8/10 하한, QC-LDPC 대비 개선 — 이식 가능 코드설계
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7888536
- **Type**: journal
- **Published**: June 2017
- **Authors**: Mohammad Gholami, Masoumeh Alinia
- **PDF**: https://ieeexplore.ieee.org/document/7888536
- **Abstract**: Recently, some attentions have been focused on a class of low-density parity-check codes from affine permutation matrices, called APM-LDPC codes, which have some advantages rather than quasi-cyclic low-density parity-check (QC-LDPC) codes in the minimum-distance, cycle distribution and error-rate performance. In this letter, first, some novel explicit constructions for exponent matrices of conventional APM-LDPC codes with girths 6, 8, and 10 are investigated, and for each given exponent matrix E corresponding to an APM-LDPC code with girth 2g , 3 ≤ g ≤ 5, a lower bound Q = Q(E,g) is obtained, such that APM-LDPC codes with exponent matrix E have girth at least 2g, for each (prime) APM size m ≥ Q. Then, regarding to reduce the lower bound, an improved bound IQ is obtained, which is significantly better than some lower bounds reported for QC-LDPC codes with explicit constructions. Simulation results show that the constructed APM-LDPC codes outperform QC-LDPC codes with the same girth.

## Retention-Aware Belief-Propagation Decoding for NAND Flash Memory

- **Status**: ✅
- **Reason**: A: NAND retention noise 대응 retention-aware BP 디코더, NAND LDPC ECC 직접
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7551127
- **Type**: journal
- **Published**: June 2017
- **Authors**: Chaudhry Adnan Aslam, Yong Liang Guan, Kui Cai
- **PDF**: https://ieeexplore.ieee.org/document/7551127
- **Abstract**: To recover decoding errors caused by data retention noise in nand Flash memory, a novel retention-aware belief-propagation (RA-BP) decoding scheme is proposed. The RA-BP scheme is based on two rounds of BP decoding in which the memory cell's charge-loss effect is systematically compensated. The most prominent feature of the proposed RA-BP scheme is that it recovers the retention-failure decoded data without performing additional memory sensing operations. Instead, the likely retention-failure memory cells are identified by using the available readback voltage signal and the decoded codeword bits. For all such likely retention-failure memory cells, the corresponding log-likelihood ratio information is modified in such a way as to reverse the effect of retention noise, and a second round of BP decoding is performed afresh. Through numerical simulations, it is shown that the proposed RA-BP decoding scheme can improve the error rate performance by more than three orders of magnitude and increase the retention time limit by up to 60% compared with a single round of BP decoding.

## Spatially coupled QC-LDPC for the tradeoff between MIMO BICM and BICM-ID schemes

- **Status**: ✅
- **Reason**: 유한길이 SC-QC-LDPC 코드설계+MET-DE 최적화(바이너리 BIAWGN). MIMO 응용이나 떼어낼 SC-LDPC 구성 기법 있어 E 포함
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7986240
- **Type**: conference
- **Published**: 7-9 June 2
- **Authors**: Yushu Zhang, Kewu Peng, Jian Song
- **PDF**: https://ieeexplore.ieee.org/document/7986240
- **Abstract**: The combination of multiple-input multiple-output (MIMO) and bit-interleaved coded modulation (BICM)/BICM with iterative demapping (BICM-ID) is one of the key technologies to meet the high-transmission-rate requirement of the next generation broadcasting systems. However, conventional low-density parity check (LDPC) coded MIMO BICM schemes always show poor performance with iterative demapping, and vice versa. In this paper, a subset of spatially coupled codes, finite-length spatially coupled (SC-) quasi-cyclic (QC-) LDPC code, is proposed and the universality of spatially coupled codes is utilized to achieve a good tradeoff between MIMO BICM and BICM-ID schemes. Due to the specific code structure of SC-QC-LDPC, the tool of multi-edge type density evolution (MET-DE) is employed for the performance analysis and code optimization. As an example, a finite-length SC-QC-LDPC code is optimized in binary-input additive white Gaussian noise channel, and then bit error rate simulations are carried out to verify the universality of the designed code in MIMO BICM and BICM-ID schemes.

## Superposition decoding scheme based on raptor-like LDPC code for signaling protection in broadcasting system

- **Status**: ✅
- **Reason**: raptor-like LDPC에서 고정 비트 위치 선택 알고리즘과 superposition 디코딩 — 코드설계/디코더 기법(C/E) 이식 가능성, 애매하면 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7986204
- **Type**: conference
- **Published**: 7-9 June 2
- **Authors**: Genning Zhang, Yin Xu, Dazhi He +1
- **PDF**: https://ieeexplore.ieee.org/document/7986204
- **Abstract**: This paper proposes a superposition decoding scheme based on raptor-like LDPC code for signaling protection in broadcasting system. The proposed scheme takes use of the fixed signaling bits to improve decoding performance significantly and lower the decoding threshold with a few frames sacrificed. Meanwhile, this paper also proposes a selection algorithm to select proper LDPC bits positions for fixed signaling which is better than random selection.

## Construction of rate compatible length scalable LDPC codes with low implementation complexity

- **Status**: ✅
- **Reason**: 공통 템플릿 행렬 기반 rate-compatible length-scalable QC-LDPC 구성법 + MET-DE — 바이너리 LDPC 코드설계 기법(E), HW 구현 용이
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7986228
- **Type**: conference
- **Published**: 7-9 June 2
- **Authors**: Zhangmei Chen, Kewu Peng, Yue Liu
- **PDF**: https://ieeexplore.ieee.org/document/7986228
- **Abstract**: Due to the rapid development of communication systems, a highly flexible scheme of multi-rate multi-length channel code is urgently required. In this paper, we propose a design method of highly flexible rate-compatible (RC) length-scalable (LS) low density parity check (LDPC) codes, which is based on the progressive extension idea of both information bit/node and parity check bit/node. According to our method, a family of RC-LS-LDPC codes with one common template matrix can be generated, which facilitates hardware implementation. With the aid of multi-edge type density evolution (MET-DE) analysis, the method can achieve near-capacity performance for each code rate and code length. The simulation results show that the designed codes with arbitrary rate and variable code length are within 0.30dB to 0.48dB compared with Shannon limit at bit error rate (BER) =2*10-9 under BI-AWGN channel.

## Improving LDPC decoding performance for ATSC 3.0 LDM profiles

- **Status**: ✅
- **Reason**: LDM 신호용 LLR PDF 공식 비교로 LDPC 디코딩 성능/구현 트레이드오프 분석 — LLR 양자화/계산 디코더 기법(C)으로 이식 가능, 애매하면 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7986136
- **Type**: conference
- **Published**: 7-9 June 2
- **Authors**: C. Regueiro, J. Barrueco, J. Montalban +2
- **PDF**: https://ieeexplore.ieee.org/document/7986136
- **Abstract**: ATSC 3.0 includes Layered Division Multiplexing (LDM) in addition to the traditional Time Division Multiplexing (TDM) technique in order to offer simultaneous stationary and mobile services. At the receiver side, Log-likelihood ratio (LLR) probability density functions are considered in the decoding process. The main objective of this paper is to analyze the performance of using different LLR PDF formulas for LDM signals in order to find the best trade-off between performance and implementation requirements, measuring the performance gain over TDM.

## A Rate-Compatible Low-Density Parity-Check Convolutional Coding Scheme Using Informed Dynamic Scheduling

- **Status**: ✅
- **Reason**: LDPC-CC에 informed dynamic scheduling 적용해 디코딩 수렴 가속+rate-compatible puncturing 구성, 이식 가능 디코더 스케줄링 기법(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8108393
- **Type**: conference
- **Published**: 4-7 June 2
- **Authors**: Huang-Chang Lee, Yung-Hsiang Su, Yeong-Luh Ueng
- **PDF**: https://ieeexplore.ieee.org/document/8108393
- **Abstract**: Low-density parity-check convolutional codes (LDPC-CCs) are generally decoded using sliding- window based message passing decoding. Based on the sliding-window decoding, an informed dynamic scheduling (IDS) for LDPC-CC is proposed in this work, where the decoding convergence can be significantly accelerated. Since the number of processors required for a satisfactory performance can be reduced, the decoder can be simplified. A set of rate-compatible (RC) puncturing patterns is also proposed and is used to construct RC LDPC-CCs for the performance evaluation of the proposed IDS. Although the proposed puncturing pattern cannot be optimized for individual code rate owing to the rate-compatible constraint, they can still provide a comparable error rate performance compared to the codes defined in the IEEE 802.16m standard. It is worth noting that these standard codes are not rate-compatible.

## Iterative Decoding for the Concatenated Code to Correct Nonbinary Insertions/Deletions

- **Status**: ✅
- **Reason**: LDPC+watermark 연접부호 반복디코딩에서 LDPC 외재정보 피드백 기법, BP 반복디코딩 메시지패싱 개선으로 이식 가능성(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8108389
- **Type**: conference
- **Published**: 4-7 June 2
- **Authors**: Yuan Liu, Weigang Chen
- **PDF**: https://ieeexplore.ieee.org/document/8108389
- **Abstract**: The lack of knowledge of the transmitted codeword limits the synchronization capability of the concatenated code,consisting of a low-density parity-check (LDPC) code and a watermark code, which is used to correct nonbinary insertion/deletion errors. In order to improve the synchronization error-locating capability of the watermark decoder and further decrease the error probability of the system, an iterative decoding method is presented in which the extrinsic soft information from the LDPC decoder is fed back into the watermark decoder. Simulation results show that, compared with the non- iterative counterpart, significant performance gain is achieved by employing the proposed decoding scheme.

## A protograph-based design of quasi-cyclic spatially coupled LDPC codes

- **Status**: ✅
- **Reason**: 프로토그래프 기반 QC-SC-LDPC 구성, 4-cycle 제거로 girth≥8·error floor 개선 — 카테고리 E
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8006816
- **Type**: conference
- **Published**: 25-30 June
- **Authors**: Li Chen, Shiyuan Mo, Daniel J. Costello +2
- **PDF**: https://ieeexplore.ieee.org/document/8006816
- **Abstract**: Spatially coupled (SC) low-density parity-check (LDPC) codes can achieve capacity approaching performance with low message recovery latency when using sliding window (SW) decoding. An SC-LDPC code constructed from a protograph can be generated by first coupling a chain of block protographs and then lifting the coupled protograph using permutation matrices. This paper introduces a systematic design of SC-LDPC codes to eliminate 4-cycles in the coupled photograph. Using a quasi-cyclic (QC) lifting, we obtain QC-SC-LDPC codes of girth at least eight. Coupling a chain of block protographs implies spreading edges from one protograph to the others. Our protograph-based design can be viewed as guiding the edge spreading and also the graph-lifting process. Simulation results show the design leads to improved decoding performance, particularly in the error floor, compared to random designs.

## Design of improved quasi-cyclic protograph-based Raptor-like LDPC codes for short block-lengths

- **Status**: ✅
- **Reason**: 짧은 블록 QC PBRL LDPC 구성, 최소거리 상한 최대화로 error floor 개선 — 바이너리 QC-LDPC 코드설계(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8006720
- **Type**: conference
- **Published**: 25-30 June
- **Authors**: Sudarsan V. S. Ranganathan, Dariush Divsalar, Richard D. Wesel
- **PDF**: https://ieeexplore.ieee.org/document/8006720
- **Abstract**: Protograph-based Raptor-like low-density parity-check codes (PBRL codes) are a recently proposed family of easily encodable and decodable rate-compatible LDPC (RC-LDPC) codes. These codes have an excellent iterative decoding threshold and performance across all design rates. PBRL codes designed thus far, for both long and short block-lengths, have been based on optimizing the iterative decoding threshold of the protograph of the RC code family at various design rates. In this work, we propose a design method to obtain better quasi-cyclic (QC) RC-LDPC codes with PBRL structure for short block-lengths (of a few hundred bits). We achieve this by maximizing an upper bound on the minimum distance of any QC-LDPC code that can be obtained from the protograph of a PBRL ensemble. The obtained codes outperform the original PBRL codes at short block-lengths by significantly improving the error floor behavior at all design rates. Furthermore, we identify a reduction in complexity of the design procedure, facilitated by the general structure of a PBRL ensemble.

## Characterization and efficient exhaustive search algorithm for elementary trapping sets of irregular LDPC codes

- **Status**: ✅
- **Reason**: irregular LDPC elementary trapping set 특성화·exhaustive 탐색 알고리즘 — error floor 코드설계(E), 바이너리 LDPC에 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8006717
- **Type**: conference
- **Published**: 25-30 June
- **Authors**: Yoones Hashemi, Amir H. Banihashemi
- **PDF**: https://ieeexplore.ieee.org/document/8006717
- **Abstract**: In this paper, we propose a characterization of elementary trapping sets (ETSs) for irregular low-density parity-check (LDPC) codes. These sets are known to be the main culprits in the error floor region of such codes. The proposed characterization is based on a hierarchical graphical representation of ETSs, starting from simple cycles of the graph, or from single variable nodes, and involves three simple expansion techniques: depth-one tree (dot), path and lollipop, thus, the terminology dpl characterization. The proposed dpl characterization corresponds to an efficient search algorithm, that, for a given irregular LDPC code, can find all the instances of (a, b) ETSs with size a and with the number of unsatisfied check nodes b, within any range of interest a ≤ amax and b ≤ bmax, exhaustively. Simulation results are presented to show the versatility of the search algorithm, and to demonstrate that, compared to the literature, significant improvement in search speed can be obtained.

## Rate-loss reduction of SC-LDPC codes by optimizing reliable variable nodes via expected graph evolution

- **Status**: ✅
- **Reason**: SC-LDPC 부호 설계(신뢰변수노드 차수분포 최적화로 rate-loss 감소)는 바이너리 LDPC 코드설계 기법(E)으로 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8007066
- **Type**: conference
- **Published**: 25-30 June
- **Authors**: Heeyoul Kwak, Jaewha Kim, Jong-Seon
- **PDF**: https://ieeexplore.ieee.org/document/8007066
- **Abstract**: The outstanding decoding performance of spatially-coupled low-density parity-check (SC-LDPC) codes comes from wave-like propagation of reliable messages. The reliable messages are triggered by shortened (known) variable nodes in some consecutive reliable positions. However, at the cost of the improvement, shortened variable nodes cause rate-loss of SC-LDPC codes. To reduce the rate-loss, additional variable nodes (so called reliable variable nodes) can be added to the reliable positions instead of shortened variable nodes. Density evolution (DE) is an efficient method to design degree distribution of the reliable variable nodes. However, degree distributions obtained by DE show degraded performance in finite-length code performance. In this paper, we generalize the expected graph evolution and use the analysis tool in optimizing degree distribution which shows the minimum rate-loss without finite-length performance degradation. From the well-designed degree distribution, rate-loss reduction by 60% can be achieved without finite-length performance degradation.

## Non-uniformly coupled LDPC codes: Better thresholds, smaller rate-loss, and less complexity

- **Status**: ✅
- **Reason**: 비균일 결합 SC-LDPC 구성으로 error floor·threshold 개선 + 윈도우 디코더 — 바이너리 코드설계(E) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8006553
- **Type**: conference
- **Published**: 25-30 June
- **Authors**: Laurent Schmalen, Vahid Aref, Fanny Jardel
- **PDF**: https://ieeexplore.ieee.org/document/8006553
- **Abstract**: We consider spatially coupled low-density parity-check codes with finite smoothing parameters. A finite smoothing parameter is important for designing practical codes that are decoded using low-complexity windowed decoders. By optimizing the amount of coupling between spatial positions, we show that we can construct codes with excellent thresholds and small rate loss, even with the lowest possible smoothing parameter and large variable node degrees, which are required for low error floors. We also establish that the decoding convergence speed is faster with non-uniformly coupled codes, which we verify by density evolution of windowed decoding with a finite number of iterations. We also show that by only slightly increasing the smoothing parameter, practical codes with potentially low error floors and thresholds close to capacity can be constructed. Finally, we give some indications on protograph designs.

## Time-invariant LDPC convolutional codes

- **Status**: ✅
- **Reason**: 시불변 LDPC convolutional 코드 구성, 구현 관점 강조 — 바이너리 코드설계(E) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8006551
- **Type**: conference
- **Published**: 25-30 June
- **Authors**: Dimitris Achlioptas, Hamed Hassani, Wei Liu +1
- **PDF**: https://ieeexplore.ieee.org/document/8006551
- **Abstract**: Spatially coupled codes have been shown to achieve the capacity for a large class of channels universally. Many variants of such codes have been introduced to date. We discuss a further such variant that is particularly simple and is determined by a very small number of parameters. More precisely, we consider and ensemble of time-invariant low-density parity-check convolutional codes with very large constraint lengths. We show via simulations that, despite their extreme simplicity, such codes still show the threshold saturation behavior known from the spatially coupled codes discussed in the literature. Further, we show how the size of the typical minimum stopping set is related to basic parameters of the code. Due to their simplicity and good performance, these codes might be attractive from an implementation perspective.

## Edge spreading design of high rate array-based SC-LDPC codes

- **Status**: ✅
- **Reason**: array-based SC-LDPC의 absorbing set 스펙트럼·최소거리 공동최적화 edge spreading은 바이너리 코드설계/error floor 기법(E)으로 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8007068
- **Type**: conference
- **Published**: 25-30 June
- **Authors**: David G. M. Mitchell, Eirik Rosnes
- **PDF**: https://ieeexplore.ieee.org/document/8007068
- **Abstract**: Absorbing sets (ASs) are combinatorially defined objects existing in the Tanner graph of a low-density parity-check (LDPC) code that have been shown to cause failures in the iterative message-passing decoder when transmission occurs over the additive white Gaussian noise channel. In this paper, we propose an edge spreading approach to construct high rate array-based spatially-coupled LDPC codes by jointly optimizing the AS spectrum and the minimum distance. By considering general edge spreadings and by considering a larger memory, we show that strictly better codes can be constructed, both in terms of achievable minimum distance for small-to-moderate block lengths and in terms of the number of small ASs.

## Message alignment for discrete LDPC decoders with quadrature amplitude modulation

- **Status**: ✅
- **Reason**: Information Bottleneck 기반 이산 LDPC 디코더의 message alignment 기법, LLR 양자화·룩업 디코더로 NAND LDPC에 직접 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8007065
- **Type**: conference
- **Published**: 25-30 June
- **Authors**: Jan Lewandowsky, Maximilian Stark, Gerhard Bauch
- **PDF**: https://ieeexplore.ieee.org/document/8007065
- **Abstract**: Recent works describe the design of discrete decoders for low-density parity-check codes by application of mutual information maximizing clustering algorithms in discrete density evolution. In the resulting discrete message passing decoders only integers are exchanged and node operations become simple lookup operations. Earlier works only describe discrete decoders for binary modulation schemes. This paper presents a new technique called message alignment which enables to design discrete decoders for higher-order modulation schemes. First, we design a channel output quantizer for quadrature amplitude modulation with the Information Bottleneck method. The quantizer attempts to preserve the relevant information on the modulation symbols. Afterwards, we illustrate that the assignment of several bits to one modulation symbol does not allow straightforward decoder design with the available discrete density evolution technique. The proposed message alignment solves this problem. The resulting discrete decoder is compared with state-of-the-art decoders using bit error rate simulations.

## A novel combinatorial framework to construct spatially-coupled codes: Minimum overlap partitioning

- **Status**: ✅
- **Reason**: circulant 기반 SC-LDPC의 minimum overlap partitioning 구성·error-floor 객체 열거 — 카테고리 E
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8006818
- **Type**: conference
- **Published**: 25-30 June
- **Authors**: Homa Esfahanizadeh, Ahmed Hareedy, Lara Dolecek
- **PDF**: https://ieeexplore.ieee.org/document/8006818
- **Abstract**: Spatially-coupled (SC) codes are a family of graph-based codes that have attracted significant attention thanks to their capacity approaching performance. An SC code is constructed by partitioning an underlying block code into a number of components, and coupling their copies together. The number of components is determined by the memory parameter. In this paper, we study a finite length construction for the circulant-based SC codes. We introduce a new partitioning scheme, which we call minimum overlap partitioning, that outperforms previous methods. We also present a general approach for the enumeration of problematic objects in the error-floor regime that can be applied to any circulant-based SC code and to a variety of partitioning schemes. Compared to the uncoupled block codes, an SC code constructed by the new approach has more than 1.5 and 3 orders of magnitude performance improvement for the memory 1 and 2, respectively. Additionally, it outperforms the existing method of partitioning via cutting vectors by at least half an order of magnitude; this performance advantage becomes more pronounced for SC codes with higher memories.

## Neural offset min-sum decoding

- **Status**: ✅
- **Reason**: 신경망 기반 offset min-sum 디코더(곱셈 없는 학습형 offset), 바이너리 LDPC BP에 그대로 이식 가능 — 카테고리 C
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8006751
- **Type**: conference
- **Published**: 25-30 June
- **Authors**: Loren Lugosch, Warren J. Gross
- **PDF**: https://ieeexplore.ieee.org/document/8006751
- **Abstract**: Recently, it was shown that if multiplicative weights are assigned to the edges of a Tanner graph used in belief propagation decoding, it is possible to use deep learning techniques to find values for the weights which improve the error-correction performance of the decoder. Unfortunately, this approach requires many multiplications, which are generally expensive operations. In this paper, we suggest a more hardware-friendly approach in which offset min-sum decoding is augmented with learnable offset parameters. Our method uses no multiplications and has a parameter count less than half that of the multiplicative algorithm. This both speeds up training and provides a feasible path to hardware architectures. After describing our method, we compare the performance of the two neural decoding algorithms and show that our method achieves error-correction performance within 0.1 dB of the multiplicative approach and as much as 1 dB better than traditional belief propagation for the codes under consideration.

## An iterative soft-decision decoding algorithm for Reed-Solomon codes

- **Status**: ✅
- **Reason**: 패리티검사행렬 적응+informed dynamic scheduling 반복 소프트디코딩, 동적 스케줄링 메시지패싱 기법이 LDPC BP에 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8007035
- **Type**: conference
- **Published**: 25-30 June
- **Authors**: Huang-Chang Lee, Jyun-Han Wu, Chung-Hsuan Wang +1
- **PDF**: https://ieeexplore.ieee.org/document/8007035
- **Abstract**: This paper proposes an iterative soft-decision decoding algorithm for Reed-Solomon (RS) codes. The proposed decoding algorithm combines the concepts of adapting the parity-check matrix and informed dynamic scheduling decoding. The parity-check matrix is re-arranged before each iteration, where the systematic part is mapped to the least reliable bits, consequently reducing their influence on the other bits. Using dynamic scheduling, the more important decoding messages are updated to these least reliable bits, meaning that the majority of the error bits with low reliability can be corrected. When the proposed integrated decoding is applied to (255, 239) RS code, the difference between its frame error rate performance (FER) and the maximum-likelihood (ML) bound can be reduced to 0.8 dB, and a gain of about 0.1 dB is achieved compared to all the previously recorded soft-decision decoding for RS codes.

## Complexity-optimized concatenated LDGM-staircase codes

- **Status**: ✅
- **Reason**: LDGM-staircase 연접부호의 LDGM 앙상블 복잡도 최적화 설계(엣지수·반복수 기반), 바이너리 LDPC 코드설계 이식 가능 — 애매하나 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8006817
- **Type**: conference
- **Published**: 25-30 June
- **Authors**: Lei M. Zhang, Frank R. Kschischang
- **PDF**: https://ieeexplore.ieee.org/document/8006817
- **Abstract**: A concatenated soft-decision channel coding scheme consisting of an inner LDGM code and an outer staircase code is proposed. The soft-decision LDGM code is used for error reduction while the majority of bit errors are corrected by the low complexity hard-decision staircase code. Decoding complexity of the concatenated code is quantified by a score based on the number of edges in the LDGM code Tanner graph, the number of decoding iterations, and the number of staircase code decoding operations. The inner LDGM ensemble is designed by solving an optimization problem, which minimizes the product of the average node degree and an estimate of the required number of decoding iterations. A search procedure is used to find the inner and outer code pair with lowest complexity. The design procedure results in a Pareto-frontier characterization of the trade-off between net coding-gain and complexity for the concatenated code. Simulations of code designs at rate 5/6 show that the proposed scheme achieves net coding-gains equivalent to existing soft-decision codes, with up to 57% reduction in complexity.

## Analysis and implementation of resource efficient probabilistic Gallager B LDPC decoder

- **Status**: ✅
- **Reason**: 새 확률적 자극함수 PGaB 하드디시전 디코더 + FPGA HW 구현 비교, 이식 가능(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8010173
- **Type**: conference
- **Published**: 25-28 June
- **Authors**: Burak Ünal, Fakhreddine Ghaffari, Ali Akoglu +2
- **PDF**: https://ieeexplore.ieee.org/document/8010173
- **Abstract**: Low-Density-Parity-Check (LDPC) codes have gained popularity in communication systems and standards due to their capacity-approaching error-correction performance. In this paper, we first expose the tradeoff between decoding performance and hardware performance across three LDPC hard-decision decoding algorithms: Gallager B (GaB), Gradient Descent Bit Flipping (GDBF), and Probabilistic Gradient Descent Bit Flipping (PGDBF). We show that GaB architecture delivers the best throughput while using fewest Field Programmable Gate Array (FPGA) resources, however performs the worst in terms of decoding performance. We then modify the GaB architecture, introduce a new Probabilistic stimulation function (PGaB), and achieve dramatic decoding performance improvement over the GaB, exceeding the performance of GDBF, without sacrificing its superior maximum operating frequency.

## Design of LDPC Fast Encoding Based on Dynamic Memory Structure of Linked List Queue

- **Status**: ✅
- **Reason**: QC-LDPC 고속 인코더 FPGA/배럴시프터 HW 구조 제안 — 이식 가능 HW 아키텍처(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:8121766
- **Type**: conference
- **Published**: 21-23 June
- **Authors**: Bo Chen, Shiming Li, Xiuli Du +1
- **PDF**: https://ieeexplore.ieee.org/document/8121766
- **Abstract**: The existing LDPC encoder exists the problem of high computing complexity and much resources consumption, therefore, a strategy of LDPC fast encoding based on dynamic memory structure of linked list queue is proposed in this paper. Specifically, this strategy simplifies the design of encoder by making full use of the characteristics of the parity check matrix structure and sparsity. On the basis of this, the hardware structure of the quasi loop and the matrix vector multiplier of the barrel shifter are designed. Moreover, the FPGA implementation of the LDPC encoder is completed. Finally, we use Verilog language to implement the algorithm and XILINX ISE 14.7 as the functional simulation tool to simulate the timing of different code rate. And simulation results show that this method can achieve a linear relationship between the encoding complexity and the code length, effectively improve the encoding speed and reduce the amount of logic resources.

## A novel IRA-like codes construction method based on cyclic matrix permutation

- **Status**: ✅
- **Reason**: 순환행렬 치환 기반 IRA-like QC-LDPC 신규 구성으로 복잡도/error floor 개선(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7984686
- **Type**: conference
- **Published**: 2-4 June 2
- **Authors**: Wei Wang, Yingxiang Liu, Xiaomei Tang +2
- **PDF**: https://ieeexplore.ieee.org/document/7984686
- **Abstract**: Due to the structure limitation of navigation message, the channel coding used by the satellite navigation system should have as high a coding gain as possible under short code lengths. At the same time, in order to reduce the cost of the receiver, the channel coding suitable for the navigation system should have the lowest complexity for coding and decoding. A well-designed structured LDPC code can reduce the complexity of the codec significantly without the loss of performance. In this paper, a method based on cyclic matrix permutation is proposed to improve IRA-like codes, which is combined Irregular Repeat Accumulation Codes (IRA) with Quasi-Cyclic LDPC codes. Simulation results show our method has good iterative decoding performance in decreasing bit error rate and greatly reducing the number of iterations required for decoding as well as error platform.

## Reducing LDPC soft sensing latency by lightweight data refresh for flash read performance improvement

- **Status**: ✅
- **Reason**: NAND 플래시 LDPC soft-sensing 지연 개선(LDR refresh), 플래시 ECC 직접 → A
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8060396
- **Type**: conference
- **Published**: 18-22 June
- **Authors**: Yajuan Du, Qiao Li, Liang Shi +3
- **PDF**: https://ieeexplore.ieee.org/document/8060396
- **Abstract**: In order to relieve reliability problem caused by technology scaling, LDPC codes have been widely applied in flash memories to provide high error correction capability. However, LDPC read performance slowdown along with data retention largely weakens the access speed advantage of flash memories. This paper considers to apply the concept of refresh, that were used for flash lifetime improvement, to optimize flash read performance. Exploiting data read characteristics, this paper proposes LDR, a lightweight data refresh method, that aggressively corrects errors in read-hot pages with long read latency and reprograms error-free data into new pages. Experimental results show that LDR can achieve 29% read performance improvement with only 0.2% extra P/E cycles on average, which causes negligible overhead on flash lifetime.

## 2-dimensional minimum fast-searching design approach of LDPC decoder architecture for IEEE 802.11n/ac/ax applications

- **Status**: ✅
- **Reason**: LDPC 디코더의 2D 최소/차순위최소 고속탐색 HW 아키텍처(critical-path 개선) — 이식 가능 HW(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:7991024
- **Type**: conference
- **Published**: 12-14 June
- **Authors**: Xin-Yu Shih, Yu-Chun Chen
- **PDF**: https://ieeexplore.ieee.org/document/7991024
- **Abstract**: This work proposes a systematic design approach to perform minimum and second minimum fast-searching in 2-dimensional xy-planes. This fast-searching approach can extremely improve the calculating timing in LDPC decoder architecture, especially for high row weights defined in IEEE 802.11n/ac/ax SPEC. In a design example with row weight of 22, our developed approach only requires about 42.9% of critical-path timing under 12.2% hardware overhead with respect to often-used binary-tree approach. This approach also extends to other various high row weights for enhancing critical-path timing performance.

## On the design of good LDPC codes with joint genetic algorithm and linear programming optimization

- **Status**: ✅
- **Reason**: GA+LP로 LDPC 변수/체크노드 차수분포 최적화(코드설계 E) — 이식 가능한 바이너리 LDPC 구성 기법
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7994822
- **Type**: conference
- **Published**: 11-14 June
- **Authors**: Ahmadreza Amirzadeh, Mohamed Haj Taieb, Jean-Yves Chouinard
- **PDF**: https://ieeexplore.ieee.org/document/7994822
- **Abstract**: In communication systems, the transmitted data is corrupted by channel perturbations, such as noise and fading, which affect the reliability of the received data. Error correction codes are employed to mitigate channel perturbations. However, design and implementation of good and efficient error correction codes remains an open problem. In this paper, Low Density Parity Check (LDPC) codes are considered as they provide a reasonable trade-off between computational complexity and reliability. Good LDPC codes should ideally provide low complexity, close to capacity acheivable transmission rate, high coding threshold, and high decoding stability. In this paper, we investigate a joint LDPC code optimization algorithm using Genetic Algorithm (GA) and Linear Programming (LP) to determine the variable nodes and check nodes degrees distributions. EXIT chart analysis and Frame Error Rate (FER) performance are used to validate the proposed method.
