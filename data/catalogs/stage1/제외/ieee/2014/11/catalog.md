# IEEE Xplore — 2014-11


## EXIT Chart Analysis of Nonbinary Protograph LDPC Codes for Partial Response Channels

- **Status**: ❌
- **Reason**: 비이진(GF(q)) protograph LDPC의 EXIT 분석 — non-binary는 기준상 제외
- **ID**: ieee:6971550
- **Type**: journal
- **Published**: Nov. 2014
- **Authors**: Watid Phakphisut, Pornchai Supnithi, Nattakan Puttarak
- **PDF**: https://ieeexplore.ieee.org/document/6971550
- **Abstract**: Low-density parity-check (LDPC) codes over finite fields GF( \({\boldsymbol {q}}\) ) provide an error correction in the noisy partial response (PR) channels. The extrinsic information transfer (EXIT) chart can be used to predict the threshold decoding of protograph LDPC codes, however, previous works only consider the binary protograph LDPC codes in the PR channels. In this paper, we propose to perform the EXIT chart analysis on the nonbinary protograph LDPC codes for the PR channels. Unlike prior works, the actual extrinsic information of the channel detector is measured, then the extrinsic information to the variable nodes is generated with the measured statistics. Moreover, since the mutual information of the variable nodes depends on GF( \({\boldsymbol {q}}\) ), we use the Monte Carlo method to approximate the mutual information. The analysis on the regular (2,4) code, regular (3,6) code, RA code, and AR3A code on the PR channels reveal that, for the PR1 channel, the RA code outperforms the others for  \({\boldsymbol {q}} = 2\) , 4, and 8, but the regular (2,4) code is the best for  \({\boldsymbol {q}} = 16\)  and 32. For the PR2 channel, the RA code is the best code for  \({\boldsymbol {q}} = 2\)  and 4, but the regular (2,4) code is the best code for  \({\boldsymbol {q}} > 4.\)  The simulation of the codes for  \({\boldsymbol {q}} = 4\)  and 16 are then used to confirm the theoretical results.

## Two-Dimensional Magnetic Recording Using a Rotated Head Array and LDPC Code Decoding

- **Status**: ❌
- **Reason**: TDMR 회전 헤드 어레이 성능 분석, 표준 QC-LDPC 디코딩 그대로 사용 — 신규 ECC 기여 없음
- **ID**: ieee:6971812
- **Type**: journal
- **Published**: Nov. 2014
- **Authors**: Yao Wang, Bo Yuan, Keshab K. Parhi +1
- **PDF**: https://ieeexplore.ieee.org/document/6971812
- **Abstract**: This paper examines the improvement in performance of rotated and normally oriented heads by using the quasi-cyclic low-density parity-check (QC-LDPC) code in a two-dimensional magnetic recording (TDMR) system. This paper indicates that the significant improvement in performance in the rotated head compared to the normally oriented head can be attributed to the larger amplitude of its dibit response and the reduced overlap between conditional probability density functions. Simulation also indicates that maximum areal densities of 9.85 T/in $^{2}$  and 6.64 T/in $^{2}$  can be reached by the rotated head array (RHA) and normally oriented head array (NHA) at optimum bit aspect ratios of 0.67 and 3.5 for 5.5 nm Voronoi grains, respectively. After decoding, the performance of the NHA is about 8.5 dB worse than the RHA. With an oversampled signal, 2-D linear minimum mean-squared error (LMMSE) equalizer and LDPC codes, a user bit density near 10 Tbits/in $^{2}$  is feasible for a rotated head array.

## Shuffled Multi-Track Detection for Shingled Magnetic Recording Channels With an Array of Read Heads

- **Status**: ❌
- **Reason**: SMR 멀티트랙 검출기(detector) 기법 + 비이진 LDPC — non-binary, 떼어낼 바이너리 LDPC 기법 없음
- **ID**: ieee:6971557
- **Type**: journal
- **Published**: Nov. 2014
- **Authors**: Guojun Han, Yong Liang Guan, Lingjun Kong
- **PDF**: https://ieeexplore.ieee.org/document/6971557
- **Abstract**: Shingled magnetic recording (SMR) with 2-D magnetic recording has recently emerged as a promising technology to sustain the growth of magnetic storage areal density. However, with the reduction of track pitch, the intertrack interference (ITI) becomes a major impairment. Furthermore, in SMR, the ITI is non-uniform among the top and lower tracks. A 2-D read channel which makes use of an array of read heads can effectively detect and compensate the severe ITI. In this paper, based on a read-array SMR channel model with non-uniform ITI, a shuffled multi-track detection (SMTD) detector, which shuffles and propagates the most reliable extrinsic information among the upper, lower, and middle detectors, is proposed to mitigate ITI more effectively. With the optimized non-binary low-density parity-check code, the performance of the proposed SMTD over the read-array SMR channel is evaluated.

## Precoding Mapping Optimization for Magnetic Recording Channels

- **Status**: ❌
- **Reason**: 자기기록 채널용 블록 프리코더(순열) 최적화 — LDPC ECC 기법 아님, turbo equalization 응용
- **ID**: ieee:6971549
- **Type**: journal
- **Published**: Nov. 2014
- **Authors**: Aman Bhatia, Shaohua Yang, Paul H. Siegel
- **PDF**: https://ieeexplore.ieee.org/document/6971549
- **Abstract**: We study the problem of designing a rate-1 block-precoder to minimize bit/symbol error rate when storing a given source on a magnetic recording channel. A block-precoder of length  \(b\) -bits is defined by a permutation  \(\pi \)  on  \(2^{b}\)  blocks. We show that the problem of finding a permutation for the block-precoder that minimizes bit/symbol error rate is equivalent to solving the quadratic assignment problem, a known combinatorial optimization problem that is NP-complete. We exploit the symmetry group of the  \(b\) -dimensional hypercube to reduce the search space, allowing a branch-and-bound technique to find the optimal 5-bit precoders. We also implement a local search algorithm that can find good precoders for larger blocklengths. We design precoders for MTR-constrained user bits and unconstrained parity bits with a reverse-concatenation architecture, and we evaluate the resulting SNR gains in a turbo equalization scheme.

## Scalable Compression of Stream Cipher Encrypted Images Through Context-Adaptive Sampling

- **Status**: ❌
- **Reason**: Scalable compression of encrypted images; source coding, not channel ECC.
- **ID**: ieee:6884840
- **Type**: journal
- **Published**: Nov. 2014
- **Authors**: Jiantao Zhou, Oscar C. Au, Guangtao Zhai +2
- **PDF**: https://ieeexplore.ieee.org/document/6884840
- **Abstract**: This paper proposes a novel scalable compression method for stream cipher encrypted images, where stream cipher is used in the standard format. The bit stream in the base layer is produced by coding a series of nonoverlapping patches of the uniformly down-sampled version of the encrypted image. An off-line learning approach can be exploited to model the reconstruction error from pixel samples of the original image patch, based on the intrinsic relationship between the local complexity and the length of the compressed bit stream. This error model leads to a greedy strategy of adaptively selecting pixels to be coded in the enhancement layer. At the decoder side, an iterative, multiscale technique is developed to reconstruct the image from all the available pixel samples. Experimental results demonstrate that the proposed scheme outperforms the state-of-the-arts in terms of both rate-distortion performance and visual quality of the reconstructed images at low and medium rate regions.

## Secrecy Transmission on Parallel Channels: Theoretical Limits and Performance of Practical Codes

