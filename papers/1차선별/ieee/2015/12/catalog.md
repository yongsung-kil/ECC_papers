# IEEE Xplore — 2015-12 (1차선별 통과)


## Approximated Box-Plus Decoding of LDPC Codes

- **Status**: ✅
- **Reason**: SPA box-plus 연산의 신규 저복잡도 근사 디코딩 알고리즘, min-sum류 디코더 변형으로 NAND LDPC에 직접 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7301997
- **Type**: journal
- **Published**: Dec. 2015
- **Authors**: Stylianos Papaharalabos, Fotis Lazarakis
- **PDF**: https://ieeexplore.ieee.org/document/7301997
- **Abstract**: The problem of how to approximate effectively the box-plus operation used in sum-product algorithm (SPA) decoding of low-density parity-check (LDPC) codes has been widely investigated over the past years of research. This letter deals, for the first time, with a totally different approach where a very simple, yet efficient, decoding algorithm for LDPC codes is proposed. The tremendous savings, in terms of required number of operations, offered by the proposed algorithm and its near optimal SPA performance are making it appealing in practical applications requiring very low complexity LDPC decoding architectures.

## Reliability of Memories Built From Unreliable Components Under Data-Dependent Gate Failures

- **Status**: ✅
- **Reason**: 불신뢰 게이트로 만든 비트플립 디코더로 LDPC 메모리 신뢰성 보장 - 디코더 강건성 기법(C) 이식 가능, 메모리 도메인
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7312924
- **Type**: journal
- **Published**: Dec. 2015
- **Authors**: Srdan Brkic, Predrag Ivaniš, Bane Vasić
- **PDF**: https://ieeexplore.ieee.org/document/7312924
- **Abstract**: In this letter, we investigate fault-tolerance of memories built from unreliable cells. In order to increase the memory reliability, information is encoded by a low-density parity-check (LDPC) code, and then stored. The memory content is updated periodically by the bit-flipping decoder, built also from unreliable logic gates, whose failures are transient and data-dependent. Based on the expander property of Tanner graph of LDPC codes, we prove that the proposed memory architecture can tolerate a fixed fraction of component failures and consequently preserve all the stored information, if code length tends to infinity.

## High Throughput Pipeline Decoder for LDPC Convolutional Codes on GPU

