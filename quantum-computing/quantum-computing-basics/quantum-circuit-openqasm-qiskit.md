---
question: How is a quantum circuit drawn, written in OpenQASM, and loaded and run in Qiskit?
date: 2026-10-19
status: answered
---

## TL;DR
A circuit diagram has one wire per qubit, read left to right, with gates as boxes, a CNOT as a control dot joined to a ⊕ target, and measurements written onto double-line classical bits[^circ]. In OpenQASM 3 the Bell circuit is `OPENQASM 3.0; include "stdgates.inc"; qubit[2] q; bit[2] c; h q[0]; cx q[0], q[1]; c = measure q;`[^ver][^types][^insts]. Qiskit 2.5 loads it with `qasm3.loads`, draws it with `draw()` and samples it with `StatevectorSampler`[^qasm3][^qc][^svs]. PennyLane 0.45 builds it as a QNode with `qp.draw` and `qp.counts`, and loads QASM with `qp.from_qasm3` or, through pennylane-qiskit, `qp.from_qasm`[^draw][^counts][^fq3][^fq]. In 0.45.1, `from_qasm3` worked only without the `include` line *(inference: ran with pennylane 0.45.1)*.

## Explanation

Versions: the Qiskit pages describe Qiskit 2.5, and the guides were written against `qiskit[all]~=2.5.2`[^qasm3][^pio][^hello]. The PennyLane pages describe PennyLane 0.45.1[^fq3]. The code below was run with qiskit 2.5.2, qiskit-qasm3-import 0.6.0, pennylane 0.45.1 and Python 3.12 *(inference: ran in a scratch venv)*.

Running example: the Bell state |φ+⟩ = (|00⟩ + |11⟩)/√2, made by an H on one qubit followed by a CNOT from that qubit to the other[^circ].

### 1. Reading a circuit diagram
- **Wires are qubits.** In the circuit model, wires represent qubits and gates represent operations on them[^circ].
- **Time runs left to right.** Information flows from left to right, so the leftmost gate is applied first[^circ]. A circuit whose gates read H, S, H, T from left to right applies the matrix product T·H·S·H, which is written right to left[^circ].
- **Start state.** Circuits usually start with every qubit in |0⟩[^circ].
- **Gates are boxes.** A one-qubit gate is a box with its name, such as H[^circ].
- **CNOT.** The solid dot marks the control qubit and the ⊕ marks the target[^circ].
- **Measurement.** Classical bits are drawn as double lines[^circ]. A measurement box writes its outcome onto the classical bit its arrow points to[^circ].
- **Qubit order in Qiskit.** In Qiskit the top wire is q0, and q0 is the rightmost character of a bitstring[^circ][^order].

Qiskit's default text drawer prints this for the Bell circuit with two measurements *(inference: ran with qiskit 2.5.2)*:

```
     ┌───┐     ┌─┐
q_0: ┤ H ├──■──┤M├───
     └───┘┌─┴─┐└╥┘┌─┐
q_1: ─────┤ X ├─╫─┤M├
          └───┘ ║ └╥┘
c: 2/═══════════╩══╩═
                0  1
```

In this ASCII form the CNOT target is drawn as a boxed `X` under the `■` control *(inference: ran with qiskit 2.5.2)*. `M` is a measurement, and `╩` with a number shows which bit of the classical register `c` receives the result *(inference: ran with qiskit 2.5.2)*. `draw("mpl")` draws the same circuit with a ⊕ target and meter symbols, and it needs the extra package `pylatexenc` *(inference: ran with qiskit 2.5.2)*.

### 2. Writing it in OpenQASM 3
```qasm
OPENQASM 3.0;
include "stdgates.inc";
qubit[2] q;
bit[2] c;
h q[0];
cx q[0], q[1];
c = measure q;
```
- **Version line.** `OPENQASM 3.0;` is optional[^ver]. If present, it must be the first non-comment line and appear only once[^ver].
- **Gate library.** `include "stdgates.inc";` pulls in the standard gate library, which is where `h` and `cx` are defined[^ver][^stdgates].
- **Declarations.** `qubit[2] q;` declares a two-qubit register, and `bit[2] c;` declares a two-bit classical register[^types].
- **Gates.** A gate statement names the gate and then its qubits *(inference: from the example programs)*. `cx q[0], q[1];` has control `q[0]` and target `q[1]`[^stdgates].
- **Measurement.** `c = measure q;` measures in the Z basis[^insts]. Because both sides are registers of the same size, it broadcasts to `c[j] = measure q[j];` for each j[^insts]. It is equivalent to the older form `measure q -> c;`[^insts].

