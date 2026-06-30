# Calculus of Variations

Source: [The Lazy Universe](../../../References/Coopersmith2017TheLazyUniverse.pdf)

Book hub: [Coopersmith](../Coopersmith.md)

Book section: 3.7, printed pages 47-58.

Previous: [Configuration Space and Invariants](Configuration%20Space%20and%20Invariants.md)

Next: [Chapter 4 Overview](../Chapter%204/Chapter%20Overview.md)

## Reading Status

- Status: started
- Pages: 47-58
- Date started: 2026-06-28
- Date finished:

## Big Ideas

- Ordinary calculus finds stationary values of functions; variational calculus finds stationary functions or paths.
- Coopersmith distinguishes several infinitesimal ideas that are easy to blur: ordinary differentials, virtual variations, and finite increments taken toward a limit.
- Extremum language is too narrow for mechanics; the central requirement is stationarity.
- Stationary integral problems prepare the reader for the action principle.

## From Functions To Functionals

In ordinary calculus, one varies a number and asks when a function has no first-order change. In the calculus of variations, one varies a whole curve and asks when an integral depending on that curve has no first-order change.

A typical functional has the form:

$$
J[y]=\int_{x_1}^{x_2} f(y,y',x) dx
$$

The stationary curve satisfies the Euler-Lagrange equation:

$$
\frac{d}{dx}\left(\frac{\partial f}{\partial y'}\right)-\frac{\partial f}{\partial y}=0
$$

## Role In The Book

Coopersmith introduces this material before virtual work and D'Alembert's principle so that the reader can see the shared pattern: replace a finite physical displacement by a controlled virtual variation and require the first-order effect to vanish.

## Links To Concept Notes

- [Calculus of Variations](../../../Mathematics/Calculus%20of%20Variations.md)
- [Action Principle](../../../Mechanics/Action%20Principle.md)
- [Euler-Lagrange Equations](../../../Mechanics/Euler-Lagrange%20Equations.md)

<!-- semantic-edges
{"source":"Calculus of Variations","relation":"EXTENDS","target":"Ordinary Calculus","evidence_heading":"From Functions To Functionals","evidence_summary":"Ordinary calculus varies a number, while variational calculus varies a whole curve and studies the first-order change of an integral.","confidence":0.95}
{"source":"Calculus of Variations","relation":"DERIVES","target":"Euler-Lagrange Equations","evidence_heading":"From Functions To Functionals","evidence_summary":"The note gives a typical functional and states that the stationary curve satisfies the Euler-Lagrange equation.","confidence":0.95}
{"source":"Stationarity","relation":"CONTRASTS_WITH","target":"Extremum Language","evidence_heading":"Big Ideas","evidence_summary":"The note says extremum language is too narrow for mechanics and that stationarity is the central requirement.","confidence":0.9}
{"source":"Virtual Variations","relation":"ENABLES","target":"Action Principle","evidence_heading":"Role In The Book","evidence_summary":"Coopersmith uses controlled virtual variations and vanishing first-order effects to prepare for the action principle.","confidence":0.9}
-->
