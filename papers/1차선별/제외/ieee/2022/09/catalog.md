# IEEE Xplore — 2022-09


## Decoding Nonbinary LDPC Codes via Proximal-ADMM Approach

- **Status**: ❌
- **Reason**: 비이진(GF(2^m)) LDPC ADMM 디코더 — 비이진 LDPC는 원칙 제외
- **ID**: ieee:9698061
- **Type**: journal
- **Published**: Sept. 2022
- **Authors**: Yongchao Wang, Jing Bai
- **PDF**: https://ieeexplore.ieee.org/document/9698061
- **Abstract**: In this paper, we focus on decoding nonbinary low-density parity-check (LDPC) codes in Galois fields of characteristic two via the proximal alternating direction method of multipliers (proximal-ADMM). By exploiting Flanagan/Constant-Weighting embedding techniques and the decomposition technique based on three-variables parity-check equations, two efficient proximal-ADMM decoders for nonbinary LDPC codes are proposed. We show that both of them are theoretically guaranteed convergent to some stationary point of the decoding model and either of their computational complexities in each proximal-ADMM iteration scales linearly with LDPC code’s length and the size of the considered Galois field. Moreover, the decoder based on the Constant-Weight embedding technique satisfies the favorable property of codeword symmetry. Simulation results demonstrate their effectiveness in comparison with state-of-the-art LDPC decoders.

## Improving Performance of LDPC-Coded Links via Partial Superposition Retransmission

- **Status**: ❌
- **Reason**: 5G LDPC를 그대로 쓴 재전송(superposition retransmission) 통신 기법, 떼어낼 디코더/코드설계 ECC 기여 없음
- **ID**: ieee:9906940
- **Type**: journal
- **Published**: Sept. 2022
- **Authors**: Yinchu Wang, Qianfan Wang, Ming Jiang +1
- **PDF**: https://ieeexplore.ieee.org/document/9906940
- **Abstract**: In this paper, we propose a transmission scheme for uplink and downlink transmissions, where the fifth generation (5G) low-density parity-check (LDPC) codes are implemented for error correction. In the proposed scheme, the acknowledgment (ACK) or negative acknowledgment (NACK) feedback information is transmitted along with the payload data by cyclically shifting coded sequence, while the re-transmitted codewords are superimposed (XORed) partially on the current codewords. The distinguished feature of the proposed transmission scheme is that it requires neither extra transmission bandwidth nor extra transmission power. We also propose to truncate the error patterns for the purpose of reducing the implementation complexity and reducing the error propagation. Numerical results show that the proposed scheme significantly outperforms conventional LDPC-coded transmission. For the 5G LDPC code with length 1920 at the signal-to-noise ratio (SNR) of 1.3 dB, the word error rate (WER) of the data transmitted by the proposed scheme is about 10−4, while that of the conventional LDPC-coded transmission is about 10−2.

## Design and Optimization of Protograph LDPC-Coded Multipulse PPM Systems Over Poisson Channels

- **Status**: ❌
- **Reason**: FSO/Poisson 채널 PLDPC-코드 MPPM 변조·constellation 설계 — 채널/변조 특이적, 일반 LDPC 코드설계 기여 약함
- **ID**: ieee:9786657
- **Type**: journal
- **Published**: Sept. 2022
- **Authors**: Zhaojie Yang, Yi Fang, Guohua Zhang +1
- **PDF**: https://ieeexplore.ieee.org/document/9786657
- **Abstract**: Combining powerful error-correction codes (ECCs) with multipulse pulse-position modulation (MPPM) has great potential to realize high-throughput and high-reliability transmissions in free-space optical (FSO) communication systems. This paper conducts an insightful investigation on protograph low-density parity-check (PLDPC)-coded MPPM systems over Poisson channels. To be specific, we first put forward a novel type of constellations, referred to as irregular pulse-distribution (IPD) constellations, for MPPM. We also conceive a bit-level rate-adaptive (RA) scheme, which can exploit the structural property of the IPD constellations to significantly improve the convergence performance at the price of transmission-rate loss. Furthermore, with the aid of a modified protograph extrinsic information transfer (PEXIT) algorithm, we construct three enhanced PLDPC codes with code rates $1/2, 2/3$ and $3/4$ that exhibit excellent decoding thresholds over Poisson channels. The proposed PLDPC-coded MPPM systems with the use of the IPD constellations, RA scheme, and enhanced PLDPC codes are superior to the state-of-the-art counterparts.

## DeepWiVe: Deep-Learning-Aided Wireless Video Transmission

- **Status**: ❌
- **Reason**: DeepWiVe JSCC 비디오 전송, LDPC는 비교 베이스라인 뿐, 이식 ECC 기법 없음
- **ID**: ieee:9837870
- **Type**: journal
- **Published**: Sept. 2022
- **Authors**: Tze-Yang Tung, Deniz Gündüz
- **PDF**: https://ieeexplore.ieee.org/document/9837870
- **Abstract**: We present DeepWiVe, the first-ever end-to-end joint source-channel coding (JSCC) video transmission scheme that leverages the power of deep neural networks (DNNs) to directly map video signals to channel symbols, combining video compression, channel coding, and modulation steps into a single neural transform. Our DNN decoder predicts residuals without distortion feedback, which improves the video quality by accounting for occlusion/disocclusion and camera movements. We simultaneously train different bandwidth allocation networks for the frames to allow variable bandwidth transmission. Then, we train a bandwidth allocation network using reinforcement learning (RL) that optimizes the allocation of limited available channel bandwidth among video frames to maximize the overall visual quality. Our results show that DeepWiVe can overcome the cliff-effect, which is prevalent in conventional separation-based digital communication schemes, and achieve graceful degradation with the mismatch between the estimated and actual channel qualities. DeepWiVe outperforms H.264 video compression followed by low-density parity check (LDPC) codes in all channel conditions by up to 0.0485 in terms of the multi-scale structural similarity index measure (MS-SSIM), and H.265+ LDPC by up to 0.0069 on average. We also illustrate the importance of optimizing bandwidth allocation in JSCC video transmission by showing that our optimal bandwidth allocation policy is superior to uniform allocation as well as a heuristic policy benchmark.

