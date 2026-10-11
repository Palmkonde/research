# HPC basics
How programs get fast on modern hardware, covering only what quantum circuit simulation needs. Parallelism comes in four levels: SIMD vector instructions inside one core (AVX2, AVX-512, NEON), threads across cores (OpenMP), GPUs with thousands of threads, and MPI processes across nodes. Many kernels are limited by memory bandwidth rather than arithmetic. Their speed then depends on caches, data layout and how many bytes they move per FLOP, which the roofline model makes visible. Profiling tools and the STREAM benchmark measure where a program actually sits against those limits.

## Questions
- [ ] What are SIMD instructions (AVX2, AVX-512, NEON), and how does C++ code use them through compiler auto-vectorization or intrinsics?
- [ ] How does OpenMP parallelize a loop, and when does thread overhead outweigh the gain?
- [ ] How do the cache hierarchy and memory bandwidth limit a streaming kernel, and what does the STREAM benchmark measure?
- [ ] What is the roofline model, and how do you compute a kernel's arithmetic intensity?
- [ ] How does a GPU execute a data-parallel kernel, and why does it beat a CPU on bandwidth-bound work?
- [ ] How does MPI split work across processes, and what do communication latency and bandwidth cost?
- [ ] How do you profile and benchmark C++ code reliably (perf, VTune or likwid, timers, warm-up, repetitions)?
