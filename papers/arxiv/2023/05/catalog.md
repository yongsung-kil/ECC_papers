# arXiv — 2023-05


## Improved belief propagation decoding algorithm based on decoupling representation of Pauli operators for quantum LDPC codes

- **ID**: arxiv:2305.17505v4
- **Type**: preprint
- **Published**: 2023-05-27
- **Authors**: Zhengzhong Yi, Zhipeng Liang, Kaixin Zhong +3
- **PDF**: https://arxiv.org/pdf/2305.17505v4
- **Abstract**: We propose a new method called decoupling representation to represent Pauli operators as vectors over $GF(2)$, based on which we propose partially decoupled belief propagation and fully decoupled belief propagation decoding algorithm for quantum low density parity-check codes. These two algorithms have the capability to deal with the correlations between the $X$ part and the $Z$ part of the vectors in symplectic representation, which are introduced by Pauli $Y$ errors. Hence, they can not only apply to CSS codes, but also to non-CSS codes. Under the assumption that there is no measurement error, compared with traditional belief propagation algorithm in symplectic representation over $GF(2)$, within the same number of iterations, the decoding accuracy of partially decoupled belief propagation and fully decoupled belief propagation algorithm is significantly improved in pure $Y$ noise and depolarizing noise, which supports that decoding algorithms of quantum error correcting codes might have better performance in decoupling representation than in symplectic representation. The impressive performance of fully decoupled belief propagation algorithm might promote the realization of quantum error correcting codes in engineering.

## Non-Gaussian reconciliation for continuous-variable quantum key distribution

- **ID**: arxiv:2305.01963v1
- **Type**: preprint
- **Published**: 2023-05-03
- **Authors**: Xiangyu Wang, Menghao Xu, Yin Zhao +3
- **PDF**: https://arxiv.org/pdf/2305.01963v1
- **Abstract**: Non-Gaussian modulation can improve the performance of continuous-variable quantum key distribution (CV-QKD). For Gaussian modulated coherent state CV-QKD, photon subtraction can realize non-Gaussian modulation, which can be equivalently implemented by non-Gaussian postselection. However, non-Gaussian reconciliation has not been deeply researched, which is one of the key technologies in CV-QKD. In this paper, we propose a non-Gaussian reconciliation method to obtain identical keys from non-Gaussian data. Multidimensional reconciliation and multi-edge type low density parity check codes (MET-LDPC) are used in non-Gaussian reconciliation scheme, where the layered belief propagation decoding algorithm of MET-LDPC codes is used to reduce the decoding complexity. Furthermore, we compare the error correction performance of Gaussian data and non-Gaussian data. The results show that the error correction performance of non-Gaussian data is better than Gaussian data, where the frame error rate can be reduced by 50% for code rate 0.1 at SNR of 0.1554 and the average iteration number can be reduced by 25%.

## Non-Binary LDPC Code Design for Energy-Time Entanglement Quantum Key Distribution

- **ID**: arxiv:2305.00956v1
- **Type**: preprint
- **Published**: 2023-05-01
- **Authors**: Debarnab Mitra, Lev Tauz, Murat Can Sarihan +2
- **PDF**: https://arxiv.org/pdf/2305.00956v1
- **Abstract**: In energy-time entanglement Quantum Key Distribution (QKD), two users extract a shared secret key from the arrival times (discretized as symbols) of entangled photon pairs. In prior work, Zhou et al. proposed a multi-level coding (MLC) scheme that splits the observed symbols into bit layers and utilizes binary Low-Density Parity-Check (LDPC) codes for reconciliation of the symbols. While binary LDPC codes offer low latency for key generation, splitting the symbols into bits results in a loss of key generation rate due to error propagation. Additionally, existing LDPC codes do not fully utilize the properties of the QKD channel to optimize the key rates. In this paper, we mitigate the above issues by first generalizing the MLC scheme to a non-binary(NB) MLC scheme that has layers with non-binary symbols and utilizes NB-LDPC codes. We show the NB-MLC scheme offers flexibility in system design. Additionally, we show that the NB-MLC scheme with a small symbol size per layer offers the best trade-off between latency and key rate. We then propose a framework to jointly optimize the rate and degree profile of the NB-LDPC codes that is tailored towards the QKD channel resulting in higher key rates than prior work.

## General Distance Balancing for Quantum Locally Testable Codes

- **ID**: arxiv:2305.00689v1
- **Type**: preprint
- **Published**: 2023-05-01
- **Authors**: Adam Wills, Ting-Chun Lin, Min-Hsiu Hsieh
- **PDF**: https://arxiv.org/pdf/2305.00689v1
- **Abstract**: In this paper, we prove a lower bound on the soundness of quantum locally testable codes under the distance balancing construction of Evra et al. arXiv:2004.07935 [quant-ph]. Our technical contribution is that the new soundness of the quantum code is at least the old soundness divided by the classical code length (up to a constant factor). This allows us to use any classical code with independent checks when distance balancing, where previously only the repetition code had been considered for qLTCs. By using a good classical LDPC code, we are able to grow the dimension of the hypersphere product codes arXiv:1608.05089 [quant-ph] and the hemicubic codes arXiv:1911.03069 [quant-ph] while maintaining their distance and locality, but at the expense of soundness. From this, and also by distance balancing a chain complex of Cross et al. arXiv:2209.11405 [cs.IT], we obtain quantum locally testable codes of new parameters.
