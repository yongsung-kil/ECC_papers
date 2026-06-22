# IEEE Xplore — 2022-11


## Designing a Common DP-LDPC Code Pair for Variable On-Body Channels

- **Status**: ❌
- **Reason**: JSCC + DP-LDPC code pair (소스-채널 결합), 채널 ECC 기법 아님 — 제외 원칙
- **ID**: ieee:9788536
- **Type**: journal
- **Published**: Nov. 2022
- **Authors**: Dan Song, Jinkai Ren, Lin Wang +1
- **PDF**: https://ieeexplore.ieee.org/document/9788536
- **Abstract**: The joint source channel coding (JSCC) system is sensitive to the changing channel characteristics, because the optimally designed source-channel code pair always needs to be redesigned when the transmission environment is updated. A solution is to seek a common code pair for variable channels. Channel model 3 (CM3) is a variable on-body channel following the Weibull distribution, which is analyzed in four conditions due to varying shape factors, namely with exponential, Rayleigh, log-normal and normal distributions. The JSCC system is considered in this paper based on double protograph low-density parity-check (DP-LDPC) code pair over the variable CM3 channel. Firstly, four DP-LDPC code pairs are searched by the conventional differential evolution (DE) algorithm with four distributions of the Weibull model, respectively. However, these four code pairs only present good bit-error ratio performance in their own distribution, and have error floors in the other three. To resolve the problem, an artificial intelligence method based on principle component analysis (PCA) algorithm is designed to extract the common code pair. It is demonstrated that the common code pair performs well in noise-varying and practical-parameter transmissions. Instead of four DE code pairs, the designed one PCA code pair provides a strong technical support to low-complexity manufacturing such as eHealthcare.

## Lower Bounds for Maximally Recoverable Tensor Codes and Higher Order MDS Codes

- **Status**: ❌
- **Reason**: MR 텐서/고차 MDS 부호 순수 이론 bound (필드 크기), 디코더/HW로 안 이어짐
- **ID**: ieee:9812946
- **Type**: journal
- **Published**: Nov. 2022
- **Authors**: Joshua Brakensiek, Sivakanth Gopi, Visu Makam
- **PDF**: https://ieeexplore.ieee.org/document/9812946
- **Abstract**: An  $(m,n,a,b)$ -tensor code consists of  $m\times n$  matrices whose columns satisfy ‘ $a$ ’ parity checks and rows satisfy ‘ $b$ ’ parity checks (i.e., a tensor code is the tensor product of a column code and row code). Tensor codes are useful in distributed storage because a single erasure can be corrected quickly either by reading its row or column. Maximally Recoverable (MR) Tensor Codes, introduced by Gopalan et al., are tensor codes which can correct every erasure pattern that is information theoretically possible to correct. The main questions about MR Tensor Codes are characterizing which erasure patterns are correctable and obtaining explicit constructions over small fields. In this paper, we study the important special case when  $a=1$ , i.e., the columns satisfy a single parity check equation. We introduce the notion of higher order MDS codes ( $\mathrm {MDS}(\ell)$  codes) which is an interesting generalization of the well-known MDS codes, where  $\ell $  captures the order of genericity of points in a low-dimensional space. We then prove that a tensor code with  $a=1$  is MR if the row code is an  $\mathrm {MDS}(m)$  code. We then show that  $\mathrm {MDS}(m)$  codes satisfy some weak duality. Using this characterization and duality, we prove that  $(m,n,a=1,b)$ -MR tensor codes require fields of size  $q=\Omega _{m,b}(n^{\min \{b,m\}-1})$ . Our lower bound also extends to the setting of  $a>1$ . We also give a deterministic polynomial time algorithm to check if a given erasure pattern is correctable by the MR tensor code (when  $a=1$ ).

## On Hard and Soft Decision Decoding of BCH Codes

- **Status**: ❌
- **Reason**: BCH 부호 hard/soft 디코딩, LDPC 아님 — NAND LDPC 이식 기법 없음
- **ID**: ieee:9801634
- **Type**: journal
- **Published**: Nov. 2022
- **Authors**: Martin Bossert, Rebekka Schulz, Sebastian Bitzer
- **PDF**: https://ieeexplore.ieee.org/document/9801634
- **Abstract**: The binary primitive BCH codes are cyclic and are constructed by choosing a subset of the cyclotomic cosets. Which subset is chosen determines the dimension, the minimum distance and the weight distribution of the BCH code. We construct possible BCH codes and determine their coderate, true minimum distance and the non-equivalent codes. A particular choice of cyclotomic cosets gives BCH codes which are, extended by one bit, equivalent to Reed-Muller codes, which is a known result from the sixties. We show that BCH codes have possibly better parameters than Reed-Muller codes, which are related in recent publications to polar codes. We study the decoding performance of these different BCH codes using information set decoding based on minimal weight codewords of the dual code. We show that information set decoding is possible even in case of a channel without reliability information since the decoding algorithm inherently calculates reliability information. Different BCH codes of the same rate are compared and different decoding performances and complexity are observed. Some examples of hard decision decoding of BCH codes have the same decoding performance as maximum likelihood decoding. All presented decoding methods can possibly be extended to include reliability information of a Gaussian channel for soft decision decoding. We show simulation results for soft decision list information set decoding and compare the performance to other methods.

## Sparse IDMA: A Joint Graph-Based Coding Scheme for Unsourced Random Access

- **Status**: ❌
- **Reason**: unsourced random access용 sparse IDMA, 압축센싱+다중접속 그래프 — 떼어낼 LDPC ECC 기법 없음
- **ID**: ieee:9797778
- **Type**: journal
- **Published**: Nov. 2022
- **Authors**: Asit Kumar Pradhan, Vamsi K. Amalladinne, Avinash Vem +2
- **PDF**: https://ieeexplore.ieee.org/document/9797778
- **Abstract**: This article introduces a novel communication paradigm for the unsourced, uncoordinated Gaussian multiple access problem. The major components of the envisioned framework are as follows. The encoded bits of every message are partitioned into two groups. The first portion is transmitted using a compressive sensing scheme, whereas the second set of bits is conveyed using a multi-user coding scheme. The compressive sensing portion is key in sidestepping some of the challenges posed by the unsourced aspect of the problem. The information afforded by the compressive sensing is employed to create a sparse random multi-access graph conducive to joint decoding. This construction leverages the lessons learned from traditional IDMA into creating low-complexity schemes for the unsourced setting, while also accounting for inherent randomness. Under joint message-passing decoding, the proposed scheme offers good performance at a low computational complexity. Findings are supported by numerical simulations, and results are compared to existing alternatives.

