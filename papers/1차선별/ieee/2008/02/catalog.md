# IEEE Xplore — 2008-02 (1차선별 통과)


## Enhanced Verification-Based Decoding for Packet-Based LDPC Codes

- **Status**: ✅
- **Reason**: 바이너리 LDPC verification-based 디코딩 알고리즘 개선(C), BP 디코더 변형으로 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4450667
- **Type**: journal
- **Published**: February 2
- **Authors**: Bin Zhu, Defeng Huang, Sven Nordholm
- **PDF**: https://ieeexplore.ieee.org/document/4450667
- **Abstract**: In this letter, an enhanced verification-based decoding algorithm (EVA) for packet level low-density parity-check (LDPC) codes is proposed. Compared with the verification algorithm (VA) in the literature, the proposed algorithm reduces the likelihood of false verification by enhancing the verification condition to achieve a better decoding performance. For example, simulation results in this letter show that EVA reduces frame error rate (FER) by two orders when comparing the VA over binary symmetric channel (BSC), while the increase of the computational load is less than 90%.

## On the Error Correction of Regular LDPC Codes Using the Flipping Algorithm

- **Status**: ✅
- **Reason**: 정규 바이너리 LDPC의 비트플리핑 디코딩 오류정정 능력 분석/개선(left degree 4까지 확장), 이식 가능 디코더 분석(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4439836
- **Type**: journal
- **Published**: Feb. 2008
- **Authors**: David Burshtein
- **PDF**: https://ieeexplore.ieee.org/document/4439836
- **Abstract**: The iterative bit flipping algorithm is applied to the standard regular low-density parity-check (LDPC) code ensemble. In the past, it was shown, for a typical code in the ensemble with left degree at least five and block length sufficiently large, that this algorithm can correct a linear (in the block length) number of worst case errors. In this paper, this result is extended to the case where the left degree is at least four. For the case where the left degree is larger than four, an improvement, compared to existing results, of several orders of magnitude is obtained on the fraction of worst case errors that can be corrected. It is also shown how the results can be further improved when random errors produced by the channel (as opposed to worst case errors) are considered.

## Design of systematic LDPC codes using density evolution based on tripartite graph

- **Status**: ✅
- **Reason**: systematic LDPC를 tripartite graph로 표현해 source/redundancy edge 분리 degree distribution 최적화 — 신규 코드설계(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4460838
- **Type**: conference
- **Published**: 30 Jan.-1 
- **Authors**: Jun Ning, Jinhong Yuan
- **PDF**: https://ieeexplore.ieee.org/document/4460838
- **Abstract**: In this paper we consider the design of systematic low-density parity-check (LDPC) codes using density evolution. We show that systematic LDPC codes can be well represented by tripartite graphs, where the edges in the code graph are divided into two types, source edges and redundancy edges. Using the tripartite code graph representation, we consider the degree distributions for source edges and redundancy edges separately. In particular, we discuss the necessary conditions for the two types of edges to be viewed as a single type in terms of specifying the LDPC codes properly. Then we discuss the relationship between the conventional bipartite graph representation and the tripartite graph representation. For the design of systematic LDPC codes, we show that the tripartite representation can specify the ensembles that are not available for the bipartite representation. Furthermore, we show that codes optimized by deploying the tripartite representation can achieve better performance with respect to the bipartite representation.

## LDPC decoder strategies for achieving low error floors

- **Status**: ✅
- **Reason**: trapping set 기반 커스텀 SPA 디코더로 error floor 낮춤(C) - NAND LDPC에 직접 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4601062
- **Type**: conference
- **Published**: 27 Jan.-1 
- **Authors**: Yang Han, William E. Ryan
- **PDF**: https://ieeexplore.ieee.org/document/4601062
- **Abstract**: One of the most significant impediments to the use of LDPC codes in many communication and storage systems is the error-rate floor phenomenon associated with their iterative decoders. The error floor has been attributed to certain subgraphs of an LDPC codepsilas Tanner graph induced by so-called trapping sets. We show in this paper that once we identify the trapping sets of an LDPC code of interest, a sum-product algorithm (SPA) decoder can be custom-designed to yield floors that are orders of magnitude lower than the conventional SPA decoder. We present three classes of such decoders: (1) a bi-mode decoder, (2) a bit-pinning decoder which utilizes one or more outer algebraic codes, and (3) three generalized-LDPC decoders. We demonstrate the effectiveness of these decoders for two codes, the rate-1/2 (2640,1320) Margulis code which is notorious for its floors and a rate-0.3 (640,192) quasi-cyclic code which has been devised for this study. Although the paper focuses on these two codes, the decoder design techniques presented are fully generalizable to any LDPC code.

## Buffering requirements for variable-iterations LDPC decoders

- **Status**: ✅
- **Reason**: 가변반복 LDPC 디코더의 버퍼링 요구량 분석 - 디코더 HW 스케줄링/스루풋 기법(D), NAND 디코더 이식 가능
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:4601025
- **Type**: conference
- **Published**: 27 Jan.-1 
- **Authors**: Sarah L. Sweatlock, Sam Dolinar, Kenneth Andrews
- **PDF**: https://ieeexplore.ieee.org/document/4601025
- **Abstract**: Low-density parity-check (LDPC) decoders, like iterative decoders for other block codes, can be designed to stop after a variable number of iterations, dependent on the difficulty of decoding particular noisy received words, also called frames. The number of iterations the decoder spends on a given frame determines both the probability of successful decoding, and the time expended. But whereas the speed of an LDPC decoder without a buffer is determined by its most difficult frames, the speed of a variable-iterations decoder with sufficient buffering approaches that determined by frames of average difficulty. It is relatively straightforward to analyze this as a D/G/1 queuing problem combined with empirically measured probability distributions of iteration counts for specific LDPC codes. Our analysis parallels that of other researchers, e.g., (J. Vogt and A. Finger, 2001), (G. Bosco et al., 2005), (M. Rovini and A. Martinez, 2007), and examines the resulting implications on LDPC decoder design choices. We find that a buffer large enough to hold only B = 2 or 3 additional frames is sufficient to achieve near optimal performance. We prove a strong monotonicity condition: not only does a variable-iterations decoder with buffer size B +1 frames outperform one with buffer size B in terms of average error rate, every single frame is guaranteed to receive at least as many iterations from the decoder with the larger buffer, if needed. Significantly, at low error rates, a variable-iterations decoder with buffer size B can keep pace with an input data rate B +1 times faster than a fixed-iterations decoder with the same processing speed.

## Interior-point algorithms for linear-programming decoding

- **Status**: ✅
- **Reason**: LP 디코딩용 interior-point 알고리즘 구현 - 이식 가능 디코더 기법(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4601085
- **Type**: conference
- **Published**: 27 Jan.-1 
- **Authors**: Pascal O. Vontobel
- **PDF**: https://ieeexplore.ieee.org/document/4601085
- **Abstract**: Interior-point algorithms constitute a very interesting class of algorithms for solving linear-programming problems. In this paper we study efficient implementations of such algorithms for solving the linear program that appears in the linear-programming decoder formulation.

## Can the storage capacity of memories built from unreliable components be determined?

- **Status**: ✅
- **Reason**: 불신뢰 소자 메모리의 코딩기반 신뢰성 저장; 스토리지 ECC 일반(B)에 근접, 애매하여 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4601020
- **Type**: conference
- **Published**: 27 Jan.-1 
- **Authors**: Shashi Kiran Chilappagari, Bane Vasic, Michael Marcellin
- **PDF**: https://ieeexplore.ieee.org/document/4601020
- **Abstract**: A memory is a device in which information is stored at some time and retrieved at a later time . Let the information be stored in form of bits in registers (memory elements) each of which can store a single bit. The information storage capability of a memory is the number of information bits it stores. Building a memory with information storage capability of k bits with reliable memory elements requires k registers. Such a memory is termed as an irredundant memory. This paper considers the problem of building a memory with memory elements and logic gates which fail according to a known random mechanism. The required minimum redundancy memory in which makes arbitrarily reliable information possible is discussed. For a reliable storage, the information needs to be stored in coded form . To ensure reliability, a correcting circuit is employed which performs error correction and updates the contents of the registers with an estimate of the original codeword.

## Large Girth Low-Density Parity-Check Codes for Long-Haul High-Speed Optical Communications

- **Status**: ✅
- **Reason**: large girth(girth-10) block-circulant LDPC 구성, error floor 개선 - 코드설계(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4528208
- **Type**: conference
- **Published**: 24-28 Feb.
- **Authors**: Ivan B. Djordjevic, Lei Xu, Ting Wang +1
- **PDF**: https://ieeexplore.ieee.org/document/4528208
- **Abstract**: An FEC scheme based on large girth LDPC codes is proposed. A girth-10 block-circulant LDPC code of rate 0.8 outperforms its turbo-product code counterpart by 0.95 dB at BER of 10-10, on an AWGN channel. It provides the net effective coding gain of 10.95 dB at BER of 10-12. In long-haul optical transmission at 40-Gb/s it provides at least 1.47 dB improvement over corresponding turbo-product code.

## Experimental Evaluation of High-Rate LDPC Codes for PMD Compensation by Turbo Equalization

- **Status**: ✅
- **Reason**: 고율(>0.9) block-circulant LDPC 설계+turbo equalization - QC-LDPC 코드설계(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4528090
- **Type**: conference
- **Published**: 24-28 Feb.
- **Authors**: Lyubomir L. Minkov, Ivan B. Djordjevic, Hussam G. Batshon +4
- **PDF**: https://ieeexplore.ieee.org/document/4528090
- **Abstract**: Several LDPC-codes with rate above 0.9 are proposed, and employed in PMD- compensation by LDPC-coded turbo-equalization. The block-circulant LDPC(15328,13893) is only 1.25 dB away from the channel-capacity limit for DGD of 125 ps (and NRZ transmission at 10- Gb/s).

## Efficient FEC for Optical Communications using Concatenated Codes to Combat Error-floor

- **Status**: ✅
- **Reason**: LDPC+RS 연접으로 error-floor 억제 코드설계 - 바이너리 LDPC error floor 기법(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4528592
- **Type**: conference
- **Published**: 24-28 Feb.
- **Authors**: Yoshikuni Miyata, Wataru Matsumoto, Hideo Yoshida +1
- **PDF**: https://ieeexplore.ieee.org/document/4528592
- **Abstract**: We propose concatenated LDPC(9252,7967)+RS(992,956) codes for application to systems beyond 40 Gb/s, taking practical implementation into account. Simulation shows that the Q limit is 7.1 dB, and that the concatenation effectively suppresses unwanted error-floor.

## A Systematic Optimized Comparison Algorithm for LDPC Decoder

- **Status**: ✅
- **Reason**: 신규 CNU 비교 알고리즘+디코더 아키텍처(짧은 지연/저복잡도 비교기)로 D 카테고리 HW 이식 가능
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:4494066
- **Type**: conference
- **Published**: 17-20 Feb.
- **Authors**: Jui-Hui Hung, Jui-Hung Hung, Sau-Gee Chen
- **PDF**: https://ieeexplore.ieee.org/document/4494066
- **Abstract**: This paper proposes a novel systematic optimized comparison algorithm for LDPC codes with arbitrary code lengths. Based on the presented algorithm, we also design a corresponding decoder architecture which has a short comparison delay time of lceillog2(n - 1)rceil and a very low comparator complexity of ntimeslceillog2(n - 1)rceil, where n is the input number to CNU. Besides, the proposed design is general, systematic and flexible, which can be applied to arbitrary input number of a CNU. The designed CNU is favorable to the existing CNU designs which are non-systematically designed with either longer critical path delays or higher comparator counts than the proposed designs. The proposed design is particularly good for long code length cases, when it is impractical to do customized optimized designs by hand, due to high design complexity.

## Edge Stream Oriented LDPC Decoding

- **Status**: ✅
- **Reason**: D. 스트림기반 Tanner 그래프 자료구조로 SPA/BP 디코딩 GPU 가속, 디코더 HW/병렬화 기법 이식 가능
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:4457129
- **Type**: conference
- **Published**: 13-15 Feb.
- **Authors**: Gabriel Falcao Paiva Fernandes, Vitor Manuel Mendes da Silva, Marco Alexandre Cravo Gomes +1
- **PDF**: https://ieeexplore.ieee.org/document/4457129
- **Abstract**: Low-Density Parity-Check (LDPC) codes are among the best error correcting codes known and have been adopted by data transmission standards, such as DVB-S2 or WiMax. They are based on binary sparse parity check matrices and usually represented by Tanner graphs. LDPC decoders require very intensive message-passing algorithms, also known as belief propagation. This paper proposes a very compact stream-based data structure to represent such a bipartite Tanner graph, which supports both regular and irregular codes. This compact data structure not only reduces the memory required to represent the graph but also puts it in an appropriate format to gather data into streams. This representation also allows to map the irregular processing behavior of the Sum Product Algorithm (SPA) used in LDPC decoding into the stream-based computing model. Stream programs were developed for LDPC decoding and the results show significant speedups obtained either using general purpose processors, or graphics processing units. The simultaneous decoding of several codewords was performed using the SIMD capabilities of modern stream-based architectures available on recent processing units.
