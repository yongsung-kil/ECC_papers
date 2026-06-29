# arXiv — 2017-02 (1차선별 통과)


## Key Reconciliation with Low-Density Parity-Check Codes for Long-Distance Quantum Cryptography

- **Status**: ✅
- **Reason**: CV-QKD reconciliation이나 QC-LDPC 구성+GPU 가속 디코더 throughput - HW 디코더(D) 기법 이식 가능
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: arxiv:1702.07740v2
- **Type**: preprint
- **Published**: 2017-02-24
- **Authors**: Mario Milicevic, Chen Feng, Lei M. Zhang +1
- **PDF**: https://arxiv.org/pdf/1702.07740v2
- **Abstract**: The speed at which two remote parties can exchange secret keys over a fixed-length fiber-optic cable in continuous-variable quantum key distribution (CV-QKD) is currently limited by the computational complexity of post-processing algorithms for key reconciliation. Multi-edge low-density parity-check (LDPC) codes with low code rates and long block lengths were proposed for CV-QKD, in order to extend the maximum reconciliation distance between the two remote parties. Key reconciliation over multiple dimensions has been shown to further improve the error-correction performance of multi-edge LDPC codes in CV-QKD, thereby increasing both the secret key rate and distance. However, the computational complexity of LDPC decoding for long block lengths on the order of 10^6 bits remains a challenge. This work introduces a quasi-cyclic (QC) code construction for multi-edge LDPC codes that is highly suitable for hardware-accelerated decoding on a modern graphics processing unit (GPU). When combined with an 8-dimensional reconciliation scheme, the LDPC decoder achieves a raw decoding throughput of 1.72Mbit/s and an information throughput of 7.16Kbit/s using an NVIDIA GeForce GTX 1080 GPU at a maximum distance of 160km with a secret key rate of 4.10x10^{-7} bits/pulse for a rate 0.02 multi-edge code with block length of 10^6 bits when finite-size effects are considered. This work extends the previous maximum CV-QKD distance of 100km to 160km, while delivering between 1.07x and 8.03x higher decoded information throughput over the upper bound on the secret key rate for a lossy channel. The GPU-based QC-LDPC decoder achieves a 1.29x improvement in throughput over the best existing GPU decoder implementation for a rate 1/10 multi-edge LDPC code with block length of 2^{20} bits. These results show that LDPC decoding is no longer the computational bottleneck in long-distance CV-QKD.
