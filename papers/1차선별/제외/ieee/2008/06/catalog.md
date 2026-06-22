# IEEE Xplore — 2008-06


## Application of Nonbinary LDPC Cycle Codes to MIMO Channels

- **Status**: ❌
- **Reason**: 비이진 GF(q) LDPC cycle code — 비이진 LDPC는 제외 대상
- **ID**: ieee:4543051
- **Type**: journal
- **Published**: June 2008
- **Authors**: Ronghui Peng, Rong-Rong Chen
- **PDF**: https://ieeexplore.ieee.org/document/4543051
- **Abstract**: In this paper, we investigate the application of nonbinary low-density parity-check (LDPC) cycle codes over Galois field GF(q) to multiple-input multiple-output (MIMO) channels. Two types of LDPC coded systems that employ either joint or separate MIMO detection and channel decoding are considered, depending on the size of the Galois field and the modulation choice. We construct a special class of nonbinary LDPC cycle codes called the parallel sparse encodable (PSE) codes. The PSE code, consisting of a quasi-cyclic (QC) LDPC cycle code and a simple tree code, has the attractive feature that it is not only linearly encodable, but also allows parallel encoding which can reduce the encoding time significantly. We provide a systematic comparison between nonbinary coded systems and binary coded systems in both performance and complexity. Our results show that the proposed nonbinary system employing the PSE code outperforms not only the binary LDPC code specified in the 802.16e standard, but also the optimized binary LDPC code obtained using the EXIT chart methods. Through a detailed complexity analysis, we conclude that for the MIMO channel considered, the nonbinary coded systems achieve a superior performance at a receiver complexity that is comparable to that of the binary systems.

## Multi-Level Dirty Paper Coding

- **Status**: ❌
- **Reason**: dirty paper coding(멀티레벨 셰이핑) 통신 응용, LDPC는 베이스라인일 뿐 떼어낼 ECC 신규기법 없음
- **ID**: ieee:4542781
- **Type**: journal
- **Published**: June 2008
- **Authors**: Sae-Young Chung
- **PDF**: https://ieeexplore.ieee.org/document/4542781
- **Abstract**: We propose multi-level coding and successive decoding for dirty paper coding (DPC) in the high signal-to-noise ratio (SNR) regime. We divide the channel code into two levels, the upper code interacting with the shaping code and the lower code that does not such that it is information lossless. Our code design is more intuitive for designing DPC in the high SNR regime. The design of the lower code becomes trivial since it does not interact with the shaping code anymore. The design of the upper code is also simplified since we can now assume binary signaling for the code. We evaluate the capacity of each level and design codes to approach the estimated capacity. We demonstrate a good performance can indeed be achieved by simulations using low- density parity-check (LDPC) codes at each level. Our best code is only 0.45 dB from the no-interference Gaussian capacity at the spectral efficiency of 3 b/s/Hz.

## Wireless Information-Theoretic Security

- **Status**: ❌
- **Reason**: 무선 보안 정보조정(reconciliation)용 LDPC - 채널 ECC 아닌 reconciliation, 떼어낼 신규 기법 없음
- **ID**: ieee:4529264
- **Type**: journal
- **Published**: June 2008
- **Authors**: Matthieu Bloch, JoÃo Barros, Miguel R. D. Rodrigues +1
- **PDF**: https://ieeexplore.ieee.org/document/4529264
- **Abstract**: This paper considers the transmission of confidential data over wireless channels. Based on an information-theoretic formulation of the problem, in which two legitimates partners communicate over a quasi-static fading channel and an eavesdropper observes their transmissions through a second independent quasi-static fading channel, the important role of fading is characterized in terms of average secure communication rates and outage probability. Based on the insights from this analysis, a practical secure communication protocol is developed, which uses a four-step procedure to ensure wireless information-theoretic security: (i) common randomness via opportunistic transmission, (ii) message reconciliation, (iii) common key generation via privacy amplification, and (iv) message protection with a secret key. A reconciliation procedure based on multilevel coding and optimized low-density parity-check (LDPC) codes is introduced, which allows to achieve communication rates close to the fundamental security limits in several relevant instances. Finally, a set of metrics for assessing average secure key generation rates is established, and it is shown that the protocol is effective in secure key renewal—even in the presence of imperfect channel state information.

