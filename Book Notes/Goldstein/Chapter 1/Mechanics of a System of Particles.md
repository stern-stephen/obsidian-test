# Mechanics of a System of Particles

Source: [Classical Mechanics](../../../References/GoldsteinPooleSafkoClassicalMechanics.pdf)

Book hub: [Goldstein](../Goldstein.md)

Book section: 1.2, printed pages 5-12.

Previous: [Mechanics of a Particle](Mechanics%20of%20a%20Particle.md)

Next: [Constraints](Constraints.md)

## Reading Status

- Status: started
- Pages: 5-12
- Date started: 2026-06-14
- Date finished:

## Big Ideas

- Internal forces cancel from the center-of-mass equation when they obey the weak action-reaction law.
- Angular momentum conservation requires the stronger condition that internal forces also be central.
- Total angular momentum and kinetic energy separate into center-of-mass motion plus motion relative to the center of mass.
- For conservative pair forces, the total potential energy includes each interacting pair once.

## Center Of Mass

For total mass $M=\sum_i m_i$, define:

$$
\mathbf{R}=\frac{1}{M}\sum_i m_i\mathbf{r}_i
$$

If internal forces occur in equal and opposite pairs:

$$
M\ddot{\mathbf{R}}=\mathbf{F}^{(e)}
$$

The total momentum is:

$$
\mathbf{P}=\sum_i \mathbf{p}_i=M\dot{\mathbf{R}}
$$

Therefore zero total external force implies conservation of total linear momentum.

## Weak And Strong Action-Reaction Laws

Weak law:

$$
\mathbf{F}_{ij}=-\mathbf{F}_{ji}
$$

- Strong law: the forces are also directed along the line joining particles $i$ and $j$.

The weak law is enough for the center-of-mass momentum theorem. The strong law is needed for internal torques to cancel, giving:

$$
\frac{d\mathbf{L}}{dt}=\mathbf{N}^{(e)}
$$

When mechanical action-reaction fails, as it can for moving charges, field momentum or field angular momentum may need to be included in the conserved total.

## Separation About The Center Of Mass

Write:

$$
\mathbf{r}_i=\mathbf{R}+\mathbf{r}'_i
$$

Because $\mathbf{r}'_i=\mathbf{r}_i-\mathbf{R}$ and $M\mathbf{R}=\sum_i m_i\mathbf{r}_i$ by definition,

$$
\sum_i m_i\mathbf{r}'_i=\sum_i m_i\mathbf{r}_i-\mathbf{R}\sum_i m_i=M\mathbf{R}-M\mathbf{R}=0
$$

Thus the mass-weighted relative positions vanish identically; this is what removes the cross terms in the center-of-mass separation. See [Center of Mass](../../../Mechanics/Center%20of%20Mass.md) for the general identity and its time derivative.

Then total angular momentum separates as:

$$
\mathbf{L}=\mathbf{R}\times M\dot{\mathbf{R}}+\sum_i \mathbf{r}'_i\times\mathbf{p}'_i
$$

Likewise, the kinetic energy separates as:

$$
T=\frac{1}{2}M\dot{\mathbf{R}}^2+\frac{1}{2}\sum_i m_i\mathbf{v}'_i{}^2
$$

The first term describes bulk translation; the second describes internal motion about the center of mass.

## Potential Energy

For external potentials $V_i$ and conservative pair potentials $V_{ij}$:

$$
V=\sum_i V_i+\frac{1}{2}\sum_{i\ne j}V_{ij}
$$

The factor $1/2$ removes double counting. If all forces are conservative, $T+V$ is conserved.

For a rigid body, all pair distances are fixed. The internal forces therefore do no work, and the internal potential is constant.

## Common Confusions

- Equal and opposite internal forces do not automatically imply zero internal torque; they must also be central.
- The center-of-mass theorem says how the center of mass moves, not that the particles move together.
- Angular momentum generally depends on the origin.
- Internal potential energy is not generally constant; rigidity is the special case.

## Links To Concept Notes

- [Conservation Laws](../../../Mechanics/Conservation%20Laws.md)
- [Center of Mass](../../../Mechanics/Center%20of%20Mass.md)
- [Two-Body Problem](../../../Mechanics/Two-Body%20Problem.md)

<!-- semantic-edges
{"source":"Goldstein Section 1.2","relation":"INTRODUCES","target":"Many-Particle Conservation Theorems","evidence_heading":"Big Ideas","evidence_summary":"Extends particle conservation laws to systems of particles while tracking assumptions about external and internal forces.","confidence":0.9}
{"source":"Weak Action-Reaction Law","relation":"ENABLES","target":"Center-of-Mass Momentum Theorem","evidence_heading":"Weak And Strong Action-Reaction Laws","evidence_summary":"Equal and opposite internal forces are enough for internal forces to cancel from the center-of-mass equation.","confidence":0.89}
{"source":"Strong Action-Reaction Law","relation":"ENABLES","target":"Angular Momentum Conservation","evidence_heading":"Weak And Strong Action-Reaction Laws","evidence_summary":"Internal forces must also be central for internal torques to cancel in the angular momentum theorem.","confidence":0.88}
{"source":"Center-of-Mass Decomposition","relation":"REFORMULATES","target":"Many-Particle Kinetic Energy","evidence_heading":"Separation About The Center Of Mass","evidence_summary":"Separates total kinetic energy into bulk center-of-mass motion and internal motion about the center of mass.","confidence":0.89}
{"source":"Conservative Pair Forces","relation":"DETERMINES","target":"Many-Particle Potential Energy","evidence_heading":"Potential Energy","evidence_summary":"Builds total potential energy from external potentials and pair potentials with a factor that removes double counting.","confidence":0.87}
-->
