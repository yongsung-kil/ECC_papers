# arXiv — 2022-08 (1차선별 통과)


## An Modified Cole's Importance Sampling Method For Low Error Floor QC-LDPC Codes Construction

- **Status**: ✅
- **Reason**: Trapping set 열거 가속(병렬 IS, GPU/FPGA)으로 error-floor 낮춘 QC-LDPC 구성 기법 — 바이너리, 이식 가능 코드설계(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: arxiv:2208.05795v1
- **Type**: preprint
- **Published**: 2022-08-11
- **Authors**: Vasiliy Usatyuk
- **PDF**: https://arxiv.org/pdf/2208.05795v1
- **Abstract**: We modified Cole's Importance Sampling (IS) method for enumerating of Trapping Sets (TS, asymmetric subgraphs) causing an error under message-passing decoder. Proposed Cole's IS modifications based on combination of several ideas: parallel TS impulse tree decomposition using unwrapping of message passing iterations, according short cycles dense and straightforward idea of Tanner Graph/ Forney's Normal Graph symmetry - Graph Authomorphism. Its allowed superior Velasquez-Subramani and Karimi-Banihashemi TS enumerating methods. Particularly proposed method under PEG (1008, 504) Mackay code for single thread implementation 5027-times (71463 times, multi-treads) faster compare to Velasquez-Subramani LP method and 43-times faster compare to original Cole's method. For TS enumerating problem under (2640, 1320) Margulis code compare to Velasquez-Subramani LP method proposed method for single thread implementation 37958 times faster, 82-times faster than Karimi-Banihashemi and 134-times faster than Cole's original method. NVIDIA Titan RTX GPU implementation of proposed method gives a further 2-30 times acceleration. FPGA device providing further acceleration from 1.25 to 44 times. We show on example of QC-LDPC codes construction how improvement of EMD spectrum, increase hamming(code) distance effect on TS spectrum and BER/FER error-floor level.
