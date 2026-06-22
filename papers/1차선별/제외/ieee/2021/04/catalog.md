# IEEE Xplore — 2021-04


## Analytic Expressions of Decoding Thresholds for LDPC Codes Over BEC

- **Status**: ❌
- **Reason**: BEC/AWGN LDPC 디코딩 임계값 해석적 표현 — 순수 이론 bound/threshold, 디코더·HW·구성으로 안 이어짐
- **ID**: ieee:9292083
- **Type**: journal
- **Published**: April 2021
- **Authors**: Meilin He, Haiquan Wang, Zhirui Hu +1
- **PDF**: https://ieeexplore.ieee.org/document/9292083
- **Abstract**: Analytic expressions of decoding thresholds both for regular and irregular low-density parity-check (LDPC) codes over the binary erasure channel (BEC) are given, and low-complexity methods for determining the thresholds are proposed based on the analytic expressions. Specifically, firstly, a fixed-point equation, which represents a constraint relationship between the threshold and erasure probability of transmitted bits, is established. Secondly, by introducing an auxiliary equation, the threshold can be solved as an analytically function of solutions of a polynomial equation. Moreover, this method is extended to the Additive White Gaussian Noise (AWGN) channel. Numerical results show that, our proposed method is more accurate, and the complexity is much lower than that of conventional density evolution (DE). Moreover, our method does not require to compute the inverse of degree distribution function for irregular LDPC codes.

## An Efficient NB-LDPC Decoder Architecture for Space Telecommand Links

- **Status**: ❌
- **Reason**: NB-LDPC(GF(16)) 디코더 — 비이진 LDPC는 제외 대상
- **ID**: ieee:9241740
- **Type**: journal
- **Published**: April 2021
- **Authors**: Ángel Álvarez, Víctor Fernández, Balázs Matuz
- **PDF**: https://ieeexplore.ieee.org/document/9241740
- **Abstract**: In the framework of error correction in space telecommand (TC) links, the Consultative Committee for Space Data Systems (CCSDS) currently recommends short block-length BCH and binary low-density parity-check (LDPC) codes. Other alternatives have been discarded due to their high decoding complexity, such as non-binary LDPC (NB-LDPC) codes. NB-LDPC codes perform better than their binary counterparts over AWGN and jamming channels, being great candidates for space communications. We show the feasibility of NB-LDPC coding for space TC applications by proposing a highly efficient decoding architecture. The proposed decoder is implemented for a (128,64) NB-LDPC code over GF(16) and the design is particularized for a space-certified Virtex-5QV FPGA. The results prove that NB-LDPC coding is an alternative that outperforms the standardized binary LDPC, with a coding gain of 0.7 dB at a reasonable implementation cost. Given that the maximum rate for TC recommended by the CCSDS is 2 Mbps, the proposed architecture achieves a throughput of 2.03 Mbps using only 9615 LUTs and 5637 FFs (no dedicated memories are used). In addition, this architecture is suitable for any regular (2,4) NB-LDPC (128,64) code over GF(16) independently of the H matrix, allowing flexibility in the choice of the code. This brief places NB-LDPC codes as the excellent candidates for future versions of the telecommand uplink standard.

## An Improved Reliability-Based Decoding Algorithm for NB-LDPC Codes

- **Status**: ❌
- **Reason**: 비이진(NB-LDPC) 신뢰도 기반 디코딩 — 비이진 LDPC는 원칙 제외
- **ID**: ieee:9316234
- **Type**: journal
- **Published**: April 2021
- **Authors**: Suwen Song, Jing Tian, Jun Lin +1
- **PDF**: https://ieeexplore.ieee.org/document/9316234
- **Abstract**: When non-binary low-density parity-check (NB-LDPC) codes with low column weights are adopted, the iterative reliability-based majority-logic decoding (IRB-MLGD) algorithms suffer from severe performance degradation compared to message passing algorithms. In this brief, based on the improved iterative soft reliability-based (IISRB)-MLGD algorithm, we propose a perturbation-injected (P)-IISRB algorithm, where a regular perturbation is introduced to alleviate the periodic point problem that is the main reason for IISRB decoding failure. Compared with the conventional IISRB, the new algorithm significantly improves the decoding performance, lowering the error-floor by at least two orders of magnitude for the example code. Besides, instead of traditionally pre-computing and storing all the q-ary channel reliability measures, a real-time computing method is presented, which reduces the memory cost from O( q) to O( log2q).

## Analysis and Design of Partially Information- and Partially Parity-Coupled Turbo Codes

