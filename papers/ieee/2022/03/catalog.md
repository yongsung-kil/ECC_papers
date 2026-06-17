# IEEE Xplore — 2022-03


## Stopping-Set Assisted Reinforced Belief Propagation for Decoding Short LDPC Codes

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:9656848
- **Type**: journal
- **Published**: March 2022
- **Authors**: Asif Ali Zamzami, Kuan-Chuan Chao, Shih-Chun Lin
- **PDF**: https://ieeexplore.ieee.org/document/9656848
- **Abstract**: The low-density parity-check (LDPC) code is chosen to be a channel coding scheme for ultra-reliable and low-latency communications (URLLC) in 5G. However, short LDPC compromises the belief propagation (BP) decoder because of the stopping set (SS) in the decoding graph. We propose to perform different node operations according to the SS. A dynamic SS selection according to the received sequence is further applied. In the length 308 5G LDPC, our decoders outperform prior work, improving BP and collaborative BP at block error probability (BLER) of  $3 \times 10^{-5}$  by around 0.176 and 0.092 dB respectively, with almost the same number of iterations.

## Area- and Energy-Efficient LDPC Decoder Using Mixed-Resolution Check-Node Processing

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:9530762
- **Type**: journal
- **Published**: March 2022
- **Authors**: Sangbu Yun, Byeong Yong Kong, Youngjoo Lee
- **PDF**: https://ieeexplore.ieee.org/document/9530762
- **Abstract**: A practical min-sum algorithm is associated with tree-based comparison units for the check-node operation, being a major bottleneck in designing low-cost and energy-efficient low-density parity-check (LDPC) decoders. In this brief, we present a cost-effective LDPC decoder architecture by changing its internal computing resolution for the power-hungry check-node processing. The proposed mixed-resolution comparison offers significant advantages in terms of both area and energy, while achieving error-correcting performance within 0.3 dB of the previous normalized min-sum (NMS) algorithm for a (1644, 1408) quasi-cyclic LDPC code of the 5G New Radio specifications. Compared to the baseline NMS architecture, the proposed decoder in a 65-nm CMOS technology reduces the hardware complexity and the power consumption by 28.4% and 23.1%, respectively, enhancing the area efficiency by more than 88.2%.

## Advanced ISDB-T and ATSC 3.0 LDPC Codes Performance and Complexity Comparison

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:9665205
- **Type**: journal
- **Published**: March 2022
- **Authors**: Fadi Jerji, Cristiano Akamine
- **PDF**: https://ieeexplore.ieee.org/document/9665205
- **Abstract**: This paper presents a comparative performance and complexity analysis of the advanced ISDB-T and ATSC 3.0 Low-Density Parity-Check (LDPC) codes using the Sum-Product Algorithm and Min-Sum Algorithm LDPC decoders. The performance value for each of the code rates of the LDPC codes over an additive white Gaussian noise (AWGN) channel and Rayleigh fading channel is presented. The mathematical representation of each of the SPA and MSA decoders is presented along with the calculated and measured numerical complexity values.

## High-Throughput LDPC-CC Decoders Based on Storage, Arithmetic, and Control Improvements

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:9647009
- **Type**: journal
- **Published**: March 2022
- **Authors**: Yuxing Chen, Hangxuan Cui, Zhongfeng Wang
- **PDF**: https://ieeexplore.ieee.org/document/9647009
- **Abstract**: This brief presents high-throughput low-density parity-check convolutional code (LDPC-CC) decoders in full compliance with the IEEE 1901 standard. The decoding architecture is improved from storage, arithmetic, and control aspects. First, to address the throughput bottleneck caused by memory bandwidth, we propose two methods, register-based and categorized memory-based (CMem-based) storage schemes. Then, the arithmetic improvement is extensively exploited for better area. Besides, the control unit is well-designed to reduce the hardware complexity. Equipped with these techniques, efficient LDPC-CC decoders for IEEE 1901 standard are developed and implemented with 55nm technology. Implementation results demonstrate that the proposed decoders can achieve more than twice the throughput of existing decoders. Furthermore, the proposed CMem-based decoder improves the area efficiency by 84.5%.

## Multilevel Coding for Physical-Layer Security

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:9690167
- **Type**: journal
- **Published**: March 2022
- **Authors**: Johannes Pfeiffer, Robert F.H. Fischer
- **PDF**: https://ieeexplore.ieee.org/document/9690167
- **Abstract**: In any transmission scheme, security against eavesdroppers is of importance. Contrary to classical encryption, security directly at the physical layer can be achieved by applying suited coding and modulation schemes. In this paper, coded modulation schemes, i.e., the use of higher-order constellations, is studied for generating both security against a wiretapper and reliability for the legitimate user. Specifically, a multilevel coding (MLC) scheme is considered. The influence of the constellation, in particular its cardinality and its dimensionality, on the gained security is assessed. As LSB component code, a practical secure coding scheme based on punctured LDPC codes is used. The security level for the employed LDPC code ensembles within MLC constructions is examined with an adapted density evolution technique. Results from numerical simulations cover the theoretical considerations and match with the derived asymptotic behavior. The results are compared to the situation when straightforwardly applying a binary code according to the BICM approach.

