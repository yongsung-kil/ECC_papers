# IEEE Xplore — 2015-09


## Spatially Coupled LDPC Codes Constructed From Protographs

- **Status**: ✅
- **Reason**: 프로토그래프 기반 SC-LDPC 구성 기법(E), 바이너리, BP 임계값/최소거리 설계 — NAND LDPC 코드설계 이식 가능
- **ID**: ieee:7152893
- **Type**: journal
- **Published**: Sept. 2015
- **Authors**: David G. M. Mitchell, Michael Lentmaier, Daniel J. Costello
- **PDF**: https://ieeexplore.ieee.org/document/7152893
- **Abstract**: In this paper, we construct protograph-based spatially coupled low-density parity-check (LDPC) codes by coupling together a series of L disjoint, or uncoupled, LDPC code Tanner graphs into a single coupled chain. By varying L , we obtain a flexible family of code ensembles with varying rates and frame lengths that can share the same encoding and decoding architecture for arbitrary L . We demonstrate that the resulting codes combine the best features of optimized irregular and regular codes in one design: capacity approaching iterative belief propagation (BP) decoding thresholds and linear growth of minimum distance with block length. In particular, we show that, for sufficiently large L , the BP thresholds on both the binary erasure channel and the binary-input additive white Gaussian noise channel saturate to a particular value significantly better than the BP decoding threshold and numerically indistinguishable from the optimal maximum a posteriori decoding threshold of the uncoupled LDPC code. When all variable nodes in the coupled chain have degree greater than two, asymptotically the error probability converges at least doubly exponentially with decoding iterations and we obtain sequences of asymptotically good LDPC codes with fast convergence rates and BP thresholds close to the Shannon limit. Further, the gap to capacity decreases as the density of the graph increases, opening up a new way to construct capacity achieving codes on memoryless binary-input symmetric-output channels with low-complexity BP decoding.

## Efficient Puncturing Scheme for Irregular LDPC Codes Based on Serial Schedules

- **Status**: ✅
- **Reason**: 불규칙 LDPC 직렬스케줄 기반 신규 puncturing 기법; 바이너리 LDPC 코드설계(E) 이식 가능
- **ID**: ieee:7152871
- **Type**: journal
- **Published**: Sept. 2015
- **Authors**: Hua Li, Linhua Zheng
- **PDF**: https://ieeexplore.ieee.org/document/7152871
- **Abstract**: In practice, low-density parity-check (LDPC) codes are usually decoded by serial schedules. However, the existing schemes for rate-compatible puncturing LDPC codes are proposed on the assumption that the flooding schedules are employed in decoding algorithm. In this letter, an efficient puncturing scheme is proposed for irregular LDPC codes based on serial schedule. The scheme selects variable nodes to be punctured one at a time. At each time, a check node is selected firstly based on the idea that the punctured variable nodes are allocated evenly to all the check nodes. Then the puncturing variable node is selected among its neighbors. Furthermore, the order of the check nodes in the selection serves as the updating order in the serial schedule, which ensures that all the punctured codes can be recovered at the first iteration. Simulation results demonstrate that the scheme performs better for a wide range of code rates compared with the existing puncturing scheme, especially for high-rate punctured codes.

## Spatially Coupled LDPC Codes Constructed by Parallelly Connecting Multiple Chains

- **Status**: ✅
- **Reason**: 바이너리 SC-LDPC 다중체인 병렬연결 신규 구성으로 디코딩 임계값 개선; 코드설계(E) 이식 가능
- **ID**: ieee:7130575
- **Type**: journal
- **Published**: Sept. 2015
- **Authors**: Yang Liu, Ying Li, Yuhao Chi
- **PDF**: https://ieeexplore.ieee.org/document/7130575
- **Abstract**: A particular class of spatially coupled low-density parity-check (SC-LDPC) codes are constructed by parallelly connecting multiple different coupled chains. The connection structure is realized by edge exchanges between adjacent chains, which can help these chains support each other and improve the iterative decoding thresholds. By varying the number of the connected chains and the degree of each chain, a family of SC-LDPC codes with wide rate range can be obtained. Density evolution analysis shows that the decoding thresholds of the proposed codes are very close to Shannon limits and are slightly better than that constructed by a single chain over the binary erasure channel.

## Simplified Trellis Min–Max Decoder Architecture for Nonbinary Low-Density Parity-Check Codes

- **Status**: ❌
- **Reason**: Non-binary LDPC (GF(32)) trellis min-max decoder; 비이진 LDPC는 기준상 제외
- **ID**: ieee:6881677
- **Type**: journal
- **Published**: Sept. 2015
- **Authors**: Jesús O. Lacruz, Francisco García-Herrero, David Declercq +1
- **PDF**: https://ieeexplore.ieee.org/document/6881677
- **Abstract**: Nonbinary low-density parity-check (NB-LDPC) codes have become an efficient alternative to their binary counterparts in different scenarios, such as moderate codeword lengths, high-order modulations, and burst error correction. Unfortunately, the complexity of NB-LDPC decoders is still too high for practical applications, especially for the check node (CN) processing, which limits the maximum achievable throughput. Although a great effort has been made in the recent literature to overcome this disadvantage, the proposed decoders are still not ready for high-speed implementations for high-order fields. In this paper, a simplified trellis min-max algorithm is proposed, where the CN messages are computed in a parallel way using only the most reliable information. The proposed CN algorithm is implemented using a horizontal layered schedule. The overall decoder architecture has been implemented in a 90-nm CMOS process for a (N = 837 and K = 726) NB-LDPC code over GF(32), achieving a throughput of 660 Mb/s at nine iterations based on postlayout results. This decoder increases hardware efficiency compared with the existing recent solutions for the same code.

## An Optimization Scheme of Adaptive Dynamic Energy Consumption Based on Joint Network-Channel Coding in Wireless Sensor Networks

- **Status**: ❌
- **Reason**: WSN 결합 네트워크-채널코딩 에너지 최적화; LDPC 부수, 떼어낼 ECC 기법 없음
- **ID**: ieee:7101805
- **Type**: journal
- **Published**: Sept. 2015
- **Authors**: Xingcheng Liu, Nandi Xiong, Wei Li +1
- **PDF**: https://ieeexplore.ieee.org/document/7101805
- **Abstract**: Energy efficiency is one of the most important factors in wireless sensor networks (WSNs). Recent research results have demonstrated that the previously suggested scheme of the joint network-channel coding (JNCC) can greatly improve the efficiency and the communications reliability of WSNs. In this paper, the effect of the number of network coding packets on the energy consumption with the JNCC model was analyzed. An adaptive dynamic energy consumption (ADEC) optimization scheme was proposed. With this scheme, the number of the packets with network coding can be dynamically adjusted based on the feedback of the bit-error rate (BER) to minimize the total energy consumption. In this scheme, the BER threshold can be estimated. Simulation results show that the proposed ADEC optimization scheme achieves an excellent energy efficiency, especially in the low SNR region.

## New Nonasymptotic Channel Coding Theorems for Structured Codes

- **Status**: ❌
- **Reason**: 비점근 채널코딩 정리(랜덤코딩 bound); 순수 이론, 디코더/HW/구성으로 안 이어짐
- **ID**: ieee:7134794
- **Type**: journal
- **Published**: Sept. 2015
- **Authors**: En-Hui Yang, Jin Meng
- **PDF**: https://ieeexplore.ieee.org/document/7134794
- **Abstract**: New nonasymptotic random coding theorems (with error probability E and finite block length n) based on Gallager parity check ensemble and general parity check ensembles are derived in this paper. The resulting nonasymptotic achievability bounds, when combined with nonasymptotic equipartition properties developed in this paper, can be easily computed. Analytically, these nonasymptotic achievability bounds are shown to be asymptotically tight up to the second order of the coding rate as n goes to infinity with either constant or subexponentially decreasing E in the case of Gallager parity check ensemble, and to imply that low density parity check (LDPC) codes be capacity-achieving in the case of LDPC ensembles. Numerically, they are also compared favorably, for finite n and E of practical interest, with existing nonasymptotic achievability bounds in the literature.

## LP Decoding Excess Over Symmetric Channels

- **Status**: ❌
- **Reason**: 바이너리 선형부호 LP 디코딩의 순수 이론 bound(LP excess lemma) — 디코더/HW/구성으로 이어지지 않음
- **ID**: ieee:7159028
- **Type**: journal
- **Published**: Sept. 2015
- **Authors**: Louay Bazzi, Ibrahim Abou-Faycal
- **PDF**: https://ieeexplore.ieee.org/document/7159028
- **Abstract**: We consider the problem of Linear Programming (LP) decoding of binary linear codes. The LP excess lemma was introduced by the first author, B. Ghazi, and R. Urbanke (IEEE Trans. Inf. Th., 2014) as a technique to trade crossover probability for “LP excess” over the Binary Symmetric Channel. We generalize the LP excess lemma to discrete, binary-input, Memoryless, Symmetric and LLR-Bounded (MSB) channels. As an application, we extend a result by the first author and H. Audah (IEEE Trans. Inf. Th., 2015) on the impact of redundant checks on LP decoding to discrete MSB channels.

## Matching Criterion Between Source Statistics and Source Coding Rate

- **Status**: ❌
- **Reason**: JSCC용 DP-LDPC의 PEXIT 소스율 매칭 기준 — 소스-채널 결합, 떼어낼 ECC 디코더/HW 기법 없음
- **ID**: ieee:7153518
- **Type**: journal
- **Published**: Sept. 2015
- **Authors**: Chen Chen, Lin Wang, Zixiang Xiong
- **PDF**: https://ieeexplore.ieee.org/document/7153518
- **Abstract**: Joint source-channel coding (JSCC) based on double protograph low-density parity-check (DP-LDPC) codes has been shown to be a good solution for wireless communications. However, the premature error floor region of the DP-LDPC codes usually does not meet the bit-error-rate requirements. In this letter, we provide a matching criterion between the source statistics and the source coding rate using a novel protograph extrinsic information transfer (PEXIT) algorithm with a new decoding threshold. The resulting matching criterion helps predict the error floor region performance and give directions for source coding rate designs.

## A Construction of Physical-Layer Systematic Raptor Codes Based on Protographs

- **Status**: ❌
- **Reason**: 물리계층 Raptor(fountain) 부호 구성; fountain 부호는 원칙 제외, 떼어낼 LDPC ECC 기법 없음
- **ID**: ieee:7131466
- **Type**: journal
- **Published**: Sept. 2015
- **Authors**: Shiuan-Hao Kuo, Huang-Chang Lee, Yeong-Luh Ueng +1
- **PDF**: https://ieeexplore.ieee.org/document/7131466
- **Abstract**: A construction of physical-layer Raptor (PLR) codes based on protographs is proposed. We first set up a sequence of signal-to-noise ratios (SNRs). For each SNR, we employ a modified protograph EXIT analysis to find the extra check nodes in addition to the existing check nodes so as to meet the threshold required by the outer low-density parity check code. PLR codes which are capacity-approaching for a wide SNR range can be obtained using the proposed construction.

## Analysis of low-bit soft-decision error correction in optical front ends

- **Status**: ✅
- **Reason**: 광 수신단 저비트 soft-decision FEC 디코딩 성능/노이즈 분석, LLR 양자화·thermometer code 관련 — 저비트 양자화 디코더 이식 가능성, 애매하여 보존(C)
- **ID**: ieee:7255255
- **Type**: journal
- **Published**: Sept. 2015
- **Authors**: M. Moayedi Pour Fard, G. Cowan, O. Liboiron-Ladouceur
- **PDF**: https://ieeexplore.ieee.org/document/7255255
- **Abstract**: A novel methodology for analyzing the advantageous decoding performance of multibranch configurations of low-bit optical soft-decision forward error correction receivers is presented. The decoding performance and noise behavior of three front-end schemes are evaluated and compared. Arising from a multiple-branch configuration, the concept of inconsistency in the decoder (thermometer code) is presented and used to optimize decoding performance. The experimentally validated methodology considers both optically amplified long-haul and short-reach applications.

## Shortened Polar Codes

- **Status**: ❌
- **Reason**: 폴라 부호 shortening 최적화로 부호 비의존적 BP 이식 기법 없음, LDPC는 비교 대상일 뿐 — 비-LDPC 제외
- **ID**: ieee:7152894
- **Type**: journal
- **Published**: Sept. 2015
- **Authors**: Vera Miloslavskaya
- **PDF**: https://ieeexplore.ieee.org/document/7152894
- **Abstract**: An optimization algorithm for finding a shortening pattern and a set of frozen symbols for polar codes is proposed. The structure of polar codes is exploited to eliminate many equivalent shortening patterns, thus reducing the search space. A reduced-complexity suboptimal algorithm is proposed for finding shortening patterns for long polar codes. Shortened codes obtained with the proposed method are shown to outperform low-density parity-check (LDPC) codes.

