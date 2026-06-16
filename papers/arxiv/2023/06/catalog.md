# arXiv — 2023-06


## Efficiently Using Polar Codes in 5G Base Stations to Enhance Rural Connectivity

- **ID**: arxiv:2306.15476v1
- **Type**: preprint
- **Published**: 2023-06-27
- **Authors**: Aman Shreshtha, Smruti R Sarangi
- **PDF**: https://arxiv.org/pdf/2306.15476v1
- **Abstract**: 5G connectivity has become essential to integrate rural communities into the broader digital economy and support critical applications like remote education and remote surgery. A major hindrance to expanding rural broadband coverage, especially in developing countries, is the high cost of installing 5G base stations. Hence, there is a need to reduce the cost of a 5G base station without degrading its performance. Our work proposes a novel approach to efficiently utilize the polar code encoders in a 5G base station. The idea is to use the idle time of the polar encoders during downlink transmission for error correction in the 5G data plane. Polar codes have conventionally been used in the 5G control plane, while LDPC codes are used in the data plane. We perform detailed characterization experiments to show the advantages of using polar codes in the data plane as well. Further, to intelligently distribute the user data packets among the available compute nodes, we propose a set of novel resource allocation algorithms and compare their performance with other algorithms in the literature. Using our proposed optimization techniques, we achieve a 17% reduction in the cost of a 5G base station. Simultaneously, we are able to improve the performance by 24% compared to a conventional base station.

## High-Speed Area-Efficient Hardware Architecture for the Efficient Detection of Faults in a Bit-Parallel Multiplier Utilizing the Polynomial Basis of GF(2m)

- **ID**: arxiv:2306.13347v3
- **Type**: preprint
- **Published**: 2023-06-23
- **Authors**: Saeideh Nabipour, Javad Javidan
- **PDF**: https://arxiv.org/pdf/2306.13347v3
- **Abstract**: The utilization of finite field multipliers is pervasive in contemporary digital systems, with hardware implementation for bit parallel operation often necessitating millions of logic gates. However, various digital design issues, whether inherent or stemming from soft errors, can result in gate malfunction, ultimately can cause gates to malfunction, which in turn results in incorrect multiplier outputs. Thus, to prevent susceptibility to error, it is imperative to employ a reliable finite field multiplier implementation that boasts a robust fault detection capability. In order to achieve the best fault detection performance for finite field detection performance for finite field multipliers while maintaining a low-complexity implementation, this study proposes a novel fault detection scheme for a recent bit-parallel polynomial basis over GF(2m). The primary concept behind the proposed approach is centered on the implementation of an efficient BCH decoder that utilize Berlekamp-Rumsey-Solomon (BRS) algorithm and Chien-search method to effectively locate errors with minimal delay. The results of our synthesis indicate that our proposed error detection and correction architecture for a 45-bit multiplier with 5-bit errors achieves a 37% and 49% reduction in critical path delay compared to existing designs. Furthermore, a 45-bit multiplicand with five errors has hardware complexity that is only 80%, which is significantly less complex than the most advanced BCH-based fault recognition techniques, such as TMR, Hamming's single error correction, and LDPC-based methods for finite field multiplication which is desirable in constrained applications, such as smart cards, IoT devices, and implantable medical devices.

## Single-shot decoding of good quantum LDPC codes

- **ID**: arxiv:2306.12470v2
- **Type**: preprint
- **Published**: 2023-06-21
- **Authors**: Shouzhen Gu, Eugene Tang, Libor Caha +3
- **PDF**: https://arxiv.org/pdf/2306.12470v2
- **Abstract**: Quantum Tanner codes constitute a family of quantum low-density parity-check (LDPC) codes with good parameters, i.e., constant encoding rate and relative distance. In this article, we prove that quantum Tanner codes also facilitate single-shot quantum error correction (QEC) of adversarial noise, where one measurement round (consisting of constant-weight parity checks) suffices to perform reliable QEC even in the presence of measurement errors. We establish this result for both the sequential and parallel decoding algorithms introduced by Leverrier and Zémor. Furthermore, we show that in order to suppress errors over multiple repeated rounds of QEC, it suffices to run the parallel decoding algorithm for constant time in each round. Combined with good code parameters, the resulting constant-time overhead of QEC and robustness to (possibly time-correlated) adversarial noise make quantum Tanner codes alluring from the perspective of quantum fault-tolerant protocols.

## High Throughput Open-Source Implementation of Wi-Fi 6 and WiMAX LDPC Encoder and Decoder

- **ID**: arxiv:2306.12063v1
- **Type**: preprint
- **Published**: 2023-06-21
- **Authors**: Tomas Palenik, Viktor Szitkey
- **PDF**: https://arxiv.org/pdf/2306.12063v1
- **Abstract**: This paper describes the design and C99 implementation of a free and open-source Low-Density Parity-Check (LDPC) codes encoder and decoder focused primarily on the Quasi-Cyclic LDPC (QCLDPC) codes utilized in the IEEE 802.11ax-2021 (Wi-Fi 6) and IEEE 802.16-2017 (WiMAX) standards. The encoder is designed in two variants: the first one universal, the other a minimal memory usage design. The decoder provides a single- and multi- threaded implementation of the layered singlescan min-sum LDPC decoding algorithm both for floating point and fixed-point arithmetic. Both encoder and decoder are directly callable from MATLAB using the provided MEX wrappers but are designed to be simply used in any C project. A comparison of throughput and error performance with the recent commercial closed-source MEX implementation of an LDPC encoder and decoder introduced in MATLAB R2021b Communications Toolbox is provided. Source code portability to alternative nonx86 architectures is facilitated by using only the standard C99 constructs, GNU tools, and POSIX libraries. The implementation maintains low-memory requirements, enabling its deployment in a constrained-architecture in the context of Internet of Things. All source codes are freely available on GitHub under a permissive BSD license.
