# IEEE Xplore — 2015-10 (1차선별 통과)


## A Novel Construction Approach of Irregular LDPC Codes Based on QC Structure and Zigzag Pattern

- **Status**: ✅
- **Reason**: QC 구조+zigzag 기반 신규 irregular 바이너리 LDPC 구성, short cycle/low-weight codeword 회피 기준 제시 — 카테고리 E 코드설계 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10856913
- **Type**: journal
- **Published**: October 20
- **Authors**: Jing Lei, Chunguang Yao, Bin Chen +2
- **PDF**: https://ieeexplore.ieee.org/document/10856913
- **Abstract**: This paper presents a novel construction method of irregular Low-density parity-check (LDPC) codes based on Quasi-cyclic (QC) structure and zigzag pattern. By using the proposed method, a class of irregular and highly structured LDPC codes can be designed with the advantages of low storage requirement and linear time encoding complexity. The constructed codes are called Irregular repeat-accumulate like (IRA-like) codes since their parity-check matrices are similar with those of IRA codes, which all contain a sparse zigzag pattern submatrix. The left part of the parity-check matrix of IRA-like codes is a kind of circulant permutation matrix. A best-effort analyzing method for optimizing the cycle structure of IRA-like codes is presented. We further details the proper constraints for avoiding short cycles and low-weight code-words. Simulation results show that the proposed IRA-like codes have low encoding complexity, good iterative decoding performance and flexible choice of code parameters.

## Multimode Radix-4 SISO Kernel Design for Turbo/LDPC Decoding

- **Status**: ✅
- **Reason**: Turbo/LDPC 공용 radix-4 SISO 커널 VLSI 설계 — 카테고리 D LDPC 디코더 HW 아키텍처 이식 가능
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:6942228
- **Type**: journal
- **Published**: Oct. 2015
- **Authors**: Cheng-Hung Lin, Chih-Shiang Yu
- **PDF**: https://ieeexplore.ieee.org/document/6942228
- **Abstract**: To increase the quality of wireless transmission, wireless communication systems employ advanced forward error correction codes such as turbo codes and low-density parity-check (LDPC) codes. To achieve smooth transition between turbo and LDPC decoding in different communication standards, we propose a VLSI design of a multimode radix-4 soft-input soft-output (SISO) kernel in this paper. The proposed radix-4 SISO kernel composed of three recursive processing elements alternatively employs a radix-4 forward-backward algorithm for LDPC decoding and a radix-4 single-binary/double-binary enhanced max-log-maximum a posteriori probability algorithm for turbo decoding by efficiently sharing computational units. The proposed radix-4 SISO kernel achieves an area reduction of 21.8% when compared with the uncombined SISO kernels for alternatively decoding the turbo and LDPC codes. The proposed radix-4 SISO kernel is verified by implementing it in an application-specific integrated circuit of 0.45 mm2 core area by using a 90-nm CMOS process with a maximum area efficiency of 10.65 bits/mm2. In addition, the throughput rates of the long-term evolution and worldwide interoperability for microwave access schemes for both LDPC and turbo decoding can be achieved using eight proposed radix-4 SISO kernels.

## An Iterative Detection and Decoding Receiver for LDPC-Coded MIMO Systems

- **Status**: ✅
- **Reason**: LDPC-coded MIMO용 IDD 디코더 HW(40nm, layered non-resetting, 면적/에너지 효율) — 바이너리 LDPC 디코더 HW 아키텍처(D) 이식 가능
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:7272776
- **Type**: journal
- **Published**: Oct. 2015
- **Authors**: Wei-Cheng Sun, Wei-Hsuan Wu, Chia-Hsiang Yang +1
- **PDF**: https://ieeexplore.ieee.org/document/7272776
- **Abstract**: This paper presents a high-throughput, area-efficient and energy-efficient iterative detection and decoding (IDD) receiver for low-density parity-check (LDPC)-coded multiple-input multiple-output (MIMO) systems. A layered non-resetting IDD technique is used to minimize the number of inner iterations for a required error performance. An area-efficient minimum mean-square error with parallel interference cancellation (MMSE-PIC) detector is devised to simplify matrix inversion. A detector-decoder interface that is used to exchange soft messages efficiently is proposed. Given the throughput specifications, inner and outer loops are optimally combined to maximize the error performance. The design specifications defined in the IEEE 802.11n standard are adopted as the design target. A 4 × 4 antenna configuration with BPSK, QPSK, 16-QAM modulations are realized in silicon. The designs that support 64-QAM and 256-QAM modulations are also demonstrated for comparison with prior work. Fabricated in 40 nm technology, the chip integrates 998k logic gates in 1.33 mm2 and achieves a maximum throughput of 794 Mb/s. The chip dissipates 135 mW at 0.9 V, achieving an energy efficiency of 170 pJ/bit.

