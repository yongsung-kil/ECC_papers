# IEEE Xplore — 2010-08


## Joint Channel and Network Coding for Cooperative Diversity in a Shared-Relay Environment

- **Status**: ❌
- **Reason**: 공유 릴레이 협력 다이버시티 조인트 채널/네트워크코딩 + sliding-window LLR 메시지패싱, 무선 릴레이 응용 특이적이고 LDPC 비의존, 떼어낼 NAND 기법 없음
- **ID**: ieee:5494766
- **Type**: journal
- **Published**: August 201
- **Authors**: Xiaoyan Xu, Mark F. Flanagan, Norbert Goertz +1
- **PDF**: https://ieeexplore.ieee.org/document/5494766
- **Abstract**: In this paper we propose a cooperative diversity scheme for the communication model of two sources sharing a single relay. The scheme uses algebraic code superposition relaying in the multiple access fading channel to create spatial diversity under the constraint of limited communications resources. We also describe in detail a novel computationally efficient message passing algorithm at the destination's decoder which extracts the substantial spatial diversity contained in the code superposition and signal superposition. The decoder is based on a sliding window structure where certain a posteriori LLRs are retained to form a priori LLRs for the next decoding. We show that despite the simplicity of the proposed scheme, diversity gains are efficiently leveraged by the simple combination of channel coding at the sources and network coding at the relay.

## Asymptotic Performance Analysis of Coded BLAST Architectures with Statistical Rate and Power Allocations

- **Status**: ❌
- **Reason**: BLAST MIMO 공간시간 부호의 rate/power allocation 용량분석. LDPC ECC와 무관, 떼어낼 디코더/HW 기법 없음
- **ID**: ieee:5510785
- **Type**: journal
- **Published**: August 201
- **Authors**: Hyo-Jin Lee, Dong-Min Shin, Kyeongcheol Yang
- **PDF**: https://ieeexplore.ieee.org/document/5510785
- **Abstract**: In this paper we first analyze some mathematical properties of ergodic capacity and outage capacity functions of the layers in Bell labs layered space-time (BLAST) architectures employing successive decoding and interference cancellation. We then present statistical rate allocation and power allocation methods that optimize the asymptotic performance of BLAST architectures. Since the methods are developed by using ergodic capacity and outage capacity functions of the layers, the allocated rates and powers depend only on a given channel statistic. Finally, we prove that the rate allocation yields a better asymptotic performance than the power allocation. Numerical results show that BLAST architectures with the rate and power allocation perform better by 4 dB and 3 dB, respectively, than a BLAST architecture with the same rate and power in all layers.

## On the Dynamics of Analog Min-Sum Iterative Decoders: An Analytical Approach

- **Status**: ✅
- **Reason**: 아날로그 min-sum 디코더 동역학·error floor·absorption set 분석은 LDPC 디코더 기법으로 이식 가능(C)
- **ID**: ieee:5555878
- **Type**: journal
- **Published**: August 201
- **Authors**: Saied Hemati, Abbas Yongaçoglu
- **PDF**: https://ieeexplore.ieee.org/document/5555878
- **Abstract**: In this paper, we show an ideal analog min-sum decoder, in the log-likelihood ratio domain, can be considered as a piecewise linear system. Many theoretical aspects of these decoders, thus, can be studied analytically. It is also shown that the dynamic equations can become singular for codes with cycles. When it is non-singular, the corresponding dynamic equations can be solved analytically to derive outputs of the decoder. We study the relationship between singularity and error floor and prove that absorption sets with degree two check nodes are singular graphs and under specific conditions the dynamic equations of an analog min-sum decoder can be reduced to that of an absorption set. The proposed approach paves the way for further analytical analysis on the dynamics of analog min-sum decoders and error floor in low-density parity-check codes.

## Nested Polar Codes for Wiretap and Relay Channels

- **Status**: ❌
- **Reason**: wiretap/relay 보안용 nested polar 부호로 비-LDPC + 보안 응용, 바이너리 LDPC BP 이식 기법 없음 제외
- **ID**: ieee:5545658
- **Type**: journal
- **Published**: August 201
- **Authors**: Mattias Andersson, Vishwambhar Rathi, Ragnar Thobaben +2
- **PDF**: https://ieeexplore.ieee.org/document/5545658
- **Abstract**: We show that polar codes asymptotically achieve the whole capacity-equivocation region for the wiretap channel when the wiretapper's channel is degraded with respect to the main channel, and the weak secrecy notion is used. Our coding scheme also achieves the capacity of the physically degraded receiver-orthogonal relay channel. We show simulation results for moderate block length for the binary erasure wiretap channel, comparing polar codes and two edge type LDPC codes.

