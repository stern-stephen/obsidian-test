# Density Operator

Source: [quantum-computation-and-quantum-information-nielsen-chuang](../../../References/quantum-computation-and-quantum-information-nielsen-chuang.pdf)

Book hub: [Nielsen And Chuang](../Nielsen%20Chuang.md)

Parent chapter: [Quantum Mechanics](Quantum%20Mechanics.md)

Book section: 2.4, pages 98-108.

## Overview

The density operator is a way to describe quantum states when there may be uncertainty about which pure state a system is in.

It is also the natural language for subsystems of entangled composite systems.

Reusable topic note: [Density Operators](../../../Quantum%20Mechanics/Density%20Operators.md).

## 2.4.1 Ensembles Of Quantum States

Suppose a system is prepared in state $|\psi_i\rangle$ with probability $p_i$.

The ensemble is:

$$
\lbrace p_i, |\psi_i\rangle\rbrace
$$

The corresponding density operator is:

$$
\rho = \sum_i p_i |\psi_i\rangle\langle \psi_i|
$$

A pure state $|\psi\rangle$ has density operator:

$$
\rho = |\psi\rangle\langle \psi|
$$

A mixed state represents classical uncertainty over possible quantum states.

## 2.4.2 General Properties

A density operator $\rho$ satisfies:

$$
\operatorname{tr}(\rho) = 1
$$

and:

$$
\rho \ge 0
$$

The condition $\rho \ge 0$ means the density operator is positive: all measurement probabilities it produces are nonnegative.

The probability of a measurement outcome can be computed from $\rho$.

For a POVM element $E_m$:

$$
p(m) = \operatorname{tr}(E_m \rho)
$$

For a pure state density operator, the trace condition corresponds to state normalization.

A useful test for purity is:

$$
\operatorname{tr}(\rho^2) = 1
$$

for pure states, while mixed states have:

$$
\operatorname{tr}(\rho^2) < 1
$$

## 2.4.3 The Reduced Density Operator

The reduced density operator describes part of a composite system.

If a joint system $AB$ has density operator $\rho^{AB}$, then the state of subsystem $A$ is:

$$
\rho^A = \operatorname{tr}_B(\rho^{AB})
$$

The operation $\operatorname{tr}_B$ is the partial trace over system $B$.

This is important because a subsystem of an entangled pure state can look mixed.

For example, if two qubits are in an entangled Bell state, the state of either qubit alone is not a pure state. The reduced density operator captures what can be predicted from measurements on that subsystem alone.

## Why It Matters

Density operators are more general than state vectors.

They handle:

- Classical uncertainty about preparation.
- Subsystems of entangled states.
- Measurement probabilities.
- Open systems interacting with an environment.

They become essential for later topics such as noise, decoherence, quantum channels, and quantum error correction.

## Questions To Revisit

- How can different ensembles produce the same density operator?
- Why does tracing out part of an entangled system produce a mixed state?
- What is the operational meaning of $\operatorname{tr}(\rho^2)$?

## Related Concepts

- [Quantum Mechanics](../../../Quantum%20Mechanics/Quantum%20Mechanics.md)
- [Density Operators](../../../Quantum%20Mechanics/Density%20Operators.md)
- [Quantum Measurement](../../../Quantum%20Mechanics/Quantum%20Measurement.md)
- [Composite Quantum Systems](../../../Quantum%20Mechanics/Composite%20Quantum%20Systems.md)
- [Entanglement](../../../Quantum%20Mechanics/Entanglement.md)
- [Postulates Of Quantum Mechanics](Postulates%20of%20Quantum%20Mechanics.md)
- [Bra-Ket Notation](../../../Linear%20Algebra/Bra-Ket%20Notation.md)
- [Hermitian Matrices and Operators](../../../Linear%20Algebra/Hermitian%20Matrices%20and%20Operators.md)

<!-- semantic-edges
{"source":"Density Operator","relation":"PART_OF","target":"Nielsen Chuang Chapter 2","evidence_heading":"Book metadata","evidence_summary":"This note is a source-specific section note in Nielsen Chuang Chapter 2.","confidence":0.85}
{"source":"Density Operator","relation":"SOURCE_CONTEXT_FOR","target":"Nielsen And Chuang","evidence_heading":"Density Operator","evidence_summary":"This source note explicitly links its treatment to Nielsen And Chuang.","confidence":0.8}
{"source":"Density Operator","relation":"SOURCE_CONTEXT_FOR","target":"Quantum Mechanics","evidence_heading":"Density Operator","evidence_summary":"This source note explicitly links its treatment to Quantum Mechanics.","confidence":0.8}
{"source":"Density Operator","relation":"SOURCE_CONTEXT_FOR","target":"Density Operators","evidence_heading":"Overview","evidence_summary":"This source note explicitly links its treatment to Density Operators.","confidence":0.8}
{"source":"Density Operator","relation":"SOURCE_CONTEXT_FOR","target":"Quantum Measurement","evidence_heading":"Related Concepts","evidence_summary":"This source note explicitly links its treatment to Quantum Measurement.","confidence":0.8}
-->
