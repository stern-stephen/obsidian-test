# Postulates Of Quantum Mechanics

## Overview

The postulates of quantum mechanics are the bridge between the linear algebra and the physical interpretation.

In the form used for quantum information, the core ideas are:

- States live in complex inner product spaces.
- Closed-system evolution is unitary.
- Measurements produce probabilistic outcomes and can change the state.
- Composite systems use tensor product state spaces.

## State Spaces

An isolated quantum system is associated with a complex vector space with an inner product.

A pure state is represented by a unit vector:

$$
|\psi\rangle
$$

with normalization:

$$
\langle \psi|\psi\rangle=1
$$

## Evolution

Closed-system evolution is represented by a unitary operator:

$$
|\psi'\rangle=U|\psi\rangle
$$

where:

$$
U^\dagger U=I
$$

Unitarity preserves inner products and therefore preserves total probability.

In Shankar's single-particle formulation, the continuous-time version is the Schrodinger equation:

$$
i\hbar \frac{d}{dt}|\psi(t)\rangle=H|\psi(t)\rangle
$$

## Measurement

Measurement is probabilistic. In the general measurement-operator formalism, outcome $m$ has probability:

$$
p(m)=\langle \psi|M_m^\dagger M_m|\psi\rangle
$$

See [Quantum Measurement](Quantum%20Measurement.md) for the reusable measurement note.

In Shankar's projective-measurement presentation, measuring an observable gives one of the corresponding Hermitian operator's eigenvalues, with probabilities determined by projection onto the eigenspaces.

## Composite Systems

The state space of a composite system is the tensor product of the subsystem state spaces:

$$
\mathcal{H}_{AB}=\mathcal{H}_A \otimes \mathcal{H}_B
$$

Tensor products make entangled states possible.

## Related Book Notes

- [Nielsen and Chuang: Postulates of Quantum Mechanics](../Book%20Notes/Nielsen%20Chuang/Chapter%202/Postulates%20of%20Quantum%20Mechanics.md)
- [Townsend: Stern-Gerlach Experiments](../Book%20Notes/Townsend/Chapter%201/Stern-Gerlach%20Experiments.md)
- [Shankar Chapter 4: The Postulates](../Book%20Notes/Shankar/Chapter%204/The%20Postulates.md)

## Related Concepts

- [Quantum Mechanics](Quantum%20Mechanics.md)
- [Quantum State Vector](Quantum%20State%20Vector.md)
- [Quantum Measurement](Quantum%20Measurement.md)
- [Schrodinger Equation](Schrodinger%20Equation.md)
- [Composite Quantum Systems](Composite%20Quantum%20Systems.md)
- [Tensor Products](../Linear%20Algebra/Tensor%20Products.md)
- [Inner Product Spaces](../Linear%20Algebra/Inner%20Product%20Spaces.md)
- [Unitary Operators](../Linear%20Algebra/Unitary%20Matrices.md)
- [Density Operators](Density%20Operators.md)

<!-- semantic-edges
{"source":"Postulates of Quantum Mechanics","relation":"REFORMULATES","target":"Linear Algebra","evidence_heading":"Overview","evidence_summary":"The note describes the postulates as the bridge between linear algebra and physical interpretation.","confidence":0.9}
{"source":"Quantum State Vector","relation":"REQUIRES","target":"Complex Inner Product Spaces","evidence_heading":"State Spaces","evidence_summary":"The note says an isolated quantum system is associated with a complex vector space with an inner product and a pure state is a normalized unit vector.","confidence":0.95}
{"source":"Unitary Operators","relation":"DETERMINES","target":"Closed-System Evolution","evidence_heading":"Evolution","evidence_summary":"The note states that closed-system evolution is represented by a unitary operator preserving inner products and total probability.","confidence":0.95}
{"source":"Quantum Measurement","relation":"DETERMINES","target":"Probabilistic Outcomes","evidence_heading":"Measurement","evidence_summary":"The note says measurement is probabilistic and gives the measurement-operator probability formula for outcome m.","confidence":0.9}
{"source":"Tensor Products","relation":"DETERMINES","target":"Composite Quantum Systems","evidence_heading":"Composite Systems","evidence_summary":"The note says the state space of a composite system is the tensor product of subsystem state spaces.","confidence":0.95}
-->
