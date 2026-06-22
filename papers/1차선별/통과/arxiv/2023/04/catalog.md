# arXiv — 2023-04 (1차선별 통과)


## Spatially-Coupled QLDPC Codes

- **Status**: ✅
- **Reason**: SC-LDPC 구조를 양자에 적용하나 Tanner graph 단주기 최적화·2D-SC 대수 프레임워크는 고전 바이너리 SC-LDPC 코드 설계(E)에서 유래, 이식 가능성 있어 애매 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: arxiv:2305.00137v6
- **Type**: preprint
- **Published**: 2023-04-29
- **Authors**: Siyi Yang, Robert Calderbank
- **PDF**: https://arxiv.org/pdf/2305.00137v6
- **Abstract**: Spatially-coupled (SC) codes is a class of convolutional LDPC codes that has been well investigated in classical coding theory thanks to their high performance and compatibility with low-latency decoders. We describe toric codes as quantum counterparts of classical two-dimensional spatially-coupled (2D-SC) codes, and introduce spatially-coupled quantum LDPC (SC-QLDPC) codes as a generalization. We use the convolutional structure to represent the parity check matrix of a 2D-SC code as a polynomial in two indeterminates, and derive an algebraic condition that is both necessary and sufficient for a 2D-SC code to be a stabilizer code. This algebraic framework facilitates the construction of new code families. While not the focus of this paper, we note that small memory facilitates physical connectivity of qubits, and it enables local encoding and low-latency windowed decoding. In this paper, we use the algebraic framework to optimize short cycles in the Tanner graph of 2D-SC hypergraph product (HGP) codes that arise from short cycles in either component code. While prior work focuses on QLDPC codes with rate less than 1/10, we construct 2D-SC HGP codes with small memories, higher rates (about 1/3), and superior thresholds.
