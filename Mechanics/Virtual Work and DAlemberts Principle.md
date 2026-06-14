# Virtual Work and D'Alembert's Principle

## Overview

Virtual work reformulates equilibrium using infinitesimal allowed changes of configuration. D'Alembert's principle extends the same idea to dynamics and provides the bridge from Newton's laws to Lagrange's equations.

## Virtual Displacement

A virtual displacement $\delta\mathbf{r}_i$ is an infinitesimal change consistent with the constraints at a fixed instant. It is not the actual displacement during a time interval.

For equilibrium:

$$
\sum_i\mathbf{F}_i\cdot\delta\mathbf{r}_i=0
$$

For ideal constraints:

$$
\sum_i\mathbf{f}_i\cdot\delta\mathbf{r}_i=0
$$

so only applied forces remain in the virtual-work equation.

## D'Alembert's Principle

Write Newton's law as:

$$
\mathbf{F}_i-\dot{\mathbf{p}}_i=0
$$

Then:

$$
\sum_i\left(\mathbf{F}_i-\dot{\mathbf{p}}_i\right)\cdot\delta\mathbf{r}_i=0
$$

After ideal constraint forces are removed, transform the remaining expression to independent generalized-coordinate variations. This gives:

$$
\frac{d}{dt}\frac{\partial T}{\partial\dot q_j}-\frac{\partial T}{\partial q_j}=Q_j
$$

For conservative forces, this becomes the Euler-Lagrange equation.

## Intuition

The inertial term $-\dot{\mathbf{p}}_i$ lets a dynamical trajectory be treated as an instantaneous virtual-work balance. The method is valuable because the allowed virtual displacements automatically respect the constraints.

## Related Concepts

- [Constraints](Constraints.md)
- [Generalized Coordinates](Generalized%20Coordinates.md)
- [Lagrangian Mechanics](Lagrangian%20Mechanics.md)
- [Euler-Lagrange Equations](Euler-Lagrange%20Equations.md)
- [Goldstein Section 1.4](../Book%20Notes/Goldstein/Chapter%201/DAlemberts%20Principle%20and%20Lagranges%20Equations.md)