## A Polygonal Line Min-Sum Decoding Scheme for Low Density Parity Check Codes

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:9520687
- **Type**: journal
- **Published**: March 2022
- **Authors**: Yin Xu, Hao Ju, Dazhi He +4
- **PDF**: https://ieeexplore.ieee.org/document/9520687
- **Abstract**: Low-density parity-check (LDPC) codes are widely used as error correction codes in new generation digital TV standards, such as the second generation of terrestrial digital video broadcasting standard (DVB-T2), Advanced Television Systems Committee (ATSC) 3.0, etc. The nonlinear belief propagation (BP) algorithm has excellent decoding performance for LDPC codes, but is often simplified in hardware implementations by linear min-sum (MS) algorithm due to its high complexity. This simplification also leads to over-estimation problems, which can be corrected by adding factors in conventional algorithms (e.g., normalized min-sum (NMS), offset min-sum (OMS), and variable scaling normalized min-sum (VMS) algorithms). However, the correction factors of these modified MS algorithms cannot adapt to different channels and modulations, and the performance needs further improvement. In this paper, the concepts of over-estimation value (OEV) and over-estimation rate (OER) are introduced to describe the over-estimation problem of the MS algorithm. Then, under the guidance of OEV and OER, a polygonal line min-sum (PMS) algorithm with correction factors adapted to different channels and modulations is proposed according to LLR distribution. Following the properties of OEV and OER, PMS algorithm is further simplified into Simplified PMS (SPMS) algorithm. LDPC codes from ATSC 3.0 are adopted in this paper to evaluate SPMS algorithm in comparison with the conventional algorithms. Extensive simulation results show that the SPMS algorithm for ATSC 3.0 LDPC decoder has at most 1.61dB, 0.24dB and 0.36dB gain over NMS, OMS and VMS algorithms respectively when frame error rate (FER) is at 10−4 level over additive white Gaussian noise (AWGN) channel with QPSK modulation. More importantly, the simulation results show that the SPMS algorithm can achieve much better performance than these modified MS algorithms over AWGN and Rayleigh channel with higher-order modulations or under limited maximum iteration number.

## Error Floor Analysis of LDPC Column Layered Decoders

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:9656896
- **Type**: journal
- **Published**: March 2022
- **Authors**: Ali Farsiabi, Amir H. Banihashemi
- **PDF**: https://ieeexplore.ieee.org/document/9656896
- **Abstract**: In this letter, we analyze the error floor of column layered decoders, also known as shuffled decoders, for low-density parity-check (LDPC) codes under saturating sum-product algorithm (SPA). To estimate the error floor, we evaluate the failure rate of different trapping sets (TSs) that contribute to the frame error rate in the error floor region. For each such TS, we model the dynamics of SPA in the vicinity of the TS by a linear state-space model that incorporates the information of the layered message-passing schedule. Consequently, the model parameters and the failure rate of the TS change as a result of the change in the order by which the messages of different layers are updated. This, in turn, causes the error floor of the code to change as a function of scheduling. Based on the proposed analysis, we then devise an efficient search algorithm to find a schedule that minimizes the error floor. Simulation results are presented to verify the accuracy of the proposed error floor estimation technique.

## QC-LDPC Codes With Large Column Weight and Free of Small Size ETSs

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:9663353
- **Type**: journal
- **Published**: March 2022
- **Authors**: Farzane Amirzade, Mohammad-Reza Sadeghi, Daniel Panario
- **PDF**: https://ieeexplore.ieee.org/document/9663353
- **Abstract**: An approach to improve the performance of QC-LDPC codes is the removal of harmful trapping sets by increasing the girth. However, constructing these LDPC codes with large column weights and girth more than 8 is not easy. We are concerned with protograph-based LDPC codes with large column weights and free of small size trapping sets. We use the edge-coloring technique and some concepts from graph theory such as rainbow cycles to show that for large column weights the removal of all 8-cycles but the ones we call  $\textit {rainbow 8-cycle}$  causes the elimination of several small size trapping sets. We provide a detailed theoretical analysis of these harmful trapping sets. Then, we apply them to array-based LDPC codes to significantly simplify and optimize the necessary and sufficient conditions to eliminate those 8-cycles from the Tanner graph. The given exponent matrices and simulation results show the impact of this simplification and the removal of the above mentioned 8-cycles.

## Improving Asymptotic Properties of Loop Construction of SC-LDPC Chains Over the BEC

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:9663207
- **Type**: journal
- **Published**: March 2022
- **Authors**: Alireza Eshraghi Dehaghani, Mohammad-Reza Sadeghi, Farzane Amirzade
- **PDF**: https://ieeexplore.ieee.org/document/9663207
- **Abstract**: Single SC-LDPC chains are known to provide protographs of SC-LDPC codes. These chains can be connected together and create new constructions which provide multi-dimensional (MD) SC-LDPC codes. The loop is one of the most important constructions that has been introduced so far. We propose a new method to construct code ensembles that are based on a combination of the small single chains and the loop construction. The numerical results show that our new ensembles have better iterative decoding thresholds and lower decoding complexity required to achieve a specific bit erasure probability than the single chain ensembles and the loop ensembles in a wide range of rates over the BEC. Moreover, similar to the single chain and the loop ensembles, the new ensembles are asymptotically good in terms of minimum distance.

