# IEEE Xplore — 2023-11


## Joint Design of Source-Channel Codes With Linear Source Encoding Complexity and Good Channel Thresholds Based on Double-Protograph LDPC Codes

- **Status**: ❌
- **Reason**: JSCC(소스-채널 결합) DP-LDPC, LDPC가 베이스라인이고 떼어낼 NAND ECC 기법 없음 - 제외 원칙
- **ID**: ieee:10266358
- **Type**: journal
- **Published**: Nov. 2023
- **Authors**: Jia Zhan, Francis C. M. Lau
- **PDF**: https://ieeexplore.ieee.org/document/10266358
- **Abstract**: We propose the use of a lower or upper triangular sub-base matrix to replace the identity matrix in the source-check-channel-variable linking protomatrix of a double-protograph low-density parity-check joint-source-channel code (DP-LDPC JSCC). The elements along the diagonal of the proposed lower or upper triangular sub-base matrix are assigned as “1” and the other non-zero elements can take any non-negative integral values. Compared with the traditional DP-LDPC JSCC designs, the new designs show a theoretical channel threshold improvement of up to 0.41 dB and a simulated source symbol error rate improvement of up to 0.5 dB at an error rate of 10−6.

## Joint Estimation and Compensation of CFO, IQ Imbalance and Channel Parameters for Zero Padded OTSM Systems

- **Status**: ❌
- **Reason**: OTSM CFO/IQ imbalance 추정·보상; LDPC는 부수 언급, 떼어낼 기법 없음
- **ID**: ieee:10188911
- **Type**: journal
- **Published**: Nov. 2023
- **Authors**: Sapta Girish Neelam, P. R. Sahu
- **PDF**: https://ieeexplore.ieee.org/document/10188911
- **Abstract**: The Orthogonal Time Sequency Multiplexing (OTSM) waveform demonstrates superior performance compared to the Orthogonal Frequency Division Multiplexing (OFDM) waveform under linear time-varying (LTV) channels and multiple Doppler conditions. However, the direct conversion OTSM transceiver system is constrained by hardware impairments like carrier frequency offset (CFO) and IQ imbalance. In this Letter, we address these impairments by estimating and compensating for them using a dual pilot approach in the delay-time domain. Channel estimation is done at discrete pilot locations using two different methods. In high-mobility scenarios, the system employing phase compensation at periodic intervals exhibits better performance than the direct channel estimation method, which incorporates CFO into the channel. We evaluate the mean square error of the estimated LTV channel, which decreases with higher pilot power and reduced CFO. The performance analysis covers both uncoded and low-density parity-check (LDPC) coded systems.

## FASURA: A Scheme for Quasi-Static Fading Unsourced Random Access Channels

- **Status**: ❌
- **Reason**: unsourced random access 코딩(pilot+polar code+SIC); LDPC 아니며 떼어낼 ECC 기법 없음
- **ID**: ieee:10185658
- **Type**: journal
- **Published**: Nov. 2023
- **Authors**: Michail Gkagkos, Krishna R. Narayanan, Jean-Francois Chamberland +1
- **PDF**: https://ieeexplore.ieee.org/document/10185658
- **Abstract**: Unsourced random access emerged as a novel wireless paradigm enabling massive device connectivity on the uplink. We consider quasi-static Rayleigh fading wherein the access point has multiple receive antennas and every mobile device a single transmit antenna. The objective is to construct a coding scheme that minimizes the energy-per-bit subject to a maximum probability of error given a fixed message length and a prescribed number of channel uses. Every message is partitioned into two parts: the first determines pilot values and spreading sequences; the remaining bits are encoded using a polar code. The transmitted signal contains two distinct sections. The first features pilots and the second is composed of spread modulated symbols. The receiver has three modules: an energy detector, tasked with recovering the set of active pilot sequences; a bank of Minimum Mean Square Error (MMSE) estimators acting on measurements at the receiver; and a polar list-decoder, which seeks to retrieve the coded information bits. A successive cancellation step is applied to subtract recovered codewords, before the residual signal is fed back to the decoder. Empirical evidence suggests that an appropriate combination of these ideas can outperform state-of-the-art coding techniques when the number of active users exceeds one hundred.

## Statistical Tools and Methodologies for Ultrareliable Low-Latency Communication—A Tutorial

- **Status**: ❌
- **Reason**: URLLC 통계 도구 튜토리얼, LDPC 언급 없고 디코더/HW/코드설계 이식 기법 없음
- **ID**: ieee:10323296
- **Type**: journal
- **Published**: Nov. 2023
- **Authors**: Onel L. A. López, Nurul H. Mahmood, Mohammad Shehab +4
- **PDF**: https://ieeexplore.ieee.org/document/10323296
- **Abstract**: Ultrareliable low-latency communication (URLLC) constitutes a key service class of the fifth generation (5G) and beyond cellular networks. Notably, designing and supporting URLLC pose a herculean task due to the fundamental need to identify and accurately characterize the underlying statistical models in which the system operates, e.g., interference statistics, channel conditions, and the behavior of protocols. In general, multilayer end-to-end approaches considering all the potential delay and error sources and proper statistical tools and methodologies are inevitably required for providing strong reliability and latency guarantees. This article contributes to the body of knowledge in the latter aspect by providing a tutorial on several statistical tools and methodologies that are useful for designing and analyzing URLLC systems. Specifically, we overview the frameworks related to the following: 1) reliability theory; 2) short packet communications; 3) inequalities, distribution bounds, and tail approximations; 4) rare-events simulation; 5) queuing theory and information freshness; and 6) large-scale tools, such as stochastic geometry, clustering, compressed sensing, and mean-field (MF) games. Moreover, we often refer to prominent data-driven algorithms within the scope of the discussed tools/methodologies. Throughout this article, we briefly review the state-of-the-art works using the addressed tools and methodologies, and their link to URLLC systems. Moreover, we discuss novel application examples focused on physical and medium access control layers. Finally, key research challenges and directions are highlighted to elucidate how URLLC analysis/design research may evolve in the coming years.

## RIS-Aided Multiuser MIMO-OFDM With Linear Precoding and Iterative Detection: Analysis and Optimization

- **Status**: ❌
- **Reason**: RIS-aided MIMO-OFDM precoding/passive beamforming 최적화; LDPC ECC 기법 없음, 무선 응용 특이적
- **ID**: ieee:10068417
- **Type**: journal
- **Published**: Nov. 2023
- **Authors**: Mingyang Yue, Lei Liu, Xiaojun Yuan
- **PDF**: https://ieeexplore.ieee.org/document/10068417
- **Abstract**: In this paper, we consider a reconfigurable intelligent surface (RIS) aided uplink multiuser multi-input multi-output (MIMO) orthogonal frequency division multiplexing (OFDM) system, where the receiver is assumed to conduct low-complexity iterative detection. We aim to minimize the total transmit power by jointly designing the precoder of the transmitter and the passive beamforming of the RIS. This problem can be tackled from the perspective of information theory. But this information-theoretic approach may involve prohibitively high complexity since the number of rate constraints that specify the capacity region of the uplink multiuser channel is exponential in the number of users. To avoid this difficulty, we formulate the design problem of the iterative receiver under the constraints of a maximal iteration number and target bit error rates of users. To tackle this challenging problem, we propose a groupwise successive interference cancellation (SIC) optimization approach, where the signals of users are decoded and canceled in a group-by-group manner. We present a heuristic user grouping strategy, and resort to the alternating optimization technique to iteratively solve the precoding and passive beamforming sub-problems. Specifically, for the precoding sub-problem, we employ fractional programming to convert it to a convex problem; for the passive beamforming sub-problem, we adopt successive convex approximation to deal with the unit-modulus constraints of the RIS. We show that the proposed groupwise SIC approach has significant advantages in both performance and computational complexity, as compared with the counterpart approaches.

