# Canonical Transformations

Source: [Hamill](../../../References/Hamill.pdf)

Book hub: [Hamill](../Hamill.md)

Chapter overview: [Chapter Overview](Chapter%20Overview.md)

Book sections: 5.1-5.2, printed pages 109-117.

Previous: [Chapter Overview](Chapter%20Overview.md)

Next: [Poisson Brackets](Poisson%20Brackets.md)

## Reading Status

- Status: started
- Pages: 109-117
- Date started: 2026-07-26
- Date finished:

## Purpose

Hamill motivates canonical transformations as the Hamiltonian route to solving dynamics. The hope is to transform to variables in which the equations become easy, ideally because the new Hamiltonian has cyclic coordinates or even becomes trivial.

## 5.1 Integrating The Equations Of Motion

Lagrange's equations are $n$ coupled second-order differential equations. Hamilton's equations are $2n$ coupled first-order equations:

$$
\dot q_i=\frac{\partial H}{\partial p_i}
$$

$$
\dot p_i=-\frac{\partial H}{\partial q_i}
$$

Hamill emphasizes that Hamiltonian mechanics gives a more systematic theoretical path toward integration because the variables $q_i$ and $p_i$ can both be transformed as phase-space coordinates.

The long-term aim is to find new variables $(Q_i,P_i)$ in which the equations are easier to integrate. Chapter 6 will make this explicit through Hamilton-Jacobi theory.

## 5.2 Definition

A canonical transformation takes:

$$
(q_i,p_i)\rightarrow(Q_i,P_i)
$$

such that Hamilton's equations keep their form:

$$
\dot Q_i=\frac{\partial K}{\partial P_i}
$$

$$
\dot P_i=-\frac{\partial K}{\partial Q_i}
$$

The transformed Hamiltonian $K(Q,P,t)$ generally has a different functional form from $H(q,p,t)$.

## Generating Functions

Hamill derives canonical transformations from the modified Hamilton principle. The key identity is:

$$
\sum_i p_i\dot q_i-H=\sum_i P_i\dot Q_i-K+\frac{dF}{dt}
$$

The total time derivative does not change the variational principle because endpoint variations vanish. This gives room for a generating function $F$.

For a generating function of type:

$$
F_1=F_1(q,Q,t)
$$

the transformation rules are:

$$
p_i=\frac{\partial F_1}{\partial q_i}
$$

$$
P_i=-\frac{\partial F_1}{\partial Q_i}
$$

$$
K=H+\frac{\partial F_1}{\partial t}
$$

Other useful generating functions are:

$$
F_2(q,P,t),\quad F_3(p,Q,t),\quad F_4(p,P,t)
$$

For example, $F_2(q,P,t)$ gives:

$$
p_i=\frac{\partial F_2}{\partial q_i}
$$

$$
Q_i=\frac{\partial F_2}{\partial P_i}
$$

$$
K=H+\frac{\partial F_2}{\partial t}
$$

## Momentum And Coordinate Can Trade Places

Hamill's simple example $F_1=qQ$ produces:

$$
P=-q,\quad Q=p
$$

This illustrates the phase-space nature of Hamiltonian mechanics: a canonical transformation can exchange what used to be momentum with what becomes a coordinate.

## Harmonic Oscillator Example

Hamill uses a canonical transformation to solve the harmonic oscillator by choosing a generating function that makes the new coordinate cyclic. The transformed Hamiltonian becomes:

$$
K=\omega P
$$

Then $P$ is constant and:

$$
\dot Q=\omega
$$

so:

$$
Q=\omega t+\beta
$$

Transforming back gives the familiar sinusoidal oscillator solution. Hamill notes that this is overpowered for a simple oscillator, but conceptually important: canonical transformations can turn dynamics into near-trivial integration.

## Links To Concept Notes

- [Canonical Transformations](../../../Mechanics/Canonical%20Transformations.md)
- [Hamiltonian Mechanics](../../../Mechanics/Hamiltonian%20Mechanics.md)
- [Phase Space](../../../Mechanics/Phase%20Space.md)
- [Cyclic Coordinates](../../../Mechanics/Cyclic%20Coordinates.md)

<!-- semantic-edges
{"source":"Canonical Transformations","relation":"PRESERVES","target":"Hamilton's Equations","evidence_heading":"5.2 Definition","evidence_summary":"The note defines canonical transformations by the preservation of Hamilton's equations in the transformed variables Q and P.","confidence":0.95}
{"source":"Generating Functions","relation":"GENERATES","target":"Canonical Transformations","evidence_heading":"Generating Functions","evidence_summary":"The note derives transformation rules from modified Hamilton's principle using generating functions F1 through F4.","confidence":0.94}
-->
