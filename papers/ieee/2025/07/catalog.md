# IEEE Xplore — 2025-07


## RXO-LDPC: A Physics-Inspired Relaxation Oscillator-Based Solver Leveraging Six-Body Spin Interactions for Soft Decoding of LDPC Codes

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:11052258
- **Type**: journal
- **Published**: July 2025
- **Authors**: Evangelos Dikopoulos, Luke Wormald, Ying-Tuan Hsu +4
- **PDF**: https://ieeexplore.ieee.org/document/11052258
- **Abstract**: Physics-inspired computing harnesses continuous-time (CT) operation, massive parallelism, and direct compute load mapping to coupled CMOS-based spins to accelerate solving complex optimization problems. This work advances the field by introducing relaxation oscillator (RXO)-low-density parity check (LDPC), a combinatorial optimization problem (COP) engine that natively supports six-body spin interactions for efficient, robust, and one-shot oscillator-based soft decoding of LDPC codes. The proposed RXO spins feature a capacitor-DAC-based initialization structure, allowing precise mapping of soft information to initial spin phases for high-performance decoding. A crossbar-based feedback system facilitates six-body spin interactions by directly coupling spins based on the COP graph. Implemented in 28-nm CMOS technology, the prototype achieves a frame error rate (FER) and bit error rate (BER) of  $1.36{\times }10{^{-6}}$  and  $1.89{\times }10{^{-7}}$ , respectively, at 7-dB SNR. The measured BER is more than three orders of magnitude lower than for belief propagation (BP) decoding, for channels with 2–5-dB SNR. The measured energy efficiency of 7.28 pJ/bit exceeds the normalized efficiencies of state-of-the-art decoders. Evaluated with more than 100 million decoding cycles, the system demonstrates reliable performance across a wide range of SNRs, supply voltages, temperatures, and for different dies. These measurement results highlight the RXO-based architecture’s potential as an accelerator for directly solving COPs with multi-body spin interactions.

## Margin Propagation Based XOR-SAT Solvers for Decoding of LDPC Codes

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10806722
- **Type**: journal
- **Published**: July 2025
- **Authors**: Ankita Nandi, Shantanu Chakrabartty, Chetan Singh Thakur
- **PDF**: https://ieeexplore.ieee.org/document/10806722
- **Abstract**: Decoding of Low-Density Parity Check (LDPC) codes can be viewed as a special case of XOR-SAT problems, for which low-computational complexity bit-flipping algorithms have been proposed in the literature. However, a performance gap exists between the bit-flipping LDPC decoding algorithms and the benchmark LDPC decoding algorithms, such as the Sum-Product Algorithm (SPA). In this paper, we propose an XOR-SAT solver using log-sum-exponential functions and demonstrate its advantages for LDPC decoding. This is then approximated using the Margin Propagation formulation to attain a low-complexity LDPC decoder. The proposed algorithm uses soft information to decide the bit-flips that maximize the number of parity check constraints satisfied over an optimization function. The proposed solver can achieve results that are within 0.1dB of the Sum-Product Algorithm for the same number of code iterations. It is also at least  $10 \times $  lower than other Gradient-Descent Bit Flipping decoding algorithms, which are also bit-flipping algorithms based on optimization functions. The approximation using the Margin Propagation formulation does not require any multipliers, resulting in significantly lower computational complexity than other soft-decision Bit-Flipping LDPC decoders.

## Low-Latency Channel Estimation for OFDM System in Fast-Fading Multipath Environments

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10975859
- **Type**: journal
- **Published**: July 2025
- **Authors**: Huang-Chang Lee, Yi-Ru Chen, Lu-Chi Lin +2
- **PDF**: https://ieeexplore.ieee.org/document/10975859
- **Abstract**: Although suffering from inter-carrier interference (ICI), the proposed method can accomplish the channel estimation for the orthogonal frequency division multiplexing (OFDM) systems in high-mobility wireless communication environments using the conventional equally-separated stand-alone pilot arrangements. Initially, rough channel estimation based on the pilots is used for decoding the multiple low-density parity-check (LDPC) codes in each OFDM symbol in the first iteration. Correct decoding results provide reliable decision feedback, and can be used to form pseudo pilots and be combined with the original pilots to enhance the channel estimation in the following iterations. Simulation results confirm that the proposed method can extend the applicability of the OFDM systems equipped with the conventional pilot arrangement in fast-fading channels.

## Effective IDS Error Correction Algorithms for DNA Storage Channels With Multiple Output Sequences

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10955696
- **Type**: journal
- **Published**: July 2025
- **Authors**: Caiyun Deng, Guojun Han, Pengchao Han +1
- **PDF**: https://ieeexplore.ieee.org/document/10955696
- **Abstract**: DNA data storage is a cutting-edge storage technique due to its high density, replicability, and long-term capability. It involves encoding, insertion, deletion, and substitution (IDS) channels for data synthesis and sequencing, and decoding processes. The IDS channels that feature multiple output sequences are prone to IDS errors, complicating the decoding process and degrading the performance of DNA data storage. To address this issue, we investigate effective IDS error correction algorithms considering two encoding schemes in DNA data storage. Specifically in the encoding process, we use marker codes (MC) and embedded marker codes (EMC) as inner codes, respectively, both connected to low-density parity-check (LDPC) codes as outer codes. First, we propose the segmented progressive matching (SPM) algorithm to infer the consensus sequence from multiple output sequences, thereby facilitating the decoding processes. Moreover, when using MC as the inner code, we propose a synchronous decoding algorithm based on the Hidden Markov Model (SDH) to infer the a posteriori probability (APP) of base symbols, which supports the external decoding algorithm. Furthermore, when the inner code is EMC, we propose the iterative external decoding (IED) algorithm. IED integrates synchronous decoding with embedded normalized min-sum decoding (ENMS) to achieve an enhanced APP for external decoding, enabling lower bit-error rate (BER) transmission. Meanwhile, we reduce the complexity of the external decoder by minimizing checksum node computations. Comparing the two schemes reveals that the SDH algorithm with MC as the inner code offers a lightweight solution for DNA data storage. In contrast, the IED with EMC demonstrates superior decoding performance with a linear complexity scale by the number of iterations. Compared with existing studies, simulation results show that our proposed decoding algorithm reduces the BER by  ${21}.{72}\% \sim {99}.{75}\%$ .

## Representative OSD with Local Constraints of CA-Polar Codes

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:11151187
- **Type**: journal
- **Published**: July 2025
- **Authors**: Yiwen Wang, Qianfan Wang, Jifan Liang +1
- **PDF**: https://ieeexplore.ieee.org/document/11151187
- **Abstract**: In this paper, we propose an algorithm to transform a generator matrix of a linear block code into a minimum weight staircase generator matrix (MWSGM). This allows us to apply the representative ordered statistics decoding with local constraints (LC-ROSD) algorithm to cyclic redundancy check (CRC) aided polar (CA-polar) codes. Distinguished from the conventional ordered statistics decoding (OSD), the LC-ROSD implements parallel Gaussian elimination (GE) for MWSGM instead of serial GE for a general matrix, potentially reducing the decoding latency. Numerical results show that the performance of 5G CA-polar codes under LC-ROSD is better than that of CRC aided successive cancellation list (CA-SCL) decoding and can approach the corresponding maximum likelihood (ML) lower bounds at different code rates. The numerical results also show that the LC-ROSD with MWSGM has lower decoding complexity than the CA-SCL decoding in the high signal-to-noise ratio (SNR) region.

## Multiple-Masks Error Correction Code Transformer for Short Block Codes

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10960678
- **Type**: journal
- **Published**: July 2025
- **Authors**: Seong-Joon Park, Hee-Youl Kwak, Sang-Hyo Kim +3
- **PDF**: https://ieeexplore.ieee.org/document/10960678
- **Abstract**: With the broadening applications of deep learning, neural decoders have emerged as a key research focus, specifically aimed at improving the decoding performance of conventional decoding algorithms. In particular, error correction code transformer (ECCT), which utilizes the transformer architecture, has achieved state-of-the-art performance among neural network-based decoders. We present three technical contributions to significantly enhance the performance of ECCT. First, we propose a novel transformer architecture of ECCT, termed the multiple-masks ECCT (MM ECCT). We employ multiple masked self-attention blocks with different mask matrices in a parallel manner to learn diverse relationships among the codeword bits. Second, we discover that constructing mask matrices based on systematic parity check matrices (PCMs) can make the attention maps sparse, which not only enhances the decoding performance but also reduces computational complexity. Finally, we propose using complementary mask matrices derived from cyclic permutations of the systematic PCM. These complementary mask matrices are specifically designed to enhance the decoding of cyclic codes. Our extensive simulation results show that the proposed MM ECCT architecture with carefully designed mask matrices outperforms the original ECCT by a large margin, achieving state-of-the-art decoding performance among neural decoders. The source code is available at https://github.com/iil-postech/mm-ecct.

