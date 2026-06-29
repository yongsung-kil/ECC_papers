# IEEE Xplore — 2007-08


## Pilotless Frame Synchronization via LDPC Code Constraint Feedback

- **Status**: ❌
- **Reason**: LDPC 제약 피드백 이용 파일럿리스 프레임 동기화 - 통신 수신기 동기화 응용, 떼어낼 ECC 디코더/코드설계 기법 없음
- **ID**: ieee:4290002
- **Type**: journal
- **Published**: August 200
- **Authors**: Dong-U Lee, Hyungjin Kim, Christopher R. Jones +1
- **PDF**: https://ieeexplore.ieee.org/document/4290002
- **Abstract**: In traditional receiver architectures, frame synchronization is performed using pilot symbols and a correlation rule. In this paper we show that outputs from the constraint node side of a bipartite decoding graph can be used to achieve frame synchronization in a pilotless low-density parity-check (LDPC) coded transmission, thereby avoiding the bandwidth cost inherent in use of pilot symbols. The complexity of the frame synchronizer is kept relatively low due to its XOR-based approach.

## Rate Quantization and Cross-Layer Design of Multiple-Antenna Base Stations with Transmit MMSE and Imperfect CSIT

- **Status**: ❌
- **Reason**: MISO 다중안테나 rate quantization/cross-layer 스케줄링 - 무선 통신 응용, LDPC 무관
- **ID**: ieee:4290037
- **Type**: journal
- **Published**: August 200
- **Authors**: Vincent K. N. Lau, M. L. Jiang
- **PDF**: https://ieeexplore.ieee.org/document/4290037
- **Abstract**: In this paper, the downlink rate quantization and cross-layer scheduling design are investigated in multiuser multiple-input single-output (MISO) systems with imperfect channel state information at transmitter (CSIT). We shall propose a systematic analytical design framework based on information theoretical approach. To capture the effect of the potential packet outage, we introduce the average system goodput, which measures the average b/s/Hz delivered to the mobiles successfully, as the system performance objective. Numerical results demonstrate that, by considering the statistics of CSIT errors into the design, the proposed scheduling scheme provides significant performance enhancement.

## Performance Investigation of Soft-Decodable Runlength-Limited Codes With Different Minimum Runlength Constraints in High-Density Optical Recording

- **Status**: ❌
- **Reason**: 광학기록 RLL 부호 d제약 성능평가; LDPC는 베이스라인일 뿐 떼어낼 신규 디코더/구성 기법 없음
- **ID**: ieee:4277919
- **Type**: journal
- **Published**: Aug. 2007
- **Authors**: Haibin Zhang, Andries P. Hekstra, Wim M. J. Coene +1
- **PDF**: https://ieeexplore.ieee.org/document/4277919
- **Abstract**: This paper investigates the performance of runlength-limited (RLL) codes with different d constraints in high-density optical recording, for both the low-density parity-check (LDPC)-coded Bliss scheme and the standard concatenation scheme. For the d = 5 constraint, we propose a low-complexity compression/decompression scenario that maps each 6-bit channel codeword to a 3-bit "compressed codeword" by Gray-alike coding of the position of the transition in the 6-bit codeword, to compensate the density loss introduced by the redundancy of LDPC coding in the LDPC-coded Bliss scheme. Using a scalar diffraction channel model, we ran simulations to compare the performance of RLL codes with four different d constraints: d = 0,1,2, and 5, in near-field optical recording systems. The simulation results address the average bit error number in erroneous symbols after soft-input soft-output channel detection. Further, we evaluated the net density with different sets of simulation parameters, for both the LDPC-coded Bliss scheme and the standard concatenation scheme, considering jitter noise and additive white Gaussian noise, respectively.

## Applications of LDPC Codes to the Wiretap Channel

