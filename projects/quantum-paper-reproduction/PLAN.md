# Quantum paper reproduction

**Status: paused until 1 Dec 2026** for the [LLM code detection review](../llm-code-detection-review/README.md). Re-date the milestones below on 1 Dec.

Goal: by April 2027, one reproduced headline result from one paper, written up as a Finding. Budget: about 8 h/week, roughly 190 h from 14 Oct 2026.

## Profile (as of 2026-10-14)

- Solid: qubit states, amplitudes, the Born rule, relative phase, 2^n amplitudes, Bell states, H and CNOT.
- Gap: no-cloning.
- Untested: quantum algorithms, the wider gate set, circuit notation, DAG, coupling maps, native gates.
- Programming: strong Python, learning with PennyLane; competitive programming in C++ (algorithms yes, build systems such as CMake not yet).

## Decision: 1 Dec 2026

Choose the project direction: [qubit routing](../../quantum-computing/qubit-routing/README.md) (Python, graph search) or [quantum circuit simulation](../../quantum-computing/quantum-circuit-simulation/README.md) (C++ and HPC, which also needs [HPC basics](../../low-level/hpc-basics/README.md)). Decide with the fundamentals Findings done. Default if undecided: routing.

## Milestones

- [ ] 14 Oct–10 Nov: fundamentals Findings in [quantum computing basics](../../quantum-computing/quantum-computing-basics/README.md), in this order: no-cloning, Deutsch–Jozsa, then gates and circuits (PennyLane as the main Source).
- [ ] 11 Nov–1 Dec: DAG, coupling map and native gates; read the first routing or simulation papers; decide the direction.
- [ ] Dec: choose the one paper to reproduce and set up the environment.
- [ ] Jan–Mar: reproduce the headline result.
- [ ] Apr: write the reproduction up as a Finding.

## Working mode

Each Question is one Research run, done inline in the session, following the "Research run" section of [CLAUDE.md](../../CLAUDE.md).
