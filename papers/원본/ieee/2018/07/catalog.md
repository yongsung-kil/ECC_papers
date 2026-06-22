# IEEE Xplore — 2018-07


## Reliability-Based Windowed Decoding for Spatially Coupled LDPC Codes

- **Status**: ✅
- **Reason**: SC-LDPC reliability-based windowed decoding, partial message reservation+부분 신드롬 정지규칙 — 신규 디코더 기법(C)
- **ID**: ieee:8357804
- **Type**: journal
- **Published**: July 2018
- **Authors**: Peng Kang, Yixuan Xie, Lei Yang +1
- **PDF**: https://ieeexplore.ieee.org/document/8357804
- **Abstract**: In this letter, we propose a reliability-based windowed decoding scheme for spatially coupled (SC) low-density parity-check (LDPC) codes. To mitigate the error propagation along the sliding windowed decoder of the SC LDPC codes, a partial message reservation method is proposed where only the reliable messages generated in the previous decoding window are reserved for the next decoding window. We also propose a partial syndrome check stopping rule for each decoding window, in which only the complete variable nodes are checked. Simulation results show that our proposed scheme significantly improves the error-floor performance compared to the sliding windowed decoder with the conventional weighted bit-flipping algorithm.

## Variable-Node-Shift Based Architecture for Probabilistic Gradient Descent Bit Flipping on QC-LDPC Codes

- **Status**: ✅
- **Reason**: PGDBF QC-LDPC용 VNSA HW 아키텍처, ASIC 합성 결과 포함 → D
- **ID**: ieee:8219416
- **Type**: journal
- **Published**: July 2018
- **Authors**: Khoa Le, David Declercq, Fakhreddine Ghaffari +3
- **PDF**: https://ieeexplore.ieee.org/document/8219416
- **Abstract**: Probabilistic gradient descent bit-flipping (PGDBF) is a hard-decision decoder for low-density parity-check (LDPC) codes, which offers a significant improvement in error correction, approaching the performance of soft-information decoders on the binary symmetric channel. However, this outstanding performance is known to come with an augmentation of the decoder complexity, compared to the non-probabilistic gradient descent bit flipping (GDBF), becoming a drawback of this decoder. This paper presents a new approach to implementing PGDBF decoding for quasi-cyclic LDPC (QC-LDPC) codes, based on the so-called variable-node-shift architecture (VNSA). In VNSA-based PGDBF implementations, the regularity of QC-LDPC connection networks is used to cyclically shift the memory of the decoder, leading to the fact that, a variable node (VN) is processed by different computing units during the decoding process. With this modification, the probabilistic effects in VN operations can be produced by implementing different types of processing units, without requirement of a probabilistic signal generator. The VNSA is shown to further improve the decoding performance of the PGDBF, with respect to other hardware implementations reported in the literature, while reducing the complexity below that of the GDBF. The efficiency of the VNSA is proven by ASIC synthesis results and by decoding simulations.

## Recursive Block Markov Superposition Transmission of Short Codes: Construction, Analysis, and Applications

- **Status**: ❌
- **Reason**: BMST/convolutional 부호 구성. SC-LDPC와 비교만 하고 LDPC 기법 자체 기여 아님, 비-LDPC 부호로 제외
- **ID**: ieee:8267104
- **Type**: journal
- **Published**: July 2018
- **Authors**: Shancheng Zhao, Xiao Ma, Qin Huang +1
- **PDF**: https://ieeexplore.ieee.org/document/8267104
- **Abstract**: Extensive studies have demonstrated the effectiveness and the flexibility of constructing capacity-approaching codes by block Markov superposition transmission (BMST). However, to achieve high performance, BMST codes typically require large encoding memories and large decoding window sizes, which result in high decoding complexity and high decoding latency. To address these issues, we introduce the recursive BMST (rBMST), in which the block-oriented feedback convolutional code is used instead of the block-oriented feedforward convolutional code of BMST. We propose to use a modified extrinsic information transfer chart analysis, which relates the mutual information to the bit error rate, to study the convergence behaviors of rBMST codes. On one hand, rBMST code shares most merits of BMST code, including near-capacity performance, low-complexity encoding, and flexible construction. On the other hand, compared with BMST code, rBMST code requires a smaller encoding memory, hence a lower decoding complexity, to approach the capacity. In particular, both analytical and simulation results show that rBMST code with encoding memory three reveals a lower error floor than the BMST code with encoding memory twelve. Furthermore, we show by analysis and simulations that rBMST with fixed encoding memory (m = 3 ) and fixed decoding delay (d = 12 ) can be used to construct capacity-approaching multiple-rate codes. Finally, the comparison between rBMST codes and spatially coupled low-density parity-check codes is carried out, which shows the advantages of rBMST codes in terms of performances and decoding complexities.

## Joint Sparse Graph for FBMC/OQAM Systems

