# IEEE Xplore — 2026-06 (1차선별 통과)


## eLDPC: An Elastic and Scalable LDPC-Decoder With Early Termination by Effectively Leveraging High-Level Synthesis

- **Status**: ✅
- **Reason**: FPGA LDPC 디코더 조기종료·확장성 아키텍처(스토리지 명시) - 이식 가능 HW(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:11217176
- **Type**: journal
- **Published**: June 2026
- **Authors**: Shaohua Wang, Zhihao Zeng, Qiang Cao +4
- **PDF**: https://ieeexplore.ieee.org/document/11217176
- **Abstract**: Emerging communication and storage embrace low-density parity-check (LDPC) codes to fully exploit their physical channels. A field-programmable gate array (FPGA) is widely employed to fast prototype and accelerate the LDPC decoding with high complexity. For varying channel conditions, the FPGA decoder is desired to elastically stop iteration when meeting the success condition, avoiding conservatively performing a predefined and large number of iterations. However, the dynamical-execution algorithms with adjustable parameters generally are challenging for a scalable decoder structure, preferred to deterministic execution logic. To overcome the problem, this article presents an elastic and scalable HLS-based FPGA LDPC decoder architecture with early termination to achieve high throughput and flexibility. To this end, eLDPC first provides a universal operation, fully leveraging the features of HLS to efficiently implement optimized small-scale hardware units for low-level data-update operations. Second, eLDPC presents a decoding-iteration pipeline that adds a termination-check (TC) stage to terminate the following iteration for current codeword decoding. eLDPC also presents an HLS-enhanced approach to address memory access conflicts associated with the DU pipeline. Furthermore, eLDPC extends the number of DU decoding-iteration pipelines within a single stream to decode multiple codewords in parallel. Third, eLDPC designs elastic and independent multiple decoding streams by using FIFO queues to decouple the input, output, and a decoding unit (DU) with variable iterations while avoiding the potential blockage of the queueing. We implement and evaluate eLDPC on a Xilinx U55C. Experiments show that eLDPC outperforms recent decoders by up to  $5\times $  with the same parameter and achieves the actual decoding throughput of up to 49.5 Gb/s with high scalability and flexibility.

## QFEC: A 9.97 Gb/s Fully Configurable Quad-Mode Decoder for LDPC, Polar, Turbo, and Convolutional Codes

- **Status**: ✅
- **Reason**: QC-LDPC 포함 멀티모드 FEC 디코더 칩, 공유 메시지패싱 아키텍처 - 이식 가능 HW(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:11424013
- **Type**: journal
- **Published**: June 2026
- **Authors**: Yufan Yue, Kuan-Yu Chen, Xiangdong Wei +5
- **PDF**: https://ieeexplore.ieee.org/document/11424013
- **Abstract**: Rapidly evolving wireless channel conditions and communication standards demand adaptable forward error correction (FEC) decoders. Existing rigid architectures, designed for a single standard, exhibit limited adaptability in terms of throughput and/or coding gain, hindering the timely deployment of new applications. To overcome these limitations, we propose QFEC (quad-mode FEC decoder), a unified and highly configurable FEC decoder. QFEC enables a wide range of throughput vs. coding gain tradeoffs across QC-LDPC, Turbo, Polar, and Convolutional codes (CC) by providing full configurability for existing standards and proprietary systems. This ensures communication reliability under varying channel conditions and seamless support for both legacy and emerging communication protocols. Our hardware-unified approach leverages a shared memory and computation unit architecture that exploits the inherent commonalities in the iterative message-passing dataflow of all four code types. We attain outstanding flexibility at high data rates through an innovative combination of a fully customizable interconnect and a multi-mode computation datapath. The QFEC chip, fabricated in GF 12 nm FinFET technology, achieves 9.97 Gb/s throughput for the Optical Communication Terminal (OCT) standard and 6.52 Gb/s for 5G BG1, while consuming normalized energy efficiency (NEE) of 1.04 pJ/b and 1.53 pJ/b, respectively. This design can reach a maximum of 25.4 Gb/s using a proprietary QC-LDPC configuration. This design significantly surpasses existing solutions in flexibility by offering the broadest support for standards and parameters with a unified, efficient architecture. To the best of our knowledge, this is the first chip implementation of a fully flexible quad-mode FEC decoder for QC-LDPC, Polar, Turbo, CC codes.
