# Hamiltonian Mechanics

## Overview

Hamiltonian mechanics describes dynamics using generalized coordinates and conjugate momenta in phase space.

## Definition

The Hamiltonian is obtained from the Lagrangian by a [Legendre transform](../Mathematics/Legendre%20Transforms.md):

$$
H(q,p,t) = \sum_i p_i\dot{q}_i - L(q,\dot{q},t)
$$

where:

$$
p_i = \frac{\partial L}{\partial \dot{q}_i}
$$

After computing the momenta, solve these equations for the velocities $\dot{q}_i$ in terms of $q_i,p_i,t$. Then substitute those velocities into the Legendre transform so that $H$ is a function of $q,p,t$, not $q,\dot{q},t$.

## Key Equations

Hamilton's equations are:

$$
\dot{q}_i = \frac{\partial H}{\partial p_i}
$$

$$
\dot{p}_i = -\frac{\partial H}{\partial q_i}
$$

## Intuition

The Hamiltonian is often the total energy, but its structural role is broader: it generates time evolution in phase space.

## Deriving The Hamiltonian From The Lagrangian

Start with:

$$
L(q,\dot{q},t)
$$

The Lagrangian uses generalized positions and velocities. Hamiltonian mechanics instead uses generalized positions and conjugate momenta.

First define the conjugate momenta:

$$
p_i=\frac{\partial L}{\partial \dot{q}_i}
$$

Then solve these equations for the velocities:

$$
\dot{q}_i=\dot{q}_i(q,p,t)
$$

Finally define:

$$
H(q,p,t)=\sum_i p_i\dot{q}_i-L(q,\dot{q},t)
$$

with the velocities rewritten in terms of $q,p,t$.

This change of variables is a [Legendre transform](../Mathematics/Legendre%20Transforms.md). It replaces the velocity variables $\dot{q}_i$ with the momentum variables $p_i$.

### Simple Particle Example

For:

$$
L=\frac{1}{2}m\dot{x}^2-V(x)
$$

the conjugate momentum is:

$$
p=\frac{\partial L}{\partial \dot{x}}=m\dot{x}
$$

So:

$$
\dot{x}=\frac{p}{m}
$$

Now compute:

$$
H=p\dot{x}-L
$$

Substitute $\dot{x}=p/m$:

$$
H=p\frac{p}{m}-\left(\frac{1}{2}m\left(\frac{p}{m}\right)^2-V(x)\right)
$$

Simplifying gives:

$$
H=\frac{p^2}{2m}+V(x)
$$

For this simple system, the Hamiltonian equals the total energy:

$$
H=T+V
$$

But this is a result of the example, not the definition. The definition is the Legendre transform from $L(q,\dot{q},t)$ to $H(q,p,t)$.

## Quantum Bridge

The Hamiltonian becomes the operator that generates time evolution in quantum mechanics.

## Related Concepts

- [Phase Space](Phase%20Space.md)
- [Canonical Momentum](Canonical%20Momentum.md)
- [Poisson Brackets](Poisson%20Brackets.md)
- [Lagrangian Mechanics](Lagrangian%20Mechanics.md)
- [Legendre Transforms](../Mathematics/Legendre%20Transforms.md)
- [The Hamiltonian Formalism](../Book%20Notes/Shankar/Chapter%202/The%20Hamiltonian%20Formalism.md)
