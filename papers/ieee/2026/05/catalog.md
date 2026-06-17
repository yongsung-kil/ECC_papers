# IEEE Xplore — 2026-05


## Hardware-Efficient QC-LDPC Decoding Architecture With Reduced Bit-Width and Saturation Management

- **Status**: ✅
- **Reason**: QC-LDPC 디코더 비트폭 축소·포화관리 VLSI 아키텍처 — NAND 디코더에 직접 이식 가능(D)
- **ID**: ieee:11435440
- **Type**: journal
- **Published**: May 2026
- **Authors**: Hyeongseok Moon, In-Cheol Park
- **PDF**: https://ieeexplore.ieee.org/document/11435440
- **Abstract**: In quantized layered low-density parity-check (LDPC) decoding, the saturated a posteriori probability (APP) value prevents extrinsic information from being correctly accumulated and overemphasizes certain error paths, making it necessary to use a larger APP representation. The proposed method compensates for the information loss caused by such saturation and eliminates the need for a larger APP bitwidth, reducing the APP bitwidth to the level of the check-to-variable message while preserving the decoding performance. This compensation is achieved by disabling APP updates when saturation occurs, starting from the iteration identified by the shortest cycles in the parity-check matrix. The proposed control preserves correct message passing and prevents the accumulation of error-path weights in the APP. In the prototype LDPC decoder, the proposed method requires only a lightweight circuit to detect saturation, incurring a negligible area overhead and almost no degradation of processing delay. As a result, the proposed architecture reduces area and power by 15% and 25%, respectively, and achieves a throughput-to-area ratio of 25.08 Gbps/itr/mm2, while maintaining the FER performance of the 7-bit APP representation.

## Enhanced-Throughput Antithetic Sample Generation Architecture for Monte Carlo Simulation

- **Status**: ❌
- **Reason**: Monte Carlo 시뮬용 antithetic 표본생성 HW — LDPC는 BER 시뮬 대상일 뿐, 디코더 HW 아님
- **ID**: ieee:11431593
- **Type**: journal
- **Published**: May 2026
- **Authors**: Kangjoon Choi, In-Cheol Park
- **PDF**: https://ieeexplore.ieee.org/document/11431593
- **Abstract**: Monte Carlo simulation imposes significant computational and hardware costs due to extensive sample generation. While antithetic variates can reduce sample requirements, direct hardware application doubles transformation paths. Based on a point-symmetric inverse cumulative distribution, this brief introduces a hardware architecture that generates antithetic pairs using a single transformation path and a sign inversion, guaranteeing strong negative correlation and effective variance reduction. Implemented on a Xilinx ZCU104 field-programmable gate array (FPGA), the architecture doubles throughput with minimal hardware overhead. In Monte Carlo bit error rate (BER) simulation for an 802.11n LDPC code, the proposed architecture maintains accuracy while achieving a  $2.14\times $  to  $3.62\times $  speed gain in random-variable generation.

## Toward a Practical Key Generation System for V2X Communications

- **Status**: ❌
- **Reason**: V2X 무선 키생성/보안 응용 — LDPC는 키일치용 부수 언급, 이식 가능 기법 없음
- **ID**: ieee:11278625
- **Type**: journal
- **Published**: May 2026
- **Authors**: Hua Fu, Linning Peng, Junqing Zhang +3
- **PDF**: https://ieeexplore.ieee.org/document/11278625
- **Abstract**: The vehicle to everything (V2X) serves as a crucial foundation for future intelligent transportation systems. Security concerns within the V2X have garnered significant attention and key generation from wireless channels have emerged as a promising technique. However, applying key generation to V2X is quite challenging because the fast moving vehicles result in very small coherence time and impact channel measurements correlation. This paper designed a practical V2X key generation by enhancing channel state information (CSI) reciprocity and carried out extensive experimental evaluation. In particular, the designed key generation consists of channel probing, CSI preprocessing, CSI compensation and key establishment. In the channel probing, we deliberately reduced the time delay between uplink and downlink transmissions, to allow almost simultaneous measurements. We then carefully designed CSI preprocessing to remove hardware carrier leakage and eliminate noise effects. Furthermore, we devised CSI compensation by using interpolation or deep learning prediction to further improve the reciprocity. Finally, key establishment converted the measured CSI into binary sequences and reconcile on a common key via low-density parity-check (LDPC) code. We adopted universal software radio peripheral (USRP) X310 platforms for channel measurements and implemented the above algorithms. We carried out extensive experiments in real-road environments with various vehicle speeds. These carefully designed algorithms enabled our system working robustly even in high mobility scenarios, e.g., 40 km/h. Experimental results demonstrated common and random key can be generated with a key block error rate (BER) less than 0.1.

## Efficient and Resilient Packet Recovery for Federated Learning via Approximation

