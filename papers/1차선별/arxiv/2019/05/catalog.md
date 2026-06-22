# arXiv — 2019-05 (1차선별 통과)


## MIST: A Novel Training Strategy for Low-latency Scalable Neural Net Decoders

- **Status**: ✅
- **Reason**: 바이너리 LDPC용 신경망(CNN) 디코더 + MIST 학습전략 — 이식 가능 디코더(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: arxiv:1905.08990v1
- **Type**: preprint
- **Published**: 2019-05-22
- **Authors**: Kumar Yashashwi, Deepak Anand, Sibi Raj B Pillai +2
- **PDF**: https://arxiv.org/pdf/1905.08990v1
- **Abstract**: In this paper, we propose a low latency, robust and scalable neural net based decoder for convolutional and low-density parity-check (LPDC) coding schemes. The proposed decoders are demonstrated to have bit error rate (BER) and block error rate (BLER) performances at par with the state-of-the-art neural net based decoders while achieving more than 8 times higher decoding speed. The enhanced decoding speed is due to the use of convolutional neural network (CNN) as opposed to recurrent neural network (RNN) used in the best known neural net based decoders. This contradicts existing doctrine that only RNN based decoders can provide a performance close to the optimal ones. The key ingredient to our approach is a novel Mixed-SNR Independent Samples based Training (MIST), which allows for training of CNN with only 1\% of possible datawords, even for block length as high as 1000. The proposed decoder is robust as, once trained, the same decoder can be used for a wide range of SNR values. Finally, in the presence of channel outages, the proposed decoders outperform the best known decoders, {\it viz.} unquantized Viterbi decoder for convolutional code, and belief propagation for LDPC. This gives the CNN decoder a significant advantage in 5G millimeter wave systems, where channel outages are prevalent.
