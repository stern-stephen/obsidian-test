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

## Derivation From Stationary Action

Start with the action functional:

$$
S[q]=\int_{t_1}^{t_2} L(q,\dot{q},t) dt
$$

The physical path is the path for which the action is stationary under small variations. Consider a nearby path:

$$
q(t)\to q(t)+\epsilon\eta(t)
$$

The variation $\eta(t)$ is arbitrary in the middle of the interval, but the endpoints are fixed:

$$
\eta(t_1)=\eta(t_2)=0
$$

To first order, the change in the action is:

$$
\delta S=\int_{t_1}^{t_2}\left(\frac{\partial L}{\partial q}\delta q+\frac{\partial L}{\partial \dot{q}}\delta\dot{q}\right)dt
$$

Since:

$$
\delta\dot{q}=\frac{d}{dt}\delta q
$$

we have:

$$
\delta S=\int_{t_1}^{t_2}\left(\frac{\partial L}{\partial q}\delta q+\frac{\partial L}{\partial \dot{q}}\frac{d}{dt}\delta q\right)dt
$$

The second term has a derivative on $\delta q$. Integrate by parts to move that derivative onto $\frac{\partial L}{\partial \dot{q}}$:

$$
\int_{t_1}^{t_2}\frac{\partial L}{\partial \dot{q}}\frac{d}{dt}\delta q dt=\left[\frac{\partial L}{\partial \dot{q}}\delta q\right]_{t_1}^{t_2}-\int_{t_1}^{t_2}\frac{d}{dt}\left(\frac{\partial L}{\partial \dot{q}}\right)\delta q dt
$$

The boundary term vanishes because the endpoints are fixed:

$$
\delta q(t_1)=\delta q(t_2)=0
$$

So:

$$
\delta S=\int_{t_1}^{t_2}\left[\frac{\partial L}{\partial q}-\frac{d}{dt}\left(\frac{\partial L}{\partial \dot{q}}\right)\right]\delta q dt
$$

For the action to be stationary, $\delta S=0$ for every allowed variation $\delta q(t)$. The only way this can hold for arbitrary $\delta q(t)$ is:

$$
\frac{\partial L}{\partial q}-\frac{d}{dt}\left(\frac{\partial L}{\partial \dot{q}}\right)=0
$$

Rearranging gives:

$$
\frac{d}{dt}\left(\frac{\partial L}{\partial \dot{q}}\right)=\frac{\partial L}{\partial q}
$$

For several generalized coordinates, repeat the same argument for each independent variation $\delta q_i(t)$:

$$
\frac{d}{dt}\left(\frac{\partial L}{\partial \dot{q}_i}\right)=\frac{\partial L}{\partial q_i}
$$

In words: vary the whole path, compute the first-order change in the action, use integration by parts to make every term proportional to $\delta q$, then require the coefficient of every possible variation to vanish.

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
