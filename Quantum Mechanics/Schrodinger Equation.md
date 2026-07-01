# Schrodinger Equation

## Overview

The Schrodinger equation is the quantum time-evolution law for a state vector.

In abstract ket form:

$$
i\hbar \frac{d}{dt}|\psi(t)\rangle=H|\psi(t)\rangle
$$

Here $H$ is the Hamiltonian operator.

## Position-Basis Form

For a particle in one dimension with:

$$
H=\frac{P^2}{2m}+V(X)
$$

the position-space wavefunction obeys:

$$
i\hbar \frac{\partial \psi(x,t)}{\partial t}=-\frac{\hbar^2}{2m}\frac{\partial^2 \psi(x,t)}{\partial x^2}+V(x)\psi(x,t)
$$

## Intuition

The equation evolves probability amplitudes, not ordinary probabilities directly. Because the Hamiltonian is Hermitian, the evolution preserves total probability.

For time-independent $H$, energy eigenstates are especially simple:

$$
H|E\rangle=E|E\rangle
$$

and their time dependence is a phase:

$$
|E,t\rangle=e^{-iEt/\hbar}|E\rangle
$$

## Related Book Notes

- [Shankar Chapter 4: The Schrodinger Equation](../Book%20Notes/Shankar/Chapter%204/The%20Schrodinger%20Equation.md)

## Related Concepts

- [Quantum Mechanics](Quantum%20Mechanics.md)
- [Postulates of Quantum Mechanics](Postulates%20of%20Quantum%20Mechanics.md)
- [Quantum State Vector](Quantum%20State%20Vector.md)
- [Hamiltonian Mechanics](../Mechanics/Hamiltonian%20Mechanics.md)
- [Hermitian Matrices and Operators](../Linear%20Algebra/Hermitian%20Matrices%20and%20Operators.md)

<!-- semantic-edges
{"source":"Schrodinger Equation","relation":"DETERMINES","target":"Quantum Time Evolution","evidence_heading":"Overview","evidence_summary":"The note defines the Schrodinger equation as the quantum time-evolution law for a state vector.","confidence":0.95}
{"source":"Schrodinger Equation","relation":"REQUIRES","target":"Hamiltonian Operator","evidence_heading":"Overview","evidence_summary":"The abstract ket form of the Schrodinger equation uses the Hamiltonian operator H to generate time evolution.","confidence":0.9}
{"source":"Position-Basis Schrodinger Equation","relation":"SPECIALIZES","target":"Schrodinger Equation","evidence_heading":"Position-Basis Form","evidence_summary":"The note gives the one-dimensional position-space wavefunction form for a Hamiltonian with kinetic and potential energy terms.","confidence":0.9}
{"source":"Hermitian Hamiltonian","relation":"ENABLES","target":"Probability Conservation","evidence_heading":"Intuition","evidence_summary":"The note says the Hamiltonian being Hermitian makes evolution preserve total probability.","confidence":0.9}
{"source":"Energy Eigenstates","relation":"ENABLES","target":"Stationary Time Evolution","evidence_heading":"Intuition","evidence_summary":"The note says that for time-independent H, energy eigenstates acquire only a phase factor over time.","confidence":0.9}
-->
