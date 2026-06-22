# IEEE Xplore — 2010-06 (1차선별 통과)


## Performance and Complexity of 32 k-bit Binary LDPC Codes for Magnetic Recording Channels

- **Status**: ✅
- **Reason**: 바이너리 QC-LDPC(32k-bit) 부호 설계/복잡도 분석, column weight up to 13 girth-6 구성 — 이식 가능 코드설계(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5467496
- **Type**: journal
- **Published**: June 2010
- **Authors**: Seungjune Jeon, B. V. K. Vijaya Kumar
- **PDF**: https://ieeexplore.ieee.org/document/5467496
- **Abstract**: Recently, 32 k-bit sector size for hard disk drives is being investigated to take advantage of the superior performance of long error correcting codes. Meanwhile, low-density parity-check (LDPC) codes have been actively investigated for obtaining coding gains over conventional Reed-Solomon (RS) codes mainly for 4 k-bit sectors. In this paper, the coding gain of a 32 k-bit LDPC code over a 4 k-bit LDPC code, a 32 k-bit RS code, and a 4 k-bit RS code in magnetic recording channels is investigated. The decoding complexity of 32 k-bit LDPC codes and 4 k-bit LDPC codes is also discussed. It is important to evaluate whether the coding gains are enough to justify the increased complexity. Using the 32 k-bit LDPC code, 0.8-dB gain over the 32 k-bit RS code or the 4 k-bit LDPC code (the two schemes coincidentally showed similar performance) at 32 k-bit block error rate (BLER) $10^{-3}$ , and 1.6-dB gain over the 4 k-bit RS code were obtained. It is shown that 32 k-bit LDPC codes require a larger number of iterations than the 4 k-bit LDPC codes. It is also shown that there is much room to improve the design of 32 k-bit LDPC codes than the code used in the simulation. To illustrate the potential, quasicyclic LDPC codes with column weights up to 13 with girth 6 are investigated.

## RS Plus LDPC Codes for Perpendicular Magnetic Recording

- **Status**: ✅
- **Reason**: 마그네틱 레코딩 스토리지용 RS+LDPC concatenated, column weight별 성능과 error floor 분석 — 스토리지 ECC(B)+error floor(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5467440
- **Type**: journal
- **Published**: June 2010
- **Authors**: Wu Chang, J. R. Cruz
- **PDF**: https://ieeexplore.ieee.org/document/5467440
- **Abstract**: In this paper, we investigate RS plus LDPC concatenated architectures for perpendicular magnetic recording channels. Using simulations, we find the optimal code rate and iterative scheme for the concatenated codes, compare their performance in both random noise and media defects, and show that those whose inner LDPC codes have lower column weights exhibit better performance. In addition, we estimate the performance of the concatenated codes with inner LDPC codes of column weight two, at very high signal-to-noise ratios, and find their error floors.

## Signal Processing for Near 10 Tbit/in$^{2}$ Density in Two-Dimensional Magnetic Recording (TDMR)

- **Status**: ✅
- **Reason**: TDMR 스토리지 채널에 LDPC+2D 등화 아키텍처; 스토리지 ECC 일반(B), unwritten bit LLR 모델링 이식 가능성
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5467383
- **Type**: journal
- **Published**: June 2010
- **Authors**: E. Hwang, R. Negi, B. V. K. Vijaya Kumar
- **PDF**: https://ieeexplore.ieee.org/document/5467383
- **Abstract**: Two-dimensional magnetic recording (TDMR) is a new magnetic recording paradigm that aims to record one bit of information in one or a few grains, with the goal of achieving a recording density of nearly 10 Tbit/in$^{2}$. In addition to the usual noise, a TDMR channel experiences the problem that some bits are never recorded because of the randomness of grain size and location. Thus, it is believed that a key component of a TDMR channel is two-dimensional (2-D) signal processing along with a strong error correction code. In this study, the TDMR channel is investigated based on a random Voronoi grain model and a signal processing architecture is proposed. Here, a 2-D linear minimum mean squared error (LMMSE) equalizer and a low-density parity-check (LDPC) code are employed and the effects of unwritten bits are modeled by a Gaussian mixture model. In numerical simulations, the proposed architecture shows the feasibility of user bit densities near 10 Tbit/in$^{2}$  for media with a 20 ${\rm Tgrains/in}^{2}$ grain density.

## Error Correction Capability of Column-Weight-Three LDPC Codes Under the Gallager A Algorithm—Part II

- **Status**: ✅
- **Reason**: column-weight-3 LDPC의 girth-에러정정능력 관계와 trapping set 분석, Gallager A 알고리즘 — 이식 가능 코드설계/디코더(E/C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5466541
- **Type**: journal
- **Published**: June 2010
- **Authors**: Shashi Kiran Chilappagari, Dung Viet Nguyen, Bane Vasic +1
- **PDF**: https://ieeexplore.ieee.org/document/5466541
- **Abstract**: The relation between the girth and the error correction capability of column-weight-three LDPC codes under the Gallager A algorithm is investigated. It is shown that a column-weight-three LDPC code with Tanner graph of girth g ¿ 10 can correct all error patterns with up to (g/2-1) errors in at most g/2 iterations of the Gallager A algorithm. For codes with Tanner graphs of girth g ¿ 8, it is shown that girth alone cannot guarantee correction of all error patterns with up to (g/2-1) errors under the Gallager A algorithm. Sufficient conditions to correct (g/2-1) errors are then established by studying trapping sets.

## Gradient descent bit flipping algorithms for decoding LDPC codes

- **Status**: ✅
- **Reason**: Gradient descent bit-flipping (GDBF) decoding for binary LDPC, novel decoder algorithm directly portable (C).
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5474623
- **Type**: journal
- **Published**: June 2010
- **Authors**: Tadashi Wadayama, Keisuke Nakamura, Masayuki Yagita +3
- **PDF**: https://ieeexplore.ieee.org/document/5474623
- **Abstract**: A novel class of bit-flipping (BF) algorithm for decoding low-density parity-check (LDPC) codes is presented. The proposed algorithms, which are referred to as gradient descent bit flipping (GDBF) algorithms, can be regarded as simplified gradient descent algorithms. The proposed algorithms exhibit better decoding performance than known BF algorithms, such as the weighted BF algorithm or the modified weighted BF algorithm for several LDPC codes.

## Error Floor Estimation of Long LDPC Codes on Magnetic Recording Channels

- **Status**: ✅
- **Reason**: 긴 LDPC error floor 추정, trapping set 기반 방법+FPGA 시뮬; 스토리지 채널 error floor 분석(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5467506
- **Type**: journal
- **Published**: June 2010
- **Authors**: Xinde Hu, Zongwang Li, B. V. K. Vijaya Kumar +1
- **PDF**: https://ieeexplore.ieee.org/document/5467506
- **Abstract**: The presence of error floor in low density parity check (LDPC) codes is of great concern for potential applications of LDPC codes to data storage channels, which require the code to maintain the near capacity error correcting performance down to frame error rates of $10^{-12}$. In order to investigate the error floor of LDPC codes under magnetic recording channels used in data storage systems, we extended the trapping set based estimation method to predict the error floor under magnetic recording channels. The goal is to accurately estimate the error rates in the error floor region for certain types of LDPC codes under the partial response channel. First, we use field-programmable gate array (FPGA) hardware simulation to find the trapping sets that cause the decoding failure in the error floor region. For each trapping set, we extract the parameters that are key to the decoding failure caused by this trapping set. Then we use a much simpler in situ simulation with these parameters to obtain the conditional decoding failure rate. By considering all the trapping sets, we obtain the overall frame error rate in the error floor region. The estimation results under the magnetic recording channel are within 0.3 dB of the direct simulation results.

## Low-power design of variable block-size LDPC decoder using nanometer technology

- **Status**: ✅
- **Reason**: 이식 가능 HW 아키텍처(D): variable block-size LDPC 디코더, 파이프라인/병렬/단일 라우팅 네트워크, TDMP/SMSA VLSI 구현
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:5537590
- **Type**: conference
- **Published**: 30 May-2 J
- **Authors**: Chih-Hung Lin, Alex Chien-Lin Huang, Robert Chen-Hao Chang +1
- **PDF**: https://ieeexplore.ieee.org/document/5537590
- **Abstract**: This paper presents a low-power, variable block-size and irregular LDPC decoding. Our proposed LDPC decoder uses nanometer technology running the well-known TDMP and SMSA decoding algorithm. We further improved the design with pipeline structure, parallel computation and without any memory unit. Therefore, we can utilize only one routing network to route three different block-size data. The prototype architecture is being implemented on 90 nm VLSI technology. Because this VLSI technology has multi-Vth layers, we can make the design more effective. Compared to recent state-of-the-art architectures, the proposed variable block-size LDPC decoder has 450 MHz clock frequency, 349.48 K gate counts, 168 mW power dissipation, and 1.215 Gbps throughput.

## Low power decoder design for QC-LDPC codes

- **Status**: ✅
- **Reason**: 이식 가능 HW(D): layered min-sum 기반 저전력 QC-LDPC 디코더, message length-shortening + bit-serial CNU 신규 기법
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:5537671
- **Type**: conference
- **Published**: 30 May-2 J
- **Authors**: Kai He, Jin Sha, Li Li +1
- **PDF**: https://ieeexplore.ieee.org/document/5537671
- **Abstract**: This paper presents a low-power decoder design approach for generic quasi-cyclic low-density parity-check (QC-LDPC) codes based on the layered min-sum decoding algorithm. To reduce the energy consumption, a novel message length-shortening scheme is explored. The check node processing unit (CNU) is accordingly optimized using bit-serial architecture. This low cost design scheme can greatly lower the power consumption while maintaining the necessary throughput required by mobile applications. We further demonstrate the benefits of the proposed techniques by applying the new architecture to the QC-LDPC code in CMMB standard.

## Dual-rail decoding of low-density parity-check codes

- **Status**: ✅
- **Reason**: 이식 가능 디코더 스케줄링(C/D): CN/VN 완전 오버랩 스케줄링으로 throughput 증가, PCM 형태 무제약 - 바이너리 LDPC BP에 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5537628
- **Type**: conference
- **Published**: 30 May-2 J
- **Authors**: Bongjin Kim, Hasan Ahmed, In-Cheol Park
- **PDF**: https://ieeexplore.ieee.org/document/5537628
- **Abstract**: In this paper, a new scheduling scheme is proposed to increase the throughput of a low-density parity-check decoder by maximizing resource utilization. The operations of check nodes and variable nodes are fully overlapped in the proposed scheduling to achieve maximized utilization of hardware resources, which in turn increases the throughput and reduces the overall decoding latency. Moreover, no restriction is posed on the formation of the parity check matrix. To verify the effectiveness of the proposed scheme, a series of simulations is performed for irregular random LDPC codes with considering additive white Gaussian noise channel.

## Constructing high-rate scale-free LDPC codes

- **Status**: ✅
- **Reason**: 이식 가능 코드 설계(E): high-rate scale-free LDPC의 degree-2 노드 small-cycle 문제에 새 제약 부과 - 사이클 제거/코드 구성 기법
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5537734
- **Type**: conference
- **Published**: 30 May-2 J
- **Authors**: X. Zheng, F. C. M. Lau, C. K. Tse
- **PDF**: https://ieeexplore.ieee.org/document/5537734
- **Abstract**: Low-density parity-check (LDPC) codes with scale-free (SF) symbol-node degree distribution have been shown to provide very good error performance. When the code rate becomes high, however, there will be a lot of degree-2 symbol nodes in the “pure” SF-LDPC codes. As a consequence, when the codes are constructed by connecting the symbol nodes with the check nodes, many small-size cycles will be formed. Such small-cycles will degrade the error performance of the codes. In this paper, we address the issue by imposing a new constraint on the design of high-rate SF-LDPC codes. We will compare the error rates of the constrained SF-LDPC codes and other optimized LDPC codes.

## A flexible LDPC decoder architecture supporting two decoding algorithms

- **Status**: ✅
- **Reason**: 이식 가능 HW(D): TPMP/TDMP 둘 다 지원하는 프로그래머블 area-efficient Block-LDPC 디코더 아키텍처
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:5537686
- **Type**: conference
- **Published**: 30 May-2 J
- **Authors**: Shuangqu Huang, Dan Bao, Bo Xiang +2
- **PDF**: https://ieeexplore.ieee.org/document/5537686
- **Abstract**: In this paper a programmable and area-efficient decoder architecture supporting two main stream decoding algorithms for any Block-LDPC codes is presented. The novel decoder can be configured to decode in either TPMP or TDMP decoding mode according to different Block-LDPC codes. To verify our proposed architecture, a flexible LDPC decoder which supports IEEE 802.16e is implemented using a 0.13um CMOS process with a total area of 6.3 mm2 and maximum clock frequency of 260 MHz. The estimated comsumption is 270 mW when operates at 125 MHz and 1.2V supply.

## An early stopping criterion for decoding LDPC codes in WiMAX and WiFi standards

- **Status**: ✅
- **Reason**: 이식 가능 디코더 기법(C): 새 조기종료 기준(정보비트 정정 시 중단) - 바이너리 LDPC BP에 이식 가능, WiMAX/WiFi는 응용 예시일 뿐
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5537638
- **Type**: conference
- **Published**: 30 May-2 J
- **Authors**: Zhixiang Chen, Xiongxin Zhao, Xiao Peng +2
- **PDF**: https://ieeexplore.ieee.org/document/5537638
- **Abstract**: Based on the particular structure of parity check matrix (PCM) of LDPC codes in WiMAX and WiFi wireless communication standards, a new early stopping criterion (SC) is proposed to save the unnecessary decoding iterations. By using the proposed SC, decoding process will be stopped if all the information bits in a code word are corrected even if there are still some errors in the redundant (parity) part. Simulation shows that our proposed SC outperforms previous ones on decoding speed evaluated by average iteration number (AIN) with no bit error rate (BER) performance loss.

## A memory mapping approach for parallel interleaver design with multiples read and write accesses

- **Status**: ✅
- **Reason**: 이식 가능 HW(D): 병렬 디코더용 collision-free 메모리 매핑/인터리버 설계, LDPC 명시 적용 - 병렬화 아키텍처 기법
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:5537955
- **Type**: conference
- **Published**: 30 May-2 J
- **Authors**: C. Chavet, P. Coussy
- **PDF**: https://ieeexplore.ieee.org/document/5537955
- **Abstract**: For high throughput applications, turbo-like iterative decoders are implemented with parallel architectures. However, to be efficient parallel architectures require to avoid collision accesses i.e. concurrent read/write accesses should not target the same memory block. This consideration applies to the two main classes of turbo-like codes which are Low Density Parity Check (LDPC) and Turbo-Codes. In this paper we propose a methodology which always finds a collision-free mapping of the variables in the memory banks and which optimizes the resulting interleaving architecture. Finally, we show through a pedagogical example the interest our approach. This research was supported by the European project DAVINCI.

## Construction of quasi cyclic LDPC with ACE constraint

- **Status**: ✅
- **Reason**: ACE 제약 QC-LDPC 구성으로 trapping set 회피·girth 최대화—바이너리 코드설계 기법(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5541895
- **Type**: conference
- **Published**: 25-27 June
- **Authors**: Jilong Li, Na Di, Ming Yang +1
- **PDF**: https://ieeexplore.ieee.org/document/5541895
- **Abstract**: In this paper, LDPC code structure and decoder implementation is reviewed. The effect of graph connectivity on LDPC performance is analyzed. The metric of ACE (approximate cycle EMD) in code construction avoids small trapping sets by emphasizing the connectivity. A construction algorithm with ACE constraint is proposed which maximize the girth and stopping sets in a best effort way. Simulation results justify the efficiency of the algorithm.

## A quantization schema with negligible degradation for LDPC decoder

- **Status**: ✅
- **Reason**: LLR BP 디코더 양자화 스킴: 4~6비트 양자화 기준·정적 스텝 HW 구현—NAND LLR 양자화/HW에 직결(A/C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5541929
- **Type**: conference
- **Published**: 25-27 June
- **Authors**: Ming-Qiu Wang, Shu-Tao Xia, He-Guang Su +1
- **PDF**: https://ieeexplore.ieee.org/document/5541929
- **Abstract**: A quantization schema with negligible degradation for LDPC decoder is proposed. It's based on the decoding algorithm deduced from Belief Propagation algorithm on LLR. The schema offers a quantization criterion for iteration decoder, based on the study of channel outputs. The schema is adaptable for different channel status and quantization scale. Static step lengths for hardware implementation are selected according to the proposed criterion. The performance of the proposed schema is illustrated by both structured and random codes. In simulations for 6-bits quantization, performance loss is negligible. And the schema produces less than 0.01dB degradation for 5-bits quantization above 10−5 BER and about 0.1dB for 4-bits quantization. There is no error floor of BER even around 10−7. Simulations show the coverage plays an important role in quantization process. The results of static step lengths are as good as or even better than those of the variable step lengths.

## An improved IWBF decoding algorithm based on LDPC codes in the image transmission

- **Status**: ✅
- **Reason**: 개선된 가중비트플리핑(IWBF) 디코더—매 반복 다중비트 갱신으로 수렴속도/BER 향상, 부호 비의존 이식 가능 디코더(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5541758
- **Type**: conference
- **Published**: 25-27 June
- **Authors**: Wang Zhong-xun, Yu Xin-qiao, Wang Xing-cheng +1
- **PDF**: https://ieeexplore.ieee.org/document/5541758
- **Abstract**: In order to improve the performance and the decoding convergence speed of the improved weighted bit-flipping algorithm (IWBF), an algorithm based on the characteristics of parallel bit-flipping algorithm that updates multiple bits in each iteration is presented here. Also this algorithm is used in the image transmission. Simulation results show that: improved algorithm not only enables significant improvement in bit error performance, the decoding convergence speed has also been greatly improved, and the image transmission in communication can obtain high speed and high equality.

## A modified Min-Sum algorithm for low-density parity-check codes

- **Status**: ✅
- **Reason**: 수정 Min-Sum 디코더: 변수노드 메시지 보정으로 BP 근접, 추가 곱셈 1회로 저복잡도—이식 가능 디코더(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5541818
- **Type**: conference
- **Published**: 25-27 June
- **Authors**: Wei Han, Jianguo Huang, Fangfei Wu
- **PDF**: https://ieeexplore.ieee.org/document/5541818
- **Abstract**: A modified Min-Sum algorithm for low-density parity check codes is proposed in this paper. The inaccurate check node messages of the Min-Sum algorithm compared to the belief propagation (BP) algorithm are compensated by modified variable node messages, which is different from the normalized Min-Sum algorithm. The modified factor is obtained before decoding program and only one extra multiplication is needed in one cycle. So the increased complexity is fairly low. The simulation results show that the bit error rate (BER) and average number of iteration of the modified Min-Sum algorithm are very close to the BP algorithm, the modified algorithm can improve the BER performance compared to the Min-Sum algorithm while added complexity slightly.

## Decoding low-density parity-check codes with error-floor free over the AWGN channel

- **Status**: ✅
- **Reason**: BP+OSD 결합으로 error-floor 제거, stopping set 대응—이식 가능 디코더(C), error floor 관련
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5541918
- **Type**: conference
- **Published**: 25-27 June
- **Authors**: Li Yang, Martin Tomlinson, Marcel Ambroze
- **PDF**: https://ieeexplore.ieee.org/document/5541918
- **Abstract**: We propose a new soft decision decoding arrangement for LDPC codes over the AWGN channel with error-floor free. The iterative belief propagation decoder is used as the initial decoder with the iterative output conditioned prior to OSD decoding. Improved results are obtained to break the corresponding error floors caused by the stopping sets. The basis of the conditioning of the iterative output is explained with supporting analysis. Some practical examples of performance are presented for some well known LDPC codes and it is shown that the proposed decoder with OSD-i does not only produce better results than a stand-alone OSD-(i + 1) decoder with considerable reduction in decoder complexity, but also guarantees the error-floor free.

## A BP decoding algorithm based on nodes residual for LDPC codes

- **Status**: ✅
- **Reason**: VC-RBP 동적 스케줄링 BP(잔차 기반)로 빠른 수렴·저복잡도—이식 가능 디코더(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5541903
- **Type**: conference
- **Published**: 25-27 June
- **Authors**: Wang Zhong-xun, Wang Xing-cheng, Yu Xin-qiao +1
- **PDF**: https://ieeexplore.ieee.org/document/5541903
- **Abstract**: We researched BP decoding algorithm based on variable-to-check information residual for LDPC code (VC-RBP) in this paper. It is a dynamic scheduling belief propagation using residuals, and has some advantages, such as fast decoding, good performance, and low complexity. It is similar to residual belief propagation (RBP),but has some difference in computing the residual message. Simulation shows that it outperforms with only a maximum of ten iterations by about 0.28 dB compared with RBP at an BER of 10-4.

## A Resource-Efficient Decoder Architecture for LDPC Codes

- **Status**: ✅
- **Reason**: foldable horizontal process unit + check-matrix splitting reuse 아키텍처(D) — min-sum HW 자원효율 기법, 바이너리 LDPC 이식 가능
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:5630711
- **Type**: conference
- **Published**: 25-27 June
- **Authors**: Qinzhi Hong, Jun Wang, Weilong Lei
- **PDF**: https://ieeexplore.ieee.org/document/5630711
- **Abstract**: A novel architecture for the LDPC decoder with Chinese DTTB standard is presented in this paper. Two kinds of schemes to do the minimizing operations in the horizontal process of min-sum algorithm are compared, and then a foldable horizontal process unit is developed to support the splitting-matrix architecture, which is a reuse architecture based on check matrix splitting to increase the resource efficiency of the decoder. Theoretical analyses and implementation results are both provided to demonstrate that the decoder using this architecture has higher resource utilization efficiency than classical decoder. In addition, the new architecture can also be applied to other LDPC decoder, especially to LDPC codes with long code words.

## Voltage scaling and body biasing methodology for high performance hardwired LDPC

- **Status**: ✅
- **Reason**: LDPC 하드와이어 IP의 voltage scaling/body biasing 방법론 + 45nm 실측 → 이식 가능 HW(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:5510289
- **Type**: conference
- **Published**: 2-4 June 2
- **Authors**: Nabila Moubdi, Philippe Maurine, Robin Wilson +4
- **PDF**: https://ieeexplore.ieee.org/document/5510289
- **Abstract**: This paper aims at introducing a safe voltage scaling and body biasing methodology for Low-Density Parity Check (LDPC) hard-wired IP. The proposed methodology allows an efficient post-silicon tuning of the LDPC, and the performances can be adapted to High Speed mode, or Low Operating Power mode, or Low Standby Power mode requirements. Concrete 45 nm silicon results are introduced in this paper to demonstrate the added value of the methodology. More precisely, it is shown that running the High Performance mode leads to +24% on circuit maximum operating frequency. And the Low Standby Power mode results on x0.73 leakage minimization. The proposed adaptive LDPC encoder/decoder can remove some barriers to the adoption of long LDPC codes on portable devices.

## A 10.37 mm2 675 mW reconfigurable LDPC and Turbo encoder and decoder for 802.11n, 802.16e and 3GPP-LTE

- **Status**: ✅
- **Reason**: Turbo/LDPC 재구성 가능 ASIP 디코더 칩(데이터패스 재사용) — 이식 가능 HW 아키텍처(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:5560292
- **Type**: conference
- **Published**: 16-18 June
- **Authors**: F. Naessens, V. Derudder, H. Cappelle +12
- **PDF**: https://ieeexplore.ieee.org/document/5560292
- **Abstract**: This paper describes the implementation of a flexible Turbo and LDPC outer modem engine which is capable of supporting the WiFi(802.11n), WiMax(802.16e) and 3GPPLTE standard on the same hardware resources. The chip is implemented in a 65nm CMOS technology and occupies 10.37 mm2. The decoder flexibility is offered by means of an application-specific instruction-set processor (ASIP), with full datapath reuse between Turbo and LDPC decoding. The encoders are dedicated ASIC datapaths. The maximum clock speed can be set to 320 MHz allowing a decoder output rate for a single iteration in excess of 140 Mbps for Turbo and 640 Mbps for LDPC with a maximum power consumption of 675 mW. The architecture template has been extended to support other standards like the DVB-S2/T2 LDPC decoding as well.

## Binary dirty paper coding

- **Status**: ✅
- **Reason**: 바이너리 DPC용 수정 BP 알고리즘 제안(C), 디코더 기법 이식 가능성 검토 필요
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5722449
- **Type**: conference
- **Published**: 16-18 June
- **Authors**: Daniel Castanheira, Atilio Gameiro
- **PDF**: https://ieeexplore.ieee.org/document/5722449
- **Abstract**: This paper proposes a practical scheme for implementing binary dirty paper coding (DPC) using a low density generator matrix code (LDGM) concatenated with a high rate low density parity check (LDPC) code. We also propose a new algorithm, a modified version of the belief propagation algorithm (BP), for doing lossy source coding at the encoder, with linear complexity in the block length. In contrast to the superposition coding framework, where high order alphabet codes are used, we propose to implement binary DPC using only binary codes. Through application of approximate density evolution and linear programming we optimize the degree distribution of the proposed code. Simulation results show that our scheme achieves close to state-of-the-art performance with reduced complexity.

## A 4.84 mm2 847–955 Mb/s 397 mW dual-path fully-overlapped QC-LDPC decoder for the WiMAX system in 0.13 µm CMOS

- **Status**: ✅
- **Reason**: dual-path fully-overlapped QC-LDPC 디코더 VLSI 구현, 메모리 접근 감소 스케줄링 — 이식 가능 HW 아키텍처(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:5560295
- **Type**: conference
- **Published**: 16-18 June
- **Authors**: Bo Xiang, Xiaoyang Zeng
- **PDF**: https://ieeexplore.ieee.org/document/5560295
- **Abstract**: This paper presents a dual-path fully-overlapped QC-LDPC decoder for the WiMAX system. Each phase scans nonzero sub-matrices two by two in block row-wise order, and two phases are fully overlapped. It reduces memory accesses by 24.3-48.8%, and takes only 48-54 clock cycles per iteration. It is fabricated in SMIC 0.13 μm 1P8M CMOS process, which occupies 4.84 mm2, attains 847-955 Mb/s, and consumes 397 mW with power efficiency of 42 pJ per bit per iteration.

## An adaptable low density parity check (LDPC) engine for space based communication systems

- **Status**: ✅
- **Reason**: FPGA 적응형 LDPC 디코더 아키텍처, 부분재구성·병렬화 HW 기법 이식 가능(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:5546275
- **Type**: conference
- **Published**: 15-18 June
- **Authors**: Gregory M. Striemer, Ali Akoglu
- **PDF**: https://ieeexplore.ieee.org/document/5546275
- **Abstract**: Space communication systems are characterized by the severe limitations to the on-board computational power and the tight constraints of received signal strengths. Also, these systems observe degradation in signals caused by large propagation latencies, extreme distances traveled, as well as data corruption causing high bit-error rates. LDPC codes provide powerful error correction capability where signal power is very low, making them an ideal candidate for space based applications. A hardware architecture that is configurable to dynamic changes in channel conditions is a necessity for error resilient communication systems. In this study we demonstrate the feasibility of designing an FPGA based adaptable LDPC decoder architecture that also matches the throughput demand of current space based communications requirements. We design an LDPC engine that is adaptable to three code rates by taking advantage of the partial reconfiguration technology and parallel nature of the FPGA architecture. We evaluate the tradeoff between the level of parallelism to exploit on the FPGA when implementing LDPC codes and resource demand for each code rate under the constraints of delivering a partially reconfigurable and adaptable solution. Based on the implementation using a Xilinx Virtex-5 FPGA, our design handles context switching between the codes on board in 92μs.

## Novel code-construction of high rate (3, k) regular LDPC codes

- **Status**: ✅
- **Reason**: 신규 (3,k) regular 바이너리 LDPC 코드 구성법: rank 결손 없음, 4-cycle 제거, 저복잡 인코딩 — E 코드설계
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5716175
- **Type**: conference
- **Published**: 15-17 June
- **Authors**: Silvia Anggraeni, Varun Jeoti
- **PDF**: https://ieeexplore.ieee.org/document/5716175
- **Abstract**: This paper proposes a novel code-construction method for constructing (3, k) regular low density parity check (LDPC) codes. Other methods of designing regular LDPC codes suffer from rank-deficiency of H and high encoding complexity. The basic design of the proposed code-construction utilizes deterministic base matrices of information part and parity part in three stages of code-construction to achieve no rank-deficiency of H, no girth of 4-cycles, non-singular parity part (Hpar) and low encoding complexity. It is shown that the proposed (3, k) regular LDPC codes perform better in high code rate application. The result of (3, 42) regular code performs 0.97 dB from Shannon limit at BER 10-6 when the value of code rate R = 0.928, code length N = 14364 and encoding complexity of the order of O(1.0225 N).

## (5, k) regular LDPC codes using novel code-construction

- **Status**: ✅
- **Reason**: 위 구성법을 (5,k) regular 바이너리 LDPC로 일반화한 신규 코드설계 — E
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5716198
- **Type**: conference
- **Published**: 15-17 June
- **Authors**: Silvia Anggraeni, Varun Jeoti
- **PDF**: https://ieeexplore.ieee.org/document/5716198
- **Abstract**: This paper is a continuation of the work in [15] wherein a novel code-construction method was proposed for constructing (3, k) regular LDPC codes. In this paper, the (3, k) construction technique is generalized to construct (5, k) regular code. The basic design of the proposed code-construction utilizes deterministic base matrices for information part and parity part in three stages of code-construction to achieve no rank-deficiency of H, no girth of 4-cycles, non-singular parity part (Hpar) and low encoding complexity. A typical performance of proposed (5, k) regular LDPC codes has been shown.

## New low-density parity-check codes with large girth based on hypergraphs

- **Status**: ✅
- **Reason**: 하이퍼그래프 기반 large-girth 신규 QC-LDPC 구성 알고리즘, 최적 girth·최소거리 — 바이너리 코드설계 이식(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5513639
- **Type**: conference
- **Published**: 13-18 June
- **Authors**: Irina E. Bocharova, Florian Hug, Rolf Johannesson +2
- **PDF**: https://ieeexplore.ieee.org/document/5513639
- **Abstract**: The relation between low-density parity-check (LDPC) codes and hypergraphs supports searching for powerful LDPC codes based on hypergraphs. On the other hand, coding theory methods can be used in searching for hypergraphs with large girth. Moreover, compact representations of hypergraphs based on convolutional codes can be found. Algorithms for iteratively constructing LDPC codes with large girth and for determining their minimum distance are introduced. New quasi-cyclic (QC) LDPC codes are presented, some having both optimal girth and optimal minimum distance.

## Decoding of LDPC convolutional codes with rational parity-check matrices from a new graphical perspective

- **Status**: ✅
- **Reason**: LDPC-CC 유리 패리티검사 행렬을 4-cycle 없는 등가 Tanner 그래프로 변환+BP 스케줄링 — 바이너리 LDPC 코드설계/디코더 이식 가능(E/C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5513631
- **Type**: conference
- **Published**: 13-18 June
- **Authors**: Jian-Jia Weng, Chih-Chieh Lai, Chung-Hsuan Wang
- **PDF**: https://ieeexplore.ieee.org/document/5513631
- **Abstract**: Previous studies on low-density parity-check convolutional codes (LDPC-CC) reveal that LDPC-CC with rational parity-check matrices (RPCM) suffer from the unaffordable decoding latency/complexity due to the infinite memory order and the poor bit-error-rate performance due to the existence of length-4 cycles in the Tanner graph. However, in this paper, we show that every LDPC-CC with RPCM can be associated with an equivalent Tanner graph which can avoid the infinite memory order and undesired short length cycles but still implements the same constraints specified by the RPCM. Together with the iterative decoding based on belief propagation with proper scheduling, simulation results indicate that LDPC-CC with RPCM can also provide satisfactory decoding performance.

## New families of LDPC block codes formed by terminating irregular protograph-based LDPC convolutional codes

- **Status**: ✅
- **Reason**: irregular protograph LDPC-CC 종단으로 새 LDPC 블록부호 족 구성, 바이너리 코드설계 기법 이식 가능(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5513633
- **Type**: conference
- **Published**: 13-18 June
- **Authors**: David G. M. Mitchell, Michael Lentmaier, Daniel J. Costello
- **PDF**: https://ieeexplore.ieee.org/document/5513633
- **Abstract**: In this paper, we present a method of constructing new families of LDPC block code ensembles formed by terminating irregular protograph-based LDPC convolutional codes. Using the accumulate-repeat-by-4-jagged-accumulate (AR4JA) protograph as an example, a density evolution analysis for the binary erasure channel shows that this flexible design technique gives rise to a large selection of LDPC block code ensembles with varying code rates and thresholds close to capacity. Further, by means of an asymptotic weight enumerator analysis, we show that all the ensembles in this family also have minimum distance that grows linearly with block length, i.e., they are asymptotically good.

## A new construction of UEP QC-LDPC codes

- **Status**: ✅
- **Reason**: 새 UEP QC-LDPC 구성(girth>=8, min distance 상한 확대) — 바이너리 QC-LDPC 신규 코드설계(E) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5513610
- **Type**: conference
- **Published**: 13-18 June
- **Authors**: Chi-Jen Wu, Chung-Hsuan Wang, Chi-chao Chao
- **PDF**: https://ieeexplore.ieee.org/document/5513610
- **Abstract**: In this paper, a new construction of quasi-cyclic low-density parity-check (QC-LDPC) codes for unequal error protection (UEP) is proposed. We first give a new class of UEP block codes. QC-LDPC codes with binomial-term parity-check matrices which can avoid girths less than 8 and achieve an enlarged upper bound on the minimum distance are also introduced. An effective UEP scheme based on the proposed UEP block codes and QC-LDPC codes which can provide flexible choice of protection levels is then presented. Simulation results show that the new QC-LDPC codes can achieve good performance and low error floors. The bits with different designed protection levels can indeed have unequal bit-error-rate performance.

## LP decoding of regular LDPC codes in memoryless channels

- **Status**: ✅
- **Reason**: 정규 바이너리 LDPC의 LP 디코딩 오류 bound/threshold 이론이나 LP 디코더는 바이너리 LDPC C에 이식 가능, 애매하면 in
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5513612
- **Type**: conference
- **Published**: 13-18 June
- **Authors**: Nissim Halabi, Guy Even
- **PDF**: https://ieeexplore.ieee.org/document/5513612
- **Abstract**: We study error bounds for linear programming decoding of regular LDPC codes. For memoryless binary-input output-symmetric channels, we prove bounds on the word error probability that are inverse doubly-exponential in the girth of the factor graph. For memoryless binary-input AWGN channels, we derive lower bounds on the thresholds for regular LDPC codes under LP decoding. Specifically, we prove a lower bound of σ = 0.735 on the threshold of (3, 6)-regular LDPC codes with logarithmic girth.

## Circulant arrays: Rank analysis and construction of quasi-cyclic LDPC codes

- **Status**: ✅
- **Reason**: 유한체 cyclic subgroup 기반 신규 바이너리 QC-LDPC 구성+rank 분석, PEG 대비 우수 SPA — 코드설계 이식(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5513640
- **Type**: conference
- **Published**: 13-18 June
- **Authors**: Li Zhang, Shu Lin, Khaled Abdel-Ghaffar +1
- **PDF**: https://ieeexplore.ieee.org/document/5513640
- **Abstract**: This paper consists of three parts. The first part presents a large class of new binary quasi-cyclic (QC)-LDPC codes with girth of at least 6 whose parity-check matrices are constructed based on cyclic subgroups of finite fields. Experimental results show that the codes constructed perform well over the binary-input AWGN channel with iterative decoding using the sum-product algorithm (SPA) and they outperform the corresponding pseudo-random QC-LDPC codes constructed with the PEG-algorithm. The second part analyzes the ranks of the parity-check matrices of codes constructed based on finite fields with characteristic of 2 and gives combinatorial expressions for these ranks. The third part identifies a subclass of constructed QC-LDPC codes that have large minimum distances. Decoding of codes in this subclass with the SPA converges very fast.

## Lowering the error floor of LDPC codes using cyclic liftings

- **Status**: ✅
- **Reason**: cyclic lifting으로 trapping set/short cycle 제거하여 error floor 저감 — 바이너리 LDPC 코드설계(E), 임의 코드/채널/디코더에 보편 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5513605
- **Type**: conference
- **Published**: 13-18 June
- **Authors**: Reza Asvadi, Amir H. Banihashemi, Mahmoud Ahmadian-Attari
- **PDF**: https://ieeexplore.ieee.org/document/5513605
- **Abstract**: Cyclic liftings are proposed to lower the error floor of low-density parity-check (LDPC) codes. The liftings are designed to eliminate dominant trapping sets of the base code by removing the short cycles which form the trapping sets. We derive a necessary and sufficient condition for the cyclic permutations assigned to the edges of a cycle c of length ℓ(c) in the base graph such that the inverse image of c in the lifted graph consists of only cycles of length strictly larger than ℓ(c). The proposed method is universal in the sense that it can be applied to any LDPC code over any channel and for any iterative decoding algorithm. It also preserves important properties of the base code such as degree distributions. The proposed method is applied to both structured and random codes over the binary symmetric channel (BSC). The error floor improves consistently by increasing the lifting degree, and the results show significant improvements in the error floor compared to the base code, a random code of the same degree distribution and block length, and a random lifting of the same degree. Similar improvements are also observed when the codes designed for the BSC are applied to the additive white Gaussian noise (AWGN) channel.

## Channels with both random errors and burst erasures: Capacities, LDPC code thresholds, and code performances

- **Status**: ✅
- **Reason**: BP/density evolution 기반 LDPC 코드 설계로 random error+erasure 동시 대응 — 바이너리 LDPC 코드설계(E) 기여, 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5513593
- **Type**: conference
- **Published**: 13-18 June
- **Authors**: Kan Li, Aleksandar Kavčić, Raman Venkataramani +1
- **PDF**: https://ieeexplore.ieee.org/document/5513593
- **Abstract**: We derive the capacities of a class of channels, either memoryless or indecomposable finite-state, that also suffer from bursts of erasures. For such channels, we analyze the performances of low-density parity-check (LDPC) codes and code ensembles under belief propagation (BP) decoding, using density evolution (DE) techniques. Although known LDPC codes perform well in non-erasure-affected channels, their performances are far from the capacities when both random errors and erasures are present. We show that enhancing the codes' erasure handling using published methods beats, in some instances, the BP thresholds. However, to achieve capacity, codes must be constructed to tackle both effects simultaneously.

## Error floor analysis in LDGM codes

- **Status**: ✅
- **Reason**: LDGM error floor 예측 DDE 분석 — 바이너리 LDPC계열 error floor 분석 기법(E), 애매하나 in으로 살림(Phase 3 재검토)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5513607
- **Type**: conference
- **Published**: 13-18 June
- **Authors**: Kejing Liu, Javier García-Frías
- **PDF**: https://ieeexplore.ieee.org/document/5513607
- **Abstract**: Based on discrete density evolution (DDE), we develop closed form expressions to predict the error floor of LDGM codes. The first, rougher, approximation is obtained by assuming perfect message passing between systematic and parity bit nodes in DDE. The second, finer, expression leads to a more involved formulation. While the rougher approximation matches well to simulation results and DDE analysis for high signal to noise ratio (additive white Gaussian noise, AWGN, channel) or low crossover probability (binary symmetric channel, BSC), the finer approximation shows a good match for a wider range in the channel quality.

## Tree-structure expectation propagation for decoding LDPC codes over binary erasure channels

- **Status**: ✅
- **Reason**: BEC용 tree-structure expectation propagation 디코더 — BP가 막힐 때 추가 제약으로 복호, 부호 비의존 바이너리 LDPC 디코더 개선(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5513636
- **Type**: conference
- **Published**: 13-18 June
- **Authors**: Pablo M. Olmos, Juan José Murillo-Fuentes, Fernando Pérez-Cruz
- **PDF**: https://ieeexplore.ieee.org/document/5513636
- **Abstract**: Expectation Propagation is a generalization to Belief Propagation (BP) in two ways. First, it can be used with any exponential family distribution over the cliques in the graph. Second, it can impose additional constraints on the marginal distributions. We use this second property to impose pair-wise marginal distribution constraints in some check nodes of the LDPC Tanner graph. These additional constraints allow decoding the received codeword when the BP decoder gets stuck. In this paper, we first present the new decoding algorithm, whose complexity is identical to the BP decoder, and we then prove that it is able to decode codewords with a larger fraction of erasures, as the block size tends to infinity. The proposed algorithm can be also understood as a simplification of the Maxwell decoder, but without its computational complexity. We also illustrate that the new algorithm outperforms the BP decoder for finite block-size codes.

## On the joint decoding of LDPC codes and finite-state channels via linear programming

- **Status**: ✅
- **Reason**: 바이너리 LDPC의 LP joint-decoding을 FSC로 확장하는 디코더 기법, BP 디코더 개선(C)으로 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5513614
- **Type**: conference
- **Published**: 13-18 June
- **Authors**: Byung-Hak Kim, Henry D. Pfister
- **PDF**: https://ieeexplore.ieee.org/document/5513614
- **Abstract**: In this paper, the linear programming (LP) decoder for binary linear codes, introduced by Feldman, et al. is extended to joint-decoding of binary-input finite-state channels. In particular, we provide a rigorous definition of LP joint-decoding pseudo-codewords (JD-PCWs) that enables evaluation of the pairwise error probability between codewords and JD-PCWs. This leads naturally to a provable upper bound on decoder failure probability. If the channel is a finite-state intersymbol interference channel, then the LP joint decoder also has the maximum-likelihood (ML) certificate property and all integer valued solutions are codewords. In this case, the performance loss relative to ML decoding can be explained completely by fractional valued JD-PCWs.

## LDPC codes with fixed initialization decoding over binary symmetric channel

- **Status**: ✅
- **Reason**: BSC용 correctable error set 기반 일반화 sum-product 디코딩(고정 초기화) — 바이너리 LDPC 디코더 개선(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5513630
- **Type**: conference
- **Published**: 13-18 June
- **Authors**: Manabu Hagiwara, Marc P.C. Fossorier, Hideki Imai
- **PDF**: https://ieeexplore.ieee.org/document/5513630
- **Abstract**: In this paper, we introduce the concept of correctable error set for the BSC, which allows to generalize sum-product decoding for this channel. As a result, better error performance or faster convergence can be achieved. Furthermore, the correctable error set allows to evaluate the error performance of generalized sum-product decoding with a given iteration number for the BSC.

## A practical message-wise unequal error protection coding scheme

- **Status**: ✅
- **Reason**: all-odd degree check node LDPC + 미충족 체크노드 추적 기반 디코더 검출 기법 — 부호 설계/디코더 변형으로 이식 가능(C/E), 유한길이 분석 포함
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5513487
- **Type**: conference
- **Published**: 13-18 June
- **Authors**: Chen Gong, Guosen Yue, Xiaodong Wang
- **PDF**: https://ieeexplore.ieee.org/document/5513487
- **Abstract**: We propose a practical message-wise unequal error protection (UEP) scheme using low-density parity-check (LDPC) codes, where one or more special messages are more protected than other ordinary messages, which performs codeword flipping to separate the codewords of special and ordinary messages. To better distinguish the original and flipped codewords, the LDPC codes with all-odd degree check nodes are employed. The decoder performs message type detection and codeword flipping detection by tracking the number of unsatisfied check nodes in iterative decoding. We provide both finite-length and asymptotic performance analysis for the proposed coding scheme. Simulation results are provided to show that the proposed practical message-wise UEP schemes offer capacity-approaching protections to both types of messages as if only one type of message is transmitted.

## Multitree decoding and multitree-aided LDPC decoding

- **Status**: ✅
- **Reason**: multitree 탐색으로 비트 clamp 후 sum-product 재시도하는 LDPC 디코딩 기법 — 이식 가능 디코더(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5513629
- **Type**: conference
- **Published**: 13-18 June
- **Authors**: Maja Ostojic, Hans-Andrea Loeliger
- **PDF**: https://ieeexplore.ieee.org/document/5513629
- **Abstract**: New decoding algorithms for linear codes are proposed. The first part of the paper considers decoding general binary linear codes by searching multiple trees, which is shown to achieve near maximum-likelihood performance for short block lengths. The second part of the paper considers decoding low-density parity check (ldpc) codes by means of repeated decoding attempts by standard sum-product message passing. Each decoding attempt starts from modified channel output, where some of the bits are clamped to a fixed value. The values of the fixed bits are obtained from multitree search.

## Exhaustive search for small fully absorbing sets and the corresponding low error-floor decoder

- **Status**: ✅
- **Reason**: fully absorbing set 완전탐색 + 신규 post-processing 디코더로 error floor 저감 — 바이너리 LDPC 디코더(C)/코드설계(E) 기여
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5513611
- **Type**: conference
- **Published**: 13-18 June
- **Authors**: Gyu Bum Kyung, Chih-Chun Wang
- **PDF**: https://ieeexplore.ieee.org/document/5513611
- **Abstract**: This work provides an exhaustive search algorithm for finding small fully absorbing sets (FASs) of arbitrary low-density parity-check (LDPC) codes. In particular, given any LDPC code, the problem of finding all FASs of size less than t is formulated as an integer programming problem, for which a new branch-&-bound algorithm is devised. New node selection and the tree-trimming mechanisms are designed to further enhance the efficiency of the algorithm. The proposed algorithm is capable of finding all FASs of size ≤ 11 with no larger than 2 induced odd-degree check nodes for LDPC codes of length ≤ 1000. The resulting exhaustive list of small FASs is then used to devise a new post-processing decoder. Numerical results show that by taking advantage of the exhaustive list of small FASs, the proposed decoder significantly lowers the error floor for codes of practical lengths and outperforms the state-of-the-art low-error-floor decoders.

## Channel decoding with a Bayesian equalizer

- **Status**: ✅
- **Reason**: CSI 추정 불확실성을 반영한 Bayesian equalizer로 LDPC 디코더 APP/LLR 입력 개선 — NAND read의 LLR 추정 불확실성에 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5513348
- **Type**: conference
- **Published**: 13-18 June
- **Authors**: Luis Salamanca, Juan José Murillo-Fuentes, Fernando Pérez-Cruz
- **PDF**: https://ieeexplore.ieee.org/document/5513348
- **Abstract**: Low-density parity-check (LPDC) decoders assume the channel estate information (CSI) is known and they have the true a posteriori probability (APP) for each transmitted bit. But in most cases of interest, the CSI needs to be estimated with the help of a short training sequence and the LDPC decoder has to decode the received word using faulty APP estimates. In this paper, we study the uncertainty in the CSI estimate and how it affects the bit error rate (BER) output by the LDPC decoder. To improve these APP estimates, we propose a Bayesian equalizer that takes into consideration not only the uncertainty due to the noise in the channel, but also the uncertainty in the CSI estimate, reducing the BER after the LDPC decoder.

## Multilevel decoders surpassing belief propagation on the binary symmetric channel

- **Status**: ✅
- **Reason**: BSC용 새 양자화 메시지패싱 디코더(trapping set 기반 3-bit 규칙), BP/min-sum 능가 — 이식 가능 디코더(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5513620
- **Type**: conference
- **Published**: 13-18 June
- **Authors**: Shiva Kumar Planjery, David Declercq, Shashi Kiran Chilappagari +1
- **PDF**: https://ieeexplore.ieee.org/document/5513620
- **Abstract**: In this paper, we propose a new class of quantized message-passing decoders for LDPC codes over the BSC. The messages take values (or levels) from a finite set. The update rules do not mimic belief propagation but instead are derived using the knowledge of trapping sets. We show that the update rules can be derived to correct certain error patterns that are uncorrectable by algorithms such as BP and min-sum. In some cases even with a small message set, these decoders can guarantee correction of a higher number of errors than BP and min-sum. We provide particularly good 3-bit decoders for 3-left-regular LDPC codes. They significantly outperform the BP and min-sum decoders, but more importantly, they achieve this at only a fraction of the complexity of the BP and min-sum decoders.

## Worst configurations (instantons) for Compressed Sensing over reals: A channel coding approach

- **Status**: ✅
- **Reason**: LDPC error-floor의 가장 가능성 높은 오류패턴(instanton) 탐색 알고리즘을 CS로 일반화 — instanton/error-floor 분석 기법은 NAND LDPC error floor 분석에 이식 가능(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5513360
- **Type**: conference
- **Published**: 13-18 June
- **Authors**: Shashi Kiran Chilappagari, Michael Chertkov, Bane Vasic
- **PDF**: https://ieeexplore.ieee.org/document/5513360
- **Abstract**: We consider the Linear Programming (LP) solution of the Compressed Sensing (CS) problem over reals, also known as the Basis Pursuit (BasP) algorithm. The BasP allows interpretation as a channel-coding problem, and it guarantees error-free reconstruction with a properly chosen measurement matrix and sufficiently sparse error vectors. In this manuscript, we examine how the BasP performs on a given measurement matrix and develop an algorithm to discover the sparsest vectors for which the BasP fails. The resulting algorithm is a generalization of our previous results on finding the most probable error-patterns degrading performance of a finite size Low-Density Parity-Check (LDPC) code in the error-floor regime. The BasP fails when its output is different from the actual error-pattern. We design a CS-Instanton Search Algorithm (ISA) generating a sparse vector, called a CS-instanton, such that the BasP fails on the CS-instanton, while the BasP recovery is successful for any modification of the CS-instanton replacing a nonzero element by zero. We also prove that, given a sufficiently dense random input for the error-vector, the CS-ISA converges to an instanton in a small finite number of steps. The performance of the CS-ISA is illustrated on a randomly generated 120 × 512 matrix. For this example, the CS-ISA outputs the shortest instanton (error vector) pattern of length 11.

## Improved adaptive belief propagation decoding using edge-local complementation

- **Status**: ✅
- **Reason**: SPA 반복 사이 edge-local complementation 기반 adaptive BP 디코더 개선+damping — 이식 가능 디코더(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5513625
- **Type**: conference
- **Published**: 13-18 June
- **Authors**: Joakim Grahl Knudsen, Constanza Riera, Lars Eirik Danielsen +2
- **PDF**: https://ieeexplore.ieee.org/document/5513625
- **Abstract**: This work is an extension of our previous work on an iterative soft-decision decoder for high-density parity-check codes, using a graph-local operation known as edge-local complementation (ELC). Inferred least reliable codeword positions are targeted by an ELC stage in between sum-product algorithm iterations. A gain is shown over related iterative decoding algorithms - mainly due to an improved heuristic to determine optimum ELC locations in the Tanner graph - both in error-rate performance, as well as complexity in terms of a significant reduction in the required number of ELC operations. We also present a novel damping operation, generalized to the graph-local setting where extrinsic information remains on edges not affected by ELC.
