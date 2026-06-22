# arXiv — 2024-02 (1차선별 통과)


## Random Staircase Generator Matrix Codes: Performance Analysis and Construction

- **Status**: ✅
- **Reason**: SGMC + LC-ROSD: GE 병렬화로 OSD 디코딩 지연 저감, 바이너리 채널 ECC 디코더 기법 — NAND LDPC OSD에 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: arxiv:2402.16245v2
- **Type**: preprint
- **Published**: 2024-02-26
- **Authors**: Qianfan Wang, Yiwen Wang, Yixin Wang +2
- **PDF**: https://arxiv.org/pdf/2402.16245v2
- **Abstract**: In this paper, we propose a class of codes, referred to as random staircase generator matrix codes (SGMCs), which have staircase-like generator matrices. In the infinite-length region, we prove that the random SGMC is capacity-achieving over binary-input output-symmetric (BIOS) channels. In the finite-length region, we present the representative ordered statistics decoding with local constraints (LC-ROSD) algorithm for the SGMCs. The most distinguished feature of the SGMCs with LC-ROSD is that the staircase-like matrices enable parallel implementation of the Gaussian elimination (GE), avoiding the serial GE of conventional OSD and supporting a potential low decoding latency, as implied from simulations. To analyze the performance of random SGMCs in the finite-length region, we derive the ensemble weight spectrum and invoke the conventional union bound. We also derive a partially random coding union (RCU) bound, which is tighter than the conventional one and is used as a criterion to design the SGMCs. Staircase-like generator matrices allow us to derive a series of (tighter and tighter) lower bounds based on the second-order Bonferroni inequality with the incremental number of codewords. The numerical results show that the decoding performance can match well with the proposed partially RCU bound for different code rates and different profiles. The numerical results also show that the tailored SGMCs with the LC-ROSD algorithm can approach the finite-length performance bound, outperforming the 5G low-density parity-check (LDPC) codes, 5G polar codes, and Reed-Muller (RM) codes.
