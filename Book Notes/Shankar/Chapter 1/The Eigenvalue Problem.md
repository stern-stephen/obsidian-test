# The Eigenvalue Problem

Source: [Principles of Quantum Mechanics](../../../References/Principals%20of%20quantum%20mechanics%20Shankar%20.pdf)

Book hub: [Shankar](../Shankar.md)

Book section: 1.8.

## Reading Status

- Status: started
- Pages:
- Date started: 2026-05-17
- Date finished:

## Big Ideas

- The eigenvalue problem asks for vectors whose direction is preserved by an operator.
- Eigenvectors give the natural basis for understanding an operator.
- Hermitian operators have especially nice eigenvalue structure: real eigenvalues and orthogonal eigenspaces.
- Diagonalization rewrites an operator in a basis where it acts by simple scalar multiplication.
- Simultaneous diagonalization is tied to commuting Hermitian operators.

## Notes

The eigenvalue equation is:

$$
A|v\rangle = \lambda |v\rangle
$$

where $|v\rangle \ne |0\rangle$.

The scalar $\lambda$ is the eigenvalue, and $|v\rangle$ is the eigenvector.

## Characteristic Equation

In matrix form, the eigenvalue equation becomes:

$$
(A-\lambda I)|v\rangle = |0\rangle
$$

For a nonzero solution to exist:

$$
\det(A-\lambda I) = 0
$$

This is the characteristic equation.

## Degeneracy

An eigenvalue is degenerate when more than one linearly independent eigenvector has that same eigenvalue.

The subspace of vectors with the same eigenvalue is called an eigenspace.

## Diagonalization

If an operator has enough linearly independent eigenvectors to form a basis, then its matrix in that basis is diagonal:

$$
A =
\begin{pmatrix}
\lambda_1 & 0 & \cdots \\
0 & \lambda_2 & \cdots \\
\vdots & \vdots & \ddots
\end{pmatrix}
$$

In that basis, applying $A$ just multiplies each component by the corresponding eigenvalue.

## Hermitian Operators

Hermitian operators are central in quantum mechanics because:

- their eigenvalues are real,
- eigenvectors with distinct eigenvalues are orthogonal,
- they can be diagonalized using an orthonormal eigenbasis.

This is why they are used for observables.

## Simultaneous Diagonalization

Two Hermitian operators can be simultaneously diagonalized when they commute and have the right shared eigenspace structure:

$$
[A,B] = 0
$$

This means there is a basis of vectors that are eigenvectors of both operators.

## Common Confusions

- Eigenvectors are not all vectors. They are special vectors whose direction is preserved by the operator.
- Degeneracy means an eigenspace has dimension greater than one.
- Diagonalization is a change of basis, not a change of the underlying operator.
- Commuting operators are important because they can often be understood using the same eigenbasis.

## Study Questions

- Why does $\det(A-\lambda I)=0$ signal the existence of a nonzero eigenvector?
- What does degeneracy mean geometrically?
- Why are Hermitian operators the right mathematical model for observables?
- What physical idea is suggested by two observables sharing an eigenbasis?

## Links To Concept Notes

- [Eigenvalues and Eigenvectors](../../../Linear%20Algebra/Eigenvalues%20and%20Eigenvectors.md)
- [Hermitian Matrices and Operators](../../../Linear%20Algebra/Hermitian%20Matrices%20and%20Operators.md)
- [Change of Basis](../../../Linear%20Algebra/Change%20of%20Basis.md)
- [Unitary Matrices](../../../Linear%20Algebra/Unitary%20Matrices.md)
- [Functions of Operators](Functions%20of%20Operators.md)
