# IEEE Xplore — 2012-09


## Flexible Channel Coding Approach for Short-Length Codewords

- **Status**: ❌
- **Reason**: convolutional+q-ary 선형결합 short-length 부호, LDPC 아니고 q-ary, 떼어낼 BP 기법 없음
- **ID**: ieee:6259797
- **Type**: journal
- **Published**: September 
- **Authors**: Mikel Hernaez, Pedro M. Crespo, Javier Del Ser
- **PDF**: https://ieeexplore.ieee.org/document/6259797
- **Abstract**: This letter introduces a channel coding design framework for short-length codewords which can achieve lower error floor than previous approaches. The proposed code is based on combining convolutional coding with a q-ary linear combination and unequal energy allocation. Simulation results suggest that for very low Bit Error Rates (BER) the proposed system will exhibit lower error floors than previous approaches, with a small performance penalty at mid-range BERs. On the other hand, when selecting an error floor higher than the previous approaches, the loss in performance at mid-range BERs is negligible.

## FFT Based Sum-Product Algorithm for Decoding LDPC Lattices

- **Status**: ❌
- **Reason**: LDPC lattice의 비이진/래티스 SPA(check node에서 local codeword 탐색), 바이너리 LDPC 아님
- **ID**: ieee:6259793
- **Type**: journal
- **Published**: September 
- **Authors**: Lida Safarnejad, Mohammad-Reza Sadeghi
- **PDF**: https://ieeexplore.ieee.org/document/6259793
- **Abstract**: LDPC lattices were introduced by Sadeghi et al. in [13] and have a good performance under generalized minsum and sum-product algorithms. The high complexity of these algorithms is mainly due to the search for local valid codewords in each check node process. In addition, when the dimension of such lattices is increased, these decoding algorithms are very time-consuming. In this paper, we propose an FFT based sum-product algorithm to decode LDPC lattices. In the check node process, using the FFT method reduces the check node complexity from O(dcg2) to O(dcg log g) where dc is the degree of a check equation and g is the alphabet size of an LDPC lattice. As a result, with almost the same complexity cost, we have a significant improvement over the performance of the minsum based decoding 2-level LDPC lattices with the symbol error probability smaller than 10-5 at SNR = 1.5 dB.

## Energy-Delay Tradeoff and Dynamic Sleep Switching for Bluetooth-Like Body-Area Sensor Networks

- **Status**: ❌
- **Reason**: BAN 에너지-지연 트레이드오프/스케줄링, 부호화 무관
- **ID**: ieee:6305027
- **Type**: journal
- **Published**: September 
- **Authors**: Eric Rebeiz, Giuseppe Caire, Andreas F. Molisch
- **PDF**: https://ieeexplore.ieee.org/document/6305027
- **Abstract**: Wireless technology enables novel approaches to healthcare, in particular the remote monitoring of vital signs and other parameters indicative of people's health. This paper considers a system scenario relevant to such applications, where a smart-phone acts as a data-collecting hub, gathering data from a number of wireless-capable body sensors, and relaying them to a healthcare provider host through standard existing cellular networks. Delay of critical data and sensors' energy efficiency are both relevant and conflicting issues. Therefore, it is important to operate the wireless body-area sensor network at some desired point close to the optimal energy-delay tradeoff curve. This tradeoff curve is a function of the employed physical-layer protocol: in particular, it depends on the multiple-access scheme and on the coding and modulation schemes available. In this work, we consider a protocol closely inspired by the widely-used Bluetooth standard. First, we consider the calculation of the minimum energy function, i.e., the minimum sum energy per symbol that guarantees the stability of all transmission queues in the network. Then, we apply the general theory developed by Neely to develop a dynamic scheduling policy that approaches the optimal energy-delay tradeoff for the network at hand. Finally, we examine the queue dynamics and propose a novel policy that adaptively switches between connected and disconnected (sleeping) modes. We demonstrate that the proposed policy can achieve significant gains in the realistic case where the control "NULL" packets necessary to maintain the connection alive, have a non-zero energy cost, and the data arrival statistics corresponding to the sensed physical process are bursty.

## Embracing Asynchronism: Achieving Cooperative Diversity using Zigzag Interference Cancellation

- **Status**: ❌
- **Reason**: 협력 다이버시티/지그재그 간섭제거 기법, LDPC 무관, 떼어낼 ECC 기법 없음
- **ID**: ieee:6225390
- **Type**: journal
- **Published**: September 
- **Authors**: Charlotte Hucher, Parastoo Sadeghi
- **PDF**: https://ieeexplore.ieee.org/document/6225390
- **Abstract**: Synchronization between the received signals from several transmitters is a challenging problem for cooperative communications. In the literature it is often assumed that the signals are somehow perfectly synchronized, but the problem of communication with asynchronism is rarely addressed. Moreover, in the few works where the problem is addressed, the proposed techniques are designed for a maximum delay whose value determines the decoding complexity. Thus in practice, only small delays can be dealt with. In this paper, instead of trying to avoid asynchronism between the received signals from two different transmitters, we propose to exploit it to provide cooperative diversity by optimally combining the two signals resulting from forward and backward zigzag interference cancellation. In addition to being tolerant to any delay, our bit error rate derivations and simulations show that the proposed scheme provides similar performance as delay-tolerant space-time block codes, such as the delay-tolerant Alamouti code, with a much lower complexity compared to a maximum likelihood (ML) decoder.

## Hierarchical Space Shift Keying for Unequal Error Protection

- **Status**: ❌
- **Reason**: 공간변조(SSK) UEP 설계, 변조 기법이라 LDPC ECC와 무관
- **ID**: ieee:6235070
- **Type**: journal
- **Published**: September 
- **Authors**: Ronald Y. Chang, Sian-Jheng Lin, Wei-Ho Chung
- **PDF**: https://ieeexplore.ieee.org/document/6235070
- **Abstract**: In this letter, we introduce the concept of enabling unequal error protection (UEP) with space shift keying (SSK)-type modulation that encodes the source information entirely in the antenna indices. Unique characteristics associated with SSK-type modulation as compared with conventional pulse/quadrature amplitude modulation (PAM/QAM) are discussed in the context of UEP design. Three general design concepts for two-level and three-level UEP are presented. Simulation results confirm the multilevel bit protection capabilities of the proposed hierarchical spatial constellation designs.

## A Simulation and Graph Theoretical Analysis of Certain Properties of Spectral Null Codebooks

- **Status**: ❌
- **Reason**: Spectral null 코드 그래프이론 분석, LDPC와의 link 언급뿐 떼어낼 신규 LDPC 기법 없음
- **ID**: ieee:8532162
- **Type**: journal
- **Published**: Sept. 2012
- **Authors**: K. Ouahada, H. C. Ferreira
- **PDF**: https://ieeexplore.ieee.org/document/8532162
- **Abstract**: The spectral shaping technique and the design of codes providing nulls at rational sub-multiples of the symbol frequency, as the case with spectral null (SN) codes, have enhanced digital signaling over communication channels as digital mass recorders and metallic cables. The study of the special structure of these codes helps in investigating and analyzing certain of their properties which have been proved and emphasized from a mathematical perspective using graph theory. The cardinality of spectral null codebooks reflects the rate of spectral null codes and therefore the amount of transmitted information data. The rate of these codes can also play a role in their error correction capability. The paper presents in different ways the special structure of spectral null codebooks and analyze better their properties. A possible link between these codes and other error correcting codes as the case of Low Density Parity Check (LDPC) is presented and discussed in this paper.