- **Status**: ❌
- **Reason**: wiretap/QKD 보안용 secrecy LDPC 부호 설계; 채널 ECC가 아닌 보안·정보조정 응용으로 원칙 제외
- **ID**: ieee:4276938
- **Type**: journal
- **Published**: Aug. 2007
- **Authors**: Andrew Thangaraj, Souvik Dihidar, A. R. Calderbank +2
- **PDF**: https://ieeexplore.ieee.org/document/4276938
- **Abstract**: With the advent of quantum key distribution (QKD) systems, perfect (i.e., information-theoretic) security can now be achieved for distribution of a cryptographic key. QKD systems and similar protocols use classical error-correcting codes for both error correction (for the honest parties to correct errors) and privacy amplification (to make an eavesdropper fully ignorant). From a coding perspective, a good model that corresponds to such a setting is the wire tap channel introduced by Wyner in 1975. In this correspondence, we study fundamental limits and coding methods for wire tap channels. We provide an alternative view of the proof for secrecy capacity of wire tap channels and show how capacity achieving codes can be used to achieve the secrecy capacity for any wiretap channel. We also consider binary erasure channel and binary symmetric channel special cases for the wiretap channel and propose specific practical codes. In some cases our designs achieve the secrecy capacity and in others the codes provide security at rates below secrecy capacity. For the special case of a noiseless main channel and binary erasure channel, we consider encoder and decoder design for codes achieving secrecy on the wiretap channel; we show that it is possible to construct linear-time decodable secrecy codes based on low-density parity-check (LDPC) codes that achieve secrecy.

## A Binary Communication Channel With Memory Based on a Finite Queue

- **Status**: ❌
- **Reason**: 유한 큐 기반 메모리 이진채널 모델링(채널 통계/용량); 부호·디코더·HW 기여 없음, 순수 채널 이론
- **ID**: ieee:4276944
- **Type**: journal
- **Published**: Aug. 2007
- **Authors**: Libo Zhong, Fady Alajaji, Glen Takahara
- **PDF**: https://ieeexplore.ieee.org/document/4276944
- **Abstract**: A model for a binary additive noise communication channel with memory is introduced. The channel noise process, which is generated according to a ball sampling mechanism involving a queue of finite length $M$, is a stationary ergodic $M$th-order Markov source. The channel properties are analyzed and several of its statistical and information-theoretical quantities (e.g., block transition distribution, autocorrelation function (ACF), capacity, and error exponent) are derived in either closed or easily computable form in terms of its four parameters. The capacity of the queue-based channel (QBC) is also analytically and numerically compared for a variety of channel conditions with the capacity of other binary models, such as the well-known Gilbert–Elliott channel (GEC), the Fritchman channel, and the finite-memory contagion channel. We also investigate the modeling of the traditional GEC using this QBC model. The QBC parameters are estimated by minimizing the Kullback–Leibler divergence rate between the probability of noise sequences generated by the GEC and the QBC, while maintaining identical bit-error rates (BER) and correlation coefficients. The accuracy of fitting the GEC via the QBC is evaluated in terms of ACF, channel capacity, and error exponent. Numerical results indicate that the QBC provides a good approximation of the GEC for various channel conditions; it thus offers an interesting alternative to the GEC while remaining mathematically tractable.

## Hardware Generation of Arbitrary Random Number Distributions From Uniform Distributions Via the Inversion Method

