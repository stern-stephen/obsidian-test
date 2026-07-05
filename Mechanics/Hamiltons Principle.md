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

Split the applied and inertial parts:

$$
\int_{t_a}^{t_b}\sum_i\mathbf{F}_i^{appl}\cdot\delta\mathbf{r}_i dt-\int_{t_a}^{t_b}\sum_i m_i\mathbf{a}_i\cdot\delta\mathbf{r}_i dt=0
$$

For conservative applied forces:

$$
\sum_i\mathbf{F}_i^{appl}\cdot\delta\mathbf{r}_i=-\delta V
$$

So the applied-force term becomes:

$$
-\int_{t_a}^{t_b}\delta V dt
$$

For the inertial term, write $\mathbf{a}_i=d\mathbf{v}_i/dt$. With constant masses:

$$
\int_{t_a}^{t_b}\sum_i m_i\mathbf{a}_i\cdot\delta\mathbf{r}_i dt=\int_{t_a}^{t_b}\sum_i\frac{d}{dt}(m_i\mathbf{v}_i)\cdot\delta\mathbf{r}_i dt
$$

Integrate by parts:

$$
\int_{t_a}^{t_b}\sum_i\frac{d}{dt}(m_i\mathbf{v}_i)\cdot\delta\mathbf{r}_i dt=\left[\sum_i m_i\mathbf{v}_i\cdot\delta\mathbf{r}_i\right]_{t_a}^{t_b}-\int_{t_a}^{t_b}\sum_i m_i\mathbf{v}_i\cdot\frac{d}{dt}(\delta\mathbf{r}_i)dt
$$

The velocity variation satisfies:

$$
\delta\mathbf{v}_i=\frac{d}{dt}(\delta\mathbf{r}_i)
$$

Therefore:

$$
\sum_i m_i\mathbf{v}_i\cdot\delta\mathbf{v}_i=\delta T
$$

So:

$$
\int_{t_a}^{t_b}\sum_i m_i\mathbf{a}_i\cdot\delta\mathbf{r}_i dt=\left[\sum_i m_i\mathbf{v}_i\cdot\delta\mathbf{r}_i\right]_{t_a}^{t_b}-\int_{t_a}^{t_b}\delta T dt
$$

Hamilton's fixed endpoint condition is:

$$
\delta\mathbf{r}_i(t_a)=\delta\mathbf{r}_i(t_b)=0
$$

This kills the boundary term:

$$
\left[\sum_i m_i\mathbf{v}_i\cdot\delta\mathbf{r}_i\right]_{t_a}^{t_b}=0
$$

Substituting back into the time-integrated D'Alembert equation gives:

$$
-\int_{t_a}^{t_b}\delta V dt+\int_{t_a}^{t_b}\delta T dt=0
$$

Combine the terms:

$$
\int_{t_a}^{t_b}\delta(T-V)dt=0
$$

Because the endpoint times are fixed, the variation can be moved outside the integral:

$$
\delta\int_{t_a}^{t_b}(T-V)dt=0
$$

With $L=T-V$, this becomes Hamilton's principle:

$$
\delta\int_{t_a}^{t_b}L dt=0
$$

## Scope Of The Conservative-Force Derivation

The derivation above proves a sufficient route to Hamilton's principle:

$$
\text{conservative applied forces} \Rightarrow L=T-V \Rightarrow \delta\int Ldt=0
$$

It does not prove that conservative forces are the only possible forces compatible with Hamilton's principle.

The broader test is whether the force law can be produced by some Lagrangian through the Euler-Lagrange equations. Some forces that are not conservative in the simple position-only potential sense are still Lagrangian. A charged particle in an electromagnetic field is the standard example: the Lagrangian contains velocity-dependent terms, so it is not just $T-V(q)$, but Hamilton's principle still applies.

