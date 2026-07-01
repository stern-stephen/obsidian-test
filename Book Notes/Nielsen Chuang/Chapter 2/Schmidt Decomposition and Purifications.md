# Schmidt Decomposition And Purifications

Source: [quantum-computation-and-quantum-information-nielsen-chuang](../../../References/quantum-computation-and-quantum-information-nielsen-chuang.pdf)

Book hub: [Nielsen And Chuang](../Nielsen%20Chuang.md)

Parent chapter: [Quantum Mechanics](Quantum%20Mechanics.md)

Book section: 2.5, pages 109-110.

## Overview

The Schmidt decomposition is a canonical way to write pure states of bipartite quantum systems.

It exposes the entanglement structure of a state and connects naturally to reduced density operators.

Reusable topic notes:

- [Entanglement](../../../Quantum%20Mechanics/Entanglement.md)
- [Density Operators](../../../Quantum%20Mechanics/Density%20Operators.md)
- [Composite Quantum Systems](../../../Quantum%20Mechanics/Composite%20Quantum%20Systems.md)

## Schmidt Decomposition

For a pure state $|\psi\rangle$ of a composite system $AB$, there exist orthonormal bases $\lbrace |i_A\rangle\rbrace$ and $\lbrace |i_B\rangle\rbrace$ such that:

$$
|\psi\rangle = \sum_i \lambda_i |i_A\rangle|i_B\rangle
$$

The nonnegative numbers $\lambda_i$ are the Schmidt coefficients.

Because $|\psi\rangle$ is normalized:

$$
\sum_i \lambda_i^2 = 1
$$

The number of nonzero Schmidt coefficients is called the Schmidt number.

## Entanglement

The Schmidt decomposition gives a clean test for entanglement.

If a bipartite pure state has Schmidt number $1$, it is a product state.

If it has Schmidt number greater than $1$, it is entangled.

For a maximally entangled two-qubit state, the Schmidt coefficients are equal:

$$
\lambda_1 = \lambda_2 = \frac{1}{\sqrt{2}}
$$

## Purification

Purification represents a mixed state as part of a larger pure state.

Given a density operator $\rho^A$, we can introduce an auxiliary reference system $R$ and find a pure state $|AR\rangle$ such that:

$$
\rho^A = \operatorname{tr}_R(|AR\rangle\langle AR|)
$$

The larger pure state $|AR\rangle$ is called a purification of $\rho^A$.

This reinforces the idea that mixed states can arise from ignoring part of a larger entangled system.

## Why It Matters

The Schmidt decomposition and purification are basic tools for reasoning about composite quantum systems.

They help explain:

- Which pure states are entangled.
- How reduced density operators arise.
- Why a mixed state can be viewed as part of a larger pure state.
- How auxiliary systems can simplify proofs and constructions.

## Related Concepts

- [Density Operators](../../../Quantum%20Mechanics/Density%20Operators.md)
- [Entanglement](../../../Quantum%20Mechanics/Entanglement.md)
- [Composite Quantum Systems](../../../Quantum%20Mechanics/Composite%20Quantum%20Systems.md)
- [Quantum Mechanics](../../../Quantum%20Mechanics/Quantum%20Mechanics.md)
- [Quantum Computing](../../../Quantum%20Computing/Quantum%20Computing.md)
- [Vector Spaces](../../../Linear%20Algebra/Vector%20Spaces.md)
- [Tensor Products](../../../Linear%20Algebra/Tensor%20Products.md)
- [Eigenvalues](../../../Linear%20Algebra/Eigenvalues%20and%20Eigenvectors.md)

<!-- semantic-edges
{"source":"Nielsen and Chuang Section 2.5","relation":"INTRODUCES","target":"Schmidt Decomposition","evidence_heading":"Overview","evidence_summary":"Introduces the Schmidt decomposition as a canonical representation of pure bipartite quantum states.","confidence":0.92}
{"source":"Schmidt Coefficients","relation":"DETERMINES","target":"Schmidt Number","evidence_heading":"Schmidt Decomposition","evidence_summary":"The number of nonzero Schmidt coefficients is defined as the Schmidt number.","confidence":0.89}
{"source":"Schmidt Number","relation":"DETERMINES","target":"Pure-State Entanglement","evidence_heading":"Entanglement","evidence_summary":"A bipartite pure state is a product state when the Schmidt number is one and entangled when it is greater than one.","confidence":0.91}
{"source":"Equal Schmidt Coefficients","relation":"REPRESENTS","target":"Maximally Entangled Two-Qubit State","evidence_heading":"Entanglement","evidence_summary":"For a maximally entangled two-qubit state, the two Schmidt coefficients are equal to one over square root two.","confidence":0.88}
{"source":"Purification","relation":"REPRESENTS","target":"Mixed State as Larger Pure State","evidence_heading":"Purification","evidence_summary":"Purification represents a mixed state as the reduced state of a larger pure state on an auxiliary reference system.","confidence":0.91}
-->