## Trapping Sets of Fountain Codes

- **Status**: ❌
- **Reason**: Fountain 코드의 trapping set 분석으로 비-LDPC 부호이며 떼어낼 바이너리 LDPC BP 기법 없음(fountain/erasure 제외)
- **ID**: ieee:5545659
- **Type**: journal
- **Published**: August 201
- **Authors**: Vivian Lucia Orozco, Shahram Yousefi
- **PDF**: https://ieeexplore.ieee.org/document/5545659
- **Abstract**: The remarkable results of Fountain codes over the binary erasure channel (BEC) have motivated research on their practical implementation over noisy channels. Trapping sets are a phenomenon of great practical importance for certain graph codes on noisy channels. Although trapping sets have been extensively studied for low-density parity-check (LDPC) codes, to the best of our knowledge they have never been fully explored for Fountain codes. In this letter, we demonstrate that trapping sets are damaging to the realized rate and decoding cost of Fountain codes. Furthermore, we show that through trapping set detection we may combat these negative effects.

## Approximate Performance Analysis for Linear Codes in Superposition Schemes over Gaussian Broadcast Channels

- **Status**: ❌
- **Reason**: 가우시안 방송채널 superposition 선형부호 성능분석(union bound)으로 순수 이론/응용 특이적, 떼어낼 디코더·HW·구성 기법 없음
- **ID**: ieee:5555872
- **Type**: journal
- **Published**: August 201
- **Authors**: Uttam Bhat, Dario Fertonani, Tolga M. Duman
- **PDF**: https://ieeexplore.ieee.org/document/5555872
- **Abstract**: Unequal error-protection schemes obtained by means of two-level superposition coding are considered. Their performance over Gaussian broadcast channels (GBCs) is investigated with optimal maximum-likelihood decoding as well as with a suboptimal decoding strategy based on interference cancellation. We focus on GBCs without fading and, assuming that linear codes are used, we evaluate, for both decoding strategies, analytical approximations of the word-error rate based on a suitable application of the union bound. As in the case of turbo codes and turbo-coded modulations in schemes without superposition, the derivation of the approximations exploits the concept of uniform interleaving. The analytical expressions obtained are in excellent agreement with the simulation results, and thus provide a useful tool for analysis and design of practical superposition-coding schemes. Unlike the existing design tools, which rely on the assumption of infinite-length superposition codes, the proposed approach allows us to study the effectiveness of finite-length coding schemes with known distance spectrum.

## Optimal Routing for Decode-Forward in Cooperative Wireless Networks

- **Status**: ❌
- **Reason**: 협력 무선 네트워크 라우팅 논문, LDPC는 BER 비교용 부수 언급일 뿐 떼어낼 ECC 기법 없음
- **ID**: ieee:5555886
- **Type**: journal
- **Published**: August 201
- **Authors**: Lawrence Ong, Mehul Motani
- **PDF**: https://ieeexplore.ieee.org/document/5555886
- **Abstract**: We investigate routing in cooperative multiple-terminal wireless networks in which the nodes can collaborate with each other in data transmission. First, we motivate cooperation by showing that decode-forward, an information-theoretic cooperative coding strategy, achieves rates significantly higher than those achievable by the conventional multi-hop routing, a point-to-point non-cooperative coding strategy. We then construct an algorithm to find optimal (rate-maximizing) routes for decode-forward. We show that the algorithm is able to find shortest optimal routes and is optimal in fading channels. However, the algorithm runs in factorial time in the worst case. So, we propose a near-optimal heuristic algorithm that runs in polynomial time. The heuristic algorithm always outputs optimal routes when the nodes transmit independent codewords, and outputs optimal routes with high probability when the nodes transmit arbitrarily correlated codewords. Lastly, we implement decode-forward using low-density parity-check codes to compare the bit error rate performance of different routes.

## LDPC-Coded OFDM for Heterogeneous Access Optical Networks