## A Probabilistic Shaping Scheme for Bit-Interleaved Coded Modulation With Iterative Decoding

- **Status**: ❌
- **Reason**: BICM-ID 확률적 셰이핑 변조 기법, LDPC는 베이스라인 디코더 — 떼어낼 ECC 기여 없음
- **ID**: ieee:9864149
- **Type**: journal
- **Published**: Nov. 2022
- **Authors**: Weimin Kang
- **PDF**: https://ieeexplore.ieee.org/document/9864149
- **Abstract**: In this letter, a probabilistic shaping (PS) scheme for bit-interleaved coded modulation with iterative decoding (BICM-ID) between low density parity check (LDPC) decoder and demodulator is proposed. Compared to conventional LDPC-coded 8-quadrature amplitude modulation (QAM) system on additive white Gaussian noise (AWGN) channel, when spectral efficiency (SE) is 2.10 bits/s/Hz, the proposed PS-8QAM scheme for BICM-ID can obtain 0.73 dB theoretical gain, where the simulated error performance gain is 1.02 dB with frame error rate (FER) at 10−3. Compared to conventional LDPC-coded 32QAM system on AWGN channel, when SE is 3.75 bits/s/Hz, the proposed PS-32QAM scheme for BICM-ID can obtain 1.08 dB theoretical gain, where the simulated error performance gain is 1.10 dB with FER at 10−3. Both the information-theoretic analysis and simulated error performance show that the proposed PS scheme for BICM-ID is reliable, which is suitable for non gray mapped constellations.

## Machine Learning Based End-to-End Constellation Training for Communication Systems

- **Status**: ❌
- **Reason**: 오토인코더 기반 constellation 설계 — 변조/성상 최적화로 LDPC ECC와 무관
- **ID**: ieee:9980231
- **Type**: conference
- **Published**: 7-10 Nov. 
- **Authors**: Po-Chiang Lin
- **PDF**: https://ieeexplore.ieee.org/document/9980231
- **Abstract**: The constellation design is critical to the performance of communication systems. Conventional constellation schemes usually do not achieve optimal performance. Their design is usually based on some assumptions such as channel models and equal information bit probability distributions. Therefore, the performance degrades if the assumptions are unreal or oversimplified. Furthermore, effective and efficient methods to generate massive order constellations are still missing. In this paper, we propose a machine learning based constellation training method for communication systems. We use the autoencoder to train the constellation points. The proposed method trains the constellation by transmitted and received information bits. It does not depend on the assumptions such as specific channel models or information bit probability distributions. The proposed method can effectively optimize the constellation points, even for massive order constellations. Simulation results show that the proposed method outperforms conventional methods. The performance improvement is more significant when the number of bits per symbol is larger.

## A Modified Permutation Algorithm for Low Complexity Encoding in NB-QC-LDPC Codes

- **Status**: ❌
- **Reason**: NB-QC-LDPC(비이진) 인코딩용 순열 알고리즘 — non-binary는 제외 대상
- **ID**: ieee:10088896
- **Type**: conference
- **Published**: 5-8 Nov. 2
- **Authors**: Miao Zhu, Liqian Wang, Yatong Zhao +4
- **PDF**: https://ieeexplore.ieee.org/document/10088896
- **Abstract**: A modified permutation algorithm that optimizes the preprocessing step of the efficient encoding algorithm is proposed for nonbinary quasi-cyclic low-density parity-check (NB-QC-LDPC) codes. Linear complexity encoding is implemented and at least 0.15dB performance loss is avoided.

## DWDM Optical Network Monitoring Based on PAM4 Digital Label with QC-LDPC Coding

- **Status**: ❌
- **Reason**: DWDM 광망 모니터링에 표준 QC-LDPC를 응용 적용한 수준, 새 부호·디코더 기여 없음
- **ID**: ieee:10088729
- **Type**: conference
- **Published**: 5-8 Nov. 2
- **Authors**: Xue Wang, Tao Yang, Jiao Wang +2
- **PDF**: https://ieeexplore.ieee.org/document/10088729
- **Abstract**: A DWDM optical network monitoring scheme based on PAM4 digital label with QC-LDPC coding is proposed and demonstrated. The monitoring efficiency of the optical network monitoring system can be significantly improved, as more monitoring information of each channel can be obtained correctly and simultaneously with low cost.

## Interaction of Probabilistic Shaping and the LDPC Code Rate

- **Status**: ❌
- **Reason**: 확률적 셰이핑과 LDPC 부호율 상호작용 평가 — 시스템 레벨 분석, 떼어낼 디코더/구성 기법 없음
- **ID**: ieee:10089117
- **Type**: conference
- **Published**: 5-8 Nov. 2
- **Authors**: Zhongliang Sun, Han Cui, Du Tang +3
- **PDF**: https://ieeexplore.ieee.org/document/10089117
- **Abstract**: We evaluated the interaction of probabilistic shaping and forward error correction using low-density parity check. The results indicate that the shaping and the code rate should be simultaneously taken into consideration in probabilistic shaping system.

## A Low Complexity Windowed Decoding Based on Extended Min-Sum Algorithm for Non-Binary Spatially-Coupled LDPC Codes

- **Status**: ❌
- **Reason**: 비이진(non-binary) SC-LDPC용 EMS 윈도우 디코딩 — non-binary는 제외 대상
- **ID**: ieee:10088862
- **Type**: conference
- **Published**: 5-8 Nov. 2
- **Authors**: Yatong Zhao, Liqian Wang, Miao Zhu +4
- **PDF**: https://ieeexplore.ieee.org/document/10088862
- **Abstract**: A windowed decoding scheme based on the Extended Min-Sum algorithm (EMS-WD) is proposed in this paper, which can reduce the complexity of the window decoder by more than 30%. Furthermore, we propose an improved EMS-WD scheme (iEMS-WD), simulation result shows that 0.3 dB performance gain is obtained without the complexity cost.

## Security and Spectral Efficiency Enhanced OQAM/FBMC Based on a Chaotic Trellis Coded Modulation Encoder

- **Status**: ❌
- **Reason**: 카오스 TCM 인코더 기반 OQAM/FBMC 암호화/보안 기법 — LDPC 무관, 떼어낼 ECC 기법 없음
- **ID**: ieee:10088655
- **Type**: conference
- **Published**: 5-8 Nov. 2
- **Authors**: Yu Bai, Xiangyu Wu, Bo Liu +5
- **PDF**: https://ieeexplore.ieee.org/document/10088655
- **Abstract**: A novel encrypted PS OQAM/FBMC scheme based on the chaotic TCM encoder is proposed. The transmission experiment is demonstrated and the results verify the scheme shows higher spectral efficiency and security performance simultaneously.