- **Status**: ❌
- **Reason**: 임의 분포 난수 생성 HW(ICDF 다항식 근사); LDPC ECC와 무관, 떼어낼 디코더/코드 기법 없음
- **ID**: ieee:4276772
- **Type**: journal
- **Published**: Aug. 2007
- **Authors**: Ray C. C. Cheung, Dong-U Lee, Wayne Luk +1
- **PDF**: https://ieeexplore.ieee.org/document/4276772
- **Abstract**: We present an automated methodology for producing hardware-based random number generator (RNG) designs for arbitrary distributions using the inverse cumulative distribution function (ICDF). The ICDF is evaluated via piecewise polynomial approximation with a hierarchical segmentation scheme that involves uniform segments and segments with size varying by powers of two which can adapt to local function nonlinearities. Analytical error analysis is used to guarantee accuracy to one unit in the last place (ulp). Compact and efficient RNGs that can reach arbitrary multiples of the standard deviation sigma can be generated. For instance, a Gaussian RNG based on our approach for a Xilinx Virtex-4 XC4VLX100-12 field-programmable gate array produces 16-bit random samples up to 8.2 sigma. It occupies 487 slices, 2 block-RAMs, and 2 DSP-blocks. The design is capable of running at 371 MHz and generates one sample every clock cycle.

## Distributed Source Coding for Multimedia Multicast Over Heterogeneous Networks

- **Status**: ❌
- **Reason**: 분산 소스코딩+JSCC 멀티미디어 멀티캐스트; LDPC 채널ECC 기여 없음, 떼어낼 디코더/HW/구성 기법 없음
- **ID**: ieee:4276661
- **Type**: journal
- **Published**: Aug. 2007
- **Authors**: Vladimir Stankovic, Yang Yang, Zixiang Xiong
- **PDF**: https://ieeexplore.ieee.org/document/4276661
- **Abstract**: Real-time multimedia multicast over wireless networks is an exciting application that has generated a lot of interest recently. Its main challenge lies in the stringent bandwidth and time-delay requirements of real-time multimedia and severe impairments of the wireless channels. We develop a network-aware cross-layer design for multimedia multicast over heterogeneous wireless-wireline networks, that leverages the knowledge on network information theory, multimedia processing, error control, and networking. In particular, the encoded multimedia data are broadcast to multiple Internet servers over a wireless radio link. Each server merely compresses the signal it has received using distributed source coding by exploiting mutual correlation among signals received at different servers. The receiver collects bitstreams from the servers before performing joint decoding. We provide an algorithm for optimal nonuniform scalar quantizer design at the server side that minimizes the required rate under the decoder bit error rate constraint. For scalable multimedia codes, we develop a joint source-channel coding scheme which combines error-protection at the base station and distributed source coding at the servers. Our experimental results show significant performance improvements over conventional solutions due to spatial diversity and distributed source coding gains.

## Design for Testability of CMOS Analog Sum-Product Error-Control Decoders

- **Status**: ❌
- **Reason**: 아날로그 SP 디코더용 BIST 테스트 기법; 디코더 알고리즘/구성 아닌 테스트 회로라 이식 ECC 기법 없음
- **ID**: ieee:4277946
- **Type**: journal
- **Published**: Aug. 2007
- **Authors**: Mimi Yiu, Chris Winstead, Vincent Gaudet +1
- **PDF**: https://ieeexplore.ieee.org/document/4277946
- **Abstract**: A built-in self-test (BIST) technique is presented for testing analog iterative decoders. Catastrophic circuit faults are detected by temporarily operating the analog soft gates in a digital mode. Self-testing operations are performed in the digital domain, thereby lowering the cost and complexity compared to alternative mixed-signal BIST approaches. A proof-of-concept CMOS integrated circuit realization of the BIST is also presented. BER measurements show that the added circuits do not interfere with the decoder's performance during normal operation.

## A new encoder implementation for low-density parity-check convolutional codes

- **Status**: ❌
- **Reason**: LDPC convolutional 인코더(partial syndrome) FPGA 구현, 디코더/구성 아닌 인코더 전용이며 SC 블록 적용성 낮음
- **ID**: ieee:4487987
- **Type**: conference
- **Published**: 5-8 Aug. 2
- **Authors**: Zhengang Chen, Ramkrishna Swamy, Stephen Bates
- **PDF**: https://ieeexplore.ieee.org/document/4487987
- **Abstract**: Low-density parity-check (LDPC) convolutional codes provide an alternative to popular LDPC block codes and are better suited for certain applications such as streaming or packet-based systems with variable frame size. A newly proposed encoder architecture for such codes, referred to as the partial syndrome encoder, is implemented on a Xilinx Virtex II FPGA device in this paper. The results are compared to the existing direct encoder architecture for the same code on the same device. We show that the partial syndrome encoder achieves a better tradeoff between complexity and throughput. Results for larger codes demonstrates that the partial syndrome encoder architecture scales well with the code size.

