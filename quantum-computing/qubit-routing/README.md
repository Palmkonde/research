# Qubit routing

Qubit routing (also called qubit mapping or layout synthesis) makes a circuit fit a device's coupling map. It picks an initial logical-to-physical layout and inserts SWAPs so every two-qubit gate acts on coupled qubits, at the lowest added gate count, depth or fidelity loss.
The standard baseline is SABRE, now LightSABRE in Qiskit. Other families are A* search (MQT QMAP), tket, exact SAT/MaxSAT/ILP methods (OLSQ2, SATMap, Q-Synth) and RL routers.
Known-optimal benchmarks (QUEKO, QUBIKOS) show heuristics still insert far more SWAPs than needed on large heavy-hex devices, while exact methods only scale to small circuits.
This Topic is scoped as a candidate reproduce-then-extend final project on a laptop.

## Prerequisites

No Prerequisite Topic exists in the vault yet. Gate-level circuits and two-qubit gate decomposition would be candidates.

## Questions

### Baselines and code
- [ ] How does SABRE choose SWAPs (front layer, extended lookahead set, decay), and how does its forward-backward pass refine the initial layout?
- [ ] What exactly did LightSABRE change from the 2019 SABRE, and how much of its 18.9% SWAP gain comes from running many trials instead of from heuristic changes?
- [ ] Which baseline routers (Qiskit SABRE, MQT QMAP A*, tket, OLSQ2, SATMap, Q-Synth, TOQM, NASSC) have public code that still installs alongside Qiskit 2.x?
- [ ] How do exact formulations (OLSQ2's SMT, SATMap's MaxSAT, Q-Synth's planning/SAT) encode layout synthesis, and at what circuit and device size does each time out?

### Benchmarks and metrics
- [ ] What do QASMBench, MQT Bench, QUEKO, QUBIKOS and Benchpress each test, and which suite best measures routing quality as opposed to layout quality?
- [ ] Which metrics matter for routing (added SWAPs, final two-qubit count, two-qubit depth, compile time, estimated success probability), and when do they disagree?
- [ ] What is a fair comparison protocol for routers (version pinning, seeds, trial or wall-clock budget), and how do published papers break it?
- [ ] How do you obtain real coupling maps (IBM Eagle and Heron, Google Sycamore, Rigetti) for laptop experiments?

### Reproducibility on a laptop
- [ ] Which 2022–2026 routing papers can one student reproduce on a laptop at about 8 h/week, and what headline result can each one reproduce?
- [ ] Can a pure-Python SABRE clone be calibrated to match Qiskit's SabreSwap at SABRE-equivalent settings?
- [ ] Does the QUBIKOS SWAP-optimality gap for LightSABRE reproduce across trial counts (1, 20, 100, 1,000) and Qiskit versions (1.2.4 vs 2.5.x)?
- [ ] Can a small RL routing policy, for example one built on qgym, be trained on a CPU for a 16–20-qubit device, and how does it compare with SABRE?

### Open problems and extensions
- [ ] Does decaying the SABRE lookahead weight with layer distance, as QUBIKOS proposes, reduce the SWAP-optimality gap, and does Qiskit 2.5's layer-based lookahead already do this?
- [ ] How much of SABRE's optimality gap is layout and how much is routing, measured by giving the router the optimal initial mapping?
- [ ] Can exact re-solving of small windows of SABRE output (with Q-Synth) save more SWAPs than spending the same CPU time on extra SABRE trials, and how does it compare with SATMap's hybrid mode?
- [ ] Do published RL-router gains over SABRE (10–20%) survive a comparison against a 1,000-trial LightSABRE with a matched compute budget?
- [ ] How much does commutation-aware routing (2QAN, Qiskit's commuting-2q-gate routing) beat SABRE on QAOA and Hamiltonian-simulation circuits?
- [ ] How do mirror gates (MIRAGE) change the routing cost model on sqrt(iSWAP) gate sets, and does MIRAGE still run on current Qiskit?
- [ ] Why does the heuristic optimality gap grow so much on sparse heavy-hex devices compared with grids?
- [ ] How does routing change for neutral-atom architectures with atom movement (Enola, ZAC, DasAtom)?
