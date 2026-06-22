# arXiv — 2022-06


## Two-sided Robustly Testable Codes

- **Status**: ❌
- **Reason**: 양자 good qLDPC 구성용 robustly testable code 순수 이론 — 디코더/HW/바이너리 구성으로 안 이어짐
- **ID**: arxiv:2206.09973v3
- **Type**: preprint
- **Published**: 2022-06-20
- **Authors**: Gleb Kalachev, Pavel Panteleev
- **PDF**: https://arxiv.org/pdf/2206.09973v3
- **Abstract**: We show that the tensor product of two random linear codes is robustly testable with high probability. This implies that one can obtain pairs of linear codes such that their product and the product of their dual codes are simultaneously robustly testable. Such two-sided robustly testable codes (with a much weaker form of robustness) were the key ingredient in the recent constructions of asymptotically good quantum LDPC codes, which ensured their linear minimum distance. We hope that the existence of such codes with a stronger form of robustness, shown here, can be used to simplify the proofs and provide better distance bounds in these constructions. We also give new very simple examples of non-robustly testable codes. We show that if the parity-checks of two codes are mutually orthogonal, then their product is not robustly testable. In particular, this implies that the product of a code with its dual can never be robustly testable. We also study a property of a collection of linear codes called product-expansion, which can be viewed as a coboundary expansion of the cochain complex naturally associated with the product of these codes. We show that this property is related with the robust testability and the agreement testability of the products of codes.

## Good Quantum LDPC Codes with Linear Time Decoders

- **Status**: ❌
- **Reason**: 양자 LDPC(qLDPC) 부호 구성·선형시간 디코더 — Cayley complex 등 양자 전용 구조에 의존, 고전 바이너리 LDPC로 그대로 이식 불가, 원칙 제외
- **ID**: arxiv:2206.07750v1
- **Type**: preprint
- **Published**: 2022-06-15
- **Authors**: Irit Dinur, Min-Hsiu Hsieh, Ting-Chun Lin +1
- **PDF**: https://arxiv.org/pdf/2206.07750v1
- **Abstract**: We construct a new explicit family of good quantum low-density parity-check codes which additionally have linear time decoders. Our codes are based on a three-term chain $(\mathbb{F}_2^{m\times m})^V \quad \xrightarrow{δ^0}\quad (\mathbb{F}_2^{m})^{E} \quad\xrightarrow{δ^1} \quad \mathbb{F}_2^F$ where $V$ ($X$-checks) are the vertices, $E$ (qubits) are the edges, and $F$ ($Z$-checks) are the squares of a left-right Cayley complex, and where the maps are defined based on a pair of constant-size random codes $C_A,C_B:\mathbb{F}_2^m\to\mathbb{F}_2^Δ$ where $Δ$ is the regularity of the underlying Cayley graphs.   One of the main ingredients in the analysis is a proof of an essentially-optimal robustness property for the tensor product of two random codes.

## Efficient decoding up to a constant fraction of the code length for asymptotically good quantum codes

- **Status**: ❌
- **Reason**: 양자 Tanner 부호 전용 디코더(adversarial error) — 양자 코드 구조 의존, 고전 바이너리 LDPC 이식성 없음, 원칙 제외
- **ID**: arxiv:2206.07571v2
- **Type**: preprint
- **Published**: 2022-06-15
- **Authors**: Anthony Leverrier, Gilles Zémor
- **PDF**: https://arxiv.org/pdf/2206.07571v2
- **Abstract**: We introduce and analyse an efficient decoder for the quantum Tanner codes of that can correct adversarial errors of linear weight. Previous decoders for quantum low-density parity-check codes could only handle adversarial errors of weight $O(\sqrt{n \log n})$. We also work on the link between quantum Tanner codes and the Lifted Product codes of Panteleev and Kalachev, and show that our decoder can be adapted to the latter. The decoding algorithm alternates between sequential and parallel procedures and converges in linear time.

## An efficient decoder for a linear distance quantum LDPC code

- **Status**: ❌
- **Reason**: 양자 Tanner 부호 전용 선형시간 디코더 — 양자 구조 의존, 고전 바이너리 LDPC로 이식 불가, 원칙 제외
- **ID**: arxiv:2206.06557v1
- **Type**: preprint
- **Published**: 2022-06-14
- **Authors**: Shouzhen Gu, Christopher A. Pattison, Eugene Tang
- **PDF**: https://arxiv.org/pdf/2206.06557v1
- **Abstract**: Recent developments have shown the existence of quantum low-density parity check (qLDPC) codes with constant rate and linear distance. A natural question concerns the efficient decodability of these codes. In this paper, we present a linear time decoder for the recent quantum Tanner codes construction of asymptotically good qLDPC codes, which can correct all errors of weight up to a constant fraction of the blocklength. Our decoder is an iterative algorithm which searches for corrections within constant-sized regions. At each step, the corrections are found by reducing a locally defined and efficiently computable cost function which serves as a proxy for the weight of the remaining error.
