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

## Exercise Answers

These are answer summaries for Shankar Chapter 1 exercises in this section. I am not reproducing the full problem statements here.

### Exercise 1.8.1

For:

$$
\Omega=
\begin{bmatrix}
1&3&1\\
0&2&0\\
0&1&4
\end{bmatrix}
$$

the characteristic equation is:

$$
\det(\Omega-\omega I)=(1-\omega)(2-\omega)(4-\omega)=0
$$

So:

$$
\omega=1,2,4
$$

Normalized eigenvectors may be chosen as:

$$
|\omega=1\rangle=
\begin{bmatrix}
1\\
0\\
0
\end{bmatrix}
$$

$$
|\omega=2\rangle=\frac{1}{\sqrt{30}}
\begin{bmatrix}
5\\
2\\
-1
\end{bmatrix}
$$

$$
|\omega=4\rangle=\frac{1}{\sqrt{10}}
\begin{bmatrix}
1\\
0\\
3
\end{bmatrix}
$$

The matrix is not Hermitian, since $\Omega^\dagger\ne\Omega$. The eigenvectors are not mutually orthogonal.

### Exercise 1.8.2

For:

$$
\Omega=
\begin{bmatrix}
0&0&1\\
0&0&0\\
1&0&0
\end{bmatrix}
$$

the matrix is Hermitian. Its eigenvalues are:

$$
\omega=1,-1,0
$$

A normalized eigenbasis is:

$$
|\omega=1\rangle=\frac{1}{\sqrt{2}}
\begin{bmatrix}
1\\
0\\
1
\end{bmatrix}
$$

$$
|\omega=-1\rangle=\frac{1}{\sqrt{2}}
\begin{bmatrix}
1\\
0\\
-1
\end{bmatrix}
$$

$$
|\omega=0\rangle=
\begin{bmatrix}
0\\
1\\
0
\end{bmatrix}
$$

If $U$ has these eigenvectors as columns, then:

$$
U^\dagger\Omega U=
\begin{bmatrix}
1&0&0\\
0&-1&0\\
0&0&0
\end{bmatrix}
$$

up to the ordering of the eigenvectors.

### Exercise 1.8.3

For:

$$
\Omega=\frac{1}{2}
\begin{bmatrix}
2&0&0\\
0&3&-1\\
0&-1&3
\end{bmatrix}
$$

the first basis vector is already an eigenvector with eigenvalue $1$:

$$
\Omega
\begin{bmatrix}
1\\
0\\
0
\end{bmatrix}
=
\begin{bmatrix}
1\\
0\\
0
\end{bmatrix}
$$

The lower $2\times 2$ block has eigenvectors $(1,1)$ and $(1,-1)$ with eigenvalues $1$ and $2$. Thus:

$$
\omega_1=\omega_2=1,\qquad \omega_3=2
$$

One normalized eigenvector for $\omega=2$ is:

$$
|\omega=2\rangle=\frac{1}{\sqrt{2}}
\begin{bmatrix}
0\\
1\\
-1
\end{bmatrix}
$$

The $\omega=1$ eigenspace is two-dimensional. One orthonormal basis for it is:

$$
\begin{bmatrix}
1\\
0\\
0
\end{bmatrix},
\qquad
\frac{1}{\sqrt{2}}
\begin{bmatrix}
0\\
1\\
1
\end{bmatrix}
$$

Equivalently, it consists of all vectors orthogonal to the $\omega=2$ eigenvector:

$$
\left\{
\begin{bmatrix}
a\\
b\\
b
\end{bmatrix}
:a,b\in\mathbb{C}
\right\}
$$

### Exercise 1.8.4

For:

$$
\Omega=
\begin{bmatrix}
4&1\\
-1&2
\end{bmatrix}
$$

the characteristic equation is:

$$
\det(\Omega-\omega I)=(3-\omega)^2=0
$$

So both eigenvalues are:

$$
\omega_1=\omega_2=3
$$

But:

$$
\Omega-3I=
\begin{bmatrix}
1&1\\
-1&-1
\end{bmatrix}
$$

The eigenvalue equation gives:

$$
x+y=0
$$

so every eigenvector is proportional to:

$$
\begin{bmatrix}
1\\
-1
\end{bmatrix}
$$

There is only one independent eigenvector, even though the eigenvalue has algebraic multiplicity two. This is the example showing that an arbitrary matrix need not have a full eigenbasis.

### Exercise 1.8.5

For:

$$
\Omega=
\begin{bmatrix}
\cos\theta&\sin\theta\\
-\sin\theta&\cos\theta
\end{bmatrix}
$$

the columns are orthonormal, so:

$$
\Omega^\dagger\Omega=I
$$

Since the matrix is real, this is also:

$$
\Omega^T\Omega=I
$$

The characteristic equation gives:

$$
\omega=e^{i\theta},\quad e^{-i\theta}
$$

