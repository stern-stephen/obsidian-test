# Stern-Gerlach Experiments

Source: [A Modern Approach to Quantum Mechanics by John S. Townsend _2](../../../References/A%20Modern%20Approach%20to%20Quantum%20Mechanics%20by%20John%20S.%20Townsend%20_2.pdf)

Book hub: [Townsend](../Townsend.md)

Book chapter: 1, pages 1-28.

PDF reference: [Townsend PDF](../../../References/A%20Modern%20Approach%20to%20Quantum%20Mechanics%20by%20John%20S.%20Townsend%20_2.pdf). In this file, Townsend printed page 1 is PDF page 17.

## Reading Status

- Status: started
- Pages: 1-28
- Date started: 2026-05-13
- Date finished:

## Overview

Chapter 1 uses [Stern-Gerlach experiments](../../../Quantum%20Mechanics/Stern-Gerlach%20Experiments.md) to introduce quantum mechanics operationally.

Instead of starting with wave functions, Townsend starts with what idealized measurement devices do to beams of atoms. The central lesson is that quantum states carry probability amplitudes for different measurement arrangements, and sequential measurements can disturb the state in ways that classical filtering cannot explain.

## 1.1 The Original Stern-Gerlach Experiment

Book section: 1.1, pages 1-5.

The original Stern-Gerlach experiment sends silver atoms through an inhomogeneous magnetic field. A classical magnetic moment picture suggests a continuous spread of deflections, but the observed beam splits into discrete components.

For a spin-$1/2$ particle measured along the $z$ axis, the apparatus separates the beam into two possible outcomes:

$$
S_z = +\frac{\hbar}{2}
$$

and:

$$
S_z = -\frac{\hbar}{2}
$$

This motivates the notation:

$$
|+z\rangle,\quad |-z\rangle
$$

These are states with definite $z$-component of spin.

## 1.2 Four Experiments

Book section: 1.2, pages 5-10.

Townsend then considers a sequence of ideal Stern-Gerlach analyzers. The important point is not just that a single analyzer splits a beam, but that arranging analyzers in sequence reveals the state-changing role of measurement.

If a beam is filtered through an $S_z$ analyzer and only the $|+z\rangle$ output is kept, a second $S_z$ analyzer sends the whole beam through the $|+z\rangle$ channel.

But if an $S_x$ analyzer is inserted after preparing $|+z\rangle$, the beam splits into $|+x\rangle$ and $|-x\rangle$ components with equal probability. A later $S_z$ analyzer no longer behaves as if the earlier $S_z$ result was simply stored as a hidden classical property.

This is the first major warning: spin components along different axes cannot all be treated as simultaneously pre-existing classical values.

## 1.3 The Quantum State Vector

Book section: 1.3, pages 10-14.

The state vector collects the information needed to predict outcomes for future measurements.

For a spin-$1/2$ system, the state can be expanded in a basis associated with a measurement direction. For the $S_z$ basis:

$$
|\psi\rangle = c_+|+z\rangle + c_-|-z\rangle
$$

The coefficients are probability amplitudes. Their squared magnitudes give probabilities:

$$
P(+z) = |c_+|^2
$$

$$
P(-z) = |c_-|^2
$$

The normalization condition is:

$$
|c_+|^2 + |c_-|^2 = 1
$$

This connects directly to [bra-ket notation](../../../Linear%20Algebra/Bra-Ket%20Notation.md), where kets represent state vectors and bras represent dual vectors.

## 1.4 Analysis of Experiment 3

Book section: 1.4, pages 14-18.

Experiment 3 shows that a state prepared with definite $S_z$ does not have a definite value of $S_x$.

The relationship between the $z$-basis and $x$-basis states is expressed through superpositions:

$$
|+z\rangle =
\frac{1}{\sqrt{2}}|+x\rangle
+ \frac{1}{\sqrt{2}}|-x\rangle
$$

This equation says that a particle prepared as $|+z\rangle$ has equal probabilities for the two $S_x$ outcomes.

The reverse relationship is also useful:

$$
|+x\rangle =
\frac{1}{\sqrt{2}}|+z\rangle
+ \frac{1}{\sqrt{2}}|-z\rangle
$$

The important physical point is that measurement in the $x$ direction prepares the outgoing beam in an $S_x$ eigenstate. If a later $S_z$ analyzer is used, the probabilities reflect that new state, not the earlier preparation.

## 1.5 Experiment 5

Book section: 1.5, pages 18-21.

The fifth experiment introduces the role of relative phase.

Two beams may carry the same probabilities for a given measurement while still representing physically different states. The difference appears when the state is measured in another basis.

This is why amplitudes cannot be replaced by probabilities alone. The complex structure of the state vector contains interference information that becomes visible in later measurements.

## 1.6 Summary

Book section: 1.6, pages 21-24.

Chapter 1 builds a compact first model of quantum mechanics:

- Stern-Gerlach analyzers measure spin components.
- Spin-$1/2$ measurements along a given axis have two possible outcomes.
- Preparing a definite result for one axis does not prepare definite results for all axes.
- State vectors encode probability amplitudes, not just probabilities.
- Measurement generally changes the state.
- Relative phases matter because they affect later measurement outcomes.

## Problems

Book problems: pages 25-28.

The problems are likely useful for practicing:

- estimating Stern-Gerlach beam separations,
- translating analyzer sequences into state-vector language,
- computing probabilities from amplitudes,
- distinguishing classical filtering intuition from quantum measurement behavior.

## Questions To Revisit

- What assumptions about hidden classical spin values are ruled out by sequential Stern-Gerlach experiments?
- How does the apparatus both measure and prepare a state?
- Why are probability amplitudes more fundamental than probabilities in this chapter?
- Where does complex phase first become experimentally visible?

## Related Concepts

- [Stern-Gerlach Experiments](../../../Quantum%20Mechanics/Stern-Gerlach%20Experiments.md)
- [Quantum State Vector](../../../Quantum%20Mechanics/Quantum%20State%20Vector.md)
- [Spin-1/2 Systems](../../../Quantum%20Mechanics/Spin-1-2%20Systems.md)
- [Quantum Mechanics](../../../Quantum%20Mechanics/Quantum%20Mechanics.md)
- [Bra-Ket Notation](../../../Linear%20Algebra/Bra-Ket%20Notation.md)
- [Hermitian Matrices and Operators](../../../Linear%20Algebra/Hermitian%20Matrices%20and%20Operators.md)
