# Qiskit source: crates/circuit/src/dag_circuit.rs (stable/2.5)

Rust source of DAGCircuit in Qiskit 2.5: add_wire creates an in/out node pair joined by one edge per qubit, clbit or var; new operations are put between the last node on each wire and the wire's out node; multigraph_layers starts from every input node; front_layer takes the op nodes of the second multigraph layer; depth is the longest path length minus one; remove_op_node reconnects predecessors to successors only along the same wire.

- URL: <https://github.com/Qiskit/qiskit/blob/stable/2.5/crates/circuit/src/dag_circuit.rs>
- Fetched: 2026-10-25
