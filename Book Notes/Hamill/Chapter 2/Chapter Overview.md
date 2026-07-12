# Chapter Overview

Source: [Hamill](../../../References/Hamill.pdf)

Book hub: [Hamill](../Hamill.md)

Book chapter: 2, printed pages 44-69.

PDF reference: [Hamill PDF](../../../References/Hamill.pdf). In this file, Hamill printed page 44 is PDF page 56.

Previous: [Chapter 1 - Fundamental Concepts](../Chapter%201/Chapter%20Overview.md)

Next: [Introduction and Euler-Lagrange Equation](Introduction%20and%20Euler-Lagrange%20Equation.md)

## Reading Status

- Status: started
- Pages: 44-69
- Date started: 2026-07-12
- Date finished:

## Big Ideas

- Variational calculus asks which whole function or path makes an integral stationary.
- Hamill builds the Euler-Lagrange equation from fixed-endpoint variations and integration by parts.
- The variation symbol $\delta$ compares neighboring functions at the same independent-variable value, while $d$ moves along one function.
- Two shortcut forms are useful when the integrand omits either the dependent variable or the independent variable.
- The brachistochrone problem shows how the no-explicit-$x$ form can reduce a variational problem to a first-order equation.
- Several dependent variables produce one Euler-Lagrange equation for each independent variation.
- Constraints can be handled either by reducing variables or by augmenting the integrand with Lagrange multipliers.
- Hamill distinguishes holonomic, differential non-holonomic, and isoperimetric constraints as different kinds of auxiliary conditions.

## Section Notes

- [Introduction and Euler-Lagrange Equation](Introduction%20and%20Euler-Lagrange%20Equation.md)
- [Variations and Alternate Euler-Lagrange Forms](Variations%20and%20Alternate%20Euler-Lagrange%20Forms.md)
- [Several Dependent Variables](Several%20Dependent%20Variables.md)
- [Constrained Variational Problems](Constrained%20Variational%20Problems.md)
- [Problems](Problems.md)

## Logical Progression

1. Start from ordinary stationary-point tests and reinterpret "no first-order change" for an integral.
2. Write nearby fixed-endpoint curves as a one-parameter family.
3. Differentiate the functional with respect to the path-family parameter.
4. Integrate by parts so the variation, not its derivative, multiplies the whole coefficient.
5. Use the arbitrariness of the interior variation to obtain the Euler-Lagrange equation.
6. Record shortcut first integrals for special forms of the integrand.
7. Generalize from one unknown function to several.
8. Add auxiliary conditions with Lagrange multipliers when the variations are not independent.

## Links To Concept Notes

- [Calculus of Variations](../../../Mathematics/Calculus%20of%20Variations.md)
- [Euler-Lagrange Equations](../../../Mechanics/Euler-Lagrange%20Equations.md)
- [Action Principle](../../../Mechanics/Action%20Principle.md)
- [Hamilton's Principle](../../../Mechanics/Hamiltons%20Principle.md)
- [Constraints](../../../Mechanics/Constraints.md)
- [Lagrangian Mechanics](../../../Mechanics/Lagrangian%20Mechanics.md)

## Questions

- Which examples in the problems are true minima, and which are only stationary curves unless a second-variation argument is added?
- How do Hamill's variational constraints compare with the constraint forces found later through Lagrange multipliers in mechanics?
- Which shortcut equation is most useful for each classic problem: shortest path, brachistochrone, geodesic, and isoperimetric maximum-area curve?
- How exactly does the replacement $x\mapsto t$ and $\Phi\mapsto L$ turn this chapter into Hamilton's principle?

<!-- semantic-edges
{"source":"Hamill Chapter 2","relation":"INTRODUCES","target":"Calculus of Variations","evidence_heading":"Big Ideas","evidence_summary":"The overview identifies Chapter 2 as Hamill's development of stationary functionals, fixed-endpoint variations, and constrained variational problems.","confidence":0.94}
{"source":"Hamill Chapter 2","relation":"MOTIVATES","target":"Euler-Lagrange Equations","evidence_heading":"Logical Progression","evidence_summary":"The chapter progression moves from fixed-endpoint path variations through integration by parts to the Euler-Lagrange equation.","confidence":0.92}
{"source":"Hamill Chapter 2","relation":"MOTIVATES","target":"Hamilton's Principle","evidence_heading":"Questions","evidence_summary":"The overview frames the chapter as the mathematical setup for replacing the independent variable by time and the integrand by the Lagrangian.","confidence":0.88}
-->
