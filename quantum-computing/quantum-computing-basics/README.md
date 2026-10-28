# Quantum computing basics
Fundamentals of quantum computing: qubit states, gates, circuits and a first algorithm. The last group covers what qubit routing needs from the circuit model. A quantum program is a circuit: a sequence of one- and two-qubit gates applied to qubits, usually written in OpenQASM. Gates on the same qubits must run in order, so a circuit forms a dependency graph (DAG) whose front layer holds the gates ready to run. Real hardware runs only a small native gate set, and its two-qubit gates work only on coupled qubit pairs given by the device's coupling map. A SWAP gate exchanges two qubits' states and costs three CNOTs, which is why routers try to add as few as possible.

## Prerequisites
- [Linear algebra](../../fundamentals/linear-algebra/README.md)

## Questions
- [x] [Why is a qubit, and a superposition, represented as a vector?](qubit-state-as-vector.md)
- [x] [Which mathematical objects can represent a qubit's state, and when should each be used?](qubit-state-representations.md)
- [x] [How do the common one- and two-qubit gates (X, H, S, T, Rz, CNOT, CZ, SWAP) act on qubit states?](common-gates-action.md)
- [x] [How is a quantum circuit drawn, written in OpenQASM, and loaded and run in Qiskit?](quantum-circuit-openqasm-qiskit.md)
- [x] [How does a circuit become a DAG, and what are its layers and front layer?](circuit-dag-layers.md)
- [ ] What is a coupling map, and what do real device topologies (heavy-hex, grid) look like?
- [ ] What is a native gate set, and how do SWAP and other two-qubit gates decompose into native gates?
- [ ] Why does each extra two-qubit gate lower a circuit's success probability on noisy hardware?
- [ ] Why does the global phase between P and Rz stop being ignorable once the gate is controlled (CP vs CRZ)?
- [ ] How do Hadamards reverse a CNOT's control and target, and when does a router need that on a directed coupling map?
- [ ] What does transpiling to an ISA circuit with `generate_preset_pass_manager` change in a circuit, stage by stage?
- [ ] How do mid-circuit measurement and classical feed-forward (`if (c[0]) ...`) work in OpenQASM 3, Qiskit and PennyLane?
- [ ] Why does PennyLane's `from_qasm3` reject `include "stdgates.inc"` and register wire maps, and is that fixed in a newer release?
- [ ] Why are quantum amplitudes complex rather than real, and could quantum theory work with real amplitudes only?
- [ ] Why must quantum evolution be linear, and what would a nonlinear evolution break?
- [ ] How do noise channels such as dephasing and amplitude damping move a qubit's Bloch vector inside the ball?
- [ ] How does a stabilizer tableau store an $n$-qubit stabilizer state, and how do H, S and CNOT update it?
- [ ] How is a qubit's density matrix reconstructed from measurement data (state tomography)?
