# IEEE Xplore — 2009-08


## Design of joint network-low density parity check codes based on the EXIT charts

- **Status**: ❌
- **Reason**: joint network-LDPC(릴레이 네트워크 코딩) EXIT 설계-무선 네트워크 응용 특이적, NAND 이식 기법 없음
- **ID**: ieee:5200898
- **Type**: journal
- **Published**: August 200
- **Authors**: Ying Li, Guanghui Song, Lili Wang
- **PDF**: https://ieeexplore.ieee.org/document/5200898
- **Abstract**: For the multiple-access relay network where two sources communicate with one destination in the presence of one relay, a practical joint network-low density parity check code is designed to help the relay jointly re-encode the messages from both sources. A bilayer extrinsic information transfer chart is developed based on which a design methodology is proposed to iteratively improve the degree distribution of the proposed code. Simulations illustrate that the gap between the convergence threshold and the performance of the coding scheme is less than 0.6dB at BER=10-5.

## Capacity-achieving codes for finite-state channels with maximum-likelihood decoding

- **Status**: ❌
- **Reason**: sparse-graph 부호의 FSC 용량달성 ML 디코딩 이론 bound-순수 이론, 실용 디코더/HW/구성 기여 없음
- **ID**: ieee:5174526
- **Type**: journal
- **Published**: August 200
- **Authors**: Jung Hyun Bae, Achilleas Anastasopoulos
- **PDF**: https://ieeexplore.ieee.org/document/5174526
- **Abstract**: Codes on sparse graphs have been shown to achieve remarkable performance in point-to-point channels with low decoding complexity. Most of the results in this area are based on experimental evidence and/or approximate analysis. The question of whether codes on sparse graphs can achieve the capacity of noisy channels with iterative decoding is still open, and has only been conclusively and positively answered for the binary erasure channel. On the other hand, codes on sparse graphs have been proven to achieve the capacity of memoryless, binary-input, output-symmetric channels with finite graphical complexity per information bit when maximum likelihood (ML) decoding is performed. In this paper, we consider transmission over finite-state channels (FSCs). We derive upper bounds on the average error probability of code ensembles with ML decoding. Based on these bounds we show that codes on sparse graphs can achieve the symmetric information rate (SIR) of FSCs, which is the maximum achievable rate with independently and uniformly distributed input sequences. In order to achieve rates beyond the SIR, we consider a simple quantization scheme that when applied to ensembles of codes on sparse graphs induces a Markov distribution on the transmitted sequence. By deriving average error probability bounds for these quantized code ensembles, we prove that they can achieve the information rates corresponding to the induced Markov distribution, and thus approach the FSC capacity.

## Turbo coded multiple-antenna systems for near-capacity performance

- **Status**: ❌
- **Reason**: turbo coded MIMO/BLAST 무선 응용, LDPC 무관 떼어낼 기법 없음
- **ID**: ieee:5174524
- **Type**: journal
- **Published**: August 200
- **Authors**: Yeong-Luh Ueng, Chia-Jung Yeh, Mao-Chao Lin +1
- **PDF**: https://ieeexplore.ieee.org/document/5174524
- **Abstract**: For a turbo coded BLAST (Bell LAbs Space-Time architecture) system with Nt transmit antennas and Nr receive antennas, there is a significant gap between its detection threshold and the capacity in case Nt > Nr. In this paper, we show that by introducing a convolutional interleaver with block delay between the BLAST mapper and the turbo encoder, the threshold can be improved. Near-capacity thresholds can be achieved for some cases. To take advantage of the low detector complexity in Alamouti STBC (space-time block code), we also investigate a STBC system, which is the concatenation of the Alamouti STBC with a turbo trellis coded modulation. By using a proper labelling and adding a convolutional interleaver with block delay to such a STBC system, we achieve both lower error floors and lower thresholds.

## Quasi-systematic doped LT codes

- **Status**: ❌
- **Reason**: QS-DLT(rateless erasure/LT fountain) 코드; fountain/erasure 부호로 떼어낼 채널 ECC 기법 없음
- **ID**: ieee:5174516
- **Type**: journal
- **Published**: August 200
- **Authors**: Xiaojun Yuan, Li Ping
- **PDF**: https://ieeexplore.ieee.org/document/5174516
- **Abstract**: We propose a family of binary erasure codes, namely, quasi-systematic doped Luby-Transform (QS-DLT) codes, that are rate-less, almost systematic, and universally capacity-achieving without the prior knowledge of channel erasure rate. The encoding and decoding complexities of QS-DLT codes are O(Klog(1/epsiv)), where K is the information length, and epsiv is the overhead. Stopping-set analysis is carried out to study the error-floor behavior of QS-DLT codes. Analysis and numerical results demonstrate that QS-DLT codes provide a low-complexity alternative to systematic Raptor codes with comparable performance.

