# Hamilton's Principle

## Overview

Hamilton's principle says that the actual motion of a mechanical system makes the action stationary among nearby allowed histories with the same endpoint times and endpoint configurations.

It is the standard fixed-endpoint action principle for Lagrangian mechanics.

## Definition

For generalized coordinates $q_i(t)$ and Lagrangian $L(q,\dot q,t)$, define the action:

$$
S[q]=\int_{t_a}^{t_b}L(q,\dot q,t)dt
$$

Hamilton's principle is:

$$
\delta S=0
$$

or:

$$
\delta\int_{t_a}^{t_b}L(q,\dot q,t)dt=0
$$

The variations compare nearby allowed paths with:

$$
\delta q_i(t_a)=\delta q_i(t_b)=0
$$

## Derivation From D'Alembert's Principle

Coopersmith derives Hamilton's principle by embedding D'Alembert's instantaneous virtual-work balance in a time integral:

$$
\int_{t_a}^{t_b}\sum_i(\mathbf{F}_i^{appl}-m_i\mathbf{a}_i)\cdot\delta\mathbf{r}_i dt=0
$$

For conservative applied forces:

$$
\sum_i\mathbf{F}_i^{appl}\cdot\delta\mathbf{r}_i=-\delta V
$$

For the inertial term, integration by parts turns the acceleration term into a kinetic-energy variation plus a boundary term. Fixed endpoint variations make the boundary term vanish, leaving:

$$
\delta\int_{t_a}^{t_b}(T-V)dt=0
$$

With $L=T-V$, this becomes Hamilton's principle.

## Deriving Equations Of Motion

Varying the action and integrating the velocity-variation term by parts gives:

$$
\delta S=\left[\sum_i\frac{\partial L}{\partial\dot q_i}\delta q_i\right]_{t_a}^{t_b}+\int_{t_a}^{t_b}\sum_i\left[\frac{\partial L}{\partial q_i}-\frac{d}{dt}\left(\frac{\partial L}{\partial\dot q_i}\right)\right]\delta q_i dt
$$

The boundary term vanishes because the endpoint configurations are fixed. Since the interior variations are arbitrary, each coefficient must vanish:

$$
\frac{d}{dt}\left(\frac{\partial L}{\partial\dot q_i}\right)-\frac{\partial L}{\partial q_i}=0
$$

So Hamilton's principle implies the Euler-Lagrange equations.

## Common Confusions

- "Stationary" does not always mean "minimum"; it means the first-order variation is zero.
- The varied paths are mathematical comparison paths, not alternative physical motions that already obey the equations of motion.
- The endpoint configurations are fixed in the standard form; changing endpoint conditions changes the variational problem.
- Hamilton's principle is a specific fixed-endpoint action principle, while "action principle" can refer to a broader family of variational principles.

## Related Concepts

- [Action Principle](Action%20Principle.md)
- [Lagrangian Mechanics](Lagrangian%20Mechanics.md)
- [Euler-Lagrange Equations](Euler-Lagrange%20Equations.md)
- [Virtual Work and D'Alembert's Principle](Virtual%20Work%20and%20DAlemberts%20Principle.md)
- [Coopersmith Section 6.1-6.2](../Book%20Notes/Coopersmith/Chapter%206/Introduction%20and%20Hamiltons%20Principle.md)
- [Goldstein Section 2.1](../Book%20Notes/Goldstein/Chapter%202/Hamilton%27s%20Principle.md)

<!-- semantic-edges
{"source":"Hamilton's Principle","relation":"SPECIALIZES","target":"Action Principle","evidence_heading":"Overview","evidence_summary":"The note identifies Hamilton's principle as the standard fixed-endpoint action principle for Lagrangian mechanics.","confidence":0.95}
{"source":"Hamilton's Principle","relation":"DERIVES_FROM","target":"D'Alembert's Principle","evidence_heading":"Derivation From D'Alembert's Principle","evidence_summary":"The note derives Hamilton's principle by integrating D'Alembert's virtual-work balance through time and using fixed endpoint variations to remove the boundary term.","confidence":0.95}
{"source":"Hamilton's Principle","relation":"DERIVES","target":"Euler-Lagrange Equations","evidence_heading":"Deriving Equations Of Motion","evidence_summary":"The note derives the Euler-Lagrange equations by varying the action, integrating by parts, and using fixed endpoint variations.","confidence":0.95}
{"source":"Hamilton's Principle","relation":"REQUIRES","target":"Fixed Endpoint Variations","evidence_heading":"Definition","evidence_summary":"The standard form compares nearby paths whose endpoint times and endpoint configurations are fixed.","confidence":0.9}
-->
