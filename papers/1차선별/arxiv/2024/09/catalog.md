# arXiv — 2024-09 (1차선별 통과)


## An almost-linear time decoding algorithm for quantum LDPC codes under circuit-level noise

- **Status**: ✅
- **Reason**: BP+OTF 디코더 — BP에 ordered Tanner forest 후처리로 수렴 보장, 고전 바이너리 BP 기반 신규 디코더 기법으로 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: arxiv:2409.01440v2
- **Type**: preprint
- **Published**: 2024-09-02
- **Authors**: Antonio deMarti iOlius, Imanol Etxezarreta Martinez, Joschka Roffe +1
- **PDF**: https://arxiv.org/pdf/2409.01440v2
- **Abstract**: Fault-tolerant quantum computers must be designed in conjunction with classical co-processors that decode quantum error correction measurement information in real-time. In this work, we introduce the belief propagation plus ordered Tanner forest (BP+OTF) algorithm as an almost-linear time decoder for quantum low-density parity-check codes. The OTF post-processing stage removes qubits from the decoding graph until it has a tree-like structure. Provided that the resultant loop-free OTF graph supports a subset of qubits that can generate the syndrome, BP decoding is then guaranteed to converge. To enhance performance under circuit-level noise, we introduce a technique for sparsifying detector error models. This method uses a transfer matrix to map soft information from the full detector graph to the sparsified graph, preserving critical error propagation information from the syndrome extraction circuit. Our BP+OTF implementation first applies standard BP to the full detector graph, followed by BP+OTF post-processing on the sparsified graph. Numerical simulations show that the BP+OTF decoder achieves similar logical error suppression compared to state-of-the-art inversion-based and matching decoders for bivariate bicycle and surface codes, respectively, while maintaining almost-linear runtime complexity across all stages.
