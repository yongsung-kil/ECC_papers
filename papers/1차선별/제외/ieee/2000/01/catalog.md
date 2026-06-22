# IEEE Xplore — 2000-01


## Thresholds for turbo codes

- **Status**: ❌
- **Reason**: Turbo code threshold/concentration theory; pure non-LDPC bound analysis, no decoder/HW/code-design technique portable to binary LDPC BP.
- **ID**: ieee:866615
- **Type**: conference
- **Published**: 2000
- **Authors**: T. Richardson, R. Urbanke
- **PDF**: https://ieeexplore.ieee.org/document/866615
- **Abstract**: We prove the existence of thresholds for turbo codes and we prove concentration of the performance of turbo codes within the ensemble determined by the random interleaver. In effect, we show that the results obtained for low-density parity-check codes extend to turbo codes. The main technical innovation is to rigorously show that dependence of output extrinsic information on input priors decays with distance along the trellis. In an infinitely long turbo code the densities of the extrinsic information fulfill a certain symmetry condition which we call the consistency condition. This condition provides the basis for an efficient Monte-Carlo algorithm for the determination of thresholds for turbo codes. Thresholds of all symmetric parallel concatenated codes of memory up to 6 have been determined.

## One-shot Reed-Solomon decoding for high-performance dependable systems

- **Status**: ❌
- **Reason**: One-shot Reed-Solomon decoder ASIC for memory systems; non-LDPC algebraic code, RS-specific decoding, not portable to binary LDPC.
- **ID**: ieee:857567
- **Type**: conference
- **Published**: 2000
- **Authors**: Y. Katayama, S. Morioka
- **PDF**: https://ieeexplore.ieee.org/document/857567
- **Abstract**: This paper presents a scheme of ultra-fast one-shot Reed-Solomon decoding (prototyped (40-34,32,8) soft-IP demonstrating over 7 Gb/s using 0.35 /spl mu/m ASIC technology) and discusses its application to future dependable computer systems, taking a redundant array memory system as an example. We compare different memory configurations and identify improved fault-tolerance to single-bit failures as well as chip and card failures for smaller system overheads when random quad-byte one-shot Reed-Solomon decoding is used. We also discuss an alternative use of the powerful coding gain, i.e., an application to the dynamic refresh interval control of DRAMs, in order to optimize the refresh overheads in performance and power consumption. We believe that the one-shot Reed-Solomon decoding offers an advanced error correction capability for various parts of future high-performance computer systems, where system-level reliability can suffer because of rapidly increasing data size and speed.

## Watermark codes: reliable communication over insertion/deletion channels

- **Status**: ❌
- **Reason**: 삽입/삭제 채널용 watermark 블록코드(비-LDPC), 동기화 오류 정정 — 떼어낼 LDPC BP 기법 없음
- **ID**: ieee:866775
- **Type**: conference
- **Published**: 2000
- **Authors**: M. C. Davey, D. J. C. Mackay
- **PDF**: https://ieeexplore.ieee.org/document/866775
- **Abstract**: A new block code is introduced which is capable of correcting multiple insertion, deletion and substitution errors present in a single block. An inner code resilient to synchronisation errors provides soft inputs to an outer code capable of correcting substitution errors. The decoder does not require knowledge of the block boundaries.

## Vector symbol decoding with list inner symbol decisions

- **Status**: ❌
- **Reason**: vector symbol decoding(concatenated 외부코드, 신드롬 가우스-조던) — 비-LDPC, LDPC BP 이식성 없음
- **ID**: ieee:866779
- **Type**: conference
- **Published**: 2000
- **Authors**: J. J. Metzner
- **PDF**: https://ieeexplore.ieee.org/document/866779
- **Abstract**: Vector symbol decoding is an outer code decoding technique for a concatenated code which works with a (n-k)*r syndrome matrix S of n-k linear combinations of r-bit inner code symbol vectors. A Gauss-Jordan reduction provides an error location vector. The zeros in the error location vector are the apparent error positions, and the number of zeros should match the rank of S. Then the error values can be solved. Decoding success is related to the linear independence of error vectors. Data scrambling techniques for inner code symbols can make linear independence likely for moderately large r. Any parity check code structure can be used for the combination rules. The new result is that, if the outer code decoder has available a (possibly ordered) list of two or more alternative decisions for some or all inner symbols, a slightly modified vector symbol decoder automatically reveals most correct alternatives, allowing more powerful and often simpler correction. Moreover, the ability to recognize these alternatives does not require error vector linear independence. The main idea is to store differences between alternative choices and the first choice as additional rows below the syndrome matrix S.

## AWGN coding theorems from ensemble weight enumerators

