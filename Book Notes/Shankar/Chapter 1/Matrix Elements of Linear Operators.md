# Matrix Elements of Linear Operators

Source: [Principles of Quantum Mechanics](../../../References/Principals%20of%20quantum%20mechanics%20Shankar%20.pdf)

Book hub: [Shankar](../Shankar.md)

Book section: 1.6.

Previous: [Linear Operators](Linear%20Operators.md)

Next: [Active and Passive Transformations](Active%20and%20Passive%20Transformations.md)

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

## Exercise Answers

These are answer summaries for Shankar Chapter 1 exercises in this section. I am not reproducing the full problem statements here.

### Exercise 1.6.1

The matrix is:

$$
\Omega=
\begin{bmatrix}
0&0&1\\
1&0&0\\
0&1&0
\end{bmatrix}
$$

The columns tell us the images of the basis kets:

$$
\Omega|1\rangle=|2\rangle
$$

$$
\Omega|2\rangle=|3\rangle
$$

$$
\Omega|3\rangle=|1\rangle
$$

So $\Omega$ cyclically permutes the three basis vectors:

$$
|1\rangle\to |2\rangle\to |3\rangle\to |1\rangle
$$

For a general vector:

$$
|v\rangle=v_1|1\rangle+v_2|2\rangle+v_3|3\rangle
$$

the output is:

$$
\Omega|v\rangle=v_3|1\rangle+v_1|2\rangle+v_2|3\rangle
$$

### Exercise 1.6.2

Assume $\Omega$ and $\Lambda$ are Hermitian.

For the product:

$$
(\Omega\Lambda)^\dagger=\Lambda\Omega
$$

So $\Omega\Lambda$ is Hermitian only if:

$$
\Omega\Lambda=\Lambda\Omega
$$

For the symmetrized product:

$$
(\Omega\Lambda+\Lambda\Omega)^\dagger=\Omega\Lambda+\Lambda\Omega
$$

so it is Hermitian.

For the commutator:

$$
[\Omega,\Lambda]^\dagger=(\Omega\Lambda-\Lambda\Omega)^\dagger=\Lambda\Omega-\Omega\Lambda=-[\Omega,\Lambda]
$$

so $[\Omega,\Lambda]$ is anti-Hermitian.

Multiplying by $i$ makes it Hermitian:

$$
(i[\Omega,\Lambda])^\dagger=i[\Omega,\Lambda]
$$

### Exercise 1.6.3

Let $U$ and $V$ be unitary:

$$
U^\dagger U=I,\qquad V^\dagger V=I
$$

Then:

$$
(UV)^\dagger(UV)=V^\dagger U^\dagger UV=V^\dagger IV=V^\dagger V=I
$$

So $UV$ is unitary.

### Exercise 1.6.4

If $U$ is unitary, then:

$$
U^\dagger U=I
$$

Take determinants:

$$
\det(U^\dagger U)=\det I=1
$$

Using multiplicativity:

$$
\det(U^\dagger)\det(U)=1
$$

But:

$$
\det(U^\dagger)=(\det U)^*
$$

Therefore:

$$
(\det U)^*\det U=|\det U|^2=1
$$

So:

$$
|\det U|=1
$$

The determinant of a unitary matrix is a complex number of unit modulus:

$$
\det U=e^{i\theta}
$$

### Exercise 1.6.5

For the rotation matrix $R$, orthogonality means:

$$
R^TR=I
$$

Using:

$$
R=
\begin{bmatrix}
1&0&0\\
0&0&-1\\
0&1&0
\end{bmatrix}
$$

one finds:

$$
R^T=
\begin{bmatrix}
1&0&0\\
0&0&1\\
0&-1&0
\end{bmatrix}
$$

and direct multiplication gives:

$$
R^TR=I
$$

So the rotation operator is unitary; since its entries are real, it is also orthogonal.

### Exercise 1.6.6

For each proposed matrix, compute $U^\dagger U$. The columns are orthonormal, so:

$$
U^\dagger U=I
$$

Thus each matrix is unitary.

For the common two-dimensional example:

$$
U=\frac{1}{2}
\begin{bmatrix}
1+i&1-i\\
1-i&1+i
\end{bmatrix}
$$

the determinant is:

$$
\det U=i=e^{i\pi/2}
$$

For:

$$
V=\frac{1}{\sqrt{2}}
\begin{bmatrix}
1&i\\
i&1
\end{bmatrix}
$$

the determinant is:

$$
\det V=1=e^{i0}
$$

Neither matrix is Hermitian, because neither equals its own conjugate transpose.

## Links To Concept Notes

- [Matrices](../../../Linear%20Algebra/Matrices.md)
- [Linear Operators](../../../Linear%20Algebra/Linear%20Operators.md)
- [Adjoints](../../../Linear%20Algebra/Adjoints.md)
- [Hermitian Matrices and Operators](../../../Linear%20Algebra/Hermitian%20Matrices%20and%20Operators.md)
- [Unitary Matrices](../../../Linear%20Algebra/Unitary%20Matrices.md)
- [Bra-Ket Notation](../../../Linear%20Algebra/Bra-Ket%20Notation.md)