## DNA-Based Storage: Trends and Methods

- **Status**: ❌
- **Reason**: DNA 저장용 constrained coding(이산 알파벳 시퀀스 설계). 채널 LDPC ECC 디코더/HW/바이너리 코드설계 기법 없음
- **ID**: ieee:7423733
- **Type**: journal
- **Published**: Sept. 2015
- **Authors**: S. M. Hossein Tabatabaei Yazdi, Han Mao Kiah, Eva Garcia-Ruiz +3
- **PDF**: https://ieeexplore.ieee.org/document/7423733
- **Abstract**: We provide an overview of current approaches to DNA-based storage system design and of accompanying synthesis, sequencing and editing methods. We also introduce and analyze a suite of new constrained coding schemes for both archival and random access DNA storage channels. The analytic contribution of our work is the construction and design of sequences over discrete alphabets that avoid pre-specified address patterns, have balanced base content, and exhibit other relevant substring constraints. These schemes adapt the stored signals to the DNA medium and thereby reduce the inherent error-rate of the system.

## A Study on Impulse Noise and Its Models

- **Status**: ❌
- **Reason**: 임펄스 노이즈 모델 서베이/튜토리얼. ECC는 부수 언급, 떼어낼 LDPC 디코더/HW 기법 없음
- **ID**: ieee:8531938
- **Type**: journal
- **Published**: Sept. 2015
- **Authors**: Thokozani Shongwe, A. J. Han Vinck, Hendrik C. Ferreira
- **PDF**: https://ieeexplore.ieee.org/document/8531938
- **Abstract**: This article gives an overview of impulse noise and its models, and points out some important and interesting facts about the study of impulse noise which are sometimes overlooked or not well understood. We discuss the different impulse noise models in the literature, focusing on their similarities and differences when applied in communications systems. The impulse noise models discussed are memoryless (Middleton Class A, Bernoulli-Gaussian and Symmetric alpha-stable), and with memory (Markov-Middleton and Markov-Gaussian). We then go further to give performance comparisons in terms of bit error rates for some of the variants of impulse noise models. We also compare the bit error rate performance of single-carrier (SC) and multi-carrier (MC) communications systems operating under impulse noise. It can be seen that MC is not always better than SC under impulse noise. Lastly, the known impulse noise mitigation schemes (clipping/nulling using thresholds, iterative based and error control coding methods) are discussed.

## Achieving the Near-Capacity of Two-Way Relay Channels With Modulation-Coded Physical-Layer Network Coding

- **Status**: ❌
- **Reason**: GF(q) IRA MC-PNC 양방향 중계; 비이진+무선 PNC 특이적, 이식 가능 바이너리 LDPC 기법 없음
- **ID**: ieee:7109943
- **Type**: journal
- **Published**: Sept. 2015
- **Authors**: Lei Yang, Tao Yang, Jinhong Yuan +1
- **PDF**: https://ieeexplore.ieee.org/document/7109943
- **Abstract**: We propose and design a practical modulation-coded (MC) physical-layer network coding (PNC) scheme to approach the capacity limits of Gaussian and fading two-way relay channels (TWRCs). In the proposed scheme, an irregular repeat-accumulate (IRA) MC over GF(q) with the same random coset is employed at two users, which directly maps the message sequences into coded PAM or QAM symbol sequences. The relay chooses appropriate network coding coefficients and computes the associated finite-field linear combinations of the two users' message sequences using an iterative belief propagation algorithm. For a symmetric Gaussian TWRC, we show that, by introducing the same random coset vector at the two users and a time-varying accumulator in the IRA code, the MC-PNC scheme exhibits symmetry and permutation-invariant properties for the soft information distribution of the network-coded message sequence (NCMS). We explore these properties in analyzing the convergence behavior of the scheme and optimizing the MC to approach the capacity limit of a TWRC. For a block fading TWRC, we present a new MC linear PNC scheme and an algorithm used at the relay for computing the NCMS. We demonstrate that our developed schemes achieve near-capacity performance in both Gaussian and Rayleigh fading TWRCs. For example, our designed codes over GF(7) and GF(3) with a code rate of 3/4 are within 1 and 1.2 dB of the TWRC capacity, respectively. Our method can be regarded as a practical embodiment of the notion of compute-and-forward with a good nested lattice code, and it can be applied to a wide range of network configurations.

## A MIMO-Channel-Precoding Scheme for Next Generation Terrestrial Broadcast TV Systems

- **Status**: ❌
- **Reason**: MIMO 지상파 방송 프리코더, LDPC 언급 없음 — 무선 응용 특이적, 떼어낼 기법 없음
- **ID**: ieee:7161328
- **Type**: journal
- **Published**: Sept. 2015
- **Authors**: David Vargas, Yong Jin Daniel Kim, Jan Bajcsy +2
- **PDF**: https://ieeexplore.ieee.org/document/7161328
- **Abstract**: To cope with increasing demands for spectral efficiency, multiple-input multiple-output (MIMO) technology is being considered for next generation terrestrial broadcasting television systems. In this paper, we propose a MIMO channel-precoder that utilizes channel statistical structure and is suitable for terrestrial broadcasting systems, while being potentially transparent to the receivers. The performance of the channel-precoder is evaluated in a wide set of channel scenarios and mismatched channel conditions, a typical situation in the broadcast setup. Capacity results show performance improvements in the case of strong line-of-sight scenarios with correlated antenna components and resilience against mismatched condition. Finally, we present bit-error-rate simulation results for state-of-the-art digital terrestrial broadcast systems based on digital video broadcasting-next generation handheld to compare the performance of single-input single-output, 2 × 2 and 4 × 2 MIMO systems and proposed MIMO channel-precoder.

## Hybrid Minimum Pearson and Euclidean Distance Detection

- **Status**: ❌
- **Reason**: 플래시/광 저장 신호 검출(Pearson/Euclidean distance) — 신호검출 기법, LDPC 디코더/구성 기여 없음
- **ID**: ieee:7163311
- **Type**: journal
- **Published**: Sept. 2015
- **Authors**: Kees A. Schouhamer Immink, Jos H. Weber
- **PDF**: https://ieeexplore.ieee.org/document/7163311
- **Abstract**: The reliability of mass storage systems, such as optical data recording and non-volatile memory (Flash), is seriously hampered by uncertainty of the actual value of the offset (drift) or gain (amplitude) of the retrieved signal. The recently introduced minimum Pearson distance detection is immune to unknown offset or gain, but this virtue comes at the cost of a lessened noise margin at nominal channel conditions. We will present a novel hybrid detection method, where we combine the outputs of the minimum Euclidean distance and Pearson distance detectors so that we may trade detection robustness versus noise margin. We will compute the error performance of hybrid detection in the presence of unknown channel mismatch and additive noise.

## Distributed Lossless Coding Techniques for Hyperspectral Images

- **Status**: ❌
- **Reason**: 분산 무손실 소스코딩(초분광 압축); 채널코딩 ECC 아님
- **ID**: ieee:7038166
- **Type**: journal
- **Published**: Sept. 2015
- **Authors**: Jinlei Zhang, Houqiang Li, Chang Wen Chen
- **PDF**: https://ieeexplore.ieee.org/document/7038166
- **Abstract**: In this paper, we present a novel distributed coding scheme for lossless, progressive and low complexity compression of hyperspectral images. Hyperspectral images have several unique requirements that are vastly different from consumer images. Among them, lossless compression, progressive transmission, and low complexity onboard processing are three most prominent ones. To satisfy these requirements, we design a distributed coding scheme that shifts the complexity of data decorrelation to the decoder side to achieve lightweight onboard processing after image acquisition. At the encoder, the images are subsampled in order to facilitate successive encoding and progressive transmission. At the decoder, we generate the side information with adaptive region-based predictor by taking full advantage of the decoded subsampled images and previously decoded neighboring bands based on the assumptions that the objects appearing in different bands are highly correlated. The proposed progressive transmission via subsampling enables the spectral correlation to be refined successively, resulting in gradually improved decoding performance of higher-resolution layers as more sub-images are decoded. Experimental results on the Airborne Visible/Infrared Imaging Spectrometer (AVIRIS) data demonstrate that the proposed scheme is able to achieve competitive compression performance comparing with the-state-of-the-art 3D schemes, including existing distributed source coding (DSC) schemes. The proposed scheme has even lower encoding complexity than that of the conventional 2D schemes.

## A Near-Capacity MIMO Coded Modulation Scheme for Digital Terrestrial Television Broadcasting

- **Status**: ❌
- **Reason**: MIMO DTTB BICM, APSK 성좌+비트인터리버 — LDPC는 UEP 부수 언급, 떼어낼 ECC 기법 없음
- **ID**: ieee:7165610
- **Type**: journal
- **Published**: Sept. 2015
- **Authors**: Tao Cheng, Kewu Peng, Fang Yang +2
- **PDF**: https://ieeexplore.ieee.org/document/7165610
- **Abstract**: Multiple-input multiple-output (MIMO), which can provide ultrahigh data transmission rate, is one of the key technologies for the next generation digital terrestrial television broadcasting (DTTB) standards. This paper proposes a near-capacity MIMO bit-interleaved coded modulation scheme with either independent or iterative demapping (BICM/BICM-ID) for the DTTB system. First, the amplitude phase shift keying (APSK) constellation with Gray mapping is proposed to replace the conventional Gray quadrature amplitude modulation (QAM) counterpart. From the perspective of average mutual information analysis, Gray-APSK has certain shaping gain compared to Gray-QAM for both independent and iterative demapping schemes. Besides the APSK constellation, a novel bit interleaver named bit mapping, which takes into account the unequal error protection of both APSK constellations and low-density parity-check codes, is proposed to further improve the system performance. The tool of extrinsic information transfer chart is utilized to analyze and design the optimal bit mapping for the BICM/BICM-ID scheme. Bit error rate simulations are finally carried out to verify the superiority of the proposed MIMO coded modulation scheme.

## A reduced-complexity demapping algorithm for BICM-ID systems

- **Status**: ❌
- **Reason**: BICM-ID demapping 복잡도 감소; LDPC 비의존 demapper, 부호화 ECC 기법 없음
- **ID**: ieee:6942236
- **Type**: journal
- **Published**: Sept. 2015
- **Authors**: Jiandong Tan, Qi Wang, Chen Qian +3
- **PDF**: https://ieeexplore.ieee.org/document/6942236
- **Abstract**: As a highly efficient decoding and demodulation scheme, bit-interleaved coded modulation (BICM) is widely adopted in modern communication systems. In order to enhance the attainable spectral efficiency, usually, high-order modulation schemes are used for BICM systems. When BICM is combined with iterative decoding (BICM-ID), it is capable of further improving the achievable receiver performance. However, the complexity of the standard max-sum approximation of the maximum aposteriori probability in log-domain (Max-Log-MAP) invoked by the iterative demapper is on the order of 2m or O(2m) for a 2m-ary modulation constellation having m bits per symbol, which may become excessive for high-order BICM-ID systems. The existing simplified algorithms employed for noniterative demappers are based on exploiting the constellation's symmetry, which is no longer retained upon the introduction of the a priori information in BICM-ID systems. Hence, in this paper, a simplified iterative demapping algorithm is proposed to substantially reduce the demapping complexity for a binary-reflected Gray-labeled constellation. Our detailed analysis shows that the simplified demapping scheme proposed for BICM-ID reduces the computational complexity to O(m). We demonstrate that this dramatic computational complexity only imposes modest performance degradation with respect to that of the optimal high-complexity Max-Log-MAP scheme.

## Cellular-Based Real-Time Flow Repair for Broadcast Flows

- **Status**: ❌
- **Reason**: 셀룰러/방송 실시간 플로우 복구 서비스 — 네트워크 프로토콜, LDPC ECC 무관
- **ID**: ieee:7165618
- **Type**: journal
- **Published**: Sept. 2015
- **Authors**: Muhammad Moiz Anis, Xavier Lagrange, Ramesh Pyndiah
- **PDF**: https://ieeexplore.ieee.org/document/7165618
- **Abstract**: Watching television on a portable device is possible on broadcast and cellular systems. With broadcast technologies, due to the absence of a feedback channel it is not possible to guarantee an error free reception at the receivers. With cellular technologies, the transmission is based on unicast and the same content is transmitted as many times as the number of people who are watching the same program in the cell. We propose to combine both technologies and consider the concept of repairing a broadcast data flow for dual-mode (cellular and broadcast) smartphones in real time in order to ensure a better quality of service. We propose to use the constrained application protocol (CoAP) and specify a real-time flow repair (RFR) service based on CoAP in the cellular networks. We describe the architecture to provide such a service. We analyze the load generated in the cellular radio access network due to the retransmission of the packets lost on the broadcast system and also develop a model for the evaluation of the residual errors in the RFR operations.

