# Spin-1/2 Systems

## Overview

A **spin-$1/2$ system** has two possible outcomes when one component of spin is measured.

For the $z$ component:

$$
S_z = +\frac{\hbar}{2}
$$

or:

$$
S_z = -\frac{\hbar}{2}
$$

The corresponding states are:

$$
|+z\rangle,\quad |-z\rangle
$$

## Basis States

The states $|+z\rangle$ and $|-z\rangle$ form a basis for the two-dimensional spin state space.

A general state can be written:

$$
|\psi\rangle = c_+|+z\rangle + c_-|-z\rangle
$$

Other measurement directions have their own basis states, such as:

$$
|+x\rangle,\quad |-x\rangle
$$

## Intuition

Spin-$1/2$ is the simplest nontrivial quantum system.

It is mathematically two-dimensional, but it already contains many essential quantum features:

- superposition,
- probabilistic measurement outcomes,
- incompatible measurements,
- relative phase,
- state preparation by measurement.

This is why Townsend begins quantum mechanics with [Stern-Gerlach experiments](Stern-Gerlach%20Experiments.md).

## Related Concepts

- [Quantum Mechanics](Quantum%20Mechanics.md)
- [Quantum State Vector](Quantum%20State%20Vector.md)
- [Stern-Gerlach Experiments](Stern-Gerlach%20Experiments.md)
- [Bra-Ket Notation](../Linear%20Algebra/Bra-Ket%20Notation.md)
- [Bloch Sphere](../Quantum%20Computing/Bloch%20Sphere.md)
- [Townsend Chapter 1](../Book%20Notes/Townsend/Chapter%201/Stern-Gerlach%20Experiments.md)

<!-- semantic-edges
{"source":"Spin-1/2 Systems","relation":"SPECIALIZES","target":"Quantum State Vector","evidence_heading":"Basis States","evidence_summary":"The note writes a spin-1/2 state as a two-component superposition in the spin basis.","confidence":0.9}
{"source":"Spin-1/2 Systems","relation":"INTRODUCES","target":"Basis States","evidence_heading":"Basis States","evidence_summary":"The note identifies |+z> and |-z> as a basis for the two-dimensional spin state space and notes other measurement-direction bases.","confidence":0.85}
{"source":"Quantum Superposition","relation":"REPRESENTS","target":"Spin-1/2 States","evidence_heading":"Basis States","evidence_summary":"The note writes a general spin state as a linear combination of spin-up and spin-down basis states.","confidence":0.85}
{"source":"Spin-1/2 Systems","relation":"INTRODUCES","target":"Incompatible Observables","evidence_heading":"Intuition","evidence_summary":"The note lists incompatible measurements as an essential quantum feature already present in spin-1/2 systems.","confidence":0.85}
{"source":"Stern-Gerlach Experiments","relation":"MOTIVATES","target":"Spin-1/2 Systems","evidence_heading":"Intuition","evidence_summary":"The note says Townsend begins quantum mechanics with Stern-Gerlach experiments because spin-1/2 exposes essential quantum features.","confidence":0.85}
-->
