# IEEE Xplore — 2008-07


## Construction of Regular Quasi-Cyclic Protograph LDPC Codes Based on Vandermonde Matrices

- **Status**: ✅
- **Reason**: Vandermonde 기반 정규 QC protograph 바이너리 LDPC 구성(girth>=6), HW친화 인코딩/디코딩 — 이식 가능 코드설계(E)
- **ID**: ieee:4389049
- **Type**: journal
- **Published**: July 2008
- **Authors**: Nicholas Bonello, Sheng Chen, Lajos Hanzo
- **PDF**: https://ieeexplore.ieee.org/document/4389049
- **Abstract**: In this paper, we investigate the attainable performance of quasi-cyclic (QC) protograph low-density parity-check (LDPC) codes for transmission over both additive white Gaussian noise and uncorrelated Rayleigh channels. The presented codes are constructed using the Vandermonde matrix and thus have a girth of at least six in their corresponding Tanner graph. Furthermore, they also benefit from both low-complexity encoding and decoding, low memory requirements, as well as hardware-friendly implementations. Our simulation results demonstrate that the advantages offered by this family of QC protograph LDPC codes accrue with no compromise in the attainable bit error ratio (BER) and block error ratio (BLER) performances. In fact, it is also shown that despite their implementational benefits, the proposed codes exhibit slight BER/BLER gains when compared to some of their more complex counterparts of the same length.

## Switch-Type Hybrid Hard Decision Decoding Algorithms for Regular Low-Density Parity-Check Codes

- **Status**: ✅
- **Reason**: 정규 LDPC용 switch-type 하이브리드 경판정 디코딩(NSS) 신규 알고리즘 — 이식 가능 디코더(C)
- **ID**: ieee:4544955
- **Type**: journal
- **Published**: July 2008
- **Authors**: Gong Chen, Liu Qi, Cui Huijuan +1
- **PDF**: https://ieeexplore.ieee.org/document/4544955
- **Abstract**: This correspondence presents the switch strategies for switch-type hybrid hard decision decoding algorithms for regular low-density parity-check (LDPC) codes. After the piecewise analysis of extrinsic information transfer functions for Gallager decoding algorithm B (GB), the normalized switch scheme (NSS), for which the majority-based algorithms and GB are two examples, is proposed. Then, several other examples of NSSs are presented and their convergence properties are analyzed based on the extrinsic information transfer (EXIT) functions. In simulations, the proposed NSSs show meaningful performance improvements and less sensitivity to channel parameter underestimations compared with GB for small and moderate block length codes.

## A general construction of constrained parity-check codes for optical recording

- **Status**: ❌
- **Reason**: 광기록용 제약+패리티검사 결합코드 설계, 선형 PC 코드 기반이며 LDPC BP로 이식할 기법 없음
- **ID**: ieee:4568448
- **Type**: journal
- **Published**: July 2008
- **Authors**: Kui Cai, Kees A.S. Immink
- **PDF**: https://ieeexplore.ieee.org/document/4568448
- **Abstract**: This paper proposes a general and systematic code design method to efficiently combine constrained codes with parity-check (PC) codes for optical recording. The proposed constrained PC code includes two component codes: the normal constrained (NC) code and the parity-related constrained (PRC) code. They are designed based on the same finite state machine (FSM). The rates of the designed codes are only a few tenths below the theoretical maximum. The PC constraint is defined by the generator matrix (or generator polynomial) of a linear binary PC code, which can detect any type of dominant error events or error event combinations of the system. Error propagation due to parity bits is avoided, since both component codes are protected by PCs. Two approaches are proposed to design the code in the non-return-to-zero-inverse (NRZI) format and the non-return-to-zero (NRZ) format, respectively. Designing the codes in NRZ format may reduce the number of parity bits required for error detection and simplify post-processing for error correction. Examples of several newly designed codes are illustrated. Simulation results with the Blu-Ray disc (BD) systems show that the new d = 1 constrained 4-bit PC code significantly outperforms the rate 2/3 code without parity, at both nominal density and high density.

## Bypass Decoding: A Reduced-Complexity Decoding Technique for LDPC-Coded MIMO-OFDM Systems

- **Status**: ✅
- **Reason**: LLR 임계 기반 bypass 디코딩으로 LDPC 디코더 복잡도 저감 — 부호 비의존적 디코더 기법으로 이식 가능(C)
- **ID**: ieee:4382921
- **Type**: journal
- **Published**: July 2008
- **Authors**: Yan Xin, Syed Aon Mujtaba, Tong Zhang +1
- **PDF**: https://ieeexplore.ieee.org/document/4382921
- **Abstract**: In this paper, we propose a simple reduced-complexity decoding technique called bypass decoding for low-density parity-check (LDPC)-coded multiple-input-multiple-output (MIMO) orthogonal frequency-division multiplexing (OFDM) systems. Employing the bypass decoding technique, the receiver of an LDPC-coded MIMO-OFDM system decodes a codeword in two steps based on the log-likelihood ratios (LLRs) of coded bits. The hard decisions are first made on the coded bits whose LLRs have magnitudes above a certain threshold, and the rest of the coded bits will next be decoded by using an iterative receiver. We show that, as long as the threshold is properly selected, the bypass decoding technique not only delivers considerable complexity reductions but also maintains a comparable performance in LDPC-coded MIMO-OFDM transmissions. We also provide a selection rule for choosing a suitable threshold and show its effectiveness by simulations.

## Implementation aspects of LDPC convolutional codes

- **Status**: ✅
- **Reason**: LDPC convolutional 코드 저복잡도 디코딩/HW 구현 전략 — 디코더+HW 기법(C/D), 바이너리
- **ID**: ieee:4568447
- **Type**: journal
- **Published**: July 2008
- **Authors**: Ali Emre Pusane, Alberto Jimenez Feltstrom, Arvind Sridharan +3
- **PDF**: https://ieeexplore.ieee.org/document/4568447
- **Abstract**: Potentially large storage requirements and long initial decoding delays are two practical issues related to the decoding of low-density parity-check (LDPC) convolutional codes using a continuous pipeline decoder architecture. In this paper, we propose several reduced complexity decoding strategies to lessen the storage requirements and the initial decoding delay without significant loss in performance. We also provide bit error rate comparisons of LDPC block and LDPC convolutional codes under equal processor (hardware) complexity and equal decoding delay assumptions. A partial syndrome encoder realization for LDPC convolutional codes is also proposed and analyzed. We construct terminated LDPC convolutional codes that are suitable for block transmission over a wide range of frame lengths. Simulation results show that, for terminated LDPC convolutional codes of sufficiently large memory, performance can be improved by increasing the density of the syndrome former matrix.

## Pilotless Frame Synchronization for LDPC-Coded Transmission Systems

- **Status**: ❌
- **Reason**: LDPC 신드롬 피드백 기반 프레임 동기화 — 채널 ECC 디코더/구성 기여 아닌 동기화 기법
- **ID**: ieee:4493497
- **Type**: journal
- **Published**: July 2008
- **Authors**: Dong-Uno period after U Lee, Hyungjin Kim, Christopher R. Jones +1
- **PDF**: https://ieeexplore.ieee.org/document/4493497
- **Abstract**: We present a pilotless frame synchronization approach that exploits feedback from a low-density parity-check (LDPC) code decoder. The synchronizer is based on syndrome checks using hard decisions from the channel observations. The bandwidth overhead associated with pilot symbols in conventional receiver architectures is eliminated while providing sufficient synchronization performance. An LDPC decoder coupled with our synchronizer exhibits negligible frame error rate degradation over a system with perfect synchronization. The complexity of the frame synchronizer is kept relatively low due to its XOR-based approach.

## Sequential message-passing decoding of LDPC codes by partitioning check nodes

- **Status**: ✅
- **Reason**: 체크노드 분할 순차 메시지패싱 디코딩 — 수렴 빠른 신규 BP 변형(C)
- **ID**: ieee:4568441
- **Type**: journal
- **Published**: July 2008
- **Authors**: Sunghwan Kim, Min-Ho Jang, Jong-Seon No +2
- **PDF**: https://ieeexplore.ieee.org/document/4568441
- **Abstract**: In this paper, we analyze the sequential message- passing decoding algorithm of low-density parity-check (LDPC) codes by partitioning check nodes. This decoding algorithm shows better bit error rate (BER) performance than the conventional message-passing decoding algorithm, especially for the small number of iterations. Analytical results indicate that as the number of partitioned subsets of check nodes increases, the BER performance is improved. We also derive the recursive equations for mean values of messages at check and variable nodes by using density evolution with a Gaussian approximation. From these equations, the mean values are obtained at each iteration of the sequential decoding algorithm and the corresponding BER values are calculated. They show that the sequential decoding algorithm converges faster than the conventional one. Finally, the analytical results are confirmed by the simulation results.

## Scaling tape-recording areal densities to 100 Gb/in2

- **Status**: ❌
- **Reason**: 자기 테이프 기록 면밀도 스케일링, 매체/서보 이슈로 떼어낼 ECC 기법 없음
- **ID**: ieee:5388603
- **Type**: journal
- **Published**: July 2008
- **Authors**: A. J. Argumedo, D. Berman, R. G. Biskeborn +16
- **PDF**: https://ieeexplore.ieee.org/document/5388603
- **Abstract**: We examine the issue of scaling magnetic tape-recording to higher areal densities, focusing on the challenges of achieving 100 Gb/in2 in the linear tape format. The current highest achieved areal density demonstrations of 6.7 Gb/in2 in the linear tape and 23.0 Gb/in2 in the helical scan format provide a reference for this assessment. We argue that controlling the head-tape interaction is key to achieving high linear density, whereas track-following and reel-to-reel servomechanisms as well as transverse dimensional stability are key for achieving high track density. We envision that advancements in media, data-detection techniques, reel-to-reel control, and lateral motion control will enable much higher areal densities. An achievable goal is a linear density of 800 Kb/in and a track pitch of 0.2 µm, resulting in an areal density of 100 Gb/in2.

## Highly Robust Error Correction byConvex Programming

- **Status**: ❌
- **Reason**: convex programming(LP/SOCP) 기반 실수 신호 오류정정 — LDPC 디코더 아님, 채널 ECC 이식 기법 없음
- **ID**: ieee:4544953
- **Type**: journal
- **Published**: July 2008
- **Authors**: Emmanuel J. Candes, Paige A. Randall
- **PDF**: https://ieeexplore.ieee.org/document/4544953
- **Abstract**: This paper discusses a stylized communications problem where one wishes to transmit a real-valued signal (a block of pieces of information) to a remote receiver. We ask whether it is possible to transmit this information reliably when a fraction of the transmitted codeword is corrupted by arbitrary gross errors, and when in addition, all the entries of the codeword are contaminated by smaller errors (e.g., quantization errors). We show that if one encodes the information as where is a suitable coding matrix, there are two decoding schemes that allow the recovery of the block of pieces of information with nearly the same accuracy as if no gross errors occurred upon transmission (or equivalently as if one had an oracle supplying perfect information about the sites and amplitudes of the gross errors). Moreover, both decoding strategies are very concrete and only involve solving simple convex optimization programs, either a linear program or a second-order cone program. We complement our study with numerical simulations showing that the encoder/decoder pair performs remarkably well.

## Antenna Selection in Space-Time Block Coded Systems: Performance Analysis and Low-Complexity Algorithm

- **Status**: ❌
- **Reason**: MIMO STBC 안테나 선택, LDPC 무관 무선 통신 응용
- **ID**: ieee:4545253
- **Type**: journal
- **Published**: July 2008
- **Authors**: Chiang-Yu Chen, Aydin Sezgin, John M. Cioffi +1
- **PDF**: https://ieeexplore.ieee.org/document/4545253
- **Abstract**: This paper presents outage probability analysis and a practical algorithm for antenna selection in multiple-input multiple-output wireless communication systems employing space-time block codes (STBC). First, to minimize the outage probability in these systems, a satisfactory antenna selection criterion for an STBC is to maximize the channel Frobenius norm. Analysis shows that the more receive antennas are selected, the better the performance. However, the performance of transmit antenna selection heavily depends on how fast the channel changes. When the channel changes slowly, since STBC averages the channel gains of the selected transmit antennas, selecting more transmit antennas causes lower coding gain and thus higher outage probability. When the channel is fast changing, it is shown analytically that the system can no longer provide transmit selection diversity in the high SNR regime. Since the transmit diversity can be still provided by using STBC, the best STBC scheme varies with SNR. Although the outage analysis helps determine the STBC scheme, finding the optimal antenna subsets with maximum channel Frobenius norm for each fading state is still a challenging problem. This is because solving the problem optimally requires an exhaustive search with exponentially growing complexity. When the numbers of antennas are large, the problem becomes intractable. To reduce the complexity, this problem is formulated as a quadratically constrained quadratic programming (QCQP) problem. Despite the fact that the problem is nonconvex, a semidefinite relaxation of QCQP enables the problem to be solved approximately in polynomial time. Simulation results indicate that the loss of semidefinite relaxation to optimal selection is negligible.