- **Status**: ❌
- **Reason**: 앙상블 weight enumerator로 ML 오류 한계 유도 — 순수 이론 bound, 디코더/HW/구성으로 안 이어짐
- **ID**: ieee:866757
- **Type**: conference
- **Published**: 2000
- **Authors**: D. Divsalar, S. Dolinar, H. Jin +1
- **PDF**: https://ieeexplore.ieee.org/document/866757
- **Abstract**: We develop AWGN coding theorems for ensembles of codes for which we can calculate, or at least closely estimate, the ensemble weight enumerator. As a rule, for such an ensemble we can find a threshold c such that if E/sub b//N/sub 0/>c, then the ensemble maximum-likelihood error probability approaches zero. This threshold is always better, and usually much better, than can be obtained from the union bound. The role of low-weight code words is the key.

## Performance limits of concatenated codes with iterative decoding

- **Status**: ❌
- **Reason**: 연접부호(concatenated/turbo계열)의 SISO 반복디코딩 점근적 성능한계 이론 — 비-LDPC, 떼어낼 바이너리 LDPC BP 기법 없음(density propagation은 표준 DE 수준)
- **ID**: ieee:866442
- **Type**: conference
- **Published**: 2000
- **Authors**: S. Vialle, J. Boutros
- **PDF**: https://ieeexplore.ieee.org/document/866442
- **Abstract**: We present the performance limits of concatenated codes with interleaver of infinite size and under iterative decoding. We study the propagation of the probabilities at the output of the SISO decoder, and give a general formula for the density propagation through iterations.

## Content adaptive watermarking based on a stochastic multiresolution image modeling

- **Status**: ❌
- **Reason**: 웨이블릿 도메인 워터마킹 기법, 반복 ECC는 부수 언급 — 떼어낼 LDPC 디코더/구성 기법 없음
- **ID**: ieee:7075622
- **Type**: conference
- **Published**: 2000
- **Authors**: S. Voloshynovskiy, F. Deguillaume, T. Pun
- **PDF**: https://ieeexplore.ieee.org/document/7075622
- **Abstract**: In this paper, a wavelet domain robust watermarking technique for still images is presented. The proposed watermarking algorithm is based on 3 key aspects. First, message encoding is accomplished based on iterative error correction codes to reach channel capacity with reasonable decoder complexity. Secondly, watermark embedding is performed in the wavelet domain using a stochastically driven perceptual criterion to provide watermark invisibility. Thirdly, a new principle of watermark spatial allocation, based on the watermark magnitude spectrum, is proposed to recover from general affine geometrical distortions.

## On structure and decoding of product codes

- **Status**: ❌
- **Reason**: ML decoding of product codes via acyclic Tanner graphs and Wagner rule; product-code/parity-repetition specific, no portable binary-LDPC BP/construction technique.
- **ID**: ieee:866376
- **Type**: conference
- **Published**: 2000
- **Authors**: S. A. Miri, A. K. Khandani
- **PDF**: https://ieeexplore.ieee.org/document/866376
- **Abstract**: Product codes have been an effective coding method for communication channels where both random and burst error occur. We present a new approach to the structure and maximum likelihood (ML) decoding of product codes using Tanner (1981) graphs. For product codes having a sub-code which is a product of simple parity codes and repetition codes, we show how to obtain a sub-code with an acyclic Tanner graph and the largest possible distance. We show that in all cases of interest, a n-dimensional product code has such a structure. Wagner rule decoding is used on this sub-code and its cosets to obtain an effective and efficient maximum likelihood decoding of the given product code.

## Torbo decoding for high-rate concatenated parity-check codes on PRML channels

- **Status**: ❌
- **Reason**: 초록 없음(summary only)이나 제목상 concatenated parity-check + turbo decoding on PRML, 비-LDPC 부호 중심이며 떼어낼 바이너리 LDPC BP 기법 불명확
- **ID**: ieee:872295
- **Type**: conference
- **Published**: 2000
- **Authors**: H. Sawaguchi, J. K. Wolf
- **PDF**: https://ieeexplore.ieee.org/document/872295
- **Abstract**: Summary form only given. The complete presentation was not made available for publication as part of the conference proceedings.

## Parity-accumulate codes for magnetic recording

- **Status**: ❌
- **Reason**: 자기기록용 parity-accumulate 코드, 초록이 'summary form only'로 내용 없음 — 떼어낼 기법 확인 불가
- **ID**: ieee:872292
- **Type**: conference
- **Published**: 2000
- **Authors**: M. Oberg, H. D. Pfister, P. H. Siegel
- **PDF**: https://ieeexplore.ieee.org/document/872292
- **Abstract**: Summary form only given. The complete presentation was not made available for publication as part of the conference proceedings.

## Serial concatenated trellis coded modulation with rate-1 inner code

