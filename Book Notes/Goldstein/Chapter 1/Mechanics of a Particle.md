# Mechanics of a Particle

Source: [Classical Mechanics](../../../References/GoldsteinPooleSafkoClassicalMechanics.pdf)

Book hub: [Goldstein](../Goldstein.md)

Book section: 1.1, printed pages 1-5.

Previous: [Chapter Overview](Chapter%20Overview.md)

Next: [Mechanics of a System of Particles](Mechanics%20of%20a%20System%20of%20Particles.md)

## Reading Status

- Status: started
- Pages: 1-5
- Date started: 2026-06-14
- Date finished:

## Big Ideas

- Newton's second law is fundamentally a statement about momentum, not merely acceleration.
- Linear momentum, angular momentum, and energy conservation follow under different physical conditions.
- The energy theorem requires care when the potential depends explicitly on time.
- An inertial frame is an idealized frame in which Newton's momentum equation holds.

## Notes

For position $\mathbf{r}$ and velocity $\mathbf{v}$:

$$
\mathbf{v}=\frac{d\mathbf{r}}{dt}
$$

Linear momentum is:

$$
\mathbf{p}=m\mathbf{v}
$$

Newton's second law is:

$$
\mathbf{F}=\frac{d\mathbf{p}}{dt}
$$

Only for constant mass does this reduce to:

$$
\mathbf{F}=m\mathbf{a}
$$

If the total force vanishes, linear momentum is conserved.

## Angular Momentum

About a chosen origin:

$$
\mathbf{L}=\mathbf{r}\times\mathbf{p}
$$

The torque is:

$$
\mathbf{N}=\mathbf{r}\times\mathbf{F}
$$

For constant mass:

$$
\mathbf{N}=\frac{d\mathbf{L}}{dt}
$$

Thus zero torque implies conservation of angular momentum. Both angular momentum and torque depend on the reference point.

## Work And Energy

The work done from point 1 to point 2 is:

$$
W_{12}=\int_1^2 \mathbf{F}\cdot d\mathbf{s}
$$

For constant mass:

$$
W_{12}=T_2-T_1
$$

where:

$$
T=\frac{1}{2}mv^2
$$

For a conservative force:

$$
\mathbf{F}=-\nabla V
$$

This follows from path-independent work: define $V(\mathbf{r})$ as minus the work from a fixed reference point to $\mathbf{r}$. Changing the endpoint by $d\mathbf{r}$ gives $dV=-\mathbf{F}\cdot d\mathbf{r}$, while the differential of a scalar field is $dV=\nabla V\cdot d\mathbf{r}$. Therefore $\mathbf{F}=-\nabla V$. See [Conservative Forces](../../../Mechanics/Conservative%20Forces.md) for the full proof and the necessary domain assumptions.

and:

$$
T+V=E=\text{constant}
$$

If $V(\mathbf{r},t)$ depends explicitly on time, a force may still be obtained from $-\nabla V$, but $T+V$ need not be conserved.

## Common Confusions

- $\mathbf{F}=m\mathbf{a}$ assumes constant mass; $\mathbf{F}=d\mathbf{p}/dt$ is the more general statement.
- Zero force and zero torque are different conditions and lead to different conservation laws.
- A conservative spatial force does not guarantee energy conservation when its potential depends explicitly on time.
- The additive zero of potential energy is arbitrary.

## Links To Concept Notes

- [Classical Mechanics](../../../Mechanics/Classical%20Mechanics.md)
- [Conservative Forces](../../../Mechanics/Conservative%20Forces.md)
- [Conservation Laws](../../../Mechanics/Conservation%20Laws.md)

<!-- semantic-edges
{"source":"Goldstein Section 1.1","relation":"INTRODUCES","target":"Particle Conservation Theorems","evidence_heading":"Big Ideas","evidence_summary":"Reviews momentum, angular momentum, and energy conservation for a single particle under distinct physical conditions.","confidence":0.9}
{"source":"Momentum Form of Newton's Second Law","relation":"GENERALIZES","target":"Acceleration Form of Newton's Second Law","evidence_heading":"Notes","evidence_summary":"Emphasizes force as the time derivative of momentum, with F = ma only following for constant mass.","confidence":0.89}
{"source":"Zero Torque","relation":"DETERMINES","target":"Angular Momentum Conservation","evidence_heading":"Angular Momentum","evidence_summary":"Shows that zero torque about a chosen origin implies conservation of angular momentum about that origin.","confidence":0.88}
{"source":"Time-Dependent Potential","relation":"CONTRASTS_WITH","target":"Energy Conservation","evidence_heading":"Work And Energy","evidence_summary":"Notes that a force may be derived from minus the gradient of a time-dependent potential while T plus V need not be conserved.","confidence":0.88}
-->
