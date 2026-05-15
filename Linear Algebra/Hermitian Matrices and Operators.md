# Hermitian Operators And Matrices

## Overview

A **Hermitian operator** is an operator that is equal to its own adjoint.

For an operator $A$, this means:

$$
A = A^\dagger
$$

where $A^\dagger$ is the adjoint of $A$.

When a Hermitian operator is represented by a complex matrix, that matrix is equal to its conjugate transpose. In real-valued matrix representations, Hermitian matrices reduce to **symmetric matrices**, since complex conjugation has no effect.

The operation $A^\dagger$ is called the [adjoint](Adjoints.md).

## Definition

For a matrix representation $A = [a_{ij}]$, the operator is Hermitian when:

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

This matrix represents a Hermitian operator because:

- The diagonal entries $2$ and $5$ are real.
- The off-diagonal entries $3+i$ and $3-i$ are complex conjugates.

## Key Properties

Hermitian operators are important because they behave like real numbers in many linear algebra settings.

- Every eigenvalue of a Hermitian operator is real.
- Eigenvectors belonging to distinct eigenvalues are orthogonal.
- A Hermitian operator can be diagonalized by a unitary operator.
- Hermitian operators represent observable quantities in quantum mechanics.

## Eigenvalues And Eigenvectors

Hermitian operators have especially well-behaved [Eigenvalues](Eigenvalues.md).

### Real Eigenvalues

Their eigenvalues are always real.

Suppose $A$ is Hermitian and $A v = \lambda v$ for a nonzero vector $v$. Because $A$ is Hermitian:

$$
A = A^\dagger
$$

Now look at the scalar $v^\dagger A v$. Using $A v = \lambda v$:

$$
v^\dagger A v = v^\dagger \lambda v
$$

so:

$$
v^\dagger A v = \lambda v^\dagger v
$$

But $v^\dagger A v$ is equal to its own complex conjugate:

$$
\overline{v^\dagger A v}
= (v^\dagger A v)^\dagger
= v^\dagger A^\dagger v
= v^\dagger A v
$$

So $v^\dagger A v$ is real. Also, $v^\dagger v$ is the squared length of $v$, so it is real and positive:

$$
v^\dagger v > 0
$$

Therefore:

$$
\lambda = \frac{v^\dagger A v}{v^\dagger v}
$$

Since the numerator and denominator are both real, $\lambda$ is real.

### Orthogonal Eigenvectors

Eigenvectors with different eigenvalues are orthogonal.

Suppose:

$$
A v = \lambda v
$$

and:

$$
A w = \mu w
$$

where $\lambda \ne \mu$.

Look at $v^\dagger A w$. Using $A w = \mu w$:

$$
v^\dagger A w = \mu v^\dagger w
$$

Using $A = A^\dagger$ and $A v = \lambda v$:

$$
v^\dagger A w = (A v)^\dagger w
$$

so:

$$
v^\dagger A w = (\lambda v)^\dagger w
$$

Because Hermitian eigenvalues are real, $\overline{\lambda} = \lambda$, so:

$$
v^\dagger A w = \lambda v^\dagger w
$$

Putting the two expressions for $v^\dagger A w$ together:

$$
\mu v^\dagger w = \lambda v^\dagger w
$$

Thus:

$$
(\mu - \lambda)v^\dagger w = 0
$$

Since $\mu \ne \lambda$, it must be true that:

$$
v^\dagger w = 0
$$

This means a Hermitian operator has a clean geometry: its eigenvectors point in mutually perpendicular directions.

A Hermitian operator can be written in an orthonormal basis of eigenvectors. In matrix form:

$$
A = U \Lambda U^\dagger
$$

where $U$ is a unitary matrix whose columns are eigenvectors, and $\Lambda$ is a diagonal matrix containing the eigenvalues. This is the **spectral theorem** for Hermitian operators.

The orthonormal eigenvector basis can be understood using ideas from [Vector Spaces](Vector%20Spaces.md) and [Gram-Schmidt](Gram-Schmidt.md).

## Inner Product Definition

The definition of a Hermitian operator can also be written directly in terms of the inner product.

An operator $T$ on an inner product space is Hermitian, also called **self-adjoint**, if:

$$
\langle T x, y \rangle = \langle x, T y \rangle
$$

for all vectors $x$ and $y$ in the space.

This condition says that applying the operator to the first input of the inner product has the same effect as applying it to the second input.

In [Bra-Ket Notation](Bra-Ket%20Notation.md), Hermitian operators are often used inside expressions like $\langle \psi|A|\psi\rangle$.

## Connection To Quantum Mechanics

In quantum mechanics, Hermitian operators are used to represent measurable physical quantities, such as:

- Position
- Momentum
- Energy
- Spin

The reason is that measurements must produce real values, and Hermitian operators have real eigenvalues.

## Intuition

You can think of a Hermitian operator as an operator with a special kind of symmetry relative to the inner product.

In a matrix representation, this symmetry appears by mirroring entries with complex conjugation. This gives the operator enough structure to guarantee real eigenvalues and orthogonal eigenvectors.

## Related Concepts

- [Linear Algebra](Linear%20Algebra.md)
- [Vector Spaces](Vector%20Spaces.md)
- [Adjoints](Adjoints.md)
- [Bra-Ket Notation](Bra-Ket%20Notation.md)
- [Eigenvalues](Eigenvalues.md)
- [Unitary Matrices](Unitary%20Matrices.md)
- [Quantum Mechanics](../Quantum%20Mechanics/Quantum%20Mechanics.md)
