# Composite Quantum Systems

## Overview

A composite quantum system is built from smaller quantum systems. The state space of the whole system is the tensor product of the state spaces of its parts.

For systems $A$ and $B$:

$$
\mathcal{H}_{AB}=\mathcal{H}_A \otimes \mathcal{H}_B
$$

If system $A$ is in $|\psi\rangle$ and system $B$ is in $|\phi\rangle$, a product state is:

$$
|\psi\rangle|\phi\rangle
$$

## Two Qubits

Two qubits have a four-dimensional state space:

$$
\mathbb{C}^2 \otimes \mathbb{C}^2
$$

with computational basis:

$$
|00\rangle,\ |01\rangle,\ |10\rangle,\ |11\rangle
$$

A general two-qubit state is a linear combination of these basis states.

## Entanglement

Composite systems allow entangled states. An entangled state cannot be written as a product of individual subsystem states.

This is why composite quantum systems are not just a bookkeeping device. The tensor product structure creates states with correlations that have no classical analogue.

## Related Book Notes

- [Nielsen and Chuang: Postulates of Quantum Mechanics](../Book%20Notes/Nielsen%20Chuang/Chapter%202/Postulates%20of%20Quantum%20Mechanics.md#228-composite-systems)
- [Nielsen and Chuang: Schmidt Decomposition and Purifications](../Book%20Notes/Nielsen%20Chuang/Chapter%202/Schmidt%20Decomposition%20and%20Purifications.md)
- [Nielsen and Chuang: EPR and Bell Inequality](../Book%20Notes/Nielsen%20Chuang/Chapter%202/EPR%20and%20Bell%20Inequality.md)

## Related Concepts

- [Quantum Mechanics](Quantum%20Mechanics.md)
- [Tensor Products](../Linear%20Algebra/Tensor%20Products.md)
- [Entanglement](Entanglement.md)
- [Density Operators](Density%20Operators.md)
- [Quantum Computing](../Quantum%20Computing/Quantum%20Computing.md)

<!-- semantic-edges
{"source":"Composite Quantum Systems","relation":"PART_OF","target":"Quantum Mechanics","evidence_heading":"Overview","evidence_summary":"This concept note belongs to the Quantum Mechanics area of the vault.","confidence":0.85}
{"source":"Composite Quantum Systems","relation":"QUANTUM_MECHANICS_RELATED_TO","target":"Nielsen and Chuang: Postulates of Quantum Mechanics","evidence_heading":"Related Book Notes","evidence_summary":"The note explicitly connects Composite Quantum Systems with Nielsen and Chuang: Postulates of Quantum Mechanics in its discussion or related-note links.","confidence":0.75}
{"source":"Composite Quantum Systems","relation":"QUANTUM_MECHANICS_RELATED_TO","target":"Nielsen and Chuang: Schmidt Decomposition and Purifications","evidence_heading":"Related Book Notes","evidence_summary":"The note explicitly connects Composite Quantum Systems with Nielsen and Chuang: Schmidt Decomposition and Purifications in its discussion or related-note links.","confidence":0.75}
{"source":"Composite Quantum Systems","relation":"QUANTUM_MECHANICS_RELATED_TO","target":"Nielsen and Chuang: EPR and Bell Inequality","evidence_heading":"Related Book Notes","evidence_summary":"The note explicitly connects Composite Quantum Systems with Nielsen and Chuang: EPR and Bell Inequality in its discussion or related-note links.","confidence":0.75}
{"source":"Composite Quantum Systems","relation":"QUANTUM_MECHANICS_RELATED_TO","target":"Quantum Mechanics","evidence_heading":"Related Concepts","evidence_summary":"The note explicitly connects Composite Quantum Systems with Quantum Mechanics in its discussion or related-note links.","confidence":0.75}
-->