## Interval-Passing Algorithm for Non-Negative Measurement Matrices: Performance and Reconstruction Analysis

- **Status**: ❌
- **Reason**: Compressive sensing 신호복원 알고리즘(IPA), 채널 ECC 아님 - LDPC는 측정행렬 stopping set 분석에만 부수 사용
- **ID**: ieee:6317120
- **Type**: journal
- **Published**: Sept. 2012
- **Authors**: Vida Ravanmehr, Ludovic Danjean, Bane Vasic +1
- **PDF**: https://ieeexplore.ieee.org/document/6317120
- **Abstract**: We consider the Interval-Passing Algorithm (IPA), an iterative reconstruction algorithm for reconstruction of non-negative sparse real-valued signals from noise-free measurements. We first generalize the IPA by relaxing the original constraint that the measurement matrix must be binary. The new algorithm operates on any non-negative sparse measurement matrix. We give a performance comparison of the generalized IPA with the reconstruction algorithms based on 1) linear programming and 2) verification decoding. Then we identify signals not recoverable by the IPA on a given measurement matrix, and show that these signals are related to stopping sets responsible to failures of iterative decoding algorithms on the binary erasure channel (BEC). Contrary to the results of the iterative decoding on the BEC, the smallest stopping set of a measurement matrix is not the smallest configuration on which the IPA fails. We analyze the recovery of sparse signals on subsets of stopping sets via the IPA and provide sufficient conditions on the exact recovery of sparse signals. Reconstruction performance of the IPA using the IEEE 802.16e LDPC codes as measurement matrices are given to show the effect of stopping sets in the performance of the IPA.

## An Iterative Algorithm for Trust Management and Adversary Detection for Delay-Tolerant Networks

- **Status**: ❌
- **Reason**: DTN 신뢰관리/적대노드 탐지에 LDPC 메시지패싱 영감만 받은 reputation 알고리즘, ECC 기법 아님
- **ID**: ieee:5975152
- **Type**: journal
- **Published**: Sept. 2012
- **Authors**: Erman Ayday, Faramarz Fekri
- **PDF**: https://ieeexplore.ieee.org/document/5975152
- **Abstract**: Delay/Disruption Tolerant Networks (DTNs) have been identified as one of the key areas in the field of wireless communication, wherein sparseness and delay are particularly high. They are emerging as a promising technology in vehicular, planetary/interplanetary, military/tactical, disaster response, underwater and satellite networks. DTNs are characterized by large end-to-end communication latency and the lack of end-to-end path from a source to its destination. These characteristics pose several challenges to the security of DTNs. Especially, Byzantine attacks in which one or more legitimate nodes have been compromised and fully controlled by the adversary can give serious damages to the network in terms of latency and data availability. Using reputation-based trust management systems is shown to be an effective way to handle the adversarial behavior in Mobile Ad hoc Networks (MANETs). However, because of the unique characteristics of DTNs, those traditional techniques do not apply to DTNs. Our main objective in this paper is to develop a robust trust mechanism and an efficient and low cost malicious node detection technique for DTNs. Inspired by our recent results on reputation management for online systems and e-commerce, we develop an iterative malicious node detection mechanism for DTNs referred as ITRM. The proposed scheme is a graph-based iterative algorithm motivated by the prior success of message passing techniques for decoding low-density parity-check codes over bipartite graphs. Applying ITRM to DTNs for various mobility models, we observed that the proposed iterative reputation management scheme is far more effective than well-known reputation management techniques such as the Bayesian framework and EigenTrust. Further, we concluded that the proposed scheme provides high data availability and packet-delivery ratio with low latency in DTNs under various adversary attacks which attempt to both undermine the trust and detection scheme and the packet delivery protocol.

## Fast Decoding and Hardware Design for Binary-Input Compressive Sensing

- **Status**: ❌
- **Reason**: Binary-input compressive sensing 변조 코딩, 채널 ECC 아닌 rate adaptation - LDPC ECC 아님
- **ID**: ieee:6331566
- **Type**: journal
- **Published**: Sept. 2012
- **Authors**: Min Wang, Jun Wu, Sai Feng Shi +2
- **PDF**: https://ieeexplore.ieee.org/document/6331566
- **Abstract**: Binary-input compressive sensing (BiCS) has recently been applied to wireless communications as a modulated coding scheme for seamless rate adaptation. Different from conventional channel codes which generate binary symbols with logical-OR (XOR) operations, BiCS generates multilevel symbols through weighted sum operation. Although BiCS can be decoded by message passing, it needs to compute the convolution of probability functions in each iteration. The high decoding complexity has prevented the technique from being applied to practical use. In this paper, we propose a fast BiCS decoding algorithm and its corresponding partial-parallel hardware design. In this algorithm, we first build lookup tables to solve the computationally intensive problem of convolution. Through these tables, we successfully convert the convolution of probabilities into the polynomial of some exponential terms. This key step allows us to use log-likelihood ratio as message in message passing decoding and a fast algorithm is developed by approximate computing. We further design a partial-parallel hardware decoder. To avoid memory collision, we propose a multilevel cyclic-shift approach to generate the CS measurement matrix. We design horizontal unit processors with the proposed tables for iterative computing. Our analyses show that the proposed fast algorithm can reduce multiplications by nearly 90%. The decoding speed of our field-programmable gate array design reaches the range of communication rate in modern wireless networks.

## A Practical Architecture for OFDM-Based Decode-and-Forward Physical Layer Network Coding

- **Status**: ❌
- **Reason**: OFDM physical layer network coding 무선 응용, LDPC 언급 없고 떼어낼 ECC 기법 없음
- **ID**: ieee:6214625
- **Type**: journal
- **Published**: Sept. 2012
- **Authors**: Francesco Rossetto, Michele Zorzi
- **PDF**: https://ieeexplore.ieee.org/document/6214625
- **Abstract**: In physical layer network coding, it has been argued that performance improvements of a few dBs can be achieved by decoding a linear combination of colliding frames at an intermediate relay. The best results have been achieved by directly decoding the necessary linear combination rather than decoding each of the colliding packets, but so far only rather impractical architectures have been proposed. We explore in this paper a more pragmatic approach, where some important problems have been solved. We show by simulation that the proposed system is able to outperform analog network coding, the only other known practical architecture in this area so far, with substantial gains especially when noise amplification at the relay can be particularly detrimental, for instance when spatial diversity is available or large networks are analyzed.

## Improved soft-output M-algorithm for differential encoded LDPC coded systems with multiple-symbol differential detection

- **Status**: ❌
- **Reason**: 차분부호 LDPC+MSDD용 soft-output M-algorithm 복조기(SISO demodulator) 개선이 핵심, NAND LDPC 디코더에 떼어낼 부호-비의존 BP 기법 아님
- **ID**: ieee:6362679
- **Type**: conference
- **Published**: 9-12 Sept.
- **Authors**: Yang Yu, Shiro Handa, Fumihito Sasamori +1
- **PDF**: https://ieeexplore.ieee.org/document/6362679
- **Abstract**: In this paper, we propose an improved soft-output M-algorithm (ISOMA) and use it to reduce the computational complexity of differential encoded LDPC (DE-LDPC) coded systems with multiple-symbol differential detection (MSDD). The proposed ISOMA combines the features of iterative tree search detection based on M-algorithm (ITS-MA) and soft-output M-algorithm (SOMA) approaches, which can guarantee that the log-likelihood ratio (LLR) of each coded bit can be computed with high reliability. Simulation results show that the computational complexity of the MSDD soft-input soft-output demodulator (SISOD) as well as the iterative decoding complexity of DE-LDPC coded systems with MSDD can be greatly reduced by the proposed ISOMA. Compared with the existing ITS-MA and SOMA, the proposed ISOMA has better performance in terms of the BER performance and the ability of reducing the decoding complexity of DE-LDPC systems with MSDD. In addition, it is shown that the approach of the ISOMA using a proper selected scaling factor (SF) in the computation of the extrinsic LLRs can be used to further improve the performance of the ISOMA.

