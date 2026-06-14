# D'Alembert's Principle and Lagrange's Equations

Source: [Classical Mechanics](../../../References/GoldsteinPooleSafkoClassicalMechanics.pdf)

Book hub: [Goldstein](../Goldstein.md)

Book section: 1.4, printed pages 16-21.

Previous: [Constraints](Constraints.md)

Next: [Velocity-Dependent Potentials and the Dissipation Function](Velocity-Dependent%20Potentials%20and%20the%20Dissipation%20Function.md)

## Reading Status

- Status: started
- Pages: 16-21
- Date started: 2026-06-14
- Date finished:

## Big Ideas

- A virtual displacement is an allowed infinitesimal configuration change at a fixed time.
- Ideal constraint forces do no net virtual work.
- D'Alembert's principle converts dynamics into a virtual-work statement by adding the inertial term $-\dot{\mathbf{p}}_i$.
- Independent generalized-coordinate variations turn that statement into Lagrange's equations.

## Virtual Work

For equilibrium:

$$
\sum_i \mathbf{F}_i\cdot\delta\mathbf{r}_i=0
$$

Write each force as an applied force plus a constraint force:

$$
\mathbf{F}_i=\mathbf{F}_i^{(a)}+\mathbf{f}_i
$$

For ideal constraints:

$$
\sum_i \mathbf{f}_i\cdot\delta\mathbf{r}_i=0
$$

The equilibrium condition becomes the principle of virtual work:

$$
\sum_i \mathbf{F}_i^{(a)}\cdot\delta\mathbf{r}_i=0
$$

## D'Alembert's Principle

Using $\mathbf{F}_i-\dot{\mathbf{p}}_i=0$, the dynamical statement is:

$$
\sum_i \left(\mathbf{F}_i-\dot{\mathbf{p}}_i\right)\cdot\delta\mathbf{r}_i=0
$$

After ideal constraint forces are removed:

$$
\sum_i \left(\mathbf{F}_i^{(a)}-\dot{\mathbf{p}}_i\right)\cdot\delta\mathbf{r}_i=0
$$

This is D'Alembert's principle.

## Generalized Forces

For:

$$
\mathbf{r}_i=\mathbf{r}_i(q_1,\ldots,q_n,t)
$$

the virtual displacement is:

$$
\delta\mathbf{r}_i=\sum_j\frac{\partial\mathbf{r}_i}{\partial q_j}\delta q_j
$$

The generalized force conjugate to $q_j$ is:

$$
Q_j=\sum_i\mathbf{F}_i\cdot\frac{\partial\mathbf{r}_i}{\partial q_j}
$$

$Q_j$ need not have units of force, but $Q_j\delta q_j$ always has units of work.

## Lagrange's Equations

Transforming the inertial term gives:

$$
\frac{d}{dt}\frac{\partial T}{\partial\dot q_j}-\frac{\partial T}{\partial q_j}=Q_j
$$

For forces derived from an ordinary potential $V(q,t)$:

$$
Q_j=-\frac{\partial V}{\partial q_j}
$$

Define:

$$
L=T-V
$$

Then:

$$
\frac{d}{dt}\frac{\partial L}{\partial\dot q_j}-\frac{\partial L}{\partial q_j}=0
$$

The Lagrangian is not unique. Adding a total time derivative leaves the equations of motion unchanged:

$$
L'=L+\frac{dF(q,t)}{dt}
$$

## Common Confusions

- A virtual displacement is taken at fixed time; it is not the actual displacement during $dt$.
- Applied forces need not vanish in equilibrium because the allowed virtual displacements are constrained.
- Constraint forces disappear only when their total virtual work vanishes.
- $L=T-V$ is a standard construction, not a unique representation of the dynamics.

## Links To Concept Notes

- [Virtual Work and D'Alembert's Principle](../../../Mechanics/Virtual%20Work%20and%20DAlemberts%20Principle.md)
- [Generalized Coordinates](../../../Mechanics/Generalized%20Coordinates.md)
- [Lagrangian Mechanics](../../../Mechanics/Lagrangian%20Mechanics.md)
- [Euler-Lagrange Equations](../../../Mechanics/Euler-Lagrange%20Equations.md)
