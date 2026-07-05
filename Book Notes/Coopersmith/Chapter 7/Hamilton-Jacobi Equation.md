# Hamilton-Jacobi Equation

Source: [The Lazy Universe](../../../References/Coopersmith2017TheLazyUniverse.pdf)

Book hub: [Coopersmith](../Coopersmith.md)

Book section: 7.8, printed pages 166-175.

Previous: [Conservation Theorems](Conservation%20Theorems.md)

Next: [Royal Road to Quantum Mechanics](Royal%20Road%20to%20Quantum%20Mechanics.md)

## Reading Status

- Status: started
- Pages: 166-175
- Date started: 2026-07-05
- Date finished:

## Big Ideas

- Hamilton-Jacobi theory tries to solve mechanics through a generating function rather than by directly solving all equations of motion.
- The action function $S$ generates canonical transformations.
- The Hamilton-Jacobi equation connects the Hamiltonian, action, and the motion of action wavefronts.
- Coopersmith presents it as the point where the optical analogy becomes structurally powerful.

## The Problem It Solves

Hamiltonian mechanics puts the motion in phase space, but the action surfaces live in configuration space. The Hamilton-Jacobi approach uses a generating function to connect these pictures.

The action function $S$ is treated as a function of the coordinates and time. Its coordinate derivatives give momenta:

$$
p_i=\frac{\partial S}{\partial q_i}
$$

## The Equation

In common notation, the Hamilton-Jacobi equation is:

$$
\frac{\partial S}{\partial t}+H\left(q_i,\frac{\partial S}{\partial q_i},t\right)=0
$$

This says that if one knows the right action function $S$, then the momenta and the motion are encoded in its derivatives.

## Wavefront Picture

Coopersmith emphasizes surfaces of common action. These surfaces move through configuration space like wavefronts. Mechanical trajectories act like rays crossing the action surfaces. This is the heart of the optics-mechanics analogy.

## Links To Concept Notes

- [Hamilton-Jacobi Equation](../../../Mechanics/Hamilton-Jacobi%20Equation.md)
- [Hamiltonian Mechanics](../../../Mechanics/Hamiltonian%20Mechanics.md)
- [Canonical Transformations](../../../Mechanics/Canonical%20Transformations.md)
- [Action Principle](../../../Mechanics/Action%20Principle.md)

<!-- semantic-edges
{"source":"Coopersmith Section 7.8","relation":"INTRODUCES","target":"Hamilton-Jacobi Equation","evidence_heading":"Big Ideas","evidence_summary":"Section 7.8 presents Hamilton-Jacobi theory as a way to solve mechanics through an action generating function.","confidence":0.95}
{"source":"Action Function","relation":"ENABLES","target":"Canonical Transformations","evidence_heading":"The Problem It Solves","evidence_summary":"The note says the action function S generates canonical transformations linking phase-space and configuration-space pictures.","confidence":0.88}
{"source":"Hamilton-Jacobi Equation","relation":"MOTIVATES","target":"Optical Analogy","evidence_heading":"Wavefront Picture","evidence_summary":"Coopersmith uses common-action wavefronts and mechanical rays to connect the Hamilton-Jacobi equation with Hamilton's optical analogy.","confidence":0.9}
-->