- **Status**: ❌
- **Reason**: Physical layer secrecy/security on parallel channels; practical codes only as baseline, no transferable LDPC decoder/code/HW technique.
- **ID**: ieee:6879445
- **Type**: journal
- **Published**: Nov. 2014
- **Authors**: Marco Baldi, Franco Chiaraluce, Nicola Laurenti +2
- **PDF**: https://ieeexplore.ieee.org/document/6879445
- **Abstract**: We consider a system where an agent (Alice) aims at transmitting a message to a second agent (Bob) over a set of parallel channels, while keeping it secret from a third agent (Eve) by using physical layer security techniques. We assume that Alice perfectly knows the set of channels with respect to Bob, but she has only a statistical knowledge of the channels with respect to Eve. We derive bounds on the achievable outage secrecy rates, by considering coding either within each channel or across all parallel channels. Transmit power is adapted to the channel conditions, with a constraint on the average power over the whole transmission. We also focus on the maximum cumulative outage secrecy rate that can be achieved. Moreover, in order to assess the performance in a real life scenario, we consider the use of practical error correcting codes. We extend the definitions of security gap and equivocation rate, previously applied to the single additive white Gaussian noise channel, to Rayleigh distributed parallel channels, on the basis of the error rate targets and the outage probability. Bounds on these metrics are also derived, considering the statistics of the parallel channels. Numerical results are provided, that confirm the feasibility of the considered physical layer security techniques.

## Achievable Rates of MIMO Systems With Linear Precoding and Iterative LMMSE Detection

- **Status**: ❌
- **Reason**: MIMO linear precoding + iterative LMMSE detection; detection/precoding not an LDPC decoder, nothing to port to NAND LDPC.
- **ID**: ieee:6880374
- **Type**: journal
- **Published**: Nov. 2014
- **Authors**: Xiaojun Yuan, Li Ping, Chongbin Xu +1
- **PDF**: https://ieeexplore.ieee.org/document/6880374
- **Abstract**: We establish area theorems for iterative detection and decoding (or simply, iterative detection) over coded linear systems, including multiple-input multiple-output channels, intersymbol interference channels, and orthogonal frequency-division multiplexing systems. We propose a linear precoding technique that asymptotically ensures the Gaussianness of the messages passed in iterative detection, as the transmission block length tends to infinity. Area theorems are established to characterize the behavior of the iterative receiver. We show that, for unconstrained signaling, the proposed single-code scheme with linear precoding and iterative linear minimum mean-square error (LMMSE) detection is potentially information lossless, under various assumptions on the availability of the channel state information at the transmitter. We further show that, for constrained signaling, our proposed single-code scheme considerably outperforms the conventional multicode parallel transmission scheme based on singular value decomposition and water-filling power allocation. Numerical results are provided to verify our analysis.

## Quantum Synchronizable Codes From Finite Geometries

- **Status**: ❌
- **Reason**: Quantum synchronizable codes from cyclic/finite-geometry/BCH codes; quantum EC, not binary LDPC.
- **ID**: ieee:6895165
- **Type**: journal
- **Published**: Nov. 2014
- **Authors**: Yuichiro Fujiwara, Peter Vandendriessche
- **PDF**: https://ieeexplore.ieee.org/document/6895165
- **Abstract**: Quantum synchronizable error-correcting codes are special quantum error-correcting codes that are designed to correct both the effect of quantum noise on qubits and misalignment in block synchronization. It is known that, in principle, such a code can be constructed through a combination of a classical linear code and its subcode if the two are both cyclic and dual-containing. However, finding such classical codes that lead to promising quantum synchronizable error-correcting codes is not a trivial task. In fact, although there are two families of classical codes that are proved to produce quantum synchronizable codes with good minimum distances and highest possible tolerance against misalignment, their code lengths have been restricted to primes and Mersenne numbers. In this paper, examining the incidence vectors of projective spaces over the finite fields of characteristic 2, we give quantum synchronizable codes from cyclic codes whose lengths are not primes or Mersenne numbers. These projective geometric codes achieve good performance in quantum error correction and possess the best possible ability to recover synchronization, thereby enriching the variety of good quantum synchronizable codes. We also extend the current knowledge of cyclic codes in classical coding theory by explicitly giving generator polynomials of the finite geometric codes and completely characterizing the minimum weight nonzero codewords. In addition to the codes based on projective spaces, we carry out a similar analysis on the well-known cyclic codes from Euclidean spaces that are known to be majority logic decodable and determine their exact minimum distances.

## On the Convergence and Optimality of Reweighted Message Passing for Channel Assignment Problems

- **Status**: ❌
- **Reason**: Reweighted message passing for OFDMA channel/b-matching assignment optimization, not channel ECC; not transferable to LDPC BP.
- **ID**: ieee:6851895
- **Type**: journal
- **Published**: Nov. 2014
- **Authors**: Marco Moretti, Andrea Abrardo, Marco Belleschi
- **PDF**: https://ieeexplore.ieee.org/document/6851895
- **Abstract**: Many assignment problems, and channel allocation in OFDMA networks is a typical example, can be formulated as bipartite weighted b-matching (BWBM) problems. In this letter we provide a proof of the convergence and the optimality of the reweighted message passing (ReMP) algorithm when applied to solve BWBM problems in a distributed fashion. To this aim, we first show that the ReMP rule is a contraction mapping under a maximum mapping norm. Then, we show that the fixed convergence point is an optimal solution for the original assignment problem.

## Ant Colony Optimization-Based Fault-Aware Routing in Mesh-Based Network-on-Chip Systems

- **Status**: ❌
- **Reason**: Ant-colony fault-aware routing for NoC; unrelated to LDPC ECC.
- **ID**: ieee:6926921
- **Type**: journal
- **Published**: Nov. 2014
- **Authors**: Hsien-Kai Hsin, En-Jui Chang, Chia-An Lin +1
- **PDF**: https://ieeexplore.ieee.org/document/6926921
- **Abstract**: The advanced deep submicrometer technology increases the risk of failure for on-chip components. In advanced network-on-chip (NoC) systems, the failure constrains the on-chip bandwidth and network throughput. Fault-tolerant routing algorithms aim to alleviate the impact on performance. However, few works have integrated the congestion-, deadlock-, and fault-awareness information in channel evaluation function to avoid the hotspot around the faulty router. To solve this problem, we propose the ant colony optimization-based fault-aware routing (ACO-FAR) algorithm for load balancing in faulty networks. The behavior of an ant colony while facing an obstacle (failure in NoC) can be described in three steps: 1) encounter; 2) search; and 3) select. We implement the corresponding mechanisms as: 1) notification of fault information; 2) path searching mechanism; and 3) path selecting mechanism. With proposed ACO-FAR, the router can evaluate the available paths and detour packets through a less-congested fault-free path. The simulation results show that this paper has higher throughput than related works by 29.1%–66.5%. In addition, ACO-FAR can reduce the undelivered packet ratio to 0.5%–0.02% and balance the distribution of traffic flow in the faulty network.

## Soft-Decision-Aided Channel Estimation Over the Flat-Fading Channel, and an Application to Iterative Decoding Using an Example LTE Turbo Code

