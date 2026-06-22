# arXiv — 2022-08


## An Modified Cole's Importance Sampling Method For Low Error Floor QC-LDPC Codes Construction

- **Status**: ✅
- **Reason**: Trapping set 열거 가속(병렬 IS, GPU/FPGA)으로 error-floor 낮춘 QC-LDPC 구성 기법 — 바이너리, 이식 가능 코드설계(E)
- **ID**: arxiv:2208.05795v1
- **Type**: preprint
- **Published**: 2022-08-11
- **Authors**: Vasiliy Usatyuk
- **PDF**: https://arxiv.org/pdf/2208.05795v1
- **Abstract**: We modified Cole's Importance Sampling (IS) method for enumerating of Trapping Sets (TS, asymmetric subgraphs) causing an error under message-passing decoder. Proposed Cole's IS modifications based on combination of several ideas: parallel TS impulse tree decomposition using unwrapping of message passing iterations, according short cycles dense and straightforward idea of Tanner Graph/ Forney's Normal Graph symmetry - Graph Authomorphism. Its allowed superior Velasquez-Subramani and Karimi-Banihashemi TS enumerating methods. Particularly proposed method under PEG (1008, 504) Mackay code for single thread implementation 5027-times (71463 times, multi-treads) faster compare to Velasquez-Subramani LP method and 43-times faster compare to original Cole's method. For TS enumerating problem under (2640, 1320) Margulis code compare to Velasquez-Subramani LP method proposed method for single thread implementation 37958 times faster, 82-times faster than Karimi-Banihashemi and 134-times faster than Cole's original method. NVIDIA Titan RTX GPU implementation of proposed method gives a further 2-30 times acceleration. FPGA device providing further acceleration from 1.25 to 44 times. We show on example of QC-LDPC codes construction how improvement of EMD spectrum, increase hamming(code) distance effect on TS spectrum and BER/FER error-floor level.

## Energy-Efficient Backscatter-Assisted Coded Cooperative-NOMA for B5G Wireless Communications

- **Status**: ❌
- **Reason**: NOMA 무선 응용 특이적; QC-LDPC는 joint decoder 베이스라인이고 NAND에 떼어낼 새 ECC 기법 없음
- **ID**: arxiv:2208.01123v2
- **Type**: preprint
- **Published**: 2022-08-01
- **Authors**: Muhammad Asif, Asim Ihsan, Wali Ullah Khan +3
- **PDF**: https://arxiv.org/pdf/2208.01123v2
- **Abstract**: In this manuscript, we propose an alternating optimization framework to maximize the energy efficiency of a backscatter-enabled cooperative Non-orthogonal multiple access (NOMA) system by optimizing the transmit power of the source, power allocation coefficients (PAC), and power of the relay node under imperfect successive interference cancellation (SIC) decoding. A three-stage low-complexity energy-efficient alternating optimization algorithm is introduced which optimizes the transmit power, PAC, and relay power by considering the quality of service (QoS), power budget, and cooperation constraints. Subsequently, a joint channel coding framework is introduced to enhance the performance of far user which has no direct communication link with the base station (BS) and has bad channel conditions. In the destination node, the far user data is jointly decoded using a Sum-product algorithm (SPA) based joint iterative decoder realized by jointly-designed Quasi-cyclic Low-density parity-check (QC-LDPC) codes. Simulation results evince that the proposed backscatter-enabled cooperative NOMA system outperforms its counterpart by providing an efficient performance in terms of energy efficiency. Also, proposed jointly-designed QC-LDPC codes provide an excellent bit-error-rate (BER) performance by jointly decoding the far user data for considered BSC cooperative NOMA system with only a few decoding iterations.

## Fast erasure decoder for hypergraph product codes

- **Status**: ❌
- **Reason**: 양자 hypergraph product code의 erasure 디코더 — 양자 전용, 고전 바이너리 LDPC 이식성 없음
- **ID**: arxiv:2208.01002v3
- **Type**: preprint
- **Published**: 2022-08-01
- **Authors**: Nicholas Connolly, Vivien Londe, Anthony Leverrier +1
- **PDF**: https://arxiv.org/pdf/2208.01002v3
- **Abstract**: We propose a decoder for the correction of erasures with hypergraph product codes, which form one of the most popular families of quantum LDPC codes. Our numerical simulations show that this decoder provides a close approximation of the maximum likelihood decoder that can be implemented in O(N^2) bit operations where N is the length of the quantum code. A probabilistic version of this decoder can be implemented in O(N^1.5) bit operations.
