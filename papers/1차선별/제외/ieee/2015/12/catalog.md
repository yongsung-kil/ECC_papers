# IEEE Xplore — 2015-12


## Analysis and Optimization of P-LDPC Coded RGB-LED-Based VLC Systems

- **Status**: ❌
- **Reason**: VLC RGB-LED용 P-LDPC 코딩변조/인터리버 최적화, 무선광통신 응용 특이적이며 떼어낼 바이너리 LDPC ECC 기법 없음
- **ID**: ieee:7320948
- **Type**: journal
- **Published**: Dec. 2015
- **Authors**: Chengjun Tang, Ming Jiang, Hong Shen +1
- **PDF**: https://ieeexplore.ieee.org/document/7320948
- **Abstract**: The goal of this paper is to study a well-performed coded modulation structure in visible light communication (VLC) systems equipped with red, green, and blue (RGB) light-emitting diodes (LEDs) to provide tools for performance analysis and to give guidelines for practical designs. Specifically, the protograph-based low-density parity-check (P-LDPC) codes and the optimized generalized variable degree matched mapping interleavers are applied to VLC systems for the first time. To theoretically analyze the system under concern, we utilize the protograph-based extrinsic information transfer (PEXIT) methodology that can accurately predict error performance. Furthermore, by leveraging this powerful analysis tool, we propose optimizing a VLC system from three perspectives, i.e., the interleaver design, the optimization of the power mixing ratio of RGB color lights, and the selection of coding schemes. Both PEXIT analyses and simulations verify that the performance of a VLC system can be greatly improved by optimizing these three components.

## Comparison of Convolutional and Block Codes for Low Structural Delay

- **Status**: ❌
- **Reason**: 짧은 블록 LDPC/convolutional/turbo 성능 비교(비이진 포함), 신규 디코더/구성/HW 기여 없는 비교 연구
- **ID**: ieee:7296605
- **Type**: journal
- **Published**: Dec. 2015
- **Authors**: Christoph Rachinger, Johannes B. Huber, Ralf R. Müller
- **PDF**: https://ieeexplore.ieee.org/document/7296605
- **Abstract**: The performance of short block length low-density parity-check (LDPC) codes (both binary and nonbinary) and convolutional codes is compared under the constraint of tight structural delay constraints. Additionally, we use fundamental bounds on block codes and low rate turbo codes to evaluate our results in a broader context. It turns out that-depending on the code rate and given delay-convolutional codes are able to outperform fundamental lower bounds for block codes, yielding a definite result on the question, which codes are superior in this regime. From a break-even point onward, convolutional codes cannot compete with block codes anymore and nonbinary LDPC codes show the best performance. Turbo codes with a short interleaver length show competitive results.

## Bandwidth Efficient and Rate-Matched Low-Density Parity-Check Coded Modulation

- **Status**: ❌
- **Reason**: 확률적 신호 셰이핑 + DVB-S2 표준 LDPC 그대로 사용한 코딩변조 기법, 떼어낼 신규 LDPC ECC 기법 없음
- **ID**: ieee:7307154
- **Type**: journal
- **Published**: Dec. 2015
- **Authors**: Georg Böcherer, Fabian Steiner, Patrick Schulte
- **PDF**: https://ieeexplore.ieee.org/document/7307154
- **Abstract**: A new coded modulation scheme is proposed. At the transmitter, the concatenation of a distribution matcher and a systematic binary encoder performs probabilistic signal shaping and channel coding. At the receiver, the output of a bitwise demapper is fed to a binary decoder. No iterative demapping is performed. Rate adaption is achieved by adjusting the input distribution and the transmission power. The scheme is applied to bipolar amplitudeshift keying (ASK) constellations with equidistant signal points and it is directly applicable to two-dimensional quadrature amplitude modulation (QAM). The scheme is implemented by using the DVB-S2 low-density parity-check (LDPC) codes. At a frame error rate of 10-3, the new scheme operates within less than 1.1 dB of the AWGN capacity 1/2 log2(1 + SNR) at any spectral efficiency between 1 and 5 bits/s/Hz by using only 5 modes, i.e., 4-ASK with code rate 2/3, 8-ASK with 3/4, 16-ASK and 32-ASK with 5/6, and 64-ASK with 9/10.

## Coded Slotted ALOHA: A Graph-Based Method for Uncoordinated Multiple Access

- **Status**: ❌
- **Reason**: coded slotted ALOHA 랜덤액세스, erasure 코드/SIC 그래프 기반 MAC 최적화로 채널 ECC 기법 아님
- **ID**: ieee:7302046
- **Type**: journal
- **Published**: Dec. 2015
- **Authors**: Enrico Paolini, Gianluigi Liva, Marco Chiani
- **PDF**: https://ieeexplore.ieee.org/document/7302046
- **Abstract**: In this paper, a random access scheme is introduced, which relies on the combination of packet erasure correcting codes and successive interference cancellation (SIC). The scheme is named coded slotted ALOHA. A bipartite graph representation of the SIC process, resembling iterative decoding of generalized low-density parity-check codes over the erasure channel, is exploited to optimize the selection probabilities of the component erasure correcting codes through a density evolution analysis. The capacity (in packets per slot) of the scheme is then analyzed in the context of the collision channel without feedback. Moreover, a capacity bound is developed, and component code distributions tightly approaching the bound are derived.

## Improved Generation of Identifiers, Secret Keys, and Random Numbers From SRAMs

- **Status**: ❌
- **Reason**: SRAM PUF 식별자/키/난수 생성, ECC 복잡도는 부수 언급만, 떼어낼 LDPC 디코더/구성/HW 없음
- **ID**: ieee:7217837
- **Type**: journal
- **Published**: Dec. 2015
- **Authors**: Iluminada Baturone, Miguel A. Prada-Delgado, Susana Eiroa
- **PDF**: https://ieeexplore.ieee.org/document/7217837
- **Abstract**: This paper presents a method to simultaneously improve the quality of the identifiers, secret keys, and random numbers that can be generated from the start-up values of standard static random access memories (SRAMs). The method is based on classifying memory cells after evaluating their start-up values at multiple measurements in a registration phase. The registration can be done without unplugging the device from its application context, and with no need for a complex laboratory setup. The method has been validated experimentally with standard low-power SRAM modules in two different application specific integrated circuits (ASICs) fabricated with the 90-nm TSMC technology. The results show that with a simple registration the length of the identifiers can be reduced by 45%, the worst case bit error probability (which defines the complexity of the error correcting code needed to recover a secret key) can be reduced by 64%, and the worst case minimum entropy value is improved, thus reducing the number of bits that have to be processed to obtain full entropy by 81%. The method can be applied to standard digital designs by controlling the external power supply to the SRAM using software or by incorporating simple circuitry in the design. In the latter case, a module for implementing the method in an ASIC designed in the 90-nm TSMC technology occupies an active area of 42, 025 μm2.

## Iterative Channel Estimation and Impulsive Noise Mitigation Algorithm for OFDM-Based Receivers With Application to Power-Line Communications

- **Status**: ❌
- **Reason**: PLC OFDM 임펄스 잡음 완화/채널추정 수신기 — LDPC ECC 디코더/HW/코드설계 기여 없음
- **ID**: ieee:7124501
- **Type**: journal
- **Published**: Dec. 2015
- **Authors**: Ying-Ren Chien
- **PDF**: https://ieeexplore.ieee.org/document/7124501
- **Abstract**: This paper presents a novel iterative receiver used to mitigate the impact of impulsive noise (IN) on orthogonal frequency-division multiplexing (OFDM)-based baseband power-line communications. An adaptive threshold is mathematically derived for the detection of IN under a desired false alarm probability. This detection mechanism is then used to mitigate IN in two stages. Prior to the OFDM demodulation, a pre-IN mitigation block is used to clip the stronger portions of the IN source. This preprocessing significantly reduces the power of the IN spreading into all subcarriers and, thus, facilitates the detection of residual IN in the second stage. After the OFDM demodulation, the proposed receiver iteratively estimates the channel impulse response and reduces IN sources that were not detected by the pre-IN mitigation block. Post-IN mitigation involves the iterative reconstruction of residual IN, which is then subtracted from the received signal. Denoising is also applied to the estimated channel impulse response. Thus, channel estimation and IN mitigation are mutually beneficial. Simulation results confirm that the proposed iterative receiver significantly improves the mean squared error of the channel estimation as well as bit-error rate.

## The Second-Order Coding Rate of the MIMO Quasi-Static Rayleigh Fading Channel

- **Status**: ❌
- **Reason**: MIMO 페이딩 채널 2차 코딩레이트 순수 이론 bound, 디코더/HW/구성으로 안 이어짐
- **ID**: ieee:7296644
- **Type**: journal
- **Published**: Dec. 2015
- **Authors**: Jakob Hoydis, Romain Couillet, Pablo Piantanida
- **PDF**: https://ieeexplore.ieee.org/document/7296644
- **Abstract**: The second-order coding rate of the multiple-input multiple-output (MIMO) quasi-static Rayleigh fading channel is studied. We tackle this problem via an information-spectrum approach and statistical bounds based on recent random matrix theory techniques. We derive a central limit theorem (CLT) to analyze the information density in the regime where the block length n and the number of transmit and receive antennas K and N, respectively, grow simultaneously large. This result leads to the characterization of closed-form upper and lower bounds on the optimal average error probability when the coding rate is within O(1/√(nK)) of the asymptotic capacity.