## Error-Correcting Codes for Dynamic Spectrum Allocation in Cognitive Radio Systems

- **Status**: ❌
- **Reason**: 인지무선 스펙트럼 할당에 LDPC를 응용 적용만, 떼어낼 신규 디코더/구성 기법 없음
- **ID**: ieee:4294459
- **Type**: conference
- **Published**: 30 July-2 
- **Authors**: Chris Nicola, Hugues Mercier, Vijay K. Bhargava
- **PDF**: https://ieeexplore.ieee.org/document/4294459
- **Abstract**: Cognitive radio is an innovative technology proposed to increase spectrum usage by allowing dynamic allocation of the unused spectrum in changing environments. Cognitive users monitor the spectrum and are allowed to use it as long as it does not interfere with the primary users to whom it has been licensed. In this paper, we describe how some well established tools from the fields of error-correcting codes and information theory can be applied to the opportunistic spectrum access problem in cognitive radio. More precisely, we describe simple channel models based on information theoretic analysis and demonstrate that common error-correcting coding techniques, specifically low-density parity-check codes and insertion-deletion codes, can be used to solve this problem.

## Low power soft-output signal detector design for wireless MIMO communication systems

- **Status**: ❌
- **Reason**: MIMO soft-output 신호검출기 설계로 LDPC 부호/디코더 무관, 떼어낼 ECC 기법 없음
- **ID**: ieee:5514324
- **Type**: conference
- **Published**: 27-29 Aug.
- **Authors**: Sizhong Chen, Tong Zhang
- **PDF**: https://ieeexplore.ieee.org/document/5514324
- **Abstract**: Energy-efficient realization of soft-output signal detection is of great importance in emerging high-speed multiple-input multiple-output (MIMO) wireless communication systems. This paper presents three algorithm-level complexity-reduction techniques for soft-output detector design to achieve significant energy savings. To demonstrate their effectiveness, we designed a soft-output detector for 4-4 MIMO with 64-QAM using 65nm CMOS technology. While achieving near-optimum detection performance, the detector can support over 100Mbps throughput with only 0.24mm2 silicon area and 11mw power, leading to a ×10 improvement over the state of the art.

## LDPC Codes for High Data Rate Multiband OFDM Systems over 1Gbps

- **Status**: ❌
- **Reason**: 멀티밴드 OFDM용 기존 LDPC(irregular/simplified/array)의 PER 성능평가만 — 새 코드/디코더 기여 없음
- **ID**: ieee:4313243
- **Type**: conference
- **Published**: 22-24 Aug.
- **Authors**: Daisuke Abematsu, Tomoaki Ohtsuki, Tsuyoshi Kashima +1
- **PDF**: https://ieeexplore.ieee.org/document/4313243
- **Abstract**: In this paper, we evaluate packet error rate (PER) performances of high data rate multiband OFDM systems over 1 Gbps in CM 3 using irregular structured LDPC code, simplified LDPC code, and array LDPC code. We also evaluate the decoding complexities of simplified LDPC code and array LDPC code with code rates of R = 3/4,7/8, when belief propagation (BP) algorithm is used. From simulation results, we show that at data transmission rates of 640, 960 Mbps, simplified LDPC codes have the best error rate performances, and at data transmission rate of 1120 Mbps, array LDPC code has better error rate performances than simplified LDPC code. We also show that the order of decoding complexity for array LDPC code and simplified LDPC codes are same.

## On Construction of Concatenated Low-Density Generator Matrix Codes

