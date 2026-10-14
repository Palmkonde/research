---
question: Why does the no-cloning theorem hold?
date: 2026-10-14
status: answered
---

## TL;DR
No quantum operation can copy an arbitrary unknown state. Copying, as a unitary, would have to preserve inner products, but a copy squares them, and x = x² has only the solutions 0 and 1. So only mutually orthogonal (or identical) states can be copied by one device.

## Explanation
Wootters and Zurek asked whether some process, such as stimulated emission of a photon, can produce several copies of an unknown quantum state, and answered that the linearity of quantum mechanics forbids it for all quantum systems.[^wz82]

The same result has a short proof in terms of unitaries. Suppose a unitary U maps |ψ⟩|s⟩ to |ψ⟩|ψ⟩ and |φ⟩|s⟩ to |φ⟩|φ⟩, where |s⟩ is a fixed blank state.[^pl-teleport]
- Unitaries preserve inner products, so the inner product of the two outputs equals the inner product of the two inputs, which is ⟨ψ|φ⟩ because ⟨s|s⟩ = 1.[^pl-teleport]
- Directly, the inner product of the two outputs is ⟨ψ|φ⟩².[^pl-teleport]
- Setting x = ⟨ψ|φ⟩ gives x = x², so x is 0 or 1: the two states are either orthogonal or identical, so no single U copies arbitrary states.[^pl-teleport]

The linearity version can be seen on one qubit. If U copies |0⟩ and |1⟩, linearity forces U(α|0⟩ + β|1⟩)|s⟩ = α|00⟩ + β|11⟩, but a true copy would be (α|0⟩ + β|1⟩)⊗(α|0⟩ + β|1⟩), which also contains cross terms αβ|01⟩ and βα|10⟩. These agree only if αβ = 0. *(inference)*

For α = β = 1/√2, the linear result α|00⟩ + β|11⟩ is the Bell state from H then CNOT: the "copy" the circuit makes is an entangled pair, not two independent copies. *(inference)*

The classical case is not forbidden: a device that copies only states known to be orthogonal, such as |0⟩ and |1⟩, exists, and a CNOT does that job, which is why classical bits can be copied. *(inference)*

For routing, this is why a router moves a qubit with SWAP (exchange the states) and never by copying the state to a neighbor. *(inference)*

The Nature letter's full text was not accessible, so the physical argument (stimulated emission, signalling) is only as detailed as its abstract.[^wz82]

## Follow-ups
- How does the no-cloning theorem relate to quantum teleportation, which moves a state without copying it?
- Which approximate or probabilistic cloning machines exist, and how close to a perfect copy can they get?
- What does no-cloning imply for quantum error correction, given that a code cannot just copy a state three times?

[^wz82]: [Wootters & Zurek 1982](sources/wootters-zurek-1982.md)
[^pl-teleport]: [PennyLane: Quantum Teleportation](sources/pennylane-quantum-teleportation.md)