## Task-Oriented Multi-User Semantic Communications

- **Status**: ❌
- **Reason**: DL 시맨틱 통신, LDPC ECC 기법 없음
- **ID**: ieee:9830752
- **Type**: journal
- **Published**: Sept. 2022
- **Authors**: Huiqiang Xie, Zhijin Qin, Xiaoming Tao +1
- **PDF**: https://ieeexplore.ieee.org/document/9830752
- **Abstract**: While semantic communications have shown the potential in the case of single-modal single-users, its applications to the multi-user scenario remain limited. In this paper, we investigate deep learning (DL) based multi-user semantic communication systems for transmitting single-modal data and multimodal data, respectively. We adopt three intelligent tasks, including, image retrieval, machine translation, and visual question answering (VQA) as the transmission goal of semantic communication systems. We propose a Transformer based framework to unify the structure of transmitters for different tasks. For the single-modal multi-user system, we propose two Transformer based models, named, DeepSC-IR and DeepSC-MT, to perform image retrieval and machine translation, respectively. In this case, DeepSC-IR is trained to optimize the distance in embedding space between images and DeepSC-MT is trained to minimize the semantic errors by recovering the semantic meaning of sentences. For the multimodal multi-user system, we develop a Transformer enabled model, named, DeepSC-VQA, for the VQA task by extracting text-image information at the transmitters and fusing it at the receiver. In particular, a novel layer-wise Transformer is designed to help fuse multimodal data by adding connection between each of the encoder and decoder layers. Numerical results show that the proposed models are superior to traditional communications in terms of the robustness to channels, computational complexity, transmission delay, and the task-execution performance at various task-specific metrics.

## Optimised Multithreaded CV-QKD Reconciliation for Global Quantum Networks

- **Status**: ❌
- **Reason**: CV-QKD reconciliation(양자 원칙 제외), sliced reconciliation은 QKD 고유로 고전 LDPC 신기여 아님
- **ID**: ieee:9813742
- **Type**: journal
- **Published**: Sept. 2022
- **Authors**: Xiaoyu Ai, Robert Malaney
- **PDF**: https://ieeexplore.ieee.org/document/9813742
- **Abstract**: Designing a practical Continuous Variable (CV) Quantum Key Distribution (QKD) system requires an estimation of the quantum channel characteristics and the extraction of secure keys based on a large number of distributed quantum signals. On standard processors, it can take hours to reconcile the required number of quantum signals. This problem is exacerbated for Low Earth Orbit (LEO) satellite CV-QKD, where the satellite flyover time is less than a few minutes. A potential solution is massive parallelisation of the classical reconciliation where a large-code block is subdivided into many shorter blocks for individual decoding. However, the penalty of this procedure on the important final secured key rate is non-trivial to determine and hitherto has not been formally analysed. In this work, we fill this important knowledge gap via detailed analyses and experimental verification of a CV-QKD sliced reconciliation protocol that uses large block-length low-density parity-check decoders. Our new solution results in a significant increase in the final key rate relative to non-optimised reconciliation. In addition, it allows for the acquisition of quantum secured messages between terrestrial stations and LEO satellites within a flyover timescale even using off-the-shelf processors. Our work allows for optimised global quantum networks secured via fundamental physics.

## The Secret Arithmetic of Patterns: A General Method for Designing Constrained Codes Based on Lexicographic Indexing

- **Status**: ❌
- **Reason**: constrained code(LOCO) 설계 — 채널 ECC LDPC가 아닌 변조제약부호, 떼어낼 LDPC 기법 없음
- **ID**: ieee:9763472
- **Type**: journal
- **Published**: Sept. 2022
- **Authors**: Ahmed Hareedy, Beyza Dabak, Robert Calderbank
- **PDF**: https://ieeexplore.ieee.org/document/9763472
- **Abstract**: Constrained codes are used to prevent errors from occurring in various data storage and data transmission systems. They can help in increasing the storage density of magnetic storage devices, in managing the lifetime of solid-state storage devices, and in increasing the reliability of data transmission over wires. Over the years, designing practical (complexity-wise) capacity-achieving constrained codes has been an area of research gaining significant interest. We recently designed various constrained codes based on lexicographic indexing. We introduced binary symmetric lexicographically-ordered constrained (S-LOCO) codes,  $q$ -ary asymmetric LOCO (QA-LOCO) codes, and a class of two-dimensional LOCO (TD-LOCO) codes. These families of codes achieve capacity with simple encoding and decoding, and they are easy to reconfigure. We demonstrated that these codes can contribute to notable density and lifetime gains in magnetic recording (MR) and Flash systems, and they find application in other systems too. In this paper, we generalize our work on LOCO codes by presenting a systematic method that guides the code designer to build any constrained code based on lexicographic indexing once the finite set of data patterns to forbid is known. In particular, we connect the set of forbidden patterns directly to the cardinality of the LOCO code and most importantly to the rule that uncovers the index associated with a LOCO codeword. By doing that, we reveal the secret arithmetic of patterns, and make the design of such constrained codes significantly easier. We give examples illustrating the method via codes based on lexicographic indexing from the literature. We then design optimal (rate-wise) constrained codes for the new two-dimensional magnetic recording (TDMR) technology. Over a practical TDMR model, we show notable performance gains as a result of solely applying the new codes. Moreover, we show how near-optimal constrained codes for TDMR can be designed and used to further reduce complexity and error propagation. All the newly introduced LOCO codes are designed using the proposed general method, and they inherit all the desirable properties in our previously designed LOCO codes.