## A Mathematical Theory for Learning Semantic Languages by Abstract Learners

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10960361
- **Type**: journal
- **Published**: July 2025
- **Authors**: Kuo-Yu Liao, Cheng-Shang Chang, Y.-W. Peter Hong
- **PDF**: https://ieeexplore.ieee.org/document/10960361
- **Abstract**: Recent advances in Large Language Models (LLMs) have demonstrated the emergence of capabilities (learned skills) when the number of system parameters and the size of training data surpass certain thresholds. The exact mechanisms behind such phenomena are not fully understood and remain a topic of active research. Inspired by the skill-text bipartite graph model proposed by Arora and Goyal for modeling semantic languages, we develop a mathematical theory to explain the emergence of learned skills, taking the learning (or training) process into account. Our approach models the learning process for skills in the skill-text bipartite graph as an iterative decoding process in Low-Density Parity Check (LDPC) codes and Irregular Repetition Slotted ALOHA (IRSA). Using density evolution analysis, we demonstrate the emergence of learned skills when the ratio of the number of training texts to the number of skills exceeds a certain threshold. Our analysis also yields a scaling law for testing errors relative to this ratio. Upon completion of the training, the association of learned skills can also be acquired to form a skill association graph. We use site percolation analysis to derive the conditions for the existence of a giant component in the skill association graph. Our analysis can also be extended to the setting with a hierarchy of skills, where a fine-tuned model is built upon a foundation model. It is also applicable to the setting with multiple classes of skills and texts. As an important application, we propose a method for semantic compression and discuss its connections to semantic communication.

## SHINE: Symbol-Based Heuristic Iterative NB-LDPC Coded MIMO BP Detection and Decoding

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:11007208
- **Type**: journal
- **Published**: July 2025
- **Authors**: Wenyu Huang, Wenyue Zhou, Yutai Sun +5
- **PDF**: https://ieeexplore.ieee.org/document/11007208
- **Abstract**: In this letter, we propose SHINE, a Symbol-based Heuristic Iterative NB-LDPC codEd MIMO BP detection and decoding scheme. More specifically, we develop an NB-LDPC coded iterative detection and decoding (IDD) receiver equiped with a fine-tailored LLR interface between the real-domain detection and the Galois-field decoding. To further reduce the complexity of the IDD receiver, we propose a Joint Symbol Pruning Optimization (JSPO) framework, leveraging metaheuristic learning to jointly optimize the symbol search space in both detection and decoding. Numerical results demonstrate that compared with its basic version, SHINE succeeds in achieving up to 37.32% and 58.31% complexity reduction for the detection and the decoding w/o performance degradation. Numerical results also demonstrate the performance merits of the proposed SHINE compared with other NB-LDPC coded IDD counterparts.

## A High Performance and Low Complexity LDPC Decoding Strategy for Space-Air–Ground-Sea Integrated Communication Networks

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10787111
- **Type**: journal
- **Published**: July 2025
- **Authors**: Xinyuan Ren, Jiahao Zhang, Chao Chen +4
- **PDF**: https://ieeexplore.ieee.org/document/10787111
- **Abstract**: In the coming sixth-generation era, space-air–ground-sea integrated (SAGSI) communication networks will be rapidly developed, with broader coverage, connectivity, security, and so on. The various communication requirements call for a decoding algorithm with lower complexity and higher coding gain for the channel code. Inspired by this point and based on the fifth-generation networks standard, this paper proposes a high-performance and low-complexity Low-Density Parity-Check (LDPC) decoding strategy for SAGSI communication networks. Based on a two-dimensional self-corrected min-sum algorithm (2D-SCMSA), the message reliability can be improved by the proposed Enhanced 2D-SCMSA (E-2D-SCMSA) while considering the erasure range of the variable node message. For given LDPC codes, the simulation results show that the proposed E-2D-SCMSA can achieve a performance gain of approximately 0.1 dB at bit error rate (BER) of $10^{-4}$ compared to 2D-SCMSA with a negligible increase in computational complexity. Moreover, the performance gap between the proposed E-2D-SCMSA and likelihood ratio belief-propagation algorithm is less than 0.1 dB at BER of $10^{-4}$ .

## Collaborative Secret and Covert Communications for Multi-User Multi-Antenna Uplink UAV Systems: Design and Optimization

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10938035
- **Type**: journal
- **Published**: July 2025
- **Authors**: Jinpeng Xu, Lin Bai, Xin Xie +1
- **PDF**: https://ieeexplore.ieee.org/document/10938035
- **Abstract**: Motivated by diverse secure requirements of multi-user in uncrewed aerial vehicle (UAV) systems, we propose a collaborative secret and covert transmission method for multi-antenna ground users to UAV communications. Specifically, based on the power domain non-orthogonal multiple access (NOMA), two ground users with distinct security requirements, named Bob and Carlo, superimpose their signals and transmit the combined signal to the UAV named Alice. An adversary Willie attempts to simultaneously eavesdrop Bob’s confidential message and detect whether Carlo is transmitting or not. We derive close-form expressions of the secrecy connection probability (SCP) and the covert connection probability (CCP) to evaluate the link reliability for wiretap and covert transmissions, respectively. Furthermore, we bound the secrecy outage probability (SOP) from Bob to Alice and the detection error probability (DEP) of Willie to evaluate the link security for wiretap and covert transmissions, respectively. To characterize the theoretical benchmark of the above model, we formulate a weighted multi-objective optimization problem to maximize the average of secret and covert transmission rates subject to constraints SOP, DEP, the beamformers of Bob and Carlo, and UAV trajectory parameters. To solve the optimization problem, we propose an iterative optimization algorithm using successive convex approximation and block coordinate descent (SCA-BCD) methods. Our results reveal the influence of design parameters of the system on the wiretap and covert rates, analytically and numerically. In summary, our study fills the gaps in collaborative secret and covert transmission for multi-user multi-antenna uplink UAV communications and provides insights to construct such systems.

## A Sub-0.8-pJ/bit Universal Soft-Detection Decoder Using ORBGRAND

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10768996
- **Type**: journal
- **Published**: July 2025
- **Authors**: Arslan Riaz, Alperen Yasar, Furkan Ercan +6
- **PDF**: https://ieeexplore.ieee.org/document/10768996
- **Abstract**: Guessing random additive noise decoding (GRAND) has enabled the practical implementation of maximum likelihood (ML) or near-ML decoding, shifting the paradigm of code-specific decoder design to a code-agnostic decoding architecture. Ordered reliability bits GRAND (ORBGRAND) is a soft-detection variant of GRAND that uses soft information to guide its query order to significantly improve the decoding performance. This work presents the first-integrated energy-efficient hardware implementation of ORBGRAND to achieve ultra-low energy (sub-pJ/bit) and power consumption (5 mW) while using a small core area of 0.4 mm2 in 40-nm CMOS. The proposed architecture enables dynamic power savings by implementing an efficient sorter that allows the decoder to use the sorted bits immediately without waiting for the entire list to be sorted and an efficient landslide unit that generates noise effect sequences in parallel. The chip is implemented in 40-nm CMOS with a re-configurable architecture that enables decoding of any binary linear code from 32 to 256 bits of code length and 0.8–1 code rate. For a code length of 256 bits and a code rate of 0.94, it provides a measured energy consumption of 0.76 pJ/bit and power consumption of 4.9 mW from a 1.0-V supply voltage at an operating frequency of 90 MHz providing a throughput of 6.5 Gb/s and a latency of 40 ns at a targeted frame error rate (FER) of 10-7.

## Family of Mutually Uncorrelated Codes for DNA Storage Address Design

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10843767
- **Type**: journal
- **Published**: July 2025
- **Authors**: Zhenlu Liu, Ben Cao, Qi Shao +4
- **PDF**: https://ieeexplore.ieee.org/document/10843767
- **Abstract**: Deoxyribonucleic acid (DNA) has become an ideal medium for long-term storage and retrieval due to its extremely high storage density and long-term stability. But access efficiency is an existing bottleneck in DNA storage, especially the lack of high-quality random access address sequences. Therefore, in this paper, we report a series of approaches based on k-weakly mutually uncorrelated (k-WMU) codes to design the address sequence to improve the access efficiency of DNA storage. To address the problem of DNA sequences that are poorly scalable at the base level, we propose a 0-m-ruling coding scheme combined with k-WMU codes that can make address sequences avoid generating secondary structure with stem lengths ranging from 3 to 9. Based on the decoupled structure, We further extend the k-WMU codes with error correction function while satisfying combinatorial biological constraints. In order to investigate the performance of the designed address sequences for real-world applications, we perform simulation experiments based on thermodynamic properties and error correction capability as well as compared the minimum free energy (MFE), melting temperature (TM), and average decoding success rate (ADSR) with previous work. The results show that designed address sequences have a high MFE value and ADSR and a substantial reduction in TM-variance while satisfying the combinatorial biological constraints. As the quality of address sequences improves, this will help to achieve accurate random access as well as enhance the robustness of the DNA storage system.