## GS-16QAM OFDM with ANN Scheme for W-band RoF System

- **Status**: ❌
- **Reason**: W-band RoF용 GS-16QAM OFDM+ANN — LDPC 무관 무선 변조 기법, 떼어낼 ECC 기법 없음
- **ID**: ieee:10089025
- **Type**: conference
- **Published**: 5-8 Nov. 2
- **Authors**: Jiacong Liang, Jing He, Ran Song +2
- **PDF**: https://ieeexplore.ieee.org/document/10089025
- **Abstract**: In the paper, a geometrically shaped (GS) 16 QAM based OFDM with artificial neural network (ANN) scheme is proposed in W-band RoF system. After 0.8-m wireless transmission, the experimental results show that, the receiver sensitivity and NGMI of the GS-16QAM OFDM outperforms that of the OFDM with uniform 16QAM at the FEC threshold of 3.8×10-3.

## FPGA Implementation of Raptor Coded DS-CDMA for Wireless Sensor Networks in Low SNR Regime

- **Status**: ❌
- **Reason**: Raptor code+DS-CDMA FPGA 구현 - fountain/raptor 코드, LDPC 디코더 이식 기법 아님
- **ID**: ieee:10010226
- **Type**: conference
- **Published**: 4-5 Nov. 2
- **Authors**: Ikhlas M. Farhan, Dhafer R. Zaghar, Hadeel N. Abdullah
- **PDF**: https://ieeexplore.ieee.org/document/10010226
- **Abstract**: Reliable communications over a noisy channel have emerged as a severe challenge in the field of digital wireless communications. The proposed system addresses the high BER issue in AWGN channels in the Low SNR (LSNR) regime by combining the Raptor code with the DS-CDMA technique. This paper focuses on the hardware implementation of the proposed system. The hardware implementation was implemented on FPGA because it has the advantage of flexibility over traditional ASIC implementation. The Quarts tool is used to synthesize the proposed system on FPGA Altera DE2 70 using VHDL. As can be found in the report of compilation, approximately 32421 logic elements of the 68,416 logic elements available (47%) and 97 pins of the available 622 pins (16%) were employed.

## Quantum Tanner codes

- **Status**: ❌
- **Reason**: 양자 Tanner 코드(qLDPC) - 양자 EC 원칙 제외, 스태빌라이저 기반 양자 전용 구성
- **ID**: ieee:9996782
- **Type**: conference
- **Published**: 31 Oct.-3 
- **Authors**: Anthony Leverrier, Gilles Zémor
- **PDF**: https://ieeexplore.ieee.org/document/9996782
- **Abstract**: Tanner codes are long error correcting codes obtained from short codes and a graph, with bits on the edges and parity-check constraints from the short codes enforced at the vertices of the graph. Combining good short codes together with a spectral expander graph yields the celebrated expander codes of Sipser and Spielman, which are asymptotically good classical LDPC codes. In this work we apply this prescription to the left-right Cayley complex that lies at the heart of the recent construction of a c3 locally testable code by Dinur et at. Specifically, we view this complex as two graphs that share the same set of edges. By defining a Tanner code on each of those graphs we obtain two classical codes that together define a quantum code. This construction can be seen as a simplified variant of the Panteleev and Kalachev asymptotically good quantum LDPC code, with improved estimates for its minimum distance. This quantum code is closely related to the Dinur et at. code in more than one sense: indeed, we prove a theorem that simultaneously gives a linearly growing minimum distance for the quantum code and recovers the local testability of the Dinur et at. code.

## Explicit Lower Bounds Against Ω(n)-Rounds of Sum-of-Squares

- **Status**: ❌
- **Reason**: Sum-of-Squares 하한 증명 + qLDPC 기반 고차원 확장기 - 순수 이론, 디코더/HW/이식 가능 코드설계 없음
- **ID**: ieee:9996759
- **Type**: conference
- **Published**: 31 Oct.-3 
- **Authors**: Max Hopkins, Ting-Chun Lin
- **PDF**: https://ieeexplore.ieee.org/document/9996759
- **Abstract**: We construct an explicit family of 3-XOR instances hard for $\Omega(n)$-levels of the Sum-of-Squares (SoS) semi-definite programming hierarchy. Not only is this the first explicit construction to beat brute force search (beyond low-order improvements (Tulsiani 2021, Pratt 2021)), combined with standard gap amplification techniques it also matches the (optimal) hardness of random instances up to imperfect completeness (Grigoriev TCS 2001, Schoenebeck FOCS 2008).Our result is based on a new form of small-set high dimensional expansion (SS-HDX) inspired by recent breakthroughs in locally testable and quantum LDPC codes. Adapting the recent framework of Dinur, Filmus, Harsha, and Tulsiani (ITCS 2021) for SoS lower bounds from the Ramanujan complex to this setting, we show any (bounded-degree) SS-HDX can be transformed into a highly unsatisfiable 3-XOR instance that cannot be refuted by $\Omega(n)$-levels of SoS. We then show Leverrier and Zémor’s (Arxiv 2022) recent qLDPC construction gives the desired explicit family of bounded-degree SS-HDX. Incidentally, this gives the strongest known form of bi-directional high dimensional expansion to date.A full version of this paper is accessible at: https://arxiv.org/abs/2204.11469.

## End-to-End Learned Self-Interference Cancellation

- **Status**: ❌
- **Reason**: full-duplex self-interference cancellation NN, LDPC는 베이스라인 - 무선 응용 특이적, 떼어낼 ECC 기법 없음
- **ID**: ieee:10052024
- **Type**: conference
- **Published**: 31 Oct.-2 
- **Authors**: Alexios Balatsoukas-Stimming
- **PDF**: https://ieeexplore.ieee.org/document/10052024
- **Abstract**: Full-duplex communications systems can transmit and received information at the same time and on the same frequency band. However, they require strong self-interference (SI) cancellation. While a part of this SI cancellation is carried out in the analog domain, in most cases digital SI cancelation is required as well. In this work, we examine various digital SI cancellation methods for a full-duplex system with high-order QAM constelations and 5G low-density parity-check (LDPC) based error-correction. Our results show that an end-to-end trained neural network joint SI canceller and demodulator can lead to significant bit error rate performance gains over a range of constellation sizes and LDPC code blocklengths.

## DUIDD: Deep-Unfolded Interleaved Detection and Decoding for MIMO Wireless Systems

