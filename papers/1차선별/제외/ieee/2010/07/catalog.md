# IEEE Xplore — 2010-07


## Mitigation of Impulsive Noise Effect on the PLC Channel With QC–LDPC Codes as the Outer Coding Scheme

- **Status**: ❌
- **Reason**: QC-LDPC+RS outer for PLC/OFDM; 표준 SP/bit-flip, 수정 SP는 RS 연접 의존이라 NAND로 떼어낼 신기법 없음
- **ID**: ieee:5439947
- **Type**: journal
- **Published**: July 2010
- **Authors**: Nikoleta Andreadou, Fotini-Niovi Pavlidou
- **PDF**: https://ieeexplore.ieee.org/document/5439947
- **Abstract**: In this paper, the characteristics of irregular quasicyclic-low-density parity check (QC-LDPC) codes are examined when they are applied on a highly impulsive noise channel, such as the power-line-communications (PLC) channel. We study two decoding algorithms: 1) the sum product and 2) the bit-flipping algorithm, and how they affect the system's performance. LDPC codes are introduced in combination with other coding schemes, such as Reed-Solomon and convolutional codes. We propose irregular QC-LDPC codes as outer codes for the PLC channel in combination with Reed-Solomon codes, due to their decoding characteristics. In addition, various code rates are used for each different coding scenario. We also test how common Reed-Solomon codes affect the system's performance, such as the RS(63, 53), RS(511, 431), RS(127, 107), and RS(255, 239) codes. Furthermore, we propose an altered version of the sum-product decoding algorithm to enable its operation when QC-LDPC codes are used as the outer coding scheme in combination with Reed-Solomon codes. Regarding the system's design, the orthogonal frequency-division multiplexing transmission technique is utilized. We also take Zimmermann's model into consideration for the PLC channel and Middleton's noise model.

## Reduced-Memory Decoding of Low-Density Lattice Codes

- **Status**: ❌
- **Reason**: low-density lattice code용 BP 디코더—바이너리 LDPC 아님(격자부호)
- **ID**: ieee:5545622
- **Type**: journal
- **Published**: July 2010
- **Authors**: Brian Kurkoski, Justin Dauwels
- **PDF**: https://ieeexplore.ieee.org/document/5545622
- **Abstract**: This letter describes a belief-propagation decoder for low-density lattice codes of finite dimension, in which the messages are represented as single Gaussian functions. Compared to previously-proposed decoders, memory is reduced because each message consists of only two values, the mean and variance. Complexity is also reduced because the check node operations are on single Gaussians, avoiding approximations needed previously, and because the variable node performs approximations on a smaller number of Gaussians. For lattice dimension n = 1000 and 10,000, this decoder looses no more than 0.1 dB in SNR, compared to the decoders which use much more memory.

## A Novel JSCC Framework With Diversity-Multiplexing-Coding Gain Tradeoff for Scalable Video Transmission Over Cooperative MIMO

- **Status**: ❌
- **Reason**: JSCC 비디오/MIMO 프레임워크, LDPC는 UEP 베이스라인—제외 대상(JSCC)
- **ID**: ieee:5473098
- **Type**: journal
- **Published**: July 2010
- **Authors**: Hongjiang Xiao, Qionghai Dai, Xiangyang Ji +1
- **PDF**: https://ieeexplore.ieee.org/document/5473098
- **Abstract**: The multiple-input-multiple-output (MIMO) and cooperative communication are two state-of-the-art techniques to provide high-rate high-quality video communication services. By taking advantage of both techniques, this paper presents a novel joint source-channel coding (JSCC) framework for scalable video transmission over cooperative MIMO. In this framework, we first propose a cooperative MIMO architecture, which employs macro-micro power control strategy as a relaying protocol to determine the on/off mode of relays and the specific power allocation among them either by equal power amplification or by cooperative beamforming. Then, an unequal error protection structure is proposed to protect the video layers with different importance levels by concatenating the rate-variable low-density parity-check codes and diversity-embedded space-time block codes. Moreover, for the purpose of channel adaptation, the switch of space-time codes is designed to achieve different diversity and multiplexing tradeoff points. Finally, the JSCC algorithm integrated with diversity-multiplexing-coding gain tradeoff is proposed to optimize the resources of cooperative system to improve the transmission quality of scalable video. Experimental results demonstrate the effectiveness of our proposed schemes.