**OpenQASM 2 differences.** The same circuit in OpenQASM 2 is[^qasm2]:

```qasm
OPENQASM 2.0;
include "qelib1.inc";
qreg q[2];
creg c[2];
h q[0];
cx q[0],q[1];
measure q[0] -> c[0];
measure q[1] -> c[1];
```
This is the output shown on Qiskit's `qasm2` page[^qasm2]. OpenQASM 2 uses `qelib1.inc` instead of `stdgates.inc`[^qasm2][^qelib], `qreg`/`creg` instead of `qubit[]`/`bit[]`, and the arrow form of `measure`. OpenQASM 3 still accepts `qreg` and `creg` for backwards compatibility, but says they may be removed[^types].

### 3. Qiskit: build, draw, export, load, run

**Build and draw.**
```python
from qiskit import QuantumCircuit

qc = QuantumCircuit(2, 2)      # 2 qubits, 2 classical bits
qc.h(0)
qc.cx(0, 1)                    # control 0, target 1
qc.measure([0, 1], [0, 1])     # qubit i -> bit i
print(qc.draw())               # text drawer by default
```
`QuantumCircuit(4, 3)` means 4 qubits and 3 classical bits[^qc]. `draw()` accepts `output="text"`, `"mpl"`, `"latex"` or `"latex_source"`[^qc]. It uses the text drawer unless `~/.qiskit/settings.conf` sets another default[^qc]. Without classical bits, `qc.measure_all()` adds a new classical register and measures every qubit into it[^qc]. That register is named `meas`[^pio], and the drawing shows a barrier before the measurements *(inference: ran with qiskit 2.5.2)*.

**Export to OpenQASM.**
```python
from qiskit import qasm2, qasm3

print(qasm3.dumps(qc))   # OpenQASM 3 string
print(qasm2.dumps(qc))   # OpenQASM 2 string
```
`qasm3.dumps` serialises a `QuantumCircuit` to an OpenQASM 3 string, and `qasm3.dump` writes to a file-like stream[^qasm3]. `qasm2.dumps` exports OpenQASM 2[^qasm2]. For the circuit above, `qasm3.dumps` printed this *(inference: ran with qiskit 2.5.2)*:

```qasm
OPENQASM 3.0;
include "stdgates.inc";
bit[2] c;
qubit[2] q;
h q[0];
cx q[0], q[1];
c[0] = measure q[0];
c[1] = measure q[1];
```
The exporter declares `bit` before `qubit` and writes one `measure` per bit rather than `c = measure q;` *(inference: ran with qiskit 2.5.2)*. The two forms mean the same thing *(inference: ran with qiskit 2.5.2; equivalence per [^insts])*.

**Load OpenQASM.**
```python
from qiskit import qasm2, qasm3

prog3 = """
OPENQASM 3.0;
include "stdgates.inc";
qubit[2] q;
bit[2] c;
h q[0];
cx q[0], q[1];
c = measure q;
"""
qc3 = qasm3.loads(prog3)       # needs: pip install "qiskit[qasm3-import]"
print(qc3.draw())

prog2 = 'OPENQASM 2.0;\ninclude "qelib1.inc";\nqreg q[2];\ncreg c[2];\nh q[0];\ncx q[0],q[1];\nmeasure q -> c;\n'
qc2 = qasm2.loads(prog2)
```
`qasm3.loads` reads a string and `qasm3.load` reads a file[^qasm3]. Both need the `qiskit_qasm3_import` package, which the extra `qiskit[qasm3-import]` installs[^qasm3]. `qasm3.loads` also takes `num_qubits=` to widen the circuit to a backend's size[^qasm3]. Qiskit also ships a native Rust parser, `qasm3.loads_experimental`, that needs no extra package[^qasm3]. It is usually much faster, supports fewer features, and issues an `ExperimentalWarning`[^qasm3]. `qasm2.loads` is built in[^qasm2]. By default it searches only the current directory for includes, but it always finds `qelib1.inc`[^qasm2]. Both loaders gave the same drawing as the hand-built circuit, and the loaded QASM 3 circuit kept the register name `c` *(inference: ran with qiskit 2.5.2)*.

