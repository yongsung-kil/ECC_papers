# arXiv — 2022-11 (1차선별 통과)


## Parallel decoder for Low Density Parity Check Codes: A MPSoC study

- **Status**: ✅
- **Reason**: MPSoC/NoC 기반 병렬 LDPC 디코더, reduced min-sum 사용 — 이식 가능 HW 병렬 아키텍처(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: arxiv:2211.14382v1
- **Type**: preprint
- **Published**: 2022-11-25
- **Authors**: Sudeep Kanur, Georgios Georgakarakos, Antti Siirilä +4
- **PDF**: https://arxiv.org/pdf/2211.14382v1
- **Abstract**: The near channel performance of Low Density Parity Check Codes (LDPC) has motivated its wide applications. Iterative decoding of LDPC codes provides significant implementation challenges as the complexity grows with the code size. Recent trends in integrating Multiprocessor System on Chip (MPSoC) with Network on Chip (NoC) gives a modular platform for parallel implementation. This paper presents an implementation platform for decoding LDPC codes based on HeMPS, an open source MPSoC framework based on NoC communication fabric. Reduced minimum sum algorithm is used for decoding LDPC codes and simulations are performed using HeMPS tool. The data rate and speedup factor measured for decoding a rate 1/2 LDPC code characterised by 252x504 parity matrix is presented

## Comparison of different coding schemes for 1-bit ADC

- **Status**: ✅
- **Reason**: 1-bit ADC 양자화 채널에서 LDPC 등 코딩 성능 비교 — 1비트 양자화 LLR/FER 분석이 NAND 양자화 ECC와 연관, 애매하여 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: arxiv:2211.10712v1
- **Type**: preprint
- **Published**: 2022-11-19
- **Authors**: Fedor Ivanov, Dmitry Osipov
- **PDF**: https://arxiv.org/pdf/2211.10712v1
- **Abstract**: This paper devotes to comparison of different coding schemes (various constructions of Polar and LDPC codes, Product codes and BCH codes) for the case when information is transmitted over AWGN channel with quantization with lowest possible complexity and resolution: 1-bit. We examine performance (in terms of Frame-error-rate -- FER) for schemes mentioned above and give some reasoning for results we obtained. Also we give some recommendations for choosing coding schemes for a given code rate and code length.
