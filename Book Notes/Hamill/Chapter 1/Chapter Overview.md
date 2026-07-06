# Chapter 1 - Fundamental Concepts

Source: [Hamill](../../../References/Hamill.pdf)

Book hub: [Hamill](../Hamill.md)

Book chapter: 1, printed pages 3-43.

PDF reference: [Hamill PDF](../../../References/Hamill.pdf). In this file, Hamill printed page 3 is PDF page 15.

## Reading Status

- Status: started
- Pages: 3-43
- Date started: 2026-07-06
- Date finished:

## Chapter Focus

Hamill opens by setting up the vocabulary needed before the formal derivation of Lagrange's equations. The chapter is not yet mainly about Hamilton's principle or variational calculus. It is about the mechanical objects that later enter those tools: generalized coordinates, generalized velocities, constraints, virtual displacements, generalized forces, configuration space, phase space, equations of motion, and conservation laws.

The chapter's central practical message is that analytical mechanics replaces a particle-by-particle Cartesian force description with coordinates adapted to the system. Once the right coordinates are chosen, the equations of motion can often be obtained from scalar quantities rather than from every component of every force.

## 1.1 Kinematics

Book section: 1.1, printed pages 3-5.

Hamill begins with the kinematics of a particle: position, velocity, and acceleration. The point is not to rederive elementary vector mechanics, but to emphasize that the same physical motion can be described using different coordinate systems.

This prepares the shift to generalized coordinates. Cartesian coordinates are not privileged when constraints or symmetries make another coordinate description simpler.

## 1.2 Generalized Coordinates

Book section: 1.2, printed pages 5-7.

Generalized coordinates are a minimal independent set of coordinates that specify the configuration of a system. They do not need to be lengths. They may be angles, distances along a curve, or other parameters suited to the constraints.

For a system with $n$ degrees of freedom, use coordinates:

$$
q_1,q_2,\ldots,q_n
$$

The value of using generalized coordinates is that constraints can often be built into the coordinate choice. For example, a pendulum bob constrained to a circle can be described by one angle rather than by Cartesian coordinates plus a constraint equation.

## 1.3 Generalized Velocity

Book section: 1.3, printed pages 7-9.

Generalized velocities are the time derivatives of generalized coordinates:

$$
\dot q_i=\frac{dq_i}{dt}
$$

When Cartesian particle positions are written as functions of generalized coordinates and time,

$$
\mathbf{r}_j=\mathbf{r}_j(q_1,\ldots,q_n,t)
$$

the particle velocities follow by the chain rule:

$$
\mathbf{v}_j=\sum_i\frac{\partial\mathbf{r}_j}{\partial q_i}\dot q_i+\frac{\partial\mathbf{r}_j}{\partial t}
$$

This is one of the places where generalized-coordinate mechanics starts to become systematic: once positions are expressed in the chosen coordinates, velocities and kinetic energy can be generated mechanically.

## 1.4 Constraints

Book section: 1.4, printed pages 9-11.

Constraints reduce the number of independent degrees of freedom. Hamill distinguishes constraints that can be expressed as equations among coordinates from more general constraints involving velocities or inequalities.

A holonomic constraint can be written in the form:

$$
f(q_1,\ldots,q_n,t)=0
$$

Holonomic constraints are especially friendly to Lagrangian mechanics because they can often be solved by choosing independent generalized coordinates. Non-holonomic constraints require more care and return later in the book.

## 1.5 Virtual Displacements

Book section: 1.5, printed pages 11-12.

A virtual displacement is an imagined infinitesimal displacement compatible with the constraints at a fixed instant of time. It is not an actual time evolution of the system.

This fixed-time character matters. During a virtual displacement, time is held constant, and only the coordinates are varied in ways allowed by the constraints.

## 1.6 Virtual Work And Generalized Force

Book section: 1.6, printed pages 12-13.

Virtual work is the work done by forces during a virtual displacement. In generalized coordinates, the total virtual work can be written as:

$$
\delta W=\sum_i Q_i\delta q_i
$$