- **Status**: ❌
- **Reason**: MIMO IDD deep-unfolding, LDPC는 베이스라인 구성요소일 뿐 떼어낼 새 디코더 기법 없음 - 무선 응용 특이적
- **ID**: ieee:10051944
- **Type**: conference
- **Published**: 31 Oct.-2 
- **Authors**: Reinhard Wiesmayr, Chris Dick, Jakob Hoydis +1
- **PDF**: https://ieeexplore.ieee.org/document/10051944
- **Abstract**: Iterative detection and decoding (IDD) is known to achieve near-capacity performance in multi-antenna wireless systems. We propose deep-unfolded interleaved detection and decoding (DUIDD), a new paradigm that reduces the complexity of IDD while achieving even lower error rates. DUIDD interleaves the inner stages of the data detector and channel decoder, which expedites convergence and reduces complexity. Furthermore, DUIDD applies deep unfolding to automatically optimize algorithmic hyperparameters, soft-information exchange, message damping, and state forwarding. We demonstrate the efficacy of DUIDD using NVIDIA's Sionna link-level simulator in a 5G-near multi-user MIMO-OFDM wireless system with a novel low-complexity soft-input soft-output data detector, an optimized low-density parity-check decoder, and channel vectors from a commercial ray-tracer. Our results show that DUIDD outperforms classical IDD both in terms of block error rate and computational complexity.

## From fibers to satellites: lessons to learn and pitfalls to avoid when optical communications move to long distance free space

- **Status**: ❌
- **Reason**: FSO 광통신 시스템 연구, LDPC 코드 설계 예시는 표준 적용 수준 - 통신 응용 특이적, 새 기여 없음
- **ID**: ieee:10052034
- **Type**: conference
- **Published**: 31 Oct.-2 
- **Authors**: A. Vannucci, T. Foggi, A. Zahr +4
- **PDF**: https://ieeexplore.ieee.org/document/10052034
- **Abstract**: The paper summarizes the recent investigation on feasibility of adapting state-of-the-art coherent fiber-optics (FO) systems for Free Space Optical (FSO) scenarios. This investigation is critically dependent on the intertwined aspects of architecture, as well as device and propagation impairments (including the channel) appearing in the aforementioned systems. Towards this, the work identified the key system differences between the two systems. Particularly, the FSO channel model was investigated, impact of atmospheric turbulence on FSO was discussed and a channel series was generated. Subsequently, relevant FO techniques including coherent detection, wavelength division multiplexing and Time-Frequency packing (TFP) were reviewed. Another departure from FSO works was the emphasis on coherent reception; receiver architectures and diversity schemes were first investigated. The former strived to make fair comparison amongst the receivers considering the diverse nature of perturbation added, while the latter indicated gain in performance through increase of diversity order (2–4 dB gain). An immediate conclusion is a suggestion on adaptation of wavelength diversity when coherent receivers. The investigation also evaluated the capacity and outage of fast and slow fading channels with parameters motivated by the channel modelling work. The shaping gain was evaluated and an LDPC code design example was provided for FSO downlinks. Finally, TFP enabled a remarkable performance gain when applied to coherent detection schemes, but only marginal with direct detection. The paper concludes by pointing to the next steps that build on this investigation and the need to corroborate with measurements.

## Deep Learning Detector for Large-Scale MIMO Systems with Low-Resolution ADCs

- **Status**: ❌
- **Reason**: LS-MIMO deep-learning 검출기(BP와 비교), LDPC ECC 디코더 기법 아님 - 무선 검출 응용 특이적
- **ID**: ieee:10013385
- **Type**: conference
- **Published**: 31 Oct.-1 
- **Authors**: Anh T. Pham, Duc T.M. Hoang, Hieu T. Nguyen
- **PDF**: https://ieeexplore.ieee.org/document/10013385
- **Abstract**: A large-scale multiple-input multiple-out (LS-MIMO) transmission scheme with low-resolution analog-to-digital converters (ADCs) has become one of the promising techniques for 5G and future wireless networks. In this paper, we investigate the power of a deep-learning network in detecting LS-MIMO signals when the resolution of the ADCs is limited to just a few bits. We found that the performance of the deep-learning detector is sensitive to the resolution of the input signals. And thus, it desires to train a specific deep-learning detector for each level of the resolution. Furthermore, the deep-learning detector can deliver equal or better performance than the belief propagation detector. At the high level of signal-to-noise ratio, the deeper the network is, the better performance of the detector is improved. This makes the deep-learning detector a promising technique to detect large-scale MIMO signals to achieve good performance while keeping the complexity manageable.

## Performance Evaluation of Spatial Modulation Patterns in Compressive Sensing Terahertz Imaging

- **Status**: ❌
- **Reason**: 테라헤르츠 압축센싱 이미징용 마스크 설계 — 채널코딩 ECC 아님, LDPC 무관
- **ID**: ieee:9967090
- **Type**: conference
- **Published**: 30 Oct.-2 
- **Authors**: Adolphe Ndagijimana, Miguel Heredia Conde, Iñigo Ederra Urzainqui
- **PDF**: https://ieeexplore.ieee.org/document/9967090
- **Abstract**: Terahertz (THz) imaging traditionally uses pixel-to-pixel mechanical raster scanning, which is slow and limits the resolution and potential applications. Compressive Sensing Terahertz (CS-THz) imaging has the potential to solve these challenges by reducing the number of required measurements. However, there is an existing research gap between the current CS-THz implementations, which often use random binary masks without further consideration, and specialized Compressive Sensing works, which focus on RIP and coherence reduction but ignore the physics underlying THz wave propagation such as the effect of diffraction on masks patterns. This paper discusses and evaluates the use of low-coherence sensing matrices as mask patterns for CS-THz imaging. Although not previously used in THz imaging, Best Antipodal Spherical Code masks show the best image reconstruction performance among the considered alternatives. We also demonstrate the feasibility of phase-only modulation.

## A Combination of Successive Interference Cancellation and Repetition for UL-NOMA Systems