## Coded MIMO With Asymmetric Constellation Sizes

- **Status**: ❌
- **Reason**: Coded MIMO 비대칭 성상도+sphere decoding; 무선 변조 특이적, 떼어낼 LDPC 디코더 기법 없음
- **ID**: ieee:6917058
- **Type**: journal
- **Published**: Sept. 2015
- **Authors**: Chen Qian, Zhaocheng Wang, Zhaohua Lu +2
- **PDF**: https://ieeexplore.ieee.org/document/6917058
- **Abstract**: An asymmetric constellation scheme for coded multiple-input-multiple-output (MIMO) transmission is proposed, which applies different constellation mappings to different transmit streams and carefully selects the coding rates for different transmit streams. An improved power allocation is derived to naturally incorporate with the coding rate selection and to further enhance the achievable performance. The proposed scheme provides more flexible choices of data rate selection, and by employing fixed-complexity sphere decoding (FSD) detection, it achieves better performance with reduced detection complexity in comparison with the conventional MIMO using the FSD-based detection with the same constellation set for all streams.

## Overview of Wireless Microphones—Part I: System and Technologies

- **Status**: ❌
- **Reason**: 무선 마이크 시스템 개요 — ECC/LDPC 무관
- **ID**: ieee:7185356
- **Type**: journal
- **Published**: Sept. 2015
- **Authors**: Hong Liu, Donald McLachlan, Demin Wang
- **PDF**: https://ieeexplore.ieee.org/document/7185356
- **Abstract**: Wireless microphones are indispensable to modern society. They are used worldwide by professionals and amateurs for such applications as live performances, electronic news gathering, and conference presentations. Due to the radio spectrum crunch, wireless microphones have become a hot topic of discussion and debate among television broadcasters, wireless microphone manufacturers, wireless network operators, and spectrum regulators. In order to keep wireless microphones operating well, it is necessary to give engineers, researchers, and regulators a comprehensive overview of wireless microphones in the aspects of technologies, spectrum requirements, and interference that may be experienced or generated by wireless microphones. This overview is divided into two parts. Part I provides an overview of typical wireless microphone system components, their performance requirements and technical parameters, and the technologies that are used in current wireless microphones. Part II focuses on the spectrum, sources of interference, and regulations surrounding wireless microphones.

## Performance of IEEE 802.11n LDPC codes with modified reliability based hybrid ARQ and Unequal Error Protection

- **Status**: ❌
- **Reason**: 802.11n LDPC에 RB-HARQ+UEP 결합 — 무선 응용 특이적, NAND에 떼어낼 디코더/HW/코드설계 기법 없음
- **ID**: ieee:7313674
- **Type**: conference
- **Published**: 8-11 Sept.
- **Authors**: T.P. Fowdur, B.N. Furzun
- **PDF**: https://ieeexplore.ieee.org/document/7313674
- **Abstract**: Wireless communication standards such as the IEEE 802.11n Wi-Fi standard employ powerful error correcting codes such as Low Density Parity Check (LDPC) codes and Hybrid Automatic Repeat reQuest (HARQ) to achieve reliable transmission. Reliability-Based HARQ (RB-HARQ) schemes have proved to be an efficient alternative approach to incremental redundancy ARQ. This paper proposes a modified RB-HARQ scheme for IEEE 802.11n LDPC codes and combines it with an Unequal Error Protection (UEP) scheme which performs prioritized constellation mapping to exploit the inherent UEP property of the Quadrature Amplitude Modulation (QAM) constellation. With 16-QAM and a code-rate of ½, the proposed scheme provides a gain of 1.5 dB in Eb/No (ratio of energy per bit to noise power spectral density) and 2% in throughout at a Bit Error Rate (BER) close to 10-1 over a scheme which uses conventional RB-HARQ without UEP. Moreover, with 64-QAM a maximum gain of 4.5 dB in Eb/No is obtained.

## Modulation design analysis for two-way relay channels

- **Status**: ❌
- **Reason**: 양방향 중계 채널 변조설계, LDPC는 베이스라인 시뮬레이션용일 뿐 이식 기법 없음
- **ID**: ieee:7313676
- **Type**: conference
- **Published**: 8-11 Sept.
- **Authors**: Hadi E. Sawaya, Elias A. Rachid
- **PDF**: https://ieeexplore.ieee.org/document/7313676
- **Abstract**: This paper deals with the joint modulation relaying (JMR) design for the two-way relay channel where two users exchange information via a half-duplex relay node. We studied in particular the broadcast mode where the relay node combines the bits received from the two users and retransmit the combined information to both users. Symmetric and asymmetric data rate transmissions are considered. We show that the performance of the JMR scheme that uses a higher order modulation is improved using asymmetric constellations. This was verified by calculation the capacity of the channel and by determining the bit error probability of an LDPC coded JMR scheme using Monte Carlo simulation. Moreover, increasing the degree of asymmetry will lead asymptotically to a lower order signal constellation as in a network coding scheme. Therefore, there's no need for a higher order modulation at the relay node in order to retransmit data but only to apply network coding and modulation using the constellation of the stronger link.

## Novel ECC structure and evaluation method for NAND flash memory

- **Status**: ✅
- **Reason**: A — NAND 플래시 ECC 직접, adaptive LDPC 구조 및 error-free information capacity 평가법 제시
- **ID**: ieee:7406921
- **Type**: conference
- **Published**: 8-11 Sept.
- **Authors**: Jiang Xiao-bo, Tan Xue-qing, Huang Wei-pei
- **PDF**: https://ieeexplore.ieee.org/document/7406921
- **Abstract**: The evaluation of error correction code (ECC) for NAND flash memory is increasingly complicated by the increasing bit error rate in memory. The concept of error-free information capacity is proposed to evaluate the performance ECC of NAND flash memory. The new method simultaneously considers the capacity and reliability of NAND flash memory. Low-density parity-check (LDPC) codes with a medium code rate can improve the integrated performance of NAND flash memory in order of magnitudes. Observations provide guides for the development of ECC schemes in NAND flash memory in future. An ECC structure based on adaptive LDPC codes is also presented in this paper. The new structure achieves integrated performance of both capacity and reliability in NAND flash memory.

## Efficient stochastic list successive cancellation decoder for polar codes

- **Status**: ✅
- **Reason**: C 후보 — stochastic list SC 디코더는 polar용이나 stochastic decoding은 부호 비의존적 BP 기법이라 바이너리 LDPC BP HW에 이식 여지, 애매하여 살림
- **ID**: ieee:7406997
- **Type**: conference
- **Published**: 8-11 Sept.
- **Authors**: Xiao Liang, Chuan Zhang, Menghui Xu +2
- **PDF**: https://ieeexplore.ieee.org/document/7406997
- **Abstract**: Representing continuous values by streams of random binary bits, stochastic decoding has shown advantages in both hardware efficiency and fault tolerance, therefore has been widely adopted by iterative decoding of error correction codes such as low-density parity-check (LDPC) codes and so on. Recently, polar codes, the first codes that can provably achieve the capacity of symmetric binary-input discrete memoryless channels (B-DMCs), have drawn a lot of attentions from both academia and industry. Although, polar codes with list successive cancellation (SC) decoding can outperform several best-known LDPC codes even within high error-rate regions, the linearly increasing hardware complexity makes its efficient implementation difficult. To this end, the stochastic list SC polar decoding algorithm is proposed in this paper to provide a good tradeoff between performance and complexity. In order to increase the decoding performance of stochastic list SC polar decoder, doubling probability approach is presented. The corresponding hardware architecture is also given. The approximate doubling approach is employed to facilitate the efficient implementation. Implementation results have shown that the proposed stochastic list SC polar decoder can achieve a good trade-off between performance and complexity.

## Loop acceleration and instruction repeat support for application specific instruction-set processors

- **Status**: ❌
- **Reason**: ASIP 루프 가속/명령어 반복 하드웨어 — LDPC와 무관
- **ID**: ieee:7406957
- **Type**: conference
- **Published**: 8-11 Sept.
- **Authors**: Zhenzhi Wu, Dake Liu, Xiaoyang Li
- **PDF**: https://ieeexplore.ieee.org/document/7406957
- **Abstract**: Computation intensive tasks which consist of nested short loops usually suffer from massive control overhead, or memory size increasing when employing loop unrolling. In this approach, by introducing a modified instruction fetch unit with instruction FIFO and multiple loop controllers, loops can be performed in hardware, and single execution-cycle instructions can be executed in self-loop. Therefore no loop overhead exists for the optimized processor. The flexibility and the instruction granularity are maintained. Special domains for loop and repeat indications are added in the application-specific instructions. The proposed approach achieves dramatically performance and area benefits for many nested short loop dominated programs where the loops are determinable.

## Improved coded massive MIMO OFDM detection using LLRs derived from complex ratio distributions

- **Status**: ❌
- **Reason**: MIMO-OFDM 검출기 LLR 유도 — 채널 검출 특이적, LDPC는 베이스라인, NAND 이식 기법 없음
- **ID**: ieee:7390482
- **Type**: conference
- **Published**: 7-9 Sept. 
- **Authors**: Ali Al-Askery, Charalampos C. Tsimenidis, Said Boussakta +1
- **PDF**: https://ieeexplore.ieee.org/document/7390482
- **Abstract**: In this paper, a novel receiver is proposed for coded massive Multiple-Input-Multiple-Output systems using Orthogonal Frequency Division Multiplexing (MIMO-OFDM). The receiver utilizes log-likelihood ratios (LLR) derived from complex ratio distributions to model the noise probability density function (PDF) at the output of a zero-forcing detector. These LLRs are subsequently used to improve the performance of the decoding of Low Density Parity Check (LDPC) codes. The Neumann large matrix approximation is employed to simplify the matrix inversion in deriving the PDF. To verify the new findings, Monte Carlo simulations are used to demonstrate the optimality of the fitting between the derived PDF the experimentally obtained histogram of the noise. Further simulations results over time-flat frequency selective multi-path fading channels demonstrated improved performance over equivalent systems using the Gaussian approximation for the PDF of the noise. A significant gain of 1 dB was observed at bit error rate of 10-4 which corresponds to a reduction of approximately 30 receive antenna elements.

## Throughput maximization in hybrid FSO/RF communication systems

- **Status**: ❌
- **Reason**: 하이브리드 FSO/RF 전력할당/처리량 최적화 — LDPC 무관, 떼어낼 ECC 기법 없음
- **ID**: ieee:7342264
- **Type**: conference
- **Published**: 7-8 Sept. 
- **Authors**: S. Enayati, H. Saeedi, N. Mokari
- **PDF**: https://ieeexplore.ieee.org/document/7342264
- **Abstract**: In this paper, we analyze the problem of power allocation with the objective of maximizing the throughput for hybrid free-space optical/radio-frequency (FSO/RF) communication systems. Such systems consist of a free space optical link as well as an RF link. We consider both soft switching (SS) and hard switching (HS) schemes. In the former, at any time slot only one of the links is active while in the latter, both links simultaneously transmit data and the available power is divided between the two links. It is shown that for a given visibility, the obtained spectral efficiency is always greater than that of HS. The superiority of the SS scheme over the HS scheme is so significant such that the SS scheme outperforms the HS scheme for a visibility as bad as fives times lower than that of the HS case.

## High-Throughput FPGA-Based QC-LDPC Decoder Architecture

- **Status**: ✅
- **Reason**: 바이너리 QC-LDPC 디코더 신규 PCM 표현/superlayer 파이프라이닝 FPGA 아키텍처 — 이식 가능 HW(D)
- **ID**: ieee:7390967
- **Type**: conference
- **Published**: 6-9 Sept. 
- **Authors**: Swapnil Mhaske, Hojin Kee, Tai Ly +2
- **PDF**: https://ieeexplore.ieee.org/document/7390967
- **Abstract**: We propose without loss of generality strategies to achieve a high-throughput FPGA-based architecture for a binary Quasi-Cyclic Low-Density Parity-Check (QC-LDPC) code based on a circulant-1 identity matrix construction. We present a novel representation of the parity-check matrix (PCM) providing a multi-fold throughput gain. Splitting of the node processing algorithm enables us to achieve pipelining of blocks and hence layers. By partitioning the PCM into not only layers but superlayers we derive an upper bound on the two-layer pipelining depth for the compact representation. To validate the architecture, a decoder for the IEEE 802.11n (2012) QC-LDPC is implemented on the Xilinx Kintex-7 FPGA with the help of the FPGA IP compiler available in the NI LabVIEW Communication System Design Suite (CSDS). It offers an automated and systematic compilation flow where an optimized hardware implementation from the LDPC algorithm was generated, achieving an overall throughput of 608Mb/s (at 260MHz). As per our knowledge this is the fastest implementation of the IEEE 802.11n QC-LDPC decoder using an algorithmic compiler.