## Prioritized Random MAC Optimization Via Graph-Based Analysis

- **Status**: ❌
- **Reason**: IRSA 우선순위 랜덤 MAC 최적화, BP 유추일 뿐 떼어낼 LDPC 디코더/ECC 기법 없음
- **ID**: ieee:7305777
- **Type**: journal
- **Published**: Dec. 2015
- **Authors**: Laura Toni, Pascal Frossard
- **PDF**: https://ieeexplore.ieee.org/document/7305777
- **Abstract**: Motivated by the analogy between successive interference cancellation and iterative belief-propagation on erasure channels, irregular repetition slotted ALOHA (IRSA) strategies have received a lot of attention in the design of medium access control protocols. In this work, we consider generic systems where sources in different importance classes compete for a common channel. We propose a new prioritized IRSA algorithm and derive the probability to correctly resolve collisions for data from each source class. We then make use of our theoretical analysis to formulate a new optimization problem for selecting the transmission strategies of heterogenous sources. We optimize both the replication probability per class and the source rate per class, in such a way that the overall system utility is maximized. We then propose a heuristic-based algorithm for the selection of the transmission strategy, which is built on intrinsic characteristics of the iterative decoding methods adopted for recovering from collisions. Experimental results validate the accuracy of the theoretical study and show the gain of well-chosen prioritized transmission strategies for transmission of data from heterogenous classes over shared wireless channels.

## Performance Characterization and Optimization of Mobile Service Delivery in LDM-Based Next Generation DTV Systems

- **Status**: ❌
- **Reason**: LDM 기반 DTV 모바일 서비스 채널추정/안테나 다이버시티, LDPC 베이스라인일 뿐 이식할 ECC 기법 없음
- **ID**: ieee:7271003
- **Type**: journal
- **Published**: Dec. 2015
- **Authors**: Liang Zhang, Wei Li, Yiyan Wu +9
- **PDF**: https://ieeexplore.ieee.org/document/7271003
- **Abstract**: Layered-division-multiplexing (LDM) technology is a non-orthogonal multiplexing technology to provide more efficient transmission of multiple services that have different requirements on the robustness and throughput in one TV channel. The core of LDM is to transmit multiple-layer signals, where each layer occupies the whole channel bandwidth and the whole time. To meet the different requirements on different layers, each layer is allocated a specific power level, and is configured to use a different channel coding and modulation scheme, as well as its own multiple-antenna technology. Delivering robust and high-quality mobile TV services is one of the top priorities for the next generation digital TV (NG-DTV) systems. In this paper, we first investigate the performance of the NG-DTV systems with LDM in various difficult propagation channels that are likely encountered by the large variety of mobile devices, including fast-fading channels, slow-fading channels, indoor channels, and single-frequency-network (SFN) channels. A new channel estimation technique is proposed to overcome the severe performance degradation caused by the SFN channels. We will further show that using LDM makes it possible to deliver mobile services using the efficient 32k transmission mode. Finally, receive antenna diversity is shown to provide different levels of performance improvement for different LDM configurations.

## Multilevel Coded Modulation With Reduced Latency Decoding Based on Novel Set Partitioning for APSK

- **Status**: ❌
- **Reason**: APSK 멀티레벨 코딩의 셋파티셔닝/레이블링 기법, LDPC 비의존적 변조 기법으로 이식할 LDPC ECC 기여 없음
- **ID**: ieee:7329953
- **Type**: journal
- **Published**: Dec. 2015
- **Authors**: Daiki Yoda, Hideki Ochiai
- **PDF**: https://ieeexplore.ieee.org/document/7329953
- **Abstract**: We address the use of a multilevel coding (MLC) to the amplitude phase-shift keying (APSK) modulations that consist of multiple PSK rings of different radii with a distinct number of constellation points. Such modulations have been adopted in the satellite broadcasting standards since they have a significant advantage over commonly used square-type quadrature amplitude modulations; their signals exhibit lower peak-to-average power ratio and thus enhance the power amplifier efficiency at the transmitter. A common low-complexity approach for decoding of MLC is the multi-stage decoding (MSD). However, MSD in general leads to severe latency at the decoder since the binary decisions on the higher levels should wait for those of the lower levels. Furthermore, this latency issue is even more salient for APSK signaling due to its circular nature of constellations that does not allow its decomposition into in-phase and quadrature components (i.e., I-Q decomposition). Therefore, in this paper we introduce a new MLC design for APSK that enables the decoder to reduce its latency without any increase in terms of complexity. The proposed approach consists of a novel labeling with an unconventional set partitioning that allows the detector to make use of I-Q decomposition. Specifically, the proposed set partitioning results in a quadrature-PSK constellation at the penultimate level, which can be decomposed into a pair of separately decodable binary-PSK constellations at the final level. The resulting decoder consists of a combination of MSD and parallel independent decoding that can be implemented with lower latency. The simulation results together with the theoretical analyses demonstrate that the reduction of not only the decoding latency but also the complexity in bit metric calculation can be achieved without noticeable degradation in terms of error performance compared to the conventional set partitioning approach.

## Hybrid-ARQ-Aided Short Fountain Codes Designed for Block-Fading Channels

- **Status**: ❌
- **Reason**: fading용 fountain/Raptor 코드 + HARQ — fountain/erasure 코드, 떼어낼 바이너리 LDPC ECC 기법 없음
- **ID**: ieee:7004076
- **Type**: journal
- **Published**: Dec. 2015
- **Authors**: Hong Chen, Robert G. Maunder, Yi Ma +2
- **PDF**: https://ieeexplore.ieee.org/document/7004076
- **Abstract**: As a benefit of their inherent rateless nature, fountain codes constitute a favorable choice for protecting packet-based transmissions in the physical layer for wireless channels having varying quality. However, previous research has revealed that the performance of fountain codes substantially degrades as their block length is reduced. Three structural phenomena of the Tanner graph were identified by Mackay in the hard decoding of fountain codes on binary erasure channels (BECs), which may be referred to as having “no degree-one check nodes (CNs),” “no emerging degree-one CNs,” and “uncovered variable nodes (VNs).” In this paper, we explicitly analyzed how these structural phenomena influence their soft decoding algorithm. Furthermore, these phenomena are shown to be responsible for the high error floors when fountain codes are transmitted over noisy fading channels, particularly for the transmissions of short blocks. To eliminate the influence of these structural phenomena, we conceived a technique of generating a few specifically encoded bits with the aid of the associated Tanner graph. Simulation results have demonstrated that our improved Raptor (IRaptor) codes significantly reduce the packet loss ratio (PLR) of conventional fountain codes, despite imposing reduced low complexity. Finally, we conceive a novel adaptive hybrid automatic repeat request (HARQ) scheme based on a lookup table (LUT)-aided technique, which may adapt its coding rate for each transmission. Our simulation results demonstrated that the proposed IRaptor HARQ achieves a similar performance to the Long-Term Evolution (LTE) turbo-coded HARQ scheme or even outperforms the LTE arrangement for block length in excess of 1000 bits.

## A non-binary LDPC Code in WBAN: Patterned data transmission

- **Status**: ❌
- **Reason**: 비이진(non-binary) LDPC — 기준상 명시적 제외
- **ID**: ieee:7391863
- **Type**: conference
- **Published**: 9-12 Dec. 
- **Authors**: Sekson Timakul, Buncha Sansoda, Somsak Choomchuay
- **PDF**: https://ieeexplore.ieee.org/document/7391863
- **Abstract**: This paper details the application of a PEG originated non-binary LDPC codes designed to fit the pay load size of MAC frame of IEEE 802.15.6 Wireless Body Area Network. The resulted codes are with the block size is 255 bytes. Codes with the rate of 0.5 and 0.9 are investigated for their performance. The symbol error rate and block error rate performance given by the system simulation has confirmed that the non-binary LDPC code can yield better performance when compared with hard decision Reed Solomon codes.

## Protograph Quantum LDPC Codes from Tensor Product of Parity-Check Matrices

- **Status**: ❌
- **Reason**: Quantum LDPC codes via tensor product, non-binary parity matrices, depolarizing channel — quantum + non-binary, excluded.
- **ID**: ieee:7414205
- **Type**: conference
- **Published**: 6-10 Dec. 
- **Authors**: Yixuan Xie, Jinhong Yuan
- **PDF**: https://ieeexplore.ieee.org/document/7414205
- **Abstract**: We propose two constructions, namely Construction 1 and Construction 2, for the design of protograph quantum LDPC codes by exploiting conventional quasi cyclic protograph LDPC codes with lift operation, and tensor product operation, respectively. We show that by carefully designing the proto-matrix using quadratic residue sets of parameters p = 4n ± 1, the proposed Construction 1 yields protograph quantum LDPC codes of various rates. Furthermore, by performing tensor product between two non-binary parity-check matrices obtained from idempotent polynomials of a quadratic residue set, the proposed Construction 2 yields a class of protograph quantum LDPC codes with rate at least 0.9. The performance of the proposed codes over quantum depolarizing channel with iterative sum-product decoding algorithm is shown.

