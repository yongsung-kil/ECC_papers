# arXiv — 2025-09


## Decoding quantum low density parity check codes with diffusion

- **Status**: ❌
- **Reason**: Quantum LDPC (bivariate bicycle) syndrome decoding for QEC; quantum EC domain, excluded per criteria.
- **ID**: arxiv:2509.22347v1
- **Type**: preprint
- **Published**: 2025-09-26
- **Authors**: Zejun Liu, Anqi Gong, Bryan K. Clark
- **PDF**: https://arxiv.org/pdf/2509.22347v1
- **Abstract**: An efficient decoder is essential for quantum error correction, and data-driven neural decoders have emerged as promising, flexible solutions. Here, we introduce a diffusion model framework to infer logical errors from syndrome measurements in quantum low-density parity-check codes. Using the bivariate bicycle code with realistic circuit-level noise, we show that masked diffusion decoders are more accurate, often faster on average, and always faster in the worst case than other state-of-the-art decoders, including belief propagation with ordered statistics decoding (BP-OSD) and autoregressive neural decoders. We show that by using fewer diffusion steps during inference one can gain significant speed at minimal cost in accuracy. By examining the factored attention from our trained neural network we find that, despite being trained solely on paired samples of syndrome-logical errors, this diffusion decoder learns the structure of the quantum codes. We also compare both masked and continuous diffusion decoders on code-capacity noise models, finding that masked diffusion decoders scale better than continuous diffusion decoders.

## From Indexing to Coding: A New Paradigm for Data Availability Sampling

- **Status**: ❌
- **Reason**: Blockchain data availability sampling via RLNC; erasure/network coding application, no transferable NAND LDPC ECC technique.
- **ID**: arxiv:2509.21586v2
- **Type**: preprint
- **Published**: 2025-09-25
- **Authors**: Moritz Grundei, Vipindev Adat Vasudevan, Kishori Konwar +1
- **PDF**: https://arxiv.org/pdf/2509.21586v2
- **Abstract**: The data availability problem is a central challenge in blockchain systems and lies at the core of the accessibility and scalability issues faced by platforms such as Ethereum. Modern solutions employ several approaches, with data availability sampling (DAS) being the most self-sufficient and minimalistic in its security assumptions. Existing DAS methods typically form cryptographic commitments on codewords of fixed-rate erasure codes, which restrict light nodes to sampling from a predetermined set of coded symbols.   In this paper, we introduce a new approach to DAS that modularizes the coding and commitment process by committing to the uncoded data while performing sampling through on-the-fly coding. The resulting samples are significantly more expressive, enabling light nodes to obtain, in concrete implementations, up to multiple orders of magnitude stronger assurances of data availability than from sampling pre-committed symbols from a fixed-rate redundancy code as done in established DAS schemes using Reed Solomon or low density parity check codes. We present a concrete protocol that realizes this paradigm using random linear network coding (RLNC).

## Sparse Regression LDPC Codes for the Block-Fading Non-Coherent SIMO Channel

- **Status**: ❌
- **Reason**: Uses non-binary NB-LDPC outer code with SPARCs/AMP for fading SIMO; non-binary LDPC excluded.
- **ID**: arxiv:2509.16376v1
- **Type**: preprint
- **Published**: 2025-09-19
- **Authors**: Alexander Fengler, Burak Çakmak, Giuseppe Caire
- **PDF**: https://arxiv.org/pdf/2509.16376v1
- **Abstract**: Sparse regression codes (SPARCs) are a class of codes that encode information through the superposition of columns of a randomised coding matrix. The combination with an outer non-binary low density parity check (NB-LDPC) code was recently shown to improve the finite-length performance of these codes over the unfaded AWGN channel. In this paper, we propose a low-complexity approximate message passing (AMP) decoder that is capable of decoding NB-LDPC encoded SPARCs on a Rayleigh fading channel with multiple receive antennas. Notably, the decoder does not require channel state information (CSI), i.e., it is fully non-coherent, but achieves the same error probability as a decoder with full CSI, even for moderate block lengths. This is achieved by iteratively re-estimating the channel throughout the decoding iterations. In addition, we provide a rigorous asymptotic analysis of both the block error probability and the channel estimation error. Numerical results confirm the precision of the analysis and show that the presented coding scheme performs within 1.5 dB of the outage capacity and is competitive with coded modulation schemes employing standardised LDPC codes for 5G cellular networks and pilot-based channel estimation.

