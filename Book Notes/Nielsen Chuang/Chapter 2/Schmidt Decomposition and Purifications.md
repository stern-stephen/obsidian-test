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