## Finite-length scaling of turbo-like code ensembles on the binary erasure channel

- **Status**: ❌
- **Reason**: BEC에서 turbo-like 부호 유한길이 scaling 추정-순수 이론 bound, 떼어낼 디코더/HW/구성 없음
- **ID**: ieee:5174521
- **Type**: journal
- **Published**: August 200
- **Authors**: Iryna Andriyanova
- **PDF**: https://ieeexplore.ieee.org/document/5174521
- **Abstract**: A possibility of estimating the finite-length performance of sparse-graph code ensembles gives two opportunities: to compare different codes of the same length in a context very close to real, practical applications and to perform the parameter optimization for a given code length [2]. We need a finite-length approximation that is valid for any code ensemble. The scaling approach seems to be a tool, general enough to provide such an approximation. However, the analytical derivation of parameters of the scaling approximation has been successful only for LDPC codes [1]; despite several attempts [25], [20], no such result was proposed for other code ensembles. In this paper, we focus on the finite-length performance of turbo-like codes, by applying the scaling approach to this case. In particular, by assuming the transmission over the binary erasure channel, we conjecture the scaling law and derive its scaling parameter. As examples, we present the performance estimation for Repeat-Accumulate codes [11], parallel turbo codes [8] and TLDPC codes [5], in all cases matching well the numerical results.

## Good concatenated code ensembles for the binary erasure channel

- **Status**: ❌
- **Reason**: BEC용 concatenated(RMA/HCC) 부호 ensemble 점근 stopping set 분석-비-LDPC 부호+이론 분석, 이식 기법 없음
- **ID**: ieee:5174522
- **Type**: journal
- **Published**: August 200
- **Authors**: Alexandre Graell I Amat, Eirik Rosnes
- **PDF**: https://ieeexplore.ieee.org/document/5174522
- **Abstract**: In this work, we give good concatenated code ensembles for the binary erasure channel (BEC). In particular, we consider repeat multiple-accumulate (RMA) code ensembles formed by the serial concatenation of a repetition code with multiple accumulators, and the hybrid concatenated code (HCC) ensembles recently introduced by Koller et al. (5th Int. Symp. on Turbo Codes & Rel. Topics, Lausanne, Switzerland) consisting of an outer multiple parallel concatenated code serially concatenated with an inner accumulator. We introduce stopping sets for iterative constituent code oriented decoding using maximum a posteriori erasure correction in the constituent codes. We then analyze the asymptotic stopping set distribution for RMA and HCC ensembles and show that their stopping distance hmin, defined as the size of the smallest nonempty stopping set, asymptotically grows linearly with the block length. Thus, these code ensembles are good for the BEC. It is shown that for RMA code ensembles, contrary to the asymptotic minimum distance dmin, whose growth rate coefficient increases with the number of accumulate codes, the hmin growth rate coefficient diminishes with the number of accumulators. We also consider random puncturing of RMA code ensembles and show that for sufficiently high code rates, the asymptotic hmin does not grow linearly with the block length, contrary to the asymptotic dmin, whose growth rate coefficient approaches the Gilbert-Varshamov bound as the rate increases. Finally, we give iterative decoding thresholds for the different code ensembles to compare the convergence properties.

## Toward optimizing cauchy matrix for cauchy reed-solomon code

- **Status**: ❌
- **Reason**: Cauchy Reed-Solomon 행렬 최적화-비-LDPC(RS) 부호, 이식 디코더 기법 없음
- **ID**: ieee:5200899
- **Type**: journal
- **Published**: August 200
- **Authors**: Xiangxue Li, Qingji Zheng, Haifeng Qian +2
- **PDF**: https://ieeexplore.ieee.org/document/5200899
- **Abstract**: The computational costs of Cauchy Reed-Solomon (CRS) encoding operation make a great impact on the performance of its practical applications. The letter concentrates on how to construct a good Cauchy matrix which can lead to an efficient CRS coding scheme. We first formally model the problem by using a binary quadratic programming, then present an approximate method called localized greedy algorithm (LGA) to solve it. Compared with existing work, LGA requires much lower complexities to obtain the same performance of Cauchy matrices.

