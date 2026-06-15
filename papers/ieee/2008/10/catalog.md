# IEEE Xplore — 2008-10


## Unified decoder architecture for LDPC/turbo codes

- **ID**: ieee:4671730
- **Published**: 8-10 Oct. 
- **Authors**: Yang Sun, Joseph R. Cavallaro
- **PDF**: https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=4671730
- **Abstract**: Low-density parity-check (LDPC) codes on par with convolutional turbo codes (CTC) are two of the most powerful error correction codes known to perform very close to the Shannon limit. However, their different code structures usually lead to different hardware implementations. In this paper, we propose a unified decoder architecture that is capable of decoding both LDPC and turbo codes with a limited hardware overhead. We employ maximum a posteriori (MAP) algorithm as a bridge between LDPC and turbo codes. We represent LDPC codes as parallel concatenated single parity check (PCSPC) codes and propose a group sub-trellis (GST) decoding algorithm for the efficient decoding of PCSPC codes. This algorithm achieves about 2X improvement in the convergence speed and is more numerically robust than the classical “tanh” algorithm. What is more interesting is that we can generalize a unified trellis decoding algorithm for LDPC and turbo codes based on their trellis structures. We propose a reconfigurable computation kernel for log-MAP decoding of LDPC and turbo codes at a cost of ∼15% hardware overhead. Small lookup tables (LUTs) with 9 entries of 2-bit data are designed to implement the log-MAP algorithm. Fixed point (6:2) simulation results show that there is negligible or nearly no performance loss by using this LUT approximation compared to the ideal case. The proposed architecture results in scalable and flexible datapath units enabling parallel decoding of LDPC/turbo codes.
