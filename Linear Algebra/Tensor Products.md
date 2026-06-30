# Tensor Products

## Overview

Tensor products combine vector spaces into a larger vector space. They are the linear algebra behind composite quantum systems and multi-qubit states.

If $V$ and $W$ are vector spaces, their tensor product is written:

$$
V \otimes W
$$

If $|v\rangle \in V$ and $|w\rangle \in W$, their product state is:

$$
|v\rangle \otimes |w\rangle
$$

In quantum mechanics this is often abbreviated:

$$
|v\rangle|w\rangle
$$

## Basis Construction

If $V$ has basis $\lbrace |i\rangle\rbrace$ and $W$ has basis $\lbrace |j\rangle\rbrace$, then $V \otimes W$ has basis vectors:

$$
|i\rangle|j\rangle
$$

For two qubits:

$$
\mathbb{C}^2 \otimes \mathbb{C}^2
$$

has computational basis:

$$
|00\rangle,\ |01\rangle,\ |10\rangle,\ |11\rangle
$$

The dimensions multiply:

$$
\dim(V \otimes W)=\dim(V)\dim(W)
$$

## Product States And Entangled States

A product state can be written as a tensor product of subsystem states:

$$
|\psi\rangle_A|\phi\rangle_B
$$

Not every vector in a tensor product space can be written this way. States that cannot be factored into subsystem states are entangled.

## Operators On Tensor Products

Operators can also be tensored. If $A$ acts on $V$ and $B$ acts on $W$, then $A \otimes B$ acts on $V \otimes W$ by:

$$
(A \otimes B)(|v\rangle|w\rangle)=(A|v\rangle)(B|w\rangle)
$$

This is the algebraic language for applying gates or observables to parts of a composite quantum system.

## Related Book Notes

- [Nielsen and Chuang: Linear Algebra](../Book%20Notes/Nielsen%20Chuang/Chapter%202/Linear%20Algebra.md#217-tensor-products)
- [Nielsen and Chuang: Postulates of Quantum Mechanics](../Book%20Notes/Nielsen%20Chuang/Chapter%202/Postulates%20of%20Quantum%20Mechanics.md#228-composite-systems)
- [Nielsen and Chuang: Schmidt Decomposition and Purifications](../Book%20Notes/Nielsen%20Chuang/Chapter%202/Schmidt%20Decomposition%20and%20Purifications.md)

## Related Concepts

- [Vector Spaces](Vector%20Spaces.md)
- [Bra-Ket Notation](Bra-Ket%20Notation.md)
- [Quantum Mechanics](../Quantum%20Mechanics/Quantum%20Mechanics.md)
- [Composite Quantum Systems](../Quantum%20Mechanics/Composite%20Quantum%20Systems.md)
- [Entanglement](../Quantum%20Mechanics/Entanglement.md)