## High performance of parallel concatenated code

- **Status**: ❌
- **Reason**: 연접부호(외부 대수부호+내부 LDPC) 광통신 응용, 새 디코더/구성 기여 없음
- **ID**: ieee:5564637
- **Type**: conference
- **Published**: 9-11 July 
- **Authors**: Qian Zhao, Liang Zhou, Hong Wen +2
- **PDF**: https://ieeexplore.ieee.org/document/5564637
- **Abstract**: In this paper, we introduce a kind of high performance of concatenated code that is called parallel concatenated code. Comparing to conventional serial concatenated code, it has more matching room and higher adaptability. Moreover, burst of errors which are aroused by noise are beautiful restrained. For certifying the superiority and practicability, we research a parallel concatenated code by combining the outer algebraic code with the inner Low density Parity Check (LDPC) code. The bit error rate (BER) may be as low as 10−22 when Signal Noise Ratio (SNR) is 3.9dB. In the high speed 100Gp/s optical communication system, it will play a significant role.

## A note on relationship between algebraic geometric codes and LDPC codes

- **Status**: ❌
- **Reason**: 대수기하부호와 LDPC의 관계 분석 순수 이론, 디코더/HW/구성으로 안 이어짐(AG코드는 LDPC가 드묾 결론)
- **ID**: ieee:5555509
- **Type**: conference
- **Published**: 5-7 July 2
- **Authors**: Wanbao Hu, Huaping Cai, Yanxia Wu +1
- **PDF**: https://ieeexplore.ieee.org/document/5555509
- **Abstract**: Low-density parity-check (LDPC) codes constructed by a sparse parity-check matrix are of very fast encoding and decoding algorithms. Another kind of codes, which improved the well-known Gilbert-Varshamov bound, are algebraic geometry codes (Goppa geometry codes) from algebraic curves over finite fields. In the note, we analyze their characteristic of the two class of codes and show that the algebraic geometric codes are seldom LDPC codes.

## Quasi-cyclic LDPC-coded signal space diversity with precoding over fading channels

- **Status**: ❌
- **Reason**: QC-LDPC를 신호공간다이버시티(SSD)+프리코더에 결합한 무선 응용, QC구조는 표준 재사용·떼어낼 신규 LDPC 기법 없음
- **ID**: ieee:5555283
- **Type**: conference
- **Published**: 5-7 July 2
- **Authors**: Jintao hu, Yongsheng Wang, Zhiping Shi +1
- **PDF**: https://ieeexplore.ieee.org/document/5555283
- **Abstract**: Signal space diversity (SSD) has been viewed as a very efficient method to increase the diversity order and the reliability of wireless transmission over fading channels. The LDPC code can provide powerful error protection. The quasi cyclic structure which has significant advantage for memory efficiency, facilitates encoder and decoder implementation through shift register based circuits. The combination of quasi-cyclic LDPC codes and SSD is an effective technique to improve the performance of communication system for fading channel. This paper discusses a signal space diversity with a precoder by adding a simple encoder before applying the rotation matrix that can be viewed as a SSD with rate below 1. We propose three design criteria and two implementation method. And we further consider a quasi-cyclic LDPC-coded signal space diversity with precoding and their rate reallocation between channel coding and SSD. The simulation results show that our scheme outperforms the conventional coded-SSD over the fading channel when we get a better rate allocation that depends on the specific channel coding.

## Cross-layer design in multiuser diversity system