- **Status**: ❌
- **Reason**: UL-NOMA SIC+repetition, LDPC 무관 - 무선 다중접속 응용
- **ID**: ieee:10014751
- **Type**: conference
- **Published**: 30 Oct.-2 
- **Authors**: Masafumi Moriyama, Masahiro Yamazoe, Takashi Matsuda +1
- **PDF**: https://ieeexplore.ieee.org/document/10014751
- **Abstract**: As Internet of Things (IoT) develops, new radio access techniques that can effectively accommodate a massive number of devices are required to improve spectrum efficiency. Moreover, low latency communications are recently required for automation systems in IoT communications. For this reason, we have researched and developed a system which realizes both massive connection and low latency simultaneously by using both non-orthogonal multiple access (NOMA) and configured grant (CG). In our system, successive interference cancellation (SIC) is applied as a signal separation method for NOMA because of less amount of calculation. However, when signal to interference power ratio (SIR) of the superimposed signals is not sufficiently high, the probability that the SIC can correctly separate them decreases. To prevent this, we propose that repetition is combined with SIC named repetition-SIC that can improve block error probability (BLER). Although the repetition makes the probability of the collision increase, SIC can mitigate this disadvantage by removing replica from the collision signals. Moreover, in our study, the repetition signal is configured by changing redundancy version (RV). Thanks only to the RV changes in repetition signals, the gNodeB (gNB) can deal with the repetition signals as retransmission signal of hybrid automatic repeat request (HARQ). To evaluate the repetition-SIC, we conduct the computer simulation. From the results of the simulations, we confirm that the proposed method is effective to reduce BLER from $1.50\times 10^{-2}$ to $1.31\times 10^{-3}$ when 5 UEs randomly transmit signals every 833.3 μs in average.

## An Improved Genetic Algorithm-based Routing Protocol for Multimedia Data Transmission

- **Status**: ❌
- **Reason**: 멀티미디어 라우팅 프로토콜용 유전 알고리즘 — LDPC/ECC 무관, 떼어낼 기법 없음
- **ID**: ieee:10014845
- **Type**: conference
- **Published**: 30 Oct.-2 
- **Authors**: Fozia Hanif, Rehan Shams, Samia Masood Awan +1
- **PDF**: https://ieeexplore.ieee.org/document/10014845
- **Abstract**: The purpose of this study is to obtain an improved and optimized network with minimum end-to-end delay and improved throughput by using the Genetic Algorithm (GA) for multimedia communication. The proposed study also increases the Quality of Service (QoS) with the consideration of the optimal path. Nowadays, the transformation of multimedia information is essential for the users however, many factors affect the transmission of multimedia communication, such as quality of service, end-to-end delay, energy efficiency, and many more. This paper is intended to provide an efficient algorithm for multimedia communication that overcomes the factors mentioned above. For validating our proposed methodology simulation will be carried out for multimedia traffic and video streamed network traffic using OPNET Simulator. Comparison with existing algorithms will prove that the suggested algorithm outperforms them and provides better efficiency.

## Performance Evaluation of 5G in VHF Band for Super-large Coverage Communication Systems

- **Status**: ❌
- **Reason**: VHF 대역 5G-NR 전송성능 평가, LDPC는 부수 언급, 떼어낼 ECC 기법 없음
- **ID**: ieee:10051012
- **Type**: conference
- **Published**: 28-30 Nov.
- **Authors**: Hiroshi Harada, Shota Mori, Keiichi Mizutani
- **PDF**: https://ieeexplore.ieee.org/document/10051012
- **Abstract**: In the 6th-generation mobile communication (6G) system, massive simultaneous connections are required, including all “things” such as sensors, meters, and monitors, in addition to ordinary users. To realize this large number of simultaneous connections, it is necessary to provide stable communication over a wide area. In this study, we propose the utilization of the VHF band (200 MHz) for 5G new radio (NR), which is even lower than the frequency of 450-6000 MHz, defined as the frequency range 1 (FR1) in 3GPP. Since the VHF band has a longer wavelength than the microwave band in which the 5G-NR currently operates, the transmission distance of the signal from the base station increases. However, delay waves of over 20 μs were received in rural areas. These waves cause an inter-symbol interference and deteriorate the transmission performance. Therefore, the parameters of the 5G-NR may be adapted to the radio wave propagation environment in the VHF band. Since 5G-NR uses a strong error-correcting code such as low-density parity-check (LDPC) code and the frame structure can correspond to various radio wave propagation path characteristics, we may not need to change any parameters. Herein, the transmission performance of 5G-NR in the VHF band is evaluated via computer simulations, and it is shown that the required block error rate (BLER) can be achieved even when QPSK, 16QAM, and 64QAM are utilized without changing the parameters of 5G-NR and that the transmission range can be achieved to 20 km.

## Construction of Polar Code using Code Spectrum

- **Status**: ❌
- **Reason**: Polar code 구성(code spectrum) — LDPC 아니며 떼어낼 LDPC 기법 없음
- **ID**: ieee:10062591
- **Type**: conference
- **Published**: 25-27 Nov.
- **Authors**: Yongsong Wang, Yinsheng Liu, Rong Li
- **PDF**: https://ieeexplore.ieee.org/document/10062591
- **Abstract**: The construction of Polar code algorithm using reliability can be proved to be optimal under successive cancellation (SC) decoding algorithm, but for successive cancellation list (SCL) decoding algorithm, the construction method using reliability alone is not optimal. Based on the existing reliability construction method, this paper proposes a Polar code construction scheme which takes reliability and code spectrum into consideration, designs a new coding rule, and reduces the bit error rate (BER) without significantly increasing the coding complexity. Simulation results show that the proposed algorithm outperforms the original Polar code construction algorithm in SCL decoding.

## Learning Scheme for Adaptive Modulation and Coding in 5G New Radio

- **Status**: ❌
- **Reason**: 5G AMC용 KNN 변조·코딩 선택, LDPC 디코더/구성 이식 기법 없음
- **ID**: ieee:10067597
- **Type**: conference
- **Published**: 23-25 Nov.
- **Authors**: Li-Sheng Chen, Chih-Hsiang Ho, Cheng-Chang Chen +1
- **PDF**: https://ieeexplore.ieee.org/document/10067597
- **Abstract**: Adaptive modulation and coding (AMC) is a link adaptation technique based on the physical layer of fifth-generation (5G) new radio (NR) systems. Studies on AMC and AMC improvement techniques have primarily focused on adding a feedback and retransmission mechanism or on improving channel prediction algorithms, including pilot signal insertion algorithms. A common improvement solution for AMC in machine learning is the K nearest neighbor (KNN)-based modulation and coding scheme selection method. However, to use this method, channel information must be complete and accurate. We adopted a supervised learning–based AMC scheme that considers the effects of channel and noise bias on AMC performance and explored the effects of the K value, distance metrics, and eigenvectors on scheme performance. The K value associated with the highest average classification accuracy rate was determined and verified through ten-fold cross-validation, and the channel quality indicator estimation errors were analyzed. We compared the classification performance of the scheme by using training samples with channel and noise values and those with estimated channel and noise values. The results indicated that the classification accuracy was higher when training samples with estimated values were adopted. In addition, the KNN-based AMC scheme outperformed genetic algorithms regarding bit error rates and spectral efficiency.

