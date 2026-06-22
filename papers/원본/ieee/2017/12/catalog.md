# IEEE Xplore — 2017-12


## Design of Protograph-Based LDPC Codes with Limited Decoding Complexity

- **Status**: ✅
- **Reason**: 디코딩 복잡도·반복수 제한 하의 protograph LDPC 설계법(PEXIT+DE), 바이너리 LDPC 코드설계(E)로 이식 가능
- **ID**: ieee:8053758
- **Type**: journal
- **Published**: Dec. 2017
- **Authors**: Chengjun Tang, Ming Jiang, Chunming Zhao +1
- **PDF**: https://ieeexplore.ieee.org/document/8053758
- **Abstract**: In this letter, we present a design method to find good protograph-based low-density parity-check codes with the numbers of nonzero elements in the parity-check matrix and decoding iterations both strictly limited. We utilize the protograph-based extrinsic information transfer (PEXIT) analysis to evaluate the error performance and employ the differential evolution algorithm to devise a well-performed coding scheme. In particular, the number of iterations in the PEXIT analysis is set to a small value due to the limited iterations in the decoding process. Both numerical analyses and simulations verify that the resulting codes exhibit better performance than conventional code designs under the limitation of decoding complexity.

## Set Message-Passing Decoding Algorithms for Regular Non-Binary LDPC Codes

- **Status**: ❌
- **Reason**: 비이진(non-binary) LDPC용 set message-passing/EMS, 비이진 명시 제외
- **ID**: ieee:8017555
- **Type**: journal
- **Published**: Dec. 2017
- **Authors**: Qin Huang, Liyuan Song, Zulin Wang
- **PDF**: https://ieeexplore.ieee.org/document/8017555
- **Abstract**: In the check node (CN) update of non-binary message-passing algorithms, each element of reliability vectors takes the same computational complexity. However, our analysis indicates that various elements in the same vector have various correct probabilities, thus have different contributions to error performance. In order to match computational complexity with correct probability, all elements in a vector are partitioned into different sets. For the extended min-sum (EMS) decoding, various strategies are applied for sets according to their correct probability. For the trellis-based EMS decoding, it is interesting that set partition only involves fixed paths, thus it does not need to search over the whole trellis of a CN. Complexity analysis and simulation results show that the proposed algorithms efficiently decode non-binary low-density parity-check codes, including ultra-sparse ones.

## Analysis and Design of Raptor Codes Using a Multi-Edge Framework

- **Status**: ❌
- **Reason**: Raptor(fountain) 코드 설계·MET-DE 분석, fountain/erasure는 제외 대상이며 바이너리 LDPC BP로 이식할 신규 ECC 기법 없음
- **ID**: ieee:8030096
- **Type**: journal
- **Published**: Dec. 2017
- **Authors**: Sachini Jayasooriya, Mahyar Shirvanimoghaddam, Lawrence Ong +1
- **PDF**: https://ieeexplore.ieee.org/document/8030096
- **Abstract**: The focus of this paper is on the analysis and design of Raptor codes using a multi-edge framework. In this regard, we first represent Raptor codes as multi-edge type (MET) low-density parity-check codes. This MET representation gives a general framework to analyze and design Raptor codes over a binary input additive white Gaussian noise channel using MET density evolution (MET-DE). We then consider a joint decoding scheme based on the belief propagation (BP) decoding for Raptor codes in the multi-edge framework, and analyze the convergence behavior of the BP decoder using MET-DE. In joint decoding of Raptor codes, the component codes corresponding to the inner code and the precode are decoded in parallel and provide information to each other. We also derive an exact expression for the stability of Raptor codes with joint decoding. We then propose an efficient Raptor code design method using the multi-edge framework, where we simultaneously optimize the inner code and the precode. Through density evolution analysis we show that the designed Raptor codes using the multi-edge framework outperform the existing Raptor codes in literature in terms of realized rates.

## Offset and Normalized Min-Sum Algorithms for ATSC 3.0 LDPC Decoder

- **Status**: ✅
- **Reason**: OMSA/NMSA min-sum offset·scaling 최적화 및 error floor·채널 미스매치 분석 = 이식 가능 디코더(C)
- **ID**: ieee:7898488
- **Type**: journal
- **Published**: Dec. 2017
- **Authors**: Seho Myung, Sung-Ik Park, Kyung-Joong Kim +3
- **PDF**: https://ieeexplore.ieee.org/document/7898488
- **Abstract**: Offset min-sum algorithm (OMSA) and normalized min-sum algorithm (NMSA) are widely used in commercial LDPC decoders due to low complexity and reasonable performance. In this paper, we provide optimized offset and scaling values for those LDPC decoders based on Advanced Television Systems Committee (ATSC) 3.0 LDPC codes. Furthermore, according to extensive computer simulations, it is shown that the performance of the OMSA and NMSA with the obtained values is close to that of sum-product algorithm, even though the NMSA-based decoder may show a serious error floor due to a channel mismatch effect. Consequently, we recommend that the ATSC 3.0 transmitters use a concatenation of BCH outer code and LDPC inner code as channel coding, considering the use of NMSA for LDPC decoder in ATSC 3.0 receivers.

## Continuous Transmission of Spatially Coupled LDPC Code Chains

- **Status**: ✅
- **Reason**: SC-LDPC continuous chain 전송으로 유한길이 성능 개선, protograph 앙상블 코드설계(E)
- **ID**: ieee:8003438
- **Type**: journal
- **Published**: Dec. 2017
- **Authors**: Pablo M. Olmos, David G. M. Mitchell, Dmitri Truhachev +1
- **PDF**: https://ieeexplore.ieee.org/document/8003438
- **Abstract**: We propose a novel encoding/transmission scheme called continuous chain (CC) transmission that is able to improve the finite-length performance of a system using spatially coupled low-density parity-check (SC-LDPC) codes. In CC transmission, instead of transmitting a sequence of independent code words from a terminated SC-LDPC code chain, we connect multiple chains in a layered format, where encoding, transmission, and decoding are performed in a continuous fashion. The connections between chains are created at specific points, chosen to improve the finite-length performance of the code structure under iterative decoding. We describe the design of CC schemes for different SC-LDPC code ensembles constructed from protographs: a (J,K) -regular SC-LDPC code chain, a spatially coupled repeat-accumulate (SC-RA) code, and a spatially coupled accumulate-repeat-jagged-accumulate (SC-ARJA) code. In all cases, significant performance improvements are reported and it is shown that using CC transmission only requires a small increase in decoding complexity and decoding delay with respect to a system employing a single SC-LDPC code chain for transmission.

## Design of a Capacity-Approaching Chaos-Based Multiaccess Transmission System

- **Status**: ✅
- **Reason**: 수정 EXIT 분석 기반 신규 protograph 코드 설계 = 바이너리 코드설계(E)
- **ID**: ieee:7968491
- **Type**: journal
- **Published**: Dec. 2017
- **Authors**: Pingping Chen, Yi Fang, Kaixiong Su +1
- **PDF**: https://ieeexplore.ieee.org/document/7968491
- **Abstract**: As an enhanced version of Walsh-code-based multiaccess differential chaos shift keying (DCSK-WC), the differentially DCSK-WC (DDCSK-WC) benefits from better error performance and stronger robustness against inter-symbol interference in multipath fading channels. In this paper, the Bahl-Cocke-Jelinek-Raviv (BCJR) decoding algorithm is applied in the detection of DDCSK-WC to form DDCSK-WC-BCJR. Theoretical analyses and simulation results demonstrate that the BCJR detector achieves a significant performance gain with respect to the conventional generalized-maximum-likelihood detector, while retaining the hardware complexity almost unchanged. To further improve the performance, protograph-based low-density-parity-check channel codes are incorporated into the DDCSK-WC-BCJR system so as to construct a serial concatenated coding scheme. However, the capacity-approaching protograph code in additive white Gaussian noise (AWGN) channels performs poorly in the DDCSK-WC-BCJR system over multipath fading channels. To tackle this problem, a new protograph code is designed with the help of a modified extrinsic information transfer analysis. The proposed code has decoding thresholds gap within 1.0 dB way from to the system capacity limits. Besides, the performance superiority of the protograph-coded DDCSK-WC-BCJR architecture is illustrated over a practical UWB channel. More importantly, the proposed scheme does not require channel state information as in uncoded-DCSK schemes, which makes it extremely promising for low-cost and low-complexity wireless communication applications.

## Capacity-Achieving Rate-Compatible Polar Codes

- **Status**: ❌
- **Reason**: rate-compatible polar 코드 구성/순차디코더, polar 전용 기법으로 바이너리 LDPC BP 이식성 없음
- **ID**: ieee:8049513
- **Type**: journal
- **Published**: Dec. 2017
- **Authors**: Song-Nam Hong, Dennis Hui, Ivana Marić
- **PDF**: https://ieeexplore.ieee.org/document/8049513
- **Abstract**: A method of constructing rate-compatible polar codes that are capacity achieving at multiple code rates with low-complexity sequential decoders is presented. The underlying idea of the construction exploits certain common characteristics of polar codes that are optimized for a sequence of successively degraded channels. The proposed code consists of parallel concatenation of multiple polar codes with information-bit divider at the input of each polar encoder. Thus, it is referred to as parallel concatenated polar (PCP) codes. A lower-rate PCP code is simply constructed by adding more constituent polar codes, which enables incremental retransmissions at different rates in order to adapt to channel conditions. Due to the length limitation of polar codes, the PCP code can only support a restricted set of rates that is characterized by the size of the kernel when conventional polar codes are used. To overcome this limitation, punctured polar codes, which provide more flexibility on blocklength by controlling a puncturing fraction, are considered as constituent codes. The existence of capacity-achieving punctured polar codes for any given puncturing fraction is proven. Using such punctured polar codes as constituent codes, it is shown that the proposed PCP code is capacity achieving for an arbitrary sequence of rates and for any class of degraded channels.

