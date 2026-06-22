# arXiv — 2024-01 (1차선별 통과)


## Topology-Aware Exploration of Energy-Based Models Equilibrium: Toric QC-LDPC Codes and Hyperbolic MET QC-LDPC Codes

- **Status**: ✅
- **Reason**: Multi-Edge QC-LDPC/SC-LDPC 코드 구성과 토릭·하이퍼볼릭 토폴로지 기반 girth·구조 설계 — 바이너리 QC-LDPC 코드설계 기법(E) 이식 가능성, 애매하므로 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: arxiv:2401.14749v1
- **Type**: preprint
- **Published**: 2024-01-26
- **Authors**: Vasiliy Usatyuk, Denis Sapozhnikov, Sergey Egorov
- **PDF**: https://arxiv.org/pdf/2401.14749v1
- **Abstract**: This paper presents a method for achieving equilibrium in the ISING Hamiltonian when confronted with unevenly distributed charges on an irregular grid. Employing (Multi-Edge) QC-LDPC codes and the Boltzmann machine, our approach involves dimensionally expanding the system, substituting charges with circulants, and representing distances through circulant shifts. This results in a systematic mapping of the charge system onto a space, transforming the irregular grid into a uniform configuration, applicable to Torical and Circular Hyperboloid Topologies. The paper covers fundamental definitions and notations related to QC-LDPC Codes, Multi-Edge QC-LDPC codes, and the Boltzmann machine. It explores the marginalization problem in code on the graph probabilistic models for evaluating the partition function, encompassing exact and approximate estimation techniques. Rigorous proof is provided for the attainability of equilibrium states for the Boltzmann machine under Torical and Circular Hyperboloid, paving the way for the application of our methodology. Practical applications of our approach are investigated in Finite Geometry QC-LDPC Codes, specifically in Material Science. The paper further explores its effectiveness in the realm of Natural Language Processing Transformer Deep Neural Networks, examining Generalized Repeat Accumulate Codes, Spatially-Coupled and Cage-Graph QC-LDPC Codes. The versatile and impactful nature of our topology-aware hardware-efficient quasi-cycle codes equilibrium method is showcased across diverse scientific domains without the use of specific section delineations.

## Shift-Interleave Coding for DNA-Based Storage: Correction of IDS Errors and Sequence Losses

- **Status**: ✅
- **Reason**: DNA 스토리지용 두 개의 바이너리 LDPC 코드워드 shift-interleave 구성 + 비반복 검출/디코딩 — 스토리지 ECC 코드설계 기법(B/E) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: arxiv:2401.14594v1
- **Type**: preprint
- **Published**: 2024-01-26
- **Authors**: Ryo Shibata, Haruhiko Kaneko
- **PDF**: https://arxiv.org/pdf/2401.14594v1
- **Abstract**: We propose a novel coding scheme for DNA-based storage systems, called the shift-interleave (SI) coding, designed to correct insertion, deletion, and substitution (IDS) errors, as well as sequence losses. The SI coding scheme employs multiple codewords from two binary low-density parity-check codes. These codewords are processed to form DNA base sequences through shifting, bit-to-base mapping, and interleaving. At the receiver side, an efficient non-iterative detection and decoding scheme is employed to sequentially estimate codewords. The numerical results demonstrate the excellent performance of the SI coding scheme in correcting both IDS errors and sequence losses.

## Log-Log Domain Sum-Product Algorithm for Information Reconciliation in Continuous-Variable Quantum Key Distribution

- **Status**: ✅
- **Reason**: CV-QKD용이나 log-log domain SPA로 디코더 메시지 비트폭 축소 + 고정소수점 HW 구현 — 고전 바이너리 LDPC BP 디코더 양자화/HW 기법(C/D)으로 이식 가능, 양자 전용 개념 비의존
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: arxiv:2401.13748v1
- **Type**: preprint
- **Published**: 2024-01-24
- **Authors**: Erdem Eray Cil, Laurent Schmalen
- **PDF**: https://arxiv.org/pdf/2401.13748v1
- **Abstract**: In this paper, we present a novel log-log domain sum-product algorithm (SPA) for decoding low-density parity-check (LDPC) codes in continuous-variable quantum key distribution (CV-QKD) systems. This algorithm reduces the fractional bit width of decoder messages, leading to a smaller memory footprint and a lower resource consumption in hardware implementation. We also provide practical insights for fixed-point arithmetic and compare our algorithm with the conventional SPA in terms of performance and complexity. Our results show that our algorithm achieves comparable or better decoding accuracy than the conventional SPA while saving at least $25\%$ of the fractional bit width.
