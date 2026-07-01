# Classical Mechanics

## Overview

Classical mechanics describes the motion of particles and systems using positions, velocities, momenta, forces, energy, and variational principles.

## Main Formulations

- Newtonian mechanics emphasizes forces and acceleration.
- Lagrangian mechanics emphasizes the action of paths in configuration space.
- Hamiltonian mechanics emphasizes phase-space evolution using coordinates and conjugate momenta.

## Key Equations

Newton's second law:

$$
\mathbf{F} = m\mathbf{a}
$$

Euler-Lagrange equations:

$$
\frac{d}{dt}\frac{\partial L}{\partial \dot{q}_i} - \frac{\partial L}{\partial q_i} = 0
$$

Hamilton's equations:

$$
\dot{q}_i = \frac{\partial H}{\partial p_i}
$$

$$
\dot{p}_i = -\frac{\partial H}{\partial q_i}
$$

## Quantum Bridge

Quantum mechanics keeps many classical labels, especially $q$, $p$, and $H$, but turns the state description into vectors in a Hilbert space and observables into operators.

## Related Concepts

- [Mechanics](Mechanics.md)
- [Lagrangian Mechanics](Lagrangian%20Mechanics.md)
- [Hamiltonian Mechanics](Hamiltonian%20Mechanics.md)
- [Conservation Laws](Conservation%20Laws.md)
- [Shankar Chapter 2 Overview](../Book%20Notes/Shankar/Chapter%202/Chapter%20Overview.md)

<!-- semantic-edges
{"source":"Newtonian Mechanics","relation":"SPECIALIZES","target":"Classical Mechanics","evidence_heading":"Main Formulations","evidence_summary":"The note lists Newtonian mechanics as a classical formulation emphasizing forces and acceleration.","confidence":0.9}
{"source":"Lagrangian Mechanics","relation":"SPECIALIZES","target":"Classical Mechanics","evidence_heading":"Main Formulations","evidence_summary":"The note lists Lagrangian mechanics as a classical formulation emphasizing the action of paths in configuration space.","confidence":0.9}
{"source":"Hamiltonian Mechanics","relation":"SPECIALIZES","target":"Classical Mechanics","evidence_heading":"Main Formulations","evidence_summary":"The note lists Hamiltonian mechanics as a classical formulation emphasizing phase-space evolution using coordinates and conjugate momenta.","confidence":0.9}
{"source":"Quantum Mechanics","relation":"CONTRASTS_WITH","target":"Classical Mechanics","evidence_heading":"Quantum Bridge","evidence_summary":"The note contrasts quantum mechanics with classical mechanics by saying quantum theory keeps labels such as q, p, and H but changes states into Hilbert-space vectors and observables into operators.","confidence":0.85}
-->
