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
{"source":"Conservation Laws","relation":"PART_OF","target":"Mechanics","evidence_heading":"Overview","evidence_summary":"This concept note belongs to the Mechanics area of the vault.","confidence":0.85}
{"source":"Conservation Laws","relation":"MECHANICS_RELATED_TO","target":"Goldstein Section 2.6","evidence_heading":"Related Concepts","evidence_summary":"The note explicitly connects Conservation Laws with Goldstein Section 2.6 in its discussion or related-note links.","confidence":0.75}
{"source":"Conservation Laws","relation":"MECHANICS_RELATED_TO","target":"Energy Function","evidence_heading":"Related Concepts","evidence_summary":"The note explicitly connects Conservation Laws with Energy Function in its discussion or related-note links.","confidence":0.75}
{"source":"Conservation Laws","relation":"MECHANICS_RELATED_TO","target":"Poisson Brackets","evidence_heading":"Related Concepts","evidence_summary":"The note explicitly connects Conservation Laws with Poisson Brackets in its discussion or related-note links.","confidence":0.75}
{"source":"Conservation Laws","relation":"MECHANICS_RELATED_TO","target":"Symmetries","evidence_heading":"Related Concepts","evidence_summary":"The note explicitly connects Conservation Laws with Symmetries in its discussion or related-note links.","confidence":0.75}
-->