## Multi-Scale Semantic Communication for Object Detection: Single and Cross-Domain Scenarios

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10944429
- **Type**: journal
- **Published**: July 2025
- **Authors**: Jie Guo, Hang Yin, Bin Song +4
- **PDF**: https://ieeexplore.ieee.org/document/10944429
- **Abstract**: With the rapid popularity of vision-driven communication applications, object detection has become one of the fundamental techniques for performing practical vision tasks. In traditional communication systems, images are compressed for transmission, reconstructed at the receiver, and then processed by existing object detection algorithms. However, transmitting large amounts of images consumes significant storage and communication resources. To address this challenge, a semantic communication-based image reconstruction scheme has been proposed for object detection, which transmits only the semantic information relevant to image reconstruction. However, this method is prone to losing key information, such as object position and texture details, leading to degraded object detection performance. Additionally, it is sensitive to environmental factors such as weather and lighting, resulting in poor adaptability across multiple scenarios. To address these issues, we propose a multi-scale semantic communication framework for object detection that transmits only multi-scale semantic features relevant to the task and employs decoupling at the receiver to separate positional and classification information of target objects without requiring image reconstruction. To improve adaptability across multiple scenarios, we introduce a cross-domain object detection technique that ensures reliable object detection in new scenarios by optimizing the framework’s multi-scale semantic encoder through domain adversarial learning. Numerical results demonstrate that the proposed framework achieves mean average precision improvements of  $15.4\% \sim 38.5\%$  over the traditional communication framework within low to medium signal-to-noise ratio regions in additive white Gaussian noise and Rayleigh fading channels.

## Hybrid Digital-Analog Semantic Communications

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10960639
- **Type**: journal
- **Published**: July 2025
- **Authors**: Huiqiang Xie, Zhijin Qin, Zhu Han +1
- **PDF**: https://ieeexplore.ieee.org/document/10960639
- **Abstract**: Digital and analog semantic communications (SemCom) face inherent limitations such as data security concerns in analog SemCom, as well as leveling-off and cliff-edge effects in digital SemCom. In order to overcome these challenges, we propose a novel SemCom framework and a corresponding system called HDA-DeepSC, which leverages a hybrid digital-analog approach for multimedia transmission. This is achieved through the introduction of analog-digital allocation and fusion modules. To strike a balance between data rate and distortion, we design new loss functions that take into account long-distance dependencies in the semantic distortion constraint, essential information recovery in the channel distortion constraint, and optimal bit stream generation in the rate constraint. Additionally, we propose denoising diffusion-based signal detection techniques, which involve carefully designed variance schedules and sampling algorithms to refine transmitted signals. Through extensive numerical experiments, we will demonstrate that HDA-DeepSC exhibits robustness to channel variations and is capable of supporting various communication scenarios. Our proposed framework outperforms existing benchmarks in terms of peak signal-to-noise ratio and multi-scale structural similarity, showcasing its superiority in semantic communication quality.

## A Deep Joint Source-Channel Coding Scheme for Hybrid Mobile Multi-Hop Networks

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10960356
- **Type**: journal
- **Published**: July 2025
- **Authors**: Chenghong Bian, Yulin Shao, Deniz Gündüz
- **PDF**: https://ieeexplore.ieee.org/document/10960356
- **Abstract**: Efficient data transmission across mobile multi-hop networks that connect edge devices to core servers presents significant challenges, particularly due to the variability in link qualities between wireless and wired segments. This variability necessitates a robust transmission scheme that transcends the limitations of existing deep joint source-channel coding (DeepJSCC) strategies, which often struggle at the intersection of analog and digital methods. Addressing this need, this paper introduces a novel hybrid DeepJSCC framework, h-DJSCC, tailored for effective image transmission from edge devices through a network architecture that includes initial wireless transmission followed by multiple wired hops. Our approach harnesses the strengths of DeepJSCC for the initial, variable-quality wireless link to avoid the cliff effect inherent in purely digital schemes. For the subsequent wired hops, which feature more stable and high-capacity connections, we implement digital compression and forwarding techniques to prevent noise accumulation. This dual-mode strategy is adaptable even in scenarios with limited knowledge of the image distribution, enhancing the framework’s robustness and utility. Extensive numerical simulations demonstrate that our hybrid solution outperforms traditional fully digital approaches by effectively managing transitions between different network segments and optimizing for variable signal-to-noise ratios (SNRs). We also introduce a fully adaptive h-DJSCC architecture with both SNR-adaptive (SA) and rate-adaptive (RA) modules capable of adjusting to different network conditions and achieving diverse rate-distortion objectives, thereby reducing the memory requirements on network nodes.

## Orthogonal Chirp-Frequency Division Multiplexing

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10778593
- **Type**: journal
- **Published**: July 2025
- **Authors**: Túlio Fernandes Moreira, Mateus de Lima Filomeno, Wallace Alves Martins +1
- **PDF**: https://ieeexplore.ieee.org/document/10778593
- **Abstract**: This paper introduces a multicarrier communication technique termed orthogonal chirp-frequency division multiplexing (OCFDM). It relies on a unitary transform named discrete modular chirp transform. The proposed OCFDM amalgamates characteristics from the orthogonal frequency division multiplexing (OFDM) and orthogonal chirp division multiplexing (OCDM), partitioning the frequency spectrum into distinct subbands and populating each of them with orthogonal chirps. By deriving the reconstructed signal at the receiver, the paper shows that the normalized signal-to-noise ratio exhibits changes across subbands, allowing the use of resource allocation, for instance, for power allocation or bit-loading. Moreover, it is shown that the OCFDM introduces an additional degree of freedom through its tile geometries, allowing it to be configured to perform in between OFDM and OCDM and, consequently, to offer novel and balanced trade-offs among symbol error rate, data rate, and robustness to interference. Numerical analyses illustrate those trade-offs and confirm the versatility and efficacy of the OCFDM.

## Optimized Algorithms for FPGA Implementation of PDCCH Chain for 5G-NR Base Station

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10835153
- **Type**: journal
- **Published**: July 2025
- **Authors**: Harsha Rudramuniyappa, Samudrala Soujanya, Prem Singh +1
- **PDF**: https://ieeexplore.ieee.org/document/10835153
- **Abstract**: The physical layer in a cellular network base station typically runs on a field programmable gate array (FPGA) to enable reconfigurability and adaptability to meet future demands of the network with sufficient computational power. This work proposes a novel architecture and algorithms for the FPGA implementation of the fifth-generation (5G) new radio (NR) physical downlink control channel (PDCCH) using the 3GPP procedures for downlink control information (DCI) processing, including sub-block interleaver, bit selection, scrambling, golden sequence generation, and modulation. The proposed algorithms are optimized to meet 5G-NR frame timings for DCI processing with minimum power consumption and hardware resource utilization. We perform rigorous testing including all corner cases to benchmark our designs in i) standalone mode, and ii) integrated fashion for the end-to-end PDCCH processing. The PDCCH implementation, with maximum DCI payload, using the proposed architecture and algorithms achieves  $1.5 ~\mu s$  latency, 1.98% hardware resource utilization, 1.2 Gbps throughput and 10 Gbps/W power efficiency. With a subcarrier spacing  $\Delta f=30$  KHz, it can multiplex DCI to schedule up to 20 and 40 users for one orthogonal frequency division multiplexing (OFDM) and two OFDM symbols long PDCCH respectively.

## An Efficient and Unified RTL Accelerator Design for HQC-128, HQC-192, and HQC-256

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10949843
- **Type**: journal
- **Published**: July 2025
- **Authors**: Francesco Antognazza, Alessandro Barenghi, Gerardo Pelosi
- **PDF**: https://ieeexplore.ieee.org/document/10949843
- **Abstract**: In the Post-Quantum Standardization (PQC) process held by the National Institute of Standards and Technology (NIST), the final round of evaluation of the asymmetric cryptographic schemes Classic McEliece, BIKE and HQC will elect the alternative Key Establishment Mechanism (KEM) to the FIPS $203$203 standard CRYSTALS-Kyber. In this work we present two configurations of a RTL hardware design of the HQC candidate, either optimized for devices exclusively working with client-server style protocols, or a unified accelerator compatible with all KEM operations, i.e. Key Generation, Encapsulation, and Decapsulation. Our designs are compatible with all the parameter sets defined by the HQC specification, providing security margins equivalent to the ones of AES-128, AES-192, and AES-256 based on a selection made at runtime. We are providing an extensive comparison with the current state-of-the-art RTL hardware designs for Artix-$7$7 FPGAs of the schemes in the PQC process, introducing a new metric to evaluate the area utilization, historically a challenging task for such devices made of heterogeneous resources, and determining that HQC has by far the best figures among the code-based candidates in terms of latency, area occupied and efficiency, and even comparable with the lattice-based CRYSTALS-Kyber when using the parameters with lowest security margin.

