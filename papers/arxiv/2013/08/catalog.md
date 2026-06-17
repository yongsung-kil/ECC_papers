# arXiv — 2013-08


## Improving Sparse Associative Memories by Escaping from Bogus Fixed Points

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: arxiv:1308.6003v1
- **Type**: preprint
- **Published**: 2013-08-27
- **Authors**: Zhe Yao, Vincent Gripon, Michael Rabbat
- **PDF**: https://arxiv.org/pdf/1308.6003v1
- **Abstract**: The Gripon-Berrou neural network (GBNN) is a recently invented recurrent neural network embracing a LDPC-like sparse encoding setup which makes it extremely resilient to noise and errors. A natural use of GBNN is as an associative memory. There are two activation rules for the neuron dynamics, namely sum-of-sum and sum-of-max. The latter outperforms the former in terms of retrieval rate by a huge margin. In prior discussions and experiments, it is believed that although sum-of-sum may lead the network to oscillate, sum-of-max always converges to an ensemble of neuron cliques corresponding to previously stored patterns. However, this is not entirely correct. In fact, sum-of-max often converges to bogus fixed points where the ensemble only comprises a small subset of the converged state. By taking advantage of this overlooked fact, we can greatly improve the retrieval rate. We discuss this particular issue and propose a number of heuristics to push sum-of-max beyond these bogus fixed points. To tackle the problem directly and completely, a novel post-processing algorithm is also developed and customized to the structure of GBNN. Experimental results show that the new algorithm achieves a huge performance boost in terms of both retrieval rate and run-time, compared to the standard sum-of-max and all the other heuristics.

## Joint Phase Noise Estimation and Data Detection in Coded MIMO Systems

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: arxiv:1308.3772v1
- **Type**: preprint
- **Published**: 2013-08-17
- **Authors**: Arif O. Isikman, Hani Mehrpouyan, Ali A. Nasir +2
- **PDF**: https://arxiv.org/pdf/1308.3772v1
- **Abstract**: In this paper, the problem of joint oscillator phase noise (PHN) estimation and data detection for multi-input multi-output (MIMO) systems using bit-interleaved coded modulation (BICM) is analyzed. A new MIMO receiver that iterates between the estimator and the detector, based on the expectation-maximization (EM) framework, is proposed. It is shown that at high signal-to-noise ratios, a maximum a posteriori estimator (MAP) can be used to carry out the maximization step of the EM algorithm. Moreover, to reduce the computational complexity of the proposed EM algorithm, a soft decision-directed extended Kalman filter-smoother (EKFS) is applied instead of the MAP estimator to track the PHN parameters. Numerical results show that by combining the proposed EKFS based approach with an iterative detector that employs low density parity check (LDPC) codes, PHN can be accurately tracked. Simulations also demonstrate that compared to existing algorithms, the proposed iterative receiver can significantly enhance the performance of MIMO systems in the presence of PHN.

## On Characterization of Elementary Trapping Sets of Variable-Regular LDPC Codes

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: arxiv:1308.1259v1
- **Type**: preprint
- **Published**: 2013-08-06
- **Authors**: Mehdi Karimi, Amir H. Banihashemi
- **PDF**: https://arxiv.org/pdf/1308.1259v1
- **Abstract**: In this paper, we study the graphical structure of elementary trapping sets (ETS) of variable-regular low-density parity-check (LDPC) codes. ETSs are known to be the main cause of error floor in LDPC coding schemes. For the set of LDPC codes with a given variable node degree $d_l$ and girth $g$, we identify all the non-isomorphic structures of an arbitrary class of $(a,b)$ ETSs, where $a$ is the number of variable nodes and $b$ is the number of odd-degree check nodes in the induced subgraph of the ETS. Our study leads to a simple characterization of dominant classes of ETSs (those with relatively small values of $a$ and $b$) based on short cycles in the Tanner graph of the code. For such classes of ETSs, we prove that any set ${\cal S}$ in the class is a layered superset (LSS) of a short cycle, where the term "layered" is used to indicate that there is a nested sequence of ETSs that starts from the cycle and grows, one variable node at a time, to generate ${\cal S}$. This characterization corresponds to a simple search algorithm that starts from the short cycles of the graph and finds all the ETSs with LSS property in a guaranteed fashion. Specific results on the structure of ETSs are presented for $d_l = 3, 4, 5, 6$, $g = 6, 8$ and $a, b \leq 10$ in this paper. The results of this paper can be used for the error floor analysis and for the design of LDPC codes with low error floors.