## Iterative Low Complexity Algorithm for LDPC Systems in the Presence of Phase Noise

- **Status**: ✅
- **Reason**: phase noise 하 LDPC 그래프 기반 반복 수신기, 복소 가우시안 메시지 구성 = BP 메시지패싱 변형(C), 애매하나 살림
- **ID**: ieee:8014470
- **Type**: journal
- **Published**: Dec. 2017
- **Authors**: Seare Haile Rezenom, Fambirai Takawira
- **PDF**: https://ieeexplore.ieee.org/document/8014470
- **Abstract**: In this letter, we propose a low-complexity graph-based iterative receiver for low-density parity-check (LDPC) coded systems in the presence of strong phase noise. The proposed receiver exploits the inherent circular characteristics of phase noise and uses complex Gaussian density functions to construct the messages. We show the proposed method achieves similar bit-error rate performance as the existing lowest complexity algorithm, and has lower complexity for higher modulation.

## On Orthogonal and Superimposed Pilot Schemes in Massive MIMO NOMA Systems

- **Status**: ❌
- **Reason**: Massive MIMO NOMA 파일럿/채널추정, LDPC는 베이스라인일 뿐 이식할 ECC 기법 없음
- **ID**: ieee:7974727
- **Type**: journal
- **Published**: Dec. 2017
- **Authors**: Junjie Ma, Chulong Liang, Chongbin Xu +1
- **PDF**: https://ieeexplore.ieee.org/document/7974727
- **Abstract**: This paper is concerned with pilot transmission schemes in a large antenna system with non-orthogonal multiple-access (NOMA). We investigate two pilot structures-orthogonal pilot (OP) and superimposed pilot (SP). In OP, pilots occupy dedicated time (or frequency) slots, while in SP, pilots are superimposed with data. We study an iterative data-aided channel estimation (IDACE) receiver, where partially decoded data are used to refine channel estimation. We analyze the achievable rates for systems with IDACE receivers for both OP and SP. We show that the optimal portion of pilot power tends to zero for SP with Gaussian signaling. This result is consistent with existing findings obtained via the replica method in statistical physics. The latter involves multiple codes, which is convenient for theoretical analysis but difficult to implement. As a comparison, IDACE is potentially implementable in practice. We demonstrate that, with code optimization, SP can outperform OP in a high mobility environment with a large number of users. We provide numerical examples to verify our analysis.

## Constellation Design for Bit-Interleaved Coded Modulation (BICM) Systems in Advanced Broadcast Standards

- **Status**: ❌
- **Reason**: BICM 콘스텔레이션 기하 최적화(PSO), LDPC 디코더·HW·코드설계 이식 기법 없음
- **ID**: ieee:7883869
- **Type**: journal
- **Published**: Dec. 2017
- **Authors**: Jon Barrueco, Jon Montalban, Cristina Regueiro +5
- **PDF**: https://ieeexplore.ieee.org/document/7883869
- **Abstract**: This paper presents a generic methodology to optimize constellations based on their geometrical shaping for bit-interleaved coded modulation (BICM) systems. While the method can be applicable to any wireless standard design it has been tailored to two delivery scenarios typical of broadcast systems: 1) robust multimedia delivery and 2) UHDTV quality bitrate services. The design process is based on maximizing the BICM channel capacity for a given power constraint. The major contribution of this paper is a low complexity optimization algorithm for the design of optimal constellation schemes. The proposal consists of a set of initial conditions for a particle swarm optimization algorithm, and afterward, a customized post processing procedure for further improving the constellation alphabet. According to the broadcast application cases, the sizes of the constellations proposed range from 16 to 4096 symbols. The BICM channel capacities and performance of the designed constellations are compared to conventional quadrature amplitude modulation constellations for different application scenarios. The results show a significant improvement in terms of system performance and BICM channel capacities under additive white Gaussian noise and Rayleigh independently and identically distributed channel conditions.

## Advanced Baseband Processing Algorithms, Circuits, and Implementations for 5G Communication

- **Status**: ❌
- **Reason**: 5G 베이스밴드 회로/알고리즘 개관 서베이, 구체적 신규 LDPC 기여 없음
- **ID**: ieee:8014436
- **Type**: journal
- **Published**: Dec. 2017
- **Authors**: Chuan Zhang, Yuan-Hao Huang, Farhana Sheikh +1
- **PDF**: https://ieeexplore.ieee.org/document/8014436
- **Abstract**: The rapid emergence of 5G communications technology and standardization has seen an accelerated transfer of theoretical concepts to advanced development and implementation. Not only are 5G baseband signal processing algorithms becoming more important, but also the co-design and implementation of corresponding circuits, architectures, and platforms are becoming necessary due to rapid standardization of 5G communications. This timely overview paper introduces circuits and systems (CAS) for key enabling technologies for the new 5G era: massive MIMO, mmWave baseband systems, NOMA schemes, advanced channel coding, and so on. The state-of-the-art research progress in these areas is summarized for interested readers to initiate discussion on limitations of existing solutions and open research problems that are looking for innovative solutions, especially in the CAS area. We hope this paper can bridge the gap between the theoretical investigation and application implementation for 5G communications.

## Constructions of LDPCs From Elliptic Curves Over Finite Fields

- **Status**: ✅
- **Reason**: 유한체 타원곡선 기반 신규 LDPC 구성법 제안, 바이너리 LDPC 코드설계(E)로 이식 가능 — Phase 3에서 바이너리/비이진 여부 확인 필요
- **ID**: ieee:8031075
- **Type**: journal
- **Published**: Dec. 2017
- **Authors**: Yannick Saouter
- **PDF**: https://ieeexplore.ieee.org/document/8031075
- **Abstract**: In this letter, a new framework for the construction of low density parity check codes is exposed. Parameters of the new codes are estimated, performance simulations are reported and compared with some classical constructions.

## Dedicated protection with signal overlap in elastic optical networks

- **Status**: ❌
- **Reason**: 탄성광망 경로보호·스펙트럼할당(ILP), LDPC/ECC와 무관
- **ID**: ieee:8204498
- **Type**: journal
- **Published**: Dec. 2017
- **Authors**: F. Cugini, M. Ruiz, T. Foggi +3
- **PDF**: https://ieeexplore.ieee.org/document/8204498
- **Abstract**: In optical dedicated path protection (1+1), the same optical signal is transmitted along both working and backup paths. Thus, in 1+1, the transmission parameters need to be configured according to the most impaired path, e.g., the backup one. This implies that the working signal is typically served with higher than necessary quality of transmission and occupies larger than necessary spectrum resources, leading to inefficient network resource utilization. In this study, we propose to apply the recently introduced signal overlap technique to improve network efficiency of optical dedicated path protection. The signal overlap technique enables uncorrelated optical signals to be superimposed along the same spectrum resources. It relies on a cancellation detection strategy also exploited in wireless communications and recently applied on coherent optical receivers. In particular, this study summarizes the key aspect and transmission performance of the overlap technique and discusses its implementation complexity. Then, two signal overlap schemes, namely, working signal overlap and working and backup signal overlap are introduced for effective optical dedicated path protection. An integer linear programming (ILP) formulation based on the routing, modulation, and spectrum allocation problem and an efficient heuristic are then presented to effectively assess the performance of the proposed overlap-based 1+1 protection strategy under various topologies and traffic profiles. In the considered simulative scenarios (e.g., network diameters well below a thousand kilometers), results show that the more efficient working and backup signal overlap scheme significantly improves the accepted load of dedicated protection requests.

## A Novel SCMA System for Coexistence of Active Users and Inactive Users

- **Status**: ❌
- **Reason**: SCMA grant-free 다중접속 수신기/코드워드 설계, NAND LDPC ECC로 떼어낼 디코더·HW·코드설계 기법 없음
- **ID**: ieee:8025797
- **Type**: journal
- **Published**: Dec. 2017
- **Authors**: Joonki Kim, Kwonjong Lee, Jintae Kim +3
- **PDF**: https://ieeexplore.ieee.org/document/8025797
- **Abstract**: This letter proposes a new sparse code multiple access (SCMA) system for handling the coexistence of active user equipments (UEs) and inactive UEs, which share the same frequency/time resources for an uplink grant-free scenario. SCMA systems use a message passing algorithm, which considers all UEs to be active UEs. Therefore, inactive UEs cause significant decoding problem in SCMA systems. In order to solve the coexistence problem, we propose code words and a novel SCMA receiver which can distinguish the signal of active/inactive UEs. The numerical results show that the proposed SCMA receiver achieves a remarkable enhancement in false alarm probability, miss detection probability, and bit-error rate.

## A Reused-Public-Path Successive Cancellation List Decoding for Polar Codes With CRC

