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
{"source":"Shankar Section 4.3","relation":"INTRODUCES","target":"Schrodinger Equation","evidence_heading":"Notes","evidence_summary":"Introduces Postulate IV as the time development law for the quantum state vector.","confidence":0.92}
{"source":"Hamiltonian Operator","relation":"DETERMINES","target":"Quantum Time Evolution","evidence_heading":"Notes","evidence_summary":"The Hamiltonian acts as the generator in the abstract Schrodinger equation.","confidence":0.91}
{"source":"Position Basis","relation":"REPRESENTS","target":"Schrodinger Wave Equation","evidence_heading":"Notes","evidence_summary":"Converts the abstract state-vector equation into the familiar one-dimensional position-basis wave equation.","confidence":0.9}
{"source":"Hermitian Hamiltonian","relation":"ENABLES","target":"Normalization Preservation","evidence_heading":"Notes","evidence_summary":"Notes that Hermiticity of the Hamiltonian preserves normalization during time evolution.","confidence":0.89}
{"source":"Energy Eigenstates","relation":"DETERMINES","target":"Stationary State Phase Evolution","evidence_heading":"Stationary States","evidence_summary":"For a time-independent Hamiltonian, energy eigenstates evolve by phase factors while relative phases affect superpositions.","confidence":0.89}
-->
