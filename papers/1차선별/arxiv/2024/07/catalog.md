# arXiv — 2024-07 (1차선별 통과)


## Error correction for encoded quantum annealing revisited

- **Status**: ✅
- **Reason**: 양자 어닐링 readout이지만 고전 LDPC(SLHZ)용 bit-flipping 디코더 알고리즘 제안 — 양자 전용 개념 비의존, 고전 바이너리 LDPC에 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: arxiv:2407.15480v2
- **Type**: preprint
- **Published**: 2024-07-22
- **Authors**: Yoshihiro Nambu
- **PDF**: https://arxiv.org/pdf/2407.15480v2
- **Abstract**: F. Pastawski and J. Preskill discussed error correction of quantum annealing (QA) based on a parity-encoded spin system, known as the Sourlas-Lechner-Hauke-Zoller (SLHZ) system. They pointed out that the SLHZ system is closely related to a classical low-density parity-check (LDPC) code and demonstrated its error-correcting capability through a belief propagation (BP) algorithm assuming independent random spin-flip errors. In contrast, Ablash et al. suggested that the SLHZ system does not receive the benefits of post-readout decoding. The reason is that independent random spin-flips are not the most relevant error arising from sampling excited states during the annealing process, whether in closed or open system cases. In this work, we revisit this issue: we propose a very simple decoding algorithm to eliminate errors in the readout of SLHZ systems and show experimental evidence suggesting that SLHZ system exhibits error-correcting capability in decoding annealing readouts. Our new algorithm can be thought of as a bit-flipping algorithm for LDPC codes. Assuming an independent and identical noise model, we found that the performance of our algorithm is comparable to that of the BP algorithm. The error correcting-capability for the sampled readouts was investigated using Monte Carlo calculations that simulate the final time distribution of QA. The results show that the algorithm successfully eliminates errors in the sampled readouts under conditions where error-free state or even code state is not sampled at all. Our simulation suggests that decoding of annealing readouts will be successful if the correctable states can be sampled by annealing, and annealing can be considered to play a role as a pre-process of the classical decoding process. This knowledge will be useful for designing and developing practical QA based on the SLHZ system in the near future.
