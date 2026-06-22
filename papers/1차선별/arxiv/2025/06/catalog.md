# arXiv — 2025-06 (1차선별 통과)


## Dynamic Layered Decoding Scheduling for LDPC Codes Aided by Check Node Error Probabilities

- **Status**: ✅
- **Reason**: 바이너리 LDPC 동적 layered BP 스케줄링(Dyn-EBP/PEBP) 신규 디코더 기법, NAND 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: arxiv:2506.13507v1
- **Type**: preprint
- **Published**: 2025-06-16
- **Authors**: Chenyuan Jia, Dongxu Chang, Ruiyuan Wang +3
- **PDF**: https://arxiv.org/pdf/2506.13507v1
- **Abstract**: In this study, a new scheduling strategies for low-density parity-check (LDPC) codes under layered belief propagation (LBP) is designed. Based on the criteria of prioritizing the update of check nodes with lower error probabilities, we propose two dynamic scheduling methods: dynamic error belief propagation (Dyn-EBP) and dynamic penalty error belief propagation (Dyn-PEBP). In Dyn-EBP, each check node is restricted from being updated the same number of times, whereas Dyn-PEBP removes this restriction and instead introduces a penalty term to balance the number of updates. Simulation results show that, for 5G new radio (NR) LDPC codes, our proposed scheduling methods can outperform existing dynamic and offline scheduling strategies under various blocklengths and code rates. This demonstrates that prioritizing the update of check nodes with lower error probabilities can lead to higher decoding efficiency and validates the effectiveness of our algorithms.

## On the High-Rate FDPC Codes: Construction, Encoding, and a Generalization

- **Status**: ✅
- **Reason**: FDPC 바이너리 부호 신규 구성+저복잡도 인코딩+MP 디코더, 코드설계/디코더 이식 가능(C/E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: arxiv:2506.11345v1
- **Type**: preprint
- **Published**: 2025-06-12
- **Authors**: Mohsen Moradi, Sheida Rabeti, Hessam Mahdavifar
- **PDF**: https://arxiv.org/pdf/2506.11345v1
- **Abstract**: Recently introduced Fair-Density Parity-Check (FDPC) codes, targeting high-rate applications, offer superior error-correction performance (ECP) compared to 5G Low-Density Parity-Check (LDPC) codes, given the same number of message-passing decoding iterations. In this paper, we present a novel construction method for FDPC codes, introduce a generalization of these codes, and propose a low-complexity encoding algorithm. Numerical results demonstrate the fast convergence of the message-passing decoder for FDPC codes.

## A Neural Network-aided Low Complexity Chase Decoder for URLLC

- **Status**: ✅
- **Reason**: Chase는 대수부호용이나 NN 섭동패턴 예측 디코더 아이디어 이식 여지 — 애매, Phase3 재검토
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: arxiv:2506.10513v2
- **Type**: preprint
- **Published**: 2025-06-12
- **Authors**: Enrico Testi, Enrico Paolini
- **PDF**: https://arxiv.org/pdf/2506.10513v2
- **Abstract**: Ultra-reliable low-latency communications (URLLC) demand decoding algorithms that simultaneously offer high reliability and low complexity under stringent latency constraints. While iterative decoding schemes for LDPC and Polar codes offer a good compromise between performance and complexity, they fall short in approaching the theoretical performance limits in the typical URLLC short block length regime. Conversely, quasi-ML decoding schemes for algebraic codes, like Chase-II decoding, exhibit a smaller gap to optimum decoding but are computationally prohibitive for practical deployment in URLLC systems. To bridge this gap, we propose an enhanced Chase-II decoding algorithm that leverages a neural network (NN) to predict promising perturbation patterns, drastically reducing the number of required decoding trials. The proposed approach combines the reliability of quasi-ML decoding with the efficiency of NN inference, making it well-suited for time-sensitive and resource-constrained applications.
