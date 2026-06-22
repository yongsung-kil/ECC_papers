# arXiv — 2008-12


## On Quantum and Classical Error Control Codes: Constructions and Applications

- **Status**: ❌
- **Reason**: 양자/비-LDPC(BCH,RS,convolutional,subsystem) 위주 구성 논문; 유한기하/Latin square LDPC도 표준 구성 수준, 양자 의존 — 제외
- **ID**: arxiv:0812.5104v1
- **Type**: preprint
- **Published**: 2008-12-30
- **Authors**: Salah A. Aly
- **PDF**: https://arxiv.org/pdf/0812.5104v1
- **Abstract**: It is conjectured that quantum computers are able to solve certain problems more quickly than any deterministic or probabilistic computer. A quantum computer exploits the rules of quantum mechanics to speed up computations. However, it is a formidable task to build a quantum computer, since the quantum mechanical systems storing the information unavoidably interact with their environment. Therefore, one has to mitigate the resulting noise and decoherence effects to avoid computational errors.   In this work, I study various aspects of quantum error control codes -- the key component of fault-tolerant quantum information processing. I present the fundamental theory and necessary background of quantum codes and construct many families of quantum block and convolutional codes over finite fields, in addition to families of subsystem codes over symmetric and asymmetric channels.   Particularly, many families of quantum BCH, RS, duadic, and convolutional codes are constructed over finite fields. Families of subsystem codes and a class of optimal MDS subsystem codes are derived over asymmetric and symmetric quantum channels. In addition, propagation rules and tables of upper bounds on subsystem code parameters are established. Classes of quantum and classical LDPC codes based on finite geometries and Latin squares are constructed.

## Error-Trellis State Complexity of LDPC Convolutional Codes Based on Circulant Matrices

- **Status**: ✅
- **Reason**: 순환행렬 기반 QC-LDPC convolutional 부호의 error-trellis 상태복잡도 저감 신규 구성(행 시프트 제어) — 바이너리 QC/SC-LDPC 설계 기법 이식 가능(E)
- **ID**: arxiv:0812.4642v2
- **Type**: preprint
- **Published**: 2008-12-26
- **Authors**: M. Tajima, K. Okino, T. Miyagoshi
- **PDF**: https://arxiv.org/pdf/0812.4642v2
- **Abstract**: Let H(D) be the parity-check matrix of an LDPC convolutional code corresponding to the parity-check matrix H of a QC code obtained using the method of Tanner et al. We see that the entries in H(D) are all monomials and several rows (columns) have monomial factors. Let us cyclically shift the rows of H. Then the parity-check matrix H'(D) corresponding to the modified matrix H' defines another convolutional code. However, its free distance is lower-bounded by the minimum distance of the original QC code. Also, each row (column) of H'(D) has a factor different from the one in H(D). We show that the state-space complexity of the error-trellis associated with H'(D) can be significantly reduced by controlling the row shifts applied to H with the error-correction capability being preserved.