## Latency Components and Analysis in 5G New Radio

- **Status**: ❌
- **Reason**: 5G NR latency 분석 리뷰 — LDPC ECC 기법 없음, 무선 응용 특이적
- **ID**: ieee:9965239
- **Type**: conference
- **Published**: 22-24 Nov.
- **Authors**: Madhavsingh Indoonundon, Tulsi Pawan Fowdur
- **PDF**: https://ieeexplore.ieee.org/document/9965239
- **Abstract**: Low latency communications are a crucial enabling factor of several 5G New Radio (NR) use cases. In fact, the support of ultra-reliable low-latency communications (URLLC) in 5G NR opens doors to a panoply of wireless applications such as robotics, autonomous driving, telesurgery, virtual reality and telepresence. To achieve URLLC, the long-term evolution of network architecture and key enabling communication technologies are necessary. Since its initial conception, the design of 5G NR has been made with the objective of drastically minimizing the latency at various segments (such as the air interface, fronthaul, backhaul, edge, core and transport) in its end-to-end network. In this paper, a detailed analysis of the concept of latency in the 5G NR communication system in terms of the end-to-end network, user plane and control plane latency is presented. Moreover, the different enabling technologies to achieve URLLC are also reviewed. Challenges that remain to be addressed and gaps in current research are also identified.

## SCMA-LDPC coded communication system

- **Status**: ❌
- **Reason**: SCMA+LDPC 결합 통신 시스템 — LDPC는 베이스라인 부수 언급, 떼어낼 새 ECC 기법 없음(무선 NOMA 응용)
- **ID**: ieee:10003016
- **Type**: conference
- **Published**: 17-19 Nov.
- **Authors**: Dmitriy Pokamestov, Artem Shinkevich, Yakov Kryukov +3
- **PDF**: https://ieeexplore.ieee.org/document/10003016
- **Abstract**: Non-orthogonal multiple access (NOMA) methods are a promising technology that can be the basis of the next generation communication networks and ensure their high throughput. One of the most effective NOMA methods is sparse code multiple access (SCMA). SCMA allows providing better noise immunity and connecting a larger number of subscribers compared to classical solutions used in modern networks. Together with modulation and multiple access, it is reasonable to consider noise-resistant coding procedures that equally affect communication characteristics. One of the most efficient types of noise-resistant codes is low density parity check (LDPC) codes. Now LDPC is used in a number of communication systems, including 5G NR. In this paper, we propose the concept of a communication system with the joint use of LDPC and SCMA. We introduce a sequence of algorithms for the generation and processing of signals. The dependencies of bit error rate (BER) performance on SNR are given: they show the efficiency of the proposed solutions and the ability of the considered communication system to work in various conditions. The results obtained can be used to form a modulation and code scheme (MCS) table for next-generation communication systems.

## Study on Channel Coding for Future Railway Mobile Communication Systems

- **Status**: ❌
- **Reason**: 5G NR 표준 QC-LDPC를 철도통신에 적용해 EXIT 평가; 표준 부호 단순 재사용, 새 디코더/구성 기여 없음
- **ID**: ieee:10009038
- **Type**: conference
- **Published**: 14-16 Nov.
- **Authors**: Falindio Muhammad Riyadi, Khoirul Anwar, Nachwan Mufti Adriansyah
- **PDF**: https://ieeexplore.ieee.org/document/10009038
- **Abstract**: This paper studies 5G channel coding, Quasi-Cyclic Low Density Parity Check (QC-LDPC) codes, which are expected to be used in future railway mobile communication systems (FRMCS), of which the standard is being specified by Union Internationale des Chemins de fer (UIC) in Europe. The QC-LDPC codes, used by the 5G New Radio (NR), has an ability to adapt to the channel dynamics due to the rateless capability of the codes. Evaluation is performed using Extrinsic Information Transfer (EXIT) chart based on an equivalent erasure probability derived from the simulated FRMCS under Indonesia FRMCS channel model at speed up to 500 km/h. We found that the rateless characteristic of QC-LDPC codes is useful for FRMCS to reduce the error, especially at low signal-to-noise power ratio (SNR) below 15 dB. Results of this paper are expected to provide contributions either on software or hardware for the development of FRMCS high speed train.

## Study on Simple Channel Coding Scheme for Molecular Communications

- **Status**: ❌
- **Reason**: 분자통신용 화학반응 기반 LDPC; 양자가 아니라 화학반응 기판 특이적, 전자식 디코더로 이식할 새 기법 없음(애매하나 box-plus 모사 외 기여 빈약)
- **ID**: ieee:10010169
- **Type**: conference
- **Published**: 14-16 Nov.
- **Authors**: Khoirul Anwar, Nadaina Salsabila, Muhammad Rizky Satya Bhaskara +1
- **PDF**: https://ieeexplore.ieee.org/document/10010169
- **Abstract**: This paper studies two channel coding schemes for molecular communications, i.e., (i) repetition codes and (ii) low density parity check (LDPC) codes based on chemical reactions. We investigate the number of molecules to make the error correction works. We also derive a chemical reaction principle to resemble a function of box-plus operation as the in electronic case. We perform a series of computer simulations to obtain the numerical results. We found that minimum number of molecules is about 500 to make the decoding works, while the chemical reactions resembling box-plus operation is a promising principle for further development. The larger number of molecules improves the performances significantly.

## Massive MIMO Enabled Unsourced Random Access Through LDPC Coding and Random Spreading

- **Status**: ❌
- **Reason**: Massive MIMO unsourced random access — LDPC+random spreading 시스템 설계, 표준 SPA 사용, 떼어낼 새 ECC 기법 없음
- **ID**: ieee:10073330
- **Type**: conference
- **Published**: 11-14 Nov.
- **Authors**: Yiwei Su, Jianping Zheng, Zijie Liang +1
- **PDF**: https://ieeexplore.ieee.org/document/10073330
- **Abstract**: In this paper, we propose a novel massive multiple-input multiple-output enabled unsourced random access scheme through low-density parity-check (LDPC) encoding and random spreading. In the proposed scheme, the pilot is modulated by spreading sequence and transmitted over the first time slot, and data are transmitted over other time slots by shorter spreading sequence, a fraction of the sequence in the first time slot, after LDPC encoding. At receiver, by utilizing received signals in pilot time slot, the covariance-based maximum likelihood detection is first used for active codeword detection and then the multiple measurement vector approximate message passing (AMP) for channel estimation. Next, data detection by generalized AMP algorithm and channel decoding by sum-product algorithm are performed subsequently. Moreover, to improve performance, iterative successive interference cancellation strategy is also employed. Finally, computer simulations are given to demonstrate the performance of the proposed scheme.

