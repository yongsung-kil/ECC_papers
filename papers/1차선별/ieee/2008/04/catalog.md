# IEEE Xplore — 2008-04 (1차선별 통과)


## An Efficient Pseudocodeword Search Algorithm for Linear Programming Decoding of LDPC Codes

- **Status**: ✅
- **Reason**: LP 디코딩 pseudocodeword 탐색 알고리즘 — 바이너리 LDPC 디코더 분석/개선 기법(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4475359
- **Type**: journal
- **Published**: April 2008
- **Authors**: Michael Chertkov, Mikhail G. Stepanov
- **PDF**: https://ieeexplore.ieee.org/document/4475359
- **Abstract**: In linear programming (LP) decoding of a low-density parity-check (LDPC) code one minimizes a linear functional, with coefficients related to log-likelihood ratios, over a relaxation of the polytope spanned by the codewords. In order to quantify LP decoding it is important to study vertexes of the relaxed polytope, so-called pseudocodewords. We propose a technique to heuristcally create a list of pseudocodewords close to the zero codeword and their distances. Our pseudocodeword-search algorithm starts by randomly choosing configuration of the noise. The configuration is modified through a discrete number of steps. Each step consists of two substeps: one applies an LP decoder to the noise-configuration deriving a pseudocodeword, and then finds configuration of the noise equidistant from the pseudocodeword and the zero codeword. The resulting noise configuration is used as an entry for the next step. The iterations converge rapidly to a pseudocodeword neighboring the zero codeword. Repeated many times, this procedure is characterized by the distribution function of the pseudocodeword effective distance. The efficiency of the procedure is demonstrated on examples of the Tanner code and Margulis codes operating over an additive white Gaussian noise (AWGN) channel.

## Construction of quasi-cyclic LDPC codes from quadratic congruences

- **Status**: ✅
- **Reason**: 이차합동식 기반 신규 QC-LDPC 구성, 4-cycle 제거, 바이너리 — E 해당
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4489678
- **Type**: journal
- **Published**: April 2008
- **Authors**: Chun-Ming Huang, Jen-Fa Huang, Chao-Chin Yang
- **PDF**: https://ieeexplore.ieee.org/document/4489678
- **Abstract**: In this paper, we proposed a novel method for constructing quasi-cyclic low-density parity-check (QC-LDPC) codes based on circulant permutation matrices via a simple quadratic congruential equation. The main advantage is that QC-LDPC codes with a variety of block lengths and rates can be easily constructed with no cycles of length four or less. Simulation results show that the proposed QC-LDPC codes perform slight better than the random regular LDPC codes for short to moderate block lengths and have almost the same performance as Sridara-Fuja-Tanner codes.

## Transactions Letters - Random Redundant Iterative Soft-in Soft-out Decoding

- **Status**: ✅
- **Reason**: redundant Tanner graph 기반 iterative SISO 디코딩 — 임의 선형부호 적용 디코더 기법, 바이너리 LDPC BP 개선 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4489620
- **Type**: journal
- **Published**: April 2008
- **Authors**: Thomas R. Halford, Keith M. Chugg
- **PDF**: https://ieeexplore.ieee.org/document/4489620
- **Abstract**: This letter presents an iterative soft-in soft-out (SISO) decoding algorithm based on redundant Tanner graphs that is applicable to arbitrary linear block codes. The proposed algorithm utilizes the permutation group of a code in order to efficiently and randomly generate redundant parity-checks.

## High-performance scheduling algorithm for partially parallel LDPC decoder

- **Status**: ✅
- **Reason**: partially parallel LDPC 디코더용 overlapped message passing 스케줄링 알고리즘 — 이식 가능 HW/디코더 기법(C/D), 바이너리 LDPC
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4518325
- **Type**: conference
- **Published**: 31 March-4
- **Authors**: Cheng-Zhou Zhan, Xin-Yu Shih, An-Yeu Wu
- **PDF**: https://ieeexplore.ieee.org/document/4518325
- **Abstract**: In this paper, we propose a new scheduling algorithm for the overlapped message passing decoding, which can be applied to general low-density parity check (LDPC) codes. The partially parallel LDPC architecture is commonly used for reducing the area cost of the processing units. The dependency of two kinds of processing units, check node unit (CNU) and bit node unit (BNU), should be considered to enhance the hardware utilization efficiency (HUE). Based on the properties of the parity check matrix of LDPC codes, the updating calculation of the CNU and BNU can be overlapped to reduce the decoding latency by enhancing the HUE with the matrix scheduling algorithm. By applying our proposed LDPC scheduling algorithm to a (1944, 972)-irregular LDPC code, we can get about 60% throughput gain in average without any performance degradation.

## Using input/output queues to increase LDPC decoder performance

- **Status**: ✅
- **Reason**: BP LDPC 디코더에 입출력 큐로 throughput/성능 향상 — 이식 가능 디코더/HW 기법(C/D), 바이너리 PEG LDPC
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4493550
- **Type**: conference
- **Published**: 31 March-4
- **Authors**: Esa Alghonaim, Aiman El-Maleh, M. Adnan Landolsi
- **PDF**: https://ieeexplore.ieee.org/document/4493550
- **Abstract**: The paper presents a novel approach to increase the performance and/or throughput of iterative belief propagation (BP) decoding of low density parity check (LDPC) codes. The proposed approach is based on utilizing the decoder idle time by introducing two queue s: one at the decoder input and the other at the decoder output. At the presence of an input queue, the decoder runs extra iterations beyond the maximum allowable iterations as long as the input queue is not full. The function of the output queue is to preserve decoder timing, guaranteeing frames to be decoded within a fixed time similar to a conventional LDPC decoder, making it practical for real time applications. Simulation results for a rate ½ (1024,512) progressive edge-growth (PEG) LDPC code show that the proposed approach can increase the decoder performance up to 69% keeping the same throughput, or doubling the throughput while keeping performance almost the same.

## Design of block-structured LDPC codes for iterative receivers with soft sphere detection

- **Status**: ✅
- **Reason**: MIMO iterative receiver용 block-structured 바이너리 LDPC 코드 설계, EXIT chart 기반 — 이식 가능 코드설계(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4518204
- **Type**: conference
- **Published**: 31 March-4
- **Authors**: Predrag Radosavljevic, Joseph R. Cavallaro
- **PDF**: https://ieeexplore.ieee.org/document/4518204
- **Abstract**: In this paper we design block-structured LDPC codes for iterative MIMO receivers with soft sphere detection in particular channel environments. The receiver EXIT charts are used as a design tool. The main design constraint is to preserve the block-structure of parity-check matrices supporting modular semi-parallel decoder architectures. We show that newly designed block-structured code profiles provide improved error-rate performance of between 0.5 dB and 1 dB in different channel environments for moderate codeword size.

## A Hybrid ARQ Scheme Based on Shortened Low-Density Parity-Check Codes

- **Status**: ✅
- **Reason**: shortened LDPC 기반 HARQ + multi-edge type 코드 설계로 부호 구성·복잡도 개선, 바이너리 LDPC 코드설계(E) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4489051
- **Type**: conference
- **Published**: 31 March-3
- **Authors**: Toshihiko Okamura
- **PDF**: https://ieeexplore.ieee.org/document/4489051
- **Abstract**: This paper presents a hybrid ARQ (HARQ) scheme based on shortened low-density parity-check (LDPC) codes. Although conventional incremental redundancy HARQ (IR-HARQ) schemes based on punctured LDPC codes can achieve high throughput, puncturing slows the convergence of iterative decoding, and moreover, LDPC codes originally designed to be high-rate generally have lower decoding complexity for each iteration than low-rate codes. This makes computational complexity at high rates a problem for conventional IR-HARQ schemes. The proposed HARQ scheme uses a high-rate mother code: for a retransmission request, information bits are divided into smaller sub-blocks, and additional parity bits are generated for one of the sub-blocks to be used as a shortened form of the mother code. In order to achieve high throughput with the proposed HARQ scheme, it is necessary for the shortened codes of all the sub-blocks to perform well. A multi-edge type code-design is employed to construct irregular LDPC codes that meet this requirement. Simulation results show that the proposed HARQ scheme can achieve throughput comparable to that of a conventional IR-HAQR scheme over a wide range of signal-to-noise ratios and with lower computational complexity.

## Decoding on Graphs: LDPC-Coded MISO Systems and Belief Propagation

- **Status**: ✅
- **Reason**: 수정 Tanner 그래프로 검출+디코딩 통합 BP, 복잡도 저감 메시지패싱 기법은 BP 디코더(C)로 이식 검토 여지(애매->in)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4489053
- **Type**: conference
- **Published**: 31 March-3
- **Authors**: Amir H. Djahanshahi, Paul H. Siegel, Larry B. Milstein
- **PDF**: https://ieeexplore.ieee.org/document/4489053
- **Abstract**: This paper proposes a new approach for decoding LDPC codes over MISO channels. Since in an nT times 1 MISO system with a modulation of alphabet size 2M, nT transmitted symbols are combined and produce one received symbol at the receiver, we propose considering the LDPC-coded MISO system as an LDPC code over 2MnT-ary alphabet. Consequently, we propose a modified Tanner graph to introduce belief propagation for decoding MISO-LDPC systems. As a result, the MISO symbol detection and binary LDPC decoding steps are merged into a single message passing decoding. We also propose an efficient method that significantly reduces the complexity of belief propagation decoding in MISO-LDPC systems. Furthermore, we show that our proposed decoder outperforms the conventional decoder for short length LDPC codes in unknown channel scenarios.

## RECFEC: A Reconfigurable FEC Processor for Viterbi, Turbo, Reed-Solomon and LDPC Coding

- **Status**: ✅
- **Reason**: Viterbi/Turbo/RS/LDPC 재구성형 FEC 프로세서, LDPC 디코더 HW 아키텍처(D) 이식 가능
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:4489143
- **Type**: conference
- **Published**: 31 March-3
- **Authors**: Afshin Niktash, Hooman T. Parizi, Amir H. Kamalizad +1
- **PDF**: https://ieeexplore.ieee.org/document/4489143
- **Abstract**: RECFEC is a REConfigurable processor optimized for soft implementation of Forward Error Correction (FEC) algorithms. Viterbi, Turbo, Reed-Solomon and LDPC coding algorithms are widely used in wired and wireless standards. The implantation of these algorithms on RECFEC for a multi-mode wireless system is explored and performance metrics are demonstrated. RECFEC is comprised of a pool of processing elements, a processing element controller and memory. Each processing element encapsulates multiple functional units which are optimized for FEC algorithms. Memory includes the configuration and the data buffers. A high bandwidth interconnect network facilitates data movements. Unlike traditional approach to programmable FEC architectures, RECFEC supports multiple algorithms and is instruction-level programmable which results the ultimate flexibility and programmability.

## An FPGA architecture for low density parity check codes

- **Status**: ✅
- **Reason**: 동적 코드 선택 가능한 LDPC FPGA 아키텍처 — 이식 가능 HW(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:4494283
- **Type**: conference
- **Published**: 3-6 April 
- **Authors**: Orlando J. Hernandez, Nathaniel F. Blythe
- **PDF**: https://ieeexplore.ieee.org/document/4494283
- **Abstract**: Low density parity check (LDPC) codes are a family of linear block codes that can approach the Shannon limit to within less than a hundredth of a decibel, and along with Turbo codes are the codes of choice for all next- generation high-noise, high-rate communication systems. A generalized architecture is cost-prohibitive, and code- specific ASICs are not flexible enough for channels with dynamic noise parameters. In this paper we describe a field programmable gate array (FPGA) architecture for LDPC coding that allows for code-specific architectures while providing dynamic code selection. Gate and LUT counts in the encoder are examined for various codes, and size and timing results for different decoder parameters are compared.

## High throughput partially-parallel irregular LDPC decoder based on delta-value message-passing schedule

- **Status**: ✅
- **Reason**: D/C: delta-value message-passing 기반 partially-parallel irregular LDPC 디코더 아키텍처 — HW/디코더 기법 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4542452
- **Type**: conference
- **Published**: 23-25 Apri
- **Authors**: Wen Ji, Xing Li, Takeshi Ikenaga +1
- **PDF**: https://ieeexplore.ieee.org/document/4542452
- **Abstract**: In this paper, we propose a partially-parallel decoder architecture for irregular LDPC code targeting high throughput applications. The proposed decoder is based on a novel delta-value message-passing algorithm to facilitate the decoding throughput by removing redundant computations using the difference between the updated value and the original value. Techniques such as binary sorting, high performance pipelining are used to further speed up the message-passing procedure. The synthesis result in TSMC 0.18 CMOS technology shows that for (648,324) irregular LDPC code, our decoder can increase 8 times in throughput, which reaches 418 Mbps at the frequency of 200MHz.

## On the design of a superior irregular LDPC code

- **Status**: ✅
- **Reason**: 불규칙 LDPC 신규 코드설계(differential evolution+bit filling, 유한길이 N=1000 용량근접), 바이너리 코드설계 기법(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4632538
- **Type**: conference
- **Published**: 20-22 Apri
- **Authors**: Tolga Mataracioglu, Umit Aygolu
- **PDF**: https://ieeexplore.ieee.org/document/4632538
- **Abstract**: In this paper, low density parity check (LDPC) codes are considered. Design techniques are examined and new LDPC codes with improved error performance are proposed for irregular LDPC codes. Especially for BPSK modulation and AWGN channel, superior LDPC codes are successfully designed for R = 0.5 and N = 1000. For the designed superior irregular codes, it can be said that not only the performance of the codes is good when the code block length goes to infinity, but also they approach to the channel capacity and for code rate R = 0.5, they perform better than their counterparts given in the literature, when the code block length is finite (N = 1000). For irregular codes, when the degree of the bit node that possess the maximum number of branches is large, then that code approaches to the channel capacity. During the optimization of the encoder and decoder blocks, a combination of differential evolution technique, bit filling and message passing algorithms are considered to reach superior codes. The best superior code proposed in the paper is an irregular LDPC code with rate R = 0.5 which is only 0.02 dB away from the channel capacity.

## A New Powerful Scalable Generic Multi-Standard LDPC Decoder Architecture

- **Status**: ✅
- **Reason**: D. 확장형 멀티표준 병렬/모듈러 LDPC 디코더 아키텍처 FPGA 구현, NAND 디코더 HW에 이식 가능
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:4724931
- **Type**: conference
- **Published**: 14-15 Apri
- **Authors**: François Charot, Christophe Wolinski, Nicolas Fau +1
- **PDF**: https://ieeexplore.ieee.org/document/4724931
- **Abstract**: We propose a new powerful scalable generic parallel and modular architecture well suited to LDPC code decoding. This architecture template has been instantiated in the case of the 802.16e WiMax standard. The proposed design is fully compliant with all the code classes defined by the standard. It has been validated through an implementation on a Xilinx Virtex5 FPGA component. A four or six-module FPGA design yields a throughput ranging from 10 to 30 Mbit/s by means of 20 iterations at a clock frequency of 160 MHz which mostly satisfies communication throughput in the case of the WiMax mobile communication.