## An Information-Theoretic Perspective on Successive Cancellation List Decoding and Polar Code Design

- **Status**: ❌
- **Reason**: Polar/SCL 디코딩 및 Reed-Muller 설계 — LDPC ECC 이식 기법 아님
- **ID**: ieee:9770084
- **Type**: journal
- **Published**: Sept. 2022
- **Authors**: Mustafa Cemil Coşkun, Henry D. Pfıster
- **PDF**: https://ieeexplore.ieee.org/document/9770084
- **Abstract**: This work identifies information-theoretic quantities that are closely related to the required list size on average for successive cancellation list (SCL) decoding to implement maximum-likelihood decoding over general binary memoryless symmetric (BMS) channels. It also provides upper and lower bounds for these quantities that can be computed efficiently for very long codes. For the binary erasure channel (BEC), we provide a simple method to estimate the mean accurately via density evolution. The analysis shows how to modify, e.g., Reed-Muller codes, to improve the performance when practical list sizes, e.g.,  $L\in {[{8, 1024}]}$ , are adopted. Exemplary constructions with block lengths  $N\in \{128,512\}$  outperform polar codes of 5G over the binary-input additive white Gaussian noise channel. It is further shown that there is a concentration around the mean of the logarithm of the required list size for sufficiently large block lengths, over discrete-output BMS channels. We provide the probability mass functions (p.m.f.s) of this logarithm, over the BEC, for a sequence of the modified RM codes with an increasing block length via simulations, which illustrate that the p.m.f.s concentrate around the estimated mean.

## Development of Transmitter and Receiver With Set Partitioning 64APSK Coded Modulation Designed on Basis of Channel Capacity

- **Status**: ❌
- **Reason**: 위성 SP-64APSK 코딩변조 송수신기 — LDPC 부수 언급, 떼어낼 ECC 기법 없음
- **ID**: ieee:9780593
- **Type**: journal
- **Published**: Sept. 2022
- **Authors**: Yuki Koizumi, Yoichi Suzuki, Masaaki Kojima +2
- **PDF**: https://ieeexplore.ieee.org/document/9780593
- **Abstract**: In this paper, we present a prototype transmitter and receiver with set partitioning (SP)-64 amplitude and phase shift keying (APSK) coded modulation we developed for expanding satellite transmission capacity. SP-multi-level coded modulation is a transmission scheme that can improve noise immunity by properly combining a modulation scheme, bit allocation, and error-correction codes. We designed SP-64APSK coded modulation on the basis of channel capacity for expanding satellite transmission capacity. We confirmed that it has higher robustness to additive white Gaussian noise (AWGN) than DVB-S2X’s 64APSK modulation with Gray mapping through computer simulation. We also developed a prototype transmitter and receiver to implement our SP-64APSK coded modulation and evaluated its transmission performances in an AWGN channel and in a non-linear channel simulating 12-GHz-band satellite transponder characteristics. We describe the method of designing our SP-64APSK coded modulation through computer simulation, the modulation/demodulation process, and transmission performances of the prototype transmitter and receiver. We also indicate that 8K ultra-high definition television (UHDTV) with an encoded bit rate of 150 Mbps can be transmitted using the prototype within 34.5 MHz, which is the bandwidth of a single transponder for satellite broadcasting in Japan.

## Optimized Linear and Non-Linear Precoding for Biased ASK Modulation in Multiuser SWIPT With Integrated Receiver

- **Status**: ❌
- **Reason**: SWIPT 무선 ASK 프리코딩, LDPC·이식 가능한 디코더/코드설계 기법 없음
- **ID**: ieee:9813713
- **Type**: journal
- **Published**: Sept. 2022
- **Authors**: Erica Debels, Marc Moeneclaey
- **PDF**: https://ieeexplore.ieee.org/document/9813713
- **Abstract**: Simultaneous wireless information and power transfer can be achieved using an integrated receiver, where the incoming signal is rectified, and both the energy harvesting (EH) and the information detection (ID) operate on this rectified signal. Because phase information is lost at the input of the ID, commonly-used modulation techniques cannot be straightforwardly applied and biased  $M$ -ASK is used instead. We consider downstream communication over a Rician block-fading channel, from a multi–antenna basestation to a number of single-antenna users. Multi-user interference is eliminated by applying zero-forcing precoding. Using a realistic rectifier model, we compare EH and ID performances of linear precoding (LP) and modified Tomlinson-Harashima precoding (THP). We add low-complexity algorithms to these precoders that optimize the user ordering and the constellation rotations. Moreover, we investigate the effect of the amplitude ratio  $\rho _{\mathrm {ASK}}$  of the constellation on the energy-rate trade-off. Compared to the same precoders without optimization, optimizing the user ordering, rotations and  $\rho _{\mathrm {ASK}}$  considerably reduces the transmit power required to achieve a harvested power of −30 dBm or an average mutual information of  $(\log _{2}M)/2$ . Both with and without optimizations, THP outperforms LP in terms of EH and ID, but THP exhibits much larger gains when optimizations are applied.

## Non-Binary PRN-Chirp Modulation: A GNSS Fast Acquisition Signal Waveform

