# IEEE Xplore — 2024-03


## Design and Evaluation of Multi-Layer NOMA on NR Physical Layer for 5G and Beyond

- **Status**: ❌
- **Reason**: 5G NR multi-layer NOMA PHY 설계; LDPC는 MCS 평가 구성요소로 부수 언급, 떼어낼 ECC 기법 없음
- **ID**: ieee:10314140
- **Type**: journal
- **Published**: March 2024
- **Authors**: Md Shantanu Islam, Raouf Abozariba, De Mi +3
- **PDF**: https://ieeexplore.ieee.org/document/10314140
- **Abstract**: This paper investigates the integration of multi-layer non-orthogonal multiple access (N-NOMA) into a 5G New Radio (NR) compliant transceiver model, aiming to reveal the full potential of the NOMA technology in practical scenarios. We propose an N-NOMA-aided 5G NR physical layer (PHY) design, where a simplified multi-layer NOMA multiplexer with a one-shot multiplexing technique is developed to reduce the transmitter complexity and thus potential delay for processing the additional NOMA layers. Our design offers a new perspective for the NOMA technology to address various challenging use cases, such as massive machine type communication (mMTC) and enhanced mobile broadband (eMBB) under low signal-to-noise ratio (SNR) regimes. Then, in order to provide a comprehensive error performance evaluation of the proposed N-NOMA PHY design, we take into account various system configurations, e.g., different modulation and coding schemes (MCSs) with low-density parity-check (LDPC) code and different multi-input multi-output (MIMO) configurations. During the evaluation of the proposed design, we uncovered key factors missing from the existing bit error rate (BER) analytical models literature, e.g., the imperfect successive interference cancellation (SIC). The derived BER expressions capture the effect of the SIC errors, which is consistent in our analytical and simulation performance comparison. Through the simulation, we also comprehensively evaluate and discuss the link-level performance of the proposed PHY design.

## Polar Coded Power Domain Non-Orthogonal Multiple Access System: Construction and Optimization

- **Status**: ❌
- **Reason**: Polar coded NOMA 최적화; LDPC는 비교 대상 베이스라인일 뿐, 이식할 LDPC 기법 없음
- **ID**: ieee:10398183
- **Type**: journal
- **Published**: March 2024
- **Authors**: Hongji Cui, Kai Niu, Meijia Ren +1
- **PDF**: https://ieeexplore.ieee.org/document/10398183
- **Abstract**: The generalized polarization phenomenon exists in non-orthogonal multiple access (NOMA) systems. This letter specifically focuses on two-user coding-NOMA systems, which provide a practical joint optimization solution for next-generation mobile communication. In this letter, we employ the finite code length normal approximation bound to establish the connection among error probabilities, power allocation, and code rate allocation in coding-NOMA systems. First, we formulate an optimization problem to minimize error probability, and another one to maximize energy efficiency under a given system error performance for practical scenarios. Then, we derive the relationship between optimal code rates and powers, and then compute suitable power scheme using an iterative algorithm. Finally, we optimize polar coded NOMA systems using polarization subchannels. The proposed optimization scheme exhibits only a 0.5dB deviation from the normal approximation bound at a block error rate of 10−3. Furthermore, the polar coded NOMA scheme outperforms low-density parity-check code (LDPC) coding.

## Rate-Adaptive Coding Mechanism for Semantic Communications With Multi-Modal Data

- **Status**: ❌
- **Reason**: 딥러닝 멀티모달 시맨틱 통신 + rate-adaptive UEP; 채널 ECC 기법 아님, 시맨틱 통신은 원칙 제외
- **ID**: ieee:10327757
- **Type**: journal
- **Published**: March 2024
- **Authors**: Yangshuo He, Guanding Yu, Yunlong Cai
- **PDF**: https://ieeexplore.ieee.org/document/10327757
- **Abstract**: Recently, the ever-increasing demand for bandwidth in multi-modal communication systems requires a paradigm shift. Powered by deep learning, semantic communications are applied to multi-modal scenarios to boost communication efficiency and save communication resources. However, the existing end-to-end neural network (NN) based framework without the channel encoder/decoder is incompatible with modern digital communication systems. Moreover, most end-to-end designs are task-specific and require re- design and re- training for new tasks, which limits their applications. In this paper, we propose a distributed multi-modal semantic communication framework incorporating the conventional channel encoder/decoder. We adopt NN-based semantic encoder and decoder to extract correlated semantic information contained in different modalities, including speech, text, and image. Based on the proposed framework, we further establish a general rate-adaptive coding mechanism for various types of multi-modal semantic tasks. In particular, we utilize unequal error protection based on semantic importance, which is derived by evaluating the distortion bound of each modality. We further formulate and solve an optimization problem that aims at minimizing inference delay while maintaining inference accuracy for semantic tasks. Numerical results show that the proposed mechanism fares better than both conventional communication and existing semantic communication systems in terms of task performance, inference delay, and deployment complexity.

## Semantic-Forward Relaying: A Novel Framework Toward 6G Cooperative Communications

- **Status**: ❌
- **Reason**: 시맨틱 통신 + JSCC 릴레잉; LDPC 언급 없고 떼어낼 ECC 기법 없음
- **ID**: ieee:10388241
- **Type**: journal
- **Published**: March 2024
- **Authors**: Wensheng Lin, Yuna Yan, Lixin Li +2
- **PDF**: https://ieeexplore.ieee.org/document/10388241
- **Abstract**: This letter proposes a novel relaying framework, semantic-forward (SF), for cooperative communications towards the sixth-generation (6G) wireless networks. The SF relay extracts and transmits the semantic features, which reduces forwarding payload, and also improves the network robustness against intra-link errors. Based on the theoretical basis for cooperative communications with side information and the turbo principle, we design a joint source-channel coding algorithm to iteratively exchange the extrinsic information for enhancing the decoding gains at the destination. Surprisingly, simulation results indicate that even in bad channel conditions, SF relaying can still effectively improve the recovered information quality.

## Iterative Successive Nonlinear Self-Interference Cancellation for In-Band Full-Duplex Communications