## Decoding with Early Termination for Raptor Codes

- **Status**: ❌
- **Reason**: Raptor(rateless) 코드 조기종료 디코딩 - 비-LDPC 부호이며 rateless 특이적, 바이너리 LDPC BP 직접 이식 불명확
- **ID**: ieee:4542777
- **Type**: journal
- **Published**: June 2008
- **Authors**: Ali Abdulhussein, Anand Oka, Lutz Lampe
- **PDF**: https://ieeexplore.ieee.org/document/4542777
- **Abstract**: Rateless codes, and especially Raptor codes, have received considerable attention in the recent past due to their inherent ability to adapt to channel conditions and their capacity- approaching performance. Since decoding of rateless codes typically involves multiple decoding attempts, early termination of such attempts is mandatory for overall efficient decoding. In this letter, we propose a new decoding scheme with early termination that is particularly suited for rateless codes. Simulation results for the example of the binary symmetric channel show complexity reductions (in terms of the total required number of decoding iterations) by 87% compared to conventional message-passing decoding and 54% compared to a recently proposed incremental decoding scheme for Raptor codes.

## Recovering Sparse Signals Using Sparse Measurement Matrices in Compressed DNA Microarrays

- **Status**: ❌
- **Reason**: compressed sensing/DNA 마이크로어레이 희소신호 복원 — 채널 ECC LDPC 아님
- **ID**: ieee:4550564
- **Type**: journal
- **Published**: June 2008
- **Authors**: Farzad Parvaresh, Haris Vikalo, Sidhant Misra +1
- **PDF**: https://ieeexplore.ieee.org/document/4550564
- **Abstract**: Microarrays (DNA, protein, etc.) are massively parallel affinity-based biosensors capable of detecting and quantifying a large number of different genomic particles simultaneously. Among them, DNA microarrays comprising tens of thousands of probe spots are currently being employed to test multitude of targets in a single experiment. In conventional microarrays, each spot contains a large number of copies of a single probe designed to capture a single target, and, hence, collects only a single data point. This is a wasteful use of the sensing resources in comparative DNA microarray experiments, where a test sample is measured relative to a reference sample. Typically, only a fraction of the total number of genes represented by the two samples is differentially expressed, and, thus, a vast number of probe spots may not provide any useful information. To this end, we propose an alternative design, the so-called compressed microarrays, wherein each spot contains copies of several different probes and the total number of spots is potentially much smaller than the number of targets being tested. Fewer spots directly translates to significantly lower costs due to cheaper array manufacturing, simpler image acquisition and processing, and smaller amount of genomic material needed for experiments. To recover signals from compressed microarray measurements, we leverage ideas from compressive sampling. For sparse measurement matrices, we propose an algorithm that has significantly lower computational complexity than the widely used linear-programming-based methods, and can also recover signals with less sparsity.

## Reliability of flat XOR-based erasure codes on heterogeneous devices

- **Status**: ❌
- **Reason**: XOR 기반 erasure code 신뢰성 배치 최적화로 LDPC ECC 디코더/구성 기법이 아님
- **ID**: ieee:4630083
- **Type**: conference
- **Published**: 24-27 June
- **Authors**: Kevin M. Greenan, Ethan L. Miller, Jay J. Wylie
- **PDF**: https://ieeexplore.ieee.org/document/4630083
- **Abstract**: XOR-based erasure codes are a computationally-efficient means of generating redundancy in storage systems. Some such erasure codes provide irregular fault tolerance: some subsets of failed storage devices of a given size lead to data loss, whereas other subsets of failed storage devices of the same size are tolerated. Many storage systems are composed of heterogeneous devices that exhibit different failure and recovery rates, in which different placements— mappings of erasure-coded symbols to storage devices—of a flat XOR-based erasure code lead to different reliabilities. We have developed redundancy placement algorithms that utilize the structure of flat XOR-based erasure codes and a simple analytic model to determine placements that maximize reliability. Simulation studies validate the utility of the simple analytic reliability model and the efficacy of the redundancy placement algorithms.