- **Status**: ❌
- **Reason**: 연합학습 패킷복구 저랭크근사+네트워크코딩 — LDPC ECC 아님, 채널코딩 디코더 기법 없음
- **ID**: ieee:11267083
- **Type**: journal
- **Published**: May 2026
- **Authors**: Jungmin Kwon, Hyunggon Park
- **PDF**: https://ieeexplore.ieee.org/document/11267083
- **Abstract**: To alleviate network congestion resulting from packet retransmission in Federated Learning (FL) systems, the User Datagram Protocol (UDP) has been adopted. However, data loss under UDP inevitably degrades FL performance, as learning is sensitive to incomplete model parameters. This paper addresses such degradation by proposing a low-rank approximation–based parameter transmission method for FL. This approach decomposes model parameters at the transmitter to extract dominant singular values, which are essential for accurate approximation of the model parameters at the receiver. Although the selective delivery of singular values and vectors reduces communication overhead, their loss would cause severe performance degradation, making it essential to employ protection mechanisms. Therefore, to protect the extracted singular values and vectors, we use Systematic Network Coding (SysNC). The SysNC with low-rank approximation can recover original information under a packet loss environment, enhancing robustness against partial loss during the transmission of model parameters. Theoretical analysis and experiments confirm its effectiveness. As an example from our experiments, with a packet loss ratio of $p=0.1$p=0.1, the proposed method achieves over 96% of the accuracy observed in the packet loss-free case, while reducing the end-to-end delay for model parameter transmission by approximately 50% compared to a UDP baseline.

## A Decorrelation-Based Fused Initial Key Generation and Joint Key Agreement Mechanism for V2V Communication

- **Status**: ❌
- **Reason**: V2V 물리계층 키생성/보안 응용 — LDPC는 키일치용 부수 언급, 떼어낼 디코더/HW 기법 없음
- **ID**: ieee:11240567
- **Type**: journal
- **Published**: May 2026
- **Authors**: Jianpo Li, Danni Li, Qi Xu
- **PDF**: https://ieeexplore.ieee.org/document/11240567
- **Abstract**: This paper addresses the issues of low entropy, low quantization efficiency, and error correction in physical layer key generation (PLKG) in high-speed vehicular networks. It proposes a decorrelation-based fused initial key generation and joint key agreement mechanism for V2V communication. First, the Karhunen-Loève (K-L) transformation is used to decorrelate the amplitude of the channel state information, and the phase features are incorporated to construct a high-entropy random source. Next, the ACQG-CDF algorithm is proposed, which significantly enhances the key generation rate (KGR) by dynamically adjusting the threshold and using Gray code encoding. An LDPC-Polar key agreement method is designed to achieve fast error correction and fine-tuning, thereby reducing the key disagreement rate (KDR). Simulation results show that the KGR of the ACQG-CDF algorithm is at least 29% higher than that of the DRL algorithm, resulting in a total runtime reduction of approximately 0.095 s. The joint agreement can reduce the KDR to nearly zero within three rounds. This mechanism exhibits high security (the average mutual information is only 0.01 b against passive eavesdropping, and the KDR is $< $ 0.01 with a stable KGR $\geq$ $5.2 \times 10^{5}$ bits/s against active attacks) and strong randomness (key entropy is 0.92–0.98 bits and passes all NIST tests). It also demonstrates good adaptability in various typical V2V scenarios, such as urban areas, highways, and tunnels. Although the computational complexity is moderately high, this mechanism still demonstrates significant advantages in both runtime and memory usage. Finally, the advantages of the proposed mechanism are visually presented through a radar chart. The results demonstrate that the mechanism performs exceptionally well in terms of key quality, generation efficiency, security, and randomness, making it particularly suitable for low-latency, high-rate, high-speed vehicular networks.

## Leveraging Overfitting for Low-Complexity and Modality-Agnostic Joint Source-Channel Coding

- **Status**: ❌
- **Reason**: joint source-channel coding(JSCC) 신경망 — 소스 코딩 결합으로 채널 ECC 디코더로 떼어낼 기법 없음
- **ID**: ieee:11460387
- **Type**: conference
- **Published**: 3-8 May 20
- **Authors**: Haotian Wu, Gen Li, Pier Luigi Dragotti +1
- **PDF**: https://ieeexplore.ieee.org/document/11460387
- **Abstract**: This paper introduces Implicit-JSCC, a novel overfitted joint source–channel coding paradigm that directly optimizes channel symbols and a lightweight neural decoder for each source. This instance-specific strategy eliminates the need for training datasets or pre-trained models, enabling a storage-free, modality-agnostic solution. As a low-complexity alternative, Implicit-JSCC achieves efficient image transmission with around 1000× lower decoding complexity, using as few as 607 model parameters and 641 multiplications per pixel. This overfitted design inherently addresses source generalizability and achieves state-of-the-art results in the high SNR regimes, underscoring its promise for future communication systems, especially streaming scenarios where one-time offline encoding supports multiple online decoding. Project page: https://eedavidwu.github.io/Implicit-JSCC/