**Run locally and read counts.**
```python
from qiskit.primitives import StatevectorSampler

sampler = StatevectorSampler(seed=42)
result = sampler.run([qc3], shots=1000).result()
print(result[0].data.c.get_counts())     # register named c
# {'11': 497, '00': 503}
```
`StatevectorSampler` is the built-in SamplerV2[^svs]. It simulates the full state vector, defaults to 1024 shots, and accepts a seed[^svs]. It cannot handle mid-circuit measurements[^svs]. `run()` takes a list of PUBs, which are circuits with optional parameter values and shots[^svs]. Each classical register becomes an attribute of `result[i].data` holding a `BitArray`, which has `get_counts()` and `get_bitstrings()`[^svs][^pio]. A circuit built with `measure_all()` is read as `result[0].data.meas.get_counts()`[^pio]. The seed-42 run printed `{'11': 497, '00': 503}`, so only the two correlated outcomes appear, at about 50% each *(inference: ran with qiskit 2.5.2)*. On a lone `X` on q0 the sampler returns `'01'`, which confirms that q0 is the rightmost bit[^order] *(inference: ran with qiskit 2.5.2)*.

**Run on IBM hardware (from the docs, not run here).**
```python
from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2 as Sampler
from qiskit.transpiler import generate_preset_pass_manager

service = QiskitRuntimeService()
backend = service.least_busy(simulator=False, operational=True)
pm = generate_preset_pass_manager(backend=backend, optimization_level=1)
isa_circuit = pm.run(qc3)                     # map to the device's gates and qubits
job = Sampler(mode=backend).run([isa_circuit], shots=1000)
print(job.result()[0].data.c.get_counts())
```
The hardware path is `pip install qiskit-ibm-runtime`, saving an account, picking a backend with `least_busy`, and transpiling to an ISA circuit with `generate_preset_pass_manager` before running a primitive[^hello]. That guide lists qiskit-ibm-runtime ~=0.47.0 in its requirements[^hello]. Its code comments call the top-level `qiskit_ibm_runtime` primitives "legacy server-side" ones, used before qiskit-ibm-runtime 0.50.0[^hello]. They also say client-side primitives were introduced in 0.50.0[^hello]. For the Sampler, the client-side version is `qiskit_ibm_runtime.executor_sampler.Sampler`, and `SamplerV2` there is an alias of it[^execsampler]. The block above uses the legacy top-level `SamplerV2(mode=..., options=...)`[^rtsampler]. Like `StatevectorSampler`, it follows the V2 sampler interface, so results are read per classical register in the same way[^rtsampler][^pio]. The guide shows this flow with the Estimator[^hello]. The Sampler lines above put together these documented pieces and were not run *(inference)*. The transpile step is where qubit routing happens, which is the subject of this Topic's later Questions *(inference)*.

### 4. PennyLane: the same Bell circuit
The PennyLane 0.45.0 docs and source changed the conventional alias from `import pennylane as qml` to `import pennylane as qp`[^plrn]. Both are the same module under a different name *(inference)*.

**Build, draw and run.**
```python
import pennylane as qp

dev = qp.device("default.qubit", wires=2, seed=42)

@qp.set_shots(1000)
@qp.qnode(dev)
def bell():
    qp.Hadamard(wires=0)
    qp.CNOT(wires=[0, 1])        # control 0, target 1
    return qp.counts()

print(qp.draw(bell)())
# 0: ──H─╭●─┤  Counts
# 1: ────╰X─┤  Counts
print(bell())
# {'00': 503, '11': 497}   (printed with np.str_/np.int64 wrappers)

@qp.qnode(dev)                   # no shots: exact (analytic) mode
def bell_probs():
    qp.Hadamard(wires=0)
    qp.CNOT(wires=[0, 1])
    return qp.probs(wires=[0, 1])

print(bell_probs())              # [0.5 0.  0.  0.5]
fig, ax = qp.draw_mpl(bell_probs)()
```
- **Device.** `default.qubit` is PennyLane's Python simulator device, and `seed` fixes its sampling[^dq].
- **Drawing.** `qp.draw(qnode)` returns a function with the QNode's signature that prints the circuit, wires top to bottom in device order[^draw]. In its text output a CNOT is `╭●` on the control and `╰X` on the target *(inference: ran with pennylane 0.45.1)*. `qp.draw_mpl` returns a matplotlib `(Figure, Axes)` pair[^drawmpl], and it draws the CNOT target as ⊕ *(inference: ran with pennylane 0.45.1)*.
- **Shots.** Shots are set with the `qp.set_shots` decorator or transform[^shots]. `None` means analytic mode and an integer means that many shots[^shots]. PennyLane 0.43.0 deprecated passing `shots=` to `qp.device(...)` or to a QNode call[^plrn].
- **Counts and probabilities.** `qp.counts()` returns a dictionary of observed basis-state bitstrings, and `all_outcomes=True` adds the zero-count outcomes[^counts]. `qp.probs(wires=...)` returns probabilities in lexicographic order of the listed wires[^probs].
- **Measurement.** Measurement is the QNode's return value, so the circuit needs no classical register *(inference)*.