## LDPC Code Design Aspects for Physical-Layer Key Reconciliation

- **Status**: ❌
- **Reason**: Physical-layer key reconciliation with LDPC (multi-edge density evolution); reconciliation not channel ECC, no extractable decoder/HW technique.
- **ID**: ieee:7417119
- **Type**: conference
- **Published**: 6-10 Dec. 
- **Authors**: Nazia Islam, Oana Graur, Alexandra Filip +1
- **PDF**: https://ieeexplore.ieee.org/document/7417119
- **Abstract**: In this work, we investigate a physical-layer key reconciliation protocol for a reciprocal, flat fading channel between two legitimate users. We consider the scenario when the n bits of the secret key are measured independently by Alice and Bob without a transmission over the channel. Due to reciprocity, the generated keys are identical except for noise at both ends. We assume Gaussian noise and ignore non-ideal behavior of circuitry and alike. Redundancy information required to reconciliate the key is transmitted from one legitimate user to the other. LDPC codes are employed for the reconciliation procedure. The main focus of this work lies in designing the code structure through density evolution for a multi-edge-type description.

## Enhanced Cryptcoding: Joint Security and Advanced Dual-Step Quasi-Cyclic LDPC Coding

- **Status**: ❌
- **Reason**: QC-LDPC와 AES 결합 cryptcoding—보안 결합 응용, 새 디코더/구성 없이 표준 QC-LDPC 사용
- **ID**: ieee:7417284
- **Type**: conference
- **Published**: 6-10 Dec. 
- **Authors**: Eran Pisek, Shadi Abu-Surra, Rakesh Taori +2
- **PDF**: https://ieeexplore.ieee.org/document/7417284
- **Abstract**: Data security has always been a major concern and a huge challenge for governments and individuals throughout the world since early times. Recent advances in technology, such as the introduction of cloud computing, make it even a bigger challenge to keep data secure. In parallel, high throughput mobile devices such as smartphones and tablets are designed to support these new technologies. The high throughput requires power-efficient designs to maintain the battery-life. In this paper, we propose a novel Joint Security and Advanced Low Density Parity Check (LDPC) Coding (JSALC) method. The JSALC is composed of two parts: the Joint Security and Advanced LDPC-based Encryption (JSALE) and the dual-step Secure LDPC code for Channel Coding (SLCC). The JSALE is obtained by interlacing Advanced Encryption System (AES)-like rounds and Quasi-Cyclic (QC)-LDPC rows into a single primitive. Both the JSALE code and the SLCC code share the same base quasi-cyclic parity check matrix (PCM) which retains the power efficiency compared to conventional systems. We show that the overall JSALC Frame-Error-Rate (FER) performance outperforms other cryptcoding methods by over 1.5 dB while maintaining the AES-128 security level. Moreover, the JSALC enables error resilience and has higher diffusion than AES-128.

## The Joint Demodulation and Decoding for BICM-ID System with BEC Approximation and Optimized Bit Mapping

- **Status**: ❌
- **Reason**: BICM-ID EXIT/비트매핑 최적화에 DVB-S2 표준 LDPC를 베이스라인으로 사용; 새 LDPC 디코더/구성 기여 없음
- **ID**: ieee:7417843
- **Type**: conference
- **Published**: 6-10 Dec. 
- **Authors**: Junyi Du, Liang Zhou, Xuan He
- **PDF**: https://ieeexplore.ieee.org/document/7417843
- **Abstract**: To improve the performance further for the bit- interleaved coded modulation with iterative decoding (BICM-ID) system, a modified extrinsic information transfer (EXIT) model is presented, in which the decoding and the demodulation are modeled as two iterative processing units. By using the binary erasure channel (BEC) approximation for the a priori AWGN channel, the analytical formulation of mutual information for sub-channels in M-QAM are obtained. Besides, the grid depth-first searching algorithm (GDFSA) is modified for designing the optimal bit mapping distribution with minimum convergence rate. Using the DVB-S2 rate-0.5 64800-bit low-density parity-check (LDPC) code as demonstration, the simulations show that the BER performances achieve 0.225/0.650dB gains at 10^-5 for 16-QAM/32-QAM under AWGN channel, compared to the consecutive bit mapping.

## Soft-Output Demapper with Approximated LLR for DVB-T2 Systems

- **Status**: ❌
- **Reason**: DVB-T2 QAM 디맵퍼 LLR 근사—변조 디맵핑 단계 근사, LDPC 디코더 내부 기법 아님(무선 응용 특이적)
- **ID**: ieee:7417395
- **Type**: conference
- **Published**: 6-10 Dec. 
- **Authors**: Giuseppe Baruffa, Luca Rugini
- **PDF**: https://ieeexplore.ieee.org/document/7417395
- **Abstract**: Bit-interleaved coded modulation (BICM) is at the heart of the second generation digital terrestrial television systems (DVB-T2), which achieves a large spectral efficiency by means of high-order quadrature amplitude modulation (QAM) and low-density parity-check (LDPC) codes. This paper proposes a simple but effective approximation for the log-likelihood ratio (LLR) of the bits estimated by the soft-output QAM demapper. The proposed approximation, which keeps few dominant terms of the LLR expression, needs low additional complexity with respect to the conventional Max-Log approximation. Simulation results for DVB-T2 in multipath channels show a performance gain with respect to the Max-Log approach, especially for QAM with large modulation order.

## Non-Binary LDPC Code Optimization for Partial-Response Channels

- **Status**: ❌
- **Reason**: NB-LDPC(비이진) PR채널 error floor 최적화—비이진 LDPC라 제외(바이너리만 포함)
- **ID**: ieee:7417425
- **Type**: conference
- **Published**: 6-10 Dec. 
- **Authors**: Ahmed Hareedy, Behzad Amiri, Shancheng Zhao +2
- **PDF**: https://ieeexplore.ieee.org/document/7417425
- **Abstract**: In this paper, we analyze and optimize non- binary low-density parity-check (NB-LDPC) codes for magnetic recording applications. While the topic of the error floor performance of binary LDPC codes over additive white Gaussian noise (AWGN) channels has recently received considerable attention, very little is known about the error floor performance of NB-LDPC codes over other types of channels, despite the early results demonstrating superior characteristics of NB-LDPC codes relative to their binary counterparts. We first show that, due to outer looping between detector and decoder in the receiver, the error profile of NB-LDPC codes over partial-response (PR) channels is qualitatively different from the error profile over AWGN channels - this observation motivates us to introduce new combinatorial definitions aimed at capturing decoding errors that dominate PR channel error floor region. We call these errors (or objects) balanced absorbing sets (BASs), which are viewed as a special subclass of previously introduced absorbing sets (ASs). Additionally, we prove that due to the more restrictive definition of BASs (relative to the more general class of ASs), an additional degree of freedom can be exploited in code design for PR channels. We then demonstrate that the proposed code optimization aimed at removing dominant BASs offers improvements in the frame error rate (FER) in the error floor region by up to 2.5 orders of magnitude over the uninformed designs. Our code optimization technique carefully yet provably removes BASs from the code while preserving its overall structure (node degree, quasi-cyclic property, regularity, etc.). The resulting codes outperform existing binary and NB-LDPC solutions for PR channels by about 2.5 and 1.5 orders of magnitude, respectively.

## Novel Fast Iterative Decoding Threshold Estimation for Protograph-Based LDPC Convolutional Codes

- **Status**: ❌
- **Reason**: PEXIT 기반 LDPC-CC 디코딩 임계값 추정—순수 분석 기법, 떼어낼 디코더/HW/코드설계 기여 없음
- **ID**: ieee:7417209
- **Type**: conference
- **Published**: 6-10 Dec. 
- **Authors**: Tian Xia, Hsiao-Chun Wu, Hong Jiang
- **PDF**: https://ieeexplore.ieee.org/document/7417209
- **Abstract**: The iterative decoding threshold (IDT) estimation for LDPC convolutional codes (LDPC-CCs) may become difficult over additive white Gaussian noise channels, especially when the termination length L gets very large or even approaches infinity. In this paper, we devise a novel fast IDT estimation scheme using the protograph-based extrinsic information transfer (PEXIT) analysis for protograph-based LDPC-CCs. Based on our new analysis, we propose a PEXIT-fast algorithm in which only the mutual information (MI) of a posteriori probability (APP) of the first variable node will be monitored to determine whether the current E_b/N_0 (signal-energy-per-information-bit to noise-power- spectral-density ratio) in evaluation is an upper bound or a lower bound of the IDT. Hence, it is no longer necessary to get through the whole MI evolution and the computational complexity can be greatly reduced thereby. We also design an efficient approach to determine the IDT for an LDPC-CC with an arbitrary large termination length L which can also be allowed to be infinity. The closeness between the known IDTs and the estimated IDTs using our proposed new method for several LDPC-CCs in simulation confirms the effectiveness of our scheme.

