# The Postulates

Source: [Principles of Quantum Mechanics](../../../References/Principals%20of%20quantum%20mechanics%20Shankar%20.pdf)

Book hub: [Shankar](../Shankar.md)

Book section: 4.1, pages 115-116.

Previous: [Chapter Overview](Chapter%20Overview.md)

Next: [Discussion of Postulates I-III](Discussion%20of%20Postulates%20I-III.md)

## Reading Status

- Status: started
- Pages: 115-116

## Notes

Shankar states the postulates first for one particle in one spatial dimension and places them beside their Hamiltonian-mechanics analogues.

Classically, the state is a phase-space point $(x,p)$. Quantum mechanically, the state is a vector $|\psi(t)\rangle$ in a Hilbert space.

Classically, dynamical variables are functions $\omega(x,p)$. Quantum mechanically, observables are represented by Hermitian operators built from $X$ and $P$.

In the position basis, Shankar uses:

$$
\langle x|X|x'\rangle=x\delta(x-x')
$$

and:

$$
\langle x|P|x'\rangle=-i\hbar \delta'(x-x')
$$

Measurement of an observable yields one of its eigenvalues, with probabilities determined by the state's projection onto the corresponding eigenvectors. Time evolution is governed by:

$$
i\hbar \frac{d}{dt}|\psi(t)\rangle=H|\psi(t)\rangle
$$

## Links To Concept Notes

- [Postulates of Quantum Mechanics](../../../Quantum%20Mechanics/Postulates%20of%20Quantum%20Mechanics.md)
- [Quantum State Vector](../../../Quantum%20Mechanics/Quantum%20State%20Vector.md)
- [Quantum Measurement](../../../Quantum%20Mechanics/Quantum%20Measurement.md)
- [Schrodinger Equation](../../../Quantum%20Mechanics/Schrodinger%20Equation.md)
- [Hermitian Matrices and Operators](../../../Linear%20Algebra/Hermitian%20Matrices%20and%20Operators.md)

<!-- semantic-edges
{"source":"The Postulates","relation":"PART_OF","target":"Shankar Chapter 4","evidence_heading":"Book metadata","evidence_summary":"This note is a source-specific section note in Shankar Chapter 4.","confidence":0.85}
{"source":"The Postulates","relation":"SOURCE_CONTEXT_FOR","target":"Chapter Overview","evidence_heading":"The Postulates","evidence_summary":"This source note explicitly links its treatment to Chapter Overview.","confidence":0.8}
{"source":"The Postulates","relation":"SOURCE_CONTEXT_FOR","target":"Discussion of Postulates I-III","evidence_heading":"The Postulates","evidence_summary":"This source note explicitly links its treatment to Discussion of Postulates I-III.","confidence":0.8}
{"source":"The Postulates","relation":"SOURCE_CONTEXT_FOR","target":"Postulates of Quantum Mechanics","evidence_heading":"Links To Concept Notes","evidence_summary":"This source note explicitly links its treatment to Postulates of Quantum Mechanics.","confidence":0.8}
{"source":"The Postulates","relation":"SOURCE_CONTEXT_FOR","target":"Quantum State Vector","evidence_heading":"Links To Concept Notes","evidence_summary":"This source note explicitly links its treatment to Quantum State Vector.","confidence":0.8}
-->