**Bit order differs from Qiskit.** PennyLane puts wire 0 at the left of a bitstring[^counts][^probs]. In its docs, `X(0)` gives counts `{'10': 4}`[^counts], and `Hadamard(wires=1)` gives `probs` `[0.5, 0.5, 0, 0]` over `|00⟩, |01⟩`[^probs]. Qiskit puts q0 on the right, so the same one-qubit flip prints `'01'` there[^order]. The Bell counts `00`/`11` look the same in both frameworks only because the state is symmetric *(inference)*.

**Loading OpenQASM 3: `qp.from_qasm3`.**
```python
prog3_pl = """
OPENQASM 3.0;
qubit q0;
qubit q1;
h q0;
cx q0, q1;
"""

@qp.set_shots(1000)
@qp.qnode(dev)
def bell_from_qasm3():
    qp.from_qasm3(prog3_pl, {"q0": 0, "q1": 1})()   # note the trailing ()
    return qp.counts()
# 0: ──H─╭●─┤  Counts
# 1: ────╰X─┤  Counts
# {'00': 505, '11': 495}
```
`qp.from_qasm3(quantum_circuit, wire_map=None)` turns an OpenQASM 3.0 string into a quantum function to call inside a QNode[^fq3]. It needs the `openqasm3` and `openqasm3[parser]` packages[^fq3]. Its docs list standard library gates, registers, subroutines, control flow, measurements and custom gates as supported, and pulses as not yet supported[^fq3]. `wire_map` maps OpenQASM qubit names to PennyLane wires[^fq3]. Three things showed up in practice *(inference: ran with pennylane 0.45.1, openqasm3 1.0.1)*:
- **No `include` line.** The program above omits `include "stdgates.inc";` *(inference: ran)*. The canonical program from section 2 fails on that line with `NotImplementedError: An unsupported QASM instruction Include was encountered` *(inference: ran)*. With the line removed, `h` and `cx` still resolve and the `OPENQASM 3.0;` header is accepted *(inference: ran)*.
- **Register wire labels.** A register `qubit[2] q;` becomes wires labelled `"q[0]"` and `"q[1]"` *(inference: ran)*. On a device created with `wires=2` this raises a `WireError`, and none of the `wire_map` keys tried (`"q[0]"`, `{"q": [0, 1]}`, `{"q": 0}`) remapped it *(inference: ran)*. Two forms worked: separate `qubit q0; qubit q1;` with a `wire_map`, as above, or a device made without `wires=` so it accepts the string labels *(inference: ran)*.
- **Measurements in the program.** QASM measurements such as `c[0] = measure q0;` are imported as mid-circuit measurements (`┤↗├` in the drawing) *(inference: ran)*. The QNode's own `qp.counts()` then measures the result, and still gives `00`/`11` *(inference: ran)*.

**Loading OpenQASM 2: `qp.from_qasm`.**
```python
# needs: pip install pennylane-qiskit
prog2 = 'OPENQASM 2.0;\ninclude "qelib1.inc";\nqreg q[2];\ncreg c[2];\nh q[0];\ncx q[0],q[1];\nmeasure q -> c;\n'
loaded = qp.from_qasm(prog2, measurements=[])   # drop QASM's terminal measurements

@qp.set_shots(1000)
@qp.qnode(dev)
def bell_from_qasm2():
    loaded()
    return qp.counts()
# {'00': 503, '11': 497}
```
`qp.from_qasm(quantum_circuit, measurements=None)` loads a QASM string through the converter in the PennyLane-Qiskit plugin[^fq]. Its result is a quantum function that must be called, since `qp.from_qasm(s)` without the trailing `()` adds no operations[^fq]. By default the QASM program's measurements are kept and returned, `measurements=[]` removes the terminal ones, and a list of PennyLane measurements replaces them[^fq]. The plugin installs with `python -m pip install pennylane-qiskit`, and its docs recommend a clean environment[^plq]. The docs point to `from_qasm3` as the choice that avoids pennylane-qiskit and supports newer syntax[^fq]. In practice `qp.from_qasm` only parsed OpenQASM 2 *(inference: ran with pennylane-qiskit 0.45.0)*. Given the OpenQASM 3 Bell program, it raised `QASM2ParseError: can only handle OpenQASM 2.0, but given 3.0` *(inference: ran with pennylane-qiskit 0.45.0)*. Installing pennylane-qiskit 0.45.0 also pulled Qiskit down from 2.5.2 to 2.3.0, so a separate environment may be needed to have both the plugin and the newest Qiskit *(inference: from the pip resolver)*.

