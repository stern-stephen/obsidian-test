# Entanglement

## Overview

Entanglement is a feature of composite quantum systems. A state is entangled when it cannot be factored into a product of states for the individual subsystems.

For a bipartite system $AB$, a product state has the form:

$$
|\psi\rangle_A|\phi\rangle_B
$$

An entangled state cannot be written in that form.

## Example

A Bell state is:

$$
\frac{|00\rangle + |11\rangle}{\sqrt{2}}
$$

This state is not merely "qubit A has a state and qubit B has a state." The composite system has a definite joint state, while the parts alone do not have independent pure states.

## Schmidt Decomposition

For a pure bipartite state, the Schmidt decomposition writes:

$$
|\psi\rangle=\sum_i \lambda_i |i_A\rangle|i_B\rangle
$$

The number of nonzero Schmidt coefficients is the Schmidt number.

- Schmidt number $1$: product state.
- Schmidt number greater than $1$: entangled state.

For a maximally entangled two-qubit state, the two Schmidt coefficients are equal:

$$
\lambda_1=\lambda_2=\frac{1}{\sqrt{2}}
$$

## Reduced States

If a composite system is entangled, the state of one subsystem alone is described by a reduced density operator.

This is one reason density operators are not just a convenience for classical ignorance. They also describe the local state of a subsystem whose full joint state may be pure.

## Related Book Notes

- [Nielsen and Chuang: Schmidt Decomposition and Purifications](../Book%20Notes/Nielsen%20Chuang/Chapter%202/Schmidt%20Decomposition%20and%20Purifications.md)
- [Nielsen and Chuang: Density Operator](../Book%20Notes/Nielsen%20Chuang/Chapter%202/Density%20Operator.md)
- [Nielsen and Chuang: EPR and Bell Inequality](../Book%20Notes/Nielsen%20Chuang/Chapter%202/EPR%20and%20Bell%20Inequality.md)
- [Nielsen and Chuang: Superdense Coding](../Book%20Notes/Nielsen%20Chuang/Chapter%202/Superdense%20Coding.md)

## Related Concepts

- [Composite Quantum Systems](Composite%20Quantum%20Systems.md)
- [Tensor Products](../Linear%20Algebra/Tensor%20Products.md)
- [Density Operators](Density%20Operators.md)
- [Quantum Mechanics](Quantum%20Mechanics.md)
- [Quantum Computing](../Quantum%20Computing/Quantum%20Computing.md)

<!-- semantic-edges
{"source":"Entanglement","relation":"REQUIRES","target":"Composite Quantum Systems","evidence_heading":"Overview","evidence_summary":"The note defines entanglement as a feature of composite quantum systems whose states cannot factor into subsystem states.","confidence":0.95}
{"source":"Entanglement","relation":"CONTRASTS_WITH","target":"Product States","evidence_heading":"Overview","evidence_summary":"The note says an entangled state cannot be written as a product of states for the individual subsystems.","confidence":0.95}
{"source":"Bell State","relation":"EXAMPLE_OF","target":"Entanglement","evidence_heading":"Example","evidence_summary":"The note uses the state (|00> + |11>)/sqrt(2) as an example whose parts do not have independent pure states.","confidence":0.95}
{"source":"Schmidt Decomposition","relation":"DETERMINES","target":"Entanglement","evidence_heading":"Schmidt Decomposition","evidence_summary":"The note says Schmidt number one gives a product state, while Schmidt number greater than one gives an entangled state.","confidence":0.95}
{"source":"Entanglement","relation":"ENABLES","target":"Reduced Density Operators","evidence_heading":"Reduced States","evidence_summary":"The note says an entangled subsystem is described by a reduced density operator even when the full joint state is pure.","confidence":0.9}
{"source":"Maximally Entangled Two-Qubit States","relation":"SPECIALIZES","target":"Entanglement","evidence_heading":"Schmidt Decomposition","evidence_summary":"The note identifies maximally entangled two-qubit states by equal Schmidt coefficients.","confidence":0.85}
-->
