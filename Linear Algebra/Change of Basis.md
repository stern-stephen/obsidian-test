# Change of Basis

## Overview

A **change of basis** rewrites the same vector or linear operator using a different coordinate system.

The underlying vector does not change. Only its coordinates change.

For example, the same geometric vector can be described using the standard basis:

$$
e_1 =
\begin{bmatrix}
1 \\
0
\end{bmatrix},
\quad
e_2 =
\begin{bmatrix}
0 \\
1
\end{bmatrix}
$$

or using another basis:

$$
b_1 =
\begin{bmatrix}
1 \\
1
\end{bmatrix},
\quad
b_2 =
\begin{bmatrix}
1 \\
-1
\end{bmatrix}
$$

The vector is the same object, but the list of coordinates depends on the basis.

## Coordinates In A Basis

Let $B = \lbrace b_1, b_2, \ldots, b_n\rbrace$ be a basis for a vector space.

If:

$$
v = c_1 b_1 + c_2 b_2 + \cdots + c_n b_n
$$

then the coordinates of $v$ in the basis $B$ are:

$$
[v]_B =
\begin{bmatrix}
c_1 \\
c_2 \\
\vdots \\
c_n
\end{bmatrix}
$$

The notation $[v]_B$ means "the coordinate vector of $v$ in the basis $B$."

## Change Of Basis Matrix

Suppose the vectors of $B$ are written in standard coordinates. Put them into a matrix as columns:

$$
P_B =
\begin{bmatrix}
| & | & & | \\
b_1 & b_2 & \cdots & b_n \\
| & | & & |
\end{bmatrix}
$$

Then $P_B$ converts $B$-coordinates into standard coordinates:

$$
v = P_B [v]_B
$$

To go from standard coordinates back to $B$-coordinates:

$$
[v]_B = P_B^{-1}v
$$

So $P_B$ moves from the new basis to the standard basis, while $P_B^{-1}$ moves from the standard basis to the new basis.

## Changing Between Two Bases

Suppose $B$ and $C$ are two bases.

To convert coordinates from basis $B$ to basis $C$:

$$
[v]_C = P_C^{-1}P_B[v]_B
$$

The matrix:

$$
P_C^{-1}P_B
$$

is the change of basis matrix from $B$-coordinates to $C$-coordinates.

## Linear Transformations In A New Basis

If a linear operator has matrix representation $A$ in the standard basis, then its matrix representation in the basis $B$ is:

$$
[A]_B = P_B^{-1} A P_B
$$

This formula has a natural order:

- $P_B$ converts input coordinates from the $B$ basis into standard coordinates.
- $A$ applies the operator in standard coordinates.
- $P_B^{-1}$ converts the output back into the $B$ basis.

Matrices related by:

$$
B = P^{-1}AP
$$

are called **similar matrices**. They represent the same linear operator in different bases.

## Connection To Diagonalization

[Diagonalization](Eigenvalues%20and%20Eigenvectors.md#Diagonalization) is a special case of change of basis.

If $A$ has enough independent eigenvectors, put those eigenvectors into a matrix $P$. Then:

$$
A = P D P^{-1}
$$

or equivalently:

$$
D = P^{-1} A P
$$

In the eigenvector basis, the operator becomes diagonal. This means the operator acts by simple scaling along each eigenvector direction.

## Intuition

Changing basis is like describing the same location with a different coordinate grid.

The object stays fixed, but the coordinate labels change. A matrix representation changes too because a matrix is not just the operator itself; it is the operator written in a chosen coordinate system.

## Common Confusions

- The vector $v$ and its coordinate vector $[v]_B$ are not the same thing. The first is the actual vector; the second is its description in basis $B$.
- The columns of $P_B$ are basis vectors written in standard coordinates.
- $P_B$ converts from $B$-coordinates to standard coordinates, not the other way around.
- Similar matrices can look different but describe the same linear operator in different bases.

## Related Concepts

- [Shankar: Active and Passive Transformations](../Book%20Notes/Shankar/Chapter%201/Active%20and%20Passive%20Transformations.md)
- [Linear Algebra](Linear%20Algebra.md)
- [Vector Spaces](Vector%20Spaces.md)
- [Vectors](Vectors.md)
- [Linear Operators](Linear%20Operators.md)
- [Matrices](Matrices.md)
- [Eigenvalues and Eigenvectors](Eigenvalues%20and%20Eigenvectors.md)
- [Unitary Operators](Unitary%20Matrices.md)
- [Singular Value Decomposition](Singular%20Value%20Decomposition.md)
