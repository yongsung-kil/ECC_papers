# IEEE Xplore — 2002-01


## Performance of low-density parity-check (LDPC) coded OFDM systems

- **Status**: ❌
- **Reason**: LDPC-COFDM 무선 OFDM 응용, M-PSK용 디코딩이지만 표준 sum-product 기반·OFDM 변조 특이적이라 NAND LDPC로 떼어낼 신규 디코더/구성 없음
- **ID**: ieee:997138
- **Type**: conference
- **Published**: 2002
- **Authors**: H. Futaki, T. Ohtsuki
- **PDF**: https://ieeexplore.ieee.org/document/997138
- **Abstract**: Orthogonal frequency division multiplexing (OFDM) is a very attractive technique for high-bit-rate data transmission in multipath environments. Many error-correcting codes have been applied to OFDM. Recently, LDPC codes have attracted much attention. The performance of LDPC codes is very close to the Shannon limit, with practical decoding complexity. We proposed LDPC coded OFDM (LDPC-COFDM) systems with BPSK and showed that the LDPC codes are effective in improving the bit error rate (BER) of OFDM in multipath environments (see Futaki, H. and Ohtsuki, T., IEEE VTC2001 fall, vol.1, p.82-6, 2001). LDPC codes can be decoded using a probability propagation algorithm known as the sum-product algorithm or belief propagation. To clarify iterative decoding properties in LDPC-COFDM systems, we first investigate the distribution of the number of iterations where the decoding algorithm stops. In mobile communications, multilevel modulation is preferred for high bandwidth efficiency. However, it has not been clarified how to apply LDPC codes to OFDM systems with multilevel modulation. We propose a decoding algorithm for the LDPC-COFDM systems with M-PSK. By simulation, we show that LDPC-COFDM systems achieve good error rate performance with a small number of iterations on both AWGN and frequency-selective fading channels. We confirm that the algorithm for LDPC-COFDM systems with M-PSK work correctly.

## Low-density parity-check (LDPC) coded OFDM systems with M-PSK

- **Status**: ❌
- **Reason**: LDPC-COFDM 무선/OFDM 응용 특이적; 표준 LDPC가 부수 사용, 떼어낼 신규 디코더/HW/코드설계 기법 없음
- **ID**: ieee:1002646
- **Type**: conference
- **Published**: 2002
- **Authors**: H. Futaki, T. Ohtsuki
- **PDF**: https://ieeexplore.ieee.org/document/1002646
- **Abstract**: Orthogonal frequency division multiplexing (OFDM) is a very attractive technique to achieve the high-bit-rate transmission required for future mobile communications. To improve the error rate performance of OFDM, forward error correction coding is essential. Recently, low-density parity-check (LDPC) codes, which can achieve the near Shannon limit performance, have attracted much attention. We proposed the LDPC coded OFDM (LDPC-COFDM) systems to improve the error rate performance of OFDM. We showed that LDPC codes are effective to improve the error rate performance of OFDM on a frequency-selective fading channel. In mobile communications high bandwidth efficiency is required, and thus multilevel modulation is preferred. We also proposed the decoding algorithm for the LDPC-COFDM systems with MPSK on an AWGN channel. In this paper, we evaluate the error rate performance of the LDPC-COFDM systems with M-PSK using the Gray and the natural mappings on an AWGN channel, and that of the systems with M-PSK using the Gray mapping on a flat Rayleigh fading channel. We show that the LDPC-COFDM systems with M-PSK using the Gray mapping have better error rate performance than the systems using the natural mapping on an AWGN channel. We also show that the LDPC-COFDM systems with QPSK is more effective than the other systems on a flat Rayleigh fading channel.

## Upper bounds on the rate of LDPC codes

- **Status**: ❌
- **Reason**: 바이너리대칭 채널상 LDPC rate 상한 — 순수 이론 bound, 디코더/HW/구성으로 안 이어짐
- **ID**: ieee:1023300
- **Type**: conference
- **Published**: 2002
- **Authors**: D. Burshtein, M. Krivelevich, S. Litsyn +1
- **PDF**: https://ieeexplore.ieee.org/document/1023300
- **Abstract**: We present upper bounds on the rate of both individual LDPC codes and ensembles of codes when operated over an arbitrary binary-input symmetric-output channel.

## Robustness of LDPC codes on periodic fading channels

- **Status**: ❌
- **Reason**: 주기적 페이딩에 대한 LDPC 강건성/상호정보 성능 분석뿐, 신규 디코더·구성·HW 기여 없음
- **ID**: ieee:1188404
- **Type**: conference
- **Published**: 2002
- **Authors**: C. Jones, Tao Tian, A. Matache +2
- **PDF**: https://ieeexplore.ieee.org/document/1188404
- **Abstract**: Root and Variya (1968) proved the existence of codes that can communicate reliably over any member of a set of linear Gaussian channels where each member exceeds a given amount of mutual information. In this paper we show that LDPC codes are such codes and that their performance lies within 0.1 bits of the Root and Variya capacity for a large family of periodic Gaussian channels. specifically, the robustness of LDPC codes to periodic fading is demonstrated through the consistency of their mutual information performance across period-2 and period-256 fading profiles. The latter case implies that these codes are ideal candidates for coding in OFDM.

## LDPC-based joint source-channel coding scheme for multimedia communications

- **Status**: ❌
- **Reason**: LDPC 기반 JSCC(소스-채널 결합)+HMS 추정, LDPC가 베이스라인이고 떼어낼 ECC 디코더 기법 없음
- **ID**: ieee:1182493
- **Type**: conference
- **Published**: 2002
- **Authors**: Liuguo Yin, Jianhua Lu, Youshou Wu
- **PDF**: https://ieeexplore.ieee.org/document/1182493
- **Abstract**: Joint source-channel coding schemes have been proven to be effective ways for reliable multimedia communications. In this paper, we develop a joint source-channel coding scheme that well combines the hidden Markov source (HMS) estimation and the powerful low-density parity-check (LDPC) codes with an iterative estimation/decoding scheme. With this coding method, the source redundancy could be accurately extracted by the hidden Markov estimation without using any priori information about the source. Moreover, the interleaver that is likely used to separate the source coding and channel coding is exempted by exploiting the randomizing property of the LDPC codes, while the channel decoding procedure may be implemented in parallel, resulting in good performance with a fairly low decoding complexity and delay. Simulation results have shown that the proposed scheme may achieve a much better performance than that of the standard coding scheme over the binary input additive white Gaussian noise (BIAWGN) channels.

## Design of LDPC codes for two-state fading channel models

- **Status**: ❌
- **Reason**: two-state fading용 LDPC 설계가 BEC ensemble로 귀결 — erasure 채널 무선 응용, NAND 이식 구성 기여 없음
- **ID**: ieee:1088325
- **Type**: conference
- **Published**: 2002
- **Authors**: M. Yang, W. E. Ryan
- **PDF**: https://ieeexplore.ieee.org/document/1088325
- **Abstract**: We consider a two-state fading channel model and the design of LDPC codes for this model. Under certain assumptions, the model leads us to what we call the burst-erasure channel with AWGN (BuEC-G), in which bits are received in Gaussian noise or as part of an erasure burst. To design codes for this channel, we take a "shortcut" and instead design codes for the burst-erasure channel (BuEC) in which a bit is received correctly or it is received as an erasure, with erasures occurring in bursts. We show that optimal BuEC code ensembles are equal to optimal binary erasure channel (BEC) code ensembles and we design optimal codes for these channels. A given code on the BuEC may be characterized by the maximum resolvable erasure-burst length, L/sub max/, and we present a simple algorithm for computing this parameter. Finally, we present error-rate results which demonstrate the superiority of our codes on the BuEC-G over other codes that appear in the literature.

## The throughput of an LDPC-based incremental-redundancy scheme over block-fading channels

- **Status**: ❌
- **Reason**: block-fading INR/HARQ throughput 정보이론 분석 — 무선 응용 이론, 떼어낼 디코더/HW 기법 없음
- **ID**: ieee:1115403
- **Type**: conference
- **Published**: 2002
- **Authors**: S. Sesia, G. Caire
- **PDF**: https://ieeexplore.ieee.org/document/1115403
- **Abstract**: INcremental-Redundancy (INR) is a form of hybrid ARQ where the receiver asks the transmitter for additional parity bits when decoding is not successful. This technique is particularly useful in time-selective fading channels, since it implements variable-rate adaptive transmission with a very simple feedback binary channel, where the feedback messages are positive or negative acknowledgments (ACK and NACK, respectively). In this work an information-theoretic analysis of the achievable throughput and delay of INR over block-fading channels for random binary codes and for low-density parity-check (LDPC) binary linear codes.

## On the implementation and optimisation of LDPC codes on a reconfigurable hardware for future communications systems

- **Status**: ❌
- **Reason**: FPGA technology mapping을 유전알고리즘으로 최적화 — 무선/FPGA 라우팅 최적화 일반론으로 LDPC 디코더 알고리즘/아키텍처 기여 아님.
- **ID**: ieee:1032022
- **Type**: conference
- **Published**: 2002
- **Authors**: D. Barral, W. Falcon, J. Altuna +1
- **PDF**: https://ieeexplore.ieee.org/document/1032022
- **Abstract**: With the advent of new services and capabilities for next generation mobile communication systems, new powerful error-correcting schemes have emerged to increase cellular capacity and achieve higher transmission data rates effectively. A new set of error-correcting codes (ECCs), called low-density parity check codes (LDPCs), significantly reduce error-rates compared to conventional ECCs. This coding scheme achieves near-Shannon capacity, but unlike other schemes,offers great possibilities for implementation and parallelisation in reconfigurable systems such as field programmable gate arrays (FPGA). FPGA technology offers devices with a large scale of integration. However, the technology mapping stage of logic synthesis is considered not to be optimal enough. We show that evolutionary algorithms, and particularly genetic algorithms, are suitable for the optimisation of technology mapping. These algorithms model natural evolutionary processes, using selection, crossover and mutation operations, and significantly optimise the routing delay in the mapping process compared to commercial automatic mapping tools. A methodology for the implementation of an LDPC encoder/decoder in a commercial FPGA and a genetic algorithm that is used to optimise this implementation is presented. The proposed scheme highlights the potential of evolutionary methods in the reconfigurability of wireless devices.

## Bounds for low-density parity-check codes over partial-response channels

- **Status**: ❌
- **Reason**: PR 채널 LDPC FER 해석적 bound 계산; 순수 이론 bound로 디코더/HW/구성으로 이어지지 않음
- **ID**: ieee:1001123
- **Type**: conference
- **Published**: 2002
- **Authors**: W. Tan, R. M. Todd, J. R. Cruz
- **PDF**: https://ieeexplore.ieee.org/document/1001123
- **Abstract**: Summary form only given. The application of low-density parity-check (LDPC) codes to magnetic recording systems motivates the search for analytical ways to evaluate system performance over partial-response (PR) channels. In this paper a technique proposed by Duman and Kurtas (IEEE Trans. Inform. Theory, vol. 47, pp. 1203-1205, 2001) is extended to bound the frame error rate (FER) of high-rate LDPC codes. We circumvent the requirement that the weight distribution of the underlying code must be known by using estimates (A. Ashikhmin et al, ibid., vol. 47, pp. 1050-1061, 2001). This new bounding technique is used to compute the bounds for geometrically constructed LDPC codes over PR channels. Simulations are used to evaluate the computed bounds.

## Two approaches to the analysis of low-density parity-check codes

- **Status**: ❌
- **Reason**: LDPC 분석 방법론 개관(selected/ensemble approach) — 서베이성, 신규 디코더·구성·HW 기여 없음
- **ID**: ieee:1023301
- **Type**: conference
- **Published**: 2002
- **Authors**: K. S. Zigangirov, M. Lentmaier, D. Truhachev
- **PDF**: https://ieeexplore.ieee.org/document/1023301
- **Abstract**: We overview two approaches to the analysis of low-density parity-check (LDPC) codes: selected code approach and ensemble approach. As examples of application of the methods we consider Gallager's homogeneous LDPC codes and Berrou-Glavieux-Thitimajshima (BGT) turbo-codes.

## Decoding in optics

- **Status**: ❌
- **Reason**: LDPC/터보의 광학(아날로그) 디코딩 구현 — 디지털 NAND ECC HW 이식성 약함, 아날로그 제외
- **ID**: ieee:1023503
- **Type**: conference
- **Published**: 2002
- **Authors**: A. H. Banihashemi, S. Hemati
- **PDF**: https://ieeexplore.ieee.org/document/1023503
- **Abstract**: We propose using optical components for decoding digital information, based on the so-called iterative coding schemes, such as turbo codes and low-density parity-check (LDPC) codes. This suggests a significant increase in speed compared to the conventional electronic decoding.

## DC-free (d, k) constrained low density parity check (LDPC) codes

- **Status**: ❌
- **Reason**: (d,k) RLL 제약 LDPC 구성은 광스토리지 채널 특화 기법으로 NAND ECC에 떼어낼 부호설계 기여 약함; bit insertion은 NAND 무관.
- **ID**: ieee:1028672
- **Type**: conference
- **Published**: 2002
- **Authors**: H. Song, J. Liu, B. V. K. V. Kumar
- **PDF**: https://ieeexplore.ieee.org/document/1028672
- **Abstract**: Recently, turbo codes and low-density parity check (LDPC) codes with iterative soft decoding have been heavily investigated as potential candidates for low-SNR, high-density data storage systems. However, relatively less attention has been devoted to the investigation of (d, k) run-length limited (RLL) constrained LDPC codes, although run-length constraints are generally employed in data storage channels due to channel nonlinearities and timing recovery issues. In this paper, we propose an extended bit insertion technique to construct DC-free (d, k) constrained LDPC codes. As an example of the proposed method, we construct a DC-free (1,7) LDPC code, and report its performance in an optical storage channel.

## LDPC code design for MMSE turbo equalization

