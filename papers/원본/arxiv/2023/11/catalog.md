# arXiv — 2023-11


## Flexible polar encoding for information reconciliation in QKD

- **Status**: ❌
- **Reason**: QKD 정보조정용 polar code 인코더 — LDPC 아닌 polar이고 양자 키분배 응용, 떼어낼 LDPC 기법 없음
- **ID**: arxiv:2312.03100v1
- **Type**: preprint
- **Published**: 2023-11-30
- **Authors**: Snehasis Addy, Sabyasachi Dutta, Somnath Panja +3
- **PDF**: https://arxiv.org/pdf/2312.03100v1
- **Abstract**: Quantum Key Distribution (QKD) enables two parties to establish a common secret key that is information-theoretically secure by transmitting random bits that are encoded as qubits and sent over a quantum channel, followed by classical information processing steps known as information reconciliation and key extraction. Transmission of information over a quantum channel introduces errors that are generally considered to be due to the adversary's tempering with the quantum channel and needs to be corrected using classical communication over an (authenticated) public channel. Commonly used error-correcting codes in the context of QKD include cascade codes, low-density parity check (LDPC) codes, and more recently polar codes. In this work, we explore the applicability of designing of a polar code encoder based on a channel reliability sequence. We show that the reliability sequence can be derived and used to design an encoder independent of the choice of decoder. We then implement our design and evaluate its performance against previous implementations of polar code encoders for QKD as well as other typical error-correcting codes. A key advantage of our approach is the modular design which decouples the encoder and decoder design and allows independent optimization of each. Our work leads to more versatile polar code-based error reconciliation in QKD systems that would result in deployment in a broader range of scenarios.

## qSIEVE: Efficient qLDPC Memory via Systolic Movement in Atom Arrays

- **Status**: ❌
- **Reason**: 원자배열에서 qLDPC 메모리 구현(systolic movement) — 양자 HW 전용, 고전 바이너리 LDPC와 무관
- **ID**: arxiv:2311.16980v3
- **Type**: preprint
- **Published**: 2023-11-28
- **Authors**: Joshua Viszlai, Willers Yang, Sophia Fuhui Lin +4
- **PDF**: https://arxiv.org/pdf/2311.16980v3
- **Abstract**: As quantum machines have scaled up in their number of qubits, significant research has turned towards increasing their fidelity with quantum error correction codes. Although promising results have been shown with the surface code, which only requires near-neighbor connections between qubits, the high qubit overhead of such local codes promises to be problematic. Consequently, recent work has explored non-local quantum LDPC (qLDPC) codes, which have good asymptotic encoding rates. Despite theoretical progress, hardware implementations of these codes has been a longstanding challenge.   At the experimental level, demonstrations of movement based communication on atom arrays suggest this is a powerful new primitive to achieve non-local connectivity. Leveraging this, we present a protocol for implementing non-local qLDPC codes in hardware. Our protocol, qSIEVE, is a co-design of such codes with movement in atom arrays. qSIEVE defines a restricted family of qLDPC codes that can be implemented efficiently with systolic movement.   We then quantify the utility of qSIEVE in the context of a complete fault tolerant architecture. We compare the cost of implementing benchmark programs in a standard, surface code only architecture and a mixed architecture where data is stored in qLDPC memory with qSIEVE and loaded to surface codes for computation.

## NLTS Hamiltonians and Strongly-Explicit SoS Lower Bounds from Low-Rate Quantum LDPC Codes

- **Status**: ❌
- **Reason**: qLDPC로부터 NLTS/SoS 복잡도 이론 하한 — 순수 양자/복잡도 이론, 디코더·HW·구성 이식 불가
- **ID**: arxiv:2311.09503v1
- **Type**: preprint
- **Published**: 2023-11-16
- **Authors**: Louis Golowich, Tali Kaufman
- **PDF**: https://arxiv.org/pdf/2311.09503v1
- **Abstract**: Recent constructions of the first asymptotically good quantum LDPC (qLDPC) codes led to two breakthroughs in complexity theory: the NLTS (No Low-Energy Trivial States) theorem (Anshu, Breuckmann, and Nirkhe, STOC'23), and explicit lower bounds against a linear number of levels of the Sum-of-Squares (SoS) hierarchy (Hopkins and Lin, FOCS'22).   In this work, we obtain improvements to both of these results using qLDPC codes of low rate:   - Whereas Anshu et al. only obtained NLTS Hamiltonians from qLDPC codes of linear dimension, we show the stronger result that qLDPC codes of arbitrarily small positive dimension yield NLTS Hamiltonians.   - The SoS lower bounds of Hopkins and Lin are only weakly explicit because they require running Gaussian elimination to find a nontrivial codeword, which takes polynomial time. We resolve this shortcoming by introducing a new method of planting a strongly explicit nontrivial codeword in linear-distance qLDPC codes, which in turn yields strongly explicit SoS lower bounds.   Our "planted" qLDPC codes may be of independent interest, as they provide a new way of ensuring a qLDPC code has positive dimension without resorting to parity check counting, and therefore provide more flexibility in the code construction.