**Exporting from PennyLane.** `qp.to_openqasm(qnode)(...)` serialises a circuit to OpenQASM 2.0 only, and by default adds a measurement on every qubit[^toq]. When read back with `from_qasm` or `from_qasm3`, those terminal measurements come back as mid-circuit measurements[^toq].

### Side-by-side
| Step | Qiskit 2.5 | PennyLane 0.45 |
|---|---|---|
| Build | `QuantumCircuit(2, 2)`; `h`, `cx`, `measure` | QNode with `qp.Hadamard`, `qp.CNOT`, return a measurement |
| Draw | `qc.draw()` / `qc.draw("mpl")` | `qp.draw(qnode)()` / `qp.draw_mpl(qnode)()` |
| Load QASM 3 | `qasm3.loads` (+ `qiskit[qasm3-import]`) | `qp.from_qasm3` (+ `openqasm3[parser]`) |
| Load QASM 2 | `qasm2.loads` (built in) | `qp.from_qasm` (+ `pennylane-qiskit`) |
| Export | `qasm3.dumps`, `qasm2.dumps` | `qp.to_openqasm` (QASM 2 only) |
| Run | `StatevectorSampler().run([qc])`; IBM `SamplerV2` | `default.qubit` + `qp.set_shots` |
| Read | `result[0].data.<creg>.get_counts()` | `qp.counts()` / `qp.probs()` return value |
| Bit order | q0 is rightmost | wire 0 is leftmost |

Sources for the table are the sections above *(inference: summary)*.

## Follow-ups
- What does transpiling to an ISA circuit with `generate_preset_pass_manager` change in a circuit, stage by stage?
- How do mid-circuit measurement and classical feed-forward (`if (c[0]) ...`) work in OpenQASM 3, Qiskit and PennyLane?
- Why does PennyLane's `from_qasm3` reject `include "stdgates.inc"` and register wire maps, and is that fixed in a newer release?

[^circ]: [IBM Quantum Learning: Quantum circuits](sources/ibm-learning-quantum-circuits.md)
[^order]: [Qiskit guide: Bit ordering](sources/qiskit-bit-ordering.md)
[^ver]: [OpenQASM 3 spec: Comments, version string and included files](sources/openqasm3-spec-comments-includes.md)
[^types]: [OpenQASM 3 spec: Types and casting](sources/openqasm3-spec-types.md)
[^insts]: [OpenQASM 3 spec: Built-in quantum instructions](sources/openqasm3-spec-insts.md)
[^stdgates]: [OpenQASM 3 stdgates.inc](sources/openqasm3-stdgates-inc.md)
[^qelib]: [Qiskit's OpenQASM 2 qelib1.inc](sources/qiskit-qelib1-inc.md)
[^qc]: [Qiskit API: QuantumCircuit](sources/qiskit-quantumcircuit.md)
[^qasm3]: [Qiskit API: qiskit.qasm3](sources/qiskit-qasm3-module.md)
[^qasm2]: [Qiskit API: qiskit.qasm2](sources/qiskit-qasm2-module.md)
[^svs]: [Qiskit API: StatevectorSampler](sources/qiskit-statevectorsampler.md)
[^pio]: [Qiskit guide: Primitive inputs and outputs](sources/qiskit-primitive-input-output.md)
[^hello]: [IBM Quantum guide: Run your first circuit on hardware](sources/qiskit-hello-world.md)
[^rtsampler]: [Qiskit IBM Runtime API: SamplerV2](sources/qiskit-ibm-runtime-samplerv2.md)
[^execsampler]: [Qiskit IBM Runtime API: executor_sampler](sources/qiskit-ibm-runtime-executor-sampler.md)
[^plrn]: [PennyLane release notes](sources/pennylane-release-notes.md)
[^dq]: [PennyLane API: DefaultQubit](sources/pennylane-default-qubit.md)
[^draw]: [PennyLane API: qp.draw](sources/pennylane-draw.md)
[^drawmpl]: [PennyLane API: qp.draw_mpl](sources/pennylane-draw-mpl.md)
[^shots]: [PennyLane API: qp.set_shots](sources/pennylane-set-shots.md)
[^counts]: [PennyLane API: qp.counts](sources/pennylane-counts.md)
[^probs]: [PennyLane API: qp.probs](sources/pennylane-probs.md)
[^fq3]: [PennyLane API: qp.from_qasm3](sources/pennylane-from-qasm3.md)
[^fq]: [PennyLane API: qp.from_qasm](sources/pennylane-from-qasm.md)
[^plq]: [PennyLane-Qiskit plugin: Installation](sources/pennylane-qiskit-installation.md)
[^toq]: [PennyLane API: qp.to_openqasm](sources/pennylane-to-openqasm.md)