## Decoded Quantum Interferometry Requires Structure

- **Status**: ❌
- **Reason**: Quantum optimization (DQI/MAX-k-XOR-SAT) theoretical bounds using LDPC ensembles; no decoder/HW/code-design contribution to extract.
- **ID**: arxiv:2509.14509v1
- **Type**: preprint
- **Published**: 2025-09-18
- **Authors**: Eric R. Anschuetz, David Gamarnik, Jonathan Z. Lu
- **PDF**: https://arxiv.org/pdf/2509.14509v1
- **Abstract**: We study the performance of Decoded Quantum Interferometry (DQI) on typical instances of MAX-$k$-XOR-SAT when the transpose of the constraint matrix is drawn from a standard ensemble of LDPC parity check matrices. We prove that if the decoding step of DQI corrects up to the folklore efficient decoding threshold for LDPC codes, then DQI is obstructed by a topological feature of the near-optimal space of solutions known as the overlap gap property (OGP). As the OGP is widely conjectured to exactly characterize the performance of state-of-the-art classical algorithms, this result suggests that DQI has no quantum advantage in optimizing unstructured MAX-$k$-XOR-SAT instances. We also give numerical evidence supporting this conjecture by showing that approximate message passing (AMP)--a classical algorithm conjectured to saturate the OGP threshold--outperforms DQI on a related ensemble of MAX-$k$-XOR-SAT instances. Finally, we prove that depth-$1$ QAOA outperforms DQI at sufficiently large $k$ under the same decoding threshold assumption.   Our result follows by showing that DQI is approximately Lipschitz under the quantum Wasserstein metric over many standard ensembles of codes. We then prove that MAX-$k$-XOR-SAT exhibits both an OGP and a related topological obstruction known as the chaos property; this is the first known OGP threshold for MAX-$k$-XOR-SAT at fixed $k$, which may be of independent interest. Finally, we prove that both of these topological properties inhibit approximately Lipschitz algorithms such as DQI from optimizing MAX-$k$-XOR-SAT to large approximation ratio.

## Towards solving industrial integer linear programs with Decoded Quantum Interferometry

- **Status**: ❌
- **Reason**: Quantum DQI for industrial ILP; BP implemented as quantum circuit, no classical NAND LDPC ECC technique to transfer.
- **ID**: arxiv:2509.08328v2
- **Type**: preprint
- **Published**: 2025-09-10
- **Authors**: Francesc Sabater, Ouns El Harzli, Geert-Jan Besjes +6
- **PDF**: https://arxiv.org/pdf/2509.08328v2
- **Abstract**: Optimization via decoded quantum interferometry (DQI) has recently gained a great deal of attention as a promising avenue for solving optimization problems using quantum computers. In this paper, we apply DQI to an industrial optimization problem in the automotive industry: the vehicle option-package pricing problem. Our main contributions are 1) formulating the industrial problem as an integer linear program (ILP), 2) converting the ILP into instances of max-XORSAT, and 3) developing a detailed quantum circuit implementation for belief propagation, a heuristic algorithm for decoding LDPC codes. Thus, we provide a full implementation of the DQI algorithm using Belief Propagation, which can be applied to any industrially relevant ILP by first transforming it into a max-XORSAT instance. We also evaluate the effectiveness of our implementation by benchmarking it against both Gurobi and a random sampling baseline.

## Compressing Syndrome Measurement Sequences

- **Status**: ❌
- **Reason**: Fault-tolerant quantum syndrome measurement scheduling for QEC codes; quantum EC domain, excluded.
- **ID**: arxiv:2509.07288v1
- **Type**: preprint
- **Published**: 2025-09-08
- **Authors**: Benjamin Anker, Milad Marvian
- **PDF**: https://arxiv.org/pdf/2509.07288v1
- **Abstract**: In this work, we analyze a framework for constructing fault-tolerant measurement schedules of varying lengths by combining stabilizer generators, and prove results about the distance of such schedules by combining according to classical codes. Using this framework, we produce explicit measurement schedules sufficient for fault-tolerant error correction of quantum codes of distance $d$ with $r$ independent stabilizer generators using only $O(d \log{r})$ measurements if the code is LDPC, and $O(d \log d \log r)$ measurements if the code is produced via concatenating a smaller code with itself $O(\log d)$ times. In both of these cases the number of measurements can be asymptotically fewer than the number of stabilizer generators which define the code. Although optimizing our construction to use the fewest measurements produces high-weight stabilizers, we also show that we can reduce the number of measurements used for specific examples while maintaining low-weight stabilizer measurements. We numerically examine the performance of our construction on the surface code under several noise models and demonstrate the exponential error suppression with increasing distance which is characteristic of weak fault tolerance.

