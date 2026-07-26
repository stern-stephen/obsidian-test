# Harmonic Oscillator and Principal Function

Source: [Hamill](../../../References/Hamill.pdf)

Book hub: [Hamill](../Hamill.md)

Chapter overview: [Chapter Overview](Chapter%20Overview.md)

Book sections: 6.2-6.3, printed pages 137-140.

Previous: [Hamilton-Jacobi Equation](Hamilton-Jacobi%20Equation.md)

Next: [Schrodinger Connection and Problems](Schrodinger%20Connection%20and%20Problems.md)

## Reading Status

- Status: started
- Pages: 137-140
- Date started: 2026-07-26
- Date finished:

## Purpose

Hamill uses the harmonic oscillator to show how the Hamilton-Jacobi method works when the Hamiltonian is time independent and the principal function can be separated.

## 6.2 Harmonic Oscillator

For a harmonic oscillator:

$$
H=\frac{1}{2m}\left(p^2+m^2\omega^2q^2\right)
$$

The Hamilton-Jacobi equation is:

$$
\frac{1}{2m}\left[\left(\frac{\partial S}{\partial q}\right)^2+m^2\omega^2q^2\right]+\frac{\partial S}{\partial t}=0
$$

Because $H$ has no explicit time dependence, separate:

$$
S(q,\alpha,t)=W(q,\alpha)-\alpha t
$$

The constant $\alpha$ is the energy:

$$
\alpha=E
$$

The time-independent equation for Hamilton's characteristic function is:

$$
\frac{1}{2m}\left[\left(\frac{dW}{dq}\right)^2+m^2\omega^2q^2\right]=\alpha
$$

so:

$$
W=\int \sqrt{2m\alpha-m^2\omega^2q^2} dq
$$

## Recovering The Oscillator Solution

The principal function gives:

$$
\beta=\frac{\partial S}{\partial \alpha}
$$

Solving for $q$ gives:

$$
q=\sqrt{\frac{2\alpha}{m\omega^2}}\sin(\omega t+\beta)
$$

The momentum is:

$$
p=\frac{\partial S}{\partial q}
$$

which gives:

$$
p=\sqrt{2m\alpha}\cos(\omega t+\beta)
$$

The constants $\alpha$ and $\beta$ are then fixed by initial position and momentum. In this example, $\alpha$ is the energy and $\beta$ is the phase.

## Hamilton's Characteristic Function

When the Hamiltonian is autonomous and separation works, write:

$$
S=W-\alpha t
$$

Here $S$ is Hamilton's principal function, while $W$ is Hamilton's characteristic function.

The characteristic function solves the time-independent Hamilton-Jacobi equation. This distinction matters because $S$ includes time, while $W$ describes the reduced spatial part of the action.

## 6.3 Principal Function And Action

Hamill shows that:

$$
\frac{dS}{dt}=L
$$

Therefore:

$$
S=\int Ldt+\text{constant}
$$

Hamilton's principal function differs from the action integral by at most an additive constant.

This gives $S$ a dual meaning:

- as a generating function for a canonical transformation to constants,
- as the action accumulated along the physical path.

## Links To Concept Notes

- [Hamilton-Jacobi Equation](../../../Mechanics/Hamilton-Jacobi%20Equation.md)
- [Action Principle](../../../Mechanics/Action%20Principle.md)
- [Hamiltonian Mechanics](../../../Mechanics/Hamiltonian%20Mechanics.md)

<!-- semantic-edges
{"source":"Hamilton's Characteristic Function","relation":"SPECIALIZES","target":"Hamilton's Principal Function","evidence_heading":"Hamilton's Characteristic Function","evidence_summary":"For autonomous systems, S separates into W minus alpha t, where W is the time-independent characteristic function.","confidence":0.9}
{"source":"Hamilton's Principal Function","relation":"EQUALS_UP_TO_CONSTANT","target":"Action Integral","evidence_heading":"6.3 Principal Function And Action","evidence_summary":"Hamill shows dS/dt = L, so S equals the integral of L dt plus a constant.","confidence":0.95}
-->