## Performance Improvement of Accumulate-Repeat-Accumulate Codes with Bounded Complexity

- **Status**: ✅
- **Reason**: SC-ARA(spatially-coupled ARA) 신규 부호 구성+DE 분석, 바이너리 SC-LDPC 계열 코드설계 기법 이식 가능(E)
- **ID**: ieee:7391080
- **Type**: conference
- **Published**: 6-9 Sept. 
- **Authors**: Waleed Saad, Shady M. Ibraheem, Maher M. Abd Elrazzak +2
- **PDF**: https://ieeexplore.ieee.org/document/7391080
- **Abstract**: In this paper, we introduce a new family of codes named as systematic spatially-coupled accumulate repeat accumulate SC-ARA codes based on chain of interconnected proto-graphs over the binary erasure channels (BEC). It has been observed that Spatially-coupled low density parity check (SC-LDPC) codes are able to approach the capacity universally across the binary-input memoryless (BMS) channels. A density evolution (DE) analysis is provided for this class of codes which categorized by bounded density and/or complexity per information bit. Simulation results show that the spatially coupling of ensembles of ARA codes, with bounded density and/or complexity, drives the message-passing belief propagation decoding threshold (BP) to be closed to the maximum a posterior (MAP) threshold of the underlying codes over the BEC.

## Improved Design Criteria for Duplicate LT Codes

- **Status**: ❌
- **Reason**: BEC상 LT/fountain UEP 코드 설계 — fountain/erasure JSCC류, 채널 ECC 디코더 기여 아님
- **ID**: ieee:7390977
- **Type**: conference
- **Published**: 6-9 Sept. 
- **Authors**: Huaan Li, Lei Yuan, Yi Wan
- **PDF**: https://ieeexplore.ieee.org/document/7390977
- **Abstract**: In this paper, we propose an efficient scheme to construct LT codes that can provide unequal error protection (UEP) property. We implement low rate LDPC codes instead of the duplication and utilize a low constant average degree distribution with high intermediate symbol recovery rates (ISRR) to improve the performance of more important bits (MIB). Asymptotic analysis of the proposed scheme is obtained by deriving unequal density evolution (DE) formulas over the binary erasure channel (BEC). Utilizing LDPC codes and the degree distribution with high ISRR in the proposed scheme, the UEP property is flexible and efficient. Compared with previous duplicate UEP-LT codes, mathematical analysis and simulation results demonstrate that the proposed UEP-LT codes have better performance.

## SCMA for Open-Loop Joint Transmission CoMP

- **Status**: ❌
- **Reason**: SCMA CoMP 5G 무선 다중접속, LDPC ECC 기법 없음
- **ID**: ieee:7391126
- **Type**: conference
- **Published**: 6-9 Sept. 
- **Authors**: Usa Vilaipornsawai, Hosein Nikopour, Alireza Bayesteh +1
- **PDF**: https://ieeexplore.ieee.org/document/7391126
- **Abstract**: Sparse Code Multiple Access (SCMA), a non-orthogonal multiple access scheme, has been introduced as a key 5G technology to improve spectral efficiency. In this work, we propose SCMA to enable open-loop coordinated multipoint (CoMP) joint transmission (JT). The scheme combines CoMP techniques with multi-user SCMA (MU-SCMA) in downlink. This scheme provides open-loop user multiplexing and JT in power and code domains, with robustness to mobility and low overhead of channel state information (CSI) acquisition. The combined scheme is called MU-SCMA- CoMP, in which SCMA layers and transmit power of multiple transmit points (TPs) are shared among multiple users while a user may receive multiple SCMA layers from multiple TPs within a CoMP cluster. The benefits of the proposed scheme includes: i) drastic overhead reduction of CSI acquisition, ii) significant increase in throughput and coverage, and iii) robustness to channel aging. Various algorithms of MU-SCMA-CoMP are presented, including the detection strategy, power sharing optimization, and scheduling. System level evaluation shows that the proposed schemes provide significant throughput and coverage gains over OFDMA for both pedestrian and vehicular users.

## Exit-Chart-Based Design of Irregular Precoded Power-Imbalanced Optical Spatial Modulation

- **Status**: ❌
- **Reason**: 광 공간변조(OSM) EXIT 기반 irregular precoder 설계 — 응용 특이적, 떼어낼 바이너리 LDPC ECC 기법 없음
- **ID**: ieee:7390941
- **Type**: conference
- **Published**: 6-9 Sept. 
- **Authors**: Naoki Ishikawa, Shinya Sugiura
- **PDF**: https://ieeexplore.ieee.org/document/7390941
- **Abstract**: In this paper, we propose a near-capacity irregular precoded power-imbalanced (PI) optical spatial modulation (OSM) scheme. The PI-OSM scheme was developed for negating the effects of high channel correlation, which is often observed in optical wireless communications. In our proposed scheme, multiple PI-OSM subcodes are used to create a novel irregular precoded PI-OSM architecture. This allows us to match the extrinsic information transfer curves of the inner and outer codes in a flexible manner, hence reducing the signal-to-noise ratio required for achieving an infinitesimally low bit error rate (BER). Our numerical simulation results demonstrate that the irregular precoded PI-OSM scheme achieves a high performance, particularly in noise-dominant channels, and it outperforms the repetition-coded benchmark scheme with pulse-amplitude modulation.

## A novel channel estimation and equalization method for DOCSIS 3.1 Downstream

- **Status**: ❌
- **Reason**: DOCSIS 3.1 채널추정/등화 — LDPC 디코더 무관
- **ID**: ieee:7391284
- **Type**: conference
- **Published**: 6-9 Sept. 
- **Authors**: JaeHwui Bae, Sang-Jung Ra, Jae-Ho Lee +2
- **PDF**: https://ieeexplore.ieee.org/document/7391284
- **Abstract**: We propose a novel channel estimation and equalization method optimized for the scattered and the continuous pilot patterns of DOCSIS 3.1 Downstream system. The proposed method aims not only to compensate the multipath interferences and OFDM symbol timing offsets but also to minimize the complexity of hardware implementation. We showed the performance of the proposed method through 4096QAM constellation analysis after channel equalization.

## Performance Evaluation of GFDMA Systems Using an Analytical Tool

- **Status**: ❌
- **Reason**: GFDMA BER 분석툴(FLAT) — 무선 다중접속 성능평가, LDPC ECC 무관
- **ID**: ieee:7391077
- **Type**: conference
- **Published**: 6-9 Sept. 
- **Authors**: Maryam Sabbaghian, Arash Ebadi-Shahrivar, Hamid Saeedi
- **PDF**: https://ieeexplore.ieee.org/document/7391077
- **Abstract**: This paper analyzes the bit error rate (BER) performance of grouped frequency division multiple access (GFDMA) using a tool known as finite length analytical tool (FLAT). We derive the equations of the FLAT method including the variance of the equalizer output signal for different iterations. We use this value to calculate the BER of the equalizer output when a specific set of sub-carriers are assigned to more than one user. Through comparative performance evaluation, we show that the proposed FLAT method can accurately evaluate the BER of the GFDMA system and the difference between the theoretical and simulated BER curves is at most 0.1 dB. Thus, we can efficiently utilize the FLAT method to design the GFDMA system and avoid extensive simulations required to determine the number of users transmitting over the same sub-carriers simultaneously.

## Non-binary LDPC coded OFDM in impulsive power line channels

- **Status**: ❌
- **Reason**: 비이진(NB) LDPC와 SL-FFT 디코딩 제안 — 비이진 LDPC는 제외 대상
- **ID**: ieee:7362620
- **Type**: conference
- **Published**: 31 Aug.-4 
- **Authors**: Ghanim A. Al-Rubaye, Charalampos C. Tsimenidis, Martin Johnston
- **PDF**: https://ieeexplore.ieee.org/document/7362620
- **Abstract**: In this paper, we propose Irregular Non-Binary Low Density Parity Check (IR-NB-LDPC) codes with Signed Log Fast Fourier Transform (SL-FFT) decoding algorithm to overcome the harsh environment of power-line communication (PLC) channels. Their performance is compared with Irregular Binary LDPC (IR-B-LDPC) codes using the Sum Product algorithm (SPA). The sparse parity check matrix H of both codes are constructed using progressive edge growth (PEG) algorithm with a novel initialization of the apriori log likelihood ratios (LLR) of each decoder to mitigate the highly impulsive noise in PLC channels. Numerical performance results obtained via simulations show that the proposed system at bit error rate of 10-4 achieves a coding gain of more than 21 dB compared to uncoded system and more than 6 dB compared to IR-B-LDPC codes for the same block length in bits and rates, however, this is accomplished with higher decoding complexity.

## Coding and modulation techniques for high spectral efficiency transmission in 5G and satcom

- **Status**: ❌
- **Reason**: 5G/Satcom 코딩·변조 후보 비교 서베이 — 신규 디코더·구성·HW 기여 없음, 응용 특이적
- **ID**: ieee:7362884
- **Type**: conference
- **Published**: 31 Aug.-4 
- **Authors**: Haesik Kim
- **PDF**: https://ieeexplore.ieee.org/document/7362884
- **Abstract**: Achieving high spectral efficiency is the key requirement of 5G and Satcom systems because it provides us with much lower cost per bit. In order to achieve high spectral efficiency, channel coding and modulation are the key part of the physical layer. Basically, high spectral efficiency can be achieved when adopting a high order modulation and low code rate at a high SNR. However, the transmit power is limited in practical wireless communication systems. The high order modulation and low code rate is restrictively used. Thus, the integrated version of 5G and Satcom needs a new type of channel coding scheme. In this paper, we look into 5G requirements and Satcom's role in 5G, review candidate error correction coding schemes for 5G and future Satcom in terms of spectral efficiency, and evaluate the performance of the candidate error correction codes.

## Performance of transmitted reference pulse cluster UWB communication systems using LDPC codes

- **Status**: ❌
- **Reason**: UWB TRPC에 LDPC 도입+PEG식 H 구성, 무선 응용 BER 비교 — 표준 구성 재사용, 떼어낼 신규 기법 없음
- **ID**: ieee:7343367
- **Type**: conference
- **Published**: 30 Aug.-2 
- **Authors**: Junshan Zang, Zhonghua Liang, Jinjin Liu +2
- **PDF**: https://ieeexplore.ieee.org/document/7343367
- **Abstract**: Transmitted reference pulse cluster (TRPC) structure was proposed as an improved transmitted reference (TR) signaling for low date-rate ultra-wideband (UWB) communications. In the uncoded case, TRPC outperforms the conventional TR and non-coherent pulse position modulation (NC-PPM) signaling schemes. Moreover, it overcomes the implementation problem of the long delay line inherent in the conventional TR. Therefore, TRPC is a promising candidate for noncoherent UWB communication systems. Accordingly, coded TRPC has also been developed employing several forward error correction (FEC) codes, such as Reed-Solomon and convolutional codes. Based on these previous works, in this paper low-density parity-check (LDPC) codes are introduced to the TRPC system and two methods are presented to construct the parity-check matrix for LDPC codes. We evaluate the bit error rate (BER) performance of the two corresponding LDPC codes in the IEEE 802.15.4a channels. Results show that both the two investigated LDPC codes obtain significant performance gains in terms of the BER over the existing FEC codes used in the TRPC system.

## Recursive encoding of spatially coupled LDPC codes with arbitrary rates

- **Status**: ✅
- **Reason**: 임의 rate SC-LDPC 재귀 인코딩용 수정 패리티검사 구조+시프트레지스터 구현, BP threshold 개선 — 바이너리 코드설계 이식 가능(E)
- **ID**: ieee:7343281
- **Type**: conference
- **Published**: 30 Aug.-2 
- **Authors**: Junyang Ma, Zhongwei Si, Zhiqiang He +1
- **PDF**: https://ieeexplore.ieee.org/document/7343281
- **Abstract**: Spatially coupled LDPC codes have attracted much attention due to the promising performance. Recursive encoding with low delay and low complexity has been proposed in the literature for selected node degrees. To realize the recursive encoding of spatially coupled LDPC codes with arbitrary rates, we propose in this paper a modified structure of the parity-check matrix and implement the encoding using a shift-register regardless of the node degrees. By rearranging the edge connections, the parity bits at each coupling position can be jointly determined by the information bits at the current position and the encoded bits at former positions. Performance analysis in terms of design rate and density evolution has been provided. It can be observed that the modified code structure leads to a better belief-propagation threshold. Finite-length simulation results are provided, which verify the theoretical analysis.

## Asymptotic performance analysis of protograph LDPC-coded STBC systems in fading channels