- **Status**: ❌
- **Reason**: GNSS 비이진 PRN-chirp 변조 파형 — LDPC ECC와 무관
- **ID**: ieee:9803216
- **Type**: journal
- **Published**: Sept. 2022
- **Authors**: Lorenzo Ortega, Jordi Vilà-Valls, Eric Chaumette
- **PDF**: https://ieeexplore.ieee.org/document/9803216
- **Abstract**: In this letter, we propose a new non-binary modulation which allows both Global Navigation Satellite Systems (GNSS) synchronization and the demodulation of non-binary symbols, without the need of a pilot signal, with the aim to provide a fast first position, velocity and time fix. The waveform is constructed as the product of i) a pseudo-random noise sequence with good auto-correlation and cross-correlation properties, and ii) a chirp spread spectrum family, which allows to demodulate non-binary symbols even if the signal phase is unknown. In order to demodulate the data, a bank of non-coherent matched filters is proposed. Because of the particular modulation structure, the receiver is capable to demodulate the navigation message faster while allowing the basic GNSS signal processing functionalities. Illustrative results are provided to support the discussion.

## Security Analysis of LDPC Code-Based Encryption

- **Status**: ❌
- **Reason**: QC-LDPC 기반 McEliece 암호(LEDAcrypt) 보안 분석; ISD 기반 보안평가로 NAND ECC 디코더·구성 이식 기법 없음
- **ID**: ieee:9952322
- **Type**: conference
- **Published**: 9-10 Sept.
- **Authors**: Dibyasree Guha, Debasish Bera, Sourabh Biswas
- **PDF**: https://ieeexplore.ieee.org/document/9952322
- **Abstract**: In the search for good alternatives to classical cryptosystems with number theory as their backbone, code-based systems have emerged as a strong competitor for “Post-Quantum cryptography”. In this paper we provide a comprehensive overview on quasi-cyclic (QC) low-density parity-check (LDPC) code-based public key encryption scheme known as LEDAcrypt. It is based on McEliece cryptosystem as the building block. A comparative study of security analysis based on different information-set decoding (ISD) and performance evaluation of the said system are also carried out.

## Effectiveness Analysis of QC-LDPC Encoder with Model Based Design Approach

- **Status**: ❌
- **Reason**: 3GPP 표준 QC-LDPC 인코더를 모델기반으로 FPGA 구현한 수준 — 표준 부호 단순 재사용, 새 기여 없음
- **ID**: ieee:9925295
- **Type**: conference
- **Published**: 7-9 Sept. 
- **Authors**: Hakan Taş, Sıddıka Berna Örs Yalçın
- **PDF**: https://ieeexplore.ieee.org/document/9925295
- **Abstract**: Channel coding techniques are used to reduce error rates during data transmission in mobile communication systems. LDPC (Low-density Parity Check) coding was first designed by Robert G. Gallager in 1962. It has been accepted and started to be used as a standard for coding data channels in fifth generation mobile communication by member companies of 3GPP (3rd Generation Partnership Project). The QC-LDPC method, which has a more hardware-friendly algorithmic structure, was chosen by 3GPP as the coding method. In this study, the QC-LDPC coding block, which is clearly stated in the 3GPP TS 38–212 standard document, is model-based and implemented on the FPGA.

## Easy5G: Software for Simulation and Study of 5G NR Interface

- **Status**: ❌
- **Reason**: 5G NR 시뮬레이션 소프트웨어. LDPC는 부수 언급일 뿐 떼어낼 디코더/HW/코드설계 기법 없음
- **ID**: ieee:9939905
- **Type**: conference
- **Published**: 7-9 Sept. 
- **Authors**: Jean Fonseca, Amanda Fernandes, Fernanda Corrêa
- **PDF**: https://ieeexplore.ieee.org/document/9939905
- **Abstract**: The new 5G mobile internet standard, expected to arrive in mid-2022, promises greater connection capacity for billions of devices and a balanced experience between speed, latency, and low power consumption. To achieve high error correction power, the 3GPP used a class of encoder known as low-density parity-check code (LDPC). In this sense, this work presents the development of a software, named Easy5G, that allows simulation and evaluation of the 5G New Radio (NR) scenarios and channel coding schemes planned for 5G NR, using LDPC codes. Easy5G, through the GNU Radio platform, allows parameter changes and simulations of bit error rate (BER) results. This software allows the creation of direct contact between this new technology, academia, and industry.

## CS-ToF sensing by means of greedy bi-lateral fusion and near-to-optimal low-density codes

- **Status**: ❌
- **Reason**: LDPC를 압축센싱 측정행렬 구성에 차용한 ToF 3D 센싱 — 채널코딩 ECC 아님, 떼어낼 디코더 기법 없음
- **ID**: ieee:9909902
- **Type**: conference
- **Published**: 29 Aug.-2 
- **Authors**: Alvaro Lopez Paredes, Miguel Heredia Conde, Otmar Loffeld
- **PDF**: https://ieeexplore.ieee.org/document/9909902
- **Abstract**: In this work, we propose a sensing scheme for the reconstruction of a highly sparse 3D view by a Pulse-Based Time-of-Flight (PB-ToF) camera aiming at achieving high angular resolution at interactive rates. The construction of the sensing matrices is focused on the optimization of the coherence and the preservation of the low density which characterize Low-Density Parity-Check (LDPC) codes. We investigate the possibility of shifting the custom sequences generated at the pixel level by selecting the shifts which maximize the minimum distance between adjacent columns, as well as the use of the information from the two complementary integration channels or taps the ToF sensor consists of. The signal reconstruction algorithm, coined greedy bi-lateral fusion, firstly determines a preliminary target probability distribution, and then re-weights it by exploiting the local correlations within the pixel array by applying a bi-lateral filtering which accounts for the affinities in spatial and intensity domains. The algorithm improves the accuracy of our camera under presence of strong noise and still preserves the speed and simplicity associated to classical greedy algorithms.

