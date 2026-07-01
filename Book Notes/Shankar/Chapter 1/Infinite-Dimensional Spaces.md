# Infinite-Dimensional Spaces

Source: [Principles of Quantum Mechanics](../../../References/Principals%20of%20quantum%20mechanics%20Shankar%20.pdf)

Book hub: [Shankar](../Shankar.md)

Book section: 1.10.

Focused walkthrough: [Operators in Infinite Dimensions - Walkthrough](Operators%20in%20Infinite%20Dimensions%20-%20Walkthrough.md)

Previous: [Functions of Operators](Functions%20of%20Operators.md)

## Reading Status

- Status: started
- Pages:
- Date started: 2026-05-17
- Date finished:

## Big Ideas

- Section 1.10 generalizes finite-dimensional vector-space ideas to spaces whose vectors are functions.
- A wavefunction can be understood as the coordinate representation of an abstract ket in a continuous basis.
- Sums over basis labels become integrals when the labels are continuous.
- The Dirac delta function plays the role of the Kronecker delta when basis labels become continuous.

## Notes

Shankar's main move is to keep the finite-dimensional vector-space rules while allowing basis labels to become infinite or continuous. A wavefunction is therefore not a replacement for the ket; it is the ket's component function in the position basis.

## Kronecker Delta To Dirac Delta

Discrete sums and Kronecker deltas become integrals and Dirac deltas. This is the continuous-basis form of orthonormality and completeness, not a new vector-space theory. [Dirac Delta Function](../../../Linear%20Algebra/Dirac%20Delta%20Function.md) owns the distributional definitions, derivative identities, Gaussian limits, and Fourier representations.

## Operators In Infinite Dimensions

An operator kernel is the continuous-basis analogue of a matrix. Shankar uses identity, multiplication, derivative, and momentum operators to show how a matrix sum becomes an integral action on a wavefunction.

The canonical finite-to-continuous dictionary and kernel formulas live in [Infinite-Dimensional Vector Spaces](../../../Linear%20Algebra/Infinite-Dimensional%20Vector%20Spaces.md). The more detailed reading aid remains in [Operators in Infinite Dimensions - Walkthrough](Operators%20in%20Infinite%20Dimensions%20-%20Walkthrough.md), including the sign distinction between differentiating the output variable and differentiating the integration variable.

## Common Confusions