- **Status**: ❌
- **Reason**: FBMC/OQAM NOMA 조인트 스파스 그래프, LDPC는 채널코딩 베이스라인일 뿐 떼어낼 신규 LDPC ECC 기법 없음
- **ID**: ieee:8304665
- **Type**: journal
- **Published**: July 2018
- **Authors**: Lei Wen, Pei Xiao, Razieh Razavi +4
- **PDF**: https://ieeexplore.ieee.org/document/8304665
- **Abstract**: As an advanced nonorthogonal multiple access (NOMA) technique, the low density signature (LDS) has never been used in filter bank multicarrier (FBMC) systems. In this paper, we model a low density weight matrix (LDWM) to utilize the intrinsic interference in FBMC systems when single-tap equalization is employed, and propose a LDS-FBMC scheme which applies LDS to FBMC signals. In addition, a joint sparse graph (JSG) for FBMC named JSG-FBMC is proposed to combine single graphs of LDS, LDWM, and low density parity-check (LDPC) codes which respectively represent techniques of NOMA, multicarrier modulation, and channel coding. By employing the message passing algorithm, a joint receiver performing detection and decoding simultaneously on the joint sparse graph is designed. Extrinsic information transfer charts and construction guidelines of the joint sparse graph are studied. Simulations show the superiority of JSG-FBMC to state-of-the-art techniques such as OFDM, FBMC, LDS-OFDM, LDS-FBMC, and turbostructured LDS-FBMC.

## Information-Propagation-Based Scheduling for the Fast Convergence of Shuffled Decoding

- **Status**: ✅
- **Reason**: shuffled BP의 정보전파 기반 스케줄링으로 수렴 가속 — 부호 비의존 BP 개선 디코더 기법(C), NAND LDPC 이식 가능
- **ID**: ieee:8345637
- **Type**: journal
- **Published**: July 2018
- **Authors**: Taehyun Kim, Jun Heo
- **PDF**: https://ieeexplore.ieee.org/document/8345637
- **Abstract**: This letter presents a scheduling scheme for the fast convergence of shuffled decoding. The messages from the variable node group that is expected to propagate the most reliable information are updated first. Mutual information is used to measure the information reliability. Simulation results show that the average number of iterations is reduced by adopting the proposed schedule, compared with previous scheduling schemes. In addition, information-theoretic analysis results show that mutual information in the proposed scheme increases faster than in the previous scheme.

## Parameter-Free  $\ell_p$ -Box Decoding of LDPC Codes

- **Status**: ✅
- **Reason**: LDPC ADMM lp-box 디코딩의 파라미터-프리 변형, error floor 개선 디코더 알고리즘(C)
- **ID**: ieee:8352866
- **Type**: journal
- **Published**: July 2018
- **Authors**: Qiong Wu, Fan Zhang, Hao Wang +2
- **PDF**: https://ieeexplore.ieee.org/document/8352866
- **Abstract**: The alternating direction method of multipliers (ADMMs) decoding of low-density parity-check codes has received many attentions due to its excellent performance at the error floor region. In this letter, we develop a parameter-free decoder based on linear program decoding by replacing the binary constraint with the intersection of a box and an ℓp sphere. An efficient ℓ2-box ADMM is designed to handle this model in a distributed fashion. Numerical experiments demonstrate that our decoder attains better adaptability to different signal-to-noise ratio and channels.

## Time-to-Space Division Multiplexing for Tb/s Mobile Cells

- **Status**: ❌
- **Reason**: mmWave 빔 스티어링 time-to-space 다중화 HW, LDPC/ECC 무관
- **ID**: ieee:8356241
- **Type**: journal
- **Published**: July 2018
- **Authors**: Romain Bonjour, Samuel Welschen, Juerg Leuthold
- **PDF**: https://ieeexplore.ieee.org/document/8356241
- **Abstract**: Space division multiplexing increases the capacity of mobile cells by reusing the frequencies in various directions. Yet, today's concepts scale badly to millimeter wave and therefore cannot provide Tb/s capacity. In this paper, we introduce time-to-space division multiplexing as a novel scheme to steer multiple beams simultaneously to different users. The main benefit of the proposed method relies in the fact that simple hardware can be used to generate the beams. In other words, it provides the advantages of space division multiplexing without relying on the complex array feeders that are usually required. Thanks to this advantage, the proposed technique can be easily combined with millimeter Wave systems as recently demonstrated.

## 10 Pbit/s Transmission Using Space-Division-Multiplexing

- **Status**: ❌
- **Reason**: 광섬유 SDM 전송 실험 리뷰, LDPC ECC 기법 없음
- **ID**: ieee:8456760
- **Type**: conference
- **Published**: 9-11 July 
- **Authors**: Itsuro Morita, Daiki Soma, Takehiro Tsuritani
- **PDF**: https://ieeexplore.ieee.org/document/8456760
- **Abstract**: Space-division-multiplexing is a promising technology to increase a system capacity drastically and the highest capacity in a single optical fiber has reached to 10 Pbit/s recently. In this paper, we review 10.16 Pbit/s transmission experiment using 6-mode 19-core fiber.