## Moment Balancing Templates: Constructions to Add Insertion/Deletion Correction Capability to Error Correcting or Constrained Codes

- **Status**: ❌
- **Reason**: 삽입/삭제 정정 moment balancing template, NAND 채널 ECC와 무관한 부호 확장 기법
- **ID**: ieee:5165175
- **Type**: journal
- **Published**: Aug. 2009
- **Authors**: Hendrik C. Ferreira, Khaled A. S. Abdel-Ghaffar, Ling Cheng +2
- **PDF**: https://ieeexplore.ieee.org/document/5165175
- **Abstract**: Templates are constructed to extend arbitrary additive error correcting or constrained codes, i.e., additional redundant bits are added in selected positions to balance the moment of the codeword. The original codes may have error correcting capabilities or constrained output symbols as predetermined by the usual communication system considerations, which are retained after extending the code. Using some number theoretic constructions in the literature, insertion/deletion correction can then be achieved. If the template is carefully designed, the number of additional redundant bits for the insertion/deletion correction can be kept small-in some cases of the same order as the number of parity bits in a Hamming code of comparable length.

## Design and Analysis of Successive Decoding With Finite Levels for the Markov Channel

- **Status**: ❌
- **Reason**: Markov 채널 successive decoding+인터리버 설계, LDPC는 베이스라인이고 채널특이적 기법으로 NAND 이식성 없음
- **ID**: ieee:5165193
- **Type**: journal
- **Published**: Aug. 2009
- **Authors**: Teng Li, Oliver Michael Collins
- **PDF**: https://ieeexplore.ieee.org/document/5165193
- **Abstract**: This paper proposes a practical successive decoding scheme with finite levels for the finite-state Markov channels (FSMCs) where there is no a priori state information at the transmitter or the receiver. The design employs either a random interleaver or a deterministic interleaver with an irregular pattern and an optional iterative estimation and decoding procedure within each level. The interleaver design criteria may be the achievable rate or the extrinsic information transfer (EXIT) chart, depending on the receiver type. For random interleavers, the optimization problem is solved efficiently using a pilot-utility function, while for deterministic interleavers, a good construction is given using empirical rules. Simulation results demonstrate that the new successive decoding scheme combined with irregular low-density parity-check (LDPC) codes can approach the identically and uniformly distributed (i.u.d.) input capacity on the Markov-fading channel using only a few levels.

## A flexible rate slepian-wolf code construction

- **Status**: ❌
- **Reason**: Slepian-Wolf 분산소스코딩+RCPC convolutional code 신드롬, LDPC 아님이고 소스코딩 도메인
- **ID**: ieee:5201023
- **Type**: journal
- **Published**: Aug. 2009
- **Authors**: Mahdi Zamani, Farshad Lahouti
- **PDF**: https://ieeexplore.ieee.org/document/5201023
- **Abstract**: A flexible rate Slepian-Wolf (SW) code is constructed, which is vital for wireless sensor network applications. The proposed solution is based on an efficient and practical algorithm to compute the syndrome of the rate-compatible convolutional codes (RCPC). Using this algorithm, there is no need to compute the syndrome of punctured version of the mother code for each puncturing matrix, which is complex. Instead, the syndrome of the punctured code is the punctured version of the syndrome of the mother code using the same pattern of puncturing. The algorithm is general for all convolutional codes in Zq. The strategy is also generalized for parallel and serial concatenated convolutional codes. For the cases, where the dependencies among sources are modeled as a virtual discrete channel, a simplified decoding scheme is suggested. This method is generalized to achieve all points on the SW boundary using a simple code design technique. Simulation results demonstrate the performance and effectiveness of the proposed methods.

## Parameter Selection for Wyner–Ziv Coding of Laplacian Sources with Additive Laplacian or Gaussian Innovation