- **Status**: ❌
- **Reason**: In-band full-duplex 자기간섭 제거 기법; LDPC ECC 무관, 무선 통신 응용 특이적이며 떼어낼 ECC 기법 없음
- **ID**: ieee:10198236
- **Type**: journal
- **Published**: March 2024
- **Authors**: Zhihong Hunter Hong, Liang Zhang, Yiyan Wu +7
- **PDF**: https://ieeexplore.ieee.org/document/10198236
- **Abstract**: In-band full-duplex (IBFD) communications have recently been considered for wireless backhaul in the ultra-high frequency (UHF) band terrestrial broadcast systems since they can double the spectral efficiency compared to conventional half-duplex communications. The inherent challenge of IBFD communication is self-interference (SI), the power leakage from the co-located transmitter to the receiver. For wireless backhaul among transmitter towers, it’s desirable to employ high-order modulation, e.g., 1024QAM or 4096QAM, for higher spectral efficiency. Furthermore, the transmitter emission power is much higher in low radio frequency (RF) bands. Due to the nonlinearity of the transmitter high-power amplifier (HPA), the nonlinear distorted SI becomes a performance-limiting impairment and must be effectively mitigated. Moreover, the SI channel exhibits a large multipath delay spread in these applications, especially in UHF-band terrestrial broadcasting systems where the transmission frequency is lower and the antenna directivity is limited. In this paper, a novel iterative successive nonlinear SI cancellation scheme, based on the previously proposed frequency-domain RF self-interference cancellation (RF-SIC) technique, is presented. The baseline RF-SIC is capable of cancelling SI with a large multipath delay spread. However, the RF-SIC performance is limited by the presence of the remote signal of interest (SOI) in the received signal. This SOI presence, referred to as “intrinsic noise” in the SI channel estimation process, occurs due to foregoing the training phase requirement. The proposed approach in this paper iteratively cancels the “intrinsic noise” and can suppress the nonlinear SI to the receiver noise floor. The proposed technique can be applied to 3rd Generation Partnership Project (3GPP) Integrated Access and Backhaul (IAB) technology to make it more feasible for deployment at the lower frequency band.

## Enhanced Message-Passing Decoding of Degenerate Quantum Codes Utilizing Trapping Set Dynamics

- **Status**: ❌
- **Reason**: 양자 LDPC(surface/toric/bicycle) 디코더; 스태빌라이저·축퇴 등 양자 전용 개념에 의존 - 원칙 제외
- **ID**: ieee:10409156
- **Type**: journal
- **Published**: March 2024
- **Authors**: Dimitris Chytas, Michele Pacenti, Nithin Raveendran +2
- **PDF**: https://ieeexplore.ieee.org/document/10409156
- **Abstract**: In this letter, we propose a novel iterative decoding algorithm that exploits the degenerate nature of three different families of quantum low-density parity-check codes, i.e., surface, toric, and row-degree-4 bicycle codes. Such families of codes share harmful trapping sets that constitute symmetric stabilizers, making it impossible for any parallel-scheduled iterative message-passing decoder to converge even for error patterns of weight as low as two. By biasing subsets of nodes in the symmetric stabilizers, the decoder is able to converge to a valid error pattern. Furthermore, the proposed decoder has low decoding complexity - linear in the code’s blocklength - and a fully parallel schedule, making it suitable for low-latency efficient implementation.

## Optimization of Security Identification in Power Grid Data through Advanced Encryption Standard Algorithm

- **Status**: ❌
- **Reason**: AES 암호화 기반 전력망 보안; LDPC·ECC 무관
- **ID**: ieee:10964000
- **Type**: journal
- **Published**: March 2024
- **Authors**: Biaoqi Li, Min Xu, Yuan Zhou +2
- **PDF**: https://ieeexplore.ieee.org/document/10964000
- **Abstract**: With the increasing reliance on digital technologies in power grid systems, ensuring the security and confidentiality of data has become paramount. This study focuses on optimizing security identification processes in power grid data using the Advanced Encryption Standard (AES) algorithm. The research explores the application of AES to enhance data protection and improve the accuracy and efficiency of security identification techniques. By implementing AES encryption, the study aims to fortify the security measures within the power grid infrastructure, safeguard sensitive information, and mitigate potential threats. The findings provide insights into the benefits of AES-based security optimization, contributing to the advancement of data security in power grid operations.

## Ising Model on Locally Tree-Like Graphs: Uniqueness of Solutions to Cavity Equations

- **Status**: ❌
- **Reason**: Ising model cavity equation/BP fixed point 유일성 순수 이론; 디코더/HW/코드구성으로 안 이어지는 이론 bound
- **ID**: ieee:10254591
- **Type**: journal
- **Published**: March 2024
- **Authors**: Qian Yu, Yury Polyanskiy
- **PDF**: https://ieeexplore.ieee.org/document/10254591
- **Abstract**: In the study of Ising models on large locally tree-like graphs, in both rigorous and non-rigorous methods one is often led to understanding the so-called belief propagation distributional recursions and its fixed points. We prove that there is at most one non-trivial fixed point for Ising models with zero or certain random external fields. Previously this was only known for sufficiently “low-temperature” models. Our main innovation is in applying information-theoretic ideas of channel comparison leading to a new metric (degradation index) between binary-input-symmetric (BMS) channels under which the Belief Propagation (BP) operator is a strict contraction (albeit non-multiplicative). A key ingredient of our proof is a strengthening of the classical stringy tree lemma of Evans-Kenyon-Peres-Schulman (2000). Our result simultaneously closes the following 6 conjectures in the literature: 1) independence of robust reconstruction accuracy to leaf noise in broadcasting on trees; 2) uselessness of global information for a labeled 2-community stochastic block model, or 2-SBM; 3) optimality of local algorithms for 2-SBM under noisy side information; 4) uniqueness of BP fixed point in broadcasting on trees in the Gaussian (large degree) limit; 5) boundary irrelevance in broadcasting on trees; 6) characterization of entropy (and mutual information) of community labels given the graph in 2-SBM.

## Multi-Domain Polarization for Enhancing the Physical Layer Security of MIMO Systems

