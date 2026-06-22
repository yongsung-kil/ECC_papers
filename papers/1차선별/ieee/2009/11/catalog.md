# IEEE Xplore — 2009-11 (1차선별 통과)


## An efficient on-the-fly encoding algorithm for binary and finite field LDPC codes

- **Status**: ✅
- **Reason**: 바이너리/유한체 LDPC on-the-fly 인코딩 프레임워크 — 스토리지 응용 명시, 바이너리 부분은 이식 가능 인코딩 구조(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5337065
- **Type**: journal
- **Published**: November 2
- **Authors**: Shayan G. Srinivasa, Anthony Weathers
- **PDF**: https://ieeexplore.ieee.org/document/5337065
- **Abstract**: We present a general framework on prototype structures for efficiently encoding low density parity check codes on-the-fly. The encoding algorithm is applicable to finite field based codes and can handle a wide range of high code rates and large block lengths. This structure can be used particularly in data storage and multimedia applications with increased code rate and throughput requirements. We also establish the necessary and sufficient conditions for the existence of such encoders.

## Memory efficient multi-rate regular LDPC decoder for CMMB

- **Status**: ✅
- **Reason**: 메모리 효율 부분병렬 멀티레이트 LDPC 디코더 HW(AGU+인덱스행렬)는 NAND LDPC 디코더 HW로 이식 가능(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:5373744
- **Type**: journal
- **Published**: November 2
- **Authors**: So-Jin Lee, Joo-Yul Park, Ki-Seok Chung
- **PDF**: https://ieeexplore.ieee.org/document/5373744
- **Abstract**: In this paper, we propose a memory efficient multi-rate Low Density Parity Check (LDPC) decoder for China Mobile Multimedia Broadcasting (CMMB). We find the best trade-off between the performance and the circuit area by designing a partially parallel decoder which is capable of passing multiple messages in parallel. By designing an efficient address generation unit (AGU) with an index matrix, we could reduce both the amount of memory requirement and the complexity of computation. The proposed regular LDPC decoder was designed in Verilog HDL and was synthesized by Synopsys¿ Design Compiler using Chartered 0.18 ¿m CMOS cell library. The synthesized design has the gate size of 455 K (in NAND2). For the two code rates supported by CMMB, the rate-1/2 decoder has a throughput of 14.32 Mbps, and the rate-3/4 decoder has a throughput of 26.97 Mbps. Compared with a conventional LDPC for CMMB, our proposed design requires only 0.39% of the memory.

## Iterative Approximate Linear Programming Decoding of LDPC Codes With Linear Complexity

- **Status**: ✅
- **Reason**: LDPC LP 디코딩의 선형복잡도 반복 근사 알고리즘(min-sum/BP 유사), 부호 비의존 디코더 기법으로 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5290280
- **Type**: journal
- **Published**: Nov. 2009
- **Authors**: David Burshtein
- **PDF**: https://ieeexplore.ieee.org/document/5290280
- **Abstract**: The problem of low complexity linear programming (LP) decoding of low-density parity-check (LDPC) codes is considered. An iterative algorithm, similar to min-sum and belief propagation, for efficient approximate solution of this problem was proposed by Vontobel and Koetter. In this paper, the convergence rate and computational complexity of this algorithm are studied using a scheduling scheme that we propose. In particular, we are interested in obtaining a feasible vector in the LP decoding problem that is close to optimal in the following sense. The distance, normalized by the block length, between the minimum and the objective function value of this approximate solution can be made arbitrarily small. It is shown that such a feasible vector can be obtained with a computational complexity which scales linearly with the block length. Combined with previous results that have shown that the LP decoder can correct some fixed fraction of errors we conclude that this error correction can be achieved with linear computational complexity. This is achieved by first applying the iterative LP decoder that decodes the correct transmitted codeword up to an arbitrarily small fraction of erroneous bits, and then correcting the remaining errors using some standard method. These conclusions are also extended to generalized LDPC codes.

## Waterfall Performance Analysis of Finite-Length LDPC Codes on Symmetric Channels

- **Status**: ✅
- **Reason**: 유한길이 바이너리 LDPC waterfall 성능분석, 블록/비트 오류확률 예측; 코드설계·성능평가 기법(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5336833
- **Type**: journal
- **Published**: Nov. 2009
- **Authors**: Raman Yazdani, Masoud Ardakani
- **PDF**: https://ieeexplore.ieee.org/document/5336833
- **Abstract**: An efficient method for analyzing the performance of finite-length low-density parity-check (LDPC) codes in the waterfall region, when transmission takes place on a memoryless binary-input output-symmetric channel is proposed. This method is based on studying the variations of the channel quality around its expected value when observed during the transmission of a finite-length codeword. We model these variations with a single parameter. This parameter is then viewed as a random variable and its probability distribution function is obtained. Assuming that a decoding failure is the result of an observed channel worse than the codeiquests decoding threshold, the block error probability of finite-length LDPC codes under different decoding algorithms is estimated. Using an extrinsic information transfer chart analysis, the bit error probability is obtained from the block error probability. Different parameters can be used for modeling the channel variations. In this work, two of such parameters are studied. Through examples, it is shown that this method can closely predict the performance of LDPC codes of a few thousand bits or longer in the waterfall region.

## Design of LDPC decoders for improved low error rate performance: quantization and algorithm choices

- **Status**: ✅
- **Reason**: permutation 기반 LDPC 병렬-직렬 디코더 HW(D), 양자화·log-tanh 근사가 absorbing set/error floor에 미치는 영향 분석(C/E) — NAND ECC 직결
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5336848
- **Type**: journal
- **Published**: Nov. 2009
- **Authors**: Zhengya Zhang, Lara Dolecek, Borivoje Nikolic +2
- **PDF**: https://ieeexplore.ieee.org/document/5336848
- **Abstract**: Many classes of high-performance low-density parity-check (LDPC) codes are based on parity check matrices composed of permutation submatrices. We describe the design of a parallel-serial decoder architecture that can be used to map any LDPC code with such a structure to a hardware emulation platform. High-throughput emulation allows for the exploration of the low bit-error rate (BER) region and provides statistics of the error traces, which illuminate the causes of the error floors of the (2048, 1723) Reed-Solomon based LDPC (RS-LDPC) code and the (2209, 1978) array-based LDPC code. Two classes of error events are observed: oscillatory behavior and convergence to a class of non-codewords, termed absorbing sets. The influence of absorbing sets can be exacerbated by message quantization and decoder implementation. In particular, quantization and the log-tanh function approximation in sum-product decoders strongly affect which absorbing sets dominate in the errorfloor region. We show that conventional sum-product decoder implementations of the (2209, 1978) array-based LDPC code allow low-weight absorbing sets to have a strong effect, and, as a result, elevate the error floor. Dually-quantized sum-product decoders and approximate sum-product decoders alleviate the effects of low-weight absorbing sets, thereby lowering the error floor.

## Linear LLR approximation for iterative decoding on wireless channels

- **Status**: ✅
- **Reason**: 반복디코딩용 선형 LLR 근사; LLR 양자화/근사 기법은 NAND LDPC LLR 처리에 이식 가능(C), 애매하나 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5336850
- **Type**: journal
- **Published**: Nov. 2009
- **Authors**: Raman Yazdani, Masoud Ardakani
- **PDF**: https://ieeexplore.ieee.org/document/5336850
- **Abstract**: On a fading channel with no channel state information at the receiver, true log-likelihood ratios (LLR) are complicated functions of the channel output. It is assumed in the literature that the power of the additive noise is known and the expected value of the fading gain is used in a linear function of the channel output to find approximate LLRs. This approach, however, is not optimal in the sense of bit error rate performance. In this paper, we introduce a measure of accuracy for the approximate LLRs based on their probability density function and we show that this measure provides a very convenient tool for finding good approximate LLRs. Assuming that the power of the additive noise is known, and using the proposed measure, we find a linear LLR approximation whose performance is extremely close to that of the true LLR calculation on an uncorrelated Rayleigh fading channel. These results are then extended to the case that the noise power is also unknown and a performance almost identical to the previous case is obtained.

## A Spectral-based partitioning algorithm for parallel LDPC decoding on a multiprocessor platform

- **Status**: ✅
- **Reason**: 멀티프로세서 LDPC 디코딩의 spectral-clustering 파티셔닝으로 inter-processor 통신 감소 — 병렬 HW 아키텍처 기법(D), NAND LDPC 디코더 병렬화에 이식 가능
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:5423793
- **Type**: conference
- **Published**: 22-24 Nov.
- **Authors**: Wen-Hsiang Hu, Chun-Yi Chen, Nader Bagherzadeh
- **PDF**: https://ieeexplore.ieee.org/document/5423793
- **Abstract**: Low Density Parity Check (LDPC) code is an error correction code that has near Shannon limit performance and is inherently suitable for parallel implementation. It has been widely used in several communication standards such as DVB-S2, WiMAX, and Wi-Fi. To address the need for supporting various LDPC codes in an era where diverse applications are integrated onto a single system, a multi-processor based implementation of the LDPC decoder was proposed. However, the heavy message exchange among processors limits the expected performance. In this paper, we present a partitioning algorithm based on graph spectral clustering to reduce the data communication during the decoding process. From the experiments, our approach successfully decreased the amount of inter-processor communication by 33% ~ 52%, as compared to the original sequential mapping approach. Together with the more balanced computation load from our algorithm, an improvement of up to 85% in the overall decoding time was observed.

## A LDPC decoder with all single port memories

- **Status**: ✅
- **Reason**: single-port 메모리 LDPC 디코더 — CVPU 재사용/shuffle network 최적화 등 이식 가능 HW 아키텍처(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:5358099
- **Type**: conference
- **Published**: 20-22 Nov.
- **Authors**: Ying-Hong Tian, Xiao-Jun Zhang, Zong-Sheng Lai
- **PDF**: https://ieeexplore.ieee.org/document/5358099
- **Abstract**: this paper proposes one LDPC decoder with all single port memories to lower requirements of logic and interconnection and save hardware cost. Considering the lower read-write speed of single port memories than that of dual port memories, the decoder needs to reduce computation complex and shorten the critical path delay so as to get high throughput. To get the purpose, the LDPC decoder uses TDMP algorithm and normalized MS algorithm to reduce computation complex, uses reusable and configurable CVPU to realize single cycle pipeline variable and check node updating calculation, uses optimized shuffle network to shorten the path delay, and uses memories dominated controller to avoid the read and write conflict of memories. The implementation results show for once iteration process the throughputs are about 890Mbps, 847Mbps, and 863Mbps for rate 0.4, 0.6, and 0.8 respectively.

## A real-time programmable LDPC decoder chip for arbitrary QC-LDPC parity check matrices

- **Status**: ✅
- **Reason**: 임의 QC-LDPC용 프로그래머블 디코더 칩(DGC/AWA/EETS, 워드길이/조기종료) — 이식 가능 HW 아키텍처(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:5357173
- **Type**: conference
- **Published**: 16-18 Nov.
- **Authors**: Xin-Yu Shih, Cheng-Zhou Zhan, An-Yeu Wu
- **PDF**: https://ieeexplore.ieee.org/document/5357173
- **Abstract**: For the applications of next-generation channel-adaptive communication systems, a real-time programmable LDPC decoder architecture is proposed with three design techniques: divided-group comparison (DGC), adaptive wordlength assignment (AWA), and efficient early termination scheme (EETS). By utilizing programmable principle, the hardware architecture can support arbitrary Quasi-Cyclic LDPC parity check matrices, including various locations of 1's, information bits, codeword lengths, and code rates. The prototyping LDPC decoder chip using 0.13um CMOS technology, which supports up to 23 code rates with a maximum block size of 1536 bits, only occupies 4.94 mm2 die area, operates at 125 MHz, and dissipates 58 mW power.

## A new method of detecting cycles in Tanner graph of LDPC codes

- **Status**: ✅
- **Reason**: Tanner graph 사이클 검출 신규 알고리즘(논리대수 기반), 바이너리 LDPC 코드설계(사이클 제거, E)에 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5371660
- **Type**: conference
- **Published**: 13-15 Nov.
- **Authors**: Bo Li, Gang Wang, Hong-juan Yang
- **PDF**: https://ieeexplore.ieee.org/document/5371660
- **Abstract**: To improve the performance of LDPC codes, we should detect and eliminate cycles in Tanner graph of the parity-check matrix when we make LDPC codes. We improved a logic algebraic algorithm in computing entire routes between the nodes of a communication network, and found a new method of detecting cycles in Tanner graph of LDPC codes. This method applied the logic algebraic calculation rules. First transformed the parity-check matrix and then constructed the relative matrix of the Tanner graph. Through integrating and deleting rows of relative matrix and correcting some elements, this new algorithm can detect all the cycles in a Tanner graph of LDPC codes which code length is n and information bits number is k, just needing integrating and deleting n-1 times and correcting k times. The calculation steps of the algorithm is shown detailed by an (8, 4, 2) LDPC example and its correctness have been validated.

## An investigation in iterative decoding of Reed-Solomon codes based on adaptive belief propagation

- **Status**: ✅
- **Reason**: RS 부호이나 적응 BP(ABP) 기반 소프트 반복 디코더+조기종료 기법이 부호 비의존적 메시지패싱으로 바이너리 LDPC BP에 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5371418
- **Type**: conference
- **Published**: 13-15 Nov.
- **Authors**: Yushan Yang, Ming Jiang, Xiaofu Wu
- **PDF**: https://ieeexplore.ieee.org/document/5371418
- **Abstract**: In this paper, a practical approach to the iterative soft-decision decoding algorithms based on adaptive belief propagation (ABP) is investigated for Reed-Solomon (RS) codes. The novelty is cascading a simplified chase type decoder to the ABP scheme in each iteration, which can be viewed as an efficient termination criterion deployed in the ABP algorithm. Simulation results show that the proposed algorithm improves the FER performance and converges with fewer iterations averagely, which declares a significant complexity reduction.

## A low-complexity rate-compatible LDPC decoder

- **Status**: ✅
- **Reason**: QC-LDPC FPGA 디코더 HW 아키텍처(PLDA 병렬 layered decoding, 칩 면적/throughput 개선)로 D 이식 가능
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:5469954
- **Type**: conference
- **Published**: 1-4 Nov. 2
- **Authors**: Kai Zhang, Xinming Huang
- **PDF**: https://ieeexplore.ieee.org/document/5469954
- **Abstract**: In this paper, we present a rate-compatible LDPC decoder architecture which supports code rates between the rate of the mother code and 1. The rate-1/2 2304-bit Quasi-Cyclic (QC) LDPC codes with dual-diagonal parity check structure is selected from WiMax standard as the mother code and is punctured using specific puncturing patterns to obtain arbitrary rates. Parallel layered decoding architecture (PLDA) is employed to reduce chip area and improve the throughput. Simulation results show that the proposed punctured codes have comparable error correcting performances with the performances of dedicated codes from WiMax standard. The decoder is implemented on the platform of Xilinx XC2V8000. Compared with previous WiMax LDPC decoders synthesized by the same device, our low-complexity decoder consumes less FPGA resources: reduction of slices by 63%, flip-flops by 73%, look-up tables (LUTs) by 60% and RAMs by 30%.

## Low error rate LDPC decoders

- **Status**: ✅
- **Reason**: error floor 없는 저오류율 LDPC 디코더 설계+HW 에뮬레이션 기반 error floor 분석, 디코더/코드설계 기법 이식 가능(C/E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5469944
- **Type**: conference
- **Published**: 1-4 Nov. 2
- **Authors**: Zhengya Zhang, Lara Dolecek, Pamela Lee +4
- **PDF**: https://ieeexplore.ieee.org/document/5469944
- **Abstract**: Low-density parity-check (LDPC) codes have been demonstrated to perform very close to the Shannon limit when decoded iteratively. However challenges persist in building practical high-throughput decoders due to the existence of error floors at low error rate levels. We apply high-throughput hardware emulation to capture errors and error-inducing noise realizations, which allow for in-depth analysis. This method enables the design of LDPC decoders that operate without error floors down to very low bit error rate (BER) levels. Such emulation-aided studies facilitate complex systems designs.

## Trends and challenges in LDPC hardware decoders

- **Status**: ✅
- **Reason**: LDPC HW 디코더 알고리즘·아키텍처 개요(서베이지만 디코더 알고리즘/VLSI 아키텍처·error floor·throughput 정량 트렌드 포함, D/C 이식 가능)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5469947
- **Type**: conference
- **Published**: 1-4 Nov. 2
- **Authors**: Tinoosh Mohsenin, Bevan Baas
- **PDF**: https://ieeexplore.ieee.org/document/5469947
- **Abstract**: Over the last decade low density parity check (LDPC) codes have received significant attention due to their superior error correction performance, and have been adopted by recent communication standards such as 10 Gigabit Ethernet (10GBASE-T), digital video broadcasting (DVB-S2), WiMAX (802.16e), Wi-Fi (802.11n) and 60 GHz WPAN (802.15.3c). While there has been much research on LDPC decoders and their VLSI implementations, many difficulties to achieve requirements remain such as lower error floors, reduced interconnect complexities, smaller die areas, lower power dissipation, and design reconfigurability (run-time) to support multiple code lengths and code rates. This paper provides an overview of current research in LDPC decoder algorithms and architectures that are well suited for hardware implementations. Near and long-term trends of next generation LDPC requirements are made and an analysis of how current architectures will fare with the increasing demands on throughput, BER performance, power dissipation, and chip area (among others) that will be necessary for the widespread adoption of LDPC codecs in near-future applications.