## Reaping Both Latency and Reliability Benefits With Elaborate Sanitization Design for 3D TLC NAND Flash

- **Status**: ❌
- **Reason**: 3D TLC NAND 데이터 sanitization(Vt 분포 조작) - ECC/LDPC 기법 아님, 보안·소거 설계
- **ID**: ieee:10113786
- **Type**: journal
- **Published**: Nov. 2023
- **Authors**: Wei-Chen Wang, Chien-Chung Ho, Yung-Chun Li +2
- **PDF**: https://ieeexplore.ieee.org/document/10113786
- **Abstract**: With the rising security concern on modern storage systems, the concept of data sanitization has been widely investigated recently. Among the existing works targeting data sanitization, an overwriting-based approach, namely one-shot sanitization, is one of the most efficient sanitization approaches. Nonetheless, we find that the one-shot sanitization approach would fail to achieve precise data sanitization for 3D TLC NAND flash, because of incurring undesired data errors. That is, how to simultaneously realize precise sanitization and high security with decent latency and reliability on emerging storage devices remains unsolved. This work proposes an elaborate sanitization design that skillfully manipulates the threshold voltage ($V_{t}$Vt) distribution of sanitized pages. Not only does the proposed design achieve precise sanitization and high security, but it also enhances read performance and data reliability. Specifically, this work elaborately sanitizes data by merging specific $V_{t}$Vt distributions of the target physical page on 3D TLC NAND flash. Besides, the proposed approach further takes lateral charge migration into consideration to improve data reliability. We conduct a series of experiments to evaluate our proposed approach on real 3D TLC NAND flash. The experiment results demonstrate the proposed approach can achieve elaborate data sanitization under various scenarios and improve read performance by 29%.

## Expectation Propagation for Flat-Fading Channels

- **Status**: ❌
- **Reason**: flat-fading 채널 신호검출용 expectation propagation 검출기; LDPC ECC 이식 기법 없음
- **ID**: ieee:10184178
- **Type**: journal
- **Published**: Nov. 2023
- **Authors**: Elisa Conti, Amina Piemontese, Giulio Colavolpe +1
- **PDF**: https://ieeexplore.ieee.org/document/10184178
- **Abstract**: This letter addresses the problem of signal detection in flat-fading channels. In this context, receivers based on the expectation propagation framework appear to be very promising although presenting some critical issues. We develop a new algorithm based on this framework where, unlike previous works, convergence is achieved after a single forward-backward pass, without additional inner detector iterations. The proposed message scheduling, together with novel adjustments of the approximating distributions’ parameters, allows to obtain significant performance advantages with respect to the state-of-the-art solution. Simulation results show the applicability of this algorithm when sparser pilot configurations have to be adopted and a considerable gain compared to the current available strategies.

## A Novel Polar Code Construction for Magnetic Induction-Based Wireless Underground Communications

- **Status**: ❌
- **Reason**: 지하 무선통신용 polar code 구성; LDPC 아님, 무선 응용 특이적
- **ID**: ieee:10244082
- **Type**: journal
- **Published**: Nov. 2023
- **Authors**: Ziwei Chen, Guanghua Liu, Huaijin Zhang +1
- **PDF**: https://ieeexplore.ieee.org/document/10244082
- **Abstract**: Magnetic induction-based wireless underground communications (MI-WUC) is susceptible to interference from the diverse underground environment, leading to intricate channel distributions and low communication reliability. To address these challenges, we propose a novel polar code construction scheme specifically optimized for MI-WUC. Our scheme extends traditional channel polarization to incorporate complex channel polarization, allowing it to adapt to various underlying channels. Further, we provide a calculation formula for Bhattacharyya parameters and a construction method for polar codes. Simulations show that our scheme achieves higher transmission rates and broader communication ranges compared to general schemes.

## Bit-Metric Decoding Rate in Multi-User MIMO Systems: Theory

- **Status**: ❌
- **Reason**: MU-MIMO PHY abstraction용 SINR 메트릭 ML 예측; LDPC 디코더/코드설계 기여 없음
- **ID**: ieee:10077516
- **Type**: journal
- **Published**: Nov. 2023
- **Authors**: K. Pavan Srinath, Jakob Hoydis
- **PDF**: https://ieeexplore.ieee.org/document/10077516
- **Abstract**: LA is one of the most important aspects of wireless communications where the MCS used by the transmitter is adapted to the channel conditions in order to meet a certain target error-rate. In a SU-SISO system with out-of-cell interference, LA is performed by computing the post-equalization SINR at the receiver. The same technique can be employed in MU-MIMO receivers that use linear detectors. Another important use of post-equalization SINR is for PHY abstraction, where several PHY blocks like the channel encoder, the detector, and the channel decoder are replaced by an abstraction model in order to speed up system-level simulations. However, for MU-MIMO systems with non-linear receivers, there is no known equivalent of post-equalization SINR which makes both LA and PHY abstraction extremely challenging. This important issue is addressed in this two-part paper. In this part, a metric called the BMDR of a detector, which is the proposed equivalent of post-equalization SINR, is presented. Since BMDR does not have a closed form expression that would enable its instantaneous calculation, a machine-learning approach to predict it is presented along with extensive simulation results.

## Bit Error Rate Performance Comparison of Low-Density Parity-Check Code and Polar Code

- **Status**: ❌
- **Reason**: 표준 LDPC vs Polar BER 비교 시뮬레이션만, 떼어낼 새 디코더/구성 기여 없음
- **ID**: ieee:10374061
- **Type**: conference
- **Published**: 8-9 Nov. 2
- **Authors**: Putri Shabrina Wulandari, Eva Y. D. Utami, Ivanna K. Timotius
- **PDF**: https://ieeexplore.ieee.org/document/10374061
- **Abstract**: A fifth generation or 5G wireless communication is claimed to be able to upload data 20 times faster than 4G networks. With the introduction of 5G wireless communication, an error-correcting code is required to detect and reduce errors. From the many existing error-correcting codes, the Low-Density Parity Check (LDPC) Code and Polar Code were chosen because they have many advantages for 5G wireless communication. Here, we report the study results and compare the LDPC and Polar Codes coding techniques on Additive White Gaussian Noise and Rayleigh Multipath Fading channel modeling using Binary Phase Shift Keying (BPSK) modulation. Our study presents the simulation results as the mean and standard error of the Bit Error Rate (BER). From the resulting BER, the Polar Code traversed on the AWGN channel can produce error-free at low Eb/No values. This study emphasizes that Polar Code is a more suitable error-correcting for applications in 5G wireless communication than LDPC Code.

## List Decoding of Tanner and Expander Amplified Codes from Distance Certificates