## Efficient First Four Minimum Values Finder for NB-LDPC Decoders With Compressed Messages

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:9583586
- **Type**: journal
- **Published**: March 2022
- **Authors**: Thang Xuan Pham, Hanho Lee
- **PDF**: https://ieeexplore.ieee.org/document/9583586
- **Abstract**: Trellis min-max algorithm based nonbinary low-density parity-check (NB-LDPC) decoders with compressed messages offer promising performance compared with their conventional counterparts. Recent studies have shown that reducing check-node output information to a set of four most reliable intrinsic messages strikes a balance between the hardware complexity and error-correcting performance of the decoder. Therefore, an efficient architecture to find the first four minimum values (F4M) from a given set of values is greatly required. This brief proposes an algorithm to derive F4M from two four-sorted sequences, with subsequent efficient tree structure based architecture to construct the F4M finder. To demonstrate the hardware efficiency, the proposed F4M finder architecture implementations using TSMC 90-nm CMOS technology were conducted. Experimental results confirmed that the latency of the proposed F4M finder was approximately halved compared with that of design in the state-of-the-art work. In particular, the proposed F4M finder architecture can be adopted to further improve the performance of the NB-LDPC decoders.

## Hard Reliability-Based Ordered Statistic Decoding and Its Application to McEliece Public Key Cryptosystem

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:9658510
- **Type**: journal
- **Published**: March 2022
- **Authors**: Shuyan Yu, Qin Huang
- **PDF**: https://ieeexplore.ieee.org/document/9658510
- **Abstract**: This letter constructs the hard reliability from the syndromes to decode low/moderate-density parity-check codes in an ordered statistic way. For regular codes with our proposed decoding algorithm, the error-correction capability can be determined by the column weight and the maximum column intersection of their parity-check matrices. Then, an upper bound is derived to verify their decoding performance in ultra-low region, which may be required by some applications, e.g., McEliece public key cryptosystem and optical communications. It allows us to reduce the size of McEliece public keys with strong security levels due to its good error-correction capability.

## Tail Latency Optimization for LDPC-Based High-Density and Low-Cost Flash Memory Devices

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:9365694
- **Type**: journal
- **Published**: March 2022
- **Authors**: Yina Lv, Liang Shi, Longfei Luo +3
- **PDF**: https://ieeexplore.ieee.org/document/9365694
- **Abstract**: Flash memory has been developed with bit density improvement, technology scaling, and 3-D stacking. With this trend, its reliability has been significantly degraded. Error correction code (ECC), such as low-density parity code (LDPC), which has strong error correction capability, has been deployed to solve this problem. However, one of the critical issues of LDPC is that it would introduce a long decoding latency on devices with low reliability. In this case, tail latency would happen, which will significantly impact the quality of service. In this work, a set of smart refresh schemes is proposed to optimize the tail latency. The basic idea of the work is to refresh data when the accessed data have a long decoding latency. Two smart refresh schemes are proposed for this work. The first refresh scheme is designed to refresh data with a long access latency when they are accessed several times. The second refresh scheme is designed to periodically check data with an extremely long access latency and refresh them. To further optimize the refresh overhead caused by the above refresh schemes, a dual-ECC-based refresh scheme is proposed. Besides, a mathematical model for all proposed schemes is constructed to clarify the benefit of each scheme. The experimental results show that the proposed schemes can significantly improve the tail latency with acceptable overhead. What is more, the access performance is well maintained compared with the state-of-the-art work.

## Analysis and Design of Polar-Coded Modulation

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:9678982
- **Type**: journal
- **Published**: March 2022
- **Authors**: Mao-Ching Chiu
- **PDF**: https://ieeexplore.ieee.org/document/9678982
- **Abstract**: Conventional design methods of polar-coded modulation schemes aim to minimize the block error rate (BLER) under successive cancellation (SC) decoding. However, codes designed by conventional methods are not competitive under successive cancellation list (SCL) decoding. This paper presents a new design method based on the BLER upper bound under maximum-likelihood (ML) decoding (ML-BLER upper bound). The ML-BLER upper bound depends on the weight enumerating function (WEF) of the polar-coded modulation scheme over the squared Euclidean distance. In this paper, the polar-coded modulation is randomized by the concept of interleaved polar (i-polar) codes, and the WEF averaged over the ensemble of the polar-coded modulation schemes can be derived. Three polar-coded modulation schemes are considered, i.e., the bit-interleaved polar-coded modulation with a single interleaver (BIPCM-SI), the bit-interleaved polar-coded modulation with multiple interleavers (BIPCM-MI), and the multi-level polar-coded modulation (MLPCM). A new bit channel selection algorithm for polar-coded modulation schemes is proposed, which takes the polarization effect and the ML-BLER upper bound as design criteria. Design examples show that, under SCL decoding, the polar-coded modulation schemes (without CRC) with the proposed channel selection algorithm outperform those with conventional algorithms and are competitive as compared to the state-of-the-art 5G LDPC codes.

## Task-Oriented Multi-User Semantic Communications for VQA

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:9653664
- **Type**: journal
- **Published**: March 2022
- **Authors**: Huiqiang Xie, Zhijin Qin, Geoffrey Ye Li
- **PDF**: https://ieeexplore.ieee.org/document/9653664
- **Abstract**: Semantic communications focus on the transmission of semantic features. In this letter, we consider a task-oriented multi-user semantic communication system for multimodal data transmission. Particularly, partial users transmit images while the others transmit texts to inquiry the information about the images. To exploit the correlation among the multimodal data from multiple users, we propose a deep neural network enabled semantic communication system, named MU-DeepSC, to execute the visual question answering (VQA) task as an example. Specifically, the transceiver for MU-DeepSC is designed and optimized jointly to capture the features from the correlated multimodal data for task-oriented transmission. Simulation results demonstrate that the proposed MU-DeepSC is more robust to channel variations than the traditional communication systems, especially in the low signal-to-noise (SNR) regime.