- **Status**: ❌
- **Reason**: Soft-decision channel estimation + LTE turbo code; channel estimation/turbo, no LDPC technique to port.
- **ID**: ieee:6919284
- **Type**: journal
- **Published**: Nov. 2014
- **Authors**: Haifeng Yuan, Pooi-Yuen Kam
- **PDF**: https://ieeexplore.ieee.org/document/6919284
- **Abstract**: We consider transmissions over the frequency-nonselective time-selective fading channel and derive the soft-decision-aided maximum a posteriori probability (SDA-MAP) channel estimator that utilizes the entire received signal sequence, including both pilot signals and data signals, and the a priori statistical information of the transmitted data symbols. This paper theoretically demonstrates how the soft data decisions should be incorporated into the channel estimation process. An iterative implementation of the SDA-MAP estimator is proposed, which uses the feedback of earlier soft decisions and the feedforward of later soft decisions to estimate the current channel gain. This approximate SDA-MAP implementation is similar in structure to the expectation-maximization algorithm. Simulation results show that the receiver using this iterative SDA-MAP estimator outperforms the conventional pilot-symbol-assisted modulation receiver in which the channel estimates are obtained from only the pilot signals. An application to iterative decoding using the LTE turbo code is also provided.

## Evaluation of Multiple Reader Location for TDMR R/W Channel

- **Status**: ❌
- **Reason**: TDMR 리더 배치/BER 평가, 표준 LDPC 반복디코딩 시스템 사용 — 떼어낼 신규 디코더/HW/코드설계 없음
- **ID**: ieee:6971422
- **Type**: journal
- **Published**: Nov. 2014
- **Authors**: Yasuaki Nakamura, Naoki Fujimoto, Yoshihiro Okamoto +2
- **PDF**: https://ieeexplore.ieee.org/document/6971422
- **Abstract**: The two-dimensional magnetic recording (TDMR) by shingled magnetic recording needs two-dimensional (TD) signal processing using the multiple read-back waveforms. In this paper, to allocate dual readers (reader 1 and 2) for the intended tracks, we evaluate the bit error rate (BER) performance of a low-density parity-check coding and iterative decoding system with a TD-finite impulse response equalizer under TDMR R/W channel specifications of 4 Tb/in \(^{2}\) . Here, the TDMR R/W channel is modeled using a discretized granular medium and the writing process based on a slope model considering the media switching field angle given by the Stoner–Walfarth reversal mechanism. The result shows that to affect the good BER performance, the reader 1 should be placed slightly toward the next track from the center of the home track, and the reader 2 should be placed around the boundary between the home and following tracks.

## Degree distribution mapping method of parity check matrix in LDPC based FSO communication through atmospheric turbulence channel

- **Status**: ❌
- **Reason**: FSO 대기난류 채널 추정 피드백에 맞춘 QC-LDPC degree distribution 매핑 — 채널적응 코드선택 응용, 표준 QC-LDPC 사용, 떼어낼 신규 구성/디코더 기법 없음.
- **ID**: ieee:6987132
- **Type**: conference
- **Published**: 9-10 Nov. 
- **Authors**: Fei Xiao, Lijia Zhang, Bo Liu +6
- **PDF**: https://ieeexplore.ieee.org/document/6987132
- **Abstract**: A degree distribution mapping method of parity check matrix in irregular QC-LDPC based FSO communication is proposed. Before channel coding, use the mapping method to select the appropriate distribution of the parity check matrix corresponding to atmospheric channel estimation feedback. BER performance of the optimal distribution of the parity check matrix in different turbulence intensity has been made. Compared to old coding schemes without optimizing degree distribution, the new one have greatly improved the transmission performance.

## The application of fountain code in differential frequency hopping systems

- **Status**: ❌
- **Reason**: Fountain 부호 DFH 안티재밍 응용 — fountain, 떼어낼 LDPC ECC 기법 없음
- **ID**: ieee:7106884
- **Type**: conference
- **Published**: 8-10 Nov. 
- **Authors**: Wenjie Zhu, Benshun Yi, Liangcai Gan +1
- **PDF**: https://ieeexplore.ieee.org/document/7106884
- **Abstract**: Based on the anti-jamming performance of differential frequency hopping (DFH) systems in Additive White Gaussian Noise (AWGN) channel, Fountain code is introduced to the DFH systems as the outer error correcting code in this paper to investigate the improvements against partial-band jamming over AWGN channel. The performance of Fountain coded DFH is theoretically analyzed and numerically simulated. The total frequencies of hopping in the simulation is 16, and results show that, on one hand, when exact jamming state information (JSI) is available, and the number of jamming frequency is n=16, the bit error rate (BER) of 10-3 is achieved with the signal to interference ratio (SIR) approximately 7.5 dB over AWGN channel, and the performance improves about 1-1.5dB compared with the no-coded system. When the number of jamming frequency is n=2, the performance increases 15-17dB. The anti-jamming performance of Fountain coded DFH systems is obviously superior to no-coded DFH systems.

## Symbol-flipping decoding of nonbinary LDPC codes over BI-AWGN channels

- **Status**: ❌
- **Reason**: 비이진(NB-LDPC, q-ary) symbol-flipping 디코더 — 비이진 LDPC는 제외 대상
- **ID**: ieee:7041866
- **Type**: conference
- **Published**: 5-7 Nov. 2
- **Authors**: Lailson F. dos Santos, Jaime Portugheis, Celso de Almeida
- **PDF**: https://ieeexplore.ieee.org/document/7041866
- **Abstract**: This paper analyzes a weighted symbol-flipping (SF) algorithm for nonbinary low density parity-check (NB-LDPC) codes over binary input AWGN (BI-AWGN) channels. The weighted SF algorithm has two main parts: the symbol-flipping function and the new candidate symbol rule. First, it is demonstrated that a rule for choosing the new candidate symbol based on absolute values of observed channel outputs is equivalent to a rule based on Euclidean distances. Then, it is verified that the weighting factor of flipping function has negligible impact on algorithm performance. Motivated by this fact, a SF decoding algorithm is proposed whose flipping function requires only syndrome values and flips symbols in parallel. It is observed that SF decoding outperforms WSF for q-ary codes with large q.

## Efficient Min-Max nonbinary LDPC decoding on GPU

- **Status**: ❌
- **Reason**: 비이진 NB-LDPC Min-Max GPU 디코더, non-binary LDPC라 제외
- **ID**: ieee:7087640
- **Type**: conference
- **Published**: 3-6 Nov. 2
- **Authors**: Huyen Pham Thi, Sabooh Ajaz, Hanho Lee
- **PDF**: https://ieeexplore.ieee.org/document/7087640
- **Abstract**: This paper presents an novel modified Min-Max algorithm (MMMA) and an efficient implementation of an nonbinary LDPC (NB-LDPC) decoder on a graphics processing unit (GPU) to achieve both great flexibility and scalability. The MMMA for check node processing removes the multiplications over Galois-field in merger step and significantly reduces the decoding latency. The proposed MMMA provides a better BER performance than previous algorithm. The experimental results show that the GPU-based implementation of the proposed NB-LDPC decoder provides higher throughput and the coding gain under low 10−8 BER comparted to CPU-based implementation.

## Hybrid automatic repeat request protocols: Turbo-Codes against Cyclic Binary low-density parity-check codes