## An EM approach to multiple-access interference mitigation in asynchronous slow FHSS systems

- **Status**: ❌
- **Reason**: FHSS MAI 완화용 EM 알고리즘, 무선 통신 응용으로 LDPC ECC 무관
- **ID**: ieee:4570232
- **Type**: journal
- **Published**: July 2008
- **Authors**: Xing Tan, John M. Shea
- **PDF**: https://ieeexplore.ieee.org/document/4570232
- **Abstract**: In this paper, we apply the EM algorithm for mitigation of multi-access interference (MAI) in asynchronous slow frequency-hop spread spectrum (FHSS) systems that employ binary frequency-shift keying (BFSK) modulation. MAI occurs if the hopping patterns of the users are not orthogonal. We show that when FSK signals arrive asynchronously, the time offset exposes portions of the desired and interfering signals in a way that can be exploited to improve the decoder performance. We develop an iterative detection, estimation, and decoding scheme to recover the desired signal in the presence of MAI. We compare the performance of this algorithm with that of a conventional noncoherent BFSK transceiver and show that the EM-based algorithm is particularly effective in the presence of strong interfering signals and allows more users in a FHSS system.

## Outage Performance and IRA Code Design for MIMO Block Fading With Unitary Scrambling

- **Status**: ❌
- **Reason**: MIMO 블록페이딩 unitary scrambling+IRA 코드 EXIT 설계, 통신 채널 응용 특이적이라 떼어낼 NAND LDPC 기법 약함
- **ID**: ieee:4400054
- **Type**: journal
- **Published**: July 2008
- **Authors**: Guosen Yue, Xiaodong Wang, Mohammad Madihian
- **PDF**: https://ieeexplore.ieee.org/document/4400054
- **Abstract**: We consider coded multiple-input-multiple-output (MIMO) systems in block-fading channels employing iterative receivers, where the MIMO channels are scrambled by unitary matrices. We show that the unitary scrambling improves the outage performance with discrete input when the outer code rate is high, i.e., Ro > 0.5. We also demonstrate that the performance improvement from scrambling can be achieved by a small number of random unitary matrices. Moreover, with unitary scrambling, the signal model can be simplified, and the performance of the MIMO demodulator can be characterized by the singular values of the channel matrix. We then consider the design of irregular repeat-accumulate (IRA) codes for unitary scrambled MIMO block-fading channels. We propose a code design method by optimizing the IRA codes for extrinsic information transfer (EXIT) average with a given effective mutual information. We also propose a pessimistic code design for some system settings to improve the frame error rate performance.

## Fault Tolerant Reversible Finite Field Arithmetic Circuits

- **Status**: ❌
- **Reason**: 가역 유한체 산술회로 fault tolerant에 LDPC를 패리티예측 도구로 사용, NAND ECC 디코더/구성 기여 없음
- **ID**: ieee:4567090
- **Type**: conference
- **Published**: 7-9 July 2
- **Authors**: Jimson Mathew, Jawar Singh, Anas Abu Taleb +1
- **PDF**: https://ieeexplore.ieee.org/document/4567090
- **Abstract**: In this paper, we present a systematic method for the designing fault tolerant reversible arithmetic circuits for finite field or Galois fields of the form GF(2m). To tackle the problem of errors in computation, we propose error detection and correction using multiple parity prediction technique based on low density parity check (LDPC) code. For error detection and correction, we need additional garbage outputs. Our technique, when compared with traditional fault tolerant approach gives better implementation cost.

## Minimum-delay decoding of turbo codes for upper-layer FEC

- **Status**: ❌
- **Reason**: BEC turbo 부호 최소지연 디코딩, 비-LDPC(turbo) 부호이며 LDPC는 성능 비교 대상일 뿐
- **ID**: ieee:4641581
- **Type**: conference
- **Published**: 6-9 July 2
- **Authors**: Ghassan M. Kraidy, Valentin Savin
- **PDF**: https://ieeexplore.ieee.org/document/4641581
- **Abstract**: In this paper we investigate the decoding of parallel turbo codes over the binary erasure channel suited for upper-layer error correction. The proposed algorithm performs ldquoon-the-flyrdquo decoding, i.e. it starts decoding as soon as the first symbols are received. This algorithm compares with the iterative decoding of codes defined on graphs [1], in that it propagates in the trellises of the turbo code by removing transitions in the same way edges are removed in a bipartite graph under message-passing decoding. Performance comparison with LDPC codes for different coding rates is shown.

## Blind frame synchronization and phase offset estimation for coded systems

- **Status**: ❌
- **Reason**: BPSK용 블라인드 프레임 동기·위상오프셋 추정, LDPC는 적용 예시일 뿐 ECC 디코더·구성 기여 없음
- **ID**: ieee:4641560
- **Type**: conference
- **Published**: 6-9 July 2
- **Authors**: Rodrigue Imad, Sebastien Houcke
- **PDF**: https://ieeexplore.ieee.org/document/4641560
- **Abstract**: In this paper, we present a new algorithm of blind frame synchronization and phase offset estimation that can be applied to any digital transmission scheme using a channel coding with a binary phase shift keying (BPSK) modulation. The estimator is based on the calculation of the syndrome elements of a received codeword obtained using the parity check matrix of the code. After presenting the proposed method, we evaluate its performance by applying it to some low density parity check (LDPC) codes and convolutional codes. This performance is measured by plotting the probability of false frame synchronization and the mean squared estimation error (MSEE) versus the signal to noise ratio (Eb/N0).

## Capacity-based performance comparison of MIMO-BICM demodulators

- **Status**: ❌
- **Reason**: MIMO-BICM 복조기 용량 비교, 무선 응용 특이적이고 LDPC는 부수 언급
- **ID**: ieee:4641591
- **Type**: conference
- **Published**: 6-9 July 2
- **Authors**: Peter Fertl, Joakim Jalden, Gerald Matz
- **PDF**: https://ieeexplore.ieee.org/document/4641591
- **Abstract**: This paper provides a performance comparison of multiple-input multiple-output (MIMO) demodulators for bit-interleaved coded modulation (BICM) systems with non-iterative demodulation and decoding. We propose to use the capacity of an equivalent ldquomodulationrdquo channel as a performance measure that has the advantage of not depending on the outer error correcting code. Based on this approach, we conclude that a universal ranking of MIMO (soft and hard) demodulation algorithms is not possible. This result is confirmed via bit error rate simulations for a practical system involving low-density parity-check codes. Our approach also allows to derive practical guidelines for MIMO-BICM system design.

## Iterative joint decoding for sensor networks with binary CEO model

- **Status**: ❌
- **Reason**: 센서네트워크 binary CEO 결합디코딩, convolutional/Hamming/SPC 사용으로 LDPC ECC 기법 아님
- **ID**: ieee:4641566
- **Type**: conference
- **Published**: 6-9 July 2
- **Authors**: Javad Haghighat, Hamid Behroozi, David V. Plant
- **PDF**: https://ieeexplore.ieee.org/document/4641566
- **Abstract**: An iterative joint decoding algorithm for data gathering wireless sensor networks is proposed in where the correlation between sensorspsila data is considered as a global code and iterative decoding is performed by concatenating the global decoder with the decoder of error correcting code applied to encode sensors observations. We apply this algorithm for sensor networks with binary CEO model where sensors observe different noisy versions of a single source, located away from sensors. This calls for employing more powerful error correcting codes, therefore we apply convolutional codes (Hamming codes and single parity check codes are applied in). We use the concept of iterative horizontal-vertical decoding for concatenated block codes to formulate the update rules for L-values for the considered binary CEO model. Our simulations confirm that the iterative joint decoding scheme substantially decreases the bit error rate compared with the separate decoding scheme, and reaches the minimum achievable distortion for channels with significantly higher noise levels.

## Min-Max decoding for non binary LDPC codes

- **Status**: ❌
- **Reason**: Min-Max decoding for non-binary LDPC; non-binary GF(q) decoder, excluded
- **ID**: ieee:4595129
- **Type**: conference
- **Published**: 6-11 July 
- **Authors**: Valentin Savin
- **PDF**: https://ieeexplore.ieee.org/document/4595129
- **Abstract**: Iterative decoding of non-binary LDPC codes is currently performed using either the sum-product or the min-sum algorithms or slightly different versions of them. In this paper, several low-complexity quasi-optimal iterative algorithms are proposed for decoding non-binary codes. The min-max algorithm is one of them and it has the benefit of two possible LLR domain implementations: a standard implementation, whose complexity scales as the square of the Galois field's cardinality and a reduced complexity implementation called selective implementation, which makes the min-max decoding very attractive for practical purposes.

## Conditional entropy of non-binary LDPC codes over the BEC

- **Status**: ❌
- **Reason**: non-binary LDPC over BEC; explicitly non-binary GF(q), excluded
- **ID**: ieee:4595126
- **Type**: conference
- **Published**: 6-11 July 
- **Authors**: Vishwambhar Rathi
- **PDF**: https://ieeexplore.ieee.org/document/4595126
- **Abstract**: We consider transmission over the binary erasure channel (BEC) using non-binary LDPC codes. We generalize the concept of stopping sets to non-binary LDPC codes. We give a combinatorial characterization of decoding failures for non-binary LDPC codes decoded via Belief Propagation (BP). Using the density evolution analysis, we compute the asymptotic residual degree distribution for non-binary LDPC codes. In order to show that asymptotically almost every code in the non-binary LDPC ensemble has a rate equal to the design rate, we generalize the arguments of Measson, Montanari, and Urbanke to the non-binary setting. This generalization enables us to compute the conditional entropy of non-binary LDPC codes. We observe that the Maxwell construction of Measson, Montanari, and Urbanke relating the performance of MAP and BP decoding, holds in the setting of non-binary LDPC codes.

## UEP non-binary LDPC codes: A promising framework based on group codes

- **Status**: ❌
- **Reason**: 비이진(group/GF(q)) LDPC UEP, 비이진 LDPC는 제외 대상
- **ID**: ieee:4595386
- **Type**: conference
- **Published**: 6-11 July 
- **Authors**: Alban Goupil, David Declercq
- **PDF**: https://ieeexplore.ieee.org/document/4595386
- **Abstract**: In this paper, we address the problem of providing unequal error protection (UEP) with LDPC codes built on finite sets of order strictly greater than 2 (nonbinary codes). The main interest of providing UEP with nonbinary LDPC codes is that future standards are likely to prefer nonbinary coding schemes because of their better robustness to the codeword length and the modulation size. However, the problem of giving UEP properties with nonbinary LDPC codes is much more difficult than with binary LDPC codes. We present a first attempt to solve this difficult problem, based on LDPC codes built on finite groups. The framework and the basis about group LDPC codes are first presented in details, and the framework is used to give examples of UEP nonbinary LDPC codes that actually achieve different UEP properties at the bit level while the symbol error properties are kept equally protected.

## Asymptotically good LDPC convolutional codes based on protographs

- **Status**: ✅
- **Reason**: protograph 기반 LDPC convolutional 코드 구성과 free distance 분석; 바이너리 LDPC 코드설계(E) 이식 가능.
- **ID**: ieee:4595143
- **Type**: conference
- **Published**: 6-11 July 
- **Authors**: David G. M. Mitchell, Ali E. Pusane, Kamil Sh. Zigangirov +1
- **PDF**: https://ieeexplore.ieee.org/document/4595143
- **Abstract**: LDPC convolutional codes have been shown to be capable of achieving the same capacity-approaching performance as LDPC block codes with iterative message-passing decoding. In this paper, asymptotic methods are used to calculate a lower bound on the free distance for several ensembles of asymptotically good protograph-based LDPC convolutional codes. Further, we show that the free distance to constraint length ratio of the LDPC convolutional codes exceeds the minimum distance to block length ratio of corresponding LDPC block codes.

## A branch and cut algorithm for finding the minimum distance of a linear block code

