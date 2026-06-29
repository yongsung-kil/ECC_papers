# IEEE Xplore — 2023-10


## Residual Network-Based Channel Estimation for the Protograph LDPC-Coded OFDM Systems

- **Status**: ❌
- **Reason**: PLDPC-OFDM 딥러닝 채널추정/클리핑복원 — LDPC는 베이스라인, 채널추정 NN은 NAND 무관
- **ID**: ieee:10229217
- **Type**: journal
- **Published**: Oct. 2023
- **Authors**: Junsheng Yang, Yi Fang, Lin Dai +2
- **PDF**: https://ieeexplore.ieee.org/document/10229217
- **Abstract**: In orthogonal frequency-division multiplexing (OFDM) systems, channel estimation is required for guaranteeing the transmission quality over rapidly changing wireless channels. At the same time, it is crucial to recover the clipping signal when resolving the high peak average power ratio (PAPR) of the transmitted OFDM signal. In this letter, we apply the deep learning (DL) technique to boost the performance of channel estimation in the protograph low-density parity-check (PLDPC)-coded bit-interleaved coded modulation (BICM)-aided OFDM (BICM-OFDM) systems. Specifically, we propose a channel estimation residual network (CERNet) to estimate the channel state information (CSI). Furthermore, a signal recovery residual network (SRRNet) is designed to recover the clipped signal. Our proposed residual networks can capture the frequency-specific features of the channel matrices and the correlation of the clipping noise over the received data signal adequately without relying on explicit priori channel information to further improve the channel estimation performance. Both analytical and simulation results show that the CERNet achieves superior performance compared with the conventional estimation scheme, and the joint CERNet and SRRNet can further improve the system performance.

## Integration of a Real-Time CCSDS 410.0-B-32 Error-Correction Decoder on FPGA-Based RISC-V SoCs Using RISC-V Vector Extension

- **Status**: ❌
- **Reason**: NB-LDPC over GF(16) min-max decoder — 비이진 LDPC라 제외 원칙 적용
- **ID**: ieee:10098873
- **Type**: journal
- **Published**: Oct. 2023
- **Authors**: Yao-Ming Kuo, Mark F. Flanagan, Francisco Garcia-Herrero +2
- **PDF**: https://ieeexplore.ieee.org/document/10098873
- **Abstract**: The Consultative Committee for Space Data Systems (CCSDS) recommends the use of short-block length Bose–Chaudhuri–Hocquenghem and binary low-density parity-check codes. Despite the high error-correction capacity of nonbinary low-density parity-check (NB-LDPC) codes, they have not yet been considered due to their high decoding complexity. In this article, the feasibility of NB-LDPC coding for space telecommand link applications using an RISC-V soft-core processor plus a vector coprocessor is demonstrated. The purpose of this article is to avoid the need for a dedicated decoder hardware, and thus, the customized general-purpose processor that performs decoding can be reconfigured to perform other important onboard tasks. In this way, the logic utilization and power consumption can be reduced since more functionalities can be assumed by the onboard processor. The method of acceleration of an NB-LDPC decoder over GF(16) using the RISC-V vector extension is demonstrated, and a throughput of 8.48 kb/s is achieved for the forward–backward implementation of the min–max decoding algorithm, which is compatible with the low-rate and mid-rate telecommand systems recommended by the CCSDS.

## Polar-Coding-Assisted Blind Frame Synchronization Based on Soft Information of Frozen Bits

- **Status**: ❌
- **Reason**: polar 부호 블라인드 프레임 동기화 — LDPC 비교대상일 뿐, 이식 디코더/구성 기법 없음
- **ID**: ieee:10233689
- **Type**: journal
- **Published**: Oct. 2023
- **Authors**: Zhongxiu Feng, Yuan Liu, Shengyu Zhang +2
- **PDF**: https://ieeexplore.ieee.org/document/10233689
- **Abstract**: In this letter, we propose a polar-coding-assisted blind frame synchronization (BFS) method with the aid of soft information of frozen bits. Specifically, a synchronization metric associated with the probability of correctly estimating the frozen bit sequence is designed. Then, a low-complexity approximation of the synchronization metric is derived and amalgamated with successive cancellation list decoding of polar codes. Finally, the simulation results demonstrate that the proposed method is capable of achieving superior frame synchronization error rate performance over the existing BFS based on low-density parity-check codes.

## Clipping Noise Cancellation Receiver for the Downlink of Massive MIMO OFDM System

- **Status**: ❌
- **Reason**: mMIMO OFDM 클리핑 잡음 제거 수신기 — LDPC 무관, 떼어낼 ECC 기법 없음
- **ID**: ieee:10175641
- **Type**: journal
- **Published**: Oct. 2023
- **Authors**: Marcin Wachowiak, Pawel Kryszkiewicz
- **PDF**: https://ieeexplore.ieee.org/document/10175641
- **Abstract**: Massive multiple-input multiple-output (mMIMO) technology is considered a key enabler for the 5G and future wireless networks. In most wireless communication systems, mMIMO is employed together with orthogonal frequency-division multiplexing (OFDM) which exhibits a high peak-to-average-power ratio (PAPR). While passing the OFDM signal through one of the common RF front-ends of limited linearity, significant distortion of the transmitted signal can be expected. In mMIMO systems, this problem is still relevant as in some channels the distortion component is beamformed in the same directions as the desired signal. In this work, we propose a multi-antenna clipping noise cancellation (MCNC) algorithm for the downlink of the mMIMO OFDM system. Computer simulations show it can remove nonlinear distortion even under severe nonlinearity. Next, a simplified version of the algorithm is proposed. It was observed that for the direct visibility channels, its performance is only slightly degraded with respect to the MCNC algorithm.

## Optimal and Asymptotically Good Locally Repairable Codes via Propagation Rules

- **Status**: ❌
- **Reason**: locally repairable codes 전파규칙 구성 — LDPC 디코더/HW 아닌 일반 블록부호 이론, NAND LDPC 이식 기법 없음
- **ID**: ieee:10172314
- **Type**: journal
- **Published**: Oct. 2023
- **Authors**: Jin Yi Chen, Shu Liu, Liming Ma +2
- **PDF**: https://ieeexplore.ieee.org/document/10172314
- **Abstract**: In classical coding theory, it is common to construct new codes via propagation rules. There are various propagation rules to construct classical block codes. However, propagation rules have not been extensively explored for locally repairable codes. In this paper, we systematically study some of propagation rules to construct optimal and asymptotically good locally repairable codes. To our surprise, these simple propagation rules produce interesting results. Firstly, by a lengthening propagation rule that adds some rows and columns to a parity-check matrix of a given linear code, we are able to convert a classical maximum distance separable (MDS) code into a Singleton-optimal locally repairable code and provide a simplified proof of the asymptotic Tafasman-Vlăduţ-Zink bound which exceeds the asymptotic Gilbert-Varshamov bound of locally repairable codes. Secondly, by concatenating a locally repairable code as an inner code with a classical block code as an outer code, we obtain a family of dimension-optimal locally repairable codes. Thirdly, we can make use of the shortening technique to produce more dimension-optimal locally repairable codes. Finally, one of phenomena that we observe in this paper is that some trivial propagation rules in classical block codes do not hold anymore for locally repairable codes.