- **Status**: ❌
- **Reason**: HARQ 프로토콜에서 Turbo vs cyclic binary LDPC 비교, 표준 부호 사용에 무선 처리량 응용일 뿐 떼어낼 신규 디코더/구성 없음
- **ID**: ieee:7107904
- **Type**: conference
- **Published**: 27-28 Nov.
- **Authors**: Anouar Yatribi, Fouad Ayoub, Zakaria M'rabet +2
- **PDF**: https://ieeexplore.ieee.org/document/7107904
- **Abstract**: Hybrid ARQ is defined as the joint use of a retransmission protocol ARQ and forward error coding (FEC) at the transmitter and/or receiver. We will focus on the HARQ-type-II protocols, namely type-II-CC (Chase Combining) characterized by a storage and combination of erroneous packets, and the type-II-IR (Incremental Redundancy) which provides an Incremental Redundancy strategy that helps to increase the throughput. These two strategies are used by the new mobile communications networks. The HARQ transmission performance depends especially on the selected retransmission protocol (ARQ), and on the model of the forward error correction code (FEC). In this paper, we propose a comparison of the HARQ protocols using two different FEC Codes, in the first hand we use the Turbo Codes, referring to 4G LTE networks, in the other hand we propose a new transmission scheme using a Cyclic Binary LDPC Code with a higher coderate. This study will allow us to reach an optimized transmission scheme based on a combination of coding and retransmission (HARQ), in order to provide higher average throughputs and reliable radio transmissions over all the SNR values.

## An enhanced coding and decoding method for raptor codes over fading channels

- **Status**: ❌
- **Reason**: Raptor(LT+LDPC) 부호 fading 채널 디코딩 개선 — fountain/concatenated 기반, LDPC가 외부코드일 뿐 NAND 바이너리 LDPC BP에 떼어낼 신규 기법 없음
- **ID**: ieee:7020875
- **Type**: conference
- **Published**: 26-28 Nov.
- **Authors**: Lingyi Han, Yuexing Peng, Hui Zhao
- **PDF**: https://ieeexplore.ieee.org/document/7020875
- **Abstract**: In this paper, an improved decoding algorithm is developed for Raptor codes in fading channels to enhance its error performance. As the classic decoding algorithm of the Raptor codes is designed for erasure channels and its error performance degrades severely over the fading channels, a modified coding and decoding algorithm is developed for Raptor codes with short codeword length in fading channels. A random interleaver is introduced between the inner LT code and the outer LDPC code, and then an iterative soft information upgrading and transferring-based decoding algorithm under Turbo principle is employed to combat the fading. Simulation results show the presented coding and decoding algorithm can enhance the bit error rate(BER) performance of Raptor codes in fading channels.

## Algorithm of choice a multiposition keying in wireless system with LDPC coding

- **Status**: ❌
- **Reason**: 무선 다위치 키잉+LDPC 조합 선택 알고리즘 — 무선 응용 특이적, 떼어낼 LDPC ECC 기법 없음
- **ID**: ieee:7034433
- **Type**: conference
- **Published**: 25-27 Nov.
- **Authors**: Leonid Uryvsky, Alina Moshynska, Serhii Osypchuk
- **PDF**: https://ieeexplore.ieee.org/document/7034433
- **Abstract**: The algorithm of choice an optimal combination of multiposition keying and antinoise code is proposed in this paper. The criterion for selecting the optimal combination is the maximal productivity in base station coverage area of mobile communication.

## Annotation of cultural heritage 3-D models by robust data embedding in the object mesh

- **Status**: ❌
- **Reason**: 3D 메쉬 워터마킹/데이터 임베딩, runlength+QIM — 채널 ECC 아님, LDPC 무관
- **ID**: ieee:7034538
- **Type**: conference
- **Published**: 25-27 Nov.
- **Authors**: Bata Vasić
- **PDF**: https://ieeexplore.ieee.org/document/7034538
- **Abstract**: This paper presents a novel method of the low-level data hiding for the cultural heritage watermarking and authentication. Method involves the algorithm for robust and blind embedding the data bits into a geometrical structure of three-dimensional (3D) mesh models and the data protection algorithm. In the first step the vector of the stabile vertex is selected using powerful vertex extraction algorithm, which calculates the most relevant geometrical and topological features of the 3D mesh model. Watermark and/or authentication data is subjected to an error-correction encoding in the second step of the algorithm. The runlength encoding converts protected bits to a run of bits to ensure synchronization and thus converts a deletion channel with infinite memory to a memoryless channel. Finally, data bits are embedded into structure of the cultural heritage model by changing the spatial Euclidean positions of mesh primitives. Choosing the one of two quantizers of the Quantization Index Modulation (QIM) algorithm determines a value of the embedded data bit. Watermark and/or authentication data is extracted from a stego object in the reverse process using the stego key only. Due to the retrieving phase of algorithm does not need information about original model a blindness of the whole process is ensured.

## Low complexity technique exploiting 2D source correlation using single parity check codes

- **Status**: ❌
- **Reason**: JSCC + turbo SPC 부호 기반, 소스상관 디코딩으로 LDPC ECC 아님, 떼어낼 BP 기법 없음 (JSCC/비-LDPC 제외)
- **ID**: ieee:7238188
- **Type**: conference
- **Published**: 24-26 Nov.
- **Authors**: Mohd Azri Mohd Izhar, Hazilah Mad Kaidi, Rudzidatul Akmam Dziyauddin +1
- **PDF**: https://ieeexplore.ieee.org/document/7238188
- **Abstract**: This paper proposes a low complexity joint source-channel coding (JSCC) technique that can well exploit two-dimensional (2D) source correlation using turbo single parity check (SPC) codes. Based on similar structure of the product accumulate code, a rate-1 inner code is serially concatenated to the turbo SPC code structure in order to overcome the high error floor issue of turbo SPC codes. The 2D source correlation, horizontal and vertical directions of the source are exploited during the decoding process. In order to exploit the source statistics (i.e. transition probabilities), a decoding algorithm based on modified check operation is proposed. This modified check operation has significantly lower computational complexity than the previous technique that based on modified Bahl-Cocke-Jelinek-Raviv (BCJR) algorithm. Simulation results reveal that the proposed technique that based on modified check operation achieves about 4.5 times lower computational complexity than the technique that based on modified BCJR algorithm. In addition to the lower computational complexity, the proposed JSCC technique can achieve optimal performance, similar with the technique that based on modified BCJR algorithm. The interesting features of low computational complexity and high performance of the proposed technique is important in designing JSCC system exploiting higher dimensional source correlation.

## Design of non-binary quasi-cyclic LDPC codes by absorbing set removal

- **Status**: ❌
- **Reason**: 비이진(NB-QC) LDPC absorbing set 제거 — non-binary는 기준상 제외
- **ID**: ieee:6970874
- **Type**: conference
- **Published**: 2-5 Nov. 2
- **Authors**: Behzad Amiri, Jorge Arturo Flores Castro, Lara Dolecek
- **PDF**: https://ieeexplore.ieee.org/document/6970874
- **Abstract**: Non-binary quasi-cyclic (NB-QC) codes are a class of graph-based codes with high performance and implementation-friendly structure. In this paper, we introduce a new method for designing NB-QC codes with improved performance in the low error-rate region. Specifically, we propose a construction which reduces the number of non-binary absorbing sets, which are known to cause errors when decoding non-binary LDPC codes. Our construction is based on a careful selection of the code design parameters. Simulation results demonstrate the superior performance of codes designed according to our technique compared to existing state-of-the-art NB-QC codes.

## Feedback systems using non-binary LDPC codes with a limited number of transmissions