- **Status**: ❌
- **Reason**: 고차변조용 저복잡도 터보/RA 부호 설계, LDPC 행렬은 부수 언급이고 비-LDPC 변조·turbo 중심
- **ID**: ieee:891245
- **Type**: conference
- **Published**: 2000
- **Authors**: D. Divsalar, S. Dolinar, F. Pollara
- **PDF**: https://ieeexplore.ieee.org/document/891245
- **Abstract**: We develop new, low complexity turbo codes suitable for bandwidth and power limited systems, for very low bit and word error rate requirements. Motivated by the structure of previously discovered low complexity codes such as repeat-accumulate (RA) codes with low density parity check matrix, we extend the structure to high-level modulation such as 8PSK, and 16QAM. The structure consists of a simple 4-state convolutional or short block code as an outer code, and a rate-1, 2 or 4-state inner code. Two design criteria are proposed: the maximum likelihood design criterion, for short to moderate block sizes, and an iterative decoding design criterion for very long block sizes.

## Evaluation of low-density parity-check codes over block fading channels

- **Status**: ❌
- **Reason**: Evaluation of irregular LDPC over block-fading channels using standard decoding; performance study only, no new decoder/construction/HW to port (standard technique).
- **ID**: ieee:853686
- **Type**: conference
- **Published**: 2000
- **Authors**: M. Chiani, A. Conti, A. Ventura
- **PDF**: https://ieeexplore.ieee.org/document/853686
- **Abstract**: Richardson, Shokrollahi, Urbanke have proposed irregular low-density parity-check codes (LDPCCs) that outperform, on memoryless channels, the best known turbo-codes. These results have been obtained by allowing the degree of each node (variable or check) of a LDPCC to vary according to some distribution. In this paper we investigate the performance of such new codes over block fading channels (i.e. channels with memory), in terms of bit and codeword error rates adopting the standard decoding algorithm and a modified version which slightly improves performance. Also, a numerical comparison with conventional convolutional codes is carried out. For a code rate 1/2, it results that irregular LDPCCs are convenient only for large codeword size (greater than 500 bits), and that the gain with respect to a constraint length 7 convolutional code decreases considerably with the channel memory.

## Multiple serially concatenated single parity check codes

- **Status**: ❌
- **Reason**: Serially concatenated single-parity-check codes vs turbo/convolutional; non-LDPC concatenation, no portable binary-LDPC decoder/construction.
- **ID**: ieee:853569
- **Type**: conference
- **Published**: 2000
- **Authors**: J. S. K. Tee, D. P. Taylor
- **PDF**: https://ieeexplore.ieee.org/document/853569
- **Abstract**: Single parity check (SPC) codes are applied in a serial concatenation structure to produce a high performance coding scheme with very low complexity. We show a simple yet elegant way of improving the system performance at low bit error rates (BER), without changing the overall code parameters (code rate, code block length). We compare its BER performance to the best 64-state convolutional codes, and the 16-state turbo codes. Comparisons show that its performance is only slightly poorer. Despite this inferior performance, the scheme is very suitable for practical implementation due to its flexible code parameters. We conclude by showing that its decoding complexity is more than 1 order of magnitude less than that of a 16-state turbo code.

## Constructing low-density parity-check codes

- **Status**: ❌
- **Reason**: 표준 LDPC 구성+IBP 디코딩의 일반 통신 시스템 적용, 교과서 수준 구성으로 새 디코더·HW·코드설계 기여 없음
- **ID**: ieee:874812
- **Type**: conference
- **Published**: 2000
- **Authors**: J. W. Bond, S. Hui, H. Schmidt
- **PDF**: https://ieeexplore.ieee.org/document/874812
- **Abstract**: A low-density parity-check code (LDPCC) has been constructed for a block size of 10/sup 7/ that provides performance within 0.01 dB of Shannon's limit using iterative belief propagation (IBP) decoding. The LDPCC can be constructed for nearly any code rate and block size and encoding and IBP decoding is practical for many applications. We describe LDPCC and their decoding. We also illustrate the performance achievable for the codes by presenting performance results for rate 1/2 and 4/7 codes for a nominal 1000-bit block size. These codes will be used in an operational communication system.

## Iterative decoding of systematic binary algebraic block codes

