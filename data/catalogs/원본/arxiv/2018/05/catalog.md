# arXiv — 2018-05


## A theory of single-shot error correction for adversarial noise

- **Status**: ❌
- **Reason**: 양자 LDPC single-shot 오류정정(소프트니스/메타체크/homological product) — 양자 EC, 스태빌라이저·측정 의존, 고전 바이너리 이식 불가
- **ID**: arxiv:1805.09271v6
- **Type**: preprint
- **Published**: 2018-05-23
- **Authors**: Earl T. Campbell
- **PDF**: https://arxiv.org/pdf/1805.09271v6
- **Abstract**: Single-shot error correction is a technique for correcting physical errors using only a single round of noisy check measurements, such that any residual noise affects a small number of qubits. We propose a general theory of single-shot error correction and establish a sufficient condition called good soundness of the code's measurement checks. Good code soundness in topological (or LDPC) codes is shown to entail a macroscopic energy barrier for the associated Hamiltonian. Consequently, 2D topological codes with local checks can not have good soundness. In tension with this, we also show that for any code a specific choice of measurement checks does exist that provides good soundness. In other words, every code can perform single-shot error correction but the required checks may be nonlocal and act on many qubits. If we desire codes with both good soundness and simple measurement checks (the LDPC property) then careful constructions are needed. Finally, we use a double application of the homological product to construct quantum LDPC codes with single-shot error correcting capabilities. Our double homological product codes exploit redundancy in measurements checks through a process we call metachecking.

## Robust Gradient Descent via Moment Encoding with LDPC Codes

- **Status**: ❌
- **Reason**: 분산컴퓨팅 straggler 완화용 moment encoding(LDPC를 erasure/계산 가속에 사용) — 채널 ECC 아님, 떼어낼 디코더 기법 없음
- **ID**: arxiv:1805.08327v2
- **Type**: preprint
- **Published**: 2018-05-22
- **Authors**: Raj Kumar Maity, Ankit Singh Rawat, Arya Mazumdar
- **PDF**: https://arxiv.org/pdf/1805.08327v2
- **Abstract**: This paper considers the problem of implementing large-scale gradient descent algorithms in a distributed computing setting in the presence of {\em straggling} processors. To mitigate the effect of the stragglers, it has been previously proposed to encode the data with an erasure-correcting code and decode at the master server at the end of the computation. We, instead, propose to encode the second-moment of the data with a low density parity-check (LDPC) code. The iterative decoding algorithms for LDPC codes have very low computational overhead and the number of decoding iterations can be made to automatically adjust with the number of stragglers in the system. We show that for a random model for stragglers, the proposed moment encoding based gradient descent method can be viewed as the stochastic gradient descent method. This allows us to obtain convergence guarantees for the proposed solution. Furthermore, the proposed moment encoding based method is shown to outperform the existing schemes in a real distributed computing setup.

## Flexible IR-HARQ Scheme for Polar-Coded Modulation

- **Status**: ❌
- **Reason**: Polar code IR-HARQ scheme(dynamically frozen bits, QUP) — 비-LDPC 부호, 디코더 기법이 LDPC BP에 이식 안 됨
- **ID**: arxiv:1805.07078v1
- **Type**: preprint
- **Published**: 2018-05-18
- **Authors**: Peihong Yuan, Fabian Steiner, Tobias Prinz +1
- **PDF**: https://arxiv.org/pdf/1805.07078v1
- **Abstract**: A flexible incremental redundancy hybrid auto- mated repeat request (IR-HARQ) scheme for polar codes is proposed based on dynamically frozen bits and the quasi-uniform puncturing (QUP) algorithm. The length of each transmission is not restricted to a power of two. It is applicable for the binary input additive white Gaussian noise (biAWGN) channel as well as higher-order modulation. Simulation results show that this scheme has similar performance as directly designed polar codes with QUP and outperforms LTE-turbo and 5G-LDPC codes with IR-HARQ.

## Improved Reconciliation With Polar Codes In Quantum Key Distribution