- **Status**: ❌
- **Reason**: 선형블록부호 최소거리 계산용 branch-and-cut IP 알고리즘, 부호 분석 도구이지 디코더·HW·코드설계 기법 아님
- **ID**: ieee:4594976
- **Type**: conference
- **Published**: 6-11 July 
- **Authors**: Ahmet Keha, Tolga M. Duman
- **PDF**: https://ieeexplore.ieee.org/document/4594976
- **Abstract**: We give a branch-and-cut algorithm for finding the minimum distance of a binary linear error correcting code. We give two integer programming (IP) models and study the convex hull of the single constraint relaxation of these IP models. We use the new inequalities as cuts in a branch-and-cut scheme. Finally, we report computational results based on low density parity check (LDPC) codes that demonstrate the effectiveness of our cuts.

## Irregular low-density parity-check lattices

- **Status**: ❌
- **Reason**: LDPC lattice(격자부호) 구성·density evolution, 채널부호가 아닌 격자코딩 게인 목적이라 NAND ECC 이식성 낮음
- **ID**: ieee:4595437
- **Type**: conference
- **Published**: 6-11 July 
- **Authors**: Ihn-Jung Baik, Sae-Young Chung
- **PDF**: https://ieeexplore.ieee.org/document/4595437
- **Abstract**: We construct lattices with high coding gains based on nested low-density parity-check (LDPC) codes by Construction D′.We generalize the LDPC lattices [1] to have irregular degrees and call them irregular LDPC lattices. To construct good irregular LDPC lattices, we optimize the degree distributions by using density evolution and a modified sequential quadratic programming (SQP) and show our optimized irregular LDPC lattice has a threshold 0.48dB from the capacity, which is about 0.6dB better than the regular one in [1]. To construct a Tanner graph corresponding to LDPC lattices, we generalize the progressive-edge growth (PEG) algorithm and show a lower bound on the girth of the graph. Simulation is performed using the sum-product algorithm. Also, we compare the performance of joint decoding and multi-stage decoding [2] and show the advantage of joint decoding.

## Non-binary decoding of structured LDPC codes: Density evolution

- **Status**: ❌
- **Reason**: non-binary decoding of structured turbo/LDPC codes; non-binary iterative decoding, excluded
- **ID**: ieee:4595127
- **Type**: conference
- **Published**: 6-11 July 
- **Authors**: Daniele Capirone, Giacomo Como, Fabio Fagnani +1
- **PDF**: https://ieeexplore.ieee.org/document/4595127
- **Abstract**: A class of serial turbo codes admitting low-density parity-check (LDPC) representation is considered. Their parity matrix has a random and a structured part. Thanks to their turbo structure, these codes are linear-time encodable, while they can be decoded as LDPC codes. Previous works enlightened the role of the inner encoder in the error floor region and suggested the use of a non-binary iterative decoding algorithm. In this paper, a density-evolution analysis is developed giving insight into the performance of these codes in the waterfall region. The inner encoder is optimized in order to guarantee the best tradeoff between error floor and threshold.

## Improved bilayer LDPC codes using irregular check node degree distribution

- **Status**: ✅
- **Reason**: bilayer LDPC 부호 설계에 비정규 체크노드 차수분포·density evolution 적용한 신규 코드설계 기법(E), 바이너리 LDPC
- **ID**: ieee:4594964
- **Type**: conference
- **Published**: 6-11 July 
- **Authors**: Marwan H. Azmi, Jinhong Yuan, Jun Ning +1
- **PDF**: https://ieeexplore.ieee.org/document/4594964
- **Abstract**: This paper presents an improved LDPC code design for decode-and-forward relay system. Our design is based on the recent work of bilayer LDPC code structures.We introduce an irregular check node degree distribution for the lower and hyper (overall) bilayer LDPC code Tanner graphs. We derive the exact relationship between the lower and hyper graphs in terms of degree distributions (node perspective). This relationship acts as constraint to perform the density evolution. We apply the differential evolution algorithm to search for the best degree distribution for both bilayer-lengthened and bilayer-expurgated LDPC codes. We show that the performance gap of the codes is within 0.07595dB and 0.28407dB from the theoretical limits.

## Two-edge type LDPC code ensembles with exponentially few codewords with linear small weight

- **Status**: ✅
- **Reason**: two-edge/multi-edge type LDPC 앙상블의 최소거리 선형증가 조건 도출; 바이너리 코드설계(E) 이식 가능.
- **ID**: ieee:4595165
- **Type**: conference
- **Published**: 6-11 July 
- **Authors**: Tsuyoshi Nakasendo, Kenta Kasai, Tomoharu Shibuya +1
- **PDF**: https://ieeexplore.ieee.org/document/4595165
- **Abstract**: Multi-Edge type LDPC codes are introduced by Richardson and Urbanke, and they show examples of their ensembles has better performance than other known ensembles. Orlitsky et al. derived the condition for irregular LDPC code ensembles with minimum distance linearly increasing in code length. We derive the condition corresponding to Orlitsky’s condition for two-edge type LDPC code ensembles which is simple example of Multi-Edge type LDPC code ensembles.

## LDPC coding schemes for error control in a multicast network

- **Status**: ✅
- **Reason**: C: joint iterative message-passing decoding scheme improvement for binary LDPC; decoder technique potentially portable
- **ID**: ieee:4595101
- **Type**: conference
- **Published**: 6-11 July 
- **Authors**: Jingyu Kang, Bo Zhou, Zhi Ding +1
- **PDF**: https://ieeexplore.ieee.org/document/4595101
- **Abstract**: This paper investigates error control at the physical layer of a multicast network using low-density parity-check (LDPC) codes. Packets for transmission are encoded into LDPC codewords. A joint iterative message-passing scheme for decoding LDPC codewords at a receive node in the network is proposed to improve error performance. Also proposed is a split-codeword transmission to provide equal error protection for all transmitted packets. Density evolution analysis and some simulation results are also presented.

## On the probabilistic computation algorithm for the minimum-size stopping sets of LDPC codes

- **Status**: ✅
- **Reason**: Probabilistic algorithm for minimum-size stopping sets of LDPC codes; relevant to error-floor/code-design analysis (E) for binary LDPC.
- **ID**: ieee:4594995
- **Type**: conference
- **Published**: 6-11 July 
- **Authors**: Masanori Hirotomo, Yoshiho Konishi, Masakatu Morii
- **PDF**: https://ieeexplore.ieee.org/document/4594995
- **Abstract**: On the binary erasure channel, the performance of LDPC codes decoded by iterative algorithms is estimated by small-size stopping sets. We have proposed a probabilistic algorithm for computing the minimum size of stopping sets of LDPC codes. In this paper, we analyze the probability and the complexity of finding the minimum-size stopping sets, and give an error probability of determining the minimum size of stopping sets after processing our algorithm. Additionally, we show the numerical results of computing the minimum size of stopping sets of several LDPC codes. In these result, we could compute the minimum size of stopping sets with high reliability.

## Ensemble weight enumerators for protograph-based doubly generalized LDPC codes

- **Status**: ✅
- **Reason**: 프로토그래프 기반 DGLDPC의 최소거리 성장률·error floor 개선 코드설계(E), 바이너리 LDPC 이식 가능
- **ID**: ieee:4595171
- **Type**: conference
- **Published**: 6-11 July 
- **Authors**: Yige Wang, Chung-Li Wang, Marc Fossorier
- **PDF**: https://ieeexplore.ieee.org/document/4595171
- **Abstract**: Protograph-based doubly generalized LDPC (DGLDPC) codes are explored in this paper. We extend (and in the process simplify) the technique for computing the ensemble weight enumerators of protograph-based LDPC and GLDPC codes to DGLDPC codes. We find that with careful design, protograph-based DGLDPC codes can have a better asymptotic growth rate of minimum distance than that of the protograph-based LDPC and GLDPC codes. Simulation results confirm that protograph-based DGLDPC codes have a low error floor.

## Sparse representations for codes and the hardness of decoding LDPC codes

- **Status**: ✅
- **Reason**: Sparse representation reduction transforming dense codes to sparse codes amenable to BP; potentially transferable code/decoding insight for binary LDPC BP.
- **ID**: ieee:4594994
- **Type**: conference
- **Published**: 6-11 July 
- **Authors**: Nandakishore Santhi
- **PDF**: https://ieeexplore.ieee.org/document/4594994
- **Abstract**: The maximum likelihood decoding problem is known to be NP-hard for binary linear codes, while belief propagation decoding is known to work well in practice for several LDPC codes. In this paper we give a polynomial time reduction from the maximum likelihood decoding (MLD) problem for binary linear codes to the weighted MLD problem for (3,3)- LDPC codes. The reduction proves the NP-hardness of weighted MLD for (3,3)-LDPC codes. It also provides a method which can be used to transform the decoding problem for dense codes to the decoding of sparse codes. The later problem is often more amenable to the use of belief propagation algorithm. For ease of presentation, we have organized the total reduction in several intermediate reductions, most of which are elementary and easy to follow.

## On the design of universal LDPC codes

- **Status**: ❌
- **Reason**: universal LDPC design across equal-capacity channels; theoretical convergence/stability conjecture, no new decoder/HW/construction portable to NAND
- **ID**: ieee:4595097
- **Type**: conference
- **Published**: 6-11 July 
- **Authors**: Ali Sanaei, Mahdi Ramezani, Masoud Ardakani
- **PDF**: https://ieeexplore.ieee.org/document/4595097
- **Abstract**: Low-density parity-check (LDPC) coding for a multitude of equal-capacity channels is studied. First, based on numerous observations, a conjecture is stated that when the belief propagation decoder converges on a set of equal-capacity channels, it would also converge on any convex combination of those channels. Then, it is proved that when the stability condition is satisfied for a number of channels, it is also satisfied for any channel in their convex hull. For the purpose of code design, a method is proposed which can decompose every symmetric channel with capacity C into a set of identical-capacity basis channels. We expect codes that work on the basis channels to be suitable for any channel with capacity C. Such codes are found and in comparison with existing LDPC codes that are designed for specific channels, our codes obtain considerable coding gains when used across a multitude of channels.

## Array dispersions of matrices and constructions of quasi-cyclic LDPC codes over non-binary fields

- **Status**: ❌
- **Reason**: 비이진(non-binary GF(q)) QC-LDPC 구성으로 기준상 명시 제외 (바이너리만 포함)
- **ID**: ieee:4595169
- **Type**: conference
- **Published**: 6-11 July 
- **Authors**: Bo Zhou, Li Zhang, Jingyu Kang +3
- **PDF**: https://ieeexplore.ieee.org/document/4595169
- **Abstract**: This paper presents two new algebraic constructions of high performance non-binary quasi-cyclic LDPC codes based on array dispersions of matrices over non-binary fields. Codes constructed perform well over the AWGN channel with iterative decoding using a Fast Fourier Transform based sum-product algorithm. They achieve significantly large coding gains over Reed-Solomon codes of the same lengths and rates decoded with either the hard-decision Berlekamp-Massey algorithm or the algebraic soft-decision Koetter-Vardy algorithm. Due to their quasi-cyclic structure, they can be efficiently encoded using simple shift-registers with linear complexity. They have a potential to replace RS codes for some applications in communication and storage systems.

## Iterative approximate linear programming decoding of LDPC codes with linear complexity

- **Status**: ✅
- **Reason**: LDPC LP 디코딩의 선형복잡도 근사 반복 알고리즘(C), 디코더 기법 이식 가능
- **ID**: ieee:4595237
- **Type**: conference
- **Published**: 6-11 July 
- **Authors**: David Burshtein
- **PDF**: https://ieeexplore.ieee.org/document/4595237
- **Abstract**: The problem of low complexity linear programming (LP) decoding of low-density parity-check (LDPC) codes is considered. An iterative algorithm for efficient approximate solution of this problem was proposed by Vontobel and Koetter. In this paper the convergence rate and computational complexity of this algorithm are studied. In particular we are interested in obtaining a feasible vector in the LP decoding problem, with objective function value whose distance to the minimum, normalized by the block length, can be made arbitrarily small. It is shown that such a feasible vector can be obtained in linear, in the block length, computational complexity. Combined with previous results, that have shown that the LP decoder can correct some fixed fraction of errors, we conclude that this error correction can be achieved with linear computational complexity.

## New sequences of capacity achieving LDPC code ensembles over the binary erasure channel

