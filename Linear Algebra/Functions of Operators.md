# Functions Of Operators

## Overview

A function of an operator is a new operator built from an old one.

This idea matters in quantum mechanics because time evolution, rotations, and many changes of basis are written using operator exponentials such as $e^{-iHt/\hbar}$.

## Polynomial Definition

If:

$$
f(x) = a_0 + a_1x + a_2x^2 + \cdots + a_nx^n
$$

then for a linear operator $A$:

$$
f(A) = a_0I + a_1A + a_2A^2 + \cdots + a_nA^n
$$

This definition uses only operations that already make sense for operators.

## Power Series

Many important functions are defined by power series. For example:

$$
e^A = I + A + \frac{A^2}{2!} + \frac{A^3}{3!} + \cdots
$$

This is the operator version of the scalar exponential series.

## Eigenvalue Shortcut

If $|a_i\rangle$ is an eigenvector of $A$:

$$
A|a_i\rangle = a_i|a_i\rangle
$$

then:

$$
f(A)|a_i\rangle = f(a_i)|a_i\rangle
$$

The operator function keeps the same eigenvectors and applies the scalar function to the eigenvalues.

## Spectral Form

When $A$ has an orthonormal eigenbasis:

$$
A = \sum_i a_i |a_i\rangle\langle a_i|
$$

then:

$$
f(A) = \sum_i f(a_i)|a_i\rangle\langle a_i|
$$

This form says: project onto each eigendirection, multiply that component by $f(a_i)$, and add the pieces back together.

## Common Confusions

- $f(A)$ usually does not mean applying $f$ entry-by-entry to a matrix representation.
- Diagonal matrices are special because applying $f$ to the diagonal entries is the same as applying $f$ to the eigenvalues.
- If the operator is not diagonalizable, defining $f(A)$ can require more care.

## Related Concepts

- [Linear Operators](Linear%20Operators.md)
- [Matrices](Matrices.md)
- [Eigenvalues and Eigenvectors](Eigenvalues%20and%20Eigenvectors.md)
- [Hermitian Matrices and Operators](Hermitian%20Matrices%20and%20Operators.md)
- [Unitary Matrices](Unitary%20Matrices.md)
- [Projection Operators](Projection%20Matrices.md)
- [Shankar 1.9](../Book%20Notes/Shankar/Chapter%201/Functions%20of%20Operators.md)

<!-- semantic-edges
{"source":"Functions of Operators","relation":"REFORMULATES","target":"Linear Operators","evidence_heading":"Overview","evidence_summary":"The note defines a function of an operator as a new operator built from an old one.","confidence":0.9}
{"source":"Operator Exponentials","relation":"EXAMPLE_OF","target":"Functions of Operators","evidence_heading":"Overview","evidence_summary":"The note cites operator exponentials such as e to the minus iHt over hbar as important functions of operators.","confidence":0.85}
{"source":"Power Series","relation":"ENABLES","target":"Functions of Operators","evidence_heading":"Power Series","evidence_summary":"The note defines functions such as the operator exponential by applying the scalar power series to an operator.","confidence":0.9}
{"source":"Eigenvalues","relation":"ENABLES","target":"Functions of Operators","evidence_heading":"Eigenvalue Shortcut","evidence_summary":"The note says if a vector is an eigenvector of A, then f(A) keeps the same eigenvector and applies f to the eigenvalue.","confidence":0.9}
{"source":"Spectral Form","relation":"DETERMINES","target":"Functions of Operators","evidence_heading":"Spectral Form","evidence_summary":"The note gives f(A) as the sum over projectors onto eigendirections weighted by f of the eigenvalues when A has an orthonormal eigenbasis.","confidence":0.9}
-->