- **Status**: ❌
- **Reason**: ISI 채널 MMSE 터보 등화용 LDPC 코드 임계값 설계 — 통신 등화 응용 특이적이고 NAND ECC로 떼어낼 디코더/HW 기여 없음
- **ID**: ieee:1023687
- **Type**: conference
- **Published**: 2002
- **Authors**: K. R. Narayanan, Xiaodong Wang, Guosen Yue
- **PDF**: https://ieeexplore.ieee.org/document/1023687
- **Abstract**: The design of low density parity check (LDPC) codes with minimum mean squared error (MMSE) turbo equalization is considered. Techniques to compute the probability density function of the extrinsic information at the output of the equalizer and the decoder are discussed. Using these techniques, it is shown that thresholds can be computed for LDPC codes for intersymbol interference (ISI) channels and good LDPC code ensembles can be designed. The distinct features of this work include: (1) The input-output pdf of the equalizer is expressed in closed-form, and evaluated analytically - no simulation of the equalizer or the code is needed during the design process; (2) ISI channels with very long memory can be easily handled; (3) Codes for fading ISI channels can be designed without the need for extensive numerical computation.

## A coding theorem for lossy data compression by LDPC codes

- **Status**: ❌
- **Reason**: LDPC를 lossy 소스 압축(rate-distortion)에 적용 — 채널 ECC가 아닌 소스 코딩, 제외
- **ID**: ieee:1023733
- **Type**: conference
- **Published**: 2002
- **Authors**: Y. Matsunaga, H. Yamamoto
- **PDF**: https://ieeexplore.ieee.org/document/1023733
- **Abstract**: Recently, low density parity check (LDPC) codes have been studied actively because of the high performance of error correction. Many previous researches showed that LDPC codes can attain near the Shannon limit by iterative decoding with belief propagation. On the other hand, it is well known that channel coding can be considered as the dual problem of lossy source coding in the rate-distortion theory, and a good error correcting code can be used for efficient lossy data compression. In this paper, we show that LDPC codes can also attain the rate-distortion function asymptotically for the same source.

## Serially concatenated coding for PR system with LDPC and PC codes

- **Status**: ❌
- **Reason**: LDPC+PC 직렬연접 코딩 시스템 설명에 그침; 표준 sum-product/BP 사용, NAND LDPC에 새로 이식할 디코더/구성/HW 기여 없음
- **ID**: ieee:1000870
- **Type**: conference
- **Published**: 2002
- **Authors**: H. Saito, Y. Okamoto, H. Osawa
- **PDF**: https://ieeexplore.ieee.org/document/1000870
- **Abstract**: Summary form only given In this work, the coded partial response (PR) system based on serially concatenated error control codes is described. The component codes of the concatenated codes are a low density parity check (LDPC) code and a punctured convolutional (PC) code. In our system, the LDPC code is used as an inner code and is an important random code which can approach Shannon's capacity limit. A practical decoding method of the LDPC code is known as the sum-product decoding algorithm or belief propagation. Furthermore, the PC code is used for an outer code and can enhance the minimum squared Euclidean distance for the coded PR system. The sequence of the PC code has a single parity check capability for the concatenated coding.

## Turbo code at 0.03 dB from capacity limit

- **Status**: ❌
- **Reason**: turbo code(비-LDPC)이며 부호 구성에 한정, 바이너리 LDPC BP에 이식할 디코더 기법 없음
- **ID**: ieee:1023328
- **Type**: conference
- **Published**: 2002
- **Authors**: J. Boutros, G. Caire, E. Viterbo +2
- **PDF**: https://ieeexplore.ieee.org/document/1023328
- **Abstract**: We propose a rate 1/3 infinite-length irregular turbo code capable of achieving an error rate P/sub eb/=10/sup -5/ at signal-to-noise ratio E/sub b//N/sub 0/=-0.46 dB, which is at distance 0.03 dB from Shannon capacity limit. Our turbo code is derived by a simple modification of the original Berrou-Glavieux code.

## Design of low-density parity-check codes for noncoherent MPSK communication

- **Status**: ❌
- **Reason**: noncoherent MPSK 통신용 LDPC 설계로 무선 채널 특이적, NAND로 이식할 일반 디코더/구성 기여 없음
- **ID**: ieee:1023441
- **Type**: conference
- **Published**: 2002
- **Authors**: Hui Jin, T. J. Richardson
- **PDF**: https://ieeexplore.ieee.org/document/1023441
- **Abstract**: We present an approach for designing low-density parity-check codes for noncoherent MPSK communication. Codes designed by this approach perform very close to noncoherent AWGN MPSK modulated channel capacity.

## Low delay burst erasure correction codes

- **Status**: ❌
- **Reason**: burst erasure correction 코드, LDPC 아니며 VoIP 실시간 패킷복구용 — 떼어낼 바이너리 LDPC ECC 기법 없음
- **ID**: ieee:997146
- **Type**: conference
- **Published**: 2002
- **Authors**: E. Martinian, C. . -E. W. Sundberg
- **PDF**: https://ieeexplore.ieee.org/document/997146
- **Abstract**: In a variety of networks, packet losses occur in bursts. Conventional application of error correction codes for packet recovery often requires interleaving and long decoder delays. These long delays are usually unacceptable in real-time multimedia communication applications such as voice over IP (VoIP). Consequently, erasure correction codes with severe limits on delay are desirable. We present various codes suitable for correcting bursts of lost packets. In addition, we show that these codes have the shortest possible decoding delay. To demonstrate the practical benefits of these codes for VoIP, we present results of informal mean opinion score listening tests conducted with various codes.

## Integrated iterative equalization for ARQ systems

- **Status**: ❌
- **Reason**: ARQ turbo-equalizer 결합 등화로 통신 수신기 응용 특이적, 바이너리 LDPC ECC로 이식할 기법 없음
- **ID**: ieee:1023468
- **Type**: conference
- **Published**: 2002
- **Authors**: H. Samra, Z. Ding
- **PDF**: https://ieeexplore.ieee.org/document/1023468
- **Abstract**: An integrated approach is presented to enhance receiver performance for ARQ communication systems in rapidly-changing environments. This approach only requires a simple modification to the traditional turbo-equalizer by integrating multiple transmissions for joint equalization of multiple systematic codewords, leading to a computationally efficient joint receiver with improved performance.

## Irregular repeat accumulate codes for non-binary modulation schemes

- **Status**: ❌
- **Reason**: IRA 부호의 비이진 변조(TCM/멀티레벨) 성능 리뷰로 변조 응용 특이적, 떼어낼 신규 LDPC 기법 없음
- **ID**: ieee:1023443
- **Type**: conference
- **Published**: 2002
- **Authors**: A. Khandekar, R. Palanki
- **PDF**: https://ieeexplore.ieee.org/document/1023443
- **Abstract**: In this paper, we review the performance of irregular repeat accumulate (IRA) codes. We present simulation results on the performance of IRA codes in two non-binary modulation schemes viz., turbo-coded modulation and multilevel coding. These results show that IRA codes are good for high data rate applications and that multilevel coding with IRA codes provides a low complexity alternative to TCM.

## Gallager codes for multiple user applications

- **Status**: ❌
- **Reason**: Gallager(LDPC) 코드의 다중접속 시스템 응용·성능한계로, 떼어낼 디코더/HW/구성 기여 없음 — 무선/통신 응용 특이적
- **ID**: ieee:1023607
- **Type**: conference
- **Published**: 2002
- **Authors**: A. de Baynast, D. Declercq
- **PDF**: https://ieeexplore.ieee.org/document/1023607
- **Abstract**: We study the performance limits of a multiple access system based on the Gallager codes. We show that we can bypass the spreading sequences in a multiple access system. The algebraic orthogonality is replaced by a statistical orthogonality provided by the randomness of the Gallager codes. The performance of our system are close to the optimum achievable bound.

## On the minimum distance of turbo codes

- **Status**: ❌
- **Reason**: turbo code 인터리버/최소거리 설계로 비-LDPC 부호 구성, 이식 가능한 LDPC 기법 없음
- **ID**: ieee:1023356
- **Type**: conference
- **Published**: 2002
- **Authors**: D. Truhachev, M. Lentmaier, O. Wintzell +1
- **PDF**: https://ieeexplore.ieee.org/document/1023356
- **Abstract**: A permutor (interleaver) design method is presented to show the existence of turbo codes with minimum distance growing logarithmically with the permutor length. It is demonstrated, that the method can also be useful for the construction of turbo codes with practical block lengths.

## Magnetic recording demonstration over 100 Gbit/In/sup 2/

- **Status**: ❌
- **Reason**: 100Gbit/in2 자기기록 헤드/미디어 데모 — ECC/LDPC 기법 없는 물리매체 시연
- **ID**: ieee:1000771
- **Type**: conference
- **Published**: 2002
- **Authors**: Zhengyong Zhang, Yong Chang Feng, T. Clinton +18
- **PDF**: https://ieeexplore.ieee.org/document/1000771
- **Abstract**: Summary form only given. Areal density growth has instigated the development of higher performance and lower cost disc drives. This has enabled us to fulfill the demands from new enterprise, desktop and consumer applications. The achievement of 100Gb/in2 areal density is a milestone to be reported in this presentation. The recording demonstration employed fully integrated magnetic recording heads and multi-layer antiferromagnetic coupled (AFC) media.

## Information geometry of turbo codes

- **Status**: ❌
- **Reason**: turbo 디코딩의 정보기하학적 분석으로 turbo 전용, 바이너리 LDPC BP로 떼어낼 구체 기법 없음
- **ID**: ieee:1023386
- **Type**: conference
- **Published**: 2002
- **Authors**: S. Ikeda, T. Tanaka, S. Amari
- **PDF**: https://ieeexplore.ieee.org/document/1023386
- **Abstract**: The properties of turbo decoding is studied from information geometrical viewpoint. Our study gives an intuitive understanding of the theoretical background, and a new framework for the analysis. Based on the framework, we reveal basic properties of the turbo decoding.

## Retry mode soft Reed-Solomon decoding

- **Status**: ❌
- **Reason**: soft Reed-Solomon 디코딩 retry 기법; 비-LDPC 부호이고 RS 전용 디코딩이라 LDPC BP 이식성 없음
- **ID**: ieee:1001130
- **Type**: conference
- **Published**: 2002
- **Authors**: Haitao Xia, Hongxin Song, J. R. Cruz
- **PDF**: https://ieeexplore.ieee.org/document/1001130
- **Abstract**: Summary form only given. In this paper, we propose a new retry mode scheme for magnetic recording systems based on a soft Reed-Solomon (RS) decoding algorithm . Instead of using asymptotic bounds, we present realistic simulation results over partial response channels, and discuss some practical implementation issues such as system architecture and erasures due to disk defects and thermal asperities. Simulation results show that a significant performance improvement can be obtained without increasing hardware complexity.

## Ultra Long-Haul High-Speed Transmission

- **Status**: ❌
- **Reason**: 40Gb/s 장거리 광전송 데모; LDPC 언급 없고 ECC 이식 기법 없음
- **ID**: ieee:1601318
- **Type**: conference
- **Published**: 2002
- **Authors**: J. -X. Cai, M. Nissov, C. R. Davidson +1
- **PDF**: https://ieeexplore.ieee.org/document/1601318
- **Abstract**: Transmission of 40 Gb/s signals over long distances presents numerous technical challenges. Rapid progress in key enabling technologies has allowed laboratory transmission demonstration of 40 Gb/s DWDM channels over transoceanic distances

## A highly parallel decoder for turbo codes

- **Status**: ❌
- **Reason**: 터보 코드 병렬 디코더, LDPC는 비교 참고만, 떼어낼 LDPC 기법 없음
- **ID**: ieee:1023500
- **Type**: conference
- **Published**: 2002
- **Authors**: J. Sun, O. Y. Takeshita, M. P. Fitz
- **PDF**: https://ieeexplore.ieee.org/document/1023500
- **Abstract**: A highly parallel decoder for turbo codes is investigated. The decoding delay of the decoder is approximately independent of the frame length. Analysis similar to those applied to low density parity check codes is possible and a "threshold" can be found.

## Enabling technologies for long-haul 40 Gb/s WDM transmission

- **Status**: ❌
- **Reason**: 40Gb/s WDM 광전송 응용 개요, FEC 부수 언급일 뿐 떼어낼 LDPC 기법 없음
- **ID**: ieee:1134057
- **Type**: conference
- **Published**: 2002
- **Authors**: Jin-Xing Cai, M. Nissov, C. R. Davidson +1
- **PDF**: https://ieeexplore.ieee.org/document/1134057
- **Abstract**: 40 Gb/s transmission over long distances presents numerous technical challenges. Rapid progress in key technological areas has allowed laboratory demonstration of 40 Gb/s DWDM transmission over transoceanic distances. The primary approach is quasi-linear transmission over dispersion flattened spans. Quasi-linear transmission is made possible by rapid advances in the key technological areas of transmission fiber, modulation formats, FEC codes, and distributed Raman amplification.

## LDPC code design for turbo equalization

- **Status**: ❌
- **Reason**: turbo equalization용 LDPC EXIT 설계 — ISI 채널 무선 특이적, NAND 이식 구성/디코더 기여 없음
- **ID**: ieee:1115415
- **Type**: conference
- **Published**: 2002
- **Authors**: K. R. Narayanan, Xiaodong Wang, Guosen Yue
- **PDF**: https://ieeexplore.ieee.org/document/1115415
- **Abstract**: We discuss techniques to characterize the probability density function of the extrinsic information at the output of a soft interference canceler based equalizer when used in a turbo equalizer. Then, we show how to use this to compute thresholds for low density parity check (LDPC) codes and to design good LDPC code ensembles for static and time-varying intersymbol interference channels. For other types of equalizers, we propose to design LDPC codes whose extrinsic information transfer (EXIT) diagram is matched to that of the equalizer.

## LDPC Codes for Long Haul Optical Communications

- **Status**: ❌
- **Reason**: 광통신 FEC에 LDPC 적용 결과만 보고; 떼어낼 신규 디코더/HW/코드설계 기여 없음(응용 특이적)
- **ID**: ieee:1601248
- **Type**: conference
- **Published**: 2002
- **Authors**: B. Vasic, I. B. Djordjevic
- **PDF**: https://ieeexplore.ieee.org/document/1601248
- **Abstract**: FEC scheme based on LDPC codes is presented in this paper. We show that LDPC codes provide a significant system performance improvement with respect to the state-of-the-art FEC schemes employed in optical communications systems.

## High rate coded OFDM with channel equalization