- **Status**: ❌
- **Reason**: capacity-achieving LDPC ensembles over BEC; pure asymptotic ensemble theory, no portable decoder/HW/finite-length construction
- **ID**: ieee:4595096
- **Type**: conference
- **Published**: 6-11 July 
- **Authors**: Hamid Saeedi, Amir H. Banihashemi
- **PDF**: https://ieeexplore.ieee.org/document/4595096
- **Abstract**: In this paper, we introduce new sequences (lambdan, rhon) of capacity achieving low-density parity-check (LDPC) code ensembles over the binary erasure channel (BEC). These sequences include the existing sequences by Shokrollahi as a special case. For a fixed code rate R, in the set of proposed sequences, Shokrollahipsilas sequences are superior to the rest of the set in that for any given value of n, their threshold is closer to the capacity upper bound 1 - R. For any given delta, 0 < delta < 1 - R, however, there are infinitely many sequences in the set that are superior to Shokrollahipsilas sequences in that for each of them, there exists an integer number n0, such that for any n > n0, the sequence (lambdan, rhon) requires a smaller maximum variable node degree as well as a smaller number of constituent variable node degrees to achieve a threshold within delta-neighborhood of the capacity upper bound 1 - R. Moreover, we prove that the check-regular subset of the proposed sequences are asymptotically quasi-optimal, i.e., their decoding complexity per iteration increases only logarithmically with the relative increase of the threshold. A stronger result on asymptotic optimality of some of the proposed sequences is also established.

## LDPC convolutional codes based on braided convolutional codes

- **Status**: ✅
- **Reason**: braided convolutional 기반 새 LDPC-CC 구성과 인코딩/디코딩 아키텍처 제시; 코드설계+디코더 이식 가능(E/C).
- **ID**: ieee:4595144
- **Type**: conference
- **Published**: 6-11 July 
- **Authors**: Marcos B.S. Tavares, Michael Lentmaier, Kamil Sh. Zigangirov +1
- **PDF**: https://ieeexplore.ieee.org/document/4595144
- **Abstract**: We introduce and analyze new constructions of LDPC convolutional codes and their tail-biting versions which are obtained from braided convolutional codes. The basic ideas behind the encoding and decoding architectures for these codes are presented. Additionally, asymptotic results concerning the iterative thresholds are shown for different ensembles. Finally, we evaluate the bit error rate performances of several codes by means of computer simulations.

## New construction of LDPC convolutional codes

- **Status**: ✅
- **Reason**: 새 (3,t)-regular LDPC-CC 구성으로 girth>=8 보장 및 error floor 개선; 바이너리 코드설계(E) 이식 가능.
- **ID**: ieee:4595145
- **Type**: conference
- **Published**: 6-11 July 
- **Authors**: Chi-Jen Wu, Yi-Chun Chou, Chung-Hsuan Wang +1
- **PDF**: https://ieeexplore.ieee.org/document/4595145
- **Abstract**: In this paper, we propose a new construction of (3, t)-regular low-density parity-check convolutional codes by properly including binomial entries in the parity-check matrices. Both of the upper and lower bounds on free distance are derived for the new codes. Compared with previous constructions, our design can not only avoid codes of girth less than 8 but also provide enlarged free distances for some code rates. Simulation results show that the codes based on the new construction can achieve better bit-error-rate performance and lower error floor.

## Asymptotic performances of woven graph codes

- **Status**: ❌
- **Reason**: Woven graph codes 점근 최소거리/free distance 이론 bound 분석; 디코더/HW/이식 코드구성 기여 없는 순수 이론.
- **ID**: ieee:4595142
- **Type**: conference
- **Published**: 6-11 July 
- **Authors**: Irina Bocharova, Boris Kudryashov, Rolf Johannesson +1
- **PDF**: https://ieeexplore.ieee.org/document/4595142
- **Abstract**: Constructions of woven graph codes based on constituent block and convolutional codes are studied. It is shown that within the random ensemble of such codes based on s-partite, s-uniform hypergraphs, where s depends only on the code rate, there exist codes satisfying the Varshamov-Gilbert (VG) and the Costello lower bound on the minimum distance and the free distance, respectively.

## Efficient layers-based schedules for iterative decoding of LDPC codes

- **Status**: ✅
- **Reason**: Tanner graph 서브그래프 분할 기반 layered serial 디코딩 스케줄로 복잡도/성능 개선; 디코더 알고리즘(C) 직접 이식 가능.
- **ID**: ieee:4595167
- **Type**: conference
- **Published**: 6-11 July 
- **Authors**: Noam Presman, Eran Sharon, Simon Litsyn
- **PDF**: https://ieeexplore.ieee.org/document/4595167
- **Abstract**: Efficient serial decoding schedules for LDPC codes are described. The schedules are based on dividing the Tanner graph to sub-graphs. This yields an improvement in complexity and performance over the standard schedules. An application of the introduced schedules to decoding codes based on lifted graphs is described. An analysis based on density evolution is presented and is used to predict the behavior of different schedules.

## Asymptotic bit error probability of LDPC codes for the binary erasure channel with finite number of iterations

- **Status**: ✅
- **Reason**: Asymptotic BER of LDPC under BP with finite iterations; finite-length/iteration analysis useful for binary LDPC code design (E).
- **ID**: ieee:4595026
- **Type**: conference
- **Published**: 6-11 July 
- **Authors**: Ryuhei Mori, Kenta Kasai, Tomoharu Shibuya +1
- **PDF**: https://ieeexplore.ieee.org/document/4595026
- **Abstract**: We consider communication over the binary erasure channel (BEC) using low-density parity-check (LDPC) code and belief propagation (BP) decoding. Furthermore, a gap between the bit error probability after finite number of iterations for finite block length n and that for infinite block length is asymptotically α/n, where α denotes a speci..c constant determined by a degree distribution, a number of iterations and erasure probability. Our main result is to derive an ef..cient algorithm for calculating α for regular ensembles.

## A Feedback Belief Propagation Algorithm for LDPC Convolutional Codes

- **Status**: ✅
- **Reason**: LDPC convolutional 부호용 feedback BP 디코딩 알고리즘, 수렴속도 개선 BP 변형으로 이식 가능(C)
- **ID**: ieee:4594966
- **Type**: conference
- **Published**: 6-11 July 
- **Authors**: Yuanhua Liu, Xinmei Wang, Yu-Cheng He
- **PDF**: https://ieeexplore.ieee.org/document/4594966
- **Abstract**: A feedback belief propagation (BP) decoding algorithm for low-density parity-check convolutional codes is proposed. The proposed algorithm can activate the variable nodes more efficiently by applying feedback decoding at each decoding iteration. Compared with the on-demand BP algorithm, the proposed algorithm has a doubled convergence speed and causes only about half of the decoding delay at similar error performances without any increase of storage requirement. Simulation results show that the proposed algorithm can offer a good trade-off between the error-correcting performance and the decoding complexity.

## LDPC codes from voltage graphs

- **Status**: ✅
- **Reason**: E: new structure-based binary QC-LDPC construction via voltage graphs, cycle classification (Abelian-inevitable cycles), portable code design
- **ID**: ieee:4595095
- **Type**: conference
- **Published**: 6-11 July 
- **Authors**: Christine A. Kelley, Judy L. Walker
- **PDF**: https://ieeexplore.ieee.org/document/4595095
- **Abstract**: Several well-known structure-based constructions of LDPC codes, for example codes based on permutation and circulant matrices and in particular, quasi-cyclic LDPC codes, can be interpreted via algebraic voltage assignments. We explain this connection and show how this idea from topological graph theory can be used to give simple proofs of many known properties of these codes. In addition, the notion of Abelian-inevitable cycle is introduced and the subgraphs giving rise to these cycles are classified. We also indicate how, by using more sophisticated voltage assignments, new classes of good LDPC codes may be obtained.

## Error floors in LDPC codes: Fast simulation, bounds and hardware emulation

- **Status**: ✅
- **Reason**: Error floor prediction via absorbing sets with hardware emulation for finite-length LDPC; transferable code-design/HW insight (E/D).
- **ID**: ieee:4595025
- **Type**: conference
- **Published**: 6-11 July 
- **Authors**: Pamela Lee, Lara Dolecek, Zhengya Zhang +3
- **PDF**: https://ieeexplore.ieee.org/document/4595025
- **Abstract**: The error-correcting performance of low-density parity check (LDPC) codes, when decoded using practical iterative decoding algorithms, is known to be very close to Shannon limits in the asymptotic limit of large blocklengths. A substantial limitation to the use of finite-length LDPC codes is the presence of an error floor in the low frame error rate (FER) region. This paper develops two methods, a stochastic one based on importance sampling and a deterministic one based on high SNR asymptotics, as applied to suitably defined absorbing structures within the LDPC code, to predict error floors. Our results are in very close agreement with hardware-based experimental results, and moreover extend the prediction of the error probability to as low as 10-30. Our deterministic estimates are guaranteed to be a lower bound to the error probability in the high SNR regime.

## Generalized low-density codes with BCH constituents for full-diversity near-outage performance

- **Status**: ❌
- **Reason**: GLD codes with BCH constituents for block fading/erasure outage; non-LDPC BCH-based, application-specific full-diversity, no portable binary LDPC ECC technique
- **ID**: ieee:4595094
- **Type**: conference
- **Published**: 6-11 July 
- **Authors**: Joseph J. Boutros, Gilles Zemor, Albert Guillen i Fabregas +1
- **PDF**: https://ieeexplore.ieee.org/document/4595094
- **Abstract**: A new graph-based construction of generalized low density codes (GLD-Tanner) with binary BCH constituents is described. The proposed family of GLD codes is optimal on block erasure channels and quasi-optimal on block fading channels. Optimality is considered in the outage probability sense. A classical GLD code for ergodic channels (e.g., the AWGN channel, the i.i.d. Rayleigh fading channel, and the i.i.d. binary erasure channel) is built by connecting bitnodes and subcode nodes via a unique random edge permutation. In the proposed construction of full-diversity GLD codes (referred to as root GLD), bitnodes are divided into 4 classes, subcodes are divided into 2 classes, and finally both sides of the Tanner graph are linked via 4 random edge permutations. The study focuses on non-ergodic channels with two states and can be easily extended to channels with 3 states or more.

## On the guaranteed error correction capability of LDPC codes

- **Status**: ✅
- **Reason**: Girth vs guaranteed error correction of regular LDPC under bit-flipping, trapping set bounds; transferable code-design/decoding insight (E/C).
- **ID**: ieee:4595023
- **Type**: conference
- **Published**: 6-11 July 
- **Authors**: Shashi Kiran Chilappagari, Dung Viet Nguyen, Bane Vasic +1
- **PDF**: https://ieeexplore.ieee.org/document/4595023
- **Abstract**: We investigate the relation between the girth and the guaranteed error correction capability of gamma-left regular LDPC codes when decoded using the bit flipping (serial and parallel) algorithms. A lower bound on the number of variable nodes which expand by a factor of at least 3gamma/4 is found based on the Moore bound. An upper bound on the guaranteed correction capability is established by studying the sizes of smallest possible trapping sets.

## Self-corrected Min-Sum decoding of LDPC codes

- **Status**: ✅
- **Reason**: self-corrected min-sum 디코딩, 부호 비의존적 min-sum 변형으로 NAND LDPC 디코더에 직접 이식 가능(C)
- **ID**: ieee:4594965
- **Type**: conference
- **Published**: 6-11 July 
- **Authors**: Valentin Savin
- **PDF**: https://ieeexplore.ieee.org/document/4594965
- **Abstract**: In this paper we propose a very simple but powerful self-correction method for the min-sum decoding of LPDC codes. Unlike other correction methods known in the literature, our method does not try to correct the check node processing approximation, but it modifies the variable node processing by erasing unreliable messages. However, this positively affects check node messages, which become symmetric Gaussian distributed, and we show that this is sufficient to ensure a quasi-optimal decoding performance. Monte-Carlo simulations show that the proposed self-corrected min-sum decoding performs very close to the sum-product decoding, while preserving the main features of the min-sum decoding, that is low complexity and independence with respect to noise variance estimation errors.

## Split non-binary LDPC codes

