# IEEE Xplore — 2007-04 (1차선별 통과)


## Construction of Irregular LDPC Codes by Quasi-Cyclic Extension

- **Status**: ✅
- **Reason**: QC 확장 기반 불규칙 LDPC 신규 구성으로 error floor 저감 → E(코드설계) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4137875
- **Type**: journal
- **Published**: April 2007
- **Authors**: Jinghu Chen, R. Michael Tanner, Juntan Zhang +1
- **PDF**: https://ieeexplore.ieee.org/document/4137875
- **Abstract**: In this correspondence, we propose an approach to construct irregular low-density parity-check (LDPC) codes based on quasi-cyclic extension. When decoded iteratively, the constructed irregular LDPC codes exhibit a relatively low error floor in the high signal-to-noise ratio (SNR) region and are subject to relatively few undetected errors. The LDPC codes constructed based on the proposed scheme remain efficiently encodable

## A Memory Efficient Partially Parallel Decoder Architecture for Quasi-Cyclic LDPC Codes

- **Status**: ✅
- **Reason**: QC-LDPC 메모리효율 부분병렬 디코더 + modified min-sum HW 아키텍처(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4162517
- **Type**: journal
- **Published**: April 2007
- **Authors**: Zhongfeng Wang, Zhiqiang Cui
- **PDF**: https://ieeexplore.ieee.org/document/4162517
- **Abstract**: This paper presents a memory efficient partially parallel decoder architecture suited for high rate quasi-cyclic low-density parity-check (QC-LDPC) codes using (modified) min-sum algorithm for decoding. In general, over 30% of memory can be saved over conventional partially parallel decoder architectures. Efficient techniques have been developed to reduce the computation delay of the node processing units and to minimize hardware overhead for parallel processing. The proposed decoder architecture can linearly increase the decoding throughput with a small percentage of extra hardware. Consequently, it facilitates the applications of LDPC codes in area/power sensitive high-speed communication systems

## Approximately Lower Triangular Ensembles of LDPC Codes With Linear Encoding Complexity

- **Status**: ✅
- **Reason**: ALT 앙상블로 LDPC 선형시간 인코딩 가능케 하는 신규 구성; 코드설계(E) 이식 가능, 애매시 in
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4137883
- **Type**: journal
- **Published**: April 2007
- **Authors**: Shay Freundlich, David Burshtein, Simon Litsyn
- **PDF**: https://ieeexplore.ieee.org/document/4137883
- **Abstract**: The complexity of brute-force encoding of low-density parity-check (LDPC) codes is proportional to the square value of the block length. Richardson and Urbanke have proposed efficient encoding algorithms for LDPC codes. These algorithms permute the parity-check matrix of the code iteratively, such that it becomes approximately lower triangular. We propose a new approach for efficient encoding of LDPC codes in which we modify the code ensemble to force an approximate lower triangular structure, thus eliminating the need to apply the algorithms of Richardson and Urbanke in this ensemble. We prove that the new ensemble has the same asymptotic threshold as the corresponding standard ensemble. The new ensemble can be used for linear time encoding of an arbitrary code profile. Computer simulations confirm that the performances of the standard and new ensembles are also very similar when using finite length codes

## High-Rate Quasi-Cyclic Low-Density Parity-Check Codes Derived From Finite Affine Planes

- **Status**: ✅
- **Reason**: 유한 아핀평면 기반 고율 QC-LDPC 신규 구성+최소거리/랭크 분석 → E(코드설계) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4137888
- **Type**: journal
- **Published**: April 2007
- **Authors**: Norifumi Kamiya
- **PDF**: https://ieeexplore.ieee.org/document/4137888
- **Abstract**: This paper shows that several attractive classes of quasi-cyclic (QC) low-density parity-check (LDPC) codes can be obtained from affine planes over finite fields. One class of these consists of duals of one-generator QC codes. Presented here for codes contained in this class are the exact minimum distance and a lower bound on the multiplicity of the minimum-weight codewords. Further, it is shown that the minimum Hamming distance of a code in this class is equal to its minimum additive white Gaussian noise (AWGN) pseudoweight. Also discussed is a class consisting of codes from circulant permutation matrices, and an explicit formula for the rank of the parity-check matrix is presented for these codes. Additionally, it is shown that each of these codes can be identified with a code constructed from a constacyclic maximum distance separable code of dimension $2$. The construction is similar to the derivation of Reed–Solomon (RS)-based LDPC codes presented by Chen  and Djurdjevic  Experimental results show that a number of high rate QC-LDPC codes with excellent error performance are contained in these classes.

## Accumulate-Repeat-Accumulate Codes

- **Status**: ✅
- **Reason**: ARA 부호 protograph 구성 + BP 디코딩, LDPC 서브클래스 — 이식 가능 코드설계(E)/디코더(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4155107
- **Type**: journal
- **Published**: April 2007
- **Authors**: Aliazam Abbasfar, Dariush Divsalar, Kung Yao
- **PDF**: https://ieeexplore.ieee.org/document/4155107
- **Abstract**: In this paper, we propose an innovative channel coding scheme called accumulate-repeat-accumulate (ARA) codes. This class of codes can be viewed as serial turbo-like codes or as a subclass of low-density parity check (LDPC) codes, and they have a projected graph or protograph representation; this allows for high-speed iterative decoding implementation using belief propagation. An ARA code can be viewed as precoded repeat accumulate (RA) code with puncturing or as precoded irregular repeat accumulate (IRA) code, where simply an accumulator is chosen as the precoder. The amount of performance improvement due to the precoder will be called precoding gain. Using density evolution on their associated protographs, we find some rate-1/2 ARA codes, with a maximum variable node degree of 5 for which a minimum bit SNR as low as 0.08 dB from channel capacity threshold is achieved as the block size goes to infinity. Such a low threshold cannot be achieved by RA, IRA, or unstructured irregular LDPC codes with the same constraint on the maximum variable node degree. Furthermore, by puncturing the inner accumulator, we can construct families of higher rate ARA codes with thresholds that stay close to their respective channel capacity thresholds uniformly. Iterative decoding simulation results are provided and compared with turbo codes. In addition to iterative decoding analysis, we analyzed the performance of ARA codes with maximum-likelihood (ML) decoding. By obtaining the weight distribution of these codes and through existing tightest bounds we have shown that the ML SNR threshold of ARA codes also approaches very closely to that of random codes. These codes have better interleaving gain than turbo codes

## Results on the Improved Decoding Algorithm for Low-Density Parity-Check Codes Over the Binary Erasure Channel

- **Status**: ✅
- **Reason**: BEC용 개선 디코딩 알고리즘: stopping set guessing + Tanner 그래프 조작 — 이식 가능 디코더 기법(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4137902
- **Type**: journal
- **Published**: April 2007
- **Authors**: Badri N. Vellambi, Faramarz Fekri
- **PDF**: https://ieeexplore.ieee.org/document/4137902
- **Abstract**: In this correspondence, we first investigate some analytical aspects of the recently proposed improved decoding algorithm for low-density parity-check (LDPC) codes over the binary erasure channel (BEC). We derive a necessary and sufficient condition for the improved decoding algorithm to successfully complete decoding when the decoder is initialized to guess a predetermined number of guesses after the standard message-passing terminates at a stopping set. Furthermore, we present improved bounds on the number of bits to be guessed for successful completion of the decoding process when a stopping set is encountered. Under suitable conditions, we derive a lower bound on the number of iterations to be performed for complete decoding of the stopping set. We then present a superior, novel improved decoding algorithm for LDPC codes over the binary erasure channel (BEC). The proposed algorithm combines the observation that a considerable fraction of unsatisfied check nodes in the neighborhood of a stopping set are of degree two, and the concept of guessing bits to perform simple and intuitive graph-theoretic manipulations on the Tanner graph. The proposed decoding algorithm has a complexity similar to previous improved decoding algorithms. Finally, we present simulation results of short-length codes over BEC that demonstrate the superiority of our algorithm over previous improved decoding algorithms for a wide range of bit error rates

## A Measure of the Girth Histogram for Improved Girth-Conditioning Construction of LDPC Codes

- **Status**: ✅
- **Reason**: girth 히스토그램 측도 + girth-conditioning 구성 알고리즘 — 신규 바이너리 LDPC 코드설계 기법(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4155636
- **Type**: journal
- **Published**: April 2007
- **Authors**: Hua Chen, Zhigang Cao
- **PDF**: https://ieeexplore.ieee.org/document/4155636
- **Abstract**: In this letter, we present a general quantitative measure of the girth histogram of low-density parity-check (LDPC) codes with joint consideration of the degrees and local girths of symbol nodes. We then propose a further girth-conditioning algorithm to optimize such a measure during the construction of LDPC codes. We show by simulation results that the algorithm improves not only the performance of irregular codes at high signal-to-noise ratios (SNR) considerably, but also the rates of regular codes

## Design of Rate-Compatible Irregular Repeat-Accumulate Codes

- **Status**: ✅
- **Reason**: RC-IRA(LDPC 서브클래스) puncturing/extending 설계 + density evolution — 이식 가능 바이너리 코드설계(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4155112
- **Type**: journal
- **Published**: April 2007
- **Authors**: 
- **PDF**: https://ieeexplore.ieee.org/document/4155112
- **Abstract**: We consider the design of efficient rate-compatible (RC) irregular repeat-accumulate (IRA) codes over a wide code-rate range. The goal is to provide a family of RC codes to achieve high throughput in hybrid automatic repeat request (ARQ) scheme for highspeed data packet wireless systems. As a subclass of low-density parity-check (LDPC) codes, IRA codes have an extremely simple encoder and a low-complexity decoder, while providing capacity-approaching performance. We focus on a hybrid design method which employs both puncturing and extending. We propose a simple puncturing method based on minimizing the maximal recoverable step of the punctured nodes. We also propose a new extending scheme for IRA codes by introducing the degree-1 parity bits for the lower rate codes, and obtaining the optimal proportions of extended nodes through density evolution analysis. The throughput performance of the designed RC-IRA codes in hybrid ARQ is evaluated for both additive white Gaussian noise and block fading channels. Simulation results demonstrate that on designed RC codes offer good error-correction performance over a wide rate range and provide high throughput, especially in the high and low signal-to-noise ratio regions.

## A Power-Saved 1Gbps Irregular LDPC Decoder based on Simplified Min-Sum Algorithm

- **Status**: ✅
- **Reason**: simplified min-sum 기반 fully-parallel LDPC 디코더 HW + 조기종료 저전력 전략, 이식 가능 HW(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4239411
- **Type**: conference
- **Published**: 25-27 Apri
- **Authors**: Qi WANG, Kazunori SHIMIZU, Takeshi IKENAGA +1
- **PDF**: https://ieeexplore.ieee.org/document/4239411
- **Abstract**: In this paper we proposed a fully-parallel irregular LDPC decoder which uses only registers to store the temporary intrinsic messages. Our decoder adopts a simplified min-sum algorithm to reduce the hardware implementation complexity and area, and due to the factor modification we achieve a negligible performance loss compared with the general min-sum algorithm. Considering reducing the power consumption, we also propose a power-saved strategy according to which the message evolution will halt as the parity-check condition is satisfied. This strategy will save us higher than 50% power under good channel condition. The synthesis result in 0.18 mum CMOS technology shows our decoder for (648,540) irregular LDPC code achieves high throughput (1 Gbps) with 9.0 ns latency.

## Weighted IS Method of Estimating FER of LDPC Codes in High SNR Region

- **Status**: ✅
- **Reason**: trapping set 기반 high-SNR FER 추정(importance sampling), error floor/dominant TS 분석 기법은 NAND LDPC 신뢰성 평가에 이식 가능(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4196284
- **Type**: conference
- **Published**: 22-28 Apri
- **Authors**: Guangwen Li, Guangzeng Feng
- **PDF**: https://ieeexplore.ieee.org/document/4196284
- **Abstract**: In this paper, one improved frame error rate (FER) estimation approach in high Signal Noise Ratio (SNR) region for low-density parity-check (LDPC) codes is reported. Firstly dominant trapping sets (TSs), accounting for most of FER in high SNR region, are picked out as decoding result, with input of decoder consisting of a group of biased bits. And how those biased bits are chosen is reduced to finding solution to an binary integer program. Then decoder termination conditions are slightly modified so that history of the tentative decoding could facilitate action of searching for dominant TSs effectively. Without no prior knowledge of shape of error regions for specific LDPC code, we implement weighted mean translation (MT) of importance sampling (IS) method to compute FER in high SNR region. Simulation results demonstrate estimated FER curve conforms well with that of standard monte carlo (MC) simulation in overlapped SNR region.

## Quantitative Evaluation of Low Density Parity Check Convolutional Code Encoder and Decoder Algorithms for the XInC MIMD Multithreaded Microprocessor

- **Status**: ✅
- **Reason**: LDPC-CC 병렬 인코더/디코더 알고리즘+메모리 기반 디코더 아키텍처를 멀티스레드 프로세서에 구현, HW/병렬화 기법 이식 가능(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:4233002
- **Type**: conference
- **Published**: 22-26 Apri
- **Authors**: Xin Sheng Zhou, Bruce Cockburn, Stephen Bates
- **PDF**: https://ieeexplore.ieee.org/document/4233002
- **Abstract**: In this paper, we introduce low density parity check convolutional code (LDPC-CC) parallel encoder and decoder algorithms for the XInC MIMD multi-threaded microprocessor. A modified memory-based decoder architecture and an interleaved LDPC-CC code scheme are also proposed. Extensions and simple modifications to the current XInC microprocessor are proposed to decrease the number of instruction cycles per decoded bit. A XInC emulator was built to evaluate and quantify the hardware utilization and performance benefits of these modifications and other alternatives.

## Effective Puncturing Schemes for Block-type Low-Density Parity-Check Codes

- **Status**: ✅
- **Reason**: block-type 이진 QC-LDPC(802.16e)용 rate-compatible puncturing 기법 — 바이너리 LDPC 코드 설계로 이식 가능(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4212810
- **Type**: conference
- **Published**: 22-25 Apri
- **Authors**: Sunghoon Choi, Youchul Shin, Jun Heo +2
- **PDF**: https://ieeexplore.ieee.org/document/4212810
- **Abstract**: In this paper, a puncturing method for block-type rate-compatible low-density parity-check (LDPC) codes with 'good' performance is proposed. Puncturing is a scheme to obtain a series of higher rate codes from a low rate mother code. It is widely used in channel coding but it causes performance loss compared with non-punctured error correcting codes at the same rate. There have been many researches about puncturing to reduce the performance loss. However, these researches are not optimized for specific types such as block-type LDPC (B-LDPC) codes adopted in IEEE 802.16e standards. B-LDPC codes are constructed as irregular quasi-cyclic LDPC (QC-LDPC) codes for reduced required memory size and efficient encoding. In this paper, we suggest a modified puncturing scheme which is optimized for B-LDPC codes and compare the performance with previous scheme.

## A Stopping Criterion for Low-Density Parity-Check Codes

- **Status**: ✅
- **Reason**: BP 디코딩 중 satisfied parity-check 변화로 디코딩 실패 예측하는 정지 기준, 반복 절감·전력 절감 기법 NAND LDPC 디코더에 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4212747
- **Type**: conference
- **Published**: 22-25 Apri
- **Authors**: Donghyuk Shin, Kyoungwoo Heo, Sangbong Oh +1
- **PDF**: https://ieeexplore.ieee.org/document/4212747
- **Abstract**: Low-density parity-check (LDPC) codes have an inherent stopping criterion, parity-check constraints (equations). By testing the parity-check constraints, an LDPC decoder can detect successful decoding and stop their decoding, which is, however, not possible with turbo codes. In this paper, we propose a stopping criterion to predict decoding failure of LDPC codes, instead of detecting successful decoding. If the decoder predicts the decoding failure in advance, the receiver can more rapidly response to the transmitter and request for additional parity bits with an automatic repeat request (ARQ) protocol, which reduces overall system latency. The receiver can also save power consumption by avoiding unnecessary decoder iterations. The proposed stopping criterion makes use of the variations of the number of satisfied parity-check constraints in the belief-propagation (BP) decoding which is always tested in the conventional BP decoding to detect successful decoding. Thus, the proposed stopping criterion does not require any additional complexity. The counting of satisfied parity-check constraints shows behaviors of the BP decoding, which comes, otherwise, from the observations of changes of log-likelihood ratio (LLR) values in multi-bit resolution with additional complexity.

## On the Addition of an Input Buffer to an Iterative Decoder for LDPC Codes

- **Status**: ✅
- **Reason**: HW 디코더 아키텍처(입력 버퍼+stopping rule로 가변 반복 처리량 향상)는 NAND LDPC 디코더에 이식 가능 (D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:4212841
- **Type**: conference
- **Published**: 22-25 Apri
- **Authors**: Massimo Rovini, Alfonso Martinez
- **PDF**: https://ieeexplore.ieee.org/document/4212841
- **Abstract**: This paper describes the application of a new hardware architecture to the design of a decoder for low-density parity-check (LDPC) codes. Thanks to the systematic use of the built-in stopping rule in the decoder, the decoder runs the minimum number of iterations on each packet of received data. The addition of a small buffer on the decoder input allows the exploitation of the variations in the decoding time of different packets, in a spirit similar to statistical multiplexing of the data flow. Analysis and simulations are presented using the decoder for the next generation satellite digital video broadcasting (DVB-S2) as a case study, to show that the throughput may be doubled with only two extra buffer locations, at almost no cost in chip area.

## Low Complexity LDPC Decoding Techniques with Adaptive Selection of Edges

- **Status**: ✅
- **Reason**: 신뢰도 기반 비트노드 선택적 사용으로 BP 복잡도 저감하는 디코더 변형, NAND LDPC에 이식 가능 (C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4212883
- **Type**: conference
- **Published**: 22-25 Apri
- **Authors**: Kwangho Shin, Jungwoo Lee
- **PDF**: https://ieeexplore.ieee.org/document/4212883
- **Abstract**: In this paper, we propose low complexity LDPC decoding algorithms with variable number of edges. The main idea of this paper is to use the bit nodes selectively instead of using all the connected bit nodes. The proposed algorithms choose the bit node selectively when calculating the check node update equation. First, we study the relationship between the number of bit nodes for updating check node and the performance of the BP decoding algorithm. Two selective algorithms are proposed accordingly. The first algorithm (algorithm 1) does not use the bit nodes whose values are highly reliable when calculating the check node update equation. In the second algorithm (algorithm 2), we increase the number of bit nodes to update check node each time we have a decoding failure. These two algorithms have lower complexity with small performance degradation compared to the LLR-BP based decoding algorithm. These algorithms reduce the computational complexity at high SNR more than they do at low SNR.

## A New Wireless Access Scheme: Novel Punctured LDPC Coded Ultra-wideband System

- **Status**: ✅
- **Reason**: 변수노드 차수 기반 punctured LDPC 최적화로 puncturing fraction 최대화하는 코드설계 기법, 이식 가능 (E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4213045
- **Type**: conference
- **Published**: 22-25 Apri
- **Authors**: Fangni Chen, Shiju Li, Yanbo Wang
- **PDF**: https://ieeexplore.ieee.org/document/4213045
- **Abstract**: Ultra-wideband (UWB) technology has attracted much attention in high speed indoor wireless communications. UWB communications have transmitted power limitations according to FCC regulation. To face this drawback, while still maintaining significant error correction capabilities, we propose a novel punctured low-density parity-check (LDPC) coding scheme for multiband OFDM (orthogonal frequency division multiplexing) UWB systems in this paper. Different from the randomly punctured coding, we puncture the variable nodes on their degrees. We fix the target SNR threshold of the punctured code and optimize (maximize) the puncturing fraction for that threshold. From our analysis and numerical results, we find that this new scheme gives a significant performance gain compared with the randomly punctured scheme.

## A Survey on LDPC Codes and Decoders for OFDM-based UWB Systems

- **Status**: ✅
- **Reason**: 서베이지만 ultra-sparse 신규 LDPC 코드 설계+65nm HW 합성 비교 제시 — 신규 구성/HW 기여로 예외 포함(D/E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4212751
- **Type**: conference
- **Published**: 22-25 Apri
- **Authors**: Torben Brack, Matthias Alles, Timo Lehnigk-Emden +4
- **PDF**: https://ieeexplore.ieee.org/document/4212751
- **Abstract**: Current UWB systems apply convolutional codes as their channel coding scheme. For next generation systems LDPC codes are in discussion due to their outstanding communications performance. LDPC codes are already utilized in the new WiMax and WiFi standards. Thus it is reasonable to investigate these codes as candidate LDPC codes for UWB. In this paper the authors present an implementation complexity and performance comparison of LDPC decoders. We will show that it is of great advantage to design new LDPC codes which are tailored to the special latency and throughput constraints of upcoming UWB systems. This new class of LDPC codes is named ultra-sparse LDPC codes. Synthesis results of WiMax, WiFi, and U-S LDPC decoders are presented based on an enhanced 65 nm CMOS process. We show that the implementation complexity of the new U-S LDPC decoders is 55% smaller, utilizing only 0.2 mm2 instead of over 0.4 mm2, while the communications performance of all observed LDPC codes are almost identical under all the considered UWB simulation conditions.

## Modification on the IPEG Algorithm for Constructing LDPC Codes with Low Error Floor

- **Status**: ✅
- **Reason**: IPEG 변형으로 stopping set 줄여 error floor 개선하는 바이너리 코드 설계 기법 (E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4212885
- **Type**: conference
- **Published**: 22-25 Apri
- **Authors**: Sung-Ha Kim, Joon-Sung Kim, Dae-Son Kim +1
- **PDF**: https://ieeexplore.ieee.org/document/4212885
- **Abstract**: We propose a modification on the improved progressive-edge-growth(IPEG) algorithm. Proposed modification increases the connectivity of variable nodes using extrinsic message degree of variable nodes, which results in reducing the small stopping sets. Through computer simulation, we confirm that the codes constructed by the proposed algorithm have lower error floor than those constructed by the original IPEG algorithm.

## A Hardware Efficient LDPC Encoding Scheme for Exploiting Decoder Structure and Resources

- **Status**: ✅
- **Reason**: QC-LDPC 인코더/디코더 HW 자원 공유 효율적 인코딩 구조로 NAND LDPC HW에 이식 가능 (D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:4212932
- **Type**: conference
- **Published**: 22-25 Apri
- **Authors**: Chanho Yoon, Jong-Ee Oh, Minho Cheong +1
- **PDF**: https://ieeexplore.ieee.org/document/4212932
- **Abstract**: Previously, there has been no report on implementation effort to integrate LDPC encoder and decoder into a single hardware. In this paper, we propose a simple yet low complex systematic LDPC encoding method for class of quasi-cyclic low-density parity-check (QC-LDPC) codes to let LDPC encoder acquire an interchangeable structure, exploited in the decoder. With the proposed encoding scheme, implementation of the proposed encoder becomes much more hardware efficient than having a separate hardware due to LDPC encoder and decoder resource sharing. Moreover, the overall computational complexity of the proposed encoding scheme is lower than the well-known Richardson's efficient encoding scheme (A.T.J. Richardson and R.L. Urbanke, 2001).

## Optimized LDPC Codes for OFDM and Spread OFDM in Correlated Channels

- **Status**: ✅
- **Reason**: PEG/eIRA 단블록 LDPC를 density/differential evolution+girth conditioning으로 error floor 개선하는 바이너리 코드설계 (E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4212898
- **Type**: conference
- **Published**: 22-25 Apri
- **Authors**: Ali Serener, Balasubramaniam Natarajan, Don M. Gruenbacher
- **PDF**: https://ieeexplore.ieee.org/document/4212898
- **Abstract**: This paper analyzes optimized short block length low-density parity-check (LDPC) codes in spread OFDM systems that operate in frequency correlated Rayleigh fading channels. Extended irregular repeat-accumulate (eIRA) codes and codes constructed with progressive edge-growth (PEG) algorithm are optimized using density evolution and differential evolution techniques and any error floors are improved using girth conditioning. It is shown here that error floors in LDPC coded OFDM is lowered by introducing spreading on top of channel coding. It is also demonstrated that by using the distribution of the number of faded bits per OFDM symbol, the similarity in performance between codes in uncorrelated and correlated Rayleigh fading channels can be determined a priori.

## A Reliability-Aware LDPC Code Decoding Algorithm

- **Status**: ✅
- **Reason**: reliability-aware LDPC 디코딩 알고리즘 확장(결함 허용 디코더 구현) — 디코더 알고리즘/HW 개선으로 이식 가능(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4212750
- **Type**: conference
- **Published**: 22-25 Apri
- **Authors**: Matthias Alles, Torben Brack, Norbert Wehn
- **PDF**: https://ieeexplore.ieee.org/document/4212750
- **Abstract**: With the continuing downscaling of microelectronic technology, chip reliability becomes a great threat to the design of future complex microelectronic systems. Hence increasing the robustness of chip implementations in terms of tolerating errors becomes mandatory. In this paper we present reliability-aware extensions of the LDPC decoding algorithm. We exploit application specific fault tolerance of the decoding algorithm combined with modifications on the algorithmic level to increase the reliability of a decoder implementation. These modifications lead to a LDPC decoder implementation which tolerates sporadic errors that occur in critical components. To the best of our knowledge this is the first investigation of the LDPC decoding algorithm in terms of implementation reliability.

## Reduced Complexity and Improved Performance for Short Regular LDPC Codes Based on Select Updating Schedule

- **Status**: ✅
- **Reason**: select updating schedule 기반 수정 BP 디코딩 알고리즘 — 부호 비의존 디코더 개선이라 바이너리 LDPC BP에 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4212748
- **Type**: conference
- **Published**: 22-25 Apri
- **Authors**: Jianquan Liu, Youyun Xu, Yueming Cai
- **PDF**: https://ieeexplore.ieee.org/document/4212748
- **Abstract**: In this paper, we present a modified BP decoding algorithm based on select updating schedule by analyzing the properties of message-passing through cycles, we also proposed a concrete scheme to obtain the select updating schedule, the simulations prove that we could improve performance and reduce complexity at the same time for short regular LDPC codes which have a small difference between the maximal and minimal single bit node girths by select updating schedule compared with the conventional BP decoding algorithm.

## Non-fractional parallelism in LDPC Decoder implementations

- **Status**: ✅
- **Reason**: sub-circulant 메모리 공유 기반 non-fractional 병렬화로 면적 3배 개선하는 디코더 HW 기법(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:4211819
- **Type**: conference
- **Published**: 16-20 Apri
- **Authors**: John Dielissen, Andries Hekstra
- **PDF**: https://ieeexplore.ieee.org/document/4211819
- **Abstract**: Because of its excellent bit-error-rate performance, the low-density parity-check (LDPC) decoding algorithm is gaining increased attention in communication standards and literature. Also the new Chinese digital video broadcast standard (CDVB-T) uses LDPC codes. This standard uses a large prime number as the parallelism factor, leading to high area cost. This paper presents a new method to allow fractional dividers to be used. The method depends on the property that consecutive sub-circulants have one memory row in common. Several techniques are shown for assuring this property, or solving memory conflicts, making the method more generally applicable. In fact, the proposed technique is a first step towards a general purpose LDPC processor. For the CDVB-T decoder implementation the method leads to a factor 3 improvement in area

## Pipelined Implementation of a Real Time Programmable Encoder for Low Density Parity Check Code on a Reconfigurable Instruction Cell Architecture

- **Status**: ✅
- **Reason**: QC-LDPC H행렬 효율적 생성+파이프라인 인코더 HW(D). NAND 인코더에 이식 가능
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:4211821
- **Type**: conference
- **Published**: 16-20 Apri
- **Authors**: Zahid Khan, Tughrul Arslan
- **PDF**: https://ieeexplore.ieee.org/document/4211821
- **Abstract**: This paper presents pipelined implementation of a real time programmable irregular low density parity check (LDPC) encoder as specified in the IEEE P802.16E/D7 standard. The encoder is programmable for frame sizes from 576 to 2304 and for five different code rates. H matrix is efficiently generated and stored for a particular frame size and code rate. The encoder is implemented on reconfigurable instruction cell architecture which has recently emerged as an ultra low power, high performance, ANSI-C programmable embedded core. Different general and architecture specific optimization techniques are applied to enhance the throughput. With the architecture, a throughput from 10 to 19 Mbps has been achieved. The maximum throughput achieved with pipelining/multi-core is 78 Mbps

## Minimum-Energy LDPC Decoder for Real-Time Mobile Application

- **Status**: ✅
- **Reason**: 프레임별 필요 반복수 예측+DVFS로 디코더 에너지 절감 기법(C/D). 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4211820
- **Type**: conference
- **Published**: 16-20 Apri
- **Authors**: Weihuang Wang, Gwan Choi
- **PDF**: https://ieeexplore.ieee.org/document/4211820
- **Abstract**: This paper presents a low-power real-time decoder that provides constant-time processing of each frame using dynamic voltage and frequency scaling. The design uses known capacity-approaching low-density parity-check (LDPC) code to contain data over fading channels. Real-time applications require guaranteed data rates. While conventional fixed-number of decoding-iteration schemes are not energy efficient for mobile devices, the proposed heuristic scheme pre-analyzes each received data frame to estimate the maximum number of necessary iterations for frame convergence. The results are then used to dynamically adjust decoder frequency. Energy use is then reduced appropriately by adjusting power supply voltage to minimum necessary for the given frequency. The resulting design provides a judicious trade-off between power consumption and error level

## Low Complexity LDPC Code Decoders for Next Generation Standards

- **Status**: ✅
- **Reason**: 저복잡도 LDPC 디코더 아키텍처, 노드처리 근사+스케줄+65nm 합성(C/D). NAND 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4211818
- **Type**: conference
- **Published**: 16-20 Apri
- **Authors**: T. Brack, M. Alles, T. Lehnigk-Emden +6
- **PDF**: https://ieeexplore.ieee.org/document/4211818
- **Abstract**: This paper presents the design of low complexity LDPC codes decoders for the upcoming WiFi (IEEE 802.11n), WiMax (IEEE802.16e) and DVB-S2 standards. A complete exploration of the design space spanning from the decoding schedules, the node processing approximations up to the top-level decoder architecture is detailed. According to this search state-of-the-art techniques for a low complexity design have been adopted in order to meet feasible high throughput decoder implementations. An analysis of the standardized codes from the decoder-aware point of view is also given, presenting, for each one, the implementation challenges (multi rates-length codes) and bottlenecks related to the complete coverage of the standards. Synthesis results on a present 65nm CMOS technology are provided on a generic decoder architecture

## High-Throughput LDPC Decoders Using A Multiple Split-Row Method

- **Status**: ✅
- **Reason**: multi-split-row LDPC 디코더 CMOS 구현, 라우팅/처리량/면적 개선 이식가능 HW 아키텍처(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:4217333
- **Type**: conference
- **Published**: 15-20 Apri
- **Authors**: T. Mohsenin, B. M. Baas
- **PDF**: https://ieeexplore.ieee.org/document/4217333
- **Abstract**: We propose the "multi-split-row'" LDPC decoding method which allows further reductions in routing complexity, greater throughput, and smaller circuit area implementations compared to the previously proposed split-row decoding method. Multi-split-row is especially useful for regular high row weight LDPC codes. A 2048-bit full parallel decoder is implemented in a 0.18 μm CMOS technology using standard MinSum, split-row-2 and split-row-4 methods. The split-row-4 decoder delivers 7.1 Gbps throughput with 15 decoding iterations, and has 3.2 times smaller circuit area and 5.2 times higher throughput than the standard MinSum decoder.

## Memory Efficient LDPC Code Design for High Throughput Software Defined Radio (SDR) systems

- **Status**: ✅
- **Reason**: 아키텍처-aware LDPC 코드 설계로 메모리접근/반복수 최소화, 이식가능 HW친화 코드구성(D/E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4217332
- **Type**: conference
- **Published**: 15-20 Apri
- **Authors**: Yuming Zhu, Chaitali Chakrabarti
- **PDF**: https://ieeexplore.ieee.org/document/4217332
- **Abstract**: Low-density parity-check (LDPC) codes have been adopted in the physical layer protocol of many communication systems because of their superior performance. A direct implementation of the LDPC decoder on an existing platform, such as a software defined radio (SDR), is likely to be inefficient. Our approach is to design the LDPC code in a way that takes into account the constraints imposed by the existing architecture, without compromising the communication performance. In this paper, a procedure for architecture-aware LDPC code design which minimize the number of global memory accesses in a memory constrained system is derived. The procedure is built on top of existing super-code based LDPC code design. The proposed code construction procedure also results in reduction in the number of iterations and thereby increases the throughput significantly.
