# Routhian and Symplectic Notation

Source: [Hamill](../../../References/Hamill.pdf)

Book hub: [Hamill](../Hamill.md)

Chapter overview: [Chapter Overview](Chapter%20Overview.md)

Book sections: 4.6-4.8, printed pages 104-108.

Previous: [Canonical Equations and Phase Space](Canonical%20Equations%20and%20Phase%20Space.md)

Next: [Chapter 5 - Canonical Transformations; Poisson Brackets](../Chapter%205/Chapter%20Overview.md)

## Reading Status

- Status: started
- Pages: 104-108
- Date started: 2026-07-26
- Date finished:

## Purpose

Hamill ends Chapter 4 with two techniques that prepare later Hamiltonian work: the Routhian procedure for systems with cyclic coordinates, and symplectic notation for writing Hamilton's equations compactly.

## 4.6 Cyclic Coordinates And The Routhian

If a coordinate does not appear in the Lagrangian, it is cyclic or ignorable. Its conjugate momentum is conserved.

Suppose $q_{s+1},\ldots,q_n$ are cyclic while $q_1,\ldots,q_s$ are not. The Routhian is:

$$
R=\sum_{i=s+1}^{n}p_i\dot q_i-L
$$

The sum runs only over the cyclic coordinates. This makes $R$ a hybrid object:

- for the non-cyclic coordinates, it behaves like a Lagrangian,
- for the cyclic coordinates and their momenta, it behaves like a Hamiltonian.

For $i=1,\ldots,s$, the non-cyclic coordinates obey:

$$
\frac{d}{dt}\left(\frac{\partial R}{\partial \dot q_i}\right)-\frac{\partial R}{\partial q_i}=0
$$

For the cyclic coordinates, the momenta are constants and can be replaced by constants determined from initial conditions. This reduces the number of variables in the problem.

## Steady Motion

Hamill uses the Routhian to describe steady motion, where the non-cyclic variables are constant. A circular orbit in polar coordinates is the model example: $r$ is constant while the cyclic angular coordinate increases linearly with time.

This gives a useful pattern:

- non-cyclic variables can describe deviations from steady motion,
- cyclic variables often carry uniform drift,
- the Routhian isolates the effective dynamics of the remaining variables.

## 4.7 Symplectic Notation

Collect all coordinates and momenta into a single column vector:

$$
\zeta=(q_1,\ldots,q_n,p_1,\ldots,p_n)^T
$$

Collect the Hamiltonian derivatives into:

$$
\frac{\partial H}{\partial\zeta}
$$

Define the block matrix:

$$
J=\begin{bmatrix}0&I\\-I&0\end{bmatrix}
$$

Then Hamilton's equations become:

$$
\dot\zeta=J\frac{\partial H}{\partial\zeta}
$$

This notation emphasizes that Hamiltonian dynamics has a fixed coordinate-momentum pairing. Hamill points out that this form is useful for symplectic integrators in celestial mechanics, molecular dynamics, and accelerator physics.

## Problems

The Chapter 4 problem set asks for Hamiltonians and Hamilton equations for systems such as pendula, orbital motion, constrained motion on a sphere, and time-dependent supports. It also asks the reader to check a canonical-transformation determinant, foreshadowing Chapter 5.

## Links To Concept Notes

- [Cyclic Coordinates](../../../Mechanics/Cyclic%20Coordinates.md)
- [Hamiltonian Mechanics](../../../Mechanics/Hamiltonian%20Mechanics.md)
- [Phase Space](../../../Mechanics/Phase%20Space.md)
- [Canonical Transformations](../../../Mechanics/Canonical%20Transformations.md)

<!-- semantic-edges
{"source":"Routhian","relation":"REDUCES","target":"Cyclic Coordinates","evidence_heading":"4.6 Cyclic Coordinates And The Routhian","evidence_summary":"The Routhian treats cyclic coordinate momenta as constants and reduces the remaining dynamical variables.","confidence":0.9}
{"source":"Symplectic Notation","relation":"REFORMULATES","target":"Hamilton's Equations","evidence_heading":"4.7 Symplectic Notation","evidence_summary":"The note writes Hamilton's equations as zdot = J partial H / partial z using a block symplectic matrix.","confidence":0.9}
-->