- **Status**: ❌
- **Reason**: Split non-binary LDPC codes over GF(2^p); non-binary, excluded
- **ID**: ieee:4595128
- **Type**: conference
- **Published**: 6-11 July 
- **Authors**: Adrian Voicila, David Declercq, Francois Verdier +2
- **PDF**: https://ieeexplore.ieee.org/document/4595128
- **Abstract**: In this paper, we propose and study a new family of error-correcting codes. These achieve excellent error performance under an iterative decoding over the binary-input noisy channel and solves the memory space requirements problem of the non-binary LDPC decoders. We named this class of codes, Split non-binary LDPC codes. The main particularity of this new family of codes is that the variable and the check nodes are not defined over the same finite field GF(2p), like in the case of classical non-binary LDPC codes. The class of Split non-binary LDPC codes is obviously larger than that of existing types of codes, which gives more degrees of freedom to find good codes when the existing codes show their limits. We provide two examples of interesting split NB-LDPC codes.

## Feature extraction for a Slepian-Wolf biometric system using LDPC codes

- **Status**: ❌
- **Reason**: Slepian-Wolf 바이오메트릭 보안저장(syndrome coding), 채널 ECC 아닌 소스/보안 응용, 표준 LDPC 사용
- **ID**: ieee:4595400
- **Type**: conference
- **Published**: 6-11 July 
- **Authors**: Yagiz Sutcu, Shantanu Rane, Jonathan S. Yedidia +2
- **PDF**: https://ieeexplore.ieee.org/document/4595400
- **Abstract**: We present an information-theoretically secure biometric storage system using graph-based error correcting codes in a Slepian-Wolf coding framework. Our architecture is motivated by the noisy nature of personal biometrics and the requirement to provide security without storing the true biometric at the device. The principal difficulty is that real biometric signals, such as fingerprints, do not obey the i.i.d. or ergodic statistics that are required for the underlying typicality properties in the Slepian-Wolf coding framework. To meet this challenge, we propose to transform the biometric data into binary feature vectors that are i.i.d. Bernoulli(0.5), independent across different users, and related within the same user through a BSC-p channel with small p< 0.5. Since this is a standard channel model for LDPC codes, the feature vectors are now suitable for LDPC syndrome coding. The syndromes serve as secure biometrics for access control. Experiments on a fingerprint database demonstrate that the system is information-theoretically secure, and achieves very low false accept rates and low false reject rates.

## Cointegrated vector autoregressive models for multitrack systems in digital magnetic recording

- **Status**: ❌
- **Reason**: 자기기록 멀티트랙 신호검출(VAR/MAP)이 핵심, LDPC는 표준 부수 사용으로 떼어낼 ECC 기법 없음
- **ID**: ieee:4595187
- **Type**: conference
- **Published**: 6-11 July 
- **Authors**: Hidetoshi Saito, Masayuki Hayashi, Ryuji Kohno
- **PDF**: https://ieeexplore.ieee.org/document/4595187
- **Abstract**: A number of multitrack recording systems with multiple-head arrays have been developed for the future high density magnetic recoding systems. In this recording system, the signal detection scheme is needed to estimate the received sequence with media noise, intersymbol interference and inter-track interference. From the recent trend of high density magnetic recording, it is indispensable for any signal processing scheme to mitigate or reduce the effect of media noise such as mixture signal-dependent transition noise and colored Gaussian thermal noise. This paper proposes the statistical inference using the cointegrated process based on vector autoregressive (VAR) models for such a finite mixture of known number of noise and interference components. Our signal detection scheme is applied to maximum a posteriori (MAP) detection with the cointegrated VAR processes. Furthermore, a high rate low-density parity-check (LDPC) code is used for the error correcting code which satisfies the specific run-length limited condition in the proposed multitrack recording system. We show that the proposed multi-track system of error correcting and signal detection scheme is effective to estimate degraded signal sequences and improve the error rate performances with respect to the conventional multitrack system which has the LDPC coding scheme and MAP detector employing the BCJR algorithm.

## Detailed evolution of degree distributions in residual graphs with joint degree distributions

- **Status**: ❌
- **Reason**: BEC 유한길이 잔여그래프 차수분포 진화의 순수 이론 분석, 디코더/HW/구성으로 안 이어짐
- **ID**: ieee:4595225
- **Type**: conference
- **Published**: 6-11 July 
- **Authors**: Takayuki Nozaki, Kenta Kasai, Tomoharu Shibuya +1
- **PDF**: https://ieeexplore.ieee.org/document/4595225
- **Abstract**: Luby et al. derived evolution of degree distributions in residual graphs for irregular LDPC code ensembles. Evolution of degree distributions in residual graphs is an important characteristic which is used for finite-length analysis of the expected block and bit error probabilities over the binary erasure channel. In this paper, we derive detailed evolution of degree distributions in residual graphs for irregular LDPC code ensembles with joint degree distributions.

## Error rate estimation of finite-length low-density parity-check codes decoded by soft-decision iterative algorithms

- **Status**: ✅
- **Reason**: Error-rate estimation of finite-length LDPC under quantized soft-decision iterative decoding incl error floor; directly relevant (E, quantization).
- **ID**: ieee:4595024
- **Type**: conference
- **Published**: 6-11 July 
- **Authors**: Hua Xiao, Amir H. Banihashemi
- **PDF**: https://ieeexplore.ieee.org/document/4595024
- **Abstract**: This paper describes a combinatorial approach to estimate the error rate performance of low-density parity-check (LDPC) codes decoded by (quantized) soft-decision iterative decoding algorithms. The method is based on efficient enumeration of input vectors with small distances to a reference vector whose elements are selected to be the most reliable values from the input alphabet. Several techniques, including modified cycle enumeration, are employed to reduce the complexity of the enumeration. The error rate estimate is derived by testing the input vectors of small distances and estimating the contribution of larger distance vectors. We demonstrate by a number of examples that the proposed method provides accurate estimates of error rate with computational complexity much lower than that of Monte Carlo simulations, especially at the error floor region.

## On the code reverse engineering problem

- **Status**: ❌
- **Reason**: Code reverse engineering / eavesdropping bound for LDPC; security-oriented theory bound, no transferable decoder/HW/design technique.
- **ID**: ieee:4595063
- **Type**: conference
- **Published**: 6-11 July 
- **Authors**: Mathieu Cluzeau, Jean-Pierre Tillich
- **PDF**: https://ieeexplore.ieee.org/document/4595063
- **Abstract**: This article deals with the problem of quantifying how many noisy codewords have to be eavesdropped in order to reverse engineer a code. The main result of this paper is a lower bound on this quantity and the proof that this number is logarithmic in the length for LDPC codes.

## Finite-length scaling of parallel turbo codes on the BEC

- **Status**: ❌
- **Reason**: turbo 부호의 BEC 유한길이 스케일링 이론(파라미터 도출), 떼어낼 디코더/HW/구성 기법 없음, 순수 bound
- **ID**: ieee:4595317
- **Type**: conference
- **Published**: 6-11 July 
- **Authors**: Iryna Andriyanova
- **PDF**: https://ieeexplore.ieee.org/document/4595317
- **Abstract**: In this paper we consider the finite-length performance of turbo codes in the waterfall region assuming the transmission on the binary erasure channel. We extend the finite-length scaling law of LDPC codes and of repeat-accumulate codes to this ensemble and we derive the scaling parameter. The obtained performance estimations match very well with numerical results.

## Interior point decoding for linear vector channels based on convex optimization

- **Status**: ✅
- **Reason**: 볼록최적화 기반 interior point 디코더(C), 바이너리 LDPC ISI/PR 채널 디코더로 이식 가능
- **ID**: ieee:4595236
- **Type**: conference
- **Published**: 6-11 July 
- **Authors**: Tadashi Wadayama
- **PDF**: https://ieeexplore.ieee.org/document/4595236
- **Abstract**: In this paper, a novel decoding algorithm for low-density parity-check (LDPC) codes based on convex optimization is presented. The decoding algorithm, called interior point decoding, is designed for linear vector channels. The linear vector channels include many practically important channels such as inter symbol interference channels, partial response channels and MIMO channels. It is shown that the maximum likelihood decoding (MLD) rule for a linear vector channel can be relaxed to a convex optimization problem, which is called a relaxed MLD problem. Approximate variations of gradient descent and Newton methods are used to solve the convex optimization problem.

## Bounds on the number of iterations for turbo-like code ensembles over the binary erasure channel

- **Status**: ❌
- **Reason**: BEC 반복횟수 하한 점근 이론 bound, LDPC 디코더/구성으로 안 이어짐
- **ID**: ieee:4595318
- **Type**: conference
- **Published**: 6-11 July 
- **Authors**: Igal Sason, Gil Wiechman
- **PDF**: https://ieeexplore.ieee.org/document/4595318
- **Abstract**: We derive simple lower bounds on the number of iterations which are required to communicate over the binary erasure channel when graph-based code ensembles are used in conjunction with an iterative message-passing decoder. These bounds refer to the asymptotic case where we let the block length tend to infinity, and the bounds apply to general ensembles of low- density parity-check (LDPC) codes, irregular repeat-accumulate (IRA) and accumulate-repeat-accumulate (ARA) codes. It is demonstrated that, under a mild condition, the number of iterations required for successful decoding scales at least like the inverse of the gap (in rate) to capacity.

## Convolutional Tanner structures for non-ergodic wireless channels

- **Status**: ❌
- **Reason**: 무선 비-에르고딕 채널용 convolutional Tanner 구성, NAND에 떼어낼 바이너리 코드설계 기여 없음
- **ID**: ieee:4595170
- **Type**: conference
- **Published**: 6-11 July 
- **Authors**: Joseph J. Boutros, Emanuele Viterbo, Gerard Cohen
- **PDF**: https://ieeexplore.ieee.org/document/4595170
- **Abstract**: We propose an original technique for the design of convolutional Tanner structures that are full diversity under iterative decoding. The code design is based on the analysis of the local trellis neighborhood and is suitable for transmission over wireless non-ergodic channels. This new technique enables us to split the giant convolutional checknode into multiple smaller checknodes which is a means to mimic the standard analysis of LDPC codes under iterative message passing decoding.

## Asymmetric quantum LDPC codes

- **Status**: ❌
- **Reason**: Asymmetric quantum stabilizer (CSS) LDPC codes; depends on quantum stabilizer/CSS, not transferable to classical binary LDPC.
- **ID**: ieee:4594997
- **Type**: conference
- **Published**: 6-11 July 
- **Authors**: Pradeep Kiran Sarvepalli, Andreas Klappenecker, Martin Rotteler
- **PDF**: https://ieeexplore.ieee.org/document/4594997
- **Abstract**: Recently, quantum error-correcting codes were proposed that capitalize on the fact that many physical error models lead to a significant asymmetry between the probabilities for bit flip and phase flip errors. An example for a channel which exhibits such asymmetry is the combined amplitude damping and dephasing channel, where the probabilities of bit flips and phase flips can be related to relaxation and dephasing time, respectively. We give systematic constructions of asymmetric quantum stabilizer codes that exploit this asymmetry. Our approach is based on a CSS construction that combines BCH and finite geometry LDPC codes.

## Quantum serial turbo-codes

- **Status**: ❌
- **Reason**: Quantum serial turbo-codes relying on degeneracy and quantum convolutional encoders; quantum-specific, non-LDPC, not transferable.
- **ID**: ieee:4594998
- **Type**: conference
- **Published**: 6-11 July 
- **Authors**: David Poulin, Jean-Pierre Tillich, Harold Ollivier
- **PDF**: https://ieeexplore.ieee.org/document/4594998
- **Abstract**: We present a theory of quantum serial turbo-codes and study their performance numerically on a depolarization channel. These codes can be considered as a generalization of classical serial turbo-codes. As their classical cousins, they can be iteratively decoded and with well chosen constituent convolutional codes, we observe an important reduction of the word error rate as the number of encoded qubits increases. Our construction offers several advantages over quantum LDPC codes. First, the Tanner graph used for decoding can be chosen to be free of 4-cycles that deteriorate the performances of iterative decoding. Secondly, the iterative decoder makes explicit use of the code's degeneracy. Finally, there is complete freedom in the code design in terms of length, rate, memory size, and interleaver choice. We address two issues related to the encoding of convolutional codes that are directly relevant for turbo-codes, namely the character of being recursive and non-catastrophic. We define a quantum analogue of a state diagram that provides an efficient way to verify these properties on a given quantum convolutional encoder. Unfortunately, we also prove that all recursive quantum convolutional encoder have catastrophic error propagation. In our constructions, the convolutional codes have thus been chosen to be non-catastrophic and non-recursive. While the resulting families of turbo-codes have bounded minimum distance, from a pragmatic point of view the effective minimum distances of the codes that we have simulated are large enough for not degrading iterative decoding performance up to reasonable word error rates and block sizes.