- **Status**: ❌
- **Reason**: protograph LDPC+STBC 점근 성능분석(PEXIT/BER bound), 무선 다중안테나 응용 — 떼어낼 신규 디코더·구성·HW 없음
- **ID**: ieee:7343282
- **Type**: conference
- **Published**: 30 Aug.-2 
- **Authors**: Yi Fang, Guojun Han, Pingping Chen +2
- **PDF**: https://ieeexplore.ieee.org/document/7343282
- **Abstract**: In this paper, we investigate the performance of the protograph low-density parity-check (LDPC) codes concatenated with space-time block code (STBC) over Rayleigh fading channels. We firstly extend the modified protograph extrinsic information transfer (PEXIT) algorithm in order to analyze the convergence performance of protograph codes. Based on the extended PEXIT algorithm and Gaussian approximation, we further derive the asymptotic bit-error-rate (BER) expression of protograph codes. Utilizing the PEXIT algorithm, theoretical and simulated BERs, we compare the performance of two classical protograph codes, i.e., accumulate-repeat-by-3-accumulate (AR3A) code and accumulate-repeat-by-4-jagged-accumulate (AR4JA) code, regular LDPC code, and optimized irregular LDPC codes, and illustrate that the AR3A code is superior to other three codes. Additionally, we discuss the impact of the number of receive antennas (i.e., NR) on the system performance and verify that the theoretical analyses hold as NR varies. As a result, the AR3A code stands out as a good candidate for wireless communication applications with multiple antennas.

## A new architecture for high throughput, low latency NB-LDPC check node processing

- **Status**: ❌
- **Reason**: NB-LDPC check node HW 아키텍처 — 비이진 LDPC는 제외 대상
- **ID**: ieee:7343516
- **Type**: conference
- **Published**: 30 Aug.-2 
- **Authors**: Philipp Schláfer, Vladimir Rybalkin, Norbert Wehn +3
- **PDF**: https://ieeexplore.ieee.org/document/7343516
- **Abstract**: Non-binary low-density parity-check codes have superior communications performance compared to their binary counterparts. However, to be an option for future standards, efficient hardware architectures must be developed. State-of-the-art decoding algorithms lead to architectures suffering from low throughput and high latency. The check node function accounts for the largest part of the decoders overall complexity. In this paper a new hardware aware check node algorithm and its architecture is proposed. It has state-of-the-art communications performance while reducing the decoding complexity. The presented architecture has a 14 times higher area efficiency, increases the energy efficiency by factor 2.5 and reduces the latency by factor of 3.5 compared to state-of-the-art architectures.

## Modified forced convergence decoding of LDPC codes with optimized decoder parameters

- **Status**: ✅
- **Reason**: forced convergence 결합 복잡도 저감 디코딩+최적 파라미터 탐색, 연산 55%·메모리접근 75% 감소 — 바이너리 LDPC 디코더 이식 가능(C)
- **ID**: ieee:7343339
- **Type**: conference
- **Published**: 30 Aug.-2 
- **Authors**: Muris Sarajlić, Liang Liu, Ove Edfors
- **PDF**: https://ieeexplore.ieee.org/document/7343339
- **Abstract**: Reducing the complexity of decoding algorithms for LDPC codes is an important prerequisite for their practical implementation. In this work we propose a reduction of computational complexity targeting the highly reliable codeword bits and show that this approach can be seamlessly merged with the forced convergence scheme. We also show how the minimum achievable complexity of the resulting scheme for given performance constraints can be found by solving a constrained optimization problem, and successfully apply a gradient-descent based stochastic approximation (SA) method for solving this problem. The proposed methods are tested on LDPC codes from the IEEE 802.11n standard. Computational complexity reduction of 55% and a 75% reduction of memory access have been observed.

## Partitioned scheduling for sphere decoding with runtime constraints for practical MIMO communication systems

- **Status**: ❌
- **Reason**: MIMO sphere decoding 스케줄링, LDPC 무관 — ECC 이식 기법 없음
- **ID**: ieee:7343392
- **Type**: conference
- **Published**: 30 Aug.-2 
- **Authors**: Tae-Hwan Kim, Jin-Hwee Kim
- **PDF**: https://ieeexplore.ieee.org/document/7343392
- **Abstract**: This paper presents a simple but effective scheduling scheme for sphere decoding (SD) with runtime constraints in multiple-input multiple-output communication systems. The proposed scheme imposes runtime constraints on SD to distribute the errors due to the early termination of SD. Because the distributed errors may be corrected effectively by forward error correction, the error-rate performance can be improved; experimental results show that the performance improvement is approximately 2 dB in terms of the signal-to-noise ratio to achieve a bit-error rate of 10-4 in 4×4 16-QAM systems.

## Joint equalization and decoding for a rateless coded V-OFDM system

- **Status**: ❌
- **Reason**: rateless coded V-OFDM 결합 등화·디코딩(fountain/rateless) — LDPC 베이스라인, 떼어낼 ECC 기법 없음
- **ID**: ieee:7343388
- **Type**: conference
- **Published**: 30 Aug.-2 
- **Authors**: Jing Zhang, Xiqian Luo, Panyu Fu +2
- **PDF**: https://ieeexplore.ieee.org/document/7343388
- **Abstract**: A novel rateless coded Vector Orthogonal Frequency Division Multiplexing (V-OFDM) system for adaptive transmission over wireless channels is studied in this paper. In particular, an iterative receiver with joint V-OFDM equalization and ratelss decoding is designed, which exchanges the logarithmic likelihood information between the belief propagation decoder and the maximum likelihood equalizer or the hard/soft decision based equalizer recursively. Both analytical and numerical results show that the proposed algorithm significantly improves the system performance with a modest complexity.

## Reliable and secure communications over Gaussian wiretap channel using HARQ LDPC codes and error contamination

- **Status**: ❌
- **Reason**: wiretap 보안+HARQ LDPC, 보안(secrecy) 응용 특이적이며 떼어낼 디코더/구성 기법 없음
- **ID**: ieee:7346824
- **Type**: conference
- **Published**: 28-30 Sept
- **Authors**: Mohamed Haj Taieb, Jean-Yves Chouinard
- **PDF**: https://ieeexplore.ieee.org/document/7346824
- **Abstract**: This paper investigates reliable and secure transmissions over the Gaussian wiretap channel. A physical layer coding scheme based on Low-Density-Parity-Check (LDPC) codes with granular Hybrid Automatic Repeat reQuest(HARQ) protocol is presented. HARQ granularity aims at sending coded data at the minimum rate required for legitimate successful decoding while minimizing the information leakage that may benefit to eavesdropping. It will be shown that the granularity increases the frame error rate at the eavesdropping receiver. Since the secrecy level can be assessed through the bit error rate (BER) at the unintended receiver, intraframe and interframe error contaminations are employed to convert the loss of only few packets in the wiretap channel into much higher BERs at the eavesdropper. From the BERs at the legitimate and illegitimate receivers, the reliability and security regions can be determined. It is observed that with granular HARQ and interframe error contamination, signal to noise (SNR) regions that are simultaneously reliable and secure are expanded significantly.

## Two-staged Weighted Bit Flipping (WBF) decoding algorithm for LDPC codes

- **Status**: ✅
- **Reason**: LDPC용 2단 WBF/BF 비트플립 복호로 error floor 저감; 이식 가능 디코더 알고리즘(C)
- **ID**: ieee:7405679
- **Type**: conference
- **Published**: 25-27 Sept
- **Authors**: Kexiang Ma, Jing Jin, Wei Li +1
- **PDF**: https://ieeexplore.ieee.org/document/7405679
- **Abstract**: In this paper, a two-staged decoding strategy which can be used for the Weighted Bit Flipping (WBF) based decoding algorithm for LDPC codes is presented. At the two stages, a parallel WBF and bit-flipping (BF) algorithms are adopted separately. Correspondingly, by the study of the iterative decoding process of the PWBF algorithm, a simple function is introduced to dynamically implement the switch of two decoding stages. The proposed algorithm can noticeably lower the error floor of PWBF algorithm with a modest increase in computation complexity and hardware cost. The validation of the proposed algorithm is verified by simulation.

## Hybrid construction of LDPC codes with (14, 8) Hamming code

- **Status**: ✅
- **Reason**: (14,8) Hamming 기반 하이브리드 LDPC 패리티검사행렬 구성+SPA 복호; 코드 설계 기법(E)
- **ID**: ieee:7405682
- **Type**: conference
- **Published**: 25-27 Sept
- **Authors**: Huan Ma, Yangwen Yu, Lijun Zhang +1
- **PDF**: https://ieeexplore.ieee.org/document/7405682
- **Abstract**: A method for constructing LDPC codes is presented based on a (14, 8) extended Hamming code which is formed via column splitting of the (7, 4) Hamming code. With this code and hybrid construction, it is effortless to generate an LDPC code by mapping the (14, 8) extended Hamming code to components of the parity-check matrix of the LDPC code. Simulation results show that the capacity of hybrid construction of PEG code and the (14, 8) extended Hamming code with rate 0.9288 is only a difference of 2 dB around to the Shannon limit owing to the gorgeous property of the (14, 8) code with sum-product algorithm decoding.

## (7, 4)-Hamming generalized LDPC code for Rayleigh fading channel

- **Status**: ✅
- **Reason**: (7,4)Hamming GLDPC 구성·짧은사이클 제거·MLD 복호; 바이너리 코드설계 기법(E), 애매하나 살림
- **ID**: ieee:7405686
- **Type**: conference
- **Published**: 25-27 Sept
- **Authors**: Yangwen Yu, Yanan Han, Lijun Zhang +1
- **PDF**: https://ieeexplore.ieee.org/document/7405686
- **Abstract**: To get a generalized version of LDPC code, we construct (7, 4)-Hamming GLDPC code with (7, 4) Hamming component code in this paper, and give the number of short cycles of this GLDPC code as well as the code weight distribution. Via MLD, the negative effects of short cycles limited in the Hamming block can be eliminated. Simulation results show that, up to 2 dB coding gain can be obtained for GLDPC code, with faster convergence rate, in comparison with the counterpart standard code, at BER of 10−7 in Rayleigh fading channel. Even compared with the standard LDPC code which has no 4-cycles, the better behaviors for GLDPC code, with still faster convergence rate, are achieved in several limits. These results may enhance the implementation of this GLDPC code in real world.

## Video over DSL with LDGM codes for interactive applications

- **Status**: ❌
- **Reason**: LDGM(Low-Density Generator Codes) AL-FEC 비디오 스트리밍, fountain/erasure형 응용으로 떼어낼 채널 LDPC ECC 기법 없음
- **ID**: ieee:7332718
- **Type**: conference
- **Published**: 24-25 Sept
- **Authors**: Filippo Casu, Julián Cabrera, Laith Al-Jobouri +1
- **PDF**: https://ieeexplore.ieee.org/document/7332718
- **Abstract**: Digital Subscriber Line (DSL) network access is subject to error bursts, which, for interactive video, can introduce unacceptable latencies if video packets need to be resent. If the video packets are protected against errors with Forward Error Correction (FEC) calculation of the application-layer channel codes themselves may also introduce additional latency. This paper proposes Low-Density Generator Codes (LDGM) rather than other popular codes because they are more suitable for interactive video streaming not only for their computational simplicity but also for their licensing advantage. The paper demonstrates that up to a 4 dB reduction in video distortion is achievable with LDGM Application Layer (AL) FEC. Telemedicine and video conferencing are typical target applications.

## Complexity reduced turbo differential decoding based on layered LDPC decoding

- **Status**: ✅
- **Reason**: 차동 디코더-LDPC 간 반복 디코딩에 layered scheduling 적용, 반복수 50% 감소 — 부호 비의존 layered decoding 기법은 바이너리 LDPC BP에 이식 가능(C)
- **ID**: ieee:7365145
- **Type**: conference
- **Published**: 23-25 Sept
- **Authors**: Christian Cabirol, Wolfgang Sauer-Greff, Andreas Bisplinghoff +1
- **PDF**: https://ieeexplore.ieee.org/document/7365145
- **Abstract**: In case of unknown carrier phase and/or imperfect channel estimation in communication systems using QPSK it is well known that phase and channel uncertainty can be resolved by differential modulation at the expense of doubling the bit error ratio. Such a differentially modulated QPSK approach has to be applied in wavelength division multiplexing (WDM) fiber optical communication systems using coherent transmission due to the phase ambiguity of carrier phase estimation (CPE) and potential cycle slips. However, this penalty can be diminished by using an iterative decoding procedure which passes information between the differential decoder and the decoder of a low-density parity-check (LDPC) code, a powerful state-of-the art forward error correction (FEC) code. In addition, it is shown that by applying a layered decoding schedule in the LDPC decoder, the number of required iterations can be reduced by up to 50%.

## Time frequency packed DP-QPSK superchannel field trial transmission over installed link