## Beyond Integer-Forcing Receiver for Lattice-Code Based Multi-User MIMO System

- **Status**: ❌
- **Reason**: lattice-code 기반 MU-MIMO integer-forcing 수신 — q-ary 격자부호 검출, NAND 바이너리 LDPC 이식 기법 없음
- **ID**: ieee:10185628
- **Type**: journal
- **Published**: Oct. 2023
- **Authors**: Tao Yang
- **PDF**: https://ieeexplore.ieee.org/document/10185628
- **Abstract**: This letter studies a lattice-code based multi-user MIMO system. In the uplink,  $K$  single-antenna users encode their messages with the same  $q$ -ary linear code mapped to  $q$ -PAM, belonging to the ensemble of lattice codes. The  $N_{R}$ -antenna receiver attempts to compute  $K$  independent streams of integer-combinations (ICBs) of the users’ messages. To this end, we put forth a new interference-whitening (IW) based ICB detection method, which reduces the loss of the linear filtering operation in existing integer-forcing (IF). The soft detection outputs are forwarded to  $K$  channel-code decoders to recover the messages. For practical configurations with moderate-to-large  $K$ , the proposed ICB detection exhibits an enlarged achievable mutual information and considerably improved FER performance, over existing IF.

## Non-Coherent Active Device Identification for Massive Random Access

- **Status**: ❌
- **Reason**: mMTC 능동단말 식별(group testing) — BP/COMP는 활성검출용, LDPC ECC 디코더 기법 아님
- **ID**: ieee:10198448
- **Type**: journal
- **Published**: Oct. 2023
- **Authors**: Jyotish Robin, Elza Erkip
- **PDF**: https://ieeexplore.ieee.org/document/10198448
- **Abstract**: Massive Machine-Type Communications (mMTC) is a key service category in the current generation of wireless networks featuring an extremely high density of energy and resource-limited devices with sparse and sporadic activity patterns. In order to enable random access in such mMTC networks, base station needs to identify the active devices while operating within stringent access delay constraints. In this paper, an energy efficient active device identification protocol is proposed in which active devices transmit On-Off Keying (OOK) modulated preambles jointly and base station employs non-coherent energy detection avoiding channel estimation overheads. The minimum number of channel-uses required by the active user identification protocol is characterized in the asymptotic regime of total number of devices  $\ell $  when the number of active devices  $k$  scales as  $k=\Theta (1)$  along with an achievability scheme relying on the equivalence of activity detection to a group testing problem. Several practical schemes based on Belief Propagation (BP) and Combinatorial Orthogonal Matching Pursuit (COMP) are also proposed. Simulation results show that BP strategies outperform COMP significantly and can operate close to the theoretical achievability bounds. In a partial-recovery setting where few misdetections are allowed, BP continues to perform well.

## A Rate-Compatible Solution to the Set Reconciliation Problem

- **Status**: ❌
- **Reason**: IBLT 집합 일치 프로토콜(MET-IBLT) — 통신복잡도 문제, 채널코딩 ECC 디코더/구성 아님
- **ID**: ieee:10185962
- **Type**: journal
- **Published**: Oct. 2023
- **Authors**: Francisco Lázaro, Balázs Matuz
- **PDF**: https://ieeexplore.ieee.org/document/10185962
- **Abstract**: We consider a set reconciliation setting in which two parties hold similar sets that they would like to reconcile. In particular, we focus on set reconciliation based on invertible Bloom lookup tables (IBLTs), a probabilistic data structure inspired by Bloom filters. IBLT-based set reconciliation schemes have the advantage of exhibiting low computational complexity, however, the schemes available in the literature are known to be far from optimal in terms of communication complexity (overhead). The inefficiency of IBLT-based set reconciliation can be attributed to two facts. First, it requires an estimate of the cardinality of the difference between the sets, which implies an increase in overhead. Second, to cope with uncertainties in the estimation of the cardinality of the set difference, IBLT schemes in the literature oversize the data structures, thus further increasing the overhead. In this work, we present a novel IBLT-based set reconciliation protocol that does not require estimating the cardinality of the set difference. The proposed scheme relies on what we termed multi-edge-type (MET) IBLTs. The simulation results illustrate that the novel scheme outperforms state-of-the-art IBLT-based approaches to set reconciliation in terms of communication cost, i.e., in terms of the number of bits to be exchanged.

## Performance Analysis of RS-Coded UOWC System under Gamma-Gamma Fading Channels for IoUT Applications

- **Status**: ❌
- **Reason**: 수중 광통신(IoUT)에서 RS 부호 성능분석. LDPC 아님, 떼어낼 ECC 기법 없음
- **ID**: ieee:10353246
- **Type**: conference
- **Published**: 6-8 Oct. 2
- **Authors**: Dushyant Singh Chauhan, Gurjit Kaur, Dinesh Kumar
- **PDF**: https://ieeexplore.ieee.org/document/10353246
- **Abstract**: The Internet of Underwater Things (IoUT) is an emerging technology that allows underwater equipment to interact with each other and allows information exchange. Underwater wireless communication networks with little bandwidth and high error rates are key difficulties in IoUT. Turbulence-induced fading is a significant performance degrader for underwater optical wireless communication equipment. Many communication systems use Reed Solomon (RS) codes to minimize channel defects and boost transmission reliability. We propose an RS code with multiple modulation techniques in this research to combat turbulence-induced fading in IoUT applications. We present an in-depth investigation of the coding gain realized by RS coding in UOWC channels, as well as an assessment of bit error rate (BER) performance for various code rates, message lengths, and channel conditions. Our simulation results show that RS coding can significantly improve UOWC channel BER performance and allow for more reliable communication in IoUT applications at higher data rates. Following that, the closed-form expression of the BER without forward error correction (FEC) code is created using the gamma-gamma (GG) fading model. Our findings demonstrate the value of RS coding in UOWC for IoUT applications and provide critical insights for the design of robust IoUT systems.

## Research on Full Link Monitoring and Fault Link Automatic Repair Based on Data Center

- **Status**: ❌
- **Reason**: 데이터센터 링크 모니터링·자동복구 시스템. ECC/LDPC 무관
- **ID**: ieee:10471706
- **Type**: conference
- **Published**: 6-8 Oct. 2
- **Authors**: Jiali Sun, Cong Hu, Ruixuan Lu +5
- **PDF**: https://ieeexplore.ieee.org/document/10471706
- **Abstract**: In this paper, the data center is taken as the object of study, the whole link monitoring mechanism with the data center as the core is studied, the whole system structure of the data link monitoring is constructed, the link monitoring flow is explained, and the link automatic repair technology is used, the classification of link failure is realized, and corresponding maintenance methods are adopted for different faults. This paper takes the whole-link Monitoring System of data center station as the research object, breaks through the single monitoring means, establishes the whole-link monitoring capability, and promotes the formation of the whole-link monitoring and the automatic repair method of applaud link covering the whole life cycle of data.

## A family of binary sequences derived from punctured simplex codes

