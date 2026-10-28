---
question: Why is a qubit, and a superposition, represented as a vector?
date: 2026-10-27
status: answered
---

## TL;DR
Quantum mechanics takes as an axiom that a state is a unit vector (up to phase) in a complex Hilbert space, so a qubit is $\alpha\lvert 0\rangle + \beta\lvert 1\rangle$ with $\lvert\alpha\rvert^2 + \lvert\beta\rvert^2 = 1$[^preskill]. A vector fits because a superposition is a linear combination of states[^preskill], and the entries must be amplitudes rather than probabilities because states with the same probabilities, such as $\lvert +\rangle$ and $\lvert -\rangle$, still behave differently[^qi]. The unit length makes the Born-rule probabilities sum to 1[^qi], and gates act on it as unitary matrices, which keep it a unit vector[^qi].

## Explanation
Every other page in this Topic writes states as kets and gates as matrices, and this page explains why that is the right language *(inference)*. The short answer is that it is an axiom: Preskill states the theory as five axioms and notes that they account for all that is currently known about quantum physics[^preskill]. The rest of the page shows which part of the axiom does which job: the vector space, the amplitudes, the unit length and the phase *(inference)*.

### The state-space axiom
Preskill's first axiom says that a state is a complete description of a physical system, and that in quantum mechanics a state is a ray in a Hilbert space[^preskill]. A Hilbert space is a vector space over the complex numbers with an inner product $\langle\psi\vert\phi\rangle$[^preskill]. Every unit vector in that space is a possible pure state of the system[^sep].

A qubit is the smallest case, a system whose Hilbert space is two-dimensional[^preskill]. With an orthonormal basis $\lvert 0\rangle, \lvert 1\rangle$, the most general normalized state is

$$\lvert\psi\rangle = \alpha\lvert 0\rangle + \beta\lvert 1\rangle, \qquad \alpha, \beta \in \mathbb{C}, \quad \lvert\alpha\rvert^2 + \lvert\beta\rvert^2 = 1,$$

and its overall phase is physically irrelevant[^preskill]. IBM writes the basis states as the column vectors $\lvert 0\rangle = \begin{pmatrix}1\\0\end{pmatrix}$ and $\lvert 1\rangle = \begin{pmatrix}0\\1\end{pmatrix}$[^qi]. So the qubit state is just the column of its two amplitudes, $\lvert\psi\rangle = \begin{pmatrix}\alpha\\\beta\end{pmatrix}$ *(inference)*. In IBM's words, the entries of a quantum state vector are complex numbers, and the vector is a unit vector in the Euclidean norm[^qi].

### Why a vector: superposition is a linear combination
Given two states $\lvert\phi\rangle$ and $\lvert\psi\rangle$, the linear superposition $a\lvert\phi\rangle + b\lvert\psi\rangle$ is again a possible state[^preskill]. Adding states and scaling them by numbers, with the result still a state, is exactly what a vector space allows, since vector addition maps any pair of vectors onto another vector[^sep]. So "superposition" is not an extra rule laid on top of the vectors; it is the vector-space structure itself *(inference)*.

Time evolution respects the same structure: operators are linear maps, $A(a\lvert\psi\rangle + b\lvert\phi\rangle) = aA\lvert\psi\rangle + bA\lvert\phi\rangle$, and the Schrödinger equation is linear[^preskill]. Because a gate is linear, it is fixed by what it does to $\lvert 0\rangle$ and $\lvert 1\rangle$, which is why every one-qubit gate in [the gates Finding](common-gates-action.md) is a $2\times 2$ matrix *(inference)*.

### Why not a list of probabilities
A classical random bit is already described by a vector *(inference)*. IBM represents a probabilistic classical state as a column vector whose entries are nonnegative reals summing to 1, a probability vector[^ci]. A random operation is a stochastic matrix, whose entries are nonnegative and whose columns each sum to 1, and it acts on the probability vector by matrix multiplication[^ci]. So the question is not "why a vector" but "why this kind of vector" *(inference)*.

