# Functions of Operators

Source: [Principles of Quantum Mechanics](../../../References/Principals%20of%20quantum%20mechanics%20Shankar%20.pdf)

Book hub: [Shankar](../Shankar.md)

Book section: 1.9.

## Reading Status

- Status: started
- Pages:
- Date started: 2026-05-17
- Date finished:

## Big Ideas

- Section 1.9 explains how expressions like $f(A)$ make sense when $A$ is an operator rather than an ordinary number.
- The cleanest case is when $A$ has a basis of eigenvectors. Then $f(A)$ acts on each eigenvector by replacing the eigenvalue $\lambda$ with $f(\lambda)$.
- This is why diagonalization matters: a hard operator function becomes an easy scalar function in the eigenbasis.
- Operator functions are especially important later for time evolution, where expressions like $e^{-iHt/\hbar}$ appear.

## Notes

For an ordinary number, $f(x)$ is familiar. For an operator $A$, the expression $f(A)$ means "build a new operator from $A$."

The easiest starting point is a polynomial:

$$
f(x) = a_0 + a_1x + a_2x^2
$$

Then:

$$
f(A) = a_0I + a_1A + a_2A^2
$$

This works because sums, scalar multiples, and products of operators are already defined.

The same idea extends to power series, such as the exponential:

$$
e^A = I + A + \frac{A^2}{2!} + \frac{A^3}{3!} + \cdots
$$

The important simplification comes from eigenvectors. If:

$$
A|a_i\rangle = a_i|a_i\rangle
$$

then:

$$
f(A)|a_i\rangle = f(a_i)|a_i\rangle
$$

So $A$ and $f(A)$ have the same eigenvectors, while the eigenvalues get transformed by $f$.

## Why This Helps

If a vector is expanded in the eigenbasis of $A$:

$$
|\psi\rangle = \sum_i c_i |a_i\rangle
$$

then:

$$
f(A)|\psi\rangle = \sum_i c_i f(a_i)|a_i\rangle
$$

This is the main mental model: decompose the vector into eigen-directions, apply the scalar function to each eigenvalue, and put the pieces back together.

## Spectral Form

If the eigenvectors form an orthonormal basis, the operator can be written:

$$
A = \sum_i a_i |a_i\rangle\langle a_i|
$$

Then:

$$
f(A) = \sum_i f(a_i)|a_i\rangle\langle a_i|
$$

The object $|a_i\rangle\langle a_i|$ is the projection onto the eigendirection $|a_i\rangle$.

## Common Confusions

- $f(A)$ is not found by applying $f$ to each matrix entry. It is found by using operator algebra or, when possible, by diagonalizing $A$ and applying $f$ to the eigenvalues.
- Diagonal matrices are special because their diagonal entries are their eigenvalues.
- If $A$ is diagonalizable, write it in its eigenbasis first, apply $f$ to the eigenvalues, and then translate back if needed.

## Study Questions

- If $A|a\rangle = a|a\rangle$, why does $A^2|a\rangle = a^2|a\rangle$?
- If $A$ is diagonal with entries $a_1,a_2,\ldots,a_n$, what is $e^A$?
- Why does $f(A)$ usually not mean applying $f$ separately to every matrix entry?

## Links To Concept Notes

- [Functions of Operators](../../../Linear%20Algebra/Functions%20of%20Operators.md)
- [Linear Operators](../../../Linear%20Algebra/Linear%20Operators.md)
- [Eigenvalues and Eigenvectors](../../../Linear%20Algebra/Eigenvalues%20and%20Eigenvectors.md)
- [Projection Operators](../../../Linear%20Algebra/Projection%20Matrices.md)
- [Bra-Ket Notation](../../../Linear%20Algebra/Bra-Ket%20Notation.md)
- [Infinite-Dimensional Spaces](Infinite-Dimensional%20Spaces.md)
