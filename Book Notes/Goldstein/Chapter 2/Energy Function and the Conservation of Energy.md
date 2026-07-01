# Energy Function and the Conservation of Energy

Source: [Classical Mechanics](../../../References/GoldsteinPooleSafkoClassicalMechanics.pdf)

Book hub: [Goldstein](../Goldstein.md)

Book section: 2.7, printed pages 61-63.

Previous: [Conservation Theorems and Symmetry Properties](Conservation%20Theorems%20and%20Symmetry%20Properties.md)

## Reading Status

- Status: started
- Pages: 61-63
- Date started: 2026-06-19
- Date finished:

## Derivation

Take the total derivative of $L(q,\dot q,t)$ and use Lagrange's equations to combine the coordinate and velocity terms. The result is:

$$
\frac{d}{dt}\left(\sum_j\dot q_j\frac{\partial L}{\partial\dot q_j}-L\right)+\frac{\partial L}{\partial t}=0
$$

Define the energy function:

$$
h(q,\dot q,t)=\sum_j\dot q_j\frac{\partial L}{\partial\dot q_j}-L
$$

Then:

$$
\frac{dh}{dt}=-\frac{\partial L}{\partial t}
$$

If $L$ has no explicit time dependence, $h$ is conserved.

## When It Equals Total Energy

Suppose the Lagrangian separates by degree in the generalized velocities:

$$
L=L_0+L_1+L_2
$$

where $L_k$ is homogeneous of degree $k$ in $\dot q$. Euler's theorem gives:

$$
h=L_2-L_0
$$

If the coordinate transformation is time independent and the potential is velocity independent, then $L_2=T$ and $L_0=-V$, so:

$$
h=T+V=E
$$

## Two Separate Questions

The conditions below must not be conflated:

1. Is $h$ conserved? This requires $\partial L/\partial t=0$.
2. Is $h$ the physical total energy $T+V$? This requires the appropriate velocity homogeneity and usually time-independent coordinates with a velocity-independent potential.

It is possible for $h$ to be conserved without equaling total energy, or to equal total energy while not being conserved.

## Dissipation

With a quadratic Rayleigh dissipation function $\mathcal F$:

$$
\frac{dh}{dt}=-2\mathcal F-\frac{\partial L}{\partial t}
$$

When $h=E$ and $L$ has no explicit time dependence:

$$
\frac{dE}{dt}=-2\mathcal F
$$

## Hamiltonian Connection

The energy function has the same value as the Hamiltonian after the Legendre transformation, but Goldstein keeps separate notation here because $h$ is expressed using $(q,\dot q)$ whereas $H$ is a function of independent phase-space variables $(q,p)$.

## Links To Concept Notes

- [Energy Function](../../../Mechanics/Energy%20Function.md)
- [Conservation Laws](../../../Mechanics/Conservation%20Laws.md)
- [Rayleigh Dissipation Function](../../../Mechanics/Rayleigh%20Dissipation%20Function.md)
- [Hamiltonian Mechanics](../../../Mechanics/Hamiltonian%20Mechanics.md)

<!-- semantic-edges
{"source":"Goldstein Section 2.7","relation":"INTRODUCES","target":"Energy Function","evidence_heading":"Derivation","evidence_summary":"Defines h as the velocity-momentum contraction minus the Lagrangian and derives its time derivative from Lagrange's equations.","confidence":0.92}
{"source":"Goldstein Section 2.7","relation":"DERIVES","target":"Energy Function Conservation Condition","evidence_heading":"Derivation","evidence_summary":"If the Lagrangian has no explicit time dependence, the energy function is conserved.","confidence":0.9}
{"source":"Velocity Homogeneity","relation":"DETERMINES","target":"Energy Function Equals Total Energy","evidence_heading":"When It Equals Total Energy","evidence_summary":"The energy function equals total energy under the appropriate velocity homogeneity and usual time-independent coordinate and potential assumptions.","confidence":0.89}
{"source":"Energy Function Conservation","relation":"CONTRASTS_WITH","target":"Total Energy Equality","evidence_heading":"Two Separate Questions","evidence_summary":"Goldstein separates whether h is conserved from whether h equals the physical total energy T plus V.","confidence":0.91}
{"source":"Rayleigh Dissipation Function","relation":"DETERMINES","target":"Mechanical Energy Loss Rate","evidence_heading":"Dissipation","evidence_summary":"With quadratic Rayleigh dissipation and no explicit time dependence, total energy decreases at twice the dissipation function.","confidence":0.88}
{"source":"Energy Function","relation":"REFORMULATES","target":"Hamiltonian","evidence_heading":"Hamiltonian Connection","evidence_summary":"The energy function has the same value as the Hamiltonian after the Legendre transform, though it is expressed in q and qdot rather than q and p.","confidence":0.88}
-->
