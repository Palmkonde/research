# Quantum computing basics
Fundamentals of quantum computing: qubit states, gates, circuits and a first algorithm. The last group covers what qubit routing needs from the circuit model. A quantum program is a circuit: a sequence of one- and two-qubit gates applied to qubits, usually written in OpenQASM. Gates on the same qubits must run in order, so a circuit forms a dependency graph (DAG) whose front layer holds the gates ready to run. Real hardware runs only a small native gate set, and its two-qubit gates work only on coupled qubit pairs given by the device's coupling map. A SWAP gate exchanges two qubits' states and costs three CNOTs, which is why routers try to add as few as possible.

## Questions
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
- [ ] How does Qiskit's commutation-aware `DAGDependency` differ from `DAGCircuit`, and how do commutation-analysis passes use it?
- [ ] How does a control-flow operation (`if_else`, `for_loop`) appear in a `DAGCircuit`, and how does `depth(recurse=True)` count it?
- [ ] How does a transpiler pass read and rewrite a `DAGCircuit` (for example with `substitute_node_with_dag`)?
- [ ] How does Qiskit's `SabreSwap` build its own DAG and front layer from a `DAGCircuit`, and does it set single-qubit gates aside as the 2019 paper does?
