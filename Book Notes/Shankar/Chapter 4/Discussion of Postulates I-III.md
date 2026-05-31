# Discussion of Postulates I-III

Source: [Principles of Quantum Mechanics](../../../References/Principals%20of%20quantum%20mechanics%20Shankar%20.pdf)

Book hub: [Shankar](../Shankar.md)

Book section: 4.2, pages 116-142.

Previous: [The Postulates](The%20Postulates.md)

Next: [The Schrodinger Equation](The%20Schrodinger%20Equation.md)

## Reading Status

- Status: started
- Pages: 116-142

## Notes

The first three postulates describe the state of the system at a given time and how measurements extract information from it.

The state vector is a probability-amplitude object. In the position basis, its components are the wavefunction:

$$
\psi(x)=\langle x|\psi\rangle
$$

The probability density for position is:

$$
P(x)=|\psi(x)|^2
$$

The same state can be expanded in any observable's eigenbasis. If $|\omega\rangle$ is an eigenstate of the observable $\Omega$, then the amplitude for the outcome $\omega$ is:

$$
\langle \omega|\psi\rangle
$$

and the probability is proportional to:

$$
|\langle \omega|\psi\rangle|^2
$$

## Measurement And Collapse

If measurement of $\Omega$ gives the eigenvalue $\omega$, the state is projected into the corresponding eigenstate or eigenspace. The post-measurement state is therefore not just updated knowledge in the classical sense; the state used for later predictions changes.

Repeated immediate measurement of the same observable gives the same result, because the first measurement prepares an eigenstate of that observable.

## Compatible Observables

Two observables that commute can have simultaneous eigenstates. In that case, one can prepare a state with definite values for both observables.

Noncommuting observables cannot generally be assigned simultaneous sharp values. This is the operator-language seed of uncertainty relations.

## Expectation Values

The expectation value of an observable $\Omega$ in state $|\psi\rangle$ is:

$$
\langle \Omega \rangle=\langle \psi|\Omega|\psi\rangle
$$

This is an average over many identically prepared systems, not the value possessed by a single system before measurement.

## Links To Concept Notes

- [Quantum State Vector](../../../Quantum%20Mechanics/Quantum%20State%20Vector.md)
- [Quantum Measurement](../../../Quantum%20Mechanics/Quantum%20Measurement.md)
- [Postulates of Quantum Mechanics](../../../Quantum%20Mechanics/Postulates%20of%20Quantum%20Mechanics.md)
- [Commutators](../../../Linear%20Algebra/Commutators.md)
- [Projection Matrices](../../../Linear%20Algebra/Projection%20Matrices.md)
