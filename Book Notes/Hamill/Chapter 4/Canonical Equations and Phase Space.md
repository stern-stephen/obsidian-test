# Canonical Equations and Phase Space

Source: [Hamill](../../../References/Hamill.pdf)

Book hub: [Hamill](../Hamill.md)

Chapter overview: [Chapter Overview](Chapter%20Overview.md)

Book sections: 4.3-4.5, printed pages 98-103.

Previous: [Legendre Transformation and Hamiltonian](Legendre%20Transformation%20and%20Hamiltonian.md)

Next: [Routhian and Symplectic Notation](Routhian%20and%20Symplectic%20Notation.md)

## Reading Status

- Status: started
- Pages: 98-103
- Date started: 2026-07-26
- Date finished:

## Purpose

This section derives Hamilton's canonical equations and then gives their phase-space interpretation. Hamill presents the Hamiltonian both as a transformed function and as the generator of a new geometric picture of dynamics.

## 4.3 Hamilton's Canonical Equations

From the Legendre transform:

$$
H=\sum_i p_i\dot q_i-L
$$

the active-variable relation gives:

$$
\dot q_i=\frac{\partial H}{\partial p_i}
$$

Using Lagrange's equations and the passive-variable relation gives:

$$
\dot p_i=-\frac{\partial H}{\partial q_i}
$$

Together:

$$
\dot q_i=\frac{\partial H}{\partial p_i}
$$

$$
\dot p_i=-\frac{\partial H}{\partial q_i}
$$

These are Hamilton's canonical equations. They replace $n$ second-order Lagrange equations with $2n$ first-order equations.

## Time Dependence And Energy

Hamill derives:

$$
\frac{dH}{dt}=\frac{\partial H}{\partial t}
$$

and:

$$
\frac{\partial H}{\partial t}=-\frac{\partial L}{\partial t}
$$

Therefore, if the Lagrangian has no explicit time dependence, the Hamiltonian is constant.

Hamill also states the usual energy condition carefully: if the transformation equations do not depend explicitly on time and the potential depends only on coordinates, then the Hamiltonian equals total energy. In many quantum-mechanics uses one writes $H=T+V$, but this is not the definition and is not universally valid.

## 4.4 Modified Hamilton Principle

Using:

$$
L=\sum_i p_i\dot q_i-H
$$

Hamilton's principle becomes:

$$
\delta\int_{t_1}^{t_2}\left(\sum_i p_i\dot q_i-H(q_i,p_i,t)\right)dt=0
$$

Hamill calls this the modified Hamilton principle. Applying the Euler-Lagrange equation separately to the variables $q_i$ and $p_i$ yields Hamilton's equations again.

This is the variational route into Hamiltonian mechanics: the action is rewritten in phase-space variables, and the canonical equations follow from stationarity.

## 4.5 Phase Space And Phase Fluid

In Lagrangian mechanics, a system traces a path in configuration space. In Hamiltonian mechanics, the system traces a path in phase space, whose coordinates are both $q_i$ and $p_i$.

A configuration-space point alone does not specify a unique future path, because different velocities can pass through the same position. A phase-space point does specify a unique future path, because position and momentum together determine the phase-space velocity through Hamilton's equations.

Hamill uses the "phase fluid" analogy:

- each possible initial condition is a point in phase space,
- Hamilton's equations define the phase-space velocity field,
- trajectories act like streamlines,
- streamlines do not cross because the equations define a unique slope at each phase-space point.

For a time-independent Hamiltonian:

$$
\frac{dH}{dt}=0
$$

so motion remains on the energy surface:

$$
H=E
$$

Hamill previews the next chapter by saying the phase fluid will behave like an incompressible fluid, which leads into Liouville's theorem.

## Links To Concept Notes

- [Hamiltonian Mechanics](../../../Mechanics/Hamiltonian%20Mechanics.md)
- [Phase Space](../../../Mechanics/Phase%20Space.md)
- [Energy Function](../../../Mechanics/Energy%20Function.md)
- [Hamilton's Principle](../../../Mechanics/Hamiltons%20Principle.md)

<!-- semantic-edges
{"source":"Hamiltonian","relation":"DETERMINES","target":"Time Evolution","evidence_heading":"4.3 Hamilton's Canonical Equations","evidence_summary":"Hamilton's canonical equations give first-order time evolution for coordinates and momenta from derivatives of H.","confidence":0.95}
{"source":"Phase Space","relation":"CONSTRAINS","target":"Dynamical Trajectories","evidence_heading":"4.5 Phase Space And Phase Fluid","evidence_summary":"A phase-space point determines a unique trajectory because Hamilton's equations define a unique velocity field at each point.","confidence":0.9}
{"source":"Time-Independent Hamiltonian","relation":"IMPLIES","target":"Energy Conservation","evidence_heading":"Time Dependence And Energy","evidence_summary":"Hamill derives dH/dt = partial H/partial t and concludes that H is constant when it has no explicit time dependence.","confidence":0.9}
-->