The quantum version changes three things *(inference)*. Its entries need not be nonnegative reals[^qi]. A measurement gives each outcome with probability equal to the absolute value squared of the matching entry[^qi]. And its operations are unitary matrices instead of stochastic ones[^qi].

The entries cannot just be probabilities, because two states with the same probabilities can still behave differently *(inference)*. Measuring $\lvert +\rangle$ or $\lvert -\rangle$ gives 0 and 1 with probability $1/2$ each, so a measurement says nothing about which was prepared[^qi]. Yet applying a Hadamard first sends $\lvert +\rangle$ to $\lvert 0\rangle$ and $\lvert -\rangle$ to $\lvert 1\rangle$, so the two states can be told apart perfectly[^qi]. Their probability vectors are both $(1/2, 1/2)$, so the difference lives only in the sign of the $\lvert 1\rangle$ amplitude *(inference)*. Preskill makes the same point with spins: reasoning about probabilistic classical bits predicts a 50/50 result, but the state $\tfrac{1}{\sqrt2}(\lvert\uparrow_x\rangle + \lvert\downarrow_x\rangle)$ is "really $\lvert\uparrow_z\rangle$ in disguise" and always gives up[^preskill]. He calls this way that probabilities add unexpectedly "quantum interference"[^preskill].

Preskill's three-analyzer setup shows the same interference with light[^preskill]. An $x$-polarized photon never passes a $y$ analyzer, yet putting a $45^\circ$ analyzer between the $x$ and $y$ ones lets about one photon in eight through all three[^preskill]. Because of this interference, no consistent picture has each photon carrying one classical bit of polarization[^preskill].