## When and how should decoding power be considered for achieving high energy efficiency?

- **Status**: ❌
- **Reason**: 무선 에너지효율 송수신 설계에서 디코딩 전력을 고려하는 시스템 최적화 논문, LDPC 디코더/HW/코드설계 신규 기여 없음
- **ID**: ieee:6362763
- **Type**: conference
- **Published**: 9-12 Sept.
- **Authors**: Cong Xiong, Geoffrey Ye Li, Yalin Liu +1
- **PDF**: https://ieeexplore.ieee.org/document/6362763
- **Abstract**: Widespread application of multimedia wireless services and requirement of ubiquitous access have triggered rapidly booming energy consumption at both transmitter and the receiver sides. Hence, energy-efficient design in wireless networks is very important and is becoming an inevitable trend. In this paper, we take decoding power into consideration when studying joint transmitter and receiver design for achieving high energy efficiency (EE). Based on a new function between transmit power and data rate that is derived by minimizing a lower bound on the overall transmit and receiver power, we investigate when and how should the decoding power be considered for optimizing EE. We find that the decoding power cannot be ignored for short-range wireless communications with a large bandwidth where the transmit power is usually low and give an analytical expression for quantifying the impact of decoding power on EE.

## Design of spatially-coupled rateless codes

- **Status**: ❌
- **Reason**: spatially-coupled rateless/Raptor(fountain, BEC) 설계 - fountain/erasure 응용, 떼어낼 채널 ECC 기법 없음
- **ID**: ieee:6362665
- **Type**: conference
- **Published**: 9-12 Sept.
- **Authors**: Iqbal Hussain, Ming Xiao, Lars K. Rasmussen
- **PDF**: https://ieeexplore.ieee.org/document/6362665
- **Abstract**: We investigate the design and performance of spatially-coupled rateless codes. A modified encoding process is introduced for spatially-coupled Luby Transform (SCLT) codes which leads to an almost regular variable-node degree distribution at the encoding graph. The proposed SCLT codes outperform its counterparts significantly over binary erasure channels, particularly in the erasure floor region. To further improve the erasure floor performance, the approach of spatial coupling is then extended to Raptor codes by concatenating a high-rate pre-coder to the SCLT codes. It is shown that the spatial coupling improves the convergence threshold of Raptor codes. Different ensembles of spatially-coupled Raptor codes are constructed depending on whether pre-coders and/or LT codes are spatially-coupled. The performance of different ensembles of spatially-coupled Raptor codes is then evaluated and compared based on density evolution, leading to an improved spatially-coupled Raptor code in terms of convergence threshold and lower complexity.

## Distributed data storage in sensor networks based on Raptor codes

- **Status**: ❌
- **Reason**: 센서망 분산저장용 Raptor(fountain) 부호, LDPC ECC 아님 - 제외 대상
- **ID**: ieee:6362587
- **Type**: conference
- **Published**: 9-12 Sept.
- **Authors**: Saber Jafarizadeh, Abbas Jamalipour
- **PDF**: https://ieeexplore.ieee.org/document/6362587
- **Abstract**: In this paper an algorithm for distributed data storage in large-scale sensor networks has been proposed. The main objective is to distribute the generated information throughout the network to increase its lifetime. At the same time it is desired that the original data can be recovered later by collecting the contents of a limited number of sensor nodes. In the scenario considered here the sensor nodes have limited energy and memory and each sensor saves only one encoded packet. Also sensors do not hold any routing table and no global information regarding network topology is available. The algorithm proposed here is based on Raptor codes and it inherits their linear time encoding and decoding complexity. Random walks are used for disseminating data amongst sensor nodes. Major benefits of the algorithm presented here is that it utilizes the online decoding property of Raptor codes by achieving the desired code degree distribution and for estimating the required global information regarding network topology, no excessive random walks and transmissions are used.

## Codes on high-order fields for the CCSDS next generation uplink

- **Status**: ❌
- **Reason**: 비이진 turbo/LDPC 우주 telecommand 부호 — non-binary는 제외 대상
- **ID**: ieee:6333104
- **Type**: conference
- **Published**: 5-7 Sept. 
- **Authors**: Gianluigi Liva, Enrico Paolini, Tomaso De Cola +1
- **PDF**: https://ieeexplore.ieee.org/document/6333104
- **Abstract**: Recently, short binary and non-binary iteratively-decodable codes have been proposed within the Next Generation Uplink (NGU) working group (WG) of the Consultative Committee for Space Data Systems (CCSDS). The NGU WG targets the design of an enhanced uplink mainly for telecommand with the aim of updating the current uplink standard that employs a short (63, 56) BCH code to protect the telecommand messages. The proposed non-binary turbo/LDPC codes attain large coding gains over the standardized BCH codes, but also over their binary turbo/LDPC counterparts (up to 1.5 dB of coding gain for information blocks of 64 bits). This paper overviews the proposed non-binary code construction, illustrating the potential of non-binary turbo/LDPC codes in the short block length regime. The impact of the proposed solution at system level is investigated, together with its integration in the CCSDS protocol stack.

## Efficient bit-interleaved APSK scheme for LDPC codes

- **Status**: ❌
- **Reason**: APSK 변조용 bit-interleaving·소프트검출, LDPC는 베이스라인이고 떼어낼 디코더 기법 없음
- **ID**: ieee:6333105
- **Type**: conference
- **Published**: 5-7 Sept. 
- **Authors**: Meixiang Zhang, Sooyoung Kim, Won-Yong Kim +1
- **PDF**: https://ieeexplore.ieee.org/document/6333105
- **Abstract**: This paper presents a new bit-interleaved higher-order APSK scheme for LDPC codes. Although the maximum decoding performance can be achieved using the maximum likelihood (ML) soft detection scheme, the complexity increases exponentially with the modulation orders. We approximate the ML soft detection scheme by applying the hard decision threshold (HDT) based method for a modified constellation of 32-APSK. In order to further improve the BER performance, we combined an efficient bit interleaving scheme, by considering that BER performance of each bit contained in a symbol is not uniform. Simulation results demonstrate that the proposed bit-interleaved scheme with very simple HDT based soft detection can achieve better performance compared to the ML detection of conventional scheme.

## Erasure codes for space communications: Recent findings and new challenges