- **Status**: ✅
- **Reason**: rate-adaptive LDPC를 modified PEG로 설계하는 부분은 코드설계 기법으로 이식 가능성 있어 애매하므로 살림(E)
- **ID**: ieee:5491028
- **Type**: journal
- **Published**: Aug. 2010
- **Authors**: Ivan B. Djordjevic, Hussam G. Batshon
- **PDF**: https://ieeexplore.ieee.org/document/5491028
- **Abstract**: In this paper, we propose a heterogeneous optical access networking scenario, in which communication links between source and destination nodes are heterogeneous, composed of free-space optical, plastic optical fiber (POF), and indoor infrared (IR) links. To deal with bandwidth limitations of POF and IR links, a power-variable rate-adaptive low-density parity-check (LDPC)-coded orthogonal frequency division multiplexing (OFDM) scheme is used, while to deal with atmospheric turbulence, the spatial diversity is used. The rate-adaptive LDPC codes are designed using a modified progressive edge-growth (MPEG) algorithm. We show that with the proposed heterogeneous communication systems, we can deliver a high-speed optical signal (40 Gb/s and beyond) to an end-user.

## A new DC-free multimode code design with error correction capability for optical storage systems

- **Status**: ❌
- **Reason**: 광학저장 DC-free RLL 다중모드 변조부호+터보등화; LDPC는 베이스라인, 떼어낼 신규 디코더/HW/구성 없음
- **ID**: ieee:5606293
- **Type**: journal
- **Published**: Aug. 2010
- **Authors**: Jun Lee
- **PDF**: https://ieeexplore.ieee.org/document/5606293
- **Abstract**: DC-free run-length limited codes have been the cornerstone of all three generations of optical recording, CD, DVD and BD. Research into efficient coding methods is paramount for the upcoming fourth generation. A Multimode coding technique is an efficient coding method that has been reported in the literatures. Under multimode coding rules, a user word is translated into a plurality of possible candidate words, and among the candidate words the encoder selects the codeword with the least low-frequency spectral content. In our paper, we will present a new coding technique for constructing error correcting high-rate DC-free multimode code using a low-density parity-check (LDPC) code for future high-density optical recording. The scheme achieves reliable DC-suppression and obtains considerable bit error rate (BER) performance gain through the iterative decoding (or turbo equalization) with the concatenated detector.

## Performance Bounds for Erasure, List, and Decision Feedback Schemes With Linear Block Codes

- **Status**: ❌
- **Reason**: erasure/list/decision-feedback의 Gallager-type 성능 bound로 순수 이론, 디코더/HW/구성으로 안 이어짐
- **ID**: ieee:5508626
- **Type**: journal
- **Published**: Aug. 2010
- **Authors**: Eran Hof, Igal Sason, Shlomo Shamai
- **PDF**: https://ieeexplore.ieee.org/document/5508626
- **Abstract**: A message independence property and some new performance upper bounds are derived in this work for erasure, list, and decision-feedback schemes with linear block codes transmitted over memoryless symmetric channels. Similar to the classical work of Forney, this work is focused on the derivation of some Gallager-type bounds on the achievable tradeoffs for these coding schemes, where the main novelty is the suitability of the bounds for both random and structured linear block codes (or code ensembles). The bounds are applicable to finite-length codes and to the asymptotic case of infinite block length, and they are applied to low-density parity-check code ensembles.

## An Energy Efficient Layered Decoding Architecture for LDPC Decoder

- **Status**: ✅
- **Reason**: layered 디코딩 메모리-bypassing 에너지효율 아키텍처+최적 디코딩순서, 이식 가능 HW 기법(D)
- **ID**: ieee:5229117
- **Type**: journal
- **Published**: Aug. 2010
- **Authors**: Jie Jin, Chi-ying Tsui
- **PDF**: https://ieeexplore.ieee.org/document/5229117
- **Abstract**: Low-density parity-check (LDPC) decoder requires large amount of memory access which leads to high energy consumption. To reduce the energy consumption of the LDPC decoder, memory-bypassing scheme has been proposed for the layered decoding architecture which reduces the amount of access to the memory storing the soft posterior reliability values. In this work, we present a scheme that achieves the optimal reduction of memory access for the memory bypassing scheme. The amount of achievable memory bypassing depends on the decoding order of the layers. We formulate the problem of finding the optimal decoding order and propose algorithm to obtain the optimal solution. We also present the corresponding architecture which combines some of memory components and results in reduction of memory area. The proposed decoder was implemented in TSMC 0.18 μm CMOS process. Experimental results show that for a LDPC decoder targeting IEEE 802.11 n specification, the amount of memory access values can be reduced by 12.9-19.3% compared with the state-of-the-art design. At the same time, 95.6%-100% hardware utilization rate is achieved.

## Iterative Polar Quantization-Based Modulation to Achieve Channel Capacity in Ultrahigh-Speed Optical Communication Systems