## On the Role of Extrinsic Value Exchange in Expectation Propagation for Coded MIMO Systems

- **Status**: ✅
- **Reason**: EP 검출기 LLR 통계 분석(negentropy로 Gaussianity 평가)으로 디코더 오류정정 능력 향상 — LLR 품질 분석은 NAND LDPC LLR 처리에 이식 가능(C 경계)
- **ID**: ieee:11464434
- **Type**: conference
- **Published**: 3-8 May 20
- **Authors**: Fuga Kobayashi, Takumi Takahashi, Hideki Ochiai
- **PDF**: https://ieeexplore.ieee.org/document/11464434
- **Abstract**: This paper investigates the statistical properties of log-likelihood ratios (LLRs) at the output of an iterative signal detector based on expectation propagation (EP), highlighting the role of moment matching (MM)-based extrinsic value exchange in coded systems. Prior studies have mainly examined convergence behavior in asymptotic regimes; however, EP’s advantage is not always evident in practical finite-size uncoded multi-input multi-output (MIMO) detection, where probabilistic data association (PDA), which lacks extrinsic value exchange, can perform comparably to or even better than EP. In contrast, when channel coding is applied, EP consistently outperforms PDA. To explain this, we analyze the statistical properties of demodulator output LLRs and show that extrinsic value exchange not only ensures inter-iteration independence but also enhances the Gaussianity of LLRs. We quantify this effect using negentropy and demonstrate its benefit in improving the decoder’s error-correcting capability, thereby establishing the superiority of EP in coded systems.

## Spatially-Coupled OTFS Systems via Block Markov Superposition Transmission

- **Status**: ✅
- **Reason**: Spatially-Coupled LDPC 구성+BMST, EXIT 차트 기반 SC 임계 최적화 — SC-LDPC 코드 설계 기법 이식 가능(E)
- **ID**: ieee:11464769
- **Type**: conference
- **Published**: 3-8 May 20
- **Authors**: Jiayi Yang, Shuangyang Li, Qianfan Wang +4
- **PDF**: https://ieeexplore.ieee.org/document/11464769
- **Abstract**: This paper investigates a novel spatially coupled orthogonal time frequency space (SC-OTFS) transmission scheme by integrating block Markov superposition transmission (BMST) with OTFS modulation. We first statistically analyze the distribution of detector mutual information across coded blocks and establish a decoding-threshold-based lower bound to characterize the asymptotic performance of conventional LDPC-coded OTFS systems. The analysis reveals that increasing the code length yields only marginal coding gains in typical doubly-selective channels with limited resolvable paths. Motivated by this observation, we propose an SC-OTFS system in which a portion of each previously coded block is superimposed onto the current block and subsequently modulated using OTFS, thereby exploiting both coding gain and inter-block diversity gain in high-mobility channels. Furthermore, an extrinsic information transfer (EXIT) chart analysis is developed for the SC-OTFS system, which enables optimization of the critical superposition fraction based on decoding thresholds. Simulation results demonstrate that this optimization leads to a significant performance improvement, achieving more than 3 dB gain over conventional 5G LDPC-coded OTFS systems.

## Binary Modulation on Conjugate-Reciprocal Zeros (MOCZ) with List Decoding for Unknown Channel Length

- **Status**: ❌
- **Reason**: MOCZ 비동기 변조+list decoding, LDPC는 통상 BP로 부수 언급 — 떼어낼 신규 디코더/코드 기법 없음
- **ID**: ieee:11460430
- **Type**: conference
- **Published**: 3-8 May 20
- **Authors**: Stephan Pfletschinger, Christian Reich, Monica Navarro
- **PDF**: https://ieeexplore.ieee.org/document/11460430
- **Abstract**: MOCZ (modulation on conjugate-reciprocal zeros) has been introduced as a non-coherent communication scheme for short packets over multi-path channels which does not require channel estimation at the receiver. In this paper, we combine MOCZ with state-of-the-art channel codes and address the problem of the unknown length of the channel impulse response by list decoding. Two criteria for the message selection from the list are evaluated and we observe that LDPC coding with the usual belief-propagation decoding performs near-optimum for realistic packet sizes.

## Low-Bandwidth High-Fidelity Speech Transmission with Generative Latent Joint Source-Channel Coding

