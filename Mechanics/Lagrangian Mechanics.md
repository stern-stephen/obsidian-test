# Lagrangian Mechanics

## Overview

Lagrangian mechanics formulates dynamics using generalized coordinates, velocities, and the action.

## Definition

For many systems, the Lagrangian is:

$$
L = T - V
$$

The action is:

$$
S = \int L dt
$$

Physical trajectories satisfy:

$$
\delta S = 0
$$

## Key Equations

The Euler-Lagrange equations are:

$$
\frac{d}{dt}\frac{\partial L}{\partial \dot{q}_i} - \frac{\partial L}{\partial q_i} = 0
$$

The conjugate momentum is:

$$
p_i = \frac{\partial L}{\partial \dot{q}_i}
$$

## Intuition

The Lagrangian approach is especially useful when constraints make Cartesian force equations awkward. Good coordinates can make the problem simpler before solving any differential equations.

## Related Concepts

- [Action Principle](Action%20Principle.md)
- [Euler-Lagrange Equations](Euler-Lagrange%20Equations.md)
- [Generalized Coordinates](Generalized%20Coordinates.md)
- [Hamiltonian Mechanics](Hamiltonian%20Mechanics.md)
- [The Principle of Least Action and Lagrangian Mechanics](../Book%20Notes/Shankar/Chapter%202/The%20Principle%20of%20Least%20Action%20and%20Lagrangian%20Mechanics.md)
