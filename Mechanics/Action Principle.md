# Action Principle

## Overview

The action principle states that the physical path of a system makes the action stationary under small variations of the path.

## Definition

The action is:

$$
S[q] = \int_{t_1}^{t_2} L(q,\dot{q},t) dt
$$

The stationary-action condition is:

$$
\delta S = 0
$$

The comparison paths share fixed endpoint configurations and endpoint times. In an $n$-degree-of-freedom system, each complete motion is a curve in configuration space rather than the physical trajectory of a single particle.

## Intuition

Instead of asking for the force at each instant, the action principle asks which whole path is consistent with the dynamics. The variational condition then produces local equations of motion.

## Common Confusions

- Stationary action does not always mean minimum action.
- The trial paths in the variation are mathematical paths with fixed endpoints.
- The principle is not saying that a particle makes decisions.
- The first variation determines a stationary path but does not by itself classify it as a minimum, maximum, or other stationary point.
- Adding a total derivative $dF(q,t)/dt$ to $L$ changes the action only by a fixed endpoint term and therefore leaves the equations of motion unchanged.

## Related Concepts

- [Lagrangian Mechanics](Lagrangian%20Mechanics.md)
- [Euler-Lagrange Equations](Euler-Lagrange%20Equations.md)
- [How Smart Is a Particle](../Book%20Notes/Shankar/Chapter%202/How%20Smart%20Is%20a%20Particle.md)
- [Calculus of Variations](../Mathematics/Calculus%20of%20Variations.md)
- [Goldstein Section 2.1](../Book%20Notes/Goldstein/Chapter%202/Hamilton%27s%20Principle.md)