- **Status**: ❌
- **Reason**: 이진 대수부호(Hamming)의 SPC-MAP 반복디코딩, 비-LDPC 부호 전용이며 바이너리 LDPC BP로의 이식 기여 불명확
- **ID**: ieee:891257
- **Type**: conference
- **Published**: 2000
- **Authors**: J. S. K. Tee, D. P. Taylor
- **PDF**: https://ieeexplore.ieee.org/document/891257
- **Abstract**: In this paper, MAP decoders for single parity check (SPC) codes are applied to the decoding of systematic binary algebraic block codes. We compare the performance of this decoding technique to hard decision syndrome decoding and soft decision brute force decoding. Simulation results are presented for the (7,4,3) and (15,11,3) Hamming codes in the AWGN and Rayleigh fading channels. Using a product (7,4,3) Hamming code, the proposed scheme is also compared to the dual code technique as described Berrou and Glavieux (see IEEE Trans. Communications, vol.44, no.10, p.1261-71, 1996). Although the BER performance is slightly inferior, the proposed scheme is much less complex to implement.

## Low complexity turbo space-time code for system with large number of antennas

- **Status**: ❌
- **Reason**: 다중안테나 space-time turbo 부호 설계, 무선 응용 특이적이며 떼어낼 LDPC ECC 기법 없음
- **ID**: ieee:891286
- **Type**: conference
- **Published**: 2000
- **Authors**: Leung Hang Ching Jason, R. S. Cheng
- **PDF**: https://ieeexplore.ieee.org/document/891286
- **Abstract**: We consider the design of a space-time code for a system with large number of antennas using a serial turbo code structure with a parity cheek code as the outer code under a quasistatic and independent Rayleigh fading environment. By studying the case with a large number of receive antennas, we have proven that interference between different transmit antennas vanishes as the number of receive antennas approaches infinity. The design of a code can then be largely simplified by dividing the antennas into groups, using a small space-time code on each group. An outer code is added to allow each information bit to fully utilize the full range of antenna diversity and to be benefited from all the space-time codes. Dividing the overall system into groups enables a trade off between complexity and performance. This scheme has been investigated for systems with 5 receive antennas and 2 or 4 transmit antennas. Simulation results showed that the system performance in terms of the frame error rate degrades only slightly when both the data rate and the number of transmit antennas are doubled while keeping the received energy per bit at the receiver constant.

## Bounds on the maximum likelihood decoding error probability of low density parity check codes

- **Status**: ❌
- **Reason**: 바이너리 LDPC 앙상블의 ML 디코딩 오류확률 상하한·error exponent 순수 이론 bound — 디코더/HW/구성으로 안 이어짐
- **ID**: ieee:866588
- **Type**: conference
- **Published**: 2000
- **Authors**: G. Miller, D. Burshtein
- **PDF**: https://ieeexplore.ieee.org/document/866588
- **Abstract**: We derive bounds on the error probability of ML decoded LDPC (low density parity check) codes, for any binary-input symmetric-output channel. For appropriately chosen ensembles of LDPC codes, reliable communication is possible up to channel capacity. The lower and upper bounds coincide asymptotically, indicating a polynomially decreasing ensemble averaged error probability. For ensembles with suitably chosen parameters, the error probability of almost all codes is exponentially decreasing. Furthermore, the error exponent can be set arbitrarily close to the standard random coding exponent.

## Fault-tolerant dynamic systems

- **Status**: ❌
- **Reason**: LDPC를 LFSM 결함허용에 응용 — 채널 ECC 디코더/HW/구성 기여 없음, 응용 특이적
- **ID**: ieee:866742
- **Type**: conference
- **Published**: 2000
- **Authors**: C. Hadjicostis, G. C. Verghese
- **PDF**: https://ieeexplore.ieee.org/document/866742
- **Abstract**: We use unreliable system replicas and unreliable voters to construct redundant dynamic systems that tolerate transient failures in their state transition and error correcting mechanisms. Using low density parity check (LDPC) codes, we develop a fault-tolerant scheme that efficiently protects linear finite state machines (LFSMs) with identical dynamics but distinct input sequences and states. The scheme achieves a probability of failure that remains below any given bound for any pre-specified (finite) time-interval using a constant amount of hardware (XOR gates and voters) per LFSM.

## Simple soft-output detection for magnetic recording channels

- **Status**: ❌
- **Reason**: 자기기록 ISI 채널용 soft-output 검출기 — LDPC는 부수 언급, 채널 검출기(detector) 기법이라 떼어낼 바이너리 LDPC ECC 기법 없음
- **ID**: ieee:866555
- **Type**: conference
- **Published**: 2000
- **Authors**: E. Soljanin
- **PDF**: https://ieeexplore.ieee.org/document/866555
- **Abstract**: Recent success of turbo-like coding schemes on memoryless channels has sparked interest in using them on intersymbol interference (ISI) channels. Decoders for turbo and low density parity check (LDPC) codes perform much better with soft input information which has to be supplied by the channel detector as its soft output. We consider a class of ISI channels commonly used to model magnetic recording channels in a wide range of linear recording densities, and show that simple soft output detectors are possible, since the channel transfer functions belong to a family of special polynomials.

## Sphere-bound-achieving coset codes and multilevel coset codes