- **Status**: ❌
- **Reason**: Polar SCL+CRC 디코더 복잡도 절감, polar 전용 successive-cancellation으로 LDPC BP에 이식 불가
- **ID**: ieee:8049511
- **Type**: journal
- **Published**: Dec. 2017
- **Authors**: Shibao Li, Lijin Lu, Yunqiang Deng +2
- **PDF**: https://ieeexplore.ieee.org/document/8049511
- **Abstract**: Since the decoding of polar codes goes wrong in sometime, several decoding methods have been proposed to overcome this issue. Unfortunately, the several schemes are still suffering from high decoding complexity. To this end, we propose a reused-public-path successive-cancellation list decoder, which can re-do the decoding from E-th level when the current decoding process fails. In addition, a reused public-path scheme is proposed. By properly designing, simulation results in binary-input additive white gaussian noise channel show that this decoding approach provides significant computational complexity reduction in the moderate and high signal-to-noise ratio regime without performance loss.

## A Differential Chaotic Bit-Interleaved Coded Modulation System Over Multipath Rayleigh Channels

- **Status**: ✅
- **Reason**: protograph LDPC 코드 설계 P-EXIT 분석 및 디코딩 임계값 최적화 = 코드설계(E), 애매하나 살림
- **ID**: ieee:7956256
- **Type**: journal
- **Published**: Dec. 2017
- **Authors**: Jia Zhan, Lin Wang, Marcos Katz +1
- **PDF**: https://ieeexplore.ieee.org/document/7956256
- **Abstract**: In this paper, a novel differential chaotic bit-interleaved coded modulation (DC-BICM) system is proposed for band-limited transmission. This system combines protograph-based low density parity check codes with constellation-based M-ary differential chaos shift keying (DCSK) modulation by one bitwise interleaving. Bit error rate simulation results show that the system has higher coding gain compared with the constellation-based M-ary DCSK modulation system with the same spectral efficiency over multipath Rayleigh fading channels. At the same time, several simulations and P-EXIT analysis are used to analyze the performance of the proposed system. It is found that there is a lot of room for optimization of the system by comparing decoding thresholds and simulation results. Moreover, the system with only partial channel state information has better performance and lower complexity compared with the traditional bit-interleaved coded modulation (BICM) directsequence-spread-spectrum system. As a result, the DC-BICM system is a good candidate for band-limited transmission.

## Efficient Decoding of LDM Core Layer at Fixed Receivers in ATSC 3.0

- **Status**: ❌
- **Reason**: ATSC 3.0 LDM SIC용 시스템 특이적 re-encoding 모듈, 이식 가능 디코더·코드 기법 없음
- **ID**: ieee:8000374
- **Type**: journal
- **Published**: Dec. 2017
- **Authors**: Seho Myung, Kyung-Joong Kim, Jin Lee +2
- **PDF**: https://ieeexplore.ieee.org/document/8000374
- **Abstract**: In order to decode an enhanced layer (EL) signal for a layered-division multiplexing (LDM) system at fixed receivers in ATSC 3.0, low-density parity-check (LDPC)/BCH decoding and successive interference cancellation should be performed to eliminate the core layer (CL) signal. For a high signal-to-noise ratio environment and sufficient low injection level of the EL signal, the CL bit-interleaved coded modulation decoder can easily achieve quasi error free for the whole LDPC codeword. However, for high injection levels, there may be still many erroneous bits in the parity part even after LDPC/BCH decoding since the ATSC 3.0 LDPC codes have the characteristic of unequal error protection due to the unequal weight distributions in their parity-check matrices. Therefore, ATSC 3.0 receivers should include re-encoding module for CL LDPC codes to completely recover the CL signal for LDM system. In this paper, we propose an efficient method to reconstruct CL signal in ATSC 3.0 LDM systems, which can be realized by a modified re-encoding after LDPC decoding of the CL signal. It significantly reduces the computational complexity and worst case latency without any loss of coding performance.

## A Novel Digital Broadcasting System Based on Polar Codes in Shortwave

- **Status**: ❌
- **Reason**: polar 코드 기반 방송시스템 — 비-LDPC, 이식 가능 BP 기법 없음
- **ID**: ieee:8283313
- **Type**: conference
- **Published**: 9-10 Dec. 
- **Authors**: Haiyun Liu, Hang Yin, Hanyu Xie
- **PDF**: https://ieeexplore.ieee.org/document/8283313
- **Abstract**: In this paper, on the basis of study on existing DRM system, we make a comparison between rate compatible punctured convolutional codes in DRM system and LDPC code in standard 802.16, then we propose a novel digital broadband broadcasting system based on polar codes in shortwave. Polar codes are used in the novel system to replace multilevel coding scheme in the original DRM system. Simulation shows that polar codes outperform significantly in error correction compared with the other channel coding schemes, and polar codes are capable to effectively enhance the performance of DRM system. In addition, the novel system has a simple process in transmitting terminal and a low complexity, which make it an effective scheme in the next generation of broadband system in shortwave.

## Efficient FPGA implementation of probabilistic gallager B LDPC decoder

- **Status**: ✅
- **Reason**: Probabilistic Gallager B 하드결정 메시지패싱 LDPC 디코더의 FPGA 구현, trapping set 탈출 기법 — 이식 가능 디코더(C)+HW(D)
- **ID**: ieee:8292048
- **Type**: conference
- **Published**: 5-8 Dec. 2
- **Authors**: Fakhreddine Ghaffari, Burak Unal, Ali Akoglu +3
- **PDF**: https://ieeexplore.ieee.org/document/8292048
- **Abstract**: This paper presents the performance evaluation of the Probabilistic Gallager B (PGaB), a hard decision message passing Low Density Parity Check (LDPC) Decoder, with respect to the soft decision based decoders MinSum (MS) and Offset-MinSum (OMS). PGaB algorithm relies on introducing deliberate and controlled randomness to some of the exchanged messages of the GaB decoder such that it is able to escape from local minima associated with dominant trapping sets. We show that PGaB delivers higher decoding throughput than soft decision based decoders MS and OMS while using much fewer amount of Field Programmable Gate Array (FPGA) resources. Our Monte-Carlo simulation results show that the decoding performance of the PGaB on Binary Symmetric Channel (BSC) is far better than the deterministic GaB and very close to MS and OMS performances especially in error floor region.

## The implementation of a successive cancellation polar decoder on Xilinx System Generator

- **Status**: ❌
- **Reason**: 폴라 SC 디코더 FPGA 구현, 비-LDPC이고 폴라 전용 구조라 LDPC HW 이식 기여 없음
- **ID**: ieee:8291995
- **Type**: conference
- **Published**: 5-8 Dec. 2
- **Authors**: A. Çağrı Arlı, Ayşe Çolak, Orhan Gazi
- **PDF**: https://ieeexplore.ieee.org/document/8291995
- **Abstract**: Polar coding is the first kind of the capacity achieving codes which are defined for binary-input discrete memoryless channels initially. Parallel processing property of the FPGA allows to decode faster with a margin of complexity. Xilinx System Generator as a practical tool to construct decoding designs in shorter time is a fact. In this study, FPGA implementation of decoding polar codes through Xilinx System Generator is shown.

## An Upper Bounding Technique on the Error Floor Performance of LDPC Codes

- **Status**: ✅
- **Reason**: LDPC error floor 상한 기법 — error floor 코드설계(E) 관련, 애매하나 살림
- **ID**: ieee:8254151
- **Type**: conference
- **Published**: 4-8 Dec. 2
- **Authors**: Santhosh Kumar, Ravi H. Motwani
- **PDF**: https://ieeexplore.ieee.org/document/8254151
- **Abstract**: Low-density parity-check (LDPC) codes have higher coding gains compared to algebraic codes in several configurations. However, unlike algebraic codes whose performance can be easily determined generally, the block error rate performance of an LDPC code needs to be obtained by simulations. While there are analytical methods for some structured LDPC codes that predict this performance in the low error rate regime, these provide little insight into the error floor of other (less structured) LDPC codes. In this article, we present a simple method to upper bound the error floor of LDPC codes based on a certain monotonicity assumption on the decoder. This upper bound is general enough so that under the monotonicity assumption it is valid for any error-correcting code. This upper bounding technique is useful when projecting very low block error rates (such as below 1E-14) for LDPC codes and there is no knowledge of the trapping sets.

## Enhanced IDMA with Rate-Compatible Raptor-Like Quasi-Cyclic LDPC Code for 5G

- **Status**: ❌
- **Reason**: 5G IDMA용 RL-QC-LDPC 설계, EXIT 기반 표준 rate-compatible 구성·무선 다중접속 특이적으로 NAND 이식 신규성 없음
- **ID**: ieee:8269093
- **Type**: conference
- **Published**: 4-8 Dec. 2
- **Authors**: Yushu Zhang, Kewu Peng, Jian Song
- **PDF**: https://ieeexplore.ieee.org/document/8269093
- **Abstract**: Due to excellent performance and low implementation complexity, raptor-like quasi-cyclic low density parity check (RL-QC-LDPC) codes have been recently selected as the coding scheme of data channel for enhanced mobile broadband applications in the 5th generation (5G) cellular networks. However, for non-orthogonal multiple access (NOMA) schemes with turbo joint decoding, like interleave-division multiple access (IDMA), RL-QC-LDPC codes designed for single-user transmission face the problem of performance degradation. In this paper, the RL-QC- LDPC codes are designed for enhanced IDMA, where the conventional symbol-by-symbol elementary signal estimator is replaced by a symbol-by-symbol maximum a posteriori probability multi-user detector. Moreover, as recommended in 3GPP New Radio study item of channel coding, rate-compatibility is considered for enhanced IDMA, and rate-compatible RL-QC-LDPC code family is designed with the tool of extrinsic information transfer (EXIT) chart. According to EXIT analysis and simulation results, enhanced IDMA with the designed rate-compatible RL- QC-LDPC code family is capable of supporting multiple rates and different numbers of users with near-capacity performance.

