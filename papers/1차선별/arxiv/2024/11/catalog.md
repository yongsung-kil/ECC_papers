# arXiv — 2024-11 (1차선별 통과)


## Neural Window Decoder for SC-LDPC Codes

- **Status**: ✅
- **Reason**: C/E: SC-LDPC용 신경 윈도우 디코더(NWD) — trainable weight/damping, CN update 41% 생략, 에러전파 완화 새 디코더 기법, 바이너리 대상
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: arxiv:2411.19092v2
- **Type**: preprint
- **Published**: 2024-11-28
- **Authors**: Dae-Young Yun, Hee-Youl Kwak, Yongjune Kim +2
- **PDF**: https://arxiv.org/pdf/2411.19092v2
- **Abstract**: In this paper, we propose a neural window decoder (NWD) for spatially coupled low-density parity-check (SC-LDPC) codes. The proposed NWD retains the conventional window decoder (WD) process but incorporates trainable neural weights. To train the weights of NWD, we introduce two novel training strategies. First, we restrict the loss function to target variable nodes (VNs) of the window, which prunes the neural network and accordingly enhances training efficiency. Second, we employ the active learning technique with a normalized loss term to prevent the training process from biasing toward specific training regions. Next, we develop a systematic method to derive non-uniform schedules for the NWD based on the training results. We introduce trainable damping factors that reflect the relative importance of check node (CN) updates. By skipping updates with less importance, we can omit $\mathbf{41\%}$ of CN updates without performance degradation compared to the conventional WD. Lastly, we address the error propagation problem inherent in SC-LDPC codes by deploying a complementary weight set, which is activated when an error is detected in the previous window. This adaptive decoding strategy effectively mitigates error propagation without requiring modifications to the code and decoder structures.
