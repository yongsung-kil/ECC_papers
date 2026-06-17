# arXiv — 2022-09


## Quantum LDPC Codes for Modular Architectures

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: arxiv:2209.14329v3
- **Type**: preprint
- **Published**: 2022-09-28
- **Authors**: Armands Strikis, Lucas Berent
- **PDF**: https://arxiv.org/pdf/2209.14329v3
- **Abstract**: In efforts to scale the size of quantum computers, modularity plays a central role across most quantum computing technologies. In the light of fault tolerance, this necessitates designing quantum error-correcting codes that are compatible with the connectivity arising from the architectural layouts. In this paper, we aim to bridge this gap by giving a novel way to view and construct quantum LDPC codes tailored for modular architectures. We demonstrate that if the intra- and inter-modular qubit connectivity can be viewed as corresponding to some classical or quantum LDPC codes, then their hypergraph product code fully respects the architectural connectivity constraints. Finally, we show that relaxed connectivity constraints that allow twists of connections between modules pave a way to construct codes with better parameters.

## Dynamic Write-Voltage Design and Read-Voltage Optimization for MLC NAND Flash Memory

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: arxiv:2209.01424v1
- **Type**: preprint
- **Published**: 2022-09-03
- **Authors**: Runbin Cai, Yi Fang, Zhifang Shi +2
- **PDF**: https://arxiv.org/pdf/2209.01424v1
- **Abstract**: To mitigate the impact of noise and interference on multi-level-cell (MLC) flash memory with the use of low-density parity-check (LDPC) codes, we propose a dynamic write-voltage design scheme considering the asymmetric property of raw bit error rate (RBER), which can obtain the optimal write voltage by minimizing a cost function. In order to further improve the decoding performance of flash memory, we put forward a low-complexity entropy-based read-voltage optimization scheme, which derives the read voltages by searching for the optimal entropy value via a log-likelihood ratio (LLR)-aware cost function. Simulation results demonstrate the superiority of our proposed dynamic write-voltage design scheme and read-voltage optimization scheme with respect to the existing counterparts.

## Software Tools for Decoding Quantum Low-Density Parity Check Codes

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: arxiv:2209.01180v1
- **Type**: preprint
- **Published**: 2022-09-02
- **Authors**: Lucas Berent, Lukas Burgholzer, Robert Wille
- **PDF**: https://arxiv.org/pdf/2209.01180v1
- **Abstract**: Quantum Error Correction (QEC) is an essential field of research towards the realization of large-scale quantum computers. On the theoretical side, a lot of effort is put into designing error-correcting codes that protect quantum data from errors, which inevitably happen due to the noisy nature of quantum hardware and quantum bits (qubits). Protecting data with an error-correcting code necessitates means to recover the original data, given a potentially corrupted data set-a task referred to as decoding. It is vital that decoding algorithms can recover error-free states in an efficient manner. While theoretical properties of recent QEC methods have been extensively studied, good techniques to analyze their performance in practically more relevant settings is still a widely unexplored area. In this work, we propose a set of software tools that allows to numerically experiment with so-called Quantum Low-Density Parity Check codes (QLDPC codes)-a broad class of codes, some of which have recently been shown to be asymptotically good. Based on that, we provide an implementation of a general decoder for QLDPC codes. On top of that, we propose an efficient heuristic decoder that tackles the runtime bottlenecks of the general QLDPC decoder while still maintaining comparable decoding performance. These tools eventually allow to confirm theoretical results around QLDPC codes in a more practical setting and showcase the value of software tools (in addition to theoretical considerations) for investigating codes for practical applications. The resulting tool, which is publicly available at https://github.com/lucasberent/qecc under the MIT license, is meant to provide a playground for the search for "practically good" quantum codes.