- **Status**: ❌
- **Reason**: 부분 결합 터보 코드 설계 — LDPC가 아닌 터보 코드, NAND ECC 이식 기법 없음
- **ID**: ieee:9328182
- **Type**: journal
- **Published**: April 2021
- **Authors**: Min Qiu, Xiaowei Wu, Alexandre Graell i Amat +1
- **PDF**: https://ieeexplore.ieee.org/document/9328182
- **Abstract**: In this paper, we study a class of spatially coupled turbo codes, namely partially information- and partially parity-coupled turbo codes. This class of codes enjoy several advantages such as flexible code rate adjustment by varying the coupling ratio and the encoding and decoding architectures of the underlying component codes can remain unchanged. For this work, we first provide the construction methods for partially coupled turbo codes with coupling memory m and study the corresponding graph models. We then derive the density evolution equations for the corresponding ensembles on the binary erasure channel to precisely compute their iterative decoding thresholds. Rate-compatible designs and their decoding thresholds are also provided, where the coupling and puncturing ratios are jointly optimized to achieve the largest decoding threshold for a given target code rate. Our results show that for a wide range of code rates, the proposed codes attain close-to-capacity performance and the decoding performance improves with increasing the coupling memory. In particular, the proposed partially parity-coupled turbo codes have thresholds within 0.0002 of the BEC capacity for rates ranging from 1/3 to 9/10, yielding an attractive way for constructing rate-compatible capacity-approaching channel codes.

## An Improved Expectation Propagation Based Detection Scheme for MIMO Systems

- **Status**: ❌
- **Reason**: MIMO 검출용 Expectation Propagation 개선 — LDPC ECC가 아닌 무선 MIMO 검출, 떼어낼 디코더/HW/코드설계 기법 없음
- **ID**: ieee:9312636
- **Type**: journal
- **Published**: April 2021
- **Authors**: Guoqiang Yao, Hang Chen, Jianhao Hu
- **PDF**: https://ieeexplore.ieee.org/document/9312636
- **Abstract**: Multiple-input Multiple-output (MIMO) technologies play an important role in modern and future wireless communication systems as they can improve the capacity without increasing the bandwidth. MIMO detection is one of the key technologies for MIMO system designs. MIMO detection schemes based on Message Passing (MP) algorithms have attracted extensive attention in recent years. The MIMO detection scheme based on Expectation Propagation (EP), which is also a kind of MP algorithms, has been proved to achieve the Bayes-optimal performance under the conditions of large system limit and compression rate threshold. However, there is improvement space for the detection performance of the EP algorithm when the conditions are not satisfied, which are the common cases in the practical applications. In this paper, when the conditions of the large system limit and compression rate threshold are not satisfied, we analyze the influences of two factors, the initial parameters selection and the moment matching strategy, on the performance of EP based detection scheme. As a result, we propose an improved EP detection scheme based on optimizing the two factors. Simulation results show that the proposed scheme outperforms the original EP detection scheme in different MIMO scenarios.

## Latency and Reliability Trade-Off With Computational Complexity Constraints: OS Decoders and Generalizations

- **Status**: ❌
- **Reason**: URLLC용 OS(order-statistic) 디코더 지연-신뢰도 트레이드오프 모델 — LDPC는 부수 언급, NAND 이식 가능 디코더 기법 아님
- **ID**: ieee:9317807
- **Type**: journal
- **Published**: April 2021
- **Authors**: Hasan Basri Celebi, Antonios Pitarokoilis, Mikael Skoglund
- **PDF**: https://ieeexplore.ieee.org/document/9317807
- **Abstract**: In this article, we study the problem of latency and reliability trade-off in ultra-reliable low-latency communication (URLLC) in the presence of decoding complexity constraints. We consider linear block encoded codewords transmitted over a binary-input AWGN channel and decoded with order-statistic (OS) decoder. We first investigate the performance of OS decoders as a function of decoding complexity and propose an empirical model that accurately quantifies the corresponding trade-off. Next, a consistent way to compute the aggregate latency for complexity constrained receivers is presented, where the latency due to decoding is also included. It is shown that, with strict latency requirements, decoding latency cannot be neglected in complexity constrained receivers. Next, based on the proposed model, several optimization problems, relevant to the design of URLLC systems, are introduced and solved. It is shown that the decoding time has a drastic effect on the design of URLLC systems when constraints on decoding complexity are considered. Finally, it is also illustrated that the proposed model can closely describe the performance versus complexity trade-off for other candidate coding solutions for URLLC such as tail-biting convolutional codes, polar codes, and low-density parity-check codes.

## Maximize Spectrum Efficiency in Underlay Coexistence With Channel Uncertainty

- **Status**: ❌
- **Reason**: 스펙트럼 효율/간섭 제어 chance-constrained 최적화 — LDPC ECC와 무관
- **ID**: ieee:9321155
- **Type**: journal
- **Published**: April 2021
- **Authors**: Shaoran Li, Yan Huang, Chengzhang Li +4
- **PDF**: https://ieeexplore.ieee.org/document/9321155
- **Abstract**: We consider an underlay coexistence scenario where secondary users (SUs) must keep their interference to the primary users (PUs) under control. However, the channel gains from the PUs to the SUs are uncertain due to a lack of cooperation between the PUs and the SUs. Under this circumstance, it is preferable to allow the interference threshold of each PU to be violated occasionally as long as such violation stays below a probability. In this article, we employ Chance-Constrained Programming (CCP) to exploit this idea of occasional interference threshold violation. We assume the uncertain channel gains are only known by their mean and covariance. These quantities are slow-changing and easy to estimate. Our main contribution is to introduce a novel and powerful mathematical tool called Exact Conic Reformulation (ECR), which reformulates the intractable chance constraints into tractable convex constraints. Further, ECR guarantees an equivalent reformulation from linear chance constraints into deterministic conic constraints without the limitations associated with Bernstein Approximation, on which our research community has been fixated on for years. Through extensive simulations, we show that our proposed solution offers a significant improvement over existing approaches in terms of performance and ability to handle channel correlations (where Bernstein Approximation is no longer applicable).