## A Novel BTBT Erase-Based PUF Generation Method With High Throughput in a 3-D NAND Flash Memory

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:11004633
- **Type**: journal
- **Published**: July 2025
- **Authors**: You-Liang Chou, C. C. Cheng, G. W. Wu +7
- **PDF**: https://ieeexplore.ieee.org/document/11004633
- **Abstract**: A novel physical unclonable function (PUF) generation method based on 3-D nand flash architecture is proposed. We exploit band-to-band tunneling (BTBT) erase operation and the inherent process variations among the bitline (BL)/common-source-line (CSL) junctions in individual nand cell strings to realize a stable PUF. Its outstanding performance sets a new benchmark for flash-based PUFs, featuring high-generation throughput (>100 Mb/s) to enhance flexibility in chip authentication and mitigate supply chain attacks. It also demonstrates nearly ideal randomness, strong uniqueness (inter-Hamming distance (inter-HD) ~0.5), and an artificially achieved Hamming weight (HW) =0.5). Besides, the proposed PUF also exhibits great sustainability of cross-temperature operations, repeated readouts (>10 M times), retention (>500 h/ $85~^{\circ }$ C bake with bit error rate (BER) almost being “zero”), and reproducibility (>1 k P/E cycles).

## Half-Marker Codes for Deletion Channels With Applications in DNA Storage

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:11004160
- **Type**: journal
- **Published**: July 2025
- **Authors**: Javad Haghighat, Tolga M. Duman
- **PDF**: https://ieeexplore.ieee.org/document/11004160
- **Abstract**: DNA data storage systems face significant challenges, including insertion, deletion, and substitution (IDS) errors. Therefore, designing effective synchronization codes, i.e., codes capable of correcting IDS errors, is essential for DNA storage systems. Marker codes are a favorable choice for this purpose. In this letter, we extend the notion of marker codes by making the following key observation. Since each DNA base is equivalent to a 2-bit storage unit, one bit can be reserved for synchronization, while the other is dedicated to data transmission. Using this observation, we propose a new class of marker codes, which we refer to as half-marker codes. We demonstrate that this extension has the potential to significantly increase the mutual information between the input sequence and the soft outputs of an IDS channel modeling a DNA storage system. Specifically, through examples, we show that when concatenated with an outer error-correcting code, half-marker codes outperform standard marker codes and significantly reduce the end-to-end bit error rate of the system.

## Achieving Uniform Side Information Gain With Multilevel Lattice Codes Over the Ring of Integers

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:11014228
- **Type**: journal
- **Published**: July 2025
- **Authors**: Juliana G. F. Souza, Sueli I. R. Costa
- **PDF**: https://ieeexplore.ieee.org/document/11014228
- **Abstract**: The index coding problem aims to optimise broadcast communication by exploring side information available at the receivers. In this work, we investigate the use of Construction  $\pi _{A}$  lattices over the ring of integers  $\mathbb {Z}$  for index coding and establish algebraic conditions on the code generators to guarantee uniform side information gain. The effectiveness of the proposed approach is demonstrated through theoretical analysis and explicit code design examples.

## Guest Editorial: Rethinking the Information Identification, Representation, and Transmission Pipeline: New Approaches to Data Compression and Communication

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:11039751
- **Type**: journal
- **Published**: July 2025
- **Authors**: Jun Chen, Alexandros G. Dimakis, Yong Fang +3
- **PDF**: https://ieeexplore.ieee.org/document/11039751
- **Abstract**: N/A

## A Study of the Performance of LDPC Codes under Various Decoding Algorithms and Schedules

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:11170007
- **Type**: conference
- **Published**: 8-11 July 
- **Authors**: Sangwon Chae, Hyojeong Choi, Gangsan Kim +2
- **PDF**: https://ieeexplore.ieee.org/document/11170007
- **Abstract**: Low-Density Parity-Check (LDPC) codes have been widely used in modern communication standards due to their strong error correction capabilities. This paper presents an experimental evaluation of a (1200, 600) irregular LDPC code over an additive white Gaussian noise (AWGN) channel, systematically comparing three decoding algorithms (Sum-Product, Normalized Min-Sum, and Offset Min-Sum) with three scheduling methods (Flooding, Layered Belief Propagation, and Residual Belief Propagation). Parameter sweeps are performed to determine the optimal normalization factor ($\alpha$) for the Normalized Min-Sum and the offset factor ($\beta$) for the Offset Min-Sum. A comparative analysis is then performed on the frame error rate (FER) and convergence behavior of each algorithm and scheduling configuration, considering the maximum number of iterations set at 10 and 25. The results show that the Offset Min-Sum algorithm with $\beta=0.5$ and Layered Belief Propagation scheduling provides an acceptable trade-off between complexity and error-correction performance, closely matching the Sum-Product algorithm but at a lower computational cost. Although Residual Belief Propagation converges quickly at lower signal-to-noise ratios, it exhibits a high error floor. These findings provide practical guidelines for selecting optimal decoding configurations in resource-constrained applications.

## Iterative Detection, Decoding and Channel Estimation for Multiple-RIS Assisted MIMO Systems

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:11143508
- **Type**: conference
- **Published**: 7-10 July 
- **Authors**: Roberto C. G. Porto, Rodrigo C. de Lamare
- **PDF**: https://ieeexplore.ieee.org/document/11143508
- **Abstract**: This work proposes an iterative detection, decoding and channel estimation scheme for multiple-antenna systems assisted by multiple reflective intelligent surfaces (RIS). A novel channel estimation technique that exploits low-density parity-check (LDPC) codes and iterative processing is developed to enhance estimation accuracy while reducing the number of required pilot symbols. The key idea is to exploit encoded pilots to improve the iterative process, enabling the use of not only pilot bits but also parity bits from the coded packet to refine channel estimation. Simulations analyze a sub-6 GHz scenario where the channel propagation is not sparse and multiple RIS are deployed, considering both LOS and NLOS conditions. Numerical results show significant performance gains for the proposed scheme and estimator over competing approaches.

## IFDMA for Massive Connectivity Over High Mobility Channels

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:11143338
- **Type**: conference
- **Published**: 7-10 July 
- **Authors**: Yuhao Chi, Jiaqi Liang, Lei Liu +2
- **PDF**: https://ieeexplore.ieee.org/document/11143338
- **Abstract**: With the rapid growth of high-mobility communication applications and the widespread use of wireless devices, ensuring reliable information transmission for massive devices over high-mobility, time-varying channels has emerged as a critical challenge. Recent studies have integrated orthogonal time frequency space (OTFS) or affine frequency division multiplexing (AFDM) with sparse code multiple access (SCMA). However, the lack of low-complexity, high-reliability detection algorithms for OTFS and AFDM, along with SCMA codebooks not accounting for delay-Doppler channel effects and requiring redesign when system parameters (e.g., number of users or antennas) change, leads to significant performance degradation and high implementation complexity in practical systems. To address these issues, this paper proposes an interleave frequency division multiple access (IFDMA) scheme that ensures reliable communication for massive users through low-complexity transceivers. Specifically, each user is assigned a specific interleaver in the IFDM modulation matrix to enable the base station to separate users. Meanwhile, a multi-user cross-domain orthogonal approximate message-passing (MU-CD-OAMP) receiver is developed, which exploits the sparsity of the time-domain channels and leverages the right-unitarily invariance property of each user's IFDM modulation matrix, achieving the replica maximum a posteriori (MAP) performance with low complexity. Numerical results show that the proposed IFDMA can achieve bit-error rate (BER) performance gains of about 4 ~ 5 dB compared to existing AFDM-SCMA and OTFS-SCMA with 5G-NR LDPC codes.