- A wavefunction $\psi(x)$ is not "more real" than a ket. It is the ket written in the position basis.
- The ket $|x\rangle$ is not a normalizable physical state in the usual sense. It is an idealized basis object used to represent states.
- The Dirac delta is not a spike-shaped ordinary function. In this setting, it is best treated by what it does under an integral.
- The derivative $\delta'(x-a)$ has a minus sign in its integral rule: $\int dx \delta'(x-a)f(x)=-f'(a)$.
- In an operator kernel such as $\frac{\partial}{\partial x}\delta(x-x')$, the derivative is with respect to the output variable $x$, so it gives $+\psi'(x)$ after integration over $x'$.
- An operator kernel $A(x,x')$ is the infinite-dimensional version of a matrix $A_{ij}$.
- Gaussian and Fourier formulas for $\delta(x)$ are distributional limits, so they should be checked by placing them inside an integral.
- Infinite-dimensional spaces follow the same vector-space rules, but questions about convergence, domains, and normalization become more delicate.

## Study Questions

- What changes when the basis label $i$ becomes a continuous label $x$?
- Why does $\int dx |x\rangle\langle x|$ behave like the identity operator?
- Why is $\psi(x)=\langle x|\psi\rangle$ a coordinate representation rather than a different physical object?
- Why does $\int dx \delta'(x-a)f(x)$ equal $-f'(a)$ instead of $f'(a)$?
- How do the Gaussian and Fourier representations of $\delta(x)$ express the same distributional idea?
- Why is $A(x,x')=\langle x|A|x'\rangle$ the continuous analogue of a matrix element $A_{ij}$?
- How does $\int dx' A(x,x')\psi(x')$ generalize ordinary matrix multiplication?

## Exercise Answers

These are answer summaries for Shankar Chapter 1 exercises in this section. I am not reproducing the full problem statements here.

### Exercise 1.10.1

Use the defining property of the delta function:

$$
\int dx \delta(x)f(x)=f(0)
$$

For $\delta(ax)$, change variables:

$$
u=ax,\qquad du=a dx
$$

The orientation of the integral depends on the sign of $a$, so the scale factor is $|a|$, not $a$. Thus:

$$
\int dx \delta(ax)f(x)=\frac{1}{|a|}\int du \delta(u)f(u/a)
$$

Therefore:

$$
\int dx \delta(ax)f(x)=\frac{1}{|a|}f(0)
$$

So:

$$
\delta(ax)=\frac{1}{|a|}\delta(x)
$$

### Exercise 1.10.2

Suppose $f(x)$ has simple zeros $x_i$, meaning:

$$
f(x_i)=0,\qquad f'(x_i)\ne 0
$$

Near each zero:

$$
f(x)\approx f'(x_i)(x-x_i)
$$

Using the result from Exercise 1.10.1:

$$
\delta(f'(x_i)(x-x_i))=\frac{1}{|f'(x_i)|}\delta(x-x_i)
$$

Summing over all zeros gives:

$$
\delta(f(x))=\sum_i \frac{\delta(x-x_i)}{|f'(x_i)|}
$$

This identity says the delta function localizes at every zero of $f$, with a weight determined by how steeply $f$ crosses zero there.

### Exercise 1.10.3

Let $\theta(x-x')$ be the step function that jumps from $0$ to $1$ at $x=x'$.

For $x\ne x'$, the derivative is zero:

$$
\frac{d}{dx}\theta(x-x')=0
$$

But at $x=x'$, the function has a unit jump. To test its derivative, integrate around the jump:

$$
\int_{x'-\epsilon}^{x'+\epsilon} dx \frac{d}{dx}\theta(x-x')=\theta(\epsilon)-\theta(-\epsilon)=1
$$

The distribution with zero value away from $x=x'$ and total integral $1$ at $x=x'$ is the delta function. Therefore:

$$
\frac{d}{dx}\theta(x-x')=\delta(x-x')
$$

### Exercise 1.10.4

This exercise uses the normal modes of a string fixed at $x=0$ and $x=L$.

For zero initial velocity, the displacement has the form:

$$
\psi(x,t)=\sum_{m=1}^{\infty} b_m \sin\left(\frac{m\pi x}{L}\right)\cos(\omega_m t)
$$

The coefficients are determined by the initial displacement:

$$
b_m=\frac{2}{L}\int_0^L dx \psi(x,0)\sin\left(\frac{m\pi x}{L}\right)
$$

For Shankar's triangular initial displacement, split the integral at $L/2$:

$$
b_m=\frac{2}{L}\left[\int_0^{L/2} dx \frac{2hx}{L}\sin\left(\frac{m\pi x}{L}\right)+\int_{L/2}^{L} dx \frac{2h(L-x)}{L}\sin\left(\frac{m\pi x}{L}\right)\right]
$$

In the second integral, substitute $u=L-x$. Since:

$$
\sin\left(\frac{m\pi(L-u)}{L}\right)=\sin(m\pi-\frac{m\pi u}{L})=(-1)^{m+1}\sin\left(\frac{m\pi u}{L}\right)
$$

the coefficient becomes:

$$
b_m=\frac{2}{L}\left[1+(-1)^{m+1}\right]\int_0^{L/2} dx \frac{2hx}{L}\sin\left(\frac{m\pi x}{L}\right)
$$

Use integration by parts:

$$
\int x\sin(ax) dx=-\frac{x\cos(ax)}{a}+\frac{\sin(ax)}{a^2}
$$

with:

$$
a=\frac{m\pi}{L}
$$

Evaluating from $0$ to $L/2$ and simplifying gives:

$$
b_m=\frac{8h}{\pi^2m^2}\sin\left(\frac{m\pi}{2}\right)
$$

Therefore:

$$
\psi(x,t)=\sum_{m=1}^{\infty}\frac{8h}{\pi^2m^2}\sin\left(\frac{m\pi}{2}\right)\sin\left(\frac{m\pi x}{L}\right)\cos(\omega_m t)
$$

Only odd $m$ contribute, because the factor:

$$
1+(-1)^{m+1}
$$

vanishes for even $m$. Equivalently, the final coefficient contains $\sin(m\pi/2)$, which is zero for even $m$.

This matches the expected physical picture: the triangular shape is symmetric about the midpoint, so only the symmetric sine modes appear.

The related eigenfunctions of the string operator are:

$$
\langle x|m\rangle=\sqrt{\frac{2}{L}}\sin\left(\frac{m\pi x}{L}\right)
$$

## Links To Concept Notes

- [Infinite-Dimensional Vector Spaces](../../../Linear%20Algebra/Infinite-Dimensional%20Vector%20Spaces.md)
- [Dirac Delta Function](../../../Linear%20Algebra/Dirac%20Delta%20Function.md)
- [Bra-Ket Notation](../../../Linear%20Algebra/Bra-Ket%20Notation.md)
- [Linear Operators](../../../Linear%20Algebra/Linear%20Operators.md)
- [Projection Operators](../../../Linear%20Algebra/Projection%20Matrices.md)
- [Functions of Operators](Functions%20of%20Operators.md)
- [Operators in Infinite Dimensions - Walkthrough](Operators%20in%20Infinite%20Dimensions%20-%20Walkthrough.md)

<!-- semantic-edges
{"source":"Shankar Section 1.10","relation":"INTRODUCES","target":"Infinite-Dimensional Vector Spaces","evidence_heading":"Big Ideas","evidence_summary":"Generalizes finite-dimensional vector-space ideas to function spaces and continuous bases.","confidence":0.94}
{"source":"Wavefunctions","relation":"REPRESENTS","target":"Quantum State Vector","evidence_heading":"Notes","evidence_summary":"Treats a wavefunction as the coordinate representation of an abstract ket in the position basis.","confidence":0.92}
{"source":"Shankar Section 1.10","relation":"MOTIVATES","target":"Dirac Delta Function","evidence_heading":"Kronecker Delta To Dirac Delta","evidence_summary":"Uses the finite-to-continuous basis transition to motivate the Dirac delta in orthonormality and completeness formulas.","confidence":0.91}
{"source":"Shankar Section 1.10","relation":"INTRODUCES","target":"Operator Kernels","evidence_heading":"Operators In Infinite Dimensions","evidence_summary":"Uses identity, multiplication, derivative, and momentum operators to introduce kernels as continuous-basis operator representations.","confidence":0.91}
{"source":"Kernel Action","relation":"GENERALIZES","target":"Matrix Multiplication","evidence_heading":"Study Questions","evidence_summary":"Shows that integral kernel action generalizes ordinary matrix multiplication when basis labels become continuous.","confidence":0.9}
-->
