# Chapter 2 - Linear Algebra

Source: [[References/quantum-computation-and-quantum-information-nielsen-chuang.pdf]]

Book hub: [[Book Notes/Nielsen Chuang/Nielsen Chuang|Nielsen And Chuang]]

Parent chapter: [[Book Notes/Nielsen Chuang/Chapter 2 - Quantum Mechanics|Chapter 2 - Quantum Mechanics]]

Book section: 2.1, pages 61-79.

## Overview

Section 2.1 reviews the [[Linear Algebra/Linear Algebra|linear algebra]] needed for quantum mechanics.

The main theme is that quantum mechanics is built on complex vector spaces. Quantum states are vectors, physical transformations are linear operators, measurements are tied to eigenvalues and eigenvectors, and composite systems are described using tensor products.

## 2.1.1 Bases And Linear Independence

A vector space is a setting where vectors can be added and scaled.

In quantum mechanics the important vector spaces are usually over the complex numbers $\mathbb{C}$, so vectors may have complex coefficients.

A set of vectors spans a vector space if every vector in the space can be written as a linear combination of them:

$$
|v\rangle = \sum_i a_i |v_i\rangle
$$

A set is linearly independent if no vector in the set can be built from the others.

A **basis** is a linearly independent spanning set. Once a basis is chosen, every vector has coordinates in that basis.

Related notes:

- [[Linear Algebra/Vector Spaces|Vector Spaces]]
- [[Linear Algebra/Bra-Ket Notation|Bra-Ket Notation]]
- [[Linear Algebra/Gram-Schmidt|Gram-Schmidt]]

## 2.1.2 Linear Operators And Matrices

A **linear operator** maps vectors to vectors while preserving linear combinations.

If $A$ is linear, then:

$$
A\left(\sum_i a_i |v_i\rangle\right) = \sum_i a_i A|v_i\rangle
$$

Once a basis is chosen, a linear operator can be represented by a matrix.

If $A$ acts on basis vectors by:

$$
A|v_i\rangle = \sum_j A_{ji}|w_j\rangle
$$

then $A_{ji}$ is the matrix element in row $j$ and column $i$.

The identity operator leaves every vector unchanged:

$$
I|v\rangle = |v\rangle
$$

Related notes:

- [[Linear Algebra/Vector Spaces|Vector Spaces]]
- [[Linear Algebra/Adjoints|Adjoints]]
- [[Linear Algebra/Unitary Matrices|Unitary Matrices]]

## 2.1.3 The Pauli Matrices

The Pauli matrices are central examples of operators on a two-dimensional complex vector space:

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

They are important because they are both [[Linear Algebra/Hermitian Matrices and Operators|Hermitian]] and [[Linear Algebra/Unitary Matrices|unitary]].

