# arXiv — 2022-01


## Low-Resolution Precoding for Multi-Antenna Downlink Channels and OFDM

- **Status**: ❌
- **Reason**: 저해상도 프리코딩(무선 다운링크); LDPC는 BER 확인용 5G 베이스라인일 뿐 떼어낼 ECC 기법 없음
- **ID**: arxiv:2201.11202v2
- **Type**: preprint
- **Published**: 2022-01-26
- **Authors**: Andrei Stefan Nedelcu, Fabian Steiner, Gerhard Kramer
- **PDF**: https://arxiv.org/pdf/2201.11202v2
- **Abstract**: Downlink precoding is considered for multi-path multi-input single-output channels where the base station uses orthogonal frequency-division multiplexing and low-resolution signaling. A quantized coordinate minimization (QCM) algorithm is proposed and its performance is compared to other precoding algorithms including squared infinity-norm relaxation (SQUID), multi-antenna greedy iterative quantization (MAGIQ), and maximum safety margin precoding. MAGIQ and QCM achieve the highest information rates and QCM has the lowest complexity measured in the number of multiplications. The information rates are computed for pilot-aided channel estimation and data-aided channel estimation. Bit error rates for a 5G low-density parity-check code confirm the information-theoretic calculations. Simulations with imperfect channel knowledge at the transmitter show that the performance of QCM and SQUID degrades in a similar fashion as zero-forcing precoding with high resolution quantizers.

## Decoding Nonbinary LDPC Codes via Proximal-ADMM Approach (include convergence proofs)

- **Status**: ❌
- **Reason**: 비이진(GF(q)) LDPC proximal-ADMM 디코더 — non-binary는 즉시 제외
- **ID**: arxiv:2201.00370v1
- **Type**: preprint
- **Published**: 2022-01-02
- **Authors**: Yongchao Wang, Jing Bai
- **PDF**: https://arxiv.org/pdf/2201.00370v1
- **Abstract**: In this paper, we focus on decoding nonbinary low-density parity-check (LDPC) codes in Galois fields of characteristic two via the proximal alternating direction method of multipliers (proximal-ADMM). By exploiting Flanagan/Constant-Weighting embedding techniques and the decomposition technique based on three-variables parity-check equations, two efficient proximal-ADMM decoders for nonbinary LDPC codes are proposed. We show that both of them are theoretically guaranteed convergent to some stationary point of the decoding model and either of their computational complexities in each proximal-ADMM iteration scales linearly with LDPC code's length and the size of the considered Galois field. Moreover, the decoder based on the Constant-Weight embedding technique satisfies the favorable property of codeword symmetry. Simulation results demonstrate their effectiveness in comparison with state-of-the-art LDPC decoders.
