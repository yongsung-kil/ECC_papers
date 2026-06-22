# IEEE Xplore — 2005-10 (1차선별 통과)


## Partition-and-shift LDPC codes

- **Status**: ✅
- **Reason**: 신규 구조적 LDPC 구성(partition-and-shift)으로 큰 girth 보장 정리 제시 — 바이너리 코드설계 기법(E) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1519179
- **Type**: journal
- **Published**: Oct. 2005
- **Authors**: Jin Lu, J.M.F. Moura
- **PDF**: https://ieeexplore.ieee.org/document/1519179
- **Abstract**: This paper describes a new type of regular structured low-density parity-check (LDPC) code: the partition-and-shift LDPC (PS-LDPC) code. PS-LDPC codes can be easily designed to have large girth. The code construction is simple to explain: we divide the bit and check nodes in the Tanner graph into subsets and connect nodes in these subsets according to a set of parameters called shifts. We derive a general theorem on the shifts to prevent cycles that are harmful to LDPC decoding. This theorem provides a methodology to design PS-LDPC codes with arbitrary column weight j and large girth g. Simulation results over EPR4 channels demonstrate the good bit-error rate performance of PS-LDPC codes.

## A generalized LDPC decoder for blind turbo equalization

- **Status**: ✅
- **Reason**: 표준 LDPC 디코더를 일반화해 임의 비트·패리티 집합 결합확률 계산하는 신규 메시지패싱 기법으로 BP에 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1510991
- **Type**: journal
- **Published**: Oct. 2005
- **Authors**: J.H. Gunther, M. Ankapura, T.K. Moon
- **PDF**: https://ieeexplore.ieee.org/document/1510991
- **Abstract**: The equations for iteratively decoding low-density parity-check (LDPC) codes are generalized to compute joint probabilities of arbitrary sets of codeword bits and parity checks. The standard iterative LDPC decoder, which computes single variable probabilities, is realized as a special case. Another specialization allows pairwise joint posterior probabilities of pairs of codeword bits to be computed. These pairwise joint probabilities are used in an expectation-maximization (EM) based blind channel estimator that is ignorant of the code constraints. Channel estimates are input to a turbo equalizer that exploits the structure of the LDPC code. Feeding pairwise posterior probabilities back to the channel estimator eliminates the need to average across time for channel estimation. Therefore, this scheme can be used to equalize very long codewords, even when the channel is time varying. This blind turbo equalizer is evaluated through computer simulations and found to perform as well as a channel-informed turbo equalizer but with approximately twice the number of turbo iterations.

## LDPC codes satisfying the (0,k) constraint

