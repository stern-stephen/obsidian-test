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
|\psi\rangle = \int dx\, \psi(x)|x\rangle
$$

where:

$$
\psi(x) = \langle x|\psi\rangle
$$

The function $\psi(x)$ is the representation of the abstract vector $|\psi\rangle$ in the position basis.

## Inner Products

For complex functions, the inner product usually has the form:

$$
\langle f|g\rangle = \int dx\, f^*(x)g(x)
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

## Common Confusions

- A function can be a vector even though it is not an arrow.
- Infinite-dimensional spaces follow the same vector-space logic, but sums may become infinite sums or integrals.
- Some basis objects used in physics, such as $|x\rangle$, are idealized and are not normalizable vectors in the ordinary sense.

## Related Concepts

- [Vector Spaces](Vector%20Spaces.md)
- [Linear Operators](Linear%20Operators.md)
- [Bra-Ket Notation](Bra-Ket%20Notation.md)
- [Dirac Delta Function](Dirac%20Delta%20Function.md)
- [Shankar 1.10](../Book%20Notes/Shankar/Chapter%201/Infinite-Dimensional%20Spaces.md)