- **Status**: ❌
- **Reason**: 비이진(NB) LDPC + 피드백 전송길이 최적화, 비이진 LDPC는 제외 대상
- **ID**: ieee:6970814
- **Type**: conference
- **Published**: 2-5 Nov. 2
- **Authors**: Kasra Vakilinia, Adam R. Williamson, Sudarsan V. S. Ranganathan +2
- **PDF**: https://ieeexplore.ieee.org/document/6970814
- **Abstract**: One advantage of incremental transmissions with feedback in point-to-point memoryless channels is a reduction in average blocklength required to approach capacity. This paper optimizes the size of each incremental transmission for non-binary (NB) LDPC codes to maximize throughput in VLFT and two-phase VLF settings. The optimization problem uses an approximation based on the inverse-Gaussian p.d.f. of the blocklength required for successful decoding. By using the optimized incremental transmission lengths (with an average blocklength of less than 500 bits), NB-LDPC codes for VLFT setting limited to 5 transmissions achieve a throughput greater than 96% of that obtained by an unlimited-transmission VLFT scheme with the same average blocklength. With a similar average blocklength, a two-phase VLF system limited to five transmissions (with optimized lengths) using the binary image of NB-LDPC codes achieves greater than 90% of the capacity of binary-input AWGN channel with SNR=2 dB. Two-phase VLF does not match the throughput of VLFT, but it is more practical than VLFT because it does not assume noiseless transmitter confirmation.

## Field-order based hardware cost analysis of non-binary LDPC decoders

- **Status**: ❌
- **Reason**: 비이진(GF(q)) LDPC 디코더 HW 분석 — 비이진 LDPC는 제외 대상
- **ID**: ieee:7094832
- **Type**: conference
- **Published**: 2-5 Nov. 2
- **Authors**: Yuta Toriyama, Behzad Amiri, Lara Dolecek +1
- **PDF**: https://ieeexplore.ieee.org/document/7094832
- **Abstract**: Non-binary low-density parity-check codes exhibit excellent coding gain at the cost of decoding complexity. Furthermore, the effects of the Galois field order on the hardware cost have not been well established. We propose a modification to the Min-Max algorithm to simplify calculations while maintaining decoding performance. In addition, a hardware area efficiency analysis is proposed, allowing a quantified exploration of the decoder design space. This analysis reveals that the proposed algorithm yields multiple choices: a GF(4) decoder with 2x hardware efficiency or a GF(8) decoder with 1dB coding gain, relative to the original algorithm in GF(4).

## Delay-exponent of bilayer anytime code

- **Status**: ❌
- **Reason**: 릴레이망 anytime code 응용 특이적; delay-exponent 이론 분석으로 떼어낼 디코더/HW/구성 기여 없음
- **ID**: ieee:6970872
- **Type**: conference
- **Published**: 2-5 Nov. 2
- **Authors**: Md. Noor-A-Rahim, Khoa D. Nguyen, Gottfried Lechner
- **PDF**: https://ieeexplore.ieee.org/document/6970872
- **Abstract**: In this paper, we study the design and the delay-exponent of anytime codes over a three terminal relay network. We propose a bilayer anytime code based on anytime spatially coupled low-density parity-check (LDPC) codes and investigate the anytime characteristics through density evolution analysis. By using mathematical induction technique, we find analytical expressions of the delay-exponent for the proposed code. Through comparison, we show that the analytical delay-exponent has a close match with the delay-exponent obtained from numerical results.

## Shaping low-density lattice codes using Voronoi integers

- **Status**: ❌
- **Reason**: LDLC(저밀도 격자부호) shaping gain 기법, 바이너리 LDPC ECC 아님
- **ID**: ieee:6970806
- **Type**: conference
- **Published**: 2-5 Nov. 2
- **Authors**: Nuwan S. Ferdinand, Brian M. Kurkoski, Behnaam Aazhang +1
- **PDF**: https://ieeexplore.ieee.org/document/6970806
- **Abstract**: A lattice code construction that employs two separate lattices, a high dimension lattice for coding gain and a low-dimension lattice for shaping gain, is described. Systematic lattice encoding is a method to encode an integer sequence to a lattice point that is nearby that integer sequence. We describe the “Voronoi integers” ℤm/Λs, the set of integers inside the fundamental Voronoi region of a shaping lattice Λs, and a concrete scheme to label these integers. By first shaping the information using the Voronoi integers in low dimension, and then performing systematic lattice encoding using a high-dimension lattice, good shaping and coding gains can be simultaneously obtained. We concentrate on the case of using the E8 lattice for shaping and low-density lattice codes (LDLC) with dimension ~ 10,000 for coding. While optimal shaping provides a well-known 1.53 dB gain, previously reported shaping gains with LDLC lattices are on the order of 0.4 dB. The proposed method preserves the shaping gain of the E8 lattice, that is, as much as 0.65 dB. This shaping operation can be implemented with lower complexity than previous LDLC approaches.

## From LDPC to chunked network codes

- **Status**: ❌
- **Reason**: LDPC를 청크 네트워크코딩 구성에 활용, 채널 ECC가 아닌 네트워크코딩 응용으로 떼어낼 ECC 기법 없음
- **ID**: ieee:6970863
- **Type**: conference
- **Published**: 2-5 Nov. 2
- **Authors**: Shenghao Yang, Bin Tang
- **PDF**: https://ieeexplore.ieee.org/document/6970863
- **Abstract**: Chunked network code is a variation of random linear network code with low computational cost and small coefficient vector overhead. In a chunked network code, intermediate network nodes only apply network coding among packets of the same chunk. In this paper, we propose an approach to construct chunks using LDPC codes. For a given LDPC code, the chunks are simply formed by first partitioning the variable nodes into disjoint groups and then filling each group with a number of variable nodes of degree zero. The chunked network codes constructed using this approach are called L-chunked codes. We analyze the asymptotic achievable rates of L-chunked codes using belief propagation decoding for an arbitrary rank distribution of the chunk transfer matrices. Numerical evaluation shows that L-chunked codes achieve a rate very close to optimal.

## Quasi-primitive block-wise concatenated BCH codes for NAND flash memories

- **Status**: ❌
- **Reason**: NAND용이나 비-LDPC(BCH 연접)부호 설계; LDPC는 비교 베이스라인일 뿐 떼어낼 LDPC 기법 없음
- **ID**: ieee:6970904
- **Type**: conference
- **Published**: 2-5 Nov. 2
- **Authors**: Daesung Kim, Jeongseok Ha
- **PDF**: https://ieeexplore.ieee.org/document/6970904
- **Abstract**: In this work, we consider high-rate error-control systems based on block-wise concatenated Bose-Chaudhuri-Hocquenghem (BC-BCH) codes with iterative hard-decision decoding (IHDD) for storage devices using multi-level per cell (MLC) NAND flash memories. In particular, we propose a novel design rule of BC-BCH codes which consists of quasi-primitive BCH codes and block-wise concatenation of the constituent codes. Comprehensive performance comparisons are carried out among error-control systems with various coding schemes such as BC-BCH codes and LDPC codes.

## Performance analysis of a MMSE turbo equalizer with LDPC in a FTN channel with application to digital video broadcast