- **Status**: ❌
- **Reason**: rate-compatible LDPC+STBC 크로스레이어 다중사용자 무선 throughput 분석, LDPC 부수 사용·신규 ECC 기법 없음
- **ID**: ieee:5555417
- **Type**: conference
- **Published**: 5-7 July 2
- **Authors**: Yuling Zhang, Wenwei He
- **PDF**: https://ieeexplore.ieee.org/document/5555417
- **Abstract**: In this paper, we investigate a cross-layer framework in multiuser diversity system. Rate compatible Low-density Parity-check codes (LDPC) and space-time block codes (STBC) are employed. Under the assumption that the channel state information (CSI) is known at the receiver and the adaptive control signaling can be perfectly fed back to the transmitter, we first derive the expressions for the throughput of the system and then give the computer simulation results.

## Performance of distributed GLD codes over mobile-to-mobile fading channels

- **Status**: ❌
- **Reason**: 분산 GLD 부호 M2M 페이딩 BER 성능 분석, 무선 응용·표준 부호·떼어낼 신규 기법 없음
- **ID**: ieee:5555708
- **Type**: conference
- **Published**: 5-7 July 2
- **Authors**: Changcai Han
- **PDF**: https://ieeexplore.ieee.org/document/5555708
- **Abstract**: For cooperative networks with mobile source and mobile relay nodes, the performance of distributed generalized low-density (GLD) codes over mobile-to-mobile (M2M) fading source-relay channels is investigated. Specifically, the probabilities of different number of relay nodes becoming unreliable due to the quasi-static cascaded Rayleigh fading are analyzed and then the average bit error rate (BER) performance of distributed GLD codes is obtained. Simulation results reveal that distributed GLD codes on M2M fading source-relay channels can still achieve significant performance gains over the direct transmission, though quasi-static cascaded Rayleigh fading channels aggravate the performance compared with quasi-static Rayleigh fading channels.

## A self-hosting configuration management system to mitigate the impact of Radiation-Induced Multi-Bit Upsets in SRAM-based FPGAs

- **Status**: ❌
- **Reason**: FPGA SRAM 방사선 비트업셋 완화 스크러버(Hamming 코드 기반), LDPC 아님·비-LDPC ECC
- **ID**: ieee:5637493
- **Type**: conference
- **Published**: 4-7 July 2
- **Authors**: Marco Lanuzza, Paolo Zicari, Fabio Frustaci +2
- **PDF**: https://ieeexplore.ieee.org/document/5637493
- **Abstract**: This paper presents an efficient circuit to mitigate the impact of Radiation-Induced Multi-Bit Upsets in Xilinx FPGAs from Virtex-II on. The proposed internal scrubber detects and corrects single bit upsets and double, triple and quadruple multi bit upsets by efficiently exploiting permuted and compressed Hamming check codes. When implemented using a Xilinx XC2V1000 Virtex-II device, it occupies just 1488 slices and dissipates less than 30 mW at a 50MHz running frequency, taking just 18us to complete the error checking over a single frame, and 18.76us to repair the corrupted frame.

## Control of a high torque density seven-phase induction motor with field-weakening capability

- **Status**: ❌
- **Reason**: 7상 유도전동기 제어 논문, LDPC·ECC와 무관
- **ID**: ieee:5637787
- **Type**: conference
- **Published**: 4-7 July 2
- **Authors**: D. Casadei, M. Mengoni, G. Serra +3
- **PDF**: https://ieeexplore.ieee.org/document/5637787
- **Abstract**: In this paper, a rotor-flux-oriented control scheme for seven-phase induction motor drives is presented. At low speed the proposed control scheme is able to increase the motor torque by adding a third harmonic component to the air-gap magnetic field. Above the base speed the control system reduces the motor flux in such a way to ensure the maximum torque capability. The validity of the proposed control scheme is confirmed by experimental tests.

## Reverse link performance of packet data with LDPC and soft handoff in cellular CDMA