- **Status**: ❌
- **Reason**: Coset/multilevel lattice codes for AWGN sphere bound; non-LDPC, pure information-theoretic, no portable binary-LDPC decoder/HW/construction technique.
- **ID**: ieee:841165
- **Type**: journal
- **Published**: 2000
- **Authors**: G. D. Forney, M. D. Trott, Sae-Young Chung
- **PDF**: https://ieeexplore.ieee.org/document/841165
- **Abstract**: A simple sphere bound gives the best possible tradeoff between the volume per point of an infinite array L and its error probability on an additive white Gaussian noise (AWGN) channel. It is shown that the sphere bound can be approached by a large class of coset codes or multilevel coset codes with multistage decoding, including certain binary lattices. These codes have structure of the kind that has been found to be useful in practice. Capacity curves and design guidance for practical codes are given. Exponential error bounds for coset codes are developed, generalizing Poltyrev's (1994) bounds for lattices. These results are based on the channel coding theorems of information theory, rather than the Minkowski-Hlawka theorem of lattice theory.

## The geometry of turbo-decoding dynamics

- **Status**: ❌
- **Reason**: turbo-decoding 동역학의 기하학적 해석 — 비-LDPC, 부호 비의존적 LDPC BP 이식 기여 불명확
- **ID**: ieee:817505
- **Type**: journal
- **Published**: 2000
- **Authors**: T. Richardson
- **PDF**: https://ieeexplore.ieee.org/document/817505
- **Abstract**: The spectacular performance offered by turbo codes sparked intense interest in them. A considerable amount of research has simplified, formalized, and extended the ideas inherent in the original turbo code construction. Nevertheless, the nature of the relatively simple ad hoc turbo-decoding algorithm has remained something of a mystery. We present a geometric interpretation of the turbo-decoding algorithm. The geometric perspective clearly indicates the relationship between turbo-decoding and maximum-likelihood decoding. Analysis of the geometry leads to new results concerning existence of fixed points, conditions for uniqueness, conditions for stability, and proximity to maximum-likelihood decoding.

## Generalized minimum distance decoding in Euclidean space: performance analysis

- **Status**: ❌
- **Reason**: GMD 디코딩(유클리드 공간 다중레벨 코드) 성능 분석 — 비-LDPC, LDPC BP 이식 기법 없음
- **ID**: ieee:817509
- **Type**: journal
- **Published**: 2000
- **Authors**: D. Agrawal, A. Vardy
- **PDF**: https://ieeexplore.ieee.org/document/817509
- **Abstract**: We present a detailed analysis of generalized minimum distance (GMD) decoding algorithms for Euclidean space codes. In particular, we completely characterize GMD decoding regions in terms of receiver front-end properties. This characterization is used to show that GMD decoding regions have intricate geometry. We prove that although these decoding regions are polyhedral, they are essentially always nonconvex. We furthermore show that conventional performance parameters, such as error-correction radius and effective error coefficient, do not capture the essential geometric features of a GMD decoding region, and thus do not provide a meaningful measure of performance. As an alternative, probabilistic estimates of, and upper bounds upon, the performance of GMD decoding are developed. Furthermore, extensive simulation results, for both low-dimensional and high-dimensional sphere-packings, are presented. These simulations show that multilevel codes in conjunction with multistage GMD decoding provide significant coding gains at a very low complexity. Simulated performance, in both cases, is in remarkably close agreement with our probabilistic approximations.

## A fast algorithm for determining the linear complexity of a sequence with period p/sup n/ over GF(q)

- **Status**: ❌
- **Reason**: GF(q) 수열 선형복잡도 알고리즘 — ECC/LDPC와 무관
- **ID**: ieee:868492
- **Type**: journal
- **Published**: 2000
- **Authors**: Guozhen Xiao, Shimin Wei, Kwok Yan Lam +1
- **PDF**: https://ieeexplore.ieee.org/document/868492
- **Abstract**: A fast algorithm is presented for determining the linear complexity of a sequence with period p/sup n/ over GF (q), where p is an odd prime, and where q is a prime and a primitive root (mod p/sup 2/).

## The super-trellis structure of turbo codes

- **Status**: ❌
- **Reason**: turbo codes의 super-trellis 구조/복잡도 — 비-LDPC, LDPC BP에 이식되는 부호비의존 기법 없음
- **ID**: ieee:868494
- **Type**: journal
- **Published**: 2000
- **Authors**: M. Breiling, L. Hanzo
- **PDF**: https://ieeexplore.ieee.org/document/868494
- **Abstract**: In this contribution we derive the super-trellis structure of turbo codes. We show that this structure and its associated decoding complexity depend strongly on the interleaver applied in the turbo encoder. We provide upper bounds for the super-trellis complexity. Turbo codes are usually decoded by an iterative decoding algorithm, which is suboptimum. Applying the super-trellis structure, we can optimally decode simple turbo codes and compare the associated bit-error rate results to those of iterative algorithms.