- **Status**: ❌
- **Reason**: Tanner/익스팬더 코드 list decoding을 SoS SDP로 푸는 순수 이론(알파벳 size q 일반·near-MDS). 비이진 일반화이고 NAND 이식 가능 디코더/구성 기여 없음
- **ID**: ieee:10353200
- **Type**: conference
- **Published**: 6-9 Nov. 2
- **Authors**: Fernando Granha Jeronimo, Shashank Srivastava, Madhur Tulsiani
- **PDF**: https://ieeexplore.ieee.org/document/10353200
- **Abstract**: We develop new list decoding algorithms for Tanner codes and distance-amplified codes based on bipartite spectral expanders. We show that proofs exhibiting lower bounds on the minimum distance of these codes can be used as certificates discoverable by relaxations in the Sum-of-Squares (SoS) semi-definite programming hierarchy. Combining these certificates with certain entropic proxies to ensure that the solutions to the relaxations cover the entire list, then leads to algorithms for list decoding several families of codes up to the Johnson bound. We prove the following results:- We show that the LDPC Tanner codes of Zémor [IEEE Trans. Inf. Theory 2001] with alphabet size q, block-length n and distance $\delta$, based on an expander graph with degree d, can be list-decoded up to distance $\mathcal{J}_{q}(\delta)-\varepsilon$ in time $n^{O_{d, q}\left(1 / \varepsilon^{4}\right)}$, where $\mathcal{J}_{q}(\delta)$ denotes the Johnson bound.- We show that the codes obtained via the expander-based distance amplification procedure of Alon, Edmonds and Luby [FOCS 1995] can be list-decoded close to the Johnson bound using the SoS hierarchy, by reducing the list decoding problem to unique decoding of the base code. In particular, starting from any base code unique-decodable up to distance $\delta$, one can obtain near-MDS codes with rate R and distance $1-R-\varepsilon$, list-decodable up to the Johnson bound in time $n^{O_{\varepsilon, \delta}(1)}$.- We show that the locally testable codes of Dinur et al. [STOC 2022] with alphabet size q, block-length n and distance $\delta$ based on a square Cayley complex with generator sets of size d, can be list-decoded up to distance $\mathcal{J}_{q}(\delta)-\varepsilon$ in time $n^{O_{d, q}\left(1 / \varepsilon^{4}\right)}$, where $\mathcal{J}_{q}(\delta)$ denotes the Johnson bound.

## Randomly Punctured Reed-Solomon Codes Achieve the List Decoding Capacity over Polynomial-Size Alphabets

- **Status**: ❌
- **Reason**: Reed-Solomon 랜덤 펑처링의 list decoding capacity 이론. LDPC 무관, 다항크기 알파벳 비이진
- **ID**: ieee:10353231
- **Type**: conference
- **Published**: 6-9 Nov. 2
- **Authors**: Zeyu Guo, Zihan Zhang
- **PDF**: https://ieeexplore.ieee.org/document/10353231
- **Abstract**: This paper shows that, with high probability, randomly punctured Reed-Solomon codes over fields of polynomial size achieve the list decoding capacity. More specifically, we prove that for any $\varepsilon \gt 0$ and $R \in(0,1)$, with high probability, randomly punctured Reed-Solomon codes of block length n and rate R are $(1-R-\varepsilon, O(1 / \varepsilon))$ list decodable over alphabets of size at least $2^{\text {poly }(1 / \varepsilon)} n^{2}$. This extends the recent breakthrough of Brakensiek, Gopi, and Makam (STOC 2023) that randomly punctured Reed-Solomon codes over fields of exponential size attain the generalized Singleton bound of Shangguan and Tamo (STOC 2020).

## HDX Condensers

- **Status**: ❌
- **Reason**: 이분 expander/HDX 조합론적 구성 순수 이론, LDPC 코드설계 직접 이식 불명확하고 디코더/HW로 안 이어짐.
- **ID**: ieee:10353114
- **Type**: conference
- **Published**: 6-9 Nov. 2
- **Authors**: Itay Cohen, Roy Roth, Amnon Ta-Shma
- **PDF**: https://ieeexplore.ieee.org/document/10353114
- **Abstract**: More than twenty years ago, Capalbo, Rein-gold, Vadhan and Wigderson gave the first (and up to date only) explicit construction of a bipartite expander with almost full combinatorial expansion. The construction incorporates zig-zag ideas together with extractor technology, and is rather complicated. We give an alternative construction that builds upon recent constructions of hyper-regular, high-dimensional expanders. The new construction is, in our opinion, simple and elegant.Beyond demonstrating a new, surprising, and intriguing, application of high-dimensional expanders, the construction employs totally new ideas which we hope may lead to progress on the still remaining open problems in the area.

## From Grassmannian to Simplicial High-Dimensional Expanders

- **Status**: ❌
- **Reason**: 고차원 익스팬더(HDX)·단체복합체와 LDPC의 위상수학적/대수학적 연결 순수 이론. 디코더·HW·구체적 바이너리 코드 구성으로 안 이어짐
- **ID**: ieee:10353186
- **Type**: conference
- **Published**: 6-9 Nov. 2
- **Authors**: Louis Golowich
- **PDF**: https://ieeexplore.ieee.org/document/10353186
- **Abstract**: In this paper, we present a new construction of simplicial complexes of subpolynomial degree with arbitrarily good local spectral expansion. Previously, the only known high-dimensional expanders (HDXs) with arbitrarily good expansion and less than polynomial degree were based on one of two constructions, namely Ramanujan complexes and coset complexes. In contrast, our construction is a Cayley complex over an abelian group, with Cayley generating set given by a Grassmannian HDX.Our construction is in part motivated by a coding-theoretic interpretation of Grassmannian HDXs that we present, which provides a formal connection between Grassmannian HDXs, simplicial HDXs, and LDPC codes. We apply this interpretation to prove a general characterization of the 1-homology groups of our Cayley simplicial complexes. Using this result, we construct simplicial complexes on N vertices with arbitrarily good local expansion for which the dimension of the 1-homology group grows as the squared logarithm of N. No prior constructions in the literature have been shown to achieve as large a 1-homology group.

## Semantics-Empowered UAV-assisted Wireless Communication System for Wildfire Detection

- **Status**: ❌
- **Reason**: UAV 산불탐지 DJSCC 시맨틱 통신. JSCC로 ECC 기법 떼어낼 것 없음
- **ID**: ieee:10478404
- **Type**: conference
- **Published**: 6-8 Nov. 2
- **Authors**: Chathuranga M. Wijerathna Basnayaka, Dushantha Nalin K. Jayakody, Marko Beko
- **PDF**: https://ieeexplore.ieee.org/document/10478404
- **Abstract**: With the increasing occurrence of wildfires globally, quick and effective detection methods are vital. This paper proposes an innovative solution for wildfire detection using Unmanned Aerial Vehicle (UAV)-assisted detection systems. On the other hand, semantic communication, a technology designed for efficient data transmission in specialized tasks, plays a crucial role in next-generation wireless communications systems. In this paper, the deep joint source-channel coding (DJSCC) scheme has been used for efficient image transmission as a deep learning based semantic communication technique for wildfire detection. DJSCC improves source and channel coding for semantic communications, offering advantages such as improved energy efficiency, reduced latency, and improved reliability compared to traditional source and channel code schemes. In this paper, the transmitter-receiver operations of the UAV communication system are modeled as a DJSCC, and they are jointly trained while taking into account the effects of the fading channel. The encoder transforms captured images into compact feature vectors, subsequently transmitting them using a reduced number of channels to minimize latency. Rather than engaging in the reconstruction of the input image in the receiver, the classifier performs a classification task using the received signals at the receiver. Alternatively, if the recovery of an image is required to understand the spread of the wildfire, the decoder reconstructs it by using the received signal at the receiver.

