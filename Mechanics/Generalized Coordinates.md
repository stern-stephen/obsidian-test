# Generalized Coordinates

## Overview

Generalized coordinates are variables chosen to describe the configuration of a system.

## Definition

A system with $n$ degrees of freedom can be described by coordinates:

$$
q_1,\ldots,q_n
$$

These coordinates may be distances, angles, normal modes, or other variables suited to the constraints.

For $N$ particles subject to $k$ independent holonomic constraints, one can choose:

$$
n=3N-k
$$

independent generalized coordinates and write:

$$
\mathbf{r}_i=\mathbf{r}_i(q_1,\ldots,q_n,t)
$$

The transformation then contains the holonomic constraints implicitly.

## Intuition

The point of generalized coordinates is to describe only the actual degrees of freedom. For constrained systems, this can remove constraint forces from the equations.

## Examples

- A pendulum can be described by its angle instead of Cartesian coordinates.
- A particle in polar coordinates can be described by $r$ and $\theta$.
- A rigid rotor can be described using angular coordinates.

Generalized coordinates are also useful without constraints. Spherical coordinates, for example, adapt naturally to a central-force problem.

## Related Concepts

- [Lagrangian Mechanics](Lagrangian%20Mechanics.md)
- [Euler-Lagrange Equations](Euler-Lagrange%20Equations.md)
- [Canonical Momentum](Canonical%20Momentum.md)
- [Constraints](Constraints.md)
- [Goldstein Section 1.3](../Book%20Notes/Goldstein/Chapter%201/Constraints.md)
- [Coopersmith Section 4.7](../Book%20Notes/Coopersmith/Chapter%204/Generalized%20Coordinates.md)