- **Status**: ❌
- **Reason**: MIMO 물리계층 보안 + 다중도메인 polarization 키생성; LDPC 무관, 무선 보안 응용 특이적
- **ID**: ieee:10311400
- **Type**: journal
- **Published**: March 2024
- **Authors**: Luping Xiang, Yao Zeng, Jie Hu +2
- **PDF**: https://ieeexplore.ieee.org/document/10311400
- **Abstract**: A novel Physical Layer Security (PLS) framework is conceived for enhancing the security of wireless communication systems by exploiting multi-domain polarization in Multiple-Input Multiple-Output (MIMO) systems. We design a sophisticated key generation scheme based on multi-domain polarization and the corresponding receivers. An in-depth analysis of the system’s secrecy rate is provided, demonstrating the confidentiality of our approach in the presence of eavesdroppers having strong computational capabilities. More explicitly, our simulation results and theoretical analysis corroborate the advantages of the proposed scheme in terms of its bit error rate (BER), block error rate (BLER), and maximum achievable secrecy rate. Our findings indicate that the innovative PLS framework effectively enhances the security and reliability of wireless communication systems. For example, in a  $4\times 4$  MIMO setup, the proposed PLS strategy exhibits an improvement of 2dB compared to conventional MIMO, systems at a BLER of  $2\cdot 10^{-5}$  while the eavesdropper’s BLER reaches 1.

## Hardware-Level Secure Coding

- **Status**: ❌
- **Reason**: Turbo code 기반 GF(4) 암호화+ECC 결합 보안 — LDPC 아니고 비이진(GF(4)) 컨볼루션, NAND 이식 불가
- **ID**: ieee:10025681
- **Type**: journal
- **Published**: March 2024
- **Authors**: Raúl Eduardo Lopresti, Jorge Castiñeira Moreira
- **PDF**: https://ieeexplore.ieee.org/document/10025681
- **Abstract**: In this letter, a combined encryption and error-control coding scheme based on turbo codes (TCs) is proposed to enhance the security of the transmission. It relies on convolutional encoders that operate over Galois fields  ${\textrm {GF}}(4)$  and include variable encryption polynomials, whose coefficients are randomly selected every  $L$  steps from a set of optimal polynomials. This type of encoder has been studied in previous papers, where a certain correspondence between the randomness of the encoded sequence and the performance of the TC was conjectured. In this work, a scheme with a varying length  $L$  is proposed to increase the output randomness and, therefore, the security of the sequence to be transmitted. That is to say, the number of steps  $L$ , over which one of the polynomials is iterated, is a random variable. The randomness of the output and the security of the TC are quantified using differential block entropy, showing that it is possible to improve the security of the transmitted data without compromising the corresponding bit error rate (BER).

## A Recursive Soft-Input Soft-Output Decoding Algorithm

- **Status**: ❌
- **Reason**: 선형 블록부호용 재귀 trellis 기반 MAP(SISO) 디코딩; LDPC가 아닌 trellis/BCJR 계열, NAND LDPC 이식성 낮음 (대상 부호·구조 상이)
- **ID**: ieee:10323282
- **Type**: journal
- **Published**: March 2024
- **Authors**: Liudmila Karakchieva, Peter Trifonov
- **PDF**: https://ieeexplore.ieee.org/document/10323282
- **Abstract**: A reduced complexity symbolwise maximum a posteriori probability (MAP) decoding algorithm for linear block codes is presented. This algorithm is based on the recursive trellises and performs two passes over the recursion tree. Probability-domain and Log-Max implementations are considered. Numeric results show that the proposed method has lower complexity compared to other known recursive algorithms and the classical BCJR algorithm. The complexity analysis for random codes is provided.

## Performance Analysis and Approximate Message Passing Detection of Orthogonal Time Sequency Multiplexing Modulation

- **Status**: ❌
- **Reason**: OTSM 변조 + AMP/VAMP-EM 검출기 논문; LDPC는 turbo 수신기 베이스라인으로 부수 언급, NAND LDPC ECC에 떼어낼 디코더/HW/코드설계 기여 없음
- **ID**: ieee:10183832
- **Type**: journal
- **Published**: March 2024
- **Authors**: Zeping Sui, Shefeng Yan, Hongming Zhang +4
- **PDF**: https://ieeexplore.ieee.org/document/10183832
- **Abstract**: In orthogonal time sequency multiplexing (OTSM) modulation, the information symbols are conveyed in the delay-sequency domain upon exploiting the inverse Walsh Hadamard transform (IWHT). It has been shown that OTSM is capable of attaining a bit error ratio (BER) similar to that of orthogonal time-frequency space (OTFS) modulation at a lower complexity, since the saving of multiplication operations in the IWHT. Hence we provide its BER performance analysis and characterize its detection complexity. We commence by deriving its generalized input-output relationship and its unconditional pairwise error probability (UPEP). Then, its BER upper bound is derived in closed form under both ideal and imperfect channel estimation conditions, which is shown to be tight at moderate to high signal-to-noise ratios (SNRs). Moreover, a novel approximate message passing (AMP) aided OTSM detection framework is proposed. Specifically, to circumvent the high residual BER of the conventional AMP detector, we proposed a vector AMP-based expectation-maximization (VAMP-EM) detector for performing joint data detection and noise variance estimation. The variance auto-tuning algorithm based on the EM algorithm is designed for the VAMP-EM detector to further improve the convergence performance. The simulation results illustrate that the VAMP-EM detector is capable of striking an attractive BER vs. complexity trade-off than the state-of-the-art schemes as well as providing a better convergence. Finally, we propose AMP and VAMP-EM turbo receivers for low-density parity-check (LDPC)-coded OTSM systems. It is demonstrated that our proposed VAMP-EM turbo receiver is capable of providing both BER and convergence performance improvements over the conventional AMP solution.

## Employing Efficient Decoding Algorithms to Reduce Bit Error Rates in 5G Applications and Beyond

- **Status**: ❌
- **Reason**: 5G/6G에서 BCH/RS/LDPC/Turbo/Polar BER 비교 시뮬레이션만, 새 디코더/구성 기여 없음 — 표준 부호 단순 비교
- **ID**: ieee:10527925
- **Type**: conference
- **Published**: 29 Feb.-3 
- **Authors**: K. Chandra Sekhar, G. Sateesh Kumar, B.T. Krishna
- **PDF**: https://ieeexplore.ieee.org/document/10527925
- **Abstract**: In 5G and 6G systems, Bit Error Rate (BER) is a critical performance metric for evaluating the dependability and data transmission quality of communication networks. In order to lower BER values, particularly in challenging channel conditions, 5G and 6G systems employ advanced algorithms. These systems commonly employ error-correcting codes like Turbo codes, Polar codes, or LDPC (Low-Density Parity-Check) codes. These next-generation wireless networks can only meet their stringent BER criteria with the aid of adaptive modulation and coding, and Massive Input & Massive Output (MIMO) techniques. In this paper, the bit error rates for various error correction codes, including BCH (Bose Chaudhuri Hocquenghem),Reed Solmon (RS) Codes LDPC, Turbo, and Polar Codes, have been compared. The entire simulation is carried out using MATLAB.

