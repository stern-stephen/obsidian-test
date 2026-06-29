# Project Instructions

## Obsidian Math Formatting

Use Obsidian-friendly MathJax syntax in Markdown notes.

- Inline math: `$A^\dagger$`
- Display math:

$$
A = A^\dagger
$$

When a list item mainly introduces an equation, put the label on its own line and place the equation in a `$$` display block. Do not put command-heavy MathJax, such as expressions containing `\mathbf`, subscripts, or superscripts, directly in the list item when the equation can stand alone. During validation, treat inline math in list items as a rendering-risk warning rather than an absolute error, since short inline expressions may still be appropriate.

Avoid `\(...\)` and `\[...\]` delimiters because they may not render nicely in the Obsidian UI.

When writing math inside Markdown tables, avoid literal `|` characters inside inline math because web Markdown renderers may treat them as table separators before MathJax renders. Use `\vert` for bra-ket separators in table cells, such as `$\langle x\vert A\vert x'\rangle$` instead of `$\langle x|A|x'\rangle$`.

For evaluated boundary terms, prefer bracket notation such as `$\left[f(x)\right]_{a}^{b}$` over sized vertical-bar forms like `\bigg|`, since bracket notation is more robust across Markdown/MathJax renderers.

Avoid LaTeX spacing commands such as `\,` in notes that should render cleanly in web Markdown previews. Some browser renderers expose them poorly when math parsing fails or is partial. Prefer ordinary spacing in the source, or rewrite expressions so the differential comes at the end, such as `$\int e^{ikx} dk$`.

For literal braces that should appear in rendered math, use `\lbrace` and `\rbrace` instead of `\{` and `\}`. GitHub Markdown may consume the backslashes in the shorter forms before its math renderer runs, causing notation such as Poisson brackets, anticommutators, and sets to display without braces.

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
- When the user asks a conceptual question and the answer would clarify or improve an existing durable note, update the appropriate concept note automatically unless the user asks for chat-only help.

## Book Chapter Navigation

For book chapter folders, make the chapter overview note act as the entry point.

- Prefer naming chapter overview notes as `Chapter Overview.md`.
- Link to the chapter overview from the book hub before the section notes.
- Add simple `Previous:` and `Next:` links near the top of each section note, after the book section/page metadata and before `## Reading Status`.
- The first section should link back to `Chapter Overview.md` as `Previous:`.
- The last section should usually have only a `Previous:` link unless there is a clear next chapter note to continue into.
- Keep navigation links as standard Markdown links with percent-encoded spaces.

## Textbook Exercise Answers

When adding answers to textbook exercises:

- Put answers in the corresponding section document, under a `## Exercise Answers` heading, unless the user asks for a separate solutions file.
- Keep exercise statements as short references only. Do not reproduce long copyrighted problem text.
- Write solutions in original words with enough intermediate steps to be useful for self-study.
- Preserve the book's exercise numbering exactly, such as `### Exercise 1.8.10`.
- If exercise numbering or content is uncertain, verify against the local PDF and note any uncertainty.
- For matrix-heavy answers, sanity-check eigenvalues, eigenvectors, commutators, traces, determinants, and normalization with a quick computation when practical.
- For section-specific answer work, update only the relevant section notes unless a hub link or topic note is clearly needed.
- Before finishing, scan the edited notes for the vault's MathJax conventions and run a Git diff check when possible.

## Graphify Without API Keys

The user does not currently have an API key to give Graphify. Use Graphify as a local navigation and graph-structure tool, and let Codex do the semantic reading and synthesis.

- Use non-LLM Graphify commands such as `graphify query`, `graphify path`, `graphify explain`, and structural `graphify update` when helpful.
- Phrase Graphify queries around concrete anchors: note titles, headings, filenames, and known concept names.
- Treat Graphify output as a map to likely files and relationships, not as the authority.
- Read the actual Markdown notes or local source PDFs before answering conceptual questions or editing notes.
- When a semantic relationship is missing from the graph, add explicit Markdown links, headings, or durable concept-note text so future structural graph updates can discover it.
- Do not rely on Graphify's LLM-backed semantic extraction unless the user later provides a suitable API key.

## Embedded Semantic Graph

This vault has a Kuzu-based semantic graph prototype. Store authored semantic relationships in hidden `semantic-edges` HTML comment blocks inside the Markdown notes that justify them, not in one large hand-edited registry file.

- Use `Graph/README.md` for the embedded edge format.
- Use `python scripts\kuzu_build.py` to rebuild the local Kuzu database at `Graph/kuzu-db`.
- Use `python scripts\kuzu_query.py "Concept Name"` to query a concept's semantic neighborhood.
- Keep `Graph/kuzu-db` ignored because it is rebuildable from Markdown.
- Each semantic edge should include `source`, `relation`, `target`, `evidence_heading`, `evidence_summary`, and `confidence`; the build script adds `evidence_path` from the containing Markdown file.
- Prefer placing edge blocks near the bottom of the relevant source or concept note so the relationship is close to its evidence.

## Git Workflow

This project is an Obsidian vault stored in Git.

Codex may perform simple, non-destructive Git interactions when they help with the user's request, including:

- Checking repository state with `git status`.
- Reviewing history with `git log`.
- Reviewing changes with `git diff`.
- Staging current project changes with `git add`.
- Creating normal commits with `git commit` when the user asks to commit.

Codex should ask before destructive or history-rewriting Git operations, including `git reset`, `git clean`, force pushes, rebases that rewrite published history, or checking out files in a way that would discard local changes.
