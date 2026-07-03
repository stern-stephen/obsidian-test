# Symmetries and Conclusions

Source: [The Lazy Universe](../../../References/Coopersmith2017TheLazyUniverse.pdf)

Book hub: [Coopersmith](../Coopersmith.md)

Book section: 6.9-6.10, printed pages 134-142.

Previous: [Noether Energy and External Conditions](Noether%20Energy%20and%20External%20Conditions.md)

## Reading Status

- Status: started
- Pages: 134-142
- Date started: 2026-07-03
- Date finished:

## Big Ideas

- A symmetry means the Lagrangian does not depend on some coordinate.
- An absent coordinate leads to a conserved canonical momentum.
- Lagrangian mechanics is powerful because the same equation form survives changes of coordinates and models.
- The method is not unlimited: it relies on functional descriptions and local variational assumptions.

## Absent Coordinates

If the Lagrangian does not depend on a coordinate $q_k$, then:

$$
\frac{\partial L}{\partial q_k}=0
$$

Lagrange's equation gives:

$$
\frac{d}{dt}\frac{\partial L}{\partial \dot{q}_k}=0
$$

So the conjugate momentum is conserved:

$$
p_k=\frac{\partial L}{\partial \dot{q}_k}
$$

This is the coordinate-level version of the symmetry-to-conservation-law idea. Rotational symmetry gives angular-momentum conservation; translational symmetry gives linear-momentum conservation.

## Conclusions

Coopersmith closes the chapter by emphasizing the invariance of Lagrange's equations. Each new problem may require fresh coordinates and fresh $T$ and $V$ functions, but the equation form remains:

$$
\frac{d}{dt}\frac{\partial L}{\partial \dot{q}_i}-\frac{\partial L}{\partial q_i}=0
$$

The method is also local and conditional. It depends on functional forms, suitable coordinates or constraints, and variational assumptions. Those limits do not make it weak; they explain why it works so broadly where those assumptions are satisfied.

## Links To Concept Notes

- [Lagrangian Mechanics](../../../Mechanics/Lagrangian%20Mechanics.md)
- [Canonical Momentum](../../../Mechanics/Canonical%20Momentum.md)
- [Conservation Laws](../../../Mechanics/Conservation%20Laws.md)
- [Hamiltonian Mechanics](../../../Mechanics/Hamiltonian%20Mechanics.md)

<!-- semantic-edges
{"source":"Absent Coordinate","relation":"DETERMINES","target":"Canonical Momentum Conservation","evidence_heading":"Absent Coordinates","evidence_summary":"If L has no dependence on q_k, Lagrange's equation makes partial L over partial dot q_k constant.","confidence":0.95}
{"source":"Spatial Symmetry","relation":"DETERMINES","target":"Momentum Conservation","evidence_heading":"Absent Coordinates","evidence_summary":"The note identifies translational symmetry with conserved linear momentum and rotational symmetry with conserved angular momentum.","confidence":0.9}
{"source":"Lagrange Equations of Motion","relation":"CONTRASTS_WITH","target":"Coordinate Choice","evidence_heading":"Conclusions","evidence_summary":"The equation form remains invariant even though each problem may use fresh generalized coordinates and system-specific T and V functions.","confidence":0.88}
-->
