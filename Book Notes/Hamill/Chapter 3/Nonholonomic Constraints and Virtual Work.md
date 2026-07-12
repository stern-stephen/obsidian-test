# Nonholonomic Constraints and Virtual Work

Source: [Hamill](../../../References/Hamill.pdf)

Book hub: [Hamill](../Hamill.md)

Chapter overview: [Chapter Overview](Chapter%20Overview.md)

Book sections: 3.6-3.7.1, printed pages 81-86.

Previous: [Constraints and Lagrange Multipliers](Constraints%20and%20Lagrange%20Multipliers.md)

Next: [Invariance and Problems](Invariance%20and%20Problems.md)

## Reading Status

- Status: started
- Pages: 81-86
- Date started: 2026-07-12
- Date finished:

## Purpose

Hamill extends the multiplier discussion to certain non-holonomic constraints and then returns to virtual work. The common theme is that allowed virtual displacements determine whether constraint forces appear or disappear from the equations.

## 3.6 Non-Holonomic Constraints

Some non-holonomic constraints can be written as differential relations:

$$
A_1dq_1+A_2dq_2+\cdots+A_ndq_n=0
$$

If the same relation holds for virtual displacements:

$$
A_1\delta q_1+A_2\delta q_2+\cdots+A_n\delta q_n=0
$$

then the multiplier method has the same algebraic shape as the holonomic case.

For one constraint:

$$
\frac{d}{dt}\left(\frac{\partial L}{\partial \dot q_i}\right)-\frac{\partial L}{\partial q_i}=\lambda A_i
$$

For $m$ constraints:

$$
\frac{d}{dt}\left(\frac{\partial L}{\partial \dot q_i}\right)-\frac{\partial L}{\partial q_i}=\sum_k\lambda_kA_{ki}
$$

The important difference is that the coefficients $A_i$ are not necessarily partial derivatives of a constraint function.

## Rheonomous Differential Constraints

Hamill also notes a time-dependent form:

$$
\sum_i A_{ki}dq_i+B_kdt=0
$$

For virtual displacements, time is frozen:

$$
\delta t=0
$$

so the $B_k$ terms do not appear in the virtual-displacement relation. They do, however, appear in the velocity constraint:

$$
\sum_i A_{ki}\dot q_i+B_k=0
$$

This is a good reminder that virtual displacement equations and actual velocity equations are related but not identical.

## 3.7 Virtual Work

The principle of virtual work says that a system is in equilibrium if and only if the total virtual work of the impressed forces is zero:

$$
\delta W=\sum_jQ_j\delta q_j=0
$$

The virtual displacements must satisfy the constraints.

Impressed forces are the applied forces, excluding reaction or constraint forces. Analytical mechanics avoids writing unknown reaction forces by restricting the virtual displacements to those allowed by the constraints.

## Newtonian Equilibrium Versus Virtual Work

Newtonian equilibrium uses the vector condition:

$$
\sum\mathbf{F}=0
$$

This includes reaction forces. The virtual-work approach instead uses:

$$
\sum_i\mathbf{F}_i\cdot\delta\mathbf{r}_i=0
$$

for allowed virtual displacements and impressed forces.

For a particle constrained to a table, allowed virtual displacements are tangent to the table. The normal reaction force does no virtual work because it is perpendicular to every allowed displacement.

## Virtual Work Postulate

Hamill states the virtual-work principle as a postulate of analytical mechanics:

$$
\delta W=0
$$

for equilibrium.

Equivalently, the virtual work of reaction forces is zero for any virtual displacement satisfying the constraints. This is why ideal constraint forces can be omitted when using allowed virtual displacements.

## Potential Energy And Equilibrium

If impressed forces come from a potential:

$$
F_i=-\frac{\partial V}{\partial q_i}
$$

then:

$$
\delta W=-\delta V
$$

Equilibrium therefore corresponds to:

$$
\delta V=0
$$

subject to the constraints.

## Physical Meaning Of Multipliers

For a holonomic constraint:

$$
f(q_1,\ldots,q_n)=0
$$

the multiplier method modifies the potential by a constraint term:

$$
V\rightarrow V+\lambda f
$$

If arbitrary variations are allowed, not just constraint-compatible ones, reaction forces appear. Hamill interprets the multiplier term as a potential associated with the constraint force. For Cartesian coordinates:

$$
F_i=-\lambda\frac{\partial f}{\partial x_i}
$$

because $f=0$ on the constraint surface.

For holonomic constraints, constraint forces can be derived from this scalar multiplier expression. For genuinely non-holonomic constraints, the forces generally cannot be derived from such a scalar potential.

## Catenary Example

Hamill's catenary example minimizes potential energy subject to fixed length. The length constraint is:

$$
l=\int_{x_1}^{x_2}\sqrt{1+y'^2}dx
$$

The potential energy, up to constants, is:

$$
V=\int_{x_1}^{x_2}y\sqrt{1+y'^2}dx
$$

The multiplier method produces the stationary integral:

$$
\delta\int_{x_1}^{x_2}(y+\lambda)\sqrt{1+y'^2}dx=0
$$

Because the integrand has no explicit $x$ dependence, the Chapter 2 shortcut form can be used to show the curve is a catenary.

## Links To Concept Notes

- [Constraints](../../../Mechanics/Constraints.md)
- [Virtual Work and D'Alembert's Principle](../../../Mechanics/Virtual%20Work%20and%20DAlemberts%20Principle.md)
- [Calculus of Variations](../../../Mathematics/Calculus%20of%20Variations.md)

<!-- semantic-edges
{"source":"Nonholonomic Constraints","relation":"CONTRASTS_WITH","target":"Holonomic Constraints","evidence_heading":"3.6 Non-Holonomic Constraints","evidence_summary":"The note distinguishes differential constraints whose coefficients need not be partial derivatives of a scalar constraint function from holonomic constraints.","confidence":0.9}
{"source":"Virtual Work","relation":"ELIMINATES","target":"Ideal Constraint Forces","evidence_heading":"Virtual Work Postulate","evidence_summary":"The note states that reaction forces do no virtual work for allowed virtual displacements, allowing them to be omitted from the virtual-work condition.","confidence":0.92}
{"source":"Lagrange Multipliers","relation":"REPRESENTS","target":"Reaction Forces","evidence_heading":"Physical Meaning Of Multipliers","evidence_summary":"The note interprets multiplier terms for holonomic constraints as producing the reaction forces associated with maintaining the constraint.","confidence":0.9}
-->