- **Status**: ❌
- **Reason**: FTN 채널 MMSE turbo equalizer + LDPC 디코더(베이스라인) — 떼어낼 LDPC ECC 기법 없음, 통신 응용 특이
- **ID**: ieee:7094793
- **Type**: conference
- **Published**: 2-5 Nov. 2
- **Authors**: Ghassan Maalouli, Brian A. Bannister
- **PDF**: https://ieeexplore.ieee.org/document/7094793
- **Abstract**: Faster-than-Nyquist (FTN) involves the transmission of information over the channel at a rate exceeding the inter-symbol interference (ISI) free rate proposed by Nyquist. FTN aims to increase channel capacity at a cost of inducing ISI. Effective use of FTN requires ISI mitigation to a level such that there is a net gain in capacity at a given SNR. Prior work demonstrated that a computationally-complex BCJR turbo-equalization scheme can mitigate ISI and result in a net gain. However, the BCJR is infeasible for practical applications where complex modulations are involved. In this work, we analyze the performance of a computationally efficient, MMSE-based, turbo-equalizer using a LDPC decoder with application to digital-video broadcast satellite channel and assess its ability to mitigate FTN induced ISI.

## Lattices from codes for harnessing interference: An overview and generalizations

- **Status**: ❌
- **Reason**: 코드로부터 격자 구성(Construction A/D/πA) 간섭완화용; 순수 이론/격자 구성으로 NAND LDPC 디코더/HW로 안 이어짐
- **ID**: ieee:6970782
- **Type**: conference
- **Published**: 2-5 Nov. 2
- **Authors**: Yu-Chih Huang, Krishna R. Narayanan
- **PDF**: https://ieeexplore.ieee.org/document/6970782
- **Abstract**: In this paper, using compute-and-forward as an example, we provide an overview of constructions of lattices from codes that possess the right algebraic structures for harnessing interference. This includes Construction A, Construction D, and Construction πA (previously called product construction) recently proposed by the authors. While most of the results in this paper have been available in the literature, we discuss two generalizations where the first one is a general construction of lattices named Construction πD subsuming the above three constructions as special cases and the second one is to go beyond principal ideal domains and build lattices over algebraic integers.

## Generalized low-density (GLD) lattices

- **Status**: ❌
- **Reason**: GLD 격자 구성(lattice sphere packing) 채널코딩/물리계층/보안용, 바이너리 LDPC ECC로 떼어낼 디코더·HW·코드설계 기법 없음
- **ID**: ieee:6970783
- **Type**: conference
- **Published**: 2-5 Nov. 2
- **Authors**: Joseph J. Boutros, Nicola di Pietro, Nour Basha
- **PDF**: https://ieeexplore.ieee.org/document/6970783
- **Abstract**: We propose the construction of a new family of lattice sphere packings. Given a small-dimensional lattice, we start by building a first lattice in a large dimension by the direct sum of the small lattice. Then, the coordinates of the first large lattice are permuted to yield a second large-dimensional lattice. Finally, our generalized low-density (GLD) lattice is the intersection of the first and the second lattice. We restrict our construction in this paper to integer lattices. GLD lattices are the result of mixing classical lattice theory with modern coding theory. They are potential candidates not only for channel coding as coded modulations, but also for physical-layer network coding and for secure digital communications.

## Multilevel coding for non-orthogonal broadcast

- **Status**: ❌
- **Reason**: 비직교 브로드캐스트용 멀티레벨 코딩(유한체 부호) — LDPC 디코더/구성 기여 없음, 통신 응용
- **ID**: ieee:7094799
- **Type**: conference
- **Published**: 2-5 Nov. 2
- **Authors**: Stephan Pfletschinger, Monica Navarro, Christian Ibars
- **PDF**: https://ieeexplore.ieee.org/document/7094799
- **Abstract**: This paper defines an information-theoretical framework for non-orthogonal broadcast systems with multilevel coding and gives design guidelines for the rate selection of multiple broadcast streams. This description includes hierarchical modulation and superposition coding with codes defined in a finite field as a special case. We show how multilevel coding can be applied to multiple antennas where, in contrast to most spacetime coding and hierarchical modulation schemes, no capacity loss occurs.

## A low-complexity improved successive cancellation decoder for polar codes

- **Status**: ❌
- **Reason**: Polar SC-flip 디코더 — 비-LDPC, SC 특화라 바이너리 LDPC BP에 이식되지 않음
- **ID**: ieee:7094848
- **Type**: conference
- **Published**: 2-5 Nov. 2
- **Authors**: Orion Afisiadis, Alexios Balatsoukas-Stimming, Andreas Burg
- **PDF**: https://ieeexplore.ieee.org/document/7094848
- **Abstract**: Under successive cancellation (SC) decoding, polar codes are inferior to other codes of similar blocklength in terms of frame error rate. While more sophisticated decoding algorithms such as list- or stack-decoding partially mitigate this performance loss, they suffer from an increase in complexity. In this paper, we describe a new flavor of the SC decoder, called the SC flip decoder. Our algorithm preserves the low memory requirements of the basic SC decoder and adjusts the required decoding effort to the signal quality. In the waterfall region, its average computational complexity is almost as low as that of the SC decoder.

## A new multiple folded successive cancellation decoder for polar codes

- **Status**: ❌
- **Reason**: polar 코드 SCD folding 디코더 — polar 전용 인코딩 그래프 의존, 바이너리 LDPC BP로 이식 불가
- **ID**: ieee:6970858
- **Type**: conference
- **Published**: 2-5 Nov. 2
- **Authors**: Harish Vangala, Emanuele Viterbo, Yi Hong
- **PDF**: https://ieeexplore.ieee.org/document/6970858
- **Abstract**: We consider a new variant of successive cancellation decoder (SCD) for polar codes based on the concept of folding, which was proposed in [1], [2] as technique to reduce the decoding latency at the cost of a higher computational complexity. In this paper, we first formally define the multiple folding operation (iterated κ times), which decomposes the original encoding graph into a number of smaller polar encoding graphs. More specifically, we show that the multiple folding gives rise to a two stage interpretation of the graph representing the polar encoder and the SCD. Based on this, we propose the improved multiple folded successive cancellation decoder (IMFSCD), which combines SCD in one stage and maximum-likelihood decoding in the other. This decoder exhibits a latency gain by a factor of 2κ, still retaining a complexity close to the classic SCD. The small increase in complexity is due to a short maximum likelihood decoder (MLD) used in place of a SCD in the last decoding stage within the IMFSCD. Moreover, we observe by simulation that the decoder performance is exactly the same as that of an SCD at all rates.

## MMSE scaling enhances performance in practical lattice codes

- **Status**: ❌
- **Reason**: LDLC 격자부호용 MMSE 스케일링/BP — 바이너리 LDPC ECC 아님, 이식 기법 없음
- **ID**: ieee:7094608
- **Type**: conference
- **Published**: 2-5 Nov. 2
- **Authors**: Nuwan S. Ferdinand, Matthew Nokleby, Brian M. Kurkoski +1
- **PDF**: https://ieeexplore.ieee.org/document/7094608
- **Abstract**: We investigate the value of MMSE scaling for practical lattice codes. For ideal lattices, MMSE scaling has been shown to be a key ingredient in achieving the capacity of the AWGN channel. We demonstrate that MMSE scaling enhances the performance, particularly at low SNR, for practical lattice codes. For example, a dimension n = 10000 LDLC lattice exhibits approximately 0.6 dB gain when MMSE scaling is used for a rate of 1 bit/dimension. Furthermore, we provide a novel derivation of the MMSE scaling rule, showing that it emerges naturally from principles of belief propagation decoders which account for the transmit power constraint.

## Superposition lattice coding for Gaussian broadcast channel with confidential message

