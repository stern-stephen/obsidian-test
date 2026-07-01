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
{"source":"Shankar Section 4.1","relation":"INTRODUCES","target":"One-Dimensional Quantum Postulates","evidence_heading":"Notes","evidence_summary":"States the postulates for one particle in one spatial dimension and compares them to Hamiltonian mechanics.","confidence":0.92}
{"source":"Quantum State Vector","relation":"CONTRASTS_WITH","target":"Classical Phase-Space Point","evidence_heading":"Notes","evidence_summary":"Compares the quantum state vector in Hilbert space with the classical state as a phase-space point.","confidence":0.9}
{"source":"Shankar Section 4.1","relation":"INTRODUCES","target":"Hermitian-Operator Observables","evidence_heading":"Notes","evidence_summary":"States that quantum observables are represented by Hermitian operators built from X and P.","confidence":0.9}
{"source":"Measurement Eigenvalue Postulate","relation":"DETERMINES","target":"Measurement Outcomes","evidence_heading":"Notes","evidence_summary":"Measurement of an observable yields one of its eigenvalues with probabilities determined by projection onto eigenvectors.","confidence":0.91}
{"source":"Shankar Section 4.1","relation":"INTRODUCES","target":"Schrodinger Time-Evolution Postulate","evidence_heading":"Notes","evidence_summary":"Gives the abstract time-evolution postulate for the state vector under the Hamiltonian.","confidence":0.9}
-->