- **Status**: ❌
- **Reason**: Wyner-Ziv 소스코딩 파라미터 선택, 채널 ECC가 아닌 소스코딩
- **ID**: ieee:4803747
- **Type**: journal
- **Published**: Aug. 2009
- **Authors**: Debargha Mukherjee
- **PDF**: https://ieeexplore.ieee.org/document/4803747
- **Abstract**: A large number of practical coding scenarios deal with sources such as transform coefficients that can be well modeled as Laplacians. For regular coding of such sources, samples are often quantized by a family of uniform quantizers possibly with a deadzone, and then entropy coded. For the Wyner-Ziv coding problem when correlated side-information is available at the decoder, the side-information can be modeled as obtained by independent additive Laplacian or Gaussian innovation on the source. This paper deals with optimal choice of parameters for practical Wyner-Ziv coding in such scenarios, using the same quantizer family as in the regular codec to cover a range of rate-distortion tradeoffs, given the variances of the source and additive noise. We propose and analyze a general encoding model based on multilevel coset codes that combines source coding and channel coding and show that at practical block lengths and code complexities, not pure channel coding but a hybrid combination of source coding and channel coding with right parameters provide optimal rate-distortion performance. We also provide a framework for on-the-fly parameter choice based on nonparametric representation of a set of seed functions, for use in scenarios where variances are estimated during encoding. A good insight in the optimal parameter selection mechanism is essential for building practical distributed codecs.

## Reliability-based retransmission criteria for hybrid ARQ

- **Status**: ❌
- **Reason**: HARQ 재전송 기준(BEP/WEP)으로 ECC 부호·디코더·HW 기여 없음, 무선 프로토콜 특이적
- **ID**: ieee:5201001
- **Type**: journal
- **Published**: Aug. 2009
- **Authors**: Justus Ch. Fricke, Peter A. Hoeher
- **PDF**: https://ieeexplore.ieee.org/document/5201001
- **Abstract**: Bit error probability (BEP) and word error probability (WEP) are used as reliability-based retransmission criteria in conjunction with hybrid ARQ (HARQ) protocols. Instead of exploiting an error-detecting code, the decision for a retransmission is based on the error probability of the decoded word, which can be calculated in or after the decoding process.

## Joint frame synchronization and belief propagation decoding for quasi-cyclic LDPC-coded system under pseudorandom noise disturbance

- **Status**: ❌
- **Reason**: 프레임 동기화+BP 결합 무선통신 응용 특이적, 떼어낼 NAND ECC 디코더 기법 없음
- **ID**: ieee:5267829
- **Type**: conference
- **Published**: 8-9 Aug. 2
- **Authors**: Zhixiong Chen, Jinsha Yuan
- **PDF**: https://ieeexplore.ieee.org/document/5267829
- **Abstract**: Because of the quasi-cyclic nature of Quasi-Cyclic LDPC (QC-LDPC) codes, there are ramps in the frame synchronization searching process. A pilotless code-aided frame synchronization algorithm joint with improved BP decoding for QC-LDPC coded system under PN disturbance to eliminate the ramps is proposed in this paper. Simulation results show the validity of the modified BP decoding algorithm and outstanding synchronization performance compared to the algorithm before improvement and hard decision frame synchronization proposed by Dong-U Lee.

## The study of LDPC code applied to underwater laser communication

- **Status**: ❌
- **Reason**: 수중 레이저 PPM 통신에 표준 LDPC 소프트판정 적용 — 신규 디코더/구성 없는 응용, 떼어낼 기법 없음
- **ID**: ieee:5292710
- **Type**: conference
- **Published**: 30-3 Aug. 
- **Authors**: Tiansong Li, Haiyan Zhou, Lihua Sun
- **PDF**: https://ieeexplore.ieee.org/document/5292710
- **Abstract**: Low density parity check code is applied to underwater laser pulse position modulation communication system. The soft-decision decoding algorithm improves the error-correcting capacity by using the output soft information of the photon detector.

## A simplified decoding algorithm for nonbinary LDPC codes

- **Status**: ❌
- **Reason**: 비이진(high order GF) LDPC 간소화 디코딩—비이진 LDPC 제외
- **ID**: ieee:5339910
- **Type**: conference
- **Published**: 26-28 Aug.
- **Authors**: Ce-lun Liu, Jian-ping An, Xiang-yuan Bu
- **PDF**: https://ieeexplore.ieee.org/document/5339910
- **Abstract**: A simplified decoding algorithm for low-density parity-check (LDPC) codes over high order Galois field is proposed to reduce the complexity of traditional sum-product algorithm (SPA). There are only addition operation and comparison operation in this algorithm, without complex multiplication operation. The computation complexity of proposed algorithm is much smaller than the SPA. The signal-to-noise power ratio (SNR) isn't needed in this algorithm, so the process of SNR estimation can also be removed. The simulation results show that the bit error rate (BER) performance of proposed algorithm degrades only about 0.5 dB than the SPA, so the proposed algorithm is an efficient simplified algorithm in engineering.