## A DigiLogue Receiver Design for Tbps Wireless Transmissions over Flat-Fading Channels

- **Status**: ❌
- **Reason**: 아날로그 도메인 DigiLogue 수신기(Tbps 무선). 단순 반복부호 수준, LDPC 디코더 신규 기여 없음
- **ID**: ieee:10478408
- **Type**: conference
- **Published**: 6-8 Nov. 2
- **Authors**: Mahmoud Mojarrad Kiasaraei, Rahim Tafazolli, Konstantinos Nikitopoulos
- **PDF**: https://ieeexplore.ieee.org/document/10478408
- **Abstract**: Utilizing ultra-wide bandwidths is a promising approach to achieve the terabits per second (Tbps) wireless links required to unlock emerging mobile applications such as holographic telepresence. However, conventional digital systems face significant challenges to exploit such ultra-wide bandwidths efficiently. On the one hand, utilizing ultra-fast, high-precision analogue-to-digital converters (ADCs) required for ultra-wide bandwidth systems becomes impractical in terms of power consumption. On the other hand, performing ultra-fast receiver processing becomes extremely challenging in terms of power consumption and processing latency not only due to the complexity of state-of-the-art signal processing algorithms but also because the increased sampling rates challenge the speed capabilities of modern digital processors. To overcome these bottlenecks, the Digilogue processing has been recently proposed, which suggests to perform signal processing directly in the analogue domain without requiring ADCs and traditional digital signal processing. While initial results show that DigiLogue receivers can potentially achieve substantial power gains, they focus on oversimplified evaluations that are far from being practical since they only account for simple repetition codes and additive white Gaussian noise (AWGN) channels. In this work, we propose a DigiLogue receiver design suitable for flat-fading channels, which is of very high interest in the case of systems operating at higher frequencies where ultra-wide bandwidths can be available. In contrast to existing analogue solutions, the proposed design can perform “soft” channel equalization/detection and decoding directly in the analogue domain and achieve the error rate performance of the corresponding digital systems, but with power savings of more than $36 \times$.

## Novel Joint Estimation and Decoding Metrics for Short-Blocklength Transmission Systems

- **Status**: ❌
- **Reason**: 5G 단블록 BICM joint estimation-detection 메트릭. LDPC는 베이스라인일 뿐 떼어낼 디코더/구성 기법 없음, 무선 응용 특이적
- **ID**: ieee:10453187
- **Type**: conference
- **Published**: 6-8 Nov. 2
- **Authors**: Mody Sy, Raymond Knopp
- **PDF**: https://ieeexplore.ieee.org/document/10453187
- **Abstract**: This paper presents Bit-Interleaved Coded Modulation metrics for joint estimation detection using training or reference signal transmission strategies for short to long block length channels. We show that it is possible to enhance the performance and sensitivity through joint detection-estimation compared to standard receivers, especially when the channel state information is unknown and the density of the training dimensions is low. The performance analysis makes use of a full 5G transmitter and receiver chains for both Polar and LDPC coded transmissions paired with BPSK/QPSK modulation schemes. We consider transmissions where reference signals are interleaved with data and both are transmitted over a small number of OFDM symbols so that near-perfect channel estimation cannot be achieved. Our findings demonstrate that when the detection windows used in the metric units is on the order of four modulated symbols the proposed BICM metrics can be used to achieve detection performance that is close to that of a coherent receiver with perfect channel state information for both polar and LDPC coded configurations. Furthermore, we show that for transmissions with low DMRS density, a good trade-off can be achieved in terms of additional coding gain and improved channel estimation quality by adaptive DMRS power adjustment.

## Optimization of NB-QC-LDPC Codes with Column Weight Not Exceeding Three

- **Status**: ❌
- **Reason**: NB-QC-LDPC(비이진/GF(q)) 흡수집합·최소거리 최적화, 비이진 LDPC는 즉시 제외
- **ID**: ieee:10369673
- **Type**: conference
- **Published**: 4-7 Nov. 2
- **Authors**: Jingke Zou, Liqian Wang
- **PDF**: https://ieeexplore.ieee.org/document/10369673
- **Abstract**: The non-binary quasi cyclic low-density parity-check (NB-QC-LDPC) code is a strong candidate code in optical communication. However, the presence of elementary absorbing sets in NB-QC-LDPC codes can degrade the frame error rate (FER) performance of the codes in the error floor region. Additionally, better minimum Hamming distance distribution can improve the FER performance of codes in the waterfall region. In this paper, a joint optimization of absorbing sets and minimum Hamming distance distribution is proposed for NB-QC-LDPC codes with a maximum column weight not exceeding 3. Simulation results show that the constructed codes could achieve comparable or better FER compared to the recently proposed NB-QC-LDPC codes with the same codes parameters.

## Research on the Performance of the LDPC-OQPSK System Used in Underwater Wireless Optical Communication

- **Status**: ❌
- **Reason**: 수중 광통신에 표준 LDPC를 부수 적용한 응용 논문, 떼어낼 새 디코더/코드/HW 기법 없음
- **ID**: ieee:10369914
- **Type**: conference
- **Published**: 4-7 Nov. 2
- **Authors**: Yi Yang, Qian Liu, Jiayuan Lei +3
- **PDF**: https://ieeexplore.ieee.org/document/10369914
- **Abstract**: Under the novel ocean turbulence model of exponential-generalized gamma (EGG) distribution, low density parity check (LDPC) coding is introduced into underwater communication system modulated by the offset quadrature phase shift keying (OQPSK). The signal-to-noise ratio (SNR) gains of LDPC-OQPSK coded joint modulation system are simulated at different turbulence intensities and water qualities. It obtains SNR gain of 5.355 $dB$ in the clear seawater when the scintillation index is 0.2. Finally, a blue light communication setup is built to research the bit error rate (BER) performances of underwater LDPC-OQPSK.

## Novel Distribution Matcher Design for Short Length Frames Based on Non-Binary Convolutional Codes

- **Status**: ❌
- **Reason**: 비이진 컨볼루션 부호 기반 분포 매처(확률적 성형), LDPC ECC 아니고 non-binary, 떼어낼 ECC 기법 없음
- **ID**: ieee:10369240
- **Type**: conference
- **Published**: 4-7 Nov. 2
- **Authors**: Rami Klaimi, Akram Abouseif, Ghaya Rekaya-Ben Othman +1
- **PDF**: https://ieeexplore.ieee.org/document/10369240
- **Abstract**: We propose a distribution matcher that enables probabilistic constellation shaping while ensuring low-complexity dematching techniques. The proposal is based on non-binary convolutional codes, designed to respect a given optimal symbol distribution. In addition to lowering the dematching complexity, the proposed structure is shown to reduce the latency, to respect the target distribution with a low overhead and to outperform existing solutions with more than 0.3dB. It is also shown that, while being able to respect the target distribution for short frame lengths, the proposed technique helps enhancing the resilience of the optical system in question to the non-linearity effects.

## FPGA Implementation of Rate Matching in 5G NR PDSCH