- **Status**: ❌
- **Reason**: concatenated LDGM(생성행렬) 코드 구성 — LDPC 패리티검사 아닌 비-LDPC 코드 패밀리, 떼어낼 LDPC 기법 없음
- **ID**: ieee:4313269
- **Type**: conference
- **Published**: 22-24 Aug.
- **Authors**: Yusuke Kumano, Tomoaki Ohtsuki
- **PDF**: https://ieeexplore.ieee.org/document/4313269
- **Abstract**: Low-density generator-matrix (LDGM) codes have advantages - fast encoding and parallel decoding, however the performance of the LDGM code is asymptotically bad. This problem can be solved by concatenating two LDGM codes serially. However, little is known about the construction of the concatenated LDGM codes - component LDGM codes, the combination of inner and outer coding rates, inner and outer code weights. In this paper, we investigate the parity check matrix of component LDGM codes that suited to concatenated LDGM codes. We also investigate appropriate combination of inner and outer coding rates and inner and outer code weights, and so on. In addition, we investigate how to set the maximum number of inner and outer iterations for concatenated LDGM codes. Our results are useful for the construction of concatenated LDGM codes.

## An Accurate HARQ Scheme for LDPC

- **Status**: ❌
- **Reason**: irregular LDPC용 HARQ 재전송 비율 최적화(Gaussian approx) — 재전송 프로토콜, 채널 ECC 디코더/코드/HW 기여 아님
- **ID**: ieee:4469463
- **Type**: conference
- **Published**: 22-24 Aug.
- **Authors**: Xuehua Li, Zhensong Li, Yiqing Cao
- **PDF**: https://ieeexplore.ieee.org/document/4469463
- **Abstract**: An accurate hybrid ARQ (HARQ) scheme for irregular LDPC codes is introduced in this paper, in which the source retransmits the nodes at specific proportions each time. The proportions of retransmission bits can be specified in definite quantity with Gaussian Approximation (GA) and optimal method as long as degree distribution and initial channel state are known. It provides an accurate mean to evaluate other HARQ schemes for LDPC coded system. The traditional Degree Distribution Based HARQ (DDB-HARQ) is also studied and compared with the proposed one. Statistic and numerical results are presented and we can conclude that the new scheme has optimal performance in the HARQ schemes based on degree distribution of LDPC codes.

## An Adaptive LDPC-coded MIMO-OFDM System with Partial Channel State Information

- **Status**: ❌
- **Reason**: MIMO-OFDM 적응 전송(비트/전력 할당)에 LDPC가 부수 언급, 떼어낼 디코더·코드설계 기법 없음
- **ID**: ieee:4469578
- **Type**: conference
- **Published**: 22-24 Aug.
- **Authors**: Binggang Huang, Yi Hui, Wenqiang Zhang +1
- **PDF**: https://ieeexplore.ieee.org/document/4469578
- **Abstract**: An adaptive transmission scheme of MIMO-OFDM system based on MQAM and LDPC code is proposed. An transmit optimization algorithm to obtain an bit and power allocation is used which selects the MCS requiring only the mean and variance assuming the received LLR distribution as Gaussian. Simulation results show the performance of the proposed scheme is up to about 3dB better than other transmission schemes at the expense of a few bits in the feedback information.

## Full Search of Side-Information in Distributed Video Coding

- **Status**: ❌
- **Reason**: 분산비디오코딩(DVC) LDPCA side-information 탐색 — 소스코딩/Slepian-Wolf, 채널 ECC로 떼어낼 기법 없음
- **ID**: ieee:4297091
- **Type**: conference
- **Published**: 22-24 Aug.
- **Authors**: Yixuan Zhang, Ce Zhu
- **PDF**: https://ieeexplore.ieee.org/document/4297091
- **Abstract**: Distributed video coding (DVC) has attracted increasing research efforts due to the requirements of low complexity encoders for portable wireless video communication devices. The recently proposed DVC scheme using Low-Density-Parity-Check-Accumulate (LDPCA) code with hash-based motion estimation at the decoder has achieved very good performance. However, there is still a performance gap compared with conventional video coding schemes. In this paper, we propose a scheme using a full search for side-information to obtain the best possible side- information at the decoder without hash or other extra bits, thus improving the coding efficiency. The simulation results validate the effectiveness of the proposed scheme with better rate-distortion performance compared with the original hash-based LDPCA scheme.

