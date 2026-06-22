# arXiv — 2019-05


## Cospectral Bipartite Graphs with the Same Degree Sequences but with Different Number of Large Cycles

- **Status**: ❌
- **Reason**: 사이클 개수 셈의 그래프이론적 negative result(순수 이론 bound), 떼어낼 코드설계·디코더 기법 없음
- **ID**: arxiv:1905.13228v1
- **Type**: preprint
- **Published**: 2019-05-31
- **Authors**: Ali Dehghan, Amir H. Banihashemi
- **PDF**: https://arxiv.org/pdf/1905.13228v1
- **Abstract**: Finding the multiplicity of cycles in bipartite graphs is a fundamental problem of interest in many fields including the analysis and design of low-density parity-check (LDPC) codes. Recently, Blake and Lin computed the number of shortest cycles ($g$-cycles, where $g$ is the girth of the graph) in a bi-regular bipartite graph, in terms of the degree sequences and the spectrum (eigenvalues of the adjacency matrix) of the graph [{\em IEEE Trans. Inform. Theory 64(10):6526--6535, 2018}]. This result was subsequently extended in [{\em IEEE Trans. Inform. Theory, accepted for publication, Dec. 2018}] to cycles of length $g+2, \ldots, 2g-2$, in bi-regular bipartite graphs, as well as $4$-cycles and $6$-cycles in irregular and half-regular bipartite graphs, with $g \geq 4$ and $g \geq 6$, respectively. In this paper, we complement these positive results with negative results demonstrating that the information of the degree sequences and the spectrum of a bipartite graph is, in general, insufficient to count (a) the $i$-cycles, $i \geq 2g$, in bi-regular graphs, (b) the $i$-cycles for any $i > g$, regardless of the value of $g$, and $g$-cycles for $g \geq 6$, in irregular graphs, and (c) the $i$-cycles for any $i > g$, regardless of the value of $g$, and $g$-cycles for $g \geq 8$, in half-regular graphs. To obtain these results, we construct counter-examples using the Godsil-McKay switching.

## MIST: A Novel Training Strategy for Low-latency Scalable Neural Net Decoders

- **Status**: ✅
- **Reason**: 바이너리 LDPC용 신경망(CNN) 디코더 + MIST 학습전략 — 이식 가능 디코더(C)
- **ID**: arxiv:1905.08990v1
- **Type**: preprint
- **Published**: 2019-05-22
- **Authors**: Kumar Yashashwi, Deepak Anand, Sibi Raj B Pillai +2
- **PDF**: https://arxiv.org/pdf/1905.08990v1
- **Abstract**: In this paper, we propose a low latency, robust and scalable neural net based decoder for convolutional and low-density parity-check (LPDC) coding schemes. The proposed decoders are demonstrated to have bit error rate (BER) and block error rate (BLER) performances at par with the state-of-the-art neural net based decoders while achieving more than 8 times higher decoding speed. The enhanced decoding speed is due to the use of convolutional neural network (CNN) as opposed to recurrent neural network (RNN) used in the best known neural net based decoders. This contradicts existing doctrine that only RNN based decoders can provide a performance close to the optimal ones. The key ingredient to our approach is a novel Mixed-SNR Independent Samples based Training (MIST), which allows for training of CNN with only 1\% of possible datawords, even for block length as high as 1000. The proposed decoder is robust as, once trained, the same decoder can be used for a wide range of SNR values. Finally, in the presence of channel outages, the proposed decoders outperform the best known decoders, {\it viz.} unquantized Viterbi decoder for convolutional code, and belief propagation for LDPC. This gives the CNN decoder a significant advantage in 5G millimeter wave systems, where channel outages are prevalent.