## Tight upper and lower bounds on the constrained capacity of non-coherent multi-antenna channels

- **Status**: ❌
- **Reason**: 비코히어런트 다중안테나 채널 용량 bound, LDPC는 효율 판단 기준 언급뿐 떼어낼 기법 없음
- **ID**: ieee:4595459
- **Type**: conference
- **Published**: 6-11 July 
- **Authors**: Krishnan Padmanabhan, Sundeep Venkatraman, Oliver M. Collins
- **PDF**: https://ieeexplore.ieee.org/document/4595459
- **Abstract**: This paper first presents an optimal receiver and coding scheme for a multi-user, multi-receiver, non-coherent Rayleigh flat fading channel which achieves the channel's constrained capacity (i.e., the capacity for a fixed input distribution). The paper then goes on to analyze the optimal receiver and uses it to generate tight upper and lower bounds on the constrained capacity. Knowing this constrained capacity is essential to judge the efficiency of coding schemes for the channel; it performs the same function as BPSK capacity for the AWGN channel in judging LDPC codes. The paper then goes on to present a practicable correlation based receiver that uses a novel iterative channel estimation technique. The performance of this receiver remains close to the constrained capacity as long as the per-user SNR is low; there is no requirement on the aggregate SNR. With 50 users, 50 receivers and a brickwall fading channel with a coherence length of 200 symbols, for example, the correlation based receiver achieves a sum rate of 36 bits/sec/Hz, significantly greater than any current cellular standards.

## Shannon bounds on the throughput for Gaussian, bi-level, block interference channels

- **Status**: ❌
- **Reason**: 블록간섭 채널 용량 bound·throughput 분석, turbo-product/LDPC는 부수 언급, 떼어낼 디코더·구성 기법 없음
- **ID**: ieee:4595427
- **Type**: conference
- **Published**: 6-11 July 
- **Authors**: Michael B. Pursley, Thomas C. Royster
- **PDF**: https://ieeexplore.ieee.org/document/4595427
- **Abstract**: Results are presented on code performance and capacity bounds for channels with Gaussian, bi-level, block interference for binary and nonbinary modulation, noncoherent demodulation, and soft-decision decoding. Each transmitted block is corrupted by additive white Gaussian noise that has one of two power spectral densities. The smaller of the two is the power spectral density of the thermal noise, and the difference between the two spectral densities is the power spectral density of the interference noise. The average power in the interference is constant, so the power spectral density of the interference is inversely proportional to the average fraction of the blocks that have interference. This block interference channel has been used to model partial-band interference in frequency-hop communications and to model pulsed interference in a number of communication systems. Throughput results for turbo-product and low-density parity-check codes that are used on Gaussian block interference channels are compared with the capacity bounds for such channels. For some code rates, we show that the throughput of the codes and the capacity bounds are both nonmonotonic functions of the fraction of the blocks that have interference. Applications to adaptive-rate coding are discussed.

## On undetected error probability of binary matrix ensembles

- **Status**: ❌
- **Reason**: 바이너리 행렬 앙상블의 undetected error probability 이론(에러지수/분산) 분석; 디코더/HW/구성 이식 기여 없음.
- **ID**: ieee:4595146
- **Type**: conference
- **Published**: 6-11 July 
- **Authors**: Tadashi Wadayama
- **PDF**: https://ieeexplore.ieee.org/document/4595146
- **Abstract**: In this paper, an analysis of the undetected error probability of ensembles of m × n binary matrices is presented. The ensemble called the Bernoulli ensemble whose members are considered as matrices generated from i.i.d. Bernoulli source is mainly considered here. The main contributions of this work are (i) derivation of the error exponent of the average undetected error probability and (ii) closed form expressions for the variance of the undetected error probability. It is shown that the behavior of the exponent for a sparse ensemble is somewhat different from that for a dense ensemble. Furthermore, as a byproduct of the proof of the variance formula, simple covariance formula of the weight distribution is derived.

## Codeword-independent performance of nonbinary linear codes under linear-programming and sum-product decoding

- **Status**: ❌
- **Reason**: 비이진 선형부호의 LP/SP 디코딩 코드워드 독립 성능 증명, 비이진 대상이라 제외
- **ID**: ieee:4595238
- **Type**: conference
- **Published**: 6-11 July 
- **Authors**: Mark F. Flanagan
- **PDF**: https://ieeexplore.ieee.org/document/4595238
- **Abstract**: A coded modulation system is considered in which nonbinary coded symbols are mapped directly to nonbinary modulation signals. It is proved that if the modulator-channel combination satisfies a particular symmetry condition, the codeword error rate performance is independent of the transmitted codeword. It is shown that this result holds for both linear-programming decoders and sum-product decoders. In particular, this provides a natural modulation mapping for nonbinary codes mapped to PSK constellations for transmission over memoryless channels such as AWGN channels or flat fading channels with AWGN.

## Performance—complexity tradeoffs of rateless codes

- **Status**: ❌
- **Reason**: rateless/raptor 부호 성능-복잡도 트레이드오프, LDPC ECC 이식 기법 없음
- **ID**: ieee:4595351
- **Type**: conference
- **Published**: 6-11 July 
- **Authors**: Dohyung Park, Sae-Young Chung
- **PDF**: https://ieeexplore.ieee.org/document/4595351
- **Abstract**: We analyze performance-complexity tradeoffs of rateless codes over noisy symmetric channels. Unlike in erasure channels, the decoder for such codes needs to use all received symbols in noisy channels because each of them have some information about the transmitted message. To reduce the complexity, the receiver can discard some unreliable symbols, but it must receive more symbols due to the lost information. This results in a performance-complexity tradeoff. We also consider another scenario where a rateless code is concatenated with a fixed-rate code, which is typically used in practice, e.g., in [1]. The fixed-rate code provides a soft-decision decoding and only correctly decoded blocks are used in the rateless code decoder. If some soft information of error-detected blocks is also used, the receiver can decode the message with less received symbols at the expense of increased processing. This results in another type of performance-complexity tradeoff. For these scenarios, we find the optimal tradeoffs and show sub-optimal tradeoffs achievable by practical rateless codes.

## Polytope representations for linear-programming decoding of non-binary linear codes

- **Status**: ❌
- **Reason**: 비이진 선형부호 LP 디코딩 폴리토프 표현, 비이진 대상이라 제외
- **ID**: ieee:4595239
- **Type**: conference
- **Published**: 6-11 July 
- **Authors**: Vitaly Skachek, Mark F. Flanagan, Eimear Byrne +1
- **PDF**: https://ieeexplore.ieee.org/document/4595239
- **Abstract**: In previous work, we demonstrated how decoding of a non-binary linear code could be formulated as a linear-programming problem. In this paper, we study different polytopes for use with linear-programming decoding, and show that for many classes of codes these polytopes yield a complexity advantage for decoding. These representations lead to polynomial-time decoders for a wide variety of classical non-binary linear codes.

## Gaussian belief propagation solver for systems of linear equations

- **Status**: ❌
- **Reason**: 선형방정식 풀이용 Gaussian BP 솔버(CDMA decorrelation 응용), LDPC 채널 디코더 기법 아님
- **ID**: ieee:4595311
- **Type**: conference
- **Published**: 6-11 July 
- **Authors**: Ori Shental, Paul H. Siegel, Jack K. Wolf +2
- **PDF**: https://ieeexplore.ieee.org/document/4595311
- **Abstract**: The canonical problem of solving a system of linear equations arises in numerous contexts in information theory, communication theory, and related fields. In this contribution, we develop a solution based upon Gaussian belief propagation (GaBP) that does not involve direct matrix inversion. The iterative nature of our approach allows for a distributed message-passing implementation of the solution algorithm. We also address some properties of the GaBP solver, including convergence, exactness, its max-product version and relation to classical solution methods. The application example of decorrelation in CDMA is used to demonstrate the faster convergence rate of the proposed solver in comparison to conventional linear-algebraic iterative solution methods.

## Message-passing decoding of lattices using Gaussian mixtures

- **Status**: ❌
- **Reason**: low-density lattice code의 가우시안 혼합 BP, 연속 lattice 전용이라 바이너리 NAND LDPC에 이식 부적합
- **ID**: ieee:4595439
- **Type**: conference
- **Published**: 6-11 July 
- **Authors**: Brian Kurkoski, Justin Dauwels
- **PDF**: https://ieeexplore.ieee.org/document/4595439
- **Abstract**: A belief-propagation decoder for low-density lattice codes, which represents messages explicitly as a mixture of Gaussians functions, is given. In order to prevent the number of functions from growing as the decoder iterations progress, a method for reducing the number of Gaussians at each step is given. A squared distance metric is used, which is shown to be a lower bound on the divergence. For an unconstrained power system, comparisons are made with a quantized implementation. For a dimension 100 lattice, a loss of about 0.2 dB was found; for dimension 1000 and 10000 lattices, the difference in error rate was indistinguishable. The memory required to store the messages is substantially superior to the quantized implementation.

## Physical-layer encryption with stream ciphers

- **Status**: ❌
- **Reason**: 물리계층 암호(stream cipher), 보안 응용으로 원칙 제외, 떼어낼 디코더·구성 기법 없음
- **ID**: ieee:4594957
- **Type**: conference
- **Published**: 6-11 July 
- **Authors**: Andre Zuquete, Joao Barros
- **PDF**: https://ieeexplore.ieee.org/document/4594957
- **Abstract**: Contemporary communication systems are based on modular architectures, where the role of the physical layer is essentially confined to error correction, whereas information security is typically dealt with at the upper layers of the protocol stack. We consider a security architecture that does exactly the opposite: information sequences are first converted to longer channel codewords which are then encrypted using a classical stream cipher. Although this approach requires longer encryption sequences, our analysis shows that the natural randomness of the noisy communication channel can be used effectively against known-plaintext attacks. We also address practical implementation issues in physical-layer encryption and discuss their impact on the system architecture and on the security performance.

## Separating erasures from errors for decoding

- **Status**: ❌
- **Reason**: erasure/error 분리용 패리티검사 행렬 구성, erasure 채널 중심 이론으로 NAND 바이너리 LDPC ECC로 떼어낼 신규 기법 부족
- **ID**: ieee:4594979
- **Type**: conference
- **Published**: 6-11 July 
- **Authors**: Khaled A.S. Abdel-Ghaffar, Jos H. Weber
- **PDF**: https://ieeexplore.ieee.org/document/4594979
- **Abstract**: Most decoding algorithms of linear codes, in general, are designed to correct or detect errors. However, many channels cause erasures in addition to errors. In principle, decoding over such channels can be accomplished by deleting the erased symbols and decoding the resulting vector with respect to a punctured code. For any given linear code and any given maximum number of correctable erasures, we introduce parity-check matrices yielding parity-check equations that do not check any of the erased symbols and which are sufficient to characterize all punctured codes corresponding to this maximum number of erasures. This allows for the separation of erasures from errors to facilitate decoding. The parity-check matrices typically have redundant rows. We give several constructions of such matrices and prove general bounds on their minimum sizes.

## Multidimensional reconciliation for continuous-variable quantum key distribution

- **Status**: ❌
- **Reason**: CV-QKD reconciliation via octonions; QKD information reconciliation, not channel ECC, no portable LDPC decoder/HW technique
- **ID**: ieee:4595141
- **Type**: conference
- **Published**: 6-11 July 
- **Authors**: Anthony Leverrier, Romain Alleaume, Joseph Boutros +2
- **PDF**: https://ieeexplore.ieee.org/document/4595141
- **Abstract**: We propose a method for extracting an errorless secret key in a continuous-variable quantum key distribution protocol, which is based on Gaussian modulation of coherent states and homodyne detection. The crucial feature is an eight-dimensional reconciliation method, relying on the algebraic properties of octonions. By using this coding scheme with an appropriate signal-to-noise ratio, the distance for secure continuous-variable quantum key distribution can be significantly extended.

## Rateless coding for quasi-static fading channels using channel estimation accuracy