## A minimax robust decoding algorithm

- **Status**: ❌
- **Reason**: Minimax robust decoding for Viterbi/APP under noise-model mismatch; turbo/convolutional context, not binary-LDPC BP technique. Possible noise-variance-mismatch insight but tied to VA/APP, no portable LDPC contribution.
- **ID**: ieee:841200
- **Type**: journal
- **Published**: 2000
- **Authors**: Lei Wei, Zheng Li, M. R. James +1
- **PDF**: https://ieeexplore.ieee.org/document/841200
- **Abstract**: We study the decoding problem in an uncertain noise environment. If the receiver knows the noise probability density function (PDF) at each time slot or its a priori probability, the standard Viterbi (1967) algorithm (VA) or the a posteriori probability (APP) algorithm can achieve optimal performance. However, if the actual noise distribution differs from the noise model used to design the receiver, there can be significant performance degradation due to the model mismatch. The minimax concept is used to minimize the worst possible error performance over a family of possible channel noise PDFs. We show that the optimal robust scheme is difficult to derive; therefore, alternative, practically feasible, robust decoding schemes are presented and implemented on a VA decoder and two-way APP decoder. The performance analysis and numerical results show our robust decoders have a performance advantage over standard decoders in uncertain noise channels, with no or little computational overhead. Our robust decoding approach can also explain why for turbo decoding overestimating the noise variance gives better results than underestimating it.

## The feasibility of magnetic recording at 1 Terabit per square inch

- **Status**: ❌
- **Reason**: 자기기록 매체 물리적 한계(초상자성) 연구, 단순 패리티 검사만 부수 언급 — 떼어낼 LDPC ECC 기법 없음
- **ID**: ieee:824422
- **Type**: journal
- **Published**: 2000
- **Authors**: R. Wood
- **PDF**: https://ieeexplore.ieee.org/document/824422
- **Abstract**: This paper explores the feasibility of implementing conventional magnetic recording technology at densities up to one Terabit per square inch. The key limiting physical factor is the superparamagnetic effect (thermal stability) in the recording medium. Ambient thermal energy can cause the magnetic signals to decay. The requirement for thermal stability over periods of years dictates a lower limit to the size of magnetic grains (switching units) in the recording medium. To achieve the highest areal densities, it will be necessary to use a magnetic recording configuration capable of writing and storing data on very small magnetic grains together with a signal processing system capable of recovering data reliably when each bit is recorded on very few such grains. In addition to these physical effects, there are a number of practical engineering factors that must be considered: tolerances on the head geometry, reliability of head-disk interface, track-following accuracy. In an example system, we use a perpendicular recording configuration since it appears to offer some advantage in terms of maximizing the number of stable magnetic grains per unit area. The readback signals are processed by equalization to a simple binary eye followed by soft detection of a low-rate simple parity check code. The example system approaches a density of 1 Terabit per square inch and allows 3 dB of margin against thermal decay, adjacent track interference, etc.

## Cochannel interference suppression through time/space diversity

- **Status**: ❌
- **Reason**: Cochannel interference suppression via time/space diversity for wireless; decoders for repetition/convolutional/Reed-Muller, no LDPC technique to port.
- **ID**: ieee:841171
- **Type**: journal
- **Published**: 2000
- **Authors**: A. R. Calderbank, G. Pottie, N. Seshadri
- **PDF**: https://ieeexplore.ieee.org/document/841171
- **Abstract**: Wireless systems are subject to a time-varying and unknown a priori combination of cochannel interference, fading, and Gaussian noise. It is well known that multiple antennas can provide diversity in space that allows system tradeoffs between interference suppression and mitigation of fading. This paper describes how to achieve these same tradeoffs through diversity in time provided by channel coding. The mathematical description of time diversity is identical to that of space diversity, and what emerges is a unified framework for signal processing. Decoding algorithms are provided for repetition codes, rate 1/n convolutional codes, first-order Reed-Muller codes, and a new class of linear combination codes that provide cochannel interference suppression. In all cases it is possible to trade performance for complexity by choosing between joint estimation and a novel low-complexity linear canceler structure that treats interference as noise. This means that a single code can be used in a variety of system environments just by changing the processing in the receiver.

## Turbo decoding for high-rate concatenated parity-check codes on PRML channels