## Regular and Irregular LDPC Code Design for Bandwidth Efficient BICM Schemes

- **Status**: ✅
- **Reason**: BICM용 LDPC 코드 설계, EXIT+미분진화+수정 PEG로 변수/체크노드 최적화 — 이식 가능 코드설계(E)
- **ID**: ieee:8254234
- **Type**: conference
- **Published**: 4-8 Dec. 2
- **Authors**: Junyi Du, Liang Zhou, Zhe Zhang +2
- **PDF**: https://ieeexplore.ieee.org/document/8254234
- **Abstract**: We consider low-density parity-check (LDPC) code design by considering the unequal error protection property in high order modulated bit-interleaved coded modulation (BICM) schemes. The existing work mainly considered the effect of variable node edge assignments on the decoding performance. In this paper, we consider both variable node and check node edge assignments to further optimize the LDPC codes for BICM schemes. To achieve this, we derive new extrinsic information transfer (EXIT) functions for both regular and irregular LDPC code ensembles. Then we employ differential evolution to optimize the code ensembles in terms of the lowest decoding threshold. Finally, we propose a modified progressive edge growth algorithm to design regular and irregular LDPC codes based on the optimized code ensembles. The numerical results show that our designed LDPC codes have better bit error rate performance compared to the codes designed in the existing work.

## Ultra-Sparse Non-Binary LDPC Codes for Probabilistic Amplitude Shaping

- **Status**: ❌
- **Reason**: GF(64)/GF(256) 비이진 LDPC + PAS — 비이진 LDPC는 제외 대상
- **ID**: ieee:8254155
- **Type**: conference
- **Published**: 4-8 Dec. 2
- **Authors**: Fabian Steiner, Gianluigi Liva, Georg Boecherer
- **PDF**: https://ieeexplore.ieee.org/document/8254155
- **Abstract**: This work shows how non-binary low-density parity-check codes over GF(2^p) can be combined with probabilistic amplitude shaping (PAS) (Böcherer, et al., 2015), which combines forward-error correction with non-uniform signaling for power-efficient communication. Ultra-sparse low-density parity-check codes over GF(64) and GF(256) gain 0.6 dB in power efficiency over state-of-the-art binary LDPC codes at a spectral efficiency of 1.5 bits per channel use and a blocklength of 576 bits. The simulation results are compared to finite length coding bounds and complemented by density evolution analysis.

## LDPC Decoder with Embedded Coding on Unreliable Memories

- **Status**: ✅
- **Reason**: 신뢰불가 메모리상 LDPC 디코더 메시지 보호(sign bit), NAND 메모리 신뢰성·LDPC HW 직접 관련(D)
- **ID**: ieee:8255010
- **Type**: conference
- **Published**: 4-8 Dec. 2
- **Authors**: Guangjun Ge, Liuguo Yin, Qin Huang
- **PDF**: https://ieeexplore.ieee.org/document/8255010
- **Abstract**: Unreliable message storage severely degrades the performance of LDPC decoders. This paper discusses the various impacts of bit errors of finite-precision messages on LDPC decoders. Discrete density evolution indicates that the sign bits of finite-precision messages have the most influence on the decoding threshold. As a result, this paper proposes to protect the sign bits of messages by Hamming product codes. Simulation results show that the proposed scheme only has a degradation of 0.1 dB for the LDPC decoder with a storage error ratio of 0.001, which outperforms the traditional triple modular redundancy scheme.

## A New LDPC Coded Scheme for Two-User Multiple-Access Channels Aided with Physical-Layer Network Coding

- **Status**: ❌
- **Reason**: PNC 보조 다중접속 LDPC 부호화 방식, 표준 BP 그대로 사용·무선 응용 특이적으로 떼어낼 새 기법 없음
- **ID**: ieee:8269090
- **Type**: conference
- **Published**: 4-8 Dec. 2
- **Authors**: Junyi Du, Liang Zhou, Xuan He +1
- **PDF**: https://ieeexplore.ieee.org/document/8269090
- **Abstract**: In this paper, we aim to design a new low-density parity-check (LDPC) coded scheme for two-user Gaussian multiple access channel aided with physical-layer network coding (PNC). The two users have equal transmission rate and employ the same LDPC code. We allocate the two users with unequal modulation power levels. Without loss of generality, we modulate User A's codeword and User B's codeword by the higher and lower power level signals, respectively. Since the PNC coded bits are the exclusive-OR (XOR) of User A's codeword and User B's codeword, the PNC coded bits are also a codeword of the employed LDPC code. At the receiver, the decoder estimates User A's codeword and the PNC codeword with conventional message passing algorithm separately, rather than decoding User A's and User B's codewords directly with the joint decoding algorithm. Then User B's codeword is estimated by the XOR of the decoding results of User A's codeword and the PNC codeword. We optimize the power ratio between the two power levels to minimize the required SNR for a scheme with a given rate. Numerical result shows that our proposed scheme has a better bit error rate performance and a lower decoding complexity, compared to the state-of-the-art scheme.

## A General Framework and Optimization for Spatially-Coupled Serially Concatenated Systems

- **Status**: ✅
- **Reason**: Spatially-coupled concatenated 시스템 + SC-protograph EXIT 분석 코드설계 — SC-LDPC 구성(E) 이식 가능, 애매하나 살림
- **ID**: ieee:8254239
- **Type**: conference
- **Published**: 4-8 Dec. 2
- **Authors**: Tarik Benaddi, Charly Poulliat, Romain Tajan
- **PDF**: https://ieeexplore.ieee.org/document/8254239
- **Abstract**: In this paper, we provide a general framework for spatially-coupled concatenated systems. We explicit the analogy with spatially-coupled protographs and provide an adapted EXIT chart analysis. By proposing a continuous-valued coupling matrix, we propose a code design procedure for faster convergence. When considering general bit- interleaved coded-modulation scheme, we also conjecture that the spatially-coupled scheme of general detectors saturates to a value very close (lower bound) to the threshold given by the Area theorem.

## Randomized Turbo Codes for the Wiretap Channel

- **Status**: ❌
- **Reason**: Wiretap channel용 randomized turbo code — 보안+turbo, 바이너리 LDPC BP로 이식할 기법 없음
- **ID**: ieee:8254154
- **Type**: conference
- **Published**: 4-8 Dec. 2
- **Authors**: Alireza Nooraiepour, Tolga M. Duman
- **PDF**: https://ieeexplore.ieee.org/document/8254154
- **Abstract**: We study application of parallel and serially concatenated convolutional codes known as turbo codes to the randomized encoding scheme introduced by Wyner for physical layer security. For this purpose, we first study how randomized convolutional codes can be constructed. Then, we use them as building blocks for developing randomized turbo codes. We also develop iterative low-complexity decoders corresponding to the randomized schemes introduced and evaluate the code performance. We demonstrate via several examples that the newly designed schemes can outperform other existing coding methods in the literature (e.g., punctured low density parity check (LDPC) and scrambled BCH codes) in terms of the resulting security gap.

## Post-Processing Methods for Improving Coding Gain in Belief Propagation Decoding of Polar Codes

- **Status**: ✅
- **Reason**: polar BP 후처리(perturb/freeze, 안정비트 강화) 기법이 부호 비의존적 메시지패싱 개선으로 LDPC BP에 이식 가능, 예외 포함(C)
- **ID**: ieee:8254247
- **Type**: conference
- **Published**: 4-8 Dec. 2
- **Authors**: Shuanghong Sun, Sung-Gun Cho, Zhengya Zhang
- **PDF**: https://ieeexplore.ieee.org/document/8254247
- **Abstract**: Belief propagation (BP) is a high-throughput, low- latency decoding algorithm for polar codes, but the error-correcting performance is known to be inferior than successive cancellation (SC) decoding. To improve the error-correcting performance of BP decoding, we design post- processing methods targeting false converged errors, oscillation errors, and unconverged errors that determine the performance of BP decoding. False convergence can be resolved by perturbing, or gradually freezing the information bits, followed by error cleanup using BP. Oscillations can be resolved by enhancing the stable bits and perturbing the unstable bits, followed by error cleanup using BP. Unconverged errors can be resolved by enhancing the reliably stable bits and weakening the unstable bits. Results show that the error rates of BP decoding can be improved by an order of magnitude or more, allowing it to overtake SC in error rate and coding gain. Post-processing can be implemented very efficiently, costing less than 4.3% overhead in silicon area, and it does not affect the throughput or latency of BP decoding.

## Partitioned List Decoding of Polar Codes: Analysis and Improvement of Finite Length Performance

