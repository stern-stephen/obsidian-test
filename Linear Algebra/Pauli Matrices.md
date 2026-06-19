# Pauli Matrices

## Overview

The **Pauli matrices** are three important $2 \times 2$ matrices used in quantum mechanics:

$$
\sigma_x =
\begin{bmatrix}
0 & 1 \\
1 & 0
\end{bmatrix}
$$

$$
\sigma_y =
\begin{bmatrix}
0 & -i \\
i & 0
\end{bmatrix}
$$

$$
\sigma_z =
\begin{bmatrix}
1 & 0 \\
0 & -1
\end{bmatrix}
$$

They are matrix representations of important spin operators for two-state quantum systems.

## Hermitian And Unitary

Each Pauli matrix is both **Hermitian** and **unitary**:

$$
\sigma_k^\dagger = \sigma_k
$$

and:

$$
\sigma_k^\dagger \sigma_k = I
$$

for $k \in \lbrace x, y, z\rbrace$.

Since they are Hermitian, their eigenvalues are real. Since they are unitary, their eigenvalues have absolute value $1$. Together, these facts force their eigenvalues to be:

$$
\lambda = \pm 1
$$

## Eigenvectors Of $\sigma_x$

For $\sigma_x$, the eigenvalue $1$ has normalized eigenvector:

$$
\frac{1}{\sqrt{2}}
\begin{bmatrix}
1 \\
1
\end{bmatrix}
$$

The eigenvalue $-1$ has normalized eigenvector:

$$
\frac{1}{\sqrt{2}}
\begin{bmatrix}
1 \\
-1
\end{bmatrix}
$$

One diagonalization is:

$$
\sigma_x =
\frac{1}{\sqrt{2}}
\begin{bmatrix}
1 & 1 \\
1 & -1
\end{bmatrix}
\begin{bmatrix}
1 & 0 \\
0 & -1
\end{bmatrix}
\frac{1}{\sqrt{2}}
\begin{bmatrix}
1 & 1 \\
1 & -1
\end{bmatrix}
$$

## Eigenvectors Of $\sigma_y$

For $\sigma_y$, the eigenvalue $1$ has normalized eigenvector:

$$
\frac{1}{\sqrt{2}}
\begin{bmatrix}
1 \\
i
\end{bmatrix}
$$

The eigenvalue $-1$ has normalized eigenvector:

$$
\frac{1}{\sqrt{2}}
\begin{bmatrix}
1 \\
-i
\end{bmatrix}
$$

One diagonalization is:

$$
\sigma_y =
\frac{1}{\sqrt{2}}
\begin{bmatrix}
1 & 1 \\
i & -i
\end{bmatrix}
\begin{bmatrix}
1 & 0 \\
0 & -1
\end{bmatrix}
\frac{1}{\sqrt{2}}
\begin{bmatrix}
1 & -i \\
1 & i
\end{bmatrix}
$$

## Eigenvectors Of $\sigma_z$

For $\sigma_z$, the eigenvalue $1$ has eigenvector:

$$
\begin{bmatrix}
1 \\
0
\end{bmatrix}
$$

The eigenvalue $-1$ has eigenvector:

$$
\begin{bmatrix}
0 \\
1
\end{bmatrix}
$$

The matrix $\sigma_z$ is already diagonal:

$$
\sigma_z =
\begin{bmatrix}
1 & 0 \\
0 & -1
\end{bmatrix}
$$

## Quantum Meaning

The Pauli matrices describe basic two-state quantum measurements, such as spin measurements along the $x$, $y$, and $z$ axes.

They are central examples because they connect several ideas at once:

- [Hermitian Operators](Hermitian%20Matrices%20and%20Operators.md), because they represent observables.
- [Unitary Operators](Unitary%20Matrices.md), because they preserve quantum-state normalization.
- [Eigenvalues and Eigenvectors](Eigenvalues%20and%20Eigenvectors.md), because their measurement outcomes are $\pm 1$.

## Related Concepts

- [Linear Algebra](Linear%20Algebra.md)
- [Linear Operators](Linear%20Operators.md)
- [Matrices](Matrices.md)
- [Eigenvalues and Eigenvectors](Eigenvalues%20and%20Eigenvectors.md)
- [Hermitian Operators](Hermitian%20Matrices%20and%20Operators.md)
- [Unitary Operators](Unitary%20Matrices.md)
- [Bra-Ket Notation](Bra-Ket%20Notation.md)
- [Quantum Mechanics](../Quantum%20Mechanics/Quantum%20Mechanics.md)