## Performance Evaluation of 3GPP-Standard Driven Polar Coded Modulation for 5G

- **Status**: ❌
- **Reason**: 5G NR Polar 부호화+변조 성능 평가, LDPC 아님이고 떼어낼 ECC 기법 없음
- **ID**: ieee:10527991
- **Type**: conference
- **Published**: 29 Feb.-3 
- **Authors**: Lopamudra Mazumder, Sandip Ghosal
- **PDF**: https://ieeexplore.ieee.org/document/10527991
- **Abstract**: This work provides a comparative study of the 5G new radio (NR) polar coding with different symbol modulation techniques and different delay profiles of NLOS channel. It has been observed that for the same remaining configurations, the block error rate and the block length error rate performances require higher amount of bit to noise ratio in 16-QAM modulation compared to the BPSK and QPSK modulation in both uplink and downlink transmission scenarios. In the next section, the impact of modulation on the signal received in a physical downlink control channel have been studied for different tapped delay profiles. The reported analyses carried out using the 3GPP guideline based 5G new radio model blocks of MATLAB 5G Toolbox can be further utilized for designing standard based 5G waveforms in different practical scenarios.

## Graphical Password Authentication using Image Processing (GPAIP)

- **Status**: ❌
- **Reason**: 그래픽 비밀번호 인증 시스템으로 ECC와 무관
- **ID**: ieee:10498683
- **Type**: conference
- **Published**: 28 Feb.-1 
- **Authors**: N. Sivaranjani, P Sanjana, S Sindhubairavi +1
- **PDF**: https://ieeexplore.ieee.org/document/10498683
- **Abstract**: In today’s digital landscape, passwords are a fundamental part of our online experience, required for accessing a wide range of services. With the increasing use of online platforms, security in authentication methods has become a pressing concern. Graphical password systems have gained attention as a potentially more secure and user-friendly alternative to traditional text-based passwords. Creating such a system is a complex task, as it involves finding the right balance between security and ease of use. The main goal is to develop an authentication system that effectively safeguards personal and financial information from cyber threats and data breaches. This project introduces a novel graphical password approach which is highly resistant to common cyber-attacks like brute force or dictionary attacks that is not only more secure but also more efficient than existing ones.

## Topology-Aware Sparse Factorization in Energy-Based Models: Tori QC-LDPC Codes and Circular Hyperboloid MET QC-LDPC Codes

- **Status**: ❌
- **Reason**: QC-LDPC를 에너지기반모델/Ising 임베딩에 응용하는 토폴로지 연구 — NAND ECC로 떼어낼 새 디코더·구성 기여 없음
- **ID**: ieee:10510073
- **Type**: conference
- **Published**: 27-29 Marc
- **Authors**: Vasiliy S. Usatyuk, Sergey I. Egorov
- **PDF**: https://ieeexplore.ieee.org/document/10510073
- **Abstract**: This study proposed the intersection of Information Theory and Applied Topology, focusing on Codes on Graphs, particularly low-density parity-check (LDPC) codes. By exploiting the connection between the parity check matrix and Markov random fields, we symmetrically embed QC LDPC codes into the barycenters of energy minima within the Ising model. This embedding, enabled by toroidal and circular hyperboloid topologies of negative curvature, associates codewords with extrema and trapping sets with local minima. Strengthening LDPC codes with increased code distance enhances the separation of saddle points, improving the neural network's noise resistance (adversarial robustness) and representation power (capacity). The inherent block and sparse structure of toroidal and hyperboloid topolo-gies streamline KAM stability and preserve negative curvature in high-dimensional invariant quantities. This study aims to merge the KAM theorem, Non-equilibrium Torical Manifold, and Novikov conjectures within LDPC codes. Our constructive approach allows for synthesizing architectures of energy-efficient models tailored to codes on graphs with toric and hyperbolic topologies. We effectively represent Markov random fields in energy-efficient models using sparse block (quasi-cyclic) matrices (tensors) corresponding to hypergraphs (multigraphs), leading to a reduction in trainable parameters and a logarithmic decrease in tensor multiplexing complexity. Applying our approach to factorization problems on dense graphs, network issues, surface meshes, and covariance matrices demonstrates notable improve-ments in reconstruction accuracy using the Frobenius metric (up to 8 orders of magnitude in individual problems).

## Prospects for Application of New Optimization Theory Technologies to the High-Throughput Satellite Communication Systems Design

- **Status**: ❌
- **Reason**: 위성통신용 multithreshold 디코더 일반론 — LDPC 특정 새 기법 없는 최적화 이론 개관
- **ID**: ieee:10510109
- **Type**: conference
- **Published**: 27-29 Marc
- **Authors**: Zolotarev V.V., Ovechkin G.V.
- **PDF**: https://ieeexplore.ieee.org/document/10510109
- **Abstract**: Fundamentally new possibilities of Optimization Theory technologies are analyzed in solving the problem of simple, highly reliable decoding of digital data when transmitted over channels with high noise. Patented fast versions of multithreshold decoders for satellite communication systems are noted. These algorithms are compared with others in classical digital channels according to the triune criterion of “noise immunity-reliability-complexity”. The need to solve various computational problems within the framework of applied coding theory is noted. To do this, it is proposed to use methods from the theory of global functional optimization. It is indicated that appropriate optimization software of various types has been created and can be actively used for the design of decoders for satellite communication systems and for further research.

## Depth-Optimal Addressing of 2D Qubit Array with 1D Controls Based on Exact Binary Matrix Factorization