- **Status**: ❌
- **Reason**: 광통신용 IPQ 코디드모듈레이션, 표준 구조적 LDPC를 그대로 사용하고 새 LDPC 기여 없음
- **ID**: ieee:5482065
- **Type**: journal
- **Published**: Aug. 2010
- **Authors**: Hussam G. Batshon, Ivan B. Djordjevic, Lei Xu +1
- **PDF**: https://ieeexplore.ieee.org/document/5482065
- **Abstract**: In this paper, we propose a nonuniform coded-modulation format based on iterative polar quantization (IPQ) as a scheme to enable achieving channel capacity in ultrahigh-speed optical communication systems. The proposed modulation format is coded with structured low-density parity-check (LDPC) codes optimized for Gaussian channels and, in combination with polarization-multiplexing, can achieve 800 Gb/s per wavelength aggregate rate and beyond utilizing the currently available components operating at 50 GS/s. Using coded IPQ, we show that we can achieve capacity for signal-to-noise ratios (SNRs) of up to 25 dB and increase the total propagation distance over optical transmission systems by 275 km over coded star-quadrature amplitude modulation (QAM).

## Hybrid ARQ with Partial Retransmissions and LDPC codes and its Impact on TCP

- **Status**: ❌
- **Reason**: LDPC 기반 HARQ+부분재전송 TCP 영향 분석, LDPC는 베이스라인이고 떼어낼 디코더·구성 기법 없음
- **ID**: ieee:5595132
- **Type**: journal
- **Published**: Aug. 2010
- **Authors**: Andre Gustavo Degraf Uchôa, Richard Demo Souza, Marcelo Eduardo Pellenz
- **PDF**: https://ieeexplore.ieee.org/document/5595132
- **Abstract**: The design of a novel HARQ scheme using LDPC codes, partial retransmissions, and diversity combining is presented. The theoretical throughput of the proposed scheme is estimated by means of EXIT charts. It is shown that the proposed method outperforms the classical equal gain combining (EGC) method while requiring few more overall decoding iterations. The transmission control protocol (TCP) performance when the proposed method is used in the physical layer is also investigated. Simulation results show that the gains with respect to the classical EGC scheme can be as large as 3.5 dB.

## Low redundancy overhead multibit error correction in memory

- **Status**: ✅
- **Reason**: 메모리 MBU 보호용 EG-LDPC+Hamming 결합 코드워드 구조, Verilog 구현—메모리 ECC 코드설계/HW 신규 기여(B/D/E)
- **ID**: ieee:5615316
- **Type**: conference
- **Published**: 28 July-1 
- **Authors**: Ming Zhu, Liyi Xiao, Zheng Sun +3
- **PDF**: https://ieeexplore.ieee.org/document/5615316
- **Abstract**: As technology scales, memories have become more susceptible to radiation induced multiple bit upsets (MBUs). Multibit error correction codes (MECC) are an effective approach to mitigate MBUs in memories. This paper proposes a new codeword structure to protect memory against MBUs. Euclidean Geometry Low Density Parity Check (EG-LDPC) codes and Hamming codes are combined in the proposed codeword to assure the reliability of memory with low redundancy overhead. Furthermore, the proposed codeword can protect some longer data which is difficult for other MECCs to deal with. By using the proposed codeword, both low redundancy overhead scheme and long data width scheme for multibit error correction are presented. Finally, the proposed schemes have been implemented in Verilog and validated through a wide set of simulations. The experiment results reveal that the proposed method has a superior protection level. Compared with general MECC, it has lower redundancy and performance overheads.

## Iterative symbol-by-symbol decoding of LDPC codes and constellation mapping for multilevel modulation

- **Status**: ❌
- **Reason**: modular arithmetic 다심볼 non-binary 부호+symbol-level sum-product, multilevel modulation 특이적 — 비이진 LDPC 제외
- **ID**: ieee:5684713
- **Type**: conference
- **Published**: 25-27 Aug.
- **Authors**: Hongtao Jiang, Zhongfeng Wang, Huaping Liu
- **PDF**: https://ieeexplore.ieee.org/document/5684713
- **Abstract**: Iterative probabilistic decoding of binary low-density parity-check (LDPC) codes have been studied extensively. Non-binary LDPC codes have recently attracted an increasing attention. Most of the existing non-binary codes are built over GF(2q), and decoding methods developed for binary LDPC codes cannot be used directly with multilevel modulations. In this paper, we first extend the binary parity-check codes to the case with multiple symbols over modular arithmetic. Then, we develop a sum-product algorithm to decode this new type of codes at the symbol level. Finally, we propose an effective constellation mapping method for multilevel modulations. Error performances of this type of codes with 4-PAM, 4-PSK, and 16-PSK modulations over AWGN channels are provided. Compared with uncoded systems, the coding gain of a medium-size regular LDPC code of rate 8/9 with 4-PAM and 4-PSK modulations is about 5 dB. With 16-PSK and an appropriate constellation mapping at a code rate 3/4, the proposed code's performance is comparable to that of trellis codes.

