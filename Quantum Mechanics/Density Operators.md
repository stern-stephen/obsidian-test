# Density Operators

## Overview

A density operator describes a quantum state in a way that includes both pure states and mixed states.

Density operators are useful when:

- There is classical uncertainty about which pure state was prepared.
- A subsystem is entangled with another system.
- The system is open or interacting with an environment.
- Measurements are easier to express using traces.

## Definition

For an ensemble where state $|\psi_i\rangle$ occurs with probability $p_i$, the density operator is:

$$
\rho=\sum_i p_i |\psi_i\rangle\langle \psi_i|
$$

A pure state $|\psi\rangle$ has density operator:

$$
\rho=|\psi\rangle\langle \psi|
$$

## Properties

A valid density operator satisfies:

$$
\operatorname{tr}(\rho)=1
$$

and:

$$
\rho \ge 0
$$

The positivity condition means measurement probabilities are never negative.

A useful purity test is:

$$
\operatorname{tr}(\rho^2)=1
$$

for pure states, while mixed states satisfy:

$$
\operatorname{tr}(\rho^2)<1
$$

## Measurement Probabilities

For a POVM element $E_m$, the probability of outcome $m$ is:

$$
p(m)=\operatorname{tr}(E_m\rho)
$$

This is the density-operator version of the Born rule.

## Reduced Density Operators

For a composite system $AB$ with density operator $\rho^{AB}$, the state of subsystem $A$ is:

$$
\rho^A=\operatorname{tr}_B(\rho^{AB})
$$

The operation $\operatorname{tr}_B$ is the partial trace over subsystem $B$.

This explains how part of an entangled pure state can look mixed when considered alone.

## Related Book Notes

- [Nielsen and Chuang: Density Operator](../Book%20Notes/Nielsen%20Chuang/Chapter%202/Density%20Operator.md)
- [Nielsen and Chuang: Schmidt Decomposition and Purifications](../Book%20Notes/Nielsen%20Chuang/Chapter%202/Schmidt%20Decomposition%20and%20Purifications.md)
- [Nielsen and Chuang: Postulates of Quantum Mechanics](../Book%20Notes/Nielsen%20Chuang/Chapter%202/Postulates%20of%20Quantum%20Mechanics.md)

## Related Concepts

- [Quantum Mechanics](Quantum%20Mechanics.md)
- [Quantum Measurement](Quantum%20Measurement.md)
- [Composite Quantum Systems](Composite%20Quantum%20Systems.md)
- [Entanglement](Entanglement.md)
- [Bra-Ket Notation](../Linear%20Algebra/Bra-Ket%20Notation.md)
- [Hermitian Operators](../Linear%20Algebra/Hermitian%20Matrices%20and%20Operators.md)

<!-- semantic-edges
{"source":"Density Operators","relation":"PART_OF","target":"Quantum Mechanics","evidence_heading":"Overview","evidence_summary":"This concept note belongs to the Quantum Mechanics area of the vault.","confidence":0.85}
{"source":"Density Operators","relation":"QUANTUM_MECHANICS_RELATED_TO","target":"Nielsen and Chuang: Density Operator","evidence_heading":"Related Book Notes","evidence_summary":"The note explicitly connects Density Operators with Nielsen and Chuang: Density Operator in its discussion or related-note links.","confidence":0.75}
{"source":"Density Operators","relation":"QUANTUM_MECHANICS_RELATED_TO","target":"Nielsen and Chuang: Schmidt Decomposition and Purifications","evidence_heading":"Related Book Notes","evidence_summary":"The note explicitly connects Density Operators with Nielsen and Chuang: Schmidt Decomposition and Purifications in its discussion or related-note links.","confidence":0.75}
{"source":"Density Operators","relation":"QUANTUM_MECHANICS_RELATED_TO","target":"Nielsen and Chuang: Postulates of Quantum Mechanics","evidence_heading":"Related Book Notes","evidence_summary":"The note explicitly connects Density Operators with Nielsen and Chuang: Postulates of Quantum Mechanics in its discussion or related-note links.","confidence":0.75}
{"source":"Density Operators","relation":"QUANTUM_MECHANICS_RELATED_TO","target":"Quantum Mechanics","evidence_heading":"Related Concepts","evidence_summary":"The note explicitly connects Density Operators with Quantum Mechanics in its discussion or related-note links.","confidence":0.75}
-->