## Robust Semantic Communications Against Semantic Noise

- **Status**: ❌
- **Reason**: 시맨틱 통신 견고성 — LDPC ECC 기법 없음
- **ID**: ieee:10012843
- **Type**: conference
- **Published**: 26-29 Sept
- **Authors**: Qiyu Hu, Guangyi Zhang, Zhijin Qin +3
- **PDF**: https://ieeexplore.ieee.org/document/10012843
- **Abstract**: Although the semantic communications have exhibited satisfactory performance in a large number of tasks, the impact of semantic noise and the robustness of the systems have not been well investigated. Semantic noise is a particular kind of noise in semantic communication systems, which refers to the misleading between the intended semantic symbols and received ones. In this paper, we first propose a framework for the robust end-to-end semantic communication systems to combat the semantic noise. Particularly, we analyze the causes of semantic noise and propose a practical method to generate it. To remove the effect of semantic noise, adversarial training is proposed to incorporate the samples with semantic noise in the training dataset. Then, the masked autoencoder (MAE) is designed as the architecture of a robust semantic communication system, where a portion of the input is masked. To further improve the robustness of semantic communication systems, we firstly employ the vector quantization-variational autoencoder (VQ-VAE) to design a discrete codebook shared by the transmitter and the receiver for encoded feature representation. Thus, the transmitter simply needs to transmit the indices of these features in the codebook. Simulation results show that our proposed method significantly improves the robustness of semantic communication systems against semantic noise with significant reduction on the transmission overhead.

## Analysis of GEO Satellite Relay Coded Systems

- **Status**: ❌
- **Reason**: GEO 위성 릴레이 분산 코딩 시스템 비교 분석 — NAND에 이식할 구체적 LDPC 디코더·코드 기법 없음
- **ID**: ieee:10012755
- **Type**: conference
- **Published**: 26-29 Sept
- **Authors**: Jiaming Zhang, Shaohua Wu, Aimin Li +2
- **PDF**: https://ieeexplore.ieee.org/document/10012755
- **Abstract**: The recent development of the low Earth orbit (LEO) satellite constellation construction has accelerated the research on applications associated with LEO satellites. One such typical application is to transmit high-resolution remote-sensing images from LEO satellites to ground stations (GS). However, the stringent visible time and the complicated antenna manipulation between LEO satellites and GS makes it challenging for a LEO satellite to complete its full transmission mission within a specified stringent deadline. As such, this paper introduces a geosynchronous equatorial orbit (GEO) satellite as a relay and explores the distributed coding-decoding schemes to assist reliable and high-speed transmission. Specifically, four types of GEO-satellite-relay coded schemes are proposed and analyzed, including three PHY-only coding systems with GEO-full-decoding on board, decoding on ground only, and GEO-partial-decoding on board and one layered coding system. Through simulations, the comparative insights among the four schemes are provided from three dimensions: effectiveness, reliability, and relay complexity. The trade-offs concerning the four schemes in terms of the three indexes are also revealed.

## OTFS Waveform with Phase Noise in sub-THz

- **Status**: ❌
- **Reason**: sub-THz OTFS 위상잡음 보상 — LDPC/ECC 기법 없음
- **ID**: ieee:10012718
- **Type**: conference
- **Published**: 26-29 Sept
- **Authors**: Yaya Bello, Samuel Barnola, David Demmer +1
- **PDF**: https://ieeexplore.ieee.org/document/10012718
- **Abstract**: The availability of large bandwidths in the sub-THz bands appears to be a solution for increasing the capabilities of future wireless communication technologies. However, phase noise generated by oscillators in these bands generates significant signal distortion which needs to be addressed. In this paper, we study the impact of phase noise on OTFS. We propose phase noise compensation scheme and associated frame format. Two dedicated pilot schemes are studied for the phase noise tracking: the first one consists in adding pilots in the delay-Doppler (DD) domain while the other in the delay-Time (DT) domain. We highlight that compensating phase noise in DT domain gives better performance. A comparison between OFDM, DFT-s-OFDM and OTFS according to the 5G-NR numerology is presented. We show that the OTFS waveform is robust to phase noise and may even significantly outperform OFDM and DFT-s-OFDM.

## Towards Quantum Annealing for Multi-user NOMA-based Networks

- **Status**: ❌
- **Reason**: NOMA용 양자 어닐링 ML 디코더 — 양자 전용 기법이며 LDPC 디코더 아님
- **ID**: ieee:10012769
- **Type**: conference
- **Published**: 26-29 Sept
- **Authors**: Eldar Gabdulsattarov, Khaled Rabie, Xingwang Li +1
- **PDF**: https://ieeexplore.ieee.org/document/10012769
- **Abstract**: Quantum Annealing (QA) uses quantum fluctuations to search for a global minimum of an optimization-type problem faster than classical computer. To meet the demand for future internet traffic and mitigate the spectrum scarcity, this work presents the QA-aided maximum likelihood (ML) decoder for multi-user non-orthogonal multiple access (NOMA) networks as an alternative to the successive interference cancellation (SIC) method. The practical system parameters such as channel randomness and possible transmit power levels are taken into account for all individual signals of all involved users. The brute force (BF) and SIC signal detection methods are taken as benchmarks in the analysis. The QA-assisted ML decoder results in the same BER performance as the BF method outperforming the SIC technique, but the execution of QA takes more time than BF and SIC. The parallelization technique can be a potential aid to fasten the execution process. This will pave the way to fully realize the potential of QA decoders in NOMA systems.

