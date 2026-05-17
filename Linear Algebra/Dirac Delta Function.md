# Dirac Delta Function

## Overview

The Dirac delta function $\delta(x-a)$ is best understood by what it does inside an integral.

It extracts the value of a function at a point:

$$
\int dx\, \delta(x-a)f(x) = f(a)
$$

It is not an ordinary function in the usual sense. It is a distribution, or generalized function.

## Continuous Version Of The Kronecker Delta

For a discrete orthonormal basis:

$$
\langle i|j\rangle = \delta_{ij}
$$

where $\delta_{ij}=1$ if $i=j$ and $0$ otherwise.

For a continuous basis:

$$
\langle x|x'\rangle = \delta(x-x')
$$

This says that two position basis kets are orthogonal unless their labels match, but the continuous case needs the delta distribution instead of ordinary $0$ and $1$ values.

## Identity Operator

In a discrete basis:

$$
I = \sum_i |i\rangle\langle i|
$$

In a continuous basis:

$$
I = \int dx\, |x\rangle\langle x|
$$

Acting on a state:

$$
\int dx\, |x\rangle\langle x|\psi\rangle
= \int dx\, \psi(x)|x\rangle
= |\psi\rangle
$$

## Common Confusions

- $\delta(x-a)$ is not a finite-height spike with area $1$. Treating it that way can be useful as intuition, but the integral rule is the reliable definition.
- $\delta(0)$ is not an ordinary number.
- The delta function appears naturally when an orthonormal basis has a continuous label.

## Related Concepts

- [Infinite-Dimensional Vector Spaces](Infinite-Dimensional%20Vector%20Spaces.md)
- [Bra-Ket Notation](Bra-Ket%20Notation.md)
- [Projection Operators](Projection%20Matrices.md)
- [Shankar 1.10](../Book%20Notes/Shankar/Chapter%201/Infinite-Dimensional%20Spaces.md#kronecker-delta-to-dirac-delta)