Arbitrary dissipative forces are different. A friction force such as linear drag usually cannot be obtained from an ordinary fixed-endpoint action for just the damped object. It can be handled by extensions such as a Rayleigh dissipation function, by generalized nonconservative forces, or by enlarging the modeled system to include the environment that receives the dissipated energy.

So the conservative-force derivation should be read as:

- conservative forces make the derivation simple;
- a force can still be allowed if it comes from some suitable Lagrangian;
- not every nonconservative force comes from such a Lagrangian.

## Minimum, Maximum, And Saddle

Hamilton's principle requires stationarity:

$$
\delta S=0
$$

This first-variation condition does not by itself classify the action value. Coopersmith emphasizes in Section 6.6 that ordinary mechanical action may be a true minimum or a saddle point, but not a true maximum in the same sense. The intuition is that comparison paths can usually be made less economical in action by adding detours or rapid variations, so there is no largest nearby action value selected by the physical path.

A saddle means some allowed variations raise the action while others lower it. Thus "least action" is useful language in many ordinary cases, especially for short enough intervals, but "stationary action" is the safer general statement.

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
- [Electromagnetic Lagrangian](Electromagnetic%20Lagrangian.md)
- [Rayleigh Dissipation Function](Rayleigh%20Dissipation%20Function.md)
- [Coopersmith Section 6.1-6.2](../Book%20Notes/Coopersmith/Chapter%206/Introduction%20and%20Hamiltons%20Principle.md)
- [Coopersmith Section 6.5-6.6](../Book%20Notes/Coopersmith/Chapter%206/The%20Forms%20of%20T%20V%20and%20L.md)
- [Goldstein Section 2.1](../Book%20Notes/Goldstein/Chapter%202/Hamilton%27s%20Principle.md)

<!-- semantic-edges
{"source":"Hamilton's Principle","relation":"SPECIALIZES","target":"Action Principle","evidence_heading":"Overview","evidence_summary":"The note identifies Hamilton's principle as the standard fixed-endpoint action principle for Lagrangian mechanics.","confidence":0.95}
{"source":"Hamilton's Principle","relation":"DERIVES_FROM","target":"D'Alembert's Principle","evidence_heading":"Derivation From D'Alembert's Principle","evidence_summary":"The note derives Hamilton's principle by integrating D'Alembert's virtual-work balance through time and using fixed endpoint variations to remove the boundary term.","confidence":0.95}
{"source":"Hamilton's Principle","relation":"DERIVES","target":"Euler-Lagrange Equations","evidence_heading":"Deriving Equations Of Motion","evidence_summary":"The note derives the Euler-Lagrange equations by varying the action, integrating by parts, and using fixed endpoint variations.","confidence":0.95}
{"source":"Hamilton's Principle","relation":"REQUIRES","target":"Fixed Endpoint Variations","evidence_heading":"Definition","evidence_summary":"The standard form compares nearby paths whose endpoint times and endpoint configurations are fixed.","confidence":0.9}
{"source":"Conservative Forces","relation":"ENABLES","target":"Hamilton's Principle","evidence_heading":"Scope Of The Conservative-Force Derivation","evidence_summary":"The note says conservative applied forces provide a sufficient route to the simple L = T - V form of Hamilton's principle.","confidence":0.9}
{"source":"Electromagnetic Lagrangian","relation":"EXAMPLE_OF","target":"Nonconservative Lagrangian Force","evidence_heading":"Scope Of The Conservative-Force Derivation","evidence_summary":"The note identifies a charged particle in an electromagnetic field as a standard case where velocity-dependent Lagrangian terms allow Hamilton's principle beyond a simple position-only potential.","confidence":0.86}
{"source":"Hamilton's Principle","relation":"CONTRASTS_WITH","target":"True Maximum Action","evidence_heading":"Minimum, Maximum, And Saddle","evidence_summary":"The note explains Coopersmith's point that Hamilton's principle gives stationary action and may give minima or saddle points, but ordinary mechanical action is not selected as a true maximum.","confidence":0.84}
-->