## A construction method of quantum low density parity check code based on projective geometry

- **Status**: ❌
- **Reason**: 양자 LDPC(QLDPC) 사영기하 구성—양자 EC, 원칙 제외
- **ID**: ieee:5339860
- **Type**: conference
- **Published**: 26-28 Aug.
- **Authors**: Sheng-Mei Zhao, Xiu-Li Zhu, Guo-Jun Sun
- **PDF**: https://ieeexplore.ieee.org/document/5339860
- **Abstract**: With the development of quantum error correction techniques, many counterparts of classical error correction coding techniques have been found in quantum area. As the quantum counterpart of a good error correction code in classical communications, quantum low density parity check code becomes a promising coding technique in quantum error correction area. In this paper, a construction method of quantum low density parity check code (quantum LDPC) based on Projective Geometry is proposed, and the quantum code QLDPC [21,6] is selected as an example to illustrate the whole construction procedures. By numerical simulation, the error correction performance of QLDPC [21,6] is discussed over the bit-flipping channel. It is shown that this method is available and has some advantages.

## Bit-wise shortening of nonbinary LDPC codes using their binary images

- **Status**: ❌
- **Reason**: 비이진(nonbinary) RC-LDPC 단축 구성—비이진 LDPC 제외
- **ID**: ieee:5339905
- **Type**: conference
- **Published**: 26-28 Aug.
- **Authors**: Lin Zhou, Baoming Bai, Ming Xu +1
- **PDF**: https://ieeexplore.ieee.org/document/5339905
- **Abstract**: Most of work on rate-compatible low-density parity-check (RC-LDPC) codes focus on binary codes. In this paper, we propose a construction of nonbinary RC-LDPC codes at short block length by using a bit-wise shortening method based on the algebraic properties of their binary images. All shortened information bits are carefully chosen according to the degree distributions of their binary images. Simulations show that a gain of around 1 dB is attained at the shortened code rate R = 1/5 over conventional symbol-wise shortening.

## Parallel encodable nonbinary quasi-cyclic LDPC codes with near-capacity performance

- **Status**: ❌
- **Reason**: 비이진(nonbinary) QC-LDPC 병렬 인코딩—비이진 LDPC 제외
- **ID**: ieee:5339907
- **Type**: conference
- **Published**: 26-28 Aug.
- **Authors**: Chao Chen, Baoming Bai, Ruijia Yuan +1
- **PDF**: https://ieeexplore.ieee.org/document/5339907
- **Abstract**: In this paper, we propose a class of efficiently encodable nonbinary quasi-cyclic low-density parity-check (QC-LDPC) codes over finite fields. The special structure of the parity-check matrix allows the construction of both regular and irregular codes. A parallel encoding algorithm with a simple shift-register circuits implementation is presented, which significantly reduces the encoding latency. Simulation results show that, the proposed codes, when combined with higher order modulations, perform close to the Shannon limit.

## A distributed joint source-channel coding scheme for multiple correlated sources

- **Status**: ❌
- **Reason**: 분산 JSCC, 단일 LDPC를 소스+채널 결합에 사용 — LDPC는 베이스라인이고 떼어낼 ECC 기법 없음
- **ID**: ieee:5339955
- **Type**: conference
- **Published**: 26-28 Aug.
- **Authors**: Xuqi Zhu, Lin Zhang, Yu Liu
- **PDF**: https://ieeexplore.ieee.org/document/5339955
- **Abstract**: Multiple nodes sensing the common target is the most popular application of the Wireless Sensor Networks (WSNs). Pure distributed compression of multiple correlated sources has been discussed much in the related literature, while taking the noisy communication channels into account is more suitable for the actual scenario. In this paper, a practical Distributed Joint Source-Channel Coding (DJSCC) scheme for multiple correlated sources is proposed. Besides considering the noisy channels and multiple sources, the processing of the noisy side information is also investigated here. By combining the Shannon theorem and the Slepian-Wolf theorem, the theoretical limits of the proposed DJSCC scheme are derived. An efficient coding strategy with a single Low-Density Parity Check (LDPC) code is designed based on the theory to cope with both source and channel coding. The simulation results demonstrate the desired efficiency of our scheme.

## Side-information-adaptive LDPC coding for distributed multi-view video coding over wireless sensor networks

