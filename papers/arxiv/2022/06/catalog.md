# arXiv — 2022-06


## Reducing the Error Floor of the Sign-Preserving Min-Sum LDPC Decoder via Message Weighting of Low-Degree Variable Nodes

- **ID**: arxiv:2206.11532v1
- **Type**: preprint
- **Published**: 2022-06-23
- **Authors**: Lotte Paulissen, Alex Alvarado, Kaiquan Wu +1
- **PDF**: https://arxiv.org/pdf/2206.11532v1
- **Abstract**: Some low-complexity LDPC decoders suffer from error floors. We apply iteration-dependent weights to the degree-3 variable nodes to solve this problem. When the 802.3ca EPON LDPC code is considered, an error floor decrease of more than 3 orders of magnitude is achieved.

## Two-sided Robustly Testable Codes

- **ID**: arxiv:2206.09973v3
- **Type**: preprint
- **Published**: 2022-06-20
- **Authors**: Gleb Kalachev, Pavel Panteleev
- **PDF**: https://arxiv.org/pdf/2206.09973v3
- **Abstract**: We show that the tensor product of two random linear codes is robustly testable with high probability. This implies that one can obtain pairs of linear codes such that their product and the product of their dual codes are simultaneously robustly testable. Such two-sided robustly testable codes (with a much weaker form of robustness) were the key ingredient in the recent constructions of asymptotically good quantum LDPC codes, which ensured their linear minimum distance. We hope that the existence of such codes with a stronger form of robustness, shown here, can be used to simplify the proofs and provide better distance bounds in these constructions. We also give new very simple examples of non-robustly testable codes. We show that if the parity-checks of two codes are mutually orthogonal, then their product is not robustly testable. In particular, this implies that the product of a code with its dual can never be robustly testable. We also study a property of a collection of linear codes called product-expansion, which can be viewed as a coboundary expansion of the cochain complex naturally associated with the product of these codes. We show that this property is related with the robust testability and the agreement testability of the products of codes.

## Good Quantum LDPC Codes with Linear Time Decoders

- **ID**: arxiv:2206.07750v1
- **Type**: preprint
- **Published**: 2022-06-15
- **Authors**: Irit Dinur, Min-Hsiu Hsieh, Ting-Chun Lin +1
- **PDF**: https://arxiv.org/pdf/2206.07750v1
- **Abstract**: We construct a new explicit family of good quantum low-density parity-check codes which additionally have linear time decoders. Our codes are based on a three-term chain $(\mathbb{F}_2^{m\times m})^V \quad \xrightarrow{δ^0}\quad (\mathbb{F}_2^{m})^{E} \quad\xrightarrow{δ^1} \quad \mathbb{F}_2^F$ where $V$ ($X$-checks) are the vertices, $E$ (qubits) are the edges, and $F$ ($Z$-checks) are the squares of a left-right Cayley complex, and where the maps are defined based on a pair of constant-size random codes $C_A,C_B:\mathbb{F}_2^m\to\mathbb{F}_2^Δ$ where $Δ$ is the regularity of the underlying Cayley graphs.   One of the main ingredients in the analysis is a proof of an essentially-optimal robustness property for the tensor product of two random codes.

## Efficient decoding up to a constant fraction of the code length for asymptotically good quantum codes

- **ID**: arxiv:2206.07571v2
- **Type**: preprint
- **Published**: 2022-06-15
- **Authors**: Anthony Leverrier, Gilles Zémor
- **PDF**: https://arxiv.org/pdf/2206.07571v2
- **Abstract**: We introduce and analyse an efficient decoder for the quantum Tanner codes of that can correct adversarial errors of linear weight. Previous decoders for quantum low-density parity-check codes could only handle adversarial errors of weight $O(\sqrt{n \log n})$. We also work on the link between quantum Tanner codes and the Lifted Product codes of Panteleev and Kalachev, and show that our decoder can be adapted to the latter. The decoding algorithm alternates between sequential and parallel procedures and converges in linear time.

## An efficient decoder for a linear distance quantum LDPC code

- **ID**: arxiv:2206.06557v1
- **Type**: preprint
- **Published**: 2022-06-14
- **Authors**: Shouzhen Gu, Christopher A. Pattison, Eugene Tang
- **PDF**: https://arxiv.org/pdf/2206.06557v1
- **Abstract**: Recent developments have shown the existence of quantum low-density parity check (qLDPC) codes with constant rate and linear distance. A natural question concerns the efficient decodability of these codes. In this paper, we present a linear time decoder for the recent quantum Tanner codes construction of asymptotically good qLDPC codes, which can correct all errors of weight up to a constant fraction of the blocklength. Our decoder is an iterative algorithm which searches for corrections within constant-sized regions. At each step, the corrections are found by reducing a locally defined and efficiently computable cost function which serves as a proxy for the weight of the remaining error.

## 6G-AUTOR: Autonomic CSI-Free Transceiver via Realtime On-Device Signal Analytics

- **ID**: arxiv:2206.03250v1
- **Type**: preprint
- **Published**: 2022-06-07
- **Authors**: Shih-Chun Lin, Chia-Hung Lin, K V S Rohit +1
- **PDF**: https://arxiv.org/pdf/2206.03250v1
- **Abstract**: Next-generation wireless systems aim at fulfilling diverse application requirements but fundamentally rely on point-to-point transmission qualities. Aligning with recent AI-enabled wireless implementations, this paper introduces autonomic radios, 6G-AUTOR, that leverage novel algorithm-hardware separation platforms, softwarization of transmission (TX) and reception (RX) operations, and automatic reconfiguration of RF frontends, to support link performance and resilience. As a comprehensive transceiver solution, our design encompasses several ML-driven models, each enhancing a specific aspect of either TX or RX, leading to robust transceiver operation under tight constraints of future wireless systems. A data-driven radio management module was developed via deep Q-networks to support fast-reconfiguration of TX resource blocks (RB) and proactive multi-agent access. Also, a ResNet-inspired fast-beamforming solution was employed to enable robust communication to multiple receivers over the same RB, which has potential applications in realisation of cell-free infrastructures. As a receiver the system was equipped with a capability of ultra-broadband spectrum recognition. Apart from this, a fundamental tool - automatic modulation classification (AMC) which involves a complex correntropy extraction, followed by a convolutional neural network (CNN)-based classification, and a deep learning-based LDPC decoder were added to improve the reception quality and radio performance. Simulations of individual algorithms demonstrate that under appropriate training, each of the corresponding radio functions have either outperformed or have performed on-par with the benchmark solutions.