- **Status**: ❌
- **Reason**: Raptor/rateless 페이딩채널 적응, LLR 정의 외 이식할 LDPC 디코더/HW/구성 없음
- **ID**: ieee:4595392
- **Type**: conference
- **Published**: 6-11 July 
- **Authors**: Auguste Venkiah, Pablo Piantanida, Charly Poullia +2
- **PDF**: https://ieeexplore.ieee.org/document/4595392
- **Abstract**: The design of efficient rateless coding schemes for multicast applications in wireless environments is investigated. First, the rateless paradigm for non-ergodic channels is introduced by making use of the dynamic-decoding nature of rateless codes that allows them to adapt opportunistically the code rate to the channel realization (assumed unknown at the transmitter). The information theoretical limits of such codes can be interpreted in terms of the notion of outage capacity. Then, we consider a quasi-static Rayleigh-fading channel with perfect and imperfect channel state information (CSI) at the receiver. We show that the optimal consistent measure of information for decoding with imperfect CSI, is given by the log-likelihood ratio (LLR) of the received bits via a composite (more noisy) channel. The optimization of Raptor codes, which depends on the delay requirements of decoding, is obtained by using Information content evolution under Gaussian approximation. Simulation results show that optimized Raptor codes can operate very close to the theoretical limits on a wide range of delay requirements.

## Joint source-channel coding with inner irregular codes

- **Status**: ❌
- **Reason**: JSCC(소스-채널 결합) 최적화로 LDPC가 베이스라인, 떼어낼 NAND ECC 기법 없음
- **ID**: ieee:4595168
- **Type**: conference
- **Published**: 6-11 July 
- **Authors**: Ragnar Thobaben, Laurent Schmalen, Peter Vary
- **PDF**: https://ieeexplore.ieee.org/document/4595168
- **Abstract**: We address the optimization of joint source-channel coding schemes for iterative source-channel decoding of first- order Markov sources. Compared to the traditional design, we propose two novelties: (1) source encoders, providing code words with a minimum Hamming distance dminges2, realized by linear block codes, and (2) irregular channel encoders which are optimized for both the source characteristics and the conditions on the channel. Inner code rates RC > 1 may be chosen in order to compensate for the additional source redundancy if required. Design examples for the AWGN channel and an overall code rate R=0.66 show that the proposed system is able to establish reliable communication within 0.3 dB of the capacity limit for an interleaver length of approximatively 200000 bits.

## Unequal error protection multilevel codes and hierarchical modulation for multimedia transmission

- **Status**: ❌
- **Reason**: 멀티레벨 코딩+계층변조 UEP 멀티미디어 전송, LDPC 디코더/구성 기여 없음
- **ID**: ieee:4595388
- **Type**: conference
- **Published**: 6-11 July 
- **Authors**: Neele von Deetzen, Werner Henkel
- **PDF**: https://ieeexplore.ieee.org/document/4595388
- **Abstract**: This paper presents the design of multilevel coding schemes optimized for the transport of multimedia data. The key feature is unequal error protection which allows for more protection for header information and essential data, accepting worse performance for less important payload. The approach is based on the information theoretical description of mutual information in multilevel coding schemes. We discuss the suitability and UEP capability of standard as well as non-uniform signal constellations. We investigate the flexibility of this method regarding the design freedom and verify the approach by an image transmission application.

## Coding for the q-ary symmetric channel with moderate q

- **Status**: ✅
- **Reason**: 표준 바이너리 LDPC 디코딩을 단순 수정해 q-ary 대칭채널에 적용하는 실용 디코더 변형, BP 이식 검토 여지(C, 애매하면 in)
- **ID**: ieee:4595371
- **Type**: conference
- **Published**: 6-11 July 
- **Authors**: Claudio Weidmann
- **PDF**: https://ieeexplore.ieee.org/document/4595371
- **Abstract**: We study coding schemes for the q-ary symmetric channel with moderate alphabet sizes q that are much smaller than the q = 2256 considered as ldquoentry levelrdquo in some recently proposed packet-based schemes. First, we show theoretical optimality of a simple layered scheme, then we propose a practical coding scheme based on a simple modification of standard binary LDPC decoding.

## Bounds on rates of LDPC codes for BEC with varying erasure rate

- **Status**: ❌
- **Reason**: BEC 가변 erasure rate 하 LDPC 설계레이트 상한 bound; 순수 이론, 떼어낼 디코더/HW/구성 없음.
- **ID**: ieee:4595164
- **Type**: conference
- **Published**: 6-11 July 
- **Authors**: Ohad Barak, Uri Erez, David Burshtein
- **PDF**: https://ieeexplore.ieee.org/document/4595164
- **Abstract**: A binary erasure channel with erasure probability which can take one of two values is considered. Transmission is done by using a low density parity-check code under the requirement that completely successful decoding is possible when the channel is in its better state, while tolerating some predetermined residual erasure fraction when the channel is in its worse state. Upper bounds on the achievable design rate under iterative decoding are derived for this setting. These bounds are compared to rates obtained by practical code profiles. It is also observed that when exceeding the capacity of the erasure channel, the performance of such codes exhibits graceful degradation as measured by the residual erasure fraction.

## Near ML detection using Dijkstra’s algorithm with bounded list size over MIMO channels

- **Status**: ❌
- **Reason**: MIMO 신호검출(Dijkstra near-ML), LDPC 부호와 무관한 통신 응용 검출기
- **ID**: ieee:4595344
- **Type**: conference
- **Published**: 6-11 July 
- **Authors**: Atsushi Okawado, Ryutaroh Matsumoto, Tomohiko Uyematsu
- **PDF**: https://ieeexplore.ieee.org/document/4595344
- **Abstract**: We propose Dijkstra’s algorithm with bounded list size after QR decomposition for decreasing the computational complexity of near maximum-likelihood (ML) detection of signals over multiple-input-multiple-output (MIMO) channels. After that, we compare the performances of proposed algorithm, QR decomposition M-algorithm (QRM-MLD), and its improvement. When the list size is set to achieve the almost same symbol error rate (SER) as the QRM-MLD, the proposed algorithm has smaller average computational complexity.

## Cryptographic primitives based on discrete-input AWGN channels

- **Status**: ❌
- **Reason**: Cryptographic commitment/oblivious transfer over AWGN; security primitives, not channel ECC, no LDPC technique.
- **ID**: ieee:4595084
- **Type**: conference
- **Published**: 6-11 July 
- **Authors**: Motohiko Isaka, Yuki Shimizu
- **PDF**: https://ieeexplore.ieee.org/document/4595084
- **Abstract**: Two cryptographic primitives, commitment and oblivious transfer, are devised based on the additive white Gaussian noise channel and discrete input alphabet. We present protocols and analyze the security and information theoretic efficiencies.

## Codes on hypergraphs

- **Status**: ❌
- **Reason**: 하이퍼그래프 부호의 가중치분포·최소거리·반복디코딩, 일반 부호족 이론으로 바이너리 LDPC BP에 직접 이식할 신규 디코더 기법 불명확하나 도메인 일반 이론 bound 성격
- **ID**: ieee:4594967
- **Type**: conference
- **Published**: 6-11 July 
- **Authors**: Alexander Barg, Gilles Zemor
- **PDF**: https://ieeexplore.ieee.org/document/4594967
- **Abstract**: A generalization of codes on regular bipartite graphs is given by a family of codes on hypergraphs. We derive the average weight distribution and estimate the minimum distance of codes in the random ensemble of hypergraph codes. We also propose an iterative decoding algorithm of hypergraph codes that corrects a larger proportion of errors than known previously for this code family.

## Fountain codes for piecewise stationary channels

- **Status**: ❌
- **Reason**: fountain/LT 부호, 소스코딩 기반 incremental 디코딩, 떼어낼 LDPC ECC 기법 없음
- **ID**: ieee:4595389
- **Type**: conference
- **Published**: 6-11 July 
- **Authors**: Bertrand Ndzana Ndzana, Andrew W. Eckford, M. Amin Shokrollahi +1
- **PDF**: https://ieeexplore.ieee.org/document/4595389
- **Abstract**: In this paper, two fixed per-information symbol complexity lossless source coding algorithms are modified for estimation and incremental LT decoding over Piecewise Stationary Memoryless Channels (PSMC’s) with a bounded number of abrupt changes in channel statistics. In particular, as a class of PSMC’s, binary symmetric channels are considered with a crossover probability that changes a bounded number of times with no repetitions in the statistics. Simulation results are given which illustrate the benefits of using our algorithms, both in terms of probability of error and in terms of redundancy.

## Exchange of limits: Why iterative decoding works

- **Status**: ❌
- **Reason**: 순수 이론, density evolution 한계의 limit 교환 증명으로 디코더/HW/구성으로 안 이어짐
- **ID**: ieee:4594993
- **Type**: conference
- **Published**: 6-11 July 
- **Authors**: Satish Babu Korada, Rudiger Urbanke
- **PDF**: https://ieeexplore.ieee.org/document/4594993
- **Abstract**: We consider communication over a family of binary-input memoryless output-symmetric channels using low-density parity-check codes under message passing decoding. The asymptotic (in the length) performance of such a combination for a fixed number of iterations is given by density evolution. It is customary to define the threshold of density evolution as the maximum channel parameter for which the bit error probability under density evolution converges to zero as a function of the iteration number. In practice we often work with short codes and perform a large number of iterations. It is therefore interesting to consider what happens if in the standard analysis we exchange the order in which the blocklength and the number of iterations diverge to infinity. In particular, we can ask whether both limits give the same threshold. Although empirical observations strongly suggest that the exchange of limits is valid for all channel parameters, we limit our discussion to channel parameters below the density evolution threshold. Specifically, we show that under some suitable technical conditions the bit error probability vanishes below the density evolution threshold regardless of how the limit is taken.

## Optimizing burst erasure correction of LDPC codes by interleaving

- **Status**: ✅
- **Reason**: QC-LDPC stopping set 기반 burst erasure 개선 인터리버 설계(WiMax protograph QC-LDPC); 바이너리 코드설계(E) 이식 가능.
- **ID**: ieee:4595166
- **Type**: conference
- **Published**: 6-11 July 
- **Authors**: Gokul Sridharan, Abishek Kumarasubramanian, Andrew Thangaraj +1
- **PDF**: https://ieeexplore.ieee.org/document/4595166
- **Abstract**: The performance of iterative decoding of low density parity check (LDPC) codes over binary erasure channels can be completely characterized by the study of stopping sets. Therefore, the burst erasure correction capability of a given LDPC code can be readily quantified by searching for stopping sets within consecutive bit nodes. In this work we study the optimal permutation of the bit nodes that will result in the maximum possible burst erasure correction capability for a given LDPC code. Noting that this is essentially a combinatorial optimization problem that is highly likely to be NP-hard, we adopt a simulated annealing based approach for finding the optimal permutation. We present bounds based on stopping sets that limit the burst erasure correction capability. As part of our results, we provide interleavers that greatly improve the burst erasure correction capability of protograph quasi-cyclic LDPC codes used in the WiMax standard.

## Performance study of non-binary LDPC Codes over GF(q)

- **Status**: ❌
- **Reason**: GF(q) 비이진 LDPC - 비이진 제외 대상
- **ID**: ieee:4610743
- **Type**: conference
- **Published**: 25-25 July
- **Authors**: V.S. Ganepola, R.A. Carrasco, I. J. Wassell +1
- **PDF**: https://ieeexplore.ieee.org/document/4610743
- **Abstract**: Low-density parity check (LDPC) codes are known to perform well in the presence of additive white Gaussian noise (AWGN) but for very large block lengths. It has been proposed to define the codes over high order Galois fields to overcome this limitation. In this paper we construct new quasi-cyclic non-binary LDPC codes with moderate code lengths from Reed-Solomon codes with two message symbols proposed by Lin et al defined over large finite fields. We evaluate the performance of these codes on the AWGN channel by computer simulation and show that they outperform binary LDPC codes of the same length in binary bits.

## On stopping criteria for Low-Density Parity-Check Codes

- **Status**: ✅
- **Reason**: 단축 LDPC 조기종료 정지기준(반복수 절감) - 이식 가능 디코더 기법(C)
- **ID**: ieee:4610813
- **Type**: conference
- **Published**: 25-25 July
- **Authors**: D. Alleyne, J. Sodha
- **PDF**: https://ieeexplore.ieee.org/document/4610813
- **Abstract**: A stopping criterion for short-length low-density parity-check codes (LDPC) is developed based on accumulating evidence which indicates whether the decoder should be allowed to iterate beyond a predefined iteration limit that is lower than the normal maximum number of decoder iterations. Without any additional decoding complexity, we find that the average number of iterations at low SNRs can be reduced without sacrificing performance. Simulation results are presented for the rate frac12 (288, 576) and the rate frac12 (1152, 2304) WiMAX 802.16e LDPC code over an AWGN channel with binary phase shift keying (BPSK) modulation.