- **Status**: ❌
- **Reason**: polar SCL 리스트 디코딩·CRC 할당, polar 전용 기법으로 LDPC BP에 이식 불가
- **ID**: ieee:8254940
- **Type**: conference
- **Published**: 4-8 Dec. 2
- **Authors**: Seyyed Ali Hashemi, Marco Mondelli, S. Hamed Hassani +2
- **PDF**: https://ieeexplore.ieee.org/document/8254940
- **Abstract**: Polar codes represent one of the major recent breakthroughs in coding theory and, because of their attractive features, they have been selected for the incoming 5G standard. As such, a lot of attention has been devoted to the development of decoding algorithms with good error performance and efficient hardware implementation. One of the leading candidates in this regard is represented by successive-cancellation list (SCL) decoding. However, its hardware implementation requires a large amount of memory. Recently, a partitioned SCL (PSCL) decoder has been proposed to significantly reduce the memory consumption [1]. In this paper, we examine the paradigm of PSCL decoding from both theoretical and practical standpoints: (i) by changing the construction of the code, we are able to improve the performance at no additional computational, latency or memory cost, (ii) we present an optimal scheme to allocate cyclic redundancy checks (CRCs), and (iii) we provide an upper bound on the list size that allows MAP performance.

## Distributing CRC Bits to Aid Polar Decoding

- **Status**: ❌
- **Reason**: polar 디코딩용 CRC 분산 기법, polar 전용으로 LDPC 이식 불가
- **ID**: ieee:8269177
- **Type**: conference
- **Published**: 4-8 Dec. 2
- **Authors**: Jie Chen, Yu Chen, Keeth Jayasinghe +2
- **PDF**: https://ieeexplore.ieee.org/document/8269177
- **Abstract**: One recent and important advancement in information and coding theory is polar code, which is selected as the coding scheme for 5G eMBB control channels. In this paper, we propose a variant of polar codes that provides significant coding gain in the regime of short blocks and enables early termination of decoding processes. The overall scheme depends on distributing CRC bits in the whole information block, and a single interleaving/deinterleaving pattern can be defined to implement CRC distribution. The design can reduce the decoding latency and energy consumption of hardware, which is crucial for mobile applications like 5G.

## Sparse Vector Recovery: Bernoulli-Gaussian Message Passing

- **Status**: ❌
- **Reason**: 희소벡터복원용 Bernoulli-Gaussian MP(압축센싱), 채널 ECC 디코더가 아니라 떼어낼 LDPC 기법 없음
- **ID**: ieee:8254836
- **Type**: conference
- **Published**: 4-8 Dec. 2
- **Authors**: Lei Liu, Chongwen Huang, Yuhao Chi +3
- **PDF**: https://ieeexplore.ieee.org/document/8254836
- **Abstract**: Low-cost message passing (MP) algorithm has been recognized as a promising technique for sparse vector recovery. However, the existing MP algorithms either focus on mean square error (MSE) of the value recovery while ignoring the sparsity requirement, or support error rate (SER) of the sparse support (non-zero position) recovery while ignoring its value. A novel low-complexity Bernoulli-Gaussian MP (BGMP) is proposed to perform the value recovery as well as the support recovery. Particularly, in the proposed BGMP, support-related Bernoulli messages and value- related Gaussian messages are jointly processed and assist each other. In addition, a strict lower bound is developed for the MSE of BGMP via the genie-aided minimum mean-square-error (GA-MMSE) method. The GA-MMSE lower bound is shown to be tight in high signal-to-noise ratio. Numerical results are provided to verify the advantage of BGMP in terms of final MSE, SER and convergence speed.

## Message Passing in C-RAN: Joint User Activity and Signal Detection

- **Status**: ❌
- **Reason**: C-RAN 신호검출 Bernoulli-Gaussian message passing — 무선 활동/신호 검출용, ECC 채널코딩 아님
- **ID**: ieee:8254230
- **Type**: conference
- **Published**: 4-8 Dec. 2
- **Authors**: Yuhao Chi, Lei Liu, Guanghui Song +3
- **PDF**: https://ieeexplore.ieee.org/document/8254230
- **Abstract**: In cloud radio access network (C-RAN), remote radio heads (RRHs) and users are uniformly distributed in a large area such that the channel matrix can be considered as sparse. Based on this phenomenon, RRHs only need to detect the relatively strong signals from nearby users and ignore the weak signals from far users, which is helpful to develop low-complexity detection algorithms without causing much performance loss. However, before detection, RRHs require to obtain the realtime user activity information by the dynamic grant procedure, which causes the enormous latency. To address this issue, in this paper, we consider a grant-free C-RAN system and propose a low- complexity Bernoulli-Gaussian message passing (BGMP) algorithm based on the sparsified channel, which jointly detects the user activity and signal. Since active users are assumed to transmit Gaussian signals at any time, the user activity can be regarded as a Bernoulli variable and the signals from all users obey a Bernoulli-Gaussian distribution. In the BGMP, the detection functions for signals are designed with respect to the Bernoulli-Gaussian variable. Numerical results demonstrate the robustness and effectivity of the BGMP. That is, for different sparsified channels, the BGMP can approach the mean-square error (MSE) of the genie-aided sparse minimum mean-square error (GA- SMMSE) which exactly knows the user activity information. Meanwhile, the fast convergence and strong recovery capability for user activity of the BGMP are also verified.

## Constructions of Fractional Repetition Codes with Flexible Per-Node Storage and Repetition Degree

- **Status**: ❌
- **Reason**: 분산저장용 fractional repetition 코드 구성, LDPC ECC 아님(Tanner graph girth 언급은 부수적)
- **ID**: ieee:8255008
- **Type**: conference
- **Published**: 4-8 Dec. 2
- **Authors**: Yi-Sheng Su
- **PDF**: https://ieeexplore.ieee.org/document/8255008
- **Abstract**: This paper considers the construction of fractional repetition (FR) codes with flexible storage capacity and repair for distributed storage systems (DSSs). FR codes are the key to constructing a class of distributed storage codes with exact repair by transfer, where, upon failure, a failed storage node is exactly regenerated by simply downloading symbols from the surviving nodes. A major drawback of existing FR codes is that their parameters are not flexible enough to adapt to system changes in DSSs. To address this issue, this paper proposes two constructions of FR codes, called adaptive-and-resolvable FR codes, based on circulant permutation matrices and affine permutation matrices. In the proposed FR codes, the storage capacity per node and repetition degree of the symbols can be varied simultaneously in a simple manner. Some results on the exact file size that can be supported by the proposed FR codes are provided, based on the girth of the corresponding Tanner graph. Furthermore, the proposed FR codes are also shown to meet a Singleton-like bound on the minimum distance for certain parameter ranges.

## Fractional Bits-Per-Cell for NAND Flash with Low Read Latency

- **Status**: ❌
- **Reason**: NAND 직접이나 비2진(non-power-of-two q-ary) 셀 매핑·비이진 ECC가 우월하다는 결론으로 바이너리 LDPC 기법 아님, 제외
- **ID**: ieee:8254419
- **Type**: conference
- **Published**: 4-8 Dec. 2
- **Authors**: Minghai Qin
- **PDF**: https://ieeexplore.ieee.org/document/8254419
- **Abstract**: Fractional bits-per-cell can be realized by a nonpower-of-two number of levels in NAND flash. They provide a larger number of modes beyond existing 4-level (MLC), 8-level (TLC), and 16-level (QLC) NAND flash and enable a smoother transition between existing modes, which increase the lifetime write capacity of the NAND device. Existing techniques for q-ary levels (where q is non-power-of-two) have a weakness in that q - 1 read thresholds are required to extract the exact cell-level information for decoding the data. In this paper, we provide logical-to-physical mappings between data and their physical programmed cell levels such that the read latency can be reduced by 2 or 3 times. In particular, we provide several mappings for q = 6 and q = 12 that enable 2.5 and 3.5 bits per cell. For non-power-of-two q-ary cells, the proposed mapping can be viewed as the counterpart of the Gray code used in MLCs, TLCs, and QLCs to map binary data into one of q = 4, 8 and 16 levels. We also provide the probability transition matrix-based channel models to extract soft information (e.g., log-likelihood ratios) in our mapping. Finally, we show that non-binary error-correction codes (ECCs) for our proposed mapping have higher data rate than binary ECCs to achieve the same data reliability.

## On Low Complexity Detection for QAM Isomorphic Constellations

- **Status**: ❌
- **Reason**: QAM isomorphic 성상 저복잡 검출·LLR 계산, 변조검출 기법으로 LDPC 디코더 기여 없음
- **ID**: ieee:8255100
- **Type**: conference
- **Published**: 4-8 Dec. 2
- **Authors**: Farbod Kayhan
- **PDF**: https://ieeexplore.ieee.org/document/8255100
- **Abstract**: Despite of the known gap from the Shannon's capacity, several standards are still employing QAM or star shape constellations, mainly due to the existing low complexity detectors. In this paper, we investigate the low complexity detection for a family of QAM isomorphic constellations. These constellations are known to perform very close to the peak-power limited capacity, outperforming the DVB-S2X standard constellations. The proposed strategy is to first remap the received signals to the QAM constellation using the existing isomorphism and then break the log likelihood ratio computations to two one dimensional PAM constellations. Gains larger than 0.6 dB with respect to QAM can be obtained over the peak power limited channels without any increase in detection complexity. Our scheme also provides a systematic way to design constellations with low complexity one dimensional detectors. Several open problems are discussed at the end of the paper.

## Function-shape-based particle swarm optimization and its application in maritime static target cooperative search

