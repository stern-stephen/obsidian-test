# Derivation of Lagrange's Equations from Hamilton's Principle

Source: [Classical Mechanics](../../../References/GoldsteinPooleSafkoClassicalMechanics.pdf)

Book hub: [Goldstein](../Goldstein.md)

Book section: 2.3, printed pages 44-45.

Previous: [Some Techniques of the Calculus of Variations](Some%20Techniques%20of%20the%20Calculus%20of%20Variations.md)

Next: [Extending Hamilton's Principle to Systems with Constraints](Extending%20Hamilton%27s%20Principle%20to%20Systems%20with%20Constraints.md)

## Reading Status

- Status: started
- Pages: 44-45
- Date started: 2026-06-19
- Date finished:

## Many-Variable Variations

For independent functions $y_i(x)$:

$$
J=\int f(y_1,\ldots,y_n,y_1',\ldots,y_n',x)dx
$$

vary each path independently while fixing every endpoint. Integration by parts yields:

$$
\delta J=\int\sum_i\left[\frac{\partial f}{\partial y_i}-\frac{d}{dx}\left(\frac{\partial f}{\partial y_i'}\right)\right]\delta y_i dx
$$

Because the $\delta y_i$ are independent and arbitrary in the interior, each coefficient vanishes.

## Application To The Action

Make the replacements:

$$
x\to t,\qquad y_i\to q_i,\qquad f\to L
$$

Then Hamilton's principle:

$$
\delta\int_{t_1}^{t_2}L(q_i,\dot q_i,t)dt=0
$$

implies one Euler-Lagrange equation per independent generalized coordinate:

$$
\frac{d}{dt}\left(\frac{\partial L}{\partial\dot q_i}\right)-\frac{\partial L}{\partial q_i}=0
$$

## Assumptions

- The endpoint configurations and endpoint times are fixed.
- The variations are sufficiently smooth.
- The generalized coordinates are independent, as they are after holonomic constraints have been absorbed into the coordinates.
- The system is described by the stated action, including any generalized potential in $L$.

## Main Point

The global condition $\delta I=0$ and the local Lagrange equations contain the same dynamics under these assumptions. The fundamental lemma is what converts an integral statement valid for every variation into a differential equation at every time.

## Links To Concept Notes

- [Euler-Lagrange Equations](../../../Mechanics/Euler-Lagrange%20Equations.md)
- [Action Principle](../../../Mechanics/Action%20Principle.md)
