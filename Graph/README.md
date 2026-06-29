# Semantic Graph Prototype

This folder holds a small Kuzu-based semantic graph experiment.

The durable source is hidden `semantic-edges` blocks embedded in Markdown notes. Each JSON line inside a block is one authored semantic edge with source, relation, target, evidence, and confidence.

The local Kuzu database lives at `Graph/kuzu-db/` and is ignored by Git because it can be rebuilt from the Markdown files.

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

Use stable concept names that match durable note titles when possible. Relation names should be specific enough to query but not so specialized that every edge invents a new type.

Suggested relation vocabulary:

- `INTRODUCES`
- `DOCUMENTS`
- `EXTENDS`
- `GENERALIZES`
- `SPECIALIZES`
- `DERIVES`
- `DERIVES_FROM`
- `MOTIVATES`
- `ENABLES`
- `USES`
- `ASSUMES`
- `CONTRASTS_WITH`
- `ANALOGOUS_TO`
- `EXAMPLE_OF`
- `REPRESENTS_STATE_OF`
- `COORDINATIZE`

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

## Workflow

- Markdown notes remain the human-readable source.
- Hidden `semantic-edges` blocks store curated relationship claims near the notes that justify them.
- Every edge should point back to note evidence through `evidence_heading` and `evidence_summary`.
- Rebuild `Graph/kuzu-db/` after editing semantic-edge blocks.
