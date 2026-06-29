# Subspaces

Source: [Principles of Quantum Mechanics](../../../References/Principals%20of%20quantum%20mechanics%20Shankar%20.pdf)

Book hub: [Shankar](../Shankar.md)

Book section: 1.4.

Previous: [Dual Spaces and Dirac Notation](Dual%20Spaces%20and%20Dirac%20Notation.md)

Next: [Linear Operators](Linear%20Operators.md)

## Reading Status

- Status: started
- Pages:
- Date started: 2026-05-17
- Date finished:

## Big Ideas

- A subspace is a smaller vector space inside a larger vector space.
- Subspaces must be closed under vector addition and scalar multiplication.
- Orthogonal complements split a vector space into mutually perpendicular pieces.
- Projection operators are the operator language for extracting the part of a vector that lies in a subspace.

## Notes

Shankar develops subspaces after dual vectors because orthogonality now lets the full space be decomposed into a subspace and its orthogonal complement. This becomes the geometric basis for projection operators and, later, projection onto eigenspaces during measurement.

The general closure and span definitions remain in [Vector Spaces](../../../Linear%20Algebra/Vector%20Spaces.md). Projection formulas and the decomposition into retained and orthogonal components live in [Projection Operators](../../../Linear%20Algebra/Projection%20Matrices.md).

## Common Confusions

- A subset is not automatically a subspace. It must be closed under addition and scalar multiplication.
- A line that does not pass through the origin is not a subspace.
- Orthogonal complements depend on the inner product.

## Exercise Answers

These are answer summaries for Shankar Chapter 1 exercises in this section. I am not reproducing the full problem statements here.

### Exercise 1.4.1

Let $|V\rangle\ne |0\rangle$ in an $n$-dimensional vector space. Consider:

$$
W=\lbrace |W\rangle:\langle V|W\rangle=0\rbrace
$$

First show $W$ is a subspace. If $|W_1\rangle,|W_2\rangle\in W$, then:

$$
\langle V|(aW_1+bW_2)\rangle=a\langle V|W_1\rangle+b\langle V|W_2\rangle=0
$$

So $a|W_1\rangle+b|W_2\rangle$ is also in $W$.

Now normalize $|V\rangle$ and extend it to an orthonormal basis by Gram-Schmidt:

$$
\lbrace |e_1\rangle,|e_2\rangle,\ldots,|e_n\rangle\rbrace
$$

with $|e_1\rangle$ parallel to $|V\rangle$. The vectors:

$$
|e_2\rangle,\ldots,|e_n\rangle
$$

span exactly the vectors orthogonal to $|V\rangle$. There are $n-1$ of them, so the orthogonal complement has dimension $n-1$.

### Exercise 1.4.2

Let $V_1$ and $V_2$ have dimensions $n_1$ and $n_2$, and suppose every vector in $V_1$ is orthogonal to every vector in $V_2$.

Choose an orthonormal basis for $V_1$:

$$
\lbrace |e_1\rangle,\ldots,|e_{n_1}\rangle\rbrace
$$

and an orthonormal basis for $V_2$:

$$
\lbrace |f_1\rangle,\ldots,|f_{n_2}\rangle\rbrace
$$

Because the two subspaces are orthogonal, the combined list is still orthonormal:

$$
\lbrace |e_1\rangle,\ldots,|e_{n_1}\rangle,|f_1\rangle,\ldots,|f_{n_2}\rangle\rbrace
$$

This gives $n_1+n_2$ mutually orthogonal basis vectors for $V_1\oplus V_2$. Therefore:

$$
\dim(V_1\oplus V_2)=n_1+n_2
$$

## Links To Concept Notes

- [Vector Spaces](../../../Linear%20Algebra/Vector%20Spaces.md)
- [Projection Operators](../../../Linear%20Algebra/Projection%20Matrices.md)
- [Four Fundamental Subspaces](../../../Linear%20Algebra/Four%20Fundamental%20Subspaces.md)
- [Gram-Schmidt](../../../Linear%20Algebra/Gram-Schmidt.md)

<!-- semantic-edges
{"source":"Subspaces","relation":"PART_OF","target":"Shankar Chapter 1","evidence_heading":"Book metadata","evidence_summary":"This note is a source-specific section note in Shankar Chapter 1.","confidence":0.85}
{"source":"Subspaces","relation":"SOURCE_CONTEXT_FOR","target":"Dual Spaces and Dirac Notation","evidence_heading":"Subspaces","evidence_summary":"This source note explicitly links its treatment to Dual Spaces and Dirac Notation.","confidence":0.8}
{"source":"Subspaces","relation":"SOURCE_CONTEXT_FOR","target":"Linear Operators","evidence_heading":"Subspaces","evidence_summary":"This source note explicitly links its treatment to Linear Operators.","confidence":0.8}
{"source":"Subspaces","relation":"SOURCE_CONTEXT_FOR","target":"Vector Spaces","evidence_heading":"Notes","evidence_summary":"This source note explicitly links its treatment to Vector Spaces.","confidence":0.8}
{"source":"Subspaces","relation":"SOURCE_CONTEXT_FOR","target":"Projection Operators","evidence_heading":"Notes","evidence_summary":"This source note explicitly links its treatment to Projection Operators.","confidence":0.8}
-->
