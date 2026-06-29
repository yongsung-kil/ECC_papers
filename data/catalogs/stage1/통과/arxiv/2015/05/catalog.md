# arXiv — 2015-05 (1차선별 통과)


## A 2.48Gb/s QC-LDPC Decoder Implementation on the NI USRP-2953R

- **Status**: ✅
- **Reason**: 표준 QC-LDPC지만 massively-parallel FPGA 디코더 아키텍처(D) 제시, NAND 디코더로 이식 가능
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: arxiv:1505.04339v1
- **Type**: preprint
- **Published**: 2015-05-16
- **Authors**: Swapnil Mhaske, David Uliana, Hojin Kee +3
- **PDF**: https://arxiv.org/pdf/1505.04339v1
- **Abstract**: The increasing data rates expected to be of the order of Gb/s for future wireless systems directly impact the throughput requirements of the modulation and coding subsystems of the physical layer. In an effort to design a suitable channel coding solution for 5G wireless systems, in this brief we present a massively-parallel 2.48Gb/s Quasi-Cyclic Low-Density Parity-Check (QC-LDPC) decoder implementation operating at 200MHz on the NI USRP-2953R, on a single FPGA. The high-level description of the entire massively-parallel decoder was translated to a Hardware Description Language (HDL), namely VHDL, using the algorithmic compiler in the National Instruments LabVIEW Communication System Design Suite (CSDS) in approximately 2 minutes. This implementation not only demonstrates the scalability of our decoder architecture but also, the rapid prototyping capability of the LabVIEW CSDS tools. As per our knowledge, at the time of writing this paper, this is the fastest implementation of a standard compliant QC-LDPC decoder on a USRP using an algorithmic compiler.
