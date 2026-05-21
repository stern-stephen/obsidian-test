# Infinite-Dimensional Spaces

Source: [Principles of Quantum Mechanics](../../../References/Principals%20of%20quantum%20mechanics%20Shankar%20.pdf)

Book hub: [Shankar](../Shankar.md)

Book section: 1.10.

Focused walkthrough: [Operators in Infinite Dimensions - Walkthrough](Operators%20in%20Infinite%20Dimensions%20-%20Walkthrough.md)

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

The finite-dimensional picture says:

$$
|v\rangle = \sum_i v_i |i\rangle
$$

where the numbers $v_i$ are the components of the vector in the chosen basis.

In an infinite-dimensional function space, the vector can have infinitely many components. For a discrete infinite basis:

$$
|f\rangle = \sum_{n=1}^{\infty} f_n |n\rangle
$$

For a continuous basis, the sum becomes an integral:

$$
|\psi\rangle = \int dx \psi(x)|x\rangle
$$

Here $\psi(x)$ is not the abstract vector itself. It is the coordinate representation of the abstract ket $|\psi\rangle$ in the $x$ basis:

$$
\psi(x) = \langle x|\psi\rangle
$$

This is one of the most important translations in quantum mechanics.

## Kronecker Delta To Dirac Delta

For a discrete orthonormal basis:

$$
\langle i|j\rangle = \delta_{ij}
$$

and:

$$
I = \sum_i |i\rangle\langle i|
$$

For a continuous position basis, these become:

$$
\langle x|x'\rangle = \delta(x - x')
$$

and:

$$
I = \int dx |x\rangle\langle x|
$$

The Dirac delta is not an ordinary function. It is a rule that extracts a value from an integral:

$$
\int dx' \delta(x - x')\psi(x') = \psi(x)
$$

That is why it acts like the continuous version of "same basis vector or different basis vector."

## Derivatives And Representations Of The Delta Function

Shankar's notation becomes easier if the delta function is treated as a distribution rather than a literal spike. The derivative of the delta function is defined by moving the derivative onto the function being integrated against:

$$
\int_{-\infty}^{\infty} dx \delta'(x-a)f(x) = -f'(a)
$$

The minus sign comes from integration by parts. In distribution language, differentiating the delta function means asking how it acts on a smooth test function:

$$
\int dx \delta'(x-a)f(x) = -\int dx \delta(x-a)f'(x) = -f'(a)
$$

One way to picture $\delta(x)$ is as the limit of normalized Gaussians:

$$
\delta(x) = \lim_{\epsilon \to 0} \frac{1}{\sqrt{2\pi}\epsilon} e^{-x^2/2\epsilon^2}
$$

This is not a pointwise limit of ordinary functions. It means:

$$
\lim_{\epsilon \to 0} \int_{-\infty}^{\infty} dx \frac{1}{\sqrt{2\pi}\epsilon} e^{-x^2/2\epsilon^2}f(x) = f(0)
$$

The Fourier representation is:

$\displaystyle \delta(x)=\frac{1}{2\pi}\int_{-\infty}^{\infty} e^{ikx} dk$

A cutoff version makes the formula more concrete:

$\displaystyle \frac{1}{2\pi}\int_{-K}^{K} e^{ikx} dk=\frac{\sin(Kx)}{\pi x}$

As $K \to \infty$, this approaches $\delta(x)$ in the distribution sense: the oscillations cancel away from $x=0$, while the total effect under an integral samples the value at $0$.

The Gaussian and Fourier pictures are connected by a regulated Fourier integral:

$\displaystyle \frac{1}{2\pi}\int_{-\infty}^{\infty} e^{ikx}e^{-\epsilon k^2/2} dk=\frac{1}{\sqrt{2\pi\epsilon}}e^{-x^2/2\epsilon}$

Letting $\epsilon \to 0$ turns the right side into $\delta(x)$ and removes the regulator on the left. See [Dirac Delta Function](../../../Linear%20Algebra/Dirac%20Delta%20Function.md) for the standalone concept note.

## Operators In Infinite Dimensions

The clean way to read Shankar here is: an operator is still a linear map from vectors to vectors, but the coordinate representation no longer has to be a finite matrix.

In a finite-dimensional basis, an operator $A$ acts like this:

$$
|w\rangle = A|v\rangle
$$

Taking components gives:

$$
w_i = \sum_j A_{ij}v_j
$$

where:

$$
A_{ij} = \langle i|A|j\rangle
$$

In the continuous position basis, the discrete labels $i,j$ become continuous labels $x,x'$. The sum becomes an integral:

$$
\psi_A(x) = \langle x|A|\psi\rangle = \int dx' \langle x|A|x'\rangle \psi(x')
$$

The object

$$
A(x,x') = \langle x|A|x'\rangle
$$

is the continuous analogue of the matrix element $A_{ij}$. It is often called the **kernel** of the operator. So the dictionary is:

| Finite matrix language | Continuous operator language |
| --- | --- |
| $A_{ij}$ | $A(x,x')=\langle x\vert A\vert x'\rangle$ |
| $w_i=\sum_j A_{ij}v_j$ | $\psi_A(x)=\int dx' A(x,x')\psi(x')$ |
| identity matrix $\delta_{ij}$ | identity kernel $\delta(x-x')$ |
| diagonal matrix $A_{ij}=a_i\delta_{ij}$ | multiplication kernel $A(x,x')=a(x)\delta(x-x')$ |

### Identity Operator

The identity operator has kernel:

$$
I(x,x') = \langle x|I|x'\rangle = \delta(x-x')
$$

Then:

$$
(I\psi)(x) = \int dx' \delta(x-x')\psi(x') = \psi(x)
$$

This is exactly the continuous version of multiplying by the identity matrix.

### Multiplication Operators

The position operator $X$ acts on a wavefunction by multiplying it by $x$:

$$
(X\psi)(x)=x\psi(x)
$$

As a kernel, this same statement is:

$$
\langle x|X|x'\rangle = x\delta(x-x')
$$

because:

$$
(X\psi)(x) = \int dx' x\delta(x-x')\psi(x') = x\psi(x)
$$

This is why multiplication operators are like diagonal matrices. They do not mix different $x'$ values together; they only multiply the value already sitting at $x$.

### Derivative Operators

Differentiation is also a linear operator:

$$
(D\psi)(x)=\frac{d\psi}{dx}
$$

Its kernel can be written using a derivative of the delta function:

$$
D(x,x') = \frac{\partial}{\partial x}\delta(x-x')
$$

Then:

$$
(D\psi)(x) = \int dx' \frac{\partial}{\partial x}\delta(x-x')\psi(x') = \frac{\partial}{\partial x} \int dx' \delta(x-x')\psi(x') = \frac{d\psi}{dx}
$$

This is a subtle but important point: the derivative here is with respect to the output variable $x$, not the integration variable $x'$. That is why this expression gives $+\psi'(x)$. By contrast, the earlier identity

$$
\int dx \delta'(x-a)f(x)=-f'(a)
$$

has the derivative attached to the integration variable. Same delta distribution, different variable being differentiated. That little sign issue is one of the sneakiest parts of this section.

In quantum mechanics, the momentum operator in the position basis is:

$$
P = -i\hbar \frac{d}{dx}
$$

so:

$$
(P\psi)(x)=-i\hbar \frac{d\psi}{dx}
$$

and its kernel can be written as:

$$
\langle x|P|x'\rangle = -i\hbar \frac{\partial}{\partial x}\delta(x-x')
$$

### The Big Picture

When Shankar writes operators in infinite-dimensional spaces, keep asking:

- What are the input and output components?
- Is this operator multiplying the function, differentiating it, or mixing values through an integral?
- What is the kernel $\langle x|A|x'\rangle$?

The scary-looking notation is mostly the same old matrix multiplication wearing continuous labels:

$$
\sum_j A_{ij}v_j \quad \longrightarrow \quad \int dx' A(x,x')\psi(x')
$$

## How To Read This Section

The section can feel slippery because Shankar is changing what "vector" looks like without changing the underlying rules.

Keep this dictionary nearby:

| Finite-dimensional vectors | Infinite-dimensional / continuous version |
| --- | --- |
| column vector $v_i$ | function $\psi(x)$ |
| sum $\sum_i$ | integral $\int dx$ |
| basis vector $\vert i\rangle$ | position basis ket $\vert x\rangle$ |
| component $v_i = \langle i\vert v\rangle$ | wavefunction $\psi(x) = \langle x\vert\psi\rangle$ |
| Kronecker delta $\delta_{ij}$ | Dirac delta $\delta(x-x')$ |
| identity $\sum_i \vert i\rangle\langle i\vert$ | identity $\int dx \vert x\rangle\langle x\vert$ |
| matrix element $A_{ij}$ | kernel $A(x,x')=\langle x\vert A\vert x'\rangle$ |
| matrix multiplication $\sum_j A_{ij}v_j$ | integral action $\int dx' A(x,x')\psi(x')$ |

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
