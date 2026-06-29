# arXiv — 2016-08


## Worst case QC-MDPC decoder for McEliece cryptosystem

- **Status**: ❌
- **Reason**: QC-MDPC McEliece 암호 보안용 bit-flipping 타이밍 사이드채널, 보안+MDPC 부호로 NAND ECC 이식 대상 아님
- **ID**: arxiv:1608.06080v1
- **Type**: preprint
- **Published**: 2016-08-22
- **Authors**: Julia Chaulet, Nicolas Sendrier
- **PDF**: https://arxiv.org/pdf/1608.06080v1
- **Abstract**: McEliece encryption scheme which enjoys relatively small key sizes as well as a security reduction to hard problems of coding theory. Furthermore, it remains secure against a quantum adversary and is very well suited to low cost implementations on embedded devices.   Decoding MDPC codes is achieved with the (iterative) bit flipping algorithm, as for LDPC codes. Variable time decoders might leak some information on the code structure (that is on the sparse parity check equations) and must be avoided. A constant time decoder is easy to emulate, but its running time depends on the worst case rather than on the average case. So far implementations were focused on minimizing the average cost. We show that the tuning of the algorithm is not the same to reduce the maximal number of iterations as for reducing the average cost. This provides some indications on how to engineer the QC-MDPC-McEliece scheme to resist a timing side-channel attack.
