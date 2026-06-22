# IEEE Xplore — 2009-10 (1차선별 통과)


## Comments on successive relaxation for decoding of LDPC codes

- **Status**: ✅
- **Reason**: successive relaxation을 BP/min-sum에 적용한 LLR/LR 도메인 분석, SR-MS-LLR이 표준 MS/BP 대비 0.6/0.3dB 개선 — 카테고리 C 이식 가능 디코더 변형
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5288477
- **Type**: journal
- **Published**: October 20
- **Authors**: Hua Xiao, Amir H. Banihashemi
- **PDF**: https://ieeexplore.ieee.org/document/5288477
- **Abstract**: The application of successive relaxation (SR) to the fixed-point problem associated with the iterative decoding of low-density parity-check (LDPC) codes was proposed by Hemati et al.. The simulation results presented by Hemati et al. for the SR version of belief propagation (BP) in the likelihood ratio (LR) domain and that of min-sum (MS) in the log-likelihood ratio (LLR) domain are based on the assumption of all-zero codeword transmission. This assumption however results in erroneous error rates when SR is applied in the LR domain. Here, we correct the simulation results reported by Hemati et al. for SR-BP in the LR domain. Furthermore, we investigate the performance of SR-BP and SR-MS in the LLR and LR domains, respectively. The results for a binary input additive white Gaussian noise (BIAWGN) channel show that for both BP and MS, the application of SR in the two domains of LR and LLR results in different error correcting performance. In particular, for the tested codes, it is shown that among the four algorithms, SR-MS-LLR has the best performance. It outperforms standard MS and BP by up to about 0.6 dB and 0.3 dB, respectively, offering an attractive solution in terms of performance/complexity tradeoff.

## A lattice-based systematic recursive construction of quasi-cyclic LDPC codes

- **Status**: ✅
- **Reason**: lattice 기반 재귀적 QC-LDPC 구성법, girth 6 보장 신규 코드설계 — 카테고리 E 바이너리 LDPC 구성
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5288480
- **Type**: journal
- **Published**: October 20
- **Authors**: M. Esmaeili, M. H. Tadayon
- **PDF**: https://ieeexplore.ieee.org/document/5288480
- **Abstract**: This paper presents a low-complexity recursive and systematic method to construct good well-structured low-density parity-check (LDPC) codes. The method is based on a recursive application of a partial Kronecker product operation on a given gamma x q, q ges 3 a prime, integer lattice L(gamma x q). The (n - 1)- fold product of L(gamma x q) by itself, denoted Ln(gamma x q), represents a regular quasi-cyclic (QC) LDPC code, denoted (see PDF), of high rate and girth 6. The minimum distance of (see PDF) is equal to that of the core code (see PDF) introduced by L(gamma x q). The support of the minimum weight codewords in (see PDF) are characterized by the support of the same type of codewords in (see PDF). From performance perspective the constructed codes compete with the pseudorandom LDPC codes.

## Highly Parallel FPGA Emulation for LDPC Error Floor Characterization in Perpendicular Magnetic Recording Channel

