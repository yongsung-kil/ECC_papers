# arXiv — 2025-03 (1차선별 통과)


## Strongly regular generalized partial geometries and associated LDPC codes

- **Status**: ✅
- **Reason**: 고전 바이너리 LDPC 코드 구성(strongly regular generalized partial geometry 기반)으로 최소거리·girth 경계 제시 — 코드 설계(E) 새 기여, 포함
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: arxiv:2503.14058v1
- **Type**: preprint
- **Published**: 2025-03-18
- **Authors**: Lijun Ma, Changli Ma, Zihong Tian
- **PDF**: https://arxiv.org/pdf/2503.14058v1
- **Abstract**: In this paper, we introduce strongly regular generalized partial geometries of grade $r$, which generalise partial geometries and strongly regular $(α,β)$-geometries. By the properties of quadrics in PG$(2,q)$ and PG$(3,q)$, we construct two classes of strongly regular generalized partial geometries of grade $3$. Besides, we define low-density parity-check (LDPC) codes by considering the combinatorial structures of strongly regular generalized partial geometries and derive bounds on minimum distance, dimension and girth for the LDPC codes.

## Construction and Decoding of Quantum Margulis Codes

- **Status**: ✅
- **Reason**: 양자 Margulis 코드지만 고전 Margulis LDPC 구성에서 유래; controlled-girth 2BGA 구성 알고리즘과 표준 min-sum 디코딩 적용은 고전 바이너리 LDPC에 이식 가능(E/C), 애매하여 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: arxiv:2503.03936v3
- **Type**: preprint
- **Published**: 2025-03-05
- **Authors**: Michele Pacenti, Dimitris Chytas, Bane Vasic
- **PDF**: https://arxiv.org/pdf/2503.03936v3
- **Abstract**: Quantum low-density parity-check codes are a promising approach to fault-tolerant quantum computation, offering potential advantages in rate and decoding efficiency. In this work, we introduce quantum Margulis codes, a new class of QLDPC codes derived from Margulis' classical LDPC construction via the two-block group algebra framework. We show that quantum Margulis codes, unlike bivariate bicycle codes which require ordered statistics decoding for effective error correction, can be efficiently decoded using a standard min-sum decoder with linear complexity, when decoded under the code capacity noise model. This is attributed to their Tanner graph structure, which does not exhibit group symmetry, thereby mitigating the well-known problem of error degeneracy in QLDPC decoding. To further enhance performance, we propose an algorithm for constructing 2BGA codes with controlled girth, ensuring a minimum girth of 6 or 8, and use it to generate several quantum Margulis codes of length 240 and 642. We validate our approach through numerical simulations, demonstrating that quantum Margulis codes behave significantly better than BB codes in the error floor region, under min-sum decoding.

## Automorphism Ensemble Decoding of Quantum LDPC Codes

- **Status**: ✅
- **Reason**: automorphism 앙상블 BP 디코더(AutDEC) - 자기동형군을 활용한 BP 앙상블 기법은 고전 바이너리 LDPC 디코더로 이식 가능(C), 양자 전용 개념 비의존
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: arxiv:2503.01738v1
- **Type**: preprint
- **Published**: 2025-03-03
- **Authors**: Stergios Koutsioumpas, Hasan Sayginel, Mark Webster +1
- **PDF**: https://arxiv.org/pdf/2503.01738v1
- **Abstract**: We introduce AutDEC, a fast and accurate decoder for quantum error-correcting codes with large automorphism groups. Our decoder employs a set of automorphisms of the quantum code and an ensemble of belief propagation (BP) decoders. Each BP decoder is given a syndrome which is transformed by one of the automorphisms, and is run in parallel. For quantum codes, the accuracy of BP decoders is limited because short cycles occur in the Tanner graph and our approach mitigates this effect. We demonstrate decoding accuracy comparable to BP-OSD-0 with a lower time overhead for Quantum Reed-Muller (QRM) codes in the code capacity setting, and Bivariate Bicycle (BB) codes under circuit level noise. We provide a Python repository for use by the community and the results of our simulations.