## Adaptive Path Interpolation Method for Sparse Systems: Application to a Censored Block Model

- **Status**: ❌
- **Reason**: Bayesian inference 상호정보 계산용 adaptive path interpolation 순수 이론 — 디코더/HW/구성으로 안 이어짐
- **ID**: ieee:9328315
- **Type**: journal
- **Published**: April 2021
- **Authors**: Jean Barbier, Chun Lam Chan, Nicolas Macris
- **PDF**: https://ieeexplore.ieee.org/document/9328315
- **Abstract**: Recently, a new adaptive path interpolation method has been developed as a simple and versatile scheme to calculate exactly the asymptotic mutual information of Bayesian inference problems defined on dense factor graphs. These include random linear and generalized estimation, sparse superposition codes, and low-rank matrix / tensor estimation. For all these systems, the adaptive interpolation method directly proves that the replica-symmetric prediction is exact, in a simple and unified manner. When the underlying factor graph of the inference problem is sparse the replica prediction is considerably more complicated, and rigorous results are often lacking or obtained by rather complicated methods. In this work we show how to extend the adaptive path interpolation method to sparse systems. We concentrate on a censored block model, where hidden variables are measured through a binary erasure channel, for which we fully prove the replica prediction.

## Is Multichannel Access Useful for Timely Information Update?

- **Status**: ❌
- **Reason**: 다채널 접속 AoI 정보 신선도 분석 — LDPC/ECC 무관
- **ID**: ieee:9296962
- **Type**: journal
- **Published**: April 2021
- **Authors**: Jiaxin Liang, Haoyuan Pan, Soung Chang Liew
- **PDF**: https://ieeexplore.ieee.org/document/9296962
- **Abstract**: This letter investigates information freshness of multichannel access in information update systems. Age of information (AoI) is a performance metric that characterizes information freshness. When multiple devices share the same wireless channel to send updates to a common receiver, an interesting question is whether dividing the whole channel into several subchannels will lead to better AoI performance. Given the same frequency band, dividing it into different numbers of subchannels leads to different transmission times and packet error rates (PER), thus affecting information freshness. We focus on a multichannel system where devices take turns to transmit with a cyclic schedule repeated over time. We derive the average AoI by estimating the PERs of short packets. We further examine bounded AoI, for which the instantaneous AoI is required to be below a threshold a large percentage of the time. Our results indicate that multichannel access can provide low average AoI and uniform bounded AoI simultaneously across different received powers.

## Chaos-Based Space-Time Trellis Codes With Deep Learning Decoding

- **Status**: ❌
- **Reason**: 혼돈 기반 space-time trellis code + 신경망 디코딩 — LDPC ECC 아님, 떼어낼 LDPC 기법 없음
- **ID**: ieee:9261618
- **Type**: journal
- **Published**: April 2021
- **Authors**: Carlos E. C. Souza, Rafael Campello, Cecilio Pimentel +1
- **PDF**: https://ieeexplore.ieee.org/document/9261618
- **Abstract**: In this brief we propose a space-time trellis code scheme based on three-dimensional chaotic attractors. The chaotic trajectories are represented by the symbolic dynamics generated by a labeled Poincaré section and are transmitted by multiple antennas, defining a chaos-based space-time trellis code (CB-STTC). This code is defined by a finite state encoder that maps information sequences to restricted sequences satisfying the dynamics of the attactor. We also propose a neural network architecture capable of learning how to decode the CB-STTC. Finally, the frame error rate of the proposed CB-STTC is analyzed with maximum likelihood and neural network decoding.

## Millimeter-Wave Wireless Communications for Home Network in Fiber-to-the-Room Scenario

- **Status**: ❌
- **Reason**: FTTR+mmWave 홈네트워크 아키텍처 — LDPC/ECC 무관
- **ID**: ieee:11285359
- **Type**: journal
- **Published**: April 2021
- **Authors**: Chao He, Zhixiong Ren, Xiang Wang +8
- **PDF**: https://ieeexplore.ieee.org/document/11285359
- **Abstract**: Millimeter-wave (mmWave) technology has been well studied for both outdoor long-distance transmission and indoor short-range communication. In the recently emerging fiber-to-the-room (FTTR) architecture in the home network of the fifth generation fixed networks (F5G), mmWave technology can be cascaded well to a new optical network terminal in the room to enable extremely high data rate communication (i.e., > 10 Gb/s). In the FTTR+mmWave scenario, the rapid degradation of the mmWave signal in long-distance transmission and the significant loss against wall penetration are no longer the bottlenecks for real application. Moreover, the surrounding walls of every room provide excellent isolation to avoid interference and guarantee security. This paper provides insights and analysis for the new FTTR+mmWave architecture to improve the customer experience in future broadband services such as immersive audiovisual videos.