- **Status**: ❌
- **Reason**: 우주통신 erasure code 연구가 비이진 LDPC로 확장하는 것이 핵심이고 바이너리는 기존 분석 인용 수준, 비이진+응용특이로 제외
- **ID**: ieee:6333092
- **Type**: conference
- **Published**: 5-7 Sept. 
- **Authors**: Giuliano Garrammone, Tomaso De Cola, Balazs Matuz +1
- **PDF**: https://ieeexplore.ieee.org/document/6333092
- **Abstract**: The use of erasure codes in space communications has proved to be promising in order to make communication more robust against both independent and correlated data losses. In particular, erasure codes are an appealing solution to provide space communications with increased reliability, especially in scenarios where large latencies make the use of automatic repeat request (ARQ) strategies problematic. In this regard, preliminary studies on the use of binary low-density parity-check (LDPC) codes under maximum likelihood (ML)/iterative (IT) decoding have been carried out showing the performance benefit they can bring over traditional schemes based on retransmissions. This paper extends the analysis conducted in previous studies towards non-binary LDPC codes. Performance assessment is carried out with respect to reliability metrics (codeword error rate) and encoding/decoding complexity, taking into consideration the limitations of space communications in terms of storage and processing capabilities. Finally, the paper sketches some design guidelines on the integration of the proposed codes into the Consultative Committee for Space Data Systems (CCSDS) protocol stack, implemented as extension of the Licklider Transmission Protocol (LTP).

## Communications over phase-noise channels: A tutorial review

- **Status**: ❌
- **Reason**: 위상잡음 채널 MAP 검출 튜토리얼 리뷰, LDPC는 부수 언급이고 떼어낼 ECC 기법 없음
- **ID**: ieee:6333095
- **Type**: conference
- **Published**: 5-7 Sept. 
- **Authors**: Giulio Colavolpe
- **PDF**: https://ieeexplore.ieee.org/document/6333095
- **Abstract**: In this tutorial paper, we first review the main information-theoretic results on channels affected by a time-varying phase noise. The main MAP symbol detection algorithms to be employed in such a challenging scenario are then described considering linear modulations and advanced coding schemes based on iterative detection and decoding. The role of pilot symbols will be also discussed.

## Bounds on the belief propagation threshold of non-binary LDPC codes

- **Status**: ❌
- **Reason**: 비이진 GF(q) LDPC의 BP threshold bound, 비이진+순수 이론 bound, 제외
- **ID**: ieee:6404692
- **Type**: conference
- **Published**: 3-7 Sept. 
- **Authors**: Leonid Geller, David Burshtein
- **PDF**: https://ieeexplore.ieee.org/document/6404692
- **Abstract**: We consider LDPC code ensembles over non-binary Galois fields, when used for transmission over arbitrary memoryless channels. Belief propagation decoding for these codes has been shown to achieve excellent results. However, computing the decoding threshold using density evolution is usually impractical, since one needs to propagate multi-dimensional probability distributions, and Monte Carlo simulations are required instead. By considering the evolution of the message Bhattacharyya parameter and the message expected value parameter we derive a simple lower bound on the performance of the algorithm. This bound applies for both regular and irregular non-binary LDPC ensembles.

## Spatially coupled quantum LDPC codes

- **Status**: ❌
- **Reason**: 양자 LDPC, entangled qubit pair 의존(양자 전용 개념), 제외
- **ID**: ieee:6404686
- **Type**: conference
- **Published**: 3-7 Sept. 
- **Authors**: Iryna Andriyanova, Denise Maurice, Jean-Pierre Tillich
- **PDF**: https://ieeexplore.ieee.org/document/6404686
- **Abstract**: We propose here a new construction of spatially coupled quantum LDPC codes using a small amount of entangled qubit pairs shared between the encoder and the decoder which improves quite significantly all other constructions of quantum LDPC codes or turbo-codes with the same rate.

## LDPC-based coded cooperative jamming codes

- **Status**: ❌
- **Reason**: 보안(coded cooperative jamming/wiretap) 응용으로 표준 classical/SC-LDPC를 보안 누설 차단에 사용; 떼어낼 디코더·구성 기여 없음, 보안 원칙 제외
- **ID**: ieee:6404716
- **Type**: conference
- **Published**: 3-7 Sept. 
- **Authors**: Alexandre J. Pierrot, Matthieu R. Bloch
- **PDF**: https://ieeexplore.ieee.org/document/6404716
- **Abstract**: We present a practical coded cooperative jamming scheme for the problem of secure communications over the two-way wiretap channel. We design low-density parity-check (LDPC) based codes whose codewords interfere at the eavesdropper's terminal, thus providing secrecy. We show that our scheme can guarantee low information leakage rate, and we assess its precise performance for classical and spatially coupled LDPC codes.

## Non-binary protograph-based LDPC codes for short block-lengths

- **Status**: ❌
- **Reason**: 비이진(non-binary) protograph LDPC 구성, 바이너리 한정 기준에 의해 제외
- **ID**: ieee:6404676
- **Type**: conference
- **Published**: 3-7 Sept. 
- **Authors**: Ben-Yue Chang, Dariush Divsalar, Lara Dolecek
- **PDF**: https://ieeexplore.ieee.org/document/6404676
- **Abstract**: This paper presents two complementary constructions of finite-length non-binary protograph-based codes with the focus on the short block-length regime. The first class is based on the existing approaches of applying the copy-and-permute operations to the constituent protograph with unweighted edges, followed by assigning non-binary scales to the edges of the derived graph. The second class is novel and is based on the so-called graph cover of a non-binary protograph: the original protograph has fixed edge scalings and copy-and-permute operations are applied to the edge-weighted protograph. The second class is arguably more restrictive, but in turn it offers simpler design and implementation. We provide design and construction of these non-binary codes for short block-lengths. Performance, cycle distribution and the minimum distance of the binary image of selected codes over AWGN is provided for information block-lengths as low as 64 bits.

## A simple proof of threshold saturation for coupled vector recursions

- **Status**: ❌
- **Reason**: threshold saturation 순수 이론 증명(DE), 디코더/HW/구성으로 이어지지 않음
- **ID**: ieee:6404671
- **Type**: conference
- **Published**: 3-7 Sept. 
- **Authors**: Arvind Yedla, Yung-Yih Jian, Phong S. Nguyen +1
- **PDF**: https://ieeexplore.ieee.org/document/6404671
- **Abstract**: Convolutional low-density parity-check (LDPC) codes (or spatially-coupled codes) have now been shown to achieve capacity on binary-input memoryless symmetric channels. The principle behind this surprising result is the threshold-saturation phenomenon, which is defined by the belief-propagation threshold of the spatially-coupled ensemble saturating to a fundamental threshold defined by the uncoupled system. Previously, the authors demonstrated that potential functions can be used to provide a simple proof of threshold saturation for coupled scalar recursions. In this paper, we present a simple proof of threshold saturation that applies to a wide class of coupled vector recursions. The conditions of the theorem are verified for the density-evolution equations of: (i) joint decoding of irregular LDPC codes for a Slepian-Wolf problem with erasures, (ii) joint decoding of irregular LDPC codes on an erasure multiple-access channel, and (iii) admissible protograph codes on the BEC. This proves threshold saturation for these systems.

## Integer low-density lattices based on construction A

- **Status**: ❌
- **Reason**: 비이진 LDPC 기반 정수 격자(LDA lattice) 구성, 비이진+격자 응용, 제외
- **ID**: ieee:6404707
- **Type**: conference
- **Published**: 3-7 Sept. 
- **Authors**: Nicola di Pietro, Joseph J. Boutros, Gilles Zémor +1
- **PDF**: https://ieeexplore.ieee.org/document/6404707
- **Abstract**: We describe a new family of integer lattices built from construction A and non-binary LDPC codes. An iterative message-passing algorithm suitable for decoding in high dimensions is proposed. This family of lattices, referred to as LDA lattices, follows the recent transition of Euclidean codes from their classical theory to their modern approach as announced by the pioneering work of Loeliger (1997), Erez, Litsyn, and Zamir (2004-2005). Besides their excellent performance near the capacity limit, LDA lattice construction is conceptually simpler than previously proposed lattices based on multiple nested binary codes and LDA decoding is less complex than real-valued message passing.

