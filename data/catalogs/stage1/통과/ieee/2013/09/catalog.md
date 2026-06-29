# IEEE Xplore — 2013-09 (1차선별 통과)


## Several Explicit Constructions for (3,L) QC-LDPC Codes with Girth at Least Eight

- **Status**: ✅
- **Reason**: girth≥8 바이너리 (3,L) QC-LDPC 명시적 구성 — E(코드설계) 해당
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6560010
- **Type**: journal
- **Published**: September 
- **Authors**: Guohua Zhang, Rong Sun, Xinmei Wang
- **PDF**: https://ieeexplore.ieee.org/document/6560010
- **Abstract**: Some explicit constructions for exponent matrices which correspond to Tanner graphs with girth at least eight are proposed. From these results, for any row weight of L>3, (3,L) quasi-cyclic LDPC codes with girth at least eight are constructed for any circulant permutation matrix (CPM) size P>L(L+mod(L,2))/2.

## Controlling the Error Floor in LDPC Decoding

- **Status**: ✅
- **Reason**: absorbing set 동적 메시지·양자화 기반 LDPC 에러플로어 제어 — C/E 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6567866
- **Type**: journal
- **Published**: September 
- **Authors**: Shuai Zhang, Christian Schlegel
- **PDF**: https://ieeexplore.ieee.org/document/6567866
- **Abstract**: The error floor of LDPC is revisited as an effect of dynamic message behavior in the so-called absorbing sets of the code. It is shown that if the signal growth in the absorbing sets is properly balanced by the growth of set-external messages, the error floor can be lowered to essentially arbitrarily low levels. Importance sampling techniques are discussed and used to verify the analysis, as well as to discuss the impact of iterations and message quantization on the code performance in the ultra-low BER (error floor) regime.

## Enabling NAND Flash Memory Use Soft-Decision Error Correction Codes at Minimal Read Latency Overhead

- **Status**: ✅
- **Reason**: NAND 플래시 소프트디시전 LDPC ECC의 read latency 저감 설계 — A 카테고리 직접 해당
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6529180
- **Type**: journal
- **Published**: Sept. 2013
- **Authors**: Guiqiang Dong, Ningde Xie, Tong Zhang
- **PDF**: https://ieeexplore.ieee.org/document/6529180
- **Abstract**: With the aggressive technology scaling and use of multi-bit per cell storage, NAND flash memory is subject to continuous degradation of raw storage reliability and demands more and more powerful error correction codes (ECC). This inevitable trend makes conventional BCH code increasingly inadequate, and iterative coding solutions such as LDPC codes become very natural alternative options. However, these powerful coding solutions demand soft-decision memory sensing, which results in longer on-chip memory sensing latency and memory-to-controller data transfer latency. Leveraging well-established lossless data compression theories, this paper presents several simple design techniques that can reduce such latency penalty caused by soft-decision ECCs. Their effectiveness have been well demonstrated through extensive simulations, and the results suggest that the latency can be reduced by up to 85.3%.

## The Approximate Maximum-Likelihood Certificate

- **Status**: ✅
- **Reason**: BP/min-sum + LP 디코딩 기반 신뢰도 인증(AMLC), 부호 비의존 메시지패싱 후처리로 바이너리 LDPC 디코더에 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6516912
- **Type**: journal
- **Published**: Sept. 2013
- **Authors**: Idan Goldenberg, David Burshtein
- **PDF**: https://ieeexplore.ieee.org/document/6516912
- **Abstract**: The confidence in the reliability of a codeword output by some (not necessarily optimal) decoding algorithm is discussed. A new property which relies on the linear programming (LP) decoder, the approximate maximum-likelihood certificate (AMLC), is introduced to address this issue as follows. First, the channel output vector is decoded by some symmetric decoder D, e.g., belief propagation or min-sum algorithm decoding. Second, the channel output vector is decoded by LP decoding. Third, if the decoding result of D is a codeword, its LP value is compared to the LP value of the LP decoding result (the latter need not be a codeword). If these two values are close, the AMLC holds. Using upper bounding techniques, we show that the conditional frame error probability given that the AMLC holds, is with some degree of confidence below a threshold. In channels with low noise, this threshold is orders of magnitude lower than the simulated frame error rate, and our bound holds with a very high degree of confidence. This is in stark contrast with standard Monte Carlo simulation, which would require excessively long runs to demonstrate like performance. When the AMLC holds, our approach thus provides the decoder with extra error detection capability, which is especially important in applications requiring high data integrity.

