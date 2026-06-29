# Constraints and Kinematical Conditions

Source: [The Lazy Universe](../../../References/Coopersmith2017TheLazyUniverse.pdf)

Book hub: [Coopersmith](../Coopersmith.md)

Book section: 4.8-4.9, printed pages 74-78.

Previous: [Generalized Coordinates](Generalized%20Coordinates.md)

Next: [Examples Using the Principle of Virtual Work](Examples%20Using%20the%20Principle%20of%20Virtual%20Work.md)

## Reading Status

- Status: started
- Pages: 74-78
- Date started: 2026-06-28
- Date finished:

## Big Ideas

- Constraints may be explicit equations or implicit kinematical conditions.
- A geometric constraint is physically maintained by reaction forces at the microscopic level.
- Applied forces are absorbed into generalized forces; internal reaction forces are avoided by choosing compatible virtual displacements.
- A compatible virtual displacement is perpendicular to the relevant reaction force.

## Two Kinds Of Forces

Coopersmith distinguishes applied forces from constraint forces.

Applied forces are given by the problem or determined as ordinary mathematical functions. In the generalized-coordinate formulation, they become generalized forces.

Constraint, internal, or reaction forces are usually unknown and microscopic in origin. They can be ignored when the virtual displacements are chosen in harmony with the constraints.

## Harmony With Constraints

For a pendulum, a harmonious virtual displacement changes the bob's angular position without stretching the cord. For a lever, a harmonious virtual displacement rotates the lever gently about the fulcrum without bending it or dislodging it.

This is the answer to why the internal constraints can be removed: the allowed virtual displacement lies along the constraint surface, while the ideal reaction force is normal to that surface. Their dot product is zero, so the reaction force does no virtual work.

## Mechanics And Geometry

Coopersmith stresses that variational mechanics blends geometry and physics. Geometry describes the allowed directions of motion, but physical reaction forces enforce those directions.

This is why the principle of virtual work can treat a whole constrained body in one scalar condition. Newtonian mechanics would have to track the internal forces particle by particle; virtual work only needs the allowed virtual motions.

## Links To Concept Notes

- [Constraints](../../../Mechanics/Constraints.md)
- [Virtual Work and D'Alembert's Principle](../../../Mechanics/Virtual%20Work%20and%20DAlemberts%20Principle.md)
- [Generalized Coordinates](../../../Mechanics/Generalized%20Coordinates.md)

<!-- semantic-edges
{"source":"Compatible Virtual Displacements","relation":"ELIMINATE","target":"Internal Constraint Forces","evidence_heading":"Harmony With Constraints","evidence_summary":"Allowed virtual displacements lie along the constraint surface while ideal reaction forces are normal to it, giving zero virtual work.","confidence":0.95}
{"source":"Constraints","relation":"ENFORCED_BY","target":"Reaction Forces","evidence_heading":"Two Kinds Of Forces","evidence_summary":"Coopersmith describes geometric constraints as physically maintained by microscopic reaction forces.","confidence":0.9}
{"source":"Principle of Virtual Work","relation":"TREATS_AS_SINGLE_SYSTEM","target":"Constrained Body","evidence_heading":"Mechanics And Geometry","evidence_summary":"Virtual work treats the whole constrained body in one scalar condition instead of tracking internal forces particle by particle.","confidence":0.9}
-->