## A Graph Approach to the Structural Analysis of Simplified Convolutional Self-Doubly-Orthogonal Codes

- **Status**: ❌
- **Reason**: convolutional self-doubly-orthogonal 코드의 그래프 구조분석 — 비-LDPC 코드 패밀리 이론분석, 이식 디코더/구성 없음
- **ID**: ieee:4313291
- **Type**: conference
- **Published**: 22-24 Aug.
- **Authors**: Yu-Cheng He, David Haccoun, Christian Cardinal
- **PDF**: https://ieeexplore.ieee.org/document/4313291
- **Abstract**: A graph approach to the structural analysis of simplified convolutional self-doubly-orthogonal codes is presented. Using difference sets and computation tree, it is shown that the code simplification leads to a reduction of the number of independent observations over two successive decoding iterations, and yields only an increase of the number of cycles of length eight in the Tanner graphs for the codes. This analysis provides a theoretical explanation on the nature of the code simplification and helps improving the search algorithms for these new codes.

## Quasi-orthogonal Space Time Block Codes (STBC) with full transmit rate Concatenated LDPC codes

- **Status**: ❌
- **Reason**: QOSTBC-LDPC concatenation(MIMO), LDPC는 베이스라인이고 새 디코더/코드설계 없음 - 무선응용 특이적
- **ID**: ieee:4350891
- **Type**: conference
- **Published**: 16-18 Aug.
- **Authors**: Wang lanxun, Li weizhen
- **PDF**: https://ieeexplore.ieee.org/document/4350891
- **Abstract**: In MIMO system of wireless communications, Space time block coding (STBC) is the attractive technique for high bit-rate and high capacity transmission. Methods for providing transmit diversity in communication over fading channels also been concerned. Although STBC has full diversity gain but not coding gain. The concatenation scheme of STBC codes and LDPC (STBC-LDPC) was proposed and it has been shown that the STBC-LDPC can achieve the good error rate performance and coding gain. Recently, low-density parity-check (LDPC) codes have attracted much attention as the good error correcting codes achieving the near Shannon limit performance like turbo codes. In this paper, a concatenation scheme of LDPC codes and Quasi orthogonal STBC which should apply full transmit rate with multiple transmit antennas is proposed. Refering to it as the QOSTBC-LDPC. We evaluate the bit error rate (BER) of the QOSTBC-LDPC with multiple transmit antennas in a quasi-static Rayleigh fading channel by the computer simulation. We show that the BER of the QOSTBC-LDPC is better than that of the STBC with same antennas in a quasi-static Rayleigh fading channel. When receive antennas increasing, the diversity gain will be increasing too.

## Code Design of Space-Time Block Codes Coded Low-Density Parity-Check Code and System Performance Analysis