- **Status**: ❌
- **Reason**: punctured simplex 코드 기반 PN 시퀀스의 상관 특성 — ranging/동기화용, LDPC ECC 기법 아님
- **ID**: ieee:10330406
- **Type**: conference
- **Published**: 5-7 Oct. 2
- **Authors**: Massimo Battaglioni, Giovanni Cancellieri
- **PDF**: https://ieeexplore.ieee.org/document/10330406
- **Abstract**: In this paper we examine the relationship between the correlation properties of Pseudo-Noise sequences and the weight distribution of punctured simplex codes. To facilitate analysis we introduce the concept of “complementary” code and use it to minimize partial period autocorrelation. The main objective is to identify a family of sequences with enhanced correlation performance, by leveraging the theory of error correcting codes. The partial period autocorrelation properties of these sequences make them suitable for ranging and synchronizations application.

## Challenges for designing an FPGA-based data link layer processor dedicated to sub-THz communication

- **Status**: ❌
- **Reason**: sub-THz FPGA 데이터링크 계층 처리; FEC 부수 언급, 떼어낼 LDPC 디코더/구성 기법 없음
- **ID**: ieee:10320062
- **Type**: conference
- **Published**: 4-6 Oct. 2
- **Authors**: Yiyun Jian, Lukasz Lopacinski, Klaus Tittelbach-Helmrich +3
- **PDF**: https://ieeexplore.ieee.org/document/10320062
- **Abstract**: This paper discusses the challenges of implementing beam management algorithms, forward error correction, automatic repeat request, data aggregation, and data fragmentation in a state-of-the-art field programmable gate arrays (FPGA) platform considering wireless communication in the sub-THz band at frequencies between 100 GHz and 300 GHz. A data link layer architecture is proposed, which supports the processing of the data frames directly in the FPGA logic for reduced latency, while the beam management is delegated to a software processor. This approach can significantly simplify data link layer processor implementation and improve efficiency.

## Adaptive LDPC FEC for ZP-OFDM Underwater Acoustic Communication Systems

- **Status**: ❌
- **Reason**: 수중음향 ZP-OFDM 적응형 LDPC 코드레이트; 표준 패리티/생성행렬 설계로 새 디코더·구성 기여 없음
- **ID**: ieee:10425421
- **Type**: conference
- **Published**: 3-6 Oct. 2
- **Authors**: P.P. Unru, A.Yu. Rodionov, A.V. Kirianov +1
- **PDF**: https://ieeexplore.ieee.org/document/10425421
- **Abstract**: Research and exploration of the ocean environment face various challenges and engineering problems. One of them is data transmission underwater, which is vital for properly using autonomous underwater vehicles. Due to immensely higher attenuation, communication systems based on electromagnetics cannot be used on distances over several tens of meters. The only way to communicate with submerged vehicles is through underwater acoustic communication systems. Sound propagation underwater heavily depends on sound speed distribution and acoustic properties and the form of the sea surface and bottom. These parameters are non-stationary or suffer from local and unpredictable inhomogeneities, causing high variability of channel bit error rate (BER) and complicating the assessment of proper parameters of underwater acoustic communications systems (UACS), including forward error correction (FEC) coder. The paper presents an adaptation method for the code rate of the low-density parity-check (LDPC) coder without two-way channel estimation. The method for the design of parity-check and generator matrices, coding, and decoding processes are also described. The effectiveness of the proposed adaptive LDPC FEC is validated through simulations, and its results are provided.

## Performance Analysis of Coded CSOC-Assisted Energy Harvesting AF Dual-hop RF/FSO System

- **Status**: ❌
- **Reason**: RF/FSO 시스템 CSOC+MLGD 분석; LDPC 무관, NAND 이식 기법 없음
- **ID**: ieee:10322972
- **Type**: conference
- **Published**: 26-28 Oct.
- **Authors**: Souad Labghough, Fouad Ayoub, Faissal El Bouanani +2
- **PDF**: https://ieeexplore.ieee.org/document/10322972
- **Abstract**: In this paper, we investigate the average bit error probability (ABEP) performance of a relaying radio- frequency/free-space optic (RF/FSO) coded and uncoded communication system employing an energy harvesting-based fixed gain amplify-and-forward (AF) relay. Along with maximal-ratio combining (MRC) at both nodes, the convolutional self orthogonal codes and majority logic decoding method (MLGD) are explicitly examined at the source and destination, respectively. In addition, the source-relay channel experiences i.n.i.d. Nakagami-m fading, while the relay-destination link is modeled by Málaga-$\mathcal{M}$ fading with the effect of pointing errors taking into account many apertures at the destination. Due to the significant coding benefits that these codes offer, the results of the Monte Carlo simulation proved that the proposed decoding technique is adequate for such communication.

## A Simple Cascade Channel Estimation Method for UAV RIS-Enabled Millimeter Wave Transmissions

- **Status**: ❌
- **Reason**: UAV-RIS mmWave 채널추정; LDPC는 오버헤드 비교에 부수 언급, 떼어낼 ECC 기법 없음 (무선 응용 특이적)
- **ID**: ieee:10322913
- **Type**: conference
- **Published**: 26-28 Oct.
- **Authors**: Kutluhan Taylan İren, Tolga Girici
- **PDF**: https://ieeexplore.ieee.org/document/10322913
- **Abstract**: Reconfigurable Intelligent Surfaces (RIS) is an emerging concept in Sixth Generation (6G) technologies. RIS can manipulate the wireless communication environment and provide virtual Line of Sight (LOS) links between a Base Station(BS) and User Equipment (UE) by controlling the coefficients of passive reflecting elements. RIS is a promising concept with its passive and low-cost nature. However, RIS-enabled transmission experiences double scattering and high path loss. Besides, it requires a massive number of elements in the millimeter-wave(mmWave) and sub-TeraHertz(THz), which makes channel estimation a complicated problem. There are quite a number of diverse methods in recent literature. In this work we assume a Unmanned Aerial Vehicle(UAV)-mounted RIS that provides a line of sight. We propose a simple cascade channel estimation method and compare its performance with that of a recently proposed channel estimation scheme. We perform comparisons, taking the overhead caused by Fifth Generation (5G) Low Density Parity Check (LDPC) coding and channel estimation overhead into account. Simulations show that our proposal achieves a much better spectral efficiency.

## Efficient Search Path Reduction for NB-LDPC Codes with T-EMS Algorithm

- **Status**: ❌
- **Reason**: NB-LDPC(GF(q)) T-EMS 디코더 — 비이진 LDPC 즉시 제외
- **ID**: ieee:10396515
- **Type**: conference
- **Published**: 24-27 Oct.
- **Authors**: Xuewei Quan, Houren Ji, Xiaohu You +1
- **PDF**: https://ieeexplore.ieee.org/document/10396515
- **Abstract**: In comparison to the forward-backward update of extended min-sum (EMS) algorithm, the trellis EMS (T-EMS) algorithm for non-binary low density parity check codes (NB-LDPC) introduces an extra trellis column during check nodes (CNs) updates, significantly enhancing parallelism and facilitating hardware implementation. However, in high-order or high code rate scenarios, the T-EMS algorithm exhibits considerable latency caused by excessive configurations searching for the largest reliability selection. To address this, the paper propose an enhanced algorithm, named as path reduction T-EMS (RT-EMS) algorithm, to simplify the configuration space through applying an additional filtering to the elements in each column of the trellis, retaining only the elements that are deemed more trustworthy from the column’s perspective. Moreover, a data compensation strategy is also proposed to tackle the data scarcity issues for some syndrome values in the extra trellis column. Finally, the simulation results demonstrate that RT-EMS algorithm can achieve more than 50% complexity reduction with a negligible performance degradation.