- **Status**: ❌
- **Reason**: 2D 큐비트 어레이 주소지정(binary matrix factorization). 양자 제어 문제, LDPC ECC 아님
- **ID**: ieee:10546763
- **Type**: conference
- **Published**: 25-27 Marc
- **Authors**: Daniel Bochen Tan, Shuohao Ping, Jason Cong
- **PDF**: https://ieeexplore.ieee.org/document/10546763
- **Abstract**: Reducing control complexity is essential for achieving large-scale quantum computing, particularly on platforms operating in cryogenic environments. Wiring each qubit to a room-temperature control poses a challenge, as this approach would surpass the thermal budget in the foreseeable future. An essential tradeoff becomes evident: reducing control knobs compromises the ability to independently address each qubit. Recent progress in neutral atom-based platforms suggests that rectangular addressing may strike a balance between control granularity and flexibility for $2\mathrm{D}$ qubit arrays. This scheme allows addressing qubits on the intersections of a set of rows and columns each time. While quadratically reducing controls, it may necessitate more depth. We formulate the depth-optimal rectangular addressing problem as exact binary matrix factorization, an NP-hard problem also appearing in communication complexity and combinatorial optimization. We introduce a satisfiability modulo theories-based solver for this problem, and a heuristic, row packing, performing close to the optimal solver on various benchmarks. Furthermore, we discuss rectangular addressing in the context of fault-tolerant quantum computing, leveraging a natural two-level structure.

## Optical Beam Steerable and Beam Dividable of Non-Orthogonal Multiple Access (NOMA) Signal with Low-Density Parity-Check (LDPC) for Multi-User Optical Wireless Communication System

- **Status**: ❌
- **Reason**: 광무선 OWC NOMA 실험 데모, LDPC는 부수 언급일 뿐 떼어낼 디코더·코드설계·HW 기법 없음
- **ID**: ieee:10526772
- **Type**: conference
- **Published**: 24-28 Marc
- **Authors**: Yin-He Jian, Chih-Chun Wang, Jian-Wen Chen +3
- **PDF**: https://ieeexplore.ieee.org/document/10526772
- **Abstract**: We propose a spatial-light-modulator (SLM)-enabled optical beam steerable and beam dividable optical-wireless-communication (OWC) using orthogonal-frequency-division-multiplexing non-orthogonal-multiple-access (OFDM-NOMA) and low-density-parity-check (LDPC). Three-layer successive-interference-cancellation (SIC) is experimentally demonstrated.

## Low-Complexity Non-Binary Forward Error Correction for Lattice-Based 4D Constellations

- **Status**: ❌
- **Reason**: 512-ary 비이진(non-binary) LDPC 디코딩 — 비이진 LDPC는 기준상 즉시 제외
- **ID**: ieee:10527041
- **Type**: conference
- **Published**: 24-28 Marc
- **Authors**: Sebastian Stern, Mahmoud Sallam, Robert F.H. Fischer
- **PDF**: https://ieeexplore.ieee.org/document/10527041
- **Abstract**: Low-complexity non-binary LDPC decoding is studied for a 512-ary lattice-based 4D Welti constellation. In an 800ZR scenario, more than 1 dB SNR gain is obtained over DP-16QAM and binary FEC at fixed symbol rate.

## Performance Evaluation and Optimization of LDPC FEC for 100 Gbps Coherent Passive Optical Networks

- **Status**: ❌
- **Reason**: 기존 PON용 LDPC FEC를 clipping 최적화로 평가만, 새 디코더·구성·HW 기여 없음 — 표준 재사용
- **ID**: ieee:10526517
- **Type**: conference
- **Published**: 24-28 Marc
- **Authors**: Qun Zhang, Haipeng Zhang, Zhensheng Jia
- **PDF**: https://ieeexplore.ieee.org/document/10526517
- **Abstract**: Using both simulation and experimental data, we investigate performance of the LDPC FEC code used in current 25G/50G PONs through clipping optimization for coherent PONs, demonstrating its feasibility for future PON’s applications

## Transoceanic-Class WDM/SDM Transmission of PDM-QPSK Signals over Coupled 12-Core Fiber

- **Status**: ❌
- **Reason**: 코어간 광섬유 장거리 전송 데모, FEC는 baseline 언급뿐 이식 가능 LDPC 기법 없음
- **ID**: ieee:10527113
- **Type**: conference
- **Published**: 24-28 Marc
- **Authors**: Manabu Arikawa, Kohki Shibahara, Taiji Sakamoto +4
- **PDF**: https://ieeexplore.ieee.org/document/10527113
- **Abstract**: We demonstrated long-haul transmission of 32-Gbaud PDM-QPSK over coupled 12-core fiber with standard cladding diameter. Error-free transmission after FEC was achieved up to 7280 km. The estimated rms MDL per 52-km span was 0.3 dB.

## 402 Tb/s GMI data-rate OESCLU-band Transmission

- **Status**: ❌
- **Reason**: 전대역 광전송 데이터레이트 기록 논문, LDPC/디코더 기법 없음
- **ID**: ieee:10527148
- **Type**: conference
- **Published**: 24-28 Marc
- **Authors**: B. J. Puttnam, R. S. Luis, I. Phillips +19
- **PDF**: https://ieeexplore.ieee.org/document/10527148
- **Abstract**: We combine 5 doped-fiber amplifier variants with lumped and distribute Raman-amplification to transmit in all of the low-loss transmission bands of silica fibers achieving an SMF record data-rate of 402.2 Tb/s (GMI)-378.9 Tb/s (Decoded) and 37.6 THz transmission bandwidth after 50 km.

## Wideband S, C,+ L-Band Comb Regeneration in Large-Scale Few-Mode MCF Link with Single-Mode Seed Channel

- **Status**: ❌
- **Reason**: 멀티코어 광섬유 콤 전송 논문, LDPC/FEC 자체가 등장하지 않으며 이식 가능 ECC 기법 없음
- **ID**: ieee:10526797
- **Type**: conference
- **Published**: 24-28 Marc
- **Authors**: B. J. Puttnam, D. Orsuti, R. S. Luis +9
- **PDF**: https://ieeexplore.ieee.org/document/10526797
- **Abstract**: We use wideband optical frequency combs covering 134 nm to transmit >336 Tb/s in a single core of a 3-mode multi-core fiber with seed transmission to regenerate synchronized local comb enabling simplified coherent reception.

## Simultaneous IM/DD Data Transmission and High-Rate Secret Key Distribution over a Single C-band Channel

- **Status**: ❌
- **Reason**: 보안 키 분배/암호 — ECC 기법 무관, 보안 도메인 제외
- **ID**: ieee:10526589
- **Type**: conference
- **Published**: 24-28 Marc
- **Authors**: M. Jachura, J. Szlachetka, M. Kucharczyk +4
- **PDF**: https://ieeexplore.ieee.org/document/10526589
- **Abstract**: We demonstrate hierarchical multiscale PAM-4 transmission combining 500 Mbps data transfer with optical-layer cryptographic key distribution at rates 24.14 Mbps and 8.38 Mbps secure against passive eavesdropper advantage 0 dB and 6 dB respectively.

