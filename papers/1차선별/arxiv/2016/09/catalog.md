# arXiv — 2016-09 (1차선별 통과)


## OpenCL/CUDA algorithms for parallel decoding of any irregular LDPC code using GPU

- **Status**: ✅
- **Reason**: GPU/FPGA용 임의 비정칙 LDPC 병렬 디코더 OpenCL/CUDA 구현, 노드차수 제한 없는 병렬화+신드롬 병렬계산은 이식 가능 HW 아키텍처(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: arxiv:1609.01567v2
- **Type**: preprint
- **Published**: 2016-09-06
- **Authors**: Jan Broulim, Alexander Ayriyan, Vjaceslav Georgiev +1
- **PDF**: https://arxiv.org/pdf/1609.01567v2
- **Abstract**: The development of multicore architectures supporting parallel data processing has led to a paradigm shift, which affects communication systems significantly. This article provides a scalable parallel approach of an iterative LDPC decoder, presented in a tutorial-based style. It is suitable for decoding any irregular LDPC code without the limitation of the maximum node degree, and it includes a parallel calculation of the syndrome. This is the main difference from algorithms presented so far. The proposed approach can be implemented in applications supporting massive parallel computing, such as GPU or FPGA devices. The implementation of the LDPC decoder with the use the OpenCL and CUDA frameworks is discussed and the performance evaluation is given at the end of this contribution.