- **Status**: ❌
- **Reason**: 5G NR rate matching의 FPGA 병렬화 — LDPC 인코딩 후단 비트선택/인터리빙, 디코더·코드설계 기여 아님
- **ID**: ieee:10322544
- **Type**: conference
- **Published**: 31 Oct.-3 
- **Authors**: Rochak Jain, Naveed Anjum, Samudrala Soujanya +5
- **PDF**: https://ieeexplore.ieee.org/document/10322544
- **Abstract**: 5G new radio (NR) distinguishes itself by offering remarkable features such as significantly higher throughput and lower latency compared to 4G. In 5G, low density parity check (LDPC) encoding is employed as the channel coding scheme for the transmission of data bits. Subsequent to the LDPC encoding stage, bit selection and bit interleaving operations are performed. Rate matching plays an important role in selecting specific encoded bits for transmission, utilizing techniques like shortening and repetition to support hybrid automatic repeat request functionality. To address the issue of latency encountered in processing large transport blocks, we propose parallel algorithms for the rate matching. These algorithms are implemented on field programmable gate arrays, and then the performance of the optimized algorithms is compared with the existing algorithms specified in the 3rd generation partnership project standards.

## Low-Complexity Decoding Algorithm Utilizing Degeneracy for Quantum LDPC Codes

- **Status**: ❌
- **Reason**: 양자 QLDPC degeneracy 후처리 디코더 — 양자 전용 개념(degeneracy·depolarizing channel)에 의존, 고전 바이너리 LDPC로 이식 불가
- **ID**: ieee:10356284
- **Type**: conference
- **Published**: 30 Oct.-3 
- **Authors**: Jaemin Kim, Hyunwoo Jung, Jeongseok Ha
- **PDF**: https://ieeexplore.ieee.org/document/10356284
- **Abstract**: Quantum low-density parity-check (QLDPC) codes have been considered as a promising solution for the fault-tolerant quantum computing. However, the belief propagation (BP) decoding for QLDPC codes does not take into account the degeneracy, resulting in certain performance degradation. Recently, various post-processing algorithms have been proposed to address this issue but they in return require excessive additional complexity and/or long decoding latency. Motivated by this, in this paper, we propose an efficient decoding algorithm that takes reduced decoding complexity for the post-processing. In particular, the proposed algorithm performs the post-processing in such a way that it first selects a variable node based on a proposed metric, and the depolarizing channel model for the selected variable node is reinitialized according to the BP decoding results. Then, the BP decoding is performed for the depolarizing channel model in which the selected node follows the reinitialized channel characteristics. The process of selection, reinitialization and BP decoding, say a trial, is iterated until it reaches a predetermined value or all syndromes are met. The main ideas of this work lie in formulating the metric for selection and reinitialization to minimize the number of trials until the degeneracy is resolved. Finally, simulation results show that the proposed decoding algorithms can significantly reduce the decoding complexity with similar decoding performance to that of an existing algorithm.

## Deep Learning-Based Demodulation in Impulse Noise Channels

- **Status**: ❌
- **Reason**: 임펄스 잡음 채널 딥러닝 복조기; LDPC 디코더 자체 기여 아님, ECC 복호 기법 떼어낼 것 없음
- **ID**: ieee:10356304
- **Type**: conference
- **Published**: 30 Oct.-3 
- **Authors**: Andreas Andersson, Kristoffer Hägglund, Erik Axell
- **PDF**: https://ieeexplore.ieee.org/document/10356304
- **Abstract**: Wireless systems on military platforms often operate in challenging electromagnetic environments. Such environments contain interference which tends to be non-Gaussian. A more suitable model to derive the necessary receiver algorithms is the Symmetric α-Stable distribution. Adapting a receiver to the α-Stable model provides significant performance gain in challenging interference environments compared to Gaussian-based receivers, at the cost of higher computational complexity. With the emergence of deep learning and neural networks, a promising application is replacing the steps of demodulation with a suitable network structure in order to decrease the complexity. In this work, the generalization capability of such networks is explored in order to examine the models’ ability to adapt to new, unseen error correcting codes of different length and type, and if good performance can be achieved in comparison to traditional demodulation as well as if the networks will consider code structure when demodulating.The results show that a networks ability to generalize largely depends on architecture, as well as training data. Furthermore, the models which were unable to generalize made bad decisions based on code structure assumptions, resulting in worse performance compared to the more general models even though it was trained and tested on the same code. It is shown that the proposed model performs well, on par with the α-Stable based method, with significantly lower computational costs.

## Open Source-Based Over-the-Air 5G New Radio Sidelink Testbed

- **Status**: ❌
- **Reason**: 5G sidelink testbed; LDPC는 표준 3GPP 부수 언급, 떼어낼 새 ECC 기법 없음
- **ID**: ieee:10356257
- **Type**: conference
- **Published**: 30 Oct.-3 
- **Authors**: Melissa Elkadi, Deokseong Kim, Ejaz Ahmed +4
- **PDF**: https://ieeexplore.ieee.org/document/10356257
- **Abstract**: The focus of this paper is to demonstrate an over-the-air (OTA) 5G new radio (NR) sidelink communication prototype. 5G NR sidelink communications allow NR UEs to transfer data independently without the assistance of a base station (gNB), which enables V2X communications, including platooning, autonomous driving, sensor extension, industrial IoT, public safety communication and much more. Our design leverages the open-source OpenAirInterface5G (OAI) software, which operates on software-defined radios (SDRs) and can be easily extended for mesh networking. The software includes all signal processing components specified by the 3GPP 5G sidelink standards, including Low-Density Parity Check (LDPC) encoding/decoding, polar encoding/decoding, data and control multiplexing, modulation/demodulation, and orthogonal frequency-division multiplexing (OFDM) modulation/demodulation. It can be configured to operate with different bands, bandwidths, and antenna settings.The first milestone in this work was to demonstrate the completed Physical Sidelink Broadcast Channel (PSBCH) development, which conducts synchronization between a Synchronization Reference (SyncRef) UE and a nearby UE. The SyncRef UE broadcasts a sidelink synchronization signal block (S-SSB) periodically, which the nearby UE detects and uses to synchronize its timing and frequency components with the SyncRef UE. Once a connection is established, the next developmental milestone is to transmit real data (text messages) via the Physical Sidelink Shared Channel (PSSCH). Our PHY sidelink framework is tested using both an RF simulator and an OTA testbed with multiple nearby UEs. Beyond the development of synchronization and data transmission/reception in 5G sidelink, we conclude with various performance tests and validation experiments. The results of these metrics show that our simulator is comparable to the OTA testbed and can be used for upper layer development in the future.

## Enhancing Cooperative Communications via Reconfigurable Intelligent Surface-Assisted Strategies and the Integration of Low-Density Parity-Check Codes

