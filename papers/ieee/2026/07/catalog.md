# IEEE Xplore — 2026-07


## From SMURF to HI-SMURF: Scalable Multivariate Nonlinear Function Approximation via Compact Stochastic Architectures

- **ID**: ieee:11499434
- **Type**: journal
- **Published**: July 2026
- **Authors**: Xincheng Feng, Wenyong Zhou, Taiqiang Wu +3
- **PDF**: https://ieeexplore.ieee.org/document/11499434
- **Abstract**: Multivariate nonlinear functions are fundamental to many tasks in artificial intelligence (AI) and communication systems but are difficult to implement efficiently in hardware due to high computational complexity and resource demands, especially on edge and embedded devices. Existing stochastic computing (SC) approaches are mostly limited to univariate cases and do not scale well for high-dimensional approximation. This paper presents SMURF (Stochastic Multivariate Universal-Radix Finite-State Machine) and its enhanced variant HI-SMURF (HIgh-Dimensional Stochastic Multivariate Universal-Radix Finite-State Machine) that uses tensor-train (TT) factorization to approximate high-dimensional functions without exponential state growth. SMURF analytically derives steady-state distributions and employs convex optimization for parameter synthesis, while HI-SMURF preserves accuracy under scalable input dimensionality by factorizing the parameter space. Both architectures use configurable state resolution and simple logic circuits driven by stochastic bitstreams. We evaluate SMURF and HI-SMURF on low-density parity-check (LDPC) decoding, image classification, image reconstruction, and high-dimensional nonlinear benchmarks against baselines including Taylor-series expansions, look-up table (LUT) methods, Bernstein polynomial SC, tensor-factorization methods, and quantized multilayer perceptrons (MLPs). Results show that our methods maintain comparable accuracy while dramatically reducing hardware area, power, and area-delay product (ADP), demonstrating superior scalability and efficiency for resource-constrained systems.
