from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

import kuzu


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DB = ROOT / "Graph" / "kuzu-db"
DEFAULT_OUTPUT = ROOT / "Graph" / "viewer" / "graph.json"


def rows(result: kuzu.QueryResult) -> list[list[Any]]:
    out: list[list[Any]] = []
    while result.has_next():
        out.append(result.get_next())
    return out


def add_node(nodes: dict[str, dict[str, Any]], node_id: str, label: str, kind: str, **properties: Any) -> None:
    if node_id not in nodes:
        nodes[node_id] = {"id": node_id, "label": label, "kind": kind, **properties}


def main() -> None:
    parser = argparse.ArgumentParser(description="Export the local Kuzu graph for the static graph viewer.")
    parser.add_argument("--db", type=Path, default=DEFAULT_DB)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    if not args.db.exists():
        raise SystemExit(f"Database not found: {args.db}. Run scripts/kuzu_build.py first.")

    db = kuzu.Database(str(args.db), read_only=True)
    conn = kuzu.Connection(db)
    nodes: dict[str, dict[str, Any]] = {}
    edges: list[dict[str, Any]] = []

    for name, in rows(conn.execute("MATCH (c:Concept) RETURN c.name ORDER BY c.name")):
        add_node(nodes, f"concept:{name}", str(name), "concept")

    for path, title in rows(conn.execute("MATCH (n:Note) RETURN n.path, n.title ORDER BY n.path")):
        add_node(nodes, f"note:{path}", str(title), "note", path=str(path))

    semantic_result = conn.execute(
        """
        MATCH (source:Concept)-[edge:SEMANTIC_EDGE]->(target:Concept)
        RETURN source.name, edge.relation, target.name, edge.evidence_path,
               edge.evidence_heading, edge.evidence_summary, edge.confidence
        """
    )
    for index, (source, relation, target, evidence_path, evidence_heading, evidence_summary, confidence) in enumerate(rows(semantic_result)):
        edges.append(
            {
                "id": f"semantic:{index}",
                "source": f"concept:{source}",
                "target": f"concept:{target}",
                "layer": "semantic",
                "relation": str(relation),
                "label": str(relation),
                "confidence": float(confidence),
                "evidence_path": str(evidence_path),
                "evidence_heading": str(evidence_heading),
                "evidence_summary": str(evidence_summary),
            }
        )

    link_result = conn.execute(
        """
        MATCH (source:Note)-[edge:LINKS_TO]->(target:Note)
        RETURN source.path, edge.label, edge.anchor, target.path
        """
    )
    for index, (source, label, anchor, target) in enumerate(rows(link_result)):
        edges.append(
            {
                "id": f"link:{index}",
                "source": f"note:{source}",
                "target": f"note:{target}",
                "layer": "links",
                "relation": "LINKS_TO",
                "label": str(label),
                "anchor": str(anchor),
                "confidence": 1.0,
            }
        )

    relations = sorted({edge["relation"] for edge in edges})
    payload = {
        "metadata": {
            "node_count": len(nodes),
            "edge_count": len(edges),
            "semantic_edge_count": sum(1 for edge in edges if edge["layer"] == "semantic"),
            "markdown_link_count": sum(1 for edge in edges if edge["layer"] == "links"),
            "relations": relations,
        },
        "nodes": list(nodes.values()),
        "edges": edges,
    }

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
    print(
        f"Exported {payload['metadata']['node_count']} node(s), "
        f"{payload['metadata']['semantic_edge_count']} semantic edge(s), "
        f"and {payload['metadata']['markdown_link_count']} Markdown link(s) to {args.output}."
    )


if __name__ == "__main__":
    main()