## Adaptive LDPC codes for MIMO transceiver with adaptive spectral efficiency

- **Status**: ❌
- **Reason**: 표준 multi-rate LDPC를 MIMO 무선 송수신에 적용, 떼어낼 새 디코더/구성 기법 없음
- **ID**: ieee:4563219
- **Type**: conference
- **Published**: 24-26 June
- **Authors**: Zhiyong He, Roy Sebastien, Paul Fortier
- **PDF**: https://ieeexplore.ieee.org/document/4563219
- **Abstract**: By using a multi-rate low density parity check (LDPC) code, we propose an LDPC coded multiple-input multiple-output (MIMO) transceiver with adaptive spectral efficiency which allows data transmission in wireless networks at rates near the channel capacity with arbitrarily low probability of error. Equipped with multiple transmit and multiple receiver antennae, the proposed LDPC coded MIMO transceiver can maximize either coding gain with space-time diversity technique or channel capacity with space-time multiplexing technique. Since the proposed multi-rate LDPC code is constructed based on a single master parity check matrix using a row-removing approach, a single universal encoder (decoder) suffices to handle all rates. Thus, the proposed approach makes the proposed scheme feasible in a subscriber station, such as a cellular phone, to maximize the total channel capacity with a guaranteed quality-of-service. The simulation results indicate that an LDPC coded MIMO transceiver with a spectral efficiency of 1, 2, 3, 4, and 5 bits/symbol/Hz can achieve extremely reliable transmission in a Rayleigh fading channel at the signal-to-noise ratio (SNR) per bit of −2.5, 0.25, 2, 4.75, and 6.5 dB, respectively, when two transmit and two receiver antennae are used for space-time diversity.

## Fixed-complexity list-type iterative joint detection and decoding of LDPC-coded V-blast systems

- **Status**: ❌
- **Reason**: LDPC-coded V-BLAST의 결합검출/디코딩(sphere decoding)으로 MIMO 검출기 특화, LDPC ECC 기법 아님
- **ID**: ieee:4563258
- **Type**: conference
- **Published**: 24-26 June
- **Authors**: Meng-Ying Tsai, Shahram Yousefi
- **PDF**: https://ieeexplore.ieee.org/document/4563258
- **Abstract**: Soft iterative detection and decoding techniques have been shown to be able to achieve near-capacity performance in multiple antenna systems. To obtain the optimal soft information by marginalizing over the entire observation space is intractable: one must resort to suboptimal methods to implement such receivers. Although list-type detectors such as those founded upon the sphere decoding algorithm provide outstanding error performance, issues such as the optimal initial sphere radius, optimal radius update strategy, and their highly variable computational complexity are still unresolved. In this paper, a new detection scheme is proposed addressing the above issues. Our simulation results show that by sacrificing less than 2 dB at error rate of 10-5, we are able to gain up to 38.6% complexity reduction as well as a detector structure that is more suitable for practical system implementation.

## Feature transformation of biometric templates for secure biometric systems based on error correcting codes