## A New Scheme of High Performance Quasi-Cyclic LDPC Codes With Girth 6

- **Status**: ✅
- **Reason**: 새 QC-LDPC 구성 기법(조합적 girth-6 설계, low error floor) — 바이너리 LDPC 코드 설계(E) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7163287
- **Type**: journal
- **Published**: Oct. 2015
- **Authors**: Sina Vafi, Narges Rezvani Majid
- **PDF**: https://ieeexplore.ieee.org/document/7163287
- **Abstract**: The letter presents a new technique for constructing regular and irregular quasi-cyclic (QC) low density parity check (LDPC) codes with girth 6. Codes are designed by the combinatorial concept, in which subsets representing circulant matrices are originated from a particular subset. Conducted simulations confirm that implemented codes have low error floor, while they provide good performance in the waterfall region.

## Iterative Receiver Design for ISI Channels Using Combined Belief- and Expectation-Propagation

- **Status**: ✅
- **Reason**: BP+EP 결합 메시지패싱 알고리즘, EP의 negative variance 해결법 제시 — 부호 비의존적 메시지패싱 개선으로 바이너리 LDPC BP 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7045526
- **Type**: journal
- **Published**: Oct. 2015
- **Authors**: Peng Sun, Chuanzong Zhang, Zhongyong Wang +2
- **PDF**: https://ieeexplore.ieee.org/document/7045526
- **Abstract**: In this letter, a message-passing algorithm that combines belief propagation and expectation propagation is applied to design an iterative receiver for intersymbol interference channels. We detail the derivation of the messages passed along the nodes of a vector-form factor graph representing the underlying probabilistic model. We also present a simple but efficient method to cope with the “negative variance” problem of expectation propagation. Simulation results show that the proposed algorithm outperforms, in terms of bit-error-rate and convergence rate, a LMMSE turbo-equalizer based on Gaussian message passing with the same order of computational complexity.

## Novel forward error correction concepts for coherent optical communications

- **Status**: ✅
- **Reason**: spatially coupled code(SC-LDPC) 신규 FEC 방향 제시; SC-LDPC 구성은 E 카테고리로 이식 가능, 애매하므로 살림(Phase3 재검토)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7323474
- **Type**: conference
- **Published**: 4-8 Oct. 2
- **Authors**: Laurent Schmalen
- **PDF**: https://ieeexplore.ieee.org/document/7323474
- **Abstract**: We discuss and present several new directions in forward error correction for coherent optical communications. In particular, we show how the class of spatially coupled codes can lead to new FEC schemes outperforming conventional codes.

## A low-latency algorithm for stochastic decoding of LDPC codes

- **Status**: ✅
- **Reason**: 이식 가능 디코더(C): conditional stochastic decoding으로 LDPC BP 지연 감소—바이너리 LDPC 디코더 신규 알고리즘
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7447188
- **Type**: conference
- **Published**: 29 Sept.-2
- **Authors**: Kuo-Lun Huang, Vincent C. Gaudet, Masoud Salehi
- **PDF**: https://ieeexplore.ieee.org/document/7447188
- **Abstract**: We introduce a low-latency stochastic decoding algorithm, called conditional stochastic decoding, to implement iterative Low-Density Parity-Check (LDPC) decoders. The conditional stochastic decoder, which utilizes reliable messages in the decoding process and the channel receiving probability to generate stochastic streams, improves error rate performance and decreases decoding latency. Compared to conventional stochastic decoders, the proposed algorithm achieves more than 20-percent reduction in the decoding latency for the (1056,528) LDPC code from the WiMAX standard. We also show that the proposed algorithm, due to its lower frame error rate, is a suitable choice to be used in the Hybrid Automatic Repeat reQuest (HARQ) systems.

## Energy-adaptive codes