## Generalized Belief Propagation Decoding of Polar Codes

- **Status**: ❌
- **Reason**: Polar 코드 일반화 BP 디코딩 — LDPC 아닌 폴라 팩터그래프 변환 전용
- **ID**: ieee:10330195
- **Type**: conference
- **Published**: 24-27 Oct.
- **Authors**: Nikolai Iakuba, Peter Trifonov
- **PDF**: https://ieeexplore.ieee.org/document/10330195
- **Abstract**: A generalized belief propagation algorithm is proposed for decoding of polar codes. The proposed approach relies on offline successive transformations of the factor graph, which merge parity check nodes into check nodes corresponding to some non-trivial codes. It was shown, that the constructed factor graph for (2048, 1024) polar code provides 0.25 performance gain under generalized belief propagation decoding with 5 iterations and lower worst case complexity compared to state-of-the-art belief propagation decoders of polar codes.

## A Reaction Attack against Cryptosystems Based on Quasi–Group MDPC Codes

- **Status**: ❌
- **Reason**: QC-MDPC 암호시스템 reaction 공격(post-quantum 보안), 비이진 포함 — ECC 디코더/구성 이식 기법 아님
- **ID**: ieee:10330086
- **Type**: conference
- **Published**: 24-27 Oct.
- **Authors**: Kirill Vedenev, Yury Kosolapov
- **PDF**: https://ieeexplore.ieee.org/document/10330086
- **Abstract**: Cryptosystems based on quasi–cyclic moderate density parity–check (QC–MDPC) codes are considered among the most perspective post–quantum public–key encryption schemes due to small public–key sizes and excellent performance. However, due to probabilistic decoding of MDPC codes, there is non–zero decryption failure rate. In 2016, Q. Guo, T. Johansson, P. Stankovski showed that decryption failures can be used to construct a key–recovery attack against QC–MDPC cryptosystems. Recently, in order to mitigate GJS attack, P. Santini, E. Persichetti, and M. Baldi proposed generalization of quasi–cyclic codes called quasi–reproducible (QR) codes and QR–MDPC cryptosystems. In this paper, we consider cryptosystems based on binary and non–binary quasi–group (QG) MDPC codes and propose a generalization of GJS reaction attack against these cryptosystems. We show that many efficient QR–MDPC cryptosystems are in fact equivalent to QG–MDPC cryptosystems, making the proposed attack applicable to them as well.

## Design of non-binary polar codes with shaping

- **Status**: ❌
- **Reason**: 비이진 polar subcode shaping — LDPC도 아니고 non-binary, 이중 제외
- **ID**: ieee:10330203
- **Type**: conference
- **Published**: 24-27 Oct.
- **Authors**: Liudmila Karakchieva, Peter Trifonov
- **PDF**: https://ieeexplore.ieee.org/document/10330203
- **Abstract**: A method for construction of non-binary polar (sub)codes with shaping is proposed. It is based on the Honda-Yamamoto scheme and does not require multilevel (ML) coding framework. Polar codes with conventional Reed-Solomon kernel, as well as the generalized Reed-Solomon kernel are considered. Simulation results show that non-binary polar (sub)codes with generalized Reed-Solomon kernel provide better shaping gain and performance compared to ML binary polar (sub)codes under list successive cancellation decoding.

## Method of Critical Set construction for Successive Cancellation List Decoder of Polar Codes Based on Deep Learning of Neural Networks

- **Status**: ❌
- **Reason**: Polar SCL 디코더용 임계집합 신경망 구성 — LDPC 아님, 폴라 전용 기법
- **ID**: ieee:10330189
- **Type**: conference
- **Published**: 24-27 Oct.
- **Authors**: Feodosii Kotov, Fedor Ivanov, Ilya Timokhin
- **PDF**: https://ieeexplore.ieee.org/document/10330189
- **Abstract**: The Successive Cancellation List (SCL) algorithm is a widely used decoding technique in communication systems. However, constructing the critical set for SCL decoding is a challenging task, as it requires a large number of computations and can lead to significant decoding delays. In this paper, a new approach to critical set construction for SCL decoding is proposed, which is based on deep learning of neural networks with special structure and activation functions.The proposed method is shown to significantly reduce the cardinality of the critical set required for achieving the target frame error rate, when used with an SCL decoder with a list size of 8. Simulation results demonstrate that the proposed method outperforms existing methods in terms of reducing decoding delay, while maintaining high decoding accuracy.The key innovation of the proposed approach lies in the use of deep learning techniques to learn the structure of the critical set, which enables the construction of a more efficient and compact set. This approach has the potential to significantly improve the performance of SCL decoding in practical communication systems, where decoding delay is a critical factor.

## Network Coding to Reduce Congestion and Improve Memory Buffer in Smart Switch

- **Status**: ❌
- **Reason**: 데이터센터 스위치 네트워크 코딩(NCSSDDA) 혼잡 제어; LDPC ECC와 무관
- **ID**: ieee:10323947
- **Type**: conference
- **Published**: 23-26 Oct.
- **Authors**: Souryendu Das, Stavros Kalafatis
- **PDF**: https://ieeexplore.ieee.org/document/10323947
- **Abstract**: Content Distribution Networks (CDNs) are gaining popularity with an ever increasing demand of streaming services. As enterprises manage larger amounts of data, they are continuously researching improvements for their data center networks. Various algorithms have been proposed to diligently manage these needs. This paper proposes a new algorithm called NCSSDDA (Network Coded SSSDDA) which incorporates network coding to improve the performance of an existing algorithm called SSDDA (Smart Switch Dynamic Delay Algorithm) in a data center network. The NCSSDDA algorithm aims to reduce packet drop rates and memory consumption of switch memory buffer, with a slight tradeoff of reduced line rate. Experiments were conducted in a data center rack with multiple endpoint servers and results show that the NCSSDDA algorithm provides algorithmic benefits over the original SSDDA.

## LDPC assisted GAMP for PAPR reduction in Super-QAM OFDM

