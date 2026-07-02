# Semantic Edges

Semantic edges are authored, typed concept relationships embedded in Markdown notes. They are source data for the graph build, not the graph database itself.

The Kuzu graph, viewer export, and query scripts are derived from this authored layer:

```text
Markdown notes + semantic-edge blocks
        -> Kuzu graph database
        -> viewer graph.json
```

## Embedded Semantic Edge Format

Add a hidden HTML comment block to a Markdown note, usually near the bottom:

```md
<!-- example-edge-block
{"source":"D'Alembert's Principle","relation":"EXTENDS","target":"Virtual Work","evidence_heading":"D'Alembert's Principle","evidence_summary":"Extends virtual work from statics to dynamics by adding inertial forces.","confidence":0.95}
-->
```

Inside the block, use JSON Lines: one complete JSON object per line. Blank lines are ignored. The block is hidden in Markdown/Obsidian preview but stays available to scripts.

In actual notes, use `semantic-edges` as the comment marker rather than `example-edge-block`. The example uses a non-parsed marker so this documentation page does not create a real graph edge.

Required fields:

- `source`: source concept name.
- `relation`: uppercase relationship type.
- `target`: target concept name.

Optional but strongly recommended fields:

- `evidence_heading`: heading inside that note.
- `evidence_summary`: short original-language reason for the relationship.
- `confidence`: number from `0.0` to `1.0`.

The graph build script adds `evidence_path` automatically from the Markdown file that contains the block.

## Evidence Fields

Treat `evidence_heading` and `evidence_summary` as the citation for the edge.

- `evidence_heading` should usually match a real heading in the same note, or the nearest useful section heading when the evidence is in a table, list, overview, exercise answer, or short note section.
- Use headings such as `Overview`, `Big Ideas`, `D'Alembert's Principle`, `Exercise Answers`, or `2.2.3 Quantum Measurement` when they help a reader find the supporting text quickly.
- Avoid vague locator labels such as `Evidence`, `Misc`, `Important`, `See above`, or labels that do not exist anywhere near the supporting text.
- `evidence_summary` should explain why the source, relation, and target are connected. It should not merely restate the triple in sentence form.
- Keep the summary short, original, and specific enough that the edge can be audited later without rereading the whole note.

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
- Use relation names that are specific enough to query but not so specialized that every edge invents a new type.
- Prefer fewer strong edges over many weak edges.
- If a relationship feels like `RELATED_TO`, leave it as a Markdown link only.

Use ordinary Markdown links for navigation and broad relatedness. Use semantic edges only for typed claims worth querying.

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
