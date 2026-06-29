# arXiv — 2026-03 (1차선별 통과)


## Exploiting the Degrees of Freedom: Multi-Dimensional Spatially-Coupled Codes Based on Gradient Descent

- **Status**: ✅
- **Reason**: 다차원 SC-LDPC 코드 설계, 유한길이 최적화·사이클/girth 제거를 스토리지·전송 시스템 대상으로 — 카테고리 E 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: arxiv:2603.25824v1
- **Type**: preprint
- **Published**: 2026-03-26
- **Authors**: Ata Tanrıkulu, Mete Yıldırım, Ahmed Hareedy
- **PDF**: https://arxiv.org/pdf/2603.25824v1
- **Abstract**: Spatially-coupled (SC) codes are a class of low-density parity-check (LDPC) codes that is gaining increasing attention. Multi-dimensional (MD) SC codes are constructed by connecting copies of an SC code via relocations in order to mitigate various sources of non-uniformity and improve performance in many storage and transmission systems. As the number of degrees of freedom in the MD-SC code design increases, appropriately exploiting them becomes more difficult because of the complexity growth of the design process. In this paper, we propose a probabilistic framework for the MD-SC code design, based on the gradient-descent (GD) algorithm, to design high performance MD codes where this challenge is addressed. In particular, we express the expected number of detrimental objects, which we seek to minimize, in the graph representation of the code in terms of entries of a probability-distribution matrix that characterizes the MD-SC code design. We then find a locally-optimal probability distribution, which serves as the starting point of the finite-length (FL) algorithmic optimizer that produces the final MD-SC code. We adopt a recently-introduced Markov chain Monte Carlo (MCMC) FL algorithmic optimizer that is guided by the proposed GD algorithm. We apply our framework to various objects of interest. We start from simple short cycles, and then we develop the framework to address more sophisticated cycle concatenations, aiming at finer-grained optimization. We offer the theoretical analysis as well as the design algorithms. Next, we present experimental results demonstrating that our MD codes, conveniently called GD-MD codes, have notably lower numbers of targeted detrimental objects compared with the available state-of-the-art. Moreover, we show that our GD-MD codes exhibit significant improvements in error-rate performance compared with MD-SC codes obtained by a uniform distribution.

## Learning to Decode Quantum LDPC Codes Via Belief Propagation

- **Status**: ✅
- **Reason**: BP 디코딩 + 강화학습 스케줄링/증분 업데이트 — 양자 대상이나 BP 개선·학습 스케줄 기법이 NAND LDPC 디코더로 이식 가능성(C, 애매시 in)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: arxiv:2603.10192v1
- **Type**: preprint
- **Published**: 2026-03-10
- **Authors**: Mohsen Moradi, Vahid Nourozi, Salman Habib +1
- **PDF**: https://arxiv.org/pdf/2603.10192v1
- **Abstract**: Belief-propagation (BP) decoding for quantum low-density parity-check (QLDPC) codes is appealing due to its low complexity, yet it often exhibits convergence issues due to quantum degeneracy and short cycles that exist in the Tanner graph. To overcome this challenge, this paper proposes a reinforcement-learning (RL) approach that learns (offline) how to decode QLDPC codes based on sequential decoding trajectories. The decoding is formulated as a Markov decision process with a local, syndrome-driven state representation of the underlying RL agent. To enable fast inference, critical for practical implementation, we incrementally update our RL-based QLDPC decoder using second-order neighborhoods that avoid global rescans. Simulation results on representative QLDPC codes demonstrate the superiority of the proposed RL-based QLDPC decoders in terms of performance and convergence speed when compared to flooding and random sequential schedules, while achieving performance competitive with state-of-the-art BP-based decoders at comparable complexity.