## Coded Distributed Computing With Partial Recovery

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:9641837
- **Type**: journal
- **Published**: March 2022
- **Authors**: Emre Ozfatura, Sennur Ulukus, Deniz Gündüz
- **PDF**: https://ieeexplore.ieee.org/document/9641837
- **Abstract**: Coded computation techniques provide robustness against straggling workers in distributed computing. However, most of the existing schemes require exact provisioning of the straggling behavior and ignore the computations carried out by straggling workers. Moreover, these schemes are typically designed to recover the desired computation results accurately, while in many machine learning and iterative optimization algorithms, faster approximate solutions are known to result in an improvement in the overall convergence time. In this paper, we first introduce a novel coded matrix-vector multiplication scheme, called coded computation with partial recovery (CCPR), which benefits from the advantages of both coded and uncoded computation schemes, and reduces both the computation time and the decoding complexity by allowing a trade-off between the accuracy and the speed of computation. We then extend this approach to distributed implementation of more general computation tasks by proposing a coded communication scheme with partial recovery, where the results of subtasks computed by the workers are coded before being communicated. Numerical simulations on a large linear regression task confirm the benefits of the proposed scheme in terms of the trade-off between the computation accuracy and latency.

## Mitigating Coherent Noise by Balancing Weight-2 Z-Stabilizers

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:9624967
- **Type**: journal
- **Published**: March 2022
- **Authors**: Jingzhen Hu, Qingzhong Liang, Narayanan Rengaswamy +1
- **PDF**: https://ieeexplore.ieee.org/document/9624967
- **Abstract**: Physical platforms such as trapped ions suffer from coherent noise that does not follow a simple stochastic model. Stochastic errors in quantum systems occur randomly but coherent errors are more damaging since they can accumulate in a particular direction. We consider coherent noise acting transversally, giving rise to an effective error which is a  $Z$ -rotation on each qubit by some angle  $\theta $ . Rather than address coherent noise through active error correction, we investigate passive mitigation through decoherence free subspaces. In the language of stabilizer codes, we require the noise to preserve the code space, and to act trivially (as the logical identity operator) on the protected information. Thus, we develop necessary and sufficient conditions for all transversal  $Z$ -rotations to preserve the code space of a stabilizer code. These conditions require the weight- $2~Z$ -stabilizers to cover all the qubits that are in the support of the  $X$ -component of some stabilizer. Furthermore, the weight- $2~Z$ -stabilizers generate a direct product of single-parity-check codes with even block length. By adjusting the sizes of these components, we are able to construct a large family of QECC codes oblivious to coherent noise, one that includes the  $[[4L^{2}, 1, 2L]]$  Shor codes. The Shor codes are examples of constant excitation codes, where logical qubits are encoded as a code state that is a sum of physical states indexed by binary vectors with the same weight. Constant excitation codes are oblivious to coherent noise since a transversal  $Z$ -rotation acts as a global phase. We prove that a CSS code is oblivious to coherent noise if and only if it is a constant excitation code, and that if the code is error-detecting, then the (constant) weights in different cosets of the  $X$ -stabilizers are identical.

## Array BP-XOR Codes for Hierarchically Distributed Matrix Multiplication

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:9632620
- **Type**: journal
- **Published**: March 2022
- **Authors**: Suayb S. Arslan
- **PDF**: https://ieeexplore.ieee.org/document/9632620
- **Abstract**: A novel fault-tolerant computation technique based on array Belief Propagation (BP)-decodable XOR (BP-XOR) codes is proposed for distributed matrix-matrix multiplication. The proposed scheme is shown to be configurable and suited for modern hierarchical compute architectures such as Graphical Processing Units (GPUs) equipped with multiple nodes, whereby each has many small independent processing units with increased core-to-core communications. The proposed scheme is shown to outperform a few of the well–known earlier strategies in terms of total end-to-end execution time while in presence of slow nodes, called stragglers. This performance advantage is due to the careful design of array codes which distributes the encoding operation over the cluster (slave) nodes at the expense of increased master-slave communication. An interesting trade-off between end-to-end latency and total communication cost is precisely described. In addition, to be able to address an identified problem of scaling stragglers, an asymptotic version of array BP-XOR codes based on projection geometry is proposed at the expense of some computation overhead. A thorough latency analysis is conducted for all schemes to demonstrate that the proposed scheme achieves order-optimal computation in both the sublinear as well as the linear regimes in the size of the computed product from an end-to-end delay perspective.