## Irregular product codes

- **Status**: ❌
- **Reason**: MDS 기반 irregular product codes(erasure 채널), 비-LDPC 부호이며 떼어낼 바이너리 LDPC BP 기법 없음
- **ID**: ieee:6404656
- **Type**: conference
- **Published**: 3-7 Sept. 
- **Authors**: Masoud Alipour, Omid Etesami, Ghid Maatouk +1
- **PDF**: https://ieeexplore.ieee.org/document/6404656
- **Abstract**: We introduce irregular product codes, a class of codes where each codeword is represented by a matrix and the entries in each row (column) of the matrix come from a component row (column) code. As opposed to standard product codes, we do not require that all component row codes nor all component column codes be the same. Relaxing this requirement can provide some additional attractive features such as allowing some regions of the codeword to be more error-resilient, providing a more refined spectrum of rates for finite lengths, and improved performance for some of these rates. We study these codes over erasure channels and prove that for any 0 <; ε <; 1, for many rate distributions on component row codes, there is a matching rate distribution on component column codes such that an irregular product code based on MDS codes with those rate distributions on the component codes has asymptotic rate 1 - ε and can decode on erasure channels having erasure probability <; ε (and having alphabet size equal to the alphabet size of the component MDS codes).

## Towards integrating Quantize-Map-Forward relaying into LTE

- **Status**: ❌
- **Reason**: LTE QMF 릴레이 통합 응용, LLR 계산만 수정, NAND LDPC에 떼어낼 신규 기법 없음
- **ID**: ieee:6404661
- **Type**: conference
- **Published**: 3-7 Sept. 
- **Authors**: Emre Atsan, Raymond Knopp, Suhas Diggavi +1
- **PDF**: https://ieeexplore.ieee.org/document/6404661
- **Abstract**: We present a method to integrate the Quantize-Map-Forward (QMF) relaying scheme [1] into the standard LTE operation, for a two-relay diamond network configuration. Our approach implements QMF using mainly existing LTE modules and functionalities, and results in minimal changes in the standard link-layer LTE operation. In particular, the destination operation is only affected in that we adapt the log-likelihood ratio (LLR) calculations at the decoder input to take into account the existence of relays; thus, the decoding complexity and operations (apart the LLR calculations) are not modified. We report extensive performance evaluations of our scheme using the OpenAirInterface (OAI) link-level simulation tools.

## Chernoff bounds for analysis of rate-compatible sphere-packing with numerous transmissions

- **Status**: ❌
- **Reason**: RCSP에 대한 Chernoff bound 순수 이론 분석으로 LDPC 디코더·구성·HW로 안 이어짐, 비-LDPC 이론 bound
- **ID**: ieee:6404719
- **Type**: conference
- **Published**: 3-7 Sept. 
- **Authors**: Tsung-Yi Chen, Dariush Divsalar, Richard D. Wesel
- **PDF**: https://ieeexplore.ieee.org/document/6404719
- **Abstract**: Recent results by Chen et al. and Polyanskiy et al. explore using feedback to approach capacity with short blocklengths. This paper explores Chernoff bounding techniques to extend the rate-compatible sphere-packing (RCSP) analysis proposed by Chen et al. to scenarios involving numerous retransmissions and different step sizes in each incremental retransmission. Williamson et al. employ exact RCSP computations for up to six transmissions. However, exact RCSP computation with more than six retransmissions becomes unwieldy because of joint error probabilities involving numerous chi-squared distributions. This paper explores Chernoff approaches for upper and lower bounds on the error probability to provide support for computations involving more than six transmissions. We present two versions of upper and lower bounds on the error probability for the two-transmission case. One of the versions is extended to the general case of m transmissions where m ≥ 1. Computing the bounds for general m requires minimization of exponential functions with the auxiliary parameters. The numerical results, however, show that weakening the bounds by considering marginal probabilities and the case of two transmissions is already tight. These bounds also provide good estimates of the expected throughput and expected latency, which are useful for optimization purposes.

## Improved joint turbo decoding and physical-layer network coding

- **Status**: ❌
- **Reason**: turbo decoding+physical-layer network coding 무선 응용, XOR soft 추정은 NC 특화로 바이너리 LDPC BP에 이식할 부호비의존 기법 아님
- **ID**: ieee:6404731
- **Type**: conference
- **Published**: 3-7 Sept. 
- **Authors**: Maria Cláudia Castro, Bartolomeu F. Uchôa-Filho, Tiago T. V. Vinhoza +2
- **PDF**: https://ieeexplore.ieee.org/document/6404731
- **Abstract**: We present an improved decoding algorithm for joint turbo decoding and physical-layer network coding. Instead of decoding the individual (binary) messages separately at the relay, the proposed algorithm, from the superimposed faded signals, yields an XOR estimate of the sent messages. Moreover, we introduce a softening of the XOR values to improve the overall performance. Simulation results show that this simple idea yields gains up to 4.5 dB in a Rayleigh fading channel model when compared to a similar scheme.

## Design of Low-Delay Distributed Joint Source-Channel Codes Using Irregular LDPC Codes

- **Status**: ❌
- **Reason**: 분산 결합 소스-채널 부호설계(UEP LP 최적화), JSCC/distributed compression으로 순수 채널 ECC 아님
- **ID**: ieee:6398904
- **Type**: conference
- **Published**: 3-6 Sept. 
- **Authors**: Iqbal Shahid, Pradeepa Yahampath
- **PDF**: https://ieeexplore.ieee.org/document/6398904
- **Abstract**: A practical approach to designing distributed joint source channel (DJSC) codes for correlated binary sources using LDPC codes is presented. In this approach, both distributed compression and channel error protection are achieved by optimally puncturing bits of a systematic channel code to match the source correlation and channel error probability. This requires the design of a channel code with a specific unequal error protection (UEP) property. Towards this end, we present a linear-programming based algorithm for optimizing an irregular LDPC code for a given level of source correlation and channel noise. Experimental results are presented for both binary symmetric channels and Gaussian channels, which demonstrate that the proposed DJSC codes can significantly outperform the best code found through random search, tandem source-channel codes and previously reported schemes based on turbo codes when the encoding delay is constrained.

## Distributed Lossy Source Coding Using Real-Number Codes

- **Status**: ❌
- **Reason**: 분산 손실 소스코딩(DFT 실수부호 양자화), 채널 ECC 아님
- **ID**: ieee:6399216
- **Type**: conference
- **Published**: 3-6 Sept. 
- **Authors**: Mojtaba Vaezi, Fabrice Labeau
- **PDF**: https://ieeexplore.ieee.org/document/6399216
- **Abstract**: We show how real-number codes can be used to compress correlated sources, and establish a new framework for distributed lossy source coding, in which we quantize compressed sources instead of compressing quantized sources. This change in the order of binning and quantization blocks makes it possible to model correlation between continuous-valued sources more realistically and correct quantization error when the sources are completely correlated. The encoding and decoding procedures are described in detail, for discrete Fourier transform (DFT) codes. Reconstructed signal, in the mean-squared error sense, is seen to be better than or close to quantization error level in the conventional approach.

## Low-Complexity Rotated QAM Demapper for the Iterative Receiver Targeting DVB-T2 Standard

