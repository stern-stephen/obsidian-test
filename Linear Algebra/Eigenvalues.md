# Eigenvalues

## Overview

An **eigenvector** of a matrix is a nonzero vector whose direction is preserved by the matrix.

If $A$ is a matrix, $v$ is a nonzero vector, and $\lambda$ is a scalar, then $v$ is an eigenvector of $A$ with eigenvalue $\lambda$ when:

$$
A v = \lambda v
$$

The matrix $A$ may stretch, shrink, flip, or rotate other vectors, but on an eigenvector it acts like simple scalar multiplication.

## Meaning

The eigenvalue $\lambda$ tells how the eigenvector changes:

- If $\lambda > 1$, the vector is stretched.
- If $0 < \lambda < 1$, the vector is shrunk.
- If $\lambda = 1$, the vector is unchanged.
- If $\lambda = -1$, the vector is flipped.
- If $\lambda$ is complex, the transformation may include a phase change or rotation.

Eigenvalues and eigenvectors reveal the special directions where a linear transformation has its simplest behavior.

## Finding Eigenvalues

To find eigenvalues, rewrite the eigenvalue equation:

$$
A v = \lambda v
$$

as:

$$
(A - \lambda I)v = 0
$$

For this equation to have a nonzero solution $v$, the matrix $A - \lambda I$ must be singular:

$$
\det(A - \lambda I) = 0
$$

This determinant equation is called the **characteristic equation**.

## Diagonalization

A matrix is **diagonalizable** when it has enough linearly independent eigenvectors to form a basis.

If $A$ has eigenvectors $v_1, v_2, \ldots, v_n$ with eigenvalues $\lambda_1, \lambda_2, \ldots, \lambda_n$, then:

$$
A = P D P^{-1}
$$

where $P$ is the matrix whose columns are the eigenvectors, and $D$ is a diagonal matrix containing the eigenvalues:

$$
D =
\begin{bmatrix}
\lambda_1 & 0 & \cdots & 0 \\
0 & \lambda_2 & \cdots & 0 \\
\vdots & \vdots & \ddots & \vdots \\
0 & 0 & \cdots & \lambda_n
\end{bmatrix}
$$

Diagonalization is useful because diagonal matrices are much easier to understand and compute with.

## Hermitian Matrices

For [[Hermitian Matrices and Operators]], eigenvalues are always real.

If $A$ is Hermitian and $A v = \lambda v$, then:

$$
\lambda = \frac{\langle A v, v \rangle}{\langle v, v \rangle}
$$

The expression on the right is real for a Hermitian matrix, so $\lambda$ must be real.

Eigenvectors with different eigenvalues are orthogonal. If $A v = \lambda v$ and $A w = \mu w$, where $\lambda \ne \mu$, then:

$$
\langle v, w \rangle = 0
$$

This means a Hermitian matrix has a clean geometry: its eigenvectors point in mutually perpendicular directions.

A Hermitian matrix can be written using an orthonormal basis of eigenvectors:

$$
A = U \Lambda U^\dagger
$$

where $U$ is a unitary matrix whose columns are eigenvectors, and $\Lambda$ is a diagonal matrix containing the eigenvalues. This is the **spectral theorem** for Hermitian matrices.

The orthonormal eigenvector basis can be understood using ideas from [[Vector Spaces]] and [[Gram-Schmidt]].

## Unitary Matrices

For [[Unitary Matrices]], eigenvalues lie on the complex unit circle.

If $U$ is unitary and $Uv = \lambda v$ for a nonzero vector $v$, then:

$$
|\lambda| = 1
$$

This means unitary matrices may change direction or phase, but their eigenvalues cannot stretch or shrink eigenvectors.

Examples of possible unitary eigenvalues include:

- $1$
- $-1$
- $i$
- $e^{i\theta}$

## Pauli Matrices

The **Pauli matrices** are three important $2 \times 2$ matrices:

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

Each Pauli matrix is both Hermitian and unitary. Since they are Hermitian, their eigenvalues are real. Since they are unitary, their eigenvalues have absolute value $1$. Together, these facts force their eigenvalues to be:

$$
\lambda = \pm 1
$$

### Eigenvectors Of $\sigma_x$

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

### Eigenvectors Of $\sigma_y$

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

### Eigenvectors Of $\sigma_z$

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

## Related Concepts

- [[Linear Algebra]]
- [[Vector Spaces]]
- [[Adjoints]]
- [[Bra-Ket Notation]]
- [[Gram-Schmidt]]
- [[Hermitian Matrices and Operators]]
- [[Unitary Matrices]]
- [[Quantum Mechanics]]