## 1200-km Transmission of 4096-ary Eigenvalue-modulated Signal Using a Neural Network-based Demodulator and SD-FEC

- **Status**: ❌
- **Reason**: 신경망 복조기+SD-FEC 광전송 데모, FEC는 부수 언급 — 떼어낼 LDPC 기법 없음
- **ID**: ieee:10526631
- **Type**: conference
- **Published**: 24-28 Marc
- **Authors**: Ryotaro Harada, Tsuyoshi Yoshida, Daisuke Hisano +2
- **PDF**: https://ieeexplore.ieee.org/document/10526631
- **Abstract**: We experimentally demonstrate the transmission of a 4096-ary eigenvalue-modulated signal using a neural network-based demodulator and SD-FEC. The experimental results indicate a successful operation with an error-free transmission through a 1200-km optical fiber line.

## Air/Water Path Switching with Beam Steering for Water Distance/Turbidity Adaptive Underwater Optical Wireless Communication Network: Concept and Demonstration

- **Status**: ❌
- **Reason**: 수중 광무선통신 빔스티어링 데모 — LDPC/ECC 무관
- **ID**: ieee:10526537
- **Type**: conference
- **Published**: 24-28 Marc
- **Authors**: Kiichiro Kuwahara, Hyuga Nagami, Keita Tanaka +4
- **PDF**: https://ieeexplore.ieee.org/document/10526537
- **Abstract**: We conducted full-duplex class 1 eye-safe transmission experiments, including 4K video demonstrating robust connectivity to maximize transmission capacity under optimal paths by introducing aerial relay nodes within underwater optical wireless communication networks in shallow seas. (tel: +81 87.864.2231, e-mail: kodama.takahiro@kagawa-u.ac.jp).

## 122.6 Tb/s S+C+L Band Unrepeated Transmission over 223 km link with Optimised Bidirectional Raman Amplification

- **Status**: ❌
- **Reason**: 무중계 광전송 throughput 기록 — ECC 무관
- **ID**: ieee:10526639
- **Type**: conference
- **Published**: 24-28 Marc
- **Authors**: Jiaqian Yang, Romulo Aparecido, Henrique Buglia +11
- **PDF**: https://ieeexplore.ieee.org/document/10526639
- **Abstract**: A 223 km unrepeated transmission link is experimentally demonstrated using 121 nm optical bandwidth. Optimised bidirectional Raman amplification as well as Thulium- and Erbium-doped fibre amplifiers enable a record throughput of 122.62 Tb/s.

## In-Service Transmitter Calibration via Offloaded 4×2 WL MIMO Equalizer with Compensating IQ Imbalance

- **Status**: ❌
- **Reason**: 송신기 IQ 불균형 보정/MIMO 이퀄라이저 — ECC 무관
- **ID**: ieee:10526541
- **Type**: conference
- **Published**: 24-28 Marc
- **Authors**: Masaki Sato, Hidemi Noguchi, Junichiro Matsui +2
- **PDF**: https://ieeexplore.ieee.org/document/10526541
- **Abstract**: In-service Tx-IQ imbalance calibration estimated with 4×2 MIMO equalizer for 96-Gbaud PM-PCS-64QAM was demonstrated over 120 km SMF. Q-penalties of 0.1 dB with 2 ps IQ skew and ±2.5 dB IQ peaking error were achieved.

## 100 Gbps PAM4 Transmissions over 50 km with 40 dB Power Budget for PON using a High-Gain Quantum Dot SOA

- **Status**: ❌
- **Reason**: PAM4 PON 전송 데모, HD-LDPC BER 한계를 기준치로만 언급, 떼어낼 ECC 기법 없음
- **ID**: ieee:10526816
- **Type**: conference
- **Published**: 24-28 Marc
- **Authors**: Lakshmi Narayanan Venkatasubramani, Ahmed Galib Reza, Vladimir S. Mikhrin +3
- **PDF**: https://ieeexplore.ieee.org/document/10526816
- **Abstract**: We experimentally demonstrate a 106 Gbps PON downstream signal transmission using a high-gain InAs/InGaAs quantum dot-based SOA as a preamplifier. We achieved a record-high power budget of 40 dB considering an HD-LDPC BER limit of 1 × 10−2.

## Next-Level Connectivity: Embedding Communication Coding for Efficient Beyond 5G Wireless Federated Learning

- **Status**: ❌
- **Reason**: Federated Learning에 표준 LDPC를 GPU-CPU 가속으로 적용; 새 디코더·코드설계 없고 가속도 NAND 이식 불가
- **ID**: ieee:10545174
- **Type**: conference
- **Published**: 22-23 Marc
- **Authors**: V. Ganesh, D. Ashwanth Raj, R. Venkata Krishnan
- **PDF**: https://ieeexplore.ieee.org/document/10545174
- **Abstract**: Wirelessly Federated Learning (WFL) holds immense promise for collaborative knowledge-sharing among distributed edge devices in the Internet of Things (IoT). However, challenges arise in unstable wireless channel conditions, where conventional WFL struggles due to transmission noise and interference. This results in inaccurate model parameters and potential model loss. Additionally, the limitations of CPU-accelerated edge devices in encoding and decoding processes hinder efficiency. To address these issues, we propose a novel software-defined architecture integrating LDPC communication coding, empowered by GPU-CPU integration. Our approach enhances resilience to disruptions by implementing wireless channel coding in both server-side weight aggregation and client-side local training. The GPU-CPU acceleration significantly boosts computing efficiency. Experimental results showcase a remarkable 100x speedup and a 10x improvement in error reduction compared to state-of-the-art WFL schemes. Our method presents a promising solution for robust and efficient WFL in IoT environments, with broad implications for applications relying on collaborative learning among distributed edge devices.

## A Channel-Insensitive Link Quality Model for Adaptive Coding and Modulation in Satellite Communications

