# Conservation Laws

## Overview

A conservation law says that some quantity remains constant during the motion.

## Common Conserved Quantities

- Energy
- Linear momentum
- Angular momentum
- Charge

## Symmetry Connection

Continuous symmetries lead to conserved quantities:

- Time-translation symmetry gives energy conservation.
- Spatial translation symmetry gives momentum conservation.
- Rotational symmetry gives angular momentum conservation.

The conserved quantity is the generator of the symmetry. In Hamiltonian mechanics, if $G$ generates a transformation and the Hamiltonian is unchanged by that transformation, then:

$$
\lbrace G,H\rbrace=0
$$

When $G$ has no explicit time dependence, this means:

$$
\frac{dG}{dt}=0
$$

## Hamiltonian Form

If a quantity $G$ has no explicit time dependence, then it is conserved when:

$$
\lbrace G,H\rbrace = 0
$$

## Quantum Bridge

In quantum mechanics, an observable associated with an operator $G$ is conserved when it commutes with the Hamiltonian, assuming no explicit time dependence:

$$
[G,H] = 0
$$

## Related Concepts

- [Goldstein Section 2.6](../Book%20Notes/Goldstein/Chapter%202/Conservation%20Theorems%20and%20Symmetry%20Properties.md)
- [Energy Function](Energy%20Function.md)
- [Poisson Brackets](Poisson%20Brackets.md)
- [Symmetries](Symmetries.md)
- [Hamiltonian Mechanics](Hamiltonian%20Mechanics.md)
- [Cyclic Coordinates](Cyclic%20Coordinates.md)
- [Commutators](../Linear%20Algebra/Commutators.md)

<!-- semantic-edges
{"source":"Symmetries","relation":"DETERMINES","target":"Conservation Laws","evidence_heading":"Symmetry Connection","evidence_summary":"The note lists time-translation, spatial-translation, and rotational symmetries as sources of energy, momentum, and angular momentum conservation.","confidence":0.95}
{"source":"Conserved Quantities","relation":"REPRESENTS","target":"Symmetry Generators","evidence_heading":"Symmetry Connection","evidence_summary":"The note states that the conserved quantity is the generator of the symmetry.","confidence":0.9}
{"source":"Poisson Brackets","relation":"ENABLES","target":"Conservation Laws","evidence_heading":"Hamiltonian Form","evidence_summary":"For a quantity with no explicit time dependence, the note gives the Poisson-bracket condition with the Hamiltonian as the conservation test.","confidence":0.9}
{"source":"Quantum Commutators","relation":"REFORMULATES","target":"Classical Conservation Tests","evidence_heading":"Quantum Bridge","evidence_summary":"The quantum bridge replaces the classical Poisson-bracket conservation condition with commutation with the Hamiltonian for observables with no explicit time dependence.","confidence":0.85}
-->