- **Status**: ❌
- **Reason**: 가우시안 브로드캐스트 보안용 superposition lattice coding, 바이너리 LDPC ECC 기법 없음
- **ID**: ieee:6970844
- **Type**: conference
- **Published**: 2-5 Nov. 2
- **Authors**: Li-Chia Choo, Cong Ling
- **PDF**: https://ieeexplore.ieee.org/document/6970844
- **Abstract**: In this paper, we propose superposition coding based on the lattice Gaussian distribution to achieve strong secrecy over the Gaussian broadcast channel with one confidential message, with a constant gap to the secrecy capacity (only for the confidential message). The proposed superposition lattice code consists of a lattice Gaussian code for the Gaussian noise and a wiretap lattice code with strong secrecy. The flatness factor is used to analyze the error probability, information leakage and achievable rates. By removing the secrecy coding, we can modify our scheme to achieve the capacity of the Gaussian broadcast channel with one common and one private message without the secrecy constraint.

## A USRP implementation of wiretap lattice codes

- **Status**: ❌
- **Reason**: wiretap lattice code USRP 구현, 보안 응용·격자부호로 떼어낼 LDPC 기법 없음
- **ID**: ieee:6970845
- **Type**: conference
- **Published**: 2-5 Nov. 2
- **Authors**: Jinlong Lu, J. Harshan, Frédérique Oggier
- **PDF**: https://ieeexplore.ieee.org/document/6970845
- **Abstract**: A wiretap channel models a communication channel between a legitimate sender Alice and a legitimate receiver Bob in the presence of an eavesdropper Eve. Confidentiality between Alice and Bob is obtained using wiretap codes, which exploit the difference between the channels to Bob and to Eve. This paper discusses a first implementation of wiretap lattice codes using USRP (Universal Software Radio Peripheral), which focuses on the channel between Alice and Eve. Benefits of coset encoding for Eve's confusion are observed, using different lattice codes in small dimensions, and varying the position of the eavesdropper.

## Multi-dimensional and non-uniform constellation optimization via the special orthogonal group

- **Status**: ❌
- **Reason**: Rayleigh 페이딩용 다차원/비균일 성상도 회전 최적화, LDPC ECC 기법 없음
- **ID**: ieee:6970838
- **Type**: conference
- **Published**: 2-5 Nov. 2
- **Authors**: David A. Karpuk, Camilla Hollanti
- **PDF**: https://ieeexplore.ieee.org/document/6970838
- **Abstract**: With the goal of optimizing the CM (coded modulation) capacity of a finite constellation over a Rayleigh fading channel, we use one-parameter subgroups of the Lie group of rotation matrices to construct families of rotation matrices which optimize a certain objective function controlling the CM capacity. Our construction does not depend on any assumptions about the constellation or signal-to-noise ratio. We confirm the benefits of our construction for uniform and non-uniform constellations at a large range of SNR values through numerous simulations. We show that in two and four dimensions one can obtain a further potential increase in CM capacity by jointly considering non-uniform and rotated constellations.

## An overview on intercell interference management in mobile cellular networks: From 2G to 5G

- **Status**: ❌
- **Reason**: 셀간간섭(ICI) 관리 서베이, LDPC 무관
- **ID**: ieee:7024797
- **Type**: conference
- **Published**: 19-21 Nov.
- **Authors**: Yiqing Zhou, Ling Liu, Hongyan Du +3
- **PDF**: https://ieeexplore.ieee.org/document/7024797
- **Abstract**: With the unrelenting demand for high bandwidth and high spectrum efficiency, intercell interference (ICI) becomes more and more serious and ICI management plays an increasingly important role in mobile cellular networks. This paper overviews the main ICI management schemes employed in the 2nd generation (2G) to the fourth generation (4G) mobile communication systems, such as the basic frequency reuse-n scheme and power control for 2G and 3G, and enhanced schemes like fractional frequency reuse (FFR), almost blank subframe (ABS) and coordinated multipoint transmission (CoMP) in 4G. These existing ICI management schemes may not be powerful enough for 5G, which is confront with extremely serious ICI given its ultra dense network (UDN) topology. Therefore, promising advanced ICI management schemes are introduced for 5G to manage IC, such as advanced coordinated communication techniques, where coordination is carried out at both the network side and mobile station (MS) side, and advanced air-interface techniques with the potential to mitigate ICI such as orthogonal frequency and code division multiplexing (OFCDM), low-density signature (LDS) spreading and sparse code multiple access (SCMA). Moreover, recent advances in interference alignment (IA) are also discussed.

## 5G: Towards energy-efficient, low-latency and high-reliable communications networks

- **Status**: ❌
- **Reason**: 5G 에너지/지연/신뢰성 서베이, LDPC 신규 기여 없음
- **ID**: ieee:7024793
- **Type**: conference
- **Published**: 19-21 Nov.
- **Authors**: Shunqing Zhang, Xiuqiang Xu, Yiqun Wu +1
- **PDF**: https://ieeexplore.ieee.org/document/7024793
- **Abstract**: In the past few decades, wireless communications have been evolved from GSM system (2G) to LTE-A networks (4G) with the major interest focusing on the throughput related criteria. 5G communication networks, however, extend to a 3-D performance metric cube based on throughput, number of links and delay simultaneously. Moreover, 5G networks confronts a wider range of future applications, including person-to-person, person-to-machine, or even machine-to-machine types. To deal with all the above cases and challenges, we start from the investigation of most popular 5G scenarios and identify the requirements on the energy efficiency, reliability and delay. Detailed technologies are surveyed and discussed thereafter, to achieve critical requirements and facilitate the fundamental tradeoffs among 3-D performance criteria. Through this study, we hope to shed some lights on the novel 5G communication system design, and further pave the way towards energy efficient, low latency and high reliable communication networks.

## A high throughput Gaussian noise generator

- **Status**: ❌
- **Reason**: AWGN 가우시안 노이즈 생성기 FPGA, 디코더가 아닌 시뮬레이션 보조 HW
- **ID**: ieee:7032733
- **Type**: conference
- **Published**: 17-20 Nov.
- **Authors**: Qing Lu, Jianfeng Fan, Chiu-Wing Sham +1
- **PDF**: https://ieeexplore.ieee.org/document/7032733
- **Abstract**: A digital additive white Gaussian noise (AWGN) generator has recently become a public focus with the increasing demand of hardware simulation in researches on communication discipline. Some successful ideas of software, such as the Box-Muller method, are then proposed and implemented into hardware platforms and the architecture design has attracted new studies. Then high-precision small-error Gaussian noise generators appeared in literatures from time to time. Considering that the academic applications prefer higher throughput and the data resolution are always limited by hardware resources, we propose to use a straightforward architecture based on a Gaussian lookup table in these cases. In this paper, such an architecture has been fully investigated and the corresponding FPGA implementation gives out a high throughput of 800 million noise samples per second.

## A Performance Study of the Joint Viterbi Detector Decoder (JVDD) with GDLD and GDPD Codes