- **Status**: ❌
- **Reason**: 위성 ACM 링크품질 모델, LDPC는 코딩 베이스라인일 뿐 이식 기법 없음
- **ID**: ieee:10521443
- **Type**: conference
- **Published**: 2-9 March 
- **Authors**: Adina Matache
- **PDF**: https://ieeexplore.ieee.org/document/10521443
- **Abstract**: Modern terrestrial and satellite communication systems use some form of link adaptation to improve the overall system efficiency and achieve higher data rates with no increase in bandwidth. Adaptive Coding and Modulation (ACM) is a common link adaptation technique used to mitigate destructive propagation effects and improve overall system efficiency by dynamically changing the communication mode according to the channel characteristics. A robust mode selection algorithm is key to an efficient ACM protocol. It requires a link quality model to estimate the decoder performance as a function of the instantaneous channel condition. In this paper, a channel-insensitive link quality model is developed together with a heuristic mode selection algorithm for ACM. The proposed link quality model uses an Information Outage Probability (IOP) bound for channel quality measurement and accurate performance prediction. The heuristic mode selection algorithm is tested and demonstrated via computer simulations using the 5G New Radio (NR) Low-Density Parity-Check (LDPC) code as the coding scheme in a system operating under a non-stationary frequency-flat fading channel profile.

## LDPC Codes with Different Frame Sizes over Multipath Fading Channels

- **Status**: ❌
- **Reason**: CCSDS LDPC 블록페이딩 프레임크기 성능분석(순수 이론/시뮬), 디코더·HW·구성 기여 없음
- **ID**: ieee:10521203
- **Type**: conference
- **Published**: 2-9 March 
- **Authors**: Dariush Divsalar, Marc Sanchez Net, Kar-Ming Cheung +1
- **PDF**: https://ieeexplore.ieee.org/document/10521203
- **Abstract**: This paper provides theoretical and simulation performance of space communications systems over block fading channels. Data frames are usually used in both coded and uncoded communications systems. If the duration of a frame is less than coherence time of the fading channel (which is inversely proportional to the Doppler spread), then the block fading model can be assumed. In other words, it is assumed that the fade amplitude is approximately constant over the frame duration. The analytical frame error rate over block fading channel can be derived if the frame error rate performance over AWGN channel is available, and the probability density function of fade amplitudes is known.This paper investigates the trade-offs in system performance versus coding frame size in block fading channels and provides guidance on how to select appropriate frame sizes as a function of the fading channel severity. We first show the performance of random codes over such channels by extending the known theoretical results to block fading. Then, we validate these new theoretical results with high-fidelity simulations using examples for both coded and uncoded systems. For coded systems, we consider the standard rate 1/2 CCSDS LDPC codes with frame sizes of 1024 and 16384 information bits, which are likely to be used by upcoming lunar missions such as the Human Landing System. We show that although the longer block codes provide clear gains compared to shorter codes in AWGN channels, this advantage is dramatically reduced depending on the severity of the fading channel, which we vary from a Rician parameter of 0 dB to 20 dB. Finally in this paper we proposed analytical results for frame error rates in partial fading where each received codeword can observe two or more independent fades. Some simulations are also provided for partial fading.

## Towards Optimal Binary Patterns for Compressive Terahertz Single-Pixel Imaging

- **Status**: ❌
- **Reason**: 테라헤르츠 압축센싱 이진 패턴 최적화 — LDPC/ECC 아님(센싱행렬 코히런스 문제)
- **ID**: ieee:10501583
- **Type**: conference
- **Published**: 17-22 Marc
- **Authors**: Adolphe Ndagijimana, Iñigo Ederra, Miguel Heredia Conde
- **PDF**: https://ieeexplore.ieee.org/document/10501583
- **Abstract**: Terahertz (THz) radiation's properties make it ideal for various imaging applications. However, creating simple, cost-effective, and high-resolution THz array detectors is challenging. Mechanical scanning is commonly used but creates a tradeoff between frame rate and resolution. Fortunately, Compressive Sensing (CS) offers a solution by reducing the required number of measurements needed compared to Shannon-Nyquist's sampling theory. CS-THz imaging is usually implemented using a single-pixel camera with spatial modulation patterns, mostly binary patterns. However, the non-uniform and diffraction propagation present in the THz range affects the mutual coherence of the resulting sensing matrices resulting in image reconstruction degradation. In this paper, we introduce an optimization procedure for generating binary patterns that consider THz diffraction and non-uniform illumination of the mask. The produced sensing matrices exhibit low coherence compared to other typical binary sensing matrices, resulting in a higher reconstruction performance than all others.

## An Intelligent Adjustment Mechanism for Communication System of Spacecraft

- **Status**: ❌
- **Reason**: 우주선 통신 시스템 계층적 지능형 조정 메커니즘 — LDPC/ECC 무관
- **ID**: ieee:10504101
- **Type**: conference
- **Published**: 15-17 Marc
- **Authors**: Kenan Zhang, Haokun Li, Chuan Lin +1
- **PDF**: https://ieeexplore.ieee.org/document/10504101
- **Abstract**: Most existed intelligent adjustment mechanism methods for communication system of spacecraft are limited to physical layer design at present, making it difficult to adapt to special conditions. The intelligent adjustment mechanism method of Communication system for most spacecraft is limited to the physical layer design at present, making it difficult to adapt to special conditions. for Communication system, a layered intelligent adjustment mechanism method is proposed, which is designed by the physical layer, data The physical layer is designed separately from watchdog and read back reconfiguration, and the data link layer has completed the independent detection design based on the data link layer. The physical layer is designed separately from watchdog and read back reconfiguration, and the data link layer has completed the independent detection design based on the RF link. The application layer has completed the design of automatic power control strategies for transmitters. The verification is carried out in ground experiment as well as in-orbit flight, and the result shows that the mechanism proposed is suitable for long-term flight.

## Low Power Area Efficient Adaptive Turbo Decoder Architecture For Wireless NoC