## Implementation of Error Correction Techniques in Memory Applications

- **Status**: ❌
- **Reason**: Hamming/SEC-DED-DAEC 블록부호 메모리 ECC, LDPC 아님
- **ID**: ieee:9418432
- **Type**: conference
- **Published**: 8-10 April
- **Authors**: Nandivada Sridevi, K. Jamal, Kiran Mannem
- **PDF**: https://ieeexplore.ieee.org/document/9418432
- **Abstract**: As the technology scales down, various soft errors in SRAM memories occurs due to which the single cell and multiple cell upsets are formed. Error correction codes such as the first technique (7,4) hamming code, where 7 denotes total code word, four refers to data bits and 3 parity bits were implemented and verified its encoding and decoding process. But it is only useful for single bit error detection and also correction, which has been the main drawback of this hamming code. So, the second technique implemented was the extended hamming code (8,4) or SEC-DED code ("Single Error Correction-Double Error Detection"). This code has an extra bit and used for correction of single error and also detection of double error. But correction of double error doesn’t happen in SEC-DED code. So, the extension of (8,4) SEC-DED code was (14,8) SEC-DED-DAEC ("Single Error Correction-Double Error Detection-Double Adjacent Error Correction") code where 14 denotes total code word, 8 data bits, six parity bits which can be used for correction of single error, detection of double error and also correction of double adjacent error was proposed in this work. These techniques related Encoding and Decoding processes were studied and all the simulation results were verified and implemented by using Verilog Coding in Xilinx ISE 14.7 tool. This proposed SEC-DED-DAEC method was also implemented in memory application and its output is verified. The double error detection was adjacently corrected by using this method and the complexity was decreased. The advantage of the proposed technique is it has the ability to detect and correct errors adjacently up to 2 bits.

## A New Transmission Scheme for Additional Bits with Rotated LDPC Coded Signals

- **Status**: ❌
- **Reason**: LDPC 코드 신호에 추가비트 전송 — 변조/전송 기법, LDPC는 베이스라인, 디코더/구성 기여 없음
- **ID**: ieee:9417597
- **Type**: conference
- **Published**: 29 March-1
- **Authors**: Jiachen Sun, Hao Liu, Xiao Ma
- **PDF**: https://ieeexplore.ieee.org/document/9417597
- **Abstract**: In this work, a new coding scheme is proposed for transmitting additional bits along with low-density parity-check (LDPC) coded data at no expense of bandwidth or transmission power. At the transmitter, the LDPC coded bits are first flipped in a random-like way specified by the additional bits and then mapped into a sequence of two-dimensional signals. The modulated sequence is then partitioned into several groups, each of which is rotated by an angle that is also specified by the additional bits, resulting in a sequence of transmitted signals. At the receiver, the additional bits are detected by a serial list decoding algorithm with an early stopping criterion. Then, by removing the effect of the additional bits, the LDPC coded data can be decoded as usual. Simulation results show that, for a rate-1/2 LDPC code of length 8064, up to twenty-four additional bits can be reliably transmitted along with LDPC coded QPSK signaling.

## Age and Energy Tradeoff for Short Packet Based Two-Hop Decode-and-Forward Relaying Networks

- **Status**: ❌
- **Reason**: AoI-에너지 트레이드오프 릴레이 네트워크 — LDPC ECC 기법 없음
- **ID**: ieee:9417497
- **Type**: conference
- **Published**: 29 March-1
- **Authors**: Mangang Xie, Jie Gong, Xiao Ma
- **PDF**: https://ieeexplore.ieee.org/document/9417497
- **Abstract**: Real-time and energy-efficient transmissions are two critical demands for status update systems, however it is difficult to meet these requirements simultaneously. This paper focuses on the tradeoff between the average age of information (AoI) and the average energy cost (EC) for two-hop decode-and-forward (DF) relaying networks with short packet transmissions. Both the partial relay selection (PRS) and max-min relay selection (MMRS) schemes are considered. The expressions for the average AoI and the average EC of two-hop relaying networks are derived, and the age-energy tradeoff is also achieved by minimizing the weighted sum of them. Numerical simulations show that both PRS and MMRS schemes have their own advantages to minimize the age and energy cost under different channel conditions, where MMRS is a fairness scheme that takes the channel conditions of two hops into account. In addition, an optimal packet length can always be found to tradeoff the average AoI and average EC in two-hop relaying networks.

## Optimized Asymmetric Feedback Detection for Rate-adaptive HARQ with Unreliable Feedback