- **Status**: ❌
- **Reason**: PRML 채널 패리티검사 부호 터보(APP/BCJR) 디코딩 — 비-LDPC, 이식 가능 LDPC 기법 없음
- **ID**: ieee:908347
- **Type**: journal
- **Published**: 2000
- **Authors**: H. Sawaguchi, J. K. Wolf
- **PDF**: https://ieeexplore.ieee.org/document/908347
- **Abstract**: A simple turbo decoding scheme is proposed for partial-response (PR) channels by using high-rate parity-check codes as an outer error-correction code (ECC). The use of the simple parity codes enables a simplified and high-speed implementation of the a posterior probability (APP) decoder. Its key feature is an iterative decoding step for the parallel concatenation of two parity-check outer codes connected via an interleaver. The parity iterative decoding can provide the high-rate parity-check outer codes with superior correction capability for random error-events, so it can help to reduce the decoding latency. The combination of the serial turbo decoding for a modified E/sup 2/PR (ME/sup 2/PR) channel and the parity iterative decoding demonstrated a coding gain of 4-5 dB at a bit error rate of 1.0E-5 for a coding rate of 8/9.

## FIR parity check codes

- **Status**: ❌
- **Reason**: FIR parity-check codes for packet sync/error detection in cable TV; CRC-type cyclic dual, non-LDPC, no portable BP/HW technique.
- **ID**: ieee:855518
- **Type**: journal
- **Published**: 2000
- **Authors**: C. Heegard, A. J. King
- **PDF**: https://ieeexplore.ieee.org/document/855518
- **Abstract**: This paper describes a method for packet synchronization and error detection for use in a synchronous digital communications system. The method relies upon a class of linear block codes that have parity checks that are expressed in terms of a finite-impulse response (FIR) filter. This system is incorporated in the newly established ITU standard of digital cable television standard, J.83 appendix B, which is based on an MPEG 2 transport packet data stream. This technique is also the basis for cable modem downstream transmission defined in the IEEE 802.14 and MCNS standards. The parity check structure is based on a pseudonoise sequence generated by a (binary) primitive polynomial. This structure allows for a computationally efficient implementation of the parity check FIR filter, in a recursive manner, that is none the less self-synchronizing. The FIR parity check codes that are described are characterized as the dual of a CRC-type, shortened cyclic code. The theory and computational structure of these codes are presented here; the J.83R code is used as an example of the general theory.

## On Gallager's low-density parity-check codes

- **Status**: ❌
- **Reason**: Gallager LDPC의 weight distribution이 random-like임을 보이는 순수 이론 분석 — 디코더/HW/구성으로 이어지지 않는 이론적 성질
- **ID**: ieee:866500
- **Type**: conference
- **Published**: 2000
- **Authors**: G. Battail
- **PDF**: https://ieeexplore.ieee.org/document/866500
- **Abstract**: We show that low-density parity-check codes are random-like (i.e. their weight distribution resembles that obtained in the average density by random coding), and comment on this result.

## Using low density parity check codes in the McEliece cryptosystem

- **Status**: ❌
- **Reason**: LDPC를 McEliece 암호시스템에 적용 — 보안/암호 응용, 채널 ECC 디코더·코드설계 신규 기여 없음
- **ID**: ieee:866513
- **Type**: conference
- **Published**: 2000
- **Authors**: C. Monico, J. Rosenthal, A. Shokrollahi
- **PDF**: https://ieeexplore.ieee.org/document/866513
- **Abstract**: We examine the implications of using a low density parity check code (LDPCC) in place of the usual Goppa code in McEliece's cryptosystem. Using a LDPCC allows for larger block lengths and the possibility of a combined error correction/encryption protocol.

## Analytical approach to low-density convolutional codes

- **Status**: ❌
- **Reason**: 저밀도 컨볼루션 부호(LDC)의 free distance/ML 오류확률 이론 bound 중심 — SC-LDPC 변형이나 순수 이론 bound로 디코더/HW/구성 신규 기여 약함, 애매하나 turbo-like 컨볼루션 분석
- **ID**: ieee:866499
- **Type**: conference
- **Published**: 2000
- **Authors**: K. Engdahl, M. Lentmaier, D. V. Truhachev +1
- **PDF**: https://ieeexplore.ieee.org/document/866499
- **Abstract**: A statistical analysis of low-density convolutional (LDC) codes is performed. This analysis is based on the consideration of a special statistical ensemble of Markov scramblers and the solution to a system of recurrent equations describing this ensemble. The results of the analysis are lower bounds for the free distance of the codes and upper bounds for the maximum likelihood decoding error probability. For the case where the size of the scrambler tends to infinity some asymptotic bounds for the free distance and the error probability are derived. Simulation results for iterative decoding of LDC codes are also presented.

## Precoder design for concatenating convolutional codes with generalized partial response channels