- **Status**: ❌
- **Reason**: 분산 다시점 비디오 코딩(DMVC)용 LDPC—응용 특이적 소스코딩, 떼어낼 ECC 기법 없음
- **ID**: ieee:5339857
- **Type**: conference
- **Published**: 26-28 Aug.
- **Authors**: Zhang Bo, Zhang Lin, Liu Yu +1
- **PDF**: https://ieeexplore.ieee.org/document/5339857
- **Abstract**: Distributed multi-view video coding (DMVC) has become a focus due to the prosperity of the multimedia applications in wireless sensor networks. We propose a novel method of an adaptive scheme, named side-information-adaptive Low Density Parity Check (LDPC) coding. Apart from the existing multiple side-information implications in DMVC, this paper is dedicated to not only utilizing LDPC to produce the syndromes to realize DMVC, but exploiting preferable side-information search scheme for decoding scheme between the temporal and the inter-view correlation in DMVC. Simulation results illustrate the significant improvements of the proposed scheme with high motion in DMVC for high motion video.

## An iterative soft-decision decoding algorithm for conventional concatenated codes

- **Status**: ❌
- **Reason**: concatenated code의 KV+BCJR 반복 소프트디코딩—비-LDPC, BP 이식성 없음
- **ID**: ieee:5339712
- **Type**: conference
- **Published**: 26-28 Aug.
- **Authors**: Jingwei Zhang, Jiaying You, Lishuang Lu +1
- **PDF**: https://ieeexplore.ieee.org/document/5339712
- **Abstract**: In this paper, we present an iterative soft-decision decoding algorithm for conventional concatenated codes, which incorporates Koetter-Vardy (KV) algorithm for outer codes and Bahl-Cocke-Jelinek-Raviv (BCJR) algorithm for inner codes. After one round of decoding, the successfully decoded codewords from the outer decoder can be fed back to the inner decoder as constraint information. We compare several decoding algorithms for conventional concatenated codes in terms of the bit-error-rate (BER) performance. Simulation results show that, for conventional concatenated codes, performance improvements of about 0.4 dB and 0.1 dB can be achieved by the iterative soft-decision decoding algorithm over the conventional two-stage decoding algorithm and the iterative hard-decision decoding algorithm, respectively.

## Soft LDPC decoding in nonlinear channels with Gaussian processes for classification

- **Status**: ❌
- **Reason**: 비선형 채널 GPC 기반 등화기 제안, LDPC는 성능평가용 후단일 뿐 떼어낼 디코더 기법 없음
- **ID**: ieee:7077392
- **Type**: conference
- **Published**: 24-28 Aug.
- **Authors**: Pablo Martínez-Olmos, Juan José Murillo-Fuentes, Fernando Pérez-Cruz
- **PDF**: https://ieeexplore.ieee.org/document/7077392
- **Abstract**: In this paper, we propose a new approach for nonlinear equalization based on Gaussian processes for classification (GPC). We also measure the performance of the equalizer after a low-density parity-check channel decoder has detected the received sequence. Typically, most channel equalizers concentrate on reducing the bit error rate, instead of providing accurate posterior probability estimates. GPC is a Bayesian nonlinear classification tool that provides accurate posterior probability estimates with short training sequences. We show that the accuracy of these estimates is essential for optimal performance of the channel decoder and that the error rate outputted by the equalizer might be irrelevant to understand the performance of the overall communication receiver. We compare the proposed equalizers with state-of-the-art solutions.

## Blind time-period synchronization for LDPC Convolutionally Coded transmission

- **Status**: ❌
- **Reason**: LDPC-CC 블라인드 시간동기화 기법, 무선 동기화 특이적이며 떼어낼 디코더/HW/코드 기법 없음
- **ID**: ieee:7077660
- **Type**: conference
- **Published**: 24-28 Aug.
- **Authors**: Čedomir Stefanović, Dejan Vukobratović, Dragana Bajić +2
- **PDF**: https://ieeexplore.ieee.org/document/7077660
- **Abstract**: In this paper we propose a scheme for blind time-period synchronization of Low-Density Parity-Check Convolutional Codes (LDPC CC) over the AWGN channel. Reliable time-period synchronization for LDPC CC coded transmission is a requirement for successful decoding at the receiving end. The proposed scheme exploits parity-check constraints incorporated into LDPC CC coded stream, and variants based both on the hard and soft-detected symbols are presented. We show that time-period synchronization can be acquired during the time-frame of one LDPC CC time period, which is considerably faster and less complex when compared to the block LDPC coded transmission of similar performance. Additionally, by appending the time-period synchronization preprocessors, we effectively incorporate the time-period synchronization into the iterative LDPC CC decoder “pipeline” structure. Our simulation study demonstrates flexibility and excellent performance of the proposed scheme.

