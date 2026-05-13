# Bloch Sphere

## Overview

The **Bloch sphere** is a geometric picture of a single qubit state.

A general normalized qubit state can be written as:

$$
|\psi\rangle = \alpha|0\rangle + \beta|1\rangle
$$

where $\alpha$ and $\beta$ are complex numbers satisfying:

$$
|\alpha|^2 + |\beta|^2 = 1
$$

Because two states that differ only by a global phase represent the same physical state, every pure single-qubit state can also be written as:

$$
|\psi\rangle =
\cos\left(\frac{\theta}{2}\right)|0\rangle
+ e^{i\phi}\sin\left(\frac{\theta}{2}\right)|1\rangle
$$

The angles $\theta$ and $\phi$ locate a point on the unit sphere:

$$
\begin{aligned}
x &= \sin\theta\cos\phi \\
y &= \sin\theta\sin\phi \\
z &= \cos\theta
\end{aligned}
$$

## Intuition

The north pole represents $|0\rangle$, and the south pole represents $|1\rangle$. Points on the equator represent equal-probability superpositions, such as:

$$
\frac{|0\rangle + |1\rangle}{\sqrt{2}}
$$

The Bloch sphere turns an abstract two-dimensional complex vector into a three-dimensional geometric picture. Single-qubit unitary operations can be viewed as rotations of the sphere, while measurements along different axes are connected to the eigenvectors of the Pauli matrices.

## Related Concepts

- [Quantum Computing](Quantum%20Computing.md)
- [Quantum Mechanics](../Quantum%20Mechanics/Quantum%20Mechanics.md)
- [Vectors](../Linear%20Algebra/Vectors.md)
- [Bra-Ket Notation](../Linear%20Algebra/Bra-Ket%20Notation.md)
- [Eigenvalues](../Linear%20Algebra/Eigenvalues.md)
- [Unitary Matrices](../Linear%20Algebra/Unitary%20Matrices.md)