- **Status**: ❌
- **Reason**: STBC-LDPC concatenation(MIMO), LDPC 베이스라인이고 새 ECC 기법 없음
- **ID**: ieee:4350915
- **Type**: conference
- **Published**: 16-18 Aug.
- **Authors**: Wang lanxun, Li weizhen
- **PDF**: https://ieeexplore.ieee.org/document/4350915
- **Abstract**: In Multiple Input and Multiple Output system of wireless communications, Space time coding using multiple transmit antennas is the attractive technique for high bit-rate and high capacity transmission. Methods for providing transmit diversity in communication over fading channels also been concerned. Although Space-Time Block Codes has full diversity gain but not coding gain. The concatenation scheme of STBC codes and LDPC (STBC-LDPC) was proposed and it has been shown that the STBC-LDPC can achieve the good error rate performance and coding gain. Low-density parity-check (LDPC) codes, as it is the good error correcting codes achieving the near Shannon limit performance. In this paper, a concatenation scheme of LDPC codes and STBC which should apply full transmit rate with multiple transmit antennas is proposed. Refering to it as the ABBA-LDPC and OSTBC-LDPC. We evaluate the bit error rate (BER) of the two schemes in a quasi-static Rayleigh fading channel by the computer simulation. We show that the BER of the ABBA-LDPC is better than that of the STBC with same antennas in a quasi-static Rayleigh fading channel, and also it is better than OSTBC-LDPC which uses real constellation. When receive antennas increasing, the diversity gain will be increasing too.

## Special Equipment Railway Transportation Communication Net Based on the Field Bus

- **Status**: ❌
- **Reason**: 철도 필드버스 통신망/RS-485 - LDPC 무관
- **ID**: ieee:4350954
- **Type**: conference
- **Published**: 16-18 Aug.
- **Authors**: Xue Xian, Zhang Shiying, Chen Jiazhao
- **PDF**: https://ieeexplore.ieee.org/document/4350954
- **Abstract**: The special equipment railway transportation communication net based on the field bus that the paper issued, aimed at the characteristic of railway transportation, such as simple structure, distinct layer, reducing data intermediate link as far as possible in network flows , reducing the cost of entire system, increasing flexibility, reliability and the fast communication. According to this principle, the paper only adopted OSI model 1, 2 and 7 layers, and created a user layer. The structures of the transportation communication net based on the field bus are physical layer, data linking layer, application layer and user layer. On the foundation of communication net layers, we designed the communication net communication protocols based on the field bus. We set monitoring unit logic number in the data token defined in transportation communication net protocol, realized the random net of transportation task at random. RS-485 half-duplex communication net shift circuit is designed and the net experiment is as well completed.

## Performance of Low Density Parity Check Code Applied in WiBro System

- **Status**: ❌
- **Reason**: WiBro에 기존 structured LDPC 적용 성능비교 - 새 코드/디코더 기여 없음
- **ID**: ieee:4393590
- **Type**: conference
- **Published**: 16-17 Aug.
- **Authors**: Wen Che, Yuexing Peng, Wenbo Wang
- **PDF**: https://ieeexplore.ieee.org/document/4393590
- **Abstract**: In Korea, a new broadband wireless access system-High speed Portable Internet (WiBro, Wireless Broadband) is devised to provide high data-rate Internet service. WiBro is considered as the subset of consolidated version of IEEE802. 16c and aims to provide high-speed packet service even when mobile speed comes to 120km/h. This paper presents a brief introduction to the key features of WiBro' s physical layer. Then an advanced channel coding technology- adopted in IEEE802. 16e- structured LDPC is applied to WiBro. The performance of structured LDPC coded WiBro system with different modulation level over AWGN and multi-path channel is simulated. Comparison between structured LDPC and Convolution Turbo Code (CTC) defined in the same proposal are discussed. Simulation results show that the two codes have similar performance when the code rate is low; but LDPC shown better performance than CTC in high code rate, especially at high modulation level.

## Enhanced HARQ Schemes Based on LDPC Coded Irregular Modulation

- **Status**: ❌
- **Reason**: LDPC coded irregular modulation+HARQ 매핑 최적화 - 무선 변조 응용, 이식 가능 디코더/코드설계 아님
- **ID**: ieee:4393458
- **Type**: conference
- **Published**: 16-17 Aug.
- **Authors**: Jia Minli, He Zunwen, Kuang Jingming
- **PDF**: https://ieeexplore.ieee.org/document/4393458
- **Abstract**: The bit-interleaved coded irregular modulation (BICIM) was initially proposed for convolutional code and turbo code cases, which applies different signal constellations and mappings within one codeword. We firstly extend this idea to irregular LDPC codes and present an optimized mapping rule for LDPC coded irregular modulation according to the code degree distribution. Furthermore, we apply this optimized LDPC coded irregular modulation to chase combing (CC) HARQ and propose two enhanced HARQ schemes. The improved schemes can efficiently reduce the reliability variances of bits after soft combining. Simulation results show that they can not only achieve better BER performance but also provide a throughput performance enhancement.