Their eigenvalues and eigenvectors are collected in [[Linear Algebra/Eigenvalues#Pauli Matrices|Eigenvalues: Pauli Matrices]].

## 2.1.4 Inner Products

An inner product takes two vectors and produces a scalar.

In bra-ket notation, the inner product between $|\phi\rangle$ and $|\psi\rangle$ is:

$$
\langle \phi|\psi\rangle
$$

The inner product gives the length of a vector:

$$
\||\psi\rangle\| = \sqrt{\langle \psi|\psi\rangle}
$$

Two vectors are orthogonal when:

$$
\langle \phi|\psi\rangle = 0
$$

An orthonormal basis is a basis whose vectors have length $1$ and are mutually orthogonal:

$$
\langle i|j\rangle = \delta_{ij}
$$

The inner product is one of the main reasons complex conjugation appears throughout quantum mechanics.

Related notes:

- [[Linear Algebra/Vector Spaces|Vector Spaces]]
- [[Linear Algebra/Bra-Ket Notation|Bra-Ket Notation]]
- [[Linear Algebra/Gram-Schmidt|Gram-Schmidt]]

## 2.1.5 Eigenvectors And Eigenvalues

An eigenvector is a nonzero vector whose direction is preserved by an operator.

If $A$ is an operator, then:

$$
A|v\rangle = \lambda |v\rangle
$$

where $|v\rangle$ is the eigenvector and $\lambda$ is the eigenvalue.

Eigenvalues matter in quantum mechanics because measurement outcomes are tied to them. Hermitian operators are especially important because their eigenvalues are real.

Related notes:

- [[Linear Algebra/Eigenvalues|Eigenvalues]]
- [[Linear Algebra/Hermitian Matrices and Operators|Hermitian Matrices and Operators]]

## 2.1.6 Adjoints And Hermitian Operators

The adjoint of an operator $A$ is written:

$$
A^\dagger
$$

It is the operator that satisfies:

$$
\langle A v, w \rangle = \langle v, A^\dagger w \rangle
$$

A Hermitian operator equals its own adjoint:

$$
A = A^\dagger
$$

Hermitian operators are the mathematical model for observables in quantum mechanics.

Related notes:

- [[Linear Algebra/Adjoints|Adjoints]]
- [[Linear Algebra/Hermitian Matrices and Operators|Hermitian Matrices and Operators]]
- [[Quantum Mechanics/Quantum Mechanics|Quantum Mechanics]]

## 2.1.7 Tensor Products

Tensor products combine vector spaces.

If $|v\rangle$ belongs to one vector space and $|w\rangle$ belongs to another, their tensor product is written:

$$
|v\rangle \otimes |w\rangle
$$

or more compactly:

$$
|v\rangle|w\rangle
$$

Tensor products are essential for describing composite quantum systems.

For example, two qubits live in the tensor product of two two-dimensional spaces:

$$
\mathbb{C}^2 \otimes \mathbb{C}^2
$$

The combined space has dimension $4$.

This is the doorway into multi-qubit states and entanglement.

Related notes:

- [[Quantum Mechanics/Quantum Mechanics|Quantum Mechanics]]
- [[Quantum Computing/Quantum Computing|Quantum Computing]]
- [[Linear Algebra/Vector Spaces|Vector Spaces]]

## 2.1.8 Operator Functions

Functions can be applied to operators, especially when the operator has a useful diagonal form.

If:

$$
A = \sum_i \lambda_i |i\rangle\langle i|
$$

then a function $f$ can be applied to $A$ by applying it to the eigenvalues:

$$
f(A) = \sum_i f(\lambda_i)|i\rangle\langle i|
$$

This is useful for expressions such as exponentials of operators:

$$
e^A
$$

Operator exponentials appear naturally in quantum time evolution.

Related notes:

- [[Linear Algebra/Eigenvalues|Eigenvalues]]
- [[Linear Algebra/Hermitian Matrices and Operators|Hermitian Matrices and Operators]]
- [[Linear Algebra/Unitary Matrices|Unitary Matrices]]

## 2.1.9 Commutators And Anti-Commutators

The commutator of two operators $A$ and $B$ is:

$$
[A, B] = AB - BA
$$

The anti-commutator is:

$$
\{A, B\} = AB + BA
$$

Commutators measure the failure of two operators to commute.

If:

$$
[A, B] = 0
$$

then $A$ and $B$ commute.

In quantum mechanics, commutators are tied to compatibility of observables, uncertainty relations, and the algebraic structure of quantum operations.

## 2.1.10 Polar And Singular Value Decompositions

The polar decomposition factors an operator into a unitary part and a positive part.

At a high level, it is analogous to writing a complex number as:

$$
z = r e^{i\theta}
$$

where $r$ is the magnitude and $e^{i\theta}$ carries the phase.

The singular value decomposition factors a matrix into unitary matrices and a diagonal matrix of singular values:

$$
A = U D V^\dagger
$$

The important study takeaway is that many operators can be understood by separating their geometric action into simpler components: rotations, reflections, scalings, and projections.

Related notes:

- [[Linear Algebra/Unitary Matrices|Unitary Matrices]]
- [[Linear Algebra/Eigenvalues|Eigenvalues]]

## Study Takeaways

- Quantum states are vectors in complex vector spaces.
- Bra-ket notation makes vectors, dual vectors, and inner products compact.
- Operators become matrices after choosing a basis.
- Inner products define length, orthogonality, and normalization.
- Hermitian operators have real eigenvalues and model observables.
- Unitary operators preserve inner products and model reversible evolution.
- Tensor products build composite quantum systems.
- Commutators encode whether two operators can be applied in either order with the same result.

## Questions To Revisit

- How exactly does tensor product notation expand into basis vectors for two or more qubits?
- Why do Hermitian operators correspond to measurements rather than arbitrary operators?
- How does the operator exponential $e^{-iHt}$ become unitary?
- What is the physical interpretation of non-commuting observables?

## Links To Concept Notes

- [[Linear Algebra/Linear Algebra|Linear Algebra]]
- [[Linear Algebra/Vector Spaces|Vector Spaces]]
- [[Linear Algebra/Bra-Ket Notation|Bra-Ket Notation]]
- [[Linear Algebra/Adjoints|Adjoints]]
- [[Linear Algebra/Eigenvalues|Eigenvalues]]
- [[Linear Algebra/Hermitian Matrices and Operators|Hermitian Matrices and Operators]]
- [[Linear Algebra/Unitary Matrices|Unitary Matrices]]
- [[Quantum Mechanics/Quantum Mechanics|Quantum Mechanics]]
- [[Quantum Computing/Quantum Computing|Quantum Computing]]
