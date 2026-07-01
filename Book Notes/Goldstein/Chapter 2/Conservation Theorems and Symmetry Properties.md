# Conservation Theorems and Symmetry Properties

Source: [Classical Mechanics](../../../References/GoldsteinPooleSafkoClassicalMechanics.pdf)

Book hub: [Goldstein](../Goldstein.md)

Book section: 2.6, printed pages 55-61.

Previous: [Advantages of a Variational Principle Formulation](Advantages%20of%20a%20Variational%20Principle%20Formulation.md)

Next: [Energy Function and the Conservation of Energy](Energy%20Function%20and%20the%20Conservation%20of%20Energy.md)

## Reading Status

- Status: started
- Pages: 55-61
- Date started: 2026-06-19
- Date finished:

## First Integrals

Complete integration of $n$ second-order equations requires $2n$ constants, but useful first integrals can reveal the motion without a full solution. They have the form:

$$
f(q,\dot q,t)=\text{constant}
$$

## Generalized Momentum

The momentum conjugate to $q_j$ is:

$$
p_j=\frac{\partial L}{\partial\dot q_j}
$$

It need not have the dimensions of ordinary linear momentum. With velocity-dependent potentials, even a Cartesian canonical momentum can differ from mechanical momentum.

## Cyclic Coordinates

If $q_j$ does not appear explicitly in $L$, then:

$$
\frac{\partial L}{\partial q_j}=0
$$

and Lagrange's equation gives:

$$
\dot p_j=0
$$

Thus the conjugate momentum of an independent cyclic coordinate is conserved. A coordinate that appears absent but is linked to others by an uneliminated constraint does not justify this conclusion.

For a charged particle in a field independent of $x$:

$$
p_x=m\dot x+qA_x
$$

is conserved. The mechanical part $m\dot x$ need not be conserved separately.

## Translation Symmetry

If changing $q_j$ translates the whole system along unit vector $\mathbf n$, then:

$$
\frac{\partial\mathbf r_i}{\partial q_j}=\mathbf n
$$

The generalized force is the total force component $\mathbf n\cdot\mathbf F$, and $p_j$ is the corresponding component of total linear momentum. Translation invariance makes $q_j$ cyclic and conserves that momentum component.

## Rotation Symmetry

For an infinitesimal rotation about $\mathbf n$:

$$
\frac{\partial\mathbf r_i}{\partial q_j}=\mathbf n\times\mathbf r_i
$$

The generalized force becomes the component of total torque about $\mathbf n$, while $p_j$ becomes the corresponding angular-momentum component. Rotational invariance therefore conserves that component.

## Symmetry Reading Rule

- Invariance under translation along an axis implies conservation of the corresponding linear momentum.
- Invariance under rotation about an axis implies conservation of the corresponding angular momentum.
- Full spherical symmetry implies conservation of all angular-momentum components.

Goldstein presents these as the symmetry content of cyclic coordinates and points forward to the more general Noether theorem.

## Links To Concept Notes

- [Cyclic Coordinates](../../../Mechanics/Cyclic%20Coordinates.md)
- [Canonical Momentum](../../../Mechanics/Canonical%20Momentum.md)
- [Symmetries](../../../Mechanics/Symmetries.md)
- [Conservation Laws](../../../Mechanics/Conservation%20Laws.md)

<!-- semantic-edges
{"source":"Goldstein Section 2.6","relation":"INTRODUCES","target":"First Integrals","evidence_heading":"First Integrals","evidence_summary":"Presents first integrals as conserved quantities that reveal motion without a complete solution.","confidence":0.88}
{"source":"Cyclic Coordinates","relation":"DETERMINES","target":"Conserved Canonical Momentum","evidence_heading":"Cyclic Coordinates","evidence_summary":"If an independent coordinate is absent from the Lagrangian, its conjugate momentum is conserved.","confidence":0.9}
{"source":"Velocity-Dependent Potentials","relation":"CONTRASTS_WITH","target":"Mechanical Momentum Conservation","evidence_heading":"Generalized Momentum","evidence_summary":"With velocity-dependent potentials, a conserved Cartesian canonical momentum can differ from mechanical momentum.","confidence":0.88}
{"source":"Translation Invariance","relation":"DETERMINES","target":"Linear Momentum Conservation","evidence_heading":"Translation Symmetry","evidence_summary":"Translation invariance makes the associated coordinate cyclic and conserves the corresponding linear momentum component.","confidence":0.9}
{"source":"Rotation Invariance","relation":"DETERMINES","target":"Angular Momentum Conservation","evidence_heading":"Rotation Symmetry","evidence_summary":"Rotational invariance makes the associated coordinate cyclic and conserves the corresponding angular-momentum component.","confidence":0.9}
{"source":"Cyclic Coordinate Symmetry Reading","relation":"MOTIVATES","target":"Noether Theorem","evidence_heading":"Symmetry Reading Rule","evidence_summary":"Goldstein presents cyclic-coordinate conservation as the symmetry content that points toward Noether's theorem.","confidence":0.88}
-->
