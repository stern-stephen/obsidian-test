# The Forms of T V and L

Source: [The Lazy Universe](../../../References/Coopersmith2017TheLazyUniverse.pdf)

Book hub: [Coopersmith](../Coopersmith.md)

Book section: 6.5-6.6, printed pages 118-129.

Previous: [Physical Meaning and Assumptions](Physical%20Meaning%20and%20Assumptions.md)

Next: [Noether Energy and External Conditions](Noether%20Energy%20and%20External%20Conditions.md)

## Reading Status

- Status: started
- Pages: 118-129
- Date started: 2026-07-03
- Date finished:

## Big Ideas

- In ordinary cases, $T$ has a more universal structure than $V$, but both depend on the chosen modeling of the system.
- $L=T-V$ is not the total energy. It is the action integrand whose variation gives the motion.
- Coopersmith follows Lanczos in treating $L$ as a balance between motion and configuration, not merely a formal subtraction.
- Different Lagrangians can produce the same equations of motion when they differ by harmless endpoint terms.

## The Form Of T

For usual mechanical systems, kinetic energy is positive and depends on generalized velocities. When the coordinates are time-independent, $T$ is typically quadratic in the generalized velocities. With time-dependent coordinate maps or moving constraints, $T$ can acquire terms that are linear in velocities or independent of velocities.

This explains why generalized-coordinate kinetic energy can look less familiar than the Cartesian expression $\frac{1}{2}mv^2$ while still representing the same physical motion.

## The Form Of V

The potential energy has no universal form. It depends on the system's interactions and configuration. Coopersmith also treats velocity-dependent potentials as part of the wider Lagrangian framework, especially because electromagnetism naturally leads to such terms.

In those cases, canonical momentum can differ from mechanical momentum:

$$
p_i=\frac{\partial L}{\partial \dot{q}_i}
$$

## Why L Equals T Minus V

Coopersmith presents $L=T-V$ as an interplay between the kinetic side of the system and the potential side. $T$ describes the motion that the system has, while $V$ encodes how configuration steers subsequent motion. The action integral tracks this balance over the full time interval.

The minus sign matters because potential energy contributes to the variational equation with the opposite sign from kinetic energy in the conservative-force case.

## Non-Uniqueness

The Lagrangian is not unique. Adding a total time derivative to $L$ changes the action by an endpoint term, and fixed endpoints leave the equations of motion unchanged. This is one reason the equations of motion are more invariant than any one displayed formula for $L$.

## Links To Concept Notes

- [Lagrangian Mechanics](../../../Mechanics/Lagrangian%20Mechanics.md)
- [Canonical Momentum](../../../Mechanics/Canonical%20Momentum.md)
- [Electromagnetic Lagrangian](../../../Mechanics/Electromagnetic%20Lagrangian.md)
- [Action Principle](../../../Mechanics/Action%20Principle.md)

<!-- semantic-edges
{"source":"Lagrangian","relation":"REPRESENTS","target":"Kinetic-Potential Balance","evidence_heading":"Why L Equals T Minus V","evidence_summary":"The note describes the Lagrangian as tracking the balance between kinetic motion and potential configuration over the time interval.","confidence":0.88}
{"source":"Velocity-Dependent Potentials","relation":"DETERMINES","target":"Canonical Momentum","evidence_heading":"The Form Of V","evidence_summary":"The note says velocity-dependent potentials can make canonical momentum differ from mechanical momentum through p_i = partial L / partial dot q_i.","confidence":0.9}
{"source":"Total Time Derivative","relation":"ELIMINATES","target":"Equation of Motion Change","evidence_heading":"Non-Uniqueness","evidence_summary":"Adding a total time derivative changes the action only by an endpoint term, so fixed endpoints leave the equations of motion unchanged.","confidence":0.9}
-->