## Learning Joint Source-Channel Coding for Wireless Image Transmission: A Benchmark

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:11143290
- **Type**: conference
- **Published**: 7-10 July 
- **Authors**: Tianjian Dang, Sixian Wang, Zhenyu Liu +3
- **PDF**: https://ieeexplore.ieee.org/document/11143290
- **Abstract**: Deep learning-based joint source-channel coding (JSCC) has demonstrated remarkable advancements in wireless image transmission. However, most existing evaluations assume stationary channel models, such as additive white Gaussian noise (AWGN) and Rayleigh fading channels, which do not capture the features of practical wireless environments where separate source-channel coding (SSCC) is already deployed (e.g., in 4 G and 5 G systems). Furthermore, the lack of a unified and fair benchmark has prevented researchers from conducting objective comparisons among JSCC schemes. To address these challenges, we introduce JSCCBench, an end-to-end JSCC benchmark that extends JSCC evaluation by incorporating orthogonal frequency-division multiplexing (OFDM) and a diverse set of non-stationary wireless channel scenarios. Experimental results indicate that current JSCC schemes possess a certain degree of robustness and effectiveness in more realistic wireless communication scenarios. However, extensive results also reveal the shortcomings of the schemes in some wireless communication scenarios. Specifically, we evaluate several representative JSCC approaches. Even those with channel-adaptive designs show significant room for improvement, while others achieve only moderate performance. The JSCCBench framework is publicly available at https://github.com/tianjian00/JSCCBench, providing a standardized platform for future JSCC research and development.

## Iterative Polar Coded OFDM-Based Underwater Acoustic Communication

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:11104453
- **Type**: conference
- **Published**: 7-10 July 
- **Authors**: Zeynep B. Kaykac Egilmez, Abdulaziz Babulghum, Mohammed El-Hajjar
- **PDF**: https://ieeexplore.ieee.org/document/11104453
- **Abstract**: Underwater communication and networking technologies are essential for exploring marine life, extracting subsea resources, and conducting national defence missions. However, underwater communications face significant challenges due to the complexity of underwater acoustic channels, leading to delays and reduced reliability. Recent studies have demonstrated that polar coding is highly effective in improving performance, when applied to underwater acoustic communications using Orthogonal Frequency Division Multiplexing (OFDM). However, the iterative turbo-detection capability of polar codes has not been utilized for underwater acoustic communication. In this paper, we propose and analyze an iterative polar-coded OFDM scheme for a time-varying underwater acoustic communication system. The performance of the proposed scheme is compared to that of a system employing the Recursive Systematic Convolutional (RSC) channel decoder. Furthermore, to characterize the proposed system, Extrinsic Information Transfer (EXIT) charts have been utilized to analyze the convergence behaviour of the iterative system considered. Our simulation results show that both the soft-decision Soft Cancellation (SCAN) and the hard-decision Successive Cancellation List (SCL) polar decoding algorithms can outperform the RSC decoding, providing approximately 7 dB and 9 dB gain at a bit error rate (BER) of ${10}^{-4}$, respectively, when communicated over a time-varying underwater acoustic channel.

## Iterative Detection and Decoding in One-Bit Quantized MIMO Systems

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:11143531
- **Type**: conference
- **Published**: 7-10 July 
- **Authors**: Péter Horváth, Gerald Matz
- **PDF**: https://ieeexplore.ieee.org/document/11143531
- **Abstract**: We consider the uplink of massive MIMO systems with one-bit quantization and propose an iterative detection and decoding (IDD) receiver based on a factor graph representation and the sum-product algorithm. We derive the relevant sum-product messages, introduce Gaussian approximations to control computational complexity, and describe the message schedule. Numerical experiments demonstrate that the BLER performance of our receiver is comparable to the state of the art, even though our method has much lower complexity – quadratic rather than exponential in the number of users – and hence scales well to large system configurations. We show that a proper scheduling of the decoding iterations substantially improves the error rate performance without increasing the computational complexity. In particular, we find that it is not beneficial to schedule the majority of decoding iterations in the initial detection iterations.

## Optimized Non-Binary Polar Codes for Short Block-Length Communications

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:11104477
- **Type**: conference
- **Published**: 7-10 July 
- **Authors**: Ali Eltohamy, Matthias Korb
- **PDF**: https://ieeexplore.ieee.org/document/11104477
- **Abstract**: Internet of Things (IoT) and direct-access Satellite IoT (SIoT) systems demand short block-length communication to accommodate brief transmissions under strict power constraints. In this context, it is critical to ensure high error correction reliability with minimal energy. One prominent candidate for Forward Error Correction (FEC) is Polar codes. Introduced by Arikan in 2009, Polar codes achieve the capacity of binary-input discrete memoryless channels through the phenomenon of channel polarization. While generalizing Polar codes to non-binary fields $\mathbb{GF}(q)$ can yield improved performance compared to their binary counterpart at long block lengths, they fall short at short block length even when applying techniques such as frozen-bit-pattern and kernel optimization. In this paper, additional strategies are evaluated that go beyond these baseline techniques. In detail, kernel optimization is extended towards a multi-kernel approach and a joint optimization of modulation order and code rate on system level is proposed. Simulation results demonstrate that under these careful optimizations, non-binary Polar codes can indeed outperform binary Polar codes for short block length, as well, making them the optimal channel-coding choice for SIoT applications.

## Hardware-Optimized RNN Detection for Insertion/Deletion Channels in Wireless Communication

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:11130325
- **Type**: conference
- **Published**: 6-9 July 2
- **Authors**: Matthias Nickel, Lester Kalms, Julian Haase +2
- **PDF**: https://ieeexplore.ieee.org/document/11130325
- **Abstract**: Insertion and deletion errors pose a significant challenge in wireless communication, especially for energyconstrained Internet of Everything (IoE) devices operating in noisy 6 G environments. While traditional error-correcting codes can handle substitution errors, they fall short against synchronization distortions. In this work, we investigate a deep learning-based detection scheme for Insertion/Deletion channels, replacing sequential compute intensive classical approaches such as the Forward-Backward (FB) algorithm with a Recurrent Neural Network (RNN). The log-probabilities predicted by the neural network are forwarded to a Low-Density Parity-Check (LDPC) decoder to recover the transmitted message. To enable easy deployment of RNN on Field Programmable Gate Arrays (FPGAs), we implement a fully streaming, hardware-optimized RNN library in C++ using Vitis High-Level Systhesis (HLS). Our FPGA-based design provides flexible integration and competitive inference performance compared to related work.

## Sustainability and Scalability of Physical Layer Security in Next-Generation Networks

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:11125294
- **Type**: conference
- **Published**: 6-10 July 
- **Authors**: Pin-Hsun Lin, Karl-Ludwig Besser, Eduard A. Jorswieck
- **PDF**: https://ieeexplore.ieee.org/document/11125294
- **Abstract**: Physical layer security (PLS) has emerged as a promising approach to ensure data confidentiality in next-generation wireless networks. As these networks transition toward 6G and beyond, two pivotal design considerations are sustainability—the ability to maintain secure communications under limited resources—and scalability—the capacity to accommodate a massive number of users and devices without compromising performance. In this paper, we explore four critical issues that can hamper the sustainable and scalable deployment of PLS: superfluous protection of non-sensitive data, non-uniform resource utilization, outages caused by limited channel information, and the rigidity of reliability–secrecy tradeoffs in finite blocklength scenarios. We propose solutions for each challenge, including schemes that protect only latent sensitive content, opportunistic scheduling of secret key generation during off-peak hours, correlation shaping to enable zero-outage secrecy even under slow fading, and neural-network-based coding to flexibly balance reliability and secrecy. Numerical and experimental results show that these approaches can significantly improve energy efficiency, resource utilization, and secrecy performance. Our findings pave the way for more sustainable and scalable PLS strategies in future large-scale wireless deployments.

## Low-Density Parity Check (LDPC) Architecture Using Verilog

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:11158053
- **Type**: conference
- **Published**: 4-5 July 2
- **Authors**: Abhay Chopde, Dhruvesh Kamble, Kapil Sangameshwar +1
- **PDF**: https://ieeexplore.ieee.org/document/11158053
- **Abstract**: Low-density Parity-Check (LDPC) codes have significantly been a vital resource in modern communication systems due to their close-to-capacity error-correcting capabilities and tendency to align well with various applications. The paper describes the architecture design and implementation of an LDPC encoder and decoder using Verilog. As for the state-of-the-art study on encoding and decoding, particularly referring to iterative methods for example, Bit-Flipping, Min-Sum, and Sum-Product algorithms, were considered. These methods are evaluated in terms of BER performance, computational complexity, and hardware efficiency. The proposed architecture is systematic encoder decoder integrated efficiently in such a way that it is optimized for high throughput and low resource utilization. Simulation results indicated the aptitude of the system in correcting transmission errors with respect to different noise conditions. It will depict its applicability in wireless communication in 5G networks and deep-space missions. These results show a possibility of LDPC codes to balance efficiency and reliability, hence provide significant contributions toward the advance of error-correcting systems.

