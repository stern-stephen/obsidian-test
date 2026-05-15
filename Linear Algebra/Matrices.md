# Matrices

## Overview

A **matrix** is a rectangular array of numbers or symbols.

Matrices are often used to represent linear operators between vector spaces after bases have been chosen.

For example:

$$
A =
\begin{bmatrix}
a & b \\
c & d
\end{bmatrix}
$$

can act on a vector:

$$
Av
$$

## Operators And Matrix Representations

Once a basis is chosen, a linear operator can be represented by a matrix.

Changing the basis changes the matrix representation of the same operator. This is the idea behind [Change of Basis](Change%20of%20Basis.md).

This is why matrices are central to [Linear Algebra](Linear%20Algebra.md), [Change of Basis](Change%20of%20Basis.md), [Gaussian Elimination](Gaussian%20Elimination.md), [Projection Matrices](Projection%20Matrices.md), [Rotation Matrices](Rotation%20Matrices.md), [Eigenvalues](Eigenvalues.md), [Unitary Matrices](Unitary%20Matrices.md), and [Hermitian Matrices and Operators](Hermitian%20Matrices%20and%20Operators.md): they are concrete coordinate representations of operators.

## Matrix Multiplication From Operators

Matrix multiplication comes from composing linear operators.

Suppose $T$ and $S$ are linear operators. The composition $S \circ T$ means apply $T$ first and then apply $S$:

$$
(S \circ T)(v) = S(T(v))
$$

If $T$ is represented by the matrix $A$ and $S$ is represented by the matrix $B$, then the composed operator $S \circ T$ is represented by:

$$
BA
$$

The order matters. The matrix closest to the vector acts first:

$$
BAx = B(Ax)
$$

This is why matrix multiplication is defined the way it is: the columns of $A$ describe where basis vectors go under $T$, and multiplying by $B$ then sends those outputs through $S$.

The entry formula:

$$
(BA)_{ij} = \sum_k B_{ik}A_{kj}
$$

records the same composition in coordinates. The $j$th column of $BA$ is what happens to the $j$th basis vector after applying $A$ first and then $B$.

Because operator composition is usually not commutative, matrix multiplication is usually not commutative:

$$
BA \ne AB
$$

## Related Concepts

- [Linear Algebra](Linear%20Algebra.md)
- [Vectors](Vectors.md)
- [Vector Spaces](Vector%20Spaces.md)
- [Linear Operators](Linear%20Operators.md)
- [Change of Basis](Change%20of%20Basis.md)
- [Gaussian Elimination](Gaussian%20Elimination.md)
- [Projection Matrices](Projection%20Matrices.md)
- [Rotation Matrices](Rotation%20Matrices.md)
- [Four Fundamental Subspaces](Four%20Fundamental%20Subspaces.md)
- [Adjoints](Adjoints.md)
- [Eigenvalues](Eigenvalues.md)