- **Status**: ❌
- **Reason**: Super-QAM OFDM의 PAPR 감소를 위한 GAMP 수신기에 LDPC 결합; 무선 응용 특이적, 떼어낼 ECC 기법 없음
- **ID**: ieee:10372912
- **Type**: conference
- **Published**: 23-25 Oct.
- **Authors**: João Madeira, Zahra Mokhtari, João Guerreiro +1
- **PDF**: https://ieeexplore.ieee.org/document/10372912
- **Abstract**: The procurement of higher data rates has motivated significant research into supporting very high order M-ary Quadrature Amplitude Modulation (M-QAM), also known as Super-QAM, combined with Orthogonal Frequency Division Multiplexing (OFDM). Unmitigated, the high Peak-to-Average Power Ratio (PAPR) of OFDM signals results in very low amplification efficiency. However, schemes that improve efficiency can introduce distortion in the transmitted signal, which is particularly challenging for Super-QAM schemes. We propose a simple PAPR reduction operation at the transmitter, which is combined with a Generalized Approximate Message Passing (GAMP) receiver, which is known to cope with nonlinear distortion. It is shown that GAMP’s convergence can be greatly improved by incorporating a Low Density Parity Check (LDPC) code within the GAMP detection algorithm, which allows for significantly low PAPR values.

## Comparison of LDPC codes based on CCSDS standard and 5G standard in underwater channels

- **Status**: ❌
- **Reason**: CCSDS/5G 표준 LDPC를 표준 normalized min-sum으로 수중채널 비교만, 새 기여 없음 — 표준 부호·기법 단순 재사용
- **ID**: ieee:10303868
- **Type**: conference
- **Published**: 20-23 Oct.
- **Authors**: Chong He, Junyan Ma, Hongfei Lv +3
- **PDF**: https://ieeexplore.ieee.org/document/10303868
- **Abstract**: In the process of information transmission, in order to provide the system with certain error correction and anti-interference capabilities, the participation of channel coding is required. Low Density Parity Check (LDPC) codes, as a member of linear block codes, have been increasingly used in recent years. In order to adapt to different scenarios and address the main impacts during transmission, LDPC codes based on multiple standards have emerged, but no standards suitable for underwater channel transmission have emerged. In this article, in order to find more suitable LDPC codes for underwater channel transmission, LDPC codes based on two standards were selected. The underwater channel was simulated using a generalized gamma distribution model, and the same normalized minimum sum decoding method was used. Starting from two aspects of iteration times and normalization factors, this paper analyzes the error rate of LDPC codes based on the Consultative Committee for Space Data Systems (CCSDS) and the 5th Generation mobile communication systems (5G) standards in underwater channel transmission to determine the performance of these two LDPC codes. It was found that LDPC codes based on the CCSDS standard have significant advantages in low signal-to-noise ratio situations and have better performance in underwater channel transmission.

## Performance Comparison of Concatenated Codes with Repetitive Code in Slow Frequency Hopping Communication

- **Status**: ❌
- **Reason**: FH 시스템 연접부호 비교, LDPC는 외부부호 후보 중 하나로 표준 사용 — 떼어낼 기법 없음
- **ID**: ieee:10419409
- **Type**: conference
- **Published**: 20-22 Oct.
- **Authors**: Lei Yao, Junshan Luo, Shilian Wang +1
- **PDF**: https://ieeexplore.ieee.org/document/10419409
- **Abstract**: Frequency hopping (FH) is a widely employed communication technique for countering jamming. However, the robustness can significantly degrade when jamming signals align with the hopping frequencies. To address this issue, channel coding is employed as an effective solution. This study focuses on the optimization of concatenated codes for a slow FH system that experiences a high probability of jamming. Additionally, a more universal jamming model is proposed. The performance of concatenated codes employing tail-biting Turbo code, Polar code, and LDPC code as the outer code, combined with repetitive code as the inner code, is meticulously evaluated. Numerical results demonstrate that both tail-biting Turbo code-repetitive code and Polar code-repetitive code achieve reliable transmission, even under an 80% probability of jamming. Notably, reducing the code rate of the repetitive code, rather than the outer code rate, proves to be an effective approach for enhancing the system's resilience to jamming while reducing decoding complexity.

## Decoding-Aided Channel Tracking in Time-Varying MIMO Systems: Short or Long Codes?

- **Status**: ❌
- **Reason**: MIMO 채널 추적(Kalman) + short/long code 비교; 떼어낼 LDPC 디코더/HW/코드설계 기법 없음, 무선 응용 특이적
- **ID**: ieee:10419669
- **Type**: conference
- **Published**: 20-22 Oct.
- **Authors**: Lin Zhao, Hongmei Kang, Yi Sun +3
- **PDF**: https://ieeexplore.ieee.org/document/10419669
- **Abstract**: Multiple-input multiple-output (MIMO) technology significantly improves spectral efficiency and energy efficiency by fully exploiting the spatial resources of the wireless channel. However, the channels can be time-varying due to the mobility of the users in practice, which leads to a non-negligible mismatch of the channel state information (CSI) acquired based on the pilots and the one corresponding to the data transmission stage, and furthermore, the performance deterioration. To handle this, this paper investigates a decoding-aided channel tracking algorithm, where both the detected symbols and the decoded output are utilized to improve the CSI accuracy based on the framework of Kalman filtering. Specifically, instead of the commonly-used long length codes, we adopt short length codes as the coding scheme to enable the fast decoding-aided channel tracking. It is interesting to find via simulations that, the proposed channel tracking algorithm with the use of short length codes can effectively mitigate the effect of channel aging and can even outperform the one using powerful long length codes.

## Channel Estimation and Reflecting Design of RIS-Aided Coded Systems Over Time-Varying Channels

- **Status**: ❌
- **Reason**: RIS 채널추정+반사계수 설계(Kalman/PSO); LDPC ECC 이식 기법 없는 무선 응용
- **ID**: ieee:10419713
- **Type**: conference
- **Published**: 20-22 Oct.
- **Authors**: Hongmei Kang, Lin Zhao, Yi Sun +3
- **PDF**: https://ieeexplore.ieee.org/document/10419713
- **Abstract**: Reconfigurable intelligent surface (RIS) is popular in recent years as a promising technology for future wireless networks. However, the bottleneck still exists due to the accurate channel state information is quite difficult to obtain. This paper investigates the estimation of a cascaded channel and the design of an optimal reflection coefficient matrix during data transmission in an RIS-aided coded system when the channel is rapidly time-variant. Moreover, the Kalman filter is proposed to optimize the channel estimation which utilizes the time correlation of the channel. Meanwhile, the decoded information can be fully exploited to assist the channel estimation, which is highly spectral-efficient. Besides, the paper introduces a particle swarm optimization algorithm to find the optimal reflection coefficient matrix based on the maximum achievable rate during data transmission. Numerical results present the proposed methods can utilize a few pilot signals to obtain excellent performance.

## Variable Rate Non-Binary Coded Schemes Based on PSK-LoRa Modulation and LDPC Codes

