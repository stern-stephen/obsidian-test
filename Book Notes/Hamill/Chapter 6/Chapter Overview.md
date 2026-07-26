# Chapter Overview

Source: [Hamill](../../../References/Hamill.pdf)

Book hub: [Hamill](../Hamill.md)

Book chapter: 6, printed pages 134-143.

PDF reference: [Hamill PDF](../../../References/Hamill.pdf). In this file, Hamill printed page 134 is PDF page 146.

Previous: [Chapter 5 - Canonical Transformations; Poisson Brackets](../Chapter%205/Chapter%20Overview.md)

Next: [Hamilton-Jacobi Equation](Hamilton-Jacobi%20Equation.md)

## Reading Status

- Status: started
- Pages: 134-143
- Date started: 2026-07-26
- Date finished:

## Big Ideas

- Hamilton-Jacobi theory tries to solve dynamics by finding a generating function that transforms to constant canonical variables.
- Hamilton's principal function $S$ is a type-$F_2$ generating function.
- Setting the transformed Hamiltonian $K$ to zero gives the Hamilton-Jacobi equation.
- Once $S$ is known, momenta and coordinates can be recovered from derivatives of $S$.
- For time-independent Hamiltonians, $S$ can often be separated into Hamilton's characteristic function plus a time term.
- Hamill uses the harmonic oscillator to show how the method recovers the usual sinusoidal solution.
- Hamilton's principal function differs from the action integral by at most an additive constant.
- The optical-mechanical analogy connects surfaces of constant action to wavefronts and helps motivate the Schrodinger equation.

## Section Notes

- [Hamilton-Jacobi Equation](Hamilton-Jacobi%20Equation.md)
- [Harmonic Oscillator and Principal Function](Harmonic%20Oscillator%20and%20Principal%20Function.md)
- [Schrodinger Connection and Problems](Schrodinger%20Connection%20and%20Problems.md)

## Logical Progression

1. Recast solving the equations of motion as finding a canonical transformation to constants.
2. Use a generating function $S(q,\alpha,t)$ to perform that transformation.
3. Set $K=0$ so the new variables are constant.
4. Derive $\partial S/\partial t+H(q,\partial S/\partial q,t)=0$.
5. Use derivatives of $S$ to recover $p_i$ and $q_i$.
6. Separate $S=W-\alpha t$ for autonomous systems.
7. Interpret $S$ as the action and connect constant-$S$ surfaces with wavefronts.
8. Sketch how the Hamilton-Jacobi equation points toward the time-independent Schrodinger equation.

## Links To Concept Notes

- [Hamilton-Jacobi Equation](../../../Mechanics/Hamilton-Jacobi%20Equation.md)
- [Hamiltonian Mechanics](../../../Mechanics/Hamiltonian%20Mechanics.md)
- [Canonical Transformations](../../../Mechanics/Canonical%20Transformations.md)
- [Action Principle](../../../Mechanics/Action%20Principle.md)
- [Schrodinger Equation](../../../Quantum%20Mechanics/Schrodinger%20Equation.md)
- [Wave-Particle Duality](../../../Quantum%20Mechanics/Wave-Particle%20Duality.md)

## Questions

- What makes solving one partial differential equation for $S$ equivalent to solving the full mechanical problem?
- Why does choosing $K=0$ make the transformed variables constants?
- How should Hamilton's principal function be distinguished from Hamilton's characteristic function?
- In what sense is Hamilton-Jacobi mechanics the classical limit of wave mechanics?

<!-- semantic-edges
{"source":"Hamill Chapter 6","relation":"INTRODUCES","target":"Hamilton-Jacobi Equation","evidence_heading":"Big Ideas","evidence_summary":"The chapter derives the Hamilton-Jacobi equation by using Hamilton's principal function as a generating function to transform to constants.","confidence":0.95}
{"source":"Hamilton-Jacobi Equation","relation":"USES","target":"Canonical Transformations","evidence_heading":"Logical Progression","evidence_summary":"The chapter recasts solving dynamics as finding a canonical transformation to constant variables.","confidence":0.92}
{"source":"Hamilton-Jacobi Theory","relation":"MOTIVATES","target":"Schrodinger Equation","evidence_heading":"Big Ideas","evidence_summary":"Hamill connects surfaces of constant action with wavefronts and sketches a route toward the time-independent Schrodinger equation.","confidence":0.88}
-->
