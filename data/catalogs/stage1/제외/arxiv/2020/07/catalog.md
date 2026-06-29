# arXiv — 2020-07


## Iterative List Detection and Decoding for mMTC

- **Status**: ❌
- **Reason**: mMTC 활동/신호 검출(JADD) 무선 응용; LDPC는 IDD 베이스라인일 뿐 떼어낼 ECC 디코더 기법 없음.
- **ID**: arxiv:2007.12836v1
- **Type**: preprint
- **Published**: 2020-07-25
- **Authors**: R. B. Di Renna, R. C. de Lamare
- **PDF**: https://arxiv.org/pdf/2007.12836v1
- **Abstract**: The main challenge of massive machine-type communications (mMTC) is the joint activity and signal detection of devices. The mMTC scenario with many devices transmitting data intermittently at low data rates and via very short packets enables its modelling as a sparse signal processing problem. In this work, we consider a grant-free system and propose a detection and decoding scheme that jointly detects activity and signals of devices. The proposed scheme consists of a list detection technique, an $l_0$-norm regularized activity-aware recursive least-squares algorithm, and an iterative detection and decoding (IDD) approach that exploits the device activity probability. In particular, the proposed list detection technique uses two candidate-list schemes to enhance the detection performance. We also incorporate the proposed list detection technique into an IDD scheme based on low-density parity-check codes. We derive uplink sum-rate expressions that take into account metadata collisions, interference and a variable activity probability for each user. A computational complexity analysis shows that the proposed list detector does not require a significant additional complexity over existing detectors, whereas a diversity analysis discusses its diversity order. Simulations show that the proposed scheme obtains a performance superior to existing suboptimal detectors and close to the oracle LMMSE detector.

## Towards Quantum Belief Propagation for LDPC Decoding in Wireless Networks

- **Status**: ❌
- **Reason**: 양자 어닐링 하드웨어 기반 LDPC 디코더 — QA 전용 임베딩이라 NAND 고전 디코더/HW로 이식 불가.
- **ID**: arxiv:2007.11069v2
- **Type**: preprint
- **Published**: 2020-07-21
- **Authors**: Srikar Kasi, Kyle Jamieson
- **PDF**: https://arxiv.org/pdf/2007.11069v2
- **Abstract**: We present Quantum Belief Propagation (QBP), a Quantum Annealing (QA) based decoder design for Low Density Parity Check (LDPC) error control codes, which have found many useful applications in Wi-Fi, satellite communications, mobile cellular systems, and data storage systems. QBP reduces the LDPC decoding to a discrete optimization problem, then embeds that reduced design onto quantum annealing hardware. QBP's embedding design can support LDPC codes of block length up to 420 bits on real state-of-the-art QA hardware with 2,048 qubits. We evaluate performance on real quantum annealer hardware, performing sensitivity analyses on a variety of parameter settings. Our design achieves a bit error rate of $10^{-8}$ in 20 $μ$s and a 1,500 byte frame error rate of $10^{-6}$ in 50 $μ$s at SNR 9 dB over a Gaussian noise wireless channel. Further experiments measure performance over real-world wireless channels, requiring 30 $μ$s to achieve a 1,500 byte 99.99$\%$ frame delivery rate at SNR 15-20 dB. QBP achieves a performance improvement over an FPGA based soft belief propagation LDPC decoder, by reaching a bit error rate of $10^{-8}$ and a frame error rate of $10^{-6}$ at an SNR 2.5--3.5 dB lower. In terms of limitations, QBP currently cannot realize practical protocol-sized ($\textit{e.g.,}$ Wi-Fi, WiMax) LDPC codes on current QA processors. Our further studies in this work present future cost, throughput, and QA hardware trend considerations.

## Maximum-Likelihood Channel Decoding with Quantum Annealing Machine

- **Status**: ❌
- **Reason**: 양자 어닐링(D-Wave) ML 디코딩을 QUBO로 정식화 — QA 전용 구현, 고전 HW/디코더로 이식 불가.
- **ID**: arxiv:2007.08689v2
- **Type**: preprint
- **Published**: 2020-07-16
- **Authors**: Naoki Ide, Tetsuya Asayama, Hiroshi Ueno +1
- **PDF**: https://arxiv.org/pdf/2007.08689v2
- **Abstract**: We formulate maximum likelihood (ML) channel decoding as a quadratic unconstraint binary optimization (QUBO) and simulate the decoding by the current commercial quantum annealing machine, D-Wave 2000Q. We prepared two implementations with Ising model formulations, generated from the generator matrix and the parity-check matrix respectively. We evaluated these implementations of ML decoding for low-density parity-check (LDPC) codes, analyzing the number of spins and connections and comparing the decoding performance with belief propagation (BP) decoding and brute-force ML decoding with classical computers. The results show that these implementations are superior to BP decoding in relatively short length codes, and while the performance in the long length codes deteriorates, the implementation from the parity-check matrix formulation still works up to 1k length with fewer spins and connections than that of the generator matrix formulation due to the sparseness of parity-check matrices of LDPC.
