# Degrees of Freedom and Generalized Mechanics

Source: [The Lazy Universe](../../../References/Coopersmith2017TheLazyUniverse.pdf)

Book hub: [Coopersmith](../Coopersmith.md)

Book section: 3.3-3.4, printed pages 36-40.

Previous: [Coordinates and Time](Coordinates%20and%20Time.md)

Next: [Configuration Space and Invariants](Configuration%20Space%20and%20Invariants.md)

## Reading Status

- Status: started
- Pages: 36-40
- Date started: 2026-06-28
- Date finished:

## Big Ideas

- Degrees of freedom are the independent coordinates left after constraints or kinematical conditions are accounted for.
- A coordinate description may contain redundancy, but the system itself has a smallest independent coordinate count.
- Generalized mechanics replaces particles, Cartesian displacements, and forces with generalized particles, generalized displacements, and generalized forces.
- Generalized force is defined by its pairing with a generalized displacement to produce energy.

## Degrees Of Freedom

If $n$ coordinates describe a system and $m$ independent conditions relate them, then the number of independent coordinates is:

$$
n-m
$$

Coopersmith treats degrees of freedom as a property of the physical system at the scale being modeled. If an effect is not noticeable at the relevant scale, it does not need a coordinate in that model.

## Generalized Work

For ordinary particles, infinitesimal work has the form:

$$
dW=\sum_i\mathbf{F}_i\cdot d\mathbf{r}_i
$$

In generalized coordinates, Coopersmith writes the corresponding structure as:

$$
dW=\sum_i Q_i dq_i
$$

The $Q_i$ are generalized forces. They need not be vectors or have units of Newtons; the requirement is that $Q_i dq_i$ have units of energy.

## Interpretation

This section sets up Coopersmith's energy-centered view. Force is not discarded, but work becomes the more flexible object because it survives the move to arbitrary generalized coordinates.

## Links To Concept Notes

- [Generalized Coordinates](../../../Mechanics/Generalized%20Coordinates.md)
- [Constraints](../../../Mechanics/Constraints.md)
- [Lagrangian Mechanics](../../../Mechanics/Lagrangian%20Mechanics.md)

<!-- semantic-edges
{"source":"Degrees of Freedom","relation":"COUNT","target":"Independent Coordinates","evidence_heading":"Degrees Of Freedom","evidence_summary":"The note gives the degree-of-freedom count as the number of coordinates minus the number of independent conditions.","confidence":0.95}
{"source":"Constraints","relation":"REDUCE","target":"Degrees of Freedom","evidence_heading":"Degrees Of Freedom","evidence_summary":"Independent conditions among coordinates reduce the number of independent coordinates needed to describe the system.","confidence":0.95}
{"source":"Generalized Work","relation":"GENERALIZES","target":"Ordinary Work","evidence_heading":"Generalized Work","evidence_summary":"Coopersmith moves from ordinary force-displacement work to generalized forces paired with generalized coordinate changes.","confidence":0.95}
{"source":"Generalized Force","relation":"PAIRS_WITH","target":"Generalized Displacement","evidence_heading":"Generalized Work","evidence_summary":"The generalized force is defined by the requirement that its product with the generalized displacement have units of energy.","confidence":0.95}
-->