## Regular Sparse NOMA: Ultimate Performance in Closed Form

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:9718537
- **Type**: journal
- **Published**: March 2022
- **Authors**: Benjamin M. Zaidel, Ori Shental, Shlomo Shamai Shitz
- **PDF**: https://ieeexplore.ieee.org/document/9718537
- **Abstract**: Understanding the fundamental limits of technologies enabling future wireless communication systems is essential for their efficient state-of-the-art design. A prominent technology of major interest in this framework is non-orthogonal multiple access (NOMA). In this paper, we derive an explicit rigorous closed-form analytical expression for the optimum spectral efficiency, in the large-system limit, of regular sparse (code-domain) NOMA, along with a closed-form formulation for the limiting spectral density of the underlying input covariance matrix. Sparse NOMA is an attractive and popular instantiation of NOMA, and its ‘regular’ variant corresponds to the case where only a fixed and finite number of orthogonal multiple-access resources are allocated to any designated user, and vice versa. Interestingly, the well-known Verdú-Shamai formula for (dense) randomly-spread code-division multiple access (RS-CDMA) turns out to coincide with the limit of the derived expression, when the number of orthogonal resources per user grows large. Furthermore, regular sparse NOMA is rigorously shown to be spectrally more efficient than RS-CDMA (viz. dense NOMA) across the entire system load range. Therefore, regular sparse NOMA may serve as an appealing means for reducing the throughput gap to orthogonal transmission in the underloaded regime, and to the ultimate Cover-Wyner bound for massive access overloaded systems. The spectral efficiency is also derived in closed form for the sub-optimal linear minimum-mean-square-error (LMMSE) receiver, which again extends the corresponding Verdú-Shamai LMMSE formula to the case of regular sparse NOMA.

## A Low-Latency Random Access Scheme by Multichannel SIC for Industrial IoT

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:9344839
- **Type**: journal
- **Published**: March 2022
- **Authors**: Chaonong Xu, Biao Jiang, Chao Li
- **PDF**: https://ieeexplore.ieee.org/document/9344839
- **Abstract**: Low latency is a prerequisite for real-time applications, and random access is almost an inevitable choice for large-scale wireless networks. In this article, we consider how to decrease access delay in random access manners for the industrial Internet of Things. We propose a novel scheme by integrating multiple subchannels on the user equipment (UE) side with message-level successive interference cancellation (SIC) on the sink side. Specifically, for any UE that starts an uplink transmission, it just stochastically chooses parts of its subchannels and then simultaneously transmits the same message on them without any power control. On the sink side, the sink decodes signals from UEs using SIC across multiple subchannels. Based on the proposed multichannel SIC scheme, minimizing the access delay in the random access manner is equivalent to minimizing the probability of decoding deadlock. Based on the mathematical method of density evolution and the help from the differential evolution algorithm, an optimal distribution for choosing subchannels is presented. With the optimal distribution, the average access delay is minimized.

## Sparse Layered MIMO With Iterative Detection

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:9627077
- **Type**: journal
- **Published**: March 2022
- **Authors**: Mohamad H. Dinan, Nemanja Stefan Perović, Mark F. Flanagan
- **PDF**: https://ieeexplore.ieee.org/document/9627077
- **Abstract**: In this paper, we propose a novel transmission scheme, called sparse layered MIMO (SL-MIMO), that combines non-orthogonal transmission and singular value decomposition (SVD) precoding. Non-orthogonality in SL-MIMO allows re-using of the eigen-channels which improves the spectral efficiency and error rate performance of the system through enhancing the coding gain and diversity gain. We also present a low-complexity message-passing (MP) detector for the proposed SL-MIMO system which performs quite close to maximum likelihood (ML). The joint moment generating function (MGF) of the ordered eigenvalues is calculated and used to derive a closed-form upper bound on the average word error probability (AWEP) of the SL-MIMO system, and this derived expression is then used to analyze the diversity gain of the system. We use our analytical results to design sub-optimal codebooks to minimize the error rate of the SL-MIMO system. Simulation results in  $4\times 4$  and  $6\times 6$  multiple-input multiple-output (MIMO) systems with 4-ary, 16-ary, and 64-ary constellations show that our proposed SL-MIMO scheme outperforms competing approaches such as X- and Y-codes in terms of system error rate performance. SL-MIMO has 5.6 dB advantage compared to X-codes and 4.7 dB advantage compared to Y-codes in  $6\times 6$  MIMO system with a 64-ary constellation.

## Low Complexity Partial Retransmission ARQ with Hard-Decision Message-Passing Technique

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:9741642
- **Type**: conference
- **Published**: 9-11 March
- **Authors**: Theethawat Keeratihuttayakorn, Julalak Khodom, Usana Tuntoolavest
- **PDF**: https://ieeexplore.ieee.org/document/9741642
- **Abstract**: Partial retransmission ARQ allows a sender to retransmit only part of a frame. This paper proposes a low complexity method using hard-Decision Message-Passing (hMP) technique to correct some errors and verify many correct symbols. A new feedback frame format is also presented. The tradeoff of the lower complexity is the unnecessary retransmission due to false unverified symbols. Results show this tradeoff as the percentage of false unverified symbols, which is from 1.95% to 10.28% for the (60,30) LDPC code with density of 10% and pe from 0.06 to 0.22 in a q-ary symmetric channel. This is very small and worth the reduction in complexity. With systematic codes, the percentage of unnecessary retransmission is decreased from 20.66% to 10.28% at pe= 0.22 for 10% density case. The code with density of 10% provides the best decoding performance and fewest unnecessary retransmissions.

