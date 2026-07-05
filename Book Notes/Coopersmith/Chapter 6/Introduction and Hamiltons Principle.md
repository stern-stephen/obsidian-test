# Introduction and Hamilton's Principle

Source: [The Lazy Universe](../../../References/Coopersmith2017TheLazyUniverse.pdf)

Book hub: [Coopersmith](../Coopersmith.md)

Book section: 6.1-6.2, printed pages 107-112.

Previous: [Chapter Overview](Chapter%20Overview.md)

Next: [Lagrange's Equations of Motion](Lagranges%20Equations%20of%20Motion.md)

## Reading Status

- Status: started
- Pages: 107-112
- Date started: 2026-07-03
- Date finished:

## Big Ideas

- D'Alembert's principle works at one instant; Lagrangian mechanics seeks a condition for an entire motion through time.
- Coopersmith frames Hamilton's principle as embedding D'Alembert's dynamical virtual work inside a time integral.
- The derivation only works cleanly when the forces, constraints, and kinematic conditions can be written as functions.
- Fixed endpoint variations make the integration-by-parts boundary term vanish.

## From Instantaneous Balance To A Path Condition

D'Alembert's principle says that at each instant the total dynamical virtual work vanishes:

$$
\sum_i(\mathbf{F}_i^{appl}-m_i\mathbf{a}_i)\cdot\delta\mathbf{r}_i=0
$$

Chapter 6 asks for a stronger-looking formulation: instead of reapplying this balance instant by instant, integrate it over the interval from $t_a$ to $t_b$ and find the whole path that makes the integrated condition stationary.

The catch is functional form. To use the calculus of variations, the applied forces must come from a potential energy function and the constraints or kinematic conditions must be expressible as functions.

## The Key Rearrangement

The applied-force part becomes a variation of potential energy:

$$
\sum_i\mathbf{F}_i^{appl}\cdot\delta\mathbf{r}_i=-\delta V
$$

The inertial term is integrated by parts. This changes the acceleration term into a kinetic-energy variation plus a boundary term. Hamilton's fixed-endpoint requirement makes the endpoint variations vanish:

$$
\delta\mathbf{r}_i(t_a)=\delta\mathbf{r}_i(t_b)=0
$$

With the boundary term gone, the remaining variational statement is:

$$
\delta\int_{t_a}^{t_b}(T-V)dt=0
$$

Coopersmith identifies this as Hamilton's principle and as a principle of least action in the broad terminology used in the book.

## Derivation Details

Start with D'Alembert's principle and integrate it through the time interval:

$$
\int_{t_a}^{t_b}\sum_i(\mathbf{F}_i^{appl}-m_i\mathbf{a}_i)\cdot\delta\mathbf{r}_i dt=0
$$

Split the applied and inertial parts:

$$
\int_{t_a}^{t_b}\sum_i\mathbf{F}_i^{appl}\cdot\delta\mathbf{r}_i dt-\int_{t_a}^{t_b}\sum_i m_i\mathbf{a}_i\cdot\delta\mathbf{r}_i dt=0
$$

For conservative applied forces, the applied-force virtual work is the negative variation of potential energy:

$$
\sum_i\mathbf{F}_i^{appl}\cdot\delta\mathbf{r}_i=-\delta V
$$

So the first term becomes:

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

Therefore the remaining integral is the variation of kinetic energy:

$$
\sum_i m_i\mathbf{v}_i\cdot\delta\mathbf{v}_i=\delta T
$$

So:

$$
\int_{t_a}^{t_b}\sum_i m_i\mathbf{a}_i\cdot\delta\mathbf{r}_i dt=\left[\sum_i m_i\mathbf{v}_i\cdot\delta\mathbf{r}_i\right]_{t_a}^{t_b}-\int_{t_a}^{t_b}\delta T dt
$$

Now use Hamilton's fixed endpoint condition:

$$
\delta\mathbf{r}_i(t_a)=\delta\mathbf{r}_i(t_b)=0
$$

This makes the boundary term vanish:

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

Because the endpoints in time are fixed, the variation can be moved outside the integral:

$$
\delta\int_{t_a}^{t_b}(T-V)dt=0
$$

With $L=T-V$, this is Hamilton's principle:

$$
\delta\int_{t_a}^{t_b}L dt=0
$$

## What To Remember

The point is not that the inertial complications never existed. The point is that, after integration by parts and fixed endpoint variations, the difficult inertial boundary contribution no longer affects the variational equation. The motion can then be found from the action built from $T-V$.

## Links To Concept Notes

- [Virtual Work and D'Alembert's Principle](../../../Mechanics/Virtual%20Work%20and%20DAlemberts%20Principle.md)
- [Action Principle](../../../Mechanics/Action%20Principle.md)
- [Hamilton's Principle](../../../Mechanics/Hamiltons%20Principle.md)
- [Lagrangian Mechanics](../../../Mechanics/Lagrangian%20Mechanics.md)
- [Calculus of Variations](../../../Mathematics/Calculus%20of%20Variations.md)

<!-- semantic-edges
{"source":"Hamilton's Principle","relation":"DERIVES_FROM","target":"D'Alembert's Principle","evidence_heading":"From Instantaneous Balance To A Path Condition","evidence_summary":"The note explains that Chapter 6 embeds D'Alembert's instantaneous dynamical virtual-work balance inside a time integral.","confidence":0.95}
{"source":"Hamilton's Principle","relation":"REQUIRES","target":"Fixed Endpoint Variations","evidence_heading":"The Key Rearrangement","evidence_summary":"The integration-by-parts boundary term vanishes because the endpoint variations are fixed to zero.","confidence":0.92}
{"source":"Hamilton's Principle","relation":"REFORMULATES","target":"Dynamical Virtual Work","evidence_heading":"What To Remember","evidence_summary":"The action statement retains the dynamical content after the inertial boundary contribution is removed by fixed endpoints.","confidence":0.9}
-->
