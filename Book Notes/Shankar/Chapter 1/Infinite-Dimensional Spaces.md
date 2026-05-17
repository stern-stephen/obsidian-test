# Infinite-Dimensional Spaces

Source: [Principles of Quantum Mechanics](../../../References/Principals%20of%20quantum%20mechanics%20Shankar%20.pdf)

Book hub: [Shankar](../Shankar.md)

Book section: 1.10.

## Reading Status

- Status: started
- Pages:
- Date started: 2026-05-17
- Date finished:

## Big Ideas

- Section 1.10 generalizes finite-dimensional vector-space ideas to spaces whose vectors are functions.
- A wavefunction can be understood as the coordinate representation of an abstract ket in a continuous basis.
- Sums over basis labels become integrals when the labels are continuous.
- The Dirac delta function plays the role of the Kronecker delta when basis labels become continuous.

## Notes

The finite-dimensional picture says:

$$
|v\rangle = \sum_i v_i |i\rangle
$$

where the numbers $v_i$ are the components of the vector in the chosen basis.

In an infinite-dimensional function space, the vector can have infinitely many components. For a discrete infinite basis:

$$
|f\rangle = \sum_{n=1}^{\infty} f_n |n\rangle
$$

For a continuous basis, the sum becomes an integral:

$$
|\psi\rangle = \int dx\, \psi(x)|x\rangle
$$

Here $\psi(x)$ is not the abstract vector itself. It is the coordinate representation of the abstract ket $|\psi\rangle$ in the $x$ basis:

$$
\psi(x) = \langle x|\psi\rangle
$$

This is one of the most important translations in quantum mechanics.

## Kronecker Delta To Dirac Delta

For a discrete orthonormal basis:

$$
\langle i|j\rangle = \delta_{ij}
$$

and:

$$
I = \sum_i |i\rangle\langle i|
$$

For a continuous position basis, these become:

$$
\langle x|x'\rangle = \delta(x - x')
$$

and:

$$
I = \int dx\, |x\rangle\langle x|
$$

The Dirac delta is not an ordinary function. It is a rule that extracts a value from an integral:

$$
\int dx'\, \delta(x - x')\psi(x') = \psi(x)
$$

That is why it acts like the continuous version of "same basis vector or different basis vector."

## How To Read This Section

The section can feel slippery because Shankar is changing what "vector" looks like without changing the underlying rules.

Keep this dictionary nearby:

| Finite-dimensional vectors | Infinite-dimensional / continuous version |
| --- | --- |
| column vector $v_i$ | function $\psi(x)$ |
| sum $\sum_i$ | integral $\int dx$ |
| basis vector $|i\rangle$ | position basis ket $|x\rangle$ |
| component $v_i = \langle i|v\rangle$ | wavefunction $\psi(x) = \langle x|\psi\rangle$ |
| Kronecker delta $\delta_{ij}$ | Dirac delta $\delta(x-x')$ |
| identity $\sum_i |i\rangle\langle i|$ | identity $\int dx\, |x\rangle\langle x|$ |

## Common Confusions

- A wavefunction $\psi(x)$ is not "more real" than a ket. It is the ket written in the position basis.
- The ket $|x\rangle$ is not a normalizable physical state in the usual sense. It is an idealized basis object used to represent states.
- The Dirac delta is not a spike-shaped ordinary function. In this setting, it is best treated by what it does under an integral.
- Infinite-dimensional spaces follow the same vector-space rules, but questions about convergence, domains, and normalization become more delicate.

## Study Questions

- What changes when the basis label $i$ becomes a continuous label $x$?
- Why does $\int dx\, |x\rangle\langle x|$ behave like the identity operator?
- Why is $\psi(x)=\langle x|\psi\rangle$ a coordinate representation rather than a different physical object?

## Links To Concept Notes

- [Infinite-Dimensional Vector Spaces](../../../Linear%20Algebra/Infinite-Dimensional%20Vector%20Spaces.md)
- [Dirac Delta Function](../../../Linear%20Algebra/Dirac%20Delta%20Function.md)
- [Bra-Ket Notation](../../../Linear%20Algebra/Bra-Ket%20Notation.md)
- [Linear Operators](../../../Linear%20Algebra/Linear%20Operators.md)
- [Projection Operators](../../../Linear%20Algebra/Projection%20Matrices.md)
- [Functions of Operators](Functions%20of%20Operators.md)