## Full-rate and Low Complexity Space-time Coding Scheme Concatenated with LDPC Codes

- **Status**: ❌
- **Reason**: space-time coding+LDPC concatenation(MIMO), LDPC 채널코딩 베이스라인 - 떼어낼 기법 없음
- **ID**: ieee:4393463
- **Type**: conference
- **Published**: 16-17 Aug.
- **Authors**: Yu Xiangbin, Xu Dazhun, Bi Guangguo
- **PDF**: https://ieeexplore.ieee.org/document/4393463
- **Abstract**: In this paper, a full-rate and low complexity space-time coding scheme with complex orthogonal design is developed, and LDPC code is employed as channel coding to improve the proposed scheme performance further. Compared with full-diversity space-time code schemes, the developed scheme can implement full data rate, low calculation complexity and partial diversity; and it can adopt lower order modulation scheme under the same system throughput. Moreover, using the developed scheme can form efficient spatial interleaving, thus the performance loss due to partial diversity is effectively compensated by the concatenation of channel coding. Simulation results show that on the condition of the same system throughput and concatenation of channel coding, the developed scheme has lower bit error rate than those low-rate and full-diversity multiple antennas space-time coding schemes.

## On Short Forward Error-Correcting Codes for Wireless Communication Systems

- **Status**: ❌
- **Reason**: RS·CZ·short FEC 코드 성능비교, 신규 LDPC 디코더·구성 기여 없음(비-LDPC 중심)
- **ID**: ieee:4317850
- **Type**: conference
- **Published**: 13-16 Aug.
- **Authors**: Sheng Tong, Dengsheng Lin, Aleksandar Kavcic +2
- **PDF**: https://ieeexplore.ieee.org/document/4317850
- **Abstract**: For real-time wireless communications, short forward error-correcting (FEC) codes are indispensable due to the strict delay requirement. In this paper we study the performance of short FEC codes. Reed-Solomon (RS) codes and concatenated zigzag (CZ) codes are chosen as representatives of classical algebraic codes and modern simple iterative decodable codes, respectively. Additionally, we use random binary linear codes as a baseline reference for comparison. Our main results (demonstrated by both simulation and ensemble distance spectrum analysis) are as follows: 1) Short RS codes are as good as random binary linear codes; 2) Carefully designed short low-density parity-check (LDPC) codes are almost as good as random binary linear codes when high decoding complexity can be tolerated; 3) Low complexity belief propagation decoders incur considerable performance loss at short coding lengths.

## Error-Correcting Codes Based on Quasigroups

- **Status**: ❌
- **Reason**: quasigroup 기반 비선형 부호 — LDPC/BP 아님, 떼어낼 기법 없음
- **ID**: ieee:4317814
- **Type**: conference
- **Published**: 13-16 Aug.
- **Authors**: Danilo Gligoroski, Smile Markovski, Ljupco Kocarev
- **PDF**: https://ieeexplore.ieee.org/document/4317814
- **Abstract**: Error-correcting codes based on quasigroup transformations are proposed. For the proposed codes, similar to recursive convolutional codes, the correlation exists between any two bits of a codeword, which can have infinite length, theoretically. However, in contrast to convolutional codes, the proposed codes are nonlinear and almost random: for codewords with large enough length, the distribution of the letters, pair of letters, triple of letters, and so on, is uniform. Simulation results of bit-error probability for several codes in binary symmetric channels are presented.
