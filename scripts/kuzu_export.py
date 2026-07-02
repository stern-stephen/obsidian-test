from __future__ import annotations

import argparse
import json
import re
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import kuzu


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DB = ROOT / "Graph" / "kuzu-db"
DEFAULT_VIEWER_JSON_OUTPUT = ROOT / "Graph" / "viewer" / "graph.json"
DEFAULT_GRAPHML_OUTPUT = ROOT / "Graph" / "exports" / "graph.graphml"
GRAPHML_NAMESPACE = "http://graphml.graphdrawing.org/xmlns"


@dataclass
class ExportGraph:
    metadata: dict[str, Any]
    nodes: list[dict[str, Any]]
    edges: list[dict[str, Any]]


def rows(result: kuzu.QueryResult) -> list[list[Any]]:
    out: list[list[Any]] = []
    while result.has_next():
        out.append(result.get_next())
    return out


def add_node(nodes: dict[str, dict[str, Any]], node_id: str, label: str, kind: str, **properties: Any) -> None:
    if node_id not in nodes:
        nodes[node_id] = {"id": node_id, "label": label, "kind": kind, **properties}


def default_output(export_format: str) -> Path:
    if export_format == "viewer-json":
        return DEFAULT_VIEWER_JSON_OUTPUT
    if export_format == "graphml":
        return DEFAULT_GRAPHML_OUTPUT
    raise ValueError(f"Unsupported export format: {export_format}")


def output_extension(export_format: str) -> str:
    if export_format == "viewer-json":
        return ".json"
    if export_format == "graphml":
        return ".graphml"
    raise ValueError(f"Unsupported export format: {export_format}")


def slugify(value: str) -> str:
    slug = re.sub(r"[^A-Za-z0-9]+", "-", value).strip("-").lower()
    return slug or "focused-graph"


def default_focused_output(export_format: str, concept: str, depth: int) -> Path:
    filename = f"{slugify(concept)}-depth-{depth}{output_extension(export_format)}"
    return ROOT / "Graph" / "exports" / filename


def read_kuzu_graph(db_path: Path) -> ExportGraph:
    if not db_path.exists():
        raise SystemExit(f"Database not found: {db_path}. Run scripts/kuzu_build.py first.")

    db = kuzu.Database(str(db_path), read_only=True)
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

    metadata = {
        "node_count": len(nodes),
        "edge_count": len(edges),
        "semantic_edge_count": sum(1 for edge in edges if edge["layer"] == "semantic"),
        "markdown_link_count": sum(1 for edge in edges if edge["layer"] == "links"),
        "relations": sorted({edge["relation"] for edge in edges}),
    }
    return ExportGraph(metadata=metadata, nodes=list(nodes.values()), edges=edges)


def edge_layers(layer: str) -> set[str]:
    if layer == "all":
        return {"semantic", "links"}
    return {layer}


def summarize_graph(nodes: list[dict[str, Any]], edges: list[dict[str, Any]], extra: dict[str, Any] | None = None) -> dict[str, Any]:
    metadata = {
        "node_count": len(nodes),
        "edge_count": len(edges),
        "semantic_edge_count": sum(1 for edge in edges if edge["layer"] == "semantic"),
        "markdown_link_count": sum(1 for edge in edges if edge["layer"] == "links"),
        "relations": sorted({edge["relation"] for edge in edges}),
    }
    if extra:
        metadata.update(extra)
    return metadata


def filter_neighborhood(graph: ExportGraph, concept: str, depth: int, layer: str) -> ExportGraph:
    if depth < 0:
        raise SystemExit("--depth must be zero or greater.")

    start_id = f"concept:{concept}"
    nodes_by_id = {node["id"]: node for node in graph.nodes}
    if start_id not in nodes_by_id:
        raise SystemExit(f"Concept not found: {concept!r}. Run scripts/kuzu_query.py --list to inspect available concepts.")

    layers = edge_layers(layer)
    candidate_edges = [edge for edge in graph.edges if edge["layer"] in layers]
    adjacency: dict[str, set[str]] = {}
    for edge in candidate_edges:
        adjacency.setdefault(edge["source"], set()).add(edge["target"])
        adjacency.setdefault(edge["target"], set()).add(edge["source"])

    visited = {start_id}
    frontier = {start_id}
    for _ in range(depth):
        next_frontier: set[str] = set()
        for node_id in frontier:
            next_frontier.update(adjacency.get(node_id, set()) - visited)
        visited.update(next_frontier)
        frontier = next_frontier

    filtered_edges = [edge for edge in candidate_edges if edge["source"] in visited and edge["target"] in visited]
    filtered_nodes = [node for node in graph.nodes if node["id"] in visited]
    metadata = summarize_graph(
        filtered_nodes,
        filtered_edges,
        {
            "filtered": True,
            "center_concept": concept,
            "depth": depth,
            "layer_filter": layer,
        },
    )
    return ExportGraph(metadata=metadata, nodes=filtered_nodes, edges=filtered_edges)


