# Canonical Equations

Source: [The Lazy Universe](../../../References/Coopersmith2017TheLazyUniverse.pdf)

Book hub: [Coopersmith](../Coopersmith.md)

Book section: 7.4, printed pages 150-155.

Previous: [Hamiltonian Coordinates and Optical Analogy](Hamiltonian%20Coordinates%20and%20Optical%20Analogy.md)

Next: [Phase Fluid](Phase%20Fluid.md)

## Reading Status

- Status: started
- Pages: 150-155
- Date started: 2026-07-05
- Date finished:

## Big Ideas

- The Hamiltonian is built from the transformed Lagrangian and becomes the central scalar function in Hamiltonian mechanics.
- Hamilton's equations are first-order equations for the paired variables $q_i$ and $p_i$.
- The equations place all time derivatives on the left and the algebraic Hamiltonian derivatives on the right.
- Coopersmith treats the simplicity of this form as the beginning of a new mechanics, not merely a computational trick.

## Hamiltonian Form

Starting from the Lagrangian and the conjugate momentum definition, Hamiltonian mechanics rewrites the dynamics in terms of:

$$
H(q,p,t)
$$

For many standard systems, this function equals the total energy. More generally, its defining role is to generate the phase-space motion.

## Hamilton's Canonical Equations

The canonical equations are:

$$
\dot{q}_i=\frac{\partial H}{\partial p_i}
$$

$$
\dot{p}_i=-\frac{\partial H}{\partial q_i}
$$

They replace the second-order Lagrange equations with a pair of first-order equations. This split is especially useful because it treats coordinates and momenta as dynamically linked but independent phase-space coordinates.

## Why Coopersmith Cares

Coopersmith emphasizes the form of the equations. The time changes are isolated on one side, while the right-hand sides are ordinary partial derivatives of one function, the Hamiltonian. This structure makes conservation laws, qualitative phase-space behavior, and later quantum analogies easier to see.

## Links To Concept Notes

- [Hamiltonian Mechanics](../../../Mechanics/Hamiltonian%20Mechanics.md)
- [Phase Space](../../../Mechanics/Phase%20Space.md)
- [Canonical Momentum](../../../Mechanics/Canonical%20Momentum.md)
- [Legendre Transforms](../../../Mathematics/Legendre%20Transforms.md)

<!-- semantic-edges
{"source":"Hamiltonian","relation":"DETERMINES","target":"Hamiltonian Time Evolution","evidence_heading":"Hamilton's Canonical Equations","evidence_summary":"The note gives Hamilton's equations, where partial derivatives of H determine the time evolution of q_i and p_i.","confidence":0.95}
{"source":"Hamiltonian Mechanics","relation":"REFORMULATES","target":"Lagrange Equations of Motion","evidence_heading":"Hamilton's Canonical Equations","evidence_summary":"Hamilton's equations replace the Lagrange equations with paired first-order equations for coordinates and momenta.","confidence":0.9}
{"source":"Hamiltonian Canonical Equations","relation":"ENABLES","target":"Conservation Laws","evidence_heading":"Why Coopersmith Cares","evidence_summary":"The note says the canonical form makes conservation laws and qualitative phase-space behavior easier to see.","confidence":0.86}
-->