- **Status**: ✅
- **Reason**: QC-LDPC 기반 energy-adaptive 코드 신규 구성(계층적, 배선 on/off), 코드 설계 기여(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7446995
- **Type**: conference
- **Published**: 29 Sept.-2
- **Authors**: Haewon Jeong, Pulkit Grover
- **PDF**: https://ieeexplore.ieee.org/document/7446995
- **Abstract**: We provide the first constructions of a new family of error-correcting codes called “energy-adaptive codes.” These codes are designed to enable adaptive circuit implementations that minimize the total system-level energy based on varying distances and target error probabilities. Recent work has explored fundamental limits and practical strategies for minimizing total (transmit + circuit) power, considering both power consumed in computational nodes as well as wires in the circuit. It is now established that to minimize total power, code choice and circuit-design should change with communication distances and/or target error probability. Motivated by circuit area constraints, the energy-adaptive codes adapt energy consumption as distances and/or target error probability change. These codes shrink and expand the wiring area they occupy as demands on the system change, adjusting the hardware by turning on and off non-local wires in the circuit. The code constructions are hierarchical, and use QC-LDPC codes as the basis. We estimate the decoding power savings attained by use of these codes through simulation results. Such codes can be of increasing utility as we enter the era of 1000 devices per person where designing the skilled labor for obtaining optimized designs for each system will simply be unavailable. While our first constructions are admittedly simplistic, the goal of the paper is to bring this new problem to the attention of the coding-theory community.

## A low-complexity decoding algorithm for concatenated tree codes

- **Status**: ✅
- **Reason**: 이식 가능 디코더(C): two-way scheduling 수정 BP 알고리즘, 부호 비의존적 메시지패싱+저복잡도 HW 적합—BP에 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7354592
- **Type**: conference
- **Published**: 28-30 Oct.
- **Authors**: Daesung Kim, Jeongseok Ha
- **PDF**: https://ieeexplore.ieee.org/document/7354592
- **Abstract**: This work considers a modified belief-propagation algorithm with two way scheduling for concatenated tree (CT) codes in which tree codes are employed as constituent codes. It will be shown that constituent tree codes can be efficiently decoded with the modified algorithm. Thus, by repeatedly using the modified BP algorithm for the constituent tree codes, CT codes can be decoded in an efficient way. Moreover, we show that the modified algorithm is especially suited for low complexity hardware implementation. Finally, a simple analysis technique for error-correcting performances of tree codes will be presented.

## On interleaver design for BICM system with low error-floors

- **Status**: ✅
- **Reason**: 코드 설계(E): 수정 QC 구조로 저중량 코드워드 제거→error-floor 개선, 저복잡도 HW—바이너리 QC 구성 신규 기여
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7354659
- **Type**: conference
- **Published**: 28-30 Oct.
- **Authors**: Sangha Lee, Jeongseok Ha, Jaeyoon Lee
- **PDF**: https://ieeexplore.ieee.org/document/7354659
- **Abstract**: In this paper, we propose a design rule of a modified quasi-cyclic structure for bit-interleaved coded modulation with iterative decoding (BICM-ID). The proposed structure is especially favorable for low-complexity hardware implementation. In addition, it will be shown that the proposed structure effectively removes low-weight codewords, which in turn greatly improves error-floor behaviors as compared to quasi-cyclic interleaver.

## Energy-efficient soft-decision LDPC FEC For long-haul optical communication

- **Status**: ✅
- **Reason**: 저복잡도 LDPC 디코딩 알고리즘+랜덤구조 LDPC 코드+ASIC 합성, 이식 가능 디코더/HW 기여 가능성(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7341747
- **Type**: conference
- **Published**: 27 Sept.-1
- **Authors**: Kevin Cushon, Per Larsson-Edefors, Peter Andrekson
- **PDF**: https://ieeexplore.ieee.org/document/7341747
- **Abstract**: We present forward error correction systems based on a low-complexity LDPC decoding algorithm and randomly-structured LDPC codes. Simulation and ASIC synthesis results show throughput and net coding gain sufficient for long-haul applications, with greatly reduced energy consumption.

## A log-likelihood ratio for improved receiver performance for VLF/LF communication in atmospheric noise

- **Status**: ✅
- **Reason**: 임펄스성 대기잡음에 적응한 복조기 LLR 설계 — 비AWGN 채널 LLR 산출 기법은 NAND LDPC 입력 LLR 양자화/설계(C)에 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7357596
- **Type**: conference
- **Published**: 26-28 Oct.
- **Authors**: K. Wiklundh, K. Fors, P. Holm
- **PDF**: https://ieeexplore.ieee.org/document/7357596
- **Abstract**: Receiver-improving techniques are important for submarine communication at the LF/VLF bands, due to very demanding reception conditions. At the surface, the interference environment is dominated by the atmospheric noise, which is highly impulsive in character and may impede the reception of the radio signals. To handle the demanding channel and the impulsive interference environment, error correction and an adapted receiver are necessary. In this paper, we propose a log-likelihood ratio (LLR) as soft output from the demodulator suitable for atmospheric noise. The radio system is assumed to use minimum shift keying (MSK) and a low parity density check (LDPC) code. It is shown that the proposed interference-adapted LLR improves the performance substantially in atmospheric noise compared to when the LLR is designed for AWGN. The performance is also compared to a solution, where the soft output from the demodulator is simplified to a limiter, and to a solution when a larger system bandwidth is used in combination with a limiter. It is concluded that the proposed interference-adapted LLR achieves the best performance in the comparison, although the performance could probably be further improved, when compared to the obtained Shannon capacity of this particular interference.

## Construction of LDPC codes based on resolvable group divisible designs

- **Status**: ✅
- **Reason**: E: 바이너리 정규 LDPC 새 구성법(RGDD 기반, girth>=6, low error floor) — 이식 가능 코드 설계
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7354346
- **Type**: conference
- **Published**: 21-23 Oct.
- **Authors**: Hengzhou Xu, Dan Feng, Cheng Sun +1
- **PDF**: https://ieeexplore.ieee.org/document/7354346
- **Abstract**: In this paper, we present a method for constructing LDPC codes from resolvable group divisible designs (RGDDs). According to the incidence matrices (or their submatrices) of RGDDs, a class of regular LDPC codes can be constructed. Since the parity-check matrix of the resulting code satisfies the row-column constraint, the girth of the proposed codes is at least six. Furthermore, based on a resolvable group divisible design, we can obtain a sequence of LDPC codes with various lengths and rates, which perform well over the AWGN channel with iterative decoding and have low error floors.

## Construction of cyclic one-step majority-logic decodable codes using genetic algorithms

- **Status**: ✅
- **Reason**: 유전알고리즘 기반 신규 바이너리 순환 OSMLD(LDPC) 부호 구성 — 코드설계(E) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7381301
- **Type**: conference
- **Published**: 20-23 Oct.
- **Authors**: Anouar Yatribi, Fouad Ayoub, Mostafa Belkasmi
- **PDF**: https://ieeexplore.ieee.org/document/7381301
- **Abstract**: In [6], a construction of cyclic one-step majority-logic decodable codes based on idempotent polynomials is given. However, the search for the feasible Parity-Check Idempotent runs through all possible combinations of cyclotomic cosets modulo n, satisfying some algebraic constraints, consequently, increasing the code length may result in very large dimension space search, and the search for the solution becomes more difficult. In this paper, we propose a Genetic Algorithm that aimes to construct new moderate and high lengths Binary Cyclic OSMLD codes, considered as LDPC codes, with high correction capacities. Our construction is very efficient and provide codes with high lenghts and high rates.

## A shared hard decisions storing in partially parallel FPGA-based QC-LDPC decoder

- **Status**: ✅
- **Reason**: 부분병렬 FPGA QC-LDPC 디코더 hard decision 메모리 공유로 33% 메모리 절감 — HW 아키텍처 이식 가능 (D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:7454239
- **Type**: conference
- **Published**: 16-18 Oct.
- **Authors**: Tianjiao Xie, Ruijia Yuan, Jianhua Zhang
- **PDF**: https://ieeexplore.ieee.org/document/7454239
- **Abstract**: A strategy of hard decisions sharing intrinsic and extrinsic memory banks for partially parallel Quasi-Cyclic (QC) LDPC decoder is proposed in this paper. The proposed method not need extra memory banks to store hard decisions, could reduce the total number of memory by 33% compared with the decoder in reference [6] which is significantly fewer memory banks than the other published FPGA implementations decoders in reference [4-8], while maintaining the same hardware requirements at the same throughput level.

## Joint design of QC-LDPC codes for cascade-based multisource coded cooperation

- **Status**: ✅
- **Reason**: QC-LDPC girth-4 사이클(Type-I/II) 제거 공동 설계 — 사이클 제거 코드설계 기법 이식 가능 (E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7340967
- **Type**: conference
- **Published**: 15-17 Oct.
- **Authors**: Shunwai Zhang, Rongfang Song, Fengfan Yang
- **PDF**: https://ieeexplore.ieee.org/document/7340967
- **Abstract**: Quasi-cyclic low-density-parity-check (QC-LDPC) codes are jointly designed for cascade-based multisource coded cooperation system. Firstly, QC-LDPC codes based on the base matrix and exponent matrix are introduced, and then two types of girth-4 cycles in QC-LDPC codes employed by the sources and relay are explicated. Secondly, we propose joint design method of QC-LDPC codes employed by the sources and relay, by which all girth-4 cycles including both Type-I and Type-II are canceled. Numerical simulations show that the jointly designed QC-LDPC coded cooperation well combines cooperation gain and channel coding gain, and outperforms the coded noncooperation under the same conditions. Furthermore, the bit error rate (BER) performance of the coded cooperation employing jointly designed QC-LDPC codes is better than those of random LDPC codes and separately designed QC-LDPC codes over AWGN channels.

## A mixed behavior/structural model for analog LDPC decoders including mismatch effects and dynamic behavior

- **Status**: ✅
- **Reason**: 아날로그 LDPC 디코더의 mismatch·동적거동 포함 거동/구조 혼합 모델 — HW 구현/최적화 기법(D)으로 이식 가능성, 애매하여 살림
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:7341182
- **Type**: conference
- **Published**: 15-17 Oct.
- **Authors**: Zhe Zhao, Fei Gao, Hanyue Li +2
- **PDF**: https://ieeexplore.ieee.org/document/7341182
- **Abstract**: The analog implementation of error control decoders is a power efficiency and speed competitive methodology comparing with the digital implementation. In this paper, we propose a mixed behavioral/structural model for the analog implementation of low-density parity-check (LDPC) decoders based on the sum-product algorithm, while taking transistor mismatch effects and circuit dynamic behavior into account. The model, relating transistor-level parameters to system-level specifications, can be used for both estimating the system performance of the analog decoders and providing circuit-optimization guidelines for complex decoder. The model is applied to a (40, 16) linear block code and simulation results demonstrated the model can reliably predict the system performance in a short time.

## Low complexity memory architectures based on LDPC codes: Benefits and disadvantages

- **Status**: ✅
- **Reason**: 메모리 셀에 LDPC 부호로 저장하는 신뢰성 메모리 아키텍처 — 스토리지 ECC 일반(B)에 부합
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7357727
- **Type**: conference
- **Published**: 14-17 Oct.
- **Authors**: Bane Vasić, Predrag Ivaniš, Srdan Brkic
- **PDF**: https://ieeexplore.ieee.org/document/7357727
- **Abstract**: In this paper we investigate the problem of information storage in inherently unreliable memory cells. In order to increase the memory reliability, information is stored in memory cells as a codeword of a low-density parity-check (LDPC) code, while the memory content is updated periodically by an error correction scheme. We first present an overview on the state-of-the memory architectures based on LDPC codes, and then asses the benefits of using the coded architectures expressed through the increased reliability. In addition, we provide upper bounds on the complexity of such memories.

## LDPC decoder architecture for DVB-S2 and DVB-S2X standards

- **Status**: ✅
- **Reason**: DVB-S2/S2X layered LDPC 디코더 아키텍처, barrel shifter 제거 등 HW 기법 — 이식 가능 HW(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:7345034
- **Type**: conference
- **Published**: 14-16 Oct.
- **Authors**: Cédric Marchand, Emmanuel Boutillon
- **PDF**: https://ieeexplore.ieee.org/document/7345034
- **Abstract**: A particular type of conflict due to multiple-diagonal sub-matrices in the DVB-S2 parity-check matrices is known to complicate the implementation of the layered decoder architecture. The new matrices proposed in DVB-S2X no longer use such sub-matrices. For implementing a decoder compliant both with DVB-S2 and DVB-S2X, we propose an elegant solution which overcomes these conflicts. The solution relye on an efficient write disable of the memories, allowing a straightforward implementation of layered LDPC decoders. The complexity and latency are further reduced by eliminating one barrel shifter. Compared with the existing solutions, complexity is reduced without performance degradation.

## A fully-unrolled LDPC decoder based on quantized message passing

- **Status**: ✅
- **Reason**: 유한알파벳 메시지패싱(LUT 기반 VN 업데이트, 상호정보 최대화) + fully-unrolled HW — 이식 가능 디코더/HW(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7345024
- **Type**: conference
- **Published**: 14-16 Oct.
- **Authors**: Alexios Balatsoukas-Stimming, Michael Meidlinger, Reza Ghanaatian +2
- **PDF**: https://ieeexplore.ieee.org/document/7345024
- **Abstract**: In this paper, we propose a finite alphabet message passing algorithm for LDPC codes that replaces the standard min-sum variable node update rule by a mapping based on generic look-up tables. This mapping is designed in a way that maximizes the mutual information between the decoder messages and the codeword bits. We show that our decoder can deliver the same error rate performance as the conventional decoder with a much smaller message bit-width. Finally, we use the proposed algorithm to design a fully unrolled LDPC decoder hardware architecture.

## A high-throughput multi-rate LDPC decoder for error correction of solid-state drives

- **Status**: ✅
- **Reason**: SSD용 고처리율 multi-rate LDPC 디코더, adaptive NMS + LUT VLSI 구현 — A/C/D 직접 부합
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7345006
- **Type**: conference
- **Published**: 14-16 Oct.
- **Authors**: Yishan Zhang, Chun Zhang, Zhiyuan Yan +2
- **PDF**: https://ieeexplore.ieee.org/document/7345006
- **Abstract**: This paper presents a high-throughput multi-rate low density parity check (LDPC) decoder for error correction in solid-state drives (SSDs). In order to meet the high throughput requirement of SSDs, an adaptive normalized min-sum algorithm (NMSA) is implemented by using multiple look-up tables. With the proposed technique, a reduction in average iteration number of around 22.5%∼30.3% is achieved when signal-to-noise ratio (SNR) is 6.14dB, and the area overhead is only 0.87%. The LDPC decoder is implemented in TSMC 65nm standard CMOS technology. For a rate-0.889 length-36864 quasi-cyclic (QC) LDPC code, the decoder achieves a throughput of 14.9 Gb/s with an area of 5.365 mm2, and compares favorably with previously proposed architectures.

## A parallel-routing network for reliability inferences of single-parity-check decoder

- **Status**: ✅
- **Reason**: SPC/LDPC 디코더용 병렬 라우팅 네트워크 + LUT 기반 FPGA 구현 — 이식 가능 HW 아키텍처(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:7388304
- **Type**: conference
- **Published**: 14-16 Oct.
- **Authors**: Qing Lu, Zhuoer Shen, Chiu-Wing Sham +1
- **PDF**: https://ieeexplore.ieee.org/document/7388304
- **Abstract**: The computation of the reliability inferences among the variables of a single-parity-check (SPC) code is a common challenge to the implementation of channel decoders. Applicable to a variety of computational mechanisms using disparate kernels, a parallel-routing network has been developed, which is, compared to the state-of-art structure, exploring the best of its parallel nature for an improved timing performance. Furthermore, we assure that the proposed structure has no degradation in neither computation accuracy nor hardware complexity. With this structure, the LUT-based method becomes the optimal solution as a whole to implement an SPC decoder and other decoders containing it, like, for example, a low-density parity-check (LDPC) decoder. The improvement of the proposed design has been verified by a field-programmable gate array (FPGA), showing a 186% increase in clock rate for a 32-degree SPC decoder.

## Low-power LDPC decoder design exploiting memory error statistics

- **Status**: ✅
- **Reason**: 전압스케일링/메모리 에러통계 기반 저전력 LDPC 디코더 + 반복수 조정 기법 — NAND LDPC 디코더 HW에 이식 가능(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:7315157
- **Type**: conference
- **Published**: 12-14 Oct.
- **Authors**: Junlin Chen, Lei Wang
- **PDF**: https://ieeexplore.ieee.org/document/7315157
- **Abstract**: This paper presents a low-power LDPC decoder design by exploiting inherent memory error statistics due to voltage scaling. By analyzing the error sensitivity to the decoding performance at different memory bits and memory locations in the LDPC decoder, the scaled supply voltage is applied to memory bits with high algorithmic error-tolerance capability to reduce the memory power consumption while mitigating the impact on decoding performance. We also discuss how to improve the tolerance to memory errors by increasing the number of iterations in LDPC decoders, and investigate the energy overheads and the decoding throughput loss due to extra iterations. Simulation results of the proposed low-power LDPC decoder technique demonstrate that, by deliberately adjusting the scaled supply voltage to memory bits in different memory locations, the memory power consumption as well as the overall energy consumption of the LDPC decoder can be significantly reduced with negligible performance loss.

## New PEG algorithm with low error floor for construction of irregular LDPC codes

- **Status**: ✅
- **Reason**: 개선된 PEG 알고리즘으로 irregular LDPC 단블록 error floor 저감 — 바이너리 코드 설계(E) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7387584
- **Type**: conference
- **Published**: 10-11 Oct.
- **Authors**: Feijin Shi, Shuangshuang Han
- **PDF**: https://ieeexplore.ieee.org/document/7387584
- **Abstract**: The progressive-edge-growth (PEG) algorithm for constructing Tanner graphs with large girth by progressively establishing edges/connections between symbol nodes and check nodes in an edge-by-edge way is highly known to construct low-density parity-check (LDPC) codes at short block lengths for achieving good performance. This paper proposed an improved PEG construction for irregular codes, which heuristically selects good codes from random graphs for short block lengths. The simulation results are given to demonstrate that the proposed algorithm gians better BER performance for high signal-to-noise (SNR) ratios without performance loss for low-SNR region, i.e. low error floor.

## Linear-encodable rate-compatible QC-LDPC codes with low error floor

- **Status**: ✅
- **Reason**: 선형인코딩·낮은 error floor의 rate-compatible QC-LDPC 구성(LT form, layered short-cycle 최적화, density evolution) — 바이너리 LDPC 코드 설계 신규 기여(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7387582
- **Type**: conference
- **Published**: 10-11 Oct.
- **Authors**: Song Zhang, Linhua Ma, Le Ru +3
- **PDF**: https://ieeexplore.ieee.org/document/7387582
- **Abstract**: A class of rate-compatible (RC) quasi-cycle low-density parity-check (QC-LDPC) codes that have linear encodable complexity and low error floor is presented. To ensure linear encoding complexity, a lower triangular (LT) form for the parity part of the mother parity-check matrix is designed. By the designed LT form, a recursive encoding strategy is proposed. This encoding strategy can achieve linear encodable complexity, which is completely proportional to the code length. To guarantee good performances for a wide range of code rates, a layered short-cycle optimization algorithm is designed to obtain good girth distribution, and a layered density evolution algorithm is used to optimize degree distributions of each code rate. Then, a class of RC QC-LDPC codes can be obtained by both extension and puncturing from the optimized QC-LDPC mother code with rate 1/2. Simulation results show that no error floor is exhibited for the proposed RC QC-LDPC codes at FER=10−5. The practical performance at BER=10−6 shows a gap of about 1.477 dB to the Shannon limit.

## Unequal Error Protection of Memories in LDPC Decoders

- **Status**: ✅
- **Reason**: LDPC 디코더 메모리 UEP 보호 기법+HW 구현/면적·전력 평가 - 디코더 HW 신뢰성 기법으로 이식 가능(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:6977956
- **Type**: journal
- **Published**: 1 Oct. 201
- **Authors**: Carlo Condo, Guido Masera, Paolo Montuschi
- **PDF**: https://ieeexplore.ieee.org/document/6977956
- **Abstract**: Memories are one of the most critical components of many systems: due to exposure to energetic particles, fabrication defects and aging they are subject to various kinds of permanent and transient errors. In this scenario, Unequal error protection (UEP) techniques have been proposed in the past to encode stored information, allowing to detect and possibly recover from errors during load operations, while offering different levels of protection to partitions of codewords according to their importance. Low-density parity-check (LDPC) codes are used in many communication standards to encode the transmitted information: at reception, LDPC decoders heavily rely on memories to store and correct the received information. To ensure efficient and reliable decoding of information, the need to protect the memories used in LDPC decoders is of primary importance. In this paper we present a study on how to efficiently design UEP techniques for LDPC decoder memories. The devised UEP method is divided in four adjustable levels, each one offering a different degree of protection. The full UEP, along with simplified versions, has been implemented within an existing decoder and its area occupation and power consumption evaluated. Comparison with the literature on the subject shows an unmatched level of protection from errors at a small complexity and energy cost.