- **Status**: ❌
- **Reason**: RIS 협력통신에 표준 LDPC 적용 — 새 디코더/구성 없음, 무선 응용 특이적
- **ID**: ieee:10404162
- **Type**: conference
- **Published**: 29-30 Nov.
- **Authors**: Shakespear Takudzwa Samu, Shunwai Zhang, Samuel Magunda
- **PDF**: https://ieeexplore.ieee.org/document/10404162
- **Abstract**: Reconfigurable Intelligent Surfaces (RIS), also known as Intelligent Reconfigurable Surfaces (IRS), stand as one of the most promising technologies in wireless communications. Their remarkable attributes, including energy efficiency, low latency, and enhanced spectral efficiency, have drawn significant attention. This paper presents a novel approach to harnessing RIS for cooperative communications, seeking to replace traditional relay systems such as Decode and Forward (DF), Amplify and Forward (AF), and Coded Cooperation (CC). In this study, the RIS serves as a passive element within the communication system. The information originates from the sources and is transmitted to the RIS and destination in a single timeslot. RIS plays its role by reflecting the messages and redirecting them toward their intended destination. Additionally, this paper proposes an innovative combination of the RIS system with Low-Density Parity Check (LDPC) codes to enhance the overall system performance. Encoding of messages takes place at the source, while decoding occurs at the destination, facilitating the retrieval of the original information bits. Furthermore, the paper incorporates the Maximal Ratio Combining (MRC) technique to effectively combine signals for joint iterative decoding at the destination. The entire simulation was conducted using MATLAB software, with a focus on assessing key performance parameters (KPIs), namely the Bit Error Rate (BER) and Signal-to-Noise Ratio (SNR). Our proposed system was subjected to comparative analysis against various benchmarks, including a system without RIS, a system featuring coded cooperation relay, and several RIS-based systems with varying numbers of RIS surfaces. The objective was to not only demonstrate the enhanced BER performance brought about by our proposed system but also to determine the optimal conditions under which it operates most effectively. This research showcases the potential of RIS in transforming cooperative communications and paving the way for more efficient and reliable wireless networks.

## BiSPARCs for Unsourced Random Access in Massive MIMO

- **Status**: ❌
- **Reason**: 무선 unsourced random access(SPARC+BiGAMP), LDPC는 outer code 베이스라인일 뿐 떼어낼 ECC 기법 없음
- **ID**: ieee:10477087
- **Type**: conference
- **Published**: 29 Oct.-1 
- **Authors**: Patrick Agostini, Zoran Utkovski, Slawomir Stanczak
- **PDF**: https://ieeexplore.ieee.org/document/10477087
- **Abstract**: This paper considers the massive MIMO unsourced random access problem in a quasi-static Rayleigh fading setting. The proposed coding scheme is based on a concatenation of a “conventional” channel code (such as, e.g., LDPC) serving as an outer code, and a sparse regression code (SPARC) serving as an inner code. The scheme combines channel estimation, single-user decoding, and successive interference cancellation in a novel way. The receiver performs joint channel estimation and SPARC decoding via an instance of a bilinear generalized approximate message passing (BiGAMP) based algorithm, which leverages the intrinsic bilinear structure that arises in the considered communication regime. The detection step is followed by a per-user soft-input-soft-output (SISO) decoding of the outer channel code in combination with a successive interference cancellation (SIC) step. We show via numerical simulation that the resulting scheme achieves stat-of-the-art performance in the massive connectivity setting, while attaining comparatively low implementation complexity.

## URLLC in IRS-Aided MIMO Systems: Finite Blocklength Analysis and Design

- **Status**: ❌
- **Reason**: IRS-MIMO URLLC 유한블록길이 이론 bound — LDPC는 검증 베이스라인, 디코더/HW 기여 없음
- **ID**: ieee:10476786
- **Type**: conference
- **Published**: 29 Oct.-1 
- **Authors**: Xin Zhang, Shenghui Song
- **PDF**: https://ieeexplore.ieee.org/document/10476786
- **Abstract**: This paper investigates the ultra reliable and low latency communication (URLLC) performance of the IRS-aided MIMO system. The upper and lower bounds of the optimal average error probability (OAEP) for the coding rate within $\mathcal{O}\left(\frac{1 }{\sqrt{M n}}\right)$ of the capacity are derived, where n and M represent the blocklength and the number of transmit antennas, respectively. To achieve this goal, a new central limit theorem (CLT) for the mutual information density over the IRS-aided MIMO system is derived in the asymptotic regime where the block-length, the IRS size, and number of the antennas go to infinity with the same pace. The CLT is then utilized to derive the closed-form upper and lower bounds for the OAEP. Based on the analysis result, a gradient-based algorithm is proposed to minimize the lower bound of the OAEP by optimizing the phase shift of the IRS. Simulation results validate the fitness of the CLT and the effectiveness of the proposed algorithm in optimizing the theoretical bound, as well as the performance of practical LDPC code.

## LLR Refinement Strategies for Iterative Detection and Decoding Schemes in Cell-Free Massive MIMO Networks

- **Status**: ❌
- **Reason**: CF-mMIMO IDD용 LLR 정제(MMSE-PIC/검열/선형결합) — 검출기 영역 기법, 떼어낼 LDPC 디코더/코드/HW 기여 없음
- **ID**: ieee:10476860
- **Type**: conference
- **Published**: 29 Oct.-1 
- **Authors**: Tonny Ssettumba, Zhichao Shao, Lukas T. N. Landau +3
- **PDF**: https://ieeexplore.ieee.org/document/10476860
- **Abstract**: In this paper, we propose low-complexity local detectors and log-likelihood ratio (LLR) refinement techniques for a coded cell-free massive multiple input multiple output (CF-mMIMO) systems, where an iterative detection and decoding (IDD) scheme is applied using parallel interference cancellation (PIC) and access point (AP) selection. In particular, we propose three LLR processing schemes based on the individual processing of the LLRs of each AP, LLR censoring, and a linear combination of LLRs by assuming statistical independence. We derive new closed-form expressions for the local soft minimum mean square error (MMSE)-PIC detector and receive matched filter (RMF). We also examine the system performance as the number of iterations increases. Simulations assess the performance of the proposed techniques against existing approaches.

## An Improved Dictionary Design for Multicarrier Underwater Transmission

- **Status**: ❌
- **Reason**: 수중 OFDM 압축센싱 채널추정 dictionary 설계 — LDPC ECC와 무관
- **ID**: ieee:10477070
- **Type**: conference
- **Published**: 29 Oct.-1 
- **Authors**: Xiang Huang, Rong-Rong Chen
- **PDF**: https://ieeexplore.ieee.org/document/10477070
- **Abstract**: In this work, we study joint channel estimation and turbo equalization for coded orthogonal frequency division multiplexing (OFDM) in underwater acoustic (UWA) channels. We propose an alignment-aware basis (Aw-BS) design for compressed sensing (CS) based channel estimation that explicitly takes time alignment of the OFDM blocks into account after Doppler resampling and carrier frequency offset (CFO) compensation. Using the data collected from actual underwater experiments, our results show that the proposed Aw-BS design enhances the CS algorithm's ability to focus on dominant signal paths, and yields superior performance to existing works that use a fixed basis for the CS based channel estimation.

## Improved Belief Propagation Polar Decoder Based on Permuted Factor Graphs and Reliable Frozen Nodes

- **Status**: ❌
- **Reason**: Polar 부호 BP 디코더 개선(permuted factor graph + frozen node) — Polar 전용 frozen 개념 의존, 바이너리 LDPC로 직접 이식 부적합
- **ID**: ieee:10382367
- **Type**: conference
- **Published**: 27-29 Nov.
- **Authors**: Van Phe Nguyen, Nghia Xuan Pham, Quach Co Nguyen
- **PDF**: https://ieeexplore.ieee.org/document/10382367
- **Abstract**: In this Letter, an improved belief propagation technique aided by reliable frozen nodes and a permuted factor graph is designed to enhance the performance of the polar decoding in the finite regime length. The support from added check nodes makes frozen nodes more reliable. At the same time, a wisely selected factor graph helps generate a large number of frozen nodes, thereby can provide better support for the decoding. The simulation results show that the proposed decoding scheme obtains gains of about 0.6 dB for the code (1024, 512) and 0.5 dB for the code (2048, 1024) at the BER of 10$^{-4}$, respectively, with reasonable complexity.