- **Status**: ✅
- **Reason**: LDPC-CC GPU 파이프라인 디코더 병렬화 기법, 병렬 디코더 아키텍처로 이식 가능(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:7289356
- **Type**: journal
- **Published**: Dec. 2015
- **Authors**: Yi Hou, Rongke Liu, Hao Peng +1
- **PDF**: https://ieeexplore.ieee.org/document/7289356
- **Abstract**: In this letter, we present a graphics processing unit (GPU)-based LDPC convolutional code (LDPC-CC) pipeline decoder with optimized parallelism. The proposed decoder exploits different granularities of decoding parallelism for both the compute unified device architecture (CUDA) kernel execution stage and the data transfer stage. Moreover, the parameter selection criteria for decoder implementation are designed to avoid exhaustive search of all the combinations of parameters. The experiments are carried out on Nvidia GTX460 and GTX580 platforms. The results demonstrate the proposed decoder achieves about 3 times speedup compared to the existing GPU-based work.

## On the LLR Metrics for DPSK Modulations Over Two-Symbol Observation Intervals for the Flat Rician Fading Channel

- **Status**: ✅
- **Reason**: DPSK LLR 메트릭 도출이 turbo/LDPC 반복디코딩에 적용, LLR 계산 기법은 NAND LDPC LLR 양자화에 참고 가능(애매→살림)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7275142
- **Type**: journal
- **Published**: Dec. 2015
- **Authors**: Haifeng Yuan, Pooi-Yuen Kam
- **PDF**: https://ieeexplore.ieee.org/document/7275142
- **Abstract**: We consider the differential phase-shift keying modulation over the flat Rician fading channel with perfect channel model information (PCMI), and derive the two-symbol-observation-interval log-likelihood ratio (LLR) metric from first principles. The work generalizes the previous LLR derivations in [16]-[19], and demonstrates the necessity of the knowledge of the statistical channel model in the exact LLR computation. Assuming the channel is slowly time-varying, we also propose a simple approximate LLR metric based on the generalized likelihood ratio test (GLRT), which requires only the information of the noise spectral density. The advantage of the newly derived PCMI-LLR metric over the approximate metric and the other LLR metrics in the literature is explained from the information-theoretic perspective via the generalized mutual information. Computer simulations are also provided to demonstrate the superiority of the PCMI-LLR metric in both error rate performance and convergence speed for iterative decoding of turbo and low-density parity-check codes in practical systems. This paper aims to present the fundamental principles of LLR computation, emphasizing the importance of selecting the appropriate metric for iterative decoding over fading channels.

## High-Throughput Trellis Processor for Multistandard FEC Decoding

- **Status**: ✅
- **Reason**: 멀티스탠다드 trellis FEC 프로세서로 LDPC 디코딩 지원 — 병렬 trellis HW 아키텍처 이식 여지(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:7066973
- **Type**: journal
- **Published**: Dec. 2015
- **Authors**: Zhenzhi Wu, Dake Liu
- **PDF**: https://ieeexplore.ieee.org/document/7066973
- **Abstract**: Trellis codes, including Low-Density Parity-Check (LDPC), turbo, and convolutional code (CC), are widely adopted in advanced wireless standards to offer high-throughput forward error correction (FEC). Designing a multistandard FEC decoder is of great challenge. In this paper, a trellis application specified instruction-set processor (TASIP) is presented for multistandard trellis decoding. A unified forward-backward recursion kernel with an eight-state parallel trellis structure is proposed. Based on the kernel, a datapath for multialgorithm and a shared memory subsystem are introduced. The flexibility and the compatibility are guaranteed by a programmable decoding flow and the trellis decoding instruction set. Synthesis results show that the area consumption is 2.12 mm2 (65 nm). TASIP provides trimode FEC decoding ability with the throughput of 533, 186, and 225 Mb/s for LDPC, turbo, and 64 states CC under the clock frequency of 200 MHz, which outperforms other trimode proposals both in area efficiency and recursion efficiency. TASIP provides high-throughput decoding for current standards, including 3rd Generation Partnership Project-Long Term Evolution, 802.16e, and 802.11n, with unified architecture and high compatibility.

## ACOCO: Adaptive Coding for Approximate Computing on Faulty Memories

- **Status**: ✅
- **Reason**: faulty memory 상의 min-sum 디코더용 적응 코딩, 메모리 오류 하 min-sum 견고화는 NAND 디코더 HW에 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7275150
- **Type**: journal
- **Published**: Dec. 2015
- **Authors**: Chu-Hsiang Huang, Yao Li, Lara Dolecek
- **PDF**: https://ieeexplore.ieee.org/document/7275150
- **Abstract**: With scaling of process technologies and increase in process variations, embedded memories will be inherently unreliable. Approximate computing is a new class of techniques that relax the accuracy requirement of computing systems. In this paper, we present the Adaptive Coding for approximate Computing (ACOCO) framework, which provides us with an analysis-guided design methodology to develop adaptive codes for different computations on the data read from faulty memories. In ACOCO, we first compress the data by introducing distortion in the source encoder, and then add redundant bits to protect the data against memory errors in the channel encoder. We are thus able to protect the data against memory errors without additional memory overhead so that the coded data have the same bit-length as the uncoded data. We design the source encoder by first specifying a cost function measuring the effect of the data compression on the system output, and then design the source code according to this cost function. We develop adaptive codes for two types of systems under ACOCO. The first type of systems we consider, which includes many machine learning and graph-based inference systems, is the systems dominated by product operations. We evaluate the cost function statistics for the proposed adaptive codes, and demonstrate its effectiveness via two application examples: max-product image denoising and naïve Bayesian classification. Next, we consider another type of systems: iterative decoders with min operation and sign-bit decision, which are widely applied in wireless communication systems. We develop an adaptive coding scheme for the min-sum decoder subject to memory errors. A density evolution analysis and simulations on finite length codes both demonstrate that the decoder with our adaptive code achieves a residual error rate that is on the order of the square of the residual error rate achieved by the nominal min-sum decoder.

## Parallel Algorithmic Optimization and Achievement for LDPC Encoding and Decoding on CUDA Platform

- **Status**: ✅
- **Reason**: CUDA GPU 기반 LDPC BP 병렬 디코딩/인코딩 가속 — 병렬 디코더 HW/구현 기법 이식 가능(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:7424168
- **Type**: conference
- **Published**: 7-9 Dec. 2
- **Authors**: Liu Zhen, Wang Yunpei, Lu Lulu
- **PDF**: https://ieeexplore.ieee.org/document/7424168
- **Abstract**: With the development of mobile Internet applications, the fourth generation mobile communication (4G) has been widely used, low-density parity-check (LDPC) codes have gradually become the first choice for 4G communication because of its superior performance. For the short of traditional encoding and belief propagation (BP) decoding algorithm, this paper adopts a method of parallel processing for LDPC encoding and decoding which is finally realized on the mobile terminal. On the CUDA platform, CPU scheduling and GPU parallelization are used to process a large number of repeated operations so that parallel encoding algorithm and heterogeneous parallel BP algorithm are achieved and the efficiency is significantly improved.

## Analysis of ADMM-LP algorithm for LDPC decoding, a first step to hardware implementation

- **Status**: ✅
- **Reason**: ADMM-LP LDPC 디코더 복잡도 분석+병렬화, HW 구현 지향 — 디코더 알고리즘/HW 이식 가능(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7440322
- **Type**: conference
- **Published**: 6-9 Dec. 2
- **Authors**: Imen Debbabi, Bertrand Le Gal, Nadia Khouja +2
- **PDF**: https://ieeexplore.ieee.org/document/7440322
- **Abstract**: The recent interest in linear programming techniques for LDPC decoding showed that these methods are too complex for real applicability. Alternating direction method of multipliers is a classic technique in convex optimization theory. When applied to the linear programming decoding of LDPC codes, the ADMM algorithm acts as a message passing decoding method. In this work, we present a complexity analysis of the ADMM LDPC decoder compared with the sum product approach and we explain the parallelism levels that are explored in the ADMM algorithm. A software implementation by taking advantage of the architectural features of the multi-core processors parallelism is presented. The overall analysis provides a better understanding of the ADMM approach complexity which makes a start to possible hardware implementations.

## A Novel Fast LDPC Decoder Using APP-Based Dynamic Scheduling Scheme

- **Status**: ✅
- **Reason**: 바이너리 LDPC BP용 신규 동적 스케줄링(APPRBP)으로 반복 수 감소—NAND LDPC 디코더에 이식 가능한 알고리즘(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7417208
- **Type**: conference
- **Published**: 6-10 Dec. 
- **Authors**: Tian Xia, Hsiao-Chun Wu, Scott C.-H. Huang
- **PDF**: https://ieeexplore.ieee.org/document/7417208
- **Abstract**: Low-density parity-check (LDPC) codes are favorable in modern telecommunication technologies due to its superior error-correction capability especially when the codeword length is large. The commonly-used LDPC decoders are based on the belief-propagation (BP) algorithms. It is well known that the layered (serial) belief-propagation (LBP) decoding algorithms can reduce the number of iterations by half in comparison with the flooding (parallel) BP decoding algorithms. Further reduction in total number of iterations can be achieved by using the informed dynamic scheduling techniques, such as residual BP (RBP) and node-wise residual BP (NWRBP) methods. However, the incurred additional computation of residuals is far from trivial. In this paper, we propose a novel efficient dynamic scheduling scheme, called a posteriori probability RBP (APPRBP) algorithm, which offers more flexibility to leverage the performance-complexity trade-off using a threshold parameter. The simulation results demonstrate that the average iteration numbers for our proposed APPRBP algorithm can be remarkably reduced especially in the low E_b/N_0 (signal-energy-per-information-bit to noise-power-spectral-density ratio) conditions while the bit-error rate (BER) performance is subject to slight degradation.

## XJ-BP: Express Journey Belief Propagation Decoding for Polar Codes

- **Status**: ✅
- **Reason**: polar용 BP지만 MS-BP 복잡도 90% 절감 round-trip 메시지패싱 스케줄링—부호 비의존적 BP 기법으로 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7417316
- **Type**: conference
- **Published**: 6-10 Dec. 
- **Authors**: Jingwei Xu, Tiben Che, Gwan Choi
- **PDF**: https://ieeexplore.ieee.org/document/7417316
- **Abstract**: This paper presents a novel belief propagation (BP) based decoding algorithm for polar codes. The proposed algorithm facilitates belief propagation by utilizing the specific constituent codes that exist in the factor graph, which results in an express journey (XJ) for belief information to propagate in each decoding iteration. In addition, this XJ-BP decoder employs a novel round-trip message passing scheduling method for the increased efficiency. The proposed method simplifies min-sum (MS) BP decoder by 40.6\%. Along with the round-trip scheduling, the XJ-BP algorithm reduces the computational complexity of MS BP decoding by 90.4\%; this enables an energy-efficient hardware implementation of BP decoding in practice.

## Performance of the modified SRBI-MLGD algorithm for LDPC codes in MLC NAND flash memory

- **Status**: ✅
- **Reason**: MLC NAND용 수정 SRBI-MLGD 저복잡도 디코딩 알고리즘(BP 대체)으로 카테고리 A/C 직접 해당
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7459823
- **Type**: conference
- **Published**: 2-4 Dec. 2
- **Authors**: Jiaying Wen, Guojun Han, Xusheng Lin +1
- **PDF**: https://ieeexplore.ieee.org/document/7459823
- **Abstract**: With continued scaling down of the NAND flash memory, the multi-level cell (MLC) technique emerges to dramatically increase the storage density. Meanwhile, this technique also leads to worse error performance owing to the cell-to-cell interference (CCI). Recently, low-density parity-check (LDPC) code has appeared to be a promising solution to combat the performance degradation of NAND flash memory. Although LDPC codes can provide stronger error performance, the conventional belief propagation (BP) decoding algorithm requires calculating soft-decision log-likelihood (LLR) information and hence possesses a massive computational complexity. In this paper, by exploiting the characteristics of MLC NAND flash memory channels, we present a modified soft reliability-based iterative majority-logic decoding (SRBI-MLGD) algorithm for the LDPC codes over MLC NAND flash memory channels. The modified decoding algorithm has less computational complexity as compared with the sum-product decoding algorithm (SPA). Moreover, the simulation results show that the decoding algorithm offers an effective trade-off between complexity and performance over high-column-weight LDPC coded MLC NAND flash memory channels.

## Further results on LDPC decoding scheduling for faster convergence

- **Status**: ✅
- **Reason**: 빠른 수렴을 위한 LDPC 디코딩 스케줄링(LM2I2) 신규 기법으로 카테고리 C 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7459839
- **Type**: conference
- **Published**: 2-4 Dec. 2
- **Authors**: Huang-Chang Lee, Yen-Ming Chen, Yeong-Luh Ueng +1
- **PDF**: https://ieeexplore.ieee.org/document/7459839
- **Abstract**: This paper presents a listed maximum mutual information increase (LM2I2)-based algorithm, which is used to arrange low-density parity-check (LDPC) decoding schedules for faster convergence. The increments in the predicted mutual information for the messages to be updated is used to guide the arrangement of the fixed decoding schedule. Consequently, by looking ahead for several decoding stages, a high-order prediction can be realized. For each decoding stages, the searching branches can be trimmed to fit a predetermined size of list, and the efficiency in the selection of update candidates is thus increased. Comparing to previous algorithms, the proposed LM2I2-based algorithm can be used to arrange the decoding schedules converged in the same speed with lower complexity, or accelerate the convergence with the same computation cost.

## Template-based QC-LDPC decoder architecture generation

- **Status**: ✅
- **Reason**: layered QC-LDPC HW 아키텍처 자동생성(부분병렬, 분산제어) 템플릿으로 카테고리 D 이식 가능
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:7459838
- **Type**: conference
- **Published**: 2-4 Dec. 2
- **Authors**: Oana Boncalo, Petru Florin Mihancea, Alexandra Amaricai
- **PDF**: https://ieeexplore.ieee.org/document/7459838
- **Abstract**: This paper presents an automated template-based approach for layered QC-LDPC architectures. The underlying idea is to be able to generate any number of fairly optimized hardware designs with only a minimum effort required by tuning high level parameters (parity check matrix, number of AP-LLR messages being processed at a time, etc.). Having chosen a partially parallel architecture, template design effort has been concentrated in two directions: distributed control across the LDPC decoder for modularity and versatility, and datapath design in order to support any given parallelism at processing node level. All user inputs are propagated by the proposed automated flow for all design phases: (i) Verilog HDL LDPC architecture (ii) test-benches and verification environments (iii) evaluation step (BER/FER, average iterations, cost, throughput) of the LDPC decoder architecture. We present the results for the architectures generated for dv = 3, dv = 4 regular QC-LDPC code, as well as for the WiMAX (1152,2304) irregular code, with different levels of parallelism at processing node level.

## Low-complexity quantization-aware belief-propagation (QA-BP) decoding for MLC NAND flash memory

- **Status**: ✅
- **Reason**: MLC NAND LDPC용 신규 QA-BP 디코더(shuffled BP + 불균등 LLR 활용)로 카테고리 A/C 직접 해당
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7459820
- **Type**: conference
- **Published**: 2-4 Dec. 2
- **Authors**: Chaudhry Adnan Aslam, Yong Liang Guan, Kui Cai
- **PDF**: https://ieeexplore.ieee.org/document/7459820
- **Abstract**: State-of-the-art NAND flash chips experience significant channel noise impairments and raise several data reliability issues. To overcome these issues, low-density parity-check (LDPC) codes are becoming the main stream error-correcting-codes in flash memory controllers. Consequently, the long belief-propagation (BP) decoding latency starts to deteriorate the system performance. In this paper, a low-complexity quantization-aware belief-propagation (QA-BP) decoding scheme is introduced for meeting the requirement of faster BP convergence speed. Using the shuffled BP algorithm, the proposed QA-BP scheme takes advantage of highly unequal error probability of input log-likelihood-ratios (LLRs), transpired as a result of non-uniform channel quantization, and update only less reliable variable nodes that are initiated with higher error probability LLR values. For realizing the QA-BP scheme, neither additional runtime operations nor real-valued comparisons are required. Using simulation results, it is shown that the proposed QA-BP scheme can yield a noticeable improvement in BP convergence speed without compromising the error performance.

## An efficient early stopping analog decoder for LDPC codes

- **Status**: ✅
- **Reason**: 아날로그 LDPC 디코더의 satisfied-check 확률 기반 early-stopping 기준 제안 — 반복 종료/디코더 기법으로 이식 가능(C).
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7490926
- **Type**: conference
- **Published**: 19-20 Dec.
- **Authors**: Yuan Gao, Yujie Lin, Bowen Zeng +2
- **PDF**: https://ieeexplore.ieee.org/document/7490926
- **Abstract**: The analog implementation of error control decoders is a competitive methodology compared with the digital implementation in power efficiency and throughput. In order to detect uncorrectable frames and early stop the iterative decoding of low-density parity check (LDPC) analog decoders, a probability stopping block using probabilities of satisfied checks is proposed. Simulation results show that the proposed criterion can greatly reduce the average number of iterations at low SNR, and has better tradeoff between complexity and performance than other stopping criteria using extrinsic information.

## Novel construction and cycle analysis of Quasi-Cyclic Low-Density Parity-Check codes

- **Status**: ✅
- **Reason**: QC-LDPC 신규 shift matrix 구성으로 사이클 구조 복제 회피·girth 6 이상 보장 — 바이너리 QC-LDPC 코드설계(E) 직접 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7489843
- **Type**: conference
- **Published**: 18-20 Dec.
- **Authors**: Wenwen Li, Mao Ai, Jie Qiu +1
- **PDF**: https://ieeexplore.ieee.org/document/7489843
- **Abstract**: Quasi-Cyclic Low-Density Parity-Check (QC-LDPC) codes have practical significance in the field of engineering, thus their construction algorithm is a hot issue in the field of LDPC codes. Based on existing construction methods, particularly the method based on Progressive Edge-Growth (PEG) algorithm, a new construction method of shift matrix is proposed. It can effectively avoid the copy of cycle structures, especially short cycles in base matrix after extension. Besides, it also relieves the time cost caused by random search, and greatly improves the length of cycles when compared with algorithms based on methods such as quadratic congruence and arithmetic sequence. Those algorithms can only eliminate short cycles with length 4, while our method can provide QC-LDPC codes without length 6 at least. Cycle analysis and simulation results show that the newly constructed QC-LDPC codes have good cycle structure and error correction performance.

## PAPR reduction in OFDM systems using Quasi Cyclic Invertible Subset LDPC codes

- **Status**: ✅
- **Reason**: PAPR 감소용 QC-IS-LDPC(준순환 가역 부분집합) 신규 코드 구성 제안, 낮은 탐색복잡도·우수한 오류정정 — 바이너리 QC-LDPC 구성(E) 이식 여지, 애매하여 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7475350
- **Type**: conference
- **Published**: 18-19 Dec.
- **Authors**: Ciya Thomas, C.D Suriyakala
- **PDF**: https://ieeexplore.ieee.org/document/7475350
- **Abstract**: Wireless communication is one of the important aspects of long distance communication. Along with the progress in technology rapid changes has been achieved in the field of wireless communication. Recent advances in wireless communication systems have increased the throughput and reliability of wireless channels. But still the bandwidth and spectral availability demands are endless. Researches in this field show that Orthogonal Frequency Division Multiplexing (OFDM) has become the modulation choice for high data-rate communication systems. But OFDM has the disadvantage of having large fluctuations in signal amplitude which has resulted in a high Peak-to-Average-Power Ratio (PAPR). High PAPR is a major drawback of multicarrier transmission system which leads to power inefficiency in RF section of the transmitter. The important PAPR reduction techniques for multicarrier transmission includes amplitude clipping and filtering, coding, partial transmit sequence and selected mapping. Among which, coding based approaches have inherent error control capability and simplicity of implementation. But this approach has limitations like an exhaustive search to find the best codes and to store large lookup tables for encoding and decoding. We are proposing a novel coding method called as Quasi Cyclic Invertible Subset LDPC (QC-IS-LDPC) codes for PAPR reduction in OFDM systems with low searching complexity and good error correcting performance. An intensive study will be done to compare the PAPR reduction capability and BER performance of QC-IS-LDPC coded OFDM with other PAPR reduction methods. Through this work we also examine the impact of different modulation schemes and coding rate on PAPR reduction.

## A 6.16Gb/s 4.7pJ/bit/iteration LDPC decoder for IEEE 802.11ad standard in 40nm LP-CMOS

- **Status**: ✅
- **Reason**: D: 802.11ad용이지만 column-parallel 저전력 고속 LDPC 디코더 HW 아키텍처(메모리 60% 절감, 파이프라인 최소화) 이식 가능
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:7418406
- **Type**: conference
- **Published**: 14-16 Dec.
- **Authors**: Hiroyuki Motozuka, Naoya Yosoku, Takenori Sakamoto +3
- **PDF**: https://ieeexplore.ieee.org/document/7418406
- **Abstract**: This paper presents an LDPC decoder employing a column-parallel architecture that enables low-power and high-speed operation suitable for the 802.11ad standard. As compared to the conventional row-parallel architecture, the proposed architecture reduces the required memory size by 60% and also minimizes the number of pipeline stages for high throughput operation. Fabricated in 40nm LP CMOS technology, the prototype achieves high energy efficiency of 4.7pJ/bit/iteration for 6.16Gb/s while supporting all the modulation and coding schemes (MCS0 to MCS12) required for the 802.11ad single-carrier (SC) modulation.

## Coding performance for signal dependent channels in visible light communication system

- **Status**: ✅
- **Reason**: 신호의존 채널 최적 LLR 계산 + 저복잡도 수정 min-sum + (3,6) LDPC — 이식 가능 LLR 계산/디코더 기법(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7418355
- **Type**: conference
- **Published**: 14-16 Dec.
- **Authors**: Ming Yuan, Xiaoshi Sha, Xiao Liang +3
- **PDF**: https://ieeexplore.ieee.org/document/7418355
- **Abstract**: Avalanche photo-diodes (APD) are widely employed in visible light communication (VLC) systems. Experiments show that under official illuminance APD shot noise can not be ignored due to the multiplication process. Under VLC dual-purpose illumination, symbols on different constellation points inevitably experience different levels of noise. In such a signal dependent noise channel, traditional log likely-hood ratio (LLR) calculation for decoder assuming signal independent noise will cause performance loss. In this work, we first investigate the general signal dependent Gaussian channel. The optimal LLR calculation for decoder is then derived. We further analyze the extrinsic information transfer chat to find the decoding thresholds. Finally a modified minimum sum algorithm is suggested with reduced complexity. Numerical simulations show that, with a regular (3,6) low-density parity check (LDPC) code of block length 20000, our proposed scheme can achieve 0.7dB gain over the scheme designed for signal independent noise.

## Trellis based node operations for LDPC decoders from the Information Bottleneck method

- **Status**: ✅
- **Reason**: Information Bottleneck 기반 이산 LDPC 디코더 — 4bit 정수 메시지로 min-sum 능가, NAND LLR 양자화에 직결되는 이식 가능 디코더(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7391731
- **Type**: conference
- **Published**: 14-16 Dec.
- **Authors**: Jan Lewandowsky, Gerhard Bauch
- **PDF**: https://ieeexplore.ieee.org/document/7391731
- **Abstract**: We utilize the Information Bottleneck method in a discrete density evolution scheme that was introduced by Brian M. Kurkoski et al. in order to find message mappings for the node operations of discrete LDPC decoders. The resulting decoders have performance close to belief propagation decoding but require much lower implementation efforts because they only process unsigned integers instead of log-likelihood-ratios. An efficient trellis implementation of the resulting discrete node operations is presented. In the trellis implementation the passed messages are calculated using recursive formulas that are fully characterized by two static vectors of integers. Bit error rate simulations for exemplary (3, 6)-regular LDPC codes with a 4 bit message representation prove the performance of the proposed decoders that even outperform Min-Sum decoders with quasi continuous message representation.

## Improved controlled start-up stochastic LDPC decoder for efficient FPGA-based implementation

- **Status**: ✅
- **Reason**: D: 개선된 controlled start-up stochastic LDPC 디코더 FPGA 구현(가변노드 내부메모리 확장) — 이식 가능 HW 아키텍처
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:7416861
- **Type**: conference
- **Published**: 13-15 Dec.
- **Authors**: Ghania Zerari, Abderrezak Guessoum
- **PDF**: https://ieeexplore.ieee.org/document/7416861
- **Abstract**: This paper introduces a new and an improved controlled start-up stochastic (CSS) architecture of Low-Density Parity-Check (LDPC) decoding, to implement fully parallel FPGA-based decoders. The developed architecture uses a new variable nodes structure with larger internal memory lengths, to improve the convergence, without significant additional field programmable gate array (FPGA) resource. To validate the advantage of the proposed approach, a medium (1024, 512) and short (200, 100) codes are implemented. The results of Xilinx Virtex-6 VLX240T FPGA shoes that the variable node internal memories lengths can be increased from 2-bit, used in CSS and Delayed Stochastic (DS) decoders, to 64-bit without addition resource.

## Simplified LLR calculation for DVB-S2 LDPC decoder

- **Status**: ✅
- **Reason**: DVB-S2 LDPC 디코더용 간략 LLR 계산(constellation 분할 근사) — LLR 양자화/근사 기법 NAND 디코더에 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7434300
- **Type**: conference
- **Published**: 10-12 Dec.
- **Authors**: Vanessa B. Olivatto, Renato R. Lopes, Eduardo R. de Lima
- **PDF**: https://ieeexplore.ieee.org/document/7434300
- **Abstract**: The computation of the Log-Likelihood Ratio (LLR) at the channel output may impose great demand of memory and hardware area, especially for high-order modulations. This paper introduces a new approach for the approximation of the LLR in AWGN channels based on the splitting of the original constellation into smaller sectors. Each new sector has a less complex configuration in which it is possible to take into account only two symbols besides the received one. The proposed solution is applied for the 8-PSK and 16-APSK constellations adopted in the Digital Video for Satellite Second Generation standard (DVBS2).