- **Status**: ❌
- **Reason**: DVB-T2 회전 QAM 디맵퍼 복잡도 저감, LDPC ECC 기법 없음(변복조 전용)
- **ID**: ieee:6399046
- **Type**: conference
- **Published**: 3-6 Sept. 
- **Authors**: YouZhe Fan, Chi-ying Tsui
- **PDF**: https://ieeexplore.ieee.org/document/6399046
- **Abstract**: Gray mapping and signal space diversity (SSD) are adopted in DVB-T2 to achieve better performance and system robustness. However, the traditional maximum a posteriori demapping for Gray mapped SSD signal is complicated for higher order modulation and it is not practical to be used in the iterative receiver structure. In this work, simplified demappers are proposed by approximating the 2-dimensional detection with 1-dimensional detection and compensating the loss due to the correlation between the I and Q components. Simulation results show that the proposed simplified demappers can approach the optimal demapper performance with a much lower complexity.

## Nonbinary LDPC-coded modulation for multi-Tb/s optical transport

- **Status**: ❌
- **Reason**: 비이진(non-binary) LDPC 코딩 변조 — 비이진 LDPC는 제외 대상
- **ID**: ieee:6358725
- **Type**: conference
- **Published**: 23-27 Sept
- **Authors**: Murat Arabaci, Ivan B. Djordjevic
- **PDF**: https://ieeexplore.ieee.org/document/6358725
- **Abstract**: Nonbinary LDPC codes and their use in multi-Tb/s optical transport networks are discussed. Comparisons are made against prior-art binary LDPC-coded modulation schemes.

## Nonbinary LDPC-coded OFDM over four/eight-mode fibers with mode-dependent loss

- **Status**: ❌
- **Reason**: 비이진 LDPC 코딩 OFDM(few-mode fiber) — 비이진 LDPC는 제외 대상
- **ID**: ieee:6358763
- **Type**: conference
- **Published**: 23-27 Sept
- **Authors**: Changyu Lin, Ivan B. Djordjevic, Ding Zou +2
- **PDF**: https://ieeexplore.ieee.org/document/6358763
- **Abstract**: We propose a non-binary LDPC coded mode-multiplexed coherent optical OFDM system suitable for transmission of 1.28 Tb/s 16-QAM signals over 2000 km of few-mode fiber with mode dependent loss, in strong coupling regime.

## Power and Bandwidth Efficient Q-Ary LDPC Coded Partial Response Continuous Phase Modulation

- **Status**: ❌
- **Reason**: GF(q) q-ary LDPC coded CPM — 비이진 LDPC 제외
- **ID**: ieee:6478621
- **Type**: conference
- **Published**: 21-23 Sept
- **Authors**: Rui Xue, Chun-li Xiao
- **PDF**: https://ieeexplore.ieee.org/document/6478621
- **Abstract**: Continuous Phase Modulation (CPM) provides an attractive option for spectral efficient communication systems. Binary low-density parity-check (LDPC) coded CPM can improve power efficiency and attain high error correcting capacity, but the convergence of threshold is still much higher than Shannon limit. In order to improve bit error performance, bandwidth efficiency and reduction of convergence threshold compared to above-mentioned scheme, we employ LDPC codes over GF(q>2) as the outer code. In this paper, the combination of q-ary LDPC coding and partial response CPM (PRCPM) is presented, then the effect of LDPC code length, code rate and iterative number on the performance of the system is studied. In the proposed scheme, q-ary LDPC codes and PRCPM are considered together to improve both error performance and bandwidth efficiencies, and the combination can achieve better trade-off between power efficiency and bandwidth efficiency than binary LDPC coded CPM. Meanwhile, the LDPC codes over GF(q) combined with q-ary CPM can avoid the conversion from bit probability to symbol probability and its inversion in combination of binary LDPC coded q-ary CPM, and improve reliability of information transmission.

## A Compact Construction for Nonbinary LDPC Codes Using Permutation Polynomials

- **Status**: ❌
- **Reason**: permutation polynomial 기반 nonbinary GF(q) LDPC 구성 — 비이진 LDPC는 명시적 제외
- **ID**: ieee:6478269
- **Type**: conference
- **Published**: 21-23 Sept
- **Authors**: Tao Xiong, Hongyu Zhao
- **PDF**: https://ieeexplore.ieee.org/document/6478269
- **Abstract**: A compact construction for nonbinary low-density parity-check (LDPC) codes over GF(q) (q>2) using permutation polynomials (PPs) is proposed in this paper. Following the previous compact construction for binary LDPC codes using quadratic permutation polynomials (QPPs) over integer rings, a QPP whose coefficients are chosen for maximizing the girth is used for determining all the positions of nonzero elements in the parity check matrix of a regular nonbinary LDPC code. Moreover, it is proposed to use a linear permutation polynomial (LPP) over GF(q) for determining the distribution of nonzero elements of GF(q) at the nonzero positions. Computer simulation results of LDPC codes over GF(8) have shown that the propose compact construction can attain similar error correction performance with Mackay's random construction for nonbinary LDPC codes.

## Construction of Non-Binary LDPC Codes with Very Large Girth

- **Status**: ❌
- **Reason**: 비이진 GF(q) LDPC 구성(large girth) — 비이진 LDPC 제외
- **ID**: ieee:6478463
- **Type**: conference
- **Published**: 21-23 Sept
- **Authors**: Xiongfei Tao, Deyu Feng, Yan Zhang +1
- **PDF**: https://ieeexplore.ieee.org/document/6478463
- **Abstract**: A non-binary LDPC codes whose parity check matrix has uniform column weight 2 is constructed in this paper. The approach derives a non-binary LDPC codes from a column-weight 2 binary LDPC codes which is designed according to a all one (2, k) matrix, We proposed a search algorithm for constructing a (2, k) LDPC codes with desired girth, and in this paper, we use the search algorithm twice to obtain a code with larger girth. The simulation result shows that the proposed LDPC codes outperform the random codes.

## Research on LDPC Coding Scheme for Relay Cooperative Communication

- **Status**: ❌
- **Reason**: 릴레이 협력통신 전송 스킴(검사행렬 서브블록 분할 전송), 응용특이적이고 이식 가능 코드설계 아님
- **ID**: ieee:6478651
- **Type**: conference
- **Published**: 21-23 Sept
- **Authors**: Xuehua Li, Zhensong Li, Yiqing Cao
- **PDF**: https://ieeexplore.ieee.org/document/6478651
- **Abstract**: This article analyses the Frame Error Rate (FER) performance with the Pairwise Error Probability (PEP) and presents a LDPC coding scheme for Relay Cooperative Communication (RCC) system. In this scheme, the Degree Distribution of excellent LDPC codes is considered and the LDPC check Matrix is divided into several sub-blocks with different mean column weight (MCW), then specific sub-blocks are transmitted in different transmission Modes. In the Broadcasting (BC) Mode, the sub-block with large MCW has high priority to be transmitted by the source node to make sure the relay nodes correctly receive and re-transmit the signal, which can obtain the system diversity gain. In the Multi-address (MAC) Mode, the source node and relay nodes transmit sub-blocks that haven't been used before to form the complementary redundancy structure in the terminal node, and earn high coding gain. Simulation results confirm the effectiveness of this coding scheme for RCC system.

## A Joint Coded Modulation Scheme and Its Iterative Receiving for Deep-Space Communications

