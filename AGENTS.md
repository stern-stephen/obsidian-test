# Project Instructions

## Obsidian Math Formatting

Use Obsidian-friendly MathJax syntax in Markdown notes.

- Inline math: `$A^\dagger$`
- Display math:

$$
A = A^\dagger
$$

Avoid `\(...\)` and `\[...\]` delimiters because they may not render nicely in the Obsidian UI.

When writing math inside Markdown tables, avoid literal `|` characters inside inline math because web Markdown renderers may treat them as table separators before MathJax renders. Use `\vert` for bra-ket separators in table cells, such as `$\langle x\vert A\vert x'\rangle$` instead of `$\langle x|A|x'\rangle$`.

For evaluated boundary terms, prefer bracket notation such as `$\left[f(x)\right]_{a}^{b}$` over sized vertical-bar forms like `\bigg|`, since bracket notation is more robust across Markdown/MathJax renderers.

Avoid LaTeX spacing commands such as `\,` in notes that should render cleanly in web Markdown previews. Some browser renderers expose them poorly when math parsing fails or is partial. Prefer ordinary spacing in the source, or rewrite expressions so the differential comes at the end, such as `$\int e^{ikx} dk$`.

For simple display equations, keep the math expression on a single line between `$$` delimiters. Some browser Markdown renderers fail on stacked display equations such as putting `=` on separate lines. Multi-line display blocks are fine for true structured environments such as `\begin{bmatrix}...\end{bmatrix}`.

## Markdown Links

Use standard Markdown links instead of Obsidian wiki links so notes remain readable in regular editors and on GitHub.

- Prefer `[Eigenvalues](Linear%20Algebra/Eigenvalues%20and%20Eigenvectors.md)` over Obsidian wiki-link syntax.
- Use relative links from the current note.
- Percent-encode spaces in link destinations, such as `Book%20Notes/Nielsen%20Chuang/Nielsen%20Chuang.md`.
- Section links should use Markdown anchors, such as `[Pauli Matrices](Linear%20Algebra/Eigenvalues%20and%20Eigenvectors.md#pauli-matrices)`.

## Book Notes And Topic Notes

Keep book notes and topic notes separate.

- Use `Book Notes/` for source-specific reading notes: what a particular book says, section references, examples, page ranges, questions, and reading status.
- Use topic folders such as `Linear Algebra/`, `Quantum Mechanics/`, and `Quantum Computing/` for reusable concepts that span multiple books.
- When a book section introduces a durable concept, create or update the relevant topic note and link to it from the book note.
- Do not let general explanations live only inside a book note when they will be useful across books.
- Topic notes should synthesize in original words and may link back to the book sections that motivated them.

## Git Workflow

This project is an Obsidian vault stored in Git.

Codex may perform simple, non-destructive Git interactions when they help with the user's request, including:

- Checking repository state with `git status`.
- Reviewing history with `git log`.
- Reviewing changes with `git diff`.
- Staging current project changes with `git add`.
- Creating normal commits with `git commit` when the user asks to commit.

Codex should ask before destructive or history-rewriting Git operations, including `git reset`, `git clean`, force pushes, rebases that rewrite published history, or checking out files in a way that would discard local changes.