- **Status**: ❌
- **Reason**: CDMA 망 패킷데이터 성능분석에 LDPC 부수 언급, 떼어낼 ECC 기법 없음
- **ID**: ieee:5591646
- **Type**: conference
- **Published**: 29-31 July
- **Authors**: Priyabrata Parida, Sanjay Dhar Roy, Sumit Kundu
- **PDF**: https://ieeexplore.ieee.org/document/5591646
- **Abstract**: Performance analysis of data services is studied in CDMA network by incorporating Low Density Parity Check (LDPC) codes in presence of soft handoff. This scheme is found to enhance throughput and reduce delay and packet error rate significantly. A stop and wait ARQ has been assumed. Both the cases of coded and un-coded data transmission are investigated.

## Rate-Adaptive nonbinary-LDPC-coded modulation with backpropagation for long-haul optical transport networks

- **Status**: ❌
- **Reason**: 비이진(nonbinary) LDPC 코딩변조—비이진 LDPC는 제외 대상
- **ID**: ieee:5549085
- **Type**: conference
- **Published**: 27 June-1 
- **Authors**: Murat Arabaci, Ivan B. Djordjevic, Ted Schmidt +2
- **PDF**: https://ieeexplore.ieee.org/document/5549085
- **Abstract**: We propose a novel rate-adaptive, polarization-multiplexed, nonbinary-LDPC-coded modulation scheme with backpropagation as an enabling technology for high-speed data transmission over long-haul optical transport networks. We show that the proposed scheme with a very simple dispersion map ensures transmission at information bit rates of 200 Gb/s, 300 Gb/s and 400 Gb/s even in the worst channel conditions over reaches exceeding 6400 km, 3900 km and 2100 km, respectively.

## Generalized hybrid subcarrier/amplitude/phase/polarization LDPC-coded modulation based FSO networking

- **Status**: ❌
- **Reason**: FSO GH-SAPP LDPC 코딩변조—LDPC 베이스라인 응용, 떼어낼 ECC 신규 기법 없음
- **ID**: ieee:5549018
- **Type**: conference
- **Published**: 27 June-1 
- **Authors**: Ivan B. Djordjevic, Hussam G. Batshon
- **PDF**: https://ieeexplore.ieee.org/document/5549018
- **Abstract**: In this paper, we propose a generalized hybrid subcarrier/amplitude/phase/polarization (GH-SAPP) modulation based free-space optical (FSO) communication network. By using 32-GH-SAPP modulation and mature 10 Gb/s technology the aggregate rate of 110 Gb/s can be achieved, which represents an FSO scheme compatible with 100G Ethernet. The 32-GH-SAPP coded-modulation scheme can operate even under strong atmospheric turbulence regime while still carrying 100G traffic. The corresponding polarization-multiplexed 16-QAM scheme can only operate under weak turbulence regime with aggregate data rate of only 80 Gb/s. The proposed scheme represents a cost effective solution to current high-bandwidth demands.

## The stability of LDPC codes with higher order modulation schemes

- **Status**: ❌
- **Reason**: 고차 변조(M-PSK/M-QAM)에서 LDPC 안정성 조건의 밀도진화 이론분석 — 디코더/HW/구성으로 안 이어지는 순수 이론 bound, 제외
- **ID**: ieee:5580434
- **Type**: conference
- **Published**: 21-23 July
- **Authors**: V. S. Ganepola, R. A. Carrasco, I. J. Wassell +1
- **PDF**: https://ieeexplore.ieee.org/document/5580434
- **Abstract**: In this paper, we derive stability conditions for low-density-parity-check (LDPC) codes with Gray mapped M-ary phase-shift keying (M-PSK) and M-ary quadrate-amplitude-modulation (M-QAM) constellations. The stability of the LDPC decoder with higher order modulation schemes is examined on both additive-white-Gaussian-noise (AWGN) and block Rayleigh fading channels and threshold stability conditions under iterative decoding are obtained using density evolution techniques. It is shown that both on block Rayleigh fading channel when the ideal channel state information (CSI) of the fading process is known, and on AWGN channel, the stability condition of the underlying code is bounded by the Bhattacharya noise parameter. We show that the derived stability condition is both sufficient and necessary condition for iterative belief propagation decoding assuming cycle free massage passing between variable and check nodes. The evolution of stability condition is assessed as the modulation order is increased for both M-PSK and M-QAM constellations. This study provides an analytical framework to evaluate the performance bounds of LDPC coded systems that extend over higher order modulation schemes.

