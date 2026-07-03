# Lagrange's Equations of Motion

Source: [The Lazy Universe](../../../References/Coopersmith2017TheLazyUniverse.pdf)

Book hub: [Coopersmith](../Coopersmith.md)

Book section: 6.3, printed pages 112-115.

Previous: [Introduction and Hamilton's Principle](Introduction%20and%20Hamiltons%20Principle.md)

Next: [Physical Meaning and Assumptions](Physical%20Meaning%20and%20Assumptions.md)

## Reading Status

- Status: started
- Pages: 112-115
- Date started: 2026-07-03
- Date finished:

## Big Ideas

- The Lagrangian is introduced as the compact integrand $L=T-V$.
- Hamilton's principle has the same mathematical shape as the variational problems from Chapter 3.
- Applying the Euler-Lagrange equations to $L(q_i,\dot{q}_i,t)$ gives Lagrange's equations of motion.
- Generalized coordinates are what let the same form cover many different mechanical models.

## Hamilton's Principle In Lagrangian Form

Define:

$$
L=T-V
$$

Then Hamilton's principle becomes:

$$
\delta\int_{t_a}^{t_b}Ldt=0
$$

For generalized coordinates $q_i$, Coopersmith treats $L$ as a function of coordinates, generalized velocities, and possibly time:

$$
L=L(q_i,\dot{q}_i,t)
$$

## Lagrange's Equations

The calculus-of-variations result from the Euler-Lagrange equations gives, for each generalized coordinate:

$$
\frac{d}{dt}\frac{\partial L}{\partial \dot{q}_i}-\frac{\partial L}{\partial q_i}=0
$$

These are Lagrange's equations of motion. The power of the result is that the form of the equation stays the same even as the coordinates and the system-specific forms of $T$ and $V$ change.

## Why This Is More Than Notation

Coopersmith emphasizes that replacing a generic variational function by $L(q_i,\dot{q}_i,t)$ is not a trivial relabeling. It imports physical assumptions: coordinates describe a mechanical system, velocities enter the kinetic energy, potentials encode the applied interactions, and ideal constraints have already been eliminated or handled.

## Links To Concept Notes

- [Euler-Lagrange Equations](../../../Mechanics/Euler-Lagrange%20Equations.md)
- [Lagrangian Mechanics](../../../Mechanics/Lagrangian%20Mechanics.md)
- [Generalized Coordinates](../../../Mechanics/Generalized%20Coordinates.md)
- [Action Principle](../../../Mechanics/Action%20Principle.md)

<!-- semantic-edges
{"source":"Lagrange Equations of Motion","relation":"DERIVES_FROM","target":"Hamilton's Principle","evidence_heading":"Lagrange's Equations","evidence_summary":"The note says applying the Euler-Lagrange variational result to Hamilton's principle gives Lagrange's equations of motion.","confidence":0.95}
{"source":"Lagrangian Mechanics","relation":"REQUIRES","target":"Generalized Coordinates","evidence_heading":"Hamilton's Principle In Lagrangian Form","evidence_summary":"The note writes the Lagrangian as a function of generalized coordinates and generalized velocities.","confidence":0.9}
{"source":"Lagrange Equations of Motion","relation":"REFORMULATES","target":"Euler-Lagrange Equations","evidence_heading":"Lagrange's Equations","evidence_summary":"The same Euler-Lagrange form becomes the mechanical equations of motion when the variational function is the Lagrangian.","confidence":0.92}
-->