## Flexible Upstream FEC for Higher Throughput, Efficiency, and Robustness for 50G PON

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:9748605
- **Type**: conference
- **Published**: 6-10 March
- **Authors**: Amitkumar Mahadevan, Yannick Lefevre, Ed Harstead +3
- **PDF**: https://ieeexplore.ieee.org/document/9748605
- **Abstract**: A low-complexity flexible forward error correction scheme based on different shortening and puncturing of the standard G.hsp 50G PON LDPC mother code to achieve enhanced throughput and robustness in upstream PON is motivated and presented. © 2022 The Author(s)

## Investigation of Potential FEC Schemes for 800G-ZR Forward Error Correction

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:9748672
- **Type**: conference
- **Published**: 6-10 March
- **Authors**: Weiming Wang, Weifeng Qian, Kai Tao +4
- **PDF**: https://ieeexplore.ieee.org/document/9748672
- **Abstract**: With a record 400Gbps 100-piece-FPGA implementation, we investigate performance of the potential FEC schemes for OIF-800GZR. By comparing the power dissipation and correction threshold at 10−15 BER, we proposed the simplified OFEC for the 800G-ZR FEC.

## Mitigating Nonlinear Interference by Limiting Energy Variations in Sphere Shaping

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:9748613
- **Type**: conference
- **Published**: 6-10 March
- **Authors**: Yunus Can Gültekin, Alex Alvarado, Olga Vassilieva +4
- **PDF**: https://ieeexplore.ieee.org/document/9748613
- **Abstract**: Band-trellis enumerative sphere shaping is proposed to decrease the energy variations in channel input sequences. Against sphere shaping, 0.74 dB SNR gain and up to 9% increase in data rates are demonstrated for single-span systems. © 2021 The Author(s)

## Mitigation of Transmitter Impairment with 4×2 WL MIMO Equalizer Embedding Preliminary CPR

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:9748236
- **Type**: conference
- **Published**: 6-10 March
- **Authors**: Masaki Sato, Manabu Arikawa, Hidemi Noguchi +3
- **PDF**: https://ieeexplore.ieee.org/document/9748236
- **Abstract**: Transmitter impairment mitigation for 58-GBaud PM-64QAM with 4×2 WL MIMO embedding preliminary CPR was demonstrated over 100 km SSMF. Q-penalties of 0.1 dB with 14 ps IQ skew and 10 degree phase error were achieved. © 2021 The Author(s)

## New Use Cases for PONs Beyond Residential Services

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:9748323
- **Type**: conference
- **Published**: 6-10 March
- **Authors**: R. Bonk, Th. Pfeiffer
- **PDF**: https://ieeexplore.ieee.org/document/9748323
- **Abstract**: New use cases for PON are highlighted in critical network infrastructures and industrial factories. Introduction of more flexibility and increased determinism including bounded latency, low jitter, highly secure and available connectivity over PON is addressed.

## Practical Entropy Loading Enabled by Enumerative Sphere Shaping with Short Block Lengths

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:9748820
- **Type**: conference
- **Published**: 6-10 March
- **Authors**: Yizhao Chen, Weihao Li, Junda Chen +4
- **PDF**: https://ieeexplore.ieee.org/document/9748820
- **Abstract**: We propose a practical entropy loading scheme using enumerative sphere shaping, providing considerable shaping gain even with ultra-short block lengths. In the experimental validation, up to 6.0% capacity improvement is achieved. © 2022 The Author(s)

## Implementing Low-Density Parity-Check Codes in the Mars Relay Network

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:9843399
- **Type**: conference
- **Published**: 5-12 March
- **Authors**: Neil Chamberlain, Steve Allen, Kenneth Andrews +5
- **PDF**: https://ieeexplore.ieee.org/document/9843399
- **Abstract**: This paper describes the implementation of Low-Density Parity-Check (LDPC) channel codes in the Mars Relay Network; specifically in the NASA MAVEN orbiter and the ESA ExoMars Trace Gas Orbiter. LDPC codes, also known as Gallager codes, were invented in the early 1960s. At the time, available computational hardware was not powerful enough to implement these codes, so they became “forgotten.” They were later “rediscovered” in the 1990s, whereupon it was demonstrated that practical LDPC decoders performed substantially better than standard convolutional codes. This spurred research and development of LDPC codes at JPL, which culminated in the implementation of a rate 1/2 LDPC decoder and encoder in the Electra proximity radio delivered to MAVEN in 2012 and subsequently to other Mars spacecraft. The paper starts with a brief history of LDPC code development and then goes on to describe the development and validation of recent firmware and software updates to facilitate LDPC code operation with adaptive data rate control. The LDPC codes developed for Electra were verified to produce approximately 3 dB coding gain relative to NASA's standard convolutional code, increasing data return by up to a factor of two. The paper concludes with an assessment of in-flight performance of LDPC-enabled relay passes between MAVEN and the Mars 2020 rover.