## LDPC FEC code extension for unequal error protection in 2nd generation DVB systems

- **Status**: ❌
- **Reason**: DVB UEP용 표준 LDPC 코드 확장, BCH+LDPC 연접 — 응용 특이적, 떼어낼 신규 ECC 기법 없음
- **ID**: ieee:5582541
- **Type**: conference
- **Published**: 19-23 July
- **Authors**: Lukasz Kondrad, Imed Bouazizi, Moncef Gabbouj
- **PDF**: https://ieeexplore.ieee.org/document/5582541
- **Abstract**: One of the envisioned advantages of scalable video coding is its inherent suitability for achieving unequal error protection (UEP). UEP can be effectively used for graceful quality degradation under harsh network conditions. The Digital Video Broadcasting (DVB) organization recently introduced second generations of broadcast transmission technologies like DVB-T2 and DVB-S2. These technologies, due to the newly introduced and advanced tools, ensure better quality of service compared to their respective first generation counterparts. Among the important tools that directly affect the quality of service positively in these emerging technologies is the new physical layer-chained forward error correction coding. In both cases, the chained codes comprise of a Bose-Chaudhuri-Hocquenghem (BCH) code, which functions as the outer code, followed by a Low-Density Parity Check (LDPC) code as the inner code. To allow for improved graceful quality degradation in the second generation DVB broadcast technologies, this article proposes a novel method to extend deployed LDPC codes. This code extension enables the implementation of UEP schemes in an effective manner in these DVB broadcast systems. Furthermore, the proposed solution is backward compatible to legacy receivers. The performance evaluation of the proposed method is supported by results, obtained through simulations.

## A GPU implementation for two MIMO-OFDM detectors

- **Status**: ❌
- **Reason**: MIMO-OFDM 검출기 GPU 구현 (SSFE/LORD), LDPC 무관 — ECC 기법 없음
- **ID**: ieee:5642054
- **Type**: conference
- **Published**: 19-22 July
- **Authors**: Teemu Nyländen, Janne Janhunen, Olli Silvén +1
- **PDF**: https://ieeexplore.ieee.org/document/5642054
- **Abstract**: Two real-valued signal models based on selective spanning with fast enumeration (SSFE) and layered orthogonal lattice detector (LORD) algorithms are implemented on a Nvidia graphics processing unit (GPU). A 2×2 multiple-input multiple-output (MIMO) antenna system with 16-quadrature amplitude modulation (16-QAM) is assumed. The chosen level update vector for SSFE is based on computer simulation results carried out in MATLAB environment. We implemented the algorithms with Nvidia Quadro FX 1700 GPU and achieved a throughput of 36.06 Mbps for SSFE and 16.8 Mbps for LORD. The results show that the general-purpose graphics processing unit (GPGPU) has the potential to achieve high throughput, presuming a detection algorithm that allows efficient parallel processing. The latency of the control code and partial Euclidean distance (PED) calculations are very small-scale, but the latency of memory loads and stores to the GPUs global memory are significant. We also compare results from the trellis based detector implementation for GPU, where a more powerful GPU and a different detection algorithm are used. The GPUs offer superior computing power and programmability compared to the application specific software defined radio (SDR) designs implemented so far.

## Performance analysis of projective geometry LDPC coded UWB system

- **Status**: ❌
- **Reason**: UWB OFDM에 표준 projective geometry LDPC 그대로 적용한 성능 비교, 신규 구성/디코더 기여 없음
- **ID**: ieee:5568734
- **Type**: conference
- **Published**: 17-18 July
- **Authors**: Fangni Chen
- **PDF**: https://ieeexplore.ieee.org/document/5568734
- **Abstract**: In this paper, we proposed a novel MB-OFDM UWB system, which exploits projective geometry constructed LDPC code as its channel encoding code. We emphasized on the construction of projective geometry LDPC code and the model of the UWB communication system. Also we simulated this novel system with computer software and compared the performance with uncoded UWB system. Finally we make a conclusion that projective geometry constructed LDPC codes are strong competitors to FEC codes for error control in communication systems.