## Deployment Strategies for Ultra-Reliable and Low-Latency Communication in Factory Automation

- **Status**: ❌
- **Reason**: 5G factory automation deployment strategies (coverage/capacity); no LDPC ECC content.
- **ID**: ieee:7414016
- **Type**: conference
- **Published**: 6-10 Dec. 
- **Authors**: Nadia Brahmi, Osman N. C. Yilmaz, Ke Wang Helmersson +2
- **PDF**: https://ieeexplore.ieee.org/document/7414016
- **Abstract**: Factory automation is one of the challenging use cases that the fifth generation, 5G, networks are expected to support. It involves mission-critical machine-type communications, MTC, with requirements of extreme low-latency and ultra-reliable communication to enable real-time control of automation processes in manufacturing facilities. In this paper, we discuss the deployment strategies for the 5G mission-critical MTC solution designed to meet the needs of factory automation applications. The paper analyzes the coverage and capacity aspects based on a series of system-level evaluations considering both noise-limited and interference- limited operations. It further analyzes the related trade-offs to provide insights on the network deployment strategies for a realistic factory scenario.

## HARQ Rate-Compatible Polar Codes for Wireless Channels

- **Status**: ❌
- **Reason**: HARQ rate-compatible polar codes—polar 부호 설계, 떼어낼 바이너리 LDPC BP 기법 없음
- **ID**: ieee:7417429
- **Type**: conference
- **Published**: 6-10 Dec. 
- **Authors**: Mostafa El-Khamy, Hsien-Ping Lin, Jungwon Lee +2
- **PDF**: https://ieeexplore.ieee.org/document/7417429
- **Abstract**: A design of rate-compatible polar codes suitable for HARQ communications is proposed in this paper. An important feature of the proposed design is that the puncturing order is chosen with low complexity on a base code of short length, which is then further polarized to the desired length. A practical rate-matching system that has the flexibility to choose any desired rate through puncturing or repetition while preserving the polarization is suggested. The proposed rate-matching system is combined with channel interleaving and a bit-mapping procedure that preserves the polarization of the rate-compatible polar code family over bit-interleaved coded modulation systems. Simulation results on AWGN and fast fading channels with different modulation orders show the robustness of the proposed rate-compatible polar code in both Chase combining and incremental redundancy HARQ communications.

## Physical-Layer Secrecy Performance in Finite Blocklength Case

- **Status**: ❌
- **Reason**: 물리계층 보안 유한블록길이 분석—순수 이론 bound, LDPC 무관
- **ID**: ieee:7417362
- **Type**: conference
- **Published**: 6-10 Dec. 
- **Authors**: Chen Cao, Hongxiang Li, Zixia Hu +2
- **PDF**: https://ieeexplore.ieee.org/document/7417362
- **Abstract**: For physical-layer secrecy performance, existing studies only focus on coding schemes that can achieve the secrecy capacity. However, finite blocklength penalty could be fatal for security of private message. In this paper, we explore the impact of finite blocklength on secrecy for the wiretap channel model. We propose secrecy performance matrices for finite blocklength analysis and provide analytical expressions to evaluate the secrecy performance. We demonstrate trade-off between secrecy and reliability, and also provide an upper bound of secret information rate in finite blocklength case. The results are also applied to indicate asymptotic performance.

## Universal Multi-Stage Precoding with Monomial Phase Rotation for Full-Diversity M2M Transmission

- **Status**: ❌
- **Reason**: M2M 다단 프리코딩(유니터리 변환·위상회전)—LDPC 무관 무선 다이버시티 기법
- **ID**: ieee:7417467
- **Type**: conference
- **Published**: 6-10 Dec. 
- **Authors**: Toshiaki Koike-Akino, Keyong Jin Kim, Milutin Pajovic +1
- **PDF**: https://ieeexplore.ieee.org/document/7417467
- **Abstract**: Machine-to-machine (M2M) communications have been considered as an important application to connect a massively large number of different devices in networks. In particular for M2M wireless networks, low latency and high reliability are of great importance. To fulfill the requirements, a diversity technique exploiting limited resources is proposed in this paper for short-message transmissions. The proposed method uses multiple stages of fast unitary transforms and diagonal phase rotations to achieve full- diversity gain. A monomial phase rotation is also proposed to facilitate an optimization of the precoding matrix. It is verified that the proposed four-stage precoding provides universal diversity gain irrespective of channel selectivity in time and frequency, without changing monomial parameters. In addition, it is shown that the four-stage precoding based on the discrete Haar transform (DHT) achieves a full diversity while the computational complexity is significantly reduced from a log- linear order to a linear order compared to the other unitary transforms such as the discrete Fourier transform (DFT).

## Low-Complexity Decoding of Repeat-Accumulate Codes over Quasi-Static Fading Channels

- **Status**: ❌
- **Reason**: RA(repeat-accumulate) 코드 + SOVA/MLSD 트렐리스 디코더; LDPC 아님, 떼어낼 BP 이식 기법 없음
- **ID**: ieee:7417667
- **Type**: conference
- **Published**: 6-10 Dec. 
- **Authors**: Haifeng Yuan, Pooi Yuen Kam
- **PDF**: https://ieeexplore.ieee.org/document/7417667
- **Abstract**: We consider iterative decoding of repeat- accumulate (RA) codes over frequency-flat, quasi- static fading channels. A soft-input, soft-output decoder is proposed for the inner convolutional decoding, which fuses the decoding approach of the soft-output Viterbi algorithm and the estimation approach of the maximum-likelihood sequence detector. The decoder deploys trellis search algorithm based on the generalized likelihood ratio test, whereby the channel state information is acquired implicitly using both the pilot and data signals during the decoding process. Through simulations, we show that the RA decoding with the proposed decoder has much better error performance than standard RA decoding with pilot-symbol- assisted channel estimation, while having approximately the same computational complexity. Compared with the conventional scheme of iterative channel estimation and decoding, the proposed decoder has much simpler structure and requires significantly less computational power, although it incurs some loss in error performance.

## Mutual Information and Coded BER Analysis of PAPR Reduced OFDM System with Active Constellation Extension

- **Status**: ❌
- **Reason**: OFDM PAPR/ACE 클리핑 잡음 분석; 채널코딩은 부수 언급, 떼어낼 LDPC 디코더 기법 없음
- **ID**: ieee:7417808
- **Type**: conference
- **Published**: 6-10 Dec. 
- **Authors**: Ryota Yoshizawa, Hideki Ochiai
- **PDF**: https://ieeexplore.ieee.org/document/7417808
- **Abstract**: Active constellation extension (ACE) has been proposed for a peak-to-average power (PAPR) reduction of orthogonal frequency- division multiplexing (OFDM) signals, which projects the clipping noise generated by iterative clipping and filtering (CAF) onto the outside region of the constellation such that its minimum Euclidean distance (MED) is not reduced. Due to this arrangement, some amount of average power increase is introduced, but ACE can achieve better trade-off between uncoded bit-error rate (BER) and power amplifier (PA) efficiency compared to simple CAF. However, the coded BER of ACE has not been analyzed so far, where the degradation of signal-to-noise power ratio (SNR) due to the average power increase may have dominant effect on the performance. Moreover, in order to perform effective error correction, the statistical property of the clipping noise imposed by ACE should be developed. This paper empirically models the clipping noise distribution after ACE such that soft decoding can be employed at its receiver, and investigates its performance in terms of mutual information and coded BER employing near optimal channel coding. It is revealed that the simple CAF may outperform the ACE in terms of both PA efficiency and BER performance when both are protected by practical channel coding.

## Adaptive Minimum-Distance Based Precoder for NB-LDPC Coded MIMO Transmission

- **Status**: ❌
- **Reason**: NB-LDPC MIMO 프리코더—비이진 LDPC + 무선 프리코딩, 제외 대상
- **ID**: ieee:7417370
- **Type**: conference
- **Published**: 6-10 Dec. 
- **Authors**: Tarek Chehade, Ludovic Collin, Philippe Rostaing +2
- **PDF**: https://ieeexplore.ieee.org/document/7417370
- **Abstract**: In this paper, we focus on a multiple-input multiple-output (MIMO) linear precoder based on the minimum Euclidean distance criterion, the max- dmin precoder. We propose an optimization of this precoder for the case of an association with a non-binary low density parity check code (NB- LDPC). After recalling the well-known max-dmin precoder, we set forth an optimization of the mutual information of initial message, i.e. I(0), through the extrinsic information transfer (EXIT) analysis of the system. We present a new adaptive precoder whose forms are determined in function of an adaptive threshold angle, optimized in terms of the mutual information I(0), and depending on the signal-to-noise ratio at the reception (SNR_R). The performance of the new precoder is brought out through a theoretical study along with a series of numerical simulations.

