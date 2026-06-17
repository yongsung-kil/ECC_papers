# arXiv — 2014-11


## Impact of redundant checks on the LP decoding thresholds of LDPC codes

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: arxiv:1411.7554v3
- **Type**: preprint
- **Published**: 2014-11-27
- **Authors**: Louay Bazzi, Hani Audah
- **PDF**: https://arxiv.org/pdf/1411.7554v3
- **Abstract**: Feldman et al.(2005) asked whether the performance of the LP decoder can be improved by adding redundant parity checks to tighten the LP relaxation. We prove that for LDPC codes, even if we include all redundant checks, asymptotically there is no gain in the LP decoder threshold on the BSC under certain conditions on the base Tanner graph. First, we show that if the graph has bounded check-degree and satisfies a condition which we call asymptotic strength, then including high degree redundant checks in the LP does not significantly improve the threshold in the following sense: for each constant delta>0, there is a constant k>0 such that the threshold of the LP decoder containing all redundant checks of degree at most k improves by at most delta upon adding to the LP all redundant checks of degree larger than k. We conclude that if the graph satisfies a rigidity condition, then including all redundant checks does not improve the threshold of the base LP. We call the graph asymptotically strong if the LP decoder corrects a constant fraction of errors even if the LLRs of the correct variables are arbitrarily small. By building on the work of Feldman et al.(2007) and Viderman(2013), we show that asymptotic strength follows from sufficiently large expansion. We also give a geometric interpretation of asymptotic strength in terms pseudocodewords. We call the graph rigid if the minimum weight of a sum of check nodes involving a cycle tends to infinity as the block length tends to infinity. Under the assumptions that the graph girth is logarithmic and the minimum check degree is at least 3, rigidity is equivalent to the nondegeneracy property that adding at least logarithmically many checks does not give a constant weight check. We argue that nondegeneracy is a typical property of random check-regular graphs.

## Optical Time-Frequency Packing: Principles, Design, Implementation, and Experimental Demonstration

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: arxiv:1411.6892v2
- **Type**: preprint
- **Published**: 2014-11-25
- **Authors**: Marco Secondini, Tommaso Foggi, Francesco Fresi +7
- **PDF**: https://arxiv.org/pdf/1411.6892v2
- **Abstract**: Time-frequency packing (TFP) transmission provides the highest achievable spectral efficiency with a constrained symbol alphabet and detector complexity. In this work, the application of the TFP technique to fiber-optic systems is investigated and experimentally demonstrated. The main theoretical aspects, design guidelines, and implementation issues are discussed, focusing on those aspects which are peculiar to TFP systems. In particular, adaptive compensation of propagation impairments, matched filtering, and maximum a posteriori probability detection are obtained by a combination of a butterfly equalizer and four 8-state parallel Bahl-Cocke-Jelinek-Raviv (BCJR) detectors. A novel algorithm that ensures adaptive equalization, channel estimation, and a proper distribution of tasks between the equalizer and BCJR detectors is proposed. A set of irregular low-density parity-check codes with different rates is designed to operate at low error rates and approach the spectral efficiency limit achievable by TFP at different signal-to-noise ratios. An experimental demonstration of the designed system is finally provided with five dual-polarization QPSK-modulated optical carriers, densely packed in a 100 GHz bandwidth, employing a recirculating loop to test the performance of the system at different transmission distances.

## Design of Spatially Coupled LDPC Codes over GF(q) for Windowed Decoding

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: arxiv:1411.4373v1
- **Type**: preprint
- **Published**: 2014-11-17
- **Authors**: Lai Wei, David G. M. Mitchell, Thomas E. Fuja +1
- **PDF**: https://arxiv.org/pdf/1411.4373v1
- **Abstract**: In this paper we consider the generalization of binary spatially coupled low-density parity-check (SC-LDPC) codes to finite fields GF$(q)$, $q\geq 2$, and develop design rules for $q$-ary SC-LDPC code ensembles based on their iterative belief propagation (BP) decoding thresholds, with particular emphasis on low-latency windowed decoding (WD). We consider transmission over both the binary erasure channel (BEC) and the binary-input additive white Gaussian noise channel (BIAWGNC) and present results for a variety of $(J,K)$-regular SC-LDPC code ensembles constructed over GF$(q)$ using protographs. Thresholds are calculated using protograph versions of $q$-ary density evolution (for the BEC) and $q$-ary extrinsic information transfer analysis (for the BIAWGNC). We show that WD of $q$-ary SC-LDPC codes provides significant threshold gains compared to corresponding (uncoupled) $q$-ary LDPC block code (LDPC-BC) ensembles when the window size $W$ is large enough and that these gains increase as the finite field size $q=2^m$ increases. Moreover, we demonstrate that the new design rules provide WD thresholds that are close to capacity, even when both $m$ and $W$ are relatively small (thereby reducing decoding complexity and latency). The analysis further shows that, compared to standard flooding-schedule decoding, WD of $q$-ary SC-LDPC code ensembles results in significant reductions in both decoding complexity and decoding latency, and that these reductions increase as $m$ increases. For applications with a near-threshold performance requirement and a constraint on decoding latency, we show that using $q$-ary SC-LDPC code ensembles, with moderate $q>2$, instead of their binary counterparts results in reduced decoding complexity.

## Novel LDPC Decoder via MLP Neural Networks

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: arxiv:1411.3425v1
- **Type**: preprint
- **Published**: 2014-11-13
- **Authors**: Alireza Karami, Mahmoud Ahmadian Attari
- **PDF**: https://arxiv.org/pdf/1411.3425v1
- **Abstract**: In this paper, a new method for decoding Low Density Parity Check (LDPC) codes, based on Multi-Layer Perceptron (MLP) neural networks is proposed. Due to the fact that in neural networks all procedures are processed in parallel, this method can be considered as a viable alternative to Message Passing Algorithm (MPA), with high computational complexity. Our proposed algorithm runs with soft criterion and concurrently does not use probabilistic quantities to decide what the estimated codeword is. Although the neural decoder performance is close to the error performance of Sum Product Algorithm (SPA), it is comparatively less complex. Therefore, the proposed decoder emerges as a new infrastructure for decoding LDPC codes.

## Four-Dimensional Coded Modulation with Bit-wise Decoders for Future Optical Communications

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: arxiv:1411.0401v2
- **Type**: preprint
- **Published**: 2014-11-03
- **Authors**: Alex Alvarado, Erik Agrell
- **PDF**: https://arxiv.org/pdf/1411.0401v2
- **Abstract**: Coded modulation (CM) is the combination of forward error correction (FEC) and multilevel constellations. Coherent optical communication systems result in a four-dimensional (4D) signal space, which naturally leads to 4D-CM transceivers. A practically attractive design paradigm is to use a bit-wise decoder, where the detection process is (suboptimally) separated into two steps: soft-decision demapping followed by binary decoding. In this paper, bit-wise decoders are studied from an information-theoretic viewpoint. 4D constellations with up to 4096 constellation points are considered. Metrics to predict the post-FEC bit-error rate (BER) of bit-wise decoders are analyzed. The mutual information is shown to fail at predicting the post-FEC BER of bit-wise decoders and the so-called generalized mutual information is shown to be a much more robust metric. For the suboptimal scheme under consideration, it is also shown that constellations that transmit and receive information in each polarization and quadrature independently (e.g., PM-QPSK, PM-16QAM, and PM-64QAM) outperform the best 4D constellations designed for uncoded transmission. Theoretical gains are as high as 4 dB, which are then validated via numerical simulations of low-density parity check codes.
