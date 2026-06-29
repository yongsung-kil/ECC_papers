# arXiv — 2016-12


## Roads towards fault-tolerant universal quantum computation

- **Status**: ❌
- **Reason**: 양자 fault-tolerant 연산 리뷰, 고차원 양자 LDPC 코드. 양자 전용 개념 의존, 서베이라 제외
- **ID**: arxiv:1612.07330v2
- **Type**: preprint
- **Published**: 2016-12-21
- **Authors**: Earl T. Campbell, Barbara M. Terhal, Christophe Vuillot
- **PDF**: https://arxiv.org/pdf/1612.07330v2
- **Abstract**: Current experiments are taking the first steps toward noise-resilient logical qubits. Crucially, a quantum computer must not merely store information, but also process it. A fault-tolerant computational procedure ensures that errors do not multiply and spread. This review compares the leading proposals for promoting a quantum memory to a quantum processor. We compare magic state distillation, color code techniques and other alternative ideas, paying attention to relative resource demands. We discuss the several no-go results which hold for low-dimensional topological codes and outline the potential rewards of using high-dimensional quantum (LDPC) codes in modular architectures.

## Transmission and Storage Rates for Sequential Massive Random Access

- **Status**: ❌
- **Reason**: 소스 코딩(SMRA), rate-compatible LDPC를 베이스라인으로 사용. 채널 ECC가 아니라 제외
- **ID**: arxiv:1612.07163v2
- **Type**: preprint
- **Published**: 2016-12-21
- **Authors**: Elsa Dupraz, Thomas Maugey, Aline Roumy +1
- **PDF**: https://arxiv.org/pdf/1612.07163v2
- **Abstract**: This paper introduces a new source coding paradigm called Sequential Massive Random Access (SMRA). In SMRA, a set of correlated sources is encoded once for all and stored on a server, and clients want to successively access to only a subset of the sources. Since the number of simultaneous clients can be huge, the server is only allowed to extract a bitstream from the stored data: no re-encoding can be performed before the transmission of the specific client's request. In this paper, we formally define the SMRA framework and introduce both storage and transmission rates to characterize the performance of SMRA. We derive achievable transmission and storage rates for lossless source coding of i.i.d. and non i.i.d. sources, and transmission and storage rates-distortion regions for Gaussian sources. We also show two practical implementations of SMRA systems based on rate-compatible LDPC codes. Both theoretical and experimental results demonstrate that SMRA systems can reach the same transmission rates as in traditional point to point source coding schemes, while having a reasonable overhead in terms of storage rate. These results constitute a breakthrough for many recent data transmission applications in which different parts of the data are requested by the clients.

## Construction of Full-Diversity LDPC Lattices for Block-Fading Channels

- **Status**: ❌
- **Reason**: block-fading용 LDPC lattice, 신규 반복 디코더 제시하나 lattice/number field 의존이라 NAND 바이너리 채널 ECC 이식성 낮아 제외(애매하나 lattice 디코더 특이적)
- **ID**: arxiv:1612.04039v1
- **Type**: preprint
- **Published**: 2016-12-13
- **Authors**: Hassan Khodaiemehr, Mohammad-Reza Sadeghi, Daniel Panario
- **PDF**: https://arxiv.org/pdf/1612.04039v1
- **Abstract**: LDPC lattices were the first family of lattices which have an efficient decoding algorithm in high dimensions over an AWGN channel. Considering Construction D' of lattices with one binary LDPC code as underlying code gives the well known Construction A LDPC lattices or 1-level LDPC lattices. Block-fading channel (BF) is a useful model for various wireless communication channels in both indoor and outdoor environments. Frequency-hopping schemes and orthogonal frequency division multiplexing (OFDM) can conveniently be modelled as block-fading channels. Applying lattices in this type of channel entails dividing a lattice point into multiple blocks such that fading is constant within a block but changes, independently, across blocks. The design of lattices for BF channels offers a challenging problem, which differs greatly from its counterparts like AWGN channels. Recently, the original binary Construction A for lattices, due to Forney, have been generalized to a lattice construction from totally real and complex multiplication fields. This generalized Construction A of lattices provides signal space diversity intrinsically, which is the main requirement for the signal sets designed for fading channels. In this paper we construct full diversity LDPC lattices for block-fading channels using Construction A over totally real number fields. We propose a new iterative decoding method for these family of lattices which has complexity that grows linearly in the dimension of the lattice. In order to implement our decoding algorithm, we propose the definition of a parity check matrix and Tanner graph for full diversity Construction A lattices. We also prove that the constructed LDPC lattices together with the proposed decoding method admit diversity order n-1 over an n-block-fading channel.

## Symmetric blind information reconciliation for quantum key distribution

- **Status**: ❌
- **Reason**: QKD 블라인드 정보조정(reconciliation) 개선. 채널 ECC가 아니며 떼어낼 디코더/HW 기법 명시 없음
- **ID**: arxiv:1612.03673v2
- **Type**: preprint
- **Published**: 2016-12-12
- **Authors**: E. O. Kiktenko, A. S. Trushechkin, C. C. W. Lim +2
- **PDF**: https://arxiv.org/pdf/1612.03673v2
- **Abstract**: Quantum key distribution (QKD) is a quantum-proof key-exchange scheme which is fast approaching the communication industry. An essential component in QKD is the information reconciliation step, which is used for correcting the quantum-channel noise errors. The recently suggested blind reconciliation technique, based on low-density parity-check (LDPC) codes, offers remarkable prospectives for efficient information reconciliation without an a priori error rate estimation. We suggest an improvement of the blind-information-reconciliation protocol promoting a significant increase in the efficiency of the procedure and reducing its interactivity. The proposed technique is based on introducing symmetry in operations of parties, and the consideration of results of unsuccessful belief-propagation decodings.
