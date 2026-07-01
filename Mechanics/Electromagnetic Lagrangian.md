# Electromagnetic Lagrangian

## Overview

The electromagnetic Lagrangian describes a charged particle interacting with scalar and vector potentials.

## Definition

For charge $q$ and mass $m$:

$$
L = \frac{1}{2}m\dot{\mathbf{r}}^2 - q\phi + q\dot{\mathbf{r}}\cdot\mathbf{A}
$$

The canonical momentum is:

$$
\mathbf{p} = m\dot{\mathbf{r}} + q\mathbf{A}
$$

The Hamiltonian is:

$$
H = \frac{1}{2m}(\mathbf{p} - q\mathbf{A})^2 + q\phi
$$

## Intuition

The vector potential shifts canonical momentum away from mechanical momentum. That shift is the classical root of minimal coupling.

## Related Concepts

- [Canonical Momentum](Canonical%20Momentum.md)
- [Lagrangian Mechanics](Lagrangian%20Mechanics.md)
- [Hamiltonian Mechanics](Hamiltonian%20Mechanics.md)
- [The Electromagnetic Lagrangian](../Book%20Notes/Shankar/Chapter%202/The%20Electromagnetic%20Lagrangian.md)

<!-- semantic-edges
{"source":"Electromagnetic Lagrangian","relation":"EXAMPLE_OF","target":"Lagrangian Mechanics","evidence_heading":"Overview","evidence_summary":"The note presents the electromagnetic Lagrangian as the Lagrangian for a charged particle interacting with scalar and vector potentials.","confidence":0.9}
{"source":"Electromagnetic Lagrangian","relation":"DETERMINES","target":"Canonical Momentum","evidence_heading":"Definition","evidence_summary":"The note gives the charged particle canonical momentum as mechanical momentum plus the charge times the vector potential.","confidence":0.95}
{"source":"Electromagnetic Lagrangian","relation":"DETERMINES","target":"Hamiltonian","evidence_heading":"Definition","evidence_summary":"The note gives the Hamiltonian obtained from the charged-particle electromagnetic Lagrangian in terms of canonical momentum and electromagnetic potentials.","confidence":0.9}
{"source":"Vector Potential","relation":"DETERMINES","target":"Canonical Momentum","evidence_heading":"Intuition","evidence_summary":"The note says the vector potential shifts canonical momentum away from mechanical momentum, which is the classical root of minimal coupling.","confidence":0.9}
-->