- **Status**: ✅
- **Reason**: 고병렬 FPGA 에뮬레이션으로 LDPC error floor 특성화 가속; HW 평가 아키텍처 이식 가능(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:5257218
- **Type**: journal
- **Published**: Oct. 2009
- **Authors**: Yu Cai, Seungjune Jeon, Ken Mai +1
- **PDF**: https://ieeexplore.ieee.org/document/5257218
- **Abstract**: Low-density parity-check (LDPC) codes offer a promising error correction approach for high-density magnetic recording systems due to their near-Shannon limit error-correcting performance. However, evaluation of LDPC codes at the extremely low bit error rates (BER) required by hard disk drive systems, typically around $10^{-12}$  to $10^{- 15}$ , cannot be carried out on high-performance workstations using conventional Monte Carlo techniques in a tractable amount of time. Even field-programmable gate array (FPGA) emulation platforms take a few weeks to reach BER between $10^{-11}$ and $10^{-12}$. Thus, we implemented a highly parallel FPGA processing cluster to emulate a perpendicular magnetic recording channel, which enabled us to accelerate the emulation by $> 100 \times$ over the fastest reported emulation. This increased throughput enabled us to characterize the performance of LDPC code BER down to near  $10^{- 14}$ and investigate its error floor.

## Construction of Quasi-Cyclic LDPC Codes and the Performance on the PR4-Equalized MRC Channel

- **Status**: ✅
- **Reason**: PEG 기반 QC-LDPC 구성에 unreliable factor 도입, short cycle 제거·low error-floor·HW-friendly 코드설계(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5257171
- **Type**: journal
- **Published**: Oct. 2009
- **Authors**: Xingcheng Liu, Weibo Zhang, Zhiyong Fan
- **PDF**: https://ieeexplore.ieee.org/document/5257171
- **Abstract**: In this paper, we constructed a type of parity-check matrices of QC-LDPC codes based on the progressive edge-growth (PEG) algorithm with suggested unreliable factors incorporated. The proposed algorithm can eliminate short cycles efficiently and gain low error-floors. With this method, we can avoid the unreliable information transferred in decoding as far as possible. The proposed QC-LDPC codes are hardware-friendly due to the benefit from the quasi-cyclic structure of such codes. Simulation results demonstrate that the codes constructed with the proposed algorithm have better performance than those constructed with the PEG algorithm over the additive white Gaussian noise (AWGN) channel and the PR4-equalized magnetic recording channel (MRC).

## A good puncturing scheme for rate compatible low-density parity-check codes

- **Status**: ✅
- **Reason**: rate-compatible LDPC puncturing 패턴 설계 신규 알고리즘 — 바이너리 코드설계 기법(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6388389
- **Type**: journal
- **Published**: Oct. 2009
- **Authors**: Sunghoon Choi, Sungroh Yoon, Wonjin Sung +2
- **PDF**: https://ieeexplore.ieee.org/document/6388389
- **Abstract**: We consider the challenges of finding good puncturing patterns for rate-compatible low-density parity-check code (LDPC) codes over additive white Gaussian noise (AWGN) channels. Puncturing is a scheme to obtain a series of higher rate codes from a lower rate mother code. It is widely used in channel coding but it causes performance is lost compared to non-punctured LDPC codes at the same rate. Previous work, considered the role of survived check nodes in puncturing patterns. Limitations, such as single survived check node assumption and simulation-based verification, were examined. This paper analyzes the performance according to the role of multiple survived check nodes and multiple dead check nodes. Based on these analyses, we propose new algorithm to find a good puncturing pattern for LDPC codes over AWGN channels.

## Multistep linear programming approaches for decoding low-density parity-check codes

- **Status**: ✅
- **Reason**: LP 디코딩 개선(MLP, 적응적 제약 추가, ML certificate) — 바이너리 LDPC 이식 가능 디코더 알고리즘(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6076252
- **Type**: journal
- **Published**: Oct. 2009
- **Authors**: Haiyang Liu, Lianrong Ma, Jie Chen
- **PDF**: https://ieeexplore.ieee.org/document/6076252
- **Abstract**: The problem of improving the performance of linear programming (LP) decoding of low-density parity-check (LDPC) codes is considered in this paper. A multistep linear programming (MLP) algorithm was developed for decoding LDPC codes that includes a slight increase in computational complexity. The MLP decoder adaptively adds new constraints which are compatible with a selected check node to refine the results when an error is reported by the original LP decoder. The MLP decoder result is shown to have the maximum-likelihood (ML) certificate property. Simulations with moderate block length LOpe codes suggest that the M LP decoder gives better performance than both the original LP decoder and the conventional sum-product (SP) decoder.

## A Low-Complexity Hybrid LDPC Code Encoder for IEEE 802.3an (10GBase-T) Ethernet

- **Status**: ✅
- **Reason**: 바이너리 LDPC 저복잡도 하이브리드 인코더 HW 아키텍처(면적/ROM/전력 절감), NAND 이식 가능(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:4915776
- **Type**: journal
- **Published**: Oct. 2009
- **Authors**: Aaron E. Cohen, Keshab K. Parhi
- **PDF**: https://ieeexplore.ieee.org/document/4915776
- **Abstract**: This paper presents a novel hybrid encoding method for encoding of low-density parity-check (LDPC) codes. The design approach is applied to design 10-Gigabit Ethernet transceivers over copper cables. For a specified encoding speed, the proposed method requires substantially lower complexity in terms of area and storage. Furthermore, this method is generic and can be adapted easily for other LDPC codes. One major advantage of this design is that it does not require column swapping and it maintains compatibility with optimized LDPC decoders. For a 10-Gigabit Ethernet transceiver which is compliant with the IEEE 802.3an standard, the proposed sequential (5-Parallel) hybrid architecture has the following implementation properties: critical path: $(\log_{2}(324)+1){\rm T}_{\rm xor}+{\rm T}_{\rm and}$, number of xor gates: 11 056, number of and gates: 1620, and ROM storage: 104 976 bits (which can be minimized to 52 488 bits using additional hardware). This method achieves comparable critical path, and requires 74% gate area, 10% ROM storage as compared with a similar 10-Gigabit sequential (5-Parallel) LDPC encoder design using only the G matrix multiplication method. Additionally the proposed method accesses fewer bits per cycle than the G matrix method which reduces power consumption by about 82%.

## A Generalized Data Detection Scheme Using Hyperplane for Magnetic Recording Channels With Pattern-Dependent Noise

- **Status**: ✅
- **Reason**: SVM 기반 LLR 재조정으로 LDPC 디코더 반복수 절반 감소; LLR 전처리/디코더 가속 기법 이식 가능(C), 애매하면 in
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5257152
- **Type**: journal
- **Published**: Oct. 2009
- **Authors**: Seiichi Mita, Vo Tam Van
- **PDF**: https://ieeexplore.ieee.org/document/5257152
- **Abstract**: We propose a novel data-detection scheme using support vector machine techniques in the presence of pattern-dependent noise on magnetic recording channels. First, the log-likelihood ratios (LLRs) of data series were generated using the Bahl-Cocke-Jelinek-Raviv algorithm. Second, these LLRs were mapped to a 3-D space, and hyperplanes for data discrimination were generated using the radial-basis-function kernel. Third, the LLR of each bit was rescaled on the basis of the distance from the hyperplanes and then fed to an LDPC decoder. We evaluated the performance of the proposed method by retrieving a real data series from a perpendicular magnetic recording channel, and obtained a bit-error rate of approximately 10-3. For projective geometry-low-density parity-check codes with a code rate of 0.93, the proposed method can reduce the iteration number for a sum product algorithm using conventional LLRs by approximately half.

## Conflict resolution for pipelined layered LDPC decoders

- **Status**: ✅
- **Reason**: 파이프라인 layered LDPC 디코더 메모리 접근 충돌 해소 스케줄링 기법(D), NAND HW에 이식 가능
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:5336255
- **Type**: conference
- **Published**: 7-9 Oct. 2
- **Authors**: Cedric Marchand, Jean-Baptiste Dore, Laura Conde-Canencia +1
- **PDF**: https://ieeexplore.ieee.org/document/5336255
- **Abstract**: Many of the current LDPC implementations of DVB-S2, T2 or WiMAX standard use the so-called layered architecture combined with pipeline. However, the pipeline process may introduce memory access conflicts. The resolution of these conflicts requires careful scheduling combined with dedicated hardware and/or idle cycle insertion. In this paper, based on the DVB-T2 example, we explain explicitly how the scheduling can solve most of the pipeline conflicts. The two contributions of the paper are 1) how to split the matrix to relax the pipeline conflicts at a cost of a reduced maximum available parallelism 2) how to project the problem of the research of an efficient scheduling to the well-known “Travelling Salesman Problem” and use a genetic algorithm to solve it.

## A Channel-Adaptive Early Termination strategy for LDPC decoders

- **Status**: ✅
- **Reason**: Channel-Adaptive Early Termination 디코더 조기종료 전략(C), NAND LDPC 디코딩 지연 감소에 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5336256
- **Type**: conference
- **Published**: 7-9 Oct. 2
- **Authors**: Yu-Hsin Chen, Yi-Ju Chen, Xin-Yu Shih +1
- **PDF**: https://ieeexplore.ieee.org/document/5336256
- **Abstract**: In this paper, we propose a new Channel-Adaptive Early Termination (CAET) strategy to early stop Low-Density Parity-Check (LDPC) decoders. Our method checks the sign-changing rate of the log-likelihood ratios, and is able to perform the early termination under all SNR ranges with simple methodology. The average decoding latency can be decreased from the preset number of 8 to 6.73 iterations with negligible performance degradation. In addition, we create the BER Performance Loss Ratio (BPLR) index to evaluate the performance loss of different ET criteria. Compared to the hard-decision-aided criterion, our CAET strategy reduces the decoding iterations effectively and improves the BPLR by 76.6%.

## An improved min-sum based column-layered decoding algorithm for LDPC codes

- **Status**: ✅
- **Reason**: min-sum column-layered 디코딩의 비교연산 감축 신기법(C)—바이너리 LDPC 디코더 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5336258
- **Type**: conference
- **Published**: 7-9 Oct. 2
- **Authors**: Lin Jun, Sha Jin, Zhongfeng Wang +1
- **PDF**: https://ieeexplore.ieee.org/document/5336258
- **Abstract**: Low-density parity-check code is a kind of near-optimal error correction code. Developing a highly efficient decoding algorithm is the main challenge of the implementation of LDPC code. In this paper, based on the min-sum column-layered decoding algorithm, a new selective computation technique is proposed to reduce the number of comparisons. With the presented decoding algorithm, the total number of floating number comparisons can be reduced dramatically (range from 81% to 91%) at the cost of negligible hardware overhead. Simulation results show that the decoding performance and iteration times are almost the same as the original column-layered decoding algorithm.

## Massively parallel implementation of cyclic LDPC codes on a general purpose graphics processing unit

- **Status**: ✅
- **Reason**: QC/cyclic LDPC 패리티행렬 압축 통한 병렬 GPU 디코딩 기법(D)—HW/병렬화 이식 가능
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:5336268
- **Type**: conference
- **Published**: 7-9 Oct. 2
- **Authors**: Hyunwoo Ji, Junho Cho, Wonyong Sung
- **PDF**: https://ieeexplore.ieee.org/document/5336268
- **Abstract**: Simulation of low-density parity-check (LDPC) codes frequently takes several days, thus the use of general purpose graphics processing units (GPGPUs) is very promising. However, GPGPUs are designed for compute-intensive applications, and they are not optimized for data caching or control management. In LDPC decoding, the parity check matrix H needs to be accessed at every node updating process, and the size of H matrix is often larger than that of GPU on-chip memory especially when the code-length is long or the weight is high. In this work, the parity check matrix of cyclic or quasi-cyclic LDPC codes is greatly compressed by exploiting the periodic property of the matrix. In our experiments, the Compute Unified Device Architecture (CUDA) of Nvidia is used. With the (1057, 813) and (4161, 3431) projective geometry (PG)-LDPC codes, the execution speed of the proposed method is more than twice of the reference implementations that do not exploit the cyclic property of the parity check matrices.

## Bidirectional interleavers for LDPC decoders using transmission gates

- **Status**: ✅
- **Reason**: transmission gate 양방향 interleaver/shuffle network HW 아키텍처(permutation network, D), NAND 디코더 HW에 이식 가능
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:5336257
- **Type**: conference
- **Published**: 7-9 Oct. 2
- **Authors**: Kevin Cushon, Warren J. Gross, Shie Mannor
- **PDF**: https://ieeexplore.ieee.org/document/5336257
- **Abstract**: Low-density parity check (LDPC) codes are used for forward error correction in several state-of-the-art and upcoming communications standards. This paper presents a new interleaver architecture for LDPC decoders, especially suitable for multi-mode codes such as IEEE 802.16e (WiMAX) and IEEE 802.11n (Wi-Fi), that utilizes a bidirectional datapath and shuffle network composed of transmission gates. An implementation of this architecture for IEEE 802.11n achieves 28% area reduction and similar throughput compared to a unidirectional reference design.

## Low-power implementation of a high-throughput LDPC decoder for IEEE 802.11N standard

- **Status**: ✅
- **Reason**: 고처리량 LDPC 디코더 저전력 HW 구현(serial-parallel, VOS/RPR), NAND 디코더 HW에 이식 가능(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:5336223
- **Type**: conference
- **Published**: 7-9 Oct. 2
- **Authors**: Junho Cho, Naresh R. Shanbhag, Wonyong Sung
- **PDF**: https://ieeexplore.ieee.org/document/5336223
- **Abstract**: Flexible and scalable LDPC decoder architecture is developed for the IEEE 802.11n standard. The serial-parallel architecture is employed for achieving high throughput with low chip area, and triple-bank memory blocks are used for parallel factor expansion. Two low-power strategies using voltage over-scaling (VOS) and reduced-precision replica (RPR) are applied to the decoder. By applying these techniques, power saving of up to 35% is demonstrated when implemented in a 90 nm CMOS technology.

## A new Quasi-Cyclic low density parity check codes

- **Status**: ✅
- **Reason**: row division 기반 신규 QC-LDPC 구성으로 girth/rate/length 유연성 — 바이너리 코드 설계 기법(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5356472
- **Type**: conference
- **Published**: 4-6 Oct. 2
- **Authors**: Abid Yahya, Othman Sidek, M. F. M. Salleh +1
- **PDF**: https://ieeexplore.ieee.org/document/5356472
- **Abstract**: This paper proposes a new technique for constructing the Quasi-Cyclic low density parity check (QC-LDPC) codes based on row division method. The new codes offer more flexibility in term of girth, code rates and codeword length. In this method of code construction, the rows are used to form as the distance graph. Then they are transformed to a parity-check matrix in order to acquire the desired girth. The new QC-LDPC codes show good bit-error rate performance as compared to the renowned Mackay codes for given values of Eb/No by 0.12 dB at BER of10-7 .

## On systematic design of universally capacity approaching rate-compatible sequences of LDPC code ensembles over binary-input output-symmetric memoryless channels

- **Status**: ✅
- **Reason**: BIOSM 채널 capacity-approaching rate-compatible 바이너리 LDPC 앙상블 체계적 설계(SM 원리, puncturing) — 코드설계 기법(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5394793
- **Type**: conference
- **Published**: 30 Sept.-2
- **Authors**: Hamid Saeedi, Hossein Pishro-Nik, Amir H. Banihashemi
- **PDF**: https://ieeexplore.ieee.org/document/5394793
- **Abstract**: Despite tremendous amount of research on the design of low-density parity-check (LDPC) codes with belief propagation decoding over different types of binary-input output-symmetric memoryless (BIOSM) channels, most results on this topic are based on numerical methods and optimization which do not provide much insight into the design process. In particular, systematic design of provably capacity achieving sequences of LDPC code ensembles over the general class of BIOSM channels, has remained a fundamental open problem. For the case of the binary erasure channel, explicit construction of capacity achieving sequences have been proposed based on a property called the flatness condition. In this paper, we propose a systematic method to design universally capacity approaching rate-compatible LDPC code ensemble sequences over BIOSM channels. This is achieved by interpreting the flatness condition over the BEC, as a successive maximization (SM) principle that is generalized to other BIOSM channels to design a sequence of capacity approaching ensembles called the parent sequence. The SM principle is then applied to each ensemble within the parent sequence, this time to design rate-compatible puncturing schemes. As part of our results, we extend the stability condition which was previously derived for degree-2 variable nodes to other variable node degrees as well as to the case of rate-compatible codes. Consequently, we rigorously prove that using the SM principle, one is able to design universally capacity achieving rate-compatible LDPC code ensemble sequences over the BEC. Unlike the previous results on such schemes over the BEC in the literature, the proposed SM approach is naturally extendable to other BIOSM channels. The performance of the rate-compatible schemes designed based on our systematic method is comparable to those designed by optimization.

## LDPC codes for the cascaded BSC-BAWGN channel

- **Status**: ✅
- **Reason**: cascaded BSC-BAWGN 바이너리 LDPC BP 변형 메시지패싱 스킴 제안·DE 분석 — 이식 가능 디코더(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5394916
- **Type**: conference
- **Published**: 30 Sept.-2
- **Authors**: Aravind R. Iyengar, Paul H. Siegel, Jack K. Wolf
- **PDF**: https://ieeexplore.ieee.org/document/5394916
- **Abstract**: We study the performance of LDPC codes over the cascaded BSC-BAWGN channel. This channel belongs to a family of binary-input, memoryless, symmetric-output channels, one that we call the {CBMSC(p, ¿)} family. We analyze the belief propagation (BP) decoder over this channel by characterizing the decodable region of an ensemble of LDPC codes. We then give inner and outer bounds for this decodable region based on existing universal bounds on the performance of a BP decoder. We numerically evaluate the decodable region using density evolution. We also propose other message-passing schemes of interest and give their decodable regions. The performance of each proposed decoder over the CBMS channel family is evaluated through simulations. Finally, we explore capacity-approaching LDPC code ensembles for the {CBMSC(p, ¿)} family.

## A binary message-passing decoding algorithm for LDPC codes

- **Status**: ✅
- **Reason**: soft reliability 기반 바이너리 메시지패싱 디코더(WBF 개선, 저복잡도), 스토리지 적용 명시 — 이식 가능 디코더(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5394796
- **Type**: conference
- **Published**: 30 Sept.-2
- **Authors**: Chao-Yu Chen, Qin Huang, Jingyu Kang +2
- **PDF**: https://ieeexplore.ieee.org/document/5394796
- **Abstract**: This paper presents a soft reliability-based binary message-passing algorithm for decoding LDPC codes. This algorithm outperforms the existing weighted bit-flipping algorithms with much less computational complexity. It is particularly effective for decoding LDPC codes constructed based on finite-geometries and finite fields. The proposed algorithm can be simplified for applications in communication or storage systems where either soft reliability information is not available to the decoder or a simple decoder is needed.

## FPGA-based low-complexity high-throughput tri-mode decoder for quasi-cyclic LDPC codes

- **Status**: ✅
- **Reason**: QC-LDPC tri-mode FPGA 디코더, 부분병렬 아키텍처·메모리공유·1.9Gbps 바이너리 HW(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:5394917
- **Type**: conference
- **Published**: 30 Sept.-2
- **Authors**: Xiaoheng Chen, Qin Huang, Shu Lin +1
- **PDF**: https://ieeexplore.ieee.org/document/5394917
- **Abstract**: This paper presents an FPGA-based implementation of a tri-mode decoder for decoding the cyclic (4095,3367) Euclidean geometry LDPC code which has minimum distance 65 and no trapping set of size less than 65. The implementation integrates three compatible decoding algorithms in a single decoder. The three decoding algorithms are the one-step majority-logic decoding (OS-MLGD) algorithm and two iterative binary message passing algorithms (IBMP) derived from the OS-MLGD algorithm, one based on soft reliability information and the other on hard reliability information. All three algorithms requires only binary logical operations, integer additions, and single-bit messages, which makes them significantly less complex in terms of hardware requirements than sum-product algorithm, with a very modest loss in performance. The implementation is based on the partially parallel architecture and is optimized to take advantage of the high-speed dual-ported block RAMs in a Xilinx Virtex-4 FPGA. An optimization called memory sharing is introduced to take advantage of the configurable data width (word size) of the block RAMs to accommodate the 262080 edges in the Tanner graph of the (4095,3367) code. A technique is introduced to decode two codewords simultaneously to take advantage of the depth of the block RAMs. As a result, the proposed implementation achieves a throughput of 1.9 Gbps on a Virtex-4 LX160 FPGA and supports bit-error rate simulation down to 10-11 in a day or so.

## Trapping set ontology

- **Status**: ✅
- **Reason**: trapping set ontology로 error floor 예측·코드설계 개선, 바이너리 LDPC 디코더/코드설계 직접 이식(C/E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5394825
- **Type**: conference
- **Published**: 30 Sept.-2
- **Authors**: Bane Vasić, Shashi Kiran Chilappagari, Dung Viet Nguyen +1
- **PDF**: https://ieeexplore.ieee.org/document/5394825
- **Abstract**: The failures of iterative decoders for low-density parity-check (LDPC) codes on the additive white Gaussian noise channel (AWGNC) and the binary symmetric channel (BSC) can be understood in terms of combinatorial objects known as trapping sets. In this paper, we derive a systematic method to identify the most relevant trapping sets for decoding over the BSC in the error floor region. We elaborate on the notion of the critical number of a trapping set and derive a classification of trapping sets. We then develop the trapping set ontology, a database of trapping sets that summarizes the topological relations among trapping sets. We elucidate the usefulness of the trapping set ontology in predicting the error floor as well as in designing better codes.

## Parallel LDPC Decoding on a Network-on-Chip Based Multiprocessor Platform

- **Status**: ✅
- **Reason**: NoC 기반 멀티프로세서에서 병렬 LDPC 디코더 아키텍처, 메모리 병목 제거(D, HW 이식 가능)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:5336214
- **Type**: conference
- **Published**: 28-31 Oct.
- **Authors**: Wen-Hsiang Hu, Jun Ho Bahn, Nader Bagherzadeh
- **PDF**: https://ieeexplore.ieee.org/document/5336214
- **Abstract**: Low Density Parity Check (LDPC) code is an error correction code that can achieve performance close to Shannon limit and inherently suitable for parallel implementation. It has been widely adopted in various communication standards such as DVB-S2, WiMAX, and Wi-Fi. However, the irregular message exchange pattern is a major challenge in LDPC decoder implementation In addition, faced with an era that diverse applications are integrated in a single system, a flexible, scalable, efficient and cost-effective implementation of LDPC decoder is highly preferable. In this paper, we proposed a multi-processor platform based on network-on-chip (NoC) interconnect as a solution to these problems. By using a distributed and cooperative way for LDPC decoding, the memory bottleneck commonly seen in LDPC decoder design is eliminated. Simulation results from long LDPC codes with various code rates show good scalability and speedups are obtained by our approach.

## A modified PEG algorithm for construction of LDPC codes with Polynomial of Cycle

- **Status**: ✅
- **Reason**: PEG 개선 알고리즘으로 girth 키우고 최단사이클 수 최소화(Polynomial of Cycle); 바이너리 LDPC 코드설계(E) 신규 기여
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5355908
- **Type**: conference
- **Published**: 27-29 Oct.
- **Authors**: Lei Xiong, Dongping Yao, Yimeng Wu
- **PDF**: https://ieeexplore.ieee.org/document/5355908
- **Abstract**: Progressive Edge-Growth (PEG) algorithm is a novel approach for construction of low-density parity-check (LDPC) codes with large girth. However, PEG algorithm ignores the effect of the number of shortest cycles. In this paper, we propose a modified PEG algorithm with Polynomial of Cycle, which achieves not only large girth, but also minimizes the number of shortest cycles significantly. Simulation results show that our proposed algorithm can improves the performance of LDPC codes.

## Implementation of LDPC decoder for 802.16e

- **Status**: ✅
- **Reason**: TDMP + normalized/offset min-sum QC-LDPC 디코더 FPGA 구현 비교 — 이식 가능 디코더/HW(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5351628
- **Type**: conference
- **Published**: 20-23 Oct.
- **Authors**: Xiao Peng, Satoshi Goto
- **PDF**: https://ieeexplore.ieee.org/document/5351628
- **Abstract**: The implementation complexity of the decoder for Low-density Parity-check Codes (LDPC) is dictated by memory and interconnection requirements. In this paper, we investigate the approaches to realize Turbo Decoding Message Passing (TDMP) algorithm. We compare the performance and implementation complexity of original approach, Jacobian approach, normalized min-sum approach and offset min-sum approach which are targeted for Quasi-Cyclic (QC) LDPC code defined in IEEE 802.16e standard. The normalized and offset approaches are more suitable for hardware implementation, which are realized on the FPGA.1

## A cost efficient LDPC decoder for DVB-S2

- **Status**: ✅
- **Reason**: Min-Sum+TDMP 스케줄 LDPC 디코더 저복잡도 HW 구현, 디코더 스케줄·HW 기법 이식 가능(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5351522
- **Type**: conference
- **Published**: 20-23 Oct.
- **Authors**: Yan Ying, Dan Bo, Shuangqu Huang +3
- **PDF**: https://ieeexplore.ieee.org/document/5351522
- **Abstract**: Based on the Min-Sum algorithm, this paper proposes an LDPC decoder integrating the TDMP schedule, which could achieve low complexity as well as good performance. The LDPC decoder is for DVB-S2, which includes 11 kinds of code rates with a block size of 64800. Based on SMIC 0.13µm standard CMOS process, the LDPC decoder has an estimation area of 14mm2, a throughput of 135Mbps with a frequency of 105MHz and maximum iteration number of 30,which shows advantage over previous DVB-S2 LDPC decoders1.

## A flexible architecture for multi-standard LDPC decoders

- **Status**: ✅
- **Reason**: 다중표준 block-LDPC용 재구성형 RPPU 디코더 아키텍처(row/column update 가변), HW 기법 이식 가능(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:5351626
- **Type**: conference
- **Published**: 20-23 Oct.
- **Authors**: Shuangqu Huang, Bo Xiang, Bei Huang +2
- **PDF**: https://ieeexplore.ieee.org/document/5351626
- **Abstract**: Since Low-Density Parity-Check codes have near-capacity decoding performance and very high decoding throughput, they have been employed as FEC coding scheme in many transmission standards for wireless communication, such as IEEE 802.22n, IEEE 802.16e, DVB-S2, and DTMB. This trend triggers the need for so-called multi-standard LDPC decoders. In this paper, a flexible architecture that supports multiple code rates, variable block sizes and is code independent for block-LDPC codes is proposed, based on rearranged TPMP algorithm,. By implementing a dynamically reconfigurable RPPU, our proposed architecture can be configured into row update or column update mode by time-division multiplexing. Consequently, the decoder achieves a high area and power efficiency. To verify our proposed architecture, a novel LDPC decoder which supports IEEE802.16e standard has been implemented. The results on a 0.18 um CMOS process show that the decoder occupies an area of approximately 13.7 mm2 and runs correctly at an maximum operating frequency of 110 MHz, resulting in 98 Mbps decoding throughput1.

## An multi-rate LDPC decoder based on ASIP for DMB-TH

- **Status**: ✅
- **Reason**: ASIP 기반 멀티레이트 LDPC 디코더 아키텍처+TDMP, 프로그래머블 디코더 HW 기법 이식 가능(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:5351527
- **Type**: conference
- **Published**: 20-23 Oct.
- **Authors**: Xiaojun Zhang, Yinghong Tian, Jianming Cui +2
- **PDF**: https://ieeexplore.ieee.org/document/5351527
- **Abstract**: Based on ASIP (application specific instruction set processor), this paper propose a decoder architecture for LDPC (low density parity check codes) in the DMB-TH standard. The decoder use a five-stage pipeline, 32-bit RISC processor and it can supports three different code rates (0.4, 0.6 and 0.8) by only modifying the program. Based on XC4VLX150, at the max frequency of 126 MHz, the max throughput of the decoder can achieve 96 Mps for 10 TDMP-decoding Iterations. Compared with other GPP and DSP implementations, this ASIP simplify the control logical and enhance the flexibility.

## Design of irregular quasi-cyclic LDPC codes based on Euclidean geometries

- **Status**: ✅
- **Reason**: 유클리드 기하 기반 비정규 QC-LDPC 구성, EXIT/curve-fitting 차수분포 최적화로 error floor 저감 — 바이너리 코드설계(E) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5346414
- **Type**: conference
- **Published**: 19-23 Oct.
- **Authors**: Xueqin Jiang, Moon Ho Lee
- **PDF**: https://ieeexplore.ieee.org/document/5346414
- **Abstract**: This paper presents an approach to the construction of low-density parity-check (LDPC) codes based on hyperplanes (mu-flats) of different dimensions in Euclidean geometries. Codes constructed by this method have quasicyclic and irregular structure. The degree distributions of these codes are optimized by the curve fitting approach in the extrinsic information transfer (EXIT) charts. By constraining the fraction of degree-2 nodes, we can lower the error floor at the cost of a small increase in the threshold SNR. Simulation results show that these codes perform very well at both of waterfall region and the error floor region with the iterative decoding.

## Reduced complexity-and-latency variable-to-check residual belief propagation decoding algorithms for LDPC codes

- **Status**: ✅
- **Reason**: VCRBP(variable-to-check residual BP)의 forced-convergence/sign-based 개선으로 복잡도·지연 감소 — 부호 비의존 디코더(C) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5346442
- **Type**: conference
- **Published**: 19-23 Oct.
- **Authors**: Jung-Hyun Kim, Hong-Yeop Song
- **PDF**: https://ieeexplore.ieee.org/document/5346442
- **Abstract**: This paper proposes some new improved versions of node-wise VCRBP algorithm, called forced-convergence node-wise VCRBP and sign-based node-wise VCRBP, both of which significantly reduce the decoding complexity and latency, with only negligible deterioration in error correcting performance.

## A novel approach for construction of rate-compatible low-density parity-check codes

- **Status**: ✅
- **Reason**: 행 기반 rate-compatible LDPC 신규 구성 + zigzag PEG 변형 + 단일 디코더 — 이식 가능 코드설계(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5379985
- **Type**: conference
- **Published**: 18-21 Oct.
- **Authors**: Liang Chen, Ziyu Wu
- **PDF**: https://ieeexplore.ieee.org/document/5379985
- **Abstract**: In this paper, we construct rate compatible low density parity-check (RC-LDPC) codes from a new perspective. In traditional methods, the columns of parity-check matrix, each of which corresponds to a bit of a codeword, are deleted or added to obtain codes at various rates. Different from them, only the rows of parity-check matrix are operated in our method. Since the number of columns remains unchanged, the block lengths of RC-LDPC codes across a range of rates are always invariable. In our novel construction method, new rows are appended to form the new matrices corresponding to lower-rate codes while some selected rows are eliminated to obtain higher-rate codes. We employ a modified progressive edge growth (PEG) construction with zigzag pattern to actualize linear-time encoding. Before implementing this modified PEG algorithm, a constrained density evolution algorithm is applied to optimize the degree distributions of the mother code. To those columns in the left portion of a mother parity-check matrix which correspond to information bits of a codeword, specified weights are allocated as the condition of the posterior PEG algorithm. We also demonstrate that a single decoder can be used over the entire range of rates. Moreover, the decoder always operates at a high code rate so that energy consumption and circuit size can be reduced. In addition, based on our construction of RC-LDPC codes, a novel effective scheme for hybrid ARQ protocols has been proposed as well.

## Design of a New Kind of LDPC Decoder

- **Status**: ✅
- **Reason**: min-sum+보정인자 부분병렬 LDPC 디코더 HW 구현, 디코더/HW 기법 이식 가능(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5301400
- **Type**: conference
- **Published**: 17-19 Oct.
- **Authors**: Hanhong Jiang, Guifeng Zhong, Qing Li +1
- **PDF**: https://ieeexplore.ieee.org/document/5301400
- **Abstract**: The properties of the LDPC (low-density parity-check) error-correcting codes are bearing down on Shannon limit, but it also needs to solve the problem of reducing the complexity of decoding as much as possible in practical applications. A new type of (1008, 3, 6) rules LDPC decoder was introduced in this paper. It adopted the min-sum-plus-correction-factor decoding algorithm and part parallel structure, which not only reduced the complexity of the hardware realization, but also improved the decoding speed. The maximum decoding rate could achieve 128 Mbit/s. These properties laid a good foundation for the actual application of LDPC.

## Improved Approximately Lower Triangular Encoding of LDPC Codes

- **Status**: ✅
- **Reason**: 개선된 ALT 인코딩으로 희소행렬 순환성 활용 메모리 절감, 코드설계/HW 인코딩 기법(E/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5301507
- **Type**: conference
- **Published**: 17-19 Oct.
- **Authors**: Peng Zhang, Fei Yang, Rui Lv +1
- **PDF**: https://ieeexplore.ieee.org/document/5301507
- **Abstract**: Concerning the high encoding complexity of low-density parity-check (LDPC) codes, an improved approximately lower triangular (ALT) encoding method is proposed, which is able to take full advantage of the characteristics of the sparse parity-check matrix, such as cyclicity and equality of row weight. Experimental results show that, the proposed method can reduce dramatically the memory requirements in hardware implementation, while maintaining the computational complexity nearly.

## A new forced convergence decoding scheme for LDPC codes

- **Status**: ✅
- **Reason**: LDPC forced convergence: 조기 수렴 변수노드 제거로 Tanner 그래프 축소, 디코딩 복잡도 감소 — 이식 가능 디코더 기법(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5349137
- **Type**: conference
- **Published**: 16-18 Oct.
- **Authors**: Jianxiao Fan, Hongwen Yang
- **PDF**: https://ieeexplore.ieee.org/document/5349137
- **Abstract**: In this paper, we present a new forced convergence decoding scheme for LDPC codes. We remove the early detected variable nodes from the Tanner graph and thus the parity matrix shrinks iteration by iteration and the decoding complexity can be reduced. When the parity check matrix shrinks to zero before the maximum iteration, we get a chance to detect the wrong deletion and, for the decodable codewords, most of such failure can be recovered by restoring the original Tanner graph and resuming the decoding in the remaining iterations. Simulations results indicate that the proposed method can reduce the decoding complexity significantly while keep the error rate performance unchanged or even better.

## Improving performance of some irregular LDPC codes by means of three optimization techniques

- **Status**: ✅
- **Reason**: permutation matrix(Q-matrix)·girth·column weight 최적화로 QC-LDPC 개선(E), 바이너리
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5295850
- **Type**: conference
- **Published**: 12-14 Oct.
- **Authors**: Li Peng, Guangxi Zhu
- **PDF**: https://ieeexplore.ieee.org/document/5295850
- **Abstract**: In this paper we present three optimization techniques of improving the performance of some irregular low-density parity-check ensemble with determinate structure and finite block length. Firstly, it is permutation matrix optimization. We present a new random permutation matrix called as the Q-matrix. We substituted Q-matrix for identity matrix in base matrix array which can be expanded into H-matrix of the irregular QC-LDPC codes recommended in IEEE 802.16e standard draft and can make the performance of this QC-LDPC codes improve about 0.4dB. Secondly, it is large girth optimization technique. We design H-matrix of the irregular LDPC ensemble and make it at least not include 8-cycle. Thirdly, it is column weight optimization technique in H-matrix of the irregular LDPC ensemble. For the presented irregular LDPC ensemble, it is not such case that the larger the column weight is and the better the performance is, but the column weight should be a moderate value.

## Performance analysis of implement-oriented capacity-achieving LDPC codes on erasure channel and its encoder design

- **Status**: ✅
- **Reason**: erasure용 capacity-achieving LDPC의 저복잡도 재귀 인코더 회로 설계(D/E), 바이너리
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5295824
- **Type**: conference
- **Published**: 12-14 Oct.
- **Authors**: Li Peng, Guangxi Zhu, Qi Luo
- **PDF**: https://ieeexplore.ieee.org/document/5295824
- **Abstract**: distribution pair equal 1 instead of 0. Its H-matrix is constructed by combining zigzag matrix and partitioned permutation matrices. This paper completed a design from capacity-achieving sequence to algebraic structural H-matrix, and the H-matrix can directly be used to design low complexity recursive encoding circuit.1

## Energy efficiency of SISO algorithms for turbo-decoding message-passing LDPC decoders

- **Status**: ✅
- **Reason**: turbo-decoding message-passing LDPC 디코더 SISO 커널(Self-Corrected Min-Sum) VLSI 에너지효율 비교, min-sum 변형+HW 이식 가능(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6041337
- **Type**: conference
- **Published**: 12-14 Oct.
- **Authors**: Erick Amador, Vincent Rezard, Renaud Pacalet
- **PDF**: https://ieeexplore.ieee.org/document/6041337
- **Abstract**: The decoding of LDPC codes using the turbo-decoding message-passing strategy is considered. This strategy can be used with different SISO message computation kernels. We analyze the suitability for VLSI implementation of various message computation algorithms in terms of implementation area, energy consumption and error-correcting performance. As one of the computation kernels, we introduce the recent Self-Corrected Min-Sum algorithm and show the advantages it brings from an energy efficiency perspective. We present comparisons among the studied kernels implemented in a 65nm CMOS process and use a test case from the codes defined in IEEE 802.11n to show differences in energy efficiency.

## An efficient pseudo-codeword search algorithm for Belief Propagation decoding of LDPC codes

- **Status**: ✅
- **Reason**: BP 디코딩 pseudo-codeword/error floor 분석용 신규 탐색 알고리즘(FFH/Wang-Landau), 바이너리 LDPC BP 이식 가능(C/E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5345453
- **Type**: conference
- **Published**: 12-14 Oct.
- **Authors**: S. Kakakhail, S. Reynal, D. Declercq +1
- **PDF**: https://ieeexplore.ieee.org/document/5345453
- **Abstract**: We introduce the use of fast flat histogram (FFH) method employing Wang Landau algorithm in an adaptive noise sampling framework using random walk to find out the pseudo-codewords and consequently the pseudo-weights for the belief propagation (BP) decoding of LDPC codes over an additive white Gaussian noise (AWGN) channel. The FFH method enables us to tease out pseudo-codewords at very high signal-to-noise ratios (SNRs) exploring the error floor region of a wide range of codes varying in length and structure. We present the pseudo-weight (effective distance) spectra for these codes and analyze their respective behavior.

## Generalized quasi-cyclic low-density parity-check codes based on finite geometries

- **Status**: ✅
- **Reason**: GQC-LDPC(유한기하 기반) 부호 구성 및 선형복잡도 인코더 HW 아키텍처 제시 → 이식 가능 코드설계/HW(E/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5351273
- **Type**: conference
- **Published**: 11-16 Oct.
- **Authors**: Vo Tam Van, Hajime Matsui, Seiichi Mita
- **PDF**: https://ieeexplore.ieee.org/document/5351273
- **Abstract**: In this study, we proved that several promising classes of codes based on finite geometries cannot be classified as quasi-cyclic (QC) codes but should be included in broader generalized quasi-cyclic (GQC) codes. Further, we proposed an algorithm (transpose algorithm) for the computation of the Grobner bases from the parity check matrices of GQC codes. Because of the GQC structure of such codes, they can be encoded systematically using Gro¿bner bases and their encoder can be implemented using simple feedback-shift registers. In order to demonstrate the efficiency of our encoder, we proved that the number of circuit elements in the encoder architecture is proportional to the code length for finite geometry (FG) LDPC codes. For codes constructed using points and lines of finite geometries, the hardware complexity of the serial-in serial-out encoder architecture of the codes is linear order O(n). To encode a binary codeword of length n, less than 2n adder and 3n memory elements are required.

## On the dynamics of the error floor behavior in regular LDPC codes

- **Status**: ✅
- **Reason**: 정규 LDPC error floor의 absorption set(trapping set) 동역학 분석 - error floor 코드설계(E) 관련, NAND LDPC error floor 분석에 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5351244
- **Type**: conference
- **Published**: 11-16 Oct.
- **Authors**: Christian Schlegel, Shuai Zhang
- **PDF**: https://ieeexplore.ieee.org/document/5351244
- **Abstract**: It is shown that dominant trapping sets of regular LDPC codes, so called absorption sets, undergo a two-phase dynamic behavior in the iterative message-passing (MP) decoding algorithm. Using a linear dynamic model for the iteration behavior of these sets, it is shown that they undergo an initial geometric growth phase which stabilizes in a final bit-flipping behavior where the algorithm reaches a fixed point. This analysis is shown to lead to very accurate numerical calculations of the error floor bit error rates down to error rates that are inaccessible by simulation. The topology of the dominant absorption sets of an example code, the IEEE 802.3 an (2048, 1723) regular LDPC code, is identified and tabulated using topological relationships in combination with search algorithms.

## Two efficient and low-complexity iterative reliability-based majority-logic decoding algorithms for LDPC codes

- **Status**: ✅
- **Reason**: 신규 reliability-based majority-logic 반복 디코딩 알고리즘 - 단순 논리회로 구현 가능한 바이너리 메시지패싱 디코더, 이식 가능 디코더(C)+HW(D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5351264
- **Type**: conference
- **Published**: 11-16 Oct.
- **Authors**: Qin Huang, Jingyu Kang, Li Zhang +2
- **PDF**: https://ieeexplore.ieee.org/document/5351264
- **Abstract**: This paper presents two novel iterative reliability-based majority-logic algorithms for decoding LDPC codes. Both algorithms are binary message-passing algorithms and require only logical operations and integer additions. Consequently, they can be implemented with simple combinational logic circuits. They either outperform or perform just well as the existing weighted bit-flipping or other reliability-based decoding algorithms for LDPC codes in error performance with a faster rate of decoding convergence and less decoding complexity. Compared to the sum-product algorithm for LDPC codes, they offer effective trade-offs between performance and decoding complexity.

## Generating random Tanner-graphs with large girth

- **Status**: ✅
- **Reason**: large-girth Tanner 그래프 랜덤 생성 알고리즘 → 사이클 제거 기반 바이너리 LDPC 코드설계 기법(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5351491
- **Type**: conference
- **Published**: 11-16 Oct.
- **Authors**: Mohsen Bayati, Raghunandan Keshavan, Andrea Montanari +2
- **PDF**: https://ieeexplore.ieee.org/document/5351491
- **Abstract**: We present a simple and efficient algorithm for randomly generating Tanner-graphs with given symbol-node and check-node degrees and without small cycles. These graphs can be used to design high performance low-density parity-check (LDPC) codes. Our algorithm generates a graph by sequentially adding the edges to an empty graph. Recently, these types of sequential methods for counting and random generation have been very successful.

## Continuous-time matched filtering and decoding without synchronization

- **Status**: ✅
- **Reason**: LDPC용 input-tracking 디코더(동기화 없는 디코딩)라는 신규 디코더 알고리즘 제시 → 이식 가능 디코더(C), 애매하면 in
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5351431
- **Type**: conference
- **Published**: 11-16 Oct.
- **Authors**: Murthy V. R. S. Devarakonda, Hans-Andrea Loeliger
- **PDF**: https://ieeexplore.ieee.org/document/5351431
- **Abstract**: Standard communication receivers need to establish both symbol synchronization and frame synchronization before error correction can take place. In this paper, we present a coded multi-tone packet transmission format in which synchronization is moved past decoding (and thus effectively eliminated). We also present the concept of an input-tracking decoder, which is required in such a scheme. An example of an input-tracking decoder for LDPC codes is presented and some preliminary simulation results are given.
