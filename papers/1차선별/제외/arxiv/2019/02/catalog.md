# arXiv — 2019-02


## Probabilistic Parity Shaping for Linear Codes

- **Status**: ❌
- **Reason**: 확률적 패리티 셰이핑(PAS/PPS) — 변조/셰이핑 아키텍처, LDPC는 베이스라인, 떼어낼 ECC 디코더/구성 기법 없음
- **ID**: arxiv:1902.10648v1
- **Type**: preprint
- **Published**: 2019-02-27
- **Authors**: Georg Böcherer, Diego Lentner, Alessandro Cirino +1
- **PDF**: https://arxiv.org/pdf/1902.10648v1
- **Abstract**: Linear layered probabilistic shaping (LLPS) is proposed, an architecture for linear codes to efficiently encode to shaped code words. In the previously proposed probabilistic amplitude shaping (PAS) architecture, a distribution matcher (DM) maps information bits to shaped bits, which are then systematically encoded by appending uniformly distributed parity bits. LLPS extends PAS by probabilistic parity shaping (PPS), which uses a syndrome DM to calculate shaped parity bits. LLPS enables the transmission with any desired distribution using linear codes, furthermore, by LLPS, a given linear code with rate $R_\text{fec}$ can be operated at any rate $R\leq R_\text{fec}$ by changing the distribution. LLPS is used with an LDPC code for dirty paper coding against an interfering BPSK signal, improving the energy efficiency by 0.8 dB.

## Multi-Matrix Post-Processing for Quantum Key Distribution

- **Status**: ❌
- **Reason**: QKD multi-LDPC reconciliation 에러율 추정 — 정보조정 영역, 떼어낼 디코더 양자화/HW 기법 없이 추정기법만
- **ID**: arxiv:1902.05263v1
- **Type**: preprint
- **Published**: 2019-02-14
- **Authors**: Chaohui Gao, Dong Jiang, Liangliang Lu +2
- **PDF**: https://arxiv.org/pdf/1902.05263v1
- **Abstract**: Post-processing is a significant step in quantum key distribution(QKD), which is used for correcting the quantum-channel noise errors and distilling identical corrected keys between two distant legitimate parties. Efficient error reconciliation protocol, which can lead to an increase in the secure key generation rate, is one of the main performance indicators of QKD setups. In this paper, we propose a multi-low-density parity-check codes based reconciliation scheme, which can provide remarkable perspectives for highly efficient information reconciliation. With testing our approach through data simulation, we show that the proposed scheme combining multi-syndrome-based error rate estimation allows a more accurate estimation about the error rate as compared with random sampling and single-syndrome estimation techniques before the error correction, as well as a significant increase in the efficiency of the procedure without compromising security and sacrificing reconciliation efficiency.
