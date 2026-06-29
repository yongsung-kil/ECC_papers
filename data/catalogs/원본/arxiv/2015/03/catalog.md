# arXiv — 2015-03


## Decoding LDPC codes via Noisy Gradient Descent Bit-Flipping with Re-Decoding

- **Status**: ✅
- **Reason**: NGDBF 비트플립 디코더 + re-decoding 개선(C) — 바이너리 LDPC BP에 직접 이식 가능
- **ID**: arxiv:1503.08913v1
- **Type**: preprint
- **Published**: 2015-03-31
- **Authors**: Tasnuva Tithi, Chris Winstead, Gopalakrishnan Sundararajan
- **PDF**: https://arxiv.org/pdf/1503.08913v1
- **Abstract**: In this paper, we consider the performance of the Noisy Gradient Descent Bit Flipping (NGDBF) algorithm under re-decoding of failed frames. NGDBF is a recent algorithm that uses a non-deterministic gradient descent search to decode low-density parity check (LDPC) codes. The proposed re-decode procedure obtains improved performance because the perturbations are independent at each re-decoding phase, therefore increasing the likelihood of successful decoding. We examine the benefits of re-decoding for an LDPC code from the IEEE 802.3an standard, and find that only a small fraction of re-decoded frames are needed to obtain significant performance benefits. When re-decoding is used, the NGDBF performance is very close to a benchmark offset min-sum decoder for the 802.3an code.

## Strategies for High-Throughput FPGA-based QC-LDPC Decoder Architecture

- **Status**: ✅
- **Reason**: 고처리율 FPGA QC-LDPC 디코더 아키텍처(PCM 표현/파이프라이닝, D) — NAND 디코더 HW 이식 가능
- **ID**: arxiv:1503.02986v3
- **Type**: preprint
- **Published**: 2015-03-10
- **Authors**: Swapnil Mhaske, Hojin Kee, Tai Ly +2
- **PDF**: https://arxiv.org/pdf/1503.02986v3
- **Abstract**: We propose without loss of generality strategies to achieve a high-throughput FPGA-based architecture for a QC-LDPC code based on a circulant-1 identity matrix construction. We present a novel representation of the parity-check matrix (PCM) providing a multi-fold throughput gain. Splitting of the node processing algorithm enables us to achieve pipelining of blocks and hence layers. By partitioning the PCM into not only layers but superlayers we derive an upper bound on the pipelining depth for the compact representation. To validate the architecture, a decoder for the IEEE 802.11n (2012) QC-LDPC is implemented on the Xilinx Kintex-7 FPGA with the help of the FPGA IP compiler [2] available in the NI LabVIEW Communication System Design Suite (CSDS) which offers an automated and systematic compilation flow where an optimized hardware implementation from the LDPC algorithm was generated in approximately 3 minutes, achieving an overall throughput of 608Mb/s (at 260MHz). As per our knowledge this is the fastest implementation of the IEEE 802.11n QC-LDPC decoder using an algorithmic compiler.