## Symmetric Distributed Joint Source-Channel Coding Using Raptor Codes

- **Status**: ❌
- **Reason**: Raptor 기반 분산 JSCC; LDPC는 비교 베이스라인, 떼어낼 LDPC ECC 기법 없음
- **ID**: ieee:5575677
- **Type**: conference
- **Published**: 15-17 July
- **Authors**: Xuqi Zhu, Wenbo Zhang, Bin Li +1
- **PDF**: https://ieeexplore.ieee.org/document/5575677
- **Abstract**: Distributed compression of correlated sources has been discussed much in wireless sensor networks, while the error-resilient implementation of this efficient coding strategy is one of the crucial issues for applications. In this paper, a symmetric Distributed Joint Source-Channel Coding (DJSCC) scheme is proposed by using Raptor codes for the independent channels case. The channel noise and the correlation of sources are considered simultaneously within one set of encoder and decoder. The symmetric structure of the proposed approach leads to more flexible and balanced rate allocation, and the rateless property of Raptor codes also guarantees tractable code rates and error correction. At last, the simulation results demonstrate that our scheme outperforms the existing LDPC-based scheme at low SNR.

## New algorithm for message restoring with errors detection and correction using binary LDPC-codes and network coding

- **Status**: ❌
- **Reason**: binary LDPC + 네트워크코딩 메시지 복원, NAND ECC로 떼어낼 새 디코더 기법 불명확한 통신 응용
- **ID**: ieee:5555305
- **Type**: conference
- **Published**: 11-15 July
- **Authors**: Sergey Vladimirov
- **PDF**: https://ieeexplore.ieee.org/document/5555305
- **Abstract**: New algorithm for message restoring with error detection and correction using binary LDPC-codes with network coding is presented. The algorithm continues the ideas described in works of Kang et al. and also can be used in random network coding. New algorithm improves decoding characteristics over straightforward method with separate message restoring and errors detection and correction stages.

## What is the role of DSP in future optical access?

- **Status**: ❌
- **Reason**: 광 액세스망 DSP/OFDMA 비전 논문, LDPC ECC 기법 무관
- **ID**: ieee:5546422
- **Type**: conference
- **Published**: 11-14 July
- **Authors**: Ezra Ip, Neda Cvijetic, Dayou Qian +1
- **PDF**: https://ieeexplore.ieee.org/document/5546422
- **Abstract**: Digital signal processing enables software-defined optical access networks based on orthogonal frequency-division multiple access with improved spectral efficiency, flexible resource allocation, and high degree of reconfigurability.

## Iterative bit-flipped decoding of concatenated reed solomon/convolutional codes with HMAC

- **Status**: ❌
- **Reason**: RS/convolutional 연접부호 iterative bit-flip+암호해시, 비-LDPC이고 부호의존적이라 BP 이식 불가
- **ID**: ieee:5588212
- **Type**: conference
- **Published**: 11-14 July
- **Authors**: Obaid Ur Rehman, Natasa Zivic, Christoph Ruland
- **PDF**: https://ieeexplore.ieee.org/document/5588212
- **Abstract**: Cryptography and Coding theory are believed to have common roots. Foundations for both the fields were laid down by Claude Shannon. There is, however, very little research being done to investigate the relationship between the two and to see how one field can be used to benefit the other. In this contribution an interesting case study is considered to improve the channel coding results of concatenated Reed Solomon and Convolutional codes using cryptographic hash function and on the other hand to recover and verify the cryptographic hash code using the RS/Convolutional code with iterative bit flipped decoding. This is of interest for the applications that need security as well as resilience to communication errors. It is also demonstrated that a coding gain is achieved at the same time.
