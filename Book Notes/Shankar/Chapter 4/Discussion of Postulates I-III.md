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

### Collapse Of The State Vector

Before measurement, the state can be a superposition of many possible outcomes for the observable being measured. If $\Omega$ has eigenstates $|\omega_n\rangle$, the state may be written as:

$$
|\psi\rangle=\sum_n c_n|\omega_n\rangle
$$

The coefficients $c_n$ are probability amplitudes. A measurement of $\Omega$ does not reveal all the coefficients. Instead, it produces one eigenvalue, say $\omega_k$, with probability:

$$
P(\omega_k)=|c_k|^2
$$

After that result is obtained, the state used for future predictions is no longer the original superposition. It is replaced by the eigenstate corresponding to the observed result:

$$
|\psi\rangle \rightarrow |\omega_k\rangle
$$

This replacement is what Shankar calls collapse of the state vector. It is a rule for updating the quantum state after a measurement outcome is obtained. The collapse is not ordinary time evolution under the Schrodinger equation; Schrodinger evolution is smooth and deterministic, while collapse is outcome-dependent and probabilistic.

The practical meaning is that measurement also prepares a new state. If a second measurement of the same observable is made immediately, it gives the same result because the first measurement left the system in an eigenstate of that observable. But a later measurement of an incompatible observable may have a spread of possible outcomes.

For an observable with degenerate eigenvalues, collapse is into the eigenspace associated with the measured eigenvalue rather than necessarily into one unique eigenvector.

Around page 122, Shankar's point is not that position and momentum can both be known arbitrarily well. A position measurement can be made so gentle that the momentum kick is small, but only by using a probe with poor position resolution. To know position sharply, the apparatus must localize the particle sharply, and that collapse produces a broad momentum spread. Conversely, a sharp momentum state is delocalized in position.

For approximate states, the tradeoff is summarized by:

$$
\Delta x \Delta p \geq \frac{\hbar}{2}
$$

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
