# arXiv — 2022-11


## McEliece cryptosystem based on Plotkin construction with QC-MDPC and QC-LDPC codes

- **Status**: ❌
- **Reason**: McEliece 암호시스템용 QC-LDPC/MDPC + Plotkin 구성 — 암호 보안 목적, 새 디코더/ECC 구성 기여 아님, NAND ECC 이식 기법 없음
- **ID**: arxiv:2211.14206v3
- **Type**: preprint
- **Published**: 2022-11-25
- **Authors**: Belkacem Imine, Naima Hadj-Said, Adda Ali-Pacha
- **PDF**: https://arxiv.org/pdf/2211.14206v3
- **Abstract**: In this paper, we propose a new variant of the McEliece cryptosystem using two families of quasi-cyclic codes: low density parity check codes (QC-LDPC) and moderate density parity check codes (QC-MDPC). Due to the low weight codewords in the dual of LDPC codes, this family of codes is vulnerable to dual code attacks, making it unsuitable for use with the McEliece cryptosystem. However, this is not the case in our proposal, and it is possible by using the (U |U + V ) construction to concatenate LDPC codes with MDPC codes. We will demonstrate that our proposed cryptosystem can withstand dual code and generic decoding attacks, and that the public key can be reduced by leveraging the quasi-cyclic property and the Plotkin construction.

## Homomorphic Logical Measurements

- **Status**: ❌
- **Reason**: 양자 LDPC homomorphic logical measurement — CSS/표면코드 스태빌라이저 측정 프로토콜, 양자 전용 개념 의존, 이식 불가
- **ID**: arxiv:2211.03625v2
- **Type**: preprint
- **Published**: 2022-11-07
- **Authors**: Shilin Huang, Tomas Jochym-O'Connor, Theodore J. Yoder
- **PDF**: https://arxiv.org/pdf/2211.03625v2
- **Abstract**: Shor and Steane ancilla are two well-known methods for fault-tolerant logical measurements, which are successful on small codes and their concatenations. On large quantum low-density-parity-check (LDPC) codes, however, Shor and Steane measurements have impractical time and space overhead respectively. In this work, we widen the choice of ancilla codes by unifying Shor and Steane measurements into a single framework, called homomorphic measurements. For any Calderbank-Shor-Steane (CSS) code with the appropriate ancilla code, one can avoid repetitive measurements or complicated ancilla state preparation procedures such as distillation, which overcomes the difficulties of both Shor and Steane methods. As an example, we utilize the theory of covering spaces to construct homomorphic measurement protocols for arbitrary $X$- or $Z$-type logical Pauli operators on surface codes in general, including the toric code and hyperbolic surface codes. Conventional surface code decoders, such as minimum-weight perfect matching, can be directly applied to our constructions.

## Survey on Source-coding technique

- **Status**: ❌
- **Reason**: 소스코딩(이미지 압축) 서베이, LDPC는 채널코딩 베이스라인 부수 언급 — 떼어낼 ECC 기법 없음
- **ID**: arxiv:2211.00230v2
- **Type**: preprint
- **Published**: 2022-11-01
- **Authors**: Weida Wang
- **PDF**: https://arxiv.org/pdf/2211.00230v2
- **Abstract**: Shannon separation theorem lays the foundation for traditional image compression and transmission schemes, which consist of JPEG type image compression methods and the usual channel coding schemes such as Turbo and LDPC codes. One of the advantages of the separate design is that each of the two components, channel coding and source coding can be handled independently without considering the other, which is the base of decades-long technologies.