The coefficients $Q_i$ are generalized forces. They are not always ordinary force components; if $q_i$ is an angle, the corresponding generalized force is a torque-like quantity.

This section is a bridge from Newtonian force language to Lagrange's equations, where generalized forces pair naturally with generalized coordinate variations.

## 1.7 Configuration Space

Book section: 1.7, printed pages 13-15.

Configuration space is the space whose points represent complete configurations of the system. A system with $n$ degrees of freedom has an $n$-dimensional configuration space, with axes labeled by generalized coordinates.

The important shift is that a single point in configuration space represents the whole system, not just one particle's physical location.

## 1.8 Phase Space

Book section: 1.8, printed page 15.

Phase space records both positions and momenta. For $n$ generalized coordinates, the phase-space description uses pairs:

$$
(q_i,p_i)
$$

Hamill introduces phase space early because Hamiltonian mechanics will later use it as the natural state space.

## 1.9 Dynamics

Book section: 1.9, printed pages 15-18.

Hamill reviews Newton's laws and emphasizes that an equation of motion determines how the system evolves. In Newtonian mechanics the equation of motion is commonly obtained from:

$$
\mathbf{F}=\frac{d\mathbf{p}}{dt}
$$

or, for constant mass:

$$
\mathbf{F}=m\mathbf{a}
$$

The chapter then turns toward how analytical mechanics obtains equivalent equations in a different language.

## 1.10 Obtaining The Equation Of Motion

Book section: 1.10, printed pages 18-25.

Hamill contrasts the Newtonian and Lagrangian routes.

The Newtonian route writes force balances in coordinates and solves for acceleration. The Lagrangian route constructs:

$$
L=T-V
$$

and applies Lagrange's equations:

$$
\frac{d}{dt}\left(\frac{\partial L}{\partial \dot q_i}\right)-\frac{\partial L}{\partial q_i}=0
$$

At this stage in the book, Hamill presents Lagrange's equations as a working tool before deriving them fully. The formal variational derivation comes later, after the calculus of variations.

The worked examples show the method's appeal: the hard part is often choosing good generalized coordinates and writing $T$ and $V$ correctly. Once that is done, the equation-generation procedure is uniform.

## 1.11 Conservation Laws And Symmetry Principles

Book section: 1.11, printed pages 25-40.

Hamill introduces conservation laws through symmetry ideas before the full Noether theorem machinery appears.

If the Lagrangian does not depend on a coordinate $q_i$, that coordinate is cyclic, and its conjugate momentum is conserved:

$$
p_i=\frac{\partial L}{\partial \dot q_i}
$$

$$
\frac{dp_i}{dt}=0
$$

The chapter connects:

- translational symmetry with conservation of linear momentum;
- rotational symmetry with conservation of angular momentum;
- time-translation symmetry with conservation of an energy-like quantity.

Hamill also introduces the energy function:

$$
h=\sum_i\dot q_i\frac{\partial L}{\partial \dot q_i}-L
$$

When the Lagrangian has no explicit time dependence, this quantity is conserved. In many common mechanical systems it equals the total energy, but that equality depends on additional assumptions.

## 1.12 Problems

Book section: 1.12, printed pages 41-43.

The problems practice the chapter's core skills: choosing generalized coordinates, identifying constraints, constructing Lagrangians, recognizing cyclic coordinates, and relating symmetries to conserved quantities.

## What To Remember

- Generalized coordinates are chosen to match the system's degrees of freedom.
- Constraints can reduce the number of independent coordinates.
- Virtual displacements are fixed-time comparison displacements compatible with constraints.
- Generalized forces are the coefficients of generalized coordinate variations in virtual work.
- Configuration space stores complete configurations; phase space stores coordinates and momenta.
- Hamill presents Lagrange's equations as a practical equation-generating method before deriving them later.
- Cyclic coordinates reveal conserved canonical momenta.
- Conservation laws are tied to symmetry: translation, rotation, and time-translation invariance.

## Questions To Revisit

