# Semantic Graph Prototype

This folder holds a small Kuzu-based graph experiment for the vault.

The durable source is hidden `semantic-edges` blocks embedded in Markdown notes. Each JSON line inside a block is one authored semantic edge with source, relation, target, evidence, and confidence.

The build also parses ordinary Markdown links between notes. The local Kuzu database lives at `Graph/kuzu-db/` and is ignored by Git because it can be rebuilt from the Markdown files.

## Graph Layers

The Kuzu graph contains two layers:

- Automatic structural links: `(:Note)-[:LINKS_TO]->(:Note)` from standard Markdown links.
- Curated semantic edges: `(:Concept)-[:SEMANTIC_EDGE {relation: "..."}]->(:Concept)` from hidden `semantic-edges` blocks.

Use ordinary Markdown links for navigation and broad relatedness. Use hidden semantic edges only for typed claims worth querying. Do not mirror ordinary links into `SEMANTIC_EDGE` with broad labels such as `RELATED_TO`, `PART_OF`, `SOURCE_CONTEXT_FOR`, or folder-specific variants like `MECHANICS_RELATED_TO`; those belong in the `LINKS_TO` layer unless the note supports a stronger relationship.

## Embedded Semantic Edge Format

Add a hidden HTML comment block to a Markdown note, usually near the bottom:

```md
<!-- semantic-edges
{"source":"D'Alembert's Principle","relation":"EXTENDS","target":"Virtual Work","evidence_heading":"D'Alembert's Principle","evidence_summary":"Extends virtual work from statics to dynamics by adding inertial forces.","confidence":0.95}
-->
```

Inside the block, use JSON Lines: one complete JSON object per line. Blank lines are ignored. The block is hidden in Markdown/Obsidian preview but stays available to scripts.

Required fields:

- `source`: source concept name.
- `relation`: uppercase relationship type.
- `target`: target concept name.

Optional but strongly recommended fields:

- `evidence_heading`: heading inside that note.
- `evidence_summary`: short original-language reason for the relationship.
- `confidence`: number from `0.0` to `1.0`.

The build script adds `evidence_path` automatically from the Markdown file that contains the block.

### Evidence Fields

Treat `evidence_heading` and `evidence_summary` as the citation for the edge.

- `evidence_heading` should usually match a real heading in the same note, or the nearest useful section heading when the evidence is in a table, list, overview, exercise answer, or short note section.
- Use headings such as `Overview`, `Big Ideas`, `D'Alembert's Principle`, `Exercise Answers`, or `2.2.3 Quantum Measurement` when they help a reader find the supporting text quickly.
- Avoid vague locator labels such as `Evidence`, `Misc`, `Important`, `See above`, or labels that do not exist anywhere near the supporting text.
- `evidence_summary` should explain why the source, relation, and target are connected. It should not merely restate the triple in sentence form.
- Keep the summary short, original, and specific enough that the edge can be audited later without rereading the whole note.

Use stable concept names that match durable note titles when possible. Relation names should be specific enough to query but not so specialized that every edge invents a new type.

Avoid semantic edges that only say two notes are near each other, in the same folder, or linked in Markdown. A good semantic edge should answer "how are these ideas related?" in a way that can be defended from the evidence summary.

## Relation Vocabulary

Use a small vocabulary before inventing a new relation type.

Derivation:

- `DERIVES`
- `DERIVES_FROM`

Concept hierarchy:

- `GENERALIZES`
- `SPECIALIZES`
- `EXTENDS`

Dependency:

- `REQUIRES`
- `ASSUMES`
- `ENABLES`
- `DETERMINES`

Interpretation:

- `REFORMULATES`
- `REPRESENTS`
- `VISUALIZES`

Contrast and removal:

- `CONTRASTS_WITH`
- `ELIMINATES`

Pedagogy and source role:

- `INTRODUCES`
- `MOTIVATES`
- `EXAMPLE_OF`

## Edge Quality Rules

- Do not create semantic edges merely because two notes are linked, near each other, or in the same folder.
- Every semantic edge should answer: "How are these ideas related?"
- Every edge needs an `evidence_heading` and an `evidence_summary`.
- Use stable concept names that match durable note titles when possible.
- Prefer fewer strong edges over many weak edges.
- If a relationship feels like `RELATED_TO`, leave it as a Markdown link only.

## Update Workflow

1. Pick one domain, book cluster, or focused concept.
2. Read the target note completely.
3. Read directly linked notes that define, motivate, or receive the main ideas.
4. Add or revise only edges supported by the note text.
5. Rebuild Kuzu:

```powershell
python scripts\kuzu_build.py
```

6. Re-export the viewer:

```powershell
python scripts\kuzu_export_viewer.py
```

7. Spot-check focused queries for the edited concepts.

## Setup

Install Kuzu for the active Python interpreter:

```powershell
python -m pip install --user kuzu
```

## Build

```powershell
python scripts\kuzu_build.py
```

## Query

List known concepts:

```powershell
python scripts\kuzu_query.py --list
```

Inspect a concept's semantic neighborhood:

```powershell
python scripts\kuzu_query.py "D'Alembert's Principle"
```

Inspect links for a note:

```powershell
python scripts\kuzu_query.py "Book Notes/Coopersmith/Chapter 5/Chapter Overview.md" --note
```

Inspect both layers:

```powershell
python scripts\kuzu_query.py "D'Alembert's Principle" --all
```

## Viewer

Export the graph to the static viewer:

```powershell
python scripts\kuzu_export_viewer.py
```

Serve the vault root so the browser can load `graph.json`:

```powershell
python -m http.server 8765
```

Then open:

```text
http://localhost:8765/Graph/viewer/
```

The viewer is dependency-free and reads `Graph/viewer/graph.json`, which is ignored because it can be regenerated from Kuzu.

## Workflow

- Markdown notes remain the human-readable source.
- Standard Markdown links become `LINKS_TO` edges automatically.
- Hidden `semantic-edges` blocks store curated relationship claims near the notes that justify them.
- Every edge should point back to note evidence through `evidence_heading` and `evidence_summary`.
- Rebuild `Graph/kuzu-db/` after editing semantic-edge blocks.

See [Semantic Edge Audit](semantic-edge-audit.md) for domain progress tracking.