- **Status**: ❌
- **Reason**: PR 채널+convolutional 외부부호 인터리버/프리코더 최적화, 비-LDPC 부호 중심이며 LDPC는 부수 언급
- **ID**: ieee:891956
- **Type**: conference
- **Published**: 2000
- **Authors**: A. Ghrayeb, W. E. Ryan
- **PDF**: https://ieeexplore.ieee.org/document/891956
- **Abstract**: A number of papers have recently been published on the concatenation of an outer code with a partial response (PR) channel, where the outer code is a turbo code, a convolutional code, or a low density parity check code. This paper deals with the second case assuming EPR4 and modified extended EPR4 (MEEPR4) partial response targets. The goal in this work is the joint optimization of interleaver and precoder for a fixed outer convolutional code and PR target. We introduce mathematical and algorithmic tools for accomplishing this goal and present simulation results which support our approach. Among the positive results is the ability to lower the well-known error rate floor of these concatenated schemes for arbitrary partial response channels.

## Iterative turbo decoder analysis based on Gaussian density evolution

- **Status**: ❌
- **Reason**: 터보 디코더 가우시안 density evolution 분석 — 비-LDPC, 디코더/HW/구성 기여 없는 순수 분석
- **ID**: ieee:904940
- **Type**: conference
- **Published**: 2000
- **Authors**: D. Divsalar, S. Dolinar, F. Pollara
- **PDF**: https://ieeexplore.ieee.org/document/904940
- **Abstract**: We model the density of extrinsic information in iterative turbo decoders by Gaussian density functions. This model is verified by experimental measurements. We consider evolution of these density functions through the iterative turbo decoder as a nonlinear dynamical system with feedback. Iterative decoding of turbo codes and of serially concatenated codes are analyzed based on this method. We define a "noise figure" for the iterative decoder, such that the turbo decoder will converge to the correct codeword if the noise figure is bounded below 0 dB. Many mysteries of turbo codes can be explained based on this analysis. For example we can explain why certain codes converge better with iterative decoding than more powerful codes which are only suitable for maximum likelihood decoding. The roles of systematic bits and of recursive convolutional codes as constituents of turbo codes are explained based on this analysis.

## Interference mitigation in frequency-hopped spread-spectrum systems

- **Status**: ❌
- **Reason**: 주파수도약 확산스펙트럼 간섭완화 코딩 연구, LDPC 핵심 아님·떼어낼 ECC 기법 없는 무선 응용
- **ID**: ieee:878081
- **Type**: conference
- **Published**: 2000
- **Authors**: A. Worthen, W. Stark
- **PDF**: https://ieeexplore.ieee.org/document/878081
- **Abstract**: In this paper we explore the error probability of different coding schemes in a frequency-hopped spread-spectrum communication systems subject to partial-band interference and a system subject to Rayleigh fading. The interplay between block length of the code and channel memory is quantified. We show that there is an optimal memory length that maximizes performance. At low signal-to-noise ratios (or close to capacity) large memory is better while at large signal-to-noise ratio smaller memory is optimum.

## Turbo decoding of a low-density generator matrix code for a high-density magnetic recording channel

- **Status**: ❌
- **Reason**: LDGM+turbo BCJR 디코딩으로 BP는 BCJR soft-output에 종속 — 부호 비의존적 바이너리 LDPC BP 이식 기여 없음
- **ID**: ieee:891960
- **Type**: conference
- **Published**: 2000
- **Authors**: T. Nishiya, S. Mita, T. Nara
- **PDF**: https://ieeexplore.ieee.org/document/891960
- **Abstract**: In this paper, we propose a turbo decoding method for a low-density generator matrix code. It is based on the Bahl-Cocke-Jelinek-Raviv (BCJR) algorithm and the belief propagation (BP) algorithm. Userbits with high error probability are selected for the BP algorithm by using the soft-output of the BCJR algorithm. Since the amount of calculation in the BP algorithm increases exponentially with the number of the userbits, the amount of calculation is reduced drastically by the selection of the userbits with higher error probability. We showed that the use of the proposed algorithm and 16/17 MTR code on an MEEPR4 channel results in a performance better than that obtained without turbo decoding.

## Improved upper bounds on the ensemble performance of ML decoded low density parity check codes

- **Status**: ❌
- **Reason**: 바이너리 LDPC의 ML 디코딩 앙상블 성능 상계 — 순수 이론 bound, 디코더/HW/구성으로 안 이어짐
- **ID**: ieee:831034
- **Type**: journal
- **Published**: 2000
- **Authors**: I. Sason, S. Shamai
- **PDF**: https://ieeexplore.ieee.org/document/831034
- **Abstract**: In this letter, we study improved upper bounds on the performance of low density parity check codes over binary-input additive white Gaussian noise channels, assuming that the codes are maximum-likelihood decoded. The results demonstrate the phenomenal performance of the low density parity check codes.