## AI-Driven Error Correction Mechanisms in Next-Generation Wireless Networks

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:11158779
- **Type**: conference
- **Published**: 4-5 July 2
- **Authors**: A. V. V. Sudhakar, Heena Khera, Gururaj Hosamani +3
- **PDF**: https://ieeexplore.ieee.org/document/11158779
- **Abstract**: Communication reliability becomes crucial in ever changing and challenging environments in next generation wireless networks; hence, efficient error correction mechanisms are highly sought after. The paper presents an AI driven method of coding Error Correction Codes (ECC) based on advanced machine learning techniques like the Reinforcement Learning (RL) and genetic algorithms. Preprocessing is the first step in the process where channel conditions and signal parameters are prepared for AI models. Handling data normalization, cleaning and organizing those relevant features like SNR and packet loss patterns. After finding these features, we use them to extract feature, so that AI models will focus on the most important feature which has impact on the network performance. The core of the proposed approach is in the classifier, where we let AI models optimize the construction of ECC parameters (block length and redundancy) to optimize performance. Experimental results show the superiority of AI driven error correction in terms of performance in the face of difficult Wi-Fi transmission, thereby improving reliability of the future networks.

## A New Class of Codes with Error Localization and its Noise Immunity: Core Concept

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:11079325
- **Type**: conference
- **Published**: 30 June-3 
- **Authors**: Victor V. Zyablov, Sergey L. Portnoy, Sergey E. Nikitin +2
- **PDF**: https://ieeexplore.ieee.org/document/11079325
- **Abstract**: The possibility of reinterpreting established coding structures is considered. A new modification of traditional cascade and generalized cascade codes is proposed, which, in turn, gives rise to a fundamentally new family of codes and opens up prospects for the development of novel decoding algorithms. Three examples of code constructions with error localization are presented, along with the results of their simulation. Directions for further research on new classes of codes are outlined.

## Complexity-Efficient LLR Estimation Using Piecewise Polynomial Fitting for LDPC Decoding in 100 Gb/S Bandwidth-Limited Flexible-Rate IM/DD System

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:11109143
- **Type**: conference
- **Published**: 29 June-3 
- **Authors**: Yiao Zhang, Xiangchen Kong, Yanlu Huang +5
- **PDF**: https://ieeexplore.ieee.org/document/11109143
- **Abstract**: We demonstrate a low complexity LLR estimation method based on piecewise polynomial fitting for LDPC decoding in 100 Gb/s bandwidth-limited flexible-rate IM/DD system, which reduces complexity by more than 90 % while maintaining almost equivalent performance.

## Adaptation of 5G NR LDPC-Coded Probabilistic Amplitude Shaping to 50 GBaud PAM4 Signals in IM/DD Bandwidth-Limited System

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:11110465
- **Type**: conference
- **Published**: 29 June-3 
- **Authors**: Xiangchen Kong, Yiao Zhang, Liyan Wu +5
- **PDF**: https://ieeexplore.ieee.org/document/11110465
- **Abstract**: We experimentally demonstrate 50-GBaud probabilistically shaped PAM4 via 5G NR LDPC-coded PAS over 20 km in IM/DD bandwidth-limited system, achieving up to 2.6 dB receiver sensitivity gain over uniformly distributed PAM4 post-FEC decoding and IDM.

## State Error Decoding for Combating Equalizer-Induced Error Propagation in Terahertz-Over-Fiber Systems

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:11111107
- **Type**: conference
- **Published**: 29 June-3 
- **Authors**: Liga Bai, Lu Zhang, Zhidong Lyu +4
- **PDF**: https://ieeexplore.ieee.org/document/11111107
- **Abstract**: This paper presents a state error decoding algorithm to mitigate equalizer-induced error propagation in terahertz-over-fiber systems, achieving a 1.7 dB power gain and improved post-FEC performance for 30 Gbit/s QPSK transmission at 277 GHz.

## Application of SD-FEC to ${b}$-Modulation Based on Inverse Scattering Transform

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:11110989
- **Type**: conference
- **Published**: 29 June-3 
- **Authors**: Kaito Geshi, Ryotaro Harada, Takumi Motomura +4
- **PDF**: https://ieeexplore.ieee.org/document/11110989
- **Abstract**: We propose applying a neural network-based demodulator and SD-FEC to b-modulation. We demonstrate that the transmission distance of a 64-QAM signal can be extended to 5,000 km using the proposed method through numerical simulations.

## Redundant-Bit-Free Error Correction Utilizing Short-Term Correlation in Oversampled Waveform in Underwater Optical Wireless Communications

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:11109964
- **Type**: conference
- **Published**: 29 June-3 
- **Authors**: Masanori Hanawa, Taishu Takatsuki, Ekkaphol Khansalee +2
- **PDF**: https://ieeexplore.ieee.org/document/11109964
- **Abstract**: A redundant-bit-free bit error correction, utilizing short-term correlation in received samples through $2 \times$ oversampling, is proposed. Experiments achieved 1.2 dB decoding gain for OOK in underwater optical wireless transmission by error correction without additional redundant bits.

## Experimental Verification of Physical Layer Key Generation and Distribution Based on End-to-End Error Vector Phase

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:11109185
- **Type**: conference
- **Published**: 29 June-3 
- **Authors**: Yanwen Zhu, Yuang Li, Xu Zhang +4
- **PDF**: https://ieeexplore.ieee.org/document/11109185
- **Abstract**: We propose and experimentally verify an error-free 0.8 Gbps key generation rate optical communication system based on Error Vector Phase over 120km Fiber, without modifying the existing commercial system architecture.

## FEC-Assist Decision-Directed Equalization for Bandwidth-Limited Optical Interconnection

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:11110789
- **Type**: conference
- **Published**: 29 June-3 
- **Authors**: Xuanwei Liu, Yuyao Wen, Junyuan Song +5
- **PDF**: https://ieeexplore.ieee.org/document/11110789
- **Abstract**: We propose a FEC-assist decision-directed equalizer to mitigate inter-symbol interference in bandwidth-limited IM/DD systems. Experimental validation on a 160 Gbit/s PAM4 interconnction demonstrates over 1.5 dB receiver sensitivity improvement compared with conventional methods.

## End-to-End Amplitude Noise based Classical Key Generation and Distribution with FPGA-implemented Post-Processing

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:11110298
- **Type**: conference
- **Published**: 29 June-3 
- **Authors**: Yanwen Zhu, Yuang Li, Xu Zhang +4
- **PDF**: https://ieeexplore.ieee.org/document/11110298
- **Abstract**: The PLSKGD scheme based on E2E amplitude noise is proposed and implemented on FPGA for quantization, information reconciliation, and privacy amplification. An experimental KGR of 1.21 Gbps was achieved on a 120 km optical fiber link.

## LDPC decoder based on a minimalist bipartite GCN

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:11145491
- **Type**: conference
- **Published**: 28-31 July
- **Authors**: Yiqun Pan, Qinghua Tian, Fangxu Yang +5
- **PDF**: https://ieeexplore.ieee.org/document/11145491
- **Abstract**: This paper proposes a Low-Density Parity-Check (LDPC) decoder based on a minimalist bipartite graph convolutional neural network (GCN). The proposed method has been validated in a 16QAM coherent optical communication simulation system.

## Highly Efficient Information Reconciliation Based on Correlation Thresholding Driven by Experimental Data in Classical Key Distribution

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:11145588
- **Type**: conference
- **Published**: 28-31 July
- **Authors**: Manlin Guo, Linjie Xu, Xiaogang Wang +4
- **PDF**: https://ieeexplore.ieee.org/document/11145588
- **Abstract**: An ET-based adaptive scheme for classical key post-processing reduces LDPC decoding iterations by 76.8% and high-error FER by 74.2%, greatly improving efficiency and lowering computational cost.

## A Next-Generation Real-Time Optical Data Link for Air-Gapped Environments Using a Novel Firmware-Based Post-Quantum Methodology

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:11186611
- **Type**: conference
- **Published**: 28-31 July
- **Authors**: Zeyad E. Badwi, Mohmed F. Elsamman, Walid S. Mohamed +2
- **PDF**: https://ieeexplore.ieee.org/document/11186611
- **Abstract**: Air-gapped networks remain a critical component in safeguarding classified and mission-critical systems; however, they pose significant challenges for secure data exchange. This paper presents EgyXOS, a novel firmwarebased optical communication platform designed to enable highassurance, one-way data transmission between physically isolated endpoints. Operating independently of any operating system, EgyXOS minimizes the attack surface while integrating lattice-based post-quantum encryption, forward error correction using LDPC codes, and real-time anomaly detection within its architecture. Specifically utilizing an NTRU-based lattice cryptographic scheme $N$ is $701, q$ is 2048 and aligned with NIST Round 4 post-quantum candidates. We provide a detailed description of the system's proprietary optical encoding schemes, cryptographic layering strategies, and secure transmission algorithms. Experimental validation demonstrates secure optical data transfer rates up to $256 ~\text{KB} / \mathrm{s}$ with sub- 5 millisecond latency, achieving full resistance to electromagnetic side-channel leakage under 40 GHz spectrum analysis. Comparative evaluations against LANTENNA, MOSQUITO, and military-grade free-space optical systems highlight EgyXOS's superior performance, cryptographic resilience, and physical-layer security. The proposed platform offers a futureproof solution for secure data exchange across air-gapped environments, meeting the stringent demands of defense, intelligence, and critical infrastructure sectors.

