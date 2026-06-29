# The Schrodinger Equation

Source: [Principles of Quantum Mechanics](../../../References/Principals%20of%20quantum%20mechanics%20Shankar%20.pdf)

Book hub: [Shankar](../Shankar.md)

Book section: 4.3, pages 143-150.

Previous: [Discussion of Postulates I-III](Discussion%20of%20Postulates%20I-III.md)

## Reading Status

- Status: started
- Pages: 143-150

## Notes

Postulate IV gives the time development of the state vector. The abstract form is:

$$
i\hbar \frac{d}{dt}|\psi(t)\rangle=H|\psi(t)\rangle
$$

For a single particle in one dimension with Hamiltonian:

$$
H=\frac{P^2}{2m}+V(X)
$$

the position-basis form becomes the familiar wave equation:

$$
i\hbar \frac{\partial \psi(x,t)}{\partial t}=-\frac{\hbar^2}{2m}\frac{\partial^2 \psi(x,t)}{\partial x^2}+V(x)\psi(x,t)
$$

The Schrodinger equation is first order in time, so the state at one time determines the state at later times. The Hamiltonian is Hermitian, which preserves normalization during time evolution.

## Stationary States

When $H$ is time independent, energy eigenstates evolve by phase factors. If:

$$
H|E\rangle=E|E\rangle
$$

then:

$$
|E,t\rangle=e^{-iEt/\hbar}|E\rangle
$$

The overall phase does not change measurement probabilities for that single energy eigenstate, but relative phases between different energy components do matter.

## Links To Concept Notes

- [Schrodinger Equation](../../../Quantum%20Mechanics/Schrodinger%20Equation.md)
- [Postulates of Quantum Mechanics](../../../Quantum%20Mechanics/Postulates%20of%20Quantum%20Mechanics.md)
- [Quantum State Vector](../../../Quantum%20Mechanics/Quantum%20State%20Vector.md)
- [Hamiltonian Mechanics](../../../Mechanics/Hamiltonian%20Mechanics.md)
- [Hermitian Matrices and Operators](../../../Linear%20Algebra/Hermitian%20Matrices%20and%20Operators.md)

<!-- semantic-edges
{"source":"The Schrodinger Equation","relation":"PART_OF","target":"Shankar Chapter 4","evidence_heading":"Book metadata","evidence_summary":"This note is a source-specific section note in Shankar Chapter 4.","confidence":0.85}
{"source":"The Schrodinger Equation","relation":"SOURCE_CONTEXT_FOR","target":"Discussion of Postulates I-III","evidence_heading":"The Schrodinger Equation","evidence_summary":"This source note explicitly links its treatment to Discussion of Postulates I-III.","confidence":0.8}
{"source":"The Schrodinger Equation","relation":"SOURCE_CONTEXT_FOR","target":"Schrodinger Equation","evidence_heading":"Links To Concept Notes","evidence_summary":"This source note explicitly links its treatment to Schrodinger Equation.","confidence":0.8}
{"source":"The Schrodinger Equation","relation":"SOURCE_CONTEXT_FOR","target":"Postulates of Quantum Mechanics","evidence_heading":"Links To Concept Notes","evidence_summary":"This source note explicitly links its treatment to Postulates of Quantum Mechanics.","confidence":0.8}
{"source":"The Schrodinger Equation","relation":"SOURCE_CONTEXT_FOR","target":"Quantum State Vector","evidence_heading":"Links To Concept Notes","evidence_summary":"This source note explicitly links its treatment to Quantum State Vector.","confidence":0.8}
-->
