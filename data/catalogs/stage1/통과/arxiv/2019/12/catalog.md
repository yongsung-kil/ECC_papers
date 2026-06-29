# arXiv — 2019-12 (1차선별 통과)


## A Code-specific Conservative Model for the Failure Rate of Bit-flipping Decoding of LDPC Codes with Cryptographic Applications

- **Status**: ✅
- **Reason**: 비트플립 디코더 변형 및 decoding failure rate(error floor 유사) 분석 — 암호 응용이나 디코더/구성 기법은 바이너리 LDPC에 이식 가능(C/E), 애매하여 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: arxiv:1912.05182v1
- **Type**: preprint
- **Published**: 2019-12-11
- **Authors**: Paolo Santini, Alessandro Barenghi, Gerardo Pelosi +2
- **PDF**: https://arxiv.org/pdf/1912.05182v1
- **Abstract**: Characterizing the decoding failure rate of iteratively decoded Low- and Moderate-Density Parity Check (LDPC/MDPC) codes is paramount to build cryptosystems based on them, able to achieve indistinguishability under adaptive chosen ciphertext attacks. In this paper, we provide a statistical worst-case analysis of our proposed iterative decoder obtained through a simple modification of the classic in-place bit-flipping decoder. This worst case analysis allows both to derive the worst-case behaviour of an LDPC/MDPC code picked among the family with the same length, rate and number of parity checks, and a code-specific bound on the decoding failure rate. The former result allows us to build a code-based cryptosystem enjoying the $δ$-correctness property required by IND-CCA2 constructions, while the latter result allows us to discard code instances which may have a decoding failure rate significantly different from the average one (i.e., representing weak keys), should they be picked during the key generation procedure.