- **Status**: ❌
- **Reason**: 비대칭 피드백 검출 IR-HARQ — MDP 기반 통신 응용, LDPC ECC 기법 없음
- **ID**: ieee:9417573
- **Type**: conference
- **Published**: 29 March-1
- **Authors**: Weihang Ding, Mohammad Shikh-Bahaei
- **PDF**: https://ieeexplore.ieee.org/document/9417573
- **Abstract**: This work considers downlink incremental redundancy Hybrid Automatic Repeat Request (IR-HARQ) over unreliable feedback channels. Since the impact of positive feedback (i.e., ACK) error is smaller than that of negative feedback (i.e., NACK) error, an asymmetric feedback detection scheme is proposed to protect NACK and further reduce the outage probability. We formulate the HARQ process as a Markov Decision Process (MDP) model to adapt to the transmission rate of each transmission attempt without enriched feedback and additional feedback cost. We aim to optimize the performance of HARQ process under certain outage probability requirements by finding optimal asymmetric detection thresholds. Numerical results obtained on the downlink Rayleigh fading channel and 5G new radio (NR) PUCCH feedback channel show that by applying asymmetric feedback detection and adaptive rate allocation, higher throughput can be achieved under outage probability limitations.

## An IR-HARQ scheme for covert communications

- **Status**: ❌
- **Reason**: covert 통신용 IR-HARQ — 응용 특이적, 떼어낼 LDPC ECC 기법 없음
- **ID**: ieee:9417551
- **Type**: conference
- **Published**: 29 March-1
- **Authors**: Meritxell Lamarca
- **PDF**: https://ieeexplore.ieee.org/document/9417551
- **Abstract**: This paper explores the advantages of incremental redundancy hybrid-ARQ schemes for covert communications in which a feedback channel is available. The use of efficient incremental redundancy with sub-codewords of different sizes provides significant gains in terms of covertness while preserving the error rate performance. The convexity of covertness metrics is exploited to design the size and degree profile of each block when a concatenated code based on MDNL codes is employed in the binary symmetric channel.

## On Opportunistic Selection of Common Randomness and LLR generation for Algebraic Group Secret-Key Generation

- **Status**: ❌
- **Reason**: 물리계층 그룹 비밀키 생성용 LLR/reconciliation, LDPC은 부수, 보안 응용 특이적, 떼어낼 ECC 기법 없음
- **ID**: ieee:9448927
- **Type**: conference
- **Published**: 25-28 Apri
- **Authors**: Rohit Joshi, J. Harshan
- **PDF**: https://ieeexplore.ieee.org/document/9448927
- **Abstract**: It is well known that physical-layer key generation methods enable wireless devices to harvest symmetric keys by accessing the randomness offered by the wireless channels. Although two-user key generation is well understood, group secret-key (GSK) generation, wherein more than two nodes in a network generate secret-keys, still poses open problems. Recently, Manish Rao et al., have proposed the Algebraic Symmetrically Quantized GSK (A-SQGSK) protocol for a network of three nodes wherein the nodes share quantized versions of the channel realizations over algebraic rings, and then harvest a GSK. Although A-SQGSK protocol guarantees confidentiality of common randomness to an eavesdropper, we observe that the key-rate of the protocol is poor since only one channel in the network is used to harvest GSK. Identifying this limitation, in this paper, we propose an opportunistic selection method wherein more than one wireless channel is used to harvest GSKs without compromising the confidentiality feature, thereby resulting in remarkable improvements in the key-rate. Furthermore, we also propose a log-likelihood ratio (LLR) generation method for the common randomness observed at various nodes, so that the soft-values are applied to execute LDPC codes based reconciliation to reduce the bit mismatches among the nodes.

## Joint uplink PD-NOMA and SCMA for future multiple access systems

- **Status**: ❌
- **Reason**: PD-NOMA+SCMA 다중접속, EXIT chart 기반 코드율 최적화만, LDPC 디코더/구성 새 기법 없음
- **ID**: ieee:9449037
- **Type**: conference
- **Published**: 25-28 Apri
- **Authors**: Xiaotian Fu, Mylene Pischella, Didier Le Ruyet
- **PDF**: https://ieeexplore.ieee.org/document/9449037
- **Abstract**: In this paper, we propose an uplink system which combines power-domain non-orthogonal multiple access (PD-NOMA) and sparse code multiple access (SCMA) together, in order to enable massive user connectivity. The receiver adopts successive interference cancellation (SIC) and iterative SCMA detection algorithm for decoding the superimposed signals. An optimization method of the code rate for the error-correcting channel codes is proposed by analyzing the extrinsic information transfer (EXIT) charts, so as to reach a trade-off between system convergence behavior and spectral efficiency. To evaluate the performance, a conventional SCMA system is used as comparison baseline. Numerical results show that the proposed system along with the optimization method achieves good bit error rate (BER) performance and significantly improves the spectral efficiency.

## Reliability Based Candidate Selection of List Decoding for Polar Code