## On distributed arithmetic codes and syndrome based turbo codes for Slepian-Wolf coding of non uniform sources

- **Status**: ❌
- **Reason**: 분산 산술부호+turbo의 Slepian-Wolf 분산소스코딩, LDPC 아님이며 소스코딩 영역
- **ID**: ieee:7077599
- **Type**: conference
- **Published**: 24-28 Aug.
- **Authors**: V. Toto-Zarasoa, E. Magli, A. Roumy +1
- **PDF**: https://ieeexplore.ieee.org/document/7077599
- **Abstract**: We consider the use of source codes and channel codes for asymmetric distributed source coding of non uniform correlated sources. In particular, we use distributed arithmetic codes as source codes and syndrome based turbo codes as channel codes. We compare the advantages and drawbacks of the two systems for different source probabilities and different compression ratio. We show that prior knowledge of the source distribution improves the performance of both approaches in terms of their distances to the Slepian-Wolf bound. Turbo codes are better when the puncturing is low, while distributed arithmetic codes are less impacted by the change of compression rate.

## Network low density parity check codes designed for multiple-access relay channel

- **Status**: ❌
- **Reason**: 멀티액세스 릴레이용 network LDPC(네트워크코딩 결합) 설계 - NAND ECC에 떼어낼 기법 없는 응용 특이적
- **ID**: ieee:5291317
- **Type**: conference
- **Published**: 23-26 Aug.
- **Authors**: Guanghui Song, Ying Li, Jun Cheng +1
- **PDF**: https://ieeexplore.ieee.org/document/5291317
- **Abstract**: A relay scheme combining network coding with channel coding is proposed for multiple-access relay channel. Via a newly designed network low density parity check code, this scheme permits the relay node to jointly encode the data information from two source nodes. To predict the system performance, a newly generalized Gaussian approximation algorithm is derived, based on which an optimization algorithm is developed to search the degree distribution of the network LDPC code. Simulations show that, in a network with two sources, one relay and one destination, the system with the designed network low density parity check code hold a performance gap less than 0.6 dB from the threshold and a performance gain of about 0.3 dB can be achieved to the same rate XOR network coding scheme at BER = 10-5.

## Low density parity check codes for dedicated short range communication (DSRC) systems

- **Status**: ❌
- **Reason**: DSRC IVC에 표준 regular LDPC를 convolutional code와 성능 비교만; 새 디코더·구성 없음, 응용 특이적
- **ID**: ieee:5291266
- **Type**: conference
- **Published**: 23-26 Aug.
- **Authors**: Najmeh Khosroshahi, T. Aaron Gulliver
- **PDF**: https://ieeexplore.ieee.org/document/5291266
- **Abstract**: In this paper, we consider the performance of a dedicated short range communication (DSRC) system for inter-vehicle communications (IVC). The DSRC standard employs convolutional codes for forward error correction (FEC). The performance of the DSRC system is evaluated in three different channels with convolutional codes and regular LDPC codes. In addition, we compare the complexity of these codes. It is shown that LDPC codes provide a significant improvement in performance with similar complexity to convolutional codes.

## M-ary hyper phase-shift keying over non-linear satellite channels

- **Status**: ❌
- **Reason**: MHPSK 변조+RS/DVB-LDPC 베이스라인 위성통신 비교; LDPC 부수 언급, 떼어낼 기법 없음
- **ID**: ieee:5291402
- **Type**: conference
- **Published**: 23-26 Aug.
- **Authors**: James Caldwell, Clark Robertson
- **PDF**: https://ieeexplore.ieee.org/document/5291402
- **Abstract**: Forward error correction (FEC) coding in conjunction with M-ary hyper phase-shift keying (MHPSK) is considered in order to improve the robustness of a high spectral efficiency, non-linear satellite communications link. MHPSK is a spectrally efficient modulation technique that uses four orthonormal basis functions to increase the Euclidean distance between different symbols in the signal space. The use of four orthonormal basis functions provides an advantage over traditional spectrally efficient modulation techniques such as M-ary phase-shift keying (MPSK) and M-ary quadrature amplitude modulation (MQAM) that only possess two degrees of freedom. MHPSK offers an improvement in probability of bit error performance over other spectrally efficient modulation techniques for the same average energy per bit-to-noise power spectral density ratio and the same spectral efficiency. As a result, MHPSK offers a novel way to improve both throughput and reduce power requirements using easy to generate waveforms. MHPSK and two-subcarrier orthogonal frequency division multiplexing (OFDM) with 8-PSK or 8-QAM on each subcarrier are compared in terms of the effect of peak-to-average power ratio and required amplifier backoff on the probability of bit error. In this paper, long block length Reed Solomon (RS) codes are used to encode information symbols which are then transmitted with MHPSK. Additionally, a comparison is made with two-subcarrier OFDM that uses 8-PSK or 8-QAM on each subcarrier and utilizing the Digital Video Broadcast (DVB) standard rate 0.9 low density parity check (LDPC) code commonly employed in non-linear satellite communications. As such, MHPSK and two-subcarrier OFDM with 8-QAM or 8-PSK on each subcarrier are compared in terms of probability of bit error, peak-to-average power ratio, amplifier backoff, and bandwidth efficiency using long forward error correction code block lengths.