- **Status**: ❌
- **Reason**: PSK-LoRa용 비이진(non-binary) LDPC — 비이진 LDPC는 제외 대상
- **ID**: ieee:10461420
- **Type**: conference
- **Published**: 2-4 Oct. 2
- **Authors**: Jocelyn Bourduge, Charly Poulliat, Benjamin Gadat +1
- **PDF**: https://ieeexplore.ieee.org/document/10461420
- **Abstract**: We investigate PSK-LoRa modulation, which serves as an alternative to LoRa by introducing additional information in the phase using Phase-Shift Keying (PSK) symbols. This extension of LoRa provides flexibility in achieving spectral efficiency gains while maintaining a constant envelope. To fully leverage the advantages of PSK-LoRa, we propose a variable nonbinary coded scheme that allows for varying the proportion of bits associated with LoRa modulation and PSK modulation, while maintaining a fixed number of bits per PSK-LoRa symbol. This approach enables coverage of a wide range of spectral efficiencies using a single outer error-correcting code for all inner modulation schemes. We demonstrate that regular non-binary LDPC (Low- Density Parity-Check) codes are highly effective for our scheme based on PSK-LoRa for the Gaussian channel. However, due to a lack of diversity offered by the receiver, the performance of these codes are significantly penalized for the Rayleigh channel. Hence, we investigate quasi-regular, precoded punctured, and irregular codes for the Rayleigh channel. We illustrate that irregular nonbinary LDPC codes emerge as strong candidates for both the Gaussian and Rayleigh channels.

## A Comparative Study of Linear Block Channel Codes in Macroscale Molecular Communications

- **Status**: ❌
- **Reason**: 분자통신에서 Hamming/RS/LDPC 부호 성능 비교 서베이성 연구, 신규 디코더/구성/HW 기여 없음
- **ID**: ieee:10461399
- **Type**: conference
- **Published**: 2-4 Oct. 2
- **Authors**: Pit Hofmann, Juan A. Cabrera, Riccardo Bassoli +1
- **PDF**: https://ieeexplore.ieee.org/document/10461399
- **Abstract**: Molecular communication (MC) has emerged as a promising paradigm for enabling communication between nanoscale devices and macroscopic systems. In this context, channel coding plays a crucial role in mitigating the adverse effects of noise, and inter-symbol interference (ISI) in MC channels. This paper presents a comprehensive comparative study of various channel coding schemes (linear block codes, f.e. Hamming codes, Reed-Solomon (RS) codes, and low-density parity-check (LDPC) codes) in the macroscale MC domain. The objective is to analyze and evaluate the performance of different coding techniques in terms of the data rate, the code rate, and the bit error ratio (BER) on the error pattern of a macroscale MC testbed. In this paper, we show an up to 50% gain in the BER of a drift-assisted macroscale MC coded system compared to the uncoded case. The findings provide valuable insights into the benefits and limitations of different channel coding schemes. Thereby, the results demonstrate the potential of channel coding schemes to enhance the performance and reliability of macroscale MC networks, paving the way for the integration into future nanoscale communication applications.

## Invited Talk #1: Joint source-channel coding systems based on double-protograph low-density parity-check codes

- **Status**: ❌
- **Reason**: JSCC 소스-채널 결합 초청강연(서베이성), LDPC 베이스라인, 떼어낼 신규 채널 ECC 기법 없음
- **ID**: ieee:10318894
- **Type**: conference
- **Published**: 19-21 Oct.
- **Authors**: C.M Francis Lau
- **PDF**: https://ieeexplore.ieee.org/document/10318894
- **Abstract**: Designing source code and channel code separately is optimal when the code length is very long. For application scenarios requiring short to moderate code lengths, designing source code and channel code jointly can provide a higher coding gain. The main idea of jointly designing source-channel code (JSCC) is to exploit the residual redundancy of the source in the tandem joint source-channel encoding/decoding algorithms so as to achieve coding gains. Low-density parity-check (LDPC) codes have been widely used in many communication systems because of their capacity-approaching error correction capability. Recently, protography-based LDPC codes have been applied to designing JSCC systems. In this talk, we will present the architecture of such JSCC systems, including the encoding and decoding mechanisms. We will also introduce the mathematical techniques for analyzing the thresholds of such systems. Finally, we will show some hardware implementation results and some future research directions.

## Field Trial on DTMB-A for the Coverage Performance of HDTV Program Under High Mobility and Spectrum Efficiency

- **Status**: ❌
- **Reason**: DTMB-A/3GPP 방송 커버리지 필드 트라이얼, time-interleaver 위주 — 떼어낼 LDPC ECC 기법 없음
- **ID**: ieee:10318585
- **Type**: conference
- **Published**: 19-20 Oct.
- **Authors**: Jian Song, Changyong Pan, Kewu Peng +4
- **PDF**: https://ieeexplore.ieee.org/document/10318585
- **Abstract**: The coverage performance for Digital Television/ Terrestrial Multimedia Broadcasting-Advance system and 3GPP “Further evolved Multimedia Broadcast Multicast Service”, long-term evolution-based broadcasting system defined by release 16 (R16) with different working parameters has been evaluated through the field trial in Shenzhen with a focus on high-speed mobility car with reasonably high spectrum efficiency. The trial uses the same transmitter facility of same the RF hardware, at the same frequency and with the same power. Results show that terrain is major deterministic factor for coverage performance for each system and well-designed longer time-interleaver for R16 is indispensable to users' satisfaction under this application scenario.

## Research on Adaptive Coding Modulation Technique of Atmospheric Optical Communication Based on LDPC Code

- **Status**: ❌
- **Reason**: 대기광통신 적응변조 임계값 스위칭 응용. LDPC 부수 언급, 떼어낼 디코더/코드설계 기법 없음
- **ID**: ieee:10367294
- **Type**: conference
- **Published**: 13-16 Oct.
- **Authors**: Yuyou Guo, Zhi Liu, Haifeng Yao +2
- **PDF**: https://ieeexplore.ieee.org/document/10367294
- **Abstract**: Aiming at the problem that the transmission mode switching threshold is not accurate due to turbulence in atmospheric optical communication, a threshold switching selection method based on LDPC coding combined with BPSK modulation is proposed. The performance of lognormal channel model under weak turbulence conditions was analyzed, Monte Carlo method was used to simulate weak turbulence channel fading, and the formula for the relationship between turbulence intensity and signal-to-noise ratio threshold was given. The logarithmic variance of light intensity scintillation index was used as the turbulence intensity index, and the simulated weak turbulence intensity was 0,0.05, 0.15. The relationship between bit error rate and SNR of three transmission modes under 10−51e-5 is obtained, and the threshold switching interval of three transmission modes is obtained when the expected bit error rate of the system is. The simulation results show that the proposed method can dynamically switch transmission modes according to channel changes, and accurately realize the requirement of bit error rate of the system.

## Staircase Codes For MIMO-FSO System Over Gamma-Gamma Turbulence Channel With Spatially Correlated Fading

- **Status**: ❌
- **Reason**: Staircase codes(비-LDPC) + MIMO-FSO 응용. LDPC 아니고 떼어낼 BP 이식 기법 없음
- **ID**: ieee:10367224
- **Type**: conference
- **Published**: 13-16 Oct.
- **Authors**: Minghua Cao, Lili Li, Ruifang Yao +3
- **PDF**: https://ieeexplore.ieee.org/document/10367224
- **Abstract**: The implementation of multiple input multiple output (MIMO) technique in free-space optical (FSO) systems can improve reliability and data rate without requiring additional system bandwidth or transmit power. However, the presence of atmospheric turbulence and spatially correlated fading can significantly deteriorate the system performance. Staircase codes (SCCs) exhibit robust error correction capability and enable substantial coding gains in fading channels. Therefore, the combination of SCCs and MIMO techniques is employed in FSO communications to further resist turbulence fading and spatially correlated fading effects. Simulation results demonstrate that the use of SCCs effectively alleviate the fading effect, resulting in a net coding gain (NCG) exceeding 17 dB.

