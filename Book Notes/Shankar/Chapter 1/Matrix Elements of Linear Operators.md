# Matrix Elements of Linear Operators

Source: [Principles of Quantum Mechanics](../../../References/Principals%20of%20quantum%20mechanics%20Shankar%20.pdf)

Book hub: [Shankar](../Shankar.md)

Book section: 1.6.

## Reading Status

- Status: started
- Pages:
- Date started: 2026-05-17
- Date finished:

## Big Ideas

- Matrix elements are the components of an operator in a chosen basis.
- The matrix element $A_{ij}$ is found by inserting a bra and ket around the operator.
- Products, adjoints, Hermitian operators, and unitary operators all have clean matrix-element rules.
- This section connects abstract operator equations to concrete matrix calculations.

## Notes

If $\{|i\rangle\}$ is an orthonormal basis, the matrix element of $A$ is:

$$
A_{ij} = \langle i|A|j\rangle
$$

This entry answers: if $A$ acts on basis vector $|j\rangle$, how much of the result points along $|i\rangle$?

The operator can be reconstructed from its matrix elements:

$$
A = \sum_{ij} |i\rangle A_{ij}\langle j|
$$

## Products Of Operators

For a product $AB$:

$$
(AB)_{ij} = \sum_k A_{ik}B_{kj}
$$

This is the usual matrix multiplication rule.

## Adjoint Of An Operator

The adjoint satisfies:

$$
\langle u|A v\rangle = \langle A^\dagger u|v\rangle
$$

In matrix form:

$$
(A^\dagger)_{ij} = A_{ji}^*
$$

So the matrix of $A^\dagger$ is the conjugate transpose of the matrix of $A$.

## Special Operator Classes

A Hermitian operator satisfies:

$$
A^\dagger = A
$$

An anti-Hermitian operator satisfies:

$$
A^\dagger = -A
$$

A unitary operator satisfies:

$$
U^\dagger U = I
$$

Hermitian operators matter because their eigenvalues are real. Unitary operators matter because they preserve inner products and norms.

## Common Confusions

- The indices in $A_{ij}=\langle i|A|j\rangle$ are ordered: $j$ labels the input basis vector, $i$ labels the output component.
- The adjoint is not just a transpose in complex spaces. It is a conjugate transpose.
- Hermitian and unitary mean different things, though some operators can be both.

## Links To Concept Notes

- [Matrices](../../../Linear%20Algebra/Matrices.md)
- [Linear Operators](../../../Linear%20Algebra/Linear%20Operators.md)
- [Adjoints](../../../Linear%20Algebra/Adjoints.md)
- [Hermitian Matrices and Operators](../../../Linear%20Algebra/Hermitian%20Matrices%20and%20Operators.md)
- [Unitary Matrices](../../../Linear%20Algebra/Unitary%20Matrices.md)
- [Bra-Ket Notation](../../../Linear%20Algebra/Bra-Ket%20Notation.md)