- **Status**: ❌
- **Reason**: OFDM+LDPC 무선 시스템, LDPC 부수 언급, 떼어낼 디코더/HW/구성 신규 기여 없음
- **ID**: ieee:1187069
- **Type**: conference
- **Published**: 2002
- **Authors**: D. M. Gruenbacher, A. Serener
- **PDF**: https://ieeexplore.ieee.org/document/1187069
- **Abstract**: We consider the use of wideband systems for the fixed point-to-point transmission of coded data with low bit-error rate requirements. A system is defined which is based on OFDM transmission with PSK and QAM subcarrier modulation, error control coding using low-density parity-check (LDPC) codes, and channel equalization to reduce intersymbol interference from a fading channel. Tradeoffs between modulation parameters and equalization complexity are also discussed. High rate LDPC codes are considered for this system.

## Compression of binary sources with side information using low-density parity-check codes

- **Status**: ❌
- **Reason**: Slepian-Wolf 측면정보 소스 압축(syndrome 기반) — 채널 ECC가 아닌 소스 코딩이라 제외
- **ID**: ieee:1188407
- **Type**: conference
- **Published**: 2002
- **Authors**: A. D. Liveris, Zixiang Xiong, C. N. Georghiades
- **PDF**: https://ieeexplore.ieee.org/document/1188407
- **Abstract**: It is shown how low-density parity-check (LDPC) codes can be used as an application of the Slepian-Wolf (1973) theorem for correlated binary sources. We focus on the asymmetric case of compression with side information. The approach is based on viewing the correlation as a channel and applying the syndrome concept. The encoding and decoding procedures, i.e. the compression and decompression, are explained in detail. The simulated performance results are better than most of the existing turbo code results available in the literature and very close to the Slepian-Wolf limit.

## Blind synchronization with enhanced sum-product algorithm for low-density parity-check codes

- **Status**: ❌
- **Reason**: LDPC blind sync(타이밍/캐리어 복구)용 enhanced SPA — 무선 동기화 특이적, NAND ECC로 떼어낼 디코더 기법 없음
- **ID**: ieee:1088321
- **Type**: conference
- **Published**: 2002
- **Authors**: W. Matsumoto, H. Imai
- **PDF**: https://ieeexplore.ieee.org/document/1088321
- **Abstract**: We propose a blind synchronization scheme with soft phase error canceller using the sum-product algorithm for LDPC codes. Our scheme can perform frame synchronization, timing recovery, and carrier recovery without a phase lock loop (PLL). Furthermore, our scheme does not use a training signal and/or a preamble signal. The paper proposes the enhanced sum-product algorithm for the situations when the phase error is given by sample timing offset and carrier frequency offset. We show it is possible to perform the synchronization blindly, since the parameters of phase error can be estimated by the minimization of mean square error (MMSE) calculation with soft bits output of the sum-product algorithm.

## Concatenated space-time codes for quasi-static fading channels: constrained capacity and code design

- **Status**: ❌
- **Reason**: 연접 space-time 부호 설계, LDPC는 MIMO에서 capacity 접근용 표준 사용, 신규 LDPC 기법 없음
- **ID**: ieee:1188387
- **Type**: conference
- **Published**: 2002
- **Authors**: V. Gulati, K. R. Narayanan
- **PDF**: https://ieeexplore.ieee.org/document/1188387
- **Abstract**: The problem of designing codes with close-to-capacity performance on the multiple-input multiple-output (MIMO) quasi-static fading channel (QSFC) is addressed. We consider three different coding schemes - namely, direct transmission of random-like codes, concatenation with linear processing orthogonal space-time block codes (o-STBC) and concatenation with space-time trellis codes (STTC). The constrained modulation outage capacity of each of these schemes is computed. It is shown how low-density parity check (LDPC) codes may be used to approach capacity in these cases. For the STTC, the serial concatenation scheme of Gulati et al. (2001) turns out to have close to capacity performance.

## Integrated iterative equalization for ARQ systems

- **Status**: ❌
- **Reason**: ARQ turbo-equalizer 통합 기법; LDPC는 시뮬 대상일 뿐 떼어낼 디코더 기여 없음
- **ID**: ieee:5745225
- **Type**: conference
- **Published**: 2002
- **Authors**: H. Samra, Z. Ding
- **PDF**: https://ieeexplore.ieee.org/document/5745225
- **Abstract**: In this paper, a new approach is presented to enhance receiver performance for ARQ communication systems that use systematic codes in rapidly-changing environments. This new approach involves a simple modification to the traditional turbo-equalizer by integrating multiple ARQ transmissions for joint equalization of systematic codewords. This modification provides a computationally efficient joint receiver that improves frame error rates and throughput when compared with a few other simple approaches. To analyze the receiver, simulation results are presented for two types of systematic codes: recursive systematic codes (RSC) and low-density parity check codes (LDPC). Results are also presented for a hybrid ARQ system where subsequent transmissions contain only portions of the original transmission.

## Towards closing the capacity gap on multiple antenna channels

- **Status**: ❌
- **Reason**: 다중안테나 sphere decoder(Fincke-Pohst) 수정; LDPC는 부수 언급, MIMO 검출 기법으로 NAND LDPC BP에 이식성 없음
- **ID**: ieee:5745126
- **Type**: conference
- **Published**: 2002
- **Authors**: H. Vikalo, B. Hassibi
- **PDF**: https://ieeexplore.ieee.org/document/5745126
- **Abstract**: In recent years, soft iterative decoding techniques have been shown to greatly improve the bit error rate performance of various communication systems. For multiple antenna systems, however, it is not clear what is the best way to obtain the soft-information required of the iterative scheme with low complexity. In this paper, we propose a modification of the Fincke-Pohst (sphere decoder) algorithm to estimate the MAP probability of the received symbol sequence. The new algorithm solves a nonlinear integer leasts-quares problem and, over a wide range of rates and SNRs, has polynomial-time (often cubic) complexity. The performance of the algorithm, combined with convolutional, turbo, and LDPC codes is demonstrated on several multiple antenna channels.

## Magnetization enumerator for LDPC codes - a statistical physics approach

- **Status**: ❌
- **Reason**: 통계물리 자화 enumerator로 임계잡음 분석 — 순수 이론 bound, 디코더/HW/구성으로 안 이어짐
- **ID**: ieee:1023528
- **Type**: conference
- **Published**: 2002
- **Authors**: J. van Mourik, D. Saad, Y. Kabashima
- **PDF**: https://ieeexplore.ieee.org/document/1023528
- **Abstract**: We propose a method based on the magnetization enumerator to determine the critical noise level for Gallager type low density parity check error correcting codes (LDPC). Our method provides an appealingly simple interpretation to the relation between different decoding schemes, and provides more optimistic critical noise levels than those reported in the information theory literature.

## Wyner-Ziv coding of motion video

- **Status**: ❌
- **Reason**: Wyner-Ziv 비디오 소스코딩(분산 소스코딩)으로 채널 ECC 아님, LDPC 무관 — 소스코딩 제외
- **ID**: ieee:1197184
- **Type**: conference
- **Published**: 2002
- **Authors**: A. Aaron, Rui Zhang, B. Girod
- **PDF**: https://ieeexplore.ieee.org/document/1197184
- **Abstract**: In current interframe video compression systems, the encoder performs predictive coding to exploit the similarities of successive frames. The Wyner-Ziv theorem on source coding with side information available only at the decoder suggests that an asymmetric video codec, where individual frames are encoded separately, but decoded conditionally (given temporally adjacent frames) could achieve similar efficiency. We report the first results on a Wyner-Ziv coding scheme for motion video that uses intraframe encoding, but interframe decoding.

## Convergence prediction for iterative decoding of threefold concatenated systems

- **Status**: ❌
- **Reason**: concatenated 시스템 EXIT chart 수렴분석, LDPC 전용 디코더/코드설계 기여 없음
- **ID**: ieee:1188420
- **Type**: conference
- **Published**: 2002
- **Authors**: M. Tuchler
- **PDF**: https://ieeexplore.ieee.org/document/1188420
- **Abstract**: We show how to use EXIT charts for convergence prediction of a threefold serially concatenated system. The corresponding chart has three dimensions and allows us to appropriately select system parameters and to find an optimal schedule of decoding iterations between the three decoders of such a system. Convergence thresholds are obtained to determine the minimal signal-to-noise ratios for which convergence is possible. It turns out that threefold concatenated systems do not achieve any additional performance gain compared to suitably designed twofold systems. We conclude that a threefold concatenation should be considered only when the decoders cannot be chosen freely.

## Joint source-channel coding of binary sources with side information at the decoder using IRA codes

- **Status**: ❌
- **Reason**: IRA 부호로 사이드정보 결합 소스-채널 코딩(Slepian-Wolf) — 채널 ECC 아닌 JSCC, 떼어낼 BP 기법 없음
- **ID**: ieee:1203246
- **Type**: conference
- **Published**: 2002
- **Authors**: A. D. Liveris, Zixiang Xiong, C. N. Georghiades
- **PDF**: https://ieeexplore.ieee.org/document/1203246
- **Abstract**: We use systematic irregular repeat accumulate (IRA) codes as source-channel codes for the transmission of an equiprobable memoryless binary source with side information at the decoder. A special case of this problem is joint source-channel coding for a nonequiprobable memoryless binary source. The theoretical limits of this problem are given by combining the Slepian-Wolf theorem, the source entropy in the special case, with the channel capacity. The approach is based on viewing the correlation between the binary source output and the side information as a separate channel or an enhancement of the original channel. The joint source-channel encoding, decoding and code design procedures are explained in detail. The simulated performance results are better than the recently published solutions using turbo codes and very close to the theoretical limit.

## Iterative decoding schemes for source and joint source-channel coding of correlated sources

- **Status**: ❌
- **Reason**: 저밀도 생성행렬(LDGM) 기반 소스/JSCC 상관소스 코딩 — 채널 ECC 아니고 JSCC, 떼어낼 LDPC ECC 기법 없음
- **ID**: ieee:1197186
- **Type**: conference
- **Published**: 2002
- **Authors**: J. Garcia-Frias, W. Zhong, Y. Zhao
- **PDF**: https://ieeexplore.ieee.org/document/1197186
- **Abstract**: We propose the use of linear codes with low density generator matrix for channel coding, and joint source-channel coding of correlated sources. The use of iterative decoding techniques, i.e. message passing, over the corresponding graph achieves a performance close to the theoretical limits. As an advantage with respect to turbo and standard low-density parity check codes, the complexity of the decoding and encoding procedures is very low.

## Potential of chaos communication over noisy channels - channel coding using chaotic piecewise linear maps

- **Status**: ❌
- **Reason**: 카오스 통신 정보이론 분석; LDPC/ECC 디코더 기법 무관
- **ID**: ieee:1010519
- **Type**: conference
- **Published**: 2002
- **Authors**: M. Hasler, T. Schimming
- **PDF**: https://ieeexplore.ieee.org/document/1010519
- **Abstract**: The paper gives an information theoretic analysis of the potential of chaos in digital communication schemes, underlining that there is no fundamental principle that speaks against the use of chaotic systems in digital communications. The channel model considered throughout the paper is that of additive white Gaussian noise (AWGN). In particular, an example using the dyadic shift (Bernoulli shift) map is presented to illustrate the fact that the use of chaotic piecewise linear maps has no systematic negative effect for digital communications applications.

## Iterative decoding in a two-node distributed array

- **Status**: ❌
- **Reason**: 분산 2-노드 네트워크 공간다이버시티+SISO 신뢰도교환 기법, NAND LDPC BP/HW/구성에 떼어낼 기여 없음
- **ID**: ieee:1179671
- **Type**: conference
- **Published**: 2002
- **Authors**: T. F. Wong, Xin Li, J. M. Shea
- **PDF**: https://ieeexplore.ieee.org/document/1179671
- **Abstract**: This paper investigates the possibility of using a network-based approach to obtain spatial diversity without the use of physical antenna arrays. To this end, we examine the simple case of a two-node network. A distant transmitter sends a packet of coded data bits to the two nodes in the network. Each of the two nodes receives an independent copy of the transmitted signal. Each node decodes the signal that it receives and generates reliability estimates (soft outputs) for the transmitted data bits. The two nodes then exchange soft outputs of a small portion of the bits that are least reliable. Upon receiving additional information about the least reliable bits from another node, a node will restart the decoding process. This process of information exchange and iterative decoding then continues for a number of iterations. With a properly chosen coding and information exchange strategy, simulation results show that a close-to-full diversity advantage can be achieved using the proposed scheme, requiring exchanging only a small amount of information between the two nodes.

## On the construction of turbo code interleavers based on graphs with large girth

- **Status**: ❌
- **Reason**: 터보코드 인터리버를 large-girth 그래프로 구성 — 비-LDPC, 터보 전용 인터리버 설계로 LDPC BP/구성에 직접 이식되는 기여 아님
- **ID**: ieee:997082
- **Type**: conference
- **Published**: 2002
- **Authors**: P. O. Vontobel
- **PDF**: https://ieeexplore.ieee.org/document/997082
- **Abstract**: We discuss how interleavers for parallel concatenated turbo codes with good minimum distance can be derived from graphs having large girth, i.e. graphs whose length of the shortest cycle is large.

## Iteratively decodable codes for bridging the shaping gap in communication channels

- **Status**: ❌
- **Reason**: shaping gap/trellis shaping 무선 응용, LDPC는 베이스라인이고 떼어낼 ECC 기법 없음
- **ID**: ieee:1197140
- **Type**: conference
- **Published**: 2002
- **Authors**: N. Varnica, Xiao Ma, A. Kavcic
- **PDF**: https://ieeexplore.ieee.org/document/1197140
- **Abstract**: We consider the power-constrained complex memoryless additive white Gaussian noise channel whose channel inputs are drawn from a finite alphabet. It is well known that if the probability mass function over the finite alphabet is uniform, a shaping gap is created that asymptotically approaches 1.53 dB as the constellation cardinality approaches infinity. In a recent paper, we proposed a method to compute the shaping gap for a finite alphabet size and finite SNR. Here, we take advantage of the constellations that can be represented as cross products of the in-phase (real) and quadrature (imaginary) unidimensional constellations. For a 256-QAM constellation, we construct separate simple in-phase and quadrature inner trellis codes whose combined information rate bridges (and nearly closes) the shaping gap. We then demonstrate that a judiciously constructed outer iteratively decodable low-density parity-check code performs inside the shaping gap, which is very near the channel capacity.

## Low-complexity iterative detection and decoding of multi-antenna systems employing channel and space-time codes