## QC-LDPC codes from various Golomb Rulers

- **Status**: ❌
- **Reason**: Golomb ruler 기반 QC-LDPC girth 분석이나 표준 곱셈표 구성+교과서 수준 사이클 카운팅, 신규 디코더/HW 없음 — 표준 기법 재사용
- **ID**: ieee:10392287
- **Type**: conference
- **Published**: 11-13 Oct.
- **Authors**: Daekyeong Kim, Hyojeong Choi, Hong-Yeop Song
- **PDF**: https://ieeexplore.ieee.org/document/10392287
- **Abstract**: In this paper, we analyze the girth of QC-LDPC codes constructed using a special type of Golomb rulers called Bh sequences and a well-known multiplication table method. We investigate the condition for the existence of 8-cycles and we are able to count the exact number of 8-cycles in the QC-LDPC codes using Bh sequences. The analysis focuses on the case h =3. By computer simulation, we show that the resulting codes for h =3 have a better performance than those from general Golomb rulers (non-B3 sequences) and have a comparable performance to the modified LDPC codes from basegraph2 in 5GNR spec. As h increases, the result could have higher girth but the performance improvement is only marginal.

## Application of Adaptive Polar Code based CV-QKD Scheme for LEO Satellite Systems

- **Status**: ❌
- **Reason**: Polar 코드 기반 CV-QKD 정보조정 리뷰 — 비-LDPC + QKD reconciliation, 떼어낼 LDPC 디코더/HW 없음
- **ID**: ieee:10392481
- **Type**: conference
- **Published**: 11-13 Oct.
- **Authors**: Qiang Wang, Thara Son, Meixiang Zhang +1
- **PDF**: https://ieeexplore.ieee.org/document/10392481
- **Abstract**: The information reconciliation protocol plays a crucial role in achieving a high secret key rate in continuous variable quantum key distribution (CV-QKD) systems. It is closely intertwined with a forward error correction scheme. In systems that operate under dynamic channel conditions, such as low earth orbit (LEO) satellite systems, the utilization of an adaptive reconciliation protocol becomes essential to ensure efficiency. This necessity calls for an efficient rate-adaptive forward error correction scheme, encompassing a single encoder and decoder. This paper provides a comprehensive review of adaptive information reconciliation schemes utilizing polar codes. It also explores their application to LEO satellite systems.

## Some New Binary Locally Repairable Codes with Availability based on Golomb Rulers

- **Status**: ❌
- **Reason**: Golomb ruler 기반 LRC(Locally Repairable Code), QC-LDPC 패리티생성 표준기법 차용뿐 — LRC 부호이지 LDPC ECC 신규 기여 아님
- **ID**: ieee:10392879
- **Type**: conference
- **Published**: 11-13 Oct.
- **Authors**: Hyojeong Choi, Hong-Yeop Song
- **PDF**: https://ieeexplore.ieee.org/document/10392879
- **Abstract**: In this paper, we propose some new binary 5-sequential recovery Locally Repairable Codes (5-seq LRCs) with availability 2 based on Golomb rulers and some well-known technique of generating the parity check matrix for the QC-LDPC codes. The proposed 5-seq LRCs can repair up to 5 erased symbols sequentially within 3 repair time. It can be viewed as an intersection of two LRCs without availability and its code rate is optimal for some cases.

## Recognition of Punctured Convolutional Codes Based on Multi-scale CNN

- **Status**: ❌
- **Reason**: Blind recognition of punctured convolutional codes via CNN — non-LDPC, code identification not ECC decoding, no transplantable LDPC technique
- **ID**: ieee:10333411
- **Type**: conference
- **Published**: 10-13 Oct.
- **Authors**: Jie Yang, Changyi Yan, Ying Ma +2
- **PDF**: https://ieeexplore.ieee.org/document/10333411
- **Abstract**: Punctured convolutional codes are widely applied in satellite communication systems and mobile communication systems. Blind recognition of channel coding plays a significant role in wireless communication technologies such as cognitive radio and radio spectrum detection. This work proposes a deep multi-scale convolution neural network (CNN) which is composed of a multi-scale feature extractor and dilated convolution layers for punctured convolutional codes recognition. The multi-scale feature extractor can better extract the features of different punctured matrices from codeword sequence with convolution kernels of different sizes. The dilated convolution layers expand the receptive field by using different dilation factors. In addition, mixture of experts is adopted to improve model stability and increase classification accuracy. Experimental results demonstrate that the proposed model performs consistently better than existing models on punctured convolutional codes. The proposed multi-scale CNN also shows better performance on common convolutional codes with code rate R = 1/2 and diverse constraint lengths.

## Code-aided Synchronization for DVB-RCS2

- **Status**: ❌
- **Reason**: Code-aided synchronization for turbo codes (DVB-RCS2) — non-LDPC, synchronization not ECC decoding, no transplantable binary LDPC BP technique
- **ID**: ieee:10333734
- **Type**: conference
- **Published**: 10-13 Oct.
- **Authors**: Qingsheng Xue, Jie Wang, Ming Chen +2
- **PDF**: https://ieeexplore.ieee.org/document/10333734
- **Abstract**: The second generation digital television broadcasting interactive satellite system (DVB-RCS2) plays a very important role in the satellite communication return channel. In actual application, interference from timing deviation and carrier frequency deviation will be encountered, especially turbo codes are very sensitive to carrier frequency deviation, so the design of efficient receiver for DVB-RCS2 must consider the synchronization problem. In this paper, we integrate the synchronization scheme into the decoding process of turbo codes. We use the log-likelihood ratio provided by the decoder for iterative synchronization, and use the result of cyclic redundancy check (CRC) as a stop signal for iterative detection, we call this approach code-aided (CA) synchronization. Simulation experiments show that the CA synchronization scheme is significantly better than the traditional data-assisted synchronization scheme, even comparable to the performance in ideal synchronous scenarios. In addition, combined with the CRC check, redundant iterations are avoided.

## Phase Noise Estimation and Compensation Using FDM Pilot for High-Order QAM Transmission in DFT-Spread OFDM Backhaul Links