- When is a constraint best eliminated by coordinate choice, and when should it remain as an explicit constraint equation?
- How should one distinguish ordinary force components from generalized forces?
- In which examples does Hamill's energy function $h$ equal total mechanical energy, and when can it fail to do so?
- How does this chapter's early use of Lagrange's equations compare with the later derivation from Hamilton's principle?

## Links To Concept Notes

- [Generalized Coordinates](../../../Mechanics/Generalized%20Coordinates.md)
- [Constraints](../../../Mechanics/Constraints.md)
- [Virtual Work and D'Alembert's Principle](../../../Mechanics/Virtual%20Work%20and%20DAlemberts%20Principle.md)
- [Configuration Space](../../../Mechanics/Configuration%20Space.md)
- [Phase Space](../../../Mechanics/Phase%20Space.md)
- [Lagrangian Mechanics](../../../Mechanics/Lagrangian%20Mechanics.md)
- [Euler-Lagrange Equations](../../../Mechanics/Euler-Lagrange%20Equations.md)
- [Canonical Momentum](../../../Mechanics/Canonical%20Momentum.md)
- [Cyclic Coordinates](../../../Mechanics/Cyclic%20Coordinates.md)
- [Conservation Laws](../../../Mechanics/Conservation%20Laws.md)
- [Energy Function](../../../Mechanics/Energy%20Function.md)

<!-- semantic-edges
{"source":"Hamill Chapter 1","relation":"INTRODUCES","target":"Generalized Coordinates","evidence_heading":"1.2 Generalized Coordinates","evidence_summary":"Hamill introduces generalized coordinates as a minimal independent set of coordinates suited to the system's constraints and degrees of freedom.","confidence":0.92}
{"source":"Hamill Chapter 1","relation":"INTRODUCES","target":"Generalized Velocities","evidence_heading":"1.3 Generalized Velocity","evidence_summary":"The chapter defines generalized velocities as time derivatives of generalized coordinates and uses the chain rule to relate them to particle velocities.","confidence":0.9}
{"source":"Holonomic Constraints","relation":"ENABLES","target":"Generalized Coordinate Reduction","evidence_heading":"1.4 Constraints","evidence_summary":"The note explains that holonomic constraints can often be solved by choosing independent generalized coordinates.","confidence":0.9}
{"source":"Virtual Displacement","relation":"REQUIRES","target":"Fixed Time Variation","evidence_heading":"1.5 Virtual Displacements","evidence_summary":"Hamill treats virtual displacements as infinitesimal displacements compatible with constraints at a fixed instant of time.","confidence":0.9}
{"source":"Generalized Forces","relation":"REPRESENTS","target":"Virtual Work Coefficients","evidence_heading":"1.6 Virtual Work And Generalized Force","evidence_summary":"The note writes virtual work as a sum of generalized forces times generalized coordinate variations.","confidence":0.92}
{"source":"Hamill Chapter 1","relation":"CONTRASTS_WITH","target":"Configuration Space and Phase Space","evidence_heading":"1.7 Configuration Space","evidence_summary":"The chapter distinguishes configuration space as the space of complete configurations from phase space as the space of coordinates and momenta.","confidence":0.88}
{"source":"Hamill Chapter 1","relation":"INTRODUCES","target":"Lagrange's Equations","evidence_heading":"1.10 Obtaining The Equation Of Motion","evidence_summary":"Hamill presents Lagrange's equations as a working method for obtaining equations of motion before deriving them later.","confidence":0.9}
{"source":"Cyclic Coordinates","relation":"DETERMINES","target":"Conserved Canonical Momentum","evidence_heading":"1.11 Conservation Laws And Symmetry Principles","evidence_summary":"The note says that if the Lagrangian does not depend on a coordinate, its conjugate momentum is conserved.","confidence":0.92}
{"source":"Time-Independent Lagrangian","relation":"DETERMINES","target":"Energy Function Conservation","evidence_heading":"1.11 Conservation Laws And Symmetry Principles","evidence_summary":"Hamill introduces the energy function and states that it is conserved when the Lagrangian has no explicit time dependence.","confidence":0.9}
-->