- **Status**: ❌
- **Reason**: 다중안테나 시공간 검출(Fincke-Pohst 기반 MAP soft 검출) — LDPC 디코더 아님, 무선 검출 특이적 제외
- **ID**: ieee:1197194
- **Type**: conference
- **Published**: 2002
- **Authors**: H. Vikalo, B. Hassibi
- **PDF**: https://ieeexplore.ieee.org/document/1197194
- **Abstract**: We study multiple antenna systems that employ space-time modulation schemes and transmit data encoded by powerful channel codes. Decoders for such codes require probabilistic (soft) information about transmitted bits. We use a modification of the Fincke-Pohst algorithm to solve maximum a posteriori detection problem and efficiently approximate soft information. Simulation results that illustrate performance of the proposed system are presented.

## n-channel multiple descriptions: theory and constructions

- **Status**: ❌
- **Reason**: 다중설명(MD) 소스-채널 erasure 코딩 이론·구성, 채널 ECC 아니고 스칼라 양자화+선형부호 — 떼어낼 LDPC 디코더 없음
- **ID**: ieee:999964
- **Type**: conference
- **Published**: 2002
- **Authors**: R. Puri, S. S. Pradhan, K. Ramchandran
- **PDF**: https://ieeexplore.ieee.org/document/999964
- **Abstract**: We present new achievable rate regions and code constructions for the symmetric n-channel multiple descriptions (MD) coding problem (Puri et al. (2002)) for n>2. Our approach is inspired by unexplored connections between MD and the problem of distributed source coding (Slepian et al. (1973); Wyner et al. (1976)). For illustrative clarity, we restrict our focus to the important special case relating to (n, k) source-channel erasure codes (Pradhan et al. (2001)). This involves n encodings of a source with the goal of maximizing its reconstruction fidelity with the availability of any k of them, while strictly improving this reconstruction fidelity with the availability of more than k descriptions. We describe the underlying information-theoretic framework, and then formulate practical constructions based on scalar quantizers and linear channel codes for the n=3 case to illustrate our concepts.

## Video transmission for multi-hop networks using IEEE 802.11 FHSS

- **Status**: ❌
- **Reason**: IEEE 802.11 FHSS 비디오 전송·Viterbi 수신기 — LDPC 무관, 떼어낼 ECC 기법 없음
- **ID**: ieee:1037948
- **Type**: conference
- **Published**: 2002
- **Authors**: K. Ban, H. Gharavi
- **PDF**: https://ieeexplore.ieee.org/document/1037948
- **Abstract**: In many applications, such as construction, manufacturing, ground robotic vehicles, and rescue operations, there are many issues that necessitate the capability of transmitting digital video and that such transmissions should be performed wirelessly and in an ad-hoc manner. Recently, we proposed an ad-hoc, cluster-based, multi-hop network architecture for video communications (see Gharavi, H. and Ban, K., 3G Wireless Conference, 2002). For implementation, the IEEE 802.11 FHSS wireless LAN system using 2GFSK modulation was employed. To enhance the overall throughput rate for higher quality video communications, we present a performance evaluation of the IEEE 802.11 FHSS when 4GFSK modulation option is selected. Unfortunately, the 2 Mb/s system utilizing 4GFSK modulation is not very efficient in terms of RF range. Therefore, to improve its performance for multi-hop applications, a combination of diversity and non-coherent Viterbi based receiver is considered. For the video transmission part, we have considered a bitstream. splitting technique together with a packet-based error protection strategy to combat packet drops under multipath fading conditions. Finally, the paper presents simulation results, including the effects of receiver design and diversity on the quality of the received video signals.

## Scalable image transmission using rate-compatible irregular repeat accumulate (IRA) codes

- **Status**: ❌
- **Reason**: IRA(turbo계열) 비-LDPC 부호의 펑처링/UEP — 바이너리 LDPC BP에 그대로 이식되는 디코더 기여 없음
- **ID**: ieee:1039072
- **Type**: conference
- **Published**: 2002
- **Authors**: Chingfu Lan, K. R. Narayanan, Zixiang Xiong
- **PDF**: https://ieeexplore.ieee.org/document/1039072
- **Abstract**: This paper considers designing and applying rate-compatible irregular repeat accumulate (IRA) codes for scalable image transmission over binary symmetric channels. IRA codes of different rates are obtained by puncturing the parity bits of a mother IRA code which uses a systematic encoder. One of the main ideas presented here is the design of the mother code such that the entire set of higher rate codes obtained by puncturing are good. Using the Viterbi algorithm for finding the optimal unequal error protection of JPEG2000 bit streams, we present better results with IRA codes than those reported with turbo codes. The proposed IRA codes also have lower decoding complexity than the turbo codes.

## On the design, simulation and analysis of parallel concatenated Gallager codes

- **Status**: ❌
- **Reason**: LDPC 성분코드 기반 병렬연접(PCGC) 연접부호 구성으로 무선 채널·delay 응용 특이적, 떼어낼 단일 바이너리 LDPC 디코더/구성 기여 약함
- **ID**: ieee:997168
- **Type**: conference
- **Published**: 2002
- **Authors**: H. Behairy, Shih-Chun Chang
- **PDF**: https://ieeexplore.ieee.org/document/997168
- **Abstract**: We present a framework for designing a class of concatenated codes based on low-density parity-check component codes that we call parallel concatenated Gallager codes (PCGC). The iterative decoding trajectories technique is used to explain the performance of PCGC. Simulation results show an enhanced performance in the practical E/sub b//N/sub 0/ range in both AWGN and flat Rayleigh fading channels. The reduced decoding complexity of the proposed coding scheme along with its good performance makes it an attractive candidate in delay sensitive applications.

## Polynomial-complexity, adaptive symbol-by-symbol soft-decision algorithms with application to non-coherent detection of LDPCC

- **Status**: ❌
- **Reason**: 미지 반송파 위상하 LDPC 비동기 검출용 SbSSDM 메트릭 생성 — 채널 추정 결합 기법으로 NAND 디지털 ECC로 이식성 약함
- **ID**: ieee:997134
- **Type**: conference
- **Published**: 2002
- **Authors**: I. Motedayen, A. Anastasopoulos
- **PDF**: https://ieeexplore.ieee.org/document/997134
- **Abstract**: Iterative decoding in the presence of unknown channel parameters requires the generation of symbol-by-symbol soft-decision metrics (SbSSDMs), jointly with parameter estimation. Traditional methods for the exact evaluation of these metrics have exponential complexity with the length of the data sequence. In this paper, a class of problems is identified, for which the exact SbSSDMs can be obtained with only polynomial complexity with the data sequence length. The applicability of this technique is demonstrated by considering the problem of iterative detection of low-density parity-check codes in the presence of unknown and time-varying carrier-phase offset.

## Analysis and design of natural and threaded space-time codes with iterative decoding

- **Status**: ❌
- **Reason**: 시공간 부호 설계+반복 검출(간섭제거 디코더), LDPC 아님 — 무선 응용 특이적, 이식 LDPC BP 기법 없음
- **ID**: ieee:1197191
- **Type**: conference
- **Published**: 2002
- **Authors**: A. Guillen i Fabregas, G. Caire
- **PDF**: https://ieeexplore.ieee.org/document/1197191
- **Abstract**: We consider code design of threaded and natural space-time codes and analyze their performance. We show by a counter example that, for these codes, even if the binary rank criterion is not satisfied, they demonstrate full diversity performance in the region of interest when iterative decoding is used. Hence, the relevant parameter for efficient code design is not the rank diversity. We conjecture that this parameter is the block-diversity. We provide simulation results, and, in order to reinforce our conjecture, we analyze the behavior of the iterative interference cancellation decoder by using density evolution with the Gaussian approximation.

## Performance analysis of augmented RAC codes under memoryless conditions

- **Status**: ❌
- **Reason**: RAC array/SPC 부호 + 트렐리스 ML 디코딩 — 비-LDPC 부호이고 BP 이식 기여 없음, 제외.
- **ID**: ieee:1029138
- **Type**: conference
- **Published**: 2002
- **Authors**: L. Kaya
- **PDF**: https://ieeexplore.ieee.org/document/1029138
- **Abstract**: Augmentation of row and column (RAC) array codes based on single parity check codes is presented. The augmentation is performed by superimposition of information bits to parity check positions of the original RAC code. The augmentation technique has a simple construction procedure and allows us to create new codes from existing ones. A compact trellis diagram of these codes has been constructed. Maximum-likelihood decoding using either hard-decision or soft-decision detection schemes using a trellis diagram has been implemented and results are presented. Code rate improvements and performance characteristics of the augmentation technique are given.

## Fast joint source-channel coding algorithms for Internet/wireless multimedia

- **Status**: ❌
- **Reason**: JSCC 멀티미디어 UEP 최적화; 채널 LDPC ECC 기법 아님, 소스-채널 결합으로 제외
- **ID**: ieee:1007467
- **Type**: conference
- **Published**: 2002
- **Authors**: R. Hamzaoui, V. Stankovic, Zixiang Xiong
- **PDF**: https://ieeexplore.ieee.org/document/1007467
- **Abstract**: We consider joint source-channel coding for Internet and wireless multimedia applications. Embedded source bitstreams are protected against noise in both binary symmetric channels (BSC) and packet erasure channels. For each channel, a local search joint source-channel coding (JSCC) algorithm is proposed to search for the optimal unequal error protection (UEP) scheme. Each algorithm starts with a linear-complexity step that maximizes the number of correctly decoded source bits, followed by a quick local refinement of the resulting UEP solution to minimize the average distortion. Experiments for both binary symmetric channels and packet erasure channels with the SPIHT, JPEG2000 and 3D SPIHT coders show that our local search algorithms are near-optimal in performance, whereas they are orders of magnitude faster than the best previous solutions.

## Iterative reliability-based decoding of turbo-like codes

- **Status**: ❌
- **Reason**: 터보형 부호의 신뢰도 기반 반복 디코딩 — 비-LDPC, 터보 전용 구성에 의존
- **ID**: ieee:997099
- **Type**: conference
- **Published**: 2002
- **Authors**: M. Isaka, M. Fossorier, H. Imai
- **PDF**: https://ieeexplore.ieee.org/document/997099
- **Abstract**: In this paper, the use of a reliability-based decoding algorithm for some concatenated codes with an interleaver, known as turbo-like codes, is examined to address and overcome the suboptimality of iterative decoding. Simulation results show that the suboptimality of iterative decoding for moderate length codes can be at least partially compensated by this combined approach. Some insights about the potential additional coding gains achievable by the combined approach are investigated based on the characteristics of the constituent decoders, which highlights the nature of suboptimality in iterative decoding.

## Analysis and design of pilot-symbol-assisted codes, for the noncoherent AWGN channel, using density evolution

- **Status**: ❌
- **Reason**: 비동기 AWGN 파일럿심볼 코드 설계 + density evolution 무선 응용, 떼어낼 LDPC 디코더/구성 기법 없음
- **ID**: ieee:997102
- **Type**: conference
- **Published**: 2002
- **Authors**: R. Nuriyev, A. Anastasopoulos
- **PDF**: https://ieeexplore.ieee.org/document/997102
- **Abstract**: Pilot-symbol-assisted transmission of coded data over the block independent noncoherent AWGN channel is considered in this paper. Several iterative receivers are proposed and their performance is analyzed using density evolution. Upper and lower performance bounds are derived for the receiver based on the sum-product algorithm, and the optimal allocation of power to the pilots and coded bits is investigated. It is discovered that the optimal power allocation affects considerably the achievable performance, and depends highly on the phase dynamics. These results are verified by simulating practical codes and iterative receivers.

## Analysis of the iterative decoding of product codes using the Gaussian approximation

- **Status**: ❌
- **Reason**: product code 반복디코딩 가우시안 근사 분석, LDPC BP 이식 기여 없는 비-LDPC 부호
- **ID**: ieee:1188419
- **Type**: conference
- **Published**: 2002
- **Authors**: F. Lehmann, G. M. Maggio
- **PDF**: https://ieeexplore.ieee.org/document/1188419
- **Abstract**: In this paper we introduce a model of the iterative decoding of product codes. For each iteration, an approximation of the bit error rate (BER) at the output of the decoders is used to evaluate the density of the extrinsic information. The decoding thresholds obtained for the additive white Gaussian noise (AWGN) and the Rayleigh fading channel are consistent with the simulation results available in the literature.

## Performance of space-time codes over a flat-fading channel using a subspace-invariant detector

- **Status**: ❌
- **Reason**: MIMO 시공간 부호+LDPC 외부부호 부수 사용; 표준 LDPC를 갖다 쓴 수준, 떼어낼 신규 디코더/구성 없음
- **ID**: ieee:1197280
- **Type**: conference
- **Published**: 2002
- **Authors**: K. W. Forsythe
- **PDF**: https://ieeexplore.ieee.org/document/1197280
- **Abstract**: Multiple-input, multiple-output (MIMO) communications has received considerable attention in recent years. The flat-fading channel, with identical, independently distributed gains between all transmitter and receiver pairs has been one of the MIMO channels studied extensively. Many studies have focused on channel capacity and coding in additive white Gaussian noise. When the noise background has an unknown spatial covariance due to interference, receivers that adapt to the noise background can be more robust. One way of achieving robustness builds invariances into the detector, creating a channel model that incorporates adaptive beamforming naturally into signal detection and coding. In the particular case of frequency-hopped waveforms with random fading and hop to hop white noise, the capacity of this channel can be evaluated. A family of space-time codes for the invariant detector is investigated and its performance compared with the derived capacity bounds. Theoretical predictions of performance in interference and in different fading conditions are presented and compared with simulation results for a concatenated coding architecture involving space-time inner codes and low density parity-check outer code.

## Low-complexity iterative per-antenna MAP equalizer for MIMO frequency selective fading channels