## Design and Analysis of Probabilistic Shaping for Polar Coded Communication Systems with Finite Blocklength

- **Status**: ❌
- **Reason**: polar 부호 확률 성형(PS) — LDPC 아니며 채널코딩 ECC 신규 기법 떼어낼 것 없음
- **ID**: ieee:10012882
- **Type**: conference
- **Published**: 26-29 Sept
- **Authors**: Hongjie He, Bin Xia, Yinghong Guo +1
- **PDF**: https://ieeexplore.ieee.org/document/10012882
- **Abstract**: Probabilistic shaping (PS) has been demonstrated as an efficient method to achieve the shaping gain and to approach the Shannon limit in additive white Gaussian noise channels. To narrow the shaping gap caused by the channel fluctuation and the finite blocklength, a novel PS strategy is designed for polar coded communication systems with finite blocklength in Rayleigh flat fading channels. The proposed system transmits the quadrature amplitude modulation symbols and demodulates the received signal through log-maximum-a-posteriori (Log-MAP) detection. The channel capacity is theoretically derived in terms of the mutual information considering the influence of PS and the finite blocklength. Moreover, to solve the non-convex problem that maximizes the channel capacity on the basis of mutual information, an alternating optimization algorithm is proposed. Finally, numerical results indicate that with the optimal probabilistic shaping scheme, the system has 1.7 dB and 0.45 dB gain on the block error rate and channel capacity of the uniform distribution, respectively.

## Highly Efficient OFDM Applying Symbol-Edges Truncating Transmission Technique

- **Status**: ❌
- **Reason**: OFDM 심볼 에지 절단 전송 기법 — LDPC/ECC 무관
- **ID**: ieee:10012901
- **Type**: conference
- **Published**: 26-29 Sept
- **Authors**: Yuu Ichikawa, Keiichi Mizutani, Hiroshi Harada
- **PDF**: https://ieeexplore.ieee.org/document/10012901
- **Abstract**: Wireless technology that can conFigure wide-area IoT systems with high data rates is required toward 6G. To further expand area coverage, it is necessary to improve the data rate of the conventional machine type communications (MTC) such as LTE-M and mMTC at the edge of the coverage area. In this paper, we propose an orthogonal frequency division multiplexing (OFDM) with symbol-edges truncating transmission (STTOFDM) for data rate enhancement. In the proposed STT-OFDM scheme, only a part of the cyclic prefix (CP)-OFDM symbols, which is the legacy communication scheme adopted to 4G and 5G, is transmitted. On the receiver side, zeros are inserted where the no transmission took place at the transmitter side before normal OFDM demodulation is performed. The energy per one-symbol transmission is expected to be reduced by the proposed STTOFDM. We evaluate the achievable throughput and show the usefulness of the proposed STT-OFDM scheme. The proposed STT-OFDM can improve the throughput of the CP-OFDM by about 1.5 times even in low SNR environments.

## Soft Syndrome Decoding of Quantum LDPC Codes for Joint Correction of Data and Syndrome Errors

- **Status**: ❌
- **Reason**: 양자 LDPC(QLDPC) soft syndrome 디코딩 — 양자 전용 syndrome 개념 의존, 원칙 제외
- **ID**: ieee:9951264
- **Type**: conference
- **Published**: 18-23 Sept
- **Authors**: Nithin Raveendran, Narayanan Rengaswamy, Asit Kumar Pradhan +1
- **PDF**: https://ieeexplore.ieee.org/document/9951264
- **Abstract**: Quantum errors are primarily detected and corrected using the measurement of syndrome information which itself is an unreliable step in practical error correction implementations. Typically, such faulty or noisy syndrome measurements are modeled as a binary measurement outcome flipped with some probability. However, the measured syndrome is in fact a discretized value of the continuous voltage or current values obtained in the physical implementation of the syndrome extraction. In this paper, we use this "soft" or analog information without the conventional discretization step to benefit the iterative decoders for decoding quantum low-density parity-check (QLDPC) codes. Syndrome-based iterative belief propagation (BP) decoders are modified to utilize the syndrome-soft information to successfully correct both data and syndrome errors simultaneously, without repeated measurements. We demonstrate the advantages of extracting the soft information from the syndrome in our improved decoders, not only in terms of comparison of thresholds and logical error rates for quasi-cyclic lifted-product QLDPC code families, but also for faster convergence of iterative decoders. In particular, the new BP decoder with noisy syndrome performs as good as the standard BP decoder under ideal syndrome.

## DFE State-Tracking Demapper for Soft-Input FEC in 800G Data Center Interconnects

- **Status**: ❌
- **Reason**: DFE state-tracking demapper로 LLR 정확도 개선 — 광통신 채널 특이적 demapping, NAND LDPC로 떼어낼 디코더/코드설계 기법 없음
- **ID**: ieee:9979553
- **Type**: conference
- **Published**: 18-22 Sept
- **Authors**: Kaiquan Wu, Gabriele Liga, Jeffrey Lee +3
- **PDF**: https://ieeexplore.ieee.org/document/9979553
- **Abstract**: A simple one-step state model is used to track the DFE error propagation for 4-PAM. The knowledge of DFE output states is used to improve LLR accuracy. Demapping via DFE state tracking outperforms bit-interleaving and precoding schemes for the 802.3ca LDPC code by 0.76 dB.

## Bit interleaved chirp spread spectrum coded modulations with iterative decoding based on LDPC codes for coherent and non-coherent regimes