### Example: two Hadamards on $\lvert 0\rangle$
Take the Hadamard $H = \tfrac{1}{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix}$, with $H\lvert 0\rangle = \lvert +\rangle$ and $H\lvert +\rangle = \lvert 0\rangle$[^qi]. As column vectors *(inference: from IBM's column forms of $\lvert 0\rangle, \lvert 1\rangle$ and $H\lvert 0\rangle = \lvert +\rangle$[^qi])*:

$$\begin{pmatrix}1\\0\end{pmatrix} \xrightarrow{\;H\;} \begin{pmatrix}\tfrac{1}{\sqrt2}\\[2pt] \tfrac{1}{\sqrt2}\end{pmatrix} \xrightarrow{\;H\;} \begin{pmatrix}1\\0\end{pmatrix}.$$

For comparison, take the classical "fair coin" operation $C = \begin{pmatrix}\tfrac12&\tfrac12\\[2pt] \tfrac12&\tfrac12\end{pmatrix}$, which resets the bit to 0 or 1 with probability $1/2$ each *(inference: it meets IBM's definition of a stochastic matrix[^ci])*. After one step, $C$ and $H$ give the same measurement statistics, $1/2$ and $1/2$ *(inference: checked by matrix multiplication)*. After two steps they differ: $C^2$ still gives $(1/2, 1/2)$, but $H^2$ gives $\lvert 0\rangle$ with certainty *(inference: checked by matrix multiplication)*.

Splitting the two steps into paths shows why *(inference)*. Each path multiplies one matrix entry from each step, and the paths that end in the same state are added *(inference)*:

| Path | Classical $C$: probability | Quantum $H$: amplitude |
|---|---|---|
| $0 \to 0 \to 0$ | $\tfrac12\cdot\tfrac12 = \tfrac14$ | $\tfrac{1}{\sqrt2}\cdot\tfrac{1}{\sqrt2} = +\tfrac12$ |
| $0 \to 1 \to 0$ | $\tfrac12\cdot\tfrac12 = \tfrac14$ | $\tfrac{1}{\sqrt2}\cdot\tfrac{1}{\sqrt2} = +\tfrac12$ |
| total for $0$ | $\tfrac12$ | $+1$, probability $1$ |
| $0 \to 0 \to 1$ | $\tfrac12\cdot\tfrac12 = \tfrac14$ | $\tfrac{1}{\sqrt2}\cdot\tfrac{1}{\sqrt2} = +\tfrac12$ |
| $0 \to 1 \to 1$ | $\tfrac12\cdot\tfrac12 = \tfrac14$ | $\tfrac{1}{\sqrt2}\cdot\big({-\tfrac{1}{\sqrt2}}\big) = -\tfrac12$ |
| total for $1$ | $\tfrac12$ | $0$, probability $0$ |

Classical probabilities are nonnegative, so paths can only add up *(inference)*. The $-1$ in the corner of $H$ makes the two paths into $\lvert 1\rangle$ cancel, while the paths into $\lvert 0\rangle$ reinforce *(inference)*. A description that stores only the probabilities after the first $H$, $(1/2, 1/2)$, has thrown away that sign and cannot predict this *(inference)*. This is Preskill's "$\lvert\uparrow_z\rangle$ in disguise" example in qubit notation, with $\lvert 0\rangle, \lvert 1\rangle$ as spin up and down along $z$[^preskill].

### Why unit length
The Born rule turns amplitudes into probabilities: measuring $\alpha\lvert 0\rangle + \beta\lvert 1\rangle$ gives $0$ with probability $\lvert\alpha\rvert^2$ and $1$ with probability $\lvert\beta\rvert^2$[^preskill][^qi]. More generally, measuring in a basis that contains $\lvert a\rangle$ gives that outcome with probability $\lvert\langle a\vert\psi\rangle\rvert^2$[^preskill][^sep]. Since the probabilities of all outcomes must sum to 1, the squared lengths of the entries must sum to 1, so the vector has length 1 *(inference)*. IBM states this as the condition that the absolute values squared of the entries sum to 1[^qi].

### Why the global phase does not count, and the Bloch sphere
A ray is the set of vectors that differ by a nonzero complex factor, so $\lvert\psi\rangle$ and $e^{i\gamma}\lvert\psi\rangle$ describe the same state[^preskill]. The relative phase inside a superposition does count: $a\lvert\phi\rangle + b\lvert\psi\rangle$ is the same state as $e^{i\gamma}(a\lvert\phi\rangle + b\lvert\psi\rangle)$ but not as $a\lvert\phi\rangle + e^{i\gamma}b\lvert\psi\rangle$[^preskill]. IBM likewise notes that changing the sign or phase of an entry can change the state significantly[^qi]; $\lvert +\rangle$ and $\lvert -\rangle$ above differ only in that way *(inference)*.

Two complex numbers carry four real numbers *(inference)*. Normalization and the irrelevant overall phase remove two, and the two real numbers left are the polar angle $\theta$ and azimuth $\varphi$ of a direction in space[^preskill]. That direction is the qubit's point on the Bloch sphere[^bloch].

![Bloch sphere with ket 0 at the top, ket 1 at the bottom, and a state psi at polar angle theta and azimuth phi](assets/common-gates-action/bloch-sphere.svg)
*Figure: the Bloch sphere, with $\lvert 0\rangle$ on $+\hat z$, $\lvert 1\rangle$ on $-\hat z$, and a state $\lvert\psi\rangle$ at polar angle $\theta$ and azimuth $\varphi$[^bloch]. The two angles are the two real numbers left after normalization and global phase are removed[^preskill]. Image by Glosser.ca, CC BY-SA 3.0[^wm-bloch].*

Complex entries are needed to reach the whole sphere *(inference)*. The state $\lvert {+i}\rangle$ on the $+y$ axis has the imaginary amplitude $i/\sqrt2$ on $\lvert 1\rangle$[^bloch], and the circular polarization state of a photon is $\lvert R\rangle = \tfrac{1}{\sqrt2}\begin{pmatrix}1\\ i\end{pmatrix}$[^preskill]. With real amplitudes only, a qubit could reach only the great circle through $\lvert 0\rangle$, $\lvert +\rangle$, $\lvert 1\rangle$ and $\lvert -\rangle$ *(inference)*. The sources read here state that amplitudes are complex but do not argue why nature needs complex rather than real numbers; that question is left as a Follow-up *(inference)*.

### What the vector picture buys
- **Gates are matrices.** Operations on quantum state vectors are unitary matrices, and multiplying a unitary matrix by a state vector gives another state vector[^qi]. The time evolution of a closed system is unitary[^preskill]. The matrices of $X$, $H$, $S$, $T$, $R_z$, CNOT, CZ and SWAP are in [the gates Finding](common-gates-action.md) *(inference)*.
- **Probabilities and overlaps are inner products.** Outcome probabilities are $\lvert\langle a\vert\psi\rangle\rvert^2$[^preskill]. Unitaries preserve inner products[^pl-teleport], and that fact is the key step in the proof of [the no-cloning theorem](no-cloning-theorem.md) *(inference)*.
- **Many qubits use a tensor product.** The Hilbert space of a composite system is the tensor product of its parts' spaces, and independent preparations give the product state $\lvert\psi\rangle_A \otimes \lvert\phi\rangle_B$[^preskill][^sep]. The entries of a multi-system state vector are indexed by the Cartesian product of the classical state sets[^ms]. For $n$ qubits that set has $2^n$ elements, so the state vector has $2^n$ complex entries, which is what a state-vector simulator must store (see [quantum circuit simulation](../quantum-circuit-simulation/README.md)) *(inference)*. Not every such vector is a product of one-qubit vectors; those that are not are entangled[^ms].

### Beyond unit vectors: density matrices
The unit-vector description is for a closed system; once only part of a larger system is observed, states are no longer rays[^preskill]. A subsystem is then described by a density operator $\rho$, which is self-adjoint, positive and has unit trace[^preskill]. It separates a coherent superposition from a coin-flip mixture: measuring $\sigma_1$ on $\tfrac{1}{\sqrt2}(\lvert\uparrow_z\rangle + \lvert\downarrow_z\rangle)$ gives $\lvert\uparrow_x\rangle$ with probability one, while the 50/50 mixture $\rho = \tfrac12 I$ gives $1/2$ along every axis[^preskill]. A pure state's density matrix $\lvert\psi\rangle\langle\psi\rvert$ has no global-phase ambiguity, and the single-qubit density matrices fill the Bloch ball, with pure states on its surface[^preskill]. [Which objects can represent a qubit's state](qubit-state-representations.md) compares the vector, the ray, the Bloch vector and the density matrix side by side *(inference)*.

## Follow-ups
- Why are quantum amplitudes complex rather than real, and could quantum theory work with real amplitudes only?
- Why must quantum evolution be linear, and what would a nonlinear evolution break?
- Mixed states and the Bloch ball are covered in [Which objects can represent a qubit's state](qubit-state-representations.md); how noise moves a state inside the ball is open there.

[^preskill]: [Preskill: Ph219 lecture notes, Chapter 2](sources/preskill-ph219-chapter-2.md)
[^sep]: [Stanford Encyclopedia of Philosophy: Quantum Mechanics](sources/sep-quantum-mechanics.md)
[^qi]: [IBM Quantum Learning: Single systems, Quantum information](sources/ibm-learning-quantum-information.md)
[^ci]: [IBM Quantum Learning: Single systems, Classical information](sources/ibm-learning-classical-information.md)
[^ms]: [IBM Quantum Learning: Multiple systems, Quantum information](sources/ibm-learning-multiple-systems-quantum-information.md)
[^bloch]: [IBM Quantum Learning: Bloch sphere](sources/ibm-learning-bloch-sphere.md)
[^wm-bloch]: [Wikimedia Commons: Bloch Sphere.svg](sources/wikimedia-bloch-sphere-svg.md)
[^pl-teleport]: [PennyLane: Quantum Teleportation](sources/pennylane-quantum-teleportation.md)