## A Study on the Fitness of GA for Improving SP Decoding Performance

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:11192636
- **Type**: conference
- **Published**: 28-30 July
- **Authors**: Madoka Nishikawa, Yasuaki Nakamura, Yasushi Kanai +1
- **PDF**: https://ieeexplore.ieee.org/document/11192636
- **Abstract**: We study low-density parity-check (LDPC) coding and iterative decoding methods for shingled magnetic recording (SMR) in ultra-high-density hard disk drives (HDDs). Previously, we applied a neural network to evaluate the log-likelihood ratios (LLRs) related to row operations in the sum-product (SP) decoder for LDPC code. Then, we updated the LLR considering the influence of noise depending on the recording pattern by providing the LLRs for the decoding target and its adjacent bits to the neural network in SP decoding. Furthermore, we explored the optimal parameters to update the LLRs by applying the genetic algorithm (GA). In this study, to explore more optimal update parameters, we propose the fitness to enhance the selection accuracy of the LLR to be updated and the number of updating targets. Then, we aim to improve the performance of SP decoding based on the GA results. As a result, applying the proposed fitness to GA remains in high selection accuracy and increases the number of updating targets in SP decoding. Also, it achieves error-free performance with fewer iterations of turbo equalization compared to the conventional fitness.

## Quantum Key Distribution in Power System Communication

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:11096656
- **Type**: conference
- **Published**: 27 June-1 
- **Authors**: Magomadov Zelimkhan, Oleg O. Khamisov
- **PDF**: https://ieeexplore.ieee.org/document/11096656
- **Abstract**: As service networks pass in the direction of distributed structures, microgrids are becoming increasingly important to improve both resistance and energy efficiency. However, reliance on digital communication also depends on a considerable number of cyber threats. Unauthorized access attempts can be detected through increased Quantum Bit Error Rates (QBER). Additionally, it also improves major reliability by including error correction techniques such as low density (LDPC) parity testing and Reed-Solomon codes. The results show that quantum key distribution (QKD) greatly enhances security by blocking unauthorized access, while also ensuring encryption suitable for low latency real-time microgroup management. We introduce a quantum key distribution -based security framework tailored for Supervisory Control and Data Acquisition (SCADA) systems, Distributed Energy Resources (DERs), and critical infrastructure. Our evaluation uses simulations to analyze Quantum Bit Error Rates across various noise and eavesdropping scenarios, examining their impact on encryption latency and overall system integrity. These findings underscore the viability of quantum key distribution for next-generation power grids, offering robust protection against emerging quantum cyber threats. This study provides a foundation for seamlessly integrating quantum key distribution into energy systems, advancing toward quantum-resilient microgrid communication.

## Distribution Network Fault Data Compression and Efficient Transmission Technology Based on Deep Learning

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:11212177
- **Type**: conference
- **Published**: 26-27 July
- **Authors**: Youzhuo Zheng, Di Weng, Jiangfeng Yan +1
- **PDF**: https://ieeexplore.ieee.org/document/11212177
- **Abstract**: There are problems such as limited bandwidth resources and large data volume in the transmission of distribution network fault data. This study proposes a multimodal data compression and transmission technology framework based on deep learning. By integrating the collaborative mechanism of graph neural network and distributed compressed sensing, an end-to-end solution from feature extraction to data compression is constructed. In the feature extraction stage, a cascade structure of graph convolutional network and spatiotemporal attention module is adopted. In the data compression stage, a distributed compressed sensing algorithm is deployed based on the edge computing architecture. By designing an overcomplete dictionary and adaptive sparse basis function, the original high-dimensional time series signal is projected into a low-dimensional measurement space and combined with residual quantization coding to further reduce data redundancy. A hybrid coding strategy of cloud-edge collaboration is introduced at the transmission optimization level, in which a lightweight entropy encoder is used on the edge side to process sparse coefficients, and a deep generative adversarial network is used on the cloud side to reconstruct the original waveform. Experiments show that the cloud-edge collaboration strategy reduces bandwidth usage, with the maximum bandwidth usage being only 22.8 Mbps, and the transmission delay being stable in the range of ${1 2 - 5 5 \text{ms}}$. In addition, through the typical case of single-phase grounding fault compression transmission, the adaptability and effectiveness of this method in complex distribution network scenarios are further verified, providing a new solution for the sustainable development of smart distribution networks.

## Overview of LDPC Decoding Based on Deep Learning

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:11427203
- **Type**: conference
- **Published**: 25-27 July
- **Authors**: Xiangwei Ren, Tao Tang, Hong Wen +3
- **PDF**: https://ieeexplore.ieee.org/document/11427203
- **Abstract**: LDPC codes, as an error correcting code close to the Shannon limit, are widely used in modern communication systems such as 5 G, satellite communication, deep space communication, and other fields. Traditional LDPC decoding algorithms, such as belief propagation (BP) algorithm and its variants, have achieved good performance, but face challenges such as high complexity and slow convergence, especially when dealing with long code lengths and high noise scenarios. The rise of deep learning has brought new opportunities for LDPC decoding, and its powerful features learning and pattern recognition capabilities are expected to break through the bottleneck of traditional decoding. Based on the overview of deep neural network decoding methods for LDPC codes by data-driven and model driven approaches, this paper analysis and comparison of error rate performance of short code $\mathbf{H} (8,16)$ matrix by convolutional neural networks (CNN), residual network (ResNet), and Kolmogorov-Arnold Network (KAN).

## Key Technologies of Distributed Array Antennas for Receiving Signals from High-Dynamic Targets

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:11274380
- **Type**: conference
- **Published**: 25-27 July
- **Authors**: Yiwen Chen, Feng Ding
- **PDF**: https://ieeexplore.ieee.org/document/11274380
- **Abstract**: The rapid advancement of space technology has created an urgent demand for systems capable of tracking and communicating with high-dynamic targets, such as low-Earthorbit (LEO) satellites and deep-space probes. Distributed Array Antennas (DAAs) present a superior solution, offering significant advantages like large equivalent aperture, high spatial resolution, robust interference suppression, and enhanced system reliability. However, high-dynamic targets introduce formidable technical challenges, including extreme Doppler shifts, rapid changes in angle of arrival, and weak signal conditions. This paper systematically addresses these issues by proposing a comprehensive technology framework that integrates several advanced approaches. Key components of this framework include predictive Doppler compensation algorithms, precision time-phase synchronization mechanisms, adaptive digital beamforming techniques, sophisticated signal enhancement strategies, and efficient hierarchical processing architectures. Simulation results validate the efficacy of these integrated technologies, demonstrating marked improvements in tracking accuracy, synchronization performance, and signal quality. This work provides both theoretical insights and practical guidance for designing the next generation of DAA systems for high-dynamic applications.

## Performance of RF MIMO MMSE OFDMA for Visible Light Communication

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:11135982
- **Type**: conference
- **Published**: 24-27 July
- **Authors**: Karthikeyan A, Srinidhi Bhimesh, Pooja Jain +1
- **PDF**: https://ieeexplore.ieee.org/document/11135982
- **Abstract**: Visible Light Communication (VLC) is emerging as a high-speed data transmission technology, leveraging the unlicensed visible light spectrum. However, VLC faces challenges such as limited bandwidth, interference from ambient light, and performance degradation under non-line-of-sight (NLOS) conditions. This paper presents a hybrid two-cross-two Multiple Input Multiple Output (MIMO) system that integrates VLC with Radio Frequency (RF) communication. The system employs Orthogonal Frequency Division Multiple Access (OFDMA) to support multi-user environments and Minimum Mean Square Error (MMSE) equalization to minimize interference. For error correction, the system uses various channel coding schemes, including Maximum Rank Distance (MRD), Reed-Solomon (RS), and Low- Density Parity Check (LDPC) codes, with simulations conducted to evaluate Bit Error Rate (BER) performance across different Signal-to-Noise Ratios (SNR). Simulation results demonstrate that MRD coding provides superior error resilience, making it an ideal choice for hybrid VLC-RF systems. In contrast, RS and LDPC codes exhibit varying performance depending on the operating conditions.