- **Status**: ❌
- **Reason**: CSS/LoRa 비선형 비이진 변조용 BICM-ID LDPC 설계, 무선 변조 특이적이며 NAND 이식성 없음
- **ID**: ieee:9978129
- **Type**: conference
- **Published**: 12-15 Sept
- **Authors**: Jocelyn Bourduge, Charly Poulliat, Benjamin Gadat +1
- **PDF**: https://ieeexplore.ieee.org/document/9978129
- **Abstract**: In this paper, we investigate on bit-interleaved chirp spread spectrum (CSS) coded modulations with iterative decoding (ID) based on low-density parity-check (LDPC) codes. First, we study coded modulation (CM) and bit-interleaved coded modulation (BICM) capacities of CSS based LoRa-like waveforms over Gaussian and Rayleigh fading channels for both coherent and non-coherent receivers. LoRa-like waveforms being by essence nonlinear nonbinary memoryless continuous-phase modulations, this study shows that optimized BICM schemes with iterative decoding are mandatory to close the non negligible gap to the CM capacity when outer binary error-correcting schemes are used. Then, we design LDPC codes, optimized for BICM-ID CSS modulation schemes using both coherent and non coherent receivers. In particular, we show that one has to be careful when using optimized codes for the different regimes. Indeed, unstructured LDPC codes optimized for the coherent regime may be asymptotically non stable when used in the non coherent regime. On the contrary, optimized codes for the non coherent case are always stable in the coherent regime with negligible to fair loss of performance. Finally, designed sparse-graph based BICM-ID CSS modulation schemes show significant performance improvement over classical or advanced LoRa legacy CSS waveforms at finite length.

## Phase Noise Compensation Using FDM Based Pilot Symbol Assisted EKF for OFDM Based Radio Backhaul Links

- **Status**: ❌
- **Reason**: OFDM 위상잡음 보상(EKF) 논문, LDPC는 부수 언급뿐 떼어낼 기법 없음
- **ID**: ieee:9977779
- **Type**: conference
- **Published**: 12-15 Sept
- **Authors**: Ryota Kuribayashi, Mamoru Sawahashi, Norifumi Kamiya
- **PDF**: https://ieeexplore.ieee.org/document/9977779
- **Abstract**: This paper proposes an iterative phase noise compensation (PNC) method using an extended Kalman filter (EKF) that employs pilot symbol assisted (PSA) PNC for computing the initial values in the EKF for orthogonal frequency division multiplexing radio backhaul links. In the PSA PNC stage of the proposed method, the phase noise is estimated and compensated using frequency division multiplexing (FDM) pilot symbols that are multiplexed into the data symbols. Based on the decision symbols after the PSA PNC, the time-varying phase noise estimate and variance in the time domain are tracked and updated using the EKF iteratively. The proposed method achieves a low computational complexity because low-density parity-check (LDPC) decoding is conducted only once after the phase noise in the received signal is suppressed by PSA-EKF PNC. Computer simulation results show that the loss in the required received signal-to-noise power ratio (SNR) satisfying the bit error rate (BER) of 10-8 of the proposed method compared to that without phase noise is suppressed to within approximately 1.2 dB for 256QAM with LDPC coding at the coding rate of 8/9.

## Digital Self-Interference Cancellation Scheme for Full-Duplex Cellular System in 5G

- **Status**: ❌
- **Reason**: 5G 풀듀플렉스 디지털 SI 제거 논문, LDPC는 평가 대상일 뿐 새 ECC 기법 없음
- **ID**: ieee:9978126
- **Type**: conference
- **Published**: 12-15 Sept
- **Authors**: Shota Mori, Keiichi Mizutani, Hiroshi Harada
- **PDF**: https://ieeexplore.ieee.org/document/9978126
- **Abstract**: Full-duplex cellular (FDC) system, which introduces in-band full-duplex (IBFD) to the cellular system, has been paid attention to for increasing spectral efficiency in 5G and 6G systems. IBFD causes new interferences, such as self-interference (SI), because uplink (UL) and downlink (DL) communications are performed simultaneously on the same frequency resources; however, if the new interferences problem can be overcome, IBFD can ideally improve spectral efficiency up to twice that of half-duplex (HD) system. Many SI cancellations have been proposed; however, to the best of our knowledge, there has been no study of digital SI cancellation for application of IBFD to the 5G system by taking into account the 5G signal configuration and the impact on the performance of low-density parity-check (LDPC) code. In this paper, we propose a digital SI cancellation for applying to the 5G-based orthogonal frequency division multiplexing (OFDM) signal. First, we propose a demodulation reference signal (DMRS) configuration to improve the estimation accuracy of the SI channel. Second, the noise power estimation scheme using the proposed DMRS configuration is also proposed for decoding 5G adopted LDPC. Finally, the proposed scheme is evaluated by computer simulations, and we found that the communication quality in IBFD operation becomes equivalent to that in HD operation by applying the proposed digital SI cancellation.

## Deep Learning-Assisted Automatic Modulation Classification in Adaptive FBMC/OQAM Systems

- **Status**: ❌
- **Reason**: FBMC/OQAM 딥러닝 변조분류; LDPC·ECC 무관
- **ID**: ieee:9977504
- **Type**: conference
- **Published**: 12-15 Sept
- **Authors**: L. Häring
- **PDF**: https://ieeexplore.ieee.org/document/9977504
- **Abstract**: This manuscript presents a novel blind modulation classification method applied to adaptive FBMC/OQAM systems which utilizes a neural network to combine different information types for distinguishing between different modulation formats. In the considered bit-loaded multicarrier transmission system, the receiver classifies the bit allocation table based on the received signal. Since the transmission channels from transmit and receive direction are correlated in time-division duplex systems, important side information about the used modulation schemes on each subcarrier is available, thus enabling a much more reliable classification. A deep learning-based algorithm is investigated numerically that extracts features from preprocessed data such as likelihood and receiver bandwidth efficiency values. Simulation results show a superior performance in typical wireless local area network scenarios compared to existing approaches.

