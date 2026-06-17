# arXiv — 2012-07


## LT Codes For Efficient and Reliable Distributed Storage Systems Revisited

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: arxiv:1207.5542v1
- **Type**: preprint
- **Published**: 2012-07-23
- **Authors**: Yongge Wang
- **PDF**: https://arxiv.org/pdf/1207.5542v1
- **Abstract**: LT codes and digital fountain techniques have received significant attention from both academics and industry in the past few years. There have also been extensive interests in applying LT code techniques to distributed storage systems such as cloud data storage in recent years. However, Plank and Thomason's experimental results show that LDPC code performs well only asymptotically when the number of data fragments increases and it has the worst performance for small number of data fragments (e.g., less than 100). In their INFOCOM 2012 paper, Cao, Yu, Yang, Lou, and Hou proposed to use exhaustive search approach to find a deterministic LT code that could be used to decode the original data content correctly in distributed storage systems. However, by Plank and Thomason's experimental results, it is not clear whether the exhaustive search approach will work efficiently or even correctly. This paper carries out the theoretical analysis on the feasibility and performance issues for applying LT codes to distributed storage systems. By employing the underlying ideas of efficient Belief Propagation (BP) decoding process in LT codes, this paper introduces two classes of codes called flat BP-XOR codes and array BP-XOR codes (which can be considered as a deterministic version of LT codes). We will show the equivalence between the edge-colored graph model and degree-one-and-two encoding symbols based array BP-XOR codes. Using this equivalence result, we are able to design general array BP-XOR codes using graph based results. Similarly, based on this equivalence result, we are able to get new results for edge-colored graph models using results from array BP-XOR codes.

## Finite Alphabet Iterative Decoders, Part I: Decoding Beyond Belief Propagation on BSC

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: arxiv:1207.4800v1
- **Type**: preprint
- **Published**: 2012-07-19
- **Authors**: Shiva Kumar Planjery, David Declercq, Ludovic Danjean +1
- **PDF**: https://arxiv.org/pdf/1207.4800v1
- **Abstract**: We introduce a new paradigm for finite precision iterative decoding on low-density parity-check codes over the Binary Symmetric channel. The messages take values from a finite alphabet, and unlike traditional quantized decoders which are quantized versions of the Belief propagation (BP) decoder, the proposed finite alphabet iterative decoders (FAIDs) do not propagate quantized probabilities or log-likelihoods and the variable node update functions do not mimic the BP decoder. Rather, the update functions are maps designed using the knowledge of potentially harmful subgraphs that could be present in a given code, thereby rendering these decoders capable of outperforming the BP in the error floor region. On certain column-weight-three codes of practical interest, we show that there exist 3-bit precision FAIDs that surpass the BP decoder in the error floor. Hence, FAIDs are able to achieve a superior performance at much lower complexity. We also provide a methodology for the selection of FAIDs that is not code-specific, but gives a set of candidate FAIDs containing potentially good decoders in the error floor region for any column-weight-three code. We validate the code generality of our methodology by providing particularly good three-bit precision FAIDs for a variety of codes with different rates and lengths.

## Analysis and Optimization of a Frequency-Hopping Ad Hoc Network in Rayleigh Fading

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: arxiv:1207.3451v1
- **Type**: preprint
- **Published**: 2012-07-14
- **Authors**: Salvatore Talarico, Matthew C. Valenti, Don Torrieri
- **PDF**: https://arxiv.org/pdf/1207.3451v1
- **Abstract**: This paper proposes a new method for optimizing frequency-hopping ad hoc networks in the presence of Rayleigh fading. It is assumed that the system uses a capacity-approaching code (e.g., turbo or LDPC) and noncoherent binary continuous-phase frequency-shift keying (CPFSK) modulation. By using transmission capacity as the performance metric, the number of hopping channels, CPFSK modulation index, and code rate are jointly optimized. Mobiles in the network are assumed to be uniformly located within a finite area. Closed-form expressions for outage probability are given for a network characterized by a physical interference channel. The outage probability is first found conditioned on the locations of the mobiles, and then averaged over the spatial distribution of the mobiles. The transmission capacity, which is a measure of the spatial spectral efficiency, is obtained from the outage probability. The transmission capacity is modified to account for the constraints of the CPFSK modulation and capacity-approaching coding. Two optimization methods are proposed for maximizing the transmission capacity. The first is a brute-force method and the second is a gradient-search algorithm. The results obtained from the optimization shed new insight into the fundamental tradeoffs among the number of frequency-hopping channels, the modulation index, and the rate of the error-correcting code.

## Quantum LDPC Codes Constructed from Point-Line Subsets of the Finite Projective Plane

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: arxiv:1207.0732v1
- **Type**: preprint
- **Published**: 2012-07-03
- **Authors**: Jacob Farinholt
- **PDF**: https://arxiv.org/pdf/1207.0732v1
- **Abstract**: Due to their fast decoding algorithms, quantum generalizations of low-density parity check, or LDPC, codes have been investigated as a solution to the problem of decoherence in fragile quantum states. However, the additional twisted inner product requirements of quantum stabilizer codes force four-cycles and eliminate the possibility of randomly generated quantum LDPC codes. Moreover, the classes of quantum LDPC codes discovered thus far generally have unknown or small minimum distance, or a fixed rate. This paper presents several new classes of quantum LDPC codes constructed from finite projective planes. These codes have rates that increase with the block length $n$ and minimum weights proportional to $n^{1/2}$.