## Video conferencing system for distance education

- **Status**: ❌
- **Reason**: 원격교육 화상회의 시스템/카메라 추적; ECC와 무관
- **ID**: ieee:7456682
- **Type**: conference
- **Published**: 4-6 Dec. 2
- **Authors**: Chandra Bhushan Kumar, Anjali Potnis, Shefali Gupta
- **PDF**: https://ieeexplore.ieee.org/document/7456682
- **Abstract**: Video conferencing plays vital role in communication which can be point-to-point or multipoint real-time communication between two or more student located at different geographical locations. However, it is very difficult to adjust a video capturing device to focus on faculty, especially in distance education classroom where faculty moves off the camera while delivering lecture. Also in distance education, there is requirement of real-time interaction between faculty and student, getting feedback of student's reactions at remote class to a lecture is very important. For faculty, it is important to control remote classroom camera particularly student's video freely and easily by local control and also it is important for the student located at any one remote classroom to see the interaction video between faculty and student of other remote classroom. However, there is some delay between camera control operations at a remote classroom and actual video image displayed on a local screen. These delays are due to network delay between sender and receiver and due to video compression. To operate remote camera interactively, user must consider these delays while controlling these device. This paper proposes a system for identification and tracking of Active participant with the help of Microsoft Kinect sensor, for the tracking of moving faculty on classroom platform. This paper also proposes solutions for the problems related to real-time interaction between faculty and student and real-time camera control. Here we have discussed latest video encoding and protection technique.

## Hybrid Redundancy Fault Tolerant Codec in Distributed Storage System

- **Status**: ❌
- **Reason**: 분산스토리지 RS erasure + self-repairing 코드, 비-LDPC, 떼어낼 LDPC 기법 없음
- **ID**: ieee:7373781
- **Type**: conference
- **Published**: 3-4 Dec. 2
- **Authors**: Qiao Sun, Ling Nie, Lei Sun +2
- **PDF**: https://ieeexplore.ieee.org/document/7373781
- **Abstract**: Reed-Solomon erasure codes is the most widely used multi-binary codes which could correct the random errors and unexpected errors. Its characteristics include: It has the strongest capability to correct random errors and burst errors under the same coding redundancy and larger coding gain under the same coding efficiency, Secondly, it is close to the limit in the case of short codes and medium codes and it can greatly improve the performance of the error correction when it is combined with the data interleaving technology, Finally, it has strict algebraic structure which is shown as the linear cyclic polynomials. This paper develops a new merge approach of nonlinear self-repairing code and Reed-Solomon codes. When the network condition is good, Reed-Solomon erasure codes is adopted, and in poor network conditions, nonlinear self-repairing codes is used. The efficiency of maintaining redundant data is improved by a few of damaged information. The experiments show that this method can reduce the amount of network transmission data, at the same time it can shorten the amount data of recovery operation and reconstruction time.

## Nonbinary multi-parallel-concatenated single-parity-check (NB-MPCSPC) codes over partial-response channels

- **Status**: ❌
- **Reason**: 비이진(GF) NB-MPCSPC SPC 코드로 비이진 LDPC 제외 원칙 해당
- **ID**: ieee:7459822
- **Type**: conference
- **Published**: 2-4 Dec. 2
- **Authors**: Zhiliang Qin, Anmin Kong, Xueqiang Wang
- **PDF**: https://ieeexplore.ieee.org/document/7459822
- **Abstract**: In this paper, we propose a high-rate nonbinary multi-parallel-concatenated single-parity-check (NB-MPCSPC) code as a low-complexity coding scheme for data storage channels. The proposed scheme is composed of parallel branches of nonbinary SPC codes over a Galois Field (GF) and can be flexibly designed to achieve a wide range of code rates and codeword lengths. The encoding can be directly implemented based on the parity-check matrix; while the decoding is simplified by using the first-order MacLaurin Series to approximate the check-node operation. Compared with its binary counterpart, the proposed nonbinary coding scheme significantly improves bit-error-rate (BER) performance in the error-floor region. Simulation results show that a noticeable performance gain is obtained over conventional binary low-density parity-check (LDPC) codes when used in turbo equalization for partial-response channels.

## EXIT chart behaviour for the hybrid FSO/RF communication system

- **Status**: ❌
- **Reason**: 하이브리드 FSO/RF 통신의 EXIT chart 수렴분석, 무선응용 특이적이며 떼어낼 신규 LDPC 기법 없음
- **ID**: ieee:7459978
- **Type**: conference
- **Published**: 2-4 Dec. 2
- **Authors**: Muhammad N. Khan, Mohsin Jamil
- **PDF**: https://ieeexplore.ieee.org/document/7459978
- **Abstract**: Free space optical (FSO) communication has received attention because of its high bandwidth, less expensive deployment and error prone links. But the FSO signals attenuate significantly due to the atmospheric and varying channel conditions. A hybrid optical/RF (radio frequency) communication system is an alternative communication system to cope with FSO signal attenuations. In such hybrid FSO/RF communication system, power and rate adaptation due to the varying channel conditions is another challenge. We have already proposed a novel puncturing optimization algorithm to solve the adaptation issue. A single pair of encoder and decoder has been suggested in order to avoid additional component cost, computational complexity and synchronisation issues. The extrinsic information transfer (EXIT) chart is well-known technique to measure the convergence of a code. In this research work, we analyse the behaviour of the EXIT chart for the hybrid optical/RF communication system.

## Finite-length EXIT analysis for protograph-coded two-dimensional ISI channels

- **Status**: ❌
- **Reason**: 2D-ISI 자기기록 채널의 protograph 코드 FL-EXIT 수렴분석으로, NAND에 떼어낼 신규 바이너리 LDPC 디코더/구성 기법 없음
- **ID**: ieee:7459821
- **Type**: conference
- **Published**: 2-4 Dec. 2
- **Authors**: Yi Fang, Guojun Han, Yong Liang Guan +1
- **PDF**: https://ieeexplore.ieee.org/document/7459821
- **Abstract**: In this paper, we consider the protograph low-density parity-check (LDPC) codes in two-dimensional inter two-dimensional (2D) intersymbol interference (ISI) channels, which are widely used in modeling ultra-high-density magnetic recoding systems. In particular, we study the convergence and error performance of protograph codes over 2D-ISI channels. We modify the finite-length (FL) extrinsic information transfer (EXIT) algorithm for the sake of facilitating the convergence analysis of protograph codes. Through the FL-EXIT analyses and simulated results, we observe that the regular column-weight-3 (CW-3) code is superior to the protograph codes optimized for one-dimensional (1D) ISI channels, e.g., the 1D-ISI protograph code. Accordingly, the 1D-ISI protograph code may not be served as a good candidate for use in ultra-high-density data storage systems.

## A low-complexity Gaussian message passing iterative detector for massive MU-MIMO systems

- **Status**: ❌
- **Reason**: massive MU-MIMO 검출용 Gaussian message passing으로 LDPC ECC 디코더 아님, 떼어낼 코드 ECC 기법 없음
- **ID**: ieee:7459842
- **Type**: conference
- **Published**: 2-4 Dec. 2
- **Authors**: Lei Liu, Chau Yuen, Yong Liang Guan +2
- **PDF**: https://ieeexplore.ieee.org/document/7459842
- **Abstract**: This paper considers a low-complexity Gaussian Message Passing Iterative Detection (GMPID) method over a pairwise graph for a massive Multiuser Multiple-Input Multiple-Output (MU-MIMO) system, in which a base station with M antennas serves K Gaussian sources simultaneously. Both K and M are large numbers and we consider the cases that K < M in this paper. The GMPID is a message passing algorithm based on a fully connected loopy graph, which is well known that it is not convergent in some cases. In this paper, we first analyse the convergence of GMPID. Two sufficient conditions that the GMPID converges to the Minimum Mean Square Error (MMSE) detection are proposed. However, the GMPID may still not converge when K/M > (√2 − l)2. Therefore, a new convergent GMPID with equally low complexity called SA-GMPID is proposed, which converges to the MMSE detection for any K < M with a faster convergence speed. Finally, numerical results are provided to verify the validity and accuracy of the proposed theoretical results.

## Multi-source erasure networks with source precoding and random linear network coding

- **Status**: ❌
- **Reason**: random linear network coding 기반 erasure network 용량 달성, LDPC ECC 디코더/구성 기법 없음
- **ID**: ieee:7459897
- **Type**: conference
- **Published**: 2-4 Dec. 2
- **Authors**: Xiaoli Xu, Yong Zeng, Yong Liang Guan
- **PDF**: https://ieeexplore.ieee.org/document/7459897
- **Abstract**: In this paper, we show that the capacity of multi-source single-sink erasure networks can be asymptotically achieved by employing random linear network coding at the intermediate nodes over a sufficiently large number of time extensions. The main idea is to model the resulting network as a finite-field linear deterministic multiple-access channel (MAC), and show that linear precoding at the source nodes is capacity-achieving. Since linear processing is performed at all the source and intermediate nodes, desired symbols can be decoded at the sink node by simply solving a set of linear equations. The result has also been extended to multi-source wireless erasure networks which incorporate the broadcast nature of wireless transmissions.