## Spatially-Coupled Faster-than-Nyquist Signaling

- **Status**: ❌
- **Reason**: SC-FTN 시그널링·sliding-window 검출기; FTN 신호용 검출 기법으로 LDPC ECC로 떼어낼 기법 없음
- **ID**: ieee:9977594
- **Type**: conference
- **Published**: 12-15 Sept
- **Authors**: Qingya Lu, Shuangyang Li, Baoming Bai +1
- **PDF**: https://ieeexplore.ieee.org/document/9977594
- **Abstract**: A spatially-coupled faster-than-Nyquist (SC-FTN) signaling is proposed in this paper. The signal of SC-FTN signaling is generated continuously by interleaving and repeating the coded FTN signals and a graph-based iterative sliding-window detector can be applied for signal detection. Both bounding and extrinsic information transfer chart analysis are provided to study the error performance of SC-FTN signaling, where performances of both error floor and convergence are considered. Those analyses unveil the intrinsic relationship between error floor, decoding threshold, and detection/decoding complexity, which provides guidelines for the designs of practical systems. Numerical results show that the promising error performance can be achieved with a simple FTN detection, where the bit error rate of coded SC-FTN signaling outperforms both state-of-art coded FTN systems and the BPSK capacity of Nyquist signaling.

## Improving Performance of Large-Scale MIMO Detector Via A Proposed Two-Step Deep-Learning Architecture

- **Status**: ❌
- **Reason**: LS-MIMO 딥러닝 검출기, LDPC 디코더와 무관한 신호 검출
- **ID**: ieee:9977645
- **Type**: conference
- **Published**: 12-15 Sept
- **Authors**: Hieu T. Nguyen, Duc T.M. Hoang, Anh T. Pham
- **PDF**: https://ieeexplore.ieee.org/document/9977645
- **Abstract**: A large-scale multiple-input multiple-out (LS-MIMO) transmission technique with low-resolution analog-to-digital converters (ADCs) has become one of the promising techniques for 5G and future wireless networks. In this paper, we first present the mathematical derivation to fit the high-order 4-ary Amplitude Shift-Keying (ASK) superposition modulation scheme in the conventional deep-learning LS-MIMO signal detector designed previously for the binary phase-shift-keying (BPSK) modulation scheme. Importantly, we also propose a two-step deep-learning detection network that does not require training the network again when changing the modulation order, for example, from BPSK to 4-ary ASK and more, provided that the MIMO configuration is kept unchanged. The two-step model offers a low computing requirement and shorter processing time and still achieves better bit error rate (BER) performance over the one-step architecture. The essential attribute of the proposed two-step detector is that no further training is needed makes it promising for the Internet of Things, where devices with a low computing capacity are embedded. Moreover, the advantages of the two-step deep-learning detector also open up a great possibility to deploy the adaptive modulation transmission scheme to enjoy the channel gain variation of wireless fading channels.

## Adaptive Block Error Correction for Memristive Crossbars

- **Status**: ❌
- **Reason**: Memristive crossbar용 Hamming/checksum 블록 ECC — LDPC 아님, NAND LDPC에 이식할 디코더/코드설계 기법 없음
- **ID**: ieee:9897817
- **Type**: conference
- **Published**: 12-14 Sept
- **Authors**: Surendra Hemaram, Mahta Mayahinia, Mehdi B. Tahoori
- **PDF**: https://ieeexplore.ieee.org/document/9897817
- **Abstract**: Matrix-vector multiplication (MVM) is one of the most frequent operations performed in deep learning and big data applications. On the other hand, the Memory wall problem in traditional processor-centric architectures limits the performance of these applications. The crossbar array of emerging non-volatile memristive devices (memristive crossbar) provides an energy-efficient hardware implementation of MVM for deep learning accelerators and edge computing hardware. However, non-idealities as well as manufacturing and runtime defects of the memristive devices may severely impact the reliability of target applications. This paper presents a new online block error correction technique for memristive crossbars. It enables reliable MVM computation by combining the idea of checksum and Hamming code-based linear coding scheme. The proposed method can correct any number of errors in one particular array block containing multiple columns. An adaptive error correction coding strategy is also presented, so that the ratio of data columns to the parity checksum columns can be adjusted at runtime based on the fault rate, enabling the optimum use of data and parity checksum columns.

## On Soft Decoding of Some Binary RLL-Transmission Codes in Systems with Coherent BPSK Modulation

- **Status**: ❌
- **Reason**: RLL-LDPC/Turbo 코드 BPSK soft 디코딩 — LLR 부호 반전만, 새 디코더/코드설계 기여 없음
- **ID**: ieee:9925949
- **Type**: conference
- **Published**: 11-14 Sept
- **Authors**: Peter Farkaš, Tomáš Páleník
- **PDF**: https://ieeexplore.ieee.org/document/9925949
- **Abstract**: Recently some RLL-LDPC and RLL-Turbocodes were proposed. In BSC the hard decoding methods applied for the original codes - not possessing the RLL properties could be used for these codes without any changes. The questions arise if also the standard soft decoding methods could be used for their decoding in Additive White Gaussian Noise channel without changes. In this paper it is shown that the answer is positive if coherent BPSK modulation is used and the received signal is filtered by Matched Filter. It is shown that the only necessary operation is the inversion of the log-likelihood ratio forming the input to the decoder from the channel for values corresponding to the inverted bits by modifier in transmitter.