- **Status**: ❌
- **Reason**: 입자군집최적화 해상 표적 탐색, LDPC/ECC와 무관
- **ID**: ieee:8291440
- **Type**: conference
- **Published**: 29-31 Dec.
- **Authors**: Jinfeng Lv, Huaici Zhao
- **PDF**: https://ieeexplore.ieee.org/document/8291440
- **Abstract**: The application of particle swarm algorithm in optimization has been growing over the last few years, but this approach becomes computationally impracticable when the complexity of the problem increases. In this context, an improvement of the particle swarm algorithm-the function-shape-based particle swarm optimization (FSPSO) is presented. For a practical maritime cooperative search problem, FSPSO makes particles move around in the corresponding solution space according to certain rules to gather information firstly. Then FSPSO exploits the history data acquired during the first process to analyze the shape of the solution space. Based on the knowledge about the function shape, FSPSO generates solutions and iteration strategies. At last, the position and speed of each particle will be updated iteratively, aiming at producing a high quality solution to the optimization problem. The main idea behind FSPSO is to hybridize PSO with the search mode of a human being. This paper uses maritime static target cooperative search as a test domain. In order to evaluate the effectiveness of FSPSO, we perform a comparison between the performances of FSPSO with other approaches drawn from the scientific literature. Results demonstrate that FSPSO is able to produce statistically significantly higher quality solutions, outperforming many other approaches.

## An improvement of decoding time of ordered statistic decoding for medium length LDPC codes

- **Status**: ✅
- **Reason**: 바이너리 LDPC OSD 디코더 개선(C) - stopping condition/coincidence rate 신규, NAND LDPC BP 이식 가능
- **ID**: ieee:8259607
- **Type**: conference
- **Published**: 29 Nov.-1 
- **Authors**: Yüki Kawauchi, Kohtaro Watanabe, Seiji Kataoka
- **PDF**: https://ieeexplore.ieee.org/document/8259607
- **Abstract**: It is well-known that the Sum-Product Algorithm (SPA) is an efficient algorithm for decoding Low Density Parity Check (LDPC) codes. In spite of this, for LDPC codes with medium length which are now attracting interests for the application to fifth generation systems, it is known that decoding error rate is much inferior to that of Maximum Likelihood Decoding (MLD). In this paper, we improve bit error rate of SPA with so called Ordered Statistic Decoding (OSD) method by Fossorier [1]D Especially, we improve stopping condition of combinatorial search in OSD method and demonstrate by simulation that the proposal stopping condition is more efficient compared to Fossorier (IEEE J. Sel. Areas Commun., 19, 2001). For that purpose, we introduce a conception “coincidence rate” which plays an important role.

## A Simple Iterative Timing Recovery Algorithm for Burst Communication System at Very Low SNR

- **Status**: ❌
- **Reason**: 버스트 통신 타이밍 복원 알고리즘, LDPC 디코더/HW/구성 기여 없음
- **ID**: ieee:8446973
- **Type**: conference
- **Published**: 25-27 Dec.
- **Authors**: Yang Jie, Guangxia Li, Hongpeng Zhu
- **PDF**: https://ieeexplore.ieee.org/document/8446973
- **Abstract**: The performance of low rate coding system could achieve close to Shannon limit, which has broad application prospects. While, the system brings higher requirement for the demodulator, especially for burst communication due to very low SNR(signal-to-noise ratio) condition. In this paper, we takes timing recovery, which is the first step in the demodulator, as a research content. Code-aided theory is an effective method for timing recovery at very low SNR. In order to overcome the contradiction between estimation range and implentation complexity for the existing code-aided algorithms, the trigonometric polynomial interpolation is introduced into M-search algorithm, and then accurate timing estimation could obtained with the use of the interpolation operation. Simulations indicate that compared with the existing algorithms, the proposed method has strong advantages both in terms of estimation performance and implementation complexity. Finally, a new receiver structure is provided here where frame synchronization and the proposed code-aided algorithm is combined implemented, with little performance loss, which could effectively solve the problem of initial synchronization for burst communication at very low SNR.

## An energy efficient multi-rate QC-LDPC decoder

- **Status**: ✅
- **Reason**: 멀티레이트 QC-LDPC 디코더: row-merge normalized min-sum + layered + eDRAM HW 구현 — 이식 가능 디코더/HW(C/D)
- **ID**: ieee:8397258
- **Type**: conference
- **Published**: 21-23 Dec.
- **Authors**: Michaelraj Kingston Roberts, Elizabeth Sunny
- **PDF**: https://ieeexplore.ieee.org/document/8397258
- **Abstract**: This paper introduces, an energy efficient multirate decoder architecture for quasi-cyclic low-density parity-check (QC-LDPC) codes. To achieve good error correcting performance with lower complexity, an improved normalized min-sum algorithm with row-merge scheme is adopted. By exploring the properties of the layered decoding scheme, an enhanced QC-LDPC code with overlapped matrix is employed to offer adequate flexibility for parallel degree optimization and convergence speed. This in turn reduces the linear encoding complexity and data correlation problems during the multi-rate operations of the proposed decoder. Furthermore, to avoid memory access conflicts without increasing the hardware resources, eDRAM is utilized. By utilizing eDRAM, the overall memory bandwidth requisite is reduced considerably along with the inter-connect complexity and hardware overhead. This overall multi-rate decoder is designed and implemented using TSMC 65nm GP CMOS Technology to support all the code rates of IEEE 802.16e applications. From the implementation results it is observed that the designed multi-rate decoder attains improved throughput-to-area ratio (TAR) with less power consumption when analysed with other multi-rate decoders.

## Scalable image tamper detection and recovery based on dual-rate source-channel coding

- **Status**: ❌
- **Reason**: SPIHT+LDPC 소스-채널 결합 이미지 변조복구, LDPC는 베이스라인이고 떼어낼 ECC 기법 없음
- **ID**: ieee:8311600
- **Type**: conference
- **Published**: 20-21 Dec.
- **Authors**: Navid Daneshmandpour, Habibollah Danyali, Mohammad Sadegh Helfroush
- **PDF**: https://ieeexplore.ieee.org/document/8311600
- **Abstract**: In image tamper detection and recovery methods prevalently two sets of data need to be embedded into the main image, one known as authentication data for tamper detection and the other known as reference data for tamper recovery. In this paper, a scalable method for image tamper detection and recovery based on a dual-rate source-channel coding is proposed. In the proposed method the original image is first compressed by a scalable source coding algorithm. The compressed bitstream is then partitioned into two parts. Both parts are protected with a channel coding algorithm but with two different rates according to their importance for tamper recovery process. The proposed method takes advantage of two state-of-the-art algorithms, SPIHT for source coding and LDPC for channel coding. Simulation results show a noticeable improvement compared with related tamper detection and recovery schemes in the literature. Besides the reconstruction quality of the recovered image is scalable. This means that in low tampering rates, high-quality images are recovered and in high tampering rates, the image is still recoverable but with less reconstruction quality. Therefore the proposed method succeeded to both recover higher tampering rates and preserve the image quality.

## Blind Identification of LDPC Codes Based on Decoding

- **Status**: ❌
- **Reason**: LDPC 블라인드 식별(패리티검사행렬 복원), 채널 ECC 디코더·구성·HW 기여가 아님
- **ID**: ieee:8789115
- **Type**: conference
- **Published**: 19-21 Dec.
- **Authors**: Weinian Wang, Hua Peng, Lei Ji
- **PDF**: https://ieeexplore.ieee.org/document/8789115
- **Abstract**: A strong fault tolerance algorithm is proposed for blind identification of LDPC codes to solve the problem that the parity-check matrix of LDPC codes is hard to be reconstructed. First, the codes are arranged by reliability to construct data matrix and part of the parity-check vectors can be obtained by using Gaussian-Jordan column elimination operation. Then, codes with errors need to be eliminated and some codes need to be replaced to obtain most of the parity-check vectors. Finally, by using the parity-check vectors, some codes with high reliability can be decoded to obtain all parity-check vectors with the repetition of previous procedures. Compared with the existing blind recognition algorithms, the proposed method can implement blind identification of LDPC codes under the higher BER, which has a relatively low complexity and can be better applied to the actual environment. In the simulation experiments which mainly use (576,288) LDPC codes, the recognition rate of this method is above 90% under BER 0.00235.

## Lowered-complexity soft decoding of generalized LDPC codes over AWGN channels

- **Status**: ❌
- **Reason**: BCH 구성부호 기반 GLDPC의 Chase-II SISO 디코딩, generalized LDPC(BCH subcode 의존)라 바이너리 LDPC BP 이식성 약함
- **ID**: ieee:8275325
- **Type**: conference
- **Published**: 19-20 Dec.
- **Authors**: Sherif I. Elsanadily, Ashraf M. Mahran, Osama M. Elghandour
- **PDF**: https://ieeexplore.ieee.org/document/8275325
- **Abstract**: This paper presents a lowered complexity version of a reliability-based iterative decoding algorithm for Generalized Low Density Parity Check (GLDPC) codes with BCH constituent codes using Soft-Input Soft-Output (SISO) Chase-II algorithm. Applied to Gallager-based global LDPC code, it shows that the proposed algorithm, when employed on GLDPC with the multi-error correction BCH subcodes, reduces the complexity of the conventional Soft-Decision Decoding (SDD) with Chase algorithm at a cost of slight degradation in the error performance. The approach is built on eliminating the employment of the Chase SISO decoder at the Generalized Check Nodes (GCNs) where the expected number of errors is within the correction capability of the Hard-Decision Decoder (HDD). As a case study, the decoder is considered under AWGN channel and Simulation results are presented showing the complexity and performance of the conventional and proposed algorithms.