## A Low-Complexity Method for Evaluating the Distance Spectrum of Polar Codes

- **Status**: ❌
- **Reason**: polar 부호 거리스펙트럼 평가, 부호 비의존적 LDPC BP 이식 기법 없음(비-LDPC 제외)
- **ID**: ieee:8516712
- **Type**: conference
- **Published**: 9-11 July 
- **Authors**: Guo Tai Chen, Lei Cao, Kangjian Qin +1
- **PDF**: https://ieeexplore.ieee.org/document/8516712
- **Abstract**: Different from linear block codes that may use one single generator matrix for different channel conditions, polar codes have different generator matrices for different channel conditions. Few papers investigated polar codes from the view of different distance spectrum associated with different generator matrices. Successive cancellation list (SCL) decoding was proposed to evaluate the distance spectrum of polar codes. However, the large memory requirement of SCL decoding using a large number of survival paths can be beyond the memory constraint of normal computers. One practical method to evaluate the distance spectrum of polar codes with SCL decoding was implemented with the aid of hard disk to store the immediately generated data. In this paper, we modify the algorithm of SCL decoding proposed by Tal and Vardy to largely reduce the time complexity and the required space in hard disk. With this method, we further investigate the distance spectrum of polar codes with length N = 128 and N = 256, respectively.

## The Design and Implementation of High-Speed Codec Based on FPGA

- **Status**: ✅
- **Reason**: FPGA QC-LDPC 코덱; QC->블록QC 변환으로 병렬화·고처리율 HW 아키텍처(D) 이식 가능
- **ID**: ieee:8488239
- **Type**: conference
- **Published**: 6-9 July 2
- **Authors**: Weiji Ren, Hao Liu
- **PDF**: https://ieeexplore.ieee.org/document/8488239
- **Abstract**: This article mainly proposes a high-speed encoding and decoding method for LDPC code on FPGA. This method converts a quasi-cyclic LDPC code into a block quasi-cyclic LDPC code, and uses a similar transformation to generate a corresponding generator matrix, thereby improving the parallelism of encoder and decoder and making them have high throughput. Finally, we implemented high-speed encoding and decoding on the FPGA chip of the Kintex7 system by using the CCSDS-recommended (8176, 7154) LDPC code, and these encoder and decoder achieve a throughput of 2.97 Gbps under the condition of 5 iterations.

## High Reliability NoC switch using Modified Hamming Code with Transient Faults

- **Status**: ❌
- **Reason**: Modified Hamming Code 기반 NoC 결함정정. 비-LDPC 부호, 이식 가능 LDPC 기법 없음.
- **ID**: ieee:8541202
- **Type**: conference
- **Published**: 6-7 July 2
- **Authors**: Siva Kanakala, K Ashok Kumar, P Dananjayan
- **PDF**: https://ieeexplore.ieee.org/document/8541202
- **Abstract**: The scaling of technology decreases the communication issues between components in the System on Chip (SoC). Network on Chip (NoC) has the new architecture to deal with the overheads of communication and it is build with routers and processing elements. The router of NoC is temporarily and/or permanently disabled due to the occurrence of faults. A disabled router gives severe impact on the entire system hence the correction of faults is curial not only for single router but also entire NoC system. A Modified Hamming Code (MHC) is presented for detection and correction transient faults. The encoded data input is categorized in groups and each MHC is applied to each group parallelly there by provides high reliability of this method. The simulation results prove that MHC yields reduced latency and increased speed when compared to conventional Hamming Code (HC).

## Performance Comparison of Parallel Concatenated Gallager Codes with Different Types of Interleavers

- **Status**: ❌
- **Reason**: PCGC(LDPC 성분코드 turbo형 병렬연접)+인터리버 비교로, 표준 LDPC 사용 및 인터리버 성능평가 수준, 새 디코더/구성 기여 없음
- **ID**: ieee:8531011
- **Type**: conference
- **Published**: 5-7 July 2
- **Authors**: G P Aswathy, K Gopakumar, Niyas K Haneefa
- **PDF**: https://ieeexplore.ieee.org/document/8531011
- **Abstract**: Parallel concatenated Gallager code (PCGC) is a class of concatenated code in which Low density parity check (LDPC) codes are used as component codes in interleaver-free Turbo code architecture. These codes were introduced in order to reduce the encoding and decoding complexity of long block length LDPC codes. In this paper, we evaluate the performance of PCGC along with an interleaver included, as in Turbo code architecture. Basically, we compare the performance of PCGC with random interleaver and some structured interleavers in binary symmetric channel (BSC). It is shown that PCGC with random interleaver outperforms a dedicated LDPC of same frame length and code rate over BSC. Simulation results show that structured interleavers almost achieved the performance of random interleaver for short frame length codes. Furthermore, the application of PCGC with interleaver for cognitive radio data transmission is also discussed.