Corresponding normalized eigenvectors may be chosen as:

$$
|\omega=e^{i\theta}\rangle=\frac{1}{\sqrt{2}}
\begin{bmatrix}
1\\
i
\end{bmatrix}
$$

and:

$$
|\omega=e^{-i\theta}\rangle=\frac{1}{\sqrt{2}}
\begin{bmatrix}
1\\
-i
\end{bmatrix}
$$

They are orthogonal. If $U$ has these columns, then:

$$
U^\dagger\Omega U=
\begin{bmatrix}
e^{i\theta}&0\\
0&e^{-i\theta}
\end{bmatrix}
$$

### Exercise 1.8.6

If $\Omega$ is Hermitian or unitary, it has an orthonormal eigenbasis. Let $U$ be the unitary matrix whose columns are the eigenvectors. Then:

$$
U^\dagger\Omega U=
\begin{bmatrix}
\omega_1&0&\cdots&0\\
0&\omega_2&\cdots&0\\
\vdots&\vdots&\ddots&\vdots\\
0&0&\cdots&\omega_n
\end{bmatrix}
$$

The determinant is invariant under unitary change of basis, so:

$$
\det\Omega=\prod_i\omega_i
$$

The trace is also invariant, so:

$$
\operatorname{Tr}\Omega=\sum_i\omega_i
$$

### Exercise 1.8.7

For a $2\times 2$ Hermitian matrix, the two eigenvalues $\omega_1,\omega_2$ obey:

$$
\omega_1+\omega_2=\operatorname{Tr}\Omega
$$

and:

$$
\omega_1\omega_2=\det\Omega
$$

In Shankar's example, these invariants give:

$$
\omega_1+\omega_2=2
$$

and:

$$
\omega_1\omega_2=-3
$$

The roots are:

$$
\omega=3,-1
$$

Direct computation of $\det(\Omega-\omega I)=0$ gives the same two roots. The Hermitian assumption matters because it guarantees diagonalizability by a unitary matrix and real eigenvalues.

### Exercise 1.8.8

The matrices $M^i$ obey:

$$
M^iM^j+M^jM^i=2\delta_{ij}I
$$

For $i=j$:

$$
2(M^i)^2=2I
$$

so:

$$
(M^i)^2=I
$$

If $M^i|\omega\rangle=\omega|\omega\rangle$, then:

$$
(M^i)^2|\omega\rangle=\omega^2|\omega\rangle=|\omega\rangle
$$

so:

$$
\omega^2=1
$$

Thus the eigenvalues are $\pm 1$.

For $i\ne j$:

$$
M^iM^j=-M^jM^i
$$

Taking traces:

$$
\operatorname{Tr}(M^iM^jM^i)=-\operatorname{Tr}(M^j(M^i)^2)
$$

Using cyclicity and $(M^i)^2=I$ gives:

$$
\operatorname{Tr}M^j=-\operatorname{Tr}M^j
$$

so:

$$
\operatorname{Tr}M^j=0
$$

Since each $M^j$ has only $\pm1$ eigenvalues and trace zero, it must have equally many $+1$ and $-1$ eigenvalues. Therefore the dimension must be even. These matrices cannot be odd-dimensional.

### Exercise 1.8.9

Using:

$$
\mathbf{v}_a=\boldsymbol{\omega}\times\mathbf{r}_a
$$

the angular momentum is:

$$
\mathbf{L}=\sum_a m_a\mathbf{r}_a\times(\boldsymbol{\omega}\times\mathbf{r}_a)
$$

Use:

$$
\mathbf{A}\times(\mathbf{B}\times\mathbf{C})=\mathbf{B}(\mathbf{A}\cdot\mathbf{C})-\mathbf{C}(\mathbf{A}\cdot\mathbf{B})
$$

to get:

$$
\mathbf{L}=\sum_a m_a\left[r_a^2\boldsymbol{\omega}-\mathbf{r}_a(\mathbf{r}_a\cdot\boldsymbol{\omega})\right]
$$

In components:

$$
L_i=\sum_j M_{ij}\omega_j
$$

where:

$$
M_{ij}=\sum_a m_a(r_a^2\delta_{ij}-(r_a)_i(r_a)_j)
$$

The angular momentum and angular velocity are parallel only when $\boldsymbol{\omega}$ is an eigenvector of $M$.

The matrix $M$ is real symmetric, hence Hermitian:

$$
M_{ij}=M_{ji}=M_{ji}^*
$$

Therefore it has three orthogonal principal axes. These are found by diagonalizing $M$.

For a sphere, every direction is an eigendirection. The only matrix with every direction as an eigenvector is a scalar multiple of the identity:

$$
M=\lambda I
$$

So the three eigenvalues are equal.

### Exercise 1.8.10

For:

$$
\Omega=
\begin{bmatrix}
1&0&1\\
0&0&0\\
1&0&1
\end{bmatrix},
\qquad
\Lambda=
\begin{bmatrix}
2&1&1\\
1&0&-1\\
1&-1&2
\end{bmatrix}
$$