## A novel UEP Daul-Segment-Check H-ARQ

- **Status**: ❌
- **Reason**: UEP H-ARQ 메커니즘(FEC+ARQ+CRC), LDPC 비특정 FEC이고 떼어낼 디코더/구성 기법 없음
- **ID**: ieee:5276980
- **Type**: conference
- **Published**: 20-22 Aug.
- **Authors**: Zhibin Gao, Lianfen Huang, Yan Yao +1
- **PDF**: https://ieeexplore.ieee.org/document/5276980
- **Abstract**: In order to make multimedia data transmission more robust and meet QoS requirements over wireless channel, Forward Error Correction codes (FEC) are joint with Automatic Repeat-reQuest (ARQ) and a novel Dual-Segment-Check CRC, to form hybrid ARQ (H-ARQ) mechanism, making the system not only have strong error correcting capability and high throughput, but also can adaptively adjust code rate as channel state changes.

## Analysis of QIM-based audio watermarking using LDPC codes

- **Status**: ❌
- **Reason**: 오디오 워터마킹(QIM/DM)에 표준 Margulis LDPC를 그대로 사용, 신규 부호/디코더 기여 없음
- **ID**: ieee:5235992
- **Type**: conference
- **Published**: 2-5 Aug. 2
- **Authors**: R. Martinez-Noriega, M. Nakano, B. Kurkoski +2
- **PDF**: https://ieeexplore.ieee.org/document/5235992
- **Abstract**: In this paper, we analyze audio watermarking methods based on quantization index modulation and low-density parity-check (LDPC) codes. We found that dither modulation (DM) can achieve better performance using half-rate Margulis LDPC code even better than some low-rate codes. Then, we propose a scheme based on LDPC codes and DM with distortion-compensation (DC) property which has a robustness benefit of 6 dB versus uncoded case, 2 dB versus algebraic codes, 1 dB versus DM with LDPC code. In DM with DC property, we show that it is possible to achieve. 5 dB better robustness using a scale parameter alpha lower than the theoretically optimal and LDPC codes. Finally our proposal was evaluated against more practical attacks. These results show that our scheme could be a good option for robust watermarks.

## Density Evolution and Thresholds for Accumulate Repeat Tree Codes in Mobile Communication Systems

- **Status**: ❌
- **Reason**: ART(accumulate repeat tree) turbo-like 부호의 density evolution/threshold 분석, LDPC 자체가 아닌 새 부호족 이론, 떼어낼 바이너리 LDPC 기법 없음
- **ID**: ieee:5364641
- **Type**: conference
- **Published**: 14-16 Aug.
- **Authors**: Maofan Yang, Hua Zhou, Xin Zhang +1
- **PDF**: https://ieeexplore.ieee.org/document/5364641
- **Abstract**: Channel coding theories are widely used in computer science and communication systems. This paper proposes a novel channel coding scheme called accumulate repeat tree (ART) codes for improving the channel coding performance in mobile communication systems. This class of codes can be viewed as turbo-like codes combining many advantages of turbo codes and low-density parity-check (LDPC) codes. ART codes can be represented by the Bayesian network and Tanner graph, which allows for high-speed iterative decoding implementation using belief-propagation (BP) algorithm. The density evolution method is presented, and the practicable Gaussian approximation algorithm for ART codes to analyze the thresholds and decoding performance is discussed. ART codes have low coding complexity, and they show good performance improvement by simulation.
