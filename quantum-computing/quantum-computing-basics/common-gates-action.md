---
question: How do the common one- and two-qubit gates (X, H, S, T, Rz, CNOT, CZ, SWAP) act on qubit states?
date: 2026-10-15
status: answered
---

## TL;DR
X flips |0⟩↔|1⟩, H maps |0⟩/|1⟩ to |+⟩/|−⟩, and S, T and Rz only change the relative phase between |0⟩ and |1⟩, which rotates the state about the Bloch sphere's Z axis[^x][^h][^stdlib][^s][^t][^rz]. CNOT flips the target when the control is 1, CZ puts a −1 on |11⟩, and SWAP exchanges two qubits at a cost of three CNOTs[^cx][^cz][^stdgates]. Qiskit labels basis states little-endian, |q1 q0⟩, so its CNOT matrix differs from the textbook one[^order][^cx].

## Explanation

### States and the Bloch sphere
Up to a global phase, every qubit state can be written as cos(θ/2)|0⟩ + e^{iφ} sin(θ/2)|1⟩, which is a point on the Bloch sphere[^bloch]. On that sphere, |0⟩ is the north pole and |1⟩ the south pole[^bloch]. |+⟩ and |−⟩ sit on the equator on the +x and −x axes, and |+i⟩ and |−i⟩ sit on the +y and −y axes[^bloch]. A global phase does not move the point, so two gates that differ only by a global phase look the same on the sphere *(inference)*.

### Single-qubit gates
Matrices are written row by row, as `[[row 0],[row 1]]`.

| Gate | Matrix | On \|0⟩ | On \|1⟩ | Bloch picture | Source |
|---|---|---|---|---|---|
| X | `[[0,1],[1,0]]` | \|1⟩ | \|0⟩ | π rotation about the X axis | [^x][^stdlib] |
| H | `(1/√2)[[1,1],[1,−1]]` | \|+⟩ | \|−⟩ | π rotation about the X+Z axis | [^h][^stdlib] |
| S | `[[1,0],[0,i]]` | \|0⟩ | i\|1⟩ | π/2 rotation about Z | [^s][^stdlib] |
| T | `[[1,0],[0,e^{iπ/4}]]` | \|0⟩ | e^{iπ/4}\|1⟩ | π/4 rotation about Z | [^t][^stdlib] |
| Rz(φ) | `[[e^{−iφ/2},0],[0,e^{iφ/2}]]` | e^{−iφ/2}\|0⟩ | e^{iφ/2}\|1⟩ | rotation about Z | [^rz][^stdlib] |

X is the quantum bit flip[^x]. H changes the basis from |0⟩,|1⟩ to |+⟩,|−⟩ and back[^h]. It is its own inverse, so H|+⟩ = |0⟩ and H|−⟩ = |1⟩[^h][^qi]. Geometrically, a π rotation about the X+Z axis swaps the sphere's Z and X axes, which is why it exchanges the poles with the ±x points *(inference)*. S, T and Rz leave |0⟩ and |1⟩ in place up to a phase, so they move only the azimuth φ of a state and never its height θ on the sphere *(inference)*.

### Relations between the single-qubit gates
- **H X H = Z.** Multiplying the matrices gives this, and H Z H = X as well *(inference: checked by matrix multiplication)*. In words, a bit flip seen through Hadamards is a phase flip *(inference)*.
- **S = T², S² = Z.** OpenQASM 3 defines `s` as `pow(0.5) @ z` and `t` as `pow(0.5) @ s`[^stdgates]. Qiskit calls S a square root of Pauli-Z and T a fourth root[^s][^t].
- **Phase family.** The phase gate is P(θ) = `[[1,0],[0,e^{iθ}]]`[^qi]. S = P(π/2), T = P(π/4), Z = P(π), and the identity I = P(0)[^qi].
- **Rz versus phase gates.** P(φ) = e^{iφ/2} Rz(φ), so Rz equals the phase gate up to a global phase[^rz]. OpenQASM 3 notes that `rz` differs from `p` by a global phase of half the rotation angle[^stdlib]. Hence S ≡ Rz(π/2) and T ≡ Rz(π/4) up to global phase *(inference)*. That phase is harmless on its own, but it is not harmless under control: the global-phase difference makes `cp` and `crz` different gates[^stdlib].

### Qiskit's qubit ordering (little-endian)
By default Qiskit uses little-endian ordering: qubit 0 is the least significant bit[^order]. A label is written with qubit n−1 leftmost and qubit 0 rightmost, so `|01⟩` means q1 = 0 and q0 = 1[^order]. Textbooks usually treat the more significant (leftmost) qubit as the control, so the same CNOT gets a different matrix in a textbook than in Qiskit[^cx]. All two-qubit states below are written in Qiskit's form, |q1 q0⟩.