## 3D Cloud-RAN Functional Split to Provide 6G Connectivity on Mars

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:9843703
- **Type**: conference
- **Published**: 5-12 March
- **Authors**: Stefano Bonafini, Claudio Sacchi, Fabrizio Granelli +3
- **PDF**: https://ieeexplore.ieee.org/document/9843703
- **Abstract**: The Mars Helicopter Scout left a milestone in the history of the mankind by successfully completing the first flight on Mars. This achievement opens up to the possibility of having many unmanned aerial vehicles (UAVs) acquiring data from the Martian surface along with firmly anchored machines on ground, such as moving rovers or static landers. Moreover, it is no surprise that space agencies are also paving the way for the first human landing on the Red planet. In this context, it becomes needed to support future missions by providing connectivity to the whole Martian surface in order to allow in-situ wide band data exchange between nodes - user equipments (UEs) - composing the overall network. However, it seems tough to move common mobile terrestrial infrastructures on Mars and install them on-ground or implement them on limited-resource machines, as well as to guarantee everywhere and anytime on-demand connectivity. Thus, this paper will investigate the alternative solution of developing an autonomous Martian space ecosystem, through which globally inter-connect the UEs. UAVs and, eventually, high altitude pseudo satellites (HAPS), will act as radio unit (RU) and, partially, as distributed unit (DU) of a cloud radio access network (CRAN), while small satellites platforms, such as CubeSats (CS), placed in orbit will embark the majority of the computational load by performing the remaining DU and centralized unit (CU) functions. The proposed 3D network configuration, which looks towards a “Beyond 5G” infrastructure, or even 6G, will start by supposing very low Mars orbit (VLMO) in which CubeSats will be deployed. The design will then proceed through the installation process of CRAN on drones and CubeSats, while respecting strict latency and bandwidth requirements imposed by the Common Public Radio Interface standard (CPRI) at the fronthaul (FH) to allow low PHY-layer splitting options. A link-budget evaluation will then be proposed for the drone-to-Cubesat link. End-to-End (E2E) performance results will be shown in terms of coded BER between the UEs and the virtualized base station (BS), obtained by correlating the number of executable LDPC decoding iterations at CubeSat side and the signal-to-noise ratio (SNR) achievable over two specific areas of the Gale crater.

## Preparing the Mars Relay Network for the Arrival of the Perseverance Rover at Mars

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:9843762
- **Type**: conference
- **Published**: 5-12 March
- **Authors**: Roy Gladden, Aseel Anabtawi, Dustin Buccino +11
- **PDF**: https://ieeexplore.ieee.org/document/9843762
- **Abstract**: The Perseverance rover represents NASA's latest achievement in Mars exploration. Landing successfully on 18 Feb 2021, the rover's transmitted data during its entry, descent, and landing (EDL) were captured by the Mars Reconnaissance Orbiter (MRO) and the Mars Atmosphere and Volatile Evolution (MAVEN) orbiter. This data, broadcast in near-realtime to the world, allowed everyone to share in the excitement (and “terror”) of the day. The images returned thereafter included the first images of the new landing site, video of the landing itself taken from a variety of vantage points, and eventually the historic images of the first powered flight on another planet. Behind the scenes, the return of that data to Earth was accomplished via Mars orbiters operated by NASA and ESA, using three different ground tracking networks. Considered together, this Mars Relay Network (MRN) enabled the successful, timely, and unobtrusive return of the rover's data. This paper describes the preparations taken by the participants of the MRN in anticipation of the arrival of Perseverance at Mars. These were not only focused on successfully acquiring the rover's critical event telemetry during its EDL, but also on readying the network to return the rover's data on an ongoing basis as it pursued its mission objectives. Included is a brief description of the MRN, which represents a highly successful international collaboration and continues as critical infrastructure for NASA's and ESA's ongoing Mars exploration. Also summarized are the activities performed prior to EDL, including landing site reconnaissance and mission test and training activities; those activities performed on EDL day, especially the recording, return, and processing of the rover's critical event telemetry; and those activities that are now being performed on an ongoing basis during the rover's surface operations, including an outline of the planning processes that enable relay services. Finally, a description of the performance of the network to-date on behalf of the Perseverance rover is given, summarizing the success of the network to provide support to both it and other spacecraft on the surface of Mars.

## SelenIRIS: a Moon-Earth Optical Communication Terminal for CubeSats

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:9749725
- **Type**: conference
- **Published**: 28-31 Marc
- **Authors**: Jorge Rosano Nonay, Christian Fuchs, Davide Orsucci +2
- **PDF**: https://ieeexplore.ieee.org/document/9749725
- **Abstract**: Satellite miniaturization and sinking costs of manu-facturing and launches are bringing Moon missions in the focus of many space companies and agencies. However, achieving the desired data rates on CubeSats over long ranges is proving increasingly challenging with traditional radio-frequency communication systems. Free-space optical (FSO) communications offer a compact, light, and low-power alternative with higher data throughput and fewer limitations (e.g., fewer governmental regulations, channel interference, eavesdropping...). Based on its long heritage of laser communications and new-space tech-nology, the German Aerospace Center (DLR) is investigating SelenIRIS-a miniaturized terminal for Moon-Earth optical data transmissions-for its OSIRIS program. This paper will analyze the necessary adaptations that are required to transfer the technology from the flight-proven low Earth orbit terminals like OSIRIS4CubeSat (O4C) [1] to a concept mission in Lunar orbit.