- **Status**: ❌
- **Reason**: 생성형 latent JSCC 음성전송 — 소스 코딩 결합, NAND 채널 ECC로 이식할 기법 없음
- **ID**: ieee:11461563
- **Type**: conference
- **Published**: 3-8 May 20
- **Authors**: Guangkuan Li, Shengshi Yao, Sixian Wang +3
- **PDF**: https://ieeexplore.ieee.org/document/11461563
- **Abstract**: Existing speech joint source-channel coding (JSCC) methods show advantages in robustness, however, when it goes to extreme-low bandwidth, its perceptual quality drops sharply. This poses severe challenges for high-fidelity speech transmission over bandwidth-limited weak networks. To tackle this, we propose a new Generative Latent JSCC (GL-JSCC) framework. It performs JSCC in the generative latent space learned by a residual vector quantization generative adversarial network (RVQ-GAN), instead of in the source space. Our generative latent code exhibits higher sparsity and better alignment with human perception, and generative modeling in the latent space provides an additional prior for better quality in low bandwidth. Moreover, a three-stage progressive training strategy is given to ensure effective model alignment and training. Extensive experiments demonstrate that GL-JSCC achieves robust, high-quality speech transmission across a range of low SNR and bandwidth settings. Our scheme achieves the same perceptual quality while saving up to 60% of the bandwidth compared to Opus + 5G LDPC transmission.

## Modeling and Optimization of Noise-Tolerant Coding Algorithms for 6G-oriented Communication

- **Status**: ❌
- **Reason**: 6G용 fountain(LT/Raptor)·LDPC 비교 분석으로 erasure 채널 이론평가 중심, NAND로 이식할 디코더/HW/구성 기법 없음
- **ID**: ieee:11537117
- **Type**: conference
- **Published**: 21-23 May 
- **Authors**: Sergii Dunaiev, Stanislav Milevskyi, Iryna Aksonova +3
- **PDF**: https://ieeexplore.ieee.org/document/11537117
- **Abstract**: The relevance of the study is due to the transition to 6G-oriented networks, which are characterized by ultra-high data rates, minimal delays, and operation in heterogeneous and unstable channels. Under such conditions, traditional methods of noise-tolerant coding lose their effectiveness, which requires adaptive and self-tuning information recovery algorithms. The article analyzes the impact of random, impulse and packet interference and packet erasures on transmission reliability. The characteristics of LT-, LDPC- and Raptor codes are compared, and the conditions for using maximum likelihood decoding for fountain codes are also studied. Architectural models of fountain coding systems are proposed and a step-bystep simulation model for evaluating performance is developed, on the basis of which the Raptor coding algorithm is improved. The proposed simulation framework establishes a theoretical basis for evaluating the probability of message recovery, redundancy, and transmission delay compared to classical schemes. Preliminary analytical evaluation suggests the potential effectiveness of the optimized fountain and LDPC algorithms for highly reliable 6 G networks, necessitating further comprehensive numerical validation.

## Would Learning Help? Adaptive CRC-QC-LDPC Selection for Integrity in 5G-NR V2X

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:11532867
- **Type**: conference
- **Published**: 12-14 May 
- **Authors**: Sarah Al-Shareeda, Gulcihan Ozdemir, Arouj Fatima +4
- **PDF**: https://ieeexplore.ieee.org/document/11532867
- **Abstract**: Vehicle-to-everything (V2X) communications impose stringent physical-layer integrity requirements, particularly under short-packet transmission and mobility-induced channel variation. This paper studies whether standard-compliant online selection of Cyclic Redundancy Check (CRC) polynomials and Quasi-Cyclic Low-Density Parity-Check (QC-LDPC) coding rates can reduce silent (undetected) errors in $mathbf{5 G}$ New Radio (5GNR) V2X links. The joint configuration problem is formulated as a lightweight Contextual Bandit (CB) with a small, discrete action space, and a discounted LinUCB policy is evaluated against greedy online adaptation and a conservative fixed baseline. A 5G-NR-compliant physical-layer simulation is developed using Sionna, modeling mobility through time-correlated Rayleigh fading, where vehicle speed governs channel correlation, and non-stationary interference via a two-state Markov process. The learning agent operates on coarse receiver feedback, including a noisy Signal-to-Noise Ratio (SNR) estimate and indicators of burst interference and deep fades, and targets minimization of the Undetected Error Probability ($P_{U E}$) while accounting for the Detected Error Probability ($P_{D E}$). Overall, our objective is to delineate the mobility regimes in which learning-assisted CRC-QC-LDPC configuration improves physical-layer integrity in 5G-NR V2X systems. Our results indicate that learningassisted adaptation is most effective at low to moderate mobility, reducing $P_{U E}$ by up to $\mathbf{5 0 - 7 0 \%}$ relative to greedy selection in the low-SNR regime (-5 to $5 \mathbf{~ d B}$) and approaching the best fixed configuration at higher $E_{b} / N_{0}$. At high mobility ($\geq 180 \mathbf{~ k m} / \mathbf{h}$), fast channel decorrelation weakens temporal predictability, limiting the effectiveness of online learning and reducing performance differences across policies.
