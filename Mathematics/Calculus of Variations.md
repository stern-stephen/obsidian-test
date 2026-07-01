# Calculus of Variations

## Overview

The calculus of variations finds functions that make a functional stationary. In mechanics, its central application is deriving equations of motion from stationary action.

## Functional And Variation

A typical functional assigns a number to an entire function:

$$
J[y]=\int_{x_1}^{x_2}f(y,y',x)dx
$$

Compare nearby functions through:

$$
y(x,\alpha)=y(x)+\alpha\eta(x)
$$

For fixed endpoints:

$$
\eta(x_1)=\eta(x_2)=0
$$

The first variation is the coefficient of the first-order change:

$$
\delta J=\left.\frac{dJ}{d\alpha}\right|_{\alpha=0}\delta\alpha
$$

## Euler-Lagrange Equation

After integration by parts:

$$
\delta J=\int_{x_1}^{x_2}\left[\frac{\partial f}{\partial y}-\frac{d}{dx}\left(\frac{\partial f}{\partial y'}\right)\right]\delta y dx
$$

The fundamental lemma says that if this integral vanishes for every admissible interior variation, then:

$$
\frac{d}{dx}\left(\frac{\partial f}{\partial y'}\right)-\frac{\partial f}{\partial y}=0
$$

For several independent functions $y_i$, there is one equation for each $i$.

## Intuition

Ordinary calculus varies a number and sets a derivative to zero. Variational calculus varies a whole function and sets the first-order change of a functional to zero. The arbitrariness of the local variation turns the global stationary condition into a differential equation.

## Important Limits

- Vanishing first variation establishes stationarity, not necessarily a minimum.
- Fixed endpoints are an assumption; free boundaries produce additional boundary conditions.
- Nonsmooth extrema may escape a derivation that assumes smooth trial functions.
- Constraints may make variations dependent and require multipliers or reduced coordinates.

## Examples

- Straight lines are geodesics of the Euclidean plane.
- Catenaries generate smooth stationary surfaces of revolution.
- Cycloids solve the brachistochrone problem.
- The Euler-Lagrange equations of mechanics follow by setting $f=L$ and $x=t$.

## Related Concepts

- [Action Principle](../Mechanics/Action%20Principle.md)
- [Euler-Lagrange Equations](../Mechanics/Euler-Lagrange%20Equations.md)
- [Goldstein Section 2.2](../Book%20Notes/Goldstein/Chapter%202/Some%20Techniques%20of%20the%20Calculus%20of%20Variations.md)
- [Coopersmith Section 3.7](../Book%20Notes/Coopersmith/Chapter%203/Calculus%20of%20Variations.md)

<!-- semantic-edges
{"source":"Calculus of Variations","relation":"EXTENDS","target":"Ordinary Calculus","evidence_heading":"Intuition","evidence_summary":"The note contrasts ordinary calculus, which varies a number, with variational calculus, which varies a whole function and sets the first-order change of a functional to zero.","confidence":0.95}
{"source":"Calculus of Variations","relation":"DETERMINES","target":"Euler-Lagrange Equations","evidence_heading":"Euler-Lagrange Equation","evidence_summary":"After integration by parts and the fundamental lemma, the note obtains the Euler-Lagrange equation as the condition for a stationary functional.","confidence":0.95}
{"source":"Admissible Variations","relation":"ENABLES","target":"Euler-Lagrange Equation","evidence_heading":"Euler-Lagrange Equation","evidence_summary":"The note uses arbitrary admissible interior variations with fixed endpoints so the fundamental lemma can turn the global stationary condition into a differential equation.","confidence":0.9}
{"source":"Calculus of Variations","relation":"ENABLES","target":"Action Principle","evidence_heading":"Overview","evidence_summary":"The note identifies deriving equations of motion from stationary action as the central mechanics application of calculus of variations.","confidence":0.95}
-->
