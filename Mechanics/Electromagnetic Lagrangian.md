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

## Gauge Freedom

The electromagnetic potentials are not unique. A gauge transformation changes them by:

$$
\mathbf{A}'=\mathbf{A}+\nabla\chi
$$

$$
\phi'=\phi-\frac{\partial\chi}{\partial t}
$$

These changes leave the electric and magnetic fields unchanged:

$$
\mathbf{B}=\nabla\times\mathbf{A}
$$

$$
\mathbf{E}=-\nabla\phi-\frac{\partial\mathbf{A}}{\partial t}
$$

For the charged-particle Lagrangian, the transformed potentials give:

$$
L'=L+q\left(\dot{\mathbf{r}}\cdot\nabla\chi+\frac{\partial\chi}{\partial t}\right)
$$

The term in parentheses is the total derivative of $\chi(\mathbf{r}(t),t)$ along the particle path:

$$
\frac{d\chi}{dt}=\dot{\mathbf{r}}\cdot\nabla\chi+\frac{\partial\chi}{\partial t}
$$

So:

$$
L'=L+q\frac{d\chi}{dt}
$$

This is exactly the total-derivative freedom of the Lagrangian. The potentials and the displayed Lagrangian change, but the electromagnetic fields and the classical equations of motion do not.

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
{"source":"Gauge Transformation","relation":"PRESERVES","target":"Electromagnetic Fields","evidence_heading":"Gauge Freedom","evidence_summary":"The note shows that changing A by grad chi and phi by minus partial chi over partial t leaves E and B unchanged.","confidence":0.95}
{"source":"Gauge Transformation","relation":"CHANGES_BY","target":"Total Time Derivative of Lagrangian","evidence_heading":"Gauge Freedom","evidence_summary":"The note shows that the electromagnetic gauge transformation changes the charged-particle Lagrangian by q d chi / dt, a total derivative along the path.","confidence":0.95}
-->