- **Status**: ❌
- **Reason**: JVDD 합동 Viterbi 검출/디코딩과 GDLD/GDPD 부호는 비-LDPC 트렐리스 기반으로 바이너리 LDPC BP에 이식할 기법 없음
- **ID**: ieee:7065502
- **Type**: conference
- **Published**: 14-16 Nov.
- **Authors**: Sari Shafidah Bte Shafi'ee, Chan Kheong Sann, Guan Yong Liang
- **PDF**: https://ieeexplore.ieee.org/document/7065502
- **Abstract**: The joint Viterbi detector/decoder (JVDD) is a recently proposed receiver scheme that does both detection and decoding on a single trellis rather than doing detection on a trellis and decoding on factor graph as in the conventional iterative detector today. The JVDD attempts to return minimum metric legal codeword (MMLC) that is the optimum decision over an AWGN/ISI channel. However in so doing, the computational complexity quickly becomes untenable. In order to manage the computational complexity, GDLD and GDPD codes have been proposed that specifically target the complexity issue of the JVDD. In this work we perform a more in-depth study on several of the codes' parameters on both the performance and the complexity of the JVDD.

## LDPC vs turbocodes behavioral analysis in multiuser DS-CDMA systems

- **Status**: ❌
- **Reason**: LDPC vs turbo 단순 BER 비교(DS-CDMA 무선 응용), 떼어낼 신규 디코더·구성·HW 기법 없음
- **ID**: ieee:7010767
- **Type**: conference
- **Published**: 14-15 Nov.
- **Authors**: Ioana M. Marcu, Simona V. Halunga
- **PDF**: https://ieeexplore.ieee.org/document/7010767
- **Abstract**: Coding/decoding techniques have become key elements in communication area because of their crucial importance in recovery of the signals at receivers' end. LDPC codes versus turbocodes have been studied in order to improve bit error rate and to increase the capacity of the systems. The present paper illustrates the behavior of multiuser DS-CDMA system when turbocodes and LDPC are used. In the presence of AWGN and depending on the type of multiuser detector used to recover the signals, the performances of such system can be improved. The multiple users' performances are evaluated in terms of BER vs SNR and the main advantages and disadvantages are outlined in the final chapter.

## Graphical interface for simulation and analysis of LDPC block codes

- **Status**: ❌
- **Reason**: LDPC 시뮬레이션/교육용 GUI 도구. 신규 디코더·구성·HW 기여 없음
- **ID**: ieee:7000430
- **Type**: conference
- **Published**: 12-14 Nov.
- **Authors**: C. Medina, M. Zambrano, E. Iglesias
- **PDF**: https://ieeexplore.ieee.org/document/7000430
- **Abstract**: Low density parity check (LDPC) codes are one of the error-correction codes more versatile, promising and important, and have been adopted in most of the current communication standards. Given the actual and future relevance of these codes, we have developed a graphical interface for simulation and performance analysis considering several factors that affect their encoding and decoding. Thus, this interface could be useful in the design process of these codes, and also as a teaching-learning tool on this topic. In addition to the description of the interface and the analysis of simulations, importance of LDPC codes and graphical interfaces is discussed, the set of parameters and criteria considered in the simulations are described and some improvements to the current interface are suggested.

## Performance Evaluation of Fractional Orbital Angular Momentum (OAM) based LDPC-Coded Free-Space Optical Communications with Atmospheric Turbulence

- **Status**: ❌
- **Reason**: FSO 대기난류 OAM LDPC 코딩이득 분석. 광통신 특이적, 떼어낼 ECC 기법 없음
- **ID**: ieee:8687605
- **Type**: conference
- **Published**: 11-14 Nov.
- **Authors**: Jiaying Zhou, Zhidan Xu, Jian Wang
- **PDF**: https://ieeexplore.ieee.org/document/8687605
- **Abstract**: We simulate and analyze the effects of atmospheric turbulence on fractional orbital angular momentum (OAM) multiplexed free-space optical (FSO) communication system. Assisted by variable low-density parity-check (LDPC) codes, we get a significant coding gain of more than 10 dB compared to an uncoded system.

## Performance Analyses of LDPC-Coded Orbital Angular Momentum (OAM) Optical Communications in a Multi-Bending Ring Fiber

- **Status**: ❌
- **Reason**: OAM 광통신 LDPC 코딩이득 수치분석. 광전파 효과 특이적, 떼어낼 ECC 기법 없음
- **ID**: ieee:8687494
- **Type**: conference
- **Published**: 11-14 Nov.
- **Authors**: Jiaying Zhou, Shuhui Li, Jun Liu +4
- **PDF**: https://ieeexplore.ieee.org/document/8687494
- **Abstract**: We numerically analyze the propagation effects of orbital angular momentum (OAM) multiplexed optical system in a multi-bending fiber. In combination with variable low-density parity-check (LDPC) codes, we get a relatively favorable coding gain of more than 8 dB compared to an uncoded system.

## Multilevel Nonbinary LDPC-Coded Modulation for High-Speed Optical Transmissions

- **Status**: ❌
- **Reason**: 비이진(nonbinary) LDPC coded modulation — 비이진 LDPC는 제외 대상
- **ID**: ieee:8687787
- **Type**: conference
- **Published**: 11-14 Nov.
- **Authors**: Yequn Zhang, Ivan B. Djordjevic
- **PDF**: https://ieeexplore.ieee.org/document/8687787
- **Abstract**: Multilevel nonbinary LDPC-coded modulation has been proposed to reduce decoding complexity while maintaining the large-coding-gain performance desired for high-speed optical transmissions. Simulation results show the proposed scheme outperforms bit-interleaved LDPC-coded modulation by 0.65 dB.

## Coded Modulation for Undersea Optical Fiber Communications

- **Status**: ❌
- **Reason**: 광섬유용 SPC 기반 coded modulation; LDPC 아니고 떼어낼 디코더/구성 기법 없음
- **ID**: ieee:8687689
- **Type**: conference
- **Published**: 11-14 Nov.
- **Authors**: Hussam G. Batshon, Hongbin Zhang
- **PDF**: https://ieeexplore.ieee.org/document/8687689
- **Abstract**: We present an overview of single parity check based bit interleaved coded modulation in fiber optic systems. Coded modulation achieves high SNR sensitivity and large Euclidean distance and enables absolute phase detection without pilot symbols.

## Efficient BER Estimation for Simulation of Coherent Transmission Systems Including Digital Signal Processing and Forward-Error-Correction

- **Status**: ❌
- **Reason**: Importance Sampling 기반 코히런트 전송 BER 추정. FEC 일반 언급, LDPC 디코더 기법 아님
- **ID**: ieee:8687567
- **Type**: conference
- **Published**: 11-14 Nov.
- **Authors**: Hadrien Louchet, André Richter
- **PDF**: https://ieeexplore.ieee.org/document/8687567
- **Abstract**: We show how the Importance Sampling method can be used to accurately estimate the bit-error-rate of coherent transmission systems including digital signal processing and forward-error-correction under non-AWGN channel assumption.

## Dimensioning RS Codes for Mitigation of Phase Noise Induced Cycle Slips in DQPSK Systems

- **Status**: ❌
- **Reason**: RS 부호 dimensioning, 위상잡음 cycle slip 분석; 비-LDPC이고 이식 디코더 기법 없음
- **ID**: ieee:8687897
- **Type**: conference
- **Published**: 11-14 Nov.
- **Authors**: Miu Yoong Leong, Knud J. Larsen, Gunnar Jacobsen +3
- **PDF**: https://ieeexplore.ieee.org/document/8687897
- **Abstract**: We present a semi-analytical method for dimensioning Reed-Solomon codes for coherent DQPSK systems with laser phase noise and cycle slips. We evaluate the accuracy of our method for a 28 Gbaud system using numerical simulations.