## From product codes to structured generalized LDPC codes

- **Status**: ✅
- **Reason**: QC-GLDPC 신규 구성으로 error floor 저감(E) — 바이너리 LDPC 코드설계 기여
- **ID**: ieee:5684632
- **Type**: conference
- **Published**: 25-27 Aug.
- **Authors**: Michael Lentmaier, Gianluigi Liva, Enrico Paolini +1
- **PDF**: https://ieeexplore.ieee.org/document/5684632
- **Abstract**: Product codes, due to their relatively large minimum distance, are often seen as a natural solution for applications requiring low error floors. In this paper, we show by means of an ensemble weight enumerator analysis that the minimum distance multiplicities of product codes are much higher than those obtainable by other generalized LDPC (GLDPC) constructions employing the same component codes. We then propose a simple construction of quasi-cyclic GLDPC codes which leads to significantly lower error floors while leaving the decoder architecture of product codes almost untouched.

## A source-destination network coded cooperation for wireless ad-hoc networks

- **Status**: ❌
- **Reason**: 무선 ad-hoc 네트워크 코딩(SDNCC/ANCC), LDGM 응용 특이적 — 떼어낼 LDPC ECC 기법 없음
- **ID**: ieee:5684774
- **Type**: conference
- **Published**: 25-27 Aug.
- **Authors**: Kaibin Zhang, Liuguo Yin, Jianhua Lu
- **PDF**: https://ieeexplore.ieee.org/document/5684774
- **Abstract**: Source-destination network coded cooperation (SDNCC), an extension of adaptive network coded cooperation (ANCC), which uses network coding and matches code-on-graph with network-on-graph, is proposed for wireless ad-hoc networks that comprise a collection of terminals communicating wirelessly to a common destination. In SDNCC, the destination broadcasts which terminal packets to be selected in the relay phase, which generates low-density generator-matrix (LDGM) codes with unequal error protection at cost of 1 bit per terminal. Additionally, the outage probability of SDNCC is evaluated and closed-form expression is derived for infinity networks. Furthermore, simulation results show that SDNCC achieves 4dB performance improvement over ANCC at frame error ratio (FER) of 3 × 10-5.

## Full-rate full-diversity space-frequency block coding for digital TV broadcasting

- **Status**: ❌
- **Reason**: MIMO space-time/space-frequency 코딩(DVB-T2 STC 검출). LDPC는 베이스라인이고 떼어낼 LDPC ECC 기법 없음
- **ID**: ieee:7096618
- **Type**: conference
- **Published**: 23-27 Aug.
- **Authors**: Iker Sobron, Mikel Mendicute, Jon Altuna
- **PDF**: https://ieeexplore.ieee.org/document/7096618
- **Abstract**: The goal of the future terrestrial and mobile digital video broadcasting standards is to combine diversity and spatial multiplexing in order to fully exploit the multiple-input multiple-output (MIMO) channel capacity. Full-rate full-diversity (FR-FD) space-time codes (STC) such as the Golden code, that maximize the rate preserving the diversity gain, are studied for that purpose. Most of them present a high-complexity detection problem which results in a handicap for their hardware implementation. Therefore, we analyze the performance of a sub-optimal full-rate full-diversity 2×2 STC, whose design reduces the complexity of the detection, as an alternative for future MIMO broadcasting TV systems. The assessment of the proposed STC code is carried out over the bit-interleaved coded modulation (BICM) scheme of DVB-T2 system which includes low-density parity check (LDPC) codes for error correction. Finally, soft STC list detection is studied in order to generate soft information for LDPC decoding.

## IRIS verification system with secure template storage

- **Status**: ❌
- **Reason**: 홍채 바이오메트릭 보안 템플릿(ECC+해시). 보안 응용, 떼어낼 LDPC 디코더/구성 기법 없음
- **ID**: ieee:7096661
- **Type**: conference
- **Published**: 23-27 Aug.
- **Authors**: Tiago Marques Santos, Luís Ducla Soares, Paulo Lobato Correia
- **PDF**: https://ieeexplore.ieee.org/document/7096661
- **Abstract**: In this paper, a secure biometric recognition system, that guarantees user privacy and revocable templates, is proposed. The data stored in the system database reveals no information about the original biometric features and it is practically impossible to recover them from the stored data. Revocability is ensured by generating different templates for the same user, using the same biometric data, just by changing a parameter in the secure template scheme. To achieve this goal, a combination of an error correcting code and a hash function is used. The recognition performance of the proposed system is not significantly affected when compared to the same system without template security. The estimated number of security bits it is between 98 and 171.

