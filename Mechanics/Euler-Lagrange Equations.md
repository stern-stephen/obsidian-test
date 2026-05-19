# Euler-Lagrange Equations

## Overview

The Euler-Lagrange equations are the equations of motion that follow from stationary action.

## Definition

For generalized coordinates $q_i$, the equations are:

$$
\frac{d}{dt}\frac{\partial L}{\partial \dot{q}_i} - \frac{\partial L}{\partial q_i} = 0
$$

## Intuition

The equation balances how the Lagrangian changes with velocity against how it changes with position. It is the local condition that replaces the global variational statement $\delta S=0$.

## Example

For:

$$
L = \frac{1}{2}m\dot{x}^2 - V(x)
$$

the Euler-Lagrange equation gives:

$$
m\ddot{x} = -\frac{dV}{dx}
$$

which is Newton's second law for a conservative force.

## Related Concepts

- [Action Principle](Action%20Principle.md)
- [Lagrangian Mechanics](Lagrangian%20Mechanics.md)
- [Generalized Coordinates](Generalized%20Coordinates.md)