## Simulated Annealing Method for Construction of High-Girth QC-LDPC Codes

- **Status**: ✅
- **Reason**: high-girth QC-LDPC 구성 신규 기법(시뮬레이티드 어닐링), 카테고리 E 코드설계 이식 가능
- **ID**: ieee:8441303
- **Type**: conference
- **Published**: 4-6 July 2
- **Authors**: Vasiliy Usatyuk, Ilya Vorobyev
- **PDF**: https://ieeexplore.ieee.org/document/8441303
- **Abstract**: We present a simulated annealing method that construct high-girth quasi-cyclic low-density parity check (QC-LDPC) codes. The proposed method is applicable to both regular and irregular protograph codes. The method show improvement in term of minimal circulant size compare with previous described methods: Hill-Climbing and improved PEG. Simulated results are presented to demonstrate performance gain of proposed construction method in error-floor region under base graph 2 (BG2) using 5G eMBB standard length adaption method.

## DEVELOPMENT OF THE LDPC CODER-DECODER OF THE DVB-S2 STANDARD ON FPGA

- **Status**: ✅
- **Reason**: DVB-S2 LDPC 인코더/디코더 FPGA 구현 및 성능/자원 개선 아키텍처, 카테고리 D HW 이식 가능
- **ID**: ieee:8456924
- **Type**: conference
- **Published**: 4-5 July 2
- **Authors**: M. Yu. Zinchenko, A. M. Levadniy, Yu. A. Grebenko
- **PDF**: https://ieeexplore.ieee.org/document/8456924
- **Abstract**: Forward error correction (FEC) is a mandatory step in the processing of information in modern digital communication channels. Encoding methods are constantly improved. Today's most popular FEC codes are low-density parity check codes (LDPC).The paper presents the results of the development on the FPGA the encoder and the decoder of LDPC codes compatible with the standard DVB-S2. Parametrized FE modules with the ability to use several coding rates and two frames types of the standard were developed. In this paper, proposed architectures of coder and decoder, methods for improving performance and used resources of FPGA are presented.

## Estimation of capabilities of cooperative CubeSat systems based on Alamouti transmission scheme

- **Status**: ❌
- **Reason**: CubeSat 협력전송/Alamouti 코딩 평가, LDPC 부수 언급, 떼어낼 LDPC 기법 없음
- **ID**: ieee:8456940
- **Type**: conference
- **Published**: 4-5 July 2
- **Authors**: Z. S. Gibalina, V. A. Fadeev, K. A. Korsukova +2
- **PDF**: https://ieeexplore.ieee.org/document/8456940
- **Abstract**: Due to the size constraints of the CubeSat satellites and hence the limited capabilities in terms of battery power and solar panel's area, highly energy efficient transmission schemes are required. However, we can consider CubeSat satellites as a prospective tool for communication. In this case the effective transmission channels between CubeSats and a ground station should be optimized in terms of energy efficiency, robustness, Bit Error Ratio performance and capacity. One of the approaches to reduce the required energy consumption is to reduce the required Signal-to-Noise Ratio. We evaluate different coding schemes including LDPC and space-time codes. Due to the limited size of the CubeSat systems the use of cooperative schemes can be beneficial and shall be considered. Cooperative schemes in this context are schemes, in which several devices are virtually treated as to be a single one. Different system models for cooperative communication and basic results of the link budget calculation are presented in the introduction. A comparison of the Bit-Error- Ratio performance for different cases of using Alamouti codes as well as inter-satellite link budget calculations are shown in the main part of this paper.

## Comparative evaluation of received signal parameters in SFN DVB-T2 service area

- **Status**: ❌
- **Reason**: DVB-T2 SFN 수신 신호 파라미터 측정 평가, ECC 기법 없음
- **ID**: ieee:8456937
- **Type**: conference
- **Published**: 4-5 July 2
- **Authors**: M. I. Iacob, Yu. I. Demciuc, I. A. Avraam
- **PDF**: https://ieeexplore.ieee.org/document/8456937
- **Abstract**: In this article are presented theoretical principles with coding of frequency multiplexing of orthogonal carrier frequencies. Was performed a comparative evaluation of the qualitative parameters of the DVB-T2 signal in the synchronous network service area. The analysis is based on the results of field measurements performed in the central zone of the Republic of Moldova, where digital terrestrial television functioning on 31 television channel.

## Performance Improvement of Optical Satellite Communications by Interleaved IEEE 802.11 LDPC