## Non-uniform source modeling for distributed video coding

- **Status**: ❌
- **Reason**: 분산소스코딩(DVC)·BSC 상관모델 압축, 소스코딩 영역. 채널 ECC LDPC 기법 아님
- **ID**: ieee:7096654
- **Type**: conference
- **Published**: 23-27 Aug.
- **Authors**: V. Toto-Zarasoa, A. Roumy, C. Guillemot
- **PDF**: https://ieeexplore.ieee.org/document/7096654
- **Abstract**: We introduce a novel correlation model, called predictive Binary Symmetric Channel (BSC), for Distributed Source Coding (DSC). We then consider non-uniform binary sources and show that, for the predictive BSC model, the non-uniformity does not reduce the compression rate in asymmetric DSC. We assess the minimum achievable rate loss induced by a mismatch between the assumed and the true correlation models. We also propose an LDPC-based decoder adapted to both the classical (additive) BSC and the new (predictive) BSC correlation models. Finally, for Distributed Video Coding (DVC) application, we propose a criterion that allows us to switch between the two correlation models.

## Distributed video coding with particle filtering for correlation tracking

- **Status**: ❌
- **Reason**: DVC particle filtering으로 상관 추적; 비디오 분산소스코딩 응용 특이적, 떼어낼 일반 LDPC 디코더 기법 없음
- **ID**: ieee:7096270
- **Type**: conference
- **Published**: 23-27 Aug.
- **Authors**: Lina Stankovic, Vladimir Stankovic, Shuang Wang +1
- **PDF**: https://ieeexplore.ieee.org/document/7096270
- **Abstract**: One of the main challenges of distributed video coding (DVC) is that correlation among source and side information needs to be estimated and well modelled a priori. Since in DVC correlation dynamically changes with the scene, in order to get the full benefit from powerful distributed source code (DSC) designs, predicting and tracking correlation is essential. This paper proposes an adaptive scheme based on integrated particle filtering within the LDPC-based DSC that dynamically tracks the changes in image correlation to enhance belief propagation LDPC decoding. The system maintains its low encoder complexity, showing significant performance improvement compared to the case without dynamic particle filtering tracking.

## Security applications of distributed arithmetic coding

- **Status**: ❌
- **Reason**: 분산산술코딩 기반 생체인증 보안; 소스코딩+보안, ECC 아님
- **ID**: ieee:7096510
- **Type**: conference
- **Published**: 23-27 Aug.
- **Authors**: Marco Grangetto, Enrico Magli, Gabriella Olmo
- **PDF**: https://ieeexplore.ieee.org/document/7096510
- **Abstract**: Distributed arithmetic coding (DAC) has recently been proposed for compression in the Slepian-Wolf setting. With respect to syndrome coding, DAC allows to easily adapt to non-stationary statistics of the signal to be coded, and works well for short and medium block lengths. In this paper we develop security applications of DAC in the field of biometric authentication. We show that DAC can be used for authentication by employing the codeword as secure hash, and using the outcome of DAC decoding for authentication. Moreover, we introduce a second powerful security feature, namely the randomization of the DAC intervals. This allows to protect the hash from attacks. We assess the authentication performance of the proposed scheme with respect to template matching and turbo codes.

## Distributed source coding: Theory and applications

- **Status**: ❌
- **Reason**: 분산소스코딩 서베이(압축). 소스코딩이라 채널 ECC 아님 + 서베이
- **ID**: ieee:7096269
- **Type**: conference
- **Published**: 23-27 Aug.
- **Authors**: Vladimir Stanković, Lina Stanković, Samuel Cheng
- **PDF**: https://ieeexplore.ieee.org/document/7096269
- **Abstract**: Distributed source coding (DSC) refers to separate compression and joint decompression of mutually correlated sources. Though theoretical foundations were set more than thirty years ago, driven by applications such as wireless sensor networks, video surveillance, and multiview video, DSC has over the past few years become a very active research area. This paper provides an introduction to DSC theory, practical code designs and applications, and outlines current research trends while identifying challenges and opportunities in both theory and practice of DSC.

## Bootstrapped Iterative Decoding Algorithms for Low Density Parity Check (LDPC) Codes