- **Status**: ❌
- **Reason**: Polar code SCL 디코딩 후보 선택 기법, LDPC 아니고 NAND 이식성 낮음
- **ID**: ieee:9448742
- **Type**: conference
- **Published**: 25-28 Apri
- **Authors**: Daeson Kim, Sehyoung Kim, Inhyoung Kim +1
- **PDF**: https://ieeexplore.ieee.org/document/9448742
- **Abstract**: Polar code is adapted as the channel coding scheme for control channel in 5G NR. The basic algorithm of polar code is the successive cancelation (SC) decoding but its performance is not good enough and decoding latency is relatively high. So the simplified successive cancelation list(SSCL) decoding is generally used. When the SSCL is operated, path metric calculator generates children candidates and the number of children candidates influenced on the H/W complexity. The reliability of children candidates is affected by that of their parent candidates. The number of children candidates is adaptively selected according to the reliability of their parent candidate and the total number of children candidates could be reduced. Our proposed algorithm reduces H/W complexity of polar decoder while preserving decoding performance.

## LDPC-Coded Spectrally Efficient FDM System with Iterative Decoder

- **Status**: ❌
- **Reason**: SEFDM ICI 제거에 LDPC 적용, LDPC는 표준 베이스라인 — 떼어낼 새 ECC 기법 없음
- **ID**: ieee:9449195
- **Type**: conference
- **Published**: 23-26 Apri
- **Authors**: Mengqi Guo, Liang Quan
- **PDF**: https://ieeexplore.ieee.org/document/9449195
- **Abstract**: In this paper, low-density parity-check (LDPC) codes are applied in spectrally efficient frequency-division multiplexing (SEFDM) with iterative decoder to eliminate the influence from inter-carrier interference (ICI). SEFDM has higher spectral efficiency than orthogonal frequency-division multiplexing (OFDM) by compressing the subcarrier spacing. This self-induced ICI is eliminated by LDPC codes and iterative decoder. The SEFDM scheme analyzed in this paper is not limited by subcarrier number and modulation order because the ICI cancellation scheme has relatively low computational complexity. With LDPC codes, the iterative-SEFDM scheme supports QPSK, 16QAM, 64QAM and 256QAM modulation formats. To the best of our knowledge, the SEFDM scheme with high-order 256QAM modulation is first demonstrated. With bandwidth compression and effective ICI cancellation, LDPC-coded iterative-SEFDM can achieve better bit error rate performance than its counterpart LDPC-coded OFDM at the same spectral efficiency.

## On error correction performance of LDPC and Polar codes for the 5G Machine Type Communications

- **Status**: ❌
- **Reason**: 5G MTC LDPC vs Polar 성능 비교만 — 이식 가능한 새 기법 없음
- **ID**: ieee:9422665
- **Type**: conference
- **Published**: 21-24 Apri
- **Authors**: Salima Belhadj, Moulay Lakhdar Abdelmounaim
- **PDF**: https://ieeexplore.ieee.org/document/9422665
- **Abstract**: Channel coding for the 5th generation (5G) wireless communication system has to fulfill diverse requirements arising from new machine type communication (MTC) services. The 5G-MTC applications can be classified into two categories: Ultra-Reliable Low-Latency Communications (URLLC) and massive Machine-Type Communication (mMTC). Polar code and Low-Density Parity Check (LDPC) code are among the most advanced channel coding techniques known today that have the potential to be used in the 5G. The main objective of this paper is to evaluate the error correction performance of Polar and LDPC coding schemes in the case when short to medium information block lengths are transmitted, as it is often in mMTC and URLLC scenarios. These codes are evaluated in terms of both Block Error Rate (BLER) and Bit Error Rate (BER). Simulation results show that Polar codes exhibit a much better error correction capability compared to the LDPC codes for short block lengths, while they have a comparable performance at medium block length.

## A Construction Method of Doped Low-Density Parity-Check Codes Based on Quadratic Residue Codes

- **Status**: ❌
- **Reason**: LDPC를 QR code로 doping하는 코드구성 — trapping set 이용하나 비-LDPC(QR) 결합 부호로, 바이너리 LDPC 자체 디코더/구성 신규 기여라 보기 약함
- **ID**: ieee:9434940
- **Type**: conference
- **Published**: 14-16 Apri
- **Authors**: Yong Li, Xiang Huang, Chuan Zhou +2
- **PDF**: https://ieeexplore.ieee.org/document/9434940
- **Abstract**: In this paper, we propose an approach to constructing a class of doped low-density parity-check (LDPC) codes, by utilizing some coded bits of an LDPC code as the information bits of a quadratic residues (QR) code and then integrating the corresponding two Tanner graphs as a whole. Herein, the trapping set information of the LDPC code is used for selecting the information bits of the QR code. Simulation results show that the proposed doped LDPC codes achieve more than 1.4 dB and 1.0 dB gains with slight rate losses, respectively, at a frame error rate of 10−5, when compared to two regular LDPC codes.

