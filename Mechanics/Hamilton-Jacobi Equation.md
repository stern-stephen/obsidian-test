# Hamilton-Jacobi Equation

## Overview

The Hamilton-Jacobi equation is a reformulation of Hamiltonian mechanics in terms of an action function $S(q,t)$.

Instead of solving directly for all trajectories, the method seeks a function whose derivatives encode the momenta and generate the motion.

## Definition

For Hamiltonian $H(q,p,t)$, the Hamilton-Jacobi equation is:

$$
\frac{\partial S}{\partial t}+H\left(q_i,\frac{\partial S}{\partial q_i},t\right)=0
$$

The momenta are recovered from:

$$
p_i=\frac{\partial S}{\partial q_i}
$$

## Intuition

The action function behaves like a surface label. Surfaces of constant $S$ are surfaces of common action. Mechanical trajectories can be viewed as rays crossing these surfaces, which explains why Hamilton-Jacobi theory is closely linked to geometrical optics.

## Optical And Quantum Bridge

Hamilton-Jacobi mechanics is to quantum wave mechanics roughly what geometrical optics is to wave optics: a short-wavelength or classical limit.

This is why the equation is a natural bridge to [Wave-Particle Duality](../Quantum%20Mechanics/Wave-Particle%20Duality.md) and the [Schrodinger Equation](../Quantum%20Mechanics/Schrodinger%20Equation.md).

## Common Confusions

- $S$ is not just the numerical value of the action along one already-known path; in Hamilton-Jacobi theory it is treated as a function whose derivatives carry dynamical information.
- The method does not eliminate Hamiltonian mechanics. It repackages it through a generating function.
- The optical analogy is structural, not a claim that classical particles literally are quantum waves.

## Related Concepts

- [Hamiltonian Mechanics](Hamiltonian%20Mechanics.md)
- [Canonical Transformations](Canonical%20Transformations.md)
- [Action Principle](Action%20Principle.md)
- [Phase Space](Phase%20Space.md)
- [Coopersmith Section 7.8](../Book%20Notes/Coopersmith/Chapter%207/Hamilton-Jacobi%20Equation.md)

<!-- semantic-edges
{"source":"Hamilton-Jacobi Equation","relation":"REFORMULATES","target":"Hamiltonian Mechanics","evidence_heading":"Overview","evidence_summary":"The note describes Hamilton-Jacobi theory as a reformulation of Hamiltonian mechanics using an action function.","confidence":0.95}
{"source":"Action Function","relation":"DETERMINES","target":"Canonical Momentum","evidence_heading":"Definition","evidence_summary":"The note recovers momenta from coordinate derivatives of S, p_i = partial S / partial q_i.","confidence":0.9}
{"source":"Hamilton-Jacobi Equation","relation":"MOTIVATES","target":"Wave-Particle Duality","evidence_heading":"Optical And Quantum Bridge","evidence_summary":"The note says Hamilton-Jacobi mechanics stands to quantum wave mechanics like geometrical optics stands to wave optics.","confidence":0.86}
-->