## Design of Hybrid Encryption for Multi-relay Physical-layer Network Coding System

- **Status**: ❌
- **Reason**: PNC 시스템 AES/RSA 하이브리드 암호화 — LDPC는 부수 언급, 떼어낼 ECC 기법 없음
- **ID**: ieee:10073240
- **Type**: conference
- **Published**: 11-14 Nov.
- **Authors**: Yanru Yang, Meng Tang, Haihua Li +3
- **PDF**: https://ieeexplore.ieee.org/document/10073240
- **Abstract**: This paper proposes a hybrid encryption scheme for multi-relay (MR) physical-layer network coding (PNC). Based on the three-relay (3R) bidirectional communication model, first, we discuss the throughput performance of the PNC compared with the traditional scheme (TS) and network coding (NC) system. Through the analysis of transmission efficiency, the superior throughput of the PNC system is demonstrated. Then, to further improve the security of the communication system, we give a scheme of advanced encryption standard (AES) and Rivest-Shamir-Adleman (RSA) hybrid encryption, namely AR hybrid encryption. Finally, we embed the AR hybrid encryption into the multi-relay PNC communication system. At relay nodes of the AR-PNC system, we focus on solving the problem of signal mapping. In the meantime, to reduce the performance loss caused by the increase of relay nodes, we exploit Low-Density Parity-Check (LDPC) code to enhance the decoding accuracy. The experimental results and security analysis show that the proposed scheme can boost the system throughput and transmission dependability and stronger the security of the communication system.

## Joint Receiver Design with Natural Redundancy

- **Status**: ❌
- **Reason**: 딥러닝 기반 NN 수신기(symbol timing+demodulation), 자연 잉여도 활용 — LDPC ECC 아님, 떼어낼 디코더 기법 없음
- **ID**: ieee:10073367
- **Type**: conference
- **Published**: 11-14 Nov.
- **Authors**: Zhaorui Zhu, Hongyi Yu, Zhenyu Wang
- **PDF**: https://ieeexplore.ieee.org/document/10073367
- **Abstract**: A high-speed information transmission system demands a more powerful communication receiver. In this paper, we integrate deep learning algorithms into constructing waveform level receiver, which is capable of harnessing natural redundancy (NR) in raw message sources. Owing to end-to-end learning paradigm of neural network (NN), the proposed NN receiver can accomplish joint symbol timing synchronization and demodulation based on oversampled waveform sequences directly. The prevalent Transformer structures, suitable for excavating sequential correlation of complex sources and waveform sequences, are considered as the backbone of NN receivers. Under the cases of clean label and noisy label, we conceive two novel training algorithms and interpret their principles in theory. The clean label bits are accessible from original source encoding schemes, while noisy label bits are available from the decision results of canonical receivers with independently noised waveform sequences. When noisy labels possess sufficiently small error rates, optimized NN receiver is competitive with that adopting the accurate labels. As for natural language text sources, simulation results show that the proposed NN receivers' performances are superior to the classical receivers without a priori knowledge, especially when high spectral efficiency modulation schemes are encountered and random noise is significant.

## On the Construction of Polar Codes in Two-User Downlink NOMA with Power Allocation and Constellation-Rotation

- **Status**: ❌
- **Reason**: NOMA용 폴라코드 구성 + 전력할당 — LDPC는 베이스라인 비교 대상일 뿐
- **ID**: ieee:10073253
- **Type**: conference
- **Published**: 11-14 Nov.
- **Authors**: Benjamin K. Ng, Chan-Tong Lam
- **PDF**: https://ieeexplore.ieee.org/document/10073253
- **Abstract**: We consider the joint construction of polar codes and power allocation based on rotated QPSK constellation in the two-user downlink non-orthogonal multiple access (NOMA) system. Our work is suitable for IoT-like networks where lightweight devices employ simple constellations with low data rate traffic, and the traditional coding performance analysis assuming Gaussian inputs and infinite blocklength may become less accurate. With the goal of achieving fairness and minimizing the maximum block-error-rate (BLER) among the NOMA users, the construction of polar codes, which takes into consideration the BLER estimated by the Gaussian-approximation-based density evolution (GA-DE) method, is jointly determined with the constellation-rotation angle and the power allocation over the NOMA users. Simulations verify that the proposed approach yields generally comparable BLER performance as the LDPC codes over the range of SNR considered while having shorter blocklength.

## Deep Learning-Based Joint Modulation and Coding Scheme Recognition for 5G New Radio Protocols

- **Status**: ❌
- **Reason**: 5G NR LDPC 변조/코딩 스킴 인식(CNN) — ECC 디코더/구성이 아닌 blind detection, 이식 기법 없음
- **ID**: ieee:10072789
- **Type**: conference
- **Published**: 11-14 Nov.
- **Authors**: Xiang Chen, Xinyao Wang, Hanyu Zhao +1
- **PDF**: https://ieeexplore.ieee.org/document/10072789
- **Abstract**: Blind detection of signals is a crucial technique in the 5G/B5G wireless communication systems, especially for the cognitive spectrum radio network, where the parameters of the transmit signals working on the free spectrum can not be known by the receiver. Following the 5G New Radio (NR) protocols, we propose a joint modulation and coding scheme (M-CS) recognition framework based on the supervised learning architecture and the given candidate set of the LDPC encoder. Specifically, the framework is composed of two cascaded modules. Firstly, the type of digital modulation according to the SG NR protocols is recognized blindly based on the proposed Res-Inception convolutional neural network (RICNN). Then, the low-density parity check (LDPC) coding scheme implemented under various bitrates is identified by exhaustively searching the validation candidate to maximize the corresponding average log-likelihood ratio (ALLR). Numerical results show the effectiveness of our proposed blind recognition framework, especially for the practical 5G NR protocols. Moreover, it is demonstrated that our proposed method can guarantee the robustness of the recognition under various channel fading model scenarios.

## On the improvement of McEliece cryptosystem based on LDPC codes

- **Status**: ❌
- **Reason**: QC-LDPC 기반 McEliece 암호 개선 — 보안/암호 응용, 기존 soft-decision 디코더 재사용, 새 ECC 기여 없음
- **ID**: ieee:10016999
- **Type**: conference
- **Published**: 11-13 Nov.
- **Authors**: A.D. Rudzyanskiy, F.I. Ivanov
- **PDF**: https://ieeexplore.ieee.org/document/10016999
- **Abstract**: In this paper an improvement of the McEliece cryptosystem based on QC-LDPC codes is considered. The key idea of the improvement is to use soft-decision decoding algorithm of LDPC codes in decryption step. This allows to reduce a public- key size in comparison with the McEliece cryptosystem based on QC-LDPC codes decoded by hard-decision bit-flipping decoder. In addition, the analysis of the dependence between key size and security in bits for the proposed cryptosystem was conducted.