## LP decoding of LDPC codes in HARQ systems

- **Status**: ✅
- **Reason**: LP 디코딩+ARQ, integrality 기반 재전송 기준 - 바이너리 LDPC 디코더 기법(C)
- **ID**: ieee:4610781
- **Type**: conference
- **Published**: 25-25 July
- **Authors**: Michael Lunglmayr, Jens Berkmann, Mario Huemer
- **PDF**: https://ieeexplore.ieee.org/document/4610781
- **Abstract**: The combination of low density parity check (LDPC) Codes and Automatic Repeat reQuest (ARQ) has shown to be a promising option to increase the throughput of a communication system. A recently proposed method uses the decoding result to request unreliable bits for retransmission (reliability-based Hybrid ARQ). Commonly, Belief Propagation is used to decode LDPC codes. The result of this algorithm naturally provides an estimate for the probability of a bit to be erroneous. Another possibility to decode LDPC codes is via linear programming (LP) decoding. Despite some drawbacks (e.g. in terms of implementation complexity), linear programming decoding provides an interesting alternative to Belief Propagation. This work investigates the feasibility of combining LP decoding with ARQ. In lack of a probability measure for the decoded bits, when using LP decoding, request criteria using the integrality of the values in the LP solution are proposed. We present statistical investigations on the proposed criteria and the results of throughput simulations demonstrating the gains achievable by the proposed methods.

## Design of structured irregular LDPC codes

- **Status**: ✅
- **Reason**: cyclic shift 행렬 기반 불규칙 LDPC 구성+파라미터 최적화 알고리즘 — 코드설계(E) 이식 가능
- **ID**: ieee:4602580
- **Type**: conference
- **Published**: 21-25 July
- **Authors**: Peter Trifonov
- **PDF**: https://ieeexplore.ieee.org/document/4602580
- **Abstract**: A novel construction of irregular LDPC codes based on cyclic shift matrices is presented. The construction allows compact specification of LDPC codes of arbitrary length. An optimization algorithm is presented for finding the parameters of the code.

## Code construction algorithm for architecture aware LDPC codes with low-error-floor

- **Status**: ✅
- **Reason**: low-error-floor 위한 trapping/stopping set 감소 코드 구성+TDMP 디코더 FPGA 구현 — 코드설계(E)/HW(D)
- **ID**: ieee:4602573
- **Type**: conference
- **Published**: 21-25 July
- **Authors**: Dariusz Kania, Wojciech Sulek
- **PDF**: https://ieeexplore.ieee.org/document/4602573
- **Abstract**: The common approach for the design of an error correction system is first to construct a code and then to define the hardware structure of the encoder and decoder. However, in the case of LDPC codes (low-density parity-check) such a constructed code is generally not well suited for a hardware implementation. It has been recognized that the code construction and hardware design must be considered jointly to facilitate LDPC decoder and encoder implementation. In this paper, an efficient decoder structure for regular and irregular LDPC codes, based on TDMP (turbo-decoding message passing) scheme is designed first. The decoder has been implemented and verified in an FPGA device. Constraints for the parity check matrix of a code to be suitable for the decoder architecture are defined. Then an algorithm for LDPC parity check matrix construction subject to these constraints is presented. The algorithm aims at improving performance of the code in the low SNR region by employing irregular codes as well as in high SNR region by reducing the number of small Stopping Sets and Trapping Sets in the Tanner graph of the code making use of a computer search technique.

## HAPS systems performance evaluation by simulation techniques at Ka band

- **Status**: ❌
- **Reason**: HAPS Ka대역 LDPC/M-APSK 전송 BER 시뮬레이션 — LDPC 부수 언급, 떼어낼 기법 없음
- **ID**: ieee:4602599
- **Type**: conference
- **Published**: 21-25 July
- **Authors**: Jose A. Delgado-Penin, Luca Dell' Orletta
- **PDF**: https://ieeexplore.ieee.org/document/4602599
- **Abstract**: The high altitude platforms stations (HAPS) represent an attractive option today for fixed broadband wireless access. This paper describes an analysis by simulation of the performance of a coded digital transmission system at Ka band for HATS in urban area when are considered weather impairments. Numerical results in terms of BER are obtained when (LDPC/M-APSK) coded signals are affected by fading caused by weather effects at Ka band. These effects are taken in consideration using a time series obtained by simulation. These results should be useful to a system designer of HATS communications systems at Ka band.

## LDPC-based advanced FEC for 100 Gbps transmission

- **Status**: ✅
- **Reason**: 100Gbps FEC용 회로복잡도 감소 LDPC 알고리즘 + concatenation으로 error-floor 억제 — 복잡도 저감 디코더/error-floor 기법 이식 가능(C/E)
- **ID**: ieee:4590567
- **Type**: conference
- **Published**: 21-23 July
- **Authors**: Takashi Mizuochi, Yoshikuni Miyata
- **PDF**: https://ieeexplore.ieee.org/document/4590567
- **Abstract**: Practical FEC implementation of 100 Gbps long-haul transmission is discussed. An LDPC code using a novel algorithm is introduced to reduce circuit complexity. Simulation shows that the Q limit is 7.1 dB, and that the concatenation effectively suppresses unwanted error-floor.

## Mitigation of linear and nonlinear impairments in high-speed optical networks by using LDPC-coded turbo equalization

- **Status**: ❌
- **Reason**: 광통신 LDPC-coded turbo equalization, 표준 large-girth block-circulant + BCJR 등화기; NAND에 새로 이식할 디코더/구성 기여 없음 (응용 특이적)
- **ID**: ieee:4590536
- **Type**: conference
- **Published**: 21-23 July
- **Authors**: Ivan B. Djordjevic
- **PDF**: https://ieeexplore.ieee.org/document/4590536
- **Abstract**: We present a nonlinear ISI cancellation scheme based on LDPC-coded turbo equalization. This scheme is suitable for simultaneous suppression of intra-channel nonlinearities, chromatic dispersion compensation, and PMD compensation. LDPC coding is based on large girth block-circulant codes, and maximum a posteriori probability equalizer is based on Bahl-Cocke-Jelinek-Raviv (BJCR) algorithm.

## PMD compensation in multilevel coded-modulation schemes with coherent detection using Alamouti-type polarization-time coding

- **Status**: ❌
- **Reason**: PMD 보상+Alamouti 편광시간 부호화 광통신 응용, LDPC는 채널코드 언급뿐 떼어낼 기법 없음
- **ID**: ieee:4590510
- **Type**: conference
- **Published**: 21-23 July
- **Authors**: Ivan B. Djordjevic, Lei Xu, Ting Wang
- **PDF**: https://ieeexplore.ieee.org/document/4590510
- **Abstract**: We present a PMD compensation scheme suitable for use in multilevel coded-modulation schemes, with PMD compensation efficiency comparable to that of OFDM, but with lower complexity of both transmitter and receiver. It is based on Alamouti-type polarization-time coding, with LDPC codes as channel codes.

## Use of LDPC to improve the MIMO-OFDM systems performance

- **Status**: ❌
- **Reason**: MIMO-OFDM PAPR 저감용 LDPC 응용; 무선 특이적이고 NAND로 이식할 신규 부호·디코더 기여 없음
- **ID**: ieee:4632778
- **Type**: conference
- **Published**: 20-22 July
- **Authors**: Omar Daoud
- **PDF**: https://ieeexplore.ieee.org/document/4632778
- **Abstract**: Orthogonal frequency division multiplexing (OFDM) is a promising technique in the next evolution of the mobile telephony, However it suffers from peak to average power ratio (PAPR). It is a problem for broadcast engineers in many different applications. Non-linearities can cause severe out-of-band radiation when confronted with high PAPRs. Previous work has shown that the application of coding just before the transmission frontend can help alleviate this effect. This paper presents a design for a low density parity check (LDPC) code that achieves a good error correction performance and is used to lower the PAPR in a multiple input multiple output orthogonal frequency division multiplex system. The paper will detail the results of software simulations, verified through hardware simulations that show that further reductions in PAPR can be achieved over previous work in this field. Finally, this paper will show that PAPR reduction can be achieved by employing LDPC coding prior to modulation.

## Architecture and VLSI realization of a high-speed programmable decoder for LDPC convolutional codes

- **Status**: ✅
- **Reason**: 수정 Min-Sum 기반 고속 프로그래머블 LDPC 디코더 VLSI/ASIC 아키텍처, 병렬화 기법(C/D)
- **ID**: ieee:4580181
- **Type**: conference
- **Published**: 2-4 July 2
- **Authors**: Marcos B.S. Tavares, Steffen Kunze, Emil Matus +1
- **PDF**: https://ieeexplore.ieee.org/document/4580181
- **Abstract**: In this paper, we present a novel high-speed dual-core programmable decoder architecture for LDPC convolutional codes and their tail-biting versions. This architecture uses a modified Min-Sum algorithm and enables the decoding of a multitude of codes with different node degree distributions, rates and block lengths. We show how the parallelization concepts are derived using the properties of the bipartite graphs underlying the codes. Moreover, the hardware elements composing the architecture will be presented and analyzed in detail. The programmability of the decoder is also considered. Finally, we present the synthesis results for a prototype ASIC which is capable of achieving high decoding throughput still with very high flexibility, relatively low power consumption and small area.

## Cross layer adaptive transmission in communication systems

- **Status**: ❌
- **Reason**: MIMO 크로스레이어 AMC+HARQ 처리량 분석; LDPC는 FEC로 부수 언급, 떼어낼 ECC 기법 없음
- **ID**: ieee:4597977
- **Type**: conference
- **Published**: 2-4 July 2
- **Authors**: Yuling Zhang, Dongfeng Yuan, Tingting Han +1
- **PDF**: https://ieeexplore.ieee.org/document/4597977
- **Abstract**: In this paper, we investigate the cross layer adaptive transmission in communication system, in which there are multiple input and multiple output antennas (MIMO). Two adaptive transmission techniques, adaptive modulation and coding (AMC) in physical layer and hybrid automatic repeat request (HARQ) protocol in data link layer are combined to improve the average spectral efficiency of the system. A low-density parity-check code (L DPC) is used as the forward error control code. We derive the expressions of the throughput of the MIMO system when spatial diversity and multiplexing techniques are used respectively.

## Performance Analysis of Raptor Codes in OFDM Systems

- **Status**: ❌
- **Reason**: Raptor/Fountain 코드 성능 분석, QC-LDPC는 비교 베이스라인일 뿐 떼어낼 신규 LDPC ECC 기법 없음
- **ID**: ieee:4580107
- **Type**: conference
- **Published**: 16-18 July
- **Authors**: P. Palanisamy, T.V.S. Sreedhar
- **PDF**: https://ieeexplore.ieee.org/document/4580107
- **Abstract**: In wireless communication systems, intended to support broadcast services, it is not feasible to use an error control strategy such as automatic repeat request (ARQ) due to the heavy channel and transmitter load caused by all repeat-requests. An alternative error correcting strategy not suffering from the disadvantages of using ARQ is the introduction of a forward error correcting (FEC) code. In this paper, forward error correcting codes called Raptor codes (a class of Fountain codes) are applied for orthogonal frequency division multiplexing(OFDM) systems, which is a popular multi-carrier modulation technique in broadband communications and is currently being used in the IEEE 802.16e (Wi-Max) standard. The BER performance and burst-erasure correction capability of Raptor codes are compared with that of quasi-cyclic LDPC codes in AWGN channel.

## LDPC coded OFDM modulation for high spectral efficiency transmission

- **Status**: ❌
- **Reason**: LDPC coded OFDM 고효율 전송(RS-LCM, gray labeling)—무선 변조 응용, 떼어낼 ECC 기법 없음
- **ID**: ieee:4611693
- **Type**: conference
- **Published**: 10-11 July
- **Authors**: Chih-Yuan Yang, Mong-Kai Ku
- **PDF**: https://ieeexplore.ieee.org/document/4611693
- **Abstract**: This paper investigates efficient low-density parity-check (LDPC) coded orthogonal frequency division multiplexing (OFDM) modulation schemes for fixed wireless application. We use partially LDPC coded with double gray code labeling technique and Reed-Solomon code with LDPC Coded Modulation (RS-LCM) to achieve better performance than the conventional LDPC bit-interleaved coded modulation (BICM) scheme. RS-LCM scheme outperforms BICM scheme by 0.4 dB at a BER of 10−5.
