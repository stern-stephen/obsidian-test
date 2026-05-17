# Postulates Of Quantum Mechanics

Source: [quantum-computation-and-quantum-information-nielsen-chuang](../../../References/quantum-computation-and-quantum-information-nielsen-chuang.pdf)

Book hub: [Nielsen And Chuang](../Nielsen%20Chuang.md)

Parent chapter: [Quantum Mechanics](Quantum%20Mechanics.md)

Book section: 2.2, pages 80-96.

## Overview

Section 2.2 gives the basic postulates of quantum mechanics in a form suitable for quantum information.

The postulates connect the linear algebra from [Linear Algebra](Linear%20Algebra.md) to physical interpretation: states are vectors, closed-system evolution is unitary, measurements are described by measurement operators, and composite systems use tensor products.

Reusable topic note: [Postulates of Quantum Mechanics](../../../Quantum%20Mechanics/Postulates%20of%20Quantum%20Mechanics.md).

## 2.2.1 State Space

An isolated quantum system is associated with a complex vector space with an inner product.

The state of the system is represented by a unit vector:

$$
|\psi\rangle
$$

The normalization condition is:

$$
\langle \psi|\psi\rangle = 1
$$

For a qubit, a general state can be written:

$$
|\psi\rangle = \alpha|0\rangle + \beta|1\rangle
$$

with:

$$
|\alpha|^2 + |\beta|^2 = 1
$$

The amplitudes $\alpha$ and $\beta$ are complex numbers. Their squared magnitudes become probabilities when the state is measured in the computational basis.

## 2.2.2 Evolution

The evolution of a closed quantum system is described by a unitary operator.

If the system starts in state $|\psi\rangle$, then after the evolution $U$ it is in state:

$$
|\psi'\rangle = U|\psi\rangle
$$

The operator $U$ must be unitary:

$$
U^\dagger U = I
$$

This preserves normalization and therefore preserves total probability.

Related note: [Unitary Matrices](../../../Linear%20Algebra/Unitary%20Matrices.md).

## 2.2.3 Quantum Measurement

Quantum measurements are described by a collection of measurement operators:

$$
\{M_m\}
$$

The index $m$ labels the possible measurement outcomes.

If the system is in state $|\psi\rangle$, then the probability of outcome $m$ is:

$$
p(m) = \langle \psi|M_m^\dagger M_m|\psi\rangle
$$

After observing outcome $m$, the new state is:

$$
\frac{M_m|\psi\rangle}{\sqrt{p(m)}}
$$

The measurement operators must satisfy the completeness relation:

$$
\sum_m M_m^\dagger M_m = I
$$

This guarantees that the total probability of all outcomes is $1$.

Reusable topic note: [Quantum Measurement](../../../Quantum%20Mechanics/Quantum%20Measurement.md).

## 2.2.4 Distinguishing Quantum States

Quantum states are not always perfectly distinguishable.

Orthogonal states can be reliably distinguished by an appropriate measurement. Non-orthogonal states cannot be distinguished with certainty in a single measurement.

This is one of the major differences between classical and quantum information. Classical states can often be read without disturbance; unknown quantum states cannot generally be identified perfectly.

## 2.2.5 Projective Measurements

Projective measurements are a special and important class of measurements.

A projective measurement is described by projectors $P_m$ satisfying:

$$
P_m P_n = \delta_{mn}P_m
$$

and:

$$
\sum_m P_m = I
$$

The probability of outcome $m$ is:

$$
p(m) = \langle \psi|P_m|\psi\rangle
$$

and the post-measurement state is:

$$
\frac{P_m|\psi\rangle}{\sqrt{p(m)}}
$$

Projective measurements are closely connected to [Hermitian operators](../../../Linear%20Algebra/Hermitian%20Matrices%20and%20Operators.md) and [eigenvalues](../../../Linear%20Algebra/Eigenvalues%20and%20Eigenvectors.md).

## 2.2.6 POVM Measurements

A POVM focuses on the probabilities of measurement outcomes rather than the full post-measurement state.

The POVM elements are:

$$
E_m = M_m^\dagger M_m
$$

They satisfy:

$$
\sum_m E_m = I
$$

and the probability of outcome $m$ is:

$$
p(m) = \langle \psi|E_m|\psi\rangle
$$

POVMs are useful when the main question is what outcome probabilities are possible, rather than what happens to the state afterward.

Reusable topic note: [Quantum Measurement](../../../Quantum%20Mechanics/Quantum%20Measurement.md#povms).

## 2.2.7 Phase

Global phase does not change the physical state.

The states:

$$
|\psi\rangle
$$

and:

$$
e^{i\theta}|\psi\rangle
$$

represent the same physical state.

Relative phase, however, can matter. For example:

$$
\frac{|0\rangle + |1\rangle}{\sqrt{2}}
$$

and:

$$
\frac{|0\rangle - |1\rangle}{\sqrt{2}}
$$

are physically different states.

## 2.2.8 Composite Systems

The state space of a composite quantum system is the tensor product of the state spaces of its parts.

For two systems with states $|\psi\rangle$ and $|\phi\rangle$, the combined state is:

$$
|\psi\rangle \otimes |\phi\rangle
$$

often written more compactly as:

$$
|\psi\rangle|\phi\rangle
$$

For two qubits, the computational basis is:

$$
|00\rangle,\ |01\rangle,\ |10\rangle,\ |11\rangle
$$

Composite systems allow entangled states, which cannot be written as a simple tensor product of individual subsystem states.

Reusable topic notes:

- [Composite Quantum Systems](../../../Quantum%20Mechanics/Composite%20Quantum%20Systems.md)
- [Tensor Products](../../../Linear%20Algebra/Tensor%20Products.md)
- [Entanglement](../../../Quantum%20Mechanics/Entanglement.md)

## 2.2.9 Global View

The postulates give a compact model for quantum information:

- States live in complex vector spaces.
- Closed-system evolution is unitary.
- Measurements are probabilistic.
- Composite systems use tensor products.
- Entanglement appears naturally in composite systems.

The rest of the chapter develops these tools through superdense coding, density operators, the Schmidt decomposition, and Bell inequalities.

## Questions To Revisit

- Why does unitarity fully characterize closed-system evolution?
- What information is lost when moving from measurement operators to POVMs?
- How should global phase be understood geometrically?
- Why does tensor product structure make entanglement possible?

## Related Concepts

- [Quantum Mechanics](../../../Quantum%20Mechanics/Quantum%20Mechanics.md)
- [Postulates of Quantum Mechanics](../../../Quantum%20Mechanics/Postulates%20of%20Quantum%20Mechanics.md)
- [Quantum Measurement](../../../Quantum%20Mechanics/Quantum%20Measurement.md)
- [Composite Quantum Systems](../../../Quantum%20Mechanics/Composite%20Quantum%20Systems.md)
- [Entanglement](../../../Quantum%20Mechanics/Entanglement.md)
- [Quantum Computing](../../../Quantum%20Computing/Quantum%20Computing.md)
- [Tensor Products](../../../Linear%20Algebra/Tensor%20Products.md)
- [Bra-Ket Notation](../../../Linear%20Algebra/Bra-Ket%20Notation.md)
- [Unitary Matrices](../../../Linear%20Algebra/Unitary%20Matrices.md)
- [Hermitian Matrices and Operators](../../../Linear%20Algebra/Hermitian%20Matrices%20and%20Operators.md)
- [Eigenvalues](../../../Linear%20Algebra/Eigenvalues%20and%20Eigenvectors.md)