- **Status**: ❌
- **Reason**: MIMO MAP 등화기 복잡도 저감 기법으로 LDPC 부호/디코더 기여 없음, 떼어낼 ECC 기법 없음
- **ID**: ieee:1188370
- **Type**: conference
- **Published**: 2002
- **Authors**: V. Gulati, Heung-no Lee
- **PDF**: https://ieeexplore.ieee.org/document/1188370
- **Abstract**: We consider the equalization of a (N/sub t/, N/sub r/) MIMO, L + 1-tap fading channel. We first evaluate the performance of a full complexity, vector MAP equalizer which runs the forward/backward algorithm on a trellis which has M(N/sub t//spl times/L) states with M(N/sub t/) transitions from each state when an M-ary constellation is used. This MAP equalizer achieves the N/sub r//spl times/(L+1) diversity benefit while realizing N/sub t//spl times/log/sub 2/(M) bits/sec/Hz. We then propose a novel iterative per-antenna MAP(PAMAP) approach which can be used (1) to reduce the complexity and (2) to achieve the full diversity order N/sub t//spl times/N/sub r//spl times/(L+1) at the rate of log/sub 2/(M) bits/sec/Hz. The proposed equalizer consists of a probabilistic "signal separator" and a bank of N/sub t/ PAMAPs each having M/sup L/ states with M transitions from each state. The signal separator and the PAMAPs exchange extrinsic information during iterations. Simulation results indicate that the proposed receiver closely achieves the performance of the full complexity MAP within 2 to 3 iterations. The proposed scheme saves a significant amount of complexity in uncoded systems with a large number of transmit antennas and a high modulation order. In coded systems, the PAMAP scheme becomes more beneficial when iterative equalization and decoding is used.

## Stability analysis of non-recursive parallel concatenated real number codes

- **Status**: ❌
- **Reason**: 실수(real number) 병렬연접 부호 안정성 분석, 초록 없음; 바이너리 LDPC ECC와 무관한 이론 — 제외
- **ID**: ieee:1231139
- **Type**: conference
- **Published**: 2002
- **Authors**: J. Vieira
- **PDF**: https://ieeexplore.ieee.org/document/1231139
- **Abstract**: N/A

## Parallel decoding of interleaved single parity check turbo product codes

- **Status**: ❌
- **Reason**: SPC turbo product code의 Max-Log-MAP 디코더; 비-LDPC 부호이고 디코더 기법이 바이너리 LDPC BP로 이식되는 기여 아님
- **ID**: ieee:1049680
- **Type**: conference
- **Published**: 2002
- **Authors**: Yanni Chen, K. K. Parhi
- **PDF**: https://ieeexplore.ieee.org/document/1049680
- **Abstract**: In this paper, both complexity and performance aspects of serially concatenated 2-D single parity check turbo product codes are investigated. The extremely simple Max-Log-MAP decoding is alternatively derived with only three additions needed to compute each bit's extrinsic information. Parallel decoding structure is proposed to increase the decoding throughput while a new helical interleaver is constructed to further improve the coding gain. For performance evaluation, (16, 14, 2)/sup 2/ single parity check turbo product codes with code rate 0.766 over an AWGN channel using QPSK are considered. The simulation results using Max-Log-MAP decoding show that it can achieve BER of 10/sup -5/ at SNR of 3.8 dB with 8 iterations. Compared to the same rate and codeword length turbo product code composed of extended Hamming codes, the considered scheme can achieve similar performance with much less complexity. Other implementation issues such as the finite precision analysis and efficient sorting circuit design are also presented.

## An analog turbo decoder for an (8,4) product code

- **Status**: ❌
- **Reason**: 아날로그 turbo/product code 디코더(Gilbert multiplier 회로)—아날로그 구현은 디지털 NAND 컨트롤러 ECC HW 이식성 약해 제외
- **ID**: ieee:1187119
- **Type**: conference
- **Published**: 2002
- **Authors**: N. Correal, J. Heck, M. Valenti
- **PDF**: https://ieeexplore.ieee.org/document/1187119
- **Abstract**: This paper illustrates how analog circuitry can be used to decode turbo and turbo-like codes. For ease of exposition, the focus is on a simple two dimensional product code comprised of a 2 by 2 array of (3,2) single parity check codes. It is shown that the heart of the decoder is a soft exclusive-or operation which is easily implemented in analog as a modified Gilbert multiplier. Finally, a complete decoder design is presented which is capable of achieving throughput on the order of hundreds of Mbps.

## Combined source-channel coding for a power and bandwidth constrained noisy channel with application to progressive image transmission

- **Status**: ❌
- **Reason**: 결합 소스-채널 코딩(점진적 이미지 전송, UEP coded modulation) — LDPC 아님, JSCC 제외
- **ID**: ieee:1197190
- **Type**: conference
- **Published**: 2002
- **Authors**: N. S. Raja, Zixiang Xiong, M. Fossorier
- **PDF**: https://ieeexplore.ieee.org/document/1197190
- **Abstract**: In this paper, combined source-channel coding for a power and bandwidth constrained channel is studied, with application to progressive image transmission. For a given power constrained and bandwidth constrained Gaussian communication channel, we consider the optimum coded modulation scheme among a predetermined set of signaling constellations when the performance is measured by end-to-end average distortion. This scheme particularly fits progressive source coding in conjunction with unequal error protection.

## t-error correcting/d-error detecting (d>t) and all unidirectional error detecting codes with neural network. II

- **Status**: ❌
- **Reason**: t-EC/d-ED/AUED 부호의 신경망 구성/검출 — 비-LDPC 단방향 오류검출 부호, LDPC BP 이식 기법 없음
- **ID**: ieee:1000420
- **Type**: conference
- **Published**: 2002
- **Authors**: Maung Maung Htay, S. S. Iyengar, Si Qing Zheng
- **PDF**: https://ieeexplore.ieee.org/document/1000420
- **Abstract**: For pt.I. see ITCC, IEEE proceeding, p. 529-36 (April 2001). In this paper, we develop an algorithm for t-error correcting/d-error detecting and all unidirectional error detecting (t-EC/d-ED/AUED) codes in the framework of neural work. As t-EC/d-ED/AUED codewords are formed by concatenation of information bits and one or more groups of check bits depending on how we want to construct code, we demonstrate neural network algorithms for constructing, detecting and correcting codes. As a continuation of the previous paper, we present an algorithm, code construction, detecting and correcting for 2EC/5ED/AUED code II. We also plan to present for other codes with more examples in near future as well.

## Generalized irregular low-density (Tanner) codes based on Hamming component codes

- **Status**: ❌
- **Reason**: Hamming 성분부호 기반 GLDPC, 성분부호 전용 SISO 디코딩 의존(일반화 LDPC 제외)
- **ID**: ieee:1146832
- **Type**: conference
- **Published**: 2002
- **Authors**: T. M. Ngatched, F. Takawira
- **PDF**: https://ieeexplore.ieee.org/document/1146832
- **Abstract**: In this paper we introduce the construction of new families of error-correcting codes based on Irregular low-density parity-check codes, which we called generalized irregular low density (GILD) codes, where as component codes, single-error correcting Hamming codes are used instead of single-error detecting parity-check codes. The decoding of GILD Is based on simple and fast SISO (soft input-soft output) decoding of Hamming component codes. Simulation results over an AWGN channel indicate that excellent performances can be achieved.

## Design of serially concatenated coded CDMA system

- **Status**: ❌
- **Reason**: CDMA 직렬연접 FEC + 다중사용자검출 시스템 설계, LDPC 무관·통신 응용 특이적, 떼어낼 ECC 기법 없음
- **ID**: ieee:997178
- **Type**: conference
- **Published**: 2002
- **Authors**: Zhenning Shi, C. Schlegel
- **PDF**: https://ieeexplore.ieee.org/document/997178
- **Abstract**: A code-division multiple-access (CDMA) system in conjunction with serial concatenation of FEC codes is considered. Iterative decoding strategies are used at the receiver. The component decoders are functionally described by variance transfer (VTR) charts. Pinch-off SNRs, where the iterative decoding starts to function, are precisely predicted by this approach. Designs of the multiuser detection (MUD) method and the component FEC codes have been carried out and system performance to within about 1 dB of the Shannon capacity of the multiple-access channel is demonstrated.

## Iterative equalization/decoding of LDPC code transmitted over MIMO fading ISI channels

- **Status**: ❌
- **Reason**: MIMO ISI 무선 응용, LDPC는 표준이고 기여는 채널특이적 reduced-complexity MAP 등화기
- **ID**: ieee:1045245
- **Type**: conference
- **Published**: 2002
- **Authors**: Heung-no Lee, V. Gulati
- **PDF**: https://ieeexplore.ieee.org/document/1045245
- **Abstract**: We propose a spectrum efficient and robust space-time-frequency code system for a (N/sub t/, N/sub r/) MIMO, (L+1)-tap, fading channel. The LDPC (low-density parity-check) code is employed at the transmitter and iterative maximum a posteriori (MAP) equalizers are used at the receiver. We propose a novel, reduced-complexity iterative decoding and equalization scheme in which we combine the message-passing decoder, on the bipartite graph for the LDPC code, with an iterative MAP equalizer in a turbo-like manner. First, we consider a full-complexity vector MAP equalizer which runs the forward/backward algorithm on the trellis which has M/sup Nt/spl times/L/ states with M/sup Nt/ transitions from each state when an M-ary constellation is used. Second, we replace the full MAP with the bank of N/sub t/ per-antenna MAP (PAMAP) equalizers - each works on an M/sup L/ state trellis - and evaluate the performance loss due to the use of the reduced complexity scheme. The simulation results show that the performance of the PAMAP-bipartite equalization/decoding scheme is very close to the full complexity vector MAP-bipartite. In addition, in the fast fading case, the performance of the proposed space-time-frequeney system with N/sub t/ = 2, N/sub r/ = 2 and L = 2 is very close, within 0.5 dB, to the results of the LDPC code on AWGN channels.

## Cycle-slip-detector-aided iterative timing recovery algorithm

- **Status**: ❌
- **Reason**: LDPC 사용하는 채널의 cycle-slip 타이밍복구 알고리즘 — ECC 디코더 자체가 아닌 동기화 기법, 떼어낼 LDPC BP/HW 기여 없음
- **ID**: ieee:1000863
- **Type**: conference
- **Published**: 2002
- **Authors**: Xiaowei Jin, A. Kavcic
- **PDF**: https://ieeexplore.ieee.org/document/1000863
- **Abstract**: Summary form only given. Recent research on capacity approaching codes, i.e., low density parity check (LDPC) codes and turbo codes, assumes perfect timing recovery systems. Conventional timing recovery devices tend to experience cycle-slips at low signal-to-noise ratios (SNRs). In our previous work, we developed a cycle-slip detector (CSD) for AWGN channels using the decoder soft information. In this paper, we generalize the method and develop the CSD for channels with intersymbol interference. We investigate the PR4 (1-D/sup 2/) channel with a rate 4/5 LDPC code. The channel experiences a slowly time-varying phase drift. We use the Mueller and Muller (M&M) synchronizer to track the phase drift. For i.i.d. equally likely binary symbols, the soft information is the symbol a posteriori probability (APP). Both the symbol APPs and the preliminary decisions for the timing recovery algorithm are provided by a forward-only implementation of the BCJR algorithm, with a survival memory length of 6. This paper further investigates an iterative timing recovery scheme with the aid of the CSD.

## Space-time low-density parity-check codes

- **Status**: ❌
- **Reason**: MIMO space-time LDPC, 무선 특이적 그래프 구성으로 떼어낼 일반 LDPC 코드설계/디코더 기여 약함
- **ID**: ieee:1196957
- **Type**: conference
- **Published**: 2002
- **Authors**: P. Meshkat, H. Jafarkhani
- **PDF**: https://ieeexplore.ieee.org/document/1196957
- **Abstract**: We use a graph based representation to develop space-time low density parity check (LDPC) codes. Shortly after the advent of turbo codes in 1993, several researchers noticed that existing graphical representations such as Bayesian Networks and later-developed representations like factor graphs are excellent unifying frameworks for developing iterative algorithms such as (joint) decoding and equalization. This work is one such example where we use the framework of Bayesian networks to develop LDPC codes for a multiple transmit/multiple receive antenna scenario. The performance of these codes and corresponding iterative decoding algorithm is explored.

## Low density parity check codes in a frequency hopped communication system with partial-band interference

- **Status**: ❌
- **Reason**: 주파수도약 부분대역 재밍 통신 응용, 기존 불규칙 LDPC 성능평가일 뿐 신규 디코더·구성·HW 없음
- **ID**: ieee:1179593
- **Type**: conference
- **Published**: 2002
- **Authors**: S. H. Schremmer
- **PDF**: https://ieeexplore.ieee.org/document/1179593
- **Abstract**: In this paper the applicability of low density parity check (LDPC) codes to a frequency hopped communications system with partial-band jamming is investigated. We show an irregular LDPC code which exhibits good waterfall and error floor performance with a block length of 1560 bits using binary phase-shift keying. The performance of this code is investigated in a partial band jammed environment with various channel interleaver lengths. We show that with a channel interleaver consisting of 120 hops and available side information, a partial band jammer only causes a loss of 0.3 dB over the full band case at a bit error rate of 10/sup -5/.

## Performance comparison of layered space time codes

- **Status**: ❌
- **Reason**: 층화 시공간 코드/MIMO 무선 응용, LDPC는 비교 성분코드로 언급될 뿐 떼어낼 ECC 기법 없음
- **ID**: ieee:997077
- **Type**: conference
- **Published**: 2002
- **Authors**: Ka Leong Lo, S. Marinkovic, Zhuo Chen +1
- **PDF**: https://ieeexplore.ieee.org/document/997077
- **Abstract**: Multiple antenna systems have the potential to provide a high capacity wireless communication system. The spectral efficiency of space time trellis coding (STTC) is limited by the encoder structure. The layered space time (LST) architecture can overcome this problem. Three different LST schemes are presented. An improved iterative parallel interference canceller (PIC) method is applied at the receiver. A significant performance improvement is achieved compared to the standard PIC. Simulation results of three various layer structures are compared with low density parity check (LDPC) and convolutional codes as component codes.

## Low density parity check codes over groups and rings

- **Status**: ❌
- **Reason**: 환/군(ring/group) 위 LDPC = 비이진 구조 부호, 바이너리 LDPC 아님
- **ID**: ieee:1115443
- **Type**: conference
- **Published**: 2002
- **Authors**: D. Sridhara, T. E. Fuja
- **PDF**: https://ieeexplore.ieee.org/document/1115443
- **Abstract**: The role of low density parity check principles in the design of group codes for coded modulation is examined. In this context, the structure of linear codes over certain rings /spl Zopf//sub m/ and G/sub m/ is discussed, and LDPC codes over these ring structures are designed.

## Analysis of joint iterative decoding and phase estimation for the noncoherent AWGN channel, using density evolution

- **Status**: ❌
- **Reason**: LDPC를 쓰나 noncoherent AWGN 위상추정 결합 디코딩이라는 무선응용 특이적, 떼어낼 일반 LDPC 디코더/구성 기법 없음
- **ID**: ieee:1023440
- **Type**: conference
- **Published**: 2002
- **Authors**: R. Nuriyev, A. Anastasopoulos
- **PDF**: https://ieeexplore.ieee.org/document/1023440
- **Abstract**: Coding for the additive white Gaussian noise (AWGN) channel that also introduces an unknown carrier phase rotation is considered in this work. A simple model that captures the phase dynamics is one, where the unknown carrier phase is considered constant over a block of N symbols, and independent from block to block. In this work, LDPC codes in conjunction with pilot symbols are considered. In particular, a single pilot symbol of specified power is inserted in the beginning of each block of length N, in order to aid the joint estimation and decoding process. As expected, the presence of a pilot symbol implies an inevitable loss in the transmitted power, resulting in a trade-off between the power allocated between the pilots and the coded bits, and the quality of the joint estimation and decoding process.

## Performance of clustered OFDM with low density parity check codes over dispersive channels

- **Status**: ❌
- **Reason**: OFDM/채널추정 무선 응용, LDPC는 부수 적용이고 이식할 ECC 기법 없음
- **ID**: ieee:1197095
- **Type**: conference
- **Published**: 2002
- **Authors**: Huaning Niu, Manyuan Shen, J. A. Ritcey +1
- **PDF**: https://ieeexplore.ieee.org/document/1197095
- **Abstract**: We present a new low density parity check (LCPC) coded clustered orthogonal frequency division multiplexing (OFDM) system with 16QAM modulation operating over a frequency selective fast fading channel. Various channel estimation methods are studied and pilot-symbol-aided channel estimation with uniquely designed spacing pattern is used to obtain channel side information in fast fading. A BER of 10/sup -6/ is achieved at 12.8dB with Doppler frequency f/sub m/ = 200 Hz and 14.8 dB with f/sub m/ = 100 Hz. The overall capacity of this system is about 1.56 bit/s/Hz. Compared with other wideband systems, our design has much better performance in fading channels than the LDPC coded classical OFDM and is much simpler than TTCM-OFDM system.

## A new high performance turbo encoder scheme for bandwidth efficient modulation

- **Status**: ❌
- **Reason**: turbo coded modulation의 비균등 신호성형(shaping) 기법, LDPC는 부수 언급, 채널 ECC 기여 없음
- **ID**: ieee:1178445
- **Type**: conference
- **Published**: 2002
- **Authors**: D. Raphaeli, A. Gurevitz
- **PDF**: https://ieeexplore.ieee.org/document/1178445
- **Abstract**: In this paper we combine nonuniform signaling with the pragmatic binary turbo coded modulation environment. Our shaping method follows the technique proposed by Gallager (1968). This technique can be easily applied to any binary turbo or turbo-like code, including parallel, serial and low density parity check (LDPC) codes. The nonequiprobable letters are obtained by using a table that maps b-bits equiprobable input words onto nonequiprobable m-bits M-ary PAM (or equivalently M/sup 2/ QAM) symbols, at rates 2 and 3 bits/dim.

## Soft signal space detection for magnetic recording

- **Status**: ❌
- **Reason**: soft signal space detector(채널 검출기) 제안, LDPC는 soft 입력 받는 부수 언급; 떼어낼 LDPC 디코더/구성 기법 없음
- **ID**: ieee:1001129
- **Type**: conference
- **Published**: 2002
- **Authors**: B. Steingrimsson
- **PDF**: https://ieeexplore.ieee.org/document/1001129
- **Abstract**: Summary form only given. Soft signal space detectors approximate the symbol-by-symbol maximum a posteriori probability detection algorithms whose optimization criterion is the symbol error probability. The soft signal space detectors (SSDs) yield probabilistic reliability information about the transmitted symbols in contrast to yielding hard decisions about these symbols, as the hard SSD detectors do. The soft information can be used as input to soft error correction codes (ECCs), such as turbo codes or low density parity check (LDPC) codes, resulting in large performance gains over hard channel decoders and hard ECCs.

## Performance of clustered OFDM with low density parity check codes over dispersive channels

- **Status**: ❌
- **Reason**: LDPC를 OFDM 무선 채널에 부수 적용; 떼어낼 디코더/HW/코드설계 신규 기여 없음 — 무선 응용 특이적 제외
- **ID**: ieee:1197168
- **Type**: conference
- **Published**: 2002
- **Authors**: Huaning Niu, Manyuan Shen, J. A. Ritcey +1
- **PDF**: https://ieeexplore.ieee.org/document/1197168
- **Abstract**: A new LDPC coded clustered OFDM system with 16QAM modulation operating over a frequency selective fast fading channel is presented. Various channel estimation methods are studied and pilot-symbol-aided channel estimation with uniquely designed spacing pattern is used to obtain channel side information for fast fading. A BER of 10/sup -6/ is achieved at 12.8 dB with Doppler frequency f/sub m/ = 200 Hz and 14.8 dB with f/sub m/ = 100 Hz. The overall capacity of this system is about 1.56 bit/s/Hz. Compared with other wideband systems, it has much better performance in fading channels than the LPDC coded classical OFDM and is much simpler than TTCM-OFDM system.

## Symbol timing recovery for low-SNR partial response recording channels

- **Status**: ❌
- **Reason**: 기록채널 심볼 타이밍 복구 기법, LDPC는 시뮬레이션 베이스라인일 뿐 이식할 LDPC 기법 없음
- **ID**: ieee:1188372
- **Type**: conference
- **Published**: 2002
- **Authors**: Jingfeng Liu, Hongwei Song, B. V. K. V. Kumar
- **PDF**: https://ieeexplore.ieee.org/document/1188372
- **Abstract**: Future very high density data storage systems will exhibit significantly more intersymbol interference (ISI) and significantly lower signal-to-noise ratio (SNR). Advanced signal detection algorithms, such as noise predictive maximum likelihood (NPML) and iterative soft decoding, are aimed at coping with such lower SNRs and higher ISI. However, at such low SNRs, because of their large residual timing jitter, current timing recovery schemes suffer frequently from loss of lock (the event where the estimated phase drift differs significantly from the actual phase drift for a significantly long duration leading to misindexing of the detected bits and thus error bursts) potentially offsetting the SNR gains provided by advanced detection methods. The main contribution of this paper is that by approximating the phase drifts present in recording systems as a piecewise linear phase drift model, we propose a novel timing recovery scheme, which is named frequency offset feedforward symbol timing recovery (FOSTR). For such a piecewise linear phase drift model, the problem of estimating the time-changing phase drift can be transformed to the problem of estimating the slopes (i.e., frequency offsets) and initial phase offsets of several linear ramps. The performance of the timing recovery based on this approach will be better than current methods in low SNR because the number of parameters to be estimated is significantly smaller. Bit-by-bit simulations with iterative soft decoding (low density parity check (LDPC) code of rate 16/17 and codeword size 4352 bits is used) show that FOSTR results in a significantly smaller residual timing jitter than that of the conventional decision-directed PLL-based feedback timing recovery schemes, although the adjusted ("adjusted" means the sectors suffering from loss of lock are not taken into account in bit error rate calculation) bit error rate (BER) performance of FOSTR is only about 0.6 dB better for a target adjusted BER of 1/spl times/10/sup -5/ than that of the conventional timing recovery scheme because iterative soft decoding is robust to residual timing jitter. However, the loss of lock rate (i.e., the fraction of sectors suffering from loss of lock) is significantly reduced by FOSTR.

## Compression of binary sources with side information at the decoder using LDPC codes

- **Status**: ❌
- **Reason**: Slepian-Wolf 소스압축(side info) 응용, 채널 ECC 아님(소스 코딩 제외)
- **ID**: ieee:1042242
- **Type**: journal
- **Published**: 2002
- **Authors**: A. D. Liveris, Zixiang Xiong, C. N. Georghiades
- **PDF**: https://ieeexplore.ieee.org/document/1042242
- **Abstract**: We show how low-density parity-check (LDPC) codes can be used to compress close to the Slepian-Wolf limit for correlated binary sources. Focusing on the asymmetric case of compression of an equiprobable memoryless binary source with side information at the decoder, the approach is based on viewing the correlation as a channel and applying the syndrome concept. The encoding and decoding procedures are explained in detail. The performance achieved is seen to be better than recently published results using turbo codes and very close to the Slepian-Wolf limit.

## LDPC-based space-time coded OFDM systems over correlated fading channels: Performance analysis and receiver design

- **Status**: ❌
- **Reason**: LDPC 기반 STC-OFDM 무선 수신기; LDPC를 베이스라인으로 쓴 무선 응용, 떼어낼 ECC 기법 없음
- **ID**: ieee:975756
- **Type**: journal
- **Published**: 2002
- **Authors**: B. Lu, Xiaodong Wang, K. R. Narayanan
- **PDF**: https://ieeexplore.ieee.org/document/975756
- **Abstract**: We consider a space-time coded (STC) orthogonal frequency-division multiplexing (OFDM) system with multiple transmitter and receiver antennas over correlated frequency- and time-selective fading channels. It is shown that the product of the time-selectivity order and the frequency-selectivity order is a key parameter to characterize the outage capacity of the correlated fading channel. It is also observed that STCs with large effective lengths and ideal built-in interleavers are more effective in exploiting the natural diversity in multiple-antenna correlated fading channels. We then propose a low-density parity-check (LDPC)-code-based STC-OFDM system. Compared with the conventional space-time trellis code (STTC), the LDPC-based STC can significantly improve the system performance by exploiting both the spatial diversity and the selective-fading diversity in wireless channels. Compared with the previously proposed turbo-code-based STC scheme, LDPC-based STC exhibits lower receiver complexity and more flexible scalability. We also consider receiver design for LDPC-based STC-OFDM systems in unknown fast fading channels and propose a novel turbo receiver employing a maximum a posteriori expectation-maximization (MAP-EM) demodulator and a soft LDPC decoder, which can significantly reduce the error floor in fast fading channels with a modest computational complexity. With such a turbo receiver, the proposed LDPC-based STC-OFDM system is a promising solution to highly efficient data transmission over selective-fading mobile wireless channels.

## On the performance of high-rate TPC/SPC codes and LDPC codes over partial response channels

- **Status**: ❌
- **Reason**: TPC/SPC(turbo product/SPC) 부호를 LDPC와 비교; 기여는 비-LDPC TPC/SPC 측이고 부호 비의존 이식 BP 기법 없음(magnetic recording 응용)
- **ID**: ieee:1006554
- **Type**: journal
- **Published**: 2002
- **Authors**: Jing Li, K. R. Narayanan, E. Kurtas +1
- **PDF**: https://ieeexplore.ieee.org/document/1006554
- **Abstract**: This paper evaluates two-dimensional turbo product codes based on single-parity check codes (TPC/SPC) and low-density parity check (LDPC) codes for use in digital magnetic recording systems. It is first shown that the combination of a TPC/SPC code and a precoded partial response (PR) channel results in a good distance spectrum due to the interleaving gain. Then, density evolution is used to compute the thresholds for TPC/SPC codes and LDPC codes over PR channels. Analysis shows that TPC/SPC codes have a performance close to that of LDPC codes for large codeword lengths. Simulation results for practical block lengths show that TPC/SPC codes perform as well as LDPC codes in terms of bit error rate, but possess better burst error statistics which is important in the presence of an outer Reed-Solomon code. Further, the encoding complexity of TPC/SPC codes is only linear in the codeword length and the generator matrix does not have to be stored explicitly. Based on. the results in the paper and these advantages, TPC/SPC codes seem like a viable alternative to LDPC codes.

## Upper bounds on the rate of LDPC codes

- **Status**: ❌
- **Reason**: 순수 이론 bound (LDPC rate 상한) — 디코더/HW/구성으로 안 이어지는 순수 이론, 제외 항목.
- **ID**: ieee:1027775
- **Type**: journal
- **Published**: 2002
- **Authors**: D. Burshtein, M. Krivelevich, S. Litsyn +1
- **PDF**: https://ieeexplore.ieee.org/document/1027775
- **Abstract**: We derive upper bounds on the rate of low-density parity-check (LDPC) codes for which reliable communication is achievable. We first generalize Gallager's (1963) bound to a general binary-input symmetric-output channel. We then proceed to derive tighter bounds. We also derive upper bounds on the rate as a function of the minimum distance of the code. We consider both individual codes and ensembles of codes.

## Bounds on the performance of belief propagation decoding

- **Status**: ❌
- **Reason**: BP 디코딩 성능의 상한/하한 순수 이론 bound; 디코더/HW/구성으로 이어지지 않음
- **ID**: ieee:971742
- **Type**: journal
- **Published**: 2002
- **Authors**: D. Burshtein, G. Miller
- **PDF**: https://ieeexplore.ieee.org/document/971742
- **Abstract**: We consider Gallager's (1963) soft-decoding (belief propagation) algorithm for decoding low-density parity-check (LDPC) codes, when applied to an arbitrary binary-input symmetric-output channel. By considering the expected values of the messages, we derive both lower and upper bounds on the performance of the algorithm. We also derive various properties of the decoding algorithm, such as a certain robustness to the details of the channel noise. Our results apply both to regular and irregular LDPC codes.

## On ensembles of low-density parity-check codes: asymptotic distance distributions

- **Status**: ❌
- **Reason**: 정규 LDPC 앙상블의 점근 거리분포 순수 이론 분석 — 디코더/HW/구성 신규 기여 없음
- **ID**: ieee:992777
- **Type**: journal
- **Published**: 2002
- **Authors**: S. Litsyn, V. Shevelev
- **PDF**: https://ieeexplore.ieee.org/document/992777
- **Abstract**: We derive expressions for the average distance distributions in several ensembles of regular low-density parity-check codes (LDPC). Among these ensembles are the standard one defined by matrices having given column and row sums, ensembles defined by matrices with given column sums or given row sums, and an ensemble defined by bipartite graphs.

## Nested linear/lattice codes for structured multiterminal binning

- **Status**: ❌
- **Reason**: 네트워크 정보이론의 nested linear/lattice binning 기법; 채널 ECC 디코더/HW 아님, 떼어낼 바이너리 LDPC BP 기법 없음
- **ID**: ieee:1003821
- **Type**: journal
- **Published**: 2002
- **Authors**: R. Zamir, S. Shamai, U. Erez
- **PDF**: https://ieeexplore.ieee.org/document/1003821
- **Abstract**: Network information theory promises high gains over simple point-to-point communication techniques, at the cost of higher complexity. However, lack of structured coding schemes limited the practical application of these concepts so far. One of the basic elements of a network code is the binning scheme. Wyner (1974, 1978) and other researchers proposed various forms of coset codes for efficient binning, yet these schemes were applicable only for lossless source (or noiseless channel) network coding. To extend the algebraic binning approach to lossy source (or noisy channel) network coding, previous work proposed the idea of nested codes, or more specifically, nested parity-check codes for the binary case and nested lattices in the continuous case. These ideas connect network information theory with the rich areas of linear codes and lattice codes, and have strong potential for practical applications. We review these developments and explore their tight relation to concepts such as combined shaping and precoding, coding for memories with defects, and digital watermarking. We also propose a few novel applications adhering to a unified approach.

## Iterative multiuser joint decoding: unified framework and asymptotic analysis

- **Status**: ❌
- **Reason**: CDMA 다중사용자 합동복호 — sum-product/factor-graph 사용하나 무선 멀티유저 응용 특이적, NAND LDPC ECC로 떼어낼 디코더 기법 없음
- **ID**: ieee:1013125
- **Type**: journal
- **Published**: 2002
- **Authors**: J. Boutros, G. Caire
- **PDF**: https://ieeexplore.ieee.org/document/1013125
- **Abstract**: We present a framework for iterative multiuser joint decoding of code-division multiple-access (CDMA) signals, based on the factor-graph representation and on the sum-product algorithm. In this framework, known parallel and serial, hard and soft interference cancellation algorithms are derived in a unified way. The asymptotic performance of these algorithms in the limit of large code block length can be rigorously analyzed by using density evolution. We show that, for random spreading in the large-system limit, density evolution is considerably simplified. Moreover, by making a Gaussian approximation of the decoder soft output, we show that the behavior of iterative multiuser joint decoding is approximately characterized by the stable fixed points of a simple one-dimensional nonlinear dynamical system.

## Capacity-achieving sequences for the erasure channel

- **Status**: ❌
- **Reason**: erasure channel용 capacity-achieving degree distribution 이론; NAND 채널 ECC로 떼어낼 디코더/HW/구성 기여 없는 순수 이론
- **ID**: ieee:1077796
- **Type**: journal
- **Published**: 2002
- **Authors**: P. Oswald, A. Shokrollahi
- **PDF**: https://ieeexplore.ieee.org/document/1077796
- **Abstract**: This paper starts a systematic study of capacity-achieving (c.a.) sequences of low-density parity-check codes for the erasure channel. We introduce a class A of analytic functions and develop a procedure to obtain degree distributions for the codes. We show various properties of this class which help us to construct new distributions from old ones. We then study certain types of capacity-achieving sequences and introduce new measures for their optimality. For instance, it turns out that the right-regular sequence is c.a. in a much stronger sense than, e.g., the Tornado sequence. This also explains why numerical optimization techniques tend to favor graphs with only one degree of check nodes.

## Variations on the Gallager bounds, connections, and applications

- **Status**: ❌
- **Reason**: ML 디코딩 오류확률 Gallager bound 변형 — 순수 이론 bound, 디코더/HW/구성으로 안 이어짐
- **ID**: ieee:1077797
- **Type**: journal
- **Published**: 2002
- **Authors**: S. Shamai, I. Sason
- **PDF**: https://ieeexplore.ieee.org/document/1077797
- **Abstract**: There has been renewed interest in deriving tight bounds on the error performance of specific codes and ensembles, based on their distance spectrum. We discuss many reported upper bounds on the maximum-likelihood (ML) decoding error probability and demonstrate the underlying connections that exist between them. In addressing the Gallager bounds and their variations, we focus on the Duman and Salehi (see IEEE Trans. Commun., vol.46, p.717-723, 1998)variation, which originates from the standard Gallager bound. A large class of efficient bounds (or their Chernoff versions) is demonstrated to be a special case of the generalized second version of the Duman and Salehi bounds. Implications and applications of these observations are pointed out, including the fully interleaved fading channel, resorting to either matched or mismatched decoding. The proposed approach can be generalized to geometrically uniform nonbinary codes, finite-state channels, bit interleaved coded modulation systems, and it can be also used for the derivation of upper bounds on the conditional decoding error probability.

## Equalization and FEC techniques for optical transceivers

- **Status**: ❌
- **Reason**: 광 트랜시버 DSP/FEC 튜토리얼(서베이성); 구체적 신규 LDPC 디코더/구성 기여 없음
- **ID**: ieee:987083
- **Type**: journal
- **Published**: 2002
- **Authors**: K. Azadet, E. F. Haratsch, H. Kim +5
- **PDF**: https://ieeexplore.ieee.org/document/987083
- **Abstract**: In this tutorial paper, we present the application of well-known DSP techniques used in lower speed wireline and wireless applications, to high-speed optical communications. After an introduction on today's optical network architecture and typical optical channel impairments, we study techniques such as fiber equalization, maximum likelihood detection, and current and next generations Forward Error Correction (FEC), with special emphasis on VLSI implementation.

## Coding theorems for turbo code ensembles

- **Status**: ❌
- **Reason**: turbo code 앙상블의 순수 ML coding theorem(이론 bound); 비-LDPC, 떼어낼 디코더/HW 없음
- **ID**: ieee:1003833
- **Type**: journal
- **Published**: 2002
- **Authors**: Hui Jin, R. J. McEliece
- **PDF**: https://ieeexplore.ieee.org/document/1003833
- **Abstract**: This paper is devoted to a Shannon-theoretic study of turbo codes. We prove that ensembles of parallel and serial turbo codes are "good" in the following sense. For a turbo code ensemble defined by a fixed set of component codes (subject only to mild necessary restrictions), there exists a positive number /spl gamma//sub 0/ such that for any binary-input memoryless channel whose Bhattacharyya noise parameter is less than /spl gamma//sub 0/, the average maximum-likelihood (ML) decoder block error probability approaches zero, at least as fast as n/sup -/spl beta//, where /spl beta/ is the "interleaver gain" exponent defined by Benedetto et al. in 1996.

## Power control and beamforming for systems with multiple transmit and receive antennas

- **Status**: ❌
- **Reason**: MIMO 전력제어/빔포밍, LDPC 부수언급, 떼어낼 ECC 기법 없음
- **ID**: ieee:1045295
- **Type**: journal
- **Published**: 2002
- **Authors**: R. Knopp, G. Caire
- **PDF**: https://ieeexplore.ieee.org/document/1045295
- **Abstract**: This paper investigates the performance of narrowband, slowly fading, and delay-limited multiple-antenna systems where channel state information (CSI) is available at the transmission end. This situation can arise in time-division duplex (TDD) based two-way systems where channel state estimation can be performed using the signal received from the opposite link. Power control methods which attempt to keep the transmission rate constant at the expense of randomizing the transmit power are considered. It is shown that significant savings in average transmit power (sometimes on the order of tens of decibels) can be expected compared to systems which keep the total transmit power constant. Several practical channel coding examples using are illustrated and their bit and frame error rate performance are discussed.

## Perpendicular and longitudinal recording: a signal-processing and coding perspective

- **Status**: ❌
- **Reason**: 자기기록 채널의 등화·검출·RS/LDPC 외부부호 비교 — LDPC가 부수적, 신규 디코더·구성·HW 기여 없음
- **ID**: ieee:1017759
- **Type**: journal
- **Published**: 2002
- **Authors**: R. D. Cideciyan, E. Eleftheriou, T. Mittelholzer
- **PDF**: https://ieeexplore.ieee.org/document/1017759
- **Abstract**: Equalization and noise prediction followed by sequence detection and postprocessing are studied for double-layer perpendicular recording channels that are corrupted by electronics and transition noise. The performance of various outer coding schemes, such as conventional Reed-Solomon codes with 8and 10-bit symbols and low-density parity check codes, is evaluated, and a signal-processing and coding perspective is presented for both longitudinal and perpendicular recording channels. Finally, the capacity of recording channels is characterized.

## Iterative Viterbi decoding, trellis shaping, and multilevel structure for high-rate parity-concatenated TCM

- **Status**: ❌
- **Reason**: parity-concatenated TCM의 iterative Viterbi+trellis shaping; 비-LDPC, BP 이식 기여 없음
- **ID**: ieee:975743
- **Type**: journal
- **Published**: 2002
- **Authors**: Qi Wang, Lei Wei, R. A. Kennedy
- **PDF**: https://ieeexplore.ieee.org/document/975743
- **Abstract**: We define and apply a new algorithm called the iterative Viterbi decoding algorithm (IVA) to decode a high-rate parity-concatenated TCM system in which a trellis code is used as the inner code and a simple parity-check code is used as the outer code. With trellis shaping, the IVA can achieve a performance 1.25 dB away from the Shannon limit at a BER of 3/spl times/10/sup -5/ with low complexity. By augmenting the system with a binary BCH code, the error floor can be reduced to 10/sup -9/ with very little additional cost.

## Application of efficient Chase algorithm in decoding of generalized low-density parity-check codes

- **Status**: ❌
- **Reason**: GLD 코드 + Chase 알고리즘 — constraint 노드가 확장 Hamming 대수부호 전용 디코딩(Chase)에 의존, GLDPC 제외 항목.
- **ID**: ieee:1033200
- **Type**: journal
- **Published**: 2002
- **Authors**: S. Hirst, B. Honary
- **PDF**: https://ieeexplore.ieee.org/document/1033200
- **Abstract**: We consider the iterative decoding of generalized low-density (GLD) parity-check codes where, rather than employ an optimal subcode decoder, a Chase (1972) algorithm decoder more commonly associated with "turbo product codes" is used. GLD codes are low-density graph codes in which the constraint nodes are other than single parity-checks. For extended Hamming-based GLD codes, we use bit error rates derived by simulation to demonstrate this new strategy to be successful at higher code rates. For long block lengths, good performance close to capacity is possible with decoding costs reduced further since the Chase decoder employed is an efficient implementation.

## Retry mode soft Reed-Solomon decoding

- **Status**: ❌
- **Reason**: 비-LDPC(Reed-Solomon) 소프트 디코딩(Koetter-Vardy), 부호 비의존적이지 않아 바이너리 LDPC BP로 이식 불가
- **ID**: ieee:1042176
- **Type**: journal
- **Published**: 2002
- **Authors**: Haitao Xia, Hongxin Song, J. R. Cruz
- **PDF**: https://ieeexplore.ieee.org/document/1042176
- **Abstract**: We present a new retry mode scheme for magnetic recording systems based on a soft-decision Reed-Solomon decoding algorithm recently proposed by Koetter and Vardy and evaluate its performance. Instead of using asymptotic bounds, we present realistic simulation results over partial response channels, which show improved performance with a small increase in hardware complexity.

## Programmable interleaver design for analog iterative decoders

- **Status**: ❌
- **Reason**: 아날로그 반복디코더용 인터리버 HW, 아날로그/혼합신호 디코더 제외 항목 해당
- **ID**: ieee:1046045
- **Type**: journal
- **Published**: 2002
- **Authors**: V. C. Gaudet, R. J. Gaudet, P. G. Gulak
- **PDF**: https://ieeexplore.ieee.org/document/1046045
- **Abstract**: Several programmable analog interleaver architectures for iterative decoders are proposed. The architectures are evaluated in terms of transistor count, path resistance, path capacitance, and programming logic. Interleavers built out of networks consisting of three layers of small crossbars are often deemed the best, reducing both switch count and capacitance by over 70% for an interleaver size of 100, as opposed to full crossbars, while maintaining full programmability.

## Iterative Viterbi algorithm for concatenated multidimensional TCM

- **Status**: ❌
- **Reason**: 다차원 TCM+패리티의 iterative Viterbi; 비-LDPC, BP 비의존적 trellis 기반으로 이식 불가
- **ID**: ieee:975736
- **Type**: journal
- **Published**: 2002
- **Authors**: Qi Wang, Lei Wei
- **PDF**: https://ieeexplore.ieee.org/document/975736
- **Abstract**: A novel compound code is designed for the multidimensional (M-D) Wei (1987) trellis code combined with a simple parity-check code. Using the iterative Viterbi decoding algorithm, we can achieve a remarkable performance improvement with low computational complexity. Simulation results show that at a bit error rate (BER) of 3.7 /spl times/ 10/sup -6/ about 2.2-dB additional net gain has been obtained over the conventional scheme of the 4-D 16-state Wei code at a spectral efficiency of 6.7871 bit/T.

## Shannon theory: perspective, trends, and applications special issue dedicated to aaron d. wyner

- **Status**: ❌
- **Reason**: 특별호 헌정사(서지 항목), 초록 없음, 기술 기여 없음
- **ID**: ieee:1003819
- **Type**: journal
- **Published**: 2002
- **Authors**: H. J. Landau, J. E. Mazo, S. Shamai +1
- **PDF**: https://ieeexplore.ieee.org/document/1003819
- **Abstract**: N/A

## An interactive concatenated turbo coding system

- **Status**: ❌
- **Reason**: RS+turbo concatenated 시스템; 비-LDPC 부호, 바이너리 LDPC BP 이식 기여 없음
- **ID**: ieee:1105938
- **Type**: journal
- **Published**: 2002
- **Authors**: Cathy Ye Liu, Heng Tang, Shu Lin +1
- **PDF**: https://ieeexplore.ieee.org/document/1105938
- **Abstract**: This paper presents a concatenated turbo coding system in which a Reed-Solomon outer code is concatenated with a binary turbo inner code. In the proposed system, the outer code decoder and the inner turbo code decoder interact to achieve both good bit error and frame error performance. The outer code decoder helps the inner turbo code decoder to terminate its decoding iteration while the inner turbo code decoder provides soft-output information to the outer code decoder to carry out a reliability-based algebraic soft-decision decoding algorithm. In the case that outer code decoding fails, the outer code decoder instructs the inner code decoder to continue its decoding iterations until outer code decoding is successful or a preset maximum number of decoding iterations is reached. This interaction between outer and inner code decoders reduces decoding delay.

## Timing recovery for magnetic recording using cross correlation

- **Status**: ❌
- **Reason**: 자기기록 타이밍복구(cross-correlation) — 부호화·디코더 무관
- **ID**: ieee:1042164
- **Type**: journal
- **Published**: 2002
- **Authors**: J. S. Goldberg, J. K. Wolf
- **PDF**: https://ieeexplore.ieee.org/document/1042164
- **Abstract**: This paper demonstrates a method for performing timing recovery for digital magnetic recording systems using cross correlation. Estimates of the written data are cross correlated with the incoming samples to derive phase error information. Retimed sample values are found via interpolation using the incoming samples and phase-error information. Results are compared to the decision-directed timing-recovery method commonly found in digital magnetic recording systems and it is shown that the cross-correlation timing-recovery method yields a lower bit-error rate for the same amount of mistiming in the incoming samples.

## Low-density parity check codes for long-haul optical communication systems

- **Status**: ❌
- **Reason**: 광통신 FEC로 LDPC를 적용해 성능 향상 보고만, 신규 디코더·구성·HW 기여 없는 단순 적용
- **ID**: ieee:1022020
- **Type**: journal
- **Published**: 2002
- **Authors**: B. Vasic, I. B. Djordjevic
- **PDF**: https://ieeexplore.ieee.org/document/1022020
- **Abstract**: Forward error correction (FEC) scheme based on low density parity check codes (LDPC) codes is presented in this paper. We show that LDPC codes provide a significant system performance enhancement with respect to the state-of-the-art FEC schemes employed in optical communication systems.

## Constrained systems with unconstrained positions

- **Status**: ❌
- **Reason**: 변조/제약 코드(MTR) + ECC 결합 구성으로, LDPC는 부수 언급일 뿐 떼어낼 디코더·코드설계 기법 없음
- **ID**: ieee:992774
- **Type**: journal
- **Published**: 2002
- **Authors**: J. Campello de Souza, B. H. Marcus, R. New +1
- **PDF**: https://ieeexplore.ieee.org/document/992774
- **Abstract**: We develop methods for analyzing and constructing combined modulation/error-correcting codes (ECC codes), in particular codes that employ some form of reversed concatenation and whose ECC decoding scheme requires easy access to soft information (e.g., turbo codes, low-density parity-check (LDPC) codes or parity codes). We expand on earlier work of Wijngaarden and Immink (1998, 2001), Immink (1999) and Fan (1999), in which certain bit positions are reserved for ECC parity, in the sense that the bit values in these positions can be changed without violating the constraint. Earlier work has focused more on block codes for specific modulation constraints. While our treatment is completely general, we focus on finite-state codes for maximum transition run (MTR) constraints. We (1) obtain some improved constructions for MTR codes based on short block lengths, (2) specify an asymptotic lower bound for MTR constraints, which is tight in very special cases, for the maximal code rate achievable for an MTR code with a given density of unconstrained positions, and (3) show how to compute the capacity of the set of sequences that satisfy a completely arbitrary constraint with a specified set of bit positions unconstrained.

## Iterative decoding and equalization for 2-D recording channels

- **Status**: ❌
- **Reason**: 2D 기록채널 반복 등화/검출에 LDPC를 ECC로 사용; LDPC는 베이스라인, 떼어낼 신규 디코더/구성 기법 없음
- **ID**: ieee:1001131
- **Type**: conference
- **Published**: 2002
- **Authors**: N. Singla, J. A. O'Sullivan, R. S. Indeck +1
- **PDF**: https://ieeexplore.ieee.org/document/1001131
- **Abstract**: Summary form only given. As conventional magnetic recording challenges physical limits, we are motivated to consider 2-dimensional (2-D) data storage techniques. Further motivation is provided by the fact that data in 2-D recording may be arranged in bigger sectors than in 1-D and error correcting codes (ECC) such as low density parity check codes (LDPCC) get arbitrarily close to capacity for large enough block lengths. In this paper we consider the use of LDPCC as an ECC in conjunction with equalization methods, iterative and otherwise, for a 2-D recording medium with 2-D ISI. Equalization methods for 2-D recording are discussed as is iterative detection.

## Layered space-time codes with iterative receiver and space-time soft-output decoding in a Rayleigh fading environment

- **Status**: ❌
- **Reason**: BLAST 공간시간 부호 + Viterbi 소프트출력, LDPC 미사용 무선 응용
- **ID**: ieee:1046734
- **Type**: conference
- **Published**: 2002
- **Authors**: F. S. Ostuni, B. Abdool-Rassool, M. R. Nakhai +1
- **PDF**: https://ieeexplore.ieee.org/document/1046734
- **Abstract**: We propose a modified BLAST architecture which employs space-time trellis codes at each layer as constituent codes, and an iterative parallel interference canceller (PIC) at the receiver. The PIC performs both interference regeneration and cancellation; and furthermore, the scheme employs maximum-likelihood soft-output decoders, based on the Viterbi algorithm. These decoders calculate the a posteriori probabilities of the codewords in order to produce a soft output. Comparisons are drawn against the original BLAST architecture and simulation results are obtained. A significant gain is achieved in the case of Horizontal BLAST and a similar gain for the case of Diagonal BLAST, at a reduced computational complexity.

## Optimal high-rate convolutional codes for partial response channels

- **Status**: ❌
- **Reason**: 자기기록 채널용 고율 convolutional 부호+SISO, 비-LDPC이고 부호특화 trellis SISO라 LDPC BP 이식 기여 없음
- **ID**: ieee:1188351
- **Type**: conference
- **Published**: 2002
- **Authors**: A. Graell i Amat, S. Benedetto, G. Montorsi
- **PDF**: https://ieeexplore.ieee.org/document/1188351
- **Abstract**: Optimized high-rate convolutional codes are considered as the outer encoder of a serially concatenated structure where the inner encoder is replaced by the magnetic recording channel. Simulation results of the iterative decoding algorithm for an equalized Lorentzian channel model and a more realistic model that includes data-dependent transition noise are presented. The effect of precoder on performance is also studied, and simulation results are supported by EXIT chart analysis. All results refer to a comparison of the optimized codes with previously proposed schemes employing punctured codes or non optimized unpunctured codes with tail-biting decoding. Both trellis termination and tail-biting termination of the high-rate codes are studied. To terminate the code trellis we use the method derived by Amat, Montorsi and Benedetto, which only requires /spl nu/ (the code memory) tail-biting bits. Simulation results confirm the ML analysis: owing to their better distance properties, the scheme based on the new codes outperform state-of-the-art magnetic recording schemes based on both punctured and non optimized high-rate codes. The cost of using an unpunctured code versus the punctured one in terms of increased decoding complexity is turned into an advantage by applying to the high-rate code the soft-input soft-output (SISO) algorithm working on its dual trellis.

## Coding-assisted MIMO joint detection and decoding in turbo-coded OFDM

- **Status**: ❌
- **Reason**: turbo-coded MIMO-OFDM 결합검출/디코딩 — turbo 전용, LDPC 이식 기법 없음
- **ID**: ieee:1040294
- **Type**: conference
- **Published**: 2002
- **Authors**: Xiangyang Zhuang, F. W. Vook
- **PDF**: https://ieeexplore.ieee.org/document/1040294
- **Abstract**: A new coding-assisted MIMO (CA-MIMO) receive algorithm is proposed that can approach the performance of an optimal MIMO receiver, but with a significantly reduced complexity. The algorithm starts with linear MIMO processing to obtain the log-likelihood ratios (LLRs) of the channel bits. Then, at the end of an intermediate turbo decoding iteration, it refines a few channel bit LLRs based on the computed distance to only a select number of symbol candidates, thus achieving the savings. The selection is based on the LLRs of the coded bits at that iteration. In a simulated two-transmit two-receive MIMO-OFDM 16-QAM system with a rate-1/2 turbo code, the proposed algorithm can improve the FER performance by more than 3 dB in a COST-259-style bad urban environment, compared with that of the MMSE MIMO receiver, and is only 0.2 dB away from that of the optimal receiver with exponential complexity.

## Runlength-limited (3,7) code for storage channels

- **Status**: ❌
- **Reason**: RLL (3,7) 변조부호 + CMOS 구현; LDPC ECC 아닌 런렝스제한 변조코드라 떼어낼 LDPC 기법 없음
- **ID**: ieee:1000871
- **Type**: conference
- **Published**: 2002
- **Authors**: Jaejin Lee, Youpyo Hong
- **PDF**: https://ieeexplore.ieee.org/document/1000871
- **Abstract**: Summary form only given. We propose a new highly efficient RLL code with the minimum run-length constraint d=3 and the maximum run-length constraint k=7 with CMOS implementation result.

## Analysis and design of interleaver mappings for iteratively decoded BICM

- **Status**: ❌
- **Reason**: BICM 인터리버/심볼매핑 설계 무선 응용, LDPC 무관
- **ID**: ieee:997081
- **Type**: conference
- **Published**: 2002
- **Authors**: Jun Tan, G. L. Stuber
- **PDF**: https://ieeexplore.ieee.org/document/997081
- **Abstract**: Iterative decoding of bit-interleaved coded modulation (BICM) is analyzed. The interleaver of a BICM system is shown to provide not only time diversity gain as a channel interleaver, but also interleaving gain as a code interleaver. Our performance analysis of BICM assumes a uniform interleaver, and it is shown that the interleaving gain can be achieved at high SNR. The design rules on the symbol mapper are derived and a new symbol mapper design, called the maximum squared Euclidean weight (MSEW) symbol mapper, is presented for both 8-PSK and 16-QAM. Extensions to other signal constellations is straight forward. Simulation results confirm our analysis and show that BICM with MSEW symbol mapping achieves near Shannon limit performance.

## Information geometry of statistical inference - an overview

- **Status**: ❌
- **Reason**: 정보기하 개요/서베이로 BP·LDPC를 사례로만 언급, 떼어낼 신규 디코더·구성·HW 기여 없음
- **ID**: ieee:1115423
- **Type**: conference
- **Published**: 2002
- **Authors**: S. Amari
- **PDF**: https://ieeexplore.ieee.org/document/1115423
- **Abstract**: The present paper gives a short introduction to information geometry, by using a simple model of an exponential family which is a dually flat Riemannian space. The paper then overviews some of the applications of information geometry: 1) the higher-order asymptotic theory of estimation; 2) semiparametric estimation of the parameter of interest; 3) learning neural networks under the Riemannian structure; and 4) analysis of turbo codes, low density parity check codes and belief propagation algorithm.