- **Status**: ❌
- **Reason**: 광위성통신에 표준 IEEE 802.11 LDPC+인터리빙 적용. 표준 부호 단순 재사용, 신규 디코더/구성 기여 없음
- **ID**: ieee:8436720
- **Type**: conference
- **Published**: 3-6 July 2
- **Authors**: Duy Thong Nguyen, Youngil Park
- **PDF**: https://ieeexplore.ieee.org/document/8436720
- **Abstract**: Optical wireless communication using a laser is a strong candidate for the next generation satellite communications due to its large bandwidth. However, the channel environment of satellite communications is very tough, suffering from fading by atmospheric turbulence. Therefore, a powerful channel coding such as low-density parity check (LDPC) code is required for error correction. In this paper, the performance of a LDPC code is evaluated in this harsh channel environment. At the same time, in order to improve the system performance further, an interleaving method in combination with a LDPC code is used to overcome the burst error problem, which frequently occurs in optical satellite communication systems (OSC). Simulation results show that 970 consecutive burst error bits can be recovered by using a large size LDPC code and the proposed type of interleaving.

## Efficient Reconciliation Protocol with Polar Codes for Quantum Key Distribution

- **Status**: ❌
- **Reason**: QKD 정보조정용 polar code soft-output 디코더. 비-LDPC 부호+정보조정, 떼어낼 바이너리 LDPC 기법 없음
- **ID**: ieee:8436787
- **Type**: conference
- **Published**: 3-6 July 2
- **Authors**: Sunghoon Lee, Jun Heo
- **PDF**: https://ieeexplore.ieee.org/document/8436787
- **Abstract**: Information reconciliation is a critical process of any Quantum Key Distribution (QKD) protocol, where two legitimate parties agree on a secret key. Two parties attempt to eliminate the discrepancies between their correlated keys in the presence of an adversary, while revealing a minimum amount of information. In this paper, we propose a reconciliation protocol using polar codes with a soft-output decoder. We demonstrate that our method is better than a conventional protocol using polar codes in the view of reconciliation efficiency.

## Implementation of Plug & Play Quantum Key Distribution Protocol

- **Status**: ❌
- **Reason**: Plug&Play QKD 프로토콜 실험 구현. ECC/LDPC 디코더 기법 무관
- **ID**: ieee:8436633
- **Type**: conference
- **Published**: 3-6 July 2
- **Authors**: Byungkyu Ahn, Jinyoung Ha, Youngjin Seo +3
- **PDF**: https://ieeexplore.ieee.org/document/8436633
- **Abstract**: This paper represents an experimental implementation of the “Two way Plug & play” quantum key distribution (QKD) protocol, which uses weak coherent pulses at a single photon level to transfer key information from Alice to Bob via the quantum channel. In this experiment, we applied the 25km optical fiber channel and the results show a quantum bit error rate (QBER) of about 3%.

## AL-FEC Application on NGMN-Edge Computing Integrated Systems

- **Status**: ❌
- **Reason**: RaptorQ AL-FEC (fountain/erasure 코드) 엣지컴퓨팅 응용 - 비-LDPC 부호, 떼어낼 LDPC ECC 기법 없음
- **ID**: ieee:8437004
- **Type**: conference
- **Published**: 3-6 July 2
- **Authors**: Christos Bouras, Nikolaos Kanakis
- **PDF**: https://ieeexplore.ieee.org/document/8437004
- **Abstract**: Edge computing or edge networking is an architecture that uses one or more collaborative multitude of end-user clients or near-user edge devices to carry out a substantial amount of communication, control, management or other operations. Edge Computing for mobile networks is a new technology which is currently under standardization providing an IT service environment and cloud-computing capabilities at the edge of the mobile network in close proximity to the mobile end users. The aim of this technology is to reduce latency, ensure highly efficient network operation and service delivery, providing improved user experience. All of these can be translated into value and can create opportunities for operators, application and content providers enabling them to better utilize the mobile broadband capabilities. Furthermore, edge computing enables a new value chain for end users but also for industries allowing to efficient deliver their applications over the mobile network providing fresh business opportunities and new use cases. FEC is a feedback free error recovery method where the sender introduces redundant data in advance with the source data enabling the recipient to recover from different arbitrary packet losses. Recently, the adoption of FEC error control method has been boosted by the introduction of the powerful RaptorQ Application Layer FEC (AL-FEC) codes. In this work we propose the integration of AL-FEC error protection application at the edge layer. We propose a novel AL-FEC application architecture scheme based on RaptorQ codes and we analyze the performance enhancements such an error control architecture can introduce on Next Generation Mobile Networks (NGMN)-edge computing integrated systems.

## FPGA Implementation Scheme of Mixed Logarithmic Domain FFT-BP Decoding Algorithm Based on Non-Binary LDPC Codes

