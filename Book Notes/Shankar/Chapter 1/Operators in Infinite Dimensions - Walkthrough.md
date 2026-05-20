# Operators in Infinite Dimensions - Walkthrough

Source: [Principles of Quantum Mechanics](../../../References/Principals%20of%20quantum%20mechanics%20Shankar%20.pdf)

Book hub: [Shankar](../Shankar.md)

Related section note: [Infinite-Dimensional Spaces](Infinite-Dimensional%20Spaces.md)

Book section: Chapter 1, "Operators in Infinite Dimensions."

## Why This Section Feels Hard

This part is difficult because Shankar is doing two conceptual jumps at once:

1. A vector is no longer drawn as a finite column of numbers.
2. An operator is no longer drawn as a finite matrix of numbers.

But the underlying idea has not changed. An operator is still a rule that takes one vector and produces another vector:

$$
|\psi\rangle \mapsto A|\psi\rangle
$$

The only new issue is how to write that rule when the vector's components are labeled by a continuous variable like $x$ instead of a discrete index like $i$.

The guiding slogan for this section is:

**An infinite-dimensional operator is a matrix whose row and column labels have become continuous.**

So finite matrix multiplication,

$$
w_i = \sum_j A_{ij}v_j
$$

turns into continuous kernel action,

$$
(A\psi)(x) = \int dx' A(x,x')\psi(x')
$$

Most of the section is unpacking what that sentence really means.

## Step 1: Remember Ordinary Matrix Multiplication

Start with a finite-dimensional vector space. Suppose $|v\rangle$ has components $v_j$ in some basis $|j\rangle$:

$$
|v\rangle = \sum_j v_j |j\rangle
$$

Now apply an operator $A$:

$$
|w\rangle = A|v\rangle
$$

The output vector $|w\rangle$ has components $w_i$. In a finite basis, the components are found by matrix multiplication:

$$
w_i = \sum_j A_{ij}v_j
$$

The matrix element $A_{ij}$ answers this question:

**How much does input basis direction $j$ contribute to output basis direction $i$?**

In bra-ket notation:

$$
A_{ij} = \langle i|A|j\rangle
$$

The right index $j$ is the input label. The left index $i$ is the output label.

That input-output distinction is the thing to keep alive when the notation changes.

## Step 2: Replace Discrete Labels By Continuous Labels

In the position basis, the basis labels are not $i,j=1,2,3,\ldots$. They are continuous labels $x,x'$.

The finite basis vector $|i\rangle$ becomes an idealized position basis vector $|x\rangle$.

The finite component $v_i$ becomes the wavefunction value:

$$
\psi(x) = \langle x|\psi\rangle
$$

This does not mean the wavefunction is a different physical object from $|\psi\rangle$. It means:

**$\psi(x)$ is the coordinate representation of the abstract vector $|\psi\rangle$ in the position basis.**

The finite expansion

$$
|v\rangle = \sum_i v_i |i\rangle
$$

becomes the continuous expansion

$$
|\psi\rangle = \int dx \psi(x)|x\rangle
$$

So the replacements are:

| Finite-dimensional notation | Continuous position-basis notation |
| --- | --- |
| basis label $i$ | basis label $x$ |
| component $v_i$ | wavefunction $\psi(x)$ |
| sum $\sum_i$ | integral $\int dx$ |
| basis vector $\vert i\rangle$ | basis ket $\vert x\rangle$ |
| matrix element $A_{ij}$ | kernel $A(x,x')$ |

The prime on $x'$ is not decoration. It helps you remember that $x'$ is the input coordinate being integrated over, while $x$ is the output coordinate being reported.

## Step 3: The Operator Kernel Is The Infinite Matrix

In finite dimensions:

$$
A_{ij} = \langle i|A|j\rangle
$$

In the continuous position basis:

$$
A(x,x') = \langle x|A|x'\rangle
$$

This object $A(x,x')$ is called the **kernel** of the operator.

Read it as:

**If the input is concentrated at $x'$, how much does $A$ contribute to the output at $x$?**

Then the action of $A$ on a wavefunction is:

$$
(A\psi)(x) = \int dx' A(x,x')\psi(x')
$$

This is just matrix multiplication with the sum replaced by an integral:

$$
w_i = \sum_j A_{ij}v_j
$$

becomes:

$$
(A\psi)(x) = \int dx' A(x,x')\psi(x')
$$

The kernel tells you how the operator mixes all input positions $x'$ into the output position $x$.

## Step 4: The Identity Operator

The identity operator should do nothing:

$$
I|\psi\rangle = |\psi\rangle
$$

In the position representation, this means:

$$
(I\psi)(x) = \psi(x)
$$

What kernel makes that happen?

The answer is the Dirac delta:

$$
I(x,x') = \langle x|I|x'\rangle = \delta(x-x')
$$

Check it by putting it into the kernel formula:

$$
(I\psi)(x) = \int dx' \delta(x-x')\psi(x')
$$

The delta function samples the integrand at $x'=x$, so:

$$
(I\psi)(x) = \psi(x)
$$

This is exactly parallel to the finite-dimensional identity matrix:

$$
\delta_{ij}
$$

In finite dimensions:

$$
w_i = \sum_j \delta_{ij}v_j = v_i
$$

In continuous dimensions:

$$
(I\psi)(x) = \int dx' \delta(x-x')\psi(x') = \psi(x)
$$

So the Dirac delta is acting like the continuous version of the Kronecker delta.

## Step 5: Multiplication Operators Are Like Diagonal Matrices

Now consider the position operator $X$. In the position basis, it acts by multiplication:

$$
(X\psi)(x) = x\psi(x)
$$

This is a linear operator because:

$$
X(a\psi + b\phi) = aX\psi + bX\phi
$$

Its kernel is:

$$
\langle x|X|x'\rangle = x\delta(x-x')
$$

Check:

$$
(X\psi)(x) = \int dx' x\delta(x-x')\psi(x')
$$

Since $x$ is not the integration variable, it can be treated as fixed while integrating over $x'$:

$$
(X\psi)(x) = x\int dx' \delta(x-x')\psi(x')
$$

The delta function samples $\psi(x')$ at $x'=x$:

$$
(X\psi)(x) = x\psi(x)
$$

So the kernel is correct.

Why is this like a diagonal matrix? A diagonal matrix has the form:

$$
A_{ij} = a_i\delta_{ij}
$$

It does not mix component $j$ into a different component $i$. It only multiplies each component by a number.

The continuous version is:

$$
A(x,x') = a(x)\delta(x-x')
$$

So multiplication by $a(x)$ is the infinite-dimensional analogue of a diagonal matrix.

## Step 6: Nonlocal Kernels Mix Different Positions

Not every operator is a multiplication operator. A general kernel can mix values of the function from many different input points $x'$ into a single output point $x$:

$$
(A\psi)(x) = \int dx' A(x,x')\psi(x')
$$

If $A(x,x')$ is nonzero for many values of $x'$ when $x$ is fixed, then the value of $(A\psi)(x)$ depends on the whole function $\psi$, not just on $\psi(x)$.

This is the continuous version of a matrix with many nonzero off-diagonal entries. Off-diagonal entries mix different components.

So:

- diagonal matrix: each output component depends only on the matching input component
- non-diagonal matrix: each output component may depend on many input components
- multiplication kernel $a(x)\delta(x-x')$: output at $x$ depends only on input at $x$
- general kernel $A(x,x')$: output at $x$ may depend on input at many $x'$

That is the basic meaning of a kernel.

## Step 7: The Derivative Operator

Differentiation is another linear operator:

$$
(D\psi)(x) = \frac{d\psi}{dx}
$$

It is linear because:

$$
\frac{d}{dx}(a\psi + b\phi) = a\frac{d\psi}{dx} + b\frac{d\phi}{dx}
$$

Shankar writes derivative operators using derivatives of the delta function. The kernel for $D$ can be written:

$$
D(x,x') = \langle x|D|x'\rangle = \frac{\partial}{\partial x}\delta(x-x')
$$

Now check that this really differentiates $\psi$:

$$
(D\psi)(x) = \int dx' \frac{\partial}{\partial x}\delta(x-x')\psi(x')
$$

The derivative is with respect to $x$, the output variable. Since the integration is over $x'$, we can move the $x$ derivative outside the integral:

$$
(D\psi)(x) = \frac{\partial}{\partial x}\int dx' \delta(x-x')\psi(x')
$$

The integral inside is just $\psi(x)$:

$$
(D\psi)(x) = \frac{d\psi}{dx}
$$

So the kernel works.

## Step 8: The Sign Trap With Delta Derivatives

This is one of the easiest places to get lost.

You may also know the distribution identity:

$$
\int dx \delta'(x-a)f(x) = -f'(a)
$$

That has a minus sign. So why did the derivative kernel above give $+\psi'(x)$?

The answer is: the derivative is being taken with respect to a different variable.

In

$$
\int dx \delta'(x-a)f(x)
$$

the derivative is with respect to the integration variable $x$. Integration by parts moves the derivative from the delta function onto $f(x)$, producing a minus sign:

$$
\int dx \delta'(x-a)f(x) = -\int dx \delta(x-a)f'(x) = -f'(a)
$$

But in the kernel expression

$$
\int dx' \frac{\partial}{\partial x}\delta(x-x')\psi(x')
$$

the derivative is with respect to $x$, not $x'$. The variable $x$ is not being integrated over. So the derivative can be pulled outside the integral:

$$
\int dx' \frac{\partial}{\partial x}\delta(x-x')\psi(x') = \frac{\partial}{\partial x}\int dx' \delta(x-x')\psi(x')
$$

That gives:

$$
\frac{d\psi}{dx}
$$

Same delta distribution, different derivative variable.

A useful identity is:

$$
\frac{\partial}{\partial x}\delta(x-x') = -\frac{\partial}{\partial x'}\delta(x-x')
$$

If you rewrite the kernel derivative using $x'$ instead of $x$, then the integration-by-parts minus sign appears and cancels the explicit minus sign above. The final operator is still $+\frac{d}{dx}$.

## Step 9: Momentum As A Derivative Operator

In the position representation, the momentum operator is:

$$
P = -i\hbar D
$$

Since $D=\frac{d}{dx}$, this means:

$$
(P\psi)(x) = -i\hbar \frac{d\psi}{dx}
$$

Its kernel is therefore:

$$
\langle x|P|x'\rangle = -i\hbar \frac{\partial}{\partial x}\delta(x-x')
$$

This formula looks strange at first, but it is just the derivative-operator kernel multiplied by $-i\hbar$.

The physics reason this matters is that momentum is the generator of translations. A derivative measures how a function changes under a small shift in position, so it is natural that momentum becomes a derivative in the position basis.

## Step 10: Hermitian Operators In Kernel Language

In finite dimensions, a Hermitian matrix satisfies:

$$
A_{ij} = A_{ji}^*
$$

Equivalently:

$$
A^\dagger = A
$$

In the continuous basis, the analogous condition is:

$$
A(x,x') = A^*(x',x)
$$

This is the continuous version of "transpose and complex conjugate."

Why swap $x$ and $x'$? Because transposition swaps row and column labels. In the kernel, $x$ is the output label and $x'$ is the input label. Taking the adjoint swaps input and output.

So:

$$
\langle x|A^\dagger|x'\rangle = \langle x'|A|x\rangle^*
$$

If $A$ is Hermitian, then $A^\dagger=A$, giving:

$$
\langle x|A|x'\rangle = \langle x'|A|x\rangle^*
$$

In kernel notation:

$$
A(x,x') = A^*(x',x)
$$

This is important because physical observables in quantum mechanics are represented by Hermitian operators.

## Step 11: Why The Derivative Alone Is Not Hermitian

Consider the derivative operator:

$$
D = \frac{d}{dx}
$$

Use the function-space inner product:

$$
\langle \phi|\psi\rangle = \int dx \phi^*(x)\psi(x)
$$

Then:

$$
\langle \phi|D\psi\rangle = \int dx \phi^*(x)\frac{d\psi}{dx}
$$

Integrate by parts:

$$
\int dx \phi^*(x)\frac{d\psi}{dx} = \left[\phi^*(x)\psi(x)\right]_{-\infty}^{\infty} - \int dx \frac{d\phi^*}{dx}\psi(x)
$$

For wavefunctions that vanish at infinity, the boundary term is zero:

$$
\left[\phi^*(x)\psi(x)\right]_{-\infty}^{\infty} = 0
$$

So:

$$
\langle \phi|D\psi\rangle = -\int dx \left(\frac{d\phi}{dx}\right)^*\psi(x)
$$

That means:

$$
D^\dagger = -D
$$

So $D$ is not Hermitian. It is anti-Hermitian.

But momentum is:

$$
P = -i\hbar D
$$

Taking the adjoint:

$$
P^\dagger = (-i\hbar D)^\dagger = i\hbar D^\dagger
$$

Since $D^\dagger=-D$:

$$
P^\dagger = i\hbar(-D) = -i\hbar D = P
$$

So momentum is Hermitian, at least on the right domain of wavefunctions with suitable boundary behavior.

This is the deeper reason for the factor $-i$ in the momentum operator.

## Step 12: Domain Issues Are The Hidden New Difficulty

Finite-dimensional linear algebra is forgiving. If $A$ is a finite matrix, it acts on every finite column vector of the right size.

Infinite-dimensional operators are more delicate. A derivative operator does not act nicely on every possible function. The function must be differentiable, and the derivative must still belong to the space under discussion.

For example, if the state space consists of square-integrable wavefunctions, then $D\psi$ must also be square-integrable for $D\psi$ to be a valid output state.

This is called a **domain** issue.

Shankar often keeps the discussion formal at this point because the physics intuition is the main goal. But the mathematical caution is:

**In infinite dimensions, an operator is not fully specified until you know which functions it is allowed to act on.**

This especially matters for derivative operators, momentum, Hamiltonians, and boundary conditions.

## Step 13: A Worked Mini-Example

Let:

$$
\psi(x) = e^{-x^2}
$$

The position operator gives:

$$
(X\psi)(x) = xe^{-x^2}
$$

The derivative operator gives:

$$
(D\psi)(x) = \frac{d}{dx}e^{-x^2}
$$

So:

$$
(D\psi)(x) = -2xe^{-x^2}
$$

The momentum operator gives:

$$
(P\psi)(x) = -i\hbar \frac{d}{dx}e^{-x^2}
$$

Therefore:

$$
(P\psi)(x) = 2i\hbar x e^{-x^2}
$$

So $X$, $D$, and $P$ are all operators on the same input function, but they produce different output functions.

That is all an operator does: it turns one vector into another vector.

## Step 14: How To Read Each Symbol

Here is the main expression:

$$
(A\psi)(x) = \int dx' \langle x|A|x'\rangle \psi(x')
$$

Read it piece by piece:

- $(A\psi)(x)$ means "the $x$-component of the vector after $A$ acts on $\psi$."
- $\int dx'$ means "add up contributions from all possible input positions."
- $\langle x|A|x'\rangle$ means "the amount that input position $x'$ contributes to output position $x$ through $A$."
- $\psi(x')$ means "the input wavefunction's component at $x'$."

In words:

**To get the output value at $x$, take every input value $\psi(x')$, weight it by the kernel $A(x,x')$, and integrate over all input positions $x'$.**

That is the whole section in one sentence.

## Step 15: The Core Dictionary

| Finite matrices | Infinite-dimensional operators |
| --- | --- |
| vector component $v_i$ | wavefunction component $\psi(x)$ |
| basis vector $\vert i\rangle$ | position ket $\vert x\rangle$ |
| matrix element $A_{ij}$ | kernel $A(x,x')=\langle x\vert A\vert x'\rangle$ |
| output component $w_i$ | output wavefunction $(A\psi)(x)$ |
| matrix multiplication $\sum_j A_{ij}v_j$ | kernel action $\int dx' A(x,x')\psi(x')$ |
| identity matrix $\delta_{ij}$ | identity kernel $\delta(x-x')$ |
| diagonal matrix $a_i\delta_{ij}$ | multiplication kernel $a(x)\delta(x-x')$ |
| transpose conjugate $A_{ji}^*$ | adjoint kernel $A^*(x',x)$ |
| Hermitian matrix $A_{ij}=A_{ji}^*$ | Hermitian kernel $A(x,x')=A^*(x',x)$ |

## Common Sticking Points

- **The wavefunction is a component list.** It is like a column vector with continuously many entries.
- **The kernel is a matrix.** It is like a matrix with continuously many rows and columns.
- **The delta function is the identity matrix.** It selects the matching continuous label.
- **Multiplication operators are diagonal.** They multiply each position component without mixing different positions.
- **Derivative operators are local but not diagonal.** They use nearby behavior of the function, so they are not simple multiplication operators.
- **The prime on $x'$ matters.** It marks the input variable being integrated over.
- **Signs with $\delta'$ depend on the differentiated variable.** Differentiating with respect to the integration variable gives a minus sign after integration by parts; differentiating with respect to the output variable does not.
- **Hermiticity requires swapping input and output.** In kernel language, that means swapping $x$ and $x'$ and complex conjugating.
- **Domains matter.** Infinite-dimensional operators may only be valid on certain classes of functions.

## Quick Self-Test

1. If $A(x,x')=\delta(x-x')$, what is $(A\psi)(x)$?
2. If $A(x,x')=x^2\delta(x-x')$, what does $A$ do to $\psi(x)$?
3. Why is $\int dx' A(x,x')\psi(x')$ the continuous version of $\sum_j A_{ij}v_j$?
4. Why does $\frac{\partial}{\partial x}\delta(x-x')$ give $+\psi'(x)$ when integrated over $x'$?
5. What kernel condition corresponds to a Hermitian operator?

Answers:

1. $(A\psi)(x)=\psi(x)$.
2. $(A\psi)(x)=x^2\psi(x)$.
3. The discrete input label $j$ becomes the continuous input label $x'$, so the sum becomes an integral.
4. The derivative is with respect to the output variable $x$, not the integration variable $x'$.
5. $A(x,x')=A^*(x',x)$.

## Mental Model To Keep

When the notation gets dense, translate it back to this:

$$
\text{output component} = \text{sum of matrix entries times input components}
$$

Then replace "sum" by "integral":

$$
\text{output value at }x = \text{integral of kernel entries times input values}
$$

That is the heart of operators in infinite dimensions.

## Related Concept Notes

- [Infinite-Dimensional Vector Spaces](../../../Linear%20Algebra/Infinite-Dimensional%20Vector%20Spaces.md)
- [Linear Operators](../../../Linear%20Algebra/Linear%20Operators.md)
- [Dirac Delta Function](../../../Linear%20Algebra/Dirac%20Delta%20Function.md)
- [Bra-Ket Notation](../../../Linear%20Algebra/Bra-Ket%20Notation.md)
- [Adjoints](../../../Linear%20Algebra/Adjoints.md)
- [Hermitian Matrices and Operators](../../../Linear%20Algebra/Hermitian%20Matrices%20and%20Operators.md)