## Power Allocation of Two-User Downlink Channel Decoding

- **Status**: ❌
- **Reason**: NOMA 하향링크 전력할당+SIC 디코딩, LDPC는 베이스라인일 뿐 떼어낼 LDPC ECC 기법 없음 — 무선 응용 특이적
- **ID**: ieee:9434941
- **Type**: conference
- **Published**: 14-16 Apri
- **Authors**: Pingping Chen, Cong Wang, Yi Fang +1
- **PDF**: https://ieeexplore.ieee.org/document/9434941
- **Abstract**: This paper investigates an efficient power allocation for channel decoding algorithms in two-user downlink non-orthogonal multiple access (NOMA). We consider three successive interference cancellation (SIC) algorithms with low-density parity-check (LDPC) codes, i.e., the SIC treats interference as noise (N-SIC) algorithm, the SIC treats modulation of interference signal as auxiliary information (J-SIC), and the SIC exchanges the external decoding information of the signals for two users (E-SIC). To improve the decoding accuracy, we propose power allocation algorithms for SIC decoding based on fairness index and outage probability respectively. The rate-fairness of users is also optimized. Simulation results show that the iterative E-SIC can achieve a significant performance gain over N-SIC and J-SIC, and this gain is much smaller when the power allocation (PA) is used in the three SIC decodings. Moreover, we analyze performance bound of Polyanskiy-Poor-Verdu (PPV) finite-length for the SIC decodings. It provides a theoretical analysis for the optimization of frame error rate (FER) by power allocation.

## An Improved Successive Cancellation List Flip Decoder for Polar Codes Based on Key Sets

- **Status**: ❌
- **Reason**: 폴라부호 SCL-Flip 디코더. 비-LDPC, 폴라 전용 key set 기법으로 LDPC BP 이식성 없음
- **ID**: ieee:9434898
- **Type**: conference
- **Published**: 14-16 Apri
- **Authors**: Jingyun Bao, Shunjie Lin, Xingcheng Liu
- **PDF**: https://ieeexplore.ieee.org/document/9434898
- **Abstract**: Existing studies have documented that flipping operation can improve the performance of polar codes based on CRC-aided successive cancellation list (CA-SCL) decoding algorithm. However, the introduction of the flips greatly increases the complexity and delay of the decoder as well. In this paper, we analyzed the error distribution in the CA-SCL decoding and proposed a new efficient flipping set, key set, to reduce the complexity of the SCL-Flip decoding by narrowing down the size of the flipping set applicable. Different from the critical set which focuses on rate-1 nodes only, the key set can be constructed dynamically based on the results of the original CA-SCL decoding. In addition, we proposed an order-1 SCL-Flip decoder based on the key set to reduce the decoding complexity. Simulation results showed that the key set has a high accuracy of locating the first error and our proposed algorithm has almost no performance degradation compared with the existing SCL-Flip algorithms while the average complexity is reduced significantly.

## Optimization of Irregular NB QC-LDPC Block Codes over Small Alphabets

- **Status**: ❌
- **Reason**: 비이진(NB) QC-LDPC 최적화 — 비이진 LDPC는 기준상 즉시 제외
- **ID**: ieee:9457656
- **Type**: conference
- **Published**: 11-15 Apri
- **Authors**: Irina E. Bocharova, Boris D. Kudryashov, Evgenii P. Ovsyannikov +2
- **PDF**: https://ieeexplore.ieee.org/document/9457656
- **Abstract**: We propose a novel approach for optimization of nonbinary (NB) quasi-cyclic (QC)-LDPC codes. In this approach, the base parity-check matrices are constructed by the simulated annealing method, and then labeled while maximizing the so-called generalized girth of the NB LDPC code Tanner graph. Random coding bounds on the ML decoding error probability for ensembles of "almost regular" NB LDPC codes of finite lengths over extensions of the binary Galois field are derived. These bounds are based on the average bit weight spectra for the ensembles of NB LDPC codes. The observed FER performance of the sum-product BP decoding of "almost regular" NB QC-LDPC block codes is presented and compared to the finite-length random coding bounds, as well as to the performance of the optimized binary QC-LDPC block code in the 5G standard. In the waterfall region, the gap between the finite-length bounds on the error probability of the ML decoding and the simulation performance of the BP decoding is about 0.1 – 0.2 dB.

## Linear programming decoder for hypergraph product quantum codes

- **Status**: ❌
- **Reason**: 양자 CSS/하이퍼그래프곱 부호 LP 디코더 — 양자 전용, soundness 등 양자 특화 개념 의존
- **ID**: ieee:9457611
- **Type**: conference
- **Published**: 11-15 Apri
- **Authors**: Omar Fawzi, Lucien Grouès, Anthony Leverrier
- **PDF**: https://ieeexplore.ieee.org/document/9457611
- **Abstract**: We introduce a decoder for quantum CSS codes that is based on linear programming. Our definition is a priori slightly different from the one proposed by Li and Vontobel as we have a syndrome oriented approach instead of an error oriented one, but we show that the success condition is equivalent. Although we prove that this decoder fails for quantum codes that do not have good soundness property (i.e., having large errors with syndrome of small weight) such as the toric code, we obtain good results from simulations. We run our decoder for hypergraph products of two random LDPC codes, showing that it performs better than belief propagation, even combined with the small-set-flip decoder that can provably correct a constant fraction of random errors.