- **Status**: ✅
- **Reason**: message-passing 디코더 정보를 활용하는 신규 flip 디코더로 채널+flip 오류 정정 — 이식 가능 디코더(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1519171
- **Type**: journal
- **Published**: Oct. 2005
- **Authors**: S. Babvey, S.W. McLaughlin
- **PDF**: https://ieeexplore.ieee.org/document/1519171
- **Abstract**: In this paper, we use a stochastic expectation-maximization method to illustrate how to come close to achieving the capacity of the noisy (0,k) constrained additive white Gaussian noise (AWGN) channels. We use the bit-flipping-based constrained coding system proposed by Vasic and Pedagani, to transmit (0,k) constrained low-density parity check (LDPC) codewords over an AWGN channel. In the original approach of Vasic and Pedagani, if the number of flipped bits is large, the message-passing decoder of the LDPC codes fails to correct all the errors, and the system is prone to an error floor. We propose a flip decoder that exploits the information from the message-passing decoder to correct the flipped bits. We illustrate that the message-passing decoder and the flip decoder together correct both the channel and flip errors and achieve rates close to the noisy (0,k) channel capacity.

## Field-programmable gate-array-based investigation of the error floor of low-density parity check codes for magnetic recording channels

- **Status**: ✅
- **Reason**: FPGA 기반 저BER error floor 시뮬레이터 — 이식 가능 HW 평가 아키텍처(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:1519181
- **Type**: journal
- **Published**: Oct. 2005
- **Authors**: Lingyan Sun, Hongwei Song, B.V.K.V. Kumar +1
- **PDF**: https://ieeexplore.ieee.org/document/1519181
- **Abstract**: Good performance of iterative detection and decoding using low-density parity check (LDPC) codes has stimulated great interest in the data storage industry. One major concern in using LDPC codes in the read channel is their error floor, which is still an open question. To investigate the performance of LDPC codes in low bit-error rates (BER/spl sim/10/sup -10/), we developed a high-throughput fully reconfigurable simulator using a field programmable gate array. Using this simulator, we are able to observe the performance of LDPC codes at low BER within a reasonably short time (10/sup -10/ within 1.5 h). We show the evaluation results for two types of LDPC codes.

## Soft-bit decoding of regular low-density parity-check codes

- **Status**: ✅
- **Reason**: BP의 새 soft-bit 메시지 표현 및 근사, fixed-point 정밀도 분석 — 바이너리 LDPC 디코더 변형(C) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1519652
- **Type**: journal
- **Published**: Oct. 2005
- **Authors**: S.L. Howard, V.C. Gaudet, C. Schlegel
- **PDF**: https://ieeexplore.ieee.org/document/1519652
- **Abstract**: A novel representation, using soft-bit messages, of the belief propagation (BP) decoding algorithm for low-density parity-check codes is derived as an alternative to the log-likelihood-ratio (LLR)-based BP and min-sum decoding algorithms. A simple approximation is also presented. Simulation results demonstrate the functionality of the soft-bit decoding algorithm. Floating-point soft-bit and LLR BP decoding show equivalent performance; the approximation incurs 0.5-dB loss, comparable to min-sum performance loss over BP. Fixed-point results show similar performance to LLR BP decoding; the approximation converges to floating-point results with one less bit of precision.

## An improved bit-flipping scheme to achieve run length control in coded systems

- **Status**: ✅
- **Reason**: LDPC+RLL 제약 결합 개선 bit-flipping, soft-decision 호환 — 떼어낼 디코딩/제약 기법 검토 가치(애매하여 살림)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1519180
- **Type**: journal
- **Published**: Oct. 2005
- **Authors**: Zongwang Li, Jin Xie, B.V.K.V. Kumar
- **PDF**: https://ieeexplore.ieee.org/document/1519180
- **Abstract**: We propose an improved bit-flipping scheme that combines error-correcting codes such as low-density parity check codes with run length limit (RLL) constraints. In addition to its compatibility with soft decision decoding, the proposed scheme has the advantages of no error propagation and fixed block length. Testing with simulated data and real data show good performance. The loss in performance due to the introduction of RLL constraint is less than 0.1 dB at bit-error rate 10/sup -6/ and block-error rate 10/sup -4/.

## Properties of optimum binary message-passing decoders

- **Status**: ✅
- **Reason**: 바이너리 message-passing 디코더 최적성(Gallager Alg B) + irregular degree distribution 설계 — 이식 가능 디코더/코드설계(C/E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1512437
- **Type**: journal
- **Published**: Oct. 2005
- **Authors**: M. Ardakani, F.R. Kschischang
- **PDF**: https://ieeexplore.ieee.org/document/1512437
- **Abstract**: We consider a class of message-passing decoders for low-density parity-check (LDPC) codes whose messages are binary valued. We prove that if the channel is symmetric and all codewords are equally likely to be transmitted, an optimum decoding rule (in the sense of minimizing message error rate) should satisfy certain symmetry and isotropy conditions. Using this result, we prove that Gallager's Algorithm B achieves the optimum decoding threshold among all binary message-passing decoding algorithms for regular codes. For irregular codes, we argue that when the nodes of the message-passing decoder do not exploit knowledge of their decoding neighborhood, optimality of Gallager's Algorithm B is preserved. We also consider the problem of designing irregular LDPC codes and find a bound on the achievable rates with Gallager's Algorithm B. Using this bound, we study the case of low error-rate channels and analytically find good degree distributions for them.

## Iteratively decodable codes from orthogonal arrays for optical communication systems

- **Status**: ✅
- **Reason**: 직교배열 기반 신규 LDPC 부호 구성(girth>=6, 고율, 큰 최소거리) — 이식 가능 바이너리 코드설계(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1515671
- **Type**: journal
- **Published**: Oct. 2005
- **Authors**: I.B. Djordjevic, B. Vasic
- **PDF**: https://ieeexplore.ieee.org/document/1515671
- **Abstract**: A novel family of low-density parity-check codes is proposed based on orthogonal arrays. Codes from this family have high code rate, girth of at least six, large minimum distance, and significantly outperform the error correction schemes based on turbo product codes proposed for optical communication systems.

## LDPC Code for Reduced Routing Decoder

- **Status**: ✅
- **Reason**: LDPC 디코더 VLSI 라우팅 복잡도 저감 코드 설계+병렬 디코더 HW(D/E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1554212
- **Type**: conference
- **Published**: 5-5 Oct. 2
- **Authors**: Euncheol Kim, Gwan S. Choi
- **PDF**: https://ieeexplore.ieee.org/document/1554212
- **Abstract**: A design approach that reduces the routing complexity in a VLSI implementation of Low-Density Parity-Check (LDPC) decoder is presented. An LDPC code is a linear-block code for forward error correction, attributed by a sparse parity-check matrix. Iterative decoding of this code is shown to yield Bit Error Rate (BER) performance approaching Shannon Limit. However, implementation of decoder for this code is difficult due to the routing requirements of its massive number of data-flow structures in decoding logic. We present a routing approach for a parallel LDPC decoder implementation by 1) analyzing the physical routability limitations and 2) designing the code parameters to limit the interconnect lengths to a bounded region. The approach does not compromise the BER performance, and yet achieves a much higher throughput resulting from significantly reduced wires lengths.

## Interconnection Network for Structured Low-Density Parity-Check Decoders

- **Status**: ✅
- **Reason**: 구조화 LDPC 디코더용 Benes permutation 네트워크/라우팅, 이식 가능 HW(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:1554118
- **Type**: conference
- **Published**: 5-5 Oct. 2
- **Authors**: G. Malema, M. Liebelt
- **PDF**: https://ieeexplore.ieee.org/document/1554118
- **Abstract**: Most structured codes use the group-and-permute design approach in which rows and columns are divided into groups of the same size. Row/column groups and individual row-column are connected by some permutation. A general group-and-permute decoder requires an interconnection network for group-to-group communication. In this paper we suggest the use of self-routed Benes networks based on the communication pattern of LDPC codes. Bipartite edge coloring is used to schedule messages such that there are no switch network output conflicts. The looping routing algorithm for Benes networks is used to compute switching codes. Both scheduling information and switching codes are pre-computed and stored for each design code since they do not change in the lifetime of the code

## Hyperbolic tangent function avoided for encoded pilot low density parity check decoding

- **Status**: ✅
- **Reason**: sum-product에서 tanh overflow/underflow 회피 수정 — BP 수치안정 기법이 바이너리 LDPC에 이식 가능(C), 애매하여 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1617677
- **Type**: conference
- **Published**: 3-4 Oct. 2
- **Authors**: A. Goyal, H.M. Kwon
- **PDF**: https://ieeexplore.ieee.org/document/1617677
- **Abstract**: Very recently the same authors of this paper proposed an encoded pilot system where pilot bits are encoded with the message bits using a systematic code, e.g., a systematic low density parity check (LDPC) code. The authors claimed that the encoded pilot system can have significantly lower complexity and better energy efficiency at the same bandwidth efficiency or even higher bandwidth efficiency over the no pilot systems or the conventional time multiplexed pilot systems. The pilot bits have not been encoded with message bits but multiplexed after the encoder and de-multiplexed before decoding at the conventional receiver. The last case is called a deleted case because its corresponding parity check matrix is obtained by deleting the corresponding columns of the original parity check matrix. This paper finds a difficulty to use the well known sum-product LDPC decoding algorithm for the deleted case because hyperbolic tangent function causes overflow and underflow. In this paper the sum-product algorithm is modified. And this paper takes a well known Hamming code of (3,7) parity check matrix H under additive white Gaussian noise environment (AWGN) and demonstrates that the encoded pilot system is superior to the other systems, using the modified algorithm

## An efficient low complexity LDPC encoder based on LU factorization with pivoting

- **Status**: ✅
- **Reason**: 피벗팅 LU분해 기반 선형복잡도 LDPC 인코더, 희소행렬 메모리구조+FPGA 구현 - HW(D) 기여 이식 가능
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:1611277
- **Type**: conference
- **Published**: 24-27 Oct.
- **Authors**: Jia-ning Su, Zhou Jiang, Ke Liu +2
- **PDF**: https://ieeexplore.ieee.org/document/1611277
- **Abstract**: In this paper, we present an efficient encoder for regular and irregular low-density parity-check (LDPC) codes with its complexity linear to code length. Inspired by the idea of Neal, we further exploit the sparsity of parity check matrix of LDPC codes and use extended LU factorization with pivoting in encoding process, which is flexible and supporting arbitrary H matrices, code rate and block lengths. An FPGA implementation for a rate 1/2 regular (3,6) length 1536 LDPC code encoder is provided with throughput of 31 Mbps. An efficient memory organization for storing and performing computations on sparse matrices is also presented.

## Partially-parallel LDPC decoder based on high-efficiency message-passing algorithm

- **Status**: ✅
- **Reason**: partially-parallel LDPC 디코더+high-efficiency message-passing FPGA 구현, HW/디코더 이식 가능(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1524200
- **Type**: conference
- **Published**: 2-5 Oct. 2
- **Authors**: K. Shimizu, T. Ishikawa, N. Togawa +2
- **PDF**: https://ieeexplore.ieee.org/document/1524200
- **Abstract**: This paper proposes a partially-parallel LDPC decoder based on a high-efficiency message-passing algorithm. Our proposed partially-parallel LDPC decoder performs the column operations for bit nodes in conjunction with the row operations for check nodes. Bit functional unit with pipeline architecture in our LDPC decoder allows us to perform column operations for every bit node connected to each of check nodes which are updated by the row operations in parallel. Our proposed LDPC decoder improves the tuning when the column operations are performed, accordingly it improves the message-passing efficiency within the limited number of iterations for decoding. We implemented the proposed partially-parallel LDPC decoder on an FPGA, and simulated its decoding performance. Practical simulation shows that our proposed LDPC decoder reduces the number of iterations for decoding, and it improves the bit error performance with a small hardware overhead.

## Structured low-density parity-check code design for next generation digital video broadcast

- **Status**: ✅
- **Reason**: 라우팅 제거·collision-free 단일 메모리 접근 구조화 LDPC — HW 아키텍처+코드설계 이식 가능(D/E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1606037
- **Type**: conference
- **Published**: 17-20 Oct.
- **Authors**: M. Eroz, L.-N. Lee
- **PDF**: https://ieeexplore.ieee.org/document/1606037
- **Abstract**: We describe a novel design for low-density parity-check (LDPC) codes that eliminates the routing problem associated with LDPC decoder implementation resulting in a small silicon area in application specific integrated circuits (ASICs). Unlike previous solutions that require a large number of small and hence area inefficient memory blocks, this design allows collision-free memory access on a single memory block by imposing certain restrictions on the parity check matrix of the codes. Therefore, it leads to substantially smaller circuits. Furthermore the resulting codes have outstanding error rate performance very close to Shannon limit for a wide range of throughputs from 0.5 bits/symbol up to 4 bits/symbol. As a result LDPC codes designed with this method have been standardized for the next generation digital video broadcasting (DVB).

## Approximate cycle extrinsic message degree regular quasi circulant LDPC codes

- **Status**: ✅
- **Reason**: ACE/EMD 기반 QC-LDPC 구성으로 stopping set 확대·error floor 저감 — 바이너리 코드설계 이식 가능(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1606100
- **Type**: conference
- **Published**: 17-20 Oct.
- **Authors**: S. John, H.M. Kwon
- **PDF**: https://ieeexplore.ieee.org/document/1606100
- **Abstract**: We propose a new class of quasi circulant matrices for high rate (R/spl ges/ 1/2 ), by applying the approximate cycle extrinsic message degree (ACE) algorithm, which not only avoids cycles of certain length but also increases the extrinsic message degree (EMD) of stopping sets in a quasi circulant matrix. This novel technique avoids cycles of length four in its primary designing stage, while conditioning on higher length cycles increases the size of a stopping set in the parity check matrix and, hence, lowers the error floor. Appropriate cycle conditioning on quasi circulant matrices in comparison with quasi circulant, irregular and regular matrices (with or without cycle conditioning) yields codes with the lowest error floors under belief propagation decoding for the fading channel. A significant gain of /spl ap/5 dB is observed at bit error 10/sup -4/ under the Jake's fading channel model.

## Short low-error-floor Tanner codes with Hamming nodes

- **Status**: ✅
- **Reason**: Hamming 노드 doping Tanner 부호와 전용 반복 디코딩 알고리즘으로 error floor 저감 — C/E 바이너리 LDPC 그래프 구성+디코더
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1605687
- **Type**: conference
- **Published**: 17-20 Oct.
- **Authors**: G. Liva, W.E. Ryan
- **PDF**: https://ieeexplore.ieee.org/document/1605687
- **Abstract**: While it is fairly easy to design good low-density parity-check codes with medium or large block lengths, and with code rates 1/2 or greater, much more effort is required for short lengths and low rates. We propose a code structure which incorporates Hamming codes into a code's graph, leading to a type of a Tanner code. The incorporation of Hamming codes into the graph, which we call "Hamming code doping", tends to lead to larger minimum distances and hence low error-rate floors. We present an iterative decoding algorithm tailored to graphs possessing "Hamming nodes". Further, a density evolution analysis based on the Gaussian approximation is presented, which is a useful tool for finding good codes. Finally, we present numerical results of some Hamming-doped Tanner codes simulated on the AWGN channel. The simulated codes exhibit remarkably low error floors, while simultaneously displaying good decoding thresholds

## A computationally efficient selective node updating scheme for decoding of LDPC codes

- **Status**: ✅
- **Reason**: 선택적 노드 업데이트로 sum-product 변형, 연산/메모리 접근 절감 — NAND LDPC 디코더에 이식 가능(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1605869
- **Type**: conference
- **Published**: 17-20 Oct.
- **Authors**: E. Cavus, B. Daneshrad
- **PDF**: https://ieeexplore.ieee.org/document/1605869
- **Abstract**: In this paper, we introduce a computationally efficient selective node update algorithm for the decoding of low-density parity check codes. Unlike the standard sum-product algorithm, where all bit and check nodes are updated at each decoding iteration, the developed algorithm only updates unreliable check and bit nodes. A simple reliability criteria is developed to determine the active bit and check nodes per decoding iteration. Based on the developed technique, significant computation reductions are achieved with very little or no loss in the BER performance of the LDPC codes. At a WER of 10-5 , 91.8% and 72.7% check node and 80% and 41% bit node computation reductions are obtained for a (96, 48) and a (504, 252) LDPC code, respectively. The proposed method can be implemented with a slight modification to the standard sum-product decoding algorithm with negligible additional hardware complexity. From a hardware point of view, the proposed algorithm offers power reductions proportional to the computation savings and it leads to higher decoding speeds in serial implementations by decreasing the number of required memory accesses

## Protograph based low error floor LDPC coded modulation

- **Status**: ✅
- **Reason**: protograph 기반 바이너리 LDPC 저 error floor 구성, 고속 디코더 구현 지원, FPGA — E/D 코드설계+HW
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1605713
- **Type**: conference
- **Published**: 17-20 Oct.
- **Authors**: D. Divsalar, C. Jones
- **PDF**: https://ieeexplore.ieee.org/document/1605713
- **Abstract**: In this paper we propose an innovative LDPC coded modulation scheme. We design binary low density parity check (LDPC) codes that are combined with high level modulations such as 8PSK and 16QAM with and without a channel interleaver. At the receiver a demapper transforms the received inphase and quadrature samples to produce reliability information that feeds the binary LDPC decoder. Using this scheme, the same encoder and decoder can support various modulations. Analysis of ensemble average weight enumerators shows that the minimum distance of the proposed LDPC codes grows linearly with block size. Our constructions are based on protograph structures that support high-speed decoder implementations. We also show that precoding can be used to lower the threshold of LDPC codes. The decoding thresholds of the proposed codes, which have linearly increasing minimum distance in block size, outperform that of regular LDPC codes. Furthermore, a family of low to high rate codes, with thresholds that adhere closely to their respective channel capacity thresholds, is presented. For maximum variable node degree 6, the iterative decoding thresholds of these codes outperform the best known unstructured irregular LDPC codes reported in the literature. Iterative decoding simulation results are provided for BPSK, QPSK, 8PSK, and 16QAM modulations over the additive white Gaussian noise channel. FPGA simulation results for the proposed LDPC codes with input block size of 4096 and QPSK modulation (throughput=1 bps/Hz) show that a frame error rate of 10-8 and a bit error rate of 10 -10 can be achieved at Eb/No=1.50 dB

## Design of scaled BP-based decoding algorithm for LDPC codes on flat Rayleigh fading SI channel using EXIT

- **Status**: ✅
- **Reason**: scaled BP 디코딩 알고리즘 설계(스케일 팩터 EXIT 산출), 부호 비의존 디코더 개선(C) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1566878
- **Type**: conference
- **Published**: 12-14 Oct.
- **Authors**: He Zheng, Xiaolei Jin, Hanying Hu
- **PDF**: https://ieeexplore.ieee.org/document/1566878
- **Abstract**: By means of extrinsic information transfer (EXIT), we propose a novel method for designing the scaled belief propagation (BP)-based algorithm for decoding of low-density parity-check (LDPC) codes on the uncorrelated flat Rayleigh fading channel with side information (SI). Using this method, numerical calculations on convergence thresholds for several rate-1/2 regular LDPC codes are provided. The simulation results for the (3,6) regular LDPC code of length 8000 on the Rayleigh fading channel show that the scaled BP-based algorithm with the proposed factor by the EXIT method can achieve the performance very close to that of the BP algorithm.
