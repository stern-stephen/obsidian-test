# The Principle of Least Action and Lagrangian Mechanics

Source: [Principles of Quantum Mechanics](../../../References/Principals%20of%20quantum%20mechanics%20Shankar%20.pdf)

Book hub: [Shankar](../Shankar.md)

Book section: 2.1.

Previous: [Chapter Overview](Chapter%20Overview.md)

Next: [The Electromagnetic Lagrangian](The%20Electromagnetic%20Lagrangian.md)

## Reading Status

- Status: started
- Pages:
- Date started: 2026-05-19
- Date finished:

## Big Ideas

- Lagrangian mechanics reformulates dynamics as a condition on an entire path.
- The action is a functional: it takes a possible trajectory and returns a number.
- The physical path is stationary under small variations that keep the endpoints fixed.
- The Euler-Lagrange equations are the local differential equations that follow from the stationary-action condition.
- Generalized coordinates make the formalism useful for constrained systems.

## Notes

Shankar begins his classical review with the action because the path-based formulation has the closest structural resemblance to quantum mechanics. A trajectory is treated as a whole object, and the local Euler-Lagrange equations follow from varying that path with fixed endpoints.

The reusable action, variation, and Euler-Lagrange derivation lives in [Action Principle](../../../Mechanics/Action%20Principle.md) and [Euler-Lagrange Equations](../../../Mechanics/Euler-Lagrange%20Equations.md). Here the source-specific point is the bridge Shankar is building from classical trajectories to the later quantum formalism.

## Generalized Momentum

Shankar defines momentum through the Lagrangian rather than assuming it must be $m\mathbf{v}$. That choice prepares the electromagnetic example, where [canonical momentum](../../../Mechanics/Canonical%20Momentum.md) differs from mechanical momentum.

## Common Confusions

- "Least action" often really means stationary action, not always an absolute minimum.
- A generalized coordinate does not have to be a Cartesian position coordinate.
- The Lagrangian is not always total energy.
- The action is a number assigned to a whole path, not a force at one instant.

## Links To Concept Notes

- [Action Principle](../../../Mechanics/Action%20Principle.md)
- [Lagrangian Mechanics](../../../Mechanics/Lagrangian%20Mechanics.md)
- [Euler-Lagrange Equations](../../../Mechanics/Euler-Lagrange%20Equations.md)
- [Generalized Coordinates](../../../Mechanics/Generalized%20Coordinates.md)
- [Conservation Laws](../../../Mechanics/Conservation%20Laws.md)

<!-- semantic-edges
{"source":"Shankar Section 2.1","relation":"INTRODUCES","target":"Lagrangian Mechanics","evidence_heading":"Big Ideas","evidence_summary":"Introduces Lagrangian mechanics as a reformulation of dynamics through stationary paths rather than instantaneous force laws.","confidence":0.92}
{"source":"Shankar Section 2.1","relation":"MOTIVATES","target":"Action Principle","evidence_heading":"Notes","evidence_summary":"Begins with action because the path-based formulation most directly resembles later quantum mechanics.","confidence":0.9}
{"source":"Shankar Section 2.1","relation":"INTRODUCES","target":"Euler-Lagrange Equations","evidence_heading":"Big Ideas","evidence_summary":"Presents the Euler-Lagrange equations as the local differential equations obtained from stationary action.","confidence":0.9}
{"source":"Generalized Momentum","relation":"MOTIVATES","target":"Canonical Momentum","evidence_heading":"Generalized Momentum","evidence_summary":"Defines momentum through the Lagrangian, preparing examples where canonical momentum differs from mechanical momentum.","confidence":0.88}
-->