## Using List Decoding to Improve the Finite-Length Performance of Sparse Regression Codes

- **Status**: ❌
- **Reason**: Sparse regression(SPARC) + AMP 리스트 디코딩 — 비-LDPC, AMP 기법 LDPC BP에 직접 이식성 없음
- **ID**: ieee:9457621
- **Type**: conference
- **Published**: 11-15 Apri
- **Authors**: Haiwen Cao, Pascal O. Vontobel
- **PDF**: https://ieeexplore.ieee.org/document/9457621
- **Abstract**: We consider sparse superposition codes (SPARCs) over complex AWGN channels. Such codes can be efficiently decoded by an approximate message passing (AMP) decoder, whose performance can be predicted via so-called state evolution in the large-system limit. In this paper, we mainly focus on how to use concatenation of SPARCs and cyclic redundancy check (CRC) codes on the encoding side and use list decoding on the decoding side to improve the finite-length performance of the AMP decoder for SPARCs over complex AWGN channels. Simulation results show that such a concatenated coding scheme works much better than SPARCs with the original AMP decoder and results in a steep waterfall-like behavior in the bit-error rate performance curves.

## Correcting Erasures with Topological Subsystem Color Codes

- **Status**: ❌
- **Reason**: 양자 토폴로지 색부호의 erasure 디코딩 — 양자 전용 개념 의존, 고전 바이너리 LDPC 이식 기법 없음
- **ID**: ieee:9457583
- **Type**: conference
- **Published**: 11-15 Apri
- **Authors**: Hiteshvi Manish Solanki, Pradeep Kiran Sarvepalli
- **PDF**: https://ieeexplore.ieee.org/document/9457583
- **Abstract**: Qubit loss is one of the forms of noise encountered in some quantum technologies. Such noise is modeled using the quantum erasure channel. Unlike the depolarizing noise, it is much more tractable, yet the performance of many quantum codes over the erasure channel has not been studied as extensively. In this paper, we study the performance of topological subsystem color codes (TSCCs) over the quantum erasure channel. It is the first such study of TSCCs over the erasure channel. We propose multiple decoding algorithms for TSCC and obtain the highest threshold of about 9.7% for the subsystem color code derived from the square octagon lattice.

## On Lifted Multiplicity Codes

- **Status**: ❌
- **Reason**: Lifted RS/multiplicity 부호의 rate·distance bound — 비-LDPC, 순수 이론, 떼어낼 LDPC 기법 없음
- **ID**: ieee:9457625
- **Type**: conference
- **Published**: 11-15 Apri
- **Authors**: Lukas Holzbaur, Rina Polyanskaya, Nikita Polyanskii +2
- **PDF**: https://ieeexplore.ieee.org/document/9457625
- **Abstract**: Lifted Reed-Solomon codes and multiplicity codes are two classes of evaluation codes that allow for the design of high-rate codes that can recover every codeword or information symbol from many disjoint sets. Recently, the underlying approaches have been combined to construct lifted bi-variate multiplicity codes, that can further improve on the rate. We continue the study of these codes by providing lower bounds on the rate and distance for lifted multiplicity codes obtained from polynomials in an arbitrary number of variables. Specifically, we investigate a subcode of a lifted multiplicity code formed by the linear span of m-variate monomials whose restriction to an arbitrary line in Fqm is equivalent to a low-degree uni-variate polynomial. We find the tight asymptotic behavior of the fraction of such monomials when the number of variables m is fixed and the alphabet size q=2ℓ is large. For some parameter regimes, lifted multiplicity codes are then shown to have a better tradeoff between redundancy and the number of disjoint recovering sets for every codeword or information symbol than previously known constructions.

## Universal interactive Gaussian quantization with side information

- **Status**: ❌
- **Reason**: Polar lattice 기반 가우시안 양자화(side info) — 소스 코딩/양자화, 채널 ECC 아님
- **ID**: ieee:9457662
- **Type**: conference
- **Published**: 11-15 Apri
- **Authors**: Shubham K Jha, Himanshu Tyagi
- **PDF**: https://ieeexplore.ieee.org/document/9457662
- **Abstract**: We consider universal quantization with side information for Gaussian observations, where the side information is a noisy version of the sender’s observation with an unknown noise variance. We propose a universally rate optimal and practical quantization scheme for all values of unknown noise variance. Our scheme is interactive, uses Polar lattices from prior work, and proceeds by checking in each round if a reliable estimate has been formed. In particular, our scheme is based on a structural decomposition of the underlying auxiliaries so that even when recovery fails in a round, the parties agree on a common "reference point" that is closer than the previous one.