- **Status**: ❌
- **Reason**: QKD 정보조정 + polar 코드(비-LDPC), 떼어낼 바이너리 LDPC BP 기법 없음
- **ID**: arxiv:1805.05046v1
- **Type**: preprint
- **Published**: 2018-05-14
- **Authors**: Sunghoon Lee, Jooyoun Park, Jun Heo
- **PDF**: https://arxiv.org/pdf/1805.05046v1
- **Abstract**: Quantum key distribution (QKD) is a cryptographic system that generates an information-theoretically secure key shared by two legitimate parties. QKD consists of two parts: quantum and classical. The latter is referred to as classical post-processing (CPP). Information reconciliation is a part of CPP in which parties are given correlated variables and attempt to eliminate the discrepancies between them while disclosing a minimum amount of information. The elegant reconciliation protocol known as \emph{Cascade} was developed specifically for QKD in 1992 and has become the de-facto standard for all QKD implementations. However, the protocol is highly interactive. Thus, other protocols based on linear block codes such as Hamming codes, low-density parity-check (LDPC) codes, and polar codes have been researched. In particular, reconciliation using LDPC codes has been mainly studied because of its outstanding performance. Nevertheless, with small block size, the bit error rate performance of polar codes under successive-cancellation list (SCL) decoding with a cyclic redundancy check (CRC) is comparable to state-of-the-art turbo and LDPC codes. In this study, we demonstrate the use of polar codes to improve the performance of information reconciliation in a QKD system with small block size. The best decoder for polar codes, a CRC-aided SCL decoder, requires CRC-precoded messages. However, messages that are sifted keys in QKD are obtained arbitrarily as a result of a characteristic of the QKD protocol and cannot be CRC-precoded. We propose a method that allows arbitrarily obtained sifted keys to be CRC precoded by introducing a virtual string. Thus the best decoder can be used for reconciliation using polar codes and improves the efficiency of the protocol.

## Hindering reaction attacks by using monomial codes in the McEliece cryptosystem

- **Status**: ❌
- **Reason**: McEliece 암호계 reaction attack 방어(보안), NAND ECC로 이식할 디코더/구성 기법 없음
- **ID**: arxiv:1805.04722v1
- **Type**: preprint
- **Published**: 2018-05-12
- **Authors**: Paolo Santini, Marco Baldi, Giovanni Cancellieri +1
- **PDF**: https://arxiv.org/pdf/1805.04722v1
- **Abstract**: In this paper we study recent reaction attacks against QC-LDPC and QC-MDPC code-based cryptosystems, which allow an opponent to recover the private parity-check matrix through its distance spectrum by observing a sufficiently high number of decryption failures. We consider a special class of codes, known as monomial codes, to form private keys with the desirable property of having a unique and complete distance spectrum. We verify that for these codes the problem of recovering the secret key from the distance spectrum is equivalent to that of finding cliques in a graph, and use this equivalence to prove that current reaction attacks are not applicable when codes of this type are used in the McEliece cryptosystem.

## Reliability-Based Windowed Decoding for Spatially-Coupled LDPC Codes

- **Status**: ✅
- **Reason**: SC-LDPC용 신규 신뢰도 기반 윈도디코딩(PMR+PSC stopping), error floor 개선 — 바이너리 디코더 기법(C/E)
- **ID**: arxiv:1805.02902v2
- **Type**: preprint
- **Published**: 2018-05-08
- **Authors**: Peng Kang, Yixuan Xie, Lei Yang +1
- **PDF**: https://arxiv.org/pdf/1805.02902v2
- **Abstract**: In this letter, we propose a reliability-based windowed decoding scheme for spatially-coupled (SC) low-density parity-check (LDPC) codes. To mitigate the error propagation along the sliding windowed decoder of the SC LDPC codes, a partial message reservation (PMR) method is proposed where only the reliable messages generated in the previous decoding window are reserved for the next decoding window. We also propose a partial syndrome check (PSC) stopping rule for each decoding window, in which only the complete VNs are checked. Simulation results show that our proposed scheme significantly improves the error floor performance compared to the sliding windowed decoder with the conventional weighted bit-flipping (WBF) algorithm.