- **Status**: ❌
- **Reason**: Phase noise compensation for QAM/OFDM backhaul — no LDPC ECC technique, pure wireless RX signal processing
- **ID**: ieee:10333487
- **Type**: conference
- **Published**: 10-13 Oct.
- **Authors**: Ryota Kuribayashi, Mamoru Sawahashi
- **PDF**: https://ieeexplore.ieee.org/document/10333487
- **Abstract**: This paper proposes a phase noise compensation (PNC) method using frequency division multiplexing (FDM) pilot multiplexing with high-order QAM in discrete Fourier transform-Spread orthogonal frequency-division multiplexing (DFT-S-OFDM) back-haul links. The proposed PNC method comprises pilot symbol assisted (PSA) PNC and iterative PNC using an extended Kalman filter (EKF) associated with the cancellation of distortion due to puncturing of the single carrier (SC) and pilot interference. Computer simulation results show that the peak-to-average power ratio (PAPR) at the complementary cumulative distribution of 10−4 of the DFT-S-OFDM with FDM pilot multiplexing is decreased by approximately 2.7 dB compared to that for OFDM for 256QAM. We show that the proposed iterative PNC receiver achieves the bit-error rate (BER) of 10−8 at a received signal-to-noise power ratio (SNR) of approximately 26.0 dB with 256QAM for DFT-S-OFDM. The loss in the required received SNR satisfying the BER of 10−8 of the proposed iterative PNC receiver for DFT-S-OFDM compared to OFDM when both employ FDM pilot multiplexing is suppressed to approximately 1.0 dB for 256QAM. We conclude that the proposed iterative PNC with FDM based pilot multiplexing is effective in achieving a very low BER such as 10−8 in DFT-S-OFDM backhaul links.

## An integrated coherent driver modulator enabled 1.6-Tb/s coherent transmission

- **Status**: ❌
- **Reason**: 1.6Tb/s 코히어런트 광전송/변조기 데모, LDPC ECC 무관.
- **ID**: ieee:10484773
- **Type**: conference
- **Published**: 1-5 Oct. 2
- **Authors**: D. Che, X. Chen, B. Krueger +1
- **PDF**: https://ieeexplore.ieee.org/document/10484773
- **Abstract**: We demonstrate a 1.6-Tb/s coherent transmission based on a fully packaged 80-GHz-class coherent driver modulation (CDM) compatible with OIF HB-CDM implementation agreement, indicating a practical single-channel 1.6-Tb/s solution is around the corner.

## C+L-band 2,160 km bidirectional transmission using three vendor-installed 4-core fibre cables

- **Status**: ❌
- **Reason**: 멀티코어 광섬유 전송 실험, ECC 기여 없음
- **ID**: ieee:10484571
- **Type**: conference
- **Published**: 1-5 Oct. 2
- **Authors**: D. Soma, S. Beppu, Y. Wakayama +2
- **PDF**: https://ieeexplore.ieee.org/document/10484571
- **Abstract**: Full C+L-band transmission is experimentally demonstrated using multivendor 4-core fibre cables installed in an outdoor environment. By applying bidirectional transmission technology to suppress core-to-core XT, the transmission distance can be extended to 2,160 km, which is 1.5 times longer than that for unidirectional transmission.

## Single-wavelength 1.2-Tb/s IM-DD transmission by polarization-multiplexing three 160-GBd PAM-8 signals

- **Status**: ❌
- **Reason**: IM-DD 편광 다중화 PAM-8 전송 데모, 부호화 기법 없음.
- **ID**: ieee:10484898
- **Type**: conference
- **Published**: 1-5 Oct. 2
- **Authors**: D. Che, X. Chen
- **PDF**: https://ieeexplore.ieee.org/document/10484898
- **Abstract**: IM-DD is facing a speed bottleneck per lane due to its intensity-only signaling. We break such a bottleneck by combining three IM signals with a novel polarization multiplexing technique and achieve the first IM-DD based single-wavelength transmission beyond 1 Tb/s.

## Application of SD-FEC to optical eigenvalue-modulated signals using a neural network-based demodulator

- **Status**: ❌
- **Reason**: 고유값 변조 신호용 NN 복조기+SD-FEC 응용, LDPC ECC 신규 기법 없음
- **ID**: ieee:10484724
- **Type**: conference
- **Published**: 1-5 Oct. 2
- **Authors**: K. Mishina, T. Yoshida, D. Hisano +1
- **PDF**: https://ieeexplore.ieee.org/document/10484724
- **Abstract**: We propose the application of an SD-FEC technique to an eigenvalue-modulated signal using a multilabel neural-network demodulator. The experimental results indicate a successful operation with an error-free transmission through a 3000-km optical fiber line.

## Low-complexity architecture for soft-output trellis-based detection in high-speed data center applications

- **Status**: ❌
- **Reason**: 트렐리스 기반 soft-output 검출 아키텍처(DFE), 비-LDPC 등화기로 LDPC BP 이식 기법 없음
- **ID**: ieee:10484655
- **Type**: conference
- **Published**: 1-5 Oct. 2
- **Authors**: K. Wu, G. Liga, J. Riani +1
- **PDF**: https://ieeexplore.ieee.org/document/10484655
- **Abstract**: An architecture enabled by DFE is proposed to achieve reduced-state trellis-based algorithms for data center applications. Performance evaluation using PAM-4 IM/DD experimental data shows that the penalty due to state pruning is below 0.5 dB, while a complexity reduction up to 57% is achieved.

## 140-Gbaud PAM-8 IM/DD transmission and FTN signal processing based on low-complexity nonlinear M-BCJR equalization with deep neural-network channel model

- **Status**: ❌
- **Reason**: PAM-8 IM/DD FTN M-BCJR 등화, 비-LDPC 신호처리로 NAND LDPC 이식 기법 없음
- **ID**: ieee:10484767
- **Type**: conference
- **Published**: 1-5 Oct. 2
- **Authors**: A. Yan, S. Xing, G. Li +9
- **PDF**: https://ieeexplore.ieee.org/document/10484767
- **Abstract**: We propose and experimentally demonstrate an FTN signal processing scheme based on low-complexity nonlinear M-BCJR equalization with DNN model for nonlinear channel fitting in IM/DD system, achieving 140-GBaud PAM-8 signal transmission over 0.5-km SSMF in the C-band and a net-data-rate of 340 Gbps/λ.

## C + L-band seeded comb regeneration for MCF networks

- **Status**: ❌
- **Reason**: 광주파수 콤 재생/MCF 네트워크 아키텍처, ECC 기법 없음.
- **ID**: ieee:10484808
- **Type**: conference
- **Published**: 1-5 Oct. 2
- **Authors**: B. J. Puttnam, R. S. Luis, G. Rademacher +6
- **PDF**: https://ieeexplore.ieee.org/document/10484808
- **Abstract**: We demonstrate C+L-band optical-frequency-comb regeneration from seed-signals that can be split, amplified, and transmitted over a novel metro/DC network architecture. Multi-core-fiber seed and data distribution with spatial-switching enables identical network-wide transceiver combs and ≈100 Tb/s/core and 600 Tb/s per-fiber data-rates.

## 22.9 Pb/s data-rate by extreme space-wavelength multiplexing

- **Status**: ❌
- **Reason**: 광 SDM 전송 데이터레이트 기록, LDPC는 베이스라인 언급뿐 떼어낼 기법 없음
- **ID**: ieee:10484688
- **Type**: conference
- **Published**: 1-5 Oct. 2
- **Authors**: B. J. Puttnam, M. van den Hout, G. Di Sciullo +6
- **PDF**: https://ieeexplore.ieee.org/document/10484688
- **Abstract**: We transmit 750 wavelength channels covering 19 THz bandwidth over a few-mode multi-core fiber with 114 spatial channels, recording a total GMI-estimated data-rate of 24.7 petabit/second and 22.9 Pb/s after LDPC decoding, both exceeding 200 Tb/s per spatial channel
