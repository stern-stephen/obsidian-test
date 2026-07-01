# Euler-Lagrange Equations

## Overview

The Euler-Lagrange equations can be reached either by projecting Newton's laws through D'Alembert's principle or by requiring the action to be stationary.

## Definition

For generalized coordinates $q_i$, the equations are:

$$
\frac{d}{dt}\frac{\partial L}{\partial \dot{q}_i} - \frac{\partial L}{\partial q_i} = 0
$$

## Intuition

The equation balances how the Lagrangian changes with velocity against how it changes with position. It is the local condition that replaces the global variational statement $\delta S=0$.

## Derivation From D'Alembert's Principle

D'Alembert's principle removes ideal constraint forces and projects the applied and inertial forces onto independent generalized-coordinate variations. The key kinetic-energy identity is

$$
\sum_i\dot{\mathbf{p}}_i\cdot\frac{\partial\mathbf{r}_i}{\partial q_j}=\frac{d}{dt}\frac{\partial T}{\partial\dot q_j}-\frac{\partial T}{\partial q_j}
$$

It produces Lagrange's equation

$$
\frac{d}{dt}\frac{\partial T}{\partial\dot q_j}-\frac{\partial T}{\partial q_j}=Q_j
$$

For $Q_j=-\partial V/\partial q_j$ and $L=T-V$, this is the Euler-Lagrange equation. See [Virtual Work and D'Alembert's Principle](Virtual%20Work%20and%20DAlemberts%20Principle.md#dalemberts-principle) for the complete derivation.

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

For the action to be stationary, $\delta S=0$ for every allowed variation $\delta q(t)$. The fundamental lemma of the calculus of variations says that if a continuous function $F(t)$ satisfies

$$
\int_{t_1}^{t_2}F(t)\delta q(t)dt=0
$$

for every sufficiently smooth variation that vanishes at the endpoints, then $F(t)=0$ throughout the interval. Here,

$$
F(t)=\frac{\partial L}{\partial q}-\frac{d}{dt}\left(\frac{\partial L}{\partial \dot{q}}\right)
$$

so the coefficient of the arbitrary variation must vanish pointwise:

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

- [Goldstein Section 2.3](../Book%20Notes/Goldstein/Chapter%202/Derivation%20of%20Lagrange%27s%20Equations%20from%20Hamilton%27s%20Principle.md)
- [Action Principle](Action%20Principle.md)
- [Virtual Work and D'Alembert's Principle](Virtual%20Work%20and%20DAlemberts%20Principle.md)
- [Lagrangian Mechanics](Lagrangian%20Mechanics.md)
- [Generalized Coordinates](Generalized%20Coordinates.md)

<!-- semantic-edges
{"source":"Euler-Lagrange Equations","relation":"DERIVES_FROM","target":"D'Alembert's Principle","evidence_heading":"Derivation From D'Alembert's Principle","evidence_summary":"The note shows how D'Alembert's principle removes ideal constraint forces, projects forces onto generalized-coordinate variations, and gives the Euler-Lagrange equations for conservative forces.","confidence":0.95}
{"source":"Euler-Lagrange Equations","relation":"DERIVES_FROM","target":"Action Principle","evidence_heading":"Derivation From Stationary Action","evidence_summary":"The note derives the Euler-Lagrange equations from stationary action by integrating by parts and applying the fundamental lemma of the calculus of variations.","confidence":0.95}
{"source":"Euler-Lagrange Equations","relation":"REFORMULATES","target":"Stationary Action","evidence_heading":"Intuition","evidence_summary":"The note describes the Euler-Lagrange equation as the local condition that replaces the global variational statement delta S equals zero.","confidence":0.9}
{"source":"Euler-Lagrange Equations","relation":"REFORMULATES","target":"Newton's Second Law","evidence_heading":"Example","evidence_summary":"For L = m dot x squared over two minus V(x), the Euler-Lagrange equation gives Newton's second law for a conservative force.","confidence":0.9}
-->