## Quantum Locally Recoverable Codes

- **Status**: ❌
- **Reason**: 양자 locally recoverable codes(qLRC)·qLDPC 대상, 스태빌라이저 등 양자 전용 개념 의존 — 고전 이식 불가
- **ID**: arxiv:2311.08653v1
- **Type**: preprint
- **Published**: 2023-11-15
- **Authors**: Louis Golowich, Venkatesan Guruswami
- **PDF**: https://arxiv.org/pdf/2311.08653v1
- **Abstract**: Classical locally recoverable codes, which permit highly efficient recovery from localized errors as well as global recovery from larger errors, provide some of the most useful codes for distributed data storage in practice. In this paper, we initiate the study of quantum locally recoverable codes (qLRCs). In the long term, like their classical counterparts, such qLRCs may be used for large-scale quantum data storage. Our results also have concrete implications for quantum LDPC codes, which are applicable to near-term quantum error-correction.   After defining quantum local recoverability, we provide an explicit construction of qLRCs based on the classical LRCs of Tamo and Barg (2014), which we show have (1) a close-to-optimal rate-distance tradeoff (i.e. near the Singleton bound), (2) an efficient decoder, and (3) permit good spatial locality in a physical implementation. Although the analysis is significantly more involved than in the classical case, we obtain close-to-optimal parameters by introducing a "folded" version of our quantum Tamo-Barg (qTB) codes, which we then analyze using a combination of algebraic techniques. We furthermore present and analyze two additional constructions using more basic techniques, namely random qLRCs, and qLRCs from AEL distance amplification. Each of these constructions has some advantages, but neither achieves all 3 properties of our folded qTB codes described above.   We complement these constructions with Singleton-like bounds that show our qLRC constructions achieve close-to-optimal parameters. We also apply these results to obtain Singleton-like bounds for qLDPC codes, which to the best of our knowledge are novel. We then show that even the weakest form of a stronger locality property called local correctability, which permits more robust local recovery and is achieved by certain classical codes, is impossible quantumly.

## Joint Design of Coding and Modulation for Digital Over-the-Air Computation

- **Status**: ❌
- **Reason**: 비이진(non-binary) LDPC 기반 AirComp 코딩 — 비이진 LDPC는 즉시 제외 대상
- **ID**: arxiv:2311.06829v1
- **Type**: preprint
- **Published**: 2023-11-12
- **Authors**: Xin Xie, Cunqinq Hua, Jianan Hong +1
- **PDF**: https://arxiv.org/pdf/2311.06829v1
- **Abstract**: Due to its high communication efficiency, over-the-air computation (AirComp) has been expected to carry out various computing tasks in the next-generation wireless networks. However, up to now, most applications of AirComp are explored in the analog domain, which limits the capability of AirComp in resisting the complex wireless environment, not to mention to integrate the AirComp technique to the existing universal communication standards, most of which are based on the digital system. In this paper, we propose a joint design of channel coding and digital modulation for digital AirComp transmission to attempt to reinforce the foundation for the application of AirComp in the digital system. Specifically, we first propose a non-binary LDPC-based channel coding scheme to enhance the error-correction capability of AirComp. Then, a digital modulation scheme is proposed to achieve the number summation from multiple transmitters via the lattice coding technique. We also provide simulation results to demonstrate the feasibility and the performance of the proposed design.

## A Spin-Optical Quantum Computing Architecture

- **Status**: ❌
- **Reason**: 스핀-광학 양자컴퓨팅 아키텍처, qLDPC 언급뿐 — 양자 HW 전용, 이식할 고전 LDPC 기법 없음
- **ID**: arxiv:2311.05605v5
- **Type**: preprint
- **Published**: 2023-11-09
- **Authors**: Grégoire de Gliniasty, Paul Hilaire, Pierre-Emmanuel Emeriau +3
- **PDF**: https://arxiv.org/pdf/2311.05605v5
- **Abstract**: We introduce an adaptable and modular hybrid architecture designed for fault-tolerant quantum computing. It combines quantum emitters and linear-optical entangling gates to leverage the strength of both matter-based and photonic-based approaches. A key feature of the architecture is its practicality, grounded in the utilisation of experimentally proven optical components. Our framework enables the execution of any quantum error correcting code, but in particular maintains scalability for low-density parity check codes by exploiting built-in non-local connectivity through distant optical links. To gauge its efficiency, we evaluated the architecture using a physically motivated error model. It exhibits loss tolerance comparable to existing all-photonic architecture but without the need for intricate linear-optical resource-state-generation modules that conventionally rely on resource-intensive multiplexing. The versatility of the architecture also offers uncharted avenues for further advancing performance standards.

## Improved Noisy Syndrome Decoding of Quantum LDPC Codes with Sliding Window