- **Status**: ❌
- **Reason**: 바이오메트릭 보안 저장(syndrome) 응용으로 LDPC가 부수 사용, ECC 채널코딩 기법 아님
- **ID**: ieee:4563111
- **Type**: conference
- **Published**: 23-28 June
- **Authors**: Yagiz Sutcu, Shantanu Rane, Jonathan S. Yedidia +2
- **PDF**: https://ieeexplore.ieee.org/document/4563111
- **Abstract**: Secure storage of biometric templates is extremely important because a compromised biometric cannot be revoked and replaced an unlimited number of times. In many approaches proposed for secure biometric storage, an error correcting code (ECC) is applied to the enrollment biometric and the resulting parity or syndrome symbols are stored on the access control device, instead of the original biometric. The principal challenge here is that most standard ECCs are designed for memoryless channel statistics, whereas the variations between enrollment and probe biometrics have significant spatial correlation. To address this challenge, we propose to transform the original biometric into a feature vector that is explicitly matched to standard ECCs, thereby improving the security-robustness tradeoff of the overall biometric system. As a concrete example, we transform fingerprint minutiae maps into feature vectors compatible with ECCs designed for a binary symmetric channel. We conduct a statistical analysis of these feature vectors and show how our feature transformation algorithm may be combined with Low-Density Parity Check (LDPC) codes to obtain a secure fingerprint biometric system.

## Unsupervised feature selection via distributed coding for multi-view object recognition

- **Status**: ❌
- **Reason**: 분산 코딩 기반 비지도 특징선택(객체인식)으로 LDPC ECC와 무관
- **ID**: ieee:4587615
- **Type**: conference
- **Published**: 23-28 June
- **Authors**: C. Mario Christoudias, Raquel Urtasun, Trevor Darrell
- **PDF**: https://ieeexplore.ieee.org/document/4587615
- **Abstract**: Object recognition accuracy can be improved when information from multiple views is integrated, but information in each view can often be highly redundant. We consider the problem of distributed object recognition or indexing from multiple cameras, where the computational power available at each camera sensor is limited and communication between cameras is prohibitively expensive. In this scenario, it is desirable to avoid sending redundant visual features from multiple views. Traditional supervised feature selection approaches are inapplicable as the class label is unknown at each camera. In this paper we propose an unsupervised multi-view feature selection algorithm based on a distributed coding approach. With our method, a Gaussian process model of the joint view statistics is used at the receiver to obtain a joint encoding of the views without directly sharing information across encoders. We demonstrate our approach on recognition and indexing tasks with multi-view image databases and show that our method compares favorably to an independent encoding of the features from each camera.

## Hybrid ARQ Based on Accumulated Reliabilities and Error Hamming Weights

- **Status**: ❌
- **Reason**: Hybrid ARQ for binary linear block codes over AWGN; ARQ 재전송 throughput 기법으로 LDPC BP에 이식할 디코더 기여 없음
- **ID**: ieee:4603570
- **Type**: conference
- **Published**: 18-20 June
- **Authors**: Hsin-Kun Lai, Erl-Huei Lu
- **PDF**: https://ieeexplore.ieee.org/document/4603570
- **Abstract**: Based on accumulated reliabilities and error Hamming-weights, this paper proposes an error control scheme of hybrid ARQ for binary linear block codes over AWGN channel. The proposed scheme accumulates reliabilities of received word at each retransmission. As a consequence, errors are gradually corrected one after another. Retransmissions continue until the accumulated reliabilities result in a code word after hard decision. Simulation results show that the proposed scheme outperforms ARQ scheme by 30% of throughput efficiency at 4dB of Eb/No and 1dB coding gain in error-correcting performance. Theoretically, the proposed scheme corrects errors beyond minimum Hamming distance between code words. Ideally, the proposed scheme corrects errors as many as code word length in sense of probability.

## Optimum joint decoding in a LDPC-coded CDMA multiuser system

- **Status**: ❌
- **Reason**: LDPC-coded CDMA 다중사용자 joint decoding의 spectral efficiency 이론 평가만; 디코더/HW/구성 신규 기여 없음
- **ID**: ieee:4610864
- **Type**: conference
- **Published**: 17-19 June
- **Authors**: Toru Yano, Toshiyuki Tanaka, David Saad +1
- **PDF**: https://ieeexplore.ieee.org/document/4610864
- **Abstract**: We study a low-density parity-check (LDPC) coded CDMA system. The performance of the system with the optimum joint decoding is analytically evaluated by the spectral efficiency, together with numerical evaluation.