- **Status**: ❌
- **Reason**: 무선 NoC용 적응 터보 디코더 — 터보 부호이고 LDPC 아님, 떼어낼 NAND ECC 기법 없음
- **ID**: ieee:10921849
- **Type**: conference
- **Published**: 15-16 Marc
- **Authors**: Anupama Sindgi, Asha M, Nipun Sharma +2
- **PDF**: https://ieeexplore.ieee.org/document/10921849
- **Abstract**: This research introduces a novel Turbo encoder and Adaptive Turbo decoder model designed to enhance Bit Error Rate (BER) performance across a spectrum of modulation schemes. The study systematically evaluates the model's efficacy in diverse channel environments, including AWGN, Rayleigh, and Rician channels, employing simulations and comparisons with conventional Adaptive Viterbi Decoder and Turbo decoder methods. Results underscore the Adaptive Turbo Decoding (ATD) model's superior BER performance, particularly as iterations increase. The investigation further extends to RF Wireless Network-On-Chip (WiNoC) scenarios, emphasizing the adaptability of ATD for effective error correction. Furthermore, the research explores the implications of ATD in Orthogonal Frequency Division Multiplexing (OFDM) systems, comparing models based on Fast Fourier Transform (FFT), Discrete Wavelet Transform (DWT), and Dual-Tree Complex Wavelet Transform (DTCWT). Notably, the ATD-DTCWT-OFDM model exhibits a substantial reduction in BER, showcasing the potential advantages of Dual-Tree Complex Wavelet Transform for OFDM modulation in acoustic channels with multipath. This research contributes valuable insights into the optimization of communication channels through the application of adaptive decoding techniques.

## Development of Turbo Product Code with Elementary Encoders as LDPC Code

- **Status**: ❌
- **Reason**: DVB-S2용 터보곱부호의 elementary encoder로 LDPC 사용 — LDPC가 베이스라인, 떼어낼 새 LDPC ECC 기법 없음
- **ID**: ieee:10496787
- **Type**: conference
- **Published**: 12-14 Marc
- **Authors**: O. G. Chertova, D. S. Chirov, A. D. Grigorieva +1
- **PDF**: https://ieeexplore.ieee.org/document/10496787
- **Abstract**: This work explores the possibility of using low-density parity check codes as elementary encoders for turbo product code. This approach has prospects for implementation in digital video broadcasting - satellite communication standard version 2. The article describes in detail the algorithm for implementing an encoder and layered belief propagation decoder for a turbo product code based on low density parity check codes, taking into account turbo code elementary codes operation specificity. The result of the work is an estimate of the noise immunity of turbo product codes using codes with low-density parity check for the noise immunity of the communication system used in digital video broadcasting - satellite communication standard version 2. The bit error rate was used as a criterion for noise immunity.

## Development of Turbo Product Code with Elementary Encoders as LDPC Code

- **Status**: ❌
- **Reason**: 제목만 LDPC이고 초록은 트랙터 하이브리드 전기구동에 관한 내용 — LDPC와 전혀 무관
- **ID**: ieee:10496801
- **Type**: conference
- **Published**: 12-14 Marc
- **Authors**: O. N. Didmanidze, R. S. Fedotkin, V. A. Kryuchkov +2
- **PDF**: https://ieeexplore.ieee.org/document/10496801
- **Abstract**: Increasing the environmental safety of agricultural machinery is a key direction in the development of automotive and tractor engineering. The current situation with tractor technology indicates the need to update and improve the tractor fleet as a whole, and especially in relation to small and medium traction classes of 0.6-2.0. Solving the problems of greening and updating the tractor fleet is facilitated by the creation of tractor equipment with a hybrid electric drive. Available developments make it possible to offer the most efficient hybrid electric drive schemes suitable for use in tractor technology. Based on the existing experience of tractor manufacturing, it is possible to determine a list of traction classes required for replacement. Using worldwide experience in creating tractors with electric drive, it is possible to determine the requirements for traction batteries sufficient for their use in a tractor with a hybrid drivetrain. In total, schemes and basic technical requirements for a tractor with a hybrid drivetrain are proposed. The benefits of using such solutions in the long term are preliminarily described.

## Research of the Efficiency of Using LDPC, Turbo Product and Polar Codes with OCDM-OChDM

- **Status**: ❌
- **Reason**: LDPC/터보/폴라 코드의 수중·페이딩 채널 BER 비교 연구 — 표준 부호 성능 평가만, 새 디코더/구성 기여 없음
- **ID**: ieee:10496768
- **Type**: conference
- **Published**: 12-14 Marc
- **Authors**: V. D. Klyuchnikov, A. I. Sattarova, D. Ch. Tsoi +2
- **PDF**: https://ieeexplore.ieee.org/document/10496768
- **Abstract**: This article discusses the using of various code structures in systems with cascaded multiple access Orthogonal Code Division Multiplexing - Orthogonal Chirp Division Multiplexing, the goal of determining signal-code structures that provide the best noise immunity in Waterson, Rayleigh, and underwater channels. The main purpose of research is to find out the data about Bit Error Rate for different cases of usage of popular types of noise immunity codes. All of these codes are used for reducing of the negative effects of various channels such as high rate of noise or fading etc. For every other channel the influence of these effects does vary. The results of the research would provide the information about the effectiveness of low-density-parity-check, polar and turbo product codes in different channels such as underwater, Rayleigh, Waterson.

## Implementing Reversible and Lossless Data Hiding Within Encrypted Images

- **Status**: ❌
- **Reason**: 암호화 이미지 내 가역 데이터 은닉(스테가노그래피·카오스 암호), ECC 무관
- **ID**: ieee:10512302
- **Type**: conference
- **Published**: 1-3 March 
- **Authors**: Supreetha R, Pearl Alisha Lobo
- **PDF**: https://ieeexplore.ieee.org/document/10512302
- **Abstract**: In the realm of data protection, cryptography and steganography stand out as effective methods. Cryptography involves securing data through encryption and decryption processes, while steganography focuses on concealing data within other data. Combining these methodologies creates a strong approach for concealing data within encrypted images, enhancing overall security. Chaotic cryptography has gained prominence due to its effectiveness in encrypting and decrypting images. To reduce the compatibility challenges between certain data hiding techniques and chaotic cryptography, two types of process is devised and put into practice. The first method involves interpolation technique and Least Significant Bit (LSB) data hiding within the chaotic encryption framework. The interpolation technique enhances the compatibility of information insertion within encrypted images. LSB data hiding involves replacing LSB bits of pixels with the secret data. In the second method, a prediction error technique is done along with chaotic encryption. In this, significant effectiveness in securely hiding data within encrypted images is achieved. Chaotic encryption is integrated into both methods to guarantee the confidentiality and protection of the embedded data. In each method, the concealed data is seamlessly embedded within the encrypted image, and upon reception, the information can be accurately extracted. A comparative analysis is conducted based on various parameters, including Peak Signal to Noise Ratio (PSNR), Structural Similarity (SSIM), computation time, and embedding rate