## Polar Codes with Dynamic Frozen Bits for Gaussian Multiple Access Channel

- **Status**: ❌
- **Reason**: Polar 코드 dynamic frozen bit 설계 for MAC — LDPC가 아니라 polar 코드, 무관
- **ID**: ieee:10016939
- **Type**: conference
- **Published**: 11-13 Nov.
- **Authors**: Evgeny Marshakov, Anna Fominykh, Alexey Frolov
- **PDF**: https://ieeexplore.ieee.org/document/10016939
- **Abstract**: Machine-type communications with a large number of autonomous devices, small packets, and a lack of centralized coordination are the future of cellular systems. This scenario is typically called massive machine-type communications (mMTC). There are several candidate solutions for this problem that are proposed by the 3GPP standartization committee. In this paper, we continue the investigation of the model proposed by Marshakov et al. in [1]. We propose a method for polar code design for multiple access channels (MAC) by means of dynamic frozen bits. We present an algorithm for polar code design by optimizing the search of dynamic frozen positions based on the properties of the joint successive cancellation decoding in combination with the list decoding method. Series of experiments for single and multi-user cases were conducted and it was shown that obtained configuration of dynamic frozen bits increases the practical performance of polar codes in a multi-user scenario.

## Authentication System Based On Ldpc And Sha-3

- **Status**: ❌
- **Reason**: LDPC+SHA3 인증 시스템(보안 응용). 표준 Min-Sum 그대로 사용, 새 디코더/코드설계 기여 없음.
- **ID**: ieee:9987322
- **Type**: conference
- **Published**: 10-12 Nov.
- **Authors**: Sheetal B V, A Rajagopal
- **PDF**: https://ieeexplore.ieee.org/document/9987322
- **Abstract**: Security is one of the most demanding parameters in today’s world, in order to ensure the integrity of the information. In order to authenticate the information and maintain its integrity, this paper describes a design to authenticate a message using Low Density Parity Check(LDPC) codes and Secure Hash Algorithm 3(SHA3). As LDPC codes are reliable and highly efficient information transfer over noisy channels, the integrity of the information can be ensured. In order to decrease the implementation complexity, the decoding is done using the Min-Sum Algorithm which provides an error corrected code vector. For authentication, the new hash value produced by employing SHA3 on the error corrected code vector is compared with the stored hash value. The SHA3 produces a unique hash value for a given input, the security of this scheme is high. Here a hash value of length 224-bit is generated which is used for authentication. The introduced design is implemented and the desired simulation results are obtained using MatLAB.

## Performances Analysis of Turbo Codes, LDPC Codes and Polar Codes using AWGN channel with and without Inter Symbol Interference

- **Status**: ❌
- **Reason**: Turbo/LDPC/Polar 성능 비교 분석(BER vs SNR). 표준 부호 비교일 뿐 새 디코더/구성/HW 기여 없음.
- **ID**: ieee:10010114
- **Type**: conference
- **Published**: 10-11 Nov.
- **Authors**: Adriana-Maria Cuc, Florin Lucian Morgoş, Cristian Grava
- **PDF**: https://ieeexplore.ieee.org/document/10010114
- **Abstract**: The purpose of this paper is to analyse the performances of Turbo codes, LDPC (Low Density Parity Check) codes and Polar codes, over an AWGN (Additive White Gaussian Noise) channel with and without ISI (Inter Symbol Interference). In case of using an AWGN channel without ISI, the channel impulse response was considered to be unitary. In contrast, in the case of an AWGN channel in the presence of ISI, it was required to apply equalisation. In this respect, it was used Zero Forcing equalizer to remove the ISI consequences. As performance indicator the BER (Bit Error Rate) was considered for a given SNR (Signal to noise Ratio), using BPSK modulation (Binary Phase Shift Keying).

## Stabilizer Inactivation for Message-Passing Decoding of Quantum LDPC Codes

- **Status**: ❌
- **Reason**: 양자 LDPC stabilizer-inactivation 후처리, 스태빌라이저 의존으로 고전 바이너리 LDPC 이식 불가
- **ID**: ieee:9965902
- **Type**: conference
- **Published**: 1-9 Nov. 2
- **Authors**: Julien Du Crest, Mehdi Mhalla, Valentin Savin
- **PDF**: https://ieeexplore.ieee.org/document/9965902
- **Abstract**: We propose a post-processing method for message-passing (MP) decoding of CSS quantum LDPC codes, called stabilizer-inactivation (SI). It relies on inactivating a set of qubits, supporting a check in the dual code, and then running the MP decoding again. This allows MP decoding to converge outside the inactivated set of qubits, while the error on these is determined by solving a small, constant size, linear system. Compared to the state of the art post-processing method based on ordered statistics decoding (OSD), we show through numerical simulations that MP-SI outperforms MP-OSD for different quantum LDPC code constructions, different MP decoding algorithms, and different MP scheduling strategies, while having a significantly reduced complexity.

## Belief Propagation with Quantum Messages for Symmetric Classical-Quantum Channels

- **Status**: ❌
- **Reason**: 양자 메시지 BP(BPQM)은 양자 채널 전용 측정 기반, 고전 바이너리 LDPC로 이식 불가
- **ID**: ieee:9965841
- **Type**: conference
- **Published**: 1-9 Nov. 2
- **Authors**: S. Brandsen, Avijit Mandal, Henry D. Pfister
- **PDF**: https://ieeexplore.ieee.org/document/9965841
- **Abstract**: Belief propagation (BP) is a classical algorithm that approximates the marginal distribution associated with a factor graph by passing messages between adjacent nodes in the graph. It gained popularity in the 1990’s as a powerful decoding algorithm for LDPC codes. In 2016, Renes introduced a belief propagation with quantum messages (BPQM) and described how it could be used to decode classical codes defined by tree factor graphs that are sent over the classical-quantum pure-state channel. In this work, we propose an extension of BPQM to general binary-input symmetric classical-quantum (BSCQ) channels based on the implementation of a symmetric "paired measurement". While this new paired-measurement BPQM (PMBPQM) approach is suboptimal in general, it provides a concrete BPQM decoder that can be implemented with local operations. Finally, we demonstrate that density evolution can be used to analyze the performance of PMBPQM on tree factor graphs. As an application, we compute noise thresholds of some LDPC codes with BPQM decoding for a class of BSCQ channels.