- **Status**: ❌
- **Reason**: LDPC-CPM 딥스페이스 결합변복조, LDPC는 베이스라인이고 떼어낼 신규 디코더/HW 없음
- **ID**: ieee:6478295
- **Type**: conference
- **Published**: 21-23 Sept
- **Authors**: Rui Xue, Chun-li Xiao
- **PDF**: https://ieeexplore.ieee.org/document/6478295
- **Abstract**: Space exploration missions have become increasingly complicated and various, and the current deep-space communication schemes can't meet the demand of high-speed and real-time multimedia correspondence. Therefore, the design of a fast and efficient transmission scheme is one of the important ways to solve the conflict. With organic combination of LDPC codes, continuous phase modulation (CPM) and turbo iterative detection, a scheme of joint coded modulation based on turbo principle is presented. In this paper, the model of LDPC-CPM system is established firstly, then realization scheme of CPM is proposed, and the effect of main parameters on the performance of the system is studied finally, which can provide the reference basis for practical application. The research results show that the proposed scheme can not only improve power efficiency and BER performance in the background of extremely low SNR effectively, but also give consideration to validity of information transmission and improve the band efficiency, and partly solve the problem of failing to give attention to both high-speed transmission and reliable transmission. Meanwhile, the receiver whose implementation is achievable can reach a good compromise between performance and complexity.

## Coded Cooperation with Permutation and Block Encoding for Wireless Networks

- **Status**: ❌
- **Reason**: 무선 협력통신용 인터리브드 블록코드 기법, 비-LDPC·응용특이적
- **ID**: ieee:6478454
- **Type**: conference
- **Published**: 21-23 Sept
- **Authors**: Changcai Han, Jing Huang
- **PDF**: https://ieeexplore.ieee.org/document/6478454
- **Abstract**: A novel coded cooperation scheme based on the intersection of interleaved block codes is proposed for multisource multi-relay networks. Specifically, the multiple source data are jointly encoded and forwarded to the destination by multiple cooperative relays while the sources and relays have low complexity. In this way, a distributed coding scheme with permutation and block encoding is constructed to achieve diversity and coding gains simultaneously. The scheme can achieve significant performance gain over direct transmission and fit for cooperative networks with different number of sources or relays.

## Joint Iterative Source Channel Decoder for Video Transmitted Stream

- **Status**: ❌
- **Reason**: H.264 비디오 결합소스채널 디코더(JSCC), LDPC 베이스라인이고 떼어낼 ECC 기법 없음
- **ID**: ieee:6478555
- **Type**: conference
- **Published**: 21-23 Sept
- **Authors**: Yue Wang, Rong Xie
- **PDF**: https://ieeexplore.ieee.org/document/6478555
- **Abstract**: H.264 is widely used in recently years and has achieved a significant improvement in coding efficiency. The entropy coding methods used in H.264 are CAVLC and CABAC. Although these two variable length code methods can achieve high compression, they are very sensitive to channel errors. In this paper, An iterative joint source channel decoder which combines the variable length code and low density parity check (LDPC) code in an iterative scheme is proposed to dealing with this sensitivity to channel errors and this joint source channel decoder is applied to the decoding of the motion vectors in H.264 coded video stream.. Although H.264 codec has proposed several error resilience methods, we believe this method could provide additional error resilience to H.264 stream. Experiment indicates that our IJSCD achieves significant improvement than a separate scheme.

## A Novel Decoding Method for Rateless Codes Basing on Packet Combing

- **Status**: ❌
- **Reason**: rateless(BDRC/LT) 코드용 패킷결합 디코딩, 비-LDPC fountain 부호 기법
- **ID**: ieee:6478327
- **Type**: conference
- **Published**: 21-23 Sept
- **Authors**: Qin Zhang, Dengsheng Lin, Gang Wu
- **PDF**: https://ieeexplore.ieee.org/document/6478327
- **Abstract**: In this paper, two novel decoding methods are designed for two kinds of rateless codes: binary deterministic rateless (BDRC) codes and LT codes. The traditional decoding algorithms for the two kinds of codes discard the erroneous packets that may only contain few erroneous bits, which will causes the waste of bandwidth. The novel decoding methods adopt the packet combining technology to find the positions of the erroneous bits in the erroneous packets and correct them, which will accelerate the collection of the correct packets for the traditional decoding methods. The simulation results show that the proposed decoding methods outperform the traditional decoding methods for both BDRC codes and LT codes.

## Performance of Min-Sum for Decoding Fountain Codes over BIAWGN Channels

- **Status**: ❌
- **Reason**: fountain 코드에 표준 NMS/OMS 적용·Gaussian 근사 분석, 비-LDPC 부호+표준 MS변형
- **ID**: ieee:6478614
- **Type**: conference
- **Published**: 21-23 Sept
- **Authors**: Lei Yuan
- **PDF**: https://ieeexplore.ieee.org/document/6478614
- **Abstract**: In this paper, we extend the min-sum (MS) and its two improved algorithms (i.e., the normalized MS algorithm and the offset MS algorithm) to decode fountain codes over the binary input additive white Gaussian noise (BIAWGN) channel. We use Gaussian approximation method to analyze the asymptotic performance of fountain codes under various decoding algorithms and optimize the parameters of the two improved MS algorithms. Both the theoretical analysis and simulation results demonstrate that the normalized MS decoding with optimal parameter has better bit error performance than the offset MS decoding with optimal parameter.

## Rate and Power Allocation for 2-Level Superposition Coded Modulation Supporting Both Unicast and Multicast Traffic

- **Status**: ❌
- **Reason**: superposition 변조 rate/power 할당, LDPC 디코더·코드설계 기여 없음
- **ID**: ieee:6478632
- **Type**: conference
- **Published**: 21-23 Sept
- **Authors**: YouZhe Fan, Chi-ying Tsui
- **PDF**: https://ieeexplore.ieee.org/document/6478632
- **Abstract**: To support simultaneous multicasting and unicasting service, a 2-level superposition coded modulation (SCM) system with variable code rate allocation is studied. To obtain the most power-efficient scheme for this system, brute-force method can be used to find the best power allocation for each code rate allocation. However, it is very complicated and time-consuming. In this work, the properties of the 2-level SCM capacity is first studied using numerical evaluation and a heuristic method is proposed to efficiently find the optimal rate assignment and power allocation. The simulation results verify the performance of the proposed power allocation method and experimental results show that equal rate allocation scheme provides a power-efficient transmission.

## Modified turbo codes for next generation wireless networks

- **Status**: ❌
- **Reason**: 비-LDPC(turbo-like MTC) 부호, LDPC는 비교 대상일 뿐 떼어낼 바이너리 LDPC 기법 없음
- **ID**: ieee:6331884
- **Type**: conference
- **Published**: 20-22 Sept
- **Authors**: Archana Bhise, Prakash D. Vyavahare
- **PDF**: https://ieeexplore.ieee.org/document/6331884
- **Abstract**: Turbo Convolutional Codes (TCC) are widely used to reduce Bit Error Rate (BER) for Second Generation (2G) and Third Generation (3G) wireless networks. However, TCC require large decoding complexity. Recently, Low Density Parity Check Codes (LDPC) have been included in standards for 3G wireless networks. But encoding complexity of LDPC is larger than that of TCC. Modified Turbo codes (MTC) are low complexity turbo-like codes with error performance which is equivalent to that of Turbo codes. However, MTC require 2-dimensional interleavers with large spreading factor and dispersion. In this paper, it is shown that BER of MTC is almost equivalent to TCC. Moreover, MTC decoders require 50% less computations than those of TCC and LDPC. Spreading factor and dispersion for various interleavers are compared. It is observed that 2-stage interleaver achieves large spreading factor and dispersion.