## Capacity of power constrained memoryless AWGN channels with fixed input constellations

- **Status**: ❌
- **Reason**: AWGN 용량/입력분포 계산(Blahut-Arimoto)·shaping, ECC 디코더/HW/코드설계 아님
- **ID**: ieee:1188416
- **Type**: conference
- **Published**: 2002
- **Authors**: N. Varnica, Xiao Ma, A. Kavcic
- **PDF**: https://ieeexplore.ieee.org/document/1188416
- **Abstract**: We propose a numerical method to compute the capacity of a power constrained memoryless additive white Gaussian noise (AWGN) channel with finite and fixed input alphabets. The method is based on a two-part algorithm. The first part is a modified version of the Blahut-Arimoto algorithm and the second part is a simple maximization algorithm over a single parameter. The optimal input distribution we obtain can be utilized to construct probabilistic codes for this channel. These codes promise to bridge the shaping gap between the uniform-input information rate and the capacity of the channel.

## Multi-user interference cancellation technique for coded OFDM-CDMA system

- **Status**: ❌
- **Reason**: OFDM-CDMA 다중사용자 간섭제거 무선 응용, LDPC 부수 사용, 떼어낼 ECC 기법 없음
- **ID**: ieee:1188130
- **Type**: conference
- **Published**: 2002
- **Authors**: Taeyoon Park, Jaechul Lee, Youngshin Ahn +2
- **PDF**: https://ieeexplore.ieee.org/document/1188130
- **Abstract**: In a mobile communication channel, the multi-user interference is one of the major performance degradation factors, and restoring the signal-to-signal orthogonality among users is the challenging problem. As a solution to the problem, we proposed a method of combining OFDM and CDMA into a coded OFDM-CDMA system. The proposed system is equipped with a multi-user interference suppression capability based on chip-based interference cancellation and adaptive DFE equalization in series with a low-density parity checker. The performance of the proposed system is verified in a reverse-link multipath Rayleigh fading channel using computer simulation. The overall system performance has improved over a single-carrier CDMA in terms of BER vs SNR.

