# Extending Hamilton's Principle to Systems with Constraints

Source: [Classical Mechanics](../../../References/GoldsteinPooleSafkoClassicalMechanics.pdf)

Book hub: [Goldstein](../Goldstein.md)

Book section: 2.4, printed pages 45-51.

Previous: [Derivation of Lagrange's Equations from Hamilton's Principle](Derivation%20of%20Lagrange%27s%20Equations%20from%20Hamilton%27s%20Principle.md)

Next: [Advantages of a Variational Principle Formulation](Advantages%20of%20a%20Variational%20Principle%20Formulation.md)

## Reading Status

- Status: started
- Pages: 45-51
- Date started: 2026-06-19
- Date finished:

## Why Multipliers Are Needed

If dependent coordinates are retained, their variations are linked by the constraints. Lagrange multipliers let the coordinates be varied independently while the constraints are enforced as additional equations.

For holonomic constraints $f_\alpha(q,t)=0$, vary the augmented action:

$$
I=\int_{t_1}^{t_2}\left(L+\sum_{\alpha=1}^m\lambda_\alpha f_\alpha\right)dt
$$

Variation with respect to $\lambda_\alpha$ returns the constraints. Variation with respect to $q_k$ gives:

$$
\frac{d}{dt}\left(\frac{\partial L}{\partial\dot q_k}\right)-\frac{\partial L}{\partial q_k}=-\sum_{\alpha=1}^m\lambda_\alpha\frac{\partial f_\alpha}{\partial q_k}
$$

The right side is the generalized constraint force, up to the sign convention used in the augmented action.

## Why Keep Redundant Coordinates

- Eliminating the constraints may be algebraically awkward.
- The multipliers can supply constraint forces that reduced-coordinate equations hide.

For a particle sliding on a smooth sphere, the multiplier gives the normal force and shows when contact is lost. For a hoop rolling down an incline, the multiplier gives the static-friction force while the coupled equations give $\ddot x=g\sin\phi/2$.

## Velocity Constraints

Goldstein also considers constraints of the form:

$$
f_\alpha(q,\dot q,t)=0
$$

especially linear differential relations:

$$
f_\alpha=\sum_k a_{\alpha k}(q,t)\dot q_k+a_{\alpha0}(q,t)=0
$$

An augmented variational treatment can be used for the semiholonomic class discussed in the text, with multipliers $\mu_\alpha(t)$. The resulting generalized constraint forces are:

$$
Q_k=-\sum_\alpha\mu_\alpha\frac{\partial f_\alpha}{\partial\dot q_k}
$$

This is not a variational formulation for every nonholonomic constraint. Inequality constraints, for example, are outside this form.

## Workless Constraint Requirement

The extension still assumes that constraint forces do no virtual work in the allowed variations. Rolling without slipping often satisfies this ideal-constraint condition even though static friction is nonzero.

## Common Confusions

- A multiplier is not automatically positive; its physical direction depends on the chosen constraint function and sign convention.
- Retaining constraints explicitly increases both the unknowns and the equations.
- A velocity relation may be integrable and therefore holonomic despite its appearance.
- The textbook's multiplier prescription covers a restricted class, not arbitrary nonholonomic mechanics.

## Links To Concept Notes

- [Constraints](../../../Mechanics/Constraints.md)
- [Generalized Coordinates](../../../Mechanics/Generalized%20Coordinates.md)
- [Virtual Work and D'Alembert's Principle](../../../Mechanics/Virtual%20Work%20and%20DAlemberts%20Principle.md)
