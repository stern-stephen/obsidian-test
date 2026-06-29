# Infinite-Dimensional Vector Spaces

## Overview

An infinite-dimensional vector space is a vector space whose vectors require infinitely many basis coefficients.

Quantum mechanics needs these spaces because wavefunctions behave like vectors, and many physical quantities such as position have continuously many possible values.

## From Columns To Functions

In a finite-dimensional basis:

$$
|v\rangle = \sum_i v_i |i\rangle
$$

The components $v_i$ can be collected into a column vector.

In a function space, the "components" may be the values or expansion coefficients of a function. A function can therefore play the role of a vector.

For a continuous position basis:

$$
|\psi\rangle = \int dx \psi(x)|x\rangle
$$

where:

$$
\psi(x) = \langle x|\psi\rangle
$$

The function $\psi(x)$ is the representation of the abstract vector $|\psi\rangle$ in the position basis.

## Inner Products

For complex functions, the inner product usually has the form:

$$
\langle f|g\rangle = \int dx f^*(x)g(x)
$$

This is the continuous analogue of:

$$
\langle v|w\rangle = \sum_i v_i^*w_i
$$

## Operators On Functions

Operators can act on functions just as matrices act on column vectors.

Examples include multiplication:

$$
(X\psi)(x) = x\psi(x)
$$

and differentiation:

$$
(D\psi)(x) = \frac{d\psi}{dx}
$$

In quantum mechanics, position and momentum are represented by operators on wavefunctions.

## Operator Kernels

In finite dimensions, an operator $A$ is represented by matrix elements:

$$
A_{ij} = \langle i|A|j\rangle
$$

and acts on components by:

$$
w_i = \sum_j A_{ij}v_j
$$

In a continuous basis, the matrix elements become a kernel:

$$
A(x,x') = \langle x|A|x'\rangle
$$

and the sum becomes an integral:

$$
(A\psi)(x) = \int dx' A(x,x')\psi(x')
$$

The identity operator has kernel:

$$
I(x,x')=\delta(x-x')
$$

because:

$$
(I\psi)(x) = \int dx' \delta(x-x')\psi(x') = \psi(x)
$$

A multiplication operator, such as position, has kernel:

$$
\langle x|X|x'\rangle = x\delta(x-x')
$$

so:

$$
(X\psi)(x) = \int dx' x\delta(x-x')\psi(x') = x\psi(x)
$$

A derivative operator can be represented using a derivative of the delta function:

$$
D(x,x') = \frac{\partial}{\partial x}\delta(x-x')
$$

so:

$$
(D\psi)(x) = \int dx' \frac{\partial}{\partial x}\delta(x-x')\psi(x') = \frac{d\psi}{dx}
$$

The derivative here is with respect to the output variable $x$. This is why the sign differs from the identity $\int dx \delta'(x-a)f(x)=-f'(a)$, where the derivative is attached to the integration variable.

## Common Confusions

- A function can be a vector even though it is not an arrow.
- Infinite-dimensional spaces follow the same vector-space logic, but sums may become infinite sums or integrals.
- An operator kernel $A(x,x')$ is the continuous-basis version of a matrix $A_{ij}$.
- Multiplication operators are like diagonal matrices; derivative operators are not diagonal in the position basis.
- Some basis objects used in physics, such as $|x\rangle$, are idealized and are not normalizable vectors in the ordinary sense.

## Related Concepts

- [Vector Spaces](Vector%20Spaces.md)
- [Linear Operators](Linear%20Operators.md)
- [Bra-Ket Notation](Bra-Ket%20Notation.md)
- [Dirac Delta Function](Dirac%20Delta%20Function.md)
- [Shankar 1.10](../Book%20Notes/Shankar/Chapter%201/Infinite-Dimensional%20Spaces.md)

<!-- semantic-edges
{"source":"Infinite-Dimensional Vector Spaces","relation":"PART_OF","target":"Linear Algebra","evidence_heading":"Overview","evidence_summary":"This concept note belongs to the Linear Algebra area of the vault.","confidence":0.85}
{"source":"Infinite-Dimensional Vector Spaces","relation":"LINEAR_ALGEBRA_RELATED_TO","target":"Vector Spaces","evidence_heading":"Related Concepts","evidence_summary":"The note explicitly connects Infinite-Dimensional Vector Spaces with Vector Spaces in its discussion or related-note links.","confidence":0.75}
{"source":"Infinite-Dimensional Vector Spaces","relation":"LINEAR_ALGEBRA_RELATED_TO","target":"Linear Operators","evidence_heading":"Related Concepts","evidence_summary":"The note explicitly connects Infinite-Dimensional Vector Spaces with Linear Operators in its discussion or related-note links.","confidence":0.75}
{"source":"Infinite-Dimensional Vector Spaces","relation":"LINEAR_ALGEBRA_RELATED_TO","target":"Bra-Ket Notation","evidence_heading":"Related Concepts","evidence_summary":"The note explicitly connects Infinite-Dimensional Vector Spaces with Bra-Ket Notation in its discussion or related-note links.","confidence":0.75}
{"source":"Infinite-Dimensional Vector Spaces","relation":"LINEAR_ALGEBRA_RELATED_TO","target":"Dirac Delta Function","evidence_heading":"Related Concepts","evidence_summary":"The note explicitly connects Infinite-Dimensional Vector Spaces with Dirac Delta Function in its discussion or related-note links.","confidence":0.75}
-->