## File distribution in wireless broadcast network: A unified performance comparison

- **Status**: ❌
- **Reason**: 무선 브로드캐스트 파일분배 성능비교 서베이성, 떼어낼 LDPC ECC 기법 없음
- **ID**: ieee:7459898
- **Type**: conference
- **Published**: 2-4 Dec. 2
- **Authors**: Xiaoli Xu, Yong Liang Guan, Chee-Cheon Chui
- **PDF**: https://ieeexplore.ieee.org/document/7459898
- **Abstract**: In this paper, we study a class of wireless broadcast networks where the source intends to send a common file to a group of closely-located receivers. In such networks, reliable file distribution can be achieved either via source retransmissions or user cooperations based on peer-to-peer communications. Various existing schemes are reviewed and compared in terms of feedback load, implementation complexity, coding overhead and transmission efficiency. Extensive computer simulations are performed to compare their efficiency under different channel conditions.

## Reconstruct LDPC codes in an error-free environment

- **Status**: ❌
- **Reason**: 에러프리 환경에서 패리티검사행렬 복원(코드 인식/리버스엔지니어링). ECC 디코더/구성/HW 기여 아님.
- **ID**: ieee:7490941
- **Type**: conference
- **Published**: 19-20 Dec.
- **Authors**: Xin Bao, Yuanling Huang, WenYa Gan +1
- **PDF**: https://ieeexplore.ieee.org/document/7490941
- **Abstract**: This paper presents two algorithms to recover LDPC codes in an error-free environment. Both algorithms reconstruct the sparse parity-check matrices of LDPC codes based on elementary row transformation, and are equivalent to recognize LDPC codes. The first one is appropriate to the LDPC codes whose parity-check matrices have the double-diagonal structure; the second one is a general algorithm that ensures the second-best solution for every type of LDPC codes. Simulation results show that, these algorithms work well with most of LDPC standards and protocols, including 802.16e, 802.11n, DVB-S2 GJB7296 and GB20600.

## Reconstruct LDPC codes in a noisy environment

- **Status**: ❌
- **Reason**: 잡음환경 LDPC 부호 블라인드 인식(parity-check 복원) — ECC 디코딩/구성이 아닌 부호 재구성 문제, 떼어낼 기법 없음
- **ID**: ieee:7489889
- **Type**: conference
- **Published**: 18-20 Dec.
- **Authors**: Xin Bao, Yuanling Huang, Guiliang Wang
- **PDF**: https://ieeexplore.ieee.org/document/7489889
- **Abstract**: Focus on the problem of reconstructing LDPC codes in a noisy environment, an algorithm based on Column Elimination Operation, Parity-Check Vector Judgment Criterion and Gradual Row Transformation is proposed, which is used to blind recognize LDPC codes. This algorithm first gets enough dual vectors of the receive codes, then selects real parity-check vectors of the dual-space of LDPC codes, and then, detectives and deletes the error code words. The above steps are iteratively carried out until the original problem is reduced to an easier problem, i.e., blind recognition LDPC codes in an error-free context, and finally obtain the sparse parity-check matrix by using Gradual Row Transformation. The simulation and experiment results show that, this algorithm fits most of LDPC standards, including 802.16e, 802.11n, DVB-S2, GJB7296, GB20600, etc., and it is an effective solution for LDPC codes blind recognition in a noisy environment.

## Low-complexity LDPC decoder for physical layer network coded multi-way wireless relay systems

- **Status**: ❌
- **Reason**: 물리계층 네트워크 코딩 다방향 릴레이용 결합 BF 디코딩 — 네트워크코딩 결합 응용 특이적, NAND ECC로 떼어낼 순수 LDPC 디코더 기법 없음
- **ID**: ieee:7399015
- **Type**: conference
- **Published**: 18-20 Dec.
- **Authors**: Nuwan Balasuriya, Chandika B. Wavegedara
- **PDF**: https://ieeexplore.ieee.org/document/7399015
- **Abstract**: Recently, in multi-way relay systems employing physical-layer network coding (PNC), channel condition-based pair selection for pairwise information exchange has drawn increased attention as it provides improved performance over the alternative approaches such as round-robin scheduling of node pairs. With pairwise information exchange, there is additional time diversity available due to transmission of the same coded information block of most of the nodes twice in two adjacent time slots. This additional time diversity can be exploited to further enhance the system performance by means of joint channel decoding-network coding. To this end, a joint belief propagation (BP)-based channel decoding-network coding algorithm was proposed by us in [9] for the relay node of low density parity check (LDPC)-coded multi-way relay systems. Even though the algorithm of [9] offers much superior performance over separate channel decoding, it is highly computational expensive and may not be suitable for applications in wireless sensor networks. Alternatively, bit-flipping (BF)-based LDPC decoding can be adopted at much lower computational complexity. In this paper, we develop a low complexity joint bit-flipping (BF)-based channel decoding and network coding algorithm for LDPC-based multi-way relay systems. The BER performance of the proposed algorithm is investigated using computer simulation for two commonly used LDPC codes. The simulation results demonstrate that superior BER performance can be achieved using the proposed joint decoding algorithm over separate and independent bit-flipping-based LDPC channel decoding at the relay. The simulation results also verify that our proposed algorithm is capable of harnessing the aforesaid additional time diversity available. Though the performance of the proposed joint decoding algorithm is inferior to the BP-based algorithm of [9], due to its low computationally complexity, this algorithm may be appealing for applications in relay nodes with low computational capabilities and memory constraints.

## Concatenated polar codes based on selective polarization

- **Status**: ❌
- **Reason**: polar 부호 선택적 분극 연접 구조 — 비-LDPC, 디코더 기법이 LDPC BP에 이식 불가
- **ID**: ieee:7494026
- **Type**: conference
- **Published**: 18-20 Dec.
- **Authors**: Dongsheng Wu, Aijun Liu, Qingshuang Zhang +1
- **PDF**: https://ieeexplore.ieee.org/document/7494026
- **Abstract**: In this paper, we propose a selectively polarized concatenation structure for polar codes. We first divide the polarized bit-channels into three types, i.e., good, intermediate and bad bit-channels according to their Bhattacharyya parameter. Then, through combining several information blocks, the intermediate bit-channels are further polarized to enhance polarization rate. Theoretical and numerical results indicate that the proposed scheme achieves the same capacity as original polar codes at the same length, while the bit error rate (BER) performance is better than that of original polar codes as same decoding delay is considered. The polar codes can be used in the cognitive radio system.

## Effectiveness and performance analysis of MC-CDMA system

- **Status**: ❌
- **Reason**: MC-CDMA 시스템 성능분석, LDPC는 부수적 ECC 베이스라인 언급 — 떼어낼 신규 LDPC 기법 없음, 무선 응용 특이적
- **ID**: ieee:7475337
- **Type**: conference
- **Published**: 18-19 Dec.
- **Authors**: Rohini S, Suriyakala C.D
- **PDF**: https://ieeexplore.ieee.org/document/7475337
- **Abstract**: To achieve high data rate, large system capacity and multimedia services the next generation wireless communication system uses a multiple access technique such as Multi Carrier Code Division Multiple Access (MC-CDMA). It is actually the mixture of two efficient techniques such as CDMA and OFDM. The CDMA part enhances the spectrum utilization whereas the OFDM part reduces multipath fading and ISI. The OFDM technique uses narrowband signal to reduce the frequency selective multipath fading because narrowband signal are less sensitive to ISI and frequency selective multipath fading. The spreading sequences used in a CDMA system have an efficient role in interference reduction and spectrum utilization. With the use of efficient spreading sequence the system enjoys low interference. The performance of the system will depend upon the correlation properties and length of the spreading sequences used. In this paper we are suggesting a novel coding technique which may further improve the system performance in terms of bit error rate (BER) with the use of Low Density Parity Check (LDPC) codes as the error correcting code. An intensive comparative study were carried out to compare the performance of MC-CDMA system in terms of BER Vs SNR and PAPR Vs CCDF curves based on the coding techniques such as Walsh-Hadamard (WH) code and Zero Correlation Zone (ZCZ) code.

## An improved design for latency improvement of SCCC system in wireless communication

- **Status**: ❌
- **Reason**: 무선용 직렬연접부호(SCCC) 인코더 지연 개선 — 비-LDPC, mux/demux 구조 추가로 NAND LDPC와 무관
- **ID**: ieee:7475294
- **Type**: conference
- **Published**: 18-19 Dec.
- **Authors**: Manish Kumar, Taranjit Singh
- **PDF**: https://ieeexplore.ieee.org/document/7475294
- **Abstract**: Serial concatenated code (SCC) has drawn lots of attention by its outstanding performance in terms of reduced bit error rate (BER). It is considered that the encoding structure and decoding algorithm are the two crucial parameters for performance improvement of any code system. This paper introduces the modified structure of SCCC encoder design. The addition of a set of de-Multiplexer and multiplexer in the proposed design makes a contribution to the requirement of short delay. Performance comparison of our modified SCCC system with the Original SCCC structure in terms of BER and Latency has been performed. It is researched that modified SCCC design has better latency & marginally poor BER performance as compared to traditional SCCC structure. Hence modified SCCC design can be a better option for low latency applications & a tradeoff between latency and BER is always required while choosing codes in wireless communication.