- **Status**: ✅
- **Reason**: 신뢰도비 기반 가중 비트플리핑(WBF) 디코더에 bootstrap 단계 추가한 신규 경판정 디코더(C), 바이너리 LDPC 이식 가능
- **ID**: ieee:5634871
- **Type**: conference
- **Published**: 22-27 Aug.
- **Authors**: Albashir Adel Mohamed, Maha Mohamed Elsabrouty, Salwa Hussien El-Ramly
- **PDF**: https://ieeexplore.ieee.org/document/5634871
- **Abstract**: Reliability ratio based weighted bit-flipping algorithm is one of the best hard decision decoding algorithms in performance. Recently several modifications are done to this technique either to improve performance or to lower the complexity. The implementation efficient reliability ratio based weighted bit-flipping is developed targeting decreasing processing time of the decoding process. In this paper we are targeting improving performance of recent developed algorithm named low complex implementation efficient reliability ratio based weighted bit-flipping by adding a bootstrap step to the decoding technique which leads to increase in reliability of received bits then number of decoded bits will be increased leading to improve in performance. Also a modification done to bootstrap step for further increase the performance.

## Modified Log-BP decoding algorithm combined with PSO for Low-Density Parity Check Codes

- **Status**: ✅
- **Reason**: Log-BP에 PSO 결합한 신규 디코더로 0.1dB 이득 → 이식 가능 디코더 알고리즘(C), Phase3 효용 재검토
- **ID**: ieee:5579320
- **Type**: conference
- **Published**: 20-22 Aug.
- **Authors**: Xiali Yan, Wenquan Feng, Qi Zhao +1
- **PDF**: https://ieeexplore.ieee.org/document/5579320
- **Abstract**: Message-Passing is the main decoding algorithm for Low-Density Parity Check (LDPC) Codes, in which Logarithmic Belief Propagation (Log-BP) algorithm is the most popularly used one. Particle Swarm Optimization (PSO) can also be regarded as an optimization algorithm by message-passing, which makes it possible to combine Log-BP algorithm with PSO. PSO was introduced into Log-BP algorithm by regarding all messages that bit nodes send to check nodes as the swarm with each message individually as a particle. Move the particles around in the search-space by certain iterations in each BP iteration processing, guided by the two best current values respectively found by particles themselves and that of the whole swarm. Those two best values were continually updated in each PSO iteration. In this way, the output of decoder is more consistent with accurate input sequence, in other words, the decoder performance was improved. Simulation results show that this new algorithm combined with Log-BP and PSO can get an additional 0.1 dB coding gain at Bit Error Rate (BER) of 10-5 compared with Log-BP algorithm.

## Reliability-based iterative decoding of LDPC codes using segmented accumulation of likelihood ratio

- **Status**: ✅
- **Reason**: BP+OSD 직렬연접에 segmented LLR accumulation 메트릭 개선 → 이식 가능 디코더 알고리즘(C)
- **ID**: ieee:5578935
- **Type**: conference
- **Published**: 20-22 Aug.
- **Authors**: Dong Zi-jian
- **PDF**: https://ieeexplore.ieee.org/document/5578935
- **Abstract**: In this work, we present an improvement on the belief propagation (BP) algorithm concatenated serially with order statistic decoding (OSD) for low-density parity-check (LDPC) codes. We use the segmented accumulation of log-likelihood ratio (LLR) of variance nodes as the ordered information metric to reconstruct received sequence. This method can reduce the sensitivity of accumulated parameter selection to the fluctuation of performance, and further improve decoding performance.

## A Construction Method of Niederreiter Public-Key Cryptosystem Based on Quantum LDPC Codes

- **Status**: ❌
- **Reason**: 양자 stabilizer LDPC 기반 Niederreiter 공개키 암호; 양자 전용 개념 의존+보안 응용, 고전 바이너리 LDPC 이식 기법 없음
- **ID**: ieee:5566239
- **Type**: conference
- **Published**: 20-22 Aug.
- **Authors**: Dong Cao, Yaoliang Song
- **PDF**: https://ieeexplore.ieee.org/document/5566239
- **Abstract**: Quantum public-key cryptosystem includes unconditionally secure quantum public-key cryptographic algorithm and computationally secure quantum public-key cryptographic algorithm. This paper presents a quantum Niederreiter public-key cryptosystem by using quantum stabilizer LDPC codes. Constructed key based on quantum LDPC codes directly. Take advantage of the sparsity of LDPC codes. Compared with McEliece public-key cryptosystem, Encoding complexity is reduced. Its security relies on the fact that NPC problem can not be solved on quantum Turing machines.