## Proficient Adjacent Error Correcting Codes

- **Status**: ❌
- **Reason**: 메모리 인접오류 행렬/해밍 코드 — LDPC 아님, 표준 해밍 ECC
- **ID**: ieee:10389891
- **Type**: conference
- **Published**: 24-26 Nov.
- **Authors**: Neelima K, C. Subhas
- **PDF**: https://ieeexplore.ieee.org/document/10389891
- **Abstract**: As technology scales down, the semiconductor memories undergo radiation effects due to congestion which may be recovered called as soft errors. This paper develops three decoding mechanisms of matrix codes to detect and correct errors in data read from memory using hamming and extended hamming codes. The proposed decoding method-1 uses extended hamming bits based on rows and vertical parity bits using columns odd adjacent bits in either half can be corrected. The proposed method-2 corrects half less by one data bit. The proposed method-3 corrects half adjacent erroneous data bits prove to be more reliable for image processing applications. The methods are developed in Verilog HDL code, verified for Zynq 28nm High-K CMOS FPGA in Xilinx Vivado tool. The method-3 achieves a decrease in code rate by 52%, increase in bit overhead by 31.24%, decrease in area by atleast 5.08% and power delay product by atleast 24.07%.

## Nonbinary Zipper Codes Based on Reed-Solomon Codes

- **Status**: ❌
- **Reason**: 비이진 zipper/RS 부호 기반, ABP 디코딩이지만 RS 구조 의존 — 비이진+비-LDPC로 제외
- **ID**: ieee:10405189
- **Type**: conference
- **Published**: 2-4 Nov. 2
- **Authors**: Mengjiao Li, Chen Zhou, Ruimin Yuan +3
- **PDF**: https://ieeexplore.ieee.org/document/10405189
- **Abstract**: In this paper, we study nonbinary zipper codes constructed based on Reed-Solomon (RS) codes. In addition, the sliding window decoding (SWD) based on adaptive belief propagation (ABP) is proposed. Furthermore, we propose the miscorrection mitigation algorithm by introducing a scaling factor β. Simulation results show that a rate 0.73 zipper code constructed by (63,55) RS code, using SWD based on ABP, has better performance than the SWD based on hard-decision decoding by 2.2 dB at a frame error rate (FER) of 10−6.

## Path Metric Range Based Iterative Construction Method for Polar Codes

- **Status**: ❌
- **Reason**: Polar code 구성(SCL 디코딩용 PMR) — 비-LDPC, 부호 구성 기법이라 LDPC BP에 이식 불가
- **ID**: ieee:10405177
- **Type**: conference
- **Published**: 2-4 Nov. 2
- **Authors**: Hao Chen, Rongchi Xu, Baoming Bai
- **PDF**: https://ieeexplore.ieee.org/document/10405177
- **Abstract**: In this paper, we consider the construction of polar codes for the successive cancellation list (SCL) decoding and propose a path metric range (PMR) based iterative construction method. In order to find the construction sequence for the SCL decoding, we simulate and calculate the PMRs and log-likelihood ratios (LLRs) of sub-channels to select the frozen bits and information bits, which is different from the the construction based on the successive cancellation (SC) decoding to calculate the error probability of sub-channels. The proposed construction can achieve 0.3 dB and 1.2 dB gain over the union-Bhattacharyya bound weight (SUBW) method and the Gaussian approximation (GA) method/polarization weight (PW) method in the SCL decoding algorithm, respectively. When using the CRC-aided SCL (CA-SCL) decoding, the proposed construction can also achieve 0.5 dB gain compared to traditional construction schemes.

## Slotted ALOHA-based URA Scheme with Index Modulation for Short Block Length

- **Status**: ❌
- **Reason**: URA 슬롯ALOHA+CS+LDPC 결합 무선 응용, HD 디코더는 표준 수준이고 떼어낼 LDPC ECC 신규 기법 없음
- **ID**: ieee:10404132
- **Type**: conference
- **Published**: 2-4 Nov. 2
- **Authors**: Linjie Yang, Pingzhi Fan, Jingqiu Gao
- **PDF**: https://ieeexplore.ieee.org/document/10404132
- **Abstract**: Unsourced random access (URA) has become a promising technique to support massive connectivity scenarios. This work proposes a slotted ALOHA-based URA scheme with index modulation for short packet transmission under Multiple-Input Multiple-Output (MIMO) channel. In our scheme, the short data packet of each active user is divided into three parts, where the first two parts are encoded by compressed sensing (CS) and the low-density-parity-check (LDPC) code, respectively, while the third part is the index of the slot where the encoded packet is transmitted. The data decoding is implemented slot-by-slot at the base station (BS). To this end, a hard decision (HD)-based decoder, including the index modulation demodulation, CS decoding, and LDPC decoding, is developed. Simulation results reveal that our proposal outperforms the counterparts significantly.

## Performance of PSA-EKF Phase Noise Compensation in 3GPP Phase Noise Models for Mobile Backhaul Links

- **Status**: ❌
- **Reason**: 위상잡음 보상(PSA-EKF) 연구, LDPC는 베이스라인 부수 언급, 떼어낼 ECC 기법 없음
- **ID**: ieee:10460604
- **Type**: conference
- **Published**: 19-22 Nov.
- **Authors**: Ryota Kuribayashi, Mamoru Sawahashi, Norifumi Kamiya
- **PDF**: https://ieeexplore.ieee.org/document/10460604
- **Abstract**: The time-varying phase noise (PN) due to a local oscillator of a base station and a set of user equipment (UE) is a major impairment to the backhaul and access links employing millimeter-wave bands. This paper presents the bit error rate (BER) performance of a pilot symbol assisted (PSA)-extended Kalman filter (EKF) phase noise compensation (PNC) method that combines PSA PNC in the time domain and iterative PNC using the EKF in the 3rd Generation Partnership Project (3GPP) PN model for orthogonal frequency division multiplexing (OFDM) backhaul links. We first derive the discrete-time transfer function of the power spectral density based on the z-transform for time-domain 3GPP PN signal generation employing a small number of low-pass filter taps, and show the validity of the generated PN signal based on a comparison to the continuous-time transfer function that is specified by the 3GPP Technical Report. We then show that when using PSA-EKF PNC with a low-density parity-check (LDPC) code and the coding rate of 8/9, the loss in the required received signal-to-noise ratio (SNR) satisfying the BER of $10^{-8}$ in 3GPP PN Models 1 and 2 compared to that without PN is only approximately 2.3 dB and 0.6 dB, respectively.

## Viterbi Soft Demodulation Algorithm for CPFSK Systems