def write_viewer_json(graph: ExportGraph, output: Path) -> None:
    payload = {"metadata": graph.metadata, "nodes": graph.nodes, "edges": graph.edges}
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")


def graphml_type(value: Any) -> str:
    if isinstance(value, bool):
        return "boolean"
    if isinstance(value, int):
        return "long"
    if isinstance(value, float):
        return "double"
    return "string"


def collect_graphml_keys(graph: ExportGraph) -> dict[tuple[str, str], str]:
    keys: dict[tuple[str, str], str] = {}
    for scope, records in (("node", graph.nodes), ("edge", graph.edges)):
        for record in records:
            for name, value in record.items():
                if name in {"source", "target"}:
                    continue
                key = (scope, name)
                if key not in keys:
                    keys[key] = graphml_type(value)
    return keys


def add_data(parent: ET.Element, key_id: str, value: Any) -> None:
    data = ET.SubElement(parent, f"{{{GRAPHML_NAMESPACE}}}data", {"key": key_id})
    data.text = "" if value is None else str(value)


def write_graphml(graph: ExportGraph, output: Path) -> None:
    ET.register_namespace("", GRAPHML_NAMESPACE)
    root = ET.Element(f"{{{GRAPHML_NAMESPACE}}}graphml")
    keys = collect_graphml_keys(graph)
    key_ids: dict[tuple[str, str], str] = {}

    for index, ((scope, name), attr_type) in enumerate(sorted(keys.items())):
        key_id = f"d{index}"
        key_ids[(scope, name)] = key_id
        ET.SubElement(
            root,
            f"{{{GRAPHML_NAMESPACE}}}key",
            {"id": key_id, "for": scope, "attr.name": name, "attr.type": attr_type},
        )

    graph_el = ET.SubElement(root, f"{{{GRAPHML_NAMESPACE}}}graph", {"id": "vault", "edgedefault": "directed"})
    node_xml_ids = {node["id"]: f"n{index}" for index, node in enumerate(graph.nodes)}

    for node in graph.nodes:
        node_el = ET.SubElement(graph_el, f"{{{GRAPHML_NAMESPACE}}}node", {"id": node_xml_ids[node["id"]]})
        for name, value in node.items():
            add_data(node_el, key_ids[("node", name)], value)

    for index, edge in enumerate(graph.edges):
        edge_el = ET.SubElement(
            graph_el,
            f"{{{GRAPHML_NAMESPACE}}}edge",
            {
                "id": f"e{index}",
                "source": node_xml_ids[edge["source"]],
                "target": node_xml_ids[edge["target"]],
            },
        )
        for name, value in edge.items():
            if name in {"source", "target"}:
                continue
            add_data(edge_el, key_ids[("edge", name)], value)

    output.parent.mkdir(parents=True, exist_ok=True)
    ET.ElementTree(root).write(output, encoding="utf-8", xml_declaration=True)


def main() -> None:
    parser = argparse.ArgumentParser(description="Export the local Kuzu graph.")
    parser.add_argument("--db", type=Path, default=DEFAULT_DB)
    parser.add_argument("--format", choices=["viewer-json", "graphml"], default="viewer-json")
    parser.add_argument("--output", type=Path, help="Output path. Defaults depend on --format.")
    parser.add_argument("--concept", help="Export only a focused neighborhood around this concept.")
    parser.add_argument("--depth", type=int, default=1, help="Neighborhood depth when --concept is set.")
    parser.add_argument("--layer", choices=["semantic", "links", "all"], default="semantic", help="Edge layer to traverse when --concept is set.")
    args = parser.parse_args()

    graph = read_kuzu_graph(args.db)
    if args.concept:
        graph = filter_neighborhood(graph, args.concept, args.depth, args.layer)
        output = args.output or default_focused_output(args.format, args.concept, args.depth)
    else:
        output = args.output or default_output(args.format)

    if args.format == "viewer-json":
        write_viewer_json(graph, output)
    elif args.format == "graphml":
        write_graphml(graph, output)
    else:
        raise SystemExit(f"Unsupported export format: {args.format}")

    print(
        f"Exported {graph.metadata['node_count']} node(s), "
        f"{graph.metadata['semantic_edge_count']} semantic edge(s), "
        f"and {graph.metadata['markdown_link_count']} Markdown link(s) to {output}."
    )


if __name__ == "__main__":
    main()