## A measurement based feasibility study of space-frequency MIMO detection and decoding techniques for next generation wireless LANs

- **Status**: ❌
- **Reason**: MIMO/OFDM WLAN 검출·turbo 코딩 측정 연구 — LDPC 무관, 무선 응용 특이적, 제외.
- **ID**: ieee:1037068
- **Type**: journal
- **Published**: 2002
- **Authors**: R. Piechocki, P. Fletcher, A. Nix +2
- **PDF**: https://ieeexplore.ieee.org/document/1037068
- **Abstract**: This article presents a performance evaluation of various multi-antenna concepts based on OFDM for wireless LANs. The studies are based on state-of-the-art measured channel data in the 5 GHz band. The investigated techniques include: spatial multiplexing (BLAST), space frequency trellis coded modulation, their concatenation, turbo bit interleaved coded modulation and turbo space frequency trellis coded modulation. The studies aim to assess the MIMO concepts for future high speed WLANs.

## Predicting and adapting satellite channels with weather-induced impairments

- **Status**: ❌
- **Reason**: 위성채널 예측·적응(전력/변조/코드레이트) — 부호화·디코더 기법 아님
- **ID**: ieee:1039399
- **Type**: journal
- **Published**: 2002
- **Authors**: J. P. Choi, V. W. S. Chan
- **PDF**: https://ieeexplore.ieee.org/document/1039399
- **Abstract**: Efficiency improvements using predictive and adaptive methods over satellite channels with weather-induced impairments are presented. Scintillation and rain attenuation are the two dominant factors for signal fading over satellite-Earth paths at operating frequencies over 10 GHz. We develop statistical and spectral analyses of these processes, and obtain simple linear predictors for received signal attenuation using autoregressive (AR) models. For adaptation, we propose changing signal transmission power, modulation symbol size, and/or code rate as the state of the channel changes. In particular, we introduce a continuous power control and discrete rate control strategy. Quantitative analyses of power consumption and channel capacity indicate that there can be a substantial gain in performance with such adaptive schemes.