## Packet size optimization in WSN using LDPC codes

- **Status**: ❌
- **Reason**: WSN 패킷 크기 최적화에 LDPC 부수 사용, 떼어낼 디코더·HW·코드설계 기법 없음
- **ID**: ieee:7443530
- **Type**: conference
- **Published**: 17-20 Dec.
- **Authors**: Daljit Singh, Hartej Singh
- **PDF**: https://ieeexplore.ieee.org/document/7443530
- **Abstract**: In Wireless Sensor Networks energy (WSN) resources are limited. Most of the energy in a WSN is consumed in communication between the sensor nodes. Packet size is one of the important parameter of the wireless communication. Larger packets have low energy consumption per bit. However larger packets are less reliable. This paper studies packet size optimization in a WSN based on energy throughput and reliability metrics and analyzes the effect of using LDPC codes on energy efficiency. Our results show that LDPC codes can give larger optimal packet size and higher energy efficiency in comparison to no error control at higher probability of bit error rate.

## List message passing algorithm for noiseless compressed sensing

- **Status**: ❌
- **Reason**: noiseless 압축센싱 verification-based 복원 알고리즘 — 소스/CS 도메인, LDPC는 성능 상한 비교용일 뿐 떼어낼 채널 ECC 기법 없음
- **ID**: ieee:7415444
- **Type**: conference
- **Published**: 16-19 Dec.
- **Authors**: Francisco Ramirez-Javega, Meritxell Lamarca
- **PDF**: https://ieeexplore.ieee.org/document/7415444
- **Abstract**: We propose a verification-based algorithm for noiseless Compressed Sensing that reconstructs the original signal operating on a sparse graph. The proposed scheme has affordable computational complexity and its performance is significantly better than previous verification-based algorithms and similar to AMP-based algorithms. We also show that the performance of a noiseless compressed sensing scheme when verification-based algorithms and a sparse matrix is employed to reconstruct the original signal can be upper bounded by the performance of a LDPC code employing the same parity matrix when correcting a codeword transmitted through a BEC.

## Convergence analysis of Gaussian belief propagation for distributed state estimation

- **Status**: ❌
- **Reason**: 분산 상태추정용 Gaussian BP 수렴성 이론 — 통신/제어 BP 응용, LDPC BP 디코더 이식 기법 아님
- **ID**: ieee:7402359
- **Type**: conference
- **Published**: 15-18 Dec.
- **Authors**: Tianju Sui, Damian E. Marelli, Minyue Fu
- **PDF**: https://ieeexplore.ieee.org/document/7402359
- **Abstract**: Belief propagation (BP) is a well-celebrated iterative optimization algorithm in statistical learning over network graphs with vast applications in many scientific and engineering fields. This paper studies a fundamental property of this algorithm, namely, its convergence behaviour. Our study is conducted through the problem of distributed state estimation for a networked linear system with additive Gaussian noises, using the weighted least-squares criterion. The corresponding BP algorithm is known as Gaussian BP. Our main contribution is to show that Gaussian BP is guaranteed to converge, under a mild regularity condition. Our result significantly generalizes previous known results on BP's convergence properties, as our study allows general network graphs with cycles and network nodes with random vectors. This result is expected to inspire further investigation of BP and wider applications of BP in distributed estimation and control.

## Informed dynamic scheduling strategies for novel majority-logic decoding of non-binary LDPC codes

- **Status**: ❌
- **Reason**: 비이진(non-binary GF(q)) LDPC majority-logic 디코딩 — 비이진 LDPC 제외
- **ID**: ieee:7391797
- **Type**: conference
- **Published**: 14-16 Dec.
- **Authors**: Xuan Liu, Abbas Jamalipour
- **PDF**: https://ieeexplore.ieee.org/document/7391797
- **Abstract**: Recent studies show that dynamic scheduling using the latest available information is superior to the flooding scheduling. While the existing works on informed dynamic scheduling focus on belief propagation (BP) based algorithm for binary LDPC codes, in this paper we devise novel methods which are appropriate for majority-logic decoding of non-binary LDPC codes. Firstly we propose a low complexity extrinsic message based decoding algorithm for non-binary LDPC codes. The novelty of this decoding algorithm lies in that we compute extrinsic messages and iteratively update the messages in every iteration. Then we propose a dynamic scheduling schemes specifically designed for majority-logic decoding of non-binary LDPC codes. The proposed scheduling method, named informed dynamic scheduling, can achieve better performance compared with the layered and the flooding schemes.

## Algebraic constructions of quasi-cyclic LDPC codes based on generators

- **Status**: ❌
- **Reason**: QC-LDPC 대수적 구성이나 표준 multiplicative/additive dispersion 수준, 새 이식 기여 약함(애매하나 표준 구성)
- **ID**: ieee:7391757
- **Type**: conference
- **Published**: 14-16 Dec.
- **Authors**: Ningbo Zhang, Rui Zhang, Guixia Kang +1
- **PDF**: https://ieeexplore.ieee.org/document/7391757
- **Abstract**: This paper puts forward two novel algebraic construction of quasi-cyclic low-density parity-check(QC-LDPC) codes. The two constructions are achieved on multiplicative and additive matrix dispersions of two specified base matrices, which are constructed based on multiplicative and cyclic groups, respectively. In addition, making technique in code construction can also be applied to the two constructions. Simulation results show that codes generated in this paper perform well with iterative decoding over AWGN channel. The codes have advantages over Maykay codes in some aspects of code performances. Meanwhile, a code constructed in this paper converges very fast in iterative decoding, which is an important property in high throughput communication system.

## High rate serially concatenated codes with low error floors

- **Status**: ❌
- **Reason**: Hamming+accumulator 직렬연접 부호 error floor 개선 — 비-LDPC 부호, 부호 비의존 BP 기법 아님
- **ID**: ieee:7391747
- **Type**: conference
- **Published**: 14-16 Dec.
- **Authors**: Bo Liu, Sheng Tong, Qinghua Guo +3
- **PDF**: https://ieeexplore.ieee.org/document/7391747
- **Abstract**: Serial concatenation of Hamming codes and an accumulator has been shown to achieve near capacity performance at high code rates. However, these codes usually exhibit poor error floor performance due to their small minimum distances. To overcome this weakness, we propose to replace the outer Hamming codes by product codes constructed from Hamming codes and single-parity-check codes. In this way, the minimum distance of the outer code can be doubled, which is expected to increase the minimum distance of the serially concatenated code and thus to improve error floor performance. Three-dimensional EXIT chart is used for their convergence analysis and the derived thresholds are shown to be close to Shannon limit. Low weight distance spectrum of the proposed code is also calculated and compared with the original code. Simulation results show that the proposed codes can lower the error floor by two orders of magnitudes without waterfall performance degradation at short block length.

## Design of degrees of distribution of LDS-OFDM

- **Status**: ❌
- **Reason**: LDS-OFDM 차수분포 설계 — 다중접속 시그니처 설계, 채널 ECC 아님, 떼어낼 기법 없음
- **ID**: ieee:7391767
- **Type**: conference
- **Published**: 14-16 Dec.
- **Authors**: Tao Huang, Jinhong Yuan, Xingqing Cheng +1
- **PDF**: https://ieeexplore.ieee.org/document/7391767
- **Abstract**: In this paper, we study the design of low density signature-orthogonal frequency division multiple access (LDS-OFDM). Compare to the conventional OFDMA system, LDS system has some desirable properties that allows system operating at overloaded conditions. LDS-OFDM system has been shown that outperforms the corresponding OFDMA system. In this paper, we focus on the design of the LDS degrees distribution, which has not been addressed in the literature. The goal is to achieve the optimum system load. We propose an iterative optimization procedure by utilizing the EXIT chart. Optimized load has been given in this paper with corresponding LDS spreading parameters. The performance of the designed LDS-OFDM system is evaluated. Monte Carlo based simulations further confirm that the designed LDS-OFDM outperforms the corresponding OFDMA system by up to 10 dB.

## Experimental study of continuous variable quantum key distribution

