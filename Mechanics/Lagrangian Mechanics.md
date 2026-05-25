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

The Hamiltonian is obtained by replacing the velocity variables with momentum variables through a [Legendre transform](../Mathematics/Legendre%20Transforms.md):

$$
H(q,p,t)=\sum_i p_i\dot{q}_i-L(q,\dot{q},t)
$$

After defining $p_i$, solve for $\dot{q}_i$ in terms of $q_i,p_i,t$ before treating $H$ as a phase-space function.

## Intuition

The Lagrangian approach is especially useful when constraints make Cartesian force equations awkward. Good coordinates can make the problem simpler before solving any differential equations.

## Related Concepts

- [Action Principle](Action%20Principle.md)
- [Euler-Lagrange Equations](Euler-Lagrange%20Equations.md)
- [Generalized Coordinates](Generalized%20Coordinates.md)
- [Hamiltonian Mechanics](Hamiltonian%20Mechanics.md)
- [Legendre Transforms](../Mathematics/Legendre%20Transforms.md)
- [The Principle of Least Action and Lagrangian Mechanics](../Book%20Notes/Shankar/Chapter%202/The%20Principle%20of%20Least%20Action%20and%20Lagrangian%20Mechanics.md)