## Intelligent Channel Coding Using Graph Neural Networks: A Machine Learning Perspective

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:11171308
- **Type**: conference
- **Published**: 21-23 July
- **Authors**: K. Koushik, M. Thilakeshwari, T. Likith Vignesh +2
- **PDF**: https://ieeexplore.ieee.org/document/11171308
- **Abstract**: Wireless communication is rapidly evolving, and this evolution has led to increasing demands for better error correction, lower latency, and higher adaptability, particularly in Beyond 5G (B5G) networks. Traditional channel coding methods like Low-density Parity-check (LDPC) and Turbo codes often struggle to meet these advanced requirements. To address this challenge, we explore the use of Graph Neural Networks (GNNs) to enhance LDPC decoding. By imposing the structured nature of the Tanner graph, GNNs improve decoding accuracy, optimize bit error rate (BER), and adapt to changing signal conditions in real-time. We implement and evaluate our approach using MATLAB and Python, training our ML-based decoder on varying SNR levels to ensure robustness. The results show that integrating machine learning into LDPC decoding significantly enhances error correction and communication reliability. This work highlights the potential of ML-driven techniques in shaping the future of wireless networks.

## HERACLES: Hierarchical Semantic Communications for Distributed Dynamic Sensor Fusion

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:11183785
- **Type**: conference
- **Published**: 21-23 July
- **Authors**: Langtian Qin, Yashuo Wu, Sameh Najeh +2
- **PDF**: https://ieeexplore.ieee.org/document/11183785
- **Abstract**: Distributed sensor fusion is a key component of a broad spectrum of applications, such as autonomous systems, where the ability of jointly process multi-sensor data at the edge boosts the range of operating conditions and overall task performance. However, existing distributed sensor fusion approaches encounter limitations in achieving efficient transmission and computation, primarily due to sensor data redundancy, unreliable sensor data transmission, and inflexible sensor fusion methods. In this paper, we propose HERACLES, a distributed sensor fusion framework that connects multi-branched dynamic neural network architectures, which we extend to include branches of different complexity, to (i) a computing methodology that distributes portions of the multi-branched neural network across mobile devices and edge servers, enabling flexible semantic feature extraction and sensor fusion; (ii) a hierarchical modulation-based transmission strategy, where multi-modal semantic features are allocated to different modulation layers to provide varying levels of error protection, and (iii) an infrastructure-level logic that controls the matching between semantic features and modulation layers, and the complexity of the neural model itself to meet an accuracy target while minimizing latency and energy consumption. As a result, HERACLES deeply connects computing, communications and resource allocations in a semantic and context-aware fashion. We evaluate HERACLES using real-world datasets and demonstrate that it can reduce the total delay and energy consumption by 20.39%–89.41% and 4.86%–88.17% (resp.), while maintaining near-optimal inference accuracy. The evaluation code is available at https://github.com/qlt315/HERACLES.

## Robust Iterative Multi-User Data Detection for Polar-Coded IDMA Underwater Acoustic Communications

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:11194645
- **Type**: conference
- **Published**: 18-21 July
- **Authors**: Lin Cheng, Wei Men, Wei Ge +2
- **PDF**: https://ieeexplore.ieee.org/document/11194645
- **Abstract**: Reliable and efficient multi-user acoustic communication (MUAC) is essential for underwater acoustic sensor networks. However, the limited bandwidth, significant multipath delays, and strong multi-access interference (MAI) in underwater acoustic channels pose extreme challenges to MUAC systems. In this paper, we investigate a MUAC scheme that combines polar codes with interleaved division multiple access (IDMA). This scheme leverages the error correction strength of polar codes to enhance communication reliability and supports higher communication rates. Furthermore, we propose an iterative multi-user detection method based on successive interference cancellation (IMDD-SIC), which is well-suited for soft-rake IDMA architectures. In particular, accurate polar decoding is realized due to the ability of IMDD-SIC to mitigate the impact of MAI on channel estimation. Finally, the communication performance of the proposed polar-coded IDMA scheme is evaluated through field experiments conducted in Songhua Lake. The results of four-user communication experiments show that the proposed IMDD-SIC achieves a lower BER compared to conventional receivers under low SNR conditions.

## Deep Learning-Based Decoding of Protograph LDPC Codes for Spin-Transfer Torque Magnetic Random Access Memory

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:11208063
- **Type**: conference
- **Published**: 16-18 July
- **Authors**: Jie Dong, Kui Cai, Zhen Mei +2
- **PDF**: https://ieeexplore.ieee.org/document/11208063
- **Abstract**: Spin-transfer torque magnetic random access memory (STT-MRAM) has attracted significant attention as a promising memory technology for consumer electronics. However, its reliability is severely degraded by process variation and thermal fluctuation, which lead to both write and read errors. An increase in working temperature also results in an unknown resistance offset. In this paper, we first propose novel neural network (NN)-based decoding schemes for protograph low-density parity-check (P-LDPC) codes with parallel edges in the base graph. We further develop a transfer learning (TL)-based approach to mitigate the resistance offset, which can reduce the training data size by 90%. Simulation results demonstrate the effectiveness of these approaches in improving decoding performance in the presence of various channel impairments of STT-MRAM.

## Adaptive Quantization for Key Generation: Balancing Rate and Consistency

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:11171534
- **Type**: conference
- **Published**: 12-14 July
- **Authors**: Ruikai Zhang, Sicheng Song, Shuhang He +3
- **PDF**: https://ieeexplore.ieee.org/document/11171534
- **Abstract**: Wireless key generation systems often face challenges in achieving low Key Disagreement Rates (KDR) and Key Generation Rate (KGR) across diverse scenarios, limiting their reliability and efficiency. This paper presents a wireless key generation system based on the ESP32 platform, combining quantization methods and error correction codes to address these issues through comparative experiments. To obtain the ideal quantization order in different scenarios, we propose an adaptive quantization order selection model based on the Technique for Order Preference by Similarity to Ideal Solution (TOPSIS). The results indicate that the performance of quantization methods is influenced by both the specific scenarios and the quantization order employed. Moreover, the combination of Joint Amplitude-Phase Equiprobable Quantization (JAPEQ) and Low-Density Parity-Check Codes (LDPC) outperforms other combinations in terms of KDR. Finally, our proposed adaptive quantization order selection model demonstrates ideal performance in terms of both key consistency and generation rate.

## A Link Adaptive Intelligent Modulation and Coding Strategy Based on Deep Reinforcement Learning

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:11136977
- **Type**: conference
- **Published**: 11-13 July
- **Authors**: Tiantian Jiang, Zhe Zhang, Qichao Liang +3
- **PDF**: https://ieeexplore.ieee.org/document/11136977
- **Abstract**: To address the challenge of coordinated optimization for reliability and efficiency in 5 G adaptive modulation and coding, this paper proposes an intelligent decision-making strategy based on the Dueling Deep Q-Network. By constructing a dual-branch network architecture that decouples state value and action advantage, dynamic perception of time-varying channel states and adaptive optimization of modulation coding schemes are achieved. In scenarios with signal-to-noise ratio fluctuations ranging from −5 dB to 35 dB, the proposed strategy significantly reduces the signal-to-noise ratio requirement corresponding to the bit error rate threshold and improves spectral efficiency compared with traditional channel quality indicator-modulation and coding scheme (CQI-MCS) lookup methods and basic Deep Q-Network algorithms. This study validates the effectiveness of deep reinforcement learning in breaking through fixed threshold limitations and realizing dynamic adaptive modulation and coding optimization, providing new insights for the coordinated adaptation of 5 G URLLC and eMBB services.

## Low-Complexity LDPC Decoder for Cloud Based Architectures

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:11306760
- **Type**: conference
- **Published**: 10-13 July
- **Authors**: Satya Kumar Vankayala, Tirthankar Mittra, Thirumulanathan D +3
- **PDF**: https://ieeexplore.ieee.org/document/11306760
- **Abstract**: LDPC code structure allows high parallelism to deliver the high demanding data rates, but the LDPC decoder does not perform well concerning the low latency requirements needed for high-speed applications. This is partly due to the soft decoder involving the computation of non-linear functions with high computational complexity. Virtualized radio access networks (VRANs) are a new paradigm that brings software-based network functions to run on the cloud. In this paper, we propose four LDPC soft decoder approximations: a piecewise linear (PL) approximation, a polynomial approximation, a machine learning (ML) based approximation, and a modification of min-sum approximation using regression methods. We show that the approximations retain a comparable BLER performance and, at the same time, bring down the computational complexity of the decoder. We also show that the BLER performance of our approximations is significantly better than the well-known min-sum approximation. Our methods are suitable for direct implementation in cloud based VRAN systems.