- **Status**: ❌
- **Reason**: 비이진 NB-LDPC FFT-BP FPGA 디코더 — 비이진 LDPC는 제외 대상
- **ID**: ieee:8483120
- **Type**: conference
- **Published**: 25-27 July
- **Authors**: Ziyong Wang, Jiahui Meng, Zhibin Deng +2
- **PDF**: https://ieeexplore.ieee.org/document/8483120
- **Abstract**: In this paper, an improved decoding algorithm for Non-binary low density parity check (NB-LDPC) codes with low decoding complexity and suitable for field-programmable gate array (FPGA) implementation is proposed, which is a mixed logarithmic domain FFT-BP decoding algorithm (Mixed Log-FFT-BP) for the problem of high complexity of the existing decoding algorithms for Non-binary LDPC codes. The algorithm combines the traditional Log-BP algorithm with the FFT-BP algorithm, and simplifies the update of the check nodes in the iterative decoding process. A large number of convolution operations are converted into multiplication operations in frequency domain by using FFT transform and IFFT transform. The multiplication of the original FFT-BP algorithm is converted into the addition and look-up table operations in the logarithmic domain. Then, the logarithm of the probability information is directly solved, so that it can be decoded in the logarithmic domain, which saves the computation of the log likelihood ratio, and then reduces the complexity. Simulation results show that under the additive Gauss white noise channel, when the bit error rate is 10-5, compared with BP algorithm, Log-Bp algorithm and FFT-BP algorithm, the performance of Mixed Log-FFT-BP algorithm is not decreased, and all of them remain within the range of 0.1-0.2dB.

## Weighted Symbol Flipping Decoding for Non-binary LDPC Codes Based on Iteration Stopping Criterion

- **Status**: ❌
- **Reason**: 비이진 NB-LDPC 가중 심볼플리핑 디코더 — 비이진 LDPC는 제외 대상
- **ID**: ieee:8483599
- **Type**: conference
- **Published**: 25-27 July
- **Authors**: Haiwei Mu, Jiahui Meng, Liang Zhang +2
- **PDF**: https://ieeexplore.ieee.org/document/8483599
- **Abstract**: To speed up the convergence rate of non-binary low-density parity check codes and reduce decoding computational complexity of decoding algorithm, a weighted symbol flipping decoding algorithm based on iterative stopping criteria is proposed. The algorithm determines the position and amplitude of the flipped symbol according to the weight of the information node and the flipping function in the check equation, and selects the optimal value of the weighting factor through simulation. At the same time, the iteration stop criterion is introduced, and the iteration is stopped by setting the number of parity equations without satisfying the different signal-to-noise ratio. The simulation results show that the channel additive white Gauss noise, the algorithm ensures the invariant properties of weighted symbol flipping decoding algorithm under the condition that can accelerate the convergence speed, reduce the average number of iterations, so the decoding performance and complexity trad-off between effective.

## Evaluation of LDPC Code and Polar Code Coding Scheme in 5G Technology – Massive Machine Type Communication

- **Status**: ❌
- **Reason**: 초록이 키워드 나열뿐인 5G LDPC/polar 코딩 비교 평가로 떼어낼 구체적 디코더/구성/HW 기여 식별 불가
- **ID**: ieee:8534937
- **Type**: conference
- **Published**: 24-26 July
- **Authors**: Guntur Kuntoro Prayogo, Reihan Putra, Akmal Hugo Prasetyo +1
- **PDF**: https://ieeexplore.ieee.org/document/8534937
- **Abstract**: The following topics are dealt with: Internet; learning (artificial intelligence); feature extraction; optimisation; social networking (online); pattern classification; mean square error methods; decision making; smart phones; and distributed power generation.

## FPGA Implementation of High-Speed LDPC Codec for Wireless Laser Communication

- **Status**: ❌
- **Reason**: CCSDS 표준 LDPC를 무선 레이저통신에 FPGA로 단순 구현, 새 디코더/HW 기여 없는 표준 코덱 적용
- **ID**: ieee:8612730
- **Type**: conference
- **Published**: 20-22 July
- **Authors**: Xiaoshuai Jin, Hao Liu
- **PDF**: https://ieeexplore.ieee.org/document/8612730
- **Abstract**: With the improvement of the theory and the rapid development of the technology of laser communication, wireless laser communication has wider application fields. At the same time, people's requirements of information transmission rate in the communication system are constantly improving. Thus, Low Density Parity Check (LDPC) codes have become the first selection of channel coding with its excellent performance of error correction and low implementation complexity, but how to realize the efficient encoding and decoding of LDPC codes is the difficulty of the research. The encoding and decoding technology of LDPC codes as well as the wireless laser communication technology are the important issues. This paper will combine with these and mainly studies the actual application of LDPC codes in wireless laser communication. Then the codec of LDPC codes based on the CCSDS standard on the condition of high-speed communication is implemented with FPGA and the throughput can reach 2.5Gbps.

## Ultra High-Capacity Transmission Using Space-Division-Multiplexing

