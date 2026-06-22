# arXiv — 2024-07


## On the energy barrier of hypergraph product codes

- **Status**: ❌
- **Reason**: 하이퍼그래프 곱 양자코드 에너지 장벽 — 양자 self-correcting 메모리 이론 bound, 비대상
- **ID**: arxiv:2407.20526v1
- **Type**: preprint
- **Published**: 2024-07-30
- **Authors**: Guangqi Zhao, Andrew C. Doherty, Isaac H. Kim
- **PDF**: https://arxiv.org/pdf/2407.20526v1
- **Abstract**: A macroscopic energy barrier is a necessary condition for self-correcting quantum memory. In this paper, we prove tight bounds on the energy barrier applicable to any quantum code obtained from the hypergraph product of two classical codes. If the underlying classical codes are low-density parity-check codes (LDPC), the energy barrier of the quantum code is shown to be the minimum energy barrier of the underlying classical codes (and their transposes) up to an additive $O(1)$ constant.

## Telecommand Rejection Probability for CCSDS-compliant LDPC-Coded Transmissions with Tail Sequence

- **Status**: ❌
- **Reason**: CCSDS TC tail-sequence rejection 확률 분석; 표준 LDPC 사용, 떼어낼 새 디코더·코드설계·HW 기법 없음 (통신 응용 특이적)
- **ID**: arxiv:2407.16258v1
- **Type**: preprint
- **Published**: 2024-07-23
- **Authors**: Rebecca Giuliani, Massimo Battaglioni, Marco Baldi +2
- **PDF**: https://arxiv.org/pdf/2407.16258v1
- **Abstract**: According to the Consultative Committee for Space Data Systems (CCSDS) recommendation for TeleCommand (TC) synchronization and coding, the Communications Link Transmission Unit (CLTU) consists of a start sequence, followed by coded data, and a tail sequence, which might be optional depending on the employed coding scheme. With regard to the latter, these transmissions traditionally use a modified Bose-Chaudhuri-Hocquenghem (BCH) code, to which two state-of-the-art Low-Density Parity-Check (LDPC) codes were later added. As a lightweight technique to detect the presence of the tail sequence, an approach based on decoding failure has traditionally been used, choosing a non-correctable string as the tail sequence. This works very well with the BCH code, for which bounded-distance decoders are employed. When the same approach is employed with LDPC codes, it is necessary to design the tail sequence as a non-correctable string for the case of iterative decoders based on belief propagation. Moreover, the tail sequence might be corrupted by noise, potentially converting it into a correctable pattern. It is therefore important that the tail sequence is chosen to be as much distant as possible, according to some metric, from any legitimate codeword. In this paper we study such problem, and analyze the TC rejection probability both theoretically and through simulations. Such a performance figure, being the rate at which the CLTU is discarded, should clearly be minimized. Our analysis is performed considering many different choices of the system parameters (e.g., length of the CLTU, decoding algorithm, maximum number of decoding iterations).

## Error correction for encoded quantum annealing revisited

- **Status**: ✅
- **Reason**: 양자 어닐링 readout이지만 고전 LDPC(SLHZ)용 bit-flipping 디코더 알고리즘 제안 — 양자 전용 개념 비의존, 고전 바이너리 LDPC에 이식 가능(C)
- **ID**: arxiv:2407.15480v2
- **Type**: preprint
- **Published**: 2024-07-22
- **Authors**: Yoshihiro Nambu
- **PDF**: https://arxiv.org/pdf/2407.15480v2
- **Abstract**: F. Pastawski and J. Preskill discussed error correction of quantum annealing (QA) based on a parity-encoded spin system, known as the Sourlas-Lechner-Hauke-Zoller (SLHZ) system. They pointed out that the SLHZ system is closely related to a classical low-density parity-check (LDPC) code and demonstrated its error-correcting capability through a belief propagation (BP) algorithm assuming independent random spin-flip errors. In contrast, Ablash et al. suggested that the SLHZ system does not receive the benefits of post-readout decoding. The reason is that independent random spin-flips are not the most relevant error arising from sampling excited states during the annealing process, whether in closed or open system cases. In this work, we revisit this issue: we propose a very simple decoding algorithm to eliminate errors in the readout of SLHZ systems and show experimental evidence suggesting that SLHZ system exhibits error-correcting capability in decoding annealing readouts. Our new algorithm can be thought of as a bit-flipping algorithm for LDPC codes. Assuming an independent and identical noise model, we found that the performance of our algorithm is comparable to that of the BP algorithm. The error correcting-capability for the sampled readouts was investigated using Monte Carlo calculations that simulate the final time distribution of QA. The results show that the algorithm successfully eliminates errors in the sampled readouts under conditions where error-free state or even code state is not sampled at all. Our simulation suggests that decoding of annealing readouts will be successful if the correctable states can be sampled by annealing, and annealing can be considered to play a role as a pre-process of the classical decoding process. This knowledge will be useful for designing and developing practical QA based on the SLHZ system in the near future.

## SSIP: automated surgery with quantum LDPC codes

- **Status**: ❌
- **Reason**: qLDPC CSS 코드 surgery 자동화 툴; 스태빌라이저·논리측정 등 양자 전용 개념 의존, 고전 이식 불가
- **ID**: arxiv:2407.09423v1
- **Type**: preprint
- **Published**: 2024-07-12
- **Authors**: Alexander Cowtan
- **PDF**: https://arxiv.org/pdf/2407.09423v1
- **Abstract**: We present Safe Surgery by Identifying Pushouts (SSIP), an open-source lightweight Python package for automating surgery between qubit CSS codes. SSIP is flexible: it is capable of performing both external surgery, that is surgery between two codeblocks, and internal surgery, that is surgery within the same codeblock. Under the hood, it performs linear algebra over $\mathbb{F}_2$ governed by universal constructions in the category of chain complexes. We demonstrate on quantum Low-Density Parity Check (qLDPC) codes, which are not topological codes in general, and are of interest for near-term fault-tolerant quantum computing. Such qLDPC codes include lift-connected surface codes, generalised bicycle codes and bivariate bicycle codes. We show that various logical measurements can be performed cheaply by surgery without sacrificing the high code distance. For example, half of the single-qubit logical measurements in the $Z$ or $X$ basis on the $[[ 144 ,12, 12 ]]$ gross code require only 30 total additional qubits each, assuming the upper bound on distance given by QDistRnd is tight. This is two orders of magnitude lower than the additional qubit count of 1380 initially predicted by Bravyi et al.