- **Status**: ❌
- **Reason**: CPFSK용 Viterbi 소프트 복조 LLR 계산 — 변조/복조 특이적, LDPC는 부수 언급, 떼어낼 LDPC 기법 없음
- **ID**: ieee:10355684
- **Type**: conference
- **Published**: 17-19 Nov.
- **Authors**: Changheng Wang, Xinyu Wang, Kun Jiang +1
- **PDF**: https://ieeexplore.ieee.org/document/10355684
- **Abstract**: Continuous Phase Frequency Shift Keying (CPFSK) is a phase-continuous constant-envelope modulation scheme. In modern communication systems, Turbo codes or LDPC codes are commonly used as error control codes to combat the effects of channel noise and fading. In the process of channel decoding, soft demodulation information is required to reduce the bit error rate(BER). This paper proposes a soft output calculation method for CPFSK signals based on the Viterbi demodulation algorithm. The method utilizes the difference of cumulative correlation values of the signal to characterize the log-likelihood ratio (LLR) information of the information symbols based on the derived results from conditional probability theory. These LLR values are then used as soft decision outputs. Simulation results demonstrate that, with almost no increase in algorithm complexity, this method achieves a performance improvement of approximately 3dB compared to hard decision demodulation.

## LLR Metrics for 16K-QAM Soft-Decision: Implementation in IEEE 802.11bn (Wi-Fi 8)

- **Status**: ❌
- **Reason**: Wi-Fi 8 16K-QAM 소프트판정 LLR 메트릭 — 변조 응용 특이적, LDPC는 부수 언급, 떼어낼 ECC 기법 없음
- **ID**: ieee:10361859
- **Type**: conference
- **Published**: 15-17 Nov.
- **Authors**: Roger Pierre Fabris Hoefel
- **PDF**: https://ieeexplore.ieee.org/document/10361859
- **Abstract**: The IEEE 802.11 Ultra High Reliability (UHR) Study Group (SG) was created in July 2022 to develop the 802.11bn amendment (Wi-Fi 8). It aims to deliver a maximum aggregate throughput of at least 100 Gbps measured at medium access control (MAC) service access point (SAP) with low latency and high reliability. This allows supporting advanced services, such as extended reality/virtual reality, metaverse, robotics [1]. In this paper, aiming to increase the physical layer (PHY) throughput, it is derived and validated low-complexity log-likelihood ratio (LLR) metrics suitable for soft-decoding rectangular Gray-coding 16K-QAM scheme with either binary convolutional codes (BCC) or low-density parity-check (LDPC) codes.

## A Low Complexity Turbo MMSE Equalization Method for OTFS Underwater Acoustic Communications

- **Status**: ❌
- **Reason**: OTFS 수중음향 turbo MMSE 등화에 LDPC가 베이스라인일 뿐, 떼어낼 ECC 기법 없음
- **ID**: ieee:10400345
- **Type**: conference
- **Published**: 14-17 Nov.
- **Authors**: Qingsong Wang, Nan Zhao, Lianyou Jing +2
- **PDF**: https://ieeexplore.ieee.org/document/10400345
- **Abstract**: This paper provides a low complexity turbo iterative equalization algorithm for OTFS underwater acoustic communication systems. The method defines the influence range of symbols in the delay-doppler domain, performs symbol-by-symbol MMSE equalization and LDPC soft decoding. By exchanging soft information between equalizer and decoder, turbo iteration equalization is realized. It uses iterative structure to further enhance the performance by using the information of the previous iteration. In addition, based on block iterative matrix inversion, the direct inversion of large matrices is avoided. Simulation results show that the proposed method can significantly reduce the computational complexity while losing less performance.

## Density Evolution Analysis for 5G NR Quasi-Cyclic Low Density Parity Check (QC-LDPC) Codes

- **Status**: ❌
- **Reason**: 5G NR QC-LDPC 표준부호의 DE 분석(이론 bound). 표준 부호 재사용, 신규 디코더/구성/HW 기여 없음
- **ID**: ieee:10390907
- **Type**: conference
- **Published**: 13-15 Nov.
- **Authors**: Wahidin, Khoirul Anwar, Nachwan Mufti Adriansyah
- **PDF**: https://ieeexplore.ieee.org/document/10390907
- **Abstract**: In this paper, we analyze the performances of the fifth telecommunication generation (5G) new radio (NR) quasi-cyclic (QC) low-density parity check (QC-LDPC) codes via density evolution (DE) for base graph 2 (BG2) over binary erasure channel (BEC). We derive the degree distribution of variable nodes (VND) and check nodes (CND) from the parity check matrix (PCM) of the 3rd Generation Partnership Project (3GPP) TS.38.212 and use them for DE analysis assuming of no cycle or girth. With several number of iterations, we found that 5G NR QC-LDPC of BG2 mother codes have a threshold of $\in$=0.2809. The DE analysis shows that the rateless capability with the extended parity successfully correct the error for higher $\in$, without suffering from the error-floor (although many degree-Is exist), but slightly loose in gap from the Shannon limit. We expect that these results are useful for the future development of QC-LDPC codes for possible improvement in the sixth telecommunication generation (6G).

## CVQKD System with Variable SNR Based on Variable Code Rate LDPC

- **Status**: ❌
- **Reason**: CVQKD variable code-rate LDPC for QKD reconciliation — info reconciliation not channel ECC, standard LDPC reuse, no new decoder/HW
- **ID**: ieee:10425909
- **Type**: conference
- **Published**: 10-12 Nov.
- **Authors**: Jiaxu Wen, Xuchao Liu
- **PDF**: https://ieeexplore.ieee.org/document/10425909
- **Abstract**: In this paper, a comprehensive overview of Gaussian data modulation and error correction negotiation in Continuous Variable Quantum Key Distribution (CVQKD) is presented. Emphasizing on CVQKD systems under varying Signal-to-Noise Ratios (SNR), a variable code rate Low-Density Parity-Check (LDPC) error correction method is employed. Our findings indicate that compared to the fixed code rate LDPC error correction, the variable code rate LDPC showcases superior error correction performance in CVQKD systems subjected to fluctuating SNR.

## Vehicle Density in mmWave 5G V2X Highway Communication Systems: A Channel Coding Approach

- **Status**: ❌
- **Reason**: V2X vehicle density study comparing turbo/polar/LDPC impact — LDPC is baseline benchmark only, no transplantable technique
- **ID**: ieee:10470852
- **Type**: conference
- **Published**: 10-12 Nov.
- **Authors**: Dimitrios Chatzoulis, Costas Chaikalis, Dimitrios Kosmanos +2
- **PDF**: https://ieeexplore.ieee.org/document/10470852
- **Abstract**: Vehicle-to-everything (V2X) is an emerging communication technology that enables data communication between vehicles and inevitably has become part of the 5th-Generation New Radio (5G-NR) and the millimeter wave 5G-NR (mmWave 5G-NR) technologies. The V2X use cases and their quality of service (QoS) parameters were defined by the 3rd-Generation Partnership Project (3GPP). These parameters, namely reliability, end-to-end latency, data rate and range, are highly dependent on channel coding, which is a method of improving communication quality. Apart from these parameters the 5G Automotive Association (5GAA) introduced vehicle density as another crucial parameter that is significantly affected by the 3GPP QoS parameters and the channel coding scheme, affecting the overall communication quality. Ιn this paper, we investigate the vehicle density constraints in a highway 5G V2X communication environment and we measure the impact of use of 4th-Generation Long-Term Evolution (4G-LTE) turbo codes, 5G-NR polar codes and low-density parity-check codes (LDPC) on vehicle density for all V2X use cases.
