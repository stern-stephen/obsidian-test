# Hermitian Matrices and Operators

## Overview

A **Hermitian matrix** is a complex square matrix that is equal to its own conjugate transpose.

For a matrix $A$, this means:

$$
A = A^\dagger
$$

where $A^\dagger$ means transpose the matrix and take the complex conjugate of every entry.

In real-valued matrices, Hermitian matrices reduce to **symmetric matrices**, since complex conjugation has no effect.

The operation $A^\dagger$ is called the [[Adjoints|adjoint]].

## Definition

If $A = [a_{ij}]$, then $A$ is Hermitian when:

$$
a_{ij} = \overline{a_{ji}}
$$

for every pair of indices $i$ and $j$.

This means entries mirrored across the diagonal are complex conjugates of each other.

## Example

$$
A =
\begin{bmatrix}
2 & 3+i \\
3-i & 5
\end{bmatrix}
$$

This matrix is Hermitian because:

- The diagonal entries $2$ and $5$ are real.
- The off-diagonal entries $3+i$ and $3-i$ are complex conjugates.

## Key Properties

Hermitian matrices are important because they behave like real numbers in many linear algebra settings.

- Every eigenvalue of a Hermitian matrix is real.
- Eigenvectors belonging to distinct eigenvalues are orthogonal.
- A Hermitian matrix can be diagonalized by a unitary matrix.
- Hermitian matrices represent observable quantities in quantum mechanics.

## Eigenvalues And Eigenvectors

Hermitian matrices have especially well-behaved [[Eigenvalues]].

Their eigenvalues are always real, eigenvectors with distinct eigenvalues are orthogonal, and every Hermitian matrix can be diagonalized by a unitary matrix:

$$
A = U \Lambda U^\dagger
$$

The detailed eigenvalue explanation is in [[Eigenvalues#Hermitian Matrices]].

## Hermitian Operators

A **Hermitian operator** is the infinite-dimensional or abstract vector-space version of a Hermitian matrix.

An operator $T$ on an inner product space is Hermitian, also called **self-adjoint**, if:

$$
\langle T x, y \rangle = \langle x, T y \rangle
$$

for all vectors $x$ and $y$ in the space.

This condition says that applying the operator to the first input of the inner product has the same effect as applying it to the second input.

In [[Bra-Ket Notation]], Hermitian operators are often used inside expressions like $\langle \psi|A|\psi\rangle$.

## Connection To Quantum Mechanics

In quantum mechanics, Hermitian operators are used to represent measurable physical quantities, such as:

- Position
- Momentum
- Energy
- Spin

The reason is that measurements must produce real values, and Hermitian operators have real eigenvalues.

## Intuition

You can think of a Hermitian matrix as a complex matrix with a special kind of symmetry.

Instead of mirroring entries exactly, it mirrors them with complex conjugation. This gives the matrix enough structure to guarantee real eigenvalues and orthogonal eigenvectors.

## Related Concepts

- [[Linear Algebra]]
- [[Vector Spaces]]
- [[Adjoints]]
- [[Bra-Ket Notation]]
- [[Eigenvalues]]
- [[Unitary Matrices]]
- [[Quantum Mechanics]]