- **Status**: ❌
- **Reason**: TFP DP-QPSK 슈퍼채널 필드 전송, iterative MAP 검출이나 떼어낼 LDPC ECC 기법 없음
- **ID**: ieee:7328940
- **Type**: conference
- **Published**: 22-25 Sept
- **Authors**: Gianluca Meloni
- **PDF**: https://ieeexplore.ieee.org/document/7328940
- **Abstract**: Time frequency packing technique was demonstrated in a superchannel field trial transmission over long-haul distances. The technique allows a high spectral efficiency even with low order modulation formats. The transmission was successfully performed on an installed link between Milan and Finkenstein (Austria) in a loop back configuration, which included 2 ×660 km of ITU-T G.655 fiber. The superchannel is composed by eight subchannels with low-level modulation format, i.e. polarization multiplexed (PM)-quadrature phase shift keying (QPSK). The use of low order modulation format guarantee better robustness in terms of optical signal to noise ratio (OSNR) and reduced complexity with respect to higher order formats. Coherent detection was used together with iterative maximum a posteriori probability (MAP) detection and decoding at the receiver. A 992 Gb/s PM-QPSK superchannel was successfully transmitted between Milan-Finkenstein-Milan with a spectral efficiency (SE) of 6.2 bit/s/Hz. Long term measurements confirm the system reliability.

## Self-adaptation technique for bandwidth-variable transponders

- **Status**: ❌
- **Reason**: BVT 자가적응 트랜스폰더 기법, LDPC ECC 무관
- **ID**: ieee:7328985
- **Type**: conference
- **Published**: 22-25 Sept
- **Authors**: Francesco Fresi
- **PDF**: https://ieeexplore.ieee.org/document/7328985
- **Abstract**: Self-adaptive technique for Bandwidth Variable Transponders (BVTs) supporting superchannels in next generation optical networks is proposed. Automatic transponder configuration includes chromatic dispersion estimation, local oscillator fine tuning, maximization of information rate, subcarrier spacing optimization, while monitoring quality of transmission (QoT). The proposed procedure has been exploited in 1Tb/s field trial transmission over 1300 km.

## Experimental comparison of 1.28 Tb/s Nyquist WDM vs. time-frequency packing

- **Status**: ❌
- **Reason**: Nyquist WDM vs TFP 실험 비교, ECC 기법 없음
- **ID**: ieee:7328953
- **Type**: conference
- **Published**: 22-25 Sept
- **Authors**: Talha Rahman, Francesco Fresi, Antonio Napoli +9
- **PDF**: https://ieeexplore.ieee.org/document/7328953
- **Abstract**: We experimentally compared terabit transmission employing 16QAM Nyquist WDM and QPSK Time-Frequency Packing. The two modulation schemes have been transmitted over the same link configuration. The latter showed slightly better performance in terms of spectral efficiency and reach, at the expense of a more expensive and complex hardware.

## Modern error correcting codes for 4G and beyond: Turbo codes and LDPC codes

- **Status**: ❌
- **Reason**: 4G/이후 무선용 Turbo vs LDPC 비교 서베이; 신규 디코더/구성/HW 기여 없음
- **ID**: ieee:7323369
- **Type**: conference
- **Published**: 21-24 Sept
- **Authors**: Pradeep M. Shah, Prakash D. Vyavahare, Anjana Jain
- **PDF**: https://ieeexplore.ieee.org/document/7323369
- **Abstract**: Modern error correcting codes are used in 4G and are proposed for future wireless cellular networks for achieving improved channel error correcting capability. Turbo codes, and their improved variants with better error correcting capabilities, and LDPC codes are near Shannon limit channel codes and are used in such systems. This paper focuses on error correcting codes used in present and future generations of mobile communication systems for improving system performance. These systems have higher data rates and low energy per bit. The comparative performance evaluation of Turbo codes and LDPC codes and their suitability for future cellular network is explored in the paper. This comparison will be useful in the selection of error correcting codes for future mobile communication systems.

## FFT-based parallel encoding algorithm for structured LDPC codes

- **Status**: ✅
- **Reason**: 구조적 QC-LDPC용 FFT 기반 병렬 인코딩 알고리즘; 인코더 측이지만 코드설계/구현 기여(E/D), 애매하므로 살림
- **ID**: ieee:7446776
- **Type**: conference
- **Published**: 21-23 Sept
- **Authors**: Yanan Fan, Xin Meng, Xiujuan Yao +1
- **PDF**: https://ieeexplore.ieee.org/document/7446776
- **Abstract**: Structured LDPC, such as RA, IRA, ARA, QC-LDPC etc., are some important LDPC codes, these codes usually have very good performance and facilitate the implementation of encoding and decoding for the structural features they have. A new method for the encoding of the structured LDPC codes has been presented, namely FFT-based parallel encoding algorithm, which uses FFT to realize the parallel encoding of LDPC codes by achieving the circular convolution in the frequency domain. The study shows that the proposed algorithm has lower computational complexity than the previously proposed encoding algorithm. Although transforming to the frequency domain requires complex operations in real domain which increasing the number of the quantization points, the throughput of the encoder has greatly improved because of the increase of the degree of parallelism. The simulation results show that the computational complexity of the FFT-based encoding algorithm has an approximately linear relationship with the size of sub-circulate matrix, and when this size goes larger, the newly proposed algorithm will possess a lower computational complexity and a higher throughput compared with the previously proposed algorithms.

## Interface-aware LDPC codes for millimeter wave communication systems

- **Status**: ❌
- **Reason**: 밀리미터파 이더넷 인터페이스용 표준 LDPC 코드 설계로 지연 최소화; 표준 구성 적용 수준, 신규 기법 없음
- **ID**: ieee:7446778
- **Type**: conference
- **Published**: 21-23 Sept
- **Authors**: Peipei Li, Zhigang Zhou, Meili Na
- **PDF**: https://ieeexplore.ieee.org/document/7446778
- **Abstract**: Millimeter wave communication is a main solution for the high speed backhaul and ultra-high speed access transmission. This paper presented the interface-aware LDPC codes in the millimeter-wave system to support highspeed Ethernet interfaces and reduce the conversion delay. Considering constraints of the encoded codeword length of 1 G to 100 G Ethernet physical layer, LDPC (196, 120), LDPC (588, 528), LDPC (1197, 1089) codes on the basis of 1 G, 10 G and 100G Ethernet interface were designed to reach low latency in the channel coding process. The simulation results claimed that the interface-aware LDPC codes have an excellent performance and the minimum processing delay in the system, taking encoding delay and decoding delay into consideration. The encoding delay of 0.58 - 1.17 us and the decoding delay of 3.20 - 4.26 us could meet the code rate for the different channels in Ethernet interfaces.

## A simplifed joint demapping and decoding for LDPC coded BICM systems

- **Status**: ✅
- **Reason**: LDPC-BICM 결합 디매핑/디코딩에서 UMP-BP 단순화 + LLR 최적화 제안; 이식 가능 BP 디코더 변형(C)
- **ID**: ieee:7446764
- **Type**: conference
- **Published**: 21-23 Sept
- **Authors**: Ping Huang, Yueheng Li, Meiyan Ju
- **PDF**: https://ieeexplore.ieee.org/document/7446764
- **Abstract**: To make full use of the characteristics of LDPC decoding, Stephan ten Brink had proposed a joint iterative demapping and decoding algorithm for LDPC coded BICM systems. Based on Brink proposed algorithm, we propose a modified joint iterative scheme to further reduce the computation complex. Different from the algorithm presented by Brink, in the process of iterative demapping and decoding, the proposed method simplifies the update calculation of the LDPC parity check nodes by adopting the UMP-BP. More importantly, to compensate for the performance degradation brought by UMP-BP, LLRs optimization based on certain optimality criterion is employed for the proposed method. Numerical analysis shows that the complexity of the proposed method is less than traditional joint iterative algorithm. Simulation results also show that by LLRs optimization the proposed method achieves noticeable performance improvement compared with the BICM-ID and the joint iterative algorithm.

## Joint Channel Network Coding for correlated sources

- **Status**: ❌
- **Reason**: PLNC/TWRC 결합 채널-네트워크 코딩; LDPC는 베이스라인, 소스 상관 활용은 네트워크코딩 특이적, 떼어낼 ECC 기법 없음
- **ID**: ieee:7446833
- **Type**: conference
- **Published**: 21-23 Sept
- **Authors**: Youssef Zid, Sonia Zaibi Ammar, Ridha Bouallègue
- **PDF**: https://ieeexplore.ieee.org/document/7446833
- **Abstract**: In this paper, we consider a Generalized Joint Channel Network Coding (GJCNC) applied to Physical Layer Network Coding (PLNC) for Two Way Relay Channel (TWRC). For this purpose, two correlated sources A and B desire to exchange information with each other by the help of a relay R. PLNC allows the relay to decode the combined information of both sources from the superimposed information. A Low Density Parity Check (LDPC) code is used as a channel code. A new design of GJCNC is developed by exploiting the correlation between nodes. Since the relay doesn't know in advance the correlation between sources, an estimation of this quantity must be applied. Simulation results show that the Bit Error Rate (BER) can be significantly decreased by exploiting this correlation. In addition, a lower number of iterations is necessary to achieve a desired BER in comparison with a classical scheme which doesn't exploit the correlation between sources.

## A 2.48Gb/s FPGA-based QC-LDPC decoder: An algorithmic compiler implementation

- **Status**: ✅
- **Reason**: 2.48Gb/s QC-LDPC FPGA 디코더 병렬화 아키텍처 — HW(D) 이식 가능
- **ID**: ieee:7324649
- **Type**: conference
- **Published**: 20-22 Sept
- **Authors**: Swapnil Mhaske, David Uliana, Hojin Kee +3
- **PDF**: https://ieeexplore.ieee.org/document/7324649
- **Abstract**: The increasing data rates expected to be of the order of Gb/s for future wireless systems directly impact the throughput requirements of the modulation and coding systems of the physical layer. In an effort to design a suitable channel coding solution for 5G wireless systems, in this brief we present two approaches to improve the throughput of a Quasi-Cyclic Low-Density Parity-Check (QC-LDPC) decoder architecture. While providing an algorithmic method to enhance parallel processing within the decoder in the first approach, in the second approach we apply the decoder architecture to achieve another highly-parallel architecture. We have successfully validated the second approach to get a 2.48Gb/s QC-LDPC decoder implementation operating at 200MHz on the Xilinx Kintex-7 FPGA in the NI USRP-2953R. For rapid-prototyping our research findings, the high-level description of the entire decoder was translated to a Hardware Description Language (HDL), namely VHDL, using the algorithmic compiler in the National Instruments LabVIEW™ Communication System Design Suite (CSDS™). As per our knowledge, at the time of writing this paper, this is the fastest FPGA-based implementation of a standard compliant QC-LDPC decoder on a USRP using an algorithmic compiler.

## Optimized metric clipping decoder design for impulsive noise channels at high signal-to-noise ratios

- **Status**: ✅
- **Reason**: 임펄스 잡음용 metric clipping 디코더 기법, 부호 비의존적이라 LDPC BP의 LLR 클리핑으로 이식 가능성 — 애매하여 살림(C, Phase3)
- **ID**: ieee:7324641
- **Type**: conference
- **Published**: 20-22 Sept
- **Authors**: Changsheng Chen, Wai Ho Mow
- **PDF**: https://ieeexplore.ieee.org/document/7324641
- **Abstract**: In many practical communication systems, the channel is corrupted by non-Gaussian impulsive noise (IN). It introduces decoding metric mismatch for the traditional Euclidean metric decoders and limits system performance. The situation is worsen by the practical difficulty in accurately estimating the IN statistics. Recently, some metric clipping based decoders with a properly chosen clipping threshold has been shown to be very effective in mitigating the effect of IN, even without a precise knowledge of its statistics. However, we observe that such a clipping threshold is derived based on some assumptions which lead to an error floor in the bit error probability curve at high signal-to-noise ratio (SNR). In this work, a clipping threshold is derived by an optimization approach without exploiting the IN statistics. It is demonstrated by experiment that with our proposed clipping threshold, the optimized metric clipping decoder is able to perform close to the maximum likelihood decoding performance at high SNR under the Bernoulli Gaussian noise model with various parameters.

## Analysis of MIMO OFDM Based WiMAX System with LDPC

