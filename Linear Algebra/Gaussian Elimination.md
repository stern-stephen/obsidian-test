# Gaussian Elimination

## Overview

**Gaussian elimination** is a method for solving systems of linear equations by simplifying a matrix using row operations.

It turns a system into an equivalent system that is easier to solve.

For a linear system:

$$
Ax = b
$$

Gaussian elimination works with the augmented matrix:

$$
\begin{bmatrix}
A & b
\end{bmatrix}
$$

## Elementary Row Operations

Gaussian elimination uses three row operations:

- Swap two rows.
- Multiply a row by a nonzero scalar.
- Add a multiple of one row to another row.

These operations do not change the solution set of the system.

## Row Echelon Form

The goal is usually to reach **row echelon form**, where:

- All zero rows are at the bottom.
- Each leading entry, or pivot, is to the right of the pivot above it.
- Entries below each pivot are zero.

For example:

$$
\begin{bmatrix}
1 & 2 & -1 & 3 \\
0 & 1 & 4 & -2 \\
0 & 0 & 1 & 5
\end{bmatrix}
$$

is in row echelon form.

Once a matrix is in row echelon form, the system can be solved by **back substitution**.

## Reduced Row Echelon Form

**Gauss-Jordan elimination** continues the process until the matrix is in **reduced row echelon form**, where:

- Each pivot is $1$.
- Each pivot is the only nonzero entry in its column.

For example:

$$
\begin{bmatrix}
1 & 0 & 0 & 2 \\
0 & 1 & 0 & -1 \\
0 & 0 & 1 & 4
\end{bmatrix}
$$

This form gives the solution directly.

## Pivots And Free Variables

A **pivot column** contains a leading entry.

Variables corresponding to pivot columns are **pivot variables**. Variables corresponding to non-pivot columns are **free variables**.

Free variables appear when the system has infinitely many solutions.

## Rank

The number of pivots is the **rank** of the matrix.

Rank measures how many independent directions the matrix keeps. It is closely connected to the [Four Fundamental Subspaces](Four%20Fundamental%20Subspaces.md):

- The rank is the dimension of the column space.
- The rank is also the dimension of the row space.

## Example

Consider:

$$
\begin{aligned}
x + y &= 3 \\
2x + 3y &= 8
\end{aligned}
$$

The augmented matrix is:

$$
\begin{bmatrix}
1 & 1 & 3 \\
2 & 3 & 8
\end{bmatrix}
$$

Subtract $2$ times the first row from the second row:

$$
\begin{bmatrix}
1 & 1 & 3 \\
0 & 1 & 2
\end{bmatrix}
$$

The second row gives:

$$
y = 2
$$

Then the first row gives:

$$
x + 2 = 3
$$

so:

$$
x = 1
$$

## Common Confusions

- Row operations preserve the solution set of $Ax = b$, but they may change the column space of $A$.
- Pivot columns in the original matrix form a basis for the column space.
- Free variables do not mean there is no solution. They mean there are infinitely many solutions, as long as the system is consistent.

## Related Concepts

- [Linear Algebra](Linear%20Algebra.md)
- [Matrices](Matrices.md)
- [Vector Spaces](Vector%20Spaces.md)
- [Vectors](Vectors.md)
- [Four Fundamental Subspaces](Four%20Fundamental%20Subspaces.md)