## High-order circular QAM constellation with high LDPC coding rate for phase noise channels

- **Status**: ❌
- **Reason**: Circular QAM constellation/Gray mapping design; LDPC is generic FEC, no transferable decoder/code-design technique
- **ID**: ieee:8301807
- **Type**: conference
- **Published**: 17-20 Dec.
- **Authors**: Bin Zheng, Lianjun Deng, Mamoru Sawahashi +1
- **PDF**: https://ieeexplore.ieee.org/document/8301807
- **Abstract**: This paper proposes a design for a high-order circular quadrature amplitude modulation (QAM) constellation using partial low-density parity-check (LDPC) coding associated with parallel double Gray mapping aiming at the application to a microwave radio backhaul to deal with time-varying phase noise channels. In the proposed circular QAM constellation design, we first design the best constellation in which the same number of signal points is mapped to all concentric rings. Then, we decrease the number of signal points in the inner rings and remap the signal points to the newly added rings outside the original rings while maintaining high affinity to the double Gray mapping feature. Computer simulation results show that partial LDPC coding with double Gray mapping decreases the required received signal-to-noise power ratio (SNR) at the bit error rate (BER) of 10−6 by approximately 0.2 dB compared to full LDPC coding for a high LDPC coding rate such as 0.9. We also show that the proposed circular 1024QAM decreases the required received SNR at the average BER of 10−6 by approximately 0.5 dB compared to that for rectangular 1024QAM.

## Performance of polar codes with MIMO-OFDM under frequency selective fading channel

- **Status**: ❌
- **Reason**: polar 부호 MIMO-OFDM BER 분석, SC 디코더는 polar 전용이라 바이너리 LDPC BP 비이식
- **ID**: ieee:8301790
- **Type**: conference
- **Published**: 17-20 Dec.
- **Authors**: Koya Watanabe, Shoichi Higuchi, Kazuki Maruta +1
- **PDF**: https://ieeexplore.ieee.org/document/8301790
- **Abstract**: This paper presents the BER performance analysis of polar codes with MIMO-OFDM under frequency selective channel, which has not been disclosed so far. Multiple-input multiple-output (MIMO) has been widely implemented or standardized to improve the throughput performance of wireless communications. Forward error correction (FEC) codes are also key techniques for stably improving bit error rate (BER) and have been studied as well as a demodulation scheme. FEC is required to be composed of simple encoder and decoder while achieving good BER performance as much as possible. Polar codes emerged as a promising FEC scheme. This code has a simple recursive encoder structure by using a phenomenon called "channel polarization". In addition, it has been reported that polar codes provably achieve the theoretical limit for communication systems with a successive cancellation decoder based on likelihood ratio. An calculation complexity of polar codes is less than that of low density parity check (LDPC) codes. Therefore, polar codes are an effective technique in realizing low electric power consumption to meet one of the demand conditions of 5G. Based on legacy detection schemes as zero forcing (ZF) and maximum likelihood detection (MLD), computer simulation results reveal the fundamental BER performance with controlling coding rate. Moreover, there is a problem that the log likelihood ratio (LLR) of MLD detection for soft-decision decoding can not be obtained. Therefore, in this paper, we investigate the likelihood function of MLD detection in the proposed system.

## Design of troposcatter broadband link based on SCFDE

- **Status**: ❌
- **Reason**: Troposcatter SCFDE link design; LDPC is generic FEC component, no extractable LDPC technique
- **ID**: ieee:8384095
- **Type**: conference
- **Published**: 17-20 Dec.
- **Authors**: Amit Garg, Suvra Shekhar Das
- **PDF**: https://ieeexplore.ieee.org/document/8384095
- **Abstract**: Troposcatter communication link is essentially a broadband, multipath, highly frequency selective, slow fading, long hop, point to point link. Orthogonal Frequency Domain Multiplexing (OFDM) has been proposed for troposcatter link design [1]. However, OFDM being a multi-carrier transmission scheme suffers from high Peak to Average Power Ratio (PAPR) problem which leads to non-linear distortion by Power Amplifier (PA) and considerable SNR loss if input signal is backed off. Single Carrier Frequency Domain Equalisation (SCFDE) exhibits a low PAPR, due to single carrier transmission, while retaining the advantage of Frequency Domain Equalisation (FDE). We present a troposcatter link design based on SCFDE in this paper. The design incorporates all the components of a practical system and is hardware implementable. It employs Low Density Parity Check (LDPC) Forward Error Correction (FEC) coding for SNR gain, QPSK/ 16 QAM modulation, Solid State Power Amplifier (SSPA) model to analyse the effect of nonlinearity and Input Back Off (IBO), frequency and timing synchronisation using double sliding window packet detection and Moose algorithm, Zero Forcing (ZF) channel estimation with Minimum Mean Square Error (MMSE) equalisation and dual diversity with Maximal Ratio Combining (MRC) combining. A novel frame format has been presented suited to the link design. Simulation parameters are derived from parameters of actual troposcatter links located in North China and between Dallas and Austin, Texas (U.S.A). SCFDE achieves a link margin of 3.4 dB with QPSK modulation and 2.8 dB with 16 QAM modulation due to high IBO for OFDM.

## Joint Source Channel Coding for Hyperspectral Imagery

- **Status**: ❌
- **Reason**: JSCC+LDPC/RS 직렬연접 채널코딩, LDPC는 베이스라인으로 표준 사용, 떼어낼 신규 ECC 기법 없음
- **ID**: ieee:8488122
- **Type**: conference
- **Published**: 15-17 Dec.
- **Authors**: A.S Mamatha, K Sagar, J Sumanth +3
- **PDF**: https://ieeexplore.ieee.org/document/8488122
- **Abstract**: On-board compression of hyperspectral imagery plays a vital role in the arena of remote sensing applications. This paper proposes a methodology to concatenate source coding with channel coding referred to as Joint Source Channel coding (JSCC) for hyperspectral images. The leverage of JSCC is that firstly the three on-board constraints namely memory, power and bandwidth are tackled with source coding. Secondly Channel coding mitigates the adverse effects of channel during the course of transmission of the downlinked image, thus maintaining the quality of the reconstructed image at the decoding side. Source coding exploits spatial and spectral decorrelation utilizing Intraband and Interband predictive coders. Serial Concatenated coders using Low Density Parity Check / Reed-Solomon (LDPC/RS) coder along with Convolutional coder are suggested for Channel coding. The proposed algorithm is simulated for Additive White Gaussian Noise (AWGN), Binary Symmetric Channel (BSC) and Rician channels. The methodology outcomes with an average BER of around 10-5 for different channel parameters, with an acceptable trade-off between complexity and performance.

## A LDPC convolutional code optimization method for FTN systems

- **Status**: ✅
- **Reason**: LDPC-CC 최적화(degree distribution, girth profile, sliding-window girth)로 코드설계 기법 이식 가능(E)
- **ID**: ieee:8322785
- **Type**: conference
- **Published**: 13-16 Dec.
- **Authors**: Zhanji Wu, Xin Huang
- **PDF**: https://ieeexplore.ieee.org/document/8322785
- **Abstract**: Next-generation satellite communication requires high transmission efficiency and high reliability to provide subscribers with various services. To satisfy these requirements, we optimize low-density parity-check convolutional codes (LDPC CC) for faster-than-Nyquist (FTN) systems with good degree distributions, girth profile (GP) as well as good sliding-window girth (SWG). In this paper, we mainly investigate the time-invariant LDPC CC which can be a parent code of a low-density parity-check block code (LDPC BC). A comprehensive set of LDPC CC optimization algorithm for FTN systems is presented and the optimized LDPC CC for FTN system can achieve about 2.9dB gain compared with the LDPC BC from WiMAX standard.

## A data recovering algorithm for LDPC codes in highly mobile satellite communications

- **Status**: ✅
- **Reason**: LDPC 디코딩 알고리즘 개선(소실 데이터 LLR=0 처리)과 BEC erasure 정정, 이식 가능(C)
- **ID**: ieee:8322679
- **Type**: conference
- **Published**: 13-16 Dec.
- **Authors**: Wang Yaowen, Guo Daoxing
- **PDF**: https://ieeexplore.ieee.org/document/8322679
- **Abstract**: In highly mobile satellite communication systems, the rapid motion of terminals, such as airplanes and missiles, will lead to the interruption of the communication and data loss, which includes burst data loss and packet loss. For the burst data loss, we will improve the decoding algorithm of the LDPC codes, which set the initial channel information corresponding to the lost data 0. This method can exhibit good data recovering performance within a certain range. While for the packet loss, we propose the group coding method to turn the packet recovering into the erasure correcting in the BEC, and we also compare the performance and complexity between iterative decoding and maximum likelihood decoding. The simulation results suggest that, the proposed algorithm can recover the lost data with relatively low complexity, which will be well suited in satellite communication systems under high mobility environments.

## Concatenated finite geometry and finite field LDPC codes

