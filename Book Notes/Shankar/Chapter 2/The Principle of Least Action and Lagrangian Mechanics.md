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

The Lagrangian is usually written as:

$$
L(q,\dot{q},t) = T - V
$$

The action of a path is:

$$
S[q] = \int_{t_1}^{t_2} L(q,\dot{q},t) dt
$$

Hamilton's principle says that the physical path has stationary action:

$$
\delta S = 0
$$

For coordinates $q_i$, this gives the Euler-Lagrange equations:

$$
\frac{d}{dt}\frac{\partial L}{\partial \dot{q}_i} - \frac{\partial L}{\partial q_i} = 0
$$

## Generalized Momentum

The momentum conjugate to $q_i$ is:

$$
p_i = \frac{\partial L}{\partial \dot{q}_i}
$$

This equals ordinary momentum in simple Cartesian problems, but it can differ in generalized coordinates or in electromagnetic fields.

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
