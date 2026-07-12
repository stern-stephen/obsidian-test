# Constrained Variational Problems

Source: [Hamill](../../../References/Hamill.pdf)

Book hub: [Hamill](../Hamill.md)

Chapter overview: [Chapter Overview](Chapter%20Overview.md)

Book section: 2.4, printed pages 60-66.

Previous: [Several Dependent Variables](Several%20Dependent%20Variables.md)

Next: [Problems](Problems.md)

## Reading Status

- Status: started
- Pages: 60-66
- Date started: 2026-07-12
- Date finished:

## Purpose

Hamill next considers variational problems with auxiliary conditions. A constraint prevents all variations from being independent, so the simple "set each coefficient to zero" argument cannot be used without modification.

There are two broad strategies:

- use the constraints to eliminate dependent variables;
- keep the variables and add Lagrange multipliers.

The multiplier method is usually more systematic, especially when solving the constraint explicitly would be messy.

## Holonomic Constraints

For $n$ dependent variables and $m$ holonomic constraints:

$$
f_1(y_1,\ldots,y_n,x)=0
$$

$$
\cdots
$$

$$
f_m(y_1,\ldots,y_n,x)=0
$$

each constraint reduces the number of independent degrees of freedom by one.

If there are no multipliers, one can in principle solve the constraints and reduce the problem to $n-m$ independent variables. Hamill then turns to the multiplier method, which keeps all $n$ variables.

## Variation Of A Constraint

For one constraint:

$$
f(y_1,\ldots,y_n,x)=0
$$

the variation satisfies:

$$
\delta f=\sum_i\frac{\partial f}{\partial y_i}\delta y_i=0
$$

Multiplying by an undetermined multiplier $\lambda$ gives:

$$
\lambda\delta f=0
$$

Because this is zero, it can be added to the stationarity condition without changing the constrained problem.

## Multiplier Reformulation

The constrained stationarity condition:

$$
\delta\Phi=0
$$

subject to:

$$
f=0
$$

is replaced by:

$$
\delta(\Phi+\lambda f)=0
$$

together with the original constraint.

For several constraints:

$$
\delta(\Phi+\lambda_1f_1+\cdots+\lambda_mf_m)=0
$$

The multipliers are not arbitrary after the equations are solved. They are unknowns determined along with the coordinates.

## What The Multiplier Does

The multiplier method works by canceling the dependence among variations. In the one-constraint case, the variations are related by $\delta f=0$, so not all $\delta y_i$ are independent. Introducing $\lambda$ lets one choose it so that the coefficient of one dependent variation is handled, leaving equations that can be treated as if the remaining variations were independent.

In mechanics, this same idea later lets constraint forces appear through multiplier terms while avoiding a premature coordinate elimination.

## Simple Constrained Extremum Example

Hamill illustrates the method with the plane:

$$
\Phi(x,y)=x+y
$$

subject to the circle:

$$
(x-2)^2+(y-2)^2=1
$$

The augmented function is:

$$
\Phi+\lambda f=x+y+\lambda[(x-2)^2+(y-2)^2-1]
$$

The stationary equations are:

$$
1+2\lambda(x-2)=0
$$

$$
1+2\lambda(y-2)=0
$$

$$
(x-2)^2+(y-2)^2=1
$$

The first two equations imply $x=y$. Substitution into the circle gives:

$$
2(x-2)^2=1
$$

Thus the extrema occur along the diagonal through the circle's center:

$$
x=y=2\pm\frac{1}{\sqrt{2}}
$$

The example is elementary, but it shows the structure used in more complicated variational problems.

## Differential Constraints

Hamill then considers constraints that are expressed as relations among differentials rather than as coordinate-only equations.

A typical rolling-without-slipping relation has the form:

$$
ds=rd\theta
$$

If such a differential relation can be integrated into a coordinate relation, then it is effectively holonomic. If it cannot be integrated, it is genuinely non-holonomic.

For some non-holonomic constraints, Hamill writes the virtual-displacement relation:

$$
A_1\delta y_1+A_2\delta y_2+\cdots+A_n\delta y_n=0
$$

The multiplier method can then be applied by adding:

$$
\lambda(A_1\delta y_1+\cdots+A_n\delta y_n)
$$

to the variation. The important caution is that this is not the same as adding $\lambda f$ for an ordinary holonomic constraint, because there may be no scalar function $f$ whose variation gives those coefficients.

## Isoperimetric Constraints

An isoperimetric constraint fixes the value of an integral:

$$
\int_{x_1}^{x_2}f(x,y,y')dx=C
$$

If the functional to be extremized is:

$$
I[y]=\int_{x_1}^{x_2}\Phi(x,y,y')dx
$$

then the multiplier method says to extremize:

$$
\int_{x_1}^{x_2}(\Phi+\lambda f)dx
$$

The same endpoints appear in both integrals. The multiplier $\lambda$ is constant for this fixed-integral condition.

## Maximum Area For Fixed Perimeter

Hamill's isoperimetric example is the classic problem: find the curve of fixed length that encloses the greatest area.

Parametrize the curve by $t$:

$$
x=x(t)
$$

$$
y=y(t)
$$

The enclosed area can be written:

$$
A=\frac{1}{2}\oint (x\dot y-y\dot x)dt
$$

The fixed-length constraint is:

$$
\oint\sqrt{\dot x^2+\dot y^2}dt=L
$$

The augmented integrand is:

$$
\frac{1}{2}(x\dot y-y\dot x)+\lambda\sqrt{\dot x^2+\dot y^2}
$$

Applying the Euler-Lagrange equations and integrating leads to:

$$
(x-C_1)^2+(y-C_2)^2=\lambda^2
$$

So the extremal curve is a circle. This matches the geometric fact that a circle encloses the maximum area for a given perimeter.

## What To Remember

- Holonomic constraints can sometimes be solved directly, but multipliers often keep the calculation cleaner.
- Multiplier terms convert constrained stationarity into unconstrained stationarity plus constraint equations.
- Differential constraints need special care because they may not come from a scalar constraint function.
- Isoperimetric constraints fix an integral and are handled by augmenting the integrand.
- The circle as maximum-area curve is the standard fixed-perimeter isoperimetric result.

## Links To Concept Notes

- [Constraints](../../../Mechanics/Constraints.md)
- [Calculus of Variations](../../../Mathematics/Calculus%20of%20Variations.md)
- [Euler-Lagrange Equations](../../../Mechanics/Euler-Lagrange%20Equations.md)
- [Lagrangian Mechanics](../../../Mechanics/Lagrangian%20Mechanics.md)

<!-- semantic-edges
{"source":"Lagrange Multipliers","relation":"ENABLES","target":"Constrained Variational Problems","evidence_heading":"Multiplier Reformulation","evidence_summary":"The note explains how adding multiplier-weighted constraint terms converts constrained stationarity into an augmented stationarity condition plus the original constraints.","confidence":0.92}
{"source":"Differential Constraints","relation":"CONTRASTS_WITH","target":"Holonomic Constraints","evidence_heading":"Differential Constraints","evidence_summary":"The note distinguishes integrable differential constraints from genuinely non-holonomic constraints that may not arise from a scalar constraint function.","confidence":0.88}
{"source":"Isoperimetric Constraints","relation":"EXAMPLE_OF","target":"Constrained Variational Problems","evidence_heading":"Isoperimetric Constraints","evidence_summary":"The note describes fixed-integral auxiliary conditions and handles them by augmenting the variational integrand with a multiplier term.","confidence":0.9}
-->