## Study of Iterative Detection, Decoding and Channel Estimation for RIS-Aided MIMO Networks

- **Status**: ❌
- **Reason**: RIS-aided MIMO 채널추정에 LDPC를 부수적으로 활용; 떼어낼 새 디코더/HW/코드설계 기법 없음 (무선 응용 특이적)
- **ID**: arxiv:2509.05875v1
- **Type**: preprint
- **Published**: 2025-09-07
- **Authors**: Roberto C. G. Porto, Rodrigo C. de Lamare
- **PDF**: https://arxiv.org/pdf/2509.05875v1
- **Abstract**: This work proposes an iterative detection, decoding and channel estimation scheme for multiple-antenna systems assisted by multiple reflective intelligent surfaces (RIS). A novel channel estimation technique that exploits low-density parity-check (LDPC) codes and iterative processing is developed to enhance estimation accuracy while reducing the number of required pilot symbols. The key idea is to exploit encoded pilots to improve the iterative process, enabling the use of not only pilot bits but also parity bits from the coded packet to refine channel estimation. Simulations analyze a sub-6 GHz scenario where the channel propagation is not sparse and multiple RIS are deployed, considering both LOS and NLOS conditions. Numerical results show significant performance gains for the proposed scheme and estimator over competing approaches.

## List Decoding Expander-Based Codes via Fast Approximation of Expanding CSPs: I

- **Status**: ❌
- **Reason**: expander/Tanner LDPC의 near-linear list decoding 순수 이론; alphabet size 비이진 대형이며 디코더/HW 구현으로 이어지지 않는 이론 bound
- **ID**: arxiv:2509.05203v1
- **Type**: preprint
- **Published**: 2025-09-05
- **Authors**: Fernando Granha Jeronimo, Aman Singh
- **PDF**: https://arxiv.org/pdf/2509.05203v1
- **Abstract**: We present near-linear time list decoding algorithms (in the block-length $n$) for expander-based code constructions. More precisely, we show that   (i) For every $δ\in (0,1)$ and $ε> 0$, there is an explicit family of good Tanner LDPC codes of (design) distance $δ$ that is $(δ- ε, O_\varepsilon(1))$ list decodable in time $\widetilde{\mathcal{O}}_{\varepsilon}(n)$ with alphabet size $O_δ(1)$,   (ii) For every $R \in (0,1)$ and $ε> 0$, there is an explicit family of AEL codes of rate $R$, distance $1-R -\varepsilon$ that is $(1-R-ε, O_\varepsilon(1))$ list decodable in time $\widetilde{\mathcal{O}}_{\varepsilon}(n)$ with alphabet size $\text{exp}(\text{poly}(1/ε))$, and   (iii) For every $R \in (0,1)$ and $ε> 0$, there is an explicit family of AEL codes of rate $R$, distance $1-R-\varepsilon$ that is $(1-R-ε, O(1/ε))$ list decodable in time $\widetilde{\mathcal{O}}_{\varepsilon}(n)$ with alphabet size $\text{exp}(\text{exp}(\text{poly}(1/ε)))$ using recent near-optimal list size bounds from [JMST25].   Our results are obtained by phrasing the decoding task as an agreement CSP [RWZ20,DHKNT19] on expander graphs and using the fast approximation algorithm for $q$-ary expanding CSPs from [Jer23], which is based on weak regularity decomposition [JST21,FK96]. Similarly to list decoding $q$-ary Ta-Shma's codes in [Jer23], we show that it suffices to enumerate over assignments that are constant in each part (of the constantly many) of the decomposition in order to recover all codewords in the list.