- **Status**: ❌
- **Reason**: MIMO OFDM WiMAX에 표준 QC-LDPC를 채널코딩으로 적용한 무선 응용, 떼어낼 신규 디코더·구성 기법 없음
- **ID**: ieee:7433810
- **Type**: conference
- **Published**: 2-4 Sept. 
- **Authors**: Monika Cheema, Sukanya A. Kulkarni
- **PDF**: https://ieeexplore.ieee.org/document/7433810
- **Abstract**: Driven by multimedia based applications, the future wireless systems require high data rate capable technologies. WiMAX has attracted immense interest globally for next generation wireless communication. The requirement of a spectrally efficient modulation technique and power efficient forward error correction scheme are key factors for these technologies. Wireless link quality is determined by transmission rate, range and reliability. Multiple Input Multiple Output (MIMO), along with Orthogonal Frequency Divsion Multiplexing(OFDM) techniques improve these parameters and are also habituated in WiMAX. It uses smart antenna techniques which include spatial transmit diversity and spatial multiplexing (SM). Spatial transmit diversity is achieved by applying Alamouti's Space Time coding. To achieve high capacity with minimum error rate Low-Density Parity-Check (LDPC) codes have recently drawn much attention and have superior interest because their error correction performance in wide applications. These codes are called Tanner graph which have short cycles that degrade the performance of LDPC decoders. The Quasi Cyclic (QC) LDPC as channel coding method is incorporated in the paper. STBC is used as a MIMO technique providing a strong diversity gain. Analysis of the performance of MIMO OFDM physical layer in WiMAX with the use of LDPC under different digital modulation techniques is presented in this paper.

## A Novel Approach for Design, Implementation and Construction of Low Density Parity Check (LDPC) Memory

- **Status**: ✅
- **Reason**: LDPC용 Majority Logic 디코딩에서 무오류 시 디코딩 사이클을 줄이는 신규 ML 디코더 기법 — 이식 가능 디코더(C)/메모리 ECC(B)
- **ID**: ieee:7433907
- **Type**: conference
- **Published**: 2-4 Sept. 
- **Authors**: B. Harshitha, M. Karthik, Vinayak Tambralli
- **PDF**: https://ieeexplore.ieee.org/document/7433907
- **Abstract**: Memory is an important part of any digital circuit in which data is stored and retrieved. Technology scaling, lower operating voltages and high integration densities leads for failures in the reliability of memories. The main problem is Single Event Upsets (SEUs) that alters the memories from its normal way of functioning. This paper presents design and implementation of Majority Logic (ML) detecting/decoding on different cyclic codes for error detection and correction. ML decoding method is more capable to detect and correct large number of errors but it takes same high access time for both error and error free codes which impacts memory performance. In this paper, the proposed advanced ML method reduces decoding cycles when there is no error in the data read. The error detection and correction method is done by majority logic decoding and is made effective for Low Density Parity Check (LDPC) codes. This method lowers the power consumption and latency for wide range sizes of code words.

## From low-architectural expertise up to high-throughput non-binary LDPC decoders: Optimization guidelines using high-level synthesis

- **Status**: ❌
- **Reason**: 비이진(non-binary) LDPC 디코더의 HLS FPGA 구현 — 바이너리 LDPC 한정 기준에 따라 비이진 제외
- **ID**: ieee:7293940
- **Type**: conference
- **Published**: 2-4 Sept. 
- **Authors**: Joao Andrade, Nithin George, Kimon Karras +4
- **PDF**: https://ieeexplore.ieee.org/document/7293940
- **Abstract**: HLS tools have been introduced with the promise of easening and shortening the design cycle of tedious and error-prone RTL-based development of hardware accelerators. However, they do so either by concealing meaningful hardware decisions which model the computing architecture-such as OpenCL compilers-or by abstracting them away into a high-level programming language-usually C-based. In this paper, we show that although Vivado HLS is sufficiently mature to generate a functionally correct FPGA accelerator from a naive description, reaching an accelerator which optimizes the FPGA resource utilization in a way that conveys maximum performance is a process for a hardware architect mindset. We use a highly demanding application, that requires real-time operation, and develop a non-binary LDPC decoder on a state-of-the-art Virtex 7 FPGA, using the Vivado HLS framework. Despite using the same programming syntax as a C-language software compiler, the underlying programming model is not the same, thus, the optimizations required in code refactoring are distinct. Moreover, directive-based optimizations that tweak the synthesized C description hardware must be used in order to attain efficient architectures. These processes are documented in this paper, to guide the reader on how an HLS-based accelerator can be designed, which in our case can come close to the performance achieved with dedicated hand-made RTL descriptions.

## Energy efficiency based concatenated LDPC and turbo codes for wireless sensor networks

- **Status**: ❌
- **Reason**: LDPC+turbo 직렬연접(WSN 에너지효율) — 표준 부호 조합, 떼어낼 신규 바이너리 LDPC 기법 없음
- **ID**: ieee:7338892
- **Type**: conference
- **Published**: 19-22 Sept
- **Authors**: Moataz M. Salah, Ashraf A. Elrahman
- **PDF**: https://ieeexplore.ieee.org/document/7338892
- **Abstract**: Recently wireless sensor networks have been shown to be very attractive for many wireless communications applications. A large number of very tiny sensors spread over the area under consideration constitute the wireless sensor networks. These tiny sensors have limited power resources. Due to limited built-in battery life-time at each sensor, minimizing power consumption in the sensors is an important issue for reliable and sustainable network operation. Error control coding (ECC), such as turbo codes and Low Density Parity Check (LDPC), is a classic approach used to increase link reliability and lower the required transmitted power. However, lowered power at the transmitter comes at the cost of extra power consumption due to the decoder at the receiver. Stronger codes provide better performance with lower power requirements, but have more complex decoders with higher power consumption than simpler error control codes. Turbo codes shows good performance at low SNR with iterative decoding but error floor phenomenon is occurred at high SNR region. LDPC code shows good performance at high SNR without error floor in contrast to turbo code. Therefore, LDPC code can be concatenated to turbo code to reduce error floor. In this paper, an energy efficiency based serially concatenated scheme of Low Density Parity Check (LDPC) and turbo codes scheme is proposed. The proposed scheme is discussed, analyzed, and evaluated. The performance of the proposed scheme is investigated through computer simulations, which shows an improvement in the bit error rate (BER).

## Updating conflict solution for pipelined layered LDPC decoder

- **Status**: ✅
- **Reason**: 파이프라인 layered LDPC 디코더 데이터 갱신 충돌 해결(레이어 순서 조정) — 이식 가능 HW 아키텍처(D)
- **ID**: ieee:7338879
- **Type**: conference
- **Published**: 19-22 Sept
- **Authors**: Zijing Wu, Kaixiong Su
- **PDF**: https://ieeexplore.ieee.org/document/7338879
- **Abstract**: Due to the overlap of nonzero sub-matrices in the successive layers of check matrix, the pipeline process might introduce data updating conflict in pipelined layered LDPC decoder. A solution to solve this problem by adjusting the decoding order of layers in check matrix and nonzero sub-matrices in the same layer is proposed in this paper. Furthermore the corresponding fast algorithm is given. In term of hardware implementation, this method which can be achieved simply by changing the order of the corresponding data in the ROMs will not increase any extra hardware overhead. Experimental results show that due to fewer idle clocks even zero idle clock need to be inserted into decoding pipeline when using this solution, the decoding rate is improved effectively. More importantly, the method will not degrade the decoding performance for LDPC codes.

## Performances analysis of polar codes decoding algorithms over variant binary-input channels

- **Status**: ❌
- **Reason**: Polar codes 디코딩 분석 + polar-LDPC concatenation. LDPC는 베이스라인, 떼어낼 새 LDPC 디코더/구성 기법 없음(비-LDPC 원칙 제외).
- **ID**: ieee:7338951
- **Type**: conference
- **Published**: 19-22 Sept
- **Authors**: Wenjiao Xie, Ruifu Tian, Lixin Li +2
- **PDF**: https://ieeexplore.ieee.org/document/7338951
- **Abstract**: In this paper, the performance of state of the art decoding methods of polar codes, such as the SC (Successive Cancellation), BP (belief propagation), LP (Linear Programming), LSC(List Successive Cancellation) and ML(Maximum Likelihood) decoding, over different binary-input discrete memoryless channels (B-DMCs) are presented. Simulation results indicate that decoding algorithms of polar codes have the performances of the estimated bit error rate (BER) below the order of 10-5. In addition, we came to the conclusion that BP algorithm outperforms SC at the cost of computational complexity. The performance of LP decoder is better than BP and the complexity is less than BP scheme, however, it can only be used in binary erasure channels (BECs). ML decoder has the best performance, but its high complexity makes it act as a reference to reveal the gap between ML and other algorithms. In order to remedy the performance deficiencies without any significant increase in decoding complexity, we further study the concatenated polar codes - the polar-LDPC(Low Density Parity Check) concatenation scheme, which is substantially outperforms ML decoding. What's more, the concatenated Polar-LDPC codes can remedy the error floor of LDPC codes. We firmly believed that the concatenated scheme of polar-LDPC would be a prominent technique in 5G (5th-generation) to support the more reliable transmission demand.

## Reliable and secure regions for the Gaussian wiretap channel using LDPC codes with granular HARQ

- **Status**: ❌
- **Reason**: Gaussian wiretap 보안+HARQ 무선 응용. LDPC 보안 응용, 떼어낼 디코더/구성/HW 기법 없음(보안 원칙 제외).
- **ID**: ieee:7368289
- **Type**: conference
- **Published**: 19-21 Sept
- **Authors**: Mohamed Haj Taieb, Jean-Yves Chouinard
- **PDF**: https://ieeexplore.ieee.org/document/7368289
- **Abstract**: This paper investigates reliable and secure transmissions over the Gaussian wiretap channel. A physical layer coding scheme based on Low-Density-Parity-Check (LDPC) codes with granular Hybrid Automatic Repeat reQuest(HARQ) protocol is presented. Increasing the HARQ granularity aims at sending coded data at the minimum rate required for legitimate successful decoding. This minimizes the information leakage that may benefit to eavesdropping. It will be shown that the granularity increases the frame error rate of the eavesdropper. Since the secrecy level can be assessed through the bit error rate (BER) at the unintended receiver, intraframe and interframe error contamination is employed to convert the loss of only few packets into much higher BERs. After obtaining the BERs at the legitimate and illegitimate receivers the reliable and secret regions can be determined. It is observed that with granular HARQ and interframe error contamination, regions that are reliable and secure at the same time are expanded.

## Improving MIMO systems performances by concatenating LDPC decoder to the STBC and MRC receivers

- **Status**: ❌
- **Reason**: MIMO STBC/MRC에 표준 LDPC를 단순 concatenate한 무선 응용. LDPC는 기성 채널코딩, 떼어낼 신규 기법 없음.
- **ID**: ieee:7368281
- **Type**: conference
- **Published**: 19-21 Sept
- **Authors**: Elies Ghayoula, Mohamed Haj Taieb, Jean-Yves Chouinard +2
- **PDF**: https://ieeexplore.ieee.org/document/7368281
- **Abstract**: Multiple-input multiple-output (MIMO) systems are commonly used in wireless communications to ensure high bit-rate and high capacity transmission. Space time block coding (STBC) is a technique used in MIMO to provide transmit diversity in communication over fading channels. Although STBC has full diversity gain, the coding gain need to be improved by using channel coding such as low density parity check (LDPC) codes or Turbo codes. This paper evaluates the performance of MIMO systems and the improvement obtained by concatenating LDPC codes. MIMO are based on spatially separated multiple transmitting and receiving antennas to provide diversity. This helps combatting the effect of multipath fading in wireless channels. For single-input multiple-output (SIMO) schemes, maximum ratio combining (MRC) receiver are used to handle redundantly the same information-bearing signal over two or more fading channel. The output of this receiver consist on soft decision metrics that can be fed to LDPC decoder for error correction. For MIMO and multiple-input single-output (MISO) systems, space time block codes (STBC) are used to generate orthogonal signals to avoid interference between signal streams. These signals are transmitted at slightly different times to benefit from temporal diversity. LDPC codes are used in conjunction with STBC to improve the error capability. This paper investigates diversity coding for MIMO systems combined with LDPC soft decoding. Performances of the proposed scheme in terms of bit error rates are reported.

## Research on Performance of Visible Light Communication Based on LDPC Code

- **Status**: ✅
- **Reason**: girth-4 제거 QC-LDPC 구성 + multiplicative factor 도입 개선 MS 디코딩(복잡도 저감) — 코드설계(E)+디코더(C) 이식 가능
- **ID**: ieee:7406090
- **Type**: conference
- **Published**: 18-20 Sept
- **Authors**: Yishuo Chen, Yanyong Su, Dong Xue +1
- **PDF**: https://ieeexplore.ieee.org/document/7406090
- **Abstract**: Visible light communication (VLC) technology is a new high-speed wireless access technology, finding a appropriate channel coding scheme is one of its main research directions. This paper proposed a new scheme to construct quasi-cyclic low-density parity-check (QC-LDPC) code. It is proved by the simulation result that the QC-LDPC code can help to improve the BER performance of the system because there is no girth four in its parity-check matrix. Then this paper studied the decoding algorithms of QC-LDPC code and proposed an improved decoding algorithm which can decrease the complexity of decoding process by introducing the multiplicative factor. The simulation results show that the QC-LDPC code is a suitable channel code for VLC, and the improved MS decoding algorithm reduces the complexity to a large extent on the basis of ensuring the BER performance of the VLC system.