- **Status**: ❌
- **Reason**: 양자 LDPC sliding-window 디코딩으로 stabilizer/single-shot 등 양자 전용 개념에 의존, 고전 바이너리 LDPC로 그대로 이식 불가
- **ID**: arxiv:2311.03307v1
- **Type**: preprint
- **Published**: 2023-11-06
- **Authors**: Shilin Huang, Shruti Puri
- **PDF**: https://arxiv.org/pdf/2311.03307v1
- **Abstract**: Quantum error correction (QEC) with single-shot decoding enables reduction of errors after every single round of noisy stabilizer measurement, easing the time-overhead requirements for fault tolerance. Notably, several classes of quantum low-density-parity-check (qLDPC) codes are known which facilitate single-shot decoding, potentially giving them an additional overhead advantage. However, the perceived advantage of single-shot decoding is limited because it can significantly degrade the effective code distance. This degradation may be compensated for by using a much larger code size to achieve the desired target logical error rate, at the cost of increasing the amount of syndrome information to be processed, as well as, increasing complexity of logical operations. Alternatively, in this work we study sliding-window decoding, which corrects errors from previous syndrome measurement rounds while leaving the most recent errors for future correction. We observe that sliding-window decoding significantly improves the logical memory lifetime and hence the effective distance compared to single-shot decoding on hypergraph-product codes and lifted-product codes. Remarkably, we find that this improvement may not cost a larger decoding complexity. Thus, the sliding-window strategy can be more desirable for fast and accurate decoding for fault-tolerant quantum computing with qLDPC codes.

## Analog information decoding of bosonic quantum LDPC codes

- **Status**: ❌
- **Reason**: 보존(bosonic) QLDPC 아날로그 신드롬 디코딩 — 양자 전용 개념(연접 보존 코드) 의존, 고전 이식성 없음
- **ID**: arxiv:2311.01328v2
- **Type**: preprint
- **Published**: 2023-11-02
- **Authors**: Lucas Berent, Timo Hillmann, Jens Eisert +2
- **PDF**: https://arxiv.org/pdf/2311.01328v2
- **Abstract**: Quantum error correction is crucial for scalable quantum information processing applications. Traditional discrete-variable quantum codes that use multiple two-level systems to encode logical information can be hardware-intensive. An alternative approach is provided by bosonic codes, which use the infinite-dimensional Hilbert space of harmonic oscillators to encode quantum information. Two promising features of bosonic codes are that syndrome measurements are natively analog and that they can be concatenated with discrete-variable codes. In this work, we propose novel decoding methods that explicitly exploit the analog syndrome information obtained from the bosonic qubit readout in a concatenated architecture. Our methods are versatile and can be generally applied to any bosonic code concatenated with a quantum low-density parity-check (QLDPC) code. Furthermore, we introduce the concept of quasi-single-shot protocols as a novel approach that significantly reduces the number of repeated syndrome measurements required when decoding under phenomenological noise. To realize the protocol, we present a first implementation of time-domain decoding with the overlapping window method for general QLDPC codes, and a novel analog single-shot decoding method. Our results lay the foundation for general decoding algorithms using analog information and demonstrate promising results in the direction of fault-tolerant quantum computation with concatenated bosonic-QLDPC codes.

## Addressing Stopping Failures for Small Set Flip Decoding of Hypergraph Product Codes

- **Status**: ❌
- **Reason**: 하이퍼그래프곱 QLDPC의 Small-Set-Flip + PAL 디코더 — 양자 코드 구조(스태빌라이저)에 특화, 바이너리 고전 LDPC 이식 불가
- **ID**: arxiv:2311.00877v1
- **Type**: preprint
- **Published**: 2023-11-01
- **Authors**: Lev Stambler, Anirudh Krishna, Michael E. Beverland
- **PDF**: https://arxiv.org/pdf/2311.00877v1
- **Abstract**: For a quantum error correcting code to be used in practice, it needs to be equipped with an efficient decoding algorithm, which identifies corrections given the observed syndrome of errors.Hypergraph product codes are a promising family of constant-rate quantum LDPC codes that have a linear-time decoding algorithm called Small-Set-Flip ($\texttt{SSF}$) (Leverrier, Tillich, Zémor FOCS 2015). The algorithm proceeds by iteratively applying small corrections which reduce the syndrome weight. Together, these small corrections can provably correct large errors for sufficiently large codes with sufficiently large (but constant) stabilizer weight. However, this guarantee does not hold for small codes with low stabilizer weight. In this case, $\texttt{SSF}$ can terminate with stopping failures, meaning it encounters an error for which it is unable to identify a small correction. We find that the structure of errors that cause stopping failures have a simple form for sufficiently small qubit failure rates. We propose a new decoding algorithm called the Projection-Along-a-Line ($\texttt{PAL}$) decoder to supplement $\texttt{SSF}$ after stopping failures. Using $\texttt{SSF}+\texttt{PAL}$ as a combined decoder, we find an order-of-magnitude improvement in the logical error rate.
