# Quantum circuit simulation
Classical simulation of quantum circuits, treated as an HPC problem. A full state vector holds 2^n complex amplitudes, so memory caps a 16 GB laptop at about 28–30 qubits. Applying a gate streams the whole vector through memory, which makes the kernel memory-bandwidth bound. The main speedups come from SIMD, OpenMP threads, gate fusion, cache blocking, GPUs (cuQuantum, Qiskit Aer GPU) and MPI distribution across nodes. Tensor networks, MPS, decision diagrams and stabilizer methods beat the state vector only when the circuit has exploitable structure.

## Prerequisites
- [HPC basics](../../low-level/hpc-basics/README.md)

## Questions
- [ ] Which baseline simulators and papers define CPU state-vector simulation (qHiPSTER/Intel-QS, Häner & Steiger 2017, QuEST, qsim, Qulacs, Qiskit Aer, PennyLane Lightning), and which have public, readable C++ code?
- [ ] How does a state-vector simulator apply a k-qubit gate, and how do memory layout, SIMD (AVX2/AVX-512/NEON) and OpenMP thresholds change its speed?
- [ ] How do qsim, Qiskit Aer and Qulacs decide which gates to fuse, and why is the best fused-gate size about 2–4?
- [ ] Can a dynamic-programming or cost-model fuser (as in Atlas, SC24) beat qsim's fixed fusion rule on a laptop CPU?
- [ ] What fraction of STREAM memory bandwidth do state-vector gate kernels reach, and where do they sit on a roofline?
- [ ] Which standard benchmark circuits and suites (QFT, random circuits, Trotter dynamics, Grover, GHZ; QASMBench, MQT Bench) and which metrics should a simulator study report?
- [ ] What did cross-simulator benchmarks (Jamadagni, Läuchli & Hempel 2024) find, and why do packages differ by up to ~1000× on the same hardware?
- [ ] Can the single-node results of Rezaei et al. 2025 (AVX, AoS layout, prefetching on QuEST) be reproduced on a single-socket laptop, and do they carry over to QuEST v4?
- [ ] How many qubits and how much speed does a laptop CPU give, and what do a consumer GPU, a T4 or an A100 add?
- [ ] How do distributed simulators split qubits into local and global ones, and how do cache blocking and swap scheduling reduce MPI communication?
- [ ] Can distributed communication cost be studied on one laptop with several MPI ranks, and how faithful is that?
- [ ] When do tensor-network contraction, MPS, decision diagrams or stabilizer simulation beat a state vector, and can the right method be chosen automatically?
- [ ] What open problems and known weaknesses (heuristic fusion, missing bandwidth analysis, Apple Silicon/ARM portability, precision bugs, noise cost) are worth extending in a student project?
- [ ] Which reproduce-and-extend project fits a solo undergrad with a laptop and ~8–10 h/week over two semesters?