- **Status**: ✅
- **Reason**: finite-geometry/finite-field 연접 LDPC 신규 구성(globally coupled, 2-phase 디코딩), 바이너리 코드설계 이식 가능(E)
- **ID**: ieee:8270513
- **Type**: conference
- **Published**: 13-15 Dec.
- **Authors**: Mona Nasseri, Xin Xiao, Shaoliang Zhang +2
- **PDF**: https://ieeexplore.ieee.org/document/8270513
- **Abstract**: This paper presents two types of concatenated finite-geometry and finite-field LDPC codes which have the distinct features of both finite geometry and finite field LDPC codes, such as large minimum distances, no small trapping sets, fast decoding convergence, capable of correcting both random errors and bursts of erasures, flexibility in code construction, cyclic and quasi-cyclic structures. It is shown that these concatenated codes are globally coupled LDPC codes and they perform well over the AWGN and binary erasure channels with a two-phase iterative decoding scheme.

## A mathematical model of access control to allocate downlink bandwidth in high-density wireless LAN

- **Status**: ❌
- **Reason**: WLAN 다운링크 대역폭 할당 수학모델, LDPC와 무관
- **ID**: ieee:8270501
- **Type**: conference
- **Published**: 13-15 Dec.
- **Authors**: Yuto Katayama, Daisuke Umehara, Koichiro Wakasugi
- **PDF**: https://ieeexplore.ieee.org/document/8270501
- **Abstract**: In the IEEE 802.11 standards used for wireless local area networks (WLANs), an access point (AP) and stations (STAs) have opportunities to transmit the data frame in a basic service set (BSS) by carrier sense multiple access with collision avoidance (CSMA/CA). When there are a large number of STAs with high traffic in the BSS, the throughput from AP to a STA will deteriorate since its transmit opportunities are severely limited. We develop a mathematical model of access control to allocate bandwidth for the downlink from AP to STAs in the saturated traffic. The mathematical model enables us to derive a contention window (CW) size at AP with uniform backoff algorithm such that the downlink bandwidth is guaranteed even in the bidirectional saturated traffic. We show the validity of the CW size obtained from the mathematical model using a network simulator, ns3.

## Adaptive package coding on unreliable memories for LDPC decoders in radiation environment

- **Status**: ✅
- **Reason**: 불신뢰 메모리상 LDPC 디코더의 메시지 패키지 적응 코딩+sign/LSB 중요도+밀도진화, 이식 가능 디코더/HW 신뢰성 기법(C/D)
- **ID**: ieee:8303967
- **Type**: conference
- **Published**: 11-13 Dec.
- **Authors**: Guangjun Ge, Liuguo Yin
- **PDF**: https://ieeexplore.ieee.org/document/8303967
- **Abstract**: The commercial off-the-shelf technology, advanced by NASA, has driven the utilization of commercial components in aerospace, which results in severe fault problems for electronic systems. This paper considers the implementation of LDPC decoders on the unreliable memories, which introduce errors to the iterative messages. Firstly, LDPC decoders are typically implemented with the partially parallel architectures, where the messages are synchronously produced in groups. Based on this, we propose to put the messages into packages so as to permit an efficient coding on the package instead of the single message. Secondly, the sign bit of the message is shown to have the most influence on the decoding, while the least significant bit (LSB) is less important especially when the message has a large magnitude. Thus, by evaluating the magnitude level, we introduce an adaptive coding on the sign bits utilizing the LSBs. And we utilize a majority logic decision to achieve the evaluation, which makes the decoding execution more reliable. We develop a discrete density evolution to analyze the performances of various schemes, where the proposed scheme is shown to have a coding gain of 0.2 dB to the existing scheme, as well as a residual error that is nearly one order of magnitude lower. Moreover, the results of finite length codeword simulations are well matched with the density evolution analysis.

## The performance of nonbinary channel coded DCSK modulation system over Rayleigh fading channel

- **Status**: ❌
- **Reason**: 비이진(non-binary) LDPC 기반 DCSK, 비이진 LDPC는 제외
- **ID**: ieee:8304009
- **Type**: conference
- **Published**: 11-13 Dec.
- **Authors**: Pingping Chen, Guofa Cai, Fang Yi
- **PDF**: https://ieeexplore.ieee.org/document/8304009
- **Abstract**: This paper investigates the performance of nonbinary low-density parity-check (LDPC) channel coded M-ary differential chaos shift keying (DCSK) modulation systems over Rayleigh fading channels. The receiver adopts non-coherent detector for DCSK modulation and sum-product algorithm (SPA) for channel coding. Unlike that the previous binary channel coded M-ary DCSK system uses turbo iterative decoding between the detector and the channel decoder, the nonbinary coded DCSK system does not require turbo iteration, which simplifies the receiver implementation and reduces the decoding latency, because that soft information from M-ary detector can be directly used by M-ary channel decoder. The simulation result shows that the proposed nonbinary coded M-ary DCSK system has much better error performance than the binary coded one.

## Performance of pilot symbol assisted and PLL phase noise estimation and compensation for high-order circular QAM

- **Status**: ❌
- **Reason**: circular QAM 위상잡음 추정/보상, LDPC는 부수 언급
- **ID**: ieee:8303987
- **Type**: conference
- **Published**: 11-13 Dec.
- **Authors**: Bin Zheng, Lianjun Deng, Mamoru Sawahashi +1
- **PDF**: https://ieeexplore.ieee.org/document/8303987
- **Abstract**: Recently, we proposed a high-order circular quadrature amplitude modulation (QAM) constellation scheme with a high low-density parity-check (LDPC) coding rate that is suitable for partial LDPC coding associated with parallel double Gray mapping for microwave mobile backhaul. This paper presents the bit error rate (BER) performance of circular QAM when using a combination of Wiener filter based pilot symbol assisted (PSA) and phase locked loop (PLL) phase noise (PN) estimation and compensation methods. Computer simulation results show that the required received signal-to-noise power ratio (SNR) at the BER of 10-6 using the PSA and PLL PN estimation and compensation is decreased by approximately 0.3, 0.6, and 1.3 dB for the pilot symbol insertion interval of 25, 50, and 100 symbols, respectively, compared to that using only the PSA PN estimation for circular 1024QAM. Accordingly, we show that the PLL PN estimation is effective in decreasing the pilot symbol overhead of PSA PN estimation for circular QAM, which is robust against time-varying PN.

## Optimal signal constellation for downlink two-user NOMA

- **Status**: ❌
- **Reason**: NOMA 신호 성상도 최적화, LDPC는 베이스라인일 뿐
- **ID**: ieee:8304063
- **Type**: conference
- **Published**: 11-13 Dec.
- **Authors**: Wei Wang, Wei Zhang
- **PDF**: https://ieeexplore.ieee.org/document/8304063
- **Abstract**: In this paper, optimal signal constellation for downlink 2-user NOMA is investigated from both information theoretical and system level perspectives. Specifically, utilizing the gradient relationship between mutual information and minimum mean squared error, we first propose the optimal superposition coded constellation that maximizes the sum weighted mutual information. In order to verify the effectiveness of the proposed design, we then implement the proposed design in a low-density parity-check code (LDPC) coded modulated NOMA system. Numerical results demonstrate that, in the considered system, the promised achievable rate of our optimized superposition coded constellation can be achieved with a negligible gap.

## MRAM-based memorization system for NB-LDPC decoder

- **Status**: ❌
- **Reason**: 비이진(NB) LDPC 디코더용 MRAM 메모리 구현, 비이진 LDPC는 제외
- **ID**: ieee:8268886
- **Type**: conference
- **Published**: 10-13 Dec.
- **Authors**: Mohammad Sabbah, Ali Chamas Al Ghouwayel, Mostafa Rizk +1
- **PDF**: https://ieeexplore.ieee.org/document/8268886
- **Abstract**: This paper presents a novel implementation of the memorization system of the Non-Binary LDPC Decoder. The proposed approach relies on new implementations of STT-MRAM with power gating capabilities. A new data mapping has been defined to fit in with the physical dimensions of these implementations. The decoder adopting the devised memorization system has been compared to SRAM-based one which is used in almost all traditional decoders in order to demonstrate the feasibility of using power-gated MRAM. The obtained results show a significant reduction in the consumed energy by the memory reaching up to 78.45%.

## Demoiréing for screen-shot images with multi-channel layer decomposition

- **Status**: ❌
- **Reason**: LDPC=Layer Decomposition on Polyphase Components, 이미지 디모아레 처리. ECC LDPC 부호와 무관.
- **ID**: ieee:8305057
- **Type**: conference
- **Published**: 10-13 Dec.
- **Authors**: Jingyu Yang, Xue Zhang, Changrui Cai +1
- **PDF**: https://ieeexplore.ieee.org/document/8305057
- **Abstract**: Moiré patterns on screen-shot images are mainly due to the aliasing of the grid of the display and the camera sensor, which heavily degenerated the image quality. This paper proposes an demoiréing method for screen-shot images via layer decomposition on polyphase components (LDPC). The layer decomposition model separates the image into a background layer and a moiré layer, which are both regularized by a patch-based Gaussian Mixture Model (GMM) prior. To enhance the distinguishability between the image patches and moiré patches, the input image is first subsampled into four polyphase components, each of which is decomposed with the GMM-based layer decomposition model. The proposed model is applied on luminance (Y) channel to weaken the intensity of moiré patterns, and on red, green, blue channels respectively to further remove moiré patterns. Experimental results demonstrate that the proposed method is able to efficiently remove moiré artifacts for screen-shot images and outperform several other methods.