direct multiplication gives:

$$
[\Omega,\Lambda]=0
$$

So the Hermitian matrices can be simultaneously diagonalized.

Because $\Omega$ is degenerate but $\Lambda$ is not, diagonalize $\Lambda$ first. A common orthonormal eigenbasis is:

$$
|a\rangle=\frac{1}{\sqrt{2}}
\begin{bmatrix}
1\\
0\\
1
\end{bmatrix}
$$

$$
|b\rangle=\frac{1}{\sqrt{3}}
\begin{bmatrix}
1\\
1\\
-1
\end{bmatrix}
$$

$$
|c\rangle=\frac{1}{\sqrt{6}}
\begin{bmatrix}
1\\
-2\\
-1
\end{bmatrix}
$$

Their eigenvalues are:

$$
\Omega|a\rangle=2|a\rangle,\qquad \Omega|b\rangle=0,\qquad \Omega|c\rangle=0|c\rangle
$$

and:

$$
\Lambda|a\rangle=3|a\rangle,\qquad \Lambda|b\rangle=2|b\rangle,\qquad \Lambda|c\rangle=-|c\rangle
$$

If $U$ has these vectors as columns, then:

$$
U^\dagger\Omega U=\operatorname{diag}(2,0,0)
$$

and:

$$
U^\dagger\Lambda U=\operatorname{diag}(3,2,-1)
$$

up to column ordering.

### Exercise 1.8.11

For the coupled mass problem, the normal-mode eigenvectors are:

$$
|I\rangle=\frac{1}{\sqrt{2}}
\begin{bmatrix}
1\\
1
\end{bmatrix}
$$

and:

$$
|II\rangle=\frac{1}{\sqrt{2}}
\begin{bmatrix}
1\\
-1
\end{bmatrix}
$$

with frequencies:

$$
\omega_I=\sqrt{\frac{k}{m}},\qquad \omega_{II}=\sqrt{\frac{3k}{m}}
$$

The initial state $|1\rangle$ decomposes as:

$$
|1\rangle=\frac{1}{\sqrt{2}}|I\rangle+\frac{1}{\sqrt{2}}|II\rangle
$$

Thus:

$$
|x(t)\rangle=\frac{1}{\sqrt{2}}|I\rangle\cos\left(\sqrt{\frac{k}{m}}t\right)+\frac{1}{\sqrt{2}}|II\rangle\cos\left(\sqrt{\frac{3k}{m}}t\right)
$$

Projecting back onto the original basis:

$$
x_1(t)=\frac{1}{2}\left[\cos\left(\sqrt{\frac{k}{m}}t\right)+\cos\left(\sqrt{\frac{3k}{m}}t\right)\right]
$$

$$
x_2(t)=\frac{1}{2}\left[\cos\left(\sqrt{\frac{k}{m}}t\right)-\cos\left(\sqrt{\frac{3k}{m}}t\right)\right]
$$

This agrees with Shankar's propagator formula for the initial vector $(1,0)^T$.

### Exercise 1.8.12

Assume:

$$
|x(t)\rangle=U(t)|x(0)\rangle
$$

and:

$$
\frac{d^2}{dt^2}|x(t)\rangle=\Omega|x(t)\rangle
$$

Then:

$$
\frac{d^2U}{dt^2}|x(0)\rangle=\Omega U(t)|x(0)\rangle
$$

Since $|x(0)\rangle$ is arbitrary:

$$
\frac{d^2U}{dt^2}=\Omega U
$$

In the common eigenbasis of $\Omega$ and $U$, this becomes independent scalar equations:

$$
\frac{d^2U_i}{dt^2}=\Omega_i U_i
$$

For the coupled mass example, $\Omega_i=-\omega_i^2$, so:

$$
\frac{d^2U_i}{dt^2}=-\omega_i^2 U_i
$$

With $U_i(0)=1$ and zero initial velocity:

$$
U_i(t)=\cos(\omega_i t)
$$

Therefore:

$$
U(t)=\sum_i |i\rangle\langle i|\cos(\omega_i t)
$$

In the normal-mode basis:

$$
U(t)=
\begin{bmatrix}
\cos(\omega_I t)&0\\
0&\cos(\omega_{II} t)
\end{bmatrix}
$$

## Links To Concept Notes

- [Eigenvalues and Eigenvectors](../../../Linear%20Algebra/Eigenvalues%20and%20Eigenvectors.md)
- [Hermitian Matrices and Operators](../../../Linear%20Algebra/Hermitian%20Matrices%20and%20Operators.md)
- [Change of Basis](../../../Linear%20Algebra/Change%20of%20Basis.md)
- [Unitary Matrices](../../../Linear%20Algebra/Unitary%20Matrices.md)
- [Functions of Operators](Functions%20of%20Operators.md)