## Graphical Characterizations of Linear Programming Pseudocodewords for Cycle Codes

- **Status**: ✅
- **Reason**: LP 의사부호어/cycle code 그래프 특성화 — 메시지패싱 디코더 성능 예측·코드설계(error floor)에 이식 가능(C/E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6557539
- **Type**: journal
- **Published**: Sept. 2013
- **Authors**: Nathan Axvig, Deanna Dreher
- **PDF**: https://ieeexplore.ieee.org/document/6557539
- **Abstract**: The performance of linear programming decoding is determined by the set of nonzero linear programming pseudocodewords. The minimum pseudoweight of this set of linear programming pseudocodewords is also generally accepted as a good predictor of the performance of iterative message-passing decoding. Since the linear programming decoder has a natural description based on the Tanner graph of a code, linear programming pseudocodewords can be analyzed from a graphical viewpoint. In this paper, two graphical characterizations of linear programming pseudocodewords of cycle codes are provided: one for the entire set of linear programming pseudocodewords, and one for the set of minimal linear programming pseudocodewords. The first of these characterizations is used to determine a formula for the minimum degree of a graph cover necessary to realize a linear programming pseudocodeword of a cycle code, and the second is used to prove a result concerning the asymptotic performance of the linear programming decoder when considering transmission over either the additive white Gaussian noise channel or the binary symmetric channel. Finally, a discussion contrasting these two characterizations both with each other and with Horn's characterization of bad pseudocycles is provided.

## Design of masking matrix for QC-LDPC codes

- **Status**: ✅
- **Reason**: QC-LDPC masking matrix 신규 구조 + 프로토그래프 GA 알고리즘으로 0.2dB 이득 (E, 바이너리 코드설계 이식 가능)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6691248
- **Type**: conference
- **Published**: 9-13 Sept.
- **Authors**: Yang Liu, Ying Li
- **PDF**: https://ieeexplore.ieee.org/document/6691248
- **Abstract**: The masking matrix plays an important role in constructing new classes of regular and irregular quasi-cyclic low density parity check (QC-LDPC) codes. By coupling two identical graphs in a special way, we present a new structure of the masking matrix, whose Tanner graph can be seen as a protograph. From this perspective, we propose a Gaussian Approximation algorithm for protograph-based LDPC codes to analyze the asymptotic performance of this class of codes. It is shown that, although the proposed structure of the masking matrix has almost the same convergence threshold as the conventional one produced randomly by progressive edge growth (PEG) algorithm, the former converges faster than the latter. Simulation results illustrate that the QC-LDPC code constructed by the proposed structure of the masking matrix has about 0.2dB coding gains compared with the conventional one.

## A finite length performance analysis of LDPC codes constructed by connecting spatially coupled chains

- **Status**: ✅
- **Reason**: SC-LDPC 체인 연결 구성의 유한길이 성능 분석, 연결체인이 단일체인보다 우수 (E, 바이너리 SC-LDPC 구성 이식 가능)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6691239
- **Type**: conference
- **Published**: 9-13 Sept.
- **Authors**: Pablo M. Olmos, David G. M. Mitchell, Dmitri Truhachev +1
- **PDF**: https://ieeexplore.ieee.org/document/6691239
- **Abstract**: The finite length performance of codes on graphs constructed by connecting spatially coupled low-density parity-check (SC-LDPC) code chains is analyzed. Successive (peeling) decoding is considered for the binary erasure channel (BEC). The evolution of the undecoded portion of the bipartite graph remaining after each iteration is analyzed as a dynamical system. It is shown that, in addition to superior iterative decoding thresholds, connected chain ensembles have better performance than single chain ensembles of the same rate and length.

## Hardware implementations of Gaussian elimination over GF(2) for channel decoding algorithms

- **Status**: ✅
- **Reason**: GF(2) 가우스소거 FPGA HW 아키텍처, 신규 채널디코딩 알고리즘용 저자원/고처리량 구현. 이식 가능 HW(D)로 NAND LDPC 디코더에 활용 가능
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:6757620
- **Type**: conference
- **Published**: 9-12 Sept.
- **Authors**: Stefan Scholl, Christopher Stumm, Norbert Wehn
- **PDF**: https://ieeexplore.ieee.org/document/6757620
- **Abstract**: In this paper, we investigate hardware implementations for Gaussian elimination of binary matrices. Gaussian elimination over GF(2) is a key operation used in several new channel decoding algorithms, that can provide large improvement of frame error rate over currently used algorithms. We first apply state-of-the-art architectures for binary Gaussian elimination to decoding algorithms. Then, we present a new hardware architecture, that has considerably less resource utilization and a higher throughput than state-of-the-art solutions. The designs have been implemented and compared on a Virtex 7 FPGA.

## The Systematic Form of a Class of Regular Structured LDPC Codes

- **Status**: ✅
- **Reason**: circulant permutation 기반 QC-LDPC(dv=2)의 systematic form 구성·Tanner 그래프상 직접 인코딩 — 바이너리 QC-LDPC 코드설계(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6631695
- **Type**: conference
- **Published**: 9-11 Sept.
- **Authors**: Xiuni Wang, Dongqing Xie
- **PDF**: https://ieeexplore.ieee.org/document/6631695
- **Abstract**: In this paper, we propose a systematic form about a class of regular structured LDPC codes. This class of LDPC codes is quasi-cyclic code with variable node degree dv = 2 on the Tanner graph. The defining parity-check matrices are composed of circulant permutation matrices. By columns permutation, we can locate the information bits and parity check bits easily. Furthermore, the values of associated parity check bits can be calculated directly on the Tanner graph.

## Automatic implementation of low-complexity QC-LDPC encoders

- **Status**: ✅
- **Reason**: 6662182과 동일 내용(low-complexity QC-LDPC 인코더 HW 자동구현) — 이식 가능 HW 아키텍처(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:6662186
- **Type**: conference
- **Published**: 9-11 Sept.
- **Authors**: Georgios Tzimpragos, Christoforos Kachris, Dimitrios Soudris +1
- **PDF**: https://ieeexplore.ieee.org/document/6662186
- **Abstract**: Low Density Parity Check (LDPC) codes are a special class of error correction codes widely used in communication and disk storage systems, due to their Shannon limit approaching performance and their favorable structure. In this paper an Electronic Design Automation tool for the generation of synthesizable VHDL codes, implementing low-complexity Quasi-Cyclic LDPC (QC-LDPC) encoders is presented. The designs generated by the developed tool has been proved to exhibit hardware savings and greater throughput as compared to other published QC-LDPC encoder implementations and are based on a design methodology, where the signals in many cases are hard-wired in the LUTs and the cyclic-shifters and block-memories conventionally used, are eliminated. The presented tool also offers the advantage of providing designers with the ability to study the trade-offs in maximum clock frequency, throughput, resources utilization and power consumption, between architectures with different design parameters, enabling rapid Design Space Exploration.

## Automatic implementation of low-complexity QC-LDPC encoders

- **Status**: ✅
- **Reason**: low-complexity QC-LDPC 인코더 VHDL 자동생성, LUT 하드와이어·시프터 제거로 HW 절감 — 이식 가능 HW 아키텍처(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:6662182
- **Type**: conference
- **Published**: 9-11 Sept.
- **Authors**: Georgios Tzimpragos, Christoforos Kachris, Dimitrios Soudris +1
- **PDF**: https://ieeexplore.ieee.org/document/6662182
- **Abstract**: Low Density Parity Check (LDPC) codes are a special class of error correction codes widely used in communication and disk storage systems, due to their Shannon limit approaching performance and their favorable structure. In this paper an Electronic Design Automation tool for the generation of synthesizable VHDL codes, implementing low-complexity Quasi-Cyclic LDPC (QC-LDPC) encoders is presented. The designs generated by the developed tool has been proved to exhibit hardware savings and greater throughput as compared to other published QC-LDPC encoder implementations and are based on a design methodology, where the signals in many cases are hard-wired in the LUTs and the cyclic-shifters and block-memories conventionally used, are eliminated. The presented tool also offers the advantage of providing designers with the ability to study the trade-offs in maximum clock frequency, throughput, resources utilization and power consumption, between architectures with different design parameters, enabling rapid Design Space Exploration.

## Advances in error correction coding for high-speed optical transmission

- **Status**: ✅
- **Reason**: QC/convolutional/staircase/spatially-coupled LDPC를 QC-LDPC 설계에서 유도, irregular QC-LDPC 설계로 coding gain — 바이너리 코드설계(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6656407
- **Type**: conference
- **Published**: 8-12 Sept.
- **Authors**: Ivan B. Djordjevic
- **PDF**: https://ieeexplore.ieee.org/document/6656407
- **Abstract**: Several attractive classes of LDPC codes including quasi-cyclic (QC), convolutional, staircase, and spatially-coupled codes are described. We show that these classes of LDPC codes can be derived from QC-LDPC code design. We demonstrate that record coding gains can be obtained from properly designed irregular QC-LDPC codes.

## Informed dynamic schedules for LDPC decoding using belief propagation

- **Status**: ✅
- **Reason**: T-RBP/S-RBP: IDS 기반 BP 스케줄링 신규 디코더, 바이너리 LDPC BP에 직접 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6666154
- **Type**: conference
- **Published**: 8-11 Sept.
- **Authors**: Huang-Chang Lee, Yeong-Luh Ueng
- **PDF**: https://ieeexplore.ieee.org/document/6666154
- **Abstract**: After the publication of the residual belief-propagation (RBP) algorithm, many low-density parity-check (LDPC) decoders using informed dynamic scheduling (IDS) have been investigated. In this paper, we propose the twofold-RBP (T-RBP) decoder that combines two residuals. Using T-RBP, significant improvement can be achieved in both convergence speed and convergence error-rate performance. In addition to T-RBP, the simplified-RBP (S-RBP) decoder is also proposed in order to reduce the complexity. Instead of comparing all the residuals of all edges in the code graph, as with previous IDS decoders, S-RBP only compares the residuals of the edges connected to a single check node, thus dramatically reduces the complexity without any significant degradation in performance. The proposed T-RBP and S-RBP can improve not only the performance of dedicated codes, but also that of punctured codes, especially the convergence speed. The improvement can make punctured LDPC codes more practical and becoming a competitive candidate for the rate compatible applications.

## Application specific hardware architecture for high-throughput short-length LDPC decoders

- **Status**: ✅
- **Reason**: short-length LDPC 디코더 FPGA HW 아키텍처(BP/min-sum, arctanh 근사, 병렬화) — 이식 가능 HW 아키텍처(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:6646126
- **Type**: conference
- **Published**: 5-7 Sept. 
- **Authors**: Bogdan Belean, Sergiu Nedevschi, Monica Borda
- **PDF**: https://ieeexplore.ieee.org/document/6646126
- **Abstract**: LDPC codes have been intensively used in various wireless communication applications, due to their increased BER performance. The present paper summarizes the state of the art applications of short length LDPC codes and proposes FPGA based application specific hardware architectures for short-length LDPC decoders. The decoding algorithms considered for implementation are both belief propagation and min-sum algorithm. Due to the increased BER performances, the proposed architecture make use of parallel computation capabilities offered by FPGA technology in order to implement the belief propagation algorithm. In spite of the iterative nature and increased computational complexity of the LDPC decoding algorithm, the proposed architecture achieves high-throughput, mandatory in real-time application and data transmission. The architecture for the LDPC belief propagation based decoder is based on arctangent hyperbolic function approximation used for check nodes update.

## An modified beyond belief propagation algorithm over AWGN channel

- **Status**: ✅
- **Reason**: trapping set 기반 beyond-BP 디코더를 AWGN용으로 penalty factor로 개선 - 부호 비의존적 BP 개선 디코더(C)로 NAND LDPC에 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6645826
- **Type**: conference
- **Published**: 4-6 Sept. 
- **Authors**: Yibo Lv, Lin Wang
- **PDF**: https://ieeexplore.ieee.org/document/6645826
- **Abstract**: Recently one decoding algorithm called as beyond belief propagation (BP) algorithm for LDPC Codes is derived using the knowledge of trapping set and different from standard BP algorithm, whose performance outperforms that of the latter over binary symmetric channel (BSC). However, the former is not suitable for additive white Gaussian noise (AWGN) channel. In this paper how to improve bit error rate (BER) performance of Beyond BP Algorithm is investigated over AWGN channel. It is found that this algorithm can be modified through setting appropriate penalty factor and obtains better performance than BP one over AWGN channel. The simulation results show dependently on choosing penalty factor modified Beyond BP Algorithm outperforms BP one over AWGN channel in high signal noise rate (SNR) region or almost whole SNR one and there are some differences for different code rates. Concretely, for medium or low code rate proposed algorithm can obtain more performance gain relative to high one when short frame is used.

## Scaling challenges of NAND flash memory and hybrid memory system with storage class memory & NAND flash memory

- **Status**: ✅
- **Reason**: NAND 플래시 직접; EP-LDPC ECC로 inter-cell coupling 보정, retention/lifetime 다룸(A)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6658450
- **Type**: conference
- **Published**: 22-25 Sept
- **Authors**: Ken Takeuchi
- **PDF**: https://ieeexplore.ieee.org/document/6658450
- **Abstract**: This paper summarizes the scaling challenges of the conventional 2D floating-gate cell NAND flash memories [1, 2]. The scaling trends and limits of the bulk and SOI NAND flash memories are investigated in terms of short channel effects and channel boosting leakage from 20nm to below 10nm generation using 3D-device simulation. In the bulk NAND cell, 13nm generation is the scaling limit for realizing both channel boosting during program-inhibit and SCE suppression. The SOI NAND cell scaling limit is decreased to 8nm generation. Then, scaling problems and device design for 3D-stackable NAND flash memory are investigated [3]. Control gate length (Lg) and spacing (Lspace) are paid attention since they can be separately varied in 3D NAND and significantly affect the cell area of the 3D NAND as well as the electrical characteristics. Lg and Lspace should be the same to cope with the tradeoff between memory window and disturbance. If the number of stacked layers is 18 with the layer pitch of 40nm, the effective cell size of the 3D NAND corresponds to that of 15nm planar NAND technology. Then, this paper discusses an error prediction (EP) low density parity check (LDPC) error correcting code (ECC) which realizes an over 10-times extended lifetime [4, 5]. As the design rule shrinks, the floating gate (FG)-FG capacitive coupling among neighboring memory cells seriously degrades the memory cell reliability. The EP-LDPC ECC calibrates the inter-cell coupling without access time penalty. Finally, this paper overviews a state-of-the-art hybrid memory solution with storage class memory (SCM) and NAND flash memory for the big data solid-state storage system [5, 6]. Data fragmentation of MLC NAND flash memory is suppressed and efficient MLC NAND flash usage is realized by storing small hot data to SCM. The 3D TSV hybrid SSD realizes 11 times performance increase, 6.9 times endurance enhancement and 93% write energy reduction.

## New high rate LDPC codes for radio applications

- **Status**: ✅
- **Reason**: shifted identity+staircase 행렬로 고율 LDPC 신규 구성, BP/min-sum 디코딩 — E 코드설계 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6710530
- **Type**: conference
- **Published**: 21-22 Sept
- **Authors**: Ankita Pramanik, Gangamma Patil, L. Borman
- **PDF**: https://ieeexplore.ieee.org/document/6710530
- **Abstract**: Low-density parity-check (LDPC) code is linear-block error-correcting code defined by sparse parity-check matrix. LDPC codes have found wide application in various fields like satellite transmission, recording in magnetic discs etc. because of their capability to reach near Shannon limit performance. This paper presents 3 new high rates - 0.81, 0.84 and 0.89 of length 2512, 1843 and 2619 respectively, LDPC codes for radio application. The codes are constructed using shifted identity matrix and a lower staircase matrix. The complexity of encoding of these codes is low and decoding can be done by belief propagation. Simulation results of the codes show good bit error rate performance with min-sum decoding algorithm.

## PG-LDPCC Codes in Turbo Equalizer Systems: Trade-Off between Design Parameters of the Protograph and the Permutation Size

- **Status**: ✅
- **Reason**: protograph 기반 terminated LDPC-CC(SC-LDPC)의 설계 파라미터(ms,L,permutation size P)와 성능 trade-off 분석 — E(코드 설계, SC-LDPC 구성) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6692361
- **Type**: conference
- **Published**: 2-5 Sept. 
- **Authors**: Patrick Grosa, Gerhard Fettweis
- **PDF**: https://ieeexplore.ieee.org/document/6692361
- **Abstract**: Turbo equalization is a technique to enable wireless transmissions by means of an iterative exchange of information between several components at the receiver incorporating a soft equalizer. The performance achievable can be improved by adjusting the components related to one another. The focus of this paper lies on the study of the possible adjustments to terminated protograph-based Low- Density Parity Check convolutional codes. Some of the parameters (syndrome former memory ms, termination length L) are related to the underlying terminated convolutional protograph, while others (like permutation size P) come into play during the actual code construction process. Compared to our previous work where the design parameter of the protograph is the only focus of the study, this work will also focus on the final constructed codes and their performance. In order to evaluate the code's performance, the length of the code is an important property. Along with the permutation size P and the protograph parameters (ms, L), it is possible to make a fair comparison between the codes and to decide in favor of the code used to achieve the desired requirements of code length, performance, and code rate.

## A low-complexity implementation of QC-LDPC encoder in reconfigurable logic

- **Status**: ✅
- **Reason**: QC-LDPC 인코더 HW 구현(GF(2) 상수행렬 곱셈 최적화, LUT 하드와이어로 cyclic-shifter 제거) - 이식 가능 HW 아키텍처(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:6645587
- **Type**: conference
- **Published**: 2-4 Sept. 
- **Authors**: Georgios Tzimpragos, Christoforos Kachris, Dimitrios Soudris +1
- **PDF**: https://ieeexplore.ieee.org/document/6645587
- **Abstract**: Low Density Parity Check(LDPC) codes are a special class of error correction codes widely used in communication and disk storage systems, due to their Shannon limit approaching performance and their favorable structure. In this paper, a methodology for optimized hardware multiplication by constant matrices in GF(2) is introduced and then applied to the Quasi-Cyclic LDPC encoding algorithm. Taking advantage of the fact that the parity check matrix rarely changes, the signals in many cases are hard-wired into the LUTs and thus the cyclic-shifters and block-memories conventionally used are eliminated. Therefore, the proposed framework leads to less complex, mapped to reconfigurable logic designs, whereas it combines the performance of hard-wired solutions (high throughput, low latency) and the flexibility of the software and its hardware counterparts. These advantages in terms of hardware savings and throughput prove that the proposed encoder scheme is suitable for high-speed applications, such as long-haul optical transmission, where speed and resources utilization are a major issue.

## Configurable low complexity decoder architecture for Quasi-Cyclic LDPC codes

- **Status**: ✅
- **Reason**: QC-LDPC layered 디코더 HW 아키텍처(permutation network 재구성, 메모리/전력 절감) - 이식 가능 HW(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:6671861
- **Type**: conference
- **Published**: 18-20 Sept
- **Authors**: Sherif Abou Zied, Ahmed T. Sayed, Rafik Guindi
- **PDF**: https://ieeexplore.ieee.org/document/6671861
- **Abstract**: In this paper, we present a fully pipelined QC-LDPC decoder for 802.11n standard that supports variable block sizes and multiple code rates. The proposed architecture utilizes features of Quasi-Cyclic LDPC codes and layered decoding to reduce memory bits and interconnection complexity through efficient utilization of permutation network for forward and backward interconnection routing. Permutation network reorganization and small check node granularity reduced the overall resources required for routing, thus reducing the overall decoder dynamic power consumption. Proposed architecture has been synthesized using Virtex-6 FPGA and achieved 19% reduction in dynamic power consumption, 5% less logic resources and 12% increase in throughput.