## Design of structured LDPC codes with quasi-cyclic and rotation architecture

- **Status**: ✅
- **Reason**: 새 구조화 QC/rotation LDPC 코드 설계 + dual-diagonal 선형복잡도 인코딩 + partially parallel 디코더 구조 → 바이너리 LDPC 코드설계(E)/HW(D) 이식 가능
- **ID**: ieee:5578934
- **Type**: conference
- **Published**: 20-22 Aug.
- **Authors**: Guo-lei Qiao, Zi-jian Dong
- **PDF**: https://ieeexplore.ieee.org/document/5578934
- **Abstract**: Quasi-cyclic low density parity check (LDPC) codes and rotation LDPC codes are investigated in this paper, based on which, a new class of well-structured LDPC codes are proposed. Additionally, for ease of coding, a dual-diagonal structure is applied to the parity-check matrices of those codes, which ensure that parity-check bits can be recursively calculated with linear computational complexity. With the rotating and cyclic shift structure, decoders can be effectively implemented with partially parallel architecture appeared in some literatures on QC-LDPC codes and other structured LDPC codes. Simulation results show that the proposed structured LDPC codes are feasible.

## Reduced-complexity extended Min-sum check node processing for non-binary LDPC decoding

- **Status**: ❌
- **Reason**: 비이진 NB-LDPC(GF(2^5)) 디코더 VLSI 아키텍처 — 비이진 LDPC는 제외 대상
- **ID**: ieee:5548712
- **Type**: conference
- **Published**: 1-4 Aug. 2
- **Authors**: Xinmiao Zhang, Fang Cai
- **PDF**: https://ieeexplore.ieee.org/document/5548712
- **Abstract**: Non-binary low-density parity-check (NB-LDPC) codes can achieve higher coding gain than binary LDPC codes when the code length is moderate at the cost of higher complexity. One major step of NB-LDPC decoding is check node processing. Previously, iterative forward-backward approaches are employed to implement this step. However, the storage of the intermediate results of the forward and backward computations requires large memory. In this paper, a novel check node processing scheme and corresponding VLSI architectures are proposed for the extended Min-sum NB-LDPC decoding. The proposed scheme only stores a limited number of sorted variable-to-check messages. Then the check-to-variable messages for different variable node are generated independently. For a (837, 726) NB-LDPC code over GF(25), the proposed architecture only requires 64% of the area of the previous design with the same throughput and error-correcting performance.

## A fixed bits LDPC decoder

- **Status**: ✅
- **Reason**: 부호/채널/알고리즘 비의존 fixed-bits 디코딩으로 error floor 개선 — 이식 가능 디코더 기법(C)
- **ID**: ieee:5559810
- **Type**: conference
- **Published**: 1-3 Aug. 2
- **Authors**: Fen Xu, Liang Zhou, Hong Wen +2
- **PDF**: https://ieeexplore.ieee.org/document/5559810
- **Abstract**: With iterative decoding, most LDPC codes have a weakness known as error floor. In this work, we propose a fixed bits LDPC decoding scheme to improve the ability of LDPC transmission. The method is universal as it can be applied to any code/channel model/decoding algorithm and it improves performance greatly, without losing the code regularity, without changing the decoding algorithm. Simulation results show that the error floor performance also can be significantly improved with this decoding scheme.

## Efficient uncompressed video communications using multicarrier, redundancy exploitation and low density error correction techniques

- **Status**: ❌
- **Reason**: 무선 비압축 비디오 전송 시스템에 LDPC 부수 사용, 떼어낼 ECC 기법 없음
- **ID**: ieee:5559780
- **Type**: conference
- **Published**: 1-3 Aug. 2
- **Authors**: Mohamed Khedr, Maha Sharkas, Ahmed Fawzy
- **PDF**: https://ieeexplore.ieee.org/document/5559780
- **Abstract**: In this paper, we present an efficient system for transmitting uncompressed image (HD) over wireless noisy channel. With the advances in RF technology and the huge bandwidth available worldwide in the 57-66 GHz millimeter-wave unlicensed spectrum, WPANs that can support multigigabit transmission are being developed. However, retransmissions due to error in packets may be unsuitable for uncompressed video streaming. In this paper we develop, simulate and evaluate an efficient system for reliable transmission of uncompressed image over wireless channel. The system uses image partitioning for redundancy exploitation, LDPC (low density parity check code) for channel coding and OFDM to recover the fading problem. Simulation using MATLAB indicates that with small SNR, we can achieve small image symbol error rate and high PSNR.