### Two-qubit gates
Here `cx q0, q1` means control q0 and target q1[^cx]. Matrix rows and columns run over |00⟩, |01⟩, |10⟩, |11⟩ in Qiskit labels.

| Gate | Qiskit matrix | \|00⟩ | \|01⟩ | \|10⟩ | \|11⟩ | Source |
|---|---|---|---|---|---|---|
| CX q0,q1 | `[[1,0,0,0],[0,0,0,1],[0,0,1,0],[0,1,0,0]]` | \|00⟩ | \|11⟩ | \|10⟩ | \|01⟩ | [^cx] |
| CZ | `diag(1,1,1,−1)` | \|00⟩ | \|01⟩ | \|10⟩ | −\|11⟩ | [^cz][^stdlib] |
| SWAP | `[[1,0,0,0],[0,0,1,0],[0,1,0,0],[0,0,0,1]]` | \|00⟩ | \|10⟩ | \|01⟩ | \|11⟩ | [^swap] |

- **CNOT (CX)** flips the target when the control is |1⟩; written control-first (textbook order) it maps |a, b⟩ to |a, a⊕b⟩[^cx]. In Qiskit labels with control q0, that is |q1 q0⟩ → |q1⊕q0, q0⟩ *(inference)*. Its operator is I ⊗ |0⟩⟨0| + X ⊗ |1⟩⟨1|, with q0 as the control[^cx]. The basis-state columns above follow from that matrix *(inference)*. CNOT is not symmetric, so which qubit is the control matters *(inference)*.
- **CZ** puts a −1 phase on |11⟩ and leaves the other three basis states alone[^stdlib][^cz]. Qiskit calls it symmetric[^cz], so control and target are interchangeable and it does not care which way a coupled pair is used *(inference)*.
- **SWAP** maps |a, b⟩ to |b, a⟩ and exchanges the two qubits' states[^swap][^stdlib].

### Two-qubit relations
- **CZ from CNOT.** Qiskit's OpenQASM 2 library defines `gate cz a,b { h b; cx a,b; h b; }`, which is CZ with a Hadamard on each side of the target[^qelib]. In textbook ordering, with the target on the right, this is CZ = (I⊗H) CNOT (I⊗H) *(inference)*. In Qiskit's little-endian matrices, an H on target q1 is written H⊗I instead *(inference: checked by matrix multiplication)*. This is the two-qubit form of H X H = Z *(inference)*.
- **SWAP from three CNOTs.** Both OpenQASM 2 and OpenQASM 3 define `swap a, b { cx a, b; cx b, a; cx a, b; }`, three CNOTs with the middle one pointing the other way[^stdgates][^qelib]. This is why every SWAP a router inserts costs three two-qubit gates *(inference)*.

## Follow-ups
- Why does the global phase between P and Rz stop being ignorable once the gate is controlled (CP vs CRZ)?
- How do Hadamards reverse a CNOT's control and target, and when does a router need that on a directed coupling map?

[^bloch]: [IBM Quantum Learning: Bloch sphere](sources/ibm-learning-bloch-sphere.md)
[^qi]: [IBM Quantum Learning: Single systems, Quantum information](sources/ibm-learning-quantum-information.md)
[^x]: [Qiskit API: XGate](sources/qiskit-xgate.md)
[^h]: [Qiskit API: HGate](sources/qiskit-hgate.md)
[^s]: [Qiskit API: SGate](sources/qiskit-sgate.md)
[^t]: [Qiskit API: TGate](sources/qiskit-tgate.md)
[^rz]: [Qiskit API: RZGate](sources/qiskit-rzgate.md)
[^cx]: [Qiskit API: CXGate](sources/qiskit-cxgate.md)
[^cz]: [Qiskit API: CZGate](sources/qiskit-czgate.md)
[^swap]: [Qiskit API: SwapGate](sources/qiskit-swapgate.md)
[^order]: [Qiskit guide: Bit ordering](sources/qiskit-bit-ordering.md)
[^stdlib]: [OpenQASM 3 spec: Standard library](sources/openqasm3-standard-library.md)
[^stdgates]: [OpenQASM 3 stdgates.inc](sources/openqasm3-stdgates-inc.md)
[^qelib]: [Qiskit's OpenQASM 2 qelib1.inc](sources/qiskit-qelib1-inc.md)