## Distributed Image Encoding Scheme Using LDPC Codes over GF(q) on Wireless Sensor Networks

- **Status**: ❌
- **Reason**: GF(q) 비이진 LDPC + 이미지 분산 인코딩(소스코딩/WSN) - 비이진 제외
- **ID**: ieee:6337920
- **Type**: conference
- **Published**: 19-21 Sept
- **Authors**: Phat Nguyen Huu, Vinh Tran-Quang, Takumi Miyoshi
- **PDF**: https://ieeexplore.ieee.org/document/6337920
- **Abstract**: This work reports an image encoding scheme that distributes low-density parity-check (LDPC) encoding over a prime field of order q, GF(q), on a wireless sensor network (WSN). In the scheme, we divide the input data into several small parts, which are then distributed to multiple nodes to perform a LDPC encoding task in a cluster. We conducted extensive computational simulations to verify our method and found that the LDPC codes over GF(4) achieve a fair trade off between the bit error rate (BER) and power consumption criteria. As a result, the proposed scheme of using LDPC codes over GF(4) not only solves the energy balance problem by sharing processing tasks but also increases the data quality.

## Encoding and decoding for turbo-like codes

- **Status**: ❌
- **Reason**: Turbo↔LDPC 부호 변환·BCJR vs BP 등가성 이론; 떼어낼 신규 바이너리 LDPC 디코더·HW 기법 없음(turbo 중심)
- **ID**: ieee:6335318
- **Type**: conference
- **Published**: 17-19 Sept
- **Authors**: J. Bas
- **PDF**: https://ieeexplore.ieee.org/document/6335318
- **Abstract**: Generally, the major part of communication systems use Turbo Codes (TC) and/or Low-Density Parity-Check (LDPC) codes to protect the data to transmit (e.g. 3GPP-LTE, IEEE 802.11p, IEEE 802.16, etc). Given that these coding strategies share similarities (e.g. two stage iterative decoding, Log-Likelihood Ratio based, etc.) in their respective encoding and decoding parts it is possible to express one code in terms of the other one. However, this conversion has some constraints, which have been formulated in this paper for different structures of convolutional codes. If these constraints are fulfilled the Bit Error Rate (BER) of Turbo Code using Believe Propagation (BP) decoding is quite similar to that offers the Bahl-Cocke-Jelinek-Raviv (BCJR) decoding.

## Secure image databases through distributed source coding of SIFT descriptors

- **Status**: ❌
- **Reason**: SIFT 디스크립터 분산소스코딩(압축)에 LDPC 사용; 채널 ECC 아님(소스코딩)
- **ID**: ieee:6343428
- **Type**: conference
- **Published**: 17-19 Sept
- **Authors**: Athira M. Nambiar, Marco Tagliasacchi, Enrico Magli
- **PDF**: https://ieeexplore.ieee.org/document/6343428
- **Abstract**: The adoption of distributed databases calls for storing data at two or more sites, in order to address application-specific requirements including, e.g., redundancy, data locality, and so on. When visual data (including images, videos and their corresponding descriptors) need to be stored, synchronization across different sites might require significant bandwidth resources. In this paper we explore the use of distributed source coding to encode local SIFT descriptors extracted from static images. The key tenet is to exploit, at the decoder side, the correlation between matching pairs of descriptors extracted, respectively, from the out-of-date and up-to-date image. Preliminary results show that a coding efficiency gain up to 1 bit/descriptor can be achieved in the case of ideal lossless coding. In the case of distributed source coding with LDPC codes, a practical average gain of 0.19 bit/descriptor is observed.

## Experimental demonstration of LDPC coded free-space, space-division-multiplexed systems using Orbital Angular Momentum modes

- **Status**: ❌
- **Reason**: OAM 모드 LDPC 코딩 광링크 실험, LDPC는 베이스라인 적용일 뿐 신규 기법 없음
- **ID**: ieee:6706114
- **Type**: conference
- **Published**: 16-20 Sept
- **Authors**: Yongxiong Ren, Hao Huang, Yequn Zhang +6
- **PDF**: https://ieeexplore.ieee.org/document/6706114
- **Abstract**: The performance of LDPC coded four-mode multiplexed Orbital Angular Momentum (OAM) data link using QPSK signal with net data rate of 320Gbit/s is experimentally investigated. The experiment results show that crosstalk effect can be efficiently mitigated and the LDPC codes with soft decoding can provide >7 dB coding depending on OAM crosstalk.

## Turbo differential decoding failure for a coherent phase slip channel

- **Status**: ❌
- **Reason**: 광통신 위상슬립 채널 turbo differential 디코딩 실패 분석 — 비-LDPC 응용 특이적, 떼어낼 LDPC 기법 없음
- **ID**: ieee:6705899
- **Type**: conference
- **Published**: 16-20 Sept
- **Authors**: A. Bisplinghoff, S. Langenbach, T. Kupfer +1
- **PDF**: https://ieeexplore.ieee.org/document/6705899
- **Abstract**: We study the impact of stressors such as phase slips on the performance of LDPC codes with differentially encoded coherent DP-QPSK, comparing classical soft-decision decoding and iterative (turbo) differential decoding. We find that turbo decoding shows improved baseline performance but suffers from severely reduced phase slip resilience.

## 25 Tb/s transmission over 5,530 km using 16QAM at 5.2 bits/s/Hz spectral efficiency

- **Status**: ❌
- **Reason**: 25Tb/s 광전송 실험, LDPC FEC는 베이스라인, 떼어낼 디코더/구성 기법 없음
- **ID**: ieee:6705906
- **Type**: conference
- **Published**: 16-20 Sept
- **Authors**: J.-X. Cai, H. G. Batshon, H. Zhang +7
- **PDF**: https://ieeexplore.ieee.org/document/6705906
- **Abstract**: We transmit 250×100G PDM RZ 16QAM channels with 5.2 bits/s/Hz spectral efficiency over 5,530 km using single stage C-band EDFAs equalized to 40 nm. We use coded modulation and all channels are decoded with no errors after iterative decoding between a MAP and an LDPC based FEC decoder.

## Casting 1 Tb/s DP-QPSK communication into 200 GHz bandwidth

- **Status**: ❌
- **Reason**: DP-QPSK time-frequency packing 광전송, LDPC 미언급 수준 — 떼어낼 ECC 기법 없음
- **ID**: ieee:6706034
- **Type**: conference
- **Published**: 16-20 Sept
- **Authors**: L. Potì, G. Meloni, G. Berrettini +9
- **PDF**: https://ieeexplore.ieee.org/document/6706034
- **Abstract**: We demonstrate the feasibility of a novel time-frequency packing technique to implement DP-QPSK communication with a record spectral efficiency ranging from 5.14 to 4.3 bit/s/Hz over a distance ranging from 3000 km to 5200 km of uncompensated standard fiber, respectively.

## Advances in signal processing

- **Status**: ❌
- **Reason**: 광 코히어런트 통신 DSP 리뷰 — 서베이, 구체적 신규 LDPC 기여 없음
- **ID**: ieee:6706256
- **Type**: conference
- **Published**: 16-20 Sept
- **Authors**: M. Kuschnerov, O. Agazzi, A. Napoli +11
- **PDF**: https://ieeexplore.ieee.org/document/6706256
- **Abstract**: We review the latest developments and challenges in the field of digital signal processing for state of the art and future optical coherent communications for 400Gb/s and beyond.
