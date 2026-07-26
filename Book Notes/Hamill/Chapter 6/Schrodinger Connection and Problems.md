# Schrodinger Connection and Problems

Source: [Hamill](../../../References/Hamill.pdf)

Book hub: [Hamill](../Hamill.md)

Chapter overview: [Chapter Overview](Chapter%20Overview.md)

Book sections: 6.4-6.5, printed pages 140-143.

Previous: [Harmonic Oscillator and Principal Function](Harmonic%20Oscillator%20and%20Principal%20Function.md)

## Reading Status

- Status: started
- Pages: 140-143
- Date started: 2026-07-26
- Date finished:

## Purpose

Hamill ends the chapter by using Hamilton-Jacobi theory as a bridge from classical mechanics to wave mechanics. The argument is not a full derivation of quantum mechanics, but it explains why the action function $S$ is a natural classical precursor to a wave phase.

## 6.4 Relationship To Schrodinger's Equation

De Broglie's relation connects wavelength and momentum:

$$
\lambda=\frac{h}{p}
$$

In geometrical optics, wavefronts are surfaces of constant phase. Hamill compares this with Hamilton-Jacobi theory, where surfaces of constant $S$ propagate in a way analogous to optical wavefronts.

This motivates a matter-wave expression of the form:

$$
\psi=\psi_0 e^{iS/\hbar}
$$

The phase is the classical action divided by $\hbar$, so the exponent is dimensionless.

## From Hamilton-Jacobi To A Wave Equation

For a one-dimensional particle in a potential:

$$
\frac{\partial S}{\partial t}+\frac{1}{2m}\left(\frac{\partial S}{\partial q}\right)^2+V=0
$$

For a stationary state, Hamill uses:

$$
\frac{\partial S}{\partial t}=-E
$$

and relates $\partial S/\partial q$ to derivatives of $\psi$. His sketch then leads to the time-independent Schrodinger equation:

$$
-\frac{\hbar^2}{2m}\frac{d^2\psi}{dq^2}+V\psi=E\psi
$$

The conceptual link is more important than the algebraic details: classical action becomes wave phase, and Hamilton-Jacobi theory supplies the classical equation whose wave version becomes quantum mechanics.

## Interpretation

Hamilton-Jacobi theory sits at a crossroads:

- it is classical mechanics written through an action function,
- it resembles geometrical optics through constant-action surfaces,
- it points toward wave mechanics when the action appears as a phase.

This is why Hamill treats the method as theoretically important even when it is not the most efficient computational route for elementary mechanics problems.

## Problems

The Chapter 6 problems ask for Hamilton-Jacobi solutions in systems including the relativistic Kepler problem, separable spherical-coordinate Hamiltonians, elliptic coordinates, a bead on a rotating hoop, and vertical motion in a gravitational field. The problems emphasize separation, construction of $S$, and recovery of motion from derivatives of $S$.

## Links To Concept Notes

- [Hamilton-Jacobi Equation](../../../Mechanics/Hamilton-Jacobi%20Equation.md)
- [Action Principle](../../../Mechanics/Action%20Principle.md)
- [Schrodinger Equation](../../../Quantum%20Mechanics/Schrodinger%20Equation.md)
- [Wave-Particle Duality](../../../Quantum%20Mechanics/Wave-Particle%20Duality.md)

<!-- semantic-edges
{"source":"Hamilton-Jacobi Theory","relation":"MOTIVATES","target":"Schrodinger Equation","evidence_heading":"6.4 Relationship To Schrodinger's Equation","evidence_summary":"The note describes Hamill's bridge from matter-wave phase psi = psi0 exp(iS/hbar) to the time-independent Schrodinger equation.","confidence":0.88}
{"source":"Classical Action","relation":"BECOMES","target":"Wave Phase","evidence_heading":"Interpretation","evidence_summary":"The note explains that Hamilton-Jacobi theory makes the classical action function play the role of a wave phase.","confidence":0.88}
-->