- **Status**: ❌
- **Reason**: SDM 광전송 용량, ECC/LDPC 기법 없음
- **ID**: ieee:8729935
- **Type**: conference
- **Published**: 2-6 July 2
- **Authors**: Itsuro Morita, Daiki Soma, Takehiro Tsuritani +1
- **PDF**: https://ieeexplore.ieee.org/document/8729935
- **Abstract**: Space-division multiplexing is a promising technology enabling significant growth of a fiber capacity. By using a combination of SDM and DWDM in C+L bands, the fiber capacity has recently reached to 10.16 Pbit/s.

## Research of LDPC Coding and Encoding for Satellite Communication

- **Status**: ❌
- **Reason**: 표준 QC-LDPC와 표준 LLR-BP를 위성통신에 그대로 적용; 새 디코더/구성 기여 없음(표준 기법 단순 재사용)
- **ID**: ieee:9045733
- **Type**: conference
- **Published**: 19-21 July
- **Authors**: Ning Liu, Xiaohang Ren, Yunhe Liu +1
- **PDF**: https://ieeexplore.ieee.org/document/9045733
- **Abstract**: As the increasing demands of spatial frequency resources, more and more geostationary satellites use Ka-band to realize high-speed data transmission. The data transmission link has characteristics of long distance and high rain attenuation. For the convenience of data processing and improving the performance of codecs, quasi - cyclic LDPC (QC-LDPC) and log - likelihood ratio decoding (LLR-BP) algorithms are designed. This paper mainly studies the coding and decoding algorithm of LDPC, proposes the overall optimized design method of the satellite communication system, finally gives the verification results of a nearly launched geostationary orbit satellite.

## Performance Evaluation and Improvement of PER and Throughput in Galvanic-Coupling Intra-Body Communication Systems

- **Status**: ❌
- **Reason**: 갈바닉 인체통신 PER/throughput 평가에 표준 LDPC 적용; 무선 응용 특이적, 새 기법 없음
- **ID**: ieee:8513354
- **Type**: conference
- **Published**: 18-21 July
- **Authors**: Kenichi Ito
- **PDF**: https://ieeexplore.ieee.org/document/8513354
- **Abstract**: This study examined the following communication characteristics of contact and partially non-contact galvanic intra-body communication (IBC) systems using a human-body path loss model developed previously: 1) packet error rate (PER) calculation for the contact and partially non-contact IBC path, and PER improvement by the low-density parity check (LDPC) error correction code; and 2) signal-to-noise ratio (SNR) estimation using the blind SNR prediction method and throughput optimization using adaptive coding. The following results were obtained for these characteristics: 1) Applying the LDPC coding rate 3/4 through 1/4 can improve the required SNR by approximately 8~20 dB when PER = 10-2; and 2) the blind SNR prediction method can estimate SNR precisely, thus realizing appropriate throughput communication.

## An Implementation of Maximum Likelihood Decoder for Error-File Recovery on Cloud Storage System

- **Status**: ❌
- **Reason**: 클라우드 스토리지용 CGR/MDS erasure 코드 + ML 디코더; 비-LDPC 부호이며 이식 가능 LDPC 기법 없음
- **ID**: ieee:8619946
- **Type**: conference
- **Published**: 18-21 July
- **Authors**: Pakpoom Sangprasittichok, Nattakan Puttarak
- **PDF**: https://ieeexplore.ieee.org/document/8619946
- **Abstract**: Cloud storage system is a distributed storage system which stores data in many disks on the Internet. In order to achieve more reliable data and improve performance of the storage system, an erasure code is invented and applied to cloud storage system wherein the user's data will be stored online through the Internet. This paper applies the complete graph of ring (CGR) codes [7], which is a maximum distance separable (MDS) code, and implements in cloud storage system. Moreover, the maximum likelihood decoder (MLD) is also applied and implemented on the receiver to detect and correct errors due to noisy channel. In this paper, the grey-scale images/files are randomly stored on distributed cloud storage, then sent via communications channel, and finally read by receivers. The result shows that the receiver operated with the MLD outperforms by giving the lower BER.

## IEEE 802.11ax: On Performance of Multi-Antenna Technologies with LDPC Codes

- **Status**: ❌
- **Reason**: 802.11ax 무선에서 LDPC vs BCC 성능비교, 표준 LDPC 부수 언급일 뿐 떼어낼 신규 기법 없음
- **ID**: ieee:8465732
- **Type**: conference
- **Published**: 18-20 July
- **Authors**: Roger Pierre Fabris Hoefel
- **PDF**: https://ieeexplore.ieee.org/document/8465732
- **Abstract**: The implementation of low-density parity-check (LDPC) codes will be a mandatory feature in the 2019 IEEE 802.11ax amendment, the sixth generation of wireless local area networks (WLANs) for frequencies below 6 GHz. Orthogonal frequency division multiplexing multi-user multiple-input multiple-output (OFDM MU-MIMO) technologies for both downlink and uplink have been specified in Task Group (TG) 802.11ax meetings to improve the spectrum and area efficiency in ultra-dense WLANs. In this paper, we compare the performance of binary convolutional codes (BCC) and LDPC codes using different configurations of multi-antenna technologies taking into account both hardware and system impairments. We have concluded that on the most study cases, the implementation of LDPC codes in the IEEE 802.11ax physical layer allows power gains between 2.5 and 4.0 dB in relation to BCC with soft-decision Viterbi decoding.

