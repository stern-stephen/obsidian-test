# Semantic Graph Prototype

This folder holds the Kuzu-based graph prototype for the vault.

The durable source is ordinary Markdown plus authored hidden `semantic-edges` blocks in notes. The semantic-edge authoring convention lives in [Semantic Edges](../Conventions/Semantic%20Edges.md). This folder documents the compiled graph layer: how that source is built into Kuzu, queried, and exported for the viewer.

```text
Markdown notes + semantic-edge blocks
        -> Graph/kuzu-db
        -> Graph/viewer/graph.json
        -> Graph/exports/graph.graphml
```

The local Kuzu database lives at `Graph/kuzu-db/` and is ignored by Git because it can be rebuilt from the Markdown files.

## Graph Layers

The Kuzu graph contains two layers:

- Automatic structural links: `(:Note)-[:LINKS_TO]->(:Note)` from standard Markdown links.
- Curated semantic edges: `(:Concept)-[:SEMANTIC_EDGE {relation: "..."}]->(:Concept)` from hidden `semantic-edges` blocks.

Markdown links remain the human-readable navigation layer. Semantic edges remain the authored typed-claim layer. Kuzu is the compiled query layer.

## How Markdown Becomes Kuzu

`scripts\kuzu_build.py` compiles the Markdown source into `Graph/kuzu-db`.

The conversion rules are:

- Each Markdown file becomes a `Note` node.
- Standard Markdown links become `LINKS_TO` note edges.
- Each JSON line inside a hidden `semantic-edges` block becomes a typed concept relationship.
- `source` and `target` become `Concept` nodes when needed.
- `relation` becomes the `relation` property on the `SEMANTIC_EDGE`.
- `evidence_heading`, `evidence_summary`, and `confidence` are copied onto the semantic edge.
- `evidence_path` is added automatically from the Markdown file containing the edge block.

The authored Markdown remains the durable source. `Graph/kuzu-db`, `Graph/viewer/graph.json`, and `Graph/exports/graph.graphml` are rebuildable derived artifacts.

## Build

Rebuild the local Kuzu database from Markdown:

```powershell
python scripts\kuzu_build.py
```

The build script:

- parses standard Markdown links into `LINKS_TO` note edges;
- parses hidden `semantic-edges` blocks into typed concept edges;
- adds `evidence_path` automatically from the Markdown file that contains each semantic edge.

## Query

List known concepts:

```powershell
python scripts\kuzu_query.py --list
```

Inspect a concept's semantic neighborhood:

```powershell
python scripts\kuzu_query.py "D'Alembert's Principle"
```

Inspect Markdown links for a note:

```powershell
python scripts\kuzu_query.py "Book Notes/Coopersmith/Chapter 5/Chapter Overview.md" --note
```

Inspect both layers:

```powershell
python scripts\kuzu_query.py "D'Alembert's Principle" --all
```

## Viewer

Export the graph to the static viewer JSON format:

```powershell
python scripts\kuzu_export.py --format viewer-json
```

Export the graph to GraphML for external graph tools:

```powershell
python scripts\kuzu_export.py --format graphml
```

Serve the vault root so the browser can load `graph.json`:

```powershell
python -m http.server 8765
```

Then open:

```text
http://localhost:8765/Graph/viewer/
```

The viewer is dependency-free and reads `Graph/viewer/graph.json`, which is ignored because it can be regenerated from Kuzu. The GraphML export is written to `Graph/exports/graph.graphml` by default and is also rebuildable from Kuzu.

## Setup

Install Kuzu for the active Python interpreter:

```powershell
python -m pip install --user kuzu
```

## Workflow

- Author notes and semantic edges in Markdown.
- Follow [Semantic Edges](../Conventions/Semantic%20Edges.md) for the edge format, evidence fields, relation vocabulary, and quality rules.
- Rebuild `Graph/kuzu-db/` after editing semantic-edge blocks.
- Re-export `Graph/viewer/graph.json` after rebuilding.
- Export `Graph/exports/graph.graphml` when external graph tooling is useful.
- Spot-check affected concepts with `scripts\kuzu_query.py`.

See [Semantic Edge Audit](semantic-edge-audit.md) for domain progress tracking and quality-pass notes.