## Non-binary LDPC Codes for Rotor Occlusion in Helicopter Communication

- **Status**: ❌
- **Reason**: 비이진(non-binary) LDPC — 기준상 명시 제외
- **ID**: ieee:7405829
- **Type**: conference
- **Published**: 18-20 Sept
- **Authors**: Zhang Fu-Xing, Xu Sheng-Wang
- **PDF**: https://ieeexplore.ieee.org/document/7405829
- **Abstract**: Satellite communication is important in helicopter communication, it can effectively improve the communication range and communication capacity. Controlled by the installation conditions, satellite antenna will be influenced by helicopter rotor periodically, signal transmission will suffer periodic continuous fading and occur periodic burst errors. Non-binary LDPC code is a kind of advanced channel coding scheme, it has strong ability of error correcting. It can convert continuous bit burst errors into less M-ary symbol errors, so it has a good ability to anti burst error. In this paper, simulation of using non-binary LDPC codes to resist the burst errors in the helicopter satellite communication is placed, the results show that non-binary LDPC codes can correct the burst error well which are caused by helicopter rotors. In addition, this paper also discusses a method of decoding initialization in which zero is set in positions under covered, the results demonstrate that the way to set zero can obtain better decoding performance advantages, the performance improvement is about 0.2dB.

## Asymmetric Slepian-Wolf Coding Design with Spatially Coupled LDPC Convolutional Codes

- **Status**: ❌
- **Reason**: Slepian-Wolf 소스 코딩(분산 압축)에 SC-LDPCC 적용 — 채널 ECC 아닌 소스코딩, 표준 구성 사용
- **ID**: ieee:7307804
- **Type**: conference
- **Published**: 17-19 Sept
- **Authors**: Shumin Tu
- **PDF**: https://ieeexplore.ieee.org/document/7307804
- **Abstract**: In this paper, a new Slepian-Wolf codec was constructed with spatially coupled Low-Density Parity-Check Convolutional (SP-LDPCC) codes. The approach is based on considering the correlation as a virtual binary erasure channel (BEC) and Binary-Input Additive White Gaussian Noise (BIAWGN)channel and applying the syndrome concept. The system is focusing on the compression of a equal-probable memory less binary source with side information at the decoder. Results obtained through both simulations and theoretical demonstrated that the proposed compression scheme performed better than the classical LDPC codes in asymmetric Slepian-Wolf framework.

## Low-rate LDPC convolutional codes with short constraint length

- **Status**: ✅
- **Reason**: LDPC convolutional code 설계 — graph 기법으로 최소거리 최대화·local cycle 분석, symbolic graph 신규 도구 (E 코드설계)
- **ID**: ieee:7314104
- **Type**: conference
- **Published**: 16-18 Sept
- **Authors**: Marco Baldi, Giovanni Cancellieri
- **PDF**: https://ieeexplore.ieee.org/document/7314104
- **Abstract**: We study a family of LDPC convolutional codes having code rate of the type 1/a, and analyze their minimum distance and local cycles length properties. We consider some low weight codewords that are known from the literature, and are easily obtained from the symbolic parity-check matrix of these codes. Starting from the structure of such codewords, we follow a twofold approach: i) we exploit graph-based techniques to design these codes with the aim to maximize their minimum distance while keeping the syndrome former constraint length as small as possible and ii) we provide a simple form for their generator matrices that allows to perform exhaustive searches through which we verify that the code design actually reaches its target. We also estimate the normalized minimum distance multiplicity for the codes we consider, and introduce the notion of symbolic graphs as a new tool to study the code properties.

## A 1.31Gb/s, 96.6% utilization stochastic nonbinary LDPC decoder for small cell applications

- **Status**: ❌
- **Reason**: stochastic 비이진(NB-LDPC) 디코더 칩 — 비이진 LDPC라 제외
- **ID**: ieee:7313837
- **Type**: conference
- **Published**: 14-18 Sept
- **Authors**: Xin-Ru Lee, Chih-Wen Yang, Chih-Lung Chen +2
- **PDF**: https://ieeexplore.ieee.org/document/7313837
- **Abstract**: In this paper, an over Gb/s stochastic nonbinary LDPC (NB-LDPC) decoder chip is first-reported. The operation of proposed decoder is transformed to logarithm domain, so that the decoding complexity is mitigated by the simpler summations and fewer bit-width. In addition, the storage requirements are dramatically reduced by truncated TFM architecture. After, benefited from architecture optimizations and symbol-serial property, the routing capability of proposed decoder is extraordinarily enhanced. According to the measurement results, this decoder can deliver 1.31Gb/s throughput under 368MHz clock frequency with the corresponding energy-efficiency of 0.45nJ/bit. Compared to other NB-LDPC decoders, our stochastic NB-LDPC decoder with 96.6% chip utilization improves 2x area-efficiency and 7x energy-efficiency.

## Threshold upper bounds and optimized design of protograph LDPC codes for the Binary Erasure Channel

- **Status**: ✅
- **Reason**: protograph LDPC threshold 상계 + capacity 근접 protograph 최적화 구성법, 바이너리 코드 설계(E) 이식 가능
- **ID**: ieee:7458400
- **Type**: conference
- **Published**: 14-18 Sept
- **Authors**: Surajkumar Harikumar, Jayanth Ramesh, Manikandan Srinivasan +1
- **PDF**: https://ieeexplore.ieee.org/document/7458400
- **Abstract**: Exact density evolution of protograph Low Density Parity Check (LDPC) codes over the Binary Erasure Channel (BEC) is considered. Upper bounds on the threshold are derived and expressed as single-variable minimizations. A simplified version of the upper bound is expressed in closed form in terms of the degrees of the nodes in the protograph. By maximizing the upper bound, useful conditions are derived for optimizing protographs to get thresholds close to capacity bounds. Using these conditions, a randomized construction method for good small-sized protographs is presented.

## Information set and iterative encoding for Affine Grassmann codes

- **Status**: ❌
- **Reason**: Affine Grassmann 코드 인코딩/permutation decoding — 비-LDPC 대수 부호, 이식 기법 없음
- **ID**: ieee:7458398
- **Type**: conference
- **Published**: 14-18 Sept
- **Authors**: Sudhir R. Ghorpade, Fernando L. Piñero
- **PDF**: https://ieeexplore.ieee.org/document/7458398
- **Abstract**: We explicitly determine an information set for the affine Grassmann codes of an arbitrary level and then use it to describe a systematic encoder for these codes. In the case of affine Grassmann codes of full level, we use our explicit information set together with some known results concerning duals of affine Grassmann codes to describe an iterative encoding algorithm and also show that permutation decoding is possible up to a reasonable bound.

## Generalized Gaussian distribution-based LDPC receiver for power-line communications

- **Status**: ❌
- **Reason**: PLC용 GGD 노이즈 모델 기반 LDPC 수신기 — 채널 특이적 LLR 모델, 떼어낼 일반 디코더/HW 기법 없음
- **ID**: ieee:7331950
- **Type**: conference
- **Published**: 14-17 Sept
- **Authors**: Tayyar Güzel, Ali E. Pusane, Hakan Deliç
- **PDF**: https://ieeexplore.ieee.org/document/7331950
- **Abstract**: Power-line communications (PLC) usually suffers from the effects of non-white (correlated) noise, which results from the memory in the channel. In order to combat the effects of the channel memory, interleavers, which introduce a large amount of delay, are often employed together with error control coding. Low-density parity-check (LDPC) codes have been adopted in the recent broadband PLC (BPLC) standards, including the Homeplug AV specification. Analysis of the noise amplitude distribution of each individual frequency component across the PLC noise spectrum has recently shown that noise can be modeled using the generalized Gaussian distribution (GGD). In this paper, an LDPC-coding based receiver that utilizes the GGD noise model is developed, and it is shown that the proposed receiver structure outperforms the conventional receivers designed under the Gaussian noise assumption. Real noise measurements and Homeplug AV specification definitions are employed to demonstrate the high error performance of the proposed receiver structure.

## Improving coding scheme of LDACS in the reverse link

- **Status**: ❌
- **Reason**: 항공통신 LDACS에 비이진(non-binary) LDPC/turbo 적용 — 비이진 LDPC는 제외, 떼어낼 신규 기법 없음
- **ID**: ieee:7311367
- **Type**: conference
- **Published**: 13-17 Sept
- **Authors**: Mohamad Mostafa, Nico Franzen, Ulrich Epple +1
- **PDF**: https://ieeexplore.ieee.org/document/7311367
- **Abstract**: We show in this paper the achievable improvement of the coding gain in the reverse link (air-to-ground) for the L-band Digital Aeronautical Communications System if the current forward error correction scheme based on a concatenated Reed-Solomon convolutional code is replaced by either a turbo code or a nonbinary low-density parity-check code for the smallest assignable data block. Additionally to improving the coding gain, the proposed coding schemes enable a fully iterative detection because of their soft-value decoding algorithms. This improves in general the detection process as a whole.

## Designing of efficient LDPC based MIMO-OFDM using 4-PSK scheme

- **Status**: ❌
- **Reason**: MIMO-OFDM 4-PSK 설계, LDPC 부수 언급뿐 — 무선 응용, 떼어낼 LDPC 기법 없음
- **ID**: ieee:7375653
- **Type**: conference
- **Published**: 10-12 Sept
- **Authors**: Megha Raghuwansi, Ashutosh Sharma
- **PDF**: https://ieeexplore.ieee.org/document/7375653
- **Abstract**: Current modern wireless communication is based on orthogonal frequency division multiplexing (OFDM) and the reliability of it significantly increased with the multiple inputs multiple outputs (MIMO), and there is a scope to enhance the performance of the system further. Working on the same goal this paper proposed a methodology to enhance end to end performance of the system. The projected methodology utilizes the MIMO-OFDM architecture with 4-PSK modulation and BPSK modulation. The BER is calculated for both the schemes and the performance of the system is evaluated with the different values of the FFT sizes and found that BER is achieved better with 1024 FFT points and BPSK modulation.

## VLSI architecture design and implementation of a LDPC encoder for the IEEE 802.22 WRAN standard

- **Status**: ✅
- **Reason**: 802.22 LDPC 인코더 VLSI/ASIC 아키텍처 — 이식 가능 HW(D)
- **ID**: ieee:7347589
- **Type**: conference
- **Published**: 1-4 Sept. 
- **Authors**: Nelson Alves Ferreira Neto, Joaquim Ranyere S. de Oliveira, Wagner Luiz A. de Oliveira +1
- **PDF**: https://ieeexplore.ieee.org/document/7347589
- **Abstract**: This paper presents two architectures for the Low Density Parity Check (LDPC) encoder, the first one based on a fully serial approach and the second one in a mixed way, as well as their respective realizations in ASIC. The proposed designs are capable of operating in 84 combinations of code rate and word size, according to the IEEE 802.22 Wireless Regional Area Network (WRAN) standard, aiming low power and small area. Although the proposed architectures are primarily designed for the mentioned standard, they can be easily adapted to other wireless broadband standards.

## Code 5-6: An Efficient MDS Array Coding Scheme to Accelerate Online RAID Level Migration

- **Status**: ❌
- **Reason**: RAID-5→6 마이그레이션용 MDS array code(비-LDPC erasure), 떼어낼 LDPC ECC 기법 없음
- **ID**: ieee:7349600
- **Type**: conference
- **Published**: 1-4 Sept. 
- **Authors**: Chentao Wu, Xubin He, Jie Li +1
- **PDF**: https://ieeexplore.ieee.org/document/7349600
- **Abstract**: With the rapid growth of data storage, the demand for high reliability becomes critical in large data centers where RAID-5 is widely used. However, the disk failure rate increases sharply after some usage, and thus concurrent disk failures are not rare, therefore RAID-5 is insufficient to provide high reliability. A solution is to convert an existing RAID-5 to a RAID-6 (a type of "RAID level migration") to tolerate more concurrent disk failures via erasure codes, but existing approaches involve complex conversion process and high transformation cost. To address these challenges, we propose a novel MDS code, called "Code 5-6", to combine a new dedicated parity column with the original RAID-5 layout. Code 5-6 not only accelerates online conversion from a RAID-5 to a RAID-6, but also demonstrates several optimal properties of MDS codes. Our mathematical analysis shows that, compared to existing MDS codes, Code 5-6 reduces new parities, decreases the total I/O operations, and speeds up the conversion process by up to 80%, 48.5%, and 3.38×, respectively.