## The Design of Low-Iteration Protograph Codes for Rayleigh Fading Channels with Spatial Diversity

- **Status**: ❌
- **Reason**: Rayleigh fading+공간다이버시티 전용 protograph 설계, NAND 무관 채널특화로 이식할 일반기법 없음
- **ID**: ieee:8465765
- **Type**: conference
- **Published**: 18-20 July
- **Authors**: Thuy V. Nguyen, Hieu T. Nguyen
- **PDF**: https://ieeexplore.ieee.org/document/8465765
- **Abstract**: The contribution of this paper is to propose a new design framework for good low-iteration protograph low density parity check (LDPC) codes for fading channels where space spatial diversity is feasible. The performance of a protograph code of rate 1/2 proves that a power gain of 0.4 dB is achieved at frame error rate (FER) of 10−4 in comparison with the counterpart protograph accumulate-repeat-by-3-accumulate (AR3A) code, which has been shown to have the best performance in the fading environment [1]. Such power gain is meaningful for battery-operated devices in wireless communications systems.

## A Novel Truncation Rule for the EMS Decoding of Non-binary LDPC Codes

- **Status**: ❌
- **Reason**: 비이진 NB-LDPC EMS 디코더 truncation 기법 — non-binary는 제외 대상
- **ID**: ieee:8724394
- **Type**: conference
- **Published**: 16-19 July
- **Authors**: Kuntal Deka, A. Rajesh, P. K. Bora
- **PDF**: https://ieeexplore.ieee.org/document/8724394
- **Abstract**: This paper presents a novel truncation rule for the extended min-sum (EMS) decoding of non-binary low-density parity-check (NB-LDPC) codes. The conventional NB-LDPC decoders involve vector-messages of length equal to the field size q. The complexity of these decoders increases significantly as q increases. In the EMS algorithm, the vector-messages are truncated by discarding the less-likely symbols. In this paper, we propose a truncation rule so that the lengths of the vector-messages are reduced to the so-far best limit without compromising on the error correction capability. We devise a proximity matrix which helps to identify the essential components of a vector-message for truncation. The proposed truncation rule has been applied to several NB-LDPC codes of different field sizes. Simulation results for these codes show that the proposed rule can achieve the maximum truncation with negligible performance loss.

## LDPC Codes Derived from Quasi-cyclic Code Design Suitable for Optical Communications

- **Status**: ✅
- **Reason**: SC-LDPC from QC-LDPC 신규 구성 + FPGA HW + error floor 개선 — 바이너리 LDPC 코드설계/HW 이식 가능 (E/D)
- **ID**: ieee:8473793
- **Type**: conference
- **Published**: 1-5 July 2
- **Authors**: Xiaole Sun, Ivan B. Djordjevic
- **PDF**: https://ieeexplore.ieee.org/document/8473793
- **Abstract**: We propose a rate-adaptive forward error correction (FEC) scheme based on spatially-coupled (SC) LDPC codes derived from quasi-cyclic (QC) LDPC codes with its field-programmable gate array (FPGA) architecture. By FPGA emulation, we show that, with comparable computational complexity, the proposed LDPC codes provide larger coding gain and smaller error floor compare to the QC-LDPC base code. As a result, due to its hardware friendly structure, they are presented to be a promising candidate for the next-generation intelligent optical communication systems such as long-haul optical transmission system.

## Probabilistically Shaped 8-PAM Suitable for Data Centers Communication

- **Status**: ❌
- **Reason**: 데이터센터용 확률성형 8-PAM, 소스분포/MI 분석 중심이고 LDPC는 베이스라인, 떼어낼 디코더/코드 기법 없음
- **ID**: ieee:8473738
- **Type**: conference
- **Published**: 1-5 July 2
- **Authors**: Xiao Han, Ivan B. Djordjevic
- **PDF**: https://ieeexplore.ieee.org/document/8473738
- **Abstract**: We study non-uniform 8-PAM signaling schemes, based on Maxwell-Boltzmann and exponential source distributions, as candidates suitable for data centers’ communications. We evaluate mutual information of these schemes against corresponding uniform 8-PAM scheme, for different parameters of source distributions. The properly chosen variable parameters for different SNR-regions allows us to closely approach Shannon limit, and to significantly outperform the corresponding uniform counterpart. We demonstrate that LPDC-coded 8-PAM with exponential distribution outperforms the LDPC-coded 8-PAM with uniform distribution of the same achievable information rate by 1.8 dB, and this improvement is comparable to that obtained from mutual information calculations.