- **Status**: ❌
- **Reason**: CV-QKD reconciliation에 Turbo code 사용 — 비-LDPC + QKD 정보조정, 떼어낼 디코더/HW 기법 없음
- **ID**: ieee:7492751
- **Type**: conference
- **Published**: 14-16 Dec.
- **Authors**: N. Benletaief, H. Rezig, A. Bouallegue
- **PDF**: https://ieeexplore.ieee.org/document/7492751
- **Abstract**: It has been proven in the literature that the main technological factors limiting the communication rates of quantum cryptography systems by single photon are mainly related to the choice of the encoding method. In fact, the efficiency of the used sources is very limited, at best of the order of a few percent for the single photon sources and the photon counters can not be operated beyond a certain speed and with a low order of detection efficiency. In order to overcome partially these drawbacks, it is advantageous to use continuous quantum states as an alternative to standard encodings based on quantum qubits. In this context, we propose a new reconciliation method based on Turbo codes. Our theoretical model assumptions are supported by experimental results. Indeed, our method leads to a significant improvement of the protocol security and a large decrease of the QBER. The gain is obtained with a reasonable complexity increase. Also, the novelty of our work is that it tested the reconciliation method on a real photonic system under VPItransmissionMaker.

## Efficient RSS measurement in wireless networks based on compressive sensing

- **Status**: ❌
- **Reason**: 압축센싱 기반 무선 RSS 측정 — LDPC/ECC 무관
- **ID**: ieee:7410304
- **Type**: conference
- **Published**: 14-16 Dec.
- **Authors**: Yanchao Zhao, Wenzhong Li, Jie Wu +1
- **PDF**: https://ieeexplore.ieee.org/document/7410304
- **Abstract**: Collecting the RSS between all pair of nodes in the networks is very significant for wireless network optimization, localization, interference management and etc. Aside from its significances, the measurement process could be tedious, time consuming and involving human operations. The state-of-art works usually applied the fashion of “measure a few, predict many”, which use measurement calibrated models to generate the RSS for the whole networks. However, this kind of methods still cannot provide accurate results in a short duration and low measurement cost. In addition, they also require careful scheduling of the measurement which is vulnerable to measurement conflict. In this paper, we propose a compressive sensing (CS)-based RSS measurement solution, which is conflict-tolerant, time-efficient and accuracy-guaranteed without any model-calibrate operation. The CS-based solution takes advantage of compressive sensing theory to enable simultaneous measurement in the same channel, which reduces the time cost to the level of O(logN) (where N is the network size) and works well for sparse networks. Extensive experiments based on real data trace are conducted to show the efficiency of the proposed solutions.

## Performance comparison of turbo codes with LDPC codes and with BCH codes for forward error correcting codes

- **Status**: ❌
- **Reason**: turbo/LDPC/BCH 성능 MATLAB 비교 — 표준 부호 단순 비교, 신규 디코더/구성/HW 기여 없음
- **ID**: ieee:7449398
- **Type**: conference
- **Published**: 13-14 Dec.
- **Authors**: Mohammed Hasan Alwan, Mandeep Singh, Hussain Falih Mahdi
- **PDF**: https://ieeexplore.ieee.org/document/7449398
- **Abstract**: In the field of communication, one of the most thriving and prevalent subject is the channel coding. Channel coding generally deals with the bandwidth which is the bit-rate or information storage capacity. It is a technical field which relies heavily on cost. In fact, it is undeniable that cost is the most crucial element in every system. Nowadays, together with the latency or time element which is also an equally significant factor, especially in mobile communication. The objective of this paper is to analyse and compare distinctively the three types of codes namely, turbo codes, LDBC codes and BCH codes, all simulated respectively in MATLAB environment. According to the conducted studies, it is evident that the BCH codes are excellent in performance compared to other codes. The turbo code, despite requiring maximum processing to decode the message has fairly good performance as well. Regardless of the level of processing, all the codes possess good & reliable performances compared to other codes.

## Iterative ICI Cancellation in MIMO OFDM WiMAX System with LDPC Channel Coding

- **Status**: ❌
- **Reason**: MIMO OFDM WiMAX ICI 제거 응용, LDPC는 부수 FEC 베이스라인, 떼어낼 LDPC 기법 없음
- **ID**: ieee:7546150
- **Type**: conference
- **Published**: 12-14 Dec.
- **Authors**: Monika Cheema, Sukanya A. Kulkarni
- **PDF**: https://ieeexplore.ieee.org/document/7546150
- **Abstract**: The employment of MIMO OFDM technique constitutes a cost effective approach to high throughput wireless communications. The system performance is sensitive to frequency offset which increases with the doppler spread and causes Intercarrier interference (ICI). ICI is a major concern in the design as it can potentially cause a severe deterioration of quality of service (QoS) which necessitates the need for a high speed data detection and decoding with ICI cancellation along with the intersymbol interference (ISI) cancellation in MIMO OFDM communication systems. Iterative parallel interference canceller (PIC) with joint detection and decoding is a promising approach which is used in this work. The receiver consists of a two stage interference canceller. The co channel interference cancellation is performed based on Zero Forcing (ZF) Detection method used to suppress the effect of ISI in the first stage. The latter stage consists of a simplified PIC scheme. High bit error rates of wireless communication system require employing forward error correction (FEC) methods on the data transferred in order to avoid burst errors that occur in physical channel. To achieve high capacity with minimum error rate Low Density Parity Check (LDPC) codes which have recently drawn much attention because of their error correction performance is used in this system. The system performance is analyzed for two different values of normalized doppler shift for varying speeds. The bit error rate (BER) is shown to improve in every iteration due to the ICI cancellation. The interference analysis with the use of ICI cancellation is examined for a range of normalized doppler shift which corresponds to mobile speeds varying from 5Km/hr to 250Km/hr.

## Joint Source-Channel Coding for First-Order Hidden Markov Source

- **Status**: ❌
- **Reason**: IRA 기반 JSCC + 소스코딩(HMM source) — 소스-채널 결합, 채널 ECC 기법 아님
- **ID**: ieee:7546172
- **Type**: conference
- **Published**: 12-14 Dec.
- **Authors**: Hong Yang, Linbo Qing, Xiaohai He +1
- **PDF**: https://ieeexplore.ieee.org/document/7546172
- **Abstract**: In this paper, a novel Joint Source-Channel Coding scheme based on Irregular Repeat-Accumulate codec is proposed for the transmission of Hidden Markov Source in AWGN scenarios. The encoder structure of the scheme consists of two units, one for source assign and another for encode. The simulation results demonstrate that the proposed scheme have better compression performance than the traditional code model and can exploit the different transmission performance based on four different types sources.

## A Bayesian Approach for Targets Localization Using Binary Sensor Networks

- **Status**: ❌
- **Reason**: LDPC 행렬을 센서망 코드설계/베이지안 위치추정에 사용 — 채널 ECC 아님, 떼어낼 디코더 없음
- **ID**: ieee:7469171
- **Type**: conference
- **Published**: 12-13 Dec.
- **Authors**: Gongjin Lan, Xiaoli Hu, Qi Hao
- **PDF**: https://ieeexplore.ieee.org/document/7469171
- **Abstract**: This paper presents a Bayesian approach to energy efflcient and data-efflcient target localization using binary sensor networks. The novelty of this work lies in that the methods of channel coding (code design, encoding and decoding) are used to solve the target localization problem. First, the binary sensor networks are constructed via Low density parity-check (LDPC) matrices. As a result, the observation space targets is partitioned into many units that encoded into a set of binary codes. Then, when targets move around, the system measurements will be the encoded with those binary codes through OR operations. In the decoding stage, Bayesian inference algorithms are developed to flnd the unit of source target, which is complicated by OR logic operations. Compared with the match pursuit algorithm, the Bayesian approach is more robust against noise. Numerical simulations have demonstrated the advantages of the proposed approach.

## Performance evaluation of DVB-S2 and DVB-S2X systems

- **Status**: ❌
- **Reason**: DVB-S2/S2X 시스템 성능평가, MATLAB 시뮬레이션 비교뿐 — 신규 디코더·구성·HW 기여 없음
- **ID**: ieee:7434305
- **Type**: conference
- **Published**: 10-12 Dec.
- **Authors**: Karim El-Abbasy, Bassant Abdelhamid, Salwa Elramly
- **PDF**: https://ieeexplore.ieee.org/document/7434305
- **Abstract**: Recently, Digital Video Broadcasting (DVB) has evolved to improve the spectrum efficiency of current multimedia communications. This paper summarizes the main features and presents the error performance for the second generation of satellite DVB (DVB-S2) utilizing an upgraded MATLAB simulation model. In addition, the paper makes a validation of the developed simulation model by comparing between model results and field measurements. Furthermore, a new version of DVB-S2 (DVB-S2X) is simulated to evaluate its performance. The validity of simulation is tested by comparing with the standard error performance for different modulation and coding (MODCOD). The results show that the actual bit error rate (BER) of the measured DVB-S2 system is higher than those obtained in simulation due to variations in realistic satellite link channel conditions. The simulation results showed that DVB-S2X improves the capacity and the spectral efficiency at very high signal to noise ratio (SNR) by including a new higher order Amplitude Phase Shift Keying (APSK) modulation. Moreover, the new coding ratios for DVB-S2X were found to increase the granularity for more capacity options, and provide certain MODCOD optimized only for linear satellite channel. Finally, the new smaller roll-off factors added to DVB-S2X increase the bitrate capacity for the same bandwidth, but it needs a high complex filter design.
