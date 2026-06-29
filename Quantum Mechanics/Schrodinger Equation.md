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
{"source":"Schrodinger Equation","relation":"PART_OF","target":"Quantum Mechanics","evidence_heading":"Overview","evidence_summary":"This concept note belongs to the Quantum Mechanics area of the vault.","confidence":0.85}
{"source":"Schrodinger Equation","relation":"QUANTUM_MECHANICS_RELATED_TO","target":"Shankar Chapter 4: The Schrodinger Equation","evidence_heading":"Related Book Notes","evidence_summary":"The note explicitly connects Schrodinger Equation with Shankar Chapter 4: The Schrodinger Equation in its discussion or related-note links.","confidence":0.75}
{"source":"Schrodinger Equation","relation":"QUANTUM_MECHANICS_RELATED_TO","target":"Quantum Mechanics","evidence_heading":"Related Concepts","evidence_summary":"The note explicitly connects Schrodinger Equation with Quantum Mechanics in its discussion or related-note links.","confidence":0.75}
{"source":"Schrodinger Equation","relation":"QUANTUM_MECHANICS_RELATED_TO","target":"Postulates of Quantum Mechanics","evidence_heading":"Related Concepts","evidence_summary":"The note explicitly connects Schrodinger Equation with Postulates of Quantum Mechanics in its discussion or related-note links.","confidence":0.75}
{"source":"Schrodinger Equation","relation":"QUANTUM_MECHANICS_RELATED_TO","target":"Quantum State Vector","evidence_heading":"Related Concepts","evidence_summary":"The note explicitly connects Schrodinger Equation with Quantum State Vector in its discussion or related-note links.","confidence":0.75}
-->
