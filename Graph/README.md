# Semantic Graph Prototype

This folder holds the Kuzu-based graph prototype for the vault.

The durable source is ordinary Markdown plus authored hidden `semantic-edges` blocks in notes. The semantic-edge authoring convention lives in [Semantic Edges](../Conventions/Semantic%20Edges.md). This folder documents the compiled graph layer: how that source is built into Kuzu, queried, and exported for the viewer.

```text
Markdown notes + semantic-edge blocks
        -> Graph/kuzu-db
        -> Graph/viewer/graph.json
```

The local Kuzu database lives at `Graph/kuzu-db/` and is ignored by Git because it can be rebuilt from the Markdown files.

## Graph Layers

The Kuzu graph contains two layers:

- Automatic structural links: `(:Note)-[:LINKS_TO]->(:Note)` from standard Markdown links.
- Curated semantic edges: `(:Concept)-[:SEMANTIC_EDGE {relation: "..."}]->(:Concept)` from hidden `semantic-edges` blocks.

Markdown links remain the human-readable navigation layer. Semantic edges remain the authored typed-claim layer. Kuzu is the compiled query layer.

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
- Spot-check affected concepts with `scripts\kuzu_query.py`.

See [Semantic Edge Audit](semantic-edge-audit.md) for domain progress tracking and quality-pass notes.
