# arXiv — 2015-08 (1차선별 통과)


## Framework for Application Mapping over Packet-Switched Network of FPGAs: Case Studies

- **Status**: ✅
- **Reason**: LDPC 디코딩을 메시지패싱 PE로 NoC/멀티FPGA에 매핑하는 HW 프레임워크 — 디코더 병렬화·HW 아키텍처(D) 이식 가능, 애매하나 살림
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: arxiv:1508.06823v1
- **Type**: preprint
- **Published**: 2015-08-27
- **Authors**: Vinay B. Y. Kumar, Pinalkumar Engineer, Mandar Datar +4
- **PDF**: https://arxiv.org/pdf/1508.06823v1
- **Abstract**: The algorithm-to-hardware High-level synthesis (HLS) tools today are purported to produce hardware comparable in quality to handcrafted designs, particularly with user directive driven or domains specific HLS. However, HLS tools are not readily equipped for when an application/algorithm needs to scale. We present a (work-in-progress) semi-automated framework to map applications over a packet-switched network of modules (single FPGA) and then to seamlessly partition such a network over multiple FPGAs over quasi-serial links. We illustrate the framework through three application case studies: LDPC Decoding, Particle Filter based Object Tracking, and Matrix Vector Multiplication over GF(2). Starting with high-level representations of each case application, we first express them in an intermediate message passing formulation, a model of communicating processing elements. Once the processing elements are identified, these are either handcrafted or realized using HLS. The rest of the flow is automated where the processing elements are plugged on to a configurable network-on-chip (CONNECT) topology of choice, followed by partitioning the 'on-chip' links to work seamlessly across chips/FPGAs.