## Performance Analysis of Pulse Shaping Filters with Novel Rate Adaptive Irregular LDPC Codes

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:9767149
- **Type**: conference
- **Published**: 24-26 Marc
- **Authors**: Mahalakshmi Alias Isakki Ramakrishnan, Tharini Chandraprakasam
- **PDF**: https://ieeexplore.ieee.org/document/9767149
- **Abstract**: In a communication system, pulse shaping filters are used to create a band limited channel and to reduce the Inter Symbol Interference (ISI). Low Density Parity Check Codes (LDPC) code is the improved error correction code used in 5G technology to reduce BER to a great extent. This paper focuses on combining the effect of different pulse shaping filters with the novel rate adaptive irregular LDPC codes. The novel LDPC encoding algorithm having sparse Parity Check Matrix (PCM) is used to achieve capacity nearer to Shannon's Capacity. From the simulation results it is clear that this combination reduces the BER further. It is observed that this idea of combining pulse shaping filters and LDPC can be applied to high data rate communication like 5G in the view of reducing Bit Error Rate (BER).

## Error-Control Coding Algorithms and Architecture for Modern Applications Powered by LDPC Codes and Belief Propagation

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:9763119
- **Type**: conference
- **Published**: 23-25 Marc
- **Authors**: Prashnatita Pal, Bikash Chandra Sahana, Jayanta Poray +1
- **PDF**: https://ieeexplore.ieee.org/document/9763119
- **Abstract**: In modern data communication system Error Detection and Correction has great practical importance to maintain the data integrity across the noisy channel. To deal with this challenge, the theory of Error detection and correction need to get one's precise attention. To retrieve the original data, an efficient process is required. A class of error correcting codes which performs iterative decoding inside a graph is considered which can provide a good approximation. In this context Low Density Parity Check (LDPC) code comes with an excellent error correction performance. In this paper architecture and algorithms for Error Detection and Correction method based on LDPC code is proposed. Also, a simulator for the proposed algorithms is designed and tested successfully.

## DWR: Differential Wearing for Read Performance Optimization on High-Density NAND Flash Memory

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:9774738
- **Type**: conference
- **Published**: 14-23 Marc
- **Authors**: Yunpeng Song, Qiao Li, Yina Lv +2
- **PDF**: https://ieeexplore.ieee.org/document/9774738
- **Abstract**: With the cost reduction and density optimization, the read performance and lifetime of high-density NAND flash memory have been significantly degraded during the last decade. Previous works proposed to optimize lifetime with wear leveling and optimize read performance with reliability improvement. However, with wearing, the reliability and read performance will be degraded along with the life of the device. To solve this problem, a differential wearing scheme (DWR) is proposed to optimize the read performance. The basic idea of DWR is to partition the flash memory into two areas and wear them at different speeds. For the area with low wearing speed, read operations are scheduled for read performance optimization. For the area with high wearing speed, write operations are scheduled but designed to avoid generating bad blocks early. Through careful design and real workloads evaluation on 3D TLC NAND flash, DWR achieves encouraging read performance optimization with negligible impacts to the lifetime.

## Area efficient implementation of short length QC-LDPC codes for Ultra-Reliable Low-Latency Communication (URLLC) application

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:9774211
- **Type**: conference
- **Published**: 10-12 Marc
- **Authors**: Lakshmi J L, Jayakumari J
- **PDF**: https://ieeexplore.ieee.org/document/9774211
- **Abstract**: This paper presents an area efficient implementation of short block length and low rate Quasi cyclic (QC)-Low Density parity check code (LDPC) encoder for binary input additive white Gaussian noise channel (BIAWGN) targeting the Ultra-reliable low-latency communication (URLLC) application. The stringent prerequisites like ultra-high reliability and lesser latency have made URLLC applications most critical feature of the 5G wireless communication. In the proposed architecture the dual diagonal encoding is used to generate the codeword. The primary building block in the dual diagonal encoding is the barrel shifter, which performs the cyclic shift operations. Thus, it occupies larger part of area next to the memory blocks. This works aims at drastically reducing the number of barrel shifters using hardware sharing technique. The implementation of the encoder for short length code is done in Xilinx Virtex-7 FPGA platform. The simulation results show that the proposed architecture can reduce the number of multiplexers in the encoder architecture by 37%, thus considerably reducing the area compared to the existing architectures.

## DaRe: Data Recovery Through Application Layer Coding for LoRaWAN

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:9167471
- **Type**: journal
- **Published**: 1 March 20
- **Authors**: Paul J. Marcelis, Nikolaos Kouvelas, Vijay S. Rao +1
- **PDF**: https://ieeexplore.ieee.org/document/9167471
- **Abstract**: Long-range wide-area network (LoRaWAN) is an energy-efficient and inexpensive networking technology that is rapidly being adopted for many Internet-of-Things applications. In this study, we perform extensive measurements on a new LoRaWAN deployment to characterise the spatio-temporal properties of the LoRaWAN channel. Our experiments reveal that LoRaWAN frames are mostly lost due to the channel effects, which are adverse when the end-devices are mobile. The frame losses are up to 70 percent, which can be bursty for both mobile and stationary scenarios. Frame losses result in data losses since the frames are transmitted only once in the basic configuration. To reduce data losses in LoRaWAN, we design a novel coding scheme for data recovery called DaRe that works on the application layer. DaRe combines techniques from convolutional and fountain codes. By implementing DaRe, we show that 99 percent of the data can be recovered with a code rate of 1/2 when the frame loss is up to 40 percent. Compared to the repetition coding scheme, DaRe provides 21 percent higher data recovery and can save up to 42 percent of the energy consumed on a transmission for 10-byte data units. We also show that DaRe provides better resilience to bursty frame losses.
